"""The Beta law and Bayesian updating of a proportion: density, moments, conjugacy, predictive, MAP (chapter M04).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m04_bayes.py``.
Do not use ``scipy.stats`` nor ``scipy.special``: the tests compare your results with them. ``math.lgamma`` (the
logarithm of the Gamma function, with ``Γ(n) = (n - 1)!``) and ``math.comb`` are allowed. Every number returned is
a Python ``float``, except the parameters returned by :func:`conjugate_beta_update`.
"""


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
    # TODO: the ends 0 and 1 first; then compute log B(a, b) with math.lgamma, to avoid overflow.
    raise NotImplementedError("beta_pdf() is not implemented yet")


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
    # TODO: the two formulas of the fiche.
    raise NotImplementedError("beta_moments() is not implemented yet")


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
    # TODO: check, then add the pseudo-counts.
    raise NotImplementedError("conjugate_beta_update() is not implemented yet")


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
    # TODO: the impossible values of k first; then the formula, with log B computed by math.lgamma.
    raise NotImplementedError("posterior_predictive() is not implemented yet")


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
    # TODO: the general case, then the boundary cases one by one (draw the density for each).
    raise NotImplementedError("map_estimate_beta() is not implemented yet")
