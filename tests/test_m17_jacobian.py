"""Tests of mymath.jacobian (chapter M17): the Jacobian by centered differences, column by column; the diagonal Jacobian
of an elementwise map with one pair of evaluations; a Jacobian-vector product without forming the matrix.

Oracles: SymPy (``sympy.Matrix.jacobian``, exact derivatives evaluated at the point), ``scipy.differentiate.jacobian``,
linear maps (their Jacobian is their matrix), and properties (``J v`` for every direction ``v``, the diagonal of an
elementwise map, the number of evaluations of ``f``). They describe the expected behaviour without showing the
solution.

    pytest tests/test_m17_jacobian.py              # your code
    pytest tests/test_m17_jacobian.py --impl=ref   # the reference
"""

import ast
import inspect
import warnings

import numpy as np
import pytest
import sympy


@pytest.fixture
def jac(mymath_module):
    return mymath_module("jacobian")


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


def _expect_value_error(call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ValueError itself."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        try:
            result = call()
        except NotImplementedError:
            raise                 # a function not written yet stays ⏳
        except ValueError as exc:
            if type(exc) is ValueError:
                return exc
            pytest.fail(f"expected {what} to raise ValueError itself ({why}), got {type(exc).__name__}: check the "
                        "input yourself and raise ValueError, as the docstring asks")
        except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
            pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned {result!r}")


def _show(v):
    return np.array2string(np.asarray(v, dtype=float), precision=6, suppress_small=True).replace("\n", "")


def _float_array(got, shape, what):
    assert isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape, (
        f"expected {what} as a numpy.ndarray of floats of shape {shape}, got {type(got).__name__}"
        + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray) else ""))


def _close(got, want, what, atol=1e-6, hint=""):
    got = np.asarray(got, dtype=float)
    assert got.shape == np.shape(want) and np.allclose(got, want, rtol=1e-6, atol=atol), (
        f"expected {what} = {_show(want)}, got {_show(got)}" + (f" ({hint})" if hint else ""))


class Counted:
    """A map of ℝⁿ into ℝᵐ that counts its calls and refuses to be called on the caller's array."""

    def __init__(self, f):
        self.f, self.calls, self.seen = f, 0, []

    def __call__(self, p):
        self.calls += 1
        self.seen.append(p)
        return self.f(p)


# Maps with an exact Jacobian (SymPy), all on the same symbols
X, Y, Z = sympy.symbols("x y z")
SPHERICAL = sympy.Matrix([X * sympy.sin(Y) * sympy.cos(Z), X * sympy.sin(Y) * sympy.sin(Z), X * sympy.cos(Y)])
MIXED = sympy.Matrix([sympy.exp(X * Y) - Z, sympy.log(1 + X ** 2) * sympy.sqrt(Z), sympy.atan(Y - Z)])
WIDE = sympy.Matrix([X * Y * Z + sympy.sin(X), Y ** 3 - 2 * X * Z])                     # ℝ³ → ℝ²
TALL_2 = sympy.Matrix([X ** 2 * Y, sympy.cos(X + 2 * Y), X - Y ** 2, sympy.atan(X * Y)])   # ℝ² → ℝ⁴


def _numeric(expr, symbols):
    f = sympy.lambdify([symbols], list(expr), "numpy")
    return lambda p: np.array(f(np.asarray(p, dtype=float)), dtype=float)


def _exact_jacobian(expr, symbols, point):
    J = expr.jacobian(symbols)
    return np.array(J.subs(dict(zip(symbols, point))).evalf(), dtype=float)


CASES = [
    (SPHERICAL, (X, Y, Z), [2.0, 0.7, -1.2], "spherical coordinates (r, θ, φ)"),
    (MIXED, (X, Y, Z), [0.4, -0.9, 1.6], "a mixed map of ℝ³ into ℝ³"),
    (WIDE, (X, Y, Z), [1.3, -0.5, 0.8], "a map of ℝ³ into ℝ² (2 rows, 3 columns)"),
    (TALL_2, (X, Y), [0.6, -1.1], "a map of ℝ² into ℝ⁴ (4 rows, 2 columns)"),
]


# --- what the module may use ------------------------------------------------------------------------------------

