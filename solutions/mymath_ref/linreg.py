"""Least squares: normal equations, ridge, hat matrix, sums of squares, monomials, Huber loss (chapter M09b).

Reference implementation of templates/mymath_stubs/linreg.py (same signatures, same docstrings, which are the
specification). NumPy only: ``@``, ``.T`` and ``np.linalg.solve``, never an inverse nor ``lstsq``.
"""

import math

import numpy as np


def _design(X):
    """A copy of X as a 2-D array of floats (ValueError if X is not 2-D)."""
    arr = np.array(X, dtype=float)
    if arr.ndim != 2:
        raise ValueError(f"X must be a 2-D design matrix, got an array of shape {arr.shape}")
    return arr


def _targets(y, n, what="y"):
    """A copy of y as a 1-D array of n floats (ValueError otherwise)."""
    arr = np.array(y, dtype=float)
    if arr.ndim != 1 or arr.size != n:
        raise ValueError(f"{what} must be a vector of {n} entries (one per row of X), got the shape {arr.shape}")
    return arr


def normal_equations(X, y):
    """Return the matrix ``XᵀX`` and the vector ``Xᵀy`` of the normal equations ``XᵀX w = Xᵀy``.

    Parameters
    ----------
    X : 2-D array-like
        The ``(n, p)`` design matrix.
    y : 1-D array-like
        The ``n`` targets.

    Returns
    -------
    tuple of numpy.ndarray
        ``(XtX, Xty)``, of shapes ``(p, p)`` and ``(p,)``.

    Raises
    ------
    ValueError
        If ``X`` is not 2-D or if ``y`` does not have one entry per row of ``X``.

    Examples
    --------
    >>> XtX, Xty = normal_equations([[1, -1], [1, 0], [1, 1]], [1, 2, 6])
    >>> XtX
    array([[3., 0.],
           [0., 2.]])
    >>> Xty
    array([9., 5.])
    """
    X = _design(X)
    y = _targets(y, X.shape[0])
    return X.T @ X, X.T @ y


def solve_least_squares(X, y, ridge=0.0):
    """Return the weights ``w`` that solve ``(XᵀX + ridge · I) w = Xᵀy``.

    With ``ridge = 0``, the least squares solution, which minimizes ``‖y - Xw‖²``; with ``ridge > 0``, the ridge
    solution, which minimizes ``‖y - Xw‖² + ridge ‖w‖²``. Every coefficient is penalized, the one of a column of ones
    included.

    Parameters
    ----------
    X : 2-D array-like
        The ``(n, p)`` design matrix.
    y : 1-D array-like
        The ``n`` targets.
    ridge : float, default 0.0
        The penalty ``λ ≥ 0``.

    Returns
    -------
    numpy.ndarray
        The ``p`` weights.

    Raises
    ------
    ValueError
        If the shapes do not match, if ``ridge < 0``, or if the matrix ``XᵀX + ridge · I`` is singular (catch
        ``numpy.linalg.LinAlgError``).

    Examples
    --------
    >>> solve_least_squares([[1, -1], [1, 0], [1, 1]], [1, 2, 6])
    array([3. , 2.5])
    >>> solve_least_squares([[1, -1], [1, 0], [1, 1]], [1, 2, 6], ridge=1.0)
    array([2.25      , 1.66666667])
    """
    ridge = float(ridge)
    if not ridge >= 0:                       # also refuses NaN
        raise ValueError(f"ridge must be at least 0, got {ridge}")
    XtX, Xty = normal_equations(X, y)
    A = XtX + ridge * np.eye(XtX.shape[0])
    try:
        return np.linalg.solve(A, Xty)
    except np.linalg.LinAlgError as exc:
        raise ValueError("the matrix XᵀX + ridge·I is singular: redundant columns, or more columns than rows "
                         "(use ridge > 0)") from exc


