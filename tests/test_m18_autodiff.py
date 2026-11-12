"""Tests of mymath.autodiff (chapter M18): dual numbers (forward-mode automatic differentiation), the derivative of a
function of one variable, the gradient by one forward pass per coordinate, and the gradient of a function of a matrix
read in its differential.

Oracles: SymPy (the algebra of ``a + b ε`` with ``ε² = 0``, computed as a series in ``ε`` cut after the term in ``ε``;
exact derivatives and gradients evaluated at the point), linear forms whose coefficients are known, and properties
(one evaluation of ``f`` per pass, the seeds of each pass, the moves ``E_ij`` given to the differential, exact results
on polynomials with binary numbers). They describe the expected behaviour without showing the solution.

    pytest tests/test_m18_autodiff.py              # your code
    pytest tests/test_m18_autodiff.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings

import numpy as np
import pytest
import sympy


@pytest.fixture
def ad(mymath_module):
    return mymath_module("autodiff")


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)
        try:
            return call()
        except NotImplementedError:
            raise                 # a function not written yet: ⏳
        except RuntimeWarning as warning:
            pytest.fail(f"expected {expected}{' for ' + what if what else ''} without a RuntimeWarning, got "
                        f"RuntimeWarning: {warning}" + (f" ({hint})" if hint else ""))
        except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
            pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised "
                        f"{type(exc).__name__}: {exc}" + (f" ({hint})" if hint else ""))


def _expect_error(error, call, what, why):
    """Fail with what was expected first, whatever the code did instead of raising `error` itself."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        try:
            result = call()
        except NotImplementedError:
            raise                 # a function not written yet stays ⏳
        except error as exc:
            return exc
        except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
            pytest.fail(f"expected {what} to raise {error.__name__} ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise {error.__name__} ({why}), but it returned {result!r}")


def _show(v):
    return np.array2string(np.asarray(v, dtype=float), precision=6, suppress_small=True).replace("\n", "")


def _float_array(got, shape, what):
    assert isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape, (
        f"expected {what} as a numpy.ndarray of floats of shape {shape}, got {type(got).__name__}"
        + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray) else ""))


def _close(got, want, what, atol=1e-9, hint=""):
    got = np.asarray(got, dtype=float)
    assert got.shape == np.shape(want) and np.allclose(got, want, rtol=1e-9, atol=atol), (
        f"expected {what} = {_show(want)}, got {_show(got)}" + (f" ({hint})" if hint else ""))


def _dual_parts(ad, got, want, what, hint=""):
    """Check that got is a Dual with value want[0] and derivative want[1] (relative tolerance 1e-9)."""
    assert isinstance(got, ad.Dual), (f"expected {what} to be a new Dual, got {type(got).__name__} {got!r}"
                                      + (f" ({hint})" if hint else ""))
    ok = all(math.isclose(g, w, rel_tol=1e-9, abs_tol=1e-12)
             for g, w in ((got.value, want[0]), (got.derivative, want[1])))
    assert ok, (f"expected {what} = Dual(value={want[0]:.10g}, derivative={want[1]:.10g}), got "
                f"Dual(value={got.value:.10g}, derivative={got.derivative:.10g})" + (f" ({hint})" if hint else ""))


# --- the oracle: a + b ε with ε² = 0, by SymPy -------------------------------------------------------------------

EPS = sympy.Symbol("eps")


def _eps(a, b):
    """The SymPy number a + b ε (a, b exact rationals of the floats)."""
    return sympy.Rational(a) + sympy.Rational(b) * EPS


def _parts(expr):
    """(value, derivative) of a SymPy expression in ε: its series in ε, cut after the term in ε."""
    s = sympy.series(expr, EPS, 0, 2).removeO()
    return float(s.coeff(EPS, 0)), float(s.coeff(EPS, 1))


PAIRS = [((3.0, 1.0), (-2.0, 0.5)), ((-1.25, 4.0), (0.75, -2.0)), ((0.5, -3.0), (2.5, 1.5)), ((7.0, 0.0), (-0.25, 6.0))]

OPERATIONS = [("+", lambda u, w: u + w, "__add__", "values and derivatives add up"),
              ("-", lambda u, w: u - w, "__sub__", "values and derivatives subtract"),
              ("*", lambda u, w: u * w, "__mul__", "(a + b ε)(c + d ε) = a c + (a d + b c) ε: the product rule"),
              ("/", lambda u, w: u / w, "__truediv__", "a / c + (b c - a d) / c² ε: the quotient rule")]


