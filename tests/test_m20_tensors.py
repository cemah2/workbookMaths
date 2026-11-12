"""Tests of mymath.tensors (chapter M20): ``einsum`` for two arrays written with loops, the mean and the variance
along chosen axes, and the Horvitz-Thompson estimator of a total.

Oracles: ``np.einsum`` (on random arrays and every kind of formula), ``np.mean`` and ``np.var`` with
``keepdims=True``, exact sums of fractions (``fractions.Fraction``) for the Horvitz-Thompson estimate and its
expectation over all the 2ᴺ possible samples, and properties (shapes, floats, a 0-d result, inputs left unchanged,
the values outside the sample never read). They describe the expected behaviour without showing the solution.

    pytest tests/test_m20_tensors.py              # your code
    pytest tests/test_m20_tensors.py --impl=ref   # the reference
"""

import ast
import inspect
import itertools
import math
import warnings
from fractions import Fraction

import numpy as np
import pytest


@pytest.fixture
def te(mymath_module):
    return mymath_module("tensors")


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
    """A short text for an array: more than 8 numbers show the first 8 (flattened), then « … »."""
    arr = np.asarray(v, dtype=float)
    if arr.size > 8:
        return np.array2string(arr.ravel()[:8], precision=6, suppress_small=True).replace("]", " …]") + (
            f" (shape {arr.shape})")
    return np.array2string(arr, precision=6, suppress_small=True, max_line_width=10_000).replace("\n", "")


def _float_array(got, shape, what):
    assert isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape, (
        f"expected {what} as a numpy.ndarray of floats of shape {shape}, got {type(got).__name__}"
        + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray) else ""))


def _close(got, want, what, rtol=1e-9, atol=1e-12, hint=""):
    got = np.asarray(got, dtype=float)
    want = np.asarray(want, dtype=float)
    where = ""
    if got.shape == want.shape and want.size > 8:
        wrong = np.argwhere(~np.isclose(got, want, rtol=rtol, atol=atol))
        if wrong.size:
            i = tuple(int(k) for k in wrong[0])
            where = f", first difference at index {i}: expected {want[i]:.10g}, got {got[i]:.10g}"
    assert got.shape == want.shape and np.allclose(got, want, rtol=rtol, atol=atol), (
        f"expected {what} = {_show(want)}, got {_show(got)}"
        + ("" if got.shape == want.shape else f" (shape {got.shape} instead of {want.shape})")
        + where + (f" ({hint})" if hint else ""))


# --- what the module may use ------------------------------------------------------------------------------------

FORBIDDEN = {"einsum_pair": {"einsum", "tensordot", "matmul", "dot", "inner", "outer", "vdot", "@"},
             "moments_along_axes": {"var", "std", "nanvar", "nanstd"}}


def test_module_uses_neither_einsum_in_einsum_pair_nor_var_in_moments_along_axes(te):
    """The docstring forbids np.einsum, tensordot, matmul (@), dot, inner and outer in einsum_pair, and np.var and
    np.std in moments_along_axes, also in the module's own functions that they call."""
    try:
        tree = ast.parse(inspect.getsource(te))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    functions = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    imported = {a.asname or a.name for node in ast.walk(tree) if isinstance(node, ast.ImportFrom) for a in node.names}
    found = []
    for root, forbidden in FORBIDDEN.items():
        seen, todo = set(), [root]
        while todo:                              # root and the module functions it calls, directly or not
            name = todo.pop()
            if name in seen or name not in functions:
                continue
            seen.add(name)
            for node in ast.walk(functions[name]):
                if isinstance(node, ast.Name) and node.id in functions:
                    todo.append(node.id)
                used = None
                if isinstance(node, ast.Attribute):
                    used = node.attr
                elif isinstance(node, ast.Name) and node.id in imported:
                    used = node.id
                elif isinstance(node, (ast.BinOp, ast.AugAssign)) and isinstance(node.op, ast.MatMult):
                    used = "@"
                if used in forbidden:
                    found.append(f"{used} in {name}" + ("" if name == root else f" (called by {root})"))
    assert not found, (f"expected einsum_pair without einsum, tensordot, matmul, @, dot, inner, outer, and "
                       f"moments_along_axes without var and std, found {sorted(set(found))} (the tests compare your "
                       f"results with them)")


