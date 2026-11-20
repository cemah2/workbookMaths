"""Tests of mymath.gaussian_paths (chapter MB5): the means and the variances of a linear Gaussian recursion followed
step by step, the optimal denoiser E[x | y] of a measurement y = a x + b n when x follows a mixture of Gaussians
(points included), and the methods of Euler and of the midpoint for a velocity field f(t, x) that depends on time,
forward or backward.

Oracles: for the recursion, the unrolled formula (cumulative products and the sum of the docstring) and the recursion
itself computed exactly in ``fractions`` from the floats received, and a simulation of many paths with a fixed seed;
for the denoiser, ``scipy.integrate.quad`` on the posterior density of x (and exact sums for the point masses),
Tweedie's formula E[x | y] = (y + b² (ln p_Y)′(y)) / a with the derivative of ln p_Y (``scipy.stats.norm`` and
``scipy.special.logsumexp``) taken by finite differences, ``scipy.special.softmax`` for a set of points, the
conditioning of the joint law of (x, y) for a single Gaussian (M25a), and a simulation of (x, y) pairs whose mean
squared error no other function of y beats; for the two methods, ``scipy.integrate.solve_ivp`` at a tight tolerance
(the error at t1, and at every t_k, divided by 2 for Euler and by 4 for the midpoint when the number of steps doubles),
exact solutions (a velocity constant along the path, a velocity affine in t), the sums of Riemann at the left and at
the midpoint (M02a) for a velocity of time only, and the products of the factors of one step for a linear field
(``np.cumprod``, ``np.linalg.matrix_power``). Never another function of yours.
Plus properties: for the recursion, mean0 that scales the means only, var0 that adds the squared products, b_t and
-b_t, negative coefficients, a coefficient 0 that forgets the past, no noise, the stationary law of a coefficient
constant below 1 in absolute value, a random walk, T = 0 and the defaults; for the denoiser, a = 0 (the mean of the
mixture), weights 0, components permuted or split, a negative gain, a change of scale of the signal or of the
measurement, a result that grows with y when a > 0, far measurements (logarithms needed), one log-sum-exp per
measurement, many points and measurements quickly; for the two methods, the number of evaluations of f and where they
are made, t1 < t0 and t1 = t0, several coordinates or points at once, many steps quickly, and a field that is never
called more than needed (a version that takes useless steps fails at once). Exact types and shapes, inputs left
unchanged (floats that are not dyadic), lists, NumPy integers, and every refusal of the docstrings. They describe the
expected behaviour without showing the solution.

    pytest tests/test_mb5_gaussian_paths.py              # your code
    pytest tests/test_mb5_gaussian_paths.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import threading
import warnings
from fractions import Fraction

import numpy as np
import pytest
from scipy import integrate, special, stats


@pytest.fixture
def gp_module(mymath_module):
    """The module itself: for the tests that check that your functions never write into the arrays they receive, and
    for the check of what the module uses."""
    return mymath_module("gaussian_paths")


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
def gp(gp_module):
    return _OnCopies(gp_module)


def _text(hint):
    """A hint given as a text or as a function that computes it (only when a test fails)."""
    if not callable(hint):
        return hint
    try:
        return hint()
    except Exception:  # noqa: BLE001 - a hint must never hide the failure it explains
        return ""


LOG_OF_ZERO = "divide by zero encountered in log"     # np.log of a weight 0 gives -inf: allowed


def _result(call, expected, what="", hint="", allow_log_of_zero=False):
    """call(), any error other than NotImplementedError (and any RuntimeWarning: a division by 0, an overflow, an
    invalid value…) being reported with what was expected first."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)
        if allow_log_of_zero:
            warnings.filterwarnings("ignore", message=LOG_OF_ZERO, category=RuntimeWarning)
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


def _within(seconds, call, what, expected, hint="", allow_log_of_zero=False):
    """_result(call, …) in a thread that is given `seconds` to answer: a result that never comes fails the test
    instead of blocking it (the thread is left to finish on its own, and every later call fails at once, so that the
    tests end quickly)."""
    if _TOO_SLOW:
        pytest.fail(f"expected {expected} for {what} in little time, but an earlier call, {_TOO_SLOW[0]}, gave no "
                    f"result after {seconds} s ({_text(hint)})")
    box = {}

    def target():
        try:
            box["value"] = _result(call, expected, what, hint, allow_log_of_zero)
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
    """_show for something that may not be an array of numbers (a pair of arrays, a list…)."""
    if isinstance(v, tuple):
        return "(" + ", ".join(_show_any(x) for x in v) + ")"
    try:
        return _show(v) + (f" (dtype {v.dtype}, shape {v.shape})" if isinstance(v, np.ndarray) else
                           f" ({type(v).__name__})")
    except (TypeError, ValueError):
        return repr(v)


def _same(got, value, rtol=1e-12, atol=1e-14):
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
    """Why got differs from want, in a few words: the largest gap, where it is, and the two values there."""
    try:
        g = np.asarray(got, dtype=float)
        w = np.asarray(want, dtype=float)
    except (TypeError, ValueError):
        return ""
    if g.shape != w.shape:
        return f" (shape {g.shape} instead of {w.shape})"
    if not np.all(np.isfinite(g)):
        bad = tuple(int(i) for i in np.argwhere(~np.isfinite(g))[0]) if g.ndim else ()
        return f" (the result holds nan or inf, first at {bad if len(bad) != 1 else bad[0]})"
    if g.size:
        d = np.abs(g - w)
        k = np.unravel_index(int(np.argmax(d)), d.shape)
        where = tuple(int(i) for i in k) if d.ndim > 1 else (int(k[0]) if d.ndim else "the single entry")
        return f" (largest gap {float(d[k]):.1e}, at {where}: expected {float(w[k]):.10g}, got {float(g[k]):.10g})"
    return ""


def _close(got, want, what, rtol=1e-12, atol=1e-14, hint=""):
    if _same(got, want, rtol, atol):
        return
    hint = _text(hint)
    pytest.fail(f"expected {what} = {_show(want)}, got {_show_any(got)}{_gap(got, want)}"
                + (f" ({hint})" if hint else ""))


def _first_match(got, want, candidates, rtol=1e-9, atol=1e-11):
    """The texts of the classic errors whose value got matches (and that differ from the right value), joined by
    « or » when several errors give the same value here; "" when none does."""
    texts = [text for value, text in candidates
             if value is not None and not _same(value, want, rtol, atol) and _same(got, value, rtol, atol)]
    return " — or ".join(dict.fromkeys(texts))


def _rng(seed, case=None):
    """The generator of a test (seeds 7600 to 7690), one stream per case of a parametrized test."""
    return np.random.default_rng(seed if case is None else (seed, case))


# --- the rules of the chapter for the data of its tests ---------------------------------------------------------------

def _as_floats(values):
    """values as a 1-D float array, or None when they are not numbers (the data of a refusal)."""
    try:
        arr = np.atleast_1d(np.asarray(values, dtype=float))
    except (TypeError, ValueError):
        return None
    return arr.ravel() if np.all(np.isfinite(arr)) else None


def _follows_the_rules(a, b):
    """The coefficients of every test of this file follow the rules of the chapter (MB5, notes of the syllabus): never a
    pair (a, b) whose squares add up to 1, nor close to it, and never three consecutive coefficients a_t, b_t, a_t² or
    b_t² in arithmetic progression (a constant coefficient is allowed). Checked before each call; data that are not
    numbers (a refusal) are not checked."""
    a, b = _as_floats(a), _as_floats(b)
    if a is None or b is None:
        return
    n = min(a.size, b.size)
    sums = a[:n] ** 2 + b[:n] ** 2
    assert np.all(np.abs(sums - 1.0) >= 0.01), (
        f"expected test data that follow the rules of the chapter, got a pair (a, b) with a² + b² = "
        f"{_show(sums[np.abs(sums - 1.0) < 0.01])}")
    for sequence in (a, b, a ** 2, b ** 2):
        steps = np.diff(sequence)
        for i in range(steps.size - 1):
            assert steps[i] == 0 or not math.isclose(steps[i], steps[i + 1], rel_tol=1e-9, abs_tol=1e-12), (
                f"expected test data that follow the rules of the chapter, got three coefficients in arithmetic "
                f"progression: {_show(sequence[i:i + 3])}")


# --- what the module may use ----------------------------------------------------------------------------------------

