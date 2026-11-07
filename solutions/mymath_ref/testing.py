"""Statistical tests: exact binomial test, permutation test, intervals, Bonferroni, AIC and BIC (chapter M08).

Reference implementation (solutions/mymath_ref).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m08_testing.py``.
NumPy is allowed, and so are the quantile functions ``statistics.NormalDist().inv_cdf`` and ``scipy.stats.t.ppf``;
the other tools of ``scipy.stats`` (``binomtest``, ``permutation_test``, ``ttest_rel``…) are not: the tests compare
your results with them. Randomness comes from one generator ``numpy.random.default_rng(seed)``, used in the order the
docstring gives, so that the same seed gives the same p-value. Every number returned is a Python ``float``.
"""

import math
import statistics

import numpy as np
from scipy.stats import t as student


def _check_binomial(k, n, p):
    """(k, n, p) after the checks shared by binomial_test and proportion_ci (ValueError when out of range)."""
    if isinstance(n, bool) or int(n) != n or n < 1:
        raise ValueError(f"n must be an integer at least 1, got {n!r}")
    if isinstance(k, bool) or int(k) != k or not 0 <= k <= n:
        raise ValueError(f"k must be an integer between 0 and n = {n}, got {k!r}")
    if not 0 < p < 1:
        raise ValueError(f"p must be strictly between 0 and 1, got {p!r}")
    return int(k), int(n), float(p)


def _binomial_pmf(j, n, p):
    """P(K = j) for K ~ B(n, p): with math.comb up to n = 1000, with logarithms beyond (no float overflow)."""
    if n <= 1000:
        return float(math.comb(n, j)) * p ** j * (1 - p) ** (n - j)
    log_pmf = (math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1)
               + j * math.log(p) + (n - j) * math.log1p(-p))
    return math.exp(log_pmf)


def _sample(x, what):
    """x as a 1-D array of floats with at least one value (ValueError otherwise)."""
    arr = np.array(x, dtype=float)
    if arr.ndim != 1 or arr.size == 0:
        raise ValueError(f"{what} must be a non-empty 1-D sample, got shape {arr.shape}")
    return arr


def binomial_test(k, n, p=0.5, alternative="two-sided"):
    """Return the exact p-value of the binomial test of ``H0 : the probability of success is p``.

    ``K`` follows the binomial law B(n, p) under H0, and ``k`` successes were observed:

    * ``"greater"`` : ``P(K ≥ k)`` (the alternative says the probability is larger than ``p``);
    * ``"less"`` : ``P(K ≤ k)``;
    * ``"two-sided"`` : the sum of ``P(K = j)`` over every ``j`` such that ``P(K = j) ≤ P(K = k) × (1 + 1e-7)`` (the
      outcomes at most as likely as the observed one), capped at 1.

    Parameters
    ----------
    k : int
        Number of successes, ``0 ≤ k ≤ n``.
    n : int
        Number of trials, at least 1.
    p : float, default 0.5
        Probability of success under H0, strictly between 0 and 1.
    alternative : {"two-sided", "greater", "less"}, default "two-sided"

    Returns
    -------
    float
        A p-value in ]0, 1].

    Raises
    ------
    ValueError
        If ``k``, ``n`` or ``p`` is out of range, or if ``alternative`` is unknown.

    Examples
    --------
    >>> binomial_test(9, 10, alternative="greater")
    0.0107421875
    >>> binomial_test(9, 10)
    0.021484375
    >>> binomial_test(5, 10)
    1.0
    """
    k, n, p = _check_binomial(k, n, p)
    if alternative not in ("two-sided", "greater", "less"):
        raise ValueError(f"alternative must be 'two-sided', 'greater' or 'less', got {alternative!r}")
    probs = [_binomial_pmf(j, n, p) for j in range(n + 1)]
    if alternative == "greater":
        total = math.fsum(probs[k:])
    elif alternative == "less":
        total = math.fsum(probs[: k + 1])
    else:
        threshold = probs[k] * (1 + 1e-7)
        total = math.fsum(q for q in probs if q <= threshold)
    return float(min(1.0, total))


