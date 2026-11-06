"""Tests of mymath.integrate (chapter M02a): Riemann sums, trapezoids, Simpson, CDF from a density, quantiles.

Oracles: exact sums with ``fractions.Fraction``, ``numpy.trapezoid``, ``scipy.integrate.simpson`` and
``scipy.integrate.quad``, exact integrals with SymPy, and ``scipy.stats`` for quantiles. They describe the expected
behaviour without showing the solution.

    pytest tests/test_m02a_integrate.py              # your code
    pytest tests/test_m02a_integrate.py --impl=ref   # the reference
"""

import ast
import inspect
import math
from fractions import Fraction

import numpy as np
import pytest
import sympy as sp
from scipy import integrate as sci_integrate
from scipy import stats

CALL_LIMIT = 5_000


@pytest.fixture
def integrate(mymath_module):
    return mymath_module("integrate")


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
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned {result!r}")


def _counted(f):
    """f, which stops a loop that never ends: past CALL_LIMIT calls it raises with a message."""
    calls = 0

    def wrapped(x):
        nonlocal calls
        calls += 1
        if calls > CALL_LIMIT:
            raise RuntimeError(f"the function was called more than {CALL_LIMIT} times: does your loop stop? (stop "
                               "when the interval is shorter than tol, and after 200 halvings even when tol = 0)")
        return f(x)

    return wrapped


def _cubic(x):
    return 2 * x ** 3 - 3 * x + 1


def _exact_sum(f, points, h):
    """h × Σ f(points), computed exactly with fractions (the oracle of a Riemann sum)."""
    return float(h * sum(f(Fraction(p)) for p in points))


# ---------------------------------------------------------------- no ready-made integrator
def test_integrate_uses_no_ready_made_integrator(integrate):
    """integrate.py writes the sums itself: no SciPy, and no numpy.trapezoid (or trapz)."""
    try:
        tree = ast.parse(inspect.getsource(integrate))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    imported, attributes = set(), set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
            attributes.update(alias.name for alias in node.names)
        elif isinstance(node, ast.Attribute):
            attributes.add(node.attr)
    assert "scipy" not in imported, (
        "expected integrate.py not to import SciPy (the tests compare your sums with scipy.integrate): write the "
        "sums yourself")
    used = sorted(attributes & {"trapezoid", "trapz", "simpson", "quad", "cumulative_trapezoid"})
    assert not used, (f"expected integrate.py to write the sums itself, not to call {', '.join(used)}: a loop (or "
                      "sum over a generator) is the exercise")


# ---------------------------------------------------------------- riemann_sum
def test_riemann_sum_docstring_example(integrate):
    got = _result(lambda: integrate.riemann_sum(lambda x: x, 0, 1, 4), "0.375 (the docstring example)")
    assert got == pytest.approx(0.375, abs=1e-12), f"expected 0.375 (the docstring example), got {got!r}"
    got = _result(lambda: integrate.riemann_sum(lambda x: x, 0, 1, 4, rule="midpoint"), "0.5 (docstring)")
    assert got == pytest.approx(0.5, abs=1e-12), f"expected 0.5 (the midpoint example of the docstring), got {got!r}"


@pytest.mark.parametrize("rule, shift", [("left", Fraction(0)), ("right", Fraction(1)), ("midpoint", Fraction(1, 2))],
                         ids=["left", "right", "midpoint"])
@pytest.mark.parametrize("a, b, n", [(1, 3, 4), (-2, 1, 6), (0, 5, 1), (Fraction(1, 2), Fraction(9, 4), 7)],
                         ids=["1-3-n4", "-2-1-n6", "0-5-n1", "half-n7"])
def test_riemann_sum_matches_the_exact_sum(integrate, rule, shift, a, b, n):
    h = Fraction(b - a) / n
    expected = _exact_sum(_cubic, [a + (i + shift) * h for i in range(n)], h)
    got = _result(lambda: integrate.riemann_sum(_cubic, float(a), float(b), n, rule=rule),
                  f"{expected} (the {rule} sum, computed exactly)")
    assert got == pytest.approx(expected, rel=1e-12, abs=1e-12), (
        f"expected {expected} (h × the sum of the heights read at the {rule} {'ends' if rule != 'midpoint' else 'points'} "
        f"of the {n} rectangles of [{float(a)}, {float(b)}]), got {got!r}")