# --- what the module may use ------------------------------------------------------------------------------------

def test_module_uses_no_symbolic_or_autodiff_library(ad):
    """The docstring allows math and NumPy only: the tests compare the results with SymPy."""
    try:
        tree = ast.parse(inspect.getsource(ad))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names] + ([node.module] if isinstance(node, ast.ImportFrom) else [])
            found |= {n.split(".")[0] for n in names
                      if n and n.split(".")[0] in ("sympy", "jax", "torch", "autograd", "tensorflow")}
    assert not found, (f"expected the module to differentiate by itself with dual numbers, found an import of "
                       f"{sorted(found)} (the tests compare your results with SymPy)")


# --- Dual: the four operations --------------------------------------------------------------------------------

def test_dual_docstring_examples(ad):
    x = ad.Dual(3.0, 1.0)
    got = _result(lambda: (x + 1) / (x - 1), "Dual(value=2.0, derivative=-0.5)", "(x + 1) / (x - 1) at x = 3")
    _dual_parts(ad, got, (2.0, -0.5), "(x + 1) / (x - 1) for x = Dual(3.0, 1.0)")
    got = _result(lambda: 2 * x ** 2, "Dual(value=18.0, derivative=12.0)", "2 x² at x = 3")
    _dual_parts(ad, got, (18.0, 12.0), "2 * x ** 2 for x = Dual(3.0, 1.0)")
    for method, a, b, want in (("exp", 0.0, 1.0, (1.0, 1.0)), ("exp", 0.0, 2.0, (1.0, 2.0)),
                               ("log", 1.0, 3.0, (0.0, 3.0)), ("sin", 0.0, 1.0, (0.0, 1.0)),
                               ("cos", 0.0, 1.0, (1.0, 0.0))):
        got = _result(lambda: getattr(ad.Dual(a, b), method)(), f"Dual{want}", f"Dual({a}, {b}).{method}()")
        _dual_parts(ad, got, want, f"Dual({a}, {b}).{method}()")


@pytest.mark.parametrize("symbol, op, method, rule", OPERATIONS, ids=["add", "sub", "mul", "div"])
def test_dual_operation_follows_the_algebra_of_epsilon(ad, symbol, op, method, rule):
    for (a, b), (c, d) in PAIRS:
        want = _parts(op(_eps(a, b), _eps(c, d)))
        u, w = ad.Dual(a, b), ad.Dual(c, d)
        got = _result(lambda: op(u, w), f"Dual{want}", f"({a} + {b} ε) {symbol} ({c} + {d} ε)", method)
        _dual_parts(ad, got, want, f"Dual({a}, {b}) {symbol} Dual({c}, {d}), ε² = 0", rule)


@pytest.mark.parametrize("symbol, op, method, rule", OPERATIONS, ids=["add", "sub", "mul", "div"])
def test_dual_operation_with_a_plain_number_on_each_side(ad, symbol, op, method, rule):
    """A plain number k counts as Dual(k, 0.0): u op k needs __add__ and the like, k op u needs __radd__ and the like."""
    for (a, b), k in (((2.5, 1.0), 4), ((-3.0, 0.5), -1.5), ((0.75, -2.0), 2.0)):
        u = ad.Dual(a, b)
        want = _parts(op(_eps(a, b), sympy.Rational(k)))
        got = _result(lambda: op(u, k), f"Dual{want}", f"Dual({a}, {b}) {symbol} {k}", method)
        _dual_parts(ad, got, want, f"Dual({a}, {b}) {symbol} {k!r}", f"{method}: {k!r} counts as Dual({k!r}, 0.0)")
        right = "__r" + method[2:]
        want = _parts(op(sympy.Rational(k), _eps(a, b)))
        got = _result(lambda: op(k, u), f"Dual{want}", f"{k} {symbol} Dual({a}, {b})", right)
        _dual_parts(ad, got, want, f"{k!r} {symbol} Dual({a}, {b})",
                    f"{right}: Python calls it when the number on the left cannot handle a Dual")


def test_dual_negation(ad):
    for a, b in ((2.0, 3.0), (-0.5, -1.25), (0.0, 1.0)):
        got = _result(lambda: -ad.Dual(a, b), f"Dual({-a}, {-b})", f"-Dual({a}, {b})", "__neg__")
        _dual_parts(ad, got, (-a, -b), f"-Dual({a}, {b})", "both parts change sign")


