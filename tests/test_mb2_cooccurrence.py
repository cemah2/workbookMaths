"""Tests of mymath.cooccurrence (chapter MB2): the table of the pointwise mutual information (PMI) of a joint law, the
logit of a population estimated on a case-control sample, and the removal of a direction from the rows of a matrix.

Oracles: exact rational arithmetic (``fractions.Fraction``, then ``math.log`` of the exact ratio) for the PMI of a
table and for the corrected logit; ``sklearn.metrics.mutual_info_score`` (in nats) and the entropies of
``scipy.stats.entropy`` (H(X) + H(Y) - H(X, Y)) for the mean of the PMI under the joint law; ``scipy.special.logit`` of
the observed proportion, and the coefficient of ``sklearn.linear_model.LogisticRegression`` fitted on the labels of the
sample; the residual of ``np.linalg.lstsq`` and the projection on an orthonormal basis of the complement of u
(``scipy.linalg.null_space``) for ``remove_direction``. Never another function of yours. Plus properties: the bounds
ln p(x, y) ≤ PMI(x, y) ≤ min(-ln p(x), -ln p(y)), the upper one reached when x occurs only with y, and a normalized
PMI between -1 and 1; the sign of the PMI against independence, the zero PMI of a column independent of the rows; the
transposed and the permuted tables; -inf on the cells of probability 0 without a warning, no clipping of tiny
probabilities; for the logit, the same result when both numbers of examples (or both rates) are multiplied by the same
factor, the opposite logit when the labels are swapped, a shift that is the same for every group, ±inf,
broadcasting, and a sample drawn at random whose corrected logit finds the population back; for the direction, rows
orthogonal to u, the same result when the direction is removed twice or when u is replaced by c u, Pythagoras on the
distances, linearity, an orthogonal change of basis, the centering by (1, …, 1); inputs left unchanged, lists,
integers and NumPy numbers, and every refusal of the docstrings. They describe the expected behaviour without showing
the solution.

    pytest tests/test_mb2_cooccurrence.py              # your code
    pytest tests/test_mb2_cooccurrence.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings
from fractions import Fraction

import numpy as np
import pytest
from scipy import linalg, special, stats
from scipy.spatial import distance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mutual_info_score


@pytest.fixture
def cc_module(mymath_module):
    """The module itself: for the tests that check that your functions never write into the arrays they receive, and
    for the check of what the module uses."""
    return mymath_module("cooccurrence")


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
def cc(cc_module):
    return _OnCopies(cc_module)


def _text(hint):
    """A hint given as a text or as a function that computes it (only when a test fails)."""
    if not callable(hint):
        return hint
    try:
        return hint()
    except Exception:  # noqa: BLE001 - a hint must never hide the failure it explains
        return ""


def _result(call, expected, what="", hint="", on_warning=None):
    """call(), any error other than NotImplementedError being reported with what was expected first; on_warning(text)
    gives the cause of a classic RuntimeWarning."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)
        try:
            return call()
        except NotImplementedError:
            raise                 # a function not written yet: ⏳
        except RuntimeWarning as warning:
            cause = on_warning(str(warning)) if on_warning else ""
            hint = _text(hint)
            hint = f"{hint}; here {cause}" if cause else hint
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


def _show(v):
    """A short text for an array: more than 12 numbers show the first 12 (flattened), then « … »."""
    arr = np.asarray(v, dtype=float)
    if arr.size > 12:
        return np.array2string(arr.ravel()[:12], precision=6, suppress_small=True,
                               max_line_width=10_000).replace("]", " …]") + f" (shape {arr.shape})"
    return np.array2string(arr, precision=6, suppress_small=True, max_line_width=10_000).replace("\n", "")


def _show_any(v):
    """_show for something that may not be an array of numbers."""
    try:
        return _show(v)
    except (TypeError, ValueError):
        return repr(v)


def _same(got, value, rtol=1e-9, atol=1e-12):
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
    except (TypeError, ValueError):
        return ""
    if g.shape != want.shape:
        return f" (shape {g.shape} instead of {want.shape})"
    if np.isnan(g).any():
        return " (the result holds nan)"
    if not (np.array_equal(np.isposinf(g), np.isposinf(want)) and np.array_equal(np.isneginf(g), np.isneginf(want))):
        return " (the infinite entries are not where they are expected, or not of the expected sign)"
    finite = np.isfinite(want)
    if finite.any():
        with np.errstate(all="ignore"):
            return f" (largest gap {float(np.max(np.abs(g[finite] - want[finite]))):.1e})"
    return ""


def _close(got, want, what, rtol=1e-9, atol=1e-12, hint=""):
    want = np.asarray(want, dtype=float)
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


def _float_table(got, shape, what, hint=""):
    if isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape:
        return
    hint = _text(hint)
    pytest.fail(f"expected {what} as a numpy.ndarray of floats of shape {shape}, got {type(got).__name__}"
                + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray) else f" {got!r}")
                + (f" ({hint})" if hint else ""))


def _float(got, what, hint=""):
    if type(got) is float:
        return
    hint = _text(hint)
    pytest.fail(f"expected {what} as a Python float (float(...)), got {type(got).__module__}.{type(got).__name__} "
                f"{got!r}" + (f" ({hint})" if hint else ""))


# --- what the module may use ----------------------------------------------------------------------------------------

def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``logit`` (from scipy.special import logit) → "scipy.special.logit"."""
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
    ("pmi", "scipy.special.xlogy"); ``where`` is the top-level function, or "the module level"."""
    inner = {id(node.value) for node in ast.walk(tree) if isinstance(node, ast.Attribute)}
    uses = []
    for statement in tree.body:
        where = _where(statement)
        for node in ast.walk(statement):
            if not isinstance(node, (ast.Name, ast.Attribute)) or id(node) in inner:
                continue                                  # only the whole chain scipy.special.logit, not scipy.special
            attrs = []
            while isinstance(node, ast.Attribute):
                attrs.append(node.attr)
                node = node.value
            if isinstance(node, ast.Name) and node.id in names:
                uses.append((where, ".".join([names[node.id]] + attrs[::-1])))
    return uses


FORBIDDEN_MODULES = ("scipy", "sklearn")
FORBIDDEN_STRINGS = {"special", "logit", "expit", "xlogy", "optimize", "metrics", "mutual_info_score", "linear_model",
                     "LogisticRegression"}


