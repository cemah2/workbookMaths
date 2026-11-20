"""Tests of mymath.positional (chapter MB3): the matrix of a Givens rotation of ℝⁿ, the state (m, l, acc) of an online
softmax read block by block, and the merge of two such states.

Oracles: the matrices of MML written by hand, the plane (3.76), the three rotations of space (3.77)–(3.79) and the
Givens rotation in blocks (3.80) and by its four entries (3.81); ``scipy.spatial.transform.Rotation`` (rotations about
the three axes, their compositions, the image of a vector); exact values of cos and sin by SymPy; for the online
softmax, ``scipy.special.logsumexp`` (m + ln l) and ``scipy.special.softmax`` (l = 1 / the weight of the largest
score, acc / l and the weights), and exact rational weights (``fractions``) for scores that are logarithms of fractions;
for the merge, the state of the union of the two sets of scores (``softmax`` again) and ``logsumexp`` with signed
weights for arbitrary states.
Never another function of yours. Plus properties: G orthogonal of determinant 1, G⁻¹ = Gᵀ = the rotation by -θ,
swapping i and j, e_i turned towards e_j and the other basis vectors fixed, angles that add in a plane, rotations in
disjoint planes that commute (a block-diagonal matrix), rotations in planes sharing a coordinate that do not, a
renumbering of the coordinates (PᵀGP); for the online softmax, the state after every block (the invariant), the
maximum that changes exactly at the records, the same final state for every block size, for a permutation of the
scores and the values, and up to m for a constant added to the scores, masked scores (-inf) and masked blocks, the
empty state of each kind, l ≥ 1 as soon as m is finite, large and very negative scores without overflow nor
underflow, no exponential of a positive number; for the merge, commutativity, associativity, the empty state of the
same kind as neutral element, far apart maxima; Python floats, new arrays, inputs left unchanged, and every refusal of
the docstrings. They describe the expected behaviour without showing the solution.

    pytest tests/test_mb3_positional.py              # your code
    pytest tests/test_mb3_positional.py --impl=ref   # the reference
"""

import ast
import inspect
import itertools
import math
import warnings
from fractions import Fraction

import numpy as np
import pytest
import sympy
from scipy import linalg, special
from scipy.spatial.transform import Rotation


@pytest.fixture
def pos_module(mymath_module):
    """The module itself: for the tests that check that your functions never write into the arrays they receive, that
    they never take the exponential of a positive number, and for the check of what the module uses."""
    return mymath_module("positional")


def _copied(value):
    """A copy of the NumPy arrays in value (also inside a tuple or a list: the states of the merge)."""
    if isinstance(value, np.ndarray):
        return value.copy()
    if isinstance(value, tuple):
        return tuple(_copied(v) for v in value)
    if isinstance(value, list):
        return [_copied(v) for v in value]
    return value


class _OnCopies:
    """The functions of the module, each called on copies of the NumPy arrays it receives. A function that writes into
    its inputs is then reported by the tests named …_not_modify_… (which call the module itself), instead of
    silently changing the arrays from which the other tests compute what they expect."""

    def __init__(self, module):
        self._module = module

    def __getattr__(self, name):
        function = getattr(self._module, name)

        def on_copies(*args, **kwargs):
            return function(*[_copied(a) for a in args], **{k: _copied(v) for k, v in kwargs.items()})

        return on_copies


@pytest.fixture
def pos(pos_module):
    return _OnCopies(pos_module)


def _text(hint):
    """A hint given as a text or as a function that computes it (only when a test fails)."""
    if not callable(hint):
        return hint
    try:
        return hint()
    except Exception:  # noqa: BLE001 - a hint must never hide the failure it explains
        return ""


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError (and any RuntimeWarning: an overflow, 0 / 0, inf - inf…) being
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
                        f"RuntimeWarning: {warning} (an overflow or an underflow of np.exp, -inf - (-inf) or 0 * inf "
                        f"is nan…" + (f"; {hint})" if hint else ")"))
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


def _show(v):
    """A short text for an array: more than 12 numbers show the first 12 (flattened), then « … »."""
    arr = np.asarray(v, dtype=float)
    if arr.size > 12:
        return np.array2string(arr.ravel()[:12], precision=6, suppress_small=True,
                               max_line_width=10_000).replace("]", " …]") + f" (shape {arr.shape})"
    return np.array2string(arr, precision=6, suppress_small=True, max_line_width=10_000).replace("\n", "")


def _show_any(v):
    """_show for something that may not be an array of numbers (a state, a list of states…)."""
    if isinstance(v, tuple) and len(v) == 3:
        return _show_state(v)
    if isinstance(v, list) and v and all(isinstance(s, tuple) and len(s) == 3 for s in v):
        shown = ", ".join(_show_state(s) for s in v[:4])
        return f"[{shown}{', …' if len(v) > 4 else ''}] ({len(v)} states)"
    try:
        return _show(v)
    except (TypeError, ValueError):
        return repr(v)


def _show_number(x):
    try:
        return f"{float(x):.12g}"
    except (TypeError, ValueError, OverflowError):
        return repr(x)


def _show_state(state):
    try:
        m, l, acc = state
    except (TypeError, ValueError):
        return repr(state)
    if acc is None:
        shown = "None"
    elif isinstance(acc, np.ndarray):
        try:
            shown = _show(acc)
        except (TypeError, ValueError):
            shown = repr(acc)
    else:
        shown = _show_number(acc)
    return f"({_show_number(m)}, {_show_number(l)}, {shown})"


def _same(got, value, rtol=1e-12, atol=0.0):
    """Whether got equals value: same shape, the same infinite entries (with their signs) and the finite ones close;
    nan never equals anything."""
    try:
        g = np.asarray(got, dtype=float)
        v = np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        return False
    if g.shape != v.shape or np.isnan(g).any() or np.isnan(v).any():
        return False
    if not (np.array_equal(np.isposinf(g), np.isposinf(v)) and np.array_equal(np.isneginf(g), np.isneginf(v))):
        return False
    finite = np.isfinite(v)
    return bool(np.allclose(g[finite], v[finite], rtol=rtol, atol=atol))


def _gap(got, want):
    """Why got differs from want, in a few words."""
    try:
        g = np.asarray(got, dtype=float)
        w = np.asarray(want, dtype=float)
    except (TypeError, ValueError):
        return ""
    if g.shape != w.shape:
        return f" (shape {g.shape} instead of {w.shape})"
    if np.isnan(g).any():
        return " (the result holds nan)"
    finite = np.isfinite(w) & np.isfinite(g)
    if finite.any():
        with np.errstate(all="ignore"):
            return f" (largest gap {float(np.max(np.abs(g[finite] - w[finite]))):.1e})"
    return ""


def _close(got, want, what, rtol=1e-12, atol=0.0, hint=""):
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


def _float_matrix(got, shape, what, hint=""):
    if isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape:
        return
    hint = _text(hint)
    pytest.fail(f"expected {what} as a numpy.ndarray of floats of shape {shape}, got {type(got).__name__}"
                + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray) else f" {got!r}")
                + (f" ({hint})" if hint else ""))


def _rng(seed, case=None):
    """The generator of a test (seeds 7200 to 7290), one stream per case of a parametrized test."""
    return np.random.default_rng(seed if case is None else (seed, case))


# --- what the module may use ----------------------------------------------------------------------------------------

def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``logsumexp`` (from scipy.special import logsumexp) → "scipy.special.logsumexp"."""
    names = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname:
                    names[alias.asname] = alias.name
                else:                                     # import scipy.special binds the name scipy
                    names[alias.name.split(".")[0]] = alias.name.split(".")[0]
        elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
            for alias in node.names:
                names[alias.asname or alias.name] = f"{node.module}.{alias.name}"
    return names


def _where(statement):
    return statement.name if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)) else "the module level"


def _uses(tree, names):
    """Each use of an imported name (or of a chain of attributes on it): (where, dotted path), e.g.
    ("online_softmax", "scipy.special.logsumexp"); ``where`` is the top-level function, or "the module level"."""
    inner = {id(node.value) for node in ast.walk(tree) if isinstance(node, ast.Attribute)}
    uses = []
    for statement in tree.body:
        where = _where(statement)
        for node in ast.walk(statement):
            if not isinstance(node, (ast.Name, ast.Attribute)) or id(node) in inner:
                continue                                  # only the whole chain scipy.special.softmax
            attrs = []
            while isinstance(node, ast.Attribute):
                attrs.append(node.attr)
                node = node.value
            if isinstance(node, ast.Name) and node.id in names:
                uses.append((where, ".".join([names[node.id]] + attrs[::-1])))
    return uses


FORBIDDEN_STRINGS = {"logaddexp", "special", "softmax", "logsumexp", "spatial", "transform", "Rotation"}


def _string_uses(tree):
    """getattr(np, "logaddexp") and the like, and __import__("scipy") or importlib.import_module("scipy…"): a forbidden
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
            if name in ("__import__", "import_module") and any(t.startswith("scipy") for t in texts):
                found.append(f"{name}({texts[0]!r}) in {where}")
    return found


def test_module_uses_numpy_and_math_but_no_scipy_nor_logaddexp(pos_module):
    """The docstring allows NumPy and the module math, but no SciPy at all (scipy.special.softmax and logsumexp would do
    the online softmax, scipy.spatial.transform.Rotation the rotations) and not np.logaddexp: the tests compare your
    results with them. Only the code counts: a comment, a docstring or an import never used is not a use."""
    try:
        tree = ast.parse(inspect.getsource(pos_module))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = []
    for where, path in _uses(tree, _imported_names(tree)):
        parts = path.split(".")
        if parts[0] == "scipy":
            found.append(f"{path} in {where}")
        elif parts[0] == "numpy" and len(parts) > 1 and parts[1] == "logaddexp":
            found.append(f"np.{'.'.join(parts[1:])} in {where}")
    found += _string_uses(tree)
    assert not found, (f"expected NumPy and math only, with no SciPy and no np.logaddexp, found {sorted(set(found))} "
                       f"(the tests compare your results with scipy.special.softmax, logsumexp and "
                       f"scipy.spatial.transform.Rotation: np.eye, math.cos, math.sin, np.exp, math.exp, max and the "
                       f"@ product are enough)")


# --- givens_rotation ------------------------------------------------------------------------------------------------

GIVENS_HINT = ("start from the identity np.eye(n) (floats) and change four entries only: G[i, i] = G[j, j] = cos θ, "
               "G[j, i] = sin θ (row j, column i) and G[i, j] = -sin θ, θ in radians and indices from 0; then the "
               "column i is G e_i = cos θ e_i + sin θ e_j")


def _mml_3_80(n, i, j, theta):
    """MML (3.80) for 0-based i < j: the blocks I_i, the 2 × 2 rotation spread on the rows and columns i and j,
    I_{j-i-1} between them and I_{n-j-1} after them."""
    c, s = math.cos(theta), math.sin(theta)
    a, b, e = i, j - i - 1, n - j - 1

    def zeros(rows, columns):
        return np.zeros((rows, columns))

    def one(x):
        return np.full((1, 1), x)

    return np.block([[np.eye(a), zeros(a, 1), zeros(a, b), zeros(a, 1), zeros(a, e)],
                     [zeros(1, a), one(c), zeros(1, b), one(-s), zeros(1, e)],
                     [zeros(b, a), zeros(b, 1), np.eye(b), zeros(b, 1), zeros(b, e)],
                     [zeros(1, a), one(s), zeros(1, b), one(c), zeros(1, e)],
                     [zeros(e, a), zeros(e, 1), zeros(e, b), zeros(e, 1), np.eye(e)]])


def _mml_3_81(n, i, j, theta):
    """MML (3.81), 0-based: the identity with r_ii = r_jj = cos θ, r_ij = -sin θ, r_ji = sin θ for i < j; for i > j,
    the rotation of MML in the plane (j, i) by -θ (swapping i and j changes θ into -θ)."""
    if i > j:
        return _mml_3_81(n, j, i, -theta)
    R = np.eye(n)
    R[i, i] = R[j, j] = math.cos(theta)
    R[i, j] = -math.sin(theta)
    R[j, i] = math.sin(theta)
    return R


def _mml_3_76(theta):
    return np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])


def _mml_3_77_to_3_79(axis, theta):
    """R₁(θ), R₂(θ) and R₃(θ) of MML (3.77)–(3.79), the rotations about e₁, e₂ and e₃ (axis 0, 1, 2 here)."""
    c, s = math.cos(theta), math.sin(theta)
    return [np.array([[1, 0, 0], [0, c, -s], [0, s, c]]),
            np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]]),
            np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])][axis]


def _givens_candidates(n, i, j, theta):
    """The right matrix and the matrices of classic errors, with their explanation."""
    want = _mml_3_81(n, i, j, theta)
    candidates = [(want.T, "G[j, i] = sin θ and G[i, j] = -sin θ: here the two sines are swapped, which is the "
                           "rotation by -θ (G e_i must be cos θ e_i + sin θ e_j)"),
                  (_mml_3_81(n, i, j, math.radians(theta)), "θ is in radians: math.cos(theta), not of "
                                                             "math.radians(theta)"),
                  (_mml_3_81(n, i, j, math.degrees(theta)), "θ is in radians: no conversion to degrees")]
    swapped = np.eye(n)
    swapped[i, i] = swapped[j, j] = math.sin(theta)
    swapped[j, i], swapped[i, j] = math.cos(theta), -math.cos(theta)
    candidates.append((swapped, "cos θ on the diagonal (G[i, i] and G[j, j]), sin θ off the diagonal"))
    bare = want.copy()
    bare[np.eye(n, dtype=bool) & (want == 1)] = 0.0
    candidates.append((bare, "start from the identity: the n - 2 other basis vectors are fixed (1 on the diagonal)"))
    half = want.copy()
    half[j, j] = 1.0
    candidates.append((half, "G[j, j] = cos θ too (both diagonal entries of the plane)"))
    if max(i, j) + 1 < n:
        candidates.append((_mml_3_81(n, i + 1, j + 1, theta), "indices start at 0: the plane of the coordinates i and "
                                                              "j, not i + 1 and j + 1"))
    if min(i, j) >= 1:
        candidates.append((_mml_3_81(n, i - 1, j - 1, theta), "indices start at 0 here, as in NumPy: do not subtract "
                                                              "1 (MML numbers from 1, the code from 0)"))
    return want, candidates


