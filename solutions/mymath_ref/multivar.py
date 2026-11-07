"""Functions of several variables: partial and directional derivatives, steepest ascent, tangent plane (M05b).

Reference implementation (solutions/mymath_ref).
Do not use SymPy nor ``numpy.gradient``: the tests compare your results with them. A function ``f`` of several
variables takes **one** argument, a NumPy array of floats ``p`` (``p[0]`` is x, ``p[1]`` is y…), and returns a
number, e.g. ``lambda p: p[0] ** 2 + 3 * p[1]``. Numbers are returned as Python ``float``, vectors as NumPy arrays.
"""

import math

import numpy as np


def _check_step(h):
    if not h > 0:                                       # refuses nan too
        raise ValueError(f"the step h must be positive, got {h!r}")


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
    p = np.array(point, dtype=float)                    # a copy in floats: the caller's point never changes
    if not 0 <= i < p.size:
        raise ValueError(f"i must be between 0 and {p.size - 1}, got {i!r}")
    _check_step(h)
    step = np.zeros_like(p)
    step[i] = h                                         # move only coordinate i
    return float((f(p + step) - f(p - step)) / (2 * h))


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
    p = np.array(point, dtype=float)
    d = np.array(direction, dtype=float)
    if d.shape != p.shape:
        raise ValueError(f"point and direction must have the same length, got {p.size} and {d.size}")
    norm = math.sqrt(float(np.dot(d, d)))
    if norm == 0:
        raise ValueError("the direction is the zero vector: it gives no direction")
    _check_step(h)
    u = d / norm                                        # the unit vector of the direction
    return float((f(p + h * u) - f(p - h * u)) / (2 * h))   # one centred difference along u


def _gradient(f, point, h):
    p = np.array(point, dtype=float)
    return np.array([partial_derivative(f, p, i, h) for i in range(p.size)])


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
    _check_step(h)
    grad = _gradient(f, point, h)
    norm = float(np.linalg.norm(grad))
    if norm < 1e-8:
        raise ValueError(f"the gradient is (almost) zero at {tuple(point)}: no direction of steepest ascent")
    return grad / norm


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
    p = np.array(point, dtype=float)
    if p.shape != (2,):
        raise ValueError(f"the tangent plane needs a point (x0, y0) with two coordinates, got {p.size}")
    _check_step(h)
    a = partial_derivative(f, p, 0, h)
    b = partial_derivative(f, p, 1, h)
    c = float(f(p)) - a * p[0] - b * p[1]              # z = f(p) + a (x - x0) + b (y - y0), expanded
    return float(a), float(b), float(c)