# --- einsum_pair --------------------------------------------------------------------------------------------------

def test_einsum_pair_docstring_examples(te):
    got = _result(lambda: te.einsum_pair("ij,jk->ik", [[1, 2], [3, 4]], [[1, 0], [1, 1]]), "[[3, 2], [7, 4]]",
                  '"ij,jk->ik", [[1, 2], [3, 4]] and [[1, 0], [1, 1]]')
    _float_array(got, (2, 2), 'einsum_pair("ij,jk->ik", …)')
    _close(got, [[3, 2], [7, 4]], 'einsum_pair("ij,jk->ik", [[1, 2], [3, 4]], [[1, 0], [1, 1]])')
    got = _result(lambda: te.einsum_pair("i,i->", [1, 2, 3], [4, 5, 6]), "array(32.)", '"i,i->"')
    _float_array(got, (), 'einsum_pair("i,i->", [1, 2, 3], [4, 5, 6]), a 0-d array')
    _close(got, 32.0, 'einsum_pair("i,i->", [1, 2, 3], [4, 5, 6])')
    got = _result(lambda: te.einsum_pair("i,j->ij", [1, 2], [3, 4, 5]), "[[3, 4, 5], [6, 8, 10]]", '"i,j->ij"')
    _float_array(got, (2, 3), 'einsum_pair("i,j->ij", [1, 2], [3, 4, 5])')
    _close(got, [[3, 4, 5], [6, 8, 10]], 'einsum_pair("i,j->ij", [1, 2], [3, 4, 5])')
    got = _result(lambda: te.einsum_pair("nij,njk->nik", np.ones((2, 2, 3)), np.ones((2, 3, 1))), "shape (2, 2, 1)",
                  '"nij,njk->nik"')
    _float_array(got, (2, 2, 1), 'einsum_pair("nij,njk->nik", ones (2, 2, 3), ones (2, 3, 1))')
    _close(got, np.full((2, 2, 1), 3.0), 'einsum_pair("nij,njk->nik", ones (2, 2, 3), ones (2, 3, 1))')


FORMULAS = [
    ("ij,jk->ik", (3, 4), (4, 2), "a matrix product"),
    ("ij,jk->ki", (3, 4), (4, 2), "the transpose of a product: the result letters in another order"),
    ("i,i->", (5,), (5,), "a dot product"),
    ("ij,ij->", (3, 4), (3, 4), "the sum of the products of two tables"),
    ("ij,ij->i", (3, 4), (3, 4), "one dot product per row"),
    ("ij,j->i", (3, 4), (4,), "a matrix times a vector"),
    ("j,ij->i", (4,), (3, 4), "the same, operands swapped"),
    ("ij,kj->ik", (3, 4), (2, 4), "a matrix times the transpose of another"),
    ("ij,j->j", (3, 4), (4,), "a letter of a alone, summed over"),
    ("ij,kl->ijkl", (2, 3), (2, 2), "every product, nothing summed"),
    ("sij,sjk->sik", (3, 2, 4), (3, 4, 2), "a product for each matrix stacked along an axis"),
    ("ijk,kl->ijl", (3, 2, 4), (4, 3), "a 3-axis array times a matrix along its last axis"),
    ("abc,ca->b", (3, 2, 5), (5, 3), "two summed letters"),
    ("Ij,jK->IK", (2, 3), (3, 2), "upper-case letters"),
    (",i->i", (), (3,), "a 0-d operand (no letter) times a vector"),
    ("ij,->ji", (2, 3), (), "a matrix times a 0-d operand, transposed"),
]


