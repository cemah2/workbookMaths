"""The mathematics of ensembles: the Chernoff bound on the tail of a binomial law, the variance of a weighted average
of correlated variables, and the exponential weights of the Hedge algorithm (chapter M14).

Reference implementation (solutions/mymath_ref).
NumPy and the module ``math`` are allowed, but not SciPy: the tests compare your results with ``scipy.stats`` and
``scipy.special``.
Numbers are returned as Python ``float``, vectors and matrices as ``numpy.ndarray`` of floats.
"""

import math
import numbers

import numpy as np


def _array(x, what):
    """A copy of x as an array of floats (ValueError if it is not made of numbers)."""
    a = np.asarray(x)
    if a.dtype.kind not in "iuf":
        raise ValueError(f"{what} must be made of numbers, got values of type {a.dtype}")
    return a.astype(float)


def _unit(value, what):
    """value as a float in [0, 1] (ValueError otherwise, NaN included)."""
    if isinstance(value, bool) or not isinstance(value, numbers.Real) or not 0 <= value <= 1:
        raise ValueError(f"{what} must be a number in [0, 1], got {value!r}")
    return float(value)



def chernoff_bound(n, p, a):
    """Return the Chernoff bound ``exp(-n KL(a ‖ p))`` on ``P(X ≥ n a)``, for ``X`` of binomial law ``B(n, p)``.

    For ``a > p``, Markov's inequality applied to ``e^{λX}`` gives ``P(X ≥ n a) ≤ e^{-λ n a} (1 - p + p e^λ)^n`` for
    every ``λ > 0``; the best ``λ`` turns the bound into ``exp(-n KL(a ‖ p))``, with the divergence (in nats) between
    the Bernoulli laws of parameters ``a`` and ``p``:
    ``KL(a ‖ p) = a ln(a / p) + (1 - a) ln((1 - a) / (1 - p))``, where ``0 ln 0`` counts as 0. For ``a ≤ p`` the bound
    says nothing: return ``1.0``. If ``p = 0`` and ``a > 0``, the event is impossible: return ``0.0``.

    Parameters
    ----------
    n : int
        The number of trials, ``n ≥ 0``.
    p : float
        The probability of success of each trial, in ``[0, 1]``.
    a : float
        The proportion of successes in the event ``X ≥ n a``, in ``[0, 1]``.

    Returns
    -------
    float
        The bound, in ``[0, 1]``.

    Raises
    ------
    ValueError
        If ``n`` is not a non-negative integer, or if ``p`` or ``a`` is outside ``[0, 1]``.

    Examples
    --------
    >>> round(chernoff_bound(10, 0.5, 0.8), 4)
    0.1455
    >>> chernoff_bound(10, 0.5, 0.4)
    1.0
    """
    if isinstance(n, bool) or not isinstance(n, numbers.Integral) or n < 0:
        raise ValueError(f"n must be an integer ≥ 0, got {n!r}")
    p, a = _unit(p, "p"), _unit(a, "a")
    if a <= p:
        return 1.0
    if p == 0.0:
        return 0.0
    kl = a * math.log(a / p)                     # a > p > 0 here
    if a < 1.0:                                  # 0 ln 0 counts as 0 when a = 1
        kl += (1.0 - a) * math.log((1.0 - a) / (1.0 - p))
    return min(1.0, math.exp(-int(n) * kl))      # a rounding of KL just below 0 when a is very close to p


