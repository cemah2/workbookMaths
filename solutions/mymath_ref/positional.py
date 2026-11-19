"""Rotations of ℝⁿ and the online softmax: the matrix of a Givens rotation, the state of a softmax-weighted mean read
block by block, and the merge of two such states (chapter MB3).

Reference implementation (solutions/mymath_ref).
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
masked score: its weight is 0. The **empty state** is ``(-inf, 0.0, acc0)``, with ``acc0`` ``None`` (no values),
``0.0`` (one number per score) or a zero array of length ``k``: it is the state of no score (or of masked scores
only), it has no law, and ``acc / l`` is ``0 / 0``.

A state is a tuple ``(m, l, acc)``: ``m`` and ``l`` are Python ``float``; ``acc`` is ``None`` (no values), a Python
``float`` (one number per score) or a 1-D ``numpy.ndarray`` of ``k`` floats (a vector of length ``k`` per score).

Nothing here builds positions, frequencies, masks or encodings, nor rotates the rows of a table pair by pair: those are
the functions of workbookIA B3.
"""

import math
import numbers

import numpy as np


def _is_bool(value):
    """Whether value is a bool or a NumPy bool (True == 1, but a bool is not a number here)."""
    return isinstance(value, (bool, np.bool_))


def _integer(value, what, low, high=None):
    """value as a Python int in [low, high] (a Python or NumPy integer; a bool or a float is refused), or ValueError."""
    if _is_bool(value) or not isinstance(value, numbers.Integral):
        raise ValueError(f"{what} must be an integer (not a bool, not a float such as 3.0), got {value!r}")
    value = int(value)
    if value < low or (high is not None and value > high):
        bounds = f"≥ {low}" if high is None else f"in [{low}, {high}]"
        raise ValueError(f"{what} must be an integer {bounds}, got {value!r}")
    return value


def _real(value, what):
    """value as a Python float if it is a real number (Python or NumPy; not a bool, not a string), or ValueError.
    Infinite values and nan are returned as they are: the callers decide."""
    if _is_bool(value) or not isinstance(value, numbers.Real):
        raise ValueError(f"{what} must be a real number (not a bool), got {value!r}")
    try:
        return float(value)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(f"{what} must be a real number, got {value!r}") from None


def _real_array(values, what):
    """values as a NEW float array (never a view of what was received), or ValueError; booleans, strings and complex
    numbers are refused."""
    try:
        raw = np.asarray(values)
    except (TypeError, ValueError):             # a ragged list
        raise ValueError(f"{what} must be an array of real numbers, got {values!r}") from None
    if raw.dtype.kind in "bcUSaV" or _is_bool(values):
        raise ValueError(f"{what} must hold real numbers (not booleans, strings or complex numbers), got {values!r}")
    try:
        return np.array(raw, dtype=float)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(f"{what} must be an array of real numbers, got {values!r}") from None


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
    n = _integer(n, "n", 2)
    i = _integer(i, "i", 0, n - 1)
    j = _integer(j, "j", 0, n - 1)
    if i == j:
        raise ValueError(f"i and j must be two different coordinates, got i = j = {i}")
    angle = _real(theta, "theta")
    if not math.isfinite(angle):
        raise ValueError(f"theta must be a finite angle (in radians), got {theta!r}")
    c, s = math.cos(angle), math.sin(angle)
    G = np.eye(n)
    G[i, i] = c
    G[j, j] = c
    G[j, i] = s                                 # the column i is G e_i = cos θ e_i + sin θ e_j
    G[i, j] = -s                                # the column j is G e_j = -sin θ e_i + cos θ e_j
    return G


def _scores(scores):
    """The scores as a new 1-D float array of n ≥ 1 entries, -inf allowed, nan and +inf refused."""
    s = _real_array(scores, "scores")
    if s.ndim != 1 or s.size == 0:
        raise ValueError(f"scores must be a non-empty 1-D array of real numbers, got shape {s.shape}")
    if np.isnan(s).any() or np.isposinf(s).any():
        raise ValueError("scores must not hold nan nor +inf (-inf is a masked score)")
    return s


