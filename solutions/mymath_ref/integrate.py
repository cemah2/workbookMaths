"""Integrals by hand and by computer: Riemann sums, trapezoids, Simpson, CDF and quantiles (chapter M02a).

Reference implementation (solutions/mymath_ref).
Do not use ``scipy.integrate`` nor ``numpy.trapezoid``: the tests compare your results with them. A function ``f``
takes one float and returns one float; every result is a Python ``float``.
"""


def riemann_sum(f, a, b, n, rule="left"):
    """Approximate the integral of ``f`` from ``a`` to ``b`` by a Riemann sum with ``n`` rectangles.

    The ``n`` rectangles have the same width ``h = (b - a) / n``; the height of the rectangle on
    ``[a + i h, a + (i + 1) h]`` is the value of ``f`` at its left end, its right end or its middle.

    Parameters
    ----------
    f : callable
        A function of one real variable.
    a, b : float
        Bounds of the integral. ``a > b`` is allowed: the width ``h`` is then negative and the same formula
        approximates ``∫_a^b f = -∫_b^a f``.
    n : int
        Number of rectangles, at least 1.
    rule : {"left", "right", "midpoint"}, default "left"
        Where the height of each rectangle is read.

    Returns
    -------
    float
        ``h * (f(x_0) + ... + f(x_{n-1}))`` where ``x_i`` is the chosen point of the ``i``-th rectangle.

    Raises
    ------
    ValueError
        If ``n < 1`` or if ``rule`` is not one of the three names.

    Examples
    --------
    >>> riemann_sum(lambda x: x, 0, 1, 4)
    0.375
    >>> riemann_sum(lambda x: x, 0, 1, 4, rule="midpoint")
    0.5
    """
    offsets = {"left": 0.0, "right": 1.0, "midpoint": 0.5}
    if n < 1:
        raise ValueError(f"n must be at least 1, got {n}")
    if rule not in offsets:
        raise ValueError(f"rule must be 'left', 'right' or 'midpoint', got {rule!r}")
    h = (b - a) / n
    shift = offsets[rule]
    return float(h * sum(f(a + (i + shift) * h) for i in range(n)))


def trapezoid(f, a, b, n):
    """Approximate the integral of ``f`` from ``a`` to ``b`` by the trapezoid rule with ``n`` intervals.

    Parameters
    ----------
    f : callable
        A function of one real variable.
    a, b : float
        Bounds of the integral (``a > b`` is allowed, as in :func:`riemann_sum`).
    n : int
        Number of intervals of width ``h = (b - a) / n``, at least 1.

    Returns
    -------
    float
        ``h * (f(x_0) / 2 + f(x_1) + ... + f(x_{n-1}) + f(x_n) / 2)`` with ``x_i = a + i h``.

    Raises
    ------
    ValueError
        If ``n < 1``.

    Examples
    --------
    >>> trapezoid(lambda x: x ** 2, 0, 2, 2)
    3.0
    """
    if n < 1:
        raise ValueError(f"n must be at least 1, got {n}")
    h = (b - a) / n
    inner = sum(f(a + i * h) for i in range(1, n))
    return float(h * ((f(a) + f(b)) / 2 + inner))


def simpson(f, a, b, n):
    """Approximate the integral of ``f`` from ``a`` to ``b`` by Simpson's rule with ``n`` intervals.

    Parameters
    ----------
    f : callable
        A function of one real variable.
    a, b : float
        Bounds of the integral (``a > b`` is allowed, as in :func:`riemann_sum`).
    n : int
        Number of intervals of width ``h = (b - a) / n``: even and at least 2.

    Returns
    -------
    float
        ``h / 3 * (f(x_0) + 4 f(x_1) + 2 f(x_2) + 4 f(x_3) + ... + 4 f(x_{n-1}) + f(x_n))``.

    Raises
    ------
    ValueError
        If ``n`` is odd or smaller than 2.

    Examples
    --------
    >>> simpson(lambda x: x ** 3, 0, 2, 2)
    4.0
    """
    if n < 2 or n % 2 != 0:
        raise ValueError(f"n must be even and at least 2, got {n}")
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 == 1 else 2) * f(a + i * h)
    return float(h / 3 * total)


def cdf_from_pdf(pdf, x, lower, n=1000):
    """Return the value at ``x`` of the cumulative distribution function of a density.

    ``F(x) = ∫_lower^x pdf(t) dt``, approximated by the trapezoid rule with ``n`` intervals.

    Parameters
    ----------
    pdf : callable
        A probability density, zero (or negligible) below ``lower``.
    x : float
        Where the CDF is evaluated.
    lower : float
        A finite point below which the density is zero.
    n : int, default 1000
        Number of intervals of the trapezoid rule, at least 1.

    Returns
    -------
    float
        ``0.0`` when ``x <= lower``; otherwise the trapezoid approximation of the integral from ``lower`` to ``x``.

    Raises
    ------
    ValueError
        If ``n < 1``.

    Examples
    --------
    >>> round(cdf_from_pdf(lambda t: 2 * t, 0.5, 0), 6)
    0.25
    """
    if n < 1:
        raise ValueError(f"n must be at least 1, got {n}")
    if x <= lower:
        return 0.0
    return trapezoid(pdf, lower, x, n)


def quantile(cdf, p, low, high, tol=1e-10):
    """Return the quantile of order ``p`` of a law, given its CDF, by bisection on ``[low, high]``.

    The quantile is the smallest ``x`` such that ``cdf(x) >= p``; for ``p = 0.5`` it is the median.

    Parameters
    ----------
    cdf : callable
        A cumulative distribution function: non-decreasing, with values in ``[0, 1]``.
    p : float
        The order, strictly between 0 and 1.
    low, high : float
        An interval that contains the quantile: ``low < high``, ``cdf(low) <= p <= cdf(high)``.
    tol : float, default 1e-10
        Stop as soon as the interval is shorter than ``tol``, or after 200 halvings.

    Returns
    -------
    float
        The middle of the last interval: within ``tol`` of the quantile when the loop stops because of ``tol``.

    Raises
    ------
    ValueError
        If ``p`` is not strictly between 0 and 1, if ``low >= high``, or if ``cdf(low) > p`` or ``cdf(high) < p``.

    Examples
    --------
    >>> round(quantile(lambda x: x ** 2, 0.25, 0, 1), 6)
    0.5
    """
    if not 0 < p < 1:
        raise ValueError(f"p must be strictly between 0 and 1, got {p}")
    if low >= high:
        raise ValueError(f"low must be smaller than high, got {low} and {high}")
    if cdf(low) > p or cdf(high) < p:
        raise ValueError("the quantile is not in [low, high]: cdf(low) <= p <= cdf(high) is needed")
    lo, hi = low, high
    for _ in range(200):
        if hi - lo < tol:
            break
        mid = (lo + hi) / 2
        if cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return float((lo + hi) / 2)
