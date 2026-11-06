"""Approximation and floating point: Taylor polynomials, Newton's method, Richardson, epsilon, log-sum-exp (M05a).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m05a_approx.py``.
Do not use ``scipy.special.logsumexp``, ``numpy.finfo`` nor ``sys.float_info``: the tests compare your results with
them. Every number returned is a Python ``float``.
"""


def taylor_polynomial(derivatives, a, x):
    """Evaluate at ``x`` the Taylor polynomial of a function at ``a``, given its derivatives at ``a``.

    ``Σ_k f⁽ᵏ⁾(a) (x - a)**k / k!`` for ``k`` from 0 to ``len(derivatives) - 1``.

    Parameters
    ----------
    derivatives : sequence of float
        ``[f(a), f'(a), f''(a), ...]``, at least one value.
    a : float
        The point where the derivatives are taken.
    x : float
        Where the polynomial is evaluated.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If ``derivatives`` is empty.

    Examples
    --------
    >>> round(taylor_polynomial([1, 1, 1, 1], 0, 0.5), 6)   # exp at 0, order 3
    1.645833
    """
    # TODO: a loop that keeps k! and (x - a)**k up to date (math.factorial is allowed too).
    raise NotImplementedError("taylor_polynomial() is not implemented yet")


def newton(f, fprime, x0, tol=1e-12, max_iter=50):
    """Find a zero of ``f`` by Newton's method, starting from ``x0``.

    Repeat ``x ← x - f(x) / f'(x)`` until two successive values differ by less than ``tol``.

    Parameters
    ----------
    f, fprime : callable
        The function and its derivative.
    x0 : float
        The starting point.
    tol : float, default 1e-12
        Stop when ``|x_{k+1} - x_k| < tol`` (or when ``f(x_k) == 0`` exactly).
    max_iter : int, default 50
        Maximum number of steps.

    Returns
    -------
    float
        The last value computed.

    Raises
    ------
    ValueError
        If ``fprime`` is 0 at a point of the sequence (the tangent is horizontal).
    RuntimeError
        If the method has not stopped after ``max_iter`` steps.

    Examples
    --------
    >>> round(newton(lambda x: x * x - 2, lambda x: 2 * x, 1.0), 10)
    1.4142135624
    """
    # TODO: a loop of at most max_iter steps; check fprime before dividing.
    raise NotImplementedError("newton() is not implemented yet")


def richardson_derivative(f, x, h=0.01):
    """Approximate ``f'(x)`` by Richardson extrapolation of the centred difference.

    With ``D(h) = (f(x + h) - f(x - h)) / (2 h)``, whose error starts with a term in ``h²``, the combination
    ``(4 D(h / 2) - D(h)) / 3`` cancels that term: its error starts with a term in ``h⁴``.

    Parameters
    ----------
    f : callable
        A function of one real variable.
    x : float
    h : float, default 0.01
        The larger step, positive.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If ``h <= 0``.

    Examples
    --------
    >>> round(richardson_derivative(lambda x: x ** 5, 1.0, 0.1), 8)
    4.999975
    """
    # TODO: write D as a small inner function, then combine D(h / 2) and D(h).
    raise NotImplementedError("richardson_derivative() is not implemented yet")


def machine_epsilon(dtype=float):
    """Return the machine epsilon of a floating-point type: the gap between 1 and the next representable number.

    It is the smallest power of 2, ``eps``, such that ``1 + eps`` is not rounded back to 1 in that type.

    Parameters
    ----------
    dtype : type, default float
        ``float`` (Python's 64-bit floats) or a NumPy type such as ``numpy.float32`` or ``numpy.float16``; every
        computation is done in that type, e.g. ``one = dtype(1)``.

    Returns
    -------
    float
        A Python ``float``.

    Examples
    --------
    >>> machine_epsilon() == 2.0 ** -52
    True
    """
    # TODO: start from eps = dtype(1) and halve it while dtype(1) + eps / 2 is still different from dtype(1).
    raise NotImplementedError("machine_epsilon() is not implemented yet")


def logsumexp(values):
    """Return ``ln(e**v_1 + ... + e**v_n)`` without overflow nor underflow.

    Factor out the largest value ``m``: ``ln Σ e**v_i = m + ln Σ e**(v_i - m)``.

    Parameters
    ----------
    values : sequence of float
        At least one value; ``-math.inf`` is allowed (``e**-inf = 0``).

    Returns
    -------
    float
        ``-math.inf`` when every value is ``-math.inf``.

    Raises
    ------
    ValueError
        If ``values`` is empty.

    Examples
    --------
    >>> round(logsumexp([0, 0]), 6)
    0.693147
    >>> round(logsumexp([1000, 1000]), 6)
    1000.693147
    """
    # TODO: the case where the maximum is -inf first (inf - inf would give nan), then the factored formula.
    raise NotImplementedError("logsumexp() is not implemented yet")
