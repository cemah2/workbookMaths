"""Tests of mymath.distances (chapter M27): the values of a matrix game in pure strategies, the optimal mixed strategies
and the value of a 2 × 2 game, the iterates of gradient descent-ascent on a bilinear game, and the 2-Wasserstein
distance between two normal laws on the line.

Oracles: the maximin and the minimax recomputed by loops over the rows and the columns, and the saddle points found
entry by entry; ``scipy.optimize.linprog`` for the value of a game and the optimal strategies (the linear program of
each player); the recurrence of the iterates recomputed in the test, the powers of the matrix of one step
(``np.linalg.matrix_power``), its determinant and its eigenvalues (``np.linalg.det``, ``np.linalg.eigvals``); the
integral of the squared gap between the two quantile functions (``scipy.integrate.quad`` and ``scipy.stats.norm.ppf``)
for W₂, and ``scipy.stats.wasserstein_distance`` on quantiles for W₁. Never another function of yours. Plus properties:
maximin ≤ minimax, equal exactly when the game has a saddle point (with integers as with floats), the smallest indices
of a tie, the value between the maximin and the minimax, moved to v + c by G + c and to k v by k G (k > 0), strategies
that make the opponent indifferent and guarantee the value, the pure strategies of a saddle point; the simultaneous
iterates that never get closer to the equilibrium (a step whose eigenvalues have a modulus > 1), the alternating step of
determinant 1 and the quantity it keeps; the symmetry of W₂, |Δμ| for equal standard deviations, standard deviations
and not variances, point masses, W₁ ≤ W₂, translations, scalings and the triangle inequality; inputs left unchanged,
Python floats and ints, arrays of floats, lists of integers, and the refusals of the docstrings. They describe the
expected behaviour without showing the solution.

    pytest tests/test_m27_distances.py              # your code
    pytest tests/test_m27_distances.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings

import numpy as np
import pytest
from scipy import integrate, optimize, stats


@pytest.fixture
def ds_module(mymath_module):
    """The module itself: for the tests that check that your functions never write into the arrays they receive, and
    for the check of what the module uses."""
    return mymath_module("distances")


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
def ds(ds_module):
    return _OnCopies(ds_module)


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
    pytest.fail(f"expected {what} to raise {error.__name__} ({why}), but it returned {_show_any(result)}")


def _show(v):
    """A short text for an array: more than 8 numbers show the first 8 (flattened), then « … »."""
    arr = np.asarray(v, dtype=float)
    if arr.size > 8:
        return np.array2string(arr.ravel()[:8], precision=6, suppress_small=True,
                               max_line_width=10_000).replace("]", " …]") + (
            f" (shape {arr.shape})")
    return np.array2string(arr, precision=6, suppress_small=True, max_line_width=10_000).replace("\n", "")


def _show_any(v):
    """_show for something that may not be an array of numbers (a tuple of arrays, a tuple of numbers…)."""
    if isinstance(v, tuple) and v and all(isinstance(e, np.ndarray) for e in v):
        return "(" + ", ".join(_show(e) for e in v) + ")"
    if isinstance(v, tuple):
        return "(" + ", ".join(f"{e:.10g}" if isinstance(e, float) else repr(e) for e in v) + ")"
    try:
        return _show(v)
    except (TypeError, ValueError):
        return repr(v)


def _float_array(got, shape, what, hint=""):
    assert isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape, (
        f"expected {what} as a numpy.ndarray of floats of shape {shape}, got {type(got).__name__}"
        + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray) else "")
        + (f" ({hint})" if hint else ""))


def _float(got, what):
    assert type(got) is float, (f"expected {what} as a Python float (float(...)), got "
                                f"{type(got).__module__}.{type(got).__name__} {got!r}")


def _int(got, what):
    assert type(got) is int, (f"expected {what} as a Python int (int(...)), got "
                              f"{type(got).__module__}.{type(got).__name__} {got!r}")


def _tuple(got, k, what, names):
    assert isinstance(got, tuple) and len(got) == k, (
        f"expected {what} to return a tuple of {k} items {names}, got {type(got).__name__}"
        + (f" of {len(got)} items" if isinstance(got, (tuple, list)) else f" {_show_any(got)}"))


def _close(got, want, what, rtol=1e-9, atol=1e-12, hint=""):
    got = np.asarray(got, dtype=float)
    want = np.asarray(want, dtype=float)
    assert got.shape == want.shape and np.allclose(got, want, rtol=rtol, atol=atol), (
        f"expected {what} = {_show(want)}, got {_show(got)}"
        + ("" if got.shape == want.shape else f" (shape {got.shape} instead of {want.shape})")
        + (f" ({hint})" if hint else ""))


def _matches(got, value, rtol=1e-9, atol=1e-11):
    """Whether the result got equals the value of a classic error (same shape, close)."""
    if value is None:
        return False
    try:
        got, value = np.asarray(got, dtype=float), np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        return False
    return got.shape == value.shape and bool(np.all(np.isfinite(value))) and np.allclose(got, value, rtol=rtol,
                                                                                         atol=atol)


def _first_match(got, want, candidates, rtol=1e-9, atol=1e-11):
    """The text of the first classic error whose value got matches (and that differs from the right value), or ""."""
    for value, text in candidates:
        if value is not None and not _matches(value, want, rtol, atol) and _matches(got, value, rtol, atol):
            return text
    return ""


# --- the oracles ----------------------------------------------------------------------------------------------------

def _pure_oracle(G):
    """(maximin, minimax, row, col) by loops: the first row whose minimum is the largest, the first column whose maximum
    is the smallest."""
    rows = [[float(v) for v in r] for r in np.asarray(G, dtype=float)]
    minima = [min(r) for r in rows]
    maxima = [max(r[j] for r in rows) for j in range(len(rows[0]))]
    maximin, minimax = max(minima), min(maxima)
    return maximin, minimax, minima.index(maximin), maxima.index(minimax)


def _saddle_points(G):
    """Every (i, j) whose entry is the smallest of its row and the largest of its column, found entry by entry."""
    G = np.asarray(G, dtype=float)
    return [(i, j) for i in range(G.shape[0]) for j in range(G.shape[1])
            if all(G[i, j] <= G[i, k] for k in range(G.shape[1])) and all(G[i, j] >= G[k, j]
                                                                          for k in range(G.shape[0]))]


def _lp_row(G):
    """The row player's linear program (scipy.optimize.linprog): maximize v such that pᵀ G ≥ v on every column,
    p ≥ 0, Σ p = 1. Returns (v, p)."""
    G = np.asarray(G, dtype=float)
    m, n = G.shape
    res = optimize.linprog(np.r_[np.zeros(m), -1.0], A_ub=np.hstack([-G.T, np.ones((n, 1))]), b_ub=np.zeros(n),
                           A_eq=np.r_[np.ones(m), 0.0][None, :], b_eq=[1.0],
                           bounds=[(0, None)] * m + [(None, None)], method="highs")
    assert res.status == 0, f"oracle: linprog failed ({res.message})"
    return float(res.x[-1]), res.x[:m]


def _lp_column(G):
    """The column player's linear program: minimize w such that G q ≤ w on every row, q ≥ 0, Σ q = 1. Returns (w, q)."""
    G = np.asarray(G, dtype=float)
    m, n = G.shape
    res = optimize.linprog(np.r_[np.zeros(n), 1.0], A_ub=np.hstack([G, -np.ones((m, 1))]), b_ub=np.zeros(m),
                           A_eq=np.r_[np.ones(n), 0.0][None, :], b_eq=[1.0],
                           bounds=[(0, None)] * n + [(None, None)], method="highs")
    assert res.status == 0, f"oracle: linprog failed ({res.message})"
    return float(res.x[-1]), res.x[:n]


def _game_without_saddle(rng, scale=3.0, integers=False):
    """A random 2 × 2 game without a saddle point (checked entry by entry)."""
    while True:
        G = rng.integers(-9, 10, size=(2, 2)).astype(float) if integers else rng.normal(size=(2, 2)) * scale
        if not _saddle_points(G):
            return G


def _game_with_saddle(rng, scale=3.0, integers=False):
    """A random 2 × 2 game with a saddle point."""
    while True:
        G = rng.integers(-9, 10, size=(2, 2)).astype(float) if integers else rng.normal(size=(2, 2)) * scale
        if _saddle_points(G):
            return G


def _step_matrix(A, eta, alternating):
    """The matrix M of one step, z_{k+1} = M z_k for z = (x, y): [[I, -ηA], [ηAᵀ, I]] (simultaneous), or the product of
    the two half-steps [[I, 0], [ηAᵀ, I]] [[I, -ηA], [0, I]] (alternating)."""
    A = np.asarray(A, dtype=float)
    n, m = A.shape
    down = np.block([[np.eye(n), -eta * A], [np.zeros((m, n)), np.eye(m)]])
    up = np.block([[np.eye(n), np.zeros((n, m))], [eta * A.T, np.eye(m)]])
    if alternating:
        return up @ down
    return np.block([[np.eye(n), -eta * A], [eta * A.T, np.eye(m)]])


def _iterates_power(A, x0, y0, eta, N, alternating):
    """z_k = M^k z_0, M^k by np.linalg.matrix_power. Returns (xs, ys)."""
    A = np.asarray(A, dtype=float)
    n = A.shape[0]
    M = _step_matrix(A, eta, alternating)
    z0 = np.concatenate([np.asarray(x0, dtype=float), np.asarray(y0, dtype=float)])
    Z = np.array([np.linalg.matrix_power(M, k) @ z0 for k in range(N + 1)])
    return Z[:, :n], Z[:, n:]


def _iterates_loop(A, x0, y0, eta, N, rule):
    """Iterates by a given rule (the contract, or a classic error): row 0 is (x0, y0), then (x, y) = rule(x, y)."""
    A = np.asarray(A, dtype=float)
    xs, ys = [np.asarray(x0, dtype=float)], [np.asarray(y0, dtype=float)]
    for _ in range(N):
        x, y = rule(A, xs[-1], ys[-1], eta)
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


def _simultaneous(A, x, y, eta):
    return x - eta * (A @ y), y + eta * (A.T @ x)


def _alternating(A, x, y, eta):
    x_new = x - eta * (A @ y)
    return x_new, y + eta * (A.T @ x_new)


def _w2_quad(mu1, sigma1, mu2, sigma2):
    """sqrt(∫₀¹ (F₁⁻¹(u) - F₂⁻¹(u))² du), F⁻¹(u) = μ + σ Φ⁻¹(u) by scipy.stats.norm.ppf, the integral by
    scipy.integrate.quad on [0, ½] and [½, 1] (a standard deviation 0 is the constant quantile μ)."""
    def gap(u):
        z = stats.norm.ppf(u)
        return ((mu1 + sigma1 * z) - (mu2 + sigma2 * z)) ** 2

    total = 0.0
    for a, b in ((0.0, 0.5), (0.5, 1.0)):
        value, _ = integrate.quad(gap, a, b, limit=200, epsabs=1e-13, epsrel=1e-12)
        total += value
    return math.sqrt(total)


def _w1_quantiles(mu1, sigma1, mu2, sigma2, K=20_000):
    """W₁ by scipy.stats.wasserstein_distance between K quantiles of each law, at the levels (k - ½)/K."""
    z = stats.norm.ppf((np.arange(K) + 0.5) / K)
    return float(stats.wasserstein_distance(mu1 + sigma1 * z, mu2 + sigma2 * z))


# --- what the module may use ----------------------------------------------------------------------------------------