def test_riemann_sum_default_rule_is_left(integrate):
    expected = _exact_sum(_cubic, [Fraction(i, 2) for i in range(6)], Fraction(1, 2))
    got = _result(lambda: integrate.riemann_sum(_cubic, 0, 3, 6), f"{expected} (the left sum)")
    assert got == pytest.approx(expected, rel=1e-12), (
        f"expected {expected} (without rule=..., the heights are read at the left ends), got {got!r}")


def test_riemann_sum_returns_a_float(integrate):
    got = _result(lambda: integrate.riemann_sum(lambda x: 3, 0, 2, 4), "6.0 (a float)")
    assert isinstance(got, float), f"expected a float (as the docstring says), got {type(got).__name__} {got!r}"
    assert got == pytest.approx(6.0), f"expected 6.0 (a constant 3 on an interval of length 2), got {got!r}"


@pytest.mark.parametrize("rule, mirror", [("left", "right"), ("right", "left"), ("midpoint", "midpoint")],
                         ids=["left", "right", "midpoint"])
def test_riemann_sum_with_reversed_bounds(integrate, rule, mirror):
    forward = _result(lambda: integrate.riemann_sum(_cubic, -1, 2, 5, rule=mirror), f"the {mirror} sum on [-1, 2]")
    got = _result(lambda: integrate.riemann_sum(_cubic, 2, -1, 5, rule=rule),
                  f"{-forward} (minus the {mirror} sum on [-1, 2])")
    assert got == pytest.approx(-forward, rel=1e-12), (
        f"expected {-forward} with a > b: h = (b - a)/n is negative, and the same formula gives minus the {mirror} sum "
        f"on [b, a]; got {got!r}")


def test_riemann_sum_converges_to_the_integral(integrate):
    exact = float(sp.integrate(sp.exp(sp.Symbol("x")) * sp.sin(sp.Symbol("x")), (sp.Symbol("x"), 0, 2)))
    f = lambda x: math.exp(x) * math.sin(x)   # noqa: E731
    errors = {}
    for rule in ("left", "midpoint"):
        e1 = abs(_result(lambda: integrate.riemann_sum(f, 0, 2, 200, rule=rule), "a Riemann sum") - exact)
        e2 = abs(integrate.riemann_sum(f, 0, 2, 400, rule=rule) - exact)
        errors[rule] = (e1, e2)
    left1, left2 = errors["left"]
    mid1, mid2 = errors["midpoint"]
    assert 1.7 < left1 / left2 < 2.3, (
        f"expected the error of the left sum to be divided by about 2 when n doubles (errors {left1:.2e} and "
        f"{left2:.2e})")
    assert 3.5 < mid1 / mid2 < 4.5, (
        f"expected the error of the midpoint sum to be divided by about 4 when n doubles (errors {mid1:.2e} and "
        f"{mid2:.2e})")


@pytest.mark.parametrize("n", [0, -3], ids=["n0", "n-3"])
def test_riemann_sum_refuses_n_below_1(integrate, n):
    _expect_value_error(lambda: integrate.riemann_sum(_cubic, 0, 1, n), f"riemann_sum(f, 0, 1, {n})",
                        "there must be at least one rectangle")


@pytest.mark.parametrize("rule", ["center", "Left", "trapezoid"], ids=["center", "Left", "trapezoid"])
def test_riemann_sum_refuses_an_unknown_rule(integrate, rule):
    _expect_value_error(lambda: integrate.riemann_sum(_cubic, 0, 1, 4, rule=rule),
                        f"riemann_sum(f, 0, 1, 4, rule={rule!r})", "the rule is 'left', 'right' or 'midpoint'")


# ---------------------------------------------------------------- trapezoid
def test_trapezoid_docstring_example(integrate):
    got = _result(lambda: integrate.trapezoid(lambda x: x ** 2, 0, 2, 2), "3.0 (the docstring example)")
    assert got == pytest.approx(3.0, abs=1e-12), f"expected 3.0 (the docstring example), got {got!r}"


@pytest.mark.parametrize("a, b, n", [(0, 1, 1), (-1, 3, 5), (0.5, 4.25, 12), (2, 7, 37)],
                         ids=["n1", "n5", "n12", "n37"])