def _givens_hint(got, n, i, j, theta):
    try:
        g = np.asarray(got, dtype=float)
        want, candidates = _givens_candidates(n, i, j, theta)
    except (TypeError, ValueError):
        return GIVENS_HINT
    text = _first_match(g, want, candidates, rtol=1e-9, atol=1e-12)
    return f"{GIVENS_HINT}; here {text}" if text else GIVENS_HINT


def _givens(pos, n, i, j, theta, what=None):
    """givens_rotation(n, i, j, theta), its type and shape checked."""
    what = what or f"givens_rotation({n!r}, {i!r}, {j!r}, {theta!r})"
    got = _result(lambda: pos.givens_rotation(n, i, j, theta), "a numpy.ndarray of floats (the rotation matrix)",
                  what, GIVENS_HINT)
    size = int(n)
    _float_matrix(got, (size, size), what, lambda: _givens_hint(got, size, int(i), int(j), float(theta)))
    return got


def _check_givens(got, want, n, i, j, theta, what, atol=1e-15):
    _close(got, want, what, rtol=0, atol=atol, hint=lambda: _givens_hint(got, n, i, j, theta))


BLOCK_CASES = [(2, 0, 1), (3, 0, 1), (3, 0, 2), (3, 1, 2), (4, 0, 3), (4, 2, 3), (5, 1, 4), (5, 0, 2), (6, 2, 3),
               (7, 0, 6), (8, 3, 5), (9, 1, 7)]


@pytest.mark.parametrize("n, i, j", BLOCK_CASES, ids=[f"n{n}-plane-{i}-{j}" for n, i, j in BLOCK_CASES])
def test_givens_rotation_is_mml_3_80_in_blocks(pos, n, i, j):
    """For i < j (0-based), the matrix of MML (3.80): I_i, then the rotation spread on the rows and columns i and j,
    I_{j-i-1} between them and I_{n-j-1} after them; R_ij(θ) of MML is givens_rotation(n, i - 1, j - 1, θ)."""
    rng = _rng(7200, BLOCK_CASES.index((n, i, j)))
    for theta in rng.uniform(-math.pi, math.pi, size=3).tolist() + [float(rng.uniform(4, 11))]:
        got = _givens(pos, n, i, j, theta)
        _check_givens(got, _mml_3_80(n, i, j, theta), n, i, j, theta,
                      f"givens_rotation({n}, {i}, {j}, {theta!r}) (MML (3.80): R_{i + 1}{j + 1}(θ) of ℝ^{n})")


SWAP_CASES = [(2, 1, 0), (3, 2, 1), (3, 1, 0), (4, 3, 0), (5, 4, 2), (6, 5, 1), (8, 6, 3)]


@pytest.mark.parametrize("n, i, j", SWAP_CASES, ids=[f"n{n}-plane-{i}-{j}" for n, i, j in SWAP_CASES])
def test_givens_rotation_with_i_greater_than_j_is_mml_3_81_by_minus_theta(pos, n, i, j):
    """i > j is allowed: the matrix still has G[i, i] = G[j, j] = cos θ, G[j, i] = sin θ, G[i, j] = -sin θ, so it is
    the rotation of MML (3.81) in the plane (j, i) by -θ."""
    rng = _rng(7201, SWAP_CASES.index((n, i, j)))
    for theta in rng.uniform(-2.0 * math.pi, 2.0 * math.pi, size=3).tolist():
        got = _givens(pos, n, i, j, theta)
        _check_givens(got, _mml_3_81(n, j, i, -theta), n, i, j, theta,
                      f"givens_rotation({n}, {i}, {j}, {theta!r}) (MML (3.81) in the plane ({j}, {i}) by -θ)")


def test_givens_rotation_in_the_plane_is_mml_3_76(pos):
    """n = 2: givens_rotation(2, 0, 1, θ) is R(θ) of MML (3.76), and givens_rotation(2, 1, 0, θ) is R(-θ)."""
    rng = _rng(7202)
    for theta in rng.uniform(-7.0, 7.0, size=6).tolist():
        got = _givens(pos, 2, 0, 1, theta)
        _check_givens(got, _mml_3_76(theta), 2, 0, 1, theta, f"givens_rotation(2, 0, 1, {theta!r}) (MML (3.76))")
        got = _givens(pos, 2, 1, 0, theta)
        _check_givens(got, _mml_3_76(-theta), 2, 1, 0, theta,
                      f"givens_rotation(2, 1, 0, {theta!r}) (R(-θ) of MML (3.76))")


# the rotation about the axis k of ℝ³ turns e_{k+1} towards e_{k+2} (indices mod 3): x: (1, 2), y: (2, 0), z: (0, 1)
AXES = [("x", 0, 1, 2), ("y", 1, 2, 0), ("z", 2, 0, 1)]


@pytest.mark.parametrize("name, axis, i, j", AXES, ids=["about-x", "about-y", "about-z"])
def test_givens_rotation_of_space_are_mml_3_77_to_3_79_and_scipy_rotations(pos, name, axis, i, j):
    """In ℝ³, the rotation by θ about the axis e_k turns e_{k+1} towards e_{k+2} (indices mod 3): it is
    givens_rotation(3, k + 1, k + 2, θ), R₁, R₂ or R₃ of MML (3.77)–(3.79), Rotation.from_euler(axis, θ) and
    Rotation.from_rotvec(θ e_k) of scipy.spatial.transform."""
    rng = _rng(7203, axis)
    for theta in rng.uniform(-math.pi, math.pi, size=4).tolist():
        what = f"givens_rotation(3, {i}, {j}, {theta!r}) (the rotation about the axis {name})"
        got = _givens(pos, 3, i, j, theta, what)
        _check_givens(got, _mml_3_77_to_3_79(axis, theta), 3, i, j, theta, f"{what} (MML R_{axis + 1}(θ))")
        _check_givens(got, Rotation.from_euler(name, theta).as_matrix(), 3, i, j, theta,
                      f"{what} (scipy Rotation.from_euler({name!r}, θ))", atol=1e-14)
        e = np.zeros(3)
        e[axis] = theta
        _check_givens(got, Rotation.from_rotvec(e).as_matrix(), 3, i, j, theta,
                      f"{what} (scipy Rotation.from_rotvec(θ e_{axis}))", atol=1e-14)


def test_givens_rotation_compositions_match_scipy_rotations(pos):
    """Three rotations about x, then y, then z (fixed axes): R_z(c) R_y(b) R_x(a) is Rotation.from_euler("xyz",
    [a, b, c]); in the other order, R_x(a) R_y(b) R_z(c) is Rotation.from_euler("XYZ", [a, b, c]) (moving axes). The
    two differ: rotations of space do not commute. The image of a vector is Rotation.apply."""
    rng = _rng(7204)
    for k in range(6):
        a, b, c = rng.uniform(-math.pi, math.pi, size=3).tolist()
        Rx = _givens(pos, 3, 1, 2, a)
        Ry = _givens(pos, 3, 2, 0, b)
        Rz = _givens(pos, 3, 0, 1, c)
        what = (f"givens_rotation(3, 0, 1, {c!r}) @ givens_rotation(3, 2, 0, {b!r}) @ givens_rotation(3, 1, 2, {a!r}) "
                f"(about x, then y, then z)")
        _close(Rz @ Ry @ Rx, Rotation.from_euler("xyz", [a, b, c]).as_matrix(),
               f"{what} (scipy Rotation.from_euler('xyz', [a, b, c]))", rtol=0, atol=1e-14, hint=GIVENS_HINT)
        what = (f"givens_rotation(3, 1, 2, {a!r}) @ givens_rotation(3, 2, 0, {b!r}) @ givens_rotation(3, 0, 1, {c!r}) "
                f"(the other order)")
        _close(Rx @ Ry @ Rz, Rotation.from_euler("XYZ", [a, b, c]).as_matrix(),
               f"{what} (scipy Rotation.from_euler('XYZ', [a, b, c]))", rtol=0, atol=1e-14, hint=GIVENS_HINT)
        v = rng.normal(size=3) * 3.0
        _close(Rz @ Ry @ Rx @ v, Rotation.from_euler("xyz", [a, b, c]).apply(v),
               f"the image of v = {_show(v)} by the rotations about x, then y, then z (scipy Rotation.apply)",
               rtol=0, atol=1e-13, hint=GIVENS_HINT)


EXACT_ANGLES = [(1, 5), (2, 5), (3, 8), (5, 12), (7, 10), (-3, 5), (1, 2), (1, 1), (-5, 8), (11, 12)]


@pytest.mark.parametrize("p, q", EXACT_ANGLES, ids=[f"{p}pi-over-{q}" for p, q in EXACT_ANGLES])
def test_givens_rotation_exact_values_by_sympy(pos, p, q):
    """θ = pπ/q: cos θ and sin θ computed exactly by SymPy (radicals for π/5, 3π/8, 5π/12…), at 40 digits."""
    rng = _rng(7205, EXACT_ANGLES.index((p, q)))
    n = int(rng.integers(2, 7))
    i, j = (int(x) for x in rng.choice(n, size=2, replace=False))
    angle = sympy.pi * sympy.Rational(p, q)
    c, s = float(sympy.cos(angle).evalf(40)), float(sympy.sin(angle).evalf(40))
    want = np.eye(n)
    want[i, i] = want[j, j] = c
    want[j, i], want[i, j] = s, -s
    theta = p * math.pi / q
    got = _givens(pos, n, i, j, theta)
    _check_givens(got, want, n, i, j, theta, f"givens_rotation({n}, {i}, {j}, {p}π/{q}) (cos θ = {sympy.cos(angle)}, "
                  f"sin θ = {sympy.sin(angle)}, by SymPy)", atol=2e-15)


def test_givens_rotation_turns_e_i_towards_e_j_and_fixes_the_other_basis_vectors(pos):
    """G e_i = cos θ e_i + sin θ e_j, G e_j = -sin θ e_i + cos θ e_j, and G e_k = e_k exactly for the n - 2 others;
    G x changes the coordinates i and j only: (x_i, x_j) → (x_i cos θ - x_j sin θ, x_i sin θ + x_j cos θ)."""
    rng = _rng(7206)
    for k in range(10):
        n = int(rng.integers(2, 10))
        i, j = (int(x) for x in rng.choice(n, size=2, replace=False))
        theta = float(rng.uniform(-4.0, 4.0))
        got = _givens(pos, n, i, j, theta)
        c, s = math.cos(theta), math.sin(theta)
        I = np.eye(n)
        what = f"givens_rotation({n}, {i}, {j}, {theta!r})"
        _close(got @ I[i], c * I[i] + s * I[j], f"G e_{i} for G = {what} (cos θ e_{i} + sin θ e_{j})", rtol=0,
               atol=1e-15, hint=lambda: _givens_hint(got, n, i, j, theta))
        _close(got @ I[j], -s * I[i] + c * I[j], f"G e_{j} for G = {what} (-sin θ e_{i} + cos θ e_{j})", rtol=0,
               atol=1e-15, hint=lambda: _givens_hint(got, n, i, j, theta))
        others = [m for m in range(n) if m not in (i, j)]
        moved = [m for m in others if not np.array_equal(got[:, m], I[m]) or not np.array_equal(got[m, :], I[m])]
        assert not moved, (f"expected the rows and columns {others} of {what} to be those of the identity (the other "
                           f"basis vectors are fixed), got changes in {moved} ({_givens_hint(got, n, i, j, theta)})")
        x = rng.normal(size=n) * 5.0
        want = x.copy()
        want[i], want[j] = c * x[i] - s * x[j], s * x[i] + c * x[j]
        _close(got @ x, want, f"G x for G = {what} and x = {_show(x)}", rtol=0, atol=1e-13,
               hint=lambda: _givens_hint(got, n, i, j, theta))


def test_givens_rotation_is_orthogonal_of_determinant_1_and_keeps_lengths_and_angles(pos):
    """G Gᵀ = Gᵀ G = I, det G = 1 (np.linalg.det), ‖G x‖ = ‖x‖ and (G x)·(G y) = x·y (MML §3.9.4)."""
    rng = _rng(7207)
    for k in range(10):
        n = int(rng.integers(2, 12))
        i, j = (int(x) for x in rng.choice(n, size=2, replace=False))
        theta = float(rng.uniform(-10.0, 10.0))
        what = f"givens_rotation({n}, {i}, {j}, {theta!r})"
        got = _givens(pos, n, i, j, theta)
        hint = lambda: _givens_hint(got, n, i, j, theta)                   # noqa: E731
        _close(got @ got.T, np.eye(n), f"G Gᵀ for G = {what} (the identity)", rtol=0, atol=1e-15, hint=hint)
        _close(got.T @ got, np.eye(n), f"Gᵀ G for G = {what} (the identity)", rtol=0, atol=1e-15, hint=hint)
        _close(np.linalg.det(got), 1.0, f"det G for G = {what} (a rotation, not a reflection)", rtol=0, atol=1e-14,
               hint=hint)
        x, y = rng.normal(size=n), rng.normal(size=n)
        _close(np.linalg.norm(got @ x), np.linalg.norm(x), f"‖G x‖ for G = {what} (‖x‖)", rtol=1e-14, atol=0,
               hint=hint)
        _close((got @ x) @ (got @ y), x @ y, f"(G x)·(G y) for G = {what} (x·y)", rtol=0, atol=1e-13, hint=hint)


