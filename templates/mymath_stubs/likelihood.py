"""Likelihood: Bernoulli log-likelihood and maximum likelihood estimates (Bernoulli, categorical with smoothing,
Gaussian), and the logistic loss computed from scores without overflow (chapter M13a).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m13a_likelihood.py``.
NumPy and the module ``math`` are allowed, but not SciPy nor scikit-learn: the tests compare your results with
``scipy.stats``, ``scipy.special`` and ``sklearn.metrics.log_loss``. Logarithms are natural logarithms. Labels are
0 or 1 (an int, a float or a bool). Numbers are returned as Python ``float``, vectors as ``numpy.ndarray`` of floats.
"""


def bernoulli_log_likelihood(y, p):
    """Return the log-likelihood ``Σ [y_i ln p_i + (1 - y_i) ln(1 - p_i)]`` of labels ``y`` under probabilities ``p``.

    ``p`` is either one probability shared by all the labels, or one probability per label. A label of probability 0
    makes the log-likelihood ``-inf`` (return ``-math.inf``, without warning); the terms ``0 · ln 0`` count as 0.

    Parameters
    ----------
    y : 1-D array-like
        The labels, 0 or 1.
    p : float or 1-D array-like
        The probabilities that each label is 1, in ``[0, 1]``.

    Returns
    -------
    float
        The log-likelihood, at most 0.

    Raises
    ------
    ValueError
        If ``y`` is empty or not made of 0 and 1, if ``p`` has the wrong length, or a value outside ``[0, 1]``.

    Examples
    --------
    >>> round(bernoulli_log_likelihood([1, 0, 1, 1], 0.75), 4)
    -2.2493
    >>> bernoulli_log_likelihood([1, 0], [1.0, 1.0])
    -inf
    """
    # TODO: check y and p, then sum the log of the probability of each observed label (p_i or 1 - p_i).
    raise NotImplementedError("bernoulli_log_likelihood() is not implemented yet")


def bernoulli_mle(y):
    """Return the maximum likelihood estimate of the parameter of a Bernoulli law: the proportion of 1.

    Parameters
    ----------
    y : 1-D array-like
        The labels, 0 or 1.

    Returns
    -------
    float
        ``p̂ = (number of 1) / n``.

    Raises
    ------
    ValueError
        If ``y`` is empty or not made of 0 and 1.

    Examples
    --------
    >>> bernoulli_mle([1, 0, 1, 1])
    0.75
    """
    # TODO: check y, then its mean.
    raise NotImplementedError("bernoulli_mle() is not implemented yet")


def categorical_mle(counts, alpha=0.0):
    """Return the estimated probabilities of the ``K`` categories of a categorical law from their counts.

    With ``alpha = 0``, the maximum likelihood estimate ``n_k / N``; with ``alpha > 0``, the smoothed estimate
    ``(n_k + alpha) / (N + K alpha)`` (Laplace smoothing for ``alpha = 1``, M04), which never gives a probability of 0.

    Parameters
    ----------
    counts : 1-D array-like
        The ``K`` counts, non-negative.
    alpha : float, default 0.0
        The pseudo-count added to each category, ``alpha ≥ 0``.

    Returns
    -------
    numpy.ndarray
        The ``K`` probabilities, of sum 1.

    Raises
    ------
    ValueError
        If ``counts`` is empty, not 1-D or has a negative entry, if ``alpha < 0``, or if every count is 0 while
        ``alpha = 0``.

    Examples
    --------
    >>> categorical_mle([3, 1, 0])
    array([0.75, 0.25, 0.  ])
    >>> categorical_mle([3, 1, 0], alpha=1)
    array([0.57142857, 0.28571429, 0.14285714])
    """
    # TODO: check the counts and alpha, then (n_k + alpha) / (N + K alpha).
    raise NotImplementedError("categorical_mle() is not implemented yet")


def gaussian_mle(x):
    """Return the maximum likelihood estimates ``(μ̂, σ̂²)`` of a normal law ``N(μ, σ²)`` from a sample.

    ``μ̂`` is the sample mean and ``σ̂² = (1/n) Σ (x_i - μ̂)²``: the maximum likelihood divides by ``n``, not by
    ``n - 1`` (it is a biased estimate of ``σ²``, M02c).

    Parameters
    ----------
    x : 1-D array-like
        The sample, at least one value.

    Returns
    -------
    tuple of float
        ``(mean, variance)``.

    Raises
    ------
    ValueError
        If ``x`` is empty or not 1-D.

    Examples
    --------
    >>> gaussian_mle([2, 4, 4, 6])
    (4.0, 2.0)
    """
    # TODO: the mean, then the mean of the squared deviations.
    raise NotImplementedError("gaussian_mle() is not implemented yet")


def logistic_loss(z, y):
    """Return the mean logistic loss ``(1/n) Σ [ln(1 + e^{z_i}) - y_i z_i]`` of scores ``z`` and labels ``y``.

    With ``p_i = σ(z_i)``, each term equals ``-[y_i ln p_i + (1 - y_i) ln(1 - p_i)]``: this is the log-loss of the
    probabilities ``σ(z)``, written with the scores. Compute ``ln(1 + e^z)`` (the *softplus*) without overflow as
    ``max(z, 0) + ln(1 + e^{-|z|})`` (``np.log1p``), so that very large scores give finite results.

    Parameters
    ----------
    z : 1-D array-like
        The scores (any real numbers).
    y : 1-D array-like
        The labels, 0 or 1, one per score.

    Returns
    -------
    float
        The mean loss, non-negative.

    Raises
    ------
    ValueError
        If the lengths differ, if ``y`` is empty or not made of 0 and 1.

    Examples
    --------
    >>> round(logistic_loss([0.0, 0.0], [1, 0]), 6)
    0.693147
    >>> round(logistic_loss([30.0, -30.0], [0, 1]), 6)
    30.0
    """
    # TODO: check the inputs, the stable softplus of z, minus y z, then the mean.
    raise NotImplementedError("logistic_loss() is not implemented yet")
