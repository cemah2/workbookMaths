"""Tests of mymath.approx (chapter M05a): Taylor polynomial, Newton's method, Richardson, epsilon, log-sum-exp.

Oracles: SymPy (derivatives and series), ``scipy.optimize.brentq`` (roots), exact derivatives, ``numpy.finfo`` and
``scipy.special.logsumexp``. They describe the expected behaviour without showing the solution.

    pytest tests/test_m05a_approx.py              # your code
    pytest tests/test_m05a_approx.py --impl=ref   # the reference
"""

import ast
import inspect
import math

import numpy as np
import pytest
import sympy as sp
from scipy import optimize, special


@pytest.fixture
def approx(mymath_module):
    return mymath_module("approx")


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError being reported with what was expected first (``what`` names
    the call, ``hint`` says how to avoid the error)."""
    try:
        return call()
    except NotImplementedError:
        raise                 # a function not written yet: ⏳
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised {type(exc).__name__}: {exc}"
                    + (f" ({hint})" if hint else ""))


def _expect_error(error, call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ``error``."""
    try:
        result = call()
    except NotImplementedError:
        raise                 # first: NotImplementedError is a RuntimeError, it must stay ⏳
    except error:
        return
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise {error.__name__} ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise {error.__name__} ({why}), but it returned {result!r}")


def _python_float(got, what):
    assert type(got) is float, (f"expected {what} to be a Python float (float(...)), got "
                                f"{type(got).__module__}.{type(got).__name__}")


# ---------------------------------------------------------------- no ready-made tool
def test_approx_uses_no_ready_made_tool(approx):
    """approx.py computes its results itself: neither scipy.special.logsumexp, numpy.finfo nor sys.float_info."""
    try:
        tree = ast.parse(inspect.getsource(approx))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in ("finfo", "float_info", "logsumexp"):
            found.add(node.attr)
        elif isinstance(node, ast.ImportFrom) and node.module:
            found.update(alias.name for alias in node.names if alias.name in ("finfo", "float_info", "logsumexp"))
        elif isinstance(node, ast.Name) and node.id in ("finfo", "float_info"):
            found.add(node.id)
    assert not found, (
        f"expected approx.py to use none of numpy.finfo, sys.float_info, scipy.special.logsumexp (the tests compare "
        f"your results with them), found {sorted(found)}: compute epsilon by halving, and log-sum-exp yourself")


# ---------------------------------------------------------------- taylor_polynomial
def _sympy_derivatives(expr, a, order):
    x = sp.Symbol("x")
    return [float(sp.diff(expr(x), x, k).subs(x, a)) for k in range(order + 1)]


def _sympy_taylor_value(expr, a, order, at):
    x = sp.Symbol("x")
    series = sp.series(expr(x), x, a, order + 1).removeO()
    return float(series.subs(x, at))


def test_taylor_polynomial_docstring_example(approx):
    got = _result(lambda: approx.taylor_polynomial([1, 1, 1, 1], 0, 0.5), "about 1.645833")
    assert got == pytest.approx(1 + 0.5 + 0.125 + 0.125 / 6, rel=1e-12), f"expected 1.6458333 (1 + x + x²/2 + x³/6), got {got!r}"


@pytest.mark.parametrize("name, expr, a, order, at", [
    ("exp at 0.3, order 6", sp.exp, 0.3, 6, 1.1),
    ("cos at 1.2, order 5", sp.cos, 1.2, 5, 0.4),
    ("log at 2, order 4", sp.log, 2.0, 4, 2.7),
    ("sqrt at 9, order 3", sp.sqrt, 9.0, 3, 7.5),
], ids=["exp-0.3-6", "cos-1.2-5", "log-2-4", "sqrt-9-3"])
def test_taylor_polynomial_matches_sympy_series(approx, name, expr, a, order, at):
    derivatives = _sympy_derivatives(expr, a, order)
    expected = _sympy_taylor_value(expr, a, order, at)
    got = _result(lambda: approx.taylor_polynomial(derivatives, a, at), f"{expected:.12g}", f"{name} at x = {at}")
    assert got == pytest.approx(expected, rel=1e-10, abs=1e-12), (
        f"expected {expected:.12g} for {name} at x = {at} (the Taylor polynomial of SymPy), got {got!r}: each term is "
        "f⁽ᵏ⁾(a) (x - a)**k / k! (check the factorial k! and the powers of x - a)")


def test_taylor_polynomial_at_its_centre_is_the_value(approx):
    got = _result(lambda: approx.taylor_polynomial([2.5, -7.0, 3.0, 11.0], 1.75, 1.75), "2.5")
    assert got == pytest.approx(2.5, abs=1e-12), f"expected 2.5 = f(a) at x = a (every other term is 0), got {got!r}"


