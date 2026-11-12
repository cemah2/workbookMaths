"""Tests of mymath.iterative (chapter M19): the Hessian by centered differences, the critical step 2 / λmax of a
symmetric positive definite matrix, the iterates of Richardson's method for ``A x = b``, and linear recurrences of
any order.

Oracles: SymPy (exact Hessians evaluated at the point), polynomials on which the centered formulas are exact for a
binary step, ``np.linalg.eigvals`` (the critical step), ``np.linalg.solve`` and ``np.linalg.matrix_power`` (the
closed form ``x_k = x* + (I - ω A)^k (x_0 - x*)`` of Richardson's iterates), ``fractions`` (exact terms of a
recurrence), closed forms (Fibonacci, ``2^k + 3^k``, ``cos(k θ)``), and properties (exact symmetry, the number of
evaluations of ``f``, inputs left unchanged). They describe the expected behaviour without showing the solution.

    pytest tests/test_m19_iterative.py              # your code
    pytest tests/test_m19_iterative.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings
from fractions import Fraction

import numpy as np
import pytest
import sympy


@pytest.fixture
def it(mymath_module):
    return mymath_module("iterative")


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


def _expect_error(error, call, what, why):
    """Fail with what was expected first, whatever the code did instead of raising `error` itself."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        try:
            result = call()
        except NotImplementedError:
            raise                 # a function not written yet stays ⏳
        except error as exc:
            return exc
        except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
            pytest.fail(f"expected {what} to raise {error.__name__} ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise {error.__name__} ({why}), but it returned {result!r}")


def _show(v):
    return np.array2string(np.asarray(v, dtype=float), precision=6, suppress_small=True,
                           max_line_width=10_000).replace("\n", "")


def _float_array(got, shape, what):
    assert isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape, (
        f"expected {what} as a numpy.ndarray of floats of shape {shape}, got {type(got).__name__}"
        + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray) else ""))


def _close(got, want, what, rtol=1e-9, atol=1e-12, hint=""):
    got = np.asarray(got, dtype=float)
    want = np.asarray(want, dtype=float)
    assert got.shape == want.shape and np.allclose(got, want, rtol=rtol, atol=atol), (
        f"expected {what} = {_show(want)}, got {_show(got)}" + (f" ({hint})" if hint else ""))


def _spd(n, seed, low=0.5, high=6.0):
    """A symmetric positive definite (n, n) matrix whose eigenvalues are spread between low and high."""
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    values = np.linspace(low, high, n) if n > 1 else np.array([high])
    A = Q @ np.diag(values) @ Q.T
    return (A + A.T) / 2


# --- what the module may use ------------------------------------------------------------------------------------

def test_module_uses_no_solver_and_eigenvalues_only_in_critical_step_size(it):
    """The docstring forbids solve, inv, scipy.optimize and scipy.sparse.linalg, and allows eigvalsh in one place."""
    try:
        tree = ast.parse(inspect.getsource(it))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module.startswith(("scipy.optimize", "scipy.sparse")):
                found.append(f"from {node.module} import …")
            found += [f"from {node.module} import {a.name}" for a in node.names if a.name in ("solve", "inv")]
        if isinstance(node, ast.Import):
            found += [f"import {a.name}" for a in node.names if a.name.startswith(("scipy.optimize", "scipy.sparse"))]
    eigen = {"eigvalsh", "eigh", "eig", "eigvals"}
    imported = {a.asname or a.name for node in ast.walk(tree) if isinstance(node, ast.ImportFrom) for a in node.names}
    for function in (n for n in tree.body if isinstance(n, ast.FunctionDef)):
        for node in ast.walk(function):
            if isinstance(node, ast.Attribute):
                name = node.attr
            elif isinstance(node, ast.Name) and node.id in imported:
                name = node.id
            else:
                continue
            if name in ("solve", "inv"):
                found.append(f"{name} in {function.name}")
            elif name in eigen and function.name != "critical_step_size":
                found.append(f"{name} in {function.name}")
    assert not found, (f"expected NumPy without a solver (and eigvalsh in critical_step_size only), found "
                       f"{sorted(set(found))} (the tests compare your results with them)")


