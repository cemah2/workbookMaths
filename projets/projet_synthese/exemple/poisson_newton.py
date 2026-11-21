"""Poisson regression fitted by Newton's method (iteratively reweighted least squares).

The worked example of the synthesis project (``projets/projet_synthese/exemple/exemple.ipynb`` derives every formula
used here). The model: counts ``y_i ~ Poisson(mu_i)`` with ``ln mu_i = x_i . w`` (the canonical link), for the rows
``x_i`` of a design matrix ``X`` of shape ``(n, p)`` whose columns are linearly independent (usually a column of ones
and ``p - 1`` features). Writing ``z = X w`` and ``mu = exp(z)`` (elementwise):

* log-likelihood   ``l(w) = sum_i [y_i z_i - exp(z_i) - ln(y_i!)]``;
* gradient         ``grad l(w) = X^T (y - mu)``, of shape ``(p,)``, like ``w``;
* Hessian          ``H(w) = -X^T diag(mu) X``, of shape ``(p, p)``, negative definite;
* Newton direction ``delta = -H^{-1} grad l = (X^T W X)^{-1} X^T (y - mu)`` with ``W = diag(mu)``: the weighted least
  squares coefficients of the working residuals ``(y - mu) / mu`` on ``X``, with the weights ``mu``.

Conventions: vectors are 1-D NumPy arrays (columns in the formulas of the notebook); every gradient has the shape of
the variable. Only NumPy, ``math`` and ``mymath`` are imported, and five published functions of ``mymath`` do part of
the work: ``orthogonal.least_squares_qr`` (the weighted least squares step), ``svd_pca.condition_number`` (full rank,
and weights that collapse), ``eigen.cholesky`` (standard errors), ``approx.newton`` (the model without features) and
``iterative.critical_step_size`` (the learning rate of a gradient ascent, for comparison).

>>> import numpy as np
>>> X = np.column_stack([np.ones(5), [-1.0, 0.0, 1.0, 2.0, 3.0]])
>>> y = np.array([0, 1, 2, 4, 5])
>>> newton_direction(np.zeros(2), X, y)            # from w = 0: least squares of y - 1 on X, (1/10, 13/10)
array([0.1, 1.3])
>>> np.round(fit(X, y).w, 6)
array([-0.120104,  0.629163])
"""

from __future__ import annotations

import math

import numpy as np

try:
    from mymath import approx, eigen, iterative, orthogonal, svd_pca
except ImportError as exc:  # mymath is registered by wbm.load_mymath (setup cell of the notebook, or conftest.py)
    raise ImportError("poisson_newton needs the library mymath: load it first, with wbm.load_mymath(\"ref\") in a "
                      "notebook, or run pytest from this folder (its conftest.py loads it)") from exc

__all__ = ["NoMaximumError", "PoissonFit", "check_data", "mean", "log_likelihood", "gradient", "hessian",
           "newton_direction", "fit", "standard_errors", "intercept_only", "critical_learning_rate",
           "gradient_ascent"]

# A fitted mean below this value, for a count y_i = 0, counts as "gone to 0" in the diagnosis of NoMaximumError.
COLLAPSED_MEAN = 1e-8


class NoMaximumError(RuntimeError):
    """The log-likelihood has no maximum: Newton's iterates run away instead of converging.

    It happens exactly when some direction ``d != 0`` has ``X d <= 0`` coordinate by coordinate, with ``(X d)_i = 0``
    for every count ``y_i > 0`` (all counts 0 with a column of ones; a group of rows, picked out by a 0/1 feature, whose
    counts are all 0). Along ``d`` the log-likelihood keeps increasing: the fitted means of some counts ``y_i = 0``
    tend to 0 and ``||w||`` grows without end.

    Attributes
    ----------
    history : list of numpy.ndarray
        The iterates ``w_0, w_1, ...`` computed before the error (each of shape ``(p,)``).
    log_likelihoods : list of float
        ``l(w_k)`` for each iterate.
    """

    def __init__(self, message: str, history=None, log_likelihoods=None):
        super().__init__(message)
        self.history = list(history or [])
        self.log_likelihoods = list(log_likelihoods or [])


