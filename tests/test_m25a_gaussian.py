"""Tests of mymath.gaussian (chapter M25a): the log-density of a multivariate normal law, sampling by Cholesky, the
Schur complement of a block, the conditional law of a Gaussian vector, and the posterior of a Bayesian linear
regression.

Oracles: ``scipy.stats.multivariate_normal`` (``logpdf``) and ``scipy.stats.norm`` for the log-density, with
``np.linalg.slogdet`` and ``np.linalg.det`` (the value at the mean, a change of variable) and a Riemann sum of the
density; for the draws, the formula fixed by the docstring, ``mean + E @ L.T`` with
``E = np.random.default_rng(seed).standard_normal((n, d))`` and ``L = np.linalg.cholesky(cov)``, and the empirical
moments of many draws; ``np.linalg.inv`` and ``np.linalg.det`` for the Schur complement (the block of ``M⁻¹`` on the
other indices is its inverse, ``det M = det D · det S``); the precision matrix ``Σ⁻¹`` (``np.linalg.inv``) and the
ratio of densities ``p(x_a, x_b) / p(x_b)`` (``scipy.stats.multivariate_normal``) for the conditional law; and, for the
posterior, the precision form computed with ``np.linalg.inv``, one observation at a time (the covariance form, without
any inverse), the conditional law of the joint Gaussian of the weights and the targets, and the ridge solution by
``np.linalg.lstsq``. Plus properties: symmetric covariance matrices, a covariance that does not depend on the observed
values, inputs left unchanged, Python floats and arrays of floats, dimension 1, and the refusals of the docstrings.
They describe the expected behaviour without showing the solution.

    pytest tests/test_m25a_gaussian.py              # your code
    pytest tests/test_m25a_gaussian.py --impl=ref   # the reference
"""

import ast
import inspect
import math
import warnings

import numpy as np
import pytest
from scipy import stats


@pytest.fixture
def gauss(mymath_module):
    return mymath_module("gaussian")


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


def _check_pair(got, shapes, what):
    """A tuple of two float arrays of the given shapes (mean, covariance)."""
    assert isinstance(got, tuple) and len(got) == 2, (
        f"expected a tuple (mean, covariance) for {what}, got {type(got).__name__}"
        + (f" of length {len(got)}" if isinstance(got, (tuple, list)) else ""))
    _float_array(got[0], shapes[0], f"the mean returned for {what}")
    _float_array(got[1], shapes[1], f"the covariance matrix returned for {what}")
    return got


def _symmetric_by_the_rule(A):
    """The rule of the module: |A[i, j] - A[j, i]| ≤ 1e-12 · max(1, max |A|) for every entry."""
    return bool(np.all(np.abs(A - A.T) <= 1e-12 * max(1.0, float(np.max(np.abs(A))))))


def _spd(rng, d, scale=1.0, floor=0.3):
    """A random symmetric positive definite (d, d) matrix, exactly symmetric, of moderate condition number."""
    B = rng.normal(size=(d, d))
    S = scale * (B @ B.T / d + floor * np.eye(d))
    return (S + S.T) / 2


def _scipy_logpdf(points, mean, cov):
    """ln p of N(mean, cov) for each row of points, by scipy.stats.multivariate_normal (one row at a time)."""
    law = stats.multivariate_normal(mean=mean, cov=cov)
    return np.array([float(law.logpdf(row)) for row in np.atleast_2d(points)])


def _logpdf_parts(x, mean, cov):
    """(d, ln det Σ, Mahalanobis²) by np.linalg.slogdet and np.linalg.solve, for the hints."""
    x, mean, cov = (np.asarray(v, dtype=float) for v in (x, mean, cov))
    sign, logdet = np.linalg.slogdet(cov)
    dev = x - mean
    return mean.size, logdet, float(dev @ np.linalg.solve(cov, dev))


# --- what the module may use ------------------------------------------------------------------------------------

