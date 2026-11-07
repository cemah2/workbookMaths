"""The Beta law and Bayesian updating of a proportion: density, moments, conjugacy, predictive, MAP (chapter M04).

Reference implementation (solutions/mymath_ref).
Do not use ``scipy.stats`` nor ``scipy.special``: the tests compare your results with them. ``math.lgamma`` (the
logarithm of the Gamma function, with ``Γ(n) = (n - 1)!``) and ``math.comb`` are allowed. Every number returned is
a Python ``float``, except the parameters returned by :func:`conjugate_beta_update`.
"""

import math


def _check_parameters(a, b):
    """ValueError unless a > 0 and b > 0 (a nan fails both comparisons, so it is refused too)."""
    if not (a > 0 and b > 0):
        raise ValueError(f"the parameters of a Beta law are positive, got a = {a!r}, b = {b!r}")


def _log_beta(a, b):
    """log B(a, b) = log Γ(a) + log Γ(b) - log Γ(a + b), without computing the (possibly huge) Gamma values."""
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


def beta_pdf(x, a, b):
    """Return the density at ``x`` of the Beta law ``Beta(a, b)``.

    ``x**(a - 1) (1 - x)**(b - 1) / B(a, b)`` on ``[0, 1]``, with ``B(a, b) = Γ(a) Γ(b) / Γ(a + b)``.

    Parameters
    ----------
    x : float
    a, b : float
        Positive parameters.

    Returns
    -------
    float
        ``0.0`` when ``x < 0`` or ``x > 1``. At ``x = 0`` the density is ``0.0`` if ``a > 1``, ``1 / B(1, b)`` if
        ``a = 1`` and ``math.inf`` if ``a < 1``; at ``x = 1``, the same with ``b`` in place of ``a``.

    Raises
    ------
    ValueError
        If ``a <= 0`` or ``b <= 0``.

    Examples
    --------
    >>> round(beta_pdf(0.5, 2, 2), 6)
    1.5
    """
    _check_parameters(a, b)
    if x < 0 or x > 1:
        return 0.0
    if x == 0 or x == 1:
        near, far = (a, b) if x == 0 else (b, a)      # the exponent near - 1 is the one that meets 0**(near - 1)
        if near > 1:
            return 0.0
        if near < 1:
            return math.inf
        return float(math.exp(-_log_beta(1, far)))    # 1 / B(1, far), which is far
    log_density = (a - 1) * math.log(x) + (b - 1) * math.log1p(-x) - _log_beta(a, b)
    return float(math.exp(log_density))


def beta_moments(a, b):
    """Return the mean and the variance of the Beta law ``Beta(a, b)``.

    Parameters
    ----------
    a, b : float
        Positive parameters.

    Returns
    -------
    tuple of float
        ``(a / (a + b), a b / ((a + b)**2 (a + b + 1)))``.

    Raises
    ------
    ValueError
        If ``a <= 0`` or ``b <= 0``.

    Examples
    --------
    >>> beta_moments(2, 3)
    (0.4, 0.04)
    """
    _check_parameters(a, b)
    total = a + b
    return float(a / total), float(a * b / (total ** 2 * (total + 1)))


def conjugate_beta_update(a, b, successes, failures):
    """Return the parameters of the posterior law after observing successes and failures, from a ``Beta(a, b)`` prior.

    Parameters
    ----------
    a, b : float
        Positive parameters of the prior.
    successes, failures : int
        Non-negative numbers of observed successes and failures.

    Returns
    -------
    tuple
        ``(a + successes, b + failures)``: ints stay ints.

    Raises
    ------
    ValueError
        If ``a <= 0``, ``b <= 0``, or a count is negative.

    Examples
    --------
    >>> conjugate_beta_update(1, 1, 3, 7)
    (4, 8)
    """
    _check_parameters(a, b)
    if not (successes >= 0 and failures >= 0):
        raise ValueError(f"counts are non-negative, got successes = {successes!r}, failures = {failures!r}")
    return a + successes, b + failures


def posterior_predictive(a, b, k=1, n=1):
    """Return the probability of ``k`` successes in the next ``n`` trials when the proportion follows ``Beta(a, b)``.

    ``C(n, k) B(a + k, b + n - k) / B(a, b)``; with ``k = n = 1``, the probability that the next trial is a
    success, ``a / (a + b)``.

    Parameters
    ----------
    a, b : float
        Positive parameters (of a prior or of a posterior).
    k : int, default 1
        Any integer: the probability is 0.0 when ``k < 0`` or ``k > n``.
    n : int, default 1
        Number of future trials, non-negative.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If ``a <= 0``, ``b <= 0`` or ``n < 0``.

    Examples
    --------
    >>> round(posterior_predictive(4, 8), 4)
    0.3333
    >>> round(posterior_predictive(1, 1, 2, 4), 4)
    0.2
    """
    _check_parameters(a, b)
    if n < 0:
        raise ValueError(f"the number of future trials is non-negative, got n = {n!r}")
    if k < 0 or k > n:
        return 0.0
    log_comb = math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
    return float(math.exp(log_comb + _log_beta(a + k, b + n - k) - _log_beta(a, b)))


def map_estimate_beta(a, b):
    """Return the mode of ``Beta(a, b)``: the MAP estimate of a proportion whose posterior is ``Beta(a, b)``.

    Parameters
    ----------
    a, b : float
        Positive parameters.

    Returns
    -------
    float
        ``(a - 1) / (a + b - 2)`` when ``a > 1`` and ``b > 1``. When the density decreases on ``(0, 1)``
        (``a <= 1 < b``, or ``a < 1 = b``) the mode is ``0.0``; when it increases (``b <= 1 < a``, or
        ``b < 1 = a``) it is ``1.0``.

    Raises
    ------
    ValueError
        If ``a <= 0`` or ``b <= 0``, or when there is no single mode: ``a = b = 1`` (uniform law), or ``a < 1`` and
        ``b < 1`` (two modes, at 0 and at 1).

    Examples
    --------
    >>> map_estimate_beta(4, 8)
    0.3
    """
    _check_parameters(a, b)
    if a > 1 and b > 1:
        return float((a - 1) / (a + b - 2))
    if a == 1 and b == 1:
        raise ValueError("Beta(1, 1) is the uniform law: every point of [0, 1] is a mode")
    if a < 1 and b < 1:
        raise ValueError(f"Beta({a}, {b}) has two modes, at 0 and at 1")
    if a <= 1 < b or (a < 1 and b == 1):
        return 0.0                                     # decreasing density
    return 1.0                                         # increasing density: b <= 1 < a, or b < 1 = a
