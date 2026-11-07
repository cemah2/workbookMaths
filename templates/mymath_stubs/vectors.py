"""Vectors of ℝⁿ: p-norms, cosine similarity, projection on a line, centroid, hyperplanes (chapter M07).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m07_vectors.py``.
NumPy is allowed (arrays, sums, ``np.abs``, ``np.sqrt``…), but not ``np.linalg.norm`` nor ``scipy.spatial``: the
tests compare your results with them. A vector is a 1-D array-like of numbers (list, tuple or array); a set of
points is a 2-D array-like, one point per row. Every number returned is a Python ``float`` (or ``int`` for a side),
every vector or table a ``numpy.ndarray`` of floats.
"""


def norm_p(x, p=2):
    """Return the p-norm ``‖x‖_p = (Σ |x_i|^p)^(1/p)`` of a vector, and ``max |x_i|`` for ``p = inf``.

    Parameters
    ----------
    x : 1-D array-like
        A non-empty vector.
    p : float, default 2
        At least 1; ``float("inf")`` (or ``numpy.inf``) gives the maximum norm L∞.

    Returns
    -------
    float
        Non-negative.

    Raises
    ------
    ValueError
        If ``x`` is empty or ``p < 1`` (below 1, the formula is not a norm).

    Examples
    --------
    >>> norm_p([3, -4])
    5.0
    >>> norm_p([3, -4], p=1)
    7.0
    >>> norm_p([3, -4], p=float("inf"))
    4.0
    """
    # TODO: three cases: p = inf (the largest absolute value), p = 1, and the general formula.
    raise NotImplementedError("norm_p() is not implemented yet")


def cosine_similarity(u, v):
    """Return the cosine similarity ``u · v / (‖u‖ ‖v‖)`` of two vectors of the same length.

    Parameters
    ----------
    u, v : 1-D array-like
        Two non-zero vectors of the same length.

    Returns
    -------
    float
        Between -1 and 1 (clip a value like 1.0000000000000002 caused by rounding).

    Raises
    ------
    ValueError
        If the lengths differ or if a vector is zero (its direction is not defined).

    Examples
    --------
    >>> round(cosine_similarity([1, 0], [1, 1]), 4)
    0.7071
    >>> cosine_similarity([1, 2, 2], [-2, -4, -4])
    -1.0
    >>> cosine_similarity([1, 0, 0], [0, 5, 0])
    0.0
    """
    # TODO: the dot product divided by the product of the two Euclidean norms, then np.clip to [-1, 1].
    raise NotImplementedError("cosine_similarity() is not implemented yet")


def project_onto_line(x, u):
    """Return the orthogonal projection of ``x`` on the line through the origin directed by ``u``.

    ``proj(x) = (x · u / u · u) u`` : the point of the line closest to ``x``; ``x - proj(x)`` is orthogonal to ``u``.

    Parameters
    ----------
    x, u : 1-D array-like
        Two vectors of the same length; ``u`` is not zero (it need not have norm 1).

    Returns
    -------
    numpy.ndarray
        A vector of floats, a multiple of ``u``.

    Raises
    ------
    ValueError
        If the lengths differ or if ``u`` is zero.

    Examples
    --------
    >>> project_onto_line([2, 3], [1, 0])
    array([2., 0.])
    >>> project_onto_line([1, 2], [1, 1])
    array([1.5, 1.5])
    >>> project_onto_line([1, 2], [3, 3])
    array([1.5, 1.5])
    """
    # TODO: the coefficient (x · u) / (u · u), then multiply u by it.
    raise NotImplementedError("project_onto_line() is not implemented yet")


