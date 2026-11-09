"""Tests of mymath.eigen (chapter M12c): determinant, power iteration, Rayleigh quotient, Cholesky, positive
definiteness, square root and whitening matrix.

Oracles: NumPy (``np.linalg.det``, ``eigh``, ``eig``, ``cholesky``), SciPy (``scipy.linalg.sqrtm``), SymPy (exact
determinants of integer matrices) and properties (B B = A, W Σ Wᵀ = I, λ_min ≤ quotient ≤ λ_max, a unit vector that A
only stretches). They describe the expected behaviour without showing the solution.

    pytest tests/test_m12c_eigen.py              # your code
    pytest tests/test_m12c_eigen.py --impl=ref   # the reference
"""

import ast
import inspect
import math

import numpy as np
import pytest
import scipy.linalg
import sympy


@pytest.fixture
def eigen(mymath_module):
    return mymath_module("eigen")


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
                    + (hint or "catch it and raise ValueError, as the docstring asks"))
    except Exception as exc:  # noqa: BLE001 - any other error is reported, with what was expected first
        pytest.fail(f"expected {what} to raise ValueError ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise ValueError ({why}), but it returned {result!r}")


def _array(got, what, shape):
    assert isinstance(got, np.ndarray), (f"expected {what} to be a numpy.ndarray of floats (np.array(...)), got "
                                         f"{type(got).__module__}.{type(got).__name__}")
    assert got.shape == shape, f"expected {what} to have the shape {shape}, got {got.shape}"
    assert np.issubdtype(got.dtype, np.floating), f"expected {what} to hold floats, got the dtype {got.dtype}"


def _float(got, what):
    assert type(got) is float, (f"expected {what} to be a Python float (float(...)), got "
                                f"{type(got).__module__}.{type(got).__name__}")


def _show(M):
    return np.array2string(np.asarray(M, dtype=float), precision=4, suppress_small=True).replace("\n", "")


# ---------------------------------------------------------------- no ready-made tool
FORBIDDEN = {"det", "slogdet", "eig", "eigvals", "cholesky", "inv", "pinv", "sqrtm"}
SPECTRAL = {"eigh", "eigvalsh"}                       # the spectral theorem: allowed in two functions only
SPECTRAL_ALLOWED = {"sqrtm_psd", "whitening_matrix"}
ADVICE = {".det": "eliminate below each pivot and multiply the diagonal", ".slogdet": "eliminate, as for det",
          ".eig": "iterate x ← A x / ‖A x‖", ".eigvals": "iterate x ← A x / ‖A x‖",
          ".cholesky": "fill L column by column with the two formulas of the docstring",
          ".inv": "solve a system with np.linalg.solve instead of inverting", ".pinv": "solve a system instead",
          ".sqrtm": "use the spectral theorem: Q diag(√λ) Qᵀ",
          ".eigh": "np.linalg.eigh is allowed directly inside sqrtm_psd and whitening_matrix only (not in a helper, "
                   "nor elsewhere: is_positive_definite tries cholesky)",
          ".eigvalsh": "the spectral tools are allowed in sqrtm_psd and whitening_matrix only"}


def test_eigen_uses_no_ready_made_tool(eigen):
    """eigen.py computes by itself: no np.linalg.det, eig, cholesky, inv, SciPy or SymPy; eigh in two functions only."""
    try:
        tree = ast.parse(inspect.getsource(eigen))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found, places = set(), set()
    aliases = {"linalg"}                     # names bound to numpy.linalg: np.linalg.x, or LA.x after an import
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "numpy":
            aliases.update(a.asname or a.name for a in node.names if a.name == "linalg")
        elif isinstance(node, ast.Import):
            aliases.update(a.asname for a in node.names if a.name == "numpy.linalg" and a.asname)

    def linalg_value(node):
        return ((isinstance(node, ast.Attribute) and node.attr == "linalg")
                or (isinstance(node, ast.Name) and node.id in aliases))

    def visit(node, function):
        if isinstance(node, ast.FunctionDef):
            function = node.name
        if isinstance(node, ast.Attribute):
            if node.attr in FORBIDDEN and linalg_value(node.value):
                found.add(f".{node.attr}")
            elif node.attr in SPECTRAL and function not in SPECTRAL_ALLOWED:
                found.add(f".{node.attr}")
                places.add(f"{node.attr} in {function or 'the module body'}")
        elif isinstance(node, ast.Import):
            found.update(a.name for a in node.names if a.name.split(".")[0] in ("scipy", "sympy", "sklearn"))
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.split(".")[0] in ("scipy", "sympy", "sklearn"):
                found.add(node.module)
            elif node.module.startswith("numpy"):
                found.update(f".{a.name}" for a in node.names if a.name in FORBIDDEN | SPECTRAL)
        for child in ast.iter_child_nodes(node):
            visit(child, function)

    visit(tree, None)
    hints = "; ".join(sorted({ADVICE.get(name, "use NumPy's elementary tools") for name in found}
                             | ({f"found {', '.join(sorted(places))}"} if places else set())))
    assert not found, (f"expected eigen.py to use @, .T, np.linalg.norm and np.linalg.solve (and np.linalg.eigh in "
                       f"sqrtm_psd and whitening_matrix only), found {sorted(found)}: {hints}")