def test_trapezoid_matches_numpy(integrate, a, b, n):
    f = lambda x: math.cos(x) + x ** 2 / 10   # noqa: E731
    xs = np.linspace(a, b, n + 1)
    expected = float(np.trapezoid([f(x) for x in xs], xs))
    got = _result(lambda: integrate.trapezoid(f, a, b, n), f"{expected} (numpy.trapezoid on {n + 1} points)")
    assert got == pytest.approx(expected, rel=1e-10, abs=1e-12), (
        f"expected {expected} (h × (f(x0)/2 + f(x1) + ... + f(x(n-1)) + f(xn)/2), as numpy.trapezoid on the "
        f"{n + 1} points), got {got!r}")


@pytest.mark.parametrize("n", [1, 3, 10], ids=["n1", "n3", "n10"])
def test_trapezoid_is_exact_for_an_affine_function(integrate, n):
    got = _result(lambda: integrate.trapezoid(lambda x: 7 - 3 * x, -2, 4, n), "24.0")
    assert got == pytest.approx(24.0, abs=1e-12), (
        f"expected 24.0 (the trapezoids follow a straight line exactly: ∫_-2^4 (7 - 3x) dx = 24), got {got!r}")


def test_trapezoid_returns_a_float_and_handles_reversed_bounds(integrate):
    forward = _result(lambda: integrate.trapezoid(_cubic, 0, 3, 6), "a float")
    assert isinstance(forward, float), f"expected a float (as the docstring says), got {type(forward).__name__}"
    backward = integrate.trapezoid(_cubic, 3, 0, 6)
    assert backward == pytest.approx(-forward, rel=1e-12), (
        f"expected {-forward} with the bounds reversed (minus the integral from 0 to 3), got {backward!r}")


def test_trapezoid_error_is_divided_by_about_4(integrate):
    exact = 1 - math.cos(1.5)
    e1 = abs(_result(lambda: integrate.trapezoid(math.sin, 0, 1.5, 50), "a trapezoid sum") - exact)
    e2 = abs(integrate.trapezoid(math.sin, 0, 1.5, 100) - exact)
    assert 3.6 < e1 / e2 < 4.4, f"expected the error to be divided by about 4 when n doubles ({e1:.2e}, {e2:.2e})"


def test_trapezoid_refuses_n_below_1(integrate):
    _expect_value_error(lambda: integrate.trapezoid(_cubic, 0, 1, 0), "trapezoid(f, 0, 1, 0)",
                        "there must be at least one interval")


# ---------------------------------------------------------------- simpson
def test_simpson_docstring_example(integrate):
    got = _result(lambda: integrate.simpson(lambda x: x ** 3, 0, 2, 2), "4.0 (the docstring example)")
    assert got == pytest.approx(4.0, abs=1e-12), f"expected 4.0 (the docstring example), got {got!r}"


@pytest.mark.parametrize("n", [2, 4, 10], ids=["n2", "n4", "n10"])
def test_simpson_is_exact_for_a_cubic(integrate, n):
    x = sp.Symbol("x")
    exact = float(sp.integrate(2 * x ** 3 - 3 * x + 1, (x, -1, 2)))
    got = _result(lambda: integrate.simpson(_cubic, -1, 2, n), f"{exact} (exact for a polynomial of degree 3)")
    assert got == pytest.approx(exact, abs=1e-10), (
        f"expected {exact} (Simpson's rule is exact for a polynomial of degree at most 3), got {got!r}")


@pytest.mark.parametrize("a, b, n", [(0, 2, 2), (-1, 3, 8), (1, 6, 20)], ids=["n2", "n8", "n20"])
def test_simpson_matches_scipy(integrate, a, b, n):
    f = lambda x: math.exp(-x / 3) * (1 + x ** 2)   # noqa: E731
    xs = np.linspace(a, b, n + 1)
    expected = float(sci_integrate.simpson([f(x) for x in xs], x=xs))
    got = _result(lambda: integrate.simpson(f, a, b, n), f"{expected} (scipy.integrate.simpson)")
    assert got == pytest.approx(expected, rel=1e-10), (
        f"expected {expected} (h/3 × (f(x0) + 4 f(x1) + 2 f(x2) + ... + 4 f(x(n-1)) + f(xn)), as "
        f"scipy.integrate.simpson on the {n + 1} points), got {got!r}")


