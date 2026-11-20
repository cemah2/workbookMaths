"""The hidden part of the challenge 🏆 MB4.13 (chapter MB4): the noisy tables and the method of the check.

Reference material, like ``solutions/mymath_ref/``: the data cell of the notebook loads this file by its path from the
root of the repository (``wbm.repo_root() / "solutions" / "challenges" / "mb4_13.py"``), inside a function, and takes
only the five tables of the notebook (:func:`notebook_tables`). The check cell runs it as a script in another process
(``python -I mb4_13.py --serve``, :func:`serve`): that process draws three new series of five hidden tables at each run
and gives their ranks only once the learner's function has seen all of them, so that neither a hidden rank nor what makes
it (a seed, a kind) lives in the notebook's process while that function runs. Reading this file before solving the
challenge spoils it.

- :func:`table` builds a noisy table of hidden rank ``r``: ``U diag(θ) Vᵀ + σ Z``, with ``U`` (m × r) and ``V`` (n × r)
  orthonormal, ``Z`` standard Gaussian noise, and ``θ_i = g_i σ (m n)^{1/4}`` (``g_i`` measures the strength of a
  direction against the noise: below ``g = 1``, it is lost in the noise; the tables keep ``g ≥ 3``).
- :func:`notebook_tables` gives the five tables of the notebook (``TABLES_13``, seed 7513), :func:`notebook_ranks`
  their hidden ranks.
- :func:`hidden_table` draws a table of one of the five kinds of :data:`KINDS`: an easy one, a weak signal just above
  the noise, a signal whose singular values spread over a factor 10 or more, a very elongated table, and a table
  without signal or at an extreme scale (σ about 10^±4.5); otherwise σ is drawn from 10^-3 to 10^3. A series
  (:func:`hidden_series`) holds one table of each kind, in a random order.
- :func:`reference` is the method of the check: the noise level estimated on what the rank leaves aside
  (Eckart-Young: ``Σ_{i>r} s_i² ≈ σ² (m − r)(n − r)``), the rank counted above ``1.2 σ̂ (√m + √n)``, repeated until the
  rank no longer changes.
"""

import io
import json
import math
import struct
import sys

import numpy as np

KINDS = ("facile", "signal faible", "étalé", "allongé", "sans signal ou échelle extrême")
TAU = 1.2                                   # the margin of the method of the check above σ̂ (√m + √n)
SERIES = 3                                  # the series of five hidden tables drawn at each run of the check
NOTEBOOK_SEED = 7513
NOTEBOOK_SPECS = (((90, 60), (9.0, 6.5, 5.0), 0.8),
                  ((70, 110), (4.2,), 2.5),
                  ((120, 120), tuple(np.geomspace(22, 3.6, 5)), 0.3),
                  ((80, 50), (6.0, 3.4), 1.5),
                  ((100, 75), (8.5, 6.0, 4.6, 4.0), 0.6))


def _orthonormal(rng, m, r):
    Q, _ = np.linalg.qr(rng.normal(size=(m, r)))
    return Q


def table(rng, m, n, g, sigma):
    """A table (m, n) = U diag(θ) Vᵀ + σ Z of rank len(g) before the noise, θ_i = g_i σ (m n)^{1/4}."""
    g = np.asarray(g, dtype=float)
    M = sigma * rng.normal(size=(m, n))
    if g.size:
        theta = g * sigma * (m * n) ** 0.25
        M = M + (_orthonormal(rng, m, g.size) * theta) @ _orthonormal(rng, n, g.size).T
    return M


def notebook_tables():
    """The five tables of the notebook (TABLES_13), a list of arrays."""
    rng = np.random.default_rng(NOTEBOOK_SEED)
    return [table(rng, m, n, g, sigma) for (m, n), g, sigma in NOTEBOOK_SPECS]


def notebook_ranks():
    """The hidden ranks of the five tables of the notebook."""
    return [len(g) for _, g, _ in NOTEBOOK_SPECS]


