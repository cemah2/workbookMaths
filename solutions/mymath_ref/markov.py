"""Markov chains and Bellman equations: the law of a chain after n steps, its stationary law, and the values of a
fixed policy, solved as a linear system or approached by iterating the Bellman operator (chapter M26).

Conventions. The chain has ``m`` states ``0, …, m - 1``. A transition matrix ``P`` is a square ``(m, m)`` array with
entries ``≥ 0``: ``P[i, j]`` is the probability of moving from ``i`` to ``j`` in one step.

- A **law** (a probability distribution over the states) is a 1-D array read as a **row**: the law after one more
  step is ``mu @ P`` (the probabilists' convention; M22 wrote ``x_{t+1} = A x_t`` in columns, and ``mu @ P`` is
  that recurrence for ``A = Pᵀ``).
- A **value** (a number per state) is a 1-D array read as a **column**: ``(P @ V)[i] = Σ_j P[i, j] V[j]`` is the
  expectation of ``V`` at the next state, starting from ``i``.

In ``n_step_distribution`` and ``stationary_distribution``, ``P`` is **stochastic**: every row sums to 1, within
``1e-9``. In the two Bellman functions, ``P`` may also be **substochastic**: every row sums to at most ``1 + 1e-9``,
and the missing mass ``1 - Σ_j P[i, j]`` is the probability that the process **ends** after state ``i`` (nothing is
collected afterwards). For ``γ < 1``, an absorbing state with a zero reward gives the same values as a row that
ends. For ``γ = 1``, an end must be coded by rows that end (an absorbing state makes ``I - P`` singular), and the
process must end for sure from every state.

``concentration.markov_bound`` (M11) is Markov's inequality: the same mathematician, another subject.

Reference implementation (solutions/mymath_ref).
NumPy is allowed, but from ``np.linalg`` only ``solve`` and ``matrix_rank``, in ``stationary_distribution`` and
``bellman_linear_solve``; not ``np.linalg.matrix_power``, ``eig``, ``eigvals`` nor ``inv``, and no SciPy at all: the
tests compare your results with them. Never modify the arrays you receive. Vectors and matrices are returned as
``numpy.ndarray`` of floats.
"""

import math
import numbers

import numpy as np

SUM_TOLERANCE = 1e-9          # rows of P and laws sum to 1 (or, for a substochastic P, to at most 1) up to this


def _float_array(values, what):
    """values as a NEW float array (never a view of what was received), or ValueError."""
    try:
        return np.array(values, dtype=float)
    except (TypeError, ValueError):
        raise ValueError(f"{what} must be an array of numbers, got {values!r}") from None


def _transition(P, substochastic=False):
    """Check P: a square (m, m) array, m ≥ 1, of finite entries ≥ 0, whose rows sum to 1 (stochastic) or to at most
    1 (substochastic), up to SUM_TOLERANCE. Returns a new float array."""
    matrix = _float_array(P, "P")
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.shape[0] == 0:
        raise ValueError(f"P must be a square (m, m) matrix with m >= 1, got shape {matrix.shape}")
    if not np.all(np.isfinite(matrix)):
        raise ValueError("P must hold finite numbers only (no nan, no inf)")
    if np.any(matrix < 0):
        raise ValueError("P must hold probabilities >= 0 only")
    sums = np.sum(matrix, axis=1)
    if substochastic:
        bad = np.flatnonzero(sums > 1.0 + SUM_TOLERANCE)
        if bad.size:
            raise ValueError(f"each row of P must sum to at most 1 (up to {SUM_TOLERANCE}): row {int(bad[0])} sums "
                             f"to {float(sums[bad[0]])!r}")
    else:
        bad = np.flatnonzero(np.abs(sums - 1.0) > SUM_TOLERANCE)
        if bad.size:
            raise ValueError(f"each row of P must sum to 1 (up to {SUM_TOLERANCE}): row {int(bad[0])} sums to "
                             f"{float(sums[bad[0]])!r}")
    return matrix