@pytest.mark.parametrize("formula, shape_a, shape_b, text", FORMULAS, ids=[f[0] for f in FORMULAS])
def test_einsum_pair_matches_np_einsum(te, formula, shape_a, shape_b, text):
    rng = np.random.default_rng(5310 + FORMULAS.index((formula, shape_a, shape_b, text)))
    a = rng.integers(-5, 6, size=shape_a).astype(float) / 2   # halves: the products and sums are exact
    b = rng.integers(-5, 6, size=shape_b).astype(float) / 2
    want = np.einsum(formula, a, b)
    got = _result(lambda: te.einsum_pair(formula, a, b), f"np.einsum({formula!r}, a, b) of shape {want.shape}",
                  f"{text}, a of shape {shape_a} and b of shape {shape_b}")
    _float_array(got, want.shape, f"einsum_pair({formula!r}, a, b) ({text})")
    _close(got, want, f"einsum_pair({formula!r}, a, b) ({text})", rtol=0, atol=1e-12)


def test_einsum_pair_random_reals_and_integer_inputs(te):
    rng = np.random.default_rng(5326)
    a, b = rng.normal(size=(4, 3, 2)), rng.normal(size=(2, 5))
    _close(_result(lambda: te.einsum_pair("ijk,kl->li", a, b), "np.einsum('ijk,kl->li', a, b)", "random reals"),
           np.einsum("ijk,kl->li", a, b), "einsum_pair('ijk,kl->li', a, b) on random reals", rtol=1e-12)
    a, b = [[1, 2, 3], [4, 5, 6]], [[1, 1], [0, 2], [3, 0]]
    got = _result(lambda: te.einsum_pair("ij,jk->ik", a, b), "[[10, 5], [22, 14]]", "lists of integers")
    _float_array(got, (2, 2), "einsum_pair on lists of integers (a result of floats)")
    _close(got, [[10, 5], [22, 14]], "einsum_pair('ij,jk->ik', [[1, 2, 3], [4, 5, 6]], [[1, 1], [0, 2], [3, 0]])")


def test_einsum_pair_with_an_axis_of_length_zero(te):
    """An empty sum is 0; an empty result axis gives an empty result (as np.einsum)."""
    got = _result(lambda: te.einsum_pair("ij,jk->ik", np.zeros((2, 0)), np.zeros((0, 3))), "zeros of shape (2, 3)",
                  "a summed letter of length 0 (an empty sum is 0)")
    _float_array(got, (2, 3), "einsum_pair('ij,jk->ik') with j of length 0")
    _close(got, np.zeros((2, 3)), "einsum_pair('ij,jk->ik') with j of length 0 (an empty sum is 0)")
    got = _result(lambda: te.einsum_pair("ij,jk->ik", np.zeros((0, 2)), np.ones((2, 3))), "an array of shape (0, 3)",
                  "i of length 0")
    _float_array(got, (0, 3), "einsum_pair('ij,jk->ik') with i of length 0")


def test_einsum_pair_does_not_modify_its_inputs(te):
    a = np.array([[1.0, -2.0], [0.5, 3.0]])
    b = np.array([2.0, -1.0])
    a0, b0 = a.copy(), b.copy()
    got = _result(lambda: te.einsum_pair("ij,j->i", a, b), "[4, -2]", "a (2, 2) matrix and a vector")
    _close(got, [4.0, -2.0], "einsum_pair('ij,j->i', [[1, -2], [0.5, 3]], [2, -1])")
    assert np.array_equal(a, a0) and np.array_equal(b, b0), (
        f"expected a and b unchanged, got a = {_show(a)} and b = {_show(b)} (work on copies)")
    got[0] = 99.0
    assert np.array_equal(a, a0) and np.array_equal(b, b0), (
        "expected a result that is a new array, but changing it changed a or b")


EINSUM_REFUSALS = [
    ("ij,jk", (2, 2), (2, 2), "no '->': the explicit form is required"),
    ("ij,jk->ik->ik", (2, 2), (2, 2), "two '->'"),
    ("ijjk->ik", (2, 2), (2, 2), "no comma: two operands are expected"),
    ("ij,jk,kl->il", (2, 2), (2, 2), "two commas"),
    ("ij,jk->i k", (2, 2), (2, 2), "a space in the result"),
    ("i1,1k->ik", (2, 2), (2, 2), "a digit is not a letter"),
    ("...j,jk->...k", (2, 2), (2, 2), "'...' is not allowed here: letters only"),
    ("ijk,jk->i", (2, 2), (2, 2), "3 letters for a 2-axis array"),
    ("i,ij->j", (2, 2), (2, 2), "1 letter for a 2-axis array"),
    ("ii,i->i", (2, 2), (2,), "a letter repeated in one operand (a trace inside a is excluded)"),
    ("ij,jk->ii", (2, 2), (2, 2), "a letter repeated in the result"),
    ("ij,jk->iz", (2, 2), (2, 2), "z appears in no operand"),
    ("ij,jk->ik", (2, 3), (4, 2), "the shared letter j has lengths 3 and 4"),
    ("i,i->", (3,), (2,), "the shared letter i has lengths 3 and 2"),
]


