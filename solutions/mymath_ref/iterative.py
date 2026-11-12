"""Curvature and iterative methods: the Hessian by finite differences, the critical step of a symmetric positive
definite matrix, the iterates of Richardson's method for ``A x = b`` (an iteration, not the extrapolation
``richardson_derivative`` of M05a: both are named after L. F. Richardson), and linear recurrences of any order
(chapter M19).

Reference implementation (solutions/mymath_ref).
NumPy is allowed, and ``np.linalg.eigvalsh`` (the spectral theorem of M12c) in ``critical_step_size`` only; not
``np.linalg.solve``, ``np.linalg.inv``, ``scipy.optimize`` nor ``scipy.sparse.linalg``: the tests compare your
results with them. Never modify the arrays you receive. Numbers are returned as Python ``float``, vectors and
matrices as ``numpy.ndarray`` of floats. A matrix counts as symmetric when
``|A[i, j] - A[j, i]| ≤ 1e-12 · max(1, max |A|)`` for every entry.
"""

import numbers

import numpy as np


def _float_array(values, what):
    """values as a NEW float array, or ValueError if they are not numbers."""
    try:
        return np.array(values, dtype=float)
    except (TypeError, ValueError):
        raise ValueError(f"{what} must be an array of numbers, got {values!r}") from None


def _square(A):
    """A as a new float (n, n) array, n ≥ 1, or ValueError."""
    matrix = _float_array(A, "A")
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.shape[0] == 0:
        raise ValueError(f"A must be a square matrix, got shape {matrix.shape}")
    return matrix


def _check_count(n, what):
    """n must be an integer ≥ 0 (a bool is not accepted)."""
    if isinstance(n, bool) or not isinstance(n, numbers.Integral) or n < 0:
        raise ValueError(f"{what} must be an integer >= 0, got {n!r}")



def numerical_hessian(f, x, h=1e-4):
    """Return the ``(n, n)`` Hessian of ``f : ℝⁿ → ℝ`` at ``x`` by centered differences.

    On the diagonal, ``(f(x + h e_i) - 2 f(x) + f(x - h e_i)) / h²``; off the diagonal,
    ``(f(x + h e_i + h e_j) - f(x + h e_i - h e_j) - f(x - h e_i + h e_j) + f(x - h e_i - h e_j)) / (4 h²)``, the same
    formula for ``(i, j)`` and ``(j, i)``, so the result is symmetric. The error is in ``O(h²)``, but the rounding
    errors grow like ``ε / h²`` (a second derivative divides by ``h²``): hence a larger step than for a first
    derivative (M05a).

    Parameters
    ----------
    f : callable
        A real function of a 1-D array of ``n`` floats.
    x : 1-D array-like
        The ``n`` coordinates of the point, ``n ≥ 1``.
    h : float, default 1e-4
        The step, ``h > 0``.

    Returns
    -------
    numpy.ndarray
        The symmetric ``(n, n)`` Hessian.

    Raises
    ------
    ValueError
        If ``x`` is not 1-D or is empty, or if ``h ≤ 0``.

    Examples
    --------
    >>> f = lambda v: v[0] ** 2 * v[1] + 3 * v[1] ** 2
    >>> np.round(numerical_hessian(f, [1.0, 2.0]), 4)
    array([[4., 2.],
           [2., 6.]])
    """
    point = _float_array(x, "x")
    if point.ndim != 1 or point.size == 0:
        raise ValueError(f"x must be a non-empty 1-D array, got shape {point.shape}")
    if not h > 0:
        raise ValueError(f"the step h must be > 0, got {h!r}")
    n = point.size
    steps = np.eye(n) * h
    centre = float(f(point.copy()))
    hessian = np.zeros((n, n))
    for i in range(n):
        hessian[i, i] = (float(f(point + steps[i])) - 2.0 * centre + float(f(point - steps[i]))) / h ** 2
        for j in range(i + 1, n):
            value = (float(f(point + steps[i] + steps[j])) - float(f(point + steps[i] - steps[j]))
                     - float(f(point - steps[i] + steps[j])) + float(f(point - steps[i] - steps[j]))) / (4.0 * h ** 2)
            hessian[i, j] = hessian[j, i] = value
    return hessian


def critical_step_size(A):
    """Return the critical step ``2 / λmax`` of a symmetric positive definite matrix ``A``.

    Richardson's iteration ``x ← x + ω (b - A x)`` for ``A x = b`` multiplies the error by ``I - ω A``, whose
    eigenvalues are ``1 - ω λ_i``: it converges from every start if and only if ``0 < ω < 2 / λmax``, where ``λmax``
    is the largest eigenvalue of ``A``.

    Parameters
    ----------
    A : 2-D array-like
        A symmetric positive definite ``(n, n)`` matrix.

    Returns
    -------
    float
        ``2 / λmax``.

    Raises
    ------
    ValueError
        If ``A`` is not square, not symmetric, or not positive definite (its smallest eigenvalue is ``≤ 0``).

    Examples
    --------
    >>> critical_step_size([[7, 2], [2, 4]])     # eigenvalues 3 and 8
    0.25
    >>> critical_step_size([[1, 2], [2, 1]])
    Traceback (most recent call last):
        ...
    ValueError: the matrix is not positive definite
    """
    matrix = _square(A)
    scale = max(1.0, float(np.max(np.abs(matrix))))
    if np.any(np.abs(matrix - matrix.T) > 1e-12 * scale):
        raise ValueError("the matrix is not symmetric")
    eigenvalues = np.linalg.eigvalsh(matrix)          # increasing order
    if eigenvalues[0] <= 0:
        raise ValueError("the matrix is not positive definite")
    return float(2.0 / eigenvalues[-1])


