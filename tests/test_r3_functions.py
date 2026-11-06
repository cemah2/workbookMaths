"""Tests of mymath.functions (chapter R3): Horner, affine functions, quadratics, composition.

Oracles: NumPy (``numpy.polyval``, ``numpy.polyfit``) and SymPy (exact real roots, exact vertex). They describe the
expected behaviour without showing the solution.

    pytest tests/test_r3_functions.py              # your code
    pytest tests/test_r3_functions.py --impl=ref   # the reference
"""

import random

import numpy as np
import pytest
import sympy as sp

X = sp.Symbol("x", real=True)


@pytest.fixture
def functions(mymath_module):
    return mymath_module("functions")


def _expect_value_error(call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ValueError."""
    try:
        call()
    except ValueError:
        return
    except NotImplementedError:
        raise                 # a function not written yet: the notebook shows ⏳, not a failure
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned a value")


def _close(got, want):
    return isinstance(got, (tuple, list)) and len(got) == len(want) and all(
        g == pytest.approx(w, rel=1e-9, abs=1e-9) for g, w in zip(got, want))


# ---------------------------------------------------------------- polyval
def test_polyval_matches_numpy(functions):
    rng = random.Random(0)
    for _ in range(60):
        coefficients = [rng.randint(-9, 9) for _ in range(rng.randint(1, 6))]
        x = rng.randint(-6, 6) / 2
        want = float(np.polyval(coefficients, x))
        got = functions.polyval(coefficients, x)
        assert got == pytest.approx(want), (
            f"expected polyval({coefficients}, {x}) == {want} (like numpy.polyval), got {got!r}")


@pytest.mark.parametrize("coefficients, x, want, why", [
    ([2, 0, -1], 3, 17, "the docstring example"),
    ([5], 10, 5, "a constant polynomial"),
    ([1, 0, 0, 0], -2, -8, "x³: the zero coefficients count"),
    ([3, -1], 0, -1, "at x = 0, the constant term"),
    ([], 4, 0, "an empty list is the zero polynomial"),
])
def test_polyval_special_cases(functions, coefficients, x, want, why):
    got = functions.polyval(coefficients, x)
    assert got == pytest.approx(want), f"expected polyval({coefficients}, {x}) == {want} ({why}), got {got!r}"


def test_polyval_keeps_integers(functions):
    got = functions.polyval([2, 0, -1], 3)
    assert isinstance(got, int) and got == 17, (
        f"expected the int 17: with int coefficients and an int x, Horner only multiplies and adds, got {got!r}")


def test_polyval_highest_degree_first(functions):
    got = functions.polyval([1, 2], 10)
    assert got == pytest.approx(12), (
        f"expected polyval([1, 2], 10) == 12, that is 1·x + 2 (the first coefficient goes with the highest "
        f"degree), got {got!r}")


def test_polyval_works_on_a_numpy_array(functions):
    xs = np.array([-1.0, 0.0, 2.0])
    got = functions.polyval([1, -3, 2], xs)
    want = np.polyval([1, -3, 2], xs)
    assert isinstance(got, np.ndarray) and got.shape == xs.shape and np.allclose(got, want), (
        f"expected an array {want.tolist()}: plain + and * work element-wise on a NumPy array, got {got!r}")


# ---------------------------------------------------------------- affine_from_points
def test_affine_from_points_matches_numpy(functions):
    rng = random.Random(1)
    for _ in range(50):
        x1, x2 = rng.sample(range(-10, 11), 2)
        y1, y2 = rng.randint(-20, 20), rng.randint(-20, 20)
        want = np.polyfit([x1, x2], [y1, y2], 1)
        got = functions.affine_from_points((x1, y1), (x2, y2))
        assert _close(got, want), (
            f"expected affine_from_points({(x1, y1)}, {(x2, y2)}) == ({want[0]:.6g}, {want[1]:.6g}) "
            f"(slope, intercept), got {got!r}")


@pytest.mark.parametrize("p, q, want, why", [
    ((1, 3), (3, 7), (2.0, 1.0), "the docstring example"),
    ((3, 7), (1, 3), (2.0, 1.0), "the order of the two points does not matter"),
    ((-2, 5), (4, 5), (0.0, 5.0), "a horizontal line: slope 0"),
    ((0, 1), (4, 0), (-0.25, 1.0), "a negative slope that is not a whole number"),
])
def test_affine_from_points_special_cases(functions, p, q, want, why):
    got = functions.affine_from_points(p, q)
    assert _close(got, want), f"expected affine_from_points({p}, {q}) == {want} ({why}), got {got!r}"


def test_affine_from_points_returns_a_tuple_of_floats(functions):
    got = functions.affine_from_points((1, 3), (3, 7))
    assert isinstance(got, tuple) and len(got) == 2 and all(isinstance(v, float) for v in got), (
        f"expected the tuple (2.0, 1.0), two floats (m, c), got {got!r}")


@pytest.mark.parametrize("p, q", [((2, 1), (2, 5)), ((0, 0), (0, 0))], ids=["vertical", "same_point"])
def test_affine_from_points_same_abscissa_raises(functions, p, q):
    _expect_value_error(lambda: functions.affine_from_points(p, q), f"affine_from_points({p}, {q})",
                        "the two points have the same abscissa: no function goes through both")


# ---------------------------------------------------------------- quadratic_roots
def _sympy_roots(a, b, c):
    return sorted(float(r) for r in sp.solveset(a * X**2 + b * X + c, X, sp.S.Reals))


def test_quadratic_roots_matches_sympy(functions):
    rng = random.Random(2)
    for _ in range(80):
        a = rng.choice([v for v in range(-6, 7) if v != 0])
        b, c = rng.randint(-12, 12), rng.randint(-12, 12)
        want = _sympy_roots(a, b, c)
        got = functions.quadratic_roots(a, b, c)
        assert isinstance(got, list) and _close(got, want), (
            f"expected quadratic_roots({a}, {b}, {c}) == {want} (the real roots, in increasing order), got {got!r}")


@pytest.mark.parametrize("a, b, c, want, why", [
    (1, -3, 2, [1.0, 2.0], "the docstring example"),
    (4, -4, 1, [0.5], "a double root (discriminant 0): listed once"),
    (3, -2, 4, [], "a negative discriminant: no real root, an empty list"),
    (-2, 2, 12, [-2.0, 3.0], "a negative a: the roots still in increasing order"),
    (4, 0, -1, [-0.5, 0.5], "b = 0: two opposite roots"),
    (3, 5, 0, [-5 / 3, 0.0], "c = 0: 0 is a root"),
])
def test_quadratic_roots_special_cases(functions, a, b, c, want, why):
    got = functions.quadratic_roots(a, b, c)
    assert isinstance(got, list) and _close(got, want), (
        f"expected quadratic_roots({a}, {b}, {c}) == {want} ({why}), got {got!r}")


def test_quadratic_roots_returns_floats(functions):
    got = functions.quadratic_roots(1, -3, 2)
    assert isinstance(got, list) and all(isinstance(r, float) for r in got), (
        f"expected [1.0, 2.0], a list of floats, got {got!r}")


def test_quadratic_roots_zero_a_raises(functions):
    _expect_value_error(lambda: functions.quadratic_roots(0, 2, 1), "quadratic_roots(0, 2, 1)",
                        "with a = 0, the expression is not of degree 2")


# ---------------------------------------------------------------- quadratic_vertex
def _sympy_vertex(a, b, c):
    alpha = sp.Rational(-b, 2 * a)
    return (float(alpha), float(a * alpha**2 + b * alpha + c))


def test_quadratic_vertex_matches_sympy(functions):
    rng = random.Random(3)
    for _ in range(60):
        a = rng.choice([v for v in range(-6, 7) if v != 0])
        b, c = rng.randint(-12, 12), rng.randint(-12, 12)
        want = _sympy_vertex(a, b, c)
        got = functions.quadratic_vertex(a, b, c)
        assert _close(got, want), (
            f"expected quadratic_vertex({a}, {b}, {c}) == ({want[0]:.6g}, {want[1]:.6g}) (alpha, beta), got {got!r}")


@pytest.mark.parametrize("a, b, c, want, why", [
    (1, -4, 1, (2.0, -3.0), "the docstring example"),
    (-2, 4, 1, (1.0, 3.0), "a negative a: the vertex is a maximum"),
    (3, 0, 7, (0.0, 7.0), "b = 0: the vertex is on the vertical axis"),
])
def test_quadratic_vertex_special_cases(functions, a, b, c, want, why):
    got = functions.quadratic_vertex(a, b, c)
    assert _close(got, want), f"expected quadratic_vertex({a}, {b}, {c}) == {want} ({why}), got {got!r}"


def test_quadratic_vertex_returns_a_tuple(functions):
    got = functions.quadratic_vertex(1, -4, 1)
    assert isinstance(got, tuple) and len(got) == 2, f"expected the tuple (2.0, -3.0), not a list, got {got!r}"


def test_quadratic_vertex_zero_a_raises(functions):
    _expect_value_error(lambda: functions.quadratic_vertex(0, 2, 1), "quadratic_vertex(0, 2, 1)",
                        "with a = 0, there is no parabola, so no vertex")


# ---------------------------------------------------------------- compose
def test_compose_returns_a_function(functions):
    h = functions.compose(lambda t: t + 1, lambda t: 2 * t)
    assert callable(h), f"expected compose(f, g) to return a function (callable), got {h!r}"


def test_compose_applies_g_first(functions):
    h = functions.compose(lambda t: t + 1, lambda t: 2 * t)
    got = h(5)
    assert got == 11, (f"expected compose(f, g)(5) == 11 with f(t) = t + 1 and g(t) = 2t: g first (2 × 5 = 10), "
                       f"then f (10 + 1), got {got!r}")


def test_compose_matches_direct_evaluation(functions):
    pairs = [(lambda t: t**2, lambda t: t - 3), (lambda t: 1 / t, lambda t: t + 2), (abs, lambda t: 4 - t)]
    for k, (f, g) in enumerate(pairs):
        h = functions.compose(f, g)
        for x in (-1.5, 0.5, 2.0, 7.0):
            assert h(x) == pytest.approx(f(g(x))), f"expected compose(f, g)({x}) == f(g({x})) for pair {k}, got {h(x)!r}"


def test_compose_does_not_call_the_functions_too_early(functions):
    calls = []

    def g(t):
        calls.append(t)
        return t

    h = functions.compose(lambda t: t, g)
    assert calls == [], (f"expected compose to only build the new function (no call yet), but g was already called "
                         f"with {calls}")
    h(3)
    h(4)
    assert calls == [3, 4], f"expected g to be called once for each call of the composite, with 3 then 4, got {calls}"


def test_compose_can_be_chained(functions):
    h = functions.compose(functions.compose(lambda t: t - 1, lambda t: 3 * t), lambda t: t**2)
    assert h(2) == 11, f"expected compose(compose(f, g), k)(2) == f(g(k(2))) == 3·4 − 1 == 11, got {h(2)!r}"


def test_compose_works_on_numpy_arrays(functions):
    h = functions.compose(np.sqrt, lambda t: t + 1)
    xs = np.array([0.0, 3.0, 8.0])
    got = h(xs)
    assert isinstance(got, np.ndarray) and np.allclose(got, [1.0, 2.0, 3.0]), (
        f"expected array([1., 2., 3.]): the composite passes the array to g, then to f, got {got!r}")
