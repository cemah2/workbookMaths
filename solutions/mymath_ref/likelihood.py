"""Likelihood: Bernoulli log-likelihood and maximum likelihood estimates (Bernoulli, categorical with smoothing,
Gaussian), and the logistic loss computed from scores without overflow (chapter M13a).

Reference implementation (solutions/mymath_ref).
NumPy and the module ``math`` are allowed, but not SciPy nor scikit-learn: the tests compare your results with
``scipy.stats``, ``scipy.special`` and ``sklearn.metrics.log_loss``. Logarithms are natural logarithms. Labels are
0 or 1 (an int, a float or a bool). Numbers are returned as Python ``float``, vectors as ``numpy.ndarray`` of floats.
"""

import math

import numpy as np


def _labels(y):
    """A copy of y as a 1-D array of floats, each 0 or 1 (ValueError otherwise; booleans are accepted)."""
    a = np.asarray(y)
    if a.dtype.kind not in "biuf":
        raise ValueError(f"y must be made of 0 and 1, got values of type {a.dtype}")
    a = a.astype(float)
    if a.ndim != 1 or a.size == 0:
        raise ValueError(f"y must be a non-empty 1-D array of 0 and 1, got an array of shape {a.shape}")
    if not np.all((a == 0) | (a == 1)):
        raise ValueError("y must be made of 0 and 1")
    return a


def _vector(x, what):
    """A copy of x as a 1-D array of floats (ValueError otherwise)."""
    a = np.asarray(x)
    if a.dtype.kind not in "biuf":
        raise ValueError(f"{what} must be made of numbers, got values of type {a.dtype}")
    a = a.astype(float)
    if a.ndim != 1:
        raise ValueError(f"{what} must be a 1-D array, got an array of shape {a.shape}")
    return a



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
    labels = _labels(y)
    q = np.asarray(p)
    if q.dtype.kind not in "biuf":
        raise ValueError(f"p must be made of numbers, got values of type {q.dtype}")
    q = q.astype(float)
    if q.ndim == 0:
        q = np.full(labels.size, float(q))
    elif q.ndim != 1 or q.size != labels.size:
        raise ValueError(f"p must be one probability, or one per label ({labels.size}), got shape {q.shape}")
    if not np.all((q >= 0) & (q <= 1)):                     # NaN fails too
        raise ValueError("every probability p must be in [0, 1]")
    with np.errstate(divide="ignore"):                      # ln 0 = -inf, without warning
        logs = np.where(labels == 1, np.log(q), np.log1p(-q))
    return float(np.sum(logs))


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
    return float(np.mean(_labels(y)))


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
    n = _vector(counts, "counts")
    if n.size == 0:
        raise ValueError("counts must not be empty")
    if not np.all(n >= 0):                                  # NaN fails too
        raise ValueError("every count must be non-negative")
    a = float(alpha)
    if not a >= 0:
        raise ValueError(f"alpha must be non-negative, got {alpha!r}")
    total = float(n.sum()) + n.size * a
    if total == 0:
        raise ValueError("every count is 0: with alpha = 0, the maximum likelihood estimate is undefined")
    return (n + a) / total


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
    v = _vector(x, "x")
    if v.size == 0:
        raise ValueError("x must not be empty")
    mean = float(np.mean(v))
    return mean, float(np.mean((v - mean) ** 2))


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
    scores = _vector(z, "z")
    labels = _labels(y)
    if scores.size != labels.size:
        raise ValueError(f"z and y must have the same length, got {scores.size} and {labels.size}")
    t = np.where(labels == 1, -scores, scores)              # softplus(z) - y z = softplus(±z)
    softplus = np.maximum(t, 0.0) + np.log1p(np.exp(-np.abs(t)))
    return float(np.mean(softplus))
