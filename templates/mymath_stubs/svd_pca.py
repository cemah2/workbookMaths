"""SVD and principal component analysis: singular value decomposition, low-rank approximation, pseudo-inverse,
condition number, principal axes and explained variance (chapter M12d).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m12d_svd_pca.py``.
NumPy is allowed, ``@``, ``.T``, ``np.linalg.norm``, ``np.linalg.solve`` and ``np.linalg.eigh`` (the spectral theorem
of M12c) included, but not ``np.linalg.svd``, ``np.linalg.pinv``, ``np.linalg.cond``, ``np.linalg.lstsq``,
``np.linalg.matrix_rank``, ``scipy.linalg`` nor scikit-learn: the tests compare your results with them. A matrix is a
2-D array-like; never modify the one you receive. Numbers are returned as Python ``float``, vectors and matrices as
``numpy.ndarray`` of floats. Sign convention, so that the results are unique when the singular values (the
eigenvalues) are distinct: every right singular vector (a row of ``Vt``) and every principal axis has its first entry
of largest absolute value positive.
"""


def svd(A, tol=1e-6):
    """Return the compact singular value decomposition ``A = U diag(s) Vt``, computed from the eigenvalues of ``AᵀA``.

    ``AᵀA`` is symmetric positive semi-definite: ``np.linalg.eigh`` gives its eigenvalues ``λ`` and orthonormal
    eigenvectors. Clip its tiny negative eigenvalues (rounding errors) to 0, take ``s = √λ`` in decreasing order, and
    keep only the singular values above ``tol · s_max``: their number ``r`` is the numerical rank. The rows of ``Vt``
    are the corresponding eigenvectors (sign convention of the module), and the columns of ``U`` are ``A v_i / s_i``.
    This route squares the condition number: the eigenvalues of ``AᵀA`` carry rounding errors of about
    ``1e-16 · s_max²``, so a small singular value ``s_r`` is only known to about ``1e-16 · s_max² / s_r``, and the
    columns of ``U`` are orthonormal to about ``1e-16 · (s_max / s_r)²`` only (hence the default ``tol``). It is
    simple, but less accurate than the algorithm of ``np.linalg.svd`` when ``A`` is ill-conditioned.

    Parameters
    ----------
    A : 2-D array-like
        An ``(m, n)`` matrix.
    tol : float, default 1e-6
        Singular values at most ``tol`` times the largest one are dropped.

    Returns
    -------
    tuple of numpy.ndarray
        ``(U, s, Vt)``, of shapes ``(m, r)``, ``(r,)`` and ``(r, n)``: ``Vt Vtᵀ = I``, ``UᵀU = I`` (up to the error
        above), ``s`` positive and decreasing. For a zero matrix, ``r = 0``.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D.

    Examples
    --------
    >>> U, s, Vt = svd([[3, 0], [0, -2]])
    >>> s
    array([3., 2.])
    >>> U
    array([[ 1.,  0.],
           [ 0., -1.]])
    >>> Vt
    array([[1., 0.],
           [0., 1.]])
    """
    # TODO: eigh(AᵀA), sort in decreasing order, keep s > tol · s_max, fix the signs of V, then U = A V / s.
    raise NotImplementedError("svd() is not implemented yet")


def low_rank_approximation(A, k):
    """Return the best approximation of ``A`` by a matrix of rank at most ``k``: ``Σ_{i ≤ k} s_i u_i v_iᵀ``.

    Keep the ``k`` largest singular values of ``svd(A)`` (Eckart-Young: no matrix of rank ``k`` is closer to ``A``
    in Frobenius norm, and the squared error is the sum of the squared singular values dropped). If ``A`` has rank at
    most ``k``, the result is ``A`` itself (up to rounding).

    Parameters
    ----------
    A : 2-D array-like
        An ``(m, n)`` matrix.
    k : int
        The rank kept, ``0 ≤ k ≤ min(m, n)``.

    Returns
    -------
    numpy.ndarray
        The ``(m, n)`` approximation.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D, or if ``k`` is not an integer between 0 and ``min(m, n)``.

    Examples
    --------
    >>> low_rank_approximation([[3, 0], [0, 1]], 1)
    array([[3., 0.],
           [0., 0.]])
    """
    # TODO: check k, svd(A), then the product of the first k columns of U, values of s and rows of Vt.
    raise NotImplementedError("low_rank_approximation() is not implemented yet")


