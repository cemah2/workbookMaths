"""Exponential and logarithm: logarithms in any base, sigmoid, tanh, doubling time (chapter R6).

Reference implementation (solutions/mymath_ref).
"""

import math


def log_base(x, base):
    """Return the logarithm of ``x`` in base ``base``.

    Parameters
    ----------
    x : float
        Positive.
    base : float
        Positive and different from 1.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If ``x <= 0``, ``base <= 0`` or ``base == 1``.

    Examples
    --------
    >>> round(log_base(8, 2), 12)
    3.0
    """
    if x <= 0:
        raise ValueError(f"the logarithm needs x > 0, got x = {x}")
    if base <= 0 or base == 1:
        raise ValueError(f"the base must be positive and different from 1, got base = {base}")
    return math.log(x) / math.log(base)


def sigmoid(x):
    """Return the logistic sigmoid ``1 / (1 + exp(-x))``.

    Parameters
    ----------
    x : float
        A single number with ``|x| <= 30`` (the tests stay there; NumPy arrays and very large ``|x|`` come later,
        in workbookIA).

    Returns
    -------
    float
        A number in ``]0, 1[``.

    Examples
    --------
    >>> sigmoid(0)
    0.5
    """
    return 1 / (1 + math.exp(-x))


def tanh(x):
    """Return the hyperbolic tangent of ``x``, computed from ``exp``.

    Parameters
    ----------
    x : float
        A single number with ``|x| <= 30``.

    Returns
    -------
    float
        A number in ``]-1, 1[`` (rounding may give exactly ±1.0 near the ends).

    Examples
    --------
    >>> tanh(0)
    0.0
    """
    return 2 * sigmoid(2 * x) - 1


def doubling_time(rate):
    """Return the number of periods after which a quantity growing by ``rate`` per period has doubled.

    Parameters
    ----------
    rate : float
        Growth rate per period, as a decimal (``0.07`` for +7 %), positive.

    Returns
    -------
    float
        The real number ``n`` such that ``(1 + rate)**n == 2`` (not rounded).

    Raises
    ------
    ValueError
        If ``rate <= 0``.

    Examples
    --------
    >>> round(doubling_time(1.0), 12)
    1.0
    """
    if rate <= 0:
        raise ValueError(f"a doubling time needs a positive growth rate, got rate = {rate}")
    return math.log(2) / math.log(1 + rate)