@pytest.mark.parametrize("formula, shape_a, shape_b, why", EINSUM_REFUSALS,
                         ids=["no-arrow", "two-arrows", "no-comma", "two-commas", "space", "digit", "ellipsis",
                              "too-many-letters", "too-few-letters", "repeated-in-operand", "repeated-in-result",
                              "unknown-result-letter", "shared-lengths-differ", "vectors-of-two-lengths"])
def test_einsum_pair_refusals(te, formula, shape_a, shape_b, why):
    a, b = np.ones(shape_a), np.ones(shape_b)
    _expect_error(ValueError, lambda: te.einsum_pair(formula, a, b),
                  f"einsum_pair({formula!r}, a of shape {shape_a}, b of shape {shape_b})", why)


# --- moments_along_axes -------------------------------------------------------------------------------------------

def test_moments_along_axes_docstring_examples(te):
    x = np.array([[1.0, 2.0, 6.0], [3.0, 2.0, 4.0]])
    got = _result(lambda: te.moments_along_axes(x, axes=1), "(mean [[3], [3]], var [[14/3], [2/3]])",
                  "[[1, 2, 6], [3, 2, 4]], axes=1")
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (mean, var), got {got!r}"
    mean, var = got
    _float_array(mean, (2, 1), "the mean along axes=1 (the reduced axis kept with length 1)")
    _float_array(var, (2, 1), "the variance along axes=1")
    _close(mean, [[3.0], [3.0]], "the mean of [[1, 2, 6], [3, 2, 4]] along axis 1")
    _close(var, [[14 / 3], [2 / 3]], "the variance (ddof=0) of [[1, 2, 6], [3, 2, 4]] along axis 1")
    mean, var = _result(lambda: te.moments_along_axes(x, axes=(0, 1), ddof=1), "(mean [[3]], var [[3.2]])",
                        "axes=(0, 1), ddof=1")
    _float_array(mean, (1, 1), "the mean along axes=(0, 1)")
    _float_array(var, (1, 1), "the variance along axes=(0, 1)")
    _close(mean, [[3.0]], "the mean of the 6 values")
    _close(var, [[3.2]], "the variance with ddof=1 of the 6 values (16 / 5)")


# a table of measurements: 4 stations × 7 days × 6 hours, then other shapes
CASES = [((4, 7, 6), 0, 0), ((4, 7, 6), 1, 1), ((4, 7, 6), 2, 0), ((4, 7, 6), -1, 1), ((4, 7, 6), (0, 2), 0),
         ((4, 7, 6), (2, 0), 1), ((4, 7, 6), (1, 2), 1), ((4, 7, 6), (0, 1, 2), 0), ((4, 7, 6), (-3, -2), 1),
         ((9,), 0, 1), ((9,), (0,), 0), ((3, 4, 2, 2), (1, 3), 1), ((3, 4, 2, 2), [0, 1, 3], 0), ((5, 1), 0, 4)]


