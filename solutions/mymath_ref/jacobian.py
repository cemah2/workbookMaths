"""Jacobians by finite differences: the whole matrix column by column, the diagonal Jacobian of an elementwise map with
a single pair of evaluations, and a Jacobian-vector product without forming the matrix (chapter M17).

Reference implementation (solutions/mymath_ref).
NumPy is allowed, but neither SymPy nor ``scipy.differentiate``: the tests compare your results with them.
A function ``f`` of these exercises takes a 1-D ``numpy.ndarray`` of floats and returns a 1-D array (a number counts
as an array of length 1); never modify the ``x`` you receive. The Jacobian follows MML §5.3, as workbookIA does: one
row per output, one column per input, ``J[i, j] = ∂f_i/∂x_j``. Matrices and vectors are returned as
``numpy.ndarray`` of floats.
"""

import numbers

import numpy as np


def _point(x, what):
    """A copy of x as a 1-D, non-empty array of floats (ValueError otherwise)."""
    try:
        a = np.array(x, dtype=float)
    except (TypeError, ValueError):
        raise ValueError(f"{what} must be a 1-D array of numbers, got {x!r}") from None
    if a.ndim != 1 or a.size == 0:
        raise ValueError(f"{what} must be a non-empty 1-D array, got shape {a.shape}")
    return a


def _step(h):
    """h as a positive finite float (ValueError otherwise)."""
    if not isinstance(h, numbers.Real) or not np.isfinite(h) or h <= 0:
        raise ValueError(f"h must be a positive number, got {h!r}")
    return float(h)


def _values(f, point):
    """f at a copy of point, as a 1-D array of floats (a number counts as an array of length 1)."""
    y = np.atleast_1d(np.asarray(f(point.copy()), dtype=float))
    if y.ndim != 1:
        raise ValueError(f"the values of f must be 1-D arrays, got shape {y.shape}")
    return y



def numerical_jacobian(f, x, h=1e-5):
    """Return the ``(m, n)`` Jacobian of ``f`` at ``x`` by centered differences, one column per coordinate of ``x``.

    Column ``j`` is ``(f(x + h e_j) - f(x - h e_j)) / (2 h)``, where ``e_j`` is the ``j``-th vector of the canonical
    basis: the derivative of every output along the axis ``j``, with an error in ``O(h²)`` (M05a). The whole matrix
    costs ``2 n`` evaluations of ``f``.

    Parameters
    ----------
    f : callable
        A map of ℝⁿ into ℝᵐ.
    x : 1-D array-like
        The ``n`` coordinates of the point, ``n ≥ 1``.
    h : float, default 1e-5
        The step, ``h > 0``.

    Returns
    -------
    numpy.ndarray
        The ``(m, n)`` Jacobian.

    Raises
    ------
    ValueError
        If ``x`` is not 1-D or is empty, if ``h ≤ 0``, or if the values of ``f`` are not 1-D arrays of the same
        length.

    Examples
    --------
    >>> polar = lambda p: np.array([p[0] * np.cos(p[1]), p[0] * np.sin(p[1])])   # (r, θ) ↦ (x, y)
    >>> np.round(numerical_jacobian(polar, [2.0, 0.0]), 6)
    array([[1., 0.],
           [0., 2.]])
    >>> g = lambda v: np.array([v[0] * v[1], v[0] + 3 * v[1], v[1] ** 2])
    >>> np.round(numerical_jacobian(g, [1.0, 2.0]), 6)
    array([[2., 1.],
           [1., 3.],
           [0., 4.]])
    """
    x = _point(x, "x")
    h = _step(h)
    columns = []
    for j in range(len(x)):
        step = np.zeros_like(x)
        step[j] = h
        plus, minus = _values(f, x + step), _values(f, x - step)
        if plus.shape != minus.shape or (columns and plus.shape != columns[0].shape):
            raise ValueError("the values of f must all have the same length")
        columns.append((plus - minus) / (2 * h))
    return np.column_stack(columns)


