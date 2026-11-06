"""First probabilities: counting, exact probabilities, expectation, variance, simulation (chapter R8).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_r8_proba_basics.py``.
Do not use ``math.factorial``, ``math.comb`` or ``statistics``: the tests compare your results with them.
"""


def factorial(n):
    """Return ``n! = 1 × 2 × ... × n`` (with ``0! = 1``).

    Parameters
    ----------
    n : int
        Non-negative.

    Returns
    -------
    int

    Raises
    ------
    ValueError
        If ``n`` is negative.

    Examples
    --------
    >>> factorial(5)
    120
    """
    # TODO: a loop (or a product); 0! is the empty product.
    raise NotImplementedError("factorial() is not implemented yet")


def binomial(n, k):
    """Return the number of ways to choose ``k`` objects among ``n`` (« k parmi n »).

    Parameters
    ----------
    n : int
        Non-negative.
    k : int
        Any integer: the result is 0 when ``k < 0`` or ``k > n``.

    Returns
    -------
    int
        An exact integer, even for large ``n`` (no float division).

    Examples
    --------
    >>> binomial(5, 2)
    10
    """
    # TODO: the formula with factorials, using integer division //.
    raise NotImplementedError("binomial() is not implemented yet")


def enumerate_probability(outcomes, event):
    """Return the exact probability of an event when every outcome is equally likely.

    Parameters
    ----------
    outcomes : iterable
        Every possible outcome, each one equally likely (e.g. the 36 pairs of two dice).
    event : callable
        A predicate: ``event(outcome)`` is True when the outcome belongs to the event.

    Returns
    -------
    fractions.Fraction
        Favourable outcomes / possible outcomes, as an exact fraction.

    Raises
    ------
    ValueError
        If there is no outcome.

    Examples
    --------
    >>> enumerate_probability(range(1, 7), lambda x: x % 2 == 0)
    Fraction(1, 2)
    """
    # TODO: count all outcomes and the favourable ones; return a Fraction (from fractions import Fraction).
    raise NotImplementedError("enumerate_probability() is not implemented yet")


def expectation(values, probabilities):
    """Return the expectation ``E[X] = Σ x_i p_i`` of a finite random variable.

    Parameters
    ----------
    values : sequence of float
        The values ``x_i`` taken by ``X``.
    probabilities : sequence of float
        ``P(X = x_i)``: same length, non-negative, summing to 1 (up to 1e-9).

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If the lengths differ, a probability is negative, or they do not sum to 1.

    Examples
    --------
    >>> expectation([0, 10], [0.5, 0.5])
    5.0
    """
    # TODO: check the law first, then the weighted sum.
    raise NotImplementedError("expectation() is not implemented yet")


def variance(values, probabilities):
    """Return the variance ``V(X) = E[(X - E[X])**2]`` of a finite random variable.

    Parameters
    ----------
    values : sequence of float
    probabilities : sequence of float
        Same rules as :func:`expectation`.

    Returns
    -------
    float
        Non-negative.

    Raises
    ------
    ValueError
        Same cases as :func:`expectation`.

    Examples
    --------
    >>> variance([0, 10], [0.5, 0.5])
    25.0
    """
    # TODO: reuse expectation (relative import is not needed: it is in this module).
    raise NotImplementedError("variance() is not implemented yet")


def simulate_frequency(experiment, n_trials, seed=0):
    """Repeat a random experiment and return the frequency of success.

    Parameters
    ----------
    experiment : callable
        ``experiment(rng)`` performs one trial with the NumPy generator ``rng`` and returns True (success) or
        False, e.g. ``lambda rng: rng.integers(1, 7) == 6``.
    n_trials : int
        Number of trials, positive.
    seed : int, default 0
        Seed of the generator ``numpy.random.default_rng(seed)``: the same seed gives the same frequency.

    Returns
    -------
    float
        Number of successes / ``n_trials``.

    Raises
    ------
    ValueError
        If ``n_trials`` is not positive.

    Examples
    --------
    >>> f = simulate_frequency(lambda rng: rng.integers(1, 7) == 6, 60_000)
    >>> abs(f - 1 / 6) < 0.01
    True
    """
    # TODO: create one generator, call experiment(rng) n_trials times, count the successes.
    raise NotImplementedError("simulate_frequency() is not implemented yet")
