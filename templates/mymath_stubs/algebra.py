"""Solving equations, inequalities and systems (chapter R2).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_r2_algebra.py``.
"""


def solve_linear(a, b):
    """Solve the equation ``a*x + b = 0`` in every case.

    Parameters
    ----------
    a, b : float

    Returns
    -------
    list of float or str
        ``[x]`` when there is one solution, ``[]`` when there is none, and the string ``"all"`` when every real
        number is a solution.

    Examples
    --------
    >>> solve_linear(2, -6)
    [3.0]
    >>> solve_linear(0, 5)
    []
    """
    # TODO: three cases, depending on a (and on b when a is zero).
    raise NotImplementedError("solve_linear() is not implemented yet")


def solve_linear_inequality(a, b, sense="<"):
    """Solve ``a*x + b < 0`` (or ``<=``, ``>``, ``>=``) and return the solution set as an interval.

    Parameters
    ----------
    a, b : float
    sense : {"<", "<=", ">", ">="}, default "<"

    Returns
    -------
    tuple of (bool, float, float, bool) or None
        ``(left_closed, low, high, right_closed)``, read like the bracket notation: ``(True, 2.0, inf, False)``
        is ``[2 ; +∞[`` (``float("inf")`` for an infinite end, always open). ``None`` for the empty set; the whole
        line is ``(False, -inf, inf, False)``.

    Raises
    ------
    ValueError
        If ``sense`` is not one of the four symbols.

    Examples
    --------
    >>> solve_linear_inequality(-2, 4, "<=")
    (True, 2.0, inf, False)
    """
    # TODO: dividing by a negative number reverses the inequality; a = 0 is a separate case.
    raise NotImplementedError("solve_linear_inequality() is not implemented yet")


def solve_abs_equation(a, c):
    """Solve ``|x - a| = c``: the points at distance ``c`` from ``a``.

    Parameters
    ----------
    a, c : float

    Returns
    -------
    list of float
        The solutions in increasing order (none, one or two).

    Examples
    --------
    >>> solve_abs_equation(1, 3)
    [-2.0, 4.0]
    """
    # TODO: a distance cannot be negative; c = 0 gives one point.
    raise NotImplementedError("solve_abs_equation() is not implemented yet")


def solve_2x2(A, b):
    """Solve the system ``A[0][0]*x + A[0][1]*y = b[0]``, ``A[1][0]*x + A[1][1]*y = b[1]`` with Cramer's rule.

    Parameters
    ----------
    A : sequence of two sequences of two floats
        The coefficients, row by row.
    b : sequence of two floats
        The right-hand sides.

    Returns
    -------
    tuple of (float, float)
        The unique solution ``(x, y)``.

    Raises
    ------
    ValueError
        If the determinant is zero (no solution or infinitely many).

    Examples
    --------
    >>> solve_2x2([[1, 1], [1, -1]], [5, 1])
    (3.0, 2.0)
    """
    # TODO: compute the determinant, then x and y as quotients of determinants.
    raise NotImplementedError("solve_2x2() is not implemented yet")
