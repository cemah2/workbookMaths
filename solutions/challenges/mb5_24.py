"""The two right methods of the check of 🛠️ MB5.24 (chapter MB5): Euler's method and the midpoint method, written
otherwise than in mymath (the times accumulated step after step).

Reference material, like ``solutions/mymath_ref/``. The check cell loads this file (``importlib``) and passes each method,
under a neutral name, to the learner's three property tests, which must accept them. They live here, not in the notebook,
because they are right versions of ``euler_ode`` and ``midpoint_ode`` (🔨 MB5.18): reading this file before writing them
spoils that exercise.
"""

import numpy as np


def euler_twin(f, x0, t0, t1, n_steps):
    """RIGHT: Euler's method written another way (the times accumulated step after step, the points as the start plus
    the sum of the steps): rounding errors of about 1e-16."""
    h = (t1 - t0) / n_steps
    x, t, moves = np.array(x0, dtype=float), t0, []
    for _ in range(n_steps):
        moves.append(h * np.asarray(f(t, x), dtype=float))
        x, t = x + moves[-1], t + h
    return np.array([np.array(x0, dtype=float)] + [np.array(x0, dtype=float) + s for s in np.cumsum(moves, axis=0)])


def midpoint_twin(f, x0, t0, t1, n_steps):
    """RIGHT: the midpoint method written another way (the times accumulated step after step)."""
    h = (t1 - t0) / n_steps
    x, t = np.array(x0, dtype=float), t0
    out = [x]
    for _ in range(n_steps):
        x = x + h * np.asarray(f(t + 0.5 * h, x + 0.5 * h * np.asarray(f(t, x), dtype=float)), dtype=float)
        t = t + h
        out.append(x)
    return np.array(out)
