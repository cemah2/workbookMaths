"""Tests of mymath.likelihood (chapter M13a): Bernoulli log-likelihood, maximum likelihood estimates (Bernoulli,
categorical with smoothing, Gaussian) and the logistic loss computed from scores.

Oracles: SciPy (``scipy.stats.bernoulli``, ``scipy.stats.norm``, ``scipy.special.log_expit``, ``xlogy``),
scikit-learn (``sklearn.metrics.log_loss``), ``fractions.Fraction`` for exact smoothed estimates, and properties (an
estimate of maximum likelihood is not beaten by its neighbours, the loss of a score 0 is ln 2). They describe the
expected behaviour without showing the solution.

    pytest tests/test_m13a_likelihood.py              # your code
    pytest tests/test_m13a_likelihood.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings
from fractions import Fraction

import numpy as np
import pytest
from scipy import special, stats
from sklearn.metrics import log_loss


@pytest.fixture
def likelihood(mymath_module):
    return mymath_module("likelihood")


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    try:
        return call()
    except NotImplementedError:
        raise                 # a function not written yet: ⏳
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised {type(exc).__name__}: {exc}"
                    + (f" ({hint})" if hint else ""))


def _quiet(call, expected, what="", hint=""):
    """_result(call), a RuntimeWarning (overflow, ln 0, 0/0) becoming a failure that says what was expected."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)
        try:
            return call()
        except RuntimeWarning as warning:
            pytest.fail(f"expected {expected}{' for ' + what if what else ''} without a RuntimeWarning, got "
                        f"RuntimeWarning: {warning}" + (f" ({hint})" if hint else ""))
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
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


def _show(v):
    return np.array2string(np.asarray(v, dtype=float), precision=6, suppress_small=False).replace("\n", "")


FORBIDDEN_MODULES = ("scipy", "sklearn")


def test_likelihood_uses_no_ready_made_tool(likelihood):
    """likelihood.py computes by itself: NumPy and math only, no SciPy nor scikit-learn."""
    try:
        tree = ast.parse(inspect.getsource(likelihood))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(a.name for a in node.names if a.name.split(".")[0] in FORBIDDEN_MODULES)
        elif isinstance(node, ast.ImportFrom) and node.module and node.module.split(".")[0] in FORBIDDEN_MODULES:
            found.add(node.module)
    assert not found, (f"expected likelihood.py to use NumPy and math only, found imports of {sorted(found)}: the "
                       f"tests compare your results with SciPy and scikit-learn, so write the formulas yourself")


# ---------------------------------------------------------------- data
RNG = np.random.default_rng(1310)


def _scipy_log_likelihood(y, p):
    return float(np.sum(stats.bernoulli.logpmf(np.asarray(y, dtype=int), np.broadcast_to(p, np.shape(y)))))


LL_CASES = {
    "shared-p": ([1, 1, 0, 1, 0, 1, 1], 0.6),
    "per-label-p": ([1, 0, 0, 1, 1], [0.9, 0.2, 0.35, 0.5, 0.71]),
    "all-zero": ([0, 0, 0, 0], 0.15),
    "one-label": ([1], 0.4),
    "random-200": (RNG.integers(0, 2, size=200).tolist(), RNG.uniform(0.01, 0.99, size=200).tolist()),
    "tiny-p": ([0, 0, 1], [1e-12, 1e-9, 0.5]),
}


# ---------------------------------------------------------------- bernoulli_log_likelihood
@pytest.mark.parametrize("name", list(LL_CASES))
def test_bernoulli_log_likelihood_matches_scipy(likelihood, name):
    y, p = LL_CASES[name]
    expected = _scipy_log_likelihood(y, p)
    got = _quiet(lambda: likelihood.bernoulli_log_likelihood(list(y), p), "a float", name)
    _python_float(got, f"bernoulli_log_likelihood for {name}")
    assert math.isclose(got, expected, rel_tol=1e-9, abs_tol=1e-12), (
        f"expected the log-likelihood {expected:.10g} for {name} (scipy.stats.bernoulli.logpmf, summed), got {got!r} "
        f"(ln p_i for a label 1, ln(1 - p_i) for a label 0, then the SUM)")


