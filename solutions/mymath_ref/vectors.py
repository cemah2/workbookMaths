"""Vectors of ℝⁿ: p-norms, cosine similarity, projection on a line, centroid, hyperplanes (chapter M07).

Reference implementation (solutions/mymath_ref).
NumPy is allowed (arrays, sums, ``np.abs``, ``np.sqrt``…), but not ``np.linalg.norm`` nor ``scipy.spatial``: the
tests compare your results with them. A vector is a 1-D array-like of numbers (list, tuple or array); a set of
points is a 2-D array-like, one point per row. Every number returned is a Python ``float`` (or ``int`` for a side),
every vector or table a ``numpy.ndarray`` of floats.
"""

import math

import numpy as np


def _vector(x, what="x"):
    """x as a 1-D array of floats, after checking that it is a non-empty vector (ValueError otherwise)."""
    arr = np.array(x, dtype=float)
    if arr.ndim != 1 or arr.size == 0:
        raise ValueError(f"{what} must be a non-empty 1-D vector, got shape {arr.shape}")
    return arr


def _points(points, what="points"):
    """points as a 2-D array of floats, one point per row, at least one point (ValueError otherwise)."""
    arr = np.array(points, dtype=float)
    if arr.ndim != 2 or arr.shape[0] == 0 or arr.shape[1] == 0:
        raise ValueError(f"{what} must be a non-empty 2-D table, one point per row, got shape {arr.shape}")
    return arr


def _scores(x, w, b):
    """(w · x + b for one point or each row, the normal vector w, True for one point), after the checks."""
    w = _vector(w, "w")
    if not np.any(w):
        raise ValueError("the normal vector w of a hyperplane cannot be zero")
    pts = np.array(x, dtype=float)
    if pts.ndim not in (1, 2) or pts.shape[-1] != w.size:
        raise ValueError(f"each point must have {w.size} coordinates (one per coordinate of w), got shape {pts.shape}")
    return np.sum(pts * w, axis=-1) + float(b), w, pts.ndim == 1


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
    x = _vector(x)
    if not p >= 1:                                  # also refuses nan
        raise ValueError(f"p must be at least 1 (below 1 the formula is not a norm), got {p!r}")
    a = np.abs(x)
    if math.isinf(p):
        return float(np.max(a)) + 0.0
    if p == 1:
        return float(np.sum(a)) + 0.0
    m = float(np.max(a))
    if m == 0:
        return 0.0
    return float(m * np.sum((a / m) ** p) ** (1 / p))   # scaled by the largest entry: no overflow


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
    u, v = _vector(u, "u"), _vector(v, "v")
    if u.size != v.size:
        raise ValueError(f"u and v must have the same length, got {u.size} and {v.size}")
    nu, nv = math.sqrt(float(np.sum(u * u))), math.sqrt(float(np.sum(v * v)))
    if nu == 0 or nv == 0:
        raise ValueError("the cosine similarity of a zero vector is not defined (it has no direction)")
    return float(np.clip(np.sum(u * v) / (nu * nv), -1.0, 1.0)) + 0.0


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
    x, u = _vector(x), _vector(u, "u")
    if x.size != u.size:
        raise ValueError(f"x and u must have the same length, got {x.size} and {u.size}")
    uu = float(np.sum(u * u))
    if uu == 0:
        raise ValueError("u cannot be zero: it gives no direction")
    return (float(np.sum(x * u)) / uu) * u + 0.0


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
    pts = _points(points)
    if weights is None:
        w = np.ones(pts.shape[0])
    else:
        w = np.array(weights, dtype=float)
        if w.shape != (pts.shape[0],):
            raise ValueError(f"one weight per point is needed: {pts.shape[0]} points, weights of shape {w.shape}")
        if not np.all(w >= 0):                      # also refuses nan
            raise ValueError("the weights must be non-negative")
        if not w.sum() > 0:
            raise ValueError("the sum of the weights must be positive")
    return np.sum(w[:, None] * pts, axis=0) / w.sum() + 0.0


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
    pts, c = _points(points), _vector(c, "c")
    if c.size != pts.shape[1]:
        raise ValueError(f"c must have one coordinate per column of points ({pts.shape[1]}), got {c.size}")
    return float(np.sum((pts - c) ** 2)) + 0.0


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
    scores, _, single = _scores(x, w, b)
    sides = np.sign(scores).astype(int)
    return int(sides) if single else sides


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
    scores, w, single = _scores(x, w, b)
    d = scores / math.sqrt(float(np.sum(w * w)))
    if not signed:
        d = np.abs(d)
    return float(d) + 0.0 if single else d + 0.0
