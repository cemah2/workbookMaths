"""Tests of mymath.linreg (chapter M09b): normal equations, least squares and ridge, hat matrix, sums of squares,
number of monomials, Huber loss.

Oracles: NumPy (``np.linalg.lstsq``, ``np.linalg.pinv``), scikit-learn (``Ridge``, ``PolynomialFeatures``,
``r2_score``), SciPy (``scipy.special.huber``) and properties (H symmetric and idempotent, SST = SSE + SSR). They
describe the expected behaviour without showing the solution.

    pytest tests/test_m09b_linreg.py              # your code
    pytest tests/test_m09b_linreg.py --impl=ref   # the reference
"""

import ast
import inspect

import numpy as np
import pytest
import scipy.special
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures


@pytest.fixture
def linreg(mymath_module):
    return mymath_module("linreg")


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    try:
        return call()
    except NotImplementedError:
        raise                 # a function not written yet: ⏳
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised {type(exc).__name__}: {exc}"
                    + (f" ({hint})" if hint else ""))


def _expect_value_error(call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ValueError."""
    try:
        result = call()
    except NotImplementedError:
        raise                 # a function not written yet stays ⏳
    except ValueError:
        return
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned {result!r}")


def _array(got, what, shape):
    assert isinstance(got, np.ndarray), (f"expected {what} to be a numpy.ndarray of floats (np.array(...)), got "
                                         f"{type(got).__module__}.{type(got).__name__}")
    assert got.shape == shape, f"expected {what} to have the shape {shape}, got {got.shape}"
    assert np.issubdtype(got.dtype, np.floating), f"expected {what} to hold floats, got the dtype {got.dtype}"


def _show(M):
    return np.array2string(np.asarray(M, dtype=float), precision=4, suppress_small=True).replace("\n", "")


# ---------------------------------------------------------------- no ready-made solver
FORBIDDEN = {"lstsq", "pinv", "inv"}


def test_linreg_uses_no_ready_made_solver(linreg):
    """linreg.py solves with np.linalg.solve only: no lstsq, pinv, inv, SciPy or scikit-learn."""
    try:
        tree = ast.parse(inspect.getsource(linreg))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in FORBIDDEN:
            found.add(f".{node.attr}")
        elif isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names if alias.name.split(".")[0] in ("scipy", "sklearn"))
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.split(".")[0] in ("scipy", "sklearn"):
                found.add(node.module)
            elif node.module.startswith("numpy"):
                found.update(alias.name for alias in node.names if alias.name in FORBIDDEN)
    assert not found, (f"expected linreg.py to solve its systems with np.linalg.solve only (the tests compare with "
                       f"lstsq, pinv and scikit-learn), found {sorted(found)}")


# ---------------------------------------------------------------- data
RNG = np.random.default_rng(919)


def _dataset(seed, n, p, intercept=False):
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, p))
    if intercept:
        X[:, 0] = 1.0
    y = X @ rng.normal(size=p) + 0.3 * rng.normal(size=n)
    return X, y


DATASETS = {   # none is an example of the fiche, of workbookIA 9 or an exercise of the chapter
    "8x3": _dataset(11, 8, 3),
    "20x4-intercept": _dataset(12, 20, 4, intercept=True),
    "one-column": (np.array([[2.0], [-1.0], [0.5], [3.0]]), np.array([3.5, -2.0, 1.5, 5.5])),
    "square-3x3": _dataset(13, 3, 3),
    "50x6": _dataset(14, 50, 6),
}


# ---------------------------------------------------------------- normal_equations
@pytest.mark.parametrize("name", list(DATASETS))
def test_normal_equations_match_numpy(linreg, name):
    X, y = DATASETS[name]
    expected_A, expected_b = X.T @ X, X.T @ y
    got = _result(lambda: linreg.normal_equations(X.tolist(), y.tolist()), "a tuple (XtX, Xty)", name)
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (XtX, Xty) for {name}, got {got!r}"
    A, b = got
    _array(A, f"XtX for {name}", expected_A.shape)
    _array(b, f"Xty for {name}", expected_b.shape)
    assert np.allclose(A, expected_A) and np.allclose(b, expected_b), (
        f"expected XtX = {_show(expected_A)} and Xty = {_show(expected_b)} for {name}, got {_show(A)} and {_show(b)}")


def test_normal_equations_docstring_example(linreg):
    got = _result(lambda: linreg.normal_equations([[1, -1], [1, 0], [1, 1]], [1, 2, 6]), "([[3, 0], [0, 2]], [9, 5])",
                  "the docstring")
    assert np.allclose(got[0], [[3, 0], [0, 2]]) and np.allclose(got[1], [9, 5]), (
        f"expected XtX = [[3, 0], [0, 2]] and Xty = [9, 5] for the docstring example, got {got!r}")


@pytest.mark.parametrize("X, y, why", [
    ([1.0, 2.0, 3.0], [1.0, 2.0, 3.0], "X is a 1-D vector, not a design matrix"),
    ([[1.0, 2.0], [3.0, 4.5], [0.0, 1.0]], [1.0, 2.0], "y has 2 entries for 3 rows"),
    ([[1.0, 2.0], [3.0, 4.5]], [[1.0], [2.0]], "y is a column (2-D), not a vector"),
], ids=["X-1d", "y-length", "y-2d"])
def test_normal_equations_reject_bad_shapes(linreg, X, y, why):
    _expect_value_error(lambda: linreg.normal_equations(X, y), f"normal_equations({X}, {y})", why)


def test_normal_equations_do_not_modify_their_inputs(linreg):
    X, y = DATASETS["8x3"]
    X0, y0 = X.copy(), y.copy()
    _result(lambda: linreg.normal_equations(X, y), "a tuple (XtX, Xty)", "arrays")
    assert np.array_equal(X, X0) and np.array_equal(y, y0), (
        "expected normal_equations to leave X and y unchanged, but one was modified")


# ---------------------------------------------------------------- solve_least_squares
@pytest.mark.parametrize("name", list(DATASETS))
def test_solve_least_squares_matches_lstsq(linreg, name):
    X, y = DATASETS[name]
    expected = np.linalg.lstsq(X, y, rcond=None)[0]
    got = _result(lambda: linreg.solve_least_squares(X, y), f"w = {_show(expected)}", name)
    _array(got, f"w for {name}", expected.shape)
    assert np.allclose(got, expected, rtol=1e-8, atol=1e-10), (
        f"expected w = {_show(expected)} for {name} (the least squares solution of np.linalg.lstsq), got {_show(got)}")


@pytest.mark.parametrize("name, ridge", [("8x3", 0.5), ("20x4-intercept", 3.0), ("one-column", 2.0), ("50x6", 25.0)])
def test_solve_least_squares_ridge_matches_scikit_learn(linreg, name, ridge):
    X, y = DATASETS[name]
    expected = Ridge(alpha=ridge, fit_intercept=False, solver="cholesky").fit(X, y).coef_
    got = _result(lambda: linreg.solve_least_squares(X, y, ridge=ridge), f"w = {_show(expected)}",
                  f"{name} with ridge = {ridge}")
    _array(got, f"w for {name} with ridge = {ridge}", expected.shape)
    assert np.allclose(got, expected, rtol=1e-8, atol=1e-10), (
        f"expected w = {_show(expected)} for {name} with ridge = {ridge} (scikit-learn's Ridge without intercept: every "
        f"coefficient is penalized), got {_show(got)}: add ridge on the diagonal of XᵀX")


def test_solve_least_squares_docstring_examples(linreg):
    X, y = [[1, -1], [1, 0], [1, 1]], [1, 2, 6]
    for ridge, expected in [(0.0, [3.0, 2.5]), (1.0, [2.25, 5 / 3])]:
        got = _result(lambda ridge=ridge: linreg.solve_least_squares(X, y, ridge=ridge), f"{expected}",
                      f"the docstring example with ridge = {ridge}")
        assert np.allclose(np.asarray(got, dtype=float), expected), (
            f"expected w = {expected} for the docstring example with ridge = {ridge}, got {got!r}")


def test_solve_least_squares_ridge_handles_redundant_columns(linreg):
    X = np.array([[1.0, 2.0, 2.0], [0.0, 1.0, 1.0], [3.0, -1.0, -1.0], [2.0, 0.0, 0.0]])   # columns 2 and 3 equal
    y = np.array([1.0, -2.0, 4.0, 0.5])
    expected = Ridge(alpha=1.5, fit_intercept=False, solver="cholesky").fit(X, y).coef_
    got = _result(lambda: linreg.solve_least_squares(X, y, ridge=1.5), f"w = {_show(expected)}",
                  "two equal columns and ridge = 1.5", hint="with ridge > 0, XᵀX + ridge·I is always invertible")
    assert np.allclose(got, expected, rtol=1e-8, atol=1e-10), (
        f"expected w = {_show(expected)} for two equal columns and ridge = 1.5, got {_show(got)}")


def test_solve_least_squares_ridge_with_more_columns_than_rows(linreg):
    rng = np.random.default_rng(15)
    X, y = rng.normal(size=(4, 7)), rng.normal(size=4)
    expected = Ridge(alpha=0.8, fit_intercept=False, solver="cholesky").fit(X, y).coef_
    got = _result(lambda: linreg.solve_least_squares(X, y, ridge=0.8), f"w = {_show(expected)}",
                  "a (4, 7) design matrix and ridge = 0.8")
    _array(got, "w for a (4, 7) design matrix", (7,))
    assert np.allclose(got, expected, rtol=1e-8, atol=1e-10), (
        f"expected w = {_show(expected)} for a (4, 7) design matrix with ridge = 0.8, got {_show(got)}")


@pytest.mark.parametrize("X, y, ridge, why", [
    ([[1.0, 2.0, 2.0], [0.0, 1.0, 1.0], [3.0, -1.0, -1.0]], [1.0, 2.0, 3.0], 0.0,
     "columns 2 and 3 are equal: XᵀX is singular without ridge"),
    ([[1.0, 0.0], [2.0, 0.0], [-1.0, 0.0]], [1.0, 2.0, 3.0], 0.0, "a column of zeros: XᵀX is singular without ridge"),
    ([[1.0, 2.0], [3.0, 4.5], [0.0, 1.0]], [1.0, 2.0, 3.0], -1.0, "ridge must be at least 0"),
    ([[1.0, 2.0], [3.0, 4.5], [0.0, 1.0]], [1.0, 2.0], 0.0, "y has 2 entries for 3 rows"),
], ids=["equal-columns", "zero-column", "negative-ridge", "y-length"])
def test_solve_least_squares_rejects_invalid_problems(linreg, X, y, ridge, why):
    _expect_value_error(lambda: linreg.solve_least_squares(X, y, ridge=ridge),
                        f"solve_least_squares({X}, {y}, ridge={ridge})", why)


def test_solve_least_squares_gradient_vanishes(linreg):
    X, y = DATASETS["20x4-intercept"]
    w = np.asarray(_result(lambda: linreg.solve_least_squares(X, y, ridge=2.0), "the ridge weights",
                           "20x4-intercept with ridge = 2"), dtype=float)
    gradient = -2 * X.T @ (y - X @ w) + 2 * 2.0 * w
    assert np.allclose(gradient, 0, atol=1e-8), (
        f"expected the gradient of ‖y − Xw‖² + 2‖w‖² to vanish at your w, got {_show(gradient)}")


# ---------------------------------------------------------------- hat_matrix
@pytest.mark.parametrize("name", list(DATASETS))
def test_hat_matrix_matches_pinv(linreg, name):
    X, _ = DATASETS[name]
    expected = X @ np.linalg.pinv(X)
    got = _result(lambda: linreg.hat_matrix(X), "the hat matrix", name)
    _array(got, f"H for {name}", expected.shape)
    assert np.allclose(got, expected, atol=1e-9), (
        f"expected H = X (XᵀX)⁻¹ Xᵀ for {name}, of shape {expected.shape}, got entries off by "
        f"{np.max(np.abs(np.asarray(got) - expected)):.1e}")


def test_hat_matrix_properties(linreg):
    X, y = DATASETS["20x4-intercept"]
    H = np.asarray(_result(lambda: linreg.hat_matrix(X), "the hat matrix", "20x4-intercept"), dtype=float)
    assert np.allclose(H, H.T, atol=1e-10), "expected H to be symmetric (H = Hᵀ)"
    assert np.allclose(H @ H, H, atol=1e-9), "expected H to be idempotent (H H = H: projecting twice changes nothing)"
    assert abs(np.trace(H) - 4) < 1e-9, f"expected the trace of H to be p = 4, got {np.trace(H):.6f}"
    fitted = X @ np.linalg.lstsq(X, y, rcond=None)[0]
    assert np.allclose(H @ y, fitted, atol=1e-9), "expected H y to be the fitted values of least squares"


def test_hat_matrix_docstring_example(linreg):
    got = _result(lambda: linreg.hat_matrix([[1], [1]]), "[[0.5, 0.5], [0.5, 0.5]]", "the docstring")
    assert np.allclose(np.asarray(got, dtype=float), [[0.5, 0.5], [0.5, 0.5]]), (
        f"expected [[0.5, 0.5], [0.5, 0.5]] for hat_matrix([[1], [1]]), got {got!r}")


@pytest.mark.parametrize("X, why", [
    ([[1.0, 2.0], [2.0, 4.0], [-1.0, -2.0]], "column 2 is twice column 1: XᵀX is singular"),
    ([1.0, 2.0, 3.0], "a 1-D vector, not a design matrix"),
], ids=["dependent-columns", "1d"])
def test_hat_matrix_rejects_invalid_designs(linreg, X, why):
    _expect_value_error(lambda: linreg.hat_matrix(X), f"hat_matrix({X})", why)


# ---------------------------------------------------------------- residual_decomposition
def _fit(name):
    X, y = DATASETS[name]
    return y, X @ np.linalg.lstsq(X, y, rcond=None)[0]


@pytest.mark.parametrize("name", ["20x4-intercept", "8x3", "50x6"])
def test_residual_decomposition_matches_definitions(linreg, name):
    y, y_hat = _fit(name)
    mean = y.mean()
    expected = (np.sum((y - mean) ** 2), np.sum((y_hat - mean) ** 2), np.sum((y - y_hat) ** 2))
    got = _result(lambda: linreg.residual_decomposition(y, y_hat), "a tuple (sst, sse, ssr)", name)
    assert isinstance(got, tuple) and len(got) == 3, f"expected a tuple (sst, sse, ssr) for {name}, got {got!r}"
    assert all(type(v) is float for v in got), (
        f"expected three Python floats (float(...)), got the types {[type(v).__name__ for v in got]}")
    assert np.allclose(got, expected), (
        f"expected (SST, SSE, SSR) = ({expected[0]:.4f}, {expected[1]:.4f}, {expected[2]:.4f}) for {name}, got "
        f"({got[0]:.4f}, {got[1]:.4f}, {got[2]:.4f}) (all three around the mean of y, the targets)")


def test_residual_decomposition_gives_scikit_learn_r2(linreg):
    y, y_hat = _fit("8x3")
    sst, _, ssr = _result(lambda: linreg.residual_decomposition(y, y_hat), "a tuple (sst, sse, ssr)", "8x3")
    assert abs((1 - ssr / sst) - r2_score(y, y_hat)) < 1e-12, (
        f"expected 1 − SSR / SST = {r2_score(y, y_hat):.6f} (sklearn.metrics.r2_score), got {1 - ssr / sst:.6f}")


def test_residual_decomposition_sst_equals_sse_plus_ssr_with_an_intercept(linreg):
    y, y_hat = _fit("20x4-intercept")
    sst, sse, ssr = _result(lambda: linreg.residual_decomposition(y, y_hat), "a tuple (sst, sse, ssr)",
                            "a least squares fit with a column of ones")
    assert abs(sst - (sse + ssr)) < 1e-9 * max(1.0, sst), (
        f"expected SST = SSE + SSR for a least squares fit with a column of ones, got {sst:.6f} and "
        f"{sse:.6f} + {ssr:.6f}")


def test_residual_decomposition_docstring_example(linreg):
    got = _result(lambda: linreg.residual_decomposition([1, 2, 6], [0.5, 3, 5.5]), "(14.0, 12.5, 1.5)", "the docstring")
    assert np.allclose(got, (14.0, 12.5, 1.5)), f"expected (14.0, 12.5, 1.5) for the docstring example, got {got!r}"


@pytest.mark.parametrize("y, y_hat, why", [
    ([1.0, 2.0, 3.0], [1.0, 2.0], "the lengths differ"),
    ([], [], "no value"),
], ids=["lengths", "empty"])
def test_residual_decomposition_rejects_bad_lengths(linreg, y, y_hat, why):
    _expect_value_error(lambda: linreg.residual_decomposition(y, y_hat), f"residual_decomposition({y}, {y_hat})", why)


# ---------------------------------------------------------------- count_monomials
def _sklearn_count(p, degree, include_constant):
    return PolynomialFeatures(degree, include_bias=include_constant).fit(np.zeros((1, p))).n_output_features_


@pytest.mark.parametrize("p, degree", [(1, 1), (2, 3), (3, 4), (5, 2), (6, 3), (7, 0), (12, 2)])
@pytest.mark.parametrize("include_constant", [False, True])
def test_count_monomials_matches_polynomial_features(linreg, p, degree, include_constant):
    expected = _sklearn_count(p, degree, include_constant) if degree > 0 else int(include_constant)
    got = _result(lambda: linreg.count_monomials(p, degree, include_constant=include_constant), f"{expected}",
                  f"p = {p}, degree = {degree}, include_constant = {include_constant}")
    assert type(got) is int, f"expected a Python int (int(...)), got {type(got).__name__}"
    assert got == expected, (
        f"expected {expected} monomials for p = {p}, degree = {degree}, include_constant = {include_constant} (the "
        f"number of columns of sklearn's PolynomialFeatures), got {got}")


def test_count_monomials_docstring_examples(linreg):
    for args, kwargs, expected in [((4, 2), {}, 14), ((4, 2), {"include_constant": True}, 15), ((1, 5), {}, 5)]:
        got = _result(lambda args=args, kwargs=kwargs: linreg.count_monomials(*args, **kwargs), f"{expected}",
                      f"count_monomials{args} {kwargs}")
        assert got == expected, f"expected {expected} for count_monomials{args} {kwargs}, got {got!r}"


def test_count_monomials_is_exact_for_large_counts(linreg):
    from math import comb
    got = _result(lambda: linreg.count_monomials(60, 9), "an exact int", "p = 60, degree = 9")
    expected = comb(69, 9) - 1
    assert got == expected, f"expected exactly {expected} for p = 60, degree = 9 (an int, no float rounding), got {got}"


@pytest.mark.parametrize("p, degree, why", [(0, 2, "p must be at least 1"), (3, -1, "degree must be at least 0")],
                         ids=["p-0", "degree-negative"])
def test_count_monomials_rejects_invalid_arguments(linreg, p, degree, why):
    _expect_value_error(lambda: linreg.count_monomials(p, degree), f"count_monomials({p}, {degree})", why)


# ---------------------------------------------------------------- huber_loss
HUBER_CASES = {   # (residuals, delta)
    "mixed": (np.array([0.2, -1.7, 3.5, -0.4, 0.0, 2.2]), 1.0),
    "all-small": (np.array([0.3, -0.6, 0.9]), 1.5),
    "all-large": (np.array([-5.0, 4.0, 7.5]), 0.5),
    "random": (RNG.normal(scale=2.0, size=40), 1.3),
}


@pytest.mark.parametrize("name", list(HUBER_CASES))
def test_huber_loss_matches_scipy(linreg, name):
    r, delta = HUBER_CASES[name]
    expected = float(np.mean(scipy.special.huber(delta, r)))
    got = _result(lambda: linreg.huber_loss(r.tolist(), delta=delta), f"{expected:.6f}", f"{name}, delta = {delta}")
    assert type(got) is float, f"expected a Python float (float(...)), got {type(got).__name__}"
    assert abs(got - expected) < 1e-12, (
        f"expected {expected:.6f} for {name} with delta = {delta} (r²/2 if |r| ≤ δ, δ (|r| − δ/2) otherwise, then the "
        f"mean), got {got:.6f}")


def test_huber_loss_docstring_examples(linreg):
    for delta, expected in [(1.0, 1.3125), (4.0, 2.3125)]:
        got = _result(lambda delta=delta: linreg.huber_loss([0.5, -3.0], delta=delta), f"{expected}",
                      f"the docstring example with delta = {delta}")
        assert abs(got - expected) < 1e-12, f"expected {expected} for the docstring example with delta = {delta}, got {got!r}"


def test_huber_loss_is_continuous_at_delta(linreg):
    delta = 0.8
    values = [_result(lambda r=r: linreg.huber_loss([r], delta=delta), "a float", f"r = {r}")
              for r in (delta - 1e-9, delta, delta + 1e-9)]
    assert max(values) - min(values) < 1e-8, (
        f"expected the Huber loss to be continuous at |r| = δ = {delta} (both formulas give δ²/2), got {values}")


@pytest.mark.parametrize("residuals, delta, why", [
    ([], 1.0, "no residual"), ([1.0, -2.0], 0.0, "delta must be positive"), ([1.0], -1.0, "delta must be positive"),
], ids=["empty", "delta-0", "delta-negative"])
def test_huber_loss_rejects_invalid_arguments(linreg, residuals, delta, why):
    _expect_value_error(lambda: linreg.huber_loss(residuals, delta=delta), f"huber_loss({residuals}, delta={delta})",
                        why)
