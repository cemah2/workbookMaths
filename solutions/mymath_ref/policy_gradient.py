"""Score-function estimates of a derivative, the exact gradient of the values of a tabular softmax policy, importance
weights with their effective sample size, and the Bradley-Terry model of pairwise comparisons (chapter MB8).

Conventions.

- A **score** is the derivative of a log-probability with respect to the parameter ``θ`` of a law:
  ``s_θ(x) = ∂_θ ln p_θ(x)``, a number for a scalar ``θ`` and a vector of the shape of ``θ`` otherwise. It is the
  score *in θ*; the score of MB5, ``∇ₓ ln p(x)``, is a derivative in ``x``.
- A Markov decision process (M26) with ``m`` states and ``K`` actions is given as in M26.14: ``P[a, s, t]`` is the
  probability of moving from state ``s`` to state ``t`` under action ``a`` (shape ``(K, m, m)``), ``r[a, s]`` the
  expected reward ``r(s, a) = Σ_t P[a, s, t] R[a, s, t]`` (M26.14 gives the rewards ``R[a, s, s2]`` of each
  transition) of action ``a`` in state ``s`` (shape ``(K, m)``), and a policy is given by its logits, ``logits[s, a]``
  (shape ``(m, K)``, the layout of ``pi[s, a]`` in M26.14). As in ``markov`` (M26), each ``P[a]`` may be
  substochastic: the missing mass of a row is the probability that the process ends. Values are columns.

Reference implementation (solutions/mymath_ref).
NumPy and the module ``math`` are allowed, but from ``np.linalg`` only ``solve`` and ``matrix_rank`` (in
``policy_gradient_exact``), and no SciPy nor scikit-learn (``scipy.optimize``, ``scipy.special``,
``sklearn.linear_model``…): the tests compare your results with exact sums, with finite differences of values
computed by ``np.linalg.solve``, with ``scipy.optimize.minimize`` and with scikit-learn. You may import
``bellman_linear_solve`` from your module of M26 with a relative import (``from .markov import
bellman_linear_solve``). Nothing here draws at random: the functions receive values computed from draws made
elsewhere. Never modify the arrays you receive. Numbers are returned as Python ``float``, vectors and arrays as
``numpy.ndarray`` of floats.
"""

import math
import numbers

import numpy as np

SUM_TOLERANCE = 1e-9          # the rows of each P[a] sum to at most 1 up to this (as in markov, M26)


def _is_bool(value):
    """Whether value is a bool or a NumPy bool (True == 1, but a bool is not a number here)."""
    return isinstance(value, (bool, np.bool_))


def _real(value):
    """Whether value is a real number (a Python or NumPy integer or float), not a bool."""
    return isinstance(value, numbers.Real) and not _is_bool(value)


def _floats(values, what):
    """values as a NEW float array of its own shape (never a view of what was received), or ValueError; strings,
    complex numbers, None and ragged lists are refused. Finiteness is checked by the caller."""
    if values is None or isinstance(values, str):
        raise ValueError(f"{what} must be an array of real numbers, got {values!r}")
    try:
        raw = np.asarray(values)
    except (TypeError, ValueError):             # a ragged list
        raise ValueError(f"{what} must be an array (rows of the same length) of real numbers") from None
    if raw.dtype.kind in "cUSaV":
        raise ValueError(f"{what} must hold real numbers (not strings or complex numbers), got dtype {raw.dtype}")
    try:
        return np.array(raw, dtype=float)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(f"{what} must be an array of real numbers") from None


def _finite(X, what):
    """X itself when all its entries are finite, or ValueError."""
    if not np.all(np.isfinite(X)):
        raise ValueError(f"{what} must hold finite numbers only (no nan, no inf)")
    return X


