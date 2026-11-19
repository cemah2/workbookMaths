"""Pointwise mutual information and two building blocks of embeddings: the PMI table of a joint law, the logit of a
population estimated on a case-control sample, and the removal of a direction (chapter MB2).

Reference implementation (solutions/mymath_ref).
NumPy and the module ``math`` are allowed, but no SciPy (``scipy.special.logit``, ``scipy.special.xlogy``,
``scipy.optimize``…) and no scikit-learn (``sklearn.metrics.mutual_info_score``, ``LogisticRegression``…): the tests
compare your results with them. Logarithms are natural logarithms: a PMI or a logit is in nats. A joint law is a 2-D
table, as in ``conditional.py`` (M03) and ``info.py`` (M06): the rows are the values of a variable X, the columns
those of a variable Y, and the non-negative entries sum to 1 (up to 1e-9). Never modify the arrays you receive.
Tables and vectors are returned as ``numpy.ndarray`` of floats, a single number as a Python ``float``.
"""

import math

import numpy as np

SUM_TOLERANCE = 1e-9      # a joint law sums to 1 up to this


def _holds_booleans(values):
    """Whether values is a bool, a NumPy bool, or an array (or nested lists) of booleans."""
    if isinstance(values, (bool, np.bool_)):
        return True
    try:
        return np.asarray(values).dtype.kind == "b"
    except (TypeError, ValueError):             # a ragged list: not booleans (refused later anyway)
        return False


def _float_array(values, what):
    """values as a NEW float array (never a view of what was received), or ValueError; booleans are refused."""
    if _holds_booleans(values):
        raise ValueError(f"{what} must hold numbers, not booleans, got {values!r}")
    try:
        return np.array(values, dtype=float)
    except (TypeError, ValueError):
        raise ValueError(f"{what} must be an array of numbers, got {values!r}") from None


def _rate(value, what):
    """A selection rate: one real number in ]0, 1] (not a bool, not nan). Returns it as a Python float."""
    if _holds_booleans(value) or isinstance(value, (str, bytes)) or np.ndim(value) != 0:
        raise ValueError(f"{what} must be a number in ]0, 1] (not a bool), got {value!r}")
    try:
        rate = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{what} must be a number in ]0, 1], got {value!r}") from None
    if not 0.0 < rate <= 1.0:                   # also refuses nan, for which every comparison is False
        raise ValueError(f"{what} must be in ]0, 1], got {value!r}")
    return rate


def _counts(values, what):
    """Numbers of examples: a number or an array of finite numbers >= 0 (no bool). Returns a new float array."""
    counts = _float_array(values, what)
    if not np.all(np.isfinite(counts)):
        raise ValueError(f"{what} must hold finite numbers only (no nan, no inf), got {values!r}")
    if np.any(counts < 0):
        raise ValueError(f"{what} must hold numbers >= 0 only, got {values!r}")
    return counts


