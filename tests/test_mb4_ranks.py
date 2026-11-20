"""Tests of mymath.ranks (chapter MB4): the rank factorization M = C F of a matrix through its pivot columns and the
non-zero rows of its reduced row echelon form, the Borda points of complete rankings, and the exact expected
reciprocal rank of the first relevant item in an order drawn at random.

Oracles: SymPy's ``Matrix.rref`` (pivot columns and reduced form, in exact rational arithmetic) for matrices of
integers or fractions; ``np.linalg.matrix_rank`` and ``np.linalg.svd`` (the rank, and the Eckart-Young bound on
‖M - C F‖_F when ``tol`` ignores a part of M), ``np.linalg.lstsq`` and ``np.linalg.solve`` (F as the coordinates of the
columns of M in the basis C) for matrices of floats; matrices built with known pivot columns and known coordinates. For
the Borda points, ``scipy.stats.rankdata`` of the marks the rankings come from, and the ranks read by ``np.argsort``.
For the mean reciprocal rank, the n! orders listed by ``itertools.permutations`` (small n), the sets of positions of
the relevant items listed by ``itertools.combinations``, the survival function P(R > j) = C(n - q, j) / C(n, j) in
``fractions``, and ``sympy.harmonic``. Never another function of yours.
Plus properties: for the factorization, C F = M, F equal to the identity in the pivot columns, a column that is a
combination of the columns before it is never a pivot, zero columns, row operations that keep F, full column and full
row rank, rank one, the transpose, partial pivoting, ``tol`` as an absolute threshold (« at most tol »), entries set to
0 at the end, a matrix of measurements whose rank is a numerical rank; for the Borda points, their total and their
bounds, unanimous judges, reversed rankings, judges added up or reordered, candidates renamed, an increasing
transformation of the marks; for the mean reciprocal rank, H_n / n and its bounds ln(n + 1) / n and (1 + ln n) / n,
q / n at depth 1, all items relevant, a depth that changes nothing, the directions of variation, large n in little time;
exact types, inputs left unchanged (floats that are not dyadic), lists, NumPy integers, and every refusal of the
docstrings. They describe the expected behaviour without showing the solution.

    pytest tests/test_mb4_ranks.py              # your code
    pytest tests/test_mb4_ranks.py --impl=ref   # the reference
"""

import ast
import inspect
import itertools
import math
import threading
import warnings
from collections import Counter
from fractions import Fraction

import numpy as np
import pytest
import sympy
from scipy import stats


@pytest.fixture
def ranks_module(mymath_module):
    """The module itself: for the tests that check that your functions never write into the arrays they receive, and
    for the check of what the module uses."""
    return mymath_module("ranks")


class _OnCopies:
    """The functions of the module, each called on copies of the NumPy arrays it receives. A function that writes into
    its inputs is then reported by the tests named …_not_modify_… (which call the module itself), instead of
    silently changing the arrays from which the other tests compute what they expect."""

    def __init__(self, module):
        self._module = module

    def __getattr__(self, name):
        function = getattr(self._module, name)

        def on_copies(*args, **kwargs):
            args = [a.copy() if isinstance(a, np.ndarray) else a for a in args]
            kwargs = {k: v.copy() if isinstance(v, np.ndarray) else v for k, v in kwargs.items()}
            return function(*args, **kwargs)

        return on_copies


@pytest.fixture
def rk(ranks_module):
    return _OnCopies(ranks_module)


def _text(hint):
    """A hint given as a text or as a function that computes it (only when a test fails)."""
    if not callable(hint):
        return hint
    try:
        return hint()
    except Exception:  # noqa: BLE001 - a hint must never hide the failure it explains
        return ""


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError (and any RuntimeWarning: a division by 0, an overflow…) being
    reported with what was expected first."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)
        try:
            return call()
        except NotImplementedError:
            raise                 # a function not written yet: ⏳
        except RuntimeWarning as warning:
            hint = _text(hint)
            pytest.fail(f"expected {expected}{' for ' + what if what else ''} without a RuntimeWarning, got "
                        f"RuntimeWarning: {warning}" + (f" ({hint})" if hint else ""))
        except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
            hint = _text(hint)
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
    pytest.fail(f"expected {what} to raise {error.__name__} ({why}), but it returned {_show_any(result)}")


_TOO_SLOW = []      # the first call that gave no result in time: the later calls fail at once instead of waiting


def _within(seconds, call, what, expected, hint=""):
    """_result(call, …) in a thread that is given `seconds` to answer: a result that never comes fails the test
    instead of blocking it (the thread is left to finish on its own, and every later call fails at once, so that the
    tests end quickly)."""
    if _TOO_SLOW:
        pytest.fail(f"expected {expected} for {what} in little time, but an earlier call, {_TOO_SLOW[0]}, gave no "
                    f"result after {seconds} s ({_text(hint)})")
    box = {}

    def target():
        try:
            box["value"] = _result(call, expected, what, hint)
        except BaseException as exc:  # noqa: BLE001 - re-raised in the test (⏳, or the failure of _result)
            box["error"] = exc

    thread = threading.Thread(target=target, daemon=True)
    thread.start()
    thread.join(seconds)
    if thread.is_alive():
        _TOO_SLOW.append(what)
        pytest.fail(f"expected {expected} for {what} in less than {seconds} s, got no result after {seconds} s "
                    f"({_text(hint)})")
    if "error" in box:
        raise box["error"]
    return box["value"]


def _show(v):
    """A short text for an array: more than 12 numbers show the first 12 (flattened), then « … »."""
    arr = np.asarray(v, dtype=float)
    if arr.size > 12:
        return np.array2string(arr.ravel()[:12], precision=6, suppress_small=True,
                               max_line_width=10_000).replace("]", " …]") + f" (shape {arr.shape})"
    return np.array2string(arr, precision=6, suppress_small=True, max_line_width=10_000).replace("\n", "")


def _show_any(v):
    """_show for something that may not be an array of numbers (a pair (C, F), a fraction…)."""
    if isinstance(v, tuple):
        return "(" + ", ".join(_show_any(x) for x in v) + ")"
    if isinstance(v, Fraction):
        return f"Fraction({v.numerator}, {v.denominator})"
    try:
        return _show(v) + (f" (dtype {v.dtype})" if isinstance(v, np.ndarray) else "")
    except (TypeError, ValueError):
        return repr(v)


def _same(got, value, rtol=1e-9, atol=1e-12):
    """Whether got equals value: same shape, finite entries close; nan or inf never equal anything."""
    try:
        g = np.asarray(got, dtype=float)
        v = np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        return False
    if g.shape != v.shape or not np.all(np.isfinite(g)):
        return False
    return bool(np.allclose(g, v, rtol=rtol, atol=atol))


def _gap(got, want):
    """Why got differs from want, in a few words."""
    try:
        g = np.asarray(got, dtype=float)
        w = np.asarray(want, dtype=float)
    except (TypeError, ValueError):
        return ""
    if g.shape != w.shape:
        return f" (shape {g.shape} instead of {w.shape})"
    if not np.all(np.isfinite(g)):
        return " (the result holds nan or inf)"
    if g.size:
        return f" (largest gap {float(np.max(np.abs(g - w))):.1e})"
    return ""


def _close(got, want, what, rtol=1e-9, atol=1e-12, hint=""):
    if _same(got, want, rtol, atol):
        return
    hint = _text(hint)
    pytest.fail(f"expected {what} = {_show(want)}, got {_show_any(got)}{_gap(got, want)}"
                + (f" ({hint})" if hint else ""))


def _first_match(got, want, candidates, rtol=1e-9, atol=1e-11):
    """The text of the first classic error whose value got matches (and that differs from the right value), or ""."""
    for value, text in candidates:
        if value is not None and not _same(value, want, rtol, atol) and _same(got, value, rtol, atol):
            return text
    return ""


def _rng(seed, case=None):
    """The generator of a test (seeds 7400 to 7490), one stream per case of a parametrized test."""
    return np.random.default_rng(seed if case is None else (seed, case))


# --- what the module may use ----------------------------------------------------------------------------------------

