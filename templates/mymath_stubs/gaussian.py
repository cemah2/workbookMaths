"""The multivariate normal law: the log-density, sampling by Cholesky, the Schur complement of a block, the conditional
law of some coordinates given the others, and the posterior of a Bayesian linear regression (chapter M25a).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m25a_gaussian.py``.
NumPy is allowed, but from ``np.linalg`` only ``cholesky`` and ``solve`` (and ``np.linalg.LinAlgError``, to catch a
failure): no ``det``, ``slogdet``, ``inv``, ``pinv``, ``eig``, ``eigh``, ``eigvals``, ``svd`` nor ``lstsq``; no
``multivariate_normal`` either (neither ``np.random.multivariate_normal`` nor the method of a ``Generator``, which
draws ``N(μ, Σ)`` for you), and no SciPy at all (``scipy.stats.multivariate_normal``, ``scipy.linalg.cho_solve``…):
the tests compare your results with them. Your own modules may be imported with a relative import, for instance your
``cholesky`` of M12c (``from .eigen import cholesky``) instead of ``np.linalg.cholesky``. Vectors are 1-D (one vector =
one column of the fiche), several vectors are the rows of a 2-D array of shape ``(n, d)``. A matrix counts as
symmetric when ``|A[i, j] - A[j, i]| ≤ 1e-12 · max(1, max |A|)`` for every entry, as positive definite when its
Cholesky decomposition exists, and as invertible when ``np.linalg.solve`` succeeds on it. Never modify the arrays you
receive. Numbers are returned as Python ``float``, vectors and matrices as ``numpy.ndarray`` of floats.
"""


def mvn_logpdf(x, mean, cov):
    """Return the natural logarithm of the density of ``N(mean, cov)`` at ``x``.

    With ``d`` the dimension, ``μ = mean`` and ``Σ = cov``:
    ``ln p(x) = -½ [d ln(2π) + ln det Σ + (x - μ)ᵀ Σ⁻¹ (x - μ)]``.
    Compute it with the Cholesky factor ``L`` of ``Σ`` (``Σ = L Lᵀ``, M12c), never with ``det`` nor an inverse:
    ``ln det Σ = 2 Σ_i ln L[i, i]``, and the quadratic form is ``‖y‖²``, where ``y`` solves ``L y = x - μ``. The density
    itself is ``np.exp(mvn_logpdf(x, mean, cov))``; in high dimension it underflows to 0, its logarithm does not.

    Parameters
    ----------
    x : 1-D or 2-D array-like
        One point of shape ``(d,)``, or ``n`` points, one per row, of shape ``(n, d)``. In dimension 1, ``n`` points
        form a column ``(n, 1)``: a 1-D ``x`` of length ``n > 1`` is refused (``scipy.stats.multivariate_normal``
        would read it as ``n`` points).
    mean : 1-D array-like
        The mean ``μ``, of length ``d ≥ 1``.
    cov : 2-D array-like
        The ``(d, d)`` covariance matrix ``Σ``, symmetric positive definite.

    Returns
    -------
    float or numpy.ndarray
        A ``float`` for one point; a 1-D array of ``n`` floats (one per row) for a 2-D ``x``.

    Raises
    ------
    ValueError
        If ``mean`` is not 1-D or is empty, if ``cov`` is not ``(d, d)``, not symmetric or not positive definite, or if
        ``x`` is not 1-D or 2-D with ``d`` coordinates.

    Examples
    --------
    >>> round(mvn_logpdf([1, -1], [1, -1], [[2, 3], [3, 9]]), 6)     # at the mean: -ln(2π) - ½ ln 9
    -2.936489
    >>> np.round(mvn_logpdf([[1, -1], [1, 2]], [1, -1], [[2, 3], [3, 9]]), 6)
    array([-2.936489, -3.936489])
    """
    # TODO: check the shapes; L = np.linalg.cholesky(cov) (a LinAlgError means "not positive definite"); the
    #  deviations x - mean, one per row; y = np.linalg.solve(L, deviations.T); then the formula, row by row.
    raise NotImplementedError("mvn_logpdf() is not implemented yet")