# --- numerical_hessian -------------------------------------------------------------------------------------------

V = sympy.symbols("v0:4")

# functions written once, for NumPy arrays and for SymPy symbols, with points where they are smooth
FUNCTIONS = [
    ("v0²/2 + sin v0", lambda v, F: v[0] ** 2 * 0.5 + F["sin"](v[0]), 1, ([0.3], [-2.0])),
    ("e^(v0) sin v1", lambda v, F: F["exp"](v[0]) * F["sin"](v[1]), 2, ([0.2, 1.1], [-1.0, -0.4])),
    ("v0³ - 2 v0 v1² + ln(1 + v1²)", lambda v, F: v[0] ** 3 - 2 * v[0] * v[1] ** 2 + F["log"](1 + v[1] ** 2), 2,
     ([1.5, -0.5], [-0.75, 2.0])),
    ("v0 v1 v2 + cos(v0 + 2 v2)", lambda v, F: v[0] * v[1] * v[2] + F["cos"](v[0] + 2 * v[2]), 3,
     ([0.5, -1.0, 2.0], [1.2, 0.3, -0.6])),
    ("quadratic form in 4 variables", lambda v, F: (3 * v[0] ** 2 + v[0] * v[3] - 2 * v[1] * v[2] + 0.5 * v[2] ** 2
                                                    + 4 * v[1] * v[3] - v[3] ** 2 + 7 * v[0]), 4,
     ([1.0, -2.0, 0.5, 3.0], [0.0, 0.0, 0.0, 0.0])),
]
NUMPY = {"sin": np.sin, "cos": np.cos, "exp": np.exp, "log": np.log}
SYMPY = {"sin": sympy.sin, "cos": sympy.cos, "exp": sympy.exp, "log": sympy.log}


def _exact_hessian(build, n, point):
    symbols = V[:n]
    expr = build(symbols, SYMPY)
    hessian = sympy.hessian(expr, symbols)
    return np.array(hessian.subs(dict(zip(symbols, point))).evalf(), dtype=float)


def test_numerical_hessian_docstring_example(it):
    f = lambda v: v[0] ** 2 * v[1] + 3 * v[1] ** 2   # noqa: E731
    got = _result(lambda: it.numerical_hessian(f, [1.0, 2.0]), "[[4, 2], [2, 6]]", "v0² v1 + 3 v1² at (1, 2)")
    _float_array(got, (2, 2), "numerical_hessian of the docstring example")
    _close(got, [[4.0, 2.0], [2.0, 6.0]], "the Hessian of v0² v1 + 3 v1² at (1, 2)", rtol=1e-6, atol=1e-6)


@pytest.mark.parametrize("text, build, n, points", FUNCTIONS,
                         ids=["one-variable", "exp-sin", "cubic-log", "three-variables", "quadratic-4"])
def test_numerical_hessian_matches_sympy(it, text, build, n, points):
    f = lambda v: build(v, NUMPY)   # noqa: E731
    for point in points:
        want = _exact_hessian(build, n, point)
        got = _result(lambda: it.numerical_hessian(f, point), _show(want), f"{text} at {point}")
        _float_array(got, (n, n), f"numerical_hessian for {text} (n = {n})")
        _close(got, want, f"the Hessian of {text} at {point} (h = 1e-4)", rtol=1e-5, atol=1e-5,
               hint="diagonal: (f(x + h eᵢ) - 2 f(x) + f(x - h eᵢ)) / h², off the diagonal: four values / (4 h²)")