def diagonal_jacobian(f, x, h=1e-5):
    """Return the Jacobian at ``x`` of an elementwise map ``f``, a diagonal matrix, with one pair of evaluations.

    When ``f`` applies one function ``g`` of one variable to each coordinate (``f(x)_i = g(x_i)``), output ``i``
    depends on ``x_i`` only: ``J = diag(g'(x_1), …, g'(x_n))``. Moving all the coordinates at once then gives all the
    derivatives together: ``(f(x + h) - f(x - h)) / (2 h)``, computed coordinate by coordinate, is the diagonal, for
    2 evaluations of ``f`` instead of ``2 n``. The function does not check that ``f`` is elementwise: for another map
    the result is wrong (``numerical_jacobian`` tells the difference).

    Parameters
    ----------
    f : callable
        An elementwise map of ℝⁿ into ℝⁿ.
    x : 1-D array-like
        The ``n`` coordinates of the point, ``n ≥ 1``.
    h : float, default 1e-5
        The step, ``h > 0``.

    Returns
    -------
    numpy.ndarray
        The ``(n, n)`` diagonal Jacobian.

    Raises
    ------
    ValueError
        If ``x`` is not 1-D or is empty, if ``h ≤ 0``, or if ``f(x)`` does not have the length of ``x``.

    Examples
    --------
    >>> np.round(diagonal_jacobian(lambda v: v ** 3, [1.0, -2.0, 0.5]), 6)
    array([[ 3.  ,  0.  ,  0.  ],
           [ 0.  , 12.  ,  0.  ],
           [ 0.  ,  0.  ,  0.75]])
    >>> np.round(diagonal_jacobian(np.arctan, [0.0, 1.0]), 6)
    array([[1. , 0. ],
           [0. , 0.5]])
    """
    x = _point(x, "x")
    h = _step(h)
    plus, minus = _values(f, x + h), _values(f, x - h)
    if plus.shape != x.shape or minus.shape != x.shape:
        raise ValueError(f"f(x) must have the length of x, {len(x)}, got {len(plus)}")
    return np.diag((plus - minus) / (2 * h))


def jacobian_vector_product(f, x, v, h=1e-5):
    """Return the product ``J_f(x) v`` without forming the Jacobian: ``(f(x + h v) - f(x - h v)) / (2 h)``.

    ``J_f(x) v`` is the derivative of every output of ``f`` in the direction ``v`` (the directional derivative of
    M05b, for a map with several outputs): 2 evaluations of ``f``, whatever the dimension ``n``, against ``2 n`` for
    the whole Jacobian. The step is taken along ``v``; it suits a vector ``v`` of norm about 1.

    Parameters
    ----------
    f : callable
        A map of ℝⁿ into ℝᵐ.
    x : 1-D array-like
        The ``n`` coordinates of the point, ``n ≥ 1``.
    v : 1-D array-like
        The direction, ``n`` coordinates.
    h : float, default 1e-5
        The step, ``h > 0``.

    Returns
    -------
    numpy.ndarray
        The ``m`` coordinates of ``J_f(x) v``.

    Raises
    ------
    ValueError
        If ``x`` or ``v`` is not 1-D, if they are empty or of different lengths, or if ``h ≤ 0``.

    Examples
    --------
    >>> g = lambda p: np.array([p[0] ** 2 - p[1], p[0] * p[1]])
    >>> np.round(jacobian_vector_product(g, [1.0, 3.0], [1.0, -1.0]), 6)    # J = [[2, -1], [3, 1]]
    array([3., 2.])
    """
    x, v = _point(x, "x"), _point(v, "v")
    if v.shape != x.shape:
        raise ValueError(f"x and v must have the same length, got {len(x)} and {len(v)}")
    h = _step(h)
    plus, minus = _values(f, x + h * v), _values(f, x - h * v)
    if plus.shape != minus.shape:
        raise ValueError("the values of f must all have the same length")
    return (plus - minus) / (2 * h)
