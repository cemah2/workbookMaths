"""Convolution of sequences and kernels: the convolution of two sequences in three modes, the Toeplitz matrix of a
convolution, the circular convolution of two periodic sequences, the equivalent kernel of a stack of strided sums,
and the two factors of a separable 2-D kernel (chapter M21).

Two conventions meet here: ``convolve``, ``toeplitz_matrix`` and ``circular_convolve`` compute the convolution of
the mathematicians, which flips the kernel (``Σ_i a[i] b[k - i]``), while ``equivalent_kernel`` describes the
sliding sums of the libraries, which do not flip it (``Σ_u w[u] x[s i + u]``).

Reference implementation (solutions/mymath_ref).
NumPy is allowed, but not ``np.convolve``, ``np.correlate``, ``np.polymul``, ``np.polynomial`` nor ``np.fft``, and
no SciPy at all (``scipy.signal``, ``scipy.ndimage``, ``scipy.linalg.toeplitz``, ``convolution_matrix``,
``circulant``…): the tests compare your results with them. From ``np.linalg``, only ``svd``, in
``separable_factors`` (M12d). Never modify the arrays you receive. Sequences and matrices are returned as
``numpy.ndarray`` of floats, integers as Python ``int``.
"""

import numbers

import numpy as np

_MODES = ("full", "valid", "same")


def _sequence(values, what):
    """values as a NEW non-empty 1-D float array, or ValueError."""
    try:
        array = np.array(values, dtype=float)
    except (TypeError, ValueError):
        raise ValueError(f"{what} must be a 1-D sequence of numbers, got {values!r}") from None
    if array.ndim != 1 or array.size == 0:
        raise ValueError(f"{what} must be a non-empty 1-D sequence, got shape {array.shape}")
    return array


def _check_mode(mode):
    """mode must be one of the three strings "full", "valid" and "same"."""
    if not isinstance(mode, str) or mode not in _MODES:
        raise ValueError(f"mode must be 'full', 'valid' or 'same', got {mode!r}")


def _check_positive_int(value, what):
    """value must be an integer ≥ 1 (a bool is not accepted)."""
    if isinstance(value, bool) or not isinstance(value, numbers.Integral) or value < 1:
        raise ValueError(f"{what} must be an integer >= 1, got {value!r}")


def _rows(n, m, mode):
    """The slice of the full convolution (length n + m - 1) kept by ``mode``, for sequences of lengths n and m."""
    longest, shortest = max(n, m), min(n, m)
    if mode == "full":
        return slice(0, n + m - 1)
    if mode == "valid":                       # the shorter sequence entirely inside the longer one
        return slice(shortest - 1, longest)
    start = (shortest - 1) // 2               # "same": NumPy's convention, the extra value on the right
    return slice(start, start + longest)


def convolve(a, b, mode="full"):
    """Return the convolution ``a * b`` of two 1-D sequences: ``(a * b)[k] = Σ_i a[i] b[k - i]``.

    The sum runs over the indices ``i`` where ``a[i]`` and ``b[k - i]`` both exist. It is the product of polynomials:
    the coefficients of ``(Σ a[i] Xⁱ)(Σ b[j] Xʲ)``. It is also the law of the sum of two independent variables with
    values ``0, 1, …``, when ``a`` and ``b`` are their laws (M02b). The convolution is commutative.

    With ``n = len(a)``, ``m = len(b)``, ``L = max(n, m)`` and ``l = min(n, m)``:

    - ``"full"``: every value, ``k = 0, …, n + m - 2`` (length ``n + m - 1``);
    - ``"valid"``: only the values where the shorter sequence lies entirely inside the longer one, ``k = l - 1, …,
      L - 1`` (length ``L - l + 1``);
    - ``"same"``: ``L`` values, those of the full convolution from index ``(l - 1) // 2`` on (NumPy's convention).

    Parameters
    ----------
    a, b : 1-D array-like
        Two non-empty sequences of numbers.
    mode : {"full", "valid", "same"}, default "full"

    Returns
    -------
    numpy.ndarray
        The 1-D convolution, of floats.

    Raises
    ------
    ValueError
        If ``a`` or ``b`` is not 1-D or is empty, or if ``mode`` is not one of the three modes.

    Examples
    --------
    >>> convolve([2, 1], [1, 3, 1])               # (2 + X)(1 + 3X + X²)
    array([2., 7., 5., 1.])
    >>> convolve([3, 1, 4, 1, 5], [2, -1, 1], mode="valid")
    array([10., -1., 13.])
    >>> convolve([3, 1, 4, 1, 5], [2, -1, 1], mode="same")
    array([-1., 10., -1., 13., -4.])
    """
    x, y = _sequence(a, "a"), _sequence(b, "b")
    _check_mode(mode)
    n, m = x.size, y.size
    full = np.zeros(n + m - 1)
    for j in range(m):
        full[j:j + n] += y[j] * x             # the term b[j] Xʲ times the polynomial of a
    return full[_rows(n, m, mode)].copy()


