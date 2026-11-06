"""Logic, sums and products, counterexamples (chapter R4).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_r4_logic.py``.
"""


def truth_table(formula, n):
    """Return the truth table of a formula with ``n`` propositional variables.

    Parameters
    ----------
    formula : callable
        A function of ``n`` booleans returning a boolean, e.g. ``lambda p, q: p and not q``.
    n : int
        Number of variables (at least 1).

    Returns
    -------
    list of tuple
        ``2**n`` rows ``(values, result)``, ``values`` being a tuple of ``n`` booleans, in the order of
        ``itertools.product([True, False], repeat=n)`` (the usual order: all true first).

    Examples
    --------
    >>> truth_table(lambda p: not p, 1)
    [((True,), False), ((False,), True)]
    """
    # TODO: loop over every combination of n booleans and call formula(*values).
    raise NotImplementedError("truth_table() is not implemented yet")


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
    # TODO: one line, using not and or.
    raise NotImplementedError("implies() is not implemented yet")


def sigma(f, start, stop):
    """Return the sum ``f(start) + f(start + 1) + ... + f(stop)`` (both ends included, as the symbol Σ).

    Parameters
    ----------
    f : callable
        A function of an integer.
    start, stop : int
        If ``stop < start`` the sum is empty and equals 0.

    Returns
    -------
    number

    Examples
    --------
    >>> sigma(lambda k: k, 1, 100)
    5050
    """
    # TODO: careful, range(start, stop) does not include stop.
    raise NotImplementedError("sigma() is not implemented yet")


def product(f, start, stop):
    """Return the product ``f(start) * f(start + 1) * ... * f(stop)`` (both ends included, as the symbol Π).

    Parameters
    ----------
    f : callable
        A function of an integer.
    start, stop : int
        If ``stop < start`` the product is empty and equals 1.

    Returns
    -------
    number

    Examples
    --------
    >>> product(lambda k: k, 1, 5)
    120
    """
    # TODO: same as sigma, but which value do you start from?
    raise NotImplementedError("product() is not implemented yet")


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
    # TODO: try the integers in order and stop at the first failure.
    raise NotImplementedError("find_counterexample() is not implemented yet")
