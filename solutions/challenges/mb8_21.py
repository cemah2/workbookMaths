"""The hidden part of the challenge 🏆 MB8.21 (chapter MB8): the hidden laws and thresholds, their exact derivatives and
budgets, and the process that serves the draws.

Reference material, like ``solutions/mymath_ref/``. The notebook gives its own case (the phone waits of ✏️ MB8.1: an
exponential law of rate 0.1, the threshold 18, a budget of 10 000 draws; ``NOTEBOOK_CASE`` below) and never reads this
file; the check cell runs it as a script in another process (``python -I mb8_21.py --serve``, :func:`serve`): that
process draws new hidden cases at each run, answers the draw requests of the learner's function and counts them, case by
case, against the budget of the case, and compares the estimates it receives with the exact derivatives only at the
end, so that no hidden law, parameter, derivative nor seed lives in the notebook's process while that function runs.
Reading this file before solving the challenge spoils it.

The challenge. A law ``p_θ`` of a real parameter ``θ`` and a threshold ``c`` are hidden; the learner's function
``derivative_21(draw, c, budget)`` must estimate ``J'(θ) = d/dθ P_θ(X > c)``. It may call ``draw(k, delta=0.0)``,
which returns two arrays of ``k`` floats: ``k`` independent draws ``x_i`` of ``p_{θ + δ}`` and their scores
``s_{θ+δ}(x_i) = ∂ ln p_{θ+δ}(x_i)`` at the parameter of the draw; the draws of all its calls together may not exceed
``budget`` (beyond, ``draw`` returns NaNs, and the case fails). The path derivative of an indicator is 0; finite
differences between independent samples at ``θ ± h`` drown the gap of two close probabilities in their noise; the
plain score estimator ``mean(f(x_i) s(x_i))`` is very noisy when ``P_θ(X > c)`` is close to 1 (``f`` is then almost
always 1, and the estimator is almost the mean of the scores, of variance ``E[s²]``); a constant baseline ``b`` fixes one
end only (``b = 1`` is noisy for a rare event, ``b = ½`` for a very frequent one). A baseline estimated on the draws
(the optimal one ``Σ f s² / Σ s²``, the mean of the other draws, the mean of the sample) works in every case.

- :data:`FAMILIES`: the exponential law of rate ``θ``, the law of Poisson of mean ``θ``, the normal law ``N(θ, σ²)``
  with ``σ`` known to this process only, and the binomial law ``B(m, θ)``.
- :data:`KINDS`: four kinds of thresholds, by the probability ``P_θ(X > c)`` they give (:data:`PROB_RANGES`):
  « très fréquent » (0.988 to 0.998), « fréquent » (0.90 to 0.97), « moyen » (0.36 to 0.70) and « rare » (0.0025 to
  0.008). A series has :data:`PER_SERIES` cases (:data:`COMPOSITION` gives the number of each kind), with families
  drawn at random; :data:`SERIES` series per run: 120 hidden cases, about 17 million draws in all.
- :func:`budget_for` sizes the budget of a case from the one-draw standard deviation ``σ_E`` of the score estimator
  with the baseline ``b = E[f]`` (the mean of the other draws behaves like it): ``⌈(Z σ_E / (TOL |J'|))²⌉`` draws, so
  that a method with a baseline at least that good misses the tolerance with a probability of about
  ``P(|N(0, 1)| > Z)``, about 3·10⁻³.
- Criterion: a case succeeds when ``|estimate − J'(θ)| ≤ TOL |J'(θ)|`` within its budget; the challenge is met when the
  notebook's case succeeds and at least :data:`PASS_FRACTION` of the hidden cases do (« neuf fois sur dix »). Measured
  per run on 200 runs and more (scratchpad of session 76): every adaptive baseline succeeds at every run, and the plain
  estimator, the constant baselines ½ and 1, the path derivative, finite differences, a method frozen on the notebook's
  case or on its family, and a control variate ``x − x̄`` fail at every run (or at most one run in a hundred).

The notebook's case comes last (series 0); for it, the verdict says only whether the estimate is within the tolerance
(its relative error would give back the exact derivative, the answer of ✏️ MB8.1 b).
"""

import json
import math
import sys

import numpy as np

