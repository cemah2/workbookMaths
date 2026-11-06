"""Tests of mymath.logic (chapter R4): truth tables, implication, Σ and Π, counterexamples.

Oracles: Python's own evaluation of the formulas over ``itertools.product``, SymPy (``summation``, ``product``),
``math.prod`` and a direct search. They describe the expected behaviour without showing the solution.

    pytest tests/test_r4_logic.py              # your code
    pytest tests/test_r4_logic.py --impl=ref   # the reference
"""

import itertools
import math
import random

import pytest
import sympy as sp

K = sp.Symbol("k", integer=True)


@pytest.fixture
def logic(mymath_module):
    return mymath_module("logic")


def _result(call, expected):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    try:
        return call()
    except NotImplementedError:
        raise                 # a function not written yet: ⏳
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        pytest.fail(f"expected {expected}, but it raised {type(exc).__name__}: {exc}")


def _expect_value_error(call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ValueError."""
    try:
        call()
    except ValueError:
        return
    except NotImplementedError:
        raise
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned a value")


def _table(formula, n):
    """The oracle: every combination, all true first, and the value of the formula."""
    return [(values, bool(formula(*values))) for values in itertools.product([True, False], repeat=n)]


FORMULAS = [
    (1, lambda p: p, "p"),
    (2, lambda p, q: p and not q, "p and not q"),
    (2, lambda p, q: (not p) or q, "(not p) or q"),
    (2, lambda p, q: p == q, "p == q (equivalence)"),
    (3, lambda p, q, r: (p or q) and not r, "(p or q) and not r"),
    (3, lambda p, q, r: p != (q != r), "p xor q xor r"),
    (4, lambda a, b, c, d: (a and b) or (c and d), "(a and b) or (c and d)"),
]


# ---------------------------------------------------------------- truth_table
@pytest.mark.parametrize("n, formula, text", FORMULAS, ids=[f[2] for f in FORMULAS])
def test_truth_table_matches_direct_evaluation(logic, n, formula, text):
    want = _table(formula, n)
    got = _result(lambda: logic.truth_table(formula, n), f"the {2 ** n} rows of the truth table of {text}")
    assert got == want, (
        f"expected truth_table({text}, {n}) == {want} (rows in the order of itertools.product([True, False], "
        f"repeat={n}): all true first), got {got!r}")


def test_truth_table_docstring_example(logic):
    got = _result(lambda: logic.truth_table(lambda p: not p, 1), "[((True,), False), ((False,), True)]")
    assert got == [((True,), False), ((False,), True)], (
        f"expected [((True,), False), ((False,), True)] (the docstring example), got {got!r}")


def test_truth_table_puts_all_true_first(logic):
    got = _result(lambda: logic.truth_table(lambda p, q: p and q, 2), "four rows, (True, True) first")
    firsts = [row[0] for row in got] if isinstance(got, list) else got
    assert firsts == [(True, True), (True, False), (False, True), (False, False)], (
        f"expected the rows (True, True), (True, False), (False, True), (False, False) in this order, got {firsts!r}")


@pytest.mark.parametrize("n", [1, 2, 3, 5])
def test_truth_table_has_two_to_the_n_rows(logic, n):
    got = _result(lambda: logic.truth_table(lambda *values: all(values), n), f"{2 ** n} rows")
    assert isinstance(got, list) and len(got) == 2**n, (
        f"expected a list of 2**{n} = {2 ** n} rows (each variable doubles the number of cases), got "
        f"{len(got) if isinstance(got, list) else got!r}")


def test_truth_table_rows_are_tuples_of_booleans(logic):
    got = _result(lambda: logic.truth_table(lambda p, q: p or q, 2), "rows (values, result)")
    assert all(isinstance(row, tuple) and len(row) == 2 and isinstance(row[0], tuple)
               and all(isinstance(v, bool) for v in row[0]) and isinstance(row[1], bool) for row in got), (
        f"expected rows (values, result): a tuple of booleans, then a boolean, got {got!r}")


@pytest.mark.parametrize("n", [0, -2], ids=["zero", "negative"])
def test_truth_table_needs_a_variable(logic, n):
    _expect_value_error(lambda: logic.truth_table(lambda *values: True, n), f"truth_table(formula, {n})",
                        "a truth table needs at least one variable")


# ---------------------------------------------------------------- implies
@pytest.mark.parametrize("p, q, want", [(True, True, True), (True, False, False), (False, True, True),
                                         (False, False, True)], ids=["VV", "VF", "FV", "FF"])
def test_implies_four_cases(logic, p, q, want):
    got = _result(lambda: logic.implies(p, q), f"implies({p}, {q}) == {want}")
    assert got is want, (f"expected implies({p}, {q}) == {want} (an implication is false only when p is true and "
                         f"q is false), got {got!r}")


def test_implies_returns_a_bool(logic):
    got = _result(lambda: logic.implies(False, True), "the boolean True")
    assert isinstance(got, bool), f"expected the bool True, got {got!r} of type {type(got).__name__}"


def test_implies_is_not_the_converse(logic):
    got = _result(lambda: [logic.implies(True, False), logic.implies(False, True)], "[False, True]")
    assert got == [False, True], (
        f"expected [implies(True, False), implies(False, True)] == [False, True]: p ⇒ q is not q ⇒ p, got {got!r}")


# ---------------------------------------------------------------- sum_over
def test_sum_over_matches_sympy(logic):
    rng = random.Random(4)
    for _ in range(40):
        a, b, c = rng.randint(-5, 5), rng.randint(-5, 5), rng.randint(-9, 9)
        start = rng.randint(-6, 6)
        stop = start + rng.randint(0, 12)
        want = int(sp.summation(a * K**2 + b * K + c, (K, start, stop)))
        got = _result(lambda: logic.sum_over(lambda k: a * k * k + b * k + c, start, stop),
                      f"sum of {a}k² + {b}k + {c} for k = {start}..{stop} == {want}")
        assert got == want, (f"expected sum_over({a}k² + {b}k + {c}, {start}, {stop}) == {want} (both ends included, "
                             f"like sympy.summation), got {got!r}")


@pytest.mark.parametrize("terms, start, stop, want, why", [
    ("k", 1, 100, 5050, "the docstring example"),
    ("1", 1, 10, 10, "ten terms of 1: the stop is included"),
    ("k", 7, 7, 7, "a single term (start == stop)"),
    ("k", 5, 4, 0, "stop < start: an empty sum is 0"),
    ("k", -3, 3, 0, "negative indices are allowed"),
], ids=["docstring", "stop_included", "single_term", "empty_sum", "negative_indices"])
def test_sum_over_special_cases(logic, terms, start, stop, want, why):
    f = (lambda k: k) if terms == "k" else (lambda k: 1)
    got = _result(lambda: logic.sum_over(f, start, stop), f"sum_over({terms}, {start}, {stop}) == {want} ({why})")
    assert got == want, f"expected sum_over({terms}, {start}, {stop}) == {want} ({why}), got {got!r}"


def test_sum_over_keeps_integers(logic):
    got = _result(lambda: logic.sum_over(lambda k: 2 * k, 1, 4), "the int 20")
    assert isinstance(got, int) and got == 20, (
        f"expected the int 20 (2 + 4 + 6 + 8): start the total at 0, not 0.0, got {got!r}")


def test_sum_over_works_with_floats(logic):
    got = _result(lambda: logic.sum_over(lambda k: 0.5**k, 1, 3), "0.875")
    assert got == pytest.approx(0.875), f"expected 0.5 + 0.25 + 0.125 == 0.875, got {got!r}"


# ---------------------------------------------------------------- prod_over
def test_prod_over_matches_sympy(logic):
    rng = random.Random(5)
    for _ in range(40):
        a, c = rng.randint(-3, 3), rng.randint(-4, 4)
        start = rng.randint(-4, 4)
        stop = start + rng.randint(0, 7)
        want = int(sp.product(a * K + c, (K, start, stop)))
        got = _result(lambda: logic.prod_over(lambda k: a * k + c, start, stop),
                      f"product of {a}k + {c} for k = {start}..{stop} == {want}")
        assert got == want, (f"expected prod_over({a}k + {c}, {start}, {stop}) == {want} (both ends included, like "
                             f"sympy.product), got {got!r}")


@pytest.mark.parametrize("start, stop, want, why", [
    (1, 5, 120, "the docstring example"),
    (6, 6, 6, "a single factor"),
    (3, 2, 1, "stop < start: an empty product is 1"),
    (-2, 2, 0, "a zero factor makes the product 0"),
    (-3, -1, -6, "an odd number of negative factors: a negative product"),
], ids=["docstring", "single_factor", "empty_product", "zero_factor", "negative_factors"])
def test_prod_over_special_cases(logic, start, stop, want, why):
    got = _result(lambda: logic.prod_over(lambda k: k, start, stop), f"prod_over(k, {start}, {stop}) == {want} ({why})")
    assert got == want, f"expected prod_over(k, {start}, {stop}) == {want} ({why}), got {got!r}"


def test_prod_over_keeps_integers(logic):
    want = math.prod(range(1, 13))
    got = _result(lambda: logic.prod_over(lambda k: k, 1, 12), f"the int {want}")
    assert isinstance(got, int) and got == want, (
        f"expected the int 12! = {want} (start the product at 1, not 1.0), got {got!r}")


# ---------------------------------------------------------------- find_counterexample
def _first_failure(predicate, n_max):
    return next((n for n in range(n_max + 1) if not predicate(n)), None)


def test_find_counterexample_matches_a_direct_search(logic):
    rng = random.Random(6)
    for _ in range(40):
        m, r, limit = rng.randint(2, 9), rng.randint(0, 8), rng.randint(0, 60)
        predicate = (lambda n: n % m != r % m) if rng.random() < 0.5 else (lambda n: n * n < limit)
        n_max = rng.randint(0, 40)
        want = _first_failure(predicate, n_max)
        got = _result(lambda: logic.find_counterexample(predicate, n_max),
                      f"the first n in 0..{n_max} where the predicate fails, {want}")
        assert got == want, (f"expected find_counterexample(predicate, {n_max}) == {want} (the smallest n from 0 to "
                             f"{n_max} included where the predicate is false, else None), got {got!r}")


@pytest.mark.parametrize("text, predicate, n_max, want", [
    ("n * n < 50", lambda n: n * n < 50, 100, 8),
    ("n > 0", lambda n: n > 0, 10, 0),
    ("n < 20", lambda n: n < 20, 20, 20),
    ("n < 20", lambda n: n < 20, 19, None),
    ("n != 0", lambda n: n != 0, 0, 0),
    ("n >= 0", lambda n: n >= 0, 0, None),
], ids=["docstring", "zero_is_tried", "n_max_is_tried", "holds_up_to_n_max", "n_max_zero_fails", "n_max_zero_holds"])
def test_find_counterexample_special_cases(logic, text, predicate, n_max, want):
    got = _result(lambda: logic.find_counterexample(predicate, n_max),
                  f"find_counterexample({text}, {n_max}) == {want}")
    assert got == want and type(got) is type(want), (
        f"expected find_counterexample({text}, {n_max}) == {want!r} (0 and n_max are both tried; None when the "
        f"statement holds up to n_max), got {got!r}")


def test_find_counterexample_stops_at_the_first_failure(logic):
    def predicate(n):
        if n > 3:
            raise AssertionError("the function went on after the first counterexample, 3")
        return n < 3

    got = _result(lambda: logic.find_counterexample(predicate, 10), "3, without trying n = 4")
    assert got == 3, f"expected 3, the first counterexample (the search stops there), got {got!r}"