@pytest.mark.parametrize("shape, axes, ddof", CASES, ids=[f"{s}-axes{a}-ddof{d}" for s, a, d in CASES])
def test_moments_along_axes_match_numpy(te, shape, axes, ddof):
    rng = np.random.default_rng(5320 + CASES.index((shape, axes, ddof)))
    x = rng.normal(loc=12.0, scale=4.0, size=shape)
    axis = tuple(axes) if isinstance(axes, list) else axes
    want_mean = np.mean(x, axis=axis, keepdims=True)
    want_var = np.var(x, axis=axis, keepdims=True, ddof=ddof)
    got = _result(lambda: te.moments_along_axes(x, axes, ddof=ddof),
                  f"np.mean and np.var(ddof={ddof}) with keepdims, of shape {want_mean.shape}",
                  f"x of shape {shape}, axes={axes!r}")
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (mean, var), got {type(got).__name__}"
    mean, var = got
    _float_array(mean, want_mean.shape, f"the mean of x {shape} along axes={axes!r} (reduced axes kept, length 1)")
    _float_array(var, want_var.shape, f"the variance of x {shape} along axes={axes!r}")
    _close(mean, want_mean, f"the mean along axes={axes!r}", rtol=1e-12)
    _close(var, want_var, f"the variance along axes={axes!r} with ddof={ddof}", rtol=1e-10,
           hint=f"divide the sum of the squared deviations by N - ddof, N being the number of values reduced together")


def test_moments_along_axes_is_accurate_for_large_values(te):
    """The definition subtracts the mean first: Σ x²/N - mean² loses every digit when the values are large."""
    x = 1e8 + np.array([[1.0, 2.0, 3.0, 4.0], [0.0, 1.0, 1.0, 4.0]])
    mean, var = _result(lambda: te.moments_along_axes(x, axes=1), "var [[1.25], [2.25]]", "1e8 + [[1, 2, 3, 4], [0, 1, 1, 4]]")
    _close(mean, [[1e8 + 2.5], [1e8 + 1.5]], "the means of 1e8 + [[1, 2, 3, 4], [0, 1, 1, 4]] along axis 1",
           rtol=1e-15)
    _close(var, [[1.25], [2.25]], "the variances of 1e8 + [[1, 2, 3, 4], [0, 1, 1, 4]] along axis 1", rtol=1e-9,
           hint="compute Σ (x - mean)² / (N - ddof) as defined; the formula mean of x² - mean² cancels the digits")


def test_moments_along_axes_integers_and_ddof_at_its_limit(te):
    mean, var = _result(lambda: te.moments_along_axes([[1, 4], [5, 14]], axes=(0, 1), ddof=3),
                        "mean [[6]] and var [[94]]", "the integers [[1, 4], [5, 14]], ddof = N - 1 = 3")
    _float_array(mean, (1, 1), "the mean of an integer array (floats)")
    _float_array(var, (1, 1), "the variance of an integer array (floats)")
    _close(mean, [[6.0]], "the mean of [[1, 4], [5, 14]]")
    _close(var, [[94.0]], "the variance of [[1, 4], [5, 14]] with ddof=3 (94 / 1)")


def test_moments_along_axes_broadcast_back_and_inputs_unchanged(te):
    """With the reduced axes kept, x - mean has the shape of x: centered, its mean is 0 and its variance unchanged."""
    x = np.random.default_rng(5329).normal(size=(4, 7, 6)) * 3 + 7      # stations × days × hours
    x0 = x.copy()
    mean, var = _result(lambda: te.moments_along_axes(x, (1, 2)), "a mean and a variance of shape (4, 1, 1)",
                        "x of shape (4, 7, 6), axes=(1, 2)")
    assert np.array_equal(x, x0), "expected x unchanged (the function only computes the two moments)"
    centered = x - mean
    assert centered.shape == x.shape, f"expected x - mean of shape {x.shape}, got {centered.shape}"
    mean2, var2 = _result(lambda: te.moments_along_axes(centered, (1, 2)), "the moments of x - mean",
                          "x - mean, axes=(1, 2)")
    _close(mean2, np.zeros((4, 1, 1)), "the mean of x - mean along axes (1, 2)", atol=1e-12)
    _close(var2, var, "the variance of x - mean along axes (1, 2) (a translation does not change it)")