def score_function_gradient(f_values, scores, baseline=0.0):
    """Return the score-function estimate of ``d/dθ E_θ[f(X)]`` from a sample, and its standard error.

    ``x_1, …, x_n`` are drawn independently from ``p_θ``; you give the values ``f(x_i)`` and the scores
    ``s_i = ∂_θ ln p_θ(x_i)``. When the support of ``p_θ`` does not depend on ``θ``,
    ``d/dθ E_θ[f(X)] = E_θ[f(X) s_θ(X)]`` (MB8 §2), so the mean of the terms ``g_i = (f(x_i) - b_i) s_i`` estimates
    the derivative, where ``b_i`` is a **baseline**:

    - a number ``b``, the same for every draw: since ``E_θ[s_θ(X)] = 0``, the estimate is unbiased whatever ``b``,
      and only its variance depends on ``b`` (``b = 0`` gives the plain estimator);
    - the string ``"leave-one-out"``: ``b_i`` is the mean of the ``n - 1`` other values ``f(x_j)``, ``j ≠ i``. It
      does not depend on ``x_i``, so the estimate is unbiased too.

    A number computed from the whole sample, ``x_i`` included (``baseline=float(np.mean(f_values))``), is accepted
    as a constant, but the estimate is then biased: that baseline depends on each ``x_i`` (MB8 §3).

    ``f`` need not be differentiable, nor even continuous: ``f(x) = 1{x > c}`` is allowed, and it is the point of the
    method (the derivative along the path of M25b §7 is 0 there). The standard error is ``std(g, ddof=1) / √n``,
    coordinate by coordinate; with ``"leave-one-out"`` the terms ``g_i`` are not independent, and it is only an
    approximation.

    Parameters
    ----------
    f_values : 1-D array-like
        The ``n ≥ 2`` finite values ``f(x_i)``.
    scores : 1-D or 2-D array-like
        The finite scores: ``n`` numbers for a scalar ``θ``, or an ``(n, d)`` array whose row ``i`` is the gradient
        of ``ln p_θ(x_i)`` for a parameter ``θ`` in ``ℝ^d``, ``d ≥ 1``.
    baseline : float or str, default 0.0
        A finite number, or ``"leave-one-out"`` (a bool is refused).

    Returns
    -------
    tuple
        ``(estimate, standard_error)``: two Python ``float`` when ``scores`` is 1-D, two ``numpy.ndarray`` of shape
        ``(d,)`` when it is 2-D.

    Raises
    ------
    ValueError
        If ``f_values`` is not 1-D with at least 2 entries, if ``scores`` is not 1-D or 2-D with ``n`` rows (and at
        least one column), if a value is not finite, or if ``baseline`` is neither a finite number nor
        ``"leave-one-out"``.

    Examples
    --------
    >>> f, s = [3.0, 0.0, 2.0, 5.0], [0.5, -1.0, 0.0, 1.5]
    >>> est, se = score_function_gradient(f, s)
    >>> est, round(se, 4)
    (2.25, 1.7854)
    >>> score_function_gradient(f, s, baseline=1.0)[0]               # unbiased too, another variance
    2.0
    >>> round(score_function_gradient(f, s, baseline="leave-one-out")[0], 4)
    2.1667
    >>> score_function_gradient(f, [[0.5, 1.0], [-1.0, 0.0], [0.0, 2.0], [1.5, -1.0]])[0]    # θ in ℝ²
    array([2.25, 0.5 ])
    """
    f = _finite(_floats(f_values, "f_values"), "f_values")
    if f.ndim != 1 or f.size < 2:
        raise ValueError(f"f_values must be 1-D with at least 2 values, got the shape {f.shape}")
    n = f.size
    s = _floats(scores, "scores")
    if s.ndim not in (1, 2) or s.shape[0] != n or (s.ndim == 2 and s.shape[1] < 1):
        raise ValueError(f"scores must be 1-D with {n} entries or 2-D with {n} rows and at least one column, got the "
                         f"shape {s.shape}")
    _finite(s, "scores")
    if isinstance(baseline, str):
        if baseline != "leave-one-out":
            raise ValueError(f'baseline must be a finite number or "leave-one-out", got {baseline!r}')
        b = (np.sum(f) - f) / (n - 1)           # the mean of the n - 1 other values, for each draw
    else:
        if not _real(baseline) or not math.isfinite(baseline):
            raise ValueError(f'baseline must be a finite number (not a bool) or "leave-one-out", got {baseline!r}')
        b = float(baseline)
    centred = f - b                             # f(x_i) - b_i
    g = centred * s if s.ndim == 1 else centred[:, None] * s
    estimate = np.mean(g, axis=0)
    standard_error = np.std(g, axis=0, ddof=1) / math.sqrt(n)
    if s.ndim == 1:
        return float(estimate), float(standard_error)
    return estimate, standard_error


