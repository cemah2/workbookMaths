"""Tests of mymath.policy_gradient (chapter MB8): the score-function estimate of a derivative with its standard error,
the values of a tabular softmax policy and their exact gradient in its logits, importance weights computed from
logarithms with their effective sample size, and the strengths of a Bradley-Terry model fitted to a tournament.

Oracles: for the score-function estimate, exact sums in ``fractions`` from the floats received (the mean of the terms
(f(x_i) - b_i) s_i and their variance with n - 1), and the absence of bias checked on discrete laws by enumerating
every sample of n draws (the mean of the estimates, weighted by the probability of each sample, is the exact
derivative d/dθ E_θ[f(X)], or (n - 1)/n of it for a baseline computed from the whole sample); for the gradient of the
values, the values computed by ``np.linalg.solve`` on (I - γ P_π) V = r_π (π by ``scipy.special.softmax``) and their
centred finite differences in each logit (two steps combined by Richardson's extrapolation); for the importance
weights, NumPy, ``scipy.special.logsumexp`` (the weights divided by their sum, and the effective sample size
(Σ w)² / Σ w² = exp(2 LSE(ln w) - LSE(2 ln w))), exact sums on a discrete law, and the invariance by a common
factor; for the strengths, ``scipy.optimize.minimize`` on the log-likelihood with Σ β = 0,
``sklearn.linear_model.LogisticRegression(fit_intercept=False, penalty=None)`` on the differences of indicators
e_i - e_j, the likelihood equations (observed wins = expected wins), and ``scipy.sparse.csgraph`` for the strong
connectivity of the graph of wins. Never another function of yours.
Plus properties: for the estimate, a constant baseline or the leave-one-out baseline that leave the expectation
unchanged, a common shift of f and of the baseline, 1-D and 2-D scores, d = 1, two draws, a discontinuous f, large
samples; for the gradient, a zero sum over the actions of each state, a common shift of the logits of a state, logits
of the order of a thousand, a state where the policy is deterministic in floats, substochastic transitions, γ = 1
when the process ends for sure (and its refusal when it never ends), γ = 0, one action, one state, rewards shifted by
a constant; for the weights, -inf in log_target (a weight 0), every weight 0, weights beyond the largest float (inf)
or below the smallest (0) with an exact effective sample size, truncation before normalization, np.inf, one draw, the
bounds 1 and n of the effective sample size; for the strengths, two players (a closed form), players relabelled, every
count multiplied by the same factor, half-points, a cycle that is strongly connected only through its longest path, an
unbeaten player, a player who never won, a group that never beat the others, two groups that never met, the
RuntimeError after max_iter sweeps, and a version that never stops (it fails quickly instead of blocking the tests).
Exact types and shapes (numbers as Python floats), inputs left unchanged (floats that are not dyadic), lists, NumPy
numbers, and every refusal of the docstrings. The data follow the rules of the chapter (checked before each call).
They describe the expected behaviour without showing the solution.

    pytest tests/test_mb8_policy_gradient.py              # your code
    pytest tests/test_mb8_policy_gradient.py --impl=ref   # the reference
"""

import ast
import inspect
import itertools
import math
import numbers
import re
import threading
import warnings
from fractions import Fraction

import numpy as np
import pytest
from scipy import optimize, special
from scipy.sparse.csgraph import connected_components
from sklearn.linear_model import LogisticRegression


@pytest.fixture
def pg_module(mymath_module):
    """The module itself: for the tests that check that your functions never write into the arrays they receive, and
    for the check of what the module uses."""
    return mymath_module("policy_gradient")


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
def pg(pg_module):
    return _OnCopies(pg_module)


def _text(hint):
    """A hint given as a text or as a function that computes it (only when a test fails)."""
    if not callable(hint):
        return hint
    try:
        return hint()
    except Exception:  # noqa: BLE001 - a hint must never hide the failure it explains
        return ""


def _result(call, expected, what="", hint="", allow_overflow=False):
    """call(), any error other than NotImplementedError (and any RuntimeWarning: a division by 0, an overflow, an
    invalid value…) being reported with what was expected first. allow_overflow lets e^x overflow to inf, which the
    docstring allows for the weights that are not normalized."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)
        if allow_overflow:
            warnings.filterwarnings("ignore", message="overflow encountered", category=RuntimeWarning)
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


_TOO_SLOW = {}      # function name -> its first call that gave no result in time: its later calls fail at once


def _within(seconds, call, what, expected, hint="", allow_overflow=False):
    """_result(call, …) in a thread that is given `seconds` to answer: a result that never comes fails the test
    instead of blocking it (the thread is left to finish on its own, and every later call of the same function fails
    at once, so that the tests end quickly)."""
    name = re.match(r"\w*", what).group(0)
    if name in _TOO_SLOW:
        pytest.fail(f"expected {expected} for {what} in little time, but an earlier call, {_TOO_SLOW[name]}, gave no "
                    f"result after {seconds} s ({_text(hint)})")
    box = {}

    def target():
        try:
            box["value"] = _result(call, expected, what, hint, allow_overflow)
        except BaseException as exc:  # noqa: BLE001 - re-raised in the test (⏳, or the failure of _result)
            box["error"] = exc

    thread = threading.Thread(target=target, daemon=True)
    thread.start()
    thread.join(seconds)
    if thread.is_alive():
        _TOO_SLOW[name] = what
        pytest.fail(f"expected {expected} for {what} in less than {seconds} s, got no result after {seconds} s "
                    f"({_text(hint)})")
    if "error" in box:
        raise box["error"]
    return box["value"]


def _expect_error(error, call, what, why, seconds=10):
    """Fail with what was expected first, whatever the code did instead of raising `error` itself (within `seconds`:
    a version that loops forever fails instead of blocking the tests)."""
    box = {}

    def target():
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            try:
                box["value"] = call()
            except BaseException as exc:  # noqa: BLE001 - sorted out below
                box["error"] = exc

    thread = threading.Thread(target=target, daemon=True)
    thread.start()
    thread.join(seconds)
    if thread.is_alive():
        _TOO_SLOW.setdefault(re.match(r"\w*", what).group(0), what)
        pytest.fail(f"expected {what} to raise {error.__name__} ({why}), got no answer after {seconds} s")
    exc = box.get("error")
    if isinstance(exc, NotImplementedError):
        raise exc                 # a function not written yet stays ⏳
    if isinstance(exc, error):
        return exc
    if exc is not None:
        pytest.fail(f"expected {what} to raise {error.__name__} ({why}), got {type(exc).__name__}: {exc}")
    pytest.fail(f"expected {what} to raise {error.__name__} ({why}), but it returned {_show_any(box.get('value'))}")


def _show(v):
    """A short text for an array: more than 12 numbers show the first 12 (flattened), then « … »."""
    try:
        arr = np.asarray(v, dtype=float)
    except (TypeError, ValueError):
        return repr(v)
    if arr.size > 12:
        return np.array2string(arr.ravel()[:12], precision=6, suppress_small=True,
                               max_line_width=10_000).replace("]", " …]") + f" (shape {arr.shape})"
    return np.array2string(arr, precision=6, suppress_small=True, max_line_width=10_000).replace("\n", "")


def _show_any(v):
    """_show for something that may not be an array of numbers (a tuple, a string, None…)."""
    if isinstance(v, tuple):
        return "(" + ", ".join(_show_any(x) for x in v) + ")"
    if isinstance(v, (str, type(None))):
        return repr(v)
    try:
        return _show(v) + (f" (dtype {v.dtype}, shape {v.shape})" if isinstance(v, np.ndarray) else
                           f" ({type(v).__module__}.{type(v).__name__})")
    except (TypeError, ValueError):
        return repr(v)


def _num(x):
    return repr(float(x)) if isinstance(x, (float, np.floating)) else repr(x)


def _matches(g, w, rtol, atol):
    """Entry by entry: equal infinities, or finite values within rtol and atol."""
    with np.errstate(invalid="ignore"):
        same_inf = np.isinf(g) & np.isinf(w) & (np.sign(g) == np.sign(w))
        close = np.isfinite(g) & np.isfinite(w) & (np.abs(g - w) <= atol + rtol * np.abs(w))
    return same_inf | close


def _same(got, value, rtol=1e-12, atol=1e-14):
    """Whether got equals value: same shape, entries close (an inf only where value has the same inf); nan never
    equals anything."""
    try:
        g = np.asarray(got, dtype=float)
        v = np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        return False
    if g.shape != v.shape:
        return False
    return bool(np.all(_matches(g, v, rtol, atol)))


def _place(k, where):
    if where is not None:
        return where(k if len(k) != 1 else k[0])
    return "the single entry" if not k else k[0] if len(k) == 1 else k


def _gap(got, want, rtol=1e-12, atol=1e-14, where=None):
    """Why got differs from want, case by case: how many entries differ, the largest gap, where it is (``where(k)``
    names entry k: an index, or a tuple of indices), and the two values there."""
    try:
        g = np.asarray(got, dtype=float)
        w = np.asarray(want, dtype=float)
    except (TypeError, ValueError):
        return ""
    if g.shape != w.shape:
        return f" (shape {g.shape} instead of {w.shape})"
    if not g.size:
        return ""
    wrong = ~_matches(g, w, rtol, atol)
    count = f"{int(wrong.sum())} of the {g.size} entries differ; " if g.size > 1 else ""
    odd = wrong & ~np.isfinite(g)
    if np.any(odd):
        k = tuple(int(i) for i in np.argwhere(odd)[0]) if g.ndim else ()
        return f" ({count}the result holds nan or inf, first at {_place(k, where)}, where {float(w[k]):.10g} was " \
               f"expected)"
    with np.errstate(invalid="ignore"):
        d = np.where(wrong, np.abs(np.nan_to_num(g - w, nan=np.inf, posinf=np.inf, neginf=np.inf)), -1.0)
    k = np.unravel_index(int(np.argmax(d)), d.shape)
    k = tuple(int(i) for i in k)
    return (f" ({count}largest gap {float(abs(g[k] - w[k])):.1e}, at {_place(k, where)}: expected {float(w[k]):.10g}, "
            f"got {float(g[k]):.10g})")


def _close(got, want, what, rtol=1e-12, atol=1e-14, hint="", where=None):
    if _same(got, want, rtol, atol):
        return
    hint = _text(hint)
    pytest.fail(f"expected {what} = {_show(want)}, got {_show_any(got)}{_gap(got, want, rtol, atol, where)}"
                + (f" ({hint})" if hint else ""))


def _first_match(got, want, variants, rtol=1e-9, atol=1e-11):
    """The texts of the classic errors whose value got matches (and that differ from the right value), joined by
    « or » when several errors give the same value here; "" when none does. A variant without a text is a value
    that the hint does not explain."""
    texts = [text for value, text in variants
             if text and value is not None and not _same(value, want, rtol, atol) and _same(got, value, rtol, atol)]
    return " — or ".join(dict.fromkeys(texts))


def _here(text, hint):
    return ("here " + text + "; " if text else "") + hint


def _rng(seed, case=None):
    """The generator of a test (seeds 8000 to 8090), one stream per case of a parametrized test."""
    return np.random.default_rng(seed if case is None else (seed, case))


def _python_float(got, what, hint):
    if type(got) is not float:
        pytest.fail(f"expected {what} as a Python float (float(...)), got {type(got).__module__}.{type(got).__name__} "
                    f"{_show_any(got)} ({hint})")


def _float_array(got, shape, what, hint):
    if not (isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape):
        pytest.fail(f"expected {what} as a numpy.ndarray of floats of shape {shape}, got {type(got).__module__}."
                    f"{type(got).__name__}" + (f" of dtype {got.dtype} and shape {got.shape}"
                                                 if isinstance(got, np.ndarray) else f" {_show_any(got)}")
                    + f" ({hint})")


def _real(value):
    return isinstance(value, numbers.Real) and not isinstance(value, (bool, np.bool_))


def _floats_or_none(values):
    """values as a float array, or None when they are not numbers (the data of a refusal)."""
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return np.asarray(values, dtype=float)
    except (TypeError, ValueError):
        return None


# --- the rules of the chapter for the data of its tests ---------------------------------------------------------------

GAMMAS = (0.6, 0.7)             # the discount factors of the chapter; 0 and 1 are the bounds of the contract
BOUNDS = (0.0, 1.0)
# 1 ± ε for ε = 0.1, …, 0.4: the bounds of a symmetric interval around 1, never a truncation level here (a truncation
# has no lower bound)
SYMMETRIC_BOUNDS = tuple(1 + sign * k / 10 for sign in (-1, 1) for k in range(1, 5))


def _rules_failure(text):
    pytest.fail(f"expected test data that follow the rules of the chapter, got {text}")


def _follows_the_rules_sfg(f, s):
    """Never the example of the docstring."""
    F, S = _floats_or_none(f), _floats_or_none(s)
    if F is None or S is None or F.ndim != 1 or S.ndim not in (1, 2) or len(S) != F.size:
        return
    if F.size == 4 and np.allclose(F, [3, 0, 2, 5]):
        _rules_failure("the values f of the example of the docstring")


def _follows_the_rules_pge(P, r, logits, gamma):
    """γ among 0.6 and 0.7 (0 and 1 for the bounds of the contract); never a state with two actions whose logits are
    equal (π = (1/2, 1/2), as with the zero logits of the example of the docstring); never the MDP of the example of
    the docstring. Data that are not numbers or out of range (a refusal) are not checked."""
    if _real(gamma) and math.isfinite(gamma) and 0 <= gamma <= 1 and float(gamma) not in GAMMAS + BOUNDS:
        _rules_failure(f"γ = {gamma!r} (the chapter takes γ among {GAMMAS}, plus the bounds 0 and 1 of the contract)")
    Z = _floats_or_none(logits)
    if Z is not None and Z.ndim == 2 and Z.shape[1] == 2 and np.all(np.isfinite(Z)) and np.any(Z[:, 0] == Z[:, 1]):
        _rules_failure(f"a state with two actions of equal logits: {_show(Z)}")
    T, R = _floats_or_none(P), _floats_or_none(r)
    if (T is not None and R is not None and T.shape == (2, 2, 2) and R.shape == (2, 2)
            and np.allclose(T, [[[1, 0], [1, 0]], [[0, 1], [0, 1]]]) and np.allclose(R, [[1, 0], [0, 2]])):
        _rules_failure("the MDP of the example of the docstring")


def _follows_the_rules_iw(lt, lq, max_weight):
    """Never the examples of the docstring; a truncation level is never one of the bounds 1 ± ε of a symmetric interval
    around 1 (a truncation has no lower bound)."""
    if _real(max_weight) and math.isfinite(max_weight) and any(math.isclose(max_weight, b) for b in SYMMETRIC_BOUNDS):
        _rules_failure(f"the truncation level {max_weight!r}, a bound 1 ± ε of a symmetric interval around 1")
    A, B = _floats_or_none(lt), _floats_or_none(lq)
    if A is None or B is None or A.ndim != 1 or A.shape != B.shape:
        return
    if A.size == 4 and np.allclose(A, [-1.0, -0.5, -0.5, -2.0]) and np.allclose(B, [-1.5, -1.0, -1.0, -1.0]):
        _rules_failure("the log-densities of the example of the docstring")
    if A.size == 3 and np.array_equal(np.isinf(A), [False, True, False]) and np.allclose(B, 0.0):
        _rules_failure("the truncated example of the docstring")


def _follows_the_rules_bt(wins):
    """Never the tournaments of the docstring."""
    W = _floats_or_none(wins)
    if W is None or W.ndim != 2:
        return
    for example in ([[0, 4], [1, 0]], [[0, 4, 2], [1, 0, 3], [1, 2, 0]], [[0, 2, 1], [0, 0, 3], [0, 1, 0]]):
        if W.shape == np.shape(example) and np.allclose(W, example):
            _rules_failure(f"the tournament {example} of the docstring")


# --- what the module may use ----------------------------------------------------------------------------------------

def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``solve`` (from numpy.linalg import solve) → "numpy.linalg.solve". Relative imports
    (from .markov import bellman_linear_solve) are your own modules."""
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
    ("policy_gradient_exact", "numpy.linalg.solve"); ``where`` is the top-level function, or "the module level"."""
    inner = {id(node.value) for node in ast.walk(tree) if isinstance(node, ast.Attribute)}
    uses = []
    for statement in tree.body:
        where = _where(statement)
        for node in ast.walk(statement):
            if not isinstance(node, (ast.Name, ast.Attribute)) or id(node) in inner:
                continue                                  # only the whole chain numpy.linalg.solve
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


FORBIDDEN_MODULES = ("scipy", "sklearn", "statistics", "pandas", "sympy", "mpmath", "torch", "jax")
ALLOWED_LINALG = ("solve", "matrix_rank")
FORBIDDEN_STRINGS = {"scipy", "sklearn", "inv", "pinv", "lstsq", "eig", "eigvals", "matrix_power", "det",
                     "logsumexp", "softmax", "expit", "minimize", "LogisticRegression"}


def _string_uses(tree):
    """getattr(np.linalg, "inv") and the like, and __import__("scipy") or importlib.import_module("sklearn"): a
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