def test_bernoulli_log_likelihood_docstring_example(likelihood):
    got = _result(lambda: likelihood.bernoulli_log_likelihood([1, 0, 1, 1], 0.75), "a float")
    assert round(got, 4) == -2.2493, f"expected -2.2493 for y = [1, 0, 1, 1] and p = 0.75, got {got!r}"


def test_bernoulli_log_likelihood_of_an_impossible_label_is_minus_inf(likelihood):
    for y, p in (([1, 0, 1], [0.5, 1.0, 0.5]), ([1, 0], [1.0, 1.0]), ([1, 1], 0.0)):
        got = _quiet(lambda: likelihood.bernoulli_log_likelihood(y, p), "-inf", f"y = {y}, p = {p}",
                     "a label of probability 0: return -math.inf, ln 0 must not be computed with a warning")
        assert got == -math.inf, f"expected -inf for y = {y} and p = {p} (a label of probability 0), got {got!r}"


def test_bernoulli_log_likelihood_counts_zero_log_zero_as_zero(likelihood):
    for y, p in (([1, 1, 0], [1.0, 1.0, 0.0]), ([0, 0], 0.0), ([1, 1], 1.0)):
        got = _quiet(lambda: likelihood.bernoulli_log_likelihood(y, p), "0.0", f"y = {y}, p = {p}",
                     "only the probability of the OBSERVED label counts: 0 · ln 0 is 0")
        assert got == 0.0, (f"expected 0.0 for y = {y} and p = {p} (every label is certain), got {got!r} (the terms "
                            f"0 · ln 0 count as 0: take ln of the probability of the observed label only)")


def test_bernoulli_log_likelihood_accepts_booleans_and_float_labels(likelihood):
    expected = _scipy_log_likelihood([1, 0, 1], 0.25)
    for y in ([True, False, True], [1.0, 0.0, 1.0], np.array([1, 0, 1])):
        got = _result(lambda: likelihood.bernoulli_log_likelihood(y, 0.25), "a float", f"y = {y!r}")
        assert math.isclose(got, expected, rel_tol=1e-12), f"expected {expected:.10g} for y = {y!r}, got {got!r}"


def test_bernoulli_log_likelihood_is_largest_at_the_proportion(likelihood):
    y = [1, 0, 1, 1, 0, 1, 1, 1]                        # proportion 0.75
    best = _result(lambda: likelihood.bernoulli_log_likelihood(y, 0.75), "a float")
    for p in np.linspace(0.05, 0.95, 19):
        other = likelihood.bernoulli_log_likelihood(y, float(p))
        assert other <= best + 1e-12, (f"expected the log-likelihood at p = {p:.2f} ({other:.6f}) to be at most the "
                                       f"one at the proportion 0.75 ({best:.6f})")


def test_bernoulli_log_likelihood_does_not_modify_its_inputs(likelihood):
    y, p = np.array([1.0, 0.0, 1.0]), np.array([0.3, 0.3, 0.9])
    y0, p0 = y.copy(), p.copy()
    _result(lambda: likelihood.bernoulli_log_likelihood(y, p), "a float")
    assert np.array_equal(y, y0) and np.array_equal(p, p0), "expected y and p to be unchanged after the call"


