"""Tests of mymath.explog (chapter R6): logarithm in any base, sigmoid, tanh, doubling time.

Oracles: ``math.log2``, ``math.log10`` and exact powers for the logarithms, ``scipy.special.expit`` for the sigmoid,
``numpy.tanh`` for the hyperbolic tangent, and ``(1 + rate)**n == 2`` checked directly for the doubling time. They
describe the expected behaviour without showing the solution.

    pytest tests/test_r6_explog.py              # your code
    pytest tests/test_r6_explog.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import random

import numpy as np
import pytest
from scipy.special import expit


@pytest.fixture
def explog(mymath_module):
    return mymath_module("explog")


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


def test_explog_uses_only_exp_and_log(explog):
    """The docstring allows math.exp and math.log with one argument (ln), not the ready-made tanh, log2, log10, the
    sigmoid of SciPy, nor math.log(x, base), which is log_base itself. math.log1p, ln(1 + x) computed precisely, is
    allowed (R6.22)."""
    try:
        tree = ast.parse(inspect.getsource(explog))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    forbidden = {"tanh", "log2", "log10", "expit", "logit", "sinh", "cosh"}
    log_names = {alias.asname or alias.name for node in ast.walk(tree)        # from math import log (as ln)
                 if isinstance(node, ast.ImportFrom) and node.module == "math"
                 for alias in node.names if alias.name == "log"}
    used = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in forbidden:
            used.add(f"{getattr(node.value, 'id', '?')}.{node.attr}")
        elif isinstance(node, ast.ImportFrom) and any(alias.name in forbidden for alias in node.names):
            used.update(f"{node.module}.{alias.name}" for alias in node.names if alias.name in forbidden)
        elif isinstance(node, ast.Call) and len(node.args) + len(node.keywords) > 1 and (
                (isinstance(node.func, ast.Attribute) and node.func.attr == "log")
                or (isinstance(node.func, ast.Name) and node.func.id in log_names)):
            used.add("math.log(x, base)")
    assert not used, (
        f"expected explog.py to use only math.exp and math.log(x) with one argument, not {', '.join(sorted(used))}: "
        "the docstring asks you to write these functions with exp and ln yourself")


# ---------------------------------------------------------------- log_base
LOGS = [(8, 2, 3.0, "the docstring example"), (729, 3, 6.0, "an exact power of 3"), (0.0625, 2, -4.0, "a power of 1/2"),
        (1, 7, 0.0, "the logarithm of 1 is 0 in every base"), (20, 0.5, -math.log2(20), "a base below 1"),
        (1e-6, 10, -6.0, "a negative power of 10"), (math.e, math.e, 1.0, "log_e(e) = 1")]


@pytest.mark.parametrize("x, base, want, why", LOGS, ids=[g[3] for g in LOGS])
def test_log_base_cases(explog, x, base, want, why):
    got = _result(lambda: explog.log_base(x, base), f"log_base({x}, {base}) ≈ {want} ({why})")
    assert got == pytest.approx(want, rel=1e-12, abs=1e-12), (
        f"expected log_base({x}, {base}) ≈ {want} ({why}: the exponent y such that {base}**y == {x}), got {got!r}")


def test_log_base_inverts_the_power(explog):
    rng = random.Random(61)
    for _ in range(40):
        base = rng.choice([1.5, 2, 3, 5, 10, 0.2, 0.75])
        y = rng.uniform(-8, 8)
        x = base**y
        got = _result(lambda: explog.log_base(x, base), f"{y}")
        assert got == pytest.approx(y, rel=1e-9, abs=1e-9), (
            f"expected log_base({x!r}, {base}) ≈ {y} (since {base}**{y} == {x!r}), got {got!r}")


@pytest.mark.parametrize("x, oracle, name", [(1000.0, math.log10, "log10"), (12345.678, math.log10, "log10"),
                                             (1 / 3, math.log2, "log2"), (7e15, math.log2, "log2")],
                         ids=["log10 of 1000", "log10 of 12345.678", "log2 of 1/3", "log2 of 7e15"])
def test_log_base_matches_log2_and_log10(explog, x, oracle, name):
    base = 10 if name == "log10" else 2
    want = oracle(x)
    got = _result(lambda: explog.log_base(x, base), f"{want} (like math.{name})")
    assert got == pytest.approx(want, rel=1e-12), f"expected log_base({x}, {base}) ≈ math.{name}({x}) = {want}, got {got!r}"


@pytest.mark.parametrize("x, base, why", [(0, 10, "x = 0: ln 0 does not exist"), (-5, 10, "x < 0"),
                                          (5, 1, "base 1: every power of 1 is 1"), (5, 0, "base 0"),
                                          (5, -2, "a negative base")],
                         ids=["x zero", "x negative", "base one", "base zero", "base negative"])
def test_log_base_rejects_bad_inputs(explog, x, base, why):
    _expect_value_error(lambda: explog.log_base(x, base), f"log_base({x}, {base})", why)


# ---------------------------------------------------------------- sigmoid
@pytest.mark.parametrize("x", [0, 0.5, -0.5, 1.2, -1.2, 4, -4, 10, -10, 30, -30], ids=lambda x: f"x={x}")
def test_sigmoid_matches_scipy_expit(explog, x):
    want = float(expit(x))
    got = _result(lambda: explog.sigmoid(x), f"{want} (scipy.special.expit)")
    assert got == pytest.approx(want, rel=1e-12, abs=1e-15), (
        f"expected sigmoid({x}) ≈ {want} (1 / (1 + exp(-x)), like scipy.special.expit), got {got!r}")


def test_sigmoid_docstring_example(explog):
    got = _result(lambda: explog.sigmoid(0), "0.5")
    assert got == 0.5, f"expected sigmoid(0) == 0.5 (the docstring example), got {got!r}"


def test_sigmoid_is_symmetric(explog):
    rng = random.Random(62)
    for _ in range(30):
        x = rng.uniform(-30, 30)
        a, b = _result(lambda: (explog.sigmoid(x), explog.sigmoid(-x)), "σ(x) + σ(−x) = 1")
        assert a + b == pytest.approx(1, abs=1e-12), (
            f"expected sigmoid({x}) + sigmoid({-x}) == 1 (the symmetry σ(−x) = 1 − σ(x)), got {a} + {b} = {a + b}")


def test_sigmoid_stays_in_zero_one(explog):
    values = _result(lambda: [explog.sigmoid(x) for x in (-30, -5, 0, 5, 30)], "values in ]0, 1[")
    assert all(0 < v < 1 for v in values), (
        f"expected values strictly between 0 and 1 for x = -30, -5, 0, 5, 30, got {values}")
    assert values == sorted(values), f"expected an increasing function, got {values} for x = -30, -5, 0, 5, 30"


# ---------------------------------------------------------------- tanh
@pytest.mark.parametrize("x", [0, 0.25, -0.25, 0.75, -2, 2, 5, -5, 18, -18], ids=lambda x: f"x={x}")
def test_tanh_matches_numpy(explog, x):
    want = float(np.tanh(x))
    got = _result(lambda: explog.tanh(x), f"{want} (numpy.tanh)")
    assert got == pytest.approx(want, rel=1e-9, abs=1e-12), (
        f"expected tanh({x}) ≈ {want} ((e^x − e^(−x)) / (e^x + e^(−x)), like numpy.tanh), got {got!r}")


def test_tanh_docstring_example(explog):
    got = _result(lambda: explog.tanh(0), "0.0")
    assert got == 0, f"expected tanh(0) == 0.0 (the docstring example), got {got!r}"


def test_tanh_is_odd_and_bounded(explog):
    rng = random.Random(63)
    for _ in range(30):
        x = rng.uniform(-30, 30)
        a, b = _result(lambda: (explog.tanh(x), explog.tanh(-x)), "tanh(−x) = −tanh(x)")
        assert a == pytest.approx(-b, abs=1e-12), f"expected tanh({-x}) == -tanh({x}) (tanh is odd), got {b} and {a}"
        assert -1 <= a <= 1, f"expected tanh({x}) between -1 and 1, got {a}"


def test_tanh_at_the_ends(explog):
    got = _result(lambda: [explog.tanh(30), explog.tanh(-30)], "[1.0, -1.0] (rounded)")
    assert got == pytest.approx([1.0, -1.0], abs=1e-12), (
        f"expected tanh(30) ≈ 1 and tanh(-30) ≈ -1 (the docstring: |x| <= 30 must work), got {got}")


# ---------------------------------------------------------------- doubling_time
RATES = [(1.0, 1.0, "the docstring example: +100 % doubles in one period"), (0.07, None, "+7 %"),
         (0.25, None, "+25 %"), (0.001, None, "a tiny rate: a long doubling time"), (3.0, 0.5, "+300 %: x4 per period")]


@pytest.mark.parametrize("rate, exact, why", RATES, ids=[r[2].split(":")[0] for r in RATES])
def test_doubling_time_doubles(explog, rate, exact, why):
    got = _result(lambda: explog.doubling_time(rate), f"the real n such that (1 + {rate})**n == 2 ({why})")
    if exact is not None:
        assert got == pytest.approx(exact, rel=1e-12), f"expected doubling_time({rate}) ≈ {exact} ({why}), got {got!r}"
    assert isinstance(got, float), f"expected a float (not rounded, not an int), got {got!r}"
    assert (1 + rate) ** got == pytest.approx(2, rel=1e-9), (
        f"expected (1 + {rate}) ** doubling_time({rate}) == 2 ({why}: a real number of periods, not rounded), "
        f"got doubling_time({rate}) = {got!r}, and (1 + {rate}) ** {got!r} = {(1 + rate) ** got}")


def test_doubling_time_is_close_to_the_rule_of_70_for_small_rates(explog):
    got = _result(lambda: explog.doubling_time(0.01), "about 70 periods for +1 %")
    assert got == pytest.approx(math.log(2) / math.log(1.01), rel=1e-12), (
        f"expected doubling_time(0.01) ≈ {math.log(2) / math.log(1.01)} (the exact value ln 2 / ln 1.01, close to "
        f"the 70 periods of the rule of 70), got {got!r}")


@pytest.mark.parametrize("rate", [0, -0.1], ids=["zero", "negative"])
def test_doubling_time_needs_a_positive_rate(explog, rate):
    _expect_value_error(lambda: explog.doubling_time(rate), f"doubling_time({rate})",
                        "a quantity that does not grow never doubles")
