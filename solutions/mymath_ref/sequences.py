"""Sequences: arithmetic and geometric sequences, recurrences, moving averages (chapter R5).

Reference implementation (solutions/mymath_ref).
"""


def arithmetic_term(u0, r, n):
    """Return the term ``u(n)`` of the arithmetic sequence of first term ``u0`` and common difference ``r``.

    Parameters
    ----------
    u0, r : float
    n : int
        **Index** of the term, ``n >= 0`` (``u(0) = u0``).

    Returns
    -------
    int or float
        An int when ``u0`` and ``r`` are ints.

    Examples
    --------
    >>> arithmetic_term(5, 3, 10)
    35
    """
    return u0 + n * r


def geometric_sum(u0, q, n):
    """Return the sum of the first ``n`` terms ``u0 + u0*q + ... + u0*q**(n - 1)`` of a geometric sequence.

    Parameters
    ----------
    u0, q : float
    n : int
        **Number of terms**, ``n >= 0`` (the empty sum is 0): the last term is ``u0*q**(n - 1)``.

    Returns
    -------
    float

    Examples
    --------
    >>> geometric_sum(1, 2, 10)
    1023.0
    """
    if n == 0:
        return 0.0
    if q == 1:
        return float(n * u0)
    return u0 * (1 - q**n) / (1 - q)


def iterate(f, u0, n):
    """Return the first terms of the sequence defined by ``u(0) = u0`` and ``u(k + 1) = f(u(k))``.

    Parameters
    ----------
    f : callable
    u0 : float
    n : int
        **Last index** computed, ``n >= 0``.

    Returns
    -------
    list
        ``[u(0), u(1), ..., u(n)]`` (``n + 1`` values).

    Examples
    --------
    >>> iterate(lambda u: 2 * u + 1, 0, 4)
    [0, 1, 3, 7, 15]
    """
    terms = [u0]
    for _ in range(n):
        terms.append(f(terms[-1]))
    return terms


def moving_average(values, window):
    """Return the simple moving averages of ``values`` over ``window`` consecutive values.

    Parameters
    ----------
    values : sequence of float
    window : int
        Between 1 and ``len(values)``.

    Returns
    -------
    list of float
        ``len(values) - window + 1`` averages: the mean of ``values[0:window]``, then of ``values[1:window + 1]``,
        and so on.

    Raises
    ------
    ValueError
        If ``window`` is not between 1 and ``len(values)``.

    Examples
    --------
    >>> moving_average([1, 2, 3, 4, 5], 2)
    [1.5, 2.5, 3.5, 4.5]
    """
    values = list(values)
    if not 1 <= window <= len(values):
        raise ValueError(f"the window must be between 1 and {len(values)} (the number of values), got {window}")
    return [sum(values[start:start + window]) / window for start in range(len(values) - window + 1)]


def exponential_moving_average(values, beta):
    """Return the exponential moving average ``v(t) = beta*v(t - 1) + (1 - beta)*x(t)``, starting from ``v(0) = 0``.

    Parameters
    ----------
    values : sequence of float
        ``x(1), x(2), ..., x(T)``.
    beta : float
        Between 0 (included) and 1 (excluded): the weight kept from the past.

    Returns
    -------
    list of float
        ``[v(1), ..., v(T)]``.

    Raises
    ------
    ValueError
        If ``beta`` is not in ``[0, 1)``.

    Examples
    --------
    >>> exponential_moving_average([10, 10], 0.5)
    [5.0, 7.5]
    """
    if not 0 <= beta < 1:
        raise ValueError(f"beta must be in [0, 1), got {beta}")
    averages, v = [], 0.0
    for x in values:
        v = beta * v + (1 - beta) * x
        averages.append(v)
    return averages