FAMILIES = ("exponentielle", "Poisson", "normale", "binomiale")
KINDS = ("très fréquent", "fréquent", "moyen", "rare")
COMPOSITION = {"très fréquent": 4, "fréquent": 1, "moyen": 1, "rare": 4}
PER_SERIES = sum(COMPOSITION.values())
SERIES = 12                      # series of hidden cases per run: 120 cases
TOL = 0.10                       # the relative tolerance on J'(θ)
Z = 3.0                          # the budget gives the baseline E[f] a standard error of TOL |J'| / Z
PASS_FRACTION = 0.9              # « neuf fois sur dix »
BUDGET_RANGE = (240, 400_000)
MAX_REQUEST = 1_000_000          # the largest number of draws the process accepts in one request
PROB_RANGES = {"très fréquent": (0.988, 0.998), "fréquent": (0.90, 0.97), "moyen": (0.36, 0.70),
               "rare": (0.0025, 0.008)}
NOTEBOOK_CASE = {"family": "exponentielle", "theta": 0.1, "c": 18.0, "sigma": None, "m": None, "budget": 10_000}


# --------------------------------------------------------------------------------------------------------------------
# the laws: sampling, scores, tail probabilities and their exact derivatives (NumPy and math only)
# --------------------------------------------------------------------------------------------------------------------
def _norm_sf(z):
    return 0.5 * math.erfc(z / math.sqrt(2))


def _norm_pdf(z):
    return math.exp(-0.5 * z * z) / math.sqrt(2 * math.pi)


def _poisson_pmf(k, th):
    return math.exp(k * math.log(th) - th - math.lgamma(k + 1)) if k >= 0 else 0.0


def _binom_pmf(k, m, th):
    if k < 0 or k > m:
        return 0.0
    return math.comb(m, k) * th ** k * (1 - th) ** (m - k)


def tail(case, theta=None):
    """P_θ(X > c) for the case (θ of the case unless given)."""
    th, c = case["theta"] if theta is None else theta, case["c"]
    fam = case["family"]
    if fam == "exponentielle":
        return math.exp(-th * c) if c > 0 else 1.0
    if fam == "Poisson":
        k = math.floor(c)
        return 1.0 - sum(_poisson_pmf(j, th) for j in range(k + 1))
    if fam == "normale":
        return _norm_sf((c - th) / case["sigma"])
    if fam == "binomiale":
        k = math.floor(c)
        return 1.0 - sum(_binom_pmf(j, case["m"], th) for j in range(k + 1))
    raise ValueError(f"unknown family {fam!r}")


def exact_derivative(case):
    """J'(θ) = d/dθ P_θ(X > c), in closed form."""
    th, c, fam = case["theta"], case["c"], case["family"]
    if fam == "exponentielle":
        return -c * math.exp(-th * c)
    if fam == "Poisson":
        return _poisson_pmf(math.floor(c), th)
    if fam == "normale":
        s = case["sigma"]
        return _norm_pdf((c - th) / s) / s
    if fam == "binomiale":
        k, m = math.floor(c), case["m"]
        return m * math.comb(m - 1, k) * th ** k * (1 - th) ** (m - 1 - k) if 0 <= k <= m - 1 else 0.0
    raise ValueError(f"unknown family {fam!r}")


def sample(case, k, rng, delta=0.0):
    """k draws of p_{θ+δ} and their scores at θ + δ (two float arrays). An invalid parameter gives NaNs."""
    th, fam = case["theta"] + delta, case["family"]
    if fam == "exponentielle":
        if th <= 0:
            return np.full(k, np.nan), np.full(k, np.nan)
        x = rng.exponential(1 / th, k)
        return x, 1 / th - x
    if fam == "Poisson":
        if th <= 0:
            return np.full(k, np.nan), np.full(k, np.nan)
        x = rng.poisson(th, k).astype(float)
        return x, x / th - 1
    if fam == "normale":
        s = case["sigma"]
        x = rng.normal(th, s, k)
        return x, (x - th) / s ** 2
    if fam == "binomiale":
        if not 0 < th < 1:
            return np.full(k, np.nan), np.full(k, np.nan)
        m = case["m"]
        x = rng.binomial(m, th, k).astype(float)
        return x, (x - m * th) / (th * (1 - th))
    raise ValueError(f"unknown family {fam!r}")


def moments(case):
    """(E[f s²], E[s²], J') for f = 1{X > c}, by exact sums (discrete laws) or closed forms (continuous laws)."""
    th, c, fam = case["theta"], case["c"], case["family"]
    D = exact_derivative(case)
    if fam == "exponentielle":
        P = math.exp(-th * c)
        return P * (1 / th ** 2 + c ** 2), 1 / th ** 2, D          # memorylessness: X = c + Y beyond c
    if fam == "normale":
        s = case["sigma"]
        a = (c - th) / s
        return (a * _norm_pdf(a) + _norm_sf(a)) / s ** 2, 1 / s ** 2, D
    if fam == "Poisson":
        kmax = int(th + 40 * math.sqrt(th) + 60)
        ks = np.arange(kmax)
        p = np.array([_poisson_pmf(int(k), th) for k in ks])
        s = ks / th - 1
    else:
        m = case["m"]
        ks = np.arange(m + 1)
        p = np.array([_binom_pmf(int(k), m, th) for k in ks])
        s = (ks - m * th) / (th * (1 - th))
    f = (ks > c).astype(float)
    return float(np.sum(p * f * s * s)), float(np.sum(p * s * s)), D


