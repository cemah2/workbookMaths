"""Vector recurrences and products of matrices: the states of a linear recurrence with an input, the induced norms
of a matrix, and the norms of a long product of matrices with their upper bound (chapter M22).

Reference implementation (solutions/mymath_ref).
NumPy is allowed, but from ``np.linalg`` only ``eigvalsh`` (in ``operator_norm``, M12c) and ``norm`` (in
``product_norms``), and no SciPy at all: the tests compare your results with ``np.linalg.norm``,
``np.linalg.matrix_norm``, ``np.linalg.svdvals`` and ``np.linalg.matrix_power``. Never modify the arrays you
receive. Numbers are returned as Python ``float``, vectors and matrices as ``numpy.ndarray`` of floats.
"""

import numbers

import numpy as np

_ORDS = "1, 2 or np.inf"


def _float_array(values, what):
    """values as a NEW float array, or ValueError if they are not numbers (or a ragged list)."""
    try:
        return np.array(values, dtype=float)
    except (TypeError, ValueError):
        raise ValueError(f"{what} must be an array of numbers, got {values!r}") from None


def _matrix(values, what):
    """values as a new non-empty 2-D float array, or ValueError."""
    matrix = _float_array(values, what)
    if matrix.ndim != 2 or matrix.size == 0:
        raise ValueError(f"{what} must be a non-empty 2-D array, got shape {matrix.shape}")
    return matrix


def _check_ord(ord):
    """ord must be 1, 2 or np.inf: a number (a bool is not accepted, nor "fro", which is not an induced norm)."""
    if (isinstance(ord, (bool, np.bool_)) or not isinstance(ord, numbers.Real)
            or ord not in (1, 2, np.inf)):
        raise ValueError(f"ord must be {_ORDS}, got {ord!r}")


def _induced_norm(matrix, ord):
    """The induced norm of a non-empty 2-D float array, ord already checked (no np.linalg.norm here)."""
    absolute = np.abs(matrix)
    if ord == 1:
        return float(np.max(np.sum(absolute, axis=0)))      # the largest column sum
    if ord == np.inf:
        return float(np.max(np.sum(absolute, axis=1)))      # the largest row sum
    # ord = 2: s_max² is the largest eigenvalue of the symmetric positive semi-definite matrix AᵀA
    largest = float(np.linalg.eigvalsh(matrix.T @ matrix)[-1])   # eigvalsh: increasing order
    return float(np.sqrt(largest)) if largest > 0 else 0.0      # a rounding below 0 is clipped at 0


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
    transition = _matrix(A, "A")
    n = transition.shape[0]
    if transition.shape != (n, n):
        raise ValueError(f"A must be a square matrix, got shape {transition.shape}")
    gain = _matrix(B, "B")
    if gain.shape[0] != n:
        raise ValueError(f"B must have {n} rows (one per coordinate of the state), got shape {gain.shape}")
    m = gain.shape[1]
    x = _float_array(x0, "x0")
    if x.shape != (n,):
        raise ValueError(f"x0 must be a 1-D array of {n} coordinates, got shape {x.shape}")
    u = _float_array(inputs, "inputs")
    if u.ndim != 2 or u.shape[1] != m:
        raise ValueError(f"inputs must be a 2-D array of shape (T, {m}), one input per row "
                         f"(np.zeros((0, {m})) for T = 0), got shape {u.shape}")
    T = u.shape[0]
    states = np.empty((T + 1, n))
    states[0] = x
    for t in range(T):
        x = transition @ x + gain @ u[t]       # x_{t+1} = A x_t + B u_t: a NEW array at each step
        states[t + 1] = x
    return states


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
    matrix = _matrix(A, "A")
    _check_ord(ord)
    return _induced_norm(matrix, ord)


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
    if isinstance(matrices, (str, bytes)):
        raise ValueError(f"matrices must be a sequence of square matrices, got {matrices!r}")
    try:
        factors = [_matrix(M, f"matrix {i}") for i, M in enumerate(matrices)]
    except TypeError:                                  # not iterable (a number)
        raise ValueError(f"matrices must be a sequence of square matrices, got {matrices!r}") from None
    if not factors:
        raise ValueError("there must be at least one matrix")
    n = factors[0].shape[0]
    for i, M in enumerate(factors):
        if M.shape != (n, n):
            raise ValueError(f"every matrix must be square of shape ({n}, {n}) like the first one, "
                             f"got shape {M.shape} for matrix {i}")
    _check_ord(ord)
    norms, bounds = np.empty(len(factors)), np.empty(len(factors))
    P, bound = np.eye(n), 1.0
    for t, M in enumerate(factors):
        P = M @ P                                      # P_t = A_t P_{t-1}: the new matrix on the LEFT
        bound *= float(np.linalg.norm(M, ord))         # ‖A_t‖ ⋯ ‖A_1‖, cumulated
        norms[t] = np.linalg.norm(P, ord)
        bounds[t] = bound
    return norms, bounds
