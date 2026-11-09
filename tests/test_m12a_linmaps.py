"""Tests of mymath.linmaps (chapter M12a): independence, column space, kernel, coordinates, change of basis.

Oracles: SymPy (``Matrix.rank``, ``Matrix.columnspace``, ``Matrix.nullspace``, exact on integer matrices) and NumPy
(``np.linalg.matrix_rank``, ``np.linalg.lstsq``, ``np.linalg.inv``), plus properties (A N = 0, B c = v). They
describe the expected behaviour without showing the solution.

    pytest tests/test_m12a_linmaps.py              # your code
    pytest tests/test_m12a_linmaps.py --impl=ref   # the reference
"""

import ast
import inspect

import numpy as np
import pytest
import sympy


@pytest.fixture
def linmaps(mymath_module):
    return mymath_module("linmaps")


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
    """Fail with what was expected first, whatever the function did instead of raising ValueError."""
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


# ---------------------------------------------------------------- no ready-made tool
FORBIDDEN = {"matrix_rank", "svd", "qr", "lstsq", "pinv", "inv", "null_space", "orth"}


def test_linmaps_uses_no_ready_made_tool(linmaps):
    """linmaps.py reduces its matrices itself: np.linalg.solve only, no matrix_rank, svd, qr, lstsq, inv, SciPy, SymPy."""
    try:
        tree = ast.parse(inspect.getsource(linmaps))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in FORBIDDEN:
            found.add(f".{node.attr}")
        elif isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names if alias.name.split(".")[0] in ("sympy", "scipy"))
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.split(".")[0] in ("sympy", "scipy"):
                found.add(node.module)
            elif node.module.startswith("numpy"):
                found.update(alias.name for alias in node.names if alias.name in FORBIDDEN)
    advice = {".inv": "solve a system with np.linalg.solve instead of inverting",
              ".lstsq": "solve BᵀB c = Bᵀv with np.linalg.solve", ".pinv": "solve a system with np.linalg.solve"}
    hints = "; ".join(sorted({advice.get(name, "find the pivots by row reduction (your _rref)") for name in found}))
    assert not found, (f"expected linmaps.py to use only NumPy's elementary tools and np.linalg.solve (the tests "
                       f"compare with matrix_rank, SymPy and the others), found {sorted(found)}: {hints}")


# ---------------------------------------------------------------- data
RNG = np.random.default_rng(1212)


def _low_rank(seed, m, n, r):
    """An (m, n) integer matrix of rank r: a product of two random integer factors (rank checked by SymPy)."""
    rng = np.random.default_rng(seed)
    while True:
        M = rng.integers(-4, 5, size=(m, r)) @ rng.integers(-4, 5, size=(r, n))
        if sympy.Matrix(M.tolist()).rank() == r:
            return M.tolist()


CASES = {   # integer matrices: SymPy is exact on them; none is an example of the fiche or of an exercise
    "square-invertible-4x4": [[2, -1, 0, 3], [1, 3, -2, 0], [0, 1, 4, -1], [-3, 0, 1, 2]],
    "tall-independent-5x3": RNG.integers(-6, 7, size=(5, 3)).tolist(),
    "tall-rank-2-5x3": _low_rank(21, 5, 3, 2),
    "wide-rank-2-3x5": _low_rank(22, 3, 5, 2),
    "square-rank-3-5x5": _low_rank(23, 5, 5, 3),
    "first-column-zero": [[0, 2, -1, 4], [0, -1, 3, 1], [0, 1, 2, 5]],
    "repeated-column": [[1, 4, 4, -2], [3, -1, -1, 0], [2, 5, 5, 1]],
    "more-columns-than-rows": [[1, -2, 0, 3], [2, 1, -1, 1]],
    "one-column": [[0], [3], [-2]],
    "zero-matrix": [[0, 0, 0], [0, 0, 0]],
    "one-row": [[0, 3, -6, 1]],
}


def _sympy(A):
    return sympy.Matrix(A)


def _columns(vectors, m):
    """A list of SymPy column vectors as an (m, k) float array (shape (m, 0) for an empty list)."""
    if not vectors:
        return np.zeros((m, 0))
    return np.array(sympy.Matrix.hstack(*vectors).tolist(), dtype=float)


