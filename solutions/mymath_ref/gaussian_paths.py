"""Gaussian paths: the moments of a linear Gaussian recursion followed step by step, the optimal denoiser of a noisy
measurement whose signal follows a mixture of Gaussians, and two methods to follow a velocity field that depends on
time, forward or backward (chapter MB5).

Reference implementation (solutions/mymath_ref).
NumPy and ``math`` are allowed, and no SciPy at all (``scipy.integrate.solve_ivp``, ``odeint`` and ``quad``,
``scipy.stats.norm``, ``scipy.special.logsumexp`` and ``softmax``…): the tests compare your results with SciPy and
with simulations. Relative imports of your own modules are allowed (``from .approx import logsumexp``, M05a).

Conventions. ``N(μ, v)`` is written with a **variance** ``v``, never a standard deviation. A noise ``ε`` (or ``n``)
has the law ``N(0, 1)`` and is independent of everything else. A velocity field is a function ``f(t, x)``, time
first, as in SciPy. Never modify the arrays you receive. Results are returned as ``numpy.ndarray`` of floats.
"""

import math

import numpy as np


def _is_bool(value):
    """Whether value is a bool, a NumPy bool or an array of booleans (True == 1, but a bool is not a number here)."""
    return isinstance(value, (bool, np.bool_)) or (isinstance(value, np.ndarray) and value.dtype.kind == "b")


def _real(value, what):
    """value as a finite Python float (a Python or NumPy real number; a bool, a string, a complex number or an array
    of more than one dimension is refused), or ValueError."""
    if value is None or _is_bool(value) or isinstance(value, (str, bytes, complex, np.complexfloating)):
        raise ValueError(f"{what} must be a finite real number (not a bool), got {value!r}")
    if isinstance(value, np.ndarray) and (value.ndim != 0 or value.dtype.kind not in "iuf"):
        raise ValueError(f"{what} must be a finite real number, got an array of shape {value.shape}")
    try:
        x = float(value)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(f"{what} must be a finite real number, got {value!r}") from None
    if not math.isfinite(x):
        raise ValueError(f"{what} must be a finite real number, got {value!r}")
    return x


def _floats(values, what):
    """values as a NEW float array of finite numbers, of its own shape (never a view of what was received), or
    ValueError; booleans, strings and complex numbers are refused."""
    if values is None or _is_bool(values):
        raise ValueError(f"{what} must hold finite real numbers, got {values!r}")
    try:
        raw = np.asarray(values)
    except (TypeError, ValueError):             # a ragged list
        raise ValueError(f"{what} must be an array (rows of the same length) of finite real numbers") from None
    if raw.dtype.kind in "bcUSaV":
        raise ValueError(f"{what} must hold real numbers (not booleans, strings or complex numbers), got dtype "
                         f"{raw.dtype}")
    try:
        X = np.array(raw, dtype=float)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(f"{what} must hold finite real numbers") from None
    if not np.all(np.isfinite(X)):
        raise ValueError(f"{what} must hold finite numbers only (no nan, no inf)")
    return X


def _vector(values, what):
    """values as a NEW 1-D float array of finite numbers, or ValueError."""
    X = _floats(values, what)
    if X.ndim != 1:
        raise ValueError(f"{what} must be 1-D, got an array of shape {X.shape}")
    return X


def _steps(n_steps):
    """n_steps as a Python int ≥ 1 (a Python or NumPy integer; a bool or a float is refused), or ValueError."""
    if _is_bool(n_steps) or not isinstance(n_steps, (int, np.integer)):
        raise ValueError(f"n_steps must be an integer ≥ 1 (not a bool, not a float such as 4.0), got {n_steps!r}")
    if n_steps < 1:
        raise ValueError(f"n_steps must be an integer ≥ 1, got {n_steps!r}")
    return int(n_steps)