# ---------------------------------------------------------------- data
RNG = np.random.default_rng(1232)


def _spd(n, rng=RNG, shift=0.5):
    """A random symmetric positive definite (n, n) matrix."""
    X = rng.normal(size=(n + 3, n))
    return X.T @ X / (n + 3) + shift * np.eye(n)


SQUARES = {   # none is an example of the fiche, of a docstring or of an exercise
    "one-by-one": np.array([[-7.5]]),
    "integers-3x3": np.array([[2.0, -3.0, 1.0], [4.0, 0.0, -2.0], [1.0, 5.0, 3.0]]),
    "zero-corner-3x3": np.array([[0.0, 2.0, -1.0], [3.0, 1.0, 4.0], [-2.0, 5.0, 0.0]]),
    "random-5x5": RNG.normal(size=(5, 5)),
    "random-8x8": RNG.normal(size=(8, 8)),
    "large-entries-4x4": 1e6 * RNG.normal(size=(4, 4)),
    "permutation-4x4": np.eye(4)[[2, 0, 3, 1]],
}


# ---------------------------------------------------------------- det
@pytest.mark.parametrize("name", list(SQUARES))
def test_det_matches_numpy(eigen, name):
    A = SQUARES[name]
    expected = float(np.linalg.det(A))
    got = _result(lambda: eigen.det(A.copy()), f"the determinant {expected:.6g}", name)
    _float(got, f"det for {name}")
    scale = float(np.prod(np.maximum(np.linalg.norm(A, axis=1), 1e-300)))     # Hadamard's bound on |det A|
    assert abs(got - expected) <= 1e-10 * scale, (
        f"expected det = {expected:.10g} for {name}, got {got:.10g} (each row swap changes the sign, the "
        f"determinant of the triangular matrix is the product of its diagonal)")


@pytest.mark.parametrize("rows", [
    [[3, 1, -2], [0, 4, 5], [2, -1, 1]],
    [[1, 2, 0, -1], [3, -1, 2, 0], [0, 4, 1, 2], [2, 0, -3, 1]],
    [[6, -2, 0, 1, 3], [1, 0, 4, -1, 2], [0, 3, -2, 5, 1], [-4, 1, 1, 0, 2], [2, 2, -1, 3, 0]],
])
def test_det_matches_sympy_on_integer_matrices(eigen, rows):
    expected = int(sympy.Matrix(rows).det())
    got = _result(lambda: eigen.det(rows), f"the integer {expected}", f"det({rows})")
    assert abs(got - expected) <= 1e-9 * max(1, abs(expected)), (
        f"expected det({rows}) = {expected} (SymPy, exact), got {got!r}")


def test_det_docstring_examples(eigen):
    for rows, expected in [([[2, 1], [1, 3]], 5.0), ([[0, 1], [1, 0]], -1.0), ([[1, 2], [2, 4]], 0.0)]:
        got = _result(lambda: eigen.det(rows), repr(expected), f"det({rows})")
        assert got == pytest.approx(expected, abs=1e-12), f"expected det({rows}) = {expected}, got {got!r}"


def test_det_uses_partial_pivoting(eigen):
    A = np.array([[1e-20, 1.0, 1.0], [1.0, 1.0, 0.0], [1.0, 0.0, 1.0]])     # det = 1e-20 - 2, about -2
    got = _result(lambda: eigen.det(A), "about -2", "a tiny pivot 1e-20 in the corner")
    assert got == pytest.approx(-2.0, rel=1e-9), (
        f"expected det = -2.0 (to 1e-9) for [[1e-20, 1, 1], [1, 1, 0], [1, 0, 1]], got {got!r}: in each column, swap "
        f"up the row whose entry has the LARGEST absolute value, not just a non-zero one")


@pytest.mark.parametrize("rows", [
    [[2, 4, -2], [1, 2, -1], [3, 0, 5]],            # two proportional rows
    [[0, 3, 1], [2, 1, 0], [0, 0, 0]],              # a zero row, after a row swap
    [[1, 0, 2, 0], [0, 0, 0, 0], [3, 1, 1, 1], [2, 2, 0, 5]],
])
def test_det_of_a_singular_matrix_is_exactly_zero(eigen, rows):
    got = _result(lambda: eigen.det(rows), "0.0", f"det({rows})")
    assert got == 0 and math.copysign(1.0, got) > 0, (
        f"expected exactly 0.0 for the singular matrix {rows}, got {got!r}: when a column has no non-zero pivot, "
        f"return 0.0 at once (never -0.0)")


