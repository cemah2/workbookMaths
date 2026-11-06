"""Tests of mymath.distributions (chapter M02b): binomial, Poisson and normal laws, sampling by inversion.

Oracles: ``scipy.stats`` (binom, poisson, norm), exact sums with ``fractions.Fraction`` and the uniforms of
``numpy.random.default_rng``. They describe the expected behaviour without showing the solution.

    pytest tests/test_m02b_distributions.py              # your code
    pytest tests/test_m02b_distributions.py --impl=ref   # the reference
"""

import ast
import inspect
import math
from fractions import Fraction

import numpy as np
import pytest
from scipy import stats


@pytest.fixture
def distributions(mymath_module):
    return mymath_module("distributions")


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


def _python_float(got, what="the result"):
    """Fail unless got is a Python float (numpy.float64 passes isinstance(..., float), but prints np.float64(...))."""
    assert type(got) is float, (
        f"expected {what} to be a Python float (as the docstring says), got {type(got).__module__}."
        f"{type(got).__name__} {got!r}: convert with float(...)")


# ---------------------------------------------------------------- no ready-made law
def test_distributions_uses_no_ready_made_law(distributions):
    """distributions.py writes the formulas itself: no SciPy, no statistics.NormalDist, no NumPy sampler."""
    try:
        tree = ast.parse(inspect.getsource(distributions))
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
        "expected distributions.py not to import SciPy (the tests compare your results with scipy.stats): write "
        "the formulas yourself")
    used = sorted(attributes & {"NormalDist", "binomial", "poisson", "normal", "standard_normal", "exponential"})
    assert not used, (f"expected distributions.py to write the laws itself, not to call {', '.join(used)}: the "
                      "formulas of the chapter, with math.comb, math.factorial, math.exp and math.erf, are the "
                      "exercise")


# ---------------------------------------------------------------- binomial_pmf
def test_binomial_pmf_docstring_example(distributions):
    got = _result(lambda: distributions.binomial_pmf(2, 4, 0.5), "0.375 (the docstring example)")
    assert got == pytest.approx(0.375, abs=1e-12), f"expected 0.375 (the docstring example), got {got!r}"


@pytest.mark.parametrize("k, n, p", [(0, 1, 0.3), (1, 1, 0.3), (3, 10, 0.25), (7, 10, 0.25), (0, 20, 0.9),
                                     (20, 20, 0.9), (50, 100, 0.5), (13, 40, 0.07)],
                         ids=["0-1", "1-1", "3-10", "7-10", "0-20", "20-20", "50-100", "13-40"])
def test_binomial_pmf_matches_scipy(distributions, k, n, p):
    expected = float(stats.binom(n, p).pmf(k))
    got = _result(lambda: distributions.binomial_pmf(k, n, p), f"{expected} (scipy.stats.binom({n}, {p}).pmf({k}))")
    assert got == pytest.approx(expected, rel=1e-9, abs=1e-300), (
        f"expected {expected} = C({n}, {k}) × {p}^{k} × (1 − {p})^{n - k}, got {got!r}")


def test_binomial_pmf_exact_with_fractions(distributions):
    expected = math.comb(6, 2) * Fraction(1, 3) ** 2 * Fraction(2, 3) ** 4      # 240/729
    got = _result(lambda: distributions.binomial_pmf(2, 6, 1 / 3), f"{float(expected)} (= 240/729)")
    assert got == pytest.approx(float(expected), rel=1e-12), (
        f"expected {float(expected)} (= 240/729: C(6, 2) = 15 paths, each of probability (1/3)² (2/3)⁴), "
        f"got {got!r}")


def test_binomial_pmf_returns_a_float(distributions):
    got = _result(lambda: distributions.binomial_pmf(1, 2, 0.5), "0.5 (a float)")
    _python_float(got)
    assert got == pytest.approx(0.5), f"expected 0.5 (C(2, 1) × 0.5 × 0.5), got {got!r}"


def test_binomial_pmf_probabilities_sum_to_1(distributions):
    total = sum(_result(lambda k=k: distributions.binomial_pmf(k, 15, 0.37), "a probability") for k in range(16))
    assert total == pytest.approx(1.0, abs=1e-12), (
        f"expected the 16 probabilities P(X = 0), …, P(X = 15) of B(15, 0.37) to sum to 1, got {total!r}")