def test_module_uses_neither_sympy_nor_scipy(jac):
    """The docstring allows NumPy only: the tests compare the results with SymPy and scipy.differentiate."""
    try:
        tree = ast.parse(inspect.getsource(jac))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names] + ([node.module] if isinstance(node, ast.ImportFrom) else [])
            found |= {n.split(".")[0] for n in names if n and n.split(".")[0] in ("sympy", "scipy", "jax", "torch")}
    assert not found, (f"expected the module to compute the differences itself with NumPy, found an import of "
                       f"{sorted(found)} (the tests compare your results with SymPy and scipy.differentiate)")


# --- numerical_jacobian -----------------------------------------------------------------------------------------

def test_numerical_jacobian_docstring_examples(jac):
    polar = lambda p: np.array([p[0] * np.cos(p[1]), p[0] * np.sin(p[1])])   # noqa: E731
    got = _result(lambda: jac.numerical_jacobian(polar, [2.0, 0.0]), "[[1, 0], [0, 2]]", "polar coordinates at (2, 0)")
    _float_array(got, (2, 2), "numerical_jacobian(polar, [2.0, 0.0])")
    _close(got, [[1.0, 0.0], [0.0, 2.0]], "the Jacobian of (r, θ) ↦ (r cos θ, r sin θ) at (2, 0)",
           hint="column j is (f(x + h e_j) - f(x - h e_j)) / (2 h): one column per input")
    g = lambda v: np.array([v[0] * v[1], v[0] + 3 * v[1], v[1] ** 2])        # noqa: E731
    got = _result(lambda: jac.numerical_jacobian(g, [1.0, 2.0]), "[[2, 1], [1, 3], [0, 4]]", "g at (1, 2)")
    _float_array(got, (3, 2), "numerical_jacobian(g, [1.0, 2.0])")
    _close(got, [[2.0, 1.0], [1.0, 3.0], [0.0, 4.0]], "the Jacobian of (x, y) ↦ (xy, x + 3y, y²) at (1, 2)",
           hint="one ROW per output and one COLUMN per input: the shape is (m, n), not (n, m)")


@pytest.mark.parametrize("expr, symbols, point, why", CASES)
def test_numerical_jacobian_matches_sympy(jac, expr, symbols, point, why):
    f = _numeric(expr, symbols)
    want = _exact_jacobian(expr, symbols, point)
    got = _result(lambda: jac.numerical_jacobian(f, point), f"the {want.shape} Jacobian", why)
    _float_array(got, want.shape, f"numerical_jacobian for {why}")
    _close(got, want, f"the Jacobian of {why} at {point} (exact, by SymPy)",
           hint="J[i, j] = ∂f_i/∂x_j: row i for the output i, column j for the input j")


def test_numerical_jacobian_matches_scipy_differentiate(jac):
    """scipy.differentiate.jacobian, on a map written for arrays of points (one column per point)."""
    from scipy.differentiate import jacobian as scipy_jacobian
    def field(p):                                    # works on a point (n,) and on points (n, k)
        return np.array([np.sin(p[0]) * p[1], p[0] ** 2 + np.exp(-p[1]), np.cos(p[0] * p[1])])
    point = np.array([0.8, -0.3])
    want = scipy_jacobian(field, point).df
    got = _result(lambda: jac.numerical_jacobian(field, point), f"the {want.shape} Jacobian", "a field of ℝ² into ℝ³")
    _close(got, want, "the Jacobian of (x, y) ↦ (y sin x, x² + e^(-y), cos(xy)) at (0.8, -0.3) "
                      "(scipy.differentiate.jacobian)")


def test_numerical_jacobian_of_a_linear_map_is_its_matrix(jac):
    rng = np.random.default_rng(5010)
    for m, n in ((1, 1), (3, 5), (6, 2)):
        A = rng.integers(-5, 6, size=(m, n)).astype(float)
        x = rng.normal(size=n)
        got = _result(lambda: jac.numerical_jacobian(lambda p: A @ p, x), f"the ({m}, {n}) matrix A", "p ↦ A p")
        _float_array(got, (m, n), f"numerical_jacobian of p ↦ A p for A of shape ({m}, {n})")
        _close(got, A, f"the Jacobian of the linear map p ↦ A p (A of shape ({m}, {n})): A itself", atol=1e-7)


