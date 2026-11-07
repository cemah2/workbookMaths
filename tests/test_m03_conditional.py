"""Tests of mymath.conditional (chapter M03): joint, marginal and conditional laws, independence, AUC by pairs.

Oracles: NumPy sums written out cell by cell, ``fractions.Fraction`` for exact values, and
``sklearn.metrics.roc_auc_score`` for the AUC. They describe the expected behaviour without showing the solution.

    pytest tests/test_m03_conditional.py              # your code
    pytest tests/test_m03_conditional.py --impl=ref   # the reference
"""

import ast
import inspect
from fractions import Fraction

import numpy as np
import pytest
from sklearn.metrics import roc_auc_score

COUNTS = [[30, 10, 20], [15, 45, 30]]           # a 2 × 3 contingency table, total 150
JOINT = [[0.12, 0.08, 0.20], [0.18, 0.12, 0.30]]  # an independent joint law: (0.4, 0.6) × (0.3, 0.2, 0.5)


@pytest.fixture
def conditional(mymath_module):
    return mymath_module("conditional")


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
        result = call()
    except ValueError:
        return
    except NotImplementedError:
        raise
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    shown = result.tolist() if isinstance(result, np.ndarray) else result   # one line, even for an array
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned {shown!r}")


def _truth(got):
    """The truth value of a Python or NumPy bool: the type itself is checked by test_are_independent_returns_a_python_bool
    alone, so that a right value of the wrong type is not reported as a wrong value."""
    return bool(got) if isinstance(got, (bool, np.bool_)) else got


def _float_array(got, shape, what):
    assert isinstance(got, np.ndarray), f"expected {what} to be a numpy.ndarray (np.asarray(...)), got {type(got).__name__}"
    assert got.shape == shape, f"expected {what} of shape {shape}, got shape {got.shape}"
    assert got.dtype.kind == "f", f"expected {what} with a float dtype, got dtype {got.dtype}: use dtype=float"


# ---------------------------------------------------------------- no ready-made tool
def test_conditional_uses_no_sklearn(conditional):
    """conditional.py computes its results itself: no scikit-learn (the tests compare with roc_auc_score)."""
    try:
        tree = ast.parse(inspect.getsource(conditional))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    assert "sklearn" not in imported, (
        "expected conditional.py not to import scikit-learn (the tests compare your results with it): write the sums "
        "and the pair count yourself, NumPy is allowed")


# ---------------------------------------------------------------- joint_from_counts
def test_joint_from_counts_docstring_example(conditional):
    got = _result(lambda: conditional.joint_from_counts([[1, 3], [2, 4]]), "[[0.1, 0.3], [0.2, 0.4]]")
    _float_array(got, (2, 2), "joint_from_counts([[1, 3], [2, 4]])")
    assert np.allclose(got, [[0.1, 0.3], [0.2, 0.4]], rtol=0, atol=1e-12), (
        f"expected [[0.1, 0.3], [0.2, 0.4]] (each count divided by the total 10), got {got.tolist()}")


def test_joint_from_counts_keeps_the_shape_and_sums_to_1(conditional):
    got = _result(lambda: conditional.joint_from_counts(COUNTS), "a 2 × 3 table")
    _float_array(got, (2, 3), "joint_from_counts(a 2 × 3 table)")
    expected = [[Fraction(c, 150) for c in row] for row in COUNTS]
    assert np.allclose(got, np.array(expected, dtype=float), rtol=0, atol=1e-12), (
        f"expected {np.round(np.array(expected, dtype=float), 6).tolist()} (each count / 150, rows kept as rows), "
        f"got {np.asarray(got).round(6).tolist()}")
    assert abs(got.sum() - 1) < 1e-12, f"expected a joint law summing to 1, got a sum of {got.sum()}"


def test_joint_from_counts_accepts_an_array_and_does_not_modify_it(conditional):
    counts = np.array(COUNTS, dtype=int)
    before = counts.copy()
    got = _result(lambda: conditional.joint_from_counts(counts), "a joint law")
    assert np.array_equal(counts, before), "expected the table of counts to stay unchanged (return a new array)"
    assert got.dtype.kind == "f", f"expected a float dtype even for integer counts, got {got.dtype}"


