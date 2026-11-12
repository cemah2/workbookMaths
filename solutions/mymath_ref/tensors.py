"""Tensors: ``einsum`` for two arrays written with loops, means and variances along chosen axes, and the
Horvitz-Thompson estimator of a total (chapter M20).

Reference implementation (solutions/mymath_ref).
NumPy is allowed, but not ``np.einsum``, ``np.tensordot``, ``np.matmul`` (nor ``@``), ``np.dot``, ``np.inner`` nor
``np.outer`` in ``einsum_pair``, nor ``np.var`` and ``np.std`` in ``moments_along_axes``: the tests compare your
results with them. Never modify the arrays you receive. Numbers are returned as Python ``float``, arrays as
``numpy.ndarray`` of floats.
"""

import itertools
import numbers

import numpy as np


def _float_array(values, what):
    """values as a NEW float array, or ValueError if they are not numbers."""
    try:
        return np.array(values, dtype=float)
    except (TypeError, ValueError):
        raise ValueError(f"{what} must be an array of numbers, got {values!r}") from None


def _letters(part, what):
    """The letters of one part of an einsum formula, checked: ASCII letters, each at most once."""
    if any(not (c.isascii() and c.isalpha()) for c in part):
        raise ValueError(f"the {what} {part!r} must contain letters only")
    if len(set(part)) != len(part):
        raise ValueError(f"a letter is repeated in the {what} {part!r}")
    return part



def einsum_pair(subscripts, a, b):
    """Return ``np.einsum(subscripts, a, b)``, computed with loops over every value of the indices.

    ``subscripts`` is written ``"ij,jk->ik"``: one letter per axis of ``a``, a comma, one letter per axis of ``b``,
    then ``->`` and the letters of the result (the explicit form, required here). A letter shared by ``a`` and ``b``
    is an index they share: the two axes must have the same length. A letter absent from the result is summed over;
    the others index the result, in the order written. The value of the result at an index is the sum, over all the
    values of the summed letters, of the products ``a[…] * b[…]``. The cost is the product of the lengths of all the
    letters.

    Restrictions of this exercise: a letter appears at most once in ``a`` and at most once in ``b`` (no trace inside
    one operand), and the letters of the result are distinct and appear in ``a`` or ``b``. An empty result (``"i,i->"``)
    is a 0-d array.

    Parameters
    ----------
    subscripts : str
        The formula, such as ``"ij,jk->ik"``; spaces are not allowed.
    a, b : array-like
        The two arrays.

    Returns
    -------
    numpy.ndarray
        The result, of floats, of the shape given by the letters after ``->``.

    Raises
    ------
    ValueError
        If the formula is malformed (no ``->``, not exactly one comma, a character that is not a letter), if the
        number of letters of an operand differs from its number of axes, if a letter is repeated in one operand or
        in the result, if a letter of the result appears in no operand, or if a shared letter has two lengths.

    Examples
    --------
    >>> einsum_pair("ij,jk->ik", [[1, 2], [3, 4]], [[1, 0], [1, 1]])
    array([[3., 2.],
           [7., 4.]])
    >>> einsum_pair("i,i->", [1, 2, 3], [4, 5, 6])
    array(32.)
    >>> einsum_pair("i,j->ij", [1, 2], [3, 4, 5])
    array([[ 3.,  4.,  5.],
           [ 6.,  8., 10.]])
    >>> einsum_pair("nij,njk->nik", np.ones((2, 2, 3)), np.ones((2, 3, 1))).shape
    (2, 2, 1)
    """
    if not isinstance(subscripts, str) or subscripts.count("->") != 1:
        raise ValueError(f"the formula must be written 'ij,jk->ik' (with one '->'), got {subscripts!r}")
    left, out = subscripts.split("->")
    if left.count(",") != 1:
        raise ValueError(f"the formula must have exactly one comma before '->', got {subscripts!r}")
    la, lb = left.split(",")
    la, lb = _letters(la, "first operand"), _letters(lb, "second operand")
    out = _letters(out, "result")
    A, B = _float_array(a, "a"), _float_array(b, "b")
    for letters, array, what in ((la, A, "a"), (lb, B, "b")):
        if len(letters) != array.ndim:
            raise ValueError(f"{what} has {array.ndim} axes but {len(letters)} letters {letters!r}")
    sizes = {}
    for letters, array in ((la, A), (lb, B)):
        for letter, length in zip(letters, array.shape):
            if sizes.setdefault(letter, length) != length:
                raise ValueError(f"the letter {letter!r} has two lengths, {sizes[letter]} and {length}")
    missing = [letter for letter in out if letter not in sizes]
    if missing:
        raise ValueError(f"the letters {missing} of the result appear in no operand")
    summed = [letter for letter in sizes if letter not in out]
    result = np.zeros(tuple(sizes[letter] for letter in out))
    for out_index in np.ndindex(*result.shape):
        value = dict(zip(out, out_index))
        total = 0.0
        for summed_index in itertools.product(*(range(sizes[letter]) for letter in summed)):
            value.update(zip(summed, summed_index))
            total += A[tuple(value[l] for l in la)] * B[tuple(value[l] for l in lb)]
        result[out_index] = total
    return result