def _law(mu0, m):
    """Check the initial law: m finite entries ≥ 0 whose sum is 1, up to SUM_TOLERANCE. Returns a new float array."""
    mu = _float_array(mu0, "mu0")
    if mu.shape != (m,):
        raise ValueError(f"mu0 must be a 1-D array of {m} entries (one per state of P), got shape {mu.shape}")
    if not np.all(np.isfinite(mu)):
        raise ValueError("mu0 must hold finite numbers only (no nan, no inf)")
    if np.any(mu < 0):
        raise ValueError("mu0 must hold probabilities >= 0 only")
    total = float(np.sum(mu))
    if abs(total - 1.0) > SUM_TOLERANCE:
        raise ValueError(f"mu0 must sum to 1 (up to {SUM_TOLERANCE}), got a sum of {total!r}")
    return mu


def _vector(values, m, what):
    """Check a 1-D array of m numbers (rewards or values). Returns a new float array."""
    vector = _float_array(values, what)
    if vector.shape != (m,):
        raise ValueError(f"{what} must be a 1-D array of {m} entries (one per state of P), got shape {vector.shape}")
    return vector


def _count(n, what):
    """n must be an integer ≥ 0: a Python or NumPy integer, not a bool nor a float such as 2.0."""
    if isinstance(n, (bool, np.bool_)) or not isinstance(n, numbers.Integral) or n < 0:
        raise ValueError(f"{what} must be an integer >= 0 (not a bool, not a float), got {n!r}")
    return int(n)


def _discount(gamma):
    """gamma must be a real number in [0, 1], not a bool. Returns it as a Python float."""
    if (isinstance(gamma, (bool, np.bool_)) or not isinstance(gamma, numbers.Real) or not math.isfinite(gamma)
            or not 0 <= gamma <= 1):
        raise ValueError(f"gamma must be a number in [0, 1] (not a bool), got {gamma!r}")
    return float(gamma)


def n_step_distribution(P, mu0, n):
    """Return the law ``μ_n = μ_0 Pⁿ`` of a Markov chain after ``n`` steps, from the initial law ``μ_0``.

    One step is the law of total probability (M03): ``μ_{k+1}[j] = Σ_i μ_k[i] P[i, j]``, a sum over the state ``i``
    where the chain was. Each ``μ_k`` is a law (entries ``≥ 0``, sum 1). When ``μ_0`` is the ``i``-th vector of the
    canonical basis (the chain starts in ``i`` for sure), ``μ_n`` is the row ``i`` of ``Pⁿ``. In the column
    convention of M22, it is the recurrence ``x_{k+1} = Pᵀ x_k``, without input (``linear_system_states``).

    Parameters
    ----------
    P : 2-D array-like
        A stochastic ``(m, m)`` matrix, ``m ≥ 1``.
    mu0 : 1-D array-like
        The initial law: ``m`` entries ``≥ 0`` whose sum is 1, within ``1e-9``.
    n : int
        The number of steps, an integer ``≥ 0`` (a NumPy integer is accepted; a bool, or a float such as ``2.0``,
        is refused).

    Returns
    -------
    numpy.ndarray
        The ``m`` entries of ``μ_n`` (for ``n = 0``, those of ``μ_0``, as floats).

    Raises
    ------
    ValueError
        If ``P`` is not a square stochastic matrix, if ``mu0`` is not a law with ``m`` entries, or if ``n`` is not an
        integer ``≥ 0``.

    Examples
    --------
    >>> P = [[0.5, 0.5, 0.0], [0.25, 0.5, 0.25], [0.0, 0.5, 0.5]]
    >>> n_step_distribution(P, [1, 0, 0], 2)
    array([0.375, 0.5  , 0.125])
    >>> n_step_distribution(P, [0, 0, 1], 0)
    array([0., 0., 1.])
    """
    matrix = _transition(P)
    mu = _law(mu0, matrix.shape[0])
    steps = _count(n, "n")
    # μ Pⁿ by squaring: P, P², P⁴, P⁸…, and μ is multiplied by P^(2^k) for each binary digit 1 of n (the powers of P
    # commute, so the order of the products does not matter): about log₂ n products instead of n.
    power = matrix
    while steps:
        if steps & 1:
            mu = mu @ power                      # a row times a matrix: the law convention
        steps >>= 1
        if steps:
            power = power @ power
    return mu


