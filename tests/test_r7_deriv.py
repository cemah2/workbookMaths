"""Tests of mymath.deriv (chapter R7): rate of change, tangent line, bisection.

Oracles: exact rates of change of affine and quadratic functions, derivatives computed by ``sympy.diff``, and roots
given by ``scipy.optimize.brentq`` or known exactly (√2, ln 3). They describe the expected behaviour without showing
the solution.

    pytest tests/test_r7_deriv.py              # your code
    pytest tests/test_r7_deriv.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import random

import pytest
import sympy as sp
from scipy.optimize import brentq


@pytest.fixture
def deriv(mymath_module):
    return mymath_module("deriv")


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


X = sp.symbols("x")


def _sympy_derivative(expression, point):
    """The exact derivative of ``expression`` (in x) at ``point``, as a float: the oracle of the derivatives."""
    return float(sp.diff(expression, X).subs(X, point))


def test_deriv_uses_only_python_and_math(deriv):
    """Part 0 convention: plain Python and the math module (no NumPy, SciPy or SymPy solver in deriv.py)."""
    try:
        tree = ast.parse(inspect.getsource(deriv))
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
        f"expected deriv.py to import only math (plain Python, the convention of part 0), not "
        f"{', '.join(forbidden)}: write the rate of change, the tangent and the bisection yourself")


# ---------------------------------------------------------------- difference_quotient
def test_difference_quotient_docstring_example(deriv):
    got = _result(lambda: deriv.difference_quotient(lambda x: x * x, 3, 1), "7.0 (the docstring example)")
    assert got == pytest.approx(7.0), f"expected difference_quotient(x², 3, 1) == 7.0 ((16 − 9) / 1), got {got!r}"


AFFINE = [(0, 1), (2, 0.5), (-3, -2), (10, 1e-4)]


@pytest.mark.parametrize("a, h", AFFINE, ids=[f"a={a},h={h}" for a, h in AFFINE])
def test_difference_quotient_of_an_affine_function_is_its_slope(deriv, a, h):
    got = _result(lambda: deriv.difference_quotient(lambda x: 3 * x + 7, a, h), "3, the slope of 3x + 7")
    assert got == pytest.approx(3, rel=1e-9), (
        f"expected 3 (the slope of 3x + 7, whatever a and h), got difference_quotient(3x + 7, {a}, {h}) = {got!r}")


@pytest.mark.parametrize("a, h", [(1, 0.5), (4, -1), (-2, 0.25), (0.5, -0.125)],
                         ids=["h>0", "h<0", "a<0", "small negative h"])
def test_difference_quotient_of_x_squared_is_2a_plus_h(deriv, a, h):
    got = _result(lambda: deriv.difference_quotient(lambda x: x * x, a, h), f"2a + h = {2 * a + h}")
    assert got == pytest.approx(2 * a + h, rel=1e-12), (
        f"expected difference_quotient(x², {a}, {h}) == 2a + h = {2 * a + h} (((a + h)² − a²) / h, h of either "
        f"sign), got {got!r}")


def test_difference_quotient_returns_a_float(deriv):
    got = _result(lambda: deriv.difference_quotient(lambda x: x * x, 3, 1), "a float")
    assert isinstance(got, float), f"expected a float (7.0, the docstring example), got {type(got).__name__} {got!r}"


SMOOTH = [(sp.exp(X), math.exp, 0.5, "exp"), (sp.sqrt(X), math.sqrt, 4, "sqrt"), (sp.log(X), math.log, 2, "ln"),
          (X**3 - 2 * X, lambda x: x**3 - 2 * x, -1, "x³ − 2x")]


@pytest.mark.parametrize("expression, f, a, name", SMOOTH, ids=[s[3] for s in SMOOTH])
def test_difference_quotient_approaches_the_derivative(deriv, expression, f, a, name):
    exact = _sympy_derivative(expression, a)
    got = _result(lambda: deriv.difference_quotient(f, a, 1e-6), f"≈ {exact} (the derivative of {name} at {a})")
    assert got == pytest.approx(exact, abs=1e-4), (
        f"expected difference_quotient({name}, {a}, 1e-6) ≈ {exact}, the derivative at {a} (SymPy), got {got!r}")


@pytest.mark.parametrize("h", [0, 0.0], ids=["int zero", "float zero"])
def test_difference_quotient_refuses_a_zero_step(deriv, h):
    _expect_value_error(lambda: deriv.difference_quotient(lambda x: x * x, 3, h), f"difference_quotient(x², 3, {h!r})",
                        "the rate of change divides by h")


# ---------------------------------------------------------------- tangent_line
def test_tangent_line_docstring_example(deriv):
    got = _result(lambda: deriv.tangent_line(lambda x: x * x, lambda x: 2 * x, 3), "(6, -9)")
    assert tuple(got) == (6, -9), f"expected (6, -9) (y = 6x − 9, the tangent of x² at 3), got {got!r}"


def test_tangent_line_gives_ints_for_ints(deriv):
    got = _result(lambda: deriv.tangent_line(lambda x: x * x, lambda x: 2 * x, 3), "(6, -9), two ints")
    assert all(isinstance(v, int) and not isinstance(v, bool) for v in got), (
        f"expected two ints (f, df and a give ints: no float() and no division), got {got!r}")


def test_tangent_line_of_exp_at_0(deriv):
    got = _result(lambda: deriv.tangent_line(math.exp, math.exp, 0), "(1.0, 1.0): y = x + 1")
    assert len(got) == 2 and got[0] == pytest.approx(1.0) and got[1] == pytest.approx(1.0), (
        f"expected (1.0, 1.0) (y = x + 1, the tangent of exp at 0), got {got!r}")


def test_tangent_line_of_ln_at_1(deriv):
    got = _result(lambda: deriv.tangent_line(math.log, lambda x: 1 / x, 1), "(1.0, -1.0): y = x − 1")
    assert got[0] == pytest.approx(1.0) and got[1] == pytest.approx(-1.0), (
        f"expected (1.0, -1.0) (y = x − 1, the tangent of ln at 1), got {got!r}")


def test_tangent_line_touches_the_curve_with_the_right_slope(deriv):
    rng = random.Random(71)
    for _ in range(30):
        c3, c2, c1, c0 = (rng.randint(-5, 5) for _ in range(4))
        expression = c3 * X**3 + c2 * X**2 + c1 * X + c0
        f = sp.lambdify(X, expression)
        df = sp.lambdify(X, sp.diff(expression, X))
        a = round(rng.uniform(-3, 3), 3)
        got = _result(lambda: deriv.tangent_line(f, df, a), f"the tangent of {expression} at {a}")
        m, c = got
        exact_slope = _sympy_derivative(expression, a)
        assert m == pytest.approx(exact_slope, rel=1e-9, abs=1e-9), (
            f"expected the slope m = f'({a}) = {exact_slope} for f(x) = {expression}, got m = {m!r}")
        assert m * a + c == pytest.approx(f(a), rel=1e-9, abs=1e-9), (
            f"expected the tangent to pass through (a, f(a)) = ({a}, {f(a)}) for f(x) = {expression}: "
            f"m*a + c == f(a), got m*a + c = {m * a + c!r} (c = {c!r})")


# ---------------------------------------------------------------- bisection
def test_bisection_docstring_example(deriv):
    got = _result(lambda: deriv.bisection(lambda x: x * x - 2, 0, 2), "√2 ≈ 1.41421356")
    assert got == pytest.approx(math.sqrt(2), abs=1e-9), f"expected √2 ≈ {math.sqrt(2)} (zero of x² − 2), got {got!r}"


ROOTS = [(lambda x: x**3 + x - 1, 0, 1, "x³ + x − 1"), (lambda x: math.exp(x) - 3, 0, 2, "eˣ − 3"),
         (lambda x: 2 - x, 0, 5, "2 − x (decreasing)"), (lambda x: math.log(x) + x, 0.1, 1, "ln x + x")]


@pytest.mark.parametrize("f, a, b, name", ROOTS, ids=[r[3] for r in ROOTS])
def test_bisection_finds_the_zero(deriv, f, a, b, name):
    exact = brentq(f, a, b, xtol=1e-14)
    got = _result(lambda: deriv.bisection(f, a, b), f"≈ {exact} (the zero of {name} on [{a}, {b}])")
    assert got == pytest.approx(exact, abs=1e-9), (
        f"expected ≈ {exact} (the zero of {name} on [{a}, {b}], from scipy.optimize.brentq), got {got!r}")


@pytest.mark.parametrize("tol", [1e-3, 1e-6, 1e-12], ids=["1e-3", "1e-6", "1e-12"])
def test_bisection_respects_the_tolerance(deriv, tol):
    exact = math.log(3)
    got = _result(lambda: deriv.bisection(lambda x: math.exp(x) - 3, 0, 2, tol=tol), f"within {tol} of ln 3")
    assert abs(got - exact) <= tol, (
        f"expected a result within tol = {tol} of ln 3 = {exact} (zero of eˣ − 3), got {got!r} "
        f"(off by {abs(got - exact):.3g})")


ENDS = [(lambda x: x - 1, 1, 3, 1, "zero at a"), (lambda x: x - 3, 1, 3, 3, "zero at b"),
        (lambda x: x, -1, 1, 0, "zero at the first middle")]


@pytest.mark.parametrize("f, a, b, zero, why", ENDS, ids=[e[4] for e in ENDS])
def test_bisection_returns_an_exact_zero(deriv, f, a, b, zero, why):
    got = _result(lambda: deriv.bisection(f, a, b), f"{zero} ({why})")
    assert got == pytest.approx(zero, abs=1e-12), (
        f"expected {zero} ({why}: f is exactly 0 there, no sign change is needed), got {got!r}")


def test_bisection_stops_after_max_iter_halvings(deriv):
    got = _result(lambda: deriv.bisection(lambda x: x**3 + x - 1, 0, 1, max_iter=3),
                  "0.6875, the middle of [0.625, 0.75] after 3 halvings")
    assert got == pytest.approx(0.6875), (
        f"expected 0.6875 (after 3 halvings of [0, 1] for x³ + x − 1: [0.5, 1], [0.5, 0.75], [0.625, 0.75], whose "
        f"middle is 0.6875), got {got!r}")


def test_bisection_with_a_zero_tolerance_still_stops(deriv):
    got = _result(lambda: deriv.bisection(lambda x: x * x - 2, 0, 2, tol=0, max_iter=60), "≈ √2, after 60 halvings")
    assert got == pytest.approx(math.sqrt(2), abs=1e-9), (
        f"expected ≈ √2 (tol = 0 can never be reached: max_iter = 60 must stop the loop), got {got!r}")


BAD = [(lambda x: x * x + 1, -1, 1, "f(a) and f(b) have the same sign (x² + 1 > 0)"),
       (lambda x: x - 5, 0, 1, "f(a) and f(b) are both negative"),
       (lambda x: x, 1, -1, "a > b"), (lambda x: x, 2, 2, "a == b")]


@pytest.mark.parametrize("f, a, b, why", BAD, ids=["same sign positive", "same sign negative", "a > b", "a == b"])
def test_bisection_refuses_a_bad_interval(deriv, f, a, b, why):
    _expect_value_error(lambda: deriv.bisection(f, a, b), f"bisection on [{a}, {b}]", why)
