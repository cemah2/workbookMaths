"""Approximation and floating point: Taylor polynomials, Newton's method, Richardson, epsilon, log-sum-exp (M05a).

Reference implementation (solutions/mymath_ref).
Do not use ``scipy.special.logsumexp``, ``numpy.finfo`` nor ``sys.float_info``: the tests compare your results with
them. Every number returned is a Python ``float``.
"""

import math


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
    derivatives = list(derivatives)
    if not derivatives:
        raise ValueError("at least one derivative is needed: [f(a), f'(a), ...]")
    dx = x - a
    term = 1.0                     # (x - a)**k / k!, kept up to date: no factorial nor power overflows on its own
    total = 0.0
    for k, derivative in enumerate(derivatives):
        if k > 0:
            term *= dx / k
        total += derivative * term
    return float(total)


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
    x = float(x0)
    for _ in range(max_iter):
        fx = f(x)
        if fx == 0:
            return float(x)                            # already a zero: no step to take
        slope = fprime(x)
        if slope == 0:
            raise ValueError(f"f'({x}) = 0: the tangent is horizontal, Newton's step is not defined")
        x_new = x - fx / slope
        if abs(x_new - x) < tol:
            return float(x_new)
        x = x_new
    raise RuntimeError(f"Newton's method has not converged after {max_iter} steps (last value {x})")


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
    if not h > 0:
        raise ValueError(f"the step h must be positive, got {h!r}")

    def centred(step):
        return (f(x + step) - f(x - step)) / (2 * step)

    return float((4 * centred(h / 2) - centred(h)) / 3)


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
    one, two = dtype(1), dtype(2)
    eps = dtype(1)
    while dtype(one + dtype(eps / two)) != one:        # half of eps still changes 1: eps is not the gap yet
        eps = dtype(eps / two)
    return float(eps)


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
    values = [float(v) for v in values]
    if not values:
        raise ValueError("log-sum-exp of an empty sequence is not defined")
    m = max(values)
    if math.isinf(m):
        return m                                       # -inf (every term is 0) or +inf (one term is infinite)
    return float(m + math.log(math.fsum(math.exp(v - m) for v in values)))