@pytest.mark.parametrize("counts, why", [
    ([1, 2, 3], "a 1-D list is not a table"),
    ([[[1, 2]], [[3, 4]]], "a 3-D table"),
    ([[1, -2], [3, 4]], "a negative count"),
    ([[0, 0], [0, 0]], "only zeros"),
], ids=["1-D", "3-D", "negative", "zeros"])
def test_joint_from_counts_refuses_bad_tables(conditional, counts, why):
    _expect_value_error(lambda: conditional.joint_from_counts(counts), f"joint_from_counts({counts})", why)


# ---------------------------------------------------------------- marginal
def test_marginal_docstring_example(conditional):
    got = _result(lambda: conditional.marginal([[0.1, 0.3], [0.2, 0.4]], axis=0), "[0.3, 0.7]")
    _float_array(got, (2,), "marginal(..., axis=0)")
    assert np.allclose(got, [0.3, 0.7], rtol=0, atol=1e-12), (
        f"expected [0.3, 0.7] (axis=0 adds down each column: the law of Y), got {got.tolist()}")


@pytest.mark.parametrize("axis, expected", [(0, [0.3, 0.2, 0.5]), (1, [0.4, 0.6])], ids=["axis 0", "axis 1"])
def test_marginal_of_a_2_by_3_law(conditional, axis, expected):
    got = _result(lambda: conditional.marginal(JOINT, axis=axis), f"{expected}")
    if isinstance(got, np.ndarray) and got.ndim == 1 and got.shape != (len(expected),):
        pytest.fail(f"expected {expected}, {len(expected)} values for a 2 × 3 law with axis={axis}, got {got.tolist()}: "
                    "axis=0 sums down each column (one value per column, the law of Y); axis=1 sums along each row "
                    "(the law of X)")
    _float_array(got, (len(expected),), f"marginal(a 2 × 3 law, axis={axis})")
    hint = (" (axis=0 sums down each column, one value per column; axis=1 sums along each row)"
            if got.shape == (len(expected),) and not np.allclose(got, expected) else "")
    assert np.allclose(got, expected, rtol=0, atol=1e-12), f"expected {expected}, got {got.tolist()}{hint}"


@pytest.mark.parametrize("joint, axis, why", [
    ([[0.5, 0.6], [0.1, -0.2]], 0, "a negative entry"),
    ([[0.2, 0.3], [0.1, 0.1]], 0, "entries summing to 0.7"),
    ([0.4, 0.6], 0, "a 1-D list is not a joint law"),
    ([[0.1, 0.3], [0.2, 0.4]], 2, "axis must be 0 or 1"),
], ids=["negative", "sum 0.7", "1-D", "axis 2"])
def test_marginal_refuses_bad_input(conditional, joint, axis, why):
    _expect_value_error(lambda: conditional.marginal(joint, axis), f"marginal({joint}, axis={axis})", why)


# ---------------------------------------------------------------- conditional
def test_conditional_docstring_example(conditional):
    got = _result(lambda: conditional.conditional([[0.1, 0.3], [0.2, 0.4]], given_row=0), "[0.25, 0.75]")
    _float_array(got, (2,), "conditional(..., given_row=0)")
    assert np.allclose(got, [0.25, 0.75], rtol=0, atol=1e-12), (
        f"expected [0.25, 0.75] (the row [0.1, 0.3] divided by its sum 0.4), got {got.tolist()}")


def test_conditional_given_a_column(conditional):
    joint = [[0.1, 0.3, 0.05], [0.2, 0.1, 0.25]]
    got = _result(lambda: conditional.conditional(joint, given_column=1), "[0.75, 0.25]")
    _float_array(got, (2,), "conditional(a 2 × 3 law, given_column=1)")
    hint = (" (given_column=j: the column j, one value per row, divided by its sum)"
            if not np.allclose(got, [0.75, 0.25]) else "")
    assert np.allclose(got, [0.75, 0.25], rtol=0, atol=1e-12), f"expected [0.75, 0.25], got {got.tolist()}{hint}"


