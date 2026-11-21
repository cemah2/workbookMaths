"""The hidden methods of the check of 🛠️ MB8.20 (chapter MB8): two right ways to compute the exact gradient of the values
of a tabular softmax policy, and wrong ways, each wrong on one clause of the statement.

Reference material, like ``solutions/mymath_ref/``. The check cell loads this file (``importlib``) and passes each
method, under a neutral name, to the learner's two property tests ``matches_finite_differences_20(method)`` and
``sums_to_zero_20(method)``; a test must accept the right methods and refuse the wrong ones whose property is false.
Its texts (the clauses) live in the check cell. Every method has the signature of ``policy_gradient_exact(P, r,
logits, gamma)`` (MB8 §4, the conventions of M26.14: ``P[a, s, t]``, ``r[a, s]``, ``logits[s, a]``) and returns
``(V, grad)`` with ``grad[s0, s, a] = ∂V(s0)/∂z(s, a)``. None of them calls ``mymath`` nor ``mymath_ref``: a learner's
test that calls the reference while it judges these methods is seen by the check.

The wrong methods err by little where the statement asks for precision (the derivatives within ``1e-6`` in absolute
value, the sums within ``1e-10``): their gaps are larger than these tolerances but smaller than the default tolerance of
``np.allclose`` (``rtol=1e-5``, ``atol=1e-8``), and some are wrong only on a part of the drawn MDPs (three actions, four
states or more, rewards that differ from one action to the other, logits that differ in a state).
"""

import numpy as np


def _parts(P, r, logits, gamma):
    """pi[s, a], M = (I − γ P_π)⁻¹, V and Q[s, a] (NumPy, written for these methods only)."""
    T, R, Zl = (np.asarray(x, dtype=float) for x in (P, r, logits))
    E = np.exp(Zl - Zl.max(axis=1, keepdims=True))
    pi = E / E.sum(axis=1, keepdims=True)
    P_pi = np.einsum("sa,ast->st", pi, T)
    r_pi = np.einsum("sa,as->s", pi, R)
    M = np.linalg.inv(np.eye(len(r_pi)) - float(gamma) * P_pi)
    V = M @ r_pi
    Q = R.T + float(gamma) * np.einsum("ast,t->sa", T, V)
    return pi, M, V, Q


def _formula(M, weights):
    """grad[s0, s, a] = M[s0, s] weights[s, a]."""
    return M[:, :, None] * weights[None, :, :]


# --------------------------------------------------------------------------------------------------------------------
# right methods
# --------------------------------------------------------------------------------------------------------------------
def per_logit(P, r, logits, gamma):
    """RIGHT: the derived Bellman system solved logit by logit, (I − γ P_π) ∂V = ∂r_π + γ (∂P_π) V, with
    ∂π(b | s')/∂z(s, a) = 1{s' = s} π(b | s) (1{b = a} − π(a | s))."""
    T, R, Zl = (np.asarray(x, dtype=float) for x in (P, r, logits))
    pi, M, V, _ = _parts(T, R, Zl, gamma)
    m, K = Zl.shape
    A_sys = np.eye(m) - float(gamma) * np.einsum("sa,ast->st", pi, T)
    grad = np.zeros((m, m, K))
    for s in range(m):
        for a in range(K):
            dpi = np.zeros((m, K))
            dpi[s] = pi[s] * ((np.arange(K) == a) - pi[s, a])
            rhs = np.einsum("sa,as->s", dpi, R) + float(gamma) * np.einsum("sa,ast->st", dpi, T) @ V
            grad[:, s, a] = np.linalg.solve(A_sys, rhs)
    return V, grad


def inverse_formula(P, r, logits, gamma):
    """RIGHT: the formula M[s0, s] π(a | s) A(s, a), with M by np.linalg.inv."""
    pi, M, V, Q = _parts(P, r, logits, gamma)
    return V, _formula(M, pi * (Q - V[:, None]))


RIGHT = (per_logit, inverse_formula)


# --------------------------------------------------------------------------------------------------------------------
# wrong methods (the check says which test must refuse each, and why)
# --------------------------------------------------------------------------------------------------------------------
def occupancy(P, r, logits, gamma):
    """WRONG everywhere: (1 − γ) M (the occupancy law ν) instead of M."""
    V, grad = inverse_formula(P, r, logits, gamma)
    return V, (1 - float(gamma)) * grad


