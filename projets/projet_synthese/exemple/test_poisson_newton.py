"""Tests of the worked example (PS.7): python -m pytest -q test_poisson_newton.py --impl=ref

The fixture ``algo`` is the module poisson_newton.py (conftest.py, the kit's one, copied); the tests call
``algo.<function>(...)`` so that ``--mutant=<name>`` (mutants.py) reaches them. The oracles are independent of the
module and of mymath, and no formula of the notebook's §3 is copied here:

* scikit-learn ``PoissonRegressor`` (another solver, another objective: the mean half deviance, same maximum) and
  ``scipy.optimize.minimize`` (BFGS on minus the log-likelihood, its gradient by SciPy's own differences);
* the log-likelihood written with ``scipy.stats.poisson.logpmf``, and its derivatives by centred finite differences
  written below (M05a §5 and §7, M19 §1); ``numpy.linalg`` for eigenvalues, inverses and linear systems;
* ``fractions.Fraction`` and ``math`` for the example computed by hand in §5.

Random cases: three sizes (n, p) and three seeds (9010 to 9012), the column of ones first in X; the other seeds of
the file are 9020 to 9049. Each failure message says on its first line what was expected.
"""

from __future__ import annotations

import math
import warnings
from fractions import Fraction

import numpy as np
import pytest
from scipy.optimize import minimize
from scipy.stats import poisson
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import PoissonRegressor

SEEDS = [9010, 9011, 9012]
SIZES = [(20, 2), (100, 3), (500, 5)]          # (n, p): n examples, p columns of X (the column of ones included)
SIZE_IDS = [f"n={n},p={p}" for n, p in SIZES]
SEED_IDS = [f"seed={seed}" for seed in SEEDS]

# The example of §5: x = deviation of the evening temperature from the seasonal norm (°C), y = mosquito bites.
HAND_X = np.column_stack([np.ones(5), [-1.0, 0.0, 1.0, 2.0, 3.0]])
HAND_Y = np.array([0.0, 1.0, 2.0, 4.0, 5.0])


def make_data(n: int, p: int, seed: int):
    """A random case: X = [1, features drawn from N(0, 1)], counts drawn from the model with weights w_true."""
    rng = np.random.default_rng(seed)
    X = np.column_stack([np.ones(n), rng.normal(size=(n, p - 1))])
    w_true = np.concatenate([[0.8], rng.uniform(-0.5, 0.5, size=p - 1)])
    y = rng.poisson(np.exp(X @ w_true)).astype(float)
    return X, y, w_true


def oracle_log_likelihood(w, X, y) -> float:
    """The log-likelihood of the counts, from SciPy's Poisson law (not from the formula of §3)."""
    return float(np.sum(poisson.logpmf(y, np.exp(X @ np.asarray(w, dtype=float)))))


def centred_gradient(f, w, h: float):
    """Centred differences (f(w + h e_j) - f(w - h e_j)) / (2 h), coordinate by coordinate (M05a §5)."""
    w = np.asarray(w, dtype=float)
    basis = np.eye(w.size)
    return np.array([(f(w + h * e) - f(w - h * e)) / (2 * h) for e in basis])


def centred_hessian(f, w, h: float):
    """Second centred differences: the two formulas of M19 §1 (diagonal and crossed), mirrored."""
    w = np.asarray(w, dtype=float)
    basis = np.eye(w.size)
    H = np.empty((w.size, w.size))
    f0 = f(w)
    for i, ei in enumerate(basis):
        H[i, i] = (f(w + h * ei) - 2 * f0 + f(w - h * ei)) / h ** 2
        for j in range(i + 1, w.size):
            ej = basis[j]
            H[i, j] = H[j, i] = (f(w + h * ei + h * ej) - f(w + h * ei - h * ej) - f(w - h * ei + h * ej)
                                 + f(w - h * ei - h * ej)) / (4 * h ** 2)
    return H


