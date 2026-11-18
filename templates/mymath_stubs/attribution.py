"""Cooperative games, paths and ranks: the weights of the coalitions in the Shapley value, the Harsanyi dividends of a
game, the line integral of a vector field along a polygonal path, and Spearman's rank correlation (chapter MB6).

Conventions for the games. A game has ``n`` players ``0, 1, …, n - 1``. A coalition is a ``frozenset`` of players:
``frozenset()`` is the empty coalition, ``frozenset(range(n))`` the grand coalition. A game is given by its
characteristic function ``v``, a callable that receives a coalition and returns its worth, a finite real number
(``v(frozenset())`` need not be 0). A table ``t`` of worths keyed by frozensets is passed as ``lambda S: t[S]``.

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_mb6_attribution.py``.
NumPy and the modules ``math``, ``fractions`` and ``itertools`` are allowed; SciPy is not (``scipy.stats.rankdata``,
``spearmanr``, ``pearsonr``, ``scipy.integrate``), nor ``np.corrcoef`` and ``np.cov`` (write Pearson's formula on the
ranks, M02c), nor the module ``statistics`` (``statistics.correlation(x, y, method="ranked")`` is Spearman's ρ), nor
pandas: the tests compare your results with ``math.comb`` and ``fractions.Fraction``, with a game rebuilt from its
dividends, with ``scipy.integrate.quad`` on each segment and with ``scipy.stats.spearmanr``. Relative imports of your
own modules are allowed (``from .integrate import simpson``, M02a). Never modify the arrays you receive. Numbers are
returned as Python ``float`` (or ``fractions.Fraction`` when asked for), vectors as ``numpy.ndarray`` of floats.
"""


def coalition_weights(n_players, exact=False):
    """Return the weights ``w[s] = s! (n - 1 - s)! / n!``, ``s = 0, …, n - 1``, of the Shapley value of ``n`` players.

    The Shapley value of player ``i`` is the average of its marginal contribution ``v(S ∪ {i}) - v(S)`` over the
    ``n!`` orders in which the players can arrive, ``S`` being the set of players arrived before ``i``. Grouping the
    orders by ``S`` gives ``φ_i = Σ_S w[|S|] (v(S ∪ {i}) - v(S))``, a sum over the ``2^(n - 1)`` coalitions ``S`` that
    do not contain ``i``: ``w[s]`` is the weight of **one** coalition of size ``s``, the share of the orders in which
    exactly the players of ``S`` come before ``i`` (``s!`` ways to order them, ``(n - 1 - s)!`` for those after).

    Read as probabilities: in an order drawn uniformly, the number of players before ``i`` is uniform on
    ``{0, …, n - 1}``, and given this number ``s``, the set of these players is uniform among the ``C(n - 1, s)``
    possible ones; so ``w[s] = 1 / (n C(n - 1, s))``, ``Σ_s C(n - 1, s) w[s] = 1``, and ``w[s] = w[n - 1 - s]``.

    Parameters
    ----------
    n_players : int
        ``n ≥ 1`` (a NumPy integer is accepted; a bool or a float such as ``4.0`` is refused).
    exact : bool, default False
        ``True`` returns a list of ``fractions.Fraction`` in lowest terms, ``False`` a ``numpy.ndarray`` of floats.

    Returns
    -------
    numpy.ndarray or list of Fraction
        The ``n`` weights ``w[0], …, w[n - 1]``.

    Raises
    ------
    ValueError
        If ``n_players`` is not an integer ``≥ 1``, or if ``exact`` is not a bool.

    Examples
    --------
    >>> coalition_weights(6, exact=True)
    [Fraction(1, 6), Fraction(1, 30), Fraction(1, 60), Fraction(1, 60), Fraction(1, 30), Fraction(1, 6)]
    >>> coalition_weights(2)          # first, or after the other player: half of the two orders each
    array([0.5, 0.5])
    """
    # TODO: check the arguments; the n weights with math.factorial (or math.comb); Fraction(a, b) keeps them exact,
    #  float() converts them.
    raise NotImplementedError("coalition_weights() is not implemented yet")