def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``solve_ivp`` (from scipy.integrate import solve_ivp) → "scipy.integrate.solve_ivp".
    Relative imports (from .approx import logsumexp) are your own modules."""
    names = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname:
                    names[alias.asname] = alias.name
                else:                                     # import scipy.integrate binds the name scipy
                    names[alias.name.split(".")[0]] = alias.name.split(".")[0]
        elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
            for alias in node.names:
                names[alias.asname or alias.name] = f"{node.module}.{alias.name}"
    return names


def _where(statement):
    return statement.name if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)) else "the module level"


def _uses(tree, names):
    """Each use of an imported name (or of a chain of attributes on it): (where, dotted path), e.g.
    ("euler_ode", "scipy.integrate.solve_ivp"); ``where`` is the top-level function, or "the module level"."""
    inner = {id(node.value) for node in ast.walk(tree) if isinstance(node, ast.Attribute)}
    uses = []
    for statement in tree.body:
        where = _where(statement)
        for node in ast.walk(statement):
            if not isinstance(node, (ast.Name, ast.Attribute)) or id(node) in inner:
                continue                                  # only the whole chain scipy.integrate.solve_ivp
            attrs = []
            while isinstance(node, ast.Attribute):
                attrs.append(node.attr)
                node = node.value
            if isinstance(node, ast.Name) and node.id in names:
                uses.append((where, ".".join([names[node.id]] + attrs[::-1])))
    return uses


FORBIDDEN_MODULES = ("scipy", "sympy", "mpmath", "statistics", "sklearn")
FORBIDDEN_STRINGS = {"scipy", "integrate", "solve_ivp", "odeint", "quad", "special", "stats"}


def _string_uses(tree):
    """getattr(…, "solve_ivp") and the like, and __import__("scipy") or importlib.import_module("scipy.integrate"): a
    forbidden name reached through a string."""
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
            if name in ("__import__", "import_module") and any(t.startswith(FORBIDDEN_MODULES) for t in texts):
                found.append(f"{name}({texts[0]!r}) in {where}")
    return found


def test_module_uses_numpy_and_math_but_no_scipy(gp_module):
    """The docstring allows NumPy and math (and your own modules, by relative imports: from .approx import logsumexp),
    and no SciPy at all: scipy.integrate.solve_ivp, odeint and quad, scipy.stats.norm, scipy.special.logsumexp and
    softmax are the oracles of the tests; nor SymPy, mpmath or statistics, which would do the same work. Only the code
    counts: a comment, a docstring or an import never used is not a use."""
    try:
        tree = ast.parse(inspect.getsource(gp_module))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = [f"{path} in {where}" for where, path in _uses(tree, _imported_names(tree))
             if path.split(".")[0] in FORBIDDEN_MODULES]
    found += _string_uses(tree)
    assert not found, (f"expected NumPy and math only (and your own modules), with no SciPy at all, found "
                       f"{sorted(set(found))} (the tests compare your results with scipy.integrate.solve_ivp and "
                       f"quad, scipy.stats.norm and scipy.special.logsumexp: np.exp, np.log, np.max, np.sum, a loop "
                       f"over the steps and the * and @ products are enough)")


# --- linear_gaussian_recursion --------------------------------------------------------------------------------------

LGR_HINT = ("the two lists start with mean0 and var0; step t (from 1) uses a[t - 1] = a_t and b[t - 1] = b_t: the "
            "new mean is a_t times the previous mean, the new variance a_t² times the previous variance plus b_t²; "
            "return two arrays of floats of T + 1 entries, the means first")


def _show_args(*values):
    return ", ".join(_show(v) if isinstance(v, (list, tuple, np.ndarray)) else repr(v) for v in values)


def _describe_lgr(a, b, mean0=None, var0=None):
    text = f"linear_gaussian_recursion({_show_args(a, b)}"
    if mean0 is not None:
        text += f", mean0={mean0!r}"
    if var0 is not None:
        text += f", var0={var0!r}"
    return text + ")"


def _lgr(gp, a, b, mean0=None, var0=None, what=None, positional=False):
    """linear_gaussian_recursion(a, b[, mean0=…][, var0=…]), its type and shapes checked: (means, variances)."""
    _follows_the_rules(a, b)
    what = what or _describe_lgr(a, b, mean0, var0)
    if positional:
        call = lambda: gp.linear_gaussian_recursion(a, b, mean0, var0)                      # noqa: E731
    else:
        kwargs = {**({} if mean0 is None else {"mean0": mean0}), **({} if var0 is None else {"var0": var0})}
        call = lambda: gp.linear_gaussian_recursion(a, b, **kwargs)                         # noqa: E731
    got = _result(call, "a tuple (means, variances) of two arrays of floats", what, LGR_HINT)
    if not (isinstance(got, tuple) and len(got) == 2):
        pytest.fail(f"expected {what} to return a tuple (means, variances) of two numpy.ndarray, got "
                    f"{type(got).__name__} {_show_any(got)} ({LGR_HINT})")
    T = len(np.asarray(a))
    for name, arr in zip(("means", "variances"), got):
        if not (isinstance(arr, np.ndarray) and arr.dtype.kind == "f" and arr.shape == (T + 1,)):
            pytest.fail(f"expected the {name} of {what} as a numpy.ndarray of T + 1 = {T + 1} floats, got "
                        f"{type(arr).__name__}" + (f" of dtype {arr.dtype} and shape {arr.shape}"
                                                   if isinstance(arr, np.ndarray) else f" {arr!r}") + f" ({LGR_HINT})")
    return got


def _exact(values):
    return [Fraction(float(v)) for v in values]


def _unrolled(a, b, mean0=0.0, var0=0.0):
    """The moments of x_0, …, x_T by the unrolled formula of the docstring, exactly (``fractions``) from the floats
    received: m_t = (a_1 ⋯ a_t) m_0 and v_t = (a_1 ⋯ a_t)² v_0 + Σ_{k ≤ t} b_k² (a_{k+1} ⋯ a_t)²."""
    A, B = _exact(a), _exact(b)
    m0, v0 = Fraction(float(mean0)), Fraction(float(var0))
    means, variances = [], []
    for t in range(len(A) + 1):
        product = math.prod(A[:t], start=Fraction(1))
        noise = sum((B[k] ** 2 * math.prod(A[k + 1:t], start=Fraction(1)) ** 2 for k in range(t)), Fraction(0))
        means.append(product * m0)
        variances.append(product ** 2 * v0 + noise)
    return np.array([float(m) for m in means]), np.array([float(v) for v in variances])


def _stepwise(a, b, mean0=0.0, var0=0.0):
    """The moments by the recursion m_t = a_t m_{t-1}, v_t = a_t² v_{t-1} + b_t², exactly (``fractions``)."""
    m, v = Fraction(float(mean0)), Fraction(float(var0))
    means, variances = [m], [v]
    for at, bt in zip(_exact(a), _exact(b)):
        m, v = at * m, at * at * v + bt * bt
        means.append(m)
        variances.append(v)
    return np.array([float(x) for x in means]), np.array([float(x) for x in variances])


def _variant(a, b, mean0, var0, square_a=True, square_b=True, noise_inside=False, abs_a=False, start=None):
    """The moments computed with a classic error (in floats): a or b not squared, the noise added before the
    multiplication, |a_t| for the means, another starting variance."""
    m, v = float(mean0), float(var0) if start is None else start
    means, variances = [m], [v]
    for at, bt in zip(np.asarray(a, dtype=float), np.asarray(b, dtype=float)):
        m = (abs(at) if abs_a else at) * m
        factor = at * at if square_a else at
        noise = bt * bt if square_b else bt
        v = factor * (v + noise) if noise_inside else factor * v + noise
        means.append(m)
        variances.append(v)
    return np.array(means), np.array(variances)


def _lgr_hint(got, a, b, mean0, var0):
    """LGR_HINT, with the classic error that (means, variances) matches, if any (exact values for a few steps, floats
    beyond)."""
    want_m, want_v = _unrolled(a, b, mean0, var0) if len(a) <= 16 else _variant(a, b, mean0, var0)
    got_m, got_v = got
    texts = []
    if not _same(got_m, want_m, 1e-9, 1e-12):
        texts.append(_first_match(got_m, want_m, [
            (_variant(a, b, mean0, var0, abs_a=True)[0], "the means are multiplied by |a_t| instead of a_t: a "
                                                          "negative coefficient changes the sign of the mean"),
            (want_v if _same(got_v, want_m, 1e-9, 1e-12) else None, "the means and the variances are swapped")]))
    if not _same(got_v, want_v, 1e-9, 1e-12):
        texts.append(_first_match(got_v, want_v, [
            (_variant(a, b, mean0, var0, square_a=False)[1], "the previous variance is multiplied by a_t, not by a_t² "
                                                              "(the variance of a_t x is a_t² times that of x)"),
            (_variant(a, b, mean0, var0, square_b=False)[1], "b_t is added to the variance, not b_t² (the variance of "
                                                              "b_t ε_t is b_t²)"),
            (_variant(a, b, mean0, var0, noise_inside=True)[1], "the noise b_t² is added before the multiplication by "
                                                                 "a_t²: it comes after it"),
            (_variant(a, b, mean0, var0, start=float(var0) ** 2)[1], "var0 is a variance, not a standard deviation: "
                                                                      "do not square it"),
            (np.concatenate([[float(var0)], _variant(a, b, mean0, 0.0)[1][1:]]),
             "the recursion starts from the variance var0 of x_0, not from 0"),
            (np.sqrt(np.abs(want_v)), "these are standard deviations: return the variances"),
            (want_m if _same(got_m, want_v, 1e-9, 1e-12) else None, "the means and the variances are swapped")]))
    texts = list(dict.fromkeys(t for t in texts if t))
    return f"here {'; '.join(texts)}; {LGR_HINT}" if texts else LGR_HINT


def _check_lgr(got, a, b, mean0, var0, what, rtol=1e-12, want=None):
    """got equal to the moments of the unrolled formula (or to want), each array compared with its own scale."""
    want_m, want_v = _unrolled(a, b, mean0, var0) if want is None else want
    hint = lambda: _lgr_hint(got, a, b, mean0, var0)                          # noqa: E731
    _close(got[0], want_m, f"the means of {what}", rtol=rtol, atol=1e-14 * (1 + float(np.max(np.abs(want_m)))),
           hint=hint)
    _close(got[1], want_v, f"the variances of {what}", rtol=rtol, atol=1e-14 * (1 + float(np.max(np.abs(want_v)))),
           hint=hint)


def _coefficients(rng, T, a_range=(-1.6, 1.6), b_range=(0.15, 1.4)):
    """T coefficients a_t and b_t (b_t of random sign) drawn at random, a pair being drawn again while a_t² + b_t² is
    within 0.05 of 1."""
    a, b = [], []
    while len(a) < T:
        at = float(rng.uniform(*a_range))
        bt = float(rng.uniform(*b_range) * rng.choice([-1.0, 1.0]))
        if abs(at * at + bt * bt - 1.0) >= 0.05:
            a.append(at)
            b.append(bt)
    return np.array(a), np.array(b)


LENGTHS = [1, 2, 3, 4, 6, 9, 12]


@pytest.mark.parametrize("T", LENGTHS, ids=[f"T{T}" for T in LENGTHS])
def test_linear_gaussian_recursion_matches_the_exact_formula_in_fractions(gp, T):
    """Random coefficients (negative a_t included), several starts: the unrolled formula and the recursion of the
    docstring, both computed exactly in fractions from the floats received, agree; the result is the same up to the
    rounding of floats."""
    rng = _rng(7600, LENGTHS.index(T))
    for k in range(4):
        a, b = _coefficients(rng, T)
        mean0 = float(np.round(rng.normal() * 3.0, 3)) if k else 0.0
        var0 = float(np.round(rng.uniform(0.1, 2.5), 3)) if k % 2 else 0.0
        want = _unrolled(a, b, mean0, var0)
        assert all(np.array_equal(x, y) for x, y in zip(want, _stepwise(a, b, mean0, var0))), (
            "expected the two exact oracles to agree")
        what = _describe_lgr(a, b, mean0, var0)
        _check_lgr(_lgr(gp, a, b, mean0, var0, what), a, b, mean0, var0, what, want=want)


SIMULATIONS = [(5, 1.7, 0.0), (6, -2.3, 0.45), (4, 0.0, 2.6), (7, 3.1, 1.35)]


@pytest.mark.parametrize("T, mean0, var0", SIMULATIONS, ids=[f"T{T}-mean{m}-var{v}" for T, m, v in SIMULATIONS])
def test_linear_gaussian_recursion_matches_a_simulation_of_many_paths(gp, T, mean0, var0):
    """200 000 paths x_0 ~ N(mean0, var0), x_t = a_t x_{t-1} + b_t ε_t, drawn with a fixed seed: the empirical mean
    and variance of each x_t are within 5 standard errors of the result."""
    rng = _rng(7601, SIMULATIONS.index((T, mean0, var0)))
    a, b = _coefficients(rng, T, a_range=(-1.3, 1.3), b_range=(0.3, 1.2))
    n = 200_000
    x = mean0 + math.sqrt(var0) * rng.standard_normal(n)
    empirical = [(x.mean(), x.var(ddof=1))]
    for at, bt in zip(a, b):
        x = at * x + bt * rng.standard_normal(n)
        empirical.append((x.mean(), x.var(ddof=1)))
    what = _describe_lgr(a, b, mean0, var0)
    means, variances = _lgr(gp, a, b, mean0, var0, what)
    for t, (m_hat, v_hat) in enumerate(empirical):
        v = float(variances[t])
        if not (np.isfinite(means[t]) and np.isfinite(v) and v >= 0):
            pytest.fail(f"expected the mean and the variance of x_{t} for {what}, finite and a variance ≥ 0, got "
                        f"{means[t]!r} and {variances[t]!r} ({_lgr_hint((means, variances), a, b, mean0, var0)})")
        if t == 0 and var0 == 0:
            continue
        se_mean, se_var = math.sqrt(v / n), v * math.sqrt(2 / (n - 1))
        if abs(means[t] - m_hat) > 5 * se_mean + 1e-12 or abs(v - v_hat) > 5 * se_var + 1e-12:
            pytest.fail(f"expected the mean and the variance of x_{t} for {what} close to those of 200 000 simulated "
                        f"paths, {m_hat:.5f} (± {5 * se_mean:.1e}) and {v_hat:.5f} (± {5 * se_var:.1e}), got "
                        f"{float(means[t]):.5f} and {v:.5f} ({_lgr_hint((means, variances), a, b, mean0, var0)})")


def test_linear_gaussian_recursion_from_a_known_start_at_1_the_means_are_cumulative_products(gp):
    """mean0 = 1 and var0 = 0: the means are 1, a_1, a_1 a_2, … (np.cumprod), and the variances those of the unrolled
    formula."""
    rng = _rng(7602)
    for T in (3, 5, 8, 11):
        a, b = _coefficients(rng, T)
        what = _describe_lgr(a, b, 1.0, 0.0)
        got = _lgr(gp, a, b, 1.0, 0.0, what)
        _close(got[0], np.concatenate([[1.0], np.cumprod(a)]), f"the means of {what} (cumulative products)",
               hint=lambda: _lgr_hint(got, a, b, 1.0, 0.0))
        _check_lgr(got, a, b, 1.0, 0.0, what)


def test_linear_gaussian_recursion_mean0_scales_the_means_and_leaves_the_variances(gp):
    """Multiplying mean0 by c multiplies every mean by c; the variances do not depend on mean0."""
    rng = _rng(7603)
    for k in range(5):
        a, b = _coefficients(rng, int(rng.integers(2, 9)))
        var0 = float(rng.uniform(0.0, 2.0))
        mean0 = float(rng.normal() * 2.0)
        c = float(rng.uniform(-3.0, 3.0))
        base = _lgr(gp, a, b, mean0, var0)
        what = _describe_lgr(a, b, c * mean0, var0)
        got = _lgr(gp, a, b, c * mean0, var0, what)
        _close(got[0], c * base[0], f"the means of {what} ({c:.6g} times those with mean0 = {mean0:.6g})",
               rtol=1e-12, atol=1e-13, hint=LGR_HINT)
        _close(got[1], base[1], f"the variances of {what} (the same whatever mean0)", rtol=1e-14, atol=0,
               hint=LGR_HINT)
        _check_lgr(got, a, b, c * mean0, var0, what)


def test_linear_gaussian_recursion_var0_adds_the_squared_cumulative_products(gp):
    """An uncertain start adds (a_1 ⋯ a_t)² var0 to the variance of x_t."""
    rng = _rng(7604)
    for k in range(5):
        a, b = _coefficients(rng, int(rng.integers(2, 9)))
        mean0 = float(rng.normal())
        var0 = float(rng.uniform(0.2, 3.0))
        known = _lgr(gp, a, b, mean0, 0.0)
        what = _describe_lgr(a, b, mean0, var0)
        got = _lgr(gp, a, b, mean0, var0, what)
        squares = np.concatenate([[1.0], np.cumprod(a)]) ** 2
        _close(got[1] - known[1], squares * var0, f"the variances of {what} minus those with var0 = 0 (the squared "
               f"cumulative products times var0)", rtol=1e-10, atol=1e-12 * (1 + float(np.max(got[1]))),
               hint=lambda: _lgr_hint(got, a, b, mean0, var0))
        _check_lgr(got, a, b, mean0, var0, what)


def test_linear_gaussian_recursion_only_b_squared_matters(gp):
    """b_t and -b_t give the same law: changing the signs of the b_t changes nothing."""
    rng = _rng(7605)
    for k in range(5):
        a, b = _coefficients(rng, int(rng.integers(2, 9)))
        mean0, var0 = float(rng.normal()), float(rng.uniform(0.0, 1.5))
        base = _lgr(gp, a, np.abs(b), mean0, var0)
        for signs in (-np.ones(b.size), rng.choice([-1.0, 1.0], size=b.size)):
            what = _describe_lgr(a, signs * np.abs(b), mean0, var0)
            got = _lgr(gp, a, signs * np.abs(b), mean0, var0, what)
            _close(got[1], base[1], f"the variances of {what} (the same as with |b_t|)", rtol=1e-14, atol=0,
                   hint=lambda: _lgr_hint(got, a, signs * np.abs(b), mean0, var0))
            _close(got[0], base[0], f"the means of {what} (b does not change them)", rtol=1e-14, atol=0,
                   hint=LGR_HINT)


def test_linear_gaussian_recursion_negative_coefficients_flip_the_mean_not_the_variance(gp):
    """Negative a_t: the mean changes sign at each of them, and the variances are those obtained with |a_t|."""
    rng = _rng(7606)
    for k in range(5):
        T = int(rng.integers(3, 9))
        a, b = _coefficients(rng, T, a_range=(0.2, 1.6))
        flipped = a * np.where(np.arange(T) % 2 == k % 2, -1.0, 1.0)
        mean0, var0 = float(rng.uniform(0.5, 3.0)), float(rng.uniform(0.0, 1.0))
        what = _describe_lgr(flipped, b, mean0, var0)
        got = _lgr(gp, flipped, b, mean0, var0, what)
        _check_lgr(got, flipped, b, mean0, var0, what)
        _close(got[1], _unrolled(a, b, mean0, var0)[1], f"the variances of {what} (those with |a_t|)",
               hint=LGR_HINT)


def test_linear_gaussian_recursion_a_coefficient_zero_forgets_the_past(gp):
    """a_s = 0: x_s = b_s ε_s whatever happened before; from step s on, the mean is 0, the variance of x_s is b_s², and
    nothing depends on mean0, var0 or the coefficients before step s."""
    rng = _rng(7607)
    for k in range(5):
        T = int(rng.integers(3, 9))
        s = int(rng.integers(1, T + 1))                       # the step whose coefficient is 0 (from 1)
        a, b = _coefficients(rng, T)
        a[s - 1] = 0.0
        _follows_the_rules(a, b)
        results = []
        for case in range(2):
            mean0, var0 = float(rng.normal() * 3.0), float(rng.uniform(0.0, 4.0))
            before_a, before_b = _coefficients(rng, s - 1)
            a2, b2 = a.copy(), b.copy()
            a2[:s - 1], b2[:s - 1] = before_a, before_b
            what = _describe_lgr(a2, b2, mean0, var0)
            got = _lgr(gp, a2, b2, mean0, var0, what)
            _check_lgr(got, a2, b2, mean0, var0, what)
            if got[0][s] != 0.0 or not math.isclose(got[1][s], b[s - 1] ** 2, rel_tol=1e-14):
                pytest.fail(f"expected the mean 0 and the variance b_{s}² = {b[s - 1] ** 2:.10g} for x_{s} in {what} "
                            f"(a_{s} = 0), got {got[0][s]!r} and {got[1][s]!r} ({LGR_HINT})")
            results.append(got)
        for name, i in (("means", 0), ("variances", 1)):
            _close(results[1][i][s:], results[0][i][s:], f"the {name} of x_{s}, …, x_{T} (the same for two different "
                   f"starts and coefficients before step {s}, since a_{s} = 0)", rtol=1e-14, atol=0, hint=LGR_HINT)


def test_linear_gaussian_recursion_without_noise_the_variance_is_only_carried(gp):
    """b = 0: v_t = (a_1 ⋯ a_t)² var0, and with var0 = 0 every variance is exactly 0 (a known path)."""
    rng = _rng(7608)
    for k in range(5):
        T = int(rng.integers(2, 9))
        a = np.array([float(x) for x in rng.uniform(-1.7, 1.7, size=T) if abs(x * x - 1) >= 0.05][:T])
        while a.size < T:
            a = np.append(a, 1.35)
        b = np.zeros(a.size)
        mean0 = float(rng.normal() * 2.0)
        for var0 in (0.0, float(rng.uniform(0.3, 2.0))):
            what = _describe_lgr(a, b, mean0, var0)
            got = _lgr(gp, a, b, mean0, var0, what)
            want_v = np.concatenate([[1.0], np.cumprod(a)]) ** 2 * var0
            if var0 == 0.0 and np.any(got[1] != 0.0):
                pytest.fail(f"expected every variance of {what} to be exactly 0 (no noise, a known start), got "
                            f"{_show(got[1])} ({_lgr_hint(got, a, b, mean0, var0)})")
            _close(got[1], want_v, f"the variances of {what} (squared cumulative products times var0)",
                   rtol=1e-12, atol=0, hint=lambda: _lgr_hint(got, a, b, mean0, var0))
            _check_lgr(got, a, b, mean0, var0, what)


AR1_CASES = [(0.35, 1.3, 4.5, 0.0), (-0.73, 0.45, -2.65, 1.85), (0.87, 0.3, 1.15, 0.0), (-0.41, 1.75, 0.0, 5.8)]


@pytest.mark.parametrize("a, b, mean0, var0", AR1_CASES, ids=[f"a{a}-b{b}" for a, b, _, _ in AR1_CASES])
def test_linear_gaussian_recursion_constant_coefficient_converges_to_the_stationary_law(gp, a, b, mean0, var0):
    """A constant coefficient |a| < 1 (an autoregressive process of order 1): the stationary variance is
    v∞ = b² / (1 - a²) (a geometric sum, R5); from any start, m_t = a^t m_0 and the gap v_t - v∞ is a^{2t} (v_0 - v∞),
    so that after 240 steps the law is N(0, v∞) up to rounding."""
    T = 240
    A, B = np.full(T, a), np.full(T, b)
    what = _describe_lgr(A, B, mean0, var0) + f" (a = {a} and b = {b} at every step)"
    got = _lgr(gp, A, B, mean0, var0, what)
    stationary = b * b / (1 - a * a)
    powers = a ** np.arange(T + 1)
    hint = lambda: _lgr_hint(got, A, B, mean0, var0)                          # noqa: E731
    _close(got[0], powers * mean0, f"the means of {what} (a^t mean0)", rtol=1e-12, atol=1e-15, hint=hint)
    _close(got[1] - stationary, powers ** 2 * (var0 - stationary), f"the variances of {what} minus b² / (1 - a²) = "
           f"{stationary:.10g}", rtol=1e-9, atol=1e-13, hint=hint)
    _close(got[1][-1], stationary, f"the variance of x_{T} for {what} (the stationary variance)", rtol=1e-12,
           hint=hint)


def test_linear_gaussian_recursion_random_walk_and_explosive_coefficient(gp):
    """a = 1 at every step (a random walk): the mean stays mean0 and the variance grows by b² at each step,
    v_t = v_0 + t b²; a constant |a| > 1: v_t = a^{2t} v_0 + b² (a^{2t} - 1) / (a² - 1), no stationary law."""
    rng = _rng(7610)
    for k in range(3):
        T = int(rng.integers(5, 30))
        b = float(rng.uniform(0.2, 1.5)) * float(rng.choice([-1.0, 1.0]))
        mean0, var0 = float(rng.normal() * 2.0), float(rng.uniform(0.0, 2.0))
        A, B = np.ones(T), np.full(T, b)
        what = _describe_lgr(A, B, mean0, var0) + " (a random walk)"
        got = _lgr(gp, A, B, mean0, var0, what)
        _close(got[0], np.full(T + 1, mean0), f"the means of {what}", rtol=0, atol=0, hint=LGR_HINT)
        _close(got[1], var0 + np.arange(T + 1) * b * b, f"the variances of {what} (v_0 + t b²)", rtol=1e-13,
               hint=lambda: _lgr_hint(got, A, B, mean0, var0))
    for a, b in ((1.15, 0.65), (-1.4, 0.35)):
        T = 25
        mean0, var0 = 0.85, 0.4
        A, B = np.full(T, a), np.full(T, b)
        what = _describe_lgr(A, B, mean0, var0) + f" (a = {a} at every step)"
        got = _lgr(gp, A, B, mean0, var0, what)
        squares = (a * a) ** np.arange(T + 1)
        _close(got[1], squares * var0 + b * b * (squares - 1) / (a * a - 1), f"the variances of {what}",
               rtol=1e-11, hint=lambda: _lgr_hint(got, A, B, mean0, var0))
        _close(got[0], a ** np.arange(T + 1) * mean0, f"the means of {what}", rtol=1e-12, hint=LGR_HINT)


def test_linear_gaussian_recursion_without_steps_returns_the_start(gp):
    """T = 0 (empty a and b, as lists or arrays): the means are [mean0] and the variances [var0]."""
    for a, b in (([], []), (np.array([]), np.array([])), (np.zeros(0, dtype=int), np.zeros(0)), ((), ())):
        for mean0, var0 in ((None, None), (-1.85, 0.37), (2.65, 0.0)):
            what = _describe_lgr(a, b, mean0, var0) + " (T = 0)"
            got = _lgr(gp, a, b, mean0, var0, what)
            want = (np.array([0.0 if mean0 is None else mean0]), np.array([0.0 if var0 is None else var0]))
            _close(got[0], want[0], f"the means of {what}", rtol=0, atol=0, hint=LGR_HINT)
            _close(got[1], want[1], f"the variances of {what}", rtol=0, atol=0, hint=LGR_HINT)


def test_linear_gaussian_recursion_defaults_are_a_known_start_at_0(gp):
    """Without mean0 and var0, x_0 = 0: the means are all 0; positional and keyword arguments give the same result."""
    rng = _rng(7611)
    for k in range(4):
        a, b = _coefficients(rng, int(rng.integers(1, 8)))
        what = _describe_lgr(a, b)
        got = _lgr(gp, a, b, what=what)
        _close(got[0], np.zeros(a.size + 1), f"the means of {what} (x_0 = 0)", rtol=0, atol=0, hint=LGR_HINT)
        _check_lgr(got, a, b, 0.0, 0.0, what)
        mean0, var0 = float(rng.normal()), float(rng.uniform(0.1, 1.0))
        what = f"linear_gaussian_recursion({_show_args(a, b, mean0, var0)}) (positional)"
        got = _lgr(gp, a, b, mean0, var0, what, positional=True)
        _check_lgr(got, a, b, mean0, var0, what)


ACCEPTED_LGR = [
    (([2, -1, 3], [1, 2, -1], 3, np.int64(2)), "lists of integers, mean0 an int, var0 a NumPy int64"),
    (((1.35, -0.45, 2.05), (0.15, 1.65, -0.35), np.float64(-1.25), 0.75), "tuples, mean0 a NumPy float64"),
    ((np.array([3, -2, 1, 2], dtype=np.int32), np.array([2, 1, -3, 1], dtype=np.int32), 1, 0), "int32 arrays"),
    ((np.array([0.375, -1.625, 1.375], dtype=np.float32), np.array([0.5, 1.75, -0.125], dtype=np.float32),
      np.float32(1.5), np.float32(0.75)), "float32 arrays and float32 numbers"),
]


@pytest.mark.parametrize("args, text", ACCEPTED_LGR, ids=["int-lists", "tuples", "int32", "float32"])
def test_linear_gaussian_recursion_accepts_lists_integers_and_returns_float_arrays(gp, args, text):
    """Lists and tuples, integers (Python or NumPy), float32: the means and the variances are arrays of floats, equal to
    the exact values (these data need no rounding)."""
    a, b, mean0, var0 = args
    what = _describe_lgr(a, b, mean0, var0) + f" ({text})"
    got = _lgr(gp, a, b, mean0, var0, what)
    _check_lgr(got, a, b, mean0, var0, what, rtol=1e-15)


def test_linear_gaussian_recursion_does_not_modify_its_inputs(gp_module):
    """Float arrays that are not dyadic (squaring in place, even undone afterwards with a square root, would show),
    float64 and float32."""
    rng = _rng(7613)
    for k in range(3):
        a, b = _coefficients(rng, 6)
        for A, B in ((a, b), (a.astype(np.float32), b.astype(np.float32))):
            copies = A.copy(), B.copy()
            what = _describe_lgr(A, B, 0.35, 1.45)
            _follows_the_rules(A, B)
            _result(lambda: gp_module.linear_gaussian_recursion(A, B, mean0=0.35, var0=1.45), "(means, variances)",
                    what, LGR_HINT)
            for name, arr, copy in (("a", A, copies[0]), ("b", B, copies[1])):
                assert np.array_equal(arr, copy), (
                    f"expected {name} unchanged by {what}, got {_show(arr)} (largest change "
                    f"{float(np.max(np.abs(arr.astype(float) - copy))):.1e}; never modify the arrays you receive: "
                    f"a ** 2 or b * b make new arrays, a **= 2 writes into a)")


def test_linear_gaussian_recursion_of_many_steps_is_fast(gp):
    """T = 20 000 coefficients close to 1: the means are the cumulative products times mean0, and the variances
    P_t² (v_0 + Σ_{k ≤ t} b_k² / P_k²) with P_t = a_1 ⋯ a_t (np.cumprod and np.cumsum), in a few milliseconds."""
    rng = _rng(7614)
    T = 20_000
    a = rng.uniform(0.995, 1.005, size=T)
    b = rng.uniform(0.2, 0.6, size=T) * rng.choice([-1.0, 1.0], size=T)
    mean0, var0 = 1.65, 0.85
    _follows_the_rules(a, b)
    what = f"linear_gaussian_recursion(a, b, mean0={mean0}, var0={var0}) (T = {T})"
    got = _within(20, lambda: gp.linear_gaussian_recursion(a, b, mean0=mean0, var0=var0), what,
                  "a tuple (means, variances)", LGR_HINT)
    if not (isinstance(got, tuple) and len(got) == 2 and all(isinstance(x, np.ndarray) and x.shape == (T + 1,)
                                                             for x in got)):
        pytest.fail(f"expected {what} to return two arrays of {T + 1} floats, got {_show_any(got)} ({LGR_HINT})")
    P = np.concatenate([[1.0], np.cumprod(a)])
    variances = P ** 2 * (var0 + np.concatenate([[0.0], np.cumsum(b ** 2 / P[1:] ** 2)]))
    _close(got[0], P * mean0, f"the means of {what}", rtol=1e-10, hint=LGR_HINT)
    _close(got[1], variances, f"the variances of {what}", rtol=1e-10, hint=LGR_HINT)


GOOD_A, GOOD_B = [0.4, 1.3], [1.05, -0.2]
BAD_LGR = [
    (([[0.4, 1.3]], [[1.05, -0.2]]), {}, "a and b are 2-D"), ((GOOD_A, [[1.05, -0.2]]), {}, "b is 2-D"),
    (([[0.4], [1.3]], GOOD_B), {}, "a is a column, 2-D"), ((1.3, 1.05), {}, "a and b are numbers, not 1-D arrays"),
    (([0.4, 1.3, -0.35], GOOD_B), {}, "a has 3 entries and b 2"), ((GOOD_A, [1.05]), {}, "b has 1 entry and a 2"),
    (([0.4, np.nan], GOOD_B), {}, "a holds nan"), ((GOOD_A, [np.inf, -0.2]), {}, "b holds inf"),
    (([-np.inf, 1.3], GOOD_B), {}, "a holds -inf"), (([0.4, None], GOOD_B), {}, "a holds None"),
    (([0.4, "x"], GOOD_B), {}, "a holds a string"), (([[0.4], [1.3, 2.1]], GOOD_B), {}, "a is a ragged list"),
    ((None, GOOD_B), {}, "a is None"),
    ((GOOD_A, GOOD_B), {"mean0": np.nan}, "mean0 is nan"), ((GOOD_A, GOOD_B), {"mean0": np.inf}, "mean0 is inf"),
    ((GOOD_A, GOOD_B), {"mean0": None}, "mean0 is None"), ((GOOD_A, GOOD_B), {"mean0": True}, "mean0 is True, a bool"),
    ((GOOD_A, GOOD_B), {"mean0": np.True_}, "mean0 is np.True_, a NumPy bool"),
    ((GOOD_A, GOOD_B), {"mean0": "one"}, "mean0 is a string"), ((GOOD_A, GOOD_B), {"mean0": 1j}, "mean0 is complex"),
    ((GOOD_A, GOOD_B), {"var0": -0.37}, "var0 is negative"), ((GOOD_A, GOOD_B), {"var0": np.nan}, "var0 is nan"),
    ((GOOD_A, GOOD_B), {"var0": np.inf}, "var0 is inf"), ((GOOD_A, GOOD_B), {"var0": False}, "var0 is False, a bool"),
    ((GOOD_A, GOOD_B), {"var0": np.False_}, "var0 is np.False_, a NumPy bool"),
    ((GOOD_A, GOOD_B), {"var0": None}, "var0 is None"), ((GOOD_A, GOOD_B), {"var0": "half"}, "var0 is a string"),
]


@pytest.mark.parametrize("args, kwargs, why", BAD_LGR,
                         ids=["a-b-2d", "b-2d", "a-column", "numbers", "a-longer", "b-shorter", "a-nan", "b-inf",
                              "a-minus-inf", "a-none-entry", "a-string-entry", "a-ragged", "a-none", "mean0-nan",
                              "mean0-inf", "mean0-none", "mean0-bool", "mean0-numpy-bool", "mean0-string",
                              "mean0-complex", "var0-negative", "var0-nan", "var0-inf", "var0-bool",
                              "var0-numpy-bool", "var0-none", "var0-string"])
def test_linear_gaussian_recursion_refusals(gp, args, kwargs, why):
    _follows_the_rules(*args)
    shown = ", ".join([repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
    _expect_error(ValueError, lambda: gp.linear_gaussian_recursion(*args, **kwargs),
                  f"linear_gaussian_recursion({shown})", why)


# --- posterior_mean_mixture -----------------------------------------------------------------------------------------

PMM_HINT = ("for each component k: the variance of y given k is a² s_k² + b², and E[x | y, k] = "
            "μ_k + a s_k² (y - a μ_k) / (a² s_k² + b²); for each measurement, the logs of "
            "π_k N(y | a μ_k, a² s_k² + b²) (minus infinity when π_k = 0), minus their largest value over k, "
            "then their exponentials divided by their sum over k: the responsibilities of this measurement; "
            "E[x | y] is the average of the E[x | y, k] weighted by them, and the result has the shape of y")

LOG_ROOT_2PI = 0.5 * math.log(2 * math.pi)


def _describe_pmm(y, a, b, W, M, S):
    return f"posterior_mean_mixture({_show_args(y, a, b, W, M, S)})"


def _pmm(gp, y, a, b, W, M, S, what=None, seconds=None):
    """posterior_mean_mixture(y, a, b, W, M, S), its type and shape checked: an array of floats of the shape of y."""
    _follows_the_rules(a, b)
    what = what or _describe_pmm(y, a, b, W, M, S)
    call = lambda: gp.posterior_mean_mixture(y, a, b, W, M, S)                                # noqa: E731
    expected = "a numpy.ndarray of floats of the shape of y"
    if seconds is None:
        got = _result(call, expected, what, PMM_HINT, allow_log_of_zero=True)
    else:
        got = _within(seconds, call, what, expected, PMM_HINT, allow_log_of_zero=True)
    shape = np.shape(y)
    if not (isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape):
        pytest.fail(f"expected {what} as a numpy.ndarray of floats of shape {shape} (the shape of y"
                    + ("; a 0-d array for a single number, np.asarray(…) or .reshape(()) makes one" if shape == ()
                       else "") + f"), got {type(got).__name__}"
                    + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray)
                       else f" {got!r}") + f" ({PMM_HINT})")
    return got


def _arrays(W, M, S):
    return tuple(np.asarray(v, dtype=float) for v in (W, M, S))


def _log_normal(x, mean, var):
    return -0.5 * (x - mean) ** 2 / var - 0.5 * math.log(var) - LOG_ROOT_2PI


def _quad_mean(y, a, b, W, M, S):
    """E[x | y] for one measurement, by scipy.integrate.quad: the integrals of x p(x) p(y | x) and of p(x) p(y | x)
    over each Gaussian component (an exact sum for each point mass), all scaled by one common factor."""
    W, M, S = _arrays(W, M, S)
    keep = W > 0
    W, M, S = W[keep], M[keep], S[keep]
    top = float(np.max(np.log(W) + stats.norm.logpdf(y, a * M, np.sqrt(a * a * S + b * b))))   # a common scale
    numerator = denominator = 0.0
    for w, m, s2 in zip(W, M, S):
        lw = math.log(w)
        if s2 == 0:
            p = math.exp(lw + _log_normal(y, a * m, b * b) - top)
            numerator += p * m
            denominator += p
            continue
        s = math.sqrt(s2)

        def density(x, m=m, s2=s2, lw=lw):
            return math.exp(lw + _log_normal(x, m, s2) + _log_normal(y, a * x, b * b) - top)

        lo, hi, points = m - 14 * s, m + 14 * s, [m]
        if a != 0:
            center, width = y / a, b / abs(a)
            lo, hi = min(lo, center - 14 * width), max(hi, center + 14 * width)
            points.append(center)
        points = sorted(p for p in points if lo < p < hi)
        with warnings.catch_warnings():
            warnings.simplefilter("error", integrate.IntegrationWarning)
            z, z_error = integrate.quad(density, lo, hi, points=points, epsabs=0, epsrel=1e-13, limit=500)
            dz, dz_error = integrate.quad(lambda x: (x - m) * density(x), lo, hi, points=points,
                                          epsabs=1e-14 * z * (hi - lo), epsrel=1e-13, limit=500)
        assert z_error <= 1e-11 * z and dz_error <= 1e-11 * z * (hi - lo), "expected quad to converge (the oracle)"
        numerator += dz + m * z
        denominator += z
    return numerator / denominator


def _log_marginal(y, a, b, W, M, S):
    """ln p_Y(y), p_Y = Σ_k π_k N(a μ_k, a² s_k² + b²), by scipy.stats.norm.logpdf and scipy.special.logsumexp."""
    W, M, S = _arrays(W, M, S)
    y = np.asarray(y, dtype=float)
    logs = stats.norm.logpdf(y[..., None], a * M, np.sqrt(a * a * S + b * b))
    return special.logsumexp(logs, axis=-1, b=W)


def _tweedie(y, a, b, W, M, S):
    """E[x | y] by Tweedie's formula (y + b² (ln p_Y)′(y)) / a, the derivative taken by finite differences of order 4
    (a ≠ 0)."""
    y = np.asarray(y, dtype=float)
    d = 1e-3 * b
    L = lambda z: _log_marginal(z, a, b, W, M, S)                                      # noqa: E731
    slope = (L(y - 2 * d) - 8 * L(y - d) + 8 * L(y + d) - L(y + 2 * d)) / (12 * d)
    return (y + b * b * slope) / a


def _softmax_mean(y, a, b, W, M):
    """E[x | y] for point masses only: the average of the points weighted by scipy.special.softmax of
    ln π_k - (y - a μ_k)² / (2 b²)."""
    W, M = np.asarray(W, dtype=float), np.asarray(M, dtype=float)
    keep = W > 0
    y = np.asarray(y, dtype=float)
    logs = np.log(W[keep]) - (y[..., None] - a * M[keep]) ** 2 / (2 * b * b)
    return special.softmax(logs, axis=-1) @ M[keep]


def _variant_mean(y, a, b, W, M, S, spread=None, center=None, pull=None, shift=None):
    """E[x | y] computed with a classic error (another variance of y given k, another center of y given k, another
    pull, another center in E[x | y, k] = μ_k + pull (y - shift))."""
    W, M, S = _arrays(W, M, S)
    y = np.asarray(y, dtype=float)[..., None]
    spread = a * a * S + b * b if spread is None else spread
    center = a * M if center is None else center
    pull = a * S / (a * a * S + b * b) if pull is None else pull
    shift = a * M if shift is None else shift
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        logs = np.where(W > 0, np.log(np.where(W > 0, W, 1.0)), -np.inf) - 0.5 * np.log(spread) \
            - (y - center) ** 2 / (2 * spread)
        weights = special.softmax(logs, axis=-1)
        return np.sum(weights * (M + pull * (y - shift)), axis=-1)


def _pmm_hint(got, y, a, b, W, M, S):
    """PMM_HINT, with the classic error that got matches, if any."""
    if a == 0:
        return PMM_HINT
    Wf, Mf, Sf = _arrays(W, M, S)
    want = _variant_mean(y, a, b, W, M, S)
    text = _first_match(got, want, [
        (_variant_mean(y, a, b, W, M, S, pull=Sf / (a * a * Sf + b * b)),
         "E[x | y, k] = μ_k + a s_k² (y - a μ_k) / (a² s_k² + b²): the factor a is missing"),
        (_variant_mean(y, a, b, W, M, S, spread=a * Sf + b * b, pull=a * Sf / (a * Sf + b * b)),
         "the variance of y given k is a² s_k² + b², not a s_k² + b²"),
        (_variant_mean(y, a, b, W, M, S, spread=a * a * Sf + b, pull=a * Sf / (a * a * Sf + b)),
         "b is a scale: the variance of b n is b², not b"),
        (_variant_mean(y, a, b, W, M, S, spread=a * a * np.sqrt(Sf) + b * b,
                       pull=a * np.sqrt(Sf) / (a * a * np.sqrt(Sf) + b * b)),
         "s_k² is a variance: do not take its square root"),
        (_variant_mean(y, a, b, W, M, S, spread=a * a * Sf ** 2 + b * b, pull=a * Sf ** 2 / (a * a * Sf ** 2 + b * b)),
         "variances holds the variances s_k², not standard deviations: do not square them"),
        (_variant_mean(y, a, b, W, M, S, center=Mf),
         "the mean of y given k is a μ_k, not μ_k"),
        (_variant_mean(y, a, b, W, M, S, center=Mf, shift=Mf),
         "the mean of y given k is a μ_k, not μ_k (in the responsibilities and in E[x | y, k])"),
        (_variant_mean(y, a, b, W, M, S, spread=np.full(Mf.shape, b * b)),
         "the responsibilities need the variance of y given k, a² s_k² + b², not b² alone"),
        (_variant_mean(y, a, b, np.full(Wf.shape, 1.0 / Wf.size), M, S),
         "the responsibilities are proportional to π_k N(y | a μ_k, a² s_k² + b²): the weights π_k are missing"),
    ])
    return f"here {text}; {PMM_HINT}" if text else PMM_HINT


def _check_pmm(got, want, y, a, b, W, M, S, what, rtol=1e-10, scale_atol=1e-11):
    scale = 1.0 + float(np.max(np.abs(np.asarray(M, dtype=float))))
    _close(got, want, what, rtol=rtol, atol=scale_atol * scale, hint=lambda: _pmm_hint(got, y, a, b, W, M, S))


def _mixture(rng, K, points=0.4, spread=3.0, variances=(0.05, 2.0)):
    """K weights (non-dyadic, summing to 1; for two components, never close to 1/4 and 3/4 nor to 0.3 and 0.7), means
    and variances drawn at random; a share of point masses."""
    W = rng.dirichlet(np.full(K, 1.5))
    while K == 2 and np.min(np.abs(W[0] - np.array([0.25, 0.3, 0.7, 0.75]))) < 0.01:
        W = rng.dirichlet(np.full(K, 1.5))
    M = rng.uniform(-spread, spread, size=K)
    S = rng.uniform(*variances, size=K)
    S[rng.uniform(size=K) < points] = 0.0
    return W, M, S


def _gains(rng, a_range=(0.3, 2.5), b_range=(0.2, 1.8), sign=None):
    """(a, b) drawn at random, of random sign for a, drawn again while a² + b² or a + b is within 0.05 of 1."""
    while True:
        s = float(rng.choice([-1.0, 1.0])) if sign is None else sign
        a, b = s * float(rng.uniform(*a_range)), float(rng.uniform(*b_range))
        if abs(a * a + b * b - 1) >= 0.05 and abs(a + b - 1) >= 0.05:
            return a, b


QUAD_CASES = [(1, 0.0, 1.0), (2, 0.0, -1.0), (2, 0.5, 1.0), (3, 0.0, 1.0), (3, 0.4, -1.0), (4, 0.3, 1.0),
              (4, 0.6, -1.0), (5, 0.2, 1.0)]


@pytest.mark.parametrize("K, points, sign", QUAD_CASES, ids=[f"K{K}-points{p}-{'neg' if s < 0 else 'pos'}"
                                                              for K, p, s in QUAD_CASES])
def test_posterior_mean_mixture_matches_quad_on_the_posterior_density(gp, K, points, sign):
    """E[x | y] = ∫ x p(x) p(y | x) dx / ∫ p(x) p(y | x) dx, by scipy.integrate.quad over each Gaussian component
    (and exact sums for the point masses), for seven measurements at a time."""
    rng = _rng(7620, QUAD_CASES.index((K, points, sign)))
    for k in range(2):
        W, M, S = _mixture(rng, K, points)
        if K == 1 or not np.any(S > 0):
            S[0] = float(rng.uniform(0.2, 1.5))
        a, b = _gains(rng, sign=sign)
        y = rng.uniform(-5.0, 5.0, size=7) * max(1.0, abs(a))
        what = _describe_pmm(y, a, b, W, M, S)
        want = np.array([_quad_mean(float(v), a, b, W, M, S) for v in y])
        _check_pmm(_pmm(gp, y, a, b, W, M, S, what), want, y, a, b, W, M, S, what)


TWEEDIE_KS = [1, 2, 3, 5, 8]


@pytest.mark.parametrize("K", TWEEDIE_KS, ids=[f"K{K}" for K in TWEEDIE_KS])
def test_posterior_mean_mixture_matches_tweedie_by_finite_differences(gp, K):
    """Tweedie's formula, E[x | y] = (y + b² (ln p_Y)′(y)) / a, with ln p_Y by scipy.stats.norm.logpdf and
    scipy.special.logsumexp and its derivative by finite differences, for measurements from -12 to 12."""
    rng = _rng(7621, TWEEDIE_KS.index(K))
    for k in range(4):
        W, M, S = _mixture(rng, K, points=0.4)
        a, b = _gains(rng)
        y = np.sort(rng.uniform(-12.0, 12.0, size=15))
        what = _describe_pmm(y, a, b, W, M, S)
        _check_pmm(_pmm(gp, y, a, b, W, M, S, what), _tweedie(y, a, b, W, M, S), y, a, b, W, M, S, what,
                   rtol=1e-8, scale_atol=1e-8)


def test_posterior_mean_mixture_of_one_gaussian_is_the_linear_gaussian_model(gp):
    """K = 1, x ~ N(μ, s²): (x, y) = (x, a x + b n) is a Gaussian vector of covariance [[s², a s²], [a s², a² s² + b²]]
    (M25a), and E[x | y] = μ + Cov(x, y) (y - a μ) / V(y), affine in y; a point mass (s² = 0) gives μ whatever y."""
    rng = _rng(7622)
    for k in range(6):
        mu, s2 = float(rng.normal() * 2.0), float(rng.uniform(0.1, 3.0))
        a, b = _gains(rng)
        L = np.array([[math.sqrt(s2), 0.0], [a * math.sqrt(s2), b]])          # (x, y) = (μ, a μ) + L (z, n)
        cov = L @ L.T
        y = rng.uniform(-6.0, 6.0, size=9)
        want = mu + cov[0, 1] * (y - a * mu) / cov[1, 1]
        what = _describe_pmm(y, a, b, [1.0], [mu], [s2])
        _check_pmm(_pmm(gp, y, a, b, [1.0], [mu], [s2], what), want, y, a, b, [1.0], [mu], [s2], what, rtol=1e-12,
                   scale_atol=1e-13)
        what = _describe_pmm(y, a, b, [1.0], [mu], [0.0])
        _check_pmm(_pmm(gp, y, a, b, [1.0], [mu], [0.0], what), np.full(y.shape, mu), y, a, b, [1.0], [mu], [0.0],
                   what + " (a single point)", rtol=1e-14, scale_atol=0)


POINT_KS = [2, 3, 5, 8, 13]


@pytest.mark.parametrize("K", POINT_KS, ids=[f"K{K}" for K in POINT_KS])
def test_posterior_mean_mixture_of_points_is_a_softmax_average_of_the_points(gp, K):
    """Variances 0 (a set of points with their frequencies): E[x | y] is the average of the points weighted by
    scipy.special.softmax of ln π_k - (y - a μ_k)² / (2 b²); it lies between the smallest and the largest point. The
    measurements go far from the points (logs of weights down to -10³)."""
    rng = _rng(7623, POINT_KS.index(K))
    for k in range(4):
        W, M, _ = _mixture(rng, K, points=1.0)
        S = np.zeros(K)
        a, b = _gains(rng, b_range=(0.15, 1.2))
        y = np.sort(np.concatenate([rng.uniform(-4.0, 4.0, size=10) * abs(a), rng.uniform(-40.0, 40.0, size=4)]))
        what = _describe_pmm(y, a, b, W, M, S)
        got = _pmm(gp, y, a, b, W, M, S, what)
        _check_pmm(got, _softmax_mean(y, a, b, W, M), y, a, b, W, M, S, what, rtol=1e-11, scale_atol=1e-12)
        assert np.all(got >= M.min() - 1e-12) and np.all(got <= M.max() + 1e-12), (
            f"expected every value of {what} between the smallest and the largest point, {M.min():.6g} and "
            f"{M.max():.6g}, got {_show(got)} ({PMM_HINT})")


def test_posterior_mean_mixture_far_measurements_need_logarithms(gp):
    """Narrow components and points, measurements far from all of them: every π_k N(y | a μ_k, a² s_k² + b²) is below
    1e-300 (its exponential gives 0, and 0 / 0 without the largest log subtracted first); the value is that of
    Tweedie's formula (and of the softmax, for points)."""
    rng = _rng(7624)
    for k in range(6):
        K = int(rng.integers(2, 6))
        W, M, S = _mixture(rng, K, points=0.5 if k % 2 else 1.0, variances=(0.0005, 0.005))
        a, b = _gains(rng, a_range=(0.5, 1.8), b_range=(0.05, 0.2))
        centers = a * M
        y = np.array([centers.max() + 12.3, centers.min() - 14.0, 45.0 * float(rng.choice([-1, 1]))])
        assert np.all(_log_marginal(y, a, b, W, M, S) < -690), "expected far measurements (the data of the test)"
        what = _describe_pmm(y, a, b, W, M, S) + " (far measurements)"
        got = _pmm(gp, y, a, b, W, M, S, what)
        want = _softmax_mean(y, a, b, W, M) if not np.any(S > 0) else _tweedie(y, a, b, W, M, S)
        _check_pmm(got, want, y, a, b, W, M, S, what, rtol=1e-7, scale_atol=1e-7)


