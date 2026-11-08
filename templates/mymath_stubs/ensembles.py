"""The mathematics of ensembles: the Chernoff bound on the tail of a binomial law, the variance of a weighted average
of correlated variables, and the exponential weights of the Hedge algorithm (chapter M14).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m14_ensembles.py``.
NumPy and the module ``math`` are allowed, but not SciPy: the tests compare your results with ``scipy.stats`` and
``scipy.special``.
Numbers are returned as Python ``float``, vectors and matrices as ``numpy.ndarray`` of floats.
"""


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
    # TODO: check the arguments, handle a ≤ p and p = 0, then the divergence (math.log) and math.exp(-n · KL).
    raise NotImplementedError("chernoff_bound() is not implemented yet")


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
    # TODO: check cov and the weights (default np.full(M, 1/M)), then w @ cov @ w.
    raise NotImplementedError("variance_of_average() is not implemented yet")


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
    # TODO: the cumulative losses (a row of zeros, then np.cumsum), minus their minimum per row, exp(-eta ·), normalize.
    raise NotImplementedError("hedge_weights() is not implemented yet")
