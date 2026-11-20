"""The hidden part of the challenge 🏆 MB5.25 (chapter MB5): the hidden two-bump laws and the method of the corrected
version.

Reference material, like ``solutions/mymath_ref/``. The notebook gives its own two-bump law (``MIX_25``, a literal of its
data cell) and never reads this file; the check cell runs it as a script in another process (``python -I mb5_25.py
--serve``, :func:`serve`): that process draws three new series of five hidden laws at each run, answers the field
requests of the learner's function (and counts them, law by law), and measures the points it receives only at the end,
so that no hidden law (nor a seed, nor a kind) lives in the notebook's process while that function runs. Reading this
file before solving the challenge spoils it.

The challenge. ``x_s = (1 − s) x_0 + s ε`` is the straight path between a datum ``x_0`` of a two-bump law (a mixture of
two Gaussians of dimension 1) and a noise ``ε ~ N(0, 1)`` (MB5 §9); its mean field ``v(x, s) = (x − E[x_0 | x_s = x]) / s``
is exact here (the posterior mean of a mixture, with the gains ``1 − s`` and ``s``). From points of ``N(0, 1)`` at
``s = 1``, the learner's function follows ``x' = v(x, s)`` down to ``s = 0`` with at most :data:`BUDGET` calls of the
field (one call for a whole array counts once). Criterion: the distance of Wasserstein ``W₁`` (M27) between the points
reached and the two-bump law, divided by the standard deviation of that law, is at most :data:`REL` for the law of the
notebook, and at most :data:`REL` on average over the hidden laws of a run (a criterion on the mean: a method of order 2
stays far under it, a method of order 1 far over it, so that the verdict does not depend on the laws drawn).

- :func:`hidden_mixture` draws a law of one kind of :data:`KINDS`: two bumps of moderate width; two very narrow bumps
  (variances 10^-2.7 to 10^-1.5: the trajectories split late); a light bump (weight 0.08 to 0.2) of another width; two
  bumps 5 to 8 apart, further apart than the noise is wide; two overlapping bumps 1 to 1.8 apart. The light bump is put
  on either side.
- :func:`w1_to_mixture` is ``W₁ = ∫ |F_n − F|`` between the empirical law of the points and the mixture, on a fine grid,
  with the exact distribution function of the mixture.
- :func:`reference` is the method of the corrected version (eight calls).
"""

import json
import math
import sys

import numpy as np

KINDS = ("facile", "deux bosses très étroites", "une bosse légère d'une autre largeur", "deux bosses très écartées",
         "deux bosses qui se chevauchent")
REL = 0.07               # the criterion: W₁ / (the standard deviation of the law) ≤ REL (on average for the hidden laws)
BUDGET = 8               # the calls of the field allowed
SERIES = 3               # the series of len(KINDS) hidden laws drawn at each run of the check
MAX_POINTS = 2_000_000   # the largest array of points the process accepts in one request
NOTEBOOK_LAW = ((0.38, 0.62), (-1.6, 2.1), (0.12, 0.3))   # MIX_25, the two-bump law of the notebook (not hidden)


