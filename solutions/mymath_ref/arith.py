"""Arithmetic with exact numbers (chapter R1): fractions, scientific notation, percentages.

Reference implementation (solutions/mymath_ref): plain Python and the ``math`` module, as the stub asks.
"""

import math


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
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


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
    if denominator == 0:
        raise ValueError("the denominator of a fraction cannot be zero")
    divisor = gcd(numerator, denominator)
    p, q = numerator // divisor, denominator // divisor
    if q < 0:
        p, q = -p, -q
    return (p, q)


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
    (p1, q1), (p2, q2) = a, b
    if q1 == 0 or q2 == 0:
        raise ValueError("the denominator of a fraction cannot be zero")
    return simplify_fraction(p1 * q2 + p2 * q1, q1 * q2)


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
    if x == 0:
        return (0.0, 0)
    exponent = math.floor(math.log10(abs(x)))
    mantissa = x / 10**exponent if exponent >= 0 else x * 10**(-exponent)
    if abs(mantissa) >= 10:     # log10 rounded the wrong way (x just below a power of 10)
        mantissa, exponent = mantissa / 10, exponent + 1
    elif abs(mantissa) < 1:
        mantissa, exponent = mantissa * 10, exponent - 1
    mantissa = round(mantissa, digits - 1)
    if abs(mantissa) >= 10:     # 9.996 rounded to 3 digits is 10.0: write it 1.00 × 10
        mantissa, exponent = round(mantissa / 10, digits - 1), exponent + 1
    return (float(mantissa), exponent)


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
    coefficient = 1.0
    for rate in rates:
        if rate < -1:
            raise ValueError("a rate of change cannot be below -1 (-100 %)")
        coefficient *= 1 + rate
    return coefficient - 1


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
    values, weights = list(values), list(weights)
    if len(values) != len(weights):
        raise ValueError("values and weights must have the same length")
    if any(w < 0 for w in weights):
        raise ValueError("weights must be non-negative")
    total = sum(weights)
    if total == 0:
        raise ValueError("the weights sum to zero")
    return float(sum(v * w for v, w in zip(values, weights))) / total
