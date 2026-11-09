"""Tests of mymath.svd_pca (chapter M12d): singular value decomposition, low-rank approximation, pseudo-inverse,
condition number, principal axes and explained variance.

Oracles: NumPy (``np.linalg.svd``, ``pinv``, ``cond``, ``lstsq``, ``matrix_rank``, ``eigh``, ``inv``), scikit-learn
(``sklearn.decomposition.PCA``) and properties (U diag(s) Vᵀ = A, orthonormal columns, Eckart-Young's error, the four
Penrose conditions, C u = λ u). They describe the expected behaviour without showing the solution.

    pytest tests/test_m12d_svd_pca.py              # your code
    pytest tests/test_m12d_svd_pca.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings

import numpy as np
import pytest
from sklearn.decomposition import PCA


@pytest.fixture
def svd_pca(mymath_module):
    return mymath_module("svd_pca")


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    try:
        return call()
    except NotImplementedError:
        raise                 # a function not written yet: ⏳
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised {type(exc).__name__}: {exc}"
                    + (f" ({hint})" if hint else ""))


def _expect_value_error(call, what, why, hint=""):
    """Fail with what was expected first, whatever the function did instead of raising ValueError itself."""
    try:
        result = call()
    except NotImplementedError:
        raise                 # a function not written yet stays ⏳
    except ValueError as exc:
        if type(exc) is ValueError:
            return
        pytest.fail(f"expected {what} to raise ValueError itself ({why}), got {type(exc).__name__}: "
                    + (hint or "check the input yourself and raise ValueError, as the docstring asks"))
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned {result!r}")


def _array(got, what, shape):
    assert isinstance(got, np.ndarray), (f"expected {what} to be a numpy.ndarray of floats (np.array(...)), got "
                                         f"{type(got).__module__}.{type(got).__name__}")
    assert got.shape == shape, f"expected {what} to have the shape {shape}, got {got.shape}"
    assert np.issubdtype(got.dtype, np.floating), f"expected {what} to hold floats, got the dtype {got.dtype}"


def _show(M):
    return np.array2string(np.asarray(M, dtype=float), precision=4, suppress_small=True).replace("\n", "")


def _fix_rows(Vt):
    """Each row times ±1, so that its first entry of largest absolute value is positive (the module's convention)."""
    Vt = np.array(Vt, dtype=float)
    for i, row in enumerate(Vt):
        if row[int(np.argmax(np.abs(row)))] < 0:
            Vt[i] = -row
    return Vt


def _svd_oracle(A, tol=1e-6):
    """NumPy's compact SVD, cut at tol · s_max, with the module's sign convention (U follows Vᵀ)."""
    U, s, Vt = np.linalg.svd(np.asarray(A, dtype=float), full_matrices=False)
    r = int(np.sum(s > tol * s[0])) if s.size and s[0] > 0 else 0
    U, s, Vt = U[:, :r], s[:r], Vt[:r]
    fixed = _fix_rows(Vt)
    signs = np.sign(np.sum(fixed * Vt, axis=1)) if r else np.ones(0)
    return U * signs, s, fixed


# ---------------------------------------------------------------- no ready-made tool
FORBIDDEN = {"svd", "pinv", "cond", "lstsq", "matrix_rank", "svdvals"}
ADVICE = {".svd": "use np.linalg.eigh on AᵀA, as the docstring says", ".svdvals": "use np.linalg.eigh on AᵀA",
          ".pinv": "build V diag(1/s) Uᵀ from your svd", ".cond": "divide the extreme singular values of your svd",
          ".lstsq": "the pseudo-inverse gives the least squares solution", ".matrix_rank": "count what your svd keeps"}


def test_svd_pca_uses_no_ready_made_tool(svd_pca):
    """svd_pca.py computes by itself: no np.linalg.svd, pinv, cond, lstsq, matrix_rank, SciPy or scikit-learn."""
    try:
        tree = ast.parse(inspect.getsource(svd_pca))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    aliases = {"linalg"}                     # names bound to numpy.linalg: np.linalg.x, or LA.x after an import
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "numpy":
            aliases.update(a.asname or a.name for a in node.names if a.name == "linalg")
        elif isinstance(node, ast.Import):
            aliases.update(a.asname for a in node.names if a.name == "numpy.linalg" and a.asname)
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in FORBIDDEN:
            value = node.value
            if (isinstance(value, ast.Attribute) and value.attr == "linalg") or (
                    isinstance(value, ast.Name) and value.id in aliases):
                found.add(f".{node.attr}")
        elif isinstance(node, ast.Import):
            found.update(a.name for a in node.names if a.name.split(".")[0] in ("scipy", "sklearn"))
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.split(".")[0] in ("scipy", "sklearn"):
                found.add(node.module)
            elif node.module.startswith("numpy"):
                found.update(f".{a.name}" for a in node.names if a.name in FORBIDDEN)
    hints = "; ".join(sorted({ADVICE.get(name, "use NumPy's elementary tools and np.linalg.eigh") for name in found}))
    assert not found, (f"expected svd_pca.py to use @, .T, np.linalg.norm, np.linalg.solve and np.linalg.eigh only, "
                       f"found {sorted(found)}: {hints}")


# ---------------------------------------------------------------- data
RNG = np.random.default_rng(1240)


def _orthonormal(n, rng=RNG):
    return np.linalg.qr(rng.normal(size=(n, n)))[0]


def _with_singular_values(m, n, s, rng=RNG):
    """A random (m, n) matrix with the given singular values (the others are 0)."""
    S = np.zeros((m, n))
    S[np.arange(len(s)), np.arange(len(s))] = s
    return _orthonormal(m, rng) @ S @ _orthonormal(n, rng).T


MATRICES = {   # none is an example of the fiche, of a docstring or of an exercise
    "tall-5x3": _with_singular_values(5, 3, [6.0, 2.5, 0.7]),
    "wide-2x4": _with_singular_values(2, 4, [3.0, 1.2]),
    "square-4x4": _with_singular_values(4, 4, [9.0, 4.0, 1.5, 0.3]),
    "rank-2-4x3": _with_singular_values(4, 3, [5.0, 2.0]),
    "integers-3x2": np.array([[2.0, 1.0], [-1.0, 3.0], [0.0, 2.0]]),
    "row-1x3": np.array([[2.0, -1.0, 4.0]]),
    "column-3x1": np.array([[2.0], [-1.0], [2.0]]),
    "large-entries-3x3": 1e6 * _with_singular_values(3, 3, [2.0, 1.0, 0.25]),
    "random-6x5": RNG.normal(size=(6, 5)),
}


# ---------------------------------------------------------------- svd
@pytest.mark.parametrize("name", list(MATRICES))
def test_svd_reconstructs_a(svd_pca, name):
    A = MATRICES[name]
    got = _result(lambda: svd_pca.svd(A.copy()), "a tuple (U, s, Vt)", name)
    assert isinstance(got, tuple) and len(got) == 3, f"expected a tuple (U, s, Vt) of 3 arrays for {name}, got {got!r}"
    U, s, Vt = (np.asarray(x) for x in got)
    scale = max(1.0, float(np.max(np.abs(A))))
    hint = "U = A V / s, column by column"
    if s.size == 0:
        hint = "s is empty: the cut-off removed every value; sort the eigenvalues of AᵀA in decreasing order first"
    elif s.ndim == 1 and np.any(np.diff(s) > 0):
        hint = "s is increasing: sort the eigenvalues of AᵀA in decreasing order first"
    assert U.ndim == 2 and Vt.ndim == 2 and np.allclose((U * s) @ Vt, A, rtol=0, atol=1e-9 * scale), (
        f"expected U diag(s) Vt to give back A for {name}, got {_show((U * s) @ Vt)} instead of {_show(A)} "
        f"({hint})")


@pytest.mark.parametrize("name", list(MATRICES))
def test_svd_matches_numpy(svd_pca, name):
    A = MATRICES[name]
    U_np, s_np, Vt_np = _svd_oracle(A)
    U, s, Vt = _result(lambda: svd_pca.svd(A.copy()), "a tuple (U, s, Vt)", name)
    m, n = A.shape
    r = s_np.size
    _array(s, f"s for {name}", (r,))
    _array(Vt, f"Vt for {name}", (r, n))
    _array(U, f"U for {name}", (m, r))
    assert np.allclose(s, s_np, rtol=1e-9, atol=0), (
        f"expected the singular values {_show(s_np)} for {name} (np.linalg.svd), got {_show(s)} (the square roots of "
        f"the eigenvalues of AᵀA, in decreasing order)")
    assert np.allclose(Vt, Vt_np, rtol=0, atol=1e-8), (
        f"expected Vt = {_show(Vt_np)} for {name} (np.linalg.svd, sign convention of the module), got {_show(Vt)} "
        f"(the eigenvectors of AᵀA as ROWS, each with its first entry of largest absolute value positive)")
    assert np.allclose(U, U_np, rtol=0, atol=1e-8), (
        f"expected U = {_show(U_np)} for {name} (np.linalg.svd), got {_show(U)} (column i of U is A v_i / s_i)")


@pytest.mark.parametrize("name", list(MATRICES))
def test_svd_vectors_are_orthonormal(svd_pca, name):
    A = MATRICES[name]
    U, s, Vt = (np.asarray(x) for x in _result(lambda: svd_pca.svd(A.copy()), "a tuple (U, s, Vt)", name))
    r = s.size
    assert np.allclose(Vt @ Vt.T, np.eye(r), atol=1e-12), (
        f"expected orthonormal rows of Vt (Vt Vtᵀ = I) for {name}, got Vt Vtᵀ = {_show(Vt @ Vt.T)}")
    assert np.allclose(U.T @ U, np.eye(r), atol=1e-9), (
        f"expected orthonormal columns of U (UᵀU = I) for {name}, got UᵀU = {_show(U.T @ U)} (divide A v_i by s_i)")


def test_svd_values_are_positive_and_decreasing(svd_pca):
    A = MATRICES["random-6x5"]
    _, s, _ = _result(lambda: svd_pca.svd(A), "a tuple (U, s, Vt)", "a random 6 × 5 matrix")
    assert np.all(s > 0) and np.all(np.diff(s) <= 0), (
        f"expected positive singular values in decreasing order, got {_show(s)}")


def test_svd_sign_convention(svd_pca):
    A = MATRICES["random-6x5"]
    _, _, Vt = _result(lambda: svd_pca.svd(A), "a tuple (U, s, Vt)", "a random 6 × 5 matrix")
    for i, row in enumerate(np.asarray(Vt)):
        assert row[int(np.argmax(np.abs(row)))] > 0, (
            f"expected row {i} of Vt to have its first entry of largest absolute value positive, got {_show(row)} "
            f"(multiply the eigenvector by -1, and U's column with it)")


@pytest.mark.parametrize("rows, rank", [
    ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], 2),
    ([[2.0, -1.0, 3.0], [-4.0, 2.0, -6.0]], 1),
    ([[1.0, 0.0], [0.0, 0.0], [0.0, 0.0]], 1),
    ([[3.0, 1.0, 1.0], [1.0, 3.0, 1.0], [5.0, 7.0, 3.0], [2.0, 2.0, 1.0]], 2),
])
def test_svd_keeps_the_numerical_rank(svd_pca, rows, rank):
    assert np.linalg.matrix_rank(np.array(rows)) == rank
    U, s, Vt = _result(lambda: svd_pca.svd(rows), f"{rank} singular values", f"svd({rows})")
    assert np.asarray(s).size == rank, (
        f"expected {rank} singular value(s) for {rows} (np.linalg.matrix_rank), got {_show(s)}: keep only the "
        f"values above tol · s_max (the eigenvalues of AᵀA of order 1e-16 · s_max² are rounding errors)")
    assert np.asarray(U).shape == (len(rows), rank) and np.asarray(Vt).shape == (rank, len(rows[0])), (
        f"expected U of shape {(len(rows), rank)} and Vt of shape {(rank, len(rows[0]))}, got "
        f"{np.asarray(U).shape} and {np.asarray(Vt).shape}")