def _string_uses(tree):
    """getattr(…, "special") and the like, and __import__("scipy") or importlib.import_module("sklearn…"): a forbidden
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
            if name in ("__import__", "import_module") and any(t.startswith(FORBIDDEN_MODULES) for t in texts):
                found.append(f"{name}({texts[0]!r}) in {where}")
    return found


def test_module_uses_numpy_and_math_but_no_scipy_nor_sklearn(cc_module):
    """The docstring allows NumPy and the module math, but no SciPy (scipy.special.logit, xlogy, scipy.optimize) and no
    scikit-learn (mutual_info_score, LogisticRegression): the tests compare your results with them. Only the code
    counts: a comment, a docstring or an import never used is not a use."""
    try:
        tree = ast.parse(inspect.getsource(cc_module))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = [f"{path} in {where}" for where, path in _uses(tree, _imported_names(tree))
             if path.split(".")[0] in FORBIDDEN_MODULES]
    found += _string_uses(tree)
    assert not found, (f"expected NumPy and math only, with no SciPy nor scikit-learn, found {sorted(set(found))} (the "
                       f"tests compare your results with scipy.special.logit, sklearn.metrics.mutual_info_score and "
                       f"LogisticRegression: np.log, np.sum, np.nonzero, np.broadcast_arrays and the @ product are "
                       f"enough)")


# --- pmi ------------------------------------------------------------------------------------------------------------

PMI_HINT = ("PMI(x, y) = ln(p(x, y) / (p(x) p(y))), with p(x) the sum of ROW x (axis=1) and p(y) the sum of COLUMN y "
            "(axis=0), in nats (np.log), computed on the cells where p(x, y) > 0 only; -inf on the other cells (start "
            "from np.full(shape, -np.inf): np.log(0) warns), with no max(0, ·), no clipping and no smoothing")


def _exact_pmi(joint):
    """The PMI of the table as given, in exact rational arithmetic: each float entry is a Fraction (exactly), the
    marginals are exact sums, and math.log is taken of the exact ratio p(x, y) / (p(x) p(y)) = P(Y = y | X = x) / P(Y =
    y), the lift of the rule "x ⇒ y"; -inf where p(x, y) = 0."""
    table = np.asarray(joint, dtype=float)
    cells = [[Fraction(float(v)) for v in row] for row in table]
    rows = [sum(row, Fraction(0)) for row in cells]
    columns = [sum(column, Fraction(0)) for column in zip(*cells)]
    want = np.full(table.shape, -np.inf)
    for i, row in enumerate(cells):
        for j, v in enumerate(row):
            if v > 0:
                want[i, j] = math.log(v / (rows[i] * columns[j]))
    return want


def _pmi_candidates(table):
    """The right table and the tables of classic errors, with their explanation."""
    want = _exact_pmi(table)
    m, n = table.shape
    rows, columns = table.sum(axis=1), table.sum(axis=0)
    positive = table > 0

    def on_positive(values):
        out = np.full(table.shape, -np.inf)
        out[positive] = values[positive]
        return out

    with np.errstate(all="ignore"):
        candidates = [
            (np.where(positive, want, 0.0), "a cell of probability 0 gets -inf, not 0"),
            (want / math.log(2), "the PMI is in nats: np.log, not np.log2 (bits)"),
            (want / math.log(10), "the PMI is in nats: np.log, not np.log10"),
            (np.exp(want), "the logarithm is missing: the PMI is the logarithm of the lift p(x, y) / (p(x) p(y))"),
            (np.maximum(want, 0.0), "no max(0, ·): the PMI is negative where x and y occur together less often than "
                                    "if they were independent, and -inf on a cell of probability 0"),
            (-want, "the ratio is p(x, y) / (p(x) p(y)), not its inverse"),
            (on_positive(np.log(table / rows[:, None])), "divide by p(y) too: ln(p(x, y) / p(x)) is "
                                                         "ln P(Y = y | X = x), not the PMI"),
            (on_positive(np.log(table / columns[None, :])), "divide by p(x) too: ln(p(x, y) / p(y)) is "
                                                            "ln P(X = x | Y = y), not the PMI"),
            (on_positive(np.log(table)), "the marginals are missing: the PMI divides p(x, y) by p(x) p(y)"),
            (want + math.log(m * n), "p(x) and p(y) are the SUMS of a row and of a column (axis=1 and axis=0), not "
                                     "their means"),
        ]
        if m == n:
            candidates.append((on_positive(np.log(table / np.outer(columns, rows))),
                               "p(x) is the sum of ROW x (axis=1) and p(y) the sum of COLUMN y (axis=0): here the two "
                               "marginals are swapped"))
    return want, candidates


def _pmi_hint(got, joint):
    """PMI_HINT, plus the classic error that the result got matches, if any."""
    try:
        g = np.asarray(got, dtype=float)
        table = np.asarray(joint, dtype=float)
    except (TypeError, ValueError):
        return PMI_HINT
    want, candidates = _pmi_candidates(table)
    if g.shape != want.shape:
        if g.shape == want.shape[::-1] and want.shape[0] != want.shape[1]:
            return f"{PMI_HINT}; here the table is transposed: one row per value of X, shape (m, n) = {want.shape}"
        return PMI_HINT
    text = _first_match(g, want, candidates)
    zero = np.isneginf(want)
    if not text and np.isnan(g).any():
        text = ("the result holds nan: in a row or a column of probability 0, p(x) p(y) = 0 and 0 / 0 is nan; compute "
                "the logarithm on the cells where p(x, y) > 0 only")
    elif not text and zero.any() and np.all(g[zero] == 0):
        text = "a cell of probability 0 gets -inf, not 0"
    elif not text and zero.any() and np.isfinite(g[zero]).any():
        text = "a cell of probability 0 gets -inf: add no epsilon to the probabilities and clip nothing"
    return f"{PMI_HINT}; here {text}" if text else PMI_HINT


def _pmi_warning(text):
    if "divide by zero" in text:
        return ("np.log(0) warns: take the logarithm on the cells where p(x, y) > 0 only, and leave -inf on the others "
                "(np.full(shape, -np.inf))")
    if "invalid value" in text:
        return ("0 / 0 in a row or a column of probability 0 (p(x) p(y) = 0): compute the ratio on the cells where "
                "p(x, y) > 0 only")
    return ""


def _pmi(cc, joint, what):
    got = _result(lambda: cc.pmi(joint), "a numpy.ndarray of floats (the table of the PMI)", what, PMI_HINT,
                  _pmi_warning)
    _float_table(got, np.asarray(joint, dtype=float).shape, what, lambda: _pmi_hint(got, joint))
    return got


def _check_pmi(got, joint, what, want=None, rtol=1e-12, atol=1e-12):
    want = _exact_pmi(joint) if want is None else want
    _close(got, want, what, rtol=rtol, atol=atol, hint=lambda: _pmi_hint(got, joint))


def _random_counts(rng, shape, zero_share=0.0, high=40, empty_rows=0, empty_columns=0):
    """A table of integer counts, some cells (and possibly whole rows or columns) at 0, never all 0."""
    m, n = shape
    counts = rng.integers(1, high + 1, size=shape)
    if zero_share:
        counts[rng.random(shape) < zero_share] = 0
    if empty_rows:
        counts[rng.choice(m, size=empty_rows, replace=False), :] = 0
    if empty_columns:
        counts[:, rng.choice(n, size=empty_columns, replace=False)] = 0
    if counts.sum() == 0:
        counts[int(rng.integers(m)), int(rng.integers(n))] = int(rng.integers(1, high + 1))
    return counts


def _show_counts(counts):
    """A table of counts as a list of lists of integers, or its first 12 entries for a large one."""
    counts = np.asarray(counts)
    if counts.size <= 12:
        return str(counts.tolist())
    return str(counts.ravel()[:12].tolist()).replace("]", ", …]") + f" (shape {counts.shape})"


def _random_law(rng, shape, zero_share=0.0):
    """A joint law drawn from a Dirichlet law, some cells at 0, renormalized."""
    p = rng.dirichlet(np.full(shape[0] * shape[1], float(rng.uniform(0.3, 2.0)))).reshape(shape)
    if zero_share:
        p[rng.random(shape) < zero_share] = 0.0
    if p.sum() == 0:
        p[0, 0] = 1.0
    return p / p.sum()


def test_pmi_docstring_examples(cc):
    call = "pmi([[0.4, 0.1], [0.2, 0.3]]) (p(x) = (0.5, 0.5), p(y) = (0.6, 0.4))"
    joint = [[0.4, 0.1], [0.2, 0.3]]
    got = _pmi(cc, joint, call)
    _close(np.round(got, 4), [[0.2877, -0.6931], [-0.4055, 0.4055]], call, rtol=0, atol=1e-12,
           hint=lambda: _pmi_hint(got, joint))
    call = "pmi([[0.5, 0.0], [0.1, 0.4]]) (a cell that never occurs)"
    joint = [[0.5, 0.0], [0.1, 0.4]]
    got = _pmi(cc, joint, call)
    _close(np.round(got, 4), [[0.5108, -np.inf], [-1.0986, 0.6931]], call, rtol=0, atol=1e-12,
           hint=lambda: _pmi_hint(got, joint))


PMI_CASES = [((1, 1), 0.0, 0, 0, "a single cell"), ((1, 5), 0.3, 0, 0, "a single row"),
             ((4, 1), 0.0, 0, 0, "a single column"), ((2, 2), 0.0, 0, 0, "a 2 × 2 table"),
             ((2, 3), 0.25, 0, 0, "a 2 × 3 table with empty cells"), ((3, 4), 0.3, 1, 0, "an empty row"),
             ((5, 5), 0.2, 0, 1, "an empty column"), ((6, 3), 0.3, 1, 1, "an empty row and an empty column"),
             ((8, 9), 0.5, 0, 0, "half of the cells empty"), ((12, 7), 0.1, 2, 0, "two empty rows"),
             ((20, 30), 0.6, 0, 3, "a large sparse table")]


@pytest.mark.parametrize("shape, zeros, empty_rows, empty_columns, text", PMI_CASES,
                         ids=[f"{s[0]}x{s[1]}-{t.replace(' ', '-').replace('×', 'x')}" for s, _, _, _, t in PMI_CASES])
def test_pmi_matches_the_exact_logarithm_of_the_lift(cc, shape, zeros, empty_rows, empty_columns, text):
    """Tables of counts divided by their total (M03): the PMI equals ln(p(x, y) / (p(x) p(y))) computed with fractions
    (the logarithm of the lift P(Y = y | X = x) / P(Y = y)), and -inf on the empty cells."""
    rng = np.random.default_rng(7000 + [c[0] for c in PMI_CASES].index(shape))
    counts = _random_counts(rng, shape, zeros, empty_rows=empty_rows, empty_columns=empty_columns)
    joint = counts / counts.sum()
    what = f"pmi(C / N) for the {shape[0]} × {shape[1]} table of counts C = {_show_counts(counts)} ({text})"
    got = _pmi(cc, joint, what)
    _check_pmi(got, joint, what)


MI_CASES = [((2, 2), 0.0), ((3, 5), 0.2), ((6, 4), 0.35), ((10, 10), 0.5), ((25, 15), 0.7), ((2, 40), 0.3),
            ((1, 6), 0.0)]


@pytest.mark.parametrize("shape, zeros", MI_CASES, ids=[f"{s[0]}x{s[1]}" for s, _ in MI_CASES])
def test_pmi_mean_under_the_joint_law_is_the_mutual_information_in_nats(cc, shape, zeros):
    """Σ p(x, y) PMI(x, y) over the cells where p(x, y) > 0 is the mutual information I(X ; Y) in nats:
    sklearn.metrics.mutual_info_score of the table of counts, and H(X) + H(Y) - H(X, Y) by scipy.stats.entropy. It is
    ≥ 0, although some PMI are negative."""
    rng = np.random.default_rng(7011 + [s for s, _ in MI_CASES].index(shape))
    counts = _random_counts(rng, shape, zeros, high=200)
    joint = counts / counts.sum()
    what = f"pmi(C / N) for the {shape[0]} × {shape[1]} table of counts C = {_show_counts(counts)}"
    got = _pmi(cc, joint, what)
    positive = joint > 0
    with np.errstate(all="ignore"):
        mean = float(np.sum(joint[positive] * got[positive]))
    mi = float(mutual_info_score(None, None, contingency=counts))
    entropies = float(stats.entropy(joint.sum(axis=1)) + stats.entropy(joint.sum(axis=0))
                      - stats.entropy(joint.ravel()))
    assert abs(mi - entropies) <= 1e-10, "oracle: two values of the mutual information"
    assert abs(mean - mi) <= 1e-10, (
        f"expected Σ p(x, y) PMI(x, y) = I(X ; Y) = {mi:.12g} nats (sklearn.metrics.mutual_info_score) for {what}, got "
        f"{mean!r} ({_pmi_hint(got, joint)})")


def test_pmi_is_between_ln_p_and_minus_ln_of_each_marginal(cc):
    """On the cells where p(x, y) > 0: ln p(x, y) ≤ PMI(x, y) ≤ min(-ln p(x), -ln p(y)) (because p(x, y) ≤ p(x), p(y)
    ≤ 1), so the normalized PMI, PMI / (-ln p(x, y)), is between -1 and 1 when p(x, y) < 1."""
    rng = np.random.default_rng(7018)
    for k in range(40):
        shape = (int(rng.integers(1, 9)), int(rng.integers(1, 9)))
        joint = _random_law(rng, shape, zero_share=0.4 if k % 2 else 0.0)
        what = f"pmi(p) for a random {shape[0]} × {shape[1]} joint law p = {_show(joint)}"
        got = _pmi(cc, joint, what)
        positive = joint > 0
        p_x = np.broadcast_to(joint.sum(axis=1)[:, None], shape)[positive]
        p_y = np.broadcast_to(joint.sum(axis=0)[None, :], shape)[positive]
        values, p = got[positive], joint[positive]
        upper = np.minimum(-np.log(p_x), -np.log(p_y))
        lower = np.log(p)
        with np.errstate(all="ignore"):
            above = ~(values <= upper + 1e-12 * (1 + np.abs(upper)))
            below = ~(values >= lower - 1e-12 * (1 + np.abs(lower)))
        assert not above.any(), (
            f"expected PMI(x, y) ≤ min(-ln p(x), -ln p(y)) on every cell of positive probability for {what}, got "
            f"{_show(values[above])} above the bounds {_show(upper[above])} ({_pmi_hint(got, joint)})")
        assert not below.any(), (
            f"expected PMI(x, y) ≥ ln p(x, y) on every cell of positive probability for {what}, got "
            f"{_show(values[below])} below {_show(lower[below])} ({_pmi_hint(got, joint)})")
        rare = p < 1
        if rare.any():
            with np.errstate(all="ignore"):
                normalized = values[rare] / -np.log(p[rare])
            assert np.all(np.abs(normalized) <= 1 + 1e-9), (
                f"expected a normalized PMI, PMI / (-ln p(x, y)), between -1 and 1 for {what}, got "
                f"{_show(normalized)} ({_pmi_hint(got, joint)})")


def test_pmi_bound_is_reached_when_x_occurs_only_with_y(cc):
    """When x occurs only with y, p(x, y) = p(x) and PMI(x, y) = -ln p(y), the largest value the bound allows; when y
    occurs only with x, PMI(x, y) = -ln p(x)."""
    counts = np.array([[0, 0, 7], [11, 5, 9], [3, 13, 2]])
    joint = counts / counts.sum()
    what = f"pmi(C / {counts.sum()}) for C = {counts.tolist()} (the value x0 occurs only with y2)"
    got = _pmi(cc, joint, what)
    _close(got[0, 2], math.log(50 / 18), f"PMI(x0, y2) for {what} (-ln p(y2) = ln(50 / 18))", rtol=1e-12,
           atol=1e-12, hint=lambda: _pmi_hint(got, joint))
    rng = np.random.default_rng(7019)
    for k in range(20):
        shape = (int(rng.integers(2, 8)), int(rng.integers(2, 8)))
        joint = _random_law(rng, shape, zero_share=0.2)
        by_row = k % 2 == 0
        i, j = int(rng.integers(shape[0])), int(rng.integers(shape[1]))
        if by_row:                                # x_i occurs only with y_j
            joint[i, :] = 0.0
            joint[i, j] = float(rng.uniform(0.02, 0.3))
        else:                                     # y_j occurs only with x_i
            joint[:, j] = 0.0
            joint[i, j] = float(rng.uniform(0.02, 0.3))
        joint /= joint.sum()
        marginal = joint.sum(axis=0)[j] if by_row else joint.sum(axis=1)[i]
        text = f"x{i} occurs only with y{j}" if by_row else f"y{j} occurs only with x{i}"
        what = f"pmi(p) for a {shape[0]} × {shape[1]} joint law where {text}, p = {_show(joint)}"
        got = _pmi(cc, joint, what)
        _close(got[i, j], -math.log(marginal), f"PMI(x{i}, y{j}) for {what} (-ln p({'y' if by_row else 'x'}"
               f"{j if by_row else i}))", rtol=1e-12, atol=1e-12, hint=lambda: _pmi_hint(got, joint))


def test_pmi_of_a_diagonal_law_is_minus_ln_p_on_the_diagonal(cc):
    """X = Y: the law diag(p) has PMI(x, x) = -ln p(x) and -inf off the diagonal, and the mean of the PMI is the entropy
    H(X) (scipy.stats.entropy)."""
    rng = np.random.default_rng(7020)
    for K in (1, 2, 5, 9):
        p = rng.dirichlet(np.full(K, 1.5))
        joint = np.diag(p)
        what = f"pmi(diag(p)) for p = {_show(p)}"
        got = _pmi(cc, joint, what)
        want = np.full((K, K), -np.inf)
        want[np.diag_indices(K)] = -np.log(p)
        _close(got, want, what, rtol=1e-12, atol=1e-12, hint=lambda: _pmi_hint(got, joint))
        with np.errstate(all="ignore"):
            mean = float(np.sum(p * np.diag(got)))
        assert abs(mean - float(stats.entropy(p))) <= 1e-12, (
            f"expected Σ p(x) PMI(x, x) = H(X) = {float(stats.entropy(p)):.12g} for {what}, got {mean!r} "
            f"({_pmi_hint(got, joint)})")


def test_pmi_of_the_transposed_law_is_the_transposed_table(cc):
    """Exchanging X and Y (joint.T) transposes the table of the PMI."""
    rng = np.random.default_rng(7021)
    for shape in ((2, 5), (7, 3), (4, 4), (1, 6), (9, 2)):
        joint = _random_law(rng, shape, zero_share=0.3)
        table = _pmi(cc, joint, f"pmi(p) for a random {shape[0]} × {shape[1]} joint law p = {_show(joint)}")
        what = f"pmi(p.T) for a random {shape[0]} × {shape[1]} joint law p = {_show(joint)}"
        got = _pmi(cc, joint.T, what)
        _close(got, np.asarray(table, dtype=float).T, f"{what} (the table of pmi(p), transposed)", rtol=1e-12,
               atol=1e-13, hint=lambda: _pmi_hint(got, joint.T))
        _check_pmi(got, joint.T, what)


def test_pmi_renumbering_the_values_renumbers_the_table(cc):
    """Permuting the rows and the columns of the law (renumbering the values of X and Y) permutes the table."""
    rng = np.random.default_rng(7022)
    for shape in ((3, 3), (5, 8), (10, 4)):
        joint = _random_law(rng, shape, zero_share=0.25)
        rows, columns = rng.permutation(shape[0]), rng.permutation(shape[1])
        table = _pmi(cc, joint, f"pmi(p) for a random {shape[0]} × {shape[1]} joint law")
        permuted = joint[rows][:, columns]
        what = f"pmi(p[rows][:, columns]) for rows = {rows.tolist()}, columns = {columns.tolist()}"
        got = _pmi(cc, permuted, what)
        _close(got, np.asarray(table, dtype=float)[rows][:, columns], f"{what} (the table of pmi(p), permuted)",
               rtol=1e-12, atol=1e-13, hint=lambda: _pmi_hint(got, permuted))


def test_pmi_is_zero_on_a_column_independent_of_the_rows(cc):
    """A column whose cells are p(x) times its total, p(x, y) = p(x) p(y), has a PMI of 0 (here in dyadic numbers, so
    exactly), whatever the other columns; the cells of the other columns keep their own PMI."""
    joint = np.array([[3, 5, 4], [1, 0, 3], [4, 7, 5]]) / 32
    what = "pmi(C / 32) for C = [[3, 5, 4], [1, 0, 3], [4, 7, 5]] (column 0 is p(x) / 4)"
    got = _pmi(cc, joint, what)
    _close(got[:, 0], np.zeros(3), f"the column 0 of {what}", rtol=0, atol=1e-15, hint=lambda: _pmi_hint(got, joint))
    _check_pmi(got, joint, what)
    rng = np.random.default_rng(7023)
    for m, n in ((2, 3), (4, 4), (6, 9)):
        others = _random_law(rng, (m, n - 1), zero_share=0.3)       # the other columns, rescaled to 1 - c
        c = float(rng.uniform(0.05, 0.6))
        others *= 1 - c
        column = others.sum(axis=1) * c / (1 - c)                   # p(x) c: then p(x) = row sum of others / (1 - c)
        j = int(rng.integers(n))
        joint = np.insert(others, j, column, axis=1)
        what = f"pmi(p) for a random {m} × {n} law whose column {j} is independent of the rows, p = {_show(joint)}"
        got = _pmi(cc, joint, what)
        want = np.where(column > 0, 0.0, -np.inf)
        _close(got[:, j], want, f"the column {j} of {what}", rtol=0, atol=1e-12, hint=lambda: _pmi_hint(got, joint))
        _check_pmi(got, joint, what)


def test_pmi_sign_says_whether_x_and_y_occur_together_more_often_than_if_independent(cc):
    """PMI(x, y) > 0 exactly when p(x, y) > p(x) p(y), < 0 when p(x, y) < p(x) p(y) (compared with fractions)."""
    rng = np.random.default_rng(7024)
    for k in range(15):
        shape = (int(rng.integers(2, 7)), int(rng.integers(2, 7)))
        counts = _random_counts(rng, shape, 0.2, high=12)
        N = int(counts.sum())
        joint = counts / N
        what = f"pmi(C / {N}) for C = {counts.tolist()}"
        got = _pmi(cc, joint, what)
        rows, columns = counts.sum(axis=1), counts.sum(axis=0)
        for i, j in zip(*np.nonzero(counts)):
            excess = int(counts[i, j]) * N - int(rows[i]) * int(columns[j])     # N² (p(x, y) - p(x) p(y))
            value = float(got[i, j])
            ok = value > 0 if excess > 0 else value < 0 if excess < 0 else abs(value) <= 1e-12
            relation = ">" if excess > 0 else "<" if excess < 0 else "="
            sign = "> 0" if excess > 0 else "< 0" if excess < 0 else "= 0"
            assert ok, (f"expected PMI(x{i}, y{j}) {sign} for {what} "
                        f"(p(x, y) {relation} p(x) p(y)), got {value!r} ({_pmi_hint(got, joint)})")


ZERO_CELL_CASES = [([[0.0, 0.0], [0.0, 1.0]], "a certain outcome"),
                   (np.array([[5, 0, 2], [0, 0, 0], [6, 0, 7]]) / 20, "an empty row and an empty column"),
                   (np.array([[0, 9, 0, 0], [4, 0, 0, 3], [0, 0, 8, 0]]) / 24, "more empty cells than full ones")]


@pytest.mark.parametrize("joint, text", ZERO_CELL_CASES, ids=["certain", "empty-row-and-column", "mostly-empty"])
def test_pmi_cells_of_probability_0_get_minus_inf_without_a_warning(cc, joint, text):
    """-inf exactly on the cells of probability 0 (also in a row or a column of probability 0), finite values on the
    others, and no RuntimeWarning (np.log(0) and 0 / 0 warn)."""
    what = f"pmi({_show(joint)}) ({text})"
    got = _pmi(cc, joint, what)
    zero = np.asarray(joint) == 0
    assert np.all(np.isneginf(got[zero])) and np.all(np.isfinite(got[~zero])), (
        f"expected -inf exactly on the cells of probability 0 for {what}, got {_show(got)} ({_pmi_hint(got, joint)})")
    _check_pmi(got, joint, what)


def test_pmi_of_random_sparse_laws_has_minus_inf_on_every_empty_cell(cc):
    rng = np.random.default_rng(7025)
    for k in range(12):
        shape = (int(rng.integers(2, 10)), int(rng.integers(2, 10)))
        counts = _random_counts(rng, shape, 0.75, empty_rows=int(k % 3 == 0), empty_columns=int(k % 4 == 0))
        joint = counts / counts.sum()
        what = f"pmi(C / N) for the sparse table of counts C = {_show_counts(counts)}"
        got = _pmi(cc, joint, what)
        _check_pmi(got, joint, what)


@pytest.mark.parametrize("t", [1e-15, 1e-40, 1e-120], ids=["1e-15", "1e-40", "1e-120"])
def test_pmi_does_not_clip_tiny_probabilities(cc, t):
    """A cell of probability t > 0, however small, has a finite PMI, ln(t / (p(x) p(y))): no epsilon added, no clipping
    (only a cell of probability 0 gets -inf)."""
    joint = np.array([[t, 0.29, 0.08 - t], [0.17, 0.0, 0.46]])
    what = f"pmi([[{t:g}, 0.29, 0.08 - {t:g}], [0.17, 0.0, 0.46]])"
    got = _pmi(cc, joint, what)
    _check_pmi(got, joint, what)


@pytest.mark.parametrize("joint, want, text", [
    ([[1.0]], [[0.0]], "a single cell"),
    ([[0.22, 0.0, 0.78]], [[0.0, -np.inf, 0.0]], "a single row: Y is independent of the only value of X"),
    ([[0.35], [0.0], [0.65]], [[0.0], [-np.inf], [0.0]], "a single column"),
], ids=["one-cell", "one-row", "one-column"])
def test_pmi_of_a_single_row_or_column_is_zero(cc, joint, want, text):
    what = f"pmi({joint}) ({text})"
    got = _pmi(cc, joint, what)
    _close(got, want, what, rtol=0, atol=1e-15, hint=lambda: _pmi_hint(got, joint))


@pytest.mark.parametrize("gap", [6e-10, -6e-10], ids=["sum-just-above-1", "sum-just-below-1"])
def test_pmi_accepts_a_law_that_sums_to_1_up_to_1e_9(cc, gap):
    joint = [[0.33, 0.12], [0.2, 0.35 + gap]]
    what = f"pmi([[0.33, 0.12], [0.2, 0.35 {'+' if gap > 0 else '-'} 6e-10]]) (a sum within 1e-9 of 1)"
    got = _pmi(cc, joint, what)
    _check_pmi(got, joint, what, rtol=1e-8, atol=1e-8)


@pytest.mark.parametrize("joint, text", [
    ([[0, 1], [0, 0]], "a list of integers"),
    (np.array([[0, 0, 0], [0, 1, 0]], dtype=np.int64), "an int64 array"),
    ([[Fraction(1, 6), Fraction(1, 3)], [Fraction(5, 12), Fraction(1, 12)]], "a list of fractions"),
    (np.array([[0.375, 0.125], [0.1875, 0.3125]], dtype=np.float32), "a float32 array (dyadic numbers)"),
], ids=["int-list", "int64-array", "fractions", "float32"])
def test_pmi_accepts_integers_fractions_and_float32(cc, joint, text):
    what = f"pmi({joint!r}) ({text})"
    got = _pmi(cc, joint, what)
    _check_pmi(got, np.asarray(joint, dtype=float), what, rtol=1e-6, atol=1e-6)


def test_pmi_does_not_modify_its_input(cc_module):
    joint = np.array([[0.21, 0.0, 0.14], [0.0, 0.0, 0.0], [0.35, 0.18, 0.12]])
    copy = joint.copy()
    _result(lambda: cc_module.pmi(joint), "a table", "pmi(p) for a law with an empty row and empty cells")
    assert np.array_equal(joint, copy), (f"expected p unchanged by pmi(p), got p = {_show(joint)} (never modify the "
                                         f"arrays you receive: p /= ... or p[p == 0] = ... writes into p)")


PMI_REFUSALS = [
    ([0.25, 0.75], "joint is 1-D"), (1.0, "joint is a number, not 2-D"),
    (np.full((2, 2, 2), 0.125), "joint is 3-D (although it sums to 1)"),
    (np.zeros((0, 0)), "joint is empty (0 × 0)"), (np.zeros((0, 3)), "joint has no row"),
    (np.zeros((3, 0)), "joint has no column"), ([], "joint is an empty list"),
    ([[]], "joint is [[]], a row without entries"),
    ([[0.5, 0.25], [0.25]], "joint is a ragged list"), ([["a", 0.5], [0.25, 0.25]], "joint holds a string"),
    (None, "joint is None"), ([[0.65, 0.45], [-0.1, 0.0]], "joint has a negative entry (although it sums to 1)"),
    ([[0.3, np.nan], [0.2, 0.5]], "joint holds nan"), ([[np.inf, 0.0], [0.0, 0.0]], "joint holds an inf"),
    ([[0.5, -np.inf], [np.inf, 0.5]], "joint holds inf and -inf"), ([[0.3, 0.2], [0.1, 0.3]], "joint sums to 0.9"),
    ([[0.45, 0.35], [0.25, 0.05]], "joint sums to 1.1"),
    ([[0.27, 0.18], [0.31, 0.24 + 2e-9]], "joint sums to 1 + 2e-9"),
    ([[0.27, 0.18], [0.31, 0.24 - 2e-9]], "joint sums to 1 - 2e-9"), (np.zeros((2, 3)), "joint is all zeros"),
    ([[3, 1], [2, 6]], "joint holds counts (it sums to 12): a joint law holds probabilities"),
    (np.array([[True, False], [False, False]]), "joint is an array of booleans (although it sums to 1)"),
    ([[False, True], [False, False]], "joint is a list of booleans (although it sums to 1)"),
]
PMI_REFUSAL_IDS = ["one-d", "scalar", "three-d", "empty", "no-row", "no-column", "empty-list", "empty-row", "ragged",
                   "string", "none", "negative", "nan", "inf", "inf-and-minus-inf", "sum-below", "sum-above",
                   "sum-just-above", "sum-just-below", "all-zeros", "counts", "bool-array", "bool-list"]


@pytest.mark.parametrize("joint, why", PMI_REFUSALS, ids=PMI_REFUSAL_IDS)
def test_pmi_refusals(cc, joint, why):
    _expect_error(ValueError, lambda: cc.pmi(joint), f"pmi({joint!r})", why)


# --- case_control_logit ---------------------------------------------------------------------------------------------

LOGIT_HINT = ("ln(n₁ / n₀) - ln(s₁ / s₀), natural logarithms: the logit of the observed proportion MINUS the logarithm "
              "of the ratio of the rates s₁ = keep_positive and s₀ = keep_negative; +inf where only n₁ > 0, -inf where "
              "only n₀ > 0 (np.log(0) warns: treat these cells apart); a Python float when both numbers of examples "
              "are numbers, an array of the broadcast shape otherwise")


def _exact_logit(n1, n0, s1=1.0, s0=1.0):
    """ln(n₁ s₀ / (n₀ s₁)) cell by cell, the ratio computed exactly with fractions (of the floats given); ±inf."""
    a, b = np.broadcast_arrays(np.asarray(n1, dtype=float), np.asarray(n0, dtype=float))
    rates = Fraction(float(s0)) / Fraction(float(s1))
    want = np.empty(a.shape)
    for index in np.ndindex(a.shape):
        x, y = Fraction(float(a[index])), Fraction(float(b[index]))
        want[index] = math.inf if y == 0 else -math.inf if x == 0 else math.log(x / y * rates)
    return want


def _logit_candidates(n1, n0, s1, s0):
    want = _exact_logit(n1, n0, s1, s0)
    a, b = np.broadcast_arrays(np.asarray(n1, dtype=float), np.asarray(n0, dtype=float))
    shift = math.log(float(s1)) - math.log(float(s0))
    with np.errstate(all="ignore"):
        base = np.log(a) - np.log(b)
        candidates = [
            (base + shift, "SUBTRACT ln(s₁ / s₀): the odds observed in the sample are those of the population "
                           "multiplied by s₁ / s₀ (Bayes), so the population logit is the observed one minus "
                           "ln(s₁ / s₀)"),
            (base, "the rates count: subtract ln(s₁ / s₀) = ln(keep_positive / keep_negative) from ln(n₁ / n₀)"),
            (-want, "the logit is ln(n₁ / n₀) - ln(s₁ / s₀): positives over negatives, not its opposite"),
            (-base - shift, "the observed logit is ln(n₁ / n₀), positives over negatives, not ln(n₀ / n₁)"),
            (want / math.log(10), "natural logarithms (np.log, math.log), not log10"),
            (want / math.log(2), "natural logarithms (np.log, math.log), not log2"),
            (np.log(a / (a + b)) - shift, "the logit of the proportion q = n₁ / (n₁ + n₀) is ln(q / (1 - q)) = "
                                          "ln(n₁ / n₀), not ln q"),
            (special.expit(want), "the logit is asked, not the probability σ(logit)"),
        ]
    return want, candidates


def _logit_hint(got, n1, n0, s1=1.0, s0=1.0):
    """LOGIT_HINT, plus the classic error that the result got matches, if any."""
    try:
        want, candidates = _logit_candidates(n1, n0, s1, s0)
        g = np.asarray(got, dtype=float)
    except (TypeError, ValueError):
        return LOGIT_HINT
    text = _first_match(g, want, candidates)
    if not text and g.shape == want.shape:
        if np.isnan(g).any():
            text = ("the result holds nan: where n₁ = 0 or n₀ = 0 a logarithm is -inf and -inf - (-inf) is nan; put "
                    "+inf where only n₁ > 0 and -inf where only n₀ > 0")
        elif np.isinf(want).any() and np.array_equal(np.isposinf(g), np.isneginf(want)):
            text = "+inf where n₀ = 0 (only positives: infinite odds), -inf where n₁ = 0 (odds 0)"
    return f"{LOGIT_HINT}; here {text}" if text else LOGIT_HINT


def _logit_warning(text):
    if "divide by zero" in text:
        return ("np.log(0) (or a division by 0) warns: put +inf where only n₁ > 0 and -inf where only n₀ > 0 directly, "
                "and take the logarithms on the cells where both are positive only")
    if "invalid value" in text:
        return "-inf - (-inf) or 0 / 0 gives nan: treat the cells where n₁ = 0 or n₀ = 0 apart"
    return ""


def _logit(cc, what, n1, n0, s1=None, s0=None):
    """case_control_logit(n1, n0[, keep_positive=s1][, keep_negative=s0]), its type checked: a Python float for two
    numbers, an array of floats of the broadcast shape otherwise."""
    kwargs = {}
    if s1 is not None:
        kwargs["keep_positive"] = s1
    if s0 is not None:
        kwargs["keep_negative"] = s0
    rates = (1.0 if s1 is None else s1, 1.0 if s0 is None else s0)
    got = _result(lambda: cc.case_control_logit(n1, n0, **kwargs), "a logit", what, LOGIT_HINT, _logit_warning)
    if np.ndim(n1) == 0 and not isinstance(n1, np.ndarray) and np.ndim(n0) == 0 and not isinstance(n0, np.ndarray):
        _float(got, what, lambda: _logit_hint(got, n1, n0, *rates))
    else:
        shape = np.broadcast_shapes(np.shape(n1), np.shape(n0))
        _float_table(got, shape, what, lambda: _logit_hint(got, n1, n0, *rates))
    return got


def _check_logit(got, n1, n0, what, s1=1.0, s0=1.0, want=None, rtol=1e-12, atol=1e-12):
    want = _exact_logit(n1, n0, s1, s0) if want is None else want
    _close(got, want, what, rtol=rtol, atol=atol, hint=lambda: _logit_hint(got, n1, n0, s1, s0))


def test_case_control_logit_docstring_examples(cc):
    call = "case_control_logit(45, 10) (everything kept: ln 4.5)"
    got = _logit(cc, call, 45, 10)
    _close(round(got, 4), 1.5041, call, rtol=0, atol=1e-12, hint=lambda: _logit_hint(got, 45, 10))
    call = "case_control_logit(45, 10, keep_negative=0.25) (one negative in 4 kept: ln(4.5 / 4))"
    got = _logit(cc, call, 45, 10, s0=0.25)
    _close(round(got, 4), 0.1178, call, rtol=0, atol=1e-12, hint=lambda: _logit_hint(got, 45, 10, 1.0, 0.25))
    call = "case_control_logit([2, 0, 5], [2, 7, 0])"
    got = _logit(cc, call, [2, 0, 5], [2, 7, 0])
    _close(got, [0.0, -np.inf, np.inf], call, rtol=0, atol=1e-15, hint=lambda: _logit_hint(got, [2, 0, 5], [2, 7, 0]))


def test_case_control_logit_with_both_rates_1_is_the_logit_of_the_observed_proportion(cc):
    """Nothing dropped: ln(n₁ / n₀) = logit(n₁ / (n₁ + n₀)), scipy.special.logit of the observed proportion, and the
    exact logarithm of the ratio (fractions); the default rates are 1, and giving them as 1 changes nothing."""
    rng = np.random.default_rng(7030)
    n1 = rng.integers(1, 5000, size=25)
    n0 = rng.integers(1, 5000, size=25)
    for a, b in zip(n1.tolist(), n0.tolist()):
        what = f"case_control_logit({a}, {b})"
        got = _logit(cc, what, a, b)
        _close(got, special.logit(a / (a + b)), f"{what} (scipy.special.logit({a} / {a + b}))", rtol=1e-9, atol=1e-9,
               hint=lambda: _logit_hint(got, a, b))
        _check_logit(got, a, b, what)
        what = f"case_control_logit({a}, {b}, keep_positive=1, keep_negative=1.0)"
        got = _logit(cc, what, a, b, 1, 1.0)
        _check_logit(got, a, b, what)


LR_CASES = [(23, 377, 1.0, 0.125), (148, 61, 0.5, 1.0), (6, 1487, 1.0, 0.04), (95, 230, 0.8, 0.3)]


@pytest.mark.parametrize("n1, n0, s1, s0", LR_CASES, ids=[f"{a}-{b}" for a, b, _, _ in LR_CASES])
def test_case_control_logit_matches_logistic_regression_on_the_sample_minus_ln_of_the_rates(cc, n1, n0, s1, s0):
    """A logistic regression with a constant feature only (sklearn LogisticRegression, no penalty), fitted on the labels
    of the sample (n₁ ones, n₀ zeros), has the coefficient ln(n₁ / n₀) (M13a); the population logit is that coefficient
    minus ln(s₁ / s₀)."""
    labels = np.r_[np.ones(n1), np.zeros(n0)]
    model = LogisticRegression(penalty=None, fit_intercept=False, solver="newton-cg", tol=1e-12, max_iter=1000)
    model.fit(np.ones((n1 + n0, 1)), labels)
    fitted = float(model.coef_[0, 0])
    want = fitted - math.log(s1 / s0)
    what = f"case_control_logit({n1}, {n0}, keep_positive={s1}, keep_negative={s0})"
    got = _logit(cc, what, n1, n0, s1, s0)
    _close(got, want, f"{what} (LogisticRegression on the sample: {fitted:.10g}, minus ln({s1} / {s0}))", rtol=1e-8,
           atol=1e-8, hint=lambda: _logit_hint(got, n1, n0, s1, s0))


def test_case_control_logit_matches_the_exact_corrected_logit(cc):
    """Random numbers of examples and rates k / m in ]0, 1]: ln(n₁ s₀ / (n₀ s₁)), the ratio computed with fractions."""
    rng = np.random.default_rng(7031)
    for k in range(30):
        a = int(rng.integers(1, 20000))
        b = int(rng.integers(1, 20000))
        s1 = float(rng.integers(1, 41)) / 40 if k % 3 else 1.0
        s0 = float(rng.integers(1, 101)) / 100 if k % 4 else 1.0
        what = f"case_control_logit({a}, {b}, keep_positive={s1!r}, keep_negative={s0!r})"
        got = _logit(cc, what, a, b, s1, s0)
        _check_logit(got, a, b, what, s1, s0)


def test_case_control_logit_finds_the_population_back_when_exact_fractions_are_kept(cc):
    """A population of P₁ positives and P₀ negatives, of which exactly the fractions s₁ and s₀ are kept: n₁ = s₁ P₁ and
    n₀ = s₀ P₀ (not always integers). The corrected logit is that of the population, logit(P₁ / (P₁ + P₀))
    (scipy.special.logit)."""
    rng = np.random.default_rng(7032)
    for k in range(20):
        population = (int(rng.integers(50, 100000)), int(rng.integers(50, 100000)))
        s1, s0 = float(rng.uniform(0.01, 1.0)), float(rng.uniform(0.01, 1.0))
        if k % 2:
            s1 = 1.0
        n1, n0 = s1 * population[0], s0 * population[1]
        want = float(special.logit(population[0] / sum(population)))
        what = (f"case_control_logit({n1!r}, {n0!r}, keep_positive={s1!r}, keep_negative={s0!r}) (a population of "
                f"{population[0]} positives and {population[1]} negatives)")
        got = _logit(cc, what, n1, n0, s1, s0)
        _close(got, want, f"{what} (the logit of the population, logit({population[0]} / {sum(population)}))",
               rtol=1e-9, atol=1e-9, hint=lambda: _logit_hint(got, n1, n0, s1, s0))


def test_case_control_logit_of_a_sample_drawn_at_random_estimates_the_population_logit(cc):
    """Constat: 270 000 visits, each a purchase with probability 0.05; every purchase kept, each other visit kept with
    probability s₀ = 0.08 (a fixed seed). The corrected logit lies within 5 standard errors (√(1/n₁ + 1/n₀)) of the
    logit of the population; the logit of the sample, ln(n₁ / n₀), is about ln(1 / 0.08) ≈ 2.5 too high."""
    rng = np.random.default_rng(7040)
    purchase = rng.random(270_000) < 0.05
    kept = purchase | (rng.random(purchase.size) < 0.08)
    population = (int(purchase.sum()), int((~purchase).sum()))
    n1, n0 = int((kept & purchase).sum()), int((kept & ~purchase).sum())
    truth = math.log(population[0] / population[1])
    error = math.sqrt(1 / n1 + 1 / n0)
    assert abs(math.log(n1 / n0) - truth) > 20 * error, "oracle: the sample logit is far from the population"
    what = f"case_control_logit({n1}, {n0}, keep_negative=0.08) (every purchase kept, one other visit in 12.5)"
    got = _logit(cc, what, n1, n0, s0=0.08)
    assert abs(got - truth) <= 5 * error, (
        f"expected {what} within 5 standard errors ({5 * error:.3g}) of the population logit {truth:.6g}, got {got!r} "
        f"({_logit_hint(got, n1, n0, 1.0, 0.08)})")


def test_case_control_logit_is_unchanged_when_both_counts_or_both_rates_are_scaled(cc):
    """Only the ratios count: (c n₁, c n₀) gives the same logit as (n₁, n₀), and (c s₁, c s₀) as (s₁, s₀)."""
    rng = np.random.default_rng(7033)
    n1 = rng.integers(0, 300, size=12).astype(float)
    n0 = rng.integers(1, 300, size=12).astype(float)
    base = _logit(cc, "case_control_logit(n1, n0, 0.6, 0.15) for random arrays n1, n0", n1, n0, 0.6, 0.15)
    for c in (1e-3, 7.5, 2e6):
        what = f"case_control_logit({c:g} n1, {c:g} n0, 0.6, 0.15) for n1 = {_show(n1)}, n0 = {_show(n0)}"
        got = _logit(cc, what, c * n1, c * n0, 0.6, 0.15)
        _close(got, base, f"{what} (the logit of (n1, n0))", rtol=1e-12, atol=1e-12,
               hint=lambda: _logit_hint(got, c * n1, c * n0, 0.6, 0.15))
    for c in (0.5, 0.01):
        what = f"case_control_logit(n1, n0, {0.6 * c:g}, {0.15 * c:g}) for n1 = {_show(n1)}, n0 = {_show(n0)}"
        got = _logit(cc, what, n1, n0, 0.6 * c, 0.15 * c)
        _close(got, base, f"{what} (the logit with the rates 0.6 and 0.15)", rtol=1e-12, atol=1e-12,
               hint=lambda: _logit_hint(got, n1, n0, 0.6 * c, 0.15 * c))


def test_case_control_logit_swapping_the_labels_gives_the_opposite(cc):
    """Calling the negatives positive (n₁ ↔ n₀, s₁ ↔ s₀) changes the logit into its opposite, +inf into -inf."""
    rng = np.random.default_rng(7034)
    n1 = rng.integers(0, 50, size=20).astype(float)
    n0 = rng.integers(0, 50, size=20).astype(float)
    n0[(n1 == 0) & (n0 == 0)] = 3.0
    for s1, s0 in ((1.0, 1.0), (0.3, 0.85), (1.0, 0.05)):
        straight = _logit(cc, f"case_control_logit(n1, n0, {s1}, {s0})", n1, n0, s1, s0)
        what = f"case_control_logit(n0, n1, {s0}, {s1}) for n1 = {_show(n1)}, n0 = {_show(n0)}"
        got = _logit(cc, what, n0, n1, s0, s1)
        _close(got, -np.asarray(straight, dtype=float), f"{what} (the opposite of case_control_logit(n1, n0, {s1}, "
               f"{s0}))", rtol=1e-12, atol=1e-12, hint=lambda: _logit_hint(got, n0, n1, s0, s1))
        _check_logit(got, n0, n1, what, s0, s1)


def test_case_control_logit_moves_every_group_by_the_same_ln_of_the_rates(cc):
    """Several groups (one cell each): with the same rates for every group, each logit moves by -ln(s₁ / s₀) from the
    logit with nothing dropped, so the differences between groups do not move (only the intercept of a logistic model
    moves)."""
    rng = np.random.default_rng(7035)
    n1 = rng.integers(1, 400, size=6).astype(float)
    n0 = rng.integers(1, 400, size=6).astype(float)
    observed = _logit(cc, "case_control_logit(n1, n0) for six groups", n1, n0)
    for s1, s0 in ((1.0, 0.1), (0.25, 1.0), (0.65, 0.4)):
        what = f"case_control_logit(n1, n0, {s1}, {s0}) for six groups, n1 = {_show(n1)}, n0 = {_show(n0)}"
        got = _logit(cc, what, n1, n0, s1, s0)
        with np.errstate(all="ignore"):
            shift = np.asarray(got, dtype=float) - np.asarray(observed, dtype=float)
        _close(shift, np.full(6, -math.log(s1 / s0)), f"the shift from case_control_logit(n1, n0) of {what} "
               f"(-ln({s1} / {s0}) for every group)", rtol=1e-12, atol=1e-12,
               hint=lambda: _logit_hint(got, n1, n0, s1, s0))


def test_case_control_logit_grows_with_n1_and_s0_and_decreases_with_n0_and_s1(cc):
    n1 = np.array([[0.5], [3.0], [17.0], [260.0]])
    n0 = np.array([1.0, 8.0, 45.0])
    grid = _logit(cc, "case_control_logit(n1, n0) for n1 of shape (4, 1) and n0 of shape (3,)", n1, n0)
    _check_logit(grid, n1, n0, "case_control_logit(n1, n0) for n1 = [[0.5], [3], [17], [260]], n0 = [1, 8, 45]")
    assert np.all(np.diff(grid, axis=0) > 0) and np.all(np.diff(grid, axis=1) < 0), (
        f"expected a logit that grows with n₁ (down the rows) and decreases with n₀ (along the columns), got "
        f"{_show(grid)} ({_logit_hint(grid, n1, n0)})")
    rates = (0.05, 0.3, 1.0)
    by_s1 = [_logit(cc, f"case_control_logit(19, 7, keep_positive={s})", 19, 7, s1=s) for s in rates]
    by_s0 = [_logit(cc, f"case_control_logit(19, 7, keep_negative={s})", 19, 7, s0=s) for s in rates]
    assert by_s1[0] > by_s1[1] > by_s1[2] and by_s0[0] < by_s0[1] < by_s0[2], (
        f"expected a logit that decreases with s₁ and grows with s₀ (keeping more positives makes the population "
        f"logit lower), got {by_s1} for s₁ = {rates} and {by_s0} for s₀ = {rates} ({LOGIT_HINT})")


INFINITE_CASES = [((8, 0, 0.5, 0.2), math.inf, "only positives"), ((0, 13, 0.5, 0.2), -math.inf, "only negatives"),
                  ((0.25, 0.0, 1.0, 1.0), math.inf, "a quarter of a positive"),
                  ((0, 6, 0.01, 1.0), -math.inf, "no positive although s₁ is small")]


@pytest.mark.parametrize("args, want, text", INFINITE_CASES, ids=["plus-inf", "minus-inf", "small-plus-inf",
                                                                    "minus-inf-small-rate"])
def test_case_control_logit_is_infinite_when_a_class_is_absent(cc, args, want, text):
    """+inf when n₁ > 0 and n₀ = 0, -inf when n₁ = 0 and n₀ > 0, whatever the rates, as a Python float and without a
    RuntimeWarning."""
    n1, n0, s1, s0 = args
    what = f"case_control_logit({n1}, {n0}, {s1}, {s0}) ({text})"
    got = _logit(cc, what, n1, n0, s1, s0)
    _close(got, want, what, rtol=0, atol=0, hint=lambda: _logit_hint(got, n1, n0, s1, s0))


def test_case_control_logit_arrays_mixing_finite_and_infinite_cells(cc):
    n1 = np.array([[3.0, 0.0, 12.0], [0.0, 5.5, 1.0]])
    n0 = np.array([[9.0, 4.0, 0.0], [2.0, 0.0, 1.0]])
    what = f"case_control_logit(n1, n0, 0.75, 0.3) for n1 = {n1.tolist()}, n0 = {n0.tolist()}"
    got = _logit(cc, what, n1, n0, 0.75, 0.3)
    _check_logit(got, n1, n0, what, 0.75, 0.3)


BROADCAST_CASES = [([4, 9, 0.5], 3, None, None), (11, [[2], [5]], 0.4, 0.9), ([[2], [9], [0]], [3.5, 7], None, 0.35),
                   (np.arange(1, 7).reshape(2, 3), np.array([[4], [9]]), 0.2, None), ([7], 2, None, None),
                   (np.ones((2, 1, 3)), np.full((4, 1), 3.0), 0.5, 0.5)]


@pytest.mark.parametrize("n1, n0, s1, s0", BROADCAST_CASES, ids=["list-and-number", "number-and-column",
                                                                 "column-and-row", "row-arrays", "one-cell-list",
                                                                 "three-d"])
def test_case_control_logit_broadcasts_its_two_numbers_of_examples(cc, n1, n0, s1, s0):
    """Two arrays (or lists, or an array and a number) are combined cell by cell with NumPy broadcasting: an array of
    the broadcast shape, also for a list of a single number."""
    what = f"case_control_logit({n1!r}, {n0!r}" + (f", keep_positive={s1}" if s1 else "") + \
           (f", keep_negative={s0}" if s0 else "") + ")"
    got = _logit(cc, what, n1, n0, s1, s0)
    _check_logit(got, n1, n0, what, s1 or 1.0, s0 or 1.0)


NUMBER_CASES = [(29, 4, None, None, "two Python ints"), (29.0, 4.5, 0.5, None, "two Python floats"),
                (np.int64(29), np.int64(4), None, 0.25, "two np.int64"),
                (np.float64(29), np.float32(4.5), np.float64(0.5), np.float32(0.25), "NumPy floats, float32 rates"),
                (np.int32(29), 4, 1, None, "an np.int32 and an int, the rate the int 1")]


@pytest.mark.parametrize("n1, n0, s1, s0, text", NUMBER_CASES, ids=["ints", "floats", "int64", "numpy-floats",
                                                                    "int32"])
def test_case_control_logit_returns_a_python_float_for_two_numbers(cc, n1, n0, s1, s0, text):
    what = f"case_control_logit({n1!r}, {n0!r}" + (f", keep_positive={s1!r}" if s1 is not None else "") + \
           (f", keep_negative={s0!r}" if s0 is not None else "") + f") ({text})"
    got = _logit(cc, what, n1, n0, s1, s0)
    _check_logit(got, n1, n0, what, 1.0 if s1 is None else s1, 1.0 if s0 is None else s0)


def test_case_control_logit_accepts_numbers_of_examples_that_are_not_integers(cc):
    """Finite numbers ≥ 0, not only integers: weighted or rescaled numbers of examples."""
    for n1, n0, s1, s0 in ((2.5, 0.625, 1.0, 1.0), (1e-3, 4e-3, 0.7, 0.2), (1e12, 3e11, 0.05, 1.0)):
        what = f"case_control_logit({n1!r}, {n0!r}, {s1}, {s0})"
        got = _logit(cc, what, n1, n0, s1, s0)
        _check_logit(got, n1, n0, what, s1, s0)


def test_case_control_logit_does_not_modify_its_inputs(cc_module):
    n1 = np.array([4.0, 0.0, 19.0, 7.5])
    n0 = np.array([12.0, 3.0, 0.0, 2.0])
    copies = n1.copy(), n0.copy()
    _result(lambda: cc_module.case_control_logit(n1, n0, 0.4, 0.8), "an array of logits",
            "case_control_logit(n1, n0, 0.4, 0.8)")
    assert np.array_equal(n1, copies[0]) and np.array_equal(n0, copies[1]), (
        f"expected n1 and n0 unchanged by case_control_logit, got n1 = {_show(n1)}, n0 = {_show(n0)} (never modify the "
        f"arrays you receive: n1 /= ... or n1[n1 == 0] = ... writes into n1)")


COUNT_REFUSALS = [
    ((-1, 5), "n_positive is negative"), ((4, -0.5), "n_negative is negative"), ((np.nan, 5), "n_positive is nan"),
    ((4, np.inf), "n_negative is inf"), ((-np.inf, 5), "n_positive is -inf"), ((True, 5), "n_positive is True, a bool"),
    ((4, False), "n_negative is False, a bool"), ((np.True_, 5), "n_positive is np.True_, a NumPy bool"),
    ((np.array([True, False]), [3, 4]), "n_positive is an array of booleans"),
    (([3, 4], [[True], [False]]), "n_negative is a list of booleans"),
    ((0, 0), "both numbers are 0: nothing was observed"), ((0.0, 0), "both numbers are 0.0 and 0"),
    (([5, 0, 2], [1, 0, 3]), "both are 0 in the second cell"),
    (([1, 2, 3], [1, 2]), "the shapes (3,) and (2,) do not broadcast"),
    ((np.ones((2, 3)), np.ones((3, 2))), "the shapes (2, 3) and (3, 2) do not broadcast"),
    ((["a", 2], [1, 1]), "n_positive holds a string"), ((None, 4), "n_positive is None"),
    (([2, np.nan], [1, 1]), "n_positive holds nan"), (([2, 3], [1, -1]), "n_negative holds a negative number"),
]
COUNT_REFUSAL_IDS = ["negative-positives", "negative-negatives", "nan", "inf", "minus-inf", "true", "false",
                     "numpy-bool", "bool-array", "bool-list", "both-zero", "both-zero-float", "both-zero-in-a-cell",
                     "no-broadcast", "no-broadcast-2d", "string", "none", "nan-in-array", "negative-in-array"]


@pytest.mark.parametrize("args, why", COUNT_REFUSALS, ids=COUNT_REFUSAL_IDS)
def test_case_control_logit_refuses_bad_numbers_of_examples(cc, args, why):
    _expect_error(ValueError, lambda: cc.case_control_logit(*args), f"case_control_logit({args[0]!r}, {args[1]!r})",
                  why)


RATE_REFUSALS = [({"keep_positive": 0}, "s₁ = 0"), ({"keep_negative": 0.0}, "s₀ = 0.0"),
                 ({"keep_positive": -0.3}, "s₁ is negative"), ({"keep_negative": 1.0001}, "s₀ is above 1"),
                 ({"keep_positive": 2}, "s₁ = 2"), ({"keep_negative": np.inf}, "s₀ is inf"),
                 ({"keep_positive": np.nan}, "s₁ is nan"),
                 ({"keep_negative": np.float64("nan")}, "s₀ is np.float64(nan)"),
                 ({"keep_positive": True}, "s₁ is True, a bool (True == 1, but a bool is refused)"),
                 ({"keep_negative": False}, "s₀ is False, a bool"),
                 ({"keep_positive": np.True_}, "s₁ is np.True_, a NumPy bool")]


@pytest.mark.parametrize("kwargs, why", RATE_REFUSALS, ids=["s1-zero", "s0-zero", "s1-negative", "s0-above-1",
                                                            "s1-two", "s0-inf", "s1-nan", "s0-numpy-nan", "s1-true",
                                                            "s0-false", "s1-numpy-bool"])
def test_case_control_logit_refuses_bad_rates(cc, kwargs, why):
    args = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
    _expect_error(ValueError, lambda: cc.case_control_logit(22, 9, **kwargs), f"case_control_logit(22, 9, {args})",
                  why)


# --- remove_direction -----------------------------------------------------------------------------------------------

REMOVE_HINT = ("each row x becomes x - (x·u / u·u) u: the coefficients X @ u / (u @ u), one per row (u need not have "
               "norm 1), then subtract coefficient × u from each row (np.outer(coefficients, u), or broadcasting); the "
               "vectors are the ROWS of X, and a 1-D X gives a 1-D result")


def _rows(X):
    X = np.asarray(X, dtype=float)
    return X.reshape(1, -1) if X.ndim == 1 else X


def _lstsq_residual(X, u):
    """The residual of the least squares fit of each row x by c u (np.linalg.lstsq), and the coefficients c."""
    X, u = np.asarray(X, dtype=float), np.asarray(u, dtype=float)
    rows = _rows(X)
    coefficients = np.linalg.lstsq(u.reshape(-1, 1), rows.T, rcond=None)[0][0]
    return (rows - np.outer(coefficients, u)).reshape(X.shape), coefficients


def _removal_candidates(X, u):
    X, u = np.asarray(X, dtype=float), np.asarray(u, dtype=float)
    rows = _rows(X)
    want, c = _lstsq_residual(X, u)
    uu = float(u @ u)
    candidates = [
        (rows - np.outer(rows @ u, u), "divide by u·u: the coefficient is x·u / u·u (u need not have norm 1)"),
        (rows - np.outer(rows @ u / math.sqrt(uu), u), "divide by u·u = ‖u‖², not by ‖u‖"),
        (np.outer(c, u), "the result is x MINUS its projection (x·u / u·u) u on the line, not the projection"),
        (rows + np.outer(c, u), "SUBTRACT (x·u / u·u) u from x, do not add it"),
    ]
    if rows.shape[0] == rows.shape[1] and rows.shape[0] > 1:
        candidates.append((rows - np.outer(u, rows.T @ u / uu), "the vectors are the ROWS of X: one coefficient "
                                                                "x·u / u·u per row (X @ u), not per column"))
    return want, [(value.reshape(X.shape), text) for value, text in candidates]


def _removal_hint(got, X, u):
    """REMOVE_HINT, plus the classic error that the result got matches, if any."""
    try:
        want, candidates = _removal_candidates(X, u)
        g = np.asarray(got, dtype=float)
    except (TypeError, ValueError, np.linalg.LinAlgError):
        return REMOVE_HINT
    if g.shape != want.shape:
        if want.ndim == 1 and g.shape == (1, want.size):
            return f"{REMOVE_HINT}; here a 1-D X of shape {want.shape} gave the shape {g.shape}"
        return REMOVE_HINT
    text = _first_match(g, want, candidates, rtol=1e-8, atol=1e-10 * max(1.0, float(np.max(np.abs(want)))))
    return f"{REMOVE_HINT}; here {text}" if text else REMOVE_HINT


def _removed(cc, X, u, what):
    got = _result(lambda: cc.remove_direction(X, u), "a numpy.ndarray of floats of the shape of X", what, REMOVE_HINT)
    _float_table(got, np.asarray(X, dtype=float).shape, what, lambda: _removal_hint(got, X, u))
    return got


def _scale(X, u=None):
    """The size of the entries, for the absolute tolerances."""
    return max(1.0, float(np.max(np.abs(np.asarray(X, dtype=float)))))


def _check_removed(got, X, u, what, rtol=1e-9):
    want, _ = _lstsq_residual(X, u)
    _close(got, want, f"{what} (the residual of np.linalg.lstsq)", rtol=rtol, atol=1e-12 * _scale(X),
           hint=lambda: _removal_hint(got, X, u))


def test_remove_direction_docstring_examples(cc):
    call = "remove_direction([3.0, 1.0], [1.0, 1.0])"
    got = _removed(cc, [3.0, 1.0], [1.0, 1.0], call)
    _close(got, [1.0, -1.0], call, rtol=0, atol=1e-15, hint=lambda: _removal_hint(got, [3.0, 1.0], [1.0, 1.0]))
    call = "remove_direction([[2, 0, 1], [1, 1, 1]], [0, 0, 5]) (the third coordinate is removed)"
    X, u = [[2, 0, 1], [1, 1, 1]], [0, 0, 5]
    got = _removed(cc, X, u, call)
    _close(got, [[2.0, 0.0, 0.0], [1.0, 1.0, 0.0]], call, rtol=0, atol=1e-15, hint=lambda: _removal_hint(got, X, u))


REMOVE_CASES = [((1,), 1.0), ((2,), 1.0), ((7,), 3.0), ((1, 1), 1.0), ((1, 4), 1.0), ((5, 1), 2.0), ((2, 2), 1.0),
                ((4, 3), 0.5), ((10, 5), 40.0), ((30, 8), 1.0), ((200, 16), 0.01), ((3, 50), 1.0)]


@pytest.mark.parametrize("shape, scale", REMOVE_CASES, ids=["x".join(map(str, s)) for s, _ in REMOVE_CASES])
def test_remove_direction_is_the_residual_of_least_squares_on_u(cc, shape, scale):
    """Random X (one vector, or the rows of a matrix) and u: each row minus c u, with c the least squares coefficient
    of the row on u (np.linalg.lstsq); a 1-D X gives a 1-D result."""
    rng = np.random.default_rng(7060 + [s for s, _ in REMOVE_CASES].index(shape))
    X = (rng.normal(size=shape) + rng.normal(size=shape[-1])) * scale
    u = rng.normal(size=shape[-1]) * float(rng.uniform(0.2, 5.0))
    what = f"remove_direction(X, u) for X of shape {shape} = {_show(X)} and u = {_show(u)}"
    got = _removed(cc, X, u, what)
    _check_removed(got, X, u, what)


def test_remove_direction_is_the_projection_on_the_complement_of_u(cc):
    """X N Nᵀ, where the columns of N are an orthonormal basis of the vectors orthogonal to u (scipy.linalg.null_space):
    the orthogonal projection on the complement of the line (M12b)."""
    rng = np.random.default_rng(7072)
    for shape in ((6, 4), (3, 9), (12, 2)):
        X = rng.normal(size=shape) * 2.0
        u = rng.normal(size=shape[1])
        N = linalg.null_space(u[None, :])
        what = f"remove_direction(X, u) for X of shape {shape} and u = {_show(u)}"
        got = _removed(cc, X, u, what)
        _close(got, X @ N @ N.T, f"{what} (X N Nᵀ, N an orthonormal basis of the complement of u)", rtol=1e-9,
               atol=1e-12 * _scale(X), hint=lambda: _removal_hint(got, X, u))


def test_remove_direction_with_integers_matches_exact_fractions(cc):
    """Integer X and u: x - (x·u / u·u) u computed with fractions."""
    rng = np.random.default_rng(7073)
    for k in range(10):
        n, d = int(rng.integers(1, 6)), int(rng.integers(2, 7))
        X = rng.integers(-9, 10, size=(n, d))
        u = rng.integers(-5, 6, size=d)
        if not np.any(u):
            u[0] = 3
        uu = sum(int(v) * int(v) for v in u)
        want = np.array([[Fraction(int(x[j])) - Fraction(sum(int(a) * int(b) for a, b in zip(x, u)), uu) * int(u[j])
                          for j in range(d)] for x in X], dtype=float)
        what = f"remove_direction({X.tolist()}, {u.tolist()})"
        got = _removed(cc, X, u, what)
        _close(got, want, f"{what} (computed with fractions)", rtol=1e-12, atol=1e-12,
               hint=lambda: _removal_hint(got, X, u))


def test_remove_direction_rows_of_the_result_are_orthogonal_to_u(cc):
    rng = np.random.default_rng(7074)
    for k in range(15):
        d = int(rng.integers(2, 12))
        X = rng.normal(size=(int(rng.integers(1, 20)), d)) * float(rng.uniform(0.1, 50))
        u = rng.normal(size=d) * float(rng.uniform(0.05, 20))
        what = f"remove_direction(X, u) for X of shape {X.shape} and u = {_show(u)}"
        got = _removed(cc, X, u, what)
        dots = got @ u
        bound = 1e-12 * np.linalg.norm(u) * np.maximum(1.0, np.linalg.norm(X, axis=1))
        assert np.all(np.abs(dots) <= bound), (
            f"expected rows orthogonal to u (r·u = 0) for {what}, got r·u = {_show(dots)} ({_removal_hint(got, X, u)})")


def test_remove_direction_twice_changes_nothing(cc):
    """The projection is idempotent: removing u from a result that no longer has it gives the same result."""
    rng = np.random.default_rng(7075)
    for shape in ((4,), (5, 3), (40, 10)):
        X = rng.normal(size=shape) * 3.0
        u = rng.normal(size=shape[-1])
        once = _removed(cc, X, u, f"remove_direction(X, u) for X of shape {shape}")
        what = f"remove_direction(remove_direction(X, u), u) for X of shape {shape} and u = {_show(u)}"
        got = _removed(cc, once, u, what)
        _close(got, once, f"{what} (the result of the first removal)", rtol=1e-9, atol=1e-12 * _scale(X),
               hint=lambda: _removal_hint(once, X, u))


def test_remove_direction_keeps_what_is_orthogonal_to_u_and_removes_a_multiple_of_u(cc):
    """For every v orthogonal to u, r·v = x·v (the columns of scipy.linalg.null_space); and x - r is c u, with c the
    least squares coefficient of x on u."""
    rng = np.random.default_rng(7076)
    for shape in ((7, 5), (2, 8)):
        X = rng.normal(size=shape) * 4.0
        u = rng.normal(size=shape[1]) * 0.3
        N = linalg.null_space(u[None, :])
        what = f"remove_direction(X, u) for X of shape {shape} and u = {_show(u)}"
        got = _removed(cc, X, u, what)
        _close(got @ N, X @ N, f"the components orthogonal to u of {what} (r·v = x·v)", rtol=1e-9,
               atol=1e-12 * _scale(X), hint=lambda: _removal_hint(got, X, u))
        _, c = _lstsq_residual(X, u)
        _close(X - got, np.outer(c, u), f"X minus {what} (c u for each row, c by np.linalg.lstsq)", rtol=1e-9,
               atol=1e-12 * _scale(X), hint=lambda: _removal_hint(got, X, u))


def test_remove_direction_distances_lose_only_their_part_along_u(cc):
    """Pythagoras: ‖x - y‖² = ‖r_x - r_y‖² + ((x - y)·u)² / (u·u) for every pair of rows (scipy.spatial.distance)."""
    rng = np.random.default_rng(7077)
    for shape in ((6, 3), (15, 7)):
        X = rng.normal(size=shape) * 5.0
        u = rng.normal(size=shape[1]) * 2.0
        what = f"remove_direction(X, u) for X of shape {shape} and u = {_show(u)}"
        got = _removed(cc, X, u, what)
        along = distance.pdist((X @ u / np.linalg.norm(u))[:, None], "sqeuclidean")
        want = distance.pdist(X, "sqeuclidean") - along
        _close(distance.pdist(got, "sqeuclidean"), want, f"the squared distances between the rows of {what} "
               f"(‖x - y‖² - ((x - y)·u)² / (u·u))", rtol=1e-9, atol=1e-10 * _scale(X) ** 2,
               hint=lambda: _removal_hint(got, X, u))


def test_remove_direction_rows_parallel_to_u_become_zero(cc):
    rng = np.random.default_rng(7078)
    u = rng.normal(size=6) * 1.7
    c = np.array([2.5, -0.4, 0.0, 13.0, -7.25])
    X = np.outer(c, u)
    what = f"remove_direction(X, u) for rows c_i u, c = {c.tolist()}, u = {_show(u)}"
    got = _removed(cc, X, u, what)
    _close(got, np.zeros_like(X), what, rtol=0, atol=1e-13 * _scale(X), hint=lambda: _removal_hint(got, X, u))


@pytest.mark.parametrize("c", [-1.0, -3.5, 1e-6, 2e5, 0.125, 1e-100, 1e100],
                         ids=["minus-1", "minus-3.5", "1e-6", "2e5", "0.125", "1e-100", "1e100"])
def test_remove_direction_with_c_u_gives_the_same_result(cc, c):
    """u need not have norm 1, and c u (c ≠ 0, negative or tiny or huge) gives the same result as u."""
    rng = np.random.default_rng(7079)
    X = rng.normal(size=(8, 5)) * 6.0
    u = rng.normal(size=5)
    what = f"remove_direction(X, {c:g} u) for X of shape (8, 5) and u = {_show(u)}"
    got = _removed(cc, X, c * u, what)
    want, _ = _lstsq_residual(X, u)
    _close(got, want, f"{what} (the result for u)", rtol=1e-9, atol=1e-12 * _scale(X),
           hint=lambda: _removal_hint(got, X, c * u))


def test_remove_direction_is_linear_and_works_row_by_row(cc):
    """remove(a X + b Y) = a remove(X) + b remove(Y), and permuting the rows of X permutes the rows of the result."""
    rng = np.random.default_rng(7080)
    X, Y = rng.normal(size=(9, 4)), rng.normal(size=(9, 4)) * 3.0
    u = rng.normal(size=4)
    rX = _removed(cc, X, u, "remove_direction(X, u) for X of shape (9, 4)")
    rY = _removed(cc, Y, u, "remove_direction(Y, u) for Y of shape (9, 4)")
    for a, b in ((2.0, -0.5), (-1.25, 3.0)):
        what = f"remove_direction({a} X + {b} Y, u) for X and Y of shape (9, 4)"
        got = _removed(cc, a * X + b * Y, u, what)
        _close(got, a * rX + b * rY, f"{what} ({a} remove_direction(X, u) + {b} remove_direction(Y, u))", rtol=1e-9,
               atol=1e-12 * _scale(a * X + b * Y), hint=lambda: _removal_hint(got, a * X + b * Y, u))
    order = rng.permutation(9)
    what = f"remove_direction(X[order], u) for order = {order.tolist()}"
    got = _removed(cc, X[order], u, what)
    _close(got, rX[order], f"{what} (the rows of remove_direction(X, u), permuted)", rtol=1e-12, atol=1e-14,
           hint=lambda: _removal_hint(got, X[order], u))


def test_remove_direction_commutes_with_an_orthogonal_change_of_basis(cc):
    """For an orthogonal matrix R (scipy.linalg.qr of a random matrix), removing u R from the rows of X R gives the
    result for X and u, times R: the projection does not depend on the axes."""
    rng = np.random.default_rng(7081)
    for d in (3, 6):
        R, _ = linalg.qr(rng.normal(size=(d, d)))
        X = rng.normal(size=(5, d)) * 2.0
        u = rng.normal(size=d)
        base = _removed(cc, X, u, f"remove_direction(X, u) for X of shape (5, {d})")
        what = f"remove_direction(X R, u R) for X of shape (5, {d}) and an orthogonal R"
        got = _removed(cc, X @ R, u @ R, what)
        _close(got, base @ R, f"{what} (remove_direction(X, u) R)", rtol=1e-9, atol=1e-12 * _scale(X),
               hint=lambda: _removal_hint(got, X @ R, u @ R))


@pytest.mark.parametrize("d, c", [(4, 1.0), (7, 2.5), (5, -0.2)], ids=["d4", "d7-scaled", "d5-negative"])
def test_remove_direction_of_all_ones_centers_each_vector(cc, d, c):
    """Removing the direction (c, …, c) subtracts from each row the mean of its coordinates (M20): every row of the
    result sums to 0."""
    rng = np.random.default_rng(7082)
    X = rng.normal(size=(6, d)) * 3.0 + rng.uniform(-10, 10, size=(6, 1))
    u = np.full(d, c)
    what = f"remove_direction(X, {_show(u)}) for X of shape (6, {d})"
    got = _removed(cc, X, u, what)
    _close(got, X - X.mean(axis=1, keepdims=True), f"{what} (each row minus the mean of its coordinates)", rtol=1e-9,
           atol=1e-12 * _scale(X), hint=lambda: _removal_hint(got, X, u))


def test_remove_direction_in_dimension_1_gives_zero(cc):
    """In dimension 1 every vector is parallel to u: everything becomes 0."""
    X = np.array([[3.5], [-1.25], [0.0], [31.75]])
    for given, u, text in ((X, [-2.5], "4 rows of length 1"), ([6.5], [0.5], "a vector of length 1")):
        what = f"remove_direction({np.asarray(given).tolist()}, {u}) ({text})"
        got = _removed(cc, given, u, what)
        _close(got, np.zeros(np.shape(given)), what, rtol=0, atol=1e-13 * _scale(given),
               hint=lambda: _removal_hint(got, given, u))


def test_remove_direction_along_an_axis_zeroes_that_coordinate(cc):
    """u = c e_k: the coordinate k becomes 0, the others do not change."""
    rng = np.random.default_rng(7083)
    X = rng.normal(size=(5, 4)) * 7.0
    for k, c in ((1, -3.0), (3, 0.6)):
        u = np.zeros(4)
        u[k] = c
        what = f"remove_direction(X, {u.tolist()}) for X of shape (5, 4)"
        got = _removed(cc, X, u, what)
        want = X.copy()
        want[:, k] = 0.0
        _close(got, want, f"{what} (X with its column {k} set to 0)", rtol=1e-12, atol=1e-13 * _scale(X),
               hint=lambda: _removal_hint(got, X, u))


@pytest.mark.parametrize("X, u, text", [
    ([[4, -1, 0], [2, 2, 7]], [1, 0, -1], "lists of integers"),
    (np.array([[3, 5], [-2, 6], [1, 1]], dtype=np.int64), np.array([2, -1], dtype=np.int64), "int64 arrays"),
    (np.array([[0.5, 1.25, -2.0]], dtype=np.float32), np.array([0.75, 0.0, 1.5], dtype=np.float32),
     "float32 arrays (dyadic numbers)"),
    ([7, -4, 2, 1], [np.int64(2), np.int64(3), np.int64(0), np.int64(-1)], "a list of NumPy integers for u"),
], ids=["int-lists", "int64", "float32", "numpy-ints"])
def test_remove_direction_accepts_lists_integers_and_float32(cc, X, u, text):
    what = f"remove_direction({np.asarray(X).tolist()}, {np.asarray(u).tolist()}) ({text})"
    got = _removed(cc, X, u, what)
    _check_removed(got, X, u, what, rtol=1e-6)


def test_remove_direction_does_not_modify_its_inputs(cc_module):
    X = np.array([[1.25, -2.0, 3.5], [0.25, 3.0, -1.0]])
    u = np.array([2.0, 1.0, -3.0])
    for given in (X, X[0]):
        copies = given.copy(), u.copy()
        _result(lambda: cc_module.remove_direction(given, u), "an array", "remove_direction(X, u)")
        assert np.array_equal(given, copies[0]) and np.array_equal(u, copies[1]), (
            f"expected X and u unchanged by remove_direction, got X = {_show(given)}, u = {_show(u)} (never modify the "
            f"arrays you receive: X -= ... or u /= ... writes into them)")


REMOVE_REFUSALS = [
    (np.ones((2, 2, 2)), [1.0, 0.0], "X is 3-D"), (3.0, [1.0], "X is a number, not 1-D or 2-D"),
    ([], [], "X is an empty list"), (np.zeros((0, 3)), [1.0, 2.0, 0.5], "X has no row"),
    ([[]], [], "X is [[]], a row without entries"), ([[1.5, 2.0], [0.5]], [1.0, 1.0], "X is a ragged list"),
    ([[1.25, -3.5]], [[1.0, 0.5]], "u is 2-D"), ([[1.25, -3.5]], 2.0, "u is a number"),
    ([4.0], 2.0, "u is a number, not 1-D (even when d = 1)"),
    ([[3.0], [-4.5]], [[2.0]], "u is 2-D (1 × 1), not 1-D (even when d = 1)"),
    ([[1.25, -3.5, 0.5]], [2.0, 0.5], "u is shorter than the rows of X"),
    ([[1.25, -3.5]], [2.0, 0.5, 0.0], "u is longer than the rows of X"),
    ([1.25, -3.5, 0.5], [2.0, 0.5], "X is 1-D of length 3 and u of length 2"),
    ([[1.25, -3.5], [0.5, 4.5]], [0.0, 0.0], "u is zero (u·u = 0)"),
    ([[1.25, -3.5], [0.5, 4.5]], [-0.0, 0.0], "u is zero (-0.0 and 0.0)"),
    ([[1.0, np.nan]], [1.0, 1.0], "X holds nan"), ([[1.0, np.inf]], [1.0, 1.0], "X holds inf"),
    ([[1.25, -3.5]], [np.nan, 1.0], "u holds nan"), ([[1.25, -3.5]], [1.0, -np.inf], "u holds -inf"),
    (np.array([[True, False], [False, True]]), [1.0, 1.0], "X is an array of booleans"),
    ([[1.25, -3.5]], [True, False], "u is a list of booleans"), ([["a", 2.0]], [1.0, 1.0], "X holds a string"),
    ([[1.25, -3.5]], None, "u is None"), (None, [2.0, 0.5], "X is None"),
]
REMOVE_REFUSAL_IDS = ["x-three-d", "x-scalar", "x-empty", "x-no-row", "x-empty-row", "x-ragged", "u-two-d", "u-scalar",
                      "u-scalar-d1", "u-one-by-one", "u-short", "u-long", "u-wrong-length-1d", "u-zero", "u-minus-zero",
                      "x-nan", "x-inf", "u-nan", "u-minus-inf", "x-bool", "u-bool", "x-string", "u-none", "x-none"]


@pytest.mark.parametrize("X, u, why", REMOVE_REFUSALS, ids=REMOVE_REFUSAL_IDS)
def test_remove_direction_refusals(cc, X, u, why):
    _expect_error(ValueError, lambda: cc.remove_direction(X, u), f"remove_direction({X!r}, {u!r})", why)