def _values(values, n):
    """The values as a new float array of shape (n,) or (n, k), k ≥ 1, finite entries."""
    V = _real_array(values, "values")
    if V.ndim not in (1, 2):
        raise ValueError(f"values must be a 1-D or a 2-D array (one number or one vector per score), got shape "
                         f"{V.shape}")
    if V.shape[0] != n:
        raise ValueError(f"values must have one row per score (n = {n}), got shape {V.shape}")
    if V.ndim == 2 and V.shape[1] == 0:
        raise ValueError(f"values must have at least one column, got shape {V.shape}")
    if not np.all(np.isfinite(V)):
        raise ValueError("values must hold finite numbers only (no nan, no inf)")
    return V


def _copy(state):
    """The state with its own acc (a copy of an array)."""
    m, l, acc = state
    return m, l, acc.copy() if isinstance(acc, np.ndarray) else acc


def online_softmax(scores, values=None, block_size=1, history=False):
    """Return the state ``(m, l, acc)`` of the scores (and values) read by consecutive blocks of ``block_size``.

    The scores are read in order, by blocks of ``block_size`` (the last block may be shorter). Starting from the
    empty state, each block ``B`` updates the state: with ``m_new = max(m, max_{j∈B} s_j)``,

    - ``l ← l · e^{m - m_new} + Σ_{j∈B} e^{s_j - m_new}``,
    - ``acc ← acc · e^{m - m_new} + Σ_{j∈B} e^{s_j - m_new} v_j``,
    - ``m ← m_new``.

    The factor ``e^{m - m_new}`` rescales what was accumulated when the maximum changes (it is 1 otherwise, and
    ``e^{-inf} = 0`` at the first finite block); a block whose scores are all ``-inf`` leaves the state unchanged.
    After every block, ``l`` and ``acc`` are exactly the sums of the module docstring over the scores read (the
    invariant of MB3 §8): the final state does not depend on ``block_size``, up to rounding, and no exponential of a
    positive number is ever computed. From the final state, ``acc / l`` is the softmax-weighted mean of the values,
    ``m + ln l`` the log-sum-exp of the scores, and ``e^{s_j - m} / l`` the weight of score ``j``.

    If ``history`` is true, return the list of the states after each block instead (its last element is the final
    state): ``⌈n / block_size⌉`` states, the ``b``-th being the state of the first ``b · block_size`` scores (the
    invariant). A block whose scores are all ``-inf`` repeats the previous state. After the first finite block, what
    was accumulated is rescaled exactly when ``m`` changes from one state to the next.

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
    history : bool, default False
        Return the state after every block (a list), instead of the final state only.

    Returns
    -------
    tuple or list of tuples
        ``(m, l, acc)``: two Python ``float``, and ``acc`` as described in the module docstring (``None``, a
        ``float``, or a 1-D array of ``k`` floats). If every score is ``-inf``, the empty state of that kind (module
        docstring). With ``history=True``, the list of the ``⌈n / block_size⌉`` states after each block, each with
        its own ``acc`` (no array is shared between two states).

    Raises
    ------
    ValueError
        If ``scores`` is not a non-empty 1-D array of real numbers, has a ``nan`` or a ``+inf``; if ``values`` does
        not have ``n`` rows, is not 1-D or 2-D, has no column, or has an entry that is not a finite number; if
        ``block_size`` is not an integer ``≥ 1``; or if ``history`` is not a ``bool``.

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
    >>> states = online_softmax([0.5, 0.0, 2.0, 1.0, 4.0], block_size=2, history=True)    # three blocks
    >>> [(m, round(l, 4)) for m, l, _ in states]       # m changes twice: two rescalings
    [(0.5, 1.6065), (2.0, 1.7263), (4.0, 1.2336)]
    """
    s = _scores(scores)
    n = s.size
    V = None if values is None else _values(values, n)
    size = _integer(block_size, "block_size", 1)
    if not _is_bool(history):
        raise ValueError(f"history must be a bool (True or False), got {history!r}")

    m, l = -math.inf, 0.0                       # the empty state
    acc = None if V is None else 0.0 if V.ndim == 1 else np.zeros(V.shape[1])
    states = []
    for start in range(0, n, size):
        block = s[start:start + size]
        top = float(block.max())
        if top > -math.inf:                     # a block whose scores are all -inf leaves the state unchanged
            m_new = max(m, top)
            rescale = math.exp(m - m_new)       # e^{m - m_new} ≤ 1: 1 if the maximum did not change, 0 at first
            weights = np.exp(block - m_new)     # e^{s_j - m_new} ≤ 1, 0 for a masked score
            l = l * rescale + float(weights.sum())
            if V is not None:
                contribution = weights @ V[start:start + size]
                acc = acc * rescale + (float(contribution) if V.ndim == 1 else contribution)
            m = m_new
        if history:
            states.append(_copy((m, l, acc)))
    return states if history else (m, l, acc)