def policy_gradient_exact(P, r, logits, gamma):
    """Return ``(V, grad)``: the values of a tabular softmax policy, and their exact gradient in its logits.

    In state ``s``, the policy draws action ``a`` with the probability ``π(a | s) = e^{z(s, a)} / Σ_b e^{z(s, b)}``,
    the softmax of the row ``logits[s]`` (M17). It induces the chain ``P_π[s, t] = Σ_a π(a | s) P[a, s, t]`` and the
    rewards ``r_π[s] = Σ_a π(a | s) r[a, s]`` (M26 §4); its values ``V`` solve the Bellman system
    ``(I - γ P_π) V = r_π`` (M26 §5). Differentiating this system with respect to the logit ``z(s, a)`` gives
    (MB8 §4)

        ∂V(s0) / ∂z(s, a) = M[s0, s] · π(a | s) · A(s, a),    where    M = (I - γ P_π)⁻¹,

    ``Q(s, a) = r[a, s] + γ Σ_t P[a, s, t] V(t)`` is the value of action ``a`` in state ``s`` and
    ``A(s, a) = Q(s, a) - V(s)`` its advantage. For ``γ < 1``, the row ``(1 - γ) M[s0]`` is the discounted occupancy
    law from ``s0`` (a law when every ``P[a]`` is stochastic; M26 §5). Adding the same number to every logit of a state
    does not change the policy, so ``Σ_a grad[s0, s, a] = 0`` for every ``s0`` and ``s``.

    Parameters
    ----------
    P : 3-D array-like
        The ``(K, m, m)`` transition matrices, ``K ≥ 1`` actions and ``m ≥ 1`` states: each ``P[a]`` has entries
        ``≥ 0`` and rows summing to at most 1 (within ``1e-9``; the missing mass is the probability to end).
    r : 2-D array-like
        The ``(K, m)`` finite expected rewards: ``r[a, s] = r(s, a)``.
    logits : 2-D array-like
        The ``(m, K)`` finite logits of the policy: ``logits[s, a] = z(s, a)``.
    gamma : float
        The discount factor, ``0 ≤ γ ≤ 1`` (a bool is refused); ``γ = 1`` only when the process ends for sure under
        the policy.

    Returns
    -------
    tuple
        ``(V, grad)``: ``V`` of shape ``(m,)`` and ``grad`` of shape ``(m, m, K)``, with
        ``grad[s0, s, a] = ∂V(s0) / ∂z(s, a)``; floats.

    Raises
    ------
    ValueError
        If the shapes do not match, if an entry is not finite, if a ``P[a]`` has a negative entry or a row summing
        to more than 1, if ``gamma`` is a bool or is not in ``[0, 1]``, or if ``γ = 1`` and ``I - P_π`` is singular
        according to ``np.linalg.matrix_rank`` with its default tolerance (from some state, the process never ends).

    Examples
    --------
    >>> P = [[[1, 0], [1, 0]],            # action 0 leads to state 0
    ...      [[0, 1], [0, 1]]]            # action 1 leads to state 1
    >>> r = [[1, 0],                      # r[a, s]
    ...      [0, 2]]
    >>> V, grad = policy_gradient_exact(P, r, [[0, 0], [0, 0]], 0.6)    # π(a | s) = 1/2 everywhere
    >>> V
    array([1.625, 2.125])
    >>> np.round(grad[0], 5)              # ∂V(0)/∂z(s, a): row s, column a
    array([[ 0.30625, -0.30625],
           [-0.43125,  0.43125]])
    >>> policy_gradient_exact(P, r, [[0, 0], [0, 0]], 1.0)
    Traceback (most recent call last):
        ...
    ValueError: gamma = 1 and the process never ends from some state
    """
    T = _finite(_floats(P, "P"), "P")
    if T.ndim != 3 or T.shape[1] != T.shape[2] or T.shape[0] < 1 or T.shape[1] < 1:
        raise ValueError(f"P must have the shape (K, m, m) with K >= 1 and m >= 1, got {T.shape}")
    K, m = T.shape[0], T.shape[1]
    if np.any(T < 0):
        raise ValueError("P must hold probabilities >= 0 only")
    sums = np.sum(T, axis=2)
    if np.any(sums > 1.0 + SUM_TOLERANCE):
        a, s = (int(i) for i in np.argwhere(sums > 1.0 + SUM_TOLERANCE)[0])
        raise ValueError(f"each row of each P[a] must sum to at most 1 (up to {SUM_TOLERANCE}): row {s} of P[{a}] "
                         f"sums to {float(sums[a, s])!r}")
    R = _finite(_floats(r, "r"), "r")
    if R.shape != (K, m):
        raise ValueError(f"r must have the shape (K, m) = {(K, m)}, got {R.shape}")
    Z = _finite(_floats(logits, "logits"), "logits")
    if Z.shape != (m, K):
        raise ValueError(f"logits must have the shape (m, K) = {(m, K)}, got {Z.shape}")
    if not _real(gamma) or not math.isfinite(gamma) or not 0 <= gamma <= 1:
        raise ValueError(f"gamma must be a number in [0, 1] (not a bool), got {gamma!r}")
    g = float(gamma)
    E = np.exp(Z - np.max(Z, axis=1, keepdims=True))   # each row shifted: exponentials in (0, 1]
    pi = E / np.sum(E, axis=1, keepdims=True)           # pi[s, a] = π(a | s)
    P_pi = np.einsum("sa,ast->st", pi, T)               # Σ_a π(a | s) P[a, s, t]
    r_pi = np.einsum("sa,as->s", pi, R)                 # Σ_a π(a | s) r[a, s]
    I_minus = np.eye(m) - g * P_pi
    if g == 1.0 and np.linalg.matrix_rank(I_minus) < m:
        raise ValueError("gamma = 1 and the process never ends from some state")
    M = np.linalg.solve(I_minus, np.eye(m))             # (I - γ P_π)⁻¹
    V = M @ r_pi
    Q = R.T + g * np.einsum("ast,t->sa", T, V)          # Q[s, a] = r[a, s] + γ Σ_t P[a, s, t] V(t)
    A = Q - V[:, None]                                  # the advantages
    grad = M[:, :, None] * (pi * A)[None, :, :]         # grad[s0, s, a] = M[s0, s] π(a | s) A(s, a)
    return V, grad