def test_posterior_mean_mixture_one_log_sum_exp_per_measurement(gp):
    """A measurement near the points and another far from them, in the same call: the largest log is subtracted for
    each measurement separately (one largest log for all of them leaves only zeros for the far one)."""
    rng = _rng(7625)
    for k in range(5):
        K = int(rng.integers(2, 6))
        W, M, S = _mixture(rng, K, points=1.0 if k % 2 == 0 else 0.5, variances=(0.01, 0.1))
        a, b = _gains(rng, a_range=(0.6, 1.6), b_range=(0.1, 0.3))
        near = a * float(M[0]) + 0.05
        far = a * float(M.max()) + 30.0
        for y in (np.array([near, far]), np.array([[far, near], [near - 0.4, -far]])):
            what = _describe_pmm(y, a, b, W, M, S) + " (near and far measurements together)"
            got = _pmm(gp, y, a, b, W, M, S, what)
            want = _softmax_mean(y, a, b, W, M) if not np.any(S > 0) else _tweedie(y, a, b, W, M, S)
            _check_pmm(got, want, y, a, b, W, M, S, what, rtol=1e-7, scale_atol=1e-7)


ZERO_GAINS = [0.0, -0.0, 0, np.float64(0.0)]


@pytest.mark.parametrize("case, a", list(enumerate(ZERO_GAINS)), ids=["zero", "minus-zero", "int-zero", "numpy-zero"])
def test_posterior_mean_mixture_with_a_zero_is_the_mixture_mean(gp, case, a):
    """a = 0: y says nothing about x, and E[x | y] = Σ_k π_k μ_k for every measurement (points and Gaussians, any
    shape of y)."""
    rng = _rng(7626, case)
    for k in range(3):
        W, M, S = _mixture(rng, int(rng.integers(1, 6)), points=0.5)
        b = float(rng.uniform(1.1, 2.4)) if k % 2 else float(rng.uniform(0.2, 0.85))
        for y in (float(rng.normal() * 3.0 * b), rng.normal(size=4) * 4.0 * b, rng.normal(size=(2, 3)) * 5.0 * b):
            what = _describe_pmm(y, a, b, W, M, S) + " (a = 0)"
            got = _pmm(gp, y, a, b, W, M, S, what)
            _close(got, np.full(np.shape(y), float(W @ M)), what + " (the mean of the mixture, Σ π_k μ_k)",
                   rtol=1e-12, atol=1e-13, hint=PMM_HINT)


