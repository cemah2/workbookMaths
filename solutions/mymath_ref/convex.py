"""Convexity and separation: convex hull in the plane, linear separability, geometric margin (chapter M10).

Reference implementation of templates/mymath_stubs/convex.py (same signatures, same docstrings, which are the
specification). NumPy, and ``scipy.optimize.linprog`` for :func:`is_linearly_separable`; never ``scipy.spatial``.
"""

import numpy as np
from scipy.optimize import linprog


def _points(points, what="points"):
    """A copy of points as a 2-D array of floats with at least one row (ValueError otherwise)."""
    arr = np.array(points, dtype=float)
    if arr.ndim != 2 or arr.shape[0] == 0:
        raise ValueError(f"{what} must be a non-empty 2-D array, one point per row, got the shape {arr.shape}")
    return arr


def _labels(y, n):
    """A copy of y as a 1-D array of n labels, each -1 or +1 (ValueError otherwise)."""
    arr = np.array(y, dtype=float)
    if arr.ndim != 1 or arr.size != n:
        raise ValueError(f"y must hold one label per point ({n}), got the shape {arr.shape}")
    if not np.all((arr == 1) | (arr == -1)):
        raise ValueError(f"every label must be -1 or +1, got {sorted(set(arr.tolist()))}")
    return arr


def _cross(o, a, b):
    """The cross product (a - o) × (b - o): positive for a left turn o → a → b, zero when they are aligned."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

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
    P = _points(points)
    if P.shape[1] != 2:
        raise ValueError(f"points must have two columns (x, y), got the shape {P.shape}")
    pts = np.unique(P, axis=0)                 # distinct points, sorted by x, then by y
    if len(pts) == 1:
        return pts.copy()

    def half(sequence):
        chain = []
        for p in sequence:
            while len(chain) >= 2 and _cross(chain[-2], chain[-1], p) <= 0:
                chain.pop()                        # not a strict left turn: the last vertex is not a vertex
            chain.append(p)
        return chain

    lower, upper = half(pts), half(pts[::-1])
    return np.array(lower[:-1] + upper[:-1], dtype=float)   # each half ends where the other starts


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
    X_arr = _points(X, "X")
    labels = _labels(y, X_arr.shape[0])
    A_ub = -labels[:, None] * np.hstack([X_arr, np.ones((X_arr.shape[0], 1))])   # rows (-y_i x_i, -y_i)
    res = linprog(np.zeros(X_arr.shape[1] + 1), A_ub=A_ub, b_ub=-np.ones(X_arr.shape[0]),
                  bounds=(None, None), method="highs")
    return bool(res.status == 0)


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
    X_arr = _points(X, "X")
    labels = _labels(y, X_arr.shape[0])
    w_arr = np.array(w, dtype=float)
    if w_arr.ndim != 1 or w_arr.size != X_arr.shape[1]:
        raise ValueError(f"w must have one entry per coordinate ({X_arr.shape[1]}), got the shape {w_arr.shape}")
    norm = float(np.sqrt(np.sum(w_arr ** 2)))
    if norm == 0:
        raise ValueError("w must be a non-zero normal vector")
    return float(np.min(labels * (X_arr @ w_arr + float(b)))) / norm + 0.0
