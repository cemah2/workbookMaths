"""Vectors and lines in the plane: coordinates, norm, dot product, angle, equations (chapter R9).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_r9_plane.py``.
Points and vectors are tuples of coordinates; the functions work in the plane and, unless stated otherwise, in
any dimension.
"""


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
    # TODO: end minus start, for each coordinate.
    raise NotImplementedError("vector() is not implemented yet")


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
    # TODO: Pythagoras, generalised to any number of coordinates.
    raise NotImplementedError("norm() is not implemented yet")


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
    # TODO: sum of the products of the coordinates.
    raise NotImplementedError("dot() is not implemented yet")


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
    # TODO: cos(angle) = dot / (norm × norm); rounding can give 1.0000000002: clamp to [-1, 1] before acos.
    raise NotImplementedError("angle_between() is not implemented yet")


def line_through(A, B):
    """Return a Cartesian equation ``a*x + b*y + c = 0`` of the line through two distinct points of the plane.

    Parameters
    ----------
    A, B : tuple of (float, float)
        Two distinct points of the plane.

    Returns
    -------
    tuple of (float, float, float)
        ``(a, b, c)`` with ``(a, b) != (0, 0)`` (ints when the coordinates are ints). Any non-zero multiple is also correct: the tests accept every
        equation of the line. Vertical lines are allowed.

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
    # TODO: a direction vector (dx, dy) gives a normal vector (−dy, dx); then c from point A.
    raise NotImplementedError("line_through() is not implemented yet")


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
    # TODO: 180 degrees is pi radians.
    raise NotImplementedError("deg_to_rad() is not implemented yet")