def _imported_names(tree):
    """The local names bound by the absolute imports of the module, mapped to what they stand for: ``np`` (import
    numpy as np) → "numpy", ``inv`` (from numpy.linalg import inv) → "numpy.linalg.inv"."""
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
    ("mvn_logpdf", "numpy.linalg.cholesky"); ``where`` is the top-level function, or "the module level"."""
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


def _multivariate_normal_uses(tree):
    """Every use of the name multivariate_normal in the code, whatever it is called on: np.random.multivariate_normal,
    rng.multivariate_normal, default_rng(seed).multivariate_normal, a name bound to it,
    getattr(…, "multivariate_normal"). An import never used, a comment or a docstring does not count."""
    found = []
    for statement in tree.body:
        where = _where(statement)
        for node in ast.walk(statement):
            if isinstance(node, ast.Attribute) and node.attr == "multivariate_normal":
                found.append(f".multivariate_normal in {where}")
            elif isinstance(node, ast.Name) and node.id == "multivariate_normal":
                found.append(f"multivariate_normal in {where}")
            elif (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "getattr"
                  and any(isinstance(a, ast.Constant) and isinstance(a.value, str) and "multivariate_normal" in a.value
                          for a in node.args)):
                found.append(f"getattr(…, 'multivariate_normal') in {where}")
    return found


ALLOWED_LINALG = ("cholesky", "solve", "LinAlgError")


def test_module_uses_only_cholesky_and_solve_of_np_linalg_and_neither_scipy_nor_multivariate_normal(gauss):
    """The docstring allows, from np.linalg, only cholesky and solve (and np.linalg.LinAlgError, an exception), no
    multivariate_normal in any form (np.random.multivariate_normal, the method of a Generator) and no SciPy at all.
    Only the code counts: a comment, a docstring or an import never used is not a use. Relative imports of your own
    modules (from .eigen import cholesky) are allowed."""
    try:
        tree = ast.parse(inspect.getsource(gauss))
    except (OSError, TypeError, SyntaxError):   # source not readable: nothing to check
        return
    found = []
    for where, path in _uses(tree, _imported_names(tree)):
        parts = path.split(".")
        shown = ".".join(["np"] + parts[1:]) if parts[0] == "numpy" else path
        if parts[0] == "scipy" or "multivariate_normal" in parts:
            found.append(f"{shown} in {where}")
        elif parts[0] == "numpy" and len(parts) > 2 and parts[1] == "linalg" and parts[2] not in ALLOWED_LINALG:
            found.append(f"{shown} in {where}")
    found += _multivariate_normal_uses(tree)
    assert not found, (f"expected NumPy with, from np.linalg, only cholesky and solve, no multivariate_normal and no "
                       f"SciPy at all, found {sorted(set(found))} (the tests compare your results with "
                       f"scipy.stats.multivariate_normal, np.linalg.inv, det and slogdet: write the computation "
                       f"yourself, with a Cholesky factor and np.linalg.solve)")


# --- mvn_logpdf -----------------------------------------------------------------------------------------------------

LOGPDF_HINT = ("ln p(x) = -½ [d ln(2π) + ln det Σ + (x - μ)ᵀ Σ⁻¹ (x - μ)], with ln det Σ = 2 Σ_i ln L[i, i] and the "
               "quadratic form ‖y‖², where y solves L y = x - μ")


def _logpdf_hint(got, x, mean, cov):
    """LOGPDF_HINT, plus the classic error that the value got matches, if any."""
    d, logdet, quad = _logpdf_parts(x, mean, cov)
    want = -0.5 * (d * math.log(2 * math.pi) + logdet + quad)
    dev = np.asarray(x, dtype=float) - np.asarray(mean, dtype=float)
    L = np.linalg.cholesky(np.asarray(cov, dtype=float))
    wrong = [
        (-(d * math.log(2 * math.pi) + logdet + quad), "the factor ½ is missing"),
        (-0.5 * (logdet + quad), "the term d ln(2π) is missing"),
        (-0.5 * (d * math.log(2 * math.pi) + logdet / 2 + quad),
         "ln det Σ = 2 Σ_i ln L[i, i]: the factor 2 is missing (det Σ = (det L)²)"),
        (-0.5 * (d * math.log(2 * math.pi) + 2 * logdet + quad), "ln det Σ counted twice"),
        (-0.5 * (d * math.log(2 * math.pi) + logdet + float(dev @ np.asarray(cov, dtype=float) @ dev)),
         "the quadratic form uses Σ instead of Σ⁻¹"),
        (-0.5 * (d * math.log(2 * math.pi) + logdet + float(np.sum(np.linalg.solve(L.T, dev) ** 2))),
         "y must solve L y = x - μ, not Lᵀ y = x - μ"),
        (-0.5 * (d * math.log(2 * math.pi) + logdet + quad ** 0.5), "the quadratic form is ‖y‖², not ‖y‖"),
        (-0.5 * (d * math.log(2 * math.pi) - logdet + quad), "+ ln det Σ, not - ln det Σ"),
    ]
    for value, text in wrong:
        if not math.isclose(value, want, rel_tol=1e-9) and math.isclose(got, value, rel_tol=1e-9, abs_tol=1e-12):
            return f"{LOGPDF_HINT}; here {text}"
    return LOGPDF_HINT


def test_mvn_logpdf_docstring_examples(gauss):
    call = "mvn_logpdf([1, -1], [1, -1], [[2, 3], [3, 9]])"
    got = _result(lambda: gauss.mvn_logpdf([1, -1], [1, -1], [[2, 3], [3, 9]]), "-2.936489 (rounded)", call)
    _float(got, call)
    assert round(got, 6) == -2.936489, (f"expected round({call}, 6) = -2.936489, -ln(2π) - ½ ln 9 at the mean, got "
                                        f"{got!r} ({_logpdf_hint(got, [1, -1], [1, -1], [[2, 3], [3, 9]])})")
    call = "mvn_logpdf([[1, -1], [1, 2]], [1, -1], [[2, 3], [3, 9]])"
    got = _result(lambda: gauss.mvn_logpdf([[1, -1], [1, 2]], [1, -1], [[2, 3], [3, 9]]),
                  "array([-2.936489, -3.936489]) (rounded)", call)
    _float_array(got, (2,), f"{call} (one value per row)")
    assert np.array_equal(np.round(got, 6), [-2.936489, -3.936489]), (
        f"expected np.round({call}, 6) = [-2.936489, -3.936489], got {_show(got)} ({LOGPDF_HINT})")


@pytest.mark.parametrize("d", [1, 2, 3, 5, 8], ids=lambda d: f"d{d}")
def test_mvn_logpdf_matches_scipy_for_one_point(gauss, d):
    rng = np.random.default_rng(5810 + d)
    cov = _spd(rng, d, scale=1.7)
    mean = rng.normal(size=d) * 3.0
    for trial in range(4):
        x = mean + rng.normal(size=d) * (0.5 + trial)
        want = float(_scipy_logpdf(x, mean, cov)[0])
        what = f"mvn_logpdf(x, mean, cov) for a random point in dimension {d} (point {trial + 1})"
        got = _result(lambda: gauss.mvn_logpdf(x, mean, cov), f"{want:.12g}", what)
        _float(got, what)
        _close_number(got, want, f"{what}, scipy.stats.multivariate_normal(mean, cov).logpdf(x)", rtol=1e-10,
                      hint=_logpdf_hint(got, x, mean, cov))


ROWS = [(1, 7, "dimension 1: n points form a column (n, 1)"), (2, 50, "50 points in dimension 2"),
        (4, 30, "30 points in dimension 4"), (6, 1, "a single row (1, 6): still an array of one value"),
        (3, 2, "2 points in dimension 3")]


@pytest.mark.parametrize("d, n, text", ROWS, ids=[f"d{d}-n{n}" for d, n, _ in ROWS])
def test_mvn_logpdf_matches_scipy_row_by_row(gauss, d, n, text):
    rng = np.random.default_rng(5816 + ROWS.index((d, n, text)))
    cov = _spd(rng, d, scale=0.8)
    mean = rng.normal(size=d)
    X = mean + rng.normal(size=(n, d)) * 1.5
    want = _scipy_logpdf(X, mean, cov)
    what = f"mvn_logpdf(X, mean, cov) for {text}"
    got = _result(lambda: gauss.mvn_logpdf(X, mean, cov), f"an array of {n} floats", what)
    _float_array(got, (n,), f"{what} (one value per row of X)")
    _close(got, want, f"{what}, scipy.stats.multivariate_normal(mean, cov).logpdf of each row", rtol=1e-10,
           hint=_logpdf_hint(float(got[0]), X[0], mean, cov) + "; rows hold the points: X - mean subtracts the mean "
                                                                "from each row")


def test_mvn_logpdf_in_dimension_1_is_the_normal_law(gauss):
    """N(μ, σ²) with σ² = cov[0][0], a variance: scipy.stats.norm takes the standard deviation σ = √cov."""
    mu, var = 1.25, 0.64
    for x in (1.25, -0.35, 3.05):
        want = float(stats.norm.logpdf(x, loc=mu, scale=math.sqrt(var)))
        what = f"mvn_logpdf([{x}], [{mu}], [[{var}]])"
        got = _result(lambda: gauss.mvn_logpdf([x], [mu], [[var]]), f"{want:.12g}", what)
        _float(got, what)
        _close_number(got, want, f"{what}, ln of the density of N({mu}, {var}) (scipy.stats.norm with scale = √{var})",
                      hint="cov is the variance σ² (here σ = 0.8): ln p = -½ [ln(2π) + ln σ² + (x - μ)² / σ²]")
    X = np.array([[1.25], [-0.35], [3.05], [0.6]])
    got = _result(lambda: gauss.mvn_logpdf(X, [mu], [[var]]), "4 values", "a column (4, 1) of points in dimension 1")
    _float_array(got, (4,), "mvn_logpdf of a column (4, 1) in dimension 1 (one value per row)")
    _close(got, stats.norm.logpdf(X[:, 0], loc=mu, scale=math.sqrt(var)),
           "mvn_logpdf of the column (4, 1), the normal log-densities of N(1.25, 0.64)", rtol=1e-10)


def test_mvn_logpdf_at_the_mean_and_on_a_level_ellipsoid(gauss):
    """At the mean: -½ [d ln(2π) + ln det Σ] (np.linalg.slogdet); at μ + c Σ^(1/2) u with ‖u‖ = 1 (a square root by
    np.linalg.eigh), the Mahalanobis distance is c: the log-density drops by c²/2."""
    rng = np.random.default_rng(5821)
    for d in (2, 3, 6):
        cov = _spd(rng, d, scale=2.3)
        mean = rng.normal(size=d) * 2.0
        sign, logdet = np.linalg.slogdet(cov)
        at_mean = -0.5 * (d * math.log(2 * math.pi) + logdet)
        what = f"mvn_logpdf(mean, mean, cov) in dimension {d}"
        got = _result(lambda: gauss.mvn_logpdf(mean, mean, cov), f"{at_mean:.12g}", what)
        _float(got, what)
        _close_number(got, at_mean, f"{what}, -½ [d ln(2π) + ln det Σ] (np.linalg.slogdet)", rtol=1e-11,
                      hint=_logpdf_hint(got, mean, mean, cov))
        values, vectors = np.linalg.eigh(cov)
        root = vectors @ np.diag(np.sqrt(values)) @ vectors.T
        for c in (0.5, 1.75, 3.0):
            u = rng.normal(size=d)
            x = mean + c * root @ (u / np.linalg.norm(u))
            what = f"mvn_logpdf at a point of Mahalanobis distance {c} from the mean, dimension {d}"
            got = _result(lambda: gauss.mvn_logpdf(x, mean, cov), f"{at_mean - c * c / 2:.12g}", what)
            _close_number(got, at_mean - c * c / 2, f"{what}, the value at the mean minus c²/2", rtol=1e-10,
                          hint=_logpdf_hint(got, x, mean, cov))


def test_mvn_logpdf_follows_an_affine_change_of_variable(gauss):
    """If X ~ N(μ, Σ) and A is invertible, A X + b ~ N(A μ + b, A Σ Aᵀ), and its log-density at A x + b is
    ln p_X(x) - ln |det A| (np.linalg.det)."""
    rng = np.random.default_rng(5822)
    for d in (2, 4):
        cov = _spd(rng, d)
        mean = rng.normal(size=d)
        A = rng.normal(size=(d, d)) + 1.5 * np.eye(d)
        b = rng.normal(size=d)
        new_cov = A @ cov @ A.T
        new_cov = (new_cov + new_cov.T) / 2
        X = mean + rng.normal(size=(5, d))
        before = _result(lambda: gauss.mvn_logpdf(X, mean, cov), "5 values", f"X in dimension {d}")
        after = _result(lambda: gauss.mvn_logpdf(X @ A.T + b, A @ mean + b, new_cov), "5 values",
                        f"A X + b in dimension {d}")
        _float_array(after, (5,), f"mvn_logpdf of 5 rows in dimension {d}")
        _close(after, np.asarray(before) - math.log(abs(np.linalg.det(A))),
               f"mvn_logpdf(A x + b, A μ + b, A Σ Aᵀ), equal to mvn_logpdf(x, μ, Σ) - ln |det A| in dimension {d}",
               rtol=1e-9, atol=1e-10, hint=LOGPDF_HINT)


def test_mvn_logpdf_density_integrates_to_one(gauss):
    """exp(mvn_logpdf) summed on a fine grid times the area of a cell (a Riemann sum) gives 1, in dimension 1 and 2:
    the normalizing constant (2π)^(-d/2) (det Σ)^(-1/2) is right."""
    mean, var = np.array([-0.4]), 1.69
    t = np.linspace(-0.4 - 13.0, -0.4 + 13.0, 2001)
    got = _result(lambda: gauss.mvn_logpdf(t[:, None], mean, [[var]]), "2001 values", "a grid in dimension 1")
    total = float(np.sum(np.exp(got)) * (t[1] - t[0]))
    _close_number(total, 1.0, "the Riemann sum of exp(mvn_logpdf) for N(-0.4, 1.69) in dimension 1", rtol=0,
                  atol=1e-8, hint=LOGPDF_HINT)
    rng = np.random.default_rng(5823)
    cov = _spd(rng, 2, scale=1.4)
    mean = rng.normal(size=2)
    sd = np.sqrt(np.diag(cov))
    u = np.linspace(mean[0] - 9 * sd[0], mean[0] + 9 * sd[0], 361)
    v = np.linspace(mean[1] - 9 * sd[1], mean[1] + 9 * sd[1], 361)
    U, V = np.meshgrid(u, v, indexing="ij")
    grid = np.column_stack([U.ravel(), V.ravel()])
    got = _result(lambda: gauss.mvn_logpdf(grid, mean, cov), f"{grid.shape[0]} values", "a grid in dimension 2")
    _float_array(got, (grid.shape[0],), "mvn_logpdf of a grid of 361 × 361 points")
    total = float(np.sum(np.exp(got)) * (u[1] - u[0]) * (v[1] - v[0]))
    _close_number(total, 1.0, "the Riemann sum of exp(mvn_logpdf) on a grid in dimension 2 (the total mass)", rtol=0,
                  atol=1e-7, hint=LOGPDF_HINT)


def test_mvn_logpdf_in_high_dimension_stays_finite(gauss):
    """In dimension 150, far from the mean, the density underflows to 0 but its logarithm is an ordinary number."""
    rng = np.random.default_rng(5824)
    d = 150
    cov = _spd(rng, d, scale=0.9)
    mean = rng.normal(size=d)
    x = mean + 4.0 * np.linalg.cholesky(cov) @ np.ones(d)          # Mahalanobis distance 4 √150
    want = float(_scipy_logpdf(x, mean, cov)[0])
    assert np.exp(want) == 0.0                                       # the oracle: the density itself underflows
    what = "mvn_logpdf(x, mean, cov) in dimension 150, far from the mean"
    got = _result(lambda: gauss.mvn_logpdf(x, mean, cov), f"{want:.12g}", what,
                  hint="never compute the density nor det Σ itself: ln det Σ = 2 Σ_i ln L[i, i]")
    _float(got, what)
    _close_number(got, want, f"{what} (scipy.stats.multivariate_normal), finite although exp of it is 0.0",
                  rtol=1e-9, hint=LOGPDF_HINT)


def test_mvn_logpdf_takes_lists_of_integers_and_returns_python_floats(gauss):
    mean, cov = [2, -1, 3], [[4, 1, -1], [1, 3, 0], [-1, 0, 5]]
    points = [[2, -1, 3], [3, 1, -2], [0, 0, 1]]
    want = _scipy_logpdf(np.array(points, dtype=float), np.array(mean, dtype=float), np.array(cov, dtype=float))
    for given, text in ((lambda v: v, "lists of integers"), (np.array, "integer arrays")):
        what = f"mvn_logpdf of one point, with {text}"
        got = _result(lambda: gauss.mvn_logpdf(given(points[1]), given(mean), given(cov)), f"{want[1]:.12g}", what)
        _float(got, what)
        _close_number(got, float(want[1]), what, rtol=1e-10, hint=LOGPDF_HINT)
        what = f"mvn_logpdf of 3 points, with {text}"
        got = _result(lambda: gauss.mvn_logpdf(given(points), given(mean), given(cov)), "3 floats", what)
        _float_array(got, (3,), what)
        _close(got, want, what, rtol=1e-10, hint=LOGPDF_HINT)


def test_mvn_logpdf_does_not_modify_its_inputs(gauss):
    rng = np.random.default_rng(5825)
    cov, mean = _spd(rng, 3), rng.normal(size=3)
    X, x = rng.normal(size=(6, 3)), rng.normal(size=3)
    copies = [v.copy() for v in (X, x, mean, cov)]
    _result(lambda: gauss.mvn_logpdf(X, mean, cov), "6 values", "float arrays")
    _result(lambda: gauss.mvn_logpdf(x, mean, cov), "a float", "float arrays")
    for name, value, copy in zip(("X", "x", "mean", "cov"), (X, x, mean, cov), copies):
        assert np.array_equal(value, copy), (
            f"expected {name} unchanged by mvn_logpdf, got {name} = {_show(value)} (never modify the arrays you "
            f"receive: x - mean makes a new array, x -= mean writes into x)")


def test_mvn_logpdf_accepts_a_rounding_asymmetry(gauss):
    """The symmetry test is relative: |Σ[i, j] - Σ[j, i]| ≤ 1e-12 · max(1, max |Σ|)."""
    cov = np.array([[3.2, -0.9, 0.4], [-0.9, 2.6, 0.7], [0.4, 0.7, 1.9]])
    mean, x = np.array([0.3, -1.1, 2.0]), np.array([1.0, 0.2, 1.5])
    want = float(_scipy_logpdf(x, mean, cov)[0])
    tilted = cov.copy()
    tilted[0, 2] += 2e-12                            # below 1e-12 · max(1, 3.2) = 3.2e-12
    got = _result(lambda: gauss.mvn_logpdf(x, mean, tilted), f"{want:.12g}", "an asymmetry of 2e-12",
                  "the symmetry test is relative: |Σ[i, j] - Σ[j, i]| ≤ 1e-12 · max(1, max |Σ|)")
    _close_number(got, want, "mvn_logpdf with an asymmetry of 2e-12 in cov", rtol=1e-9)
    big = 1e6 * cov
    big[2, 1] += 3e-7                                # below 1e-12 · 3.2e6 = 3.2e-6
    _result(lambda: gauss.mvn_logpdf(1e3 * x, 1e3 * mean, big), "a float",
            "entries of order 1e6 and an asymmetry of 3e-7",
            "the symmetry test is relative to the size of the entries: 1e-12 · max(1, max |Σ|)")


MEAN2, COV2 = [0.25, -1.5], [[2.8, 0.75], [0.75, 1.5]]
LOGPDF_REFUSALS = [
    ([0.25, -1.5], [[0.25, -1.5]], COV2, "mean is 2-D"),
    ([0.25, -1.5], [], [[2.8]], "mean is empty"),
    (0.25, 0.25, [[2.8]], "mean is a number, not 1-D"),
    ([0.25, -1.5], MEAN2, [[2.8, 0.75, 0.0], [0.75, 1.5, 0.0], [0.0, 0.0, 1.0]], "cov is 3 × 3 for d = 2"),
    ([0.25, -1.5], MEAN2, [2.8, 1.5], "cov is 1-D"),
    ([0.25, -1.5], MEAN2, [[2.8, 0.75], [-0.75, 1.5]], "cov is not symmetric (its lower triangle alone has a Cholesky "
                                                      "factor)"),
    ([0.25, -1.5], MEAN2, [[2.8, 0.75 + 1e-9], [0.75, 1.5]], "an asymmetry of 1e-9, above 1e-12 · max(1, max |Σ|)"),
    ([0.25, -1.5], MEAN2, [[1.2, 2.8], [2.8, 1.2]], "cov is not positive definite (eigenvalues 4 and -1.6)"),
    ([0.25, -1.5], MEAN2, [[25.0, 10.0], [10.0, 4.0]], "cov is only semi-definite (rank 1: a pivot is exactly 0)"),
    ([0.25, -1.5], MEAN2, [[-2.8, 0.0], [0.0, 1.5]], "cov has a negative variance"),
    ([0.25, -1.5, 0.0], MEAN2, COV2, "x has 3 coordinates for d = 2"),
    ([[0.25, -1.5, 0.0], [1.0, 1.0, 1.0]], MEAN2, COV2, "x has 3 columns for d = 2"),
    (np.zeros((2, 3, 2)), MEAN2, COV2, "x is 3-D"),
    (0.4, [1.25], [[0.64]], "x is a number, even in dimension 1: write [0.4]"),
    ([0.4, 1.1, -0.2, 2.0], [1.25], [[0.64]], "a 1-D x of length 4 in dimension 1: 4 points form a column (4, 1)"),
]


@pytest.mark.parametrize("x, mean, cov, why", LOGPDF_REFUSALS,
                         ids=["mean-two-d", "mean-empty", "mean-scalar", "cov-shape", "cov-one-d", "cov-not-symmetric",
                              "cov-asymmetry-1e-9", "cov-indefinite", "cov-semi-definite", "cov-negative-variance",
                              "x-length", "x-columns", "x-three-d", "x-scalar", "x-one-d-in-dimension-1"])
def test_mvn_logpdf_refusals(gauss, x, mean, cov, why):
    _expect_error(ValueError, lambda: gauss.mvn_logpdf(x, mean, cov), f"mvn_logpdf({x!r}, {mean!r}, {cov!r})", why)


# --- sample_mvn -----------------------------------------------------------------------------------------------------

SAMPLE_HINT = ("E = np.random.default_rng(seed).standard_normal((n, d)) in ONE call, L = the Cholesky factor of cov "
               "(lower triangular, Σ = L Lᵀ), then mean + E @ L.T: row i is μ + L ε_i")


def _draws(mean, cov, n, seed):
    """The draws fixed by the docstring: mean + E @ L.T."""
    mean, cov = np.asarray(mean, dtype=float), np.asarray(cov, dtype=float)
    E = np.random.default_rng(seed).standard_normal((n, mean.size))
    return mean + E @ np.linalg.cholesky(cov).T


def _sample_hint(got, mean, cov, n, seed):
    """SAMPLE_HINT, plus the classic error that the draws got match, if any."""
    mean, cov = np.asarray(mean, dtype=float), np.asarray(cov, dtype=float)
    d = mean.size
    if not (isinstance(got, np.ndarray) and got.shape == (n, d)):
        return SAMPLE_HINT
    L = np.linalg.cholesky(cov)
    E = np.random.default_rng(seed).standard_normal((n, d))
    values, vectors = np.linalg.eigh(cov)
    candidates = [
        (mean + E @ L, "E @ L: row i would be μ + Lᵀ ε_i, of covariance LᵀL ≠ Σ; write E @ L.T"),
        (mean + E @ (vectors @ np.diag(np.sqrt(values)) @ vectors.T), "another square root of Σ (eigh) gives other "
                                                                      "draws: L is the Cholesky factor"),
        (mean + E @ cov, "E @ cov: multiply by Lᵀ, the transpose of the Cholesky factor, not by Σ"),
        (mean + E * np.sqrt(np.diag(cov)), "only the variances were used: the correlations come from L"),
        (mean + np.random.default_rng(seed).standard_normal((d, n)).T @ L.T,
         "standard_normal((n, d)), not standard_normal((d, n)).T: the draws are fixed by one call of shape (n, d)"),
        (mean + np.random.default_rng(0).standard_normal((n, d)) @ L.T, "the seed was not used: "
                                                                        "rng = np.random.default_rng(seed)"),
    ]
    want = mean + E @ L.T
    for value, text in candidates:
        if not np.allclose(value, want) and np.allclose(got, value, rtol=1e-10, atol=1e-10):
            return f"{SAMPLE_HINT}; here {text}"
    return SAMPLE_HINT


def test_sample_mvn_docstring_example(gauss):
    X = _result(lambda: gauss.sample_mvn([1, -1], [[2, 3], [3, 9]], 200_000, seed=2), "an array of shape (200000, 2)",
                "the example of the docstring")
    _float_array(X, (200_000, 2), "sample_mvn([1, -1], [[2, 3], [3, 9]], 200_000, seed=2)")
    assert np.array_equal(np.round(X.mean(axis=0), 1), [1.0, -1.0]), (
        f"expected the means of the docstring example rounded to [1., -1.], got {_show(X.mean(axis=0))} "
        f"({_sample_hint(X, [1, -1], [[2, 3], [3, 9]], 200_000, 2)})")
    C = np.round(np.cov(X.T, bias=True), 1)
    assert np.array_equal(C, [[2.0, 3.0], [3.0, 9.0]]), (
        f"expected the covariance of the docstring example rounded to [[2, 3], [3, 9]], got {_show(C)} "
        f"({_sample_hint(X, [1, -1], [[2, 3], [3, 9]], 200_000, 2)})")


DRAWS = [(1, 9, 5830, "dimension 1"), (2, 5, 5831, "dimension 2"), (3, 40, 5832, "dimension 3"),
         (6, 25, 5833, "dimension 6"), (4, 1, 5834, "a single draw"), (5, 300, 5835, "300 draws in dimension 5")]


@pytest.mark.parametrize("d, n, seed, text", DRAWS, ids=[f"d{d}-n{n}" for d, n, _, _ in DRAWS])
def test_sample_mvn_matches_mean_plus_E_times_L_transposed_with_the_same_seed(gauss, d, n, seed, text):
    rng = np.random.default_rng(seed + 20)
    cov = _spd(rng, d, scale=2.0)
    mean = rng.normal(size=d) * 4.0
    want = _draws(mean, cov, n, seed)
    what = f"sample_mvn(mean, cov, {n}, seed={seed}) for {text}"
    got = _result(lambda: gauss.sample_mvn(mean, cov, n, seed=seed), f"an array of shape {want.shape}", what)
    _float_array(got, (n, d), f"{what} (one draw per row)")
    _close(got, want, f"{what}, mean + E @ L.T", rtol=1e-12, atol=1e-12,
           hint=_sample_hint(got, mean, cov, n, seed))


def test_sample_mvn_same_seed_same_draws_other_seed_other_draws(gauss):
    rng = np.random.default_rng(5840)
    cov, mean = _spd(rng, 3), rng.normal(size=3)
    first = _result(lambda: gauss.sample_mvn(mean, cov, 8, seed=5841), "8 draws", "seed=5841")
    again = _result(lambda: gauss.sample_mvn(mean, cov, 8, seed=5841), "8 draws", "seed=5841 again")
    _float_array(first, (8, 3), "sample_mvn(mean, cov, 8, seed=5841)")
    assert np.array_equal(first, again), "expected the same draws for the same seed (5841, twice)"
    other = _result(lambda: gauss.sample_mvn(mean, cov, 8, seed=5842), "8 draws", "seed=5842")
    assert not np.allclose(first, other), (
        "expected other draws for another seed (5841, then 5842), got the same (rng = np.random.default_rng(seed))")
    default = _result(lambda: gauss.sample_mvn(mean, cov, 8), "8 draws", "no seed")
    _close(default, _draws(mean, cov, 8, 0), "sample_mvn(mean, cov, 8) without seed, the draws of seed=0 (the default)",
           rtol=1e-12, atol=1e-12, hint=SAMPLE_HINT)
    _close(first, _draws(mean, cov, 8, 5841), "sample_mvn(mean, cov, 8, seed=5841)", rtol=1e-12, atol=1e-12,
           hint=_sample_hint(first, mean, cov, 8, 5841))


def test_sample_mvn_moments_match_the_law(gauss):
    """150 000 draws: each empirical mean within 5 standard errors of μ_j (√(Σ_jj / n)), each empirical covariance
    within 5 standard errors of Σ_jk (√((Σ_jj Σ_kk + Σ_jk²) / n))."""
    mean = np.array([4.0, -2.5, 0.75])
    cov = np.array([[2.4, 1.6, -0.9], [1.6, 3.5, 0.4], [-0.9, 0.4, 1.2]])
    n = 150_000
    L = np.linalg.cholesky(cov)
    tol_cov = 5 * np.sqrt((np.outer(np.diag(cov), np.diag(cov)) + cov ** 2) / n)
    assert np.any(np.abs(L.T @ L - cov) > 10 * tol_cov)             # the oracle: E @ L would be seen
    X = _result(lambda: gauss.sample_mvn(mean, cov, n, seed=5843), f"an array of shape ({n}, 3)",
                f"{n} draws in dimension 3")
    _float_array(X, (n, 3), f"sample_mvn(mean, cov, {n}, seed=5843)")
    m = X.mean(axis=0)
    tol_mean = 5 * np.sqrt(np.diag(cov) / n)
    assert np.all(np.abs(m - mean) <= tol_mean), (
        f"expected the empirical means within {_show(tol_mean)} of μ = {_show(mean)}, got {_show(m)} ({SAMPLE_HINT})")
    S = (X - m).T @ (X - m) / n
    assert np.all(np.abs(S - cov) <= tol_cov), (
        f"expected the empirical covariance within 5 standard errors of Σ = {_show(cov)}, got {_show(S)}"
        + (" (it is close to LᵀL: write E @ L.T, not E @ L)" if np.all(np.abs(S - L.T @ L) <= tol_cov) else "")
        + f" ({SAMPLE_HINT})")


def test_sample_mvn_in_dimension_1_uses_the_standard_deviation(gauss):
    """In dimension 1, L = [[√σ²]]: the draws are μ + σ ε, of shape (n, 1)."""
    got = _result(lambda: gauss.sample_mvn([-3.5], [[6.25]], 12, seed=5844), "an array of shape (12, 1)",
                  "sample_mvn([-3.5], [[6.25]], 12, seed=5844)")
    _float_array(got, (12, 1), "sample_mvn([-3.5], [[6.25]], 12, seed=5844) (a column: one draw per row)")
    E = np.random.default_rng(5844).standard_normal((12, 1))
    _close(got, -3.5 + 2.5 * E, "the draws -3.5 + 2.5 ε of N(-3.5, 6.25)", rtol=1e-12, atol=1e-12,
           hint="cov is the variance σ² = 6.25: its Cholesky factor is σ = 2.5")


def test_sample_mvn_accepts_numpy_integers_and_lists_of_integers(gauss):
    mean, cov = [3, 0, -2], [[6, 2, 0], [2, 3, -1], [0, -1, 4]]
    want = _draws(mean, cov, 6, 5845)
    for n, seed, text in ((6, 5845, "Python integers"), (np.int64(6), np.int64(5845), "NumPy integers n and seed"),
                          (np.int32(6), np.uint16(5845), "np.int32 and np.uint16")):
        got = _result(lambda: gauss.sample_mvn(mean, cov, n, seed=seed), "an array of shape (6, 3)", text,
                      "a NumPy integer is accepted for n and seed")
        _float_array(got, (6, 3), f"sample_mvn with lists of integers and {text}")
        _close(got, want, f"sample_mvn with lists of integers and {text}", rtol=1e-12, atol=1e-12, hint=SAMPLE_HINT)


def test_sample_mvn_does_not_modify_its_inputs(gauss):
    rng = np.random.default_rng(5846)
    cov, mean = _spd(rng, 4), rng.normal(size=4)
    copies = [mean.copy(), cov.copy()]
    got = _result(lambda: gauss.sample_mvn(mean, cov, 1, seed=5847), "an array of shape (1, 4)", "float arrays")
    _float_array(got, (1, 4), "sample_mvn(mean, cov, 1, seed=5847)")
    for name, value, copy in zip(("mean", "cov"), (mean, cov), copies):
        assert np.array_equal(value, copy), (
            f"expected {name} unchanged by sample_mvn, got {name} = {_show(value)} (never modify the arrays you "
            f"receive)")
    got[:] = 99.0
    assert np.array_equal(mean, copies[0]), "expected sample_mvn to return a new array, but changing it changed mean"


SAMPLE_REFUSALS = [
    (MEAN2, COV2, 0, 5848, "n = 0: at least one draw"),
    (MEAN2, COV2, -4, 5848, "n = -4"),
    (MEAN2, COV2, 6.0, 5848, "n = 6.0 is a float"),
    (MEAN2, COV2, True, 5848, "n = True is a bool"),
    (MEAN2, COV2, None, 5848, "n = None"),
    (MEAN2, COV2, 6, -1, "seed = -1"),
    (MEAN2, COV2, 6, 58.5, "seed = 58.5 is a float"),
    (MEAN2, COV2, 6, 5848.0, "seed = 5848.0 is a float, even a whole one"),
    (MEAN2, COV2, 6, True, "seed = True is a bool"),
    (MEAN2, COV2, 6, None, "seed = None: the draws must be fixed by an integer seed"),
    ([[0.25, -1.5]], COV2, 6, 5848, "mean is 2-D"),
    ([], [[2.8]], 6, 5848, "mean is empty"),
    (MEAN2, [[2.8, 0.75]], 6, 5848, "cov is 1 × 2 for d = 2"),
    (MEAN2, [[2.8, 0.75], [-0.75, 1.5]], 6, 5848, "cov is not symmetric"),
    (MEAN2, [[1.2, 2.8], [2.8, 1.2]], 6, 5848, "cov is not positive definite"),
    (MEAN2, [[25.0, 10.0], [10.0, 4.0]], 6, 5848, "cov is only semi-definite"),
]


@pytest.mark.parametrize("mean, cov, n, seed, why", SAMPLE_REFUSALS,
                         ids=["n-zero", "n-negative", "n-float", "n-bool", "n-none", "seed-negative", "seed-float",
                              "seed-whole-float", "seed-bool", "seed-none", "mean-two-d", "mean-empty", "cov-shape",
                              "cov-not-symmetric", "cov-indefinite", "cov-semi-definite"])
def test_sample_mvn_refusals(gauss, mean, cov, n, seed, why):
    _expect_error(ValueError, lambda: gauss.sample_mvn(mean, cov, n, seed=seed),
                  f"sample_mvn({mean!r}, {cov!r}, {n!r}, seed={seed!r})", why)


# --- schur_complement -----------------------------------------------------------------------------------------------

SCHUR_HINT = ("D = M[idx, idx] (the block eliminated), A = M[rest, rest] with rest the OTHER indices in increasing "
              "order, B = M[rest, idx], C = M[idx, rest]; the result is A - B D⁻¹ C, with "
              "D⁻¹ C = np.linalg.solve(D, C)")


def _rest(m, idx):
    return [i for i in range(m) if i not in idx]


def _schur_by_inverse(M, idx):
    """The oracle: the inverse of the block of M⁻¹ on the other indices (np.linalg.inv)."""
    rest = _rest(M.shape[0], idx)
    return np.linalg.inv(np.linalg.inv(M)[np.ix_(rest, rest)])


def _invertible(rng, m, symmetric):
    """A random invertible (m, m) matrix whose blocks are invertible: symmetric positive definite, or not symmetric."""
    if symmetric:
        return _spd(rng, m, scale=1.5)
    return rng.normal(size=(m, m)) + 2.5 * np.eye(m)


def test_schur_complement_docstring_examples(gauss):
    M = [[5, 2, 2], [2, 4, 0], [2, 0, 4]]
    for idx, want in (([2], [[4.0, 2.0], [2.0, 4.0]]), ([1, 2], [[3.0]])):
        call = f"schur_complement([[5, 2, 2], [2, 4, 0], [2, 0, 4]], {idx})"
        got = _result(lambda: gauss.schur_complement(M, idx), _show(want), call)
        _float_array(got, np.shape(want), call)
        _close(got, want, call, rtol=1e-12, atol=1e-12, hint=SCHUR_HINT)


SCHUR_CASES = [(2, [0], True), (2, [1], False), (3, [2], True), (3, [0], False), (4, [0, 2], True), (4, [3, 1], False),
               (5, [4, 1], True), (6, [1, 2, 3, 5], False), (5, [0, 1, 2, 3], True), (7, [6, 0, 3], False)]


@pytest.mark.parametrize("m, idx, symmetric", SCHUR_CASES,
                         ids=[f"m{m}-idx{'-'.join(map(str, idx))}-{'sym' if s else 'nonsym'}"
                              for m, idx, s in SCHUR_CASES])
def test_schur_complement_is_the_inverse_of_the_block_of_the_inverse(gauss, m, idx, symmetric):
    """The block of M⁻¹ on the other indices is S⁻¹ (np.linalg.inv), and det M = det D · det S (np.linalg.det)."""
    rng = np.random.default_rng(5850 + SCHUR_CASES.index((m, idx, symmetric)))
    M = _invertible(rng, m, symmetric)
    want = _schur_by_inverse(M, idx)
    k = len(idx)
    kind = "symmetric positive definite" if symmetric else "non-symmetric"
    what = f"schur_complement(M, {idx}) for a random {kind} {m} × {m} matrix"
    got = _result(lambda: gauss.schur_complement(M, idx), f"an array of shape {want.shape}", what)
    _float_array(got, (m - k, m - k), f"{what} (the size of the indices left, m - k = {m - k})")
    _close(got, want, f"{what}, the inverse of the block of M⁻¹ on the indices {_rest(m, idx)}", rtol=1e-9,
           atol=1e-11, hint=SCHUR_HINT)
    D = M[np.ix_(idx, idx)]
    _close_number(float(np.linalg.det(D) * np.linalg.det(got)), float(np.linalg.det(M)),
                  f"det D · det S for {what}, equal to det M", rtol=1e-9, hint=SCHUR_HINT)


def test_schur_complement_of_a_non_symmetric_matrix_uses_B_and_C(gauss):
    """For a non-symmetric M, B = M[rest, idx] and C = M[idx, rest] differ: A - B D⁻¹ C, never A - B D⁻¹ Bᵀ nor its
    transpose."""
    M = np.array([[4.5, 1.5], [-0.5, 2.0]])
    for idx, want in (([1], [[4.5 - 1.5 * (-0.5) / 2.0]]), ([0], [[2.0 - (-0.5) * 1.5 / 4.5]])):
        call = f"schur_complement([[4.5, 1.5], [-0.5, 2.0]], {idx})"
        got = _result(lambda: gauss.schur_complement(M, idx), _show(want), call)
        _float_array(got, (1, 1), call)
        _close(got, want, f"{call}, a - b c / d (or d - c b / a)", rtol=1e-12, hint=SCHUR_HINT)
    rng = np.random.default_rng(5861)
    M = rng.normal(size=(5, 5)) + 3.0 * np.eye(5)
    idx, rest = [3, 1], [0, 2, 4]
    want = _schur_by_inverse(M, idx)
    B, C, D = M[np.ix_(rest, idx)], M[np.ix_(idx, rest)], M[np.ix_(idx, idx)]
    assert not np.allclose(want, M[np.ix_(rest, rest)] - B @ np.linalg.solve(D, B.T))   # the oracle: Bᵀ ≠ C here
    got = _result(lambda: gauss.schur_complement(M, idx), "a 3 × 3 matrix", "a non-symmetric 5 × 5 matrix")
    _float_array(got, (3, 3), "schur_complement(M, [3, 1]) for a non-symmetric 5 × 5 matrix")
    hint = SCHUR_HINT
    if np.allclose(got, want.T, rtol=1e-9):
        hint += " (your result is the transpose: B is M[rest, idx], on the left)"
    elif np.allclose(got, M[np.ix_(rest, rest)] - C.T @ np.linalg.solve(D, B.T), rtol=1e-9):
        hint += " (B and C were swapped)"
    _close(got, want, "schur_complement(M, [3, 1]) for a non-symmetric 5 × 5 matrix", rtol=1e-9, atol=1e-11, hint=hint)


def test_schur_complement_order_of_idx_does_not_change_the_result(gauss):
    rng = np.random.default_rng(5862)
    M = _invertible(rng, 6, symmetric=False)
    want = _schur_by_inverse(M, [0, 2, 5])
    for idx in ([0, 2, 5], [5, 0, 2], (2, 5, 0)):
        got = _result(lambda: gauss.schur_complement(M, idx), "a 3 × 3 matrix", f"idx = {idx!r}")
        _float_array(got, (3, 3), f"schur_complement(M, {idx!r})")
        _close(got, want, f"schur_complement(M, {idx!r}) for a non-symmetric 6 × 6 matrix, the same for any order of "
                          f"the indices 0, 2, 5 (rest = [1, 3, 4] in increasing order)", rtol=1e-9, atol=1e-11,
               hint=SCHUR_HINT)


def test_schur_complement_special_cases(gauss):
    """A block-diagonal M (B = C = 0) gives A itself; a symmetric M gives a symmetric result (by the rule of the
    module); the identity gives the identity."""
    A = np.array([[2.5, -0.4, 1.1], [0.3, 3.0, 0.0], [-0.7, 0.2, 1.8]])
    D = np.array([[1.6, 0.5], [-0.2, 0.9]])
    M = np.zeros((5, 5))
    M[np.ix_([0, 2, 4], [0, 2, 4])] = A
    M[np.ix_([1, 3], [1, 3])] = D
    got = _result(lambda: gauss.schur_complement(M, [3, 1]), "the block A", "a block-diagonal matrix")
    _close(got, A, "schur_complement(M, [3, 1]) for a block-diagonal M: B = C = 0 leaves "
                   "A = M[[0, 2, 4]][:, [0, 2, 4]]", rtol=1e-12, atol=1e-15, hint=SCHUR_HINT)
    got = _result(lambda: gauss.schur_complement(np.eye(4), [1]), "the identity", "the identity")
    _close(got, np.eye(3), "schur_complement(np.eye(4), [1])", rtol=0, atol=1e-15, hint=SCHUR_HINT)
    rng = np.random.default_rng(5863)
    S = _spd(rng, 6)
    got = _result(lambda: gauss.schur_complement(S, [4, 0]), "a symmetric 4 × 4 matrix", "a symmetric matrix")
    _float_array(got, (4, 4), "schur_complement(S, [4, 0]) for a symmetric 6 × 6 matrix")
    assert _symmetric_by_the_rule(got), (
        f"expected a symmetric result for a symmetric M (|S[i, j] - S[j, i]| ≤ 1e-12 · max(1, max |S|)), got a largest "
        f"asymmetry of {np.max(np.abs(got - got.T)):.3g} ({SCHUR_HINT})")


def test_schur_complement_takes_integers_returns_floats_and_does_not_modify_M(gauss):
    M = [[6, 1, -2, 0], [1, 5, 1, 2], [-2, 1, 4, 1], [0, 2, 1, 3]]
    want = _schur_by_inverse(np.array(M, dtype=float), [1, 3])
    for given, text in ((M, "a list of integers"), (np.array(M), "an integer array")):
        got = _result(lambda: gauss.schur_complement(given, [1, 3]), _show(want), text)
        _float_array(got, (2, 2), f"schur_complement of {text}")
        _close(got, want, f"schur_complement of {text} with idx = [1, 3]", rtol=1e-12, hint=SCHUR_HINT)
    rng = np.random.default_rng(5864)
    F = _invertible(rng, 4, symmetric=False)
    copy = F.copy()
    got = _result(lambda: gauss.schur_complement(F, [0]), "a 3 × 3 matrix", "a float array")
    assert np.array_equal(F, copy), (
        f"expected M unchanged by schur_complement, got {_show(F)} (never modify the array you receive)")
    got[:] = 99.0
    assert np.array_equal(F, copy), "expected schur_complement to return a new array, but changing it changed M"


M3 = [[4.0, 1.0, 0.5], [1.0, 3.0, -1.0], [0.5, -1.0, 2.4]]
SCHUR_REFUSALS = [
    ([[4.0, 1.0, 0.5], [1.0, 3.0, -1.0]], [0], "M is 2 × 3, not square"),
    ([[4.0]], [0], "M is 1 × 1, smaller than 2 × 2"),
    ([4.0, 1.0], [0], "M is 1-D"),
    (np.ones((2, 2, 2)), [0], "M is 3-D"),
    (M3, [], "idx is empty"),
    (M3, [0, 1, 2], "idx holds every index"),
    (M3, [2, 0, 1], "idx holds every index, in another order"),
    (M3, [1, 1], "idx repeats the index 1"),
    (M3, [3], "the index 3 is out of range for m = 3"),
    (M3, [-1], "the index -1 is out of range: indices go from 0 to m - 1"),
    (M3, 2, "idx is a bare int: write [2]"),
    (M3, np.int64(2), "idx is a bare NumPy integer: write [2]"),
    (M3, True, "idx is a bool"),
    ([[4.0, 1.0], [1.0, 3.0]], [True], "idx holds a bool (np.ix_ would read [True] as a mask)"),
    ([[2.0, 1.0, 3.0], [5.0, 1.0, 7.0], [4.0, 0.5, 6.0]], [0, 2], "the block M[[0, 2]][:, [0, 2]] = [[2, 3], [4, 6]] "
                                                               "is not invertible"),
    ([[0.0, 1.0], [1.0, 2.5]], [0], "the block M[[0]][:, [0]] = [[0]] is not invertible"),
]


@pytest.mark.parametrize("M, idx, why", SCHUR_REFUSALS,
                         ids=["M-not-square", "M-one-by-one", "M-one-d", "M-three-d", "idx-empty", "idx-every-index",
                              "idx-every-index-shuffled", "idx-repeated", "idx-too-large", "idx-negative",
                              "idx-bare-int", "idx-bare-numpy-int", "idx-bool", "idx-holds-a-bool", "block-singular",
                              "block-zero"])
def test_schur_complement_refusals(gauss, M, idx, why):
    _expect_error(ValueError, lambda: gauss.schur_complement(M, idx), f"schur_complement({M!r}, {idx!r})", why)


# --- condition_gaussian ---------------------------------------------------------------------------------------------

COND_HINT = ("with a = the other indices (increasing order) and b = idx: mean μ_a + Σ_ab Σ_bb⁻¹ (values - μ_b), "
             "covariance Σ_aa - Σ_ab Σ_bb⁻¹ Σ_ba, where Σ_ab = cov[a][:, b] and values[j] goes with idx[j]")


def _condition_by_precision(mean, cov, idx, values):
    """The oracle: with Λ = Σ⁻¹ (np.linalg.inv), the conditional law is N(μ_a - Λ_aa⁻¹ Λ_ab (values - μ_b), Λ_aa⁻¹)."""
    mean, cov, values = (np.asarray(v, dtype=float) for v in (mean, cov, values))
    rest = _rest(mean.size, idx)
    P = np.linalg.inv(cov)
    C = np.linalg.inv(P[np.ix_(rest, rest)])
    m = mean[rest] - C @ P[np.ix_(rest, idx)] @ (values - mean[idx])
    return m, C


def _logpdf_numpy(x, mean, cov, what):
    """ln N(x | mean, cov) by np.linalg.slogdet and solve, for a covariance returned by the code under test."""
    sign, logdet = np.linalg.slogdet(cov)
    assert sign > 0 and np.all(np.linalg.eigvalsh((cov + cov.T) / 2) > 0), (
        f"expected {what} to be positive definite, got {_show(cov)} ({COND_HINT})")
    dev = np.asarray(x, dtype=float) - mean
    return -0.5 * (mean.size * math.log(2 * math.pi) + logdet + float(dev @ np.linalg.solve(cov, dev)))


def test_condition_gaussian_docstring_examples(gauss):
    mean, cov = [1, 0, 2], [[5, 2, 2], [2, 4, 0], [2, 0, 4]]
    for idx, values, want_m, want_C in (([2], [4], [2.0, 0.0], [[4.0, 2.0], [2.0, 4.0]]),
                                        ([1, 2], [1, 4], [2.5], [[3.0]])):
        call = f"condition_gaussian([1, 0, 2], [[5, 2, 2], [2, 4, 0], [2, 0, 4]], {idx}, {values})"
        got = _result(lambda: gauss.condition_gaussian(mean, cov, idx, values), f"({want_m}, {want_C})", call)
        m, C = _check_pair(got, ((len(want_m),), np.shape(want_C)), call)
        _close(m, want_m, f"the conditional mean of {call}", rtol=1e-12, atol=1e-12, hint=COND_HINT)
        _close(C, want_C, f"the conditional covariance of {call}", rtol=1e-12, atol=1e-12, hint=COND_HINT)


COND_CASES = [(2, [0]), (2, [1]), (3, [1]), (4, [3, 0]), (5, [1, 2, 4]), (6, [5]), (6, [0, 1, 2, 3, 4]), (7, [2, 6, 3])]


@pytest.mark.parametrize("d, idx", COND_CASES, ids=[f"d{d}-idx{'-'.join(map(str, idx))}" for d, idx in COND_CASES])
def test_condition_gaussian_matches_the_precision_matrix(gauss, d, idx):
    """With Λ = Σ⁻¹ (np.linalg.inv): conditional covariance Λ_aa⁻¹, conditional mean μ_a - Λ_aa⁻¹ Λ_ab (x_b - μ_b)."""
    rng = np.random.default_rng(5865 + COND_CASES.index((d, idx)))
    cov = _spd(rng, d, scale=2.0)
    mean = rng.normal(size=d) * 3.0
    values = mean[idx] + rng.normal(size=len(idx)) * 2.0
    want_m, want_C = _condition_by_precision(mean, cov, idx, values)
    k = len(idx)
    what = f"condition_gaussian(mean, cov, {idx}, values) in dimension {d}"
    got = _result(lambda: gauss.condition_gaussian(mean, cov, idx, values), "(cond_mean, cond_cov)", what)
    m, C = _check_pair(got, ((d - k,), (d - k, d - k)), what)
    _close(C, want_C, f"the conditional covariance for {what}, the inverse of the block of the precision Σ⁻¹ on the "
                      f"indices {_rest(d, idx)}", rtol=1e-9, atol=1e-11, hint=COND_HINT)
    hint = COND_HINT
    if np.allclose(m, 2 * mean[_rest(d, idx)] - want_m, rtol=1e-9):
        hint += " (the shift has the wrong sign: + Σ_ab Σ_bb⁻¹ (values - μ_b))"
    elif np.allclose(m, mean[_rest(d, idx)], rtol=1e-9):
        hint += " (the observed values were not used)"
    _close(m, want_m, f"the conditional mean for {what}, μ_a - Λ_aa⁻¹ Λ_ab (values - μ_b) with Λ = Σ⁻¹", rtol=1e-9,
           atol=1e-11, hint=hint)


def test_condition_gaussian_is_the_ratio_of_the_joint_and_the_marginal_densities(gauss):
    """p(x_a | x_b) = p(x_a, x_b) / p(x_b): ln N(x_a | cond_mean, cond_cov) equals the joint log-density minus the
    log-density of the marginal N(μ_b, Σ_bb), both by scipy.stats.multivariate_normal, at several points x_a."""
    rng = np.random.default_rng(5873)
    for d, idx in ((3, [0]), (5, [4, 1]), (6, [2, 3, 5])):
        cov = _spd(rng, d, scale=1.3)
        mean = rng.normal(size=d)
        rest = _rest(d, idx)
        values = mean[idx] + rng.normal(size=len(idx))
        what = f"condition_gaussian(mean, cov, {idx}, values) in dimension {d}"
        got = _result(lambda: gauss.condition_gaussian(mean, cov, idx, values), "(cond_mean, cond_cov)", what)
        m, C = _check_pair(got, ((len(rest),), (len(rest), len(rest))), what)
        marginal = float(stats.multivariate_normal(mean=mean[idx], cov=cov[np.ix_(idx, idx)]).logpdf(values))
        for _ in range(4):
            x = np.empty(d)
            x[idx] = values
            x[rest] = mean[rest] + rng.normal(size=len(rest)) * 1.5
            want = float(stats.multivariate_normal(mean=mean, cov=cov).logpdf(x)) - marginal
            got_value = _logpdf_numpy(x[rest], m, C, f"the conditional covariance for {what}")
            _close_number(got_value, want, f"ln N(x_a | cond_mean, cond_cov) for {what}, equal to "
                                           f"ln p(x_a, x_b) - ln p(x_b) at x_a = {_show(x[rest])}", rtol=1e-9,
                          atol=1e-10, hint=COND_HINT)


def test_condition_gaussian_covariance_does_not_depend_on_the_values_and_the_mean_is_affine(gauss):
    """The same conditional covariance for any observed values; the conditional mean of the midpoint of two
    observations is the midpoint of their conditional means, and it moves by Σ_ab Σ_bb⁻¹ Δ."""
    rng = np.random.default_rng(5874)
    cov = _spd(rng, 5, scale=1.8)
    mean = rng.normal(size=5)
    idx = [1, 4]
    v1, v2 = mean[idx] + np.array([2.5, -1.0]), mean[idx] + np.array([-3.0, 4.25])
    results = []
    for values in (v1, v2, (v1 + v2) / 2):
        got = _result(lambda: gauss.condition_gaussian(mean, cov, idx, values), "(cond_mean, cond_cov)",
                      f"values = {_show(values)}")
        results.append(_check_pair(got, ((3,), (3, 3)), f"condition_gaussian(mean, cov, [1, 4], {_show(values)})"))
    (m1, C1), (m2, C2), (m3, C3) = results
    for C, text in ((C2, "the second observation"), (C3, "their midpoint")):
        _close(C, C1, f"the conditional covariance for {text}, equal to that of the first observation (it does not "
                      f"depend on the observed values)", rtol=1e-12, atol=1e-13,
               hint="Σ_aa - Σ_ab Σ_bb⁻¹ Σ_ba: the values enter the mean only")
    _close(m3, (m1 + m2) / 2, "the conditional mean of the midpoint of two observations, the midpoint of their "
                              "conditional means (an affine function of the values)", rtol=1e-10, atol=1e-12,
           hint=COND_HINT)
    want_m, want_C = _condition_by_precision(mean, cov, idx, v2)
    _close(m2, want_m, "the conditional mean for the second observation", rtol=1e-9, atol=1e-11, hint=COND_HINT)
    _close(C2, want_C, "the conditional covariance (np.linalg.inv of the block of the precision matrix)", rtol=1e-9,
           atol=1e-11, hint=COND_HINT)


def test_condition_gaussian_order_of_idx_goes_with_the_values(gauss):
    """values[j] is the observed value of the coordinate idx[j]: ([3, 1], [v3, v1]) is ([1, 3], [v1, v3])."""
    rng = np.random.default_rng(5875)
    cov = _spd(rng, 5, scale=1.2)
    mean = rng.normal(size=5)
    v1, v3 = 2.75, -1.5
    want_m, want_C = _condition_by_precision(mean, cov, [1, 3], [v1, v3])
    for idx, values in (([1, 3], [v1, v3]), ([3, 1], [v3, v1]), ((3, 1), np.array([v3, v1]))):
        what = f"condition_gaussian(mean, cov, {idx!r}, {values!r})"
        got = _result(lambda: gauss.condition_gaussian(mean, cov, idx, values), "(cond_mean, cond_cov)", what)
        m, C = _check_pair(got, ((3,), (3, 3)), what)
        _close(m, want_m, f"the conditional mean for {what}, x_1 = {v1} and x_3 = {v3} whatever the order", rtol=1e-9,
               atol=1e-11, hint="values[j] goes with idx[j]: sort neither idx alone nor values alone; the result "
                                "follows rest = [0, 2, 4], in increasing order")
        _close(C, want_C, f"the conditional covariance for {what}", rtol=1e-9, atol=1e-11, hint=COND_HINT)


def test_condition_gaussian_in_dimension_2_follows_the_regression_line(gauss):
    """Σ = [[2.25, -0.72], [-0.72, 0.64]] (σ₁ = 1.5, σ₂ = 0.8, ρ = -0.6), μ = (3, -1): given x₂ = 0.2, the mean is
    μ₁ + (Σ₁₂ / Σ₂₂)(0.2 - μ₂) = 1.65 and the variance σ₁²(1 - ρ²) = 1.44; given x₁ = 4.5, -1.48 and 0.4096."""
    mean, cov = [3.0, -1.0], [[2.25, -0.72], [-0.72, 0.64]]
    for idx, values, want_m, want_v in (([1], [0.2], 1.65, 1.44), ([0], [4.5], -1.48, 0.4096)):
        what = f"condition_gaussian([3, -1], [[2.25, -0.72], [-0.72, 0.64]], {idx}, {values})"
        got = _result(lambda: gauss.condition_gaussian(mean, cov, idx, values), "(cond_mean, cond_cov)", what)
        m, C = _check_pair(got, ((1,), (1, 1)), what)
        _close(m, [want_m], f"the conditional mean for {what} (a negative correlation: a value above its mean pulls "
                            f"the other one below its mean)", rtol=1e-12, atol=1e-12, hint=COND_HINT)
        _close(C, [[want_v]], f"the conditional variance for {what}, σ²(1 - ρ²)", rtol=1e-12, atol=1e-12,
               hint=COND_HINT)


def test_condition_gaussian_independent_blocks_and_a_smaller_symmetric_covariance(gauss):
    """Independent blocks (Σ_ab = 0): the conditional law is the marginal N(μ_a, Σ_aa), whatever the values. In
    general, the conditional covariance is symmetric (by the rule of the module), positive definite, and Σ_aa minus it
    is positive semi-definite: observing never adds uncertainty."""
    Saa = np.array([[2.2, 0.6, -0.3], [0.6, 1.5, 0.2], [-0.3, 0.2, 1.1]])
    Sbb = np.array([[0.9, 0.25], [0.25, 0.7]])
    cov = np.zeros((5, 5))
    cov[np.ix_([0, 2, 3], [0, 2, 3])] = Saa
    cov[np.ix_([1, 4], [1, 4])] = Sbb
    mean = np.array([1.5, -0.5, 0.25, 2.0, -3.0])
    got = _result(lambda: gauss.condition_gaussian(mean, cov, [4, 1], [7.5, -6.0]), "(cond_mean, cond_cov)",
                  "independent blocks")
    m, C = _check_pair(got, ((3,), (3, 3)), "condition_gaussian(mean, cov, [4, 1], [7.5, -6.0]) for independent blocks")
    _close(m, mean[[0, 2, 3]], "the conditional mean for independent blocks, μ_a = mean[[0, 2, 3]] (the observed "
                               "values tell nothing about the others)", rtol=1e-12, atol=1e-14, hint=COND_HINT)
    _close(C, Saa, "the conditional covariance for independent blocks, Σ_aa", rtol=1e-12, atol=1e-14, hint=COND_HINT)
    rng = np.random.default_rng(5876)
    for d, idx in ((4, [2]), (6, [0, 5, 3]), (8, [1, 2, 6, 7])):
        cov = _spd(rng, d, scale=3.0)
        mean = rng.normal(size=d)
        rest = _rest(d, idx)
        what = f"condition_gaussian(mean, cov, {idx}, values) in dimension {d}"
        got = _result(lambda: gauss.condition_gaussian(mean, cov, idx, mean[idx] + 1.0), "(cond_mean, cond_cov)",
                      what)
        m, C = _check_pair(got, ((len(rest),), (len(rest), len(rest))), what)
        assert _symmetric_by_the_rule(C), (
            f"expected a symmetric conditional covariance for {what} (|C[i, j] - C[j, i]| ≤ 1e-12 · max(1, max |C|), "
            f"so that sample_mvn and mvn_logpdf accept it), got a largest asymmetry of {np.max(np.abs(C - C.T)):.3g}")
        sym = (C + C.T) / 2
        assert np.min(np.linalg.eigvalsh(sym)) > 0, (
            f"expected a positive definite conditional covariance for {what}, got the eigenvalues "
            f"{_show(np.linalg.eigvalsh(sym))} ({COND_HINT})")
        gap = np.linalg.eigvalsh(cov[np.ix_(rest, rest)] - sym)
        assert np.min(gap) >= -1e-10, (
            f"expected Σ_aa - cond_cov positive semi-definite for {what} (observing reduces the variances), got the "
            f"eigenvalues {_show(gap)} ({COND_HINT})")


def test_condition_gaussian_takes_lists_returns_new_arrays_and_does_not_modify_its_inputs(gauss):
    mean, cov = [2, -1, 0, 1], [[4, 1, 0, -1], [1, 3, 1, 0], [0, 1, 3, 0], [-1, 0, 0, 5]]
    want_m, want_C = _condition_by_precision(mean, cov, [2], [3])
    for args, text in (((mean, cov, [2], [3]), "lists of integers"),
                       ((np.array(mean), np.array(cov), (2,), np.array([3])), "integer arrays and a tuple idx")):
        got = _result(lambda: gauss.condition_gaussian(*args), "(cond_mean, cond_cov)", text)
        m, C = _check_pair(got, ((3,), (3, 3)), f"condition_gaussian with {text}")
        _close(m, want_m, f"the conditional mean with {text}", rtol=1e-12, atol=1e-12, hint=COND_HINT)
        _close(C, want_C, f"the conditional covariance with {text}", rtol=1e-12, atol=1e-12, hint=COND_HINT)
    rng = np.random.default_rng(5877)
    cov_f, mean_f = _spd(rng, 4), rng.normal(size=4)
    values = np.array([0.4, -0.8])
    copies = [mean_f.copy(), cov_f.copy(), values.copy()]
    got = _result(lambda: gauss.condition_gaussian(mean_f, cov_f, [3, 0], values), "(cond_mean, cond_cov)",
                  "float arrays")
    m, C = _check_pair(got, ((2,), (2, 2)), "condition_gaussian with float arrays")
    for name, value, copy in zip(("mean", "cov", "values"), (mean_f, cov_f, values), copies):
        assert np.array_equal(value, copy), (
            f"expected {name} unchanged by condition_gaussian, got {name} = {_show(value)} (never modify the arrays "
            f"you receive)")
    m[:] = 99.0
    C[:] = 99.0
    assert all(np.array_equal(v, c) for v, c in zip((mean_f, cov_f, values), copies)), (
        "expected condition_gaussian to return new arrays, but changing them changed an input")


MEAN3 = [1.0, -2.0, 0.75]
COND_REFUSALS = [
    ([1.0], [[2.4]], [0], [1.0], "mean has 1 value: at least 2 are needed (one observed, one left)"),
    ([[1.0, -2.0, 0.75]], M3, [0], [1.0], "mean is 2-D"),
    (MEAN3, [[4.0, 1.0], [1.0, 3.0]], [0], [1.0], "cov is 2 × 2 for d = 3"),
    (MEAN3, [[4.0, 1.0, 0.5], [-1.0, 3.0, -1.0], [0.5, -1.0, 2.4]], [0], [1.0], "cov is not symmetric"),
    (MEAN3, [[1.0, 2.0, 0.0], [2.0, 1.0, 0.0], [0.0, 0.0, 1.0]], [0], [1.0], "cov is not positive definite"),
    (MEAN3, M3, [], [], "idx is empty"),
    (MEAN3, M3, [0, 1, 2], [1.0, 1.0, 1.0], "idx holds every index"),
    (MEAN3, M3, [2, 2], [1.0, 1.0], "idx repeats the index 2"),
    (MEAN3, M3, [3], [1.0], "the index 3 is out of range for d = 3"),
    (MEAN3, M3, [-1], [1.0], "the index -1 is out of range"),
    (MEAN3, M3, 1, [1.0], "idx is a bare int: write [1]"),
    (MEAN3, M3, True, [1.0], "idx is a bool"),
    (MEAN3, M3, [1], 1.0, "values is a scalar, even with len(idx) = 1: write [1.0]"),
    (MEAN3, M3, [1], [1.0, 2.0], "values has 2 numbers for 1 index"),
    (MEAN3, M3, [0, 2], [1.0], "values has 1 number for 2 indices"),
    (MEAN3, M3, [1], [[1.0]], "values is 2-D"),
]


@pytest.mark.parametrize("mean, cov, idx, values, why", COND_REFUSALS,
                         ids=["mean-one-value", "mean-two-d", "cov-shape", "cov-not-symmetric", "cov-indefinite",
                              "idx-empty", "idx-every-index", "idx-repeated", "idx-too-large", "idx-negative",
                              "idx-bare-int", "idx-bool", "values-scalar", "values-too-long", "values-too-short",
                              "values-two-d"])
def test_condition_gaussian_refusals(gauss, mean, cov, idx, values, why):
    _expect_error(ValueError, lambda: gauss.condition_gaussian(mean, cov, idx, values),
                  f"condition_gaussian({mean!r}, {cov!r}, {idx!r}, {values!r})", why)


# --- linreg_posterior -----------------------------------------------------------------------------------------------

POSTERIOR_HINT = ("S_N = (S_0⁻¹ + ΦᵀΦ / σ²)⁻¹ and m_N = S_N (S_0⁻¹ m_0 + Φᵀ y / σ²), with σ² = noise_var itself "
                  "(a variance) and the prior precision S_0⁻¹ (np.linalg.solve(S_0, I))")


def _posterior_by_inverse(Phi, y, m0, S0, s2):
    """The oracle: the precision form with np.linalg.inv."""
    Phi, y, m0, S0 = (np.asarray(v, dtype=float) for v in (Phi, y, m0, S0))
    P0 = np.linalg.inv(S0)
    S = np.linalg.inv(P0 + Phi.T @ Phi / s2)
    return S @ (P0 @ m0 + Phi.T @ y / s2), S


def _posterior_one_at_a_time(Phi, y, m0, S0, s2):
    """The oracle: one observation at a time in the covariance form, without any inverse (each posterior is the prior
    of the next step): k = S φ / (σ² + φᵀ S φ), m ← m + k (y - φᵀ m), S ← S - k φᵀ S."""
    m, S = np.array(m0, dtype=float), np.array(S0, dtype=float)
    for phi, target in zip(np.asarray(Phi, dtype=float), np.asarray(y, dtype=float)):
        Sphi = S @ phi
        k = Sphi / (s2 + phi @ Sphi)
        m = m + k * (target - phi @ m)
        S = S - np.outer(k, Sphi)
        S = (S + S.T) / 2
    return m, S


def _posterior_hint(got, Phi, y, m0, S0, s2):
    """POSTERIOR_HINT, plus the classic error that the result got matches, if any."""
    if not (isinstance(got, tuple) and len(got) == 2):
        return POSTERIOR_HINT
    m, S = (np.asarray(v, dtype=float) for v in got)
    want_m, want_S = _posterior_by_inverse(Phi, y, m0, S0, s2)
    p = want_m.size
    Phi_, y_, m0_ = (np.asarray(v, dtype=float) for v in (Phi, y, m0))
    if m.shape != (p,) or S.shape != (p, p):
        return POSTERIOR_HINT
    gram = Phi_.T @ Phi_
    S_flat = np.linalg.inv(gram / s2) if np.linalg.matrix_rank(gram) == p else None     # no prior precision at all
    candidates = [
        (_posterior_by_inverse(Phi, y, m0, S0, s2 ** 2), "noise_var is already σ²: divide by noise_var, not by its "
                                                         "square"),
        (_posterior_by_inverse(Phi, y, m0, S0, math.sqrt(s2)), "noise_var is σ², a variance: divide by noise_var, "
                                                               "not by its square root"),
        (_posterior_by_inverse(Phi, y, m0, np.linalg.inv(S0), s2), "the prior precision is S_0⁻¹, not S_0"),
        ((np.linalg.inv(np.linalg.inv(S0) + Phi_.T @ Phi_ / s2) @ (Phi_.T @ y_ / s2),
          np.linalg.inv(np.linalg.inv(S0) + Phi_.T @ Phi_ / s2)), "the prior mean was left out: + S_0⁻¹ m_0"),
        ((np.linalg.inv(np.linalg.inv(S0) + Phi_.T @ Phi_ / s2) @ (m0_ + Phi_.T @ y_ / s2),
          np.linalg.inv(np.linalg.inv(S0) + Phi_.T @ Phi_ / s2)), "the prior mean is weighed by S_0⁻¹: S_0⁻¹ m_0"),
    ]
    if S_flat is not None:
        candidates.append(((S_flat @ (Phi_.T @ y_ / s2), S_flat), "the prior precision S_0⁻¹ was left out"))
    for (cm, cS), text in candidates:
        if np.allclose(cm, want_m) and np.allclose(cS, want_S):
            continue
        if np.allclose(m, cm, rtol=1e-8, atol=1e-10) and np.allclose(S, cS, rtol=1e-8, atol=1e-10):
            return f"{POSTERIOR_HINT}; here {text}"
    return POSTERIOR_HINT


def _random_regression(rng, n, p):
    """(Phi, y, m0, S0): random features, targets from random weights plus noise, a full prior covariance."""
    Phi = rng.normal(size=(n, p)) * 1.5
    theta = rng.normal(size=p) * 2.0
    y = Phi @ theta + rng.normal(size=n) * 0.7
    return Phi, y, rng.normal(size=p), _spd(rng, p, scale=2.5)


def test_linreg_posterior_docstring_examples(gauss):
    call = "linreg_posterior([[1, 0], [1, 1], [1, 2]], [1, 2, 2], [0, 0], [[1, 0], [0, 1]], 1.0)"
    got = _result(lambda: gauss.linreg_posterior([[1, 0], [1, 1], [1, 2]], [1, 2, 2], [0, 0], [[1, 0], [0, 1]], 1.0),
                  "(array([0.8, 0.6]), array([[0.4, -0.2], [-0.2, 0.2667]])) (rounded)", call)
    m, S = _check_pair(got, ((2,), (2, 2)), call)
    _close(m, [0.8, 0.6], f"m_N for {call}", rtol=1e-12, atol=1e-12, hint=POSTERIOR_HINT)
    _close(S, [[0.4, -0.2], [-0.2, 4 / 15]], f"S_N for {call}", rtol=1e-12, atol=1e-12, hint=POSTERIOR_HINT)
    call = "linreg_posterior(np.zeros((0, 2)), [], [1, 2], [[1, 0], [0, 1]], 0.5)"
    got = _result(lambda: gauss.linreg_posterior(np.zeros((0, 2)), [], [1, 2], [[1, 0], [0, 1]], 0.5),
                  "(array([1., 2.]), array([[1., 0.], [0., 1.]])) (the prior)", call)
    m, S = _check_pair(got, ((2,), (2, 2)), call)
    _close(m, [1.0, 2.0], f"m_N for {call} (no data: the prior mean)", rtol=1e-12, atol=1e-12, hint=POSTERIOR_HINT)
    _close(S, np.eye(2), f"S_N for {call} (no data: the prior covariance)", rtol=1e-12, atol=1e-12,
           hint=POSTERIOR_HINT)


REGRESSIONS = [(12, 2, 0.36), (30, 3, 2.25), (5, 4, 0.8), (1, 1, 1.7), (40, 6, 0.05), (3, 5, 4.0), (8, 1, 0.3)]


@pytest.mark.parametrize("n, p, s2", REGRESSIONS, ids=[f"n{n}-p{p}" for n, p, _ in REGRESSIONS])
def test_linreg_posterior_matches_the_precision_form(gauss, n, p, s2):
    rng = np.random.default_rng(5880 + REGRESSIONS.index((n, p, s2)))
    Phi, y, m0, S0 = _random_regression(rng, n, p)
    want_m, want_S = _posterior_by_inverse(Phi, y, m0, S0, s2)
    what = f"linreg_posterior(Phi, y, m0, S0, {s2}) for n = {n} examples and p = {p} weights"
    got = _result(lambda: gauss.linreg_posterior(Phi, y, m0, S0, s2), "(m_N, S_N)", what)
    m, S = _check_pair(got, ((p,), (p, p)), what)
    hint = _posterior_hint(got, Phi, y, m0, S0, s2)
    _close(S, want_S, f"S_N for {what}, (S_0⁻¹ + ΦᵀΦ / σ²)⁻¹ by np.linalg.inv", rtol=1e-9, atol=1e-12, hint=hint)
    _close(m, want_m, f"m_N for {what}, S_N (S_0⁻¹ m_0 + Φᵀ y / σ²) by np.linalg.inv", rtol=1e-9, atol=1e-11,
           hint=hint)


def test_linreg_posterior_matches_one_observation_at_a_time(gauss):
    """Each observation updates the law of the weights in turn (the covariance form, without any inverse): after the
    last one, the posterior of all the data."""
    rng = np.random.default_rng(5887)
    for n, p, s2 in ((15, 3, 0.45), (6, 2, 3.2), (2, 4, 0.9)):
        Phi, y, m0, S0 = _random_regression(rng, n, p)
        want_m, want_S = _posterior_one_at_a_time(Phi, y, m0, S0, s2)
        what = f"linreg_posterior(Phi, y, m0, S0, {s2}) for n = {n} and p = {p}"
        got = _result(lambda: gauss.linreg_posterior(Phi, y, m0, S0, s2), "(m_N, S_N)", what)
        m, S = _check_pair(got, ((p,), (p, p)), what)
        hint = _posterior_hint(got, Phi, y, m0, S0, s2)
        _close(S, want_S, f"S_N for {what}, after {n} updates of one observation each", rtol=1e-9, atol=1e-12,
               hint=hint)
        _close(m, want_m, f"m_N for {what}, after {n} updates of one observation each", rtol=1e-9, atol=1e-11,
               hint=hint)


def test_linreg_posterior_is_the_conditional_law_of_the_weights_given_the_targets(gauss):
    """(θ, y) is a Gaussian vector: y = Φ θ + ε has mean Φ m_0 and covariance Φ S_0 Φᵀ + σ² I, and
    Cov(θ, y) = S_0 Φᵀ; the posterior is the law of θ given y (here with np.linalg.inv of the covariance of y)."""
    rng = np.random.default_rng(5888)
    for n, p, s2 in ((4, 3, 0.6), (10, 2, 1.9)):
        Phi, y, m0, S0 = _random_regression(rng, n, p)
        K = np.linalg.inv(Phi @ S0 @ Phi.T + s2 * np.eye(n))
        want_m = m0 + S0 @ Phi.T @ K @ (y - Phi @ m0)
        want_S = S0 - S0 @ Phi.T @ K @ Phi @ S0
        what = f"linreg_posterior(Phi, y, m0, S0, {s2}) for n = {n} and p = {p}"
        got = _result(lambda: gauss.linreg_posterior(Phi, y, m0, S0, s2), "(m_N, S_N)", what)
        m, S = _check_pair(got, ((p,), (p, p)), what)
        _close(S, want_S, f"S_N for {what}, the conditional covariance S_0 - S_0 Φᵀ (Φ S_0 Φᵀ + σ² I)⁻¹ Φ S_0",
               rtol=1e-8, atol=1e-11, hint=_posterior_hint(got, Phi, y, m0, S0, s2))
        _close(m, want_m, f"m_N for {what}, the conditional mean m_0 + S_0 Φᵀ (Φ S_0 Φᵀ + σ² I)⁻¹ (y - Φ m_0)",
               rtol=1e-8, atol=1e-10, hint=_posterior_hint(got, Phi, y, m0, S0, s2))


def test_linreg_posterior_with_no_data_is_the_prior(gauss):
    rng = np.random.default_rng(5889)
    for p in (1, 3):
        m0, S0 = rng.normal(size=p), _spd(rng, p, scale=1.7)
        for y, text in (([], "y = []"), (np.zeros(0), "y = np.zeros(0)")):
            what = f"linreg_posterior(np.zeros((0, {p})), {text}, m0, S0, 0.7)"
            got = _result(lambda: gauss.linreg_posterior(np.zeros((0, p)), y, m0, S0, 0.7), "(m0, S0)", what)
            m, S = _check_pair(got, ((p,), (p, p)), what)
            _close(m, m0, f"m_N for {what} (no data: the prior mean m_0)", rtol=1e-10, atol=1e-12, hint=POSTERIOR_HINT)
            _close(S, S0, f"S_N for {what} (no data: the prior covariance S_0)", rtol=1e-10, atol=1e-12,
                   hint=POSTERIOR_HINT)


def test_linreg_posterior_mean_is_the_ridge_solution(gauss):
    """m_0 = 0 and S_0 = τ² I: m_N minimizes ‖y - Φ θ‖² + λ ‖θ‖² with λ = σ²/τ², the least squares solution of the
    stacked system [Φ; √λ I] θ ≈ [y; 0] (np.linalg.lstsq)."""
    rng = np.random.default_rng(5890)
    for n, p, s2, tau2 in ((25, 4, 0.36, 2.25), (6, 3, 1.3, 0.4), (3, 5, 0.8, 3.5)):
        Phi, y, _, _ = _random_regression(rng, n, p)
        lam = s2 / tau2
        stacked = np.vstack([Phi, math.sqrt(lam) * np.eye(p)])
        want = np.linalg.lstsq(stacked, np.concatenate([y, np.zeros(p)]), rcond=None)[0]
        what = f"m_N of linreg_posterior(Phi, y, 0, {tau2} I, {s2}) for n = {n} and p = {p}"
        got = _result(lambda: gauss.linreg_posterior(Phi, y, np.zeros(p), tau2 * np.eye(p), s2), "(m_N, S_N)", what)
        m, _ = _check_pair(got, ((p,), (p, p)), what)
        _close(m, want, f"{what}, the ridge solution of λ = σ²/τ² = {lam:.6g} (np.linalg.lstsq)", rtol=1e-9,
               atol=1e-11, hint=_posterior_hint(got, Phi, y, np.zeros(p), tau2 * np.eye(p), s2))


def test_linreg_posterior_in_two_batches_and_in_any_order(gauss):
    """The posterior of a first batch, used as the prior of the second, gives the posterior of all the data; the order
    of the examples does not matter."""
    rng = np.random.default_rng(5891)
    Phi, y, m0, S0 = _random_regression(rng, 20, 3)
    s2 = 0.85
    full = _result(lambda: gauss.linreg_posterior(Phi, y, m0, S0, s2), "(m_N, S_N)", "all 20 examples")
    m, S = _check_pair(full, ((3,), (3, 3)), "linreg_posterior of 20 examples")
    first = _result(lambda: gauss.linreg_posterior(Phi[:8], y[:8], m0, S0, s2), "(m_8, S_8)", "the first 8 examples")
    m8, S8 = _check_pair(first, ((3,), (3, 3)), "linreg_posterior of the first 8 examples")
    second = _result(lambda: gauss.linreg_posterior(Phi[8:], y[8:], m8, S8, s2), "(m_N, S_N)",
                     "the last 12 examples, with the posterior of the first 8 as prior")
    m2, S2 = _check_pair(second, ((3,), (3, 3)), "linreg_posterior of the last 12 examples with prior N(m_8, S_8)")
    _close(m2, m, "m_N in two batches (8, then 12 examples), equal to m_N of all 20 at once", rtol=1e-9, atol=1e-11,
           hint=POSTERIOR_HINT)
    _close(S2, S, "S_N in two batches, equal to S_N of all 20 at once", rtol=1e-9, atol=1e-12, hint=POSTERIOR_HINT)
    order = rng.permutation(20)
    shuffled = _result(lambda: gauss.linreg_posterior(Phi[order], y[order], m0, S0, s2), "(m_N, S_N)",
                       "the 20 examples in another order")
    ms, Ss = _check_pair(shuffled, ((3,), (3, 3)), "linreg_posterior of the 20 examples in another order")
    _close(ms, m, "m_N for the examples in another order (rows of Phi and y shuffled together)", rtol=1e-10,
           atol=1e-12, hint=POSTERIOR_HINT)
    _close(Ss, S, "S_N for the examples in another order", rtol=1e-10, atol=1e-12, hint=POSTERIOR_HINT)


def test_linreg_posterior_noise_var_is_a_variance(gauss):
    """noise_var = σ² = 4 means a noise of standard deviation 2: the data weigh 1/4 in the precision, not 1/16 nor
    1/2; a larger noise variance leaves the posterior closer to the prior."""
    rng = np.random.default_rng(5892)
    Phi, y, m0, S0 = _random_regression(rng, 10, 2)
    want_m, want_S = _posterior_by_inverse(Phi, y, m0, S0, 4.0)
    got = _result(lambda: gauss.linreg_posterior(Phi, y, m0, S0, 4.0), "(m_N, S_N)", "noise_var = 4.0")
    m, S = _check_pair(got, ((2,), (2, 2)), "linreg_posterior(Phi, y, m0, S0, 4.0)")
    hint = _posterior_hint(got, Phi, y, m0, S0, 4.0)
    _close(S, want_S, "S_N for noise_var = 4.0, (S_0⁻¹ + ΦᵀΦ / 4)⁻¹", rtol=1e-9, atol=1e-12, hint=hint)
    _close(m, want_m, "m_N for noise_var = 4.0", rtol=1e-9, atol=1e-11, hint=hint)
    variances = []
    for s2 in (0.05, 0.6, 6.0, 600.0):
        got = _result(lambda: gauss.linreg_posterior(Phi, y, m0, S0, s2), "(m_N, S_N)", f"noise_var = {s2}")
        variances.append(np.trace(_check_pair(got, ((2,), (2, 2)), f"linreg_posterior(…, {s2})")[1]))
    assert all(a < b for a, b in zip(variances, variances[1:])) and variances[-1] < np.trace(S0), (
        f"expected the total posterior variance tr S_N to grow with noise_var (0.05, 0.6, 6, 600) and stay below "
        f"tr S_0 = {np.trace(S0):.6g}, got {_show(variances)} ({POSTERIOR_HINT})")


def test_linreg_posterior_covariance_is_symmetric_and_below_the_prior(gauss):
    """S_N is symmetric (by the rule of the module), positive definite, and S_0 - S_N is positive semi-definite: data
    never add uncertainty on the weights."""
    rng = np.random.default_rng(5893)
    for n, p, s2 in ((50, 5, 0.2), (4, 6, 1.1), (200, 3, 0.01)):
        Phi, y, m0, S0 = _random_regression(rng, n, p)
        what = f"linreg_posterior(Phi, y, m0, S0, {s2}) for n = {n} and p = {p}"
        got = _result(lambda: gauss.linreg_posterior(Phi, y, m0, S0, s2), "(m_N, S_N)", what)
        _, S = _check_pair(got, ((p,), (p, p)), what)
        assert _symmetric_by_the_rule(S), (
            f"expected a symmetric S_N for {what} (|S[i, j] - S[j, i]| ≤ 1e-12 · max(1, max |S|), so that sample_mvn "
            f"accepts it), got a largest asymmetry of {np.max(np.abs(S - S.T)):.3g}")
        sym = (S + S.T) / 2
        assert np.min(np.linalg.eigvalsh(sym)) > 0, (
            f"expected a positive definite S_N for {what}, got the eigenvalues {_show(np.linalg.eigvalsh(sym))} "
            f"({POSTERIOR_HINT})")
        gap = np.linalg.eigvalsh(S0 - sym)
        assert np.min(gap) >= -1e-10, (
            f"expected S_0 - S_N positive semi-definite for {what} (precisions add up), got the eigenvalues "
            f"{_show(gap)} ({POSTERIOR_HINT})")


def test_linreg_posterior_takes_integers_returns_floats_and_does_not_modify_its_inputs(gauss):
    Phi, y, m0, S0 = [[1, 2], [0, -1], [3, 1], [2, 2]], [4, -1, 5, 3], [1, 0], [[5, -1], [-1, 3]]
    want_m, want_S = _posterior_by_inverse(Phi, y, m0, S0, 2.0)
    for args, text in (((Phi, y, m0, S0, 2), "lists of integers and noise_var = 2 (an int)"),
                       ((np.array(Phi), np.array(y), np.array(m0), np.array(S0), np.float64(2.0)),
                        "integer arrays and noise_var = np.float64(2.0)")):
        got = _result(lambda: gauss.linreg_posterior(*args), "(m_N, S_N)", text)
        m, S = _check_pair(got, ((2,), (2, 2)), f"linreg_posterior with {text}")
        _close(m, want_m, f"m_N with {text}", rtol=1e-10, atol=1e-12, hint=POSTERIOR_HINT)
        _close(S, want_S, f"S_N with {text}", rtol=1e-10, atol=1e-12, hint=POSTERIOR_HINT)
    rng = np.random.default_rng(5894)
    arrays = _random_regression(rng, 7, 3)
    copies = [a.copy() for a in arrays]
    got = _result(lambda: gauss.linreg_posterior(*arrays, 0.6), "(m_N, S_N)", "float arrays")
    m, S = _check_pair(got, ((3,), (3, 3)), "linreg_posterior with float arrays")
    for name, value, copy in zip(("Phi", "y", "prior_mean", "prior_cov"), arrays, copies):
        assert np.array_equal(value, copy), (
            f"expected {name} unchanged by linreg_posterior, got {name} = {_show(value)} (never modify the arrays you "
            f"receive)")
    m[:] = 99.0
    S[:] = 99.0
    assert all(np.array_equal(v, c) for v, c in zip(arrays, copies)), (
        "expected linreg_posterior to return new arrays, but changing them changed an input")
    empty = _result(lambda: gauss.linreg_posterior(np.zeros((0, 3)), [], arrays[2], arrays[3], 0.6), "(m0, S0)",
                    "no data")
    me, Se = _check_pair(empty, ((3,), (3, 3)), "linreg_posterior with no data")
    me[:] = 99.0
    Se[:] = 99.0
    assert np.array_equal(arrays[2], copies[2]) and np.array_equal(arrays[3], copies[3]), (
        "expected new arrays without data too, but changing them changed prior_mean or prior_cov (return copies)")


PHI2, Y2, M02, S02 = [[1.0, 0.5], [1.0, -1.5], [1.0, 2.0]], [0.4, -1.2, 2.6], [0.0, 1.0], [[2.4, 0.3], [0.3, 1.5]]
POSTERIOR_REFUSALS = [
    ([1.0, 0.5, 2.0], Y2, [0.0], [[2.0]], 0.5, "Phi is 1-D"),
    (np.zeros((3, 0)), Y2, [], np.zeros((0, 0)), 0.5, "Phi has no column (p = 0)"),
    (np.zeros((3, 2, 1)), Y2, M02, S02, 0.5, "Phi is 3-D"),
    (PHI2, [0.4, -1.2], M02, S02, 0.5, "y has 2 targets for 3 rows of Phi"),
    (PHI2, [[0.4], [-1.2], [2.6]], M02, S02, 0.5, "y is a 2-D column, not 1-D"),
    (PHI2, Y2, [0.0, 1.0, 2.0], S02, 0.5, "prior_mean has 3 values for p = 2"),
    (PHI2, Y2, [[0.0, 1.0]], S02, 0.5, "prior_mean is 2-D"),
    (PHI2, Y2, M02, [[2.4, 0.3, 0.0], [0.3, 1.5, 0.0], [0.0, 0.0, 1.0]], 0.5, "prior_cov is 3 × 3 for p = 2"),
    (PHI2, Y2, M02, [[2.4, 0.3], [-0.3, 1.5]], 0.5, "prior_cov is not symmetric"),
    (PHI2, Y2, M02, [[1.0, 2.0], [2.0, 1.0]], 0.5, "prior_cov is not positive definite"),
    (PHI2, Y2, M02, S02, 0.0, "noise_var = 0"),
    (PHI2, Y2, M02, S02, -0.5, "noise_var = -0.5"),
    (PHI2, Y2, M02, S02, math.inf, "noise_var = inf"),
    (PHI2, Y2, M02, S02, math.nan, "noise_var = nan"),
    (PHI2, Y2, M02, S02, True, "noise_var = True: a bool is refused"),
    (PHI2, Y2, M02, S02, None, "noise_var = None"),
]


@pytest.mark.parametrize("Phi, y, prior_mean, prior_cov, noise_var, why", POSTERIOR_REFUSALS,
                         ids=["Phi-one-d", "Phi-no-column", "Phi-three-d", "y-length", "y-column", "prior-mean-length",
                              "prior-mean-two-d", "prior-cov-shape", "prior-cov-not-symmetric", "prior-cov-indefinite",
                              "noise-zero", "noise-negative", "noise-inf", "noise-nan", "noise-bool", "noise-none"])
def test_linreg_posterior_refusals(gauss, Phi, y, prior_mean, prior_cov, noise_var, why):
    _expect_error(ValueError, lambda: gauss.linreg_posterior(Phi, y, prior_mean, prior_cov, noise_var),
                  f"linreg_posterior({Phi!r}, {y!r}, {prior_mean!r}, {prior_cov!r}, {noise_var!r})", why)