def test_numerical_jacobian_of_a_scalar_function_is_one_row(jac):
    """A number counts as an array of length 1: the Jacobian of a scalar function is a (1, n) row, its gradient."""
    f = lambda p: float(p[0] ** 2 + 3 * p[0] * p[1] - p[2])                    # noqa: E731
    got = _result(lambda: jac.numerical_jacobian(f, [1.0, 2.0, 5.0]), "the (1, 3) row [[8, 3, -1]]",
                  "a function that returns a Python float", "np.atleast_1d on the values of f")
    _float_array(got, (1, 3), "numerical_jacobian of a scalar function of 3 variables")
    _close(got, [[8.0, 3.0, -1.0]], "the Jacobian of x² + 3xy - z at (1, 2, 5), a single row (the gradient of M05b)")
    got = _result(lambda: jac.numerical_jacobian(np.sin, [0.0]), "[[1.0]]", "sin at 0, with n = m = 1")
    _close(got, [[1.0]], "the Jacobian of sin at 0, a (1, 1) matrix")


def test_numerical_jacobian_uses_centered_differences(jac):
    """With h = 1e-3, centered differences are exact to about h²; a forward difference is off by about h/2."""
    f = lambda p: np.exp(p)                                                     # noqa: E731
    got = _result(lambda: jac.numerical_jacobian(f, [1.0], h=1e-3), "[[e]]", "exp at 1 with h = 1e-3")
    _close(got, [[np.e]], "the derivative of exp at 1 with h = 1e-3, to about 5e-7", atol=2e-6,
           hint="(f(x + h e_j) - f(x - h e_j)) / (2 h): a forward difference (f(x + h) - f(x)) / h is off by h/2")


def test_numerical_jacobian_takes_2n_evaluations_and_leaves_x_alone(jac):
    rng = np.random.default_rng(5011)
    n = 7
    A = rng.normal(size=(4, n))
    f = Counted(lambda p: A @ np.sin(p))
    x = rng.normal(size=n)
    kept = x.copy()
    _result(lambda: jac.numerical_jacobian(f, x), "a (4, 7) Jacobian", "a map of ℝ⁷ into ℝ⁴")
    assert np.array_equal(x, kept), (f"expected x to be left unchanged (copy it before moving one coordinate), "
                                     f"got {_show(x)} instead of {_show(kept)}")
    assert f.calls <= 2 * n + 1, (f"expected 2 n = {2 * n} evaluations of f (two per column), got {f.calls}")
    assert all(p is not x for p in f.seen), "expected f to be called on copies of x, never on x itself"


def test_numerical_jacobian_accepts_a_list_of_integers(jac):
    got = _result(lambda: jac.numerical_jacobian(lambda p: p ** 2, [1, 2, 3]), "diag(2, 4, 6)", "x = [1, 2, 3]",
                  "convert x to floats: an array of integers cannot move by h")
    _float_array(got, (3, 3), "numerical_jacobian(lambda p: p ** 2, [1, 2, 3])")
    _close(got, np.diag([2.0, 4.0, 6.0]), "the Jacobian of p ↦ p² at (1, 2, 3)")


@pytest.mark.parametrize("x, h, why", [([[1.0, 2.0]], 1e-5, "x is 2-D"),
                                       ([], 1e-5, "x is empty"),
                                       ([1.0, 2.0], 0.0, "h = 0"),
                                       ([1.0, 2.0], -1e-3, "h < 0")])
def test_numerical_jacobian_refuses_bad_arguments(jac, x, h, why):
    _expect_value_error(lambda: jac.numerical_jacobian(lambda p: p * 2, x, h=h),
                        f"numerical_jacobian(f, {x!r}, h={h!r})", why)


def test_numerical_jacobian_refuses_values_that_are_not_1d(jac):
    _expect_value_error(lambda: jac.numerical_jacobian(lambda p: np.outer(p, p), [1.0, 2.0]),
                        "numerical_jacobian of a map whose values are (2, 2) matrices",
                        "the values of f must be 1-D arrays")
    _expect_value_error(lambda: jac.numerical_jacobian(lambda p: np.ones(1 if p[0] > 1 else 2), [1.0, 3.0]),
                        "numerical_jacobian of a map whose values change length",
                        "the values of f must all have the same length")