@pytest.mark.parametrize("y, p, why", [
    ([], 0.5, "an empty y"),
    ([1, 2, 0], 0.5, "a label 2"),
    ([1, 0.5, 0], 0.5, "a label 0.5"),
    ([1, 0, 1], [0.5, 0.5], "p has 2 values for 3 labels"),
    ([1, 0, 1], [0.5], "p is a list of 1 value for 3 labels: one probability per label, or a single number"),
    ([1, 0], 1.2, "p = 1.2 is not a probability"),
    ([1, 0], [0.5, -0.1], "p = -0.1 is not a probability"),
    ([1, 0], [0.5, float("nan")], "p = nan is not a probability"),
])
def test_bernoulli_log_likelihood_rejects_bad_inputs(likelihood, y, p, why):
    _expect_value_error(lambda: likelihood.bernoulli_log_likelihood(y, p), f"bernoulli_log_likelihood({y}, {p})",
                        why)


# ---------------------------------------------------------------- bernoulli_mle
@pytest.mark.parametrize("y", [[1, 0, 1, 1], [0, 0, 0], [1], [True, False, False, True, True],
                               RNG.integers(0, 2, size=101).tolist()])
def test_bernoulli_mle_is_the_proportion(likelihood, y):
    expected = float(np.mean(np.asarray(y, dtype=float)))
    got = _result(lambda: likelihood.bernoulli_mle(y), "a float", f"y = {y[:6]}…")
    _python_float(got, "bernoulli_mle")
    assert math.isclose(got, expected, rel_tol=1e-12, abs_tol=0), (
        f"expected the proportion of 1, {expected!r}, got {got!r}")


def test_bernoulli_mle_maximizes_the_log_likelihood(likelihood):
    y = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1]
    p_hat = _result(lambda: likelihood.bernoulli_mle(y), "a float")
    best = _scipy_log_likelihood(y, p_hat)
    for p in np.linspace(0.01, 0.99, 99):
        assert _scipy_log_likelihood(y, p) <= best + 1e-12, (
            f"expected p̂ = {p_hat!r} to maximize the log-likelihood (scipy), but p = {p:.2f} does better")


@pytest.mark.parametrize("y, why", [([], "an empty y"), ([0, 1, 2], "a label 2"), ([0.5, 1], "a label 0.5")])
def test_bernoulli_mle_rejects_bad_labels(likelihood, y, why):
    _expect_value_error(lambda: likelihood.bernoulli_mle(y), f"bernoulli_mle({y})", why)


# ---------------------------------------------------------------- categorical_mle
def _fraction_estimate(counts, alpha):
    a = Fraction(alpha).limit_denominator(1000)
    total = sum(Fraction(c) for c in counts) + len(counts) * a
    return [float((Fraction(c) + a) / total) for c in counts]


CAT_CASES = [([3, 1, 0], 0), ([3, 1, 0], 1), ([5, 0, 2, 7], 0.5), ([12, 30, 8], 3), ([0, 4], 1), ([9], 0),
             ([2, 2, 2, 2, 2], 2), (list(RNG.integers(0, 20, size=12)), 1)]


@pytest.mark.parametrize("counts, alpha", CAT_CASES)
def test_categorical_mle_matches_exact_fractions(likelihood, counts, alpha):
    expected = _fraction_estimate(counts, alpha)
    got = _quiet(lambda: likelihood.categorical_mle(list(counts), alpha=alpha), "an array",
                 f"counts = {counts}, alpha = {alpha}")
    assert isinstance(got, np.ndarray), (f"expected a numpy.ndarray of floats (np.array(...)), got "
                                         f"{type(got).__module__}.{type(got).__name__}")
    assert got.shape == (len(counts),) and np.issubdtype(got.dtype, np.floating), (
        f"expected {len(counts)} floats, got shape {got.shape} and dtype {got.dtype}")
    assert np.allclose(got, expected, rtol=1e-12, atol=0), (
        f"expected {_show(expected)} for counts = {counts} and alpha = {alpha} ((n_k + alpha) / (N + K alpha), "
        f"exact fractions), got {_show(got)}")


