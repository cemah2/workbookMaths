"""Tests of mymath.matrices (chapter M09a): product, transpose, reduced row echelon form, rank, solve, inverse.

Oracles: NumPy (``@``, ``.T``, ``np.linalg.solve``, ``np.linalg.inv``, ``np.linalg.matrix_rank``) and SymPy
(``Matrix.rref``, exact on integer matrices), plus properties (A A⁻¹ = I, A x = b). They describe the expected
behaviour without showing the solution.

    pytest tests/test_m09a_matrices.py              # your code
    pytest tests/test_m09a_matrices.py --impl=ref   # the reference
"""

import ast
import inspect

import numpy as np
import pytest
import sympy


@pytest.fixture
def matrices(mymath_module):
    return mymath_module("matrices")


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
    except ValueError:
        return
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
FORBIDDEN_ATTRIBUTES = {"dot", "matmul", "einsum", "T", "transpose", "linalg", "inner", "tensordot", "vdot",
                        "swapaxes", "moveaxis"}


def test_matrices_uses_no_ready_made_product(matrices):
    """matrices.py computes products, transposes and eliminations itself: no @, .T, np.dot, np.linalg, SymPy."""
    try:
        tree = ast.parse(inspect.getsource(matrices))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.MatMult):
            found.add("the operator @")
        elif isinstance(node, ast.AugAssign) and isinstance(node.op, ast.MatMult):
            found.add("the operator @=")
        elif isinstance(node, ast.Attribute) and node.attr in FORBIDDEN_ATTRIBUTES:
            found.add(f".{node.attr}")
        elif isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names if alias.name.split(".")[0] in ("sympy", "scipy")
                         or alias.name.startswith("numpy.linalg"))
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.split(".")[0] in ("sympy", "scipy") or node.module.startswith("numpy.linalg"):
                found.add(node.module)
            elif node.module == "numpy":
                found.update(alias.name for alias in node.names if alias.name in FORBIDDEN_ATTRIBUTES)
    assert not found, (f"expected matrices.py to compute its products and eliminations itself (element-wise "
                       f"operations, np.sum, np.eye, np.hstack are allowed), found {sorted(found)}")


# ---------------------------------------------------------------- data
RNG = np.random.default_rng(909)
PRODUCTS = {   # (A, B): none is an example of the fiche, of 0B or an exercise of the chapter
    "2x3-3x4": (RNG.integers(-5, 6, size=(2, 3)), RNG.integers(-5, 6, size=(3, 4))),
    "row-column": ([[2.5, -1.0, 0.5, 3.0, -2.0]], [[1.0], [4.0], [-2.0], [0.5], [1.5]]),
    "column-row": ([[3.0], [-1.0], [2.0], [0.0]], [[1.5, -2.0, 4.0]]),
    "square": (RNG.integers(-9, 10, size=(4, 4)), RNG.integers(-9, 10, size=(4, 4))),
    "one-by-one": ([[-3.5]], [[2.0]]),
    "floats": (RNG.normal(size=(5, 2)), RNG.normal(size=(2, 6))),
}


@pytest.mark.parametrize("name", list(PRODUCTS))
def test_matmul_matches_numpy(matrices, name):
    A, B = (np.array(M, dtype=float) for M in PRODUCTS[name])
    expected = A @ B
    got = _result(lambda: matrices.matmul(A.copy(), B.copy()), f"the {expected.shape} product", name)
    _array(got, f"matmul for {name}", expected.shape)
    assert np.allclose(got, expected, rtol=1e-12, atol=1e-12), (
        f"expected {_show(expected)} for {name}, got {_show(got)} ((AB)[i, j] is the dot product of row i of A and "
        f"column j of B)")


def test_matmul_docstring_examples(matrices):
    for A, B, expected in [([[1, 2], [3, 4]], [[5], [6]], [[17.0], [39.0]]), ([[1, 2, 3]], [[1], [0], [-1]], [[-2.0]])]:
        got = _result(lambda A=A, B=B: matrices.matmul(A, B), f"{expected}", f"matmul({A}, {B})")
        assert np.allclose(np.asarray(got, dtype=float), expected), f"expected {expected} for matmul({A}, {B}), got {got!r}"


