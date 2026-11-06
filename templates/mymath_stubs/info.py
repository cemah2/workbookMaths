"""Information of two variables: joint and conditional entropies, mutual information, Kraft, Jensen (chapter M06).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m06_info.py``.
Do not use ``scipy.stats.entropy`` nor scikit-learn: the tests compare your results with them. A joint law is a
2-D table (list of lists or array) as in ``conditional.py``: rows are the values of X, columns those of Y,
non-negative entries summing to 1 (up to 1e-9). In every sum, ``0 log 0`` counts as 0. ``base=2`` gives bits,
``base=math.e`` nats. Every number returned is a Python ``float`` or ``bool``.
"""


def joint_entropy(joint, base=2):
    """Return the joint entropy ``H(X, Y) = -Σ p(x, y) log p(x, y)`` of a joint law.

    Parameters
    ----------
    joint : 2-D array-like
        A valid joint law.
    base : float, default 2
        Base of the logarithm, greater than 1.

    Returns
    -------
    float
        Non-negative.

    Raises
    ------
    ValueError
        If ``joint`` is not a valid joint law or ``base <= 1``.

    Examples
    --------
    >>> joint_entropy([[0.25, 0.25], [0.25, 0.25]])
    2.0
    """
    # TODO: keep only the positive cells (0 log 0 = 0), then the sum.
    raise NotImplementedError("joint_entropy() is not implemented yet")


def conditional_entropy(joint, base=2):
    """Return ``H(Y | X)``, the entropy of the column variable Y once the row variable X is known.

    ``H(Y | X) = -Σ p(x, y) log p(y | x) = H(X, Y) - H(X)``.

    Parameters
    ----------
    joint : 2-D array-like
        A valid joint law (rows: X, columns: Y).
    base : float, default 2
        Greater than 1.

    Returns
    -------
    float
        Non-negative.

    Raises
    ------
    ValueError
        If ``joint`` is not a valid joint law or ``base <= 1``.

    Examples
    --------
    >>> conditional_entropy([[0.25, 0.25], [0.5, 0.0]])
    0.5
    """
    # TODO: the chain rule: the joint entropy minus the entropy of the law of X (the sums of the rows).
    raise NotImplementedError("conditional_entropy() is not implemented yet")


def mutual_information(joint, base=2):
    """Return the mutual information ``I(X ; Y) = Σ p(x, y) log(p(x, y) / (p(x) p(y)))`` of a joint law.

    Parameters
    ----------
    joint : 2-D array-like
        A valid joint law.
    base : float, default 2
        Greater than 1.

    Returns
    -------
    float
        Non-negative (a tiny negative rounding error, above ``-1e-12``, is returned as ``0.0``).

    Raises
    ------
    ValueError
        If ``joint`` is not a valid joint law or ``base <= 1``.

    Examples
    --------
    >>> mutual_information([[0.5, 0.0], [0.0, 0.5]])
    1.0
    """
    # TODO: H(Y) - H(Y | X) with your conditional_entropy, or the double sum over the positive cells.
    raise NotImplementedError("mutual_information() is not implemented yet")


def kraft_sum(lengths, alphabet=2):
    """Return the Kraft sum ``Σ D**(-l_i)`` of a list of codeword lengths, for an alphabet of ``D`` symbols.

    A prefix code with these lengths exists if and only if the sum is at most 1.

    Parameters
    ----------
    lengths : sequence of int
        Lengths of the codewords, each at least 1; at least one length.
    alphabet : int, default 2
        Number ``D`` of symbols of the code alphabet (2 for bits), at least 2.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If ``lengths`` is empty, a length is smaller than 1, or ``alphabet < 2``.

    Examples
    --------
    >>> kraft_sum([1, 2, 3, 3])
    1.0
    """
    # TODO: one term per codeword.
    raise NotImplementedError("kraft_sum() is not implemented yet")


def is_prefix_code(codewords):
    """Tell whether no codeword is the beginning (prefix) of another one.

    Parameters
    ----------
    codewords : sequence of str
        The codewords, e.g. ``["0", "10", "11"]``; a word repeated twice makes the code not prefix-free.

    Returns
    -------
    bool
        A Python ``bool``; ``True`` for an empty list or a single word.

    Raises
    ------
    ValueError
        If a codeword is the empty string.

    Examples
    --------
    >>> is_prefix_code(["0", "10", "110", "111"])
    True
    >>> is_prefix_code(["0", "01", "11"])
    False
    """
    # TODO: compare every pair (str.startswith), or sort the words: a prefix comes just before a word it starts.
    raise NotImplementedError("is_prefix_code() is not implemented yet")


def jensen_gap(f, values, weights=None):
    """Return ``E[f(X)] - f(E[X])`` for a discrete random variable ``X``: non-negative when ``f`` is convex.

    Parameters
    ----------
    f : callable
        A function of one real variable.
    values : sequence of float
        The values of ``X``, at least one.
    weights : sequence of float, optional
        Their probabilities: same length, non-negative, summing to 1 (up to 1e-9). Default: all equal.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If ``values`` is empty, or if the weights are not a valid law of the same length.

    Examples
    --------
    >>> jensen_gap(lambda x: x ** 2, [1, 3])
    1.0
    """
    # TODO: the two expectations, E[f(X)] and E[X], then the difference.
    raise NotImplementedError("jensen_gap() is not implemented yet")
