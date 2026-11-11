"""Constrained optimization and SVM: a quadratic problem under equality constraints (Lagrange), the hinge loss, a
subgradient of the soft-margin SVM objective, and the RBF and polynomial kernels (chapter M13b).

Reference implementation (solutions/mymath_ref).
NumPy is allowed, ``@``, ``.T``, ``np.linalg.norm`` and ``np.linalg.solve`` included, but not ``scipy.optimize``,
``scipy.spatial``, ``scipy.linalg`` nor scikit-learn: the tests compare your results with them. Beware of the
namesakes of scikit-learn: its ``rbf_kernel`` and ``polynomial_kernel`` take ``gamma = 1 / p`` by default (and
``degree = 3``), and its ``hinge_loss`` takes the labels first. Data have one example per row; SVM labels are ``-1``
or ``+1``. Numbers are returned as Python ``float``, vectors and matrices as ``numpy.ndarray`` of floats.
"""

import numbers

import numpy as np


def _array(x, ndim, what):
    """A copy of x as an array of floats with ndim dimensions (ValueError otherwise)."""
    a = np.asarray(x)
    if a.dtype.kind not in "iuf":
        raise ValueError(f"{what} must be made of numbers, got values of type {a.dtype}")
    a = a.astype(float)
    if a.ndim != ndim:
        raise ValueError(f"{what} must be a {ndim}-D array, got an array of shape {a.shape}")
    return a


def _labels(y, n):
    """A copy of y as a 1-D array of n floats, each -1 or +1 (ValueError otherwise)."""
    labels = _array(y, 1, "y")
    if labels.size != n:
        raise ValueError(f"y must hold one label per example ({n}), got {labels.size}")
    if not np.all((labels == -1) | (labels == 1)):
        raise ValueError("the labels y must be -1 or +1")
    return labels


def _positive(value, what):
    """value as a float > 0 (ValueError otherwise, NaN included)."""
    if isinstance(value, bool) or not isinstance(value, numbers.Real) or not value > 0:
        raise ValueError(f"{what} must be a number > 0, got {value!r}")
    return float(value)


def _two_sets(X, Z):
    """X and Z as 2-D arrays of floats with the same number of columns."""
    A, B = _array(X, 2, "X"), _array(Z, 2, "Z")
    if A.shape[1] != B.shape[1]:
        raise ValueError(f"X and Z must have the same number of columns, got {A.shape[1]} and {B.shape[1]}")
    return A, B



def lagrange_equality_qp(Q, c, A, b):
    """Solve ``min ½ xᵀQ x + cᵀx`` subject to ``A x = b`` by the Lagrange conditions; return ``(x, λ)``.

    With the Lagrangian ``½ xᵀQ x + cᵀx + λᵀ(A x - b)``, a solution satisfies ``Q x + c + Aᵀλ = 0`` and ``A x = b``:
    one linear system for ``(x, λ)``, with the block matrix ``[[Q, Aᵀ], [A, 0]]`` (``np.block``, then
    ``np.linalg.solve``). When ``Q`` is symmetric positive definite and the rows of ``A`` are independent, the system
    has exactly one solution and ``x`` is the minimum.

    Parameters
    ----------
    Q : 2-D array-like
        A symmetric ``(n, n)`` matrix.
    c : 1-D array-like
        A vector of length ``n``.
    A : 2-D array-like
        The ``(m, n)`` matrix of the ``m`` constraints.
    b : 1-D array-like
        The ``m`` right-hand sides.

    Returns
    -------
    tuple of numpy.ndarray
        ``(x, lam)``, of lengths ``n`` and ``m``.

    Raises
    ------
    ValueError
        If the shapes do not match, or if the block matrix is singular (catch ``numpy.linalg.LinAlgError``).

    Examples
    --------
    >>> x, lam = lagrange_equality_qp([[2, 0], [0, 2]], [0, 0], [[1, 1]], [2])
    >>> x
    array([1., 1.])
    >>> lam
    array([-2.])
    """
    Qm, cv, Am, bv = _array(Q, 2, "Q"), _array(c, 1, "c"), _array(A, 2, "A"), _array(b, 1, "b")
    n, m = cv.size, bv.size
    if n == 0 or m == 0:
        raise ValueError("the problem needs at least one variable and one constraint")
    if Qm.shape != (n, n):
        raise ValueError(f"Q must be ({n}, {n}) like c, got {Qm.shape}")
    if Am.shape != (m, n):
        raise ValueError(f"A must be ({m}, {n}) for {m} right-hand sides and {n} variables, got {Am.shape}")
    K = np.block([[Qm, Am.T], [Am, np.zeros((m, m))]])
    try:
        solution = np.linalg.solve(K, np.concatenate([-cv, bv]))
    except np.linalg.LinAlgError as exc:
        raise ValueError(f"the Lagrange system has no unique solution: {exc}") from None
    return solution[:n], solution[n:]


def hinge_loss(scores, y):
    """Return the mean hinge loss ``(1/n) Σ max(0, 1 - y_i s_i)`` of scores ``s`` and labels ``y`` in ``{-1, +1}``.

    A point well classified with a margin (``y s ≥ 1``) costs nothing; inside the margin or misclassified, it costs
    ``1 - y s``.

    Parameters
    ----------
    scores : 1-D array-like
        The scores ``s_i = w · x_i + b``.
    y : 1-D array-like
        The labels, -1 or +1, one per score.

    Returns
    -------
    float
        The mean loss, non-negative.

    Raises
    ------
    ValueError
        If ``scores`` is empty or not 1-D, or if ``y`` does not hold one label -1 or +1 per score.

    Examples
    --------
    >>> hinge_loss([2.0, 0.5, -1.0], [1, 1, 1])
    0.8333333333333334
    """
    s = _array(scores, 1, "scores")
    if s.size == 0:
        raise ValueError("scores must not be empty")
    labels = _labels(y, s.size)
    return float(np.mean(np.maximum(0.0, 1.0 - labels * s)))