def test_binomial_pmf_mean_is_n_p(distributions):
    mean = sum(k * _result(lambda k=k: distributions.binomial_pmf(k, 12, 0.4), "a probability") for k in range(13))
    assert mean == pytest.approx(12 * 0.4, abs=1e-12), (
        f"expected Σ k P(X = k) = n p = 4.8 for B(12, 0.4), got {mean!r}")


@pytest.mark.parametrize("k", [-1, 7, 12], ids=["k-1", "k=n+1", "k=n+6"])
def test_binomial_pmf_is_zero_outside_0_n(distributions, k):
    got = _result(lambda: distributions.binomial_pmf(k, 6, 0.3), "0.0")
    assert got == 0.0, f"expected 0.0 for k = {k} (X ~ B(6, 0.3) takes the values 0 to 6 only), got {got!r}"
    _python_float(got)


@pytest.mark.parametrize("k, n, p, expected", [(0, 5, 0.0, 1.0), (1, 5, 0.0, 0.0), (5, 5, 1.0, 1.0),
                                               (4, 5, 1.0, 0.0), (0, 0, 0.6, 1.0)],
                         ids=["p0-k0", "p0-k1", "p1-kn", "p1-k4", "n0"])
def test_binomial_pmf_extreme_cases(distributions, k, n, p, expected):
    got = _result(lambda: distributions.binomial_pmf(k, n, p), f"{expected}")
    assert got == pytest.approx(expected, abs=1e-15), (
        f"expected binomial_pmf({k}, {n}, {p}) = {expected} (with p = 0, no success is sure; with p = 1, n successes "
        f"are sure; in Python 0 ** 0 == 1), got {got!r}")


@pytest.mark.parametrize("k, n, p, why", [(1, -1, 0.5, "n is negative"), (1, 3, -0.1, "p < 0"),
                                          (1, 3, 1.2, "p > 1")], ids=["n-1", "p-0.1", "p1.2"])
def test_binomial_pmf_refuses_bad_parameters(distributions, k, n, p, why):
    _expect_value_error(lambda: distributions.binomial_pmf(k, n, p), f"binomial_pmf({k}, {n}, {p})", why)


# ---------------------------------------------------------------- poisson_pmf
def test_poisson_pmf_docstring_example(distributions):
    got = _result(lambda: distributions.poisson_pmf(0, 2), "0.135335… (the docstring example)")
    assert got == pytest.approx(math.exp(-2), rel=1e-12), f"expected e^(−2) ≈ 0.135335 (the docstring example), got {got!r}"


@pytest.mark.parametrize("k, lam", [(0, 0.5), (3, 2.5), (10, 4.0), (1, 0.001), (60, 50.0), (100, 50.0), (0, 50.0)],
                         ids=["0-0.5", "3-2.5", "10-4", "1-0.001", "60-50", "100-50", "0-50"])
def test_poisson_pmf_matches_scipy(distributions, k, lam):
    expected = float(stats.poisson(lam).pmf(k))
    got = _result(lambda: distributions.poisson_pmf(k, lam), f"{expected} (scipy.stats.poisson({lam}).pmf({k}))")
    assert got == pytest.approx(expected, rel=1e-9, abs=1e-300), (
        f"expected {expected} = e^(−{lam}) × {lam}^{k} / {k}!, got {got!r}")


def test_poisson_pmf_returns_a_float(distributions):
    got = _result(lambda: distributions.poisson_pmf(1, 1), "e^(−1) (a float)")
    _python_float(got)


def test_poisson_pmf_probabilities_sum_to_1(distributions):
    total = sum(_result(lambda k=k: distributions.poisson_pmf(k, 7.3), "a probability") for k in range(61))
    assert total == pytest.approx(1.0, abs=1e-10), (
        f"expected Σ P(X = k) for k = 0 to 60 to be 1 (up to 1e-10) for the Poisson law of parameter 7.3, "
        f"got {total!r}")


def test_poisson_pmf_mean_is_lambda(distributions):
    mean = sum(k * _result(lambda k=k: distributions.poisson_pmf(k, 3.5), "a probability") for k in range(80))
    assert mean == pytest.approx(3.5, abs=1e-10), f"expected Σ k P(X = k) = λ = 3.5, got {mean!r}"