def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``det`` (from numpy.linalg import det) → "numpy.linalg.det"."""
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


def _uses(tree, names):
    """Each use of an imported name (or of a chain of attributes on it): (where, dotted path), e.g.
    ("w2_gaussians_1d", "numpy.linalg.norm"); ``where`` is the top-level function, or "the module level"."""
    inner = {id(node.value) for node in ast.walk(tree) if isinstance(node, ast.Attribute)}
    uses = []
    for statement in tree.body:
        where = _where(statement)
        for node in ast.walk(statement):
            if not isinstance(node, (ast.Name, ast.Attribute)) or id(node) in inner:
                continue                                  # only the whole chain np.linalg.norm, not np.linalg
            attrs = []
            while isinstance(node, ast.Attribute):
                attrs.append(node.attr)
                node = node.value
            if isinstance(node, ast.Name) and node.id in names:
                uses.append((where, ".".join([names[node.id]] + attrs[::-1])))
    return uses


FORBIDDEN_STRINGS = {"linalg", "linprog", "matrix_power", "eig", "eigvals", "det", "norm", "svd", "inv", "solve"}


def _string_uses(tree):
    """getattr(np, "linalg") and the like, and __import__("scipy") or importlib.import_module("scipy…"): a forbidden
    name reached through a string."""
    found = []
    for statement in tree.body:
        where = _where(statement)
        for node in ast.walk(statement):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            name = func.id if isinstance(func, ast.Name) else func.attr if isinstance(func, ast.Attribute) else ""
            texts = [a.value for a in node.args if isinstance(a, ast.Constant) and isinstance(a.value, str)]
            if name == "getattr" and any(t in FORBIDDEN_STRINGS for t in texts):
                found.append(f"getattr(…, {next(t for t in texts if t in FORBIDDEN_STRINGS)!r}) in {where}")
            if name in ("__import__", "import_module") and any(t.startswith(("scipy", "numpy.linalg")) for t in texts):
                found.append(f"{name}({texts[0]!r}) in {where}")
    return found


def test_module_uses_numpy_and_math_but_nothing_from_np_linalg_and_no_scipy(ds_module):
    """The docstring allows NumPy and the module math, but nothing from np.linalg (not even np.linalg.norm) and no
    SciPy at all (scipy.optimize.linprog solves a matrix game): the tests compare your results with
    scipy.optimize.linprog, np.linalg.matrix_power and scipy.integrate.quad. Only the code counts: a comment, a
    docstring or an import never used is not a use. ``np.linalg.LinAlgError`` (an exception, not a computation) is
    not counted."""
    try:
        tree = ast.parse(inspect.getsource(ds_module))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = []
    for where, path in _uses(tree, _imported_names(tree)):
        parts = path.split(".")
        shown = ".".join(["np"] + parts[1:]) if parts[0] == "numpy" else path
        if parts[0] == "scipy":
            found.append(f"{shown} in {where}")
        elif parts[0] == "numpy" and len(parts) > 1 and parts[1] == "linalg":
            if len(parts) > 2 and parts[2] == "LinAlgError":
                continue
            found.append(f"{shown} in {where}")
    found += _string_uses(tree)
    assert not found, (f"expected NumPy and math only, with nothing from np.linalg and no SciPy at all, found "
                       f"{sorted(set(found))} (the tests compare your results with scipy.optimize.linprog, "
                       f"np.linalg.matrix_power and scipy.integrate.quad: G.min(axis=1), G.max(axis=0), A @ y, "
                       f"A.T @ x and math.hypot or math.sqrt are enough)")


# --- pure_strategy_values -------------------------------------------------------------------------------------------

PURE_HINT = ("maximin = max_i min_j G[i, j]: the minimum of each row (G.min(axis=1)), then the largest, and row the "
             "smallest index of a row that reaches it; minimax = min_j max_i G[i, j]: the maximum of each column "
             "(G.max(axis=0)), then the smallest, and col the smallest index of a column that reaches it")


def _last_index_oracle(G):
    """(maximin, minimax, row, col) with the LARGEST indices of a tie (a classic error)."""
    maximin, minimax, _, _ = _pure_oracle(G)
    G = np.asarray(G, dtype=float)
    rows = [i for i in range(G.shape[0]) if G[i].min() == maximin]
    cols = [j for j in range(G.shape[1]) if G[:, j].max() == minimax]
    return maximin, minimax, rows[-1], cols[-1]


def _pure_hint(got, G):
    """PURE_HINT, plus the classic error that the result got matches, if any."""
    maximin, minimax, row, col = want = _pure_oracle(G)
    transposed = _pure_oracle(np.asarray(G, dtype=float).T)
    candidates = [
        ((maximin, minimax, col, row), "row and col are swapped: row is the index of a row (the first index of "
                                       "G[i, j]), col that of a column"),
        ((minimax, maximin, row, col) if maximin != minimax else None,
         "maximin and minimax are swapped: the maximin (max of the row minima) comes first, and maximin ≤ minimax"),
        ((minimax, maximin, col, row) if maximin != minimax else None,
         "maximin and minimax are swapped, and row and col too: the result is (maximin, minimax, row, col)"),
        (transposed, "the axes are swapped: the minimum of each ROW is G.min(axis=1), the maximum of each COLUMN is "
                     "G.max(axis=0)"),
        (_last_index_oracle(G), "the largest index of a tie was taken: row and col are the smallest indices "
                                "(np.argmax and np.argmin return the first one)"),
    ]
    text = _first_match(got, want, candidates, rtol=0, atol=0)
    return f"{PURE_HINT}; here {text}" if text else PURE_HINT


def _check_pure(got, G, what):
    """The 4-tuple got equals the loops of the oracle, values and types."""
    want = _pure_oracle(G)
    hint = _pure_hint(got, G)
    _tuple(got, 4, what, "(maximin, minimax, row, col)")
    try:
        same = [float(got[0]), float(got[1]), got[2], got[3]] == list(want)
    except (TypeError, ValueError):
        same = False
    assert same, f"expected {what} = {_show_any(want)}, got {_show_any(got)} ({hint})"
    for value, name in zip(got, ("maximin", "minimax", "row", "col")):
        (_float if name.startswith("m") else _int)(value, f"{name} of {what}")


def test_pure_strategy_values_docstring_examples(ds):
    G = [[7, -4, 1], [-1, 5, 6]]
    call = "pure_strategy_values([[7, -4, 1], [-1, 5, 6]])"
    got = _result(lambda: ds.pure_strategy_values(G), "(-1.0, 5.0, 1, 1)", call, PURE_HINT)
    _check_pure(got, G, call)
    G = [[1, 6, 2], [4, 5, 4], [0, 8, 3]]
    call = "pure_strategy_values([[1, 6, 2], [4, 5, 4], [0, 8, 3]]) (saddle points (1, 0) and (1, 2))"
    got = _result(lambda: ds.pure_strategy_values(G), "(4.0, 4.0, 1, 0)", call, PURE_HINT)
    _check_pure(got, G, call)


PURE_CASES = [((1, 1), "one entry"), ((1, 5), "one row"), ((4, 1), "one column"), ((2, 3), "two rows"),
              ((3, 3), "square"), ((5, 4), "five rows"), ((8, 6), "eight rows"), ((12, 15), "twelve rows")]


@pytest.mark.parametrize("shape, text", PURE_CASES, ids=[f"{s[0]}x{s[1]}" for s, _ in PURE_CASES])
def test_pure_strategy_values_match_loops_over_rows_and_columns(ds, shape, text):
    """The maximin, the minimax and their smallest indices, recomputed by loops, for random games of floats."""
    rng = np.random.default_rng(6300 + PURE_CASES.index((shape, text)))
    G = rng.normal(size=shape) * 4.0
    what = f"pure_strategy_values(G) for a random {shape[0]} × {shape[1]} game ({text})"
    got = _result(lambda: ds.pure_strategy_values(G), "a tuple (maximin, minimax, row, col)", what, PURE_HINT)
    _check_pure(got, G, what)


def test_pure_strategy_values_maximin_never_exceeds_minimax_and_they_are_equal_iff_there_is_a_saddle_point(ds):
    """On random games of integers (many ties, many saddle points) and of floats: maximin ≤ minimax; maximin ==
    minimax exactly when some entry is the smallest of its row and the largest of its column (found entry by entry);
    and then (row, col) is such an entry."""
    rng = np.random.default_rng(6308)
    seen = {True: 0, False: 0}
    for k in range(240):
        shape = (int(rng.integers(1, 6)), int(rng.integers(1, 6)))
        integers = k % 2 == 0
        G = rng.integers(-3, 4, size=shape) if integers else np.round(rng.normal(size=shape) * 3.0, 2)
        kind = "integers" if integers else "floats"
        what = f"pure_strategy_values(G) for the {shape[0]} × {shape[1]} game of {kind} G = {G.tolist()}"
        got = _result(lambda: ds.pure_strategy_values(G), "a tuple (maximin, minimax, row, col)", what, PURE_HINT)
        _tuple(got, 4, what, "(maximin, minimax, row, col)")
        maximin, minimax, row, col = got
        saddles = _saddle_points(G)
        seen[bool(saddles)] += 1
        assert maximin <= minimax, (f"expected maximin <= minimax for {what}, got maximin = {maximin!r} and minimax = "
                                    f"{minimax!r} ({_pure_hint(got, G)})")
        if saddles:
            assert maximin == minimax and (row, col) in saddles, (
                f"expected maximin == minimax and (row, col) a saddle point for {what}, which has the saddle points "
                f"{saddles}, got {_show_any(got)} ({_pure_hint(got, G)})")
        else:
            assert maximin < minimax, (f"expected maximin < minimax for {what}, which has no saddle point, got "
                                       f"{_show_any(got)} ({_pure_hint(got, G)})")
        _check_pure(got, G, what)
    assert seen[True] > 30 and seen[False] > 30, f"oracle: games with and without saddle points expected, got {seen}"


PURE_TIES = [
    ([[-5, 8, 2], [3, 7, 3], [9, 3, 4]], (3.0, 4.0, 1, 2), "rows 1 and 2 both have the minimum 3"),
    ([[2, 4, 0, 4], [7, -1, 6, 3]], (0.0, 4.0, 0, 1), "columns 1 and 3 both have the maximum 4"),
    ([[3, 2, 2, 5], [1, 0, -2, 5], [3, 2, 2, 6]], (2.0, 2.0, 0, 1),
     "four saddle points (0, 1), (0, 2), (2, 1) and (2, 2)"),
    ([[6, 6, 6], [6, 6, 6]], (6.0, 6.0, 0, 0), "a constant game: every entry is a saddle point"),
    ([[0.1, 0.7], [0.3, 0.2 + 0.1]], (0.3, 0.3, 1, 0), "floats: 0.2 + 0.1 is a little above 0.3, so (1, 0) is the "
                                                      "only saddle point"),
]


@pytest.mark.parametrize("G, want, text", PURE_TIES, ids=["row-tie", "column-tie", "four-saddles", "constant",
                                                          "floats-in-tenths"])
def test_pure_strategy_values_take_the_smallest_indices_of_a_tie(ds, G, want, text):
    what = f"pure_strategy_values({G})"
    assert want == _pure_oracle(G), "oracle"
    got = _result(lambda: ds.pure_strategy_values(G), _show_any(want), f"{what} ({text})", PURE_HINT)
    _check_pure(got, G, f"{what} ({text})")


def test_pure_strategy_values_take_the_smallest_indices_on_random_games_with_ties(ds):
    """Games of the integers -1, 0 and 1, full of ties: the smallest indices, recomputed by loops."""
    rng = np.random.default_rng(6309)
    for _ in range(60):
        shape = (int(rng.integers(2, 7)), int(rng.integers(2, 7)))
        G = rng.integers(-1, 2, size=shape)
        what = f"pure_strategy_values({G.tolist()})"
        got = _result(lambda: ds.pure_strategy_values(G), "a tuple (maximin, minimax, row, col)", what, PURE_HINT)
        _check_pure(got, G, what)


PURE_LINES = [([[4, -2, 7]], (-2.0, -2.0, 0, 1), "one row: the row player has a single move"),
              ([[3], [-1], [8]], (8.0, 8.0, 2, 0), "one column: the column player has a single move"),
              ([[-6.5]], (-6.5, -6.5, 0, 0), "one entry")]


@pytest.mark.parametrize("G, want, text", PURE_LINES, ids=["one-row", "one-column", "one-entry"])
def test_pure_strategy_values_of_a_single_row_or_a_single_column(ds, G, want, text):
    """With a single row (or column), the game always has a saddle point."""
    assert want == _pure_oracle(G), "oracle"
    what = f"pure_strategy_values({G}) ({text})"
    got = _result(lambda: ds.pure_strategy_values(G), _show_any(want), what, PURE_HINT)
    _check_pure(got, G, what)


def test_pure_strategy_values_return_python_floats_and_ints(ds):
    G = [[2, -3, 5], [4, 1, 0]]
    for given, text in ((lambda v: v, "a list of integers"), (np.array, "an integer array"),
                        (lambda v: np.array(v, dtype=np.float32), "a float32 array"),
                        (lambda v: np.array(v, dtype=np.int64), "an int64 array")):
        what = f"pure_strategy_values with {text}, {G}"
        got = _result(lambda: ds.pure_strategy_values(given(G)), "(0.0, 4.0, 1, 2)", what,
                      "two Python floats, then two Python ints")
        _check_pure(got, G, what)


def test_pure_strategy_values_do_not_modify_their_input(ds_module):
    rng = np.random.default_rng(6310)
    G = rng.normal(size=(4, 5))
    copy = G.copy()
    _result(lambda: ds_module.pure_strategy_values(G), "a tuple", "a float array")
    assert np.array_equal(G, copy), (f"expected G unchanged by pure_strategy_values, got G = {_show(G)} (never modify "
                                     f"the arrays you receive: G.sort(axis=1) or G -= … writes into G)")


PURE_REFUSALS = [
    ([1.0, 2.0, 3.0], "G is 1-D"),
    (4.0, "G is a number, not 2-D"),
    (np.zeros((2, 2, 2)), "G is 3-D"),
    (np.zeros((0, 0)), "G is empty (0 × 0)"),
    (np.zeros((0, 3)), "G has no row"),
    (np.zeros((3, 0)), "G has no column"),
    ([], "G is an empty list"),
    ([[]], "G is [[]], a row without entries"),
    ([[1.0, 2.0], [3.0]], "G is a ragged list"),
    ([[1.0, np.nan], [3.0, 4.0]], "G holds a nan"),
    ([[1.0, 2.0], [np.inf, 4.0]], "G holds an inf"),
    ([[-np.inf, 2.0], [3.0, 4.0]], "G holds a -inf"),
    ([[np.nan]], "G is [[nan]]"),
    ([[1.0, "a"], [3.0, 4.0]], "G holds a string that is not a number"),
    (None, "G is None"),
]
PURE_IDS = ["one-d", "scalar", "three-d", "empty", "no-row", "no-column", "empty-list", "empty-row", "ragged", "nan",
            "inf", "minus-inf", "only-nan", "string", "none"]


@pytest.mark.parametrize("G, why", PURE_REFUSALS, ids=PURE_IDS)
def test_pure_strategy_values_refusals(ds, G, why):
    _expect_error(ValueError, lambda: ds.pure_strategy_values(G), f"pure_strategy_values({G!r})", why)


# --- mixed_strategy_value_2x2 ---------------------------------------------------------------------------------------

MIXED_HINT = ("first pure_strategy_values: with a saddle point (maximin == minimax), the pure strategies row and col "
              "(p = 1.0 if row == 0 else 0.0, q likewise with col) and value = maximin; otherwise the indifference "
              "formulas of the docstring: p makes the column player indifferent, q the row player")


def _formulas(G):
    """The indifference formulas of the docstring, applied whatever the game (a classic error if it has a saddle point,
    and the parts of the other classic errors). None when a - b - c + d = 0."""
    (a, b), (c, d) = np.asarray(G, dtype=float).tolist()
    den = a - b - c + d
    if den == 0:
        return None
    return (d - c) / den, (d - b) / den, (a * d - b * c) / den


def _mixed_hint(got, G):
    """MIXED_HINT, plus the classic error that the result got matches, if any."""
    G = np.asarray(G, dtype=float)
    maximin, minimax, row, col = _pure_oracle(G)
    formulas = _formulas(G)
    if maximin == minimax:
        pure = (1.0 if row == 0 else 0.0, 1.0 if col == 0 else 0.0, maximin)
        candidates = [
            (formulas, "the indifference formulas were used although the game has a saddle point (maximin == "
                       "minimax): the pure strategies row and col of pure_strategy_values are then the answer"),
            ((1.0 - pure[0], 1.0 - pure[1], maximin), "p and q are the probabilities of row 0 and column 0: p = 1.0 "
                                                      "when row == 0, and 0.0 when row == 1"),
            ((pure[1], pure[0], maximin), "p and q are swapped: p comes from row (the row player), q from col"),
        ]
        want = pure
    else:
        p, q, v = formulas
        (a, b), (c, d) = G.tolist()
        den = a - b - c + d
        candidates = [
            ((q, p, v), "p and q are swapped, as if each player made itself indifferent: p is chosen so that the "
                        "COLUMN player gets the same with both columns, p a + (1 - p) c = p b + (1 - p) d, and q so "
                        "that the row player gets the same with both rows"),
            ((1 - p, 1 - q, v), "the probabilities of row 1 and column 1 were returned: p is that of row 0, q that "
                                "of column 0"),
            ((1 - q, 1 - p, v), "p and q are swapped, and they are the probabilities of row 1 and column 1"),
            ((p, q, (a * d + b * c) / den), "the sign of b c in the value: (a d - b c) / (a - b - c + d)"),
            ((p, q, -v), "the sign of the value: (a d - b c) / (a - b - c + d)"),
            ((p, q, maximin), "the value is not the maximin of the pure strategies: with mixed strategies it is "
                              "between the maximin and the minimax"),
            ((p, q, minimax), "the value is not the minimax of the pure strategies: with mixed strategies it is "
                              "between the maximin and the minimax"),
            ((1.0 if row == 0 else 0.0, 1.0 if col == 0 else 0.0, maximin),
             "pure strategies were returned although maximin < minimax (no saddle point; maximin == minimax is an "
             "exact comparison, without tolerance): use the indifference formulas"),
        ]
        want = formulas
    text = _first_match(got, want, candidates)
    return f"{MIXED_HINT}; here {text}" if text else MIXED_HINT


def _mixed(ds, G, what):
    """The result of mixed_strategy_value_2x2(G), checked to be a tuple of three numbers."""
    got = _result(lambda: ds.mixed_strategy_value_2x2(G), "a tuple (p, q, value)", what, MIXED_HINT)
    _tuple(got, 3, what, "(p, q, value)")
    try:
        np.asarray(got, dtype=float)
    except (TypeError, ValueError):
        pytest.fail(f"expected {what} to return three numbers (p, q, value), got {got!r}")
    return got


def _check_types(got, what):
    for value, name in zip(got, ("p", "q", "value")):
        _float(value, f"{name} of {what}")


def test_mixed_strategy_value_2x2_docstring_examples(ds):
    for G, want, text in (([[4, -2], [-1, 3]], (0.4, 0.5, 1.0), ""),
                          ([[-1, 2], [5, 6]], (0.0, 1.0, 5.0), " (saddle point (1, 0))")):
        call = f"mixed_strategy_value_2x2({G}){text}"
        got = _mixed(ds, G, call)
        _close(got, want, call, rtol=0, atol=1e-15, hint=_mixed_hint(got, G))
        _check_types(got, call)


MIXED_LP_CASES = [(False, "without a saddle point"), (False, "without a saddle point, small entries"),
                  (False, "without a saddle point, large entries"), (True, "with a saddle point"),
                  (True, "with a saddle point, integers"), (False, "without a saddle point, integers")]


@pytest.mark.parametrize("saddle, text", MIXED_LP_CASES, ids=["no-saddle", "no-saddle-small", "no-saddle-large",
                                                              "saddle", "saddle-integers", "no-saddle-integers"])
def test_mixed_strategy_value_2x2_matches_linprog(ds, saddle, text):
    """The value of each player's linear program (scipy.optimize.linprog); without a saddle point the optimal
    strategies are unique, and p and q are those of the linear programs."""
    rng = np.random.default_rng(6320 + MIXED_LP_CASES.index((saddle, text)))
    scale = 1e-3 if "small" in text else 1e3 if "large" in text else 3.0
    for _ in range(12):
        draw = _game_with_saddle if saddle else _game_without_saddle
        G = draw(rng, scale=scale, integers="integers" in text)
        v_row, p_lp = _lp_row(G)
        v_col, q_lp = _lp_column(G)
        what = f"mixed_strategy_value_2x2(G), G = {G.tolist()} ({text})"
        got = _mixed(ds, G, what)
        hint = _mixed_hint(got, G)
        tol = 1e-8 * max(1.0, float(np.max(np.abs(G))))
        _close(got[2], v_row, f"the value of {what}, the value of the row player's linear program (linprog)",
               rtol=1e-8, atol=tol, hint=hint)
        _close(got[2], v_col, f"the value of {what}, the value of the column player's linear program (linprog)",
               rtol=1e-8, atol=tol, hint=hint)
        if not saddle:
            _close(got[:2], [p_lp[0], q_lp[0]], f"(p, q) of {what}, the optimal strategies of the linear programs",
                   rtol=1e-7, atol=1e-8, hint=hint)
        _check_types(got, what)


MIXED_EXACT = [([[3, -1], [-2, 1]], (3 / 7, 2 / 7, 1 / 7), "p = 3/7, q = 2/7, value 1/7"),
               ([[-3, 4], [5, 0]], (5 / 12, 1 / 3, 5 / 3), "p = 5/12, q = 1/3, value 5/3")]


@pytest.mark.parametrize("G, want, text", MIXED_EXACT, ids=["sevenths", "twelfths"])
def test_mixed_strategy_value_2x2_of_integer_games_without_a_saddle_point(ds, G, want, text):
    """Two integer games without a saddle point, whose answers (fractions) are those of the linear programs."""
    v_row, p_lp = _lp_row(G)
    v_col, q_lp = _lp_column(G)
    assert np.allclose([p_lp[0], q_lp[0], v_row, v_col], [want[0], want[1], want[2], want[2]], atol=1e-9), "oracle"
    what = f"mixed_strategy_value_2x2({G})"
    got = _mixed(ds, G, what)
    _close(got, want, f"{what} ({text})", rtol=1e-12, atol=1e-14, hint=_mixed_hint(got, G))
    _check_types(got, what)


def test_mixed_strategy_value_2x2_without_a_saddle_point_make_the_opponent_indifferent(ds):
    """Without a saddle point, 0 < p < 1 and 0 < q < 1, the row player's p gives the column player the same expected
    payment with both columns, and the column player's q gives the row player the same expected gain with both rows;
    both are the value."""
    rng = np.random.default_rng(6326)
    for k in range(40):
        G = _game_without_saddle(rng, integers=k % 4 == 0)
        what = f"mixed_strategy_value_2x2(G), G = {G.tolist()} (no saddle point)"
        got = _mixed(ds, G, what)
        p, q, value = (float(t) for t in got)
        hint = _mixed_hint(got, G)
        assert 0 < p < 1 and 0 < q < 1, (f"expected 0 < p < 1 and 0 < q < 1 for {what}, got p = {p!r} and q = {q!r} "
                                          f"({hint})")
        (a, b), (c, d) = G.tolist()
        columns = (p * a + (1 - p) * c, p * b + (1 - p) * d)
        rows = (q * a + (1 - q) * b, q * c + (1 - q) * d)
        scale = max(1.0, float(np.max(np.abs(G))))
        assert math.isclose(columns[0], columns[1], rel_tol=1e-9, abs_tol=1e-9 * scale), (
            f"expected p to give the same expected payoff against both columns for {what}: p a + (1 - p) c = "
            f"p b + (1 - p) d, got {columns[0]:.10g} and {columns[1]:.10g} with p = {p!r} ({hint})")
        assert math.isclose(rows[0], rows[1], rel_tol=1e-9, abs_tol=1e-9 * scale), (
            f"expected q to give the same expected payoff with both rows for {what}: q a + (1 - q) b = "
            f"q c + (1 - q) d, got {rows[0]:.10g} and {rows[1]:.10g} with q = {q!r} ({hint})")
        _close(value, columns[0], f"the value of {what}, the expected payoff of p against either column", rtol=1e-9,
               atol=1e-9 * scale, hint=hint)


def test_mixed_strategy_value_2x2_strategies_guarantee_the_value(ds):
    """With or without a saddle point, p wins at least the value on average against each column, and q pays at most
    the value on average against each row (von Neumann's minimax theorem); p and q are probabilities."""
    rng = np.random.default_rng(6327)
    for k in range(120):
        G = rng.integers(-5, 6, size=(2, 2)).astype(float) if k % 3 == 0 else rng.normal(size=(2, 2)) * 2.0
        what = f"mixed_strategy_value_2x2(G), G = {G.tolist()}"
        got = _mixed(ds, G, what)
        p, q, value = (float(t) for t in got)
        hint = _mixed_hint(got, G)
        assert 0 <= p <= 1 and 0 <= q <= 1, (f"expected probabilities 0 <= p, q <= 1 for {what}, got p = {p!r} and "
                                              f"q = {q!r} ({hint})")
        against_columns = np.array([p, 1 - p]) @ G
        against_rows = G @ np.array([q, 1 - q])
        tol = 1e-9 * max(1.0, float(np.max(np.abs(G))))
        assert np.all(against_columns >= value - tol), (
            f"expected the row player's strategy (p, 1 - p) to win at least the value {value:.10g} against each "
            f"column for {what}, got the expected gains {_show(against_columns)} ({hint})")
        assert np.all(against_rows <= value + tol), (
            f"expected the column player's strategy (q, 1 - q) to pay at most the value {value:.10g} against each "
            f"row for {what}, got the expected payments {_show(against_rows)} ({hint})")


def test_mixed_strategy_value_2x2_value_is_between_maximin_and_minimax(ds):
    """maximin ≤ value ≤ minimax (the maximin and the minimax recomputed by loops), with equality for a saddle point."""
    rng = np.random.default_rng(6328)
    for k in range(80):
        G = rng.integers(-4, 5, size=(2, 2)).astype(float) if k % 2 else np.round(rng.normal(size=(2, 2)) * 5, 1)
        maximin, minimax, _, _ = _pure_oracle(G)
        what = f"mixed_strategy_value_2x2(G), G = {G.tolist()} (maximin {maximin:g}, minimax {minimax:g})"
        got = _mixed(ds, G, what)
        value = float(got[2])
        tol = 1e-12 * max(1.0, float(np.max(np.abs(G))))
        assert maximin - tol <= value <= minimax + tol, (
            f"expected maximin <= value <= minimax for {what}, got value = {value!r} ({_mixed_hint(got, G)})")
        if maximin == minimax:
            assert value == maximin, (f"expected value == maximin == minimax = {maximin!r} for {what} (a saddle "
                                      f"point), got {value!r} ({_mixed_hint(got, G)})")


MIXED_SADDLES = [
    ([[2, 5], [1, 3]], (1.0, 1.0, 2.0), "saddle point (0, 0)"),
    ([[-4, 0], [6, 2]], (0.0, 0.0, 2.0), "saddle point (1, 1)"),
    ([[7, 1], [0, -3]], (1.0, 0.0, 1.0), "saddle point (0, 1)"),
    ([[-2, 9], [4, 6]], (0.0, 1.0, 4.0), "saddle point (1, 0)"),
    ([[2, 2], [1, 3]], (1.0, 1.0, 2.0), "saddle point (0, 0); column 1 is also optimal for the column player when "
                                        "mixed with column 0, but the contract asks for col"),
    ([[0, 4], [0, 1]], (1.0, 1.0, 0.0), "rows 0 and 1 both guarantee 0: the smallest index"),
    ([[5, 5], [5, 5]], (1.0, 1.0, 5.0), "a constant game: a - b - c + d = 0"),
    ([[-1.5, 2.25], [-1.5, -0.75]], (1.0, 1.0, -1.5), "floats, saddle points (0, 0) and (1, 0)"),
]


@pytest.mark.parametrize("G, want, text", MIXED_SADDLES, ids=["saddle-00", "saddle-11", "saddle-01", "saddle-10",
                                                              "weakly-dominated", "row-tie", "constant", "floats"])
def test_mixed_strategy_value_2x2_with_a_saddle_point_returns_the_pure_strategies(ds, G, want, text):
    """With a saddle point, the pure strategies row and col of pure_strategy_values (the smallest indices), exactly 1.0
    or 0.0, and value = maximin: never the indifference formulas, which may leave [0, 1], divide by 0 or pick another
    optimal strategy."""
    maximin, minimax, row, col = _pure_oracle(G)
    assert maximin == minimax and want == (1.0 if row == 0 else 0.0, 1.0 if col == 0 else 0.0, maximin), "oracle"
    what = f"mixed_strategy_value_2x2({G}) ({text})"
    got = _mixed(ds, G, what)
    _close(got, want, what, rtol=0, atol=0, hint=_mixed_hint(got, G))
    _check_types(got, what)


def test_mixed_strategy_value_2x2_compares_maximin_and_minimax_exactly(ds):
    """maximin and minimax are entries of G, so « maximin == minimax » is an exact comparison: tiny payoffs whose
    maximin 0 and minimax 1e-10 differ are no saddle point (no tolerance such as np.isclose), and the value is then
    strictly between them (the linear program of scipy.optimize.linprog, scaled)."""
    G = [[1e-10, 0.0], [0.0, 1e-10]]
    maximin, minimax, _, _ = _pure_oracle(G)
    assert maximin < minimax and not _saddle_points(G), "oracle"
    v_row, p_lp = _lp_row(np.array(G) * 1e10)
    _, q_lp = _lp_column(np.array(G) * 1e10)
    what = f"mixed_strategy_value_2x2({G}) (maximin 0 < minimax 1e-10: no saddle point)"
    got = _mixed(ds, G, what)
    hint = _mixed_hint(got, G)
    _close(got, [p_lp[0], q_lp[0], v_row * 1e-10], what, rtol=1e-9, atol=1e-20, hint=hint)
    assert maximin < float(got[2]) < minimax, (f"expected maximin < value < minimax for {what}, got value = "
                                               f"{float(got[2])!r} ({hint})")


def _shifted_and_scaled_cases():
    rng = np.random.default_rng(6329)
    cases = []
    for k in range(16):
        integers = k % 2 == 0
        G = rng.integers(-9, 10, size=(2, 2)).astype(float) if integers else rng.normal(size=(2, 2)) * 3.0
        c = float(rng.integers(-20, 21)) if integers else float(np.round(rng.uniform(-8, 8), 2))
        kk = float(rng.choice([2.0, 3.0, 0.125, 7.0])) if integers else float(np.round(rng.uniform(0.2, 6), 2))
        cases.append((G, c, kk))
    return cases


def test_mixed_strategy_value_2x2_value_moves_with_G_plus_c_and_k_G(ds):
    """The value of G + c is v + c and that of k G is k v (k > 0), with the same p and q (games of integers, with an
    integer c and k in 2, 3, 1/8, 7, and games of floats)."""
    for G, c, k in _shifted_and_scaled_cases():
        base = _mixed(ds, G, f"mixed_strategy_value_2x2(G), G = {G.tolist()}")
        scale = max(1.0, float(np.max(np.abs(G))), abs(c))
        for H, want, name in ((G + c, base[2] + c, f"G + {c:g}"), (k * G, k * base[2], f"{k:g} G")):
            what = f"mixed_strategy_value_2x2({name}), G = {G.tolist()}"
            got = _mixed(ds, H, what)
            hint = _mixed_hint(got, H)
            _close(got[2], want, f"the value of {what}, {'v + c' if '+' in name else 'k v'} with v = {base[2]!r} the "
                                 f"value of G", rtol=1e-9, atol=1e-9 * scale * max(1.0, k), hint=hint)
            _close(got[:2], base[:2], f"(p, q) of {what}, the same as for G", rtol=1e-8, atol=1e-9, hint=hint)
            v_row, _ = _lp_row(H)
            _close(got[2], v_row, f"the value of {what}, the value of the linear program (linprog)", rtol=1e-8,
                   atol=1e-8 * scale * max(1.0, k), hint=hint)


def test_mixed_strategy_value_2x2_return_python_floats(ds):
    for G, text in (([[2, 5], [1, 3]], "saddle point: p and q are 1.0 or 0.0, not 1 or True"),
                    ([[3, -1], [-2, 1]], "no saddle point")):
        for given, kind in ((lambda v: v, "a list of integers"), (np.array, "an integer array"),
                            (lambda v: np.array(v, dtype=np.float32), "a float32 array")):
            what = f"mixed_strategy_value_2x2 with {kind}, {G} ({text})"
            got = _mixed(ds, given(G), what)
            _close(got, _lp_values(G), what, rtol=1e-6, atol=1e-7, hint=_mixed_hint(got, G))
            _check_types(got, what)


def _lp_values(G):
    """(p, q, value) of a 2 × 2 game from the linear programs (for a saddle point, the pure strategies of the contract,
    whose value is that of the linear program)."""
    maximin, minimax, row, col = _pure_oracle(G)
    v_row, p_lp = _lp_row(G)
    _, q_lp = _lp_column(G)
    if maximin == minimax:
        return 1.0 if row == 0 else 0.0, 1.0 if col == 0 else 0.0, v_row
    return float(p_lp[0]), float(q_lp[0]), v_row


def test_mixed_strategy_value_2x2_does_not_modify_its_input(ds_module):
    for G in (np.array([[3.0, -1.0], [-2.0, 1.0]]), np.array([[2.0, 5.0], [1.0, 3.0]])):
        copy = G.copy()
        _result(lambda: ds_module.mixed_strategy_value_2x2(G), "a tuple", "a float array")
        assert np.array_equal(G, copy), (
            f"expected G unchanged by mixed_strategy_value_2x2, got G = {_show(G)} (never modify the arrays you "
            f"receive)")


MIXED_REFUSALS = [
    ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], "G is 2 × 3"),
    ([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], "G is 3 × 2"),
    ([[1.0, 2.0]], "G is 1 × 2"),
    ([[1.0], [2.0]], "G is 2 × 1"),
    ([[3.0]], "G is 1 × 1"),
    ([1.0, 2.0, 3.0, 4.0], "G is 1-D with four entries, not (2, 2)"),
    (np.zeros((2, 2, 1)), "G is 3-D (2, 2, 1)"),
    (np.zeros((0, 0)), "G is empty"),
    (2.0, "G is a number"),
    ([[1.0, np.nan], [3.0, 4.0]], "G holds a nan"),
    ([[np.nan, 1.0], [2.0, 3.0]], "G holds a nan in a corner"),
    ([[1.0, 2.0], [3.0, np.inf]], "G holds an inf"),
    ([[-np.inf, 2.0], [3.0, 4.0]], "G holds a -inf"),
    ([[1.0, 2.0], [3.0]], "G is a ragged list"),
    ([["x", 2.0], [3.0, 4.0]], "G holds a string that is not a number"),
    (None, "G is None"),
]
MIXED_IDS = ["2x3", "3x2", "1x2", "2x1", "1x1", "one-d-four", "three-d", "empty", "scalar", "nan", "nan-corner", "inf",
             "minus-inf", "ragged", "string", "none"]