def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``svd`` (from numpy.linalg import svd) → "numpy.linalg.svd". Relative imports (from
    .matrices import rref) are your own modules."""
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


def _where(statement):
    return statement.name if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)) else "the module level"


def _uses(statements, names):
    """Each use of an imported name (or of a chain of attributes on it) in the statements: (where, dotted path), e.g.
    ("rank_factorization", "numpy.linalg.matrix_rank"); ``where`` is the top-level function, or "the module level"."""
    uses = []
    for statement in statements:
        inner = {id(node.value) for node in ast.walk(statement) if isinstance(node, ast.Attribute)}
        where = _where(statement)
        for node in ast.walk(statement):
            if not isinstance(node, (ast.Name, ast.Attribute)) or id(node) in inner:
                continue                                  # only the whole chain numpy.linalg.svd
            attrs = []
            while isinstance(node, ast.Attribute):
                attrs.append(node.attr)
                node = node.value
            if isinstance(node, ast.Name) and node.id in names:
                uses.append((where, ".".join([names[node.id]] + attrs[::-1])))
    return uses


FORBIDDEN_STRINGS = {"linalg", "matrix_rank", "svd", "lstsq", "pinv", "rankdata", "permutations"}
FORBIDDEN_MODULES = ("scipy", "sympy", "numpy.linalg")
NO_SORT = {"argsort", "lexsort"}


def _string_uses(statements, forbidden):
    """getattr(np, "linalg") and the like, and __import__("scipy") or importlib.import_module("numpy.linalg"): a
    forbidden name reached through a string."""
    found = []
    for statement in statements:
        where = _where(statement)
        for node in ast.walk(statement):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            name = func.id if isinstance(func, ast.Name) else func.attr if isinstance(func, ast.Attribute) else ""
            texts = [a.value for a in node.args if isinstance(a, ast.Constant) and isinstance(a.value, str)]
            if name == "getattr" and any(t in forbidden for t in texts):
                found.append(f"getattr(…, {next(t for t in texts if t in forbidden)!r}) in {where}")
            if name in ("__import__", "import_module") and any(t.startswith(FORBIDDEN_MODULES) for t in texts):
                found.append(f"{name}({texts[0]!r}) in {where}")
    return found


def _borda_scope(tree):
    """The statements that borda_scores runs: its own definition, the top-level functions it reaches (directly or
    through other helpers), and the module level (an alias defined there)."""
    functions = {s.name: s for s in tree.body if isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef))}
    if "borda_scores" not in functions:
        return [s for s in tree.body if not isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef))]
    reached, todo = set(), ["borda_scores"]
    while todo:
        name = todo.pop()
        if name in reached:
            continue
        reached.add(name)
        for node in ast.walk(functions[name]):
            if isinstance(node, ast.Name) and node.id in functions and node.id not in reached:
                todo.append(node.id)
    return [s for s in tree.body if not isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef)) or s.name in reached]


def test_module_uses_numpy_but_no_linalg_scipy_sympy_nor_argsort_in_borda(ranks_module):
    """The docstring allows NumPy (@ included), but nothing from np.linalg (matrix_rank, svd, qr, lstsq, solve, inv,
    pinv), no SciPy (scipy.linalg, scipy.stats.rankdata) and no SymPy: the tests compare your results with them. In
    borda_scores (and the helpers it calls), neither np.argsort nor np.lexsort (nor the method .argsort()): you invert
    each ranking yourself. And random_ranking_mrr never lists the n! orders: itertools.permutations is an oracle of the
    tests. Your own modules (from .matrices import rref) are allowed. Only the code counts: a comment, a docstring or
    an import never used is not a use."""
    try:
        tree = ast.parse(inspect.getsource(ranks_module))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    names = _imported_names(tree)
    found = []
    for where, path in _uses(tree.body, names):
        if path.startswith(FORBIDDEN_MODULES) or path == "itertools.permutations":
            found.append(f"{path} in {where}")
    found += _string_uses(tree.body, FORBIDDEN_STRINGS)
    scope = _borda_scope(tree)
    for where, path in _uses(scope, names):
        if path.split(".")[-1] in NO_SORT:
            found.append(f"{path} in {where} (reached by borda_scores)")
    for statement in scope:
        for node in ast.walk(statement):
            if isinstance(node, ast.Attribute) and node.attr in NO_SORT and not (
                    isinstance(node.value, ast.Name) and node.value.id in names):
                found.append(f".{node.attr} in {_where(statement)} (reached by borda_scores)")
    found += [f"{text} (reached by borda_scores)" for text in _string_uses(scope, NO_SORT)]
    assert not found, (f"expected NumPy only, with nothing from np.linalg, no SciPy, no SymPy, no "
                       f"itertools.permutations, and no argsort nor lexsort in borda_scores, found "
                       f"{sorted(set(found))} "
                       f"(the tests compare your results with them: the rref of M09a, np.arange, fancy indexing, "
                       f"np.sum, math.comb and fractions.Fraction are enough)")


# --- rank_factorization ---------------------------------------------------------------------------------------------

RF_HINT = ("reduce a float copy of M as rref does in M09a (column by column from the left, partial pivoting: the "
           "entry of largest absolute value at or below the current row; a column whose candidates are all at most "
           "tol in absolute value has no pivot; at the end, the entries at most tol set to 0), and keep its pivot "
           "columns; then C = those columns of M itself, not of the reduced form, and F = the first r rows of the "
           "reduced form, r the number of pivots")


def _floats(M):
    return np.array(M, dtype=float)


def _rf(rk, M, what, tol=None):
    """rank_factorization(M) (with tol when it is given), its type and shapes checked: (C, F)."""
    call = (lambda: rk.rank_factorization(M)) if tol is None else (lambda: rk.rank_factorization(M, tol=tol))
    got = _result(call, "a tuple (C, F) of two arrays of floats", what, RF_HINT)
    if not (isinstance(got, tuple) and len(got) == 2):
        pytest.fail(f"expected {what} to return a tuple (C, F) of two numpy.ndarray, got {type(got).__name__} "
                    f"{_show_any(got)} ({RF_HINT})")
    C, F = got
    m, n = _floats(M).shape
    for name, arr in (("C", C), ("F", F)):
        if not (isinstance(arr, np.ndarray) and arr.dtype.kind == "f" and arr.ndim == 2):
            pytest.fail(f"expected {name} of {what} as a 2-D numpy.ndarray of floats, got {type(arr).__name__} "
                        + (f"of dtype {arr.dtype} and shape {arr.shape}" if isinstance(arr, np.ndarray) else repr(arr))
                        + f" ({RF_HINT})")
    if C.shape[0] != m or F.shape[1] != n or C.shape[1] != F.shape[0]:
        pytest.fail(f"expected C of shape (m, r) = ({m}, r) and F of shape (r, n) = (r, {n}), with the same r, for "
                    f"{what}, got C of shape {C.shape} and F of shape {F.shape} ({RF_HINT}"
                    + ("; F keeps the r non-zero rows only" if F.shape[0] == m and C.shape[1] != m else "") + ")")
    return C, F


def _rf_hint(C, F, A, pivots):
    """RF_HINT, with the classic error that (C, F) matches, if any."""
    m, n = A.shape
    r = len(pivots)
    if C.shape != (m, r) or F.shape != (r, n):
        return RF_HINT
    in_reduced_form = np.zeros((m, r))
    in_reduced_form[np.arange(r), np.arange(r)] = 1.0
    text = _first_match(C, A[:, list(pivots)], [
        (in_reduced_form, "C is taken in the reduced form, where the pivot columns are e_1, …, e_r: take the pivot "
                          "columns of M itself, otherwise C F is not M"),
        (A[:, :r], "C holds the first r columns of M, not its pivot columns")], rtol=1e-12, atol=1e-12)
    if not text and m >= r:
        text = _first_match(F, None, [(A[:r], "F is made of rows of the reduced form of M, not of rows of M")])
    return f"{RF_HINT}; here {text}" if text else RF_HINT


def _check_rf(C, F, M, pivots, what, F_want=None, rtol=1e-9, atol=1e-9, product_atol=None):
    """C = the columns `pivots` of M, F[:, pivots] = I_r, F = F_want and C F = M (within product_atol)."""
    A = _floats(M)
    m, n = A.shape
    r = len(pivots)
    hint = lambda: _rf_hint(C, F, A, pivots)                      # noqa: E731
    if C.shape[1] != r:
        pytest.fail(f"expected r = {r} pivots for {what} (its rank, numpy.linalg.matrix_rank; the pivot columns are "
                    f"{list(pivots)}), so C of shape ({m}, {r}) and F of shape ({r}, {n}), got C of shape {C.shape} "
                    f"and F of shape {F.shape} ({RF_HINT})")
    want_C = A[:, list(pivots)]
    if not np.array_equal(C, want_C):
        rounding = ("; C differs from them by rounding only: copy the columns of M itself, never from a matrix that "
                    "was divided and multiplied back" if _same(C, want_C, rtol=1e-12, atol=0) else "")
        pytest.fail(f"expected C = the columns {list(pivots)} of M itself (its pivot columns, as floats) for {what}, "
                    f"that is {_show(want_C)}, got {_show(C)}{_gap(C, want_C)} ({_text(hint)}{rounding})")
    _close(F[:, list(pivots)], np.eye(r), f"F[:, {list(pivots)}] for {what} (the identity I_{r} in the pivot columns)",
           rtol=0, atol=1e-12, hint=hint)
    if F_want is not None:
        _close(F, F_want, f"F for {what}", rtol=rtol, atol=atol, hint=hint)
    if product_atol is not None:
        _close(C @ F, A, f"C @ F for {what} (M itself)", rtol=0, atol=product_atol, hint=hint)


def _sympy_rref(M):
    """(pivots, F) of a matrix of integers or fractions by SymPy, exactly: the pivot columns, and the non-zero rows of
    the reduced row echelon form as floats."""
    R, pivots = sympy.Matrix(M).rref()
    r = len(pivots)
    return tuple(int(p) for p in pivots), np.array(R[:r, :].tolist(), dtype=float).reshape(r, R.shape[1])


def _leading_pivots(A, tol=None):
    """The pivot columns of a float matrix whose rank is clear, by np.linalg.matrix_rank: column j is a pivot when it
    raises the rank of the columns before it."""
    pivots, rank = [], 0
    for j in range(A.shape[1]):
        new = int(np.linalg.matrix_rank(A[:, :j + 1], tol=tol))
        if new > rank:
            pivots.append(j)
            rank = new
    return tuple(pivots)


def _describe(M, tol=None):
    return f"rank_factorization({_show(M)}" + ("" if tol is None else f", tol={tol!r}") + ")"


INTEGER_SHAPES = [(1, 3, 1), (2, 5, 2), (3, 3, 1), (3, 6, 2), (4, 4, 3), (5, 3, 2), (5, 7, 3), (6, 4, 4), (6, 8, 2),
                  (7, 6, 5), (8, 9, 4), (9, 5, 3)]


@pytest.mark.parametrize("m, n, r", INTEGER_SHAPES, ids=[f"{m}x{n}-rank{r}" for m, n, r in INTEGER_SHAPES])
def test_rank_factorization_of_integer_matrices_matches_sympy_rref(rk, m, n, r):
    """M = A B with small integers (A of r columns, B of r rows): the pivot columns and the reduced form of SymPy's
    Matrix.rref (exact), the rank of numpy.linalg.matrix_rank, C F = M."""
    rng = _rng(7400, INTEGER_SHAPES.index((m, n, r)))
    for k in range(3):
        A = rng.integers(-4, 5, size=(m, r))
        B = rng.integers(-3, 4, size=(r, n))
        if k == 2:
            B[:, rng.choice(n, size=min(2, n - 1), replace=False)] = 0      # zero columns too
        M = (A @ B).tolist()
        pivots, F_want = _sympy_rref(M)
        assert len(pivots) == np.linalg.matrix_rank(np.array(M, dtype=float)), "expected the two oracles to agree"
        what = _describe(M)
        C, F = _rf(rk, M, what)
        _check_rf(C, F, M, pivots, what, F_want, product_atol=1e-9)


PLANTED_SHAPES = [(2, 6, 1), (3, 7, 2), (5, 5, 2), (6, 9, 4), (8, 5, 3), (10, 12, 6), (12, 7, 7), (15, 20, 5)]


@pytest.mark.parametrize("m, n, r", PLANTED_SHAPES, ids=[f"{m}x{n}-rank{r}" for m, n, r in PLANTED_SHAPES])
def test_rank_factorization_of_float_matrices_of_a_planted_rank(rk, m, n, r):
    """M = A B with A (m × r) and B (r × n) drawn at random: r = numpy.linalg.matrix_rank(M) = the number of non-zero
    singular values (np.linalg.svd); F = the coordinates of the columns of M in the basis C (np.linalg.lstsq); C spans
    the column space of A and F the row space of B; C F = M."""
    rng = _rng(7401, PLANTED_SHAPES.index((m, n, r)))
    for k in range(3):
        A = rng.normal(size=(m, r)) * rng.uniform(0.5, 4.0)
        B = rng.normal(size=(r, n))
        M = A @ B
        s = np.linalg.svd(M, compute_uv=False)
        assert int(np.sum(s > 1e-9 * s[0])) == r == np.linalg.matrix_rank(M), "expected the planted rank"
        pivots = _leading_pivots(M)
        F_want = np.linalg.lstsq(M[:, list(pivots)], M, rcond=None)[0]
        what = _describe(M)
        C, F = _rf(rk, M, what)
        _check_rf(C, F, M, pivots, what, F_want, rtol=1e-8, atol=1e-8, product_atol=1e-9 * float(np.max(np.abs(M))))
        assert np.linalg.matrix_rank(np.hstack([C, A])) == r and np.linalg.matrix_rank(np.vstack([F, B])) == r, (
            f"expected the columns of C to span the column space of M, and the rows of F its row space, for {what} "
            f"({RF_HINT})")


PATTERNS = ["b b c", "z b c b", "b c c b z b", "b z z b c b c", "c? b b c b", "b b b b", "z z b", "b c b c b c b c"]


@pytest.mark.parametrize("pattern", PATTERNS, ids=[p.replace(" ", "").replace("?", "0") for p in PATTERNS])
def test_rank_factorization_columns_that_combine_earlier_columns_are_not_pivots(rk, pattern):
    """M is built column by column: « b » a new column of integers (independent of the columns before it), « c » a
    combination of the « b » columns before it with integer coefficients, « z » a zero column (« c? » first is a zero
    column too). The pivots are the « b » columns, C is made of them, and the column j of F holds the coefficients of
    the column j of M in the basis C (e_k for the k-th « b » column, 0 for a zero column)."""
    rng = _rng(7402, PATTERNS.index(pattern))
    kinds = pattern.split()
    r = kinds.count("b")
    m = r + int(rng.integers(0, 3))
    while True:
        basis = rng.integers(-5, 6, size=(m, r))
        if np.linalg.matrix_rank(basis) == r:
            break
    columns, coefficients, seen = [], [], 0
    for kind in kinds:
        coef = np.zeros(r, dtype=int)
        if kind == "b":
            coef[seen] = 1
            seen += 1
        elif kind == "c" and seen:
            coef[:seen] = rng.integers(-3, 4, size=seen)
            coef[seen - 1] = coef[seen - 1] or 2                       # never the zero combination
        columns.append(basis @ coef)
        coefficients.append(coef)
    M = np.column_stack(columns).astype(np.int64)
    F_want = np.column_stack(coefficients).astype(float)
    pivots = tuple(j for j, kind in enumerate(kinds) if kind == "b")
    assert _sympy_rref(M.tolist())[0] == pivots, "expected SymPy to find the « b » columns"
    what = _describe(M) + f" (columns {pattern!r})"
    C, F = _rf(rk, M, what)
    _check_rf(C, F, M, pivots, what, F_want, product_atol=1e-9)


def test_rank_factorization_row_operations_keep_the_pivots_and_f(rk):
    """Multiplying M on the left by an invertible matrix E (row operations) keeps its reduced form: the same pivots and
    the same F; C becomes E C (the pivot columns of E M)."""
    rng = _rng(7403)
    for k in range(6):
        m, n = int(rng.integers(3, 8)), int(rng.integers(4, 10))
        r = int(rng.integers(1, min(m, n) + 1))
        M = rng.normal(size=(m, r)) @ rng.normal(size=(r, n))
        pivots = _leading_pivots(M)
        F_want = np.linalg.lstsq(M[:, list(pivots)], M, rcond=None)[0]
        Q = np.linalg.qr(rng.normal(size=(m, m)))[0]
        E = Q @ np.diag(rng.uniform(1.0, 3.0, size=m) * rng.choice([-1.0, 1.0], size=m))
        EM = E @ M
        what = _describe(EM) + " (E M, for an invertible E)"
        C, F = _rf(rk, EM, what)
        _check_rf(C, F, EM, pivots, what, F_want, rtol=1e-8, atol=1e-8, product_atol=1e-9 * float(np.max(np.abs(EM))))


ZERO_SHAPES = [(1, 1), (1, 6), (5, 1), (4, 3), (6, 7)]


@pytest.mark.parametrize("m, n", ZERO_SHAPES, ids=[f"{m}x{n}" for m, n in ZERO_SHAPES])
def test_rank_factorization_of_a_zero_matrix_has_rank_0(rk, m, n):
    """A zero matrix (of integers, of floats, of -0.0, or whose entries are all at most tol): r = 0, C of shape
    (m, 0), F of shape (0, n), and C @ F is the (m, n) zero matrix."""
    rng = _rng(7404, ZERO_SHAPES.index((m, n)))
    small = rng.uniform(-1e-10, 1e-10, size=(m, n))
    for M, text in ((np.zeros((m, n), dtype=int).tolist(), "integers"), (np.zeros((m, n)), "floats"),
                    (-np.zeros((m, n)), "-0.0"), (small, "entries at most 1e-10, the default tol")):
        what = _describe(M) + f" ({text})"
        C, F = _rf(rk, M, what)
        if C.shape != (m, 0) or F.shape != (0, n):
            pytest.fail(f"expected r = 0 for {what}, so C of shape ({m}, 0) and F of shape (0, {n}), got shapes "
                        f"{C.shape} and {F.shape} ({RF_HINT})")
        _close(C @ F, np.zeros((m, n)), f"C @ F for {what} (the zero matrix)", rtol=0, atol=0)


def test_rank_factorization_full_column_rank_gives_c_equal_to_m_and_f_the_identity(rk):
    """Independent columns (m ≥ n, drawn at random): every column is a pivot, C = M and F = I_n."""
    rng = _rng(7405)
    for k in range(8):
        n = int(rng.integers(1, 7))
        m = n + int(rng.integers(0, 4))
        M = rng.normal(size=(m, n)) * 3.0
        what = _describe(M)
        C, F = _rf(rk, M, what)
        _check_rf(C, F, M, tuple(range(n)), what, np.eye(n), atol=1e-12, product_atol=1e-12)


def test_rank_factorization_full_row_rank_gives_f_by_solving_c_f_equal_m(rk):
    """Independent rows (m < n, drawn at random): r = m, C (m × m) is invertible and F is the solution of C F = M
    (np.linalg.solve)."""
    rng = _rng(7406)
    for k in range(8):
        m = int(rng.integers(1, 6))
        n = m + int(rng.integers(1, 5))
        M = rng.normal(size=(m, n)) * 2.0
        pivots = _leading_pivots(M)
        assert len(pivots) == m, "expected independent rows (the data of the test)"
        F_want = np.linalg.solve(M[:, list(pivots)], M)
        what = _describe(M)
        C, F = _rf(rk, M, what)
        _check_rf(C, F, M, pivots, what, F_want, rtol=1e-9, atol=1e-10, product_atol=1e-10)


def test_rank_factorization_of_rank_one_matrices(rk):
    """u vᵀ with u ≠ 0 (integers, some zero entries): r = 1, the pivot is the first column j with v_j ≠ 0, C is that
    column of M (v_j u) and F = vᵀ / v_j."""
    rng = _rng(7407)
    for k in range(8):
        m, n = int(rng.integers(2, 7)), int(rng.integers(2, 8))
        u = rng.integers(-6, 7, size=m)
        v = rng.integers(-6, 7, size=n)
        u[rng.integers(0, m)] = int(rng.integers(1, 7))
        v[: int(rng.integers(0, n))] = 0                               # leading zeros: the pivot moves right
        v[rng.integers(0, n)] = v[rng.integers(0, n)] or 5
        if not v.any():
            v[-1] = 3
        M = np.outer(u, v)
        j = int(np.nonzero(v)[0][0])
        what = _describe(M)
        C, F = _rf(rk, M, what)
        _check_rf(C, F, M, (j,), what, (v / v[j])[None, :], atol=1e-12, product_atol=1e-9)


def test_rank_factorization_of_one_row_or_one_column(rk):
    """A single row: its first entry larger than tol in absolute value is the pivot, F = the row divided by it (and its
    entries at most tol set to 0); a single column with an entry larger than tol: C = M and F = [[1.]]."""
    rng = _rng(7408)
    for k in range(5):
        n = int(rng.integers(3, 9))
        row = np.round(rng.normal(size=n) * 4.0, 3)
        lead = int(rng.integers(0, n - 1))
        row[:lead] = 0.0
        if k % 2:
            row[:lead] = rng.uniform(-9e-11, 9e-11, size=lead)          # below the default tol: no pivot either
        row[lead] = row[lead] if abs(row[lead]) > 0.5 else 2.375
        F_want = row / row[lead]
        F_want[np.abs(F_want) <= 1e-10] = 0.0
        what = _describe([row.tolist()])
        C, F = _rf(rk, [row.tolist()], what)
        _check_rf(C, F, [row.tolist()], (lead,), what, F_want[None, :], rtol=1e-14, atol=0)
        m = int(rng.integers(2, 8))
        column = np.round(rng.normal(size=(m, 1)) * 5.0, 2)
        column[0, 0] = column[0, 0] or 1.25
        what = _describe(column)
        C, F = _rf(rk, column, what)
        _check_rf(C, F, column, (0,), what, np.ones((1, 1)), atol=1e-15, product_atol=1e-14)


TINY_CASES = [(2.0e-10, 5e-11), (3.5e-10, 2e-11), (8.0e-10, 9e-11), (1.25e-10, 6e-11)]


@pytest.mark.parametrize("eps, delta", TINY_CASES, ids=[f"eps{e:.2e}" for e, _ in TINY_CASES])
def test_rank_factorization_uses_partial_pivoting(rk, eps, delta):
    """M = [[ε, ε t + δ, a], [1, t, b]] with tol < ε and δ < tol: the first column is (ε, 1)ᵀ, so partial pivoting takes
    the row [1, t, b] as the first pivot row; what is left of the second column is then δ ≤ tol (no pivot: the
    second column is t times the first, up to δ), and the third column has a pivot. A pivot ε chosen because it is the
    first entry above tol would leave -δ/ε, far above tol, and make the second column a pivot. As numpy.linalg.
    matrix_rank says, the first two columns have rank 1 for this tol."""
    rng = _rng(7409, TINY_CASES.index((eps, delta)))
    for k in range(3):
        t, a, b = float(rng.uniform(0.5, 3.0)), float(rng.uniform(2.0, 5.0)), float(rng.uniform(-1.0, 1.0))
        M = np.array([[eps, eps * t + delta, a], [1.0, t, b]])
        assert np.linalg.matrix_rank(M[:, :2], tol=1e-10) == 1 and np.linalg.matrix_rank(M) == 2, (
            "expected ranks 1 and 2 by numpy.linalg.matrix_rank (the data of the test)")
        what = _describe(M) + " (partial pivoting)"
        C, F = _rf(rk, M, what)
        _check_rf(C, F, M, (0, 2), what, np.array([[1.0, t, 0.0], [0.0, 0.0, 1.0]]), rtol=0, atol=1e-9,
                  product_atol=1e-9)


BOUNDARY_TOLS = [0.0025, 3e-7, 0.4]


@pytest.mark.parametrize("tau", BOUNDARY_TOLS, ids=[f"tol{t}" for t in BOUNDARY_TOLS])
def test_rank_factorization_an_entry_equal_to_tol_counts_as_zero(rk, tau):
    """« at most tol »: M = [[p, x, y], [0, τ, z]] with |z| > 1 > τ. With tol = τ, the candidate τ of the second column
    is at most tol: no pivot there, the pivots are (0, 2); with a tol just below τ, they are (0, 1). At the end, an
    entry of the reduced form equal to ±tol is set to 0."""
    rng = _rng(7410, BOUNDARY_TOLS.index(tau))
    for k in range(3):
        signs = rng.choice([-1.0, 1.0], size=4)
        p, x, y, z = (float(s * np.round(rng.uniform(low, high), 3))
                      for s, (low, high) in zip(signs, [(1.0, 2.0), (3.0, 6.0), (1.0, 6.0), (4.0, 9.0)]))
        M = np.array([[p, x, y], [0.0, tau, z]])
        what = _describe(M, tau)
        C, F = _rf(rk, M, what, tol=tau)
        # the pivot z divides its row: the entry τ / z (|z| > 1) is at most tol and set to 0 at the end
        F_want = np.array([[1.0, x / p - (y / p) * (tau / z), 0.0], [0.0, 0.0, 1.0]])
        _check_rf(C, F, M, (0, 2), what, F_want, rtol=1e-12, atol=1e-12)
        below = tau * (1 - 1e-6)
        what = _describe(M, below)
        C, F = _rf(rk, M, what, tol=below)
        F_want = np.array([[1.0, 0.0, (y - x * z / tau) / p], [0.0, 1.0, z / tau]])
        _check_rf(C, F, M, (0, 1), what, F_want, rtol=1e-9, atol=1e-12)
    # at the end too: in the reduced form of [[2, 2τ, -2τ, 7]], τ and -τ (exactly) are set to 0
    row = [[2.0, 2.0 * tau, -2.0 * tau, 7.0]]
    what = _describe(row, tau)
    C, F = _rf(rk, row, what, tol=tau)
    _check_rf(C, F, row, (0,), what, np.array([[1.0, 0.0, 0.0, 3.5]]), rtol=0, atol=0)


def test_rank_factorization_default_tol_is_1e_10(rk):
    """Without tol, an entry 1e-10 (= tol) counts as zero and an entry 1.5e-10 does not, as with tol=1e-10."""
    for tiny, pivots in ((1e-10, (0, 2)), (1.5e-10, (0, 1)), (9e-11, (0, 2))):
        M = np.array([[2.5, -1.75, 4.0], [0.0, tiny, -3.0]])
        for tol in (None, 1e-10):
            what = _describe(M, tol)
            C, F = _rf(rk, M, what, tol=tol)
            _check_rf(C, F, M, pivots, what)


def test_rank_factorization_tol_is_an_absolute_threshold(rk):
    """tol is compared with the absolute values of the entries, whatever the scale of M: M × 10⁻¹² (entries below
    1e-10) has rank 0 by default and its rank with tol=1e-26; M × 10⁵ keeps its rank with tol=1e-4; tol = 0 counts only
    the exact zeros; a tol above every entry, or inf, gives r = 0."""
    rng = _rng(7411)
    for k in range(4):
        m, n, r = int(rng.integers(3, 7)), int(rng.integers(3, 8)), int(rng.integers(1, 3))
        M = (rng.integers(-5, 6, size=(m, r)) @ rng.integers(-4, 5, size=(r, n))).astype(float)
        M[0, 0] = M[0, 0] or 7.0
        pivots, F_want = _sympy_rref(M.astype(int).tolist())
        small = M * 1e-12
        what = _describe(small)
        C, F = _rf(rk, small, what)
        if C.shape[1] != 0:
            pytest.fail(f"expected r = 0 for {what} (every entry is at most 1e-10 in absolute value: tol is absolute, "
                        f"not relative to the largest entry), got r = {C.shape[1]} ({RF_HINT})")
        what = _describe(small, 1e-26)
        C, F = _rf(rk, small, what, tol=1e-26)
        _check_rf(C, F, small, pivots, what, F_want, atol=1e-9)
        large = M * 1e5
        what = _describe(large, 1e-4)
        C, F = _rf(rk, large, what, tol=1e-4)
        _check_rf(C, F, large, pivots, what, F_want, atol=1e-9)
        for big in (float(np.max(np.abs(M))) * 1.5, math.inf):
            what = _describe(M, big)
            C, F = _rf(rk, M, what, tol=big)
            if C.shape != (m, 0) or F.shape != (0, n):
                pytest.fail(f"expected r = 0 for {what} (every entry is at most tol), got shapes {C.shape} and "
                            f"{F.shape} ({RF_HINT})")
    for tol in (0, 0.0):
        M = np.array([[3.0, 1.0, 2.0], [0.0, 2e-200, 0.0], [0.0, 0.0, 0.0]])
        what = _describe(M, tol)
        C, F = _rf(rk, M, what, tol=tol)
        _check_rf(C, F, M, (0, 1), what, np.array([[1.0, 0.0, 2.0 / 3.0], [0.0, 1.0, 0.0]]), atol=1e-15)


def test_rank_factorization_entries_at_most_tol_are_set_to_zero_at_the_end(rk):
    """An entry of the reduced form at most tol in absolute value is set to 0: F has an exact 0 there, and C F differs
    from M by exactly the part that this rank ignores."""
    rng = _rng(7412)
    for k in range(6):
        m, n = int(rng.integers(2, 5)), int(rng.integers(4, 8))
        r = m
        pivots = tuple(sorted(rng.choice(n, size=r, replace=False).tolist()))
        if pivots[0] != 0:
            pivots = (0,) + pivots[1:]
        F_want = np.zeros((r, n))
        for i, j in enumerate(pivots):
            F_want[i, j] = 1.0
            for later in range(j + 1, n):
                if later not in pivots:
                    F_want[i, later] = float(np.round(rng.normal() * 3.0, 2))
        ignored = np.zeros((r, n))
        free = [(i, j) for i in range(r) for j in range(n) if j not in pivots and j > pivots[i]]
        for i, j in [free[a] for a in rng.choice(len(free), size=min(2, len(free)), replace=False)]:
            ignored[i, j] = float(rng.uniform(2e-11, 9e-11)) * float(rng.choice([-1, 1]))
            F_want[i, j] = 0.0
        C_want = np.round(rng.normal(size=(m, r)) * 3.0, 1) + np.diag(np.full(r, 6.0))   # invertible
        M = C_want @ (F_want + ignored)
        if np.linalg.matrix_rank(M[:, list(pivots)]) < r:
            continue
        what = _describe(M)
        C, F = _rf(rk, M, what)
        _check_rf(C, F, M, pivots, what, F_want, rtol=0, atol=1e-9)
        zeros = (F_want == 0) & (np.abs(ignored) > 0)
        assert np.all(F[zeros] == 0.0), (
            f"expected exact zeros in F at {np.argwhere(zeros).tolist()} for {what} (entries of the reduced form at "
            f"most tol, set to 0 at the end), got {F[zeros].tolist()} ({RF_HINT})")
        _close(M - C @ F, C_want @ ignored, f"M - C @ F for {what} (the entries set to 0, times C: the part of M that "
               f"this rank ignores)", rtol=1e-3, atol=1e-12, hint=RF_HINT)


def test_rank_factorization_of_measurements_finds_a_numerical_rank(rk):
    """M = A B + noise (noise of size 10⁻⁷, A B of rank r): with tol = 1e-4, r is the number of singular values
    above tol (np.linalg.svd) and C F is only close to M: ‖M - C F‖_F is at least the Eckart-Young error of rank r,
    √(σ_{r+1}² + …), and of the order of the noise."""
    rng = _rng(7413)
    for k in range(6):
        m, n = int(rng.integers(4, 9)), int(rng.integers(5, 11))
        r = int(rng.integers(1, min(m, n)))
        A, B = rng.normal(size=(m, r)) * 2.0, rng.normal(size=(r, n))
        M = A @ B + rng.normal(size=(m, n)) * 1e-7
        s = np.linalg.svd(M, compute_uv=False)
        assert int(np.sum(s > 1e-4)) == r and np.linalg.matrix_rank(M) == min(m, n), (
            "expected r singular values above 1e-4 and a full rank by numpy (the data of the test)")
        pivots = _leading_pivots(M, tol=1e-4)
        what = _describe(M, 1e-4)
        C, F = _rf(rk, M, what, tol=1e-4)
        _check_rf(C, F, M, pivots, what, np.linalg.lstsq(M[:, list(pivots)], M, rcond=None)[0], rtol=0, atol=1e-4,
                  product_atol=1e-5)
        error = float(np.linalg.norm(M - C @ F))
        bound = float(np.sqrt(np.sum(s[r:] ** 2)))
        assert bound * (1 - 1e-9) <= error <= 1e-4, (
            f"expected ‖M - C F‖_F between the Eckart-Young error {bound:.3e} of rank {r} and 1e-4 for {what}, got "
            f"{error:.3e} ({RF_HINT})")


def test_rank_factorization_of_the_transpose_has_the_same_rank(rk):
    """rank(Mᵀ) = rank(M): the factorizations of M and of Mᵀ have the same r (SymPy's rank for both)."""
    rng = _rng(7414)
    for k in range(6):
        m, n, r = int(rng.integers(2, 8)), int(rng.integers(2, 8)), int(rng.integers(0, 4))
        M = rng.integers(-5, 6, size=(m, r)) @ rng.integers(-5, 6, size=(r, n)) if r else np.zeros((m, n), dtype=int)
        for X, text in ((M, "M"), (M.T, "Mᵀ")):
            pivots, F_want = _sympy_rref(X.tolist())
            what = _describe(X) + f" ({text})"
            C, F = _rf(rk, X, what)
            _check_rf(C, F, X, pivots, what, F_want, product_atol=1e-9)


ACCEPTED = [
    ([[3, 6, -1, 2], [1, 2, 0, 5]], "a list of lists of integers"),
    (((2, -1, 0), (6, -3, 1), (-4, 2, 5), (0, 0, 1)), "a tuple of tuples"),
    (np.array([[5, 0, 10], [-1, 4, -2]], dtype=np.int32), "an int32 array"),
    (np.array([[7, 14, 1], [3, 6, 2], [9, 18, 8]], dtype=np.uint8), "a uint8 array"),
    (np.array([[0.625, -1.25, 0.0], [1.5, -3.0, 0.875]], dtype=np.float32), "a float32 array"),
    ([[Fraction(1, 3), Fraction(2, 3), Fraction(5, 7)], [Fraction(-1, 2), Fraction(-1, 1), Fraction(4, 9)]],
     "fractions"),
    (np.array([[0.0, 2.0], [0.0, -5.0], [0.0, 1.0]]), "a first column of zeros"),
]


@pytest.mark.parametrize("M, text", ACCEPTED, ids=["int-lists", "tuples", "int32", "uint8", "float32", "fractions",
                                                   "zero-first-column"])
def test_rank_factorization_accepts_lists_integers_fractions_and_float32(rk, M, text):
    """Lists, tuples, NumPy integers, float32 and fractions are accepted; C and F are arrays of floats."""
    exact = [[Fraction(x) if not isinstance(x, (float, np.floating)) else Fraction(float(x)) for x in row]
             for row in np.array(M, dtype=object).tolist()]
    pivots, F_want = _sympy_rref(exact)
    what = _describe(M) + f" ({text})"
    C, F = _rf(rk, M, what)
    _check_rf(C, F, M, pivots, what, F_want, atol=1e-12, product_atol=1e-12)


def test_rank_factorization_does_not_modify_its_input(ranks_module):
    """Float arrays that are not dyadic (a division or a subtraction in place, even undone afterwards, would show),
    with row swaps (the largest entry of the first column is not on top), zero columns, and a Fortran-ordered copy."""
    rng = _rng(7415)
    for k in range(4):
        m, n, r = 5, 7, 3
        M = (rng.normal(size=(m, r)) * 3.7) @ (rng.normal(size=(r, n)) * 1.3)
        M[:, 4] = 0.0
        M[0, 0] = 0.1 * M[0, 0]
        for X in (M, np.asfortranarray(M), M.astype(np.float32)):
            copy = X.copy()
            for tol in (None, 1e-7):
                what = _describe(X, tol)
                call = (lambda: ranks_module.rank_factorization(X)) if tol is None else (
                    lambda: ranks_module.rank_factorization(X, tol=tol))
                _result(call, "a tuple (C, F)", what, RF_HINT)
                assert np.array_equal(X, copy), (
                    f"expected M unchanged by {what}, got M = {_show(X)} (largest change "
                    f"{float(np.max(np.abs(X - copy))):.1e}; never modify the array you receive: reduce a copy, "
                    f"np.array(M, dtype=float), not np.asarray, which returns the array itself)")


BAD_MATRICES = [
    ([1.0, 2.0, 3.0], "M is 1-D"), (np.ones((2, 2, 2)), "M is 3-D"), (4.5, "M is a number"), ([], "M is empty"),
    ([[]], "M has no column"), (np.zeros((0, 3)), "M has no row"), (np.zeros((3, 0)), "M has no column"),
    ([[1.0, np.nan], [0.625, 2.0]], "M holds nan"), ([[1.5, 2.0], [np.inf, 0.875]], "M holds inf"),
    ([[-np.inf, 1.0]], "M holds -inf"), ([[1.0, 2.0], [3.0]], "M is a ragged list"), (None, "M is None"),
    ([["a", 1.0], [2.0, 3.0]], "M holds a string"),
]


@pytest.mark.parametrize("M, why", BAD_MATRICES, ids=["one-d", "three-d", "number", "empty", "no-column", "no-row",
                                                      "no-column-array", "nan", "inf", "minus-inf", "ragged", "none",
                                                      "string"])
def test_rank_factorization_refuses_bad_matrices(rk, M, why):
    _expect_error(ValueError, lambda: rk.rank_factorization(M), f"rank_factorization({M!r})", why)


BAD_TOLS = [(-1e-12, "tol is negative"), (-1.0, "tol is -1"), (math.nan, "tol is nan"), (np.nan, "tol is np.nan"),
            (True, "tol is True, a bool"), (False, "tol is False, a bool"), (np.True_, "tol is np.True_, a NumPy bool")]


@pytest.mark.parametrize("tol, why", BAD_TOLS, ids=["negative", "minus-one", "nan", "numpy-nan", "true", "false",
                                                    "numpy-true"])
def test_rank_factorization_refuses_a_bad_tol(rk, tol, why):
    M = [[1.5, -2.0], [0.125, 4.0]]
    _expect_error(ValueError, lambda: rk.rank_factorization(M, tol=tol), f"rank_factorization({M!r}, tol={tol!r})",
                  why)


# --- borda_scores ---------------------------------------------------------------------------------------------------

BORDA_HINT = ("row i lists the candidates best first: the candidate rankings[i, p] (p from 0) is at rank p + 1 and "
              "gets n - 1 - p points; entry c of the result adds up the points of candidate c over the judges, as "
              "integers (a row is not the list of the ranks of the candidates: invert each ranking yourself)")


def _show_ints(R):
    """A short text for a table of integers: more than 12 numbers show the first 12 (flattened), then « … »."""
    arr = np.asarray(R)
    if arr.size > 12:
        return str(arr.ravel()[:12].tolist())[:-1] + f", …] (shape {arr.shape})"
    return str(arr.tolist())


def _borda_candidates(R):
    """The right points (ranks read by np.argsort) and the values of classic errors, with their explanation."""
    R = np.asarray(R)
    m, n = R.shape
    ranks = np.argsort(R, axis=1) + 1                     # ranks[i, c]: the rank of candidate c for judge i
    want = m * n - ranks.sum(axis=0)
    return want, [
        ((n - 1 - R).sum(axis=0), "you read row i as the list of the ranks of the candidates: R[i, p] is the candidate "
                                  "at position p, not the position of candidate p (invert each ranking)"),
        (ranks.sum(axis=0), "this is the sum of the ranks of each candidate; its Borda points are m n minus it"),
        (np.full(n, m) * (n - 1 - np.arange(n)), "the points go to the candidate R[i, p], not to the candidate p"),
    ]


def _borda_hint(got, R):
    try:
        want, candidates = _borda_candidates(R)
    except (TypeError, ValueError):
        return BORDA_HINT
    text = _first_match(got, want, candidates, rtol=0, atol=0)
    return f"{BORDA_HINT}; here {text}" if text else BORDA_HINT


def _borda(rk, R, what=None):
    """borda_scores(R), its type checked: a 1-D array of n integers."""
    what = what or f"borda_scores({_show_ints(R)})"
    got = _result(lambda: rk.borda_scores(R), "a numpy.ndarray of integers (the points of each candidate)", what,
                  BORDA_HINT)
    n = np.asarray(R).shape[1]
    if not (isinstance(got, np.ndarray) and got.dtype.kind in "iu" and got.shape == (n,)):
        pytest.fail(f"expected {what} as a numpy.ndarray of {n} integers (one per candidate), got "
                    f"{type(got).__name__}" + (f" of dtype {got.dtype} and shape {got.shape}"
                                               if isinstance(got, np.ndarray) else f" {got!r}") + f" ({BORDA_HINT})")
    return got


def _check_borda(got, want, R, what):
    if np.array_equal(got, want):
        return
    pytest.fail(f"expected {what} = {np.asarray(want).tolist()}, got {np.asarray(got).tolist()} "
                f"({_borda_hint(got, R)})")


def _rankings_from_marks(marks):
    """Each judge ranks the candidates by decreasing marks (no ties): the rankings, best first."""
    return np.argsort(-marks, axis=1, kind="stable")


def _is_involution(row):
    return np.array_equal(np.asarray(row)[np.asarray(row)], np.arange(len(row)))


def _shape(rng, judges, candidates):
    """(m, n) drawn in the two ranges, never 3 judges and 5 candidates (the shape of an exercise of the chapter)."""
    while True:
        m, n = int(rng.integers(*judges)), int(rng.integers(*candidates))
        if (m, n) != (3, 5):
            return m, n


MARK_SHAPES = [(1, 6), (2, 7), (4, 3), (5, 6), (6, 2), (7, 9), (12, 4), (25, 11)]


@pytest.mark.parametrize("m, n", MARK_SHAPES, ids=[f"{m}-judges-{n}-candidates" for m, n in MARK_SHAPES])
def test_borda_scores_from_marks_match_scipy_rankdata(rk, m, n):
    """Each judge gives marks (no ties) and ranks the candidates by decreasing marks; scipy.stats.rankdata of minus the
    marks gives the ranks, from 1, and the Borda points are m n minus the sum of the ranks of each candidate."""
    rng = _rng(7430, MARK_SHAPES.index((m, n)))
    for k in range(3):
        marks = rng.normal(size=(m, n)) * 4.0 + 10.0
        R = _rankings_from_marks(marks)
        if n >= 3 and all(_is_involution(row) for row in R):
            R[0] = np.roll(np.arange(n), 1)                              # one ranking that is not its own inverse
            marks[0] = n - np.argsort(R[0])
        want = (m * n - stats.rankdata(-marks, axis=1).sum(axis=0)).astype(int)
        what = f"borda_scores({_show_ints(R)})"
        _check_borda(_borda(rk, R, what), want, R, what)


def test_borda_scores_a_ranking_is_not_the_list_of_the_ranks(rk):
    """Rankings that are not their own inverse (the candidate at position p is not the candidate whose rank is p + 1):
    the points of a candidate come from its position in each row, read by np.argsort."""
    rng = _rng(7431)
    for k in range(8):
        m, n = _shape(rng, (1, 6), (3, 10))
        R = np.array([rng.permutation(n) for _ in range(m)])
        while _is_involution(R[0]):
            R[0] = rng.permutation(n)
        want, _ = _borda_candidates(R)
        what = f"borda_scores({R.tolist()})"
        _check_borda(_borda(rk, R, what), want, R, what)


def test_borda_scores_of_one_judge_are_n_minus_1_down_to_0(rk):
    """A single judge: the candidate at rank j gets n - j points, from n - 1 for the first to 0 for the last."""
    rng = _rng(7432)
    for n in (2, 3, 5, 8, 13, 21):
        row = rng.permutation(n)
        if n >= 3:
            while _is_involution(row):
                row = rng.permutation(n)
        want = np.zeros(n, dtype=int)
        want[row] = np.arange(n - 1, -1, -1)
        assert np.array_equal(want, n - stats.rankdata(np.argsort(row))), "expected the two oracles to agree"
        what = f"borda_scores([{row.tolist()}])"
        _check_borda(_borda(rk, [row.tolist()], what), want, [row], what)


def test_borda_scores_total_and_bounds(rk):
    """Every judge gives 0 + 1 + … + (n - 1) points: the total is m n (n - 1) / 2, and each candidate has between 0 and
    m (n - 1) points."""
    rng = _rng(7433)
    for k in range(10):
        m, n = _shape(rng, (1, 15), (1, 12))
        R = np.array([rng.permutation(n) for _ in range(m)])
        what = f"borda_scores({_show_ints(R)}) ({m} judges, {n} candidates)"
        got = _borda(rk, R, what)
        assert int(got.sum()) == m * n * (n - 1) // 2, (
            f"expected the points of {what} to add up to m n (n - 1) / 2 = {m * n * (n - 1) // 2}, got "
            f"{int(got.sum())} ({_borda_hint(got, R)})")
        assert got.min() >= 0 and got.max() <= m * (n - 1), (
            f"expected each candidate of {what} to have between 0 and m (n - 1) = {m * (n - 1)} points, got "
            f"{got.tolist()} ({_borda_hint(got, R)})")


