"""Concentration inequalities: Markov, Chebyshev, Hoeffding, confidence radius, empirical tail (chapter M11).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m11_concentration.py``.
NumPy and ``math`` are allowed. A bound is a probability: when the formula gives more than 1, return 1. Every number
returned is a Python ``float``.
"""


def markov_bound(mean, a):
    """Return Markov's bound ``min(1, E[X] / a)`` on ``P(X ≥ a)``, for a variable ``X ≥ 0``.

    Parameters
    ----------
    mean : float
        The expectation ``E[X] ≥ 0`` of a non-negative variable.
    a : float
        The threshold, ``a > 0``.

    Returns
    -------
    float
        Between 0 and 1.

    Raises
    ------
    ValueError
        If ``mean < 0`` or ``a <= 0``.

    Examples
    --------
    >>> markov_bound(2.0, 8.0)
    0.25
    >>> markov_bound(3.0, 2.0)
    1.0
    """
    # TODO: one division and a min.
    raise NotImplementedError("markov_bound() is not implemented yet")


def chebyshev_bound(variance, t):
    """Return Chebyshev's bound ``min(1, V(X) / t²)`` on ``P(|X - E[X]| ≥ t)``.

    Parameters
    ----------
    variance : float
        The variance ``V(X) ≥ 0``.
    t : float
        The distance to the mean, ``t > 0``.

    Returns
    -------
    float
        Between 0 and 1.

    Raises
    ------
    ValueError
        If ``variance < 0`` or ``t <= 0``.

    Examples
    --------
    >>> chebyshev_bound(4.0, 5.0)
    0.16
    """
    # TODO: one division and a min.
    raise NotImplementedError("chebyshev_bound() is not implemented yet")


def hoeffding_bound(n, t, a=0.0, b=1.0):
    """Return Hoeffding's bound on ``P(|X̄ - μ| ≥ t)`` for the mean of ``n`` independent variables in ``[a, b]``.

    ``min(1, 2 exp(-2 n t² / (b - a)²))``, where ``μ`` is the expectation of the mean ``X̄``.

    Parameters
    ----------
    n : int
        Number of variables, at least 1.
    t : float
        The deviation, ``t > 0``.
    a, b : float, default 0.0 and 1.0
        Bounds of every variable, ``a < b``.

    Returns
    -------
    float
        Between 0 and 1.

    Raises
    ------
    ValueError
        If ``n < 1``, ``t <= 0`` or ``a >= b``.

    Examples
    --------
    >>> round(hoeffding_bound(100, 0.1), 4)
    0.2707
    >>> hoeffding_bound(10, 0.1)
    1.0
    """
    # TODO: the formula with math.exp, then a min.
    raise NotImplementedError("hoeffding_bound() is not implemented yet")


def hoeffding_radius(n, delta, a=0.0, b=1.0):
    """Return the radius ``(b - a) √(ln(2/δ) / (2n))`` given by Hoeffding's inequality at confidence ``1 - δ``.

    With probability at least ``1 - δ``, the mean of ``n`` independent variables in ``[a, b]`` is at distance less
    than this radius from its expectation: it is the value of ``t`` for which :func:`hoeffding_bound` equals ``δ``.

    Parameters
    ----------
    n : int
        Number of variables, at least 1.
    delta : float
        The risk, strictly between 0 and 1.
    a, b : float, default 0.0 and 1.0
        Bounds of every variable, ``a < b``.

    Returns
    -------
    float
        Positive.

    Raises
    ------
    ValueError
        If ``n < 1``, ``delta`` is not in ]0, 1[ or ``a >= b``.

    Examples
    --------
    >>> round(hoeffding_radius(200, 0.05), 4)
    0.096
    >>> round(hoeffding_radius(200, 0.05, a=-1.0, b=1.0), 4)
    0.1921
    """
    # TODO: solve 2 exp(-2 n t² / (b - a)²) = δ for t.
    raise NotImplementedError("hoeffding_radius() is not implemented yet")


def empirical_tail(samples, threshold):
    """Return the proportion of the samples that are at least ``threshold``: an estimate of ``P(X ≥ threshold)``.

    Parameters
    ----------
    samples : 1-D array-like
        At least one value.
    threshold : float

    Returns
    -------
    float
        Between 0 and 1.

    Raises
    ------
    ValueError
        If ``samples`` is empty.

    Examples
    --------
    >>> empirical_tail([1, 3, 5, 7], 5)
    0.5
    >>> empirical_tail([1, 3, 5, 7], 8)
    0.0
    """
    # TODO: the mean of a boolean array.
    raise NotImplementedError("empirical_tail() is not implemented yet")