def test_matmul_accepts_lists_and_does_not_modify_its_inputs(matrices):
    A, B = np.array([[1.5, -2.0], [0.0, 3.0], [4.0, 1.0]]), np.array([[2.0, 0.5, -1.0], [1.0, 1.0, 2.5]])
    A0, B0 = A.copy(), B.copy()
    got = _result(lambda: matrices.matmul(A.tolist(), B.tolist()), "the (3, 3) product", "lists of rows")
    assert np.allclose(got, A0 @ B0), f"expected {_show(A0 @ B0)} for lists of rows, got {_show(got)}"
    _result(lambda: matrices.matmul(A, B), "the (3, 3) product", "arrays")
    assert np.array_equal(A, A0) and np.array_equal(B, B0), (
        "expected matmul to leave its inputs unchanged (work on copies), but A or B was modified")


@pytest.mark.parametrize("A, B, why", [
    ([[1.0, 2.0]], [[1.0, 2.0]], "a (1, 2) matrix times a (1, 2) matrix: 2 columns but 1 row"),
    (np.ones((3, 2)), np.ones((3, 2)), "(3, 2) times (3, 2): the inner dimensions differ"),
    ([1.0, 2.0], [[1.0], [2.0]], "A is a 1-D vector, not a matrix"),
    ([[1.0, -1.0], [2.0, 0.5]], [3.0, 4.0], "B is a 1-D vector, not a matrix (even with 2 entries for 2 columns)"),
], ids=["1x2-1x2", "3x2-3x2", "A-1d", "B-1d"])
def test_matmul_rejects_incompatible_shapes(matrices, A, B, why):
    _expect_value_error(lambda: matrices.matmul(A, B), f"matmul of shapes {np.shape(A)} and {np.shape(B)}", why)


# ---------------------------------------------------------------- transpose
TRANSPOSES = {
    "2x4": RNG.integers(-9, 10, size=(2, 4)),
    "row": [[0.5, -1.5, 2.0, 7.0]],
    "column": [[3.0], [-4.0], [1.25]],
    "square": RNG.normal(size=(3, 3)),
    "one-by-one": [[6.0]],
}


@pytest.mark.parametrize("name", list(TRANSPOSES))
def test_transpose_matches_numpy(matrices, name):
    A = np.array(TRANSPOSES[name], dtype=float)
    got = _result(lambda: matrices.transpose(A.copy()), f"the {A.T.shape} transpose", name)
    _array(got, f"transpose for {name}", A.T.shape)
    assert np.array_equal(got, A.T), f"expected {_show(A.T)} for {name}, got {_show(got)} (Aᵀ[j, i] = A[i, j])"


def test_transpose_docstring_example(matrices):
    got = _result(lambda: matrices.transpose([[1, 2, 3], [4, 5, 6]]), "[[1, 4], [2, 5], [3, 6]]", "the docstring")
    assert np.array_equal(np.asarray(got, dtype=float), [[1, 4], [2, 5], [3, 6]]), (
        f"expected [[1., 4.], [2., 5.], [3., 6.]] for transpose([[1, 2, 3], [4, 5, 6]]), got {got!r}")


def test_transpose_returns_a_new_array(matrices):
    A = np.array([[1.0, 2.0], [3.0, 4.0]])
    got = _result(lambda: matrices.transpose(A), "a new (2, 2) array", "a square matrix")
    got[0, 1] = 99.0
    assert A[1, 0] == 3.0 and A[0, 1] == 2.0, (
        "expected transpose to return a new array (a copy): changing the result changed the matrix received")


def test_transpose_rejects_a_vector(matrices):
    _expect_value_error(lambda: matrices.transpose([1.0, 2.0, 3.0]), "transpose([1.0, 2.0, 3.0])",
                        "a 1-D vector is not a matrix")


# ---------------------------------------------------------------- rref
RREF_CASES = {   # integer matrices: SymPy's rref is exact
    "invertible-3x3": [[2, -1, 3], [1, 4, -2], [5, 2, 1]],
    "zero-pivot-first": [[0, 2, 4], [3, 1, -1], [6, 4, 2]],
    "wide-rank-2": [[1, 3, -2, 5, 0], [2, 6, -1, 7, 3], [3, 9, -3, 12, 3]],
    "tall-4x2": [[1, 2], [3, 5], [-2, 1], [4, 0]],
    "zero-column": [[0, 1, 2], [0, 3, 7], [0, -1, 4]],
    "zero-matrix": [[0, 0, 0], [0, 0, 0]],
    "one-row": [[0, 0, 5, -10]],
    "augmented-no-solution": [[1, 1, 2, 3], [2, 1, 3, 5], [3, 2, 5, 9]],
}


def _sympy_rref(A):
    R, pivots = sympy.Matrix(A).rref()
    return np.array(R.tolist(), dtype=float), tuple(int(p) for p in pivots)