def test_dual_operations_return_new_duals_and_leave_operands_alone(ad):
    u, w = ad.Dual(1.5, 2.0), ad.Dual(-0.5, 4.0)
    calls = [("u + w", lambda: u + w), ("u - w", lambda: u - w), ("u * w", lambda: u * w), ("u / w", lambda: u / w),
             ("u + 0", lambda: u + 0), ("0 + u", lambda: 0 + u), ("u * 1", lambda: u * 1), ("1 * u", lambda: 1 * u),
             ("u - 0", lambda: u - 0), ("u / 1", lambda: u / 1), ("-u", lambda: -u), ("u ** 1", lambda: u ** 1),
             ("u.exp()", lambda: u.exp()), ("u.log()", lambda: u.log()), ("u.sin()", lambda: u.sin()),
             ("u.cos()", lambda: u.cos())]
    for text, call in calls:
        got = _result(call, "a new Dual", text)
        assert isinstance(got, ad.Dual) and got is not u and got is not w, (
            f"expected {text} to return a new Dual, got {got!r}" + (" (the operand itself)" if got is u else ""))
        assert (u.value, u.derivative, w.value, w.derivative) == (1.5, 2.0, -0.5, 4.0), (
            f"expected {text} to leave its operands unchanged, but u = {u!r} and w = {w!r} afterwards "
            "(build a new Dual instead of changing self)")


def test_dual_division_by_zero_raises_zero_division_error(ad):
    for text, call in (("Dual(1, 1) / Dual(0, 1)", lambda: ad.Dual(1.0, 1.0) / ad.Dual(0.0, 1.0)),
                       ("Dual(2, 3) / 0", lambda: ad.Dual(2.0, 3.0) / 0),
                       ("3 / Dual(0, 2)", lambda: 3 / ad.Dual(0.0, 2.0))):
        _expect_error(ZeroDivisionError, call, text, "the value of the divisor is 0")


# --- Dual: powers and elementary functions -----------------------------------------------------------------------

@pytest.mark.parametrize("a, p", [(1.3, 2), (2.0, 3), (-1.5, 3), (-2.0, 2), (0.6, -1), (-0.5, -2), (4.0, 0.5),
                                  (3.24, 1.5), (3.0, -0.5), (1.2, 2.5)])
def test_dual_power_by_a_constant_matches_sympy(ad, a, p):
    b = 1.75
    want = _parts(_eps(a, b) ** sympy.nsimplify(p))
    got = _result(lambda: ad.Dual(a, b) ** p, f"Dual{want}", f"Dual({a}, {b}) ** {p}", "__pow__")
    _dual_parts(ad, got, want, f"Dual({a}, {b}) ** {p!r}", "(a + b ε)ᵖ = aᵖ + p aᵖ⁻¹ b ε")


def test_dual_power_zero_and_powers_at_zero(ad):
    for a in (0.0, -3.0, 2.5):
        got = _result(lambda: ad.Dual(a, 5.0) ** 0, "Dual(1.0, 0.0)", f"Dual({a}, 5.0) ** 0")
        _dual_parts(ad, got, (1.0, 0.0), f"Dual({a}, 5.0) ** 0", "u ** 0 is the constant 1, even for a = 0")
    for p, want in ((1, (0.0, 2.0)), (2, (0.0, 0.0)), (3, (0.0, 0.0)), (1.5, (0.0, 0.0))):
        got = _result(lambda: ad.Dual(0.0, 2.0) ** p, f"Dual{want}", f"Dual(0.0, 2.0) ** {p}")
        _dual_parts(ad, got, want, f"Dual(0.0, 2.0) ** {p!r}", "for p ≥ 1, t ** p has a derivative at 0")


def test_dual_power_refusals(ad):
    _expect_error(TypeError, lambda: ad.Dual(2.0, 1.0) ** ad.Dual(3.0, 0.0), "Dual(2, 1) ** Dual(3, 0)",
                  "the exponent must be a constant number, not a Dual")
    for a, p, why in ((-2.0, 0.5, "a negative number to a non-integer power"),
                      (-1.0, 1.5, "a negative number to a non-integer power"),
                      (0.0, 0.5, "the derivative of √t does not exist at 0"),
                      (0.0, -1, "1/t is not defined at 0")):
        _expect_error(ValueError, lambda: ad.Dual(a, 1.0) ** p, f"Dual({a}, 1.0) ** {p}", why)