def richardson_iterates(A, b, omega, x0=None, n_steps=10):
    """Return the iterates ``x_0, x_1, …, x_N`` of Richardson's method for ``A x = b``, one per row.

    ``x_{k+1} = x_k + omega (b - A x_k)``: each step corrects ``x`` by a multiple of the residual ``b - A x``. A fixed
    point is a solution of ``A x = b``. The function does not check the convergence: with a step too large the
    iterates blow up, and it returns them.

    Parameters
    ----------
    A : 2-D array-like
        A square ``(n, n)`` matrix.
    b : 1-D array-like
        The ``n`` coordinates of the right-hand side.
    omega : float
        The step.
    x0 : 1-D array-like, optional
        The start, ``n`` coordinates; the zero vector when omitted.
    n_steps : int, default 10
        The number ``N ≥ 0`` of steps.

    Returns
    -------
    numpy.ndarray
        The ``(N + 1, n)`` array whose row ``k`` is ``x_k`` (row 0 is ``x0``).

    Raises
    ------
    ValueError
        If ``A`` is not square, if ``b`` or ``x0`` does not have ``n`` coordinates, or if ``n_steps`` is not an
        integer ``≥ 0``.

    Examples
    --------
    >>> richardson_iterates([[2, 0], [0, 4]], [2, 4], omega=0.25, n_steps=3)
    array([[0.   , 0.   ],
           [0.5  , 1.   ],
           [0.75 , 1.   ],
           [0.875, 1.   ]])
    """
    matrix = _square(A)
    n = matrix.shape[0]
    rhs = _float_array(b, "b")
    if rhs.shape != (n,):
        raise ValueError(f"b must have {n} coordinates, got shape {rhs.shape}")
    x = np.zeros(n) if x0 is None else _float_array(x0, "x0")
    if x.shape != (n,):
        raise ValueError(f"x0 must have {n} coordinates, got shape {x.shape}")
    _check_count(n_steps, "n_steps")
    iterates = np.empty((n_steps + 1, n))
    iterates[0] = x
    for k in range(n_steps):
        x = x + omega * (rhs - matrix @ x)
        iterates[k + 1] = x
    return iterates


def linear_recurrence(coefficients, initial, n_terms):
    """Return the first ``n_terms`` terms of the linear recurrence ``u_{k+d} = c_1 u_{k+d-1} + … + c_d u_k``.

    ``coefficients = [c_1, …, c_d]`` (``c_1`` multiplies the most recent term) and ``initial = [u_0, …, u_{d-1}]``;
    each new term is the combination of the ``d`` previous ones. Order 1 is the geometric sequence of R5; order 2,
    ``u_{k+2} = p u_{k+1} - q u_k``, is ``coefficients = [p, -q]`` (mind the sign of ``q``), and its characteristic
    polynomial ``r² - p r + q`` has roots that decide whether the terms tend to 0.

    Parameters
    ----------
    coefficients : 1-D array-like
        ``[c_1, …, c_d]``, ``d ≥ 1``.
    initial : 1-D array-like
        ``[u_0, …, u_{d-1}]``, ``d`` values.
    n_terms : int
        How many terms to return, ``≥ 0`` (fewer than ``d`` gives the first initial values).

    Returns
    -------
    numpy.ndarray
        ``[u_0, …, u_{n_terms - 1}]``, of floats.

    Raises
    ------
    ValueError
        If ``coefficients`` is empty, if ``initial`` does not have ``d`` values, or if ``n_terms`` is not an integer
        ``≥ 0``.

    Examples
    --------
    >>> linear_recurrence([1, 1], [0, 1], 10)                 # Fibonacci
    array([ 0.,  1.,  1.,  2.,  3.,  5.,  8., 13., 21., 34.])
    >>> linear_recurrence([1, -0.5], [1, 1], 6)               # roots (1 ± i) / 2, of modulus 1/√2
    array([ 1.  ,  1.  ,  0.5 ,  0.  , -0.25, -0.25])
    """
    c = _float_array(coefficients, "coefficients")
    if c.ndim != 1 or c.size == 0:
        raise ValueError(f"coefficients must be a non-empty 1-D array, got shape {c.shape}")
    d = c.size
    start = _float_array(initial, "initial")
    if start.shape != (d,):
        raise ValueError(f"initial must have {d} values (one per coefficient), got shape {start.shape}")
    _check_count(n_terms, "n_terms")
    terms = np.zeros(max(n_terms, d))
    terms[:d] = start
    for k in range(d, n_terms):
        terms[k] = sum(c[i] * terms[k - 1 - i] for i in range(d))     # c_1 multiplies the most recent term
    return terms[:n_terms].copy()