MOMENT_REFUSALS = [
    ((2, 5, 3), 3, 0, "axis 3 does not exist for 3 axes"),
    ((2, 5, 3), -4, 0, "axis -4 does not exist for 3 axes"),
    ((2, 5, 3), (0, 0), 0, "axis 0 is repeated"),
    ((2, 5, 3), (2, -1), 0, "-1 and 2 are the same axis"),
    ((2, 5, 3), 1, 5, "ddof = N = 5 (division by zero)"),
    ((2, 5, 3), (0, 2), 7, "ddof = 7 > N = 6"),
    ((2, 5, 3), 1, -1, "ddof is negative"),
    ((2, 5, 3), 1, 0.5, "ddof is not an integer"),
    ((2, 0, 3), 1, 0, "N = 0 values: no mean"),
]


@pytest.mark.parametrize("shape, axes, ddof, why", MOMENT_REFUSALS,
                         ids=["axis-too-large", "axis-too-negative", "repeated", "repeated-negative", "ddof-equals-N",
                              "ddof-above-N", "ddof-negative", "ddof-not-integer", "no-values"])
def test_moments_along_axes_refusals(te, shape, axes, ddof, why):
    x = np.ones(shape)
    _expect_error(ValueError, lambda: te.moments_along_axes(x, axes, ddof=ddof),
                  f"moments_along_axes(x of shape {shape}, axes={axes!r}, ddof={ddof!r})", why)


# --- horvitz_thompson_total ----------------------------------------------------------------------------------------

def _ht_exact(values, included, probs):
    return sum((Fraction(y) / Fraction(p) for y, i, p in zip(values, included, probs) if i), Fraction(0))


def test_horvitz_thompson_total_docstring_examples(te):
    got = _result(lambda: te.horvitz_thompson_total([3, 40, 2], [True, False, True], [0.125, 0.2, 0.0625]), "56.0",
                  "[3, 40, 2], units 0 and 2 in the sample, probabilities [0.125, 0.2, 0.0625]")
    assert isinstance(got, float) and math.isclose(got, 56.0, rel_tol=1e-12), (
        f"expected 56.0 (3 / 0.125 + 2 / 0.0625), got {got!r}")
    got = _result(lambda: te.horvitz_thompson_total([3, 7], [1, 1], [1, 1]), "10.0", "a census")
    assert isinstance(got, float) and math.isclose(got, 10.0, rel_tol=1e-12), (
        f"expected 10.0 (a census with probabilities 1 gives the exact total), got {got!r}")


def test_horvitz_thompson_total_matches_exact_fractions(te):
    rng = np.random.default_rng(5327)
    for trial in range(20):
        n = int(rng.integers(1, 12))
        values = rng.integers(0, 500, size=n)
        probs = rng.integers(1, 17, size=n) / 16          # multiples of 1/16 in ]0, 1]
        included = rng.random(n) < probs
        want = _ht_exact(values.tolist(), included.tolist(), probs.tolist())
        got = _result(lambda: te.horvitz_thompson_total(values, included, probs), f"{float(want)!r}",
                      f"values {values.tolist()}, included {included.astype(int).tolist()}, probs {probs.tolist()}")
        assert isinstance(got, float) and math.isclose(got, float(want), rel_tol=1e-12, abs_tol=1e-12), (
            f"expected {float(want)!r} (the sum of y_i / π_i over the sample) for values {values.tolist()}, included "
            f"{included.astype(int).tolist()} and probs {probs.tolist()}, got {got!r}")


def test_horvitz_thompson_total_is_unbiased_over_all_samples(te):
    """With independent inclusions, the 2ᴺ samples weighted by their probabilities average to the exact total."""
    values = [12, 0, 7, 30, 5, 18]
    probs = [Fraction(5, 8), Fraction(1, 6), Fraction(3, 7), Fraction(9, 10), Fraction(1, 8), Fraction(2, 3)]
    expectation = Fraction(0)
    for included in itertools.product([False, True], repeat=len(values)):
        weight = Fraction(1)
        for i, p in zip(included, probs):
            weight *= p if i else 1 - p
        got = _result(lambda: te.horvitz_thompson_total(values, list(included), [float(p) for p in probs]),
                      f"{float(_ht_exact(values, included, probs))!r}", f"the sample {[int(i) for i in included]}")
        assert math.isclose(got, float(_ht_exact(values, included, probs)), rel_tol=1e-12, abs_tol=1e-12), (
            f"expected {float(_ht_exact(values, included, probs))!r} for the sample {[int(i) for i in included]}, "
            f"got {got!r}")
        expectation += weight * Fraction(got)
    assert math.isclose(float(expectation), sum(values), rel_tol=1e-9), (
        f"expected the average over the 64 samples to be the total {sum(values)}, got {float(expectation)!r}")