@pytest.mark.parametrize("A, why", [
    ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], "a (2, 3) matrix is not square"),
    ([1.0, 2.0], "a 1-D vector is not a matrix"),
])
def test_det_rejects_a_non_square_matrix(eigen, A, why):
    _expect_value_error(lambda: eigen.det(A), f"det({A})", why)


def test_det_does_not_modify_its_input(eigen):
    A = SQUARES["zero-corner-3x3"].copy()
    _result(lambda: eigen.det(A), "a float", "an array")
    assert np.array_equal(A, SQUARES["zero-corner-3x3"]), "expected det to leave its input unchanged (work on a copy)"


# ---------------------------------------------------------------- power_iteration
def _dominant(A):
    """The eigenvalue of largest absolute value of A and a unit eigenvector, with the docstring's sign convention."""
    values, vectors = np.linalg.eig(np.asarray(A, dtype=float))
    k = int(np.argmax(np.abs(values)))
    v = np.real(vectors[:, k])
    v = v / np.linalg.norm(v)
    if v[int(np.argmax(np.abs(v)))] < 0:
        v = -v
    return float(np.real(values[k])), v


DOMINANT = {   # one eigenvalue strictly larger than the others in absolute value
    "spd-4x4": _spd(4),
    "negative-dominant-3x3": np.array([[-6.0, 1.0, 0.0], [1.0, 2.0, 1.0], [0.0, 1.0, -1.0]]),
    "non-symmetric-3x3": np.array([[4.0, 1.0, 2.0], [0.0, 2.0, 1.0], [1.0, 0.0, 1.0]]),
    "diagonal-5x5": np.diag([1.0, -3.0, 2.0, 0.5, 2.5]),
}


@pytest.mark.parametrize("name", list(DOMINANT))
def test_power_iteration_finds_the_dominant_eigenpair(eigen, name):
    A = DOMINANT[name]
    value, vector = _dominant(A)
    got = _result(lambda: eigen.power_iteration(A.copy()), "(eigenvalue, eigenvector, iterations)", name)
    assert isinstance(got, tuple) and len(got) == 3, f"expected a tuple of 3 objects, got {got!r}"
    got_value, got_vector, iterations = got
    _float(got_value, "the eigenvalue")
    _array(got_vector, "the eigenvector", vector.shape)
    assert type(iterations) is int, f"expected the number of iterations to be an int, got {type(iterations).__name__}"
    assert got_value == pytest.approx(value, rel=1e-8), (
        f"expected the eigenvalue {value:.10g} for {name}, got {got_value!r} (the Rayleigh quotient xᵀA x of the last "
        f"unit vector)")
    assert np.allclose(got_vector, vector, atol=1e-6), (
        f"expected the unit eigenvector {_show(vector)} for {name}, got {_show(got_vector)} (normalize at each step, "
        f"and make the entry of largest absolute value positive)")
    assert iterations < 1000, (f"expected convergence before 1000 iterations for {name}, got {iterations} (does x "
                               f"flip its sign at each step? the sign convention makes the entry of largest absolute "
                               f"value positive, at each step)")


def test_power_iteration_docstring_example(eigen):
    got = _result(lambda: eigen.power_iteration([[3, 2], [2, 0]], x0=[2, 1]), "(4.0, [0.894…, 0.447…], 1)",
                  "the docstring")
    value, vector, iterations = got
    assert value == pytest.approx(4.0, abs=1e-12), f"expected the eigenvalue 4.0, got {value!r}"
    assert np.allclose(vector, [2 / np.sqrt(5), 1 / np.sqrt(5)]), f"expected (2, 1)/√5, got {vector!r}"
    assert iterations == 1, (f"expected 1 iteration (x0 is already an eigenvector: one product A x, then the stopping "
                             f"test), got {iterations!r} (the first comparison is with x0 normalized, its sign fixed, "
                             f"not with x0 itself)")


def test_power_iteration_starts_from_ones_by_default(eigen):
    A = np.array([[2.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, -1.0]])
    expected = A @ np.ones(3)
    expected = expected / np.linalg.norm(expected)
    _, vector, iterations = _result(lambda: eigen.power_iteration(A, n_iter=1), "one step from (1, 1, 1)",
                                    "n_iter=1")
    assert iterations == 1, f"expected 1 iteration with n_iter=1, got {iterations!r}"
    assert np.allclose(vector, expected), (
        f"expected A 1 / ‖A 1‖ = {_show(expected)} after one step from the default x0 = np.ones(n), got "
        f"{_show(vector)}")