def one_draw_sd(case, b):
    """The one-draw standard deviation of (f − b) s, for a constant baseline b."""
    Efs2, Es2, D = moments(case)
    # E[(f − b)² s²] = (1 − 2b) E[f s²] + b² E[s²]   (f² = f)
    return math.sqrt(max((1 - 2 * b) * Efs2 + b * b * Es2 - D * D, 0.0))


def budget_for(case):
    """The budget of a case: Z standard errors of the baseline b = E[f] inside the tolerance TOL |J'|."""
    sd = one_draw_sd(case, tail(case))
    n = math.ceil((Z * sd / (TOL * abs(exact_derivative(case)))) ** 2)
    return int(min(max(n, BUDGET_RANGE[0]), BUDGET_RANGE[1]))


# --------------------------------------------------------------------------------------------------------------------
# the hidden cases
# --------------------------------------------------------------------------------------------------------------------
def _threshold(case, lo, hi, rng):
    """A threshold c with lo ≤ P(X > c) ≤ hi (continuous laws: a target probability drawn in [lo, hi]; discrete laws:
    the half-integer c = k + ½ of an admissible k, at random), or None."""
    fam = case["family"]
    if fam in ("exponentielle", "normale"):
        target = rng.uniform(lo, hi)
        if fam == "exponentielle":
            return -math.log(target) / case["theta"]
        a, b = case["theta"] - 10 * case["sigma"], case["theta"] + 10 * case["sigma"]
        for _ in range(100):                                          # bisection on the decreasing tail
            mid = 0.5 * (a + b)
            if tail(dict(case, c=mid)) > target:
                a = mid
            else:
                b = mid
        return 0.5 * (a + b)
    top = int(case["theta"] + 30 * math.sqrt(case["theta"]) + 40) if fam == "Poisson" else case["m"]
    ks = [k for k in range(0, top) if lo <= tail(dict(case, c=k + 0.5)) <= hi]
    return None if not ks else ks[int(rng.integers(len(ks)))] + 0.5


def hidden_case(rng, kind):
    """A hidden case of the given kind (one of KINDS): a dict family, theta, sigma, m, c, kind, budget."""
    lo, hi = PROB_RANGES[kind]
    while True:
        fam = FAMILIES[int(rng.integers(len(FAMILIES)))]
        case = {"family": fam, "sigma": None, "m": None, "kind": kind}
        if fam == "exponentielle":
            case["theta"] = float(10 ** rng.uniform(-1.25, 0.7))      # rates from about 0.06 to 5
        elif fam == "Poisson":
            case["theta"] = float(rng.uniform(1.5, 12.0))
        elif fam == "normale":
            case["theta"], case["sigma"] = float(rng.uniform(-5, 5)), float(10 ** rng.uniform(-0.5, 0.7))
        else:
            case["m"], case["theta"] = int(rng.integers(8, 41)), float(rng.uniform(0.1, 0.9))
        c = _threshold(case, lo, hi, rng)
        if c is None:
            continue
        case["c"] = float(c)
        if not lo <= tail(case) <= hi or exact_derivative(case) == 0:
            continue
        case["budget"] = budget_for(case)
        if case["budget"] >= BUDGET_RANGE[1]:
            continue
        return case


def hidden_series(rng=None):
    """A series of PER_SERIES new hidden cases (COMPOSITION gives the number of each kind), in a random order."""
    rng = np.random.default_rng() if rng is None else rng
    kinds = [kind for kind in KINDS for _ in range(COMPOSITION[kind])]
    rng.shuffle(kinds)
    return [hidden_case(rng, kind) for kind in kinds]


# --------------------------------------------------------------------------------------------------------------------
# the method of the corrected version (written apart from the notebook's, with its own names)
# --------------------------------------------------------------------------------------------------------------------
def corrected_estimate(sampler, level, allowed):
    """The score method with the optimal constant baseline estimated on the same draws (a control variate: the score,
    of known mean 0): the whole budget at δ = 0, weight_sum = Σ f s², the baseline Σ f s² / Σ s², then the mean of
    (f − baseline) s."""
    points, slopes = sampler(int(allowed))
    hits = np.where(points > level, 1.0, 0.0)
    squares = slopes * slopes
    weight_sum = float(np.dot(hits, squares))
    centre = weight_sum / float(squares.sum())
    return float(np.mean((hits - centre) * slopes))


