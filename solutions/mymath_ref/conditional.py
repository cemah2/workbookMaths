"""Joint, marginal and conditional probabilities of a table, independence, AUC by pairs (chapter M03).

Reference implementation (solutions/mymath_ref).
NumPy is allowed; scikit-learn is not (the tests compare with it). A joint law is a 2-D table (list of lists or
array): the rows are the values of a variable X, the columns those of a variable Y, and ``joint[i][j]`` is
``P(X = x_i, Y = y_j)``. A valid joint law has non-negative entries summing to 1 (up to 1e-9). Tables are returned as
NumPy arrays of floats, numbers as Python ``float`` or ``bool``.
"""

import numpy as np


def _joint(joint):
    """The joint law as a 2-D array of floats, after checking that it is one (ValueError otherwise)."""
    table = np.asarray(joint, dtype=float)
    if table.ndim != 2 or table.size == 0:
        raise ValueError(f"a joint law is a non-empty 2-D table, got shape {table.shape}")
    if not np.all(table >= 0):                     # also refuses nan, for which every comparison is False
        raise ValueError("a joint law has non-negative entries (no negative entry, no nan)")
    if abs(table.sum() - 1) > 1e-9:
        raise ValueError(f"a joint law sums to 1, this one sums to {table.sum()}")
    return table


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
    table = np.asarray(counts, dtype=float)
    if table.ndim != 2:
        raise ValueError(f"a contingency table is 2-D, got {table.ndim} dimension(s)")
    if not np.all(table >= 0):                     # also refuses nan
        raise ValueError("a count is a non-negative number (no negative count, no nan)")
    total = table.sum()
    if total <= 0:
        raise ValueError("the table has no positive count")
    return table / total


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
    table = _joint(joint)
    if axis not in (0, 1) or isinstance(axis, bool):
        raise ValueError(f"axis is 0 or 1, got {axis!r}")
    return table.sum(axis=axis)


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
    table = _joint(joint)
    if (given_row is None) == (given_column is None):
        raise ValueError("give exactly one of given_row and given_column")
    if given_row is not None:
        if not 0 <= given_row < table.shape[0]:
            raise ValueError(f"row index {given_row} out of range")
        line = table[given_row]
    else:
        if not 0 <= given_column < table.shape[1]:
            raise ValueError(f"column index {given_column} out of range")
        line = table[:, given_column]
    total = line.sum()
    if total <= 0:
        raise ValueError("the conditioning event has probability 0")
    return line / total


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
    table = _joint(joint)
    product = np.outer(table.sum(axis=1), table.sum(axis=0))
    return bool(np.all(np.abs(table - product) <= tol))


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
    pos = np.asarray(scores_pos, dtype=float).ravel()
    neg = np.asarray(scores_neg, dtype=float).ravel()
    if pos.size == 0 or neg.size == 0:
        raise ValueError("each list needs at least one score")
    diff = pos[:, None] - neg[None, :]
    return float((np.sum(diff > 0) + 0.5 * np.sum(diff == 0)) / diff.size)