@pytest.mark.parametrize("method, function", [("exp", sympy.exp), ("log", sympy.log), ("sin", sympy.sin),
                                              ("cos", sympy.cos)])
def test_dual_elementary_function_applies_the_chain_rule(ad, method, function):
    for a, b in ((0.3, 1.0), (1.7, -2.5), (2.9, 0.25), (0.05, 4.0)):
        want = _parts(function(_eps(a, b)))
        got = _result(lambda: getattr(ad.Dual(a, b), method)(), f"Dual{want}", f"Dual({a}, {b}).{method}()")
        _dual_parts(ad, got, want, f"Dual({a}, {b}).{method}()", "g(a + b ε) = g(a) + g'(a) b ε: times b")


def test_dual_log_refuses_non_positive_values(ad):
    for a in (0.0, -0.75):
        _expect_error(ValueError, lambda: ad.Dual(a, 1.0).log(), f"Dual({a}, 1.0).log()",
                      "log is defined for positive numbers only")


# --- dual_derivative ---------------------------------------------------------------------------------------------

T = sympy.Symbol("t")


FOR_DUAL = {"exp": lambda u: u.exp(), "log": lambda u: u.log(), "sin": lambda u: u.sin(), "cos": lambda u: u.cos()}
FOR_SYMPY = {"exp": sympy.exp, "log": sympy.log, "sin": sympy.sin, "cos": sympy.cos}


# functions written once, for Dual (methods) and for SymPy (functions), with the points where they are defined
FUNCTIONS_1 = [
    ("(3t - 1) / (t² + 2)", lambda t, F: (3 * t - 1) / (t ** 2 + 2), (-1.5, 0.0, 2.0)),
    ("sin t cos t + 1/t", lambda t, F: F["sin"](t) * F["cos"](t) + 1 / t, (-0.7, 0.4, 3.0)),
    ("ln(t² + 1) - t e^(-t)", lambda t, F: F["log"](t ** 2 + 1) - t * F["exp"](-t), (-2.0, 0.5, 1.25)),
    ("√(1 + t²) / t³", lambda t, F: (1 + t ** 2) ** 0.5 / t ** 3, (-1.1, 0.6, 2.4)),
    ("cos(e^t - 2 t)", lambda t, F: F["cos"](F["exp"](t) - 2 * t), (-1.0, 0.0, 1.5)),
    ("sin²(t) + cos²(t)", lambda t, F: F["sin"](t) ** 2 + F["cos"](t) ** 2, (-2.0, 1.0, 5.0)),
]


@pytest.mark.parametrize("text, build, points", FUNCTIONS_1,
                         ids=["quotient", "sin-cos", "log-exp", "sqrt-power", "cos-exp", "sin2-cos2"])
def test_dual_derivative_matches_sympy(ad, text, build, points):
    expr = build(T, FOR_SYMPY)
    for x in points:
        want = (float(expr.subs(T, sympy.Rational(x))), float(sympy.diff(expr, T).subs(T, sympy.Rational(x))))
        got = _result(lambda: ad.dual_derivative(lambda u: build(u, FOR_DUAL), x), f"{want}",
                      f"{text} at {x}")
        assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (value, derivative), got {got!r}"
        assert all(math.isclose(g, w, rel_tol=1e-9, abs_tol=1e-12) for g, w in zip(got, want)), (
            f"expected (f(x), f'(x)) = ({want[0]:.10g}, {want[1]:.10g}) for f(t) = {text} at x = {x} (SymPy), "
            f"got ({got[0]:.10g}, {got[1]:.10g})")


def test_dual_derivative_docstring_examples_and_types(ad):
    for text, f, x, want in (("t e^t", lambda t: t * t.exp(), 0.0, (0.0, 1.0)),
                             ("ln(t² + 1)", lambda t: (t ** 2 + 1).log(), 1.0, (math.log(2), 1.0))):
        got = _result(lambda: ad.dual_derivative(f, x), f"{want}", f"{text} at {x}")
        assert isinstance(got, tuple) and len(got) == 2 and all(type(v) is float for v in got), (
            f"expected a tuple of two float, got {got!r}")
        assert all(math.isclose(g, w, abs_tol=1e-12) for g, w in zip(got, want)), (
            f"expected {want} for {text} at {x}, got {got}")


