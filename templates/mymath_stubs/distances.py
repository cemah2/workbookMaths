"""Zero-sum games and distances between laws: the values of a matrix game in pure strategies, the optimal mixed
strategies of a 2 × 2 game, the iterates of gradient descent-ascent on a bilinear game, and the 2-Wasserstein
distance between two normal laws on the line (chapter M27).

Convention for the games: ``G[i, j]`` is what the row player wins, and the column player loses (a zero-sum game),
when row ``i`` meets column ``j``; the row player maximizes, the column player minimizes.

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m27_distances.py``.
NumPy and the module ``math`` are allowed, but nothing from ``np.linalg`` and no SciPy at all (``scipy.optimize``
solves a matrix game): the tests compare your results with ``scipy.optimize.linprog``, with
``np.linalg.matrix_power`` and with the integral of the squared gap between two quantile functions
(``scipy.integrate.quad`` and ``scipy.stats.norm.ppf``). Never modify the arrays you receive. Numbers are returned as
Python ``float``, indices as Python ``int``, iterates as ``numpy.ndarray`` of floats.
"""


def pure_strategy_values(G):
    """Return ``(maximin, minimax, row, col)``, the values in pure strategies of the zero-sum game of matrix ``G``.

    ``G[i, j]`` is what the row player wins (and the column player loses) when row ``i`` meets column ``j``: the
    row player maximizes, the column player minimizes.

    - ``maximin = max_i min_j G[i, j]`` is what the row player can guarantee by playing ``row``, whatever the
      column; ``row`` is the smallest index of a row whose minimum is ``maximin``.
    - ``minimax = min_j max_i G[i, j]`` is the most the column player can be forced to pay by playing ``col``;
      ``col`` is the smallest index of a column whose maximum is ``minimax``.

    Always ``maximin ≤ minimax``. They are equal if and only if the game has a saddle point (an entry that is the
    smallest of its row and the largest of its column), and then ``(row, col)`` is one.

    Parameters
    ----------
    G : 2-D array-like
        The ``(m, n)`` payoff matrix, ``m, n ≥ 1``, of finite numbers.

    Returns
    -------
    tuple
        ``(maximin, minimax, row, col)``: two Python ``float`` and two Python ``int``.

    Raises
    ------
    ValueError
        If ``G`` is not 2-D, is empty, or has an entry that is not a finite number.

    Examples
    --------
    >>> pure_strategy_values([[7, -4, 1], [-1, 5, 6]])
    (-1.0, 5.0, 1, 1)
    >>> pure_strategy_values([[1, 6, 2], [4, 5, 4], [0, 8, 3]])      # saddle points (1, 0) and (1, 2)
    (4.0, 4.0, 1, 0)
    """
    # TODO: a float array, checked; the minimum of each row (axis=1) and the maximum of each column
    #  (axis=0); np.argmax and np.argmin return the smallest index of a tie; convert to float and int.
    raise NotImplementedError("pure_strategy_values() is not implemented yet")


def mixed_strategy_value_2x2(G):
    """Return ``(p, q, value)``: optimal mixed strategies and value of the 2 × 2 zero-sum game of matrix ``G``.

    ``G = [[a, b], [c, d]]`` is what the row player wins (same convention as ``pure_strategy_values``). The row
    player plays row 0 with probability ``p`` and row 1 with probability ``1 - p``; the column player plays column
    0 with probability ``q`` and column 1 with probability ``1 - q``, independently.

    - If the game has a saddle point (``maximin == minimax`` in ``pure_strategy_values``), the pure strategies
      ``row`` and ``col`` of ``pure_strategy_values`` are optimal: ``p = 1.0`` if ``row == 0`` else ``0.0``,
      ``q = 1.0`` if ``col == 0`` else ``0.0``, and ``value = maximin``.
    - Otherwise ``a - b - c + d ≠ 0``, and the optimal strategies are those that make the opponent indifferent
      between its two moves: ``p = (d - c) / (a - b - c + d)``, ``q = (d - b) / (a - b - c + d)``, both strictly
      between 0 and 1, and ``value = (a d - b c) / (a - b - c + d)``.

    In both cases the row player's strategy wins at least ``value`` on average against any column, and the column
    player's strategy pays at most ``value`` on average against any row (von Neumann's minimax theorem).

    Parameters
    ----------
    G : 2-D array-like
        The ``(2, 2)`` payoff matrix, of finite numbers.

    Returns
    -------
    tuple
        ``(p, q, value)``, three Python ``float``.

    Raises
    ------
    ValueError
        If ``G`` is not ``(2, 2)`` or has an entry that is not a finite number.

    Examples
    --------
    >>> mixed_strategy_value_2x2([[4, -2], [-1, 3]])
    (0.4, 0.5, 1.0)
    >>> mixed_strategy_value_2x2([[-1, 2], [5, 6]])                    # saddle point (1, 0)
    (0.0, 1.0, 5.0)
    """
    # TODO: check the shape; pure_strategy_values first: a saddle point gives pure strategies; otherwise
    #  a, b, c, d = the four entries, and the three indifference formulas.
    raise NotImplementedError("mixed_strategy_value_2x2() is not implemented yet")


