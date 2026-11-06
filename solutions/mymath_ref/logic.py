"""Logic, sums and products, counterexamples (chapter R4).

Reference implementation (solutions/mymath_ref).
"""

import itertools


def truth_table(formula, n):
    """Return the truth table of a formula with ``n`` propositional variables.

    Parameters
    ----------
    formula : callable
        A function of ``n`` booleans returning a boolean, e.g. ``lambda p, q: p and not q``.
    n : int
        Number of variables, at least 1.

    Returns
    -------
    list of tuple
        ``2**n`` rows ``(values, result)``, ``values`` being a tuple of ``n`` booleans, in the order of
        ``itertools.product([True, False], repeat=n)`` (the usual order: all true first).

    Raises
    ------
    ValueError
        If ``n < 1``.

    Examples
    --------
    >>> truth_table(lambda p: not p, 1)
    [((True,), False), ((False,), True)]
    """
    if n < 1:
        raise ValueError(f"a truth table needs at least one variable, got n = {n}")
    return [(values, bool(formula(*values))) for values in itertools.product([True, False], repeat=n)]


def implies(p, q):
    """Return the truth value of the implication ``p ⇒ q``.

    Parameters
    ----------
    p, q : bool

    Returns
    -------
    bool
        False only when ``p`` is true and ``q`` is false.

    Examples
    --------
    >>> implies(False, False)
    True
    """
    return (not p) or bool(q)


def sum_over(f, start, stop):
    """Return the sum ``f(start) + f(start + 1) + ... + f(stop)`` (both ends included, as the symbol Σ).

    Parameters
    ----------
    f : callable
        A function of an integer.
    start, stop : int
        If ``stop < start`` the sum is empty and equals 0.

    Returns
    -------
    int or float
        An int when ``f`` returns ints.

    Examples
    --------
    >>> sum_over(lambda k: k, 1, 100)
    5050
    """
    total = 0
    for k in range(start, stop + 1):
        total = total + f(k)
    return total


def prod_over(f, start, stop):
    """Return the product ``f(start) * f(start + 1) * ... * f(stop)`` (both ends included, as the symbol Π).

    Parameters
    ----------
    f : callable
        A function of an integer.
    start, stop : int
        If ``stop < start`` the product is empty and equals 1.

    Returns
    -------
    int or float
        An int when ``f`` returns ints.

    Examples
    --------
    >>> prod_over(lambda k: k, 1, 5)
    120
    """
    product = 1
    for k in range(start, stop + 1):
        product = product * f(k)
    return product


def find_counterexample(predicate, n_max):
    """Return the smallest integer ``n`` in ``0, 1, ..., n_max`` for which ``predicate(n)`` is false.

    Parameters
    ----------
    predicate : callable
        A function of an integer returning a boolean (the statement « for every n, P(n) »).
    n_max : int
        Last integer tried (included).

    Returns
    -------
    int or None
        The first counterexample, or None if the statement holds up to ``n_max`` (which proves nothing beyond).

    Examples
    --------
    >>> find_counterexample(lambda n: n * n < 50, 100)
    8
    """
    for n in range(n_max + 1):
        if not predicate(n):
            return n
    return None
