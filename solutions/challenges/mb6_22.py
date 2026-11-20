"""The hidden part of the challenge 🏆 MB6.22 (chapter MB6): the hidden councils and the method of the corrected
version.

Reference material, like ``solutions/mymath_ref/``. The notebook gives its own council (``WEIGHTS_22`` and ``QUOTA_22``,
literals of its data cell) and never reads this file; the check cell runs it as a script in another process
(``python -I mb6_22.py --serve``, :func:`serve`): that process draws three new series of five hidden councils at each
run, sends them (weights and quotas only), receives the indices computed by the learner's function, and answers with
the largest gap of each council to the exact indices, so that no exact index of a hidden council (nor a seed, nor a
kind) lives in the notebook's process. The council of the notebook is measured there too (it comes last). Reading this
file before solving the challenge spoils it.

The challenge. In a weighted voting game ``[q ; ω_1, …, ω_n]`` with small positive integer weights, the Shapley-Shubik
index of member ``i`` is ``φ_i = Σ_s w(s) N_i(s)``, where ``w(s) = s! (n − 1 − s)! / n!`` and ``N_i(s)`` counts the
coalitions of ``s`` other members whose total weight ``t`` satisfies ``q − ω_i ≤ t ≤ q − 1`` (member ``i`` is pivot
after them). ``N_i(s)`` comes from a table of counts indexed by (size, total weight) of the coalitions of the other
members, built member by member: adding a member of weight ``ω`` turns the table ``c`` into
``c'[s][t] = c[s][t] + c[s − 1][t − ω]``. A total weight of ``q`` or more never matters: ``n × q`` cells suffice.

The hidden councils have 30 to 50 members: the ``2^29`` to ``2^49`` coalitions without a member cannot be listed one by
one, neither in time nor in memory. Five kinds (:data:`KINDS`), one of each per series:

- « majorité simple » : weights 1 to 8, ``q = ⌊W/2⌋ + 1`` ;
- « majorité qualifiée » : weights 1 to 8, ``q = ⌈rW⌉`` with ``r`` = 3/5, 2/3 or 3/4 ;
- « un membre au veto » : one member of weight 10 to 16, the others 1 to 5, and a quota above ``W − ω_max`` (the big
  member is in every winning coalition) ;
- « quelques grands et beaucoup de petits » : 3 to 5 members of weight 10 to 15, the others 1 to 3 ;
- « des poids presque égaux » : weights 3 or 4, plus one to three members of weight 1 or 5 (the indices are close to
  ``1/n``, but not equal).

Every hidden council has at least three distinct weights, and its normalized weights miss its indices by more than
``10⁻⁴``. Criterion: for the council of the notebook and for each of the fifteen hidden councils, the largest gap
between the learner's indices and those of :func:`exact_indices` is at most :data:`TOL` = ``10⁻⁹`` (a computation in
64-bit floats agrees to about ``10⁻¹⁵``; counts kept in 32-bit floats miss by ``10⁻⁹`` to ``10⁻⁸``; a Monte Carlo
estimate, by ``10⁻³``). The time limit of the check (five minutes for the fifteen councils) only stops a runaway
computation: the method below takes about 0.02 s per council.
"""

import json
import math
import sys
from fractions import Fraction

import numpy as np

KINDS = ("majorité simple", "majorité qualifiée", "un membre au veto", "quelques grands et beaucoup de petits",
         "des poids presque égaux")
SERIES = 3                     # the series of len(KINDS) hidden councils drawn at each run of the check
TOL = 1e-9                     # the largest gap allowed between the learner's indices and the exact ones
SIZES = (30, 50)               # the numbers of members of the hidden councils
NOTEBOOK_WEIGHTS = (12, 9, 9, 7, 6, 6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1)   # WEIGHTS_22
NOTEBOOK_QUOTA = 66                                                                              # QUOTA_22


# --------------------------------------------------------------------------------------------------------------------
# the method of the corrected version
# --------------------------------------------------------------------------------------------------------------------
def exact_indices(council_votes, council_quota):
    """The Shapley-Shubik indices of [council_quota ; council_votes] (positive integers), as floats: for each member,
    the table of the counts of the coalitions of the other members by (size, total weight below the quota), filled
    member by member with NumPy (the counts stay below 2^53, so the floats hold them exactly)."""
    votes_list = [int(v) for v in council_votes]
    size_n, quota_q = len(votes_list), int(council_quota)
    share_of_size = np.array([1.0 / (size_n * math.comb(size_n - 1, size)) for size in range(size_n)])
    result = np.zeros(size_n)
    for member in range(size_n):
        counts_grid = np.zeros((size_n, quota_q))
        counts_grid[0, 0] = 1.0
        for other, other_votes in enumerate(votes_list):
            if other != member and other_votes < quota_q:      # a member of weight >= q never adds a losing coalition
                counts_grid[1:, other_votes:] += counts_grid[:-1, :quota_q - other_votes].copy()
        lowest = max(quota_q - votes_list[member], 0)
        result[member] = float(share_of_size @ counts_grid[:, lowest:quota_q].sum(axis=1))
    return result.tolist()