def test_svd_u_is_a_v_divided_by_s(svd_pca):
    A = _with_singular_values(5, 3, [1.0, 1e-2, 1e-5], np.random.default_rng(1255))   # κ = 1e5
    U, s, Vt = _result(lambda: svd_pca.svd(A, tol=1e-12), "three singular values", "κ = 1e5, tol = 1e-12")
    U, s, Vt = np.asarray(U), np.asarray(s), np.asarray(Vt)
    assert s.shape == (3,), f"expected 3 singular values with tol = 1e-12, got {_show(s)}"
    gap = float(np.max(np.abs(U * s - A @ Vt.T)))
    assert gap <= 1e-14 * np.linalg.norm(A), (
        f"expected the columns of U to be exactly A v_i / s_i (U * s == A @ Vt.T within 1e-14), got a gap of "
        f"{gap:.1e}: divide A v_i by s_i, as the docstring says (normalizing A v_i instead hides the error on s_i)")


def test_svd_clips_the_negative_eigenvalues_of_ata(svd_pca):
    rng = np.random.default_rng(1241)
    A = np.outer(rng.normal(size=5), rng.normal(size=4))          # rank 1: AᵀA has three eigenvalues of order 1e-16
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)            # √ of a negative number: "invalid value"
        U, s, Vt = _result(lambda: svd_pca.svd(A), "one singular value, without a RuntimeWarning",
                           "a rank-1 matrix of random floats",
                           "if it is a RuntimeWarning (invalid value in sqrt): clip the tiny negative eigenvalues "
                           "of AᵀA to 0 before the square root")
    assert np.all(np.isfinite(s)) and np.all(np.isfinite(U)), (
        f"expected finite results for a rank-1 matrix, got s = {_show(s)}: clip the tiny negative eigenvalues of "
        f"AᵀA to 0 before √")
    assert np.asarray(s).size == 1, f"expected 1 singular value for a rank-1 matrix, got {_show(s)}"


