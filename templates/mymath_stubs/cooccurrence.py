"""Pointwise mutual information and two building blocks of embeddings: the PMI table of a joint law, the logit of a
population estimated on a case-control sample, and the removal of a direction (chapter MB2).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_mb2_cooccurrence.py``.
NumPy and the module ``math`` are allowed, but no SciPy (``scipy.special.logit``, ``scipy.special.xlogy``,
``scipy.optimize``…) and no scikit-learn (``sklearn.metrics.mutual_info_score``, ``LogisticRegression``…): the tests
compare your results with them. Logarithms are natural logarithms: a PMI or a logit is in nats. A joint law is a 2-D
table, as in ``conditional.py`` (M03) and ``info.py`` (M06): the rows are the values of a variable X, the columns
those of a variable Y, and the non-negative entries sum to 1 (up to 1e-9). Never modify the arrays you receive.
Tables and vectors are returned as ``numpy.ndarray`` of floats, a single number as a Python ``float``.
"""


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
    # TODO: check the table; the marginals p(x) (sums of the rows) and p(y) (sums of the columns), as a column and a
    #  row so that they broadcast (M20); then the logarithm of the ratio on the positive cells only, -inf elsewhere
    #  (np.log of 0 would warn: start from a table filled with -np.inf).
    raise NotImplementedError("pmi() is not implemented yet")


def case_control_logit(n_positive, n_negative, keep_positive=1.0, keep_negative=1.0):
    """Return the logit of a population estimated on a case-control sample: ``ln(n₊ / n₋) - ln(s₊ / s₋)``.

    In a *case-control* sample, each positive example of the population (label 1) is kept with probability
    ``s₊ = keep_positive`` and each negative one (label 0) with probability ``s₋ = keep_negative``, independently of
    everything else; ``n₊ = n_positive`` and ``n₋ = n_negative`` are the numbers of examples kept. The logit of the
    observed proportion ``n₊ / (n₊ + n₋)`` is ``ln(n₊ / n₋)`` (M13a, R6). By Bayes' formula (M04), the odds of a
    positive in the sample are those of the population multiplied by ``s₊ / s₋``: the logit of the population is the
    observed one minus ``ln(s₊ / s₋)``. With both rates equal to 1 (the default), nothing was dropped and the result
    is the logit of the observed proportion.

    When ``n₊ > 0`` and ``n₋ = 0``, the result is ``+inf``; when ``n₊ = 0`` and ``n₋ > 0``, it is ``-inf``. When
    ``n₊ = n₋ = 0``, nothing was observed: an error.

    Parameters
    ----------
    n_positive, n_negative : float or array-like
        The numbers of positive and negative examples in the sample: finite numbers ``≥ 0``. Two arrays are combined
        cell by cell, with NumPy broadcasting (M20): one logit per cell.
    keep_positive, keep_negative : float, default 1.0
        The selection rates ``s₊`` and ``s₋``, in ``]0, 1]``.

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
    # TODO: check the two rates, then the numbers of examples (refuse booleans before converting to floats), broadcast
    #  them (np.broadcast_arrays); three cases cell by cell: both positive (the logarithm of the ratio, minus that of
    #  the rates), only n₊ > 0, only n₋ > 0. Return a float when the broadcast shape is ().
    raise NotImplementedError("case_control_logit() is not implemented yet")


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
    # TODO: check X and u; the coefficients x·u / u·u of the rows (one matrix-vector product), then subtract
    #  coefficient × u from each row (an outer product, or broadcasting). A 1-D X gives a 1-D result.
    raise NotImplementedError("remove_direction() is not implemented yet")