class PoissonFit:
    """The result of :func:`fit`.

    Attributes
    ----------
    w : numpy.ndarray
        The maximum likelihood weights, shape ``(p,)``.
    n_iter : int
        The number of Newton steps taken.
    history : list of numpy.ndarray
        The iterates ``w_0, w_1, ..., w_K`` (``K = n_iter``), each of shape ``(p,)``.
    log_likelihoods : list of float
        ``l(w_k)`` for each iterate: a non-decreasing list (up to rounding, see :func:`fit`).
    step_sizes : list of float
        The fraction ``t`` of each Newton step that was taken (1 for a full step, 1/2, 1/4... when halved).
    gradient_norm : float
        ``max_j |grad l(w)_j|`` at the returned ``w``.
    """

    def __init__(self, w, n_iter, history, log_likelihoods, step_sizes, gradient_norm):
        self.w = w
        self.n_iter = n_iter
        self.history = history
        self.log_likelihoods = log_likelihoods
        self.step_sizes = step_sizes
        self.gradient_norm = gradient_norm

    def __repr__(self) -> str:
        return (f"PoissonFit(w={np.array2string(self.w, precision=6)}, n_iter={self.n_iter}, "
                f"gradient_norm={self.gradient_norm:.1e})")


def check_data(X, y):
    """Check a design matrix and a vector of counts, and return them as float arrays.

    The hypotheses (H1) (integer counts >= 0) and (H2) (linearly independent columns) of the notebook's §2.

    Parameters
    ----------
    X : 2-D array-like
        The ``(n, p)`` design matrix, finite, with ``1 <= p <= n`` linearly independent columns (a column of ones
        included, if the model has an intercept).
    y : 1-D array-like
        The ``n`` observed counts: integers ``>= 0`` (``3`` and ``3.0`` are accepted, ``2.5`` and ``-1`` are not).

    Returns
    -------
    tuple of numpy.ndarray
        New arrays ``(X, y)`` of floats, of shapes ``(n, p)`` and ``(n,)``.

    Raises
    ------
    ValueError
        If ``X`` is not 2-D, empty or not finite; if ``y`` is not 1-D, has another length than the number of rows of
        ``X``, or holds a negative, non-integer or non-finite value; if ``p > n`` or the columns of ``X`` are linearly
        dependent (``svd_pca.condition_number(X)`` is infinite: it also refuses a condition number above about
        ``1e6``, see its docstring).
    """
    try:
        Xm = np.array(X, dtype=float)
        yv = np.array(y, dtype=float)
    except (TypeError, ValueError):
        raise ValueError("X and y must be arrays of numbers") from None
    if Xm.ndim != 2 or Xm.size == 0:
        raise ValueError(f"X must be a non-empty 2-D array (n, p), got the shape {Xm.shape}")
    if not np.all(np.isfinite(Xm)):
        raise ValueError("X must hold finite numbers only")
    n, p = Xm.shape
    if yv.ndim != 1 or yv.shape[0] != n:
        raise ValueError(f"y must be a 1-D array of length {n} (the rows of X), got the shape {yv.shape}")
    if not np.all(np.isfinite(yv)):
        raise ValueError("y must hold finite numbers only")
    if np.any(yv < 0):
        raise ValueError(f"y must hold counts >= 0, got the value {yv[yv < 0][0]:g}")
    if np.any(yv != np.floor(yv)):
        raise ValueError(f"y must hold integer counts, got the value {yv[yv != np.floor(yv)][0]:g}")
    if p > n:
        raise ValueError(f"X has more columns ({p}) than rows ({n}): its columns cannot be linearly independent")
    if not np.any(Xm) or svd_pca.condition_number(Xm) == math.inf:
        raise ValueError("the columns of X must be linearly independent (svd_pca.condition_number(X) is infinite)")
    return Xm, yv


