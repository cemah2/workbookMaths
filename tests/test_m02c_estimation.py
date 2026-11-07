"""Tests of mymath.estimation (chapter M02c): sample means, bias and mean squared error, standard error, interval.

Oracles: the same draws replayed with ``numpy.random.default_rng`` and averaged with NumPy, ``scipy.stats.sem`` and
``numpy.std``. They describe the expected behaviour without showing the solution.

    pytest tests/test_m02c_estimation.py              # your code
    pytest tests/test_m02c_estimation.py --impl=ref   # the reference
"""

import ast
import inspect
import math

import numpy as np
import pytest
from scipy import stats


@pytest.fixture
def estimation(mymath_module):
    return mymath_module("estimation")


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


def _replayed_means(draw, n, repeats, seed):
    """The oracle: one generator, draw(rng, n) called repeats times in order, the mean of each sample."""
    rng = np.random.default_rng(seed)
    return np.array([np.mean(draw(rng, n)) for _ in range(repeats)])


def _replayed_estimates(estimator, draw_sample, repeats, seed):
    rng = np.random.default_rng(seed)
    return np.array([estimator(draw_sample(rng)) for _ in range(repeats)], dtype=float)


def _normal_5(rng):
    return rng.normal(10.0, 2.0, 5)


def _var_0(sample):
    return float(np.var(sample))


def _var_1(sample):
    return float(np.var(sample, ddof=1))


# ---------------------------------------------------------------- no ready-made tool
def test_estimation_uses_no_scipy(estimation):
    """estimation.py computes its results itself: no SciPy (the tests compare with scipy.stats.sem)."""
    try:
        tree = ast.parse(inspect.getsource(estimation))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    assert "scipy" not in imported, (
        "expected estimation.py not to import SciPy (the tests compare your results with scipy.stats.sem): write "
        "the formulas yourself, NumPy is allowed")


# ---------------------------------------------------------------- sample_means
def test_sample_means_docstring_example(estimation):
    means = _result(lambda: estimation.sample_means(lambda rng, n: rng.random(n), 12, 4_000), "4000 means")
    assert isinstance(means, np.ndarray) and means.shape == (4_000,), (
        f"expected a numpy.ndarray of shape (4000,), got {type(means).__name__} of shape {np.shape(means)}")
    assert abs(means.mean() - 0.5) < 0.01 and abs(means.std() - 1 / 12) < 0.005, (
        f"expected means around 0.5 with a standard deviation around 1/12 (the docstring example), got "
        f"{means.mean():.4f} and {means.std():.4f}")


@pytest.mark.parametrize("n, repeats, seed", [(5, 7, 0), (1, 4, 3), (30, 50, 11)], ids=["5x7", "1x4", "30x50"])
def test_sample_means_replays_the_draws_in_order(estimation, n, repeats, seed):
    draw = lambda rng, size: rng.exponential(2.0, size)   # noqa: E731
    expected = _replayed_means(draw, n, repeats, seed)
    got = _result(lambda: estimation.sample_means(draw, n, repeats, seed=seed),
                  f"the {repeats} means of default_rng({seed}), draw called {repeats} times in order")
    got = np.asarray(got, dtype=float)
    assert got.shape == (repeats,) and np.allclose(got, expected, rtol=1e-12, atol=0), (
        f"expected {np.round(expected[:4], 6).tolist()}… (one generator default_rng(seed) for everything, draw(rng, "
        f"n) called {repeats} times, one sample after the other), got {np.round(got[:4], 6).tolist()}…")


def test_sample_means_default_seed_is_0(estimation):
    draw = lambda rng, size: rng.integers(1, 7, size)   # noqa: E731
    expected = _replayed_means(draw, 4, 6, 0)
    got = _result(lambda: estimation.sample_means(draw, 4, 6), "the means of seed 0")
    assert np.allclose(np.asarray(got, dtype=float), expected, rtol=1e-12, atol=0), (
        f"expected {expected.tolist()} without seed=... (seed=0 by default), got {np.asarray(got).tolist()}")