def test_givens_rotation_inverse_is_the_transpose_and_the_rotation_by_minus_theta(pos):
    """G(-θ) = G(θ)ᵀ and G(θ) G(-θ) = I; swapping i and j transposes: G(n, j, i, θ) = G(n, i, j, θ)ᵀ =
    G(n, i, j, -θ)."""
    rng = _rng(7208)
    for k in range(8):
        n = int(rng.integers(2, 9))
        i, j = (int(x) for x in rng.choice(n, size=2, replace=False))
        theta = float(rng.uniform(-5.0, 5.0))
        G = _givens(pos, n, i, j, theta)
        what = f"givens_rotation({n}, {i}, {j}, {-theta!r}) (the rotation by -θ)"
        back = _givens(pos, n, i, j, -theta, what)
        _close(back, G.T, f"{what} (the transpose of givens_rotation({n}, {i}, {j}, {theta!r}))", rtol=0, atol=1e-15,
               hint=lambda: _givens_hint(back, n, i, j, -theta))
        _close(G @ back, np.eye(n), f"givens_rotation({n}, {i}, {j}, θ) @ {what} for θ = {theta!r} (the identity)",
               rtol=0, atol=1e-15, hint=GIVENS_HINT)
        what = f"givens_rotation({n}, {j}, {i}, {theta!r}) (i and j swapped)"
        swapped = _givens(pos, n, j, i, theta, what)
        _close(swapped, G.T, f"{what} (the transpose of givens_rotation({n}, {i}, {j}, {theta!r}))", rtol=0,
               atol=1e-15, hint=lambda: _givens_hint(swapped, n, j, i, theta))


def test_givens_rotation_angles_add_in_the_same_plane(pos):
    """In the same plane, G(α) G(β) = G(α + β) = G(β) G(α): the addition formulas, written in matrices."""
    rng = _rng(7209)
    for k in range(8):
        n = int(rng.integers(2, 8))
        i, j = (int(x) for x in rng.choice(n, size=2, replace=False))
        alpha, beta = rng.uniform(-3.5, 3.5, size=2).tolist()
        A, B = _givens(pos, n, i, j, alpha), _givens(pos, n, i, j, beta)
        what = f"givens_rotation({n}, {i}, {j}, {alpha + beta!r}) (α + β for α = {alpha!r}, β = {beta!r})"
        S = _givens(pos, n, i, j, alpha + beta, what)
        _close(A @ B, S, f"G(α) G(β) in the plane ({i}, {j}) of ℝ^{n} ({what})", rtol=0, atol=1e-14, hint=GIVENS_HINT)
        _close(B @ A, S, f"G(β) G(α) in the plane ({i}, {j}) of ℝ^{n} ({what})", rtol=0, atol=1e-14, hint=GIVENS_HINT)


def test_givens_rotation_periodic_and_special_angles(pos):
    """θ = 0 gives the identity exactly; θ + 2π the same matrix (up to rounding); θ = π changes x_i and x_j into their
    opposites; θ = π/2 sends e_i onto e_j and e_j onto -e_i."""
    rng = _rng(7210)
    for k in range(5):
        n = int(rng.integers(2, 8))
        i, j = (int(x) for x in rng.choice(n, size=2, replace=False))
        got = _givens(pos, n, i, j, 0.0)
        assert np.array_equal(got, np.eye(n)), (f"expected givens_rotation({n}, {i}, {j}, 0.0) to be the identity "
                                                f"exactly, got {_show(got)} ({GIVENS_HINT})")
        theta = float(rng.uniform(-3.0, 3.0))
        G = _givens(pos, n, i, j, theta)
        for turns in (1, -2):
            what = f"givens_rotation({n}, {i}, {j}, {theta + 2 * turns * math.pi!r}) (θ + {2 * turns}π)"
            got = _givens(pos, n, i, j, theta + 2 * turns * math.pi, what)
            _close(got, G, f"{what} (givens_rotation({n}, {i}, {j}, {theta!r}))", rtol=0, atol=1e-14, hint=GIVENS_HINT)
        flip = np.eye(n)
        flip[i, i] = flip[j, j] = -1.0
        got = _givens(pos, n, i, j, math.pi)
        _check_givens(got, flip, n, i, j, math.pi, f"givens_rotation({n}, {i}, {j}, π) (x_{i} and x_{j} change sign)")
        quarter = np.eye(n)
        quarter[i, i] = quarter[j, j] = 0.0
        quarter[j, i], quarter[i, j] = 1.0, -1.0
        got = _givens(pos, n, i, j, math.pi / 2)
        _check_givens(got, quarter, n, i, j, math.pi / 2,
                      f"givens_rotation({n}, {i}, {j}, π/2) (e_{i} ↦ e_{j}, e_{j} ↦ -e_{i})")


DISJOINT_CASES = [(4, (0, 1), (2, 3)), (4, (2, 0), (3, 1)), (5, (0, 3), (4, 1)), (6, (5, 2), (0, 4)),
                  (7, (1, 6), (3, 2))]


@pytest.mark.parametrize("n, first, second", DISJOINT_CASES,
                         ids=[f"n{n}-{a}{b}-{c}{d}" for n, (a, b), (c, d) in DISJOINT_CASES])
def test_givens_rotation_in_disjoint_planes_commute(pos, n, first, second):
    """Two rotations in planes with no common coordinate commute, and their product turns each plane by its own angle:
    the identity with the four entries of each plane (for the planes (0, 1) and (2, 3) of ℝ⁴, the block-diagonal
    matrix of scipy.linalg.block_diag)."""
    rng = _rng(7211, DISJOINT_CASES.index((n, first, second)))
    for k in range(3):
        a, b = rng.uniform(-math.pi, math.pi, size=2).tolist()
        A, B = _givens(pos, n, *first, a), _givens(pos, n, *second, b)
        what = (f"givens_rotation({n}, {first[0]}, {first[1]}, {a!r}) @ givens_rotation({n}, {second[0]}, "
                f"{second[1]}, {b!r})")
        want = _mml_3_81(n, *first, a) @ _mml_3_81(n, *second, b)
        both = np.eye(n)
        for (i, j), theta in ((first, a), (second, b)):
            both[i, i] = both[j, j] = math.cos(theta)
            both[j, i], both[i, j] = math.sin(theta), -math.sin(theta)
        assert np.allclose(want, both, rtol=0, atol=1e-15), "expected the two oracles to agree"
        _close(A @ B, both, f"{what} (each plane turned by its angle)", rtol=0, atol=1e-15, hint=GIVENS_HINT)
        _close(B @ A, both, f"{what}, in the other order (disjoint planes: they commute)", rtol=0, atol=1e-15,
               hint=GIVENS_HINT)
        if (n, first, second) == (4, (0, 1), (2, 3)):
            _close(A @ B, linalg.block_diag(_mml_3_76(a), _mml_3_76(b)), f"{what} (scipy.linalg.block_diag(R(a), "
                   f"R(b)))", rtol=0, atol=1e-15, hint=GIVENS_HINT)


def test_givens_rotation_in_planes_sharing_a_coordinate_do_not_commute(pos):
    """Two rotations of ℝⁿ (n ≥ 3) in planes that share one coordinate do not commute (for angles that are not
    multiples of π): G₁ G₂ ≠ G₂ G₁; in ℝ³, both products are those of scipy (a composition of two Rotation)."""
    rng = _rng(7212)
    for k in range(8):
        n = int(rng.integers(3, 8))
        p, q, r = (int(x) for x in rng.choice(n, size=3, replace=False))
        a, b = rng.uniform(0.3, 2.8, size=2) * rng.choice([-1, 1], size=2)
        a, b = float(a), float(b)
        A, B = _givens(pos, n, p, q, a), _givens(pos, n, q, r, b)
        names = (f"givens_rotation({n}, {p}, {q}, {a!r})", f"givens_rotation({n}, {q}, {r}, {b!r})")
        _close(A @ B, _mml_3_81(n, p, q, a) @ _mml_3_81(n, q, r, b), f"{names[0]} @ {names[1]}", rtol=0, atol=1e-15,
               hint=GIVENS_HINT)
        _close(B @ A, _mml_3_81(n, q, r, b) @ _mml_3_81(n, p, q, a), f"{names[1]} @ {names[0]}", rtol=0, atol=1e-15,
               hint=GIVENS_HINT)
        assert np.max(np.abs(A @ B - B @ A)) > 1e-3, (
            f"expected {names[0]} and {names[1]} not to commute (the planes ({p}, {q}) and ({q}, {r}) share the "
            f"coordinate {q}), got equal products ({GIVENS_HINT})")
    for (name1, axis1, i1, j1), (name2, axis2, i2, j2) in itertools.permutations(AXES, 2):
        a, b = rng.uniform(0.3, 2.8, size=2).tolist()
        A, B = _givens(pos, 3, i1, j1, a), _givens(pos, 3, i2, j2, b)
        want = (Rotation.from_euler(name1, a) * Rotation.from_euler(name2, b)).as_matrix()
        _close(A @ B, want, f"givens_rotation(3, {i1}, {j1}, {a!r}) @ givens_rotation(3, {i2}, {j2}, {b!r}) (scipy "
               f"Rotation.from_euler({name1!r}, a) * Rotation.from_euler({name2!r}, b))", rtol=0, atol=1e-14,
               hint=GIVENS_HINT)


def test_givens_rotation_renumbering_the_coordinates_moves_the_plane(pos):
    """For the permutation matrix P with P e_k = e_π(k) (M16), Pᵀ G P is the same rotation in the plane of the
    coordinates π⁻¹(i) and π⁻¹(j): Pᵀ givens_rotation(n, i, j, θ) P = givens_rotation(n, π⁻¹(i), π⁻¹(j), θ)."""
    rng = _rng(7213)
    for k in range(8):
        n = int(rng.integers(3, 9))
        perm = rng.permutation(n)
        P = np.zeros((n, n))
        P[perm, np.arange(n)] = 1.0
        inverse = np.argsort(perm)
        i, j = (int(x) for x in rng.choice(n, size=2, replace=False))
        theta = float(rng.uniform(-math.pi, math.pi))
        G = _givens(pos, n, i, j, theta)
        a, b = int(inverse[i]), int(inverse[j])
        what = f"givens_rotation({n}, {a}, {b}, {theta!r})"
        got = _givens(pos, n, a, b, theta, what)
        _close(P.T @ G @ P, got, f"Pᵀ givens_rotation({n}, {i}, {j}, {theta!r}) P for π = {perm.tolist()} ({what}, the "
               f"plane (π⁻¹({i}), π⁻¹({j})) = ({a}, {b}))", rtol=0, atol=1e-15, hint=GIVENS_HINT)
        _close(got, _mml_3_81(n, a, b, theta), what, rtol=0, atol=1e-15, hint=lambda: _givens_hint(got, n, a, b, theta))


@pytest.mark.parametrize("n, i, j, theta, text", [
    (np.int64(5), np.int64(3), np.int32(1), -0.85, "NumPy integers"),
    (6, 4, 0, 3, "an integer angle"),
    (3, 0, 2, np.float32(0.75), "an np.float32 angle"),
    (4, 2, 1, np.float64(-2.2), "an np.float64 angle"),
    (np.int32(2), 1, np.int64(0), np.int64(-4), "NumPy integers everywhere"),
    (60, 47, 12, 1.05, "a large dimension"),
], ids=["numpy-ints", "int-angle", "float32-angle", "float64-angle", "all-numpy", "large-n"])
def test_givens_rotation_accepts_numpy_integers_and_any_finite_real_angle(pos, n, i, j, theta, text):
    what = f"givens_rotation({n!r}, {i!r}, {j!r}, {theta!r}) ({text})"
    got = _givens(pos, n, i, j, theta, what)
    _check_givens(got, _mml_3_81(int(n), int(i), int(j), float(theta)), int(n), int(i), int(j), float(theta), what)


GIVENS_REFUSALS = [
    ((1, 0, 0, 0.35), "n = 1: no plane"), ((0, 0, 1, 0.35), "n = 0"), ((-3, 0, 1, 0.35), "n is negative"),
    ((3.0, 0, 1, 0.35), "n is the float 3.0, not an integer"), ((np.float64(4.0), 0, 1, 0.35), "n is np.float64(4.0)"),
    ((2.75, 0, 1, 0.35), "n is 2.75"), ((True, 0, 1, 0.35), "n is True, a bool"), (("4", 0, 1, 0.35), "n is a string"),
    ((None, 0, 1, 0.35), "n is None"),
    ((3, 1, 1, 0.35), "i = j: no plane"), ((5, 4, 4, 0.35), "i = j = 4"),
    ((4, 0, 4, 0.35), "j = n is out of [0, n - 1]"), ((4, 5, 1, 0.35), "i = 5 is out of [0, 3]"),
    ((4, -1, 2, 0.35), "i = -1 is negative (no Python negative index)"), ((3, 0, -3, 0.35), "j = -3 is negative"),
    ((4, 1.0, 2, 0.35), "i is the float 1.0"), ((4, 0, np.float64(2.0), 0.35), "j is np.float64(2.0)"),
    ((3, True, 2, 0.35), "i is True, a bool (not an integer here, as for n)"),
    ((3, 2, False, 0.35), "j is False, a bool"), ((3, "0", 2, 0.35), "i is a string"),
    ((3, 0, None, 0.35), "j is None"),
    ((3, 0, 1, math.nan), "θ is nan"), ((3, 0, 1, math.inf), "θ is inf"), ((3, 0, 1, -np.inf), "θ is -inf"),
    ((3, 0, 1, np.float64("nan")), "θ is np.float64(nan)"), ((3, 0, 1, True), "θ is True, a bool"),
    ((3, 0, 1, np.True_), "θ is np.True_, a NumPy bool"), ((3, 0, 1, "0.65"), "θ is a string"),
    ((3, 0, 1, None), "θ is None"), ((3, 0, 1, 0.35 + 0.2j), "θ is a complex number"),
]
GIVENS_REFUSAL_IDS = ["n1", "n0", "n-negative", "n-float", "n-numpy-float", "n-half", "n-bool", "n-string", "n-none",
                      "i-equals-j", "i-equals-j-4", "j-equals-n", "i-too-large", "i-negative", "j-negative", "i-float",
                      "j-numpy-float", "i-bool", "j-bool", "i-string", "j-none", "theta-nan", "theta-inf",
                      "theta-minus-inf", "theta-numpy-nan", "theta-bool", "theta-numpy-bool", "theta-string",
                      "theta-none", "theta-complex"]