@pytest.mark.parametrize("k, expected", [(0, 1.0), (1, 0.0), (4, 0.0)], ids=["k0", "k1", "k4"])
def test_poisson_pmf_with_lambda_0(distributions, k, expected):
    got = _result(lambda: distributions.poisson_pmf(k, 0), f"{expected}")
    assert got == expected, (
        f"expected poisson_pmf({k}, 0) = {expected} (λ = 0: no event, X = 0 is sure; in Python 0 ** 0 == 1), "
        f"got {got!r}")


@pytest.mark.parametrize("k", [-1, -5], ids=["k-1", "k-5"])
def test_poisson_pmf_is_zero_for_negative_k(distributions, k):
    got = _result(lambda: distributions.poisson_pmf(k, 2.0), "0.0")
    assert got == 0.0, f"expected 0.0 for k = {k} (a count is never negative), got {got!r}"
    _python_float(got)


def test_poisson_pmf_refuses_a_negative_lambda(distributions):
    _expect_value_error(lambda: distributions.poisson_pmf(1, -0.5), "poisson_pmf(1, -0.5)", "lam < 0")


# ---------------------------------------------------------------- normal_pdf
def test_normal_pdf_docstring_example(distributions):
    got = _result(lambda: distributions.normal_pdf(0), "0.398942… (the docstring example)")
    assert got == pytest.approx(1 / math.sqrt(2 * math.pi), rel=1e-12), (
        f"expected 1/√(2π) ≈ 0.398942 (the docstring example), got {got!r}")


@pytest.mark.parametrize("x, mu, sigma", [(1.5, 0.0, 1.0), (-2.0, 1.0, 0.5), (7.4, 5.0, 2.0), (-3.0, -1.0, 0.25),
                                          (100.0, 98.0, 4.0), (40.0, 0.0, 1.0)],
                         ids=["1.5", "-2|1,0.5", "7.4|5,2", "-3|-1,0.25", "100|98,4", "far"])
def test_normal_pdf_matches_scipy(distributions, x, mu, sigma):
    expected = float(stats.norm(mu, sigma).pdf(x))
    got = _result(lambda: distributions.normal_pdf(x, mu, sigma),
                  f"{expected} (scipy.stats.norm({mu}, {sigma}).pdf({x}))")
    assert got == pytest.approx(expected, rel=1e-9, abs=1e-300), (
        f"expected {expected} for N(μ = {mu}, σ = {sigma}) at x = {x}, got {got!r}")


def test_normal_pdf_default_parameters(distributions):
    got = _result(lambda: distributions.normal_pdf(1.0), "the standard normal density at 1")
    assert got == pytest.approx(float(stats.norm.pdf(1.0)), rel=1e-12), (
        f"expected φ(1) ≈ 0.241971 (mu = 0 and sigma = 1 by default), got {got!r}")


def test_normal_pdf_sigma_is_a_standard_deviation(distributions):
    expected = float(stats.norm(0, 2).pdf(1.0))
    got = _result(lambda: distributions.normal_pdf(1.0, 0.0, 2.0), f"{expected}")
    wrong = float(stats.norm(0, math.sqrt(2)).pdf(1.0))
    assert got == pytest.approx(expected, rel=1e-12), (
        f"expected {expected} for sigma = 2 (sigma is the standard deviation: the variance is 4)"
        + (", got the value for a variance of 2" if got == pytest.approx(wrong) else f", got {got!r}"))


def test_normal_pdf_can_exceed_1(distributions):
    got = _result(lambda: distributions.normal_pdf(0.0, 0.0, 0.1), "about 3.989")
    assert got == pytest.approx(10 / math.sqrt(2 * math.pi), rel=1e-12), (
        f"expected 10/√(2π) ≈ 3.989 for sigma = 0.1 (a density can exceed 1), got {got!r}")


def test_normal_pdf_returns_a_float(distributions):
    got = _result(lambda: distributions.normal_pdf(0.5, 0, 1), "a float")
    _python_float(got)


@pytest.mark.parametrize("sigma", [0.0, -1.0], ids=["sigma0", "sigma-1"])
def test_normal_pdf_refuses_sigma_not_positive(distributions, sigma):
    _expect_value_error(lambda: distributions.normal_pdf(0.0, 0.0, sigma), f"normal_pdf(0.0, 0.0, {sigma})",
                        "sigma must be positive")


