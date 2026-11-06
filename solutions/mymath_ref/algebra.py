"""Solving equations, inequalities and systems (chapter R2).

Reference implementation (solutions/mymath_ref).

Conventions of the module: a finite set of solutions is a sorted list of floats (``[]`` when there is none); every
real number is the string ``"all"``; an interval is a tuple ``(left_closed, low, high, right_closed)`` read like the
bracket notation you type in ``wbm.check``: ``(True, 2.0, inf, False)`` is ``[2 ; +∞[``. Tests of degenerate cases
(a zero coefficient, a zero determinant) use integers, so compare with 0 exactly.
"""

import math


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
    >>> solve_linear(0, 0)
    'all'
    """
    if a == 0:
        return "all" if b == 0 else []
    return [-b / a]


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
    >>> solve_linear_inequality(0, 1, "<") is None       # 1 < 0 is never true
    True
    >>> solve_linear_inequality(0, -1, "<")              # -1 < 0 is always true
    (False, -inf, inf, False)
    """
    if sense not in ("<", "<=", ">", ">="):
        raise ValueError(f"sense must be '<', '<=', '>' or '>=', not {sense!r}")
    inf = math.inf
    if a == 0:   # b < 0, b <= 0, b > 0 or b >= 0: true for every x, or for none
        holds = {"<": b < 0, "<=": b <= 0, ">": b > 0, ">=": b >= 0}[sense]
        return (False, -inf, inf, False) if holds else None
    root = -b / a
    if a < 0:    # dividing by a negative number reverses the inequality
        sense = {"<": ">", "<=": ">=", ">": "<", ">=": "<="}[sense]
    if sense in ("<", "<="):
        return (False, -inf, root, sense == "<=")
    return (sense == ">=", root, inf, False)


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
    >>> solve_abs_equation(1, 0)
    [1.0]
    """
    if c < 0:
        return []
    if c == 0:
        return [float(a)]
    return [float(a - c), float(a + c)]


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
    (a11, a12), (a21, a22) = A
    b1, b2 = b
    det = a11 * a22 - a12 * a21
    if det == 0:
        raise ValueError("the determinant is zero: no unique solution")
    return ((b1 * a22 - a12 * b2) / det, (a11 * b2 - b1 * a21) / det)