@pytest.mark.parametrize("name", list(RREF_CASES))
def test_rref_matches_sympy(matrices, name):
    A = RREF_CASES[name]
    expected_R, expected_pivots = _sympy_rref(A)
    got = _result(lambda: matrices.rref([row[:] for row in A]), "a tuple (R, pivots)", name)
    assert isinstance(got, tuple) and len(got) == 2, f"expected a tuple (R, pivots) for {name}, got {got!r}"
    R, pivots = got
    _array(R, f"R for {name}", expected_R.shape)
    assert np.allclose(R, expected_R, atol=1e-9), (
        f"expected R = {_show(expected_R)} for {name}, got {_show(R)} (each pivot equals 1 and is the only non-zero "
        f"entry of its column; a column without a pivot is skipped)")
    assert tuple(pivots) == expected_pivots, f"expected the pivot columns {expected_pivots} for {name}, got {pivots!r}"


def test_rref_uses_partial_pivoting(matrices):
    # a tiny first pivot (above tol): elimination without row swaps loses digits, by 4e-10 to 4e-8 here
    for eps in (3e-9, 1e-8, 3e-8):
        for c in ((3.0, 5.0), (1.1, 2.3)):
            A = [[eps, 1.0, c[0]], [1.0, 2.0, c[1]]]
            x = np.linalg.solve(np.array(A)[:, :2], np.array(A)[:, 2])
            expected = np.array([[1.0, 0.0, x[0]], [0.0, 1.0, x[1]]])
            got = _result(lambda A=A: matrices.rref([row[:] for row in A]), "a tuple (R, pivots)", f"{A}")
            R = got[0]
            _array(R, f"R for {A}", expected.shape)
            assert np.allclose(R, expected, rtol=0, atol=1e-10), (
                f"expected R = {_show(expected)} for {A} within 1e-10, got entries off by "
                f"{np.max(np.abs(np.asarray(R, dtype=float) - expected)):.1e}: in each column, take as pivot the row (from "
                f"the current row down) whose entry has the largest absolute value, and swap (partial pivoting)")


def test_rref_pivots_are_a_tuple_of_python_ints(matrices):
    got = _result(lambda: matrices.rref([[3, 6, 0], [1, 2, 4]]), "a tuple (R, pivots)", "[[3, 6, 0], [1, 2, 4]]")
    pivots = got[1]
    assert isinstance(pivots, tuple) and all(type(p) is int for p in pivots), (
        f"expected pivots to be a tuple of Python ints, such as (0, 2), got {pivots!r}")


def test_rref_docstring_example(matrices):
    got = _result(lambda: matrices.rref([[1, 2, 3], [2, 4, 7]]), "([[1, 2, 0], [0, 0, 1]], (0, 2))", "the docstring")
    R, pivots = got
    assert np.allclose(R, [[1, 2, 0], [0, 0, 1]]) and tuple(pivots) == (0, 2), (
        f"expected R = [[1, 2, 0], [0, 0, 1]] and pivots (0, 2) for rref([[1, 2, 3], [2, 4, 7]]), got {got!r}")


def test_rref_sets_tiny_entries_to_zero(matrices):
    A = [[1.0, 2.0, 1.0], [3.0, 6.0 + 1e-13, 2.0]]   # the second column is a multiple of the first, up to 1e-13
    got = _result(lambda: matrices.rref(A), "a tuple (R, pivots)", "a matrix with an entry of 1e-13 after elimination")
    R, pivots = got
    assert tuple(pivots) == (0, 2), (
        f"expected the pivot columns (0, 2): after elimination, 1e-13 is at most tol = 1e-10 and counts as zero, got "
        f"{pivots!r}")
    assert np.all((np.abs(R) > 1e-10) | (R == 0)), (
        f"expected the entries at most tol in absolute value to be set to 0, got {_show(R)}")


def test_rref_does_not_modify_its_input(matrices):
    A = np.array([[0.0, 2.0, 4.0], [3.0, 1.0, -1.0], [6.0, 4.0, 2.0]])
    A0 = A.copy()
    _result(lambda: matrices.rref(A), "a tuple (R, pivots)", "an array")
    assert np.array_equal(A, A0), "expected rref to leave its input unchanged (work on a copy), but it was modified"


def test_rref_rejects_a_vector(matrices):
    _expect_value_error(lambda: matrices.rref([1.0, 2.0]), "rref([1.0, 2.0])", "a 1-D vector is not a matrix")