# ---------------------------------------------------------------- normal_cdf
def test_normal_cdf_docstring_examples(distributions):
    got = _result(lambda: distributions.normal_cdf(0), "0.5 (the docstring example)")
    assert got == pytest.approx(0.5, abs=1e-15), f"expected 0.5 (the docstring example), got {got!r}"
    got = _result(lambda: distributions.normal_cdf(1.96), "0.975 (the docstring example)")
    assert round(got, 4) == 0.975, f"expected 0.975 once rounded to 4 decimals (the docstring example), got {got!r}"


@pytest.mark.parametrize("x, mu, sigma", [(-1.3, 0.0, 1.0), (2.7, 1.0, 0.8), (5.0, 5.0, 3.0), (-8.0, 0.0, 1.0),
                                          (6.0, 0.0, 1.0), (250.0, 252.5, 2.0)],
                         ids=["-1.3", "2.7|1,0.8", "mu", "-8", "6", "250|252.5,2"])
def test_normal_cdf_matches_scipy(distributions, x, mu, sigma):
    expected = float(stats.norm(mu, sigma).cdf(x))
    got = _result(lambda: distributions.normal_cdf(x, mu, sigma),
                  f"{expected} (scipy.stats.norm({mu}, {sigma}).cdf({x}))")
    without_root_2 = (1 + math.erf((x - mu) / sigma)) / 2
    hint = (" (that is (1 + erf(z)) / 2: Φ(z) = (1 + erf(z / √2)) / 2)"
            if abs(expected - without_root_2) > 1e-9 and got == pytest.approx(without_root_2, abs=1e-12) else "")
    assert got == pytest.approx(expected, abs=1e-12), (
        f"expected {expected} = Φ(({x} − {mu}) / {sigma}), got {got!r}{hint}")


def test_normal_cdf_default_parameters(distributions):
    got = _result(lambda: distributions.normal_cdf(-0.5), "Φ(−0.5)")
    assert got == pytest.approx(float(stats.norm.cdf(-0.5)), abs=1e-12), (
        f"expected Φ(−0.5) ≈ 0.308538 (mu = 0 and sigma = 1 by default), got {got!r}")


def test_normal_cdf_sigma_is_a_standard_deviation(distributions):
    expected = float(stats.norm(1, 2).cdf(3.0))
    got = _result(lambda: distributions.normal_cdf(3.0, 1.0, 2.0), f"{expected}")
    assert got == pytest.approx(expected, abs=1e-12), (
        f"expected Φ(1) ≈ {expected:.6f} for x = 3, mu = 1, sigma = 2: standardise by the standard deviation, "
        f"z = (x − mu) / sigma; got {got!r}")


def test_normal_cdf_returns_a_float(distributions):
    got = _result(lambda: distributions.normal_cdf(0.3), "a float")
    _python_float(got)


@pytest.mark.parametrize("sigma", [0.0, -2.0], ids=["sigma0", "sigma-2"])
def test_normal_cdf_refuses_sigma_not_positive(distributions, sigma):
    _expect_value_error(lambda: distributions.normal_cdf(1.0, 0.0, sigma), f"normal_cdf(1.0, 0.0, {sigma})",
                        "sigma must be positive")


# ---------------------------------------------------------------- inverse_transform_sample
def test_inverse_transform_sample_docstring_example(distributions):
    xs = _result(lambda: distributions.inverse_transform_sample(lambda u: 3 * u, 10_000), "an array of 10000 values")
    assert isinstance(xs, np.ndarray), f"expected a numpy.ndarray, got {type(xs).__name__}"
    assert xs.shape == (10_000,), f"expected the shape (10000,), got {xs.shape}"
    assert xs.min() >= 0 and xs.max() <= 3, f"expected values in [0, 3], got min {xs.min()} and max {xs.max()}"


