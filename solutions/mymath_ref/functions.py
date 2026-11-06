"""Functions: polynomials, affine and quadratic functions, composition (chapter R3).

Reference implementation (solutions/mymath_ref).
"""

import math


def polyval(coefficients, x):
    """Evaluate a polynomial at ``x`` with Horner's method.

    Parameters
    ----------
    coefficients : sequence of float
        Coefficients from the highest degree to the constant (as ``numpy.polyval``): ``[2, 0, -1]`` is
        ``2x² − 1``. An empty sequence is the zero polynomial and gives ``0``.
    x : float or numpy.ndarray
        Plain arithmetic also works element-wise on a NumPy array.

    Returns
    -------
    int, float or numpy.ndarray
        An int when the coefficients and ``x`` are ints.

    Examples
    --------
    >>> polyval([2, 0, -1], 3)
    17
    """
    result = 0
    for coefficient in coefficients:
        result = result * x + coefficient
    return result


def affine_from_points(p, q):
    """Return the affine function ``x -> m*x + c`` whose graph goes through two points.

    Parameters
    ----------
    p, q : tuple of (float, float)
        Two points ``(x, y)`` with different abscissas.

    Returns
    -------
    tuple of (float, float)
        ``(m, c)``: the slope and the intercept.

    Raises
    ------
    ValueError
        If the two points have the same abscissa (a vertical line is not the graph of a function).

    Examples
    --------
    >>> affine_from_points((1, 3), (3, 7))
    (2.0, 1.0)
    """
    (x1, y1), (x2, y2) = p, q
    if x1 == x2:
        raise ValueError("the two points have the same abscissa: a vertical line is not the graph of a function")
    m = (y2 - y1) / (x2 - x1)
    return (float(m), float(y1 - m * x1))


def quadratic_roots(a, b, c):
    """Return the real roots of ``a*x**2 + b*x + c``.

    Parameters
    ----------
    a, b, c : float
        ``a`` must not be zero.

    Returns
    -------
    list of float
        The real roots in increasing order: two, one (double root, when the discriminant is exactly 0) or none.
        Tests of a double root use integer coefficients.

    Raises
    ------
    ValueError
        If ``a`` is zero.

    Examples
    --------
    >>> quadratic_roots(1, -3, 2)
    [1.0, 2.0]
    """
    if a == 0:
        raise ValueError("a must not be zero: a*x**2 + b*x + c is not of degree 2")
    delta = b * b - 4 * a * c
    if delta < 0:
        return []
    if delta == 0:
        return [-b / (2 * a)]
    root = math.sqrt(delta)
    return sorted([(-b - root) / (2 * a), (-b + root) / (2 * a)])


def quadratic_vertex(a, b, c):
    """Return the vertex of the parabola ``y = a*x**2 + b*x + c``.

    Parameters
    ----------
    a, b, c : float
        ``a`` must not be zero.

    Returns
    -------
    tuple of (float, float)
        ``(alpha, beta)``: the extremum is reached at ``x = alpha`` and equals ``beta``.

    Raises
    ------
    ValueError
        If ``a`` is zero.

    Examples
    --------
    >>> quadratic_vertex(1, -4, 1)
    (2.0, -3.0)
    """
    if a == 0:
        raise ValueError("a must not be zero: a*x**2 + b*x + c is not of degree 2")
    return (-b / (2 * a), c - b * b / (4 * a))


def compose(f, g):
    """Return the composite function ``f ∘ g``, that is ``x -> f(g(x))``.

    Parameters
    ----------
    f, g : callable
        Functions of one argument.

    Returns
    -------
    callable

    Examples
    --------
    >>> h = compose(lambda t: t + 1, lambda t: 2 * t)
    >>> h(5)
    11
    """
    def composite(x):
        return f(g(x))

    return composite