def toeplitz_matrix(kernel, n, mode="full"):
    """Return the matrix ``T`` of the linear map ``x ↦ convolve(x, kernel, mode)`` for ``x`` of length ``n``.

    ``T @ x`` equals the convolution of ``x`` by the kernel, for every ``x`` of length ``n``. Column ``j`` of ``T``
    is the convolution of the ``j``-th vector of the canonical basis: in the mode ``"full"``, the kernel shifted down
    by ``j``; the other modes keep some of its rows (the same rows as ``convolve``). ``T`` is a **Toeplitz matrix**
    (each diagonal is constant: ``T[i, j]`` depends only on ``i - j``) and a **sparse** one (at most
    ``len(kernel)`` non-zero entries per column).

    Parameters
    ----------
    kernel : 1-D array-like
        The ``k`` coefficients of the kernel, ``k ≥ 1``.
    n : int
        The length of ``x``, ``n ≥ 1``; ``n ≥ k`` for the modes ``"valid"`` and ``"same"``.
    mode : {"full", "valid", "same"}, default "full"
        As in ``convolve``: ``T`` has ``n + k - 1``, ``n - k + 1`` or ``n`` rows.

    Returns
    -------
    numpy.ndarray
        The 2-D matrix ``T``, with ``n`` columns.

    Raises
    ------
    ValueError
        If the kernel is not 1-D or is empty, if ``n`` is not an integer ``≥ 1`` (a ``bool`` is refused), if
        ``n < k`` in the modes ``"valid"`` and ``"same"``, or if ``mode`` is unknown.

    Examples
    --------
    >>> toeplitz_matrix([2, 1, 3], 3)
    array([[2., 0., 0.],
           [1., 2., 0.],
           [3., 1., 2.],
           [0., 3., 1.],
           [0., 0., 3.]])
    >>> toeplitz_matrix([1, 2, 3], 4, mode="valid")
    array([[3., 2., 1., 0.],
           [0., 3., 2., 1.]])
    """
    w = _sequence(kernel, "kernel")
    _check_positive_int(n, "n")
    _check_mode(mode)
    k = w.size
    if mode != "full" and n < k:
        raise ValueError(f"the mode {mode!r} needs n >= len(kernel), got n = {n} and len(kernel) = {k}")
    n = int(n)
    full = np.zeros((n + k - 1, n))
    for j in range(n):
        full[j:j + k, j] = w                  # column j: the convolution of e_j, the kernel shifted down by j
    return full[_rows(n, k, mode)].copy()


def circular_convolve(a, b):
    """Return the circular convolution of two sequences of the same length ``n``: ``Σ_i a[i] b[(k - i) mod n]``.

    The two sequences are read as periodic, of period ``n``: index ``n`` is index ``0`` again. Convolving with the
    sequence ``(0, 1, 0, …, 0)`` shifts by one step (index ``k`` receives ``a[k - 1]``, and index ``0`` receives
    ``a[n - 1]``), and a circular convolution commutes with every circular shift.

    Parameters
    ----------
    a, b : 1-D array-like
        Two non-empty sequences of the same length ``n``.

    Returns
    -------
    numpy.ndarray
        The ``n`` values of the circular convolution, of floats.

    Raises
    ------
    ValueError
        If ``a`` or ``b`` is not 1-D or is empty, or if their lengths differ.

    Examples
    --------
    >>> circular_convolve([2, 5, 1, 3], [0, 1, 0, 0])      # a shift by one step
    array([3., 2., 5., 1.])
    >>> circular_convolve([2, 0, 5], [1, 1, 0])
    array([7., 2., 5.])
    """
    x, h = _sequence(a, "a"), _sequence(b, "b")
    if x.size != h.size:
        raise ValueError(f"a and b must have the same length, got {x.size} and {h.size}")
    n = x.size
    indices = np.arange(n)
    result = np.zeros(n)
    for i in range(n):
        result += x[i] * h[(indices - i) % n]     # entry k receives a[i] b[(k - i) mod n]
    return result