def test_svd_tol_drops_small_values(svd_pca):
    A = _with_singular_values(4, 3, [10.0, 1.0, 1e-4], np.random.default_rng(1242))
    _, s_default, _ = _result(lambda: svd_pca.svd(A), "3 singular values", "s = (10, 1, 1e-4), tol = 1e-6")
    assert np.asarray(s_default).size == 3, (
        f"expected 3 singular values with the default tol (1e-4 > 1e-6 · 10), got {_show(s_default)}")
    _, s_cut, _ = _result(lambda: svd_pca.svd(A, tol=1e-4), "2 singular values", "s = (10, 1, 1e-4), tol = 1e-4")
    assert np.asarray(s_cut).size == 2, (
        f"expected 2 singular values with tol=1e-4 (1e-4 is below tol · s_max = 1e-3: dropped), got {_show(s_cut)}: "
        f"compare with tol · s_max, not with tol")


def test_svd_drops_a_value_equal_to_the_threshold(svd_pca):
    _, s, _ = _result(lambda: svd_pca.svd([[4, 0], [0, 1]], tol=0.25), "one singular value",
                      "svd([[4, 0], [0, 1]], tol=0.25)")
    assert np.asarray(s).size == 1, (
        f"expected one singular value for diag(4, 1) with tol=0.25, got {_show(s)}: a value AT MOST tol · s_max "
        f"(here 1 = 0.25 × 4) is dropped, keep only s > tol · s_max")