def linear_gaussian_recursion(a, b, mean0=0.0, var0=0.0):
    """Return the means and the variances of ``x_0, x_1, …, x_T`` when ``x_t = a_t x_{t-1} + b_t ε_t``.

    The noises ``ε_1, …, ε_T`` are independent, of law ``N(0, 1)``, and independent of the start
    ``x_0 ~ N(mean0, var0)`` (``var0 = 0`` is a known start, ``x_0 = mean0``). Each ``x_t`` is an affine image of the
    Gaussian vector ``(x_0, ε_1, …, ε_t)``, hence Gaussian (M25a), and its two moments follow, one step at a time,

        ``m_t = a_t m_{t-1}``  and  ``v_t = a_t² v_{t-1} + b_t²``

    (the prediction step of a Kalman filter in dimension 1). Unrolled, ``m_t = (a_1 ⋯ a_t) m_0``, a cumulative product,
    and ``v_t = (a_1 ⋯ a_t)² v_0 + Σ_{k ≤ t} b_k² (a_{k+1} ⋯ a_t)²``.

    Parameters
    ----------
    a : 1-D array-like
        The ``T ≥ 0`` coefficients ``a_1, …, a_T`` (``a[0]`` is ``a_1``), real numbers (negative ones are allowed).
    b : 1-D array-like
        The ``T`` noise coefficients ``b_1, …, b_T``, real numbers. Only ``b_t²`` matters: ``b_t`` and ``-b_t`` give
        the same law.
    mean0 : float, default 0.0
        The mean of ``x_0``.
    var0 : float, default 0.0
        The variance of ``x_0``, ``≥ 0``.

    Returns
    -------
    tuple of two numpy.ndarray
        ``(means, variances)``, each of shape ``(T + 1,)``: entry ``t`` is the mean or the variance of ``x_t``
        (entry 0 holds ``mean0`` and ``var0``).

    Raises
    ------
    ValueError
        If ``a`` or ``b`` is not 1-D, if they do not have the same length, if one of their entries is not finite, or
        if ``mean0`` or ``var0`` is not a finite real number (a ``bool`` is refused), or if ``var0 < 0``.

    Examples
    --------
    >>> m, v = linear_gaussian_recursion([0.5, 2.0, 1.0], [1.0, 0.0, 3.0], mean0=4.0)
    >>> m
    array([4., 2., 4., 4.])
    >>> v                                  # 0.25 × 0 + 1, then 4 × 1 + 0, then 1 × 4 + 9
    array([ 0.,  1.,  4., 13.])
    >>> linear_gaussian_recursion([0.5], [-1.0], mean0=2.0, var0=8.0)    # an uncertain start: 0.25 × 8 + 1 = 3
    (array([2., 1.]), array([8., 3.]))
    """
    A = _vector(a, "a")
    B = _vector(b, "b")
    if A.shape != B.shape:
        raise ValueError(f"a and b must have the same length, got {A.size} and {B.size}")
    m = _real(mean0, "mean0")
    v = _real(var0, "var0")
    if v < 0:
        raise ValueError(f"var0 must be ≥ 0, got {var0!r}")
    T = A.size
    means = np.empty(T + 1)
    variances = np.empty(T + 1)
    means[0], variances[0] = m, v
    for t in range(T):                          # step t + 1 uses a[t] = a_{t+1} and b[t] = b_{t+1}
        m = A[t] * m
        v = A[t] * A[t] * v + B[t] * B[t]
        means[t + 1], variances[t + 1] = m, v
    return means, variances