# --- diagonal_jacobian ------------------------------------------------------------------------------------------

def test_diagonal_jacobian_docstring_examples(jac):
    got = _result(lambda: jac.diagonal_jacobian(lambda v: v ** 3, [1.0, -2.0, 0.5]), "diag(3, 12, 0.75)",
                  "v ↦ v³ at (1, -2, 0.5)")
    _float_array(got, (3, 3), "diagonal_jacobian(lambda v: v ** 3, [1.0, -2.0, 0.5])")
    _close(got, np.diag([3.0, 12.0, 0.75]), "the diagonal Jacobian of v ↦ v³ at (1, -2, 0.5)",
           hint="an (n, n) matrix: np.diag of the vector of derivatives")
    got = _result(lambda: jac.diagonal_jacobian(np.arctan, [0.0, 1.0]), "diag(1, 0.5)", "arctan at (0, 1)")
    _close(got, np.diag([1.0, 0.5]), "the diagonal Jacobian of arctan at (0, 1)")


@pytest.mark.parametrize("g, dg, why", [(np.sin, np.cos, "sin"),
                                        (np.arctan, lambda t: 1 / (1 + t ** 2), "arctan"),
                                        (lambda t: t * np.exp(-t), lambda t: (1 - t) * np.exp(-t), "t e^(-t)")])
def test_diagonal_jacobian_matches_the_derivatives(jac, g, dg, why):
    rng = np.random.default_rng(5012)
    x = rng.uniform(-3, 3, size=40)
    got = _result(lambda: jac.diagonal_jacobian(g, x), "a (40, 40) diagonal matrix", f"{why} on 40 coordinates")
    _float_array(got, (40, 40), f"diagonal_jacobian of {why} on 40 coordinates")
    _close(np.diag(got), dg(x), f"the derivatives of {why} on the diagonal")
    off = got - np.diag(np.diag(got))
    assert np.all(off == 0), f"expected zeros off the diagonal, got a largest |value| of {np.abs(off).max()!r}"


def test_diagonal_jacobian_takes_two_evaluations(jac):
    f = Counted(np.sin)
    x = np.linspace(-2, 2, 50)
    kept = x.copy()
    _result(lambda: jac.diagonal_jacobian(f, x), "a (50, 50) diagonal matrix", "sin on 50 coordinates")
    assert f.calls <= 3, (f"expected 2 evaluations of f (x + h and x - h, all the coordinates moved at once), got "
                          f"{f.calls}: moving one coordinate at a time costs 2 n")
    assert np.array_equal(x, kept), "expected x to be left unchanged"


def test_diagonal_jacobian_moves_every_coordinate_at_once(jac):
    """On a map that is NOT elementwise, the result is diag(J 1): the docstring says it is wrong, and how."""
    A = np.array([[1.0, 2.0, 0.0], [0.0, -1.0, 3.0], [4.0, 0.0, 1.0]])
    f = lambda p: A @ p                                                       # noqa: E731
    got = _result(lambda: jac.diagonal_jacobian(f, [0.3, -0.2, 1.0]), "diag(3, 2, 5)", "p ↦ A p (not elementwise)")
    _close(got, np.diag(A @ np.ones(3)), "diag(A 1) = diag(3, 2, 5) for p ↦ A p: moving all the coordinates by h "
           "adds the columns", hint="(f(x + h) - f(x - h)) / (2 h), with h added to EVERY coordinate")


@pytest.mark.parametrize("x, h, why", [([[1.0], [2.0]], 1e-5, "x is 2-D"), ([], 1e-5, "x is empty"),
                                       ([1.0, 2.0], 0.0, "h = 0"), ([1.0, 2.0], -0.1, "h < 0")])
def test_diagonal_jacobian_refuses_bad_arguments(jac, x, h, why):
    _expect_value_error(lambda: jac.diagonal_jacobian(np.sin, x, h=h), f"diagonal_jacobian(sin, {x!r}, h={h!r})", why)


