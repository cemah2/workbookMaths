"""Affine maps in homogeneous coordinates, sums over the paths of a directed graph without cycle, and the variance of
a product of independent variables (chapter M16).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m16_affine.py``.
NumPy is allowed (``@``, ``np.zeros``, ``np.eye``, ``np.hstack``, ``np.vstack`` …), but not ``np.linalg.matrix_power``,
``np.linalg.inv`` nor ``np.linalg.solve`` in ``sum_over_paths``: the tests compare your results with them.
Vectors are rows, as in workbookIA: an affine map of ℝⁿ into ℝᵐ is ``x ↦ x W + b``, with ``W`` of shape ``(n, m)``
and ``b`` of shape ``(m,)`` (MML writes ``W x + b`` with column vectors: the matrix is then the transpose).
Numbers are returned as Python ``float``, matrices as ``numpy.ndarray`` of floats.
"""


def homogeneous_matrix(W, b):
    """Return the ``(n + 1, m + 1)`` matrix of the affine map ``x ↦ x W + b`` in homogeneous coordinates.

    A point ``x`` of ℝⁿ (a row) becomes the row ``[x, 1]`` of ℝⁿ⁺¹. The block matrix ``H = [[W, 0], [b, 1]]``
    (``W`` at the top left, a column of ``n`` zeros at the top right, the row ``b`` then the number ``1`` at the
    bottom) sends ``[x, 1]`` to ``[x W + b, 1]``: the affine map becomes a linear one. Applying first the map of
    ``H1``, then the map of ``H2``, is then multiplying by the product ``H1 @ H2``.

    Parameters
    ----------
    W : 2-D array-like
        The ``(n, m)`` matrix of the linear part.
    b : 1-D array-like
        The ``m`` coordinates of the translation.

    Returns
    -------
    numpy.ndarray
        The ``(n + 1, m + 1)`` matrix ``[[W, 0], [b, 1]]``, of floats.

    Raises
    ------
    ValueError
        If ``W`` is not 2-D, if ``b`` is not 1-D, or if ``len(b) != W.shape[1]``.

    Examples
    --------
    >>> homogeneous_matrix([[2, 0], [0, 3]], [1, -1])
    array([[ 2.,  0.,  0.],
           [ 0.,  3.,  0.],
           [ 1., -1.,  1.]])
    >>> H = homogeneous_matrix([[1], [1]], [0.5])   # (x1, x2) ↦ x1 + x2 + 0.5
    >>> np.array([2.0, 3.0, 1.0]) @ H
    array([5.5, 1. ])
    """
    # TODO: convert W and b to float arrays, check the shapes, then stack [W | 0] on top of [b | 1]
    #  (np.hstack, np.vstack).
    raise NotImplementedError("homogeneous_matrix() is not implemented yet")


def sum_over_paths(weights, source, target):
    """Return the sum, over all directed paths from ``source`` to ``target``, of the product of the weights of their
    edges.

    ``weights[i, j]`` is the weight of the edge ``i → j``, and 0 means no edge. With weights 0 and 1, the result is
    the number of paths. The entry ``(Aᵏ)[i, j]`` is the sum over the paths of exactly ``k`` edges, so the result is
    ``Σ_{k ≥ 1} (Aᵏ)[source, target]``. In a graph of ``n`` nodes without cycle, no path has ``n`` edges or more:
    ``Aⁿ = 0`` and the sum stops at ``k = n - 1`` (for two distinct nodes it is the entry of
    ``(I - A)⁻¹ = I + A + … + Aⁿ⁻¹``). A path has at least one edge: the empty path is not counted, and a path from a
    node to itself would be a cycle, so the result is ``0.0`` when ``source == target``.

    The graph must have no cycle. Test it on the pattern of the non-zero weights (``weights != 0``), not on the
    weights themselves, so that weights of opposite signs along a cycle cannot hide it: the graph has no cycle if and
    only if the ``n``-th power of the pattern is zero; keep the powers of the pattern as booleans (``(B @ P) > 0``),
    so that the counts never overflow.

    Parameters
    ----------
    weights : 2-D array-like
        The ``(n, n)`` matrix of the edge weights.
    source, target : int
        Two nodes, between ``0`` and ``n - 1``.

    Returns
    -------
    float
        The sum over the paths from ``source`` to ``target`` of the products of the weights.

    Raises
    ------
    ValueError
        If ``weights`` is not a square matrix, if a node is out of range, or if the graph has a cycle (the message is
        ``"the graph has a cycle"``).

    Examples
    --------
    >>> A = [[0, 1, 1, 0],
    ...      [0, 0, 1, 1],
    ...      [0, 0, 0, 1],
    ...      [0, 0, 0, 0]]
    >>> sum_over_paths(A, 0, 3)     # 0 → 1 → 3, 0 → 2 → 3, 0 → 1 → 2 → 3
    3.0
    >>> sum_over_paths([[0, 2, 0], [0, 0, 0.5], [0, 0, 0]], 0, 2)
    1.0
    >>> sum_over_paths([[0, 1], [1, 0]], 0, 1)
    Traceback (most recent call last):
        ...
    ValueError: the graph has a cycle
    """
    # TODO: check the shapes and the nodes; detect a cycle with the boolean powers of the pattern; then add up the
    #  entries [source, target] of A, A², …, Aⁿ⁻¹ (one product @ per power).
    raise NotImplementedError("sum_over_paths() is not implemented yet")


def variance_of_product(mean_x, var_x, mean_y, var_y):
    """Return the expectation and the variance of the product ``X Y`` of two independent variables.

    Independence gives ``E[X Y] = E[X] E[Y]``, and also ``E[X² Y²] = E[X²] E[Y²]`` (``X²`` and ``Y²`` are independent
    too); with ``E[X²] = Var(X) + E[X]²``, ``Var(X Y) = E[X²] E[Y²] - (E[X] E[Y])²
    = Var(X) Var(Y) + Var(X) E[Y]² + Var(Y) E[X]²``. It is not ``Var(X) Var(Y)``, unless both means are zero.

    Parameters
    ----------
    mean_x, var_x : float
        The expectation and the variance of ``X``.
    mean_y, var_y : float
        The expectation and the variance of ``Y``.

    Returns
    -------
    tuple
        ``(E[X Y], Var(X Y))``, two ``float``.

    Raises
    ------
    ValueError
        If a variance is negative.

    Examples
    --------
    >>> variance_of_product(2, 1, 3, 4)
    (6.0, 29.0)
    >>> variance_of_product(0, 2, 5, 0)       # Y is the constant 5: Var(5 X) = 25 Var(X)
    (0.0, 50.0)
    """
    # TODO: check the variances, then the two formulas (convert to float).
    raise NotImplementedError("variance_of_product() is not implemented yet")