def importance_weights(log_target, log_proposal, self_normalize=False, max_weight=None):
    """Return the importance weights ``p(x_i) / q(x_i)`` of draws from ``q``, and their effective sample size.

    ``x_1, …, x_n`` were drawn from a **proposal** law ``q``, and an expectation under a **target** law ``p`` is
    wanted. When ``q > 0`` wherever ``p f ≠ 0``, ``E_q[(p/q)(X) f(X)] = E_p[f(X)]``: the mean of the
    ``w_i f(x_i)`` estimates ``E_p[f]`` without bias. You give the logarithms of the two densities (or
    probabilities) at the draws; the weights are ``exp(log_target - log_proposal)``, accurate even where the
    densities themselves would underflow.

    - ``max_weight=c``: the weights are truncated, ``min(w_i, c)``: some bias (towards 0 for ``f ≥ 0``) traded for
      a smaller variance.
    - ``self_normalize=True``: the weights (truncated first, if asked) are divided by their sum, so that they sum
      to 1, and ``Σ_i w_i f(x_i)`` estimates ``E_p[f]``: with a bias for a finite ``n``, but usable when ``p`` or
      ``q`` is known only up to a constant factor (the logarithms are then known up to an additive constant, which
      cancels). Subtract the largest log-weight before taking exponentials (as in log-sum-exp, M05a).

    The **effective sample size** (Kish) is ``ess = (Σ_i w_i)² / Σ_i w_i²``: ``n`` when the weights are equal,
    close to 1 when one weight dominates the others, and always between 1 and ``n`` when a weight is positive
    (0.0 when every weight is 0). Multiplying every weight by the same factor does not change it: it is the same for
    the normalized weights, and it is computed from the log-weights, so that it stays exact even if a weight
    overflows.

    Parameters
    ----------
    log_target : 1-D array-like
        The ``n ≥ 1`` values ``ln p(x_i)``; ``-inf`` is allowed (a draw where ``p`` is 0 gets the weight 0), ``nan``
        and ``+inf`` are refused.
    log_proposal : 1-D array-like
        The ``n`` values ``ln q(x_i)``, finite (a draw of ``q`` has ``q(x_i) > 0``).
    self_normalize : bool, default False
        Whether to divide the weights by their sum.
    max_weight : float, optional
        The truncation level ``c > 0`` of the weights before any normalization (``np.inf`` truncates nothing);
        ``nan`` and a bool are refused. No truncation when omitted.

    Returns
    -------
    tuple
        ``(weights, ess)``: a ``numpy.ndarray`` of ``n`` floats and a Python ``float``. Without normalization, a
        weight beyond the largest float is ``inf``.

    Raises
    ------
    ValueError
        If the two arrays are not 1-D of the same length ``n ≥ 1``, if ``log_target`` holds ``nan`` or ``+inf``, if
        ``log_proposal`` is not finite, if ``self_normalize`` is not a bool, if ``max_weight`` is not a number
        ``> 0``, or if ``self_normalize`` is true and every weight is 0.

    Examples
    --------
    >>> lp, lq = [-1.0, -0.5, -0.5, -2.0], [-1.5, -1.0, -1.0, -1.0]
    >>> w, ess = importance_weights(lp, lq)
    >>> np.round(w, 4), round(ess, 4)
    (array([1.6487, 1.6487, 1.6487, 0.3679]), 3.4063)
    >>> w, ess = importance_weights(lp, lq, self_normalize=True)
    >>> np.round(w, 4), round(ess, 4)                                # weights summing to 1, the same ess
    (array([0.3103, 0.3103, 0.3103, 0.0692]), 3.4063)
    >>> importance_weights([0.0, -np.inf, 1.0], [0.0, 0.0, 0.0], max_weight=2.0)   # e¹ truncated to 2
    (array([1., 0., 2.]), 1.8)
    """
    lp = _floats(log_target, "log_target")
    lq = _floats(log_proposal, "log_proposal")
    if lp.ndim != 1 or lq.ndim != 1 or lp.size != lq.size or lp.size < 1:
        raise ValueError(f"log_target and log_proposal must be 1-D of the same length n >= 1, got the shapes "
                         f"{lp.shape} and {lq.shape}")
    if np.any(np.isnan(lp)) or np.any(lp == np.inf):
        raise ValueError("log_target must not hold nan or +inf (-inf is a draw where p is 0)")
    _finite(lq, "log_proposal")
    if not _is_bool(self_normalize):
        raise ValueError(f"self_normalize must be a bool (True or False), got {self_normalize!r}")
    d = lp - lq                                         # ln w_i, -inf where p is 0
    if max_weight is not None:
        if not _real(max_weight) or math.isnan(max_weight) or not max_weight > 0:
            raise ValueError(f"max_weight must be a number > 0 (np.inf truncates nothing), got {max_weight!r}")
        d = np.minimum(d, math.log(max_weight))         # min(w_i, c) on the log scale
    top = np.max(d)
    if top == -np.inf:                                  # every weight is 0
        if self_normalize:
            raise ValueError("every weight is 0: they cannot be divided by their sum")
        return np.zeros(lp.size), 0.0
    u = np.exp(d - top)                                 # the weights divided by the largest: entries in [0, 1]
    ess = float(np.sum(u) ** 2 / np.sum(u * u))
    if self_normalize:
        return u / np.sum(u), ess
    with np.errstate(over="ignore"):                    # a weight beyond the largest float is inf
        return np.exp(d), ess