def test_diagonal_jacobian_refuses_a_map_that_changes_the_length(jac):
    _expect_value_error(lambda: jac.diagonal_jacobian(lambda p: np.array([p.sum()]), [1.0, 2.0, 3.0]),
                        "diagonal_jacobian of a map of ℝ³ into ℝ", "f(x) must have the length of x")


# --- jacobian_vector_product ------------------------------------------------------------------------------------

def test_jacobian_vector_product_docstring_example(jac):
    g = lambda p: np.array([p[0] ** 2 - p[1], p[0] * p[1]])                   # noqa: E731
    got = _result(lambda: jac.jacobian_vector_product(g, [1.0, 3.0], [1.0, -1.0]), "[3, 2]", "the docstring example")
    _float_array(got, (2,), "jacobian_vector_product(g, [1.0, 3.0], [1.0, -1.0])")
    _close(got, [3.0, 2.0], "J v = [[2, -1], [3, 1]] (1, -1)", hint="(f(x + h v) - f(x - h v)) / (2 h)")


@pytest.mark.parametrize("expr, symbols, point, why", CASES)
def test_jacobian_vector_product_matches_sympy(jac, expr, symbols, point, why):
    f = _numeric(expr, symbols)
    J = _exact_jacobian(expr, symbols, point)
    rng = np.random.default_rng(5013)
    for _ in range(3):
        v = rng.normal(size=len(symbols))
        v /= np.linalg.norm(v)
        got = _result(lambda: jac.jacobian_vector_product(f, point, v), f"J v of length {J.shape[0]}", why)
        _float_array(got, (J.shape[0],), f"jacobian_vector_product for {why}")
        _close(got, J @ v, f"J v for {why} at {point}, v = {_show(v)} (exact J by SymPy)",
               hint="J v has one coordinate per OUTPUT: the derivative of every output in the direction v")


def test_jacobian_vector_product_takes_two_evaluations(jac):
    rng = np.random.default_rng(5014)
    n = 200
    A = rng.normal(size=(3, n)) / np.sqrt(n)
    f = Counted(lambda p: np.arctan(A @ p))
    x, v = rng.normal(size=n), rng.normal(size=n) / np.sqrt(n)
    x_kept, v_kept = x.copy(), v.copy()
    got = _result(lambda: jac.jacobian_vector_product(f, x, v), "J v of length 3", "a map of ℝ²⁰⁰ into ℝ³")
    want = (A @ v) / (1 + (A @ x) ** 2)
    _close(got, want, "J v for p ↦ arctan(A p) of ℝ²⁰⁰ into ℝ³")
    assert f.calls <= 3, (f"expected 2 evaluations of f (x + h v and x - h v), got {f.calls}: J v needs no "
                          "column of the Jacobian")
    assert np.array_equal(x, x_kept) and np.array_equal(v, v_kept), "expected x and v to be left unchanged"


def test_jacobian_vector_product_of_a_linear_map(jac):
    A = np.array([[2.0, -1.0, 0.5], [0.0, 3.0, 1.0]])
    got = _result(lambda: jac.jacobian_vector_product(lambda p: A @ p + 7, [1, 1, 1], [0, 2, -2]), "A v = [-3, 4]",
                  "p ↦ A p + 7 with x and v given as lists of integers", "convert x and v to floats")
    _close(got, [-3.0, 4.0], "A v for the affine map p ↦ A p + 7 (the constant disappears)")


@pytest.mark.parametrize("x, v, h, why", [([1.0, 2.0], [1.0], 1e-5, "x and v of different lengths"),
                                          ([[1.0, 2.0]], [[1.0, 0.0]], 1e-5, "x and v are 2-D"),
                                          ([], [], 1e-5, "x and v are empty"),
                                          ([1.0, 2.0], [0.0, 1.0], 0.0, "h = 0")])
def test_jacobian_vector_product_refuses_bad_arguments(jac, x, v, h, why):
    _expect_value_error(lambda: jac.jacobian_vector_product(lambda p: p * 2, x, v, h=h),
                        f"jacobian_vector_product(f, {x!r}, {v!r}, h={h!r})", why)
