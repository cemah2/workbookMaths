"""Ranks of two kinds: the rank factorization of a matrix (a matrix of rank ``r`` is a product ``C F`` through ``r``
columns and ``r`` rows), the Borda points of several rankings, and the exact mean reciprocal rank of a random order
(chapter MB4).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_mb4_ranks.py``.
NumPy is allowed (``@`` included), but nothing from ``np.linalg`` (neither ``matrix_rank``, ``svd``, ``qr``,
``lstsq``, ``solve``, ``inv`` nor ``pinv``), no SciPy (``scipy.linalg``, ``scipy.stats.rankdata``…) and no SymPy:
the tests compare your results with them. ``rank_factorization`` reduces the matrix as your ``rref`` of M09a does
(you may copy it into a private helper ``_rref``). ``random_ranking_mrr`` computes exactly, with
``fractions.Fraction`` and ``math.comb``, and never lists the ``n!`` orders (``itertools.permutations`` is an oracle
of the tests). Candidates (or items) are numbered ``0, …, n - 1``; a ranking lists them best first; a rank (a
position in a ranking) starts at 1. Never modify the arrays you receive. Matrices are returned as ``numpy.ndarray``
of floats, points as ``numpy.ndarray`` of integers, exact values as ``fractions.Fraction``.
"""


def rank_factorization(M, tol=1e-10):
    """Return a factorization ``M = C F`` of an ``(m, n)`` matrix of rank ``r``, through ``r`` columns and ``r`` rows.

    ``C`` (``m × r``) is made of the pivot columns of ``M`` itself, in increasing order of index: a basis of the
    column space of ``M`` (``column_space_basis`` of M12a). ``F`` (``r × n``) is made of the ``r`` non-zero rows of
    the reduced row echelon form of ``M`` (``rref`` of M09a); in the pivot columns, it is the identity:
    ``F[:, pivots]`` is ``I_r``. Then ``C F = M`` (MB4 §1 shows why).

    Every matrix of rank ``r`` is such a product, and no product ``C F`` whose ``C`` has fewer than ``r`` columns
    gives it, since ``rank(C F) ≤`` the number of columns of ``C`` (M12a). The factorization is not unique: for any
    invertible ``r × r`` matrix ``G``, ``(C G)(G⁻¹ F)`` is another one. This function returns the one whose ``C`` is
    made of columns of ``M``.

    The row reduction is the one of ``rref``: column by column from the left, with partial pivoting (the entry of
    largest absolute value at or below the current row); a column whose candidates are all at most ``tol`` in
    absolute value has no pivot; at the end, the entries of the reduced form at most ``tol`` in absolute value are
    set to 0. For a matrix of measurements, ``tol`` decides which columns count as combinations of the previous
    ones: the rank found is a numerical rank (M12a).

    Parameters
    ----------
    M : 2-D array-like
        An ``(m, n)`` matrix of finite numbers, ``m ≥ 1`` and ``n ≥ 1``.
    tol : float, default 1e-10
        Below this absolute value, an entry counts as zero during the row reduction; ``tol ≥ 0``.

    Returns
    -------
    tuple
        ``(C, F)``: two arrays of floats, ``C`` of shape ``(m, r)`` and ``F`` of shape ``(r, n)``, where ``r`` is the
        number of pivots. For a zero matrix, ``r = 0``: the shapes are ``(m, 0)`` and ``(0, n)``, and ``C @ F`` is
        the ``(m, n)`` zero matrix.

    Raises
    ------
    ValueError
        If ``M`` is not 2-D, is empty or holds an entry that is not a finite number, or if ``tol`` is negative,
        ``nan`` or a ``bool``.

    Examples
    --------
    >>> C, F = rank_factorization([[1, 3, 0, 1], [0, 0, 1, -1], [2, 6, 1, 1]])   # row 3 = 2 × row 1 + row 2
    >>> C
    array([[1., 0.],
           [0., 1.],
           [2., 1.]])
    >>> F
    array([[ 1.,  3.,  0.,  1.],
           [ 0.,  0.,  1., -1.]])
    >>> rank_factorization([[2, -4], [-3, 6]])                     # a column times a row: rank 1
    (array([[ 2.],
           [-3.]]), array([[ 1., -2.]]))
    >>> [a.shape for a in rank_factorization([[0, 0, 0], [0, 0, 0]])]
    [(2, 0), (0, 3)]
    """
    # TODO: check M and tol; reduce a float copy of M as rref does, and keep its pivot columns; then C = those
    #  columns of the original M, and F = the first r rows of the reduced form (r = the number of pivots).
    raise NotImplementedError("rank_factorization() is not implemented yet")