def test_borda_scores_of_unanimous_judges(rk):
    """m judges who all give the same ranking: the candidate at rank j gets m (n - j) points, m (n - 1) for the first
    and 0 for the last."""
    rng = _rng(7434)
    for k in range(6):
        m, n = _shape(rng, (2, 9), (3, 9))
        row = rng.permutation(n)
        while _is_involution(row):
            row = rng.permutation(n)
        R = np.tile(row, (m, 1))
        want = np.zeros(n, dtype=int)
        want[row] = m * np.arange(n - 1, -1, -1)
        what = f"borda_scores({R.tolist()}) ({m} unanimous judges)"
        _check_borda(_borda(rk, R, what), want, R, what)


def test_borda_scores_reversed_rankings_give_m_n_minus_1_minus_the_points(rk):
    """Reversing every ranking (the last becomes the first) changes the points b into m (n - 1) - b."""
    rng = _rng(7435)
    for k in range(6):
        m, n = _shape(rng, (1, 8), (2, 10))
        R = np.array([rng.permutation(n) for _ in range(m)])
        want, _ = _borda_candidates(R)
        what = f"borda_scores({R[:, ::-1].tolist()}) (every ranking of {R.tolist()} reversed)"
        _check_borda(_borda(rk, np.ascontiguousarray(R[:, ::-1]), what), m * (n - 1) - want, R[:, ::-1], what)


