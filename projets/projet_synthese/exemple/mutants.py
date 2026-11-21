"""Deliberate mistakes of the worked example (PS.7): do the tests of test_poisson_newton.py catch them?

    python -m pytest -q test_poisson_newton.py --impl=ref --mutant=newton_direction
    python -m pytest -q test_poisson_newton.py --impl=ref --mutant=hessian

With ``--mutant=<name>``, conftest.py replaces ``poisson_newton.<name>`` by the copy below for the whole run,
including the calls made by the other functions of the module (``fit`` calls ``newton_direction``;
``standard_errors`` and ``critical_learning_rate`` call ``hessian``). Each copy has ONE plausible mistake: the same
one, the weights ``mu_i`` forgotten, made at two places of the code. The notebook (§7) shows which tests catch them.
"""

from __future__ import annotations

import numpy as np

import poisson_newton  # the module of the example: its other functions, unchanged
from mymath import orthogonal


def newton_direction(w, X, y):
    """Mutant of poisson_newton.newton_direction: the weights are forgotten, W = I in Eq. (3.6).

    It solves ``X^T X delta = X^T (y - mu)`` instead of ``X^T W X delta = X^T (y - mu)``: the step of the Hessian
    ``-X^T X``. Its fixed points are still the zeros of the gradient, so an iteration that converges with it ends at
    the right maximum; only its path changes.
    """
    Xm = np.asarray(X, dtype=float)
    yv = np.asarray(y, dtype=float)
    mu = poisson_newton.mean(w, Xm)
    return orthogonal.least_squares_qr(Xm, yv - mu)


def hessian(w, X):
    """Mutant of poisson_newton.hessian: the weights are forgotten, ``-X^T X`` instead of ``-X^T diag(mu) X``."""
    Xm = np.asarray(X, dtype=float)
    return -(Xm.T @ Xm)