def test_power_iteration_keeps_its_sign_when_the_eigenvalue_is_negative(eigen):
    A = np.diag([-5.0, 1.0, 2.0])
    for steps in (3, 4, 25, 26):     # without the sign rule, x would flip at every step
        _, vector, _ = _result(lambda: eigen.power_iteration(A, x0=[1.0, 1.0, 1.0], n_iter=steps, tol=0.0),
                               "a vector close to e1", f"n_iter={steps}")
        assert vector[0] > 0, (
            f"expected the first entry, the one of largest absolute value, to be positive after {steps} steps, got "
            f"{_show(vector)}: after each normalization, change the sign of x if that entry is negative")


def test_power_iteration_counts_its_iterations(eigen):
    A = np.diag([2.0, 1.0])            # the error halves at each step: about 40 steps to reach 1e-12
    _, _, iterations = _result(lambda: eigen.power_iteration(A, x0=[1.0, 1.0]), "a count", "diag(2, 1)")
    assert 30 <= iterations <= 50, (
        f"expected between 30 and 50 iterations for diag(2, 1) from (1, 1) with tol = 1e-12 (the error halves at "
        f"each step), got {iterations!r}: stop as soon as ‖x_new - x‖ ≤ tol, and count the products A x")


def test_power_iteration_stops_after_n_iter(eigen):
    A = np.array([[0.0, 3.0], [3.0, 0.0]])          # eigenvalues 3 and -3: x keeps swapping, no convergence
    value, _, iterations = _result(lambda: eigen.power_iteration(A, x0=[1.0, 0.0], n_iter=37), "37 iterations",
                                   "two eigenvalues of the same absolute value")
    assert iterations == 37, (f"expected iterations = n_iter = 37 when the tolerance is never reached, got "
                              f"{iterations!r}")
    _float(value, "the eigenvalue")


@pytest.mark.parametrize("A, x0, why", [
    ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], None, "A is not square"),
    ([[2.0, 1.0], [1.0, 2.0]], [1.0, 0.0, 0.0], "x0 has 3 entries, A has 2 columns"),
    ([[2.0, 1.0], [1.0, 2.0]], [0.0, 0.0], "x0 is zero"),
    ([[1.0, 1.0], [1.0, 1.0]], [1.0, -1.0], "A x0 is zero: x0 is in the kernel of A"),
])
def test_power_iteration_rejects_invalid_inputs(eigen, A, x0, why):
    _expect_value_error(lambda: eigen.power_iteration(A, x0=x0), f"power_iteration({A}, x0={x0})", why)


def test_power_iteration_does_not_modify_its_inputs(eigen):
    A, x0 = DOMINANT["spd-4x4"].copy(), np.array([1.0, -2.0, 0.5, 3.0])
    A0, x00 = A.copy(), x0.copy()
    _result(lambda: eigen.power_iteration(A, x0=x0), "a tuple", "arrays")
    assert np.array_equal(A, A0) and np.array_equal(x0, x00), (
        "expected power_iteration to leave A and x0 unchanged (normalize a copy of x0)")


# ---------------------------------------------------------------- rayleigh_quotient
def test_rayleigh_quotient_of_an_eigenvector_is_its_eigenvalue(eigen):
    A = _spd(5)
    values, vectors = np.linalg.eigh(A)
    for k in range(5):
        x = 3.0 * vectors[:, k]                      # not a unit vector
        got = _result(lambda: eigen.rayleigh_quotient(A, x), f"the eigenvalue {values[k]:.6g}", f"eigenvector {k}")
        _float(got, "the quotient")
        assert got == pytest.approx(values[k], rel=1e-10), (
            f"expected the eigenvalue {values[k]:.10g} for an eigenvector (of norm 3), got {got!r}: divide xᵀA x by xᵀx")


def test_rayleigh_quotient_is_between_the_extreme_eigenvalues(eigen):
    A = np.array([[1.0, 2.0, 0.0], [2.0, -1.0, 3.0], [0.0, 3.0, 2.0]])
    values = np.linalg.eigvalsh(A)
    rng = np.random.default_rng(12)
    for _ in range(20):
        x = rng.normal(size=3)
        got = _result(lambda: eigen.rayleigh_quotient(A, x), "a number between λ_min and λ_max", "a random x")
        assert values[0] - 1e-12 <= got <= values[-1] + 1e-12, (
            f"expected a quotient between λ_min = {values[0]:.6g} and λ_max = {values[-1]:.6g}, got {got!r}")