def test_borda_scores_add_up_over_groups_of_judges_in_any_order(rk):
    """Two groups of judges together get the sum of their points; the order of the judges does not matter."""
    rng = _rng(7436)
    for k in range(6):
        n = int(rng.integers(3, 10))
        m1, m2 = int(rng.integers(1, 6)), int(rng.integers(1, 6))
        m2 += (n, m1 + m2) == (5, 3)                                     # never 3 judges and 5 candidates
        first = np.array([rng.permutation(n) for _ in range(m1)])
        second = np.array([rng.permutation(n) for _ in range(m2)])
        both = np.vstack([first, second])
        want = _borda_candidates(first)[0] + _borda_candidates(second)[0]
        what = f"borda_scores({both.tolist()}) (two groups of judges)"
        _check_borda(_borda(rk, both, what), want, both, what)
        shuffled = both[rng.permutation(len(both))]
        what = f"borda_scores({shuffled.tolist()}) (the same judges in another order)"
        _check_borda(_borda(rk, shuffled, what), want, shuffled, what)


def test_borda_scores_renaming_the_candidates_renames_the_points(rk):
    """If candidate c is renamed σ(c) in every ranking, its points become those of σ(c): b'[σ(c)] = b[c]."""
    rng = _rng(7437)
    for k in range(6):
        m, n = _shape(rng, (1, 7), (3, 10))
        R = np.array([rng.permutation(n) for _ in range(m)])
        sigma = rng.permutation(n)
        renamed = sigma[R]
        want = np.zeros(n, dtype=int)
        want[sigma] = _borda_candidates(R)[0]
        what = f"borda_scores({renamed.tolist()}) (the candidates of {R.tolist()} renamed by σ = {sigma.tolist()})"
        _check_borda(_borda(rk, renamed, what), want, renamed, what)


