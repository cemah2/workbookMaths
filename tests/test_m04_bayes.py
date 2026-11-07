"""Tests of mymath.bayes (chapter M04): Beta density and moments, conjugate update, predictive law, MAP.

Oracles: ``scipy.stats.beta`` and ``scipy.stats.betabinom`` for the densities, moments and the predictive law,
``fractions.Fraction`` for exact small cases, and a fine grid of ``scipy.stats.beta.pdf`` for the mode. They describe
the expected behaviour without showing the solution.

    pytest tests/test_m04_bayes.py              # your code
    pytest tests/test_m04_bayes.py --impl=ref   # the reference
"""

import ast
import inspect
import math
from fractions import Fraction

import numpy as np
import pytest
from scipy import stats

PARAMETERS = [(2, 2), (3, 7), (0.5, 0.5), (2.5, 1.3), (1, 4), (12, 30)]
PARAMETER_IDS = ["2-2", "3-7", "0.5-0.5", "2.5-1.3", "1-4", "12-30"]


@pytest.fixture
def bayes(mymath_module):
    return mymath_module("bayes")


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


def _python_float(got, what):
    assert type(got) is float, (f"expected {what} to be a Python float (float(...)), got "
                                f"{type(got).__module__}.{type(got).__name__}")


# ---------------------------------------------------------------- no ready-made tool
def test_bayes_uses_no_scipy_stats_nor_special(bayes):
    """bayes.py computes its results itself: neither scipy.stats nor scipy.special (the tests compare with them)."""
    try:
        tree = ast.parse(inspect.getsource(bayes))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    used = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            used.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            used.add(node.module)
            used.update(f"{node.module}.{alias.name}" for alias in node.names)
        elif isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id == "scipy":
            used.add(f"scipy.{node.attr}")
    forbidden = sorted(name for name in used if name.startswith(("scipy.stats", "scipy.special")))
    assert not forbidden, (
        f"expected bayes.py to use neither scipy.stats nor scipy.special (the tests compare your results with them), "
        f"found {forbidden}: use math.lgamma for log B(a, b) and math.comb for C(n, k)")


# ---------------------------------------------------------------- beta_pdf
def test_beta_pdf_docstring_example(bayes):
    got = _result(lambda: bayes.beta_pdf(0.5, 2, 2), "1.5")
    assert got == pytest.approx(1.5, rel=1e-12), f"expected 1.5 (6 x 0.5 x 0.5), got {got!r}"


@pytest.mark.parametrize("a, b", PARAMETERS, ids=PARAMETER_IDS)
def test_beta_pdf_matches_scipy_inside(bayes, a, b):
    for x in (0.03, 0.2, 0.5, 0.71, 0.96):
        expected = float(stats.beta(a, b).pdf(x))
        got = _result(lambda: bayes.beta_pdf(x, a, b), f"{expected:.10g} at x = {x}")
        assert got == pytest.approx(expected, rel=1e-9), (
            f"expected {expected:.10g} for beta_pdf({x}, {a}, {b}), got {got!r}: x**(a - 1) (1 - x)**(b - 1) "
            "divided by B(a, b) = exp(lgamma(a) + lgamma(b) - lgamma(a + b))")


def test_beta_pdf_is_zero_outside_the_interval(bayes):
    for x in (-0.5, -1e-9, 1 + 1e-9, 2.0):
        got = _result(lambda: bayes.beta_pdf(x, 2, 3), "0.0")
        assert got == 0.0, f"expected 0.0 for beta_pdf({x}, 2, 3) (outside [0, 1]), got {got!r}"


@pytest.mark.parametrize("x, a, b, expected", [
    (0.0, 3, 2, 0.0), (0.0, 1, 4, 4.0), (0.0, 0.5, 2, math.inf),
    (1.0, 2, 3, 0.0), (1.0, 5, 1, 5.0), (1.0, 2, 0.3, math.inf),
], ids=["x0 a>1", "x0 a=1", "x0 a<1", "x1 b>1", "x1 b=1", "x1 b<1"])
def test_beta_pdf_at_the_ends(bayes, x, a, b, expected):
    got = _result(lambda: bayes.beta_pdf(x, a, b), f"{expected}")
    if math.isinf(expected):
        assert got == math.inf, f"expected math.inf for beta_pdf({x}, {a}, {b}) (exponent below 0 at {x}), got {got!r}"
    else:
        assert got == pytest.approx(expected, rel=1e-12, abs=1e-12), (
            f"expected {expected} for beta_pdf({x}, {a}, {b}) (see the docstring for the ends 0 and 1), got {got!r}")