def sample_mvn(mean, cov, n, seed=0):
    """Return ``n`` draws of the law ``N(mean, cov)``, one per row, made from independent standard normal draws.

    If ``ε ~ N(0, I)`` and ``Σ = L Lᵀ`` (Cholesky, M12c), then ``μ + L ε ~ N(μ, Σ)``: its mean is ``μ`` and its
    covariance ``L I Lᵀ = Σ``. The draws are fixed by the seed: draw the ``(n, d)`` array ``E`` with **one** call
    ``rng.standard_normal((n, d))``, where ``rng = numpy.random.default_rng(seed)``; row ``i`` of the result is
    ``μ + L E[i]``, that is ``mean + E @ L.T`` for all rows at once (rows hold the vectors). The tests compare your
    draws with ``mean + E @ L.T`` within ``1e-12`` (relative and absolute), not bit for bit: a loop over the rows, or
    your ``cholesky`` of M12c, suits too.

    Parameters
    ----------
    mean : 1-D array-like
        The mean ``μ``, of length ``d ≥ 1``.
    cov : 2-D array-like
        The ``(d, d)`` covariance matrix ``Σ``, symmetric positive definite.
    n : int
        The number of draws, ``n ≥ 1`` (a NumPy integer is accepted; a bool or a float is refused).
    seed : int, default 0
        The seed of ``numpy.random.default_rng``, an integer ``≥ 0`` (a NumPy integer is accepted; a bool, a float
        or ``None`` is refused): the same seed gives the same draws.

    Returns
    -------
    numpy.ndarray
        The ``(n, d)`` array of the draws.

    Raises
    ------
    ValueError
        If ``mean`` is not 1-D or is empty, if ``cov`` is not ``(d, d)``, not symmetric or not positive definite, if
        ``n`` is not an integer ``≥ 1``, or if ``seed`` is not an integer ``≥ 0``.

    Examples
    --------
    >>> X = sample_mvn([1, -1], [[2, 3], [3, 9]], 200_000, seed=2)
    >>> X.shape
    (200000, 2)
    >>> np.round(X.mean(axis=0), 1), np.round(np.cov(X.T, bias=True), 1)
    (array([ 1., -1.]), array([[2., 3.],
           [3., 9.]]))
    """
    # TODO: check the inputs; L = np.linalg.cholesky(cov); one generator, one call to standard_normal((n, d));
    #  then mean + E @ L.T.
    raise NotImplementedError("sample_mvn() is not implemented yet")


def schur_complement(M, idx):
    """Return the Schur complement of the block ``M[idx, idx]`` in the square matrix ``M``.

    Split the indices into ``idx`` (the block ``D = M[idx, idx]``) and the others, ``rest``, in increasing order (the
    block ``A = M[rest, rest]``); ``B = M[rest, idx]`` and ``C = M[idx, rest]``. The Schur complement of ``D`` is
    ``A - B D⁻¹ C``. Two identities make it useful: the block of ``M⁻¹`` on ``rest`` is its inverse (when ``M`` is
    invertible), and
    ``det M = det D · det(A - B D⁻¹ C)``. For a covariance matrix, it is the covariance of the coordinates ``rest``
    once the coordinates ``idx`` are known (``condition_gaussian``). The order of ``idx`` does not change the result.

    Parameters
    ----------
    M : 2-D array-like
        A square ``(m, m)`` matrix, ``m ≥ 2`` (not necessarily symmetric).
    idx : sequence of int
        The indices of the block to eliminate: distinct, between ``0`` and ``m - 1``, at least one and fewer than
        ``m`` (a ``bool`` is refused, and so is a bare ``int``: write ``[2]``).

    Returns
    -------
    numpy.ndarray
        The ``(m - k, m - k)`` matrix ``A - B D⁻¹ C``, where ``k = len(idx)``.

    Raises
    ------
    ValueError
        If ``M`` is not square or is smaller than ``2 × 2``, if ``idx`` is empty, holds every index, a repeated index
        or an index out of range, or if the block ``M[idx, idx]`` is not invertible.

    Examples
    --------
    >>> schur_complement([[5, 2, 2], [2, 4, 0], [2, 0, 4]], [2])
    array([[4., 2.],
           [2., 4.]])
    >>> schur_complement([[5, 2, 2], [2, 4, 0], [2, 0, 4]], [1, 2])
    array([[3.]])
    """
    # TODO: check the inputs; rest = the other indices, in increasing order; the four blocks (np.ix_); then
    #  A - B @ np.linalg.solve(D, C) (a LinAlgError means "D is not invertible").
    raise NotImplementedError("schur_complement() is not implemented yet")