def test_horvitz_thompson_total_never_reads_the_values_outside_the_sample(te):
    """Outside the sample, the values are unknown: NaN there must not change the estimate."""
    values = [4.0, np.nan, 10.0, np.nan]
    got = _result(lambda: te.horvitz_thompson_total(values, [True, False, True, False], [0.125, 0.3, 0.625, 0.1]),
                  "48.0", "values [4, nan, 10, nan] with the NaN outside the sample",
                  hint="sum over the units of the sample only, not values × included / probs over all units")
    assert isinstance(got, float) and math.isclose(got, 48.0, rel_tol=1e-12), (
        f"expected 48.0 (4 / 0.125 + 10 / 0.625: the values outside the sample are not used), got {got!r}")


def test_horvitz_thompson_total_accepts_booleans_or_0_and_1(te):
    values, probs = np.array([6.0, 2.0, 9.0]), np.array([0.3, 0.35, 0.9])
    for included, text in (([True, False, True], "booleans"), ([1, 0, 1], "integers 0 and 1"),
                           (np.array([1.0, 0.0, 1.0]), "floats 0. and 1.")):
        got = _result(lambda: te.horvitz_thompson_total(values, included, probs), "30.0", f"included as {text}")
        assert isinstance(got, float) and math.isclose(got, 30.0, rel_tol=1e-12), (
            f"expected 30.0 (6 / 0.3 + 9 / 0.9) with included given as {text}, got {got!r}")


def test_horvitz_thompson_total_empty_sample_and_inputs_unchanged(te):
    values, included, probs = np.array([5.0, 8.0]), np.array([False, False]), np.array([0.3, 0.45])
    copies = values.copy(), included.copy(), probs.copy()
    got = _result(lambda: te.horvitz_thompson_total(values, included, probs), "0.0", "an empty sample")
    assert isinstance(got, float) and got == 0.0, f"expected 0.0 for an empty sample (an empty sum), got {got!r}"
    assert all(np.array_equal(u, v) for u, v in zip((values, included, probs), copies)), (
        "expected values, included and inclusion_probs unchanged")


HT_REFUSALS = [
    ([1.0, 2.0], [True, True, False], [0.45, 0.45], "included has 3 units, values 2"),
    ([1.0, 2.0], [True, True], [0.45], "inclusion_probs has 1 unit, values 2"),
    ([[1.0, 2.0]], [[True, True]], [[0.45, 0.45]], "2-D arrays"),
    (3.0, True, 0.45, "numbers, not 1-D arrays"),
    ([1.0, 2.0], [1, 2], [0.45, 0.45], "included holds a 2"),
    ([1.0, 2.0], ["yes", "no"], [0.45, 0.45], "included holds strings"),
    ([1.0, 2.0], [True, True], [0.45, 0.0], "a probability 0: the unit could never be drawn"),
    ([1.0, 2.0], [True, False], [0.45, 0.0], "a probability 0, even outside the sample"),
    ([1.0, 2.0], [True, True], [1.2, 0.45], "a probability above 1"),
    ([1.0, 2.0], [True, True], [-0.45, 0.45], "a negative probability"),
    ([1.0, 2.0], [True, True], [np.nan, 0.45], "a probability NaN"),
]


@pytest.mark.parametrize("values, included, probs, why", HT_REFUSALS,
                         ids=["included-length", "probs-length", "two-d", "scalars", "included-2", "included-text",
                              "prob-zero", "prob-zero-outside", "prob-above-one", "prob-negative", "prob-nan"])
def test_horvitz_thompson_total_refusals(te, values, included, probs, why):
    _expect_error(ValueError, lambda: te.horvitz_thompson_total(values, included, probs),
                  f"horvitz_thompson_total({values!r}, {included!r}, {probs!r})", why)
