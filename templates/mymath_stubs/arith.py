"""Arithmetic with exact numbers (chapter R1): fractions, scientific notation, percentages.

Each function below starts as ``raise NotImplementedError``: replace that line with your code, then run
``pytest tests/test_r1_arith.py``. Use plain Python and the ``math`` module, but not ``math.gcd`` nor the
``fractions`` module: the tests compare your results with those trusted tools.
"""


def gcd(a, b):
    """Return the greatest common divisor of two integers, computed with Euclid's algorithm.

    Parameters
    ----------
    a, b : int
        Integers of any sign.

    Returns
    -------
    int
        The largest non-negative integer that divides both ``a`` and ``b``; ``gcd(0, 0)`` is ``0``.

    Examples
    --------
    >>> gcd(84, 36)
    12
    >>> gcd(-9, 6)
    3
    """
    # TODO: work with absolute values; replace (a, b) by (b, a mod b) until b is 0.
    raise NotImplementedError("gcd() is not implemented yet")


def simplify_fraction(numerator, denominator):
    """Return the irreducible form of the fraction ``numerator / denominator``.

    Parameters
    ----------
    numerator : int
    denominator : int
        Must not be zero.

    Returns
    -------
    tuple of (int, int)
        ``(p, q)`` with ``q > 0`` and ``gcd(p, q) == 1``; zero is ``(0, 1)``.

    Raises
    ------
    ValueError
        If ``denominator`` is zero.

    Examples
    --------
    >>> simplify_fraction(84, -36)
    (-7, 3)
    """
    # TODO: divide both by their gcd, then move the sign to the numerator.
    raise NotImplementedError("simplify_fraction() is not implemented yet")


def add_fractions(a, b):
    """Return the irreducible sum of two fractions, without any decimal number.

    Parameters
    ----------
    a, b : tuple of (int, int)
        Fractions written ``(numerator, denominator)``, denominators non-zero.

    Returns
    -------
    tuple of (int, int)
        The sum, as returned by :func:`simplify_fraction`.

    Raises
    ------
    ValueError
        If a denominator is zero.

    Examples
    --------
    >>> add_fractions((1, 6), (1, 4))
    (5, 12)
    """
    # TODO: put both fractions over a common denominator, add the numerators, simplify.
    raise NotImplementedError("add_fractions() is not implemented yet")


def scientific_notation(x, digits=3):
    """Write ``x`` as ``mantissa × 10**exponent`` with ``digits`` significant digits.

    Parameters
    ----------
    x : float
    digits : int, default 3
        Number of significant digits kept (at least 1).

    Returns
    -------
    tuple of (float, int)
        ``(mantissa, exponent)`` with ``1 <= abs(mantissa) < 10``, the mantissa rounded with
        ``round(m, digits - 1)``; ``x = 0`` gives ``(0.0, 0)``. Ties (a 5 exactly at the cut) are not tested:
        floats rarely hold them exactly.

    Examples
    --------
    >>> scientific_notation(0.000123456)
    (1.23, -4)
    >>> scientific_notation(9996, digits=3)
    (1.0, 4)
    """
    # TODO: find the exponent, divide, round; careful when rounding gives 10 (9.996 -> 10.0 -> 1.00 × 10).
    raise NotImplementedError("scientific_notation() is not implemented yet")


def successive_changes(rates):
    """Return the overall rate of change after several successive changes.

    Parameters
    ----------
    rates : sequence of float
        Rates written as decimals: ``0.10`` for +10 %, ``-0.25`` for −25 % (each at least −1, i.e. −100 %).

    Returns
    -------
    float
        The overall rate, as a decimal (``0.0`` for an empty sequence).

    Raises
    ------
    ValueError
        If a rate is below −1.

    Examples
    --------
    >>> round(successive_changes([0.10, -0.10]), 6)
    -0.01
    """
    # TODO: multiply the coefficients (1 + rate), then go back from a coefficient to a rate.
    raise NotImplementedError("successive_changes() is not implemented yet")


def weighted_mean(values, weights):
    """Return the weighted mean of ``values``.

    Parameters
    ----------
    values : sequence of float
    weights : sequence of float
        Non-negative, same length as ``values``, not all zero.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If the lengths differ, a weight is negative, or the weights sum to zero.

    Examples
    --------
    >>> weighted_mean([12, 15], [1, 2])
    14.0
    """
    # TODO: sum of value × weight, divided by the sum of the weights.
    raise NotImplementedError("weighted_mean() is not implemented yet")