def test_numerical_hessian_uses_the_centered_formulas_with_the_given_step(it):
    """On these polynomials, with h = 0.25 (a binary number), the two formulas of the docstring are exact in float:
    ((x + h)⁴ - 2 x⁴ + (x - h)⁴) / h² = 12 x² + 2 h² on the diagonal, and the four-point formula gives 3 x² + h² for
    ∂²(x³ z)/∂x∂z, instead of the exact 12 x² and 3 x²."""
    f = lambda v: v[0] ** 4 + v[0] ** 3 * v[2] + v[1] ** 2   # noqa: E731
    want = [[24.125, 0.0, 3.0625], [0.0, 2.0, 0.0], [3.0625, 0.0, 0.0]]
    got = _result(lambda: it.numerical_hessian(f, [1.0, 5.0, 2.0], h=0.25), _show(want),
                  "v0⁴ + v0³ v2 + v1² at (1, 5, 2) with h = 0.25")
    _float_array(got, (3, 3), "numerical_hessian with h = 0.25")
    _close(got, want, "the centered differences of v0⁴ + v0³ v2 + v1² at (1, 5, 2) with h = 0.25", rtol=0, atol=1e-12,
           hint="use h itself, the formulas of the docstring, and the right pair of coordinates (i, j)")


def test_numerical_hessian_is_exactly_symmetric(it):
    f = lambda v: np.exp(v[0] - v[1] ** 2) + np.sin(v[1] * v[2]) / (1.5 + v[0] ** 2)   # noqa: E731
    got = _result(lambda: it.numerical_hessian(f, [0.37, -0.81, 1.29]), "a symmetric 3 × 3 matrix",
                  "a function of three variables")
    _float_array(got, (3, 3), "numerical_hessian for a function of three variables")
    assert np.array_equal(got, got.T), (
        f"expected H[j, i] == H[i, j] exactly, got H = {_show(got)} (compute each entry above the diagonal once, "
        "then copy it below)")


def test_numerical_hessian_evaluates_f_at_most_three_times_per_diagonal_entry_and_four_times_per_pair(it):
    calls = []

    def f(v):
        calls.append(np.array(v, copy=True))
        return float(np.sum(np.asarray(v) ** 3))

    point = [0.5, -1.5, 2.0, 1.0]
    _result(lambda: it.numerical_hessian(f, point), "a 4 × 4 Hessian", "a function of four variables")
    n = len(point)
    limit = 3 * n + 4 * n * (n - 1) // 2
    assert len(calls) <= limit, (
        f"expected at most {limit} evaluations of f for n = {n} (three per diagonal entry, four per entry above "
        f"the diagonal, then copy below), got {len(calls)}")
    shapes = {np.shape(c) for c in calls}
    assert shapes == {(n,)}, f"expected f to be called on 1-D arrays of {n} numbers, got shapes {sorted(shapes)}"
    worst = max(float(np.max(np.abs(c - np.array(point)))) for c in calls)
    assert math.isclose(worst, 1e-4, rel_tol=1e-6), (
        f"expected the points x ± h eᵢ ± h eⱼ with h = 1e-4 (every coordinate within 1e-4 of x), got a coordinate "
        f"moved by {worst:.3g}")


def test_numerical_hessian_does_not_modify_x(it):
    x = np.array([0.25, -1.0])
    f = lambda v: v[0] ** 2 * np.exp(v[1])   # noqa: E731
    _result(lambda: it.numerical_hessian(f, x), "a 2 × 2 Hessian", "x0² e^(x1)")
    assert np.array_equal(x, [0.25, -1.0]), f"expected x to be left unchanged, got {_show(x)} afterwards"


def test_numerical_hessian_accepts_integers_and_one_variable(it):
    got = _result(lambda: it.numerical_hessian(lambda v: np.cos(v[0]), [0]), "[[-1.0]]", "cos at 0, x = [0]")
    _float_array(got, (1, 1), "numerical_hessian of cos at [0]")
    _close(got, [[-1.0]], "the second derivative of cos at 0", rtol=1e-6, atol=1e-6)