def test_rayleigh_quotient_matches_its_definition(eigen):
    A = np.array([[1.0, 4.0], [-2.0, 3.0]])          # not symmetric: the definition still holds
    for x in ([1.0, 0.0], [0.0, 2.0], [3.0, -1.0], [1e-3, 1e-3]):
        v = np.array(x)
        expected = float(v @ A @ v / (v @ v))
        got = _result(lambda: eigen.rayleigh_quotient(A, x), f"{expected:.6g}", f"x = {x}")
        assert got == pytest.approx(expected, rel=1e-12), f"expected {expected!r} for x = {x}, got {got!r}"


def test_rayleigh_quotient_docstring_examples(eigen):
    for x, expected in [([1, 0], 3.0), ([2, 1], 4.0)]:
        got = _result(lambda: eigen.rayleigh_quotient([[3, 2], [2, 0]], x), repr(expected), "the docstring")
        assert got == pytest.approx(expected, abs=1e-12), f"expected {expected} for x = {x}, got {got!r}"


@pytest.mark.parametrize("A, x, why", [
    ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], [1.0, 1.0, 1.0], "A is not square"),
    ([[2.0, 1.0], [1.0, 2.0]], [1.0, 0.0, 0.0], "x has 3 entries, A has 2 columns"),
    ([[2.0, 1.0], [1.0, 2.0]], [0.0, 0.0], "x is zero"),
])
def test_rayleigh_quotient_rejects_invalid_inputs(eigen, A, x, why):
    _expect_value_error(lambda: eigen.rayleigh_quotient(A, x), f"rayleigh_quotient({A}, {x})", why)


# ---------------------------------------------------------------- cholesky
POSITIVE_DEFINITE = {
    "one-by-one": np.array([[6.25]]),
    "integers-3x3": np.array([[9.0, -3.0, 6.0], [-3.0, 5.0, 0.0], [6.0, 0.0, 14.0]]),
    "random-4x4": _spd(4),
    "random-7x7": _spd(7),
    "large-scale-3x3": 1e8 * _spd(3),
}


@pytest.mark.parametrize("name", list(POSITIVE_DEFINITE))
def test_cholesky_matches_numpy(eigen, name):
    A = POSITIVE_DEFINITE[name]
    expected = np.linalg.cholesky(A)
    got = _result(lambda: eigen.cholesky(A.copy()), "a lower triangular L", name)
    _array(got, f"cholesky for {name}", A.shape)
    scale = max(1.0, float(np.sqrt(np.max(np.abs(A)))))
    assert np.allclose(got, expected, rtol=0, atol=1e-10 * scale), (
        f"expected L = {_show(expected)} for {name}, got {_show(got)} (column by column: the diagonal entry with the "
        f"square root, then the entries below it)")


def test_cholesky_is_exactly_lower_triangular_with_a_positive_diagonal(eigen):
    A = POSITIVE_DEFINITE["random-7x7"]
    L = _result(lambda: eigen.cholesky(A), "a lower triangular L", "a 7 × 7 matrix")
    assert np.all(np.triu(L, 1) == 0), (
        f"expected exactly 0 above the diagonal of L, got a largest |entry| of {np.max(np.abs(np.triu(L, 1))):.1e} "
        f"(start from np.zeros((n, n)) and never write above the diagonal)")
    assert np.all(np.diag(L) > 0), f"expected a positive diagonal, got {_show(np.diag(L))}"
    assert np.allclose(L @ L.T, A, atol=1e-10), "expected L Lᵀ = A"


def test_cholesky_docstring_example(eigen):
    got = _result(lambda: eigen.cholesky([[4, 2], [2, 5]]), "[[2, 0], [1, 2]]", "the docstring")
    assert np.allclose(np.asarray(got, dtype=float), [[2.0, 0.0], [1.0, 2.0]]), (
        f"expected [[2, 0], [1, 2]] for cholesky([[4, 2], [2, 5]]), got {got!r}")


def test_cholesky_accepts_a_rounding_asymmetry(eigen):
    A = POSITIVE_DEFINITE["integers-3x3"].copy()
    A[0, 1] += 14 * 1e-15                            # below 1e-12 · max(1, max |A|) = 1.4e-11
    got = _result(lambda: eigen.cholesky(A), "a lower triangular L", "an asymmetry of 1.4e-14",
                  "the symmetry test is relative: |A[i, j] - A[j, i]| ≤ 1e-12 · max(1, max |A|)")
    assert np.allclose(got @ got.T, POSITIVE_DEFINITE["integers-3x3"], atol=1e-10), "expected L Lᵀ = A"
    big = 1e8 * POSITIVE_DEFINITE["integers-3x3"]
    big[2, 0] += 1e-6                                # 1e-6 ≤ 1e-12 · 1.4e9: still symmetric for the docstring
    _result(lambda: eigen.cholesky(big), "a lower triangular L", "entries of order 1e9 and an asymmetry of 1e-6",
            "the symmetry test is relative to the size of the entries: 1e-12 · max(1, max |A|)")