def _weights_vector(w, p: int):
    """``w`` as a new float array of shape ``(p,)``, or ValueError."""
    wv = np.array(w, dtype=float)
    if wv.shape != (p,) or not np.all(np.isfinite(wv)):
        raise ValueError(f"w must be a finite 1-D array of length {p} (the columns of X), got the shape {wv.shape}")
    return wv


def _matrix(X):
    """``X`` as a 2-D float array (no other check: the public functions of this module validate their data)."""
    Xm = np.asarray(X, dtype=float)
    if Xm.ndim != 2:
        raise ValueError(f"X must be a 2-D array (n, p), got the shape {Xm.shape}")
    return Xm


def _log_factorial(y):
    """``ln(y_i!)`` for integer counts ``y_i >= 0``: ``T[y_i]`` with ``T[m] = ln 1 + ... + ln m`` (``T[0] = 0``)."""
    counts = np.asarray(y, dtype=float).astype(np.int64)
    table = np.concatenate([[0.0], np.cumsum(np.log(np.arange(1, int(counts.max(initial=0)) + 1)))])
    return table[counts]


def mean(w, X):
    """Return the fitted means ``mu = exp(X w)``, shape ``(n,)`` (Eq. (2.2) of the notebook).

    Parameters
    ----------
    w : 1-D array-like
        The ``p`` weights.
    X : 2-D array-like
        The ``(n, p)`` design matrix.

    Returns
    -------
    numpy.ndarray
        ``exp(X w)``: positive, ``inf`` where ``x_i . w`` exceeds about 709 (float64 overflow, no warning).

    Raises
    ------
    ValueError
        If the shapes do not match.
    """
    Xm = _matrix(X)
    wv = _weights_vector(w, Xm.shape[1])
    with np.errstate(over="ignore"):
        return np.exp(Xm @ wv)


def log_likelihood(w, X, y):
    """Return the Poisson log-likelihood ``l(w) = sum_i [y_i z_i - exp(z_i) - ln(y_i!)]``, with ``z = X w`` (Eq. (3.1)).

    The constant ``-sum_i ln(y_i!)`` does not change the maximum; it is kept so that ``l`` is the log of a
    probability. ``ln(y_i!) = ln 1 + ln 2 + ... + ln y_i`` is read in a cumulative sum of logarithms (no loop over
    the examples; memory in ``max(y)``).

    Parameters
    ----------
    w : 1-D array-like
        The ``p`` weights.
    X : 2-D array-like
        The ``(n, p)`` design matrix.
    y : 1-D array-like
        The ``n`` counts.

    Returns
    -------
    float
        ``l(w) <= 0``; ``-inf`` if a fitted mean overflows.

    Raises
    ------
    ValueError
        If the data are not valid (see :func:`check_data`, without the rank check) or the shapes do not match.
    """
    Xm = _matrix(X)
    wv = _weights_vector(w, Xm.shape[1])
    yv = np.asarray(y, dtype=float)
    if yv.shape != (Xm.shape[0],):
        raise ValueError(f"y must be a 1-D array of length {Xm.shape[0]}, got the shape {yv.shape}")
    z = Xm @ wv
    with np.errstate(over="ignore"):
        mu = np.exp(z)
    if not np.all(np.isfinite(mu)):
        return -math.inf
    return float(np.sum(yv * z - mu) - np.sum(_log_factorial(yv)))


def gradient(w, X, y):
    """Return the gradient of the log-likelihood, ``X^T (y - mu)``, of shape ``(p,)`` (the shape of ``w``; Eq. (3.2)).

    Parameters
    ----------
    w : 1-D array-like
        The ``p`` weights.
    X : 2-D array-like
        The ``(n, p)`` design matrix.
    y : 1-D array-like
        The ``n`` counts.

    Returns
    -------
    numpy.ndarray
        ``X^T (y - exp(X w))``.

    Raises
    ------
    ValueError
        If the shapes do not match.
    """
    Xm = _matrix(X)
    yv = np.asarray(y, dtype=float)
    if yv.shape != (Xm.shape[0],):
        raise ValueError(f"y must be a 1-D array of length {Xm.shape[0]}, got the shape {yv.shape}")
    return Xm.T @ (yv - mean(w, Xm))