def test_posterior_mean_mixture_a_component_of_weight_zero_counts_for_nothing(gp):
    """A component of weight 0, even right at y / a and narrow, gets a responsibility 0: the result is that of the
    mixture without it (np.log(0) = -inf is allowed)."""
    rng = _rng(7627)
    for k in range(6):
        K = int(rng.integers(2, 5))
        W, M, S = _mixture(rng, K, points=0.5)
        a, b = _gains(rng)
        y = rng.uniform(-4.0, 4.0, size=6)
        where = int(rng.integers(0, K + 1)) if k else 0               # the zero weight first, last or inside
        W0 = np.insert(W, where, 0.0)
        M0 = np.insert(M, where, float(y[0] / a))
        S0 = np.insert(S, where, 0.0 if k % 2 else 0.01)
        what = _describe_pmm(y, a, b, W0, M0, S0) + f" (the weight of component {where} is 0)"
        got = _pmm(gp, y, a, b, W0, M0, S0, what)
        _check_pmm(got, _tweedie(y, a, b, W, M, S), y, a, b, W0, M0, S0, what, rtol=1e-8, scale_atol=1e-8)


def test_posterior_mean_mixture_permuting_or_splitting_components_changes_nothing(gp):
    """The order of the components does not matter, and a component split into two equal halves (the same mean and
    variance, half the weight each) changes nothing."""
    rng = _rng(7628)
    for k in range(5):
        K = int(rng.integers(2, 6))
        W, M, S = _mixture(rng, K, points=0.4)
        a, b = _gains(rng)
        y = rng.uniform(-5.0, 5.0, size=8)
        base = _pmm(gp, y, a, b, W, M, S)
        order = rng.permutation(K)
        what = _describe_pmm(y, a, b, W[order], M[order], S[order]) + " (the components in another order)"
        _close(_pmm(gp, y, a, b, W[order], M[order], S[order], what), base, what, rtol=1e-12, atol=1e-13,
               hint=PMM_HINT)
        j = int(rng.integers(0, K))
        Ws = np.concatenate([W[:j], [W[j] / 2, W[j] / 2], W[j + 1:]])
        Ms, Ss = np.insert(M, j, M[j]), np.insert(S, j, S[j])
        what = _describe_pmm(y, a, b, Ws, Ms, Ss) + f" (component {j} split into two halves)"
        _close(_pmm(gp, y, a, b, Ws, Ms, Ss, what), base, what, rtol=1e-12, atol=1e-13, hint=PMM_HINT)