def hat_matrix(X):
    """Return the hat matrix ``H = X (XᵀX)⁻¹ Xᵀ``, which maps the targets to the fitted values: ``ŷ = H y``.

    Compute ``(XᵀX)⁻¹ Xᵀ`` by solving ``XᵀX M = Xᵀ`` (``np.linalg.solve`` accepts a matrix as right-hand side), never
    by inverting.

    Parameters
    ----------
    X : 2-D array-like
        An ``(n, p)`` design matrix whose columns are linearly independent (rank ``p``).

    Returns
    -------
    numpy.ndarray
        The ``(n, n)`` matrix ``H``: symmetric, ``H H = H``, trace ``p``.

    Raises
    ------
    ValueError
        If ``X`` is not 2-D or if ``XᵀX`` is singular.

    Examples
    --------
    >>> hat_matrix([[1], [1]])
    array([[0.5, 0.5],
           [0.5, 0.5]])
    """
    X = _design(X)
    try:
        M = np.linalg.solve(X.T @ X, X.T)
    except np.linalg.LinAlgError as exc:
        raise ValueError("XᵀX is singular: the columns of X are not linearly independent") from exc
    return X @ M


def residual_decomposition(y, y_hat):
    """Return the three sums of squares ``(SST, SSE, SSR)`` of a fit, around the mean ``ȳ`` of the targets.

    ``SST = Σ (y_i - ȳ)²`` (total), ``SSE = Σ (ŷ_i - ȳ)²`` (explained), ``SSR = Σ (y_i - ŷ_i)²`` (residual).
    ``SST = SSE + SSR`` when ``ŷ`` comes from least squares with a column of ones; then ``R² = SSE / SST = 1 - SSR /
    SST``.

    Parameters
    ----------
    y, y_hat : 1-D array-like
        The targets and the fitted values, of the same length (at least 1).

    Returns
    -------
    tuple of float
        ``(sst, sse, ssr)``.

    Raises
    ------
    ValueError
        If the lengths differ or are 0.

    Examples
    --------
    >>> residual_decomposition([1, 2, 6], [0.5, 3, 5.5])
    (14.0, 12.5, 1.5)
    """
    y = np.array(y, dtype=float).reshape(-1)
    y_hat = np.array(y_hat, dtype=float).reshape(-1)
    if y.size == 0 or y.size != y_hat.size:
        raise ValueError(f"y and y_hat must have the same positive length, got {y.size} and {y_hat.size}")
    mean = y.mean()
    return (float(np.sum((y - mean) ** 2)), float(np.sum((y_hat - mean) ** 2)), float(np.sum((y - y_hat) ** 2)))


def count_monomials(p, degree, include_constant=False):
    """Return the number of monomials of total degree at most ``degree`` in ``p`` variables.

    It is the number of columns of the polynomial features of degree ``degree``: ``C(p + degree, degree)``, minus 1
    without the constant monomial 1 (``math.comb`` is allowed).

    Parameters
    ----------
    p : int
        Number of variables, at least 1.
    degree : int
        Maximal total degree, at least 0.
    include_constant : bool, default False
        Count the constant monomial 1.

    Returns
    -------
    int

    Raises
    ------
    ValueError
        If ``p < 1`` or ``degree < 0``.

    Examples
    --------
    >>> count_monomials(4, 2)
    14
    >>> count_monomials(4, 2, include_constant=True)
    15
    >>> count_monomials(1, 5)
    5
    """
    if p < 1:
        raise ValueError(f"p must be at least 1, got {p}")
    if degree < 0:
        raise ValueError(f"degree must be at least 0, got {degree}")
    count = math.comb(int(p) + int(degree), int(degree))
    return int(count if include_constant else count - 1)


def huber_loss(residuals, delta=1.0):
    """Return the mean Huber loss of residuals: ``r²/2`` if ``|r| ≤ δ``, ``δ (|r| - δ/2)`` otherwise.

    Quadratic for small residuals (like the MSE), linear for large ones (like the MAE), with the same value and slope
    at ``|r| = δ``.

    Parameters
    ----------
    residuals : 1-D array-like
        At least one residual ``y_i - ŷ_i``.
    delta : float, default 1.0
        The threshold ``δ > 0``.

    Returns
    -------
    float
        Non-negative.

    Raises
    ------
    ValueError
        If ``residuals`` is empty or ``delta <= 0``.

    Examples
    --------
    >>> huber_loss([0.5, -3.0])
    1.3125
    >>> huber_loss([0.5, -3.0], delta=4.0)
    2.3125
    """
    r = np.array(residuals, dtype=float).reshape(-1)
    if r.size == 0:
        raise ValueError("residuals must contain at least one value")
    delta = float(delta)
    if not delta > 0:
        raise ValueError(f"delta must be positive, got {delta}")
    a = np.abs(r)
    losses = np.where(a <= delta, 0.5 * r ** 2, delta * (a - 0.5 * delta))
    return float(np.mean(losses))