def test_categorical_mle_docstring_examples(likelihood):
    got = _result(lambda: likelihood.categorical_mle([3, 1, 0]), "an array")
    assert np.allclose(got, [0.75, 0.25, 0.0]), f"expected [0.75, 0.25, 0] for counts [3, 1, 0], got {_show(got)}"
    got = _result(lambda: likelihood.categorical_mle([3, 1, 0], alpha=1), "an array")
    assert np.allclose(got, [4 / 7, 2 / 7, 1 / 7]), (
        f"expected [4/7, 2/7, 1/7] for counts [3, 1, 0] and alpha = 1, got {_show(got)} (alpha is added to each of "
        f"the K counts: the denominator is N + K alpha)")


def test_categorical_mle_smoothing_never_gives_zero(likelihood):
    for counts in ([10, 0, 0, 3], [0, 0, 0]):
        got = _quiet(lambda: likelihood.categorical_mle(counts, alpha=0.5), "an array", f"counts = {counts}")
        assert np.all(got > 0) and math.isclose(float(np.sum(got)), 1.0, rel_tol=1e-12), (
            f"expected positive probabilities of sum 1 for counts = {counts} and alpha = 0.5, got {_show(got)}")
    got = likelihood.categorical_mle([0, 0, 0], alpha=0.5)
    assert np.allclose(got, [1 / 3] * 3), f"expected the uniform law for counts [0, 0, 0] and alpha = 0.5, got {_show(got)}"


def test_categorical_mle_maximizes_the_categorical_log_likelihood(likelihood):
    counts = np.array([7, 2, 0, 11])
    p_hat = _result(lambda: likelihood.categorical_mle(counts.tolist()), "an array")
    best = float(np.sum(special.xlogy(counts, p_hat)))
    rng = np.random.default_rng(1311)
    for q in rng.dirichlet(np.ones(4), size=200):
        other = float(np.sum(special.xlogy(counts, q)))
        assert other <= best + 1e-12, (f"expected p̂ = {_show(p_hat)} to maximize Σ n_k ln p_k, but {_show(q)} does "
                                       f"better ({other:.6f} > {best:.6f})")


def test_categorical_mle_does_not_modify_the_counts(likelihood):
    counts = np.array([4.0, 1.0, 5.0])
    _result(lambda: likelihood.categorical_mle(counts, alpha=1.0), "an array")
    assert np.array_equal(counts, [4.0, 1.0, 5.0]), f"expected the counts to be unchanged, got {_show(counts)}"


@pytest.mark.parametrize("counts, alpha, why", [
    ([], 0.0, "empty counts"),
    ([[1, 2], [3, 4]], 0.0, "counts in 2-D"),
    ([3, -1, 2], 0.0, "a negative count"),
    ([3, 1, 2], -0.5, "alpha < 0"),
    ([0, 0, 0], 0.0, "every count is 0 and alpha = 0: 0/0"),
    ([2, float("nan")], 1.0, "a count nan"),
])
def test_categorical_mle_rejects_bad_inputs(likelihood, counts, alpha, why):
    _expect_value_error(lambda: likelihood.categorical_mle(counts, alpha=alpha),
                        f"categorical_mle({counts}, alpha={alpha})", why)


# ---------------------------------------------------------------- gaussian_mle
GAUSS_CASES = {
    "docstring": [2, 4, 4, 6],
    "small": [1.5, -0.5, 3.0, 2.0, 0.0],
    "one-value": [7.25],
    "normal-500": RNG.normal(3.0, 2.0, size=500).tolist(),
    "integers": list(range(1, 11)),
}