def test_taylor_polynomial_with_many_terms_does_not_overflow(approx):
    derivatives = [1.0] * 200                      # exp at 0: 200 terms, beyond 170! (the largest float factorial)
    got = _result(lambda: approx.taylor_polynomial(derivatives, 0.0, 3.0), f"{math.exp(3):.12g}", "200 terms",
                  "math.factorial(200) and 3.0**199 do not fit in a float together: keep (x - a)**k / k! up to date")
    assert got == pytest.approx(math.exp(3), rel=1e-12), f"expected e³ = {math.exp(3):.12g} with 200 terms, got {got!r}"


def test_taylor_polynomial_accepts_tuples_and_arrays(approx):
    for derivatives in ((0.0, 1.0, 0.0, -1.0), np.array([0.0, 1.0, 0.0, -1.0])):
        got = _result(lambda: approx.taylor_polynomial(derivatives, 0.0, 0.6), "0.564", type(derivatives).__name__)
        assert got == pytest.approx(0.6 - 0.6 ** 3 / 6, rel=1e-12), (
            f"expected 0.564 (sin at 0, order 3, at 0.6) with derivatives given as a {type(derivatives).__name__}, got {got!r}")


def test_taylor_polynomial_returns_a_python_float(approx):
    _python_float(_result(lambda: approx.taylor_polynomial([1, 2, 3], 0, 2), "a float"), "taylor_polynomial([1, 2, 3], 0, 2)")
    _python_float(_result(lambda: approx.taylor_polynomial(np.array([1.0, 2.0]), 0, 2), "a float"),
                  "taylor_polynomial(np.array([1.0, 2.0]), 0, 2)")


def test_taylor_polynomial_refuses_no_derivative(approx):
    _expect_error(ValueError, lambda: approx.taylor_polynomial([], 0, 1), "taylor_polynomial([], 0, 1)",
                  "at least one derivative is needed")


# ---------------------------------------------------------------- newton
def test_newton_docstring_example(approx):
    got = _result(lambda: approx.newton(lambda x: x * x - 2, lambda x: 2 * x, 1.0), "about 1.4142135624")
    assert got == pytest.approx(math.sqrt(2), abs=1e-12), f"expected √2 = 1.41421356237, got {got!r}"


@pytest.mark.parametrize("name, f, fprime, x0, bracket", [
    ("cos(x) - x", lambda x: math.cos(x) - x, lambda x: -math.sin(x) - 1, 0.5, (0, 1)),
    ("x³ - x - 1", lambda x: x ** 3 - x - 1, lambda x: 3 * x ** 2 - 1, 1.5, (1, 2)),
    ("exp(x) - 5", lambda x: math.exp(x) - 5, math.exp, 2.0, (1, 2)),
    ("x·ln(x) - 2", lambda x: x * math.log(x) - 2, lambda x: math.log(x) + 1, 2.0, (2, 3)),
], ids=["cos-x", "cubic", "exp", "xlnx"])
def test_newton_finds_the_root(approx, name, f, fprime, x0, bracket):
    expected = optimize.brentq(f, *bracket, xtol=1e-15)
    got = _result(lambda: approx.newton(f, fprime, x0), f"{expected:.12g}", f"newton on {name} from {x0}")
    assert got == pytest.approx(expected, abs=1e-10), (
        f"expected the root {expected:.12g} of {name} (from x0 = {x0}), got {got!r}: x ← x - f(x) / f'(x)")


def test_newton_stops_as_soon_as_two_values_are_close(approx):
    calls = []

    def f(x):
        calls.append(x)
        return x * x - 3

    got = _result(lambda: approx.newton(f, lambda x: 2 * x, 2.0, tol=0.01), "about 1.7321", "tol = 0.01")
    # 2 → 1.75 → 1.732142857… (|step| = 0.018 ≥ 0.01) → 1.7320508… (|step| < 0.01): stop there
    assert got == pytest.approx(1.7320508100147276, abs=1e-12), (
        f"expected 1.73205081 (the first value whose step from the previous one is below tol = 0.01), got {got!r}: "
        "return the new value as soon as |x_new - x| < tol")
    points = len(set(calls))                       # f evaluated twice at the same point is fine; one step too many is not
    assert points <= 4, (f"expected f to be evaluated at no more than 4 different points with tol = 0.01, got {points}: "
                         "stop as soon as |x_new - x| < tol, without taking one more step")


def test_newton_returns_a_zero_found_exactly(approx):
    got = _result(lambda: approx.newton(lambda x: x - 6.5, lambda x: 0.0, 6.5), "6.5", "f(x0) = 0 with f'(x0) = 0",
                  "test f(x) == 0 before dividing by f'(x)")
    assert got == 6.5, f"expected 6.5: f(6.5) = 0 exactly, so x0 is already the zero (no step, no division), got {got!r}"


