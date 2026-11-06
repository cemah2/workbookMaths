"""First probabilities: counting, exact probabilities, expectation, variance, simulation (chapter R8).

Reference implementation (same signatures as templates/mymath_stubs/proba_basics.py). Plain Python, ``fractions``
and, for ``simulate_frequency`` only, the NumPy generator; no ``math.factorial``, ``math.comb`` or ``statistics``.
"""

from __future__ import annotations

from fractions import Fraction
from numbers import Rational


def factorial(n):
    """Return ``n! = 1 × 2 × ... × n`` (with ``0! = 1``)."""
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def binomial(n, k):
    """Return the number of ways to choose ``k`` objects among ``n`` (« k parmi n »)."""
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)                       # symmetry: fewer factors
    result = 1
    for i in range(1, k + 1):               # n(n-1)...(n-k+1) / k!, exact at each step
        result = result * (n - k + i) // i
    return result


def enumerate_probability(outcomes, event):
    """Return the exact probability of an event when every outcome is equally likely."""
    total = 0
    favourable = 0
    for outcome in outcomes:                # works for a list as well as for a generator (read once)
        total += 1
        if event(outcome):
            favourable += 1
    if total == 0:
        raise ValueError("there is no outcome")
    return Fraction(favourable, total)


def _check_law(values, probabilities):
    values, probabilities = list(values), list(probabilities)
    if len(values) != len(probabilities):
        raise ValueError(f"{len(values)} values but {len(probabilities)} probabilities")
    if any(p < 0 for p in probabilities):
        raise ValueError("a probability is negative")
    if abs(sum(probabilities) - 1) > 1e-9:
        raise ValueError(f"the probabilities sum to {sum(probabilities)}, not 1")
    return values, probabilities


def _exact(numbers) -> bool:
    return all(isinstance(x, Rational) and not isinstance(x, bool) for x in numbers)


def expectation(values, probabilities):
    """Return the expectation ``E[X] = Σ x_i p_i`` of a finite random variable."""
    values, probabilities = _check_law(values, probabilities)
    total = sum(x * p for x, p in zip(values, probabilities))
    if _exact(values) and _exact(probabilities):
        return Fraction(total)
    return float(total)


def variance(values, probabilities):
    """Return the variance ``V(X) = E[(X - E[X])**2]`` of a finite random variable."""
    values, probabilities = _check_law(values, probabilities)
    mean = expectation(values, probabilities)
    total = sum((x - mean) ** 2 * p for x, p in zip(values, probabilities))
    if _exact(values) and _exact(probabilities):
        return Fraction(total)
    return float(total)


def simulate_frequency(experiment, n_trials, seed=0):
    """Repeat a random experiment and return the frequency of success."""
    import numpy as np

    if n_trials <= 0:
        raise ValueError(f"n_trials must be positive, got {n_trials}")
    rng = np.random.default_rng(seed)
    successes = 0
    for _ in range(n_trials):
        if experiment(rng):
            successes += 1
    return successes / n_trials