# --------------------------------------------------------------------------------------------------------------------
# the hidden laws
# --------------------------------------------------------------------------------------------------------------------
def hidden_mixture(rng, kind):
    """A hidden two-bump law of the given kind (one of KINDS), drawn by rng: (weights, means, variances), three tuples
    of two floats."""
    centre = rng.uniform(-1, 1)
    if kind == KINDS[0]:
        gap, light, spread = rng.uniform(2.5, 4.5), rng.uniform(0.35, 0.65), rng.uniform(0.15, 0.6, 2)
    elif kind == KINDS[1]:
        gap, light, spread = rng.uniform(1.5, 3.5), rng.uniform(0.3, 0.7), 10 ** rng.uniform(-2.7, -1.5, 2)
    elif kind == KINDS[2]:
        gap, light = rng.uniform(2.5, 4.5), rng.uniform(0.08, 0.2)
        spread = np.array([10 ** rng.uniform(-1.5, -0.7), rng.uniform(0.2, 0.8)])
    elif kind == KINDS[3]:
        gap, light, spread = rng.uniform(5, 8), rng.uniform(0.25, 0.75), rng.uniform(0.5, 2.0, 2)
        centre = rng.uniform(-1.5, 1.5)
    elif kind == KINDS[4]:
        gap, light, spread = rng.uniform(1.0, 1.8), rng.uniform(0.3, 0.7), rng.uniform(0.05, 0.2, 2)
    else:
        raise ValueError(f"unknown kind {kind!r}")
    weights = np.array([light, 1 - light])
    centres = np.array([centre - (1 - light) * gap, centre + light * gap])     # the mean of the law is `centre`
    spread = np.asarray(spread, dtype=float)
    if rng.random() < 0.5:                                                      # the light bump on the other side
        weights, centres, spread = weights[::-1], (2 * centre - centres)[::-1], spread[::-1]
    return tuple(weights.tolist()), tuple(centres.tolist()), tuple(spread.tolist())


def hidden_series(rng=None):
    """A series of len(KINDS) new hidden laws, one of each kind, in a random order: a list of (law, kind)."""
    rng = np.random.default_rng() if rng is None else rng
    kinds = list(KINDS)
    rng.shuffle(kinds)
    return [(hidden_mixture(rng, kind), kind) for kind in kinds]


def mixture_sd(law):
    """The standard deviation of a mixture (weights, means, variances)."""
    w, m, v = (np.asarray(part, dtype=float) for part in law)
    centre = float(w @ m)
    return math.sqrt(float(w @ (v + m * m)) - centre * centre)


def mixture_cdf(x, law):
    """The distribution function of a mixture (weights, means, variances) at the points x."""
    from scipy.special import ndtr          # this process may use SciPy; the learner's function never runs it

    w, m, v = (np.asarray(part, dtype=float) for part in law)
    x = np.asarray(x, dtype=float)
    return sum(wk * ndtr((x - mk) / math.sqrt(vk)) for wk, mk, vk in zip(w, m, v))


def w1_to_mixture(x, law, n_grid=200_001):
    """W₁ = ∫ |F_n − F| between the empirical law of the points x and the mixture, on a grid of n_grid points that
    covers the points and nine standard deviations of each bump."""
    x = np.sort(np.asarray(x, dtype=float).ravel())
    w, m, v = (np.asarray(part, dtype=float) for part in law)
    lo = min(float(x[0]), float((m - 9 * np.sqrt(v)).min()))
    hi = max(float(x[-1]), float((m + 9 * np.sqrt(v)).max()))
    grid = np.linspace(lo, hi, n_grid)
    empirical = np.searchsorted(x, grid, side="right") / x.size
    return float(np.trapezoid(np.abs(empirical - mixture_cdf(grid, law)), grid))


# --------------------------------------------------------------------------------------------------------------------
# the exact mean field (NumPy only: this file stands alone, without mymath)
# --------------------------------------------------------------------------------------------------------------------
def denoised(y, gain, scale, law):
    """E[x_0 | gain x_0 + scale ε = y] for x_0 of the mixture law (weights, means, variances)."""
    w, m, v = (np.asarray(part, dtype=float) for part in law)
    y = np.asarray(y, dtype=float)
    if gain == 0:
        return np.full(y.shape, float(w @ m))
    total = gain * gain * v + scale * scale
    gap = y.reshape(-1, 1) - gain * m
    logs = np.log(w) - 0.5 * np.log(2 * math.pi * total) - gap * gap / (2 * total)
    resp = np.exp(logs - logs.max(axis=1, keepdims=True))
    resp /= resp.sum(axis=1, keepdims=True)
    return (resp * (m + gain * v / total * gap)).sum(axis=1).reshape(y.shape)