def test_newton_refuses_a_horizontal_tangent(approx):
    _expect_error(ValueError, lambda: approx.newton(lambda x: x * x + 1, lambda x: 2 * x, 0.0),
                  "newton(x² + 1, 2x, 0.0)", "f'(0) = 0: the tangent is horizontal")


def test_newton_raises_when_it_does_not_converge(approx):
    _expect_error(RuntimeError, lambda: approx.newton(lambda x: x ** 3 - 2 * x + 2, lambda x: 3 * x ** 2 - 2, 0.0),
                  "newton(x³ - 2x + 2, 3x² - 2, 0.0)", "the sequence cycles 0, 1, 0, 1… and never stops")
    _expect_error(RuntimeError, lambda: approx.newton(lambda x: x * x - 11, lambda x: 2 * x, 3.0, max_iter=1),
                  "newton(x² - 11, 2x, 3.0, max_iter=1)", "one step is not enough to reach tol = 1e-12")


def test_newton_returns_a_python_float(approx):
    _python_float(_result(lambda: approx.newton(lambda x: x - 1, lambda x: 1, 4), "a float"), "newton(x - 1, 1, 4)")


# ---------------------------------------------------------------- richardson_derivative
def test_richardson_derivative_docstring_example(approx):
    got = _result(lambda: approx.richardson_derivative(lambda x: x ** 5, 1.0, 0.1), "4.999975")
    assert got == pytest.approx(4.999975, abs=1e-10), f"expected 4.999975, got {got!r}: (4 D(h/2) - D(h)) / 3"


@pytest.mark.parametrize("name, f, df, x", [
    ("sin at 0.4", math.sin, math.cos, 0.4),
    ("exp at -1.3", math.exp, math.exp, -1.3),
    ("atan at 2", math.atan, lambda x: 1 / (1 + x * x), 2.0),
], ids=["sin", "exp", "atan"])
def test_richardson_derivative_is_accurate(approx, name, f, df, x):
    got = _result(lambda: approx.richardson_derivative(f, x), f"{df(x):.12g}", f"{name}, h = 0.01")
    assert got == pytest.approx(df(x), abs=1e-10), (
        f"expected {df(x):.12g} (the derivative of {name}) to about 1e-10 with h = 0.01, got {got!r}: its error is in "
        "h⁴; a centred difference alone would be off by about 1e-5")


def test_richardson_derivative_is_exact_for_a_polynomial_of_degree_4(approx):
    f = lambda x: 3 * x ** 4 - x ** 2 + 5          # noqa: E731
    expected = 12 * (-0.7) ** 3 - 2 * (-0.7)
    got = _result(lambda: approx.richardson_derivative(f, -0.7, 0.3), f"{expected:.12g}", "3x⁴ - x² + 5 at -0.7")
    assert got == pytest.approx(expected, abs=1e-11), (
        f"expected {expected:.12g}: for a polynomial of degree 4 the h⁴ term vanishes too, the result is exact, got {got!r}")


def test_richardson_derivative_error_is_divided_by_16_when_h_is_halved(approx):
    errors = [abs(_result(lambda h=h: approx.richardson_derivative(math.exp, 0.7, h), "a float") - math.exp(0.7))
              for h in (0.4, 0.2)]
    ratio = errors[0] / errors[1] if errors[1] else math.inf
    assert 13 < ratio < 19, (
        f"expected the error to be divided by about 16 = 2⁴ when h goes from 0.4 to 0.2 (an error in h⁴), got a ratio "
        f"of {ratio:.3g}: combine (4 D(h/2) - D(h)) / 3 with the centred difference D")


def test_richardson_derivative_uses_the_four_points_x_plus_or_minus_h_and_h_over_2(approx):
    points = []

    def f(t):
        points.append(t)
        return math.sin(t)

    _result(lambda: approx.richardson_derivative(f, 1.0, 0.2), "a float")
    allowed = {1.2, 0.8, 1.1, 0.9}
    unexpected = sorted({round(t, 12) for t in points} - allowed)
    assert not unexpected, (
        f"expected f to be evaluated only at x ± h and x ± h/2 (1.2, 0.8, 1.1, 0.9 for x = 1, h = 0.2), got also "
        f"{unexpected}: D(h) is the centred difference (f(x + h) - f(x - h)) / (2h)")


@pytest.mark.parametrize("h", [0, -0.01], ids=["h=0", "h<0"])
def test_richardson_derivative_refuses_a_step_that_is_not_positive(approx, h):
    _expect_error(ValueError, lambda: approx.richardson_derivative(math.sin, 1.0, h),
                  f"richardson_derivative(sin, 1.0, {h})", "the step h must be positive")