def permutation_test(x, y, n_permutations=9999, alternative="two-sided", seed=0):
    """Return the p-value of the two-sample permutation test of ``H0 : x and y come from the same law``.

    The statistic is ``t = mean(x) - mean(y)``. Pool the values (``x`` first, then ``y``), then repeat
    ``n_permutations`` times: ``perm = rng.permutation(pooled)`` with ``rng = numpy.random.default_rng(seed)``, and
    ``t_perm`` = mean of ``perm[:len(x)]`` minus mean of ``perm[len(x):]``. Count ``C``, the draws at least as extreme
    as the observed ``t`` (up to 1e-9, for rounding errors):

    * ``"greater"`` : ``t_perm ≥ t - 1e-9`` ;
    * ``"less"`` : ``t_perm ≤ t + 1e-9`` ;
    * ``"two-sided"`` : ``|t_perm| ≥ |t| - 1e-9``.

    The p-value is ``(C + 1) / (n_permutations + 1)``: it counts the observed split as one of the permutations, so it
    is never 0. (``scipy.stats.permutation_test`` defines its two-sided p-value differently: twice the smaller
    one-sided one.)

    Parameters
    ----------
    x, y : 1-D array-like
        The two samples, each with at least one value.
    n_permutations : int, default 9999
        Number of random permutations, at least 1.
    alternative : {"two-sided", "greater", "less"}, default "two-sided"
        ``"greater"`` when the alternative says that ``x`` tends to be larger than ``y``.
    seed : int, default 0
        Seed of the generator.

    Returns
    -------
    float
        A p-value in ]0, 1].

    Raises
    ------
    ValueError
        If a sample is empty, if ``n_permutations < 1`` or if ``alternative`` is unknown.

    Examples
    --------
    >>> permutation_test([1, 2, 3], [3, 2, 1])
    1.0
    >>> permutation_test([10, 11, 12, 13], [1, 2, 3, 4], alternative="greater")
    0.0146
    """
    x = _sample(x, "x")
    y = _sample(y, "y")
    if isinstance(n_permutations, bool) or int(n_permutations) != n_permutations or n_permutations < 1:
        raise ValueError(f"n_permutations must be an integer at least 1, got {n_permutations!r}")
    if alternative not in ("two-sided", "greater", "less"):
        raise ValueError(f"alternative must be 'two-sided', 'greater' or 'less', got {alternative!r}")
    observed = x.mean() - y.mean()
    pooled = np.concatenate([x, y])
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(int(n_permutations)):
        perm = rng.permutation(pooled)
        t_perm = perm[: x.size].mean() - perm[x.size:].mean()
        if alternative == "greater":
            count += bool(t_perm >= observed - 1e-9)
        elif alternative == "less":
            count += bool(t_perm <= observed + 1e-9)
        else:
            count += bool(abs(t_perm) >= abs(observed) - 1e-9)
    return float((count + 1) / (int(n_permutations) + 1))


def proportion_ci(k, n, level=0.95, method="wilson"):
    """Return a confidence interval ``(low, high)`` for a proportion, after ``k`` successes in ``n`` trials.

    With ``p̂ = k / n`` and ``z`` the quantile of order ``(1 + level) / 2`` of the standard normal law:

    * ``"wald"`` : ``p̂ ± z √(p̂ (1 - p̂) / n)``, clipped to [0, 1];
    * ``"wilson"`` : ``(p̂ + z²/(2n) ± z √(p̂ (1 - p̂)/n + z²/(4n²))) / (1 + z²/n)``, always inside [0, 1].

    Parameters
    ----------
    k : int
        Number of successes, ``0 ≤ k ≤ n``.
    n : int
        Number of trials, at least 1.
    level : float, default 0.95
        Confidence level, strictly between 0 and 1.
    method : {"wilson", "wald"}, default "wilson"

    Returns
    -------
    tuple of float
        ``(low, high)`` with ``0 ≤ low ≤ high ≤ 1``.

    Raises
    ------
    ValueError
        If ``k``, ``n`` or ``level`` is out of range, or if ``method`` is unknown.

    Examples
    --------
    >>> proportion_ci(0, 10, method="wald")
    (0.0, 0.0)
    >>> [round(v, 4) for v in proportion_ci(0, 10)]
    [0.0, 0.2775]
    >>> [round(v, 4) for v in proportion_ci(8, 40)]
    [0.105, 0.3476]
    """
    k, n, _ = _check_binomial(k, n, 0.5)
    if not 0 < level < 1:
        raise ValueError(f"level must be strictly between 0 and 1, got {level!r}")
    if method not in ("wilson", "wald"):
        raise ValueError(f"method must be 'wilson' or 'wald', got {method!r}")
    z = statistics.NormalDist().inv_cdf((1 + level) / 2)
    p_hat = k / n
    if method == "wald":
        half = z * math.sqrt(p_hat * (1 - p_hat) / n)
        low, high = p_hat - half, p_hat + half
    else:
        denominator = 1 + z * z / n
        center = (p_hat + z * z / (2 * n)) / denominator
        half = z * math.sqrt(p_hat * (1 - p_hat) / n + z * z / (4 * n * n)) / denominator
        low, high = center - half, center + half
    return (float(min(1.0, max(0.0, low))), float(min(1.0, max(0.0, high))))