def test_posterior_mean_mixture_a_negative_gain_mirrors_the_measurement(gp):
    """y = -a x + b n is -y = a x - b n, and -n has the law of n: the result for (y, -a) is that for (-y, a)."""
    rng = _rng(7629)
    for k in range(5):
        W, M, S = _mixture(rng, int(rng.integers(1, 6)), points=0.4)
        a, b = _gains(rng, sign=1.0)
        y = rng.uniform(-6.0, 6.0, size=9)
        what = _describe_pmm(y, -a, b, W, M, S)
        _close(_pmm(gp, y, -a, b, W, M, S, what), _pmm(gp, -y, a, b, W, M, S), what + f" (the result for -y and "
               f"a = {a:.6g})", rtol=1e-12, atol=1e-13, hint=PMM_HINT)


def test_posterior_mean_mixture_changing_the_scale_of_the_signal_or_of_the_measurement(gp):
    """x′ = c x follows the mixture of means c μ_k and variances c² s_k², and y = (a / c) x′ + b n: its result is c
    times that of x. And λ y = (λ a) x + (λ b) n: the result for (λ y, λ a, λ b) is that for (y, a, b)."""
    rng = _rng(7630)
    for k in range(5):
        W, M, S = _mixture(rng, int(rng.integers(1, 6)), points=0.4)
        a, b = _gains(rng, a_range=(0.5, 2.0), b_range=(0.3, 1.5))
        y = rng.uniform(-5.0, 5.0, size=8)
        base = _pmm(gp, y, a, b, W, M, S)
        c = float(rng.uniform(1.3, 3.5)) * float(rng.choice([-1, 1]))
        what = _describe_pmm(y, a / c, b, W, c * M, c * c * S) + f" (the signal times c = {c:.6g})"
        _close(_pmm(gp, y, a / c, b, W, c * M, c * c * S, what), c * base, what, rtol=1e-10, atol=1e-11,
               hint=PMM_HINT)
        lam = float(rng.uniform(0.4, 3.0))
        what = _describe_pmm(lam * y, lam * a, lam * b, W, M, S) + f" (y, a and b times λ = {lam:.6g})"
        _close(_pmm(gp, lam * y, lam * a, lam * b, W, M, S, what), base, what, rtol=1e-10, atol=1e-11, hint=PMM_HINT)


def test_posterior_mean_mixture_grows_with_y_when_a_is_positive(gp):
    """For a > 0, a larger measurement never gives a smaller E[x | y]; for a < 0, never a larger one (360 measurements
    from -10 to 10)."""
    rng = _rng(7631)
    y = np.linspace(-10.0, 10.0, 360)
    for k in range(6):
        W, M, S = _mixture(rng, int(rng.integers(2, 7)), points=0.5)
        a, b = _gains(rng, b_range=(0.15, 1.2))
        what = _describe_pmm(y, a, b, W, M, S)
        got = _pmm(gp, y, a, b, W, M, S, what)
        steps = np.sign(a) * np.diff(got)
        if np.any(steps < -1e-12 * (1 + np.max(np.abs(M)))):
            i = int(np.argmin(steps))
            pytest.fail(f"expected {what} {'non-decreasing' if a > 0 else 'non-increasing'} in y (a = {a:.6g}), got "
                        f"{got[i]:.10g} at y = {y[i]:.6g} and {got[i + 1]:.10g} at y = {y[i + 1]:.6g} "
                        f"({_pmm_hint(got, y, a, b, W, M, S)})")


def test_posterior_mean_mixture_has_the_smallest_mean_squared_error(gp):
    """300 000 pairs (x, y) simulated with a fixed seed, x from a mixture of points and narrow Gaussians: the error
    x - E[x | y] has mean 0 (within 5 standard errors), and no other function of y does better on these pairs: a shift,
    a factor, a polynomial of degree 3 fitted to the pairs (np.polyfit), y / a, or the mean of the mixture."""
    rng = _rng(7632)
    W = np.array([0.22, 0.41, 0.37])
    M = np.array([-2.35, 0.15, 2.85])
    S = np.array([0.0, 0.04, 0.0])
    a, b = 1.4, 0.85
    n = 300_000
    k = rng.choice(3, size=n, p=W)
    x = M[k] + np.sqrt(S[k]) * rng.standard_normal(n)
    y = a * x + b * rng.standard_normal(n)
    what = f"posterior_mean_mixture(y, {a}, {b}, {W.tolist()}, {M.tolist()}, {S.tolist()}) (300 000 simulated pairs)"
    g = _pmm(gp, y, a, b, W, M, S, what, seconds=30)
    error = x - g
    mse = float(np.mean(error ** 2))
    if abs(error.mean()) > 5 * error.std() / math.sqrt(n):
        pytest.fail(f"expected the error x - E[x | y] of mean 0 for {what}, within "
                    f"{5 * error.std() / math.sqrt(n):.1e}, got {error.mean():.4g} ({PMM_HINT})")
    sd = float(x.std())
    others = {"E[x | y] + 0.1 sd(x)": g + 0.1 * sd, "1.05 E[x | y]": 1.05 * g,
              "a polynomial of degree 3 in y": np.polyval(np.polyfit(y, x, 3), y), "y / a": y / a,
              "the mean of the mixture": np.full(n, float(W @ M))}
    for name, other in others.items():
        other_mse = float(np.mean((x - other) ** 2))
        if not mse < other_mse:
            pytest.fail(f"expected the mean squared error of E[x | y] smaller than that of {name} for {what}, got "
                        f"{mse:.6g} against {other_mse:.6g} ({PMM_HINT})")


SHAPES = [(), (1,), (5,), (1, 1), (3, 4), (2, 2, 3)]


@pytest.mark.parametrize("shape", SHAPES, ids=["scalar", "one", "five", "one-by-one", "3x4", "2x2x3"])
def test_posterior_mean_mixture_keeps_the_shape_of_y(gp, shape):
    """The result has the shape of y: a 0-d array for a single number (float(…) converts it), and the same values as
    the measurements taken one by one."""
    rng = _rng(7633, SHAPES.index(shape))
    W, M, S = _mixture(rng, 3, points=0.4)
    a, b = _gains(rng)
    values = rng.uniform(-5.0, 5.0, size=shape)
    for y in ((float(values), np.float64(values), np.array(values)) if shape == () else (values, values.tolist())):
        what = _describe_pmm(y, a, b, W, M, S) + f" (y of shape {shape})"
        got = _pmm(gp, y, a, b, W, M, S, what)
        _check_pmm(got, _tweedie(np.asarray(y, dtype=float), a, b, W, M, S), y, a, b, W, M, S, what, rtol=1e-8,
                   scale_atol=1e-8)
    if shape == ():
        got = _pmm(gp, float(values), a, b, W, M, S)
        assert isinstance(float(got), float), f"expected float(…) to convert the 0-d result, got {got!r}"


ACCEPTED_PMM = [
    (([3, -1, 0, 2], 2, 1, (0.35, 0.65), [-3, 2], [0, 1]), "integers, a tuple of weights"),
    ((np.array([1, -2], dtype=np.int32), np.int64(-3), np.float64(1.3), np.array([0.45, 0.55]), np.array([1, 4]),
      np.array([2, 0], dtype=np.int64)), "NumPy integers and int arrays"),
    ((np.array([0.375, -1.125], dtype=np.float32), np.float32(1.375), np.float32(0.625),
      np.array([0.125, 0.875], dtype=np.float32), np.array([-0.375, 1.625], dtype=np.float32),
      np.array([0.375, 0.0], dtype=np.float32)), "float32 arrays and numbers"),
]


@pytest.mark.parametrize("args, text", ACCEPTED_PMM, ids=["ints", "numpy-ints", "float32"])
def test_posterior_mean_mixture_accepts_integers_lists_tuples_and_numpy_numbers(gp, args, text):
    y, a, b, W, M, S = args
    what = _describe_pmm(y, a, b, W, M, S) + f" ({text})"
    got = _pmm(gp, y, a, b, W, M, S, what)
    a, b = float(a), float(b)
    want = np.array([_quad_mean(float(v), a, b, W, M, S) for v in np.asarray(y, dtype=float)])
    _check_pmm(got, want, y, a, b, W, M, S, what, rtol=1e-10, scale_atol=1e-11)


def test_posterior_mean_mixture_weights_summing_to_1_up_to_1e_9_are_accepted(gp):
    """Weights whose sum differs from 1 by less than 1e-9 are accepted: the result is that of the weights divided by
    their sum."""
    rng = _rng(7635)
    for k, gap in enumerate((-6e-10, 8e-10, 3e-10)):
        W, M, S = _mixture(rng, 4, points=0.4)
        W = W * (1 + gap)
        a, b = _gains(rng)
        y = rng.uniform(-4.0, 4.0, size=5)
        what = _describe_pmm(y, a, b, W, M, S) + f" (weights summing to 1 {'+' if gap > 0 else '-'} {abs(gap):.0e})"
        got = _pmm(gp, y, a, b, W, M, S, what)
        _check_pmm(got, _tweedie(y, a, b, W / W.sum(), M, S), y, a, b, W, M, S, what, rtol=1e-8, scale_atol=1e-8)


def test_posterior_mean_mixture_does_not_modify_its_inputs(gp_module):
    """Float arrays that are not dyadic, weights summing to 1 + 4e-10 (a division in place by their sum would show),
    float64 and float32 (measurements, means and variances), a 2-D array of measurements; the result is a new
    array."""
    rng = _rng(7636)
    for k in range(3):
        W, M, S = _mixture(rng, 4, points=0.4)
        W = W * (1 + 4e-10)
        a, b = _gains(rng)
        y = rng.uniform(-4.0, 4.0, size=(5, 8))
        for arrays in ((y, W, M, S), (y.astype(np.float32), W, M.astype(np.float32), S.astype(np.float32))):
            copies = [v.copy() for v in arrays]
            what = _describe_pmm(*arrays[:1], a, b, *arrays[1:])
            _follows_the_rules(a, b)
            got = _result(lambda: gp_module.posterior_mean_mixture(arrays[0], a, b, *arrays[1:]), "E[x | y]", what,
                          PMM_HINT, allow_log_of_zero=True)
            for name, arr, copy in zip(("y", "weights", "means", "variances"), arrays, copies):
                assert np.array_equal(arr, copy), (
                    f"expected {name} unchanged by {what}, got {_show(arr)} (largest change "
                    f"{float(np.max(np.abs(arr.astype(float) - copy))):.1e}; never modify the arrays you receive: "
                    f"y - a * means makes a new array, y -= … writes into y)")
            assert not (isinstance(got, np.ndarray) and np.shares_memory(got, arrays[0])), (
                f"expected a new array for {what}, got an array that shares its memory with y ({PMM_HINT})")


def test_posterior_mean_mixture_of_many_points_and_measurements_is_fast(gp):
    """350 points and 20 000 measurements: the same values as the softmax of the logs of the weights, in a few tenths
    of a second (a loop in Python over the measurements may be too slow)."""
    rng = _rng(7637)
    K = 350
    W = rng.dirichlet(np.ones(K))
    M = rng.normal(size=K) * 3.0
    a, b = 1.35, 0.45
    y = rng.uniform(-8.0, 8.0, size=20_000)
    what = f"posterior_mean_mixture(y, {a}, {b}, weights, means, zeros) (20 000 measurements, {K} points)"
    got = _pmm(gp, y, a, b, W, M, np.zeros(K), what, seconds=20)
    _check_pmm(got, _softmax_mean(y, a, b, W, M), y, a, b, W, M, np.zeros(K), what, rtol=1e-10, scale_atol=1e-11)


OK_MIX = ([0.35, 0.65], [-1.4, 2.7], [0.45, 0.0])
BAD_PMM = [
    (([0.3, np.nan], 1.35, 0.85, *OK_MIX), "y holds nan"), (([np.inf, 0.3], 1.35, 0.85, *OK_MIX), "y holds inf"),
    ((-np.inf, 1.35, 0.85, *OK_MIX), "y is -inf"), ((None, 1.35, 0.85, *OK_MIX), "y is None"),
    (("y", 1.35, 0.85, *OK_MIX), "y is a string"), (([[0.4], [1.1, 2.0]], 1.35, 0.85, *OK_MIX), "y is ragged"),
    ((0.4, np.nan, 0.85, *OK_MIX), "a is nan"), ((0.4, np.inf, 0.85, *OK_MIX), "a is inf"),
    ((0.4, None, 0.85, *OK_MIX), "a is None"), ((0.4, True, 0.85, *OK_MIX), "a is True, a bool"),
    ((0.4, np.True_, 0.85, *OK_MIX), "a is np.True_, a NumPy bool"), ((0.4, "gain", 0.85, *OK_MIX), "a is a string"),
    ((0.4, 1.35, 0.0, *OK_MIX), "b = 0: no noise"), ((0.4, 1.35, -0.85, *OK_MIX), "b is negative"),
    ((0.4, 1.35, np.nan, *OK_MIX), "b is nan"), ((0.4, 1.35, np.inf, *OK_MIX), "b is inf"),
    ((0.4, 1.35, True, *OK_MIX), "b is True, a bool"), ((0.4, 1.35, np.True_, *OK_MIX), "b is np.True_"),
    ((0.4, 1.35, None, *OK_MIX), "b is None"), ((0.4, 1.35, "two", *OK_MIX), "b is a string"),
    ((0.4, 1.35, 0.85, [[0.35, 0.65]], [-1.4, 2.7], [0.45, 0.0]), "weights is 2-D"),
    ((0.4, 1.35, 0.85, [], [], []), "no component (K = 0)"),
    ((0.4, 1.35, 0.85, [0.35, 0.65], [-1.4, 2.7, 0.15], [0.45, 0.0, 1.0]), "2 weights for 3 means and variances"),
    ((0.4, 1.35, 0.85, [0.35, 0.65], [-1.4], [0.45, 0.0]), "1 mean for 2 weights"),
    ((0.4, 1.35, 0.85, [0.35, 0.65], [-1.4, 2.7], [0.45]), "1 variance for 2 weights"),
    ((0.4, 1.35, 0.85, [1.2, -0.2], [-1.4, 2.7], [0.45, 0.0]), "a negative weight (the sum is 1)"),
    ((0.4, 1.35, 0.85, [0.4, 0.65], [-1.4, 2.7], [0.45, 0.0]), "the weights sum to 1.05"),
    ((0.4, 1.35, 0.85, [0.3, 0.55], [-1.4, 2.7], [0.45, 0.0]), "the weights sum to 0.85"),
    ((0.4, 1.35, 0.85, [0.35 + 1e-6, 0.65], [-1.4, 2.7], [0.45, 0.0]), "the weights sum to 1 + 1e-6, beyond 1e-9"),
    ((0.4, 1.35, 0.85, [0.35 - 1e-7, 0.65], [-1.4, 2.7], [0.45, 0.0]), "the weights sum to 1 - 1e-7, beyond 1e-9"),
    ((0.4, 1.35, 0.85, [np.nan, 0.65], [-1.4, 2.7], [0.45, 0.0]), "a weight is nan"),
    ((0.4, 1.35, 0.85, [0.35, 0.65], [np.nan, 2.7], [0.45, 0.0]), "a mean is nan"),
    ((0.4, 1.35, 0.85, [0.35, 0.65], [-1.4, np.inf], [0.45, 0.0]), "a mean is inf"),
    ((0.4, 1.35, 0.85, [0.35, 0.65], [[-1.4, 2.7]], [0.45, 0.0]), "means is 2-D"),
    ((0.4, 1.35, 0.85, [0.35, 0.65], [-1.4, 2.7], [-0.1, 0.0]), "a variance is negative"),
    ((0.4, 1.35, 0.85, [0.35, 0.65], [-1.4, 2.7], [np.nan, 0.0]), "a variance is nan"),
    ((0.4, 1.35, 0.85, [0.35, 0.65], [-1.4, 2.7], [0.45, np.inf]), "a variance is inf"),
]