@pytest.mark.parametrize("G, why", MIXED_REFUSALS, ids=MIXED_IDS)
def test_mixed_strategy_value_2x2_refusals(ds, G, why):
    _expect_error(ValueError, lambda: ds.mixed_strategy_value_2x2(G), f"mixed_strategy_value_2x2({G!r})", why)


# --- descent_ascent_iterates ----------------------------------------------------------------------------------------

DA_HINT = ("row 0 holds x0 and y0; then x_{k+1} = x_k - eta A y_k (x goes down its gradient A y) and "
           "y_{k+1} = y_k + eta Aᵀ x (y goes up its gradient Aᵀ x), with the old x_k (simultaneous) or the new x_{k+1} "
           "(alternating); return (xs, ys), of shapes (N + 1, n) and (N + 1, m)")


def _pair(got):
    """got as two float arrays, or None."""
    if not (isinstance(got, tuple) and len(got) == 2):
        return None
    try:
        return np.asarray(got[0], dtype=float), np.asarray(got[1], dtype=float)
    except (TypeError, ValueError):
        return None


def _pair_matches(got, value):
    pair = _pair(got)
    return pair is not None and value is not None and _matches(pair[0], value[0]) and _matches(pair[1], value[1])


def _da_hint(got, A, x0, y0, eta, N, alternating):
    """DA_HINT, plus the classic error that the iterates got match, if any."""
    A = np.asarray(A, dtype=float)
    n, m = A.shape
    x0, y0 = np.asarray(x0, dtype=float), np.asarray(y0, dtype=float)
    pair = _pair(got)
    if pair is not None and pair[0].shape == (N, n) and pair[1].shape == (N, m) and N > 0:
        return f"{DA_HINT}; here {N} rows were returned for {N} steps: row 0 is the start (x0, y0)"
    if pair is not None and pair[0].shape == (N + 1, m) and pair[1].shape == (N + 1, n) and n != m:
        return f"{DA_HINT}; here the shapes say that ys came first: return (xs, ys) in this order"
    right = _alternating if alternating else _simultaneous
    want = _iterates_loop(A, x0, y0, eta, N, right)

    def ascent_down(A, x, y, eta):
        x_new, _ = right(A, x, y, eta)
        return x_new, y - eta * (A.T @ (x_new if alternating else x))

    def descent_up(A, x, y, eta):
        x_new = x + eta * (A @ y)
        return x_new, y + eta * (A.T @ (x_new if alternating else x))

    def roles_swapped(A, x, y, eta):
        x_new = x + eta * (A @ y)
        return x_new, y - eta * (A.T @ (x_new if alternating else x))

    def y_first(A, x, y, eta):
        y_new = y + eta * (A.T @ x)
        return x - eta * (A @ y_new), y_new

    candidates = [
        (_iterates_loop(A, x0, y0, eta, N, _simultaneous) if alternating else None,
         "the new y was computed from the old x_k (the simultaneous step): the alternating step uses the new x, "
         "y_{k+1} = y_k + eta Aᵀ x_{k+1}"),
        (_iterates_loop(A, x0, y0, eta, N, _alternating) if not alternating else None,
         "the new y already used the new x (the alternating step): in the simultaneous step both come from the old "
         "pair, keep x_k until y_{k+1} is computed"),
        (_iterates_loop(A, x0, y0, eta, N, ascent_down), "y went down its gradient: the player y maximizes, "
                                                         "y_{k+1} = y_k + eta Aᵀ x (the sign of the ascent)"),
        (_iterates_loop(A, x0, y0, eta, N, descent_up), "x went up its gradient: the player x minimizes, "
                                                        "x_{k+1} = x_k - eta A y_k"),
        (_iterates_loop(A, x0, y0, eta, N, roles_swapped), "the roles are swapped: x goes down (- eta A y), y goes up "
                                                           "(+ eta Aᵀ x)"),
        (_iterates_loop(A, x0, y0, eta, N, y_first) if alternating else None,
         "y was moved first: the alternating step moves x first, then y with the new x"),
    ]
    if n == m:
        def a_for_at(A, x, y, eta):
            return right(A.T, x, y, eta)

        def a_for_at_in_y(A, x, y, eta):
            x_new = x - eta * (A @ y)
            return x_new, y + eta * (A @ (x_new if alternating else x))

        def at_for_a_in_x(A, x, y, eta):
            x_new = x - eta * (A.T @ y)
            return x_new, y + eta * (A.T @ (x_new if alternating else x))

        candidates += [
            (_iterates_loop(A, x0, y0, eta, N, a_for_at_in_y), "A x was used for y: the gradient of f(x, y) = xᵀ A y "
                                                               "in y is Aᵀ x (A.T @ x)"),
            (_iterates_loop(A, x0, y0, eta, N, at_for_a_in_x), "Aᵀ y was used for x: the gradient of f(x, y) = xᵀ A y "
                                                               "in x is A y (A @ y)"),
            (_iterates_loop(A, x0, y0, eta, N, a_for_at), "A and Aᵀ were exchanged: the gradient of f(x, y) = xᵀ A y "
                                                          "in x is A y, in y it is Aᵀ x"),
        ]
    candidates += [
        ((np.tile(want[0][-1], (N + 1, 1)), np.tile(want[1][-1], (N + 1, 1))) if N > 0 else None,
         "every row is the last iterate: the same array was stored N + 1 times and changed in place (x -= …); store a "
         "new array each step"),
        ((np.vstack([x0, np.tile(right(A, x0, y0, eta)[0], (N, 1))]),
          np.vstack([y0, np.tile(right(A, x0, y0, eta)[1], (N, 1))])) if N > 1 else None,
         "each step starts from (x0, y0): the step k + 1 starts from (x_k, y_k)"),
        ((want[1], want[0]) if n == m else None, "xs and ys are swapped: return (xs, ys) in this order"),
    ]
    for value, text in candidates:
        if value is not None and not (_matches(value[0], want[0]) and _matches(value[1], want[1])) and _pair_matches(
                got, value):
            return f"{DA_HINT}; here {text}"
    return DA_HINT