@pytest.mark.parametrize("x, h, why", [(2.0, 1e-4, "x is a number, not a 1-D array"),
                                       ([[1.0, 2.0]], 1e-4, "x is 2-D"),
                                       ([], 1e-4, "x is empty"),
                                       ([1.0, 2.0], 0.0, "h = 0"),
                                       ([1.0, 2.0], -1e-4, "h < 0")],
                         ids=["scalar", "two-d", "empty", "h-zero", "h-negative"])
def test_numerical_hessian_refusals(it, x, h, why):
    _expect_error(ValueError, lambda: it.numerical_hessian(lambda v: float(np.sum(v)), x, h=h),
                  f"numerical_hessian(f, {x!r}, h={h!r})", why)


# --- critical_step_size ------------------------------------------------------------------------------------------

def test_critical_step_size_docstring_examples(it):
    got = _result(lambda: it.critical_step_size([[7, 2], [2, 4]]), "0.25", "[[7, 2], [2, 4]], eigenvalues 3 and 8")
    assert isinstance(got, float) and math.isclose(got, 0.25, rel_tol=1e-12), (
        f"expected the float 0.25 (2 / 8) for [[7, 2], [2, 4]], got {got!r}")
    _expect_error(ValueError, lambda: it.critical_step_size([[1, 2], [2, 1]]), "critical_step_size([[1, 2], [2, 1]])",
                  "its eigenvalues are 3 and -1: not positive definite")


@pytest.mark.parametrize("n", [1, 2, 3, 5])
def test_critical_step_size_matches_the_largest_eigenvalue(it, n):
    A = _spd(n, 5210 + n, low=0.3, high=2.0 + 3 * n)
    want = 2.0 / float(np.max(np.linalg.eigvals(A).real))
    got = _result(lambda: it.critical_step_size(A), f"{want:.10g}", f"a {n} × {n} symmetric positive definite matrix")
    assert isinstance(got, float) and math.isclose(got, want, rel_tol=1e-10), (
        f"expected 2 / λmax = {want:.10g} for a {n} × {n} symmetric positive definite matrix, got {got!r}")


def test_critical_step_size_of_diagonal_and_scaled_matrices(it):
    for A, want, text in (([[4.0]], 0.5, "[[4]]"), ([[0.5, 0, 0], [0, 10, 0], [0, 0, 2]], 0.2, "diag(0.5, 10, 2)"),
                          ([[2e6, 1e6], [1e6, 2e6]], 2 / 3e6, "[[2e6, 1e6], [1e6, 2e6]]")):
        got = _result(lambda: it.critical_step_size(A), f"{want:.10g}", text)
        assert isinstance(got, float) and math.isclose(got, want, rel_tol=1e-10), (
            f"expected 2 / λmax = {want:.10g} for {text}, got {got!r}")


def test_critical_step_size_symmetry_tolerance(it):
    """Symmetric up to 1e-12 · max(1, max |A|): a rounding error is accepted, a real asymmetry is not."""
    for A, text in (([[2.0, 1.0 + 1e-14], [1.0, 3.0]], "an asymmetry of 1e-14"),
                    ([[2e6, 1e6 + 1e-7], [1e6, 3e6]], "an asymmetry of 1e-7 on entries of order 1e6")):
        got = _result(lambda: it.critical_step_size(A), "a step (symmetric up to rounding)", text,
                      "a matrix counts as symmetric when |A[i, j] - A[j, i]| ≤ 1e-12 · max(1, max |A|)")
        assert isinstance(got, float) and got > 0, f"expected a positive float for {text}, got {got!r}"
    _expect_error(ValueError, lambda: it.critical_step_size([[2.0, 1.0 + 1e-9], [1.0, 3.0]]),
                  "critical_step_size([[2, 1 + 1e-9], [1, 3]])", "an asymmetry of 1e-9 > 1e-12 · 3: not symmetric")


