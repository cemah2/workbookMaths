"""Tests of mymath.proba_basics (chapter R8): counting, exact probabilities, expectation, variance, simulation.

Oracles: ``math.factorial`` and ``math.comb`` (exact integers), probabilities counted with ``fractions.Fraction``,
``numpy.dot`` for the expectation and the variance of float laws, and the NumPy generator ``default_rng(seed)``
replayed for the simulation. They describe the expected behaviour without showing the solution.

    pytest tests/test_r8_proba_basics.py              # your code
    pytest tests/test_r8_proba_basics.py --impl=ref   # the reference
"""

import ast
import inspect
import itertools
import math
import random
from fractions import Fraction

import numpy as np
import pytest


@pytest.fixture
def proba(mymath_module):
    return mymath_module("proba_basics")


def _result(call, expected):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    try:
        return call()
    except NotImplementedError:
        raise                 # a function not written yet: ⏳
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        pytest.fail(f"expected {expected}, but it raised {type(exc).__name__}: {exc}")


def _expect_value_error(call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ValueError."""
    try:
        call()
    except ValueError:
        return
    except NotImplementedError:
        raise
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned a value")


def test_proba_basics_does_not_use_ready_made_tools(proba):
    """The module docstring forbids math.factorial, math.comb and statistics: the tests compare with them."""
    try:
        tree = ast.parse(inspect.getsource(proba))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    used = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id == "math" \
                and node.attr in {"factorial", "comb", "perm"}:
            used.add(f"math.{node.attr}")
        elif isinstance(node, ast.ImportFrom) and node.module == "math":
            used.update(f"math.{a.name}" for a in node.names if a.name in {"factorial", "comb", "perm", "*"})
        elif isinstance(node, ast.Import):
            used.update(a.name for a in node.names if a.name.split(".")[0] in {"statistics", "scipy"})
        elif isinstance(node, ast.ImportFrom) and node.module and node.module.split(".")[0] in {"statistics", "scipy"}:
            used.add(node.module)
    assert not used, (
        f"expected proba_basics.py to compute by itself, without {', '.join(sorted(used))}: write the loops yourself "
        f"(the tests use these tools as oracles)")


# ---------------------------------------------------------------- factorial
def test_factorial_docstring_example(proba):
    got = _result(lambda: proba.factorial(5), "120 (the docstring example)")
    assert got == 120, f"expected factorial(5) == 120 (1 × 2 × 3 × 4 × 5), got {got!r}"


def test_factorial_of_zero_is_one(proba):
    got = _result(lambda: proba.factorial(0), "1 (0! is the empty product)")
    assert got == 1, f"expected factorial(0) == 1 (the empty product, by convention), got {got!r}"


def test_factorial_matches_math_factorial(proba):
    for n in range(0, 26):
        got = _result(lambda: proba.factorial(n), f"{math.factorial(n)} (= {n}!)")
        assert got == math.factorial(n), f"expected factorial({n}) == {math.factorial(n)} (math.factorial), got {got!r}"


def test_factorial_is_an_exact_int(proba):
    got = _result(lambda: proba.factorial(30), "an exact int")
    assert isinstance(got, int) and not isinstance(got, bool), (
        f"expected an int (exact, never a float), got {type(got).__name__} {got!r}")
    big = _result(lambda: proba.factorial(100), "100!, exact")
    assert big == math.factorial(100), "expected factorial(100) == math.factorial(100) exactly (a float would round it)"


@pytest.mark.parametrize("n", [-1, -5], ids=["n=-1", "n=-5"])
def test_factorial_refuses_a_negative_number(proba, n):
    _expect_value_error(lambda: proba.factorial(n), f"factorial({n})", "n! is defined for n >= 0 only")


# ---------------------------------------------------------------- binomial
def test_binomial_docstring_example(proba):
    got = _result(lambda: proba.binomial(5, 2), "10 (the docstring example)")
    assert got == 10, f"expected binomial(5, 2) == 10 (the pairs among 5 objects), got {got!r}"


def test_binomial_matches_math_comb(proba):
    for n in range(0, 21):
        for k in range(0, n + 1):
            got = _result(lambda: proba.binomial(n, k), f"{math.comb(n, k)} (= C({n}, {k}))")
            assert got == math.comb(n, k), f"expected binomial({n}, {k}) == {math.comb(n, k)} (math.comb), got {got!r}"


@pytest.mark.parametrize("n, k", [(6, -1), (6, 7), (0, 1), (3, -4)], ids=["k=-1", "k>n", "n=0,k=1", "k=-4"])
def test_binomial_is_zero_outside_0_to_n(proba, n, k):
    got = _result(lambda: proba.binomial(n, k), "0 (no way to choose)")
    assert got == 0, f"expected binomial({n}, {k}) == 0 (k < 0 or k > n: there is no way to choose), got {got!r}"


def test_binomial_is_symmetric(proba):
    for n, k in [(11, 4), (17, 6), (25, 9)]:
        left = _result(lambda: proba.binomial(n, k), f"C({n}, {k})")
        right = _result(lambda: proba.binomial(n, n - k), f"C({n}, {n - k})")
        assert left == right == math.comb(n, k), (
            f"expected binomial({n}, {k}) == binomial({n}, {n - k}) == {math.comb(n, k)} (symmetry), got {left!r} "
            f"and {right!r}")


def test_binomial_is_exact_for_large_numbers(proba):
    got = _result(lambda: proba.binomial(100, 50), "C(100, 50), exact")
    assert isinstance(got, int) and not isinstance(got, bool), (
        f"expected an int (exact: integer division //, never /), got {type(got).__name__} {got!r}")
    assert got == math.comb(100, 50), (
        f"expected binomial(100, 50) == {math.comb(100, 50)} exactly, got {got!r} (a float division loses digits)")


@pytest.mark.parametrize("n", [-1, -3], ids=["n=-1", "n=-3"])
def test_binomial_refuses_a_negative_n(proba, n):
    _expect_value_error(lambda: proba.binomial(n, 0), f"binomial({n}, 0)", "n must be non-negative")


# ---------------------------------------------------------------- enumerate_probability
def test_enumerate_probability_docstring_example(proba):
    got = _result(lambda: proba.enumerate_probability(range(1, 7), lambda x: x % 2 == 0), "Fraction(1, 2)")
    assert got == Fraction(1, 2), f"expected Fraction(1, 2) (3 even numbers out of 6), got {got!r}"


def test_enumerate_probability_returns_a_fraction(proba):
    got = _result(lambda: proba.enumerate_probability(range(10), lambda x: x < 3), "Fraction(3, 10)")
    assert isinstance(got, Fraction), f"expected a fractions.Fraction (exact), got {type(got).__name__} {got!r}"
    assert got == Fraction(3, 10), f"expected Fraction(3, 10), got {got!r}"


TWO_DICE = list(itertools.product(range(1, 7), repeat=2))
EVENTS = [
    (TWO_DICE, lambda o: (o[0] + o[1]) in {2, 3, 5, 7, 11}, "two dice, prime sum"),
    (TWO_DICE, lambda o: abs(o[0] - o[1]) >= 4, "two dice, gap >= 4"),
    (["".join(w) for w in itertools.product("PF", repeat=5)], lambda w: w.count("P") == 2, "five coins, two piles"),
    (list(range(1, 101)), lambda n: n % 7 == 0 or n % 11 == 0, "1 to 100, multiple of 7 or 11"),
]


@pytest.mark.parametrize("outcomes, event, name", EVENTS, ids=[e[2] for e in EVENTS])
def test_enumerate_probability_counts_the_favourable_outcomes(proba, outcomes, event, name):
    exact = Fraction(sum(1 for o in outcomes if event(o)), len(outcomes))
    got = _result(lambda: proba.enumerate_probability(outcomes, event), f"{exact} ({name})")
    assert got == exact, f"expected {exact} ({name}: favourable outcomes / possible outcomes), got {got!r}"


def test_enumerate_probability_reads_a_generator_once(proba):
    outcomes = (n for n in range(12))
    got = _result(lambda: proba.enumerate_probability(outcomes, lambda n: n % 4 == 0), "Fraction(1, 4)")
    assert got == Fraction(1, 4), (
        f"expected Fraction(1, 4) for a generator of the 12 outcomes 0 to 11 (multiples of 4: 0, 4, 8), got {got!r}: "
        f"a generator has no len() and can be read only once, so count while you read it")


def test_enumerate_probability_impossible_and_certain_events(proba):
    never = _result(lambda: proba.enumerate_probability("abcde", lambda c: c == "z"), "Fraction(0, 1)")
    always = _result(lambda: proba.enumerate_probability("abcde", lambda c: c.isalpha()), "Fraction(1, 1)")
    assert never == 0 and always == 1, (
        f"expected 0 for an impossible event and 1 for a certain one, got {never!r} and {always!r}")


def test_enumerate_probability_refuses_no_outcome(proba):
    _expect_value_error(lambda: proba.enumerate_probability([], lambda o: True), "enumerate_probability([], ...)",
                        "there is no outcome: the probability would divide by 0")


# ---------------------------------------------------------------- expectation
def test_expectation_docstring_example(proba):
    got = _result(lambda: proba.expectation([0, 10], [0.5, 0.5]), "5.0 (the docstring example)")
    assert got == pytest.approx(5.0), f"expected expectation([0, 10], [0.5, 0.5]) == 5.0, got {got!r}"


def test_expectation_is_exact_with_fractions(proba):
    values, probs = [0, 1, 2], [Fraction(16, 25), Fraction(8, 25), Fraction(1, 25)]
    exact = sum(Fraction(v) * p for v, p in zip(values, probs))
    got = _result(lambda: proba.expectation(values, probs), f"Fraction({exact.numerator}, {exact.denominator})")
    assert isinstance(got, Fraction) and got == exact, (
        f"expected the Fraction {exact} (ints and Fractions only: an exact result), got {type(got).__name__} {got!r}")


FLOAT_LAWS = [([1.5, -2.0, 4.0], [0.2, 0.5, 0.3]), ([10, 20, 30, 40], [0.25, 0.25, 0.25, 0.25]),
              ([-3.0, 0.5], [0.9, 0.1])]


@pytest.mark.parametrize("values, probs", FLOAT_LAWS, ids=["three values", "uniform on 4 values", "two values"])
def test_expectation_matches_a_weighted_sum(proba, values, probs):
    exact = float(np.dot(values, probs))
    got = _result(lambda: proba.expectation(values, probs), f"≈ {exact}")
    assert got == pytest.approx(exact, rel=1e-12, abs=1e-12), (
        f"expected expectation({values}, {probs}) ≈ {exact} (Σ x_i p_i, numpy.dot), got {got!r}")


def test_expectation_accepts_probabilities_that_sum_to_1_up_to_rounding(proba):
    probs = [0.1] * 10                       # sum: 0.9999999999999999
    got = _result(lambda: proba.expectation(list(range(10)), probs), "4.5 (the sum of probs is 1 up to 1e-9)")
    assert got == pytest.approx(4.5), f"expected 4.5 (ten values 0 to 9, each 0.1), got {got!r}"


BAD_LAWS = [([1, 2, 3], [0.5, 0.5], "3 values but 2 probabilities"),
            ([1, 2], [1.2, -0.2], "a negative probability"),
            ([1, 2, 3], [0.3, 0.3, 0.3], "probabilities summing to 0.9")]


@pytest.mark.parametrize("values, probs, why", BAD_LAWS, ids=["lengths differ", "negative", "sum 0.9"])
def test_expectation_refuses_a_bad_law(proba, values, probs, why):
    _expect_value_error(lambda: proba.expectation(values, probs), f"expectation({values}, {probs})", why)


# ---------------------------------------------------------------- variance
def test_variance_docstring_example(proba):
    got = _result(lambda: proba.variance([0, 10], [0.5, 0.5]), "25.0 (the docstring example)")
    assert got == pytest.approx(25.0), f"expected variance([0, 10], [0.5, 0.5]) == 25.0, got {got!r}"


def test_variance_is_exact_with_fractions(proba):
    values, probs = [1, 2, 6], [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    mean = sum(Fraction(v) * p for v, p in zip(values, probs))
    exact = sum((v - mean) ** 2 * p for v, p in zip(values, probs))
    got = _result(lambda: proba.variance(values, probs), f"Fraction({exact.numerator}, {exact.denominator})")
    assert isinstance(got, Fraction) and got == exact, (
        f"expected the Fraction {exact} (ints and Fractions only: an exact result), got {type(got).__name__} {got!r}")


@pytest.mark.parametrize("values, probs", FLOAT_LAWS, ids=["three values", "uniform on 4 values", "two values"])
def test_variance_matches_numpy(proba, values, probs):
    v, p = np.asarray(values, dtype=float), np.asarray(probs, dtype=float)
    exact = float(np.dot((v - np.dot(v, p)) ** 2, p))
    got = _result(lambda: proba.variance(values, probs), f"≈ {exact}")
    assert got == pytest.approx(exact, rel=1e-9, abs=1e-12), (
        f"expected variance({values}, {probs}) ≈ {exact} (E[(X - E[X])²]), got {got!r}")


def test_variance_of_a_constant_is_zero(proba):
    got = _result(lambda: proba.variance([7, 7, 7], [0.2, 0.3, 0.5]), "0 (a constant does not vary)")
    assert got == pytest.approx(0.0, abs=1e-12), f"expected 0 (X is always 7), got {got!r}"


def test_variance_is_never_negative(proba):
    rng = random.Random(81)
    for _ in range(30):
        values = [rng.uniform(-50, 50) for _ in range(5)]
        weights = [rng.random() for _ in range(5)]
        probs = [w / sum(weights) for w in weights]
        got = _result(lambda: proba.variance(values, probs), "a variance >= 0")
        assert got >= -1e-9, f"expected a variance >= 0 (a mean of squares), got {got!r} for {values}, {probs}"


@pytest.mark.parametrize("values, probs, why", BAD_LAWS, ids=["lengths differ", "negative", "sum 0.9"])
def test_variance_refuses_a_bad_law(proba, values, probs, why):
    _expect_value_error(lambda: proba.variance(values, probs), f"variance({values}, {probs})", why)


# ---------------------------------------------------------------- simulate_frequency
def _replay(experiment, n_trials, seed):
    """The oracle: one generator default_rng(seed), the experiment called n_trials times with it."""
    rng = np.random.default_rng(seed)
    return sum(bool(experiment(rng)) for _ in range(n_trials)) / n_trials


def test_simulate_frequency_docstring_example(proba):
    got = _result(lambda: proba.simulate_frequency(lambda rng: rng.integers(1, 7) == 6, 60_000), "≈ 1/6")
    assert abs(got - 1 / 6) < 0.01, f"expected a frequency within 0.01 of 1/6 ≈ 0.1667 (60 000 trials), got {got!r}"


EXPERIMENTS = [(lambda rng: rng.random() < 0.3, 500, 0, "random() < 0.3, seed 0"),
               (lambda rng: rng.integers(1, 5) + rng.integers(1, 5) >= 6, 800, 4, "two 4-sided dice >= 6, seed 4"),
               (lambda rng: rng.integers(0, 2, size=3).sum() == 2, 300, 11, "three coins, two piles, seed 11")]


@pytest.mark.parametrize("experiment, n_trials, seed, name", EXPERIMENTS, ids=[e[3] for e in EXPERIMENTS])
def test_simulate_frequency_replays_the_generator(proba, experiment, n_trials, seed, name):
    exact = _replay(experiment, n_trials, seed)
    got = _result(lambda: proba.simulate_frequency(experiment, n_trials, seed), f"{exact} ({name})")
    assert got == pytest.approx(exact, abs=1e-12), (
        f"expected {exact} ({name}: ONE generator np.random.default_rng(seed), created before the loop, then "
        f"experiment(rng) called n_trials times), got {got!r}")


def test_simulate_frequency_same_seed_same_result(proba):
    experiment = lambda rng: rng.random() < 0.5  # noqa: E731
    first = _result(lambda: proba.simulate_frequency(experiment, 1_000, seed=21), "a frequency")
    second = _result(lambda: proba.simulate_frequency(experiment, 1_000, seed=21), "the same frequency")
    other = _result(lambda: proba.simulate_frequency(experiment, 1_000, seed=22), "another frequency")
    assert first == second, f"expected the same frequency twice with seed 21 (reproducible), got {first!r} and {second!r}"
    assert first != other, f"expected seed 22 to give another frequency than seed 21, got {first!r} twice"


def test_simulate_frequency_calls_the_experiment_n_trials_times_with_a_generator(proba):
    seen = []

    def experiment(rng):
        seen.append(type(rng).__name__)
        return True

    got = _result(lambda: proba.simulate_frequency(experiment, 37, seed=3), "1.0")
    assert len(seen) == 37, f"expected experiment to be called exactly 37 times (n_trials = 37), got {len(seen)} calls"
    assert set(seen) == {"Generator"}, (
        f"expected experiment to receive the NumPy generator np.random.default_rng(seed), got {sorted(set(seen))}")
    assert isinstance(got, float) and got == 1.0, f"expected the float 1.0 (37 successes / 37), got {got!r}"


@pytest.mark.parametrize("n_trials", [0, -4], ids=["n=0", "n=-4"])
def test_simulate_frequency_refuses_no_trial(proba, n_trials):
    _expect_value_error(lambda: proba.simulate_frequency(lambda rng: True, n_trials),
                        f"simulate_frequency(..., {n_trials})", "n_trials must be positive")