def test_beta_pdf_with_large_parameters_does_not_overflow(bayes):
    expected = float(stats.beta(500, 700).pdf(0.42))
    got = _result(lambda: bayes.beta_pdf(0.42, 500, 700), f"{expected:.10g}", "beta_pdf(0.42, 500, 700)",
                  "Γ(1200) overflows: compute log B(a, b) with math.lgamma and take the exponential at the end")
    assert got == pytest.approx(expected, rel=1e-7), (
        f"expected {expected:.10g} for beta_pdf(0.42, 500, 700), got {got!r}: Γ(1200) overflows, compute log B(a, b) "
        "with math.lgamma and take the exponential at the end")


def test_beta_pdf_returns_a_python_float(bayes):
    for x, a, b in ((0.3, 2, 5), (1.5, 2, 5), (0.0, 3, 2), (1.0, 5, 1)):   # inside, outside, at the ends
        _python_float(_result(lambda: bayes.beta_pdf(x, a, b), "a float"), f"beta_pdf({x}, {a}, {b})")


@pytest.mark.parametrize("a, b", [(0, 2), (2, 0), (-1, 3), (2, -0.5)], ids=["a=0", "b=0", "a<0", "b<0"])
def test_beta_pdf_refuses_bad_parameters(bayes, a, b):
    _expect_value_error(lambda: bayes.beta_pdf(0.5, a, b), f"beta_pdf(0.5, {a}, {b})", "a and b must be positive")


# ---------------------------------------------------------------- beta_moments
def test_beta_moments_docstring_example(bayes):
    got = _result(lambda: bayes.beta_moments(2, 3), "(0.4, 0.04)")
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (mean, variance), got {got!r}"
    assert got[0] == pytest.approx(0.4, rel=1e-12) and got[1] == pytest.approx(0.04, rel=1e-12), (
        f"expected (0.4, 0.04), got {got!r}")


@pytest.mark.parametrize("a, b", PARAMETERS, ids=PARAMETER_IDS)
def test_beta_moments_match_scipy(bayes, a, b):
    mean, var = (float(v) for v in stats.beta(a, b).stats(moments="mv"))
    got = _result(lambda: bayes.beta_moments(a, b), f"({mean:.10g}, {var:.10g})")
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (mean, variance), got {got!r}"
    assert got[0] == pytest.approx(mean, rel=1e-12), f"expected the mean {mean:.10g} for Beta({a}, {b}), got {got[0]!r}"
    assert got[1] == pytest.approx(var, rel=1e-12), (
        f"expected the variance {var:.10g} for Beta({a}, {b}), got {got[1]!r} (the variance, not the standard "
        "deviation)")


def test_beta_moments_returns_python_floats(bayes):
    got = _result(lambda: bayes.beta_moments(3, 4), "two floats")
    for value, what in zip(got, ("the mean", "the variance")):
        _python_float(value, f"{what} of beta_moments(3, 4)")


@pytest.mark.parametrize("a, b", [(0, 1), (1, -2)], ids=["a=0", "b<0"])
def test_beta_moments_refuses_bad_parameters(bayes, a, b):
    _expect_value_error(lambda: bayes.beta_moments(a, b), f"beta_moments({a}, {b})", "a and b must be positive")


# ---------------------------------------------------------------- conjugate_beta_update
def test_conjugate_beta_update_docstring_example(bayes):
    got = _result(lambda: bayes.conjugate_beta_update(1, 1, 3, 7), "(4, 8)")
    assert got == (4, 8), f"expected (4, 8) (successes added to a, failures to b), got {got!r}"


def test_conjugate_beta_update_keeps_ints_and_accepts_floats(bayes):
    got = _result(lambda: bayes.conjugate_beta_update(2, 5, 0, 4), "(2, 9)")
    assert got == (2, 9) and all(type(v) is int for v in got), (
        f"expected the tuple of ints (2, 9), got {got!r} of types {[type(v).__name__ for v in got]}")
    got = _result(lambda: bayes.conjugate_beta_update(0.5, 0.5, 6, 1), "(6.5, 1.5)")
    assert got == pytest.approx((6.5, 1.5)), f"expected (6.5, 1.5), got {got!r}"


