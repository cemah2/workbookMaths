"""Constrained optimization and SVM: a quadratic problem under equality constraints (Lagrange), the hinge loss, a
subgradient of the soft-margin SVM objective, and the RBF and polynomial kernels (chapter M13b).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m13b_svm.py``.
NumPy is allowed, ``@``, ``.T``, ``np.linalg.norm`` and ``np.linalg.solve`` included, but not ``scipy.optimize``,
``scipy.spatial``, ``scipy.linalg`` nor scikit-learn: the tests compare your results with them. Beware of the
namesakes of scikit-learn: its ``rbf_kernel`` and ``polynomial_kernel`` take ``gamma = 1 / p`` by default (and
``degree = 3``), and its ``hinge_loss`` takes the labels first. Data have one example per row; SVM labels are ``-1``
or ``+1``. Numbers are returned as Python ``float``, vectors and matrices as ``numpy.ndarray`` of floats.
"""


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
    # TODO: check the shapes, build [[Q, Aᵀ], [A, 0]] and the right-hand side (-c, b), solve, split.
    raise NotImplementedError("lagrange_equality_qp() is not implemented yet")


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
    # TODO: check the inputs, then the mean of np.maximum(0, 1 - y s).
    raise NotImplementedError("hinge_loss() is not implemented yet")


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
    # TODO: the margins y (X w + b), the mask of the points below 1, then J, g_w and g_b.
    raise NotImplementedError("svm_subgradient() is not implemented yet")


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
    # TODO: check the inputs, the squared distances by expansion, clip at 0, then np.exp(-gamma · ...).
    raise NotImplementedError("rbf_kernel() is not implemented yet")


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
    # TODO: check the inputs, then (X Zᵀ + coef0) ** degree.
    raise NotImplementedError("polynomial_kernel() is not implemented yet")
