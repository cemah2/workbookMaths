"""The hidden part of the challenge 🏆 MB3.22 (chapter MB3): the turbines and the method of the check.

Reference material, like ``solutions/mymath_ref/``. The notebook never reads this file; the check cell runs it as a
script in another process (``python -I mb3_22.py --serve``, :func:`serve`): that process draws three new turbines at
each run, sends their relevés and their hours only, receives the predictions of the learner's function, and answers with
the error and the threshold of each (:func:`measure`), so that neither the law of a hidden turbine nor the method that
sets the threshold lives in the notebook's process. Reading this file before solving the challenge spoils it.

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


def measure(train, test, law, predictions):
    """What the check says of the predictions of one turbine: the mean squared error, the threshold (1.3 times the
    error of :func:`reference`), the width that leave-one-out chooses, and the other width of :data:`GRID` whose
    predictions the learner's are (None when none is)."""
    truth = law(test[:, 0], test[:, 1])
    limit, chosen = threshold(train, test, truth)
    try:
        got = np.asarray(predictions, dtype=float)
    except (TypeError, ValueError):
        got = None
    if got is None or got.shape != (len(test),) or not np.all(np.isfinite(got)):
        return {"error": None, "threshold": limit, "chosen": chosen, "like": None}
    like = next((float(h) for h in GRID if abs(h - chosen) > 1e-12
                 and np.allclose(got, reference(train, test, width=float(h))[0], rtol=1e-6, atol=1e-6)), None)
    return {"error": float(np.mean((got - truth) ** 2)), "threshold": limit, "chosen": chosen, "like": like}


def serve():
    """``python -I mb3_22.py --serve``: draw three hidden turbines from fresh entropy (one per range of :data:`NOISES`);
    write one JSON line, ``{"turbines": [[train, test], ...]}`` (the relevés and the hours only); read one JSON line,
    the 400 predictions of the learner's function for each turbine, in order (null for a turbine it could not do);
    write one JSON line, :func:`measure` of each turbine, then stop. Any other input, or the end of stdin: stop at
    once."""
    import json
    import sys
    rng = np.random.default_rng()
    drawn = [turbine(rng, noise_range=noise_range) for noise_range in NOISES]
    out = sys.stdout.buffer
    out.write((json.dumps({"turbines": [[train.tolist(), test.tolist()] for train, test, _ in drawn]}) + "\n").encode())
    out.flush()
    try:
        answers = json.loads(sys.stdin.buffer.readline().decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return
    if not isinstance(answers, list) or len(answers) != len(drawn):
        return
    out.write((json.dumps([measure(train, test, law, answer) for (train, test, law), answer in zip(drawn, answers)])
               + "\n").encode())
    out.flush()


if __name__ == "__main__":
    import sys as _sys
    if _sys.argv[1:] == ["--serve"]:
        serve()