def pmi(joint):
    """Return the table of the pointwise mutual information ``PMI(x, y) = ln(p(x, y) / (p(x) p(y)))`` of a joint law.

    ``p(x)`` is the sum of row ``x`` and ``p(y)`` the sum of column ``y`` (the marginals, M03). The PMI of a cell is
    positive when ``x`` and ``y`` occur together more often than if X and Y were independent, 0 when exactly as
    often, negative when less often. It is also ``ln(P(Y = y | X = x) / P(Y = y))``: the logarithm of the *lift* of
    the rule "x ⇒ y". A cell of probability 0 gets ``-inf``, without a warning, even in a row or a column of
    probability 0. Nothing else is done to the logarithms: no clipping, no smoothing of the marginals.

    The mutual information of M06, in nats (``mutual_information(joint, base=math.e)``; M06 defaults to bits), is the
    mean of the PMI under the joint law, ``I(X ; Y) = Σ p(x, y) PMI(x, y)``, the sum running over the cells where
    ``p(x, y) > 0``.

    Parameters
    ----------
    joint : 2-D array-like
        A joint law of shape ``(m, n)``, ``m ≥ 1`` and ``n ≥ 1``: finite entries ``≥ 0`` summing to 1 (up to 1e-9).

    Returns
    -------
    numpy.ndarray
        The ``(m, n)`` table of the PMI, of floats: finite where ``p(x, y) > 0``, ``-inf`` elsewhere. Transposing the
        joint law transposes the table.

    Raises
    ------
    ValueError
        If ``joint`` is not 2-D, is empty, holds booleans, has a negative or non-finite entry, or does not sum to 1
        (up to 1e-9).

    Examples
    --------
    >>> np.round(pmi([[0.4, 0.1], [0.2, 0.3]]), 4)      # p(x) = (0.5, 0.5), p(y) = (0.6, 0.4)
    array([[ 0.2877, -0.6931],
           [-0.4055,  0.4055]])
    >>> np.round(pmi([[0.5, 0.0], [0.1, 0.4]]), 4)      # a cell that never occurs
    array([[ 0.5108,    -inf],
           [-1.0986,  0.6931]])
    """
    table = _float_array(joint, "joint")
    if table.ndim != 2:
        raise ValueError(f"joint must be a 2-D table, got {table.ndim} dimension(s) (shape {table.shape})")
    if table.size == 0:
        raise ValueError(f"joint must not be empty, got shape {table.shape}")
    if not np.all(np.isfinite(table)):
        raise ValueError("joint must hold finite numbers only (no nan, no inf)")
    if np.any(table < 0):
        raise ValueError(f"joint must hold probabilities >= 0 only, got {table.min()!r}")
    total = float(np.sum(table))
    if not abs(total - 1.0) <= SUM_TOLERANCE:
        raise ValueError(f"joint must sum to 1 (up to {SUM_TOLERANCE}), got a sum of {total!r}")
    p_x = table.sum(axis=1)                     # the sums of the rows: the law of X
    p_y = table.sum(axis=0)                     # the sums of the columns: the law of Y
    result = np.full(table.shape, -np.inf)      # -inf on the cells of probability 0, without np.log(0)
    rows, columns = np.nonzero(table > 0)       # p(x) > 0 and p(y) > 0 on these cells: no 0 / 0
    result[rows, columns] = np.log(table[rows, columns]) - np.log(p_x[rows]) - np.log(p_y[columns])
    return result


def case_control_logit(n_positive, n_negative, keep_positive=1.0, keep_negative=1.0):
    """Return the logit of a population estimated on a case-control sample: ``ln(n₁ / n₀) - ln(s₁ / s₀)``.

    In a *case-control* sample, each positive example of the population (label 1) is kept with probability
    ``s₁ = keep_positive`` and each negative one (label 0) with probability ``s₀ = keep_negative``, independently of
    everything else; ``n₁ = n_positive`` and ``n₀ = n_negative`` are the numbers of examples kept. The logit of the
    observed proportion ``n₁ / (n₁ + n₀)`` is ``ln(n₁ / n₀)`` (M13a, R6). By Bayes' formula (M04), the odds of a
    positive in the sample are those of the population multiplied by ``s₁ / s₀``: the logit of the population is the
    observed one minus ``ln(s₁ / s₀)``. With both rates equal to 1 (the default), nothing was dropped and the result
    is the logit of the observed proportion.

    When ``n₁ > 0`` and ``n₀ = 0``, the result is ``+inf``; when ``n₁ = 0`` and ``n₀ > 0``, it is ``-inf``. When
    ``n₁ = n₀ = 0``, nothing was observed: an error.

    Parameters
    ----------
    n_positive, n_negative : float or array-like
        The numbers of positive and negative examples in the sample: finite numbers ``≥ 0``. Two arrays are combined
        cell by cell, with NumPy broadcasting (M20): one logit per cell.
    keep_positive, keep_negative : float, default 1.0
        The selection rates ``s₁`` and ``s₀``, in ``]0, 1]``.

    Returns
    -------
    float or numpy.ndarray
        The logit: a Python ``float`` when both numbers of examples are numbers, otherwise an array of floats of the
        broadcast shape; ``+inf`` or ``-inf`` in the two cases above.

    Raises
    ------
    ValueError
        If a number of examples is negative, ``nan``, infinite or a ``bool`` (or an array of booleans), if both are 0
        for some cell, if the two shapes do not broadcast, or if a rate is not in ``]0, 1]`` (``nan`` and a ``bool``
        are refused).

    Examples
    --------
    >>> round(case_control_logit(45, 10), 4)                        # everything kept: ln 4.5
    1.5041
    >>> round(case_control_logit(45, 10, keep_negative=0.25), 4)    # one negative in 4 kept: ln(4.5 / 4)
    0.1178
    >>> case_control_logit([2, 0, 5], [2, 7, 0])
    array([  0., -inf,  inf])
    """
    s1 = _rate(keep_positive, "keep_positive")
    s0 = _rate(keep_negative, "keep_negative")
    positives = _counts(n_positive, "n_positive")
    negatives = _counts(n_negative, "n_negative")
    try:
        n1, n0 = np.broadcast_arrays(positives, negatives)
    except ValueError:
        raise ValueError(f"the shapes {positives.shape} and {negatives.shape} of the numbers of examples do not "
                         f"broadcast") from None
    if np.any((n1 == 0) & (n0 == 0)):
        raise ValueError("n_positive and n_negative are both 0 in some cell: nothing was observed there")
    logit = np.empty(n1.shape)
    both = (n1 > 0) & (n0 > 0)
    logit[both] = (np.log(n1[both]) - np.log(n0[both])) - (math.log(s1) - math.log(s0))
    logit[(n1 > 0) & (n0 == 0)] = np.inf        # only positives: odds +inf, whatever the rates
    logit[(n1 == 0) & (n0 > 0)] = -np.inf       # only negatives: odds 0
    if logit.ndim == 0:
        return float(logit)
    return logit