def test_richardson_derivative_returns_a_python_float(approx):
    _python_float(_result(lambda: approx.richardson_derivative(lambda x: np.float64(x) ** 2, 1.0), "a float"),
                  "richardson_derivative of a function that returns NumPy floats")


# ---------------------------------------------------------------- machine_epsilon
def test_machine_epsilon_docstring_example(approx):
    got = _result(lambda: approx.machine_epsilon(), "2**-52")
    assert got == 2.0 ** -52, f"expected 2**-52 = {2.0 ** -52!r}, got {got!r}"


@pytest.mark.parametrize("dtype", [float, np.float64, np.float32, np.float16], ids=["float", "float64", "float32", "float16"])
def test_machine_epsilon_matches_numpy_finfo(approx, dtype):
    expected = float(np.finfo(dtype).eps)
    got = _result(lambda: approx.machine_epsilon(dtype), f"{expected!r}", f"machine_epsilon({dtype.__name__})",
                  "compute in that type: one = dtype(1), and dtype(...) after each operation")
    assert got == expected, (
        f"expected {expected!r} for {dtype.__name__}, got {got!r}: halve eps while dtype(1) + eps / 2 differs from "
        "dtype(1), every computation in that type")


def test_machine_epsilon_is_the_gap_after_one(approx):
    eps = _result(lambda: approx.machine_epsilon(np.float32), "2**-23")
    one = np.float32(1)
    assert one + np.float32(eps) != one and one + np.float32(eps) / np.float32(2) == one, (
        f"expected 1 + eps to differ from 1 and 1 + eps/2 to equal 1 in float32, got eps = {eps!r}")


def test_machine_epsilon_returns_a_python_float(approx):
    for dtype in (float, np.float32):
        _python_float(_result(lambda: approx.machine_epsilon(dtype), "a float"), f"machine_epsilon({dtype.__name__})")


# ---------------------------------------------------------------- logsumexp
def test_logsumexp_docstring_examples(approx):
    for values, expected in (([0, 0], math.log(2)), ([1000, 1000], 1000 + math.log(2))):
        got = _result(lambda: approx.logsumexp(values), f"{expected:.6f}", f"logsumexp({values})")
        assert got == pytest.approx(expected, rel=1e-12), f"expected {expected:.9f} for logsumexp({values}), got {got!r}"


@pytest.mark.parametrize("values", [
    [0.3, -1.2, 2.5, 0.0], [-745.0, -750.0, -760.5], [900.0, 899.0, 850.0, 120.0], [1e-3], [-3.0] * 10,
], ids=["small", "very negative", "very large", "one value", "ten equal"])
def test_logsumexp_matches_scipy(approx, values):
    expected = float(special.logsumexp(values))
    got = _result(lambda: approx.logsumexp(values), f"{expected:.12g}", f"logsumexp({values})",
                  "factor out the largest value before taking exponentials")
    assert got == pytest.approx(expected, rel=1e-12, abs=1e-12), (
        f"expected {expected:.12g} for logsumexp({values}), got {got!r}: ln Σ exp(v) = m + ln Σ exp(v - m), m the largest value")


def test_logsumexp_with_minus_infinity(approx):
    got = _result(lambda: approx.logsumexp([-math.inf, 1.5, -math.inf]), "1.5")
    assert got == pytest.approx(1.5, rel=1e-12), f"expected 1.5: exp(-inf) = 0 adds nothing, got {got!r}"
    got = _result(lambda: approx.logsumexp([-math.inf, -math.inf]), "-math.inf", "every value -inf",
                  "with m = -inf, v - m is inf - inf = nan: return -inf first")
    assert got == -math.inf, f"expected -math.inf when every value is -inf (a sum of zeros), got {got!r}"


def test_logsumexp_accepts_arrays_and_tuples(approx):
    for values in (np.array([1.0, 2.0, 3.0]), (1.0, 2.0, 3.0)):
        got = _result(lambda: approx.logsumexp(values), "3.407606", type(values).__name__)
        assert got == pytest.approx(float(special.logsumexp([1.0, 2.0, 3.0])), rel=1e-12), (
            f"expected 3.40760596 for (1, 2, 3) given as a {type(values).__name__}, got {got!r}")


def test_logsumexp_returns_a_python_float(approx):
    _python_float(_result(lambda: approx.logsumexp(np.array([0.5, 1.5])), "a float"), "logsumexp(np.array([0.5, 1.5]))")


def test_logsumexp_refuses_an_empty_sequence(approx):
    _expect_error(ValueError, lambda: approx.logsumexp([]), "logsumexp([])", "the log of an empty sum is not defined")