def _check_iterates(got, want, what, hint, rtol=1e-9, atol=1e-11):
    """got is (xs, ys), two float arrays equal to want; the message names the first wrong row."""
    xs_want, ys_want = (np.asarray(w, dtype=float) for w in want)
    _tuple(got, 2, what, "(xs, ys)")
    _float_array(got[0], xs_want.shape, f"xs of {what}", hint)
    _float_array(got[1], ys_want.shape, f"ys of {what}", hint)
    for k in range(xs_want.shape[0]):
        for name, g, w in (("x", got[0], xs_want), ("y", got[1], ys_want)):
            if not np.allclose(g[k], w[k], rtol=rtol, atol=atol):
                pytest.fail(f"expected {what}: row {k} of {name}s = {name}_{k} = {_show(w[k])}, got {_show(g[k])} "
                            f"(first wrong row) ({hint})")


def test_descent_ascent_iterates_docstring_examples(ds):
    for alternating, want in ((False, ([[1.0], [1.0], [0.75]], [[0.0], [0.5], [1.0]])),
                              (True, ([[1.0], [1.0], [0.75]], [[0.0], [0.5], [0.875]]))):
        call = (f"descent_ascent_iterates([[2.0]], [1.0], [0.0], eta=0.25, n_steps=2"
                f"{', alternating=True' if alternating else ''})")
        got = _result(lambda: ds.descent_ascent_iterates([[2.0]], [1.0], [0.0], eta=0.25, n_steps=2,
                                                         alternating=alternating), "(xs, ys)", call, DA_HINT)
        _check_iterates(got, want, call, _da_hint(got, [[2.0]], [1.0], [0.0], 0.25, 2, alternating), rtol=0,
                        atol=1e-15)