def assert_close(got, expected, *, rtol: float, atol: float, what: str) -> None:
    """Compare two arrays; the first line of the failure says what was expected (the kit's helper, with the
    numbers printed as plain floats)."""
    got = np.asarray(got, dtype=float)
    expected = np.asarray(expected, dtype=float)
    assert got.shape == expected.shape, f"{what}: expected shape {expected.shape}, got {got.shape}"
    gap = np.abs(got - expected)
    bad = gap > atol + rtol * np.abs(expected)
    if np.any(bad) or not np.all(np.isfinite(got)):
        index = tuple(int(i) for i in np.unravel_index(int(np.argmax(np.where(np.isfinite(gap), gap, np.inf))),
                                                        gap.shape))
        raise AssertionError(f"{what}: expected {float(expected[index]):.10g} at index {index} (rtol={rtol:g}, "
                             f"atol={atol:.3g}), got {float(got[index]):.10g}; {int(np.sum(bad))} value(s) out of "
                             "tolerance")


def sklearn_weights(X, y):
    """scikit-learn's maximum likelihood weights. Settings: alpha=0 (no penalty), fit_intercept=False (the column
    of ones is in X), solver="newton-cholesky", tol=1e-9 on the gradient of its mean objective (at 1e-10 its line
    search gives up at rounding level on one case of the file, with a ConvergenceWarning), max_iter=1000."""
    model = PoissonRegressor(alpha=0.0, fit_intercept=False, solver="newton-cholesky", tol=1e-9, max_iter=1000)
    with warnings.catch_warnings():
        warnings.simplefilter("error", ConvergenceWarning)      # an oracle that did not converge is no oracle
        return model.fit(X, y).coef_


# ---------------------------------------------------------------------------------------------------------------
# The fit against two libraries (Eq. (3.5))
# ---------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("seed", SEEDS, ids=SEED_IDS)
@pytest.mark.parametrize("size", SIZES, ids=SIZE_IDS)
def test_fit_matches_sklearn(algo, size, seed):
    """fit gives scikit-learn's weights. Tolerance 1e-7 relative, 1e-8 absolute: scikit-learn stops when the
    gradient of its mean objective is below 1e-9, i.e. a gradient of l below 1e-9 n, hence an error on w of about
    1e-9 n / lambda_min(X^T W X), below 1e-9 in our cases (5e-10 measured); our fit is exact to rounding."""
    X, y, _ = make_data(*size, seed)
    assert_close(algo.fit(X, y).w, sklearn_weights(X, y), rtol=1e-7, atol=1e-8,
                 what="w of fit against PoissonRegressor")


@pytest.mark.parametrize("seed", SEEDS, ids=SEED_IDS)
@pytest.mark.parametrize("size", SIZES, ids=SIZE_IDS)
def test_fit_matches_scipy_minimize(algo, size, seed):
    """fit gives the minimizer of minus the log-likelihood found by SciPy's BFGS (gradient by SciPy's 3-point
    differences, gtol = 1e-6 n on a sum of n terms): an error on w of at most about gtol / lambda_min ~ 1e-6, hence
    the absolute tolerance 5e-6."""
    X, y, _ = make_data(*size, seed)
    n, p = X.shape
    result = minimize(lambda w: -oracle_log_likelihood(w, X, y), np.zeros(p), method="BFGS", jac="3-point",
                      options={"gtol": 1e-6 * n})
    assert result.success, f"expected SciPy's BFGS to converge (the oracle), got: {result.message}"
    assert_close(algo.fit(X, y).w, result.x, rtol=0.0, atol=5e-6, what="w of fit against scipy.optimize.minimize")


def test_fit_matches_sklearn_on_the_hand_example(algo):
    """The five evenings of §5: the maximum reached from the hand-computed first step is scikit-learn's."""
    assert_close(algo.fit(HAND_X, HAND_Y).w, sklearn_weights(HAND_X, HAND_Y), rtol=1e-7, atol=1e-8,
                 what="w of fit on the example of §5")


