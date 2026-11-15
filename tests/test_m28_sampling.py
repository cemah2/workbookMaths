"""Tests of mymath.sampling (chapter M28): a configuration of points whose Gram matrix is given, a law tempered from its
probabilities, and the smallest set of outcomes that reaches a given probability mass.

Oracles: the eigenvalues and unit eigenvectors of ``scipy.linalg.eigh`` and the singular values of
``scipy.linalg.svd``; the Gram matrix X Xᵀ rebuilt from your points, their distances compared with those of the points
that made G (``scipy.spatial.distance.pdist``) and with G[i, i] + G[j, j] - 2 G[i, j], and the isometry that sends your
points onto them (``scipy.linalg.orthogonal_procrustes``); the best approximation of rank dim (Eckart-Young) given by
the SVD; ``scipy.special.softmax`` of ln p / T, and the limits T → 0 and T → ∞ written in the test;
``scipy.stats.entropy``; a stable sort ``np.argsort(-p, kind="stable")`` and an exhaustive search of the smallest sets
on small laws. Never another function of yours. Plus properties: the columns of X by decreasing eigenvalue, orthogonal,
with the sign convention of the docstring (also when the first coordinate is 0), the rank and the zero columns, the
threshold s (relative, at least tol, given by tol), the points of Q G Qᵀ (Q a permutation) that are the points
permuted, √c X for c G, the scores of a PCA for centered points, positions found again from distances (double
centering); T = 1 that gives p back, zeros kept at 0, the order kept, the entropy that grows with T, T = 0 and T = inf,
no underflow for a small T, the softmax of scores divided by T; the minimality and the order of the smallest set, ties
broken by the smaller index, the outcome that crosses mass kept, the tolerance 1e-9, never an outcome of probability 0,
mass = 1, the rounding that never reaches mass; inputs left unchanged, arrays of floats and of integers, and every
refusal of the docstrings. They describe the expected behaviour without showing the solution.

    pytest tests/test_m28_sampling.py              # your code
    pytest tests/test_m28_sampling.py --impl=ref   # the reference
"""

import ast
import inspect
import itertools
import math
import warnings

import numpy as np
import pytest
from scipy import linalg, special, stats
from scipy.spatial import distance


@pytest.fixture
def sp_module(mymath_module):
    """The module itself: for the tests that check that your functions never write into the arrays they receive, and
    for the check of what the module uses."""
    return mymath_module("sampling")


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
def sp(sp_module):
    return _OnCopies(sp_module)


def _result(call, expected, what="", hint="", on_warning=None):
    """call(), any error other than NotImplementedError being reported with what was expected first; on_warning(text)
    gives the cause of a classic RuntimeWarning."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)
        try:
            return call()
        except NotImplementedError:
            raise                 # a function not written yet: ⏳
        except RuntimeWarning as warning:
            cause = on_warning(str(warning)) if on_warning else ""
            hint = f"{hint}; here {cause}" if cause else hint
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
    """A short text for an array: more than 12 numbers show the first 12 (flattened), then « … »."""
    arr = np.asarray(v, dtype=float)
    if arr.size > 12:
        return np.array2string(arr.ravel()[:12], precision=6, suppress_small=True,
                               max_line_width=10_000).replace("]", " …]") + f" (shape {arr.shape})"
    return np.array2string(arr, precision=6, suppress_small=True, max_line_width=10_000).replace("\n", "")


def _show_any(v):
    """_show for something that may not be an array of numbers."""
    if isinstance(v, np.ndarray) and v.dtype.kind in "iub":
        return f"array({v.tolist()})"
    try:
        return _show(v)
    except (TypeError, ValueError):
        return repr(v)


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
    return (got.shape == value.shape and bool(np.all(np.isfinite(value))) and bool(np.all(np.isfinite(got)))
            and np.allclose(got, value, rtol=rtol, atol=atol))


def _first_match(got, want, candidates, rtol=1e-9, atol=1e-11):
    """The text of the first classic error whose value got matches (and that differs from the right value), or ""."""
    for value, text in candidates:
        if value is not None and not _matches(value, want, rtol, atol) and _matches(got, value, rtol, atol):
            return text
    return ""


def _float_matrix(got, shape, what, hint=""):
    assert isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape, (
        f"expected {what} as a numpy.ndarray of floats of shape {shape}, got {type(got).__name__}"
        + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray) else "")
        + (f" ({hint})" if hint else ""))


# --- what the module may use ----------------------------------------------------------------------------------------

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


def _where(statement):
    return statement.name if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)) else "the module level"


def _uses(tree, names):
    """Each use of an imported name (or of a chain of attributes on it): (where, dotted path), e.g.
    ("points_from_gram", "numpy.linalg.svd"); ``where`` is the top-level function, or "the module level"."""
    inner = {id(node.value) for node in ast.walk(tree) if isinstance(node, ast.Attribute)}
    uses = []
    for statement in tree.body:
        where = _where(statement)
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


ALLOWED_LINALG = {"eigh", "LinAlgError"}
FORBIDDEN_STRINGS = {"linalg", "svd", "eig", "eigvals", "eigvalsh", "pinv", "lstsq", "matrix_power", "norm", "det",
                     "inv", "solve", "cholesky", "qr", "softmax", "logsumexp", "special"}


def _string_uses(tree):
    """getattr(np, "linalg") and the like, and __import__("scipy") or importlib.import_module("sklearn…"): a forbidden
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
            if name in ("__import__", "import_module") and any(
                    t.startswith(("scipy", "sklearn", "numpy.linalg")) for t in texts):
                found.append(f"{name}({texts[0]!r}) in {where}")
    return found


def test_module_uses_numpy_but_from_np_linalg_only_eigh_and_no_scipy_nor_sklearn(sp_module):
    """The docstring allows NumPy, but from np.linalg only eigh, and no SciPy nor scikit-learn (scipy.special.softmax
    and logsumexp would give temper, scipy.linalg and sklearn.manifold the points): the tests compare your results with
    scipy.linalg.eigh, scipy.linalg.svd and scipy.special.softmax. Only the code counts: a comment, a docstring or an
    import never used is not a use. ``np.linalg.LinAlgError`` (an exception, not a computation) is not counted."""
    try:
        tree = ast.parse(inspect.getsource(sp_module))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = []
    for where, path in _uses(tree, _imported_names(tree)):
        parts = path.split(".")
        shown = ".".join(["np"] + parts[1:]) if parts[0] == "numpy" else path
        if parts[0] in ("scipy", "sklearn"):
            found.append(f"{shown} in {where}")
        elif parts[0] == "numpy" and len(parts) > 1 and parts[1] == "linalg":
            if len(parts) > 2 and parts[2] in ALLOWED_LINALG:
                continue
            found.append(f"{shown} in {where}")
    found += _string_uses(tree)
    assert not found, (f"expected NumPy only, with nothing from np.linalg but eigh and no SciPy nor scikit-learn, found "
                       f"{sorted(set(found))} (the tests compare your results with scipy.linalg.eigh, scipy.linalg.svd "
                       f"and scipy.special.softmax: np.linalg.eigh, np.sqrt, np.log, np.exp, np.argsort and np.cumsum "
                       f"are enough)")


# --- points_from_gram -----------------------------------------------------------------------------------------------

GRAM_HINT = ("the eigenvalues and unit eigenvectors of G by np.linalg.eigh (increasing order: reverse it), an eigenvalue "
             "below -s refused, those in [-s, s] set to 0 (s = tol · max(1, max |G[i, j]|)), then column k of X is "
             "√λ_k times the k-th unit eigenvector (column k of the matrix returned by eigh), dim columns (the rank "
             "by default, at least 1), and in each column the first coordinate of absolute value > 1e-8 made positive")

# A 4 × 4 orthogonal matrix of rationals (rows of norm 7, pairwise orthogonal): G = Q diag(λ) Qᵀ has exactly the
# eigenvalues λ, up to rounding.
Q_SEVEN = np.array([[2, -2, -4, -5], [2, 2, -5, 4], [4, 5, 2, -2], [5, -4, 2, 2]]) / 7.0
# Another one whose first two columns start with 0: the first point has the coordinate 0 on the two main axes.
Q_ZERO = np.column_stack([np.array([0, -5, 2, 14]) / 15.0, np.array([0, 10, 11, 2]) / 15.0,
                          np.array([9, -8, 8, -4]) / 15.0, np.array([-12, -6, 6, -3]) / 15.0])


def _threshold(G, tol=1e-9):
    """s = tol · max(1, max |G[i, j]|), as the docstring defines it."""
    return tol * max(1.0, float(np.max(np.abs(np.asarray(G, dtype=float)))))


def _spectrum(G):
    """The eigenvalues by decreasing order and the unit eigenvectors in the columns, by scipy.linalg.eigh on the
    symmetric part of G."""
    G = np.asarray(G, dtype=float)
    w, V = linalg.eigh((G + G.T) / 2)
    return w[::-1], V[:, ::-1]


def _kept(G, tol=1e-9):
    """The eigenvalues by decreasing order, those ≤ s set to 0, and the rank (at least 1 column by default)."""
    w, V = _spectrum(G)
    w = np.where(w > _threshold(G, tol), w, 0.0)
    return w, V, max(1, int(np.count_nonzero(w)))


def _with_signs(X):
    """The sign convention of the docstring, applied by the test: in each column, the first coordinate of absolute
    value > 1e-8 made positive."""
    X = np.array(X, dtype=float)
    for k in range(X.shape[1]):
        large = np.flatnonzero(np.abs(X[:, k]) > 1e-8)
        if large.size and X[large[0], k] < 0:
            X[:, k] = -X[:, k]
    return X


def _expected_points(G, dim=None, tol=1e-9):
    """The X of the docstring from scipy.linalg.eigh: its coordinates are meaningful only when the kept eigenvalues are
    distinct (otherwise compare Gram matrices or distances)."""
    w, V, rank = _kept(G, tol)
    k = rank if dim is None else dim
    return _with_signs(V[:, :k] * np.sqrt(w[:k]))


def _from_spectrum(eigenvalues, Q=Q_SEVEN):
    """Q diag(λ) Qᵀ, made exactly symmetric."""
    G = (Q * np.asarray(eigenvalues, dtype=float)) @ Q.T
    return (G + G.T) / 2


def _random_orthogonal(rng, n):
    """A random orthogonal matrix (QR of a Gaussian matrix, scipy.linalg.qr)."""
    Q, R = linalg.qr(rng.normal(size=(n, n)))
    return Q * np.sign(np.diag(R))


def _distinct_gram(rng, n, rank=None, low=0.3, gap=0.25):
    """A Gram matrix Q diag(λ) Qᵀ with well separated eigenvalues λ_1 > … > λ_rank > 0 (gaps ≥ gap) and n - rank zeros,
    so that the coordinates of X are well defined."""
    rank = n if rank is None else rank
    steps = gap + rng.uniform(0, 1.5, size=rank)
    lam = np.zeros(n)
    lam[:rank] = (low + np.cumsum(steps))[::-1]
    return _from_spectrum(lam, _random_orthogonal(rng, n)), lam


def _first_sign_problem(X):
    """(column, row, value) of the first column whose first coordinate of absolute value > 1e-8 is negative, or None."""
    for k in range(X.shape[1]):
        large = np.flatnonzero(np.abs(X[:, k]) > 1e-8)
        if large.size and X[large[0], k] < 0:
            return k, int(large[0]), float(X[large[0], k])
    return None


