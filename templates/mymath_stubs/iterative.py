"""Curvature and iterative methods: the Hessian by finite differences, the critical step of a symmetric positive
definite matrix, the iterates of Richardson's method for ``A x = b``, and linear recurrences of any order
(chapter M19).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m19_iterative.py``.
NumPy is allowed, and ``np.linalg.eigvalsh`` (the spectral theorem of M12c) in ``critical_step_size`` only; not
``np.linalg.solve``, ``np.linalg.inv``, ``scipy.optimize`` nor ``scipy.sparse.linalg``: the tests compare your
results with them. Never modify the arrays you receive. Numbers are returned as Python ``float``, vectors and
matrices as ``numpy.ndarray`` of floats. A matrix counts as symmetric when
``|A[i, j] - A[j, i]| ≤ 1e-12 · max(1, max |A|)`` for every entry.
"""


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
    # TODO: check x and h; the diagonal with three values of f, the entries above it with four, then mirror them.
    raise NotImplementedError("numerical_hessian() is not implemented yet")


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
    # TODO: check the shape and the symmetry, np.linalg.eigvalsh (increasing order), check the smallest, then
    #  return 2 / the largest.
    raise NotImplementedError("critical_step_size() is not implemented yet")


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
    # TODO: check the shapes, start from x0 (a float copy), apply the step n_steps times, keep every iterate.
    raise NotImplementedError("richardson_iterates() is not implemented yet")


def linear_recurrence(coefficients, initial, n_terms):
    """Return the first ``n_terms`` terms of the linear recurrence ``u_{k+d} = c_1 u_{k+d-1} + … + c_d u_k``.

    ``coefficients = [c_1, …, c_d]`` (``c_1`` multiplies the most recent term) and ``initial = [u_0, …, u_{d-1}]``;
    each new term is the combination of the ``d`` previous ones. Order 1 is the geometric sequence of R5; order 2,
    ``u_{k+2} = p u_{k+1} - q u_k``, has the characteristic polynomial ``r² - p r + q``, whose roots decide whether
    the terms tend to 0.

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
    # TODO: check the arguments, start from the initial values, then each new term Σ c_i u_{k+d-i} (a loop).
    raise NotImplementedError("linear_recurrence() is not implemented yet")