def test_dual_derivative_evaluates_f_once_on_a_seeded_dual(ad):
    """Forward mode: one evaluation of f at Dual(x, 1.0), and the derivative is exact (no finite difference)."""
    seen = []

    def f(t):
        seen.append(t)
        return t ** 3 - 2 * t + 1

    got = _result(lambda: ad.dual_derivative(f, 1.5), "(1.375, 4.75)", "t³ - 2t + 1 at 1.5")
    assert len(seen) == 1, f"expected exactly 1 evaluation of f (at Dual(x, 1.0)), got {len(seen)}"
    t = seen[0]
    assert isinstance(t, ad.Dual) and t.value == 1.5 and t.derivative == 1.0, (
        f"expected f to be evaluated at Dual(value=1.5, derivative=1.0) (the seed 1: dx/dx = 1), got {t!r}")
    assert all(math.isclose(g, w, rel_tol=1e-13) for g, w in zip(got, (1.375, 4.75))), (
        f"expected (1.375, 4.75) for t³ - 2t + 1 at 1.5 to about 13 digits (no step h, so no truncation error), "
        f"got {got}")


def test_dual_derivative_of_a_constant_function(ad):
    for value in (5, 2.5, -1):
        got = _result(lambda: ad.dual_derivative(lambda t: value, 3.0), f"({float(value)}, 0.0)",
                      f"the constant function {value}")
        assert got == (float(value), 0.0) and all(type(v) is float for v in got), (
            f"expected ({float(value)}, 0.0), two float, for a function that returns the number {value!r}, got {got!r}")


def test_dual_derivative_refuses_other_results(ad):
    for bad in ("1.5", None, [1.0, 2.0]):
        _expect_error(TypeError, lambda: ad.dual_derivative(lambda t: bad, 1.0),
                      f"dual_derivative of a function that returns {bad!r}", "f must return a Dual or a number")


# --- forward_gradient --------------------------------------------------------------------------------------------

X1, X2, X3, X4 = sympy.symbols("x1 x2 x3 x4")
FUNCTIONS_N = [
    ("x1 x2 + sin x2", lambda v, F: v[0] * v[1] + F["sin"](v[1]), (X1, X2), [2.0, 0.0]),
    ("e^(x1 - x2) / (1 + x3²)", lambda v, F: F["exp"](v[0] - v[1]) / (1 + v[2] ** 2), (X1, X2, X3), [0.3, -0.4, 1.2]),
    ("ln(x1² + x2² + 1) cos(x3 x4)", lambda v, F: F["log"](v[0] ** 2 + v[1] ** 2 + 1) * F["cos"](v[2] * v[3]),
     (X1, X2, X3, X4), [1.1, -0.6, 0.8, 2.0]),
    ("(x1 + 2 x2)³ - x1 / x2", lambda v, F: (v[0] + 2 * v[1]) ** 3 - v[0] / v[1], (X1, X2), [-1.3, 0.9]),
]


@pytest.mark.parametrize("text, build, symbols, x", FUNCTIONS_N, ids=["product-sin", "exp-quotient", "log-cos", "cube-quotient"])
def test_forward_gradient_matches_sympy(ad, text, build, symbols, x):
    expr = build(symbols, FOR_SYMPY)
    at = dict(zip(symbols, map(sympy.Rational, x)))
    want = np.array([float(sympy.diff(expr, s).subs(at)) for s in symbols])
    got = _result(lambda: ad.forward_gradient(lambda v: build(v, FOR_DUAL), x), _show(want), f"{text} at {x}")
    _float_array(got, want.shape, f"forward_gradient for {text}")
    _close(got, want, f"the gradient of {text} at {x} (SymPy)",
           hint="pass i seeds x_i with 1 and the others with 0, then keeps the derivative part")


def test_forward_gradient_makes_one_pass_per_coordinate_with_the_right_seeds(ad):
    x = np.array([0.5, -1.0, 2.0, 3.5])
    kept = x.copy()
    seen = []

    def f(v):
        seen.append([(d.value, d.derivative) if isinstance(d, ad.Dual) else d for d in v])
        return v[0] * v[1] + v[2] * v[3]

    got = _result(lambda: ad.forward_gradient(f, x), "[-1, 0.5, 3.5, 2]", "x1 x2 + x3 x4 at (0.5, -1, 2, 3.5)")
    assert len(seen) == 4, f"expected n = 4 passes (one evaluation of f per coordinate), got {len(seen)}"
    for i, duals in enumerate(seen):
        want = [(float(x[j]), 1.0 if j == i else 0.0) for j in range(4)]
        assert duals == want, (f"expected pass {i} to give f the duals {want} (value x_j, derivative 1 for j = {i} and "
                               f"0 elsewhere), got {duals}")
    _close(got, [-1.0, 0.5, 3.5, 2.0], "the gradient of x1 x2 + x3 x4 at (0.5, -1, 2, 3.5)")
    assert np.array_equal(x, kept), "expected x to be left unchanged"