@pytest.mark.parametrize("A, why", [([[1.0, 2.0, 3.0], [2.0, 1.0, 0.0]], "A is not square"),
                                    ([1.0, 2.0], "A is 1-D"),
                                    ([[2.0, 1.0], [0.0, 2.0]], "A is not symmetric"),
                                    ([[3.0, 0.0], [0.0, 0.0]], "an eigenvalue 0: only semidefinite"),
                                    ([[1.0, 3.0], [3.0, 2.0]], "eigenvalues of both signs"),
                                    ([[-2.0, 0.0], [0.0, -5.0]], "negative definite")],
                         ids=["not-square", "one-d", "not-symmetric", "semidefinite", "indefinite", "negative"])
def test_critical_step_size_refusals(it, A, why):
    _expect_error(ValueError, lambda: it.critical_step_size(A), f"critical_step_size({A!r})", why)


def test_critical_step_size_does_not_modify_A(it):
    A = np.array([[5.0, -1.0], [-1.0, 2.0]])
    _result(lambda: it.critical_step_size(A), "a step", "[[5, -1], [-1, 2]]")
    assert np.array_equal(A, [[5.0, -1.0], [-1.0, 2.0]]), f"expected A to be left unchanged, got {_show(A)} afterwards"


# --- richardson_iterates -----------------------------------------------------------------------------------------

def _closed_form(A, b, omega, x0, n_steps):
    """x_k = x* + (I - ω A)^k (x0 - x*), with x* = A⁻¹ b (np.linalg.solve)."""
    A, b, x0 = (np.asarray(v, dtype=float) for v in (A, b, x0))
    star = np.linalg.solve(A, b)
    M = np.eye(len(b)) - omega * A
    return np.array([star + np.linalg.matrix_power(M, k) @ (x0 - star) for k in range(n_steps + 1)])


def test_richardson_iterates_docstring_example(it):
    want = [[0.0, 0.0], [0.5, 1.0], [0.75, 1.0], [0.875, 1.0]]
    got = _result(lambda: it.richardson_iterates([[2, 0], [0, 4]], [2, 4], omega=0.25, n_steps=3), _show(want),
                  "diag(2, 4), b = (2, 4), ω = 0.25, 3 steps")
    _float_array(got, (4, 2), "richardson_iterates of the docstring example (n_steps = 3)")
    _close(got, want, "the iterates of the docstring example", rtol=0, atol=1e-15)


@pytest.mark.parametrize("n, steps", [(2, 15), (3, 30), (5, 40)])
def test_richardson_iterates_match_the_closed_form(it, n, steps):
    A = _spd(n, 5213 + n)
    rng = np.random.default_rng(5216 + n)
    b, x0 = rng.normal(size=n), rng.normal(size=n)
    omega = 1.5 / float(np.max(np.linalg.eigvals(A).real))
    want = _closed_form(A, b, omega, x0, steps)
    got = _result(lambda: it.richardson_iterates(A, b, omega, x0=x0, n_steps=steps), "the iterates",
                  f"a {n} × {n} system, {steps} steps")
    _float_array(got, (steps + 1, n), f"richardson_iterates for n = {n} and n_steps = {steps}")
    _close(got, want, f"the {steps + 1} iterates x_k = x* + (I - ωA)^k (x0 - x*) of a {n} × {n} system",
           rtol=1e-9, atol=1e-11, hint="x_{k+1} = x_k + ω (b - A x_k), row 0 is x0")


def test_richardson_iterates_of_a_non_symmetric_matrix(it):
    """The function applies the step whatever A is: the convergence is the learner's business, not the function's."""
    A, b, x0 = [[3.0, 1.0], [-1.0, 2.0]], [1.0, -2.0], [0.5, 0.5]
    want = _closed_form(A, b, 0.2, x0, 12)
    got = _result(lambda: it.richardson_iterates(A, b, 0.2, x0=x0, n_steps=12), "the iterates",
                  "a non-symmetric 2 × 2 matrix")
    _float_array(got, (13, 2), "richardson_iterates for a non-symmetric matrix")
    _close(got, want, "the iterates for A = [[3, 1], [-1, 2]], ω = 0.2", rtol=1e-9, atol=1e-12,
           hint="A x is A @ x: mind the order of the product for a matrix that is not symmetric")