def test_sample_means_accepts_a_draw_that_returns_a_list(estimation):
    draw = lambda rng, size: [float(v) for v in rng.random(size)]   # noqa: E731
    expected = _replayed_means(draw, 3, 5, 2)
    got = _result(lambda: estimation.sample_means(draw, 3, 5, seed=2), "5 means of lists")
    assert np.allclose(np.asarray(got, dtype=float), expected, rtol=1e-12, atol=0), (
        "expected the same means when draw returns a list (the docstring: a list or an array)")


def test_sample_means_returns_an_array_of_floats(estimation):
    got = _result(lambda: estimation.sample_means(lambda rng, size: rng.integers(0, 2, size), 2, 3), "an array")
    assert isinstance(got, np.ndarray), f"expected a numpy.ndarray (np.array(...)), got {type(got).__name__}"
    assert got.dtype.kind == "f", f"expected an array of floats, got dtype {got.dtype}"


def test_sample_means_calls_draw_with_n_repeats_times(estimation):
    calls = []

    def draw(rng, size):
        calls.append(size)
        return rng.random(size)

    _result(lambda: estimation.sample_means(draw, 8, 5), "5 calls of draw(rng, 8)")
    assert calls == [8] * 5, f"expected draw(rng, 8) to be called 5 times (one per sample), got the sizes {calls}"


@pytest.mark.parametrize("n, repeats, why", [(0, 5, "n < 1"), (4, 0, "repeats < 1"), (-2, 3, "n < 1")],
                         ids=["n0", "repeats0", "n-2"])
def test_sample_means_refuses_bad_sizes(estimation, n, repeats, why):
    _expect_value_error(lambda: estimation.sample_means(lambda rng, size: rng.random(size), n, repeats),
                        f"sample_means(draw, {n}, {repeats})", why)


# ---------------------------------------------------------------- estimator_bias
def test_estimator_bias_docstring_example(estimation):
    got = _result(lambda: estimation.estimator_bias(max, lambda rng: rng.random(4), 1.0, 20_000),
                  "about -0.2 (the docstring example)")
    assert round(got, 2) == -0.2, f"expected about -0.2 once rounded (the docstring example: E[max] = 4/5), got {got!r}"


@pytest.mark.parametrize("estimator, name", [(_var_0, "ddof=0"), (_var_1, "ddof=1"), (np.median, "median")],
                         ids=["var0", "var1", "median"])
def test_estimator_bias_replays_the_samples(estimation, estimator, name):
    true_value = 4.0 if name != "median" else 10.0
    expected = float(np.mean(_replayed_estimates(estimator, _normal_5, 300, 5)) - true_value)
    got = _result(lambda: estimation.estimator_bias(estimator, _normal_5, true_value, 300, seed=5),
                  f"{expected} (the mean of the 300 estimates minus the true value)")
    assert got == pytest.approx(expected, rel=1e-9, abs=1e-12), (
        f"expected {expected} (one generator default_rng(seed), draw_sample(rng) called 300 times in order, the mean "
        f"of the estimates minus true_value), got {got!r}")


def test_estimator_bias_returns_a_float(estimation):
    got = _result(lambda: estimation.estimator_bias(np.mean, _normal_5, 10.0, 20), "a float")
    _python_float(got)


def test_estimator_bias_of_the_variance_divided_by_n(estimation):
    got = _result(lambda: estimation.estimator_bias(_var_0, lambda rng: rng.standard_normal(5), 1.0, 20_000),
                  "about -0.2")
    assert abs(got - (-0.2)) < 0.02, (
        f"expected about -σ²/n = -0.2 for the variance divided by n on samples of 5 values of N(0, 1), got {got!r}")


def test_estimator_bias_refuses_repeats_below_1(estimation):
    _expect_value_error(lambda: estimation.estimator_bias(np.mean, _normal_5, 10.0, 0),
                        "estimator_bias(np.mean, draw, 10.0, 0)", "repeats < 1")


