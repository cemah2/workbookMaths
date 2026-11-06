"""Tests of mymath.sequences (chapter R5): arithmetic terms, geometric sums, recurrences, moving averages.

Oracles: exact arithmetic with ``fractions`` and SymPy (``summation``), the closed form of an affine recurrence in
fractions, NumPy (``np.convolve``) for the moving average and SciPy (``scipy.signal.lfilter``) for the exponential
moving average. They describe the expected behaviour without showing the solution.

    pytest tests/test_r5_sequences.py              # your code
    pytest tests/test_r5_sequences.py --impl=ref   # the reference
"""

import random
from fractions import Fraction

import numpy as np
import pytest
import sympy as sp
from scipy.signal import lfilter

K = sp.Symbol("k", integer=True)


@pytest.fixture
def sequences(mymath_module):
    return mymath_module("sequences")


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


def _floats(values):
    """A list of floats rounded for a message: [1.5, 2.333333]."""
    return [round(float(v), 6) for v in values]


# ---------------------------------------------------------------- arithmetic_term
ARITHMETIC = [(5, 3, 10, 35, "the docstring example"), (-4, 7, 12, 80, "a negative first term"),
              (9, -2, 6, -3, "a negative common difference"), (2.5, -0.5, 9, -2.0, "floats"),
              (11, 4, 0, 11, "n = 0 gives the first term"), (0, 0, 50, 0, "r = 0: a constant sequence")]


@pytest.mark.parametrize("u0, r, n, want, why", ARITHMETIC, ids=[a[4] for a in ARITHMETIC])
def test_arithmetic_term_cases(sequences, u0, r, n, want, why):
    got = _result(lambda: sequences.arithmetic_term(u0, r, n), f"arithmetic_term({u0}, {r}, {n}) == {want} ({why})")
    assert got == pytest.approx(want), (f"expected arithmetic_term({u0}, {r}, {n}) == {want} ({why}: u(n) = u0 + n r, "
                                        f"u(0) being u0), got {got!r}")


def test_arithmetic_term_matches_fractions(sequences):
    rng = random.Random(51)
    for _ in range(40):
        u0, r, n = Fraction(rng.randint(-40, 40), 4), Fraction(rng.randint(-30, 30), 8), rng.randint(0, 60)
        want = u0                                           # the oracle: add r, n times, exactly
        for _step in range(n):
            want += r
        got = _result(lambda: sequences.arithmetic_term(float(u0), float(r), n), f"{float(want)}")
        assert got == pytest.approx(float(want), abs=1e-9), (
            f"expected arithmetic_term({float(u0)}, {float(r)}, {n}) == {float(want)} (r added n times to u0), "
            f"got {got!r}")


def test_arithmetic_term_keeps_integers(sequences):
    got = _result(lambda: sequences.arithmetic_term(3, 4, 5), "the int 23")
    assert got == 23, f"expected arithmetic_term(3, 4, 5) == 23 (3 + 5 × 4), got {got!r}"
    assert isinstance(got, int), f"expected the int 23, not {got!r}: no division, no float, when u0 and r are ints"


def test_arithmetic_term_steps_by_r(sequences):
    got = _result(lambda: [sequences.arithmetic_term(1, 6, n) for n in range(6)], "[1, 7, 13, 19, 25, 31]")
    differences = [b - a for a, b in zip(got, got[1:])]
    assert got == [1, 7, 13, 19, 25, 31], (
        f"expected the terms of index 0 to 5 to be [1, 7, 13, 19, 25, 31] (a difference of 6 between two terms), "
        f"got {got!r} (differences {differences})")


# ---------------------------------------------------------------- geometric_sum
def _geometric_oracle(u0, q, n):
    """The exact sum of u0 q^k for k = 0..n−1 (SymPy, in rationals)."""
    if n == 0:
        return 0.0
    return float(sp.summation(sp.Rational(u0) * sp.Rational(q) ** K, (K, 0, n - 1)))


GEOMETRIC = [(1, 2, 10, "the docstring example"), (3, 1.5, 6, "a decimal ratio"), (2, -0.5, 7, "a negative ratio"),
             (6, 0.25, 40, "|q| < 1, many terms: close to u0 / (1 - q)"), (5, 1, 7, "q = 1: n times u0"),
             (8, 3, 0, "n = 0: the empty sum is 0"), (7, -1, 5, "q = -1: the terms cancel in pairs"),
             (-4, 2, 1, "n = 1: the first term alone"), (2.5, 0, 4, "q = 0: only the first term is not 0")]


@pytest.mark.parametrize("u0, q, n, why", GEOMETRIC, ids=[g[3] for g in GEOMETRIC])
def test_geometric_sum_matches_sympy(sequences, u0, q, n, why):
    want = _geometric_oracle(u0, q, n)
    got = _result(lambda: sequences.geometric_sum(u0, q, n), f"geometric_sum({u0}, {q}, {n}) == {want} ({why})")
    assert got == pytest.approx(want, rel=1e-9, abs=1e-12), (
        f"expected geometric_sum({u0}, {q}, {n}) == {want} ({why}; n is the NUMBER of terms, the last one is "
        f"u0*q**(n - 1)), got {got!r}")


