"""Tests of mymath.svm (chapter M13b): a quadratic problem under equality constraints solved by the Lagrange
conditions, the hinge loss, the soft-margin SVM objective and a subgradient, and the RBF and polynomial kernels.

Oracles: SciPy (``scipy.optimize.minimize`` under equality constraints, ``scipy.linalg.null_space``,
``scipy.spatial.distance.cdist``), scikit-learn (``sklearn.metrics.hinge_loss``, ``sklearn.metrics.pairwise``),
``fractions.Fraction`` for exact small problems, and properties (the Lagrange conditions hold, no feasible point does
better, a subgradient gives a lower affine bound, a Gram matrix is symmetric positive semi-definite). They describe the
expected behaviour without showing the solution.

    pytest tests/test_m13b_svm.py              # your code
    pytest tests/test_m13b_svm.py --impl=ref   # the reference
"""

import ast
import inspect
import warnings
from fractions import Fraction

import numpy as np
import pytest
from scipy.linalg import null_space
from scipy.optimize import minimize
from scipy.spatial.distance import cdist
from sklearn.metrics import hinge_loss as sk_hinge_loss
from sklearn.metrics.pairwise import polynomial_kernel as sk_polynomial_kernel
from sklearn.metrics.pairwise import rbf_kernel as sk_rbf_kernel


@pytest.fixture
def svm(mymath_module):
    return mymath_module("svm")


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)
        try:
            return call()
        except NotImplementedError:
            raise                 # a function not written yet: ⏳
        except RuntimeWarning as warning:
            pytest.fail(f"expected {expected}{' for ' + what if what else ''} without a RuntimeWarning, got "
                        f"RuntimeWarning: {warning}" + (f" ({hint})" if hint else ""))
        except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
            pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised "
                        f"{type(exc).__name__}: {exc}" + (f" ({hint})" if hint else ""))


