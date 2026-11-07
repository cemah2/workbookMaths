"""Least squares: normal equations, ridge, hat matrix, sums of squares, monomials, Huber loss (chapter M09b).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m09b_linreg.py``.
NumPy is allowed, matrix product ``@``, ``.T`` and ``np.linalg.solve`` included, but not ``np.linalg.lstsq``,
``np.linalg.pinv``, ``np.linalg.inv``, ``scipy.linalg`` nor scikit-learn: the tests compare your results with them.
The design matrix ``X`` has one row per example and one column per feature; it contains a column of ones only if you
put one in (the intercept is then an ordinary coefficient). Numbers are returned as Python ``float`` (or ``int`` for a
count), vectors and matrices as ``numpy.ndarray`` of floats.
"""


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
    # TODO: two matrix products.
    raise NotImplementedError("normal_equations() is not implemented yet")


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
    # TODO: normal_equations, add ridge on the diagonal (np.eye), then np.linalg.solve.
    raise NotImplementedError("solve_least_squares() is not implemented yet")


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
    # TODO: M = np.linalg.solve(XᵀX, Xᵀ), then H = X M.
    raise NotImplementedError("hat_matrix() is not implemented yet")


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
    # TODO: the mean of y, then three sums of squares.
    raise NotImplementedError("residual_decomposition() is not implemented yet")


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
    # TODO: one binomial coefficient (combinations with repetition), minus 1 unless include_constant.
    raise NotImplementedError("count_monomials() is not implemented yet")


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
    # TODO: np.where on |r| ≤ delta, then the mean.
    raise NotImplementedError("huber_loss() is not implemented yet")
