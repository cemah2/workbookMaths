"""Tests of mymath.attribution (chapter MB6): the weights of the coalitions in the Shapley value, the Harsanyi
dividends of a game given by its characteristic function, the line integral of a vector field along a polygonal path
by Simpson's rule on each segment, and Spearman's rank correlation.

Oracles: for the weights, ``math.comb``, ``math.factorial`` and ``fractions.Fraction`` (w[s] = 1 / (n C(n - 1, s))),
and the n! orders listed by ``itertools.permutations`` (w[|S|] is the share of the orders in which exactly the players
of S come before i); for the dividends, the game rebuilt by v(S) = Σ_{T ⊆ S} d_T, the same relation solved coalition
after coalition in ``fractions``, and the Shapley value averaged over the n! orders of ``itertools.permutations``,
compared with φ_i = Σ_{T ∋ i} d_T / |T|; for the line integral, ``scipy.integrate.quad`` on each segment, the gradient
theorem (f at the last point minus f at the first), the exactness of Simpson's rule when the integrand t ↦ g(t) is a
polynomial of degree at most 3, its exact error g''''/(180 n_sub⁴) when it is of degree 4, and an error divided by about
16 each time n_sub doubles; for Spearman's ρ, ``scipy.stats.spearmanr`` (and ``scipy.stats.rankdata`` to show the
expected ranks). Never another function of yours.
Plus properties: for the weights, their symmetry, C(n - 1, s) w[s] = 1/n, one player, many players; for the
dividends, unanimity games, additive games, linearity, v(∅) that is not 0, the order of the keys, one call of v on each
coalition (a frozenset), tables of worths, integer and NumPy worths, eleven and thirteen players; for the line
integral, gradient fields along any path (closed or not, two paths with the same ends), a field that is not a gradient,
the reversed path, forth and back, segments of length 0, a vertex added inside a segment, the points where the field is
evaluated (one at a time, a new array, never a batch), d = 1, the default n_sub, many segments; for Spearman's ρ, ties,
constant samples (nan), strictly increasing and decreasing maps, symmetry, values exactly equal or not, the bounds,
large samples. Exact types (Python floats, fractions), inputs left unchanged (floats that are not dyadic), lists,
NumPy integers, and every refusal of the docstrings. They describe the expected behaviour without showing the solution.

    pytest tests/test_mb6_attribution.py              # your code
    pytest tests/test_mb6_attribution.py --impl=ref   # the reference
"""

import ast
import inspect
import itertools
import math
import threading
import warnings
from collections import Counter
from fractions import Fraction

import numpy as np
import pytest
from scipy import integrate, stats


@pytest.fixture
def attribution_module(mymath_module):
    """The module itself: for the tests that check that your functions never write into the arrays they receive, and
    for the check of what the module uses."""
    return mymath_module("attribution")


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
def at(attribution_module):
    return _OnCopies(attribution_module)


def _text(hint):
    """A hint given as a text or as a function that computes it (only when a test fails)."""
    if not callable(hint):
        return hint
    try:
        return hint()
    except Exception:  # noqa: BLE001 - a hint must never hide the failure it explains
        return ""


def _result(call, expected, what="", hint=""):
    """call(), any error other than NotImplementedError (and any RuntimeWarning: a division by 0, an overflow, an
    invalid value…) being reported with what was expected first."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)
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


def _within(seconds, call, what, expected, hint=""):
    """_result(call, …) in a thread that is given `seconds` to answer: a result that never comes fails the test
    instead of blocking it (the thread is left to finish on its own, and every later call fails at once, so that the
    tests end quickly)."""
    if _TOO_SLOW:
        pytest.fail(f"expected {expected} for {what} in little time, but an earlier call, {_TOO_SLOW[0]}, gave no "
                    f"result after {seconds} s ({_text(hint)})")
    box = {}

    def target():
        try:
            box["value"] = _result(call, expected, what, hint)
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


def _show_fraction(w):
    return f"Fraction({w.numerator}, {w.denominator})" if isinstance(w, Fraction) else repr(w)


def _show_any(v):
    """_show for something that may not be an array of numbers (a fraction, a list of fractions, a dict…)."""
    if isinstance(v, Fraction):
        return _show_fraction(v)
    if isinstance(v, list) and v and any(isinstance(w, Fraction) for w in v):
        shown = ", ".join(_show_fraction(w) for w in v[:8])
        return f"[{shown}{', …' if len(v) > 8 else ''}] (list of {len(v)})"
    if isinstance(v, dict):
        items = list(v.items())
        shown = ", ".join(f"{_name(k) if isinstance(k, frozenset) else repr(k)}: {x!r}" for k, x in items[:6])
        return f"{{{shown}{', …' if len(items) > 6 else ''}}} (dict of {len(items)})"
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


def _gap(got, want, where=None):
    """Why got differs from want, in a few words: the largest gap, where it is (``where(k)`` names entry k), and the
    two values there."""
    try:
        g = np.asarray(got, dtype=float)
        w = np.asarray(want, dtype=float)
    except (TypeError, ValueError):
        return ""
    if g.shape != w.shape:
        return f" (shape {g.shape} instead of {w.shape})"
    if not np.all(np.isfinite(g)):
        bad = tuple(int(i) for i in np.argwhere(~np.isfinite(g))[0]) if g.ndim else ()
        place = (where(bad[0]) if where and len(bad) == 1 else bad if len(bad) != 1 else bad[0]) if bad else "it"
        return f" (the result holds nan or inf, first at {place})"
    if g.size:
        d = np.abs(g - w)
        k = np.unravel_index(int(np.argmax(d)), d.shape)
        place = (where(int(k[0])) if where and d.ndim == 1 else tuple(int(i) for i in k) if d.ndim > 1 else
                 int(k[0]) if d.ndim else "the single entry")
        return f" (largest gap {float(d[k]):.1e}, at {place}: expected {float(w[k]):.10g}, got {float(g[k]):.10g})"
    return ""


def _close(got, want, what, rtol=1e-12, atol=1e-14, hint="", where=None):
    if _same(got, want, rtol, atol):
        return
    hint = _text(hint)
    pytest.fail(f"expected {what} = {_show(want)}, got {_show_any(got)}{_gap(got, want, where)}"
                + (f" ({hint})" if hint else ""))


def _first_match(got, want, variants, rtol=1e-9, atol=1e-11):
    """The texts of the classic errors whose value got matches (and that differ from the right value), joined by
    « or » when several errors give the same value here; "" when none does."""
    texts = [text for value, text in variants
             if value is not None and not _same(value, want, rtol, atol) and _same(got, value, rtol, atol)]
    return " — or ".join(dict.fromkeys(texts))


def _rng(seed, case=None):
    """The generator of a test (seeds 7800 to 7890), one stream per case of a parametrized test."""
    return np.random.default_rng(seed if case is None else (seed, case))


def _python_float(got, what, hint):
    if type(got) is not float:
        pytest.fail(f"expected {what} as a Python float (float(...)), got {type(got).__module__}.{type(got).__name__} "
                    f"{_show_any(got)} ({hint})")


class _Overused(RuntimeError):
    """Raised by a characteristic function or a field called more times than the function can need."""


# --- what the module may use ----------------------------------------------------------------------------------------

def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``quad`` (from scipy.integrate import quad) → "scipy.integrate.quad". Relative imports
    (from .integrate import simpson) are your own modules."""
    names = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname:
                    names[alias.asname] = alias.name
                else:                                     # import scipy.stats binds the name scipy
                    names[alias.name.split(".")[0]] = alias.name.split(".")[0]
        elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
            for alias in node.names:
                names[alias.asname or alias.name] = f"{node.module}.{alias.name}"
    return names


def _where(statement):
    return statement.name if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)) else "the module level"


def _uses(tree, names):
    """Each use of an imported name (or of a chain of attributes on it): (where, dotted path), e.g.
    ("spearman_rho", "numpy.corrcoef"); ``where`` is the top-level function, or "the module level"."""
    inner = {id(node.value) for node in ast.walk(tree) if isinstance(node, ast.Attribute)}
    uses = []
    for statement in tree.body:
        where = _where(statement)
        for node in ast.walk(statement):
            if not isinstance(node, (ast.Name, ast.Attribute)) or id(node) in inner:
                continue                                  # only the whole chain numpy.ma.corrcoef
            attrs = []
            while isinstance(node, ast.Attribute):
                attrs.append(node.attr)
                node = node.value
            if isinstance(node, ast.Name) and node.id in names:
                uses.append((where, ".".join([names[node.id]] + attrs[::-1])))
    return uses


FORBIDDEN_MODULES = ("scipy", "statistics", "pandas", "sympy", "sklearn", "mpmath")
FORBIDDEN_NUMPY = {"corrcoef", "cov"}
FORBIDDEN_STRINGS = {"scipy", "statistics", "pandas", "corrcoef", "cov", "rankdata", "spearmanr", "pearsonr", "quad",
                     "correlation"}