def pinv(A, rcond=1e-6):
    """Return the Moore-Penrose pseudo-inverse ``A⁺ = V diag(1/s) Uᵀ`` of ``A``.

    Use ``svd(A, tol=rcond)``: the singular values at most ``rcond · s_max`` are dropped (treated as 0). ``A⁺ b`` is
    the least squares solution of ``A x = b`` of smallest norm; for an invertible matrix, ``A⁺ = A⁻¹``.

    Parameters
    ----------
    A : 2-D array-like
        An ``(m, n)`` matrix.
    rcond : float, default 1e-6
        Relative threshold below which a singular value counts as 0 (see ``svd``).

    Returns
    -------
    numpy.ndarray
        The ``(n, m)`` matrix ``A⁺`` (zero when ``A`` is zero).

    Raises
    ------
    ValueError
        If ``A`` is not 2-D.

    Examples
    --------
    >>> pinv([[1, 1], [1, 1]])
    array([[0.25, 0.25],
           [0.25, 0.25]])
    """
    # TODO: svd(A, tol=rcond), then Vtᵀ diag(1/s) Uᵀ (divide the columns of Vtᵀ by s).
    raise NotImplementedError("pinv() is not implemented yet")


def condition_number(A):
    """Return the condition number ``κ(A) = s_max / s_min`` of ``A`` (2-norm), ``math.inf`` if ``A`` is rank deficient.

    ``s_min`` is the smallest of the ``min(m, n)`` singular values: if ``svd(A)`` keeps fewer than ``min(m, n)`` of
    them, ``A`` does not have full rank and ``κ`` is infinite (so a ``κ`` above about ``1e6`` is seen as infinite:
    ``svd`` cannot tell such a small singular value from a rounding error). A relative error ``ε`` on ``b`` can
    become a relative error ``κ ε`` on the solution of ``A x = b``.

    Parameters
    ----------
    A : 2-D array-like
        An ``(m, n)`` matrix, not zero.

    Returns
    -------
    float
        ``κ(A) ≥ 1``, or ``math.inf``.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D or is zero.

    Examples
    --------
    >>> condition_number([[2, 0], [0, 0.5]])
    4.0
    >>> condition_number([[1, 2], [2, 4]])
    inf
    """
    # TODO: svd(A); infinite if fewer than min(m, n) singular values, else s[0] / s[-1].
    raise NotImplementedError("condition_number() is not implemented yet")


def principal_axes(C, k=None):
    """Return the ``k`` principal axes of a covariance matrix ``C`` and the variance along each of them.

    ``C`` is symmetric positive semi-definite (the covariance matrix of centered data, whatever its convention,
    ``1/n`` or ``1/(n - 1)``). Its eigenvectors (``np.linalg.eigh``), in decreasing order of eigenvalue, are the
    principal axes: the first one is the unit direction ``u`` that maximizes the variance ``uᵀ C u`` (the Rayleigh
    quotient of M12c), the next ones do the same orthogonally to the previous ones, and the variance along an axis is
    its eigenvalue. Centering the data and forming ``C`` are your job, before the call.

    Parameters
    ----------
    C : 2-D array-like
        A symmetric positive semi-definite ``(p, p)`` matrix.
    k : int, optional
        The number of axes, ``1 ≤ k ≤ p``; all ``p`` when omitted.

    Returns
    -------
    tuple of numpy.ndarray
        ``(axes, variances)``: ``axes`` of shape ``(p, k)``, one unit axis per column (sign convention of the
        module), and ``variances`` of shape ``(k,)``, the eigenvalues in decreasing order (a tiny negative eigenvalue
        due to rounding, above ``-1e-12 · max(1, λ_max)``, is returned as 0).

    Raises
    ------
    ValueError
        If ``C`` is not square, not symmetric (within ``1e-12 · max(1, max |C|)``), has an eigenvalue below
        ``-1e-12 · max(1, λ_max)``, or if ``k`` is not an integer between 1 and ``p``.

    Examples
    --------
    >>> axes, variances = principal_axes([[2, 0], [0, 5]])
    >>> axes
    array([[0., 1.],
           [1., 0.]])
    >>> variances
    array([5., 2.])
    """
    # TODO: check C, eigh, sort in decreasing order, keep k, clip the tiny negative eigenvalues, fix the signs.
    raise NotImplementedError("principal_axes() is not implemented yet")


def explained_variance_ratio(variances):
    """Return the share of the total variance carried by each axis: ``variances / Σ variances``.

    Pass **all** the variances (``principal_axes(C)`` without ``k``): the cumulative sums of the result tell how many
    axes keep a given share of the variance.

    Parameters
    ----------
    variances : 1-D array-like
        Non-negative variances (eigenvalues of a covariance matrix), not all zero.

    Returns
    -------
    numpy.ndarray
        The ratios, of sum 1, in the same order.

    Raises
    ------
    ValueError
        If ``variances`` is not 1-D, is empty, has a negative entry, or sums to 0.

    Examples
    --------
    >>> explained_variance_ratio([3, 1])
    array([0.75, 0.25])
    """
    # TODO: check the values, then divide by their sum.
    raise NotImplementedError("explained_variance_ratio() is not implemented yet")