@pytest.mark.parametrize("A, why", [
    ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], "A is not square"),
    ([[4.0, 1.0], [3.0, 5.0]], "A is not symmetric"),
    ([[9.0, 1.0 + 1e-9], [1.0, 9.0]], "an asymmetry of 1e-9, above 1e-12 · max(1, max |A|)"),
    ([[1.0, 3.0], [3.0, 2.0]], "A is not positive definite (eigenvalues of both signs)"),
    ([[1.0, 2.0, 0.0], [2.0, 4.0, 0.0], [0.0, 0.0, 1.0]], "A is only semi-definite: a pivot is exactly 0"),
    ([[-4.0, 0.0], [0.0, 1.0]], "a negative diagonal entry"),
])
def test_cholesky_rejects_invalid_inputs(eigen, A, why):
    _expect_value_error(lambda: eigen.cholesky(A), f"cholesky({A})", why)


def test_cholesky_does_not_modify_its_input(eigen):
    A = POSITIVE_DEFINITE["random-4x4"].copy()
    _result(lambda: eigen.cholesky(A), "a matrix", "an array")
    assert np.array_equal(A, POSITIVE_DEFINITE["random-4x4"]), "expected cholesky to leave its input unchanged"


# ---------------------------------------------------------------- is_positive_definite
DEFINITENESS = [
    (POSITIVE_DEFINITE["random-4x4"], True, "a random positive definite matrix"),
    (np.array([[3.0, -1.0, 0.0], [-1.0, 3.0, -1.0], [0.0, -1.0, 3.0]]), True, "a tridiagonal positive definite matrix"),
    (np.array([[1.0, 3.0], [3.0, 2.0]]), False, "eigenvalues of both signs"),
    (np.array([[1.0, 2.0, 0.0], [2.0, 4.0, 0.0], [0.0, 0.0, 1.0]]), False, "only semi-definite (an eigenvalue 0)"),
    (-POSITIVE_DEFINITE["integers-3x3"], False, "negative definite"),
    (np.array([[1.0, 1.0], [-1.0, 1.0]]), False, "xᵀA x = ‖x‖² > 0, but A is not symmetric"),
    (np.array([[0.5]]), True, "a 1 × 1 matrix with a positive entry"),
]


@pytest.mark.parametrize("A, expected, why", DEFINITENESS, ids=[why for _, _, why in DEFINITENESS])
def test_is_positive_definite_matches_the_eigenvalues(eigen, A, expected, why):
    got = _result(lambda: eigen.is_positive_definite(A.copy()), repr(expected), why)
    assert type(got) is bool, (f"expected a Python bool, got {type(got).__module__}.{type(got).__name__} "
                               f"(return True or False)")
    assert got is expected, f"expected {expected} for {_show(A)} ({why}), got {got!r}"


def test_is_positive_definite_docstring_examples(eigen):
    for rows, expected in [([[2, -1], [-1, 2]], True), ([[1, 2], [2, 1]], False)]:
        got = _result(lambda: eigen.is_positive_definite(rows), repr(expected), "the docstring")
        assert got is expected, f"expected {expected} for {rows}, got {got!r}"


def test_is_positive_definite_rejects_a_non_square_matrix(eigen):
    A = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
    _expect_value_error(lambda: eigen.is_positive_definite(A), f"is_positive_definite({A})",
                        "A is not square: raise, do not answer False")


# ---------------------------------------------------------------- sqrtm_psd
SEMI_DEFINITE = {
    "random-4x4": POSITIVE_DEFINITE["random-4x4"],
    "integers-3x3": POSITIVE_DEFINITE["integers-3x3"],
    "rank-2-of-4x4": (lambda X: X @ X.T)(RNG.normal(size=(4, 2))),
    "zero-2x2": np.zeros((2, 2)),
}


@pytest.mark.parametrize("name", list(SEMI_DEFINITE))
def test_sqrtm_psd_squares_back_to_a(eigen, name):
    A = SEMI_DEFINITE[name]
    B = _result(lambda: eigen.sqrtm_psd(A.copy()), "a symmetric matrix B with B B = A", name)
    _array(B, f"sqrtm_psd for {name}", A.shape)
    scale = max(1.0, float(np.max(np.abs(A))))
    assert np.allclose(B @ B, A, rtol=0, atol=1e-9 * scale), (
        f"expected B B = A for {name}, got B B = {_show(B @ B)} instead of {_show(A)} (B = Q diag(√λ) Qᵀ)")
    assert np.allclose(B, B.T, atol=1e-12 * scale), "expected a symmetric B"
    assert np.min(np.linalg.eigvalsh((B + B.T) / 2)) >= -1e-8 * scale, (
        "expected B positive semi-definite (the square roots √λ ≥ 0, never -√λ)")


