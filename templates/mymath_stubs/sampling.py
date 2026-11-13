"""Gram matrices and modified categorical laws: a configuration of points with a given Gram matrix, a law tempered
from its probabilities, and the smallest set of outcomes that reaches a given probability mass (chapter M28).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m28_sampling.py``.
NumPy is allowed, but from ``np.linalg`` only ``eigh`` (in ``points_from_gram``, M12c), and no SciPy nor
scikit-learn (``scipy.special.softmax``, ``scipy.special.logsumexp``, ``scipy.linalg``, ``sklearn.manifold``…): the
tests compare your results with SciPy. Points are the rows of a matrix (as in M13b). A law on ``K`` outcomes is given
by its **probabilities**, never by scores (logits): a 1-D array of ``K ≥ 1`` non-negative numbers summing to 1
(up to 1e-9). Nothing here draws at random: these functions prepare the law that a categorical draw (M02b) then
uses. Never modify the arrays you receive. Vectors and matrices are returned as ``numpy.ndarray`` of floats, sets of
indices as ``numpy.ndarray`` of integers.
"""


def points_from_gram(G, dim=None, tol=1e-9):
    """Return ``n`` points (the rows of ``X``) whose Gram matrix ``X Xᵀ`` is ``G``.

    ``G[i, j]`` is the dot product of points ``i`` and ``j``. A Gram matrix is symmetric and positive semi-definite,
    and every such matrix is a Gram matrix: with ``G = Q Λ Qᵀ`` (spectral theorem, eigenvalues
    ``λ_1 ≥ λ_2 ≥ … ≥ λ_n``), column ``k`` of ``X`` is ``√λ_k`` times the ``k``-th unit eigenvector, and
    ``X Xᵀ = Q Λ Qᵀ = G``. With as many columns as the rank of ``G`` (the default), any other configuration with the
    same Gram matrix is ``X R`` for a matrix ``R`` with orthonormal rows (an orthogonal matrix when both have the same
    number of columns): the points are found up to an isometry that fixes the origin (a rotation, possibly with a
    reflection). The columns
    come by decreasing eigenvalue: the first one is the direction of largest mean square (the first principal axis
    when the points are centered).

    The threshold ``s = tol · max(1, max |G[i, j]|)`` decides three things: ``G`` counts as symmetric when
    ``|G[i, j] - G[j, i]| ≤ s`` everywhere, an eigenvalue below ``-s`` means that ``G`` is no Gram matrix, and the
    eigenvalues in ``[-s, s]`` count as 0.

    Parameters
    ----------
    G : 2-D array-like
        A symmetric ``(n, n)`` matrix, ``n ≥ 1``, positive semi-definite up to rounding.
    dim : int, optional
        The number of columns of ``X``, ``1 ≤ dim ≤ n``. When omitted, it is the rank of ``G``, the number of
        eigenvalues larger than ``s`` (at least 1). The columns of the eigenvalues that count as 0 are zero; with
        ``dim`` smaller than the rank, ``X Xᵀ`` is the best approximation of ``G`` of rank ``dim`` (Eckart-Young, M12d).
    tol : float, default 1e-9
        The relative tolerance, ``tol ≥ 0``.

    Returns
    -------
    numpy.ndarray
        ``X``, of shape ``(n, dim)``, of floats. In each column, the first coordinate of absolute value ``> 1e-8`` is
        positive. When an eigenvalue is repeated, its columns are one choice among many (any rotation of them suits):
        compare Gram matrices or distances, never coordinates.

    Raises
    ------
    ValueError
        If ``G`` is not a square 2-D matrix or is empty, if it is not symmetric, if it has an eigenvalue below ``-s``
        (it is not positive semi-definite), if ``dim`` is not an integer between 1 and ``n`` (a ``bool`` is refused),
        or if ``tol < 0``.

    Examples
    --------
    >>> np.round(points_from_gram([[13, 5], [5, 13]]), 4)    # two vectors of length √13 with cosine 5/13
    array([[ 3.,  2.],
           [ 3., -2.]])
    >>> np.round(points_from_gram([[1, 2, 3], [2, 4, 6], [3, 6, 9]]), 6)   # rank 1: three points on a line
    array([[1.],
           [2.],
           [3.]])
    >>> points_from_gram([[1, 2, 3], [2, 4, 6], [3, 6, 9]], dim=2).shape   # a zero second column
    (3, 2)
    """
    # TODO: check G, dim and tol; the eigenvalues and unit eigenvectors (np.linalg.eigh, which sorts them in increasing
    #  order: reverse it); refuse an eigenvalue below -s; set those in [-s, s] to 0; keep dim columns; multiply each
    #  eigenvector by the square root of its eigenvalue; then the sign convention, column by column.
    raise NotImplementedError("points_from_gram() is not implemented yet")