def test_richardson_iterates_returns_diverging_iterates_without_error(it):
    A, b = [[1.0, 0.0], [0.0, 5.0]], [1.0, 5.0]
    got = _result(lambda: it.richardson_iterates(A, b, 0.45, n_steps=20), "20 diverging steps",
                  "diag(1, 5) with ω = 0.45 > 2/5")
    _float_array(got, (21, 2), "richardson_iterates with a step too large")
    _close(got, _closed_form(A, b, 0.45, [0.0, 0.0], 20), "the diverging iterates (factor 1 - 0.45 × 5 = -1.25)",
           rtol=1e-12, hint="the function does not check the convergence: it returns the iterates")


def test_richardson_iterates_defaults_and_zero_steps(it):
    A, b = [[4.0, 1.0], [1.0, 3.0]], [1.0, 2.0]
    got = _result(lambda: it.richardson_iterates(A, b, 0.1), "11 rows", "the defaults x0 = 0 and n_steps = 10")
    _float_array(got, (11, 2), "richardson_iterates with the default n_steps = 10")
    _close(got, _closed_form(A, b, 0.1, [0.0, 0.0], 10), "the iterates from x0 = 0", rtol=1e-12, atol=1e-15)
    got = _result(lambda: it.richardson_iterates(A, b, 0.1, x0=[2, -1], n_steps=0), "[[2, -1]]", "n_steps = 0")
    _float_array(got, (1, 2), "richardson_iterates with n_steps = 0")
    _close(got, [[2.0, -1.0]], "the single row x0 when n_steps = 0")
    got = _result(lambda: it.richardson_iterates(A, b, 0.1, n_steps=np.int64(2)), "3 rows", "n_steps = np.int64(2)")
    _float_array(got, (3, 2), "richardson_iterates with n_steps = np.int64(2)")


def test_richardson_iterates_from_the_solution_stay_there(it):
    A, b = [[5.0, 2.0], [2.0, 2.0]], [9.0, 6.0]              # solution (1, 2)
    got = _result(lambda: it.richardson_iterates(A, b, 0.15, x0=[1.0, 2.0], n_steps=5), "five rows (1, 2)",
                  "a start at the solution")
    _close(got, np.tile([1.0, 2.0], (6, 1)), "the iterates started at the solution of A x = b", rtol=0, atol=1e-14,
           hint="a solution is a fixed point: b - A x = 0")


def test_richardson_iterates_leaves_its_inputs_alone(it):
    A, b, x0 = np.array([[2.0, 0.5], [0.5, 1.0]]), np.array([1.0, 1.0]), np.array([3.0, -3.0])
    got = _result(lambda: it.richardson_iterates(A, b, 0.4, x0=x0, n_steps=4), "the iterates", "a 2 × 2 system")
    unchanged = (np.array_equal(A, [[2.0, 0.5], [0.5, 1.0]]) and np.array_equal(b, [1.0, 1.0])
                 and np.array_equal(x0, [3.0, -3.0]))
    assert unchanged, (f"expected A, b and x0 to be left unchanged, got A = {_show(A)}, b = {_show(b)}, "
                       f"x0 = {_show(x0)} afterwards (work on a float copy of x0)")
    got[0, 0] = 99.0
    assert x0[0] == 3.0, "expected row 0 to be a copy of x0, but changing it changed x0"


@pytest.mark.parametrize("args, why", [(([[1.0, 2.0, 3.0]], [1.0], 0.1), "A is not square"),
                                       (([[2.0, 0.0], [0.0, 2.0]], [1.0, 2.0, 3.0], 0.1), "b has 3 coordinates, not 2"),
                                       (([[2.0, 0.0], [0.0, 2.0]], [[1.0, 2.0]], 0.1), "b is 2-D")],
                         ids=["A-not-square", "b-length", "b-two-d"])
