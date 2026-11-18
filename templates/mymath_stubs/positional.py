"""Rotations of ℝⁿ and the online softmax: the matrix of a Givens rotation, the state of a softmax-weighted mean read
block by block, and the merge of two such states (chapter MB3).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_mb3_positional.py``.
NumPy and the module ``math`` are allowed, but no SciPy at all (``scipy.special.softmax``, ``scipy.special.logsumexp``,
``scipy.spatial.transform.Rotation``…) and not ``np.logaddexp``: the tests compare your results with them, and with the
matrices of MML (3.76)–(3.81). Never modify the arrays you receive. Matrices are returned as ``numpy.ndarray`` of
floats.

**The state of an online softmax.** For scores ``s_j`` and values ``v_j`` (numbers, or vectors of the same length),
the softmax-weighted mean is ``Σ_j p_j v_j`` with ``p_j = e^{s_j} / Σ_k e^{s_k}``. Reading the scores block by block,
one keeps the **state** ``(m, l, acc)`` of the scores read so far:

- ``m`` is the largest score read (``-inf`` before any finite score);
- ``l = Σ_j e^{s_j - m}`` (so ``l ≥ 1`` as soon as ``m`` is finite: the largest score contributes ``e^0 = 1``);
- ``acc = Σ_j e^{s_j - m} v_j`` (``None`` when there are no values).

Then ``acc / l`` is the weighted mean and ``m + ln l`` the log-sum-exp of the scores (M05a). A score ``-inf`` is a
masked score: its weight is 0. The **empty state** ``(-inf, 0.0, 0)``, with ``acc`` zero, is the state of no score
(or of masked scores only): it has no law, and ``acc / l`` is ``0 / 0``.

A state is a tuple ``(m, l, acc)``: ``m`` and ``l`` are Python ``float``; ``acc`` is ``None`` (no values), a Python
``float`` (one number per score) or a 1-D ``numpy.ndarray`` of ``k`` floats (a vector of length ``k`` per score).

Nothing here builds positions, frequencies, masks or encodings, nor rotates the rows of a table pair by pair: those are
the functions of workbookIA B3.
"""


def givens_rotation(n, i, j, theta):
    """Return the ``n × n`` matrix of the rotation by ``θ`` in the plane of the coordinates ``i`` and ``j``.

    It is the identity matrix, except four entries: ``G[i, i] = G[j, j] = cos θ``, ``G[j, i] = sin θ`` and
    ``G[i, j] = -sin θ``. It turns the basis vector ``e_i`` towards ``e_j``, ``G e_i = cos θ e_i + sin θ e_j`` and
    ``G e_j = -sin θ e_i + cos θ e_j``, and fixes the ``n - 2`` other basis vectors: in the plane of ``(x_i, x_j)``,
    it is the rotation ``R_θ`` of the plane (counterclockwise for ``θ > 0`` when ``x_i`` is drawn as the first
    axis). It is orthogonal, of determinant 1, and ``G⁻¹ = Gᵀ`` is the rotation by ``-θ`` in the same plane.

    Indices start at 0. MML (3.80)–(3.81) numbers the coordinates from 1 and takes ``i < j``: its ``R_ij(θ)`` is
    ``givens_rotation(n, i - 1, j - 1, θ)``. Here ``i > j`` is allowed too: swapping ``i`` and ``j`` changes ``θ``
    into ``-θ``, so ``givens_rotation(n, j, i, θ)`` is the transpose of ``givens_rotation(n, i, j, θ)``. For
    ``n = 2``, ``givens_rotation(2, 0, 1, θ)`` is ``R_θ`` (MML (3.76)).

    Parameters
    ----------
    n : int
        The dimension, an integer ``≥ 2`` (a NumPy integer is accepted; a ``bool``, or a float such as ``3.0``, is
        refused).
    i, j : int
        Two different coordinates, integers in ``[0, n - 1]``.
    theta : float
        The angle in radians, a finite real number (a ``bool`` is refused).

    Returns
    -------
    numpy.ndarray
        The ``(n, n)`` matrix, of floats.

    Raises
    ------
    ValueError
        If ``n`` is not an integer ``≥ 2``, if ``i`` or ``j`` is not an integer in ``[0, n - 1]`` or if ``i = j``,
        or if ``theta`` is not a finite real number.

    Examples
    --------
    >>> np.round(givens_rotation(4, 1, 3, np.pi / 3), 4)      # cos = 0.5, sin = √3/2 in the plane (x_1, x_3)
    array([[ 1.   ,  0.   ,  0.   ,  0.   ],
           [ 0.   ,  0.5  ,  0.   , -0.866],
           [ 0.   ,  0.   ,  1.   ,  0.   ],
           [ 0.   ,  0.866,  0.   ,  0.5  ]])
    >>> G = givens_rotation(3, 2, 0, 1.2)
    >>> np.allclose(G @ G.T, np.eye(3)), np.allclose(G, givens_rotation(3, 0, 2, -1.2))
    (True, True)
    """
    # TODO: check n, i, j and theta (integers, not bool; i != j; a finite angle); start from the identity
    #  (np.eye) and set the four entries of the plane (i, j); math.cos and math.sin, or np.cos and np.sin.
    raise NotImplementedError("givens_rotation() is not implemented yet")