def test_geometric_sum_matches_sympy_on_random_cases(sequences):
    rng = random.Random(52)
    for _ in range(40):
        u0, q, n = Fraction(rng.randint(-20, 20), 2), Fraction(rng.choice([-3, -2, -1, 1, 2, 3, 5]), 4), rng.randint(0, 25)
        want = _geometric_oracle(u0, q, n)
        got = _result(lambda: sequences.geometric_sum(float(u0), float(q), n), f"{want}")
        assert got == pytest.approx(want, rel=1e-9, abs=1e-9), (
            f"expected geometric_sum({float(u0)}, {float(q)}, {n}) == {want} (the sum of the first {n} terms), "
            f"got {got!r}")


def test_geometric_sum_returns_a_float(sequences):
    got = _result(lambda: sequences.geometric_sum(1, 2, 10), "the float 1023.0")
    assert isinstance(got, float) and got == 1023.0, (
        f"expected the float 1023.0 (the docstring example: a float, even when u0 and q are ints), got {got!r}")


def test_geometric_sum_handles_q_equal_one(sequences):
    got = _result(lambda: sequences.geometric_sum(4, 1, 6), "24.0 (six terms equal to 4)")
    assert got == pytest.approx(24.0), (
        f"expected geometric_sum(4, 1, 6) == 24.0 (q = 1: every term is u0, and the formula would divide by 0), "
        f"got {got!r}")


# ---------------------------------------------------------------- iterate
def test_iterate_docstring_example(sequences):
    got = _result(lambda: sequences.iterate(lambda u: 2 * u + 1, 0, 4), "[0, 1, 3, 7, 15]")
    assert got == [0, 1, 3, 7, 15], f"expected [0, 1, 3, 7, 15] (the docstring example), got {got!r}"


@pytest.mark.parametrize("a, b, u0, n", [(Fraction(3, 4), 2, Fraction(0), 12), (Fraction(-1, 2), 5, Fraction(7), 9),
                                         (Fraction(3), -1, Fraction(1, 2), 6), (Fraction(1), 4, Fraction(-3), 10)],
                         ids=["a=3/4", "a=-1/2", "a=3", "a=1"])
def test_iterate_matches_the_closed_form(sequences, a, b, u0, n):
    if a == 1:
        want = [u0 + k * b for k in range(n + 1)]                     # an arithmetic sequence
    else:
        fixed = Fraction(b) / (1 - a)
        want = [fixed + (u0 - fixed) * a**k for k in range(n + 1)]   # ℓ + (u0 − ℓ) a^k, exactly
    got = _result(lambda: sequences.iterate(lambda u: a * u + b, u0, n), f"the {n + 1} terms {want}")
    assert got == want, (f"expected iterate(lambda u: {a} * u + {b}, {u0}, {n}) == {[str(w) for w in want]} "
                         f"(u(0) = u0, then u(k + 1) = f(u(k)), up to index {n} included), got "
                         f"{[str(g) for g in got] if isinstance(got, list) else got!r}")


@pytest.mark.parametrize("n", [0, 1, 5, 30])
def test_iterate_has_n_plus_one_terms(sequences, n):
    got = _result(lambda: sequences.iterate(lambda u: u + 1, 0, n), f"a list of {n + 1} terms")
    assert isinstance(got, list) and len(got) == n + 1, (
        f"expected a list of n + 1 = {n + 1} terms (indices 0 to {n}), got "
        f"{len(got) if isinstance(got, list) else got!r}")
    assert got[0] == 0, f"expected the first term to be u0 = 0, got {got[0]!r}"


def test_iterate_calls_f_exactly_n_times(sequences):
    calls = []

    def f(u):
        calls.append(u)
        return u * u - 1

    got = _result(lambda: sequences.iterate(f, 2, 3), "[2, 3, 8, 63]")
    assert got == [2, 3, 8, 63], f"expected [2, 3, 8, 63] (u(k + 1) = u(k)² − 1 from 2), got {got!r}"
    assert len(calls) == 3, f"expected f to be called 3 times (n = 3), but it was called {len(calls)} times"


def test_iterate_works_on_any_values(sequences):
    got = _result(lambda: sequences.iterate(lambda word: word + "a", "", 3), "['', 'a', 'aa', 'aaa']")
    assert got == ["", "a", "aa", "aaa"], (
        f"expected ['', 'a', 'aa', 'aaa'] (iterate only applies f: it works on any value), got {got!r}")


# ---------------------------------------------------------------- moving_average
MOVING = [([1, 2, 3, 4, 5], 2, "the docstring example"), ([4, 8, 6, 10, 2, 12], 3, "a window of 3"),
          ([5.5, -2.0, 3.25, 0.0], 1, "window 1: the values themselves"), ([3, 9, 6], 3, "window = len: the mean"),
          (list(range(20)), 7, "twenty values, window 7")]