def test_richardson_iterates_refuses_bad_shapes(it, args, why):
    _expect_error(ValueError, lambda: it.richardson_iterates(*args), f"richardson_iterates{args!r}", why)


@pytest.mark.parametrize("kwargs, why", [({"x0": [1.0]}, "x0 has 1 coordinate, not 2"),
                                         ({"x0": [1.0], "n_steps": 0}, "x0 has 1 coordinate, not 2, even for 0 steps"),
                                         ({"n_steps": -1}, "a negative number of steps"),
                                         ({"n_steps": 2.5}, "a number of steps that is not an integer")],
                         ids=["x0-length", "x0-length-no-step", "steps-negative", "steps-float"])
def test_richardson_iterates_refuses_bad_start_or_steps(it, kwargs, why):
    _expect_error(ValueError, lambda: it.richardson_iterates([[2.0, 0.0], [0.0, 2.0]], [1.0, 1.0], 0.1, **kwargs),
                  f"richardson_iterates(diag(2, 2), (1, 1), 0.1, {kwargs})", why)


# --- linear_recurrence -------------------------------------------------------------------------------------------

def test_linear_recurrence_docstring_examples(it):
    got = _result(lambda: it.linear_recurrence([1, 1], [0, 1], 10), "Fibonacci", "[1, 1], [0, 1], 10 terms")
    _float_array(got, (10,), "linear_recurrence([1, 1], [0, 1], 10)")
    _close(got, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "the first 10 Fibonacci numbers", rtol=0, atol=0)
    got = _result(lambda: it.linear_recurrence([1, -0.5], [1, 1], 6), "[1, 1, 0.5, 0, -0.25, -0.25]",
                  "[1, -0.5], [1, 1], 6 terms")
    _close(got, [1, 1, 0.5, 0, -0.25, -0.25], "u_{k+2} = u_{k+1} - 0.5 u_k from (1, 1)", rtol=0, atol=1e-15)


def test_linear_recurrence_fibonacci_matches_binet(it):
    phi, psi = (1 + math.sqrt(5)) / 2, (1 - math.sqrt(5)) / 2
    want = [round((phi ** k - psi ** k) / math.sqrt(5)) for k in range(60)]
    got = _result(lambda: it.linear_recurrence([1, 1], [0, 1], 60), "the first 60 Fibonacci numbers", "60 terms")
    _close(got, want, "the first 60 Fibonacci numbers (Binet's formula)", rtol=1e-15, atol=0)


def test_linear_recurrence_with_real_roots_2_and_3(it):
    """u_{k+2} = 5 u_{k+1} - 6 u_k, roots 2 and 3 of r² - 5 r + 6: u_k = 2^k + 3^k from (2, 5)."""
    want = [2 ** k + 3 ** k for k in range(30)]
    got = _result(lambda: it.linear_recurrence([5, -6], [2, 5], 30), "2^k + 3^k", "[5, -6], [2, 5], 30 terms")
    _close(got, want, "u_k = 2^k + 3^k", rtol=0, atol=0,
           hint="coefficients = [c_1, c_2], c_1 multiplies the most recent term: u_{k+2} = 5 u_{k+1} - 6 u_k")


def test_linear_recurrence_coefficients_order(it):
    """[c_1, c_2] = [3, -1]: u_{k+2} = 3 u_{k+1} - u_k; reversing the coefficients gives another sequence."""
    got = _result(lambda: it.linear_recurrence([3, -1], [1, 2], 6), "[1, 2, 5, 13, 34, 89]", "[3, -1], [1, 2]")
    _close(got, [1, 2, 5, 13, 34, 89], "u_{k+2} = 3 u_{k+1} - u_k from (1, 2)", rtol=0, atol=0,
           hint="c_1 multiplies the most recent term u_{k+1}, c_2 the older u_k ([-1, 3] would give 1, 2, 5, 1, ...)")