@pytest.mark.parametrize("name", list(GAUSS_CASES))
def test_gaussian_mle_matches_scipy(likelihood, name):
    x = GAUSS_CASES[name]
    mean, std = stats.norm.fit(np.asarray(x, dtype=float)) if len(x) > 1 else (float(x[0]), 0.0)
    got = _quiet(lambda: likelihood.gaussian_mle(list(x)), "a tuple (mean, variance)", name)
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (mean, variance) for {name}, got {got!r}"
    _python_float(got[0], "the mean")
    _python_float(got[1], "the variance")
    assert math.isclose(got[0], mean, rel_tol=1e-12, abs_tol=1e-12), (
        f"expected the mean {mean!r} for {name} (scipy.stats.norm.fit), got {got[0]!r}")
    variance = float(np.var(np.asarray(x, dtype=float)))
    hint = ""
    if len(x) > 1 and math.isclose(got[1], variance * len(x) / (len(x) - 1), rel_tol=1e-9):
        hint = " (that is the division by n - 1: the maximum likelihood divides by n)"
    elif math.isclose(got[1], math.sqrt(variance), rel_tol=1e-9) and variance not in (0.0, 1.0):
        hint = " (that is the standard deviation: return the variance)"
    assert math.isclose(got[1], std ** 2, rel_tol=1e-9, abs_tol=1e-12), (
        f"expected the variance {std ** 2!r} for {name} (the square of scipy.stats.norm.fit's scale), got "
        f"{got[1]!r}{hint}")


def test_gaussian_mle_keeps_its_digits_for_a_large_mean(likelihood):
    x = (1e9 + np.array([-1.0, 1.0, -1.0, 1.0, 0.0, 0.0])).tolist()       # variance 2/3 around 1e9
    got = _result(lambda: likelihood.gaussian_mle(x), "a tuple (mean, variance)")
    assert math.isclose(got[1], 2 / 3, rel_tol=1e-6), (
        f"expected the variance 2/3 for 1e9 ± 1, got {got[1]!r} (compute the deviations x_i - μ̂ first, then the mean "
        f"of their squares: the mean of x² minus μ̂² loses all its digits when the mean is large)")


def test_gaussian_mle_maximizes_the_gaussian_log_likelihood(likelihood):
    x = np.array(GAUSS_CASES["small"])
    mean, variance = _result(lambda: likelihood.gaussian_mle(x.tolist()), "a tuple (mean, variance)")
    best = float(np.sum(stats.norm.logpdf(x, mean, math.sqrt(variance))))
    for dm in (-0.2, 0.0, 0.2):
        for factor in (0.8, 1.0, 1.25):
            if dm == 0.0 and factor == 1.0:
                continue
            other = float(np.sum(stats.norm.logpdf(x, mean + dm, math.sqrt(variance * factor))))
            assert other < best, (f"expected (μ̂, σ̂²) = ({mean:.4f}, {variance:.4f}) to maximize the log-likelihood "
                                  f"(scipy.stats.norm.logpdf), but ({mean + dm:.4f}, {variance * factor:.4f}) does "
                                  f"better")


def test_gaussian_mle_does_not_modify_the_sample(likelihood):
    x = np.array([3.0, 1.0, 2.0])
    _result(lambda: likelihood.gaussian_mle(x), "a tuple (mean, variance)")
    assert np.array_equal(x, [3.0, 1.0, 2.0]), f"expected x to be unchanged, got {_show(x)}"


@pytest.mark.parametrize("x, why", [([], "an empty sample"), ([[1.0, 2.0], [3.0, 4.0]], "a sample in 2-D")])
def test_gaussian_mle_rejects_bad_samples(likelihood, x, why):
    _expect_value_error(lambda: likelihood.gaussian_mle(x), f"gaussian_mle({x})", why)


# ---------------------------------------------------------------- logistic_loss
def _loss_oracle(z, y):
    """The mean of -ln σ(z) for a label 1 and -ln(1 - σ(z)) = -ln σ(-z) for a label 0 (scipy.special.log_expit)."""
    z, y = np.asarray(z, dtype=float), np.asarray(y, dtype=float)
    return float(np.mean(-np.where(y == 1, special.log_expit(z), special.log_expit(-z))))


LOSS_CASES = {
    "moderate": ([0.5, -1.2, 2.0, -0.3, 3.1], [1, 0, 1, 1, 0]),
    "zero-scores": ([0.0, 0.0, 0.0], [1, 0, 1]),
    "one": ([-2.5], [1]),
    "random-300": (RNG.normal(0.0, 3.0, size=300).tolist(), RNG.integers(0, 2, size=300).tolist()),
}