def hessian(w, X):
    """Return the Hessian of the log-likelihood, ``-X^T diag(mu) X``, of shape ``(p, p)`` (Eq. (3.3)).

    It does not depend on the counts ``y``. It is symmetric (made exactly so) and negative definite when the
    columns of ``X`` are linearly independent.

    Parameters
    ----------
    w : 1-D array-like
        The ``p`` weights.
    X : 2-D array-like
        The ``(n, p)`` design matrix.

    Returns
    -------
    numpy.ndarray
        The ``(p, p)`` matrix ``-sum_i mu_i x_i x_i^T``.

    Raises
    ------
    ValueError
        If the shapes do not match.
    """
    Xm = _matrix(X)
    mu = mean(w, Xm)
    H = -(Xm.T * mu) @ Xm                  # column i of X^T scaled by mu_i: X^T diag(mu), never forming diag(mu)
    return (H + H.T) / 2


def newton_direction(w, X, y):
    """Return Newton's direction ``delta = (X^T W X)^{-1} X^T (y - mu)``, ``W = diag(mu)``, of shape ``(p,)``.

    Eq. (3.4), computed as Eq. (3.6). It solves ``H(w) delta = -grad l(w)`` without forming ``X^T W X``: ``delta``
    minimizes
    ``sum_i mu_i (r_i - x_i . delta)^2`` with the working residuals ``r_i = (y_i - mu_i) / mu_i``, i.e. it is the
    least squares solution of ``sqrt(mu) * r`` on the rows of ``X`` scaled by ``sqrt(mu)``, computed by
    ``mymath.orthogonal.least_squares_qr``. From ``w = 0`` (all ``mu_i = 1``) it is the least squares fit of
    ``y - 1`` on ``X`` (Eq. (3.8)).

    Parameters
    ----------
    w : 1-D array-like
        The ``p`` weights.
    X : 2-D array-like
        The ``(n, p)`` design matrix, with linearly independent columns.
    y : 1-D array-like
        The ``n`` counts.

    Returns
    -------
    numpy.ndarray
        The ``p`` coordinates of ``delta``; ``w + delta`` is the next iterate of the pure Newton method (the weighted
        least squares coefficients of the working response ``X w + (y - mu) / mu``).

    Raises
    ------
    ValueError
        If the shapes do not match, if a fitted mean overflows, or if the rows of ``X`` scaled by ``sqrt(mu)`` are
        linearly dependent (raised by ``least_squares_qr``).
    """
    Xm = _matrix(X)
    yv = np.asarray(y, dtype=float)
    if yv.shape != (Xm.shape[0],):
        raise ValueError(f"y must be a 1-D array of length {Xm.shape[0]}, got the shape {yv.shape}")
    mu = mean(w, Xm)
    if not np.all(np.isfinite(mu)):
        raise ValueError("a fitted mean exp(x_i . w) overflows: start from a smaller w")
    root = np.sqrt(mu)
    return orthogonal.least_squares_qr(root[:, None] * Xm, (yv - mu) / root)