# ---------------------------------------------------------------------------------------------------------------
# The formulas of §3 against the log-likelihood of SciPy and finite differences
# ---------------------------------------------------------------------------------------------------------------
def random_point(seed: int, size):
    """A random case and a random point w near its true weights (fitted means of a reasonable size)."""
    X, y, w_true = make_data(*size, seed)
    w = w_true + np.random.default_rng(seed + 1000).normal(scale=0.1, size=w_true.size)
    return X, y, w


@pytest.mark.parametrize("seed", SEEDS, ids=SEED_IDS)
@pytest.mark.parametrize("size", SIZES, ids=SIZE_IDS)
def test_log_likelihood_matches_scipy(algo, size, seed):
    """log_likelihood (Eq. (3.1)) equals the sum of scipy.stats.poisson.logpmf, to rounding: 1e-11 (1 + |l|), the
    rounding of a sum of n terms of size |l| / n."""
    X, y, w = random_point(seed, size)
    expected = oracle_log_likelihood(w, X, y)
    assert_close(algo.log_likelihood(w, X, y), expected, rtol=1e-11, atol=1e-11,
                 what="log_likelihood against scipy.stats.poisson.logpmf")


@pytest.mark.parametrize("seed", SEEDS, ids=SEED_IDS)
@pytest.mark.parametrize("size", SIZES, ids=SIZE_IDS)
def test_gradient_matches_centred_differences(algo, size, seed):
    """gradient (Eq. (3.2)) against centred differences of SciPy's log-likelihood, step h = 1e-5.

    Step: the error of a centred difference is about h² |l'''| / 6 + eps |l| / h (M05a §5 and §7); with |l| and
    |l'''| of order n (at most 1e3 here), it is smallest near h = 1e-5 and stays below 1e-6 there. Tolerance:
    1e-6 absolute plus 1e-7 relative, ten times the error measured on these cases."""
    X, y, w = random_point(seed, size)
    expected = centred_gradient(lambda v: oracle_log_likelihood(v, X, y), w, h=1e-5)
    assert_close(algo.gradient(w, X, y), expected, rtol=1e-7, atol=1e-6, what="gradient against centred differences")


@pytest.mark.parametrize("seed", SEEDS, ids=SEED_IDS)
@pytest.mark.parametrize("size", SIZES, ids=SIZE_IDS)
def test_hessian_matches_centred_differences(algo, size, seed):
    """hessian (Eq. (3.3)) against second centred differences of SciPy's log-likelihood, step h = 1e-4.

    Step: dividing by h² amplifies the rounding of l to eps |l| / h², hence a larger step than for a gradient
    (M19 §1: h ~ eps^(1/4) ~ 1e-4); the error measured is below 3e-5 here. Tolerance: 1e-4 absolute plus 1e-6
    relative to the largest entry."""
    X, y, w = random_point(seed, size)
    expected = centred_hessian(lambda v: oracle_log_likelihood(v, X, y), w, h=1e-4)
    got = algo.hessian(w, X)
    assert_close(got, expected, rtol=0.0, atol=1e-4 + 1e-6 * np.max(np.abs(expected)),
                 what="hessian against second centred differences")


@pytest.mark.parametrize("seed", SEEDS, ids=SEED_IDS)
@pytest.mark.parametrize("size", SIZES, ids=SIZE_IDS)
def test_newton_direction_matches_finite_differences(algo, size, seed):
    """newton_direction (Eq. (3.4) computed as (3.6)) is Newton's direction, the solution of H delta = -grad l,
    with H and grad l by finite differences of SciPy's log-likelihood and the system solved by numpy.linalg.solve.
    Tolerance 1e-6 (1 + |delta|): the errors of the differences (relative 1e-8), times kappa(H) < 1e2."""
    X, y, w = random_point(seed, size)
    oracle = lambda v: oracle_log_likelihood(v, X, y)                          # noqa: E731
    expected = np.linalg.solve(centred_hessian(oracle, w, h=1e-4), -centred_gradient(oracle, w, h=1e-5))
    assert_close(algo.newton_direction(w, X, y), expected, rtol=0.0, atol=1e-6 * (1 + np.max(np.abs(expected))),
                 what="newton_direction against -H^{-1} grad l by finite differences")


