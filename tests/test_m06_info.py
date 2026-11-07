"""Tests of mymath.info (chapter M06): joint and conditional entropies, mutual information, Kraft, prefix codes,
Jensen's gap.

Oracles: ``scipy.stats.entropy`` (entropies of flattened tables and of marginals), ``sklearn.metrics.
mutual_info_score`` (mutual information from a contingency table, in nats), ``fractions.Fraction`` (exact Kraft
sums), a brute-force comparison of every pair of codewords, and NumPy averages. They describe the expected behaviour
without showing the solution.

    pytest tests/test_m06_info.py              # your code
    pytest tests/test_m06_info.py --impl=ref   # the reference
"""

import ast
import inspect
import math
from fractions import Fraction

import numpy as np
import pytest
from scipy.stats import entropy as scipy_entropy
from sklearn.metrics import mutual_info_score


@pytest.fixture
def info(mymath_module):
    return mymath_module("info")


def _result(call, expected, what=""):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    try:
        return call()
    except NotImplementedError:
        raise                 # a function not written yet: ⏳
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised {type(exc).__name__}: {exc}")


def _expect_value_error(call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ValueError."""
    try:
        result = call()
    except NotImplementedError:
        raise                 # first: a function not written yet stays ⏳
    except ValueError:
        return
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned {result!r}")


def _python_type(got, kind, what):
    assert type(got) is kind, (f"expected {what} to be a Python {kind.__name__} ({kind.__name__}(...)), got "
                               f"{type(got).__module__}.{type(got).__name__}")


# Joint laws used as test cases (rows: X, columns: Y). None of them is an answer of the chapter's exercises.
TABLES = {
    "2x2": [[0.32, 0.08], [0.18, 0.42]],
    "2x3-zeros": [[0.3, 0.0, 0.2], [0.05, 0.25, 0.2]],
    "3x2": [[0.15, 0.05], [0.1, 0.3], [0.0, 0.4]],
    "3x4": [[0.06, 0.04, 0.1, 0.0], [0.12, 0.08, 0.05, 0.15], [0.02, 0.18, 0.1, 0.1]],
    "zero-row": [[0.0, 0.0], [0.45, 0.55]],
}
IDS = list(TABLES)
INVALID = [
    ([[0.5, 0.6], [0.0, -0.1]], "a negative entry"),
    ([[0.5, float("nan")], [0.25, 0.25]], "a nan entry"),
    ([[0.4, 0.4], [0.1, 0.2]], "entries summing to 1.1"),
    ([0.25, 0.25, 0.5], "a 1-D list (a law of one variable)"),
    ([[]], "an empty table"),
]
INVALID_IDS = ["negative", "nan", "sum-1.1", "1-D", "empty"]


def _scipy_h(probs, base=2):
    return float(scipy_entropy(np.asarray(probs, dtype=float).ravel(), base=base))


def test_info_uses_no_ready_made_tool(info):
    """info.py computes its sums itself: neither scipy.stats.entropy nor scikit-learn."""
    try:
        tree = ast.parse(inspect.getsource(info))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names if alias.name.split(".")[0] == "sklearn")
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.split(".")[0] == "sklearn":
                found.add(node.module)
            elif node.module.startswith("scipy.stats") and any(alias.name == "entropy" for alias in node.names):
                found.add("scipy.stats.entropy")
        elif isinstance(node, ast.Attribute) and node.attr == "entropy" and isinstance(node.value, ast.Attribute) \
                and node.value.attr == "stats":
            found.add("scipy.stats.entropy")
    assert not found, (f"expected info.py to use neither scipy.stats.entropy nor scikit-learn (the tests compare your "
                       f"results with them), found {sorted(found)}: write the sums with NumPy")


# ---------------------------------------------------------------- joint_entropy
def test_joint_entropy_docstring_example(info):
    got = _result(lambda: info.joint_entropy([[0.25, 0.25], [0.25, 0.25]]), "2.0")
    assert got == pytest.approx(2.0, abs=1e-12), f"expected 2.0 bits for four equal cells, got {got!r}"


@pytest.mark.parametrize("name", IDS)
def test_joint_entropy_matches_scipy(info, name):
    table = TABLES[name]
    expected = _scipy_h(table)
    got = _result(lambda: info.joint_entropy(table), f"{expected:.6f}", name)
    assert got == pytest.approx(expected, abs=1e-10), (
        f"expected {expected:.10f} bits for the table {name}, got {got!r}: -Σ p log2 p over the positive cells "
        f"(0 log 0 counts as 0)")


@pytest.mark.parametrize("base", [math.e, 10, 3])
def test_joint_entropy_in_another_base(info, base):
    table = TABLES["3x4"]
    expected = _scipy_h(table, base=base)
    got = _result(lambda: info.joint_entropy(table, base=base), f"{expected:.6f}", f"base {base}")
    hint = ("0 log 0 counts as 0: keep only the positive cells (this table has a zero cell)"
            if isinstance(got, float) and math.isnan(got) else "divide the natural logarithms by ln(base)")
    assert got == pytest.approx(expected, abs=1e-10), f"expected {expected:.10f} in base {base}, got {got!r}: {hint}"


def test_joint_entropy_with_zero_cells_has_no_nan(info):
    got = _result(lambda: info.joint_entropy(TABLES["2x3-zeros"]), "a finite number")
    assert math.isfinite(got), f"expected a finite entropy for a table with a zero cell, got {got!r}: 0 log 0 = 0"


def test_joint_entropy_of_a_certain_outcome_is_zero(info):
    got = _result(lambda: info.joint_entropy([[0.0, 1.0], [0.0, 0.0]]), "0.0")
    assert got == 0.0, f"expected 0.0 for a table with a single cell equal to 1, got {got!r}"


@pytest.mark.parametrize("table, why", INVALID, ids=INVALID_IDS)
def test_joint_entropy_refuses_an_invalid_table(info, table, why):
    _expect_value_error(lambda: info.joint_entropy(table), f"joint_entropy of {table!r}", why)


@pytest.mark.parametrize("base", [1, 0.5, -2, float("nan")], ids=["1", "0.5", "-2", "nan"])
def test_joint_entropy_refuses_a_base_not_above_1(info, base):
    why = "the base must be greater than 1" + (
        "; nan <= 1 is False, so test `not base > 1`" if math.isnan(base) else "")
    _expect_value_error(lambda: info.joint_entropy(TABLES["2x2"], base=base), f"joint_entropy(..., base={base})", why)


def test_joint_entropy_returns_a_python_float(info):
    got = _result(lambda: info.joint_entropy(np.array(TABLES["2x2"])), "a float")
    _python_type(got, float, "joint_entropy")


# ---------------------------------------------------------------- conditional_entropy
def test_conditional_entropy_docstring_example(info):
    got = _result(lambda: info.conditional_entropy([[0.25, 0.25], [0.5, 0.0]]), "0.5")
    assert got == pytest.approx(0.5, abs=1e-12), f"expected 0.5 bit, got {got!r}"


@pytest.mark.parametrize("name", IDS)
def test_conditional_entropy_matches_scipy(info, name):
    table = np.asarray(TABLES[name], dtype=float)
    rows = table.sum(axis=1)
    expected = sum(r * _scipy_h(table[k] / r) for k, r in enumerate(rows) if r > 0)   # Σ p(x) H(Y | X = x)
    got = _result(lambda: info.conditional_entropy(TABLES[name]), f"{expected:.6f}", name)
    assert got == pytest.approx(expected, abs=1e-10), (
        f"expected H(Y | X) = {expected:.10f} bits for the table {name}, got {got!r}: the average, weighted by p(x), of "
        f"the entropies of the rows divided by their sums")


def test_conditional_entropy_takes_x_on_the_rows(info):
    table = TABLES["3x2"]
    expected = sum(r * _scipy_h(np.asarray(row) / r) for row in table if (r := sum(row)) > 0)
    other = sum(c * _scipy_h(col / c) for col in np.asarray(table, dtype=float).T if (c := col.sum()) > 0)
    got = _result(lambda: info.conditional_entropy(table), f"{expected:.6f}")
    assert got == pytest.approx(expected, abs=1e-10), (
        f"expected H(Y | X) = {expected:.6f}, with X on the rows, got {got!r}"
        + (": you computed H(X | Y), knowing the column instead of the row" if abs(got - other) < 1e-9 else ""))


def test_conditional_entropy_of_independent_variables_is_the_entropy_of_y(info):
    table = np.outer([0.3, 0.7], [0.5, 0.25, 0.25])
    expected = _scipy_h([0.5, 0.25, 0.25])
    got = _result(lambda: info.conditional_entropy(table), f"{expected:.6f}")
    assert got == pytest.approx(expected, abs=1e-10), (
        f"expected H(Y | X) = H(Y) = {expected:.6f} for independent X and Y, got {got!r}")


def test_conditional_entropy_is_zero_when_x_determines_y(info):
    got = _result(lambda: info.conditional_entropy([[0.2, 0.0, 0.0], [0.0, 0.0, 0.5], [0.0, 0.3, 0.0]]), "0.0")
    assert got == pytest.approx(0.0, abs=1e-12) and got >= 0, (
        f"expected 0.0 when each row has a single positive cell (Y is a function of X), got {got!r}")


def test_conditional_entropy_in_nats(info):
    table = TABLES["3x4"]
    expected = _scipy_h(table, base=math.e) - _scipy_h(np.asarray(table).sum(axis=1), base=math.e)
    got = _result(lambda: info.conditional_entropy(table, base=math.e), f"{expected:.6f}")
    assert got == pytest.approx(expected, abs=1e-10), f"expected {expected:.10f} nats, got {got!r}"


@pytest.mark.parametrize("table, why", INVALID, ids=INVALID_IDS)
def test_conditional_entropy_refuses_an_invalid_table(info, table, why):
    _expect_value_error(lambda: info.conditional_entropy(table), f"conditional_entropy of {table!r}", why)


def test_conditional_entropy_refuses_a_base_not_above_1(info):
    _expect_value_error(lambda: info.conditional_entropy(TABLES["2x2"], base=1), "conditional_entropy(..., base=1)",
                        "the base must be greater than 1")


def test_conditional_entropy_returns_a_python_float(info):
    got = _result(lambda: info.conditional_entropy(np.array(TABLES["3x2"])), "a float")
    _python_type(got, float, "conditional_entropy")


# ---------------------------------------------------------------- mutual_information
def _sklearn_mi_bits(table):
    counts = np.rint(np.asarray(table, dtype=float) * 10 ** 6)        # every table above has 2 decimals at most
    return mutual_info_score(None, None, contingency=counts) / math.log(2)


def test_mutual_information_docstring_example(info):
    got = _result(lambda: info.mutual_information([[0.5, 0.0], [0.0, 0.5]]), "1.0")
    assert got == pytest.approx(1.0, abs=1e-12), f"expected 1.0 bit, got {got!r}"


@pytest.mark.parametrize("name", IDS)
def test_mutual_information_matches_scikit_learn(info, name):
    expected = _sklearn_mi_bits(TABLES[name])
    got = _result(lambda: info.mutual_information(TABLES[name]), f"{expected:.6f}", name)
    assert got == pytest.approx(expected, abs=1e-9), (
        f"expected I(X ; Y) = {expected:.10f} bits for the table {name}, got {got!r}: Σ p(x, y) log2(p(x, y) / (p(x) "
        f"p(y))) over the positive cells")


def test_mutual_information_is_symmetric(info):
    table = TABLES["3x4"]
    a = _result(lambda: info.mutual_information(table), "a number")
    b = _result(lambda: info.mutual_information(np.asarray(table).T), "a number")
    assert a == pytest.approx(b, abs=1e-12), f"expected I(X ; Y) = I(Y ; X): got {a!r} and, transposed, {b!r}"


def test_mutual_information_of_independent_variables_is_zero(info):
    table = np.outer([0.15, 0.35, 0.5], [0.6, 0.1, 0.3])
    got = _result(lambda: info.mutual_information(table), "0.0")
    assert 0.0 <= got <= 1e-12, (f"expected 0.0 (up to 1e-12) and never negative for independent variables, got "
                                 f"{got!r}: a tiny negative rounding error, above -1e-12, is returned as 0.0 (the "
                                 f"docstring)")


def test_mutual_information_of_y_equal_to_x_is_the_entropy_of_x(info):
    table = np.diag([0.1, 0.2, 0.3, 0.4])
    expected = _scipy_h([0.1, 0.2, 0.3, 0.4])
    got = _result(lambda: info.mutual_information(table), f"{expected:.6f}")
    assert got == pytest.approx(expected, abs=1e-10), (
        f"expected I(X ; X) = H(X) = {expected:.6f} for a diagonal table, got {got!r}")


def test_mutual_information_in_nats(info):
    table = TABLES["2x3-zeros"]
    expected = _sklearn_mi_bits(table) * math.log(2)
    got = _result(lambda: info.mutual_information(table, base=math.e), f"{expected:.6f}")
    assert got == pytest.approx(expected, abs=1e-9), f"expected {expected:.10f} nats, got {got!r}"


@pytest.mark.parametrize("table, why", INVALID, ids=INVALID_IDS)
def test_mutual_information_refuses_an_invalid_table(info, table, why):
    _expect_value_error(lambda: info.mutual_information(table), f"mutual_information of {table!r}", why)


def test_mutual_information_refuses_a_base_not_above_1(info):
    _expect_value_error(lambda: info.mutual_information(TABLES["2x2"], base=0.5), "mutual_information(..., base=0.5)",
                        "the base must be greater than 1")


def test_mutual_information_returns_a_python_float(info):
    got = _result(lambda: info.mutual_information(np.array(TABLES["2x2"])), "a float")
    _python_type(got, float, "mutual_information")


# ---------------------------------------------------------------- kraft_sum
def test_kraft_sum_docstring_example(info):
    got = _result(lambda: info.kraft_sum([1, 2, 3, 3]), "1.0")
    assert got == 1.0, f"expected 1.0, got {got!r}"


@pytest.mark.parametrize("lengths, alphabet", [([2, 3, 3, 3, 4, 5], 2), ([1, 4, 4, 4, 6], 2), ([2, 2, 2, 3, 3], 2),
                                               ([1, 2, 2, 2, 3], 3), ([3] * 20, 4), ([40, 40], 2)],
                         ids=["binary-a", "binary-b", "complete", "ternary", "quaternary", "long"])
def test_kraft_sum_matches_fractions(info, lengths, alphabet):
    expected = float(sum(Fraction(1, alphabet ** n) for n in lengths))
    got = _result(lambda: info.kraft_sum(lengths, alphabet), f"{expected!r}")
    assert got == pytest.approx(expected, rel=1e-12, abs=0), (
        f"expected {expected!r} for the lengths {lengths} and an alphabet of {alphabet} symbols, got {got!r}: one term "
        f"{alphabet}**(-length) per codeword")


def test_kraft_sum_accepts_a_numpy_array(info):
    try:
        got = info.kraft_sum(np.array([2, 2, 3, 3, 3]))
    except NotImplementedError:
        raise
    except ValueError as exc:
        if "negative integer powers" in str(exc):
            pytest.fail("expected 0.875 for np.array([2, 2, 3, 3, 3]), but NumPy refuses an integer to a negative "
                        "integer power (np.int64(2) ** -3): convert each length with int(...), or the base with "
                        "float(...)")
        pytest.fail(f"expected 0.875 for np.array([2, 2, 3, 3, 3]), but it raised ValueError: {exc}")
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        pytest.fail(f"expected 0.875 for np.array([2, 2, 3, 3, 3]), but it raised {type(exc).__name__}: {exc}")
    assert got == pytest.approx(0.875, abs=1e-15), f"expected 0.875, got {got!r}"


@pytest.mark.parametrize("lengths, alphabet, why", [([], 2, "no length at all"), ([1, 0, 2], 2, "a length of 0"),
                                                    ([2, -1], 2, "a negative length"), ([1, 2], 1, "an alphabet of 1")],
                         ids=["empty", "zero", "negative", "alphabet-1"])
def test_kraft_sum_refuses_invalid_input(info, lengths, alphabet, why):
    _expect_value_error(lambda: info.kraft_sum(lengths, alphabet), f"kraft_sum({lengths}, {alphabet})", why)


def test_kraft_sum_returns_a_python_float(info):
    got = _result(lambda: info.kraft_sum([1, 1]), "a float")
    _python_type(got, float, "kraft_sum")


# ---------------------------------------------------------------- is_prefix_code
def _brute_force_prefix(words):
    return not any(i != j and b.startswith(a) for i, a in enumerate(words) for j, b in enumerate(words))


def test_is_prefix_code_docstring_examples(info):
    a = _result(lambda: info.is_prefix_code(["0", "10", "110", "111"]), "True")
    b = _result(lambda: info.is_prefix_code(["0", "01", "11"]), "False")
    assert a is True and b is False, f"expected True then False (the docstring examples), got {a!r} and {b!r}"


@pytest.mark.parametrize("words", [["11", "10", "01", "000", "001"], ["1", "01", "001", "0001"],
                                   ["00", "010", "0100", "11"], ["0110", "011", "1"], ["2", "10", "11", "12"],
                                   ["101", "100", "11", "0"]],
                         ids=["prefix-5", "prefix-chain", "prefix-inside", "start-of-another", "ternary", "unsorted"])
def test_is_prefix_code_matches_a_brute_force_check(info, words):
    expected = _brute_force_prefix(words)
    got = _result(lambda: info.is_prefix_code(words), f"{expected}")
    assert got == expected, (f"expected {expected} for {words}, got {got!r}: compare every word with every other "
                             f"(str.startswith), whatever their order in the list")


def test_is_prefix_code_on_random_codes(info):
    rng = np.random.default_rng(606)
    for _ in range(40):
        words = ["".join(rng.choice(["0", "1"], size=rng.integers(1, 6))) for _ in range(rng.integers(2, 9))]
        expected = _brute_force_prefix(words)
        got = _result(lambda: info.is_prefix_code(words), f"{expected}", f"{words}")
        assert got == expected, f"expected {expected} for {words}, got {got!r}"


def test_is_prefix_code_refuses_a_repeated_word(info):
    got = _result(lambda: info.is_prefix_code(["10", "0", "10"]), "False")
    assert got is False, f"expected False for a code that repeats the word '10' (it starts itself), got {got!r}"


@pytest.mark.parametrize("words, expected", [([], True), (["0101"], True)], ids=["empty", "single"])
def test_is_prefix_code_small_codes(info, words, expected):
    got = _result(lambda: info.is_prefix_code(words), f"{expected}")
    assert got is expected, f"expected {expected} for {words}, got {got!r}"


def test_is_prefix_code_refuses_the_empty_word(info):
    _expect_value_error(lambda: info.is_prefix_code(["0", "", "11"]), "is_prefix_code(['0', '', '11'])",
                        "a codeword is never the empty string")


def test_is_prefix_code_returns_a_python_bool(info):
    got = _result(lambda: info.is_prefix_code(np.array(["0", "10", "11"])), "a bool")
    _python_type(got, bool, "is_prefix_code")


# ---------------------------------------------------------------- jensen_gap
def test_jensen_gap_docstring_example(info):
    got = _result(lambda: info.jensen_gap(lambda x: x ** 2, [1, 3]), "1.0")
    assert got == pytest.approx(1.0, abs=1e-12), f"expected 1.0, got {got!r}"


@pytest.mark.parametrize("name, f, values, weights", [
    ("square", lambda x: x ** 2, [-1.0, 2.0, 5.0], [0.5, 0.3, 0.2]),
    ("exp", math.exp, [0.0, 0.5, 2.0], [0.25, 0.25, 0.5]),
    ("log", math.log, [1.0, 2.0, 8.0], [0.2, 0.6, 0.2]),
    ("cube", lambda x: x ** 3, [-2.0, 1.0, 3.0, 4.0], None),
], ids=["square", "exp", "log", "cube"])
def test_jensen_gap_matches_numpy(info, name, f, values, weights):
    w = np.full(len(values), 1 / len(values)) if weights is None else np.asarray(weights)
    x = np.asarray(values)
    expected = float(np.dot(w, [f(v) for v in x]) - f(float(np.dot(w, x))))
    got = _result(lambda: info.jensen_gap(f, values, weights), f"{expected:.6f}", name)
    assert got == pytest.approx(expected, abs=1e-10), (
        f"expected E[f(X)] − f(E[X]) = {expected:.10f} for f = {name}, got {got!r}"
        + (": E[f(X)] comes first, then f(E[X]) is subtracted" if abs(got + expected) < 1e-9 else ""))


def test_jensen_gap_signs(info):
    convex = _result(lambda: info.jensen_gap(lambda x: abs(x - 1), [0.0, 3.0, 4.0], [0.5, 0.25, 0.25]), "a number")
    concave = _result(lambda: info.jensen_gap(math.sqrt, [1.0, 4.0, 16.0], [0.3, 0.3, 0.4]), "a number")
    assert convex >= 0 and concave <= 0, (f"expected a gap ≥ 0 for a convex f and ≤ 0 for a concave f, got {convex!r} "
                                          f"and {concave!r}")


def test_jensen_gap_of_a_constant_variable_is_zero(info):
    got = _result(lambda: info.jensen_gap(math.exp, [2.5]), "0.0")
    assert got == pytest.approx(0.0, abs=1e-12), f"expected 0.0 when X takes a single value, got {got!r}"


@pytest.mark.parametrize("values, weights, why", [
    ([], None, "no value at all"),
    ([1.0, 2.0], [0.5, 0.25, 0.25], "3 weights for 2 values"),
    ([1.0, 2.0], [1.5, -0.5], "a negative weight"),
    ([1.0, 2.0], [0.5, 0.4], "weights summing to 0.9"),
    ([1.0, 2.0], [float("nan"), 1.0], "a nan weight"),
], ids=["empty", "length", "negative", "sum-0.9", "nan"])
def test_jensen_gap_refuses_invalid_input(info, values, weights, why):
    _expect_value_error(lambda: info.jensen_gap(math.exp, values, weights), f"jensen_gap(exp, {values}, {weights})",
                        why)


def test_jensen_gap_returns_a_python_float(info):
    got = _result(lambda: info.jensen_gap(np.exp, np.array([0.0, 1.0])), "a float")
    _python_type(got, float, "jensen_gap")