def test_simpson_error_is_divided_by_about_16(integrate):
    exact = 1 - math.cos(1.5)
    e1 = abs(_result(lambda: integrate.simpson(math.sin, 0, 1.5, 10), "a Simpson sum") - exact)
    e2 = abs(integrate.simpson(math.sin, 0, 1.5, 20) - exact)
    assert 14 < e1 / e2 < 18, f"expected the error to be divided by about 16 when n doubles ({e1:.2e}, {e2:.2e})"


def test_simpson_returns_a_float_and_handles_reversed_bounds(integrate):
    forward = _result(lambda: integrate.simpson(math.exp, 0, 1, 4), "a float")
    assert isinstance(forward, float), f"expected a float (as the docstring says), got {type(forward).__name__}"
    backward = integrate.simpson(math.exp, 1, 0, 4)
    assert backward == pytest.approx(-forward, rel=1e-12), (
        f"expected {-forward} with the bounds reversed (minus the integral from 0 to 1), got {backward!r}")


@pytest.mark.parametrize("n", [3, 7, 0, 1, -2], ids=["n3", "n7", "n0", "n1", "n-2"])
def test_simpson_refuses_odd_or_small_n(integrate, n):
    _expect_value_error(lambda: integrate.simpson(_cubic, 0, 1, n), f"simpson(f, 0, 1, {n})",
                        "Simpson's rule needs an even number of intervals, at least 2")


# ---------------------------------------------------------------- cdf_from_pdf
def test_cdf_from_pdf_docstring_example(integrate):
    got = _result(lambda: integrate.cdf_from_pdf(lambda t: 2 * t, 0.5, 0), "0.25 (the docstring example)")
    assert got == pytest.approx(0.25, abs=1e-6), f"expected 0.25 (the docstring example), got {got!r}"


@pytest.mark.parametrize("x", [-3.0, 0.0, 1.0], ids=["far-below", "below", "at-lower"])
def test_cdf_from_pdf_is_zero_up_to_lower(integrate, x):
    got = _result(lambda: integrate.cdf_from_pdf(lambda t: 0.5, x, 1.0), "0.0")
    assert got == 0.0, f"expected 0.0 for x = {x} <= lower = 1.0 (no probability below lower), got {got!r}"


@pytest.mark.parametrize("x", [0.3, 1.0, 2.5, 6.0], ids=["0.3", "1", "2.5", "6"])
def test_cdf_from_pdf_matches_quad(integrate, x):
    pdf = lambda t: t * math.exp(-t)   # noqa: E731 - the density of a sum of two exponential waiting times
    expected = sci_integrate.quad(pdf, 0, x)[0]
    got = _result(lambda: integrate.cdf_from_pdf(pdf, x, 0), f"{expected} (scipy.integrate.quad)")
    assert got == pytest.approx(expected, abs=1e-5), (
        f"expected F({x}) ≈ {expected} (the integral of the density from lower to x), got {got!r}")


def test_cdf_from_pdf_uses_the_trapezoid_rule_with_n_intervals(integrate):
    pdf = lambda t: 3 * t ** 2   # noqa: E731
    got = _result(lambda: integrate.cdf_from_pdf(pdf, 1.0, 0.0, n=1), "1.5")
    assert got == pytest.approx(1.5, abs=1e-12), (
        f"expected 1.5 with n=1: one trapezoid, (1 - 0) × (pdf(0) + pdf(1))/2 (the exact value would be 1), "
        f"got {got!r}")
    got = integrate.cdf_from_pdf(pdf, 1.0, 0.0, n=2)
    assert got == pytest.approx(1.125, abs=1e-12), f"expected 1.125 with n=2 trapezoids, got {got!r}"


def test_cdf_from_pdf_returns_a_float(integrate):
    got = _result(lambda: integrate.cdf_from_pdf(lambda t: 1, 0.5, 0), "0.5 (a float)")
    assert isinstance(got, float), f"expected a float (as the docstring says), got {type(got).__name__} {got!r}"


def test_cdf_from_pdf_refuses_n_below_1(integrate):
    _expect_value_error(lambda: integrate.cdf_from_pdf(lambda t: 1, 0.5, 0, n=0), "cdf_from_pdf(pdf, 0.5, 0, n=0)",
                        "the trapezoid rule needs at least one interval")