def _string_uses(tree):
    """getattr(np, "corrcoef") and the like, and __import__("scipy") or importlib.import_module("scipy.stats"): a
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


def test_module_uses_numpy_math_fractions_and_itertools_but_no_scipy(attribution_module):
    """The docstring allows NumPy and the modules math, fractions and itertools (and your own modules, by relative
    imports: from .integrate import simpson), but no SciPy (scipy.stats.rankdata, spearmanr, pearsonr,
    scipy.integrate), neither np.corrcoef nor np.cov, nor the module statistics (statistics.correlation with
    method="ranked" is Spearman's ρ), nor pandas; nor SymPy, scikit-learn or mpmath, which would do the same work.
    Only the code counts: a comment, a docstring or an import never used is not a use."""
    try:
        tree = ast.parse(inspect.getsource(attribution_module))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = []
    for where, path in _uses(tree, _imported_names(tree)):
        parts = path.split(".")
        if parts[0] in FORBIDDEN_MODULES or (parts[0] == "numpy" and parts[-1] in FORBIDDEN_NUMPY):
            found.append(f"{path} in {where}")
    found += _string_uses(tree)
    assert not found, (f"expected NumPy, math, fractions and itertools only (and your own modules), with no SciPy, "
                       f"neither np.corrcoef nor np.cov, no statistics and no pandas, found {sorted(set(found))} (the "
                       f"tests compare your results with math.comb and fractions.Fraction, scipy.integrate.quad and "
                       f"scipy.stats.spearmanr: math.factorial, Fraction(a, b), itertools.combinations, np.argsort, "
                       f"np.sum and the formula of Pearson on the ranks (M02c) are enough)")


# --- coalition_weights ----------------------------------------------------------------------------------------------

CW_HINT = ("w[s] = s! (n - 1 - s)! / n! for s = 0, …, n - 1, the weight of ONE coalition of s players; with "
           "exact=True, a list of fractions.Fraction(a, b) built from integers (math.factorial or math.comb), with "
           "exact=False a numpy.ndarray of floats (float() of each fraction)")
CW_SECONDS = 10


def _exact_weights(n):
    """w[s] = 1 / (n C(n - 1, s)): in an order drawn uniformly, the number s of players before i is uniform on
    {0, …, n - 1}, and the set of these players is then one of C(n - 1, s) sets, all equally likely."""
    return [Fraction(1, n * math.comb(n - 1, s)) for s in range(n)]


def _cw_variants(n):
    """The weights of classic errors, with the reason."""
    f = math.factorial
    return [
        ([Fraction(1, math.comb(n - 1, s)) for s in range(n)],
         "the factor 1/n is missing: s! (n - 1 - s)! / (n - 1)! = 1 / C(n - 1, s), and these weights, counted "
         "C(n - 1, s) times each, add up to n instead of 1"),
        ([Fraction(1, n)] * n,
         "1/n is the weight of all the C(n - 1, s) coalitions of size s together: one coalition of size s weighs "
         "1 / (n C(n - 1, s))"),
        ([Fraction(f(s) * f(n - s), f(n)) for s in range(n)],
         "(n - s)! counts one player too many: besides i and the s players before it, n - 1 - s players come after"),
    ]


def _describe_cw(n, exact=None, positional=False):
    if exact is None:
        return f"coalition_weights({n!r})"
    return f"coalition_weights({n!r}, {exact!r})" if positional else f"coalition_weights({n!r}, exact={exact!r})"


def _cw(at, n, exact=None, positional=False, seconds=CW_SECONDS):
    """coalition_weights(n[, exact]), its type checked: a list of n fractions in lowest terms (exact=True), or a
    numpy.ndarray of n floats."""
    what = _describe_cw(n, exact, positional)
    if exact is None:
        call = lambda: at.coalition_weights(n)                                         # noqa: E731
    elif positional:
        call = lambda: at.coalition_weights(n, exact)                                  # noqa: E731
    else:
        call = lambda: at.coalition_weights(n, exact=exact)                            # noqa: E731
    size = int(n)
    hint = lambda: CW_HINT + _overflow_hint(size)                                      # noqa: E731
    if exact:
        got = _within(seconds, call, what, f"a list of {size} fractions.Fraction", hint)
        if not isinstance(got, list):
            pytest.fail(f"expected {what} as a list of {size} fractions.Fraction, got "
                        f"{type(got).__module__}.{type(got).__name__} {_show_any(got)} ({CW_HINT})")
        if len(got) != size:
            pytest.fail(f"expected {what} as a list of n = {size} fractions (s = 0, …, n - 1), got {len(got)} "
                        f"of them: {_show_any(got)} ({CW_HINT})")
        for s, w in enumerate(got):
            if not isinstance(w, Fraction):
                pytest.fail(f"expected {what} as a list of fractions.Fraction, got {type(w).__module__}."
                            f"{type(w).__name__} {w!r} at s = {s} ({CW_HINT})")
            if w.denominator <= 0 or math.gcd(w.numerator, w.denominator) != 1:
                pytest.fail(f"expected the fractions of {what} in lowest terms, got {w.numerator}/{w.denominator} at "
                            f"s = {s} ({CW_HINT})")
        return got
    got = _within(seconds, call, what, f"a numpy.ndarray of {size} floats", hint)
    if not (isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == (size,)):
        pytest.fail(f"expected {what} as a numpy.ndarray of n = {size} floats, got {type(got).__name__}"
                    + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray) else
                       f" {_show_any(got)}") + f" ({CW_HINT})")
    return got


def _overflow_hint(n):
    if n <= 170:
        return ""
    return (f"; here n = {n}: n! has {len(str(math.factorial(n)))} digits, far more than a float can hold (about "
            f"1.8e308, between 170! and 171!): keep the factorials as Python integers, divide exactly with "
            f"Fraction(a, b), and only then convert with float()")


def _check_exact_weights(got, want, what, n):
    if got == want:
        return
    wrong = [s for s in range(n) if got[s] != want[s]]
    s = wrong[0]
    text = next((text for value, text in _cw_variants(n) if value != want and value == got), "")
    pytest.fail(f"expected {what} = {_show_any(want)}, got {_show_any(got)} ({len(wrong)} of the {n} weights differ; "
                f"first at s = {s}: expected {_show_fraction(want[s])}, got {_show_fraction(got[s])}) "
                f"({'here ' + text + '; ' if text else ''}{CW_HINT})")


def _check_float_weights(got, want, what, n, rtol=1e-12):
    floats = np.array([float(w) for w in want])
    variants = [(np.array([float(w) for w in value]), text) for value, text in _cw_variants(n)]

    def hint():
        text = _first_match(got, floats, variants)
        return ("here " + text + "; " if text else "") + CW_HINT + _overflow_hint(n)

    _close(got, floats, what, rtol=rtol, atol=0.0, hint=hint, where=lambda s: f"s = {s}")


CW_NS = [5, 7, 1, 3, 4, 9, 11, 13, 14, 17, 23]


@pytest.mark.parametrize("n", CW_NS, ids=[f"n{n}" for n in CW_NS])
def test_coalition_weights_exact_are_the_fractions_of_math_comb(at, n):
    """exact=True: w[s] = s! (n - 1 - s)! / n! = 1 / (n C(n - 1, s)) (math.comb), exactly, as fractions.Fraction in
    lowest terms, s = 0, …, n - 1."""
    _check_exact_weights(_cw(at, n, True), _exact_weights(n), _describe_cw(n, True), n)


@pytest.mark.parametrize("n", CW_NS, ids=[f"n{n}" for n in CW_NS])
def test_coalition_weights_floats_are_the_fractions_converted(at, n):
    """exact=False: a numpy.ndarray of the n weights as floats, each the float of the exact fraction (up to 1e-12
    relative)."""
    _check_float_weights(_cw(at, n, False), _exact_weights(n), _describe_cw(n, False), n)


def test_coalition_weights_are_the_share_of_the_orders_in_which_exactly_s_come_first(at):
    """For each player i and each coalition S without i, the share of the n! orders (itertools.permutations) in which
    the players before i are exactly those of S is w[|S|]: s! ways to order S, (n - 1 - s)! for the players after i."""
    for n in (3, 4, 5, 7):
        w = _cw(at, n, True)
        orders = list(itertools.permutations(range(n)))
        for i in range(n):
            counts = Counter(frozenset(order[:order.index(i)]) for order in orders)
            assert len(counts) == 2 ** (n - 1)        # the oracle sees every coalition without i
            for S, c in sorted(counts.items(), key=lambda item: (len(item[0]), sorted(item[0]))):
                share = Fraction(c, len(orders))
                if w[len(S)] != share:
                    text = next((text for value, text in _cw_variants(n) if value[len(S)] == w[len(S)]), "")
                    pytest.fail(f"expected w[|S|] = w[{len(S)}] = {_show_fraction(share)} for coalition_weights({n}, "
                                f"exact=True): with i = {i} and S = {_name(S)}, {c} of the {len(orders)} orders put "
                                f"exactly the players of S before i; got {_show_fraction(w[len(S)])} "
                                f"({'here ' + text + '; ' if text else ''}{CW_HINT})")


def test_coalition_weights_times_the_number_of_coalitions_of_each_size_is_1_over_n(at):
    """The number of players before i is uniform on {0, …, n - 1}: C(n - 1, s) w[s] = 1/n for each s, so that
    Σ_s C(n - 1, s) w[s] = 1, exactly; in floats, up to 1e-12."""
    for n in (1, 3, 5, 9, 14, 23, 31):
        w = _cw(at, n, True)
        for s in range(n):
            mass = math.comb(n - 1, s) * w[s]
            assert mass == Fraction(1, n), (
                f"expected C({n - 1}, {s}) w[{s}] = 1/{n} for coalition_weights({n}, exact=True) (the number of "
                f"players before i is uniform on 0, …, {n - 1}), got {_show_fraction(mass)} with w[{s}] = "
                f"{_show_fraction(w[s])} ({CW_HINT})")
        floats = _cw(at, n, False)
        total = float(sum(math.comb(n - 1, s) * float(floats[s]) for s in range(n)))
        assert math.isclose(total, 1.0, rel_tol=1e-12), (
            f"expected Σ_s C({n - 1}, s) w[s] = 1 for coalition_weights({n}), got {total!r} ({CW_HINT})")


def test_coalition_weights_are_symmetric(at):
    """w[s] = w[n - 1 - s]: as many players before i as after it in the mirrored order; exactly for the fractions,
    up to 1e-13 for the floats."""
    for n in (3, 4, 9, 14, 17, 22, 37):
        w = _cw(at, n, True)
        for s in range(n):
            assert w[s] == w[n - 1 - s], (
                f"expected w[{s}] = w[{n - 1 - s}] for coalition_weights({n}, exact=True), got "
                f"{_show_fraction(w[s])} and {_show_fraction(w[n - 1 - s])} ({CW_HINT})")
        floats = _cw(at, n, False)
        _close(floats, floats[::-1], f"coalition_weights({n}) read backwards (w[s] = w[n - 1 - s])", rtol=1e-13,
               atol=0.0, hint=CW_HINT, where=lambda s: f"s = {s}")


def test_coalition_weights_of_one_player_are_1(at):
    """One player: nobody before, nobody after, w[0] = 0! 0! / 1! = 1, as [Fraction(1, 1)] or array([1.])."""
    got = _cw(at, 1, True)
    assert got == [Fraction(1)], f"expected coalition_weights(1, exact=True) = [Fraction(1, 1)], got {got!r}"
    _close(_cw(at, 1, False), np.array([1.0]), "coalition_weights(1, exact=False)", hint=CW_HINT)


def test_coalition_weights_default_is_floats_and_exact_may_be_given_by_position(at):
    """coalition_weights(n) is coalition_weights(n, exact=False), an array of floats; exact may be given by position
    or by keyword."""
    for n in (5, 13):
        want = _exact_weights(n)
        floats = np.array([float(w) for w in want])
        _close(_cw(at, n), floats, _describe_cw(n), atol=0.0, hint=CW_HINT, where=lambda s: f"s = {s}")
        _close(_cw(at, n, False, positional=True), floats, _describe_cw(n, False, True), atol=0.0, hint=CW_HINT,
               where=lambda s: f"s = {s}")
        _check_exact_weights(_cw(at, n, True, positional=True), want, _describe_cw(n, True, True), n)


NUMPY_NS = [np.int64(9), np.int32(5), np.uint8(13), np.int16(3)]


@pytest.mark.parametrize("n", NUMPY_NS, ids=["int64", "int32", "uint8", "int16"])
def test_coalition_weights_accepts_numpy_integers(at, n):
    want = _exact_weights(int(n))
    _check_exact_weights(_cw(at, n, True), want, _describe_cw(n, True) + " (a NumPy integer)", int(n))
    _check_float_weights(_cw(at, n, False), want, _describe_cw(n, False) + " (a NumPy integer)", int(n))


LARGE_NS = [97, 171, 263, 389]


@pytest.mark.parametrize("n", LARGE_NS, ids=[f"n{n}" for n in LARGE_NS])
def test_coalition_weights_of_many_players_are_exact_and_fast(at, n):
    """n in the hundreds: the factorials have hundreds of digits (more than a float can hold past 170!), Python
    integers and fractions keep them exact, and the floats are the fractions converted (up to 1e-12 relative)."""
    want = _exact_weights(n)
    _check_exact_weights(_cw(at, n, True), want, _describe_cw(n, True), n)
    _check_float_weights(_cw(at, n, False), want, _describe_cw(n, False), n)


BAD_CW = [((0,), {}, "n_players = 0: no player"), ((-3,), {}, "n_players is negative"),
          ((7.0,), {}, "n_players is the float 7.0, not an integer"),
          ((np.float64(9.0),), {}, "n_players is np.float64(9.0)"), ((4.5,), {}, "n_players is 4.5"),
          ((True,), {}, "n_players is True, a bool"), ((np.True_,), {}, "n_players is np.True_, a NumPy bool"),
          (("5",), {}, "n_players is a string"), ((None,), {}, "n_players is None"),
          ((5,), {"exact": 1}, "exact is the integer 1, not a bool"),
          ((5,), {"exact": 0}, "exact is the integer 0, not a bool"),
          ((5,), {"exact": "True"}, "exact is a string"), ((5,), {"exact": None}, "exact is None"),
          ((5,), {"exact": 1.0}, "exact is the float 1.0")]
BAD_CW_IDS = ["n0", "n-negative", "n-float", "n-numpy-float", "n-half", "n-bool", "n-numpy-bool", "n-string",
              "n-none", "exact-1", "exact-0", "exact-string", "exact-none", "exact-float"]


@pytest.mark.parametrize("args, kwargs, why", BAD_CW, ids=BAD_CW_IDS)
def test_coalition_weights_refusals(at, args, kwargs, why):
    shown = ", ".join([repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
    _expect_error(ValueError, lambda: at.coalition_weights(*args, **kwargs), f"coalition_weights({shown})", why)


# --- harsanyi_dividends ---------------------------------------------------------------------------------------------

HD_HINT = ("list the 2^n coalitions size by size (itertools.combinations(range(n), size)) and call v once on each "
           "of them; then, for each coalition T, d_T = Σ_{S ⊆ T} (-1)^(|T| - |S|) v(S), a sum over the 2^|T| subsets "
           "of T; return the dict {T: float(d_T)} with the coalitions in the same order, as frozensets")
HD_SECONDS = 30


def _name(coalition):
    """A coalition written for a message: ∅ or {0, 2}."""
    return "{" + ", ".join(str(int(i)) for i in sorted(coalition)) + "}" if coalition else "∅"


def _coalitions(n):
    """The 2^n coalitions by increasing size, and within a size in the order of itertools.combinations."""
    return [frozenset(c) for size in range(n + 1) for c in itertools.combinations(range(n), size)]


def _subsets(T, strict=False):
    members = sorted(T)
    return [frozenset(c) for size in range(len(members) + (0 if strict else 1))
            for c in itertools.combinations(members, size)]


class _NotACoalition(TypeError):
    """Raised by a characteristic function that receives something other than a frozenset of players."""


class _Game:
    """A characteristic function given by a table of worths: it counts its calls on each coalition, records what it
    receives, and fails at once past a budget of calls (a version that calls v again and again stops quickly)."""

    def __init__(self, worths, n, budget=None):
        self.worths, self.n = worths, n
        self.budget = 2 * 2 ** n + 8 if budget is None else budget
        self.calls, self.total = Counter(), 0
        self.overused, self.bad = False, None

    def __call__(self, S):
        self.total += 1
        if self.total > self.budget:
            self.overused = True
            raise _Overused(f"v was called more than {self.budget} times")
        if type(S) is not frozenset or not S <= frozenset(range(self.n)):
            if self.bad is None:
                self.bad = f"{type(S).__module__}.{type(S).__name__} {S!r}"
            raise _NotACoalition(f"v received {S!r}, not a frozenset of players of range({self.n})")
        self.calls[S] += 1
        return self.worths[S]


def _random_worths(rng, n, integers=False, scale=6.0):
    """A game whose worths are random: floats that are not dyadic, or integers; v(∅) is not 0."""
    coalitions = _coalitions(n)
    if integers:
        values = [int(x) for x in rng.integers(-36, 37, size=len(coalitions))]
    else:
        values = [float(x) for x in rng.uniform(-scale, scale, size=len(coalitions))]
    return dict(zip(coalitions, values))


def _game_failures(game, n, what):
    if game.overused:
        pytest.fail(f"expected v called once on each of the 2^{n} = {2 ** n} coalitions for {what}, got more than "
                    f"{game.budget} calls ({HD_HINT})")
    if game.bad is not None:
        pytest.fail(f"expected v to receive frozensets of players of range({n}) for {what}, got {game.bad} "
                    f"({HD_HINT})")


def _hd(at, worths, n, what, game=None, seconds=HD_SECONDS):
    """harsanyi_dividends(v, n) for the game of the table `worths`, its type checked: a dict with the 2^n coalitions
    as frozenset keys and Python floats as values. Returns (dividends, the game, to read its calls)."""
    game = game or _Game(worths, n)
    try:
        got = _within(seconds, lambda: at.harsanyi_dividends(game, n), what, "a dict {coalition: dividend}", HD_HINT)
    except BaseException:
        _game_failures(game, int(n), what)
        raise
    _game_failures(game, int(n), what)
    n = int(n)
    if not isinstance(got, dict):
        pytest.fail(f"expected {what} as a dict {{coalition: dividend}}, got {type(got).__module__}."
                    f"{type(got).__name__} {_show_any(got)} ({HD_HINT})")
    for key, value in got.items():
        if type(key) is not frozenset:
            pytest.fail(f"expected the keys of {what} as frozensets, got {type(key).__module__}.{type(key).__name__} "
                        f"{key!r} ({HD_HINT})")
    expected = set(_coalitions(n))
    missing = [T for T in _coalitions(n) if T not in got]
    extra = sorted((T for T in got if T not in expected), key=lambda T: (len(T), sorted(T)))
    if missing or extra:
        pytest.fail(f"expected the 2^{n} = {2 ** n} coalitions of range({n}) as the keys of {what}, got {len(got)} "
                    f"keys" + (f"; missing: {', '.join(_name(T) for T in missing[:5])}" if missing else "")
                    + (f"; not coalitions of range({n}): {', '.join(_name(T) for T in extra[:5])}" if extra else "")
                    + f" ({HD_HINT})")
    for T in _coalitions(n):
        if type(got[T]) is not float:
            pytest.fail(f"expected Python floats (float(...)) as the values of {what}, got "
                        f"{type(got[T]).__module__}.{type(got[T]).__name__} {got[T]!r} at T = {_name(T)} ({HD_HINT})")
    return got, game


def _exact_dividends(worths, n):
    """The dividends that rebuild the game, v(T) = Σ_{S ⊆ T} d_S, solved coalition after coalition (by increasing
    size) in fractions: d_T = v(T) - Σ_{S ⊊ T} d_S."""
    d = {}
    for T in _coalitions(n):
        d[T] = Fraction(worths[T]) - sum((d[S] for S in _subsets(T, strict=True)), Fraction(0))
    return d


def _hd_variants(worths, n, exact):
    """Dividends computed with a classic error, with the reason."""
    coalitions = _coalitions(n)
    zeta = {T: sum((Fraction(worths[S]) for S in _subsets(T)), Fraction(0)) for T in coalitions}
    parity = {T: exact[T] if len(T) % 2 == 0 else -exact[T] for T in coalitions}
    marginal = {T: Fraction(worths[T]) - (Fraction(worths[T - {max(T)}]) if T else 0) for T in coalitions}
    shares = {T: exact[T] / len(T) if T else exact[T] for T in coalitions}
    return [(zeta, "every v(S) is added: the sum over the subsets S of T takes the sign (-1)^(|T| - |S|)"),
            (parity, "the sign is (-1)^(|T| - |S|), not (-1)^|S|: here the dividends of the coalitions of an odd size "
                     "have the wrong sign"),
            (marginal, "v(T) - v(T without its last player) is a marginal contribution, not a dividend: a dividend "
                       "takes away what every smaller coalition inside T creates"),
            (shares, "the dividend d_T is not divided by |T|: d_T / |T| is the share of each member of T in the "
                     "Shapley value")]


def _tolerance(worths, n):
    """The rounding allowed on a dividend: alternating sums of up to 2^n worths."""
    scale = 1.0 + max(abs(float(x)) for x in worths.values())
    return max(1e-13, 4.0 ** n * 2.3e-16) * scale


def _check_dividends(got, want, what, n, worths, variants=()):
    """got (a dict of floats) against want (a dict of exact or float values), coalition by coalition."""
    atol = _tolerance(worths, n)
    wrong = [T for T in _coalitions(n) if not math.isclose(got[T], float(want[T]), rel_tol=1e-12, abs_tol=atol)]
    if not wrong:
        return
    T = wrong[0]
    text = ""
    for value, reason in variants:
        if any(not math.isclose(float(value[S]), float(want[S]), rel_tol=1e-12, abs_tol=atol) for S in wrong) and all(
                math.isclose(got[S], float(value[S]), rel_tol=1e-9, abs_tol=atol) for S in _coalitions(n)):
            text = reason
            break
    pytest.fail(f"expected the dividend of {_name(T)} in {what} to be {float(want[T]):.10g}, got {got[T]:.10g} "
                f"({len(wrong)} of the 2^{n} = {2 ** n} dividends differ"
                + (f", also at {', '.join(_name(S) for S in wrong[1:4])}{', …' if len(wrong) > 4 else ''}"
                   if len(wrong) > 1 else "") + ") (" + (f"here {text}; " if text else "") + HD_HINT + ")")


def _recognized(got, worths, n):
    """The classic error whose dividends got matches (for n ≤ 9), or ""."""
    if n > 9:
        return ""
    exact = _exact_dividends(worths, n)
    atol = _tolerance(worths, n)
    for value, reason in _hd_variants(worths, n, exact):
        if all(math.isclose(got[S], float(value[S]), rel_tol=1e-9, abs_tol=atol) for S in _coalitions(n)):
            return reason
    return ""


def _check_rebuild(got, worths, what, n):
    """Σ_{T ⊆ S} d_T = v(S) for every coalition S; the first S (by size) where it fails names the dividend that is
    wrong, the dividends of the smaller coalitions inside S being right."""
    atol = _tolerance(worths, n)
    for S in _coalitions(n):
        rebuilt = math.fsum(got[T] for T in _subsets(S))
        if not math.isclose(rebuilt, worths[S], rel_tol=1e-12, abs_tol=atol):
            should = worths[S] - math.fsum(got[T] for T in _subsets(S, strict=True))
            pytest.fail(f"expected the game rebuilt from the dividends of {what}, v(S) = Σ_{{T ⊆ S}} d_T, to be the "
                        f"game itself: at S = {_name(S)}, v(S) = {float(worths[S]):.10g}, rebuilt "
                        f"{rebuilt:.10g}; so d_{_name(S)} should be {should:.10g} (the smaller coalitions inside S "
                        f"being right), got {got[S]:.10g} ("
                        + (f"here {text}; " if (text := _recognized(got, worths, n)) else "") + HD_HINT + ")")


def _describe_game(kind, n):
    return f"harsanyi_dividends(v, {n!r}) for {kind}"


HD_NS = [1, 2, 3, 4, 5, 7, 9]


@pytest.mark.parametrize("n", HD_NS, ids=[f"n{n}" for n in HD_NS])
def test_harsanyi_dividends_rebuild_the_game(at, n):
    """v(S) = Σ_{T ⊆ S} d_T for every coalition S of a game with random worths (floats that are not dyadic, v(∅) not
    0): the worth of a coalition is the sum of the dividends of the coalitions it contains."""
    rng = _rng(7810, n)
    for _ in range(3):
        worths = _random_worths(rng, n)
        what = _describe_game("a game with random worths", n)
        got, _ = _hd(at, worths, n, what)
        _check_rebuild(got, worths, what, n)


HD_EXACT = [(2, False), (3, True), (5, False), (6, True), (7, False), (9, True)]


@pytest.mark.parametrize("n, integers", HD_EXACT, ids=[f"n{n}-{'ints' if i else 'floats'}" for n, i in HD_EXACT])
def test_harsanyi_dividends_match_the_dividends_solved_in_fractions(at, n, integers):
    """The dividends of the relation v(T) = Σ_{S ⊆ T} d_S solved coalition after coalition in fractions,
    d_T = v(T) - Σ_{S ⊊ T} d_S: equal for integer worths, up to rounding for floats; the coalitions that differ are
    named."""
    rng = _rng(7811, n)
    for _ in range(2):
        worths = _random_worths(rng, n, integers=integers)
        what = _describe_game(f"a game with random {'integer ' if integers else ''}worths", n)
        got, _ = _hd(at, worths, n, what)
        want = _exact_dividends(worths, n)
        _check_dividends(got, want, what, n, worths, _hd_variants(worths, n, want))


def _shapley_by_orders(worths, n):
    """φ_i: the mean over the n! orders (itertools.permutations) of v(the players before i, and i) - v(the players
    before i), in fractions."""
    phi = [Fraction(0)] * n
    orders = list(itertools.permutations(range(n)))
    for order in orders:
        before = frozenset()
        for i in order:
            after = before | {i}
            phi[i] += Fraction(worths[after]) - Fraction(worths[before])
            before = after
    return [p / len(orders) for p in phi]


def test_harsanyi_dividends_give_the_shapley_value_averaged_over_the_orders(at):
    """φ_i = Σ_{T ∋ i} d_T / |T| (each dividend shared equally among the members of its coalition) is the mean of the
    marginal contributions of i over the n! orders of itertools.permutations, for every player."""
    rng = _rng(7812)
    for n in (2, 3, 5, 6):
        worths = _random_worths(rng, n)
        what = _describe_game("a game with random worths", n)
        got, _ = _hd(at, worths, n, what)
        want = [float(p) for p in _shapley_by_orders(worths, n)]
        phi = np.array([math.fsum(got[T] / len(T) for T in got if i in T) for i in range(n)])
        _close(phi, np.array(want), f"Σ_{{T ∋ i}} d_T / |T| with the dividends of {what} (the Shapley value of the "
                                    f"{math.factorial(n)} orders)", rtol=1e-10, atol=_tolerance(worths, n),
               hint=HD_HINT, where=lambda i: f"player {i}")


def test_harsanyi_dividends_of_unanimity_games_sit_on_their_coalition(at):
    """c u_T (worth c for the coalitions that contain T, 0 for the others): d_T = c and every other dividend is 0,
    for coalitions T of any size, the empty one included (a constant game)."""
    rng = _rng(7813)
    for n in (1, 3, 5, 7):
        for size in sorted({0, 1, n // 2, n}):
            T = frozenset(int(i) for i in rng.choice(n, size=size, replace=False))
            c = float(rng.uniform(0.6, 4.4)) * float(rng.choice([-1.0, 1.0]))
            worths = {S: (c if T <= S else 0.0) for S in _coalitions(n)}
            what = _describe_game(f"{c:.6g} times the unanimity game of {_name(T)}", n)
            got, _ = _hd(at, worths, n, what)
            want = {S: (c if S == T else 0.0) for S in _coalitions(n)}
            _check_dividends(got, want, what, n, worths)


def test_harsanyi_dividends_of_an_additive_game(at):
    """v(S) = c + Σ_{j ∈ S} a_j: d_∅ = c, d_{j} = a_j, and the dividends of the coalitions of two players or more
    are 0 (nothing is created together)."""
    rng = _rng(7814)
    for n in (2, 3, 6, 7):
        c = float(rng.uniform(-3.0, 3.0))
        a = rng.uniform(-2.6, 2.6, size=n)
        worths = {S: c + math.fsum(float(a[j]) for j in S) for S in _coalitions(n)}
        what = _describe_game(f"the additive game c + Σ a_j, c = {c:.6g}, a = {_show(a)}", n)
        got, _ = _hd(at, worths, n, what)
        want = {S: (c if not S else float(a[next(iter(S))]) if len(S) == 1 else 0.0) for S in _coalitions(n)}
        _check_dividends(got, want, what, n, worths)


def test_harsanyi_dividends_are_linear_in_the_game(at):
    """The dividends of λ v + μ w are λ times those of v plus μ times those of w."""
    rng = _rng(7815)
    for n in (2, 5, 7):
        v, w = _random_worths(rng, n), _random_worths(rng, n)
        lam, mu = float(rng.uniform(0.3, 2.7)), float(rng.uniform(-2.2, -0.4))
        mix = {S: lam * v[S] + mu * w[S] for S in _coalitions(n)}
        dv, _ = _hd(at, v, n, _describe_game("a game v", n))
        dw, _ = _hd(at, w, n, _describe_game("a game w", n))
        what = _describe_game(f"λ v + μ w, λ = {lam:.6g}, μ = {mu:.6g}", n)
        got, _ = _hd(at, mix, n, what)
        want = {S: lam * dv[S] + mu * dw[S] for S in _coalitions(n)}
        _check_dividends(got, want, what + " (λ times the dividends of v plus μ times those of w)", n, mix)


def test_harsanyi_dividends_of_the_empty_coalition_and_of_one_player(at):
    """d_∅ = v(∅), which need not be 0, and d_{i} = v({i}) - v(∅); adding a constant to every worth changes d_∅ only."""
    rng = _rng(7816)
    for n in (1, 3, 6):
        worths = _random_worths(rng, n)
        worths[frozenset()] = float(rng.uniform(2.1, 5.3))
        what = _describe_game(f"a game with v(∅) = {worths[frozenset()]:.6g}", n)
        got, _ = _hd(at, worths, n, what)
        for T in _coalitions(n)[:n + 1]:
            want = worths[T] - (worths[frozenset()] if T else 0.0)
            assert math.isclose(got[T], want, rel_tol=1e-12, abs_tol=1e-13), (
                f"expected d_{_name(T)} = {'v(∅)' if not T else f'v({_name(T)}) - v(∅)'} = {want:.10g} for {what}, "
                f"got {got[T]:.10g} ({HD_HINT})")
        shift = float(rng.uniform(-3.7, -1.3))
        moved = {S: x + shift for S, x in worths.items()}
        shifted, _ = _hd(at, moved, n, what + f" plus {shift:.6g} on every worth")
        want = {S: got[S] + (shift if not S else 0.0) for S in _coalitions(n)}
        _check_dividends(shifted, want, what + f" plus {shift:.6g} on every worth (only d_∅ moves)", n, moved)


ORDER_NS = [1, 2, 5, 6]


@pytest.mark.parametrize("n", ORDER_NS, ids=[f"n{n}" for n in ORDER_NS])
def test_harsanyi_dividends_list_the_coalitions_by_size_in_the_order_of_combinations(at, n):
    """The keys come by increasing size, and within a size in the order of itertools.combinations(range(n), size)."""
    worths = _random_worths(_rng(7817, n), n)
    what = _describe_game("a game with random worths", n)
    got, _ = _hd(at, worths, n, what)
    keys, want = list(got), _coalitions(n)
    if keys != want:
        k = next(j for j, (a, b) in enumerate(zip(keys, want)) if a != b)
        pytest.fail(f"expected the keys of {what} by increasing size, then in the order of itertools.combinations: "
                    f"position {k} should hold {_name(want[k])}, got {_name(keys[k])} (the keys begin with "
                    f"{', '.join(_name(T) for T in keys[:k + 2])}) ({HD_HINT})")


def test_harsanyi_dividends_call_v_once_on_each_coalition_a_frozenset(at):
    """v is called exactly 2^n times, once on each coalition, and always on a frozenset of players of range(n)."""
    rng = _rng(7818)
    for n in (1, 2, 5, 9):
        worths = _random_worths(rng, n)
        game = _Game(worths, n)
        what = _describe_game("a game that counts its calls", n)
        _hd(at, worths, n, what, game=game)
        twice = [S for S in _coalitions(n) if game.calls[S] > 1]
        never = [S for S in _coalitions(n) if game.calls[S] == 0]
        if game.total != 2 ** n or twice or never:
            pytest.fail(f"expected v called once on each of the 2^{n} = {2 ** n} coalitions for {what}, got "
                        f"{game.total} calls" + (f"; several calls on {', '.join(_name(S) for S in twice[:4])}"
                                                 if twice else "")
                        + (f"; never on {', '.join(_name(S) for S in never[:4])}" if never else "") + f" ({HD_HINT})")


def test_harsanyi_dividends_of_a_table_of_worths(at):
    """A table t of worths keyed by frozensets, passed as lambda S: t[S] (the convention of the module): the table is
    left unchanged."""
    rng = _rng(7819)
    for n in (3, 6):
        t = _random_worths(rng, n)
        copy = dict(t)
        what = _describe_game("lambda S: t[S], t a table of worths", n)
        got = _within(HD_SECONDS, lambda: at.harsanyi_dividends(lambda S: t[S], n), what,
                      "a dict {coalition: dividend}", HD_HINT)
        assert t == copy, f"expected the table t unchanged by {what}"
        assert isinstance(got, dict) and set(got) == set(_coalitions(n)), (
            f"expected {what} as a dict over the {2 ** n} coalitions, got {_show_any(got)} ({HD_HINT})")
        _check_dividends(got, _exact_dividends(t, n), what, n, t)


WORTH_KINDS = [(int, "Python ints"), (np.int64, "NumPy int64"), (np.float32, "NumPy float32"),
               (np.float64, "NumPy float64")]


@pytest.mark.parametrize("kind, text", WORTH_KINDS, ids=["int", "int64", "float32", "float64"])
def test_harsanyi_dividends_accept_integer_and_numpy_worths_and_return_python_floats(at, kind, text):
    """Worths given as Python ints or NumPy numbers are finite real numbers; the dividends are Python floats."""
    n = 5
    integers = _random_worths(_rng(7820, [k for k, _ in WORTH_KINDS].index(kind)), n, integers=True)
    worths = {S: kind(x) for S, x in integers.items()}
    what = _describe_game(f"worths given as {text}", n)
    got, _ = _hd(at, worths, n, what)
    _check_dividends(got, _exact_dividends(integers, n), what, n, integers)


HD_NUMPY_NS = [np.int64(5), np.int32(3), np.uint8(6), np.int16(2)]


@pytest.mark.parametrize("n", HD_NUMPY_NS, ids=["int64", "int32", "uint8", "int16"])
def test_harsanyi_dividends_accept_numpy_integers_for_n_players(at, n):
    m = int(n)
    worths = _random_worths(_rng(7821, m), m)
    what = _describe_game(f"a game with random worths (n_players a {type(n).__name__})", n)
    got, _ = _hd(at, worths, n, what)
    _check_dividends(got, _exact_dividends(worths, m), what, m, worths)


def test_harsanyi_dividends_of_eleven_and_thirteen_players(at):
    """2^11 and 2^13 coalitions: the game is rebuilt from the dividends, within a few seconds, with v called once on
    each coalition."""
    rng = _rng(7822)
    for n in (11, 13):
        worths = _random_worths(rng, n)
        game = _Game(worths, n, budget=2 ** n)
        what = _describe_game("a game with random worths", n)
        got, _ = _hd(at, worths, n, what, game=game, seconds=60)
        _check_rebuild(got, worths, what, n)


BAD_HD = [((0,), "n_players = 0: no player"), ((-2,), "n_players is negative"),
          ((5.0,), "n_players is the float 5.0, not an integer"), ((np.float64(3.0),), "n_players is np.float64(3.0)"),
          ((4.5,), "n_players is 4.5"), ((True,), "n_players is True, a bool"),
          ((np.True_,), "n_players is np.True_, a NumPy bool"), (("3",), "n_players is a string"),
          ((None,), "n_players is None")]


@pytest.mark.parametrize("args, why", BAD_HD, ids=["n0", "n-negative", "n-float", "n-numpy-float", "n-half", "n-bool",
                                                   "n-numpy-bool", "n-string", "n-none"])
def test_harsanyi_dividends_refuse_a_bad_number_of_players(at, args, why):
    worths = _random_worths(_rng(7823), 3)
    _expect_error(ValueError, lambda: at.harsanyi_dividends(lambda S: worths.get(S, 0.0), *args),
                  f"harsanyi_dividends(v, {args[0]!r})", why)


NOT_CALLABLE = [("a dict of worths", "table"), ("None", None), ("a number", 2.75), ("a list", [0.5, 1.5])]


@pytest.mark.parametrize("text, v", NOT_CALLABLE, ids=["dict", "none", "number", "list"])
def test_harsanyi_dividends_refuse_a_v_that_is_not_callable(at, text, v):
    """v must be called: a table is passed as lambda S: t[S], not as the dict itself."""
    if v == "table":
        v = _random_worths(_rng(7824), 3)
    _expect_error(ValueError, lambda: at.harsanyi_dividends(v, 3), f"harsanyi_dividends({text}, 3)",
                  "v must be a callable (a table t is passed as lambda S: t[S])")


BAD_WORTHS = [(math.nan, "nan"), (math.inf, "inf"), (-math.inf, "-inf"), (True, "True, a bool"),
              (np.False_, "np.False_, a NumPy bool"), ("3.25", "the string '3.25'"), (None, "None"), (1j, "a complex"),
              ([1.25], "a list [1.25]")]


@pytest.mark.parametrize("bad, text", BAD_WORTHS, ids=["nan", "inf", "minus-inf", "bool", "numpy-bool", "string",
                                                       "none", "complex", "list"])
def test_harsanyi_dividends_refuse_a_worth_that_is_not_a_finite_real_number(at, bad, text):
    """Every worth is checked: a bad one at a coalition of two players (not only at the first coalition) is refused."""
    n = 4
    worths = _random_worths(_rng(7825), n)
    target = frozenset({1, 3})
    worths[target] = bad
    _expect_error(ValueError, lambda: at.harsanyi_dividends(_Game(worths, n), n),
                  f"harsanyi_dividends(v, {n}) with v({_name(target)}) = {text}",
                  "every worth must be a finite real number, and a bool is refused")


# --- line_integral --------------------------------------------------------------------------------------------------

LI_HINT = ("on each segment from a to b: h = 1 / n_sub and the n_sub + 1 points a + k h (b - a), k = 0, …, n_sub, "
           "each a new 1-D float array of length d given to the field alone; g_k = F(point) · (b - a); Simpson's "
           "(h / 3) (g_0 + 4 g_1 + 2 g_2 + 4 g_3 + … + 2 g_{n_sub - 2} + 4 g_{n_sub - 1} + g_{n_sub}); the sum over "
           "the segments, as a Python float")
LI_SECONDS = 30
DEFAULT_N_SUB = 20          # the default of the signature


class _NotOnePoint(RuntimeError):
    """Raised by a field that receives something other than one point (a 1-D float array of length d)."""


class _Field:
    """A field p ↦ F(p) that counts its calls, records the points it receives if asked, refuses anything other than
    one point (a 1-D float numpy.ndarray of length d: never a batch of points), and fails at once past a budget of
    calls. With mutate=True, it writes into the point it received after reading it; with watch, it notes a point that
    shares its memory with the array of the vertices given to line_integral."""

    def __init__(self, function, d, budget, mutate=False, keep=False, watch=None):
        self.function, self.d, self.budget = function, d, budget
        self.mutate, self.watch = mutate, watch
        self.calls, self.overused, self.wrong, self.shared = 0, False, None, False
        self.received = [] if keep else None

    def __call__(self, p):
        self.calls += 1
        if self.calls > self.budget:
            self.overused = True
            raise _Overused(f"the field was called more than {self.budget} times")
        if not (isinstance(p, np.ndarray) and p.shape == (self.d,) and p.dtype.kind == "f"):
            if self.wrong is None:
                if isinstance(p, np.ndarray):
                    self.wrong = (f"a numpy.ndarray of shape {p.shape} and dtype {p.dtype}"
                                  + (" (a batch of points)" if p.ndim > 1 else ""))
                else:
                    self.wrong = f"{type(p).__module__}.{type(p).__name__} {p!r}"
            raise _NotOnePoint(f"the field received {self.wrong}, not one point of shape ({self.d},)")
        if self.watch is not None and np.shares_memory(p, self.watch):
            self.shared = True
        if self.received is not None:
            self.received.append(p.copy())
        value = self.function(p.copy())
        if self.mutate and p.flags.writeable:
            p *= -3.7                                     # written into after reading: must change nothing
            p += 11.3
        return value


def _field_failures(field, what, needed):
    if field.overused:
        pytest.fail(f"expected about (k - 1)(n_sub + 1) = {needed} evaluations of the field for {what} (n_sub + 1 per "
                    f"segment), got more than {field.budget} ({LI_HINT})")
    if field.wrong is not None:
        pytest.fail(f"expected the field to be called on one point at a time, a 1-D float numpy.ndarray of shape "
                    f"({field.d},), for {what}, got {field.wrong} ({LI_HINT})")


def _describe_li(name, points, n_sub=None, positional=False):
    P = np.asarray(points, dtype=float)
    shown = _show(P) if P.size <= 12 else f"{P.shape[0]} vertices in dimension {P.shape[1]}"
    tail = "" if n_sub is None else (f", {n_sub!r}" if positional else f", n_sub={n_sub!r}")
    return f"line_integral(F, {shown}{tail}) with F = {name}"


def _li(module, function, name, points, n_sub=None, what=None, positional=False, budget=None, mutate=False,
        keep=False, watch=None, seconds=LI_SECONDS):
    """line_integral(F, points[, n_sub]) on the field function(p), its type checked: a Python float. Returns (the
    value, the field, to read its calls)."""
    P = np.asarray(points, dtype=float)
    k, d = P.shape
    n_eff = DEFAULT_N_SUB if n_sub is None else int(n_sub)
    needed = (k - 1) * (n_eff + 1)
    field = _Field(function, d, 2 * needed + 10 if budget is None else budget, mutate, keep, watch)
    what = what or _describe_li(name, points, n_sub, positional)
    if n_sub is None:
        call = lambda: module.line_integral(field, points)                             # noqa: E731
    elif positional:
        call = lambda: module.line_integral(field, points, n_sub)                      # noqa: E731
    else:
        call = lambda: module.line_integral(field, points, n_sub=n_sub)                # noqa: E731
    try:
        got = _within(seconds, call, what, "a Python float", LI_HINT)
    except BaseException:
        _field_failures(field, what, needed)
        raise
    _field_failures(field, what, needed)
    _python_float(got, what, LI_HINT)
    return got, field


# fields of the tests: smooth or polynomial, with random coefficients (no example of the docstring)

def _smooth_field(rng, d, terms=3, freq=0.9):
    """F(p) = Σ_m c_m sin(ω_m · p + φ_m) w_m: a smooth field that is not a gradient (w_m not along ω_m)."""
    W = rng.uniform(-1.2, 1.2, size=(terms, d))
    om = rng.uniform(-freq, freq, size=(terms, d))
    ph = rng.uniform(0.0, 2 * math.pi, size=terms)
    c = rng.uniform(0.5, 1.5, size=terms)
    return (lambda p: (c * np.sin(om @ np.asarray(p, dtype=float) + ph)) @ W), "a smooth field of sines"


def _smooth_potential(rng, d, terms=3, freq=0.9):
    """f(p) = Σ_m c_m sin(ω_m · p + φ_m) + κ exp(ν · p) and its gradient."""
    om = rng.uniform(-freq, freq, size=(terms, d))
    ph = rng.uniform(0.0, 2 * math.pi, size=terms)
    c = rng.uniform(-1.5, 1.5, size=terms)
    nu = rng.uniform(-0.4, 0.4, size=d)
    kappa = float(rng.uniform(0.4, 1.3))

    def f(p):
        p = np.asarray(p, dtype=float)
        return float(c @ np.sin(om @ p + ph) + kappa * math.exp(float(nu @ p)))

    def grad(p):
        p = np.asarray(p, dtype=float)
        return (c * np.cos(om @ p + ph)) @ om + kappa * math.exp(float(nu @ p)) * nu

    return f, grad, "the gradient of a smooth f (sines and an exponential)"


def _ridges(rng, d, degrees):
    """(u_m, s_m, k_m): the terms (u_m · p + s_m)^k_m of a polynomial of total degree max(k_m)."""
    return [(rng.uniform(-1.1, 1.1, size=d), float(rng.uniform(-0.9, 0.9)), k) for k in degrees]


def _polynomial_field(rng, d, degrees=(3, 3, 1, 0)):
    """F(p) = Σ_m (u_m · p + s_m)^k_m w_m: a field whose coordinates are polynomials of total degree max(k_m), not a
    gradient."""
    terms = _ridges(rng, d, degrees)
    W = rng.uniform(-1.3, 1.3, size=(len(terms), d))

    def F(p):
        p = np.asarray(p, dtype=float)
        return sum(((u @ p + s) ** k) * w for (u, s, k), w in zip(terms, W))

    return F, terms, W, f"a polynomial field of degree {max(degrees)}"


def _polynomial_potential(rng, d, degrees=(4, 3, 3, 1)):
    """f(p) = Σ_m c_m (u_m · p + s_m)^k_m (degree at most 4: along a segment, the integrand is of degree at most 3)
    and its gradient."""
    terms = _ridges(rng, d, degrees)
    c = rng.uniform(-1.4, 1.4, size=len(terms))

    def f(p):
        p = np.asarray(p, dtype=float)
        return float(sum(cm * (u @ p + s) ** k for cm, (u, s, k) in zip(c, terms)))

    def grad(p):
        p = np.asarray(p, dtype=float)
        return sum(cm * k * (u @ p + s) ** (k - 1) * u for cm, (u, s, k) in zip(c, terms) if k > 0)

    return f, grad, f"the gradient of a polynomial f of degree {max(degrees)}"


def _polyline(rng, k, d, spread=1.3):
    """k random vertices in dimension d (floats that are not dyadic)."""
    return rng.uniform(-spread, spread, size=(k, d))


def _quad_segment(function, a, b):
    """∫_0^1 F(a + t (b - a)) · (b - a) dt by scipy.integrate.quad."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    chord = b - a
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", integrate.IntegrationWarning)    # « roundoff detected » on polynomials
        value, _ = integrate.quad(lambda t: float(np.dot(np.asarray(function(a + t * chord), dtype=float), chord)),
                                  0.0, 1.0, epsabs=1e-14, epsrel=1e-13, limit=320)
    return value


def _quad_path(function, points):
    P = np.asarray(points, dtype=float)
    return [_quad_segment(function, a, b) for a, b in zip(P[:-1], P[1:])]


def _check_segments(module, function, name, points, n_sub, rtol, atol, what_tail=""):
    """Each segment alone against scipy.integrate.quad (the segment that differs is named), then the whole path
    against the sum of its segments."""
    P = np.asarray(points, dtype=float)
    want = _quad_path(function, P)
    values = []
    for j, (a, b) in enumerate(zip(P[:-1], P[1:])):
        got, _ = _li(module, function, name, np.array([a, b]), n_sub)
        if not math.isclose(got, want[j], rel_tol=rtol, abs_tol=atol):
            pytest.fail(f"expected {_describe_li(name, P, n_sub)}{what_tail} to integrate segment {j} (from "
                        f"{_show(a)} to {_show(b)}) as scipy.integrate.quad does, {want[j]:.12g}, got {got:.12g} "
                        f"alone (gap {abs(got - want[j]):.1e}) ({LI_HINT})")
        values.append(got)
    got, _ = _li(module, function, name, P, n_sub)
    total = math.fsum(values)
    if not math.isclose(got, total, rel_tol=1e-12, abs_tol=1e-13 * (1 + math.fsum(abs(x) for x in values))):
        pytest.fail(f"expected {_describe_li(name, P, n_sub)}{what_tail} to be the sum of its {len(values)} segments "
                    f"integrated one by one, {total:.12g}, got {got:.12g} ({LI_HINT})")
    return got


QUAD_CASES = [(1, 3), (2, 2), (2, 4), (3, 5), (5, 3)]


@pytest.mark.parametrize("d, k", QUAD_CASES, ids=[f"d{d}-k{k}" for d, k in QUAD_CASES])
def test_line_integral_matches_quad_on_each_segment(at, d, k):
    """A smooth field that is not a gradient, along k random vertices in dimension d, with n_sub = 236: each segment
    agrees with scipy.integrate.quad (up to Simpson's error, below 1e-9 here), and the path is the sum of its
    segments."""
    rng = _rng(7830, d * 10 + k)
    for _ in range(2):
        function, name = _smooth_field(rng, d)
        _check_segments(at, function, name, _polyline(rng, k, d), 236, rtol=1e-9, atol=1e-10)


EXACT_CASES = [(1, 2), (2, 2), (2, 4), (3, 14), (4, 2), (2, 8)]


@pytest.mark.parametrize("d, n_sub", EXACT_CASES, ids=[f"d{d}-n{n}" for d, n in EXACT_CASES])
def test_line_integral_is_exact_for_fields_of_degree_at_most_3(at, d, n_sub):
    """Fields whose coordinates are polynomials of total degree at most 3 (not gradients): along each segment the
    integrand t ↦ g(t) is a polynomial of degree at most 3, and Simpson's rule is exact, even with n_sub = 2."""
    rng = _rng(7831, d * 100 + n_sub)
    for k in (2, 3, 6):
        function, _, _, name = _polynomial_field(rng, d)
        _check_segments(at, function, name, _polyline(rng, k, d), n_sub, rtol=1e-11, atol=1e-11)


def _fourth_derivative(terms, W, a, b):
    """g''''(t), constant along the segment from a to b when g(t) = Σ_m (u_m · (a + t (b - a)) + s_m)^4 w_m · (b - a)
    is of degree 4: Σ_m 24 (u_m · (b - a))^4 (w_m · (b - a)) (the terms of a smaller degree give 0)."""
    chord = np.asarray(b, dtype=float) - np.asarray(a, dtype=float)
    return math.fsum(24.0 * float(u @ chord) ** 4 * float(w @ chord) for (u, _, k), w in zip(terms, W) if k == 4)


QUARTIC_CASES = [(1, 2), (2, 2), (2, 4), (3, 8), (2, 12), (4, 26)]


@pytest.mark.parametrize("d, n_sub", QUARTIC_CASES, ids=[f"d{d}-n{n}" for d, n in QUARTIC_CASES])
def test_line_integral_of_a_quartic_integrand_is_off_by_exactly_g4_over_180_n_sub_4(at, d, n_sub):
    """A field of degree 4: along each segment the integrand g is of degree 4, g'''' is a constant, and Simpson's rule
    with n_sub intervals gives the exact integral (scipy.integrate.quad) plus exactly g''''/(180 n_sub⁴). This is the
    value of Simpson's rule with n_sub intervals, neither 2 n_sub nor the exact integral."""
    rng = _rng(7832, d * 100 + n_sub)
    for k in (2, 3, 5):
        function, terms, W, name = _polynomial_field(rng, d, degrees=(4, 4, 3, 0))
        P = _polyline(rng, k, d)
        for j, (a, b) in enumerate(zip(P[:-1], P[1:])):
            exact = _quad_segment(function, a, b)
            g4 = _fourth_derivative(terms, W, a, b)
            want = exact + g4 / (180.0 * n_sub ** 4)
            got, _ = _li(at, function, name, np.array([a, b]), n_sub)
            scale = abs(exact) + abs(g4) / 180.0 + 1.0
            if not math.isclose(got, want, rel_tol=1e-11, abs_tol=1e-12 * scale):
                variants = [(exact, "this is the exact integral: Simpson's rule with n_sub intervals is off by "
                                    "g''''/(180 n_sub⁴) for an integrand of degree 4"),
                            (exact + g4 / (180.0 * (2 * n_sub) ** 4),
                             "this is Simpson's rule with 2 n_sub intervals: n_sub counts the intervals of width "
                             "h = 1 / n_sub, two per parabola")]
                text = next((t for value, t in variants
                             if math.isclose(got, value, rel_tol=1e-10, abs_tol=1e-11 * scale)), "")
                pytest.fail(f"expected {_describe_li(name, np.array([a, b]), n_sub)} (segment {j} of a path) = the "
                            f"exact integral {exact:.12g} + g''''/(180 n_sub⁴) = {exact:.12g} + {g4:.6g} / (180 × "
                            f"{n_sub}⁴) = {want:.12g}, got {got:.12g} ("
                            + (f"here {text}; " if text else "") + LI_HINT + ")")
        whole = math.fsum(_quad_segment(function, a, b) + _fourth_derivative(terms, W, a, b) / (180.0 * n_sub ** 4)
                          for a, b in zip(P[:-1], P[1:]))
        got, _ = _li(at, function, name, P, n_sub)
        if not math.isclose(got, whole, rel_tol=1e-11, abs_tol=1e-11):
            pytest.fail(f"expected {_describe_li(name, P, n_sub)} = Σ over the segments of (exact integral + "
                        f"g''''/(180 n_sub⁴)) = {whole:.12g}, got {got:.12g} ({LI_HINT})")


ORDER_CASES = [(1, 1.6), (2, 1.3), (3, 1.0)]


ORDER_N_SUBS = (26, 36, 46, 58, 74)


@pytest.mark.parametrize("d, freq", ORDER_CASES, ids=[f"d{d}" for d, _ in ORDER_CASES])
def test_line_integral_error_decreases_like_1_over_n_sub_to_the_4th(at, d, freq):
    """A smooth field along a path of three segments: against scipy.integrate.quad, the error for n_sub = 26, 36, 46,
    58 and 74 is C / n_sub⁴ with the same C (error × n_sub⁴ within ±2 % of its mean): doubling n_sub divides it by
    about 2⁴ = 16."""
    rng = _rng(7833, d)
    function, name = _smooth_field(rng, d, freq=freq)
    P = _polyline(rng, 4, d, spread=1.6)
    exact = math.fsum(_quad_path(function, P))
    errors = []
    for n_sub in ORDER_N_SUBS:
        got, _ = _li(at, function, name, P, n_sub)
        errors.append(abs(got - exact))
    scaled = [e * n ** 4 for e, n in zip(errors, ORDER_N_SUBS)]
    mean = sum(scaled) / len(scaled)
    if not all(abs(c - mean) <= 0.02 * mean for c in scaled):
        pytest.fail(f"expected the error of {_describe_li(name, P)} with n_sub = "
                    f"{', '.join(map(str, ORDER_N_SUBS))} to be C / n_sub⁴ with the same C (an error of order "
                    f"1 / n_sub⁴), got errors {[f'{e:.3e}' for e in errors]}, that is error × n_sub⁴ = "
                    f"{[f'{c:.4g}' for c in scaled]}, against scipy.integrate.quad ({LI_HINT})")


GRADIENT_CASES = [(1, 3), (2, 2), (2, 5), (3, 4), (5, 3)]


@pytest.mark.parametrize("d, k", GRADIENT_CASES, ids=[f"d{d}-k{k}" for d, k in GRADIENT_CASES])
def test_line_integral_of_a_gradient_field_is_the_change_of_f(at, d, k):
    """The gradient theorem: along any path, the integral of ∇f is f(last point) - f(first point); exactly for a
    polynomial f of degree at most 4 (the integrand is of degree at most 3), with any n_sub; up to 1e-9 for a smooth
    f with n_sub = 236."""
    rng = _rng(7834, d * 10 + k)
    for n_sub in (2, 4, 16):
        f, grad, name = _polynomial_potential(rng, d)
        P = _polyline(rng, k, d)
        got, _ = _li(at, grad, name, P, n_sub)
        want = f(P[-1]) - f(P[0])
        scale = 1.0 + max(abs(f(p)) for p in P)
        assert math.isclose(got, want, rel_tol=1e-11, abs_tol=1e-11 * scale), (
            f"expected {_describe_li(name, P, n_sub)} = f(last point) - f(first point) = {want:.12g} (the gradient "
            f"theorem; Simpson's rule is exact here), got {got:.12g} ({LI_HINT})")
    f, grad, name = _smooth_potential(rng, d)
    P = _polyline(rng, k, d)
    got, _ = _li(at, grad, name, P, 236)
    want = f(P[-1]) - f(P[0])
    assert math.isclose(got, want, rel_tol=1e-9, abs_tol=1e-9), (
        f"expected {_describe_li(name, P, 236)} = f(last point) - f(first point) = {want:.12g} (the gradient theorem), "
        f"got {got:.12g} ({LI_HINT})")


def test_line_integral_of_a_gradient_field_does_not_depend_on_the_path(at):
    """Three paths with the same ends (a segment, a path in two segments, a path in five): the same value for a
    gradient field (exactly for a polynomial f of degree at most 4)."""
    rng = _rng(7835)
    for d in (2, 3):
        f, grad, name = _polynomial_potential(rng, d)
        start, end = _polyline(rng, 2, d)
        paths = [np.array([start, end]), np.array([start, _polyline(rng, 1, d)[0], end]),
                 np.vstack([start, _polyline(rng, 4, d), end])]
        values = [_li(at, grad, name, P, 14)[0] for P in paths]
        want = f(end) - f(start)
        for P, got in zip(paths, values):
            assert math.isclose(got, want, rel_tol=1e-11, abs_tol=1e-11), (
                f"expected {_describe_li(name, P, 14)} = {want:.12g}, the same along every path from {_show(start)} "
                f"to {_show(end)} (a gradient field), got {got:.12g} ({LI_HINT})")


def test_line_integral_of_a_gradient_field_around_a_closed_path_is_0(at):
    """A closed path (its last point equal to the first): 0 for a gradient field, exactly for a polynomial f of
    degree at most 4, up to 1e-9 for a smooth f with n_sub = 236."""
    rng = _rng(7836)
    for d, k in ((2, 4), (3, 6), (1, 5)):
        f, grad, name = _polynomial_potential(rng, d)
        P = _polyline(rng, k, d)
        closed = np.vstack([P, P[:1]])
        got, _ = _li(at, grad, name, closed, 8)
        scale = 1.0 + max(abs(f(p)) for p in P)
        assert abs(got) <= 1e-11 * scale, (
            f"expected {_describe_li(name, closed, 8)} = 0 (a gradient field along a closed path), got {got:.12g} "
            f"({LI_HINT})")
        f, grad, name = _smooth_potential(rng, d)
        got, _ = _li(at, grad, name, closed, 236)
        assert abs(got) <= 1e-9, (
            f"expected {_describe_li(name, closed, 236)} = 0 (a gradient field along a closed path), got {got:.12g} "
            f"({LI_HINT})")


def test_line_integral_of_a_field_that_is_not_a_gradient_depends_on_the_path(at):
    """A polynomial field of degree 3 that is not a gradient, along two paths with the same ends: each value is the
    exact one (scipy.integrate.quad on each segment), and the two values differ."""
    rng = _rng(7837)
    for d in (2, 3):
        function, _, _, name = _polynomial_field(rng, d)
        start, end = _polyline(rng, 2, d)
        first = np.array([start, _polyline(rng, 1, d)[0], end])
        second = np.array([start, _polyline(rng, 1, d)[0], _polyline(rng, 1, d)[0], end])
        values = []
        for P in (first, second):
            got, _ = _li(at, function, name, P, 4)
            want = math.fsum(_quad_path(function, P))
            assert math.isclose(got, want, rel_tol=1e-11, abs_tol=1e-11), (
                f"expected {_describe_li(name, P, 4)} = {want:.12g} (scipy.integrate.quad on each segment; exact for "
                f"a field of degree 3), got {got:.12g} ({LI_HINT})")
            values.append(want)
        assert abs(values[0] - values[1]) > 1e-3        # the oracle: the two paths do differ


def test_line_integral_reversed_path_changes_the_sign(at):
    """The same vertices in the reverse order: the opposite value, for any field (up to rounding)."""
    rng = _rng(7838)
    for d, k in ((1, 3), (2, 4), (3, 5), (4, 2)):
        function, name = _smooth_field(rng, d)
        P = _polyline(rng, k, d)
        forward, _ = _li(at, function, name, P, 12)
        backward, _ = _li(at, function, name, P[::-1], 12)
        assert math.isclose(backward, -forward, rel_tol=1e-11, abs_tol=1e-12), (
            f"expected {_describe_li(name, P[::-1], 12)} (the path reversed) = -({forward:.12g}), got "
            f"{backward:.12g} ({LI_HINT})")


def test_line_integral_forth_and_back_gives_0(at):
    """a → b → a, and a → b → c → b → a: every segment is followed back, and the integral is 0 for any field (up to
    rounding)."""
    rng = _rng(7839)
    for d in (1, 2, 3):
        function, name = _smooth_field(rng, d)
        a, b, c = _polyline(rng, 3, d)
        for P in (np.array([a, b, a]), np.array([a, b, c, b, a])):
            got, _ = _li(at, function, name, P, 22)
            assert abs(got) <= 1e-11, (
                f"expected {_describe_li(name, P, 22)} = 0 (each segment followed back), got {got:.12g} ({LI_HINT})")


def test_line_integral_a_segment_of_length_0_adds_0(at):
    """A vertex repeated (a segment of length 0) changes nothing; a path that never moves gives 0.0."""
    rng = _rng(7840)
    for d in (1, 2, 3):
        function, name = _smooth_field(rng, d)
        P = _polyline(rng, 4, d)
        want, _ = _li(at, function, name, P, 8)
        for repeated in (np.vstack([P[:2], P[1:]]), np.vstack([P[:1], P]), np.vstack([P, P[-1:], P[-1:]])):
            got, _ = _li(at, function, name, repeated, 8)
            assert math.isclose(got, want, rel_tol=1e-13, abs_tol=1e-14), (
                f"expected {_describe_li(name, repeated, 8)} = {want:.12g}, the value without the repeated vertex (a "
                f"segment of length 0 adds 0), got {got:.12g} ({LI_HINT})")
        still = np.vstack([P[2:3]] * 3)
        got, _ = _li(at, function, name, still, 8)
        assert got == 0.0, (
            f"expected {_describe_li(name, still, 8)} = 0.0 (the path never moves), got {got!r} ({LI_HINT})")


def test_line_integral_a_vertex_added_inside_a_segment_changes_nothing_for_degree_3(at):
    """A vertex added on a segment (at a fraction of it that is not ½) changes nothing when the field is of degree at
    most 3 (Simpson's rule is exact on both pieces)."""
    rng = _rng(7841)
    for d in (1, 2, 3):
        function, _, _, name = _polynomial_field(rng, d)
        P = _polyline(rng, 3, d)
        want, _ = _li(at, function, name, P, 4)
        inside = P[0] + 0.38 * (P[1] - P[0])
        cut = np.vstack([P[:1], inside, P[1:]])
        got, _ = _li(at, function, name, cut, 4)
        assert math.isclose(got, want, rel_tol=1e-11, abs_tol=1e-11), (
            f"expected {_describe_li(name, cut, 4)} = {want:.12g}, the value without the vertex added inside the first "
            f"segment (a field of degree 3), got {got:.12g} ({LI_HINT})")


def _nodes(P, n_sub):
    """The points a + (k / n_sub)(b - a), k = 0, …, n_sub, of each segment: (segment, k, point)."""
    return [(j, kk, a + (kk / n_sub) * (b - a)) for j, (a, b) in enumerate(zip(P[:-1], P[1:]))
            for kk in range(n_sub + 1)]


NODE_CASES = [(2, 4), (3, 8), (1, 2)]


@pytest.mark.parametrize("d, n_sub", NODE_CASES, ids=[f"d{d}-n{n}" for d, n in NODE_CASES])
def test_line_integral_evaluates_the_field_at_the_n_sub_plus_1_points_of_each_segment(attribution_module, d, n_sub):
    """The field is evaluated at the points a + k h (b - a), k = 0, …, n_sub, h = 1 / n_sub, of every segment (a
    common vertex may be evaluated once only), and nowhere else."""
    rng = _rng(7842, d)
    function, name = _smooth_field(rng, d)
    P = _polyline(rng, 4, d)
    what = _describe_li(name, P, n_sub)
    _, field = _li(attribution_module, function, name, P, n_sub, keep=True)
    nodes = _nodes(P, n_sub)
    points = np.array([p for _, _, p in nodes])
    scale = 1e-12 * (1.0 + float(np.max(np.abs(P))))
    for p in field.received:
        if np.min(np.max(np.abs(points - p), axis=1)) > scale:
            pytest.fail(f"expected the field to be evaluated only at the points a + k h (b - a), k = 0, …, {n_sub}, "
                        f"h = 1 / {n_sub}, of the segments of {what}, got an evaluation at {_show(p)} ({LI_HINT})")
    seen = np.array(field.received)
    for j, kk, p in nodes:
        if seen.size == 0 or np.min(np.max(np.abs(seen - p), axis=1)) > scale:
            pytest.fail(f"expected the field to be evaluated at a + {kk} h (b - a) = {_show(p)} (segment {j}, "
                        f"h = 1 / {n_sub}) for {what}, never got this point ({LI_HINT})")


def test_line_integral_calls_the_field_on_one_point_at_a_time(attribution_module):
    """The field receives one point at a time: a 1-D numpy.ndarray of floats of shape (d,) (for d = 1 too: shape
    (1,)), never a batch of points, never a list, never an array of integers (even for vertices given as integers)."""
    rng = _rng(7843)
    for d in (1, 2, 3):
        function, name = _smooth_field(rng, d)
        P = rng.integers(-12, 13, size=(3, d))
        while np.any(np.all(P[1:] == P[:-1], axis=1)):
            P = rng.integers(-12, 13, size=(3, d))
        _li(attribution_module, function, name, P, 8)
        _li(attribution_module, function, name, P.tolist(), 8)


def test_line_integral_a_field_that_writes_into_its_point_changes_nothing(attribution_module):
    """A field that writes into the array it receives, after reading it, changes neither the value nor the vertices:
    each point is a new array, and never a view of the vertices given to line_integral."""
    rng = _rng(7844)
    for d in (1, 2, 3):
        function, name = _smooth_field(rng, d)
        P = _polyline(rng, 4, d)
        copy = P.copy()
        want, _ = _li(attribution_module, function, name, P.copy(), 8)
        got, field = _li(attribution_module, function, name, P, 8, mutate=True, watch=P)
        what = _describe_li(name, copy, 8)
        assert np.array_equal(P, copy), (
            f"expected the vertices unchanged by {what} with a field that writes into the point it receives, got "
            f"{_show(P)} (each point given to the field is a new array, never a row of points)")
        assert not field.shared, (
            f"expected the field to receive new arrays for {what}, got a point that shares its memory with the "
            f"vertices given to line_integral ({LI_HINT})")
        assert math.isclose(got, want, rel_tol=1e-13, abs_tol=1e-14), (
            f"expected {what} = {want:.12g} with a field that writes into the point it receives after reading it, "
            f"got {got:.12g} (the points of the following calls must not depend on what the field did with the "
            f"previous ones) ({LI_HINT})")


def test_line_integral_does_not_modify_points(attribution_module):
    """The vertices as float arrays that are not dyadic (C or Fortran order, float32) are left unchanged."""
    rng = _rng(7845)
    function, name = _smooth_field(rng, 2)
    for P in (_polyline(rng, 4, 2) * 1.37, np.asfortranarray(_polyline(rng, 5, 2) * 2.11),
              (_polyline(rng, 3, 2) * 0.93).astype(np.float32)):
        copy = P.copy()
        what = _describe_li(name, P, 8)
        _li(attribution_module, function, name, P, 8)
        assert np.array_equal(P, copy), (
            f"expected points unchanged by {what}, got {_show(P)} (never modify the array you receive: "
            f"np.array(points, dtype=float) is a copy, np.asarray(points, dtype=float) may be the array itself)")


FIELD_RETURNS = [(lambda p: (0.38 * p[0] - 1.17, math.cos(p[1])), "a tuple"),
                 (lambda p: [0.38 * p[0] - 1.17, math.cos(p[1])], "a list"),
                 (lambda p: np.array([0.38 * p[0] - 1.17, np.cos(p[1])], dtype=np.float32), "a float32 array"),
                 (lambda p: (3, -2), "a tuple of ints")]


@pytest.mark.parametrize("function, text", FIELD_RETURNS, ids=["tuple", "list", "float32", "ints"])
def test_line_integral_accepts_any_array_like_from_the_field(at, function, text):
    """The field may return a tuple, a list, a float32 array or integers (an array-like of shape (d,))."""
    P = np.array(OK_POINTS)
    want = math.fsum(_quad_path(function, P)) if text != "a float32 array" else None
    got, _ = _li(at, function, f"a field that returns {text}", P, 236)
    if want is None:
        want = math.fsum(_quad_path(lambda p: np.array([0.38 * p[0] - 1.17, np.cos(p[1])]), P))
        assert math.isclose(got, want, rel_tol=1e-6, abs_tol=1e-6), (
            f"expected {_describe_li('a field that returns a float32 array', P, 236)} ≈ {want:.8g}, got {got:.12g} "
            f"({LI_HINT})")
    else:
        assert math.isclose(got, want, rel_tol=1e-9, abs_tol=1e-10), (
            f"expected {_describe_li(f'a field that returns {text}', P, 236)} = {want:.12g}, got {got:.12g} "
            f"({LI_HINT})")


VERTEX_KINDS = [(lambda P: P.tolist(), "a list of lists"),
                (lambda P: tuple(map(tuple, P.tolist())), "a tuple of tuples"),
                (lambda P: P.astype(np.float32), "a float32 array")]


@pytest.mark.parametrize("convert, text", VERTEX_KINDS, ids=["list", "tuple", "float32"])
def test_line_integral_accepts_vertices_as_lists_tuples_or_float32_and_returns_a_python_float(at, convert, text):
    rng = _rng(7846, [t for _, t in VERTEX_KINDS].index(text))
    f, grad, name = _polynomial_potential(rng, 2)
    P = np.round(_polyline(rng, 4, 2), 3)
    given = convert(P)
    got, _ = _li(at, grad, name, given, 8, what=_describe_li(name, P, 8) + f" (the vertices as {text})")
    Q = np.asarray(given, dtype=float)
    want = f(Q[-1]) - f(Q[0])
    assert math.isclose(got, want, rel_tol=1e-10, abs_tol=1e-10), (
        f"expected {_describe_li(name, P, 8)} (the vertices as {text}) = {want:.12g}, got {got:.12g} ({LI_HINT})")


def test_line_integral_in_dimension_1(at):
    """d = 1: the vertices form an array of shape (k, 1), the field receives arrays of shape (1,) and returns
    [value]; the gradient theorem gives f(last) - f(first) for F = [f'(x)]."""
    rng = _rng(7847)
    for _ in range(3):
        c, w, ph = float(rng.uniform(0.6, 1.8)), float(rng.uniform(0.5, 1.4)), float(rng.uniform(0.0, 3.0))
        name = f"[{c:.4g} {w:.4g} cos({w:.4g} x + {ph:.4g})]"
        P = rng.uniform(-2.0, 2.0, size=(5, 1))
        got, _ = _li(at, lambda p: [c * w * math.cos(w * p[0] + ph)], name, P, 512)
        want = c * math.sin(w * P[-1, 0] + ph) - c * math.sin(w * P[0, 0] + ph)
        assert math.isclose(got, want, rel_tol=1e-9, abs_tol=1e-10), (
            f"expected {_describe_li(name, P, 512)} = f(last) - f(first) = {want:.12g} for f = {c:.4g} sin({w:.4g} x "
            f"+ {ph:.4g}), got {got:.12g} ({LI_HINT})")


def test_line_integral_default_n_sub_and_n_sub_given_by_position(at):
    """line_integral(F, points) is line_integral(F, points, n_sub=20) (the default of the signature), and n_sub may
    be given by position; another n_sub gives another value for a smooth field."""
    rng = _rng(7848)
    function, name = _smooth_field(rng, 2)
    P = _polyline(rng, 4, 2, spread=1.9)
    default, _ = _li(at, function, name, P)
    explicit, _ = _li(at, function, name, P, DEFAULT_N_SUB)
    positional, _ = _li(at, function, name, P, DEFAULT_N_SUB, positional=True)
    assert default == explicit == positional, (
        f"expected {_describe_li(name, P)} = {_describe_li(name, P, DEFAULT_N_SUB)} = "
        f"{_describe_li(name, P, DEFAULT_N_SUB, positional=True)} (the default n_sub), got {default!r}, {explicit!r} "
        f"and {positional!r} ({LI_HINT})")
    for other in (DEFAULT_N_SUB - 2, DEFAULT_N_SUB + 2):
        value, _ = _li(at, function, name, P, other)
        assert value != default, (
            f"expected {_describe_li(name, P, other)} to differ from the value with n_sub = {DEFAULT_N_SUB} for a "
            f"smooth field, got the same {value!r} (n_sub is the number of intervals on each segment) ({LI_HINT})")


@pytest.mark.parametrize("n_sub", [np.int64(14), np.int32(8), np.uint8(26), np.int16(2)],
                         ids=["int64", "int32", "uint8", "int16"])
def test_line_integral_accepts_numpy_integers_for_n_sub(at, n_sub):
    rng = _rng(7849, int(n_sub))
    function, _, _, name = _polynomial_field(rng, 2)
    P = _polyline(rng, 3, 2)
    got, _ = _li(at, function, name, P, n_sub)
    want = math.fsum(_quad_path(function, P))
    assert math.isclose(got, want, rel_tol=1e-11, abs_tol=1e-11), (
        f"expected {_describe_li(name, P, n_sub)} (a NumPy integer) = {want:.12g}, got {got:.12g} ({LI_HINT})")


def test_line_integral_of_many_segments_is_fast(at):
    """250 segments with n_sub = 58 (14 750 evaluations of the field): a few seconds at most, and the gradient
    theorem."""
    rng = _rng(7850)
    f, grad, name = _polynomial_potential(rng, 3)
    P = np.cumsum(rng.uniform(-0.2, 0.2, size=(251, 3)), axis=0)
    got, _ = _li(at, grad, name, P, 58, seconds=60)
    want = f(P[-1]) - f(P[0])
    assert math.isclose(got, want, rel_tol=1e-10, abs_tol=1e-10), (
        f"expected {_describe_li(name, P, 58)} = f(last) - f(first) = {want:.12g}, got {got:.12g} ({LI_HINT})")


def _wave(p):
    """A field of the shape of p: 0.79 cos(1.31 p), coordinate by coordinate."""
    return 0.79 * np.cos(1.31 * np.asarray(p, dtype=float))


def _constant(p):
    """A constant field of the shape of p (it gives no nan of its own, whatever the point)."""
    return np.full(np.shape(p), 0.79)


OK_POINTS = [[0.13, -0.68], [1.37, 0.43], [0.57, 1.86]]
BAD_POINTS = [([0.38, 1.17], "points is 1-D: a path needs rows of coordinates"),
              ([[0.38, 1.17]], "a single row: a path needs k ≥ 2 vertices"),
              (np.empty((3, 0)), "d = 0 columns"), (np.full((2, 2, 2), 0.43), "points is 3-D"),
              ([[0.13, np.nan], [1.17, 2.05]], "points holds a nan"),
              ([[0.13, 0.29], [np.inf, 2.05]], "points holds inf"),
              ([[0.13, 0.29], [1.17]], "rows of different lengths"), (None, "points is None"),
              (3.25, "points is a number"), ([], "points is empty")]
BAD_POINT_IDS = ["1d", "one-row", "no-column", "3d", "nan", "inf", "ragged", "none", "number", "empty"]


@pytest.mark.parametrize("points, why", BAD_POINTS, ids=BAD_POINT_IDS)
def test_line_integral_refuses_bad_points(at, points, why):
    _expect_error(ValueError, lambda: at.line_integral(_constant, points, n_sub=4), f"line_integral(F, {points!r}, "
                  f"n_sub=4) with F(p) = (0.79, …, 0.79), a constant field", why)


BAD_N_SUB = [(0, "n_sub = 0"), (1, "n_sub = 1 is odd"), (3, "n_sub = 3 is odd"), (19, "n_sub = 19 is odd"),
             (-2, "n_sub is negative"), (-4, "n_sub is negative"), (8.0, "n_sub is the float 8.0"),
             (np.float64(12.0), "n_sub is np.float64(12.0)"), (4.5, "n_sub is 4.5"), (True, "n_sub is True, a bool"),
             (np.True_, "n_sub is np.True_, a NumPy bool"), ("8", "n_sub is a string"), (None, "n_sub is None"),
             (np.int64(9), "n_sub is np.int64(9), odd")]
BAD_N_SUB_IDS = ["n0", "n1", "n3", "n19", "n-minus-2", "n-minus-4", "n-float", "n-numpy-float", "n-half", "n-bool",
                 "n-numpy-bool", "n-string", "n-none", "n-numpy-odd"]


@pytest.mark.parametrize("n_sub, why", BAD_N_SUB, ids=BAD_N_SUB_IDS)
def test_line_integral_refuses_a_bad_n_sub(at, n_sub, why):
    field = _Field(_wave, 2, 498)
    _expect_error(ValueError, lambda: at.line_integral(field, OK_POINTS, n_sub=n_sub),
                  f"line_integral(F, {OK_POINTS!r}, n_sub={n_sub!r})", why + " (n_sub must be an even integer ≥ 2)")


@pytest.mark.parametrize("field, text", [(None, "None"), ([1.0, 2.0], "a list"), (np.array([0.5, 1.5]), "an array"),
                                         (3.25, "a number"), ("cos", "a string")],
                         ids=["none", "list", "array", "number", "string"])
def test_line_integral_refuses_a_field_that_is_not_callable(at, field, text):
    _expect_error(ValueError, lambda: at.line_integral(field, OK_POINTS, n_sub=4),
                  f"line_integral({text}, {OK_POINTS!r}, n_sub=4)", "the field must be a callable")


def _late(value, after=4):
    """A field right on its first calls, that returns `value` from call number `after` + 1 on."""
    calls = []

    def field(p):
        calls.append(1)
        return value if len(calls) > after else _wave(p)

    return field


BAD_VALUES = [(2, lambda p: 1.25, "a bare number for d = 2"),
              (1, lambda p: 0.75 * float(p[0]), "a bare number for d = 1 (for d = 1 too: [value])"),
              (1, lambda p: np.float64(0.75), "a NumPy number for d = 1"),
              (2, lambda p: np.array([0.4, 0.2, 0.1]), "shape (3,) for d = 2"),
              (2, lambda p: np.array([0.4]), "shape (1,) for d = 2, even if NumPy could broadcast it"),
              (2, lambda p: np.array([[0.4, 0.2]]), "shape (1, 2) for d = 2"),
              (2, lambda p: np.array([[0.4], [0.2]]), "shape (2, 1) for d = 2"),
              (3, lambda p: np.array([0.4, 0.2]), "shape (2,) for d = 3"),
              (2, lambda p: np.array([0.4, np.nan]), "a nan"), (2, lambda p: (np.inf, 0.2), "an inf"),
              (2, lambda p: None, "None (a field without return)"),
              (2, "late", "the right shape on the first four calls, then shape (1, 2)")]
BAD_VALUE_IDS = ["number", "number-d1", "numpy-number-d1", "longer", "one", "row", "column", "shorter-d3", "nan", "inf",
                 "none", "late"]


@pytest.mark.parametrize("d, value, why", BAD_VALUES, ids=BAD_VALUE_IDS)
def test_line_integral_refuses_a_field_value_of_another_shape_or_not_finite(at, d, value, why):
    """The field must return an array of shape (d,) of finite numbers, at every call."""
    points = [row[:d] for row in ([0.13, -0.68, 0.29], [0.43, -0.11, -0.13], [0.79, 0.43, -0.57])]
    function = _late(np.array([[0.4, 0.2]])) if value == "late" else value
    field = _Field(function, d, 498)
    _expect_error(ValueError, lambda: at.line_integral(field, points, n_sub=4),
                  f"line_integral(F, {points!r}, n_sub=4) with F returning {why}",
                  "the field must return an array of shape (d,) of finite numbers")


# --- spearman_rho ---------------------------------------------------------------------------------------------------

SR_HINT = ("rank each sample: the smallest value gets rank 1, the next rank 2, …, and tied values (exactly equal) "
           "share the mean of the places they occupy; then ρ = Σ (r_i - r̄)(s_i - s̄) / √(Σ (r_i - r̄)² · "
           "Σ (s_i - s̄)²) on the two vectors of ranks, nan when one of them is constant; return a Python float")
SR_SECONDS = 30


def _scipy_rho(x, y):
    """Spearman's ρ by scipy.stats.spearmanr (nan for a constant sample, without its warning)."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return float(stats.spearmanr(np.asarray(x, dtype=float), np.asarray(y, dtype=float)).statistic)


def _pearson(r, s):
    r, s = np.asarray(r, dtype=float), np.asarray(s, dtype=float)
    r, s = r - r.mean(), s - s.mean()
    den = math.sqrt(float(r @ r) * float(s @ s))
    return math.nan if den == 0 else float(r @ s) / den


def _sr_variants(x, y):
    """ρ computed with a classic error, with the reason."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    out = []
    for method, text in (("min", "tied values share the mean of the places they occupy, not the first of them"),
                         ("max", "tied values share the mean of the places they occupy, not the last of them"),
                         ("ordinal", "tied values share the mean of the places they occupy: here they got different "
                                     "ranks, in their order of appearance"),
                         ("dense", "tied values occupy several places, and their rank is the mean of these places: "
                                   "dense ranks (1, 2, 2, 3) skip none")):
        out.append((_pearson(stats.rankdata(x, method=method), stats.rankdata(y, method=method)), text))
    r, s = stats.rankdata(x), stats.rankdata(y)
    n = len(x)
    out.append((1 - 6 * float(np.sum((r - s) ** 2)) / (n * (n * n - 1)),
                "1 - 6 Σ d² / (n (n² - 1)) is Pearson's correlation of the ranks only without ties: with ties, use "
                "Pearson's formula on the ranks"))
    return out


def _describe_sr(x, y):
    return f"spearman_rho({_show(x)}, {_show(y)})"


def _sr(at, x, y, what=None, seconds=SR_SECONDS):
    what = what or _describe_sr(x, y)
    got = _within(seconds, lambda: at.spearman_rho(x, y), what, "a Python float", SR_HINT)
    _python_float(got, what, SR_HINT)
    return got


def _ranks_text(x):
    return _show(stats.rankdata(np.asarray(x, dtype=float)))


def _check_rho(got, x, y, what=None, rtol=1e-12, atol=1e-13):
    want = _scipy_rho(x, y)
    what = what or _describe_sr(x, y)
    if math.isnan(want):
        if not math.isnan(got):
            pytest.fail(f"expected {what} = nan (all the values of {'x' if np.ptp(x) == 0 else 'y'} are equal: the "
                        f"ranks are constant), got {got!r} ({SR_HINT})")
        return
    if math.isclose(got, want, rel_tol=rtol, abs_tol=atol):
        return
    text = " — or ".join(dict.fromkeys(t for value, t in _sr_variants(x, y)
                                       if not math.isnan(value)
                                       and not math.isclose(value, want, rel_tol=1e-9, abs_tol=1e-11)
                                       and math.isclose(got, value, rel_tol=1e-9, abs_tol=1e-11)))
    pytest.fail(f"expected {what} = {want:.12g} (scipy.stats.spearmanr; ranks of x {_ranks_text(x)}, ranks of y "
                f"{_ranks_text(y)}), got {got!r} (" + (f"here {text}; " if text else "") + SR_HINT + ")")


SR_NS = [2, 3, 5, 9, 17, 29, 101]


@pytest.mark.parametrize("n", SR_NS, ids=[f"n{n}" for n in SR_NS])
def test_spearman_rho_without_ties_matches_scipy(at, n):
    """Samples without ties (continuous values, related or not): ρ of scipy.stats.spearmanr."""
    rng = _rng(7860, n)
    for link in (0.0, 0.6, -1.4):
        x = rng.normal(size=n) * 1.7 + 0.3
        y = link * x + rng.normal(size=n) * 0.9
        _check_rho(_sr(at, x, y), x, y)


TIE_CASES = [(5, "x"), (9, "y"), (11, "both"), (23, "both"), (57, "x"), (61, "both")]


@pytest.mark.parametrize("n, where", TIE_CASES, ids=[f"n{n}-{w}" for n, w in TIE_CASES])
def test_spearman_rho_with_ties_matches_scipy(at, n, where):
    """Ties in x, in y or in both (values drawn among a few, not dyadic): ρ of scipy.stats.spearmanr, the tied values
    sharing the mean of their places."""
    rng = _rng(7861, n)
    for _ in range(3):
        levels = rng.uniform(-2.0, 2.0, size=4)
        tied = levels[rng.integers(0, 4, size=n)]
        free = rng.normal(size=n)
        x = tied if where in ("x", "both") else free
        y = (0.7 * tied + rng.normal(size=n) * 0.3 if where == "y" else
             levels[rng.integers(0, 4, size=n)] * 1.3 + 0.2 if where == "both" else free + 0.5 * tied)
        if np.ptp(x) == 0 or np.ptp(y) == 0:
            continue
        _check_rho(_sr(at, x, y), x, y)


def test_spearman_rho_of_a_constant_sample_is_nan(at):
    """All the values of x, or all those of y, equal: the ranks are constant, ρ is not defined, and the result is
    nan (a Python float), without a RuntimeWarning."""
    rng = _rng(7862)
    for n in (2, 5, 11):
        c = float(rng.uniform(-3.0, 3.0))
        free = rng.normal(size=n)
        for x, y in ((np.full(n, c), free), (free, np.full(n, c)), (np.full(n, c), np.full(n, -c))):
            got = _sr(at, x, y)
            assert math.isnan(got), (
                f"expected {_describe_sr(x, y)} = nan (all the values of {'x' if np.ptp(x) == 0 else 'y'} are equal: "
                f"the ranks are constant), got {got!r} ({SR_HINT})")


MAPS = [(np.exp, "exp"), (lambda v: v ** 3, "v ↦ v³"), (lambda v: 2.31 * v - 1.13, "v ↦ 2.31 v - 1.13"),
        (np.arctan, "arctan")]


def test_spearman_rho_does_not_change_under_strictly_increasing_maps(at):
    """A strictly increasing function applied to the values of x, of y or of both keeps the order, hence the ranks
    and ρ (exactly), with ties or without."""
    rng = _rng(7863)
    for n, ties in ((7, False), (13, True), (31, True)):
        x = np.round(rng.uniform(-2.6, 2.6, size=n), 1) if ties else rng.uniform(-2.6, 2.6, size=n)
        y = 0.79 * x + rng.normal(size=n)
        base = _sr(at, x, y)
        for g, name in MAPS:
            for gx, gy, where in ((g(x), y, "x"), (x, g(y), "y"), (g(x), g(y), "x and y")):
                got = _sr(at, gx, gy)
                assert math.isclose(got, base, rel_tol=1e-13, abs_tol=1e-14), (
                    f"expected {_describe_sr(gx, gy)} = {_describe_sr(x, y)} = {base!r} ({name} applied to {where} "
                    f"keeps the ranks), got {got!r} ({SR_HINT})")


def test_spearman_rho_changes_sign_under_a_strictly_decreasing_map(at):
    """v ↦ -v (or any strictly decreasing function) applied to the values of one sample reverses its ranks, and ρ
    changes sign (exactly), ties included."""
    rng = _rng(7864)
    for n in (6, 19):
        x = np.round(rng.uniform(-2.0, 2.0, size=n), 1)
        y = x - rng.normal(size=n) * 0.7
        base = _sr(at, x, y)
        for gx, gy, text in ((-x, y, "-x"), (x, np.exp(-y), "exp(-y)")):
            got = _sr(at, gx, gy)
            assert math.isclose(got, -base, rel_tol=1e-13, abs_tol=1e-14), (
                f"expected {_describe_sr(gx, gy)} = -{_describe_sr(x, y)} = {-base!r} ({text}: the ranks reversed), "
                f"got {got!r} ({SR_HINT})")


def test_spearman_rho_is_symmetric_and_does_not_depend_on_the_order_of_the_items(at):
    """ρ(y, x) = ρ(x, y), and listing the pairs (x[i], y[i]) in another order changes nothing."""
    rng = _rng(7865)
    for n in (5, 14, 33):
        x = np.round(rng.normal(size=n) * 2, 1)
        y = np.round(0.5 * x + rng.normal(size=n), 1)
        base = _sr(at, x, y)
        swapped = _sr(at, y, x)
        assert math.isclose(swapped, base, rel_tol=1e-13, abs_tol=1e-14), (
            f"expected {_describe_sr(y, x)} = {_describe_sr(x, y)} = {base!r} (ρ is symmetric), got {swapped!r} "
            f"({SR_HINT})")
        order = rng.permutation(n)
        moved = _sr(at, x[order], y[order])
        assert math.isclose(moved, base, rel_tol=1e-13, abs_tol=1e-14), (
            f"expected {_describe_sr(x[order], y[order])} = {base!r} (the same pairs in another order), got {moved!r} "
            f"({SR_HINT})")


def test_spearman_rho_of_a_sample_with_itself_is_1(at):
    """ρ(x, x) = 1 for a sample that is not constant, with ties or without."""
    rng = _rng(7866)
    for x in (rng.normal(size=9), np.round(rng.normal(size=17), 1)):
        got = _sr(at, x, x.copy())
        assert math.isclose(got, 1.0, rel_tol=0, abs_tol=1e-14), (
            f"expected {_describe_sr(x, x)} = 1 (the same ranks), got {got!r} ({SR_HINT})")


def test_spearman_rho_ties_are_exactly_equal_values(at):
    """Only values exactly equal are tied: 0.1 + 0.2 and 0.3, or values 1e-15 apart, are two different values, as
    for scipy.stats.spearmanr."""
    rng = _rng(7867)
    close = np.array([0.1 + 0.2, 0.3, 0.71, 0.71 + 1e-15, 1.93, 1.93 + 6e-16, -0.43])
    text = "[0.1 + 0.2, 0.3, 0.71, 0.71 + 1e-15, 1.93, 1.93 + 6e-16, -0.43] (seven different floats)"
    for _ in range(3):
        y = rng.normal(size=close.size)
        _check_rho(_sr(at, close, y), close, y, what=f"spearman_rho(x, y) with x = {text}, y = {_show(y)}")
        _check_rho(_sr(at, y, close), y, close, what=f"spearman_rho(x, y) with x = {_show(y)}, y = {text}")


def test_spearman_rho_lies_between_minus_1_and_1(at):
    rng = _rng(7868)
    for n in (3, 4, 12, 47):
        for _ in range(4):
            x = np.round(rng.normal(size=n), 1)
            y = np.round(rng.normal(size=n) + rng.uniform(-2, 2) * x, 1)
            if np.ptp(x) == 0 or np.ptp(y) == 0:
                continue
            got = _sr(at, x, y)
            assert -1.0 <= got <= 1.0, f"expected {_describe_sr(x, y)} in [-1, 1], got {got!r} ({SR_HINT})"


SR_KINDS = [(lambda v: v.tolist(), "lists"), (lambda v: tuple(v.tolist()), "tuples"),
            (lambda v: np.round(v * 10).astype(int), "integer arrays"), (lambda v: v.astype(np.float32), "float32")]


@pytest.mark.parametrize("convert, text", SR_KINDS, ids=["lists", "tuples", "ints", "float32"])
def test_spearman_rho_accepts_lists_tuples_integers_and_float32(at, convert, text):
    """Samples given as lists, tuples, integer arrays or float32 arrays; the result is a Python float."""
    rng = _rng(7869, [t for _, t in SR_KINDS].index(text))
    base = np.round(rng.normal(size=13), 2)
    x, y = convert(base), convert(np.round(base * 0.6 + rng.normal(size=13), 2))
    _check_rho(_sr(at, x, y, what=_describe_sr(x, y) + f" (samples as {text})"), x, y)


def test_spearman_rho_does_not_modify_its_inputs(attribution_module):
    """x and y as float arrays that are not dyadic, with ties, a strided view among them: left unchanged (sorting a
    sample in place would reorder it)."""
    rng = _rng(7870)
    big = rng.normal(size=46) * 1.37
    for x, y in ((rng.normal(size=11) * 2.11, np.round(rng.normal(size=11), 1) * 0.38), (big[::2], big[1::2] * 0.93)):
        cx, cy = x.copy(), y.copy()
        what = _describe_sr(x, y)
        _within(SR_SECONDS, lambda: attribution_module.spearman_rho(x, y), what, "a Python float", SR_HINT)
        assert np.array_equal(x, cx) and np.array_equal(y, cy), (
            f"expected x and y unchanged by {what}, got {_show(x)} and {_show(y)} (never modify the arrays you "
            f"receive: np.sort(x) is a sorted copy, x.sort() sorts x itself)")


def test_spearman_rho_of_a_large_sample_with_ties(at):
    """3 001 items with many ties: ρ of scipy.stats.spearmanr, within a few seconds."""
    rng = _rng(7871)
    x = np.round(rng.normal(size=3001) * 30) / 7
    y = np.round(0.4 * x * 7 + rng.normal(size=3001) * 20) / 3
    _check_rho(_sr(at, x, y), x, y, what="spearman_rho(x, y) for 3001 items with ties")


BAD_SR = [([0.43, 1.37, 2.29], [0.13, 0.89], "lengths 3 and 2"), ([0.43], [1.17], "length 1: ρ needs n ≥ 2"),
          ([], [], "empty samples"), ([[0.43], [1.37], [2.29]], [0.13, 0.89, 0.38], "x of shape (3, 1)"),
          ([0.43, 1.37, 2.29], [[0.13, 0.89, 0.38]], "y of shape (1, 3)"),
          ([[0.43, 1.37, 2.29], [0.57, 1.86, 2.31]], [0.13, 0.89, 0.38], "x is 2-D"),
          (np.float64(3.25), [0.13, 0.89], "x is a number (0-D)"),
          ([0.43, np.nan, 2.29], [0.13, 0.89, 0.38], "a nan in x"),
          ([0.43, 1.37, 2.29], [0.13, np.inf, 0.38], "inf in y"),
          ([0.43, 1.37, 2.29], [-np.inf, 0.89, 0.38], "-inf in y"),
          (None, [0.13, 0.89], "x is None"), ([0.43, [1.37, 2.29]], [0.13, 0.89], "x is ragged")]
BAD_SR_IDS = ["lengths", "one", "empty", "x-column", "y-row", "x-2d", "x-number", "x-nan", "y-inf", "y-minus-inf",
              "x-none", "x-ragged"]


@pytest.mark.parametrize("x, y, why", BAD_SR, ids=BAD_SR_IDS)
def test_spearman_rho_refusals(at, x, y, why):
    _expect_error(ValueError, lambda: at.spearman_rho(x, y), f"spearman_rho({x!r}, {y!r})", why)