def test_conditional_given_a_row_of_a_2_by_3_law(conditional):
    joint = [[0.1, 0.3, 0.05], [0.2, 0.1, 0.25]]
    expected = [Fraction(4, 11), Fraction(2, 11), Fraction(5, 11)]
    got = _result(lambda: conditional.conditional(joint, given_row=1), "[4/11, 2/11, 5/11]")
    _float_array(got, (3,), "conditional(a 2 × 3 law, given_row=1)")
    assert np.allclose(got, np.array(expected, dtype=float), rtol=0, atol=1e-12), (
        f"expected [4/11, 2/11, 5/11] (the row [0.2, 0.1, 0.25] divided by its sum 0.55), got {got.tolist()}")
    assert abs(got.sum() - 1) < 1e-12, f"expected a conditional law summing to 1, got a sum of {got.sum()}"


@pytest.mark.parametrize("kwargs, why", [
    ({}, "neither index given"),
    ({"given_row": 0, "given_column": 0}, "both indices given"),
    ({"given_row": 2}, "row index 2 out of range for 2 rows"),
    ({"given_column": 3}, "column index 3 out of range for 3 columns"),
], ids=["none", "both", "row out of range", "column out of range"])
def test_conditional_refuses_bad_indices(conditional, kwargs, why):
    joint = [[0.1, 0.3, 0.05], [0.2, 0.1, 0.25]]
    _expect_value_error(lambda: conditional.conditional(joint, **kwargs), f"conditional(joint, {kwargs})", why)


def test_conditional_refuses_an_event_of_probability_0(conditional):
    _expect_value_error(lambda: conditional.conditional([[0.0, 0.0], [0.5, 0.5]], given_row=0),
                        "conditional([[0, 0], [0.5, 0.5]], given_row=0)", "P(X = x_0) = 0: no conditional law")


def test_conditional_refuses_an_invalid_joint_law(conditional):
    _expect_value_error(lambda: conditional.conditional([[1, 3], [2, 4]], given_row=0),
                        "conditional([[1, 3], [2, 4]], given_row=0)", "counts, not a joint law: they sum to 10")


# ---------------------------------------------------------------- are_independent
def test_are_independent_docstring_examples(conditional):
    got = _result(lambda: conditional.are_independent([[0.06, 0.14], [0.24, 0.56]]), "True")
    assert _truth(got) is True, f"expected True ((0.2, 0.8) × (0.3, 0.7) gives every cell), got {got!r}"
    got = _result(lambda: conditional.are_independent([[0.1, 0.3], [0.2, 0.4]]), "False")
    assert _truth(got) is False, f"expected False (P(X = x_0) P(Y = y_0) = 0.4 × 0.3 = 0.12, not 0.1), got {got!r}"


def test_are_independent_on_a_2_by_3_law(conditional):
    got = _result(lambda: conditional.are_independent(JOINT), "True")
    assert _truth(got) is True, f"expected True (every cell is the product of its two marginals), got {got!r}"


def test_are_independent_checks_every_cell(conditional):
    # the first cell is the product of its marginals (0.5 × 0.4 = 0.2), the others are not
    joint = [[0.2, 0.1, 0.2], [0.2, 0.25, 0.05]]
    got = _result(lambda: conditional.are_independent(joint), "False")
    assert _truth(got) is False, f"expected False (cell [0][1]: 0.5 × 0.35 = 0.175, not 0.1): check every cell, got {got!r}"


def test_are_independent_uses_the_tolerance(conditional):
    joint = [[0.12 + 1e-4, 0.08 - 1e-4, 0.20], [0.18 - 1e-4, 0.12 + 1e-4, 0.30]]
    loose = _result(lambda: conditional.are_independent(joint, tol=1e-3), "True with tol=1e-3")
    strict = _result(lambda: conditional.are_independent(joint), "False with the default tol=1e-9")
    assert _truth(loose) is True, f"expected True with tol=1e-3 (every gap is below 1e-3), got {loose!r}"
    assert _truth(strict) is False, f"expected False with the default tol=1e-9 (some gaps are 1e-4), got {strict!r}"


def test_are_independent_accepts_float_rounding(conditional):
    joint = np.outer([0.1, 0.7, 0.2], [0.3, 0.3, 0.4])        # products computed in floating point
    got = _result(lambda: conditional.are_independent(joint), "True")
    assert _truth(got) is True, (f"expected True: compare with a tolerance (np.abs(...) <= tol), never with ==, got {got!r}")