def posterior_mean_mixture(y, a, b, weights, means, variances):
    """Return ``E[x | y]`` for the measurement ``y = a x + b n``, when ``x`` follows a mixture of Gaussians.

    The signal ``x`` has the density ``Σ_k π_k N(x | μ_k, s_k²)``; a variance ``s_k² = 0`` is a point mass at ``μ_k``,
    so that a finite set of points with their frequencies is such a mixture. The noise ``n ~ N(0, 1)`` is independent
    of ``x``. Given the component ``k``, ``(x, y)`` is a linear Gaussian model (M25a §5): ``y`` has the law
    ``N(a μ_k, a² s_k² + b²)``, and

        ``E[x | y, k] = μ_k + a s_k² (y - a μ_k) / (a² s_k² + b²)``.

    The component is unknown: its posterior probability given ``y`` (its responsibility, M25b) is proportional to
    ``π_k N(y | a μ_k, a² s_k² + b²)``, to be computed through logarithms (subtract the largest log before taking
    exponentials, as in log-sum-exp, M05a), and ``E[x | y]`` is the average of the ``E[x | y, k]`` weighted by the
    responsibilities. A component of weight ``π_k = 0`` gets a responsibility 0.

    ``E[x | y]``, as a function of ``y``, is the optimal denoiser: no function ``g`` has a smaller mean squared error
    ``E[(x - g(y))²]`` (MB5 §4). When ``a = 0``, ``y`` says nothing about ``x`` and the result is the mean of the
    mixture, ``Σ_k π_k μ_k``, whatever ``y``.

    Parameters
    ----------
    y : float or array-like
        One or several measurements, finite real numbers, of any shape.
    a : float
        The gain of the signal, a finite real number (0 and negative values are allowed).
    b : float
        The scale of the noise, ``b > 0``.
    weights : 1-D array-like
        The ``K ≥ 1`` weights ``π_k ≥ 0``, summing to 1 (up to 1e-9).
    means : 1-D array-like
        The ``K`` means ``μ_k``, finite real numbers.
    variances : 1-D array-like
        The ``K`` variances ``s_k² ≥ 0`` (0 for a point mass).

    Returns
    -------
    numpy.ndarray
        ``E[x | y]`` for each measurement, of the shape of ``y`` (a 0-d array for a single number; ``float(…)``
        converts it).

    Raises
    ------
    ValueError
        If ``y`` has an entry that is not finite, if ``a`` is not a finite real number or ``b`` is not a positive
        finite real number (a ``bool`` is refused), if ``weights``, ``means`` and ``variances`` are not 1-D of the same
        length ``K ≥ 1``, if a weight is negative or the weights do not sum to 1, or if a mean is not finite or a
        variance is negative or not finite.

    Examples
    --------
    >>> posterior_mean_mixture([0.0, 3.0], 1.0, 1.0, [1.0], [2.0], [3.0])     # one Gaussian: 2 + 0.75 (y - 2)
    array([0.5 , 2.75])
    >>> np.round(posterior_mean_mixture([-0.5, 0.8, 1.5], 1.0, 1.0, [0.3, 0.7], [-1.0, 2.0], [0.0, 0.0]), 4)
    array([-0.6878,  1.5548,  1.9373])
    >>> posterior_mean_mixture(5.0, 0.0, 2.0, [0.3, 0.7], [-1.0, 2.0], [0.0, 0.0])    # a = 0: the mixture mean
    array(1.1)
    """
    Y = _floats(y, "y")                         # a new array, of the shape of y
    gain = _real(a, "a")
    scale = _real(b, "b")
    if scale <= 0:
        raise ValueError(f"b must be > 0 (the scale of the noise), got {b!r}")
    W = _vector(weights, "weights")
    M = _vector(means, "means")
    S = _vector(variances, "variances")
    if W.size == 0 or not (W.size == M.size == S.size):
        raise ValueError(f"weights, means and variances must have the same length K ≥ 1, got {W.size}, {M.size} and "
                         f"{S.size}")
    if np.any(W < 0):
        raise ValueError(f"the weights must be ≥ 0, got {W.tolist()}")
    total = float(W.sum())
    if abs(total - 1.0) > 1e-9:
        raise ValueError(f"the weights must sum to 1 (up to 1e-9), got a sum of {total!r}")
    if np.any(S < 0):
        raise ValueError(f"the variances must be ≥ 0, got {S.tolist()}")
    if gain == 0.0:                             # y says nothing about x: the responsibilities are the weights
        return np.full(Y.shape, float(np.dot(W, M) / total))
    spread = gain * gain * S + scale * scale    # the variance of y given the component k: a² s_k² + b²
    pull = gain * S / spread                    # E[x | y, k] = μ_k + pull_k (y - a μ_k)
    gap = Y.reshape(-1, 1) - gain * M           # (number of measurements, K)
    positive = W > 0
    log_weights = np.full(W.shape, -np.inf)
    log_weights[positive] = np.log(W[positive])
    log_terms = log_weights - 0.5 * np.log(2 * math.pi * spread) - gap * gap / (2 * spread)
    top = log_terms.max(axis=1, keepdims=True)  # finite: at least one weight is positive
    resp = np.exp(log_terms - top)              # one log-sum-exp per measurement
    resp /= resp.sum(axis=1, keepdims=True)
    within = M + pull * gap                     # E[x | y, k] for each measurement and each component
    return (resp * within).sum(axis=1).reshape(Y.shape)


def _velocity(f, t, x, shape):
    """f(t, x) as a float array, of the shape of x0, or ValueError."""
    v = np.asarray(f(t, x), dtype=float)
    if v.shape != shape:
        raise ValueError(f"f must return a velocity of the shape {shape} of x0, got the shape {v.shape} at t = {t!r}")
    return v


def _path(f, x0, t0, t1, n_steps, step):
    """The points of the one-step method ``step`` from x(t0) = x0 to t1 in n_steps steps."""
    N = _steps(n_steps)
    start = _real(t0, "t0")
    end = _real(t1, "t1")
    x = np.array(x0, dtype=float)               # a float copy of x0, never x0 itself
    h = (end - start) / N
    points = np.empty((N + 1,) + x.shape)
    points[0] = x
    for k in range(N):
        x = step(f, start + k * h, x, h)        # a new array at each step
        points[k + 1] = x
    return points


def _euler_step(f, t, x, h):
    return x + h * _velocity(f, t, x, x.shape)


def _midpoint_step(f, t, x, h):
    k1 = _velocity(f, t, x, x.shape)
    k2 = _velocity(f, t + h / 2, x + (h / 2) * k1, x.shape)
    return x + h * k2


