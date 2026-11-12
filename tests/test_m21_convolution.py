"""Tests of mymath.convolution (chapter M21): the convolution of two sequences in three modes, the Toeplitz matrix of
a convolution, the circular convolution of two periodic sequences, the equivalent kernel of a stack of strided sliding
sums, and the two factors of a separable 2-D kernel.

Oracles: ``np.convolve`` (the three modes, a second sequence longer than the first, kernels of even length), the
values of a product of polynomials (``fractions.Fraction``), ``scipy.linalg.convolution_matrix`` and
``scipy.linalg.toeplitz`` (and ``T @ x`` against ``np.convolve``), ``np.fft`` and ``scipy.linalg.circulant``, a stack of
sliding sums applied directly to a signal and to impulses (written in this file), ``np.linalg.matrix_rank`` and the
reconstruction ``np.outer(u, v)``; and properties (commutativity, associativity, linearity, a shift of the input, the
unit impulse, the circular convolution as the full one wrapped around, inputs left unchanged, floats). They describe
the expected behaviour without showing the solution.

    pytest tests/test_m21_convolution.py              # your code
    pytest tests/test_m21_convolution.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings
from fractions import Fraction

import numpy as np
import pytest
from scipy.linalg import circulant, convolution_matrix, toeplitz


@pytest.fixture
def cv(mymath_module):
    return mymath_module("convolution")


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
        return np.array2string(arr.ravel()[:8], precision=6, suppress_small=True,
                               max_line_width=10_000).replace("]", " …]") + (
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


MODES = ("full", "valid", "same")
MODE_HINTS = {
    "full": "(a * b)[k] = Σ_i a[i] b[k - i] for k = 0, …, n + m - 2: the kernel is flipped",
    "valid": "the values k = l - 1, …, L - 1 of the full convolution, l and L the shorter and the longer length",
    "same": "L = max(n, m) values of the full convolution from index (l - 1) // 2 on (NumPy's convention), "
            "l = min(n, m)",
}


# --- what the module may use ------------------------------------------------------------------------------------

FORBIDDEN = ("convolve", "correlate", "polymul", "polynomial", "fft")


def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``svd`` (from numpy.linalg import svd) → "numpy.linalg.svd"."""
    names = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname:
                    names[alias.asname] = alias.name
                else:                                     # import numpy.linalg binds the name numpy
                    names[alias.name.split(".")[0]] = alias.name.split(".")[0]
        elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
            for alias in node.names:
                names[alias.asname or alias.name] = f"{node.module}.{alias.name}"
    return names


def _uses(tree, names):
    """Each use of an imported name (or of a chain of attributes on it): (where, dotted path), e.g.
    ("separable_factors", "numpy.linalg.svd"); ``where`` is the top-level function, or "the module level"."""
    inner = {id(node.value) for node in ast.walk(tree) if isinstance(node, ast.Attribute)}
    uses = []
    for statement in tree.body:
        where = statement.name if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)) else "the module level"
        for node in ast.walk(statement):
            if not isinstance(node, (ast.Name, ast.Attribute)) or id(node) in inner:
                continue                                  # only the whole chain np.linalg.svd, not np.linalg
            attrs = []
            while isinstance(node, ast.Attribute):
                attrs.append(node.attr)
                node = node.value
            if isinstance(node, ast.Name) and node.id in names:
                uses.append((where, ".".join([names[node.id]] + attrs[::-1])))
    return uses