@pytest.mark.parametrize("args, why", GIVENS_REFUSALS, ids=GIVENS_REFUSAL_IDS)
def test_givens_rotation_refusals(pos, args, why):
    _expect_error(ValueError, lambda: pos.givens_rotation(*args), f"givens_rotation{args!r}", why)


# --- online_softmax -------------------------------------------------------------------------------------------------

ONLINE_HINT = ("start from the empty state (m = -inf, l = 0.0, acc = 0.0, a zero array of length k, or None without "
               "values); for each block B, skip it if all its scores are -inf, otherwise m_new = max(m, max of B), "
               "multiply l AND acc by e^{m - m_new} (math.exp(-inf) is 0.0), add Σ_B e^{s_j - m_new} to l and "
               "Σ_B e^{s_j - m_new} v_j to acc, then m = m_new; return m and l as Python floats (float(...)), acc as a "
               "float for 1-D values and as a new 1-D array for 2-D values")


def _kind_of(values):
    if values is None:
        return "none", 0
    V = np.asarray(values, dtype=float)
    return ("number", 0) if V.ndim == 1 else ("vector", V.shape[1])


def _empty(kind, k):
    return None if kind == "none" else 0.0 if kind == "number" else np.zeros(k)


def _oracle_state(scores, values=None):
    """(m, l, acc) of the scores (and values) by scipy.special.softmax: m the largest score, l = 1 / its weight (the
    weight of the largest score is e^0 / l), and acc = l × the softmax-weighted mean of the values; the empty state when
    every score is -inf. (m + ln l = scipy.special.logsumexp is checked apart: near 10³⁰⁰, ln l is lost in m.)"""
    s = np.asarray(scores, dtype=float)
    kind, k = _kind_of(values)
    if not np.any(s > -np.inf):
        return -math.inf, 0.0, _empty(kind, k)
    m = float(np.max(s))
    weights = special.softmax(s)
    l = 1.0 / float(weights[int(np.argmax(s))])         # the weight of the largest score is e^0 / l = 1 / l
    if kind == "none":
        return m, l, None
    mean = weights @ np.asarray(values, dtype=float)
    return m, l, float(l * mean) if kind == "number" else l * mean


def _acc_scale(scores, values):
    """Σ e^{s_j - m} |v_j|, the size of the terms of acc, for an absolute tolerance (cancellations)."""
    s = np.asarray(scores, dtype=float)
    if values is None or not np.any(s > -np.inf):
        return 1.0
    weights = np.exp(s - np.max(s))
    return float(np.max(weights @ np.abs(np.asarray(values, dtype=float)), initial=0.0)) + 1e-300


def _check_types(got, kind, k, what, hint=""):
    """A tuple (m, l, acc) with m and l Python floats and acc None, a Python float or a 1-D float array of length k."""
    if not (isinstance(got, tuple) and len(got) == 3):
        hint = _text(hint)
        pytest.fail(f"expected a tuple (m, l, acc) for {what}, got {type(got).__name__} {_show_any(got)}"
                    + (f" ({hint})" if hint else ""))
    m, l, acc = got
    problems = []
    if type(m) is not float:
        problems.append(f"m is {type(m).__module__}.{type(m).__name__} {m!r}, not a Python float")
    if type(l) is not float:
        problems.append(f"l is {type(l).__module__}.{type(l).__name__} {l!r}, not a Python float")
    if kind == "none" and acc is not None:
        problems.append(f"acc is {_show_any(acc)}, not None (no values were given)")
    if kind == "number" and type(acc) is not float:
        problems.append(f"acc is {type(acc).__module__}.{type(acc).__name__} {_show_any(acc)}, not a Python float "
                        f"(1-D values: one number per score)")
    if kind == "vector" and not (isinstance(acc, np.ndarray) and acc.dtype.kind == "f" and acc.shape == (k,)):
        problems.append(f"acc is {type(acc).__name__}"
                        + (f" of dtype {acc.dtype} and shape {acc.shape}" if isinstance(acc, np.ndarray)
                           else f" {acc!r}")
                        + f", not a 1-D numpy.ndarray of {k} floats (2-D values of shape (n, {k}))")
    if problems:
        hint = _text(hint)
        expected = {"none": "acc None", "number": "acc a Python float",
                    "vector": f"acc a 1-D array of {k} floats"}[kind]
        pytest.fail(f"expected (m, l, acc) with m and l Python floats and {expected} for {what}, got "
                    f"{_show_state(got)}: {'; '.join(problems)}" + (f" ({hint})" if hint else ""))


def _check_state(got, want, what, rtol=1e-12, acc_scale=0.0, hint=""):
    """m exactly the largest score (or -inf), l and acc close to the expected ones (acc with the absolute tolerance
    rtol × acc_scale, for the cancellations)."""
    m, l, acc = got
    wm, wl, wacc = want
    problems = []
    if not (m == wm):
        problems.append(f"m = {m!r} instead of {wm!r}" + (" (m is the largest score read, exactly)"
                                                          if math.isfinite(wm) else ""))
    if not _same(l, wl, rtol, 0.0):
        problems.append(f"l = {_show_number(l)} instead of {_show_number(wl)}")
    if wacc is not None and not _same(acc, wacc, rtol, rtol * acc_scale):
        problems.append(f"acc = {_show_any(acc)} instead of {_show_any(wacc)}{_gap(acc, wacc)}")
    if problems:
        hint = _text(hint)
        pytest.fail(f"expected the state (m, l, acc) = {_show_state(want)} for {what}, got {_show_state(got)}: "
                    f"{'; '.join(problems)}" + (f" ({hint})" if hint else ""))


def _blocks(n, size):
    return [(start, min(start + size, n)) for start in range(0, n, size)]


def _online_candidates(scores, values, size):
    """The final states of classic errors, in closed form (no loop over the blocks): weights relative to the running
    maximum at the time of their block and never rescaled, acc not rescaled while l is, acc / l instead of acc, the
    largest score of the last block as m, Σ e^{s_j} without m."""
    s = np.asarray(scores, dtype=float)
    kind, k = _kind_of(values)
    V = None if values is None else np.asarray(values, dtype=float)
    n = s.size
    want = _oracle_state(s, values)
    if not math.isfinite(want[0]):
        return want, []
    block_of = np.repeat(np.arange(len(_blocks(n, size))), [b - a for a, b in _blocks(n, size)])
    block_max = np.array([s[a:b].max() for a, b in _blocks(n, size)])
    running = np.maximum.accumulate(block_max)[block_of]          # the running maximum after the block of each score
    with np.errstate(all="ignore"):
        stale = np.where(s > -np.inf, np.exp(s - running), 0.0)   # never rescaled
        last = float(block_max[np.max(np.nonzero(block_max > -np.inf))])
        raw = np.where(s > -np.inf, np.exp(s), 0.0)

        def acc_of(weights):
            if V is None:
                return None
            total = weights @ V
            return float(total) if kind == "number" else total

        candidates = [((want[0], float(stale.sum()), acc_of(stale)), "multiply l and acc by e^{m - m_new} when the "
                                                                       "maximum changes (here nothing was rescaled)"),
                      ((want[0], want[1], acc_of(stale)), "rescale acc too, not only l: acc ← acc · e^{m - m_new} + …"),
                      ((want[0], float(stale.sum()), want[2]), "rescale l too: l ← l · e^{m - m_new} + …"),
                      ((last, want[1], want[2]), "m is the largest score read so far, max(m, max of the block), not "
                                                 "the largest score of the last block"),
                      ((want[0], float(raw.sum()), acc_of(raw)), "l = Σ e^{s_j - m}, relative to m, not Σ e^{s_j}"),
                      ((want[0], math.log(want[1]), want[2]), "return l itself, not ln l"),
                      ((want[0] + math.log(want[1]), want[1], want[2]), "m is the largest score, not the log-sum-exp "
                                                                        "m + ln l")]
        if kind != "none":
            candidates.append(((want[0], want[1], acc_of(np.where(s > -np.inf, np.exp(s - want[0]), 0.0) / want[1])),
                               "return acc = Σ e^{s_j - m} v_j, not the weighted mean acc / l"))
    return want, candidates


def _match_state(got, state, rtol=1e-9):
    try:
        m, l, acc = got
        wm, wl, wacc = state
    except (TypeError, ValueError):
        return False
    if not (_same(m, wm, rtol, 1e-12) and _same(l, wl, rtol, 1e-300)):
        return False
    return wacc is None or _same(acc, wacc, rtol, 1e-9 * (1.0 + float(np.max(np.abs(np.asarray(wacc, dtype=float))))))


def _online_hint(got, scores, values, size):
    """ONLINE_HINT, plus the classic error that the final state got matches, if any."""
    try:
        want, candidates = _online_candidates(scores, values, size)
    except (TypeError, ValueError, IndexError):
        return ONLINE_HINT
    for state, text in candidates:
        if not _match_state(state, want) and _match_state(got, state):
            return f"{ONLINE_HINT}; here {text}"
    try:
        if any(math.isnan(float(x)) for x in got[:2]):
            return (f"{ONLINE_HINT}; here the state holds nan: -inf - (-inf) is nan, skip a block whose scores are all "
                    f"-inf (and the empty state stays (-inf, 0.0, …))")
    except (TypeError, ValueError, IndexError):
        pass
    return ONLINE_HINT


def _call_online(pos, scores, values=None, block_size=None, history=None):
    kwargs = {}
    if values is not None:
        kwargs["values"] = values
    if block_size is not None:
        kwargs["block_size"] = block_size
    if history is not None:
        kwargs["history"] = history
    return pos.online_softmax(scores, **kwargs)


def _describe(scores, values=None, block_size=None, history=None):
    args = [_show(scores) if not isinstance(scores, list) or len(scores) > 12 else repr(scores)]
    if values is not None:
        args.append(f"values={_show(values)}")
    if block_size is not None:
        args.append(f"block_size={block_size!r}")
    if history is not None:
        args.append(f"history={history!r}")
    return f"online_softmax({', '.join(args)})"


def _online(pos, scores, values=None, block_size=None, what=None):
    """online_softmax(scores[, values][, block_size]) (final state), its types checked."""
    what = what or _describe(scores, values, block_size)
    size = 1 if block_size is None else int(block_size)
    got = _result(lambda: _call_online(pos, scores, values, block_size), "a state (m, l, acc)", what,
                  ONLINE_HINT)
    kind, k = _kind_of(values)
    _check_types(got, kind, k, what, lambda: _online_hint(got, scores, values, size))
    return got


