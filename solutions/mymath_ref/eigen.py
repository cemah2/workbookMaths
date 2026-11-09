"""Eigenvalues and symmetric matrices: determinant, power iteration, Rayleigh quotient, positive definiteness,
Cholesky, square root and whitening matrix (chapter M12c).

Reference implementation (solutions/mymath_ref).
NumPy is allowed, ``@``, ``.T``, ``np.linalg.norm`` and ``np.linalg.solve`` included, but not ``np.linalg.det``,
``np.linalg.slogdet``, ``np.linalg.eig``, ``np.linalg.eigvals``, ``np.linalg.cholesky``, ``np.linalg.inv``,
``scipy.linalg`` nor SymPy: the tests compare your results with them. One exception, the spectral theorem being the
tool of the last two functions: ``np.linalg.eigh`` is allowed in ``sqrtm_psd`` and ``whitening_matrix`` only. A
matrix is a 2-D array-like; never modify the one you receive. Numbers are returned as Python ``float`` (``bool`` for
a test, ``int`` for a count), vectors and matrices as ``numpy.ndarray`` of floats. A matrix counts as symmetric when
``|A[i, j] - A[j, i]| ≤ 1e-12 · max(1, max |A|)`` for every entry.
"""

import numpy as np


def _square(A, what="A"):
    """A copy of A as a square 2-D array of floats (ValueError otherwise)."""
    M = np.array(A, dtype=float)
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        raise ValueError(f"{what} must be a square matrix, got an array of shape {M.shape}")
    return M


def _check_symmetric(M, what="A"):
    """ValueError unless |M[i, j] - M[j, i]| <= 1e-12 * max(1, max |M|) for every entry."""
    scale = max(1.0, float(np.max(np.abs(M)))) if M.size else 1.0
    if np.any(np.abs(M - M.T) > 1e-12 * scale):
        raise ValueError(f"{what} must be symmetric")


def _vector(x, n, what="x"):
    """A copy of x as a 1-D array of n floats (ValueError otherwise)."""
    v = np.array(x, dtype=float)
    if v.ndim != 1 or v.shape[0] != n:
        raise ValueError(f"{what} must be a 1-D vector of length {n}, got an array of shape {v.shape}")
    return v


def _fix_sign(v):
    """v or -v: the one whose first entry of largest absolute value is positive."""
    return -v if v[int(np.argmax(np.abs(v)))] < 0 else v



def det(A):
    """Return the determinant of the square matrix ``A``, computed by Gaussian elimination.

    Reduce ``A`` to an upper triangular matrix with partial pivoting (in each column, swap up the row whose entry has
    the largest absolute value): each row swap changes the sign, adding a multiple of a row to another changes
    nothing, and the determinant of a triangular matrix is the product of its diagonal. A column without a non-zero
    pivot means a determinant of 0: return ``0.0`` at once (never ``-0.0``).

    Parameters
    ----------
    A : 2-D array-like
        An ``(n, n)`` matrix, ``n ≥ 1``.

    Returns
    -------
    float
        ``det A``.

    Raises
    ------
    ValueError
        If ``A`` is not square.

    Examples
    --------
    >>> det([[2, 1], [1, 3]])
    5.0
    >>> det([[0, 1], [1, 0]])
    -1.0
    >>> det([[1, 2], [2, 4]])
    0.0
    """
    M = _square(A)
    n = M.shape[0]
    sign = 1.0
    for k in range(n):
        p = k + int(np.argmax(np.abs(M[k:, k])))           # partial pivoting
        if M[p, k] == 0:
            return 0.0                                       # no non-zero pivot in this column
        if p != k:
            M[[k, p]] = M[[p, k]]
            sign = -sign
        M[k + 1:, k:] -= np.outer(M[k + 1:, k] / M[k, k], M[k, k:])
    value = float(sign * np.prod(np.diag(M)))
    return 0.0 if value == 0 else value