def temper(p, temperature):
    """Return the law ``p`` at the temperature ``T``: ``q_i = p_i^(1/T) / Σ_j p_j^(1/T)``.

    It is the Boltzmann law (M17) of the energies ``E_i = -ln p_i`` at the temperature ``T``: ``T = 1`` gives ``p``
    back, ``T < 1`` sharpens it (the probable outcomes gain), ``T > 1`` flattens it. The order of the outcomes never
    changes, and an outcome of probability 0 keeps probability 0 (its energy is infinite). Both limits are allowed:

    - ``T = 0``: the uniform law on the most probable outcomes (shared equally between ties);
    - ``T = np.inf``: the uniform law on the outcomes of positive probability.

    The powers are computed through logarithms, ``ln q_i = (ln p_i - ln p_max) / T - c``, where ``p_max`` is the
    largest ``p_j`` and ``c`` the logarithm of the normalizing sum: the largest term is then 0 (as in log-sum-exp,
    M05a), so that a small ``T`` does not underflow to ``0 / 0``.

    Parameters
    ----------
    p : 1-D array-like
        A law on ``K ≥ 1`` outcomes: non-negative numbers summing to 1 (up to 1e-9).
    temperature : float
        ``T ≥ 0``; ``np.inf`` is allowed, ``nan`` and a ``bool`` are refused.

    Returns
    -------
    numpy.ndarray
        The ``K`` probabilities of the tempered law, of floats.

    Raises
    ------
    ValueError
        If ``p`` is not 1-D, is empty, has a negative entry or does not sum to 1, or if the temperature is negative,
        ``nan`` or a ``bool``.

    Examples
    --------
    >>> temper([0.5, 0.25, 0.25, 0.0], 1 / 3)       # cubes, renormalized; the zero stays
    array([0.8, 0.1, 0.1, 0. ])
    >>> np.round(temper([0.5, 0.25, 0.25, 0.0], 3), 4)      # cube roots, renormalized
    array([0.3865, 0.3068, 0.3068, 0.    ])
    >>> temper([0.4, 0.4, 0.2], 0), temper([0.7, 0.3, 0.0], np.inf)
    (array([0.5, 0.5, 0. ]), array([0.5, 0.5, 0. ]))
    """
    # TODO: check p and T; T = 0 and T = inf first (where is p maximal? where is it positive?); otherwise the
    #  logarithms of the positive p_i minus their maximum, divided by T, then exp and divide by the sum; 0 elsewhere.
    raise NotImplementedError("temper() is not implemented yet")


def smallest_mass_set(p, mass):
    """Return the indices of a smallest set of outcomes whose total probability is at least ``mass``.

    The outcomes are taken by decreasing probability (between equal probabilities, the smaller index first) until
    their cumulative probability reaches ``mass``; the outcome that makes it cross ``mass`` is kept. No set with fewer
    outcomes reaches ``mass`` (an exchange argument). It is the *highest-probability set* of mass ``mass`` (M28 §5);
    top-p (*nucleus*) sampling keeps this set.

    A cumulative probability within ``1e-9`` of ``mass`` counts as reaching it (in floats, ``0.4 + 0.3 + 0.2`` is
    ``0.8999999999999999``). If it never does (possible only through rounding, for a ``mass`` close to 1), the set is
    every outcome of positive probability.

    Parameters
    ----------
    p : 1-D array-like
        A law on ``K ≥ 1`` outcomes: non-negative numbers summing to 1 (up to 1e-9).
    mass : float
        ``0 < mass ≤ 1``; ``nan`` and a ``bool`` are refused.

    Returns
    -------
    numpy.ndarray
        The indices of the set (integers), by decreasing probability. It never holds an outcome of probability 0.

    Raises
    ------
    ValueError
        If ``p`` is not 1-D, is empty, has a negative entry or does not sum to 1, or if ``mass`` is not in ``]0, 1]``.

    Examples
    --------
    >>> smallest_mass_set([0.1, 0.42, 0.08, 0.4], 0.5)      # 0.42 < 0.5, then 0.42 + 0.4 = 0.82
    array([1, 3])
    >>> smallest_mass_set([0.02, 0.93, 0.05], 0.6)          # a confident law: a single outcome
    array([1])
    """
    # TODO: check p and mass; take the outcomes by decreasing probability (ties: smaller index first) and add up their
    #  probabilities until the total reaches mass - 1e-9; keep the outcomes taken so far.
    raise NotImplementedError("smallest_mass_set() is not implemented yet")