def _points_hint(got, G, dim=None, tol=1e-9):
    """GRAM_HINT, plus the classic error that the result got matches (compared up to the sign of each column), if any."""
    try:
        X = np.asarray(got, dtype=float)
    except (TypeError, ValueError):
        return GRAM_HINT
    G = np.asarray(G, dtype=float)
    n = G.shape[0]
    w, V, rank = _kept(G, tol)
    k = rank if dim is None else dim
    if X.ndim != 2 or X.shape != (n, k):
        if X.ndim == 2 and X.shape == (k, n):
            return f"{GRAM_HINT}; here X is transposed: one ROW per point, shape (n, dim) = {(n, k)}"
        if dim is None and X.shape == (n, n) and rank < n:
            return (f"{GRAM_HINT}; here n = {n} columns were returned: dim defaults to the rank of G, the number of "
                    f"eigenvalues larger than s ({rank} here)")
        if dim is None and X.ndim == 2 and X.shape[0] == n:
            return (f"{GRAM_HINT}; here {X.shape[1]} columns instead of the rank {rank}: an eigenvalue counts when it is "
                    f"larger than s = tol · max(1, max |G[i, j]|) = {_threshold(G, tol):.3g}")
        return GRAM_HINT
    want = V[:, :k] * np.sqrt(w[:k])
    raw, raw_vectors = linalg.eigh((G + G.T) / 2)
    s = _threshold(G, tol)
    with np.errstate(all="ignore"):
        candidates = [
            (raw_vectors[:, :k] * np.sqrt(np.where(raw[:k] > s, raw[:k], 0.0)),
             "eigh sorts the eigenvalues in INCREASING order: reverse them, so that the columns come by decreasing "
             "eigenvalue"),
            (want[:, ::-1], "the columns come by DECREASING eigenvalue: the first column belongs to the largest one"),
            (V[:, :k] * w[:k], "the square root is missing: column k is √λ_k times the k-th unit eigenvector (X Xᵀ "
                               "would otherwise have the eigenvalues λ_k², not λ_k)"),
            (V[:, :k], "each unit eigenvector must be multiplied by √λ_k"),
            (V[:k, :].T * np.sqrt(w[:k]), "an eigenvector is a COLUMN of the matrix returned by eigh (vectors[:, k]), "
                                          "not a row"),
            (V[:, :k] * np.sqrt(np.clip(raw[::-1][:k], 0, None)),
             f"an eigenvalue in [-s, s] counts as 0, a small positive one too (s = tol · max(1, max |G[i, j]|) = "
             f"{s:.3g}): set it to 0 before the square root"),
        ]
    text = _first_match(np.abs(X), np.abs(want), [(None if c is None else np.abs(c), t) for c, t in candidates],
                        rtol=1e-6, atol=1e-8 * max(1.0, float(np.sqrt(np.max(np.abs(G))))))
    if text:
        return f"{GRAM_HINT}; here {text}"
    problem = _first_sign_problem(X)
    if problem:
        col, row, value = problem
        zero = np.flatnonzero(np.abs(X[:row, col]) <= 1e-8)
        if row > 0 and zero.size == row:
            return (f"{GRAM_HINT}; here, in column {col}, the first coordinate of absolute value > 1e-8 is X[{row}, "
                    f"{col}] = {value:.6g} < 0 (the coordinates above it are 0: the sign is that of the first coordinate "
                    f"of absolute value > 1e-8, not of X[0, {col}])")
        return (f"{GRAM_HINT}; here, in column {col}, the first coordinate of absolute value > 1e-8 is X[{row}, {col}] = "
                f"{value:.6g} < 0: multiply the column by -1")
    return GRAM_HINT


def _gram_warning(text):
    if "sqrt" in text:
        return ("the square root of a negative eigenvalue: the eigenvalues in [-s, s] (tiny negative ones included) "
                "are set to 0 before the square root")
    return ""


def _points(sp, G, what, dim=None, tol=None, expected="a numpy.ndarray X of shape (n, dim)"):
    """points_from_gram(G[, dim, tol]), called as the docstring allows."""
    kwargs = {}
    if dim is not None:
        kwargs["dim"] = dim
    if tol is not None:
        kwargs["tol"] = tol
    return _result(lambda: sp.points_from_gram(G, **kwargs), expected, what, GRAM_HINT, _gram_warning)


def _check_shape(got, n, k, what, G, dim=None, tol=1e-9):
    _float_matrix(got, (n, k), what, _points_hint(got, G, dim, tol))


def _check_gram(got, target, what, G, dim=None, tol=1e-9, atol=None):
    """X Xᵀ equals target (G itself, or its best approximation of rank dim)."""
    scale = max(1.0, float(np.max(np.abs(np.asarray(G, dtype=float)))))
    atol = 1e-9 * scale if atol is None else atol
    rebuilt = got @ got.T
    gap = float(np.max(np.abs(rebuilt - target)))
    assert gap <= atol, (f"expected X Xᵀ = {_show(target)} for {what}, got X Xᵀ = {_show(rebuilt)} (largest gap {gap:.3g}"
                         f"; {_points_hint(got, G, dim, tol)})")


def _check_signs(got, what, G, dim=None, tol=1e-9):
    problem = _first_sign_problem(got)
    if problem is not None:
        col, row, value = problem
        pytest.fail(f"expected the first coordinate of absolute value > 1e-8 of each column of X to be positive for "
                    f"{what}, got X[{row}, {col}] = {value:.6g} ({_points_hint(got, G, dim, tol)})")


def _check_axes(got, eigenvalues, what, G, dim=None, tol=1e-9):
    """XᵀX = diag(λ_1, …, λ_dim): orthogonal columns, by decreasing eigenvalue (the eigenvalues of scipy.linalg.eigh)."""
    scale = max(1.0, float(np.max(np.abs(np.asarray(G, dtype=float)))))
    moments = got.T @ got
    want = np.diag(eigenvalues)
    assert np.allclose(moments, want, rtol=1e-9, atol=1e-9 * scale), (
        f"expected Xᵀ X = diag{_show(eigenvalues)} for {what} (orthogonal columns, by decreasing eigenvalue), got "
        f"Xᵀ X = {_show(moments)} ({_points_hint(got, G, dim, tol)})")


def _check_distances(got, P, what, G):
    """The distances between your points are those between the points P that made G, and ‖x_i - x_j‖² = G[i, i] +
    G[j, j] - 2 G[i, j]."""
    if len(got) < 2:
        return
    G = np.asarray(G, dtype=float)
    scale = max(1.0, float(np.max(np.abs(G))))
    squared = distance.pdist(got, "sqeuclidean")
    i, j = np.triu_indices(len(G), 1)
    from_gram = G[i, i] + G[j, j] - 2 * G[i, j]
    assert np.allclose(squared, from_gram, rtol=1e-9, atol=1e-9 * scale), (
        f"expected ‖x_i - x_j‖² = G[i, i] + G[j, j] - 2 G[i, j] = {_show(from_gram)} for {what}, got {_show(squared)} "
        f"({_points_hint(got, G)})")
    if P is not None:
        want = distance.pdist(P)
        _close(distance.pdist(got), want, f"the distances between the points of {what}", rtol=1e-7,
               atol=1e-7 * math.sqrt(scale), hint=_points_hint(got, G))


def test_points_from_gram_docstring_examples(sp):
    G = [[13, 5], [5, 13]]
    call = "points_from_gram([[13, 5], [5, 13]]) (two vectors of length √13 with cosine 5/13)"
    got = _points(sp, G, call)
    _check_shape(got, 2, 2, call, G)
    _close(got, [[3.0, 2.0], [3.0, -2.0]], call, rtol=0, atol=1e-12, hint=_points_hint(got, G))
    G = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    call = "points_from_gram([[1, 2, 3], [2, 4, 6], [3, 6, 9]]) (rank 1: three points on a line)"
    got = _points(sp, G, call)
    _check_shape(got, 3, 1, call, G)
    _close(got, [[1.0], [2.0], [3.0]], call, rtol=0, atol=1e-12, hint=_points_hint(got, G))
    call = "points_from_gram([[1, 2, 3], [2, 4, 6], [3, 6, 9]], dim=2) (a zero second column)"
    got = _points(sp, G, call, dim=2)
    _check_shape(got, 3, 2, call, G, dim=2)
    _close(got, [[1.0, 0.0], [2.0, 0.0], [3.0, 0.0]], call, rtol=0, atol=1e-12, hint=_points_hint(got, G, 2))


POINT_CASES = [((1, 1), 1.0, "a single point on a line"), ((2, 1), 1.0, "two points on a line"),
               ((2, 2), 1.0, "two points of the plane"), ((3, 2), 1.0, "three points of the plane"),
               ((4, 3), 2.0, "four points in space"), ((6, 2), 300.0, "six towns, coordinates in hundreds of km"),
               ((5, 3), 0.003, "five sensors, coordinates in mm"), ((9, 4), 1.0, "nine points in dimension 4"),
               ((16, 5), 1.5, "sixteen points in dimension 5"), ((40, 7), 1.0, "forty points in dimension 7"),
               ((2, 4), 1.0, "two points in dimension 4: rank 2"), ((3, 6), 1.0, "three points in dimension 6: rank 3")]


@pytest.mark.parametrize("shape, scale, text", POINT_CASES,
                         ids=[f"{s[0]}-points-dim-{s[1]}" for s, _, _ in POINT_CASES])
def test_points_from_gram_rebuild_G_and_the_distances_of_random_points(sp, shape, scale, text):
    """Points P (rows) drawn at random, G = P Pᵀ: your X has rank(G) = min(n, d) columns, X Xᵀ = G, the same distances
    as P, and an orthogonal matrix R (scipy.linalg.orthogonal_procrustes) sends X onto P: the points up to an isometry
    that fixes the origin."""
    rng = np.random.default_rng(6500 + POINT_CASES.index((shape, scale, text)))
    P = rng.normal(size=shape) * scale + rng.normal(size=shape[1]) * scale
    G = P @ P.T
    n, d = shape
    rank = min(n, d)
    what = f"points_from_gram(G) for G = P Pᵀ, P of shape {shape} ({text})"
    got = _points(sp, G, what)
    _check_shape(got, n, rank, what, G)
    _check_gram(got, G, what, G)
    _check_distances(got, P, what, G)
    padded = np.hstack([got, np.zeros((n, d - rank))])
    R, _ = linalg.orthogonal_procrustes(padded, P)
    _close(padded @ R, P, f"X R for the best orthogonal R (Procrustes), {what}", rtol=1e-7,
           atol=1e-7 * scale * math.sqrt(d), hint=_points_hint(got, G))


def test_points_from_gram_coordinates_match_scipy_eigh_with_the_sign_convention(sp):
    """With distinct eigenvalues, the coordinates are fixed: column k is √λ_k times the k-th unit eigenvector of
    scipy.linalg.eigh, by decreasing eigenvalue, with the sign convention of the docstring."""
    rng = np.random.default_rng(6512)
    for n, rank in ((2, 2), (3, 3), (5, 5), (6, 3), (8, 8), (10, 4)):
        G, lam = _distinct_gram(rng, n, rank)
        what = f"points_from_gram(G) for a {n} × {n} Gram matrix of eigenvalues {_show(lam)}"
        got = _points(sp, G, what)
        _check_shape(got, n, rank, what, G)
        _close(got, _expected_points(G), what, rtol=1e-8, atol=1e-9, hint=_points_hint(got, G))