def harsanyi_dividends(v, n_players):
    """Return the Harsanyi dividends ``d_T`` of the game ``v``, for the ``2^n`` coalitions ``T``.

    ``d_T = Σ_{S ⊆ T} (-1)^(|T| - |S|) v(S)``, a sum over the ``2^|T|`` subsets of ``T`` (a Möbius inversion). It is
    the only family of numbers such that ``v(S) = Σ_{T ⊆ S} d_T`` for every coalition ``S``: the worth of a coalition
    is the sum of the dividends of the coalitions it contains. So ``d_∅ = v(∅)``, ``d_{i} = v({i}) - v(∅)``, and
    ``d_T`` is what the players of ``T`` create together beyond what the smaller coalitions inside ``T`` create (an
    interaction). In other words, ``v = Σ_T d_T u_T``, where the unanimity game ``u_T`` is worth 1 for the coalitions
    that contain ``T`` and 0 for the others.

    Parameters
    ----------
    v : callable
        The characteristic function: ``v(S)``, for a ``frozenset`` ``S`` of players of ``range(n_players)``, is a
        finite real number. It is called once on each of the ``2^n`` coalitions.
    n_players : int
        ``n ≥ 1`` (a NumPy integer is accepted; a bool or a float is refused).

    Returns
    -------
    dict
        ``{T: d_T}`` for the ``2^n`` coalitions ``T`` (``frozenset`` keys, Python ``float`` values), by increasing
        size, and within a size in the order of ``itertools.combinations(range(n_players), size)``.

    Raises
    ------
    ValueError
        If ``n_players`` is not an integer ``≥ 1``, if ``v`` is not callable, or if a worth ``v(S)`` is not a finite
        real number (a bool is refused).

    Examples
    --------
    >>> d = harsanyi_dividends(lambda S: len(S) ** 2, 3)          # a coalition of s players is worth s²
    >>> list(d)[:5]
    [frozenset(), frozenset({0}), frozenset({1}), frozenset({2}), frozenset({0, 1})]
    >>> d[frozenset()], d[frozenset({2})], d[frozenset({0, 2})], d[frozenset({0, 1, 2})]
    (0.0, 1.0, 2.0, 0.0)
    >>> d = harsanyi_dividends(lambda S: 5.0 if {1, 2} <= S else 0.0, 4)     # 5 times a unanimity game
    >>> {tuple(sorted(T)): x for T, x in d.items() if x != 0}
    {(1, 2): 5.0}
    """
    # TODO: check the arguments; list the 2^n coalitions size by size (itertools.combinations) and call v once on
    #  each (keep the worths in a dict); then, for each T, the alternating sum over its subsets.
    raise NotImplementedError("harsanyi_dividends() is not implemented yet")