def paired_difference_ci(a, b, level=0.95):
    """Return Student's confidence interval ``(low, high)`` for the mean of the paired differences ``d_i = a_i - b_i``.

    ``d̄ ± t s_d / √n``, where ``s_d`` is the standard deviation of the differences with ``ddof=1`` and ``t`` the
    quantile of order ``(1 + level) / 2`` of Student's law with ``n - 1`` degrees of freedom
    (``scipy.stats.t.ppf(q, n - 1)``).

    Parameters
    ----------
    a, b : 1-D array-like
        Two measurements of the same ``n`` individuals, in the same order, ``n ≥ 2``.
    level : float, default 0.95
        Confidence level, strictly between 0 and 1.

    Returns
    -------
    tuple of float
        ``(low, high)``.

    Raises
    ------
    ValueError
        If the lengths differ, if ``n < 2`` or if ``level`` is out of range.

    Examples
    --------
    >>> [round(v, 4) for v in paired_difference_ci([5, 7, 6, 8], [4, 5, 5, 6])]
    [0.5813, 2.4187]
    """
    a = _sample(a, "a")
    b = _sample(b, "b")
    if a.size != b.size:
        raise ValueError(f"a and b must have the same length (paired measurements), got {a.size} and {b.size}")
    if a.size < 2:
        raise ValueError(f"at least 2 pairs are needed (ddof=1), got {a.size}")
    if not 0 < level < 1:
        raise ValueError(f"level must be strictly between 0 and 1, got {level!r}")
    d = a - b
    n = d.size
    quantile = student.ppf((1 + level) / 2, n - 1)
    half = quantile * d.std(ddof=1) / math.sqrt(n)
    mean = d.mean()
    return (float(mean - half), float(mean + half))


def bonferroni(p_values):
    """Return the Bonferroni-adjusted p-values ``min(1, m p_i)``, where ``m`` is the number of tests.

    Rejecting ``H0_i`` when its adjusted p-value is at most ``α`` keeps the probability of at least one false
    rejection below ``α``, whatever the dependence between the tests.

    Parameters
    ----------
    p_values : 1-D array-like
        At least one p-value, each between 0 and 1.

    Returns
    -------
    numpy.ndarray
        The adjusted p-values, in the same order.

    Raises
    ------
    ValueError
        If the list is empty or a value is outside [0, 1].

    Examples
    --------
    >>> bonferroni([0.01, 0.04, 0.3])
    array([0.03, 0.12, 0.9 ])
    """
    p = np.array(p_values, dtype=float)
    if p.ndim != 1 or p.size == 0:
        raise ValueError(f"p_values must be a non-empty 1-D list, got shape {p.shape}")
    if not np.all((p >= 0) & (p <= 1)):
        raise ValueError("every p-value must be between 0 and 1")
    return np.minimum(1.0, p * p.size)


def aic_bic(log_likelihood, k, n):
    """Return the information criteria ``(AIC, BIC) = (2k - 2 ln L, k ln n - 2 ln L)`` of a fitted model.

    The smaller, the better; BIC penalizes each parameter more than AIC as soon as ``n ≥ 8``.

    Parameters
    ----------
    log_likelihood : float
        The maximized log-likelihood ``ln L`` of the model (natural logarithm).
    k : int
        Number of fitted parameters, at least 1.
    n : int
        Number of observations, at least 1.

    Returns
    -------
    tuple of float
        ``(aic, bic)``.

    Raises
    ------
    ValueError
        If ``k < 1`` or ``n < 1``.

    Examples
    --------
    >>> aic, bic = aic_bic(-100.0, 3, 50)
    >>> aic
    206.0
    >>> round(bic, 3)
    211.736
    """
    if k < 1 or n < 1:
        raise ValueError(f"k and n must be at least 1, got k = {k!r} and n = {n!r}")
    log_likelihood = float(log_likelihood)
    return (float(2 * k - 2 * log_likelihood), float(k * math.log(n) - 2 * log_likelihood))