def fit(X, y, w0=None, tol=1e-10, max_iter=100, max_halvings=30):
    """Maximize the Poisson log-likelihood by Newton's method, with step halving, and return a :class:`PoissonFit`.

    The iteration of Eq. (3.5): ``w_{k+1} = w_k + t_k delta_k``. Each iteration computes Newton's direction
    ``delta`` (:func:`newton_direction`). If ``max_j |delta_j| <= tol * (1 + max_j |w_j|)``, the step ``w + delta``
    is taken and the method stops: Newton's convergence is quadratic, so the returned ``w`` is then exact to
    rounding. Otherwise the step ``w + t delta`` is taken with ``t = 1``, or ``1/2``, ``1/4``, ... (at most
    ``max_halvings`` halvings), the first ``t`` for which the log-likelihood does not decrease (up to
    ``1e-12 * (1 + |l(w)|)``, for rounding). Far from the maximum, a full step can decrease ``l``; ``delta`` is always
    an ascent direction (``grad l . delta > 0`` while ``grad l != 0``, because ``X^T W X`` is positive definite), so
    some ``t`` works.

    Before each step, ``svd_pca.condition_number(sqrt(mu) * X)`` is checked: it becomes infinite when weights
    ``mu_i`` collapse to 0, which is what happens when the maximum does not exist.

    Parameters
    ----------
    X : 2-D array-like
        The ``(n, p)`` design matrix, with linearly independent columns (see :func:`check_data`).
    y : 1-D array-like
        The ``n`` counts, integers ``>= 0``.
    w0 : 1-D array-like, optional
        The start, of shape ``(p,)``; default ``0`` (all fitted means equal to 1).
    tol : float, default 1e-10
        The relative size of the last Newton step, ``> 0``.
    max_iter : int, default 100
        The maximum number of Newton steps, ``>= 1``.
    max_halvings : int, default 30
        The maximum number of halvings of one step, ``>= 0``.

    Returns
    -------
    PoissonFit
        The weights ``w``, the number of steps, the iterates, their log-likelihoods, the fractions ``t`` taken and
        ``max_j |grad l(w)_j|``.

    Raises
    ------
    ValueError
        If the data are not valid (:func:`check_data`), or if ``w0``, ``tol``, ``max_iter`` or ``max_halvings`` is not.
    NoMaximumError
        If the maximum does not exist: the weights ``sqrt(mu_i)`` of counts ``y_i = 0`` have collapsed (the
        condition number of ``sqrt(mu) * X`` is infinite), or the method has not converged after ``max_iter`` steps
        while fitted means of counts ``y_i = 0`` went below ``COLLAPSED_MEAN``. The error carries the iterates.
    RuntimeError
        If the method has not converged after ``max_iter`` steps for another reason, or if no halving of a step
        stops the log-likelihood from decreasing.
    """
    Xm, yv = check_data(X, y)
    n, p = Xm.shape
    if not (isinstance(tol, (int, float)) and tol > 0):
        raise ValueError(f"tol must be a number > 0, got {tol!r}")
    for name, value, low in (("max_iter", max_iter, 1), ("max_halvings", max_halvings, 0)):
        if isinstance(value, bool) or not isinstance(value, (int, np.integer)) or value < low:
            raise ValueError(f"{name} must be an integer >= {low}, got {value!r}")
    w = np.zeros(p) if w0 is None else _weights_vector(w0, p)
    current = log_likelihood(w, Xm, yv)
    if current == -math.inf:
        raise ValueError("a fitted mean exp(x_i . w0) overflows: start from a smaller w0")
    history, values, steps = [w.copy()], [current], []
    for _ in range(max_iter):
        mu = mean(w, Xm)
        if svd_pca.condition_number(np.sqrt(mu)[:, None] * Xm) == math.inf:
            raise NoMaximumError(_no_maximum_message(mu, yv, len(steps), "the rows of sqrt(mu) * X are numerically "
                                                     "rank deficient"), history, values)
        delta = newton_direction(w, Xm, yv)
        if np.max(np.abs(delta)) <= tol * (1.0 + np.max(np.abs(w))):
            w = w + delta
            history.append(w.copy())
            values.append(log_likelihood(w, Xm, yv))
            steps.append(1.0)
            return PoissonFit(w, len(steps), history, values, steps, float(np.max(np.abs(gradient(w, Xm, yv)))))
        t = 1.0
        for _ in range(max_halvings + 1):
            candidate = w + t * delta
            value = log_likelihood(candidate, Xm, yv)
            if value >= current - 1e-12 * (1.0 + abs(current)):
                break
            t /= 2
        else:
            raise RuntimeError(f"no step w + t * delta with t >= 2**-{max_halvings} stops the log-likelihood from "
                               f"decreasing (at l = {current:.6g}): check the data")
        w, current = candidate, value
        history.append(w.copy())
        values.append(current)
        steps.append(t)
    mu = mean(w, Xm)
    if np.any((yv == 0) & (mu < COLLAPSED_MEAN)):
        raise NoMaximumError(_no_maximum_message(mu, yv, max_iter, "the method has not converged"), history, values)
    raise RuntimeError(f"Newton's method has not converged after {max_iter} steps (last step "
                       f"{np.max(np.abs(delta)):.2e}): raise max_iter or tol")


