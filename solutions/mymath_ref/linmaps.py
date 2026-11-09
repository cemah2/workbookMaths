"""Vector spaces and linear maps: independence, column space, kernel, coordinates, change of basis (chapter M12a).

Reference implementation (solutions/mymath_ref).
NumPy is allowed, ``@``, ``.T`` and ``np.linalg.solve`` included, but not ``np.linalg.matrix_rank``,
``np.linalg.svd``, ``np.linalg.qr``, ``np.linalg.lstsq``, ``np.linalg.pinv``, ``np.linalg.inv``, ``scipy.linalg``
nor SymPy: the tests compare your results with them. As in MML, a family of vectors is given as the **columns** of a
matrix (a 2-D array-like, a list of rows). The pivot columns come from the reduced row echelon form computed with
partial pivoting and the tolerance ``tol``, as in your ``rref`` of M09a (you may copy it into a private helper
``_rref``). Never modify the matrix you receive. Vectors and matrices are returned as ``numpy.ndarray`` of floats.
"""

import numpy as np


def _matrix(A, what="A"):
    """A copy of A as a 2-D array of floats (ValueError if A is not 2-D)."""
    arr = np.array(A, dtype=float)
    if arr.ndim != 2:
        raise ValueError(f"{what} must be a 2-D matrix, got an array of shape {arr.shape}")
    return arr


def _rref(A, tol=1e-10):
    """The reduced row echelon form of a copy of A and the tuple of its pivot columns (partial pivoting, as rref of
    M09a): in each column, the row of largest absolute value at or below the current row; a column whose largest
    value is at most tol has no pivot."""
    R = _matrix(A)
    n_rows, n_cols = R.shape
    pivots = []
    row = 0
    for col in range(n_cols):
        if row == n_rows:
            break
        best = row + int(np.argmax(np.abs(R[row:, col])))
        if abs(R[best, col]) <= tol:
            continue
        if best != row:
            R[[row, best]] = R[[best, row]]
        R[row] = R[row] / R[row, col]
        for other in range(n_rows):
            if other != row and R[other, col] != 0.0:
                R[other] = R[other] - R[other, col] * R[row]
        pivots.append(col)
        row += 1
    R[np.abs(R) <= tol] = 0.0
    return R + 0.0, tuple(pivots)


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
    M = _matrix(A)
    _, pivots = _rref(M, tol)
    return len(pivots) == M.shape[1]


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
    M = _matrix(A)
    _, pivots = _rref(M, tol)
    return M[:, list(pivots)].copy() + 0.0


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
    R, pivots = _rref(A, tol)
    n = R.shape[1]
    free = [j for j in range(n) if j not in pivots]
    N = np.zeros((n, len(free)))
    for c, j in enumerate(free):
        N[j, c] = 1.0
        for i, p in enumerate(pivots):
            N[p, c] = -R[i, j]
    return N + 0.0


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
    Bm = _matrix(B, "B")
    vv = np.array(v, dtype=float)
    if vv.ndim != 1 or Bm.shape[0] != vv.shape[0]:
        raise ValueError(f"B of shape {Bm.shape} needs a vector v of length {Bm.shape[0]}, got the shape {vv.shape}")
    if not is_independent(Bm, tol):
        raise ValueError("the columns of B are linearly dependent: they are not a basis")
    c = np.linalg.solve(Bm.T @ Bm, Bm.T @ vv)
    if np.linalg.norm(Bm @ c - vv) > tol * max(1.0, float(np.linalg.norm(vv))):
        raise ValueError("v is not in the span of the columns of B")
    return c + 0.0


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
    Am = _matrix(A, "A")
    Sm = _matrix(S, "S")
    Tm = Sm if T is None else _matrix(T, "T")
    m, n = Am.shape
    if Sm.shape != (n, n):
        raise ValueError(f"S must be ({n}, {n}) for A of shape {Am.shape}, got {Sm.shape}")
    if Tm.shape != (m, m):
        raise ValueError(f"T must be ({m}, {m}) for A of shape {Am.shape}, got {Tm.shape}")
    if not is_independent(Sm) or not is_independent(Tm):
        raise ValueError("S and T must be invertible: their columns must be bases")
    try:
        return np.linalg.solve(Tm, Am @ Sm) + 0.0
    except np.linalg.LinAlgError as exc:   # not reached after the checks above, kept as the docstring asks
        raise ValueError(f"S and T must be invertible: {exc}") from exc
