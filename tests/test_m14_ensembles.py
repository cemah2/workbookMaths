"""Tests of mymath.ensembles (chapter M14): the Chernoff bound on the tail of a binomial law, the variance of a
weighted average of correlated variables, and the exponential weights of the Hedge algorithm.

Oracles: SciPy (``scipy.special.rel_entr`` for the divergence, ``scipy.stats.binom`` for the exact tail,
``scipy.optimize.minimize_scalar`` for the best λ of Markov's inequality, ``scipy.special.softmax`` for normalized
exponentials), a factorization ``cov = B Bᵀ`` for the variance, and properties (the bound is above the exact tail, the
weights sum to 1 and do not change when every expert loses the same amount). They describe the expected behaviour
without showing the solution.

    pytest tests/test_m14_ensembles.py              # your code
    pytest tests/test_m14_ensembles.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings

import numpy as np
import pytest
from scipy.optimize import minimize_scalar
from scipy.special import rel_entr, softmax
from scipy.stats import binom


@pytest.fixture
def ens(mymath_module):
    return mymath_module("ensembles")


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


def _show(v):
    return np.array2string(np.asarray(v, dtype=float), precision=6, suppress_small=False).replace("\n", "")


def test_ensembles_uses_no_scipy(ens):
    """ensembles.py computes with NumPy and math only: the tests compare it with SciPy."""
    try:
        tree = ast.parse(inspect.getsource(ens))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(a.name for a in node.names if a.name.split(".")[0] in ("scipy", "sklearn"))
        elif isinstance(node, ast.ImportFrom) and node.module and node.module.split(".")[0] in ("scipy", "sklearn"):
            found.add(node.module)
    assert not found, (f"expected ensembles.py to use NumPy and math only, found imports of {sorted(found)}: the "
                       f"tests compare your results with SciPy, so write the computations yourself")


# ---------------------------------------------------------------- chernoff_bound
def _kl(a, p):
    """KL(a ‖ p) between Bernoulli laws, in nats (SciPy: 0 ln 0 = 0)."""
    return float(rel_entr(a, p) + rel_entr(1 - a, 1 - p))


def test_chernoff_docstring_examples(ens):
    got = _result(lambda: ens.chernoff_bound(10, 0.5, 0.8), "a bound", "n = 10, p = 0.5, a = 0.8")
    _python_float(got, "chernoff_bound(10, 0.5, 0.8)")
    expected = math.exp(-10 * _kl(0.8, 0.5))
    assert math.isclose(got, expected, rel_tol=1e-9), f"expected {expected!r} ≈ 0.1455 (exp(-10 KL(0.8 ‖ 0.5))), got {got!r}"
    got = _result(lambda: ens.chernoff_bound(10, 0.5, 0.4), "1.0", "a = 0.4 ≤ p = 0.5")
    assert got == 1.0 and type(got) is float, f"expected 1.0 (a ≤ p: the bound says nothing), got {got!r}"


@pytest.mark.parametrize("n, p, a", [(1, 0.3, 0.9), (7, 0.25, 0.6), (40, 0.55, 0.7), (250, 0.1, 0.13),
                                     (1000, 0.62, 0.65), (33, 0.05, 0.95)])
def test_chernoff_matches_the_divergence(ens, n, p, a):
    expected = math.exp(-n * _kl(a, p))
    got = _result(lambda: ens.chernoff_bound(n, p, a), "a bound", f"n = {n}, p = {p}, a = {a}")
    _python_float(got, "the bound")
    assert math.isclose(got, expected, rel_tol=1e-9, abs_tol=1e-300), (
        f"expected exp(-n KL(a ‖ p)) = {expected!r} for n = {n}, p = {p}, a = {a}, got {got!r}"
        + (" (KL(a ‖ p) = a ln(a/p) + (1 - a) ln((1 - a)/(1 - p)): check the order of a and p)"
           if math.isclose(got, math.exp(-n * _kl(p, a)), rel_tol=1e-9) else ""))


@pytest.mark.parametrize("n, p, a", [(12, 0.3, 0.5), (60, 0.45, 0.6), (200, 0.2, 0.26)])
def test_chernoff_is_the_best_markov_bound(ens, n, p, a):
    """The bound equals the smallest e^{-λna} (1 - p + p e^λ)^n over λ > 0."""
    log_bound = lambda lam: -lam * n * a + n * math.log(1 - p + p * math.exp(lam))   # noqa: E731
    best = minimize_scalar(log_bound, bounds=(1e-9, 20.0), method="bounded", options={"xatol": 1e-12})
    got = _result(lambda: ens.chernoff_bound(n, p, a), "a bound", f"n = {n}, p = {p}, a = {a}")
    assert math.isclose(got, math.exp(best.fun), rel_tol=1e-6), (
        f"expected {math.exp(best.fun)!r}, the smallest Markov bound e^(-λna) (1 - p + p e^λ)^n over λ > 0 "
        f"(n = {n}, p = {p}, a = {a}), got {got!r}")


def test_chernoff_is_above_the_exact_tail(ens):
    """P(X ≥ n a) ≤ exp(-n KL(a ‖ p)) for X ~ B(n, p), on a grid (scipy.stats.binom)."""
    for n in (5, 20, 80, 300):
        for p in (0.1, 0.35, 0.5, 0.8):
            for a in np.linspace(0.0, 1.0, 21):
                tail = float(binom.sf(math.ceil(n * a - 1e-12) - 1, n, p))
                got = _result(lambda: ens.chernoff_bound(n, p, float(a)), "a bound", f"n = {n}, p = {p}, a = {a}")
                assert got >= tail - 1e-12 and 0.0 <= got <= 1.0, (
                    f"expected a bound in [0, 1] above the exact tail P(X ≥ {n * a:g}) = {tail!r} for n = {n}, "
                    f"p = {p}, a = {a!r}, got {got!r}"
                    + (" (when a is extremely close to p, KL(a ‖ p) can round to a tiny negative number: keep the "
                       "bound at most 1)" if 1.0 < got < 1.0 + 1e-9 else ""))


def test_chernoff_edge_cases(ens):
    cases = [((0, 0.3, 0.9), 1.0, "n = 0: exp(0)"),
             ((15, 0.0, 0.2), 0.0, "p = 0 and a > 0: the event is impossible"),
             ((15, 0.0, 0.0), 1.0, "a = p = 0: a ≤ p, the bound says nothing"),
             ((15, 1.0, 1.0), 1.0, "a = p = 1: a ≤ p"),
             ((9, 0.6, 0.6), 1.0, "a = p: the bound says nothing")]
    for args, expected, why in cases:
        got = _result(lambda: ens.chernoff_bound(*args), repr(expected), f"chernoff_bound{args}")
        assert got == expected, f"expected {expected!r} for chernoff_bound{args} ({why}), got {got!r}"
    got = _result(lambda: ens.chernoff_bound(6, 0.4, 1.0), "0.4 ** 6", "a = 1",
                  "with a = 1, the term (1 - a) ln((1 - a)/(1 - p)) is 0 ln 0 = 0")
    assert math.isclose(got, 0.4 ** 6, rel_tol=1e-12), (
        f"expected 0.4^6 = {0.4 ** 6!r} for a = 1 (KL(1 ‖ p) = ln(1/p), and 0 ln 0 counts as 0), got {got!r}")


def test_chernoff_accepts_numpy_numbers(ens):
    got = _result(lambda: ens.chernoff_bound(np.int64(10), np.float64(0.5), np.float64(0.8)), "a bound",
                  "NumPy numbers")
    _python_float(got, "the bound")
    assert math.isclose(got, math.exp(-10 * _kl(0.8, 0.5)), rel_tol=1e-9), (
        f"expected ≈ 0.1455 with NumPy numbers, got {got!r}")


@pytest.mark.parametrize("args, why", [((-1, 0.5, 0.8), "n < 0"), ((2.5, 0.5, 0.8), "n is not an integer"),
                                       ((True, 0.5, 0.8), "n is a bool, not a number of trials"),
                                       ((10, 1.5, 0.8), "p > 1"), ((10, -0.1, 0.8), "p < 0"),
                                       ((10, 0.5, 1.2), "a > 1"), ((10, float("nan"), 0.8), "p is NaN"),
                                       ((10, 0.5, float("nan")), "a is NaN")])
def test_chernoff_refuses_bad_arguments(ens, args, why):
    _expect_value_error(lambda: ens.chernoff_bound(*args), f"chernoff_bound{args}", why)


# ---------------------------------------------------------------- variance_of_average
def test_variance_docstring_examples(ens):
    for args, kwargs, expected in [(([[4, 0], [0, 4]],), {}, 2.0), (([[4, 4], [4, 4]],), {}, 4.0),
                                   (([[1, 0], [0, 9]],), {"weights": [0.9, 0.1]}, 0.9)]:
        got = _result(lambda: ens.variance_of_average(*args, **kwargs), repr(expected), f"{args[0]}, {kwargs}")
        _python_float(got, "the variance")
        assert math.isclose(got, expected, rel_tol=1e-12), (
            f"expected {expected} for cov = {args[0]}{', ' + str(kwargs) if kwargs else ''}, got {got!r}")


@pytest.mark.parametrize("m, seed", [(1, 4310), (2, 4311), (5, 4312), (12, 4313)])
def test_variance_matches_a_factorization(ens, m, seed):
    """With cov = B Bᵀ and X = B Z (Z of independent unit variables), Σ w_i X_i = (Bᵀ w) · Z: variance ‖Bᵀ w‖²."""
    rng = np.random.default_rng(seed)
    B = rng.normal(size=(m, m + 2))
    cov = B @ B.T
    w = rng.dirichlet(np.ones(m))
    expected = float(np.sum((B.T @ w) ** 2))
    got = _result(lambda: ens.variance_of_average(cov, weights=w), "a variance", f"M = {m}")
    _python_float(got, "the variance")
    diagonal_only = float(np.sum(w ** 2 * np.diag(cov)))
    assert math.isclose(got, expected, rel_tol=1e-9), (
        f"expected wᵀ cov w = {expected!r} for M = {m}, got {got!r}"
        + (" (the covariances count too: Σ_i Σ_j w_i w_j cov[i, j], not only the diagonal)"
           if m > 1 and math.isclose(got, diagonal_only, rel_tol=1e-9) else ""))


def test_variance_default_weights_are_uniform(ens):
    rng = np.random.default_rng(4314)
    B = rng.normal(size=(6, 6))
    cov = B @ B.T
    expected = float(np.ones(6) @ cov @ np.ones(6)) / 36
    got = _result(lambda: ens.variance_of_average(cov), "a variance", "no weights")
    assert math.isclose(got, expected, rel_tol=1e-9), (
        f"expected {expected!r} with the default weights 1/M (here 1/6 each), got {got!r}"
        + (" (that is the sum of the matrix: divide by M², the weights are 1/M)"
           if math.isclose(got, expected * 36, rel_tol=1e-9) else ""))


def test_variance_accepts_rounding_noise(ens):
    cov = np.array([[2.0, 0.5], [0.5 + 1e-15, 3.0]])     # symmetric up to rounding
    w = [0.3, 0.7 + 1e-12]                                # sum 1 up to rounding
    got = _result(lambda: ens.variance_of_average(cov, weights=w), "a variance",
                  "a matrix symmetric within 1e-15 and weights of sum 1 + 1e-12")
    expected = 0.09 * 2.0 + 2 * 0.21 * 0.5 + 0.49 * 3.0
    assert abs(got - expected) < 1e-9, (
        f"expected ≈ {expected} (symmetric and of sum 1 within the tolerances of the docstring), got {got!r}")
    singular = np.array([[1.0, -1.0], [-1.0, 1.0]])           # X₂ = -X₁: their mean is 0
    got = _result(lambda: ens.variance_of_average(singular), "0 (or a rounding of it)", "X₂ = -X₁")
    assert abs(got) < 1e-12, f"expected 0 for the mean of X and -X, got {got!r}"


def test_variance_leaves_its_inputs(ens):
    cov, w = np.array([[2.0, 1.0], [1.0, 2.0]]), np.array([0.25, 0.75])
    copies = (cov.copy(), w.copy())
    _result(lambda: ens.variance_of_average(cov, weights=w), "a variance")
    assert np.array_equal(cov, copies[0]) and np.array_equal(w, copies[1]), (
        "expected cov and weights unchanged after the call, got them modified")


@pytest.mark.parametrize("cov, weights, why", [
    ([[1, 2, 3], [2, 1, 0]], None, "cov is not square"),
    ([1, 2, 3], None, "cov is not 2-D"),
    ([[2, 1], [0, 2]], None, "cov is not symmetric"),
    ([[2, 1], [1, 2]], [0.5, 0.3, 0.2], "3 weights for 2 variables"),
    ([[2, 1], [1, 2]], [1.2, -0.2], "a negative weight"),
    ([[2, 1], [1, 2]], [0.5, 0.6], "weights of sum 1.1"),
    ([[1, -3], [-3, 1]], None, "a negative variance: not a covariance matrix")])
def test_variance_refuses_bad_arguments(ens, cov, weights, why):
    _expect_value_error(lambda: ens.variance_of_average(cov, weights=weights),
                        f"variance_of_average({cov}, weights={weights})", why)


# ---------------------------------------------------------------- hedge_weights
def test_hedge_docstring_example(ens):
    got = _result(lambda: ens.hedge_weights([[0, 1], [0, 1]], eta=math.log(2)), "the (3, 2) weights")
    assert isinstance(got, np.ndarray) and got.shape == (3, 2) and got.dtype.kind == "f", (
        f"expected a numpy.ndarray of floats of shape (3, 2), got {type(got).__name__} "
        f"{getattr(got, 'shape', '')}")
    expected = [[0.5, 0.5], [2 / 3, 1 / 3], [0.8, 0.2]]
    assert np.allclose(got, expected, atol=1e-12), (
        f"expected {_show(expected)} (row t: before round t; row 0 uniform), got {_show(got)}"
        + (" (the first row is before any loss: it must be uniform)" if np.allclose(got[:2], expected[1:]) else ""))


@pytest.mark.parametrize("T, K, eta, seed", [(1, 3, 0.5, 4320), (10, 4, 0.2, 4321), (60, 7, 1.3, 4322),
                                             (200, 2, 0.05, 4323)])
def test_hedge_matches_a_softmax(ens, T, K, eta, seed):
    losses = np.random.default_rng(seed).uniform(0, 1, size=(T, K))
    cumulative = np.vstack([np.zeros(K), np.cumsum(losses, axis=0)])
    expected = softmax(-eta * cumulative, axis=1)
    got = _result(lambda: ens.hedge_weights(losses, eta), f"the ({T + 1}, {K}) weights", f"T = {T}, K = {K}")
    assert isinstance(got, np.ndarray) and got.shape == (T + 1, K), (
        f"expected an array of shape ({T + 1}, {K}) (one row before each round and one after the last), got "
        f"{type(got).__name__} of shape {getattr(got, 'shape', None)}")
    hint = ""
    if np.allclose(got, softmax(eta * cumulative, axis=1), atol=1e-12):
        hint = " (the weight is exp(-eta L): a large loss gives a SMALL weight)"
    elif np.allclose(got[1:], softmax(-eta * losses, axis=1), atol=1e-12):
        hint = " (each weight uses the cumulative loss of all the rounds before, not the loss of one round)"
    assert np.allclose(got, expected, atol=1e-12), (
        f"expected the rows exp(-eta L_t) normalized, first rows {_show(expected[:2])}, got {_show(got[:2])}{hint}")


def test_hedge_survives_large_losses(ens):
    losses = np.full((6, 3), 1000.0)
    losses[:, 1] = 990.0                     # expert 1 loses a little less at each round
    got = _result(lambda: ens.hedge_weights(losses, 1.0), "finite weights", "losses of about 1000 per round",
                  "subtract the smallest cumulative loss of each row before the exponential")
    assert np.all(np.isfinite(got)) and np.allclose(got.sum(axis=1), 1.0), (
        f"expected finite weights, each row of sum 1, even for losses of 1000 per round, got {_show(got[-2:])} "
        + ("(subtract the smallest cumulative loss of each row before the exponential)"
           if not np.all(np.isfinite(got)) else
           f"(rows of sum {_show(got.sum(axis=1)[-2:])}: normalize each row, w / w.sum(axis=1, keepdims=True))"))
    assert got[-1, 1] > 1 - 1e-12 and np.allclose(got[0], 1 / 3), (
        f"expected uniform weights before round 1 and nearly all the weight on expert 1 at the end, got "
        f"{_show(got[0])} and {_show(got[-1])}")


def test_hedge_ignores_a_loss_shared_by_every_expert(ens):
    rng = np.random.default_rng(4324)
    losses = rng.uniform(0, 1, size=(8, 4))
    shifted = losses + rng.uniform(0, 5, size=(8, 1))      # the same extra loss for every expert at each round
    a = _result(lambda: ens.hedge_weights(losses, 0.7), "the weights")
    b = _result(lambda: ens.hedge_weights(shifted, 0.7), "the weights", "every expert losing the same extra amount")
    assert np.allclose(a, b, atol=1e-12), (
        f"expected the same weights when every expert loses the same extra amount at a round, got "
        f"{_show(a[-1])} and {_show(b[-1])} (the normalization cancels a common factor)")


def test_hedge_with_no_round_and_integer_losses(ens):
    got = _result(lambda: ens.hedge_weights(np.zeros((0, 4)), 0.3), "one uniform row", "T = 0 rounds")
    assert isinstance(got, np.ndarray) and got.shape == (1, 4) and np.allclose(got, 0.25), (
        f"expected [[0.25, 0.25, 0.25, 0.25]] for no round (only the row before any loss), got {got!r}")
    got = _result(lambda: ens.hedge_weights([[1, 0, 2]], 1), "a (2, 3) array of floats", "integer losses")
    assert got.dtype.kind == "f" and np.allclose(got[1], softmax(-np.array([1.0, 0.0, 2.0]))), (
        f"expected floats {_show(softmax(-np.array([1.0, 0.0, 2.0])))} after the round, got {got!r}")


def test_hedge_leaves_its_inputs(ens):
    losses = np.array([[0.2, 0.9], [0.5, 0.1]])
    copy = losses.copy()
    _result(lambda: ens.hedge_weights(losses, 0.4), "the weights")
    assert np.array_equal(losses, copy), "expected losses unchanged after the call, got them modified"


@pytest.mark.parametrize("losses, eta, why", [([0.1, 0.2], 1.0, "losses is not 2-D"),
                                              (np.zeros((3, 0)), 1.0, "no expert (no column)"),
                                              ([[0.1, 0.2]], 0.0, "eta = 0"), ([[0.1, 0.2]], -0.5, "eta < 0"),
                                              ([[0.1, 0.2]], float("nan"), "eta is NaN")])
def test_hedge_refuses_bad_arguments(ens, losses, eta, why):
    _expect_value_error(lambda: ens.hedge_weights(losses, eta), f"hedge_weights({losses!r}, {eta!r})", why)