def test_svd_of_a_zero_matrix(svd_pca):
    U, s, Vt = _result(lambda: svd_pca.svd(np.zeros((3, 2))), "empty arrays", "a zero 3 × 2 matrix")
    assert np.asarray(U).shape == (3, 0) and np.asarray(s).shape == (0,) and np.asarray(Vt).shape == (0, 2), (
        f"expected shapes (3, 0), (0,) and (0, 2) for a zero matrix (r = 0), got {np.asarray(U).shape}, "
        f"{np.asarray(s).shape} and {np.asarray(Vt).shape}")


def test_svd_docstring_example(svd_pca):
    U, s, Vt = _result(lambda: svd_pca.svd([[3, 0], [0, -2]]), "the docstring's example", "svd([[3, 0], [0, -2]])")
    assert np.allclose(s, [3, 2]) and np.allclose(U, [[1, 0], [0, -1]]) and np.allclose(Vt, [[1, 0], [0, 1]]), (
        f"expected s = [3, 2], U = [[1, 0], [0, -1]], Vt = I, got s = {_show(s)}, U = {_show(U)}, Vt = {_show(Vt)}")


@pytest.mark.parametrize("A, why", [([1.0, 2.0, 3.0], "a 1-D vector"), (np.ones((2, 2, 2)), "a 3-D array")])
def test_svd_rejects_what_is_not_a_matrix(svd_pca, A, why):
    _expect_value_error(lambda: svd_pca.svd(A), "svd", why)


def test_svd_does_not_modify_its_input(svd_pca):
    A = MATRICES["integers-3x2"].copy()
    _result(lambda: svd_pca.svd(A), "a tuple (U, s, Vt)", "a 3 × 2 matrix")
    assert np.array_equal(A, MATRICES["integers-3x2"]), "expected svd to leave its input unchanged: work on a copy"


# ---------------------------------------------------------------- low_rank_approximation
@pytest.mark.parametrize("name", ["tall-5x3", "square-4x4", "random-6x5", "integers-3x2"])
def test_low_rank_matches_the_truncated_svd(svd_pca, name):
    A = MATRICES[name]
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    for k in range(min(A.shape) + 1):
        expected = (U[:, :k] * s[:k]) @ Vt[:k]
        got = _result(lambda: svd_pca.low_rank_approximation(A.copy(), k), f"the rank-{k} approximation", name)
        _array(got, f"the rank-{k} approximation of {name}", A.shape)
        assert np.allclose(got, expected, rtol=0, atol=1e-9 * max(1.0, s[0])), (
            f"expected the rank-{k} approximation {_show(expected)} for {name} (np.linalg.svd truncated), got "
            f"{_show(got)} (keep the k largest singular values: Σ_(i ≤ k) s_i u_i v_iᵀ)")


@pytest.mark.parametrize("name", ["tall-5x3", "square-4x4", "random-6x5"])
def test_low_rank_error_is_the_sum_of_the_dropped_squares(svd_pca, name):
    A = MATRICES[name]
    s = np.linalg.svd(A, compute_uv=False)
    for k in range(min(A.shape)):
        got = _result(lambda: svd_pca.low_rank_approximation(A, k), f"the rank-{k} approximation", name)
        error = float(np.sum((A - got) ** 2))
        assert error == pytest.approx(float(np.sum(s[k:] ** 2)), rel=1e-8, abs=1e-12), (
            f"expected ‖A − A_k‖_F² = {np.sum(s[k:] ** 2):.6g} (Eckart-Young: the dropped s_i²) for {name}, k = {k}, "
            f"got {error:.6g}")
        assert np.linalg.matrix_rank(got, tol=1e-8 * s[0]) == k, (
            f"expected a matrix of rank {k} for {name}, got rank {np.linalg.matrix_rank(got, tol=1e-8 * s[0])}")