def euler_ode(f, x0, t0, t1, n_steps):
    """Return the points ``x_0, x_1, …, x_N`` of Euler's method for ``x'(t) = f(t, x)``, from ``x(t0) = x0`` to ``t1``.

    With ``N = n_steps`` steps of length ``h = (t1 - t0) / N`` and the times ``t_k = t0 + k h``,

        ``x_{k+1} = x_k + h f(t_k, x_k)``:

    the velocity is read at the start of each step and kept during the whole step (the tangent, MB5 §8). One
    evaluation of ``f`` per step. ``t1 < t0`` is allowed: ``h`` is then negative and the method goes back in time
    along the same velocity field. Euler's method is exact when the velocity stays constant along the path; otherwise
    its error at ``t1`` is, for a regular field, of order ``h`` (MB5 §8).

    Parameters
    ----------
    f : callable
        The velocity field: ``f(t, x)`` takes a time (a float) and a point (an array of the shape of ``x0``) and
        returns the velocity, of the shape of ``x0`` (a number when ``x0`` is a number).
    x0 : float or array-like
        The starting point, at time ``t0``: a number, or an array of any shape (several coordinates, or several
        points moved at once by a vectorized ``f``).
    t0, t1 : float
        The starting and final times, finite; ``t1`` may be smaller than ``t0``, or equal to it.
    n_steps : int
        The number ``N ≥ 1`` of steps (a NumPy integer is accepted; a ``bool`` or a float is refused).

    Returns
    -------
    numpy.ndarray
        The points, of shape ``(N + 1,) + shape of x0``: entry ``k`` is ``x_k``, at time ``t_k``, and entry 0 is
        ``x0``. The times are ``np.linspace(t0, t1, N + 1)``.

    Raises
    ------
    ValueError
        If ``n_steps`` is not an integer ``≥ 1``, if ``t0`` or ``t1`` is not a finite real number, or if ``f`` returns
        a velocity whose shape is not that of ``x0``.

    Examples
    --------
    >>> euler_ode(lambda t, x: 2 * t + 1, 0.0, 1.0, 3.0, 4)    # x' = 2t + 1 from x(1) = 0: the exact x(3) is 10
    array([0. , 1.5, 3.5, 6. , 9. ])
    >>> euler_ode(lambda t, x: 2.0, 1.0, 0.0, 3.0, 1)        # a constant velocity: one step is exact
    array([1., 7.])
    >>> euler_ode(lambda t, x: -x / 4, [4.0, -8.0], 2.0, 0.0, 2)    # backward, h = -1: each step multiplies by 1.25
    array([[  4.  ,  -8.  ],
           [  5.  , -10.  ],
           [  6.25, -12.5 ]])
    """
    return _path(f, x0, t0, t1, n_steps, _euler_step)


def midpoint_ode(f, x0, t0, t1, n_steps):
    """Return the points ``x_0, x_1, …, x_N`` of the midpoint method for ``x'(t) = f(t, x)``, from ``x(t0) = x0``.

    Same steps as ``euler_ode`` (``h = (t1 - t0) / N``, ``t_k = t0 + k h``), but each step first makes a half Euler
    step to estimate the point at the middle of the step, then uses the velocity read there for the whole step:

        ``x_{k+1/2} = x_k + (h / 2) f(t_k, x_k)``,  then  ``x_{k+1} = x_k + h f(t_k + h / 2, x_{k+1/2})``.

    Two evaluations of ``f`` per step. The method is exact when the velocity depends on the time only, as an affine
    function ``α + β t``, and its error at ``t1`` is, for a regular field, of order ``h²`` (MB5 §8). ``t1 < t0`` is
    allowed, as in ``euler_ode``.

    Parameters
    ----------
    f : callable
        The velocity field ``f(t, x)``, as in ``euler_ode``.
    x0 : float or array-like
        The starting point, at time ``t0``, as in ``euler_ode``.
    t0, t1 : float
        The starting and final times, finite; ``t1`` may be smaller than ``t0``, or equal to it.
    n_steps : int
        The number ``N ≥ 1`` of steps (a NumPy integer is accepted; a ``bool`` or a float is refused).

    Returns
    -------
    numpy.ndarray
        The points, of shape ``(N + 1,) + shape of x0``, as in ``euler_ode``; the half-step points are not returned.

    Raises
    ------
    ValueError
        As ``euler_ode``.

    Examples
    --------
    >>> midpoint_ode(lambda t, x: 2 * t + 1, 0.0, 1.0, 3.0, 4)   # exact: x(t) = t² + t - 2
    array([ 0.  ,  1.75,  4.  ,  6.75, 10.  ])
    >>> midpoint_ode(lambda t, x: -x / 4, [4.0, -8.0], 2.0, 0.0, 2)  # the exact x(0) is e^0.5 x0 ≈ (6.5949, -13.1898)
    array([[  4.        ,  -8.        ],
           [  5.125     , -10.25      ],
           [  6.56640625, -13.1328125 ]])
    """
    return _path(f, x0, t0, t1, n_steps, _midpoint_step)