DA_CASES = [((1, 1), 0.3, 6), ((2, 2), 0.15, 15), ((2, 3), 0.4, 1), ((3, 1), 0.08, 25), ((4, 4), 0.2, 40),
            ((5, 2), 0.35, 9)]


@pytest.mark.parametrize("alternating", [False, True], ids=["simultaneous", "alternating"])
@pytest.mark.parametrize("shape, eta, N", DA_CASES, ids=[f"{s[0]}x{s[1]}-N{N}" for s, _, N in DA_CASES])
def test_descent_ascent_iterates_match_powers_of_the_step_matrix(ds, shape, eta, N, alternating):
    """z_k = Mᵏ z_0 for z = (x, y), with M the matrix of one step and Mᵏ by np.linalg.matrix_power, for random games
    (not symmetric, so that A and Aᵀ differ) and random starts."""
    rng = np.random.default_rng(6340 + DA_CASES.index((shape, eta, N)) + (6 if alternating else 0))
    A = rng.normal(size=shape)
    x0, y0 = rng.normal(size=shape[0]) * 2.0, rng.normal(size=shape[1]) * 2.0
    mode = "alternating" if alternating else "simultaneous"
    what = (f"descent_ascent_iterates(A, x0, y0, {eta}, n_steps={N}, alternating={alternating}) for a random "
            f"{shape[0]} × {shape[1]} matrix ({mode})")
    got = _result(lambda: ds.descent_ascent_iterates(A, x0, y0, eta, n_steps=N, alternating=alternating), "(xs, ys)",
                  what, DA_HINT)
    hint = _da_hint(got, A, x0, y0, eta, N, alternating)
    _check_iterates(got, _iterates_power(A, x0, y0, eta, N, alternating), f"{what}, Mᵏ z_0 by np.linalg.matrix_power",
                    hint)


@pytest.mark.parametrize("alternating", [False, True], ids=["simultaneous", "alternating"])
def test_descent_ascent_iterates_follow_the_recurrence(ds, alternating):
    """Each row comes from the previous one, checked on your own rows: x_{k+1} = x_k - η A y_k, and y_{k+1} =
    y_k + η Aᵀ x_k (simultaneous) or y_k + η Aᵀ x_{k+1} (alternating)."""
    rng = np.random.default_rng(6352 + alternating)
    for shape, eta, N in (((3, 2), 0.3, 20), ((2, 4), 0.12, 30), ((1, 1), 0.7, 12)):
        A = rng.normal(size=shape)
        x0, y0 = rng.normal(size=shape[0]), rng.normal(size=shape[1])
        what = f"descent_ascent_iterates(A, x0, y0, {eta}, n_steps={N}, alternating={alternating}), A {shape}"
        got = _result(lambda: ds.descent_ascent_iterates(A, x0, y0, eta, n_steps=N, alternating=alternating),
                      "(xs, ys)", what, DA_HINT)
        hint = _da_hint(got, A, x0, y0, eta, N, alternating)
        _tuple(got, 2, what, "(xs, ys)")
        xs, ys = got
        _float_array(xs, (N + 1, shape[0]), f"xs of {what}", hint)
        _float_array(ys, (N + 1, shape[1]), f"ys of {what}", hint)
        _close(xs[0], x0, f"row 0 of xs, x0, for {what}", rtol=0, atol=0, hint=hint)
        _close(ys[0], y0, f"row 0 of ys, y0, for {what}", rtol=0, atol=0, hint=hint)
        for k in range(N):
            x_next = xs[k] - eta * (A @ ys[k])
            y_next = ys[k] + eta * (A.T @ (xs[k + 1] if alternating else xs[k]))
            if not np.allclose(xs[k + 1], x_next, rtol=1e-12, atol=1e-12):
                pytest.fail(f"expected row {k + 1} of xs = x_{k} - eta A y_{k} = {_show(x_next)} for {what}, got "
                            f"{_show(xs[k + 1])} ({hint})")
            if not np.allclose(ys[k + 1], y_next, rtol=1e-12, atol=1e-12):
                rule = f"y_{k} + eta Aᵀ x_{k + 1}" if alternating else f"y_{k} + eta Aᵀ x_{k}"
                pytest.fail(f"expected row {k + 1} of ys = {rule} = {_show(y_next)} for {what}, got "
                            f"{_show(ys[k + 1])} ({hint})")