# ---------------------------------------------------------------- is_independent
@pytest.mark.parametrize("name", list(CASES))
def test_is_independent_matches_sympy(linmaps, name):
    A = CASES[name]
    M = _sympy(A)
    expected = M.rank() == M.shape[1]
    got = _result(lambda: linmaps.is_independent([row[:] for row in A]), str(expected), name)
    assert type(got) is bool, (f"expected a Python bool (True or False) for {name}, got "
                               f"{type(got).__module__}.{type(got).__name__}: {got!r} (convert with bool(...))")
    assert got == expected, (
        f"expected {expected} for {name} (rank {M.rank()}, {M.shape[1]} columns): the columns are independent exactly "
        f"when every column has a pivot")


def test_is_independent_docstring_examples(linmaps):
    for A, expected in [([[1, 0], [0, 1], [1, 1]], True), ([[1, 2, 3], [1, 0, 1], [0, 1, 1]], False)]:
        got = _result(lambda A=A: linmaps.is_independent(A), str(expected), f"is_independent({A})")
        assert got is expected, f"expected {expected} for is_independent({A}), got {got!r}"


def test_is_independent_uses_the_tolerance(linmaps):
    A = [[1.0, 2.0], [3.0, 6.0 + 1e-13]]   # the second column is twice the first, up to 1e-13
    got = _result(lambda: linmaps.is_independent(A), "False", "a column equal to twice the other up to 1e-13")
    assert got is False, ("expected False with the default tol = 1e-10: after elimination the second entry is about "
                          f"3e-14, which counts as zero, got {got!r}")
    got = _result(lambda: linmaps.is_independent(A, tol=1e-15), "True", "the same matrix with tol=1e-15")
    assert got is True, f"expected True with tol=1e-15: 3e-14 is then a pivot, got {got!r}"


def test_is_independent_more_vectors_than_dimension(linmaps):
    A = RNG.normal(size=(3, 4))
    got = _result(lambda: linmaps.is_independent(A), "False", "4 random vectors of ℝ³")
    assert got is False, f"expected False: more than m vectors of ℝᵐ are always dependent, got {got!r}"


def test_is_independent_does_not_modify_its_input(linmaps):
    A = np.array([[0.0, 2.0, 1.0], [3.0, 1.0, -1.0], [6.0, 4.0, 2.0]])
    A0 = A.copy()
    _result(lambda: linmaps.is_independent(A), "a bool", "an array")
    assert np.array_equal(A, A0), "expected is_independent to leave its input unchanged (work on a copy)"


def test_is_independent_rejects_a_vector(linmaps):
    _expect_value_error(lambda: linmaps.is_independent([1.0, 2.0, 3.0]), "is_independent([1.0, 2.0, 3.0])",
                        "a 1-D vector is not a matrix: one vector is the matrix [[1.0], [2.0], [3.0]]")


# ---------------------------------------------------------------- column_space_basis
@pytest.mark.parametrize("name", list(CASES))
def test_column_space_basis_matches_sympy(linmaps, name):
    A = CASES[name]
    M = _sympy(A)
    expected = _columns(M.columnspace(), M.shape[0])
    got = _result(lambda: linmaps.column_space_basis([row[:] for row in A]), f"the {expected.shape} pivot columns",
                  name)
    _array(got, f"column_space_basis for {name}", expected.shape)
    assert np.allclose(got, expected, rtol=0, atol=1e-12), (
        f"expected {_show(expected)} for {name}, got {_show(got)} (the columns of A itself whose index is a pivot "
        f"column of the reduced form, in increasing order)")


def test_column_space_basis_docstring_example(linmaps):
    got = _result(lambda: linmaps.column_space_basis([[1, 2, 0], [2, 4, 1]]), "[[1, 0], [2, 1]]", "the docstring")
    assert np.allclose(np.asarray(got, dtype=float), [[1, 0], [2, 1]]), (
        f"expected [[1., 0.], [2., 1.]] for column_space_basis([[1, 2, 0], [2, 4, 1]]), got {got!r}")