def test_conjugate_beta_update_twice_equals_once(bayes):
    once = _result(lambda: bayes.conjugate_beta_update(3, 4, 7, 9), "(10, 13)")
    first = _result(lambda: bayes.conjugate_beta_update(3, 4, 2, 5), "(5, 9)")
    twice = _result(lambda: bayes.conjugate_beta_update(*first, 5, 4), "(10, 13)")
    assert once == twice == (10, 13), f"expected (10, 13) for both, got {once!r} at once and {twice!r} in two steps"


@pytest.mark.parametrize("args, why", [
    ((0, 1, 2, 3), "a must be positive"), ((1, -1, 2, 3), "b must be positive"),
    ((1, 1, -1, 3), "a count cannot be negative"), ((1, 1, 2, -3), "a count cannot be negative"),
], ids=["a=0", "b<0", "successes<0", "failures<0"])
def test_conjugate_beta_update_refuses_bad_input(bayes, args, why):
    _expect_value_error(lambda: bayes.conjugate_beta_update(*args), f"conjugate_beta_update{args}", why)


# ---------------------------------------------------------------- posterior_predictive
def test_posterior_predictive_docstring_examples(bayes):
    got = _result(lambda: bayes.posterior_predictive(4, 8), "1/3")
    assert got == pytest.approx(1 / 3, rel=1e-12), f"expected 1/3 (a / (a + b) for the next trial), got {got!r}"
    got = _result(lambda: bayes.posterior_predictive(1, 1, 2, 4), "0.2")
    assert got == pytest.approx(0.2, rel=1e-12), (
        f"expected 0.2 (with Beta(1, 1), every k of 0..4 has probability 1/5), got {got!r}")


@pytest.mark.parametrize("a, b, n", [(2, 3, 4), (5, 1, 6), (3, 9, 10)], ids=["2-3 n4", "5-1 n6", "3-9 n10"])
def test_posterior_predictive_exact_small_cases(bayes, a, b, n):
    def exact(k):   # C(n, k) B(a + k, b + n - k) / B(a, b) with factorials, for integer a and b
        fact = math.factorial
        beta = lambda p, q: Fraction(fact(p - 1) * fact(q - 1), fact(p + q - 1))
        return math.comb(n, k) * beta(a + k, b + n - k) / beta(a, b)
    for k in range(n + 1):
        expected = exact(k)
        got = _result(lambda: bayes.posterior_predictive(a, b, k, n), f"{expected} = {float(expected):.10g}")
        assert got == pytest.approx(float(expected), rel=1e-9), (
            f"expected {expected} = {float(expected):.10g} for posterior_predictive({a}, {b}, {k}, {n}), got {got!r}: "
            "C(n, k) B(a + k, b + n - k) / B(a, b)")


@pytest.mark.parametrize("a, b, n", [(0.5, 2.5, 7), (40, 60, 25)], ids=["0.5-2.5 n7", "40-60 n25"])
def test_posterior_predictive_matches_scipy_betabinom(bayes, a, b, n):
    total = 0.0
    for k in range(n + 1):
        expected = float(stats.betabinom(n, a, b).pmf(k))
        got = _result(lambda: bayes.posterior_predictive(a, b, k, n), f"{expected:.10g}")
        assert got == pytest.approx(expected, rel=1e-8), (
            f"expected {expected:.10g} for posterior_predictive({a}, {b}, {k}, {n}), got {got!r}")
        total += got
    assert total == pytest.approx(1.0, abs=1e-9), f"expected the probabilities of k = 0..{n} to sum to 1, got {total!r}"


def test_posterior_predictive_impossible_counts(bayes):
    for k, n in ((-1, 3), (4, 3), (2, 0)):
        got = _result(lambda: bayes.posterior_predictive(2, 2, k, n), "0.0")
        assert got == 0.0, f"expected 0.0 for posterior_predictive(2, 2, {k}, {n}) (k outside 0..n), got {got!r}"
    got = _result(lambda: bayes.posterior_predictive(2, 2, 0, 0), "1.0")
    assert got == pytest.approx(1.0, rel=1e-12), f"expected 1.0 for 0 successes in 0 trials, got {got!r}"