def _state(state, what):
    """(m, l, kind, acc) of a state, acc a Python float or a NEW float array; ValueError if it is not a state."""
    if not isinstance(state, tuple) or len(state) != 3:
        raise ValueError(f"{what} must be a tuple (m, l, acc) of three elements, got {state!r}")
    m, l, acc = state
    m = _real(m, f"m of {what}")
    if math.isnan(m) or m == math.inf:
        raise ValueError(f"m of {what} must be a real number or -inf (not nan nor +inf), got {m!r}")
    l = _real(l, f"l of {what}")
    if not math.isfinite(l):
        raise ValueError(f"l of {what} must be finite, got {l!r}")
    if acc is None:
        kind = None
    elif isinstance(acc, numbers.Real) and not _is_bool(acc):
        kind, acc = "number", _real(acc, f"acc of {what}")
    else:
        acc = _real_array(acc, f"acc of {what}")
        if acc.ndim != 1:
            raise ValueError(f"acc of {what} must be None, a number or a 1-D array, got shape {acc.shape}")
        kind = "array"
    if kind is not None and not np.all(np.isfinite(acc)):
        raise ValueError(f"acc of {what} must be finite, got {acc!r}")
    if m == -math.inf:
        if l != 0 or (kind is not None and np.any(acc != 0)):
            raise ValueError(f"{what} has m = -inf (no score): l must be 0 and acc zero (or None), got l = {l!r} and "
                             f"acc = {acc!r}")
    elif l < 1:
        raise ValueError(f"{what} has a finite m: l must be ≥ 1 (the largest score contributes e^0 = 1), got {l!r}")
    return m, l, kind, acc


def merge_softmax_states(state1, state2):
    """Return the state of the union of two disjoint sets of scores, from their two states.

    With ``m = max(m₁, m₂)``, the merged state is ``(m, l₁ e^{m₁ - m} + l₂ e^{m₂ - m},
    acc₁ e^{m₁ - m} + acc₂ e^{m₂ - m})``: each state is first expressed relative to the common maximum. The merge is
    commutative and associative, and the empty state of the same kind is its neutral element: a long series of
    scores can be cut into pieces, each piece read separately (on another machine, say), and the states merged in any
    grouping. Reading a block after the others, in ``online_softmax``, is a merge with the state of that block.

    Parameters
    ----------
    state1, state2 : tuple
        Two states ``(m, l, acc)`` (see the module docstring), with ``acc`` of the same kind in both: both ``None``,
        both numbers, or both 1-D arrays of the same length. In a state, ``m`` is a real number or ``-inf`` (not
        ``nan`` nor ``+inf``), ``l`` is finite, ``l ≥ 1`` when ``m`` is finite, and ``l = 0`` and ``acc`` zero (or
        ``None``) when ``m = -inf``; ``acc`` is finite.

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
    m1, l1, kind1, acc1 = _state(state1, "state1")
    m2, l2, kind2, acc2 = _state(state2, "state2")
    if kind1 != kind2:
        raise ValueError(f"the two acc must be of the same kind (both None, both numbers or both 1-D arrays), got "
                         f"{kind1 or 'None'} and {kind2 or 'None'}")
    if kind1 == "array" and acc1.shape != acc2.shape:
        raise ValueError(f"the two acc must have the same length, got {acc1.size} and {acc2.size}")
    m = max(m1, m2)
    if m == -math.inf:                          # two empty states: the empty state of that kind
        return -math.inf, 0.0, None if kind1 is None else 0.0 if kind1 == "number" else np.zeros(acc1.shape)
    f1, f2 = math.exp(m1 - m), math.exp(m2 - m)     # both ≤ 1: one is 1, the other e^{-|m₁ - m₂|} (0 for -inf)
    l = l1 * f1 + l2 * f2
    acc = None if kind1 is None else acc1 * f1 + acc2 * f2
    return m, l, acc