def bradley_terry_fit(wins, tol=1e-10, max_iter=10_000):
    """Return the strengths ``β`` of a Bradley-Terry model fitted by maximum likelihood to a tournament, centered.

    In the Bradley-Terry model, player ``i`` beats player ``j`` with the probability
    ``σ(β_i - β_j) = e^{β_i} / (e^{β_i} + e^{β_j})``, independently from one match to the next. ``wins[i, j]`` is the
    number of times ``i`` beat ``j``, and ``n_ij = wins[i, j] + wins[j, i]`` the number of their matches. The
    log-likelihood ``Σ_{i, j} wins[i, j] ln σ(β_i - β_j)`` does not change when the same number is added to every
    ``β_i``: only the differences are identified, and the function returns the maximizer with ``Σ_i β_i = 0``. Its
    gradient vanishes when every player's number of wins equals its expected number,
    ``Σ_j wins[i, j] = Σ_j n_ij σ(β_i - β_j)`` (the likelihood equations).

    The maximum exists, and is then unique up to that constant, if and only if the directed graph with an edge
    ``i → j`` when ``wins[i, j] > 0`` is strongly connected: however the players are split into two groups, someone
    of each group beat someone of the other (Zermelo, 1929). Otherwise (a player who never lost, a group that never
    beat the others) the likelihood keeps increasing as some differences grow without bound, and the function
    raises ``ValueError``.

    Method (Zermelo's algorithm, MB8 §7): with ``p_i = e^{β_i}`` and ``W_i = Σ_j wins[i, j]``, compute from the
    current ``p`` the new values ``p_i ← W_i / Σ_{j ≠ i} n_ij / (p_i + p_j)`` for every ``i``, then divide them by
    their geometric mean (so that ``Σ_i ln p_i = 0``); stop when the largest change of ``β = ln p`` is below
    ``tol``. Each sweep increases the likelihood (admitted).

    Parameters
    ----------
    wins : 2-D array-like
        A square ``(K, K)`` array, ``K ≥ 2``, of finite numbers ``≥ 0`` (half-points for draws are allowed), with a
        zero diagonal.
    tol : float, default 1e-10
        The stopping threshold, a number ``> 0`` (a bool is refused).
    max_iter : int, default 10_000
        The largest number of sweeps, an integer ``≥ 1`` (a NumPy integer is accepted; a bool or a float is refused).

    Returns
    -------
    numpy.ndarray
        The ``K`` strengths ``β_i``, floats whose sum is 0 up to rounding.

    Raises
    ------
    ValueError
        If ``wins`` is not a square array of finite numbers ``≥ 0`` with ``K ≥ 2`` and a zero diagonal, if the graph
        of wins is not strongly connected (the maximum does not exist), or if ``tol`` or ``max_iter`` is not valid.
    RuntimeError
        If the largest change is still above ``tol`` after ``max_iter`` sweeps.

    Examples
    --------
    >>> np.round(bradley_terry_fit([[0, 4], [1, 0]]), 4)          # two players: β_0 - β_1 = ln 4
    array([ 0.6931, -0.6931])
    >>> np.round(bradley_terry_fit([[0, 4, 2], [1, 0, 3], [1, 2, 0]]), 4)
    array([ 0.7464, -0.2949, -0.4516])
    >>> bradley_terry_fit([[0, 2, 1], [0, 0, 3], [0, 1, 0]])      # player 0 never lost
    Traceback (most recent call last):
        ...
    ValueError: the strengths do not exist: the graph of wins is not strongly connected
    """
    W = _finite(_floats(wins, "wins"), "wins")
    if W.ndim != 2 or W.shape[0] != W.shape[1] or W.shape[0] < 2:
        raise ValueError(f"wins must be a square (K, K) array with K >= 2, got the shape {W.shape}")
    if np.any(W < 0):
        raise ValueError("wins must hold numbers >= 0 only")
    if np.any(np.diag(W) != 0):
        raise ValueError("wins must have a zero diagonal (a player never plays against itself)")
    if not _real(tol) or math.isnan(tol) or not tol > 0:
        raise ValueError(f"tol must be a number > 0 (not a bool), got {tol!r}")
    if _is_bool(max_iter) or not isinstance(max_iter, numbers.Integral) or max_iter < 1:
        raise ValueError(f"max_iter must be an integer >= 1 (not a bool, not a float), got {max_iter!r}")
    K = W.shape[0]
    reach = ((W > 0) | np.eye(K, dtype=bool)).astype(np.int64)   # i reaches j in at most 1 step
    length = 1
    while length < K - 1:                       # each product doubles the length of the paths taken into account
        reach = ((reach @ reach) > 0).astype(np.int64)
        length *= 2
    if not np.all(reach > 0):
        raise ValueError("the strengths do not exist: the graph of wins is not strongly connected")
    N = W + W.T                                 # n_ij, the number of matches between i and j
    total_wins = np.sum(W, axis=1)              # W_i, > 0 for every player of a strongly connected graph
    beta = np.zeros(K)
    for _ in range(int(max_iter)):
        p = np.exp(beta)
        denominators = np.sum(N / (p[:, None] + p[None, :]), axis=1)    # n_ii = 0: no term for j = i
        new = np.log(total_wins) - np.log(denominators)
        new -= np.mean(new)                     # divided by the geometric mean: Σ_i ln p_i = 0
        change = float(np.max(np.abs(new - beta)))
        beta = new
        if change < tol:
            return beta
    raise RuntimeError(f"Zermelo's algorithm did not reach tol = {tol!r} in max_iter = {max_iter!r} sweeps (largest "
                       f"change {change:.3g})")
