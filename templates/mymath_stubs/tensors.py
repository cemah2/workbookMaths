"""Tensors: ``einsum`` for two arrays written with loops, means and variances along chosen axes, and the
Horvitz-Thompson estimator of a total (chapter M20).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m20_tensors.py``.
NumPy is allowed, but not ``np.einsum``, ``np.tensordot``, ``np.matmul`` (nor ``@``), ``np.dot``, ``np.inner`` nor
``np.outer`` in ``einsum_pair``, nor ``np.var`` and ``np.std`` in ``moments_along_axes``: the tests compare your
results with them. Never modify the arrays you receive. Numbers are returned as Python ``float``, arrays as
``numpy.ndarray`` of floats.
"""


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
    # TODO: parse and check the formula; the length of each letter; for each index of the result (np.ndindex),
    #  add up a[...] * b[...] over every value of the summed letters (itertools.product of ranges).
    raise NotImplementedError("einsum_pair() is not implemented yet")


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
    # TODO: normalize the axes (a tuple, negatives counted from the end), check them and ddof; N; the mean
    #  (np.sum with keepdims=True, divided by N), then the sum of the squared deviations divided by N - ddof.
    raise NotImplementedError("moments_along_axes() is not implemented yet")


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
    # TODO: check the three arrays, then the sum of values / probabilities over the units of the sample.
    raise NotImplementedError("horvitz_thompson_total() is not implemented yet")