def test_module_uses_numpy_and_math_and_from_np_linalg_only_solve_and_matrix_rank(pg_module):
    """The docstring allows NumPy and the module math, but from np.linalg only solve and matrix_rank, in
    policy_gradient_exact (with the helpers of the module that it calls); not np.linalg.inv, pinv, lstsq, eig nor
    matrix_power; no SciPy (scipy.optimize, scipy.special.logsumexp, softmax and expit are oracles of the tests) and
    no scikit-learn (LogisticRegression is another); nor SymPy, statistics or pandas. Relative imports of your own
    modules are allowed (from .markov import bellman_linear_solve). Only the code counts: a comment, a docstring or an
    import never used is not a use; ``np.linalg.LinAlgError`` (an exception, not a computation) is not counted."""
    try:
        tree = ast.parse(inspect.getsource(pg_module))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    functions = {n.name: n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    allowed = _reachable(functions, "policy_gradient_exact") - {"score_function_gradient", "importance_weights",
                                                                "bradley_terry_fit"}
    found = []
    for where, path in _uses(tree, _imported_names(tree)):
        parts = path.split(".")
        shown = ".".join(["np"] + parts[1:]) if parts[0] == "numpy" else path
        if parts[0] in FORBIDDEN_MODULES:
            found.append(f"{shown} in {where}")
        elif parts[0] == "numpy" and len(parts) > 2 and parts[1] == "linalg":
            if parts[2] == "LinAlgError" or (parts[2] in ALLOWED_LINALG and where in allowed):
                continue
            found.append(f"{shown} in {where}")
    found += _string_uses(tree)
    assert not found, (f"expected NumPy and math only, with from np.linalg only solve and matrix_rank in "
                       f"policy_gradient_exact, and no SciPy nor scikit-learn, found {sorted(set(found))} (the tests "
                       f"compare your results with scipy.special.softmax and logsumexp, scipy.optimize.minimize and "
                       f"sklearn's LogisticRegression: np.exp, np.log, np.max, np.sum, np.einsum, the @ product and "
                       f"a loop for Zermelo's sweeps are enough)")


# --- score_function_gradient ----------------------------------------------------------------------------------------

SFG_HINT = ("g_i = (f(x_i) - b_i) s_i, where b_i is the constant baseline, or with \"leave-one-out\" the mean of the "
            "n - 1 other values, (Σ_j f_j - f_i) / (n - 1); return the mean of the g_i and their standard error "
            "std(g, ddof=1) / √n, coordinate by coordinate for a 2-D scores: two Python floats for a 1-D scores, two "
            "numpy.ndarray of shape (d,) for a 2-D one")
SFG_SECONDS = 20
_DEFAULT = object()


def _describe_sfg(f, s, baseline=_DEFAULT, positional=False):
    args = f"{_show(f)}, {_show(s)}"
    if baseline is _DEFAULT:
        return f"score_function_gradient({args})"
    b = repr(baseline) if isinstance(baseline, str) else _num(baseline)
    return f"score_function_gradient({args}, {b})" if positional else f"score_function_gradient({args}, baseline={b})"


def _sfg_call(pg, f, s, baseline=_DEFAULT, positional=False):
    if baseline is _DEFAULT:
        return lambda: pg.score_function_gradient(f, s)
    if positional:
        return lambda: pg.score_function_gradient(f, s, baseline)
    return lambda: pg.score_function_gradient(f, s, baseline=baseline)


def _check_sfg_types(got, s, what):
    """(estimate, standard error): two Python floats for a 1-D scores, two arrays of shape (d,) for a 2-D one."""
    if not (isinstance(got, tuple) and len(got) == 2):
        pytest.fail(f"expected {what} as a tuple (estimate, standard_error), got {_show_any(got)} ({SFG_HINT})")
    S = np.asarray(s, dtype=float)
    for value, name in zip(got, ("the estimate", "the standard error")):
        if S.ndim == 1:
            _python_float(value, f"{name} of {what}", SFG_HINT)
        else:
            _float_array(value, (S.shape[1],), f"{name} of {what} (a 2-D scores of {S.shape[1]} columns)", SFG_HINT)


def _sfg(pg, f, s, baseline=_DEFAULT, positional=False, what=None, seconds=SFG_SECONDS):
    """score_function_gradient(f, s[, baseline]), its types checked."""
    _follows_the_rules_sfg(f, s)
    what = what or _describe_sfg(f, s, baseline, positional)
    got = _within(seconds, _sfg_call(pg, f, s, baseline, positional), what, "(estimate, standard_error)", SFG_HINT)
    _check_sfg_types(got, s, what)
    return got


def _baselines(f, baseline):
    """The baselines b_i as fractions of the floats received."""
    F = [Fraction(float(x)) for x in np.asarray(f, dtype=float)]
    if isinstance(baseline, str):
        total = sum(F, Fraction(0))
        return F, [(total - x) / (len(F) - 1) for x in F]
    b = Fraction(float(0.0 if baseline is _DEFAULT else baseline))
    return F, [b] * len(F)


def _exact_sfg(f, s, baseline):
    """The estimate and the standard error computed exactly in fractions from the floats received: the terms
    g_i = (f_i - b_i) s_i, their mean, and their variance with n - 1; the standard error √(var / n) is rounded once.
    For a 2-D s, one value per column. Returns (estimate, standard error, scale of the rounding allowed)."""
    F, B = _baselines(f, baseline)
    n = len(F)
    S = np.asarray(s, dtype=float)
    columns = [S] if S.ndim == 1 else [S[:, k] for k in range(S.shape[1])]
    estimates, errors = [], []
    for column in columns:
        g = [(F[i] - B[i]) * Fraction(float(column[i])) for i in range(n)]
        mean = sum(g, Fraction(0)) / n
        var = sum(((x - mean) ** 2 for x in g), Fraction(0)) / (n - 1)
        estimates.append(float(mean))
        errors.append(math.sqrt(float(var / n)))
    scale = (1.0 + max(abs(float(x)) for x in F)) * (1.0 + float(np.max(np.abs(S))))
    if S.ndim == 1:
        return estimates[0], errors[0], scale
    return np.array(estimates), np.array(errors), scale


def _sfg_variants(f, s, baseline):
    """(part, value, reason) of classic errors computed in floats; part is "estimate" or "error"."""
    f = np.asarray(f, dtype=float)
    S = np.asarray(s, dtype=float)
    n = f.size
    loo = isinstance(baseline, str)
    b = (np.sum(f) - f) / (n - 1) if loo else np.full(n, float(0.0 if baseline is _DEFAULT else baseline))

    def terms(c):
        return c * S if S.ndim == 1 else c[:, None] * S

    g = terms(f - b)
    plain = terms(f)
    out = []
    if np.any(b != 0):
        bb = b if S.ndim == 1 else b[:, None]
        out.append(("estimate", np.mean(plain - bb, axis=0),
                    "the baseline is subtracted from f(x_i) before the product: g_i = (f(x_i) - b_i) s_i, not "
                    "f(x_i) s_i - b_i"))
        out.append(("estimate", np.mean(f[:, None] * (S - bb) if S.ndim == 2 else f * (S - b), axis=0),
                    "the baseline is subtracted from f(x_i), not from the score: g_i = (f(x_i) - b_i) s_i"))
        out.append(("error", np.std(plain, axis=0, ddof=1) / math.sqrt(n),
                    "the standard error is that of the terms g_i = (f(x_i) - b_i) s_i, the baseline included"))
    if loo:
        out.append(("estimate", np.mean(terms(f - (np.sum(f) - f) / n), axis=0),
                    "with \"leave-one-out\", b_i is the mean of the n - 1 other values: their sum Σ_j f_j - f_i, "
                    "divided by n - 1"))
    out.append(("error", np.std(g, axis=0, ddof=1),
                "the standard error of a mean is the standard deviation of its terms divided by √n"))
    out.append(("error", np.std(g, axis=0, ddof=1) / n,
                "the standard error is the standard deviation of the terms divided by √n, not by n"))
    return out


def _check_sfg(got, f, s, baseline, what, rtol=1e-11):
    estimate, error, scale = _exact_sfg(f, s, baseline)
    atol = 1e-12 * scale
    variants = _sfg_variants(f, s, baseline)
    where = (lambda k: f"coordinate {k}") if np.ndim(s) == 2 else None
    for part, got_part, want, name in (("estimate", got[0], estimate, "the estimate"),
                                       ("error", got[1], error, "the standard error")):
        candidates = [(value, text) for kind, value, text in variants if kind == part]
        _close(got_part, want, f"{name} of {what}", rtol=rtol, atol=atol, where=where,
               hint=lambda gp=got_part, w=want, c=candidates: _here(_first_match(gp, w, c), SFG_HINT))


def _sample(rng, n, scale=2.31, offset=0.0):
    """n values that are not dyadic."""
    return np.round(rng.normal(size=n) * scale + offset, 6) + 1e-7 * rng.uniform(0.11, 0.89, size=n)


SFG_NS = [2, 3, 7, 31, 400]


@pytest.mark.parametrize("n", SFG_NS, ids=[f"n{n}" for n in SFG_NS])
def test_score_function_gradient_plain_estimate_matches_exact_sums(pg, n):
    """Without a baseline (b = 0, the default): the mean of the f(x_i) s_i and the standard error
    std(g, ddof=1) / √n, computed exactly in fractions from the floats received."""
    rng = _rng(8000, n)
    for _ in range(3):
        f, s = _sample(rng, n, 1.71, 0.61), _sample(rng, n, 1.11)
        _check_sfg(_sfg(pg, f, s), f, s, _DEFAULT, _describe_sfg(f, s))


@pytest.mark.parametrize("n", SFG_NS, ids=[f"n{n}" for n in SFG_NS])
def test_score_function_gradient_constant_baseline_matches_exact_sums(pg, n):
    """A constant baseline b (positive, negative, an integer): g_i = (f(x_i) - b) s_i, then their mean and standard
    error, exactly."""
    rng = _rng(8001, n)
    for b in (float(np.round(rng.uniform(1.51, 4.5), 3)), -float(np.round(rng.uniform(0.41, 2.2), 4)), 14):
        f, s = _sample(rng, n, 1.91, 2.41), _sample(rng, n, 0.89)
        _check_sfg(_sfg(pg, f, s, b), f, s, b, _describe_sfg(f, s, b))


@pytest.mark.parametrize("n", SFG_NS, ids=[f"n{n}" for n in SFG_NS])
def test_score_function_gradient_leave_one_out_matches_exact_sums(pg, n):
    """baseline="leave-one-out": b_i is the mean of the n - 1 other values (for n = 2, the other value); the terms
    g_i = (f(x_i) - b_i) s_i, their mean and their standard error, exactly."""
    rng = _rng(8002, n)
    for _ in range(3):
        f, s = _sample(rng, n, 2.1, 1.31), _sample(rng, n, 1.31)
        _check_sfg(_sfg(pg, f, s, "leave-one-out"), f, s, "leave-one-out", _describe_sfg(f, s, "leave-one-out"))


SFG_2D = [(2, 1), (5, 2), (9, 3), (61, 5)]


@pytest.mark.parametrize("n, d", SFG_2D, ids=[f"n{n}-d{d}" for n, d in SFG_2D])
def test_score_function_gradient_2d_scores_coordinate_by_coordinate(pg, n, d):
    """scores of shape (n, d), row i the gradient of ln p_θ(x_i) for θ in ℝ^d (d = 1 included): every coordinate is
    the estimate of its own derivative, with its own standard error; both are arrays of shape (d,)."""
    rng = _rng(8003, n)
    for baseline in (_DEFAULT, float(np.round(rng.uniform(0.71, 2.91), 3)), "leave-one-out"):
        f, s = _sample(rng, n, 1.61, 0.89), _sample(rng, n * d, 1.21).reshape(n, d)
        what = _describe_sfg(f, s, baseline)
        _check_sfg(_sfg(pg, f, s, baseline, what=what), f, s, baseline, what)


def test_score_function_gradient_one_column_is_not_the_1d_case(pg):
    """scores of shape (n, 1) gives two arrays of shape (1,), with the same numbers as the 1-D scores of the same
    column (two Python floats)."""
    rng = _rng(8004)
    f, s = _sample(rng, 11, 1.41, 0.71), _sample(rng, 11, 0.79)
    flat = _sfg(pg, f, s, "leave-one-out")
    column = _sfg(pg, f, s[:, None], "leave-one-out")
    for k, name in enumerate(("estimate", "standard error")):
        _close(column[k], np.array([flat[k]]), f"the {name} of {_describe_sfg(f, s[:, None], 'leave-one-out')} (the "
               f"{name} of the 1-D scores, as an array of shape (1,))", rtol=1e-13, atol=1e-15, hint=SFG_HINT)


# --- the absence of bias, by enumeration of every sample

def _binomial_law(theta, trials=3):
    """B(trials, θ) with θ a fraction: the outcomes, their probabilities and their scores x/θ - (trials - x)/(1 - θ),
    exactly."""
    outcomes = list(range(trials + 1))
    p = [math.comb(trials, x) * theta ** x * (1 - theta) ** (trials - x) for x in outcomes]
    s = [Fraction(x) / theta - Fraction(trials - x) / (1 - theta) for x in outcomes]
    return outcomes, p, s


def _categorical_law(t1, t2):
    """The law (θ1, θ2, 1 - θ1 - θ2) on three outcomes, θ = (θ1, θ2) in ℝ²: the scores are (1/θ1, 0), (0, 1/θ2) and
    (-1/θ3, -1/θ3), exactly."""
    t3 = 1 - t1 - t2
    return [0, 1, 2], [t1, t2, t3], [(1 / t1, Fraction(0)), (Fraction(0), 1 / t2), (-1 / t3, -1 / t3)]


def _expected_estimate(pg, outcomes, p, s, f, n, baseline, what, two_d=False):
    """The expectation of the estimate over the samples of n independent draws, by enumeration: Σ over the
    len(outcomes)^n samples of P(sample) × estimate(sample), accumulated exactly from the floats returned."""
    total = [Fraction(0)] * (2 if two_d else 1)
    calls = []
    for sample in itertools.product(range(len(outcomes)), repeat=n):
        weight = Fraction(1)
        for k in sample:
            weight *= p[k]
        fv = np.array([f[k] for k in sample])
        sv = np.array([[float(c) for c in s[k]] for k in sample]) if two_d else np.array([float(s[k]) for k in sample])
        b = float(np.mean(fv)) if baseline == "mean" else baseline
        calls.append((weight, fv, sv, b))
    _follows_the_rules_sfg(calls[0][1], calls[0][2])

    def run():
        out = []
        for weight, fv, sv, b in calls:
            got = (pg.score_function_gradient(fv, sv) if b is _DEFAULT else
                   pg.score_function_gradient(fv, sv, baseline=b))
            out.append((weight, got[0]))
        return out

    results = _within(SFG_SECONDS, run, what, "an estimate for every sample", SFG_HINT)
    for weight, estimate in results:
        values = np.atleast_1d(np.asarray(estimate, dtype=float))
        if values.shape != (len(total),) or not np.all(np.isfinite(values)):
            pytest.fail(f"expected a finite estimate of shape {'(2,)' if two_d else '()'} for every sample of {what}, "
                        f"got {_show_any(estimate)} ({SFG_HINT})")
        for k in range(len(total)):
            total[k] += weight * Fraction(float(values[k]))
    return total


ENUM_CASES = [(2, "binomial"), (3, "binomial"), (4, "binomial"), (2, "categorical"), (3, "categorical"),
              (4, "categorical")]


@pytest.mark.parametrize("n, law", ENUM_CASES, ids=[f"n{n}-{law}" for n, law in ENUM_CASES])
def test_score_function_gradient_is_unbiased_on_discrete_laws_by_enumeration(pg, n, law):
    """Over every sample of n independent draws of a discrete law (B(3, θ) with θ = 0.38, or a law on three
    outcomes with a parameter in ℝ²), the mean of the estimates weighted by the probabilities of the samples is
    d/dθ E_θ[f(X)] = Σ_x f(x) p_θ(x) s_θ(x), exactly (up to the rounding of each estimate), without a baseline, with
    a constant baseline and with "leave-one-out"; a discontinuous f (an indicator) included. With the mean of the whole
    sample given as a constant baseline, it is (n - 1)/n times the derivative: that baseline depends on each x_i."""
    if law == "binomial":
        outcomes, p, s = _binomial_law(Fraction("0.38"))
        functions = [("the indicator 1{x > 1}", [0.0, 0.0, 1.0, 1.0]), ("f = (2.65, 0.53, 5.7, 1.95)",
                                                                         [2.65, 0.53, 5.7, 1.95])]
    else:
        outcomes, p, s = _categorical_law(Fraction("0.21"), Fraction("0.47"))
        functions = [("f = (1.85, -0.62, 3.37)", [1.85, -0.62, 3.37]), ("the indicator 1{x = 1}", [0.0, 1.0, 0.0])]
    two_d = law == "categorical"
    for name, f in functions:
        if two_d:
            derivative = [sum(Fraction(f[x]) * p[x] * s[x][k] for x in range(3)) for k in range(2)]
        else:
            derivative = [sum(Fraction(f[x]) * p[x] * s[x] for x in range(len(outcomes)))]
        scale = 1e-12 * (1 + max(abs(v) for v in f)) * max(abs(float(c)) for row in s
                                                           for c in (row if two_d else [row]))
        for baseline, factor, text in ((_DEFAULT, Fraction(1), "without a baseline"),
                                       (2.15, Fraction(1), "with the constant baseline 2.15"),
                                       ("leave-one-out", Fraction(1), "with \"leave-one-out\""),
                                       ("mean", Fraction(n - 1, n), "with the mean of the whole sample as a constant "
                                                                    "baseline, (n - 1)/n times the derivative")):
            what = f"score_function_gradient for every sample of {n} draws of the {law} law, {name}, {text}"
            total = _expected_estimate(pg, outcomes, p, s, f, n, baseline, what, two_d)
            for k in range(len(total)):
                want = float(factor * derivative[k])
                if not math.isclose(float(total[k]), want, rel_tol=1e-11, abs_tol=scale):
                    coordinate = f" (coordinate {k})" if two_d else ""
                    pytest.fail(f"expected the mean of the estimates over the {len(outcomes) ** n} samples of {n} "
                                f"draws, weighted by their probabilities, to be {want:.12g}{coordinate} for {what}, "
                                f"got {float(total[k]):.12g} (E_θ[s_θ(X)] = 0: a constant baseline, or one that does "
                                f"not depend on x_i, leaves the expectation unchanged; {SFG_HINT})")


def test_score_function_gradient_does_not_change_when_f_and_the_baseline_move_together(pg):
    """f + c with the baseline b + c gives the same terms (f(x_i) - b) s_i; with "leave-one-out", f + c alone gives
    the same terms too (each b_i moves by c). Equal up to rounding."""
    rng = _rng(8005)
    for n in (4, 14, 58):
        f, s = _sample(rng, n, 1.79, 0.41), _sample(rng, n, 1.06)
        c = float(np.round(rng.uniform(2.1, 9.7), 4))
        b = float(np.round(rng.uniform(-1.61, 1.61), 3))
        base = _sfg(pg, f, s, b)
        moved = _sfg(pg, f + c, s, b + c)
        scale = 1e-12 * (1 + np.max(np.abs(f)) + c) * (1 + np.max(np.abs(s)))
        for k, name in enumerate(("estimate", "standard error")):
            _close(moved[k], base[k], f"the {name} of {_describe_sfg(f + c, s, b + c)} (f and the baseline both moved "
                   f"by {c}: the same terms)", rtol=1e-11, atol=scale, hint=SFG_HINT)
        base = _sfg(pg, f, s, "leave-one-out")
        moved = _sfg(pg, f + c, s, "leave-one-out")
        for k, name in enumerate(("estimate", "standard error")):
            _close(moved[k], base[k], f"the {name} of {_describe_sfg(f + c, s, 'leave-one-out')} (f moved by {c}: "
                   f"each b_i moves by {c} too)", rtol=1e-11, atol=scale, hint=SFG_HINT)


def test_score_function_gradient_of_terms_that_are_all_zero(pg):
    """f constant and equal to the baseline: every term is 0, the estimate and the standard error are 0; the same with
    "leave-one-out" (each b_i is that constant), up to rounding."""
    rng = _rng(8006)
    for n in (2, 5, 27):
        c = float(np.round(rng.uniform(1.11, 6.3), 5))
        f, s = np.full(n, c), _sample(rng, n, 1.41)
        for baseline in (c, "leave-one-out"):
            got = _sfg(pg, f, s, baseline)
            _close(np.array(got), np.zeros(2), f"(estimate, standard error) of {_describe_sfg(f, s, baseline)} (every "
                   f"term (f(x_i) - b_i) s_i is 0)", rtol=0, atol=1e-13 * c * (1 + np.max(np.abs(s))), hint=SFG_HINT)


SFG_KINDS = [(lambda v: v.tolist(), "lists"), (lambda v: tuple(v.tolist()), "tuples"),
             (lambda v: np.round(v * 10).astype(int), "integer arrays"), (lambda v: v.astype(np.float32), "float32")]


@pytest.mark.parametrize("convert, text", SFG_KINDS, ids=["lists", "tuples", "ints", "float32"])
def test_score_function_gradient_accepts_lists_tuples_integers_and_float32(pg, convert, text):
    """f_values and scores given as lists, tuples, integer arrays or float32 arrays (the values they hold)."""
    rng = _rng(8008, [t for _, t in SFG_KINDS].index(text))
    f0, s0 = _sample(rng, 9, 1.31, 0.79), _sample(rng, 9, 0.71)
    f, s = convert(f0), convert(s0)
    what = _describe_sfg(f, s, "leave-one-out") + f" (values as {text})"
    F, S = np.asarray(f, dtype=float), np.asarray(s, dtype=float)
    _check_sfg(_sfg(pg, f, s, "leave-one-out", what=what), F, S, "leave-one-out", what)


NUMBER_BASELINES = [(np.float64(1.37), "np.float64(1.37)"), (np.int64(2), "np.int64(2)"), (-4, "the integer -4"),
                    (np.float32(0.625), "np.float32(0.625)")]


@pytest.mark.parametrize("b, text", NUMBER_BASELINES, ids=["float64", "int64", "int", "float32"])
def test_score_function_gradient_baseline_may_be_a_numpy_number_given_by_position(pg, b, text):
    """The baseline may be a Python integer or a NumPy number, given by keyword or by position."""
    rng = _rng(8009, [t for _, t in NUMBER_BASELINES].index(text))
    f, s = _sample(rng, 8, 1.21, 1.01), _sample(rng, 8, 0.89)
    for positional in (False, True):
        what = _describe_sfg(f, s, b, positional) + f" (the baseline is {text})"
        _check_sfg(_sfg(pg, f, s, b, positional=positional, what=what), f, s, b, what)


def test_score_function_gradient_does_not_modify_its_inputs(pg_module):
    """f_values and scores (1-D and 2-D) as float arrays that are not dyadic: left unchanged, whatever the baseline."""
    rng = _rng(8010)
    for s in (_sample(rng, 12, 1.31), _sample(rng, 36, 0.79).reshape(12, 3)):
        for baseline in (_DEFAULT, 2.17, "leave-one-out"):
            f = _sample(rng, 12, 1.91, 0.51)
            cf, cs = f.copy(), s.copy()
            what = _describe_sfg(f, s, baseline)
            _within(SFG_SECONDS, _sfg_call(pg_module, f, s, baseline), what, "(estimate, standard_error)", SFG_HINT)
            assert np.array_equal(f, cf) and np.array_equal(s, cs), (
                f"expected f_values and scores unchanged by {what}, got {_show(f)} and {_show(s)} (never modify the "
                f"arrays you receive: f - b is a new array, f -= b changes f itself)")


F3, S3 = [0.41, 1.67, 2.95], [0.57, -1.21, 0.64]
BAD_SFG = [
    ([[0.41, 1.67, 2.95]], S3, _DEFAULT, "f_values of shape (1, 3), not 1-D"),
    ([0.41], [0.57], _DEFAULT, "a single value: n ≥ 2"),
    ([], [], _DEFAULT, "no value"),
    (2.95, 0.57, _DEFAULT, "f_values is a number (0-D)"),
    ([0.41, np.nan, 2.95], S3, _DEFAULT, "a nan in f_values"),
    ([0.41, 1.67, np.inf], S3, _DEFAULT, "inf in f_values"),
    ([-np.inf, 1.67, 2.95], S3, "leave-one-out", "-inf in f_values"),
    (F3, [0.57, -1.21], _DEFAULT, "2 scores for 3 values"),
    (F3, [0.57], _DEFAULT, "1 score for 3 values (NumPy would broadcast it)"),
    (F3, [[0.57, -1.21]], _DEFAULT, "scores of shape (1, 2): 1 row for 3 values (NumPy would broadcast it)"),
    (F3, [[0.57, -1.21, 0.64], [0.86, 0.13, -0.47]], _DEFAULT, "scores of shape (2, 3): 2 rows for 3 values"),
    (F3, [[[0.57]], [[-1.21]], [[0.64]]], _DEFAULT, "scores of shape (3, 1, 1), 3-D"),
    (F3, np.zeros((3, 0)), _DEFAULT, "scores of shape (3, 0): no column"),
    (F3, [0.57, np.nan, 0.64], _DEFAULT, "a nan in scores"),
    (F3, [[0.57, 1.11], [-1.21, -np.inf], [0.64, 0.21]], _DEFAULT, "-inf in a 2-D scores"),
    (F3, S3, True, "baseline True, a bool"),
    (F3, S3, False, "baseline False, a bool"),
    (F3, S3, np.True_, "baseline np.True_, a NumPy bool"),
    (F3, S3, np.nan, "baseline nan"),
    (F3, S3, np.inf, "baseline inf"),
    (F3, S3, -np.inf, "baseline -inf"),
    (F3, S3, "mean", "the string \"mean\""),
    (F3, S3, "leave_one_out", "the string \"leave_one_out\", not \"leave-one-out\""),
    (F3, S3, "2.15", "a number written as a string"),
    (F3, S3, None, "baseline None"),
    (F3, S3, [1.26], "baseline [1.26], a list"),
    (None, S3, _DEFAULT, "f_values is None"),
    ([0.41, [1.67, 2.95]], S3, _DEFAULT, "f_values is ragged"),
]
BAD_SFG_IDS = ["f-2d", "n1", "empty", "f-number", "f-nan", "f-inf", "f-minus-inf", "s-short", "s-one", "s-one-row",
               "s-rows", "s-3d", "s-no-column", "s-nan", "s-2d-inf", "b-true", "b-false", "b-numpy-bool", "b-nan",
               "b-inf", "b-minus-inf", "b-mean", "b-underscores", "b-string-number", "b-none", "b-list", "f-none",
               "f-ragged"]


@pytest.mark.parametrize("f, s, baseline, why", BAD_SFG, ids=BAD_SFG_IDS)
def test_score_function_gradient_refusals(pg, f, s, baseline, why):
    shown = f"{f!r}, {s!r}" + ("" if baseline is _DEFAULT else f", baseline={baseline!r}")
    _expect_error(ValueError, _sfg_call(pg, f, s, baseline), f"score_function_gradient({shown})", why)


def test_score_function_gradient_of_a_large_sample_is_fast(pg):
    """200 000 draws and 3 coordinates, with "leave-one-out": within a few seconds, and equal to the sums of math.fsum
    (the terms computed in floats)."""
    rng = _rng(8007)
    n = 200_000
    f, s = _sample(rng, n, 2.2, 1.11), rng.normal(size=(n, 3)) * 0.97
    got = _sfg(pg, f, s, "leave-one-out", what="score_function_gradient(f, s, baseline=\"leave-one-out\") for 200 000 "
                                             "draws and 3 coordinates")
    b = (math.fsum(f) - f) / (n - 1)
    g = (f - b)[:, None] * s
    est = np.array([math.fsum(g[:, k]) / n for k in range(3)])
    se = np.array([math.sqrt(math.fsum((g[:, k] - est[k]) ** 2) / (n - 1) / n) for k in range(3)])
    _close(got[0], est, "the estimate for 200 000 draws", rtol=1e-9, atol=1e-12, hint=SFG_HINT,
           where=lambda k: f"coordinate {k}")
    _close(got[1], se, "the standard error for 200 000 draws", rtol=1e-9, atol=1e-12, hint=SFG_HINT,
           where=lambda k: f"coordinate {k}")


# --- policy_gradient_exact ------------------------------------------------------------------------------------------

PGE_HINT = ("π(a | s) is the softmax of the row logits[s]; P_π[s, t] = Σ_a π(a | s) P[a, s, t] and "
            "r_π[s] = Σ_a π(a | s) r[a, s]; M = (I - γ P_π)⁻¹ and V = M r_π; Q(s, a) = r[a, s] + γ Σ_t P[a, s, t] V(t) "
            "and A(s, a) = Q(s, a) - V(s); grad[s0, s, a] = M[s0, s] π(a | s) A(s, a); V of shape (m,), grad of shape "
            "(m, m, K)")
PGE_SECONDS = 20


def _describe_pge(P, r, logits, gamma):
    return f"policy_gradient_exact(P, r, logits, {_num(gamma)}) with P = {_show(P)}, r = {_show(r)}, logits = " \
           f"{_show(logits)}"


def _pge(pg, P, r, logits, gamma, what=None, seconds=PGE_SECONDS):
    """policy_gradient_exact(P, r, logits, gamma), its types and shapes checked: (V, grad)."""
    _follows_the_rules_pge(P, r, logits, gamma)
    what = what or _describe_pge(P, r, logits, gamma)
    got = _within(seconds, lambda: pg.policy_gradient_exact(P, r, logits, gamma), what, "(V, grad)", PGE_HINT)
    K, m = np.shape(P)[0], np.shape(P)[1]
    if not (isinstance(got, tuple) and len(got) == 2):
        pytest.fail(f"expected {what} as a tuple (V, grad), got {_show_any(got)} ({PGE_HINT})")
    _float_array(got[0], (m,), f"V of {what}", PGE_HINT)
    _float_array(got[1], (m, m, K), f"grad of {what}", PGE_HINT)
    return got


def _softmax_rows(Z):
    return special.softmax(np.asarray(Z, dtype=float), axis=1)


def _values(P, r, Z, gamma, pi=None):
    """V by np.linalg.solve on (I - γ P_π) V = r_π, π by scipy.special.softmax of each row of the logits."""
    P, r = np.asarray(P, dtype=float), np.asarray(r, dtype=float)
    pi = _softmax_rows(Z) if pi is None else pi
    m = P.shape[1]
    P_pi = np.einsum("sa,ast->st", pi, P)
    r_pi = np.einsum("sa,as->s", pi, r)
    return np.linalg.solve(np.eye(m) - gamma * P_pi, r_pi)


def _fd_gradient(P, r, Z, gamma, h=1e-3):
    """∂V/∂z(s, a) by centred finite differences of the values of np.linalg.solve, for steps h and h/2 combined by
    Richardson's extrapolation (error of order h⁴): grad[:, s, a]."""
    Z = np.asarray(Z, dtype=float)
    m, K = Z.shape
    out = np.zeros((m, m, K))
    for s in range(m):
        for a in range(K):
            def diff(step):
                up, down = Z.copy(), Z.copy()
                up[s, a] += step
                down[s, a] -= step
                return (_values(P, r, up, gamma) - _values(P, r, down, gamma)) / (2 * step)
            out[:, s, a] = (4 * diff(h / 2) - diff(h)) / 3
    return out


def _variant_pge(P, r, Z, gamma, kind):
    """(V, grad) computed with a classic error (kind), or None when it does not apply to these shapes."""
    P, r, Z = (np.asarray(x, dtype=float) for x in (P, r, Z))
    K, m = P.shape[0], P.shape[1]
    pi = _softmax_rows(Z)
    if kind == "columns":
        if m != K:
            return None
        pi = special.softmax(Z, axis=0)
    P_pi = np.einsum("sa,ast->st", pi, P)
    if kind == "destination":
        P_pi = np.einsum("ta,ast->st", pi, P)
    elif kind == "departures":
        P_pi = np.einsum("sa,ats->st", pi, P)
    r_pi = np.einsum("sa,as->s", pi, r)
    rr = r.T
    if kind == "layout":
        if m != K:
            return None
        r_pi = np.einsum("sa,sa->s", pi, r)
        rr = r
    try:
        M = np.linalg.solve(np.eye(m) - gamma * P_pi, np.eye(m))
    except np.linalg.LinAlgError:
        return None
    V = M @ r_pi
    Q = rr + (1.0 if kind == "no-discount" else gamma) * np.einsum("ast,t->sa", P, V)
    A = Q - (np.mean(Q, axis=1) if kind == "unweighted" else V)[:, None]
    if kind == "Q":
        A = Q
    G = M[:, :, None] * (pi * A)[None, :, :]
    if kind == "no-occupancy":
        G = np.eye(m)[:, :, None] * (pi * A)[None, :, :]
    elif kind == "over-1-minus-gamma":
        G = G / (1 - gamma) if gamma < 1 else None
    elif kind == "occupancy-law":
        G = G * (1 - gamma)
    elif kind == "transposed":
        G = M.T[:, :, None] * (pi * A)[None, :, :]
    return V, G


PGE_VARIANTS = [
    ("no-occupancy", "∂V(s0)/∂z(s, a) carries M[s0, s] = ((I - γ P_π)⁻¹)[s0, s]: a logit of state s changes the value "
                     "of every state from which s can be reached, not only V(s)"),
    ("over-1-minus-gamma", "M[s0, s] is already ν_s0(s) / (1 - γ), the occupancy law divided by 1 - γ: no other factor "
                           "1/(1 - γ)"),
    ("occupancy-law", "the gradient carries M[s0, s] = ν_s0(s) / (1 - γ), not the occupancy law ν_s0(s) itself"),
    ("transposed", "grad[s0, s, a] carries M[s0, s]: row s0, the state whose value is read; column s, the state whose "
                   "logit moves"),
    ("columns", "π(· | s) is the softmax of the ROW logits[s] (logits[s, a] has the shape (m, K)): each row of π sums "
                "to 1"),
    ("destination", "P_π[s, t] = Σ_a π(a | s) P[a, s, t]: the policy of the state s that the process leaves"),
    ("departures", "P[a, s, t] is the probability of moving from s to t: P_π[s, t] = Σ_a π(a | s) P[a, s, t]"),
    ("layout", "r[a, s] = r(s, a): r has the shape (K, m), one row per action, so r_π[s] = Σ_a π(a | s) r[a, s]"),
    ("no-discount", "Q(s, a) = r[a, s] + γ Σ_t P[a, s, t] V(t): the next value is discounted by γ"),
    ("unweighted", "V(s) = Σ_a π(a | s) Q(s, a), a mean weighted by π: A(s, a) = Q(s, a) - V(s)"),
    ("Q", "adding the same number to the logits of a state does not change π, so Σ_a ∂V(s0)/∂z(s, a) = 0: the "
          "gradient carries the advantage A = Q - V"),
]


def _pge_hint(got, part, want, P, r, Z, gamma):
    candidates = []
    for kind, text in PGE_VARIANTS:
        value = _variant_pge(P, r, Z, gamma, kind)
        if value is not None and value[part] is not None:
            candidates.append((value[part], text))
    return _here(_first_match(got, want, candidates, rtol=1e-7, atol=1e-9), PGE_HINT)


def _grad_place(k):
    return f"[s0, s, a] = {list(k)}"


def _check_pge(got, P, r, Z, gamma, what, V=None, grad=None):
    """V against np.linalg.solve, grad against the centred finite differences (or the given V and grad)."""
    V = _values(P, r, Z, gamma) if V is None else V
    grad = _fd_gradient(P, r, Z, gamma) if grad is None else grad
    scale = 1.0 + float(np.max(np.abs(V)))
    _close(got[0], V, f"V of {what}", rtol=1e-10, atol=1e-12 * scale, where=lambda s: f"state {s}",
           hint=lambda: _pge_hint(got[0], 0, V, P, r, Z, gamma))
    _close(got[1], grad, f"grad of {what} (the finite differences of V)", rtol=1e-7, atol=1e-9 * scale,
           where=_grad_place, hint=lambda: _pge_hint(got[1], 1, grad, P, r, Z, gamma))


def _mdp(rng, m, K, ends=False, concentration=0.89):
    """P (K, m, m) with rows drawn from a Dirichlet law (multiplied by factors below 1 when ends: the missing mass is
    the probability to end), r (K, m) and logits (m, K), all floats that are not dyadic."""
    P = rng.dirichlet(np.full(m, concentration), size=(K, m))
    if ends:
        P = P * rng.uniform(0.47, 0.97, size=(K, m, 1))
    r = np.round(rng.normal(size=(K, m)) * 2.41 + 0.61, 5) + 1e-7
    Z = np.round(rng.normal(size=(m, K)) * 1.36, 5) + 3e-7
    return P, r, Z


PGE_CASES = [(2, 2, 0.6), (3, 2, 0.7), (2, 3, 0.6), (4, 3, 0.7), (3, 4, 0.6), (5, 2, 0.7), (3, 3, 0.7), (6, 5, 0.6)]
PGE_IDS = [f"m{m}-K{K}-g{g}" for m, K, g in PGE_CASES]


@pytest.mark.parametrize("m, K, gamma", PGE_CASES, ids=PGE_IDS)
def test_policy_gradient_exact_values_solve_the_bellman_system(pg, m, K, gamma):
    """V solves (I - γ P_π) V = r_π (np.linalg.solve), π the softmax of each row of the logits."""
    rng = _rng(8020, PGE_CASES.index((m, K, gamma)))
    for _ in range(3):
        P, r, Z = _mdp(rng, m, K)
        what = _describe_pge(P, r, Z, gamma)
        got = _pge(pg, P, r, Z, gamma, what)
        V = _values(P, r, Z, gamma)
        _close(got[0], V, f"V of {what}", rtol=1e-10, atol=1e-12 * (1 + np.max(np.abs(V))),
               where=lambda s: f"state {s}", hint=lambda: _pge_hint(got[0], 0, V, P, r, Z, gamma))


@pytest.mark.parametrize("m, K, gamma", PGE_CASES, ids=PGE_IDS)
def test_policy_gradient_exact_gradient_matches_centred_finite_differences(pg, m, K, gamma):
    """grad[s0, s, a] = ∂V(s0)/∂z(s, a): the centred finite differences of the values of np.linalg.solve in each
    logit (Richardson's extrapolation of the steps 10⁻³ and 5·10⁻⁴), up to 10⁻⁷ relative."""
    rng = _rng(8021, PGE_CASES.index((m, K, gamma)))
    for _ in range(3):
        P, r, Z = _mdp(rng, m, K)
        what = _describe_pge(P, r, Z, gamma)
        _check_pge(_pge(pg, P, r, Z, gamma, what), P, r, Z, gamma, what)


def test_policy_gradient_exact_gradient_sums_to_0_over_the_actions_of_each_state(pg):
    """Adding the same number to every logit of a state does not change the policy: Σ_a grad[s0, s, a] = 0 for every
    s0 and s, up to rounding."""
    rng = _rng(8022)
    for m, K, gamma in ((3, 2, 0.6), (4, 4, 0.7), (2, 5, 0.7), (7, 3, 0.6)):
        P, r, Z = _mdp(rng, m, K)
        what = _describe_pge(P, r, Z, gamma)
        V, grad = _pge(pg, P, r, Z, gamma, what)
        _close(np.sum(grad, axis=2), np.zeros((m, m)), f"Σ_a grad[s0, s, a] for {what}", rtol=0,
               atol=1e-12 * (1 + np.max(np.abs(V))), where=lambda k: f"[s0, s] = {list(k)}",
               hint=lambda: _here(_first_match(np.sum(grad, axis=2), np.zeros((m, m)),
                                               [(np.sum(_variant_pge(P, r, Z, gamma, "Q")[1], axis=2),
                                                 dict(PGE_VARIANTS)["Q"])], rtol=1e-7, atol=1e-9), PGE_HINT))


def test_policy_gradient_exact_does_not_change_when_the_logits_of_a_state_move_together(pg):
    """logits[s] + c_s (a number per state) gives the same policy, hence the same V and the same grad."""
    rng = _rng(8023)
    for m, K, gamma in ((3, 2, 0.7), (4, 3, 0.6), (2, 4, 0.6)):
        P, r, Z = _mdp(rng, m, K)
        shift = np.round(rng.uniform(-6.5, 6.5, size=(m, 1)), 3)
        base = _pge(pg, P, r, Z, gamma)
        moved = _pge(pg, P, r, Z + shift, gamma)
        what = _describe_pge(P, r, Z + shift, gamma)
        scale = 1 + np.max(np.abs(base[0]))
        _close(moved[0], base[0], f"V of {what} (each row of the logits moved by {_show(shift.ravel())}: the same "
               f"policy)", rtol=1e-11, atol=1e-12 * scale, where=lambda s: f"state {s}", hint=PGE_HINT)
        _close(moved[1], base[1], f"grad of {what} (the same policy)", rtol=1e-10, atol=1e-12 * scale,
               where=_grad_place, hint=PGE_HINT)


def test_policy_gradient_exact_with_very_large_logits(pg):
    """Logits of the order of a thousand (each row moved by its own large number, rows far apart): e^z overflows, but
    the policy is the softmax of each row moved by its own maximum; V and grad are those of the logits before the move,
    finite."""
    rng = _rng(8024)
    for m, K, gamma, big in ((3, 2, 0.6, 987.25), (4, 3, 0.7, -1013.5), (2, 4, 0.7, 1500.75)):
        P, r, Z = _mdp(rng, m, K)
        big_z = Z + big * np.linspace(0.51, 1.49, m)[:, None]
        what = _describe_pge(P, r, big_z, gamma)
        V = _values(P, r, Z, gamma)
        _check_pge(_pge(pg, P, r, big_z, gamma, what), P, r, Z, gamma, what + " (logits of the order of a thousand)",
                   V=V)


def test_policy_gradient_exact_with_a_deterministic_state(pg):
    """In one state the logits differ by more than 745: in floats the policy plays one action with the probability 1
    and the others with 0 (e^{-745} underflows). V is the value of that deterministic choice there; the gradient in
    the logits of that state is 0 (moving them a little changes nothing), the others match the finite differences."""
    rng = _rng(8025)
    for m, K, gamma in ((3, 2, 0.7), (4, 3, 0.6), (2, 3, 0.6)):
        P, r, Z = _mdp(rng, m, K)
        s_det = int(rng.integers(0, m))
        Z[s_det] = np.round(rng.normal(size=K), 4) - 812.5 * np.arange(K)[::-1] * (np.arange(K)[::-1] > 0)
        a_det = int(np.argmax(Z[s_det]))
        pi = _softmax_rows(Z)
        assert pi[s_det, a_det] == 1.0 and np.all(np.delete(pi[s_det], a_det) == 0.0)   # the oracle sees it
        what = _describe_pge(P, r, Z, gamma) + f" (state {s_det} plays action {a_det} for sure)"
        got = _pge(pg, P, r, Z, gamma, what)
        _check_pge(got, P, r, Z, gamma, what, V=_values(P, r, Z, gamma, pi=pi))
        _close(got[1][:, s_det, :], np.zeros((m, K)), f"grad[:, {s_det}, :] of {what}", rtol=0,
               atol=1e-12 * (1 + np.max(np.abs(got[0]))), where=lambda k: f"[s0, a] = {list(k)}", hint=PGE_HINT)


def test_policy_gradient_exact_with_substochastic_transitions(pg):
    """Rows of the P[a] that sum to less than 1 (the missing mass is the probability that the process ends): V and
    grad still match np.linalg.solve and its finite differences."""
    rng = _rng(8026)
    for m, K, gamma in ((3, 2, 0.7), (4, 3, 0.6), (2, 2, 0.6), (5, 4, 0.7)):
        P, r, Z = _mdp(rng, m, K, ends=True)
        what = _describe_pge(P, r, Z, gamma) + " (rows of P summing to less than 1)"
        _check_pge(_pge(pg, P, r, Z, gamma, what), P, r, Z, gamma, what)


def test_policy_gradient_exact_gamma_1_when_the_process_ends_for_sure(pg):
    """γ = 1 is allowed when the process ends for sure under the policy: rows that end from every state, or an action
    that loops forever while the other one may end (the softmax plays both with a positive probability)."""
    rng = _rng(8027)
    for m, K in ((3, 2), (4, 3)):
        P, r, Z = _mdp(rng, m, K, ends=True)
        what = _describe_pge(P, r, Z, 1.0) + " (every row ends with a positive probability)"
        _check_pge(_pge(pg, P, r, Z, 1.0, what), P, r, Z, 1.0, what)
    P, r, Z = _mdp(rng, 3, 2)
    P[0] = np.eye(3)                                    # action 0 stays where it is, forever
    P[1] = P[1] * rng.uniform(0.51, 0.79, size=(3, 1))  # action 1 may end
    what = _describe_pge(P, r, Z, 1.0) + " (action 0 loops forever, action 1 may end)"
    _check_pge(_pge(pg, P, r, Z, 1.0, what), P, r, Z, 1.0, what)


def test_policy_gradient_exact_gamma_1_is_refused_when_the_process_never_ends(pg):
    """γ = 1 with stochastic P (the process never ends), or with a state whose policy is deterministic in floats and
    plays the action that loops forever: I - P_π is singular, ValueError."""
    rng = _rng(8028)
    P, r, Z = _mdp(rng, 3, 2)
    _expect_error(ValueError, lambda: pg.policy_gradient_exact(P, r, Z, 1.0), _describe_pge(P, r, Z, 1.0),
                  "γ = 1 and every P[a] is stochastic: the process never ends")
    P, r, Z = _mdp(rng, 3, 2, ends=True)
    P[0, 1] = np.eye(3)[1]                              # in state 1, action 0 stays in state 1, forever
    Z[1] = [3.25, -805.5]                               # and state 1 plays action 0 for sure (in floats)
    _follows_the_rules_pge(P, r, Z, 1.0)
    _expect_error(ValueError, lambda: pg.policy_gradient_exact(P, r, Z, 1.0), _describe_pge(P, r, Z, 1.0),
                  "γ = 1 and state 1 keeps the process there for sure: it never ends from state 1")


def test_policy_gradient_exact_gamma_0_is_one_step(pg):
    """γ = 0: V = r_π (one step), and ∂V(s0)/∂z(s, a) is 0 for s ≠ s0; it matches the finite differences."""
    rng = _rng(8029)
    for m, K in ((3, 2), (2, 4)):
        P, r, Z = _mdp(rng, m, K)
        what = _describe_pge(P, r, Z, 0.0)
        got = _pge(pg, P, r, Z, 0.0, what)
        r_pi = np.einsum("sa,as->s", _softmax_rows(Z), r)
        _check_pge(got, P, r, Z, 0.0, what, V=r_pi)


def test_policy_gradient_exact_with_one_action_or_one_state(pg):
    """K = 1: the policy plays the only action, V = (I - γ P[0])⁻¹ r[0] and grad is 0, of shape (m, m, 1); m = 1: one
    state, V of shape (1,), grad of shape (1, 1, K)."""
    rng = _rng(8030)
    P, r, Z = _mdp(rng, 4, 1)
    what = _describe_pge(P, r, Z, 0.7)
    got = _pge(pg, P, r, Z, 0.7, what)
    _close(got[0], np.linalg.solve(np.eye(4) - 0.7 * P[0], r[0]), f"V of {what} (one action)", rtol=1e-10,
           atol=1e-12, where=lambda s: f"state {s}", hint=PGE_HINT)
    _close(got[1], np.zeros((4, 4, 1)), f"grad of {what} (one action: π = 1 whatever the logit)", rtol=0, atol=1e-12,
           where=_grad_place, hint=PGE_HINT)
    for K, ends in ((3, False), (2, True)):
        P, r, Z = _mdp(rng, 1, K, ends=ends)
        what = _describe_pge(P, r, Z, 0.6) + " (one state)"
        _check_pge(_pge(pg, P, r, Z, 0.6, what), P, r, Z, 0.6, what)


def test_policy_gradient_exact_rewards_moved_by_a_constant(pg):
    """With stochastic P, r + c (the same number for every action and state) adds c / (1 - γ) to every value and
    leaves the advantages, hence the gradient, unchanged."""
    rng = _rng(8031)
    for m, K, gamma in ((3, 2, 0.6), (4, 3, 0.7)):
        P, r, Z = _mdp(rng, m, K)
        c = float(np.round(rng.uniform(3.11, 8.9), 3))
        base = _pge(pg, P, r, Z, gamma)
        what = _describe_pge(P, r + c, Z, gamma)
        moved = _pge(pg, P, r + c, Z, gamma, what)
        scale = 1 + np.max(np.abs(base[0])) + c / (1 - gamma)
        _close(moved[0], base[0] + c / (1 - gamma), f"V of {what} (r moved by {c}: V moves by c / (1 - γ))",
               rtol=1e-10, atol=1e-12 * scale, where=lambda s: f"state {s}", hint=PGE_HINT)
        _close(moved[1], base[1], f"grad of {what} (r moved by {c}: the same advantages)", rtol=1e-9,
               atol=1e-12 * scale, where=_grad_place, hint=PGE_HINT)


def test_policy_gradient_exact_accepts_lists_and_integer_arrays(pg):
    """P, r and logits as nested lists, or as integer arrays (deterministic moves)."""
    rng = _rng(8032)
    P, r, Z = _mdp(rng, 3, 2)
    what = _describe_pge(P, r, Z, 0.6) + " (nested lists)"
    _check_pge(_pge(pg, P.tolist(), r.tolist(), Z.tolist(), 0.6, what), P, r, Z, 0.6, what)
    moves = np.zeros((2, 3, 3), dtype=int)
    moves[0, [0, 1, 2], [1, 2, 0]] = 1                  # action 0 goes round, action 1 stays
    moves[1, [0, 1, 2], [0, 1, 2]] = 1
    ri = np.array([[2, -1, 4], [0, 3, -2]])
    Zi = np.array([[1, -2], [0, 2], [-1, 3]])
    what = _describe_pge(moves, ri, Zi, 0.7) + " (integer arrays)"
    _check_pge(_pge(pg, moves, ri, Zi, 0.7, what), moves, ri, Zi, 0.7, what)


def test_policy_gradient_exact_does_not_modify_its_inputs(pg_module):
    """P, r and logits as float arrays that are not dyadic (logits of the order of a thousand among them): left
    unchanged."""
    rng = _rng(8033)
    for big in (0.0, 1021.75):
        P, r, Z = _mdp(rng, 3, 3, ends=True)
        Z = Z + big
        cP, cr, cZ = P.copy(), r.copy(), Z.copy()
        what = _describe_pge(P, r, Z, 0.7)
        _follows_the_rules_pge(P, r, Z, 0.7)
        _within(PGE_SECONDS, lambda: pg_module.policy_gradient_exact(P, r, Z, 0.7), what, "(V, grad)", PGE_HINT)
        assert np.array_equal(P, cP) and np.array_equal(r, cr) and np.array_equal(Z, cZ), (
            f"expected P, r and logits unchanged by {what}, got P = {_show(P)}, r = {_show(r)}, logits = {_show(Z)} "
            f"(never modify the arrays you receive: logits - logits.max(axis=1, keepdims=True) is a new array, "
            f"logits -= … changes logits itself)")


def test_policy_gradient_exact_rows_summing_to_1_within_1e_9_are_accepted(pg):
    """Rows of P that sum to 1 + 5·10⁻¹⁰ are within the tolerance 10⁻⁹ of the docstring."""
    rng = _rng(8034)
    P, r, Z = _mdp(rng, 3, 2)
    P[1, 2] = P[1, 2] * (1 + 5e-10)
    what = _describe_pge(P, r, Z, 0.6) + " (row 2 of P[1] sums to 1 + 5e-10)"
    _check_pge(_pge(pg, P, r, Z, 0.6, what), P, r, Z, 0.6, what)


_P0 = np.array([[[0.27, 0.41, 0.32], [0.55, 0.17, 0.28], [0.06, 0.61, 0.33]],
                [[0.66, 0.21, 0.13], [0.36, 0.38, 0.26], [0.24, 0.24, 0.52]]])
_R0 = np.array([[1.37, -0.87, 2.15], [0.43, 1.85, -1.13]])
_Z0 = np.array([[0.62, -0.47], [1.18, 0.33], [-0.97, 0.27]])
BAD_PGE = [
    (_P0[0], _R0, _Z0, 0.7, "P of shape (3, 3), 2-D"),
    (np.concatenate([_P0, _P0[:, :, :1] * 0], axis=2), _R0, _Z0, 0.7, "P of shape (2, 3, 4): P[a] not square"),
    (np.zeros((0, 3, 3)), np.zeros((0, 3)), np.zeros((3, 0)), 0.7, "K = 0 actions"),
    (np.zeros((2, 0, 0)), np.zeros((2, 0)), np.zeros((0, 2)), 0.7, "m = 0 states"),
    (_P0, _R0.T, _Z0, 0.7, "r of shape (3, 2): (m, K) instead of (K, m)"),
    (_P0, np.vstack([_R0, _R0[:1]]), _Z0, 0.7, "r of shape (3, 3): 3 actions for 2"),
    (_P0, _R0, _Z0.T, 0.7, "logits of shape (2, 3): (K, m) instead of (m, K)"),
    (_P0, _R0, _Z0[:2], 0.7, "logits of shape (2, 2): 2 states for 3"),
    (_P0 * np.where(np.arange(3) == 1, -1, 1), _R0, _Z0, 0.7, "a negative entry in P"),
    (_P0 * np.array([1, 1, 1 + 1e-7])[:, None], _R0, _Z0, 0.7, "row 2 of each P[a] sums to 1 + 1e-7, more than 1"),
    (np.where(np.arange(3) == 2, np.nan, _P0), _R0, _Z0, 0.7, "a nan in P"),
    (_P0, np.where(np.arange(3) == 0, np.inf, _R0), _Z0, 0.7, "inf in r"),
    (_P0, _R0, np.where(np.arange(2) == 1, -np.inf, _Z0), 0.7, "-inf in logits"),
    (_P0, _R0, np.where(np.arange(2) == 0, np.nan, _Z0), 0.7, "a nan in logits"),
    (_P0 * 0.87, _R0, _Z0, True, "gamma True, a bool (with rows that end: γ = 1 would be allowed)"),
    (_P0, _R0, _Z0, np.False_, "gamma np.False_, a NumPy bool"),
    (_P0, _R0, _Z0, 1.27, "gamma 1.27 > 1"),
    (_P0, _R0, _Z0, -0.15, "gamma -0.15 < 0"),
    (_P0, _R0, _Z0, np.nan, "gamma nan"),
    (_P0, _R0, _Z0, "0.7", "gamma a string"),
    (_P0, _R0, _Z0, None, "gamma None"),
    (_P0 / _P0.sum(axis=2, keepdims=True), _R0, _Z0, 1.0, "γ = 1 and every P[a] stochastic: the process never ends"),
    (None, _R0, _Z0, 0.7, "P is None"),
    (_P0, [[1.37, -0.87], [0.43, 1.85, -1.13]], _Z0, 0.7, "r is ragged"),
]
BAD_PGE_IDS = ["P-2d", "P-not-square", "K0", "m0", "r-transposed", "r-rows", "logits-transposed", "logits-rows",
               "P-negative", "P-row-sum", "P-nan", "r-inf", "logits-minus-inf", "logits-nan", "gamma-true",
               "gamma-numpy-bool", "gamma-above-1", "gamma-negative", "gamma-nan", "gamma-string", "gamma-none",
               "gamma-1-never-ends", "P-none", "r-ragged"]


@pytest.mark.parametrize("P, r, logits, gamma, why", BAD_PGE, ids=BAD_PGE_IDS)
def test_policy_gradient_exact_refusals(pg, P, r, logits, gamma, why):
    _follows_the_rules_pge(P, r, logits, gamma)
    _expect_error(ValueError, lambda: pg.policy_gradient_exact(P, r, logits, gamma),
                  f"policy_gradient_exact(P, r, logits, {gamma!r})", why)


def test_policy_gradient_exact_of_many_states_is_fast(pg):
    """59 states and 4 actions, within a few seconds: V against np.linalg.solve, and the property Σ_a grad = 0."""
    rng = _rng(8035)
    P, r, Z = _mdp(rng, 59, 4, ends=True)
    what = "policy_gradient_exact(P, r, logits, 0.7) for 59 states and 4 actions"
    V, grad = _pge(pg, P, r, Z, 0.7, what)
    _close(V, _values(P, r, Z, 0.7), f"V of {what}", rtol=1e-10, atol=1e-12, where=lambda s: f"state {s}",
           hint=PGE_HINT)
    _close(np.sum(grad, axis=2), np.zeros((59, 59)), f"Σ_a grad[s0, s, a] for {what}", rtol=0, atol=1e-11,
           where=lambda k: f"[s0, s] = {list(k)}", hint=PGE_HINT)
    s, a = 14, 2
    up, down = Z.copy(), Z.copy()
    up[s, a] += 1e-4
    down[s, a] -= 1e-4
    fd = (_values(P, r, up, 0.7) - _values(P, r, down, 0.7)) / 2e-4
    _close(grad[:, s, a], fd, f"grad[:, {s}, {a}] of {what} (centred finite differences)", rtol=1e-5, atol=1e-8,
           where=lambda k: f"s0 = {k}", hint=PGE_HINT)


# --- importance_weights ---------------------------------------------------------------------------------------------

IW_HINT = ("d_i = log_target_i - log_proposal_i is ln w_i (-inf where p is 0), truncated at ln c when "
           "max_weight = c; the weights are exp(d_i), or, with self_normalize=True, exp(d_i - max d) divided by their "
           "sum; ess = (Σ w_i)² / Σ w_i², computed from exp(d_i - max d) (0.0 when every weight is 0); return "
           "(numpy.ndarray of n floats, Python float)")
IW_SECONDS = 20


def _describe_iw(lt, lq, self_normalize=None, max_weight=None, positional=False):
    args = [_show(lt), _show(lq)]
    if positional:
        args += [repr(self_normalize)] + ([_num(max_weight)] if max_weight is not None else [])
    else:
        args += ([f"self_normalize={self_normalize!r}"] if self_normalize is not None else [])
        args += ([f"max_weight={_num(max_weight)}"] if max_weight is not None else [])
    return f"importance_weights({', '.join(args)})"


def _iw_call(pg, lt, lq, self_normalize=None, max_weight=None, positional=False):
    if positional:
        extra = (self_normalize,) + ((max_weight,) if max_weight is not None else ())
        return lambda: pg.importance_weights(lt, lq, *extra)
    kwargs = {}
    if self_normalize is not None:
        kwargs["self_normalize"] = self_normalize
    if max_weight is not None:
        kwargs["max_weight"] = max_weight
    return lambda: pg.importance_weights(lt, lq, **kwargs)


def _iw(pg, lt, lq, self_normalize=None, max_weight=None, positional=False, what=None, allow_overflow=False):
    """importance_weights(…), its types checked: (array of n floats, Python float)."""
    _follows_the_rules_iw(lt, lq, max_weight)
    what = what or _describe_iw(lt, lq, self_normalize, max_weight, positional)
    got = _within(IW_SECONDS, _iw_call(pg, lt, lq, self_normalize, max_weight, positional), what, "(weights, ess)",
                  IW_HINT, allow_overflow=allow_overflow)
    if not (isinstance(got, tuple) and len(got) == 2):
        pytest.fail(f"expected {what} as a tuple (weights, ess), got {_show_any(got)} ({IW_HINT})")
    _float_array(got[0], (len(lt),), f"the weights of {what}", IW_HINT)
    _python_float(got[1], f"the ess of {what}", IW_HINT)
    return got


def _log_weights(lt, lq, max_weight=None):
    d = np.asarray(lt, dtype=float) - np.asarray(lq, dtype=float)
    return d if max_weight is None else np.minimum(d, np.log(float(max_weight)))


def _iw_oracle(lt, lq, self_normalize=False, max_weight=None):
    """The weights (exp(d), or exp(d - LSE(d)) with scipy.special.logsumexp) and the ess exp(2 LSE(d) - LSE(2d))."""
    d = _log_weights(lt, lq, max_weight)
    if np.all(d == -np.inf):
        return np.zeros(d.size), 0.0
    L1, L2 = special.logsumexp(d), special.logsumexp(2 * d)
    ess = math.exp(2 * L1 - L2)
    if self_normalize:
        return np.exp(d - L1), ess
    with np.errstate(over="ignore"):
        return np.exp(d), ess


def _iw_variants(lt, lq, self_normalize, max_weight):
    """(part, value, reason) of classic errors; part 0 is the weights, part 1 the ess."""
    d = _log_weights(lt, lq, max_weight)
    if np.all(d == -np.inf):
        return []
    raw, _ = _iw_oracle(lt, lq, False, max_weight)
    normal, ess = _iw_oracle(lt, lq, True, max_weight)
    out = [(0, normal if not self_normalize else None,
            "self_normalize=False: the weights themselves, exp(log_target - log_proposal), not divided by their sum"),
           (0, raw if self_normalize else None, "self_normalize=True: the weights are divided by their sum, so that "
                                                "they sum to 1"),
           (0, np.exp(d - np.max(d)) if not self_normalize else None,
            "the weights themselves, exp(d_i), not divided by the largest one"),
           (1, 1 / ess, "ess = (Σ w)² / Σ w², a number between 1 and n; Σ w² / (Σ w)² is its inverse")]
    if max_weight is not None:
        c = float(max_weight)
        untruncated = _iw_oracle(lt, lq, self_normalize, None)
        out.append((1, untruncated[1], "the ess is that of the weights truncated at max_weight"))
        if self_normalize:
            out.append((0, np.minimum(_iw_oracle(lt, lq, True, None)[0], c),
                        "max_weight truncates the weights before the normalization: min(w_i, c), then divided by "
                        "their sum"))
        if c > 0:
            d2 = np.minimum(np.asarray(lt, dtype=float) - np.asarray(lq, dtype=float), c)
            with np.errstate(over="ignore"):
                w2 = np.exp(d2 - special.logsumexp(d2)) if self_normalize else np.exp(d2)
            out.append((0, w2, "max_weight = c truncates the weights at c, min(w_i, c): the log-weights at ln c"))
    return out


def _check_iw(got, lt, lq, self_normalize, max_weight, what, rtol=1e-12):
    want_w, want_ess = _iw_oracle(lt, lq, bool(self_normalize), max_weight)
    variants = _iw_variants(lt, lq, bool(self_normalize), max_weight)
    d = _log_weights(lt, lq, max_weight)
    spread = float(np.max(np.abs(d[np.isfinite(d)]))) if np.any(np.isfinite(d)) else 0.0
    ess_rtol = rtol + 8e-16 * spread                    # 2 LSE(d) - LSE(2d) rounds at the scale of d
    for part, got_part, want, name, tol in ((0, got[0], want_w, "the weights", rtol + 4e-16 * spread),
                                            (1, got[1], want_ess, "the ess", ess_rtol)):
        candidates = [(value, text) for k, value, text in variants if k == part and value is not None]
        _close(got_part, want, f"{name} of {what}", rtol=tol, atol=0.0 if part == 0 else 1e-14,
               where=(lambda i: f"draw {i}") if part == 0 else None,
               hint=lambda gp=got_part, w=want, c=candidates: _here(_first_match(gp, w, c), IW_HINT))


def _logs(rng, n, spread=1.21, center=-1.41):
    return np.round(rng.normal(size=n) * spread + center, 6) + 1e-7 * rng.uniform(0.11, 0.89, size=n)


IW_NS = [1, 2, 5, 18, 310]


@pytest.mark.parametrize("n", IW_NS, ids=[f"n{n}" for n in IW_NS])
def test_importance_weights_are_the_exponentials_of_the_log_ratios(pg, n):
    """The weights exp(log_target - log_proposal), and the ess (Σ w)² / Σ w² by scipy.special.logsumexp."""
    rng = _rng(8040, n)
    for _ in range(3):
        lt, lq = _logs(rng, n), _logs(rng, n, 0.89, -1.11)
        _check_iw(_iw(pg, lt, lq), lt, lq, False, None, _describe_iw(lt, lq))


@pytest.mark.parametrize("n", IW_NS, ids=[f"n{n}" for n in IW_NS])
def test_importance_weights_self_normalized_sum_to_1_and_keep_the_ess(pg, n):
    """self_normalize=True: the weights divided by their sum (exp(d - LSE(d))), summing to 1; the same ess as the
    weights themselves."""
    rng = _rng(8041, n)
    for _ in range(3):
        lt, lq = _logs(rng, n, 1.71), _logs(rng, n, 1.11, -0.79)
        what = _describe_iw(lt, lq, True)
        got = _iw(pg, lt, lq, True)
        _check_iw(got, lt, lq, True, None, what)
        assert math.isclose(math.fsum(got[0]), 1.0, rel_tol=0, abs_tol=1e-13), (
            f"expected the weights of {what} to sum to 1, got a sum of {math.fsum(got[0])!r} ({IW_HINT})")


def test_importance_weights_do_not_change_when_the_logarithms_move_by_a_constant(pg):
    """log_target + c (a density known up to the factor e^c) multiplies every weight by e^c, and log_proposal + c
    divides them by e^c: the normalized weights and the ess do not change."""
    rng = _rng(8042)
    for n in (3, 11, 67):
        lt, lq = _logs(rng, n, 1.31), _logs(rng, n, 0.79, -0.89)
        c = float(np.round(rng.uniform(4.3, 47.9), 4))
        raw, ess = _iw(pg, lt, lq)
        normal, _ = _iw(pg, lt, lq, True)
        for moved_t, moved_q, factor, text in ((lt + c, lq, math.exp(c), f"log_target + {c}"),
                                               (lt, lq + c, math.exp(-c), f"log_proposal + {c}")):
            got_raw, got_ess = _iw(pg, moved_t, moved_q)
            what = _describe_iw(moved_t, moved_q)
            _close(got_raw, raw * factor, f"the weights of {what} ({text}: each weight times {factor:.6g})",
                   rtol=1e-12 + 1e-15 * c, atol=0.0, where=lambda i: f"draw {i}", hint=IW_HINT)
            _close(got_ess, ess, f"the ess of {what} ({text}: a common factor does not change it)", rtol=1e-12,
                   atol=0.0, hint=IW_HINT)
            got_normal, got_ess = _iw(pg, moved_t, moved_q, True)
            what = _describe_iw(moved_t, moved_q, True)
            _close(got_normal, normal, f"the weights of {what} ({text}: the factor cancels in the normalization)",
                   rtol=1e-12, atol=1e-16, where=lambda i: f"draw {i}", hint=IW_HINT)
            _close(got_ess, ess, f"the ess of {what}", rtol=1e-12, atol=0.0, hint=IW_HINT)


TRUNCATIONS = [(2.83, False), (0.47, False), (19.3, False), (2.83, True), (0.47, True), (4.7, True)]


@pytest.mark.parametrize("c, normalize", TRUNCATIONS,
                         ids=[f"c{c}-{'normalized' if s else 'raw'}" for c, s in TRUNCATIONS])
def test_importance_weights_truncated_at_max_weight(pg, c, normalize):
    """max_weight = c: min(w_i, c), before any normalization (self_normalize=True then divides the truncated weights
    by their sum); the ess is that of the truncated weights."""
    rng = _rng(8043, TRUNCATIONS.index((c, normalize)))
    for n in (6, 25, 140):
        lt, lq = _logs(rng, n, 1.61, -0.71), _logs(rng, n, 0.71, -1.31)
        what = _describe_iw(lt, lq, normalize, c)
        _check_iw(_iw(pg, lt, lq, normalize, c), lt, lq, normalize, c, what)


def test_importance_weights_truncated_below_every_weight_are_all_equal(pg):
    """A truncation level below every weight: every weight becomes c, the ess is n, and the normalized weights are
    all 1/n."""
    rng = _rng(8044)
    for n in (4, 9):
        lt, lq = _logs(rng, n, 0.41, -1.01), _logs(rng, n, 0.29, -2.91)
        c = float(np.round(np.exp(np.min(lt - lq)) * 0.43, 6))
        raw, ess = _iw(pg, lt, lq, max_weight=c)
        what = _describe_iw(lt, lq, max_weight=c)
        _close(raw, np.full(n, c), f"the weights of {what} (c is below every weight)", rtol=1e-12, atol=0.0,
               where=lambda i: f"draw {i}", hint=IW_HINT)
        _close(ess, float(n), f"the ess of {what} (equal weights)", rtol=1e-12, atol=0.0, hint=IW_HINT)
        normal, _ = _iw(pg, lt, lq, True, c)
        _close(normal, np.full(n, 1 / n), f"the weights of {_describe_iw(lt, lq, True, c)}", rtol=1e-12, atol=0.0,
               where=lambda i: f"draw {i}", hint=IW_HINT)


def test_importance_weights_max_weight_inf_truncates_nothing(pg):
    """max_weight=np.inf: the same weights and ess as without truncation; an integer or a NumPy number is accepted as
    a level, by keyword or by position."""
    rng = _rng(8045)
    lt, lq = _logs(rng, 12, 1.91), _logs(rng, 12, 0.61, -1.51)
    for normalize in (False, True):
        what = _describe_iw(lt, lq, normalize, np.inf)
        _check_iw(_iw(pg, lt, lq, normalize, np.inf), lt, lq, normalize, None, what)
    for c in (3, np.float64(2.85), np.int64(5)):
        for positional in (False, True):
            what = _describe_iw(lt, lq, False, c, positional)
            _check_iw(_iw(pg, lt, lq, False, c, positional), lt, lq, False, c, what)


def test_importance_weights_minus_inf_in_log_target_gives_a_weight_0(pg):
    """log_target = -inf (a draw where p is 0): its weight is 0, normalized or not, truncated or not; the ess counts
    the other draws only."""
    rng = _rng(8046)
    for n in (3, 8, 31):
        lt, lq = _logs(rng, n, 1.11), _logs(rng, n, 0.79, -1.21)
        lt[rng.choice(n, size=max(1, n // 3), replace=False)] = -np.inf
        for normalize, c in ((False, None), (True, None), (False, 2.83), (True, 0.47)):
            what = _describe_iw(lt, lq, normalize, c)
            _check_iw(_iw(pg, lt, lq, normalize, c), lt, lq, normalize, c, what)


def test_importance_weights_all_zero(pg):
    """Every log_target equal to -inf: the weights are all 0 and the ess is 0.0, without a RuntimeWarning; with
    self_normalize=True they cannot be divided by their sum: ValueError."""
    rng = _rng(8047)
    for n in (1, 4):
        lt, lq = np.full(n, -np.inf), _logs(rng, n)
        for c in (None, 2.83):
            what = _describe_iw(lt, lq, max_weight=c)
            got = _iw(pg, lt, lq, max_weight=c)
            _close(got[0], np.zeros(n), f"the weights of {what} (every p(x_i) is 0)", rtol=0, atol=0,
                   where=lambda i: f"draw {i}", hint=IW_HINT)
            assert got[1] == 0.0, (f"expected the ess of {what} to be 0.0 (every weight is 0), got {got[1]!r} "
                                   f"({IW_HINT})")
            _expect_error(ValueError, _iw_call(pg, lt, lq, True, c), _describe_iw(lt, lq, True, c),
                          "every weight is 0: they cannot be divided by their sum")


def test_importance_weights_beyond_the_largest_float_and_below_the_smallest(pg):
    """Log-weights near 800: e^800 is beyond the largest float, so the weights themselves are inf there (an overflow
    warning is allowed), while the normalized weights and the ess, computed from exp(d - max d), stay exact. Log-weights
    near -800 (every weight below the smallest float): the weights are 0 there, and still the normalized weights and
    the ess are exact."""
    rng = _rng(8048)
    for center in (803.5, -811.25):
        for n in (3, 10):
            lt, lq = _logs(rng, n, 1.41, center), _logs(rng, n, 0.61, -0.41)
            what = _describe_iw(lt, lq)
            got = _iw(pg, lt, lq, what=what, allow_overflow=True)
            _check_iw(got, lt, lq, False, None, what)
            what = _describe_iw(lt, lq, True)
            _check_iw(_iw(pg, lt, lq, True), lt, lq, True, None, what)
    lt = np.array([801.37, 799.82, -3.41, 640.15])
    lq = np.array([-0.62, -1.07, -0.88, -0.71])
    what = _describe_iw(lt, lq) + " (two weights beyond the largest float, one finite near e^641)"
    _check_iw(_iw(pg, lt, lq, what=what, allow_overflow=True), lt, lq, False, None, what)


def test_importance_weights_ess_lies_between_1_and_n(pg):
    """Equal weights: ess = n; one weight far above the others: ess close to 1; always 1 ≤ ess ≤ n when a weight is
    positive."""
    rng = _rng(8049)
    for n in (2, 7, 31):
        lt = np.full(n, -1.13)
        lq = np.full(n, -2.27)
        _, ess = _iw(pg, lt, lq)
        assert math.isclose(ess, n, rel_tol=1e-13), (
            f"expected the ess of {_describe_iw(lt, lq)} to be n = {n} (equal weights), got {ess!r} ({IW_HINT})")
        lt2 = lt.copy()
        lt2[n // 2] += 43.9
        _, ess = _iw(pg, lt2, lq)
        assert 1.0 - 1e-12 <= ess <= 1.0 + 1e-12, (
            f"expected the ess of {_describe_iw(lt2, lq)} to be close to 1 (one weight e^43.9 times the others), got "
            f"{ess!r} ({IW_HINT})")
        for _ in range(4):
            a, b = _logs(rng, n, 2.31), _logs(rng, n)
            _, ess = _iw(pg, a, b)
            assert 1.0 - 1e-12 <= ess <= n * (1 + 1e-12), (
                f"expected the ess of {_describe_iw(a, b)} between 1 and n = {n}, got {ess!r} ({IW_HINT})")


def test_importance_weights_estimate_an_expectation_under_the_target(pg):
    """On a discrete law with five outcomes: weighting the weights at the outcomes by the proposal q gives the target,
    Σ_x q(x) w(x) f(x) = Σ_x p(x) f(x) = E_p[f] and Σ_x q(x) w(x) = 1 (exact sums, up to the rounding of the
    weights)."""
    q = [Fraction(x) for x in ("0.13", "0.28", "0.11", "0.33", "0.15")]
    p = [Fraction(x) for x in ("0.29", "0.07", "0.21", "0.17", "0.26")]
    f = [Fraction(x) for x in ("3.37", "-1.21", "5.7", "0.41", "2.1")]
    lt = np.array([math.log(x) for x in p])
    lq = np.array([math.log(x) for x in q])
    what = _describe_iw(lt, lq)
    w, _ = _iw(pg, lt, lq)
    for g, text, want in ((f, "E_p[f]", sum(a * b for a, b in zip(p, f))), ([Fraction(1)] * 5, "1", Fraction(1))):
        total = sum(Fraction(float(x)) * Fraction(float(wi)) * gi for x, wi, gi in zip(q, w, g))
        assert math.isclose(float(total), float(want), rel_tol=1e-13, abs_tol=1e-14), (
            f"expected Σ_x q(x) w(x) {'f(x)' if g is f else ''} = {text} = {float(want):.12g} with the weights of "
            f"{what}, got {float(total):.12g} (q > 0 wherever p f ≠ 0: E_q[w f] = E_p[f]; {IW_HINT})")


IW_KINDS = [(lambda v: v.tolist(), "lists"), (lambda v: tuple(v.tolist()), "tuples"),
            (lambda v: np.round(v).astype(int), "integer arrays"), (lambda v: v.astype(np.float32), "float32")]


@pytest.mark.parametrize("convert, text", IW_KINDS, ids=["lists", "tuples", "ints", "float32"])
def test_importance_weights_accepts_lists_tuples_integers_and_float32(pg, convert, text):
    """log_target and log_proposal as lists, tuples, integer arrays or float32 arrays (the values they hold)."""
    rng = _rng(8050, [t for _, t in IW_KINDS].index(text))
    lt, lq = convert(_logs(rng, 7, 2.1)), convert(_logs(rng, 7, 1.71))
    what = _describe_iw(lt, lq, True) + f" (values as {text})"
    A, B = np.asarray(lt, dtype=float), np.asarray(lq, dtype=float)
    _check_iw(_iw(pg, lt, lq, True, what=what), A, B, True, None, what)


def test_importance_weights_does_not_modify_its_inputs(pg_module):
    """log_target and log_proposal as float arrays that are not dyadic (with -inf, near 800, truncated or not): left
    unchanged."""
    rng = _rng(8051)
    for center, normalize, c in ((-1.21, False, None), (802.75, True, None), (-0.61, True, 2.83), (-0.89, False, 0.47)):
        lt, lq = _logs(rng, 9, 1.31, center), _logs(rng, 9, 0.71)
        lt[4] = -np.inf
        ct, cq = lt.copy(), lq.copy()
        what = _describe_iw(lt, lq, normalize, c)
        _follows_the_rules_iw(lt, lq, c)
        _within(IW_SECONDS, _iw_call(pg_module, lt, lq, normalize, c), what, "(weights, ess)", IW_HINT,
                allow_overflow=True)
        assert np.array_equal(lt, ct) and np.array_equal(lq, cq), (
            f"expected log_target and log_proposal unchanged by {what}, got {_show(lt)} and {_show(lq)} (never modify "
            f"the arrays you receive: log_target - log_proposal is a new array)")


LT3, LQ3 = [-1.37, -0.62, -2.41], [-1.07, -1.18, -0.97]
BAD_IW = [
    (LT3, LQ3[:2], None, None, "lengths 3 and 2"),
    ([LT3], [LQ3], None, None, "2-D arrays of shape (1, 3)"),
    ([], [], None, None, "no draw: n ≥ 1"),
    (-1.37, -1.07, None, None, "numbers (0-D), not 1-D arrays"),
    ([-1.37, np.nan, -2.41], LQ3, None, None, "a nan in log_target"),
    ([-1.37, np.inf, -2.41], LQ3, None, None, "+inf in log_target"),
    (LT3, [-1.07, np.nan, -0.97], None, None, "a nan in log_proposal"),
    (LT3, [-1.07, -1.18, np.inf], None, None, "+inf in log_proposal"),
    (LT3, [-np.inf, -1.18, -0.97], None, None, "-inf in log_proposal: q(x_i) = 0 for a draw of q"),
    (LT3, LQ3, 1, None, "self_normalize is the integer 1, not a bool"),
    (LT3, LQ3, 0, None, "self_normalize is the integer 0, not a bool"),
    (LT3, LQ3, "True", None, "self_normalize is a string"),
    (LT3, LQ3, None, 0.0, "max_weight 0: c > 0"),
    (LT3, LQ3, None, -2.83, "max_weight is negative"),
    (LT3, LQ3, None, np.nan, "max_weight nan"),
    (LT3, LQ3, None, -np.inf, "max_weight -inf"),
    (LT3, LQ3, None, True, "max_weight True, a bool"),
    (LT3, LQ3, None, "2.83", "max_weight a string"),
    ([-np.inf, -np.inf, -np.inf], LQ3, True, None, "self_normalize=True and every weight is 0"),
    (None, LQ3, None, None, "log_target is None"),
    ([-1.37, [-0.62, -2.41]], LQ3, None, None, "log_target is ragged"),
]
BAD_IW_IDS = ["lengths", "2d", "empty", "numbers", "target-nan", "target-plus-inf", "proposal-nan", "proposal-inf",
              "proposal-minus-inf", "normalize-1", "normalize-0", "normalize-string", "max-0", "max-negative",
              "max-nan", "max-minus-inf", "max-bool", "max-string", "all-zero-normalized", "target-none",
              "target-ragged"]


@pytest.mark.parametrize("lt, lq, self_normalize, max_weight, why", BAD_IW, ids=BAD_IW_IDS)
def test_importance_weights_refusals(pg, lt, lq, self_normalize, max_weight, why):
    kwargs = {k: v for k, v in (("self_normalize", self_normalize), ("max_weight", max_weight)) if v is not None}
    shown = ", ".join([repr(lt), repr(lq)] + [f"{k}={v!r}" for k, v in kwargs.items()])
    _expect_error(ValueError, lambda: pg.importance_weights(lt, lq, **kwargs), f"importance_weights({shown})", why)


def test_importance_weights_of_a_large_sample_are_fast(pg):
    """480 000 draws, normalized and truncated: within a few seconds."""
    rng = _rng(8052)
    lt, lq = rng.normal(size=480_000) * 1.91 - 1.11, rng.normal(size=480_000) * 0.79 - 1.41
    what = "importance_weights(log_target, log_proposal, self_normalize=True, max_weight=19.3) for 480 000 draws"
    _check_iw(_iw(pg, lt, lq, True, 19.3, what=what), lt, lq, True, 19.3, what, rtol=1e-10)


# --- bradley_terry_fit ----------------------------------------------------------------------------------------------

BT_HINT = ("refuse a graph of wins that is not strongly connected (ValueError); then Zermelo's sweeps: with "
           "W_i = Σ_j wins[i, j] and n_ij = wins[i, j] + wins[j, i], p_i ← W_i / Σ_{j ≠ i} n_ij / (p_i + p_j) for "
           "every i, divided by their geometric mean, until the largest change of β = ln p is below tol (RuntimeError "
           "after max_iter sweeps); return β, an array of K floats whose sum is 0")
BT_SECONDS = 10


def _describe_bt(wins, tol=None, max_iter=None, positional=False):
    args = [_show(wins)]
    if positional:
        args += [_num(tol)] + ([repr(max_iter)] if max_iter is not None else [])
    else:
        args += ([f"tol={_num(tol)}"] if tol is not None else []) + (
            [f"max_iter={max_iter!r}"] if max_iter is not None else [])
    return f"bradley_terry_fit({', '.join(args)})"


def _bt_call(pg, wins, tol=None, max_iter=None, positional=False):
    if positional:
        extra = (tol,) + ((max_iter,) if max_iter is not None else ())
        return lambda: pg.bradley_terry_fit(wins, *extra)
    kwargs = {k: v for k, v in (("tol", tol), ("max_iter", max_iter)) if v is not None}
    return lambda: pg.bradley_terry_fit(wins, **kwargs)


def _bt(pg, wins, tol=None, max_iter=None, positional=False, what=None, seconds=BT_SECONDS):
    """bradley_terry_fit(…), its type checked: an array of K floats."""
    _follows_the_rules_bt(wins)
    what = what or _describe_bt(wins, tol, max_iter, positional)
    got = _within(seconds, _bt_call(pg, wins, tol, max_iter, positional), what, "the strengths β", BT_HINT)
    _float_array(got, (len(wins),), what, BT_HINT)
    return got


def _strongly_connected(W):
    """By scipy.sparse.csgraph: one strongly connected component for the graph i → j when W[i, j] > 0."""
    return connected_components(np.asarray(W, dtype=float) > 0, directed=True, connection="strong")[0] == 1


def _bt_minimize(W):
    """The maximum of Σ wins[i, j] ln σ(β_i - β_j) with Σ β = 0 (β_K = -Σ of the others) by scipy.optimize.minimize
    (BFGS with the exact gradient)."""
    W = np.asarray(W, dtype=float)
    K = W.shape[0]
    N = W + W.T

    def negative(b):
        beta = np.append(b, -np.sum(b))
        d = beta[:, None] - beta[None, :]
        grad = -(np.sum(W, axis=1) - np.sum(N * special.expit(d), axis=1))
        return -float(np.sum(W * special.log_expit(d))), grad[:-1] - grad[-1]

    res = optimize.minimize(negative, np.zeros(K - 1), jac=True, method="BFGS",
                            options={"gtol": 1e-12, "maxiter": 15_000})
    return np.append(res.x, -np.sum(res.x))


def _bt_sklearn(W):
    """LogisticRegression(fit_intercept=False, penalty=None) on the rows e_i - e_j (label 1, weight wins[i, j]) and
    their opposites (label 0): the coefficients, centred."""
    W = np.asarray(W, dtype=float)
    K = W.shape[0]
    X, y, weights = [], [], []
    for i, j in itertools.permutations(range(K), 2):
        if W[i, j] > 0:
            x = np.zeros(K)
            x[i], x[j] = 1.0, -1.0
            X += [x, -x]
            y += [1, 0]
            weights += [W[i, j], W[i, j]]
    model = LogisticRegression(fit_intercept=False, penalty=None, tol=1e-12, max_iter=25_000)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model.fit(np.array(X), np.array(y), sample_weight=np.array(weights))
    beta = model.coef_[0]
    return beta - np.mean(beta)


def _expected_wins(W, beta):
    W = np.asarray(W, dtype=float)
    N = W + W.T
    return np.sum(N * special.expit(beta[:, None] - beta[None, :]), axis=1)


def _zermelo_like(W, N, iterations=4000):
    """The fixed point of p_i ← W_i / Σ_j N_ij / (p_i + p_j) for another N (to recognize an error only)."""
    W = np.asarray(W, dtype=float)
    beta = np.zeros(len(W))
    with np.errstate(all="ignore"):
        for _ in range(iterations):
            p = np.exp(beta)
            beta = np.log(np.sum(W, axis=1)) - np.log(np.sum(N / (p[:, None] + p[None, :]), axis=1))
            beta -= np.mean(beta)
    return beta


def _bt_hint(got, want, W):
    g = np.asarray(got, dtype=float)
    texts = []
    if g.shape == want.shape and np.all(np.isfinite(g)):
        p = np.exp(want)
        if _same(g, np.log(p / np.mean(p)), 0, 1e-5):
            texts.append("dividing p by its arithmetic mean does not center β: the geometric mean gives "
                         "Σ_i ln p_i = 0")
        elif abs(float(np.mean(g))) > 1e-6 and _same(g - np.mean(g), want, 0, 1e-5):
            texts.append("only the differences β_i - β_j are identified: return the strengths with Σ_i β_i = 0 (divide "
                         "p by its geometric mean)")
        W = np.asarray(W, dtype=float)
        one_way = _zermelo_like(W, W)
        if np.all(np.isfinite(one_way)) and not _same(one_way, want, 0, 1e-4) and _same(g, one_way, 0, 1e-5):
            texts.append("n_ij = wins[i, j] + wins[j, i] counts the matches between i and j in both directions")
    return _here(" — or ".join(texts), BT_HINT)


def _check_bt(got, W, what, atol=1e-6, oracle="minimize"):
    """got against scipy.optimize.minimize (or scikit-learn's logistic regression), then the likelihood equations."""
    want = _bt_minimize(W) if oracle == "minimize" else _bt_sklearn(W)
    name = ("scipy.optimize.minimize on the log-likelihood with Σ β = 0" if oracle == "minimize" else
            "LogisticRegression(fit_intercept=False, penalty=None) on the differences of indicators, centred")
    _close(got, want, f"{what} ({name})", rtol=0, atol=atol, where=lambda i: f"player {i}",
           hint=lambda: _bt_hint(got, want, W))
    W = np.asarray(W, dtype=float)
    expected = _expected_wins(W, got)
    _close(expected, np.sum(W, axis=1), f"the wins expected with the strengths of {what}, Σ_j n_ij σ(β_i - β_j), "
           f"against the wins observed, Σ_j wins[i, j] (the likelihood equations)", rtol=0,
           atol=1e-6 * (1 + float(np.max(W + W.T))), where=lambda i: f"player {i}", hint=lambda: _bt_hint(got, want, W))
    total = float(np.sum(got))
    if abs(total) > 1e-9 * (1 + float(np.max(np.abs(got)))):
        pytest.fail(f"expected the strengths of {what} to sum to 0, got a sum of {total!r} for {_show(got)} "
                    f"({_bt_hint(got, want, W)})")


def _tournament(rng, K, draws=False, low=0, high=7, scale=1.0):
    """A strongly connected tournament: wins[i, j] drawn among low, …, high - 1 (times scale), plus half-points
    for draws, until the graph of wins is strongly connected (scipy.sparse.csgraph)."""
    while True:
        W = rng.integers(low, high, size=(K, K)).astype(float) * scale
        if draws:
            half = rng.integers(0, 3, size=(K, K))
            W = W + 0.5 * (half + half.T)
        np.fill_diagonal(W, 0.0)
        if _strongly_connected(W):
            return W


BT_CASES = [(2, False), (3, False), (3, True), (4, False), (6, True), (9, False), (13, True)]


@pytest.mark.parametrize("K, draws", BT_CASES, ids=[f"K{K}-{'halves' if d else 'ints'}" for K, d in BT_CASES])
def test_bradley_terry_fit_matches_scipy_minimize_on_the_centred_log_likelihood(pg, K, draws):
    """The maximum of the log-likelihood Σ wins[i, j] ln σ(β_i - β_j) with Σ β = 0 (scipy.optimize.minimize), up to
    10⁻⁶, on random strongly connected tournaments (half-points for draws included)."""
    rng = _rng(8060, BT_CASES.index((K, draws)))
    for _ in range(3):
        W = _tournament(rng, K, draws, low=int(rng.integers(0, 2)))
        _check_bt(_bt(pg, W), W, _describe_bt(W))


@pytest.mark.parametrize("K", [2, 3, 5, 8], ids=["K2", "K3", "K5", "K8"])
def test_bradley_terry_fit_matches_a_logistic_regression_on_differences_of_indicators(pg, K):
    """A logistic regression without intercept on the rows e_i - e_j, one per match won by i against j: its
    coefficients, centred (scikit-learn, up to 10⁻⁵)."""
    rng = _rng(8061, K)
    for _ in range(2):
        W = _tournament(rng, K, draws=bool(rng.integers(0, 2)))
        _check_bt(_bt(pg, W), W, _describe_bt(W), atol=1e-5, oracle="sklearn")


def test_bradley_terry_fit_of_two_players_has_a_closed_form(pg):
    """Two players: β_0 - β_1 = ln(wins[0, 1] / wins[1, 0]), so β = ± ln(wins[0, 1] / wins[1, 0]) / 2."""
    for a, b in ((7, 3), (2, 9), (5.5, 2.75), (12, 12), (1, 13)):
        W = np.array([[0.0, a], [b, 0.0]])
        what = _describe_bt(W)
        want = np.array([math.log(a / b) / 2, -math.log(a / b) / 2])
        got = _bt(pg, W)
        _close(got, want, f"{what} (± ln({a}/{b}) / 2)", rtol=0, atol=1e-9, where=lambda i: f"player {i}",
               hint=lambda: _bt_hint(got, want, W))


def test_bradley_terry_fit_follows_the_players_when_they_are_relabelled(pg):
    """Relabelling the players (the same permutation of the rows and the columns of wins) permutes the strengths."""
    rng = _rng(8062)
    for K in (3, 5, 7):
        W = _tournament(rng, K, draws=True)
        base = _bt(pg, W)
        order = rng.permutation(K)
        moved = W[np.ix_(order, order)]
        what = _describe_bt(moved)
        _close(_bt(pg, moved), base[order], f"{what} (the players relabelled by {order.tolist()})", rtol=0,
               atol=1e-7, where=lambda i: f"player {i}", hint=BT_HINT)


def test_bradley_terry_fit_does_not_change_when_every_count_is_multiplied(pg):
    """Multiplying every count by the same factor multiplies the log-likelihood: the same strengths."""
    rng = _rng(8063)
    for K in (3, 6):
        W = _tournament(rng, K)
        base = _bt(pg, W)
        for factor in (2.75, 0.36):
            what = _describe_bt(W * factor)
            _close(_bt(pg, W * factor), base, f"{what} (every count times {factor})", rtol=0, atol=1e-7,
                   where=lambda i: f"player {i}", hint=BT_HINT)


def test_bradley_terry_fit_of_a_cycle_connected_only_through_its_longest_path(pg):
    """A cycle i → i + 1 (each player beat only the next one, the last one beat the first): strongly connected, but
    from a player to the one before it the only path goes all the way round (K - 1 steps). The strengths exist and
    match scipy.optimize.minimize."""
    rng = _rng(8064)
    for K in (5, 8, 12):
        W = np.zeros((K, K))
        W[np.arange(K), (np.arange(K) + 1) % K] = rng.integers(1, 9, size=K)
        W[np.arange(K), (np.arange(K) + 1) % K] += 0.5 * rng.integers(0, 2, size=K)
        _check_bt(_bt(pg, W, what=_describe_bt(W) + f" (a cycle of {K} players)"), W, _describe_bt(W))


def _unbeaten(rng, K):
    W = _tournament(rng, K)
    W[:, 0] = 0.0                                       # nobody beat player 0
    return W, "player 0 never lost: its strength would be infinite"


def _never_won(rng, K):
    W = _tournament(rng, K)
    W[K - 1, :] = 0.0
    return W, f"player {K - 1} never won"


def _group_never_won(rng, K):
    W = _tournament(rng, K)
    k = K // 2
    W[k:, :k] = 0.0                                     # players k, …, K - 1 never beat players 0, …, k - 1
    return W, f"players {k} to {K - 1} never beat players 0 to {k - 1}"


def _two_groups(rng, K):
    W = _tournament(rng, K)
    k = K // 2
    W[k:, :k] = 0.0
    W[:k, k:] = 0.0                                     # the two groups never met
    return W, f"players 0 to {k - 1} and players {k} to {K - 1} never met"


def _no_match(rng, K):
    W = _tournament(rng, K)
    W[1, :] = 0.0
    W[:, 1] = 0.0
    return W, "player 1 played no match"


NOT_CONNECTED = [(_unbeaten, 3), (_unbeaten, 6), (_never_won, 4), (_group_never_won, 4), (_group_never_won, 7),
                 (_two_groups, 4), (_two_groups, 6), (_no_match, 5)]


@pytest.mark.parametrize("make, K", NOT_CONNECTED, ids=[f"{m.__name__[1:]}-K{K}" for m, K in NOT_CONNECTED])
def test_bradley_terry_fit_refuses_a_graph_of_wins_that_is_not_strongly_connected(pg, make, K):
    """An unbeaten player, a player who never won, a group that never beat the others, two groups that never met, a
    player without a match: the graph of wins is not strongly connected (scipy.sparse.csgraph), the likelihood keeps
    increasing, and the strengths do not exist: ValueError (not a RuntimeError after max_iter sweeps)."""
    W, why = make(_rng(8065, NOT_CONNECTED.index((make, K))), K)
    assert not _strongly_connected(W)                   # the oracle agrees
    _follows_the_rules_bt(W)
    _expect_error(ValueError, lambda: pg.bradley_terry_fit(W), _describe_bt(W), why)


def test_bradley_terry_fit_raises_runtime_error_after_max_iter_sweeps(pg):
    """max_iter = 1 or 2 with the default tol, on tournaments whose strengths are not all equal: the largest change is
    still above tol after these sweeps, RuntimeError (not a result, not an endless loop)."""
    rng = _rng(8066)
    for K, max_iter in ((3, 1), (5, 2), (4, np.int64(1))):
        W = _tournament(rng, K, low=1)
        W[0] = W[0] * 3 + 1                             # player 0 clearly stronger
        np.fill_diagonal(W, 0.0)
        _follows_the_rules_bt(W)
        _expect_error(RuntimeError, _bt_call(pg, W, max_iter=max_iter), _describe_bt(W, max_iter=max_iter),
                      f"{max_iter} sweep(s) cannot bring the change below tol = 1e-10")


def test_bradley_terry_fit_tol_and_max_iter_by_keyword_and_position(pg):
    """tol and max_iter given by keyword or by position (max_iter a Python or NumPy integer); a looser tol still gives
    strengths close to the maximum, Σ β = 0."""
    rng = _rng(8067)
    W = _tournament(rng, 5, draws=True)
    for tol, max_iter in ((1e-12, 18_000), (1e-11, np.int64(9000)), (1e-10, np.int32(5000))):
        for positional in (False, True):
            what = _describe_bt(W, tol, max_iter, positional)
            _check_bt(_bt(pg, W, tol, max_iter, positional, what=what), W, what)
    what = _describe_bt(W, tol=1e-4)
    got = _bt(pg, W, tol=1e-4, what=what)
    _close(got, _bt_minimize(W), f"{what} (a looser tol)", rtol=0, atol=6e-2, where=lambda i: f"player {i}",
           hint=BT_HINT)


def test_bradley_terry_fit_accepts_lists_and_integer_arrays(pg):
    rng = _rng(8068)
    W = _tournament(rng, 4)
    for wins, text in ((W.tolist(), "nested lists"), (W.astype(int), "an integer array"),
                       (tuple(map(tuple, W.tolist())), "nested tuples")):
        what = _describe_bt(wins) + f" ({text})"
        _check_bt(_bt(pg, wins, what=what), W, what)


def test_bradley_terry_fit_does_not_modify_wins(pg_module):
    """wins as a float array that is not dyadic (each count times 1.13, plus 0.38): left unchanged."""
    rng = _rng(8069)
    for K in (3, 6):
        W = _tournament(rng, K) * 1.13 + 0.38 * (1 - np.eye(K))
        before = W.copy()
        what = _describe_bt(W)
        _follows_the_rules_bt(W)
        _within(BT_SECONDS, lambda: pg_module.bradley_terry_fit(W), what, "the strengths β", BT_HINT)
        assert np.array_equal(W, before), (
            f"expected wins unchanged by {what}, got {_show(W)} (never modify the array you receive: W + W.T is a new "
            f"array, np.fill_diagonal changes the array itself)")


_W0 = np.array([[0.0, 3.0, 2.75], [2.0, 0.0, 4.0], [1.0, 4.5, 0.0]])


def _with(W, i, j, value):
    """A copy of W whose entry (i, j) is value."""
    W = np.array(W, dtype=float)
    W[i, j] = value
    return W


BAD_BT = [
    ([[0.0]], {}, "K = 1: one player"),
    (np.zeros((2, 3)), {}, "wins of shape (2, 3), not square"),
    (_W0[None], {}, "wins of shape (1, 3, 3), 3-D"),
    (_W0[0], {}, "wins 1-D"),
    (_with(_W0, 0, 1, -3.0), {}, "a negative count"),
    (_with(_W0, 1, 1, 2.0), {}, "a nonzero diagonal: player 1 against itself"),
    (_with(_W0, 2, 0, np.nan), {}, "a nan"),
    (_with(_W0, 1, 2, np.inf), {}, "an inf"),
    (_W0, {"tol": 0.0}, "tol 0: tol > 0"),
    (_W0, {"tol": -1e-8}, "tol negative"),
    (_W0, {"tol": np.nan}, "tol nan"),
    (_W0, {"tol": True}, "tol True, a bool"),
    (_W0, {"tol": "1e-10"}, "tol a string"),
    (_W0, {"max_iter": 0}, "max_iter 0: at least one sweep"),
    (_W0, {"max_iter": -3}, "max_iter negative"),
    (_W0, {"max_iter": 140.0}, "max_iter the float 140.0, not an integer"),
    (_W0, {"max_iter": np.float64(110.0)}, "max_iter np.float64(110.0)"),
    (_W0, {"max_iter": True}, "max_iter True, a bool"),
    (_W0, {"max_iter": "600"}, "max_iter a string"),
    (_W0, {"max_iter": None}, "max_iter None"),
    (None, {}, "wins is None"),
    ([[0.0, 3.0], [2.0]], {}, "wins is ragged"),
]
BAD_BT_IDS = ["K1", "not-square", "3d", "1d", "negative", "diagonal", "nan", "inf", "tol-0", "tol-negative", "tol-nan",
              "tol-bool", "tol-string", "max-iter-0", "max-iter-negative", "max-iter-float", "max-iter-numpy-float",
              "max-iter-bool", "max-iter-string", "max-iter-none", "wins-none", "wins-ragged"]


@pytest.mark.parametrize("wins, kwargs, why", BAD_BT, ids=BAD_BT_IDS)
def test_bradley_terry_fit_refusals(pg, wins, kwargs, why):
    shown = ", ".join([repr(wins)] + [f"{k}={v!r}" for k, v in kwargs.items()])
    _expect_error(ValueError, lambda: pg.bradley_terry_fit(wins, **kwargs), f"bradley_terry_fit({shown})", why)


def test_bradley_terry_fit_of_many_players_is_fast(pg):
    """58 players, half-points included: within a few seconds, and equal to the maximum of scipy.optimize.minimize."""
    rng = _rng(8070)
    W = _tournament(rng, 58, draws=True, low=0, high=4)
    what = "bradley_terry_fit(wins) for 58 players"
    _check_bt(_bt(pg, W, what=what), W, what)
