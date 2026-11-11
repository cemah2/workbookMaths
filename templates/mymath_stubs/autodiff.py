"""Forward-mode automatic differentiation with dual numbers, the gradient by one forward pass per coordinate, and the
numerical gradient of a function of a matrix (chapter M18).

Replace each ``raise NotImplementedError`` with your code, then run ``pytest tests/test_m18_autodiff.py``.
The module ``math`` and NumPy are allowed, but not SymPy: the tests compare your derivatives with it. A dual number
``a + b ε``, with ``ε² = 0``, carries a value ``a`` and a derivative ``b``. Numbers are returned as Python ``float``,
gradients as ``numpy.ndarray`` of floats, of the shape of the variable (the convention of NumPy, not the row
gradient of MML).
"""


class Dual:
    """A dual number ``value + derivative · ε``, with ``ε² = 0``: forward-mode automatic differentiation.

    Each operation computes the value and applies the rule of derivation of that operation: for ``u = a + b ε`` and
    ``w = c + d ε``, ``u + w = (a + c) + (b + d) ε``, ``u w = a c + (a d + b c) ε`` (the term in ``ε²`` vanishes),
    ``u / w = a / c + (b c - a d) / c² ε``, ``uᵖ = aᵖ + p aᵖ⁻¹ b ε`` for a constant exponent ``p``, and
    ``g(u) = g(a) + g'(a) b ε`` for ``exp``, ``log``, ``sin`` and ``cos`` (the chain rule). So evaluating a function
    ``f`` written with these operations at ``Dual(a, 1.0)`` gives ``Dual(f(a), f'(a))``. A plain number ``c`` in an
    operation counts as ``Dual(c, 0.0)``, a constant.

    Provided: the constructor and ``__repr__``. To write: ``+``, ``-``, ``*``, ``/`` on both sides (``__add__`` and
    ``__radd__``, and so on), the opposite ``-u``, the power ``u ** p`` by a constant ``p`` (an ``int`` or a
    ``float``), and the methods ``exp``, ``log``, ``sin`` and ``cos``. Every operation returns a new ``Dual``.

    Examples
    --------
    >>> x = Dual(3.0, 1.0)
    >>> (x + 1) / (x - 1)
    Dual(value=2.0, derivative=-0.5)
    >>> (2 * x ** 2).derivative
    12.0
    >>> Dual(0.0, 1.0).exp()
    Dual(value=1.0, derivative=1.0)
    """

    def __init__(self, value, derivative=0.0):
        """Provided: store ``value`` and ``derivative`` as floats."""
        self.value = float(value)
        self.derivative = float(derivative)

    def __repr__(self):
        """Provided: ``Dual(value=…, derivative=…)``."""
        return f"Dual(value={self.value!r}, derivative={self.derivative!r})"

    def __add__(self, other):
        """``self + other``: values and derivatives add up."""
        # TODO: turn a plain number into Dual(other, 0.0), then add.
        raise NotImplementedError("Dual.__add__() is not implemented yet")

    def __radd__(self, other):
        """``other + self``, for ``other`` a plain number."""
        # TODO: the sum is commutative.
        raise NotImplementedError("Dual.__radd__() is not implemented yet")

    def __neg__(self):
        """``-self``."""
        # TODO: both parts change sign.
        raise NotImplementedError("Dual.__neg__() is not implemented yet")

    def __sub__(self, other):
        """``self - other``."""
        # TODO: self + (-other), after turning a plain number into a Dual.
        raise NotImplementedError("Dual.__sub__() is not implemented yet")

    def __rsub__(self, other):
        """``other - self``, for ``other`` a plain number."""
        # TODO: Dual(other, 0.0) - self.
        raise NotImplementedError("Dual.__rsub__() is not implemented yet")

    def __mul__(self, other):
        """``self * other``: ``(a + b ε)(c + d ε) = a c + (a d + b c) ε``."""
        # TODO: turn a plain number into a Dual, then the product rule.
        raise NotImplementedError("Dual.__mul__() is not implemented yet")

    def __rmul__(self, other):
        """``other * self``, for ``other`` a plain number."""
        # TODO: the product is commutative.
        raise NotImplementedError("Dual.__rmul__() is not implemented yet")

    def __truediv__(self, other):
        """``self / other``: ``(a + b ε) / (c + d ε) = a / c + (b c - a d) / c² ε``.

        ``ZeroDivisionError`` if ``c = 0``.
        """
        # TODO: turn a plain number into a Dual, check c ≠ 0, then the quotient rule.
        raise NotImplementedError("Dual.__truediv__() is not implemented yet")

    def __rtruediv__(self, other):
        """``other / self``, for ``other`` a plain number."""
        # TODO: Dual(other, 0.0) / self.
        raise NotImplementedError("Dual.__rtruediv__() is not implemented yet")

    def __pow__(self, exponent):
        """``self ** exponent`` for a constant exponent: ``(a + b ε)ᵖ = aᵖ + p aᵖ⁻¹ b ε``.

        ``TypeError`` if the exponent is a ``Dual`` (a variable exponent is not asked here).
        """
        # TODO: refuse a Dual exponent, then the rule (a ** p, p * a ** (p - 1) * b).
        raise NotImplementedError("Dual.__pow__() is not implemented yet")

    def exp(self):
        """Return ``exp(self)``: ``e^a + e^a b ε``.

        Returns
        -------
        Dual

        Examples
        --------
        >>> Dual(0.0, 2.0).exp()
        Dual(value=1.0, derivative=2.0)
        """
        # TODO: math.exp, and the chain rule.
        raise NotImplementedError("Dual.exp() is not implemented yet")

    def log(self):
        """Return ``log(self)`` (natural logarithm): ``ln a + (b / a) ε``; ``ValueError`` if ``a ≤ 0``.

        Returns
        -------
        Dual

        Examples
        --------
        >>> Dual(1.0, 3.0).log()
        Dual(value=0.0, derivative=3.0)
        """
        # TODO: check a > 0, math.log, and the chain rule.
        raise NotImplementedError("Dual.log() is not implemented yet")

    def sin(self):
        """Return ``sin(self)``: ``sin a + (cos a) b ε``.

        Returns
        -------
        Dual

        Examples
        --------
        >>> Dual(0.0, 1.0).sin()
        Dual(value=0.0, derivative=1.0)
        """
        # TODO: math.sin, math.cos, and the chain rule.
        raise NotImplementedError("Dual.sin() is not implemented yet")

    def cos(self):
        """Return ``cos(self)``: ``cos a - (sin a) b ε``.

        Returns
        -------
        Dual

        Examples
        --------
        >>> u = Dual(0.0, 1.0).cos()
        >>> u.value, u.derivative == 0
        (1.0, True)
        """
        # TODO: math.cos, math.sin, and the chain rule.
        raise NotImplementedError("Dual.cos() is not implemented yet")