def test_forward_gradient_is_exact_and_accepts_integers(ad):
    got = _result(lambda: ad.forward_gradient(lambda v: v[0] ** 2 * v[1] - 3 * v[1], [1, 2]), "[4, -2]",
                  "x1² x2 - 3 x2 at (1, 2), a list of int")
    _float_array(got, (2,), "forward_gradient(f, [1, 2])")
    assert np.allclose(got, [4.0, -2.0], rtol=1e-13, atol=1e-13), (
        f"expected [4, -2], the gradient of x1² x2 - 3 x2 at (1, 2), to about 13 digits (no step h, so no truncation "
        f"error), got {_show(got)}")


def test_forward_gradient_docstring_example_and_constant_function(ad):
    got = _result(lambda: ad.forward_gradient(lambda v: v[0] * v[1] + v[1].sin(), [2.0, 0.0]), "[0, 3]",
                  "x1 x2 + sin x2 at (2, 0)")
    _float_array(got, (2,), "forward_gradient of the docstring example")
    _close(got, [0.0, 3.0], "the gradient of x1 x2 + sin x2 at (2, 0)")
    got = _result(lambda: ad.forward_gradient(lambda v: 7.0, [1.0, 2.0, 3.0]), "[0, 0, 0]", "a constant function")
    _float_array(got, (3,), "forward_gradient of a function that returns the number 7.0")
    _close(got, [0.0, 0.0, 0.0], "the gradient of a constant function",
           hint="a function that returns a plain number has a derivative 0 in every pass")


@pytest.mark.parametrize("x, why", [([[1.0, 2.0]], "x is 2-D"), ([], "x is empty"), (3.0, "x is a number")])
def test_forward_gradient_refuses_bad_points(ad, x, why):
    _expect_error(ValueError, lambda: ad.forward_gradient(lambda v: v[0], x), f"forward_gradient(f, {x!r})", why)


# --- gradient_from_differential ----------------------------------------------------------------------------------

def test_gradient_from_differential_docstring_examples(ad):
    X = np.array([[1.0, 0.0], [2.0, -1.0]])
    got = _result(lambda: ad.gradient_from_differential(lambda H: 2 * np.sum(X * H), X.shape), "2 X",
                  "‖X‖², df = 2 tr(Xᵀ H)")
    _float_array(got, (2, 2), "gradient_from_differential for ‖X‖²")
    _close(got, 2 * X, "the gradient of ‖X‖² at X = [[1, 0], [2, -1]]")
    got = _result(lambda: ad.gradient_from_differential(lambda H: 2 * H[0] + H[1] + 6 * H[2], 3), "[2, 1, 6]",
                  "a linear form on ℝ³, shape = 3")
    _float_array(got, (3,), "gradient_from_differential(..., 3)")
    _close(got, [2.0, 1.0, 6.0], "the coefficients of H ↦ 2 H[0] + H[1] + 6 H[2]")


@pytest.mark.parametrize("shape", [(5,), (2, 3), (3, 2), (2, 2, 3), (1, 1)])
def test_gradient_from_differential_recovers_the_coefficients(ad, shape):
    C = np.random.default_rng(5110).normal(size=shape)
    got = _result(lambda: ad.gradient_from_differential(lambda H: float(np.sum(C * H)), shape),
                  f"an array of shape {shape}", f"the linear form H ↦ Σ C[i, j] H[i, j], shape {shape}")
    _float_array(got, shape, f"gradient_from_differential(..., {shape})")
    _close(got, C, f"the coefficients C of H ↦ Σ C[idx] H[idx] (shape {shape})",
           hint="G[idx] = differential(E) for the move E with a single 1 at idx: the shape of the variable")