@pytest.mark.parametrize("args, why", BAD_PMM,
                         ids=["y-nan", "y-inf", "y-minus-inf", "y-none", "y-string", "y-ragged", "a-nan", "a-inf",
                              "a-none", "a-bool", "a-numpy-bool", "a-string", "b-zero", "b-negative", "b-nan", "b-inf",
                              "b-bool", "b-numpy-bool", "b-none", "b-string", "weights-2d", "no-component",
                              "lengths-weights-means", "lengths-means", "lengths-variances", "negative-weight",
                              "sum-above", "sum-below", "sum-1e-6", "sum-1e-7", "weight-nan", "mean-nan", "mean-inf",
                              "means-2d", "variance-negative", "variance-nan", "variance-inf"])
def test_posterior_mean_mixture_refusals(gp, args, why):
    _follows_the_rules(args[1], args[2])
    shown = ", ".join(repr(a) for a in args)
    _expect_error(ValueError, lambda: gp.posterior_mean_mixture(*args), f"posterior_mean_mixture({shown})", why)


# --- euler_ode and midpoint_ode: shared tools -----------------------------------------------------------------------

EULER_HINT = ("h = (t1 - t0) / n_steps and t_k = t0 + k h; x = a float copy of x0, then n_steps times: the velocity "
              "v = f(t_k, x_k), read at the start of the step and checked to have the shape of x0, and "
              "x_{k+1} = x_k + h v; keep every point, x0 included, in an array of shape (n_steps + 1,) + shape of x0")
MIDPOINT_HINT = ("h = (t1 - t0) / n_steps and t_k = t0 + k h; x = a float copy of x0, then n_steps times: k1 = "
                 "f(t_k, x_k), then k2 = f(t_k + h / 2, x_k + (h / 2) k1), the velocity read at the middle of the "
                 "step, and x_{k+1} = x_k + h k2; keep every point, x0 included, in an array of shape "
                 "(n_steps + 1,) + shape of x0 (not the half-step points)")
HINTS = {"euler_ode": EULER_HINT, "midpoint_ode": MIDPOINT_HINT}
CALLS_PER_STEP = {"euler_ode": 1, "midpoint_ode": 2}
ODE_SECONDS = 30


class _Overused(RuntimeError):
    """Raised by a field called more times than a method can need."""


class _Field:
    """A velocity field f(t, x) that counts its calls, records them if asked, and fails at once past a budget: a version
    that takes useless steps, or calls a solver of SciPy, stops after a few calls instead of running on."""

    def __init__(self, velocity, budget, record=False):
        self.velocity, self.budget = velocity, budget
        self.calls, self.overused = 0, False
        self.log = [] if record else None

    def __call__(self, t, x):
        self.calls += 1
        if self.calls > self.budget:
            self.overused = True
            raise _Overused(f"f was called more than {self.budget} times")
        if self.log is not None:
            self.log.append((t, np.array(x, dtype=float)))
        return self.velocity(t, x)


def _describe_ode(method, name, x0, t0, t1, n):
    return f"{method}({name}, {_show_args(x0)}, {t0!r}, {t1!r}, {n!r})"


def _ode(gp, method, velocity, name, x0, t0, t1, n, what=None, record=False, budget=None, seconds=ODE_SECONDS):
    """euler_ode or midpoint_ode on the field velocity(t, x), its type and shape checked; with the field, to read its
    calls. The field fails past 3 times the evaluations the method needs (plus 10)."""
    what = what or _describe_ode(method, name, x0, t0, t1, n)
    evaluations = CALLS_PER_STEP[method] * int(n)
    field = _Field(velocity, budget if budget is not None else 3 * evaluations + 10, record)
    expected = f"an array of shape (n_steps + 1,) + shape of x0 = {(int(n) + 1,) + np.shape(x0)}"
    overused = (f"expected {evaluations} evaluations of f for {what} ({CALLS_PER_STEP[method]} per step), got more "
                f"than {field.budget} ({HINTS[method]})")
    try:
        got = _within(seconds, lambda: getattr(gp, method)(field, x0, t0, t1, n), what, expected, HINTS[method])
    except BaseException:
        if field.overused:
            pytest.fail(overused)
        raise
    if field.overused:
        pytest.fail(overused)
    shape = (int(n) + 1,) + np.shape(x0)
    if not (isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape):
        pytest.fail(f"expected {what} as a numpy.ndarray of floats of shape {shape} (n_steps + 1 points, x0 included), "
                    f"got {type(got).__name__}" + (f" of dtype {got.dtype} and shape {got.shape}"
                                                   if isinstance(got, np.ndarray) else f" {got!r}")
                    + f" ({HINTS[method]})")
    if not np.array_equal(got[0], np.asarray(x0, dtype=float)):
        pytest.fail(f"expected the first point of {what} to be x0 = {_show(x0)}, got {_show(got[0])} "
                    f"({HINTS[method]})")
    return got, field


def _times(t0, t1, n):
    """t_k = t0 + k h, k = 0, …, n, h = (t1 - t0) / n."""
    h = (t1 - t0) / n
    return t0 + np.arange(n + 1) * h, h


def _ode_hint(method, got, candidates, want):
    text = _first_match(got, want, candidates, rtol=1e-9, atol=1e-11)
    return f"here {text}; {HINTS[method]}" if text else HINTS[method]


def _check_ode(method, got, want, what, candidates=(), rtol=1e-12, atol=None):
    scale = 1.0 + float(np.max(np.abs(want)))
    _close(got, want, what, rtol=rtol, atol=scale * 1e-12 if atol is None else atol,
           hint=lambda: _ode_hint(method, got, candidates, want))


def _time_only(g):
    """The field f(t, x) = g(t), of the shape of x (the velocity depends on the time only)."""
    return lambda t, x: np.full(np.shape(x), g(t))


def _random_g(rng):
    c = rng.uniform(-2.0, 2.0, size=4)
    w = float(rng.uniform(0.7, 2.6))
    return (lambda t: c[0] * np.cos(w * t) + c[1] * t * t + c[2] * np.sin(t / 2) + c[3]), (
        f"x' = {c[0]:.3f} cos({w:.3f} t) + {c[1]:.3f} t² + {c[2]:.3f} sin(t / 2) + {c[3]:.3f}")


def _random_rate(rng):
    c = rng.uniform(-1.5, 1.5, size=2)
    w = float(rng.uniform(0.5, 2.5))
    return (lambda t: c[0] + c[1] * np.sin(w * t)), f"x' = ({c[0]:.3f} + {c[1]:.3f} sin({w:.3f} t)) x"


def _linear(rate):
    """The field f(t, x) = λ(t) x, coordinate by coordinate."""
    return lambda t, x: rate(t) * np.asarray(x, dtype=float)


def _random_matrix(rng, d=2):
    """A matrix with no symmetry (neither a rotation nor a symmetric matrix)."""
    while True:
        A = np.round(rng.uniform(-1.8, 1.8, size=(d, d)), 2)
        if abs(A[0, 1] - A[1, 0]) > 0.3 and abs(A[0, 1] + A[1, 0]) > 0.3:
            return A


def _system(A):
    """The field f(t, x) = A x, or A X for several points in the columns of X."""
    return lambda t, x: A @ np.asarray(x, dtype=float)


def _constant_along_the_path(c, x0, t0, kappa):
    """A field whose velocity is c on the path x(t) = x0 + c (t - t0) and changes away from it:
    f(t, x) = c + κ (x - x0 - c (t - t0))."""
    c, x0 = np.asarray(c, dtype=float), np.asarray(x0, dtype=float)
    return lambda t, x: c + kappa * (np.asarray(x, dtype=float) - x0 - c * (t - t0))


def _scalar_field(t, x):
    x = np.asarray(x, dtype=float)
    return 0.85 * np.sin(1.7 * t) - 0.55 * x + 0.35 * x * x * np.cos(t)


def _system_field(t, x):
    x = np.asarray(x, dtype=float)
    return np.array([x[0] * (1.15 - 0.45 * x[1]) + 0.2 * np.sin(1.3 * t),
                     x[1] * (0.35 * x[0] - 0.85) + 0.1 * np.cos(t)])


def _solve_ivp(velocity, x0, t0, t1, times):
    """The exact path at the given times, by scipy.integrate.solve_ivp (DOP853, rtol = atol = 1e-13)."""
    shape = np.shape(x0)
    start = np.array(x0, dtype=float).ravel()

    def rhs(t, y):
        return np.asarray(velocity(t, y.reshape(shape) if shape else y[0]), dtype=float).ravel()

    times = np.clip(times, min(t0, t1), max(t0, t1))           # t0 + k h may pass t1 by a rounding
    solution = integrate.solve_ivp(rhs, (t0, t1), start, method="DOP853", rtol=1e-13, atol=1e-13, t_eval=times)
    assert solution.success, "expected solve_ivp to succeed (the oracle)"
    return solution.y.T.reshape((len(times),) + shape)


ORDER_CASES = [("scalar-forward", _scalar_field, "x' = 0.85 sin(1.7 t) - 0.55 x + 0.35 x² cos t", 0.37, 0.3, 2.9),
               ("scalar-backward", _scalar_field, "x' = 0.85 sin(1.7 t) - 0.55 x + 0.35 x² cos t", 1.13, 2.9, 0.3),
               ("system-forward", _system_field, "a forced predator-prey system", [1.7, 0.95], 0.2, 3.1),
               ("system-backward", _system_field, "a forced predator-prey system", [1.4, 1.6], 3.1, 0.2)]
STEP_COUNTS = (80, 160, 320, 640)


def _order_test(gp, method, case, order, low, high):
    """The errors at t1, and the largest error over the t_k, against solve_ivp for 80, 160, 320 and 640 steps: each
    doubling of the number of steps divides them by 2^order (within [low, high])."""
    _, velocity, name, x0, t0, t1 = case
    finals, largest = [], []
    for n in STEP_COUNTS:
        times = _times(t0, t1, n)[0]
        exact = _solve_ivp(velocity, x0, t0, t1, times)
        got, _ = _ode(gp, method, velocity, name, x0, t0, t1, n)
        if not np.all(np.isfinite(got)):
            pytest.fail(f"expected finite points for {_describe_ode(method, name, x0, t0, t1, n)}, got "
                        f"{_show(got)} ({HINTS[method]})")
        finals.append(float(np.max(np.abs(got[-1] - exact[-1]))))
        largest.append(float(np.max(np.abs(got - exact))))
    for errors, text in ((finals, "the error at t1"), (largest, "the largest error over the t_k")):
        ratios = [e / f if f > 0 else math.inf for e, f in zip(errors, errors[1:])]
        if not all(low <= r <= high for r in ratios):
            pytest.fail(f"expected {text} of {method}({name}, {x0!r}, {t0}, {t1}, n) divided by about {2 ** order} "
                        f"each time n doubles (n = {', '.join(map(str, STEP_COUNTS))}; an error of order "
                        f"h{'²' if order == 2 else ''}), got errors {[f'{e:.3e}' for e in errors]} (ratios "
                        f"{[round(r, 3) for r in ratios]}) against scipy.integrate.solve_ivp ({HINTS[method]})")


# --- euler_ode ------------------------------------------------------------------------------------------------------

DIRECTIONS = [(0.35, 2.85), (2.4, -0.65)]
DIRECTION_IDS = ["forward", "backward"]


@pytest.mark.parametrize("t0, t1", DIRECTIONS, ids=DIRECTION_IDS)
def test_euler_ode_with_a_velocity_of_time_only_is_the_left_riemann_sum(gp, t0, t1):
    """x' = g(t): Euler's points are x_k = x0 + h (g(t_0) + … + g(t_{k-1})), the sum of Riemann at the left (M02a),
    forward and backward in time, for one coordinate or several."""
    rng = _rng(7650, DIRECTIONS.index((t0, t1)))
    for n in (1, 4, 13, 50):
        g, name = _random_g(rng)
        x0 = float(np.round(rng.normal() * 2.0, 3)) if n % 2 else np.round(rng.normal(size=3) * 2.0, 3)
        times, h = _times(t0, t1, n)
        values = g(times)
        steps = h * np.concatenate([[0.0], np.cumsum(values[:-1])])
        want = np.asarray(x0)[None, ...] + steps.reshape((-1,) + (1,) * np.ndim(x0))
        got, _ = _ode(gp, "euler_ode", _time_only(g), name, x0, t0, t1, n)
        h_more = (t1 - t0) / (n + 1)
        candidates = [
            (np.asarray(x0) + (h * np.concatenate([[0.0], np.cumsum(values[1:])])).reshape(want.shape[:1] + (1,) *
                                                                                            np.ndim(x0)),
             "the velocity is read at the end of each step, t_{k+1}, not at its start t_k"),
            (np.asarray(x0) + (h * np.arange(n + 1) * values[0]).reshape(want.shape[:1] + (1,) * np.ndim(x0)),
             "the time does not move: f is always called at t0, not at t_k = t0 + k h"),
            (np.asarray(x0) + (h_more * np.concatenate([[0.0], np.cumsum(g(t0 + np.arange(n) * h_more))]))
             .reshape(want.shape[:1] + (1,) * np.ndim(x0)), "h = (t1 - t0) / n_steps, not / (n_steps + 1)")]
        _check_ode("euler_ode", got, want, _describe_ode("euler_ode", name, x0, t0, t1, n) + " (left Riemann sums)",
                   candidates)


@pytest.mark.parametrize("t0, t1", DIRECTIONS, ids=DIRECTION_IDS)
def test_euler_ode_with_a_linear_field_multiplies_by_1_plus_h_lambda_at_each_step(gp, t0, t1):
    """x' = λ(t) x with a rate that depends on time: x_{k+1} = (1 + h λ(t_k)) x_k, so that x_k is x0 times the
    cumulative product of these factors (np.cumprod), for one coordinate or several points at once."""
    rng = _rng(7651, DIRECTIONS.index((t0, t1)))
    for n in (1, 3, 8, 21, 60):
        rate, name = _random_rate(rng)
        x0 = np.round(rng.normal(size=(2, 3)) * 1.5, 3) if n % 3 == 0 else float(np.round(rng.normal() * 2.0, 3))
        times, h = _times(t0, t1, n)
        lam = rate(times)
        shape = (n + 1,) + (1,) * np.ndim(x0)

        def product(factors):
            return np.asarray(x0) * np.concatenate([[1.0], np.cumprod(factors)]).reshape(shape)

        want = product(1 + h * lam[:-1])
        got, _ = _ode(gp, "euler_ode", _linear(rate), name, x0, t0, t1, n)
        candidates = [(product(1 + h * lam[1:]), "the rate is read at the end of each step, t_{k+1}, not at t_k"),
                      (product(np.full(n, 1 + h * lam[0])), "the time does not move: f is always called at t0")]
        _check_ode("euler_ode", got, want, _describe_ode("euler_ode", name, x0, t0, t1, n), candidates)


def test_euler_ode_with_a_linear_system_is_a_matrix_power(gp):
    """x' = A x (A with no symmetry, for one point or three points in the columns of X): x_k = (I + h A)^k x0
    (np.linalg.matrix_power), forward and backward."""
    rng = _rng(7652)
    for k in range(6):
        A = _random_matrix(rng)
        t0, t1 = (0.15, 1.95) if k % 2 == 0 else (1.65, -0.4)
        n = int(rng.integers(1, 30))
        x0 = np.round(rng.normal(size=2) * 2.0, 3) if k < 3 else np.round(rng.normal(size=(2, 3)) * 2.0, 3)
        h = (t1 - t0) / n
        P = np.eye(2) + h * A
        want = np.array([np.linalg.matrix_power(P, j) @ x0 for j in range(n + 1)])
        name = f"x' = A x with A = {A.tolist()}"
        got, _ = _ode(gp, "euler_ode", _system(A), name, x0, t0, t1, n)
        _check_ode("euler_ode", got, want, _describe_ode("euler_ode", name, x0, t0, t1, n) + " ((I + h A)^k x0)")