@pytest.mark.parametrize("alternating", [False, True], ids=["simultaneous", "alternating"])
def test_descent_ascent_iterates_first_step_and_shapes(ds, alternating):
    """A 2 × 3 matrix: xs has 2 columns (x is along the rows of A), ys has 3; the first step, written out."""
    A = np.array([[1.0, -2.5, 0.5], [3.0, 0.0, -1.5]])
    x0, y0, eta = np.array([1.0, -1.0]), np.array([0.5, 2.0, -1.0]), 0.2
    x1 = x0 - eta * (A @ y0)
    y1 = y0 + eta * (A.T @ (x1 if alternating else x0))
    what = f"descent_ascent_iterates(A, x0, y0, 0.2, n_steps=1, alternating={alternating}), A 2 × 3"
    got = _result(lambda: ds.descent_ascent_iterates(A, x0, y0, eta, n_steps=1, alternating=alternating), "(xs, ys)",
                  what, DA_HINT)
    _check_iterates(got, ([x0, x1], [y0, y1]), what, _da_hint(got, A, x0, y0, eta, 1, alternating), rtol=1e-14,
                    atol=1e-15)


def test_descent_ascent_iterates_simultaneous_never_get_closer_to_the_equilibrium(ds):
    """The simultaneous iterates never get closer to the equilibrium (0, 0): ‖x_k‖² + ‖y_k‖² never decreases, and it
    increases at each step when A is square and invertible."""
    rng = np.random.default_rng(6354)
    for shape, eta, N in (((1, 1), 0.3, 60), ((3, 3), 0.1, 80), ((2, 4), 0.4, 50), ((4, 2), 0.05, 100)):
        A = rng.normal(size=shape)
        x0, y0 = rng.normal(size=shape[0]), rng.normal(size=shape[1])
        what = f"descent_ascent_iterates(A, x0, y0, {eta}, n_steps={N}) (simultaneous), A {shape}"
        got = _result(lambda: ds.descent_ascent_iterates(A, x0, y0, eta, n_steps=N), "(xs, ys)", what, DA_HINT)
        hint = _da_hint(got, A, x0, y0, eta, N, False)
        _check_iterates(got, _iterates_loop(A, x0, y0, eta, N, _simultaneous), what, hint)
        squares = np.sum(got[0] ** 2, axis=1) + np.sum(got[1] ** 2, axis=1)
        strict = shape[0] == shape[1]
        for k in range(N):
            if squares[k + 1] < squares[k] * (1 - 1e-12) or (strict and squares[k + 1] <= squares[k]):
                pytest.fail(f"expected ‖x‖² + ‖y‖² to {'increase' if strict else 'never decrease'} at each step of "
                            f"{what}, got {squares[k]:.12g} at step {k} and {squares[k + 1]:.12g} at step {k + 1} "
                            f"({hint})")


def _learner_step_matrix(ds, A, eta, alternating):
    """The matrix of one step, read column by column from your function: one step from each vector of the canonical
    basis of ℝⁿ⁺ᵐ."""
    A = np.asarray(A, dtype=float)
    n, m = A.shape
    M = np.zeros((n + m, n + m))
    for i in range(n + m):
        e = np.eye(n + m)[i]
        what = f"descent_ascent_iterates(A, e[:n], e[n:], {eta}, n_steps=1, alternating={alternating}), e = e_{i}"
        got = _result(lambda: ds.descent_ascent_iterates(A, e[:n], e[n:], eta, n_steps=1, alternating=alternating),
                      "(xs, ys)", what, DA_HINT)
        hint = _da_hint(got, A, e[:n], e[n:], eta, 1, alternating)
        _check_iterates(got, _iterates_loop(A, e[:n], e[n:], eta, 1, _alternating if alternating else _simultaneous),
                        what, hint)
        M[:, i] = np.concatenate([got[0][1], got[1][1]])
    return M


def test_descent_ascent_iterates_simultaneous_step_has_eigenvalues_of_modulus_above_1(ds):
    """The matrix of one simultaneous step (read from your function) is that of the oracle, and its eigenvalues
    (np.linalg.eigvals) all have a modulus > 1 for a square invertible A (≥ 1 for a rectangular A): the iterates move
    away from the equilibrium."""
    rng = np.random.default_rng(6356)
    for shape, eta in (((1, 1), 0.3), ((2, 2), 0.15), ((3, 3), 0.4), ((2, 3), 0.2)):
        A = rng.normal(size=shape)
        M = _learner_step_matrix(ds, A, eta, False)
        _close(M, _step_matrix(A, eta, False), f"the matrix of one simultaneous step, A {shape}, eta = {eta}",
               rtol=1e-12, atol=1e-14, hint=DA_HINT)
        moduli = np.sort(np.abs(np.linalg.eigvals(M)))
        bound = 1.0 + 1e-9 if shape[0] == shape[1] else 1.0 - 1e-12
        assert moduli[0] >= bound, (f"expected the eigenvalues of the simultaneous step to have moduli "
                                    f"{'> 1' if shape[0] == shape[1] else '>= 1'}, A {shape}, eta = {eta}, got the "
                                    f"moduli {_show(moduli)} ({DA_HINT})")


def test_descent_ascent_iterates_alternating_step_has_determinant_1(ds):
    """The matrix of one alternating step (read from your function) is that of the oracle, and its determinant
    (np.linalg.det) is 1: the step keeps areas (two shears, each of determinant 1)."""
    rng = np.random.default_rng(6357)
    for shape, eta in (((1, 1), 0.3), ((2, 2), 0.15), ((3, 3), 0.9), ((2, 3), 0.2), ((3, 1), 1.6)):
        A = rng.normal(size=shape)
        M = _learner_step_matrix(ds, A, eta, True)
        _close(M, _step_matrix(A, eta, True), f"the matrix of one alternating step, A {shape}, eta = {eta}",
               rtol=1e-12, atol=1e-14, hint=DA_HINT)
        det = float(np.linalg.det(M))
        assert math.isclose(det, 1.0, rel_tol=0, abs_tol=1e-10), (
            f"expected the determinant of the alternating step to be 1, A {shape}, eta = {eta}, got {det!r} "
            f"({DA_HINT})")


def test_descent_ascent_iterates_alternating_keep_a_quantity_and_circle_around_the_equilibrium(ds):
    """The alternating iterates keep ‖x‖² + ‖y‖² - η xᵀ A y (for f(x, y) = xy, x² + y² - η x y: an ellipse); when
    η ‖A‖ < 2 this quantity is positive definite, so the iterates stay on a bounded curve around (0, 0), neither
    spiralling out nor in."""
    rng = np.random.default_rng(6358)
    for shape, eta, N in (((1, 1), 0.3, 400), ((2, 2), 0.2, 300), ((3, 2), 0.35, 300), ((1, 3), 0.15, 500)):
        A = rng.normal(size=shape)
        x0, y0 = rng.normal(size=shape[0]), rng.normal(size=shape[1])
        what = f"descent_ascent_iterates(A, x0, y0, {eta}, n_steps={N}, alternating=True), A {shape}"
        got = _result(lambda: ds.descent_ascent_iterates(A, x0, y0, eta, n_steps=N, alternating=True), "(xs, ys)",
                      what, DA_HINT)
        hint = _da_hint(got, A, x0, y0, eta, N, True)
        _tuple(got, 2, what, "(xs, ys)")
        _float_array(got[0], (N + 1, shape[0]), f"xs of {what}", hint)
        _float_array(got[1], (N + 1, shape[1]), f"ys of {what}", hint)
        xs, ys = got
        kept = np.sum(xs ** 2, axis=1) + np.sum(ys ** 2, axis=1) - eta * np.einsum("ki,ij,kj->k", xs, A, ys)
        drift = float(np.max(np.abs(kept - kept[0])))
        assert drift <= 1e-10 * max(1.0, abs(kept[0])), (
            f"expected ‖x_k‖² + ‖y_k‖² - eta x_kᵀ A y_k to stay equal to its start {kept[0]:.12g} along {what}, got a "
            f"drift of {drift:.3g} ({hint})")
        radius = np.sqrt(np.sum(xs ** 2, axis=1) + np.sum(ys ** 2, axis=1))
        assert radius.max() <= 4.0 * radius[0] and radius.min() >= radius[0] / 4.0, (
            f"expected the alternating iterates of {what} to stay around the equilibrium (a bounded curve), got "
            f"distances to (0, 0) from {radius.min():.6g} to {radius.max():.6g} for a start at {radius[0]:.6g} "
            f"({hint})")


def test_descent_ascent_iterates_from_the_equilibrium_stay_there(ds):
    A = np.array([[1.5, -0.5], [2.5, 1.0], [0.0, -3.0]])
    for alternating in (False, True):
        what = f"descent_ascent_iterates(A, zeros(3), zeros(2), 0.3, n_steps=5, alternating={alternating})"
        got = _result(lambda: ds.descent_ascent_iterates(A, np.zeros(3), np.zeros(2), 0.3, n_steps=5,
                                                         alternating=alternating), "(xs, ys)", what, DA_HINT)
        _check_iterates(got, (np.zeros((6, 3)), np.zeros((6, 2))), f"{what}: (0, 0) is an equilibrium", DA_HINT,
                        rtol=0, atol=0)


def test_descent_ascent_iterates_defaults_and_zero_steps(ds):
    A = np.array([[0.8, -1.2], [0.4, 2.0]])
    x0, y0 = np.array([1.5, -0.5]), np.array([-1.0, 0.7])
    what = "descent_ascent_iterates(A, x0, y0, 0.3) with the defaults n_steps = 10 and alternating = False"
    got = _result(lambda: ds.descent_ascent_iterates(A, x0, y0, 0.3), "(xs, ys) of 11 rows each", what, DA_HINT)
    _check_iterates(got, _iterates_power(A, x0, y0, 0.3, 10, False), what, _da_hint(got, A, x0, y0, 0.3, 10, False))
    what = "descent_ascent_iterates(A, [2, -1], [0, 3], 0.3, n_steps=0)"
    got = _result(lambda: ds.descent_ascent_iterates(A, [2, -1], [0, 3], 0.3, n_steps=0), "([[2., -1.]], [[0., 3.]])",
                  what, "a single row each: the start, as floats")
    _check_iterates(got, ([[2.0, -1.0]], [[0.0, 3.0]]), what, "a single row each: the start, as floats", rtol=0, atol=0)
    for steps in (np.int64(3), np.int32(2), np.uint8(4)):
        for alternating in (False, True, np.bool_(True)):
            what = f"descent_ascent_iterates(A, x0, y0, 0.3, n_steps={steps!r}, alternating={alternating!r})"
            got = _result(lambda: ds.descent_ascent_iterates(A, x0, y0, 0.3, n_steps=steps, alternating=alternating),
                          f"{int(steps) + 1} rows each", what, "a NumPy integer is accepted")
            _check_iterates(got, _iterates_power(A, x0, y0, 0.3, int(steps), bool(alternating)), what,
                            _da_hint(got, A, x0, y0, 0.3, int(steps), bool(alternating)))


def test_descent_ascent_iterates_take_lists_of_integers_and_return_floats(ds):
    """Lists of integers, integer arrays and an integer step eta = 1 (a finite number > 0) are accepted."""
    A, x0, y0 = [[1, 3], [-2, 0]], [1, 0], [0, 1]
    want = {False: ([[1.0, 0.0], [-2.0, 0.0], [-15.0, 2.0]], [[0.0, 1.0], [1.0, 4.0], [-1.0, -2.0]]),
            True: _iterates_loop(A, x0, y0, 1.0, 2, _alternating)}
    for given, text in ((lambda v: v, "lists of integers"), (np.array, "integer arrays")):
        for alternating in (False, True):
            what = (f"descent_ascent_iterates({A}, {x0}, {y0}, eta=1, n_steps=2, alternating={alternating}) with "
                    f"{text}")
            got = _result(lambda: ds.descent_ascent_iterates(given(A), given(x0), given(y0), 1, n_steps=2,
                                                             alternating=alternating), "(xs, ys)", what, DA_HINT)
            _check_iterates(got, want[alternating], what, _da_hint(got, A, x0, y0, 1.0, 2, alternating), rtol=0,
                            atol=1e-15)