def _no_maximum_message(mu, y, steps: int, symptom: str) -> str:
    """The message of NoMaximumError: the symptom, and the smallest fitted mean of a count 0, after ``steps`` steps."""
    zeros = y == 0
    smallest = float(np.min(mu[zeros])) if np.any(zeros) else float(np.min(mu))
    return (f"expected a maximum of the log-likelihood, but it does not exist (or its fitted means are too close to 0 "
            f"for float64): after {steps} Newton steps, {symptom}, and the smallest fitted mean of a count y_i = 0 is "
            f"{smallest:.1e}. Look for a direction d with X d <= 0 and (X d)_i = 0 wherever y_i > 0: all the counts "
            "0, or a group of rows whose counts are all 0")


def standard_errors(w, X):
    """Return the standard errors ``sqrt(diag((X^T W X)^{-1}))`` of the weights, shape ``(p,)`` (Eq. (3.9)).

    ``X^T W X = -H(w)`` is the Fisher information of the model (the Hessian does not depend on ``y``); at the maximum
    likelihood weights, ``sqrt`` of the diagonal of its inverse estimates the standard deviation of each weight (an
    asymptotic result, for large ``n``). With ``X^T W X = L L^T`` (``mymath.eigen.cholesky``),
    ``(X^T W X)^{-1} = L^{-T} L^{-1}``, so its diagonal entry ``j`` is the squared norm of column ``j`` of
    ``L^{-1}`` (``W = diag(mu)``).

    Parameters
    ----------
    w : 1-D array-like
        The ``p`` weights (the maximum likelihood weights, for the usual reading).
    X : 2-D array-like
        The ``(n, p)`` design matrix.

    Returns
    -------
    numpy.ndarray
        The ``p`` standard errors, positive.

    Raises
    ------
    ValueError
        If the shapes do not match, or if ``X^T W X`` is not positive definite (raised by ``cholesky``).
    """
    information = -hessian(w, X)
    L = eigen.cholesky(information)
    inverse = np.linalg.solve(L, np.eye(L.shape[0]))     # L^{-1}: the solution M of L M = I
    return np.sqrt(np.sum(inverse ** 2, axis=0))


def intercept_only(y, w0=0.0, tol=1e-12, max_iter=100):
    """Fit the model without features (``X`` a column of ones) by ``mymath.approx.newton``: ``w* = ln(mean(y))``.

    Eq. (3.10).
    The derivative of ``l(w) / n = mean(y) w - exp(w) - const`` is ``f(w) = mean(y) - exp(w)``, and Newton's method on
    ``f(w) = 0`` is Newton's method for the maximum: ``w <- w + mean(y) exp(-w) - 1``. From ``w0 = 0`` the first
    iterate is ``mean(y) - 1``, which is ``>= ln(mean(y))``: when ``mean(y) > 1`` the first step goes past the
    maximum, and the iterates then decrease to it.

    Parameters
    ----------
    y : 1-D array-like
        The counts, integers ``>= 0``, not all 0.
    w0 : float, default 0.0
        The start.
    tol, max_iter
        Passed to ``approx.newton`` (stop when two iterates differ by less than ``tol``).

    Returns
    -------
    float
        The maximum likelihood intercept, ``ln(mean(y))`` up to rounding.

    Raises
    ------
    ValueError
        If ``y`` is not a non-empty 1-D array of integer counts ``>= 0``.
    NoMaximumError
        If all the counts are 0: ``l(w) = -n exp(w)`` increases without end as ``w -> -inf``.
    OverflowError
        If an iterate overflows ``math.exp`` (from ``w0 = 0``, when ``mean(y) - 1 > 709``: start closer).
    """
    yv = np.array(y, dtype=float)
    if yv.ndim != 1 or yv.size == 0:
        raise ValueError(f"y must be a non-empty 1-D array of counts, got the shape {yv.shape}")
    check_data(np.ones((yv.size, 1)), yv)
    if not np.any(yv):
        raise NoMaximumError("all the counts are 0: l(w) = -n exp(w) increases as w -> -inf, there is no maximum")
    average = float(np.mean(yv))
    return approx.newton(lambda v: average - math.exp(v), lambda v: -math.exp(v), float(w0), tol=tol,
                         max_iter=max_iter)