def test_column_space_basis_keeps_floats_and_the_rank(linmaps):
    A = RNG.normal(size=(6, 2)) @ RNG.normal(size=(2, 5))     # rank 2, float entries
    expected_rank = np.linalg.matrix_rank(A)
    got = _result(lambda: linmaps.column_space_basis(A), f"6 × {expected_rank} columns", "a random (6, 5) matrix of rank 2")
    _array(got, "column_space_basis of a random (6, 5) matrix of rank 2", (6, expected_rank))
    pivots = [j for j in range(5) if any(np.allclose(got[:, k], A[:, j], rtol=0, atol=1e-12) for k in range(got.shape[1]))]
    assert pivots == [0, 1], (f"expected the first two columns of A (the pivot columns), got the columns "
                              f"{[p + 1 for p in pivots]} of A (numbered from 1)")


def test_column_space_basis_does_not_modify_its_input(linmaps):
    A = np.array([[0.0, 2.0, 4.0], [3.0, 1.0, 7.0]])
    A0 = A.copy()
    _result(lambda: linmaps.column_space_basis(A), "a matrix", "an array")
    assert np.array_equal(A, A0), "expected column_space_basis to leave its input unchanged (work on a copy)"


def test_column_space_basis_rejects_a_vector(linmaps):
    _expect_value_error(lambda: linmaps.column_space_basis([1.0, 2.0]), "column_space_basis([1.0, 2.0])",
                        "a 1-D vector is not a matrix")


# ---------------------------------------------------------------- null_space_basis
@pytest.mark.parametrize("name", list(CASES))
def test_null_space_basis_matches_sympy(linmaps, name):
    A = CASES[name]
    M = _sympy(A)
    expected = _columns(M.nullspace(), M.shape[1])
    got = _result(lambda: linmaps.null_space_basis([row[:] for row in A]), f"a {expected.shape} matrix", name)
    _array(got, f"null_space_basis for {name}", expected.shape)
    assert np.allclose(got, expected, rtol=0, atol=1e-9), (
        f"expected {_show(expected)} for {name}, got {_show(got)} (one column per free column j of the reduced form "
        f"R: x[j] = 1, the other free entries 0, x[p] = -R[i, j] for the pivot of row i in column p)")


def test_null_space_basis_docstring_examples(linmaps):
    got = _result(lambda: linmaps.null_space_basis([[1, 0, 2], [0, 1, 3]]), "[[-2], [-3], [1]]", "the docstring")
    assert np.allclose(np.asarray(got, dtype=float), [[-2], [-3], [1]]), (
        f"expected [[-2.], [-3.], [1.]] for null_space_basis([[1, 0, 2], [0, 1, 3]]), got {got!r}")
    got = _result(lambda: linmaps.null_space_basis([[1, 0], [0, 1]]), "an array of shape (2, 0)", "the identity")
    assert np.shape(got) == (2, 0), (f"expected the shape (2, 0) for the kernel {{0}} of the identity (no column), "
                                     f"got {np.shape(got)}")


@pytest.mark.parametrize("seed, m, n, r", [(31, 4, 7, 2), (32, 8, 6, 3), (33, 5, 5, 4), (34, 3, 9, 3)])
def test_null_space_basis_of_random_float_matrices(linmaps, seed, m, n, r):
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(m, r)) @ rng.normal(size=(r, n))
    expected_dim = n - np.linalg.matrix_rank(A)
    got = _result(lambda: linmaps.null_space_basis(A), f"a ({n}, {expected_dim}) matrix", f"a random ({m}, {n}) matrix")
    _array(got, f"null_space_basis of a random ({m}, {n}) matrix of rank {r}", (n, expected_dim))
    assert np.allclose(A @ got, 0, rtol=0, atol=1e-9), (
        f"expected A x = 0 for every column x (within 1e-9), got a largest |A x| of {np.max(np.abs(A @ got)):.1e}")
    assert np.linalg.matrix_rank(got) == expected_dim, (
        f"expected {expected_dim} independent columns, got a family of rank {np.linalg.matrix_rank(got)}")


