"""Orthogonality: Gram-Schmidt, orthogonal projection, QR decomposition, least squares by QR (chapter M12b).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m12b_orthogonal.py``.
NumPy is allowed, ``@``, ``.T``, ``np.linalg.norm`` and ``np.linalg.solve`` included, but not ``np.linalg.qr``,
``np.linalg.lstsq``, ``np.linalg.pinv``, ``np.linalg.inv``, ``scipy.linalg`` nor scikit-learn: the tests compare
your results with them. As in MML, a family of vectors is given as the **columns** of a matrix. The inner product is
the usual dot product. Never modify the matrix you receive. Vectors and matrices are returned as ``numpy.ndarray`` of
floats.
"""


def gram_schmidt(A, modified=True, tol=1e-10):
    """Return a matrix ``Q`` whose columns are the orthonormal family built from the columns of ``A``.

    Column ``k`` of ``Q`` is column ``k`` of ``A`` minus its projections on the previous columns of ``Q``, divided by
    its norm. The **classical** process (``modified=False``) computes all the projections of the original column
    ``a_k``; the **modified** process (``modified=True``) removes them one by one from the current vector, which is
    the same in exact arithmetic but loses much less orthogonality with floats. Each ``q_k`` has a positive dot
    product with ``a_k``, and ``q_1, …, q_k`` span the same subspace as ``a_1, …, a_k``.

    Parameters
    ----------
    A : 2-D array-like
        An ``(m, n)`` matrix with linearly independent columns (so ``n ≤ m``).
    modified : bool, default True
        Modified (``True``) or classical (``False``) Gram-Schmidt.
    tol : float, default 1e-10
        A vector whose norm, once the projections are removed, is at most ``tol`` times the norm of ``a_k`` means
        that the columns are dependent.

    Returns
    -------
    numpy.ndarray
        The ``(m, n)`` matrix ``Q``, with ``QᵀQ = I``.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D, or if its columns are (numerically) linearly dependent.

    Examples
    --------
    >>> gram_schmidt([[3, 1], [4, 2]])
    array([[ 0.6, -0.8],
           [ 0.8,  0.6]])
    """
    # TODO: a loop over the columns; remove the projections (from a_k, or from the current vector), normalize.
    raise NotImplementedError("gram_schmidt() is not implemented yet")


def project(v, A):
    """Return the orthogonal projection of the vector ``v`` on the column space of ``A``.

    The projection ``p`` is the point of the subspace closest to ``v``: the residual ``v - p`` is orthogonal to every
    column of ``A``. Compute it with an orthonormal basis of that subspace: ``Q = gram_schmidt(A)``, then
    ``p = Q (Qᵀ v)``, the sum of the projections of ``v`` on the columns of ``Q``. The columns of ``A`` need not be
    orthonormal.

    Parameters
    ----------
    v : 1-D array-like
        A vector of ``ℝᵐ``.
    A : 2-D array-like
        An ``(m, k)`` matrix with linearly independent columns.

    Returns
    -------
    numpy.ndarray
        The projection ``p``, a vector of ``ℝᵐ``.

    Raises
    ------
    ValueError
        If the shapes do not match, or if the columns of ``A`` are linearly dependent (``gram_schmidt`` says so).

    Examples
    --------
    >>> project([1, 2, 3], [[1], [1], [1]])
    array([2., 2., 2.])
    >>> project([1, 2, 3], [[1, 0], [0, 1], [0, 0]])
    array([1., 2., 0.])
    """
    # TODO: check the shapes, Q = gram_schmidt(A), then Q @ (Q.T @ v).
    raise NotImplementedError("project() is not implemented yet")


def qr(A):
    """Return the reduced QR decomposition ``A = QR`` computed by Gram-Schmidt.

    ``Q`` is the result of ``gram_schmidt(A)`` (modified) and ``R = QᵀA`` is upper triangular, with a positive
    diagonal: ``R[j, k] = q_j · a_k`` for ``j ≤ k``. With this sign convention the decomposition is unique.

    Parameters
    ----------
    A : 2-D array-like
        An ``(m, n)`` matrix with linearly independent columns.

    Returns
    -------
    tuple of numpy.ndarray
        ``(Q, R)``, of shapes ``(m, n)`` and ``(n, n)``; entries of ``R`` below the diagonal are exactly 0.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D, or if its columns are linearly dependent.

    Examples
    --------
    >>> Q, R = qr([[3, 1], [4, 2]])
    >>> R
    array([[5. , 2.2],
           [0. , 0.4]])
    """
    # TODO: Q = gram_schmidt(A), R = QᵀA, then set the entries below the diagonal to 0 (np.triu).
    raise NotImplementedError("qr() is not implemented yet")


def least_squares_qr(X, y):
    """Return the least squares weights ``w``, minimizing ``‖y - Xw‖²``, computed with the QR decomposition of ``X``.

    With ``X = QR``, the normal equations ``XᵀX w = Xᵀy`` become ``R w = Qᵀy``: a triangular system, solved by back
    substitution from the last row, without ever forming ``XᵀX``.

    Parameters
    ----------
    X : 2-D array-like
        The ``(n, p)`` design matrix, with linearly independent columns.
    y : 1-D array-like
        The ``n`` targets.

    Returns
    -------
    numpy.ndarray
        The ``p`` weights.

    Raises
    ------
    ValueError
        If the shapes do not match, or if the columns of ``X`` are linearly dependent.

    Examples
    --------
    >>> least_squares_qr([[1, -1], [1, 0], [1, 1]], [1, 2, 6])
    array([3. , 2.5])
    """
    # TODO: qr(X), the right-hand side Qᵀy, then back substitution from the last row of R.
    raise NotImplementedError("least_squares_qr() is not implemented yet")