def power_iteration(A, x0=None, n_iter=1000, tol=1e-12):
    """Return an eigenvalue of largest absolute value of ``A``, a unit eigenvector, and the number of iterations.

    Start from ``x0`` (a vector of ones when omitted), normalized and given the sign convention below; then repeat
    ``x ← A x / ‖A x‖``, choosing at each step the sign of ``x`` that makes its first entry of largest absolute value
    positive (otherwise ``x`` would flip at every step when the eigenvalue is negative). Stop as soon as
    ``‖x_new - x‖ ≤ tol`` (the first comparison is with the normalized ``x0``), or after ``n_iter`` iterations. The
    eigenvalue is the Rayleigh quotient ``xᵀA x`` of the last unit vector. The method converges when one eigenvalue
    is strictly larger than the others in absolute value and ``x0`` is not orthogonal to its eigenvector; the error
    shrinks like ``|λ₂ / λ₁|ᵏ``.

    Parameters
    ----------
    A : 2-D array-like
        An ``(n, n)`` matrix.
    x0 : 1-D array-like, optional
        The non-zero starting vector; ``np.ones(n)`` when omitted.
    n_iter : int, default 1000
        The maximal number of iterations.
    tol : float, default 1e-12
        The stopping threshold on ``‖x_new - x‖``.

    Returns
    -------
    tuple
        ``(eigenvalue, eigenvector, iterations)``: a ``float``, a unit ``numpy.ndarray`` normalized as above, and the
        ``int`` number of products ``A x`` computed (equal to ``n_iter`` when the tolerance was not reached).

    Raises
    ------
    ValueError
        If ``A`` is not square, if ``x0`` has the wrong length or is zero, or if ``A x`` becomes zero.

    Examples
    --------
    >>> value, vector, iterations = power_iteration([[3, 2], [2, 0]], x0=[2, 1])
    >>> round(value, 12)
    4.0
    >>> vector
    array([0.89442719, 0.4472136 ])
    >>> iterations
    1
    """
    M = _square(A)
    n = M.shape[0]
    x = np.ones(n) if x0 is None else _vector(x0, n, "x0")
    norm = np.linalg.norm(x)
    if norm == 0:
        raise ValueError("x0 must be a non-zero vector")
    x = _fix_sign(x / norm)
    iterations = 0
    for _ in range(n_iter):
        y = M @ x
        iterations += 1
        norm = np.linalg.norm(y)
        if norm == 0:
            raise ValueError("A x became zero: x is in the kernel of A, try another x0")
        x_new = _fix_sign(y / norm)
        converged = np.linalg.norm(x_new - x) <= tol
        x = x_new
        if converged:
            break
    return float(x @ M @ x), x, iterations


def rayleigh_quotient(A, x):
    """Return the Rayleigh quotient ``xᵀA x / xᵀx`` of a square matrix ``A`` and a non-zero vector ``x``.

    For a symmetric ``A``, it lies between the smallest and the largest eigenvalue, and equals an eigenvalue when
    ``x`` is an eigenvector.

    Parameters
    ----------
    A : 2-D array-like
        An ``(n, n)`` matrix.
    x : 1-D array-like
        A non-zero vector of length ``n``.

    Returns
    -------
    float
        The quotient.

    Raises
    ------
    ValueError
        If ``A`` is not square, if ``x`` has the wrong length or is zero.

    Examples
    --------
    >>> rayleigh_quotient([[3, 2], [2, 0]], [1, 0])
    3.0
    >>> rayleigh_quotient([[3, 2], [2, 0]], [2, 1])
    4.0
    """
    M = _square(A)
    v = _vector(x, M.shape[0])
    squared_norm = v @ v
    if squared_norm == 0:
        raise ValueError("x must be a non-zero vector")
    return float(v @ M @ v / squared_norm)


def cholesky(A):
    """Return the lower triangular matrix ``L``, with a positive diagonal, such that ``A = L Lᵀ``.

    Column by column: ``L[j, j] = √(A[j, j] - Σ_{k<j} L[j, k]²)`` and, below the diagonal,
    ``L[i, j] = (A[i, j] - Σ_{k<j} L[i, k] L[j, k]) / L[j, j]``. A quantity under the square root that is not
    strictly positive means that ``A`` is not positive definite.

    Parameters
    ----------
    A : 2-D array-like
        A symmetric positive definite ``(n, n)`` matrix.

    Returns
    -------
    numpy.ndarray
        The ``(n, n)`` matrix ``L``; its entries above the diagonal are exactly 0.

    Raises
    ------
    ValueError
        If ``A`` is not square, not symmetric, or not positive definite.

    Examples
    --------
    >>> cholesky([[4, 2], [2, 5]])
    array([[2., 0.],
           [1., 2.]])
    """
    M = _square(A)
    _check_symmetric(M)
    n = M.shape[0]
    L = np.zeros((n, n))
    for j in range(n):
        pivot = M[j, j] - L[j, :j] @ L[j, :j]
        if not pivot > 0:
            raise ValueError(f"A is not positive definite (pivot {pivot:.3g} in column {j})")
        L[j, j] = np.sqrt(pivot)
        L[j + 1:, j] = (M[j + 1:, j] - L[j + 1:, :j] @ L[j, :j]) / L[j, j]
    return L