@pytest.mark.parametrize("name", ["random-4x4", "integers-3x3"])
def test_sqrtm_psd_matches_scipy(eigen, name):
    A = SEMI_DEFINITE[name]
    expected = np.real(scipy.linalg.sqrtm(A))
    got = _result(lambda: eigen.sqrtm_psd(A), "the matrix of scipy.linalg.sqrtm", name)
    assert np.allclose(got, expected, atol=1e-9), (
        f"expected {_show(expected)} for {name} (the only symmetric positive semi-definite square root), got "
        f"{_show(got)}")


def test_sqrtm_psd_docstring_examples(eigen):
    for rows, expected in [([[4, 0], [0, 9]], [[2.0, 0.0], [0.0, 3.0]]), ([[5, 5], [5, 10]], [[2.0, 1.0], [1.0, 3.0]])]:
        got = _result(lambda: eigen.sqrtm_psd(rows), repr(expected), "the docstring")
        assert np.allclose(np.asarray(got, dtype=float), expected), f"expected {expected} for {rows}, got {got!r}"


def test_sqrtm_psd_tolerance_is_relative_to_the_largest_eigenvalue(eigen):
    Q = np.linalg.qr(np.random.default_rng(1233).normal(size=(4, 4)))[0]
    A = Q @ np.diag([1e6, 1.0, 0.5, -1e-9]) @ Q.T       # -1e-9 is above -tol · λ_max = -1e-6: a rounding error
    A = (A + A.T) / 2
    B = _result(lambda: eigen.sqrtm_psd(A), "a square root", "λ_max = 1e6 and an eigenvalue of -1e-9",
                "the tolerance is relative: eigenvalues between -tol · max(1, λ_max) and 0 count as 0")
    assert np.all(np.isfinite(B)), "expected finite entries: clip the tiny negative eigenvalues to 0 before √"


def test_sqrtm_psd_accepts_a_tiny_negative_eigenvalue(eigen):
    Q = np.linalg.qr(RNG.normal(size=(3, 3)))[0]
    A = Q @ np.diag([4.0, 1.0, -1e-14]) @ Q.T
    A = (A + A.T) / 2
    B = _result(lambda: eigen.sqrtm_psd(A), "a square root", "an eigenvalue of -1e-14 (a rounding error)",
                "eigenvalues between -tol · max(1, λ_max) and 0 count as 0")
    assert np.all(np.isfinite(B)), "expected finite entries: clip the tiny negative eigenvalues to 0 before √"


@pytest.mark.parametrize("A, why", [
    ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], "A is not square"),
    ([[4.0, 1.0], [3.0, 5.0]], "A is not symmetric"),
    ([[1.0, 3.0], [3.0, 2.0]], "A has a negative eigenvalue"),
    ([[1.0, 0.0], [0.0, -1e-6]], "an eigenvalue of -1e-6, far below -tol · max(1, λ_max)"),
])
def test_sqrtm_psd_rejects_invalid_inputs(eigen, A, why):
    _expect_value_error(lambda: eigen.sqrtm_psd(A), f"sqrtm_psd({A})", why)


def test_sqrtm_psd_does_not_modify_its_input(eigen):
    A = SEMI_DEFINITE["rank-2-of-4x4"].copy()
    _result(lambda: eigen.sqrtm_psd(A), "a matrix", "an array")
    assert np.array_equal(A, SEMI_DEFINITE["rank-2-of-4x4"]), "expected sqrtm_psd to leave its input unchanged"


# ---------------------------------------------------------------- whitening_matrix
COVARIANCES = {
    "random-3x3": _spd(3),
    "integers-3x3": POSITIVE_DEFINITE["integers-3x3"],
    "strongly-correlated-2x2": np.array([[1.0, 0.99], [0.99, 1.0]]) * 4.0,
}


@pytest.mark.parametrize("method", ["zca", "cholesky"])
@pytest.mark.parametrize("name", list(COVARIANCES))
def test_whitening_matrix_gives_the_identity(eigen, name, method):
    S = COVARIANCES[name]
    W = _result(lambda: eigen.whitening_matrix(S.copy(), method=method), "a matrix W with W Σ Wᵀ = I",
                f"{name}, method={method!r}")
    _array(W, f"whitening_matrix for {name}", S.shape)
    assert np.allclose(W @ S @ W.T, np.eye(S.shape[0]), atol=1e-9), (
        f"expected W Σ Wᵀ = I for {name} with method={method!r}, got {_show(W @ S @ W.T)}")


