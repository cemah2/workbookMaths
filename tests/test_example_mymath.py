"""Example of a mymath test (session 1): oracle + property tests.

The oracle is NumPy: ``mymath._example.mean`` must agree with ``np.mean``.
These tests do not reveal the solution; they only describe the expected behaviour.

    pytest tests/test_example_mymath.py              # your code
    pytest tests/test_example_mymath.py --impl=ref   # the reference
"""

import numpy as np
import pytest


@pytest.fixture
def example(mymath_module):
    return mymath_module("_example")


def test_mean_matches_numpy(example):
    rng = np.random.default_rng(0)
    for _ in range(20):
        values = rng.normal(size=int(rng.integers(1, 50)))
        try:
            got = example.mean(values)
        except ValueError as exc:
            if "ambiguous" not in str(exc):
                raise
            pytest.fail("expected mean to accept a NumPy array, but `if not values` fails on an array: "
                        "test the empty case with `len(values) == 0`")
        want = np.mean(values)
        assert got == pytest.approx(want), (
            f"expected the mean of {len(values)} random values (a NumPy array) to be {want:.6f} like np.mean, "
            f"got {got!r}")


def test_mean_small_list(example):
    got = example.mean([1, 2, 3, 4])
    assert got == pytest.approx(2.5), f"expected mean([1, 2, 3, 4]) == 2.5, got {got!r}"


def test_mean_single_value(example):
    got = example.mean([7])
    assert got == pytest.approx(7.0), f"expected mean([7]) == 7.0 (a single value is its own mean), got {got!r}"


def test_mean_returns_float(example):
    got = example.mean([1, 2])
    assert isinstance(got, float), (
        f"expected a float (1.5 for [1, 2]: divide with /, not //), got {got!r} of type {type(got).__name__}")


def test_mean_empty_raises_value_error(example):
    with pytest.raises(ValueError):
        example.mean([])
        pytest.fail("expected mean([]) to raise ValueError (an empty sequence has no mean), but it returned")