def test_are_independent_has_no_relative_tolerance(conditional):
    # every cell is 2e-6 away from the product of its marginals (0.5 × 0.5): more than tol = 1e-9, but less than the
    # relative tolerance rtol=1e-5 that np.allclose and np.isclose add by default
    joint = np.outer([0.5, 0.5], [0.5, 0.5]) + np.array([[2e-6, -2e-6], [-2e-6, 2e-6]])
    got = _result(lambda: conditional.are_independent(joint), "False")
    assert _truth(got) is False, (
        f"expected False (every gap is 2e-6, more than the default tol=1e-9), got {got!r}: np.allclose and np.isclose "
        "add a relative tolerance rtol=1e-5 by default; compare np.abs(table - products) <= tol, or pass rtol=0")


def test_are_independent_returns_a_python_bool(conditional):
    got = _result(lambda: conditional.are_independent(JOINT), "True")
    assert type(got) is bool, f"expected a Python bool (bool(...)), got {type(got).__module__}.{type(got).__name__}"


def test_are_independent_refuses_an_invalid_joint_law(conditional):
    _expect_value_error(lambda: conditional.are_independent([[1, 3], [2, 4]]),
                        "are_independent([[1, 3], [2, 4]])", "counts, not a joint law")


# ---------------------------------------------------------------- auc_by_pairs
def test_auc_by_pairs_docstring_example(conditional):
    got = _result(lambda: conditional.auc_by_pairs([0.9, 0.4], [0.3, 0.4]), "0.875")
    assert got == pytest.approx(0.875, abs=1e-12), (
        f"expected 0.875 (3 pairs well ranked and 1 tie counted 1/2, out of 4), got {got!r}")


@pytest.mark.parametrize("seed", [0, 1, 2], ids=["seed 0", "seed 1", "seed 2"])
def test_auc_by_pairs_matches_sklearn_with_ties(conditional, seed):
    rng = np.random.default_rng(seed)
    pos = rng.integers(0, 6, 9) / 5          # scores on a grid of 6 values: many ties
    neg = rng.integers(0, 5, 7) / 5
    expected = roc_auc_score([1] * len(pos) + [0] * len(neg), np.concatenate([pos, neg]))
    got = _result(lambda: conditional.auc_by_pairs(list(pos), list(neg)), f"{expected}")
    assert got == pytest.approx(expected, abs=1e-12), (
        f"expected {expected} (sklearn.metrics.roc_auc_score: a tie counts 1/2), got {got!r}")


def test_auc_by_pairs_extreme_values(conditional):
    perfect = _result(lambda: conditional.auc_by_pairs([0.8, 0.9], [0.1, 0.2, 0.3]), "1.0")
    reversed_ = _result(lambda: conditional.auc_by_pairs([0.1, 0.2], [0.8, 0.9, 0.95]), "0.0")
    ties = _result(lambda: conditional.auc_by_pairs([0.5, 0.5], [0.5]), "0.5")
    assert perfect == pytest.approx(1.0) and reversed_ == pytest.approx(0.0) and ties == pytest.approx(0.5), (
        f"expected 1.0 (every positive above every negative), 0.0 (every positive below) and 0.5 (only ties), got "
        f"{perfect!r}, {reversed_!r} and {ties!r}")


def test_auc_by_pairs_accepts_arrays_and_returns_a_float(conditional):
    got = _result(lambda: conditional.auc_by_pairs(np.array([0.7, 0.2]), np.array([0.5])), "0.5")
    assert type(got) is float, f"expected a Python float (float(...)), got {type(got).__module__}.{type(got).__name__}"
    assert got == pytest.approx(0.5), f"expected 0.5 (one pair well ranked out of 2), got {got!r}"


@pytest.mark.parametrize("pos, neg", [([], [0.3]), ([0.7], [])], ids=["no positive", "no negative"])
def test_auc_by_pairs_refuses_an_empty_list(conditional, pos, neg):
    _expect_value_error(lambda: conditional.auc_by_pairs(pos, neg), f"auc_by_pairs({pos}, {neg})",
                        "no pair can be formed")