def test_posterior_predictive_with_many_trials_does_not_overflow(bayes):
    expected = float(stats.betabinom(2000, 30, 70).pmf(600))
    got = _result(lambda: bayes.posterior_predictive(30, 70, 600, 2000), f"{expected:.10g}",
                  "posterior_predictive(30, 70, 600, 2000)",
                  "Γ(2100) overflows: add the logarithms of C(n, k) and of the B values, then take the exponential")
    assert got == pytest.approx(expected, rel=1e-6), (
        f"expected {expected:.10g} for posterior_predictive(30, 70, 600, 2000), got {got!r}: compute the logarithms "
        "of C(n, k) and of the B values, add them, and take the exponential at the end")


def test_posterior_predictive_returns_a_python_float(bayes):
    _python_float(_result(lambda: bayes.posterior_predictive(3, 5, 1, 2), "a float"), "posterior_predictive(3, 5, 1, 2)")


@pytest.mark.parametrize("args, why", [
    ((0, 2, 1, 1), "a must be positive"), ((2, -1, 1, 1), "b must be positive"), ((2, 2, 0, -1), "n cannot be negative"),
], ids=["a=0", "b<0", "n<0"])
def test_posterior_predictive_refuses_bad_input(bayes, args, why):
    _expect_value_error(lambda: bayes.posterior_predictive(*args), f"posterior_predictive{args}", why)


# ---------------------------------------------------------------- map_estimate_beta
def test_map_estimate_beta_docstring_example(bayes):
    got = _result(lambda: bayes.map_estimate_beta(4, 8), "0.3")
    assert got == pytest.approx(0.3, rel=1e-12), f"expected 0.3 ((a - 1) / (a + b - 2)), got {got!r}"


@pytest.mark.parametrize("a, b", [(2, 2), (3, 7), (2.5, 1.3), (12, 30), (1.5, 9)], ids=["2-2", "3-7", "2.5-1.3",
                                                                                      "12-30", "1.5-9"])
def test_map_estimate_beta_is_the_maximum_of_the_density(bayes, a, b):
    grid = np.linspace(0, 1, 200_001)
    expected = float(grid[np.argmax(stats.beta(a, b).pdf(grid))])
    got = _result(lambda: bayes.map_estimate_beta(a, b), f"about {expected:.5f}")
    assert got == pytest.approx(expected, abs=1e-5), (
        f"expected about {expected:.5f} for map_estimate_beta({a}, {b}) (the maximum of the density), got {got!r}: "
        "the mode (a - 1) / (a + b - 2), not the mean a / (a + b)")


@pytest.mark.parametrize("a, b, expected", [
    (1, 3, 0.0), (0.5, 4, 0.0), (0.5, 1, 0.0), (3, 1, 1.0), (4, 0.5, 1.0), (1, 0.7, 1.0),
], ids=["a=1<b", "a<1<b", "a<1=b", "b=1<a", "b<1<a", "b<1=a"])
def test_map_estimate_beta_at_the_ends(bayes, a, b, expected):
    got = _result(lambda: bayes.map_estimate_beta(a, b), f"{expected}")
    assert got == expected, (
        f"expected {expected} for map_estimate_beta({a}, {b}): the density "
        f"{'decreases' if expected == 0 else 'increases'} on (0, 1), so its maximum is at {expected:g}; got {got!r}")


def test_map_estimate_beta_returns_a_python_float(bayes):
    _python_float(_result(lambda: bayes.map_estimate_beta(3, 5), "a float"), "map_estimate_beta(3, 5)")
    _python_float(_result(lambda: bayes.map_estimate_beta(1, 5), "a float"), "map_estimate_beta(1, 5)")


@pytest.mark.parametrize("a, b, why", [
    (1, 1, "Beta(1, 1) is uniform: no single mode"), (0.5, 0.5, "two modes, at 0 and at 1"),
    (0.3, 0.9, "two modes, at 0 and at 1"), (0, 2, "a must be positive"), (2, -1, "b must be positive"),
], ids=["uniform", "U 0.5-0.5", "U 0.3-0.9", "a=0", "b<0"])
def test_map_estimate_beta_refuses_no_single_mode(bayes, a, b, why):
    _expect_value_error(lambda: bayes.map_estimate_beta(a, b), f"map_estimate_beta({a}, {b})", why)
