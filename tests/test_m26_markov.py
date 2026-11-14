"""Tests of mymath.markov (chapter M26): the law of a Markov chain after n steps, its stationary law, and the values of
a fixed policy, solved as a linear system or approached by iterating the Bellman operator.

Oracles: ``np.linalg.matrix_power`` for μ₀Pⁿ; ``np.linalg.eig`` on Pᵀ (the eigenvector of the eigenvalue 1) and
``scipy.linalg.null_space(Pᵀ - I)`` (its dimension says whether π is unique) for the stationary law;
``scipy.linalg.solve`` on (I - γP) V = r and the Neumann series Σ γᵗPᵗr truncated for the values; the closed form
V + (γP)ᵏ (V₀ - V) (``np.linalg.matrix_power``) and the partial sums Σ_{t<k} γᵗPᵗr for the iterates. Never another
function of yours. Plus properties: μ_n is a law, Chapman-Kolmogorov, a canonical μ₀ gives a row of Pⁿ, πP = π with
π a law, a periodic chain with a unique π, two closed classes refused, the zero of a transient state, V = r + γPV, a
row that ends equal to an absorbing state of zero reward (γ < 1), discounting equal to ending with the probability
1 - γ, γ = 1 with a sure end (on well-conditioned cases, cond(I - P) ≤ 1e8) and refused without one, each iterate
from the previous one, the a priori bound γᵏ ‖V₀ - V‖∞, inputs left unchanged, arrays of floats, lists of integers,
and the refusals of the docstrings. They describe the expected behaviour without showing the solution.

    pytest tests/test_m26_markov.py              # your code
    pytest tests/test_m26_markov.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings

import numpy as np
import pytest
from scipy import linalg as sla


@pytest.fixture
def mk_module(mymath_module):
    """The module itself: for the tests that check that your functions never write into the arrays they receive, and
    for the check of what the module uses."""
    return mymath_module("markov")


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
def mk(mk_module):
    return _OnCopies(mk_module)


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
    pytest.fail(f"expected {what} to raise {error.__name__} ({why}), but it returned {_show_any(result)}")


def _show(v):
    """A short text for an array: more than 8 numbers show the first 8 (flattened), then « … »."""
    arr = np.asarray(v, dtype=float)
    if arr.size > 8:
        return np.array2string(arr.ravel()[:8], precision=6, suppress_small=True,
                               max_line_width=10_000).replace("]", " …]") + (
            f" (shape {arr.shape})")
    return np.array2string(arr, precision=6, suppress_small=True, max_line_width=10_000).replace("\n", "")


def _show_any(v):
    """_show for something that may not be an array of numbers."""
    try:
        return _show(v)
    except (TypeError, ValueError):
        return repr(v)


def _float_array(got, shape, what, hint=""):
    assert isinstance(got, np.ndarray) and got.dtype.kind == "f" and got.shape == shape, (
        f"expected {what} as a numpy.ndarray of floats of shape {shape}, got {type(got).__name__}"
        + (f" of dtype {got.dtype} and shape {got.shape}" if isinstance(got, np.ndarray) else "")
        + (f" ({hint})" if hint else ""))


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


def _matches(got, value, rtol=1e-9, atol=1e-11):
    """Whether the result got equals the value of a classic error (same shape, close)."""
    if value is None:
        return False
    try:
        got, value = np.asarray(got, dtype=float), np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        return False
    return got.shape == value.shape and bool(np.all(np.isfinite(value))) and np.allclose(got, value, rtol=rtol,
                                                                                         atol=atol)


def _first_match(got, want, candidates, rtol=1e-9, atol=1e-11):
    """The text of the first classic error whose value got matches (and that differs from the right value), or ""."""
    for value, text in candidates:
        if value is not None and not _matches(value, want, rtol, atol) and _matches(got, value, rtol, atol):
            return text
    return ""


def _stochastic(rng, m, alpha=1.0, zeros=0.0):
    """A random stochastic (m, m) matrix with Dirichlet rows; with ``zeros``, about that fraction of the entries are
    set to 0 (never those of the cycle i → i + 1, so the chain stays irreducible), and the rows are renormalized."""
    P = rng.dirichlet(np.full(m, alpha), size=m)
    if zeros:
        mask = rng.random((m, m)) < zeros
        mask[np.arange(m), (np.arange(m) + 1) % m] = False
        P = np.where(mask, 0.0, P)
        P = P / P.sum(axis=1, keepdims=True)
    return P


def _substochastic(rng, m, low=0.05, high=0.4, alpha=1.0):
    """A random substochastic (m, m) matrix: row i is a Dirichlet row times 1 - e_i, e_i uniform in [low, high] (the
    probability that the process ends after state i)."""
    end = rng.uniform(low, high, size=m)
    return rng.dirichlet(np.full(m, alpha), size=m) * (1.0 - end)[:, None]


def _with_absorbing_state(P, r):
    """The same process with an extra absorbing state m of reward 0: the missing mass of each row goes to it."""
    P, r = np.asarray(P, dtype=float), np.asarray(r, dtype=float)
    m = P.shape[0]
    big = np.zeros((m + 1, m + 1))
    big[:m, :m] = P
    big[:m, m] = np.maximum(1.0 - P.sum(axis=1), 0.0)       # a row summing to 1 + 1e-16 sends nothing (not -1e-16)
    big[m, m] = 1.0
    return big, np.append(r, 0.0)


# --- the oracles ----------------------------------------------------------------------------------------------------

def _mp(P, n):
    return np.linalg.matrix_power(np.asarray(P, dtype=float), n)


def _n_step_oracle(P, mu0, n):
    """μ₀ Pⁿ, Pⁿ by np.linalg.matrix_power."""
    return np.asarray(mu0, dtype=float) @ _mp(P, n)


def _stationary_eig(P):
    """The eigenvector of Pᵀ for the eigenvalue closest to 1 (np.linalg.eig), divided by its sum."""
    w, v = np.linalg.eig(np.asarray(P, dtype=float).T)
    k = int(np.argmin(np.abs(w - 1.0)))
    pi = np.real(v[:, k])
    return pi / pi.sum()


def _null_space(P):
    """scipy.linalg.null_space(Pᵀ - I): one column exactly when the stationary law is unique."""
    P = np.asarray(P, dtype=float)
    return sla.null_space(P.T - np.eye(P.shape[0]))


def _stationary_null_space(P):
    """The single column of null_space(Pᵀ - I), divided by its sum."""
    N = _null_space(P)
    assert N.shape[1] == 1, f"oracle: a unique stationary law was expected, null_space has {N.shape[1]} columns"
    return N[:, 0] / N[:, 0].sum()


def _bellman_oracle(P, r, gamma):
    """(I - γP) V = r by scipy.linalg.solve."""
    P = np.asarray(P, dtype=float)
    return sla.solve(np.eye(P.shape[0]) - gamma * P, np.asarray(r, dtype=float))


def _neumann(P, r, gamma):
    """Σ_{t<T} γᵗ Pᵗ r, T large enough for the rest, at most γᵀ ‖r‖∞ / (1 - γ), to be below 1e-17 ‖r‖∞."""
    P, r = np.asarray(P, dtype=float), np.asarray(r, dtype=float)
    T = 1 if gamma == 0 else math.ceil(math.log(1e-17 * (1 - gamma)) / math.log(gamma)) + 1
    total, term = np.zeros_like(r), r.copy()
    for _ in range(T):
        total = total + term
        term = gamma * (P @ term)
    return total


def _iterates_closed_form(P, r, gamma, V0, N):
    """V_k = V + (γP)ᵏ (V₀ - V), V by scipy.linalg.solve and (γP)ᵏ by np.linalg.matrix_power."""
    P, V0 = np.asarray(P, dtype=float), np.asarray(V0, dtype=float)
    V = _bellman_oracle(P, r, gamma)
    return np.array([V + _mp(gamma * P, k) @ (V0 - V) for k in range(N + 1)])


def _iterates_series(P, r, gamma, N):
    """From V₀ = 0: V_k = Σ_{t<k} γᵗ Pᵗ r, each Pᵗ by np.linalg.matrix_power (valid for every γ, even 1)."""
    r = np.asarray(r, dtype=float)
    terms = [gamma ** t * (_mp(P, t) @ r) for t in range(N)]
    return np.array([np.sum(terms[:k], axis=0) if k else np.zeros_like(r) for k in range(N + 1)])


def _iterates_loop(P, r, gamma, V0, N, step):
    """Iterates by a given step (the classic errors): row 0 is V0, row k + 1 is step(row k)."""
    rows = [np.asarray(V0, dtype=float)]
    for _ in range(N):
        rows.append(step(rows[-1]))
    return np.array(rows)


# --- what the module may use ------------------------------------------------------------------------------------

def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``solve`` (from numpy.linalg import solve) → "numpy.linalg.solve"."""
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
    ("bellman_linear_solve", "numpy.linalg.solve"); ``where`` is the top-level function, or "the module level"."""
    inner = {id(node.value) for node in ast.walk(tree) if isinstance(node, ast.Attribute)}
    uses = []
    for statement in tree.body:
        where = _where(statement)
        for node in ast.walk(statement):
            if not isinstance(node, (ast.Name, ast.Attribute)) or id(node) in inner:
                continue                                  # only the whole chain np.linalg.solve, not np.linalg
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


def _getattr_uses(tree, forbidden):
    """getattr(…, "matrix_power") and the like: a forbidden name reached through a string."""
    found = []
    for statement in tree.body:
        where = _where(statement)
        for node in ast.walk(statement):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "getattr"
                    and any(isinstance(a, ast.Constant) and a.value in forbidden for a in node.args)):
                found.append(f"getattr(…, {next(a.value for a in node.args if isinstance(a, ast.Constant))!r}) in "
                             f"{where}")
    return found


ALLOWED_LINALG = ("solve", "matrix_rank")
SOLVERS = ("stationary_distribution", "bellman_linear_solve")
NO_SOLVE = ("n_step_distribution", "bellman_fixed_point_iterates")


def test_module_uses_solve_and_matrix_rank_only_in_stationary_distribution_and_bellman_linear_solve_and_no_scipy(
        mk_module):
    """The docstring allows NumPy, but from np.linalg only solve and matrix_rank, in stationary_distribution and
    bellman_linear_solve (with the helpers of the module that they call); not np.linalg.matrix_power, eig, eigvals,
    inv nor any other function of np.linalg, and no SciPy at all. n_step_distribution and
    bellman_fixed_point_iterates compute by products only: they do not call the two functions that solve. Only the
    code counts: a comment, a docstring or an import never used is not a use. ``np.linalg.LinAlgError`` (an
    exception, not a computation) is not counted."""
    try:
        tree = ast.parse(inspect.getsource(mk_module))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    functions = {n.name: n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    allowed = set().union(*(_reachable(functions, name) for name in SOLVERS)) - set(NO_SOLVE)
    found = []
    for where, path in _uses(tree, _imported_names(tree)):
        parts = path.split(".")
        shown = ".".join(["np"] + parts[1:]) if parts[0] == "numpy" else path
        if parts[0] == "scipy":
            found.append(f"{shown} in {where}")
        elif parts[0] == "numpy" and len(parts) > 2 and parts[1] == "linalg":
            if parts[2] == "LinAlgError" or (parts[2] in ALLOWED_LINALG and where in allowed):
                continue
            found.append(f"{shown} in {where}")
    found += _getattr_uses(tree, {"matrix_power", "eig", "eigvals", "eigh", "eigvalsh", "inv", "pinv", "lstsq", "det",
                                  "null_space"})
    for caller in NO_SOLVE:
        for callee in SOLVERS:
            if callee in _reachable(functions, caller):
                found.append(f"{caller} calls {callee}, which solves a system")
    assert not found, (f"expected NumPy with, from np.linalg, only solve and matrix_rank in stationary_distribution "
                       f"and bellman_linear_solve, and no SciPy at all, found {sorted(set(found))} (the tests compare "
                       f"your results with np.linalg.matrix_power, np.linalg.eig, scipy.linalg.null_space and "
                       f"scipy.linalg.solve: μ₀Pⁿ and the iterates are products mu @ P and P @ V)")


# --- n_step_distribution --------------------------------------------------------------------------------------------

N_STEP_HINT = ("μ_{k+1} = μ_k P: a law is a ROW and one step is mu @ P (Σ_i μ_k[i] P[i, j]), n times from μ_0; "
               "μ_0 itself for n = 0")


def _n_step_hint(got, P, mu0, n):
    """N_STEP_HINT, plus the classic error that the law got matches, if any."""
    P, mu0 = np.asarray(P, dtype=float), np.asarray(mu0, dtype=float)
    m = P.shape[0]
    want = _n_step_oracle(P, mu0, n)
    if isinstance(got, np.ndarray) and got.shape == (n + 1, m) and n > 0:
        return f"{N_STEP_HINT}; here the n + 1 laws μ_0 … μ_n were returned: return μ_n only, of shape ({m},)"
    if isinstance(got, np.ndarray) and got.shape == (m, m) and m > 1:
        return f"{N_STEP_HINT}; here a matrix was returned: return the law μ_0 Pⁿ, of shape ({m},), not Pⁿ"
    with np.errstate(all="ignore"):
        candidates = [
            (_mp(P, n) @ mu0, "the column convention P @ mu was used: a law is a row, one step is mu @ P"),
            (mu0 @ _mp(P, n - 1) if n >= 1 else None, "n - 1 steps were made: μ_n = μ_0 Pⁿ takes n products"),
            (mu0 @ _mp(P, n + 1), "n + 1 steps were made: μ_n = μ_0 Pⁿ takes n products, and n = 0 gives μ_0"),
            (mu0 @ (P ** n), "P ** n raises each entry to the power n: Pⁿ is the matrix product P @ P @ … @ P"),
            (mu0 @ P if n > 1 else None, "only one step was made: repeat mu = mu @ P n times"),
        ]
    text = _first_match(got, want, candidates)
    return f"{N_STEP_HINT}; here {text}" if text else N_STEP_HINT


def test_n_step_distribution_docstring_examples(mk):
    P = [[0.5, 0.5, 0.0], [0.25, 0.5, 0.25], [0.0, 0.5, 0.5]]
    call = "n_step_distribution(P, [1, 0, 0], 2), P = [[0.5, 0.5, 0.0], [0.25, 0.5, 0.25], [0.0, 0.5, 0.5]]"
    got = _result(lambda: mk.n_step_distribution(P, [1, 0, 0], 2), "array([0.375, 0.5, 0.125])", call)
    _float_array(got, (3,), call)
    _close(got, [0.375, 0.5, 0.125], call, rtol=0, atol=1e-15, hint=_n_step_hint(got, P, [1, 0, 0], 2))
    call = "n_step_distribution(P, [0, 0, 1], 0)"
    got = _result(lambda: mk.n_step_distribution(P, [0, 0, 1], 0), "array([0., 0., 1.])", call)
    _float_array(got, (3,), call, "for n = 0, the entries of μ_0 as floats: [0, 0, 1] is a list of integers")
    _close(got, [0.0, 0.0, 1.0], call, rtol=0, atol=0, hint=_n_step_hint(got, P, [0, 0, 1], 0))


N_STEP_CASES = [(1, 4, "one state"), (2, 1, "one step"), (2, 7, "two states, 7 steps"), (3, 12, "three states"),
                (4, 25, "four states, 25 steps"), (5, 3, "five states"), (7, 40, "seven states, sparse"),
                (12, 60, "twelve states")]


@pytest.mark.parametrize("m, n, text", N_STEP_CASES, ids=[f"m{m}-n{n}" for m, n, _ in N_STEP_CASES])
def test_n_step_distribution_matches_matrix_power(mk, m, n, text):
    """μ_n = μ₀ Pⁿ, Pⁿ by np.linalg.matrix_power, for random chains (not symmetric: P @ mu differs) and random μ₀."""
    i = N_STEP_CASES.index((m, n, text))
    rng = np.random.default_rng(6100 + i)
    P = _stochastic(rng, m, alpha=0.7, zeros=0.4 if "sparse" in text else 0.0)
    mu0 = rng.dirichlet(np.ones(m))
    what = f"n_step_distribution(P, mu0, {n}) for {text}"
    got = _result(lambda: mk.n_step_distribution(P, mu0, n), f"an array of shape ({m},)", what)
    _float_array(got, (m,), what, hint=_n_step_hint(got, P, mu0, n))
    _close(got, _n_step_oracle(P, mu0, n), f"{what}, mu0 @ np.linalg.matrix_power(P, {n})", rtol=1e-9, atol=1e-13,
           hint=_n_step_hint(got, P, mu0, n))


def test_n_step_distribution_is_a_law(mk):
    """Each μ_n has entries ≥ 0 that sum to 1 (within 1e-12), whatever the chain and the number of steps."""
    rng = np.random.default_rng(6108)
    for m, n in ((3, 5), (6, 31), (9, 200), (4, 1000)):
        P = _stochastic(rng, m, alpha=0.4, zeros=0.3)
        mu0 = rng.dirichlet(np.full(m, 0.5))
        what = f"n_step_distribution(P, mu0, {n}) for a random chain with {m} states"
        got = _result(lambda: mk.n_step_distribution(P, mu0, n), f"a law of {m} entries", what)
        _float_array(got, (m,), what, hint=_n_step_hint(got, P, mu0, n))
        assert np.all(got >= 0) and abs(float(np.sum(got)) - 1.0) <= 1e-12, (
            f"expected a law (entries >= 0, sum 1 within 1e-12) for {what}, got {_show(got)} of sum "
            f"{float(np.sum(got)):.15g} ({_n_step_hint(got, P, mu0, n)})")
        _close(got, _n_step_oracle(P, mu0, n), what, rtol=1e-9, atol=1e-12, hint=_n_step_hint(got, P, mu0, n))


def test_n_step_distribution_from_a_canonical_vector_is_a_row_of_P_power_n(mk):
    """Starting in i for sure (μ₀ = e_i), μ_n is the row i of Pⁿ (np.linalg.matrix_power): the probabilities of the
    paths of n steps from i."""
    rng = np.random.default_rng(6109)
    m = 5
    P = _stochastic(rng, m, alpha=0.6, zeros=0.3)
    for n in (1, 2, 6):
        Pn = _mp(P, n)
        for i in range(m):
            e = np.eye(m)[i]
            what = f"n_step_distribution(P, e_{i}, {n}) for a random chain with {m} states"
            got = _result(lambda: mk.n_step_distribution(P, e, n), f"the row {i} of P^{n}", what)
            _float_array(got, (m,), what)
            _close(got, Pn[i], f"{what}, the row {i} of np.linalg.matrix_power(P, {n})", rtol=1e-10, atol=1e-14,
                   hint=_n_step_hint(got, P, e, n) + ("; the row i of Pⁿ, not its column i" if _matches(got, Pn[:, i])
                                                       else ""))


def test_n_step_distribution_satisfies_chapman_kolmogorov(mk):
    """P^(a+b) = P^a P^b: a steps then b steps from the law reached are a + b steps (and the rows e_i Pⁿ, stacked,
    give P^(a+b) = P^a P^b), each also checked against np.linalg.matrix_power."""
    rng = np.random.default_rng(6110)
    m = 6
    P = _stochastic(rng, m, alpha=0.5)
    mu0 = rng.dirichlet(np.ones(m))
    for a, b in ((1, 1), (3, 4), (10, 7), (0, 5)):
        first = _result(lambda: mk.n_step_distribution(P, mu0, a), "a law", f"n_step_distribution(P, mu0, {a})")
        _float_array(first, (m,), f"n_step_distribution(P, mu0, {a})")
        both = _result(lambda: mk.n_step_distribution(P, first, b), "a law",
                       f"n_step_distribution(P, n_step_distribution(P, mu0, {a}), {b})")
        whole = _result(lambda: mk.n_step_distribution(P, mu0, a + b), "a law",
                        f"n_step_distribution(P, mu0, {a + b})")
        _close(both, whole, f"{b} steps from μ_{a} (Chapman-Kolmogorov), the same as n_step_distribution(P, mu0, "
                            f"{a + b})", rtol=1e-10, atol=1e-14, hint=_n_step_hint(whole, P, mu0, a + b))
        _close(whole, _n_step_oracle(P, mu0, a + b), f"n_step_distribution(P, mu0, {a + b})", rtol=1e-10, atol=1e-14,
               hint=_n_step_hint(whole, P, mu0, a + b))
    rows = {n: np.array([_result(lambda: mk.n_step_distribution(P, np.eye(m)[i], n), "a law",
                                 f"n_step_distribution(P, e_{i}, {n})") for i in range(m)]) for n in (2, 3, 5)}
    _close(rows[5], rows[2] @ rows[3], "the rows n_step_distribution(P, e_i, 5) stacked, equal to P² P³ built from "
                                       "the same function", rtol=1e-10, atol=1e-14, hint=N_STEP_HINT)


def test_n_step_distribution_converges_to_the_stationary_law_or_oscillates_when_periodic(mk):
    """An irreducible aperiodic chain forgets its start: after 3000 steps, μ_n is the stationary law (np.linalg.eig on
    Pᵀ) from any start. A periodic chain does not converge: μ_n alternates."""
    rng = np.random.default_rng(6111)
    m = 5
    P = _stochastic(rng, m, alpha=1.0)
    pi = _stationary_eig(P)
    for start in (np.eye(m)[0], np.eye(m)[m - 1], rng.dirichlet(np.ones(m))):
        what = "n_step_distribution(P, mu0, 3000) for a random chain with 5 states"
        got = _result(lambda: mk.n_step_distribution(P, start, 3000), "the stationary law", what)
        _float_array(got, (m,), what)
        _close(got, pi, f"{what}, the stationary law (np.linalg.eig on Pᵀ)", rtol=1e-8, atol=1e-11,
               hint=_n_step_hint(got, P, start, 3000))
    walk = np.array([[0.0, 1.0, 0.0, 0.0], [0.45, 0.0, 0.55, 0.0], [0.0, 0.15, 0.0, 0.85], [0.0, 0.0, 1.0, 0.0]])
    for n in (1001, 1000):
        want = _n_step_oracle(walk, np.eye(4)[0], n)
        what = f"n_step_distribution(walk, e_0, {n}) for a walk on a path with reflecting ends (period 2)"
        got = _result(lambda: mk.n_step_distribution(walk, np.eye(4)[0], n), "a law", what)
        _float_array(got, (4,), what)
        _close(got, want, f"{what}: after an {'odd' if n % 2 else 'even'} number of steps, only the "
                          f"{'odd' if n % 2 else 'even'} states", rtol=1e-9, atol=1e-12,
               hint=_n_step_hint(got, walk, np.eye(4)[0], n))


def test_n_step_distribution_zero_steps_gives_mu0_as_a_new_float_array(mk_module):
    mk = mk_module
    mu0 = np.array([0.2, 0.3, 0.5])
    P = np.array([[0.1, 0.6, 0.3], [0.7, 0.2, 0.1], [0.25, 0.25, 0.5]])
    got = _result(lambda: mk.n_step_distribution(P, mu0, 0), "mu0", "n = 0")
    _float_array(got, (3,), "n_step_distribution(P, mu0, 0)")
    _close(got, mu0, "n_step_distribution(P, mu0, 0), μ_0 itself (no step)", rtol=0, atol=0,
           hint=_n_step_hint(got, P, mu0, 0))
    got[...] = 7.0
    assert np.array_equal(mu0, [0.2, 0.3, 0.5]), (
        "expected n_step_distribution(P, mu0, 0) to return a new array, but changing it changed mu0 (return a float "
        "copy of mu0)")
    got = _result(lambda: mk.n_step_distribution([[1]], [1], 0), "array([1.])", "n_step_distribution([[1]], [1], 0)")
    _float_array(got, (1,), "n_step_distribution([[1]], [1], 0)", "the entries of μ_0, as floats")


def test_n_step_distribution_accepts_numpy_integers_and_sums_within_1e_9(mk):
    P = np.array([[0.3, 0.7 + 6e-10], [0.55, 0.45 - 4e-10]])
    mu0 = np.array([0.25, 0.75 + 5e-10])
    for n in (np.int64(5), np.int32(3), np.uint8(2), 4):
        what = f"n_step_distribution(P, mu0, {n!r}), rows of P and mu0 summing to 1 within 1e-9"
        got = _result(lambda: mk.n_step_distribution(P, mu0, n), "an array of shape (2,)", what,
                      "a NumPy integer is accepted, and rows and laws sum to 1 up to 1e-9")
        _float_array(got, (2,), what)
        _close(got, _n_step_oracle(P, mu0, int(n)), what, rtol=1e-10, atol=1e-13,
               hint=_n_step_hint(got, P, mu0, int(n)))


def test_n_step_distribution_takes_lists_of_integers_and_returns_floats(mk):
    cycle = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    for given, text in ((lambda v: v, "lists of integers"), (np.array, "integer arrays")):
        what = f"n_step_distribution with {text}: a cycle 0 → 1 → 2 → 0, from state 1, 4 steps"
        got = _result(lambda: mk.n_step_distribution(given(cycle), given([0, 1, 0]), 4), "array([0., 0., 1.])", what)
        _float_array(got, (3,), what)
        _close(got, [0.0, 0.0, 1.0], f"{what} (state 1 + 4 = state 2 modulo 3)", rtol=0, atol=1e-15,
               hint=_n_step_hint(got, cycle, [0, 1, 0], 4))


def test_n_step_distribution_does_not_modify_its_inputs(mk_module):
    mk = mk_module
    rng = np.random.default_rng(6112)
    P = _stochastic(rng, 4)
    mu0 = rng.dirichlet(np.ones(4))
    copies = [P.copy(), mu0.copy()]
    got = _result(lambda: mk.n_step_distribution(P, mu0, 6), "an array of shape (4,)", "float arrays")
    for name, value, copy in zip(("P", "mu0"), (P, mu0), copies):
        assert np.array_equal(value, copy), (
            f"expected {name} unchanged by n_step_distribution, got {name} = {_show(value)} (never modify the arrays "
            f"you receive: mu = mu @ P makes a new array, mu[:] = mu @ P writes into mu0)")
    got[...] = 99.0
    assert np.array_equal(P, copies[0]) and np.array_equal(mu0, copies[1]), (
        "expected n_step_distribution to return a new array, but changing it changed P or mu0")


P2 = [[0.35, 0.65], [0.8, 0.2]]
MU2 = [0.4, 0.6]
N_STEP_REFUSALS = [
    ([0.35, 0.65], [1.0], 1, "P is 1-D"),
    ([[0.35, 0.65]], [1.0], 1, "P is 1 × 2, not square"),
    (np.zeros((0, 0)), [], 1, "P is empty (m = 0)"),
    (np.full((2, 2, 2), 0.5), MU2, 1, "P is 3-D"),
    ([[0.35, 0.65], [0.8]], MU2, 1, "P is a ragged list"),
    ([[0.35, 0.65], [np.nan, 0.2]], MU2, 1, "P holds a nan"),
    ([[0.35, 0.65], [np.nan, 0.2]], MU2, 0, "P holds a nan, even for n = 0"),
    ([[0.35, 0.65], [np.inf, 0.2]], MU2, 1, "P holds an inf"),
    ([[1.25, -0.25], [0.8, 0.2]], MU2, 1, "P holds a negative entry (its row sums to 1)"),
    ([[0.35, 0.55], [0.8, 0.2]], MU2, 1, "row 0 of P sums to 0.9: a substochastic matrix is refused here"),
    ([[0.35, 0.65 + 1e-8], [0.8, 0.2]], MU2, 1, "row 0 sums to 1 + 1e-8, beyond the tolerance 1e-9"),
    ([[0.35, 0.65], [0.8, 0.2 - 1e-8]], MU2, 1, "row 1 sums to 1 - 1e-8, beyond the tolerance 1e-9"),
    (P2, [0.4, 0.3, 0.3], 1, "mu0 has 3 entries for 2 states"),
    (P2, [0.4, 0.3, 0.3], 0, "mu0 has 3 entries for 2 states, even for n = 0"),
    (P2, [1.0], 1, "mu0 has 1 entry for 2 states"),
    (P2, [[0.4, 0.6]], 1, "mu0 is 2-D"),
    ([[1.0]], 1.0, 3, "mu0 is a number, not 1-D: write [1.0]"),
    ([[1.0]], 1.0, 0, "mu0 is a number, not 1-D, even for n = 0"),
    (P2, [1.2, -0.2], 1, "mu0 holds a negative entry (its sum is 1)"),
    (P2, [0.4, 0.5], 1, "mu0 sums to 0.9"),
    (P2, [0.4, 0.6 + 1e-8], 1, "mu0 sums to 1 + 1e-8, beyond the tolerance 1e-9"),
    (P2, [np.nan, 0.6], 1, "mu0 holds a nan"),
    (P2, [np.inf, 0.6], 1, "mu0 holds an inf"),
    (P2, MU2, -1, "n is negative"),
    (P2, MU2, 2.0, "n is the float 2.0"),
    (P2, MU2, 2.5, "n is 2.5"),
    (P2, MU2, np.float64(3.0), "n is np.float64(3.0)"),
    (P2, MU2, True, "n is a bool (True)"),
    (P2, MU2, False, "n is a bool (False), even though False == 0"),
    (P2, MU2, np.bool_(True), "n is a NumPy bool"),
    (P2, MU2, None, "n is None"),
    (P2, MU2, "3", "n is a string"),
    (P2, MU2, [3], "n is a list"),
]
N_STEP_IDS = ["P-one-d", "P-not-square", "P-empty", "P-three-d", "P-ragged", "P-nan", "P-nan-zero-steps", "P-inf",
              "P-negative", "P-substochastic", "P-sum-above", "P-sum-below", "mu0-longer", "mu0-longer-zero-steps",
              "mu0-shorter", "mu0-two-d", "mu0-scalar", "mu0-scalar-zero-steps", "mu0-negative", "mu0-sum",
              "mu0-sum-beyond-tolerance", "mu0-nan", "mu0-inf", "n-negative", "n-float", "n-fraction", "n-numpy-float",
              "n-true", "n-false", "n-numpy-bool", "n-none", "n-string",
              "n-list"]


@pytest.mark.parametrize("P, mu0, n, why", N_STEP_REFUSALS, ids=N_STEP_IDS)
def test_n_step_distribution_refusals(mk, P, mu0, n, why):
    _expect_error(ValueError, lambda: mk.n_step_distribution(P, mu0, n), f"n_step_distribution({P!r}, {mu0!r}, {n!r})",
                  why)


# --- stationary_distribution ----------------------------------------------------------------------------------------

STATIONARY_HINT = ("π P = π is (Pᵀ - I) πᵀ = 0, whose m equations add up to 0 = 0: replace the last one by "
                   "Σ_j π_j = 1 (a row of ones, right-hand side (0, …, 0, 1)), solve, set the negative roundings to 0 "
                   "and divide by the sum")


def _stationary_hint(got, P):
    """STATIONARY_HINT, plus the classic error that the law got matches, if any."""
    P = np.asarray(P, dtype=float)
    m = P.shape[0]
    want = _stationary_eig(P)
    with np.errstate(all="ignore"):
        A = P.T - np.eye(m)
        A[:, -1] = 1.0
        try:
            column = np.linalg.solve(A, np.eye(m)[-1])
            column = np.where(column < 0, 0.0, column)
            column = column / np.sum(column)                 # as the docstring asks, after the wrong system
        except np.linalg.LinAlgError:
            column = None
        candidates = [
            (np.full(m, 1.0 / m), ("the uniform law solves P 1 = 1 (a right eigenvector, P - I): π P = π is a left "
                                   "one, (Pᵀ - I) πᵀ = 0")),
            (want / np.sqrt(np.sum(want ** 2)), "π was divided by its Euclidean norm: a law is divided by its sum"),
            (want / want[-1], "π_last = 1 was imposed: the last equation becomes Σ_j π_j = 1, a row of ones"),
            (want / want[0], "π_0 = 1 was imposed: π is divided by its sum, Σ_j π_j = 1"),
            (want / np.max(want), "π was divided by its largest entry: a law is divided by its sum"),
            (column, "the last COLUMN of Pᵀ - I was replaced by ones: replace its last ROW (an equation)"),
        ]
    text = _first_match(got, want, candidates)
    return f"{STATIONARY_HINT}; here {text}" if text else STATIONARY_HINT


def _check_law(got, m, what, hint):
    _float_array(got, (m,), what, hint)
    assert np.all(got >= 0) and abs(float(np.sum(got)) - 1.0) <= 1e-12, (
        f"expected a law (entries >= 0, sum 1 within 1e-12) for {what}, got {_show(got)}, min {float(np.min(got)):.3g},"
        f" sum {float(np.sum(got)):.15g} ({hint})")


def test_stationary_distribution_docstring_examples(mk):
    call = "stationary_distribution([[0.6, 0.4], [0.2, 0.8]])"
    got = _result(lambda: mk.stationary_distribution([[0.6, 0.4], [0.2, 0.8]]), "array([0.33333333, 0.66666667])",
                  call, STATIONARY_HINT)
    _float_array(got, (2,), call)
    _close(got, [1 / 3, 2 / 3], call, rtol=0, atol=1e-12, hint=_stationary_hint(got, [[0.6, 0.4], [0.2, 0.8]]))
    call = "stationary_distribution([[0, 1], [1, 0]]) (periodic, but π is unique)"
    got = _result(lambda: mk.stationary_distribution([[0, 1], [1, 0]]), "array([0.5, 0.5])", call, STATIONARY_HINT)
    _float_array(got, (2,), call)
    _close(got, [0.5, 0.5], call, rtol=0, atol=1e-12, hint=STATIONARY_HINT)
    _expect_error(ValueError, lambda: mk.stationary_distribution([[1, 0], [0, 1]]),
                  "stationary_distribution([[1, 0], [0, 1]])", "two closed classes: the stationary law is not unique")


STATIONARY_CASES = [(1, 0.0, "one state"), (2, 0.0, "two states"), (3, 0.0, "three states"),
                    (4, 0.5, "four states, sparse"), (6, 0.0, "six states"), (8, 0.6, "eight states, sparse"),
                    (15, 0.0, "fifteen states"), (30, 0.8, "thirty states, sparse")]


@pytest.mark.parametrize("m, zeros, text", STATIONARY_CASES, ids=[f"m{m}" for m, _, _ in STATIONARY_CASES])
def test_stationary_distribution_matches_eig_of_P_transpose(mk, m, zeros, text):
    """π is the eigenvector of Pᵀ for the eigenvalue 1 (np.linalg.eig), divided by its sum; and π P = π."""
    rng = np.random.default_rng(6115 + STATIONARY_CASES.index((m, zeros, text)))
    P = _stochastic(rng, m, alpha=0.8, zeros=zeros)
    want = _stationary_eig(P)
    what = f"stationary_distribution(P) for a random irreducible chain, {text}"
    got = _result(lambda: mk.stationary_distribution(P), f"a law of {m} entries", what, STATIONARY_HINT)
    _check_law(got, m, what, _stationary_hint(got, P))
    _close(got, want, f"{what}, the eigenvector of Pᵀ for the eigenvalue 1 (np.linalg.eig) divided by its sum",
           rtol=1e-8, atol=1e-12, hint=_stationary_hint(got, P))
    _close(got @ P, got, f"π P for {what}, equal to π", rtol=1e-9, atol=1e-12, hint=_stationary_hint(got, P))


def test_stationary_distribution_matches_scipy_null_space(mk):
    """null_space(Pᵀ - I) (scipy) has one column exactly when π is unique: that column divided by its sum."""
    rng = np.random.default_rng(6123)
    for m, alpha in ((3, 0.3), (5, 2.0), (10, 0.5), (20, 1.0)):
        P = _stochastic(rng, m, alpha=alpha, zeros=0.3)
        want = _stationary_null_space(P)
        what = f"stationary_distribution(P) for a random chain with {m} states"
        got = _result(lambda: mk.stationary_distribution(P), f"a law of {m} entries", what, STATIONARY_HINT)
        _check_law(got, m, what, _stationary_hint(got, P))
        _close(got, want, f"{what}, the column of scipy.linalg.null_space(Pᵀ - I) divided by its sum", rtol=1e-8,
               atol=1e-12, hint=_stationary_hint(got, P))


def _closed_class_with_transient_states(rng, closed, transient):
    """A chain whose first ``closed`` states form a closed class, the others transient (they lead anywhere)."""
    m = closed + transient
    P = np.zeros((m, m))
    P[:closed, :closed] = rng.dirichlet(np.ones(closed), size=closed)
    P[closed:, :] = rng.dirichlet(np.ones(m), size=transient)
    return P


def test_stationary_distribution_gives_zero_to_transient_states_and_no_negative_entry(mk):
    """A single closed class and transient states: π is unique and the transient states get 0. Solving the system
    leaves roundings like -1e-17 on them (for these chains): they are set to 0, so no entry of π is negative."""
    for seed, closed, transient in ((6124, 3, 3), (6126, 2, 4), (6127, 4, 2)):
        rng = np.random.default_rng(seed)
        P = _closed_class_with_transient_states(rng, closed, transient)
        want = _stationary_null_space(P)
        what = (f"stationary_distribution(P) for a closed class of {closed} states and {transient} transient states "
                f"(seed {seed})")
        got = _result(lambda: mk.stationary_distribution(P), "a law", what, STATIONARY_HINT)
        _float_array(got, (closed + transient,), what)
        assert np.all(got >= 0), (
            f"expected no negative entry for {what}, got {_show(got)}, min {float(np.min(got)):.3g} (the docstring: "
            f"negative entries due to rounding are set to 0, then π is divided by its sum)")
        _close(got[closed:], np.zeros(transient), f"the entries of the transient states for {what}", rtol=0,
               atol=1e-13, hint="a transient state is visited a finite number of times: π gives it 0")
        _check_law(got, closed + transient, what, _stationary_hint(got, P))
        _close(got, want, f"{what}, scipy.linalg.null_space(Pᵀ - I)", rtol=1e-8, atol=1e-13,
               hint=_stationary_hint(got, P))


def test_stationary_distribution_is_invariant_and_a_law(mk):
    """π P = π, π ≥ 0 and Σ π = 1 on chains of every kind (sparse, nearly deterministic, with near-zero entries)."""
    rng = np.random.default_rng(6125)
    for m, alpha, zeros in ((3, 0.1, 0.0), (7, 0.2, 0.5), (12, 5.0, 0.0), (25, 0.3, 0.7), (40, 1.0, 0.9)):
        P = _stochastic(rng, m, alpha=alpha, zeros=zeros)
        what = f"stationary_distribution(P) for a random chain with {m} states (Dirichlet {alpha}, zeros {zeros})"
        got = _result(lambda: mk.stationary_distribution(P), "a law", what, STATIONARY_HINT)
        _check_law(got, m, what, _stationary_hint(got, P))
        _close(got @ P, got, f"π P for {what}, equal to π", rtol=1e-8, atol=1e-12, hint=_stationary_hint(got, P))


def test_stationary_distribution_of_a_periodic_chain_exists_and_is_unique(mk):
    """A periodic chain does not converge, but its stationary law exists and is unique (null_space has one column):
    a walk on a path with reflecting ends (period 2), a rotation of 3 states (period 3), and a random chain whose
    states alternate between two groups (period 2)."""
    rng = np.random.default_rng(6128)
    walk = np.array([[0.0, 1.0, 0.0, 0.0], [0.45, 0.0, 0.55, 0.0], [0.0, 0.15, 0.0, 0.85], [0.0, 0.0, 1.0, 0.0]])
    rotation = np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    bipartite = np.zeros((5, 5))
    bipartite[:2, 2:] = rng.dirichlet(np.ones(3), size=2)
    bipartite[2:, :2] = rng.dirichlet(np.ones(2), size=3)
    for P, text in ((walk, "a walk on a path with reflecting ends (period 2)"),
                    (rotation, "a rotation of 3 states (period 3)"),
                    (bipartite, "a chain that alternates between {0, 1} and {2, 3, 4} (period 2)")):
        assert _null_space(P).shape[1] == 1               # the oracle: π is unique
        want = _stationary_null_space(P)
        what = f"stationary_distribution(P) for {text}"
        got = _result(lambda: mk.stationary_distribution(P), "a law", what,
                      f"a periodic chain has a unique stationary law: do not refuse it ({STATIONARY_HINT})")
        _check_law(got, P.shape[0], what, _stationary_hint(got, P))
        _close(got, want, f"{what}, scipy.linalg.null_space(Pᵀ - I)", rtol=1e-9, atol=1e-12,
               hint=_stationary_hint(got, P))


def _blocks(rng, sizes):
    """A block-diagonal stochastic matrix: one closed class per block, random Dirichlet rows inside."""
    m = sum(sizes)
    P = np.zeros((m, m))
    start = 0
    for k in sizes:
        P[start:start + k, start:start + k] = rng.dirichlet(np.ones(k), size=k)
        start += k
    return P


def test_stationary_distribution_refuses_a_chain_with_two_closed_classes(mk):
    """Two closed classes (null_space(Pᵀ - I) has two columns): every mixture of their stationary laws is stationary,
    so the law is not unique. Solving the square system anyway gives one of them, rounding hides the singularity:
    np.linalg.matrix_rank must see it."""
    rng = np.random.default_rng(6129)
    two_absorbing = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.3, 0.1, 0.25, 0.35],
                              [0.05, 0.4, 0.5, 0.05]])
    with_transient = _blocks(rng, [2, 3, 1])
    with_transient[5] = rng.dirichlet(np.ones(6))           # state 5 is transient, it may reach both classes
    cases = [(_blocks(rng, [2, 3]), "two random closed classes of 2 and 3 states"),
             (_blocks(rng, [4, 4]), "two random closed classes of 4 states"),
             (_blocks(rng, [1, 6]), "an absorbing state and a closed class of 6 states"),
             (two_absorbing, "two absorbing states and two transient states"),
             (with_transient, "two closed classes and a transient state"),
             (np.eye(3), "the identity: three absorbing states"),
             (_blocks(rng, [3, 3, 3]), "three closed classes of 3 states")]
    for P, text in cases:
        assert _null_space(P).shape[1] >= 2               # the oracle: π is not unique
        _expect_error(ValueError, lambda: mk.stationary_distribution(P), f"stationary_distribution(P) for {text}",
                      "the stationary law is not unique: the square system is singular according to "
                      "np.linalg.matrix_rank")


def test_stationary_distribution_of_a_damped_web_matches_eig(mk):
    """The random surfer of a small web (PageRank): with the probability 0.85 a link of the page, otherwise any page;
    pages without links send to any page."""
    rng = np.random.default_rng(6131)
    m = 18
    links = rng.random((m, m)) < 0.2
    np.fill_diagonal(links, False)
    links[[3, 11]] = False                                   # two pages without links
    out = links.sum(axis=1, keepdims=True)
    follow = np.where(out > 0, links / np.maximum(out, 1), 1.0 / m)
    P = 0.85 * follow + 0.15 / m
    want = _stationary_eig(P)
    what = "stationary_distribution(P) for the random surfer of a web of 18 pages (damping 0.85)"
    got = _result(lambda: mk.stationary_distribution(P), "a law of 18 entries", what, STATIONARY_HINT)
    _check_law(got, m, what, _stationary_hint(got, P))
    _close(got, want, f"{what}, np.linalg.eig on Pᵀ", rtol=1e-9, atol=1e-13, hint=_stationary_hint(got, P))


def test_stationary_distribution_of_a_doubly_stochastic_chain_is_uniform(mk):
    """Columns that also sum to 1 (here a mixture of permutation matrices): 1/m on every state."""
    rng = np.random.default_rng(6132)
    m = 6
    weights = rng.dirichlet(np.ones(4))
    P = sum(w * np.eye(m)[rng.permutation(m)] for w in weights)
    assert _null_space(P).shape[1] == 1
    what = "stationary_distribution(P) for a doubly stochastic chain (columns summing to 1 too)"
    got = _result(lambda: mk.stationary_distribution(P), "the uniform law", what, STATIONARY_HINT)
    _check_law(got, m, what, STATIONARY_HINT)
    _close(got, np.full(m, 1 / m), f"{what}, the uniform law", rtol=1e-10, atol=1e-13, hint=STATIONARY_HINT)


def test_stationary_distribution_takes_lists_of_integers_and_accepts_sums_within_1e_9(mk):
    rotation = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    for given, text in ((lambda v: v, "a list of integers"), (np.array, "an integer array")):
        what = f"stationary_distribution of {text}, the rotation [[0, 0, 1], [1, 0, 0], [0, 1, 0]]"
        got = _result(lambda: mk.stationary_distribution(given(rotation)), "array([1/3, 1/3, 1/3])", what,
                      STATIONARY_HINT)
        _float_array(got, (3,), what)
        _close(got, np.full(3, 1 / 3), what, rtol=1e-12, atol=1e-14, hint=_stationary_hint(got, rotation))
    got = _result(lambda: mk.stationary_distribution([[1]]), "array([1.])", "stationary_distribution([[1]])",
                  "with one state, the last equation is the only one: it becomes π_0 = 1")
    _float_array(got, (1,), "stationary_distribution([[1]])")
    _close(got, [1.0], "stationary_distribution([[1]]), one state", rtol=0, atol=1e-15)
    P = np.array([[0.15, 0.85 + 7e-10], [0.55, 0.45 - 6e-10]])
    got = _result(lambda: mk.stationary_distribution(P), "a law", "rows summing to 1 + 7e-10 and 1 - 6e-10",
                  "rows sum to 1 up to 1e-9")
    _check_law(got, 2, "stationary_distribution with rows summing to 1 ± 1e-9", STATIONARY_HINT)
    _close(got, _stationary_eig(P), "stationary_distribution with rows summing to 1 ± 1e-9", rtol=1e-8,
           hint=_stationary_hint(got, P))


def test_stationary_distribution_does_not_modify_its_input(mk_module):
    mk = mk_module
    rng = np.random.default_rng(6130)
    P = _stochastic(rng, 5, zeros=0.3)
    copy = P.copy()
    got = _result(lambda: mk.stationary_distribution(P), "a law", "a float array")
    assert np.array_equal(P, copy), (
        f"expected P unchanged by stationary_distribution, got P = {_show(P)} (never modify the arrays you receive: "
        f"P.T - np.eye(m) makes a new array, but P.T is a view of P, and writing into it writes into P)")
    got[...] = 99.0
    assert np.array_equal(P, copy), "expected stationary_distribution to return a new array, but changing it changed P"


STATIONARY_REFUSALS = [
    ([0.35, 0.65], "P is 1-D"),
    ([[0.35, 0.65]], "P is 1 × 2, not square"),
    (np.zeros((0, 0)), "P is empty (m = 0)"),
    (np.full((2, 2, 2), 0.5), "P is 3-D"),
    ([[0.35, 0.65], [0.8]], "P is a ragged list"),
    ([[0.35, 0.65], [np.nan, 0.2]], "P holds a nan"),
    ([[0.35, 0.65], [0.8, np.inf]], "P holds an inf"),
    ([[1.25, -0.25], [0.8, 0.2]], "P holds a negative entry (its row sums to 1)"),
    ([[0.35, 0.55], [0.8, 0.2]], "row 0 of P sums to 0.9: a substochastic matrix is refused here"),
    ([[0.0, 0.0], [0.8, 0.2]], "row 0 of P sums to 0"),
    ([[0.35, 0.65 + 1e-8], [0.8, 0.2]], "row 0 sums to 1 + 1e-8, beyond the tolerance 1e-9"),
    ([[0.35, 0.65], [0.8, 0.2 - 1e-8]], "row 1 sums to 1 - 1e-8, beyond the tolerance 1e-9"),
    ([[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]], "P is 3 × 2"),
    ("[[0.35, 0.65], [0.8, 0.2]]", "P is a string"),
]
STATIONARY_IDS = ["P-one-d", "P-not-square", "P-empty", "P-three-d", "P-ragged", "P-nan", "P-inf", "P-negative",
                  "P-substochastic", "P-zero-row", "P-sum-above", "P-sum-below", "P-three-by-two", "P-string"]


@pytest.mark.parametrize("P, why", STATIONARY_REFUSALS, ids=STATIONARY_IDS)
def test_stationary_distribution_refusals(mk, P, why):
    _expect_error(ValueError, lambda: mk.stationary_distribution(P), f"stationary_distribution({P!r})", why)


# --- bellman_linear_solve -------------------------------------------------------------------------------------------

BELLMAN_HINT = "solve (I - γ P) V = r, values in columns: (P V)[i] = Σ_j P[i, j] V[j], so P @ V"


def _bellman_hint(got, P, r, gamma):
    """BELLMAN_HINT, plus the classic error that the values got match, if any."""
    P, r = np.asarray(P, dtype=float), np.asarray(r, dtype=float)
    m = P.shape[0]
    I = np.eye(m)
    want = _bellman_oracle(P, r, gamma)

    def solved(M):
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                if np.linalg.cond(M) > 1e10:
                    return None
                return sla.solve(M, r)
        except (np.linalg.LinAlgError, ValueError, sla.LinAlgError):
            return None

    with np.errstate(all="ignore"):
        candidates = [
            (solved(I - P), "γ is missing: (I - γ P) V = r, γ multiplies P"),
            (solved(I - gamma * P.T), "Pᵀ was used: values are columns, (P V)[i] = Σ_j P[i, j] V[j], so I - γ P"),
            (r / (1 - gamma) if gamma < 1 else None, ("P is missing: r / (1 - γ) would be the value of a state that "
                                                      "keeps its reward forever")),
            (r + gamma * (P @ r), "only two terms of the series r + γ P r + γ² P² r + …: solve the system"),
            (-want, "the sign is wrong: (I - γ P) V = r, not (γ P - I) V = r"),
            (solved(I + gamma * P), "I - γ P, with a minus: V = r + γ P V"),
            (r if gamma > 0 else None, "V = r only for γ = 0: the future rewards count too"),
        ]
    text = _first_match(got, want, candidates)
    return f"{BELLMAN_HINT}; here {text}" if text else BELLMAN_HINT


def test_bellman_linear_solve_docstring_examples(mk):
    P = [[0.5, 0.5], [0.0, 1.0]]
    call = "bellman_linear_solve([[0.5, 0.5], [0.0, 1.0]], [1, 2], 0.75)"
    got = _result(lambda: mk.bellman_linear_solve(P, [1, 2], 0.75), "array([6.4, 8. ])", call, BELLMAN_HINT)
    _float_array(got, (2,), call)
    _close(got, [6.4, 8.0], call, rtol=0, atol=1e-12, hint=_bellman_hint(got, P, [1, 2], 0.75))
    Q = [[0.5, 0.25], [0.5, 0.0]]
    call = "bellman_linear_solve([[0.5, 0.25], [0.5, 0.0]], [1, 1], 1.0) (the mean number of steps before the end)"
    got = _result(lambda: mk.bellman_linear_solve(Q, [1, 1], 1.0), "array([3.33333333, 2.66666667])", call,
                  "P may be substochastic, and γ = 1 is allowed when the process ends for sure")
    _float_array(got, (2,), call)
    _close(got, [10 / 3, 8 / 3], call, rtol=0, atol=1e-12, hint=_bellman_hint(got, Q, [1, 1], 1.0))
    _expect_error(ValueError, lambda: mk.bellman_linear_solve(P, [1, 2], 1.0),
                  "bellman_linear_solve([[0.5, 0.5], [0.0, 1.0]], [1, 2], 1.0)",
                  "gamma = 1 and the process never ends from state 1 (absorbing): I - P is singular")


BELLMAN_CASES = [(1, 0.6, "stochastic", "one state"), (2, 0.7, "stochastic", "two states"),
                 (3, 0.85, "substochastic", "three states, the process may end"),
                 (4, 0.96, "stochastic", "four states, γ = 0.96"), (5, 0.0, "stochastic", "γ = 0"),
                 (6, 0.6, "substochastic", "six states, the process may end"),
                 (8, 0.85, "sparse", "eight states, sparse"), (10, 0.96, "substochastic", "ten states, γ = 0.96"),
                 (25, 0.7, "stochastic", "twenty-five states")]


def _bellman_case(rng, m, kind):
    P = _substochastic(rng, m) if kind == "substochastic" else _stochastic(rng, m, alpha=0.7,
                                                                            zeros=0.5 if kind == "sparse" else 0.0)
    return P, rng.normal(size=m) * 3.0 + 1.0


@pytest.mark.parametrize("m, gamma, kind, text", BELLMAN_CASES, ids=[f"m{m}-g{g}" for m, g, _, _ in BELLMAN_CASES])
def test_bellman_linear_solve_matches_scipy_solve(mk, m, gamma, kind, text):
    """(I - γP) V = r by scipy.linalg.solve, for random stochastic or substochastic P and random rewards."""
    rng = np.random.default_rng(6135 + BELLMAN_CASES.index((m, gamma, kind, text)))
    P, r = _bellman_case(rng, m, kind)
    want = _bellman_oracle(P, r, gamma)
    what = f"bellman_linear_solve(P, r, {gamma}) for {text}"
    got = _result(lambda: mk.bellman_linear_solve(P, r, gamma), f"an array of shape ({m},)", what, BELLMAN_HINT)
    _float_array(got, (m,), what)
    _close(got, want, f"{what}, scipy.linalg.solve(I - γ P, r)", rtol=1e-9, atol=1e-11,
           hint=_bellman_hint(got, P, r, gamma))


def test_bellman_linear_solve_matches_the_truncated_neumann_series(mk):
    """V = Σ_t γᵗ Pᵗ r (the series of ∂ M26.11), truncated when the rest is below 1e-17 ‖r‖∞."""
    rng = np.random.default_rng(6145)
    for m, gamma, kind in ((3, 0.6, "stochastic"), (5, 0.7, "substochastic"), (7, 0.85, "sparse"),
                           (4, 0.96, "stochastic")):
        P, r = _bellman_case(rng, m, kind)
        want = _neumann(P, r, gamma)
        what = f"bellman_linear_solve(P, r, {gamma}) for a random {kind} chain with {m} states"
        got = _result(lambda: mk.bellman_linear_solve(P, r, gamma), f"an array of shape ({m},)", what, BELLMAN_HINT)
        _float_array(got, (m,), what)
        _close(got, want, f"{what}, the truncated series Σ γᵗ Pᵗ r", rtol=1e-9, atol=1e-11,
               hint=_bellman_hint(got, P, r, gamma))


def test_bellman_linear_solve_satisfies_the_bellman_equation(mk):
    """The values solve V = r + γ P V: the residual r + γ P V - V is 0 (within 1e-10 of the scale of V)."""
    rng = np.random.default_rng(6146)
    for m, gamma in ((4, 0.6), (9, 0.85), (16, 0.96), (30, 0.7)):
        P = _stochastic(rng, m, alpha=0.5, zeros=0.4)
        r = rng.uniform(-2.0, 5.0, size=m)
        what = f"bellman_linear_solve(P, r, {gamma}) for a random chain with {m} states"
        got = _result(lambda: mk.bellman_linear_solve(P, r, gamma), f"an array of shape ({m},)", what, BELLMAN_HINT)
        _float_array(got, (m,), what)
        scale = max(1.0, float(np.max(np.abs(got))))
        residual = r + gamma * (P @ got) - got
        assert np.max(np.abs(residual)) <= 1e-10 * scale, (
            f"expected V = r + γ P V for {what}, got a largest residual |r + γ P V - V| of "
            f"{float(np.max(np.abs(residual))):.3g} ({_bellman_hint(got, P, r, gamma)})")


def test_bellman_linear_solve_a_row_that_ends_equals_an_absorbing_state_of_zero_reward(mk):
    """For γ < 1, a substochastic row (the missing mass is the probability of ending) gives the same values as an extra
    absorbing state of reward 0 that receives that mass; both against scipy.linalg.solve."""
    rng = np.random.default_rng(6147)
    for m, gamma in ((3, 0.7), (6, 0.96), (4, 0.6)):
        P = _substochastic(rng, m, low=0.0, high=0.5)
        P[0] = rng.dirichlet(np.ones(m))                     # one row that does not end
        r = rng.normal(size=m) * 2.0
        big, r_big = _with_absorbing_state(P, r)
        what = f"bellman_linear_solve(P, r, {gamma}), P substochastic with {m} states"
        got = _result(lambda: mk.bellman_linear_solve(P, r, gamma), f"an array of shape ({m},)", what,
                      "P may be substochastic in the Bellman functions: rows sum to at most 1")
        _float_array(got, (m,), what)
        _close(got, _bellman_oracle(P, r, gamma), f"{what}, scipy.linalg.solve(I - γ P, r)", rtol=1e-9, atol=1e-11,
               hint=_bellman_hint(got, P, r, gamma))
        absorbing = _result(lambda: mk.bellman_linear_solve(big, r_big, gamma), f"an array of shape ({m + 1},)",
                            f"the same process with an absorbing state of reward 0, γ = {gamma}")
        _float_array(absorbing, (m + 1,), "bellman_linear_solve with an extra absorbing state")
        _close(absorbing[:m], got, f"the values of the {m} states with an absorbing state of reward 0 instead of rows "
                                   f"that end (γ = {gamma})", rtol=1e-9, atol=1e-11,
               hint=f"the missing mass of a row is the probability of ending ({BELLMAN_HINT})")
        _close(absorbing[m], 0.0, "the value of the absorbing state of reward 0", rtol=0, atol=1e-12,
               hint=BELLMAN_HINT)


def test_bellman_linear_solve_discounting_is_ending_with_probability_1_minus_gamma(mk):
    """γ P is substochastic: the values for (P, γ) are those for (γ P, γ = 1), a process that ends with the
    probability 1 - γ at each step (scipy.linalg.solve for both)."""
    rng = np.random.default_rng(6149)
    for m, gamma in ((3, 0.6), (5, 0.85), (8, 0.96)):
        P = _stochastic(rng, m, alpha=0.6)
        r = rng.normal(size=m) + 2.0
        want = _bellman_oracle(P, r, gamma)
        discounted = _result(lambda: mk.bellman_linear_solve(P, r, gamma), f"an array of shape ({m},)",
                             f"bellman_linear_solve(P, r, {gamma})", BELLMAN_HINT)
        _close(discounted, want, f"bellman_linear_solve(P, r, {gamma}), scipy.linalg.solve", rtol=1e-9, atol=1e-11,
               hint=_bellman_hint(discounted, P, r, gamma))
        ending = _result(lambda: mk.bellman_linear_solve(gamma * P, r, 1.0), f"an array of shape ({m},)",
                         f"bellman_linear_solve({gamma} P, r, 1.0)",
                         f"γ P is substochastic (rows summing to {gamma}): the process ends for sure, γ = 1 is allowed")
        _float_array(ending, (m,), f"bellman_linear_solve({gamma} P, r, 1.0)")
        _close(ending, want, f"bellman_linear_solve({gamma} P, r, 1.0), the same values as for (P, γ = {gamma})",
               rtol=1e-9, atol=1e-11, hint=_bellman_hint(ending, gamma * P, r, 1.0))


def _transient_chain(rng, m):
    """States 0 … m - 1 that only move forward (i → j > i) or end; the last state always ends: a sure end."""
    P = np.zeros((m, m))
    for i in range(m - 1):
        P[i, i + 1:] = rng.dirichlet(np.ones(m - 1 - i)) * rng.choice([1.0, 0.8])   # some rows do not end
    return P


def test_bellman_linear_solve_with_gamma_1_and_a_sure_end(mk):
    """γ = 1 is allowed when the process ends for sure from every state (I - P invertible): rows that all may end,
    stochastic rows that lead to rows that end, a closed-looking group with a single rare exit, and the zero matrix.
    The cases are well conditioned (cond(I - P) ≤ 1e8, checked); the tolerance follows the condition number."""
    rng = np.random.default_rng(6148)
    leaky = _stochastic(rng, 6, alpha=1.0)
    leaky[2] *= 1 - 1e-4                                    # a single state that ends, rarely
    cases = [(_substochastic(rng, 5, low=0.05, high=0.3), rng.normal(size=5) + 1.0,
              "five states that each end with a probability between 0.05 and 0.3"),
             (_transient_chain(rng, 6), np.ones(6), "six states that move forward, r = 1: the mean number of steps"),
             (leaky, rng.uniform(0.5, 1.5, size=6), "six states whose only end is a rare one (1e-4) from state 2"),
             (np.zeros((3, 3)), np.array([4.0, -1.5, 2.25]), "the zero matrix: the process ends after one step, V = r"),
             (np.array([[0.0, 1.0], [0.0, 0.0]]), np.array([3.0, 5.0]), "a stochastic row followed by a row that ends")]
    for P, r, text in cases:
        cond = float(np.linalg.cond(np.eye(len(r)) - P))
        assert cond <= 1e8, f"oracle: a well-conditioned case was expected, cond(I - P) = {cond:.3g}"
        want = _bellman_oracle(P, r, 1.0)
        what = f"bellman_linear_solve(P, r, 1.0) for {text}"
        got = _result(lambda: mk.bellman_linear_solve(P, r, 1.0), f"an array of shape ({len(r)},)", what,
                      "γ = 1 is allowed when I - P is invertible (the process ends for sure from every state)")
        _float_array(got, (len(r),), what)
        _close(got, want, f"{what}, scipy.linalg.solve(I - P, r) (cond(I - P) = {cond:.3g})",
               rtol=max(1e-9, 1e-13 * cond), atol=1e-11, hint=_bellman_hint(got, P, r, 1.0))
    for gamma in (1, np.float64(1.0), np.int64(1)):
        got = _result(lambda: mk.bellman_linear_solve([[0.0, 1.0], [0.0, 0.0]], [3, 5], gamma), "array([8., 5.])",
                      f"bellman_linear_solve([[0, 1], [0, 0]], [3, 5], {gamma!r})", "γ = 1 may be given as an integer")
        _float_array(got, (2,), f"bellman_linear_solve([[0, 1], [0, 0]], [3, 5], {gamma!r})")
        _close(got, [8.0, 5.0], f"bellman_linear_solve([[0, 1], [0, 0]], [3, 5], {gamma!r}): 3 + 5, then 5",
               rtol=0, atol=1e-12, hint=BELLMAN_HINT)


def test_bellman_linear_solve_with_gamma_1_and_no_sure_end_is_refused(mk):
    """γ = 1 and, from some state, the process never ends: I - P is singular (np.linalg.matrix_rank), ValueError.
    The random cases are only singular up to rounding: solving them anyway returns huge values instead of failing."""
    rng = np.random.default_rng(6151)
    closed_pair = _substochastic(rng, 5)
    closed_pair[3:] = 0.0
    closed_pair[3:, 3:] = rng.dirichlet(np.ones(2), size=2)   # states 3 and 4 never leave each other
    cases = [(_stochastic(rng, 4), "a random stochastic matrix (no row ends)"),
             (_stochastic(rng, 7, zeros=0.5), "a random sparse stochastic matrix"),
             (closed_pair, "a random substochastic matrix with a closed pair of states"),
             (np.array([[0.2, 0.5, 0.1], [0.0, 1.0, 0.0], [0.3, 0.3, 0.1]]),
              "an absorbing state (state 1): for γ = 1, an end must be coded by rows that end"),
             (np.array([[0.3, 0.2, 0.1], [0.0, 0.4, 0.6], [0.0, 0.7, 0.3]]), "states 1 and 2 never end"),
             (np.array([[1.0]]), "one state that stays forever")]
    for P, text in cases:
        assert np.linalg.matrix_rank(np.eye(len(P)) - P) < len(P)      # the oracle: I - P is singular
        r = np.ones(len(P))
        _expect_error(ValueError, lambda: mk.bellman_linear_solve(P, r, 1.0),
                      f"bellman_linear_solve(P, r, 1.0) for {text}",
                      "gamma = 1 and the process never ends from some state: I - P is singular according to "
                      "np.linalg.matrix_rank")
        what = f"bellman_linear_solve(P, r, 0.96) for {text}"
        got = _result(lambda: mk.bellman_linear_solve(P, r, 0.96), f"an array of shape ({len(P)},)", what,
                      "for γ < 1, I - γ P is always invertible: only γ = 1 can be refused")
        _close(got, _bellman_oracle(P, r, 0.96), what, rtol=1e-9, atol=1e-11, hint=_bellman_hint(got, P, r, 0.96))


def test_bellman_linear_solve_with_gamma_0_returns_r(mk):
    rng = np.random.default_rng(6152)
    P = _substochastic(rng, 4)
    r = rng.normal(size=4)
    for gamma in (0.0, 0):
        what = f"bellman_linear_solve(P, r, {gamma!r})"
        got = _result(lambda: mk.bellman_linear_solve(P, r, gamma), "r", what, "γ = 0 is allowed: only r counts")
        _float_array(got, (4,), what)
        _close(got, r, f"{what}: with γ = 0, V = r", rtol=1e-14, atol=1e-15, hint=_bellman_hint(got, P, r, 0.0))


def test_bellman_linear_solve_takes_lists_of_integers_and_returns_floats(mk):
    for given, text in ((lambda v: v, "lists of integers"), (np.array, "integer arrays")):
        what = f"bellman_linear_solve with {text}"
        got = _result(lambda: mk.bellman_linear_solve(given([[0, 1], [0, 0]]), given([3, 5]), 1), "array([8., 5.])",
                      f"{what}, [[0, 1], [0, 0]], [3, 5], γ = 1")
        _float_array(got, (2,), what)
        _close(got, [8.0, 5.0], f"{what}, [[0, 1], [0, 0]], [3, 5], γ = 1", rtol=0, atol=1e-12, hint=BELLMAN_HINT)
        P = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
        got = _result(lambda: mk.bellman_linear_solve(given(P), given([2, -1, 4]), 0.6), "an array of shape (3,)",
                      f"{what}, a stochastic integer matrix, γ = 0.6")
        _float_array(got, (3,), what)
        _close(got, _bellman_oracle(P, [2, -1, 4], 0.6), f"{what}, [[1, 0, 0], [0, 0, 1], [0, 1, 0]], [2, -1, 4], "
                                                         f"γ = 0.6", rtol=1e-12, atol=1e-13,
               hint=_bellman_hint(got, P, [2, -1, 4], 0.6))


def test_bellman_linear_solve_accepts_rows_summing_to_at_most_1_plus_1e_9(mk):
    P = np.array([[0.25, 0.75 + 8e-10], [0.4, 0.3]])
    r = np.array([1.5, -0.5])
    got = _result(lambda: mk.bellman_linear_solve(P, r, 0.85), "an array of shape (2,)", "a row summing to 1 + 8e-10",
                  "rows sum to at most 1 up to 1e-9")
    _close(got, _bellman_oracle(P, r, 0.85), "bellman_linear_solve with a row summing to 1 + 8e-10", rtol=1e-9,
           hint=_bellman_hint(got, P, r, 0.85))


def test_bellman_linear_solve_does_not_modify_its_inputs(mk_module):
    mk = mk_module
    rng = np.random.default_rng(6154)
    P = _substochastic(rng, 4)
    r = rng.normal(size=4)
    copies = [P.copy(), r.copy()]
    for gamma in (0.7, 1.0):
        got = _result(lambda: mk.bellman_linear_solve(P, r, gamma), "an array of shape (4,)",
                      f"float arrays, γ = {gamma}")
        for name, value, copy in zip(("P", "r"), (P, r), copies):
            assert np.array_equal(value, copy), (
                f"expected {name} unchanged by bellman_linear_solve, got {name} = {_show(value)} (never modify the "
                f"arrays you receive: np.eye(m) - gamma * P makes a new array, P *= gamma writes into P)")
        got[...] = 99.0
        assert np.array_equal(P, copies[0]) and np.array_equal(r, copies[1]), (
            "expected bellman_linear_solve to return a new array, but changing it changed P or r")


PB = [[0.15, 0.45], [0.3, 0.6]]
RB = [2.0, -1.0]
BELLMAN_P_REFUSALS = [
    ([0.15, 0.45], [2.0], "P is 1-D"),
    ([[0.15, 0.45]], [2.0], "P is 1 × 2, not square"),
    (np.zeros((0, 0)), [], "P is empty (m = 0)"),
    (np.full((2, 2, 2), 0.25), RB, "P is 3-D"),
    ([[0.15, 0.45], [0.3]], RB, "P is a ragged list"),
    ([[0.15, np.nan], [0.3, 0.6]], RB, "P holds a nan"),
    ([[0.15, 0.45], [np.inf, 0.6]], RB, "P holds an inf"),
    ([[0.15, 0.45], [-0.3, 0.6]], RB, "P holds a negative entry"),
    ([[0.15, 0.85 + 1e-8], [0.3, 0.6]], RB, "row 0 sums to 1 + 1e-8, beyond the tolerance 1e-9"),
    ([[0.65, 0.55], [0.3, 0.6]], RB, "row 0 of P sums to 1.2"),
    (PB, [2.0, -1.0, 0.5], "r has 3 entries for 2 states"),
    (PB, [2.0], "r has 1 entry for 2 states"),
    (PB, [[2.0], [-1.0]], "r is a column (2, 1), not 1-D"),
    (PB, [[2.0, -1.0]], "r is 2-D"),
    (PB, 2.0, "r is a number, not 1-D"),
]
BELLMAN_P_IDS = ["P-one-d", "P-not-square", "P-empty", "P-three-d", "P-ragged", "P-nan", "P-inf", "P-negative",
                 "P-sum-beyond-tolerance", "P-sum-above-one", "r-longer", "r-shorter", "r-column", "r-two-d",
                 "r-scalar"]
GAMMA_REFUSALS = [(True, "gamma is a bool (True), even though True == 1"),
                  (False, "gamma is a bool (False), even though False == 0"),
                  (np.bool_(True), "gamma is a NumPy bool"),
                  (-0.1, "gamma is negative"),
                  (1.0000001, "gamma is above 1"),
                  (1.5, "gamma is 1.5"),
                  (np.nan, "gamma is nan"),
                  (np.inf, "gamma is inf"),
                  (-np.inf, "gamma is -inf"),
                  (None, "gamma is None"),
                  ("0.7", "gamma is a string"),
                  ([0.7], "gamma is a list, not a number")]
GAMMA_IDS = ["gamma-true", "gamma-false", "gamma-numpy-bool", "gamma-negative", "gamma-above-one", "gamma-1.5",
             "gamma-nan", "gamma-inf", "gamma-minus-inf", "gamma-none", "gamma-string", "gamma-list"]


@pytest.mark.parametrize("P, r, why", BELLMAN_P_REFUSALS, ids=BELLMAN_P_IDS)
def test_bellman_linear_solve_refuses_bad_matrices_and_rewards(mk, P, r, why):
    _expect_error(ValueError, lambda: mk.bellman_linear_solve(P, r, 0.7), f"bellman_linear_solve({P!r}, {r!r}, 0.7)",
                  why)


@pytest.mark.parametrize("gamma, why", GAMMA_REFUSALS, ids=GAMMA_IDS)
def test_bellman_linear_solve_refuses_bad_gammas(mk, gamma, why):
    _expect_error(ValueError, lambda: mk.bellman_linear_solve(PB, RB, gamma),
                  f"bellman_linear_solve({PB!r}, {RB!r}, {gamma!r})", why)


# --- bellman_fixed_point_iterates -----------------------------------------------------------------------------------

ITERATES_HINT = ("row 0 is V0 (zeros when omitted), then V_{k+1} = r + γ P V_k, that is r + gamma * (P @ V), N times: "
                 "N + 1 rows, each one a new array")


def _iterates_hint(got, P, r, gamma, V0, N):
    """ITERATES_HINT, plus the classic error that the iterates got match, if any."""
    P, r, V0 = np.asarray(P, dtype=float), np.asarray(r, dtype=float), np.asarray(V0, dtype=float)
    m = P.shape[0]
    want = _iterates_loop(P, r, gamma, V0, N, lambda V: r + gamma * (P @ V))
    if isinstance(got, np.ndarray) and got.shape == (N, m):
        return f"{ITERATES_HINT}; here {N} rows were returned for {N} steps: row 0 is V0 itself"
    if isinstance(got, np.ndarray) and got.shape == (N + 2, m):
        return f"{ITERATES_HINT}; here {N + 2} rows were returned: one step too many"

    def gauss_seidel(V):
        V = V.copy()
        for i in range(m):
            V[i] = r[i] + gamma * (P[i] @ V)
        return V

    with np.errstate(all="ignore"):
        candidates = [
            (_iterates_loop(P, r, gamma, V0, N, lambda V: gamma * (P @ V)), "r is forgotten: V_{k+1} = r + γ P V_k"),
            (_iterates_loop(P, r, gamma, V0, N, lambda V: r + P @ V), "γ is missing: V_{k+1} = r + γ P V_k"),
            (_iterates_loop(P, r, gamma, V0, N, lambda V: r + gamma * (P.T @ V)),
             "Pᵀ was used: values are columns, (P V)[i] = Σ_j P[i, j] V[j], so P @ V"),
            (_iterates_loop(P, r, gamma, V0, N, lambda V: gamma * (r + P @ V)),
             "γ multiplies r too: V_{k+1} = r + γ (P V_k), the reward of the current state is not discounted"),
            (_iterates_loop(P, r, gamma, V0, N, gauss_seidel),
             "the sweep is in place (Gauss-Seidel): each V_{k+1}[i] must come from V_k only, a synchronous sweep"),
            (np.vstack([want[1:], r + gamma * (P @ want[-1])]), "row 0 is V0 itself: the rows are V_0, V_1, …, V_N"),
            (np.vstack([V0, np.tile(r + gamma * (P @ V0), (N, 1))]) if N > 1 else None,
             "each step starts from V0: V_{k+1} comes from the previous iterate V_k"),
            (np.tile(want[-1], (N + 1, 1)) if N > 0 else None,
             ("every row is the last iterate: the same array was stored N + 1 times and changed in place (V += …); "
              "store a new array each step")),
            (_iterates_loop(P, r, gamma, np.zeros(m), N, lambda V: r + gamma * (P @ V)) if np.any(V0) else None,
             "the start V0 was ignored: row 0 is V0"),
        ]
    text = _first_match(got, want, candidates)
    return f"{ITERATES_HINT}; here {text}" if text else ITERATES_HINT


def _first_wrong_row(got, want, rtol, atol):
    """The first row k where got and want differ, or None."""
    for k in range(min(len(got), len(want))):
        if not np.allclose(got[k], want[k], rtol=rtol, atol=atol):
            return k
    return None


def _close_iterates(got, want, what, hint, rtol=1e-9, atol=1e-11):
    """The iterates got equal want; the message names the first wrong row."""
    got, want = np.asarray(got, dtype=float), np.asarray(want, dtype=float)
    if got.shape == want.shape and np.allclose(got, want, rtol=rtol, atol=atol):
        return
    k = _first_wrong_row(got, want, rtol, atol) if got.shape == want.shape else None
    where = f", first wrong row {k}: expected V_{k} = {_show(want[k])}, got {_show(got[k])}" if k is not None else ""
    pytest.fail(f"expected {what} = {_show(want)}, got {_show(got)}"
                + ("" if got.shape == want.shape else f" (shape {got.shape} instead of {want.shape})") + where
                + f" ({hint})")


def test_bellman_fixed_point_iterates_docstring_example(mk):
    call = "bellman_fixed_point_iterates([[0.5, 0.5], [0.0, 1.0]], [1, 2], 0.75, n_steps=3)"
    want = [[0.0, 0.0], [1.0, 2.0], [2.125, 3.5], [3.109375, 4.625]]
    got = _result(lambda: mk.bellman_fixed_point_iterates([[0.5, 0.5], [0.0, 1.0]], [1, 2], 0.75, n_steps=3),
                  "an array of shape (4, 2)", call, ITERATES_HINT)
    hint = _iterates_hint(got, [[0.5, 0.5], [0.0, 1.0]], [1, 2], 0.75, [0.0, 0.0], 3)
    _float_array(got, (4, 2), call, hint)
    _close_iterates(got, want, call, hint, rtol=0, atol=1e-15)


ITERATES_CASES = [(1, 0.6, 5, "stochastic", "one state"), (2, 0.7, 12, "stochastic", "two states"),
                  (3, 0.85, 20, "substochastic", "three states, the process may end"),
                  (4, 0.96, 30, "stochastic", "four states, γ = 0.96"), (5, 0.0, 4, "stochastic", "γ = 0"),
                  (6, 0.6, 1, "sparse", "one step"), (9, 0.85, 40, "sparse", "nine states, sparse")]


@pytest.mark.parametrize("m, gamma, N, kind, text", ITERATES_CASES,
                         ids=[f"m{m}-g{g}-N{N}" for m, g, N, _, _ in ITERATES_CASES])
def test_bellman_fixed_point_iterates_match_the_closed_form(mk, m, gamma, N, kind, text):
    """V_k = V + (γP)ᵏ (V₀ - V), with V by scipy.linalg.solve and (γP)ᵏ by np.linalg.matrix_power, from a random V₀."""
    rng = np.random.default_rng(6160 + ITERATES_CASES.index((m, gamma, N, kind, text)))
    P, r = _bellman_case(rng, m, kind)
    V0 = rng.normal(size=m) * 4.0
    want = _iterates_closed_form(P, r, gamma, V0, N)
    what = f"bellman_fixed_point_iterates(P, r, {gamma}, V0, n_steps={N}) for {text}"
    got = _result(lambda: mk.bellman_fixed_point_iterates(P, r, gamma, V0=V0, n_steps=N),
                  f"an array of shape ({N + 1}, {m})", what, ITERATES_HINT)
    hint = _iterates_hint(got, P, r, gamma, V0, N)
    _float_array(got, (N + 1, m), what, hint)
    _close_iterates(got, want, f"{what}, V + (γP)ᵏ (V0 - V)", hint)


def test_bellman_fixed_point_iterates_from_zero_are_partial_sums_of_the_series(mk):
    """From V₀ = 0 (the default), V_k = Σ_{t<k} γᵗ Pᵗ r: the expected discounted reward of the first k steps."""
    rng = np.random.default_rng(6167)
    for m, gamma, N in ((3, 0.6, 8), (5, 0.96, 15), (4, 1.0, 10)):
        P = _substochastic(rng, m) if gamma == 1.0 else _stochastic(rng, m, alpha=0.6)
        r = rng.uniform(-1.0, 3.0, size=m)
        want = _iterates_series(P, r, gamma, N)
        what = f"bellman_fixed_point_iterates(P, r, {gamma}, n_steps={N}) from V0 = 0, {m} states"
        got = _result(lambda: mk.bellman_fixed_point_iterates(P, r, gamma, n_steps=N), f"an array of shape "
                      f"({N + 1}, {m})", what, ITERATES_HINT)
        hint = _iterates_hint(got, P, r, gamma, np.zeros(m), N)
        _float_array(got, (N + 1, m), what, hint)
        _close_iterates(got, want, f"{what}, the partial sums Σ_(t<k) γᵗ Pᵗ r", hint)


def test_bellman_fixed_point_iterates_follow_the_recurrence(mk):
    """Each row comes from the previous one: V_{k+1} = r + γ P V_k, checked on your own rows."""
    rng = np.random.default_rng(6168)
    for m, gamma, N in ((4, 0.7, 25), (7, 0.85, 12), (3, 1.0, 9)):
        P = _substochastic(rng, m, low=0.0, high=0.3)
        r = rng.normal(size=m) * 2.0
        V0 = rng.normal(size=m) * 3.0
        what = f"bellman_fixed_point_iterates(P, r, {gamma}, V0, n_steps={N}), {m} states"
        got = _result(lambda: mk.bellman_fixed_point_iterates(P, r, gamma, V0=V0, n_steps=N),
                      f"an array of shape ({N + 1}, {m})", what, ITERATES_HINT)
        hint = _iterates_hint(got, P, r, gamma, V0, N)
        _float_array(got, (N + 1, m), what, hint)
        _close(got[0], V0, f"row 0 of {what}, V0", rtol=0, atol=0, hint=hint)
        for k in range(N):
            step = r + gamma * (P @ got[k])
            if not np.allclose(got[k + 1], step, rtol=1e-12, atol=1e-12):
                pytest.fail(f"expected row {k + 1} of {what} = r + γ P (row {k}) = {_show(step)}, got "
                            f"{_show(got[k + 1])} ({hint})")


def test_bellman_fixed_point_iterates_respect_the_a_priori_bound_and_converge(mk):
    """For γ < 1, ‖V_k - V‖∞ ≤ γᵏ ‖V₀ - V‖∞ (V by scipy.linalg.solve) at every k, and after enough steps the last
    iterate solves V = r + γ P V within 1e-10 of its scale."""
    rng = np.random.default_rng(6169)
    for m, gamma, N, kind in ((5, 0.6, 80, "stochastic"), (8, 0.85, 250, "sparse"), (6, 0.96, 900, "substochastic"),
                              (12, 0.7, 120, "stochastic")):
        P, r = _bellman_case(rng, m, kind)
        V0 = rng.normal(size=m) * 10.0
        V = _bellman_oracle(P, r, gamma)
        what = f"bellman_fixed_point_iterates(P, r, {gamma}, V0, n_steps={N}), {m} states ({kind})"
        got = _result(lambda: mk.bellman_fixed_point_iterates(P, r, gamma, V0=V0, n_steps=N),
                      f"an array of shape ({N + 1}, {m})", what, ITERATES_HINT)
        hint = _iterates_hint(got, P, r, gamma, V0, N)
        _float_array(got, (N + 1, m), what, hint)
        start = float(np.max(np.abs(V0 - V)))
        scale = max(1.0, float(np.max(np.abs(V))))
        for k in range(N + 1):
            error = float(np.max(np.abs(got[k] - V)))
            bound = gamma ** k * start + 1e-12 * scale * (k + 1)
            if error > bound:
                pytest.fail(f"expected ‖V_{k} - V‖∞ ≤ γ^{k} ‖V0 - V‖∞ = {gamma ** k * start:.6g} for {what}, got "
                            f"{error:.6g} ({hint})")
        residual = float(np.max(np.abs(r + gamma * (P @ got[-1]) - got[-1])))
        assert residual <= 1e-10 * scale, (
            f"expected the last iterate of {what} to solve V = r + γ P V within {1e-10 * scale:.3g}, got a residual "
            f"of {residual:.3g} ({hint})")


def test_bellman_fixed_point_iterates_defaults_and_zero_steps(mk):
    P, r = np.array([[0.2, 0.7], [0.45, 0.35]]), np.array([1.5, -2.0])
    got = _result(lambda: mk.bellman_fixed_point_iterates(P, r, 0.85), "11 rows",
                  "the defaults V0 = 0 and n_steps = 10", ITERATES_HINT)
    hint = _iterates_hint(got, P, r, 0.85, np.zeros(2), 10)
    _float_array(got, (11, 2), "bellman_fixed_point_iterates(P, r, 0.85) with the default n_steps = 10", hint)
    _close_iterates(got, _iterates_closed_form(P, r, 0.85, np.zeros(2), 10), "the iterates from V0 = 0", hint)
    got = _result(lambda: mk.bellman_fixed_point_iterates(P, r, 0.85, V0=[2, -1], n_steps=0), "[[2., -1.]]",
                  "n_steps = 0, V0 = [2, -1]")
    _float_array(got, (1, 2), "bellman_fixed_point_iterates with n_steps = 0", "a single row: V0, as floats")
    _close(got, [[2.0, -1.0]], "the single row V0 when n_steps = 0", rtol=0, atol=0)
    for steps in (np.int64(3), np.int32(2), np.uint16(4)):
        got = _result(lambda: mk.bellman_fixed_point_iterates(P, r, 0.85, n_steps=steps), f"{int(steps) + 1} rows",
                      f"n_steps = {steps!r}", "a NumPy integer is accepted")
        _float_array(got, (int(steps) + 1, 2), f"bellman_fixed_point_iterates with n_steps = {steps!r}")
        _close_iterates(got, _iterates_closed_form(P, r, 0.85, np.zeros(2), int(steps)),
                        f"the iterates with n_steps = {steps!r}", ITERATES_HINT)


def test_bellman_fixed_point_iterates_from_the_solution_stay_there(mk):
    rng = np.random.default_rng(6170)
    P = _substochastic(rng, 4)
    r = rng.normal(size=4)
    V = _bellman_oracle(P, r, 0.7)
    got = _result(lambda: mk.bellman_fixed_point_iterates(P, r, 0.7, V0=V, n_steps=6), "seven rows equal to V",
                  "a start at the solution of (I - γ P) V = r")
    _float_array(got, (7, 4), "bellman_fixed_point_iterates from the solution")
    _close(got, np.tile(V, (7, 1)), "the iterates started at the solution (a fixed point)", rtol=1e-12, atol=1e-13,
           hint=_iterates_hint(got, P, r, 0.7, V, 6))


def test_bellman_fixed_point_iterates_with_gamma_1_return_the_iterates_without_any_check(mk):
    """The function does not check the convergence: for γ = 1 and a stochastic P (the process never ends), the
    iterates from 0 with r = 1 are V_k = k on every state, returned without error; with a sure end, they converge to
    the solution of (I - P) V = r (scipy.linalg.solve)."""
    rng = np.random.default_rng(6173)
    P = _stochastic(rng, 4)
    what = "bellman_fixed_point_iterates(P, np.ones(4), 1.0, n_steps=30), P stochastic"
    got = _result(lambda: mk.bellman_fixed_point_iterates(P, np.ones(4), 1.0, n_steps=30), "31 rows", what,
                  "γ = 1 with a process that never ends is not refused here: the iterates grow, return them")
    hint = _iterates_hint(got, P, np.ones(4), 1.0, np.zeros(4), 30)
    _float_array(got, (31, 4), what, hint)
    _close_iterates(got, np.repeat(np.arange(31.0)[:, None], 4, axis=1), f"{what}: V_k = k on every state (k steps, "
                    f"each worth 1)", hint, rtol=1e-12, atol=1e-12)
    Q = _substochastic(rng, 5, low=0.2, high=0.5)
    r = rng.uniform(0.5, 2.0, size=5)
    what = "bellman_fixed_point_iterates(Q, r, 1.0, n_steps=200), Q substochastic (rows ending with 0.2 to 0.5)"
    got = _result(lambda: mk.bellman_fixed_point_iterates(Q, r, 1.0, n_steps=200), "201 rows", what, ITERATES_HINT)
    hint = _iterates_hint(got, Q, r, 1.0, np.zeros(5), 200)
    _float_array(got, (201, 5), what, hint)
    _close(got[-1], _bellman_oracle(Q, r, 1.0), f"the last row of {what}, the solution of (I - Q) V = r (scipy)",
           rtol=1e-9, atol=1e-11, hint=hint)


def test_bellman_fixed_point_iterates_a_row_that_ends_equals_an_absorbing_state_of_zero_reward(mk):
    """Substochastic rows or an extra absorbing state of reward 0: the same iterates on the first m states."""
    rng = np.random.default_rng(6174)
    P = _substochastic(rng, 4, low=0.0, high=0.5)
    r = rng.normal(size=4)
    V0 = rng.normal(size=4)
    big, r_big = _with_absorbing_state(P, r)
    got = _result(lambda: mk.bellman_fixed_point_iterates(P, r, 0.85, V0=V0, n_steps=15), "16 rows",
                  "P substochastic, γ = 0.85", "P may be substochastic in the Bellman functions")
    hint = _iterates_hint(got, P, r, 0.85, V0, 15)
    _float_array(got, (16, 4), "bellman_fixed_point_iterates with P substochastic", hint)
    _close_iterates(got, _iterates_closed_form(P, r, 0.85, V0, 15), "the iterates with P substochastic", hint)
    absorbing = _result(lambda: mk.bellman_fixed_point_iterates(big, r_big, 0.85, V0=np.append(V0, 0.0), n_steps=15),
                        "16 rows", "the same process with an absorbing state of reward 0")
    _float_array(absorbing, (16, 5), "bellman_fixed_point_iterates with an extra absorbing state")
    _close_iterates(absorbing[:, :4], got, "the iterates of the first 4 states with an absorbing state of reward 0 "
                                           "(starting at 0)", ITERATES_HINT, rtol=1e-12, atol=1e-13)


def test_bellman_fixed_point_iterates_take_lists_of_integers_and_return_floats(mk):
    want = [[1.0, 1.0], [4.0, 5.0], [8.0, 5.0], [8.0, 5.0]]
    for given, text in ((lambda v: v, "lists of integers"), (np.array, "integer arrays")):
        what = f"bellman_fixed_point_iterates with {text}, [[0, 1], [0, 0]], r = [3, 5], γ = 1, V0 = [1, 1], 3 steps"
        got = _result(lambda: mk.bellman_fixed_point_iterates(given([[0, 1], [0, 0]]), given([3, 5]), 1,
                                                              V0=given([1, 1]), n_steps=3), "an array of shape (4, 2)",
                      what)
        hint = _iterates_hint(got, [[0, 1], [0, 0]], [3, 5], 1.0, [1, 1], 3)
        _float_array(got, (4, 2), what, hint)
        _close_iterates(got, want, what, hint, rtol=0, atol=1e-15)


def test_bellman_fixed_point_iterates_do_not_modify_their_inputs(mk_module):
    mk = mk_module
    rng = np.random.default_rng(6172)
    P = _substochastic(rng, 3)
    r, V0 = rng.normal(size=3), rng.normal(size=3)
    copies = [P.copy(), r.copy(), V0.copy()]
    got = _result(lambda: mk.bellman_fixed_point_iterates(P, r, 0.6, V0=V0, n_steps=5), "an array of shape (6, 3)",
                  "float arrays")
    for name, value, copy in zip(("P", "r", "V0"), (P, r, V0), copies):
        assert np.array_equal(value, copy), (
            f"expected {name} unchanged by bellman_fixed_point_iterates, got {name} = {_show(value)} (never modify "
            f"the arrays you receive: start from a float copy of V0; V = r + gamma * (P @ V) makes a new array, "
            f"V[:] = … writes into V0)")
    got[...] = 99.0
    assert all(np.array_equal(v, c) for v, c in zip((P, r, V0), copies)), (
        "expected bellman_fixed_point_iterates to return a new array, but changing it changed P, r or V0 (row 0 is a "
        "copy of V0)")


def test_bellman_fixed_point_iterates_accept_gamma_1_and_rows_summing_to_at_most_1_plus_1e_9(mk):
    """Unlike bellman_linear_solve, γ = 1 is never refused here, even when the process never ends."""
    P = np.array([[0.25, 0.75 + 8e-10], [0.4, 0.6]])
    for gamma in (1.0, 1, 0.96):
        what = f"bellman_fixed_point_iterates(P, [1, 2], {gamma!r}, n_steps=4), rows summing to 1 + 8e-10 and 1"
        got = _result(lambda: mk.bellman_fixed_point_iterates(P, [1, 2], gamma, n_steps=4), "an array of shape (5, 2)",
                      what, "rows sum to at most 1 up to 1e-9, and γ = 1 is allowed (the iterates are not checked)")
        hint = _iterates_hint(got, P, [1, 2], float(gamma), np.zeros(2), 4)
        _float_array(got, (5, 2), what, hint)
        _close_iterates(got, _iterates_series(P, [1, 2], float(gamma), 4), what, hint)


BELLMAN_P_REFUSALS_ITERATES = BELLMAN_P_REFUSALS + [
    (PB, [2.0, -1.0, 0.5], "r has 3 entries for 2 states, even for 0 steps"),
    (PB, 2.0, "r is a number, even for 0 steps"),
]
BELLMAN_P_IDS_ITERATES = BELLMAN_P_IDS + ["r-longer-no-step", "r-scalar-no-step"]


@pytest.mark.parametrize("P, r, why", BELLMAN_P_REFUSALS_ITERATES, ids=BELLMAN_P_IDS_ITERATES)
def test_bellman_fixed_point_iterates_refuse_bad_matrices_and_rewards(mk, P, r, why):
    steps = 0 if "0 steps" in why else 3
    _expect_error(ValueError, lambda: mk.bellman_fixed_point_iterates(P, r, 0.7, n_steps=steps),
                  f"bellman_fixed_point_iterates({P!r}, {r!r}, 0.7, n_steps={steps})", why)


@pytest.mark.parametrize("gamma, why", GAMMA_REFUSALS, ids=GAMMA_IDS)
def test_bellman_fixed_point_iterates_refuse_bad_gammas(mk, gamma, why):
    _expect_error(ValueError, lambda: mk.bellman_fixed_point_iterates(PB, RB, gamma, n_steps=3),
                  f"bellman_fixed_point_iterates({PB!r}, {RB!r}, {gamma!r}, n_steps=3)", why)


START_REFUSALS = [({"V0": [1.0]}, "V0 has 1 entry for 2 states"),
                  ({"V0": [1.0], "n_steps": 0}, "V0 has 1 entry for 2 states, even for 0 steps"),
                  ({"V0": [1.0, 2.0, 3.0]}, "V0 has 3 entries for 2 states"),
                  ({"V0": [[1.0, 2.0]]}, "V0 is 2-D"),
                  ({"V0": 1.0, "n_steps": 0}, "V0 is a number, not 1-D"),
                  ({"n_steps": -1}, "a negative number of steps"),
                  ({"n_steps": 2.5}, "a number of steps that is not an integer"),
                  ({"n_steps": 2.0}, "the float 2.0 is refused"),
                  ({"n_steps": True}, "a bool (True)"),
                  ({"n_steps": False}, "a bool (False), even though False == 0"),
                  ({"n_steps": None}, "n_steps is None"),
                  ({"n_steps": "3"}, "n_steps is a string")]
START_IDS = ["V0-shorter", "V0-shorter-no-step", "V0-longer", "V0-two-d", "V0-scalar-no-step", "steps-negative",
             "steps-fraction", "steps-float", "steps-true", "steps-false", "steps-none", "steps-string"]


@pytest.mark.parametrize("kwargs, why", START_REFUSALS, ids=START_IDS)
def test_bellman_fixed_point_iterates_refuse_bad_starts_or_steps(mk, kwargs, why):
    _expect_error(ValueError, lambda: mk.bellman_fixed_point_iterates(PB, RB, 0.7, **kwargs),
                  f"bellman_fixed_point_iterates({PB!r}, {RB!r}, 0.7, {kwargs})", why)
