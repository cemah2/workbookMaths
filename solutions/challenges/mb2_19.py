"""The hidden part of the challenge 🏆 MB2.19 (chapter MB2): the hidden joint laws of the check.

Reference material, like ``solutions/mymath_ref/``. The notebook gives its own table of counts (``COUNTS_19``, a literal
of its cell, whose five pairs are the hidden answers MB2.19k to MB2.19o) and never reads this file; the check cell runs
it as a script in another process (``python -I mb2_19.py --serve``, :func:`serve`): that process draws three new hidden
laws at each run and 3 000 sales from each, sends the counts only, receives the five pairs that the learner's function
chooses for each table, and answers with how many of them are among the five most associated pairs of the hidden law,
so that neither a hidden law nor its five pairs live in the notebook's process. Reading this file before solving the
challenge spoils it.

:func:`hidden_law` draws a 10 × 10 joint law: two rare rows and two rare columns; one dominant row and one dominant
column, whose common cell is the most probable of the table but not associated (its PMI is about 0); five cells boosted
3 to 4 times, on distinct rows and columns of the others: the five most associated pairs, each with 3 000 × p ≥ 40 and a
PMI at least 0.3 above the sixth.
"""

import json
import sys

import numpy as np

TABLES = 3            # the hidden tables drawn at each run of the check
SALES = 3000          # the sales drawn from each hidden law


def pmi(law):
    """The table of the PMI of a joint law, -inf on its empty cells."""
    law = np.asarray(law, dtype=float)
    px, py = law.sum(axis=1, keepdims=True), law.sum(axis=0, keepdims=True)
    out = np.full(law.shape, -np.inf)
    nonzero = law > 0
    out[nonzero] = np.log(law[nonzero] / (px * py)[nonzero])
    return out


def hidden_law(rng):
    """A hidden 10 × 10 joint law drawn by rng (the docstring of the module says what it holds)."""
    while True:
        px, py = rng.uniform(0.7, 1.3, 10), rng.uniform(0.7, 1.3, 10)
        rr, rc = rng.choice(10, 3, replace=False), rng.choice(10, 3, replace=False)
        px[rr[:2]], py[rc[:2]] = rng.uniform(0.01, 0.04, 2), rng.uniform(0.01, 0.04, 2)
        px[rr[2]], py[rc[2]] = rng.uniform(3.5, 4.5), rng.uniform(3.5, 4.5)
        law = np.outer(px, py) * np.exp(rng.normal(0.0, 0.08, (10, 10)))
        rows = rng.permutation([i for i in range(10) if i not in rr])[:5]
        cols = rng.permutation([j for j in range(10) if j not in rc])[:5]
        law[rows, cols] *= rng.uniform(3.0, 4.0, 5)
        law /= law.sum()
        T = pmi(law).ravel()
        order = np.argsort(-T)
        top = {(int(k // 10), int(k % 10)) for k in order[:5]}
        if (top == set(zip(rows.tolist(), cols.tolist())) and T[order[4]] - T[order[5]] > 0.3
                and SALES * min(law[i, j] for i, j in top) >= 40 and law.argmax() == rr[2] * 10 + rc[2]):
            return law


def top5(law):
    """The five cells of largest PMI of a hidden law, as a set of pairs (row, column)."""
    T = pmi(law)
    return {(int(i), int(j)) for i, j in zip(*np.unravel_index(np.argsort(-T, axis=None, kind="stable")[:5], T.shape))}


def score(law, pairs):
    """How many of the five pairs are among the five most associated pairs of the law; None for an answer that is not
    five distinct pairs of integers from 0 to 9."""
    try:
        chosen = [(int(i), int(j)) for i, j in pairs]
    except (TypeError, ValueError):
        return None
    if len(chosen) != 5 or len(set(chosen)) != 5 or not all(0 <= v < 10 for pair in chosen for v in pair):
        return None
    return len(set(chosen) & top5(law))


def serve(tables=TABLES):
    """``python -I mb2_19.py --serve``: draw ``tables`` hidden laws from fresh entropy and ``SALES`` sales from each;
    write one JSON line, ``{"counts": [table, ...]}`` (lists of lists of integers); read one JSON line, the five pairs
    of the learner's function for each table, in order (null for a table it could not do); write one JSON line, the
    score of each table (null for an answer that is not five distinct pairs), then stop. Any other input, or the end of
    stdin: stop at once."""
    rng = np.random.default_rng()
    laws = [hidden_law(rng) for _ in range(tables)]
    counts = [rng.multinomial(SALES, law.ravel()).reshape(law.shape) for law in laws]
    out = sys.stdout.buffer
    out.write((json.dumps({"counts": [c.tolist() for c in counts]}) + "\n").encode())
    out.flush()
    try:
        answers = json.loads(sys.stdin.buffer.readline().decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return
    if not isinstance(answers, list) or len(answers) != len(laws):
        return
    out.write((json.dumps([score(law, pairs) for law, pairs in zip(laws, answers)]) + "\n").encode())
    out.flush()


if __name__ == "__main__" and sys.argv[1:] == ["--serve"]:
    serve()