def test_descent_ascent_iterates_do_not_modify_their_inputs(ds_module):
    rng = np.random.default_rng(6359)
    A = rng.normal(size=(3, 2))
    x0, y0 = rng.normal(size=3), rng.normal(size=2)
    copies = [A.copy(), x0.copy(), y0.copy()]
    for alternating in (False, True):
        got = _result(lambda: ds_module.descent_ascent_iterates(A, x0, y0, 0.3, n_steps=4, alternating=alternating),
                      "(xs, ys)", "float arrays")
        for name, value, copy in zip(("A", "x0", "y0"), (A, x0, y0), copies):
            assert np.array_equal(value, copy), (
                f"expected {name} unchanged by descent_ascent_iterates, got {name} = {_show(value)} (never modify the "
                f"arrays you receive: start from float copies of x0 and y0; x = x - eta * (A @ y) makes a new array, "
                f"x -= … writes into x0)")
        _tuple(got, 2, "descent_ascent_iterates(A, x0, y0, 0.3, n_steps=4)", "(xs, ys)")
        got[0][...] = 99.0
        got[1][...] = 99.0
        assert all(np.array_equal(v, c) for v, c in zip((A, x0, y0), copies)), (
            "expected descent_ascent_iterates to return new arrays, but changing them changed A, x0 or y0 (row 0 is a "
            "copy of the start)")


A23 = [[1.0, 0.5, -2.0], [0.0, 3.0, 1.0]]
X2, Y3 = [1.0, -1.0], [0.5, 0.0, 2.0]
DA_SHAPE_REFUSALS = [
    ([1.0, 2.0], [1.0], [1.0, 2.0], {}, "A is 1-D"),
    (2.0, [1.0], [1.0], {}, "A is a number, not 2-D"),
    (np.zeros((2, 2, 2)), [1.0, 2.0], [1.0, 2.0], {}, "A is 3-D"),
    (np.zeros((0, 0)), [], [], {}, "A is empty (0 × 0)"),
    (np.zeros((0, 2)), [], [1.0, 2.0], {}, "A has no row"),
    (np.zeros((2, 0)), [1.0, 2.0], [], {}, "A has no column"),
    ([[1.0, 2.0], [3.0]], X2, [1.0, 2.0], {}, "A is a ragged list"),
    ([[1.0, np.nan, 0.0], [0.0, 3.0, 1.0]], X2, Y3, {}, "A holds a nan"),
    ([[1.0, 0.5, -2.0], [np.inf, 3.0, 1.0]], X2, Y3, {}, "A holds an inf"),
    ([[1.0, 0.5, -2.0], [np.inf, 3.0, 1.0]], X2, Y3, {"n_steps": 0}, "A holds an inf, even for 0 steps"),
    ([[1.0, "b", -2.0], [0.0, 3.0, 1.0]], X2, Y3, {}, "A holds a string that is not a number"),
    (A23, [1.0], Y3, {}, "x0 has 1 coordinate for the 2 rows of A"),
    (A23, [1.0, -1.0, 2.0], Y3, {}, "x0 has 3 coordinates for the 2 rows of A"),
    (A23, [1.0], Y3, {"n_steps": 0}, "x0 has 1 coordinate for 2 rows, even for 0 steps"),
    (A23, [[1.0, -1.0]], Y3, {}, "x0 is 2-D (a row of shape (1, 2)), not 1-D"),
    (A23, 1.0, Y3, {}, "x0 is a number, not 1-D"),
    (A23, X2, [0.5, 0.0], {}, "y0 has 2 coordinates for the 3 columns of A"),
    (A23, X2, [0.5, 0.0, 2.0, 1.0], {}, "y0 has 4 coordinates for the 3 columns of A"),
    (A23, X2, [0.5, 0.0], {"n_steps": 0}, "y0 has 2 coordinates for 3 columns, even for 0 steps"),
    (A23, X2, [[0.5], [0.0], [2.0]], {}, "y0 is a column (3, 1), not 1-D"),
    (A23, X2, 0.5, {}, "y0 is a number, not 1-D"),
    (A23, Y3, X2, {}, "x0 and y0 are swapped: x0 has one coordinate per ROW of A"),
]
DA_SHAPE_IDS = ["A-one-d", "A-scalar", "A-three-d", "A-empty", "A-no-row", "A-no-column", "A-ragged", "A-nan", "A-inf",
                "A-inf-no-step", "A-string", "x0-shorter", "x0-longer", "x0-shorter-no-step", "x0-two-d", "x0-scalar",
                "y0-shorter", "y0-longer", "y0-shorter-no-step", "y0-column", "y0-scalar", "x0-y0-swapped"]


@pytest.mark.parametrize("A, x0, y0, kwargs, why", DA_SHAPE_REFUSALS, ids=DA_SHAPE_IDS)
def test_descent_ascent_iterates_refuse_bad_matrices_and_starts(ds, A, x0, y0, kwargs, why):
    _expect_error(ValueError, lambda: ds.descent_ascent_iterates(A, x0, y0, 0.3, **kwargs),
                  f"descent_ascent_iterates({A!r}, {x0!r}, {y0!r}, 0.3, {kwargs})", why)


ETA_REFUSALS = [(0.0, "eta is 0"), (0, "eta is the integer 0"), (-0.3, "eta is negative"), (np.nan, "eta is nan"),
                (np.inf, "eta is inf"), (-np.inf, "eta is -inf"), (True, "eta is a bool (True), even though True == 1"),
                (False, "eta is a bool (False)"), (np.bool_(True), "eta is a NumPy bool"), (None, "eta is None"),
                ("0.3", "eta is a string"), ([0.3], "eta is a list, not a number")]
ETA_IDS = ["eta-zero", "eta-int-zero", "eta-negative", "eta-nan", "eta-inf", "eta-minus-inf", "eta-true", "eta-false",
           "eta-numpy-bool", "eta-none", "eta-string", "eta-list"]


@pytest.mark.parametrize("eta, why", ETA_REFUSALS, ids=ETA_IDS)
def test_descent_ascent_iterates_refuse_bad_steps_eta(ds, eta, why):
    for steps in (3, 0):
        _expect_error(ValueError, lambda: ds.descent_ascent_iterates(A23, X2, Y3, eta, n_steps=steps),
                      f"descent_ascent_iterates(A, x0, y0, {eta!r}, n_steps={steps})",
                      why + (", even for 0 steps" if steps == 0 else ""))


STEPS_REFUSALS = [(-1, "a negative number of steps"), (2.5, "a number of steps that is not an integer"),
                  (2.0, "the float 2.0 is refused"), (np.float64(3.0), "np.float64(3.0) is refused"),
                  (True, "a bool (True)"), (False, "a bool (False), even though False == 0"),
                  (np.bool_(False), "a NumPy bool"), (None, "n_steps is None"), ("3", "n_steps is a string"),
                  ([3], "n_steps is a list")]
STEPS_IDS = ["steps-negative", "steps-fraction", "steps-float", "steps-numpy-float", "steps-true", "steps-false",
             "steps-numpy-bool", "steps-none", "steps-string", "steps-list"]


@pytest.mark.parametrize("n_steps, why", STEPS_REFUSALS, ids=STEPS_IDS)
def test_descent_ascent_iterates_refuse_bad_numbers_of_steps(ds, n_steps, why):
    _expect_error(ValueError, lambda: ds.descent_ascent_iterates(A23, X2, Y3, 0.3, n_steps=n_steps),
                  f"descent_ascent_iterates(A, x0, y0, 0.3, n_steps={n_steps!r})", why)


# --- w2_gaussians_1d ------------------------------------------------------------------------------------------------

W2_HINT = ("W₂ = sqrt((mu1 - mu2)² + (sigma1 - sigma2)²), with sigma1 and sigma2 standard deviations (not variances), "
           "and the distance itself, not its square")


def _w2_hint(got, mu1, sigma1, mu2, sigma2):
    """W2_HINT, plus the classic error that the result got matches, if any."""
    dm, ds_ = mu1 - mu2, sigma1 - sigma2
    want = math.hypot(dm, ds_)
    candidates = [
        (dm ** 2 + ds_ ** 2, "W₂² was returned: the function returns the distance W₂, the square root of "
                             "(mu1 - mu2)² + (sigma1 - sigma2)²"),
        (math.hypot(dm, sigma1 ** 2 - sigma2 ** 2), "the standard deviations were squared (variances): sigma1 and "
                                                    "sigma2 are standard deviations, W₂² = Δμ² + (σ₁ - σ₂)²"),
        (math.hypot(dm, math.sqrt(sigma1) - math.sqrt(sigma2)),
         "sigma1 and sigma2 were read as variances (their square roots taken): they are standard deviations already"),
        (math.sqrt(dm ** 2 + sigma1 ** 2 + sigma2 ** 2),
         "the cost of the independent coupling was computed (Δμ² + σ₁² + σ₂²): the optimal coupling pairs the "
         "quantiles μ + σ Φ⁻¹(u), and gives Δμ² + (σ₁ - σ₂)²"),
        (abs(dm) + abs(ds_), "|Δμ| + |Δσ| was returned: W₂ = sqrt(Δμ² + Δσ²)"),
        (math.hypot(dm, sigma1 + sigma2), "σ₁ + σ₂ was used: the gap of the standard deviations is σ₁ - σ₂"),
        (abs(dm), "only the means were used: the standard deviations count too"),
    ]
    text = _first_match(got, want, candidates, rtol=1e-12, atol=1e-14)
    return f"{W2_HINT}; here {text}" if text else W2_HINT


def _w2(ds, args, what, want=None):
    """w2_gaussians_1d(*args), checked to be a Python float close to want (by default sqrt(Δμ² + Δσ²), the formula of
    the docstring; the tests named …_integral_… and …_point_mass compare with the integral of the quantiles)."""
    want = math.hypot(float(args[0]) - float(args[2]), float(args[1]) - float(args[3])) if want is None else want
    got = _result(lambda: ds.w2_gaussians_1d(*args), f"W₂ = {want:.10g}", what, W2_HINT)
    hint = _w2_hint(got, *(float(a) for a in args)) if isinstance(got, (int, float)) else W2_HINT
    try:
        value = float(got)
    except (TypeError, ValueError):
        pytest.fail(f"expected {what} to return a number (W₂ = {want:.10g}), got {got!r} ({W2_HINT})")
    assert math.isclose(value, want, rel_tol=1e-9, abs_tol=1e-12), (
        f"expected {what} = {want:.12g}, got {value:.12g} ({hint})")
    _float(got, what)
    return got


def test_w2_gaussians_1d_docstring_examples(ds):
    for args, want, text in (((10.0, 1.0, 2.0, 16.0), 17.0, ""),
                             ((-1.0, 0.5, -1.0, 3.5), 3.0, " (same mean: only the spreads differ)")):
        call = f"w2_gaussians_1d{args}{text}"
        got = _w2(ds, args, call, want)
        assert got == want, f"expected {call} = {want!r} exactly, got {got!r} ({_w2_hint(got, *args)})"


W2_CASES = [("spread", "different means and standard deviations"), ("narrow", "small standard deviations"),
            ("wide", "large means and standard deviations"), ("point-mass-2", "a point mass (sigma2 = 0)"),
            ("point-mass-1", "a point mass (sigma1 = 0)"), ("two-point-masses", "two point masses"),
            ("same-mean", "the same mean"), ("same-spread", "the same standard deviation")]