def test_borda_scores_an_increasing_transformation_of_the_marks_changes_nothing(rk):
    """Only the order chosen by each judge counts: marks changed by an increasing transformation (another scale, another
    unit: 7x + 3, eˣ, x³, ln(x + c)) give the same rankings, hence the same points (rankdata of the new marks)."""
    rng = _rng(7438)
    transformations = [(lambda x: 7.0 * x + 3.0, "7x + 3"), (np.exp, "eˣ"), (lambda x: x ** 3, "x³"),
                       (lambda x: np.log(x + 20.0), "ln(x + 20)")]
    for k in range(4):
        m, n = _shape(rng, (2, 7), (3, 9))
        marks = rng.uniform(-6.0, 6.0, size=(m, n))
        for f, name in transformations:
            changed = marks.copy()
            judge = int(rng.integers(0, m))
            changed[judge] = f(marks[judge])
            R = _rankings_from_marks(changed)
            want = (m * n - stats.rankdata(-changed, axis=1).sum(axis=0)).astype(int)
            assert np.array_equal(R, _rankings_from_marks(marks)), "expected the same rankings (the data of the test)"
            what = f"borda_scores({R.tolist()}) (the marks of judge {judge} changed by x ↦ {name})"
            _check_borda(_borda(rk, R, what), want, R, what)