def exact_fractions(council_votes, council_quota):
    """The same indices in Python integers and Fractions (for the checks of this module)."""
    votes_list = [int(v) for v in council_votes]
    size_n, quota_q = len(votes_list), int(council_quota)
    found = []
    for member in range(size_n):
        rows = [[0] * quota_q for _ in range(size_n)]
        rows[0][0] = 1
        for other, other_votes in enumerate(votes_list):
            if other == member or other_votes >= quota_q:
                continue
            for size in range(size_n - 1, 0, -1):
                upper, lower = rows[size], rows[size - 1]
                for total in range(quota_q - 1, other_votes - 1, -1):
                    upper[total] += lower[total - other_votes]
        lowest = max(quota_q - votes_list[member], 0)
        found.append(sum(Fraction(math.factorial(size) * math.factorial(size_n - 1 - size), math.factorial(size_n))
                         * sum(rows[size][lowest:quota_q]) for size in range(size_n)))
    return found


# --------------------------------------------------------------------------------------------------------------------
# the hidden councils
# --------------------------------------------------------------------------------------------------------------------
def hidden_council(rng, kind):
    """A hidden council of the given kind (one of KINDS), drawn by rng: (weights, quota), a tuple of ints and an int."""
    size_n = int(rng.integers(SIZES[0], SIZES[1] + 1))
    while True:
        if kind == KINDS[0]:
            drawn = rng.integers(1, 9, size_n)
            quota_q = int(drawn.sum()) // 2 + 1
        elif kind == KINDS[1]:
            drawn = rng.integers(1, 9, size_n)
            ratio = (Fraction(3, 5), Fraction(2, 3), Fraction(3, 4))[int(rng.integers(0, 3))]
            quota_q = math.ceil(ratio * int(drawn.sum()))
        elif kind == KINDS[2]:
            drawn = np.concatenate([[int(rng.integers(10, 17))], rng.integers(1, 6, size_n - 1)])
            total, big = int(drawn.sum()), int(drawn[0])
            quota_q = total - big + 1 + int(rng.integers(0, big // 3 + 1))
        elif kind == KINDS[3]:
            large = int(rng.integers(3, 6))
            drawn = np.concatenate([rng.integers(10, 16, large), rng.integers(1, 4, size_n - large)])
            total = int(drawn.sum())
            quota_q = total // 2 + 1 if rng.random() < 0.5 else math.ceil(2 * total / 3)
        elif kind == KINDS[4]:
            odd = int(rng.integers(1, 4))
            drawn = np.concatenate([rng.choice([3, 4], size_n - odd), rng.choice([1, 5], odd)])
            quota_q = int(drawn.sum()) // 2 + 1
        else:
            raise ValueError(f"unknown kind {kind!r}")
        votes = tuple(int(v) for v in rng.permutation(drawn))
        if len(set(votes)) < 3:
            continue
        power = np.array(exact_indices(votes, quota_q))
        if np.abs(power - np.array(votes) / sum(votes)).max() <= 1e-4:
            continue
        return votes, quota_q


def hidden_series(rng=None):
    """A series of len(KINDS) new hidden councils, one of each kind, in a random order: a list of (council, kind)."""
    rng = np.random.default_rng() if rng is None else rng
    kinds = list(KINDS)
    rng.shuffle(kinds)
    return [(hidden_council(rng, kind), kind) for kind in kinds]


def largest_gap(answer, council):
    """The largest gap between an answer (a list of numbers, one per member) and the exact indices of the council;
    None for an answer missing, of the wrong length or not finite."""
    try:
        values = np.asarray(answer, dtype=float)
    except (TypeError, ValueError):
        return None
    if values.shape != (len(council[0]),) or not np.all(np.isfinite(values)):
        return None
    return float(np.abs(values - np.array(exact_indices(*council))).max())


# --------------------------------------------------------------------------------------------------------------------
# the councils of one run, measured in another process
# --------------------------------------------------------------------------------------------------------------------
def serve(series=SERIES):
    """``python -I mb6_22.py --serve``: draw ``series`` series of hidden councils from fresh entropy; write one JSON
    line, ``{"councils": [[weights, quota], ...]}`` (the hidden councils only); read one JSON line, the learner's
    indices for each hidden council in order, then for the council of the notebook (a list of lists of numbers, null
    for a council the function could not do); write one JSON line, for each council its series (0 for the notebook's),
    its kind, its number of members and the largest gap to the exact indices (null if the answer is missing, of the
    wrong length or not finite), then stop. Any other input, or the end of stdin: stop at once."""
    drawn = [(council, kind, number) for number in range(1, series + 1)
             for council, kind in hidden_series(np.random.default_rng())]
    out = sys.stdout.buffer
    out.write((json.dumps({"councils": [[list(c[0]), c[1]] for c, _, _ in drawn]}) + "\n").encode())
    out.flush()
    try:
        answers = json.loads(sys.stdin.buffer.readline().decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return
    everything = drawn + [((NOTEBOOK_WEIGHTS, NOTEBOOK_QUOTA), "le conseil du notebook", 0)]
    if not isinstance(answers, list) or len(answers) != len(everything):
        return
    report = [{"series": number, "kind": kind, "n": len(council[0]), "gap": largest_gap(answer, council)}
              for (council, kind, number), answer in zip(everything, answers)]
    out.write((json.dumps(report) + "\n").encode())
    out.flush()


if __name__ == "__main__" and sys.argv[1:] == ["--serve"]:
    serve()