def equivalent_kernel(kernels, strides=None):
    """Return the kernel ``K`` and the step ``S`` of a stack of strided sliding sums, as a single sliding sum.

    Stage ``ℓ`` (``ℓ = 1, …, L``, in this order) receives a sequence ``x`` and returns
    ``y[i] = Σ_u w_ℓ[u] x[s_ℓ i + u]``, the sliding sum of the libraries (no kernel flip, no padding), with the
    kernel ``w_ℓ = kernels[ℓ - 1]`` and the step ``s_ℓ = strides[ℓ - 1]``. The whole stack is again a sliding sum
    ``z[j] = Σ_t K[t] x[S j + t]``, with ``S = s_1 s_2 ⋯ s_L``. ``K`` has exactly
    ``1 + Σ_ℓ (k_ℓ - 1) s_1 ⋯ s_{ℓ-1}`` coefficients, where ``k_ℓ = len(w_ℓ)`` (zeros included, never trimmed): the
    window ``x[S j], …, x[S j + len(K) - 1]`` is the **receptive field** of ``z[j]``. For two stages,
    ``K[t] = Σ_{s_1 v + u = t} w_2[v] w_1[u]``.

    Parameters
    ----------
    kernels : sequence of 1-D array-like
        The ``L ≥ 1`` kernels, from the first stage to the last; each is non-empty.
    strides : sequence of int, optional
        The ``L`` steps, each an integer ``≥ 1`` (a ``bool`` is refused); all equal to 1 when omitted.

    Returns
    -------
    tuple
        ``(K, S)``: ``K`` a 1-D ``numpy.ndarray`` of floats, ``S`` an ``int``.

    Raises
    ------
    ValueError
        If there is no kernel, if a kernel is not 1-D or is empty, or if ``strides`` does not hold ``L`` integers
        ``≥ 1``.

    Examples
    --------
    >>> equivalent_kernel([[1, 1], [1, 1]])                 # two sums of width 2
    (array([1., 2., 1.]), 1)
    >>> equivalent_kernel([[1, 1, 1], [1, -1]], strides=[2, 1])
    (array([ 1.,  1.,  0., -1., -1.]), 2)
    """
    if isinstance(kernels, (str, bytes)):
        raise ValueError(f"kernels must be a sequence of 1-D kernels, got {kernels!r}")
    try:
        stages = [_sequence(w, f"kernel {i}") for i, w in enumerate(kernels)]
    except TypeError:                             # not iterable
        raise ValueError(f"kernels must be a sequence of 1-D kernels, got {kernels!r}") from None
    if not stages:
        raise ValueError("there must be at least one kernel")
    if strides is None:
        steps = [1] * len(stages)
    else:
        try:
            steps = list(strides)
        except TypeError:
            raise ValueError(f"strides must be a sequence of {len(stages)} integers, got {strides!r}") from None
        if len(steps) != len(stages):
            raise ValueError(f"strides must hold {len(stages)} integers (one per kernel), got {len(steps)}")
        for s in steps:
            _check_positive_int(s, "each stride")
    K, S = np.ones(1), 1
    for w, s in zip(stages, steps):
        # stage ℓ reads its input every S-th value of x: its kernel, spread with S - 1 zeros between its
        # coefficients, is convolved with the kernel of the stages before it (t = S v + u)
        spread = np.zeros((w.size - 1) * S + 1)
        spread[::S] = w
        K = convolve(K, spread)
        S *= int(s)
    return K, S


def separable_factors(kernel, tol=1e-10):
    """Return the two factors ``(u, v)`` of a separable 2-D kernel, ``kernel = outer(u, v)``, or ``None``.

    A kernel is **separable** when it has rank 1: every row is a multiple of the same row ``v``. Filtering with it
    then amounts to two 1-D filterings, one along the columns with ``u`` and one along the rows with ``v``. The
    factors are normalized: ``‖v‖ = 1``, the first coordinate of ``v`` with ``|v_j| > 1e-8`` is positive (smaller
    ones count as zero), and ``u = kernel @ v``.
    The kernel counts as separable when its second singular value is at most ``tol`` times the first (a single row
    or a single column always is).

    Parameters
    ----------
    kernel : 2-D array-like
        A ``(p, q)`` kernel, not identically zero.
    tol : float, default 1e-10
        The relative tolerance, ``tol ≥ 0``.

    Returns
    -------
    tuple or None
        ``(u, v)``, two 1-D ``numpy.ndarray`` of floats of lengths ``p`` and ``q``, or ``None`` when the kernel is not
        separable.

    Raises
    ------
    ValueError
        If the kernel is not 2-D, is empty or is identically zero, or if ``tol < 0``.

    Examples
    --------
    >>> u, v = separable_factors([[2, 1, -1], [4, 2, -2]])
    >>> np.round(u, 4), np.round(v, 4)
    (array([2.4495, 4.899 ]), array([ 0.8165,  0.4082, -0.4082]))
    >>> separable_factors([[0, 1, 0], [1, -4, 1], [0, 1, 0]]) is None
    True
    """
    try:
        M = np.array(kernel, dtype=float)
    except (TypeError, ValueError):
        raise ValueError(f"kernel must be a 2-D array of numbers, got {kernel!r}") from None
    if M.ndim != 2 or M.size == 0:
        raise ValueError(f"kernel must be a non-empty 2-D array, got shape {M.shape}")
    if not np.all(np.isfinite(M)):
        raise ValueError("the kernel must hold finite numbers")
    if not np.any(M != 0):
        raise ValueError("the kernel is identically zero: it has no factors")
    try:
        tol = float(tol)
    except (TypeError, ValueError):
        raise ValueError(f"tol must be a number >= 0, got {tol!r}") from None
    if not tol >= 0:
        raise ValueError(f"tol must be >= 0, got {tol!r}")
    _, sigma, Vt = np.linalg.svd(M, full_matrices=False)       # singular values in decreasing order
    if sigma.size > 1 and sigma[1] > tol * sigma[0]:           # relative test: rank 2 or more
        return None
    v = Vt[0].copy()                                           # the first right singular vector, ‖v‖ = 1
    v = v / np.sqrt(np.sum(v * v))
    first = np.flatnonzero(np.abs(v) > 1e-8)[0]                # exists: ‖v‖ = 1
    if v[first] < 0:
        v = -v
    u = M @ v
    return u, v
