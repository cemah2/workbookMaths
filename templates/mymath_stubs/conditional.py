"""Joint, marginal and conditional probabilities of a table, independence, AUC by pairs (chapter M03).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m03_conditional.py``.
NumPy is allowed; scikit-learn is not (the tests compare with it). A joint law is a 2-D table (list of lists or
array): the rows are the values of a variable X, the columns those of a variable Y, and ``joint[i][j]`` is
``P(X = x_i, Y = y_j)``. A valid joint law has non-negative entries summing to 1 (up to 1e-9). Tables are returned as
NumPy arrays of floats, numbers as Python ``float`` or ``bool``.
"""


def joint_from_counts(counts):
    """Turn a table of counts (a contingency table) into a joint law.

    Parameters
    ----------
    counts : 2-D array-like
        Non-negative counts, at least one of them positive.

    Returns
    -------
    numpy.ndarray
        Same shape, dtype float: each count divided by the total.

    Raises
    ------
    ValueError
        If the table is not 2-D, has a negative count, or only zeros.

    Examples
    --------
    >>> joint_from_counts([[1, 3], [2, 4]])
    array([[0.1, 0.3],
           [0.2, 0.4]])
    """
    # TODO: convert with np.asarray(counts, dtype=float), check, then divide by the total.
    raise NotImplementedError("joint_from_counts() is not implemented yet")


def marginal(joint, axis):
    """Return a marginal law of a joint law, with the convention of ``numpy.sum(joint, axis=axis)``.

    Parameters
    ----------
    joint : 2-D array-like
        A valid joint law.
    axis : {0, 1}
        ``axis=0`` adds down each column and gives the law of Y (one probability per column); ``axis=1`` adds along
        each row and gives the law of X (one probability per row).

    Returns
    -------
    numpy.ndarray
        1-D, dtype float, summing to 1.

    Raises
    ------
    ValueError
        If ``joint`` is not a valid joint law or ``axis`` is not 0 or 1.

    Examples
    --------
    >>> marginal([[0.1, 0.3], [0.2, 0.4]], axis=0)
    array([0.3, 0.7])
    """
    # TODO: check the table (non-negative, sums to 1), then sum along the axis.
    raise NotImplementedError("marginal() is not implemented yet")


def conditional(joint, given_row=None, given_column=None):
    """Return a conditional law read in a joint law: Y given ``X = x_i``, or X given ``Y = y_j``.

    Parameters
    ----------
    joint : 2-D array-like
        A valid joint law.
    given_row : int, optional
        Index ``i`` of the row: the result is the law of Y given ``X = x_i``, ``joint[i] / P(X = x_i)``.
    given_column : int, optional
        Index ``j`` of the column: the result is the law of X given ``Y = y_j``. Give exactly one of the two.

    Returns
    -------
    numpy.ndarray
        1-D, dtype float, summing to 1.

    Raises
    ------
    ValueError
        If ``joint`` is not a valid joint law, if both or neither index is given, if an index is out of range, or
        if the conditioning event has probability 0.

    Examples
    --------
    >>> conditional([[0.1, 0.3], [0.2, 0.4]], given_row=0)
    array([0.25, 0.75])
    """
    # TODO: take the row (or the column) and divide it by its sum.
    raise NotImplementedError("conditional() is not implemented yet")


def are_independent(joint, tol=1e-9):
    """Tell whether the two variables of a joint law are independent.

    X and Y are independent when ``P(X = x_i, Y = y_j) = P(X = x_i) P(Y = y_j)`` for every cell.

    Parameters
    ----------
    joint : 2-D array-like
        A valid joint law.
    tol : float, default 1e-9
        Each cell may differ from the product of its marginals by at most ``tol``.

    Returns
    -------
    bool
        A Python ``bool``.

    Raises
    ------
    ValueError
        If ``joint`` is not a valid joint law.

    Examples
    --------
    >>> are_independent([[0.06, 0.14], [0.24, 0.56]])
    True
    >>> are_independent([[0.1, 0.3], [0.2, 0.4]])
    False
    """
    # TODO: the two marginals, their outer product (np.outer), then compare cell by cell.
    raise NotImplementedError("are_independent() is not implemented yet")


def auc_by_pairs(scores_pos, scores_neg):
    """Return the AUC as the proportion of (positive, negative) pairs that the scores rank correctly.

    A pair counts 1 when the positive example has the higher score, 1/2 for a tie, 0 otherwise.

    Parameters
    ----------
    scores_pos : sequence of float
        Scores of the positive examples, at least one.
    scores_neg : sequence of float
        Scores of the negative examples, at least one.

    Returns
    -------
    float
        Between 0 and 1.

    Raises
    ------
    ValueError
        If one of the two lists is empty.

    Examples
    --------
    >>> auc_by_pairs([0.9, 0.4], [0.3, 0.4])
    0.875
    """
    # TODO: two nested loops over the pairs are fine (NumPy broadcasting is faster).
    raise NotImplementedError("auc_by_pairs() is not implemented yet")