def borda_scores(rankings):
    """Return the Borda points of ``n`` candidates ranked by ``m`` judges.

    Each judge ranks all the candidates, best first. In a ranking of ``n`` candidates, the candidate at rank ``j``
    (``j = 1`` for the first) gets ``n - j`` points: ``n - 1`` for the first, ``0`` for the last. The Borda points of
    a candidate add up its points over the judges: they are ``m n`` minus the sum of its ranks, so that ordering the
    candidates by decreasing Borda points is ordering them by increasing sum of ranks. Only the order chosen by each
    judge counts, never the gaps between the candidates: two sets of marks that differ by an increasing
    transformation (another scale, another unit) give the same rankings, hence the same points.

    Parameters
    ----------
    rankings : 2-D array-like of int
        An ``(m, n)`` array, ``m ≥ 1`` and ``n ≥ 1``: row ``i`` lists the candidates ``0, …, n - 1`` in the order
        of judge ``i``, best first. Each row is a permutation of ``0, …, n - 1``; a row is **not** the list of the
        ranks of the candidates.

    Returns
    -------
    numpy.ndarray
        The ``n`` Borda points, as integers, indexed by candidate: entry ``c`` holds the points of candidate ``c``.

    Raises
    ------
    ValueError
        If ``rankings`` is not 2-D or is empty, if it is an array of booleans or of non-integers (``2.0`` is
        refused), or if a row is not a permutation of ``0, …, n - 1``.

    Examples
    --------
    >>> borda_scores([[2, 0, 1], [0, 2, 1], [2, 1, 0]])     # candidate 2 is first for two judges out of three
    array([3, 1, 5])
    >>> borda_scores([[3, 1, 0, 2]])     # one judge: candidate 3 first (3 points), candidate 2 last (0 point)
    array([1, 2, 0, 3])
    """
    # TODO: check the array (2-D, integers, each row a permutation of 0, …, n - 1); then, row by row, the candidate
    #  at position p (positions from 0) gets n - 1 - p points; add up over the rows.
    raise NotImplementedError("borda_scores() is not implemented yet")


def random_ranking_mrr(n, n_relevant=1, depth=None):
    """Return the exact expected reciprocal rank ``E[1/R]`` of the first relevant item in an order drawn at random.

    ``n`` items, ``q = n_relevant`` of which are relevant, are put in an order drawn uniformly among the ``n!``
    orders: a ranking that knows nothing. ``R`` is the rank (from 1) of the first relevant item. The positions of the
    ``q`` relevant items are ``q`` positions drawn uniformly among ``n``, so ``P(R = j) = C(n - j, q - 1) / C(n, q)``
    for ``j = 1, …, n - q + 1`` (one relevant item at ``j``, the ``q - 1`` others after it), and the function returns
    ``Σ_j P(R = j) / j``. It is the mean reciprocal rank that a random ranking scores on average: the baseline that
    any ranking should beat. For a single relevant item, ``R`` is uniform on ``{1, …, n}`` and
    ``E[1/R] = H_n / n``, with ``H_n = 1 + 1/2 + … + 1/n``.

    With ``depth = k``, only the first ``k`` items are shown: the reciprocal rank counts 0 when the first relevant
    item comes after rank ``k``, and the sum stops at ``j = k``.

    Parameters
    ----------
    n : int
        The number of items, ``n ≥ 1``.
    n_relevant : int, default 1
        The number ``q`` of relevant items, ``1 ≤ q ≤ n``.
    depth : int, optional
        The number ``k ≥ 1`` of items shown; all of them when omitted (a ``depth`` above ``n`` changes nothing).

    The three arguments are integers: a NumPy integer is accepted, a ``bool`` or a float such as ``3.0`` is refused.

    Returns
    -------
    fractions.Fraction
        The exact value, in ``]0, 1]``.

    Raises
    ------
    ValueError
        If ``n``, ``n_relevant`` or ``depth`` is not an integer, or is out of its range.

    Examples
    --------
    >>> random_ranking_mrr(4)                    # (1 + 1/2 + 1/3 + 1/4) / 4
    Fraction(25, 48)
    >>> random_ranking_mrr(5, n_relevant=2)
    Fraction(77, 120)
    >>> random_ranking_mrr(4, depth=2)           # (1 + 1/2) / 4: the first relevant item at rank 3 or 4 counts 0
    Fraction(3, 8)
    """
    # TODO: check n, n_relevant and depth (integers, not bools); then, for each rank j that counts (from 1 to
    #  n - q + 1, or to depth if it is smaller), add P(R = j) / j as a Fraction (math.comb for the binomials).
    raise NotImplementedError("random_ranking_mrr() is not implemented yet")