def is_positive_definite(A):
    """Tell whether ``A`` is symmetric positive definite: ``xᵀA x > 0`` for every non-zero vector ``x``.

    A symmetric matrix is positive definite exactly when its Cholesky decomposition exists: try ``cholesky``.

    Parameters
    ----------
    A : 2-D array-like
        An ``(n, n)`` matrix.

    Returns
    -------
    bool
        ``True`` if ``A`` is symmetric and positive definite; ``False`` otherwise (a non-symmetric matrix included).

    Raises
    ------
    ValueError
        If ``A`` is not square.

    Examples
    --------
    >>> is_positive_definite([[2, -1], [-1, 2]])
    True
    >>> is_positive_definite([[1, 2], [2, 1]])
    False
    """
    M = _square(A)
    try:
        cholesky(M)
    except ValueError:
        return False
    return True


def sqrtm_psd(A, tol=1e-12):
    """Return the symmetric positive semi-definite square root ``B`` of a symmetric positive semi-definite ``A``.

    By the spectral theorem, ``A = Q Λ Qᵀ`` with ``Q`` orthogonal (``np.linalg.eigh``); then ``B = Q √Λ Qᵀ`` is
    symmetric, positive semi-definite, and ``B B = A``. Eigenvalues between ``-tol · max(1, λ_max)`` and 0 are
    rounding errors and count as 0; a more negative eigenvalue means that ``A`` is not positive semi-definite.

    Parameters
    ----------
    A : 2-D array-like
        A symmetric positive semi-definite ``(n, n)`` matrix.
    tol : float, default 1e-12
        Relative tolerance on the negative eigenvalues.

    Returns
    -------
    numpy.ndarray
        The ``(n, n)`` matrix ``B``.

    Raises
    ------
    ValueError
        If ``A`` is not square, not symmetric, or has an eigenvalue below ``-tol · max(1, λ_max)``.

    Examples
    --------
    >>> sqrtm_psd([[4, 0], [0, 9]])
    array([[2., 0.],
           [0., 3.]])
    >>> sqrtm_psd([[5, 5], [5, 10]])
    array([[2., 1.],
           [1., 3.]])
    """
    M = _square(A)
    _check_symmetric(M)
    eigenvalues, Q = np.linalg.eigh(M)
    if eigenvalues.size and eigenvalues.min() < -tol * max(1.0, float(eigenvalues.max())):
        raise ValueError(f"A is not positive semi-definite (eigenvalue {eigenvalues.min():.3g})")
    B = (Q * np.sqrt(np.clip(eigenvalues, 0.0, None))) @ Q.T
    return (B + B.T) / 2


def whitening_matrix(cov, method="zca"):
    """Return a whitening matrix ``W`` of the covariance matrix ``cov``: ``W cov Wᵀ = I``.

    If a random vector ``X`` has covariance ``cov``, then ``W (X - mean)`` has covariance ``I``: its coordinates are
    uncorrelated, of variance 1. Two choices: ``"zca"``, ``W = cov^(-1/2)`` (symmetric: the inverse of the square
    root, from ``Q Λ Qᵀ`` with ``1 / √λ``, ``np.linalg.eigh``), which changes the data as little as possible; and
    ``"cholesky"``, ``W = L⁻¹`` where ``cov = L Lᵀ`` (lower triangular; solve ``L W = I`` with ``np.linalg.solve``).
    For a data matrix with one example per row, the whitened data are ``(X - mean) @ W.T``.

    Parameters
    ----------
    cov : 2-D array-like
        A symmetric positive definite ``(p, p)`` matrix.
    method : {"zca", "cholesky"}, default "zca"
        The whitening to compute.

    Returns
    -------
    numpy.ndarray
        The ``(p, p)`` matrix ``W``.

    Raises
    ------
    ValueError
        If ``cov`` is not square, not symmetric, or not positive definite (for ``"zca"``, an eigenvalue ``≤ 0``; for
        ``"cholesky"``, a pivot ``≤ 0`` in ``cholesky``), or if ``method`` is unknown.

    Examples
    --------
    >>> whitening_matrix([[4, 0], [0, 25]])
    array([[0.5, 0. ],
           [0. , 0.2]])
    >>> whitening_matrix([[4, 2], [2, 5]], method="cholesky")
    array([[ 0.5 ,  0.  ],
           [-0.25,  0.5 ]])
    """
    if method not in ("zca", "cholesky"):
        raise ValueError(f"unknown method {method!r}: use 'zca' or 'cholesky'")
    M = _square(cov, "cov")
    _check_symmetric(M, "cov")
    if method == "cholesky":
        L = cholesky(M)
        return np.tril(np.linalg.solve(L, np.eye(M.shape[0])))
    eigenvalues, Q = np.linalg.eigh(M)
    if np.any(eigenvalues <= 0):
        raise ValueError(f"cov is not positive definite (eigenvalue {eigenvalues.min():.3g})")
    W = (Q / np.sqrt(eigenvalues)) @ Q.T
    return (W + W.T) / 2