def online_softmax(scores, values=None, block_size=1):
    """Return the state ``(m, l, acc)`` of the scores (and values) read by consecutive blocks of ``block_size``.

    The scores are read in order, by blocks of ``block_size`` (the last block may be shorter). Starting from the
    empty state ``(-inf, 0, 0)``, each block ``B`` updates the state: with ``m_new = max(m, max_{j∈B} s_j)``,

    - ``l ← l · e^{m - m_new} + Σ_{j∈B} e^{s_j - m_new}``,
    - ``acc ← acc · e^{m - m_new} + Σ_{j∈B} e^{s_j - m_new} v_j``,
    - ``m ← m_new``.

    The factor ``e^{m - m_new}`` rescales what was accumulated when the maximum changes (it is 1 otherwise, and
    ``e^{-inf} = 0`` at the first finite block); a block whose scores are all ``-inf`` leaves the state unchanged.
    After every block, ``l`` and ``acc`` are exactly the sums of the module docstring over the scores read (the
    invariant of MB3 §8): the final state does not depend on ``block_size``, up to rounding, and no exponential of a
    positive number is ever computed. From the final state, ``acc / l`` is the softmax-weighted mean of the values,
    ``m + ln l`` the log-sum-exp of the scores, and ``e^{s_j - m} / l`` the weight of score ``j``.

    Parameters
    ----------
    scores : 1-D array-like
        ``n ≥ 1`` real scores; ``-inf`` is allowed (a masked score), ``nan`` and ``+inf`` are refused.
    values : 1-D or 2-D array-like, optional
        ``n`` finite values, one per score: a 1-D array (a number per score) or a 2-D ``(n, k)`` array (a vector of
        length ``k ≥ 1`` per score). When omitted, ``acc`` is ``None``.
    block_size : int, default 1
        The number of scores read at once, an integer ``≥ 1`` (a NumPy integer is accepted; a ``bool`` or a float
        is refused); it may exceed ``n`` (a single block).

    Returns
    -------
    tuple
        ``(m, l, acc)``: two Python ``float``, and ``acc`` as described in the module docstring (``None``, a
        ``float``, or a 1-D array of ``k`` floats). If every score is ``-inf``, the empty state ``(-inf, 0.0, 0)``
        (``acc`` is then ``0.0``, a zero array, or ``None``).

    Raises
    ------
    ValueError
        If ``scores`` is not a non-empty 1-D array of real numbers, has a ``nan`` or a ``+inf``; if ``values`` does
        not have ``n`` rows, is not 1-D or 2-D, has no column, or has an entry that is not a finite number; or if
        ``block_size`` is not an integer ``≥ 1``.

    Examples
    --------
    >>> m, l, acc = online_softmax([0.0, np.log(4), np.log(2)], values=[10.0, 20.0, 40.0], block_size=2)
    >>> round(m, 6), round(l, 6), round(acc, 6)      # the weights e^{s - m} are 1/4, 1 and 1/2
    (1.386294, 1.75, 42.5)
    >>> round(acc / l, 4)                             # the softmax-weighted mean of the values
    24.2857
    >>> m, l, _ = online_softmax([-800.0, -801.0, -799.0])          # e^{-800} would underflow to 0
    >>> round(m + float(np.log(l)), 6)                              # the log-sum-exp
    -798.592394
    >>> online_softmax([-np.inf, -np.inf], values=[[1.0, 2.0], [3.0, 4.0]])   # every score masked: no law
    (-inf, 0.0, array([0., 0.]))
    """
    # TODO: check the arguments (float arrays); start from m = -inf, l = 0, acc = 0 (or None); for each block,
    #  skip it if all its scores are -inf, otherwise compute m_new, the factor e^(m - m_new) and the weights
    #  e^(s_j - m_new) of the block, then update l and acc; return Python floats (acc a float for 1-D values).
    raise NotImplementedError("online_softmax() is not implemented yet")