def stationary_distribution(P):
    """Return the stationary law ``π`` of a Markov chain: ``π P = π``, ``π ≥ 0`` and ``Σ_j π_j = 1``.

    One step of the chain does not change ``π``: if ``S_0`` follows ``π``, so does every ``S_k``. A stationary law
    always exists (``P 1 = 1``, so 1 is an eigenvalue of ``P`` and of ``Pᵀ``; the Perron-Frobenius theorem, admitted,
    gives an eigenvector ``≥ 0``). It is unique when the chain has a single closed class, for example when it is
    irreducible (every state can reach every other one), even if it is periodic.

    It solves a linear system: the ``m`` equations of ``(Pᵀ - I) πᵀ = 0`` add up to ``0 = 0``, so one of them is
    redundant; replacing the last one by ``Σ_j π_j = 1`` gives a square system, which is invertible exactly when
    ``π`` is unique.

    Parameters
    ----------
    P : 2-D array-like
        A stochastic ``(m, m)`` matrix, ``m ≥ 1``.

    Returns
    -------
    numpy.ndarray
        The ``m`` entries of ``π``. Negative entries due to rounding are set to 0, then ``π`` is divided by its sum.

    Raises
    ------
    ValueError
        If ``P`` is not a square stochastic matrix, or if the stationary law is not unique (the square system above
        is singular according to ``np.linalg.matrix_rank`` with its default tolerance).

    Examples
    --------
    >>> stationary_distribution([[0.6, 0.4], [0.2, 0.8]])
    array([0.33333333, 0.66666667])
    >>> stationary_distribution([[0, 1], [1, 0]])          # periodic, but π is unique
    array([0.5, 0.5])
    >>> stationary_distribution([[1, 0], [0, 1]])          # two closed classes
    Traceback (most recent call last):
        ...
    ValueError: the stationary law is not unique
    """
    matrix = _transition(P)
    m = matrix.shape[0]
    A = matrix.T - np.eye(m)                     # (Pᵀ - I) πᵀ = 0: equation j is Σ_i π_i P[i, j] - π_j = 0
    A[-1, :] = 1.0                               # the last equation, redundant, becomes Σ_j π_j = 1
    b = np.zeros(m)
    b[-1] = 1.0
    if np.linalg.matrix_rank(A) < m:
        raise ValueError("the stationary law is not unique")
    pi = np.linalg.solve(A, b)
    pi = np.where(pi < 0, 0.0, pi)               # a rounding below 0 (a state of probability 0) is set to 0
    return pi / np.sum(pi)


def bellman_linear_solve(P, r, gamma):
    """Return the values ``V`` of a fixed policy: the solution of the Bellman system ``V = r + γ P V``.

    ``P`` is the transition matrix of the chain that the fixed policy induces, and ``r[i]`` the expected reward
    collected in state ``i``. The value ``V[i] = E[Σ_t γᵗ r(S_t) | S_0 = i]`` adds the rewards collected until the
    process ends (forever if it never ends), discounted by ``γ`` per step. Conditioning on the first step gives the
    Bellman equation ``V = r + γ P V``, the linear system ``(I - γ P) V = r``.

    - For ``γ < 1`` it always has a unique solution: ``‖γ P‖_∞ ≤ γ < 1`` (M22), so ``I - γ P`` is invertible,
      ``(I - γ P)⁻¹ = Σ_t γᵗ Pᵗ`` and ``V = Σ_t γᵗ Pᵗ r``.
    - For ``γ = 1`` (no discount), it has one when the process ends for sure from every state, that is when
      ``I - P`` is invertible (``P`` is then substochastic). With ``r = 1``, ``V[i]`` is the mean number of steps
      before the end, starting from ``i``.

    Parameters
    ----------
    P : 2-D array-like
        A stochastic or substochastic ``(m, m)`` matrix, ``m ≥ 1`` (see the module docstring).
    r : 1-D array-like
        The ``m`` rewards ``r[i]``.
    gamma : float
        The discount factor, ``0 ≤ γ ≤ 1`` (a bool is refused).

    Returns
    -------
    numpy.ndarray
        The ``m`` values ``V[i]``.

    Raises
    ------
    ValueError
        If ``P`` is not a square stochastic or substochastic matrix, if ``r`` is not 1-D with ``m`` entries, if
        ``gamma`` is a bool or is not in ``[0, 1]``, or if ``gamma = 1`` and ``I - P`` is singular according to
        ``np.linalg.matrix_rank`` with its default tolerance (from some state, the process never ends).

    Examples
    --------
    >>> P = [[0.5, 0.5], [0.0, 1.0]]
    >>> bellman_linear_solve(P, [1, 2], 0.75)   # state 1 is absorbing and keeps paying 2: V[1] = 2 / (1 - 0.75)
    array([6.4, 8. ])
    >>> Q = [[0.5, 0.25], [0.5, 0.0]]           # rows summing to 0.75 and 0.5: the process may end
    >>> bellman_linear_solve(Q, [1, 1], 1.0)    # the mean number of steps before the end
    array([3.33333333, 2.66666667])
    >>> bellman_linear_solve(P, [1, 2], 1.0)
    Traceback (most recent call last):
        ...
    ValueError: gamma = 1 and the process never ends from some state
    """
    matrix = _transition(P, substochastic=True)
    m = matrix.shape[0]
    rewards = _vector(r, m, "r")
    g = _discount(gamma)
    M = np.eye(m) - g * matrix                   # (I - γ P) V = r
    if g == 1.0 and np.linalg.matrix_rank(M) < m:
        raise ValueError("gamma = 1 and the process never ends from some state")
    return np.linalg.solve(M, rewards)