@pytest.mark.parametrize("values, window, why", MOVING, ids=[m[2] for m in MOVING])
def test_moving_average_matches_numpy(sequences, values, window, why):
    want = np.convolve(np.asarray(values, dtype=float), np.ones(window) / window, mode="valid")
    got = _result(lambda: sequences.moving_average(values, window), f"{_floats(want)} ({why})")
    assert isinstance(got, list) and len(got) == len(want) and np.allclose(got, want), (
        f"expected moving_average({values}, {window}) == {_floats(want)} ({why}; len(values) - window + 1 = "
        f"{len(want)} means, like np.convolve(values, np.ones(window) / window, mode='valid')), got {got!r}")


def test_moving_average_matches_numpy_on_random_cases(sequences):
    rng = np.random.default_rng(53)
    for _ in range(30):
        values = list(np.round(rng.normal(10, 5, size=int(rng.integers(1, 30))), 2))
        window = int(rng.integers(1, len(values) + 1))
        want = np.convolve(values, np.ones(window) / window, mode="valid")
        got = _result(lambda: sequences.moving_average(values, window), f"{len(want)} means")
        assert len(got) == len(want) and np.allclose(got, want), (
            f"expected the {len(want)} moving averages {_floats(want)} of {values} over {window} values, got {got!r}")


def test_moving_average_accepts_a_tuple(sequences):
    got = _result(lambda: sequences.moving_average((2, 4, 9), 2), "[3.0, 6.5]")
    assert got == pytest.approx([3.0, 6.5]), f"expected [3.0, 6.5] for the tuple (2, 4, 9), got {got!r}"


@pytest.mark.parametrize("window", [0, 4, -1], ids=["zero", "longer_than_values", "negative"])
def test_moving_average_rejects_a_bad_window(sequences, window):
    _expect_value_error(lambda: sequences.moving_average([1, 2, 3], window), f"moving_average([1, 2, 3], {window})",
                        "the window must be between 1 and len(values)")


# ---------------------------------------------------------------- exponential_moving_average
def _ema_oracle(values, beta):
    """v(t) = β v(t − 1) + (1 − β) x(t), v(0) = 0: a linear filter (scipy.signal.lfilter)."""
    if len(values) == 0:
        return np.array([])
    return lfilter([1 - beta], [1, -beta], np.asarray(values, dtype=float))


EMA = [([10, 10], 0.5, "the docstring example"), ([40, 0, 20, 20], 0.75, "beta = 0.75"),
       ([3, 1, 4, 1, 5], 0.0, "beta = 0: the values themselves"), ([100] * 30, 0.9, "a constant series"),
       ([2.5, -1.0, 7.25], 0.3, "negative values"), ([], 0.8, "no value: an empty list")]


@pytest.mark.parametrize("values, beta, why", EMA, ids=[e[2] for e in EMA])
def test_exponential_moving_average_matches_scipy(sequences, values, beta, why):
    want = _ema_oracle(values, beta)
    got = _result(lambda: sequences.exponential_moving_average(values, beta), f"{_floats(want)} ({why})")
    assert isinstance(got, list) and len(got) == len(want) and np.allclose(got, want), (
        f"expected exponential_moving_average({values if len(values) < 8 else '[…]'}, {beta}) == "
        f"{_floats(want) if len(want) < 8 else _floats(want[:4]) + ['…']} ({why}; v(0) = 0 and v(t) = beta*v(t - 1) "
        f"+ (1 - beta)*x(t)), got {got!r}")


def test_exponential_moving_average_matches_scipy_on_random_cases(sequences):
    rng = np.random.default_rng(54)
    for _ in range(30):
        values = list(np.round(rng.normal(0, 3, size=int(rng.integers(1, 40))), 2))
        beta = float(rng.choice([0.0, 0.1, 0.5, 0.9, 0.99]))
        want = _ema_oracle(values, beta)
        got = _result(lambda: sequences.exponential_moving_average(values, beta), f"{len(want)} averages")
        assert len(got) == len(want) and np.allclose(got, want), (
            f"expected the {len(want)} exponential moving averages of {values[:5]}… with beta = {beta}, starting "
            f"{_floats(want[:3])}, got {got[:3] if isinstance(got, list) else got!r}")


def test_exponential_moving_average_starts_from_zero(sequences):
    got = _result(lambda: sequences.exponential_moving_average([50, 50, 50], 0.8), "[10.0, 18.0, 24.4]")
    assert got == pytest.approx([10.0, 18.0, 24.4]), (
        f"expected [10.0, 18.0, 24.4]: v(0) = 0, so v(1) = (1 - beta) * x(1) = 0.2 * 50, not x(1); got {got!r}")


@pytest.mark.parametrize("beta", [1, 1.5, -0.1], ids=["one", "above_one", "negative"])
def test_exponential_moving_average_rejects_a_bad_beta(sequences, beta):
    _expect_value_error(lambda: sequences.exponential_moving_average([1, 2], beta),
                        f"exponential_moving_average([1, 2], {beta})", "beta must be in [0, 1)")