def mean_field(x, s, law):
    """v(x, s) = (x − E[x_0 | x_s = x]) / s on the straight path to the mixture law, for 0 < s ≤ 1."""
    if not 0 < s <= 1:
        raise ValueError(f"the field is defined for 0 < s <= 1, got s = {s!r}")
    return (np.asarray(x, dtype=float) - denoised(x, 1 - s, s, law)) / s


def reference(field, z, steps=4):
    """The method of the corrected version: the midpoint method with `steps` equal steps from s = 1 down to s = 0
    (two calls of the field per step)."""
    pts = np.array(z, dtype=float)
    grid = np.linspace(1.0, 0.0, steps + 1)
    for s_hi, s_lo in zip(grid[:-1], grid[1:]):
        dur = s_lo - s_hi
        probe = pts + 0.5 * dur * field(pts, s_hi)
        pts = pts + dur * field(probe, s_hi + 0.5 * dur)
    return pts


# --------------------------------------------------------------------------------------------------------------------
# the hidden laws of one run, served from another process
# --------------------------------------------------------------------------------------------------------------------
def _floats(stream, n):
    """n little-endian float64 read from the stream, or None if the stream ends first."""
    data = stream.read(8 * n)
    return np.frombuffer(data, dtype="<f8").copy() if len(data) == 8 * n else None


def serve(series=SERIES):
    """``python -I mb5_25.py --serve``: draw ``series`` series of hidden laws from fresh entropy, put the law of the
    notebook after them (the last one), write one JSON line ``{"count": ...}`` (the number of laws, the notebook's
    included), then answer the requests of the check on stdin, one line each:

    - ``F k s n``, followed by n little-endian float64 (points): write n float64, the mean field ``v(x, s)`` of law k
      at these points (NaN when s is not in ]0, 1]); each request counts as one call of the field of law k;
    - ``R k n``, followed by n float64: the points reached for law k (kept);
    - ``verdict``: write one JSON line, for each law in order its series (0 for the notebook's), its kind, its count of
      calls and W₁ divided by its standard deviation (null for points missing or not finite), then stop.

    Any other line, a malformed request or the end of stdin: stop at once (the check stopped, or its kernel died)."""
    drawn = [(law, kind, number) for number in range(1, series + 1)
             for law, kind in hidden_series(np.random.default_rng())] + [(NOTEBOOK_LAW, "le mélange du notebook", 0)]
    calls, reached = [0] * len(drawn), [None] * len(drawn)
    inp, out = sys.stdin.buffer, sys.stdout.buffer
    out.write((json.dumps({"count": len(drawn)}) + "\n").encode())
    out.flush()
    while True:
        words = inp.readline().decode("ascii", "replace").split()
        try:
            if words[:1] == ["F"] and len(words) == 4:
                k, s, n = int(words[1]), float(words[2]), int(words[3])
                if not (0 <= k < len(drawn) and 0 <= n <= MAX_POINTS):
                    return
                x = _floats(inp, n)
                if x is None:
                    return
                calls[k] += 1
                velocity = mean_field(x, s, drawn[k][0]) if 0 < s <= 1 else np.full(n, np.nan)
                out.write(np.asarray(velocity, dtype="<f8").tobytes())
                out.flush()
            elif words[:1] == ["R"] and len(words) == 3:
                k, n = int(words[1]), int(words[2])
                if not (0 <= k < len(drawn) and 1 <= n <= MAX_POINTS):
                    return
                reached[k] = _floats(inp, n)
                if reached[k] is None:
                    return
            elif words == ["verdict"]:
                report = []
                for (law, kind, number), count, x in zip(drawn, calls, reached):
                    ok = x is not None and bool(np.all(np.isfinite(x)))
                    rel = w1_to_mixture(x, law) / mixture_sd(law) if ok else None
                    report.append({"series": number, "kind": kind, "calls": count, "rel": rel})
                out.write((json.dumps(report) + "\n").encode())
                out.flush()
                return
            else:
                return
        except (ValueError, OverflowError, BrokenPipeError):
            return


if __name__ == "__main__" and sys.argv[1:] == ["--serve"]:
    serve()
