"""Mixtures of Gaussians and the EM algorithm: the responsibilities (the E step), the weighted maximum likelihood (the
M step), the log-likelihood of a mixture, and its evidence lower bound (ELBO) for any responsibilities (chapter M25b).

Reference implementation (solutions/mymath_ref).
Import the log-density of M25a with a relative import, ``from .gaussian import mvn_logpdf``; you may import
``logsumexp`` from ``approx`` (M05a) the same way, or write its factored formula along an axis with NumPy (any
relative import of your own modules is allowed). NumPy is allowed, but not ``np.cov`` nor ``np.average`` (the tests
compare your M step with them), from ``np.linalg`` only ``cholesky`` and ``solve`` (those of ``mvn_logpdf``), no SciPy
at all (``scipy.stats.multivariate_normal``, ``scipy.special.logsumexp``…: the tests compare your results with them)
and no scikit-learn (``GaussianMixture``). Compute with logarithms of densities, never with the densities themselves:
far from a component, a density underflows to 0 and its logarithm does not.
Shapes: the ``n`` data points are the rows of ``X``, of shape ``(n, d)``, finite numbers (measurements in dimension 1
form a column ``(n, 1)``; a 1-D ``X`` is refused); a mixture of ``K`` components is given by its weights ``(K,)``,
its means ``(K, d)`` and its covariance matrices ``(K, d, d)``; responsibilities are an ``(n, K)`` array whose row
``i`` is a law on the ``K`` components for the point ``i``. Weights are valid when they are all ``> 0`` and sum to 1
up to ``1e-9``; responsibilities when they are finite, ``≥ 0`` and each row sums to 1 up to ``1e-9``. A covariance
matrix is checked by ``mvn_logpdf`` (symmetric positive definite). Never modify the arrays you receive. Numbers are
returned as Python ``float``, vectors and matrices as ``numpy.ndarray`` of floats.
"""

import math
import numbers

import numpy as np

from .gaussian import mvn_logpdf

# logsumexp of approx (M05a) takes one sequence and returns one float: the log-sum-exp of each row of an (n, K) array
# is written below with NumPy, by the same factored formula.

SUM_TOLERANCE = 1e-9          # weights and rows of responsibilities sum to 1 up to this


def _float_array(values, what):
    """values as a float array (a view when it already is one: never written to), or ValueError."""
    try:
        return np.asarray(values, dtype=float)
    except (TypeError, ValueError):
        raise ValueError(f"{what} must be an array of numbers, got {values!r}") from None


def _data(X):
    """Check the data: a 2-D (n, d) array of finite numbers, n ≥ 1 and d ≥ 1."""
    points = _float_array(X, "X")
    if points.ndim != 2 or points.shape[0] < 1 or points.shape[1] < 1:
        raise ValueError(f"X must be a 2-D array (n, d) with n >= 1 and d >= 1 (in dimension 1, n points form a "
                         f"column (n, 1)), got shape {points.shape}")
    if not np.all(np.isfinite(points)):
        raise ValueError("X must hold finite numbers only (no nan, no inf)")
    return points


def _mixture(weights, means, covs, d):
    """Check the weights ((K,), all > 0, summing to 1) and the shapes of the means (K, d) and covariances (K, d, d).

    The covariance matrices themselves (symmetric positive definite) are checked by mvn_logpdf."""
    w = _float_array(weights, "weights")
    if w.ndim != 1 or w.size < 1:
        raise ValueError(f"weights must be a 1-D array of K >= 1 values, got shape {w.shape}")
    if not np.all(np.isfinite(w)) or np.any(w <= 0):
        raise ValueError(f"weights must all be finite and > 0, got {w}")
    if abs(float(np.sum(w)) - 1.0) > SUM_TOLERANCE:
        raise ValueError(f"weights must sum to 1 (up to {SUM_TOLERANCE}), got a sum of {float(np.sum(w))!r}")
    K = w.size
    mu = _float_array(means, "means")
    if mu.shape != (K, d):
        raise ValueError(f"means must have shape ({K}, {d}): one row of {d} coordinate(s) per component, got shape "
                         f"{mu.shape}")
    sigma = _float_array(covs, "covs")
    if sigma.shape != (K, d, d):
        raise ValueError(f"covs must have shape ({K}, {d}, {d}): one {d} x {d} matrix per component, got shape "
                         f"{sigma.shape}")
    return w, mu, sigma