@pytest.mark.parametrize("name", list(COVARIANCES))
def test_whitening_matrix_zca_is_the_inverse_square_root(eigen, name):
    S = COVARIANCES[name]
    expected = np.linalg.inv(np.real(scipy.linalg.sqrtm(S)))
    got = _result(lambda: eigen.whitening_matrix(S), "Σ^(-1/2)", name)
    assert np.allclose(got, expected, atol=1e-8), (
        f"expected the symmetric W = Σ^(-1/2) = {_show(expected)} for {name} (method='zca' by default), got "
        f"{_show(got)} (Q diag(1/√λ) Qᵀ)")


@pytest.mark.parametrize("name", list(COVARIANCES))
def test_whitening_matrix_cholesky_is_the_inverse_of_l(eigen, name):
    S = COVARIANCES[name]
    expected = np.linalg.inv(np.linalg.cholesky(S))
    got = _result(lambda: eigen.whitening_matrix(S, method="cholesky"), "L⁻¹", name)
    assert np.allclose(got, expected, atol=1e-8), (
        f"expected W = L⁻¹ = {_show(expected)} for {name}, with Σ = L Lᵀ, got {_show(got)}")
    assert np.allclose(np.triu(got, 1), 0, atol=1e-12), "expected a lower triangular W (the inverse of a lower L)"


def test_whitening_matrix_whitens_data(eigen):
    rng = np.random.default_rng(1213)
    X = rng.normal(size=(400, 3)) @ np.array([[2.0, 0.0, 0.0], [1.5, 0.5, 0.0], [-1.0, 0.8, 0.3]]) + [5.0, -2.0, 1.0]
    S = np.cov(X, rowvar=False)
    for method in ("zca", "cholesky"):
        W = _result(lambda: eigen.whitening_matrix(S, method=method), "a whitening matrix", f"method={method!r}")
        Z = (X - X.mean(axis=0)) @ W.T
        assert np.allclose(np.cov(Z, rowvar=False), np.eye(3), atol=1e-9), (
            f"expected the whitened data (X - mean) @ W.T to have the covariance I with method={method!r}, got "
            f"{_show(np.cov(Z, rowvar=False))}")


def test_whitening_matrix_docstring_examples(eigen):
    got = _result(lambda: eigen.whitening_matrix([[4, 0], [0, 25]]), "[[0.5, 0], [0, 0.2]]", "the docstring")
    assert np.allclose(np.asarray(got, dtype=float), [[0.5, 0.0], [0.0, 0.2]]), f"expected [[0.5, 0], [0, 0.2]], got {got!r}"
    got = _result(lambda: eigen.whitening_matrix([[4, 2], [2, 5]], method="cholesky"), "[[0.5, 0], [-0.25, 0.5]]",
                  "the docstring")
    assert np.allclose(np.asarray(got, dtype=float), [[0.5, 0.0], [-0.25, 0.5]]), (
        f"expected [[0.5, 0], [-0.25, 0.5]], got {got!r}")


@pytest.mark.parametrize("cov, method, why", [
    ([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], "zca", "cov is not square"),
    ([[4.0, 1.0], [3.0, 5.0]], "zca", "cov is not symmetric"),
    ([[4.0, 1.0], [3.0, 5.0]], "cholesky", "cov is not symmetric"),
    ([[4.0, 0.0], [0.0, 0.0]], "zca", "cov is only semi-definite: an eigenvalue 0, no 1/√λ"),
    ([[4.0, 2.0], [2.0, 1.0]], "cholesky", "cov is only semi-definite: a pivot 0"),
    ([[1.0, 3.0], [3.0, 2.0]], "zca", "cov has a negative eigenvalue"),
    ([[4.0, 0.0], [0.0, 1.0]], "pca", "the method is unknown"),
])
def test_whitening_matrix_rejects_invalid_inputs(eigen, cov, method, why):
    hint = ("a LinAlgError from np.linalg.solve means that L has a 0 on its diagonal: your cholesky accepted a pivot "
            "that is not strictly positive (refuse it with `not pivot > 0`)" if "pivot" in why else "")
    _expect_value_error(lambda: eigen.whitening_matrix(cov, method=method),
                        f"whitening_matrix({cov}, method={method!r})", why, hint)


def test_whitening_matrix_does_not_modify_its_input(eigen):
    S = COVARIANCES["random-3x3"].copy()
    for method in ("zca", "cholesky"):
        _result(lambda: eigen.whitening_matrix(S, method=method), "a matrix", "an array")
    assert np.array_equal(S, COVARIANCES["random-3x3"]), "expected whitening_matrix to leave its input unchanged"