def test_null_space_basis_uses_partial_pivoting(linmaps):
    # a tiny first pivot (above tol): elimination without row swaps loses digits, by 1e-9 to 1e-7 here
    for eps in (4e-9, 2e-8):
        for c in ((2.0, -7.0), (0.3, 1.9)):
            A = [[eps, 1.0, c[0]], [1.0, 3.0, c[1]]]
            x = np.linalg.solve(np.array(A)[:, :2], np.array(A)[:, 2])
            expected = np.array([[-x[0]], [-x[1]], [1.0]])
            got = _result(lambda A=A: linmaps.null_space_basis([row[:] for row in A]), "a (3, 1) matrix", f"{A}")
            _array(got, f"null_space_basis for {A}", (3, 1))
            assert np.allclose(got, expected, rtol=0, atol=1e-10), (
                f"expected {_show(expected)} for {A} within 1e-10, got entries off by "
                f"{np.max(np.abs(got - expected)):.1e}: in each column, take as pivot the row (from the current row "
                f"down) whose entry has the largest absolute value, and swap (partial pivoting)")


def test_null_space_basis_uses_the_tolerance(linmaps):
    A = [[1.0, 2.0, -1.0], [3.0, 6.0 + 1e-13, 5.0]]   # the second column is twice the first, up to 1e-13
    got = _result(lambda: linmaps.null_space_basis(A), "a (3, 1) matrix", "a column equal to twice the first up to 1e-13")
    _array(got, "null_space_basis when 1e-13 counts as zero", (3, 1))
    assert np.allclose(got, [[-2.0], [1.0], [0.0]], rtol=0, atol=1e-9), (
        f"expected [[-2], [1], [0]] (column 1 is free: 3e-14 counts as zero with tol = 1e-10), got {_show(got)}")
    got = _result(lambda: linmaps.null_space_basis(A, tol=1e-15), "a (3, 1) matrix", "the same matrix with tol=1e-15")
    _array(got, "null_space_basis with tol=1e-15", (3, 1))
    assert got[2, 0] == 1.0, (f"expected the pivots 0 and 1 with tol=1e-15 (3e-14 is then a pivot), so column 2 is "
                              f"free and x[2] = 1, got {_show(got)}")


def test_null_space_basis_does_not_modify_its_input(linmaps):
    A = np.array([[0.0, 2.0, 4.0], [3.0, 1.0, 7.0]])
    A0 = A.copy()
    _result(lambda: linmaps.null_space_basis(A), "a matrix", "an array")
    assert np.array_equal(A, A0), "expected null_space_basis to leave its input unchanged (work on a copy)"


def test_null_space_basis_rejects_a_vector(linmaps):
    _expect_value_error(lambda: linmaps.null_space_basis([1.0, 2.0]), "null_space_basis([1.0, 2.0])",
                        "a 1-D vector is not a matrix")


# ---------------------------------------------------------------- coordinates
def test_coordinates_in_a_basis_of_the_whole_space(linmaps):
    B = np.array(CASES["square-invertible-4x4"], dtype=float)
    for v in ([3.0, -1.0, 2.0, 0.5], [0.0, 0.0, 0.0, 0.0], [-12.0, 7.0, 1.0, 4.0]):
        expected = np.linalg.solve(B, v)
        got = _result(lambda v=v: linmaps.coordinates(B.copy(), list(v)), f"{np.round(expected, 4)}", f"v = {v}")
        _array(got, f"coordinates of {v}", (4,))
        assert np.allclose(got, expected, rtol=0, atol=1e-10), (
            f"expected the coordinates {_show(expected)} of {v}, got {_show(got)} (they are the numbers c with "
            f"B c = v, in the order of the columns of B)")


def test_coordinates_in_a_basis_of_a_subspace(linmaps):
    B = np.array([[1.0, 0.0], [2.0, 1.0], [0.0, -1.0], [1.0, 3.0], [-1.0, 2.0]])
    c_true = np.array([2.5, -1.5])
    v = B @ c_true
    got = _result(lambda: linmaps.coordinates(B, v), f"{c_true}", "a vector of the plane spanned by 2 vectors of ℝ⁵")
    _array(got, "coordinates in a basis of a plane of ℝ⁵", (2,))
    assert np.allclose(got, c_true, rtol=0, atol=1e-10), (
        f"expected {_show(c_true)}, got {_show(got)} (solve BᵀB c = Bᵀv: B is not square)")


