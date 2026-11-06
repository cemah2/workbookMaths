"""Functions of several variables: partial and directional derivatives, steepest ascent, tangent plane (M05b).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m05b_multivar.py``.
Do not use SymPy nor ``numpy.gradient``: the tests compare your results with them. A function ``f`` of several
variables takes **one** argument, a NumPy array of floats ``p`` (``p[0]`` is x, ``p[1]`` is y…), and returns a
number, e.g. ``lambda p: p[0] ** 2 + 3 * p[1]``. Numbers are returned as Python ``float``, vectors as NumPy arrays.
"""


def partial_derivative(f, point, i, h=1e-5):
    """Approximate the partial derivative of ``f`` with respect to its ``i``-th variable, by a centred difference.

    ``(f(p + h e_i) - f(p - h e_i)) / (2 h)``, where ``e_i`` is the ``i``-th vector of the standard basis.

    Parameters
    ----------
    f : callable
        A function of several variables (see the module docstring).
    point : sequence of float
        The point ``p`` where the derivative is taken.
    i : int
        Index of the variable, from 0 to ``len(point) - 1``.
    h : float, default 1e-5
        The step, positive.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If ``i`` is out of range or ``h <= 0``.

    Examples
    --------
    >>> round(partial_derivative(lambda p: p[0] ** 2 * p[1], (1.0, 3.0), 0), 6)
    6.0
    """
    # TODO: copy the point into a float array, move only coordinate i, by +h then by -h.
    raise NotImplementedError("partial_derivative() is not implemented yet")


def directional_derivative(f, point, direction, h=1e-5):
    """Approximate the derivative of ``f`` at ``point`` in the direction of a vector.

    The direction is first normalised: the result is the derivative along the unit vector
    ``u = direction / ||direction||``, that is ``∇f(p) · u``.

    Parameters
    ----------
    f : callable
        A function of several variables.
    point : sequence of float
    direction : sequence of float
        Same length as ``point``, not the zero vector (it does not need to be a unit vector).
    h : float, default 1e-5
        The step of the centred differences, positive.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If the lengths differ, ``direction`` is the zero vector, or ``h <= 0``.

    Examples
    --------
    >>> round(directional_derivative(lambda p: p[0] + 2 * p[1], (0.0, 0.0), (3, 4)), 6)
    2.2
    """
    # TODO: normalise the direction, then either the dot product with the gradient or one centred difference.
    raise NotImplementedError("directional_derivative() is not implemented yet")


def steepest_ascent_direction(f, point, h=1e-5):
    """Return the unit vector along which ``f`` increases the fastest at ``point``: ``∇f(p) / ||∇f(p)||``.

    Parameters
    ----------
    f : callable
        A function of several variables.
    point : sequence of float
    h : float, default 1e-5
        The step of the centred differences, positive.

    Returns
    -------
    numpy.ndarray
        A unit vector, same length as ``point``.

    Raises
    ------
    ValueError
        If the norm of the gradient is below ``1e-8`` (a critical point has no direction of steepest ascent), or
        if ``h <= 0``.

    Examples
    --------
    >>> steepest_ascent_direction(lambda p: 3 * p[0] + 4 * p[1], (0.0, 0.0)).round(6)
    array([0.6, 0.8])
    """
    # TODO: the gradient (one partial derivative per coordinate), its norm, then divide.
    raise NotImplementedError("steepest_ascent_direction() is not implemented yet")


def tangent_plane(f, point, h=1e-5):
    """Return the tangent plane at ``point`` of the surface ``z = f(x, y)``, as ``z = a x + b y + c``.

    Parameters
    ----------
    f : callable
        A function of **two** variables.
    point : sequence of float
        ``(x0, y0)``.
    h : float, default 1e-5
        The step of the centred differences, positive.

    Returns
    -------
    tuple of float
        ``(a, b, c)``: ``a`` and ``b`` are the two partial derivatives at ``(x0, y0)``, and ``c`` makes the plane go
        through ``(x0, y0, f(x0, y0))``.

    Raises
    ------
    ValueError
        If ``point`` does not have exactly two coordinates, or if ``h <= 0``.

    Examples
    --------
    >>> a, b, c = tangent_plane(lambda p: p[0] ** 2 + p[1] ** 2, (1.0, 2.0))
    >>> round(a, 6), round(b, 6), round(c, 6)
    (2.0, 4.0, -5.0)
    """
    # TODO: z = f(x0, y0) + a (x - x0) + b (y - y0), then expand to find c.
    raise NotImplementedError("tangent_plane() is not implemented yet")
