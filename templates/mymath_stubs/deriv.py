"""Limits and derivatives, numerically: rate of change, tangent, bisection (chapter R7).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_r7_deriv.py``.
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
    # TODO: one formula; a zero h is an error.
    raise NotImplementedError("difference_quotient() is not implemented yet")


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
    # TODO: y = f(a) + f'(a)(x − a), then expand.
    raise NotImplementedError("tangent_line() is not implemented yet")


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
    # TODO: keep the half where the sign changes, until the interval is short enough.
    raise NotImplementedError("bisection() is not implemented yet")
