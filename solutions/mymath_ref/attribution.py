"""Cooperative games, paths and ranks: the weights of the coalitions in the Shapley value, the Harsanyi dividends of a
game, the line integral of a vector field along a polygonal path, and Spearman's rank correlation (chapter MB6).

Conventions for the games. A game has ``n`` players ``0, 1, …, n - 1``. A coalition is a ``frozenset`` of players:
``frozenset()`` is the empty coalition, ``frozenset(range(n))`` the grand coalition. A game is given by its
characteristic function ``v``, a callable that receives a coalition and returns its worth, a finite real number
(``v(frozenset())`` need not be 0). A table ``t`` of worths keyed by frozensets is passed as ``lambda S: t[S]``.

Reference implementation (solutions/mymath_ref).
NumPy and the modules ``math``, ``fractions`` and ``itertools`` are allowed; SciPy is not (``scipy.stats.rankdata``,
``spearmanr``, ``pearsonr``, ``scipy.integrate``), nor ``np.corrcoef`` and ``np.cov`` (write Pearson's formula on the
ranks, M02c), nor the module ``statistics`` (``statistics.correlation(x, y, method="ranked")`` is Spearman's ρ), nor
pandas: the tests compare your results with ``math.comb`` and ``fractions.Fraction``, with a game rebuilt from its
dividends, with ``scipy.integrate.quad`` on each segment and with ``scipy.stats.spearmanr``. Relative imports of your
own modules are allowed (``from .integrate import simpson``, M02a). Never modify the arrays you receive. Numbers are
returned as Python ``float`` (or ``fractions.Fraction`` when asked for), vectors as ``numpy.ndarray`` of floats.
"""

import itertools
import math
from fractions import Fraction

import numpy as np

from .integrate import simpson


def _is_bool(value):
    """Whether value is a bool or a NumPy bool (True == 1, but a bool is not a number here)."""
    return isinstance(value, (bool, np.bool_))


def _players(n_players):
    """n_players as a Python int ≥ 1 (a Python or NumPy integer; a bool or a float is refused), or ValueError."""
    if _is_bool(n_players) or not isinstance(n_players, (int, np.integer)):
        raise ValueError(f"n_players must be an integer ≥ 1 (not a bool, not a float such as 3.0), got {n_players!r}")
    if n_players < 1:
        raise ValueError(f"n_players must be an integer ≥ 1, got {n_players!r}")
    return int(n_players)


def _name(coalition):
    """A coalition written for a message: ∅ or {0, 2}."""
    return "{" + ", ".join(map(str, sorted(coalition))) + "}" if coalition else "∅"


def _worth(value, coalition):
    """v(S) as a finite Python float (a Python or NumPy real number, or a Fraction; a bool, a string, a complex
    number, None or an array is refused), or ValueError."""
    if _is_bool(value) or not isinstance(value, (int, float, Fraction, np.integer, np.floating)):
        raise ValueError(f"v({_name(coalition)}) must be a finite real number (not a bool), got {value!r}")
    try:
        x = float(value)
    except (OverflowError, ValueError):
        raise ValueError(f"v({_name(coalition)}) must be a finite real number, got {value!r}") from None
    if not math.isfinite(x):
        raise ValueError(f"v({_name(coalition)}) must be a finite real number, got {value!r}")
    return x


def _floats(values, what):
    """values as a NEW float array of finite numbers, of its own shape (never a view of what was received), or
    ValueError; booleans, strings and complex numbers are refused."""
    if values is None or _is_bool(values):
        raise ValueError(f"{what} must hold finite real numbers, got {values!r}")
    try:
        raw = np.asarray(values)
    except (TypeError, ValueError):             # a ragged list
        raise ValueError(f"{what} must be an array (rows of the same length) of finite real numbers") from None
    if raw.dtype.kind in "bcUSaV":
        raise ValueError(f"{what} must hold real numbers (not booleans, strings or complex numbers), got dtype "
                         f"{raw.dtype}")
    try:
        X = np.array(raw, dtype=float)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(f"{what} must hold finite real numbers") from None
    if not np.all(np.isfinite(X)):
        raise ValueError(f"{what} must hold finite numbers only (no nan, no inf)")
    return X


def _intervals(n_sub):
    """n_sub as a Python int, even and ≥ 2 (a Python or NumPy integer; a bool or a float is refused), or ValueError."""
    if _is_bool(n_sub) or not isinstance(n_sub, (int, np.integer)):
        raise ValueError(f"n_sub must be an even integer ≥ 2 (not a bool, not a float such as 8.0), got {n_sub!r}")
    if n_sub < 2 or n_sub % 2 != 0:
        raise ValueError(f"n_sub must be an even integer ≥ 2 (Simpson's rule takes the intervals two by two), got "
                         f"{n_sub!r}")
    return int(n_sub)


