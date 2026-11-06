"""Exponential and logarithm: logarithms in any base, sigmoid, tanh, doubling time (chapter R6).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_r6_explog.py``.
You may use ``math.exp`` and ``math.log`` (natural logarithm), not ``math.tanh`` nor ``math.log2``/``math.log10``.
"""


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
    # TODO: change of base with the natural logarithm.
    raise NotImplementedError("log_base() is not implemented yet")


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
    # TODO: the definition, with math.exp.
    raise NotImplementedError("sigmoid() is not implemented yet")


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
    # TODO: (e^x − e^(−x)) / (e^x + e^(−x)), or reuse sigmoid.
    raise NotImplementedError("tanh() is not implemented yet")


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
    # TODO: take the logarithm of both sides.
    raise NotImplementedError("doubling_time() is not implemented yet")
