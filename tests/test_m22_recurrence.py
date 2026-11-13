"""Tests of mymath.recurrence (chapter M22): the states of a linear recurrence with an input, the induced norms
‖·‖₁, ‖·‖₂ and ‖·‖∞ of a matrix, and the norms of the cumulative products of a sequence of matrices with their
upper bound.

Oracles: a step-by-step loop written in this file and the closed form ``x_t = Aᵗ x_0 + Σ_{k<t} A^{t-1-k} B u_k``
(``np.linalg.matrix_power``) for the states; ``np.linalg.norm``, ``np.linalg.matrix_norm`` and
``np.linalg.svdvals`` for the induced norms, an extremal vector built here (a vector of the canonical basis for
‖·‖₁, a vector of signs for ‖·‖∞, the first right singular vector of ``np.linalg.svd`` for ‖·‖₂) and
``np.linalg.eigvals`` (ρ(A) ≤ ‖A‖); the cumulative products computed here with ``np.linalg.norm``, rotations and
diagonal matrices for the products; and properties (linearity in the start and the inputs, an impulse, special
matrices, ‖A x‖ ≤ ‖A‖ ‖x‖, norms ≤ bounds, inputs left unchanged, Python floats and arrays of floats). They describe
the expected behaviour without showing the solution.

    pytest tests/test_m22_recurrence.py              # your code
    pytest tests/test_m22_recurrence.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings

import numpy as np
import pytest


@pytest.fixture
def rc(mymath_module):
    return mymath_module("recurrence")


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


def _float(got, what):
    assert type(got) is float, (f"expected {what} as a Python float (float(...)), got "
                                f"{type(got).__module__}.{type(got).__name__} {got!r}")


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


def _close_number(got, want, what, rtol=1e-10, atol=1e-12, hint=""):
    assert math.isclose(got, want, rel_tol=rtol, abs_tol=atol), (
        f"expected {what} = {want:.12g}, got {got:.12g}" + (f" ({hint})" if hint else ""))


ORDS = (1, 2, np.inf)
ORD_NAMES = {1: "1", 2: "2", np.inf: "inf"}
ORD_HINTS = {
    1: "‖A‖₁ is the largest sum of the absolute values of a COLUMN",
    2: "‖A‖₂ is s_max, the square root of the largest eigenvalue of AᵀA (not the largest |eigenvalue| of A)",
    np.inf: "‖A‖∞ is the largest sum of the absolute values of a ROW",
}


# --- what the module may use ------------------------------------------------------------------------------------

def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``norm`` (from numpy.linalg import norm) → "numpy.linalg.norm"."""
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
    ("operator_norm", "numpy.linalg.eigvalsh"); ``where`` is the top-level function, or "the module level"."""
    inner = {id(node.value) for node in ast.walk(tree) if isinstance(node, ast.Attribute)}
    uses = []
    for statement in tree.body:
        where = statement.name if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)) else "the module level"
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


def _reachable(functions, start):
    """``start`` and the module functions it names, directly or through other module functions."""
    seen, todo = set(), [start]
    while todo:
        name = todo.pop()
        if name in seen or name not in functions:
            continue
        seen.add(name)
        todo += [n.id for n in ast.walk(functions[name]) if isinstance(n, ast.Name) and n.id in functions]
    return seen


def test_module_uses_eigvalsh_only_in_operator_norm_norm_only_in_product_norms_and_no_scipy(rc):
    """The docstring allows from np.linalg only eigvalsh, in operator_norm, and norm, in product_norms (each with the
    module's own functions that it calls; product_norms may call operator_norm, but np.linalg.norm never serves
    operator_norm), and no SciPy at all. Only the code counts: a comment, a docstring or an import never used is not
    a use. ``np.linalg.LinAlgError`` (an exception, not a computation) is not counted."""
    try:
        tree = ast.parse(inspect.getsource(rc))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    functions = {n.name: n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    eigvalsh_allowed = _reachable(functions, "operator_norm")
    norm_allowed = _reachable(functions, "product_norms") - eigvalsh_allowed
    found = []
    for where, path in _uses(tree, _imported_names(tree)):
        parts = path.split(".")
        shown = ".".join(["np"] + parts[1:]) if parts[0] == "numpy" else path
        if parts[0] == "scipy":
            found.append(f"{shown} in {where}")
        elif parts[0] == "numpy" and len(parts) > 2 and parts[1] == "linalg":
            if parts[2] == "LinAlgError":
                continue
            if not ((parts[2] == "eigvalsh" and where in eigvalsh_allowed)
                    or (parts[2] == "norm" and where in norm_allowed)):
                found.append(f"{shown} in {where}")
    assert not found, (f"expected NumPy with, from np.linalg, only eigvalsh in operator_norm and norm in "
                       f"product_norms, and no SciPy at all, found {sorted(set(found))} (the tests compare your "
                       f"results with np.linalg.norm, matrix_norm, svdvals and matrix_power: write the computation "
                       f"yourself)")


# --- linear_system_states -------------------------------------------------------------------------------------------

STATES_HINT = ("x_{t+1} = A x_t + B u_t, not A (x_t + B u_t): u_t, the row t of inputs, enters at the step from "
               "x_t to x_{t+1}; column convention: A @ x, not x @ A")


def _states_by_loop(A, B, x0, inputs):
    """The states computed step by step, one row per state."""
    x = np.array(x0, dtype=float)
    rows = [x.copy()]
    for u in np.asarray(inputs, dtype=float):
        x = np.asarray(A, dtype=float) @ x + np.asarray(B, dtype=float) @ u
        rows.append(x.copy())
    return np.array(rows)


def _states_closed_form(A, B, x0, inputs):
    """x_t = Aᵗ x_0 + Σ_{k<t} A^{t-1-k} B u_k, with np.linalg.matrix_power."""
    A, B, x0, U = (np.asarray(v, dtype=float) for v in (A, B, x0, inputs))
    rows = []
    for t in range(U.shape[0] + 1):
        x = np.linalg.matrix_power(A, t) @ x0
        for k in range(t):
            x = x + np.linalg.matrix_power(A, t - 1 - k) @ (B @ U[k])
        rows.append(x)
    return np.array(rows)


def _random_system(rng, n, m, T):
    """A random (A, B, x0, inputs); A scaled so that its powers stay of moderate size."""
    A = rng.normal(size=(n, n)) / math.sqrt(n)
    return A, rng.normal(size=(n, m)), rng.normal(size=n), rng.normal(size=(T, m))


def test_linear_system_states_docstring_example(rc):
    A, B = [[0.6, 0.3], [0.2, 0.5]], [[1.0], [2.0]]
    want = [[1.0, 0.0], [0.6, 0.2], [1.42, 2.22]]
    got = _result(lambda: rc.linear_system_states(A, B, [1.0, 0.0], [[0.0], [1.0]]), _show(want),
                  "the example of the docstring")
    _float_array(got, (3, 2), "linear_system_states(A, B, [1.0, 0.0], [[0.0], [1.0]]) (T + 1 = 3 states of n = 2)")
    _close(got, want, "the states of the docstring example", rtol=1e-12, atol=1e-12, hint=STATES_HINT)


SYSTEMS = [(3, 2, 12, "n = 3, m = 2"), (1, 1, 9, "n = m = 1"), (1, 3, 8, "n = 1 and m = 3"),
           (4, 1, 7, "m = 1 (inputs of shape (T, 1))"), (2, 3, 15, "m > n"), (5, 4, 6, "n = 5, m = 4"),
           (3, 2, 1, "a single step, T = 1")]


@pytest.mark.parametrize("n, m, T, text", SYSTEMS, ids=[f"n{s[0]}-m{s[1]}-T{s[2]}" for s in SYSTEMS])
def test_linear_system_states_match_a_step_by_step_loop(rc, n, m, T, text):
    rng = np.random.default_rng(5610 + SYSTEMS.index((n, m, T, text)))
    A, B, x0, U = _random_system(rng, n, m, T)
    want = _states_by_loop(A, B, x0, U)
    what = f"the states for {text}, T = {T}"
    got = _result(lambda: rc.linear_system_states(A, B, x0, U), f"an array of shape {want.shape}", what)
    _float_array(got, (T + 1, n), f"{what} (T + 1 rows, row 0 is x_0)")
    _close(got, want, what, rtol=1e-10, atol=1e-12, hint=STATES_HINT)


def test_linear_system_states_match_the_closed_form_with_matrix_powers(rc):
    """x_t = Aᵗ x_0 + Σ_{k<t} A^{t-1-k} B u_k, checked row by row (np.linalg.matrix_power)."""
    rng = np.random.default_rng(5620)
    for n, m, T in ((3, 2, 10), (4, 3, 8), (2, 1, 14)):
        A, B, x0, U = _random_system(rng, n, m, T)
        want = _states_closed_form(A, B, x0, U)
        got = _result(lambda: rc.linear_system_states(A, B, x0, U), f"{T + 1} states", f"n = {n}, m = {m}, T = {T}")
        _float_array(got, (T + 1, n), f"the states for n = {n}, m = {m}, T = {T}")
        for t in range(T + 1):
            _close(got[t], want[t], f"x_{t} for n = {n}, m = {m}, T = {T}, A^{t} x_0 + Σ_(k<{t}) A^({t}-1-k) B u_k",
                   rtol=1e-9, atol=1e-11, hint=STATES_HINT)


def test_linear_system_states_is_linear_in_the_start_and_the_inputs(rc):
    """The states of (a x_0 + b y_0, a U + b V) are a × those of (x_0, U) plus b × those of (y_0, V); in particular,
    the free response (no input) plus the forced response (start at 0) give the whole solution."""
    rng = np.random.default_rng(5621)
    A, B, x0, U = _random_system(rng, 3, 2, 9)
    y0, V = rng.normal(size=3), rng.normal(size=(9, 2))
    a, b = -1.75, 2.6
    one = _result(lambda: rc.linear_system_states(A, B, x0, U), "10 states", "(x_0, U)")
    two = _result(lambda: rc.linear_system_states(A, B, y0, V), "10 states", "(y_0, V)")
    mixed = _result(lambda: rc.linear_system_states(A, B, a * x0 + b * y0, a * U + b * V), "10 states",
                    "(a x_0 + b y_0, a U + b V)")
    _close(mixed, a * one + b * two, f"the states of ({a} x_0 + {b} y_0, {a} U + {b} V), equal to {a} × the states of "
                                     f"(x_0, U) + {b} × those of (y_0, V) (linearity)", rtol=1e-10, atol=1e-12)
    free = _result(lambda: rc.linear_system_states(A, B, x0, np.zeros_like(U)), "10 states", "no input")
    forced = _result(lambda: rc.linear_system_states(A, B, np.zeros(3), U), "10 states", "a start at 0")
    _close(free + forced, one, "the free response (inputs 0) plus the forced response (x_0 = 0), equal to the states "
                               "of (x_0, U)", rtol=1e-10, atol=1e-12)
    _close(free, _states_closed_form(A, B, x0, np.zeros_like(U)), "the free response x_t = Aᵗ x_0", rtol=1e-9,
           atol=1e-11)


def test_linear_system_states_impulse_response(rc):
    """From x_0 = 0, an input e_j at step 0 and nothing after: x_t = A^(t-1) B e_j for t ≥ 1, the column j of B
    carried forward by the powers of A."""
    rng = np.random.default_rng(5622)
    n, m, T = 3, 2, 8
    A, B, _, _ = _random_system(rng, n, m, T)
    for j in range(m):
        U = np.zeros((T, m))
        U[0, j] = 1.0
        got = _result(lambda: rc.linear_system_states(A, B, np.zeros(n), U), f"{T + 1} states", f"an impulse e_{j}")
        _float_array(got, (T + 1, n), f"the response to the impulse e_{j}")
        want = np.array([np.zeros(n)] + [np.linalg.matrix_power(A, t - 1) @ B[:, j] for t in range(1, T + 1)])
        _close(got, want, f"the response to an impulse e_{j} at step 0, x_t = A^(t-1) B e_j", rtol=1e-9, atol=1e-12,
               hint="the input u_0 enters at the step from x_0 to x_1, then only A acts")


def test_linear_system_states_with_special_matrices(rc):
    """A = 0: x_{t+1} = B u_t (the input of the SAME index); A = I: x_t = x_0 + B (u_0 + … + u_{t-1}); a shift matrix
    tells the column convention A x from the row convention x A."""
    rng = np.random.default_rng(5623)
    n, m, T = 3, 2, 7
    B, x0, U = rng.normal(size=(n, m)), rng.normal(size=n), rng.normal(size=(T, m))
    got = _result(lambda: rc.linear_system_states(np.zeros((n, n)), B, x0, U), f"{T + 1} states", "A = 0")
    _float_array(got, (T + 1, n), "the states for A = 0")
    _close(got, np.vstack([x0, U @ B.T]), "the states for A = 0: x_0, then x_{t+1} = B u_t", rtol=1e-12, atol=1e-12,
           hint="x_{t+1} uses the input u_t, the row t of inputs (row 0 for x_1), and every input is used, the last "
                "one included")
    got = _result(lambda: rc.linear_system_states(np.eye(n), B, x0, U), f"{T + 1} states", "A = I")
    _close(got, np.vstack([x0, x0 + np.cumsum(U @ B.T, axis=0)]),
           "the states for A = I: x_t = x_0 + B (u_0 + … + u_{t-1}), a running sum", rtol=1e-12, atol=1e-12)
    shift = np.array([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]])
    start = np.array([2.5, -4.25, 1.75])
    got = _result(lambda: rc.linear_system_states(shift, B, start, np.zeros((3, m))), "4 states", "a shift matrix")
    _close(got, [[2.5, -4.25, 1.75], [-4.25, 1.75, 0.0], [1.75, 0.0, 0.0], [0.0, 0.0, 0.0]],
           "the states of x_{t+1} = A x_t for A = [[0, 1, 0], [0, 0, 1], [0, 0, 0]] from (2.5, -4.25, 1.75)",
           rtol=0, atol=0, hint="column convention: (A x)_i = Σ_j A[i, j] x_j, so A moves each coordinate UP by one; "
                                "x @ A would move them down")


def test_linear_system_states_with_no_step(rc):
    """T = 0 is given as np.zeros((0, m)): the result is the single row x_0, in a new array."""
    rng = np.random.default_rng(5624)
    for n, m in ((3, 2), (1, 1), (2, 4)):
        A, B, x0, U = _random_system(rng, n, m, 0)
        assert U.shape == (0, m)
        x_start = x0.copy()
        got = _result(lambda: rc.linear_system_states(A, B, x0, U), f"[x_0] of shape (1, {n})",
                      f"inputs = np.zeros((0, {m}))")
        _float_array(got, (1, n), f"the states for T = 0 (inputs of shape (0, {m})): the single row x_0")
        _close(got[0], x_start, "row 0, x_0", rtol=0, atol=0)
        got[:] = 99.0
        assert np.array_equal(x0, x_start), (
            "expected a new array for T = 0, but changing the result changed x0 (copy x_0 into the result)")


def test_linear_system_states_take_lists_of_integers_and_return_floats(rc):
    A, B, x0 = [[1, -2], [0, 3]], [[2, 0, 1], [-1, 4, 0]], [5, -1]
    U = [[1, 0, -2], [0, 2, 1]]
    want = _states_by_loop(A, B, x0, U)
    got = _result(lambda: rc.linear_system_states(A, B, x0, U), _show(want), "lists of integers")
    _float_array(got, (3, 2), "linear_system_states of lists of integers (a result of floats)")
    _close(got, want, "the states for lists of integers", rtol=0, atol=0, hint=STATES_HINT)
    got = _result(lambda: rc.linear_system_states(np.array(A), np.array(B), np.array(x0), np.array(U)), _show(want),
                  "integer arrays")
    _float_array(got, (3, 2), "linear_system_states of integer arrays (a result of floats)")
    _close(got, want, "the states for integer arrays", rtol=0, atol=0)


def test_linear_system_states_leave_their_inputs_alone(rc):
    rng = np.random.default_rng(5625)
    A, B, x0, U = _random_system(rng, 3, 2, 6)
    copies = [v.copy() for v in (A, B, x0, U)]
    got = _result(lambda: rc.linear_system_states(A, B, x0, U), "7 states", "float arrays")
    _float_array(got, (7, 3), "the states for float arrays")
    for name, value, copy in zip(("A", "B", "x0", "inputs"), (A, B, x0, U), copies):
        assert np.array_equal(value, copy), (
            f"expected {name} unchanged by linear_system_states, got {name} = {_show(value)} (never modify the arrays "
            f"you receive: x = A @ x + B @ u makes a new array, x[:] = … writes into x0)")
    got[:] = 99.0
    for name, value, copy in zip(("A", "B", "x0", "inputs"), (A, B, x0, U), copies):
        assert np.array_equal(value, copy), (
            f"expected linear_system_states to return a new array, but changing it changed {name}")


STATES_REFUSALS = [
    ([[0.8, 0.1, 0.0], [0.2, 0.6, 0.4]], [[1.0], [0.0]], [1.0, 2.0], [[1.0]], "A is 2 × 3, not square"),
    ([[0.8, 0.1, 0.0], [0.2, 0.6, 0.4]], [[1.0], [0.0]], [1.0, 2.0], np.zeros((0, 1)),
     "A is 2 × 3, not square, even with no step (T = 0)"),
    ([0.8, 0.1], [[1.0], [0.0]], [1.0, 2.0], [[1.0]], "A is 1-D"),
    ([[0.8, 0.1], [0.2, 0.6]], [1.0, 0.0], [1.0, 2.0], [[1.0]], "B is 1-D, even with m = 1"),
    ([[0.8, 0.1], [0.2, 0.6]], [[1.0], [0.0], [2.0]], [1.0, 2.0], [[1.0]], "B has 3 rows for n = 2"),
    ([[0.8, 0.1], [0.2, 0.6]], [[1.0], [0.0]], [1.0, 2.0, 0.0], [[1.0]], "x0 has 3 coordinates for n = 2"),
    ([[0.8, 0.1], [0.2, 0.6]], [[1.0], [0.0]], [[1.0], [2.0]], [[1.0]], "x0 is a 2-D column, not 1-D"),
    ([[0.8, 0.1], [0.2, 0.6]], [[1.0], [0.0]], [1.75], np.zeros((0, 1)),
     "x0 has 1 coordinate for n = 2, even with no step (T = 0)"),
    ([[0.8, 0.1], [0.2, 0.6]], [[1.0], [0.0]], [1.0, 2.0], [1.0, -1.0, 0.4], "inputs is 1-D, even with m = 1"),
    ([[0.8, 0.1], [0.2, 0.6]], [[1.0], [0.0]], [1.0, 2.0], [], "inputs = [] is 1-D: T = 0 is np.zeros((0, m))"),
    ([[0.8, 0.1], [0.2, 0.6]], [[1.0], [0.0]], [1.0, 2.0], [[1.0, 0.4], [0.0, 2.0]], "inputs has 2 columns for m = 1"),
    ([[0.8, 0.1], [0.2, 0.6]], [[1.0, 0.0], [0.0, 1.0]], [1.0, 2.0], np.zeros((0, 3)),
     "inputs of shape (0, 3) for m = 2: even with no step, an input has m coordinates"),
    ([[0.8, 0.1], [0.2, 0.6]], [[1.0], [0.0]], [1.0, 2.0], np.zeros((2, 3, 1)), "inputs is 3-D"),
    ([["a", "b"], ["c", "d"]], [[1.0], [0.0]], [1.0, 2.0], [[1.0]], "A holds strings, not numbers"),
]


@pytest.mark.parametrize("A, B, x0, inputs, why", STATES_REFUSALS,
                         ids=["A-not-square", "A-not-square-no-step", "A-one-d", "B-one-d", "B-rows", "x0-length",
                              "x0-column", "x0-one-coordinate-no-step", "inputs-one-d", "inputs-empty-list",
                              "inputs-columns", "inputs-empty-columns", "inputs-three-d", "A-strings"])
def test_linear_system_states_refusals(rc, A, B, x0, inputs, why):
    _expect_error(ValueError, lambda: rc.linear_system_states(A, B, x0, inputs),
                  f"linear_system_states(A, B, x0, inputs) when {why}", why)


# --- operator_norm --------------------------------------------------------------------------------------------------

def test_operator_norm_docstring_examples(rc):
    for ord, want in ((1, 6.0), (np.inf, 7.0)):
        call = f"operator_norm([[1, -2], [3, 4]], {ORD_NAMES[ord]})"
        got = _result(lambda: rc.operator_norm([[1, -2], [3, 4]], ord), repr(want), call)
        _float(got, call)
        assert got == want, f"expected {call} = {want!r}, got {got!r} ({ORD_HINTS[ord]})"
    call = "operator_norm([[1, -2], [3, 4]], 2)"
    got = _result(lambda: rc.operator_norm([[1, -2], [3, 4]], 2), "5.1167 (rounded)", call)
    _float(got, call)
    assert round(got, 4) == 5.1167, f"expected round({call}, 4) = 5.1167, got {got!r} ({ORD_HINTS[2]})"


NORM_SHAPES = [(2, 2), (3, 3), (5, 5), (2, 5), (6, 3), (1, 4), (4, 1), (1, 1)]
NORM_CASES = [(shape, ord) for shape in NORM_SHAPES for ord in ORDS]


def _numpy_norm(A, ord):
    """The oracles: np.linalg.matrix_norm (and np.linalg.norm, which must agree), s_max of np.linalg.svdvals."""
    want = float(np.linalg.matrix_norm(A, ord=ord))
    assert math.isclose(want, float(np.linalg.norm(A, ord)), rel_tol=1e-12)
    if ord == 2:
        assert math.isclose(want, float(np.linalg.svdvals(A)[0]), rel_tol=1e-12)
    return want


@pytest.mark.parametrize("shape, ord", NORM_CASES, ids=[f"ord-{ORD_NAMES[o]}-{s[0]}x{s[1]}" for s, o in NORM_CASES])
def test_operator_norm_matches_numpy(rc, shape, ord):
    rng = np.random.default_rng(5630 + NORM_SHAPES.index(shape))
    A = rng.normal(size=shape) * 2.0
    want = _numpy_norm(A, ord)
    call = f"operator_norm(A, {ORD_NAMES[ord]}) for a random {shape[0]} × {shape[1]} matrix"
    got = _result(lambda: rc.operator_norm(A, ord), f"{want:.12g}", call)
    _float(got, call)
    _close_number(got, want, f"{call} (np.linalg.matrix_norm{', s_max of np.linalg.svdvals' if ord == 2 else ''})",
                  rtol=1e-10, atol=1e-12, hint=ORD_HINTS[ord])


def test_operator_norm_default_order_is_2(rc):
    rng = np.random.default_rng(5638)
    A = rng.normal(size=(3, 4))
    got = _result(lambda: rc.operator_norm(A), "s_max", "operator_norm(A) without ord")
    _float(got, "operator_norm(A) without ord")
    _close_number(got, float(np.linalg.svdvals(A)[0]), "operator_norm(A) without ord, ‖A‖₂ = s_max (default 2)",
                  hint=ORD_HINTS[2])


def test_operator_norm_column_sums_and_row_sums_of_absolute_values(rc):
    """Signs matter: the sums are of |a_ij|; ‖·‖₁ reads the columns, ‖·‖∞ the rows, and ‖Aᵀ‖₁ = ‖A‖∞."""
    A = np.array([[-4.0, 1.25, 0.0], [2.5, -0.75, 6.0]])
    for ord, want in ((1, 6.5), (np.inf, 9.25)):
        call = f"operator_norm([[-4, 1.25, 0], [2.5, -0.75, 6]], {ORD_NAMES[ord]})"
        got = _result(lambda: rc.operator_norm(A, ord), repr(want), call)
        _float(got, call)
        assert math.isclose(got, want, rel_tol=1e-14), (
            f"expected {call} = {want!r}, got {got!r} ({ORD_HINTS[ord]}: the column sums of |A| are 6.5, 2 and "
            f"6, the row sums 5.25 and 9.25)")
    for ord, other in ((1, np.inf), (np.inf, 1)):
        got = _result(lambda: rc.operator_norm(A.T, ord), "the norm of A", f"Aᵀ, ord {ORD_NAMES[ord]}")
        want = 9.25 if ord == 1 else 6.5
        assert math.isclose(got, want, rel_tol=1e-14), (
            f"expected operator_norm(Aᵀ, {ORD_NAMES[ord]}) = operator_norm(A, {ORD_NAMES[other]}) = {want!r} (the "
            f"columns of Aᵀ are the rows of A), got {got!r}")


def _extremal_vector(A, ord):
    """A vector x ≠ 0 with ‖A x‖ = ‖A‖ ‖x‖, built from A: e_j for the largest column (‖·‖₁), the signs of the largest
    row (‖·‖∞), the first right singular vector (‖·‖₂)."""
    if ord == 1:
        return np.eye(A.shape[1])[int(np.argmax(np.abs(A).sum(axis=0)))]
    if ord == np.inf:
        return np.sign(A[int(np.argmax(np.abs(A).sum(axis=1)))])
    return np.linalg.svd(A)[2][0]


@pytest.mark.parametrize("shape", [(3, 3), (2, 5), (6, 3), (4, 1)], ids=["3x3", "2x5", "6x3", "4x1"])
def test_operator_norm_bounds_A_x_with_equality_for_an_extremal_vector(rc, shape):
    """‖A x‖ ≤ ‖A‖ ‖x‖ for 300 random x, and equality for an extremal vector built in this test: ‖A‖ is the largest
    ratio ‖A x‖ / ‖x‖, and it is reached."""
    rng = np.random.default_rng(5640 + [(3, 3), (2, 5), (6, 3), (4, 1)].index(shape))
    A = rng.normal(size=shape)
    xs = rng.normal(size=(300, shape[1]))
    for ord in ORDS:
        what = f"operator_norm(A, {ORD_NAMES[ord]}) for a {shape[0]} × {shape[1]} matrix"
        got = _result(lambda: rc.operator_norm(A, ord), "‖A‖", what)
        _float(got, what)
        ratios = [np.linalg.norm(A @ x, ord) / np.linalg.norm(x, ord) for x in xs]
        worst = max(ratios)
        assert worst <= got * (1 + 1e-12), (
            f"expected ‖A x‖ ≤ ‖A‖ ‖x‖ for every x, with ‖A‖ = {what} = {got:.10g}, got a vector x with "
            f"‖A x‖ / ‖x‖ = {worst:.10g} ({ORD_HINTS[ord]})")
        x = _extremal_vector(A, ord)
        reached = float(np.linalg.norm(A @ x, ord) / np.linalg.norm(x, ord))
        _close_number(got, reached, f"{what}, the ratio ‖A x‖ / ‖x‖ reached by the vector x = {_show(x)}",
                      rtol=1e-10, hint=ORD_HINTS[ord])


def test_operator_norm_is_at_least_the_spectral_radius(rc):
    """ρ(A) = max |λ| (np.linalg.eigvals, complex eigenvalues included) ≤ ‖A‖ for the three norms; for these
    non-symmetric matrices ρ(A) < ‖A‖₂ strictly: the norm is not ρ(A)."""
    rng = np.random.default_rng(5644)
    for trial in range(6):
        n = 2 + trial % 3
        A = rng.normal(size=(n, n))
        rho = float(np.max(np.abs(np.linalg.eigvals(A))))
        assert rho < _numpy_norm(A, 2) * (1 - 1e-3)                  # the oracle: a strict gap here
        for ord in ORDS:
            what = f"operator_norm(A, {ORD_NAMES[ord]}) for a random non-symmetric {n} × {n} matrix"
            got = _result(lambda: rc.operator_norm(A, ord), "‖A‖", what)
            _float(got, what)
            assert rho <= got * (1 + 1e-12), (
                f"expected ρ(A) = {rho:.10g} ≤ ‖A‖ = {what}, got {got:.10g} ({ORD_HINTS[ord]})")
            _close_number(got, _numpy_norm(A, ord), what, rtol=1e-10, hint=ORD_HINTS[ord])


def test_operator_norm_of_special_matrices(rc):
    """A diagonal matrix: max |d_i| for the three norms; an orthogonal matrix: ‖Q‖₂ = 1; ‖Aᵀ‖₂ = ‖A‖₂; a matrix of
    rank 1, u vᵀ: ‖u‖₂ ‖v‖₂, ‖u‖₁ ‖v‖∞ and ‖u‖∞ ‖v‖₁; ‖c A‖ = |c| ‖A‖; the zero matrix: 0.0."""
    rng = np.random.default_rng(5645)
    D = np.diag([-3.25, 0.45, 2.6, -0.8])
    for ord in ORDS:
        got = _result(lambda: rc.operator_norm(D, ord), "3.25", f"diag(-3.25, 0.45, 2.6, -0.8), ord {ORD_NAMES[ord]}")
        _close_number(got, 3.25, f"operator_norm(diag(-3.25, 0.45, 2.6, -0.8), {ORD_NAMES[ord]}), max |d_i|",
                      hint=ORD_HINTS[ord])
    Q, _ = np.linalg.qr(rng.normal(size=(4, 4)))
    got = _result(lambda: rc.operator_norm(Q, 2), "1.0", "an orthogonal matrix")
    _close_number(got, 1.0, "operator_norm(Q, 2) for an orthogonal Q (from a QR factorization)", hint=ORD_HINTS[2])
    A = rng.normal(size=(3, 5))
    left = _result(lambda: rc.operator_norm(A, 2), "s_max", "a 3 × 5 matrix")
    right = _result(lambda: rc.operator_norm(A.T, 2), "s_max", "its 5 × 3 transpose")
    _close_number(right, left, "operator_norm(Aᵀ, 2), equal to operator_norm(A, 2) for a 3 × 5 matrix (‖Aᵀ‖₂ = ‖A‖₂)")
    u, v = rng.normal(size=3), rng.normal(size=4)
    outer = np.outer(u, v)
    for ord, want, text in ((2, np.linalg.norm(u) * np.linalg.norm(v), "‖u‖₂ ‖v‖₂"),
                            (1, np.linalg.norm(u, 1) * np.linalg.norm(v, np.inf), "‖u‖₁ ‖v‖∞"),
                            (np.inf, np.linalg.norm(u, np.inf) * np.linalg.norm(v, 1), "‖u‖∞ ‖v‖₁")):
        got = _result(lambda: rc.operator_norm(outer, ord), text, f"u vᵀ of rank 1, ord {ORD_NAMES[ord]}",
                      hint="AᵀA has eigenvalues 0 (up to rounding, maybe slightly negative): only the largest counts")
        _float(got, f"operator_norm(u vᵀ, {ORD_NAMES[ord]})")
        _close_number(got, float(want), f"operator_norm(u vᵀ, {ORD_NAMES[ord]}) for a 3 × 4 matrix of rank 1, {text}",
                      hint=ORD_HINTS[ord])
    for ord in ORDS:
        base = _result(lambda: rc.operator_norm(A, ord), "‖A‖", f"ord {ORD_NAMES[ord]}")
        scaled = _result(lambda: rc.operator_norm(-2.75 * A, ord), "2.75 ‖A‖", f"-2.75 A, ord {ORD_NAMES[ord]}")
        _close_number(scaled, 2.75 * base, f"operator_norm(-2.75 A, {ORD_NAMES[ord]}), 2.75 × operator_norm(A, "
                                           f"{ORD_NAMES[ord]}) (‖c A‖ = |c| ‖A‖)")
        zero = _result(lambda: rc.operator_norm(np.zeros((2, 3)), ord), "0.0", f"the zero matrix, ord {ORD_NAMES[ord]}")
        _float(zero, f"operator_norm(np.zeros((2, 3)), {ORD_NAMES[ord]})")
        assert zero == 0.0, f"expected operator_norm(np.zeros((2, 3)), {ORD_NAMES[ord]}) = 0.0, got {zero!r}"


def test_operator_norm_takes_integers_and_leaves_A_alone(rc):
    A = [[3, -1, 0], [-2, 5, 4]]
    for ord, want in ((1, 6.0), (np.inf, 11.0), (2, float(np.linalg.svdvals(np.array(A, dtype=float))[0]))):
        for given, text in ((A, "a list of integers"), (np.array(A), "an integer array")):
            call = f"operator_norm({text} [[3, -1, 0], [-2, 5, 4]], {ORD_NAMES[ord]})"
            got = _result(lambda: rc.operator_norm(given, ord), f"{want:.12g}", call)
            _float(got, call)
            _close_number(got, want, call, hint=ORD_HINTS[ord])
    B = np.array([[-1.75, 2.25], [0.8, -3.5], [4.5, 0.35]])
    copy = B.copy()
    for ord in ORDS:
        got = _result(lambda: rc.operator_norm(B, ord), "‖B‖", f"a float matrix, ord {ORD_NAMES[ord]}")
        _float(got, f"operator_norm(B, {ORD_NAMES[ord]})")
        assert np.array_equal(B, copy), (
            f"expected B unchanged by operator_norm(B, {ORD_NAMES[ord]}), got {_show(B)} (never modify the array you "
            f"receive: np.abs(B) makes a new array)")


NORM_REFUSALS = [
    ([1.0, -2.5, 4.0], 2, "A is 1-D"),
    (np.ones((2, 2, 2)), 1, "A is 3-D"),
    (np.zeros((0, 3)), 2, "A is empty (0 rows)"),
    (np.zeros((3, 0)), np.inf, "A is empty (0 columns)"),
    (4.5, 2, "A is a number"),
    ([[1.0, -2.5], [0.75, 4.0]], True, "ord = True: a bool is refused"),
    ([[1.0, -2.5], [0.75, 4.0]], False, "ord = False: a bool is refused"),
    ([[1.0, -2.5], [0.75, 4.0]], "fro", "ord = 'fro': the Frobenius norm is not induced by a vector norm"),
    ([[1.0, -2.5], [0.75, 4.0]], "nuc", "ord = 'nuc' is not an induced norm"),
    ([[1.0, -2.5], [0.75, 4.0]], "inf", "ord = 'inf' is a string, not np.inf"),
    ([[1.0, -2.5], [0.75, 4.0]], 0, "ord = 0"),
    ([[1.0, -2.5], [0.75, 4.0]], 3, "ord = 3"),
    ([[1.0, -2.5], [0.75, 4.0]], -1, "ord = -1"),
    ([[1.0, -2.5], [0.75, 4.0]], -np.inf, "ord = -np.inf"),
    ([[1.0, -2.5], [0.75, 4.0]], None, "ord = None"),
]


@pytest.mark.parametrize("A, ord, why", NORM_REFUSALS,
                         ids=["A-one-d", "A-three-d", "A-no-row", "A-no-column", "A-scalar", "ord-true", "ord-false",
                              "ord-fro", "ord-nuc", "ord-string-inf", "ord-zero", "ord-three", "ord-minus-one",
                              "ord-minus-inf", "ord-none"])
def test_operator_norm_refusals(rc, A, ord, why):
    _expect_error(ValueError, lambda: rc.operator_norm(A, ord), f"operator_norm({A!r}, {ord!r})", why)


# --- product_norms --------------------------------------------------------------------------------------------------

PRODUCT_HINT = "P_t = A_t ⋯ A_1: the new matrix multiplies on the LEFT (x_t = A_t x_{t-1} = P_t x_0)"


def _products_here(matrices, ord):
    """The norms of the cumulative products A_t ⋯ A_1 and the cumulative products of the norms, computed here."""
    P = np.eye(np.asarray(matrices[0]).shape[0])
    norms, bounds, bound = [], [], 1.0
    for A in matrices:
        A = np.asarray(A, dtype=float)
        P = A @ P
        bound *= float(np.linalg.norm(A, ord))
        norms.append(float(np.linalg.norm(P, ord)))
        bounds.append(bound)
    return np.array(norms), np.array(bounds)


def _check_pair(got, T, what):
    assert isinstance(got, tuple) and len(got) == 2, (
        f"expected a tuple (norms, bounds) for {what}, got {type(got).__name__}"
        + (f" of length {len(got)}" if isinstance(got, (tuple, list)) else ""))
    norms, bounds = got
    _float_array(norms, (T,), f"norms for {what} (one per product P_1, …, P_T)")
    _float_array(bounds, (T,), f"bounds for {what} (one per product P_1, …, P_T)")
    return norms, bounds


def test_product_norms_docstring_examples(rc):
    mats = [[[1, 1], [0, 1]], [[1, 0], [-1, 1]]]
    got = _result(lambda: rc.product_norms(mats), "(array([1.618, 1.618]), array([1.618, 2.618])) (rounded)",
                  "the first example of the docstring")
    norms, bounds = _check_pair(got, 2, "product_norms([[[1, 1], [0, 1]], [[1, 0], [-1, 1]]])")
    golden = (1 + math.sqrt(5)) / 2
    _close(norms, [golden, golden], "norms for the docstring example (ord 2)", rtol=1e-10, hint=PRODUCT_HINT)
    _close(bounds, [golden, golden ** 2], "bounds for the docstring example (ord 2)", rtol=1e-10,
           hint="bounds[t - 1] = ‖A_t‖ ⋯ ‖A_1‖, a cumulative product")
    got = _result(lambda: rc.product_norms(mats, ord=1), "(array([2., 2.]), array([2., 4.]))",
                  "the second example of the docstring")
    norms, bounds = _check_pair(got, 2, "product_norms([[[1, 1], [0, 1]], [[1, 0], [-1, 1]]], ord=1)")
    _close(norms, [2.0, 2.0], "norms for the docstring example with ord=1", rtol=0, atol=1e-15, hint=PRODUCT_HINT)
    _close(bounds, [2.0, 4.0], "bounds for the docstring example with ord=1", rtol=0, atol=1e-15)


PRODUCTS = [(2, 6, 2), (3, 10, 2), (4, 5, 1), (3, 8, np.inf), (2, 1, 1), (5, 4, np.inf), (3, 12, 1), (1, 7, 2)]


@pytest.mark.parametrize("n, T, ord", PRODUCTS, ids=[f"n{n}-T{T}-ord-{ORD_NAMES[o]}" for n, T, o in PRODUCTS])
def test_product_norms_match_the_products_computed_here(rc, n, T, ord):
    rng = np.random.default_rng(5650 + PRODUCTS.index((n, T, ord)))
    mats = [rng.normal(size=(n, n)) * (1.3 / math.sqrt(n)) for _ in range(T)]
    want_norms, want_bounds = _products_here(mats, ord)
    what = f"product_norms of {T} random {n} × {n} matrices, ord={ORD_NAMES[ord]}"
    got = _result(lambda: rc.product_norms(mats, ord=ord), f"two arrays of {T} floats", what)
    norms, bounds = _check_pair(got, T, what)
    _close(norms, want_norms, f"norms ‖A_t ⋯ A_1‖ for {what}", rtol=1e-10, atol=1e-12,
           hint=f"{PRODUCT_HINT}; {ORD_HINTS[ord]}")
    _close(bounds, want_bounds, f"bounds ‖A_t‖ ⋯ ‖A_1‖ for {what}", rtol=1e-10, atol=1e-12,
           hint=f"a cumulative product of the norms of the factors; {ORD_HINTS[ord]}")


def test_product_norms_order_of_the_product(rc):
    """A_1 keeps the first coordinate, A_2 sends it to the second: A_2 A_1 ≠ 0 but A_1 A_2 = 0. With random 3 × 3
    matrices too, the products A_t ⋯ A_1 and A_1 ⋯ A_t have different norms."""
    mats = [np.array([[1.0, 0.0], [0.0, 0.0]]), np.array([[0.0, 0.0], [-2.4, 0.0]])]
    for ord in ORDS:
        got = _result(lambda: rc.product_norms(mats, ord=ord), "([1, 2.4], [1, 2.4])", f"ord {ORD_NAMES[ord]}")
        norms, bounds = _check_pair(got, 2, f"A_1 = [[1, 0], [0, 0]], A_2 = [[0, 0], [-2.4, 0]], ord={ORD_NAMES[ord]}")
        _close(norms, [1.0, 2.4], f"norms for A_1 = [[1, 0], [0, 0]], A_2 = [[0, 0], [-2.4, 0]], ord={ORD_NAMES[ord]}",
               rtol=1e-12, atol=1e-15, hint=f"{PRODUCT_HINT}: P_2 = A_2 A_1 = [[0, 0], [-2.4, 0]], whereas A_1 A_2 = 0")
        _close(bounds, [1.0, 2.4], f"bounds for the same matrices, ord={ORD_NAMES[ord]}", rtol=1e-12, atol=1e-15)
    rng = np.random.default_rng(5665)
    mats = [rng.normal(size=(3, 3)) for _ in range(4)]
    for ord in ORDS:
        want, _ = _products_here(mats, ord)
        reverse, P = [], np.eye(3)
        for A in mats:
            P = P @ A                                                 # the other order, A_1 ⋯ A_t
            reverse.append(float(np.linalg.norm(P, ord)))
        assert np.all(np.abs(np.array(reverse[1:]) - want[1:]) > 1e-3 * want[1:])     # the two orders differ here
        got = _result(lambda: rc.product_norms(mats, ord=ord), "4 norms",
                      f"4 random 3 × 3 matrices, ord {ORD_NAMES[ord]}")
        norms, _ = _check_pair(got, 4, f"4 random 3 × 3 matrices, ord={ORD_NAMES[ord]}")
        _close(norms, want, f"norms ‖A_t ⋯ A_1‖ for 4 random 3 × 3 matrices, ord={ORD_NAMES[ord]}", rtol=1e-10,
               hint=PRODUCT_HINT + (" (your values are those of A_1 ⋯ A_t)"
                                    if np.allclose(norms, reverse, rtol=1e-10) else ""))


def test_product_norms_of_diagonal_matrices_and_rotations(rc):
    """Diagonal factors: ‖diag(d)‖ = max |d_i| for the three norms, and the bound can overestimate a lot
    (diag(3.2, 0.4) then diag(0.4, 3.2): the product is 1.28 I, the bound 3.2²). Rotations: ‖P_t‖₂ = 1 and the bound
    is 1; for ‖·‖₁, P_t is the rotation by θ_1 + … + θ_t, of norm |cos| + |sin| of that angle."""
    mats = [np.diag([3.2, 0.4]), np.diag([0.4, 3.2]), np.diag([3.2, 0.4])]
    for ord in ORDS:
        got = _result(lambda: rc.product_norms(mats, ord=ord), "([3.2, 1.28, 4.096], [3.2, 10.24, 32.768])",
                      f"diagonal matrices, ord {ORD_NAMES[ord]}")
        norms, bounds = _check_pair(got, 3, f"diag(3.2, 0.4), diag(0.4, 3.2), diag(3.2, 0.4), ord={ORD_NAMES[ord]}")
        _close(norms, [3.2, 1.28, 4.096], f"norms for diag(3.2, 0.4), diag(0.4, 3.2), diag(3.2, 0.4), "
                                          f"ord={ORD_NAMES[ord]} (the products are diagonal: max |product of the d_i|)",
               rtol=1e-12)
        _close(bounds, [3.2, 10.24, 32.768], f"bounds for the same matrices, ord={ORD_NAMES[ord]} (3.2, 3.2², 3.2³)",
               rtol=1e-12, hint="bounds[t - 1] = ‖A_t‖ ⋯ ‖A_1‖, a cumulative product")
    rng = np.random.default_rng(5666)
    angles = rng.uniform(-math.pi, math.pi, size=9)
    rotations = [np.array([[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]]) for a in angles]
    got = _result(lambda: rc.product_norms(rotations, ord=2), "ones", "9 rotations, ord 2")
    norms, bounds = _check_pair(got, 9, "9 rotations of the plane, ord=2")
    _close(norms, np.ones(9), "norms of products of 9 rotations, ord=2 (a rotation keeps the lengths)", rtol=1e-12)
    _close(bounds, np.ones(9), "bounds for 9 rotations, ord=2 (each ‖R‖₂ = 1)", rtol=1e-12)
    totals = np.cumsum(angles)
    got = _result(lambda: rc.product_norms(rotations, ord=1), "|cos| + |sin|", "9 rotations, ord 1")
    norms, bounds = _check_pair(got, 9, "9 rotations of the plane, ord=1")
    _close(norms, np.abs(np.cos(totals)) + np.abs(np.sin(totals)),
           "norms ‖·‖₁ of products of 9 rotations, |cos θ| + |sin θ| for θ = θ_1 + … + θ_t", rtol=1e-12)
    _close(bounds, np.cumprod(np.abs(np.cos(angles)) + np.abs(np.sin(angles))),
           "bounds ‖·‖₁ for 9 rotations, the cumulative product of |cos θ_s| + |sin θ_s|", rtol=1e-12)


def test_product_norms_never_exceed_their_bounds_and_bound_every_state(rc):
    """‖P_t‖ ≤ ‖A_t‖ ⋯ ‖A_1‖ (sub-multiplicativity), equality at t = 1 (P_1 = A_1), and ‖x_t‖ ≤ ‖P_t‖ ‖x_0‖ for the
    states x_t = A_t x_{t-1} computed here from random starts."""
    rng = np.random.default_rng(5667)
    for n, T in ((2, 9), (3, 7), (4, 6)):
        mats = [rng.normal(size=(n, n)) for _ in range(T)]
        starts = rng.normal(size=(20, n))
        for ord in ORDS:
            what = f"{T} random {n} × {n} matrices, ord={ORD_NAMES[ord]}"
            got = _result(lambda: rc.product_norms(mats, ord=ord), f"two arrays of {T} floats", what)
            norms, bounds = _check_pair(got, T, what)
            assert np.all(norms <= bounds * (1 + 1e-12)), (
                f"expected norms ≤ bounds for {what} (‖A_t ⋯ A_1‖ ≤ ‖A_t‖ ⋯ ‖A_1‖), got norms {_show(norms)} and "
                f"bounds {_show(bounds)}")
            _close_number(float(norms[0]), float(bounds[0]), f"norms[0] = bounds[0] = ‖A_1‖ for {what}")
            for x0 in starts:
                x = x0.copy()
                for t, A in enumerate(mats):
                    x = A @ x
                    assert np.linalg.norm(x, ord) <= norms[t] * np.linalg.norm(x0, ord) * (1 + 1e-12), (
                        f"expected ‖x_{t + 1}‖ ≤ ‖P_{t + 1}‖ ‖x_0‖ for x_t = A_t x_(t-1) ({what}), got "
                        f"‖x_{t + 1}‖ = {np.linalg.norm(x, ord):.10g} > {norms[t]:.10g} × "
                        f"{np.linalg.norm(x0, ord):.10g} "
                        f"({PRODUCT_HINT})")


def test_product_norms_with_one_matrix(rc):
    A = np.array([[0.35, -1.6, 0.8], [2.2, 0.15, -0.45], [-0.6, 1.15, 1.4]])
    for ord in ORDS:
        want = float(np.linalg.norm(A, ord))
        got = _result(lambda: rc.product_norms([A], ord=ord), f"([{want:.6g}], [{want:.6g}])",
                      f"T = 1, ord {ORD_NAMES[ord]}")
        norms, bounds = _check_pair(got, 1, f"a single matrix (T = 1), ord={ORD_NAMES[ord]}")
        _close(norms, [want], f"norms for a single matrix, [‖A_1‖], ord={ORD_NAMES[ord]}", rtol=1e-10,
               hint=ORD_HINTS[ord])
        _close(bounds, [want], f"bounds for a single matrix, [‖A_1‖], ord={ORD_NAMES[ord]}", rtol=1e-10)


def test_product_norms_take_lists_tuples_and_stacks_and_leave_them_alone(rc):
    ints = [[[2, -1], [0, 1]], [[1, 3], [-1, 0]], [[0, 1], [4, -2]]]
    want_norms, want_bounds = _products_here(ints, 1)
    for given, text in ((ints, "a list of lists of integers"), (np.array(ints), "a 3-D integer array (T, n, n)"),
                        (tuple(np.array(M) for M in ints), "a tuple of integer arrays")):
        got = _result(lambda: rc.product_norms(given, ord=1), "two arrays of 3 floats", text)
        norms, bounds = _check_pair(got, 3, f"product_norms({text}, ord=1)")
        _close(norms, want_norms, f"norms for {text}, ord=1", rtol=1e-12, hint=PRODUCT_HINT)
        _close(bounds, want_bounds, f"bounds for {text}, ord=1", rtol=1e-12)
    rng = np.random.default_rng(5668)
    mats = [rng.normal(size=(3, 3)) for _ in range(5)]
    stack = rng.normal(size=(4, 2, 2))
    copies, stack_copy = [M.copy() for M in mats], stack.copy()
    for ord in ORDS:
        got = _result(lambda: rc.product_norms(mats, ord=ord), "two arrays",
                      f"a list of float arrays, ord {ORD_NAMES[ord]}")
        norms, bounds = _check_pair(got, 5, f"a list of 5 float arrays, ord={ORD_NAMES[ord]}")
        for i, (M, copy) in enumerate(zip(mats, copies)):
            assert np.array_equal(M, copy), (
                f"expected the matrices unchanged by product_norms, got matrix {i} = {_show(M)} (never modify the "
                f"arrays you receive: P = A @ P makes a new array)")
        norms[:] = 99.0
        bounds[:] = 99.0
        assert all(np.array_equal(M, copy) for M, copy in zip(mats, copies)), (
            "expected product_norms to return new arrays, but changing them changed a matrix")
        got = _result(lambda: rc.product_norms(stack, ord=ord), "two arrays",
                      f"a 3-D float array, ord {ORD_NAMES[ord]}")
        _check_pair(got, 4, f"a 3-D float array of shape (4, 2, 2), ord={ORD_NAMES[ord]}")
        assert np.array_equal(stack, stack_copy), (
            f"expected the stack unchanged by product_norms, got {_show(stack)}")


PRODUCT_REFUSALS = [
    ([], 2, "no matrix"),
    ([[[1.25, -0.75, 0.0], [0.6, 2.0, 1.0]]], 2, "a 2 × 3 matrix is not square"),
    ([np.eye(2), np.eye(3)], 2, "the shapes (2, 2) and (3, 3) differ"),
    ([np.eye(2), np.ones((3, 2))], 1, "the second matrix is 3 × 2"),
    ([[1.25, -0.75], [0.6, 2.0]], 2, "a single 2-D matrix: each element of the sequence must be a matrix, not a row"),
    ([np.ones((2, 2, 2))], 2, "a 3-D element"),
    (4.5, 2, "a number, not a sequence of matrices"),
    ("matrices", 2, "a string"),
    ([np.eye(2), np.eye(2)], True, "ord = True: a bool is refused"),
    ([np.eye(2), np.eye(2)], "fro", "ord = 'fro' is not an induced norm"),
    ([np.eye(2), np.eye(2)], 0, "ord = 0"),
    ([np.eye(2), np.eye(2)], 3, "ord = 3"),
    ([np.eye(2), np.eye(2)], -np.inf, "ord = -np.inf"),
    ([np.eye(2), np.eye(2)], None, "ord = None"),
]


@pytest.mark.parametrize("matrices, ord, why", PRODUCT_REFUSALS,
                         ids=["empty", "not-square", "shapes-differ", "second-not-square", "one-matrix-not-a-list",
                              "three-d-element", "scalar", "string", "ord-true", "ord-fro", "ord-zero", "ord-three",
                              "ord-minus-inf", "ord-none"])
def test_product_norms_refusals(rc, matrices, ord, why):
    _expect_error(ValueError, lambda: rc.product_norms(matrices, ord=ord), f"product_norms({matrices!r}, ord={ord!r})",
                  why)