def remove_direction(X, u):
    """Return ``X`` without its component along the direction ``u``: each row ``x`` becomes ``x - (x·u / u·u) u``.

    It is the orthogonal projection on the complement of the line directed by ``u`` (M12b): ``x`` minus its
    projection on the line (``project_onto_line``, M07), for every row at once. Each row of the result is orthogonal
    to ``u``; removing the same direction twice changes nothing; a row parallel to ``u`` becomes 0. The distance
    between two rows splits as in Pythagoras' theorem: with ``r_x`` and ``r_y`` the two rows of the result,
    ``‖x - y‖² = ‖r_x - r_y‖² + ((x - y)·u)² / (u·u)``: only the part of the difference along ``u`` disappears.
    ``u`` need not have norm 1, and ``c u`` gives the same result for every ``c ≠ 0``.

    Parameters
    ----------
    X : 1-D or 2-D array-like
        One vector of length ``d``, or ``n`` vectors, the rows of an ``(n, d)`` array (``n ≥ 1``, ``d ≥ 1``).
    u : 1-D array-like
        A non-zero vector of length ``d``.

    Returns
    -------
    numpy.ndarray
        An array of floats of the shape of ``X``.

    Raises
    ------
    ValueError
        If ``X`` is not 1-D or 2-D or is empty, if ``u`` is not 1-D or does not have the length of the rows of
        ``X``, if ``u`` is zero (``u·u = 0``), or if an entry is not finite or is a boolean.

    Examples
    --------
    >>> remove_direction([3.0, 1.0], [1.0, 1.0])
    array([ 1., -1.])
    >>> remove_direction([[2, 0, 1], [1, 1, 1]], [0, 0, 5])     # the third coordinate is removed
    array([[2., 0., 0.],
           [1., 1., 0.]])
    """
    points = _float_array(X, "X")
    direction = _float_array(u, "u")
    if points.ndim not in (1, 2) or points.size == 0:
        raise ValueError(f"X must be a non-empty 1-D or 2-D array, got shape {points.shape}")
    if direction.ndim != 1 or direction.shape[0] != points.shape[-1]:
        raise ValueError(f"u must be a 1-D vector of length d = {points.shape[-1]} (the length of the rows of X), got "
                         f"shape {direction.shape}")
    if not (np.all(np.isfinite(points)) and np.all(np.isfinite(direction))):
        raise ValueError("X and u must hold finite numbers only (no nan, no inf)")
    squared_norm = float(direction @ direction)
    if squared_norm == 0:
        raise ValueError(f"u must not be zero (u·u = 0), got {u!r}")
    coefficients = (points @ direction) / squared_norm     # x·u / u·u for each row (a number for a 1-D X)
    return points - np.multiply.outer(coefficients, direction)