def descent_ascent_iterates(A, x0, y0, eta, n_steps=10, alternating=False):
    """Return the iterates of gradient descent-ascent on the bilinear game ``f(x, y) = xᵀ A y``.

    The player ``x`` wants ``f`` small, the player ``y`` wants it large: ``x`` takes a step down its gradient
    ``A y``, ``y`` a step up its gradient ``Aᵀ x``, with the same step ``eta``.

    - Simultaneous (``alternating=False``): ``x_{k+1} = x_k - eta A y_k`` and ``y_{k+1} = y_k + eta Aᵀ x_k``, both
      computed from the old pair.
    - Alternating (``alternating=True``): ``x_{k+1} = x_k - eta A y_k``, then ``y_{k+1} = y_k + eta Aᵀ x_{k+1}``,
      which already sees the new ``x``.

    ``(0, 0)`` is an equilibrium (a saddle point of ``f``). The simultaneous iterates never get closer to it; the
    alternating ones circle around it when ``eta`` is small. The function does not check anything about the
    convergence: it returns the iterates.

    Beware the roles: here the first player (``x``, along the rows of ``A``) minimizes, as in MML (7.23); for a game
    ``G`` of ``pure_strategy_values``, whose row player maximizes, take ``A = -G`` with ``x`` the row player, or
    ``A = G.T`` with ``x`` the column player.

    Parameters
    ----------
    A : 2-D array-like
        The ``(n, m)`` matrix of the game, ``n, m ≥ 1``, of finite numbers.
    x0 : 1-D array-like
        The ``n`` coordinates of the first player's start.
    y0 : 1-D array-like
        The ``m`` coordinates of the second player's start.
    eta : float
        The step, a finite number ``> 0`` (a ``bool`` is refused).
    n_steps : int, default 10
        The number ``N ≥ 0`` of steps (a NumPy integer is accepted; a bool or a float is refused).
    alternating : bool, default False
        ``True`` for the alternating iterates, ``False`` for the simultaneous ones.

    Returns
    -------
    tuple
        ``(xs, ys)``: two ``numpy.ndarray`` of floats, of shapes ``(N + 1, n)`` and ``(N + 1, m)``, whose rows ``k``
        are ``x_k`` and ``y_k`` (row 0 is the start).

    Raises
    ------
    ValueError
        If ``A`` is not 2-D, is empty or has an entry that is not a finite number, if ``x0`` or ``y0`` does not have
        the right number of coordinates, if ``eta`` is not a finite number ``> 0``, or if ``n_steps`` is not an integer
        ``≥ 0``.

    Examples
    --------
    >>> xs, ys = descent_ascent_iterates([[2.0]], [1.0], [0.0], eta=0.25, n_steps=2)
    >>> xs.ravel(), ys.ravel()
    (array([1.  , 1.  , 0.75]), array([0. , 0.5, 1. ]))
    >>> xs, ys = descent_ascent_iterates([[2.0]], [1.0], [0.0], eta=0.25, n_steps=2, alternating=True)
    >>> xs.ravel(), ys.ravel()
    (array([1.  , 1.  , 0.75]), array([0.   , 0.5  , 0.875]))
    """
    # TODO: check the inputs (float copies of x0 and y0); at each step, the new x from the old y, then the new
    #  y from the old x (simultaneous) or from the new x (alternating); store each pair in a row.
    raise NotImplementedError("descent_ascent_iterates() is not implemented yet")


def w2_gaussians_1d(mu1, sigma1, mu2, sigma2):
    """Return the 2-Wasserstein distance ``W₂`` between the normal laws ``N(mu1, sigma1²)`` and ``N(mu2, sigma2²)``.

    The arguments are **standard deviations**, not variances, and the result is the distance itself, not its
    square: ``W₂ = sqrt((mu1 - mu2)² + (sigma1 - sigma2)²)``. On the line, the optimal coupling pairs the
    quantiles ``mu + sigma Φ⁻¹(u)`` of the two laws (M27 §8). A standard deviation 0 is allowed: the law is then
    the point mass at ``mu``. The square ``W₂²`` is the one-dimensional case of the Fréchet distance between
    Gaussians (M27 §9).

    Parameters
    ----------
    mu1, sigma1 : float
        Mean and standard deviation (``≥ 0``) of the first law (the names are those of ``distributions.normal_pdf``;
        a Fréchet-distance function usually takes covariance matrices under the same names).
    mu2, sigma2 : float
        Mean and standard deviation (``≥ 0``) of the second law.

    Returns
    -------
    float
        ``W₂ ≥ 0``, a Python ``float``.

    Raises
    ------
    ValueError
        If an argument is not a finite real number (a ``bool`` is refused), or if a standard deviation is negative.

    Examples
    --------
    >>> w2_gaussians_1d(10.0, 1.0, 2.0, 16.0)
    17.0
    >>> w2_gaussians_1d(-1.0, 0.5, -1.0, 3.5)                       # same mean: only the spreads differ
    3.0
    """
    # TODO: check the four numbers (finite, not bool) and the signs of the standard deviations, then
    #  math.hypot (or math.sqrt of the sum of the two squares).
    raise NotImplementedError("w2_gaussians_1d() is not implemented yet")