def _responsibilities(resp, n, K=None, empty_ok=False):
    """Check responsibilities: (n, K) with K ≥ 1 (the given K if any), finite, ≥ 0, each row summing to 1; a column
    of zeros (N_k = 0) only if empty_ok."""
    R = _float_array(resp, "resp")
    if R.ndim != 2 or R.shape[0] != n or R.shape[1] < 1:
        raise ValueError(f"resp must be a 2-D array (n, K) with n = {n} rows (one per point of X) and K >= 1, got "
                         f"shape {R.shape}")
    if K is not None and R.shape[1] != K:
        raise ValueError(f"resp must have K = {K} columns, one per component (as weights), got shape {R.shape}")
    if not np.all(np.isfinite(R)):
        raise ValueError("resp must hold finite numbers only (no nan, no inf)")
    if np.any(R < 0):
        raise ValueError("resp must hold numbers >= 0 only")
    sums = np.sum(R, axis=1)
    bad = np.flatnonzero(np.abs(sums - 1.0) > SUM_TOLERANCE)
    if bad.size:
        raise ValueError(f"each row of resp must sum to 1 (up to {SUM_TOLERANCE}): row {int(bad[0])} sums to "
                         f"{float(sums[bad[0]])!r}")
    if not empty_ok:
        empty = np.flatnonzero(np.all(R == 0, axis=0))
        if empty.size:
            raise ValueError(f"resp has a column of zeros: component {int(empty[0])} is empty (N_k = 0), its mean "
                             f"and covariance are not defined")
    return R


def _log_joint(points, w, mu, sigma):
    """a[i, k] = ln π_k + ln N(x_i | μ_k, Σ_k), an (n, K) array (mvn_logpdf checks each Σ_k)."""
    columns = [mvn_logpdf(points, mu[k], sigma[k]) for k in range(w.size)]   # each: one value per row of X
    return np.column_stack(columns) + np.log(w)                              # + ln π_k on column k


def _row_logsumexp(a):
    """ln Σ_k e^(a[i, k]) for each row i, factoring out the row maximum m_i: m_i + ln Σ_k e^(a[i, k] - m_i)."""
    m = np.max(a, axis=1, keepdims=True)         # finite: every a[i, k] is
    return m[:, 0] + np.log(np.sum(np.exp(a - m), axis=1))   # each sum is ≥ 1 (the term of the maximum): no ln 0


def gmm_e_step(X, weights, means, covs):
    """Return the responsibilities of the components of a Gaussian mixture for each point (the E step of EM).

    The responsibility of component ``k`` for the point ``x_i`` is its posterior probability given ``x_i`` (Bayes,
    M04): ``r[i, k] = π_k N(x_i | μ_k, Σ_k) / Σ_j π_j N(x_i | μ_j, Σ_j)``. Compute it in logarithms: with
    ``a[i, k] = ln π_k + ln N(x_i | μ_k, Σ_k)`` (``mvn_logpdf``), ``ln r[i, k] = a[i, k] - logsumexp_j a[i, j]``,
    then take the exponential. Every row sums to 1, even for a point far from every component (no ``0/0``).

    Parameters
    ----------
    X : 2-D array-like
        The ``(n, d)`` data, one point per row, ``n ≥ 1`` and ``d ≥ 1``.
    weights : 1-D array-like
        The ``K ≥ 1`` mixture weights ``π_k``: all ``> 0``, summing to 1.
    means : 2-D array-like
        The ``(K, d)`` means ``μ_k``, one per row.
    covs : 3-D array-like
        The ``(K, d, d)`` covariance matrices ``Σ_k``, each symmetric positive definite.

    Returns
    -------
    numpy.ndarray
        The ``(n, K)`` responsibilities; each row sums to 1.

    Raises
    ------
    ValueError
        If ``X`` is not 2-D, is empty or holds a value that is not finite, if ``weights`` is not 1-D, is empty, holds
        a value ``≤ 0`` or does not sum to 1, if the shapes of ``means`` and ``covs`` do not match ``K`` and ``d``, or
        if a covariance matrix is not symmetric positive definite.

    Examples
    --------
    >>> X = [[0.5], [2.0], [3.5], [6.0]]
    >>> R = gmm_e_step(X, [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]])
    >>> np.round(R, 4), R.sum(axis=1)
    (array([[0.9924, 0.0076],
           [0.8444, 0.1556],
           [0.0678, 0.9322],
           [0.    , 1.    ]]), array([1., 1., 1., 1.]))
    >>> gmm_e_step([[1000.0]], [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]])   # far away: no 0/0
    array([[0., 1.]])
    """
    points = _data(X)
    w, mu, sigma = _mixture(weights, means, covs, points.shape[1])
    a = _log_joint(points, w, mu, sigma)
    log_r = a - _row_logsumexp(a)[:, None]       # ln r[i, k] = a[i, k] - logsumexp_j a[i, j], always ≤ 0
    return np.exp(log_r)                         # far away, a tiny r underflows to 0, never 0/0


