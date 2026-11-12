"""Convolution of sequences and kernels: the convolution of two sequences in three modes, the Toeplitz matrix of a
convolution, the circular convolution of two periodic sequences, the equivalent kernel of a stack of strided sums,
and the two factors of a separable 2-D kernel (chapter M21).

Two conventions meet here: ``convolve``, ``toeplitz_matrix`` and ``circular_convolve`` compute the convolution of
the mathematicians, which flips the kernel (``Σ_i a[i] b[k - i]``), while ``equivalent_kernel`` describes the
sliding sums of the libraries, which do not flip it (``Σ_u w[u] x[s i + u]``).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m21_convolution.py``.
NumPy is allowed, but not ``np.convolve``, ``np.correlate``, ``np.polymul``, ``np.polynomial`` nor ``np.fft``, and
no SciPy at all (``scipy.signal``, ``scipy.ndimage``, ``scipy.linalg.toeplitz``, ``convolution_matrix``,
``circulant``…): the tests compare your results with them. From ``np.linalg``, only ``svd``, in
``separable_factors`` (M12d). Never modify the arrays you receive. Sequences and matrices are returned as
``numpy.ndarray`` of floats, integers as Python ``int``.
"""


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
    # TODO: check the inputs; the full convolution (a double loop, or a loop over b adding b[j] * a in a shifted
    #  slice); then cut the "valid" or "same" part.
    raise NotImplementedError("convolve() is not implemented yet")


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
    # TODO: check the inputs; the full matrix, of shape (n + k - 1, n), with the kernel in column j from row j on;
    #  then keep the rows of the chosen mode (the same rows as in convolve).
    raise NotImplementedError("toeplitz_matrix() is not implemented yet")


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
    # TODO: check the inputs; for each k, add up a[i] * b[(k - i) % n].
    raise NotImplementedError("circular_convolve() is not implemented yet")


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
    # TODO: check the inputs; start from K = [1.0] and S = 1; for each stage, the kernel w spread with S - 1 zeros
    #  between its coefficients, convolved with K (with your convolve); then S = S * s.
    raise NotImplementedError("equivalent_kernel() is not implemented yet")


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
    # TODO: check the inputs; the singular values (np.linalg.svd); if the second one is too large, None; otherwise v
    #  is the first right singular vector, with the sign convention, and u = kernel @ v.
    raise NotImplementedError("separable_factors() is not implemented yet")
