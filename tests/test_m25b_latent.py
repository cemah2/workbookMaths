"""Tests of mymath.latent (chapter M25b): the responsibilities of a Gaussian mixture (the E step of EM), the weighted
maximum likelihood (the M step), the log-likelihood of a mixture, and its evidence lower bound (ELBO) for any
responsibilities.

Oracles: ``scipy.stats.multivariate_normal`` (``logpdf``) and ``scipy.stats.norm`` (dimension 1, with the standard
deviation) for the log-densities, ``scipy.special.logsumexp`` along the rows for the responsibilities and the
log-likelihood, ``scipy.special.entr`` (``-r ln r``, with ``0 ln 0 = 0``) for the entropy of the ELBO and
``scipy.special.rel_entr`` for the KL divergence to the posterior; ``np.average(weights=…)`` and
``np.cov(aweights=…, bias=True)`` for the M step, the proportion, the mean and the covariance of each group for
responsibilities equal to 0 or 1; scikit-learn's ``GaussianMixture`` (``predict_proba``, ``score_samples``, and one
step of EM with ``max_iter=1``, ``weights_init``, ``means_init``, ``precisions_init`` and ``reg_covar``). Plus
properties: rows that sum to 1, points far from every component (no ``0/0``), components renumbered, the M step that
maximizes the weighted log-likelihood, ``reg`` on the diagonal, ELBO ≤ log-likelihood with equality at the posterior and
a gap equal to the KL divergences, EM without regularization that never goes down, ``0 ln 0 = 0``, inputs left
unchanged, Python floats and arrays of floats, lists of integers, dimension 1 as a column ``(n, 1)``, and the refusals
of the docstrings. They describe the expected behaviour without showing the solution.

    pytest tests/test_m25b_latent.py              # your code
    pytest tests/test_m25b_latent.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings

import numpy as np
import pytest
from scipy import special, stats
from sklearn.mixture import GaussianMixture


@pytest.fixture
def lat(mymath_module):
    return mymath_module("latent")


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


def _matches(got, value, rtol=1e-9, atol=1e-11):
    """Whether the result got equals the value of a classic error (same shape, close)."""
    try:
        got, value = np.asarray(got, dtype=float), np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        return False
    return got.shape == value.shape and bool(np.all(np.isfinite(value))) and np.allclose(got, value, rtol=rtol,
                                                                                         atol=atol)


def _first_match(got, want, candidates, rtol=1e-9, atol=1e-11):
    """The text of the first classic error whose value got matches (and that differs from the right value), or ""."""
    for value, text in candidates:
        if not _matches(value, want, rtol, atol) and _matches(got, value, rtol, atol):
            return text
    return ""


def _spd(rng, d, scale=1.0, floor=0.3):
    """A random symmetric positive definite (d, d) matrix, exactly symmetric, of moderate condition number."""
    B = rng.normal(size=(d, d))
    S = scale * (B @ B.T / d + floor * np.eye(d))
    return (S + S.T) / 2


def _random_mixture(rng, K, d, spread=3.0, scale=1.0):
    """Random weights (all > 0, summing to 1), means (K, d) and covariance matrices (K, d, d)."""
    w = rng.dirichlet(np.full(K, 3.0))
    w = w / w.sum()
    mu = rng.normal(size=(K, d)) * spread
    S = np.array([_spd(rng, d, scale=scale) for _ in range(K)])
    return w, mu, S


def _draw(rng, n, w, mu, S):
    """n points of the mixture, one per row (ancestral sampling: a component, then a point of its normal law)."""
    z = rng.choice(len(w), size=n, p=w)
    L = np.linalg.cholesky(S)
    E = rng.standard_normal((n, mu.shape[1]))
    return mu[z] + np.einsum("nij,nj->ni", L[z], E)


# --- the oracles ----------------------------------------------------------------------------------------------------

def _log_joint(X, w, mu, S):
    """a[i, k] = ln π_k + ln N(x_i | μ_k, Σ_k) by scipy.stats.multivariate_normal, an (n, K) array."""
    X = np.asarray(X, dtype=float)
    w, mu, S = (np.asarray(v, dtype=float) for v in (w, mu, S))
    n = X.shape[0]
    columns = [np.reshape(stats.multivariate_normal(mean=mu[k], cov=S[k]).logpdf(X), (n,)) for k in range(w.size)]
    return np.column_stack(columns) + np.log(w)


def _posterior(X, w, mu, S):
    """The responsibilities p(z = k | x_i): exp(a - scipy.special.logsumexp(a, axis=1))."""
    a = _log_joint(X, w, mu, S)
    return np.exp(a - special.logsumexp(a, axis=1, keepdims=True))


def _log_likelihood(X, w, mu, S):
    """Σ_i scipy.special.logsumexp(a[i])."""
    return float(np.sum(special.logsumexp(_log_joint(X, w, mu, S), axis=1)))


def _elbo(X, R, w, mu, S):
    """Σ r a + Σ entr(r), with entr(r) = -r ln r and entr(0) = 0 (scipy.special.entr)."""
    R = np.asarray(R, dtype=float)
    a = _log_joint(X, w, mu, S)
    return float(np.sum(np.where(R > 0, R * a, 0.0)) + np.sum(special.entr(R)))


def _m_step(X, R, reg=0.0):
    """The M step by np.average(weights=…) and np.cov(aweights=…, bias=True), one component at a time."""
    X, R = np.asarray(X, dtype=float), np.asarray(R, dtype=float)
    d, K = X.shape[1], R.shape[1]
    weights = np.mean(R, axis=0)
    means = np.array([np.average(X, axis=0, weights=R[:, k]) for k in range(K)])
    covs = np.array([np.atleast_2d(np.cov(X.T, aweights=R[:, k], bias=True)) + reg * np.eye(d) for k in range(K)])
    return weights, means, covs


def _sklearn_mixture(w, mu, S):
    """A GaussianMixture of scikit-learn with these parameters (no fit): predict_proba and score_samples."""
    gm = GaussianMixture(n_components=len(w), covariance_type="full")
    gm.weights_, gm.means_, gm.covariances_ = np.asarray(w, float), np.asarray(mu, float), np.asarray(S, float)
    gm.precisions_cholesky_ = np.array([np.linalg.inv(np.linalg.cholesky(s)).T for s in gm.covariances_])
    return gm


def _symmetric_by_the_rule(A):
    """The rule of mvn_logpdf (M25a): |A[i, j] - A[j, i]| ≤ 1e-12 · max(1, max |A|) for every entry."""
    return bool(np.all(np.abs(A - A.T) <= 1e-12 * max(1.0, float(np.max(np.abs(A))))))


# --- what the module may use ------------------------------------------------------------------------------------

def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``cov`` (from numpy import cov) → "numpy.cov". Relative imports (from .gaussian import
    mvn_logpdf) are your own modules: they are not listed."""
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
    ("gmm_m_step", "numpy.cov"); ``where`` is the top-level function, or "the module level"."""
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


def _getattr_uses(tree, forbidden):
    """getattr(…, "cov") and the like: a forbidden name reached through a string."""
    found = []
    for statement in tree.body:
        where = _where(statement)
        for node in ast.walk(statement):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "getattr"
                    and any(isinstance(a, ast.Constant) and a.value in forbidden for a in node.args)):
                found.append(f"getattr(…, {next(a.value for a in node.args if isinstance(a, ast.Constant))!r}) in "
                             f"{where}")
    return found


ALLOWED_LINALG = ("cholesky", "solve", "LinAlgError")


def test_module_uses_only_numpy_cholesky_and_solve_and_neither_cov_average_scipy_nor_sklearn(lat):
    """The docstring allows NumPy, but not np.cov nor np.average, from np.linalg only cholesky and solve (and
    np.linalg.LinAlgError, an exception), no SciPy at all and no scikit-learn. Only the code counts: a comment, a
    docstring or an import never used is not a use. Relative imports of your own modules (from .gaussian import
    mvn_logpdf, from .approx import logsumexp) are allowed."""
    try:
        tree = ast.parse(inspect.getsource(lat))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = []
    for where, path in _uses(tree, _imported_names(tree)):
        parts = path.split(".")
        shown = ".".join(["np"] + parts[1:]) if parts[0] == "numpy" else path
        if parts[0] in ("scipy", "sklearn"):
            found.append(f"{shown} in {where}")
        elif parts[0] == "numpy" and ("cov" in parts[1:] or "average" in parts[1:]):
            found.append(f"{shown} in {where}")
        elif parts[0] == "numpy" and len(parts) > 2 and parts[1] == "linalg" and parts[2] not in ALLOWED_LINALG:
            found.append(f"{shown} in {where}")
    found += _getattr_uses(tree, {"cov", "average"})
    assert not found, (f"expected NumPy without np.cov nor np.average, with from np.linalg only cholesky and solve, "
                       f"no SciPy and no scikit-learn, found {sorted(set(found))} (the tests compare your results "
                       f"with np.cov(aweights=…), np.average(weights=…), scipy.stats.multivariate_normal, "
                       f"scipy.special.logsumexp and GaussianMixture: write the computation yourself, with mvn_logpdf "
                       f"and NumPy)")


# --- gmm_e_step -----------------------------------------------------------------------------------------------------

E_STEP_HINT = ("a[i, k] = ln π_k + mvn_logpdf(X, μ_k, Σ_k) (one column per component), then "
               "r[i, k] = exp(a[i, k] - logsumexp_j a[i, j]): each ROW sums to 1")


def _e_step_hint(got, X, w, mu, S):
    """E_STEP_HINT, plus the classic error that the responsibilities got match, if any."""
    a = _log_joint(X, w, mu, S)
    want = np.exp(a - special.logsumexp(a, axis=1, keepdims=True))
    no_weights = a - np.log(np.asarray(w, dtype=float))
    with np.errstate(all="ignore"):
        candidates = [
            (np.exp(a - special.logsumexp(a, axis=0, keepdims=True)),
             "the logsumexp was taken over the points (axis 0): it is taken over the components, along each row"),
            (np.exp(no_weights - special.logsumexp(no_weights, axis=1, keepdims=True)),
             "the weights π_k are missing: a[i, k] = ln π_k + ln N(x_i | μ_k, Σ_k)"),
            (a - special.logsumexp(a, axis=1, keepdims=True), "these are the logarithms ln r[i, k]: take np.exp"),
            (np.exp(a), "π_k N(x_i | μ_k, Σ_k) must be divided by its sum over the components k"),
            (np.exp(a - np.max(a, axis=1, keepdims=True)), "subtracting the row maximum is not enough: subtract the "
                                                           "whole logsumexp of the row"),
        ]
    text = _first_match(got, want, candidates)
    return f"{E_STEP_HINT}; here {text}" if text else E_STEP_HINT


def test_gmm_e_step_docstring_examples(lat):
    X, w, m, C = [[0.5], [2.0], [3.5], [6.0]], [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]]
    call = "gmm_e_step([[0.5], [2.0], [3.5], [6.0]], [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]])"
    R = _result(lambda: lat.gmm_e_step(X, w, m, C), "an array of shape (4, 2)", call)
    _float_array(R, (4, 2), call)
    want = [[0.9924, 0.0076], [0.8444, 0.1556], [0.0678, 0.9322], [0.0, 1.0]]
    assert np.array_equal(np.round(R, 4), want), (
        f"expected np.round({call}, 4) = {_show(want)}, got {_show(R)} ({_e_step_hint(R, X, w, m, C)})")
    _close(R.sum(axis=1), np.ones(4), f"the row sums of {call}", rtol=0, atol=1e-12, hint=E_STEP_HINT)
    call = "gmm_e_step([[1000.0]], [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]])"
    R = _result(lambda: lat.gmm_e_step([[1000.0]], w, m, C), "array([[0., 1.]])", call,
                "far away, both densities underflow to 0: compute in logarithms, never π_k N / Σ_j π_j N")
    _float_array(R, (1, 2), call)
    _close(R, [[0.0, 1.0]], f"{call} (far away: no 0/0)", rtol=0, atol=1e-12, hint=E_STEP_HINT)


E_CASES = [(1, 1, 1, "one point, one component"), (7, 1, 3, "dimension 1: a column (7, 1)"),
           (40, 2, 2, "40 points in dimension 2"), (25, 3, 4, "4 components in dimension 3"),
           (60, 5, 3, "dimension 5"), (12, 2, 5, "5 components, 12 points"), (1, 4, 2, "a single row (1, 4)"),
           (30, 8, 2, "dimension 8")]


@pytest.mark.parametrize("n, d, K, text", E_CASES, ids=[f"n{n}-d{d}-K{K}" for n, d, K, _ in E_CASES])
def test_gmm_e_step_matches_bayes_with_scipy(lat, n, d, K, text):
    """r[i, k] = exp(a[i, k] - logsumexp_j a[i, j]), a by scipy.stats.multivariate_normal and the logsumexp by
    scipy.special.logsumexp; every row is a law on the components."""
    rng = np.random.default_rng(5950 + E_CASES.index((n, d, K, text)))
    w, mu, S = _random_mixture(rng, K, d)
    X = _draw(rng, n, w, mu, S)
    want = _posterior(X, w, mu, S)
    what = f"gmm_e_step(X, weights, means, covs) for {text}"
    got = _result(lambda: lat.gmm_e_step(X, w, mu, S), f"an array of shape ({n}, {K})", what)
    _float_array(got, (n, K), f"{what} (one row per point, one column per component)")
    _close(got, want, f"{what}, the posterior of Bayes (scipy)", rtol=1e-9, atol=1e-12,
           hint=_e_step_hint(got, X, w, mu, S))
    assert np.all(got >= 0) and np.all(got <= 1 + 1e-12), (
        f"expected responsibilities between 0 and 1 for {what}, got min {got.min():.3g} and max {got.max():.3g}")
    _close(got.sum(axis=1), np.ones(n), f"the row sums of {what}", rtol=0, atol=1e-12, hint=E_STEP_HINT)


def test_gmm_e_step_matches_scikit_learn_predict_proba(lat):
    """GaussianMixture(...).predict_proba with the same weights, means and covariances."""
    rng = np.random.default_rng(5963)
    for K, d, n in ((2, 2, 30), (3, 4, 50), (4, 1, 20)):
        w, mu, S = _random_mixture(rng, K, d, spread=2.0)
        X = _draw(rng, n, w, mu, S)
        want = _sklearn_mixture(w, mu, S).predict_proba(X)
        what = f"gmm_e_step(X, weights, means, covs) for {K} components in dimension {d}"
        got = _result(lambda: lat.gmm_e_step(X, w, mu, S), f"an array of shape ({n}, {K})", what)
        _float_array(got, (n, K), what)
        _close(got, want, f"{what}, GaussianMixture.predict_proba(X)", rtol=1e-8, atol=1e-11,
               hint=_e_step_hint(got, X, w, mu, S))


def test_gmm_e_step_far_from_every_component_has_no_0_over_0(lat):
    """Far from every component, every density underflows to 0 (π_k N / Σ_j π_j N would be 0/0), but the
    responsibilities stay a law. Two components with the same covariance, and a point far away in a direction where
    their ratio does not move: the responsibilities are neither 0 nor 1."""
    shared = np.array([[1.6, 0.5], [0.5, 0.9]])
    mu = np.array([[-1.25, 0.5], [1.75, -0.25]])
    w = np.array([0.35, 0.65])
    S = np.array([shared, shared])
    diff = mu[0] - mu[1]
    v = shared @ np.array([-diff[1], diff[0]])        # (μ0 - μ1)ᵀ Σ⁻¹ v = 0: the ratio of the densities is constant
    X = np.array([(mu[0] + mu[1]) / 2 + 400.0 * v / np.linalg.norm(v),
                  (mu[0] + mu[1]) / 2 - 650.0 * v / np.linalg.norm(v) + 0.1 * diff,
                  [-730.0, 455.0]])
    a = _log_joint(X, w, mu, S)
    assert np.all(np.exp(a) == 0.0)                     # the oracle: every density underflows
    want = _posterior(X, w, mu, S)
    assert 0.05 < want[0, 0] < 0.95 and 0.05 < want[1, 0] < 0.95    # neither 0 nor 1
    what = "gmm_e_step for three points far from both components"
    got = _result(lambda: lat.gmm_e_step(X, w, mu, S), "an array of shape (3, 2)", what,
                  "every density underflows to 0 here: compute ln r = a - logsumexp(a) along each row, then np.exp")
    _float_array(got, (3, 2), what)
    _close(got, want, f"{what}, the posterior of Bayes in logarithms (scipy.special.logsumexp)", rtol=1e-8,
           atol=1e-12, hint=_e_step_hint(got, X, w, mu, S))
    in_1d = _result(lambda: lat.gmm_e_step([[-420.0], [515.0]], [0.55, 0.45], [[-1.5], [2.5]], [[[0.8]], [[1.7]]]),
                    "an array of shape (2, 2)", "two far points in dimension 1")
    want = _posterior([[-420.0], [515.0]], [0.55, 0.45], [[-1.5], [2.5]], [[[0.8]], [[1.7]]])
    _close(in_1d, want, "gmm_e_step([[-420.0], [515.0]], [0.55, 0.45], [[-1.5], [2.5]], [[[0.8]], [[1.7]]]), where the "
                        "wider component takes everything", rtol=1e-9, atol=1e-12, hint=E_STEP_HINT)


def test_gmm_e_step_permuting_the_components_permutes_the_columns(lat):
    """The numbering of the components is arbitrary: weights, means and covariances listed in another order give
    the same responsibilities, their columns in that order."""
    rng = np.random.default_rng(5959)
    w, mu, S = _random_mixture(rng, 4, 3)
    X = _draw(rng, 35, w, mu, S)
    base = _result(lambda: lat.gmm_e_step(X, w, mu, S), "an array of shape (35, 4)", "the components in order")
    _float_array(base, (35, 4), "gmm_e_step(X, weights, means, covs)")
    for order in ([2, 0, 3, 1], [3, 2, 1, 0]):
        got = _result(lambda: lat.gmm_e_step(X, w[order], mu[order], S[order]), "an array of shape (35, 4)",
                      f"the components in the order {order}")
        _close(got, base[:, order], f"gmm_e_step with the components in the order {order}, the columns of the first "
                                    f"result in that order", rtol=1e-10, atol=1e-13,
               hint="column k goes with weights[k], means[k] and covs[k]")


def test_gmm_e_step_identical_components_share_by_their_weights_and_one_component_takes_all(lat):
    """K copies of the same normal law: the data tell nothing, r[i, k] = π_k. A single component: r = 1."""
    rng = np.random.default_rng(5960)
    X = rng.normal(size=(9, 2)) * 2.0
    cov = _spd(rng, 2)
    w = np.array([0.15, 0.25, 0.6])
    got = _result(lambda: lat.gmm_e_step(X, w, np.tile([0.5, -1.0], (3, 1)), np.array([cov, cov, cov])),
                  "an array of shape (9, 3)", "three identical components")
    _float_array(got, (9, 3), "gmm_e_step for three identical components")
    _close(got, np.tile(w, (9, 1)), "gmm_e_step for three identical components, the weights on every row",
           rtol=1e-12, atol=1e-14, hint="the densities cancel out in r[i, k]: only the prior π_k is left")
    got = _result(lambda: lat.gmm_e_step(X, [1.0], [[0.5, -1.0]], [cov]), "an array of shape (9, 1)",
                  "one component")
    _float_array(got, (9, 1), "gmm_e_step for one component (K = 1)")
    _close(got, np.ones((9, 1)), "gmm_e_step for one component, a column of ones", rtol=0, atol=1e-14,
           hint=E_STEP_HINT)


def test_gmm_e_step_in_dimension_1_uses_variances(lat):
    """In dimension 1, covs[k] = [[σ_k²]] holds a variance: scipy.stats.norm takes the standard deviation σ_k."""
    X = np.array([[-1.2], [0.4], [2.9], [3.3], [7.5], [8.1]])
    w, mu, var = np.array([0.35, 0.65]), np.array([0.8, 6.2]), np.array([1.44, 2.25])
    a = np.column_stack([stats.norm.logpdf(X[:, 0], loc=mu[k], scale=math.sqrt(var[k])) for k in range(2)]) + np.log(w)
    want = np.exp(a - special.logsumexp(a, axis=1, keepdims=True))
    what = "gmm_e_step for a column (6, 1), means 0.8 and 6.2, variances 1.44 and 2.25"
    got = _result(lambda: lat.gmm_e_step(X, w, mu[:, None], var[:, None, None]), "an array of shape (6, 2)", what)
    _float_array(got, (6, 2), what)
    hint = _e_step_hint(got, X, w, mu[:, None], var[:, None, None])
    a_sd = np.column_stack([stats.norm.logpdf(X[:, 0], loc=mu[k], scale=var[k]) for k in range(2)]) + np.log(w)
    if _matches(got, np.exp(a_sd - special.logsumexp(a_sd, axis=1, keepdims=True))):
        hint += "; covs holds variances σ² (here σ = 1.2 and 1.5), not standard deviations"
    _close(got, want, f"{what} (scipy.stats.norm with scale = √variance)", rtol=1e-10, atol=1e-13, hint=hint)


def test_gmm_e_step_takes_lists_of_integers_and_returns_floats(lat):
    X = [[3, -1], [0, 3], [-2, 4], [6, 5], [2, 1]]
    w = [0.25, 0.75]
    mu = [[1, 1], [4, 3]]
    S = [[[4, 1], [1, 3]], [[2, -1], [-1, 5]]]
    want = _posterior(np.array(X, float), w, np.array(mu, float), np.array(S, float))
    for given, text in ((lambda v: v, "lists of integers"), (np.array, "integer arrays")):
        what = f"gmm_e_step with {text}"
        got = _result(lambda: lat.gmm_e_step(given(X), given(w), given(mu), given(S)), "an array of shape (5, 2)",
                      what)
        _float_array(got, (5, 2), what)
        _close(got, want, what, rtol=1e-10, atol=1e-13, hint=E_STEP_HINT)


def test_gmm_e_step_accepts_weights_summing_to_one_within_1e_9(lat):
    """Weights summing to 1 + 6e-10 are valid (the tolerance is 1e-9)."""
    X = np.array([[0.2, 1.1], [-0.7, 0.3], [2.4, -1.9]])
    w = np.array([0.3, 0.7 + 6e-10])
    mu = np.array([[0.0, 0.5], [1.5, -0.5]])
    S = np.array([[[1.3, 0.4], [0.4, 0.9]], [[2.1, -0.6], [-0.6, 1.1]]])
    got = _result(lambda: lat.gmm_e_step(X, w, mu, S), "an array of shape (3, 2)", "weights summing to 1 + 6e-10",
                  "weights are valid when they sum to 1 up to 1e-9")
    _close(got, _posterior(X, w, mu, S), "gmm_e_step with weights summing to 1 + 6e-10", rtol=1e-9,
           hint=E_STEP_HINT)


def test_gmm_e_step_does_not_modify_its_inputs(lat):
    rng = np.random.default_rng(5962)
    w, mu, S = _random_mixture(rng, 3, 2)
    X = _draw(rng, 10, w, mu, S)
    copies = [v.copy() for v in (X, w, mu, S)]
    _result(lambda: lat.gmm_e_step(X, w, mu, S), "an array of shape (10, 3)", "float arrays")
    for name, value, copy in zip(("X", "weights", "means", "covs"), (X, w, mu, S), copies):
        assert np.array_equal(value, copy), (
            f"expected {name} unchanged by gmm_e_step, got {name} = {_show(value)} (never modify the arrays you "
            f"receive: a - b makes a new array, a -= b writes into a)")


X2 = [[0.3, -1.2], [2.2, 0.7], [-0.9, 1.6]]
W2 = [0.3, 0.7]
M2 = [[0.0, 0.5], [1.5, -0.5]]
C2 = [[[1.3, 0.4], [0.4, 0.9]], [[2.1, -0.6], [-0.6, 1.1]]]
MIXTURE_REFUSALS = [
    ([0.3, -1.2], W2, M2, C2, "X is 1-D: one point is a row [[0.3, -1.2]]"),
    ([0.4, 1.1, 2.0], W2, [[0.0], [1.5]], [[[1.3]], [[2.1]]], "a 1-D X in dimension 1: 3 points form a column (3, 1)"),
    (np.zeros((0, 2)), W2, M2, C2, "X has no row"),
    (np.zeros((3, 0)), W2, np.zeros((2, 0)), np.zeros((2, 0, 0)), "X has no column (d = 0)"),
    (np.zeros((2, 3, 2)), W2, M2, C2, "X is 3-D"),
    ([[0.3, -1.2], [np.nan, 0.7]], W2, M2, C2, "X holds a nan"),
    ([[0.3, -1.2], [2.2, np.inf]], W2, M2, C2, "X holds an inf"),
    ([[0.3, -1.2, 0.0], [2.2, 0.7, 1.0]], W2, M2, C2, "X has 3 columns for means of 2 coordinates"),
    (X2, [[0.3, 0.7]], M2, C2, "weights is 2-D"),
    (X2, [], np.zeros((0, 2)), np.zeros((0, 2, 2)), "weights is empty (K = 0)"),
    (X2, 1.0, [[0.0, 0.5]], [[[1.3, 0.4], [0.4, 0.9]]], "weights is a number, not 1-D: write [1.0]"),
    (X2, [0.0, 1.0], M2, C2, "a weight is 0"),
    (X2, [-0.2, 1.2], M2, C2, "a weight is negative"),
    (X2, [0.3, 0.6], M2, C2, "the weights sum to 0.9"),
    (X2, [0.3, 0.7 + 1e-8], M2, C2, "the weights sum to 1 + 1e-8, beyond the tolerance 1e-9"),
    (X2, [np.nan, 1.0], M2, C2, "a weight is nan"),
    (X2, [0.2, 0.3, 0.5], M2, C2, "3 weights for 2 means and 2 covariance matrices"),
    (X2, W2, [0.0, 0.5], C2, "means is 1-D"),
    (X2, W2, [[0.0, 0.5], [1.5, -0.5], [1.0, 1.0]], C2, "3 means for 2 weights"),
    (X2, W2, [[0.0, 0.5, 0.0], [1.5, -0.5, 0.0]], C2, "means of 3 coordinates for points of 2"),
    (X2, W2, M2, [[1.3, 0.4], [0.4, 0.9]], "covs is one 2 × 2 matrix, not (K, d, d)"),
    (X2, W2, M2, [[[1.3, 0.4], [0.4, 0.9]]], "1 covariance matrix for 2 components"),
    (X2, W2, M2, np.stack([np.eye(3), np.eye(3)]), "covs holds 3 × 3 matrices for d = 2"),
    (X2, W2, M2, [[[1.3, 0.4], [-0.4, 0.9]], C2[1]], "a covariance matrix is not symmetric"),
    (X2, W2, M2, [C2[0], [[1.0, 2.5], [2.5, 1.0]]], "a covariance matrix is not positive definite"),
    (X2, W2, M2, [C2[0], [[1.0, 2.0], [2.0, 4.0]]], "a covariance matrix is only semi-definite (a pivot is exactly 0)"),
    (X2, W2, M2, [[[-1.3, 0.0], [0.0, 0.9]], C2[1]], "a covariance matrix has a negative variance"),
]
MIXTURE_IDS = ["X-one-d", "X-one-d-in-dimension-1", "X-no-row", "X-no-column", "X-three-d", "X-nan", "X-inf",
               "X-columns", "weights-two-d", "weights-empty", "weights-scalar", "weights-zero", "weights-negative",
               "weights-sum", "weights-sum-beyond-tolerance", "weights-nan", "weights-count", "means-one-d",
               "means-rows", "means-columns", "covs-two-d", "covs-count", "covs-size", "covs-not-symmetric",
               "covs-indefinite", "covs-semi-definite", "covs-negative-variance"]


@pytest.mark.parametrize("X, weights, means, covs, why", MIXTURE_REFUSALS, ids=MIXTURE_IDS)
def test_gmm_e_step_refusals(lat, X, weights, means, covs, why):
    _expect_error(ValueError, lambda: lat.gmm_e_step(X, weights, means, covs),
                  f"gmm_e_step({X!r}, {weights!r}, {means!r}, {covs!r})", why)


# --- gmm_m_step -----------------------------------------------------------------------------------------------------

M_STEP_HINT = ("N_k = Σ_i r[i, k] (resp.sum(axis=0)); π_k = N_k / n; μ_k = (1 / N_k) Σ_i r[i, k] x_i; "
               "Σ_k = (1 / N_k) Σ_i r[i, k] (x_i - μ_k)(x_i - μ_k)ᵀ + reg · I")


def _m_step_hints(got, X, R, reg):
    """M_STEP_HINT, plus the classic errors that the weights, means and covariances got match, if any."""
    X, R = np.asarray(X, dtype=float), np.asarray(R, dtype=float)
    n, d = X.shape
    K = R.shape[1]
    N = R.sum(axis=0)
    w, mu, S = _m_step(X, R, reg)
    eye = np.eye(d)
    weights = [(N, "π_k = N_k / n: divide N_k by the number of points n"),
               (N / K, "π_k = N_k / n, with n the number of points, not K the number of components"),
               (np.full(K, 1 / K), "the weights do not stay 1 / K: π_k = N_k / n")]
    means = [((R.T @ X) / n, "μ_k = (1 / N_k) Σ_i r[i, k] x_i: divide by N_k, not by n"),
             (np.tile(X.mean(axis=0), (K, 1)), "the responsibilities were not used: μ_k = (1 / N_k) Σ_i r[i, k] x_i")]

    def covs_with(center, divide, add):
        out = []
        for k in range(K):
            dev = X - center[k]
            out.append((R[:, k, None] * dev).T @ dev / divide[k] + add)
        return np.array(out)

    with np.errstate(all="ignore"):
        covs = [(covs_with(mu, np.full(K, n), reg * eye), "Σ_k divides by N_k, not by n"),
                (covs_with(np.zeros((K, d)), N, reg * eye), "Σ_k is centred: x_i - μ_k, not x_i"),
                (covs_with(np.tile(X.mean(axis=0), (K, 1)), N, reg * eye),
                 "Σ_k is centred on μ_k, the mean of component k, not on the mean of all the points"),
                (covs_with(mu, N - 1, reg * eye), "Σ_k divides by N_k (maximum likelihood), not by N_k - 1"),
                (covs_with(mu, N, 0 * eye), "reg · I is missing (reg is added to the diagonal)"),
                (covs_with(mu, N, reg * np.ones((d, d))), "reg is added to the diagonal only: reg · I, not reg on "
                                                         "every entry"),
                (covs_with(mu, N, 0 * eye) * (1 + reg), "reg is added to the diagonal: + reg · I, not a factor")]
    texts = []
    for part, (value, want, candidates) in zip(("weights", "means", "covs"),
                                               zip(got, (w, mu, S), (weights, means, covs))):
        text = _first_match(value, want, candidates)
        if text:
            texts.append(f"{part}: {text}")
    return M_STEP_HINT + (f"; here {'; '.join(texts)}" if texts else "")


def _check_m_step(got, K, d, what):
    """A tuple of three float arrays (weights (K,), means (K, d), covs (K, d, d))."""
    assert isinstance(got, tuple) and len(got) == 3, (
        f"expected a tuple (weights, means, covs) for {what}, got {type(got).__name__}"
        + (f" of length {len(got)}" if isinstance(got, (tuple, list)) else ""))
    _float_array(got[0], (K,), f"the weights returned by {what}")
    _float_array(got[1], (K, d), f"the means returned by {what}")
    _float_array(got[2], (K, d, d), f"the covariance matrices returned by {what}")
    return got


def _compare_m_step(got, X, R, reg, what, rtol=1e-9, atol=1e-12):
    want = _m_step(X, R, reg)
    hint = _m_step_hints(got, X, R, reg)
    for part, value, expected, oracle in zip(("weights", "means", "covariance matrices"), got, want,
                                             ("the mean of each column of resp",
                                              "np.average(X, axis=0, weights=resp[:, k])",
                                              f"np.cov(X.T, aweights=resp[:, k], bias=True) + {reg} · I")):
        _close(value, expected, f"the {part} of {what}, {oracle}", rtol=rtol, atol=atol, hint=hint)


def test_gmm_m_step_docstring_examples(lat):
    call = "gmm_m_step([[0.5], [2.0], [3.5], [6.0]], [[1, 0], [1, 0], [0, 1], [0, 1]])"
    got = _result(lambda: lat.gmm_m_step([[0.5], [2.0], [3.5], [6.0]], [[1, 0], [1, 0], [0, 1], [0, 1]]),
                  "(weights, means, covs)", call)
    w, m, C = _check_m_step(got, 2, 1, call)
    hint = _m_step_hints(got, [[0.5], [2.0], [3.5], [6.0]], [[1, 0], [1, 0], [0, 1], [0, 1]], 0.0)
    _close(w, [0.5, 0.5], f"the weights of {call}", rtol=1e-12, hint=hint)
    _close(m, [[1.25], [4.75]], f"the means of {call}", rtol=1e-12, hint=hint)
    _close(C, [[[0.5625]], [[1.5625]]], f"the covariance matrices of {call}", rtol=1e-12, hint=hint)
    X = [[0, 0], [1, 0], [0, 2], [4, 4], [5, 3]]
    R = [[1, 0], [1, 0], [1, 0], [0, 1], [0, 1]]
    call = ("gmm_m_step(X, [[1, 0], [1, 0], [1, 0], [0, 1], [0, 1]], reg=0.1), "
            "X = [[0, 0], [1, 0], [0, 2], [4, 4], [5, 3]]")
    got = _result(lambda: lat.gmm_m_step(X, R, reg=0.1), "(weights, means, covs)", call)
    w, m, C = _check_m_step(got, 2, 2, call)
    hint = _m_step_hints(got, X, R, 0.1)
    _close(w, [0.6, 0.4], f"the weights of {call}", rtol=1e-12, hint=hint)
    assert np.array_equal(np.round(m, 4), [[0.3333, 0.6667], [4.5, 3.5]]), (
        f"expected np.round(means, 4) = [[0.3333, 0.6667], [4.5, 3.5]] for {call}, got {_show(m)} ({hint})")
    assert np.array_equal(np.round(C[1], 4), [[0.35, -0.25], [-0.25, 0.35]]), (
        f"expected np.round(covs[1], 4) = [[0.35, -0.25], [-0.25, 0.35]] for {call} (two points: singular without "
        f"reg), got {_show(C[1])} ({hint})")


M_CASES = [(9, 1, 2, 0.0, "dimension 1: a column (9, 1)"), (40, 2, 3, 0.0, "40 points in dimension 2"),
           (25, 3, 2, 0.25, "dimension 3 with reg = 0.25"), (60, 4, 4, 0.0, "4 components in dimension 4"),
           (6, 2, 5, 1e-3, "5 components and only 6 points, reg = 0.001"), (1, 3, 1, 0.5, "one point, reg = 0.5"),
           (30, 6, 3, 0.0, "dimension 6")]


@pytest.mark.parametrize("n, d, K, reg, text", M_CASES, ids=[f"n{n}-d{d}-K{K}" for n, d, K, _, _ in M_CASES])
def test_gmm_m_step_matches_np_average_and_np_cov_with_weights(lat, n, d, K, reg, text):
    """Responsibilities drawn at random (rows of a Dirichlet law): weights, means and covariances against
    np.average(weights=resp[:, k]) and np.cov(aweights=resp[:, k], bias=True)."""
    rng = np.random.default_rng(5965 + M_CASES.index((n, d, K, reg, text)))
    X = rng.normal(size=(n, d)) * 2.0 + rng.normal(size=d)
    R = rng.dirichlet(np.full(K, 0.8), size=n)
    what = f"gmm_m_step(X, resp, reg={reg}) for {text}"
    got = _result(lambda: lat.gmm_m_step(X, R, reg=reg), "(weights, means, covs)", what)
    _check_m_step(got, K, d, what)
    _compare_m_step(got, X, R, reg, what)


def test_gmm_m_step_hard_responsibilities_give_proportion_mean_and_covariance_of_each_group(lat):
    """Responsibilities equal to 0 or 1: the proportion of each group, its mean and its covariance (dividing by its
    size), computed here group by group."""
    rng = np.random.default_rng(5972)
    for n, d, K in ((30, 2, 3), (45, 3, 2), (12, 1, 2)):
        X = rng.normal(size=(n, d)) * 3.0
        labels = np.concatenate([np.arange(K), rng.integers(0, K, size=n - K)])
        rng.shuffle(labels)
        labels[:d + 2] = 0                              # every group holds enough points (here: group 0)
        labels[d + 2:2 * (d + 2)] = 1
        R = np.eye(K)[labels]
        what = f"gmm_m_step(X, resp) for responsibilities equal to 0 or 1, {K} groups in dimension {d}"
        got = _result(lambda: lat.gmm_m_step(X, R), "(weights, means, covs)", what)
        w, m, C = _check_m_step(got, K, d, what)
        hint = _m_step_hints(got, X, R, 0.0)
        for k in range(K):
            group = X[labels == k]
            dev = group - group.mean(axis=0)
            _close_number(float(w[k]), len(group) / n, f"the weight of group {k} for {what}, its proportion "
                                                       f"{len(group)}/{n}", rtol=1e-12, hint=hint)
            _close(m[k], group.mean(axis=0), f"the mean of group {k} for {what}", rtol=1e-10, atol=1e-12, hint=hint)
            _close(C[k], dev.T @ dev / len(group), f"the covariance of group {k} for {what}, dividing by its size "
                                                  f"{len(group)}", rtol=1e-10, atol=1e-12, hint=hint)


def test_gmm_m_step_reg_is_added_to_the_diagonal_of_every_covariance(lat):
    """reg changes neither the weights nor the means, and adds reg · I to every covariance matrix."""
    rng = np.random.default_rng(5973)
    X = rng.normal(size=(20, 3)) * 1.5
    R = rng.dirichlet(np.ones(3), size=20)
    base = _result(lambda: lat.gmm_m_step(X, R), "(weights, means, covs)", "reg = 0 (the default)")
    _check_m_step(base, 3, 3, "gmm_m_step(X, resp)")
    _compare_m_step(base, X, R, 0.0, "gmm_m_step(X, resp) with the default reg = 0")
    for reg in (0.37, 2, 1e-6):
        what = f"gmm_m_step(X, resp, reg={reg!r})"
        got = _result(lambda: lat.gmm_m_step(X, R, reg=reg), "(weights, means, covs)", what)
        _check_m_step(got, 3, 3, what)
        hint = _m_step_hints(got, X, R, float(reg))
        _close(got[0], base[0], f"the weights of {what}, the same as with reg = 0", rtol=1e-13, atol=1e-15, hint=hint)
        _close(got[1], base[1], f"the means of {what}, the same as with reg = 0", rtol=1e-13, atol=1e-15, hint=hint)
        _close(got[2], base[2] + reg * np.eye(3), f"the covariance matrices of {what}, those of reg = 0 plus "
                                                  f"{reg} · I", rtol=1e-12, atol=1e-14, hint=hint)


def test_gmm_m_step_maximizes_the_weighted_log_likelihood(lat):
    """For reg = 0, the parameters of the M step maximize Q(θ) = Σ_i Σ_k r[i, k] (ln π_k + ln N(x_i | μ_k, Σ_k))
    (scipy.stats.multivariate_normal): moving the weights, a mean or a covariance matrix a little lowers it."""
    rng = np.random.default_rng(5974)
    X = _draw(rng, 80, *_random_mixture(rng, 3, 2))
    R = rng.dirichlet(np.full(3, 1.5), size=80)
    got = _result(lambda: lat.gmm_m_step(X, R), "(weights, means, covs)", "random responsibilities")
    w, m, C = _check_m_step(got, 3, 2, "gmm_m_step(X, resp)")
    sym = np.array([(c + c.T) / 2 for c in C])
    assert np.all(np.linalg.eigvalsh(sym) > 0), (
        f"expected positive definite covariance matrices for 80 points and 3 components, got the eigenvalues "
        f"{_show(np.linalg.eigvalsh(sym))} ({_m_step_hints(got, X, R, 0.0)})")

    def Q(weights, means, covs):
        return float(np.sum(R * _log_joint(X, weights, means, covs)))

    best = Q(w, m, sym)
    moves = []
    for k in range(3):
        for t in (-0.03, 0.03):
            moved = w.copy()
            moved[k] += t
            moved[(k + 1) % 3] -= t
            moves.append((moved, m, sym, f"weight {k} moved by {t}"))
        for _ in range(2):
            shifted = m.copy()
            shifted[k] += rng.normal(size=2) * 0.05
            moves.append((w, shifted, sym, f"mean {k} shifted"))
        for factor in (0.95, 1.05):
            scaled = sym.copy()
            scaled[k] = factor * sym[k]
            moves.append((w, m, scaled, f"covariance of component {k} multiplied by {factor}"))
        tilted = sym.copy()
        tilted[k] = sym[k] + 0.02 * np.array([[0.0, 1.0], [1.0, 0.0]])
        moves.append((w, m, tilted, f"covariance {k} with its off-diagonal entries + 0.02"))
    for weights, means, covs, text in moves:
        other = Q(weights, means, covs)
        assert other <= best + 1e-9 * abs(best), (
            f"expected Q(θ) = Σ r[i, k] (ln π_k + ln N(x_i | μ_k, Σ_k)) to be largest at the parameters of the M step "
            f"({best:.10g}), got {other:.10g} with the {text} ({_m_step_hints(got, X, R, 0.0)})")


def test_gmm_m_step_after_gmm_e_step_is_one_em_step_of_scikit_learn(lat):
    """One step of EM: gmm_m_step(X, gmm_e_step(X, θ), reg) gives the parameters of GaussianMixture(max_iter=1,
    weights_init, means_init, precisions_init = Σ⁻¹, reg_covar=reg).fit(X)."""
    for seed, K, d, n, reg in ((5975, 2, 2, 60, 0.0), (5976, 3, 3, 90, 0.05), (5977, 4, 1, 50, 0.0)):
        rng = np.random.default_rng(seed)
        w, mu, S = _random_mixture(rng, K, d)
        X = _draw(rng, n, *_random_mixture(rng, K, d))
        gm = GaussianMixture(n_components=K, covariance_type="full", max_iter=1, tol=0.0, reg_covar=reg,
                             weights_init=w, means_init=mu, precisions_init=np.array([np.linalg.inv(s) for s in S]),
                             init_params="random_from_data", random_state=0)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            gm.fit(X)
        what = f"one EM step from random parameters, {K} components in dimension {d}, reg = {reg}"
        R = _result(lambda: lat.gmm_e_step(X, w, mu, S), f"an array of shape ({n}, {K})", f"the E step of {what}")
        _float_array(R, (n, K), f"gmm_e_step for the E step of {what}")
        _close(R, _posterior(X, w, mu, S), f"the responsibilities of the E step of {what} (scipy), before the M step",
               rtol=1e-9, atol=1e-12, hint=_e_step_hint(R, X, w, mu, S))
        got = _result(lambda: lat.gmm_m_step(X, R, reg=reg), "(weights, means, covs)", f"the M step of {what}")
        weights, means, covs = _check_m_step(got, K, d, f"gmm_m_step for {what}")
        hint = _m_step_hints(got, X, R, reg)
        _close(weights, gm.weights_, f"the weights after {what}, GaussianMixture.weights_", rtol=1e-8, atol=1e-11,
               hint=hint)
        _close(means, gm.means_, f"the means after {what}, GaussianMixture.means_", rtol=1e-8, atol=1e-10, hint=hint)
        _close(covs, gm.covariances_, f"the covariance matrices after {what}, GaussianMixture.covariances_",
               rtol=1e-8, atol=1e-10, hint=hint)


def test_gmm_m_step_with_one_component_is_the_maximum_likelihood_of_m25a(lat):
    """K = 1, every responsibility 1: the weight 1, the mean of the data and their covariance dividing by n."""
    rng = np.random.default_rng(5979)
    X = rng.normal(size=(15, 3)) @ _spd(rng, 3) + np.array([2.0, -1.0, 0.5])
    got = _result(lambda: lat.gmm_m_step(X, np.ones((15, 1))), "(weights, means, covs)", "one component")
    w, m, C = _check_m_step(got, 1, 3, "gmm_m_step(X, np.ones((15, 1)))")
    hint = _m_step_hints(got, X, np.ones((15, 1)), 0.0)
    _close(w, [1.0], "the weight of a single component", rtol=1e-14, hint=hint)
    _close(m[0], X.mean(axis=0), "the mean of a single component, X.mean(axis=0)", rtol=1e-12, atol=1e-14, hint=hint)
    _close(C[0], np.cov(X.T, bias=True), "the covariance of a single component, np.cov(X.T, bias=True) (dividing by "
                                         "n)", rtol=1e-11, atol=1e-13, hint=hint)


def test_gmm_m_step_returns_valid_parameters(lat):
    """Weights > 0 summing to 1, covariance matrices symmetric (by the rule of mvn_logpdf) and positive
    semi-definite: gmm_e_step accepts them when they are definite."""
    rng = np.random.default_rng(5978)
    for n, d, K, reg in ((50, 2, 3, 0.0), (8, 4, 2, 0.0), (20, 3, 4, 0.1)):
        X = rng.normal(size=(n, d)) * rng.uniform(0.5, 4.0, size=d)
        R = rng.dirichlet(np.full(K, 0.5), size=n)
        what = f"gmm_m_step(X, resp, reg={reg}) for {n} points in dimension {d}, {K} components"
        got = _result(lambda: lat.gmm_m_step(X, R, reg=reg), "(weights, means, covs)", what)
        w, m, C = _check_m_step(got, K, d, what)
        assert np.all(w > 0) and abs(float(np.sum(w)) - 1.0) <= 1e-12, (
            f"expected weights > 0 summing to 1 for {what}, got {_show(w)} of sum {float(np.sum(w)):.15g} "
            f"({M_STEP_HINT})")
        for k in range(K):
            assert _symmetric_by_the_rule(C[k]), (
                f"expected a symmetric covariance matrix {k} for {what} "
                f"(|Σ[i, j] - Σ[j, i]| ≤ 1e-12 · max(1, max |Σ|), the rule of mvn_logpdf), got a largest asymmetry "
                f"of {np.max(np.abs(C[k] - C[k].T)):.3g}")
            eig = np.linalg.eigvalsh((C[k] + C[k].T) / 2)
            assert eig.min() >= reg - 1e-10 * max(1.0, eig.max()), (
                f"expected a positive semi-definite covariance matrix {k} for {what}, with eigenvalues ≥ reg = {reg}, "
                f"got the eigenvalues {_show(eig)} ({M_STEP_HINT})")


def test_gmm_m_step_returns_a_singular_covariance_without_any_check(lat):
    """With reg = 0, a component carried by d points or fewer gets a singular covariance matrix, returned as
    computed; gmm_e_step then refuses it (its Cholesky decomposition fails)."""
    X = np.array([[1.0, 2.0], [3.0, 6.0], [-2.0, 0.5], [0.0, -1.5], [2.5, 1.0]])
    R = np.array([[1, 0], [1, 0], [0, 1], [0, 1], [0, 1]], dtype=float)
    what = "gmm_m_step(X, resp) with component 0 carried by two points (1, 2) and (3, 6)"
    got = _result(lambda: lat.gmm_m_step(X, R), "(weights, means, covs)", what,
                  "with reg = 0 the covariance matrices are returned as computed, without any check")
    w, m, C = _check_m_step(got, 2, 2, what)
    _close(C[0], [[1.0, 2.0], [2.0, 4.0]], f"the covariance of component 0 for {what}, singular (rank 1)", rtol=1e-12,
           atol=1e-14, hint=_m_step_hints(got, X, R, 0.0))
    _compare_m_step(got, X, R, 0.0, what)
    _expect_error(ValueError, lambda: lat.gmm_e_step(X, w, m, C), "gmm_e_step with the singular covariance [[1, 2], "
                  "[2, 4]] returned by gmm_m_step", "its Cholesky decomposition fails: mvn_logpdf refuses it")
    one = np.eye(2)[[0, 1, 1, 1, 1]]
    got = _result(lambda: lat.gmm_m_step(X, one), "(weights, means, covs)", "component 0 carried by one point")
    _close(got[2][0], np.zeros((2, 2)), "the covariance of a component carried by the single point (1, 2), the zero "
                                        "matrix", rtol=0, atol=1e-15, hint=M_STEP_HINT)
    _expect_error(ValueError, lambda: lat.gmm_e_step(X, got[0], got[1], got[2]), "gmm_e_step with a zero covariance "
                  "matrix returned by gmm_m_step", "the zero matrix is not positive definite")


def test_gmm_m_step_in_dimension_1_returns_variances(lat):
    """In dimension 1, X is a column (n, 1): the covariance matrices are (K, 1, 1), the weighted variances."""
    X = np.array([[4.1], [5.3], [4.7], [9.8], [10.4], [11.0], [9.5]])
    R = np.array([[0.9, 0.1], [0.8, 0.2], [1.0, 0.0], [0.05, 0.95], [0.0, 1.0], [0.1, 0.9], [0.3, 0.7]])
    what = "gmm_m_step on a column (7, 1)"
    got = _result(lambda: lat.gmm_m_step(X, R), "(weights, means, covs)", what)
    w, m, C = _check_m_step(got, 2, 1, what)
    for k in range(2):
        mean = float(np.average(X[:, 0], weights=R[:, k]))
        var = float(np.average((X[:, 0] - mean) ** 2, weights=R[:, k]))
        _close(m[k], [mean], f"the mean of component {k} for {what}", rtol=1e-12, hint=_m_step_hints(got, X, R, 0.0))
        _close(C[k], [[var]], f"the variance of component {k} for {what} (a variance σ², not σ)", rtol=1e-11,
               hint=_m_step_hints(got, X, R, 0.0))
    _close(w, R.mean(axis=0), f"the weights of {what}", rtol=1e-12, hint=M_STEP_HINT)


def test_gmm_m_step_takes_lists_of_integers_and_returns_floats(lat):
    X = [[2, 7], [3, 5], [-1, 6], [8, -2], [9, 0], [7, -1]]
    R = [[1, 0], [1, 0], [1, 0], [0, 1], [0, 1], [0, 1]]
    for given, reg, text in ((lambda v: v, 0, "lists of integers, reg = 0 (an int)"),
                             (np.array, np.int64(1), "integer arrays, reg = np.int64(1)"),
                             (lambda v: v, np.float32(0.5), "lists of integers, reg = np.float32(0.5)")):
        what = f"gmm_m_step with {text}"
        got = _result(lambda: lat.gmm_m_step(given(X), given(R), reg=reg), "(weights, means, covs)", what,
                      "reg may be any finite number >= 0: an int, a NumPy number")
        _check_m_step(got, 2, 2, what)
        _compare_m_step(got, X, R, float(reg), what, rtol=1e-7 if isinstance(reg, np.float32) else 1e-12)


def test_gmm_m_step_accepts_rows_summing_to_one_within_1e_9_and_a_nearly_empty_component(lat):
    X = np.array([[0.5, 1.5], [2.5, -0.5], [1.0, 1.0], [3.5, 2.0]])
    R = np.array([[0.6, 0.4], [0.2, 0.8 - 7e-10], [1.0, 0.0], [0.0, 1.0 + 4e-10]])
    got = _result(lambda: lat.gmm_m_step(X, R), "(weights, means, covs)", "rows summing to 1 ± 7e-10",
                  "each row of resp sums to 1 up to 1e-9")
    _check_m_step(got, 2, 2, "gmm_m_step with rows summing to 1 - 7e-10 and 1 + 4e-10")
    R = np.array([[1.0, 0.0], [1.0 - 1e-6, 1e-6], [1.0, 0.0], [0.0, 1.0]])
    got = _result(lambda: lat.gmm_m_step(X, R), "(weights, means, covs)", "a component with N_k = 1 + 1e-6",
                  "only a column of exact zeros (N_k = 0) is refused")
    _check_m_step(got, 2, 2, "gmm_m_step with a component of N_k = 1 + 1e-6")
    _compare_m_step(got, X, R, 0.0, "gmm_m_step with a component of N_k = 1 + 1e-6", rtol=1e-8, atol=1e-10)


def test_gmm_m_step_does_not_modify_its_inputs(lat):
    rng = np.random.default_rng(5964)
    X = rng.normal(size=(12, 3))
    R = rng.dirichlet(np.ones(2), size=12)
    copies = [X.copy(), R.copy()]
    got = _result(lambda: lat.gmm_m_step(X, R, reg=0.2), "(weights, means, covs)", "float arrays")
    for name, value, copy in zip(("X", "resp"), (X, R), copies):
        assert np.array_equal(value, copy), (
            f"expected {name} unchanged by gmm_m_step, got {name} = {_show(value)} (never modify the arrays you "
            f"receive: X - means[k] makes a new array, X -= means[k] writes into X)")
    for part in got:
        part[...] = 99.0
    assert np.array_equal(X, copies[0]) and np.array_equal(R, copies[1]), (
        "expected gmm_m_step to return new arrays, but changing them changed X or resp")


XM = [[0.4, 1.0], [2.0, -0.6], [1.2, 3.1], [-0.8, 0.2]]
RM = [[0.7, 0.3], [0.1, 0.9], [0.5, 0.5], [1.0, 0.0]]
M_STEP_REFUSALS = [
    ([0.4, 2.0, 1.2, -0.8], RM, 0.0, "X is 1-D: in dimension 1, 4 points form a column (4, 1)"),
    (np.zeros((0, 2)), np.zeros((0, 2)), 0.0, "X has no row"),
    (np.zeros((4, 0)), RM, 0.0, "X has no column (d = 0)"),
    (np.zeros((4, 2, 1)), RM, 0.0, "X is 3-D"),
    ([[0.4, 1.0], [2.0, np.nan], [1.2, 3.1], [-0.8, 0.2]], RM, 0.0, "X holds a nan"),
    ([[0.4, 1.0], [2.0, -0.6], [-np.inf, 3.1], [-0.8, 0.2]], RM, 0.0, "X holds an inf"),
    (XM, [0.7, 0.1, 0.5, 1.0], 0.0, "resp is 1-D"),
    (XM, RM[:3], 0.0, "resp has 3 rows for 4 points"),
    (XM, RM + [[0.5, 0.5]], 0.0, "resp has 5 rows for 4 points"),
    (XM, np.zeros((4, 0)), 0.0, "resp has no column (K = 0)"),
    (XM, np.ones((4, 2, 1)) / 2, 0.0, "resp is 3-D"),
    (XM, [[0.7, 0.3], [0.1, 0.9], [np.nan, 0.5], [1.0, 0.0]], 0.0, "resp holds a nan"),
    (XM, [[0.7, 0.3], [0.1, 0.9], [0.5, 0.5], [np.inf, 0.0]], 0.0, "resp holds an inf"),
    (XM, [[1.2, -0.2], [0.1, 0.9], [0.5, 0.5], [1.0, 0.0]], 0.0, "resp holds a negative value (its row sums to 1)"),
    (XM, [[0.7, 0.2], [0.1, 0.9], [0.5, 0.5], [1.0, 0.0]], 0.0, "row 0 of resp sums to 0.9"),
    (XM, [[0.7, 0.3], [0.1, 0.9 + 1e-8], [0.5, 0.5], [1.0, 0.0]], 0.0, "row 1 sums to 1 + 1e-8, beyond 1e-9"),
    (XM, [[1.0, 0.0], [1.0, 0.0], [1.0, 0.0], [1.0, 0.0]], 0.0, "a column of zeros: component 1 is empty "
                                                                 "(N_k = 0)"),
    (XM, [[0.5, 0.0, 0.5], [0.4, 0.0, 0.6], [1.0, 0.0, 0.0], [0.2, 0.0, 0.8]], 0.0, "a column of zeros in the middle"),
    (XM, RM, -0.1, "reg is negative"),
    (XM, RM, np.nan, "reg is nan"),
    (XM, RM, np.inf, "reg is inf"),
    (XM, RM, True, "reg is a bool (True)"),
    (XM, RM, False, "reg is a bool (False), even though False == 0"),
    (XM, RM, None, "reg is None"),
    (XM, RM, "0.2", "reg is a string"),
    (XM, RM, [0.2], "reg is a list, not a number"),
]
M_STEP_IDS = ["X-one-d", "X-no-row", "X-no-column", "X-three-d", "X-nan", "X-inf", "resp-one-d", "resp-fewer-rows",
              "resp-more-rows", "resp-no-column", "resp-three-d", "resp-nan", "resp-inf", "resp-negative",
              "resp-row-sum", "resp-row-sum-beyond-tolerance", "resp-column-of-zeros", "resp-middle-column-of-zeros",
              "reg-negative", "reg-nan", "reg-inf", "reg-true", "reg-false", "reg-none", "reg-string", "reg-list"]


@pytest.mark.parametrize("X, resp, reg, why", M_STEP_REFUSALS, ids=M_STEP_IDS)
def test_gmm_m_step_refusals(lat, X, resp, reg, why):
    _expect_error(ValueError, lambda: lat.gmm_m_step(X, resp, reg=reg), f"gmm_m_step({X!r}, {resp!r}, reg={reg!r})",
                  why)


# --- gmm_log_likelihood ---------------------------------------------------------------------------------------------

LL_HINT = ("Σ_i logsumexp_k a[i, k], with a[i, k] = ln π_k + mvn_logpdf(x_i, μ_k, Σ_k): the logarithm of a sum does "
           "not split")


def _ll_hint(got, X, w, mu, S):
    """LL_HINT, plus the classic error that the value got matches, if any."""
    X = np.asarray(X, dtype=float)
    a = _log_joint(X, w, mu, S)
    want = float(np.sum(special.logsumexp(a, axis=1)))
    no_weights = a - np.log(np.asarray(w, dtype=float))
    candidates = [
        (want / X.shape[0], "the log-likelihood is the sum over the points, not their mean (no division by n)"),
        (float(np.sum(np.max(a, axis=1))), "the maximum of each row is only the first term of the logsumexp: add "
                                           "ln Σ_k e^(a[i, k] - m_i)"),
        (float(np.sum(np.asarray(w, dtype=float) * no_weights)), "Σ_k π_k ln N(x_i | μ_k, Σ_k) is not "
                                                                 "ln Σ_k π_k N(x_i | μ_k, Σ_k)"),
        (float(np.sum(a)), "the sum over k of the logarithms: take the logsumexp of each row instead"),
        (float(np.sum(special.logsumexp(no_weights, axis=1))), "the weights π_k are missing: a[i, k] = ln π_k + …"),
        (float(np.sum(special.logsumexp(a, axis=0))), "take the logsumexp along each row (axis=1, over the components), "
                                                       "not along each column"),
    ]
    text = _first_match(got, want, candidates, rtol=1e-9, atol=1e-9)
    return f"{LL_HINT}; here {text}" if text else LL_HINT


def test_gmm_log_likelihood_docstring_examples(lat):
    X, w, m, C = [[0.5], [2.0], [3.5], [6.0]], [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]]
    call = "gmm_log_likelihood([[0.5], [2.0], [3.5], [6.0]], [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]])"
    got = _result(lambda: lat.gmm_log_likelihood(X, w, m, C), "-8.4137 (rounded)", call)
    _float(got, call)
    assert round(got, 4) == -8.4137, f"expected round({call}, 4) = -8.4137, got {got!r} ({_ll_hint(got, X, w, m, C)})"
    call = "gmm_log_likelihood([[1000.0]], [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]])"
    got = _result(lambda: lat.gmm_log_likelihood([[1000.0]], w, m, C), "-247508.0 (rounded)", call,
                  "far away, both densities underflow to 0 and ln 0 = -inf: use the logsumexp of a[i, :]")
    _float(got, call)
    assert round(got, 1) == -247508.0, (
        f"expected round({call}, 1) = -247508.0 (not -inf), got {got!r} ({_ll_hint(got, [[1000.0]], w, m, C)})")


LL_CASES = [(1, 1, 1, "one point, one component"), (8, 1, 2, "dimension 1: a column (8, 1)"),
            (50, 2, 3, "50 points in dimension 2"), (30, 3, 2, "dimension 3"),
            (45, 5, 4, "4 components in dimension 5"),
            (2, 2, 6, "6 components and 2 points"), (20, 10, 2, "dimension 10")]


@pytest.mark.parametrize("n, d, K, text", LL_CASES, ids=[f"n{n}-d{d}-K{K}" for n, d, K, _ in LL_CASES])
def test_gmm_log_likelihood_matches_scipy(lat, n, d, K, text):
    """Σ_i scipy.special.logsumexp(a[i]), a by scipy.stats.multivariate_normal."""
    rng = np.random.default_rng(5980 + LL_CASES.index((n, d, K, text)))
    w, mu, S = _random_mixture(rng, K, d)
    X = _draw(rng, n, w, mu, S)
    want = _log_likelihood(X, w, mu, S)
    what = f"gmm_log_likelihood(X, weights, means, covs) for {text}"
    got = _result(lambda: lat.gmm_log_likelihood(X, w, mu, S), f"{want:.12g}", what)
    _float(got, what)
    _close_number(got, want, f"{what}, Σ_i logsumexp(a[i]) by scipy", rtol=1e-10, atol=1e-10,
                  hint=_ll_hint(got, X, w, mu, S))


def test_gmm_log_likelihood_matches_scikit_learn_score_samples(lat):
    """GaussianMixture(...).score_samples(X).sum(), ln p(x_i) added over the points."""
    rng = np.random.default_rng(5987)
    for K, d, n in ((2, 3, 40), (5, 2, 70), (3, 1, 25)):
        w, mu, S = _random_mixture(rng, K, d, spread=2.5)
        X = _draw(rng, n, w, mu, S)
        want = float(_sklearn_mixture(w, mu, S).score_samples(X).sum())
        what = f"gmm_log_likelihood for {K} components in dimension {d}"
        got = _result(lambda: lat.gmm_log_likelihood(X, w, mu, S), f"{want:.12g}", what)
        _float(got, what)
        _close_number(got, want, f"{what}, GaussianMixture.score_samples(X).sum()", rtol=1e-9, atol=1e-9,
                      hint=_ll_hint(got, X, w, mu, S))


def test_gmm_log_likelihood_far_from_every_component_stays_finite(lat):
    """Far away, every density underflows to 0 and ln 0 = -inf, but the logsumexp is an ordinary number."""
    rng = np.random.default_rng(5988)
    w, mu, S = _random_mixture(rng, 3, 2)
    X = np.array([[650.0, -480.0], [-905.0, 12.5], [3.0, 1.5]])
    a = _log_joint(X, w, mu, S)
    assert np.all(np.exp(a[:2]) == 0.0)                 # the oracle: every density underflows on the first two rows
    want = _log_likelihood(X, w, mu, S)
    what = "gmm_log_likelihood for two points far from every component and one near"
    got = _result(lambda: lat.gmm_log_likelihood(X, w, mu, S), f"{want:.12g}", what,
                  "factor out the maximum of each row: m_i + ln Σ_k e^(a[i, k] - m_i)")
    _float(got, what)
    _close_number(got, want, f"{what} (scipy.special.logsumexp), finite although every density underflows",
                  rtol=1e-11, hint=_ll_hint(got, X, w, mu, S))


def test_gmm_log_likelihood_is_a_sum_over_the_points_and_ignores_the_numbering(lat):
    """The log-likelihood of two sets of points is the sum of theirs (it is a sum over the points, not a mean), and
    listing the components in another order changes nothing."""
    rng = np.random.default_rng(5989)
    w, mu, S = _random_mixture(rng, 3, 3)
    X = _draw(rng, 30, w, mu, S)
    whole = _result(lambda: lat.gmm_log_likelihood(X, w, mu, S), "a float", "30 points")
    first = _result(lambda: lat.gmm_log_likelihood(X[:12], w, mu, S), "a float", "the first 12 points")
    rest = _result(lambda: lat.gmm_log_likelihood(X[12:], w, mu, S), "a float", "the other 18 points")
    _close_number(whole, first + rest, "gmm_log_likelihood of 30 points, the sum of those of the first 12 and of the "
                                       "other 18", rtol=1e-12, atol=1e-10, hint=_ll_hint(whole, X, w, mu, S))
    _close_number(whole, _log_likelihood(X, w, mu, S), "gmm_log_likelihood of 30 points (scipy)", rtol=1e-10,
                  hint=_ll_hint(whole, X, w, mu, S))
    order = [1, 2, 0]
    got = _result(lambda: lat.gmm_log_likelihood(X, w[order], mu[order], S[order]), "a float",
                  "the components in another order")
    _close_number(got, whole, "gmm_log_likelihood with the components in the order [1, 2, 0], the same value",
                  rtol=1e-12, atol=1e-11, hint="weights[k], means[k] and covs[k] go together")


def test_gmm_log_likelihood_with_one_component_is_a_sum_of_log_densities(lat):
    """K = 1: ln Σ_k π_k N(x_i | …) = ln N(x_i | μ, Σ), and the log-likelihood is Σ_i ln N(x_i | μ, Σ)."""
    rng = np.random.default_rng(5990)
    cov, mean = _spd(rng, 4, scale=2.0), rng.normal(size=4)
    X = mean + rng.normal(size=(11, 4)) * 1.5
    want = float(np.sum(stats.multivariate_normal(mean=mean, cov=cov).logpdf(X)))
    got = _result(lambda: lat.gmm_log_likelihood(X, [1.0], [mean], [cov]), f"{want:.12g}", "one component")
    _float(got, "gmm_log_likelihood for one component")
    _close_number(got, want, "gmm_log_likelihood for one component, Σ_i ln N(x_i | μ, Σ) (scipy)", rtol=1e-11,
                  hint=LL_HINT)


def test_gmm_log_likelihood_in_dimension_1_uses_variances(lat):
    X = np.array([[-1.2], [0.4], [2.9], [3.3], [7.5], [8.1]])
    w, mu, var = np.array([0.35, 0.65]), np.array([0.8, 6.2]), np.array([1.44, 2.25])
    dens = sum(w[k] * stats.norm.pdf(X[:, 0], loc=mu[k], scale=math.sqrt(var[k])) for k in range(2))
    want = float(np.sum(np.log(dens)))
    what = "gmm_log_likelihood for a column (6, 1), means 0.8 and 6.2, variances 1.44 and 2.25"
    got = _result(lambda: lat.gmm_log_likelihood(X, w, mu[:, None], var[:, None, None]), f"{want:.12g}", what)
    _float(got, what)
    _close_number(got, want, f"{what}, Σ_i ln Σ_k π_k φ_k(x_i) (scipy.stats.norm with scale = √variance)",
                  rtol=1e-11, hint=_ll_hint(got, X, w, mu[:, None], var[:, None, None]))


def test_gmm_log_likelihood_takes_lists_of_integers_and_returns_a_python_float(lat):
    X = [[3, -1], [0, 3], [-2, 4], [6, 5], [2, 1]]
    w, mu, S = [0.25, 0.75], [[1, 1], [4, 3]], [[[4, 1], [1, 3]], [[2, -1], [-1, 5]]]
    want = _log_likelihood(np.array(X, float), w, np.array(mu, float), np.array(S, float))
    for given, text in ((lambda v: v, "lists of integers"), (np.array, "integer arrays")):
        what = f"gmm_log_likelihood with {text}"
        got = _result(lambda: lat.gmm_log_likelihood(given(X), given(w), given(mu), given(S)), f"{want:.12g}", what)
        _float(got, what)
        _close_number(got, want, what, rtol=1e-11, hint=LL_HINT)


def test_gmm_log_likelihood_does_not_modify_its_inputs(lat):
    rng = np.random.default_rng(5991)
    w, mu, S = _random_mixture(rng, 2, 3)
    X = _draw(rng, 9, w, mu, S)
    copies = [v.copy() for v in (X, w, mu, S)]
    _result(lambda: lat.gmm_log_likelihood(X, w, mu, S), "a float", "float arrays")
    for name, value, copy in zip(("X", "weights", "means", "covs"), (X, w, mu, S), copies):
        assert np.array_equal(value, copy), (
            f"expected {name} unchanged by gmm_log_likelihood, got {name} = {_show(value)} (never modify the arrays "
            f"you receive)")


@pytest.mark.parametrize("X, weights, means, covs, why", MIXTURE_REFUSALS, ids=MIXTURE_IDS)
def test_gmm_log_likelihood_refusals(lat, X, weights, means, covs, why):
    _expect_error(ValueError, lambda: lat.gmm_log_likelihood(X, weights, means, covs),
                  f"gmm_log_likelihood({X!r}, {weights!r}, {means!r}, {covs!r})", why)


# --- gmm_elbo -------------------------------------------------------------------------------------------------------

ELBO_HINT = ("Σ_i Σ_k r[i, k] (a[i, k] - ln r[i, k]), a[i, k] = ln π_k + mvn_logpdf(x_i, μ_k, Σ_k), with 0 ln 0 = 0: "
             "the expected log-joint plus the entropy of each q_i")


def _elbo_hint(got, X, R, w, mu, S):
    """ELBO_HINT, plus the classic error that the value got matches, if any."""
    X, R = np.asarray(X, dtype=float), np.asarray(R, dtype=float)
    a = _log_joint(X, w, mu, S)
    expected_log_joint = float(np.sum(np.where(R > 0, R * a, 0.0)))
    entropy = float(np.sum(special.entr(R)))
    want = expected_log_joint + entropy
    no_weights = a - np.log(np.asarray(w, dtype=float))
    candidates = [
        (expected_log_joint, "the entropy of q is missing: add - Σ_k r[i, k] ln r[i, k] for each point"),
        (expected_log_joint - entropy, "the entropy has the wrong sign: - r ln r ≥ 0 is added (ELBO = Σ r (a - ln r))"),
        (want / X.shape[0], "the ELBO is a sum over the points, not a mean (no division by n)"),
        (float(np.sum(np.where(R > 0, R * no_weights, 0.0))) + entropy, "ln π_k is missing from a[i, k]"),
        (_log_likelihood(X, w, mu, S), "this is the log-likelihood: the ELBO uses the given resp, whatever they are"),
    ]
    text = _first_match(got, want, candidates, rtol=1e-9, atol=1e-9)
    return f"{ELBO_HINT}; here {text}" if text else ELBO_HINT


def test_gmm_elbo_docstring_examples(lat):
    X, w, m, C = [[0.5], [2.0], [3.5], [6.0]], [0.4, 0.6], [[1.0], [5.0]], [[[1.0]], [[2.0]]]
    R = _result(lambda: lat.gmm_e_step(X, w, m, C), "an array of shape (4, 2)", "R = gmm_e_step(X, w, m, C)")
    elbo = _result(lambda: lat.gmm_elbo(X, R, w, m, C), "a float", "gmm_elbo(X, R, w, m, C)")
    ll = _result(lambda: lat.gmm_log_likelihood(X, w, m, C), "a float", "gmm_log_likelihood(X, w, m, C)")
    _float(elbo, "gmm_elbo(X, R, w, m, C)")
    assert abs(elbo - ll) < 1e-12, (
        f"expected abs(gmm_elbo(X, R, w, m, C) - gmm_log_likelihood(X, w, m, C)) < 1e-12 "
        f"for R = gmm_e_step(X, w, m, C) (q = the posterior), got {elbo!r} and {ll!r} "
        f"({_elbo_hint(elbo, X, R, w, m, C)})")
    hard = [[1, 0], [1, 0], [0, 1], [0, 1]]
    call = "gmm_elbo(X, [[1, 0], [1, 0], [0, 1], [0, 1]], w, m, C)"
    got = _result(lambda: lat.gmm_elbo(X, hard, w, m, C), "-8.6606 (rounded)", call,
                  "a term where r[i, k] = 0 counts for 0 (0 ln 0 = 0)")
    _float(got, call)
    assert round(got, 4) == -8.6606, (
        f"expected round({call}, 4) = -8.6606 (below -8.4137), got {got!r} ({_elbo_hint(got, X, hard, w, m, C)})")
    call = "gmm_elbo(X, [[0.5, 0.5]] * 4, w, m, C)"
    got = _result(lambda: lat.gmm_elbo(X, [[0.5, 0.5]] * 4, w, m, C), "-16.638 (rounded)", call)
    _float(got, call)
    assert round(got, 4) == -16.638, (
        f"expected round({call}, 4) = -16.638, got {got!r} ({_elbo_hint(got, X, [[0.5, 0.5]] * 4, w, m, C)})")


ELBO_CASES = [(1, 1, 1, 1.0, "one point, one component"), (10, 1, 3, 0.7, "dimension 1: a column (10, 1)"),
              (40, 2, 2, 2.0, "40 points in dimension 2"), (25, 3, 4, 0.4, "4 components in dimension 3"),
              (35, 5, 3, 1.0, "dimension 5"), (3, 2, 5, 0.3, "5 components and 3 points")]


@pytest.mark.parametrize("n, d, K, alpha, text", ELBO_CASES, ids=[f"n{n}-d{d}-K{K}" for n, d, K, _, _ in ELBO_CASES])
def test_gmm_elbo_matches_the_expected_log_joint_plus_the_entropy(lat, n, d, K, alpha, text):
    """For responsibilities drawn at random: Σ r a (a by scipy.stats.multivariate_normal) + Σ entr(r)
    (scipy.special.entr, -r ln r)."""
    rng = np.random.default_rng(5995 + ELBO_CASES.index((n, d, K, alpha, text)))
    w, mu, S = _random_mixture(rng, K, d)
    X = _draw(rng, n, w, mu, S)
    R = rng.dirichlet(np.full(K, alpha), size=n)
    want = _elbo(X, R, w, mu, S)
    what = f"gmm_elbo(X, resp, weights, means, covs) for {text} and random resp"
    got = _result(lambda: lat.gmm_elbo(X, R, w, mu, S), f"{want:.12g}", what)
    _float(got, what)
    _close_number(got, want, f"{what}, Σ r a + Σ (-r ln r) by scipy", rtol=1e-10, atol=1e-10,
                  hint=_elbo_hint(got, X, R, w, mu, S))


def test_gmm_elbo_never_exceeds_the_log_likelihood(lat):
    """ELBO(q) ≤ ln p(X) (Σ_i scipy.special.logsumexp) for responsibilities of every kind: drawn at random, with
    zeros, equal to 0 or 1, uniform."""
    rng = np.random.default_rng(6002)
    for K, d, n in ((2, 1, 15), (3, 2, 30), (4, 3, 20)):
        w, mu, S = _random_mixture(rng, K, d)
        X = _draw(rng, n, w, mu, S)
        ll = _log_likelihood(X, w, mu, S)
        sparse = rng.dirichlet(np.ones(K), size=n) * (rng.random((n, K)) < 0.6)
        sparse[np.arange(n), rng.integers(0, K, size=n)] += 0.5
        sparse /= sparse.sum(axis=1, keepdims=True)
        kinds = [(rng.dirichlet(np.full(K, 0.5), size=n), "drawn at random"), (sparse, "with zeros"),
                 (np.eye(K)[rng.integers(0, K, size=n)], "equal to 0 or 1"), (np.full((n, K), 1 / K), "uniform")]
        for R, kind in kinds:
            what = f"gmm_elbo for resp {kind}, {K} components in dimension {d}"
            got = _result(lambda: lat.gmm_elbo(X, R, w, mu, S), "a float", what)
            _float(got, what)
            assert got <= ll + 1e-10 * abs(ll), (
                f"expected {what} ≤ the log-likelihood {ll:.12g} (scipy), got {got:.12g} "
                f"({_elbo_hint(got, X, R, w, mu, S)})")
            _close_number(got, _elbo(X, R, w, mu, S), what, rtol=1e-10, atol=1e-10,
                          hint=_elbo_hint(got, X, R, w, mu, S))


def test_gmm_elbo_equals_the_log_likelihood_at_the_posterior(lat):
    """With q_i = p(z | x_i), the posterior (scipy), the ELBO is the log-likelihood, within 1e-10."""
    rng = np.random.default_rng(6003)
    for K, d, n in ((2, 2, 25), (3, 1, 40), (5, 4, 30)):
        w, mu, S = _random_mixture(rng, K, d, spread=1.5)
        X = _draw(rng, n, w, mu, S)
        R = _posterior(X, w, mu, S)
        ll = _log_likelihood(X, w, mu, S)
        what = f"gmm_elbo at the posterior, {K} components in dimension {d}"
        got = _result(lambda: lat.gmm_elbo(X, R, w, mu, S), f"{ll:.12g}", what)
        _float(got, what)
        _close_number(got, ll, f"{what}, equal to the log-likelihood (the KL divergence to the posterior is 0)",
                      rtol=1e-10, atol=1e-10, hint=_elbo_hint(got, X, R, w, mu, S))


def test_gmm_elbo_equals_the_log_likelihood_for_the_responsibilities_of_gmm_e_step(lat):
    """resp = gmm_e_step(X, θ) is the posterior: gmm_elbo(X, resp, θ) is the log-likelihood (scipy), within 1e-10."""
    rng = np.random.default_rng(6006)
    for K, d, n in ((2, 3, 30), (4, 2, 50), (3, 1, 20)):
        w, mu, S = _random_mixture(rng, K, d, spread=2.0)
        X = _draw(rng, n, w, mu, S)
        ll = _log_likelihood(X, w, mu, S)
        what = f"{K} components in dimension {d}"
        R = _result(lambda: lat.gmm_e_step(X, w, mu, S), f"an array of shape ({n}, {K})", f"gmm_e_step for {what}")
        got = _result(lambda: lat.gmm_elbo(X, R, w, mu, S), f"{ll:.12g}", f"gmm_elbo for {what}")
        _float(got, f"gmm_elbo(X, gmm_e_step(X, θ), θ) for {what}")
        _close_number(got, ll, f"gmm_elbo(X, gmm_e_step(X, θ), θ) for {what}, the log-likelihood", rtol=1e-10,
                      atol=1e-10, hint=f"the E step maximizes the ELBO in q: q = the posterior ({ELBO_HINT})")


def test_gmm_elbo_gap_is_the_sum_of_the_kl_divergences_to_the_posterior(lat):
    """ln p(X) - ELBO(q) = Σ_i KL(q_i ‖ p(z | x_i)), the KL divergences computed here by scipy.special.rel_entr."""
    rng = np.random.default_rng(6004)
    for K, d, n in ((2, 2, 20), (3, 3, 25), (4, 1, 30)):
        w, mu, S = _random_mixture(rng, K, d, spread=1.5)
        X = _draw(rng, n, w, mu, S)
        P = _posterior(X, w, mu, S)
        Q = rng.dirichlet(np.full(K, 1.2), size=n)
        Q[0] = np.eye(K)[0]                              # a row with zeros: 0 ln (0 / p) = 0
        kl = float(np.sum(special.rel_entr(Q, P)))
        ll = _log_likelihood(X, w, mu, S)
        what = f"gmm_elbo for random q, {K} components in dimension {d}"
        got = _result(lambda: lat.gmm_elbo(X, Q, w, mu, S), f"{ll - kl:.12g}", what)
        _float(got, what)
        _close_number(ll - got, kl, f"the gap ln p(X) - {what}, Σ_i KL(q_i ‖ p(z | x_i)) = Σ q ln(q / p)", rtol=1e-8,
                      atol=1e-10, hint=_elbo_hint(got, X, Q, w, mu, S))


def test_gmm_elbo_counts_zero_responsibilities_for_zero(lat):
    """0 ln 0 = 0: a term where r[i, k] = 0 counts for 0, even where a[i, k] is very negative, and a column of zeros
    is allowed here (an empty component)."""
    X = np.array([[0.2, -0.4], [1.8, 2.6], [-2.5, 0.9], [340.0, -275.0]])
    w = np.array([0.2, 0.5, 0.3])
    mu = np.array([[0.0, 0.0], [2.0, 2.5], [-2.0, 1.0]])
    S = np.array([[[1.0, 0.3], [0.3, 0.8]], [[0.6, 0.0], [0.0, 1.4]], [[2.2, -0.5], [-0.5, 1.1]]])
    for R, text in ((np.eye(3)[[0, 1, 2, 2]], "equal to 0 or 1, a far point given to component 2"),
                    (np.array([[0.5, 0.5, 0.0], [0.0, 1.0, 0.0], [0.25, 0.0, 0.75], [0.0, 0.0, 1.0]]), "with zeros"),
                    (np.array([[1.0, 0.0, 0.0], [0.3, 0.0, 0.7], [0.0, 0.0, 1.0], [0.6, 0.0, 0.4]]),
                     "with a column of zeros (component 1 empty)")):
        want = _elbo(X, R, w, mu, S)
        what = f"gmm_elbo for resp {text}"
        got = _result(lambda: lat.gmm_elbo(X, R, w, mu, S), f"{want:.12g}", what,
                      "0 ln 0 counts for 0: np.log(0) is -inf (with a RuntimeWarning) and 0 * -inf is nan; "
                      "use np.where")
        _float(got, what)
        assert math.isfinite(got), f"expected a finite number for {what} (0 ln 0 = 0), got {got!r} ({ELBO_HINT})"
        _close_number(got, want, what, rtol=1e-10, atol=1e-10, hint=_elbo_hint(got, X, R, w, mu, S))


def test_gmm_elbo_and_log_likelihood_never_decrease_along_em_without_reg(lat):
    """EM without regularization (reg = 0), from rough parameters, on mixtures drawn at random: the ELBO after each
    half step (E, then M, then E…) never goes down, after each E step it equals the log-likelihood, and the
    log-likelihood never goes down; each value is also checked against scipy. Tolerance: 1e-9 relative."""
    for seed, K, d, n, steps in ((6010, 2, 1, 120, 25), (6011, 3, 2, 180, 25), (6012, 2, 3, 150, 20),
                                 (6013, 4, 2, 240, 20)):
        rng = np.random.default_rng(seed)
        X = _draw(rng, n, *_random_mixture(rng, K, d, spread=3.5))
        w = np.full(K, 1 / K)
        mu = X[rng.choice(n, size=K, replace=False)]
        S = np.array([np.cov(X.T, bias=True).reshape(d, d)] * K)
        case = f"{K} components in dimension {d}, {n} points (seed {seed})"
        history = []
        previous_ll = -math.inf

        def value(name, call, oracle, step):
            got = _result(call, "a float", f"{name} at {step} of EM, {case}")
            _float(got, f"{name} at {step} of EM, {case}")
            _close_number(got, oracle, f"{name} at {step} of EM, {case} (scipy)", rtol=1e-9, atol=1e-9,
                          hint=ELBO_HINT if name == "gmm_elbo" else LL_HINT)
            return got

        for t in range(steps):
            R = _result(lambda: lat.gmm_e_step(X, w, mu, S), f"an array of shape ({n}, {K})",
                        f"gmm_e_step at iteration {t} of EM, {case}")
            ll = value("gmm_log_likelihood", lambda: lat.gmm_log_likelihood(X, w, mu, S),
                       _log_likelihood(X, w, mu, S), f"iteration {t}")
            elbo = value("gmm_elbo", lambda: lat.gmm_elbo(X, R, w, mu, S), _elbo(X, R, w, mu, S),
                         f"the E step of iteration {t}")
            _close_number(elbo, ll, f"the ELBO after the E step of iteration {t}, {case}, equal to the "
                                    f"log-likelihood", rtol=1e-10, atol=1e-10, hint=E_STEP_HINT)
            history.append((elbo, f"after the E step of iteration {t}"))
            if ll < previous_ll - 1e-9 * abs(previous_ll):
                pytest.fail(f"expected a log-likelihood that never goes down along EM without regularization, got "
                            f"{previous_ll:.12g} then {ll:.12g} at iteration {t}, {case} ({M_STEP_HINT})")
            previous_ll = ll
            got = _result(lambda: lat.gmm_m_step(X, R, reg=0.0), "(weights, means, covs)",
                          f"gmm_m_step at iteration {t} of EM, {case}")
            w, mu, S = _check_m_step(got, K, d, f"gmm_m_step at iteration {t} of EM, {case}")
            elbo = value("gmm_elbo", lambda: lat.gmm_elbo(X, R, w, mu, S), _elbo(X, R, w, mu, S),
                         f"the M step of iteration {t}")
            history.append((elbo, f"after the M step of iteration {t}"))
        for (before, when_before), (after, when) in zip(history, history[1:]):
            assert after >= before - 1e-9 * abs(before), (
                f"expected an ELBO that never goes down along EM without regularization, got {before:.12g} "
                f"{when_before} then {after:.12g} {when}, {case} (the E step maximizes it in q, the M step in θ: "
                f"{M_STEP_HINT})")
        assert history[-1][0] > history[0][0] + 1e-6 * abs(history[0][0]), (
            f"expected EM to raise the ELBO from rough parameters, got {history[0][0]:.12g} at the start and "
            f"{history[-1][0]:.12g} at the end, {case} ({M_STEP_HINT})")


def test_gmm_elbo_in_dimension_1_uses_variances(lat):
    X = np.array([[-1.2], [0.4], [2.9], [3.3], [7.5], [8.1]])
    w, mu, var = np.array([0.35, 0.65]), np.array([0.8, 6.2]), np.array([1.44, 2.25])
    R = np.array([[0.9, 0.1], [0.75, 0.25], [0.4, 0.6], [0.3, 0.7], [0.0, 1.0], [0.05, 0.95]])
    a = np.column_stack([stats.norm.logpdf(X[:, 0], loc=mu[k], scale=math.sqrt(var[k])) for k in range(2)]) + np.log(w)
    want = float(np.sum(np.where(R > 0, R * a, 0.0)) + np.sum(special.entr(R)))
    what = "gmm_elbo for a column (6, 1), means 0.8 and 6.2, variances 1.44 and 2.25"
    got = _result(lambda: lat.gmm_elbo(X, R, w, mu[:, None], var[:, None, None]), f"{want:.12g}", what)
    _float(got, what)
    _close_number(got, want, f"{what} (scipy.stats.norm with scale = √variance)", rtol=1e-11,
                  hint=_elbo_hint(got, X, R, w, mu[:, None], var[:, None, None]))


def test_gmm_elbo_takes_lists_of_integers_and_returns_a_python_float(lat):
    X = [[3, -1], [0, 3], [-2, 4], [6, 5], [2, 1]]
    w, mu, S = [0.25, 0.75], [[1, 1], [4, 3]], [[[4, 1], [1, 3]], [[2, -1], [-1, 5]]]
    R = [[1, 0], [1, 0], [1, 0], [0, 1], [0, 1]]
    want = _elbo(np.array(X, float), np.array(R, float), w, np.array(mu, float), np.array(S, float))
    for given, text in ((lambda v: v, "lists of integers"), (np.array, "integer arrays")):
        what = f"gmm_elbo with {text}"
        got = _result(lambda: lat.gmm_elbo(given(X), given(R), given(w), given(mu), given(S)), f"{want:.12g}", what)
        _float(got, what)
        _close_number(got, want, what, rtol=1e-11, hint=ELBO_HINT)


def test_gmm_elbo_does_not_modify_its_inputs(lat):
    rng = np.random.default_rng(6016)
    w, mu, S = _random_mixture(rng, 3, 2)
    X = _draw(rng, 10, w, mu, S)
    R = rng.dirichlet(np.ones(3), size=10)
    R[2] = [0.0, 1.0, 0.0]
    copies = [v.copy() for v in (X, R, w, mu, S)]
    _result(lambda: lat.gmm_elbo(X, R, w, mu, S), "a float", "float arrays")
    for name, value, copy in zip(("X", "resp", "weights", "means", "covs"), (X, R, w, mu, S), copies):
        assert np.array_equal(value, copy), (
            f"expected {name} unchanged by gmm_elbo, got {name} = {_show(value)} (never modify the arrays you "
            f"receive: replacing the zeros of resp must happen in a new array, np.where makes one)")


RE = [[0.6, 0.4], [0.3, 0.7], [1.0, 0.0]]
ELBO_REFUSALS = [
    (X2, [[0.6, 0.3, 0.1], [0.3, 0.6, 0.1], [1.0, 0.0, 0.0]], W2, M2, C2, "resp has 3 columns for 2 weights"),
    (X2, [[1.0], [1.0], [1.0]], W2, M2, C2, "resp has 1 column for 2 weights"),
    (X2, RE[:2], W2, M2, C2, "resp has 2 rows for 3 points"),
    (X2, [0.6, 0.3, 1.0], W2, M2, C2, "resp is 1-D"),
    (X2, np.ones((3, 2, 1)) / 2, W2, M2, C2, "resp is 3-D"),
    (X2, [[0.6, 0.4], [np.nan, 0.7], [1.0, 0.0]], W2, M2, C2, "resp holds a nan"),
    (X2, [[0.6, 0.4], [0.3, 0.7], [np.inf, 0.0]], W2, M2, C2, "resp holds an inf"),
    (X2, [[1.5, -0.5], [0.3, 0.7], [1.0, 0.0]], W2, M2, C2, "resp holds a negative value (its row sums to 1)"),
    (X2, [[0.6, 0.3], [0.3, 0.7], [1.0, 0.0]], W2, M2, C2, "row 0 of resp sums to 0.9"),
    (X2, [[0.6, 0.4], [0.3, 0.7 + 1e-8], [1.0, 0.0]], W2, M2, C2, "row 1 sums to 1 + 1e-8, beyond 1e-9"),
    ([0.3, -1.2], [[0.6, 0.4]], W2, M2, C2, "X is 1-D"),
    ([[0.3, -1.2], [2.2, np.nan], [-0.9, 1.6]], RE, W2, M2, C2, "X holds a nan"),
    (X2, RE, [0.3, 0.6], M2, C2, "the weights sum to 0.9"),
    (X2, RE, [0.0, 1.0], M2, C2, "a weight is 0"),
    (X2, RE, W2, [[0.0, 0.5, 0.0], [1.5, -0.5, 0.0]], C2, "means of 3 coordinates for points of 2"),
    (X2, RE, W2, M2, [C2[0], [[1.0, 2.5], [2.5, 1.0]]], "a covariance matrix is not positive definite"),
    (X2, RE, W2, M2, [[[1.3, 0.4], [-0.4, 0.9]], C2[1]], "a covariance matrix is not symmetric"),
]
ELBO_IDS = ["resp-three-columns", "resp-one-column", "resp-fewer-rows", "resp-one-d", "resp-three-d", "resp-nan",
            "resp-inf", "resp-negative", "resp-row-sum", "resp-row-sum-beyond-tolerance", "X-one-d", "X-nan",
            "weights-sum", "weights-zero", "means-columns", "covs-indefinite", "covs-not-symmetric"]


@pytest.mark.parametrize("X, resp, weights, means, covs, why", ELBO_REFUSALS, ids=ELBO_IDS)
def test_gmm_elbo_refusals(lat, X, resp, weights, means, covs, why):
    _expect_error(ValueError, lambda: lat.gmm_elbo(X, resp, weights, means, covs),
                  f"gmm_elbo({X!r}, {resp!r}, {weights!r}, {means!r}, {covs!r})", why)


def test_gmm_elbo_accepts_rows_summing_to_one_within_1e_9(lat):
    R = np.array([[0.6, 0.4 + 8e-10], [0.3, 0.7], [1.0 - 5e-10, 0.0]])
    want = _elbo(X2, R, W2, M2, C2)
    got = _result(lambda: lat.gmm_elbo(X2, R, W2, M2, C2), f"{want:.12g}", "rows summing to 1 + 8e-10 and 1 - 5e-10",
                  "each row of resp sums to 1 up to 1e-9")
    _close_number(got, want, "gmm_elbo with rows of resp summing to 1 ± 1e-9", rtol=1e-9, hint=ELBO_HINT)
