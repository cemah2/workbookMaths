"""Statistical tests: exact binomial test, permutation test, intervals, Bonferroni, AIC and BIC (chapter M08).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m08_testing.py``.
NumPy is allowed, and so are the quantile functions ``statistics.NormalDist().inv_cdf`` and ``scipy.stats.t.ppf``;
the other tools of ``scipy.stats`` (``binomtest``, ``permutation_test``, ``ttest_rel``…) are not: the tests compare
your results with them. Randomness comes from one generator ``numpy.random.default_rng(seed)``, used in the order the
docstring gives, so that the same seed gives the same p-value. Every number returned is a Python ``float``.
"""


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
    # TODO: the n + 1 probabilities P(K = j) (math.comb), then add those the alternative asks for.
    raise NotImplementedError("binomial_test() is not implemented yet")


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
    # TODO: the observed statistic, the loop over the permutations, the count C, then (C + 1) / (n_permutations + 1).
    raise NotImplementedError("permutation_test() is not implemented yet")


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
    # TODO: z from statistics.NormalDist().inv_cdf, then the formula of the method.
    raise NotImplementedError("proportion_ci() is not implemented yet")


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
    # TODO: the differences, their mean and standard deviation (ddof=1), the quantile, then the interval.
    raise NotImplementedError("paired_difference_ci() is not implemented yet")


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
    # TODO: multiply by m, then cap at 1 (np.minimum).
    raise NotImplementedError("bonferroni() is not implemented yet")


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
    # TODO: two formulas (math.log is the natural logarithm).
    raise NotImplementedError("aic_bic() is not implemented yet")