def test_points_from_gram_columns_are_orthogonal_by_decreasing_eigenvalue(sp):
    """Xᵀ X = diag(λ_1, …, λ_dim) with λ_1 ≥ λ_2 ≥ … (scipy.linalg.eigh), for distinct and for repeated eigenvalues (any
    choice of the columns of a repeated eigenvalue suits)."""
    rng = np.random.default_rng(6513)
    cases = [(_distinct_gram(rng, 7)[0], "distinct eigenvalues"),
             (_from_spectrum([3.5, 3.5, 1.25, 1.25, 0.4], _random_orthogonal(rng, 5)),
              "eigenvalues 3.5, 3.5, 1.25, 1.25, 0.4"),
             (_from_spectrum([2.5, 2.5, 2.5, 0.0, 0.0, 0.0], _random_orthogonal(rng, 6)), "eigenvalue 2.5 three times"),
             (np.eye(5) - np.ones((5, 5)) / 5, "the 5 vertices of a regular simplex (I - 11ᵀ/5)")]
    for G, text in cases:
        w, _, rank = _kept(G)
        what = f"points_from_gram(G) for G with {text}"
        got = _points(sp, G, what)
        _check_shape(got, len(G), rank, what, G)
        _check_axes(got, w[:rank], what, G)
        _check_gram(got, G, what, G)
        _check_signs(got, what, G)