# ---------------------------------------------------------------- quantile
def test_quantile_docstring_example(integrate):
    got = _result(lambda: integrate.quantile(_counted(lambda x: x ** 2), 0.25, 0, 1), "0.5 (the docstring example)")
    assert got == pytest.approx(0.5, abs=1e-9), f"expected 0.5 (the docstring example), got {got!r}"


@pytest.mark.parametrize("p", [0.05, 0.5, 0.9, 0.999], ids=["0.05", "0.5", "0.9", "0.999"])
def test_quantile_of_an_exponential_law_matches_scipy(integrate, p):
    rate = 1.5
    cdf = _counted(lambda x: 1 - math.exp(-rate * x))
    expected = float(stats.expon.ppf(p, scale=1 / rate))
    got = _result(lambda: integrate.quantile(cdf, p, 0, 20), f"{expected} (scipy.stats.expon.ppf)")
    assert got == pytest.approx(expected, abs=1e-8), (
        f"expected the quantile of order {p} ≈ {expected} (where the CDF reaches {p}), got {got!r}")


def test_quantile_of_a_normal_law_matches_scipy(integrate):
    cdf = _counted(lambda x: stats.norm.cdf(x, loc=2, scale=3))
    expected = float(stats.norm.ppf(0.8, loc=2, scale=3))
    got = _result(lambda: integrate.quantile(cdf, 0.8, -50, 50), f"{expected} (scipy.stats.norm.ppf)")
    assert got == pytest.approx(expected, abs=1e-8), f"expected {expected} (quantile of order 0.8), got {got!r}"


def test_quantile_on_a_flat_part_is_the_smallest_x(integrate):
    def cdf(x):   # no probability between 1 and 3: F stays at 0.5 there
        if x < 0:
            return 0.0
        if x < 1:
            return x / 2
        if x < 3:
            return 0.5
        return min(1.0, 0.5 + (x - 3) / 2)
    got = _result(lambda: integrate.quantile(_counted(cdf), 0.5, -1, 5), "1.0")
    assert got == pytest.approx(1.0, abs=1e-8), (
        f"expected 1.0: the quantile is the SMALLEST x with cdf(x) >= p (F reaches 0.5 at 1 and stays flat until 3); "
        f"keep the half where cdf(mid) < p on the left; got {got!r}")


def test_quantile_respects_tol(integrate):
    got = _result(lambda: integrate.quantile(_counted(lambda x: x), 0.3, 0, 1, tol=0.01), "about 0.3")
    assert abs(got - 0.3) < 0.01, f"expected a value within tol = 0.01 of 0.3, got {got!r}"


def test_quantile_stops_after_200_halvings(integrate):
    got = _result(lambda: integrate.quantile(_counted(lambda x: x), 0.3, 0, 1, tol=0), "about 0.3 (no endless loop)")
    assert got == pytest.approx(0.3, abs=1e-12), f"expected about 0.3 with tol = 0 (stop after 200 halvings), got {got}"


def test_quantile_returns_a_float(integrate):
    got = _result(lambda: integrate.quantile(lambda x: x, 0.5, 0, 1), "0.5 (a float)")
    assert isinstance(got, float), f"expected a float (as the docstring says), got {type(got).__name__} {got!r}"


@pytest.mark.parametrize("p", [0, 1, -0.2, 1.5], ids=["0", "1", "-0.2", "1.5"])
def test_quantile_refuses_p_outside_0_1(integrate, p):
    _expect_value_error(lambda: integrate.quantile(lambda x: x, p, 0, 1), f"quantile(cdf, {p}, 0, 1)",
                        "the order p must be strictly between 0 and 1")


@pytest.mark.parametrize("low, high", [(1, 1), (2, 0)], ids=["equal", "reversed"])
def test_quantile_refuses_an_empty_interval(integrate, low, high):
    _expect_value_error(lambda: integrate.quantile(lambda x: min(1, max(0, x / 2)), 0.5, low, high),
                        f"quantile(cdf, 0.5, {low}, {high})", "low must be smaller than high")


@pytest.mark.parametrize("low, high", [(0.6, 1), (0, 0.4)], ids=["cdf(low)>p", "cdf(high)<p"])
def test_quantile_refuses_an_interval_without_the_quantile(integrate, low, high):
    _expect_value_error(lambda: integrate.quantile(lambda x: x, 0.5, low, high), f"quantile(cdf, 0.5, {low}, {high})",
                        "the quantile is not in [low, high]: check cdf(low) <= p <= cdf(high) first")
