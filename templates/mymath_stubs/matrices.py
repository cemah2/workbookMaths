"""Matrices and linear systems: product, transpose, reduced row echelon form, rank, solve, inverse (chapter M09a).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m09a_matrices.py``.
NumPy arrays are allowed, with element-wise operations (``+``, ``-``, ``*`` between rows, broadcasting, ``np.sum``),
but not ``@``, ``np.dot``, ``np.matmul``, ``np.einsum``, ``.T``, ``np.transpose`` nor ``np.linalg``: the tests compare
your results with them, and with SymPy's ``Matrix.rref``. A matrix is a 2-D array-like (a list of rows or an
array). Matrices and vectors are returned as ``numpy.ndarray`` of floats, numbers as Python ``int``. Never modify
the matrix you receive: work on a copy (``np.array(A, dtype=float)`` copies).
"""


def matmul(A, B):
    """Return the matrix product ``AB`` of an ``(n, p)`` matrix and a ``(p, m)`` matrix.

    ``(AB)[i, j] = Σ_k A[i, k] B[k, j]`` : the dot product of row ``i`` of ``A`` with column ``j`` of ``B``.

    Parameters
    ----------
    A, B : 2-D array-like
        Matrices whose shapes are compatible: as many columns in ``A`` as rows in ``B``.

    Returns
    -------
    numpy.ndarray
        The ``(n, m)`` product, of floats.

    Raises
    ------
    ValueError
        If ``A`` or ``B`` is not 2-D, or if the shapes are not compatible.

    Examples
    --------
    >>> matmul([[1, 2], [3, 4]], [[5], [6]])
    array([[17.],
           [39.]])
    >>> matmul([[1, 2, 3]], [[1], [0], [-1]])
    array([[-2.]])
    """
    # TODO: an (n, m) array of zeros, then one dot product (np.sum of a product) per entry.
    raise NotImplementedError("matmul() is not implemented yet")


def transpose(A):
    """Return the transpose ``Aᵀ`` of a matrix: ``Aᵀ[j, i] = A[i, j]``.

    Parameters
    ----------
    A : 2-D array-like
        An ``(n, m)`` matrix.

    Returns
    -------
    numpy.ndarray
        The ``(m, n)`` transpose, of floats.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D.

    Examples
    --------
    >>> transpose([[1, 2, 3], [4, 5, 6]])
    array([[1., 4.],
           [2., 5.],
           [3., 6.]])
    """
    # TODO: an (m, n) array, filled entry by entry (or column by column).
    raise NotImplementedError("transpose() is not implemented yet")


def rref(A, tol=1e-10):
    """Return the reduced row echelon form of ``A`` and its pivot columns.

    Gauss-Jordan elimination, column by column from the left, with partial pivoting: in the current column, take the
    row (at or below the current row) whose entry has the largest absolute value; if that value is at most ``tol``,
    the column has no pivot and you move to the next column. Otherwise swap the rows, divide the pivot row by the
    pivot, and subtract multiples of it from **every** other row so that the pivot is the only non-zero entry of its
    column. Entries at most ``tol`` in absolute value are set to 0 at the end. The reduced form is unique: it does not
    depend on the choices of pivots.

    Parameters
    ----------
    A : 2-D array-like
        Any ``(n, m)`` matrix.
    tol : float, default 1e-10
        Below this absolute value, an entry counts as zero.

    Returns
    -------
    tuple
        ``(R, pivots)``: ``R`` the ``(n, m)`` reduced row echelon form (an array of floats), ``pivots`` the tuple of
        the indices of the pivot columns, in increasing order.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D.

    Examples
    --------
    >>> R, pivots = rref([[1, 2, 3], [2, 4, 7]])
    >>> R
    array([[1., 2., 0.],
           [0., 0., 1.]])
    >>> pivots
    (0, 2)
    """
    # TODO: a copy of A as floats, a current row r = 0, then a loop over the columns (see the docstring).
    raise NotImplementedError("rref() is not implemented yet")


def rank(A, tol=1e-10):
    """Return the rank of ``A``: the number of pivots of its reduced row echelon form.

    Parameters
    ----------
    A : 2-D array-like
        Any matrix.
    tol : float, default 1e-10
        Passed to :func:`rref`.

    Returns
    -------
    int
        Between 0 and ``min(n, m)``.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D.

    Examples
    --------
    >>> rank([[1, 2], [2, 4]])
    1
    >>> rank([[1, 0, 1], [0, 1, 1], [1, 1, 2]])
    2
    """
    # TODO: the number of pivot columns returned by rref.
    raise NotImplementedError("rank() is not implemented yet")


def solve(A, b):
    """Return the solution ``x`` of ``A x = b`` for a square invertible matrix ``A``, by Gaussian elimination.

    Forward elimination with partial pivoting (in each column, the row with the largest absolute value at or below
    the diagonal becomes the pivot row), then back substitution from the last row.

    Parameters
    ----------
    A : 2-D array-like
        An ``(n, n)`` matrix.
    b : 1-D array-like
        A vector of length ``n``.

    Returns
    -------
    numpy.ndarray
        The vector ``x`` of length ``n``, of floats.

    Raises
    ------
    ValueError
        If ``A`` is not square, if ``b`` does not have ``n`` entries, or if ``A`` is singular (a pivot whose absolute
        value is at most 1e-12 times the largest absolute value of ``A``).

    Examples
    --------
    >>> solve([[2, 1], [1, 3]], [3, 5])
    array([0.8, 1.4])
    >>> solve([[0, 1], [1, 0]], [2, 3])
    array([3., 2.])
    """
    # TODO: work on the augmented matrix [A | b]; elimination below each pivot, then back substitution.
    raise NotImplementedError("solve() is not implemented yet")


def inverse(A):
    """Return the inverse of a square invertible matrix, by Gauss-Jordan elimination on ``[A | I]``.

    Parameters
    ----------
    A : 2-D array-like
        An ``(n, n)`` matrix.

    Returns
    -------
    numpy.ndarray
        The ``(n, n)`` matrix ``A⁻¹``, of floats, such that ``A A⁻¹ = A⁻¹ A = I``.

    Raises
    ------
    ValueError
        If ``A`` is not square or is singular (the reduced form of ``[A | I]`` does not start with ``I``).

    Examples
    --------
    >>> inverse([[2, 1], [1, 1]])
    array([[ 1., -1.],
           [-1.,  2.]])
    """
    # TODO: build [A | I] (np.hstack and np.eye are allowed), reduce it with rref, check the left half, keep the right.
    raise NotImplementedError("inverse() is not implemented yet")