def test_low_rank_of_a_low_rank_matrix_is_itself(svd_pca):
    A = MATRICES["rank-2-4x3"]
    got = _result(lambda: svd_pca.low_rank_approximation(A, 3), "A itself", "a rank-2 matrix with k = 3")
    assert np.allclose(got, A, atol=1e-10), (
        f"expected A itself for a matrix of rank 2 and k = 3, got {_show(got)}: k may exceed the number of singular "
        f"values kept by svd")


def test_low_rank_with_k_zero_is_zero(svd_pca):
    A = MATRICES["tall-5x3"]
    got = _result(lambda: svd_pca.low_rank_approximation(A, 0), "a zero matrix", "k = 0")
    _array(got, "the rank-0 approximation", A.shape)
    assert np.all(got == 0), f"expected a zero (5, 3) matrix for k = 0, got {_show(got)}"


def test_low_rank_docstring_example(svd_pca):
    got = _result(lambda: svd_pca.low_rank_approximation([[3, 0], [0, 1]], 1), "[[3, 0], [0, 0]]", "the docstring")
    assert np.allclose(got, [[3, 0], [0, 0]]), f"expected [[3, 0], [0, 0]], got {_show(got)}"


@pytest.mark.parametrize("A, k, why", [
    ([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], -1, "k is negative"),
    ([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], 3, "k exceeds min(m, n) = 2"),
    ([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], 1.5, "k is not an integer"),
    ([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], True, "k is a bool, not an integer"),
    ([1.0, 2.0, 3.0], 1, "A is not 2-D"),
])
def test_low_rank_rejects_invalid_inputs(svd_pca, A, k, why):
    _expect_value_error(lambda: svd_pca.low_rank_approximation(A, k), f"low_rank_approximation(A, {k!r})", why)


def test_low_rank_does_not_modify_its_input(svd_pca):
    A = MATRICES["tall-5x3"].copy()
    _result(lambda: svd_pca.low_rank_approximation(A, 1), "an approximation", "a 5 × 3 matrix")
    assert np.array_equal(A, MATRICES["tall-5x3"]), "expected low_rank_approximation to leave its input unchanged"


# ---------------------------------------------------------------- pinv
@pytest.mark.parametrize("name", list(MATRICES))
def test_pinv_matches_numpy(svd_pca, name):
    A = MATRICES[name]
    expected = np.linalg.pinv(A, rcond=1e-6)
    got = _result(lambda: svd_pca.pinv(A.copy()), "the pseudo-inverse", name)
    _array(got, f"pinv for {name}", A.T.shape)
    scale = float(np.max(np.abs(expected)))
    assert np.allclose(got, expected, rtol=0, atol=1e-8 * scale), (
        f"expected A⁺ = {_show(expected)} for {name} (np.linalg.pinv), got {_show(got)} (V diag(1/s) Uᵀ, of shape "
        f"(n, m))")


@pytest.mark.parametrize("name", ["tall-5x3", "rank-2-4x3", "wide-2x4", "random-6x5"])
def test_pinv_satisfies_the_penrose_conditions(svd_pca, name):
    A = MATRICES[name]
    P = np.asarray(_result(lambda: svd_pca.pinv(A), "the pseudo-inverse", name))
    for label, left, right in [("A A⁺ A = A", A @ P @ A, A), ("A⁺ A A⁺ = A⁺", P @ A @ P, P),
                               ("(A A⁺)ᵀ = A A⁺", (A @ P).T, A @ P), ("(A⁺ A)ᵀ = A⁺ A", (P @ A).T, P @ A)]:
        assert np.allclose(left, right, atol=1e-9), f"expected {label} for {name}, got {_show(left)} and {_show(right)}"


@pytest.mark.parametrize("name", ["rank-2-4x3", "wide-2x4", "tall-5x3"])
def test_pinv_gives_the_minimum_norm_least_squares_solution(svd_pca, name):
    A = MATRICES[name]
    b = np.random.default_rng(1243).normal(size=A.shape[0])
    expected = np.linalg.lstsq(A, b, rcond=None)[0]
    got = np.asarray(_result(lambda: svd_pca.pinv(A), "the pseudo-inverse", name)) @ b
    assert np.allclose(got, expected, atol=1e-9), (
        f"expected A⁺ b = {_show(expected)} for {name} (np.linalg.lstsq: the least squares solution of smallest norm), "
        f"got {_show(got)}")


def test_pinv_of_an_invertible_matrix_is_its_inverse(svd_pca):
    A = MATRICES["square-4x4"]
    got = _result(lambda: svd_pca.pinv(A), "the inverse", "an invertible 4 × 4 matrix")
    assert np.allclose(got, np.linalg.inv(A), atol=1e-9), (
        f"expected A⁺ = A⁻¹ = {_show(np.linalg.inv(A))} for an invertible matrix (np.linalg.inv), got {_show(got)}")