@pytest.mark.parametrize("seed", SEEDS, ids=SEED_IDS)
def test_standard_errors_match_the_inverse_hessian(algo, seed):
    """standard_errors (Eq. (3.9)) at the maximum: the square roots of the diagonal of the inverse of minus the
    Hessian by finite differences (numpy.linalg.inv). Tolerance 1e-5 relative: the relative error of the differences."""
    X, y, _ = make_data(100, 3, seed)
    w = sklearn_weights(X, y)
    information = -centred_hessian(lambda v: oracle_log_likelihood(v, X, y), w, h=1e-4)
    expected = np.sqrt(np.diag(np.linalg.inv(information)))
    assert_close(algo.standard_errors(w, X), expected, rtol=1e-5, atol=0.0,
                 what="standard_errors against the inverse of the Hessian by finite differences")


@pytest.mark.parametrize("seed", SEEDS, ids=SEED_IDS)
def test_critical_learning_rate_matches_the_eigenvalues(algo, seed):
    """critical_learning_rate (Eq. (3.12)) is 2 / the largest eigenvalue of minus the Hessian by finite differences
    (numpy.linalg.eigvalsh). Tolerance 1e-6 relative."""
    X, y, w = random_point(seed, (100, 3))
    eigenvalues = np.linalg.eigvalsh(-centred_hessian(lambda v: oracle_log_likelihood(v, X, y), w, h=1e-4))
    assert_close(algo.critical_learning_rate(w, X), 2.0 / eigenvalues[-1], rtol=1e-6, atol=0.0,
                 what="critical_learning_rate against 2 / lambda_max")


def test_gradient_ascent_takes_gradient_steps_and_reaches_the_maximum(algo):
    """gradient_ascent (Eq. (3.11)): its first step is w0 + eta grad l (gradient by centred differences), and with
    eta = 1 / lambda_max at the maximum it ends at scikit-learn's weights (tolerance 1e-8 after 3000 steps: the
    error is multiplied by about 1 - 1 / kappa < 0.97 per step, M19 §5)."""
    X, y, _ = make_data(100, 3, 9020)
    target = sklearn_weights(X, y)
    eigenvalues = np.linalg.eigvalsh(-centred_hessian(lambda v: oracle_log_likelihood(v, X, y), target, h=1e-4))
    eta = 1.0 / eigenvalues[-1]
    iterates = algo.gradient_ascent(X, y, eta, 3000)
    assert iterates.shape == (3001, 3), f"expected iterates of shape (3001, 3), got {iterates.shape}"
    first = eta * centred_gradient(lambda v: oracle_log_likelihood(v, X, y), np.zeros(3), h=1e-5)
    assert_close(iterates[1], first, rtol=1e-7, atol=1e-9, what="first step of gradient_ascent")
    assert_close(iterates[-1], target, rtol=0.0, atol=1e-8, what="last iterate of gradient_ascent")


# ---------------------------------------------------------------------------------------------------------------
# Properties of §4
# ---------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("seed", SEEDS, ids=SEED_IDS)
@pytest.mark.parametrize("size", SIZES, ids=SIZE_IDS)
def test_fitted_means_sum_to_the_counts(algo, size, seed):
    """Property 2 (§4): with a column of ones, the fitted means add up to the counts, to 1e-9 relative."""
    X, y, _ = make_data(*size, seed)
    w = algo.fit(X, y).w
    fitted = np.exp(X @ w)
    assert_close(fitted.sum(), y.sum(), rtol=1e-9, atol=0.0, what="sum of the fitted means exp(X w)")


@pytest.mark.parametrize("seed", SEEDS, ids=SEED_IDS)
@pytest.mark.parametrize("size", SIZES, ids=SIZE_IDS)
def test_fit_is_a_critical_point_by_finite_differences(algo, size, seed):
    """The returned w is a critical point of SciPy's log-likelihood: its centred-difference gradient is 0 up to the
    error of the differences (1e-6, see test_gradient_matches_centred_differences)."""
    X, y, _ = make_data(*size, seed)
    w = algo.fit(X, y).w
    slope = centred_gradient(lambda v: oracle_log_likelihood(v, X, y), w, h=1e-5)
    assert_close(slope, np.zeros_like(w), rtol=0.0, atol=1e-6, what="gradient at the returned w (finite differences)")


