"""Vectors and lines in the plane: coordinates, norm, dot product, angle, equations (chapter R9).

Reference implementation (same signatures as ``templates/mymath_stubs/plane.py``): plain Python and the ``math``
module, as in every chapter from R0 to R9.
"""

import math


def vector(A, B):
    """Return the coordinates of the vector from point ``A`` to point ``B``.

    Parameters
    ----------
    A, B : tuple of float
        Points with the same number of coordinates.

    Returns
    -------
    tuple of float
        ``B - A``, coordinate by coordinate.

    Raises
    ------
    ValueError
        If the points do not have the same dimension.

    Examples
    --------
    >>> vector((1, 2), (4, 6))
    (3, 4)
    """
    if len(A) != len(B):
        raise ValueError(f"the points have different dimensions: {len(A)} and {len(B)}")
    return tuple(b - a for a, b in zip(A, B))


def norm(u):
    """Return the length (Euclidean norm) of the vector ``u``.

    Parameters
    ----------
    u : tuple of float

    Returns
    -------
    float

    Examples
    --------
    >>> norm((3, 4))
    5.0
    """
    total = 0
    for x in u:
        total += x * x
    return math.sqrt(total)


def dot(u, v):
    """Return the dot product of ``u`` and ``v``.

    Parameters
    ----------
    u, v : tuple of float
        Same dimension.

    Returns
    -------
    int or float
        An int when the coordinates are ints.

    Raises
    ------
    ValueError
        If the dimensions differ.

    Examples
    --------
    >>> dot((1, 2), (3, -1))
    1
    """
    if len(u) != len(v):
        raise ValueError(f"the vectors have different dimensions: {len(u)} and {len(v)}")
    total = 0
    for x, y in zip(u, v):
        total += x * y
    return total


def angle_between(u, v):
    """Return the angle between two non-zero vectors, in radians.

    Parameters
    ----------
    u, v : tuple of float
        Non-zero vectors of the same dimension.

    Returns
    -------
    float
        An angle in ``[0, pi]``, computed with ``math.acos`` (the reciprocal of cos on ``[0, pi]``).

    Raises
    ------
    ValueError
        If one of the vectors is zero.

    Examples
    --------
    >>> import math
    >>> round(angle_between((1, 0), (0, 2)), 12) == round(math.pi / 2, 12)
    True
    """
    length_u, length_v = norm(u), norm(v)
    if length_u == 0 or length_v == 0:
        raise ValueError("the angle with a zero vector is not defined")
    cosine = dot(u, v) / (length_u * length_v)
    cosine = max(-1.0, min(1.0, cosine))            # 1.0000000000000002 would make acos fail
    return math.acos(cosine)


def line_through(A, B):
    """Return a Cartesian equation ``a*x + b*y + c = 0`` of the line through two distinct points of the plane.

    Parameters
    ----------
    A, B : tuple of (float, float)
        Two distinct points of the plane.

    Returns
    -------
    tuple of (float, float, float)
        ``(a, b, c)`` with ``(a, b) != (0, 0)`` (ints when the coordinates are ints). Any non-zero multiple is also
        correct: the tests accept every equation of the line. Vertical lines are allowed.

    Raises
    ------
    ValueError
        If ``A == B``.

    Examples
    --------
    >>> a, b, c = line_through((0, 1), (1, 3))
    >>> a * 2 + b * 5 + c   # the point (2, 5) is on the line
    0
    """
    (xa, ya), (xb, yb) = A, B
    dx, dy = xb - xa, yb - ya
    if dx == 0 and dy == 0:
        raise ValueError("two distinct points are needed to define a line")
    a, b = -dy, dx                                   # a normal vector: the direction turned by a quarter turn
    c = -(a * xa + b * ya)
    return a, b, c


def deg_to_rad(degrees):
    """Convert an angle from degrees to radians.

    Parameters
    ----------
    degrees : float

    Returns
    -------
    float

    Examples
    --------
    >>> import math
    >>> deg_to_rad(180) == math.pi
    True
    """
    return degrees * math.pi / 180