def gmm_m_step(X, resp, reg=0.0):
    """Return the weights, means and covariances of the M step of EM (for ``reg = 0``, the weighted maximum likelihood).

    With ``N_k = Σ_i r[i, k]``, the effective number of points of component ``k``:
    ``π_k = N_k / n``, ``μ_k = (1 / N_k) Σ_i r[i, k] x_i`` and
    ``Σ_k = (1 / N_k) Σ_i r[i, k] (x_i - μ_k)(x_i - μ_k)ᵀ + reg · I``.
    These are the weighted versions of the maximum likelihood of M25a (dividing by ``N_k``, like it); with
    responsibilities equal to 0 or 1, they are the proportion, the mean and the covariance of each group. The
    likelihood of a mixture is unbounded (a component whose covariance shrinks onto one point sends it to ``+∞``):
    ``reg > 0`` adds ``reg`` to the diagonal of every covariance matrix and keeps it positive definite. With
    ``reg > 0`` these parameters no longer maximize the weighted log-likelihood, and EM is no longer guaranteed to
    raise the ELBO nor the log-likelihood.

    The covariance matrices are returned as computed, without any check: with ``reg = 0``, a component whose
    responsibilities are non-zero on ``d`` points or fewer gets a singular covariance (or, through rounding, a nearly
    singular one), and ``gmm_e_step`` refuses it when its Cholesky decomposition fails.

    Parameters
    ----------
    X : 2-D array-like
        The ``(n, d)`` data, one point per row, ``n ≥ 1`` and ``d ≥ 1``.
    resp : 2-D array-like
        The ``(n, K)`` responsibilities, ``K ≥ 1``: finite, ``≥ 0``, each row summing to 1.
    reg : float, default 0.0
        The finite number ``≥ 0`` added to the diagonal of each covariance matrix (a ``bool`` is refused).

    Returns
    -------
    tuple
        ``(weights, means, covs)``: the ``(K,)`` weights, the ``(K, d)`` means and the ``(K, d, d)`` covariance
        matrices.

    Raises
    ------
    ValueError
        If ``X`` is not 2-D, is empty or holds a value that is not finite, if ``resp`` is not ``(n, K)`` with
        ``K ≥ 1``, holds a value that is not finite or is ``< 0``, has a row that does not sum to 1, or has a column of
        zeros (an empty component, ``N_k = 0``), or if ``reg`` is not a finite number ``≥ 0``.

    Examples
    --------
    >>> w, m, C = gmm_m_step([[0.5], [2.0], [3.5], [6.0]], [[1, 0], [1, 0], [0, 1], [0, 1]])
    >>> w, m, C
    (array([0.5, 0.5]), array([[1.25],
           [4.75]]), array([[[0.5625]],
    <BLANKLINE>
           [[1.5625]]]))
    >>> X = [[0, 0], [1, 0], [0, 2], [4, 4], [5, 3]]
    >>> w, m, C = gmm_m_step(X, [[1, 0], [1, 0], [1, 0], [0, 1], [0, 1]], reg=0.1)
    >>> w, np.round(m, 4)
    (array([0.6, 0.4]), array([[0.3333, 0.6667],
           [4.5   , 3.5   ]]))
    >>> np.round(C[1], 4)                                  # two points: singular without reg
    array([[ 0.35, -0.25],
           [-0.25,  0.35]])
    """
    points = _data(X)
    n, d = points.shape
    R = _responsibilities(resp, n)
    if (isinstance(reg, (bool, np.bool_)) or not isinstance(reg, numbers.Real) or not math.isfinite(reg)
            or reg < 0):
        raise ValueError(f"reg must be a finite number >= 0 (not a bool), got {reg!r}")
    K = R.shape[1]
    N = np.sum(R, axis=0)                        # N_k: the effective number of points of each component (all > 0)
    weights = N / n                              # π_k = N_k / n: they sum to 1, since each row of resp does
    means = (R.T @ points) / N[:, None]          # row k: (1 / N_k) Σ_i r[i, k] x_i
    covs = np.empty((K, d, d))
    for k in range(K):
        deviations = points - means[k]           # (n, d): x_i - μ_k in row i (a new array)
        S = (R[:, k, None] * deviations).T @ deviations / N[k]   # (1 / N_k) Σ_i r[i, k] (x_i - μ_k)(x_i - μ_k)ᵀ
        covs[k] = (S + S.T) / 2 + float(reg) * np.eye(d)         # (S + Sᵀ) / 2 removes the rounding asymmetry
    return weights, means, covs