# ---------------------------------------------------------------- rank
def _low_rank(seed, n, m, r):
    rng = np.random.default_rng(seed)
    return rng.integers(-4, 5, size=(n, r)).astype(float) @ rng.integers(-4, 5, size=(r, m)).astype(float)


RANK_CASES = {
    "rank-1-4x3": _low_rank(1, 4, 3, 1),
    "rank-2-5x5": _low_rank(2, 5, 5, 2),
    "rank-3-3x6": _low_rank(3, 3, 6, 3),
    "full-6x4": np.random.default_rng(4).normal(size=(6, 4)),
    "zero-2x3": np.zeros((2, 3)),
    "identity-5": np.eye(5),
}


@pytest.mark.parametrize("name", list(RANK_CASES))
def test_rank_matches_numpy(matrices, name):
    A = RANK_CASES[name]
    expected = int(np.linalg.matrix_rank(A))
    got = _result(lambda: matrices.rank(A.copy()), f"{expected}", name)
    assert type(got) is int, f"expected the rank to be a Python int (int(...)), got {type(got).__name__}"
    assert got == expected, f"expected the rank {expected} for {name}, got {got} (the number of pivots of rref)"


def test_rank_docstring_examples(matrices):
    for A, expected in [([[1, 2], [2, 4]], 1), ([[1, 0, 1], [0, 1, 1], [1, 1, 2]], 2)]:
        got = _result(lambda A=A: matrices.rank(A), f"{expected}", f"rank({A})")
        assert got == expected, f"expected {expected} for rank({A}), got {got!r}"


def test_rank_rejects_a_vector(matrices):
    _expect_value_error(lambda: matrices.rank([3.0, 1.0]), "rank([3.0, 1.0])", "a 1-D vector is not a matrix")


# ---------------------------------------------------------------- solve
def _system(seed, n):
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(n, n)) + n * np.eye(n) * rng.choice([-1, 1], size=n)
    return A, rng.normal(size=n)


SYSTEMS = {
    "3x3-integers": (np.array([[4.0, -2.0, 1.0], [3.0, 6.0, -4.0], [2.0, 1.0, 8.0]]), np.array([12.0, -25.0, 32.0])),
    "zero-on-diagonal": (np.array([[0.0, 3.0, -1.0], [2.0, 0.0, 4.0], [1.0, -1.0, 0.0]]), np.array([5.0, 6.0, -2.0])),
    "random-6x6": _system(61, 6),
    "random-25x25": _system(62, 25),
    "one-by-one": (np.array([[-4.0]]), np.array([10.0])),
}


@pytest.mark.parametrize("name", list(SYSTEMS))
def test_solve_matches_numpy(matrices, name):
    A, b = SYSTEMS[name]
    expected = np.linalg.solve(A, b)
    got = _result(lambda: matrices.solve(A.copy(), b.copy()), f"x = {_show(expected)}", name)
    _array(got, f"solve for {name}", expected.shape)
    assert np.allclose(got, expected, rtol=1e-9, atol=1e-9), (
        f"expected x = {_show(expected)} for {name}, got {_show(got)} (A x should give b: elimination below each pivot, "
        f"then back substitution from the last row)")


def test_solve_docstring_examples(matrices):
    for A, b, expected in [([[2, 1], [1, 3]], [3, 5], [0.8, 1.4]), ([[0, 1], [1, 0]], [2, 3], [3.0, 2.0])]:
        got = _result(lambda A=A, b=b: matrices.solve(A, b), f"{expected}", f"solve({A}, {b})")
        assert np.allclose(np.asarray(got, dtype=float), expected), f"expected {expected} for solve({A}, {b}), got {got!r}"


def test_solve_uses_partial_pivoting(matrices):
    A, b = [[1e-17, 1.0], [1.0, 1.0]], [1.0, 2.0]
    got = _result(lambda: matrices.solve(A, b), "x ≈ [1, 1]", "A = [[1e-17, 1], [1, 1]], b = [1, 2]",
                  hint="the matrix is not singular: swap rows before choosing the pivot (partial pivoting)")
    assert np.allclose(got, [1.0, 1.0], atol=1e-9), (
        f"expected x ≈ [1, 1] for A = [[1e-17, 1], [1, 1]] and b = [1, 2], got {_show(got)}: the tiny pivot 1e-17 must "
        f"not be used, swap with the row whose entry has the largest absolute value (partial pivoting), and swap whole "
        f"rows of the augmented matrix [A | b], b included")


