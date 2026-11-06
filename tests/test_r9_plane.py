"""Tests of mymath.plane (chapter R9): vectors, norm, dot product, angle, line through two points, radians.

Oracles: ``numpy`` (``np.linalg.norm``, ``np.dot``, ``np.arccos``), exact arithmetic with ``fractions.Fraction``
(a point is on a line when ``a*x + b*y + c`` is exactly 0) and ``math.radians``. They describe the expected behaviour
without showing the solution.

    pytest tests/test_r9_plane.py              # your code
    pytest tests/test_r9_plane.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import random
from fractions import Fraction

import numpy as np
import pytest


@pytest.fixture
def plane(mymath_module):
    return mymath_module("plane")


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


def _random_vectors(seed, count=20):
    """Pairs of random integer vectors of the same dimension (1 to 6), never zero."""
    rng = random.Random(seed)
    pairs = []
    while len(pairs) < count:
        n = rng.randint(1, 6)
        u = tuple(rng.randint(-9, 9) for _ in range(n))
        v = tuple(rng.randint(-9, 9) for _ in range(n))
        if any(u) and any(v):
            pairs.append((u, v))
    return pairs


def test_plane_uses_only_python_and_math(plane):
    """Convention of chapters R0 to R9: plain Python and the math module (no NumPy, SciPy or SymPy in plane.py)."""
    try:
        tree = ast.parse(inspect.getsource(plane))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    forbidden = sorted(imported - {"math", "__future__", "typing"})
    assert not forbidden, (
        f"expected plane.py to import only math (plain Python, the convention of chapters R0 to R9), not "
        f"{', '.join(forbidden)}: write the sums of products and the square roots yourself")


# ---------------------------------------------------------------- vector
def test_vector_docstring_example(plane):
    got = _result(lambda: plane.vector((1, 2), (4, 6)), "(3, 4) (the docstring example)")
    assert tuple(got) == (3, 4), f"expected vector((1, 2), (4, 6)) == (3, 4) (end minus start), got {got!r}"


def test_vector_is_end_minus_start(plane):
    got = _result(lambda: plane.vector((5, -1), (2, 3)), "(-3, 4)")
    assert tuple(got) == (-3, 4), (
        f"expected vector((5, -1), (2, 3)) == (-3, 4): B minus A, not A minus B; got {got!r}")


def test_vector_returns_a_tuple(plane):
    got = _result(lambda: plane.vector((0, 0), (1, 2)), "a tuple")
    assert isinstance(got, tuple), f"expected a tuple (as the docstring says), got {type(got).__name__} {got!r}"


@pytest.mark.parametrize("A, B", [((1, 2, 3), (0, 0, 0)), ((2.5, -1.5, 4, 0), (1, 1, 1, 1)), ((7,), (-2,))],
                         ids=["dimension 3", "dimension 4", "dimension 1"])
def test_vector_works_in_any_dimension(plane, A, B):
    expected = tuple(float(x) for x in np.subtract(B, A))
    got = _result(lambda: plane.vector(A, B), f"{expected} (numpy B - A)")
    assert got is not None and len(got) == len(A) and np.allclose(got, expected), (
        f"expected vector({A}, {B}) == {expected} (numpy B - A), got {got!r}")


@pytest.mark.parametrize("A, B", [((1, 2), (1, 2, 3)), ((0, 0, 0), (1, 1))], ids=["2 and 3", "3 and 2"])
def test_vector_refuses_points_of_different_dimensions(plane, A, B):
    _expect_value_error(lambda: plane.vector(A, B), f"vector({A}, {B})", "the points do not have the same dimension")


# ---------------------------------------------------------------- norm
def test_norm_docstring_example(plane):
    got = _result(lambda: plane.norm((3, 4)), "5.0 (the docstring example)")
    assert got == pytest.approx(5.0), f"expected norm((3, 4)) == 5.0 (√(9 + 16)), got {got!r}"


@pytest.mark.parametrize("u", [(0, 0), (0, 0, 0, 0)], ids=["(0, 0)", "zero in dimension 4"])
def test_norm_of_the_zero_vector_is_zero(plane, u):
    got = _result(lambda: plane.norm(u), "0.0")
    assert got == 0, f"expected norm({u}) == 0.0 (the zero vector has no length), got {got!r}"


def test_norm_returns_a_float(plane):
    got = _result(lambda: plane.norm((2, -2, 1)), "3.0, a float")
    assert isinstance(got, float), f"expected a float (a square root), got {type(got).__name__} {got!r}"


@pytest.mark.parametrize("u", [(-5, 0), (0, -2.5), (-1, -1, -1, -1)], ids=["(-5, 0)", "(0, -2.5)", "all -1"])
def test_norm_of_negative_coordinates_is_positive(plane, u):
    expected = float(np.linalg.norm(u))
    got = _result(lambda: plane.norm(u), f"{expected} (np.linalg.norm)")
    assert got == pytest.approx(expected), (
        f"expected norm({u}) == {expected} (np.linalg.norm: square each coordinate), got {got!r}")


def test_norm_matches_numpy_in_every_dimension(plane):
    for u, _ in _random_vectors(9):
        expected = float(np.linalg.norm(u))
        got = _result(lambda: plane.norm(u), f"{expected} (np.linalg.norm)")
        assert got == pytest.approx(expected), f"expected norm({u}) == {expected} (np.linalg.norm), got {got!r}"


# ---------------------------------------------------------------- dot
def test_dot_docstring_example(plane):
    got = _result(lambda: plane.dot((1, 2), (3, -1)), "1 (the docstring example)")
    assert got == 1, f"expected dot((1, 2), (3, -1)) == 1 (1×3 + 2×(−1)), got {got!r}"


def test_dot_of_ints_is_an_int(plane):
    got = _result(lambda: plane.dot((2, -3, 1), (4, 1, -5)), "0, an int")
    assert isinstance(got, int) and not isinstance(got, bool) and got == 0, (
        f"expected the int 0 (2×4 + (−3)×1 + 1×(−5)), got {type(got).__name__} {got!r}")


def test_dot_matches_numpy_and_is_symmetric(plane):
    for u, v in _random_vectors(19):
        expected = int(np.dot(u, v))
        got = _result(lambda: plane.dot(u, v), f"{expected} (np.dot)")
        assert got == expected, f"expected dot({u}, {v}) == {expected} (np.dot: sum of the products), got {got!r}"
        back = _result(lambda: plane.dot(v, u), f"{expected} (np.dot)")
        assert back == expected, f"expected dot({v}, {u}) == {expected} (u·v = v·u), got {back!r}"


def test_dot_of_a_vector_with_itself_is_its_squared_norm(plane):
    u = (1.5, -2, 0.5)
    expected = float(np.linalg.norm(u)) ** 2
    got = _result(lambda: plane.dot(u, u), f"{expected} (np.linalg.norm(u) ** 2)")
    assert got == pytest.approx(expected), f"expected dot(u, u) == ‖u‖² == {expected} for u = {u}, got {got!r}"


@pytest.mark.parametrize("u, v", [((1, 2), (1, 2, 3)), ((1, 2, 3), (4, 5))], ids=["2 and 3", "3 and 2"])
def test_dot_refuses_vectors_of_different_dimensions(plane, u, v):
    _expect_value_error(lambda: plane.dot(u, v), f"dot({u}, {v})", "the dimensions differ: zip would stop silently")


# ---------------------------------------------------------------- angle_between
def _numpy_angle(u, v):
    u, v = np.asarray(u, dtype=float), np.asarray(v, dtype=float)
    return float(np.arccos(np.clip(u @ v / (np.linalg.norm(u) * np.linalg.norm(v)), -1, 1)))


def test_angle_between_docstring_example(plane):
    got = _result(lambda: plane.angle_between((1, 0), (0, 2)), "π/2 (the docstring example)")
    assert got == pytest.approx(math.pi / 2), f"expected π/2 ≈ 1.5708 (orthogonal vectors), got {got!r}"


@pytest.mark.parametrize("u, v, expected", [((1, 0), (-1, 1), 3 * math.pi / 4), ((2, 0), (-3, 0), math.pi),
                                            ((1, 1), (2, 2), 0.0), ((0, 3), (5, 0), math.pi / 2)],
                         ids=["135°", "opposite: π", "same direction: 0", "90°"])
def test_angle_between_known_angles(plane, u, v, expected):
    got = _result(lambda: plane.angle_between(u, v), f"{expected:.6f} radians")
    assert got == pytest.approx(expected, abs=1e-7), (
        f"expected angle_between({u}, {v}) ≈ {expected:.6f} radians (in [0, π]), got {got!r}")


def test_angle_between_matches_numpy(plane):
    for u, v in _random_vectors(29):
        expected = _numpy_angle(u, v)
        got = _result(lambda: plane.angle_between(u, v), f"{expected:.6f} (np.arccos of the cosine)")
        assert got == pytest.approx(expected, abs=1e-7), (
            f"expected angle_between({u}, {v}) ≈ {expected:.6f} radians (np.arccos), got {got!r}")


def test_angle_between_survives_a_cosine_rounded_above_1(plane):
    """(1, 5) and (2, 10) give a computed cosine of 1.0000000000000002: acos would raise without clamping."""
    for a in range(1, 13):
        for k in (2, 3):
            u, v = (1, a), (k, k * a)
            got = _result(lambda: plane.angle_between(u, v),
                          f"0.0 for {u} and {v} (same direction): clamp the cosine to [-1, 1] before math.acos")
            assert got == pytest.approx(0.0, abs=1e-7), (
                f"expected angle_between({u}, {v}) ≈ 0 (same direction), got {got!r}")


@pytest.mark.parametrize("u, v", [((0, 0), (1, 2)), ((3, -1), (0, 0)), ((0, 0, 0), (0, 0, 0))],
                         ids=["first is zero", "second is zero", "both zero"])
def test_angle_between_refuses_a_zero_vector(plane, u, v):
    _expect_value_error(lambda: plane.angle_between(u, v), f"angle_between({u}, {v})",
                        "the angle with a zero vector is not defined")


# ---------------------------------------------------------------- line_through
def _on_line(equation, point):
    a, b, c = (Fraction(x) for x in equation)
    x, y = (Fraction(t) for t in point)
    return a * x + b * y + c == 0


def _check_line(plane, A, B):
    equation = _result(lambda: plane.line_through(A, B), f"(a, b, c) with a*x + b*y + c == 0 at {A} and {B}")
    assert equation is not None and len(equation) == 3, (
        f"expected a tuple (a, b, c) for line_through({A}, {B}), got {equation!r}")
    a, b, c = equation
    assert (a, b) != (0, 0), f"expected (a, b) != (0, 0) for line_through({A}, {B}), got {equation!r}"
    for point in (A, B):
        assert _on_line(equation, point), (
            f"expected a*x + b*y + c == 0 at {point} for line_through({A}, {B}) = {equation!r}, "
            f"got {a * point[0] + b * point[1] + c!r}")
    return equation


def test_line_through_docstring_example(plane):
    a, b, c = _check_line(plane, (0, 1), (1, 3))
    assert a * 2 + b * 5 + c == 0, f"expected the point (2, 5) on the line through (0, 1) and (1, 3), got {(a, b, c)}"


@pytest.mark.parametrize("A, B", [((1, -1), (3, 5)), ((-2, 4), (6, 4)), ((4, 1), (4, -7)), ((0, 0), (-3, 2))],
                         ids=["slanted", "horizontal", "vertical", "through the origin"])
def test_line_through_contains_both_points(plane, A, B):
    _check_line(plane, A, B)


def test_line_through_contains_the_other_points_of_the_line_and_only_them(plane):
    A, B = (1, -1), (3, 5)
    equation = _check_line(plane, A, B)
    for t in (-2, Fraction(1, 2), 4):                  # A + t (B − A): on the line
        point = (A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1]))
        assert _on_line(equation, point), f"expected {point} (on the line through {A} and {B}) to satisfy {equation}"
    assert not _on_line(equation, (2, 3)), f"expected (2, 3), not on the line, to fail {equation}"


def test_line_through_with_ints_returns_ints(plane):
    equation = _check_line(plane, (2, 7), (-1, 1))
    assert all(isinstance(x, int) and not isinstance(x, bool) for x in equation), (
        f"expected ints when the coordinates are ints (as the docstring says), got {equation!r}")


def test_line_through_random_points_exactly(plane):
    rng = random.Random(41)
    for _ in range(25):
        A = (rng.randint(-9, 9), rng.randint(-9, 9))
        B = (rng.randint(-9, 9), rng.randint(-9, 9))
        if A != B:
            _check_line(plane, A, B)


@pytest.mark.parametrize("A", [(2, 3), (0, 0)], ids=["(2, 3) twice", "(0, 0) twice"])
def test_line_through_refuses_twice_the_same_point(plane, A):
    _expect_value_error(lambda: plane.line_through(A, A), f"line_through({A}, {A})",
                        "two distinct points are needed: every line goes through a single point")


# ---------------------------------------------------------------- deg_to_rad
def test_deg_to_rad_docstring_example(plane):
    got = _result(lambda: plane.deg_to_rad(180), "math.pi")
    assert got == math.pi, f"expected deg_to_rad(180) == math.pi (180 degrees are π radians), got {got!r}"


@pytest.mark.parametrize("degrees", [0, 90, 45, -30, 360, 57.29577951308232, 1000],
                         ids=["0", "90", "45", "-30", "360", "one radian", "1000"])
def test_deg_to_rad_matches_math_radians(plane, degrees):
    expected = math.radians(degrees)
    got = _result(lambda: plane.deg_to_rad(degrees), f"{expected} (math.radians)")
    assert got == pytest.approx(expected), (
        f"expected deg_to_rad({degrees}) ≈ {expected} (math.radians: multiply by π/180), got {got!r}")