def test_euler_ode_is_exact_when_the_velocity_stays_constant_along_the_path(gp):
    """f(t, x) = c + κ (x - x0 - c (t - t0)) is c on the path x0 + c (t - t0) and changes away from it: Euler's points
    stay on the path (up to rounding), whatever the number of steps, forward and backward; a constant field too."""
    rng = _rng(7653)
    for k in range(8):
        t0, t1 = (0.45, 3.2) if k % 2 == 0 else (2.7, -1.15)
        c = float(np.round(rng.uniform(-2.5, 2.5), 3)) if k < 4 else np.round(rng.uniform(-2.5, 2.5, size=3), 3)
        x0 = float(np.round(rng.normal(), 3)) if k < 4 else np.round(rng.normal(size=3), 3)
        kappa = float(rng.uniform(1.0, 4.0)) * float(rng.choice([-1, 1]))
        for n in (1, 2, 7, 40):
            times = np.linspace(t0, t1, n + 1)
            want = np.asarray(x0)[None, ...] + np.multiply.outer(times - t0, np.asarray(c))
            name = f"x' = c + κ (x - x0 - c (t - t0)) with c = {_show(c)} and κ = {kappa:.4g}"
            got, _ = _ode(gp, "euler_ode", _constant_along_the_path(c, x0, t0, kappa), name, x0, t0, t1, n)
            _check_ode("euler_ode", got, want, _describe_ode("euler_ode", name, x0, t0, t1, n) + " (the path "
                       "x0 + c (t - t0))", rtol=1e-12, atol=1e-12 * (1 + float(np.max(np.abs(want)))) * n)
    for x0, c in ((1.85, -0.65), (np.array([0.35, -2.4]), np.array([1.45, 0.55]))):
        name = f"x' = {_show(c)} (a constant velocity)"
        got, _ = _ode(gp, "euler_ode", lambda t, x, c=c: np.array(c, dtype=float), name, x0, -0.45, 2.35, 1)
        _check_ode("euler_ode", got, np.array([x0, x0 + 2.8 * c]), _describe_ode("euler_ode", name, x0, -0.45, 2.35,
                                                                                1) + " (one step is exact)")


@pytest.mark.parametrize("case", ORDER_CASES, ids=[c[0] for c in ORDER_CASES])
def test_euler_ode_error_is_of_order_h_against_solve_ivp(gp, case):
    """A regular field that depends on time (one coordinate, or a system of two), forward or backward: against
    scipy.integrate.solve_ivp at a tight tolerance, the error at t1 and the largest error over the t_k are divided by
    about 2 (between 1.9 and 2.1) when the number of steps doubles."""
    _order_test(gp, "euler_ode", case, 1, 1.9, 2.1)


def test_euler_ode_calls_f_once_per_step_at_t_k_and_x_k(gp):
    """Exactly n_steps evaluations of f; the k-th at the time t_k = t0 + k h (a number) and at the point x_k returned
    by the method (an array of the shape of x0), never at the last point."""
    rng = _rng(7655)
    for k in range(6):
        t0, t1 = (0.25, 2.05) if k % 2 == 0 else (1.7, -0.95)
        n = int(rng.integers(1, 12))
        A = _random_matrix(rng)
        x0 = np.round(rng.normal(size=2), 3) if k < 4 else float(np.round(rng.normal(), 3))
        velocity = _system(A) if k < 4 else _linear(lambda t: 0.75 - 1.25 * np.cos(t))
        name = "x' = A x" if k < 4 else "x' = (0.75 - 1.25 cos t) x"
        what = _describe_ode("euler_ode", name, x0, t0, t1, n)
        got, field = _ode(gp, "euler_ode", velocity, name, x0, t0, t1, n, record=True)
        if field.calls != n:
            pytest.fail(f"expected n_steps = {n} evaluations of f for {what} (one per step, at the start of each "
                        f"step), got {field.calls} ({EULER_HINT})")
        times, _ = _times(t0, t1, n)
        for j, (t, x) in enumerate(field.log):
            if isinstance(t, (bool, np.bool_)) or np.ndim(t) != 0 or not isinstance(t, (int, float, np.number)):
                pytest.fail(f"expected f to receive a time (a number) for {what}, got {t!r} ({EULER_HINT})")
            if not math.isclose(float(t), times[j], rel_tol=1e-12, abs_tol=1e-12):
                pytest.fail(f"expected evaluation {j} of f for {what} at the time t_{j} = {times[j]:.12g}, got "
                            f"{float(t):.12g} ({EULER_HINT})")
            if x.shape != np.shape(x0) or not _same(x, got[j], rtol=1e-14, atol=0):
                pytest.fail(f"expected evaluation {j} of f for {what} at the point x_{j} = {_show(got[j])} (shape "
                            f"{np.shape(x0)}), got {_show(x)} (shape {x.shape}) ({EULER_HINT})")


def test_euler_ode_with_t1_equal_to_t0_stays_at_x0(gp):
    """t1 = t0: h = 0, and every point is x0."""
    for x0 in (1.35, np.array([0.45, -2.15, 3.05])):
        for n in (1, 3):
            name = "x' = 1.6 - 0.7 x + t"
            got, _ = _ode(gp, "euler_ode", lambda t, x: 1.6 - 0.7 * np.asarray(x, dtype=float) + t, name, x0, 1.25,
                          1.25, n)
            _check_ode("euler_ode", got, np.array([x0] * (n + 1)), _describe_ode("euler_ode", name, x0, 1.25, 1.25, n)
                       + " (t1 = t0)", rtol=0, atol=0)


START_POINTS = [(0.85, "a float"), (3, "an int"), (np.float32(1.5), "a NumPy float32"), ([1.2, -0.4, 2.2], "a list"),
                ([2, -1], "a list of ints"), (np.array([[0.35, -1.45], [2.15, 0.65]]), "a 2-D array"),
                (np.arange(6.0).reshape(2, 1, 3) - 2.35, "a 3-D array")]


@pytest.mark.parametrize("x0, text", START_POINTS, ids=["float", "int", "float32", "list", "int-list", "2d", "3d"])
def test_euler_ode_returns_floats_of_shape_n_plus_1_then_the_shape_of_x0(gp, x0, text):
    """x0 of any shape (a number, a list, a 2-D or 3-D array of points moved at once by a vectorized f): the points
    form a float array of shape (n_steps + 1,) + shape of x0, whose entry 0 is x0; for x' = λ x,
    x_k = (1 + h λ)^k x0."""
    lam, t0, t1, n = -1.35, 0.4, 1.9, 6
    h = (t1 - t0) / n
    name = f"x' = {lam} x"
    got, _ = _ode(gp, "euler_ode", _linear(lambda t: lam), name, x0, t0, t1, n)
    want = np.multiply.outer((1 + h * lam) ** np.arange(n + 1), np.asarray(x0, dtype=float))
    _check_ode("euler_ode", got, want, _describe_ode("euler_ode", name, x0, t0, t1, n) + f" (x0 {text})")


def test_euler_ode_does_not_modify_x0_and_returns_a_new_array(gp_module):
    """x0 as float arrays that are not dyadic (x += h v on x0 itself would show), C or Fortran order, float32; the
    result never shares its memory with x0."""
    rng = _rng(7656)
    A = _random_matrix(rng)
    for x0 in (rng.normal(size=2) * 1.37, np.asfortranarray(rng.normal(size=(2, 3)) * 2.11),
               (rng.normal(size=2) * 0.93).astype(np.float32)):
        copy = x0.copy()
        what = _describe_ode("euler_ode", "x' = A x", x0, 0.3, 1.45, 5)
        got = _result(lambda: gp_module.euler_ode(_Field(_system(A), 50), x0, 0.3, 1.45, 5), "the points", what,
                      EULER_HINT)
        assert np.array_equal(x0, copy), (
            f"expected x0 unchanged by {what}, got {_show(x0)} (never modify the array you receive: x = "
            f"np.array(x0, dtype=float) is a copy, np.asarray(x0) is x0 itself)")
        assert not (isinstance(got, np.ndarray) and np.shares_memory(got, x0)), (
            f"expected a new array for {what}, got an array that shares its memory with x0 ({EULER_HINT})")


NUMPY_ARGS = [(np.int64(6), 1, 4, "n_steps an int64, times ints"), (np.int32(5), np.float32(1.25), np.float32(3.75),
                                                                     "n_steps an int32, float32 times"),
              (np.uint8(4), np.int64(-2), np.float64(0.35), "n_steps a uint8, an int64 and a float64"),
              (np.int16(3), 2.5, -1, "n_steps an int16, backward to an int")]


@pytest.mark.parametrize("n, t0, t1, text", NUMPY_ARGS, ids=["int64", "int32", "uint8", "int16"])
def test_euler_ode_accepts_numpy_integers_and_times_of_any_real_type(gp, n, t0, t1, text):
    """A NumPy integer number of steps, times given as ints, NumPy integers or NumPy floats."""
    rate, _ = _random_rate(_rng(7657, NUMPY_ARGS.index((n, t0, t1, text))))
    x0 = 1.65
    name = "x' = λ(t) x"
    got, _ = _ode(gp, "euler_ode", _linear(rate), name, x0, t0, t1, n)
    times, h = _times(float(t0), float(t1), int(n))
    want = x0 * np.concatenate([[1.0], np.cumprod(1 + h * rate(times[:-1]))])
    _check_ode("euler_ode", got, want, _describe_ode("euler_ode", name, x0, t0, t1, n) + f" ({text})", rtol=1e-7,
               atol=1e-9)


def test_euler_ode_of_many_steps_is_fast(gp):
    """100 000 steps of x' = λ x take a fraction of a second: x_k = (1 + h λ)^k x0."""
    lam, t0, t1, n, x0 = -0.85, 0.0, 3.4, 100_000, 2.45
    h = (t1 - t0) / n
    name = f"x' = {lam} x"
    got, field = _ode(gp, "euler_ode", _linear(lambda t: lam), name, x0, t0, t1, n, seconds=60)
    _check_ode("euler_ode", got, x0 * (1 + h * lam) ** np.arange(n + 1),
               _describe_ode("euler_ode", name, x0, t0, t1, n), rtol=1e-9, atol=1e-12)


def _bad_at_even_calls():
    """A field for x0 = [0.4, -1.1, 2.3] whose velocity has the shape of the point it receives at the calls 1, 3, 5…
    and the shape (1, 3) at the calls 2, 4, 6… (for the midpoint method, the second evaluation of each step): a
    velocity of another shape is refused at any evaluation."""
    calls = []

    def velocity(t, x):
        calls.append(t)
        v = -0.35 * np.asarray(x, dtype=float)
        return v if len(calls) % 2 else v.reshape(1, -1)

    return velocity


BAD_VELOCITIES = [([0.4, -1.1, 2.3], lambda t, x: 1.7, "a number for x0 of shape (3,)"),
                  ([0.4, -1.1, 2.3], lambda t, x: np.ones(1), "shape (1,) for x0 of shape (3,)"),
                  ([0.4, -1.1, 2.3], lambda t, x: np.ones((3, 1)), "shape (3, 1) for x0 of shape (3,)"),
                  ([0.4, -1.1, 2.3], lambda t, x: np.ones(4), "shape (4,) for x0 of shape (3,)"),
                  (0.65, lambda t, x: np.ones(2), "shape (2,) for a number x0"),
                  (0.65, lambda t, x: np.ones(1), "shape (1,) for a number x0"),
                  (np.ones((2, 2)) * 0.35, lambda t, x: np.ones(2), "shape (2,) for x0 of shape (2, 2)"),
                  (np.ones((2, 2)) * 0.35, lambda t, x: np.ones(4), "shape (4,) for x0 of shape (2, 2)"),
                  ([0.4, -1.1, 2.3], _bad_at_even_calls, "the shape of x0 at the calls 1, 3, 5… and the shape "
                                                         "(1, 3) at the calls 2, 4, 6…")]
BAD_VELOCITY_IDS = ["number", "one", "column", "longer", "vector-for-number", "one-for-number", "row-for-matrix",
                    "flat-for-matrix", "at-even-calls"]


def _velocity_of(velocity):
    """The velocity of a case of BAD_VELOCITIES (a new field for the one that counts its calls)."""
    return velocity() if velocity is _bad_at_even_calls else velocity


@pytest.mark.parametrize("x0, velocity, why", BAD_VELOCITIES, ids=BAD_VELOCITY_IDS)
def test_euler_ode_refuses_a_velocity_of_another_shape(gp, x0, velocity, why):
    """A velocity whose shape is not that of x0 is refused, at any evaluation, even when NumPy could broadcast it."""
    field = _Field(_velocity_of(velocity), 50)
    _expect_error(ValueError, lambda: gp.euler_ode(field, x0, 0.0, 1.35, 3),
                  f"euler_ode(f, {x0!r}, 0.0, 1.35, 3) with f returning a velocity of {why}",
                  "the velocity must have the shape of x0")


BAD_ODE = [({"n_steps": 0}, "n_steps = 0"), ({"n_steps": -2}, "n_steps is negative"),
           ({"n_steps": 3.0}, "n_steps is the float 3.0"), ({"n_steps": np.float64(4.0)}, "n_steps is np.float64(4.0)"),
           ({"n_steps": 2.5}, "n_steps is 2.5"), ({"n_steps": True}, "n_steps is True, a bool"),
           ({"n_steps": np.True_}, "n_steps is np.True_, a NumPy bool"), ({"n_steps": "5"}, "n_steps is a string"),
           ({"n_steps": None}, "n_steps is None"), ({"t0": np.nan}, "t0 is nan"), ({"t0": np.inf}, "t0 is inf"),
           ({"t0": None}, "t0 is None"), ({"t0": "start"}, "t0 is a string"), ({"t1": -np.inf}, "t1 is -inf"),
           ({"t1": np.nan}, "t1 is nan"), ({"t1": None}, "t1 is None"), ({"t1": 1j}, "t1 is complex")]
BAD_ODE_IDS = ["n0", "n-negative", "n-float", "n-numpy-float", "n-half", "n-bool", "n-numpy-bool", "n-string", "n-none",
               "t0-nan", "t0-inf", "t0-none", "t0-string", "t1-minus-inf", "t1-nan", "t1-none", "t1-complex"]


def _bad_ode_call(gp, method, change):
    args = {"x0": np.array([0.55, -1.35]), "t0": 0.2, "t1": 1.65, "n_steps": 4, **change}
    field = _Field(lambda t, x: -0.45 * np.asarray(x, dtype=float), 50)
    shown = ", ".join(f"{k}={v!r}" for k, v in args.items())
    return (lambda: getattr(gp, method)(field, args["x0"], args["t0"], args["t1"], args["n_steps"]),
            f"{method}(f, {shown})")


@pytest.mark.parametrize("change, why", BAD_ODE, ids=BAD_ODE_IDS)
def test_euler_ode_refusals(gp, change, why):
    call, what = _bad_ode_call(gp, "euler_ode", change)
    _expect_error(ValueError, call, what, why)


