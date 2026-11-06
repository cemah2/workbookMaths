"""Tests of mymath.arith (chapter R1): fractions, scientific notation, percentages, weighted mean.

Oracles: ``math.gcd`` and ``fractions.Fraction`` (exact arithmetic), ``decimal.Decimal`` (the digits of a
number written in base 10) and exact rational computations. They describe the expected behaviour without
showing the solution.

    pytest tests/test_r1_arith.py              # your code
    pytest tests/test_r1_arith.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import random
from decimal import ROUND_HALF_EVEN, Decimal
from fractions import Fraction

import pytest


@pytest.fixture
def arith(mymath_module):
    return mymath_module("arith")


def _pairs(n=60, seed=0, low=-500, high=500):
    rng = random.Random(seed)
    return [(rng.randint(low, high), rng.randint(low, high)) for _ in range(n)]


# ---------------------------------------------------------------- the stub's rule: no trusted tool inside
def test_arith_uses_neither_math_gcd_nor_fractions(arith):
    try:
        tree = ast.parse(inspect.getsource(arith))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    used = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            used.update(alias.name for alias in node.names if alias.name == "fractions")
        elif isinstance(node, ast.ImportFrom):
            if node.module == "fractions":
                used.add("fractions")
            if node.module == "math" and any(alias.name == "gcd" for alias in node.names):
                used.add("math.gcd")
        elif isinstance(node, ast.Attribute) and node.attr == "gcd" and getattr(node.value, "id", "") == "math":
            used.add("math.gcd")
    assert not used, (
        f"expected arith.py to work without {', '.join(sorted(used))} (the tests use it as the trusted answer): "
        "write the computation yourself")


# ---------------------------------------------------------------- gcd
def test_gcd_matches_math_gcd(arith):
    for a, b in _pairs():
        got = arith.gcd(a, b)
        assert got == math.gcd(a, b), f"expected gcd({a}, {b}) == {math.gcd(a, b)} (like math.gcd), got {got!r}"


@pytest.mark.parametrize("a, b, want, why", [
    (84, 36, 12, "the docstring example"),
    (-9, 6, 3, "a negative input: the gcd is never negative"),
    (17, 5, 1, "two numbers with no common divisor but 1"),
    (0, 7, 7, "every integer divides 0, so gcd(0, b) is |b|"),
    (-12, 0, 12, "gcd(a, 0) is |a|"),
    (0, 0, 0, "gcd(0, 0) is 0 by convention (docstring)"),
])
def test_gcd_special_cases(arith, a, b, want, why):
    got = arith.gcd(a, b)
    assert got == want, f"expected gcd({a}, {b}) == {want} ({why}), got {got!r}"


def test_gcd_returns_an_int(arith):
    got = arith.gcd(84, 36)
    assert isinstance(got, int) and not isinstance(got, bool), (
        f"expected an int (use % and //, never /), got {got!r} of type {type(got).__name__}")


def test_gcd_large_numbers_quickly(arith):
    a, b = 2**61 - 1, 2**31 - 1   # two primes: Euclid needs a few dozen steps, a loop over divisors would never end
    got = arith.gcd(a * 6, b * 4)
    assert got == 2, f"expected gcd({a * 6}, {b * 4}) == 2 quickly: use Euclid's algorithm, got {got!r}"


# ---------------------------------------------------------------- simplify_fraction
def test_simplify_fraction_matches_fraction(arith):
    for p, q in _pairs(seed=1):
        if q == 0:
            continue
        want = Fraction(p, q)
        got = arith.simplify_fraction(p, q)
        assert got == (want.numerator, want.denominator), (
            f"expected simplify_fraction({p}, {q}) == {(want.numerator, want.denominator)}, got {got!r}")


@pytest.mark.parametrize("p, q, want, why", [
    (84, -36, (-7, 3), "the docstring example: the sign goes to the numerator"),
    (-6, -8, (3, 4), "two minus signs cancel"),
    (0, -5, (0, 1), "zero is written (0, 1)"),
    (7, 1, (7, 1), "an integer keeps the denominator 1"),
    (5, 5, (1, 1), "a fraction equal to 1"),
])
def test_simplify_fraction_special_cases(arith, p, q, want, why):
    got = arith.simplify_fraction(p, q)
    assert got == want, f"expected simplify_fraction({p}, {q}) == {want} ({why}), got {got!r}"


def test_simplify_fraction_returns_ints(arith):
    got = arith.simplify_fraction(84, 36)
    assert isinstance(got, tuple) and all(isinstance(v, int) and not isinstance(v, bool) for v in got), (
        f"expected a tuple of two int, like (7, 3) (divide with //, never /), got {got!r}")


def test_simplify_fraction_zero_denominator_raises(arith):
    with pytest.raises(ValueError):
        arith.simplify_fraction(3, 0)
        pytest.fail("expected simplify_fraction(3, 0) to raise ValueError (no fraction has a zero denominator), "
                    "but it returned")


# ---------------------------------------------------------------- add_fractions
def test_add_fractions_matches_fraction(arith):
    rng = random.Random(2)
    for _ in range(60):
        a = (rng.randint(-60, 60), rng.choice([d for d in range(-30, 31) if d != 0]))
        b = (rng.randint(-60, 60), rng.choice([d for d in range(-30, 31) if d != 0]))
        want = Fraction(*a) + Fraction(*b)
        got = arith.add_fractions(a, b)
        assert got == (want.numerator, want.denominator), (
            f"expected add_fractions({a}, {b}) == {(want.numerator, want.denominator)} (irreducible, "
            f"denominator > 0), got {got!r}")


@pytest.mark.parametrize("a, b, want, why", [
    ((1, 6), (1, 4), (5, 12), "the docstring example: the common denominator is 12, not 24"),
    ((1, 3), (2, 3), (1, 1), "the sum is the integer 1"),
    ((1, 2), (-1, 2), (0, 1), "the sum is zero"),
    ((3, -4), (1, 4), (-1, 2), "a negative denominator"),
])
def test_add_fractions_special_cases(arith, a, b, want, why):
    got = arith.add_fractions(a, b)
    assert got == want, f"expected add_fractions({a}, {b}) == {want} ({why}), got {got!r}"


def test_add_fractions_is_exact_for_large_denominators(arith):
    a, b = (1, 3**30), (1, 2**40)
    want = Fraction(*a) + Fraction(*b)
    got = arith.add_fractions(a, b)
    assert got == (want.numerator, want.denominator), (
        f"expected the exact sum {(want.numerator, want.denominator)}: never go through a float, got {got!r}")


def test_add_fractions_zero_denominator_raises(arith):
    with pytest.raises(ValueError):
        arith.add_fractions((1, 2), (1, 0))
        pytest.fail("expected add_fractions((1, 2), (1, 0)) to raise ValueError, but it returned")


# ---------------------------------------------------------------- scientific_notation
def _expected_notation(text: str, digits: int):
    """(mantissa, exponent) of the decimal number written in ``text``, rounded to ``digits`` significant digits."""
    d = Decimal(text)
    if d == 0:
        return 0.0, 0
    exponent = d.adjusted()
    mantissa = d.scaleb(-exponent).quantize(Decimal(1).scaleb(-(digits - 1)), rounding=ROUND_HALF_EVEN)
    if abs(mantissa) >= 10:
        mantissa, exponent = (mantissa / 10).quantize(Decimal(1).scaleb(-(digits - 1))), exponent + 1
    return float(mantissa), exponent


def _far_from_a_tie(text: str, digits: int) -> bool:
    d = Decimal(text)
    shifted = abs(d.scaleb(-d.adjusted() + digits - 1))
    fraction = shifted - int(shifted)
    return abs(fraction - Decimal("0.5")) > Decimal("0.01")


def _random_numbers(seed=3, n=80):
    rng = random.Random(seed)
    out = []
    while len(out) < n:
        sign = rng.choice(["", "-"])
        digits = "".join(str(rng.randint(0, 9)) for _ in range(6))
        text = f"{sign}{rng.randint(1, 9)}.{digits}e{rng.randint(-12, 12)}"
        if _far_from_a_tie(text, 3) and _far_from_a_tie(text, 2) and _far_from_a_tie(text, 1):
            out.append(text)
    return out


@pytest.mark.parametrize("digits", [1, 2, 3])
def test_scientific_notation_matches_decimal(arith, digits):
    for text in _random_numbers():
        want_m, want_e = _expected_notation(text, digits)
        got = arith.scientific_notation(float(text), digits=digits)
        assert isinstance(got, tuple) and len(got) == 2, (
            f"expected a tuple (mantissa, exponent), got {got!r}")
        m, e = got
        assert e == want_e and m == pytest.approx(want_m, abs=1e-9), (
            f"expected scientific_notation({text}, digits={digits}) == {(want_m, want_e)}, got {got!r}")


@pytest.mark.parametrize("x, digits, want, why", [
    (0.000123456, 3, (1.23, -4), "the docstring example: a negative exponent"),
    (9996, 3, (1.0, 4), "rounding gives 10.0: write it 1.00 × 10^4"),
    (1000, 3, (1.0, 3), "an exact power of 10"),
    (-0.00999, 2, (-1.0, -2), "a negative number whose rounding also gives 10"),
    (7.0, 3, (7.0, 0), "a number between 1 and 10 has exponent 0"),
    (0, 3, (0.0, 0), "zero is (0.0, 0) by convention (docstring)"),
])
def test_scientific_notation_special_cases(arith, x, digits, want, why):
    got = arith.scientific_notation(x, digits=digits)
    assert isinstance(got, tuple) and len(got) == 2 and got[1] == want[1] and got[0] == pytest.approx(want[0]), (
        f"expected scientific_notation({x}, digits={digits}) == {want} ({why}), got {got!r}")


def test_scientific_notation_default_digits_is_3(arith):
    got = arith.scientific_notation(123456.0)
    assert got[1] == 5 and got[0] == pytest.approx(1.23), (
        f"expected scientific_notation(123456.0) == (1.23, 5) with the default digits=3, got {got!r}")


def test_scientific_notation_exponent_is_an_int(arith):
    got = arith.scientific_notation(0.0042)
    assert isinstance(got[1], int) and not isinstance(got[1], bool), (
        f"expected the exponent as an int (-3 for 0.0042), got {got[1]!r} of type {type(got[1]).__name__}")


# ---------------------------------------------------------------- successive_changes
def test_successive_changes_matches_exact_product(arith):
    rng = random.Random(4)
    for _ in range(40):
        rates = [rng.randint(-90, 150) / 100 for _ in range(rng.randint(1, 6))]
        coefficient = Fraction(1)
        for rate in rates:
            coefficient *= 1 + Fraction(rate).limit_denominator(100)
        want = float(coefficient - 1)
        got = arith.successive_changes(rates)
        assert got == pytest.approx(want, abs=1e-9), (
            f"expected successive_changes({rates}) == {want:.6f} (multiply the coefficients 1 + rate), got {got!r}")


@pytest.mark.parametrize("rates, want, why", [
    ([0.10, -0.10], -0.01, "the docstring example: +10 % then -10 % is -1 %, not 0 %"),
    ([0.5], 0.5, "one change is itself"),
    ([], 0.0, "no change at all (docstring)"),
    ([0.25, -0.20], 0.0, "-20 % exactly cancels +25 %"),
    ([-1.0, 0.5], -1.0, "after -100 % the value is 0, and stays 0"),
])
def test_successive_changes_special_cases(arith, rates, want, why):
    got = arith.successive_changes(rates)
    assert got == pytest.approx(want, abs=1e-12), f"expected successive_changes({rates}) == {want} ({why}), got {got!r}"


def test_successive_changes_rate_below_minus_one_raises(arith):
    with pytest.raises(ValueError):
        arith.successive_changes([0.1, -1.5])
        pytest.fail("expected successive_changes([0.1, -1.5]) to raise ValueError (a value cannot lose more than "
                    "100 %), but it returned")


# ---------------------------------------------------------------- weighted_mean
def test_weighted_mean_matches_exact_computation(arith):
    rng = random.Random(5)
    for _ in range(40):
        n = rng.randint(1, 8)
        values = [rng.randint(-50, 50) / 4 for _ in range(n)]
        weights = [rng.randint(0, 10) for _ in range(n)]
        if sum(weights) == 0:
            weights[0] = 1
        want = float(sum(Fraction(v) * w for v, w in zip(values, weights)) / sum(weights))
        got = arith.weighted_mean(values, weights)
        assert got == pytest.approx(want), (
            f"expected weighted_mean({values}, {weights}) == {want:.6f}, got {got!r}")


@pytest.mark.parametrize("values, weights, want, why", [
    ([12, 15], [1, 2], 14.0, "the docstring example"),
    ([3, 9], [1, 1], 6.0, "equal weights give the ordinary mean"),
    ([4, 100], [1, 0], 4.0, "a zero weight ignores its value"),
    ([2, 5], [10, 20], 4.0, "multiplying every weight by 10 changes nothing"),
])
def test_weighted_mean_special_cases(arith, values, weights, want, why):
    got = arith.weighted_mean(values, weights)
    assert got == pytest.approx(want), f"expected weighted_mean({values}, {weights}) == {want} ({why}), got {got!r}"


def test_weighted_mean_returns_float(arith):
    got = arith.weighted_mean([1, 2], [1, 1])
    assert isinstance(got, float), (
        f"expected a float (1.5 for [1, 2] with equal weights: divide with /), got {got!r} of type "
        f"{type(got).__name__}")


@pytest.mark.parametrize("values, weights, why", [
    ([1, 2, 3], [1, 1], "the lengths differ"),
    ([1, 2], [1, -1], "a weight is negative"),
    ([1, 2], [0, 0], "the weights sum to zero"),
], ids=["lengths", "negative", "zero_sum"])
def test_weighted_mean_invalid_raises(arith, values, weights, why):
    with pytest.raises(ValueError):
        arith.weighted_mean(values, weights)
        pytest.fail(f"expected weighted_mean({values}, {weights}) to raise ValueError ({why}), but it returned")