def _history(pos, scores, values=None, block_size=None, what=None):
    """online_softmax(..., history=True): a list of ⌈n / block_size⌉ states, their types checked."""
    what = what or _describe(scores, values, block_size, True)
    size = 1 if block_size is None else int(block_size)
    n = int(np.asarray(scores, dtype=float).size)
    got = _result(lambda: _call_online(pos, scores, values, block_size, True), "a list of states (m, l, acc)", what,
                  ONLINE_HINT)
    count = -(-n // size)
    assert isinstance(got, list) and len(got) == count, (
        f"expected a list of ⌈n / block_size⌉ = ⌈{n} / {size}⌉ = {count} states for {what}, got "
        f"{type(got).__name__}" + (f" of {len(got)} elements" if isinstance(got, (list, tuple)) else f" {got!r}")
        + " (one state after each block, the last block possibly shorter; a masked block repeats the previous state)")
    kind, k = _kind_of(values)
    for b, state in enumerate(got):
        _check_types(state, kind, k, f"the state after block {b} of {what}", ONLINE_HINT)
    return got


def _check_final(got, scores, values, size, what, rtol=1e-12):
    want = _oracle_state(scores, values)
    _check_state(got, want, f"{what} (m the largest score; by scipy.special.softmax, l = 1 / the weight of m and "
                 f"acc = l × the weighted mean)", rtol=rtol, acc_scale=_acc_scale(scores, values),
                 hint=lambda: _online_hint(got, scores, values, size))


def _random_values(rng, kind, n, k, scale=1.0):
    if kind == "none":
        return None
    if kind == "number":
        return rng.normal(size=n) * scale
    return rng.normal(size=(n, k)) * scale


ONLINE_CASES = [(1, "none", 0, 1, 1.0, 0.0), (1, "vector", 3, 4, 2.0, 0.0), (2, "number", 0, 1, 1.0, 0.0),
                (5, "number", 0, 2, 3.0, 0.0), (6, "vector", 2, 4, 1.0, 0.2), (9, "none", 0, 3, 5.0, 0.0),
                (10, "vector", 1, 3, 0.45, 0.0), (17, "number", 0, 5, 7.5, 0.3), (24, "vector", 5, 7, 2.75, 0.1),
                (40, "vector", 3, 40, 1.6, 0.0), (37, "number", 0, 50, 4.5, 0.25), (150, "vector", 7, 11, 6.0, 0.4),
                (301, "number", 0, 23, 30.0, 0.05)]
ONLINE_IDS = [f"n{n}-{kind}{k or ''}-block{b}{'-masked' if z else ''}" for n, kind, k, b, _, z in ONLINE_CASES]


@pytest.mark.parametrize("n, kind, k, block_size, scale, masked", ONLINE_CASES, ids=ONLINE_IDS)
def test_online_softmax_final_state_matches_logsumexp_and_softmax(pos, n, kind, k, block_size, scale, masked):
    """Random scores (some masked by -inf), random values: m is the largest score exactly, m + ln l is
    scipy.special.logsumexp of the scores, acc / l the softmax-weighted mean of the values (scipy.special.softmax)."""
    rng = _rng(7230, ONLINE_CASES.index((n, kind, k, block_size, scale, masked)))
    scores = rng.normal(size=n) * scale
    scores[rng.random(n) < masked] = -np.inf
    if not np.any(scores > -np.inf):
        scores[int(rng.integers(n))] = float(rng.normal())
    values = _random_values(rng, kind, n, k, 9.0)
    what = _describe(scores, values, block_size)
    got = _online(pos, scores, values, block_size, what)
    _check_final(got, scores, values, block_size, what)
    m, l, acc = got
    _close(m + math.log(l), special.logsumexp(scores), f"m + ln l for {what} (scipy.special.logsumexp)", rtol=1e-13,
           atol=1e-13, hint=lambda: _online_hint(got, scores, values, block_size))
    if values is not None:
        _close(np.asarray(acc) / l, special.softmax(scores) @ values, f"acc / l for {what} (the softmax-weighted mean "
               f"of the values, scipy.special.softmax)", rtol=1e-11, atol=1e-11 * float(np.max(np.abs(values))),
               hint=lambda: _online_hint(got, scores, values, block_size))


EXACT_CASES = [(2, "number"), (3, "vector"), (4, "none"), (2, "vector")]


@pytest.mark.parametrize("block_size, kind", EXACT_CASES, ids=[f"block{b}-{k}" for b, k in EXACT_CASES])
def test_online_softmax_with_exact_rational_weights(pos, block_size, kind):
    """Scores s_j = ln r_j for fractions r_j (and -inf for masked ones): the weights e^{s_j - m} are r_j / r_max
    exactly, so l = Σ r_j / r_max and acc = Σ (r_j / r_max) v_j, computed with fractions."""
    rng = _rng(7231, EXACT_CASES.index((block_size, kind)))
    ratios = [Fraction(3, 7), Fraction(11, 3), Fraction(5, 9), Fraction(13, 4), Fraction(2, 15), Fraction(7, 5),
              None, Fraction(17, 6), Fraction(1, 11), None, Fraction(9, 10)]
    order = rng.permutation(len(ratios))
    ratios = [ratios[o] for o in order]
    scores = np.array([-np.inf if r is None else math.log(r) for r in ratios])
    n = len(ratios)
    values = None if kind == "none" else (rng.integers(-40, 41, size=n) / 8 if kind == "number"
                                          else rng.integers(-40, 41, size=(n, 3)) / 8)
    top = max(r for r in ratios if r is not None)
    weights = [Fraction(0) if r is None else r / top for r in ratios]
    l = float(sum(weights))
    if values is None:
        acc = None
    elif kind == "number":
        acc = float(sum(w * Fraction(float(v)) for w, v in zip(weights, values)))
    else:
        acc = np.array([float(sum(w * Fraction(float(v)) for w, v in zip(weights, values[:, c]))) for c in range(3)])
    shown = "[" + ", ".join("-inf" if r is None else f"ln({r})" for r in ratios) + "]"
    what = (f"online_softmax({shown}"
            + (f", values={_show(values)}" if values is not None else "") + f", block_size={block_size})")
    got = _online(pos, scores, values, block_size, what)
    _check_state(got, (float(np.max(scores)), l, acc), f"{what} (the weights r_j / r_max, with fractions)", rtol=1e-13,
                 acc_scale=_acc_scale(scores, values), hint=lambda: _online_hint(got, scores, values, block_size))


HISTORY_CASES = [(7, "number", 0, 1), (7, "number", 0, 2), (10, "vector", 3, 3), (12, "none", 0, 4),
                 (13, "vector", 2, 5), (30, "number", 0, 7), (25, "vector", 4, 6), (3, "vector", 1, 9),
                 (60, "none", 0, 11)]


@pytest.mark.parametrize("n, kind, k, block_size", HISTORY_CASES,
                         ids=[f"n{n}-{kind}{k or ''}-block{b}" for n, kind, k, b in HISTORY_CASES])
def test_online_softmax_history_is_the_state_of_each_prefix(pos, n, kind, k, block_size):
    """The invariant (MB3 §8): with history=True, ⌈n / block_size⌉ states; the b-th is the state of the first
    (b + 1) · block_size scores (the last one, of all of them), as if they had been read at once."""
    rng = _rng(7232, HISTORY_CASES.index((n, kind, k, block_size)))
    scores = rng.normal(size=n) * 3.0 + np.linspace(-2.0, 2.0, n) * float(rng.uniform(0, 3))
    scores[rng.random(n) < 0.15] = -np.inf
    values = _random_values(rng, kind, n, k, 5.0)
    what = _describe(scores, values, block_size, True)
    states = _history(pos, scores, values, block_size, what)
    for b, (start, stop) in enumerate(_blocks(n, block_size)):
        prefix = scores[:stop]
        part = None if values is None else values[:stop]
        _check_state(states[b], _oracle_state(prefix, part), f"the state after block {b} (the first {stop} scores) of "
                     f"{what}", rtol=1e-12, acc_scale=_acc_scale(prefix, part),
                     hint=lambda: _online_hint(states[b], prefix, part, block_size))
    final = _online(pos, scores, values, block_size)
    _check_state(states[-1], final, f"the last state of {what} (the final state, with history=False)", rtol=1e-12,
                 acc_scale=_acc_scale(scores, values), hint=ONLINE_HINT)


def _records(scores, size):
    """The number of blocks, after the first block that has a finite score, whose maximum exceeds every score before."""
    block_max = [float(np.max(scores[a:b])) for a, b in _blocks(len(scores), size)]
    best, count = -math.inf, 0
    for top in block_max:
        if top > best:
            count += best > -math.inf
            best = top
    return count


@pytest.mark.parametrize("order", ["increasing", "decreasing", "shuffled", "masked-start"])
def test_online_softmax_maximum_changes_exactly_at_the_records(pos, order):
    """After the first finite block, what was accumulated is rescaled exactly when m changes, that is when a block
    holds a new record: at every block for increasing scores, never for decreasing ones; m is always the largest score
    read so far (np.maximum.accumulate)."""
    rng = _rng(7233, ["increasing", "decreasing", "shuffled", "masked-start"].index(order))
    n, size = 42, 3
    scores = np.sort(rng.normal(size=n) * 3.75)
    if order == "decreasing":
        scores = scores[::-1].copy()
    elif order == "shuffled":
        scores = rng.permutation(scores)
    elif order == "masked-start":
        scores[:7] = -np.inf
    values = rng.normal(size=(n, 2))
    what = _describe(scores, values, size, True)
    states = _history(pos, scores, values, size, what)
    ms = np.array([state[0] for state in states])
    want = np.maximum.accumulate([float(np.max(scores[a:b])) for a, b in _blocks(n, size)])
    _close(ms, want, f"the values of m after each block of {what} (the largest score read so far)", rtol=0, atol=0,
           hint=ONLINE_HINT)
    changes = sum(1 for a, b in zip(ms[:-1], ms[1:]) if a > -np.inf and b != a)
    expected = {"increasing": len(states) - 1, "decreasing": 0}.get(order, _records(scores, size))
    assert changes == expected == _records(scores, size), (
        f"expected {expected} changes of m (rescalings) after the first finite block for {what}, got {changes} "
        f"({ONLINE_HINT})")


SIZES_CASES = [(19, "vector", 3), (12, "number", 0), (8, "none", 0)]


@pytest.mark.parametrize("n, kind, k", SIZES_CASES, ids=[f"n{n}-{kind}" for n, kind, _ in SIZES_CASES])
def test_online_softmax_final_state_does_not_depend_on_the_block_size(pos, n, kind, k):
    """Every block size from 1 to n + 3 (beyond n: a single block) gives the same final state, up to rounding: the
    same m exactly, l and acc within 1e-12."""
    rng = _rng(7234, SIZES_CASES.index((n, kind, k)))
    scores = rng.normal(size=n) * 6.0
    scores[rng.random(n) < 0.2] = -np.inf
    scores[int(rng.integers(n))] = float(rng.normal())
    values = _random_values(rng, kind, n, k, 3.0)
    reference = _oracle_state(scores, values)
    for size in range(1, n + 4):
        what = _describe(scores, values, size)
        got = _online(pos, scores, values, size, what)
        _check_state(got, reference, f"{what} (the same state for every block size)", rtol=1e-12,
                     acc_scale=_acc_scale(scores, values), hint=lambda: _online_hint(got, scores, values, size))


def test_online_softmax_same_permutation_of_scores_and_values_gives_the_same_state(pos):
    """Renumbering the scores and the values by the same permutation changes nothing (an order of reading)."""
    rng = _rng(7235)
    for k in range(6):
        n, size = int(rng.integers(3, 40)), int(rng.integers(1, 9))
        scores = rng.normal(size=n) * 5.0
        scores[rng.random(n) < 0.2] = -np.inf
        values = rng.normal(size=(n, 3)) * 4.25
        base = _online(pos, scores, values, size)
        order = rng.permutation(n)
        what = _describe(scores[order], values[order], size)
        got = _online(pos, scores[order], values[order], size, what)
        _check_state(got, base, f"{what}, scores and values permuted by {order.tolist()[:12]}… (the state before the "
                     f"permutation)", rtol=1e-12, acc_scale=_acc_scale(scores, values),
                     hint=lambda: _online_hint(got, scores[order], values[order], size))
        _check_final(got, scores[order], values[order], size, what)


@pytest.mark.parametrize("c", [7.25, -300.0, 1e4, -0.0625], ids=["plus-7.25", "minus-300", "plus-1e4", "minus-1/16"])
def test_online_softmax_constant_added_to_the_scores_moves_m_only(pos, c):
    """s_j + c for every j: the weights e^{s_j - m} do not change, so m becomes m + c, and l, acc (and acc / l, the
    softmax-weighted mean) stay the same, up to rounding."""
    rng = _rng(7236)
    n, size = 23, 4
    scores = rng.normal(size=n) * 3.0
    scores[[2, 15]] = -np.inf
    values = rng.normal(size=n) * 6.0
    m, l, acc = _online(pos, scores, values, size)
    shifted = scores + c
    what = _describe(shifted, values, size) + f" (the scores plus {c!r})"
    got = _online(pos, shifted, values, size, what)
    tolerance = 1e-14 * max(1.0, abs(c)) * 4
    _check_state(got, (float(np.max(shifted)), l, acc), f"{what} (m + c, and l and acc of the scores without c)",
                 rtol=tolerance, acc_scale=_acc_scale(scores, values),
                 hint=lambda: _online_hint(got, shifted, values, size))


def test_online_softmax_identity_values_give_the_weights(pos):
    """With values = I (the vector e_j for score j), acc = (e^{s_j - m})_j and acc / l is the softmax of the scores:
    e^{s_j - m} / l is the weight of score j (scipy.special.softmax), 0 for a masked score."""
    rng = _rng(7237)
    for k in range(5):
        n, size = int(rng.integers(2, 15)), int(rng.integers(1, 6))
        scores = rng.normal(size=n) * 4.25
        scores[rng.random(n) < 0.25] = -np.inf
        scores[int(rng.integers(n))] = float(rng.normal())
        what = _describe(scores, np.eye(n), size)
        got = _online(pos, scores, np.eye(n), size, what)
        m, l, acc = got
        _close(acc / l, special.softmax(scores), f"acc / l for {what} (the weights, scipy.special.softmax)", rtol=1e-12,
               atol=1e-15, hint=lambda: _online_hint(got, scores, np.eye(n), size))
        _close(acc, np.exp(scores - np.max(scores)), f"acc for {what} (the weights e^(s_j - m) before dividing by l)",
               rtol=1e-12, atol=0, hint=lambda: _online_hint(got, scores, np.eye(n), size))


def test_online_softmax_masked_scores_have_weight_zero(pos):
    """A score -inf (masked) has weight 0, whatever its value: the state is that of the other scores, computed without
    them (the softmax restricted to the scores that are not masked), even for huge values under the masks."""
    rng = _rng(7238)
    for k in range(6):
        n, size = int(rng.integers(4, 30)), int(rng.integers(1, 7))
        scores = rng.normal(size=n) * 3.0
        masked = rng.random(n) < 0.4
        masked[int(rng.integers(n))] = False
        scores[masked] = -np.inf
        values = rng.normal(size=(n, 2))
        values[masked] = 1e200 * rng.choice([-1.0, 1.0], size=(int(masked.sum()), 2))
        kept = ~masked
        what = _describe(scores, values, size)
        got = _online(pos, scores, values, size, what)
        want = _oracle_state(scores[kept], values[kept])
        _check_state(got, want, f"{what} (the state of the {int(kept.sum())} scores that are not masked)", rtol=1e-12,
                     acc_scale=_acc_scale(scores[kept], values[kept]),
                     hint=lambda: _online_hint(got, scores[kept], values[kept], size))


def test_online_softmax_masked_block_repeats_the_previous_state(pos):
    """A block whose scores are all -inf leaves the state unchanged: in the history, it repeats the previous state (the
    empty state before the first finite block), with its own copy of acc."""
    scores = np.array([-np.inf, -np.inf, -np.inf, 0.75, -1.25, -np.inf, -np.inf, -np.inf, -np.inf, 2.375, 1.625])
    values = np.array([[4.0, -2.0], [1.0, 7.0], [3.0, 3.0], [-5.0, 0.375], [2.25, -1.0], [9.0, 9.0], [-9.0, 6.0],
                       [0.375, 0.25], [-3.0, 1.8125], [6.0, -4.5], [1.0, 1.0]])
    size = 3
    what = _describe(scores, values, size, True)
    states = _history(pos, scores, values, size, what)
    _check_state(states[0], (-math.inf, 0.0, np.zeros(2)), f"the state after block 0 (three masked scores) of {what} "
                 f"(the empty state)", hint=ONLINE_HINT)
    _check_state(states[2], states[1], f"the state after block 2 (three masked scores) of {what} (the state after "
                 f"block 1, unchanged)", rtol=0, hint=ONLINE_HINT)
    for b, (start, stop) in enumerate(_blocks(len(scores), size)):
        _check_state(states[b], _oracle_state(scores[:stop], values[:stop]), f"the state after block {b} of {what}",
                     acc_scale=_acc_scale(scores[:stop], values[:stop]), hint=ONLINE_HINT)


@pytest.mark.parametrize("kind, k", [("none", 0), ("number", 0), ("vector", 1), ("vector", 4)],
                         ids=["no-values", "numbers", "vectors-k1", "vectors-k4"])
def test_online_softmax_every_score_masked_gives_the_empty_state_of_its_kind(pos, kind, k):
    """Every score -inf: no law; the state is the empty state (-inf, 0.0, acc0), acc0 None, 0.0 or a zero array of
    length k, after every block too, without a RuntimeWarning (no -inf - (-inf))."""
    rng = _rng(7239)
    for n, size in ((1, 1), (5, 2), (6, 6), (4, 9)):
        scores = np.full(n, -np.inf)
        values = _random_values(rng, kind, n, k, 3.0)
        what = _describe(scores, values, size)
        got = _online(pos, scores, values, size, what)
        _check_state(got, (-math.inf, 0.0, _empty(kind, k)), f"{what} (the empty state)",
                     hint=lambda: _online_hint(got, scores, values, size))
        what = _describe(scores, values, size, True)
        states = _history(pos, scores, values, size, what)
        for b, state in enumerate(states):
            _check_state(state, (-math.inf, 0.0, _empty(kind, k)), f"the state after block {b} of {what} (the empty "
                         f"state)", hint=ONLINE_HINT)


def test_online_softmax_l_is_at_least_1_as_soon_as_m_is_finite(pos):
    """l ≥ 1 exactly (in floats) in every state whose m is finite: the largest score contributes e^0 = 1 and the others
    add non-negative terms; with very spread scores, l = 1.0 and acc is the value of the largest score."""
    rng = _rng(7240)
    for k in range(12):
        n, size = int(rng.integers(1, 40)), int(rng.integers(1, 8))
        scores = rng.normal(size=n) * float(rng.choice([0.02, 1.0, 50.0, 3000.0]))
        scores[rng.random(n) < 0.2] = -np.inf
        what = _describe(scores, None, size, True)
        for b, (m, l, _) in enumerate(_history(pos, scores, None, size, what)):
            assert m == -math.inf or l >= 1.0, (f"expected l ≥ 1 in the state after block {b} of {what} (m = {m!r} is "
                                                f"finite: the largest score contributes e^0 = 1), got l = {l!r} "
                                                f"({ONLINE_HINT})")
    scores = np.array([-2000.0, 1.875, -1500.0, -3000.0])
    values = np.array([[7.0, -3.0], [0.25, 2.625], [4.0, 4.0], [-1.0, 8.0]])
    what = _describe(scores, values, 2)
    got = _online(pos, scores, values, 2, what)
    _check_state(got, (1.875, 1.0, np.array([0.25, 2.625])), f"{what} (the other weights underflow to 0)", rtol=0,
                 hint=lambda: _online_hint(got, scores, values, 2))


LARGE_CASES = [("large", 1), ("large", 4), ("jumps", 2), ("jumps", 1), ("very-negative", 3), ("huge", 2)]


@pytest.mark.parametrize("case, block_size", LARGE_CASES, ids=[f"{c}-block{b}" for c, b in LARGE_CASES])
def test_online_softmax_large_and_very_negative_scores_without_overflow(pos, case, block_size):
    """Scores around +900, scores that jump by more than 1 000 from one block to the next (e^{1000} overflows), scores
    around -2 000 (e^{-2000} underflows to 0) and scores near 10³⁰⁰: the state is still exact, without a RuntimeWarning,
    because only e^{s_j - m_new} ≤ 1 and e^{m - m_new} ≤ 1 are ever computed."""
    rng = _rng(7241, LARGE_CASES.index((case, block_size)))
    n = 16
    if case == "large":
        scores = 900.0 + rng.normal(size=n) * 3.5
    elif case == "jumps":
        scores = np.repeat(np.array([-700.0, 650.0, -1200.0, 1900.0]), 4) + rng.normal(size=n)
    elif case == "very-negative":
        scores = -2000.0 + rng.normal(size=n) * 2.0
    else:
        scores = 1e300 * (1.0 + rng.integers(0, 3, size=n) * 2.0 ** -40)
    values = rng.normal(size=(n, 3)) * 5.0
    what = _describe(scores, values, block_size)
    got = _online(pos, scores, values, block_size, what)
    _check_final(got, scores, values, block_size, what, rtol=1e-11)
    what = _describe(scores, values, block_size, True)
    states = _history(pos, scores, values, block_size, what)
    for b, (start, stop) in enumerate(_blocks(n, block_size)):
        _check_state(states[b], _oracle_state(scores[:stop], values[:stop]), f"the state after block {b} of {what}",
                     rtol=1e-11, acc_scale=_acc_scale(scores[:stop], values[:stop]), hint=ONLINE_HINT)


class _ExpSpy:
    """np.exp or math.exp, recording the arguments > 0 it receives (e^x > 1: an overflow beyond x ≈ 709)."""

    def __init__(self, original, name):
        self.original, self.name, self.positive = original, name, []

    def __call__(self, x, *args, **kwargs):
        try:
            with np.errstate(invalid="ignore"):
                arr = np.asarray(x, dtype=float)
                if np.any(arr > 0):
                    self.positive.append(float(np.max(arr[arr > 0])))
        except (TypeError, ValueError):
            pass
        return self.original(x, *args, **kwargs)


def _no_positive_exponential(monkeypatch, call, what, hint):
    spies = [_ExpSpy(np.exp, "np.exp"), _ExpSpy(math.exp, "math.exp")]
    with monkeypatch.context() as patch:
        patch.setattr(np, "exp", spies[0])
        patch.setattr(math, "exp", spies[1])
        _result(call, "a result", what, hint)
    found = [f"{spy.name} of {max(spy.positive)!r}" for spy in spies if spy.positive]
    assert not found, (f"expected no exponential of a positive number for {what} (only e^(s_j - m_new) ≤ 1 and "
                       f"e^(m - m_new) ≤ 1), got {', '.join(found)} ({hint})")


def test_online_softmax_never_takes_the_exponential_of_a_positive_number(pos_module, monkeypatch):
    """No call of np.exp or math.exp on a positive number: each exponent is s_j - m_new or m - m_new, both ≤ 0 (the
    exponentials of positive numbers are what overflows)."""
    rng = _rng(7242)
    for k in range(6):
        n, size = int(rng.integers(5, 30)), int(rng.integers(1, 6))
        scores = np.sort(rng.normal(size=n) * 5.0) if k % 2 else rng.normal(size=n) * 5.0
        scores[rng.random(n) < 0.2] = -np.inf
        values = rng.normal(size=(n, 2))
        what = _describe(scores, values, size, k % 3 == 0)
        _no_positive_exponential(monkeypatch, lambda: pos_module.online_softmax(scores, values, size, k % 3 == 0),
                                 what, ONLINE_HINT)


@pytest.mark.parametrize("scores, values, kind, k, text", [
    ([2, 5, -1, 5], [3, -4, 1, 0], "number", 0, "lists of integers"),
    ((0.75, -0.25, 1.625), ((1, 6), (-2, 9), (5, 7)), "vector", 2, "tuples"),
    (np.array([4, 1, 9], dtype=np.int64), None, "none", 0, "an int64 array, no values"),
    (np.array([0.375, -1.25, 2.125, 0.0], dtype=np.float32), np.array([1.8125, 2.625, -0.375, 4.25], dtype=np.float32),
     "number", 0, "float32 arrays"),
    ([Fraction(1, 3), Fraction(-2, 5)], [[Fraction(7, 2)], [Fraction(1, 4)]], "vector", 1, "fractions, k = 1"),
    ([-np.inf, 3.25], [1e6, -2.75], "number", 0, "a masked first score"),
], ids=["int-lists", "tuples", "int64-no-values", "float32", "fractions-k1", "masked-first"])
def test_online_softmax_accepts_lists_integers_and_returns_python_floats(pos, scores, values, kind, k, text):
    """Lists, tuples, integers, float32 and fractions are accepted; m and l are Python floats, acc a Python float for
    1-D values and a 1-D array of k floats for 2-D values of shape (n, k), even when k = 1."""
    as_float = None if values is None else np.asarray(values, dtype=float)
    for size in (1, 2, np.int64(3), np.int32(5)):
        what = f"online_softmax({scores!r}" + (f", values={values!r}" if values is not None else "") + \
               f", block_size={size!r}) ({text})"
        got = _online(pos, scores, values, size, what)
        _check_final(got, np.asarray(scores, dtype=float), as_float, int(size), what, rtol=1e-12)


def test_online_softmax_defaults_are_no_values_block_size_1_and_no_history(pos):
    """online_softmax(scores) reads one score at a time, without values (acc None), and returns the final state."""
    rng = _rng(7243)
    scores = rng.normal(size=9) * 2.0
    what = f"online_softmax({_show(scores)})"
    got = _result(lambda: pos.online_softmax(scores), "a state (m, l, None)", what, ONLINE_HINT)
    _check_types(got, "none", 0, what, ONLINE_HINT)
    _check_final(got, scores, None, 1, what)
    what = f"online_softmax({_show(scores)}, history=True)"
    states = _result(lambda: pos.online_softmax(scores, history=True), "a list of 9 states", what, ONLINE_HINT)
    assert isinstance(states, list) and len(states) == 9, (
        f"expected a list of 9 states (block_size 1 by default) for {what}, got {_show_any(states)} ({ONLINE_HINT})")


def test_online_softmax_single_score_and_block_larger_than_n(pos):
    """One score s with its value v: the state (s, 1.0, v); a block_size larger than n reads everything in one block
    (a history of a single state)."""
    rng = _rng(7244)
    for k in range(4):
        s, v = float(rng.normal() * 9.0), rng.normal(size=3)
        what = f"online_softmax([{s!r}], values=[{_show(v)}])"
        got = _online(pos, [s], [v], None, what)
        _check_state(got, (s, 1.0, v), what, rtol=0, hint=ONLINE_HINT)
    scores = rng.normal(size=6)
    values = rng.normal(size=6)
    what = _describe(scores, values, 50, True)
    states = _history(pos, scores, values, 50, what)
    _check_final(states[0], scores, values, 50, f"the single state of {what}")


def test_online_softmax_history_states_do_not_share_arrays(pos, pos_module):
    """With 2-D values, each state of the history has its own acc: no two of them share memory (a masked block
    included), nor with the values received; changing one state afterwards changes no other."""
    scores = np.array([0.625, -0.75, -np.inf, -np.inf, 1.375, 3.5, -np.inf, -np.inf, -2.0, 0.25])
    values = np.array([[1.0, 2.0, -1.0], [0.375, -3.0, 2.0], [4.0, 4.0, 4.0], [7.0, -1.0, 0.0], [-2.0, 1.625, 3.0],
                       [0.25, 0.75, -0.375], [5.0, 5.0, 5.0], [-6.0, 2.0, 1.0], [3.0, -2.625, 0.375], [1.0, 1.0, -4.0]])
    size = 2
    what = _describe(scores, values, size, True)
    _history(pos, scores, values, size, what)                   # the types and the number of states
    states = _result(lambda: pos_module.online_softmax(scores, values, size, True), "a list of states", what,
                     ONLINE_HINT)                               # on the arrays themselves, not on copies
    copies = [state[2].copy() for state in states]
    for a, b in itertools.combinations(range(len(states)), 2):
        assert not np.shares_memory(states[a][2], states[b][2]), (
            f"expected each state of {what} to have its own acc, got the states after blocks {a} and {b} sharing the "
            f"same array (append a copy, acc.copy(), and never update acc in place: acc *= … changes the states "
            f"already kept)")
    for b, state in enumerate(states):
        assert not np.shares_memory(state[2], values), (
            f"expected the acc of the state after block {b} of {what} to be a new array, got a view of values")
    states[1][2][:] = 1e9
    for b, state in enumerate(states):
        if b != 1:
            _close(state[2], copies[b], f"the acc of the state after block {b} of {what}, after writing into the state "
                   f"after block 1 (no shared array)", rtol=0, hint=ONLINE_HINT)


def test_online_softmax_does_not_modify_its_inputs(pos_module):
    """Float arrays (a division or a subtraction in place would show): scores with -inf and a maximum ≠ 0, values 1-D
    and 2-D."""
    # not dyadic: a subtraction in place undone afterwards (s -= m, then s += m) leaves a change of one ulp
    scores = np.array([1.7, -np.inf, 3.1, -0.6, 2.3, -np.inf, 0.9])
    for values in (np.array([2.375, -1.0, 6.25, 0.75, -3.5, 1.375, 4.0]),
                   np.array([[1.625, -2.0], [0.25, 3.0], [-4.5, 1.0], [2.0, 2.75], [-0.375, -1.625], [3.25, 0.625],
                             [1.0, -3.0]])):
        for history in (False, True):
            copies = scores.copy(), values.copy()
            what = _describe(scores, values, 2, history)
            got = _result(lambda: pos_module.online_softmax(scores, values, 2, history), "a state", what, ONLINE_HINT)
            assert np.array_equal(scores, copies[0]) and np.array_equal(values, copies[1]), (
                f"expected scores and values unchanged by {what}, got scores = {_show(scores)}, values = "
                f"{_show(values)} (largest change "
                f"{float(np.max(np.abs(np.where(scores == copies[0], 0.0, scores - copies[0])))):.1e} in the scores, "
                f"{float(np.max(np.abs(values - copies[1]))):.1e} in the values; never modify the arrays you receive: "
                f"scores -= m, values *= … or "
                f"scores[scores == -np.inf] = … write into them)")
            for state in (got if history else [got]):
                acc = state[2] if isinstance(state, tuple) and len(state) == 3 else None
                assert not (isinstance(acc, np.ndarray) and np.shares_memory(acc, values)), (
                    f"expected a new array as acc for {what}, got a view of values")


SCORE_REFUSALS = [([], "scores is empty"), (np.array([]), "scores is an empty array"),
                  ([[0.35, 1.15]], "scores is 2-D"), (np.zeros((2, 2)), "scores is a 2 × 2 array"),
                  (0.65, "scores is a number, not 1-D"), (None, "scores is None"),
                  (["a", 0.15], "scores holds a string"), ([0.45, np.nan], "scores holds nan"),
                  ([np.inf, 0.15], "scores holds +inf"), ([0.05, np.inf, -np.inf], "scores holds +inf (and -inf)"),
                  ([1.875, 2j], "scores holds a complex number"), ([[0.15, 0.25], [0.35]], "scores is a ragged list")]


@pytest.mark.parametrize("scores, why", SCORE_REFUSALS, ids=["empty", "empty-array", "two-d", "matrix", "scalar",
                                                             "none", "string", "nan", "plus-inf", "plus-and-minus-inf",
                                                             "complex", "ragged"])
def test_online_softmax_refuses_bad_scores(pos, scores, why):
    _expect_error(ValueError, lambda: pos.online_softmax(scores), f"online_softmax({scores!r})", why)


VALUE_REFUSALS = [([1.0, 2.0], "values has 2 rows for 3 scores"), ([1.0, 2.0, 3.0, 4.0], "values has 4 rows for 3 "
                                                                                        "scores (one too many)"),
                  ([[1.0, 2.25], [3.75, 4.0]], "values has 2 rows for 3 scores"),
                  (np.ones((3, 2, 2)), "values is 3-D"), (2.0, "values is a number, not 1-D or 2-D"),
                  (np.zeros((3, 0)), "values has no column"), ([1.0, np.nan, 3.0], "values holds nan"),
                  ([[1.0], [np.inf], [0.0]], "values holds inf"), ([1.0, 2.0, -np.inf], "values holds -inf"),
                  ([7.0, np.nan, 1.0], "values holds nan under a masked score (still not a finite number)"),
                  (["a", 1.0, 2.0], "values holds a string"), ([[1.0], [2.0, 3.0], [4.0]], "values is a ragged list")]


@pytest.mark.parametrize("values, why", VALUE_REFUSALS, ids=["short", "long", "short-2d", "three-d", "scalar",
                                                             "no-column", "nan", "inf", "minus-inf", "nan-masked",
                                                             "string", "ragged"])
def test_online_softmax_refuses_bad_values(pos, values, why):
    scores = [0.25, -np.inf, 1.625]
    _expect_error(ValueError, lambda: pos.online_softmax(scores, values=values),
                  f"online_softmax({scores!r}, values={values!r})", why)


def test_online_softmax_refuses_a_number_as_values_even_for_one_score(pos):
    _expect_error(ValueError, lambda: pos.online_softmax([0.625], values=3.0), "online_softmax([0.625], values=3.0)",
                  "values is a number, not a 1-D array of one value")


BLOCK_REFUSALS = [(0, "block_size = 0"), (-2, "block_size is negative"), (2.0, "block_size is the float 2.0"),
                  (np.float64(3.0), "block_size is np.float64(3.0)"), (2.25, "block_size is 2.25"),
                  (True, "block_size is True, a bool"), (False, "block_size is False, a bool"),
                  ("2", "block_size is a string"), (None, "block_size is None")]


@pytest.mark.parametrize("block_size, why", BLOCK_REFUSALS, ids=["zero", "negative", "float", "numpy-float", "half",
                                                                 "true", "false", "string", "none"])
def test_online_softmax_refuses_a_bad_block_size(pos, block_size, why):
    _expect_error(ValueError, lambda: pos.online_softmax([0.625, 1.375, -0.75], block_size=block_size),
                  f"online_softmax([0.625, 1.375, -0.75], block_size={block_size!r})", why)


@pytest.mark.parametrize("history, why", [(1, "history is the integer 1, not a bool"), (0, "history is 0"),
                                          ("yes", "history is a string"), (None, "history is None"),
                                          (1.0, "history is 1.0")], ids=["one", "zero", "string", "none", "float"])
def test_online_softmax_refuses_a_history_that_is_not_a_bool(pos, history, why):
    _expect_error(ValueError, lambda: pos.online_softmax([0.625, 1.375], history=history),
                  f"online_softmax([0.625, 1.375], history={history!r})", why)


# --- merge_softmax_states -------------------------------------------------------------------------------------------

MERGE_HINT = ("with m = max(m₁, m₂): l = l₁ e^{m₁ - m} + l₂ e^{m₂ - m} and acc = acc₁ e^{m₁ - m} + acc₂ e^{m₂ - m} "
              "(math.exp(-inf) is 0.0, and both exponents are ≤ 0); two empty states give the empty state of their "
              "kind; m and l as Python floats, acc of the kind of the arguments (a Python float, or a new array)")


def _merge_oracle(state1, state2):
    """The merged state by scipy.special.logsumexp with weights: l = e^{ln(l₁ e^{m₁} + l₂ e^{m₂}) - m}, and each
    coordinate of acc the same with its sign (return_sign=True)."""
    (m1, l1, a1), (m2, l2, a2) = state1, state2
    m = max(m1, m2)
    if m == -math.inf:
        return state1
    exponents = np.array([m1, m2])
    l = math.exp(float(special.logsumexp(exponents, b=[l1, l2])) - m)
    if a1 is None:
        return m, l, None
    first, second = np.atleast_1d(np.asarray(a1, dtype=float)), np.atleast_1d(np.asarray(a2, dtype=float))
    acc = np.empty(first.shape)
    for c in range(first.size):
        log, sign = special.logsumexp(exponents, b=[first[c], second[c]], return_sign=True)
        acc[c] = float(sign) * math.exp(float(log) - m) if sign != 0 else 0.0
    return m, l, float(acc[0]) if not isinstance(a1, np.ndarray) else acc


def _state_kind(state):
    acc = state[2]
    return ("none", 0) if acc is None else ("vector", len(acc)) if isinstance(acc, np.ndarray) else ("number", 0)


def _merge_scale(state1, state2):
    """|acc₁| e^{m₁ - m} + |acc₂| e^{m₂ - m}, the size of the terms of acc, for an absolute tolerance."""
    (m1, _, a1), (m2, _, a2) = state1, state2
    m = max(m1, m2)
    if a1 is None or m == -math.inf:
        return 1.0
    return float(np.max(np.abs(np.asarray(a1, dtype=float)) * math.exp(m1 - m)
                        + np.abs(np.asarray(a2, dtype=float)) * math.exp(m2 - m), initial=0.0))


def _merge_candidates(state1, state2):
    """The right state and the states of classic errors."""
    want = _merge_oracle(state1, state2)
    (m1, l1, a1), (m2, l2, a2) = state1, state2
    m = max(m1, m2)
    if m == -math.inf:
        return want, []
    with np.errstate(all="ignore"):
        f1, f2 = math.exp(m1 - m), math.exp(m2 - m)
        g1 = math.exp(min(m - m1, 700.0)) if m1 > -math.inf else 0.0
        g2 = math.exp(min(m - m2, 700.0)) if m2 > -math.inf else 0.0

        def acc(x1, x2):
            if a1 is None:
                return None
            value = np.asarray(a1, dtype=float) * x1 + np.asarray(a2, dtype=float) * x2
            return float(value) if not isinstance(a1, np.ndarray) else value

        candidates = [((m, l1 + l2, acc(1.0, 1.0)), "express each state relative to m = max(m₁, m₂) first: multiply "
                                                    "l and acc of each state by e^{m_i - m}"),
                      ((m, l1 * f1 + l2 * f2, acc(1.0, 1.0)), "rescale acc too, not only l"),
                      ((m, l1 * g1 + l2 * g2, acc(g1, g2)), "the factor is e^{m_i - m} ≤ 1, not e^{m - m_i}"),
                      ((min(m1, m2) if min(m1, m2) > -math.inf else m, want[1], want[2]),
                       "m is the larger of the two maxima, max(m₁, m₂)")]
    return want, candidates


def _merge_hint(got, state1, state2):
    try:
        want, candidates = _merge_candidates(state1, state2)
    except (TypeError, ValueError, OverflowError):
        return MERGE_HINT
    for state, text in candidates:
        if not _match_state(state, want) and _match_state(got, state):
            return f"{MERGE_HINT}; here {text}"
    return MERGE_HINT


def _merge(pos, state1, state2, what=None):
    """merge_softmax_states(state1, state2), its types checked."""
    what = what or f"merge_softmax_states({_show_state(state1)}, {_show_state(state2)})"
    got = _result(lambda: pos.merge_softmax_states(state1, state2), "the merged state (m, l, acc)", what, MERGE_HINT)
    kind, k = _state_kind(state1)
    _check_types(got, kind, k, what, lambda: _merge_hint(got, state1, state2))
    return got


def _new_acc_array(pos_module, state1, state2, what):
    """The merge called on the arrays themselves (not on copies): its acc must be a new array, sharing no memory with
    the acc of either argument."""
    got = _result(lambda: pos_module.merge_softmax_states(state1, state2), "the merged state", what, MERGE_HINT)
    acc = got[2] if isinstance(got, tuple) and len(got) == 3 else None
    given = [state[2] for state in (state1, state2) if isinstance(state[2], np.ndarray)]
    shown = "the array of an argument" if isinstance(acc, np.ndarray) else _show_any(acc)
    assert isinstance(acc, np.ndarray) and not any(np.shares_memory(acc, a) for a in given), (
        f"expected a new array as acc for {what}, got {shown} (return a new array, even when a state is empty: the "
        f"caller may change it)")


def _check_merge(got, state1, state2, what, rtol=1e-12):
    _check_state(got, _merge_oracle(state1, state2), f"{what} (scipy logsumexp of the two states)", rtol=rtol,
                 acc_scale=_merge_scale(state1, state2), hint=lambda: _merge_hint(got, state1, state2))


def _random_state(rng, kind, k, spread=20.0):
    """A state (m, l, acc) as the contract allows it: m any real number, l ≥ 1, acc any finite numbers."""
    m = float(rng.normal() * spread)
    l = 1.0 + float(rng.exponential(4.0))
    acc = None if kind == "none" else float(rng.normal() * 10) if kind == "number" else rng.normal(size=k) * 10
    return m, l, acc


def _scores_and_values(rng, n, kind, k, masked=0.0):
    scores = rng.normal(size=n) * 3.5
    scores[rng.random(n) < masked] = -np.inf
    return scores, _random_values(rng, kind, n, k, 6.0)


MERGE_KINDS = [("none", 0), ("number", 0), ("vector", 1), ("vector", 4)]
MERGE_IDS = ["no-values", "numbers", "vectors-k1", "vectors-k4"]


@pytest.mark.parametrize("kind, k", MERGE_KINDS, ids=MERGE_IDS)
def test_merge_softmax_states_of_two_disjoint_sets_is_the_state_of_their_union(pos, kind, k):
    """Two sets of scores (and values) cut from one series: the merge of their two states (computed by scipy) is the
    state of the whole series, also when one set is masked entirely (its state is the empty state)."""
    rng = _rng(7260, MERGE_KINDS.index((kind, k)))
    for t in range(8):
        n = int(rng.integers(2, 30))
        scores, values = _scores_and_values(rng, n, kind, k, masked=0.15)
        cut = int(rng.integers(1, n))
        if t == 5:
            scores[:cut] = -np.inf
        if not np.any(scores > -np.inf):
            scores[-1] = 0.375
        parts = [(scores[:cut], None if values is None else values[:cut]),
                 (scores[cut:], None if values is None else values[cut:])]
        state1, state2 = (_oracle_state(*part) for part in parts)
        what = (f"merge_softmax_states(state1, state2) for the states of the scores {_show(scores[:cut])} and "
                f"{_show(scores[cut:])}")
        got = _merge(pos, state1, state2, what)
        _check_state(got, _oracle_state(scores, values), f"{what} (the state of all {n} scores, scipy)", rtol=1e-12,
                     acc_scale=_acc_scale(scores, values), hint=lambda: _merge_hint(got, state1, state2))


@pytest.mark.parametrize("kind, k", MERGE_KINDS, ids=MERGE_IDS)
def test_merge_softmax_states_of_arbitrary_states(pos, kind, k):
    """Any two states allowed by the contract (m real, l ≥ 1, acc any finite numbers, possibly negative): the merged
    state is (max(m₁, m₂), l₁ e^{m₁ - m} + l₂ e^{m₂ - m}, acc₁ e^{m₁ - m} + acc₂ e^{m₂ - m}), checked with
    scipy.special.logsumexp and signed weights."""
    rng = _rng(7261, MERGE_KINDS.index((kind, k)))
    for t in range(12):
        state1 = _random_state(rng, kind, k, spread=float(rng.choice([0.45, 5.0, 40.0])))
        state2 = _random_state(rng, kind, k, spread=float(rng.choice([0.45, 5.0, 40.0])))
        if t == 3:
            state2 = (state1[0], state2[1], state2[2])               # the same maximum
        got = _merge(pos, state1, state2)
        _check_merge(got, state1, state2, f"merge_softmax_states({_show_state(state1)}, {_show_state(state2)})")


def test_merge_softmax_states_is_commutative_and_associative(pos):
    """merge(a, b) = merge(b, a), and merge(merge(a, b), c) = merge(a, merge(b, c)), up to rounding, both equal to the
    state of the three sets of scores together (a series cut into pieces, merged in any grouping)."""
    rng = _rng(7262)
    for kind, k in MERGE_KINDS:
        for t in range(5):
            pieces = [_scores_and_values(rng, int(rng.integers(1, 12)), kind, k, masked=0.2) for _ in range(3)]
            if t == 2:
                pieces[1][0][:] = -np.inf                                    # a piece masked entirely
            states = [_oracle_state(*piece) for piece in pieces]
            a, b, c = states
            ab, ba = _merge(pos, a, b), _merge(pos, b, a)
            _check_state(ba, ab, f"merge_softmax_states(b, a) for a = {_show_state(a)}, b = {_show_state(b)} "
                         f"(merge_softmax_states(a, b): the merge is commutative)", rtol=1e-14,
                         acc_scale=_merge_scale(a, b), hint=lambda: _merge_hint(ba, b, a))
            left = _merge(pos, ab, c, "merge_softmax_states(merge_softmax_states(a, b), c)")
            bc = _merge(pos, b, c)
            right = _merge(pos, a, bc, "merge_softmax_states(a, merge_softmax_states(b, c))")
            scores = np.concatenate([piece[0] for piece in pieces])
            values = None if kind == "none" else np.concatenate([piece[1] for piece in pieces])
            whole = _oracle_state(scores, values)
            text = f"for a, b, c = {_show_state(a)}, {_show_state(b)}, {_show_state(c)}"
            _check_state(left, whole, f"merge_softmax_states(merge_softmax_states(a, b), c) {text} (the state of the "
                         f"three sets of scores)", rtol=1e-12, acc_scale=_acc_scale(scores, values),
                         hint=lambda: _merge_hint(left, ab, c))
            _check_state(right, left, f"merge_softmax_states(a, merge_softmax_states(b, c)) {text} (the other "
                         f"grouping: the merge is associative)", rtol=1e-12,
                         acc_scale=_acc_scale(scores, values), hint=lambda: _merge_hint(right, a, bc))


@pytest.mark.parametrize("kind, k", MERGE_KINDS, ids=MERGE_IDS)
def test_merge_softmax_states_empty_state_of_the_same_kind_is_neutral(pos, pos_module, kind, k):
    """(-inf, 0.0, acc0) of the same kind, on either side, gives the other state back (m, l and acc unchanged, m and l
    as Python floats even when they were NumPy floats, acc a new array)."""
    rng = _rng(7263, MERGE_KINDS.index((kind, k)))
    for t in range(4):
        m, l, acc = _random_state(rng, kind, k)
        given = (np.float64(m), np.float64(l), np.float64(acc) if kind == "number" else acc) if t % 2 else (m, l, acc)
        empty = (-math.inf, 0.0, _empty(kind, k)) if t < 2 else (np.float64(-np.inf), np.float64(0.0), _empty(kind, k))
        for first, second in ((empty, given), (given, empty)):
            what = f"merge_softmax_states({_show_state(first)}, {_show_state(second)})"
            got = _merge(pos, first, second, what + (" (NumPy floats in the state)" if t % 2 else ""))
            _check_state(got, (m, l, acc), f"{what} (the non-empty state: the empty state is neutral)", rtol=1e-15,
                         acc_scale=(1.0 + float(np.max(np.abs(np.asarray(acc, dtype=float)))))
                         if acc is not None else 0.0, hint=lambda: _merge_hint(got, first, second))
            if kind == "vector":
                _new_acc_array(pos_module, first, second, what)


@pytest.mark.parametrize("kind, k", MERGE_KINDS, ids=MERGE_IDS)
def test_merge_softmax_states_of_two_empty_states_is_the_empty_state(pos, pos_module, kind, k):
    """Two empty states of the same kind: the empty state (-inf, 0.0, acc0), without a RuntimeWarning (no
    -inf - (-inf))."""
    for empty1, empty2 in (((-math.inf, 0.0, _empty(kind, k)), (-math.inf, 0.0, _empty(kind, k))),
                           ((np.float64(-np.inf), np.float64(0.0), _empty(kind, k)),
                            (float("-inf"), -0.0, _empty(kind, k)))):
        what = f"merge_softmax_states({_show_state(empty1)}, {_show_state(empty2)})"
        got = _merge(pos, empty1, empty2, what)
        _check_state(got, (-math.inf, 0.0, _empty(kind, k)), f"{what} (the empty state)", rtol=0,
                     hint=lambda: _merge_hint(got, empty1, empty2))
        if kind == "vector":
            _new_acc_array(pos_module, empty1, empty2, what)


def test_merge_softmax_states_far_apart_maxima_without_overflow(pos, pos_module, monkeypatch):
    """Maxima 1 800 apart, or 10³⁰⁰ apart: the state with the smaller maximum gets the factor e^{-1800} = 0 (or
    e^{-10³⁰⁰}), without an overflow nor a RuntimeWarning, and no exponential of a positive number is computed."""
    rng = _rng(7264)
    for m1, m2 in ((900.0, -900.0), (-1250.5, 550.25), (4e299, -5e299), (-3e300, 7e299), (12.5, 12.5 - 760.0)):
        for kind, k in MERGE_KINDS:
            state1 = (m1, 1.0 + float(rng.exponential(3.0)), None if kind == "none" else
                      float(rng.normal() * 4.5) if kind == "number" else rng.normal(size=k) * 4.5)
            state2 = (m2, 1.0 + float(rng.exponential(3.0)), None if kind == "none" else
                      float(rng.normal() * 4.5) if kind == "number" else rng.normal(size=k) * 4.5)
            what = f"merge_softmax_states({_show_state(state1)}, {_show_state(state2)})"
            got = _merge(pos, state1, state2, what)
            top = state1 if m1 >= m2 else state2
            _check_state(got, top, f"{what} (the state with the larger maximum: e^(-{abs(m1 - m2):g}) = 0)", rtol=0,
                         hint=lambda: _merge_hint(got, state1, state2))
            _no_positive_exponential(monkeypatch, lambda: pos_module.merge_softmax_states(state1, state2), what,
                                     MERGE_HINT)


def test_merge_softmax_states_never_takes_the_exponential_of_a_positive_number(pos_module, monkeypatch):
    """No call of np.exp or math.exp on a positive number: the two exponents are m₁ - m and m₂ - m, both ≤ 0."""
    rng = _rng(7265)
    for kind, k in MERGE_KINDS:
        for t in range(3):
            state1, state2 = _random_state(rng, kind, k), _random_state(rng, kind, k)
            if t == 2:
                state1 = (-math.inf, 0.0, _empty(kind, k))
            what = f"merge_softmax_states({_show_state(state1)}, {_show_state(state2)})"
            _no_positive_exponential(monkeypatch, lambda: pos_module.merge_softmax_states(state1, state2), what,
                                     MERGE_HINT)


def test_merge_softmax_states_l_is_at_least_1(pos):
    """l ≥ 1 exactly in the merged state when m is finite: the state with the larger maximum keeps its l ≥ 1 (factor
    e^0 = 1) and the other adds a non-negative term."""
    rng = _rng(7266)
    for t in range(40):
        state1 = (float(rng.normal() * 30), 1.0, None)
        state2 = (float(rng.normal() * 30), 1.0 + float(rng.exponential(1e-15)), None) if t % 2 else \
            (-math.inf, 0.0, None)
        got = _merge(pos, state1, state2)
        assert got[1] >= 1.0, (f"expected l ≥ 1 for merge_softmax_states({_show_state(state1)}, "
                               f"{_show_state(state2)}), got {got[1]!r} ({MERGE_HINT})")


def test_merge_softmax_states_does_not_modify_its_inputs(pos_module):
    """Float arrays acc₁ and acc₂: rescaling one in place (acc₁ *= …) or adding into the other (acc₂ += …) would show;
    the merged acc is a new array."""
    for m1, m2 in ((0.75, 2.625), (3.25, -1.625), (1.125, 1.125)):
        acc1 = np.array([2.375, -1.625, 4.0])
        acc2 = np.array([-0.375, 3.25, 1.625])
        state1, state2 = (m1, 1.8125, acc1), (m2, 2.3125, acc2)
        copies = acc1.copy(), acc2.copy()
        what = f"merge_softmax_states({_show_state(state1)}, {_show_state(state2)})"
        got = _result(lambda: pos_module.merge_softmax_states(state1, state2), "a state", what, MERGE_HINT)
        assert np.array_equal(acc1, copies[0]) and np.array_equal(acc2, copies[1]), (
            f"expected acc₁ and acc₂ unchanged by {what}, got acc₁ = {_show(acc1)}, acc₂ = {_show(acc2)} (never "
            f"modify the arrays you receive: acc1 *= … or acc2 += … write into them)")
        acc = got[2] if isinstance(got, tuple) and len(got) == 3 else None
        assert isinstance(acc, np.ndarray) and not (np.shares_memory(acc, acc1) or np.shares_memory(acc, acc2)), (
            f"expected a new array as acc for {what}, got {_show_any(acc)}")


STATE_REFUSALS = [
    ([0.625, 1.375, None], (0.25, 1.0, None), "state1 is a list, not a tuple"),
    ((0.625, 1.375), (0.25, 1.0, None), "state1 has two elements"),
    ((0.625, 1.375, None), (0.25, 1.0, None, 3.0), "state2 has four elements"),
    (None, (0.25, 1.0, None), "state1 is None"), ((0.625, 1.375, None), 3.0, "state2 is a number"),
    ((math.nan, 1.375, None), (0.25, 1.0, None), "m₁ is nan"),
    ((0.625, 1.375, None), (math.inf, 1.0, None), "m₂ is +inf"),
    (("0.625", 1.375, None), (0.25, 1.0, None), "m₁ is a string"),
    ((None, 1.375, None), (0.25, 1.0, None), "m₁ is None"),
    ((0.5, math.nan, None), (0.25, 1.0, None), "l₁ is nan"), ((0.5, math.inf, None), (0.25, 1.0, None), "l₁ is inf"),
    ((0.5, -2.0, None), (0.25, 1.0, None), "l₁ is negative"),
    ((0.5, 0.75, None), (0.25, 1.0, None), "l₁ = 0.75 < 1 although m₁ is finite"),
    ((0.625, 1.375, 1.625), (0.25, 0.0, 2.0), "l₂ = 0 although m₂ is finite"),
    ((-math.inf, 1.0, None), (0.25, 1.0, None), "m₁ = -inf but l₁ = 1 (no score: l must be 0)"),
    ((-math.inf, 0.0, 2.0), (0.25, 1.625, 3.0), "m₁ = -inf but acc₁ = 2 (no score: acc must be 0)"),
    ((0.25, 1.625, np.array([1.0, 2.0])), (-math.inf, 0.0, np.array([0.0, 1.0])), "m₂ = -inf but acc₂ is not zero"),
    ((0.625, 1.375, math.nan), (0.25, 1.0, 2.0), "acc₁ is nan"),
    ((0.625, 1.375, 1.0), (0.25, 1.0, -math.inf), "acc₂ is -inf"),
    ((0.625, 1.375, np.array([1.0, np.nan])), (0.25, 1.0, np.array([0.0, 1.0])), "acc₁ holds nan"),
    ((0.625, 1.375, np.ones((2, 2))), (0.25, 1.0, np.ones((2, 2))), "acc is 2-D"),
    ((0.625, 1.375, "x"), (0.25, 1.0, "y"), "acc is a string"),
    ((0.625, 1.375, None), (0.25, 1.0, 2.0), "acc₁ is None and acc₂ a number"),
    ((0.625, 1.375, 3.0), (0.25, 1.0, np.array([1.0, 2.0])), "acc₁ is a number and acc₂ an array"),
    ((0.625, 1.375, np.array([3.0])), (0.25, 1.0, None), "acc₁ is an array and acc₂ None"),
    ((0.625, 1.375, np.array([3.0, 1.0])), (0.25, 1.0, np.array([1.0, 2.0, 0.5])), "acc of lengths 2 and 3"),
    ((0.625, 1.375, np.array([3.0])), (0.25, 1.0, np.array([1.0, 2.0, 0.5])),
     "acc of lengths 1 and 3 (NumPy would broadcast them)"),
    ((-math.inf, 0.0, None), (0.25, 1.625, 3.0), "the empty state with acc None and a state with a number"),
    ((0.25, 1.625, np.array([3.0, 1.0])), (-math.inf, 0.0, 0.0),
     "a state with an array and the empty state with 0.0"),
    ((-math.inf, 0.0, np.zeros(2)), (0.25, 1.625, np.array([3.0, 1.0, 2.0])), "the empty state of length 2 and a state "
                                                                            "of length 3"),
    ((-math.inf, 0.0, None), (-math.inf, 0.0, 0.0), "two empty states of different kinds"),
]
STATE_REFUSAL_IDS = ["list", "two-elements", "four-elements", "none", "number", "m-nan", "m-plus-inf", "m-string",
                     "m-none", "l-nan", "l-inf", "l-negative", "l-below-1", "l-zero-finite-m", "l-not-zero-empty",
                     "acc-not-zero-empty", "acc-array-not-zero-empty", "acc-nan", "acc-minus-inf", "acc-array-nan",
                     "acc-two-d", "acc-string", "none-and-number", "number-and-array", "array-and-none",
                     "lengths-2-3", "lengths-1-3", "empty-none-with-number", "empty-number-with-array",
                     "empty-length-2-with-3", "two-empty-kinds"]


@pytest.mark.parametrize("state1, state2, why", STATE_REFUSALS, ids=STATE_REFUSAL_IDS)
def test_merge_softmax_states_refusals(pos, state1, state2, why):
    _expect_error(ValueError, lambda: pos.merge_softmax_states(state1, state2),
                  f"merge_softmax_states({state1!r}, {state2!r})", why)