def test_inverse_transform_sample_applies_inverse_cdf_to_the_uniforms_in_order(distributions):
    expected = 3 * np.random.default_rng(0).random(6)
    got = _result(lambda: distributions.inverse_transform_sample(lambda u: 3 * u, 6),
                  "3 × the 6 uniforms of default_rng(0).random(6), in order")
    got = np.asarray(got, dtype=float)
    assert got.shape == (6,) and np.allclose(got, expected, rtol=0, atol=1e-15), (
        f"expected {np.round(expected, 6).tolist()} (the uniforms of numpy.random.default_rng(0).random(6), in this "
        f"order, each passed to inverse_cdf), got {np.round(got, 6).tolist()}")


def test_inverse_transform_sample_uses_the_seed(distributions):
    expected = -np.log1p(-np.random.default_rng(7).random(5))
    got = _result(lambda: distributions.inverse_transform_sample(lambda u: -math.log(1 - u), 5, seed=7),
                  "the exponential draws of seed 7")
    assert np.allclose(np.asarray(got, dtype=float), expected, rtol=1e-12, atol=0), (
        f"expected {np.round(expected, 6).tolist()} with seed=7 (default_rng(seed).random(n)), "
        f"got {np.round(np.asarray(got, dtype=float), 6).tolist()}")


def test_inverse_transform_sample_default_seed_is_0(distributions):
    expected = 5 + 2 * np.random.default_rng(0).random(4)
    got = _result(lambda: distributions.inverse_transform_sample(lambda u: 5 + 2 * u, 4), "the draws of seed 0")
    assert np.allclose(np.asarray(got, dtype=float), expected, rtol=0, atol=1e-14), (
        f"expected {np.round(expected, 6).tolist()} without seed=... (seed=0 by default), "
        f"got {np.round(np.asarray(got, dtype=float), 6).tolist()}")


def test_inverse_transform_sample_passes_one_float_at_a_time(distributions):
    received = []

    def inverse_cdf(u):
        received.append(u)
        return math.sqrt(u)      # math.sqrt refuses an array of several values

    got = _result(lambda: distributions.inverse_transform_sample(inverse_cdf, 3), "3 values, inverse_cdf called 3 times")
    assert len(received) == 3 and all(np.ndim(u) == 0 for u in received), (
        f"expected inverse_cdf to be called once per uniform, with one float (the docstring: inverse_cdf(u) for one "
        f"float u), got {len(received)} call(s)")
    assert np.allclose(np.asarray(got, dtype=float), np.sqrt(np.random.default_rng(0).random(3)), atol=1e-15), (
        "expected the square roots of the 3 uniforms of seed 0")


def test_inverse_transform_sample_returns_an_array_of_floats(distributions):
    got = _result(lambda: distributions.inverse_transform_sample(lambda u: int(6 * u) + 1, 5),
                  "an array of floats, even when inverse_cdf returns integers")
    assert isinstance(got, np.ndarray), f"expected a numpy.ndarray (np.array(...)), got {type(got).__name__}"
    assert got.dtype.kind == "f", (
        f"expected an array of floats (dtype float, the docstring), got dtype {got.dtype}: np.array(values, "
        f"dtype=float)")
    assert got.shape == (5,), f"expected the shape (5,), got {got.shape}"


def test_inverse_transform_sample_with_n_1(distributions):
    got = _result(lambda: distributions.inverse_transform_sample(lambda u: u, 1), "an array of shape (1,)")
    assert isinstance(got, np.ndarray) and got.shape == (1,), (
        f"expected an array of shape (1,) for n = 1, got {type(got).__name__} {np.shape(got)}")


def test_inverse_transform_sample_gives_the_exponential_law(distributions):
    xs = _result(lambda: distributions.inverse_transform_sample(lambda u: -math.log(1 - u) / 2, 20_000, seed=1),
                 "20000 exponential draws")
    xs = np.asarray(xs, dtype=float)
    p_value = stats.kstest(xs, stats.expon(scale=0.5).cdf).pvalue
    assert p_value > 1e-3, (
        f"expected the draws of −ln(1 − U)/2 to follow the exponential law of parameter 2 (Kolmogorov-Smirnov "
        f"p-value > 0.001), got a p-value of {p_value:.2e}")


@pytest.mark.parametrize("n", [0, -3], ids=["n0", "n-3"])
def test_inverse_transform_sample_refuses_n_below_1(distributions, n):
    _expect_value_error(lambda: distributions.inverse_transform_sample(lambda u: u, n),
                        f"inverse_transform_sample(f, {n})", "at least one draw")