def dual_derivative(f, x):
    """Return ``(f(x), f'(x))`` for a function of one variable written with the operations of ``Dual``.

    Evaluate ``f(Dual(x, 1.0))``: the seed ``1.0`` says that the derivative of ``x`` with respect to itself is 1. If
    ``f`` returns a plain number (a constant function), its derivative is ``0.0``.

    Parameters
    ----------
    f : callable
        A function that takes a ``Dual`` and returns a ``Dual`` or a number.
    x : float
        The point.

    Returns
    -------
    tuple
        ``(value, derivative)``, two ``float``.

    Raises
    ------
    TypeError
        If ``f`` returns something else than a ``Dual`` or a number.

    Examples
    --------
    >>> dual_derivative(lambda t: t * t.exp(), 0.0)
    (0.0, 1.0)
    >>> dual_derivative(lambda t: (t ** 2 + 1).log(), 1.0)
    (0.6931471805599453, 1.0)
    """
    # TODO: y = f(Dual(x, 1.0)), then the two parts (a number y gives (float(y), 0.0)).
    raise NotImplementedError("dual_derivative() is not implemented yet")


def forward_gradient(f, x):
    """Return the gradient of ``f : ℝⁿ → ℝ`` at ``x`` by ``n`` forward passes with dual numbers.

    Pass ``i`` evaluates ``f`` on the list of duals ``Dual(x_j, 1.0 if j == i else 0.0)``: only ``x_i`` moves, and
    the derivative part of the result is ``∂f/∂x_i``. Forward mode thus costs one pass per input: cheap for few
    inputs, expensive for many (reverse mode, done by hand in M18 and written in workbookIA 18, costs one pass per
    output).

    Parameters
    ----------
    f : callable
        A function that takes a list of ``n`` ``Dual`` and returns a ``Dual`` (or a number, if constant).
    x : 1-D array-like
        The ``n`` coordinates of the point, ``n ≥ 1``.

    Returns
    -------
    numpy.ndarray
        The ``n`` partial derivatives.

    Raises
    ------
    ValueError
        If ``x`` is not 1-D or is empty.

    Examples
    --------
    >>> forward_gradient(lambda v: v[0] * v[1] + v[1].sin(), [2.0, 0.0])
    array([0., 3.])
    """
    # TODO: check x; for each i, build the list of duals, evaluate f, keep the derivative (0.0 for a number).
    raise NotImplementedError("forward_gradient() is not implemented yet")


def numerical_matrix_gradient(f, X, h=1e-6):
    """Return the gradient of a real function of a matrix, of the shape of the matrix, by centered differences.

    Entry ``(i, j)`` is ``(f(X + h E_ij) - f(X - h E_ij)) / (2 h)``, where ``E_ij`` has a single 1 at ``(i, j)``:
    the gradient has the shape of the variable, the convention of NumPy and of the deep learning libraries (MML
    writes a row). The same works for an array of any shape (a vector, a 3-D array). It costs ``2 X.size``
    evaluations of ``f``; ``X`` itself is never modified.

    Parameters
    ----------
    f : callable
        A function that takes an array of the shape of ``X`` and returns a number.
    X : array-like
        The point, a non-empty array of numbers.
    h : float, default 1e-6
        The step, ``h > 0``.

    Returns
    -------
    numpy.ndarray
        The gradient, of the shape of ``X``.

    Raises
    ------
    ValueError
        If ``X`` is empty or if ``h ≤ 0``.

    Examples
    --------
    >>> X = np.array([[1.0, -2.0], [0.5, 3.0]])
    >>> np.round(numerical_matrix_gradient(lambda M: np.sum(M ** 2), X), 6)
    array([[ 2., -4.],
           [ 1.,  6.]])
    >>> np.round(numerical_matrix_gradient(lambda w: w[0] * w[1], np.array([3.0, 5.0])), 6)
    array([5., 3.])
    """
    # TODO: check X and h; for each index (np.ndindex), two copies of X moved by ±h, the centered difference.
    raise NotImplementedError("numerical_matrix_gradient() is not implemented yet")