def test_module_uses_no_convolution_of_numpy_no_scipy_and_svd_only_in_separable_factors(cv):
    """The docstring forbids np.convolve, np.correlate, np.polymul, np.polynomial, np.fft and all of SciPy, and allows
    from np.linalg only svd, in separable_factors (and in the module's own functions that it calls). Only the code
    counts: a comment, a docstring or an import never used is not a use."""
    try:
        tree = ast.parse(inspect.getsource(cv))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    functions = {n.name: n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    svd_allowed, todo = set(), ["separable_factors"]
    while todo:                                  # separable_factors and the module functions it calls
        name = todo.pop()
        if name in svd_allowed or name not in functions:
            continue
        svd_allowed.add(name)
        todo += [n.id for n in ast.walk(functions[name]) if isinstance(n, ast.Name) and n.id in functions]
    found = []
    for where, path in _uses(tree, _imported_names(tree)):
        parts = path.split(".")
        shown = ".".join(["np"] + parts[1:]) if parts[0] == "numpy" else path
        if parts[0] == "scipy":
            found.append(f"{shown} in {where}")
        elif parts[0] == "numpy" and any(p in FORBIDDEN for p in parts[1:]):
            found.append(f"{shown} in {where}")
        elif parts[0] == "numpy" and len(parts) > 2 and parts[1] == "linalg":
            if parts[2] != "svd" or where not in svd_allowed:
                found.append(f"{shown} in {where}")
    assert not found, (f"expected NumPy without np.convolve, np.correlate, np.polymul, np.polynomial nor np.fft, no "
                       f"SciPy at all, and from np.linalg only svd in separable_factors, found {sorted(set(found))} "
                       f"(the tests compare your results with them)")


# --- convolve -----------------------------------------------------------------------------------------------------

def test_convolve_docstring_examples(cv):
    for a, b, mode, want in (([2, 1], [1, 3, 1], "full", [2.0, 7.0, 5.0, 1.0]),
                             ([3, 1, 4, 1, 5], [2, -1, 1], "valid", [10.0, -1.0, 13.0]),
                             ([3, 1, 4, 1, 5], [2, -1, 1], "same", [-1.0, 10.0, -1.0, 13.0, -4.0])):
        call = f"convolve({a}, {b}, mode={mode!r})"
        got = _result(lambda: cv.convolve(a, b, mode=mode), _show(want), call)
        _float_array(got, (len(want),), call)
        _close(got, want, call, rtol=0, atol=1e-12, hint=MODE_HINTS[mode])


SHAPES = [(9, 3, "a kernel of odd length"), (10, 4, "a kernel of even length"), (8, 2, "a kernel of length 2"),
          (4, 11, "b longer than a"), (3, 8, "b longer than a, a of odd length"),
          (6, 6, "two sequences of the same length"), (7, 1, "b of length 1"), (1, 5, "a of length 1"),
          (1, 1, "two single numbers")]
CONVOLVE_CASES = [(n, m, mode, text) for n, m, text in SHAPES for mode in MODES]


@pytest.mark.parametrize("n, m, mode, text", CONVOLVE_CASES, ids=[f"{c[2]}-{c[0]}-{c[1]}" for c in CONVOLVE_CASES])
def test_convolve_matches_np_convolve(cv, n, m, mode, text):
    rng = np.random.default_rng(5410 + CONVOLVE_CASES.index((n, m, mode, text)))
    a, b = rng.normal(size=n), rng.normal(size=m)
    want = np.convolve(a, b, mode)
    call = f"convolve(a, b, mode={mode!r}) with len(a) = {n}, len(b) = {m} ({text})"
    got = _result(lambda: cv.convolve(a, b, mode), f"np.convolve(a, b, {mode!r}) of length {want.size}", call)
    _float_array(got, want.shape, call)
    _close(got, want, call, rtol=1e-10, atol=1e-12, hint=MODE_HINTS[mode])


def test_convolve_same_mode_starts_at_index_l_minus_1_over_2(cv):
    """For a shorter length l, "same" keeps the full convolution from index (l - 1) // 2: 0 for l = 2, 1 for l = 4,
    2 for l = 6 (the extra value is on the right, as in NumPy), whichever of a and b is the shorter."""
    a = np.array([4.0, -2.0, 0.5, 3.0, -1.0, 2.5, 1.5])
    for b in ([1.5, -3.0], [2.0, 0.25, -1.0, 0.5], [0.5, 1.0, 1.5, -2.0, 1.0, 3.0], [3.0, -1.0, 2.0]):
        start = (len(b) - 1) // 2
        want = np.convolve(a, b)[start:start + len(a)]
        for x, y, text in ((a, b, "convolve(a, b, 'same')"), (b, a, "convolve(b, a, 'same')")):
            got = _result(lambda: cv.convolve(x, y, "same"), _show(want), f"{text} with l = {len(b)}")
            _float_array(got, (len(a),), f"{text} with l = {len(b)} (L = {len(a)} values)")
            _close(got, want, f"{text} with b = {b}", rtol=1e-12, atol=1e-12,
                   hint=f"the full convolution from index (l - 1) // 2 = {start} on, l = {len(b)} the shorter length")


def _value(coefficients, x):
    """The value at x of the polynomial Σ c[i] xⁱ, exactly."""
    return sum((Fraction(c) * x ** i for i, c in enumerate(coefficients)), Fraction(0))


def test_convolve_multiplies_polynomials(cv):
    """The full convolution of two lists of coefficients is the list of the coefficients of the product: P Q takes
    the value P(x) Q(x) at every x (checked exactly at 13 points, more than the degree of P Q)."""
    rng = np.random.default_rng(5440)
    points = [Fraction(k, 3) for k in range(-6, 7)]
    for trial in range(12):
        p = rng.integers(-9, 10, size=int(rng.integers(1, 7))).tolist()
        q = rng.integers(-9, 10, size=int(rng.integers(1, 7))).tolist()
        call = f"convolve({p}, {q})"
        got = _result(lambda: cv.convolve(p, q), "the coefficients of the product", call)
        _float_array(got, (len(p) + len(q) - 1,), f"{call} (degree {len(p) - 1} + {len(q) - 1})")
        assert all(float(c).is_integer() for c in got), (
            f"expected integer coefficients for the product of {p} and {q} (integer polynomials), got {_show(got)}")
        for x in points:
            assert _value(got, x) == _value(p, x) * _value(q, x), (
                f"expected the product of {p} and {q} to take the value P({x}) Q({x}) = "
                f"{_value(p, x) * _value(q, x)} at x = {x}, got {_value(got, x)} with the coefficients {_show(got)}")


def test_convolve_gives_the_law_of_a_sum_of_two_independent_dice(cv):
    """Laws on 0, 1, …: their convolution is a law (total 1), its mean and its variance are the sums of theirs, and
    its generating function Σ P(S = s) tˢ is the product of theirs (M02b)."""
    rng = np.random.default_rng(5441)
    for faces_a, faces_b in ((6, 6), (4, 9), (11, 3)):
        p = rng.integers(1, 12, size=faces_a).astype(float)
        q = rng.integers(1, 12, size=faces_b).astype(float)
        p, q = p / p.sum(), q / q.sum()
        text = f"the laws of a die with {faces_a} faces and of a die with {faces_b} faces"
        law = _result(lambda: cv.convolve(p, q), "the law of the sum", text)
        _float_array(law, (faces_a + faces_b - 1,), f"the law of the sum of two dice ({text})")
        values = np.arange(law.size)
        mean = lambda r: float(np.sum(np.arange(r.size) * r))                          # noqa: E731
        var = lambda r: float(np.sum((np.arange(r.size) - mean(r)) ** 2 * r))         # noqa: E731
        assert np.all(law >= -1e-15) and math.isclose(float(np.sum(law)), 1.0, rel_tol=1e-12), (
            f"expected a law (values ≥ 0 of total 1) for the sum of two dice, got {_show(law)} of total "
            f"{float(np.sum(law))!r}")
        assert math.isclose(float(np.sum(values * law)), mean(p) + mean(q), rel_tol=1e-12), (
            f"expected the mean of the sum to be {mean(p) + mean(q):.10g} (the sum of the means), got "
            f"{float(np.sum(values * law)):.10g}")
        assert math.isclose(var(law), var(p) + var(q), rel_tol=1e-10), (
            f"expected the variance of the sum to be {var(p) + var(q):.10g} (independent dice: the sum of the "
            f"variances), got {var(law):.10g}")
        for t in (0.5, -1.0, 2.0):
            g = lambda r: float(np.sum(r * t ** np.arange(r.size)))                    # noqa: E731
            assert math.isclose(g(law), g(p) * g(q), rel_tol=1e-10, abs_tol=1e-12), (
                f"expected the generating function of the sum at t = {t} to be {g(p) * g(q):.10g} (the product of "
                f"those of the two dice), got {g(law):.10g}")


def test_convolve_is_commutative_associative_and_linear(cv):
    rng = np.random.default_rng(5442)
    a, b, c, d = rng.normal(size=7), rng.normal(size=4), rng.normal(size=5), rng.normal(size=7)
    for mode in MODES:
        ab = _result(lambda: cv.convolve(a, b, mode), "a * b", f"mode={mode!r}")
        ba = _result(lambda: cv.convolve(b, a, mode), "b * a", f"mode={mode!r}")
        _close(ba, ab, f"convolve(b, a, {mode!r}), equal to convolve(a, b, {mode!r}) (the convolution is "
                       f"commutative, in every mode: L and l do not depend on the order)", rtol=1e-12, atol=1e-12)
    left = _result(lambda: cv.convolve(cv.convolve(a, b), c), "(a * b) * c", "associativity")
    right = _result(lambda: cv.convolve(a, cv.convolve(b, c)), "a * (b * c)", "associativity")
    _close(left, right, "(a * b) * c, equal to a * (b * c) (associativity, full mode)", rtol=1e-12, atol=1e-12)
    for mode in MODES:
        mixed = _result(lambda: cv.convolve(2.5 * a - 1.5 * d, b, mode), "(2.5 a - 1.5 d) * b", f"mode={mode!r}")
        _close(mixed, 2.5 * cv.convolve(a, b, mode) - 1.5 * cv.convolve(d, b, mode),
               f"convolve(2.5 a - 1.5 d, b, {mode!r}), equal to 2.5 a * b - 1.5 d * b (linearity)", rtol=1e-12,
               atol=1e-12)


def test_convolve_with_an_impulse_and_after_a_shift(cv):
    """(1) is neutral; (0, 0, 1) shifts by two steps; a shift of a shifts a * b by as much (equivariance)."""
    a = np.array([1.5, -2.0, 0.25, 4.0, -3.0])
    got = _result(lambda: cv.convolve(a, [1]), _show(a), "the impulse (1)")
    _float_array(got, (5,), "convolve(a, [1])")
    _close(got, a, "convolve(a, [1]) (the impulse (1) is neutral)", rtol=0, atol=0)
    got = _result(lambda: cv.convolve(a, [0, 0, 1]), "a shifted by two steps", "the impulse (0, 0, 1)")
    _close(got, np.concatenate([[0.0, 0.0], a]), "convolve(a, [0, 0, 1]) (a shifted by two steps)", rtol=0, atol=0,
           hint="(a * b)[k] = Σ_i a[i] b[k - i]: only b[2] = 1, so index k receives a[k - 2]")
    b = np.array([2.0, -0.5, 1.0, 3.0])
    shifted = np.concatenate([np.zeros(3), a])
    got = _result(lambda: cv.convolve(shifted, b), "a * b shifted by three steps", "a shifted by three steps")
    _close(got, np.concatenate([np.zeros(3), np.convolve(a, b)]),
           "convolve((0, 0, 0, a), b), the full convolution a * b shifted by three steps (equivariance)")


def test_convolve_takes_integers_and_lists_and_leaves_its_inputs_alone(cv):
    got = _result(lambda: cv.convolve([3, -1, 5], [1, 4]), "[3, 11, 1, 20]", "lists of integers")
    _float_array(got, (4,), "convolve([3, -1, 5], [1, 4]) (a result of floats)")
    _close(got, [3.0, 11.0, 1.0, 20.0], "convolve([3, -1, 5], [1, 4])", rtol=0, atol=0)
    got = _result(lambda: cv.convolve(np.array([5, 0, -2, 7]), np.array([2, -3, 1])), "floats", "integer arrays")
    _float_array(got, (6,), "convolve of two integer arrays (a result of floats)")
    a, b = np.array([0.5, -1.25, 2.0, 3.5, -0.75, 1.0]), np.array([2.0, -1.0, 0.5, 4.0])
    a0, b0 = a.copy(), b.copy()
    for mode in MODES:
        got = _result(lambda: cv.convolve(a, b, mode), f"np.convolve(a, b, {mode!r})", f"mode={mode!r}")
        _float_array(got, np.convolve(a0, b0, mode).shape, f"convolve(a, b, {mode!r}) for two float arrays")
        assert np.array_equal(a, a0) and np.array_equal(b, b0), (
            f"expected a and b unchanged by convolve(a, b, {mode!r}), got a = {_show(a)} and b = {_show(b)} "
            "(never modify the arrays you receive: flip a copy)")
        got[:] = 99.0
        assert np.array_equal(a, a0) and np.array_equal(b, b0), (
            f"expected convolve(a, b, {mode!r}) to return a new array, but changing it changed a or b")


CONVOLVE_REFUSALS = [
    ([[1.5, -2.0], [3.0, 0.5]], [0.5, 2.0], "full", "a is 2-D"),
    ([4.0, -1.0, 2.5], [[0.5], [2.0]], "full", "b is 2-D"),
    ([], [0.5, 2.0], "full", "a is empty"),
    ([4.0, -1.0, 2.5], [], "valid", "b is empty"),
    (3.0, [0.5, 2.0], "full", "a is a number, not a 1-D sequence"),
    ([4.0, -1.0, 2.5], [0.5, 2.0], "fill", "the mode 'fill' does not exist"),
    ([4.0, -1.0, 2.5], [0.5, 2.0], "circular", "'circular' is not a mode of convolve"),
    ([4.0, -1.0, 2.5], [0.5, 2.0], None, "the mode None"),
]


@pytest.mark.parametrize("a, b, mode, why", CONVOLVE_REFUSALS,
                         ids=["a-two-d", "b-two-d", "a-empty", "b-empty", "a-scalar", "mode-fill", "mode-circular",
                              "mode-none"])
def test_convolve_refusals(cv, a, b, mode, why):
    _expect_error(ValueError, lambda: cv.convolve(a, b, mode), f"convolve({a!r}, {b!r}, mode={mode!r})", why)


# --- toeplitz_matrix ----------------------------------------------------------------------------------------------

def test_toeplitz_matrix_docstring_examples(cv):
    want = [[2, 0, 0], [1, 2, 0], [3, 1, 2], [0, 3, 1], [0, 0, 3]]
    got = _result(lambda: cv.toeplitz_matrix([2, 1, 3], 3), _show(want), "the kernel [2, 1, 3] and n = 3")
    _float_array(got, (5, 3), "toeplitz_matrix([2, 1, 3], 3) (n + k - 1 = 5 rows, n = 3 columns)")
    _close(got, want, "toeplitz_matrix([2, 1, 3], 3)", rtol=0, atol=0,
           hint="column j is the kernel shifted down by j")
    want = [[3, 2, 1, 0], [0, 3, 2, 1]]
    got = _result(lambda: cv.toeplitz_matrix([1, 2, 3], 4, mode="valid"), _show(want), "the mode 'valid'")
    _float_array(got, (2, 4), 'toeplitz_matrix([1, 2, 3], 4, mode="valid") (n - k + 1 = 2 rows)')
    _close(got, want, 'toeplitz_matrix([1, 2, 3], 4, mode="valid")', rtol=0, atol=0,
           hint="the rows k - 1, …, n - 1 of the full matrix, the same values as convolve(x, kernel, 'valid')")


TOEPLITZ_CASES = [(3, 6, "full"), (3, 6, "valid"), (3, 6, "same"), (4, 7, "full"), (4, 7, "valid"), (4, 7, "same"),
                  (2, 5, "same"), (6, 9, "same"), (5, 5, "valid"), (5, 5, "same"), (6, 2, "full"), (1, 4, "valid"),
                  (1, 4, "same"), (1, 1, "full")]


@pytest.mark.parametrize("k, n, mode", TOEPLITZ_CASES, ids=[f"{m}-k{k}-n{n}" for k, n, m in TOEPLITZ_CASES])
def test_toeplitz_matrix_matches_scipy_convolution_matrix(cv, k, n, mode):
    rng = np.random.default_rng(5443 + TOEPLITZ_CASES.index((k, n, mode)))
    kernel, x = rng.normal(size=k), rng.normal(size=n)
    want = convolution_matrix(kernel, n, mode)
    call = f"toeplitz_matrix(kernel, {n}, mode={mode!r}) for a kernel of length {k}"
    got = _result(lambda: cv.toeplitz_matrix(kernel, n, mode), f"a matrix of shape {want.shape}", call)
    _float_array(got, want.shape, call)
    _close(got, want, f"{call} (scipy.linalg.convolution_matrix)", rtol=0, atol=0,
           hint="column j is convolve(e_j, kernel, mode): the kernel shifted down by j, cut like convolve")
    _close(got @ x, np.convolve(x, kernel, mode), f"T @ x for {call}, which must equal np.convolve(x, kernel, "
                                                  f"{mode!r})", rtol=1e-10, atol=1e-12)


def test_toeplitz_matrix_full_mode_is_scipy_toeplitz(cv):
    """In the full mode, T is the Toeplitz matrix whose first column is the kernel followed by n - 1 zeros, and
    whose first row is (kernel[0], 0, …, 0)."""
    rng = np.random.default_rng(5458)
    for k, n in ((4, 3), (2, 6), (5, 5), (3, 1)):
        kernel = rng.normal(size=k)
        column = np.concatenate([kernel, np.zeros(n - 1)])
        row = np.concatenate([kernel[:1], np.zeros(n - 1)])
        want = toeplitz(column, row)
        got = _result(lambda: cv.toeplitz_matrix(kernel, n), f"a matrix of shape {want.shape}", f"k = {k}, n = {n}")
        _float_array(got, (n + k - 1, n), f"toeplitz_matrix(kernel, {n}) for a kernel of length {k}")
        _close(got, want, f"toeplitz_matrix(kernel, {n}) for k = {k} (scipy.linalg.toeplitz(column, row))", rtol=0,
               atol=0)


def test_toeplitz_matrix_columns_are_the_convolutions_of_the_basis_vectors(cv):
    """Column j is the convolution of e_j by the kernel; every diagonal is constant; at most k non-zero entries
    per column (a sparse matrix)."""
    kernel = np.array([0.5, -1.25, 2.0, 1.5])
    for n, mode in ((6, "full"), (6, "valid"), (6, "same"), (9, "same"), (2, "full")):
        T = _result(lambda: cv.toeplitz_matrix(kernel, n, mode), "a Toeplitz matrix", f"n = {n}, mode={mode!r}")
        rows = np.convolve(np.zeros(n), kernel, mode).size
        _float_array(T, (rows, n), f"toeplitz_matrix(kernel of length 4, {n}, {mode!r})")
        for j in range(n):
            _close(T[:, j], np.convolve(np.eye(n)[j], kernel, mode),
                   f"column {j} of toeplitz_matrix(kernel, {n}, {mode!r}), the convolution of e_{j}", rtol=0, atol=0)
        for offset in range(-rows + 1, n):
            diagonal = np.diagonal(T, offset=offset)
            assert np.all(diagonal == diagonal[0]), (
                f"expected each diagonal of T to be constant (T[i, j] depends only on i - j), got {_show(diagonal)} "
                f"on the diagonal j - i = {offset} for n = {n}, mode={mode!r}")
        counts = np.count_nonzero(T, axis=0)
        assert np.all(counts <= kernel.size), (
            f"expected at most {kernel.size} non-zero entries per column, got {counts.tolist()} for n = {n}, "
            f"mode={mode!r}")


def test_toeplitz_matrix_takes_integers_and_leaves_the_kernel_alone(cv):
    got = _result(lambda: cv.toeplitz_matrix([4, -5], np.int64(3), "same"), "[[4, 0, 0], [-5, 4, 0], [0, -5, 4]]",
                  "the integer kernel [4, -5], n = np.int64(3)")
    _float_array(got, (3, 3), "toeplitz_matrix([4, -5], np.int64(3), 'same') (a result of floats)")
    _close(got, [[4, 0, 0], [-5, 4, 0], [0, -5, 4]], "toeplitz_matrix([4, -5], 3, 'same')", rtol=0, atol=0,
           hint="for k = 2, 'same' keeps the full rows from (k - 1) // 2 = 0 on")
    kernel = np.array([1.5, -0.5, 2.0])
    k0 = kernel.copy()
    for mode in MODES:
        T = _result(lambda: cv.toeplitz_matrix(kernel, 5, mode), "a matrix", f"mode={mode!r}")
        _float_array(T, convolution_matrix(k0, 5, mode).shape, f"toeplitz_matrix(kernel of length 3, 5, {mode!r})")
        assert np.array_equal(kernel, k0), (
            f"expected the kernel unchanged by toeplitz_matrix(kernel, 5, {mode!r}), got {_show(kernel)}")
        T[:] = 99.0
        assert np.array_equal(kernel, k0), "expected a new matrix, but changing it changed the kernel"


TOEPLITZ_REFUSALS = [
    ([[0.5, -2.0]], 3, "full", "the kernel is 2-D"),
    ([], 3, "full", "the kernel is empty"),
    ([0.5, -2.0], 0, "full", "n = 0"),
    ([0.5, -2.0], -3, "full", "n < 0"),
    ([0.5, -2.0], 3.0, "full", "n = 3.0 is not an integer"),
    ([2.5], True, "full", "n = True: a bool is refused"),
    ([0.5, -2.0], "3", "full", "n is a string"),
    ([3.0, -1.5, 0.5], 2, "valid", "n = 2 < k = 3 in the mode 'valid'"),
    ([2.0, -1.0, 0.5, 1.5], 3, "same", "n = 3 < k = 4 in the mode 'same'"),
    ([0.5, -2.0], 3, "fill", "the mode 'fill' does not exist"),
]


@pytest.mark.parametrize("kernel, n, mode, why", TOEPLITZ_REFUSALS,
                         ids=["kernel-two-d", "kernel-empty", "n-zero", "n-negative", "n-float", "n-bool", "n-string",
                              "valid-n-below-k", "same-n-below-k", "mode-fill"])
def test_toeplitz_matrix_refusals(cv, kernel, n, mode, why):
    _expect_error(ValueError, lambda: cv.toeplitz_matrix(kernel, n, mode),
                  f"toeplitz_matrix({kernel!r}, {n!r}, mode={mode!r})", why)


# --- circular_convolve --------------------------------------------------------------------------------------------

def test_circular_convolve_docstring_examples(cv):
    got = _result(lambda: cv.circular_convolve([2, 5, 1, 3], [0, 1, 0, 0]), "[3, 2, 5, 1]", "a shift by one step")
    _float_array(got, (4,), "circular_convolve([2, 5, 1, 3], [0, 1, 0, 0])")
    _close(got, [3.0, 2.0, 5.0, 1.0], "circular_convolve([2, 5, 1, 3], [0, 1, 0, 0]) (a shift by one step)", rtol=0,
           atol=0, hint="index k receives a[k - 1], and index 0 receives a[n - 1]")
    got = _result(lambda: cv.circular_convolve([2, 0, 5], [1, 1, 0]), "[7, 2, 5]", "[2, 0, 5] and [1, 1, 0]")
    _float_array(got, (3,), "circular_convolve([2, 0, 5], [1, 1, 0])")
    _close(got, [7.0, 2.0, 5.0], "circular_convolve([2, 0, 5], [1, 1, 0])", rtol=0, atol=0)


@pytest.mark.parametrize("n", [1, 2, 3, 5, 8, 13])
def test_circular_convolve_matches_the_fft(cv, n):
    """The discrete Fourier transform turns a circular convolution into a product: ifft(fft(a) fft(b))."""
    rng = np.random.default_rng(5460 + n)
    a, b = rng.normal(size=n), rng.normal(size=n)
    want = np.real(np.fft.ifft(np.fft.fft(a) * np.fft.fft(b)))
    got = _result(lambda: cv.circular_convolve(a, b), f"{n} values", f"two random sequences of length {n}")
    _float_array(got, (n,), f"circular_convolve(a, b) for n = {n}")
    _close(got, want, f"circular_convolve(a, b) for n = {n} (np.fft)", rtol=1e-10, atol=1e-12,
           hint="Σ_i a[i] b[(k - i) mod n]: the index k - i read modulo n")


def test_circular_convolve_matches_scipy_circulant(cv):
    """circulant(b) is the matrix of a ↦ a ⊛ b: column j is b turned by j steps."""
    rng = np.random.default_rng(5474)
    for n in (4, 7, 10):
        a, b = rng.normal(size=n), rng.normal(size=n)
        for x, y, text in ((a, b, "circular_convolve(a, b)"), (b, a, "circular_convolve(b, a)")):
            got = _result(lambda: cv.circular_convolve(x, y), f"{n} values", f"{text}, n = {n}")
            _close(got, circulant(y) @ x, f"{text} for n = {n} (scipy.linalg.circulant)", rtol=1e-10, atol=1e-12)


def test_circular_convolve_is_the_full_convolution_wrapped_around(cv):
    """The full convolution has 2n - 1 values: its values n, …, 2n - 2 come back on the indices 0, …, n - 2."""
    rng = np.random.default_rng(5475)
    for n in (2, 5, 6):
        a, b = rng.normal(size=n), rng.normal(size=n)
        full = np.convolve(a, b)
        want = full[:n].copy()
        want[:n - 1] += full[n:]
        got = _result(lambda: cv.circular_convolve(a, b), f"{n} values", f"n = {n}")
        _close(got, want, f"circular_convolve(a, b) for n = {n}, the full convolution wrapped around", rtol=1e-12,
               atol=1e-12, hint="the full convolution cut to its first n values forgets the terms that wrap around")


def test_circular_convolve_shifts_and_commutes_with_every_circular_shift(cv):
    a = np.array([2.5, -1.0, 0.5, 4.0, -3.5, 1.5, 0.25])
    b = np.array([1.0, -2.0, 0.5, 0.0, 3.0, -0.5, 2.0])
    n = a.size
    for steps in range(n):
        impulse = np.eye(n)[steps]
        got = _result(lambda: cv.circular_convolve(a, impulse), f"a turned by {steps} steps", f"the impulse e_{steps}")
        _close(got, np.roll(a, steps), f"circular_convolve(a, e_{steps}), a turned by {steps} steps", rtol=0, atol=0,
               hint=f"index k receives a[(k - {steps}) mod n]")
    ab = _result(lambda: cv.circular_convolve(a, b), "a ⊛ b", "two sequences of length 7")
    for steps in range(1, n):
        got = _result(lambda: cv.circular_convolve(np.roll(a, steps), b), "(a ⊛ b) turned", f"a turned by {steps}")
        _close(got, np.roll(ab, steps), f"circular_convolve(a turned by {steps} steps, b), equal to a ⊛ b turned by "
                                        f"{steps} steps (equivariance)", rtol=1e-12, atol=1e-12)


def test_circular_convolve_takes_integers_and_leaves_its_inputs_alone(cv):
    got = _result(lambda: cv.circular_convolve([4, -1, 3], [3, 0, -1]), "[13, -6, 5]", "lists of integers")
    _float_array(got, (3,), "circular_convolve([4, -1, 3], [3, 0, -1]) (a result of floats)")
    _close(got, [13.0, -6.0, 5.0], "circular_convolve([4, -1, 3], [3, 0, -1])", rtol=0, atol=0)
    got = _result(lambda: cv.circular_convolve([-6], [0.5]), "[-3]", "n = 1")
    _float_array(got, (1,), "circular_convolve([-6], [0.5])")
    _close(got, [-3.0], "circular_convolve([-6], [0.5]) (n = 1: a product)", rtol=0, atol=0)
    a, b = np.array([1.5, -2.0, 0.5, 3.0]), np.array([0.25, 1.0, -1.0, 2.0])
    a0, b0 = a.copy(), b.copy()
    got = _result(lambda: cv.circular_convolve(a, b), "4 values", "two float arrays")
    _float_array(got, (4,), "circular_convolve of two float arrays of length 4")
    assert np.array_equal(a, a0) and np.array_equal(b, b0), (
        f"expected a and b unchanged by circular_convolve, got a = {_show(a)} and b = {_show(b)}")
    got[:] = 99.0
    assert np.array_equal(a, a0) and np.array_equal(b, b0), (
        "expected circular_convolve to return a new array, but changing it changed a or b")


CIRCULAR_REFUSALS = [
    ([4.0, -1.0, 2.5], [0.5, 2.0], "lengths 3 and 2"),
    ([0.5, 2.0], [4.0, -1.0, 2.5], "lengths 2 and 3"),
    ([], [], "two empty sequences"),
    ([[4.0, -1.0], [2.5, 0.5]], [[0.5, 2.0], [1.0, 3.0]], "2-D arrays"),
    (3.0, 2.0, "numbers, not 1-D sequences"),
]


@pytest.mark.parametrize("a, b, why", CIRCULAR_REFUSALS,
                         ids=["lengths-3-2", "lengths-2-3", "empty", "two-d", "scalars"])
def test_circular_convolve_refusals(cv, a, b, why):
    _expect_error(ValueError, lambda: cv.circular_convolve(a, b), f"circular_convolve({a!r}, {b!r})", why)


# --- equivalent_kernel --------------------------------------------------------------------------------------------

def _sliding(x, w, s):
    """The sliding sum of the libraries, y[i] = Σ_u w[u] x[s i + u], for every i where the window fits."""
    w = np.asarray(w, dtype=float)
    count = (len(x) - len(w)) // s + 1
    return np.array([float(np.dot(w, x[s * i:s * i + len(w)])) for i in range(max(count, 0))])


def _stack(x, kernels, strides):
    for w, s in zip(kernels, strides):
        x = _sliding(x, w, s)
    return x


def _field(lengths, strides):
    """1 + Σ_ℓ (k_ℓ - 1) s_1 ⋯ s_(ℓ-1), the length of the equivalent kernel."""
    return 1 + sum((k - 1) * math.prod(strides[:i]) for i, k in enumerate(lengths))


def _by_impulses(kernels, strides):
    """K[t] is the first output of the stack for the impulse e_t: z[0] = Σ_t K[t] x[t]."""
    size = _field([len(w) for w in kernels], strides)
    return np.array([_stack(np.eye(size)[t], kernels, strides)[0] for t in range(size)])


def _check_pair(got, length, what):
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (K, S) for {what}, got {type(got).__name__}"
    K, S = got
    _float_array(K, (length,), f"K for {what} (1 + Σ (k_ℓ - 1) s_1 ⋯ s_(ℓ-1) = {length} coefficients)")
    assert isinstance(S, int) and not isinstance(S, bool), (
        f"expected S as a Python int for {what}, got {type(S).__name__} {S!r}")
    return K, S


def test_equivalent_kernel_docstring_examples(cv):
    got = _result(lambda: cv.equivalent_kernel([[1, 1], [1, 1]]), "(array([1., 2., 1.]), 1)", "two sums of width 2")
    K, S = _check_pair(got, 3, "equivalent_kernel([[1, 1], [1, 1]])")
    _close(K, [1.0, 2.0, 1.0], "K for two sums of width 2", rtol=0, atol=0)
    assert S == 1, f"expected S = 1 (strides omitted: all equal to 1), got {S!r}"
    got = _result(lambda: cv.equivalent_kernel([[1, 1, 1], [1, -1]], strides=[2, 1]),
                  "(array([1., 1., 0., -1., -1.]), 2)", "[[1, 1, 1], [1, -1]] with strides [2, 1]")
    K, S = _check_pair(got, 5, "equivalent_kernel([[1, 1, 1], [1, -1]], strides=[2, 1])")
    _close(K, [1.0, 1.0, 0.0, -1.0, -1.0], "K for [[1, 1, 1], [1, -1]] with strides [2, 1]", rtol=0, atol=0,
           hint="K[t] = Σ over s_1 v + u = t of w_2[v] w_1[u]")
    assert S == 2, f"expected S = 2 · 1 = 2, got {S!r}"


# kernel lengths and strides of stacks; the kernels are random
STACKS = [([4], [3], "one stage: K is its kernel and S its step"),
          ([5, 4], [1, 1], "two stages of step 1"),
          ([4, 3], [2, 1], "a step 2, then a step 1"),
          ([2, 3, 2], [3, 2, 1], "three stages"),
          ([1, 4], [3, 2], "a kernel of length 1, then a kernel of length 4"),
          ([5, 1, 3], [1, 4, 1], "a kernel of length 1 with a step 4 in the middle"),
          ([3, 2, 2, 4], [2, 2, 1, 3], "four stages"),
          ([2, 2, 2], [2, 2, 2], "three windows of 2 with steps 2")]


@pytest.mark.parametrize("lengths, strides, text", STACKS, ids=[f"k{s[0]}-s{s[1]}" for s in STACKS])
def test_equivalent_kernel_matches_the_stack_applied_directly(cv, lengths, strides, text):
    """K is read on impulses (K[t] = z[0] for x = e_t), and the single sliding sum of step S gives the same values
    as the whole stack on a random signal."""
    rng = np.random.default_rng(5480 + STACKS.index((lengths, strides, text)))
    kernels = [rng.normal(size=k) for k in lengths]
    size = _field(lengths, strides)
    what = f"kernels of lengths {lengths} and strides {strides} ({text})"
    got = _result(lambda: cv.equivalent_kernel(kernels, strides), f"(K of length {size}, S = {math.prod(strides)})",
                  what)
    K, S = _check_pair(got, size, what)
    assert S == math.prod(strides), (
        f"expected S = {' · '.join(map(str, strides))} = {math.prod(strides)} for {what}, got {S}")
    _close(K, _by_impulses(kernels, strides), f"K for {what} (read on impulses)", rtol=1e-10, atol=1e-12,
           hint="stage ℓ reads x every s_1 ⋯ s_(ℓ-1) values: its kernel is spread by the product of the steps "
                "BEFORE it, then combined with K by a convolution")
    x = rng.normal(size=size + 23)
    _close(_sliding(x, K, S), _stack(x, kernels, strides),
           f"the single sliding sum z[j] = Σ_t K[t] x[S j + t], which must give the values of the stack for {what}",
           rtol=1e-10, atol=1e-12)


def test_equivalent_kernel_keeps_the_zeros(cv):
    """len(K) = 1 + Σ (k_ℓ - 1) s_1 ⋯ s_(ℓ-1), zeros included: a zero at an end of K is never trimmed."""
    for kernels, strides, want, S in (([[0, 3, 0, 0], [0, 1]], [4, 1], [0, 0, 0, 0, 0, 3, 0, 0], 4),
                                      ([[0.0, 0.0], [2.5]], [1, 1], [0, 0], 1),
                                      ([[4.0], [0.0, 0.0, 0.0, -1.0]], [3, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, -4], 6)):
        what = f"equivalent_kernel({kernels}, strides={strides})"
        got = _result(lambda: cv.equivalent_kernel(kernels, strides), _show(want), what)
        K, got_S = _check_pair(got, len(want), what)
        _close(K, want, what, rtol=0, atol=0, hint="zeros included, never trimmed")
        assert got_S == S, f"expected S = {S} for {what}, got {got_S}"


def test_equivalent_kernel_order_of_the_strides(cv):
    """The kernel of stage ℓ is spread by s_1 ⋯ s_(ℓ-1), not by its own step: swapping the steps changes K."""
    kernels = [[1.5, -1.0], [2.0, 0.5, 1.0]]
    for strides, want in (([3, 1], [3.0, -2.0, 0.0, 0.75, -0.5, 0.0, 1.5, -1.0]),
                          ([1, 3], [3.0, -1.25, 1.0, -1.0])):
        what = f"equivalent_kernel({kernels}, strides={strides})"
        got = _result(lambda: cv.equivalent_kernel(kernels, strides), _show(want), what)
        K, S = _check_pair(got, len(want), what)
        _close(K, want, what, rtol=0, atol=1e-15,
               hint="K[t] = Σ over s_1 v + u = t of w_2[v] w_1[u]: the second kernel is spread by s_1")
        assert S == 3, f"expected S = 3 for {what} (the product of all the steps), got {S}"


def test_equivalent_kernel_with_steps_one_is_the_full_convolution_of_the_kernels(cv):
    rng = np.random.default_rng(5490)
    kernels = [rng.normal(size=4), rng.normal(size=4), rng.normal(size=2)]
    want = np.convolve(np.convolve(kernels[0], kernels[1]), kernels[2])
    got = _result(lambda: cv.equivalent_kernel(kernels), "the full convolution of the three kernels",
                  "three kernels, strides omitted")
    K, S = _check_pair(got, want.size, "three kernels of lengths 4, 4, 2 with strides omitted")
    _close(K, want, "K for three kernels of step 1, the full convolution w_1 * w_2 * w_3", rtol=1e-12, atol=1e-12)
    assert S == 1, f"expected S = 1 when strides is omitted, got {S}"


def test_equivalent_kernel_returns_new_floats_and_a_python_int(cv):
    got = _result(lambda: cv.equivalent_kernel((np.array([2, -3]), (3, 1)), np.array([2, 2])), "(K, 4)",
                  "integer kernels and strides np.array([2, 2])")
    K, S = _check_pair(got, 4, "integer kernels (2, -3) and (3, 1) with strides np.array([2, 2])")
    _close(K, [6.0, -9.0, 2.0, -3.0], "K for the integer kernels (2, -3) and (3, 1) with strides [2, 2]", rtol=0,
           atol=0)
    assert S == 4, f"expected S = 4 (a Python int, even for strides given as a NumPy array), got {S!r}"
    w1, w2 = np.array([1.5, -0.5, 2.0, 0.75]), np.array([0.5, 4.0])
    c1, c2 = w1.copy(), w2.copy()
    for kernels, strides in (([w1], [1]), ([w1, w2], [4, 1])):
        got = _result(lambda: cv.equivalent_kernel(kernels, strides), "(K, S)", f"{len(kernels)} float kernel(s)")
        _check_pair(got, _field([len(w) for w in kernels], strides), f"{len(kernels)} float kernel(s)")
        assert np.array_equal(w1, c1) and np.array_equal(w2, c2), (
            f"expected the kernels unchanged by equivalent_kernel, got {_show(w1)} and {_show(w2)}")
        got[0][:] = 99.0
        assert np.array_equal(w1, c1) and np.array_equal(w2, c2), (
            f"expected K to be a new array (also for one stage), but changing it changed a kernel")


EQUIVALENT_REFUSALS = [
    ([], None, "no kernel"),
    ([[1.5, -1.0], []], None, "the second kernel is empty"),
    ([[[1.5, -1.0], [0.5, 2.0]]], None, "a 2-D kernel"),
    ([2.0, 3.0], None, "a list of numbers: each kernel must be a 1-D sequence"),
    ([[1.5, -1.0], [0.5, 2.0]], [2], "one stride for two kernels"),
    ([[1.5, -1.0], [0.5, 2.0]], [2, 1, 1], "three strides for two kernels"),
    ([[1.5, -1.0], [0.5, 2.0]], [0, 1], "a stride 0"),
    ([[1.5, -1.0], [0.5, 2.0]], [2, -1], "a negative stride"),
    ([[1.5, -1.0], [0.5, 2.0]], [1.5, 1], "a stride 1.5"),
    ([[1.5, -1.0], [0.5, 2.0]], [2.0, 1], "a stride 2.0 is a float, not an integer"),
    ([[1.5, -1.0], [0.5, 2.0]], [True, 2], "a stride True: a bool is refused"),
]


@pytest.mark.parametrize("kernels, strides, why", EQUIVALENT_REFUSALS,
                         ids=["no-kernel", "empty-kernel", "two-d-kernel", "numbers", "one-stride", "three-strides",
                              "stride-zero", "stride-negative", "stride-half", "stride-float", "stride-bool"])
def test_equivalent_kernel_refusals(cv, kernels, strides, why):
    _expect_error(ValueError, lambda: cv.equivalent_kernel(kernels, strides),
                  f"equivalent_kernel({kernels!r}, strides={strides!r})", why)


# --- separable_factors --------------------------------------------------------------------------------------------

def _check_factors(got, kernel, what, atol=None):
    """(u, v) with outer(u, v) = kernel (up to atol), ‖v‖ = 1, the first |v_j| > 1e-8 positive and u = kernel @ v."""
    kernel = np.asarray(kernel, dtype=float)
    p, q = kernel.shape
    assert isinstance(got, tuple) and len(got) == 2, (
        f"expected a tuple (u, v) for {what} (a kernel of rank 1), got {got!r}")
    u, v = got
    _float_array(u, (p,), f"u for {what}")
    _float_array(v, (q,), f"v for {what}")
    _close(np.outer(u, v), kernel, f"np.outer(u, v) for {what}, which must give back the kernel", rtol=1e-9,
           atol=1e-12 * max(1.0, float(np.max(np.abs(kernel)))) if atol is None else atol)
    norm = math.sqrt(float(np.sum(v * v)))
    assert math.isclose(norm, 1.0, rel_tol=1e-12), f"expected ‖v‖ = 1 for {what}, got ‖v‖ = {norm!r}"
    first = int(np.flatnonzero(np.abs(v) > 1e-8)[0])
    assert v[first] > 0, (
        f"expected the first coordinate of v with |v_j| > 1e-8 to be positive for {what}, got v = {_show(v)} "
        f"(v[{first}] = {v[first]:.6g} < 0: take -v, and u = kernel @ v)")
    _close(u, kernel @ v, f"u for {what}, which must be kernel @ v", rtol=1e-12, atol=1e-12)
    return u, v


def _expected_v(v0):
    v = np.asarray(v0, dtype=float) / math.sqrt(float(np.sum(np.square(v0))))
    first = int(np.flatnonzero(np.abs(v) > 1e-8)[0])
    return -v if v[first] < 0 else v


def test_separable_factors_docstring_examples(cv):
    got = _result(lambda: cv.separable_factors([[2, 1, -1], [4, 2, -2]]), "(u, v)", "[[2, 1, -1], [4, 2, -2]]")
    u, v = _check_factors(got, [[2, 1, -1], [4, 2, -2]], "[[2, 1, -1], [4, 2, -2]]")
    _close(v, np.array([2.0, 1.0, -1.0]) / math.sqrt(6), "v for [[2, 1, -1], [4, 2, -2]], (2, 1, -1) / √6")
    _close(u, [math.sqrt(6), 2 * math.sqrt(6)], "u for [[2, 1, -1], [4, 2, -2]], (√6, 2√6)")
    got = _result(lambda: cv.separable_factors([[0, 1, 0], [1, -4, 1], [0, 1, 0]]), "None",
                  "[[0, 1, 0], [1, -4, 1], [0, 1, 0]] (rank 2)")
    assert got is None, f"expected None for [[0, 1, 0], [1, -4, 1], [0, 1, 0]] (rank 2: not separable), got {got!r}"


RANK_ONE = [((1, 1), "a single number"), ((1, 4), "a single row"), ((5, 1), "a single column"),
            ((3, 3), "a 3 × 3 kernel"), ((4, 6), "a 4 × 6 kernel"), ((7, 2), "a 7 × 2 kernel")]


@pytest.mark.parametrize("shape, text", RANK_ONE, ids=[f"{s[0]}x{s[1]}" for s, _ in RANK_ONE])
def test_separable_factors_of_rank_one_kernels(cv, shape, text):
    rng = np.random.default_rng(5491 + RANK_ONE.index((shape, text)))
    for trial in range(4):
        u0, v0 = rng.normal(size=shape[0]), rng.normal(size=shape[1])
        kernel = np.outer(u0, v0)
        assert np.linalg.matrix_rank(kernel) == 1           # the oracle: a kernel of rank 1
        what = f"{text} of rank 1, np.outer(u0, v0) with v0 = {_show(v0)}"
        got = _result(lambda: cv.separable_factors(kernel), "(u, v)", what)
        u, v = _check_factors(got, kernel, what)
        _close(v, _expected_v(v0), f"v for {what}, v0 / ‖v0‖ up to its sign", rtol=1e-9, atol=1e-12)


def test_separable_factors_returns_none_for_a_rank_of_two_or_more(cv):
    rng = np.random.default_rng(5497)
    kernels = [rng.normal(size=(3, 3)), rng.normal(size=(4, 5)), rng.normal(size=(2, 6)),
               np.outer(rng.normal(size=4), rng.normal(size=4)) + np.outer(rng.normal(size=4), rng.normal(size=4)),
               np.array([[2.0, -1.0, 3.0], [4.0, -2.0, 6.0 + 1e-6]])]
    for kernel in kernels:
        rank = int(np.linalg.matrix_rank(kernel))
        assert rank >= 2                                     # the oracle
        got = _result(lambda: cv.separable_factors(kernel), "None", f"a kernel of rank {rank}")
        assert got is None, (
            f"expected None for a {kernel.shape[0]} × {kernel.shape[1]} kernel of rank {rank} "
            f"(np.linalg.matrix_rank), got {got!r}")


def _two_singular_values(s1, s2, seed):
    """A 4 × 3 kernel whose singular values are exactly s1 and s2 (orthonormal vectors from a QR)."""
    rng = np.random.default_rng(seed)
    P, _ = np.linalg.qr(rng.normal(size=(4, 2)))
    Q, _ = np.linalg.qr(rng.normal(size=(3, 2)))
    return s1 * np.outer(P[:, 0], Q[:, 0]) + s2 * np.outer(P[:, 1], Q[:, 1])


def test_separable_factors_tolerance_is_relative_to_the_first_singular_value(cv):
    """σ2 ≤ tol σ1, relative: a large kernel with σ2 = 1e-5 > 1e-10 but σ2 / σ1 = 1e-11 is separable; a tiny kernel
    with σ2 = 1e-12 < 1e-10 but σ2 / σ1 = 1e-6 is not."""
    hint = "the kernel counts as separable when its second singular value is at most tol times the FIRST one"
    big = _two_singular_values(1e6, 1e-5, 5498)
    got = _result(lambda: cv.separable_factors(big), "(u, v)", "σ1 = 1e6 and σ2 = 1e-5", hint)
    assert got is not None, f"expected (u, v) for σ1 = 1e6 and σ2 = 1e-5 (σ2 / σ1 = 1e-11 ≤ 1e-10), got None ({hint})"
    _check_factors(got, big, "σ1 = 1e6 and σ2 = 1e-5", atol=1e-4)      # outer(u, v) is big up to σ2
    tiny = _two_singular_values(1e-6, 1e-12, 5499)
    got = _result(lambda: cv.separable_factors(tiny), "None", "σ1 = 1e-6 and σ2 = 1e-12", hint)
    assert got is None, f"expected None for σ1 = 1e-6 and σ2 = 1e-12 (σ2 / σ1 = 1e-6 > 1e-10), got {got!r} ({hint})"
    middle = _two_singular_values(2.0, 2e-3, 5500)
    got = _result(lambda: cv.separable_factors(middle, tol=1e-2), "(u, v)", "σ2 / σ1 = 1e-3 with tol = 1e-2")
    assert got is not None, f"expected (u, v) for σ2 / σ1 = 1e-3 with tol = 1e-2, got None ({hint})"
    got = _result(lambda: cv.separable_factors(middle, tol=1e-4), "None", "σ2 / σ1 = 1e-3 with tol = 1e-4")
    assert got is None, f"expected None for σ2 / σ1 = 1e-3 with tol = 1e-4, got {got!r} ({hint})"


def test_separable_factors_with_tol_zero_accepts_an_exact_zero(cv):
    """With tol = 0, a second singular value exactly 0 is still « at most 0 times the first »."""
    kernel = [[0.0, 0.0, 0.0], [0.0, -2.5, 0.0]]
    got = _result(lambda: cv.separable_factors(kernel, tol=0), "(u, v) = ([0, -2.5], [0, 1, 0])",
                  "[[0, 0, 0], [0, -2.5, 0]] with tol = 0")
    u, v = _check_factors(got, kernel, "[[0, 0, 0], [0, -2.5, 0]] with tol = 0 (σ2 = 0 ≤ 0 · σ1)")
    _close(v, [0.0, 1.0, 0.0], "v for [[0, 0, 0], [0, -2.5, 0]]", rtol=0, atol=1e-15)
    _close(u, [0.0, -2.5], "u for [[0, 0, 0], [0, -2.5, 0]]", rtol=0, atol=1e-15)


def test_separable_factors_sign_convention(cv):
    """The first coordinate of v with |v_j| > 1e-8 is positive: not the largest one, and a smaller one counts as 0;
    the sign is fixed on v (u follows, u = kernel @ v)."""
    cases = [(np.outer([1.5, -2.0], [0.0, -3.0, 4.0]), [0.0, 0.6, -0.8], [-7.5, 10.0],
              "v0 = (0, -3, 4): the first coordinate is 0, the second decides"),
             (np.outer([2.0, 1.0], [-1e-12, 3.0, -4.0]), [0.0, 0.6, -0.8], [10.0, 5.0],
              "v0 = (-1e-12, 3, -4): |v_0| ≤ 1e-8 counts as zero, so v_1 > 0 decides"),
             (np.outer([-1.0, 3.0], [1.5, -2.0]), [0.6, -0.8], [-2.5, 7.5],
              "v0 = (1.5, -2): the first coordinate is positive, though smaller than |-2|")]
    for kernel, want_v, want_u, text in cases:
        got = _result(lambda: cv.separable_factors(kernel), "(u, v)", text)
        u, v = _check_factors(got, kernel, text)
        _close(v, want_v, f"v for {text}", rtol=1e-9, atol=1e-12)
        _close(u, want_u, f"u for {text}", rtol=1e-9, atol=1e-12)


def test_separable_factors_of_a_single_row_or_column(cv):
    for kernel, want_u, want_v, text in (([[0.0, -3.0, 4.0]], [-5.0], [0.0, 0.6, -0.8], "a single row"),
                                         ([[-2.0], [1.0], [0.5]], [-2.0, 1.0, 0.5], [1.0], "a single column"),
                                         ([[-3.0]], [-3.0], [1.0], "a single number")):
        got = _result(lambda: cv.separable_factors(kernel), f"({want_u}, {want_v})", f"{text} {kernel}")
        u, v = _check_factors(got, kernel, f"{text} {kernel} (always separable)")
        _close(v, want_v, f"v for {text} {kernel}", rtol=1e-12, atol=1e-15)
        _close(u, want_u, f"u for {text} {kernel}", rtol=1e-12, atol=1e-15)


def test_separable_factors_takes_integers_and_leaves_the_kernel_alone(cv):
    got = _result(lambda: cv.separable_factors([[3, -6], [-2, 4]]), "(u, v)", "the integers [[3, -6], [-2, 4]]")
    u, v = _check_factors(got, [[3, -6], [-2, 4]], "[[3, -6], [-2, 4]]")
    _close(v, np.array([1.0, -2.0]) / math.sqrt(5), "v for [[3, -6], [-2, 4]], (1, -2) / √5")
    _close(u, np.array([15.0, -10.0]) / math.sqrt(5), "u for [[3, -6], [-2, 4]], (15, -10) / √5")
    kernel = np.array([[2.0, -1.0, 4.0], [-4.0, 2.0, -8.0]])
    k0 = kernel.copy()
    got = _result(lambda: cv.separable_factors(kernel), "(u, v)", "a float kernel of rank 1")
    _check_factors(got, k0, "the float kernel [[2, -1, 4], [-4, 2, -8]] of rank 1")
    assert np.array_equal(kernel, k0), f"expected the kernel unchanged by separable_factors, got {_show(kernel)}"
    got[0][:] = 99.0
    got[1][:] = 99.0
    assert np.array_equal(kernel, k0), "expected u and v to be new arrays, but changing them changed the kernel"
    column = np.array([[1.5], [-0.5]])
    got = _result(lambda: cv.separable_factors(column), "(u, v)", "a single column")
    _check_factors(got, [[1.5], [-0.5]], "the single column [[1.5], [-0.5]]")
    got[0][:] = 99.0
    assert np.array_equal(column, [[1.5], [-0.5]]), (
        "expected u to be a new array for a single column, but changing it changed the kernel")


SEPARABLE_REFUSALS = [
    ([0.5, -2.0, 1.0], 1e-10, "a 1-D kernel"),
    (np.ones((2, 2, 2)), 1e-10, "a 3-D kernel"),
    (np.zeros((0, 3)), 1e-10, "an empty kernel"),
    ([[0.0, 0.0], [0.0, 0.0]], 1e-10, "a kernel identically zero"),
    ([[0, 0, 0]], 1e-10, "a single row of zeros"),
    ([[2.0, 1.0], [4.0, 2.0]], -1e-6, "tol < 0"),
]


@pytest.mark.parametrize("kernel, tol, why", SEPARABLE_REFUSALS,
                         ids=["one-d", "three-d", "empty", "zero", "zero-row", "tol-negative"])
def test_separable_factors_refusals(cv, kernel, tol, why):
    _expect_error(ValueError, lambda: cv.separable_factors(kernel, tol=tol),
                  f"separable_factors({kernel!r}, tol={tol!r})", why)