def moments_along_axes(x, axes, ddof=0):
    """Return the mean and the variance of ``x`` along ``axes``, keeping the reduced axes with length 1.

    The values reduced together are those that differ only by their indices along ``axes``; there are ``N`` of them
    (the product of the lengths of these axes). The variance is ``Σ (x - mean)² / (N - ddof)``: ``ddof = 0`` for the
    mean of the squared deviations, ``ddof = 1`` for the unbiased estimator (M02c). Keeping the reduced axes (length
    1, like ``keepdims=True``) lets ``(x - mean) / sqrt(var)`` broadcast against ``x``. This function only computes
    the two moments: it does not center nor scale ``x``.

    Parameters
    ----------
    x : array-like
        An array of numbers, of any number of axes.
    axes : int or tuple of int
        The axes to reduce, distinct; negative values count from the end.
    ddof : int, default 0
        The correction, ``0 ≤ ddof < N``.

    Returns
    -------
    tuple
        ``(mean, var)``, two ``numpy.ndarray`` of floats of the same shape: that of ``x`` with length 1 along
        ``axes``.

    Raises
    ------
    ValueError
        If an axis is out of range or repeated, or if ``ddof`` is not an integer with ``0 ≤ ddof < N``.

    Examples
    --------
    >>> x = np.array([[1.0, 2.0, 6.0], [3.0, 2.0, 4.0]])
    >>> mean, var = moments_along_axes(x, axes=1)
    >>> mean
    array([[3.],
           [3.]])
    >>> var
    array([[4.66666667],
           [0.66666667]])
    >>> mean, var = moments_along_axes(x, axes=(0, 1), ddof=1)
    >>> mean.shape, float(var[0, 0])
    ((1, 1), 3.2)
    """
    values = _float_array(x, "x")
    raw = (axes,) if isinstance(axes, numbers.Integral) and not isinstance(axes, bool) else axes
    if not isinstance(raw, (tuple, list)) or any(
            isinstance(ax, bool) or not isinstance(ax, numbers.Integral) for ax in raw):
        raise ValueError(f"axes must be an integer or a tuple of integers, got {axes!r}")
    reduced = []
    for ax in raw:
        if not -values.ndim <= ax < values.ndim:
            raise ValueError(f"the axis {ax} is out of range for an array of {values.ndim} axes")
        reduced.append(int(ax) % values.ndim)
    if len(set(reduced)) != len(reduced):
        raise ValueError(f"an axis is repeated in {axes!r}")
    reduced = tuple(reduced)
    n = int(np.prod([values.shape[ax] for ax in reduced]))
    if isinstance(ddof, bool) or not isinstance(ddof, numbers.Integral) or not 0 <= ddof < n:
        raise ValueError(f"ddof must be an integer with 0 <= ddof < N = {n}, got {ddof!r}")
    mean = np.sum(values, axis=reduced, keepdims=True) / n
    var = np.sum((values - mean) ** 2, axis=reduced, keepdims=True) / (n - ddof)
    return mean, var


def horvitz_thompson_total(values, included, inclusion_probs):
    """Return the Horvitz-Thompson estimate ``Σ_{i in the sample} y_i / π_i`` of the total ``Σ y_i`` of a population.

    Unit ``i`` enters the sample with the probability ``π_i > 0`` (its indicator ``I_i`` follows a Bernoulli law of
    parameter ``π_i``). Since ``E[I_i y_i / π_i] = y_i``, the estimate is unbiased whatever the ``π_i``: a unit that
    had little chance to be drawn stands, when it is drawn, for the ``1 / π_i`` units it represents.

    Parameters
    ----------
    values : 1-D array-like
        The ``N`` values ``y_i`` (only those of the sample are used).
    included : 1-D array-like
        ``N`` booleans (or 0 and 1): whether unit ``i`` is in the sample.
    inclusion_probs : 1-D array-like
        The ``N`` probabilities ``π_i``, in ``]0, 1]``.

    Returns
    -------
    float
        The estimate of the total.

    Raises
    ------
    ValueError
        If the three arrays are not 1-D of the same length, if ``included`` holds something else than booleans or 0
        and 1, or if a probability is outside ``]0, 1]``.

    Examples
    --------
    >>> horvitz_thompson_total([3, 40, 2], [True, False, True], [0.125, 0.2, 0.0625])
    56.0
    >>> horvitz_thompson_total([3, 7], [1, 1], [1, 1])             # a census: the exact total
    10.0
    """
    y = _float_array(values, "values")
    pi = _float_array(inclusion_probs, "inclusion_probs")
    sample = np.asarray(included)
    if y.ndim != 1 or sample.ndim != 1 or pi.ndim != 1 or not y.shape == sample.shape == pi.shape:
        raise ValueError(f"values, included and inclusion_probs must be 1-D of the same length, got shapes "
                         f"{y.shape}, {sample.shape} and {pi.shape}")
    if sample.dtype != bool:
        if sample.dtype.kind not in "iuf" or not np.all((sample == 0) | (sample == 1)):
            raise ValueError(f"included must hold booleans or 0 and 1, got {included!r}")
        sample = sample == 1
    if not np.all((pi > 0) & (pi <= 1)):
        raise ValueError(f"every inclusion probability must be in ]0, 1], got {inclusion_probs!r}")
    return float(np.sum(y[sample] / pi[sample]))