def success(estimate, case):
    D = exact_derivative(case)
    return estimate is not None and math.isfinite(estimate) and abs(estimate - D) <= TOL * abs(D)


# --------------------------------------------------------------------------------------------------------------------
# the hidden cases of one run, served from another process
# --------------------------------------------------------------------------------------------------------------------
def serve(series=SERIES):
    """``python -I mb8_21.py --serve``: draw ``series`` series of hidden cases from fresh entropy, put the notebook's
    case after them (the last one), write one JSON line ``{"count": ..., "c": [...], "budget": [...]}`` (the thresholds
    and budgets, which the learner's function receives anyway), then answer the requests of the check on stdin, one
    line each:

    - ``D k n delta``: write 2n little-endian float64, n draws of case k at θ + δ, then their n scores; the draws count
      against the budget of case k; a request that would exceed it gets 2n NaNs and marks the case as over budget;
    - ``O k``: mark case k as over budget (the check saw a request beyond the budget, and answered it with NaNs);
    - ``R k value``: the estimate for case k (kept);
    - ``A value``: the answer a) of the notebook (the learner's estimate for the notebook's case, from its own draws);
    - ``verdict``: write one JSON line ``{"cases": [...], "answer": ...}``: for each case in order its series (0 for
      the notebook's), its kind, its family (revealed only now), its budget, the draws used, whether it went over
      budget, the relative error (``None`` for the notebook's case, and for an estimate that is missing or not finite)
      and whether it succeeds; for the answer a), whether it was given and whether it is within the tolerance of the
      notebook's case; then stop.

    Any other line, a malformed request or the end of stdin: stop at once."""
    rng = np.random.default_rng()
    drawn = [(case, number) for number in range(1, series + 1) for case in hidden_series(rng)]
    drawn.append((dict(NOTEBOOK_CASE, kind="le cas d'essai"), 0))
    used, over, estimate = [0] * len(drawn), [False] * len(drawn), [None] * len(drawn)
    answer = None
    inp, out = sys.stdin.buffer, sys.stdout.buffer
    out.write((json.dumps({"count": len(drawn), "c": [cs["c"] for cs, _ in drawn],
                           "budget": [cs["budget"] for cs, _ in drawn]}) + "\n").encode())
    out.flush()
    while True:
        words = inp.readline().decode("ascii", "replace").split()
        try:
            if words[:1] == ["D"] and len(words) == 4:
                k, n, delta = int(words[1]), int(words[2]), float(words[3])
                if not (0 <= k < len(drawn) and 0 <= n <= MAX_REQUEST and math.isfinite(delta)):
                    return
                case = drawn[k][0]
                if used[k] + n > case["budget"] or over[k]:
                    over[k] = True
                    out.write(np.full(2 * n, np.nan, dtype="<f8").tobytes())
                else:
                    used[k] += n
                    x, s = sample(case, n, rng, delta)
                    out.write(np.concatenate([x, s]).astype("<f8").tobytes())
                out.flush()
            elif words[:1] == ["O"] and len(words) == 2:
                k = int(words[1])
                if not 0 <= k < len(drawn):
                    return
                over[k] = True
            elif words[:1] == ["R"] and len(words) == 3:
                k, value = int(words[1]), float(words[2])
                if not 0 <= k < len(drawn):
                    return
                estimate[k] = value
            elif words[:1] == ["A"] and len(words) == 2:
                answer = float(words[1])
            elif words == ["verdict"]:
                report = []
                for (case, number), u, o, e in zip(drawn, used, over, estimate):
                    D = exact_derivative(case)
                    rel = abs(e - D) / abs(D) if e is not None and math.isfinite(e) else None
                    report.append({"series": number, "kind": case["kind"], "family": case["family"],
                                   "budget": case["budget"], "used": u, "over_budget": o,
                                   "rel": None if number == 0 else rel, "ok": (not o) and success(e, case)})
                notebook = drawn[-1][0]
                out.write((json.dumps({"cases": report, "answer": {
                    "given": answer is not None and math.isfinite(answer),
                    "ok": answer is not None and success(answer, notebook)}}) + "\n").encode())
                out.flush()
                return
            else:
                return
        except (ValueError, OverflowError, BrokenPipeError):
            return


if __name__ == "__main__" and sys.argv[1:] == ["--serve"]:
    serve()