def test_borda_scores_of_one_candidate_or_two(rk):
    """n = 1: every judge gives 0 point; n = 2: the first of each judge gets 1 point."""
    for m in (1, 4):
        R = [[0]] * m
        _check_borda(_borda(rk, R), np.zeros(1, dtype=int), R, f"borda_scores({R})")
    R = [[1, 0], [1, 0], [0, 1], [1, 0], [0, 1]]
    _check_borda(_borda(rk, R), np.array([2, 3]), R, f"borda_scores({R})")


@pytest.mark.parametrize("dtype", [np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16],
                         ids=["int8", "int16", "int32", "int64", "uint8", "uint16"])
def test_borda_scores_accepts_numpy_integer_arrays_lists_and_tuples(rk, dtype):
    """Every NumPy integer type is accepted, and lists and tuples of Python integers; the points are integers."""
    rng = _rng(7439, [np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16].index(dtype))
    m, n = _shape(rng, (2, 6), (3, 8))
    R = np.array([rng.permutation(n) for _ in range(m)], dtype=dtype)
    want, _ = _borda_candidates(R)
    for X, text in ((R, f"{np.dtype(dtype).name} array"), (R.tolist(), "list"),
                    (tuple(tuple(int(c) for c in row) for row in R), "tuple")):
        what = f"borda_scores({_show_ints(R)}) (a {text})"
        _check_borda(_borda(rk, X, what), want, R, what)


def test_borda_scores_of_many_judges_and_candidates(rk):
    """350 judges, 57 candidates: the same points as scipy.stats.rankdata of the marks."""
    rng = _rng(7440)
    marks = rng.normal(size=(350, 57))
    R = _rankings_from_marks(marks)
    want = (350 * 57 - stats.rankdata(-marks, axis=1).sum(axis=0)).astype(int)
    what = f"borda_scores({_show_ints(R)})"
    _check_borda(_borda(rk, R, what), want, R, what)