def test_coordinates_accept_a_large_vector_of_the_span(linmaps):
    B = np.array([[0.3, 1.7], [-1.1, 0.45], [2.9, 0.6]])
    v = B @ np.array([4.1e9, -7.3e9])       # rounding leaves ‖B c - v‖ around 1e-6
    expected = np.linalg.lstsq(B, v, rcond=None)[0]
    got = _result(lambda: linmaps.coordinates(B, v), f"{expected}", "a vector of the span of norm about 1.6e10",
                  "the check is relative: ‖B c - v‖ ≤ tol · max(1, ‖v‖)")
    assert np.allclose(got, expected, rtol=1e-9, atol=0), f"expected {expected}, got {got!r}"


def test_coordinates_docstring_examples(linmaps):
    for B, v, expected in [([[1, 1], [1, -1]], [3, 1], [2.0, 1.0]), ([[1], [2], [2]], [2, 4, 4], [2.0])]:
        got = _result(lambda B=B, v=v: linmaps.coordinates(B, v), f"{expected}", f"coordinates({B}, {v})")
        assert np.allclose(np.asarray(got, dtype=float), expected), (
            f"expected {expected} for coordinates({B}, {v}), got {got!r}")


@pytest.mark.parametrize("B, v, why", [
    ([[1.0, 0.0], [2.0, 1.0], [0.0, -1.0]], [1.0, 2.0, 1.0], "v is not in the plane spanned by the columns of B"),
    ([[1.0], [-2.0], [3.0]], [0.0, 0.0, 1e-6], "v is not on the line spanned by B, even if it is short"),
    ([[1.0, -3.0], [2.0, -6.0], [-1.0, 3.0]], [1.0, 2.0, -1.0], "the columns of B are dependent: not a basis"),
    ([[1.0, 0.0], [0.0, 1.0]], [1.0, 2.0, 3.0], "v has 3 coordinates, B has 2 rows"),
    ([[1.0, 0.0], [0.0, 1.0]], [[1.0], [2.0]], "v must be a 1-D vector"),
    ([1.0, 2.0], [1.0, 2.0], "B must be a 2-D matrix"),
])
def test_coordinates_rejects_invalid_inputs(linmaps, B, v, why):
    _expect_value_error(lambda: linmaps.coordinates(B, v), f"coordinates({B}, {v})", why)


def test_coordinates_rejects_dependent_columns_even_for_a_vector_of_their_span(linmaps):
    B = [[0.1, 0.3], [0.7, 2.1], [0.2, 0.6]]   # column 2 = 3 × column 1 (rounding hides it from np.linalg.solve)
    _expect_value_error(lambda: linmaps.coordinates(B, [0.1, 0.7, 0.2]), "coordinates(B, column 1 of B)",
                        "the columns of B are dependent, so they are not a basis and the coordinates are not unique: "
                        "check them with is_independent before solving")


def test_coordinates_does_not_modify_its_inputs(linmaps):
    B = np.array([[2.0, 1.0], [1.0, -1.0], [0.0, 3.0]])
    v = B @ np.array([1.5, -2.0])
    B0, v0 = B.copy(), v.copy()
    _result(lambda: linmaps.coordinates(B, v), "a vector", "arrays")
    assert np.array_equal(B, B0) and np.array_equal(v, v0), (
        "expected coordinates to leave B and v unchanged (work on copies)")


# ---------------------------------------------------------------- change_of_basis
def _expected_change(A, S, T=None):
    A, S = np.array(A, dtype=float), np.array(S, dtype=float)
    T = S if T is None else np.array(T, dtype=float)
    return np.linalg.inv(T) @ A @ S


CHANGES = {   # (A, S, T): none is an example of the fiche or of an exercise
    "3x3-same-basis": (RNG.integers(-5, 6, size=(3, 3)), [[1, 2, 0], [0, 1, -1], [1, 0, 1]], None),
    "2x3-two-bases": ([[2, -1, 0], [1, 3, 4]], [[1, 0, 1], [1, 1, 0], [0, 1, 1]], [[2, 1], [1, 1]]),
    "4x2-two-bases": (RNG.integers(-4, 5, size=(4, 2)), [[3, 1], [1, 1]], [[1, 0, 0, 1], [0, 2, 0, 0],
                                                                         [1, 0, 1, 0], [0, 1, 0, 1]]),
    "floats": (RNG.normal(size=(3, 3)), RNG.normal(size=(3, 3)), None),
}