def _shape(rng, lo=30, hi=200, ratio=12.0):
    """A shape (m, n), the aspect ratio drawn log-uniformly in [1/ratio, ratio], the area between 2 lo² and hi²/1.5."""
    while True:
        a = math.exp(rng.uniform(-math.log(ratio), math.log(ratio)))
        area = math.exp(rng.uniform(math.log(2 * lo * lo), math.log(hi * hi / 1.5)))
        m, n = int(round(math.sqrt(area / a))), int(round(math.sqrt(area * a)))
        if 20 <= m <= 400 and 20 <= n <= 400:
            return m, n


def hidden_table(rng, kind):
    """A hidden table of the given kind (one of KINDS), drawn by rng: (M, rank)."""
    sigma = 10 ** rng.uniform(-3, 3)
    if kind == "facile":
        m, n = _shape(rng, 50, 200, 3)
        r = int(rng.integers(2, 7))
        g = rng.uniform(5, 15, r)
    elif kind == "signal faible":
        m, n = _shape(rng)
        r = int(rng.integers(1, 5))
        g = rng.uniform(3, 3.8, r)
    elif kind == "étalé":
        m, n = _shape(rng, 60, 220, 4)
        r = int(rng.integers(4, 8))
        g = np.geomspace(rng.uniform(40, 100), rng.uniform(2.8, 3.4), r)   # neighbours further apart than s_r and s_r+1
    elif kind == "allongé":
        m, n = int(rng.integers(22, 41)), int(rng.integers(250, 401))
        r = int(rng.integers(1, 6))
        g = rng.uniform(3.4, 6, r)
        if rng.random() < 0.5:
            m, n = n, m
    elif kind == "sans signal ou échelle extrême":
        sigma = 10 ** rng.choice([-4.5, 4.5]) * 10 ** rng.uniform(-0.5, 0.5)
        m, n = _shape(rng, 30, 150, 6)
        r = 0 if rng.random() < 0.5 else int(rng.integers(1, 4))
        g = rng.uniform(4, 10, r)
    else:
        raise ValueError(f"unknown kind {kind!r}")
    return table(rng, m, n, g, sigma), r


def hidden_series(rng=None):
    """A series of five new hidden tables, one of each kind, in a random order: a list of (M, rank, kind)."""
    rng = np.random.default_rng() if rng is None else rng
    kinds = list(KINDS)
    rng.shuffle(kinds)
    return [(*hidden_table(rng, kind), kind) for kind in kinds]


def serve(series=SERIES):
    """The hidden tables of one run of the check, served from another process (``python -I mb4_13.py --serve``): draw
    ``series`` series of five tables from fresh entropy; write each table on stdout (an 8-byte little-endian length, then
    ``np.save`` bytes), then a length 0; wait for one line on stdin; then write one JSON line, the ranks and the kinds of
    the tables, in their order, and stop."""
    drawn = [table for _ in range(series) for table in hidden_series(np.random.default_rng())]
    out = sys.stdout.buffer
    for M, _, _ in drawn:
        buffer = io.BytesIO()
        np.save(buffer, M, allow_pickle=False)
        out.write(struct.pack("<Q", len(buffer.getvalue())) + buffer.getvalue())
    out.write(struct.pack("<Q", 0))
    out.flush()
    sys.stdin.readline()
    out.write((json.dumps({"ranks": [r for _, r, _ in drawn], "kinds": [k for _, _, k in drawn]}) + "\n").encode())
    out.flush()


def reference(M, tau=TAU, max_iter=50):
    """The method of the check: the rank above tau σ̂ (√m + √n), σ̂ estimated on the singular values left aside."""
    M = np.asarray(M, dtype=float)
    m, n = M.shape
    s = np.linalg.svd(M, compute_uv=False)
    r = 0
    for _ in range(max_iter):
        if r >= min(m, n):                  # nothing left to estimate the noise on
            break
        sigma = math.sqrt(float((s[r:] ** 2).sum()) / ((m - r) * (n - r)))
        r_new = int((s > tau * sigma * (math.sqrt(m) + math.sqrt(n))).sum())
        if r_new == r:
            break
        r = r_new
    return r


if __name__ == "__main__" and sys.argv[1:] == ["--serve"]:
    serve()
