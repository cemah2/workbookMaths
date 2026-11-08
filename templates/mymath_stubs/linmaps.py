"""Vector spaces and linear maps: independence, column space, kernel, coordinates, change of basis (chapter M12a).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m12a_linmaps.py``.
NumPy is allowed, ``@``, ``.T`` and ``np.linalg.solve`` included, but not ``np.linalg.matrix_rank``,
``np.linalg.svd``, ``np.linalg.qr``, ``np.linalg.lstsq``, ``np.linalg.pinv``, ``np.linalg.inv``, ``scipy.linalg``
nor SymPy: the tests compare your results with them. As in MML, a family of vectors is given as the **columns** of a
matrix (a 2-D array-like, a list of rows). The pivot columns come from the reduced row echelon form computed with
partial pivoting and the tolerance ``tol``, as in your ``rref`` of M09a (you may copy it into a private helper
``_rref``). Never modify the matrix you receive. Vectors and matrices are returned as ``numpy.ndarray`` of floats.
"""


def is_independent(A, tol=1e-10):
    """Tell whether the columns of ``A`` are linearly independent.

    The columns are independent exactly when every column of ``A`` is a pivot column: the only solution of
    ``A x = 0`` is then ``x = 0``. A family of more than ``m`` vectors of ``ℝᵐ`` is always dependent.

    Parameters
    ----------
    A : 2-D array-like
        An ``(m, k)`` matrix whose ``k`` columns are the vectors.
    tol : float, default 1e-10
        Below this absolute value, an entry counts as zero during the row reduction.

    Returns
    -------
    bool
        ``True`` if the columns are linearly independent.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D.

    Examples
    --------
    >>> is_independent([[1, 0], [0, 1], [1, 1]])
    True
    >>> is_independent([[1, 2, 3], [1, 0, 1], [0, 1, 1]])
    False
    """
    # TODO: the pivot columns of A (row reduction), then compare their number with the number of columns.
    raise NotImplementedError("is_independent() is not implemented yet")


def column_space_basis(A, tol=1e-10):
    """Return a basis of the column space (the image) of ``A``: its pivot columns.

    The pivot columns of the reduced row echelon form tell which columns of ``A`` itself to keep; their number is
    the rank of ``A``.

    Parameters
    ----------
    A : 2-D array-like
        An ``(m, n)`` matrix.
    tol : float, default 1e-10
        Below this absolute value, an entry counts as zero during the row reduction.

    Returns
    -------
    numpy.ndarray
        The ``(m, r)`` matrix made of the pivot columns of ``A`` (the original columns, not those of the reduced
        form), in increasing order of index; ``r`` is the rank, and the shape is ``(m, 0)`` when ``A`` is zero.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D.

    Examples
    --------
    >>> column_space_basis([[1, 2, 0], [2, 4, 1]])
    array([[1., 0.],
           [2., 1.]])
    """
    # TODO: the pivots of the row reduction, then the corresponding columns of A as floats.
    raise NotImplementedError("column_space_basis() is not implemented yet")


def null_space_basis(A, tol=1e-10):
    """Return a basis of the kernel (null space) of ``A``: the solutions of ``A x = 0``.

    From the reduced row echelon form ``R``, each free column ``j`` (a column without pivot) gives one basis vector
    ``x``: ``x[j] = 1``, the other free entries 0, and for the pivot of row ``i``, in column ``p``,
    ``x[p] = -R[i, j]``. This is the basis that SymPy's ``Matrix.nullspace`` returns, in the same order.

    Parameters
    ----------
    A : 2-D array-like
        An ``(m, n)`` matrix.
    tol : float, default 1e-10
        Below this absolute value, an entry counts as zero during the row reduction.

    Returns
    -------
    numpy.ndarray
        The ``(n, n - r)`` matrix whose columns are the basis vectors, one per free column in increasing order;
        the shape is ``(n, 0)`` when the kernel is ``{0}``.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D.

    Examples
    --------
    >>> null_space_basis([[1, 0, 2], [0, 1, 3]])
    array([[-2.],
           [-3.],
           [ 1.]])
    >>> null_space_basis([[1, 0], [0, 1]]).shape
    (2, 0)
    """
    # TODO: the reduced form and its pivots; then one vector per free column, filled as the docstring says.
    raise NotImplementedError("null_space_basis() is not implemented yet")


def coordinates(B, v, tol=1e-10):
    """Return the coordinates of the vector ``v`` in the basis formed by the columns of ``B``.

    The coordinates are the unique numbers ``c`` with ``B c = v``. ``B`` may have fewer columns than rows: its
    columns are then a basis of the subspace they span, and ``v`` must belong to it. Solve ``BᵀB c = Bᵀv``
    (``np.linalg.solve``), then check that ``B c`` is really ``v``.

    Parameters
    ----------
    B : 2-D array-like
        An ``(m, k)`` matrix with linearly independent columns.
    v : 1-D array-like
        A vector of ``ℝᵐ``.
    tol : float, default 1e-10
        Tolerance of the independence test, and of the check ``‖B c - v‖ ≤ tol · max(1, ‖v‖)``.

    Returns
    -------
    numpy.ndarray
        The ``k`` coordinates.

    Raises
    ------
    ValueError
        If the shapes do not match, if the columns of ``B`` are dependent, or if ``v`` is not in their span.

    Examples
    --------
    >>> coordinates([[1, 1], [1, -1]], [3, 1])
    array([2., 1.])
    >>> coordinates([[1], [2], [2]], [2, 4, 4])
    array([2.])
    """
    # TODO: check the shapes and the independence (is_independent), solve BᵀB c = Bᵀv, check B c = v.
    raise NotImplementedError("coordinates() is not implemented yet")


def change_of_basis(A, S, T=None):
    """Return the matrix ``T⁻¹ A S`` of the linear map ``x ↦ A x`` in new bases.

    The input coordinates are taken in the basis formed by the columns of ``S``, the output coordinates in the basis
    formed by the columns of ``T`` (``T = S`` when omitted, for a map from a space to itself: ``S⁻¹ A S``). Compute
    ``T⁻¹ (A S)`` by solving ``T M = A S``, never by inverting.

    Parameters
    ----------
    A : 2-D array-like
        The ``(m, n)`` matrix of the map in the standard bases.
    S : 2-D array-like
        An invertible ``(n, n)`` matrix: the new basis of the input space.
    T : 2-D array-like, optional
        An invertible ``(m, m)`` matrix: the new basis of the output space; ``S`` when omitted (then ``m = n``).

    Returns
    -------
    numpy.ndarray
        The ``(m, n)`` matrix ``T⁻¹ A S``.

    Raises
    ------
    ValueError
        If the shapes do not match, or if ``S`` or ``T`` is singular (catch ``numpy.linalg.LinAlgError``).

    Examples
    --------
    >>> change_of_basis([[1, 2], [3, 4]], [[1, 1], [0, 1]])
    array([[-2., -4.],
           [ 3.,  7.]])
    """
    # TODO: check the shapes, then np.linalg.solve(T, A @ S); a singular S must raise too.
    raise NotImplementedError("change_of_basis() is not implemented yet")