def svm_subgradient(w, b, X, y, C=1.0):
    """Return the soft-margin SVM objective and a subgradient: ``J(w, b) = ½‖w‖² + C Σ max(0, 1 - y_i (w · x_i + b))``.

    The hinge is not differentiable where ``y_i (w · x_i + b) = 1``; take the subgradient that counts only the points
    with a margin **strictly** below 1: ``g_w = w - C Σ y_i x_i`` and ``g_b = -C Σ y_i`` over those points.

    Parameters
    ----------
    w : 1-D array-like
        The ``p`` weights.
    b : float
        The bias.
    X : 2-D array-like
        The ``(n, p)`` data.
    y : 1-D array-like
        The ``n`` labels, -1 or +1.
    C : float, default 1.0
        The weight of the hinge term, ``C > 0``.

    Returns
    -------
    tuple
        ``(J, g_w, g_b)``: the objective (``float``), the subgradient with respect to ``w`` (``numpy.ndarray`` of
        length ``p``) and with respect to ``b`` (``float``).

    Raises
    ------
    ValueError
        If the shapes do not match, if the labels are not -1 or +1, or if ``C ≤ 0``.

    Examples
    --------
    >>> J, g_w, g_b = svm_subgradient([1.0, 0.0], 0.0, [[2, 0], [0.5, 1], [-1, 0]], [1, 1, -1])
    >>> J
    1.0
    >>> g_w
    array([ 0.5, -1. ])
    >>> g_b
    -1.0
    """
    wv, Xm = _array(w, 1, "w"), _array(X, 2, "X")
    if Xm.shape[0] == 0 or Xm.shape[1] != wv.size:
        raise ValueError(f"X must be (n, {wv.size}) with n ≥ 1 for {wv.size} weights, got {Xm.shape}")
    if isinstance(b, bool) or not isinstance(b, numbers.Real):
        raise ValueError(f"b must be a number, got {b!r}")
    labels = _labels(y, Xm.shape[0])
    C = _positive(C, "C")
    margins = labels * (Xm @ wv + float(b))
    below = margins < 1
    J = 0.5 * float(wv @ wv) + C * float(np.sum(np.maximum(0.0, 1.0 - margins)))
    g_w = wv - C * (labels[below] @ Xm[below])
    g_b = -C * float(np.sum(labels[below])) + 0.0
    return J, g_w, g_b


def rbf_kernel(X, Z, gamma):
    """Return the RBF (Gaussian) kernel matrix ``K[i, j] = exp(-gamma ‖x_i - z_j‖²)``.

    Expand ``‖x - z‖² = ‖x‖² - 2 x · z + ‖z‖²`` to compute all the squared distances with one matrix product, and
    clip the tiny negative values that rounding can produce to 0.

    Parameters
    ----------
    X : 2-D array-like
        The ``(n, p)`` points ``x_i``.
    Z : 2-D array-like
        The ``(m, p)`` points ``z_j``.
    gamma : float
        The width parameter, ``gamma > 0``.

    Returns
    -------
    numpy.ndarray
        The ``(n, m)`` kernel matrix, with entries in ``[0, 1]`` (``]0, 1]`` in exact arithmetic: far points give 0
        in floats).

    Raises
    ------
    ValueError
        If ``X`` or ``Z`` is not 2-D, if their numbers of columns differ, or if ``gamma ≤ 0``.

    Examples
    --------
    >>> rbf_kernel([[0, 0], [1, 1]], [[0, 0]], gamma=1.0)
    array([[1.        ],
           [0.13533528]])
    """
    A, B = _two_sets(X, Z)
    gamma = _positive(gamma, "gamma")
    squared = np.sum(A ** 2, axis=1)[:, None] - 2.0 * (A @ B.T) + np.sum(B ** 2, axis=1)[None, :]
    return np.exp(-gamma * np.maximum(squared, 0.0))


def polynomial_kernel(X, Z, degree=2, coef0=1.0):
    """Return the polynomial kernel matrix ``K[i, j] = (x_i · z_j + coef0) ** degree``.

    It is the dot product of the images of ``x`` and ``z`` by a feature map of all the monomials of degree at most
    ``degree`` (exactly ``degree`` when ``coef0 = 0``), with suitable coefficients, without ever computing that map.

    Parameters
    ----------
    X : 2-D array-like
        The ``(n, p)`` points ``x_i``.
    Z : 2-D array-like
        The ``(m, p)`` points ``z_j``.
    degree : int, default 2
        A positive integer.
    coef0 : float, default 1.0
        A non-negative constant.

    Returns
    -------
    numpy.ndarray
        The ``(n, m)`` kernel matrix.

    Raises
    ------
    ValueError
        If ``X`` or ``Z`` is not 2-D, if their numbers of columns differ, if ``degree`` is not a positive integer,
        or if ``coef0 < 0``.

    Examples
    --------
    >>> polynomial_kernel([[2, 1]], [[1, 1], [0, 0]])
    array([[16.,  1.]])
    """
    A, B = _two_sets(X, Z)
    if isinstance(degree, bool) or not isinstance(degree, numbers.Integral) or degree < 1:
        raise ValueError(f"degree must be a positive integer, got {degree!r}")
    if isinstance(coef0, bool) or not isinstance(coef0, numbers.Real) or not coef0 >= 0:
        raise ValueError(f"coef0 must be a number ≥ 0, got {coef0!r}")
    return (A @ B.T + float(coef0)) ** int(degree)