def test_linear_recurrence_cosines(it):
    """u_{k+2} = 2 cos θ u_{k+1} - u_k from (1, cos θ) gives cos(k θ): complex roots e^{± i θ}, of modulus 1."""
    theta = 0.7
    got = _result(lambda: it.linear_recurrence([2 * math.cos(theta), -1], [1, math.cos(theta)], 40), "cos(k θ)",
                  "θ = 0.7, 40 terms")
    _close(got, [math.cos(k * theta) for k in range(40)], "cos(0.7 k) for k = 0..39", rtol=1e-9, atol=1e-12)


def test_linear_recurrence_order_one_is_geometric(it):
    got = _result(lambda: it.linear_recurrence([-0.5], [3], 8), "3 (-0.5)^k", "[-0.5], [3], 8 terms")
    _float_array(got, (8,), "linear_recurrence of order 1")
    _close(got, [3 * (-0.5) ** k for k in range(8)], "the geometric sequence 3 (-0.5)^k", rtol=0, atol=0)


def test_linear_recurrence_order_three_matches_fractions(it):
    c, start = [Fraction(1, 2), Fraction(1, 4), Fraction(-1, 8)], [Fraction(1), Fraction(-2), Fraction(3)]
    terms = list(start)
    for k in range(3, 25):
        terms.append(c[0] * terms[k - 1] + c[1] * terms[k - 2] + c[2] * terms[k - 3])
    got = _result(lambda: it.linear_recurrence([0.5, 0.25, -0.125], [1, -2, 3], 25), "25 terms",
                  "an order-3 recurrence")
    _float_array(got, (25,), "linear_recurrence of order 3")
    _close(got, [float(t) for t in terms], "u_{k+3} = 0.5 u_{k+2} + 0.25 u_{k+1} - 0.125 u_k from (1, -2, 3)",
           rtol=1e-12, atol=1e-15)


def test_linear_recurrence_fewer_terms_than_initial_values(it):
    for n_terms, want in ((0, []), (1, [4.0]), (2, [4.0, -1.0]), (3, [4.0, -1.0, 0.5])):
        got = _result(lambda: it.linear_recurrence([1, 1, 1], [4, -1, 0.5], n_terms), _show(want),
                      f"n_terms = {n_terms} for an order-3 recurrence")
        _float_array(got, (n_terms,), f"linear_recurrence(..., n_terms={n_terms})")
        _close(got, want, f"the first {n_terms} initial values", rtol=0, atol=0)


def test_linear_recurrence_leaves_its_inputs_alone(it):
    c, start = np.array([0.5, 0.5]), np.array([2.0, 4.0])
    got = _result(lambda: it.linear_recurrence(c, start, 6), "6 terms", "an order-2 recurrence")
    assert np.array_equal(c, [0.5, 0.5]) and np.array_equal(start, [2.0, 4.0]), (
        f"expected coefficients and initial to be left unchanged, got {_show(c)} and {_show(start)} afterwards")
    got[0] = 99.0
    assert start[0] == 2.0, "expected the result to be a new array, but changing it changed initial"
    got = _result(lambda: it.linear_recurrence(c, start, 2), "the 2 initial values", "n_terms = d = 2")
    got[0] = 99.0
    assert start[0] == 2.0, ("expected a new array even when n_terms ≤ d, but changing the result changed initial "
                             "(return a copy of the initial values)")


@pytest.mark.parametrize("args, why", [(([], [], 5), "no coefficient"),
                                       (([1.0, 1.0], [0.0], 5), "2 coefficients but 1 initial value"),
                                       (([1.0], [0.0, 1.0], 5), "1 coefficient but 2 initial values"),
                                       (([1.0, 1.0], [0.0, 1.0], -1), "a negative number of terms"),
                                       (([1.0, 1.0], [0.0, 1.0], 4.0), "a number of terms that is not an integer")],
                         ids=["no-coefficient", "too-few-initial", "too-many-initial", "terms-negative", "terms-float"])
def test_linear_recurrence_refusals(it, args, why):
    _expect_error(ValueError, lambda: it.linear_recurrence(*args), f"linear_recurrence{args!r}", why)
