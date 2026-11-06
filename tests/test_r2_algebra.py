"""Tests of mymath.algebra (chapter R2): linear equations, inequalities, |x - a| = c, 2 x 2 systems.

Oracles: SymPy (``solveset`` on the reals: exact solution sets) and ``numpy.linalg.solve`` for the systems. They
describe the expected behaviour without showing the solution.

    pytest tests/test_r2_algebra.py              # your code
    pytest tests/test_r2_algebra.py --impl=ref   # the reference
"""

import math
import random

import numpy as np
import pytest
import sympy as sp

X = sp.Symbol("x", real=True)
INF = math.inf


@pytest.fixture
def algebra(mymath_module):
    return mymath_module("algebra")


def _expect_value_error(call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ValueError."""
    try:
        call()
    except ValueError:
        return
    except NotImplementedError:
        raise                 # a function not written yet: the notebook shows ⏳, not a failure
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned a value")


def _coefficients(seed, n=60):
    rng = random.Random(seed)
    return [(rng.choice([v for v in range(-9, 10) if v != 0]), rng.randint(-20, 20)) for _ in range(n)]


def _interval_of(sympy_set):
    """The SymPy solution set of an inequality -> (left_closed, low, high, right_closed), or None for the empty set."""
    if sympy_set is sp.S.EmptySet:
        return None
    if sympy_set == sp.S.Reals:
        return (False, -INF, INF, False)
    return (not sympy_set.left_open and sympy_set.start != -sp.oo, float(sympy_set.start),
            float(sympy_set.end), not sympy_set.right_open and sympy_set.end != sp.oo)


def _same_interval(got, want):
    if want is None or got is None:
        return got is want
    if not isinstance(got, (tuple, list)) or len(got) != 4:
        return False
    return (bool(got[0]) == want[0] and bool(got[3]) == want[3]
            and got[1] == pytest.approx(want[1]) and got[2] == pytest.approx(want[2]))


def _show(interval):
    if interval is None:
        return "None (the empty set)"
    left, low, high, right = interval
    return f"{interval!r}, that is {'[' if left else ']'}{low} ; {high}{']' if right else '['}"


# ---------------------------------------------------------------- solve_linear
def test_solve_linear_matches_sympy(algebra):
    for a, b in _coefficients(0):
        want = [float(s) for s in sp.solveset(a * X + b, X, sp.S.Reals)]
        got = algebra.solve_linear(a, b)
        assert isinstance(got, list) and len(got) == 1 and got[0] == pytest.approx(want[0]), (
            f"expected solve_linear({a}, {b}) == [{want[0]}] (one solution, in a list), got {got!r}")


@pytest.mark.parametrize("a, b, want, why", [
    (2, -6, [3.0], "the docstring example"),
    (-4, 0, [0.0], "b = 0: the solution is 0"),
    (0, 5, [], "0x + 5 = 0 never holds: no solution, an empty list"),
    (0, 0, "all", "0x + 0 = 0 always holds: every real number, the string 'all'"),
])
def test_solve_linear_special_cases(algebra, a, b, want, why):
    got = algebra.solve_linear(a, b)
    if isinstance(want, list) and want:
        ok = isinstance(got, list) and len(got) == 1 and got[0] == pytest.approx(want[0])
    else:
        ok = got == want
    assert ok, f"expected solve_linear({a}, {b}) == {want!r} ({why}), got {got!r}"


def test_solve_linear_returns_floats(algebra):
    got = algebra.solve_linear(2, -6)
    assert isinstance(got, list) and isinstance(got[0], float), (
        f"expected [3.0], a list holding a float (divide with /), got {got!r}")


# ---------------------------------------------------------------- solve_linear_inequality
SENSES = {"<": sp.Lt, "<=": sp.Le, ">": sp.Gt, ">=": sp.Ge}


@pytest.mark.parametrize("sense", ["<", "<=", ">", ">="])
def test_solve_linear_inequality_matches_sympy(algebra, sense):
    for a, b in _coefficients(1, n=30):
        want = _interval_of(sp.solveset(SENSES[sense](a * X + b, 0), X, sp.S.Reals))
        got = algebra.solve_linear_inequality(a, b, sense)
        assert _same_interval(got, want), (
            f"expected solve_linear_inequality({a}, {b}, {sense!r}) == {_show(want)}, got {got!r}")


@pytest.mark.parametrize("a, b, sense, want, why", [
    (-2, 4, "<=", (True, 2.0, INF, False), "the docstring example: dividing by -2 reverses the inequality"),
    (3, -6, "<", (False, -INF, 2.0, False), "a positive coefficient keeps the direction, the end is open"),
    (5, 10, ">=", (True, -2.0, INF, False), "a large inequality: the end is included"),
    (0, 1, "<", None, "1 < 0 is never true: the empty set is None"),
    (0, -1, "<", (False, -INF, INF, False), "-1 < 0 is always true: the whole line"),
    (0, 0, "<", None, "0 < 0 is false: strict, so no solution"),
    (0, 0, "<=", (False, -INF, INF, False), "0 <= 0 is true for every x"),
    (0, 1, ">", (False, -INF, INF, False), "1 > 0 is always true: the whole line"),
    (0, -1, ">=", None, "-1 >= 0 is never true: the empty set is None"),
    (0, 0, ">", None, "0 > 0 is false: strict, so no solution"),
    (0, 0, ">=", (False, -INF, INF, False), "0 >= 0 is true for every x"),
    (0, -2, "<=", (False, -INF, INF, False), "-2 <= 0 is always true: the whole line"),
    (0, 2, ">=", (False, -INF, INF, False), "2 >= 0 is always true: the whole line"),
])
def test_solve_linear_inequality_special_cases(algebra, a, b, sense, want, why):
    got = algebra.solve_linear_inequality(a, b, sense)
    assert _same_interval(got, want), (
        f"expected solve_linear_inequality({a}, {b}, {sense!r}) == {_show(want)} ({why}), got {got!r}")


def test_solve_linear_inequality_default_sense_is_strict_less(algebra):
    got = algebra.solve_linear_inequality(1, -3)
    assert _same_interval(got, (False, -INF, 3.0, False)), (
        f"expected solve_linear_inequality(1, -3) == (False, -inf, 3.0, False): the default sense is '<', got {got!r}")


def test_solve_linear_inequality_returns_a_tuple_of_two_bools_and_two_numbers(algebra):
    got = algebra.solve_linear_inequality(1, -3, "<=")
    ok = (isinstance(got, tuple) and len(got) == 4 and isinstance(got[0], bool) and isinstance(got[3], bool)
          and not isinstance(got[1], bool) and not isinstance(got[2], bool))
    assert ok, (f"expected a tuple (left_closed, low, high, right_closed) such as (False, -inf, 3.0, True), with "
                f"True or False at both ends (not 0 or 1, not a list), got {got!r}")


def test_solve_linear_inequality_infinite_ends_are_open(algebra):
    for a, b, sense in [(1, -3, "<="), (-2, 4, ">="), (5, 10, ">=")]:
        got = algebra.solve_linear_inequality(a, b, sense)
        infinite_ends_open = (isinstance(got, (tuple, list)) and len(got) == 4
                              and (got[1] != -INF or not got[0]) and (got[2] != INF or not got[3]))
        assert infinite_ends_open, (f"expected an open bracket on the infinite side (False next to -inf or inf): "
                                    f"an infinite end is never included, got solve_linear_inequality({a}, {b}, "
                                    f"{sense!r}) = {got!r}")


@pytest.mark.parametrize("a, sense", [(1, "="), (1, "=<"), (1, "≤"), (1, "lt"), (0, "="), (0, "≤")],
                         ids=["equals", "reversed_le", "unicode_le", "word", "a0_equals", "a0_unicode_le"])
def test_solve_linear_inequality_invalid_sense_raises(algebra, a, sense):
    _expect_value_error(lambda: algebra.solve_linear_inequality(a, 2, sense),
                        f"solve_linear_inequality({a}, 2, {sense!r})", "the sense must be '<', '<=', '>' or '>='")


# ---------------------------------------------------------------- solve_abs_equation
def test_solve_abs_equation_matches_sympy(algebra):
    rng = random.Random(2)
    for _ in range(40):
        a, c = rng.randint(-20, 20) / 2, rng.randint(-10, 20) / 2
        want = sorted(float(s) for s in sp.solveset(sp.Abs(X - sp.Rational(a)) - sp.Rational(c), X, sp.S.Reals))
        got = algebra.solve_abs_equation(a, c)
        assert isinstance(got, list) and len(got) == len(want) and all(
            g == pytest.approx(w) for g, w in zip(got, want)), (
            f"expected solve_abs_equation({a}, {c}) == {want} (sorted), got {got!r}")


@pytest.mark.parametrize("a, c, want, why", [
    (1, 3, [-2.0, 4.0], "the docstring example: the two points at distance 3 from 1, in increasing order"),
    (1, 0, [1.0], "distance 0: only a itself, once"),
    (-2, 5, [-7.0, 3.0], "a negative centre"),
    (4, -1, [], "a distance is never negative: no solution"),
])
def test_solve_abs_equation_special_cases(algebra, a, c, want, why):
    got = algebra.solve_abs_equation(a, c)
    ok = isinstance(got, list) and len(got) == len(want) and all(g == pytest.approx(w) for g, w in zip(got, want))
    assert ok, f"expected solve_abs_equation({a}, {c}) == {want} ({why}), got {got!r}"


# ---------------------------------------------------------------- solve_2x2
def _systems(seed=3, n=40):
    rng = random.Random(seed)
    out = []
    while len(out) < n:
        A = [[rng.randint(-9, 9) for _ in range(2)] for _ in range(2)]
        if A[0][0] * A[1][1] - A[0][1] * A[1][0] != 0:
            out.append((A, [rng.randint(-20, 20), rng.randint(-20, 20)]))
    return out


def test_solve_2x2_matches_numpy(algebra):
    for A, b in _systems():
        want = np.linalg.solve(np.array(A, dtype=float), np.array(b, dtype=float))
        got = algebra.solve_2x2(A, b)
        ok = isinstance(got, (tuple, list)) and len(got) == 2 and np.allclose(got, want)
        assert ok, f"expected solve_2x2({A}, {b}) == ({want[0]:.6g}, {want[1]:.6g}) like np.linalg.solve, got {got!r}"


@pytest.mark.parametrize("A, b, want, why", [
    ([[1, 1], [1, -1]], [5, 1], (3.0, 2.0), "the docstring example"),
    ([[2, 0], [0, 4]], [6, -8], (3.0, -2.0), "each equation has one unknown"),
    ([[0, 1], [1, 0]], [7, 9], (9.0, 7.0), "a zero on the diagonal: Cramer still works"),
])
def test_solve_2x2_special_cases(algebra, A, b, want, why):
    got = algebra.solve_2x2(A, b)
    ok = isinstance(got, (tuple, list)) and len(got) == 2 and np.allclose(got, want)
    assert ok, f"expected solve_2x2({A}, {b}) == {want} ({why}), got {got!r}"


def test_solve_2x2_returns_a_tuple(algebra):
    got = algebra.solve_2x2([[1, 1], [1, -1]], [5, 1])
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (x, y), (3.0, 2.0), not a list, got {got!r}"


@pytest.mark.parametrize("A, b, why", [
    ([[1, 3], [2, 6]], [3, 5], "parallel lines: no solution"),
    ([[1, 3], [2, 6]], [3, 6], "the same line twice: infinitely many solutions"),
    ([[0, 0], [0, 0]], [0, 0], "no equation at all"),
], ids=["parallel", "same_line", "zero"])
def test_solve_2x2_zero_determinant_raises(algebra, A, b, why):
    _expect_value_error(lambda: algebra.solve_2x2(A, b), f"solve_2x2({A}, {b})",
                        f"the determinant is zero, {why}")