def centroid(points, weights=None):
    """Return the centroid of the rows of ``points``: their mean, or the weighted mean ``Σ w_i x_i / Σ w_i``.

    Parameters
    ----------
    points : 2-D array-like
        At least one point, one per row.
    weights : 1-D array-like, optional
        One non-negative weight per point, with a positive sum; ``None`` gives every point the weight 1.

    Returns
    -------
    numpy.ndarray
        A vector of floats with one coordinate per column of ``points``.

    Raises
    ------
    ValueError
        If ``points`` is empty, or if the weights have the wrong length, a negative entry or a zero sum.

    Examples
    --------
    >>> centroid([[0, 0], [2, 0], [1, 3]])
    array([1., 1.])
    >>> centroid([[0, 0], [4, 0]], weights=[3, 1])
    array([1., 0.])
    """
    # TODO: multiply each row by its weight (broadcasting), add the rows (axis=0), divide by the sum of the weights.
    raise NotImplementedError("centroid() is not implemented yet")


def sum_sq_distances_to(points, c):
    """Return ``Σ_i ‖x_i - c‖²``, the sum of the squared Euclidean distances of the rows of ``points`` to ``c``.

    It is the inertia of the points around ``c``; it is smallest when ``c`` is their centroid.

    Parameters
    ----------
    points : 2-D array-like
        At least one point, one per row.
    c : 1-D array-like
        A point with one coordinate per column of ``points``.

    Returns
    -------
    float
        Non-negative.

    Raises
    ------
    ValueError
        If ``c`` does not have one coordinate per column of ``points``.

    Examples
    --------
    >>> sum_sq_distances_to([[0, 0], [2, 0], [1, 3]], [1, 1])
    8.0
    >>> sum_sq_distances_to([[0, 0], [2, 0], [1, 3]], [0, 0])
    14.0
    """
    # TODO: subtract c from every row (broadcasting), square, add everything.
    raise NotImplementedError("sum_sq_distances_to() is not implemented yet")


def side_of_hyperplane(x, w, b):
    """Return the side of the hyperplane ``w · x + b = 0`` where each point lies: the sign of ``w · x + b``.

    1 on the side the normal vector ``w`` points to, -1 on the other side, 0 on the hyperplane (exactly: no
    tolerance).

    Parameters
    ----------
    x : 1-D or 2-D array-like
        One point (1-D) or several points, one per row (2-D).
    w : 1-D array-like
        A non-zero normal vector, with one coordinate per coordinate of a point.
    b : float
        The offset.

    Returns
    -------
    int or numpy.ndarray
        A Python ``int`` for one point; an array of ints (one per row) for several points.

    Raises
    ------
    ValueError
        If ``w`` is zero or if its length does not match the points.

    Examples
    --------
    >>> side_of_hyperplane([3, 0], [1, 1], -2)
    1
    >>> side_of_hyperplane([[1, 1], [0, 0], [3, 0]], [1, 1], -2)
    array([ 0, -1,  1])
    """
    # TODO: np.sign of the scores w · x + b; for 2-D input, all the scores at once (one dot product per row).
    raise NotImplementedError("side_of_hyperplane() is not implemented yet")


def distance_to_hyperplane(x, w, b, signed=False):
    """Return the distance from each point to the hyperplane ``w · x + b = 0``: ``|w · x + b| / ‖w‖``.

    With ``signed=True``, the signed distance ``(w · x + b) / ‖w‖``: positive on the side ``w`` points to.

    Parameters
    ----------
    x : 1-D or 2-D array-like
        One point (1-D) or several points, one per row (2-D).
    w : 1-D array-like
        A non-zero normal vector (it need not have norm 1).
    b : float
        The offset.
    signed : bool, default False
        Keep the sign of ``w · x + b``.

    Returns
    -------
    float or numpy.ndarray
        A Python ``float`` for one point; an array of floats (one per row) for several points.

    Raises
    ------
    ValueError
        If ``w`` is zero or if its length does not match the points.

    Examples
    --------
    >>> distance_to_hyperplane([3, 4], [3, 4], 0)
    5.0
    >>> round(distance_to_hyperplane([0, 0], [1, 1], -2, signed=True), 4)
    -1.4142
    >>> distance_to_hyperplane([[0, 1], [2, 5]], [0, 2], -2)
    array([0., 4.])
    """
    # TODO: the scores w · x + b divided by the Euclidean norm of w; np.abs unless signed.
    raise NotImplementedError("distance_to_hyperplane() is not implemented yet")