def test_pinv_rcond_drops_small_values(svd_pca):
    A = _with_singular_values(3, 3, [2.0, 1.0, 1e-3], np.random.default_rng(1244))
    got = _result(lambda: svd_pca.pinv(A, rcond=1e-2), "a pseudo-inverse of rank 2", "s = (2, 1, 1e-3), rcond = 1e-2")
    expected = np.linalg.pinv(A, rcond=1e-2)
    assert np.allclose(got, expected, atol=1e-9), (
        f"expected {_show(expected)} (np.linalg.pinv with rcond=1e-2: 1e-3 ≤ 1e-2 · 2 counts as 0), got {_show(got)}: "
        f"pass rcond to svd as its tol")


def test_pinv_of_a_zero_matrix_is_zero(svd_pca):
    got = _result(lambda: svd_pca.pinv(np.zeros((2, 3))), "a zero (3, 2) matrix", "a zero 2 × 3 matrix")
    _array(got, "pinv of a zero 2 × 3 matrix", (3, 2))
    assert np.all(got == 0), f"expected a zero (3, 2) matrix, got {_show(got)}"


def test_pinv_docstring_example(svd_pca):
    got = _result(lambda: svd_pca.pinv([[1, 1], [1, 1]]), "[[0.25, 0.25], [0.25, 0.25]]", "the docstring")
    assert np.allclose(got, 0.25), f"expected [[0.25, 0.25], [0.25, 0.25]], got {_show(got)}"


def test_pinv_rejects_what_is_not_a_matrix(svd_pca):
    _expect_value_error(lambda: svd_pca.pinv([1.0, 2.0]), "pinv([1.0, 2.0])", "a 1-D vector")


def test_pinv_does_not_modify_its_input(svd_pca):
    A = MATRICES["wide-2x4"].copy()
    _result(lambda: svd_pca.pinv(A), "the pseudo-inverse", "a 2 × 4 matrix")
    assert np.array_equal(A, MATRICES["wide-2x4"]), "expected pinv to leave its input unchanged"


# ---------------------------------------------------------------- condition_number
@pytest.mark.parametrize("name", ["tall-5x3", "wide-2x4", "square-4x4", "integers-3x2", "large-entries-3x3",
                                  "random-6x5", "row-1x3", "column-3x1"])
def test_condition_number_matches_numpy(svd_pca, name):
    A = MATRICES[name]
    expected = float(np.linalg.cond(A))
    got = _result(lambda: svd_pca.condition_number(A.copy()), f"κ = {expected:.6g}", name)
    assert type(got) is float, f"expected a Python float (float(...)), got {type(got).__module__}.{type(got).__name__}"
    assert got == pytest.approx(expected, rel=1e-8), (
        f"expected κ = {expected:.10g} for {name} (np.linalg.cond), got {got!r} (s_max / s_min)")


def test_condition_number_of_an_ill_conditioned_matrix(svd_pca):
    A = _with_singular_values(3, 3, [1.0, 0.1, 1e-4], np.random.default_rng(1245))
    got = _result(lambda: svd_pca.condition_number(A), "κ = 1e4", "s = (1, 0.1, 1e-4)")
    assert got == pytest.approx(1e4, rel=1e-6), f"expected κ = 1e4 (np.linalg.cond) for s = (1, 0.1, 1e-4), got {got!r}"


@pytest.mark.parametrize("rows, why", [
    ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], "a 3 × 3 matrix of rank 2"),
    ([[2.0, -1.0, 3.0], [-4.0, 2.0, -6.0]], "a 2 × 3 matrix of rank 1"),
    ([[1.0, 0.0], [0.0, 1e-9]], "s_min / s_max = 1e-9, below the tolerance of svd"),
])
def test_condition_number_of_a_rank_deficient_matrix_is_infinite(svd_pca, rows, why):
    got = _result(lambda: svd_pca.condition_number(rows), "math.inf", why)
    assert got == math.inf and type(got) is float, (
        f"expected math.inf for {why}, got {got!r}: if svd keeps fewer than min(m, n) singular values, A does not "
        f"have full rank")


def test_condition_number_of_an_orthogonal_matrix_is_one(svd_pca):
    Q = _orthonormal(4, np.random.default_rng(1246))
    got = _result(lambda: svd_pca.condition_number(Q), "1.0", "an orthogonal 4 × 4 matrix")
    assert got == pytest.approx(1.0, abs=1e-12), f"expected κ = 1 for an orthogonal matrix (every s_i = 1), got {got!r}"


def test_condition_number_docstring_examples(svd_pca):
    for rows, expected in [([[2, 0], [0, 0.5]], 4.0), ([[1, 2], [2, 4]], math.inf)]:
        got = _result(lambda: svd_pca.condition_number(rows), repr(expected), f"condition_number({rows})")
        assert got == pytest.approx(expected), f"expected condition_number({rows}) = {expected}, got {got!r}"


@pytest.mark.parametrize("A, why", [([1.0, 2.0], "a 1-D vector"), (np.zeros((2, 3)), "a zero matrix")])
def test_condition_number_rejects_invalid_inputs(svd_pca, A, why):
    _expect_value_error(lambda: svd_pca.condition_number(A), f"condition_number({np.asarray(A).tolist()})", why)