def test_borda_scores_does_not_modify_its_input(ranks_module):
    """int64 and int32 arrays (np.asarray returns them as they are): sorting a row in place, or writing into it, would
    show."""
    rng = _rng(7441)
    for dtype in (np.int64, np.int32, np.intp):
        R = np.array([rng.permutation(7) for _ in range(5)], dtype=dtype)
        copy = R.copy()
        what = f"borda_scores({R.tolist()})"
        _result(lambda: ranks_module.borda_scores(R), "the points", what, BORDA_HINT)
        assert np.array_equal(R, copy), (f"expected rankings unchanged by {what}, got {R.tolist()} (never modify the "
                                         f"array you receive: row.sort() or R[i] = … write into it)")


BAD_RANKINGS = [
    ([2, 0, 1], "rankings is 1-D (a single ranking must be [[2, 0, 1]])"), (np.zeros((2, 2, 2), dtype=int), "3-D"),
    (3, "rankings is a number"), ([], "rankings is empty"), ([[]], "no candidate"),
    (np.zeros((0, 4), dtype=int), "no judge"), ([[True, False], [False, True]], "an array of booleans"),
    (np.array([[1, 0]], dtype=bool), "a NumPy array of booleans"),
    ([[0.0, 1.0, 2.0]], "floats, even with integer values (2.0 is refused)"),
    (np.array([[2.0, 0.0, 1.0]]), "a float array"), ([[0, 1.0, 2]], "a float among integers"),
    ([[0, 2, 1], [1, 2, 3]], "the second row is not a permutation of 0, 1, 2 (3 is not a candidate)"),
    ([[0, 1, 2], [2, 2, 0]], "candidate 2 appears twice in a row (and 1 is missing)"),
    ([[1, 2, 3, 4]], "the candidates are numbered from 0, …, n - 1"), ([[0, -1, 1]], "-1 is not a candidate"),
    (np.array([[3, 1, 0, 255]], dtype=np.uint8), "255 is not a candidate"),
    ([[0, 1], [1]], "a ragged list"), (None, "None"), ([["0", "1"]], "strings"), ([[0j, 1]], "complex numbers"),
]


@pytest.mark.parametrize("rankings, why", BAD_RANKINGS,
                         ids=["one-d", "three-d", "number", "empty", "no-candidate", "no-judge", "bools",
                              "numpy-bools", "floats", "float-array", "mixed-float", "out-of-range", "repeated",
                              "from-one", "negative", "uint8-255", "ragged", "none", "strings", "complex"])
def test_borda_scores_refusals(rk, rankings, why):
    _expect_error(ValueError, lambda: rk.borda_scores(rankings), f"borda_scores({rankings!r})", why)


# --- random_ranking_mrr ---------------------------------------------------------------------------------------------

MRR_HINT = ("with q relevant items among n, P(R = j) = C(n - j, q - 1) / C(n, q) for j = 1, …, n - q + 1, the sum "
            "stopping at j = depth when depth is smaller; add up P(R = j) / j as a fractions.Fraction, with math.comb "
            "and Fraction(a, b), never a float; never list the n! orders nor the C(n, q) sets of positions")


MRR_SECONDS = 10       # a sum of at most n fractions takes milliseconds; listing the orders never ends


def _mrr(rk, n, q=None, depth=None, what=None, positional=False):
    """random_ranking_mrr(n[, n_relevant=q][, depth=depth]), its type and range checked: an exact Fraction in ]0, 1]."""
    if positional:
        call = lambda: rk.random_ranking_mrr(n, q, depth)                                    # noqa: E731
        what = what or f"random_ranking_mrr({n!r}, {q!r}, {depth!r})"
    else:
        kwargs = {**({} if q is None else {"n_relevant": q}), **({} if depth is None else {"depth": depth})}
        call = lambda: rk.random_ranking_mrr(n, **kwargs)                                    # noqa: E731
        what = what or "random_ranking_mrr(" + ", ".join([repr(n)] + [f"{k}={v!r}" for k, v in kwargs.items()]) + ")"
    got = _within(MRR_SECONDS, call, what, "an exact fractions.Fraction", MRR_HINT)
    if not isinstance(got, Fraction):
        pytest.fail(f"expected {what} as an exact fractions.Fraction, got {type(got).__module__}.{type(got).__name__} "
                    f"{got!r} ({MRR_HINT})")
    if not 0 < got <= 1:
        pytest.fail(f"expected {what} in ]0, 1] (an expected reciprocal rank, the first rank always counts), got "
                    f"{_show_any(got)} ({MRR_HINT})")
    return got


def _mrr_candidates(n, q, depth):
    """Values of classic errors, with their explanation."""
    last = n - q + 1 if depth is None else min(n - q + 1, depth)

    def total(stop, top=q - 1):
        return sum(Fraction(math.comb(n - j, top), j) for j in range(1, stop + 1)) / math.comb(n, q)

    return [
        (sum(Fraction(1, j) for j in range(1, n + 1)) / n, "this is H_n / n, the value for a single relevant item"),
        (total(n - q + 1) if depth is not None else None,
         "the sum stops at j = depth: a first relevant item after rank depth counts 0"),
        (total(last - 1) if last > 1 else None, "the last rank counts: j goes up to n - q + 1 (or to depth), included"),
        (total(last, q),
         "P(R = j) = C(n - j, q - 1) / C(n, q): one relevant item at rank j, the q - 1 others after it"),
    ]


def _check_mrr(got, want, n, q, depth, what):
    if got == want:
        return
    text = ""
    for value, explanation in _mrr_candidates(n, q, depth):
        if value is not None and value != want and value == got:
            text = explanation
            break
    pytest.fail(f"expected {what} = {_show_any(want)} ≈ {float(want):.10g}, got {_show_any(got)} ≈ {float(got):.10g} "
                f"({MRR_HINT}" + (f"; here {text}" if text else "") + ")")


def _survival_mrr(n, q, depth):
    """E[1/R; R ≤ depth] by the survival function: no relevant item among the first j has the probability
    S(j) = C(n - q, j) / C(n, j) (all j first items among the n - q others), and P(R = j) = S(j - 1) - S(j)."""
    last = n if depth is None else min(n, depth)
    total, S = Fraction(0), Fraction(1)
    for j in range(1, last + 1):
        S_next = S * Fraction(n - q - j + 1, n - j + 1) if j <= n - q else Fraction(0)
        total += (S - S_next) / j
        S = S_next
    return total


def _permutations_mrr(n, q, depth):
    """E[1/R; R ≤ depth] over the n! orders listed by itertools.permutations, the relevant items being 0, …, q - 1."""
    counts = Counter()
    for order in itertools.permutations(range(n)):
        R = next(j for j, item in enumerate(order, start=1) if item < q)
        counts[R] += 1
    last = n if depth is None else depth
    return sum(Fraction(c, R) for R, c in counts.items() if R <= last) / math.factorial(n)


def _combinations_mrr(n, q, depth):
    """E[1/R; R ≤ depth] over the C(n, q) sets of positions of the relevant items (itertools.combinations): R is the
    smallest position."""
    last = n if depth is None else depth
    counts = Counter(min(positions) for positions in itertools.combinations(range(1, n + 1), q))
    return sum(Fraction(c, R) for R, c in counts.items() if R <= last) / math.comb(n, q)


PERMUTATION_CASES = {
    1: [(1, None), (1, 1), (1, 3)],
    3: [(1, None), (1, 1), (1, 5), (2, None), (2, 1), (2, 2), (3, None), (3, 2)],
    5: [(1, None), (1, 2), (1, 3), (1, 7), (2, 2), (2, 3), (3, None), (3, 3), (4, None), (4, 2), (5, None), (5, 1)],
    6: [(1, None), (1, 3), (2, None), (2, 1), (3, None), (3, 2), (3, 3), (4, None), (4, 3), (5, 1), (6, 8)],
    7: [(1, None), (1, 1), (1, 2), (1, 3), (2, None), (2, 1), (2, 3), (3, None), (3, 1), (3, 2), (4, None), (4, 3),
        (5, None), (5, 2), (6, 1), (6, 9), (7, None)],
}


@pytest.mark.parametrize("n", sorted(PERMUTATION_CASES), ids=[f"n{n}" for n in sorted(PERMUTATION_CASES)])
def test_random_ranking_mrr_matches_the_n_factorial_orders(rk, n):
    """For small n, the mean of 1/R (0 after the depth) over the n! orders of itertools.permutations, exactly."""
    for q, depth in PERMUTATION_CASES[n]:
        want = _permutations_mrr(n, q, depth)
        got = _mrr(rk, n, q, depth)
        _check_mrr(got, want, n, q, depth, f"random_ranking_mrr({n}, n_relevant={q}, depth={depth}) (the {n}! orders)")


COMBINATION_CASES = [(9, 1, None), (9, 4, 3), (11, 2, None), (11, 6, 2), (12, 3, 5), (13, 5, None), (13, 9, 4),
                     (14, 7, None), (14, 2, 6), (15, 3, 11)]


@pytest.mark.parametrize("n, q, depth", COMBINATION_CASES, ids=[f"n{n}-q{q}-depth{d}" for n, q, d in COMBINATION_CASES])
def test_random_ranking_mrr_matches_the_sets_of_positions_of_the_relevant_items(rk, n, q, depth):
    """The q relevant items occupy q positions drawn uniformly among n: the mean of 1/R over the C(n, q) sets of
    positions (itertools.combinations), R the smallest of them."""
    want = _combinations_mrr(n, q, depth)
    _check_mrr(_mrr(rk, n, q, depth), want, n, q, depth,
               f"random_ranking_mrr({n}, n_relevant={q}, depth={depth}) (the {math.comb(n, q)} sets of positions)")


def test_random_ranking_mrr_matches_the_survival_function(rk):
    """P(R > j) = C(n - q, j) / C(n, j) (no relevant item among the first j), P(R = j) = P(R > j - 1) - P(R > j):
    the same exact value, for n up to 300."""
    rng = _rng(7465)
    for k in range(25):
        n = int(rng.integers(2, 301))
        q = int(rng.integers(1, n + 1)) if k % 3 else int(rng.integers(1, min(n, 6) + 1))
        depth = None if k % 4 == 0 else int(rng.integers(1, n + 3))
        want = _survival_mrr(n, q, depth)
        _check_mrr(_mrr(rk, n, q, depth), want, n, q, depth, f"random_ranking_mrr({n}, n_relevant={q}, depth={depth})")