def merge_softmax_states(state1, state2):
    """Return the state of the union of two disjoint sets of scores, from their two states.

    With ``m = max(m₁, m₂)``, the merged state is ``(m, l₁ e^{m₁ - m} + l₂ e^{m₂ - m},
    acc₁ e^{m₁ - m} + acc₂ e^{m₂ - m})``: each state is first expressed relative to the common maximum. The merge is
    commutative and associative, and the empty state ``(-inf, 0, 0)`` is its neutral element: a long series of
    scores can be cut into pieces, each piece read separately (on another machine, say), and the states merged in any
    grouping. Reading a block after the others, in ``online_softmax``, is a merge with the state of that block.

    Parameters
    ----------
    state1, state2 : tuple
        Two states ``(m, l, acc)`` (see the module docstring), with ``acc`` of the same kind in both: both ``None``,
        both numbers, or both 1-D arrays of the same length. In a state, ``m`` is a real number or ``-inf`` (not
        ``nan`` nor ``+inf``), ``l`` is finite, ``l ≥ 1`` when ``m`` is finite, and ``l = 0`` and ``acc = 0`` when
        ``m = -inf``; ``acc`` is finite.

    Returns
    -------
    tuple
        The merged state ``(m, l, acc)``, with ``acc`` of the same kind as in the arguments (a new array: the
        arguments are not modified). The merge of two empty states is the empty state.

    Raises
    ------
    ValueError
        If a state is not a tuple of three elements satisfying the conditions above, or if the two ``acc`` are not
        of the same kind or length.

    Examples
    --------
    >>> m, l, acc = merge_softmax_states((0.0, 1.5, 3.0), (np.log(2), 1.0, 4.0))
    >>> round(m, 6), round(l, 6), round(acc, 6)      # the first state is rescaled by e^{-ln 2} = 1/2
    (0.693147, 1.75, 5.5)
    >>> merge_softmax_states((-np.inf, 0.0, None), (0.5, 1.25, None))     # the empty state is neutral
    (0.5, 1.25, None)
    >>> left = online_softmax([1.0, 3.0], values=[2.0, 6.0])
    >>> right = online_softmax([3.0, 0.0], values=[4.0, 5.0])
    >>> whole = online_softmax([1.0, 3.0, 3.0, 0.0], values=[2.0, 6.0, 4.0, 5.0])
    >>> np.allclose(merge_softmax_states(left, right), whole)
    True
    """
    # TODO: check both states and that their acc are of the same kind; two empty states give the empty state;
    #  otherwise express each state relative to m = max(m1, m2) (math.exp(-inf) is 0.0) and add them.
    raise NotImplementedError("merge_softmax_states() is not implemented yet")
