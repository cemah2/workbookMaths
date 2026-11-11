"""Jacobians by finite differences: the whole matrix column by column, the diagonal Jacobian of an elementwise map with
a single pair of evaluations, and a Jacobian-vector product without forming the matrix (chapter M17).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m17_jacobian.py``.
NumPy is allowed, but neither SymPy nor ``scipy.differentiate``: the tests compare your results with them.
A function ``f`` of these exercises takes a 1-D ``numpy.ndarray`` of floats and returns a 1-D array (a number counts
as an array of length 1); never modify the ``x`` you receive. The Jacobian follows MML §5.3, as workbookIA does: one
row per output, one column per input, ``J[i, j] = ∂f_i/∂x_j``. Matrices and vectors are returned as
``numpy.ndarray`` of floats.
"""


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
    # TODO: check x and h; for each j, a copy of x moved by ±h on coordinate j (np.atleast_1d on the values of f),
    #  the centered difference as column j.
    raise NotImplementedError("numerical_jacobian() is not implemented yet")


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
    # TODO: check x and h, the centered difference of f on x + h and x - h (all the coordinates at once), np.diag.
    raise NotImplementedError("diagonal_jacobian() is not implemented yet")


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
    # TODO: check x, v and h, then the centered difference along v (np.atleast_1d on the values of f).
    raise NotImplementedError("jacobian_vector_product() is not implemented yet")