def _expect_value_error(call, what, why, hint=""):
    """Fail with what was expected first, whatever the function did instead of raising ValueError itself."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        try:
            result = call()
        except NotImplementedError:
            raise                 # a function not written yet stays ⏳
        except ValueError as exc:
            if type(exc) is ValueError:
                return
            pytest.fail(f"expected {what} to raise ValueError itself ({why}), got {type(exc).__name__}: "
                        + (hint or "check the input yourself and raise ValueError, as the docstring asks"))
        except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
            pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned {result!r}")


def _python_float(got, what):
    assert type(got) is float, (f"expected {what} to be a Python float (float(...)), got "
                                f"{type(got).__module__}.{type(got).__name__}")


def _float_array(got, shape, what):
    assert isinstance(got, np.ndarray), (f"expected {what} to be a numpy.ndarray, got "
                                         f"{type(got).__module__}.{type(got).__name__}")
    assert got.shape == shape, f"expected {what} of shape {shape}, got shape {got.shape}"
    assert got.dtype.kind == "f", f"expected {what} made of floats, got dtype {got.dtype}"


def _show(v):
    return np.array2string(np.asarray(v, dtype=float), precision=6, suppress_small=False).replace("\n", "")


FORBIDDEN = ("scipy.optimize", "scipy.spatial", "scipy.linalg", "sklearn")


def _forbidden(module_name):
    return any(module_name == f or module_name.startswith(f + ".") for f in FORBIDDEN) or module_name == "scipy"


def test_svm_uses_no_ready_made_tool(svm):
    """svm.py computes by itself: no scipy.optimize, scipy.spatial, scipy.linalg nor scikit-learn."""
    try:
        tree = ast.parse(inspect.getsource(svm))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(a.name for a in node.names if _forbidden(a.name))
        elif isinstance(node, ast.ImportFrom) and node.module and _forbidden(node.module):
            found.add(node.module)
    assert not found, (f"expected svm.py to use NumPy only, found imports of {sorted(found)}: the tests compare your "
                       f"results with SciPy and scikit-learn, so write the computations yourself")



# ---------------------------------------------------------------- lagrange_equality_qp
def _random_qp(rng, n, m):
    """A random problem with Q symmetric positive definite and A of full row rank."""
    M = rng.normal(size=(n, n))
    Q = M @ M.T + n * np.eye(n)
    return Q, rng.normal(size=n), rng.normal(size=(m, n)), rng.normal(size=m)


def _oracle_qp(Q, c, A, b):
    """The minimum by elimination: x = x0 + N z, with N a basis of the null space of A (SciPy)."""
    x0 = np.linalg.lstsq(A, b, rcond=None)[0]
    N = null_space(A)
    if N.size:
        z = np.linalg.solve(N.T @ Q @ N, -N.T @ (Q @ x0 + c))
        x0 = x0 + N @ z
    lam = np.linalg.lstsq(A.T, -(Q @ x0 + c), rcond=None)[0]
    return x0, lam


def test_lagrange_docstring_example(svm):
    x, lam = _result(lambda: svm.lagrange_equality_qp([[2, 0], [0, 2]], [0, 0], [[1, 1]], [2]), "(x, lam)")
    _float_array(x, (2,), "x")
    _float_array(lam, (1,), "lam")
    assert np.allclose(x, [1.0, 1.0]) and np.allclose(lam, [-2.0]), (
        f"expected x = [1, 1] and lam = [-2] for min x₁² + x₂² under x₁ + x₂ = 2, got x = {_show(x)}, lam = "
        f"{_show(lam)} (the right-hand side of the system is (-c, b), and the Lagrangian adds + lamᵀ(A x - b))")


def test_lagrange_exact_small_problem(svm):
    # min x² + 2y² + 3z² - x under x + y + z = 1 and x - z = 0, solved exactly with fractions
    Q, c = [[2, 0, 0], [0, 4, 0], [0, 0, 6]], [-1, 0, 0]
    A, b = [[1, 1, 1], [1, 0, -1]], [1, 0]
    F = Fraction
    K = [[F(v) for v in row] for row in
         [[2, 0, 0, 1, 1], [0, 4, 0, 1, 0], [0, 0, 6, 1, -1], [1, 1, 1, 0, 0], [1, 0, -1, 0, 0]]]
    rhs = [F(1), F(0), F(0), F(1), F(0)]
    for col in range(5):                                  # Gauss-Jordan elimination, exact
        pivot = next(r for r in range(col, 5) if K[r][col] != 0)
        K[col], K[pivot], rhs[col], rhs[pivot] = K[pivot], K[col], rhs[pivot], rhs[col]
        for r in range(5):
            if r != col and K[r][col] != 0:
                f = K[r][col] / K[col][col]
                K[r] = [a - f * p for a, p in zip(K[r], K[col])]
                rhs[r] -= f * rhs[col]
    exact = [float(rhs[i] / K[i][i]) for i in range(5)]
    x, lam = _result(lambda: svm.lagrange_equality_qp(Q, c, A, b), "(x, lam)")
    assert np.allclose(x, exact[:3], atol=1e-12) and np.allclose(lam, exact[3:], atol=1e-12), (
        f"expected x = {_show(exact[:3])} and lam = {_show(exact[3:])} (exact solution), got x = {_show(x)}, "
        f"lam = {_show(lam)}")


@pytest.mark.parametrize("n, m", [(2, 1), (3, 1), (4, 2), (6, 3), (8, 5)])
def test_lagrange_matches_elimination(svm, n, m):
    Q, c, A, b = _random_qp(np.random.default_rng(4210 + 10 * n + m), n, m)
    x_ref, lam_ref = _oracle_qp(Q, c, A, b)
    x, lam = _result(lambda: svm.lagrange_equality_qp(Q, c, A, b), "(x, lam)", f"n = {n}, m = {m}")
    _float_array(x, (n,), "x")
    _float_array(lam, (m,), "lam")
    assert np.allclose(x, x_ref, atol=1e-9), (
        f"expected x = {_show(x_ref)} (the minimum, by elimination with scipy.linalg.null_space), got {_show(x)}")
    assert np.allclose(lam, lam_ref, atol=1e-8), (
        f"expected lam = {_show(lam_ref)}, got {_show(lam)} (the sign: Q x + c + Aᵀ lam = 0)")


def test_lagrange_conditions_and_minimality(svm):
    rng = np.random.default_rng(4211)
    Q, c, A, b = _random_qp(rng, 5, 2)
    x, lam = _result(lambda: svm.lagrange_equality_qp(Q, c, A, b), "(x, lam)")
    assert np.allclose(A @ x, b, atol=1e-10), f"expected A x = b (feasibility), got A x - b = {_show(A @ x - b)}"
    residual = Q @ x + c + A.T @ lam
    assert np.allclose(residual, 0, atol=1e-10), (
        f"expected Q x + c + Aᵀ lam = 0 (stationarity), got {_show(residual)}")
    f = 0.5 * x @ Q @ x + c @ x
    res = minimize(lambda v: 0.5 * v @ Q @ v + c @ v, np.zeros(5), jac=lambda v: Q @ v + c, method="SLSQP",
                   constraints=[{"type": "eq", "fun": lambda v: A @ v - b, "jac": lambda v: A}],
                   options={"ftol": 1e-12, "maxiter": 500})
    assert f <= res.fun + 1e-8, (f"expected the minimum value {res.fun:.10f} (scipy.optimize.minimize) or lower, got "
                                 f"f(x) = {f:.10f}")
    N = null_space(A)
    for _ in range(20):                                 # feasible neighbours do not do better
        v = x + N @ rng.normal(size=N.shape[1])
        assert 0.5 * v @ Q @ v + c @ v >= f - 1e-10, "expected no feasible point to give a smaller value than x"


def test_lagrange_does_not_modify_its_inputs(svm):
    Q, c, A, b = _random_qp(np.random.default_rng(4212), 3, 1)
    copies = [Q.copy(), c.copy(), A.copy(), b.copy()]
    _result(lambda: svm.lagrange_equality_qp(Q, c, A, b), "(x, lam)")
    for name, arr, copy in zip("QcAb", (Q, c, A, b), copies):
        assert np.array_equal(arr, copy), f"expected {name} to be left unchanged, but it was modified"


@pytest.mark.parametrize("Q, c, A, b, why", [
    ([[2, 0], [0, 2]], [0, 0, 0], [[1, 1]], [2], "c has 3 entries for a 2 x 2 Q"),
    ([[2, 0], [0, 2]], [0, 0], [[1, 1, 1]], [2], "A has 3 columns for 2 variables"),
    ([[2, 0], [0, 2]], [0, 0], [[1, 1]], [2, 3], "2 right-hand sides for 1 constraint"),
    ([[2, 0, 0], [0, 2, 0]], [0, 0], [[1, 1]], [2], "Q is not square"),
    ([2, 2], [0, 0], [[1, 1]], [2], "Q is not 2-D"),
    ([[2, 0], [0, 2]], [0, 0], [1, 1], [2], "A is not 2-D"),
])
def test_lagrange_rejects_bad_shapes(svm, Q, c, A, b, why):
    _expect_value_error(lambda: svm.lagrange_equality_qp(Q, c, A, b), "lagrange_equality_qp", why)


@pytest.mark.parametrize("Q, A, why", [
    ([[2, 0], [0, 2]], [[1, 1], [2, 2]], "two constraints that are the same up to a factor (dependent rows of A)"),
    ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1]], "Q = 0: the block matrix is singular"),
])
def test_lagrange_rejects_a_singular_system(svm, Q, A, why):
    n, m = len(Q), len(A)
    _expect_value_error(lambda: svm.lagrange_equality_qp(Q, [1.0] * n, A, [1.0] * m), "lagrange_equality_qp", why,
                        "catch numpy.linalg.LinAlgError and raise a ValueError, as the docstring asks")


# ---------------------------------------------------------------- hinge_loss
def test_hinge_docstring_example(svm):
    got = _result(lambda: svm.hinge_loss([2.0, 0.5, -1.0], [1, 1, 1]), "a float")
    _python_float(got, "hinge_loss")
    assert abs(got - 5 / 6) < 1e-12, (f"expected 5/6 ≈ 0.833333 (costs 0, 0.5 and 2), got {got!r}"
                                      + (" (that is the SUM: return the mean)" if abs(got - 2.5) < 1e-9 else ""))


@pytest.mark.parametrize("n", [1, 7, 50, 400])
def test_hinge_matches_scikit_learn(svm, n):
    rng = np.random.default_rng(4213 + n)
    y = np.where(rng.random(n) < 0.5, -1, 1)
    y[0], y[-1] = (1, -1) if n > 1 else (y[0], y[-1])
    s = rng.normal(0.0, 2.0, size=n)
    expected = float(np.mean(np.maximum(0, 1 - y * s))) if n == 1 else float(sk_hinge_loss(y, s))
    got = _result(lambda: svm.hinge_loss(s, y), "a float", f"{n} scores")
    _python_float(got, "hinge_loss")
    assert abs(got - expected) < 1e-12, (
        f"expected {expected!r} (sklearn.metrics.hinge_loss) for {n} scores, got {got!r}"
        + (" (that is the SUM: return the mean)" if abs(got - n * expected) < 1e-9 and n > 1 else ""))


def test_hinge_properties(svm):
    y = np.array([1, -1, 1, -1])
    zero = _result(lambda: svm.hinge_loss([1.0, -1.0, 3.5, -2.0], y), "0.0")
    assert zero == 0.0, f"expected 0 when every margin y s is at least 1, got {zero!r}"
    one = _result(lambda: svm.hinge_loss([0.0, 0.0, 0.0, 0.0], y), "1.0")
    assert abs(one - 1.0) < 1e-15, f"expected 1 for scores 0 (every point costs 1 - 0), got {one!r}"
    wrong = _result(lambda: svm.hinge_loss([-1.0, 1.0, -1.0, 1.0], y), "2.0")
    assert abs(wrong - 2.0) < 1e-15, f"expected 2 for four points misclassified with margin -1, got {wrong!r}"


def test_hinge_accepts_float_labels_and_leaves_inputs(svm):
    s, y = np.array([0.3, -0.2, 1.4]), np.array([1.0, -1.0, -1.0])
    s0, y0 = s.copy(), y.copy()
    got = _result(lambda: svm.hinge_loss(s, y), "a float")
    assert abs(got - (0.7 + 0.8 + 2.4) / 3) < 1e-12, f"expected {(0.7 + 0.8 + 2.4) / 3!r} for labels 1.0 and -1.0, got {got!r}"
    assert np.array_equal(s, s0) and np.array_equal(y, y0), "expected the scores and the labels to be left unchanged"


@pytest.mark.parametrize("scores, y, why", [
    ([], [], "no scores"),
    ([[1.0, 2.0]], [1, -1], "scores not 1-D"),
    ([1.0, 2.0], [1], "one label for two scores"),
    ([1.0, 2.0], [1, 0], "a label 0 (the labels are -1 and +1)"),
    ([1.0, 2.0], [1, 2], "a label 2"),
])
def test_hinge_rejects_bad_inputs(svm, scores, y, why):
    _expect_value_error(lambda: svm.hinge_loss(scores, y), "hinge_loss", why)


# ---------------------------------------------------------------- svm_subgradient
def _objective(w, b, X, y, C):
    """½‖w‖² + C Σ max(0, 1 - y_i (w · x_i + b)), written with Python loops."""
    hinge = 0.0
    for xi, yi in zip(X, y):
        hinge += max(0.0, 1.0 - yi * (sum(a * c for a, c in zip(w, xi)) + b))
    return 0.5 * sum(a * a for a in w) + C * hinge


def test_subgradient_docstring_example(svm):
    out = _result(lambda: svm.svm_subgradient([1.0, 0.0], 0.0, [[2, 0], [0.5, 1], [-1, 0]], [1, 1, -1]),
                  "(J, g_w, g_b)")
    assert isinstance(out, tuple) and len(out) == 3, f"expected a tuple (J, g_w, g_b), got {out!r}"
    J, g_w, g_b = out
    _python_float(J, "J")
    _float_array(g_w, (2,), "g_w")
    _python_float(g_b, "g_b")
    assert J == 1.0, f"expected J = 1.0 (½‖w‖² = 0.5 and one hinge of 0.5), got {J!r}"
    assert np.allclose(g_w, [0.5, -1.0]) and g_b == -1.0, (
        f"expected g_w = [0.5, -1] and g_b = -1 (only the second point, of margin 0.5, counts; the third has margin "
        f"exactly 1 and does not), got g_w = {_show(g_w)}, g_b = {g_b!r}")


@pytest.mark.parametrize("C", [0.1, 1.0, 10.0])
def test_subgradient_objective_matches_a_direct_computation(svm, C):
    rng = np.random.default_rng(4220 + int(10 * C))
    X = rng.normal(size=(40, 3))
    y = np.where(X @ [1.0, -2.0, 0.5] + rng.normal(0, 1.0, 40) > 0, 1, -1)
    w, b = rng.normal(size=3), float(rng.normal())
    expected = _objective(w, b, X, y, C)
    J, _, _ = _result(lambda: svm.svm_subgradient(w, b, X, y, C), "(J, g_w, g_b)", f"C = {C}")
    mean_version = 0.5 * w @ w + (expected - 0.5 * w @ w) / 40
    assert abs(J - expected) < 1e-9 * max(1.0, abs(expected)), (
        f"expected J = {expected!r} for C = {C}, got {J!r}"
        + (" (C multiplies the SUM of the hinges, not their mean)" if abs(J - mean_version) < 1e-9 else ""))


def test_subgradient_is_the_gradient_where_the_objective_is_smooth(svm):
    rng = np.random.default_rng(4231)
    X = rng.normal(size=(30, 2))
    y = np.where(X[:, 0] + 0.3 * X[:, 1] > 0, 1, -1)
    w, b, C = np.array([0.8, -0.4]), 0.1, 2.0
    margins = y * (X @ w + b)
    assert np.min(np.abs(margins - 1)) > 1e-3        # no point on the kink: the objective is differentiable here
    _, g_w, g_b = _result(lambda: svm.svm_subgradient(w, b, X, y, C), "(J, g_w, g_b)")
    h = 1e-6
    numeric = [(_objective(w + h * e, b, X, y, C) - _objective(w - h * e, b, X, y, C)) / (2 * h) for e in np.eye(2)]
    numeric_b = (_objective(w, b + h, X, y, C) - _objective(w, b - h, X, y, C)) / (2 * h)
    assert np.allclose(g_w, numeric, atol=1e-5) and abs(g_b - numeric_b) < 1e-5, (
        f"expected the gradient (finite differences) g_w = {_show(numeric)}, g_b = {numeric_b:.6f}, got "
        f"g_w = {_show(g_w)}, g_b = {g_b!r} (only the points with y (w · x + b) < 1 count, with - C y_i x_i)")


def test_subgradient_gives_a_lower_affine_bound(svm):
    rng = np.random.default_rng(4232)
    X = np.round(rng.normal(size=(12, 2)), 1)
    y = np.where(X[:, 0] - X[:, 1] > 0, 1, -1)
    w, b, C = np.array([1.0, -1.0]), 0.0, 1.0
    J, g_w, g_b = _result(lambda: svm.svm_subgradient(w, b, X, y, C), "(J, g_w, g_b)")
    for _ in range(200):
        v, c = w + rng.normal(0, 1.0, 2), b + rng.normal()
        assert _objective(v, c, X, y, C) >= J + g_w @ (v - w) + g_b * (c - b) - 1e-9, (
            "expected J(v, c) ≥ J(w, b) + g_w · (v - w) + g_b (c - b) for every (v, c): that is what a subgradient is")


def test_subgradient_convention_on_the_kink(svm):
    # the first point has margin exactly 1: it does not count; the second has margin 0: it counts
    J, g_w, g_b = _result(lambda: svm.svm_subgradient([0.5, 0.5], 0.0, [[1, 1], [1, -1]], [1, 1], C=3.0),
                          "(J, g_w, g_b)")
    assert J == 0.25 + 3.0, f"expected J = 0.25 + 3 × 1 = 3.25, got {J!r}"
    assert np.allclose(g_w, [0.5 - 3.0, 0.5 + 3.0]) and g_b == -3.0, (
        f"expected g_w = [-2.5, 3.5] and g_b = -3 (a margin exactly 1 does not count: strictly below 1 only), got "
        f"g_w = {_show(g_w)}, g_b = {g_b!r}")


def test_subgradient_of_a_well_separated_set_is_w(svm):
    X = np.array([[3.0, 0.0], [0.0, -4.0], [-5.0, 1.0]])
    y = np.array([1, -1, -1])
    w = np.array([1.0, 1.0])
    J, g_w, g_b = _result(lambda: svm.svm_subgradient(w, 0.0, X, y), "(J, g_w, g_b)")
    assert J == 1.0 and np.array_equal(g_w, w) and g_b == 0.0, (
        f"expected J = ½‖w‖² = 1, g_w = w and g_b = 0 when every margin is at least 1, got J = {J!r}, "
        f"g_w = {_show(g_w)}, g_b = {g_b!r}")


def test_subgradient_leaves_its_inputs(svm):
    w, X, y = np.array([0.2, -0.1]), np.array([[1.0, 2.0], [-1.0, 0.5]]), np.array([1, -1])
    copies = (w.copy(), X.copy(), y.copy())
    _result(lambda: svm.svm_subgradient(w, 0.3, X, y), "(J, g_w, g_b)")
    assert all(np.array_equal(a, c) for a, c in zip((w, X, y), copies)), "expected w, X and y to be left unchanged"


@pytest.mark.parametrize("w, b, X, y, C, why", [
    ([1.0, 0.0], 0.0, [[1, 2, 3]], [1], 1.0, "3 columns in X for 2 weights"),
    ([1.0, 0.0], 0.0, [1, 2], [1], 1.0, "X not 2-D"),
    ([1.0, 0.0], 0.0, [[1, 2], [3, 4]], [1], 1.0, "one label for two examples"),
    ([1.0, 0.0], 0.0, [[1, 2], [3, 4]], [1, 0], 1.0, "a label 0"),
    ([1.0, 0.0], 0.0, [[1, 2]], [1], 0.0, "C = 0"),
    ([1.0, 0.0], 0.0, [[1, 2]], [1], -2.0, "C < 0"),
])
def test_subgradient_rejects_bad_inputs(svm, w, b, X, y, C, why):
    _expect_value_error(lambda: svm.svm_subgradient(w, b, X, y, C), "svm_subgradient", why)


# ---------------------------------------------------------------- rbf_kernel
def test_rbf_docstring_example(svm):
    K = _result(lambda: svm.rbf_kernel([[0, 0], [1, 1]], [[0, 0]], gamma=1.0), "a (2, 1) matrix")
    _float_array(K, (2, 1), "rbf_kernel")
    assert np.allclose(K, [[1.0], [np.exp(-2.0)]], atol=1e-12), (
        f"expected [[1], [e^-2 ≈ 0.135335]], got {_show(K)} (‖x - z‖² = 2: the distance is SQUARED)")


@pytest.mark.parametrize("n, m, p, gamma", [(1, 1, 1, 0.5), (5, 3, 2, 1.0), (20, 30, 4, 0.1), (40, 40, 10, 2.5)])
def test_rbf_matches_scikit_learn(svm, n, m, p, gamma):
    rng = np.random.default_rng(4240 + n + m)
    X, Z = rng.normal(size=(n, p)), rng.normal(size=(m, p))
    expected = sk_rbf_kernel(X, Z, gamma=gamma)
    K = _result(lambda: svm.rbf_kernel(X, Z, gamma), f"a ({n}, {m}) matrix")
    _float_array(K, (n, m), "rbf_kernel")
    assert np.allclose(K, expected, atol=1e-12), (
        f"expected the matrix of sklearn.metrics.pairwise.rbf_kernel(X, Z, gamma={gamma}), largest gap "
        f"{np.max(np.abs(K - expected)):.2e} (exp(-gamma ‖x_i - z_j‖²), row i for x_i, column j for z_j)")
    assert np.allclose(K, np.exp(-gamma * cdist(X, Z, "sqeuclidean")), atol=1e-12)


def test_rbf_gram_matrix_properties(svm):
    X = np.random.default_rng(4245).normal(size=(25, 3))
    K = _result(lambda: svm.rbf_kernel(X, X, 0.7), "a (25, 25) matrix")
    assert np.allclose(K, K.T, atol=1e-14), "expected a symmetric matrix K(X, X)"
    assert np.allclose(np.diag(K), 1.0, atol=1e-12), f"expected 1 on the diagonal (‖x - x‖ = 0), got {_show(np.diag(K)[:4])}…"
    assert np.min(np.linalg.eigvalsh(K)) > -1e-10, "expected a positive semi-definite Gram matrix"


def test_rbf_clips_rounding_errors(svm):
    # points far from the origin: the expansion ‖x‖² - 2 x·z + ‖z‖² gives tiny negative values instead of 0
    X = np.random.default_rng(4246).normal(size=(50, 5)) * 1e3 + 5e3
    K = _result(lambda: svm.rbf_kernel(X, X, 1.0), "a (50, 50) matrix")
    assert np.all(K <= 1.0) and np.all(K >= 0.0) and np.all(np.isfinite(K)), (
        f"expected entries in [0, 1], got a largest entry {np.max(K)!r} (clip the tiny negative squared distances that "
        f"rounding produces to 0, as the docstring asks)")


def test_rbf_far_points_and_inputs(svm):
    X, Z = np.array([[0.0, 0.0]]), np.array([[100.0, 0.0]])
    X0, Z0 = X.copy(), Z.copy()
    K = _result(lambda: svm.rbf_kernel(X, Z, 1.0), "[[0.0]]")
    assert K[0, 0] == 0.0, f"expected 0 in floats for two points at distance 100 with gamma = 1, got {K[0, 0]!r}"
    assert np.array_equal(X, X0) and np.array_equal(Z, Z0), "expected X and Z to be left unchanged"


@pytest.mark.parametrize("X, Z, gamma, why", [
    ([0.0, 1.0], [[0.0, 1.0]], 1.0, "X not 2-D"),
    ([[0.0, 1.0]], [0.0, 1.0], 1.0, "Z not 2-D"),
    ([[0.0, 1.0]], [[0.0, 1.0, 2.0]], 1.0, "2 columns in X and 3 in Z"),
    ([[0.0, 1.0]], [[0.0, 1.0]], 0.0, "gamma = 0"),
    ([[0.0, 1.0]], [[0.0, 1.0]], -1.0, "gamma < 0"),
])
def test_rbf_rejects_bad_inputs(svm, X, Z, gamma, why):
    _expect_value_error(lambda: svm.rbf_kernel(X, Z, gamma), "rbf_kernel", why)


# ---------------------------------------------------------------- polynomial_kernel
def test_polynomial_docstring_example(svm):
    K = _result(lambda: svm.polynomial_kernel([[2, 1]], [[1, 1], [0, 0]]), "a (1, 2) matrix")
    _float_array(K, (1, 2), "polynomial_kernel")
    assert np.allclose(K, [[16.0, 1.0]]), (
        f"expected [[16, 1]] with degree 2 and coef0 1 by default, got {_show(K)} ((2·1 + 1·1 + 1)² = 16)")


@pytest.mark.parametrize("degree, coef0", [(1, 0.0), (2, 1.0), (3, 0.5), (4, 2.0), (2, 0.0)])
def test_polynomial_matches_scikit_learn(svm, degree, coef0):
    rng = np.random.default_rng(4250 + degree)
    X, Z = rng.normal(size=(7, 3)), rng.normal(size=(5, 3))
    expected = sk_polynomial_kernel(X, Z, degree=degree, gamma=1.0, coef0=coef0)
    K = _result(lambda: svm.polynomial_kernel(X, Z, degree=degree, coef0=coef0), "a (7, 5) matrix")
    _float_array(K, (7, 5), "polynomial_kernel")
    assert np.allclose(K, expected, atol=1e-10), (
        f"expected (X Zᵀ + {coef0}) ** {degree} (sklearn.metrics.pairwise.polynomial_kernel with gamma=1), largest "
        f"gap {np.max(np.abs(K - expected)):.2e}")


def test_polynomial_exact_integers_and_numpy_degree(svm):
    X = np.array([[1, 2], [-1, 3]])
    K = _result(lambda: svm.polynomial_kernel(X, X, degree=np.int64(3), coef0=2), "a (2, 2) matrix")
    expected = np.array([[(5 + 2) ** 3, (5 + 2) ** 3], [(5 + 2) ** 3, (10 + 2) ** 3]], dtype=float)
    assert np.array_equal(K, expected), f"expected {_show(expected)} (a NumPy integer is a valid degree), got {_show(K)}"
    assert np.min(np.linalg.eigvalsh(svm.polynomial_kernel(X, X))) > -1e-9, "expected a positive semi-definite Gram matrix"


@pytest.mark.parametrize("degree, coef0, why", [
    (0, 1.0, "degree = 0"),
    (-2, 1.0, "degree < 0"),
    (2.0, 1.0, "degree = 2.0, a float and not an integer"),
    (True, 1.0, "degree = True, a boolean"),
    (2, -1.0, "coef0 < 0"),
])
def test_polynomial_rejects_bad_parameters(svm, degree, coef0, why):
    _expect_value_error(lambda: svm.polynomial_kernel([[1.0, 2.0]], [[0.5, 1.0]], degree=degree, coef0=coef0),
                        "polynomial_kernel", why)


@pytest.mark.parametrize("X, Z, why", [
    ([1.0, 2.0], [[1.0, 2.0]], "X not 2-D"),
    ([[1.0, 2.0]], [[1.0, 2.0, 3.0]], "2 columns in X and 3 in Z"),
])
def test_polynomial_rejects_bad_shapes(svm, X, Z, why):
    _expect_value_error(lambda: svm.polynomial_kernel(X, Z), "polynomial_kernel", why)