HARMONIC_NS = [5, 7, 12, 31, 64, 250, 777]


@pytest.mark.parametrize("n", HARMONIC_NS, ids=[f"n{n}" for n in HARMONIC_NS])
def test_random_ranking_mrr_of_one_relevant_item_is_h_n_over_n(rk, n):
    """One relevant item: R is uniform on {1, …, n} and E[1/R] = H_n / n (sympy.harmonic); with depth k ≤ n, H_k / n."""
    want = Fraction(str(sympy.harmonic(n))) / n
    _check_mrr(_mrr(rk, n), want, n, 1, None, f"random_ranking_mrr({n}) (H_{n} / {n})")
    for k in sorted({2, 3, n // 2 + 1}):
        want = Fraction(str(sympy.harmonic(k))) / n
        _check_mrr(_mrr(rk, n, 1, k), want, n, 1, k, f"random_ranking_mrr({n}, n_relevant=1, depth={k}) "
                                                     f"(H_{k} / {n})")


def test_random_ranking_mrr_h_n_over_n_lies_between_the_rectangle_bounds(rk):
    """ln(n + 1) ≤ H_n ≤ 1 + ln n (rectangles under and over 1/x): E[1/R] for one relevant item lies between
    ln(n + 1) / n and (1 + ln n) / n."""
    for n in (1, 3, 17, 333, 1500):
        got = float(_mrr(rk, n))
        low, high = math.log(n + 1) / n, (1 + math.log(n)) / n
        assert low <= got <= high * (1 + 1e-15), (
            f"expected random_ranking_mrr({n}) between ln({n} + 1) / {n} = {low:.6g} and (1 + ln {n}) / {n} = "
            f"{high:.6g}, got {got:.10g} ({MRR_HINT})")


def test_random_ranking_mrr_with_every_item_relevant_is_1(rk):
    """q = n: the first item is relevant, R = 1, whatever the depth."""
    for n in (1, 2, 5, 9, 40):
        for depth in (None, 1, n + 3):
            _check_mrr(_mrr(rk, n, n, depth), Fraction(1), n, n, depth,
                       f"random_ranking_mrr({n}, n_relevant={n}, depth={depth}) (every item relevant)")


def test_random_ranking_mrr_at_depth_1_is_q_over_n(rk):
    """depth = 1: only R = 1 counts, and P(R = 1) = q / n."""
    for n, q in ((7, 3), (11, 4), (13, 6), (19, 2), (23, 17), (58, 7)):
        _check_mrr(_mrr(rk, n, q, 1), Fraction(q, n), n, q, 1,
                   f"random_ranking_mrr({n}, n_relevant={q}, depth=1) (P(R = 1) = q / n)")


def test_random_ranking_mrr_a_depth_beyond_the_last_possible_rank_changes_nothing(rk):
    """R ≤ n - q + 1 always: a depth ≥ n - q + 1, or above n, gives the value without depth."""
    rng = _rng(7461)
    for k in range(8):
        n = int(rng.integers(3, 58))
        q = int(rng.integers(1, n + 1))
        want = _survival_mrr(n, q, None)
        for depth in (n - q + 1, n - q + 2, n, n + 1, 10 * n):
            _check_mrr(_mrr(rk, n, q, depth), want, n, q, depth,
                       f"random_ranking_mrr({n}, n_relevant={q}, depth={depth}) (R ≤ n - q + 1 = {n - q + 1} always)")


def test_random_ranking_mrr_grows_with_q_and_the_depth_and_decreases_with_n(rk):
    """More relevant items bring the first one earlier (strictly larger for q < n); a larger depth counts more ranks
    (strictly, up to n - q + 1); more items push it later (strictly smaller for n + 1)."""
    rng = _rng(7462)
    for k in range(5):
        n = int(rng.integers(5, 40))
        values = [_mrr(rk, n, q) for q in range(1, n + 1)]
        assert all(a < b for a, b in zip(values, values[1:])), (
            f"expected random_ranking_mrr({n}, n_relevant=q) to grow strictly with q = 1, …, {n}, got "
            f"{[round(float(v), 6) for v in values]} ({MRR_HINT})")
        q = int(rng.integers(1, n))
        values = [_mrr(rk, n, q, depth) for depth in range(1, n - q + 2)]
        assert all(a < b for a, b in zip(values, values[1:])), (
            f"expected random_ranking_mrr({n}, n_relevant={q}, depth=k) to grow strictly with k = 1, …, {n - q + 1}, "
            f"got {[round(float(v), 6) for v in values]} ({MRR_HINT})")
        values = [_mrr(rk, size, q) for size in range(q + 11, q + 25)]
        assert all(a > b for a, b in zip(values, values[1:])), (
            f"expected random_ranking_mrr(n, n_relevant={q}) to decrease strictly with n = {q + 11}, …, {q + 24}, got "
            f"{[round(float(v), 6) for v in values]} ({MRR_HINT})")


def test_random_ranking_mrr_defaults_are_one_relevant_item_and_no_depth(rk):
    """random_ranking_mrr(n) is random_ranking_mrr(n, 1, None); depth=None explicitly means no depth; positional and
    keyword arguments give the same value."""
    for n, q in ((6, 1), (17, 1), (17, 5), (41, 13)):
        want = _survival_mrr(n, q, None)
        if q == 1:
            _check_mrr(_mrr(rk, n), want, n, 1, None, f"random_ranking_mrr({n})")
        _check_mrr(_mrr(rk, n, q), want, n, q, None, f"random_ranking_mrr({n}, n_relevant={q})")
        _check_mrr(_mrr(rk, n, q, None, positional=True), want, n, q, None, f"random_ranking_mrr({n}, {q}, None)")
        want = _survival_mrr(n, q, 3)
        _check_mrr(_mrr(rk, n, q, 3, positional=True), want, n, q, 3, f"random_ranking_mrr({n}, {q}, 3)")


@pytest.mark.parametrize("n, q, depth", [(np.int64(9), np.int32(3), np.int16(4)), (np.uint8(14), 2, None),
                                         (25, np.int64(25), np.uint16(30)), (np.int32(8), np.int8(1), 3)],
                         ids=["all-numpy", "uint8-n", "numpy-q-and-depth", "int8-q"])
def test_random_ranking_mrr_accepts_numpy_integers(rk, n, q, depth):
    want = _survival_mrr(int(n), int(q), None if depth is None else int(depth))
    _check_mrr(_mrr(rk, n, q, depth), want, int(n), int(q), depth,
               f"random_ranking_mrr({n!r}, n_relevant={q!r}, depth={depth!r}) (NumPy integers)")


LARGE_CASES = [(1500, 1, None), (1500, 2, 900), (2000, 40, None), (1800, 700, 3), (1200, 600, None)]


@pytest.mark.parametrize("n, q, depth", LARGE_CASES, ids=[f"n{n}-q{q}-depth{d}" for n, q, d in LARGE_CASES])
def test_random_ranking_mrr_of_large_n_is_exact_and_fast(rk, n, q, depth):
    """n in the thousands: listing the n! orders, or the C(n, q) sets of positions, never ends; a sum of at most n
    exact fractions takes a few milliseconds. The value is the exact one of the survival function."""
    what = f"random_ranking_mrr({n}, n_relevant={q}, depth={depth})"
    got = _within(2 * MRR_SECONDS, lambda: rk.random_ranking_mrr(n, n_relevant=q, depth=depth), what,
                  "an exact fractions.Fraction", MRR_HINT)
    if not isinstance(got, Fraction):
        pytest.fail(f"expected {what} as an exact fractions.Fraction, got {type(got).__name__} {got!r} ({MRR_HINT})")
    _check_mrr(got, _survival_mrr(n, q, depth), n, q, depth, what)


BAD_MRR = [
    ((0,), {}, "n = 0: no item"), ((-3,), {}, "n is negative"), ((6.0,), {}, "n is the float 6.0, not an integer"),
    ((np.float64(5.0),), {}, "n is np.float64(5.0)"), ((4.5,), {}, "n is 4.5"), ((True,), {}, "n is True, a bool"),
    ((np.True_,), {}, "n is np.True_, a NumPy bool"), (("6",), {}, "n is a string"), ((None,), {}, "n is None"),
    ((6,), {"n_relevant": 0}, "n_relevant = 0: no relevant item"), ((6,), {"n_relevant": 7}, "n_relevant > n"),
    ((6,), {"n_relevant": -2}, "n_relevant is negative"), ((6,), {"n_relevant": 2.0}, "n_relevant is the float 2.0"),
    ((6,), {"n_relevant": True}, "n_relevant is True, a bool"), ((6,), {"n_relevant": None}, "n_relevant is None"),
    ((6,), {"n_relevant": np.False_}, "n_relevant is np.False_, a NumPy bool"),
    ((6,), {"depth": 0}, "depth = 0: no item shown"), ((6,), {"depth": -1}, "depth is negative"),
    ((6,), {"depth": 3.0}, "depth is the float 3.0"), ((6,), {"depth": np.float32(2.0)}, "depth is np.float32(2.0)"),
    ((6,), {"depth": True}, "depth is True, a bool"), ((6,), {"depth": "3"}, "depth is a string"),
]


@pytest.mark.parametrize("args, kwargs, why", BAD_MRR,
                         ids=["n0", "n-negative", "n-float", "n-numpy-float", "n-half", "n-bool", "n-numpy-bool",
                              "n-string", "n-none", "q0", "q-above-n", "q-negative", "q-float", "q-bool", "q-none",
                              "q-numpy-bool", "depth0", "depth-negative", "depth-float", "depth-numpy-float",
                              "depth-bool", "depth-string"])
def test_random_ranking_mrr_refusals(rk, args, kwargs, why):
    shown = ", ".join([repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
    _expect_error(ValueError, lambda: rk.random_ranking_mrr(*args, **kwargs), f"random_ranking_mrr({shown})", why)
