"""Convexity and separation: convex hull in the plane, linear separability, geometric margin (chapter M10).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m10_convex.py``.
NumPy is allowed, and ``scipy.optimize.linprog`` for :func:`is_linearly_separable`; ``scipy.spatial`` is not: the
tests compare your hull with ``scipy.spatial.ConvexHull``. Points are given as a 2-D array-like, one point per row;
labels are -1 or +1. Numbers are returned as Python ``float`` or ``bool``, sets of points as ``numpy.ndarray`` of
floats.
"""


def convex_hull_2d(points):
    """Return the vertices of the convex hull of points of the plane, in counterclockwise order.

    Andrew's monotone chain: sort the distinct points by x, then by y; build the lower hull from left to right and
    the upper hull from right to left, removing the last vertex as long as it does not make a strict left turn
    (cross product ``(a - o) × (b - o) ≤ 0``). The first vertex is the smallest point in that order (smallest x, then
    smallest y). Points in the middle of an edge are not vertices.

    Parameters
    ----------
    points : 2-D array-like
        At least one point, two coordinates per row; repeated points are allowed.

    Returns
    -------
    numpy.ndarray
        The ``(h, 2)`` array of the vertices. With one distinct point, that point; with points all on one line, the
        two ends of the segment.

    Raises
    ------
    ValueError
        If ``points`` is empty or does not have two columns.

    Examples
    --------
    >>> convex_hull_2d([[0, 0], [2, 0], [1, 1], [2, 2], [0, 2], [1, 0]])
    array([[0., 0.],
           [2., 0.],
           [2., 2.],
           [0., 2.]])
    >>> convex_hull_2d([[3, 1], [1, 1], [2, 1]])
    array([[1., 1.],
           [3., 1.]])
    """
    # TODO: a helper cross(o, a, b), the sorted distinct points, the two half-hulls, then join them.
    raise NotImplementedError("convex_hull_2d() is not implemented yet")


def is_linearly_separable(X, y):
    """Return True if a hyperplane strictly separates the points labelled +1 from those labelled -1.

    The points are separable if and only if some ``(w, b)`` satisfies ``y_i (w · x_i + b) ≥ 1`` for every ``i``
    (scale any strict separator to reach 1). Decide it with ``scipy.optimize.linprog``: the unknowns are ``w`` and
    ``b``, the objective is zero, the constraints ``-y_i (w · x_i + b) ≤ -1`` are linear, every unknown is free
    (``bounds=(None, None)``); the points are separable if and only if the problem is feasible (``res.status == 0``).

    Parameters
    ----------
    X : 2-D array-like
        At least one point, one per row, in any dimension.
    y : 1-D array-like
        One label per point, each -1 or +1.

    Returns
    -------
    bool
        True also when every point has the same label.

    Raises
    ------
    ValueError
        If the lengths differ or a label is neither -1 nor +1.

    Examples
    --------
    >>> is_linearly_separable([[0, 0], [1, 1]], [-1, 1])
    True
    >>> is_linearly_separable([[0], [1], [2]], [1, -1, 1])
    False
    """
    # TODO: the matrix of the constraints, one row (-y_i x_i, -y_i) per point, then linprog.
    raise NotImplementedError("is_linearly_separable() is not implemented yet")


def margin_of_separator(X, y, w, b):
    """Return the geometric margin of the hyperplane ``w · x + b = 0`` on labelled points.

    ``min_i y_i (w · x_i + b) / ‖w‖`` : the signed distance of the worst-placed point to the hyperplane, positive when
    every point is on the side of its label, negative or zero otherwise.

    Parameters
    ----------
    X : 2-D array-like
        At least one point, one per row.
    y : 1-D array-like
        One label per point, each -1 or +1.
    w : 1-D array-like
        A non-zero normal vector.
    b : float
        The offset.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If the lengths do not match, if a label is neither -1 nor +1, or if ``w`` is zero.

    Examples
    --------
    >>> round(margin_of_separator([[0, 0], [2, 2]], [-1, 1], [1, 1], -2), 4)
    1.4142
    >>> margin_of_separator([[0, 0], [2, 2]], [1, 1], [0, 1], -1)
    -1.0
    """
    # TODO: the scores X w + b, multiplied by y, divided by the norm of w, then the minimum.
    raise NotImplementedError("margin_of_separator() is not implemented yet")