def bellman_fixed_point_iterates(P, r, gamma, V0=None, n_steps=10):
    """Return the iterates ``V_0, V_1, …, V_N`` of the Bellman operator ``V ↦ r + γ P V``, one per row.

    ``V_{k+1} = r + γ P V_k``: each step computes every new value from the previous ones (a synchronous sweep). It is
    Richardson's iteration of M19 with the step 1 for ``(I - γ P) V = r``, since ``V + (r - (I - γ P) V) =
    r + γ P V``. For ``γ < 1`` the operator is a ``γ``-contraction for ``‖·‖_∞``: from any start,
    ``‖V_k - V‖_∞ ≤ γᵏ ‖V_0 - V‖_∞``, where ``V`` is the solution of ``bellman_linear_solve``. From ``V_0 = 0``,
    ``V_k = Σ_{t<k} γᵗ Pᵗ r`` is the expected discounted reward of the first ``k`` steps. The function does not check
    the convergence: for ``γ = 1`` and a process that never ends, the iterates grow without bound, and it returns
    them.

    Parameters
    ----------
    P : 2-D array-like
        A stochastic or substochastic ``(m, m)`` matrix, ``m ≥ 1`` (see the module docstring).
    r : 1-D array-like
        The ``m`` rewards ``r[i]``.
    gamma : float
        The discount factor, ``0 ≤ γ ≤ 1`` (a bool is refused).
    V0 : 1-D array-like, optional
        The start, ``m`` values; the zero vector when omitted.
    n_steps : int, default 10
        The number ``N ≥ 0`` of steps (a NumPy integer is accepted; a bool or a float is refused).

    Returns
    -------
    numpy.ndarray
        The ``(N + 1, m)`` array whose row ``k`` is ``V_k`` (row 0 is ``V0``).

    Raises
    ------
    ValueError
        If ``P`` is not a square stochastic or substochastic matrix, if ``r`` or ``V0`` is not 1-D with ``m``
        entries, if ``gamma`` is a bool or is not in ``[0, 1]``, or if ``n_steps`` is not an integer ``≥ 0``.

    Examples
    --------
    >>> bellman_fixed_point_iterates([[0.5, 0.5], [0.0, 1.0]], [1, 2], 0.75, n_steps=3)
    array([[0.      , 0.      ],
           [1.      , 2.      ],
           [2.125   , 3.5     ],
           [3.109375, 4.625   ]])
    """
    matrix = _transition(P, substochastic=True)
    m = matrix.shape[0]
    rewards = _vector(r, m, "r")
    g = _discount(gamma)
    V = np.zeros(m) if V0 is None else _vector(V0, m, "V0")   # a new float array: V0 itself is never written to
    steps = _count(n_steps, "n_steps")
    iterates = np.empty((steps + 1, m))
    iterates[0] = V
    for k in range(steps):
        V = rewards + g * (matrix @ V)           # a synchronous sweep: every V_{k+1}[i] from V_k
        iterates[k + 1] = V
    return iterates