@pytest.mark.parametrize("kind, text", W2_CASES, ids=[k for k, _ in W2_CASES])
def test_w2_gaussians_1d_matches_the_integral_of_the_squared_quantile_gap(ds, kind, text):
    """W₂² = ∫₀¹ (F₁⁻¹(u) - F₂⁻¹(u))² du, the quantiles μ + σ Φ⁻¹(u) by scipy.stats.norm.ppf and the integral by
    scipy.integrate.quad, for random laws."""
    rng = np.random.default_rng(6370 + [k for k, _ in W2_CASES].index(kind))
    for _ in range(6):
        scale = 1e-3 if kind == "narrow" else 1e3 if kind == "wide" else 1.0
        mu1, mu2 = (rng.normal(size=2) * 5 * (1e3 if kind == "wide" else 1.0)).tolist()
        sigma1, sigma2 = (rng.uniform(0.0, 4.0, size=2) * scale).tolist()
        if kind == "point-mass-2":
            sigma2 = 0.0
        elif kind == "point-mass-1":
            sigma1 = 0.0
        elif kind == "two-point-masses":
            sigma1 = sigma2 = 0.0
        elif kind == "same-mean":
            mu2 = mu1
        elif kind == "same-spread":
            sigma2 = sigma1
        args = (mu1, sigma1, mu2, sigma2)
        _w2(ds, args, f"w2_gaussians_1d({mu1:.6g}, {sigma1:.6g}, {mu2:.6g}, {sigma2:.6g}) ({text})", _w2_quad(*args))


def test_w2_gaussians_1d_is_the_square_root_of_the_two_squared_gaps(ds):
    """W₂ = sqrt((μ₁ - μ₂)² + (σ₁ - σ₂)²) on random laws (math.hypot), with two integer cases."""
    rng = np.random.default_rng(6378)
    cases = [(3.0, 14.0, -2.0, 2.0), (6.5, 0.5, -13.5, 21.5)]          # gaps (5, 12) and (20, -21): 13 and 29
    cases += [tuple(v) for v in np.c_[rng.normal(size=(30, 1)) * 10, rng.uniform(0, 6, size=(30, 1)),
                                      rng.normal(size=(30, 1)) * 10, rng.uniform(0, 6, size=(30, 1))].tolist()]
    for args in cases:
        mu1, sigma1, mu2, sigma2 = args
        _w2(ds, args, f"w2_gaussians_1d({mu1:.6g}, {sigma1:.6g}, {mu2:.6g}, {sigma2:.6g})",
            math.hypot(mu1 - mu2, sigma1 - sigma2))


def test_w2_gaussians_1d_takes_standard_deviations_not_variances(ds):
    """sigma1 and sigma2 are standard deviations: N(3, 14²) and N(-2, 2²) are at W₂ = 13 (the integral of the
    quantiles), not at a distance computed from the variances 196 and 4."""
    for args in ((3.0, 14.0, -2.0, 2.0), (0.6, 0.2, 0.6, 2.7), (-4.0, 9.0, 1.0, 0.0)):
        mu1, sigma1, mu2, sigma2 = args
        what = (f"w2_gaussians_1d{args}, the laws N({mu1:g}, {sigma1:g}²) and N({mu2:g}, {sigma2:g}²) (the integral of "
                f"the quantiles)")
        _w2(ds, args, what, _w2_quad(*args))


def test_w2_gaussians_1d_is_symmetric_and_zero_for_the_same_law(ds):
    rng = np.random.default_rng(6379)
    for _ in range(20):
        mu1, mu2 = (rng.normal(size=2) * 4).tolist()
        sigma1, sigma2 = rng.uniform(0, 3, size=2).tolist()
        what = f"w2_gaussians_1d({mu1:.6g}, {sigma1:.6g}, {mu2:.6g}, {sigma2:.6g})"
        one = _w2(ds, (mu1, sigma1, mu2, sigma2), what)
        two = _w2(ds, (mu2, sigma2, mu1, sigma1), f"the same pair of laws in the other order")
        assert math.isclose(one, two, rel_tol=1e-14, abs_tol=0), (
            f"expected W₂ symmetric: {what} = {one!r} and the same laws in the other order give {two!r} ({W2_HINT})")
        same = _w2(ds, (mu1, sigma1, mu1, sigma1), f"w2_gaussians_1d({mu1:.6g}, {sigma1:.6g}, {mu1:.6g}, "
                                                   f"{sigma1:.6g}), the same law twice", 0.0)
        assert same == 0.0, f"expected 0.0 for the same law twice, got {same!r} ({W2_HINT})"


def test_w2_gaussians_1d_equal_standard_deviations_give_the_gap_of_the_means(ds):
    """A translation: with σ₁ = σ₂, W₂ = |μ₁ - μ₂|, which is also W₁ (scipy.stats.wasserstein_distance between the
    quantiles of the two laws)."""
    rng = np.random.default_rng(6380)
    for k in range(8):
        mu1, mu2 = (rng.normal(size=2) * 6).tolist()
        sigma = 0.0 if k == 0 else float(rng.uniform(0.1, 5))
        w1 = _w1_quantiles(mu1, sigma, mu2, sigma)
        assert math.isclose(w1, abs(mu1 - mu2), rel_tol=1e-9, abs_tol=1e-9), "oracle"
        _w2(ds, (mu1, sigma, mu2, sigma), f"w2_gaussians_1d({mu1:.6g}, {sigma:.6g}, {mu2:.6g}, {sigma:.6g}), equal "
                                          f"standard deviations: |Δμ| = W₁ = {w1:.10g} (scipy.stats."
                                          f"wasserstein_distance on quantiles)", abs(mu1 - mu2))


def test_w2_gaussians_1d_equal_means_give_the_gap_of_the_standard_deviations(ds):
    rng = np.random.default_rng(6381)
    for _ in range(8):
        mu = float(rng.normal() * 3)
        sigma1, sigma2 = rng.uniform(0, 5, size=2).tolist()
        _w2(ds, (mu, sigma1, mu, sigma2), f"w2_gaussians_1d({mu:.6g}, {sigma1:.6g}, {mu:.6g}, {sigma2:.6g}), equal "
                                          f"means: |σ₁ - σ₂|", abs(sigma1 - sigma2))


def test_w2_gaussians_1d_with_a_zero_standard_deviation_is_a_point_mass(ds):
    """A standard deviation 0 is the point mass at μ: W₂(N(μ, σ²), δ_ν)² = E(X - ν)² = (μ - ν)² + σ² (the integral of
    the quantiles), and two point masses are at |μ₁ - μ₂|."""
    for args in ((2.0, 1.5, -0.4, 0.0), (-0.4, 0.0, 2.0, 1.5), (7.0, 0.0, -1.5, 0.0), (0.3, 2.6, 0.3, 0.0)):
        _w2(ds, args, f"w2_gaussians_1d{args} (the integral of the quantiles)", _w2_quad(*args))


def test_w2_gaussians_1d_is_at_least_w1_computed_by_scipy_on_quantiles(ds):
    """W₁ ≤ W₂ (Jensen on the same coupling), W₁ by scipy.stats.wasserstein_distance between 20 000 quantiles."""
    rng = np.random.default_rng(6382)
    for _ in range(10):
        mu1, mu2 = (rng.normal(size=2) * 2).tolist()
        sigma1, sigma2 = rng.uniform(0.1, 4, size=2).tolist()
        what = f"w2_gaussians_1d({mu1:.6g}, {sigma1:.6g}, {mu2:.6g}, {sigma2:.6g})"
        got = _w2(ds, (mu1, sigma1, mu2, sigma2), what)
        w1 = _w1_quantiles(mu1, sigma1, mu2, sigma2)
        assert got >= w1 - 1e-6, f"expected W₂ >= W₁ = {w1:.10g} for {what}, got {got!r} ({W2_HINT})"


def test_w2_gaussians_1d_moves_with_translations_and_scalings(ds):
    """Moving both laws by t does not change W₂; multiplying both means and both standard deviations by k > 0
    multiplies W₂ by k."""
    rng = np.random.default_rng(6383)
    for _ in range(10):
        mu1, mu2 = (rng.normal(size=2) * 3).tolist()
        sigma1, sigma2 = rng.uniform(0, 3, size=2).tolist()
        t, k = float(rng.normal() * 10), float(rng.uniform(0.1, 9))
        base = _w2(ds, (mu1, sigma1, mu2, sigma2), f"w2_gaussians_1d({mu1:.6g}, {sigma1:.6g}, {mu2:.6g}, "
                                                   f"{sigma2:.6g})")
        _w2(ds, (mu1 + t, sigma1, mu2 + t, sigma2), f"w2_gaussians_1d with both means moved by {t:.6g}, the same as "
                                                    f"without the move", base)
        _w2(ds, (k * mu1, k * sigma1, k * mu2, k * sigma2), f"w2_gaussians_1d with everything multiplied by "
                                                            f"{k:.6g}, {k:.6g} times W₂", k * base)


def test_w2_gaussians_1d_satisfies_the_triangle_inequality(ds):
    rng = np.random.default_rng(6384)
    for _ in range(20):
        laws = [(float(rng.normal() * 3), float(rng.uniform(0, 3))) for _ in range(3)]
        d = {}
        for i, j in ((0, 1), (1, 2), (0, 2)):
            d[i, j] = _w2(ds, (*laws[i], *laws[j]), f"w2_gaussians_1d{(*laws[i], *laws[j])}")
        assert d[0, 2] <= d[0, 1] + d[1, 2] + 1e-12, (
            f"expected W₂(a, c) <= W₂(a, b) + W₂(b, c) for the laws (mu, sigma) {laws}, got {d[0, 2]!r} > "
            f"{d[0, 1]!r} + {d[1, 2]!r} ({W2_HINT})")


def test_w2_gaussians_1d_returns_a_python_float(ds):
    for args, text in (((9, 1, -3, 36), "Python integers"), ((np.float64(9.0), np.float64(1.0), np.float64(-3.0),
                                                              np.float64(36.0)), "np.float64"),
                       ((np.int64(9), np.int64(1), np.int64(-3), np.int64(36)), "np.int64"),
                       ((np.float32(9.0), np.float32(1.0), np.float32(-3.0), np.float32(36.0)), "np.float32")):
        _w2(ds, args, f"w2_gaussians_1d(9, 1, -3, 36) with {text}, a Python float (gaps 12 and -35)", 37.0)


W2_BAD_VALUES = [(np.nan, "nan"), (np.inf, "inf"), (-np.inf, "-inf"), (True, "a bool (True)"),
                 (False, "a bool (False)"), (np.bool_(True), "a NumPy bool"), (None, "None"), ("1.5", "a string"),
                 ([1.5], "a list, not a number"), (1.5 + 0j, "a complex number, not a real one")]
W2_REFUSALS = [(position, value, f"{name} is {text}")
               for position, name in enumerate(("mu1", "sigma1", "mu2", "sigma2")) for value, text in W2_BAD_VALUES]
W2_REFUSALS += [(1, -0.5, "sigma1 is negative"), (3, -2.0, "sigma2 is negative"),
                (1, -1e-9, "sigma1 is a little below 0"), (3, np.float64(-0.25), "sigma2 is np.float64(-0.25)")]
W2_IDS = [f"{name}-{tag}" for name in ("mu1", "sigma1", "mu2", "sigma2")
          for tag in ("nan", "inf", "minus-inf", "true", "false", "numpy-bool", "none", "string", "list", "complex")]
W2_IDS += ["sigma1-negative", "sigma2-negative", "sigma1-just-below-zero", "sigma2-numpy-negative"]


@pytest.mark.parametrize("position, value, why", W2_REFUSALS, ids=W2_IDS)
def test_w2_gaussians_1d_refusals(ds, position, value, why):
    args = [0.7, 1.2, -0.3, 2.4]
    args[position] = value
    _expect_error(ValueError, lambda: ds.w2_gaussians_1d(*args), f"w2_gaussians_1d{tuple(args)!r}", why)


def test_w2_gaussians_1d_refuses_two_negative_standard_deviations(ds):
    """Even when σ₁ - σ₂ would make sense, a negative standard deviation is refused."""
    _expect_error(ValueError, lambda: ds.w2_gaussians_1d(0.0, -1.0, 0.0, -3.0), "w2_gaussians_1d(0.0, -1.0, 0.0, -3.0)",
                  "both standard deviations are negative")
