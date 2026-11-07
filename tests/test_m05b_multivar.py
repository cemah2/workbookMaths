"""Tests of mymath.multivar (chapter M05b): partial and directional derivatives, steepest ascent, tangent plane.

Oracles: SymPy (exact partial derivatives and gradients) and exact formulas. They describe the expected behaviour
without showing the solution.

    pytest tests/test_m05b_multivar.py              # your code
    pytest tests/test_m05b_multivar.py --impl=ref   # the reference
"""

import ast
import inspect
import math

import numpy as np
import pytest
import sympy as sp


@pytest.fixture
def multivar(mymath_module):
    return mymath_module("multivar")


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    try:
        return call()
    except NotImplementedError:
        raise                 # a function not written yet: ⏳
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised {type(exc).__name__}: {exc}"
                    + (f" ({hint})" if hint else ""))


def _expect_error(error, call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ``error``."""
    try:
        result = call()
    except NotImplementedError:
        raise                 # first: a function not written yet stays ⏳
    except error:
        return
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise {error.__name__} ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise {error.__name__} ({why}), but it returned {result!r}")


def _python_float(got, what):
    assert type(got) is float, (f"expected {what} to be a Python float (float(...)), got "
                                f"{type(got).__module__}.{type(got).__name__}")


# ---------------------------------------------------------------- SymPy oracle
X, Y, Z = sp.symbols("x y z")


def _numeric(expr, symbols):
    """A function of one NumPy array p, as the module docstring asks, built from a SymPy expression."""
    fn = sp.lambdify(symbols, expr, "math")
    return lambda p: fn(*[float(v) for v in p])


def _exact_gradient(expr, symbols, point):
    values = dict(zip(symbols, point))
    return np.array([float(sp.diff(expr, s).subs(values)) for s in symbols])


CASES = [   # (name, expression, symbols, point)
    ("x²y³ − sin(xy)", X ** 2 * Y ** 3 - sp.sin(X * Y), (X, Y), (0.7, -1.2)),
    ("ln(1 + x² + 3y²)", sp.log(1 + X ** 2 + 3 * Y ** 2), (X, Y), (1.5, 0.5)),
    ("z e^(x − 2y)", Z * sp.exp(X - 2 * Y), (X, Y, Z), (0.3, 0.1, 2.0)),
    ("√(1 + x² y) cos z", sp.sqrt(1 + X ** 2 * Y) * sp.cos(Z), (X, Y, Z), (-0.8, 2.5, 0.6)),
]
IDS = ["x2y3-sin", "log", "zexp-3d", "sqrtcos-3d"]


# ---------------------------------------------------------------- no ready-made tool
def test_multivar_uses_no_ready_made_tool(multivar):
    """multivar.py computes its derivatives itself: neither SymPy nor numpy.gradient."""
    try:
        tree = ast.parse(inspect.getsource(multivar))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names if alias.name.split(".")[0] == "sympy")
        elif isinstance(node, ast.ImportFrom) and node.module and node.module.split(".")[0] == "sympy":
            found.add(node.module)
        elif isinstance(node, ast.Attribute) and node.attr == "gradient":
            found.add("numpy.gradient")
    assert not found, (
        f"expected multivar.py to use neither SymPy nor numpy.gradient (the tests compare your results with them), "
        f"found {sorted(found)}: compute each derivative by a centred difference")


# ---------------------------------------------------------------- partial_derivative
def test_partial_derivative_docstring_example(multivar):
    got = _result(lambda: multivar.partial_derivative(lambda p: p[0] ** 2 * p[1], (1.0, 3.0), 0), "about 6.0")
    assert got == pytest.approx(6.0, rel=1e-8), f"expected 6.0 (∂(x²y)/∂x = 2xy at (1, 3)), got {got!r}"


@pytest.mark.parametrize("name, expr, symbols, point", CASES, ids=IDS)
def test_partial_derivative_matches_sympy(multivar, name, expr, symbols, point):
    f = _numeric(expr, symbols)
    exact = _exact_gradient(expr, symbols, point)
    for i in range(len(symbols)):
        got = _result(lambda: multivar.partial_derivative(f, point, i), f"about {exact[i]:.8g}",
                      f"∂f/∂{symbols[i]} of {name} at {point}")
        assert got == pytest.approx(exact[i], rel=1e-7, abs=1e-8), (
            f"expected {exact[i]:.10g} for ∂f/∂{symbols[i]} of {name} at {point} (SymPy), got {got!r}: move only "
            f"coordinate i = {i}, by +h and by -h, and divide by 2h")


def test_partial_derivative_moves_only_coordinate_i(multivar):
    point = (0.4, -1.1, 2.3)
    seen = []

    def f(p):
        seen.append(np.array(p, dtype=float))
        return p[0] * p[1] + p[2] ** 2

    _result(lambda: multivar.partial_derivative(f, point, 1), "a number", "∂f/∂y at (0.4, -1.1, 2.3)")
    assert seen, "expected f to be called, but it never was"
    for q in seen:
        moved = [k for k in range(3) if q[k] != point[k]]
        assert moved in ([], [1]), (f"expected only coordinate 1 to move for ∂f/∂y, but f was called at {q.tolist()}: "
                                    f"coordinates {moved} differ from the point {list(point)}")


def test_partial_derivative_with_an_integer_point(multivar):
    point = np.array([3, 2])                       # integers: h added in place would be lost
    got = _result(lambda: multivar.partial_derivative(lambda p: p[0] ** 2 * p[1], point, 0), "about 12.0",
                  "an integer point np.array([3, 2])")
    assert got == pytest.approx(12.0, rel=1e-8), (
        f"expected 12.0 (2xy at (3, 2)), got {got!r}: copy the point into a float array, np.array(point, dtype=float)")


def test_partial_derivative_leaves_the_point_unchanged(multivar):
    point = np.array([0.25, -0.75])
    keep = point.copy()
    _result(lambda: multivar.partial_derivative(lambda p: p[0] * p[1], point, 1), "a number", "∂(xy)/∂y")
    assert np.array_equal(point, keep), (f"expected the caller's point to stay {keep.tolist()}, but it became "
                                         f"{point.tolist()}: work on a copy")


@pytest.mark.parametrize("i", [2, -1], ids=["i=2", "i=-1"])
def test_partial_derivative_refuses_an_index_out_of_range(multivar, i):
    _expect_error(ValueError, lambda: multivar.partial_derivative(lambda p: p[0] + p[1], (1.0, 2.0), i),
                  f"partial_derivative(f, (1.0, 2.0), {i})", "a point of two coordinates has the indices 0 and 1")


@pytest.mark.parametrize("h", [0.0, -1e-3], ids=["h=0", "h<0"])
def test_partial_derivative_refuses_a_step_that_is_not_positive(multivar, h):
    _expect_error(ValueError, lambda: multivar.partial_derivative(lambda p: p[0] * p[1], (1.0, 2.0), 0, h),
                  f"partial_derivative(..., h={h})", "the step must be positive")


def test_partial_derivative_returns_a_python_float(multivar):
    got = _result(lambda: multivar.partial_derivative(lambda p: np.sin(p[0]) * p[1], np.array([0.5, 2.0]), 0),
                  "a float")
    _python_float(got, "partial_derivative(...)")


# ---------------------------------------------------------------- directional_derivative
def test_directional_derivative_docstring_example(multivar):
    got = _result(lambda: multivar.directional_derivative(lambda p: p[0] + 2 * p[1], (0.0, 0.0), (3, 4)),
                  "about 2.2")
    assert got == pytest.approx(2.2, rel=1e-8), (f"expected 2.2 ((1, 2) · (3, 4)/5), got {got!r}: normalise the "
                                                 "direction first")


@pytest.mark.parametrize("name, expr, symbols, point", CASES, ids=IDS)
def test_directional_derivative_matches_sympy(multivar, name, expr, symbols, point):
    f = _numeric(expr, symbols)
    direction = np.array([2.0, -1.0, 0.5][:len(symbols)])
    exact = float(_exact_gradient(expr, symbols, point) @ (direction / np.linalg.norm(direction)))
    got = _result(lambda: multivar.directional_derivative(f, point, direction), f"about {exact:.8g}",
                  f"{name} at {point}, direction {direction.tolist()}")
    assert got == pytest.approx(exact, rel=1e-7, abs=1e-8), (
        f"expected {exact:.10g} (∇f · u with u = direction / ||direction||, SymPy) for {name} at {point}, got "
        f"{got!r}")


def test_directional_derivative_does_not_depend_on_the_length_of_the_direction(multivar):
    f = _numeric(X ** 3 * Y - Y ** 2, (X, Y))
    exact = float(_exact_gradient(X ** 3 * Y - Y ** 2, (X, Y), (1.2, 0.4)) @ (np.array([1.0, 3.0]) / math.sqrt(10)))
    for scale in (0.01, 1.0, 50.0):
        got = _result(lambda: multivar.directional_derivative(f, (1.2, 0.4), (scale, 3 * scale)),
                      f"about {exact:.8g}", f"direction ({scale}, {3 * scale})")
        assert got == pytest.approx(exact, rel=1e-6), (
            f"expected {exact:.8g} whatever the length of the direction (here ({scale}, {3 * scale})), got {got!r}: "
            "divide the direction by its norm")


def test_directional_derivative_is_zero_along_a_level_line(multivar):
    f = lambda p: p[0] ** 2 + 4 * p[1] ** 2       # noqa: E731 - gradient (4, 8) at (2, 1)
    got = _result(lambda: multivar.directional_derivative(f, (2.0, 1.0), (2.0, -1.0)), "about 0",
                  "x² + 4y² at (2, 1), along the level line")
    assert abs(got) < 1e-6, (f"expected 0 (the direction (2, -1) is orthogonal to the gradient (4, 8): f does not "
                             f"change along it), got {got!r}")


def test_directional_derivative_changes_sign_with_the_direction(multivar):
    f = lambda p: math.exp(p[0]) * p[1]           # noqa: E731
    up = _result(lambda: multivar.directional_derivative(f, (0.0, 2.0), (1.0, 1.0)), "a number")
    down = _result(lambda: multivar.directional_derivative(f, (0.0, 2.0), (-1.0, -1.0)), "a number")
    assert down == pytest.approx(-up, rel=1e-8), (f"expected opposite directions to give opposite slopes, got {up!r} "
                                                  f"and {down!r}")


@pytest.mark.parametrize("direction, why", [((0.0, 0.0), "the zero vector gives no direction"),
                                             ((1.0, 2.0, 3.0), "the direction must have as many coordinates as "
                                                               "the point")],
                         ids=["zero", "length"])
def test_directional_derivative_refuses_a_bad_direction(multivar, direction, why):
    _expect_error(ValueError, lambda: multivar.directional_derivative(lambda p: p[0] * p[1], (1.0, 2.0), direction),
                  f"directional_derivative(f, (1.0, 2.0), {direction})", why)


def test_directional_derivative_refuses_a_step_that_is_not_positive(multivar):
    _expect_error(ValueError, lambda: multivar.directional_derivative(lambda p: p[0], (1.0, 2.0), (1.0, 0.0), -0.1),
                  "directional_derivative(..., h=-0.1)", "the step must be positive")


def test_directional_derivative_returns_a_python_float(multivar):
    got = _result(lambda: multivar.directional_derivative(lambda p: np.cos(p[0] * p[1]), np.array([1.0, 0.5]),
                                                          np.array([1, 2])), "a float")
    _python_float(got, "directional_derivative(...)")


# ---------------------------------------------------------------- steepest_ascent_direction
def test_steepest_ascent_direction_docstring_example(multivar):
    got = _result(lambda: multivar.steepest_ascent_direction(lambda p: 3 * p[0] + 4 * p[1], (0.0, 0.0)),
                  "[0.6, 0.8]")
    assert np.allclose(got, [0.6, 0.8], atol=1e-8), f"expected [0.6, 0.8] ((3, 4)/5), got {got!r}"


@pytest.mark.parametrize("name, expr, symbols, point", CASES, ids=IDS)
def test_steepest_ascent_direction_matches_sympy(multivar, name, expr, symbols, point):
    exact = _exact_gradient(expr, symbols, point)
    exact = exact / np.linalg.norm(exact)
    got = _result(lambda: multivar.steepest_ascent_direction(_numeric(expr, symbols), point),
                  f"{np.round(exact, 6).tolist()}", f"{name} at {point}")
    got = np.asarray(got, dtype=float)
    assert got.shape == exact.shape and np.allclose(got, exact, atol=1e-7), (
        f"expected {np.round(exact, 8).tolist()} (∇f / ||∇f||, SymPy) for {name} at {point}, got {got.tolist()}")


def test_steepest_ascent_direction_is_a_unit_numpy_vector(multivar):
    got = _result(lambda: multivar.steepest_ascent_direction(lambda p: p[0] ** 2 - 5 * p[1] + p[2], (4.0, 1.0, 2.0)),
                  "a unit vector of length 3")
    assert isinstance(got, np.ndarray), f"expected a numpy.ndarray, got {type(got).__name__}: return np.array(...)"
    assert got.shape == (3,), f"expected the shape (3,), as the point, got {got.shape}"
    assert math.isclose(float(np.linalg.norm(got)), 1.0, rel_tol=1e-9), (
        f"expected a vector of norm 1, got norm {float(np.linalg.norm(got))!r}: divide the gradient by its norm")


def test_steepest_ascent_direction_refuses_a_critical_point(multivar):
    f = lambda p: (p[0] - 1) ** 2 + (p[1] + 2) ** 2     # noqa: E731 - minimum at (1, -2)
    _expect_error(ValueError, lambda: multivar.steepest_ascent_direction(f, (1.0, -2.0)),
                  "steepest_ascent_direction at a minimum", "the gradient is zero: there is no direction of ascent")


def test_steepest_ascent_direction_refuses_a_step_that_is_not_positive(multivar):
    _expect_error(ValueError, lambda: multivar.steepest_ascent_direction(lambda p: p[0] + p[1], (0.0, 0.0), 0.0),
                  "steepest_ascent_direction(..., h=0.0)", "the step must be positive")


def test_steepest_ascent_direction_leaves_the_point_unchanged(multivar):
    point = np.array([1.5, -0.5])
    keep = point.copy()
    _result(lambda: multivar.steepest_ascent_direction(lambda p: p[0] ** 2 + p[0] * p[1], point), "a vector")
    assert np.array_equal(point, keep), (f"expected the caller's point to stay {keep.tolist()}, but it became "
                                         f"{point.tolist()}: work on a copy")


# ---------------------------------------------------------------- tangent_plane
def test_tangent_plane_docstring_example(multivar):
    got = _result(lambda: multivar.tangent_plane(lambda p: p[0] ** 2 + p[1] ** 2, (1.0, 2.0)), "(2.0, 4.0, -5.0)")
    assert np.allclose(got, (2.0, 4.0, -5.0), atol=1e-7), f"expected (2.0, 4.0, -5.0), got {got!r}"


@pytest.mark.parametrize("expr, point", [(X * sp.exp(Y) + Y ** 2, (1.5, -0.5)),
                                         (sp.atan(X / (1 + Y ** 2)), (-2.0, 0.7)),
                                         (X ** 3 - 2 * X * Y + Y ** 4, (0.6, -1.3))],
                         ids=["xexp", "atan", "poly"])
def test_tangent_plane_matches_sympy(multivar, expr, point):
    a, b = _exact_gradient(expr, (X, Y), point)
    c = float(expr.subs({X: point[0], Y: point[1]})) - a * point[0] - b * point[1]
    got = _result(lambda: multivar.tangent_plane(_numeric(expr, (X, Y)), point),
                  f"({a:.6g}, {b:.6g}, {c:.6g})", f"z = {expr} at {point}")
    assert len(got) == 3 and np.allclose(got, (a, b, c), rtol=1e-7, atol=1e-7), (
        f"expected ({a:.8g}, {b:.8g}, {c:.8g}) for z = {expr} at {point} (a and b the partial derivatives, c so that "
        f"the plane goes through the point), got {tuple(got)!r}")


def test_tangent_plane_of_a_plane_is_the_plane_itself(multivar):
    got = _result(lambda: multivar.tangent_plane(lambda p: 2 * p[0] - 3 * p[1] + 7, (5.0, -4.0)), "(2.0, -3.0, 7.0)")
    assert np.allclose(got, (2.0, -3.0, 7.0), atol=1e-6), (
        f"expected (2.0, -3.0, 7.0) (the surface z = 2x − 3y + 7 is its own tangent plane), got {tuple(got)!r}: "
        "c = f(x0, y0) − a x0 − b y0")


@pytest.mark.parametrize("point", [(1.0, 2.0, 3.0), (1.0,)], ids=["3-coordinates", "1-coordinate"])
def test_tangent_plane_refuses_a_point_without_two_coordinates(multivar, point):
    _expect_error(ValueError, lambda: multivar.tangent_plane(lambda p: float(np.sum(p)), point),
                  f"tangent_plane(f, {point})", "the tangent plane is for a surface z = f(x, y), two variables")


def test_tangent_plane_refuses_a_step_that_is_not_positive(multivar):
    _expect_error(ValueError, lambda: multivar.tangent_plane(lambda p: p[0] * p[1], (1.0, 2.0), -1e-4),
                  "tangent_plane(..., h=-1e-4)", "the step must be positive")


def test_tangent_plane_returns_three_python_floats(multivar):
    got = _result(lambda: multivar.tangent_plane(lambda p: np.sin(p[0]) + p[1] ** 2, np.array([1, 3])),
                  "three floats")
    assert isinstance(got, tuple) and len(got) == 3, f"expected a tuple (a, b, c), got {got!r}"
    for name, value in zip("abc", got):
        _python_float(value, f"{name} of tangent_plane(...)")