def gmm_log_likelihood(X, weights, means, covs):
    """Return the log-likelihood of the data under a Gaussian mixture, ``Σ_i ln Σ_k π_k N(x_i | μ_k, Σ_k)``.

    The logarithm of a sum does not split: compute ``a[i, k] = ln π_k + ln N(x_i | μ_k, Σ_k)`` (``mvn_logpdf``), take
    the logsumexp of each row, then add the ``n`` results. Divide by ``n`` for a value in nats per point.

    Parameters
    ----------
    X, weights, means, covs
        As in ``gmm_e_step``.

    Returns
    -------
    float
        The log-likelihood, in nats.

    Raises
    ------
    ValueError
        As ``gmm_e_step``.

    Examples
    --------
    >>> X = [[0.5], [2.0], [3.5], [6.0]]
    >>> round(gmm_log_likelihood(X, [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]]), 4)
    -8.4137
    >>> round(gmm_log_likelihood([[1000.0]], [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]]), 1)   # not -inf
    -247508.0
    """
    points = _data(X)
    w, mu, sigma = _mixture(weights, means, covs, points.shape[1])
    a = _log_joint(points, w, mu, sigma)
    return float(np.sum(_row_logsumexp(a)))      # Σ_i ln p(x_i), with ln p(x_i) = logsumexp_k a[i, k]


def gmm_elbo(X, resp, weights, means, covs):
    """Return the evidence lower bound (ELBO) of a Gaussian mixture, with the rows of ``resp`` as laws of the latent.

    Row ``i`` of ``resp`` is a law ``q_i`` on the components for the point ``x_i``. The ELBO is
    ``Σ_i Σ_k r[i, k] (ln π_k + ln N(x_i | μ_k, Σ_k) - ln r[i, k])``, with ``0 ln 0 = 0`` (a term where
    ``r[i, k] = 0`` counts for 0): for each point, the expected log-joint ``E_{q_i}[ln p(x_i, z)]`` plus the entropy of
    ``q_i``. It never exceeds ``gmm_log_likelihood``; the gap is ``Σ_i KL(q_i ‖ p(z | x_i))``, zero exactly when
    ``resp`` is the output of ``gmm_e_step`` for the same parameters. EM without regularization (``reg = 0``) raises it
    at each half step: the E step in ``resp``, the M step in the parameters.

    Parameters
    ----------
    X : 2-D array-like
        The ``(n, d)`` data, one point per row.
    resp : 2-D array-like
        The ``(n, K)`` laws ``q_i``: finite, ``≥ 0``, each row summing to 1 (a column of zeros is allowed here).
    weights, means, covs
        As in ``gmm_e_step``, with the same ``K`` as ``resp``.

    Returns
    -------
    float
        The ELBO, in nats.

    Raises
    ------
    ValueError
        As ``gmm_e_step``, if ``resp`` is not ``(n, K)`` with the ``K`` of ``weights``, or if it holds a value that is
        not finite or is ``< 0``, or a row that does not sum to 1.

    Examples
    --------
    >>> X, w, m, C = [[0.5], [2.0], [3.5], [6.0]], [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]]
    >>> R = gmm_e_step(X, w, m, C)
    >>> abs(gmm_elbo(X, R, w, m, C) - gmm_log_likelihood(X, w, m, C)) < 1e-12        # q = the posterior
    True
    >>> round(gmm_elbo(X, [[1, 0], [1, 0], [0, 1], [0, 1]], w, m, C), 4)            # below -8.4137
    -8.6606
    >>> round(gmm_elbo(X, [[0.5, 0.5]] * 4, w, m, C), 4)
    -16.638
    """
    points = _data(X)
    w, mu, sigma = _mixture(weights, means, covs, points.shape[1])
    R = _responsibilities(resp, points.shape[0], K=w.size, empty_ok=True)
    a = _log_joint(points, w, mu, sigma)
    positive = R > 0
    log_r = np.log(np.where(positive, R, 1.0))   # ln r where r > 0; ln 1 = 0 elsewhere (never ln 0)
    terms = np.where(positive, R * (a - log_r), 0.0)   # r (ln p(x_i, k) - ln r), and 0 ln 0 = 0
    return float(np.sum(terms))