@pytest.mark.parametrize("seed", [9021, 9022, 9023], ids=["seed=9021", "seed=9022", "seed=9023"])
def test_fit_finds_the_same_maximum_from_random_starts(algo, seed):
    """Property 1 (§4): the maximum is unique, so three random starts end at the same weights (1e-9)."""
    X, y, _ = make_data(200, 4, seed)
    rng = np.random.default_rng(seed + 1000)
    results = [algo.fit(X, y, w0=rng.uniform(-1.0, 1.0, size=4)).w for _ in range(3)]
    for other in results[1:]:
        assert_close(other, results[0], rtol=0.0, atol=1e-9, what="w of fit from another random start")


@pytest.mark.parametrize("seed", SEEDS, ids=SEED_IDS)
def test_hessian_is_negative_definite(algo, seed):
    """Property 1 (§4): under H2 the Hessian is negative definite: its largest eigenvalue (numpy.linalg.eigvalsh)
    is negative, at random points."""
    X, y, w = random_point(seed, (100, 3))
    largest = np.linalg.eigvalsh(algo.hessian(w, X))[-1]
    assert largest < 0, f"expected a negative definite Hessian (largest eigenvalue < 0), got {largest}"


@pytest.mark.parametrize("shift", [-2.5, 4.0], ids=["shift=-2.5", "shift=4"])
def test_shifting_a_feature_changes_only_the_intercept(algo, shift):
    """An invariance: x_j -> x_j + c is the reparametrization w_0 -> w_0 - c w_j, so the fitted means and the other
    weights do not change, and the intercept moves by -c w_j (tolerance 1e-9)."""
    X, y, _ = make_data(150, 3, 9024)
    shifted = X.copy()
    shifted[:, 1] += shift
    w, v = algo.fit(X, y).w, algo.fit(shifted, y).w
    assert_close(v[1:], w[1:], rtol=0.0, atol=1e-9, what="weights of the features after the shift")
    assert_close(v[0], w[0] - shift * w[1], rtol=0.0, atol=1e-9, what="intercept after the shift")
    assert_close(np.exp(shifted @ v), np.exp(X @ w), rtol=1e-9, atol=0.0, what="fitted means after the shift")


# ---------------------------------------------------------------------------------------------------------------
# The example of §5, exactly
# ---------------------------------------------------------------------------------------------------------------
def test_hand_example_first_direction_is_least_squares_of_y_minus_1(algo):
    """From w = 0, Newton's direction is (1/10, 13/10) (§5, Eq. (3.8)): tolerance 1e-12, the rounding of a QR in
    float64 (about 1e-16 times the condition number of X, 2.4, times the size of the numbers)."""
    expected = [Fraction(1, 10), Fraction(13, 10)]
    got = algo.newton_direction(np.zeros(2), HAND_X, HAND_Y)
    gaps = [abs(Fraction(float(g)) - e) for g, e in zip(got, expected)]
    assert max(gaps) <= Fraction(1, 10 ** 12), f"expected the direction (1/10, 13/10), got {got.tolist()}"


def test_hand_example_full_step_is_refused_and_half_step_taken(algo):
    """§5: the full step lowers l, the half step (1/20, 13/20) raises it; fit takes t = 1/2 at its first iteration."""
    result = algo.fit(HAND_X, HAND_Y)
    assert result.step_sizes[0] == 0.5, f"expected a first step halved once (t = 1/2), got t = {result.step_sizes[0]}"
    assert_close(result.history[1], [1 / 20, 13 / 20], rtol=0.0, atol=1e-12, what="first iterate w_1 of fit")
    start, full = oracle_log_likelihood([0, 0], HAND_X, HAND_Y), oracle_log_likelihood([0.1, 1.3], HAND_X, HAND_Y)
    assert full < start, f"expected l(1/10, 13/10) < l(0) (the full step refused), got {full} and {start}"