# ---------------------------------------------------------------- principal_axes
def _covariance(p, rng, n=200):
    X = rng.normal(size=(n, p)) @ rng.normal(size=(p, p)) + rng.normal(size=p)
    return X, np.cov(X, rowvar=False)


COVARIANCES = {name: _covariance(p, np.random.default_rng(seed))
               for name, p, seed in [("covariance-2", 2, 1250), ("covariance-3", 3, 1251), ("covariance-5", 5, 1252)]}


def _axes_oracle(C):
    values, Q = np.linalg.eigh(np.asarray(C, dtype=float))
    return _fix_rows(Q[:, ::-1].T).T, values[::-1]


@pytest.mark.parametrize("name", list(COVARIANCES))
def test_principal_axes_match_eigh(svd_pca, name):
    _, C = COVARIANCES[name]
    axes_ref, variances_ref = _axes_oracle(C)
    p = C.shape[0]
    got = _result(lambda: svd_pca.principal_axes(C.copy()), "(axes, variances)", name)
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (axes, variances), got {got!r}"
    axes, variances = got
    _array(axes, f"the axes for {name}", (p, p))
    _array(variances, f"the variances for {name}", (p,))
    assert np.allclose(variances, variances_ref, rtol=1e-10, atol=1e-12), (
        f"expected the variances {_show(variances_ref)} for {name} (np.linalg.eigh, in DECREASING order), got "
        f"{_show(variances)}")
    assert np.allclose(axes, axes_ref, atol=1e-10), (
        f"expected the axes {_show(axes_ref)} for {name} (np.linalg.eigh: one axis per COLUMN, in decreasing order of "
        f"variance, its first entry of largest absolute value positive), got {_show(axes)}")


@pytest.mark.parametrize("name", list(COVARIANCES))
def test_principal_axes_match_scikit_learn(svd_pca, name):
    X, C = COVARIANCES[name]
    pca = PCA(svd_solver="full").fit(X)
    axes, variances = _result(lambda: svd_pca.principal_axes(C, k=2), "(axes, variances)", name)
    expected = _fix_rows(pca.components_[:2]).T
    assert np.allclose(np.asarray(axes), expected, atol=1e-8), (
        f"expected the first two axes {_show(expected)} for {name} (scikit-learn's PCA components_, as columns), got "
        f"{_show(axes)}")
    assert np.allclose(variances, pca.explained_variance_[:2], rtol=1e-8), (
        f"expected the variances {_show(pca.explained_variance_[:2])} for {name} (scikit-learn's explained_variance_), "
        f"got {_show(variances)}")


def test_principal_axes_maximize_the_variance(svd_pca):
    _, C = COVARIANCES["covariance-5"]
    axes, variances = (np.asarray(x) for x in _result(lambda: svd_pca.principal_axes(C), "(axes, variances)",
                                                      "a 5 × 5 covariance"))
    assert np.allclose(C @ axes, axes * variances, atol=1e-9), (
        "expected C u = λ u for each axis u (a column) and its variance λ")
    rng = np.random.default_rng(1253)
    for _ in range(50):
        u = rng.normal(size=5)
        u /= np.linalg.norm(u)
        assert u @ C @ u <= variances[0] + 1e-9, (
            f"expected no unit direction to have a larger variance than the first axis ({variances[0]:.6g}), got "
            f"{u @ C @ u:.6g} (the eigenvalues in DECREASING order)")


def test_principal_axes_keep_k_axes(svd_pca):
    _, C = COVARIANCES["covariance-5"]
    axes_ref, variances_ref = _axes_oracle(C)
    axes, variances = _result(lambda: svd_pca.principal_axes(C, k=2), "two axes", "k = 2")
    _array(axes, "the axes for k = 2", (5, 2))
    _array(variances, "the variances for k = 2", (2,))
    assert np.allclose(axes, axes_ref[:, :2], atol=1e-10) and np.allclose(variances, variances_ref[:2]), (
        f"expected the first two axes and variances, {_show(variances_ref[:2])}, got {_show(variances)}")


def test_principal_axes_return_zero_for_a_tiny_negative_eigenvalue(svd_pca):
    Q = _orthonormal(3, np.random.default_rng(1254))
    C = Q @ np.diag([3.0, 1.0, -1e-14]) @ Q.T
    C = (C + C.T) / 2
    _, variances = _result(lambda: svd_pca.principal_axes(C), "(axes, variances)", "an eigenvalue of -1e-14",
                           "eigenvalues between -1e-12 · max(1, λ_max) and 0 are rounding errors")
    assert np.all(np.asarray(variances) >= 0) and np.asarray(variances)[-1] == 0, (
        f"expected the variances (3, 1, 0), got {_show(variances)}: return the tiny negative eigenvalue as 0")
    assert not np.signbit(np.asarray(variances)[-1]), (
        "expected the last variance to be 0.0, got -0.0: np.maximum(values, 0.0) keeps the sign of -0.0, add 0.0")


