"""Forward-mode automatic differentiation with dual numbers, the gradient by one forward pass per coordinate, and the
gradient of a function of a matrix read in its differential (chapter M18).

Reference implementation (solutions/mymath_ref).
The module ``math`` and NumPy are allowed, but not SymPy: the tests compare your derivatives with it. A dual number
``a + b ε``, with ``ε² = 0``, carries a value ``a`` and a derivative ``b``. Numbers are returned as Python ``float``,
gradients as ``numpy.ndarray`` of floats, of the shape of the variable (the convention of NumPy, not the row
gradient of MML).
"""

import math
import numbers

import numpy as np


def _lift(other):
    """other as a Dual (a plain real number is a constant), or None if it is neither."""
    if isinstance(other, Dual):
        return other
    if isinstance(other, numbers.Real):
        return Dual(other, 0.0)
    return None



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
        o = _lift(other)
        if o is None:
            return NotImplemented
        return Dual(self.value + o.value, self.derivative + o.derivative)

    def __radd__(self, other):
        """``other + self``, for ``other`` a plain number."""
        return self.__add__(other)

    def __neg__(self):
        """``-self``."""
        return Dual(-self.value, -self.derivative)

    def __sub__(self, other):
        """``self - other``."""
        o = _lift(other)
        if o is None:
            return NotImplemented
        return Dual(self.value - o.value, self.derivative - o.derivative)

    def __rsub__(self, other):
        """``other - self``, for ``other`` a plain number."""
        o = _lift(other)
        if o is None:
            return NotImplemented
        return o - self

    def __mul__(self, other):
        """``self * other``: ``(a + b ε)(c + d ε) = a c + (a d + b c) ε``."""
        o = _lift(other)
        if o is None:
            return NotImplemented
        return Dual(self.value * o.value, self.value * o.derivative + self.derivative * o.value)

    def __rmul__(self, other):
        """``other * self``, for ``other`` a plain number."""
        return self.__mul__(other)

    def __truediv__(self, other):
        """``self / other``: ``(a + b ε) / (c + d ε) = a / c + (b c - a d) / c² ε``.

        ``ZeroDivisionError`` if ``c = 0``.
        """
        o = _lift(other)
        if o is None:
            return NotImplemented
        if o.value == 0:
            raise ZeroDivisionError("division of a Dual by a Dual of value 0")
        return Dual(self.value / o.value, (self.derivative * o.value - self.value * o.derivative) / o.value ** 2)

    def __rtruediv__(self, other):
        """``other / self``, for ``other`` a plain number."""
        o = _lift(other)
        if o is None:
            return NotImplemented
        return o / self

    def __pow__(self, exponent):
        """``self ** exponent`` for a constant exponent: ``(a + b ε)ᵖ = aᵖ + p aᵖ⁻¹ b ε``.

        ``TypeError`` if the exponent is a ``Dual`` (a variable exponent is not asked here); ``ValueError`` if
        ``a < 0`` and the exponent is not an integer (Python would return a complex number), or if ``a = 0`` and
        ``p < 1`` with ``p ≠ 0`` (the derivative ``p aᵖ⁻¹`` does not exist). ``u ** 0`` is ``Dual(1.0, 0.0)``.
        """
        if isinstance(exponent, Dual):
            raise TypeError("the exponent of a Dual must be a constant number, not a Dual")
        if not isinstance(exponent, numbers.Real):
            return NotImplemented
        p, a, b = float(exponent), self.value, self.derivative
        if p == 0:
            return Dual(1.0, 0.0)
        if a < 0 and not p.is_integer():
            raise ValueError(f"a negative number to the power {exponent!r} is not a real number")
        if a == 0 and p < 1:
            raise ValueError(f"the derivative of t ** {exponent!r} does not exist at t = 0")
        return Dual(a ** p, p * a ** (p - 1) * b)

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
        e = math.exp(self.value)
        return Dual(e, e * self.derivative)

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
        if self.value <= 0:
            raise ValueError(f"log is defined for positive numbers, got {self.value!r}")
        return Dual(math.log(self.value), self.derivative / self.value)

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
        return Dual(math.sin(self.value), math.cos(self.value) * self.derivative)

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
        return Dual(math.cos(self.value), -math.sin(self.value) * self.derivative)


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
    y = f(Dual(x, 1.0))
    if isinstance(y, Dual):
        return y.value, y.derivative
    if isinstance(y, numbers.Real):
        return float(y), 0.0
    raise TypeError(f"f must return a Dual or a number, got {type(y).__name__}")


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
    try:
        point = np.array(x, dtype=float)
    except (TypeError, ValueError):
        raise ValueError(f"x must be a 1-D array of numbers, got {x!r}") from None
    if point.ndim != 1 or point.size == 0:
        raise ValueError(f"x must be a non-empty 1-D array, got shape {point.shape}")
    n = point.size
    gradient = np.zeros(n)
    for i in range(n):
        y = f([Dual(point[j], 1.0 if j == i else 0.0) for j in range(n)])
        if isinstance(y, Dual):
            gradient[i] = y.derivative
        elif not isinstance(y, numbers.Real):
            raise TypeError(f"f must return a Dual or a number, got {type(y).__name__}")
    return gradient


def gradient_from_differential(differential, shape):
    """Return the gradient ``G`` read in a differential ``df = tr(Gᵀ dX)``, of the given shape.

    Near ``X``, a differentiable function of a matrix moves by ``df ≈ Σ_ij G[i, j] dX[i, j] = tr(Gᵀ dX)`` when ``X``
    moves by ``dX``: the differential is a linear function of the move ``H = dX``, and the gradient ``G`` is the
    array of its coefficients. Its entry ``(i, j)`` is the value of the differential on the move ``E_ij`` (a single 1
    at ``(i, j)``): ``G[i, j] = differential(E_ij)``. So the gradient has the shape of the variable, the convention
    of NumPy and of the deep learning libraries (MML writes a row). The same works for an array of any shape (a
    vector, a 3-D array). The function does not check that ``differential`` is linear.

    Parameters
    ----------
    differential : callable
        A linear function that takes an array of shape ``shape`` (the move ``H``) and returns a number.
    shape : int or tuple of int
        The shape of the variable, with positive lengths.

    Returns
    -------
    numpy.ndarray
        The gradient, of shape ``shape``, of floats.

    Raises
    ------
    ValueError
        If a length of ``shape`` is not a positive integer.

    Examples
    --------
    >>> X = np.array([[1.0, 0.0], [2.0, -1.0]])
    >>> gradient_from_differential(lambda H: 2 * np.sum(X * H), X.shape)    # f(X) = ‖X‖², df = 2 tr(XᵀH)
    array([[ 2.,  0.],
           [ 4., -2.]])
    >>> gradient_from_differential(lambda H: 2 * H[0] + H[1] + 6 * H[2], 3)
    array([2., 1., 6.])
    """
    try:
        lengths = (shape,) if isinstance(shape, numbers.Integral) else tuple(shape)
    except TypeError:
        raise ValueError(f"shape must be an int or a tuple of int, got {shape!r}") from None
    for n in lengths:
        if isinstance(n, bool) or not isinstance(n, numbers.Integral) or n <= 0:
            raise ValueError(f"the lengths of shape must be positive integers, got {shape!r}")
    gradient = np.zeros(lengths)
    for index in np.ndindex(lengths):
        move = np.zeros(lengths)
        move[index] = 1.0
        gradient[index] = float(differential(move))
    return gradient