def _sympy_gradient(f_of_symbols, shape, X):
    """The gradient of a function of a matrix, by SymPy: one partial derivative per entry, at X."""
    S = sympy.Matrix(*shape, lambda i, j: sympy.Symbol(f"x{i}{j}"))
    f = f_of_symbols(S)
    at = {S[i, j]: sympy.Rational(X[i, j]) for i in range(shape[0]) for j in range(shape[1])}
    return np.array([[float(sympy.diff(f, S[i, j]).subs(at)) for j in range(shape[1])] for i in range(shape[0])])


def test_gradient_from_differential_matches_sympy_on_matrix_functions(ad):
    """Four functions of a matrix and their differentials: the gradient has the shape of X, never its transpose."""
    a, b = np.array([1.0, -2.0, 0.5]), np.array([3.0, 0.25])
    A3 = np.array([[2.0, -1.0, 0.0], [0.5, 1.0, 3.0], [-2.0, 0.0, 1.5]])
    B = np.array([[1.0, 2.0, -1.0], [0.0, 3.0, 0.5]])
    X = np.array([[0.5, -1.0], [2.0, 1.5], [-0.25, 1.0]])           # (3, 2)
    Y = np.array([[2.0, 0.5, 0.0], [-1.0, 1.5, 0.25], [0.5, 0.0, 3.0]])   # invertible (3, 3)
    cases = [
        ("aᵀ X b", X, lambda H: a @ H @ b, lambda S: (sympy.Matrix([a.tolist()]) * S * sympy.Matrix(b))[0, 0]),
        ("tr(B X)", X, lambda H: np.trace(B @ H), lambda S: (sympy.Matrix(B.tolist()) * S).trace()),
        ("tr(Xᵀ A X)", X, lambda H: np.trace(H.T @ A3 @ X + X.T @ A3 @ H),
         lambda S: (S.T * sympy.Matrix(A3.tolist()) * S).trace()),
        ("ln |det Y|", Y, lambda H: np.trace(np.linalg.solve(Y, H)), lambda S: sympy.log(S.det())),
    ]
    for text, point, differential, f in cases:
        want = _sympy_gradient(f, point.shape, point)
        got = _result(lambda: ad.gradient_from_differential(differential, point.shape), f"an array of shape "
                      f"{point.shape}", f"the differential of {text}")
        _float_array(got, point.shape, f"gradient_from_differential for {text}")
        _close(got, want, f"the gradient of {text} (SymPy, entry by entry)", atol=1e-9,
               hint="G[i, j] is the value of the differential on the move with a single 1 at (i, j)")


def test_gradient_from_differential_gives_one_move_per_entry(ad):
    shape = (2, 3)
    moves = []

    def differential(H):
        moves.append(np.array(H, copy=True))
        return float(np.sum(H))

    _result(lambda: ad.gradient_from_differential(differential, shape), "an array of ones", "H ↦ Σ H[i, j]")
    assert len(moves) == 6, f"expected 6 evaluations of the differential (one per entry of a (2, 3) array), got {len(moves)}"
    ones = set()
    for E in moves:
        assert E.shape == shape and E.dtype.kind == "f", (
            f"expected each move to be an array of floats of shape {shape}, got shape {E.shape} and dtype {E.dtype}")
        nonzero = list(zip(*np.nonzero(E)))
        assert len(nonzero) == 1 and E[nonzero[0]] == 1.0, (
            f"expected each move to have a single 1 and zeros elsewhere, got {_show(E)} (start each move from zeros)")
        ones.add(tuple(int(i) for i in nonzero[0]))
    assert len(ones) == 6, f"expected the six moves E_ij to cover the six entries, got the entries {sorted(ones)}"


def test_gradient_from_differential_returns_floats(ad):
    got = _result(lambda: ad.gradient_from_differential(lambda H: int(round(3 * H.sum())), (2, 2)),
                  "[[3., 3.], [3., 3.]]", "a differential that returns Python int")
    _float_array(got, (2, 2), "gradient_from_differential for a differential that returns int")
    _close(got, np.full((2, 2), 3.0), "the gradient of H ↦ 3 Σ H[i, j]")


@pytest.mark.parametrize("shape, why", [(0, "a length 0"), (-2, "a negative length"), ((2, 0), "a length 0"),
                                        ((3, -1), "a negative length"), (2.5, "a length that is not an integer"),
                                        ((2, 1.5), "a length that is not an integer")])
def test_gradient_from_differential_refuses_bad_shapes(ad, shape, why):
    _expect_error(ValueError, lambda: ad.gradient_from_differential(lambda H: 0.0, shape),
                  f"gradient_from_differential(..., {shape!r})", why)