def _field_value(field, p, d):
    """F(p) as a float array of shape (d,) of finite numbers, or ValueError."""
    value = field(p)
    if value is None or _is_bool(value):
        raise ValueError(f"the field must return an array of shape ({d},) of finite numbers, got {value!r} at {p}")
    try:
        raw = np.asarray(value)
    except (TypeError, ValueError):             # a ragged list
        raise ValueError(f"the field must return an array of shape ({d},) of finite numbers at {p}") from None
    if raw.dtype.kind in "bcUSaV":
        raise ValueError(f"the field must return finite real numbers (not booleans, strings or complex numbers), "
                         f"got dtype {raw.dtype} at {p}")
    try:
        F = np.array(raw, dtype=float)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(f"the field must return an array of shape ({d},) of finite numbers at {p}") from None
    if F.shape != (d,):
        raise ValueError(f"the field must return an array of shape ({d},) (for d = 1 too: [value], not a bare "
                         f"number), got the shape {F.shape} at {p}")
    if not np.all(np.isfinite(F)):
        raise ValueError(f"the field must return finite numbers, got {F} at {p}")
    return F


def _ranks(X):
    """The ranks of the values of X, from 1, tied values (exactly equal) sharing the mean of the places they occupy."""
    n = X.size
    order = np.argsort(X, kind="stable")        # order[j]: the index of the value at place j + 1
    ordered = X[order]
    first = np.ones(n, dtype=bool)
    first[1:] = ordered[1:] != ordered[:-1]     # the first place of each run of equal values
    starts = np.flatnonzero(first)              # runs occupy the places starts + 1, …, ends (from 1)
    ends = np.append(starts[1:], n)
    ranks = np.empty(n)
    ranks[order] = np.repeat((starts + 1 + ends) / 2, ends - starts)   # the mean of the places of each run
    return ranks


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
    n = _players(n_players)
    if not _is_bool(exact):
        raise ValueError(f"exact must be a bool (True or False), got {exact!r}")
    total = math.factorial(n)
    weights = [Fraction(math.factorial(s) * math.factorial(n - 1 - s), total) for s in range(n)]   # exact, reduced
    if exact:
        return weights
    return np.array([float(w) for w in weights])


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
    n = _players(n_players)
    if not callable(v):
        raise ValueError(f"v must be a callable (the characteristic function), got {type(v).__name__}")
    coalitions = [frozenset(c) for size in range(n + 1) for c in itertools.combinations(range(n), size)]
    worths = {S: _worth(v(S), S) for S in coalitions}           # v is called once on each coalition
    # Möbius inversion on the bitmasks of the coalitions: after the pass over player i, entry T holds the alternating
    # sum over the subsets of T that differ from T only by players 0, …, i (n passes instead of 3^n terms)
    table = np.zeros(2 ** n)
    masks = [sum(1 << i for i in S) for S in coalitions]
    table[masks] = [worths[S] for S in coalitions]
    for i in range(n):
        view = table.reshape(-1, 2, 2 ** i)                     # [:, 1, :] holds the coalitions that contain i
        view[:, 1, :] -= view[:, 0, :]
    return {S: float(table[mask]) for S, mask in zip(coalitions, masks)}


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
    P = _floats(points, "points")
    if P.ndim != 2 or P.shape[0] < 2 or P.shape[1] < 1:
        raise ValueError(f"points must be a 2-D array of k ≥ 2 rows (the vertices) and d ≥ 1 columns, got an array of "
                         f"shape {P.shape}")
    n = _intervals(n_sub)
    if not callable(field):
        raise ValueError(f"field must be a callable (p ↦ F(p)), got {type(field).__name__}")
    d = P.shape[1]
    total = 0.0
    for a, b in itertools.pairwise(P):        # the segments, one after the other
        chord = b - a                           # γ(t) = a + t (b - a), γ'(t) = b - a

        def g(t, a=a, chord=chord):             # a + t * chord is a new array at each call
            return float(_field_value(field, a + t * chord, d) @ chord)

        total += simpson(g, 0.0, 1.0, n)        # nodes t = k / n, k = 0, …, n (M02a)
    return float(total)


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
    X = _floats(x, "x")
    Y = _floats(y, "y")
    if X.ndim != 1 or Y.ndim != 1:
        raise ValueError(f"x and y must be 1-D, got the shapes {X.shape} and {Y.shape}")
    if X.size != Y.size:
        raise ValueError(f"x and y must have the same length, got {X.size} and {Y.size}")
    n = X.size
    if n < 2:
        raise ValueError(f"x and y must hold at least 2 values each, got {n}")
    r = _ranks(X) - (n + 1) / 2                 # the ranks centred: their mean is always (n + 1) / 2
    s = _ranks(Y) - (n + 1) / 2
    srr, sss = float(r @ r), float(s @ s)
    if srr == 0.0 or sss == 0.0:                # all the values of x, or all those of y, are equal
        return math.nan
    rho = float(r @ s) / math.sqrt(srr * sss)
    return float(min(1.0, max(-1.0, rho)))      # a rounding never takes it out of [-1, 1]