def test_points_from_gram_vertices_of_a_regular_simplex_are_all_at_distance_sqrt_2(sp):
    """G = I - 11ᵀ/n is the Gram matrix of the n vertices of a regular simplex, centered: rank n - 1, eigenvalue 1
    repeated, every distance √2."""
    for n in (3, 4, 6):
        G = np.eye(n) - np.ones((n, n)) / n
        what = f"points_from_gram(I - 11ᵀ/{n})"
        got = _points(sp, G, what)
        _check_shape(got, n, n - 1, what, G)
        _close(distance.pdist(got), np.full(n * (n - 1) // 2, math.sqrt(2)), f"the distances of {what}", rtol=1e-9,
               atol=1e-9, hint=_points_hint(got, G))
        _close(got.sum(axis=0), np.zeros(n - 1), f"the sum of the points of {what} (centered)", rtol=0, atol=1e-9,
               hint=_points_hint(got, G))


def test_points_from_gram_sign_convention_holds_in_every_column(sp):
    """On random Gram matrices (distinct, repeated or zero eigenvalues, dim larger than the rank): in each column, the
    first coordinate of absolute value > 1e-8 is positive; a zero column stays zero."""
    rng = np.random.default_rng(6514)
    for k in range(12):
        n = int(rng.integers(2, 9))
        d = int(rng.integers(1, n + 1))
        P = rng.normal(size=(n, d)) * rng.uniform(0.5, 5)
        G = P @ P.T
        dim = int(rng.integers(1, n + 1)) if k % 3 == 0 else None
        what = f"points_from_gram(G{'' if dim is None else f', dim={dim}'}) for G = P Pᵀ, P of shape {(n, d)}"
        got = _points(sp, G, what, dim=dim)
        _check_shape(got, n, d if dim is None else dim, what, G, dim)
        _check_signs(got, what, G, dim)


SIGN_FLIPS = [(1, 1, 1, 1), (1, -1, 1, 1), (1, 1, -1, 1), (1, -1, -1, -1)]


@pytest.mark.parametrize("flips", SIGN_FLIPS, ids=["as-is", "point-1-flipped", "point-2-flipped", "three-flipped"])
def test_points_from_gram_sign_when_the_first_coordinate_is_zero(sp, flips):
    """The first point has the coordinate 0 on the two main axes: in the first two columns, the sign is that of the
    SECOND coordinate (the first one of absolute value > 1e-8), whatever the rounding of the 0."""
    X_true = np.diag(flips) @ Q_ZERO * np.sqrt([5.29, 2.25, 0.64, 0.16])
    G = X_true @ X_true.T
    G = (G + G.T) / 2
    what = f"points_from_gram(G) for G = X Xᵀ, X = D Q diag(2.3, 1.5, 0.8, 0.4), D = diag{flips} (X[0, 0] = X[0, 1] = 0)"
    got = _points(sp, G, what)
    _check_shape(got, 4, 4, what, G)
    _check_signs(got, what, G)
    _close(got, _with_signs(X_true), what, rtol=1e-8, atol=1e-9, hint=_points_hint(got, G))


def test_points_from_gram_sign_threshold_applies_to_the_coordinates_of_X(sp):
    """tol = 0 keeps the eigenvalue 1e-12, whose column of X is 1e-6 v with v = (0.0007, -0.99999976): its first
    coordinate, 7e-10, is below 1e-8 (although v[0] = 0.0007 is not), so the sign is that of the second one."""
    v = np.array([0.0007, -math.sqrt(1 - 0.0007 ** 2)])
    w = np.array([-v[1], v[0]])
    G = 2.25 * np.outer(w, w) + 1e-12 * np.outer(v, v)
    G = (G + G.T) / 2
    what = "points_from_gram(G, tol=0) for G = 2.25 w wᵀ + 1e-12 v vᵀ, v = (0.0007, -0.99999976), w ⟂ v"
    got = _points(sp, G, what, tol=0.0, expected="an X of shape (2, 2)")
    _check_shape(got, 2, 2, what, G, tol=0.0)
    want = np.column_stack([1.5 * w, -1e-6 * v])
    assert np.allclose(got, want, rtol=1e-6, atol=1e-13), (
        f"expected X = {np.array2string(want, precision=10, max_line_width=10_000)} for {what}, got "
        f"{np.array2string(np.asarray(got), precision=10, max_line_width=10_000)} ({GRAM_HINT}; here the threshold 1e-8 "
        f"applies to the coordinates of X (7e-10 in column 1), not to those of the unit eigenvector v)")


RANK_CASES = [(5, 1, 1.0), (7, 2, 3.0), (8, 3, 1.0), (12, 3, 40.0), (20, 6, 0.2)]


@pytest.mark.parametrize("n, r, scale", RANK_CASES, ids=[f"{n}-points-rank-{r}" for n, r, _ in RANK_CASES])
def test_points_from_gram_default_dim_is_the_rank_despite_rounding(sp, n, r, scale):
    """G = P Pᵀ with P of shape (n, r), r < n, computed in floats: its n - r zero eigenvalues come out as tiny numbers of
    either sign (inside [-s, s]); they count as 0, so X has r columns, without a ValueError."""
    rng = np.random.default_rng(6519 + RANK_CASES.index((n, r, scale)))
    P = rng.normal(size=(n, r)) * scale
    G = P @ P.T
    what = f"points_from_gram(G) for G = P Pᵀ, P of shape {(n, r)} (rank {r})"
    got = _points(sp, G, what, expected=f"an X of shape {(n, r)}")
    _check_shape(got, n, r, what, G)
    _check_gram(got, G, what, G)
    _check_distances(got, P, what, G)


def test_points_from_gram_dim_larger_than_the_rank_gives_zero_columns(sp):
    """With dim larger than the rank, the columns of the eigenvalues that count as 0 are zero (exactly), and X Xᵀ is
    still G."""
    rng = np.random.default_rng(6524)
    for n, r, dim in ((6, 2, 4), (5, 1, 5), (9, 4, 7)):
        P = rng.normal(size=(n, r)) * 2.0
        G = P @ P.T
        what = f"points_from_gram(G, dim={dim}) for G = P Pᵀ of rank {r} ({n} points)"
        got = _points(sp, G, what, dim=dim)
        _check_shape(got, n, dim, what, G, dim)
        tiny = bool(np.all(np.abs(got[:, r:]) <= 1e-6))
        assert np.all(got[:, r:] == 0), (
            f"expected the last {dim - r} columns of X to be zero for {what} (the eigenvalues in [-s, s] count as 0, "
            f"so their columns are zero), got {_show(got[:, r:])} ({_points_hint(got, G, dim)}"
            + ("; here an eigenvalue of absolute value ≤ s must be set to 0 before the square root, not only the "
               "negative ones)" if tiny else ")"))
        _check_gram(got, G, what, G, dim)
        _check_signs(got, what, G, dim)


def test_points_from_gram_dim_smaller_than_the_rank_is_the_best_approximation(sp):
    """With dim smaller than the rank, X Xᵀ is the best approximation of G of rank dim (Eckart-Young): U_k S_k U_kᵀ from
    scipy.linalg.svd, at the distance √(Σ_{j>k} s_j²) of G in Frobenius norm."""
    rng = np.random.default_rng(6525)
    G, _ = _distinct_gram(rng, 6)
    U, S, _ = linalg.svd(G)
    for dim in range(1, 6):
        target = (U[:, :dim] * S[:dim]) @ U[:, :dim].T
        what = f"points_from_gram(G, dim={dim}) for a 6 × 6 Gram matrix of singular values {_show(S)}"
        got = _points(sp, G, what, dim=dim)
        _check_shape(got, 6, dim, what, G, dim)
        _check_gram(got, target, what + " (X Xᵀ = U_k S_k U_kᵀ, Eckart-Young)", G, dim)
        gap = float(np.linalg.norm(G - got @ got.T))
        best = float(np.sqrt(np.sum(S[dim:] ** 2)))
        assert abs(gap - best) <= 1e-9 * max(1.0, best), (
            f"expected ‖G - X Xᵀ‖_F = √(Σ_(j>{dim}) s_j²) = {best:.10g} for {what}, got {gap:.10g} "
            f"({_points_hint(got, G, dim)})")
        _close(got, _expected_points(G, dim), what, rtol=1e-8, atol=1e-9, hint=_points_hint(got, G, dim))


def test_points_from_gram_of_a_zero_matrix_and_of_a_single_point(sp):
    """The zero matrix has rank 0: X has one zero column (at least 1 column), or dim zero columns. A 1 × 1 matrix [[c]]
    is the point √c on a line (positive, by the sign convention)."""
    for G, dim, want, text in ((np.zeros((3, 3)), None, np.zeros((3, 1)), "the 3 × 3 zero matrix"),
                               (np.zeros((3, 3)), 2, np.zeros((3, 2)), "the 3 × 3 zero matrix, dim=2"),
                               ([[0.0]], None, [[0.0]], "[[0.0]]"),
                               ([[7.84]], None, [[2.8]], "[[7.84]], a single point at distance 2.8 from the origin"),
                               ([[1e-12]], None, [[0.0]], "[[1e-12]], an eigenvalue ≤ s = 1e-9 that counts as 0")):
        what = f"points_from_gram({text})"
        got = _points(sp, G, what, dim=dim)
        _check_shape(got, len(want), len(want[0]), what, G, dim)
        _close(got, want, what, rtol=1e-12, atol=0, hint=_points_hint(got, G, dim))


def _threshold_case(eigenvalues, small, tol):
    """Q diag(λ) Qᵀ with one more eigenvalue `small` × s, s computed from G as the docstring says (with the small
    eigenvalue at 0 first: it changes max |G[i, j]| by far less than s)."""
    base = _from_spectrum(list(eigenvalues) + [0.0])
    s = _threshold(base, tol)
    lam = list(eigenvalues) + [small * s]
    return _from_spectrum(lam), lam


THRESHOLD_CASES = [
    ((6.5, 2.25, 1.5), -0.5, 1e-9, 3, "an eigenvalue -0.5 s, inside [-s, s]: it counts as 0, no error"),
    ((6.5, 2.25, 0.0), 0.5, 1e-9, 2, "an eigenvalue 0.5 s, inside [-s, s]: it counts as 0"),
    ((6.5, 2.25, 0.0), 2.0, 1e-9, 3, "an eigenvalue 2 s, larger than s: it counts"),
    ((0.03, 0.011, 0.0), 0.5, 1e-9, 2, "entries below 1: s = tol · max(1, …) = tol, and 0.5 tol counts as 0"),
    ((5.2e4, 1.3e4, 0.0), 0.5, 1e-9, 2, "entries near 10⁴: s = tol · max |G[i, j]|, and 0.5 s counts as 0"),
    ((4.5, 1.75, 0.0), 0.5, 1e-4, 2, "tol = 1e-4: s = 1e-4 · max |G[i, j]|, and 0.5 s counts as 0"),
    ((4.5, 1.75, 0.8), -0.5, 1e-4, 3, "tol = 1e-4: an eigenvalue -0.5 s counts as 0, no error"),
]


@pytest.mark.parametrize("eigenvalues, small, tol, rank, text", THRESHOLD_CASES,
                         ids=["minus-half-s", "plus-half-s", "plus-two-s", "s-is-at-least-tol", "s-is-relative",
                              "tol-given", "tol-given-negative"])
def test_points_from_gram_threshold_s_decides_the_rank(sp, eigenvalues, small, tol, rank, text):
    """s = tol · max(1, max |G[i, j]|): the eigenvalues in [-s, s] count as 0, those above s count."""
    G, lam = _threshold_case(eigenvalues, small, tol)
    s = _threshold(G, tol)
    assert abs(lam[-1] - small * s) <= 0.01 * s, "oracle: s moved"
    what = f"points_from_gram(G{'' if tol == 1e-9 else f', tol={tol}'}) for G = Q diag{_show(lam)} Qᵀ ({text})"
    got = _points(sp, G, what, tol=None if tol == 1e-9 else tol, expected=f"an X of shape {(4, rank)}")
    _check_shape(got, 4, rank, what, G, tol=tol)
    _close(got, _expected_points(G, tol=tol), what, rtol=1e-8, atol=1e-8, hint=_points_hint(got, G, tol=tol))


@pytest.mark.parametrize("eigenvalues, small, tol, text", [
    ((6.5, 2.25, 1.5), -2.0, 1e-9, "an eigenvalue -2 s, below -s"),
    ((4.5, 1.75, 0.8), -2.0, 1e-4, "tol = 1e-4, an eigenvalue -2 s, below -s"),
    ((0.03, 0.011, 0.004), -2.0, 1e-9, "entries below 1, an eigenvalue -2 tol, below -s = -tol"),
], ids=["minus-two-s", "tol-given-minus-two-s", "small-entries-minus-two-tol"])
def test_points_from_gram_refuses_an_eigenvalue_below_minus_s(sp, eigenvalues, small, tol, text):
    G, lam = _threshold_case(eigenvalues, small, tol)
    kwargs = {} if tol == 1e-9 else {"tol": tol}
    _expect_error(ValueError, lambda: sp.points_from_gram(G, **kwargs),
                  f"points_from_gram(G{'' if tol == 1e-9 else f', tol={tol}'}) for G = Q diag{_show(lam)} Qᵀ",
                  f"{text}: G is not positive semi-definite, it is no Gram matrix")


def test_points_from_gram_with_tol_0_counts_every_positive_eigenvalue(sp):
    """With tol = 0, s = 0: an eigenvalue 1e-12 counts (here G is diagonal, so its eigenvalues are exact)."""
    G = np.diag([2.25, 0.0, 1e-12])
    what = "points_from_gram(diag(2.25, 0, 1e-12), tol=0)"
    got = _points(sp, G, what, tol=0.0, expected="an X of shape (3, 2)")
    _check_shape(got, 3, 2, what, G, tol=0.0)
    _close(got, [[1.5, 0.0], [0.0, 0.0], [0.0, 1e-6]], what, rtol=1e-9, atol=0, hint=_points_hint(got, G, tol=0.0))


def test_points_from_gram_symmetry_is_judged_with_the_threshold_s(sp):
    """|G[i, j] - G[j, i]| ≤ s counts as symmetric (X Xᵀ is then G up to s); 2 s does not."""
    G = _from_spectrum([5.5, 2.75, 1.25, 0.5])
    s = _threshold(G)
    nearly = G.copy()
    nearly[2, 0] += 0.5 * s
    what = "points_from_gram(G) for a G whose entries G[2, 0] and G[0, 2] differ by 0.5 s"
    got = _points(sp, nearly, what)
    _check_shape(got, 4, 4, what, nearly)
    _check_gram(got, G, what, nearly, atol=4 * s)
    far = G.copy()
    far[2, 0] += 2 * s
    _expect_error(ValueError, lambda: sp.points_from_gram(far),
                  "points_from_gram(G) for a G whose entries G[2, 0] and G[0, 2] differ by 2 s",
                  "|G[i, j] - G[j, i]| > s: G is not symmetric")


def test_points_from_gram_accepts_a_slightly_asymmetric_matrix_with_tiny_negative_eigenvalues(sp):
    """A Gram matrix computed in floats, plus noise of order 1e-13 (not symmetric): it is accepted, and X Xᵀ is G up
    to the noise."""
    rng = np.random.default_rng(6526)
    P = rng.normal(size=(7, 3))
    G = P @ P.T
    noisy = G + rng.normal(size=G.shape) * 1e-13
    what = "points_from_gram(G + noise of order 1e-13) for G = P Pᵀ, P of shape (7, 3)"
    got = _points(sp, noisy, what)
    _check_shape(got, 7, 3, what, noisy)
    _check_gram(got, G, what, noisy, atol=1e-9)


def test_points_from_gram_of_Q_G_Qt_for_a_permutation_Q_are_the_points_permuted(sp):
    """Renumbering the points (Q G Qᵀ, Q a permutation matrix) renumbers the rows of X: same Gram matrix permuted, same
    distances permuted, same coordinates up to the sign of each column (distinct eigenvalues)."""
    rng = np.random.default_rng(6527)
    for n in (5, 8):
        G, lam = _distinct_gram(rng, n)
        order = rng.permutation(n)
        Q = np.eye(n)[order]
        X = _points(sp, G, f"points_from_gram(G) for a {n} × {n} Gram matrix")
        permuted = Q @ G @ Q.T
        what = f"points_from_gram(Q G Qᵀ) for the permutation {order.tolist()}"
        got = _points(sp, permuted, what)
        _check_shape(got, n, n, what, permuted)
        _check_gram(got, permuted, what, permuted)
        _close(distance.pdist(got), distance.pdist(Q @ X), f"the distances of {what} (those of G, permuted)",
               rtol=1e-9, atol=1e-9, hint=_points_hint(got, permuted))
        _close(np.abs(got), np.abs(Q @ X), f"|X| for {what} (the rows of X permuted, up to the sign of each column)",
               rtol=1e-8, atol=1e-9, hint=_points_hint(got, permuted))
        _check_signs(got, what, permuted)


@pytest.mark.parametrize("c", [0.0625, 7.29, 1600.0], ids=["c-1/16", "c-7.29", "c-1600"])
def test_points_from_gram_of_c_G_is_sqrt_c_X(sp, c):
    """Homogeneity: the points of c G (c > 0) are √c times those of G, sign convention included (distinct eigenvalues)."""
    rng = np.random.default_rng(6516)
    G, _ = _distinct_gram(rng, 5, rank=4)
    X = _points(sp, G, "points_from_gram(G) for a 5 × 5 Gram matrix of rank 4")
    what = f"points_from_gram({c} G) for a 5 × 5 Gram matrix of rank 4"
    got = _points(sp, c * G, what)
    _check_shape(got, 5, 4, what, c * G)
    _close(got, math.sqrt(c) * np.asarray(X, dtype=float), what + f" (√{c} times the points of G)", rtol=1e-8,
           atol=1e-8 * math.sqrt(c), hint=_points_hint(got, c * G))


def test_points_from_gram_of_centered_points_are_the_scores_of_a_pca(sp):
    """Centered points P (mean 0): the columns of X are the principal scores U S of P (scipy.linalg.svd), up to their
    signs; the first column is the direction of largest mean square, and every column sums to 0."""
    rng = np.random.default_rng(6517)
    P = rng.normal(size=(30, 3)) * [4.0, 1.5, 0.5] @ _random_orthogonal(rng, 3)
    P -= P.mean(axis=0)
    G = P @ P.T
    U, S, _ = linalg.svd(P, full_matrices=False)
    what = "points_from_gram(P Pᵀ) for 30 centered points P in dimension 3"
    got = _points(sp, G, what)
    _check_shape(got, 30, 3, what, G)
    _close(np.abs(got), np.abs(U * S), f"|X| for {what} (the scores U S of a PCA, up to their signs)", rtol=1e-7,
           atol=1e-8, hint=_points_hint(got, G))
    _close(got.sum(axis=0), np.zeros(3), f"the sums of the columns of X for {what} (centered points)", rtol=0,
           atol=1e-8, hint=_points_hint(got, G))


def test_points_from_gram_after_double_centering_of_squared_distances_gives_the_distances_back(sp):
    """Classical scaling: from the distances D of points of the plane, G = -½ J D⁽²⁾ J (J = I - 11ᵀ/n, the SQUARED
    distances) is a Gram matrix of rank 2, and the points of G have the distances D."""
    rng = np.random.default_rng(6518)
    for n, scale in ((4, 1.0), (10, 50.0), (25, 3.0)):
        P = rng.normal(size=(n, 2)) * scale
        D = distance.squareform(distance.pdist(P))
        J = np.eye(n) - np.ones((n, n)) / n
        G = -0.5 * J @ (D ** 2) @ J
        what = f"points_from_gram(-½ J D⁽²⁾ J) for the distances of {n} points of the plane"
        got = _points(sp, G, what, expected=f"an X of shape {(n, 2)}")
        _check_shape(got, n, 2, what, G)
        _check_distances(got, P, what, G)


def test_points_from_gram_accepts_integers_and_numpy_integers(sp):
    """G as a list of Python integers or an int64 array; dim as a NumPy integer: an array of floats."""
    P = np.array([[3, -1], [2, 3], [-1, 4]])
    G = P @ P.T
    for given, text in ((G.tolist(), "a list of integers"), (G.astype(np.int64), "an int64 array")):
        what = f"points_from_gram(G) for G = {G.tolist()} given as {text}"
        got = _points(sp, given, what)
        _check_shape(got, 3, 2, what, G)
        _check_gram(got, G, what, G)
        _check_distances(got, P, what, G)
    for dim in (np.int64(2), np.int32(3), 1):
        what = f"points_from_gram(G, dim={dim!r}) for G = {G.tolist()}"
        got = _points(sp, G, what, dim=dim)
        _check_shape(got, 3, int(dim), what, G, int(dim))


def test_points_from_gram_does_not_modify_its_input(sp_module):
    """G is never written to, even when it is only nearly symmetric (G += G.T writes into G)."""
    G = _from_spectrum([3.5, 1.25, 0.75, 0.0])
    G[3, 1] += 0.4 * _threshold(G)
    copy = G.copy()
    _result(lambda: sp_module.points_from_gram(G), "an X", "a nearly symmetric float array")
    assert np.array_equal(G, copy), (f"expected G unchanged by points_from_gram, got G = {_show(G)} (never modify the "
                                     f"arrays you receive: G += G.T or G /= 2 writes into G)")


GRAM_REFUSALS = [
    ([1.0, 2.0, 3.0], {}, "G is 1-D"),
    (4.0, {}, "G is a number, not 2-D"),
    (np.zeros((2, 2, 2)), {}, "G is 3-D"),
    (np.zeros((2, 3)), {}, "G is not square (2 × 3)"),
    (np.zeros((0, 0)), {}, "G is empty (0 × 0)"),
    ([], {}, "G is an empty list"),
    ([[]], {}, "G is [[]], a row without entries"),
    ([[1.0, 0.5], [0.5]], {}, "G is a ragged list"),
    ([[2.0, "a"], ["a", 2.0]], {}, "G holds a string that is not a number"),
    (None, {}, "G is None"),
    ([[2.0, 0.4], [1.3, 3.0]], {}, "G is not symmetric"),
    ([[2.0, np.nan], [np.nan, 3.0]], {}, "G holds nan (|nan - nan| ≤ s does not hold: not symmetric)"),
    ([[np.inf, 0.0], [0.0, 1.0]], {}, "G holds an inf (|inf - inf| ≤ s does not hold: not symmetric)"),
    ([[1.0, 0.0], [0.0, -np.inf]], {}, "G holds a -inf"),
    ([[1.0, 4.0], [4.0, 3.0]], {}, "G has a negative eigenvalue (determinant -13): not positive semi-definite"),
    ([[-0.36]], {}, "G = [[-0.36]]: a negative squared length"),
    ([[2.0, 0.0, 0.0], [0.0, -1e-3, 0.0], [0.0, 0.0, 1.0]], {}, "G has the eigenvalue -1e-3, far below -s"),
]
GRAM_IDS = ["one-d", "scalar", "three-d", "not-square", "empty", "empty-list", "empty-row", "ragged", "string", "none",
            "not-symmetric", "nan", "inf", "minus-inf", "negative-eigenvalue", "negative-entry", "diagonal-negative"]
DIM_REFUSALS = [(0, "dim = 0"), (-1, "dim = -1"), (4, "dim = 4 > n = 3"), (2.0, "dim = 2.0, a float"),
                (1.5, "dim = 1.5"), (True, "dim = True, a bool"), (False, "dim = False, a bool"),
                (np.True_, "dim = np.True_, a NumPy bool"), ("2", "dim = '2', a string")]
GRAM_REFUSALS += [(np.diag([3.2, 1.1, 0.45]), {"dim": dim}, why) for dim, why in DIM_REFUSALS]
GRAM_IDS += ["dim-zero", "dim-negative", "dim-above-n", "dim-float", "dim-half", "dim-true", "dim-false",
             "dim-numpy-bool", "dim-string"]
GRAM_REFUSALS += [(np.diag([3.2, 1.1, 0.45]), {"tol": -1e-9}, "tol = -1e-9 < 0"),
                  (np.diag([3.2, 1.1, 0.45]), {"tol": -0.5}, "tol = -0.5 < 0")]
GRAM_IDS += ["tol-tiny-negative", "tol-negative"]


@pytest.mark.parametrize("G, kwargs, why", GRAM_REFUSALS, ids=GRAM_IDS)
def test_points_from_gram_refusals(sp, G, kwargs, why):
    args = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
    _expect_error(ValueError, lambda: sp.points_from_gram(G, **kwargs),
                  f"points_from_gram({G!r}{', ' + args if args else ''})", why)


# --- temper ---------------------------------------------------------------------------------------------------------

TEMPER_HINT = ("q_i = p_i^(1/T) / Σ_j p_j^(1/T), through the logarithms of the POSITIVE p_i only: (ln p_i - ln p_max) / "
               "T, then exp, then divide by the sum; q_i = 0 where p_i = 0 (np.log(0) warns); T = 0: the uniform law on "
               "the most probable outcomes; T = inf: the uniform law on the outcomes of positive probability")


def _temper_oracle(p, T):
    """scipy.special.softmax of ln p_i / T on the positive p_i (0 elsewhere); the limits T → 0 (uniform on the largest
    p_i) and T → ∞ (uniform on the positive p_i) written here."""
    p = np.asarray(p, dtype=float)
    q = np.zeros_like(p)
    positive = p > 0
    if T == 0:
        top = p == p.max()
        q[top] = 1.0 / np.count_nonzero(top)
    elif math.isinf(T):
        q[positive] = 1.0 / np.count_nonzero(positive)
    else:
        q[positive] = special.softmax(np.log(p[positive]) / T)
    return q


def _temper_hint(got, p, T):
    """TEMPER_HINT, plus the classic error that the result got matches, if any."""
    p = np.asarray(p, dtype=float)
    want = _temper_oracle(p, T)
    K = p.size
    candidates = []
    with np.errstate(all="ignore"):
        if 0 < T < math.inf:
            power = p ** (1.0 / T)
            candidates += [
                (p ** T / np.sum(p ** T), "the power is 1/T, not T: q_i is proportional to p_i^(1/T)"),
                (power, "the powers p_i^(1/T) must be divided by their sum (renormalized)"),
                (power / power.max(), "divide the powers by their SUM, not by the largest one"),
                (special.softmax(p / T), "p holds probabilities, not scores (logits): the softmax of p / T is another "
                                         "law; q_i is proportional to exp(ln p_i / T) = p_i^(1/T)"),
            ]
        if math.isinf(T):
            candidates.append((np.full(K, 1.0 / K), "at T = inf an outcome of probability 0 keeps probability 0 "
                                                    "(0^(1/T) is not 0^0 = 1): the uniform law on the outcomes of "
                                                    "POSITIVE probability"))
        if T == 0:
            first = np.zeros(K)
            first[int(np.argmax(p))] = 1.0
            candidates.append((first, "at T = 0 the probability is shared EQUALLY between the most probable outcomes "
                                      "(ties), not given to the first one"))
    text = _first_match(got, want, candidates, rtol=1e-7, atol=1e-12)
    if not text:
        try:
            if np.any(np.isnan(np.asarray(got, dtype=float))):
                text = ("the result holds nan: p_i^(1/T) underflowed to 0 for every i (0 / 0); subtract ln p_max from "
                        "the logarithms before dividing by T, so that the largest term is exp(0) = 1")
        except (TypeError, ValueError):
            pass
    return f"{TEMPER_HINT}; here {text}" if text else TEMPER_HINT


def _temper_warning(text):
    if "log" in text:
        return ("np.log(0) warns: take the logarithms of the POSITIVE p_i only, and leave q_i = 0 where p_i = 0")
    if "invalid" in text or "divide" in text:
        return ("0 / 0: p_i^(1/T) underflowed to 0 for every i; subtract ln p_max from the logarithms before dividing "
                "by T, so that the largest term is exp(0) = 1")
    if "overflow" in text:
        return "an overflow: subtract ln p_max from the logarithms before dividing by T, so that every term is ≤ 0"
    return ""


def _tempered(sp, p, T, what):
    got = _result(lambda: sp.temper(p, T), "a law (numpy.ndarray of floats)", what, TEMPER_HINT, _temper_warning)
    K = np.asarray(p).size
    _float_matrix(got, (K,), what, _temper_hint(got, p, T))
    return got


def _check_tempered(got, p, T, what, rtol=1e-9, atol=1e-14):
    want = _temper_oracle(p, T)
    _close(got, want, what, rtol=rtol, atol=atol, hint=_temper_hint(got, p, T))


def _random_law(rng, K, n_zeros=0, alpha=1.0, decimals=None):
    """A law on K outcomes (Dirichlet), with n_zeros outcomes of probability 0; rounded first to make ties if asked."""
    p = rng.dirichlet(np.full(K, alpha))
    if decimals is not None:
        p = np.round(p, decimals)
    if n_zeros:
        p[rng.choice(K, size=n_zeros, replace=False)] = 0.0
    if not np.any(p > 0):
        p[int(rng.integers(K))] = 1.0
    return p / p.sum()


def test_temper_docstring_examples(sp):
    call = "temper([0.5, 0.25, 0.25, 0.0], 1 / 3) (cubes, renormalized; the zero stays)"
    got = _tempered(sp, [0.5, 0.25, 0.25, 0.0], 1 / 3, call)
    _close(got, [0.8, 0.1, 0.1, 0.0], call, rtol=1e-12, atol=1e-15, hint=_temper_hint(got, [0.5, 0.25, 0.25, 0.0], 1 / 3))
    call = "temper([0.5, 0.25, 0.25, 0.0], 3) (cube roots, renormalized)"
    got = _tempered(sp, [0.5, 0.25, 0.25, 0.0], 3, call)
    _close(np.round(got, 4), [0.3865, 0.3068, 0.3068, 0.0], call, rtol=0, atol=1e-12,
           hint=_temper_hint(got, [0.5, 0.25, 0.25, 0.0], 3))
    for p, T, want in (([0.4, 0.4, 0.2], 0, [0.5, 0.5, 0.0]), ([0.7, 0.3, 0.0], np.inf, [0.5, 0.5, 0.0])):
        call = f"temper({p}, {T})"
        got = _tempered(sp, p, T, call)
        _close(got, want, call, rtol=0, atol=1e-15, hint=_temper_hint(got, p, T))


TEMPER_CASES = [(1, 0.25, 0), (2, 0.85, 0), (3, 4.0, 1), (5, 0.1, 0), (5, 9.0, 2), (8, 0.45, 3), (12, 1.75, 0),
                (12, 0.05, 4), (30, 2.5, 6), (50, 40.0, 10), (50, 0.25, 0), (200, 0.85, 50)]


@pytest.mark.parametrize("K, T, zeros", TEMPER_CASES, ids=[f"K{K}-T{T}-zeros{z}" for K, T, z in TEMPER_CASES])
def test_temper_matches_the_softmax_of_log_p_over_T(sp, K, T, zeros):
    """Random laws, some with outcomes of probability 0: scipy.special.softmax of ln p_i / T on the positive p_i, 0
    elsewhere (the Boltzmann law of the energies -ln p_i)."""
    rng = np.random.default_rng(6530 + TEMPER_CASES.index((K, T, zeros)))
    p = _random_law(rng, K, zeros, alpha=float(rng.uniform(0.4, 3)))
    what = f"temper(p, {T}) for a random law p on {K} outcomes ({zeros} of probability 0)"
    got = _tempered(sp, p, T, what)
    _check_tempered(got, p, T, what)


def test_temper_with_T_equal_to_1_gives_p_back(sp):
    rng = np.random.default_rng(6542)
    for K, zeros in ((1, 0), (4, 1), (9, 0), (25, 5), (120, 30)):
        p = _random_law(rng, K, zeros)
        what = f"temper(p, 1) for a random law p on {K} outcomes ({zeros} of probability 0)"
        got = _tempered(sp, p, 1, what)
        _close(got, p, what + " (p itself)", rtol=1e-12, atol=1e-16, hint=_temper_hint(got, p, 1))


TEMPERATURES = [0, 1e-6, 0.05, 0.25, 0.45, 0.85, 1, 1.75, 4, 9, 40, 1e6, np.inf]


def test_temper_keeps_outcomes_of_probability_0_at_0(sp):
    """An outcome of probability 0 keeps probability exactly 0, at every temperature, T = 0 and T = inf included."""
    rng = np.random.default_rng(6543)
    for k in range(6):
        p = _random_law(rng, 9, n_zeros=int(rng.integers(1, 6)))
        for T in TEMPERATURES:
            what = f"temper(p, {T}) for p = {_show(p)}"
            got = _tempered(sp, p, T, what)
            assert np.all(got[p == 0] == 0), (
                f"expected 0 at the outcomes of probability 0 ({np.flatnonzero(p == 0).tolist()}) for {what}, got "
                f"{_show(got)} ({_temper_hint(got, p, T)})")


def test_temper_keeps_the_order_of_the_outcomes(sp):
    """p_i > p_j gives q_i ≥ q_j (q_i > q_j for a moderate T), and p_i = p_j gives q_i = q_j: the order never changes."""
    rng = np.random.default_rng(6544)
    for k in range(5):
        p = _random_law(rng, 10, n_zeros=int(k), decimals=1 if k % 2 else 2)
        i, j = np.meshgrid(np.arange(10), np.arange(10), indexing="ij")
        for T in TEMPERATURES:
            what = f"temper(p, {T}) for p = {_show(p)}"
            got = _tempered(sp, p, T, what)
            above = (p[i] > p[j]) & (got[i] < got[j])
            assert not above.any(), (
                f"expected the order of p kept for {what}, got q = {_show(got)}: p[{i[above][0]}] > p[{j[above][0]}] but "
                f"q[{i[above][0]}] < q[{j[above][0]}] ({_temper_hint(got, p, T)})")
            ties = (p[i] == p[j]) & ~np.isclose(got[i], got[j], rtol=1e-13, atol=0)
            assert not ties.any(), (f"expected equal probabilities for equal p_i for {what}, got q = {_show(got)} "
                                    f"({_temper_hint(got, p, T)})")
            if 0.2 <= T <= 10:
                strict = (p[i] > p[j]) & ~(got[i] > got[j])
                assert not strict.any(), (f"expected q_i > q_j whenever p_i > p_j for {what}, got q = {_show(got)} "
                                          f"({_temper_hint(got, p, T)})")


def test_temper_entropy_grows_with_T(sp):
    """Constat (the proof is for CP6): the entropy of the tempered law (scipy.stats.entropy) never decreases with T, from
    ln(number of most probable outcomes) at T = 0 to ln(number of outcomes of positive probability) at T = inf."""
    rng = np.random.default_rng(6545)
    for k in range(5):
        p = _random_law(rng, 8, n_zeros=k % 3, decimals=2 if k == 4 else None)
        entropies = []
        for T in TEMPERATURES:
            got = _tempered(sp, p, T, f"temper(p, {T}) for p = {_show(p)}")
            entropies.append(float(stats.entropy(got)))
        assert all(b >= a - 1e-12 for a, b in zip(entropies, entropies[1:])), (
            f"expected an entropy that never decreases with T for p = {_show(p)}, got {_show(entropies)} for T = "
            f"{TEMPERATURES} ({TEMPER_HINT})")
        ends = [math.log(np.count_nonzero(p == p.max())), math.log(np.count_nonzero(p > 0))]
        _close([entropies[0], entropies[-1]], ends, f"the entropies at T = 0 and T = inf for p = {_show(p)}",
               rtol=1e-12, atol=1e-12, hint=TEMPER_HINT)


T0_CASES = [([0.27, 0.06, 0.0, 0.21, 0.46], [0, 0, 0, 0, 1.0], "a single most probable outcome"),
            ([0.0, 0.37, 0.26, 0.37], [0, 0.5, 0, 0.5], "two most probable outcomes"),
            ([0.09, 0.29, 0.04, 0.29, 0.29], [0, 1 / 3, 0, 1 / 3, 1 / 3], "three most probable outcomes"),
            ([1.0], [1.0], "a single outcome"), ([0.0, 0.0, 1.0, 0.0], [0, 0, 1.0, 0], "a certain outcome"),
            ([0.125] * 8, [0.125] * 8, "a uniform law")]


@pytest.mark.parametrize("p, want, text", T0_CASES, ids=["one-top", "two-tops", "three-tops", "one-outcome", "certain",
                                                          "uniform"])
def test_temper_at_T_0_is_uniform_on_the_most_probable_outcomes(sp, p, want, text):
    what = f"temper({p}, 0) ({text})"
    got = _tempered(sp, p, 0, what)
    _close(got, want, what, rtol=1e-15, atol=0, hint=_temper_hint(got, p, 0))


TINF_CASES = [([0.27, 0.06, 0.0, 0.21, 0.46], [0.25, 0.25, 0, 0.25, 0.25], "one outcome of probability 0"),
              ([0.18, 0.82], [0.5, 0.5], "two outcomes"), ([0.0, 0.0, 1.0], [0, 0, 1.0], "a certain outcome"),
              ([0.0, 0.31, 0.0, 0.69, 0.0], [0, 0.5, 0, 0.5, 0], "three outcomes of probability 0")]


@pytest.mark.parametrize("p, want, text", TINF_CASES, ids=["one-zero", "two-outcomes", "certain", "three-zeros"])
def test_temper_at_T_inf_is_uniform_on_the_outcomes_of_positive_probability(sp, p, want, text):
    what = f"temper({p}, np.inf) ({text})"
    got = _tempered(sp, p, np.inf, what)
    _close(got, want, what, rtol=1e-15, atol=0, hint=_temper_hint(got, p, np.inf))


def test_temper_tends_to_its_limits_at_small_and_large_T(sp):
    """A small T (1e-4) is close to the law at T = 0 (here the most probable outcomes are ahead by a factor ≥ 1.05, or
    exactly tied), a large T (1e7) close to the law at T = inf."""
    rng = np.random.default_rng(6546)
    for k in range(6):
        p = _random_law(rng, 7, n_zeros=k % 3, decimals=2)
        positive = np.sort(p[p > 0])[::-1]
        others = positive[positive < positive[0]]
        if others.size and positive[0] / others[0] < 1.05:
            continue
        for T, limit, tol in ((1e-4, 0, 1e-12), (1e7, np.inf, 1e-5)):
            what = f"temper(p, {T}) for p = {_show(p)}"
            got = _tempered(sp, p, T, what)
            _close(got, _temper_oracle(p, limit), what + f" (close to the law at T = {limit})", rtol=0, atol=tol,
                   hint=_temper_hint(got, p, T))


SMALL_T_CASES = [([0.33, 0.26, 0.23, 0.18], 1e-3), ([0.33, 0.26, 0.23, 0.18], 1e-6),
                 ([0.24, 0.38, 0.0, 0.38], 1e-3), ([0.24, 0.38, 0.0, 0.38], 1e-6),
                 ([0.18, 0.17, 0.16, 0.17, 0.16, 0.16], 1e-3), ([0.18, 0.17, 0.16, 0.17, 0.16, 0.16], 1e-6)]


@pytest.mark.parametrize("p, T", SMALL_T_CASES, ids=[f"{len(p)}-outcomes-T{T}" for p, T in SMALL_T_CASES])
def test_temper_does_not_underflow_for_a_small_T(sp, p, T):
    """p_max^(1/T) underflows to 0 here (0.38¹⁰⁰⁰ < 1e-300), so the powers taken directly give 0 / 0: the logarithms
    minus ln p_max avoid it, without a RuntimeWarning."""
    what = f"temper({p}, {T})"
    got = _tempered(sp, p, T, what)
    _check_tempered(got, p, T, what, rtol=1e-6, atol=1e-12)


def test_temper_with_tiny_probabilities(sp):
    """Probabilities as small as 1e-300 have finite logarithms: they are tempered like the others."""
    p = np.array([1e-300, 0.3, 2e-200, 0.7 - 1e-300 - 2e-200, 0.0])
    for T in (0.05, 0.85, 40.0):
        what = f"temper(p, {T}) for p = {_show(p)} (entries 1e-300 and 2e-200)"
        got = _tempered(sp, p, T, what)
        _check_tempered(got, p, T, what, rtol=1e-9, atol=1e-300)


@pytest.mark.parametrize("T", [0.25, 0.85, 4.0, 9.0], ids=["T0.25", "T0.85", "T4", "T9"])
def test_temper_of_a_softmax_is_the_softmax_of_the_scores_over_T(sp, T):
    """Scores z (of a classifier), p = softmax(z) (scipy.special.softmax): temper(p, T) = softmax(z / T)."""
    rng = np.random.default_rng(6547)
    z = rng.normal(size=11) * 2.2
    p = special.softmax(z)
    what = f"temper(softmax(z), {T}) for scores z = {_show(z)}"
    got = _tempered(sp, p, T, what)
    _close(got, special.softmax(z / T), what + f" (softmax(z / {T}))", rtol=1e-9, atol=1e-15,
           hint=_temper_hint(got, p, T))


def test_temper_sharpens_below_1_and_flattens_above_1(sp):
    """For a law that is not uniform on its outcomes of positive probability: the most probable outcome gains for T < 1
    and loses for T > 1; the ratios become q_i / q_j = (p_i / p_j)^(1/T)."""
    rng = np.random.default_rng(6548)
    for k in range(4):
        p = _random_law(rng, 6, n_zeros=k % 2)
        top = int(np.argmax(p))
        for T in (0.25, 0.85, 1.75, 9.0):
            what = f"temper(p, {T}) for p = {_show(p)}"
            got = _tempered(sp, p, T, what)
            better = got[top] > p[top] if T < 1 else got[top] < p[top]
            assert better, (f"expected the most probable outcome to {'gain' if T < 1 else 'lose'} probability for "
                            f"{what}, got q = {_show(got)} ({_temper_hint(got, p, T)})")
            i, j = np.flatnonzero(p > 0)[:2]
            _close(got[i] / got[j], (p[i] / p[j]) ** (1 / T), f"q[{i}] / q[{j}] for {what}", rtol=1e-9,
                   hint=_temper_hint(got, p, T))


def test_temper_accepts_a_law_that_sums_to_1_up_to_1e_9(sp):
    """A law whose sum is 1 + 6e-10 or 1 - 6e-10 is accepted; the tempered law sums to 1."""
    for p in ([0.44, 0.13, 0.43 + 6e-10], [0.44, 0.13, 0.43 - 6e-10]):
        for T in (0.25, 1.75):
            what = f"temper({p}, {T}) (a sum within 1e-9 of 1)"
            got = _tempered(sp, p, T, what)
            assert abs(float(np.sum(got)) - 1.0) <= 1e-12, (f"expected a law summing to 1 for {what}, got "
                                                             f"{_show(got)} of sum {float(np.sum(got))!r} "
                                                             f"({_temper_hint(got, p, T)})")
            _check_tempered(got, p, T, what, rtol=1e-9, atol=1e-14)


def test_temper_accepts_lists_integers_and_numpy_numbers(sp):
    """p as a list, an int64 array or a float32 array; T as a Python int, a NumPy integer or a NumPy float: an array of
    floats."""
    for p, T, text in (([0.0, 1, 0], 4, "a list with integers and T an int"),
                       (np.array([0, 0, 1], dtype=np.int64), np.int64(4), "an int64 array and T an int64"),
                       (np.array([0.3125, 0.6875], dtype=np.float32), np.float32(0.25), "float32 arrays"),
                       ([0.21, 0.79], np.float64(1.75), "T a np.float64")):
        what = f"temper({p!r}, {T!r}) ({text})"
        got = _tempered(sp, p, T, what)
        _check_tempered(got, np.asarray(p, dtype=float), float(T), what, rtol=1e-6, atol=1e-12)


def test_temper_does_not_modify_its_input(sp_module):
    p = np.array([0.0, 0.26, 0.41, 0.33])
    copy = p.copy()
    for T in (0, 0.25, 1.75, np.inf):
        _result(lambda: sp_module.temper(p, T), "a law", f"temper(p, {T})")
        assert np.array_equal(p, copy), (f"expected p unchanged by temper(p, {T}), got p = {_show(p)} (never modify the "
                                         f"arrays you receive: p **= 1 / T or p /= p.sum() writes into p)")


LAW_REFUSALS = [
    ([[0.42, 0.58]], "p is 2-D"), (1.0, "p is a number, not 1-D"), ([], "p is empty"), (np.zeros(0), "p is empty"),
    ([0.62, 0.47, -0.09], "p has a negative entry"), ([0.31, 0.33], "p sums to 0.64"),
    ([0.71, 0.36], "p sums to 1.07"), ([0.71, 0.29 + 2e-9], "p sums to 1 + 2e-9"),
    ([0.71, 0.29 - 2e-9], "p sums to 1 - 2e-9"), ([0.0, 0.0, 0.0], "p is all zeros"),
    ([np.nan, 1.0], "p holds nan"), ([0.4, np.nan, 0.6], "p holds nan (the others sum to 1)"),
    ([np.inf, 0.0], "p holds an inf"), ([0.5, np.inf, -np.inf], "p holds inf and -inf"),
    (["a", "b"], "p holds strings that are not numbers"), (None, "p is None"),
]
LAW_IDS = ["two-d", "scalar", "empty-list", "empty-array", "negative", "sum-below", "sum-above", "sum-just-above",
           "sum-just-below", "all-zeros", "nan", "nan-inside", "inf", "inf-and-minus-inf", "strings", "none"]


@pytest.mark.parametrize("p, why", LAW_REFUSALS, ids=LAW_IDS)
def test_temper_refuses_a_bad_law(sp, p, why):
    _expect_error(ValueError, lambda: sp.temper(p, 1.75), f"temper({p!r}, 1.75)", why)


T_REFUSALS = [(-0.25, "T is negative"), (-1e-12, "T is a little below 0"), (-np.inf, "T is -inf"),
              (np.nan, "T is nan"), (np.float64("nan"), "T is np.float64(nan)"), (True, "T is True, a bool"),
              (False, "T is False, a bool"), (np.True_, "T is np.True_, a NumPy bool")]


@pytest.mark.parametrize("T, why", T_REFUSALS, ids=["negative", "just-below-zero", "minus-inf", "nan", "numpy-nan",
                                                    "true", "false", "numpy-bool"])
def test_temper_refuses_a_bad_temperature(sp, T, why):
    _expect_error(ValueError, lambda: sp.temper([0.13, 0.54, 0.33], T), f"temper([0.13, 0.54, 0.33], {T!r})", why)


# --- smallest_mass_set ----------------------------------------------------------------------------------------------

MASS_HINT = ("the outcomes by decreasing probability (a stable sort, np.argsort(-p, kind='stable'), keeps the smaller "
             "index first between equal probabilities), their cumulative probabilities, and the first position where "
             "the cumulative probability reaches mass - 1e-9: keep the outcomes up to it, that one included")


def _stable_order(p):
    return np.argsort(-np.asarray(p, dtype=float), kind="stable")


def _smallest_size(p, mass):
    """The smallest number of outcomes whose total probability is at least mass - 1e-9, by an exhaustive search over the
    subsets (math.fsum of each)."""
    p = [float(v) for v in np.asarray(p, dtype=float)]
    for k in range(1, len(p) + 1):
        if any(math.fsum(c) >= mass - 1e-9 for c in itertools.combinations(p, k)):
            return k
    return None


def _expected_set(p, mass):
    """The first outcomes of the stable order, as many as the exhaustive search says."""
    return _stable_order(p)[:_smallest_size(p, mass)]


def _mass_rule(p, mass, order="stable", tol=1e-9, strict=False, keep_crossing=True, renormalize=False):
    """The set given by a rule (the contract, or a classic error)."""
    p = np.asarray(p, dtype=float)
    if renormalize:
        p = p / p.sum()
    idx = {"stable": lambda: np.argsort(-p, kind="stable"), "ascending": lambda: np.argsort(p, kind="stable"),
           "larger-first": lambda: np.argsort(p, kind="stable")[::-1]}[order]()
    cumulative = np.cumsum(p[idx])
    reached = np.flatnonzero(cumulative > mass - tol if strict else cumulative >= mass - tol)
    if not reached.size:
        return idx
    return idx[:reached[0] + (1 if keep_crossing else 0)]


def _mass_hint(got, p, mass, want=None):
    """MASS_HINT, plus the classic error that the result got matches, if any."""
    p = np.asarray(p, dtype=float)
    want = _expected_set(p, mass) if want is None else np.asarray(want)
    try:
        g = np.asarray(got)
        if g.ndim == 1 and g.dtype.kind in "iu" and g.size and np.any(p[np.clip(g, 0, p.size - 1)] == 0):
            return (f"{MASS_HINT}; here the set holds an outcome of probability 0: if the cumulative probability never "
                    f"reaches mass - 1e-9 (rounding), the set is every outcome of POSITIVE probability")
    except (TypeError, ValueError, IndexError):
        pass
    try:
        if np.asarray(got).size == 0:
            return (f"{MASS_HINT}; here an empty set: mass > 0, so the set holds at least one outcome (and if the "
                    f"cumulative probability never reaches mass - 1e-9, by rounding, it is every outcome of positive "
                    f"probability)")
    except (TypeError, ValueError):
        pass
    candidates = [
        (_mass_rule(p, mass, keep_crossing=False), "one outcome is missing: the outcome that makes the cumulative "
                                                   "probability cross mass is kept"),
        (_mass_rule(p, mass, order="ascending"), "the outcomes are taken by DECREASING probability (np.argsort(-p, …)), "
                                                 "not by increasing probability"),
        (_mass_rule(p, mass, order="larger-first"), "between equal probabilities the SMALLER index comes first: a "
                                                    "stable sort np.argsort(-p, kind='stable') (np.argsort(p)[::-1] "
                                                    "puts the larger index first)"),
        (_mass_rule(p, mass, tol=0), "a cumulative probability within 1e-9 of mass counts as reaching it (in floats a "
                                     "sum of probabilities can fall just below mass): compare with mass - 1e-9"),
        (_mass_rule(p, mass, tol=0, strict=True), "a cumulative probability EQUAL to mass reaches it (>=, not >), and "
                                                  "one within 1e-9 of mass too"),
        (_mass_rule(p, mass, renormalize=True), "the cumulative probabilities are those of p as given (it sums to 1 "
                                                "only up to 1e-9): do not divide p by its sum first"),
        (np.sort(want), "the indices come by decreasing probability, not by increasing index"),
    ]
    text = _first_match(got, want, candidates, rtol=0, atol=0)
    if not text:
        try:
            g = np.asarray(got)
            if (g.shape == want.shape and sorted(p[g].tolist()) == sorted(p[want].tolist())
                    and not np.array_equal(g, want)):
                text = ("the same probabilities, but other outcomes between equal probabilities: the smaller index "
                        "first, with a stable sort, np.argsort(-p, kind='stable') (the default sort of np.argsort is "
                        "not stable)")
        except (TypeError, ValueError, IndexError):
            pass
    return f"{MASS_HINT}; here {text}" if text else MASS_HINT


def _mass_set(sp, p, mass, what):
    got = _result(lambda: sp.smallest_mass_set(p, mass), "a numpy.ndarray of indices", what, MASS_HINT)
    hint = MASS_HINT
    if isinstance(got, np.ndarray) and got.dtype.kind == "b":
        hint += "; here a boolean mask was returned: return the indices themselves, by decreasing probability"
    elif isinstance(got, np.ndarray) and got.dtype.kind == "f":
        hint += "; here floats were returned: the indices of the outcomes (integers), not their probabilities"
    assert isinstance(got, np.ndarray) and got.ndim == 1 and got.dtype.kind in "iu", (
        f"expected {what} as a 1-D numpy.ndarray of integers, got {type(got).__name__} {_show_any(got)}"
        + (f" of dtype {got.dtype}" if isinstance(got, np.ndarray) else "") + f" ({hint})")
    return got


def _check_set(got, want, p, mass, what):
    want = np.asarray(want)
    assert got.shape == want.shape and np.array_equal(got, want), (
        f"expected {what} = array({want.tolist()}), got array({got.tolist()}) ({_mass_hint(got, p, mass, want)})")


def test_smallest_mass_set_docstring_examples(sp):
    for p, mass, want, text in (([0.1, 0.42, 0.08, 0.4], 0.5, [1, 3], " (0.42 < 0.5, then 0.42 + 0.4 = 0.82)"),
                                ([0.02, 0.93, 0.05], 0.6, [1], " (a confident law: a single outcome)")):
        call = f"smallest_mass_set({p}, {mass}){text}"
        got = _mass_set(sp, p, mass, call)
        _check_set(got, want, p, mass, call)


def test_smallest_mass_set_is_a_smallest_set_found_by_exhaustive_search(sp):
    """Random laws on K ≤ 9 outcomes (some with ties and zeros), random masses: the set has the smallest size of a set
    of total probability ≥ mass - 1e-9 (every subset tried), and it is made of the most probable outcomes, in the
    order of a stable sort by decreasing probability."""
    rng = np.random.default_rng(6560)
    for k in range(70):
        K = int(rng.integers(1, 10))
        p = _random_law(rng, K, n_zeros=int(rng.integers(0, K)) if k % 3 == 0 else 0,
                        decimals=1 if k % 4 == 1 else None, alpha=float(rng.uniform(0.3, 2)))
        for mass in (float(rng.uniform(0.02, 1.0)), float(rng.choice([0.33, 0.66, 0.97, 1.0]))):
            what = f"smallest_mass_set(p, {mass:.6g}) for p = {_show(p)}"
            got = _mass_set(sp, p, mass, what)
            want = _expected_set(p, mass)
            assert got.size == want.size, (
                f"expected a set of {want.size} outcome(s) for {what} (no smaller set reaches mass; the exhaustive "
                f"search finds one of that size), got {got.size}: array({got.tolist()}) ({_mass_hint(got, p, mass)})")
            total = math.fsum(p[got]) if np.all((got >= 0) & (got < K)) else -1.0
            assert total >= mass - 1e-9, (f"expected a set of total probability at least mass - 1e-9 for {what}, got "
                                          f"array({got.tolist()}) of total {total!r} ({_mass_hint(got, p, mass)})")
            _check_set(got, want, p, mass, what)


def test_smallest_mass_set_takes_the_outcomes_by_decreasing_probability(sp):
    """The probabilities of the set never increase along it; between equal probabilities the indices increase."""
    rng = np.random.default_rng(6561)
    for k in range(25):
        p = _random_law(rng, 15, n_zeros=k % 4, decimals=1)
        mass = float(rng.uniform(0.3, 1.0))
        what = f"smallest_mass_set(p, {mass:.6g}) for p = {_show(p)}"
        got = _mass_set(sp, p, mass, what)
        assert np.all((got >= 0) & (got < p.size)), f"expected indices between 0 and {p.size - 1} for {what}, got " \
                                                    f"array({got.tolist()}) ({MASS_HINT})"
        probs = p[got]
        ok = all(a > b or (a == b and i < j) for (a, i), (b, j) in zip(zip(probs, got), zip(probs[1:], got[1:])))
        assert ok, (f"expected the outcomes by decreasing probability (equal probabilities by increasing index) for "
                    f"{what}, got array({got.tolist()}) of probabilities {_show(probs)} ({_mass_hint(got, p, mass)})")


TIE_CASES = [(0.45, [1, 3]), (0.55, [1, 3, 5]), (0.7, [1, 3, 5, 0]), (0.85, [1, 3, 5, 0, 4]), (1.0, [1, 3, 5, 0, 4, 2])]
TIE_LAW = [0.13, 0.27, 0.06, 0.27, 0.13, 0.14]


@pytest.mark.parametrize("mass, want", TIE_CASES, ids=[f"mass-{m}" for m, _ in TIE_CASES])
def test_smallest_mass_set_breaks_ties_by_the_smaller_index(sp, mass, want):
    """Outcomes 1 and 3 both have 0.27, outcomes 0 and 4 both 0.13: the smaller index comes first."""
    assert want == _expected_set(TIE_LAW, mass).tolist(), "oracle"
    what = f"smallest_mass_set({TIE_LAW}, {mass})"
    got = _mass_set(sp, TIE_LAW, mass, what)
    _check_set(got, want, TIE_LAW, mass, what)


@pytest.mark.parametrize("K", [40, 300, 2000], ids=["K40", "K300", "K2000"])
def test_smallest_mass_set_breaks_ties_on_large_laws_full_of_ties(sp, K):
    """Large laws with only five different probabilities: the order of a STABLE sort by decreasing probability (the
    default sort of np.argsort is not stable on large arrays)."""
    rng = np.random.default_rng({40: 6566, 300: 6567, 2000: 6568}[K])
    p = rng.integers(1, 6, size=K).astype(float)
    p /= p.sum()
    for mass in (0.2, 0.55, 0.85, 0.99):
        what = f"smallest_mass_set(p, {mass}) for a law on {K} outcomes with five different probabilities"
        got = _mass_set(sp, p, mass, what)
        k = int(np.flatnonzero(np.cumsum(p[_stable_order(p)]) >= mass - 1e-9)[0]) + 1
        _check_set(got, _stable_order(p)[:k], p, mass, what)


def test_smallest_mass_set_keeps_the_outcome_that_crosses_mass(sp):
    """The cumulative probability goes from below mass to above it with the last outcome kept: that outcome is in the
    set."""
    for p, mass, want in (([0.08, 0.23, 0.41, 0.28], 0.55, [2, 3]), ([0.08, 0.23, 0.41, 0.28], 0.4, [2]),
                          ([0.08, 0.23, 0.41, 0.28], 0.95, [2, 3, 1, 0]), ([0.19, 0.81], 0.82, [1, 0])):
        assert want == _expected_set(p, mass).tolist(), "oracle"
        what = f"smallest_mass_set({p}, {mass})"
        got = _mass_set(sp, p, mass, what)
        _check_set(got, want, p, mass, what)


def test_smallest_mass_set_a_cumulative_probability_equal_to_mass_reaches_it(sp):
    """Dyadic probabilities (exact in floats): 0.4375 + 0.40625 is exactly 0.84375, which reaches 0.84375 (>=, not >)."""
    p = [0.09375, 0.40625, 0.0625, 0.4375]
    for mass, want in ((0.4375, [3]), (0.84375, [3, 1]), (0.9375, [3, 1, 0]), (1.0, [3, 1, 0, 2])):
        assert float(np.cumsum(np.array(p)[_stable_order(p)])[len(want) - 1]) == mass, "oracle: an exact equality"
        what = f"smallest_mass_set({p}, {mass}) (the cumulative probability is exactly {mass})"
        got = _mass_set(sp, p, mass, what)
        _check_set(got, want, p, mass, what)


FLOAT_SUM_CASES = [([0.14, 0.36, 0.08, 0.29, 0.13], 0.79, [1, 3, 0], "0.36 + 0.29 + 0.14"),
                   ([0.05, 0.47, 0.07, 0.08, 0.05, 0.22, 0.06], 0.77, [1, 5, 3], "0.47 + 0.22 + 0.08")]


@pytest.mark.parametrize("p, mass, want, text", FLOAT_SUM_CASES, ids=["three-outcomes-of-five", "three-of-seven"])
def test_smallest_mass_set_counts_a_float_sum_just_below_mass(sp, p, mass, want, text):
    """In floats, the cumulative probability falls just below mass (by about 1e-16): within 1e-9, it reaches mass."""
    cumulative = np.cumsum(np.array(p)[_stable_order(p)])
    assert cumulative[len(want) - 1] < mass and want == _expected_set(p, mass).tolist(), "oracle: a sum below mass"
    what = f"smallest_mass_set({p}, {mass}) (in floats {text} = {cumulative[len(want) - 1]!r})"
    got = _mass_set(sp, p, mass, what)
    _check_set(got, want, p, mass, what)


@pytest.mark.parametrize("gap, want", [(0.5e-9, [0, 1]), (2e-9, [0, 1, 2])], ids=["half-tolerance", "twice-tolerance"])
def test_smallest_mass_set_tolerance_is_1e_9(sp, gap, want):
    """The two most probable outcomes reach 0.62 - gap: within 1e-9 of 0.62 they reach it, 2e-9 below they do not."""
    p = [0.33, 0.29 - gap, 0.21, 0.17 + gap]
    what = f"smallest_mass_set([0.33, 0.29 - {gap:g}, 0.21, 0.17 + {gap:g}], 0.62)"
    got = _mass_set(sp, p, 0.62, what)
    _check_set(got, want, p, 0.62, what)


def test_smallest_mass_set_with_mass_1_ignores_a_last_outcome_below_1e_9(sp):
    """mass = 1: the first two outcomes reach 1 - 4e-10, within 1e-9 of 1, so the third (4e-10) is not needed."""
    p = [0.58, 0.42 - 4e-10, 4e-10]
    what = "smallest_mass_set([0.58, 0.42 - 4e-10, 4e-10], 1.0)"
    got = _mass_set(sp, p, 1.0, what)
    _check_set(got, [0, 1], p, 1.0, what)


def test_smallest_mass_set_never_holds_an_outcome_of_probability_0(sp):
    """mass = 1 with outcomes of probability 0: the set is every outcome of positive probability, never one of
    probability 0, also when p sums to 1 - 0.9e-9."""
    rng = np.random.default_rng(6563)
    cases = [([0.0, 0.36, 0.0, 0.64 - 0.9e-9, 0.0], [3, 1], "p sums to 1 - 0.9e-9")]
    for k in range(10):
        p = _random_law(rng, 9, n_zeros=int(rng.integers(1, 7)))
        cases.append((p, _stable_order(p)[: np.count_nonzero(p)].tolist(), "random"))
    for p, want, text in cases:
        what = f"smallest_mass_set(p, 1.0) for p = {_show(p)} ({text})"
        got = _mass_set(sp, p, 1.0, what)
        _check_set(got, want, p, 1.0, what)


def test_smallest_mass_set_when_rounding_never_reaches_mass(sp):
    """A law that sums to 1 within 1e-9 (in its own order, with math.fsum too), whose cumulative probability by
    decreasing probability stops at 1 - 9007201 · 2⁻⁵³ (each 3 · 2⁻⁵⁶ is lost when added to it): it never reaches
    mass - 1e-9 for mass = 1. The set is then every outcome of positive probability, never the one of probability 0."""
    tiny = 3 * 2.0 ** -56
    large = 1.0 - 9007201 * 2.0 ** -53
    p = [tiny] * 5 + [large, 0.0]
    cumulative = np.cumsum(np.array(p)[_stable_order(p)])
    assert abs(sum(p) - 1) <= 1e-9 and abs(math.fsum(p) - 1) <= 1e-9 and abs(float(np.sum(p)) - 1) <= 1e-9, "oracle"
    assert cumulative[-1] < 1 - 1e-9 and 1 - cumulative[-1] > 1e-9, "oracle: the cumulative sum stops below 1 - 1e-9"
    what = ("smallest_mass_set([t, t, t, t, t, 1 - 9007201 · 2⁻⁵³, 0.0], 1.0) with t = 3 · 2⁻⁵⁶ (the cumulative "
            "probability by decreasing probability never reaches 1 - 1e-9)")
    got = _mass_set(sp, p, 1.0, what)
    _check_set(got, [5, 0, 1, 2, 3, 4], p, 1.0, what)


@pytest.mark.parametrize("p, want", [([1.0], [0]), ([0.0, 0.0, 1.0], [2]), ([0.0, 1.0, 0.0, 0.0], [1])],
                         ids=["one-outcome", "certain-last", "certain-second"])
def test_smallest_mass_set_of_a_certain_outcome(sp, p, want):
    for mass in (0.05, 0.62, 1.0):
        what = f"smallest_mass_set({p}, {mass})"
        got = _mass_set(sp, p, mass, what)
        _check_set(got, want, p, mass, what)


def test_smallest_mass_set_grows_with_mass_and_each_set_starts_the_next(sp):
    """For increasing masses the sets are nested: each one is the beginning of the next."""
    rng = np.random.default_rng(6564)
    for k in range(6):
        p = _random_law(rng, 12, n_zeros=k % 3, decimals=2 if k % 2 else None)
        previous = np.zeros(0, dtype=int)
        for mass in np.linspace(0.05, 1.0, 20):
            what = f"smallest_mass_set(p, {mass:.4g}) for p = {_show(p)}"
            got = _mass_set(sp, p, float(mass), what)
            assert got.size >= previous.size and np.array_equal(got[:previous.size], previous), (
                f"expected array({previous.tolist()}) (the set for a smaller mass) at the beginning of {what}, got "
                f"array({got.tolist()}) ({_mass_hint(got, p, float(mass))})")
            previous = got


def test_smallest_mass_set_shrinks_when_the_law_is_cooled(sp):
    """Laws tempered by the test itself (scipy.special.softmax of ln p / T): as T decreases, the j most probable
    outcomes weigh more, so the set of a given mass never grows; the outcomes keep their order."""
    rng = np.random.default_rng(6565)
    for k in range(5):
        p = _random_law(rng, 10, n_zeros=k % 2)
        for mass in (0.45, 0.85):
            sizes = []
            for T in (4.0, 1.75, 1.0, 0.85, 0.45, 0.25, 0.05):
                q = _temper_oracle(p, T)
                what = f"smallest_mass_set(q, {mass}) for q = p tempered at T = {T}, p = {_show(p)}"
                got = _mass_set(sp, q, mass, what)
                _check_set(got, _expected_set(q, mass), q, mass, what)
                sizes.append(got.size)
            assert all(b <= a for a, b in zip(sizes, sizes[1:])), (
                f"expected sets that never grow as T decreases for mass {mass} and p = {_show(p)}, got the sizes "
                f"{sizes} ({MASS_HINT})")


def test_smallest_mass_set_accepts_lists_integers_and_numpy_numbers(sp):
    """p as a list, an int64 array or a float32 array; mass as a Python int, a np.float64 or a np.float32."""
    for p, mass, want, text in (([0, 1, 0], 1, [1], "a list of integers, mass the int 1"),
                                (np.array([0, 0, 1], dtype=np.int64), np.float64(0.35), [2], "an int64 array"),
                                (np.array([0.3125, 0.6875], dtype=np.float32), np.float32(0.72), [1, 0],
                                 "float32 arrays"),
                                ([0.21, 0.13, 0.66], np.float64(0.83), [2, 0], "mass a np.float64")):
        what = f"smallest_mass_set({p!r}, {mass!r}) ({text})"
        got = _mass_set(sp, p, mass, what)
        _check_set(got, want, np.asarray(p, dtype=float), float(mass), what)


def test_smallest_mass_set_does_not_modify_its_input(sp_module):
    p = np.array([0.17, 0.0, 0.52, 0.31])
    copy = p.copy()
    _result(lambda: sp_module.smallest_mass_set(p, 0.7), "a set of indices", "smallest_mass_set(p, 0.7)")
    assert np.array_equal(p, copy), (f"expected p unchanged by smallest_mass_set, got p = {_show(p)} (never modify the "
                                     f"arrays you receive: p.sort() or p[::-1].sort() writes into p; np.argsort does "
                                     f"not)")


@pytest.mark.parametrize("p, why", LAW_REFUSALS, ids=LAW_IDS)
def test_smallest_mass_set_refuses_a_bad_law(sp, p, why):
    _expect_error(ValueError, lambda: sp.smallest_mass_set(p, 0.62), f"smallest_mass_set({p!r}, 0.62)", why)


MASS_REFUSALS = [(0, "mass = 0"), (0.0, "mass = 0.0"), (-0.2, "mass is negative"), (1.000001, "mass is above 1"),
                 (1.5, "mass = 1.5"), (np.inf, "mass is inf"), (-np.inf, "mass is -inf"), (np.nan, "mass is nan"),
                 (np.float64("nan"), "mass is np.float64(nan)"), (True, "mass is True, a bool"),
                 (False, "mass is False, a bool"), (np.True_, "mass is np.True_, a NumPy bool")]


@pytest.mark.parametrize("mass, why", MASS_REFUSALS, ids=["zero", "zero-float", "negative", "just-above-1", "above-1",
                                                          "inf", "minus-inf", "nan", "numpy-nan", "true", "false",
                                                          "numpy-bool"])
def test_smallest_mass_set_refuses_a_bad_mass(sp, mass, why):
    _expect_error(ValueError, lambda: sp.smallest_mass_set([0.13, 0.54, 0.33], mass),
                  f"smallest_mass_set([0.13, 0.54, 0.33], {mass!r})", why)