def condition_gaussian(mean, cov, idx, values):
    """Return the law of the coordinates of ``x ~ N(mean, cov)`` that are not in ``idx``, given ``x[idx] = values``.

    With ``a`` the other coordinates (``rest``, in increasing order) and ``b = idx``, the conditional law is normal:
    ``N(μ_a + Σ_ab Σ_bb⁻¹ (values - μ_b), Σ_aa - Σ_ab Σ_bb⁻¹ Σ_ba)``. Its mean is an affine function of the observed
    values; its covariance is the Schur complement of ``Σ_bb`` (``schur_complement(cov, idx)``), which does **not**
    depend on them. The marginal law of the coordinates ``a`` needs no function: it is ``N(μ_a, Σ_aa)``.

    Parameters
    ----------
    mean : 1-D array-like
        The mean ``μ``, of length ``d ≥ 2``.
    cov : 2-D array-like
        The ``(d, d)`` covariance matrix ``Σ``, symmetric positive definite.
    idx : sequence of int
        The indices of the observed coordinates: distinct, between ``0`` and ``d - 1``, at least one and fewer than
        ``d`` (a ``bool`` is refused, and so is a bare ``int``: write ``[2]``).
    values : 1-D array-like
        The ``len(idx)`` observed values, ``values[j]`` for the coordinate ``idx[j]``; a scalar is refused, even when
        ``len(idx) = 1``.

    Returns
    -------
    tuple
        ``(cond_mean, cond_cov)``: the 1-D array of the ``d - k`` conditional means and the ``(d - k, d - k)``
        conditional covariance matrix, where ``k = len(idx)``.

    Raises
    ------
    ValueError
        If ``mean`` is not 1-D or has fewer than 2 values, if ``cov`` is not ``(d, d)``, not symmetric or not positive
        definite, if ``idx`` is not valid (as in ``schur_complement``), or if ``values`` is not 1-D with ``len(idx)``
        numbers.

    Examples
    --------
    >>> m, C = condition_gaussian([1, 0, 2], [[5, 2, 2], [2, 4, 0], [2, 0, 4]], [2], [4])
    >>> m, C
    (array([2., 0.]), array([[4., 2.],
           [2., 4.]]))
    >>> condition_gaussian([1, 0, 2], [[5, 2, 2], [2, 4, 0], [2, 0, 4]], [1, 2], [1, 4])
    (array([2.5]), array([[3.]]))
    """
    # TODO: check the inputs (np.linalg.cholesky tells whether cov is positive definite); the blocks of mean and cov;
    #  the conditional mean with np.linalg.solve(Σ_bb, values - μ_b); the conditional covariance.
    raise NotImplementedError("condition_gaussian() is not implemented yet")


def linreg_posterior(Phi, y, prior_mean, prior_cov, noise_var):
    """Return the posterior law ``N(m_N, S_N)`` of the weights ``θ`` of a Bayesian linear regression.

    The model (MML §9.3): ``θ ~ N(m_0, S_0)`` a priori, then ``y = Φ θ + ε`` with ``ε ~ N(0, σ² I)``, where row ``i``
    of ``Φ`` holds the features of example ``i``. The posterior is normal, with
    ``S_N = (S_0⁻¹ + σ⁻² ΦᵀΦ)⁻¹`` and ``m_N = S_N (S_0⁻¹ m_0 + σ⁻² Φᵀ y)``: precisions add up, and the posterior mean
    weighs the prior mean and the data by their precisions. Without data (``n = 0``), it is the prior itself. When
    ``m_0 = 0`` and ``S_0 = τ² I``, ``m_N`` is the ridge solution of parameter ``λ = σ²/τ²`` (M09b).

    Parameters
    ----------
    Phi : 2-D array-like
        The ``(n, p)`` matrix of the features, ``n ≥ 0`` examples and ``p ≥ 1`` weights.
    y : 1-D array-like
        The ``n`` observed targets.
    prior_mean : 1-D array-like
        ``m_0``, of length ``p``.
    prior_cov : 2-D array-like
        ``S_0``, ``(p, p)``, symmetric positive definite.
    noise_var : float
        The noise variance ``σ² > 0``, a finite number (a variance, not a standard deviation; a ``bool`` is refused).

    Returns
    -------
    tuple
        ``(m_N, S_N)``: the 1-D array of the ``p`` posterior means and the ``(p, p)`` posterior covariance matrix.

    Raises
    ------
    ValueError
        If ``Phi`` is not 2-D or has no column, if the lengths of ``y`` and ``prior_mean`` or the shape of
        ``prior_cov`` do not match ``Phi``, if ``prior_cov`` is not symmetric positive definite, or if ``noise_var`` is
        not a finite number ``> 0``.

    Examples
    --------
    >>> m, S = linreg_posterior([[1, 0], [1, 1], [1, 2]], [1, 2, 2], [0, 0], [[1, 0], [0, 1]], 1.0)
    >>> np.round(m, 4), np.round(S, 4)
    (array([0.8, 0.6]), array([[ 0.4   , -0.2   ],
           [-0.2   ,  0.2667]]))
    >>> linreg_posterior(np.zeros((0, 2)), [], [1, 2], [[1, 0], [0, 1]], 0.5)    # no data: the prior
    (array([1., 2.]), array([[1., 0.],
           [0., 1.]]))
    """
    # TODO: check the inputs; the posterior precision S_0⁻¹ + ΦᵀΦ / σ² (S_0⁻¹ by np.linalg.solve(S_0, I)); S_N by
    #  solving with the identity; then m_N.
    raise NotImplementedError("linreg_posterior() is not implemented yet")