# --- midpoint_ode ---------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("t0, t1", DIRECTIONS, ids=DIRECTION_IDS)
def test_midpoint_ode_with_a_velocity_of_time_only_is_the_midpoint_rule(gp, t0, t1):
    """x' = g(t): the midpoint method gives x_k = x0 + h (g(t_0 + h/2) + … + g(t_{k-1} + h/2)), the midpoint rule of
    M02a, forward and backward in time, for one coordinate or several."""
    rng = _rng(7670, DIRECTIONS.index((t0, t1)))
    for n in (1, 4, 13, 50):
        g, name = _random_g(rng)
        x0 = float(np.round(rng.normal() * 2.0, 3)) if n % 2 else np.round(rng.normal(size=3) * 2.0, 3)
        times, h = _times(t0, t1, n)
        shape = (n + 1,) + (1,) * np.ndim(x0)

        def total(values):
            return np.asarray(x0) + (h * np.concatenate([[0.0], np.cumsum(values)])).reshape(shape)

        start, middle, end = g(times[:-1]), g(times[:-1] + h / 2), g(times[1:])
        want = total(middle)
        got, _ = _ode(gp, "midpoint_ode", _time_only(g), name, x0, t0, t1, n)
        candidates = [(total(start), "this is Euler's method (the velocity read at the start of the step): the "
                                     "midpoint method reads it at the middle, t_k + h / 2"),
                      (total((start + end) / 2), "this is the average of the velocities at t_k and t_k + h (the "
                                                 "method of Heun), not the velocity read at the middle"),
                      (total(end), "the velocity is read at the end of the step, not at its middle"),
                      (total((start + middle) / 2), "the update is (h / 2) (k1 + k2) (two half Euler steps, or the "
                                                    "average of k1 and k2): it is h k2, the velocity read at the "
                                                    "middle used for the whole step"),
                      (total(middle / 2), "the update is x_k + (h / 2) k2: the velocity read at the middle is used "
                                          "for the whole step, x_k + h k2"),
                      (total(np.full(n, g(t0 + h / 2))), "the time does not move: the steps all use t0")]
        _check_ode("midpoint_ode", got, want, _describe_ode("midpoint_ode", name, x0, t0, t1, n) + " (the midpoint "
                   "rule)", candidates)


@pytest.mark.parametrize("t0, t1", DIRECTIONS, ids=DIRECTION_IDS)
def test_midpoint_ode_is_exact_for_a_velocity_affine_in_t(gp, t0, t1):
    """x' = c + d t: the midpoint method gives the exact x0 + c (t - t0) + d (t² - t0²) / 2 at every t_k (up to
    rounding), whatever the number of steps, one step included."""
    rng = _rng(7671, DIRECTIONS.index((t0, t1)))
    for k in range(6):
        c, d = (float(np.round(v, 3)) for v in rng.uniform(-3.0, 3.0, size=2))
        x0 = float(np.round(rng.normal(), 3)) if k % 2 else np.round(rng.normal(size=2), 3)
        for n in (1, 3, 11):
            times = np.linspace(t0, t1, n + 1)
            want = np.asarray(x0)[None, ...] + (c * (times - t0) + d * (times ** 2 - t0 ** 2) / 2).reshape(
                (-1,) + (1,) * np.ndim(x0))
            name = f"x' = {c} + {d} t"
            got, _ = _ode(gp, "midpoint_ode", _time_only(lambda t, c=c, d=d: c + d * t), name,
                          x0, t0, t1, n)
            _check_ode("midpoint_ode", got, want, _describe_ode("midpoint_ode", name, x0, t0, t1, n) + " (the exact "
                       "solution)", rtol=1e-12, atol=1e-12 * (1 + float(np.max(np.abs(want)))) * n)


@pytest.mark.parametrize("t0, t1", DIRECTIONS, ids=DIRECTION_IDS)
def test_midpoint_ode_with_a_linear_field_multiplies_by_the_factor_of_one_step(gp, t0, t1):
    """x' = λ(t) x with a rate that depends on time: one step multiplies x_k by 1 + h λ(t_k + h/2) (1 + (h/2) λ(t_k)),
    so that x_k is x0 times the cumulative product of these factors (np.cumprod)."""
    rng = _rng(7672, DIRECTIONS.index((t0, t1)))
    for n in (1, 3, 8, 21, 60):
        rate, name = _random_rate(rng)
        x0 = np.round(rng.normal(size=(2, 3)) * 1.5, 3) if n % 3 == 0 else float(np.round(rng.normal() * 2.0, 3))
        times, h = _times(t0, t1, n)
        start, middle, end = rate(times[:-1]), rate(times[:-1] + h / 2), rate(times[1:])
        shape = (n + 1,) + (1,) * np.ndim(x0)

        def product(factors):
            return np.asarray(x0) * np.concatenate([[1.0], np.cumprod(factors)]).reshape(shape)

        want = product(1 + h * middle * (1 + h / 2 * start))
        got, _ = _ode(gp, "midpoint_ode", _linear(rate), name, x0, t0, t1, n)
        candidates = [
            (product(1 + h * start), "this is Euler's method (the velocity read at the start of the step): the "
                                     "midpoint method reads it at the middle"),
            (product(1 + h / 2 * (start + end * (1 + h * start))), "this is the method of Heun (the average of two "
                                                                    "velocities), not the velocity at the middle"),
            (product(1 + h * middle * (1 + h * start)), "the point at the middle is x_k + (h / 2) k1, half an Euler "
                                                        "step, not a whole one"),
            (product(1 + h * middle), "the velocity at the middle is read at x_k + (h / 2) k1, not at x_k"),
            (product(1 + h / 2 * middle * (1 + h / 2 * start)), "the update is x_k + (h / 2) k2: the velocity read "
                                                                "at the middle is used for the whole step"),
            (product(1 + h / 2 * (start + middle * (1 + h / 2 * start))), "the update is (h / 2) (k1 + k2) (two half "
                                                                          "Euler steps, or the average of k1 and "
                                                                          "k2): it is h k2"),
            (product(1 + h * end * (1 + h / 2 * start)), "the second velocity is read at t_k + h / 2, not at "
                                                         "t_k + h"),
            (product(np.full(n, 1 + h * rate(t0 + h / 2) * (1 + h / 2 * rate(t0)))),
             "the time does not move: the steps all use t0")]
        _check_ode("midpoint_ode", got, want, _describe_ode("midpoint_ode", name, x0, t0, t1, n), candidates)


def test_midpoint_ode_with_a_linear_system_is_a_matrix_power(gp):
    """x' = A x: one step multiplies by I + h A + (h A)² / 2, so x_k = (I + h A + (h A)² / 2)^k x0
    (np.linalg.matrix_power), for one point or three points in the columns of X, forward and backward."""
    rng = _rng(7673)
    for k in range(6):
        A = _random_matrix(rng)
        t0, t1 = (0.15, 1.95) if k % 2 == 0 else (1.65, -0.4)
        n = int(rng.integers(1, 30))
        x0 = np.round(rng.normal(size=2) * 2.0, 3) if k < 3 else np.round(rng.normal(size=(2, 3)) * 2.0, 3)
        h = (t1 - t0) / n
        P = np.eye(2) + h * A + (h * A) @ (h * A) / 2
        want = np.array([np.linalg.matrix_power(P, j) @ x0 for j in range(n + 1)])
        name = f"x' = A x with A = {A.tolist()}"
        got, _ = _ode(gp, "midpoint_ode", _system(A), name, x0, t0, t1, n)
        candidates = [(np.array([np.linalg.matrix_power(np.eye(2) + h * A, j) @ x0 for j in range(n + 1)]),
                       "this is Euler's method: (I + h A)^k x0"),
                      (np.array([np.linalg.matrix_power(np.eye(2) + h * A + (h * A) @ (h * A), j) @ x0
                                 for j in range(n + 1)]),
                       "the point at the middle is x_k + (h / 2) k1, half an Euler step, not a whole one")]
        _check_ode("midpoint_ode", got, want, _describe_ode("midpoint_ode", name, x0, t0, t1, n)
                   + " ((I + h A + (h A)² / 2)^k x0)", candidates)


@pytest.mark.parametrize("case", ORDER_CASES, ids=[c[0] for c in ORDER_CASES])
def test_midpoint_ode_error_is_of_order_h_squared_against_solve_ivp(gp, case):
    """A regular field that depends on time (one coordinate, or a system of two), forward or backward: against
    scipy.integrate.solve_ivp at a tight tolerance, the error at t1 and the largest error over the t_k are divided by
    about 4 (between 3.85 and 4.15) when the number of steps doubles."""
    _order_test(gp, "midpoint_ode", case, 2, 3.85, 4.15)


def test_midpoint_ode_calls_f_twice_per_step_at_the_start_then_at_the_middle(gp):
    """Exactly 2 n_steps evaluations of f; for step k, first at (t_k, x_k), then at
    (t_k + h/2, x_k + (h/2) f(t_k, x_k)), the times being numbers and the points arrays of the shape of x0."""
    rng = _rng(7675)
    for k in range(6):
        t0, t1 = (0.25, 2.05) if k % 2 == 0 else (1.7, -0.95)
        n = int(rng.integers(1, 12))
        A = _random_matrix(rng)
        x0 = np.round(rng.normal(size=2), 3) if k < 4 else float(np.round(rng.normal(), 3))
        velocity = _system(A) if k < 4 else _linear(lambda t: 0.75 - 1.25 * np.cos(t))
        name = "x' = A x" if k < 4 else "x' = (0.75 - 1.25 cos t) x"
        what = _describe_ode("midpoint_ode", name, x0, t0, t1, n)
        got, field = _ode(gp, "midpoint_ode", velocity, name, x0, t0, t1, n, record=True)
        if field.calls != 2 * n:
            pytest.fail(f"expected 2 n_steps = {2 * n} evaluations of f for {what} (two per step), got {field.calls} "
                        f"({MIDPOINT_HINT})")
        times, h = _times(t0, t1, n)
        for j, (t, x) in enumerate(field.log):
            step, second = divmod(j, 2)
            want_t = times[step] + (h / 2 if second else 0.0)
            want_x = got[step] + (h / 2) * np.asarray(velocity(times[step], got[step]), dtype=float) if second \
                else got[step]
            where = f"(t_{step} + h/2, x_{step} + (h/2) f(t_{step}, x_{step}))" if second else f"(t_{step}, x_{step})"
            if isinstance(t, (bool, np.bool_)) or np.ndim(t) != 0 or not isinstance(t, (int, float, np.number)):
                pytest.fail(f"expected f to receive a time (a number) for {what}, got {t!r} ({MIDPOINT_HINT})")
            if not math.isclose(float(t), want_t, rel_tol=1e-12, abs_tol=1e-12):
                pytest.fail(f"expected evaluation {j} of f for {what} at {where}, time {want_t:.12g}, got the time "
                            f"{float(t):.12g} ({MIDPOINT_HINT})")
            if x.shape != np.shape(x0) or not _same(x, want_x, rtol=1e-12, atol=1e-13):
                pytest.fail(f"expected evaluation {j} of f for {what} at {where}, point {_show(want_x)} (shape "
                            f"{np.shape(x0)}), got {_show(x)} (shape {x.shape}) ({MIDPOINT_HINT})")


def test_midpoint_ode_with_t1_equal_to_t0_stays_at_x0(gp):
    """t1 = t0: h = 0, and every point is x0."""
    for x0 in (1.35, np.array([0.45, -2.15, 3.05])):
        for n in (1, 3):
            name = "x' = 1.6 - 0.7 x + t"
            got, _ = _ode(gp, "midpoint_ode", lambda t, x: 1.6 - 0.7 * np.asarray(x, dtype=float) + t, name, x0,
                          1.25, 1.25, n)
            _check_ode("midpoint_ode", got, np.array([x0] * (n + 1)), _describe_ode("midpoint_ode", name, x0, 1.25,
                                                                                    1.25, n) + " (t1 = t0)",
                       rtol=0, atol=0)


@pytest.mark.parametrize("x0, text", START_POINTS, ids=["float", "int", "float32", "list", "int-list", "2d", "3d"])
def test_midpoint_ode_returns_floats_of_shape_n_plus_1_then_the_shape_of_x0(gp, x0, text):
    """x0 of any shape: the points form a float array of shape (n_steps + 1,) + shape of x0, whose entry 0 is x0; for
    x' = λ x, x_k = (1 + h λ + (h λ)² / 2)^k x0."""
    lam, t0, t1, n = -1.35, 0.4, 1.9, 6
    h = (t1 - t0) / n
    name = f"x' = {lam} x"
    got, _ = _ode(gp, "midpoint_ode", _linear(lambda t: lam), name, x0, t0, t1, n)
    want = np.multiply.outer((1 + h * lam + (h * lam) ** 2 / 2) ** np.arange(n + 1), np.asarray(x0, dtype=float))
    _check_ode("midpoint_ode", got, want, _describe_ode("midpoint_ode", name, x0, t0, t1, n) + f" (x0 {text})")


def test_midpoint_ode_does_not_modify_x0_and_returns_a_new_array(gp_module):
    """x0 as float arrays that are not dyadic (x += h k2 on x0 itself would show), C or Fortran order, float32; the
    result never shares its memory with x0."""
    rng = _rng(7676)
    A = _random_matrix(rng)
    for x0 in (rng.normal(size=2) * 1.37, np.asfortranarray(rng.normal(size=(2, 3)) * 2.11),
               (rng.normal(size=2) * 0.93).astype(np.float32)):
        copy = x0.copy()
        what = _describe_ode("midpoint_ode", "x' = A x", x0, 0.3, 1.45, 5)
        got = _result(lambda: gp_module.midpoint_ode(_Field(_system(A), 50), x0, 0.3, 1.45, 5), "the points", what,
                      MIDPOINT_HINT)
        assert np.array_equal(x0, copy), (
            f"expected x0 unchanged by {what}, got {_show(x0)} (never modify the array you receive: x = "
            f"np.array(x0, dtype=float) is a copy, np.asarray(x0) is x0 itself)")
        assert not (isinstance(got, np.ndarray) and np.shares_memory(got, x0)), (
            f"expected a new array for {what}, got an array that shares its memory with x0 ({MIDPOINT_HINT})")


@pytest.mark.parametrize("n, t0, t1, text", NUMPY_ARGS, ids=["int64", "int32", "uint8", "int16"])
def test_midpoint_ode_accepts_numpy_integers_and_times_of_any_real_type(gp, n, t0, t1, text):
    """A NumPy integer number of steps, times given as ints, NumPy integers or NumPy floats."""
    rate, _ = _random_rate(_rng(7677, NUMPY_ARGS.index((n, t0, t1, text))))
    x0 = 1.65
    name = "x' = λ(t) x"
    got, _ = _ode(gp, "midpoint_ode", _linear(rate), name, x0, t0, t1, n)
    times, h = _times(float(t0), float(t1), int(n))
    factors = 1 + h * rate(times[:-1] + h / 2) * (1 + h / 2 * rate(times[:-1]))
    want = x0 * np.concatenate([[1.0], np.cumprod(factors)])
    _check_ode("midpoint_ode", got, want, _describe_ode("midpoint_ode", name, x0, t0, t1, n) + f" ({text})",
               rtol=1e-7, atol=1e-9)


def test_midpoint_ode_of_many_steps_is_fast(gp):
    """50 000 steps of x' = λ x (100 000 evaluations) take a fraction of a second: x_k = (1 + h λ + (h λ)² / 2)^k x0."""
    lam, t0, t1, n, x0 = -0.85, 0.0, 3.4, 50_000, 2.45
    h = (t1 - t0) / n
    name = f"x' = {lam} x"
    got, _ = _ode(gp, "midpoint_ode", _linear(lambda t: lam), name, x0, t0, t1, n, seconds=60)
    _check_ode("midpoint_ode", got, x0 * (1 + h * lam + (h * lam) ** 2 / 2) ** np.arange(n + 1),
               _describe_ode("midpoint_ode", name, x0, t0, t1, n), rtol=1e-9, atol=1e-12)


@pytest.mark.parametrize("x0, velocity, why", BAD_VELOCITIES, ids=BAD_VELOCITY_IDS)
def test_midpoint_ode_refuses_a_velocity_of_another_shape(gp, x0, velocity, why):
    """A velocity whose shape is not that of x0 is refused, at any evaluation (the second one of a step included), even
    when NumPy could broadcast it."""
    field = _Field(_velocity_of(velocity), 50)
    _expect_error(ValueError, lambda: gp.midpoint_ode(field, x0, 0.0, 1.35, 3),
                  f"midpoint_ode(f, {x0!r}, 0.0, 1.35, 3) with f returning a velocity of {why}",
                  "the velocity must have the shape of x0")


@pytest.mark.parametrize("change, why", BAD_ODE, ids=BAD_ODE_IDS)
def test_midpoint_ode_refusals(gp, change, why):
    call, what = _bad_ode_call(gp, "midpoint_ode", change)
    _expect_error(ValueError, call, what, why)