@pytest.mark.parametrize("name", list(LOSS_CASES))
def test_logistic_loss_matches_sklearn_log_loss(likelihood, name):
    z, y = LOSS_CASES[name]
    expected = log_loss(y, special.expit(np.asarray(z, dtype=float)), labels=[0, 1])
    got = _quiet(lambda: likelihood.logistic_loss(list(z), list(y)), "a float", name)
    _python_float(got, f"logistic_loss for {name}")
    hint = ""
    if math.isclose(got, expected * len(y), rel_tol=1e-9) and len(y) > 1:
        hint = " (that is the SUM: return the mean)"
    assert math.isclose(got, expected, rel_tol=1e-9, abs_tol=1e-12), (
        f"expected the mean log-loss {expected:.10g} for {name} (sklearn.metrics.log_loss of σ(z)), got {got!r}{hint}")


def test_logistic_loss_docstring_examples(likelihood):
    got = _result(lambda: likelihood.logistic_loss([0.0, 0.0], [1, 0]), "a float")
    assert round(got, 6) == 0.693147, f"expected ln 2 ≈ 0.693147 for two scores 0, got {got!r}"
    got = _result(lambda: likelihood.logistic_loss([30.0, -30.0], [0, 1]), "a float")
    assert round(got, 6) == 30.0, f"expected 30.0 for scores [30, -30] and labels [0, 1], got {got!r}"


@pytest.mark.parametrize("z, y", [([1000.0, -1000.0], [1, 0]), ([1000.0, -1000.0], [0, 1]),
                                  ([745.5, -800.0, 50.0, -60.0], [0, 1, 1, 0]), ([-1e6], [1])])
def test_logistic_loss_does_not_overflow(likelihood, z, y):
    expected = _loss_oracle(z, y)
    got = _quiet(lambda: likelihood.logistic_loss(z, y), "a finite float", f"z = {z}",
                 "ln(1 + e^z) = max(z, 0) + ln(1 + e^(-|z|)), with np.log1p")
    assert math.isfinite(got) and math.isclose(got, expected, rel_tol=1e-12, abs_tol=1e-300), (
        f"expected {expected!r} for z = {z} and y = {y} (scipy.special.log_expit), got {got!r} (very large scores must "
        f"give finite results: compute the softplus as max(z, 0) + ln(1 + e^(-|z|)))")


def test_logistic_loss_is_non_negative_and_accepts_booleans(likelihood):
    z = RNG.normal(0.0, 10.0, size=50)
    y = RNG.integers(0, 2, size=50).astype(bool)
    got = _result(lambda: likelihood.logistic_loss(z, y), "a float")
    assert got >= 0 and math.isclose(got, _loss_oracle(z, y), rel_tol=1e-12), (
        f"expected {_loss_oracle(z, y)!r} for boolean labels, got {got!r}")


def test_logistic_loss_does_not_modify_its_inputs(likelihood):
    z, y = np.array([2.0, -1.0]), np.array([1.0, 0.0])
    _result(lambda: likelihood.logistic_loss(z, y), "a float")
    assert np.array_equal(z, [2.0, -1.0]) and np.array_equal(y, [1.0, 0.0]), "expected z and y to be unchanged"


@pytest.mark.parametrize("z, y, why", [
    ([0.5, 1.0, -2.0], [1, 0], "3 scores for 2 labels"),
    ([0.5], [1, 0], "1 score for 2 labels"),
    ([], [], "no labels"),
    ([0.5, 1.0], [1, 2], "a label 2"),
    ([0.5, 1.0], [1, -1], "a label -1 (the labels are 0 and 1, not -1 and 1)"),
])
def test_logistic_loss_rejects_bad_inputs(likelihood, z, y, why):
    _expect_value_error(lambda: likelihood.logistic_loss(z, y), f"logistic_loss({z}, {y})", why)
