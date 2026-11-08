"""Tests of mymath.concentration (chapter M11): the bounds of Markov, Chebyshev and Hoeffding, the confidence radius
of Hoeffding, the empirical tail of a sample.

Oracles: exact fractions (``fractions.Fraction``) for the values of the bounds, ``scipy.stats`` for the true tails of
usual laws (each bound must stay above them), distributions built so that a bound is reached exactly, and ``math`` for
the equation that defines the radius. They describe the expected behaviour without showing the solution.

    pytest tests/test_m11_concentration.py              # your code
    pytest tests/test_m11_concentration.py --impl=ref   # the reference
"""

import math
from fractions import Fraction

import numpy as np
import pytest
from scipy import stats


@pytest.fixture
def conc(mymath_module):
    return mymath_module("concentration")


def _result(call, expected, what=""):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    try:
        return call()
    except NotImplementedError:
        raise                 # a function not written yet: ⏳
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        error = exc           # reported below, outside the except block, so that pytest shows no chained traceback
    pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised {type(error).__name__}: {error}")


def _expect_value_error(call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ValueError."""
    try:
        result = call()
    except NotImplementedError:
        raise                 # a function not written yet stays ⏳
    except ValueError:
        return
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        error = exc           # reported below, outside the except block (no chained traceback)
    else:
        pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned {result!r}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(error).__name__}: {error}")


def _is_float(value, what):
    assert type(value) is float, (
        f"expected a Python float for {what}, got {type(value).__name__} {value!r} (convert with float(...))")


# ---------------------------------------------------------------- markov_bound
def test_markov_bound_docstring_examples(conc):
    got = _result(lambda: conc.markov_bound(2.0, 8.0), "0.25", "markov_bound(2.0, 8.0)")
    assert got == pytest.approx(0.25), f"expected 0.25 (E[X] / a = 2 / 8), got {got!r}"
    got = _result(lambda: conc.markov_bound(3.0, 2.0), "1.0", "markov_bound(3.0, 2.0)")
    assert got == 1.0, f"expected 1.0 (3 / 2 is more than 1, and a probability is at most 1), got {got!r}"


@pytest.mark.parametrize("mean, a", [(Fraction(1), Fraction(4)), (Fraction(7, 2), Fraction(10)),
                                     (Fraction(0), Fraction(3)), (Fraction(5), Fraction(5)),
                                     (Fraction(12), Fraction(1, 2)), (Fraction(3, 10), Fraction(9, 10))])
def test_markov_bound_values(conc, mean, a):
    expected = float(min(Fraction(1), mean / a))
    got = _result(lambda: conc.markov_bound(float(mean), float(a)), expected, f"mean = {mean}, a = {a}")
    _is_float(got, f"markov_bound({float(mean)}, {float(a)})")
    assert got == pytest.approx(expected, rel=1e-12, abs=1e-15), (
        f"expected {expected} for E[X] = {mean} and a = {a}, got {got!r}")


def test_markov_bound_accepts_integers(conc):
    got = _result(lambda: conc.markov_bound(3, 12), "0.25", "markov_bound(3, 12)")
    _is_float(got, "markov_bound(3, 12)")
    assert got == pytest.approx(0.25), f"expected 0.25 for integer arguments 3 and 12, got {got!r}"


LAWS_POSITIVE = {
    "exponential, mean 2": (stats.expon(scale=2.0), 2.0),
    "uniform on [0, 10]": (stats.uniform(0, 10), 5.0),
    "Poisson 3": (stats.poisson(3), 3.0),
    "binomial (20, 0.3)": (stats.binom(20, 0.3), 6.0),
    "gamma (shape 0.5, scale 4)": (stats.gamma(0.5, scale=4.0), 2.0),
}


@pytest.mark.parametrize("name", list(LAWS_POSITIVE))
def test_markov_bound_stays_above_the_true_tail(conc, name):
    law, mean = LAWS_POSITIVE[name]
    for a in [0.5, 1.0, 2.5, 4.0, 7.0, 12.0, 30.0]:
        tail = float(law.sf(a - 1e-9)) if hasattr(law, "pmf") else float(law.sf(a))   # P(X >= a)
        got = _result(lambda: conc.markov_bound(mean, a), f"a bound at least P(X >= {a}) = {tail:.6f}", name)
        assert got >= tail - 1e-12, (
            f"expected a bound at least the true tail P(X >= {a}) = {tail:.6f} for the {name} law (mean {mean}), "
            f"got {got!r}")


@pytest.mark.parametrize("a, p", [(4.0, 0.25), (10.0, 0.1), (0.5, 0.8)])
def test_markov_bound_is_reached_by_a_two_point_law(conc, a, p):
    """X = a with probability p, 0 otherwise: E[X] = p a and P(X >= a) = p, so the bound is exact."""
    got = _result(lambda: conc.markov_bound(p * a, a), str(p), f"X in {{0, {a}}} with P(X = {a}) = {p}")
    assert got == pytest.approx(p, rel=1e-12), (
        f"expected {p}: for X = {a} with probability {p} and 0 otherwise, E[X] / a = {p} = P(X >= {a}), got {got!r}")


@pytest.mark.parametrize("args, why", [((-1.0, 2.0), "a negative expectation"), ((2.0, 0.0), "a = 0"),
                                       ((2.0, -3.0), "a negative threshold")])
def test_markov_bound_rejects_bad_input(conc, args, why):
    _expect_value_error(lambda: conc.markov_bound(*args), f"markov_bound{args}", why)


# ---------------------------------------------------------------- chebyshev_bound
def test_chebyshev_bound_docstring_example(conc):
    got = _result(lambda: conc.chebyshev_bound(4.0, 5.0), "0.16", "chebyshev_bound(4.0, 5.0)")
    assert got == pytest.approx(0.16), f"expected 0.16 (V(X) / t² = 4 / 25), got {got!r}"


@pytest.mark.parametrize("variance, t", [(Fraction(1), Fraction(2)), (Fraction(9), Fraction(6)),
                                         (Fraction(0), Fraction(1)), (Fraction(5), Fraction(1)),
                                         (Fraction(1, 4), Fraction(1, 10)), (Fraction(2), Fraction(3, 2))])
def test_chebyshev_bound_values(conc, variance, t):
    expected = float(min(Fraction(1), variance / t ** 2))
    got = _result(lambda: conc.chebyshev_bound(float(variance), float(t)), expected, f"V = {variance}, t = {t}")
    _is_float(got, f"chebyshev_bound({float(variance)}, {float(t)})")
    assert got == pytest.approx(expected, rel=1e-12, abs=1e-15), (
        f"expected {expected} for V(X) = {variance} and t = {t} (divide by t², not by t), got {got!r}")


LAWS_ANY = {
    "normal (1, 3²)": (stats.norm(1.0, 3.0), 1.0, 9.0),
    "uniform on [-2, 4]": (stats.uniform(-2, 6), 1.0, 3.0),
    "binomial (30, 0.4)": (stats.binom(30, 0.4), 12.0, 7.2),
    "exponential, mean 1": (stats.expon(), 1.0, 1.0),
}


@pytest.mark.parametrize("name", list(LAWS_ANY))
def test_chebyshev_bound_stays_above_the_true_tail(conc, name):
    law, mu, var = LAWS_ANY[name]
    for t in [0.5, 1.0, 2.0, 3.5, 6.0, 9.0]:
        if hasattr(law, "pmf"):    # P(|X - mu| >= t) for an integer law: the values outside ]mu - t, mu + t[
            tail = float(law.cdf(math.floor(mu - t + 1e-9)) + law.sf(math.ceil(mu + t - 1e-9) - 1))
        else:
            tail = float(law.cdf(mu - t) + law.sf(mu + t))
        got = _result(lambda: conc.chebyshev_bound(var, t), f"a bound at least {tail:.6f}", name)
        assert got >= tail - 1e-12, (
            f"expected a bound at least the true tail P(|X - {mu}| >= {t}) = {tail:.6f} for the {name} law "
            f"(variance {var}), got {got!r}")


@pytest.mark.parametrize("t, p", [(2.0, 0.5), (3.0, 0.2), (1.5, 0.08)])
def test_chebyshev_bound_is_reached_by_a_three_point_law(conc, t, p):
    """X = mu ± t with probability p/2 each, mu otherwise: V(X) = p t² and P(|X - mu| >= t) = p."""
    got = _result(lambda: conc.chebyshev_bound(p * t ** 2, t), str(p), f"X in {{mu - {t}, mu, mu + {t}}}")
    assert got == pytest.approx(p, rel=1e-12), (
        f"expected {p}: for X = mu ± {t} with probability {p / 2} each, V(X) = {p * t ** 2} and the bound is exact, "
        f"got {got!r}")


@pytest.mark.parametrize("args, why", [((-0.5, 1.0), "a negative variance"), ((1.0, 0.0), "t = 0"),
                                       ((1.0, -2.0), "a negative distance")])
def test_chebyshev_bound_rejects_bad_input(conc, args, why):
    _expect_value_error(lambda: conc.chebyshev_bound(*args), f"chebyshev_bound{args}", why)


# ---------------------------------------------------------------- hoeffding_bound
def _hoeffding(n, t, a=0.0, b=1.0):
    return min(1.0, 2.0 * math.exp(-2.0 * n * t * t / (b - a) ** 2))


def test_hoeffding_bound_docstring_examples(conc):
    got = _result(lambda: conc.hoeffding_bound(100, 0.1), "≈ 0.2707", "hoeffding_bound(100, 0.1)")
    assert got == pytest.approx(0.2707, abs=5e-5), f"expected 2 e^(-2) ≈ 0.2707 for n = 100 and t = 0.1, got {got!r}"
    got = _result(lambda: conc.hoeffding_bound(10, 0.1), "1.0", "hoeffding_bound(10, 0.1)")
    assert got == 1.0, f"expected 1.0 (the formula gives 2 e^(-0.2) > 1, and a probability is at most 1), got {got!r}"
    _is_float(got, "hoeffding_bound(10, 0.1), capped at 1 (min(1.0, ...), not min(1, ...))")


@pytest.mark.parametrize("n, t, a, b", [(50, 0.2, 0.0, 1.0), (400, 0.05, 0.0, 1.0), (30, 1.0, -2.0, 2.0),
                                        (1000, 0.3, 0.0, 5.0), (8, 0.5, 0.0, 1.0), (2500, 0.02, 0.0, 1.0)])
def test_hoeffding_bound_values(conc, n, t, a, b):
    expected = _hoeffding(n, t, a, b)
    got = _result(lambda: conc.hoeffding_bound(n, t, a=a, b=b), f"≈ {expected:.6g}", f"n = {n}, t = {t}, [{a}, {b}]")
    _is_float(got, f"hoeffding_bound({n}, {t}, a={a}, b={b})")
    assert got == pytest.approx(expected, rel=1e-9), (
        f"expected {expected:.10g} for n = {n}, t = {t} and variables in [{a}, {b}] (2 exp(-2 n t² / (b - a)²): the factor 2, and the width squared), "
        f"got {got!r}")


@pytest.mark.parametrize("n, p, t", [(20, 0.5, 0.2), (50, 0.3, 0.15), (100, 0.1, 0.1), (200, 0.5, 0.08),
                                     (500, 0.7, 0.05)])
def test_hoeffding_bound_stays_above_the_exact_binomial_tail(conc, n, p, t):
    """For Bernoulli(p) variables, P(|K/n - p| >= t) is an exact binomial computation."""
    k = np.arange(n + 1)
    far = np.abs(k / n - p) >= t - 1e-12
    tail = float(stats.binom(n, p).pmf(k)[far].sum())
    got = _result(lambda: conc.hoeffding_bound(n, t), f"a bound at least {tail:.6f}", f"Bernoulli({p}), n = {n}")
    assert got >= tail - 1e-12, (
        f"expected a bound at least the exact tail P(|K/{n} - {p}| >= {t}) = {tail:.6f}, got {got!r}")


def test_hoeffding_bound_decreases_with_n(conc):
    values = [_result(lambda n=n: conc.hoeffding_bound(n, 0.1), "a probability", f"n = {n}")
              for n in (100, 200, 400, 800)]
    assert all(x > y for x, y in zip(values, values[1:])), (
        f"expected a bound that decreases strictly when n doubles from 100 to 800 (t = 0.1), got {values}")


def test_hoeffding_bound_only_depends_on_t_over_the_width(conc):
    got = _result(lambda: conc.hoeffding_bound(60, 1.5, a=-3.0, b=3.0), "the same bound as for t = 0.25 on [0, 1]")
    ref = _hoeffding(60, 0.25)
    assert got == pytest.approx(ref, rel=1e-9), (
        f"expected {ref:.10g}: a deviation 1.5 for variables in [-3, 3] is a deviation 0.25 for variables in [0, 1], "
        f"got {got!r}")


@pytest.mark.parametrize("args, kwargs, why", [((0, 0.1), {}, "n = 0"), ((10, 0.0), {}, "t = 0"),
                                               ((10, -0.1), {}, "a negative deviation"),
                                               ((10, 0.1), {"a": 1.0, "b": 1.0}, "a = b"),
                                               ((10, 0.1), {"a": 2.0, "b": 0.0}, "a > b")])
def test_hoeffding_bound_rejects_bad_input(conc, args, kwargs, why):
    _expect_value_error(lambda: conc.hoeffding_bound(*args, **kwargs), f"hoeffding_bound{args} {kwargs}", why)


# ---------------------------------------------------------------- hoeffding_radius
def test_hoeffding_radius_docstring_examples(conc):
    got = _result(lambda: conc.hoeffding_radius(200, 0.05), "≈ 0.096", "hoeffding_radius(200, 0.05)")
    assert got == pytest.approx(0.0960, abs=5e-5), f"expected ≈ 0.0960 for n = 200 and δ = 0.05, got {got!r}"
    got = _result(lambda: conc.hoeffding_radius(200, 0.05, a=-1.0, b=1.0), "≈ 0.1921", "variables in [-1, 1]")
    assert got == pytest.approx(0.1921, abs=5e-5), (
        f"expected ≈ 0.1921 for variables in [-1, 1] (twice the radius on [0, 1]), got {got!r}")


@pytest.mark.parametrize("n, delta, a, b", [(100, 0.05, 0.0, 1.0), (1000, 0.01, 0.0, 1.0), (25, 0.2, -1.0, 3.0),
                                            (1, 0.5, 0.0, 1.0), (5000, 0.001, 0.0, 10.0)])
def test_hoeffding_radius_solves_the_equation(conc, n, delta, a, b):
    """The radius r is the deviation for which 2 exp(-2 n r² / (b - a)²) equals δ."""
    r = _result(lambda: conc.hoeffding_radius(n, delta, a=a, b=b), "a positive radius", f"n = {n}, δ = {delta}")
    _is_float(r, f"hoeffding_radius({n}, {delta}, a={a}, b={b})")
    assert r > 0, f"expected a positive radius for n = {n} and δ = {delta}, got {r!r}"
    level = 2.0 * math.exp(-2.0 * n * r * r / (b - a) ** 2)
    assert level == pytest.approx(delta, rel=1e-9), (
        f"expected a radius r with 2 exp(-2 n r² / (b - a)²) = δ = {delta} (n = {n}, [{a}, {b}]), but this r = {r!r} "
        f"gives {level:.10g} (ln(2/δ), then divide by 2n, then the square root)")


def test_hoeffding_radius_shrinks_like_one_over_root_n(conc):
    r1 = _result(lambda: conc.hoeffding_radius(100, 0.05), "a radius", "n = 100")
    r4 = _result(lambda: conc.hoeffding_radius(400, 0.05), "a radius", "n = 400")
    assert r4 == pytest.approx(r1 / 2, rel=1e-9), (
        f"expected the radius to be halved when n is multiplied by 4 (a radius in 1/√n), got {r1!r} then {r4!r}")


@pytest.mark.parametrize("args, kwargs, why", [((0, 0.05), {}, "n = 0"), ((10, 0.0), {}, "δ = 0"),
                                               ((10, 1.0), {}, "δ = 1"), ((10, 1.5), {}, "δ > 1"),
                                               ((10, -0.1), {}, "a negative risk"),
                                               ((10, 0.05), {"a": 3.0, "b": 3.0}, "a = b")])
def test_hoeffding_radius_rejects_bad_input(conc, args, kwargs, why):
    _expect_value_error(lambda: conc.hoeffding_radius(*args, **kwargs), f"hoeffding_radius{args} {kwargs}", why)


# ---------------------------------------------------------------- empirical_tail
def test_empirical_tail_docstring_examples(conc):
    got = _result(lambda: conc.empirical_tail([1, 3, 5, 7], 5), "0.5", "empirical_tail([1, 3, 5, 7], 5)")
    assert got == pytest.approx(0.5), f"expected 0.5 (5 and 7 are at least 5: the threshold itself counts), got {got!r}"
    got = _result(lambda: conc.empirical_tail([1, 3, 5, 7], 8), "0.0", "empirical_tail([1, 3, 5, 7], 8)")
    assert got == 0.0, f"expected 0.0 (no value is at least 8), got {got!r}"


@pytest.mark.parametrize("seed, n, threshold", [(1101, 10, 0.3), (1102, 1000, 1.5), (1103, 37, -0.2),
                                                (1104, 5000, 2.0)])
def test_empirical_tail_counts_the_values_at_least_the_threshold(conc, seed, n, threshold):
    sample = np.round(np.random.default_rng(seed).normal(size=n), 1)       # rounded: some values equal the threshold
    expected = sum(1 for v in sample.tolist() if v >= threshold) / n
    got = _result(lambda: conc.empirical_tail(sample, threshold), f"{expected}", f"{n} values, threshold {threshold}")
    _is_float(got, "empirical_tail")
    assert got == pytest.approx(expected, abs=1e-12), (
        f"expected {expected} (the share of the {n} values that are >= {threshold}, equal values included), got {got!r}")


def test_empirical_tail_accepts_lists_tuples_and_keeps_its_input(conc):
    values = np.array([2.0, 2.0, 8.0, -1.0, 2.5])
    before = values.copy()
    got = _result(lambda: conc.empirical_tail(values, 2.0), "0.8", "an array")
    assert got == pytest.approx(0.8), f"expected 0.8 (four values out of five are >= 2.0), got {got!r}"
    assert np.array_equal(values, before), "expected empirical_tail not to modify the array it receives"
    got = _result(lambda: conc.empirical_tail((4, 1, 9), 4), "2/3", "a tuple")
    assert got == pytest.approx(2 / 3), f"expected 2/3 for the tuple (4, 1, 9) and the threshold 4, got {got!r}"
    got = _result(lambda: conc.empirical_tail([0.5], -math.inf), "1.0", "a threshold -inf")
    assert got == 1.0, f"expected 1.0: every value is >= -inf, got {got!r}"


def test_empirical_tail_rejects_an_empty_sample(conc):
    _expect_value_error(lambda: conc.empirical_tail([], 1.0), "empirical_tail([], 1.0)", "an empty sample")