def variance_of_average(cov, weights=None):
    """Return the variance of the weighted average ``Σ w_i X_i`` of variables of covariance matrix ``cov``.

    ``V(Σ w_i X_i) = Σ_i Σ_j w_i w_j Cov(X_i, X_j) = wᵀ cov w`` (M02c). Without weights, the plain average
    (``w_i = 1/M``).

    Parameters
    ----------
    cov : 2-D array-like
        The symmetric ``(M, M)`` covariance matrix of ``X_1, …, X_M``.
    weights : 1-D array-like, optional
        ``M`` non-negative weights of sum 1 (within ``1e-9``); ``1/M`` each when omitted.

    Returns
    -------
    float
        The variance of the average.

    Raises
    ------
    ValueError
        If ``cov`` is not square or not symmetric (within ``1e-12 · max(1, max |cov|)``), if the weights have the
        wrong length, a negative entry, or a sum different from 1, or if the result is negative beyond rounding
        (below ``-1e-12 · max(1, max |cov|)``): ``cov`` is then not a covariance matrix.

    Examples
    --------
    >>> variance_of_average([[4, 0], [0, 4]])
    2.0
    >>> variance_of_average([[4, 4], [4, 4]])
    4.0
    >>> variance_of_average([[1, 0], [0, 9]], weights=[0.9, 0.1])
    0.9
    """
    c = _array(cov, "cov")
    if c.ndim != 2 or c.shape[0] != c.shape[1] or c.shape[0] == 0:
        raise ValueError(f"cov must be a square (M, M) matrix with M ≥ 1, got shape {c.shape}")
    scale = max(1.0, float(np.max(np.abs(c))))
    if np.max(np.abs(c - c.T)) > 1e-12 * scale:
        raise ValueError("cov must be symmetric")
    m = c.shape[0]
    if weights is None:
        w = np.full(m, 1.0 / m)
    else:
        w = _array(weights, "weights")
        if w.ndim != 1 or w.size != m:
            raise ValueError(f"weights must hold {m} numbers, one per variable, got shape {w.shape}")
        if np.any(w < 0):
            raise ValueError("the weights must be non-negative")
        if abs(float(w.sum()) - 1.0) > 1e-9:
            raise ValueError(f"the weights must sum to 1, got {float(w.sum())!r}")
    value = float(w @ c @ w)
    if value < -1e-12 * scale:
        raise ValueError(f"the variance would be {value!r} < 0: cov is not a covariance matrix")
    return value


def hedge_weights(losses, eta):
    """Return the weights of the Hedge algorithm (exponential weights) before each round and after the last one.

    ``K`` experts suffer a loss at each of ``T`` rounds. Before round ``t``, expert ``k`` has the weight
    ``w_t[k] ∝ exp(-eta L_t[k])``, where ``L_t[k]`` is the sum of its losses over the rounds before ``t``; the weights
    are normalized to sum 1 (row 0, before any loss, is uniform). Subtract the smallest cumulative loss before taking
    the exponential, so that large losses do not make every weight 0.

    Parameters
    ----------
    losses : 2-D array-like
        The ``(T, K)`` losses, ``losses[t, k]`` for expert ``k`` at round ``t``.
    eta : float
        The learning rate, ``eta > 0``.

    Returns
    -------
    numpy.ndarray
        The ``(T + 1, K)`` weights; each row sums to 1.

    Raises
    ------
    ValueError
        If ``losses`` is not 2-D or has no column, or if ``eta ≤ 0``.

    Examples
    --------
    >>> hedge_weights([[0, 1], [0, 1]], eta=math.log(2))
    array([[0.5       , 0.5       ],
           [0.66666667, 0.33333333],
           [0.8       , 0.2       ]])
    """
    L = _array(losses, "losses")
    if L.ndim != 2 or L.shape[1] == 0:
        raise ValueError(f"losses must be a (T, K) array with K ≥ 1, got shape {L.shape}")
    if isinstance(eta, bool) or not isinstance(eta, numbers.Real) or not eta > 0:
        raise ValueError(f"eta must be a number > 0, got {eta!r}")
    cumulative = np.vstack([np.zeros((1, L.shape[1])), np.cumsum(L, axis=0)])
    shifted = cumulative - cumulative.min(axis=1, keepdims=True)
    w = np.exp(-float(eta) * shifted)
    return w / w.sum(axis=1, keepdims=True)