def transposed(P, r, logits, gamma):
    """WRONG unless M is symmetric: M[s, s0] instead of M[s0, s]."""
    pi, M, V, Q = _parts(P, r, logits, gamma)
    return V, _formula(M.T, pi * (Q - V[:, None]))


def uniform(P, r, logits, gamma):
    """WRONG unless the logits of each state are equal: 1/K instead of π(a | s)."""
    pi, M, V, Q = _parts(P, r, logits, gamma)
    return V, _formula(M, (Q - V[:, None]) / pi.shape[1])


def three_actions(P, r, logits, gamma):
    """WRONG only with three actions: the derivative of the last action set to 0, the second one minus the first one
    (the sums over the actions stay 0)."""
    V, grad = inverse_formula(P, r, logits, gamma)
    if grad.shape[2] == 3:
        grad = grad.copy()
        grad[:, :, 1] = -grad[:, :, 0]
        grad[:, :, 2] = 0.0
    return V, grad


def four_states(P, r, logits, gamma):
    """WRONG only from four states on: M transposed then."""
    V, grad = inverse_formula(P, r, logits, gamma)
    if grad.shape[0] >= 4:
        return transposed(P, r, logits, gamma)
    return V, grad


def mixed_rewards(P, r, logits, gamma):
    """WRONG when the rewards of a state differ from one action to the other: r_π(s) instead of r(s, a) in Q (the sums
    over the actions stay 0)."""
    T, R = np.asarray(P, dtype=float), np.asarray(r, dtype=float)
    pi, M, V, _ = _parts(P, r, logits, gamma)
    r_pi = np.einsum("sa,as->s", pi, R)
    Q = r_pi[:, None] + float(gamma) * np.einsum("ast,t->sa", T, V)
    return V, _formula(M, pi * (Q - V[:, None]))


def relative_8e6(P, r, logits, gamma):
    """WRONG by 8e-6 in relative value (inside the default tolerance of np.allclose): the gradient times 1 + 8e-6."""
    V, grad = inverse_formula(P, r, logits, gamma)
    return V, grad * (1 + 8e-6)


def offset_large(P, r, logits, gamma):
    """WRONG by 2.5e-6 on the derivatives of absolute value 0.25 or more (inside the default tolerance of np.allclose,
    outside 1e-6 in absolute value)."""
    V, grad = inverse_formula(P, r, logits, gamma)
    return V, grad + 2.5e-6 * np.sign(grad) * (np.abs(grad) >= 0.25)


def last_entry(P, r, logits, gamma):
    """WRONG on one derivative only, the last one, grad[m - 1, m - 1, K - 1], by 4e-6."""
    V, grad = inverse_formula(P, r, logits, gamma)
    grad = grad.copy()
    grad[-1, -1, -1] += 4e-6
    return V, grad


def zeros(P, r, logits, gamma):
    """WRONG everywhere (but of sum 0 over the actions): zeros."""
    V, grad = inverse_formula(P, r, logits, gamma)
    return V, np.zeros_like(grad)


def offset_sum(P, r, logits, gamma):
    """WRONG on the sums only: 3e-10 added to every derivative (invisible within 1e-6, and to np.allclose by default)."""
    V, grad = inverse_formula(P, r, logits, gamma)
    return V, grad + 3e-10


def one_pair(P, r, logits, gamma):
    """WRONG on the sum of one couple (s0, s) only: 5e-10 added to grad[m - 1, 0, 0]."""
    V, grad = inverse_formula(P, r, logits, gamma)
    grad = grad.copy()
    grad[-1, 0, 0] += 5e-10
    return V, grad


def opposite_pairs(P, r, logits, gamma):
    """WRONG on the sums of two couples (s0, s) that compensate: +5e-10 on the sum of (0, 0), −5e-10 on the sum of
    (m − 1, m − 1) (their total and their mean are still 0)."""
    V, grad = inverse_formula(P, r, logits, gamma)
    grad = grad.copy()
    grad[0, 0, 0] += 5e-10
    grad[-1, -1, 0] -= 5e-10
    return V, grad


def values_not_advantages(P, r, logits, gamma):
    """WRONG everywhere: π(a | s) Q(s, a) instead of π(a | s) A(s, a) (its sum over the actions is M[s0, s] V(s))."""
    pi, M, V, Q = _parts(P, r, logits, gamma)
    return V, _formula(M, pi * Q)
