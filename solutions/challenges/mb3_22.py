"""The hidden part of the challenge 🏆 MB3.22 (chapter MB3): the turbines and the method of the check.

Reference material, like ``solutions/mymath_ref/``: the check cell of the notebook loads this file by its path from the
root of the repository (``wbm.repo_root() / "solutions" / "challenges" / "mb3_22.py"``), inside a function, so that the
notebook shows neither the law of the hidden turbines nor the method that sets the threshold. Reading it before
solving the challenge spoils it.

- :func:`turbine` draws a turbine of the type of the notebook: a law of the production as a function of the direction
  of the wind and of the day of the year, 400 noisy relevés, and 400 hours to predict around 0° and the new year. The
  notebook set is ``turbine(np.random.default_rng(7328), noise=60.0)``; the check draws three new ones at each run, with
  little, some and much noise (:data:`NOISES`).
- :func:`reference` is the method of the check: Nadaraya-Watson with a Gaussian kernel on the cyclic encoding, its
  bandwidth chosen by leave-one-out cross-validation on :data:`GRID`.
- :func:`threshold` is 1.3 times the mean squared error of :func:`reference` against the expected production.
"""

import numpy as np

GRID = np.geomspace(0.03, 1.5, 30)                      # the 30 widths of the method of the check (GRID_22)
NOISES = ((3.0, 8.0), (50.0, 90.0), (600.0, 1000.0))   # the noise of the three hidden turbines (kW): little, some, much
FACTOR = 1.3                                            # the threshold: 1.3 times the error of the method of the check


def encode(theta, day):
    """The cyclic encoding (cos θ, sin θ, cos 2πd/365, sin 2πd/365) of directions (degrees) and days: (n, 4)."""
    a = np.radians(np.asarray(theta, dtype=float))
    b = 2 * np.pi * np.asarray(day, dtype=float) / 365
    return np.column_stack([np.cos(a), np.sin(a), np.cos(b), np.sin(b)])


def turbine(rng, noise=None, noise_range=None, n=400, n_test=400):
    """A turbine drawn by ``rng``: ``(train, test, law)``, train an (n, 3) array (direction in degrees, day, production in
    kW), test an (n_test, 2) array (direction, day) of hours around 0° and the new year, and ``law(theta, day)`` the
    expected production. The standard deviation of the noise is ``noise``, or is drawn log-uniformly in
    ``noise_range``."""
    th0, d0 = float(rng.uniform(-20, 20)) % 360, float(rng.uniform(-20, 20)) % 365
    amplitude, kappa, season, centre = (float(rng.uniform(1200, 1400)), float(rng.uniform(1.8, 2.4)),
                                        float(rng.uniform(0.3, 0.4)), float(rng.uniform(-10, 10)))
    if noise is None:
        noise = float(np.exp(rng.uniform(*np.log(noise_range))))

    def law(theta, day):
        return amplitude * (1 - season + season * np.cos(2 * np.pi * (np.asarray(day) - d0) / 365)) * np.exp(
            kappa * (np.cos(np.radians(np.asarray(theta) - th0)) - 1))

    th, d = (centre + rng.normal(0, 40, n)) % 360, rng.uniform(0, 365, n)
    y = np.maximum(law(th, d) + rng.normal(0, noise, n), 0.0)      # a production is never negative
    th_test, d_test = rng.uniform(-40, 40, n_test) % 360, rng.uniform(-25, 25, n_test) % 365
    return np.column_stack([th, d, y]), np.column_stack([th_test, d_test]), law


def _softmax_rows(S):
    W = np.exp(S - S.max(axis=1, keepdims=True))
    return W / W.sum(axis=1, keepdims=True)


def reference(train, test, width=None, grid=GRID):
    """The method of the check: Nadaraya-Watson on :func:`encode`, the width chosen by leave-one-out on ``grid`` (or
    the ``width`` given). Returns ``(predictions, width)``."""
    train, test = np.asarray(train, dtype=float), np.asarray(test, dtype=float)
    Z, y, Z_test = encode(train[:, 0], train[:, 1]), train[:, 2], encode(test[:, 0], test[:, 1])
    if width is None:
        D2 = ((Z[:, None, :] - Z[None, :, :]) ** 2).sum(axis=-1)
        errors = []
        for h in grid:
            S = -D2 / (2 * h * h)
            np.fill_diagonal(S, -np.inf)                    # a relevé does not predict itself
            errors.append(float(np.mean((_softmax_rows(S) @ y - y) ** 2)))
        width = float(grid[int(np.argmin(errors))])
    S = -((Z_test[:, None, :] - Z[None, :, :]) ** 2).sum(axis=-1) / (2 * width * width)
    return _softmax_rows(S) @ y, width


def threshold(train, test, truth):
    """1.3 times the mean squared error of :func:`reference` against ``truth``, and the width it chose."""
    predictions, width = reference(train, test)
    return FACTOR * float(np.mean((predictions - np.asarray(truth, dtype=float)) ** 2)), width