# ---------------------------------------------------------------- estimator_mse
def test_estimator_mse_docstring_example(estimation):
    got = _result(lambda: estimation.estimator_mse(max, lambda rng: rng.random(4), 1.0, 20_000),
                  "about 0.07 (the docstring example)")
    assert round(got, 2) == 0.07, f"expected about 0.07 once rounded (the docstring example), got {got!r}"


@pytest.mark.parametrize("estimator, name", [(_var_0, "ddof=0"), (_var_1, "ddof=1")], ids=["var0", "var1"])
def test_estimator_mse_replays_the_samples(estimation, estimator, name):
    estimates = _replayed_estimates(estimator, _normal_5, 300, 8)
    expected = float(np.mean((estimates - 4.0) ** 2))
    got = _result(lambda: estimation.estimator_mse(estimator, _normal_5, 4.0, 300, seed=8),
                  f"{expected} (the mean of the squared errors)")
    assert got == pytest.approx(expected, rel=1e-9), (
        f"expected {expected} (the mean of the 300 squared errors (θ̂ − θ)², the same samples as estimator_bias with "
        f"the same seed), got {got!r}")


def test_estimator_mse_is_bias_squared_plus_variance(estimation):
    estimates = _replayed_estimates(_var_1, _normal_5, 500, 13)
    expected = float(np.var(estimates) + (estimates.mean() - 4.0) ** 2)
    got = _result(lambda: estimation.estimator_mse(_var_1, _normal_5, 4.0, 500, seed=13), f"{expected}")
    assert got == pytest.approx(expected, rel=1e-9), (
        f"expected {expected} = (variance of the estimates) + bias², got {got!r}: the mean of (θ̂ − θ)², not of "
        f"(θ̂ − mean)²")


def test_estimator_mse_returns_a_float(estimation):
    got = _result(lambda: estimation.estimator_mse(np.mean, _normal_5, 10.0, 20), "a float")
    _python_float(got)


def test_estimator_mse_refuses_repeats_below_1(estimation):
    _expect_value_error(lambda: estimation.estimator_mse(np.mean, _normal_5, 10.0, -1),
                        "estimator_mse(np.mean, draw, 10.0, -1)", "repeats < 1")


# ---------------------------------------------------------------- standard_error
def test_standard_error_docstring_example(estimation):
    got = _result(lambda: estimation.standard_error([3, 5, 6, 10]), "1.472 (the docstring example)")
    assert round(got, 3) == 1.472, f"expected 1.472 once rounded (the docstring example), got {got!r}"


@pytest.mark.parametrize("sample", [[2.0, 7.5], [1, 4, 4, 9, 12, 3], list(np.linspace(-3, 8, 25) ** 2)],
                         ids=["2 values", "6 values", "25 values"])
def test_standard_error_matches_scipy(estimation, sample):
    expected = float(stats.sem(sample))
    got = _result(lambda: estimation.standard_error(sample), f"{expected} (scipy.stats.sem)")
    with_n = float(np.std(sample) / math.sqrt(len(sample)))
    hint = " (that is s divided by n, ddof = 0)" if got == pytest.approx(with_n, rel=1e-9) else ""
    assert got == pytest.approx(expected, rel=1e-12), (
        f"expected {expected} = s / √n with s divided by n − 1 (ddof = 1 by default), got {got!r}{hint}")


def test_standard_error_with_ddof_0(estimation):
    sample = [1.0, 2.0, 2.0, 5.0, 10.0]
    expected = float(np.std(sample) / math.sqrt(len(sample)))
    got = _result(lambda: estimation.standard_error(sample, ddof=0), f"{expected}")
    assert got == pytest.approx(expected, rel=1e-12), (
        f"expected {expected} with ddof=0 (the standard deviation divides by n), got {got!r}")


