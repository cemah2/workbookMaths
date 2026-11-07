"""Information of two variables: joint and conditional entropies, mutual information, Kraft, Jensen (chapter M06).

Reference implementation (solutions/mymath_ref).
Do not use ``scipy.stats.entropy`` nor scikit-learn: the tests compare your results with them. A joint law is a
2-D table (list of lists or array) as in ``conditional.py``: rows are the values of X, columns those of Y,
non-negative entries summing to 1 (up to 1e-9). In every sum, ``0 log 0`` counts as 0. ``base=2`` gives bits,
``base=math.e`` nats. Every number returned is a Python ``float`` or ``bool``.
"""

import math
from fractions import Fraction

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


def _log_base(base):
    """ln(base), after checking that the base is greater than 1 (ValueError otherwise, nan included)."""
    if not base > 1:
        raise ValueError(f"the base of the logarithm must be greater than 1, got {base!r}")
    return math.log(base)


def _entropy(probs, log_base):
    """-Σ p log p over the positive entries of a 1-D or 2-D array, in the base whose logarithm is log_base."""
    p = probs[probs > 0]
    return float(-np.sum(p * np.log(p)) / log_base) + 0.0     # + 0.0 turns -0.0 into 0.0


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
    table = _joint(joint)
    return _entropy(table, _log_base(base))


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
    table = _joint(joint)
    log_base = _log_base(base)
    rows = table.sum(axis=1, keepdims=True)                   # p(x), next to each cell of its row
    rows = np.broadcast_to(rows, table.shape)
    positive = table > 0
    # each term p(x, y) log(p(x) / p(x, y)) is >= 0, since a row sum is never below one of its cells
    total = np.sum(table[positive] * np.log(rows[positive] / table[positive]))
    return float(total / log_base) + 0.0


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
    table = _joint(joint)
    log_base = _log_base(base)
    product = np.outer(table.sum(axis=1), table.sum(axis=0))  # p(x) p(y), cell by cell
    positive = table > 0
    value = float(np.sum(table[positive] * np.log(table[positive] / product[positive])) / log_base)
    if -1e-12 < value < 0:
        return 0.0
    return value + 0.0


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
    lengths = list(lengths)
    if not lengths:
        raise ValueError("give at least one codeword length")
    if not alphabet >= 2:
        raise ValueError(f"a code alphabet has at least 2 symbols, got {alphabet!r}")
    if any(not length >= 1 for length in lengths):
        raise ValueError(f"a codeword has length at least 1, got {lengths}")
    return float(sum(Fraction(1, int(alphabet) ** int(length)) for length in lengths))


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
    words = [str(word) for word in codewords]
    if any(word == "" for word in words):
        raise ValueError("a codeword is never the empty string")
    words.sort()                    # a word that starts another one comes just before a word it starts
    return not any(words[k + 1].startswith(words[k]) for k in range(len(words) - 1))


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
    x = np.asarray(values, dtype=float).ravel()
    if x.size == 0:
        raise ValueError("give at least one value")
    if weights is None:
        w = np.full(x.size, 1 / x.size)
    else:
        w = np.asarray(weights, dtype=float).ravel()
        if w.shape != x.shape:
            raise ValueError(f"expected {x.size} weights, one per value, got {w.size}")
        if not np.all(w >= 0) or abs(w.sum() - 1) > 1e-9:
            raise ValueError("the weights are probabilities: non-negative, summing to 1")
    expected_f = sum(float(wi) * float(f(float(xi))) for xi, wi in zip(x, w))
    mean = float(np.dot(w, x))
    return float(expected_f - float(f(mean)))
