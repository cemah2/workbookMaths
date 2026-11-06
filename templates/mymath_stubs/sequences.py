"""Sequences: arithmetic and geometric sequences, recurrences, moving averages (chapter R5).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_r5_sequences.py``.
"""


def arithmetic_term(u0, r, n):
    """Return the term ``u(n)`` of the arithmetic sequence of first term ``u0`` and common difference ``r``.

    Parameters
    ----------
    u0, r : float
    n : int
        Index, ``n >= 0``.

    Returns
    -------
    float

    Examples
    --------
    >>> arithmetic_term(5, 3, 10)
    35
    """
    # TODO: the explicit formula, no loop.
    raise NotImplementedError("arithmetic_term() is not implemented yet")


def geometric_sum(u0, q, n):
    """Return the sum of the first ``n`` terms ``u0 + u0*q + ... + u0*q**(n - 1)`` of a geometric sequence.

    Parameters
    ----------
    u0, q : float
    n : int
        Number of terms, ``n >= 0`` (the empty sum is 0).

    Returns
    -------
    float

    Examples
    --------
    >>> geometric_sum(1, 2, 10)
    1023.0
    """
    # TODO: the closed formula, without a loop; q = 1 is a special case.
    raise NotImplementedError("geometric_sum() is not implemented yet")


def iterate(f, u0, n):
    """Return the first terms of the sequence defined by ``u(0) = u0`` and ``u(k + 1) = f(u(k))``.

    Parameters
    ----------
    f : callable
    u0 : float
    n : int
        Last index computed, ``n >= 0``.

    Returns
    -------
    list
        ``[u(0), u(1), ..., u(n)]`` (``n + 1`` values).

    Examples
    --------
    >>> iterate(lambda u: 2 * u + 1, 0, 4)
    [0, 1, 3, 7, 15]
    """
    # TODO: start the list with u0 and apply f n times.
    raise NotImplementedError("iterate() is not implemented yet")


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
    # TODO: one mean per position of the window.
    raise NotImplementedError("moving_average() is not implemented yet")


def exponential_moving_average(values, beta, bias_correction=False):
    """Return the exponential moving average ``v(t) = beta*v(t - 1) + (1 - beta)*x(t)``, starting from ``v(0) = 0``.

    Parameters
    ----------
    values : sequence of float
        ``x(1), x(2), ..., x(T)``.
    beta : float
        Between 0 (included) and 1 (excluded): the weight kept from the past.
    bias_correction : bool, default False
        If True, return ``v(t) / (1 - beta**t)`` instead of ``v(t)`` (this removes the pull towards the starting
        value 0 during the first steps).

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
    >>> exponential_moving_average([10, 10], 0.5, bias_correction=True)
    [10.0, 10.0]
    """
    # TODO: a loop that updates v; index t starts at 1.
    raise NotImplementedError("exponential_moving_average() is not implemented yet")
