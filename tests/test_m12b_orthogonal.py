"""Tests of mymath.orthogonal (chapter M12b): Gram-Schmidt, orthogonal projection, QR, least squares by QR.

Oracles: NumPy (``np.linalg.qr`` with its signs made positive, ``np.linalg.lstsq``) and properties (QᵀQ = I, QR = A,
a residual orthogonal to the columns, a projection that does not move a vector of the subspace). They describe the
expected behaviour without showing the solution.

    pytest tests/test_m12b_orthogonal.py              # your code
    pytest tests/test_m12b_orthogonal.py --impl=ref   # the reference
"""

import ast
import inspect

import numpy as np
import pytest


@pytest.fixture
def orthogonal(mymath_module):
    return mymath_module("orthogonal")


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError being reported with what was expected first."""
    try:
        return call()
    except NotImplementedError:
        raise                 # a function not written yet: ⏳
    except Exception as exc:  # noqa: BLE001 - the learner's error, after what was expected
        pytest.fail(f"expected {expected}{' for ' + what if what else ''}, but it raised {type(exc).__name__}: {exc}"
                    + (f" ({hint})" if hint else ""))


def _expect_value_error(call, what, why):
    """Fail with what was expected first, whatever the function did instead of raising ValueError itself."""
    try:
        result = call()
    except NotImplementedError:
        raise                 # a function not written yet stays ⏳
    except ValueError as exc:
        if type(exc) is ValueError:
            return
        pytest.fail(f"expected {what} to raise ValueError itself ({why}), got {type(exc).__name__}: catch it and "
                    f"raise ValueError, as the docstring asks")
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


def _numpy_qr(A):
    """The reduced QR of NumPy, with the signs chosen so that R has a positive diagonal (the docstring convention)."""
    Q, R = np.linalg.qr(np.asarray(A, dtype=float))
    signs = np.sign(np.diag(R))
    signs[signs == 0] = 1.0
    return Q * signs, R * signs[:, None]


# ---------------------------------------------------------------- no ready-made tool
FORBIDDEN = {"qr", "lstsq", "pinv", "inv"}
ADVICE = {".qr": "build Q column by column with Gram-Schmidt", ".lstsq": "use your qr, then back substitution",
          ".pinv": "use your qr, then back substitution", ".inv": "solve a system instead of inverting"}


def test_orthogonal_uses_no_ready_made_tool(orthogonal):
    """orthogonal.py builds its own Q: no np.linalg.qr, lstsq, pinv, inv, SciPy or scikit-learn."""
    try:
        tree = ast.parse(inspect.getsource(orthogonal))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in FORBIDDEN:
            found.add(f".{node.attr}")
        elif isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names if alias.name.split(".")[0] in ("scipy", "sklearn"))
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.split(".")[0] in ("scipy", "sklearn"):
                found.add(node.module)
            elif node.module.startswith("numpy"):
                found.update(f".{alias.name}" for alias in node.names if alias.name in FORBIDDEN)
    hints = "; ".join(sorted({ADVICE.get(name, "use NumPy's elementary tools") for name in found}))
    assert not found, (f"expected orthogonal.py to use @, .T, np.linalg.norm and np.linalg.solve only (the tests compare "
                       f"with np.linalg.qr and lstsq), found {sorted(found)}: {hints}")


# ---------------------------------------------------------------- data
RNG = np.random.default_rng(1222)
FAMILIES = {   # independent columns; none is an example of the fiche, of a docstring or of an exercise
    "tall-5x3": RNG.normal(size=(5, 3)),
    "square-4x4": RNG.integers(-5, 6, size=(4, 4)).astype(float),
    "one-column": np.array([[0.0], [-3.0], [4.0], [0.0]]),
    "first-column-small": np.array([[1e-3, 2.0], [2e-3, -1.0], [-2e-3, 0.5]]),
    "integers-6x2": np.array([[1.0, 4.0], [2.0, -1.0], [0.0, 3.0], [-1.0, 2.0], [3.0, 0.0], [1.0, 1.0]]),
}
LAUCHLI = np.array([[1.0, 1.0, 1.0], [1e-8, 0.0, 0.0], [0.0, 1e-8, 0.0], [0.0, 0.0, 1e-8]])   # nearly dependent


def _loss(Q):
    return float(np.max(np.abs(Q.T @ Q - np.eye(Q.shape[1]))))


# ---------------------------------------------------------------- gram_schmidt
@pytest.mark.parametrize("name", list(FAMILIES))
@pytest.mark.parametrize("modified", [True, False])
def test_gram_schmidt_matches_numpy_qr(orthogonal, name, modified):
    A = FAMILIES[name]
    expected, _ = _numpy_qr(A)
    got = _result(lambda: orthogonal.gram_schmidt(A.copy(), modified=modified), f"a {expected.shape} matrix Q", name)
    _array(got, f"gram_schmidt for {name}", expected.shape)
    assert np.allclose(got, expected, rtol=0, atol=1e-9), (
        f"expected Q = {_show(expected)} for {name} (modified={modified}), got {_show(got)} (column k: a_k minus its "
        f"projections on the previous columns of Q, divided by its norm, with q_k · a_k > 0)")


def test_gram_schmidt_docstring_example(orthogonal):
    got = _result(lambda: orthogonal.gram_schmidt([[3, 1], [4, 2]]), "[[0.6, -0.8], [0.8, 0.6]]", "the docstring")
    assert np.allclose(np.asarray(got, dtype=float), [[0.6, -0.8], [0.8, 0.6]]), (
        f"expected [[0.6, -0.8], [0.8, 0.6]] for gram_schmidt([[3, 1], [4, 2]]), got {got!r}")


def test_gram_schmidt_keeps_the_spans(orthogonal):
    A = FAMILIES["tall-5x3"]
    Q = _result(lambda: orthogonal.gram_schmidt(A), "a matrix Q", "tall-5x3")
    for k in range(1, 4):
        coefficients = np.linalg.lstsq(Q[:, :k], A[:, :k], rcond=None)[0]
        assert np.allclose(Q[:, :k] @ coefficients, A[:, :k], atol=1e-10), (
            f"expected a_1, …, a_{k} to be combinations of q_1, …, q_{k} (the same subspace), but they are not")
    assert np.all(np.sum(Q * A, axis=0) > 0), (
        f"expected q_k · a_k > 0 for every k (divide by the norm, never by minus the norm), got "
        f"{_show(np.sum(Q * A, axis=0))}")


def test_modified_gram_schmidt_stays_orthogonal_on_nearly_dependent_columns(orthogonal):
    got = _result(lambda: orthogonal.gram_schmidt(LAUCHLI.copy(), modified=True), "a (4, 3) matrix Q",
                  "three columns that differ by 1e-8")
    _array(got, "gram_schmidt(..., modified=True)", (4, 3))
    assert _loss(got) <= 1e-6, (
        f"expected QᵀQ = I within 1e-6 with modified=True, got an error of {_loss(got):.1e}: remove each projection "
        f"from the current vector v (q_j · v), not from the original column (q_j · a_k)")


def test_classical_gram_schmidt_is_really_classical(orthogonal):
    got = _result(lambda: orthogonal.gram_schmidt(LAUCHLI.copy(), modified=False), "a (4, 3) matrix Q",
                  "three columns that differ by 1e-8, modified=False")
    _array(got, "gram_schmidt(..., modified=False)", (4, 3))
    assert _loss(got) >= 0.1, (
        f"expected the classical process (modified=False) to lose orthogonality here (QᵀQ far from I, as the docstring "
        f"says), got an error of only {_loss(got):.1e}: with modified=False, compute every coefficient q_j · a_k from "
        f"the original column a_k")


@pytest.mark.parametrize("A, why", [
    ([[1.0, 2.0], [2.0, 4.0], [-1.0, -2.0]], "the second column is twice the first"),
    ([[3.0, 0.0, 3.0], [1.0, 1.0, 2.0], [0.0, 2.0, 2.0]], "the third column is the sum of the first two"),
    ([[2e8, 4e8], [1e8, 2e8]], "a dependent pair with large numbers: the test is relative to the norm of a_k"),
    ([[1.0, 0.0, 2.0], [0.0, 1.0, 3.0]], "three vectors of R^2 are always dependent"),
    ([[0.0, 1.0], [0.0, 2.0]], "a zero column"),
    ([1.0, 2.0, 3.0], "a 1-D vector is not a matrix"),
])
def test_gram_schmidt_rejects_dependent_columns(orthogonal, A, why):
    _expect_value_error(lambda: orthogonal.gram_schmidt(A), f"gram_schmidt({A})", why)


def test_gram_schmidt_accepts_small_independent_columns(orthogonal):
    A = 1e-8 * np.array([[1.0, 1.0], [0.0, 2.0], [1.0, 0.0]])
    got = _result(lambda: orthogonal.gram_schmidt(A), "a (3, 2) matrix Q", "independent columns of norm about 1e-8",
                  "the dependence test is relative: compare with tol times the norm of a_k, not with tol")
    _array(got, "gram_schmidt of small columns", (3, 2))
    assert _loss(got) <= 1e-12, f"expected QᵀQ = I, got an error of {_loss(got):.1e}"


def test_gram_schmidt_does_not_modify_its_input(orthogonal):
    A = FAMILIES["integers-6x2"].copy()
    A0 = A.copy()
    _result(lambda: orthogonal.gram_schmidt(A), "a matrix", "an array")
    assert np.array_equal(A, A0), "expected gram_schmidt to leave its input unchanged (work on a copy)"


# ---------------------------------------------------------------- project
PROJECTIONS = {
    "plane-of-R3": (np.array([[1.0, 2.0], [0.0, 1.0], [1.0, -1.0]]), np.array([3.0, -1.0, 2.0])),
    "line-of-R4": (np.array([[2.0], [-1.0], [0.0], [2.0]]), np.array([1.0, 1.0, 1.0, 1.0])),
    "random-3-of-R6": (RNG.normal(size=(6, 3)), RNG.normal(size=6)),
    "whole-space": (RNG.normal(size=(3, 3)), RNG.normal(size=3)),
}


@pytest.mark.parametrize("name", list(PROJECTIONS))
def test_project_matches_least_squares(orthogonal, name):
    A, v = PROJECTIONS[name]
    expected = A @ np.linalg.lstsq(A, v, rcond=None)[0]
    got = _result(lambda: orthogonal.project(v.copy(), A.copy()), f"the projection {_show(expected)}", name)
    _array(got, f"project for {name}", v.shape)
    assert np.allclose(got, expected, rtol=0, atol=1e-10), (
        f"expected {_show(expected)} for {name}, got {_show(got)} (p = Q Qᵀ v with Q an orthonormal basis of the column "
        f"space: the columns of A themselves are not orthonormal)")
    assert np.allclose(A.T @ (v - got), 0, atol=1e-9), "expected the residual v - p to be orthogonal to every column"


def test_project_docstring_examples(orthogonal):
    for v, A, expected in [([1, 2, 3], [[1], [1], [1]], [2.0, 2.0, 2.0]), ([1, 2, 3], [[1, 0], [0, 1], [0, 0]], [1.0, 2.0, 0.0])]:
        got = _result(lambda v=v, A=A: orthogonal.project(v, A), f"{expected}", f"project({v}, {A})")
        assert np.allclose(np.asarray(got, dtype=float), expected), f"expected {expected} for project({v}, {A}), got {got!r}"


def test_project_keeps_a_vector_of_the_subspace_and_is_idempotent(orthogonal):
    A, v = PROJECTIONS["random-3-of-R6"]
    inside = A @ np.array([2.0, -1.0, 0.5])
    got = _result(lambda: orthogonal.project(inside, A), "the vector itself", "a vector of the column space")
    assert np.allclose(got, inside, atol=1e-10), f"expected a vector of the subspace to stay where it is, got {_show(got)}"
    once = _result(lambda: orthogonal.project(v, A), "a vector", "v")
    twice = _result(lambda: orthogonal.project(once, A), "the same vector", "the projection of the projection")
    assert np.allclose(once, twice, atol=1e-10), "expected projecting twice to change nothing (P² = P)"


@pytest.mark.parametrize("v, A, why", [
    ([1.0, 2.0], [[1.0], [0.0], [1.0]], "v has 2 coordinates, A has 3 rows"),
    ([1.0, 2.0, 3.0], [[1.0, 2.0], [0.0, 0.0], [1.0, 2.0]], "the columns of A are dependent"),
    ([[1.0], [2.0]], [[1.0], [1.0]], "v must be a 1-D vector"),
])
def test_project_rejects_invalid_inputs(orthogonal, v, A, why):
    _expect_value_error(lambda: orthogonal.project(v, A), f"project({v}, {A})", why)


def test_project_does_not_modify_its_inputs(orthogonal):
    A, v = (M.copy() for M in PROJECTIONS["plane-of-R3"])
    A0, v0 = A.copy(), v.copy()
    _result(lambda: orthogonal.project(v, A), "a vector", "arrays")
    assert np.array_equal(A, A0) and np.array_equal(v, v0), "expected project to leave A and v unchanged"


# ---------------------------------------------------------------- qr
@pytest.mark.parametrize("name", list(FAMILIES))
def test_qr_matches_numpy(orthogonal, name):
    A = FAMILIES[name]
    expected_Q, expected_R = _numpy_qr(A)
    got = _result(lambda: orthogonal.qr(A.copy()), "a tuple (Q, R)", name)
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (Q, R) for {name}, got {type(got).__name__}"
    Q, R = got
    _array(Q, f"Q for {name}", expected_Q.shape)
    _array(R, f"R for {name}", expected_R.shape)
    assert np.allclose(R, expected_R, rtol=0, atol=1e-9), (
        f"expected R = {_show(expected_R)} for {name}, got {_show(R)} (R = QᵀA, upper triangular, positive diagonal)")
    assert np.allclose(Q, expected_Q, rtol=0, atol=1e-9), f"expected Q = {_show(expected_Q)} for {name}, got {_show(Q)}"
    assert np.allclose(Q @ R, A, atol=1e-9), "expected Q R = A"


def test_qr_r_is_exactly_upper_triangular(orthogonal):
    A = FAMILIES["tall-5x3"]
    _, R = _result(lambda: orthogonal.qr(A), "a tuple (Q, R)", "tall-5x3")
    below = R[np.tril_indices(R.shape[0], -1)]
    assert np.all(below == 0.0), (f"expected the entries of R below the diagonal to be exactly 0 (np.triu), got "
                                  f"{_show(below)}")


def test_qr_uses_the_modified_process(orthogonal):
    Q, _ = _result(lambda: orthogonal.qr(LAUCHLI.copy()), "a tuple (Q, R)", "three columns that differ by 1e-8")
    assert _loss(Q) <= 1e-6, (f"expected QᵀQ = I within 1e-6, got an error of {_loss(Q):.1e}: qr uses gram_schmidt "
                              f"with modified=True")


def test_qr_docstring_example(orthogonal):
    _, R = _result(lambda: orthogonal.qr([[3, 1], [4, 2]]), "a tuple (Q, R)", "the docstring")
    assert np.allclose(np.asarray(R, dtype=float), [[5.0, 2.2], [0.0, 0.4]]), (
        f"expected R = [[5., 2.2], [0., 0.4]] for qr([[3, 1], [4, 2]]), got {R!r}")


def test_qr_rejects_dependent_columns(orthogonal):
    _expect_value_error(lambda: orthogonal.qr([[1.0, 3.0], [2.0, 6.0], [0.0, 0.0]]), "qr of dependent columns",
                        "the second column is three times the first")


# ---------------------------------------------------------------- least_squares_qr
def _problem(seed, n, p):
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, p))
    return X, X @ rng.normal(size=p) + 0.2 * rng.normal(size=n)


PROBLEMS = {"20x3": _problem(41, 20, 3), "8x5": _problem(42, 8, 5), "square-4x4": _problem(43, 4, 4),
            "one-column": (np.array([[1.0], [2.0], [-1.0], [3.0]]), np.array([2.5, 3.0, -1.0, 7.5]))}


@pytest.mark.parametrize("name", list(PROBLEMS))
def test_least_squares_qr_matches_lstsq(orthogonal, name):
    X, y = PROBLEMS[name]
    expected = np.linalg.lstsq(X, y, rcond=None)[0]
    got = _result(lambda: orthogonal.least_squares_qr(X.copy(), y.copy()), f"the weights {_show(expected)}", name)
    _array(got, f"least_squares_qr for {name}", expected.shape)
    assert np.allclose(got, expected, rtol=0, atol=1e-9), (
        f"expected {_show(expected)} for {name}, got {_show(got)} (solve R w = Qᵀy by back substitution, from the last "
        f"row up)")


def test_least_squares_qr_docstring_example(orthogonal):
    got = _result(lambda: orthogonal.least_squares_qr([[1, -1], [1, 0], [1, 1]], [1, 2, 6]), "[3, 2.5]", "the docstring")
    assert np.allclose(np.asarray(got, dtype=float), [3.0, 2.5]), f"expected [3., 2.5], got {got!r}"


@pytest.mark.parametrize("X, y, why", [
    ([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0]], [1.0, 2.0, 3.0], "the columns of X are dependent"),
    ([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], [1.0, 2.0], "y has 2 values, X has 3 rows"),
    ([1.0, 2.0, 3.0], [1.0, 2.0, 3.0], "X must be a 2-D matrix"),
])
def test_least_squares_qr_rejects_invalid_inputs(orthogonal, X, y, why):
    _expect_value_error(lambda: orthogonal.least_squares_qr(X, y), f"least_squares_qr({X}, {y})", why)


def test_least_squares_qr_does_not_modify_its_inputs(orthogonal):
    X, y = (M.copy() for M in PROBLEMS["20x3"])
    X0, y0 = X.copy(), y.copy()
    _result(lambda: orthogonal.least_squares_qr(X, y), "a vector", "arrays")
    assert np.array_equal(X, X0) and np.array_equal(y, y0), "expected least_squares_qr to leave X and y unchanged"
