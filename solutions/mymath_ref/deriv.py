"""Limits and derivatives, numerically: rate of change, tangent, bisection (chapter R7).

Reference implementation (solutions/mymath_ref).
"""


def difference_quotient(f, a, h):
    """Return the rate of change ``(f(a + h) - f(a)) / h`` of ``f`` between ``a`` and ``a + h``.

    Parameters
    ----------
    f : callable
    a : float
    h : float
        Non-zero (negative is allowed).

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If ``h`` is zero.

    Examples
    --------
    >>> difference_quotient(lambda x: x * x, 3, 1)
    7.0
    """
    if h == 0:
        raise ValueError("h must be non-zero: the rate of change divides by h")
    return float((f(a + h) - f(a)) / h)


def tangent_line(f, df, a):
    """Return the tangent line to the graph of ``f`` at the point of abscissa ``a``.

    Parameters
    ----------
    f : callable
        The function.
    df : callable
        Its derivative.
    a : float

    Returns
    -------
    tuple of (float, float)
        ``(m, c)`` such that the tangent is ``y = m*x + c`` (ints when ``f``, ``df`` and ``a`` give ints).

    Examples
    --------
    >>> tangent_line(lambda x: x * x, lambda x: 2 * x, 3)
    (6, -9)
    """
    m = df(a)
    return m, f(a) - m * a


def bisection(f, a, b, tol=1e-10, max_iter=200):
    """Find a zero of a continuous function ``f`` on ``[a, b]`` by bisection (dichotomie).

    Parameters
    ----------
    f : callable
        Continuous on ``[a, b]``, with ``f(a)`` and ``f(b)`` of opposite signs (or one of them zero).
    a, b : float
        Ends of the interval, ``a < b``.
    tol : float, default 1e-10
        Stop as soon as the interval is shorter than ``tol``.
    max_iter : int, default 200
        Maximum number of halvings: after ``max_iter`` halvings, stop even if the interval is still longer than
        ``tol`` (no error is raised).

    Returns
    -------
    float
        The middle of the last interval, or an end of an interval where ``f`` is exactly 0. When the loop stops
        because of ``tol``, it is within ``tol`` of a zero of ``f``.

    Raises
    ------
    ValueError
        If ``a >= b`` or if ``f(a)`` and ``f(b)`` have the same strict sign.

    Examples
    --------
    >>> round(bisection(lambda x: x * x - 2, 0, 2), 8)
    1.41421356
    """
    if a >= b:
        raise ValueError(f"expected a < b, got a = {a} and b = {b}")
    fa, fb = f(a), f(b)
    if fa == 0:
        return a
    if fb == 0:
        return b
    if (fa > 0) == (fb > 0):
        raise ValueError("f(a) and f(b) have the same sign: no sign change to locate")
    for _ in range(max_iter):
        if b - a < tol:
            break
        m = (a + b) / 2
        fm = f(m)
        if fm == 0:
            return m
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b = m
    return (a + b) / 2