def test_principal_axes_accept_a_large_symmetric_matrix(svd_pca):
    C = 1e8 * np.array([[4.0, 1.0], [1.0, 2.0]])
    C[0, 1] += 1e-6                                       # an asymmetry far below 1e-12 · max |C| = 4e-4
    _result(lambda: svd_pca.principal_axes(C), "(axes, variances)", "entries of order 1e8, an asymmetry of 1e-6",
            "the symmetry tolerance is relative: 1e-12 · max(1, max |C|)")


def test_principal_axes_docstring_example(svd_pca):
    axes, variances = _result(lambda: svd_pca.principal_axes([[2, 0], [0, 5]]), "the docstring's example",
                              "principal_axes([[2, 0], [0, 5]])")
    assert np.allclose(axes, [[0, 1], [1, 0]]) and np.allclose(variances, [5, 2]), (
        f"expected axes [[0, 1], [1, 0]] and variances [5, 2], got {_show(axes)} and {_show(variances)}")


@pytest.mark.parametrize("C, k, why", [
    ([[1.0, 2.0, 3.0], [2.0, 4.0, 5.0]], None, "C is not square"),
    ([[2.0, 1.0], [0.5, 3.0]], None, "C is not symmetric"),
    ([[2.0, 3.0], [3.0, 1.0]], None, "C has a negative eigenvalue"),
    ([[2.0, 0.0], [0.0, 1.0]], 0, "k = 0"),
    ([[2.0, 0.0], [0.0, 1.0]], 3, "k exceeds p = 2"),
    ([[2.0, 0.0], [0.0, 1.0]], 1.5, "k is not an integer"),
    ([[2.0, 0.0], [0.0, 1.0]], True, "k is a bool, not an integer"),
])
def test_principal_axes_reject_invalid_inputs(svd_pca, C, k, why):
    _expect_value_error(lambda: svd_pca.principal_axes(C, k=k), f"principal_axes({C}, k={k!r})", why)


def test_principal_axes_do_not_modify_their_input(svd_pca):
    _, C = COVARIANCES["covariance-3"]
    copy = C.copy()
    _result(lambda: svd_pca.principal_axes(copy), "(axes, variances)", "a 3 × 3 covariance")
    assert np.array_equal(copy, C), "expected principal_axes to leave its input unchanged"


# ---------------------------------------------------------------- explained_variance_ratio
@pytest.mark.parametrize("name", list(COVARIANCES))
def test_explained_variance_ratio_matches_scikit_learn(svd_pca, name):
    X, C = COVARIANCES[name]
    variances = np.linalg.eigvalsh(C)[::-1]
    expected = PCA(svd_solver="full").fit(X).explained_variance_ratio_
    got = _result(lambda: svd_pca.explained_variance_ratio(variances.copy()), "the ratios", name)
    _array(got, f"the ratios for {name}", variances.shape)
    assert np.allclose(got, expected, rtol=1e-8), (
        f"expected the ratios {_show(expected)} for {name} (scikit-learn's explained_variance_ratio_), got {_show(got)} "
        f"(each variance divided by their sum)")


def test_explained_variance_ratio_keeps_the_order(svd_pca):
    got = _result(lambda: svd_pca.explained_variance_ratio([1.0, 0.0, 3.0]), "[0.25, 0, 0.75]", "variances (1, 0, 3)")
    assert np.allclose(got, [0.25, 0.0, 0.75]), (
        f"expected [0.25, 0, 0.75] for the variances (1, 0, 3), in the same order, got {_show(got)}")


def test_explained_variance_ratio_docstring_example(svd_pca):
    got = _result(lambda: svd_pca.explained_variance_ratio([3, 1]), "[0.75, 0.25]", "the docstring")
    assert np.allclose(got, [0.75, 0.25]), f"expected [0.75, 0.25], got {_show(got)}"


@pytest.mark.parametrize("variances, why", [
    ([[1.0, 2.0]], "a 2-D array"),
    ([], "an empty list"),
    ([2.0, -0.5, 1.0], "a negative variance"),
    ([0.0, 0.0], "variances that sum to 0"),
])
def test_explained_variance_ratio_rejects_invalid_inputs(svd_pca, variances, why):
    _expect_value_error(lambda: svd_pca.explained_variance_ratio(variances), f"explained_variance_ratio({variances})",
                        why)


def test_explained_variance_ratio_does_not_modify_its_input(svd_pca):
    v = np.array([4.0, 1.0, 0.5])
    _result(lambda: svd_pca.explained_variance_ratio(v), "the ratios", "(4, 1, 0.5)")
    assert np.array_equal(v, [4.0, 1.0, 0.5]), "expected explained_variance_ratio to leave its input unchanged"