def test_hand_example_log_likelihood_at_zero(algo):
    """§5: l(0) = -5 - ln(0! 1! 2! 4! 5!), with math.factorial and math.log, to 1e-12."""
    expected = -5 - math.log(math.prod(math.factorial(int(v)) for v in HAND_Y))
    assert_close(algo.log_likelihood(np.zeros(2), HAND_X, HAND_Y), expected, rtol=0.0, atol=1e-12,
                 what="l(0) on the example of §5")


@pytest.mark.parametrize("counts", [[0, 1, 2, 4, 5], [2, 7, 1], [0, 0, 1, 0, 3]], ids=["mean=12/5", "mean=10/3",
                                                                                        "mean=4/5"])
def test_intercept_only_is_the_log_of_the_mean(algo, counts):
    """intercept_only (Eq. (3.10)) returns ln(mean(y)) (math.log), to 1e-12."""
    expected = math.log(sum(counts) / len(counts))
    assert_close(algo.intercept_only(counts), expected, rtol=0.0, atol=1e-12, what="intercept_only")


# ---------------------------------------------------------------------------------------------------------------
# Invalid inputs and the case without maximum (§4, Theorem 3)
# ---------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("y, message", [([0, -2, 3, 1, 0], "counts >= 0"), ([0, 2.5, 3, 1, 0], "integer counts"),
                                        ([1, 2, 3], "length 5"), ([0, np.nan, 3, 1, 0], "finite")],
                         ids=["negative", "not an integer", "wrong length", "nan"])
def test_check_data_rejects_invalid_counts(algo, y, message):
    """check_data raises ValueError, with a message that says what was expected, for counts outside H1."""
    with pytest.raises(ValueError, match=message):
        algo.check_data(HAND_X, y)


def test_check_data_rejects_dependent_columns(algo):
    """check_data raises ValueError when H2 fails: a column that is twice another one, or more columns than rows."""
    X = np.column_stack([HAND_X, 2 * HAND_X[:, 1]])
    with pytest.raises(ValueError, match="linearly independent"):
        algo.check_data(X, HAND_Y)
    with pytest.raises(ValueError, match="more columns"):
        algo.check_data(np.ones((2, 3)), [1, 2])


def test_fit_raises_no_maximum_for_a_group_of_zeros(algo):
    """Theorem 3 (§4): six evenings with a mosquito net (x = 1), no bite: no maximum. fit raises NoMaximumError, the
    iterates run away along d = (0, -1) (the weight of the net goes down by about 1 per step) and l increases."""
    X = np.column_stack([np.ones(12), [0] * 6 + [1] * 6])
    y = np.array([2, 0, 3, 1, 4, 1] + [0] * 6)
    with pytest.raises(algo.NoMaximumError) as caught:
        algo.fit(X, y)
    history = np.array(caught.value.history)
    assert history[-1, 1] < -20, f"expected the weight of the net below -20 when the error is raised, got {history[-1]}"
    values = np.array(caught.value.log_likelihoods)
    assert np.all(np.diff(values) >= -1e-9), "expected a non-decreasing log-likelihood along the iterates"


def test_fit_raises_no_maximum_when_all_counts_are_zero(algo):
    """Theorem 3 (§4): all counts 0 with a column of ones, no maximum: NoMaximumError (after max_iter steps)."""
    X, _, _ = make_data(30, 2, 9025)
    with pytest.raises(algo.NoMaximumError, match="expected a maximum"):
        algo.fit(X, np.zeros(30), max_iter=40)


def test_intercept_only_raises_no_maximum_when_all_counts_are_zero(algo):
    """Eq. (3.10) has no solution when mean(y) = 0: intercept_only raises NoMaximumError."""
    with pytest.raises(algo.NoMaximumError):
        algo.intercept_only([0, 0, 0])
