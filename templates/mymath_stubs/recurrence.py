"""Vector recurrences and products of matrices: the states of a linear recurrence with an input, the induced norms
of a matrix, and the norms of a long product of matrices with their upper bound (chapter M22).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m22_recurrence.py``.
NumPy is allowed, but from ``np.linalg`` only ``eigvalsh`` (in ``operator_norm``, M12c) and ``norm`` (in
``product_norms``), and no SciPy at all: the tests compare your results with ``np.linalg.norm``,
``np.linalg.matrix_norm``, ``np.linalg.svdvals`` and ``np.linalg.matrix_power``. Never modify the arrays you
receive. Numbers are returned as Python ``float``, vectors and matrices as ``numpy.ndarray`` of floats.
"""


def linear_system_states(A, B, x0, inputs):
    """Return the states ``x_0, x_1, …, x_T`` of the recurrence ``x_{t+1} = A x_t + B u_t``.

    The state ``x_t`` has ``n`` coordinates and the input ``u_t`` has ``m``; ``A`` is ``(n, n)`` and ``B`` is
    ``(n, m)`` (column convention: ``A x_t`` is a product of a matrix by a column). The solution is
    ``x_t = Aᵗ x_0 + Σ_{k<t} A^{t-1-k} B u_k``: the initial state is multiplied by the powers of ``A``, and each
    input is carried forward by them.

    Parameters
    ----------
    A : 2-D array-like
        The ``(n, n)`` transition matrix, ``n ≥ 1``.
    B : 2-D array-like
        The ``(n, m)`` input matrix, ``m ≥ 1``.
    x0 : 1-D array-like
        The ``n`` coordinates of the initial state.
    inputs : 2-D array-like
        The inputs ``u_0, …, u_{T-1}``, one per row, of shape ``(T, m)``; ``T = 0`` (no step) is given as
        ``np.zeros((0, m))``. A 1-D ``inputs`` is refused, even when ``m = 1``.

    Returns
    -------
    numpy.ndarray
        The ``(T + 1, n)`` array whose row ``t`` is ``x_t`` (row 0 is ``x_0``).

    Raises
    ------
    ValueError
        If ``A`` is not square, if ``B`` or ``inputs`` is not 2-D, or if the shapes of ``B``, ``x0`` and
        ``inputs`` do not match ``A``.

    Examples
    --------
    >>> A = [[0.6, 0.3], [0.2, 0.5]]
    >>> B = [[1.0], [2.0]]
    >>> linear_system_states(A, B, [1.0, 0.0], [[0.0], [1.0]])
    array([[1.  , 0.  ],
           [0.6 , 0.2 ],
           [1.42, 2.22]])
    """
    # TODO: check the shapes; then one step at a time: x = A @ x + B @ u, each state stored in a row.
    raise NotImplementedError("linear_system_states() is not implemented yet")


def operator_norm(A, ord=2):
    """Return the norm of the matrix ``A`` induced by the vector norm ``ord``: ``max ‖A x‖ / ‖x‖`` over ``x ≠ 0``.

    - ``ord = 1``: the largest sum of absolute values of a column;
    - ``ord = np.inf``: the largest sum of absolute values of a row;
    - ``ord = 2``: the largest singular value ``s_max`` (M12d), the square root of the largest eigenvalue of
      ``AᵀA``.

    In each case ``‖A x‖ ≤ ‖A‖ ‖x‖`` for every ``x``, with equality for some ``x ≠ 0``. ``A`` may be rectangular.

    Parameters
    ----------
    A : 2-D array-like
        An ``(m, n)`` matrix, ``m, n ≥ 1``.
    ord : {1, 2, np.inf}, default 2

    Returns
    -------
    float
        The induced norm, ``≥ 0``.

    Raises
    ------
    ValueError
        If ``A`` is not 2-D or is empty, or if ``ord`` is not ``1``, ``2`` or ``np.inf`` (a ``bool`` is refused, and
        so is ``"fro"``: the Frobenius norm is not induced by a vector norm).

    Examples
    --------
    >>> operator_norm([[1, -2], [3, 4]], 1)
    6.0
    >>> operator_norm([[1, -2], [3, 4]], np.inf)
    7.0
    >>> round(operator_norm([[1, -2], [3, 4]], 2), 4)
    5.1167
    """
    # TODO: check A and ord; the column sums or the row sums of |A|; for ord = 2, the largest eigenvalue of
    #  A.T @ A (np.linalg.eigvalsh), clipped at 0 against rounding, then its square root.
    raise NotImplementedError("operator_norm() is not implemented yet")


def product_norms(matrices, ord=2):
    """Return the norms of the cumulative products ``P_t = A_t ⋯ A_2 A_1`` and their bound ``‖A_t‖ ⋯ ‖A_1‖``.

    The matrices are applied in the order given, as in a recurrence ``x_t = A_t x_{t-1}``: ``P_t`` multiplies on the
    left, and ``x_t = P_t x_0``. Since an induced norm is sub-multiplicative, ``‖P_t‖ ≤ ‖A_t‖ ⋯ ‖A_1‖``; the gap
    between the two says how much the bound overestimates the product.

    Parameters
    ----------
    matrices : sequence of 2-D array-like
        The ``T ≥ 1`` square matrices ``A_1, …, A_T``, all of the same shape ``(n, n)``.
    ord : {1, 2, np.inf}, default 2
        The induced norm (``np.linalg.norm`` is allowed here).

    Returns
    -------
    tuple
        ``(norms, bounds)``, two 1-D ``numpy.ndarray`` of ``T`` floats: ``norms[t - 1] = ‖P_t‖`` and
        ``bounds[t - 1] = ‖A_t‖ ⋯ ‖A_1‖``.

    Raises
    ------
    ValueError
        If there is no matrix, if a matrix is not square or the shapes differ, or if ``ord`` is not ``1``, ``2`` or
        ``np.inf`` (a ``bool`` is refused).

    Examples
    --------
    >>> norms, bounds = product_norms([[[1, 1], [0, 1]], [[1, 0], [-1, 1]]])
    >>> np.round(norms, 4), np.round(bounds, 4)
    (array([1.618, 1.618]), array([1.618, 2.618]))
    >>> product_norms([[[1, 1], [0, 1]], [[1, 0], [-1, 1]]], ord=1)
    (array([2., 2.]), array([2., 4.]))
    """
    # TODO: check the inputs; P = I, bound = 1; for each A in order: P = A @ P, bound = bound * ‖A‖; store
    #  ‖P‖ and the bound.
    raise NotImplementedError("product_norms() is not implemented yet")