def critical_learning_rate(w, X):
    """Return ``2 / lambda_max(X^T W X)``, the critical learning rate of a gradient ascent near ``w`` (Eq. (3.12)).

    Near the maximum, a gradient ascent ``w <- w + eta grad l(w)`` behaves like Richardson's iteration on
    ``X^T W X`` (computed at the maximum): it converges for ``0 < eta < 2 / lambda_max`` and, with
    ``eta = 1 / lambda_max``, multiplies the error by about ``1 - 1 / kappa`` per step, ``kappa`` the condition number
    of ``X^T W X``. Computed by ``mymath.iterative.critical_step_size``.

    Parameters
    ----------
    w : 1-D array-like
        The ``p`` weights where the curvature is read.
    X : 2-D array-like
        The ``(n, p)`` design matrix.

    Returns
    -------
    float
        ``2 / lambda_max``.

    Raises
    ------
    ValueError
        If the shapes do not match, or if ``X^T W X`` is not positive definite (raised by ``critical_step_size``).
    """
    return iterative.critical_step_size(-hessian(w, X))


def gradient_ascent(X, y, eta, n_steps, w0=None):
    """Return the iterates of the gradient ascent ``w <- w + eta X^T (y - mu)`` (Eq. (3.11)), one per row.

    It is the comparison of the notebook's experiment, not a fitting method: with a fixed learning rate, it converges
    only linearly, and it diverges (``inf`` or ``nan`` rows, returned as they are) when ``eta`` is too large.

    Parameters
    ----------
    X : 2-D array-like
        The ``(n, p)`` design matrix.
    y : 1-D array-like
        The ``n`` counts.
    eta : float
        The learning rate, ``> 0``.
    n_steps : int
        The number of steps, ``>= 0``.
    w0 : 1-D array-like, optional
        The start, default ``0``.

    Returns
    -------
    numpy.ndarray
        Shape ``(n_steps + 1, p)``: row ``k`` is ``w_k``, row 0 is the start.

    Raises
    ------
    ValueError
        If the data are not valid (:func:`check_data`), or if ``eta``, ``n_steps`` or ``w0`` is not.
    """
    Xm, yv = check_data(X, y)
    p = Xm.shape[1]
    if not (isinstance(eta, (int, float)) and eta > 0):
        raise ValueError(f"eta must be a number > 0, got {eta!r}")
    if isinstance(n_steps, bool) or not isinstance(n_steps, (int, np.integer)) or n_steps < 0:
        raise ValueError(f"n_steps must be an integer >= 0, got {n_steps!r}")
    iterates = np.empty((n_steps + 1, p))
    iterates[0] = np.zeros(p) if w0 is None else _weights_vector(w0, p)
    with np.errstate(over="ignore", invalid="ignore"):
        for k in range(n_steps):
            w = iterates[k]
            iterates[k + 1] = w + eta * (Xm.T @ (yv - np.exp(Xm @ w)))
    return iterates