def test_standard_error_accepts_an_array_and_returns_a_float(estimation):
    got = _result(lambda: estimation.standard_error(np.array([4.0, 6.0, 9.0])), "a float")
    _python_float(got)
    expected = float(stats.sem([4.0, 6.0, 9.0]))
    assert got == pytest.approx(expected, rel=1e-12), f"expected {expected} for an array, as for a list, got {got!r}"


def test_standard_error_of_a_constant_sample_is_0(estimation):
    got = _result(lambda: estimation.standard_error([3.5, 3.5, 3.5]), "0.0")
    assert got == pytest.approx(0.0, abs=1e-15), f"expected 0.0 (no dispersion), got {got!r}"


@pytest.mark.parametrize("sample, ddof, why", [([5.0], 1, "one value with ddof = 1"), ([], 1, "an empty sample"),
                                               ([1.0, 2.0], 2, "two values with ddof = 2")],
                         ids=["1 value", "empty", "ddof2"])
def test_standard_error_refuses_too_small_samples(estimation, sample, ddof, why):
    _expect_value_error(lambda: estimation.standard_error(sample, ddof=ddof),
                        f"standard_error({sample}, ddof={ddof})", why)


# ---------------------------------------------------------------- confidence_interval_mean
def test_confidence_interval_mean_docstring_example(estimation):
    got = _result(lambda: estimation.confidence_interval_mean([1, 2, 3, 4, 5], z=2), "(1.5858, 4.4142)")
    low, high = got
    assert (round(low, 4), round(high, 4)) == (1.5858, 4.4142), (
        f"expected (1.5858, 4.4142) once rounded (the docstring example), got {got!r}")


@pytest.mark.parametrize("sample, z", [([10.2, 9.8, 11.5, 10.9, 9.1], 1.96), ([0, 1] * 20, 2.576),
                                       ([3.0, 8.0], 1.0)], ids=["5 values", "40 values z2.576", "2 values z1"])
def test_confidence_interval_mean_matches_mean_plus_minus_z_sem(estimation, sample, z):
    mean, sem = float(np.mean(sample)), float(stats.sem(sample))
    got = _result(lambda: estimation.confidence_interval_mean(sample, z=z), f"({mean - z * sem}, {mean + z * sem})")
    low, high = got
    assert low == pytest.approx(mean - z * sem, rel=1e-12) and high == pytest.approx(mean + z * sem, rel=1e-12), (
        f"expected ({mean - z * sem:.6f}, {mean + z * sem:.6f}) = mean ± z × s/√n (s with n − 1), "
        f"got ({low:.6f}, {high:.6f})")


def test_confidence_interval_mean_default_z_is_1_96(estimation):
    sample = [4.0, 7.0, 5.0, 6.0]
    mean, sem = float(np.mean(sample)), float(stats.sem(sample))
    got = _result(lambda: estimation.confidence_interval_mean(sample), "the interval with z = 1.96")
    assert got[0] == pytest.approx(mean - 1.96 * sem, rel=1e-12), (
        f"expected {mean - 1.96 * sem:.6f} without z=... (z = 1.96 by default), got {got[0]!r}")


def test_confidence_interval_mean_returns_a_tuple_of_two_floats(estimation):
    got = _result(lambda: estimation.confidence_interval_mean([1.0, 2.0, 4.0]), "a tuple (low, high)")
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (low, high), got {type(got).__name__} {got!r}"
    _python_float(got[0], "low")
    _python_float(got[1], "high")


@pytest.mark.parametrize("sample, z, why", [([4.0], 1.96, "one value"), ([1.0, 2.0, 3.0], 0, "z = 0"),
                                            ([1.0, 2.0, 3.0], -1.96, "z < 0")], ids=["1 value", "z0", "z-1.96"])
def test_confidence_interval_mean_refuses_bad_input(estimation, sample, z, why):
    _expect_value_error(lambda: estimation.confidence_interval_mean(sample, z=z),
                        f"confidence_interval_mean({sample}, z={z})", why)
