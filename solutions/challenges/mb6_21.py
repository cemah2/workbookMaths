"""The methods of the check of 🛠️ MB6.21 (chapter MB6) that compute a line integral by a quadrature written out: two
right ones (Simpson with 40 intervals on each segment, the three-point Gauss-Legendre rule on 8 pieces) and three wrong
ones (left Riemann sums, the trapezoid rule, Simpson with |b - a| instead of b - a).

Reference material, like ``solutions/mymath_ref/``. The check cell loads this file (``importlib``) and passes each method,
under a neutral name, to the learner's three property tests. They live here, not in the notebook, because they show how
to write ``line_integral`` (🔨 MB6.15), the last one a single character away from it: reading this file before writing
it spoils that exercise. None of them calls mymath nor the reference.
"""

import numpy as np


def simpson_twin(field, points):
    """RIGHT: Simpson's rule with 40 intervals on each segment, written another way (the nodes accumulated)."""
    pts = np.asarray(points, dtype=float)
    total = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        values = [float(np.dot(np.asarray(field(a + (k / 40) * (b - a)), dtype=float), b - a)) for k in range(41)]
        total += (values[0] + values[-1] + 4 * sum(values[1:-1:2]) + 2 * sum(values[2:-1:2])) / 120
    return total


def gauss_twin(field, points):
    """RIGHT: the three-point Gauss-Legendre rule on 8 equal pieces of each segment (exact for degrees up to 5)."""
    nodes, weights = np.polynomial.legendre.leggauss(3)
    pts = np.asarray(points, dtype=float)
    total = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        for piece in range(8):
            for x, w in zip(nodes, weights):
                t = (piece + (x + 1) / 2) / 8
                total += w / 16 * float(np.dot(np.asarray(field(a + t * (b - a)), dtype=float), b - a))
    return total


def left_sums(field, points):
    """WRONG: left Riemann sums with 64 intervals on each segment (its nodes are not symmetric)."""
    pts = np.asarray(points, dtype=float)
    return sum(sum(float(np.dot(np.asarray(field(a + (k / 64) * (b - a)), dtype=float), b - a)) for k in range(64)) / 64
               for a, b in zip(pts[:-1], pts[1:]))


def trapezoid(field, points):
    """WRONG unless the field is affine: the trapezoid rule with 20 intervals on each segment."""
    pts = np.asarray(points, dtype=float)
    total = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        values = [float(np.dot(np.asarray(field(a + (k / 20) * (b - a)), dtype=float), b - a)) for k in range(21)]
        total += (sum(values) - (values[0] + values[-1]) / 2) / 20
    return total


def positive_steps(field, points):
    """WRONG on a segment that goes to the left or down: F . |b - a| instead of F . (b - a) (right on the segments
    that go to the right and up)."""
    pts = np.asarray(points, dtype=float)
    total = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        values = [float(np.dot(np.asarray(field(a + (k / 20) * (b - a)), dtype=float), np.abs(b - a)))
                  for k in range(21)]
        total += (values[0] + values[-1] + 4 * sum(values[1:-1:2]) + 2 * sum(values[2:-1:2])) / 60
    return total