def line_integral(field, points, n_sub=20):
    """Return the line integral ``∫_γ F · dγ`` of the vector field ``F`` along the polygonal path through ``points``.

    The path ``γ`` goes straight from ``points[0]`` to ``points[1]``, then to ``points[2]``, and so on. On a segment
    from ``a`` to ``b``, parametrized by ``γ(t) = a + t (b - a)`` for ``t`` in ``[0, 1]``, the integral is
    ``∫_0^1 F(a + t (b - a)) · (b - a) dt``, a dot product integrated over ``t``; the result is the sum over the
    segments. When ``F`` is the gradient of a function ``f``, the chain rule makes the integrand the derivative of
    ``t ↦ f(γ(t))``, and the result is ``f(points[-1]) - f(points[0])`` whatever the path (the gradient theorem); a
    field that is not a gradient can give different values along two paths with the same ends.

    Each segment is integrated in ``t`` by Simpson's rule (M02a) with ``n_sub`` intervals of width ``h = 1 / n_sub``:
    ``(h / 3) (g_0 + 4 g_1 + 2 g_2 + 4 g_3 + … + 2 g_{n_sub - 2} + 4 g_{n_sub - 1} + g_{n_sub})``, where
    ``g_k = F(a + k h (b - a)) · (b - a)``. The rule is exact (up to rounding) when ``t ↦ g(t)`` is a polynomial of
    degree at most 3, for example when the coordinates of ``F`` are polynomials of total degree at most 3; for a smooth
    field, its error decreases like ``1 / n_sub⁴``. A segment of length 0 adds 0.

    Parameters
    ----------
    field : callable
        ``F``: called with one point ``p``, a new 1-D float array of length ``d``, it returns the vector ``F(p)``, an
        array-like of shape ``(d,)`` of finite numbers (for ``d = 1`` too: ``[value]``, not a bare number). It is
        called on one point at a time, never on a batch of points.
    points : 2-D array-like
        The ``k ≥ 2`` vertices of the path, one per row: shape ``(k, d)``, ``d ≥ 1``, finite numbers. The path may come
        back on itself, or be closed (its last point equal to the first).
    n_sub : int, default 20
        The number of intervals of Simpson's rule on each segment: even and ``≥ 2`` (a NumPy integer is accepted; a
        bool or a float is refused).

    Returns
    -------
    float
        The line integral.

    Raises
    ------
    ValueError
        If ``points`` is not 2-D with at least 2 rows and 1 column or has an entry that is not finite, if ``n_sub`` is
        not an even integer ``≥ 2``, if ``field`` is not callable, or if it returns something other than an array of
        shape ``(d,)`` of finite numbers.

    Examples
    --------
    >>> F = lambda p: (3 * p[0] ** 2 + p[1], p[0])       # the gradient of f(x, y) = x³ + x y
    >>> round(line_integral(F, [[0, 0], [1, 0], [1, 2]]), 9), round(line_integral(F, [[0, 0], [1, 2]]), 9)
    (3.0, 3.0)
    >>> G = lambda p: (p[1], 0)                          # not a gradient: the value depends on the path
    >>> round(line_integral(G, [[0, 0], [1, 0], [1, 1]]), 9), round(line_integral(G, [[0, 0], [0, 1], [1, 1]]), 9)
    (0.0, 1.0)
    >>> round(line_integral(lambda p: [3 * p[0] ** 2], [[1], [3], [-1]], n_sub=2), 9)    # forth and back, d = 1
    -2.0
    """
    # TODO: check the arguments; the n_sub + 1 values of t and the Simpson weights 1, 4, 2, …, 2, 4, 1 times h / 3;
    #  for each segment, the dot products F(a + t (b - a)) · (b - a) at these t; add the weighted sums.
    raise NotImplementedError("line_integral() is not implemented yet")


def spearman_rho(x, y):
    """Return Spearman's rank correlation ``ρ`` of two paired samples ``x`` and ``y``.

    Each sample is replaced by its ranks: the smallest value gets rank 1, the next one rank 2, and so on, and tied
    values (exactly equal) share the average of the ranks they occupy (two values tied for the 3rd and 4th places both
    get 3.5). Then ``ρ`` is Pearson's correlation of the two vectors of ranks ``r`` and ``s`` (M02c),
    ``ρ = Σ (r_i - r̄)(s_i - s̄) / √(Σ (r_i - r̄)² · Σ (s_i - s̄)²)``; without ties, it equals
    ``1 - 6 Σ (r_i - s_i)² / (n (n² - 1))``. ``ρ`` depends only on the order of each sample: it does not change when
    a strictly increasing function is applied to the values of ``x`` or of ``y``.

    Parameters
    ----------
    x, y : 1-D array-like
        Two samples of the same length ``n ≥ 2``, of finite numbers; ``x[i]`` and ``y[i]`` describe the same item.

    Returns
    -------
    float
        ``ρ``, in ``[-1, 1]``; ``nan`` when all the values of ``x``, or all those of ``y``, are equal (the ranks are
        then constant, and Pearson's correlation is not defined).

    Raises
    ------
    ValueError
        If ``x`` or ``y`` is not 1-D, if their lengths differ or are smaller than 2, or if an entry is not finite.

    Examples
    --------
    >>> round(spearman_rho([0.5, 2.0, 1.5, 4.0], [1, 8, 27, 64]), 9)    # ranks (1, 3, 2, 4) and (1, 2, 3, 4)
    0.8
    >>> round(spearman_rho([2, 2, 5, 1], [4, 3, 6, 0]), 6)              # ranks (2.5, 2.5, 4, 1) and (3, 2, 4, 1)
    0.948683
    >>> spearman_rho([7, 7, 7], [1, 2, 3])
    nan
    """
    # TODO: check x and y; the ranks of each sample (np.argsort, then give each group of equal values the mean of
    #  their places, counted from 1); center them; Pearson's formula; nan when a sum of squares is 0.
    raise NotImplementedError("spearman_rho() is not implemented yet")
