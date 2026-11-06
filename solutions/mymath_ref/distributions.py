"""Usual laws: binomial, Poisson and normal probabilities, sampling by inverse transform (chapter M02b).

Reference implementation (solutions/mymath_ref).
Do not use ``scipy.stats``: the tests compare your results with it. ``math.comb``, ``math.factorial``,
``math.exp`` and ``math.erf`` are allowed. Every probability or density is a Python ``float``.
"""

import math

import numpy as np



def binomial_pmf(k, n, p):
    """Return ``P(X = k)`` for ``X`` following the binomial law ``B(n, p)``.

    Parameters
    ----------
    k : int
        Any integer: the probability is 0.0 when ``k < 0`` or ``k > n``.
    n : int
        Number of trials, non-negative.
    p : float
        Probability of success of each trial, in ``[0, 1]``.

    Returns
    -------
    float
        ``C(n, k) p**k (1 - p)**(n - k)``.

    Raises
    ------
    ValueError
        If ``n < 0`` or ``p`` is not in ``[0, 1]``.

    Examples
    --------
    >>> binomial_pmf(2, 4, 0.5)
    0.375
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    if not 0 <= p <= 1:
        raise ValueError(f"p must be in [0, 1], got {p}")
    if k < 0 or k > n:
        return 0.0
    return float(math.comb(n, k) * p ** k * (1 - p) ** (n - k))


def poisson_pmf(k, lam):
    """Return ``P(X = k)`` for ``X`` following the Poisson law of parameter ``lam``.

    Parameters
    ----------
    k : int
        Any integer: the probability is 0.0 when ``k < 0``. The tests use ``k <= 100``.
    lam : float
        The mean number of events, non-negative (``lam = 0`` gives ``P(X = 0) = 1``). The tests use ``lam <= 50``.

    Returns
    -------
    float
        ``exp(-lam) lam**k / k!``.

    Raises
    ------
    ValueError
        If ``lam < 0``.

    Examples
    --------
    >>> round(poisson_pmf(0, 2), 6)
    0.135335
    """
    if lam < 0:
        raise ValueError(f"lam must be non-negative, got {lam}")
    if k < 0:
        return 0.0
    return float(math.exp(-lam) * lam ** k / math.factorial(k))


def normal_pdf(x, mu=0.0, sigma=1.0):
    """Return the density at ``x`` of the normal law ``N(mu, sigma²)``.

    Parameters
    ----------
    x : float
    mu : float, default 0.0
        The mean.
    sigma : float, default 1.0
        The standard deviation (not the variance), positive.

    Returns
    -------
    float
        ``exp(-(x - mu)**2 / (2 sigma**2)) / (sigma sqrt(2 pi))``.

    Raises
    ------
    ValueError
        If ``sigma <= 0``.

    Examples
    --------
    >>> round(normal_pdf(0), 6)
    0.398942
    """
    if sigma <= 0:
        raise ValueError(f"sigma must be positive, got {sigma}")
    z = (x - mu) / sigma
    return float(math.exp(-z * z / 2) / (sigma * math.sqrt(2 * math.pi)))


def normal_cdf(x, mu=0.0, sigma=1.0):
    """Return ``P(X <= x)`` for ``X`` following the normal law ``N(mu, sigma²)``.

    Parameters
    ----------
    x : float
    mu : float, default 0.0
    sigma : float, default 1.0
        Positive.

    Returns
    -------
    float
        ``Φ((x - mu) / sigma)``, where ``Φ(z) = (1 + erf(z / sqrt(2))) / 2``.

    Raises
    ------
    ValueError
        If ``sigma <= 0``.

    Examples
    --------
    >>> normal_cdf(0)
    0.5
    >>> round(normal_cdf(1.96), 4)
    0.975
    """
    if sigma <= 0:
        raise ValueError(f"sigma must be positive, got {sigma}")
    z = (x - mu) / sigma
    return float((1 + math.erf(z / math.sqrt(2))) / 2)


def inverse_transform_sample(inverse_cdf, n, seed=0):
    """Draw ``n`` values of a law by applying its inverse CDF to uniform draws.

    If ``U`` is uniform on ``[0, 1)`` and ``F`` is a CDF, ``F⁻¹(U)`` follows the law of CDF ``F``.

    Parameters
    ----------
    inverse_cdf : callable
        ``inverse_cdf(u)`` for one float ``u`` in ``[0, 1)``, e.g. ``lambda u: -math.log(1 - u)`` for the
        exponential law of parameter 1.
    n : int
        Number of draws, at least 1.
    seed : int, default 0
        The uniforms are ``numpy.random.default_rng(seed).random(n)``, in this order: the same seed gives the same
        values.

    Returns
    -------
    numpy.ndarray
        Shape ``(n,)``, dtype float: ``inverse_cdf`` applied to each uniform.

    Raises
    ------
    ValueError
        If ``n < 1``.

    Examples
    --------
    >>> xs = inverse_transform_sample(lambda u: 3 * u, 10_000)   # the uniform law on [0, 3]
    >>> xs.shape, bool(xs.min() >= 0), bool(xs.max() <= 3)
    ((10000,), True, True)
    """
    if n < 1:
        raise ValueError(f"n must be at least 1, got {n}")
    uniforms = np.random.default_rng(seed).random(n)
    return np.array([float(inverse_cdf(float(u))) for u in uniforms], dtype=float)