@pytest.mark.parametrize("name", list(CHANGES))
def test_change_of_basis_matches_numpy(linmaps, name):
    A, S, T = CHANGES[name]
    expected = _expected_change(A, S, T)
    got = _result(lambda: linmaps.change_of_basis(A, S, T) if T is not None else linmaps.change_of_basis(A, S),
                  f"the {expected.shape} matrix T⁻¹AS", name)
    _array(got, f"change_of_basis for {name}", expected.shape)
    assert np.allclose(got, expected, rtol=1e-9, atol=1e-9), (
        f"expected T⁻¹AS = {_show(expected)} for {name}, got {_show(got)} (S on the right, the inverse of T on the "
        f"left; T = S when it is omitted)")


def test_change_of_basis_docstring_example(linmaps):
    got = _result(lambda: linmaps.change_of_basis([[1, 2], [3, 4]], [[1, 1], [0, 1]]), "[[-2, -4], [3, 7]]",
                  "the docstring")
    assert np.allclose(np.asarray(got, dtype=float), [[-2, -4], [3, 7]]), (
        f"expected [[-2., -4.], [3., 7.]] for change_of_basis([[1, 2], [3, 4]], [[1, 1], [0, 1]]), got {got!r}")


def test_change_of_basis_with_t_equal_to_s_is_the_same(linmaps):
    A, S, _ = CHANGES["3x3-same-basis"]
    got_default = _result(lambda: linmaps.change_of_basis(A, S), "S⁻¹AS", "T omitted")
    got_explicit = _result(lambda: linmaps.change_of_basis(A, S, S), "S⁻¹AS", "T = S given")
    assert np.allclose(got_default, got_explicit, rtol=1e-12, atol=1e-12), (
        f"expected the same matrix with T omitted and with T = S, got {_show(got_default)} and {_show(got_explicit)}")


@pytest.mark.parametrize("A, S, T, why", [
    ([[2.0, -1.0], [4.0, 3.0]], [[3.0, 6.0], [1.0, 2.0]], None, "S is singular: its columns are not a basis"),
    ([[2.0, -1.0], [4.0, 3.0]], [[3.0, 6.0], [1.0, 2.0]], [[1.0, 0.0], [0.0, 1.0]],
     "S is singular, even when T is given and invertible"),
    ([[2.0, -1.0], [4.0, 3.0]], [[1.0, 0.0], [0.0, 1.0]], [[2.0, -1.0], [-4.0, 2.0]], "T is singular"),
    ([[1.0, 2.0, 0.0], [3.0, 4.0, 1.0]], [[1.0, 0.0], [0.0, 1.0]], None,
     "S must be (3, 3) for A of shape (2, 3)"),
    ([[1.0, 2.0, 0.0], [3.0, 4.0, 1.0]], np.eye(3), np.eye(3), "T must be (2, 2) for A of shape (2, 3)"),
    ([1.0, 2.0], [[1.0]], None, "A must be a 2-D matrix"),
])
def test_change_of_basis_rejects_invalid_inputs(linmaps, A, S, T, why):
    call = (lambda: linmaps.change_of_basis(A, S)) if T is None else (lambda: linmaps.change_of_basis(A, S, T))
    _expect_value_error(call, f"change_of_basis({A}, {S}{', ' + str(T) if T is not None else ''})", why)


def test_change_of_basis_does_not_modify_its_inputs(linmaps):
    A, S, T = (np.array(M, dtype=float) for M in CHANGES["2x3-two-bases"])
    A0, S0, T0 = A.copy(), S.copy(), T.copy()
    _result(lambda: linmaps.change_of_basis(A, S, T), "a matrix", "arrays")
    assert np.array_equal(A, A0) and np.array_equal(S, S0) and np.array_equal(T, T0), (
        "expected change_of_basis to leave A, S and T unchanged (work on copies)")
