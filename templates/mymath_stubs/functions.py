"""Functions: polynomials, affine and quadratic functions, composition (chapter R3).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_r3_functions.py``.
"""


def polyval(coefficients, x):
    """Evaluate a polynomial at ``x`` with Horner's method.

    Parameters
    ----------
    coefficients : sequence of float
        Coefficients from the highest degree to the constant (as ``numpy.polyval``): ``[2, 0, -1]`` is
        ``2x² − 1``. An empty sequence is the zero polynomial.
    x : float or numpy.ndarray
        Plain arithmetic also works element-wise on a NumPy array.

    Returns
    -------
    float or numpy.ndarray

    Examples
    --------
    >>> polyval([2, 0, -1], 3)
    17
    """
    # TODO: start from 0; for each coefficient, multiply by x and add the coefficient.
    raise NotImplementedError("polyval() is not implemented yet")


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
    # TODO: the slope is the rate of change between the two points; then use one point to get c.
    raise NotImplementedError("affine_from_points() is not implemented yet")


def quadratic_roots(a, b, c):
    """Return the real roots of ``a*x**2 + b*x + c``.

    Parameters
    ----------
    a, b, c : float
        ``a`` must not be zero.

    Returns
    -------
    list of float
        The real roots in increasing order: two, one (double root) or none.

    Raises
    ------
    ValueError
        If ``a`` is zero.

    Examples
    --------
    >>> quadratic_roots(1, -3, 2)
    [1.0, 2.0]
    """
    # TODO: the discriminant decides how many roots there are.
    raise NotImplementedError("quadratic_roots() is not implemented yet")


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
    # TODO: canonical form a(x − alpha)² + beta.
    raise NotImplementedError("quadratic_vertex() is not implemented yet")


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
    # TODO: define and return a new function; careful with the order (g first).
    raise NotImplementedError("compose() is not implemented yet")