def test_solve_singularity_threshold_is_relative(matrices):
    A, b = SYSTEMS["3x3-integers"]
    expected = np.linalg.solve(A, b)
    got = _result(lambda: matrices.solve(1e-13 * A, 1e-13 * b), f"x = {_show(expected)}",
                  "the 3x3 system with A and b multiplied by 1e-13",
                  hint="the singularity test is relative: a pivot at most 1e-12 times the largest absolute value of A")
    _array(got, "solve for the system multiplied by 1e-13", expected.shape)
    assert np.allclose(got, expected, rtol=1e-9, atol=1e-9), (
        f"expected x = {_show(expected)} for A and b multiplied by 1e-13 (the same solution), got {_show(got)}: a pivot "
        f"is too small when it is at most 1e-12 times the largest absolute value of A, not 1e-12 itself")


def test_solve_does_not_modify_its_inputs(matrices):
    A, b = SYSTEMS["zero-on-diagonal"]
    A0, b0 = A.copy(), b.copy()
    _result(lambda: matrices.solve(A, b), "a solution", "a system that needs a row swap")
    assert np.array_equal(A, A0) and np.array_equal(b, b0), (
        "expected solve to leave A and b unchanged (work on the augmented copy [A | b]), but one was modified")


@pytest.mark.parametrize("A, b, why", [
    ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], [1.0, 2.0], "A is (2, 3), not square"),
    ([[2.0, 1.0], [1.0, 3.0]], [1.0, 2.0, 3.0], "b has 3 entries for a (2, 2) matrix"),
    ([[1.0, -2.0, 3.0], [2.0, -4.0, 6.0], [0.0, 1.0, 1.0]], [1.0, 2.0, 3.0], "A is singular (row 2 = 2 × row 1)"),
    ([[3.0, 1.0, 4.0], [1.0, 5.0, 6.0], [4.0, 6.0, 10.0]], [1.0, 1.0, 1.0], "A is singular (column 3 = column 1 + column 2)"),
], ids=["not-square", "b-length", "singular-rows", "singular-columns"])
def test_solve_rejects_invalid_systems(matrices, A, b, why):
    _expect_value_error(lambda: matrices.solve(A, b), f"solve({A}, {b})", why)


# ---------------------------------------------------------------- inverse
INVERSES = {
    "2x2": np.array([[4.0, 7.0], [2.0, 6.0]]),
    "3x3-needs-swap": np.array([[0.0, 1.0, 2.0], [1.0, 0.0, 3.0], [4.0, -3.0, 8.0]]),
    "random-5x5": _system(71, 5)[0],
    "diagonal": np.diag([2.0, -0.5, 4.0]),
}


@pytest.mark.parametrize("name", list(INVERSES))
def test_inverse_matches_numpy(matrices, name):
    A = INVERSES[name]
    expected = np.linalg.inv(A)
    got = _result(lambda: matrices.inverse(A.copy()), f"A⁻¹ = {_show(expected)}", name)
    _array(got, f"inverse for {name}", A.shape)
    assert np.allclose(got, expected, rtol=1e-9, atol=1e-9), (
        f"expected A⁻¹ = {_show(expected)} for {name}, got {_show(got)} (reduce [A | I] and keep its right half)")
    assert np.allclose(A @ got, np.eye(A.shape[0]), atol=1e-9), f"expected A A⁻¹ = I for {name}"


def test_inverse_docstring_example(matrices):
    got = _result(lambda: matrices.inverse([[2, 1], [1, 1]]), "[[1, -1], [-1, 2]]", "the docstring")
    assert np.allclose(np.asarray(got, dtype=float), [[1, -1], [-1, 2]]), (
        f"expected [[1., -1.], [-1., 2.]] for inverse([[2, 1], [1, 1]]), got {got!r}")


def test_inverse_does_not_modify_its_input(matrices):
    A = INVERSES["3x3-needs-swap"].copy()
    A0 = A.copy()
    _result(lambda: matrices.inverse(A), "an inverse", "a matrix that needs a row swap")
    assert np.array_equal(A, A0), "expected inverse to leave its input unchanged, but it was modified"


@pytest.mark.parametrize("A, why", [
    ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], "A is (2, 3), not square"),
    ([[3.0, -6.0], [-1.0, 2.0]], "A is singular (column 2 = −2 × column 1)"),
    ([[1.0, 2.0, 0.0], [0.0, 1.0, 1.0], [1.0, 3.0, 1.0]], "A is singular (row 3 = row 1 + row 2)"),
], ids=["not-square", "singular-2x2", "singular-3x3"])
def test_inverse_rejects_singular_or_non_square(matrices, A, why):
    _expect_value_error(lambda: matrices.inverse(A), f"inverse({A})", why)
