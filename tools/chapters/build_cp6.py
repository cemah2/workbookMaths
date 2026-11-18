#!/usr/bin/env python
"""Build the two notebooks of the mock exam CP6 from a single source (used by Claude).

    python tools/chapters/build_cp6.py
    python tools/run_all_notebooks.py checkpoints/partie_6/03_examen_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py checkpoints/partie_6/02_examen_notebook.ipynb

Same mechanism as build_cp5.py: the exam of CP6 is on paper only (01_examen_sujet.md), and the exam notebook is the
check done AFTER the exam; nothing is checked while EXAM_OVER is False, so that « Run all » goes to the end.
Wrong-answer messages state a rule or ask a question, never a number of the answer, the calculation that gives it,
its last step, nor another sub-question. The solutions notebook records the answers, each one computed from the
numbers of the statement, with NumPy (Cholesky factor, eigenvalues, matrix powers) and exact fractions (the
conditional laws, the KL terms, the chains, the Bellman system, the game, the double centring, the truncated chain
and its stationary law), cross-checked by asserts (Monte Carlo estimates of the KL, of a covariance and of the bias
of a distance, the end as an absorbing state, the series Σ Pᵏ r, every pairing of the two samples, a grid of mixed
strategies, the distances given back by the map, the brute force of the top-p sets, the power method); each wrong
value is computed by the slip its message names. The cells are tagged `answer` and read by build_answers.py.
Not in the notebook: the true/false quiz CP6.Q1, the proof CP6.8, the corrections of CP6.9 b) and the
justifications « sur ta copie ».

The answers are typed as TEXT (one cell per question, a RAW string between triple quotes, r'''...''' with double
quotes, one line « a) value » per sub-question, as on the answer sheet), so that nothing typed can stop a cell: a
decimal comma (0,0264), a French list (0,83 ; -2,6), a missing bracket or pasted LaTeX ($\\xi$, \\frac, \\N: the
simulated candidate of CP6 crashed a cell with a plain triple-quoted block) gives a message, never the SyntaxError
that stopped « Run all » for the simulated candidate of CP5; the block is cut at line feeds only (a pasted \\f or
\\v is no line break). Each value is read as a calculator reads it (0.83, 3/8, sqrt(7), ln(7), -ln(0,79): a decimal
comma inside a calculation of one number is read); a lone number with a decimal comma goes to wbm as a text (wbm
reads it); a list with semicolons is read with decimal commas; a list that mixes « 4,1 » and « , » gets a message,
and so does a set between braces (no order); the fractions and the letters go to wbm as texts. A line pasted from
the answer sheet 04_mes_reponses.md is read too (« - a) L = [[4, 0], [3, 2]] »: what follows the last equals sign or
colon), a matrix may span several lines, a second line for the same letter replaces the first. Then wbm.check
decides, as in CP5. The map of CP6.6 d) is a matrix of one column: [[5], [1], [-6]], and also the flat list of its
values, [5, 1, -6] or with semicolons, are read as such (COLUMNS). 43 checks (CP6.7 f) was removed at step 3 to
shorten the exam); besides the wrong values of s68/reponses_cp6.md (version 2), the simulated candidate of CP6 added
0.14 in CP6.4 b) (two years at the rate of the young plot: a rounding message before), Σ1 without its off-diagonal
terms in CP6.2 b), [34, 7] in CP6.1 d), 2/3 in CP6.3 b) and the traces divided by the total number of days in CP6.7
d) and e). A line without a sub-question letter (a working line pasted from the answer sheet) is ignored with a calm
warning. The letters of CP6.9 a) get a message that depends on their number only (4, 5 or 6 letters among A to H),
never one that tells which letters are right.

Decimals, as the column « Réponse attendue » of the statement says: « valeur exacte » (a decimal with few decimals)
is recorded with decimals=6, the convention of the repository for an exact value, so that the value is accepted as
it is and a rounded value is told « donne la valeur exacte », never « l'énoncé en demande 4 »; « 4 décimales »,
« 3 décimales » and « 2 décimales » are recorded with those decimals; the lists of eigenvalues
(CP6.6 c, CP6.7 a) are exact (decimals=6), never refused for not being integers;
the answers « entier(s) » are whole numbers. The order counts in every list but the letters of CP6.9 a) (« dans
n'importe quel ordre »); the fractions are asked irreducible because the statement says so. A wrong value that a
learner writes rounded (a repeating or irrational wrong value where the statement asks for an exact value) is
recorded exact and rounded to 4, 3 and 2 decimals (as_typed), so that a mistake of substance gets its message, never
a message about rounding (the slip of CP5.5 h); wbm looks the mistakes up before any rounding diagnosis.

The data are those of 01_examen_sujet.md, session 68 (step 3, after the reviews and the simulated candidate): a calf, μ = (40, 55),
Σ = [[16, 12], [12, 13]], ε = (1, −2.5) (CP6.1); two pollutants and a slerp of u = (2, 2, 1), v = (0, 3, 0) (CP6.2);
germination times 22, 27, 36 h of seeds from two bags, σ² = 16 (CP6.3); vine plots, a row that ends,
r = (0, 22, 6), γ = 1 (CP6.4); a poacher and a warden, and two nurseries (CP6.5); three aligned buoys, AB² = 16,
AC² = 121, BC² = 49, a Gram matrix of rank 1 (CP6.6); two solar farms, Σ_A = [[12, 2], [2, 9]], Σ_B = 4 Σ_A, a) to e)
(CP6.7); the letters ACEGH (CP6.9 a); a charging station with three states, top-p m = 0.68, whose
total variation distance was removed: the old g) and h) are now f) and g) (CP6.10). They were chosen and checked
against both repositories by the author of the statement. Seeds 6801 to 6803 (the Monte Carlo checks).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import Paper, check_unique_keys, md  # noqa: E402
from nbbuild import badge, code, setup_cell, write_notebook  # noqa: E402

FOLDER = "checkpoints/partie_6"
EXAM = f"{FOLDER}/02_examen_notebook.ipynb"
SOLUTIONS = f"{FOLDER}/03_examen_solutions.ipynb"
MINUTES = 111                       # the sum of the durations of CP6.Q1 to CP6.10 in the syllabus

EXACT = "(exact values)"
ONE_EXACT = "(exact value)"
FRACTION = "an irreducible fraction, like 3/8"
LETTERS = "the letters, in any order, like ABCDE"
COLUMN = "a matrix with 3 rows and 1 column"

PAPER_CONTEXT = r'''# The answers are computed from the numbers of the statement (01_examen_sujet.md), with NumPy and exact fractions
import math
from fractions import Fraction
from itertools import combinations, permutations

import numpy as np


def floats(a):
    """Fractions or floats (a number, nested lists or an array) as plain floats."""
    return np.asarray(a, dtype=float).tolist()


def ints(a):
    """An array (or nested lists) of whole numbers as lists of int, after checking that every value is whole."""
    arr = np.asarray(a, dtype=float)
    assert np.allclose(arr, np.round(arr)), arr
    return np.round(arr).astype(int).tolist()


def fr(x):
    """A number of the statement, written as text ("0.45") or as an int, as an exact fraction."""
    return Fraction(x)


def fmat(rows):
    return [[fr(x) for x in row] for row in rows]


def fmatmul(p, q):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*q)] for row in p]


def fmatvec(p, v):
    return [sum(a * b for a, b in zip(row, v)) for row in p]


def fvecmat(v, p):
    """A row vector times a matrix (the row convention of the chains)."""
    return [sum(a * b for a, b in zip(v, col)) for col in zip(*p)]


def ftranspose(p):
    return [list(col) for col in zip(*p)]


def finv2(p):
    """The inverse of a 2 x 2 matrix of fractions."""
    (a, b), (c, d) = p
    det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]]


def fsolve(a, b):
    """The solution x of a x = b, by Gauss-Jordan elimination on fractions."""
    n = len(a)
    m = [list(row) + [b_i] for row, b_i in zip(a, b)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if m[r][col] != 0)
        m[col], m[pivot] = m[pivot], m[col]
        m[col] = [x / m[col][col] for x in m[col]]
        for r in range(n):
            if r != col and m[r][col] != 0:
                m[r] = [x - m[r][col] * y for x, y in zip(m[r], m[col])]
    return [row[-1] for row in m]


def fsqrt(q):
    """The exact square root of a fraction that is a perfect square (25 -> 5)."""
    q = Fraction(q)
    num, den = math.isqrt(q.numerator), math.isqrt(q.denominator)
    assert num * num == q.numerator and den * den == q.denominator, q
    return Fraction(num, den)


def as_typed(value, right, places=(4, 3, 2), decimals=6):
    """A wrong value as a learner may write it where the statement asks for an exact value: exact, then rounded to 4,
    3 and 2 decimals, without the roundings that are the same value at the recorded decimals, or the right answer.
    A set for a number (wbm gives one message to all), a list of variants for a list (see same_message)."""
    def key(v):
        return tuple(np.round(np.ravel(np.asarray(v, dtype=float)), decimals))

    seen, variants = {key(right)}, []
    for v in [value] + [np.round(np.asarray(value, dtype=float), k) for k in places]:
        v = floats(v)
        if key(v) not in seen:
            seen.add(key(v))
            variants.append(v)
    return set(variants) if np.ndim(value) == 0 else variants


def same_message(message, values):
    """One message for several wrong values of a list or of a fraction (wbm takes one value per message there): the
    keys differ by trailing spaces, which the message shown leaves out."""
    return {message + " " * i: v for i, v in enumerate(values)}


# CP6.1: the birth mass x1 and the mass at one month x2 of a calf (kg)
MU_1, S_1 = [fr(40), fr(55)], fmat([[16, 12], [12, 13]])
X1_1, X2_1, EPS_1, M_1 = fr(48), fr("48.5"), [fr(1), fr("-2.5")], fmat([[0, 4], [2, 3]])
L_1 = np.linalg.cholesky(np.array(floats(S_1)))
assert np.allclose(L_1 @ L_1.T, floats(S_1)) and L_1[0, 1] == 0 and (np.diag(L_1) > 0).all()
L11_1 = math.sqrt(S_1[0][0])
L21_1 = float(S_1[1][0]) / L11_1
assert np.allclose(L_1, [[L11_1, 0], [L21_1, math.sqrt(S_1[1][1] - L21_1 ** 2)]])   # the formulas of M25a
L_ROOT_1 = [[L11_1, 0], [L21_1, math.sqrt(S_1[1][1])]]                 # l22 = √Σ22: the l21² forgotten
L21_SIGMA_1 = float(S_1[1][0] / S_1[0][0])                             # Σ21 divided by Σ11, not by l11
L_SIGMA_1 = [[L11_1, 0], [L21_SIGMA_1, math.sqrt(S_1[1][1] - L21_SIGMA_1 ** 2)]]


def conditional(read, other, value, s=S_1, mu=MU_1):
    """The law of x_other given x_read = value, [mean, variance] (the Schur complement), exactly."""
    gain = s[other][read] / s[read][read]
    return [mu[other] + gain * (value - mu[read]), s[other][other] - gain * s[read][other]]


MARG_1 = [MU_1[1], S_1[1][1]]
C21_1 = conditional(0, 1, X1_1)
C12_1 = conditional(1, 0, X2_1)
assert math.isclose(C21_1[1], L_1[1, 1] ** 2)                          # var(x2 | x1) = l22²
MARG_COND_1 = [MU_1[1], C21_1[1]]                                     # the variance read given x1
MARG_SD_1 = [float(MU_1[1]), math.sqrt(S_1[1][1])]
C21_OTHER_1 = [MU_1[1] + S_1[1][0] / S_1[1][1] * (X1_1 - MU_1[0]), S_1[1][1] - S_1[1][0] ** 2 / S_1[1][1]]
C21_MEAN_1 = [MU_1[1] + S_1[1][0] / S_1[0][0] * (X1_1 - MU_1[1]), C21_1[1]]   # the gap read from the other mean
C12_OTHER_1 = [MU_1[0] + S_1[0][1] / S_1[0][0] * (X2_1 - MU_1[1]), S_1[0][0] - S_1[0][1] ** 2 / S_1[0][0]]
C12_SIGN_1 = [MU_1[0] - S_1[0][1] / S_1[1][1] * (X2_1 - MU_1[1]), C12_1[1]]
DRAW_1 = (np.array(floats(MU_1)) + L_1 @ floats(EPS_1)).tolist()
DRAW_T_1 = (np.array(floats(MU_1)) + L_1.T @ floats(EPS_1)).tolist()   # Lᵀ in place of L
DRAW_S_1 = floats([m + e for m, e in zip(MU_1, fmatvec(S_1, EPS_1))])  # Σ in place of L
DRAW_0_1 = (L_1 @ floats(EPS_1)).tolist()                              # the mean forgotten
COV_M_1 = fmatmul(M_1, ftranspose(M_1))
RNG_1 = np.random.default_rng(6801)
E_1 = RNG_1.standard_normal((200_000, 2))
assert np.allclose(np.cov((E_1 @ np.array(floats(M_1)).T).T), floats(COV_M_1), atol=0.2)   # the draws M ε

# CP6.2 (1): two pollutants, the true law p0 and the model p1
MU0_2, S0_2 = [fr(1), fr(0)], fmat([[5, 3], [3, 4]])
MU1_2, S1_2 = [fr(3), fr(1)], fmat([[4, 2], [2, 2]])
D_2 = [b - a for a, b in zip(MU0_2, MU1_2)]


def det2(s):
    return s[0][0] * s[1][1] - s[0][1] * s[1][0]


def trace(s):
    return sum(s[i][i] for i in range(len(s)))


def kl_terms(m0, s0, m1, s1):
    """The three terms of KL(N(m0, s0) ‖ N(m1, s1)) in dimension 2: tr(s1⁻¹ s0), δᵀ s1⁻¹ δ and ln(det s1 / det s0)."""
    inv = finv2(s1)
    delta = [b - a for a, b in zip(m0, m1)]
    return trace(fmatmul(inv, s0)), sum(d * x for d, x in zip(delta, fmatvec(inv, delta))), math.log(det2(s1) / det2(s0))


def kl_gauss(m0, s0, m1, s1):
    tr, q, ln = kl_terms(m0, s0, m1, s1)
    return 0.5 * (float(tr) + float(q) - len(m0) + ln)


TR_2, Q_2, LN_2 = kl_terms(MU0_2, S0_2, MU1_2, S1_2)
KL_2 = kl_gauss(MU0_2, S0_2, MU1_2, S1_2)


def log_density(x, m, s):
    s = np.array(floats(s))
    d = x - np.array(floats(m))
    return -0.5 * np.einsum("ni,ij,nj->n", d, np.linalg.inv(s), d) - 0.5 * math.log(np.linalg.det(2 * math.pi * s))


RNG_2 = np.random.default_rng(6802)
SAMPLE_2 = RNG_2.multivariate_normal(floats(MU0_2), floats(S0_2), size=200_000)
assert abs(np.mean(log_density(SAMPLE_2, MU0_2, S0_2) - log_density(SAMPLE_2, MU1_2, S1_2)) - KL_2) < 0.01   # E_p0
TR_SWAP_2 = kl_terms(MU0_2, S1_2, MU1_2, S0_2)[0]                    # tr(Σ0⁻¹Σ1)
TR_COF_2 = TR_2 * det2(S1_2)                                       # the cofactors not divided by the determinant
TR_PROD_2 = trace(finv2(S1_2)) * trace(S0_2)
Q_DIRECT_2 = sum(d * x for d, x in zip(D_2, fmatvec(S1_2, D_2)))   # Σ1 in place of its inverse
Q_OTHER_2 = sum(d * x for d, x in zip(D_2, fmatvec(finv2(S0_2), D_2)))
Q_PLAIN_2 = sum(d * d for d in D_2)
Q_DIAG_2 = sum(d * d / s for d, s in zip(D_2, (S1_2[0][0], S1_2[1][1])))   # Σ1 without its off-diagonal terms
KL_LOG_2 = 0.5 * (float(TR_2) + float(Q_2) - 2 - LN_2)             # ln(det Σ0 / det Σ1)
KL_NO_D_2 = 0.5 * (float(TR_2) + float(Q_2) + LN_2)                # the dimension not subtracted
KL_NO_HALF_2 = float(TR_2) + float(Q_2) - 2 + LN_2
KL_REVERSE_2 = kl_gauss(MU1_2, S1_2, MU0_2, S0_2)

# CP6.2 (2): u and v, of the same norm, and the slerp at t = 1/4
U_2, V_2, T_2 = np.array([2.0, 2, 1]), np.array([0.0, 3, 0]), 0.25
NORM_2 = float(np.linalg.norm(U_2))
assert math.isclose(NORM_2, np.linalg.norm(V_2))
OMEGA_2 = math.acos(U_2 @ V_2 / NORM_2 ** 2)
DEGREES_2 = math.degrees(OMEGA_2)


def slerp(u, v, t, omega=OMEGA_2):
    return (math.sin((1 - t) * omega) * u + math.sin(t * omega) * v) / math.sin(omega)


SLERP_2 = slerp(U_2, V_2, T_2)
assert math.isclose(np.linalg.norm(SLERP_2), NORM_2) and math.isclose(math.acos(SLERP_2 @ U_2 / NORM_2 ** 2), T_2 * OMEGA_2)
ASIN_2 = math.degrees(math.asin(U_2 @ V_2 / NORM_2 ** 2))
SWAPPED_2 = slerp(V_2, U_2, T_2)                                   # the two coefficients exchanged
LINE_2 = (1 - T_2) * U_2 + T_2 * V_2
PROJECTED_2 = NORM_2 * LINE_2 / np.linalg.norm(LINE_2)            # the straight point brought back to the sphere
LINE_NORM_2 = float(np.linalg.norm(LINE_2))
MIDDLE_2 = float(np.linalg.norm((U_2 + V_2) / 2))

# CP6.3: delivery times (h), two warehouses, a known common variance, one EM step on the weight and the means
PI_3, MU_3, S2_3, X_3 = np.array([0.62, 0.38]), np.array([24.0, 32.0]), 16.0, np.array([22.0, 27.0, 36.0])


def weighted_densities(pi, mu=MU_3, s2=S2_3, x=X_3, half=True):
    """π_k N(x_i | μ_k, σ²), one row per measure (half=False: the square of the gap divided by σ² only)."""
    gaps = (x[:, None] - mu[None, :]) ** 2 / (2 * s2 if half else s2)
    return pi[None, :] * np.exp(-gaps) / math.sqrt(2 * math.pi * s2)


def responsibilities(pi, half=True):
    w = weighted_densities(pi, half=half)
    return w / w.sum(axis=1, keepdims=True)


R_3 = responsibilities(PI_3)
LOGIT_3 = np.log(PI_3[0] / PI_3[1]) + ((X_3 - MU_3[1]) ** 2 - (X_3 - MU_3[0]) ** 2) / (2 * S2_3)
assert np.allclose(R_3[:, 0], 1 / (1 + np.exp(-LOGIT_3)))          # a sigmoid of the log-odds
N_3 = R_3.sum(axis=0)
PI_NEW_3 = float(N_3[0] / len(X_3))
MU_NEW_3 = (R_3 * X_3[:, None]).sum(axis=0) / N_3
HARD_3 = R_3.argmax(axis=1)                                        # the component of largest responsibility
LOG_P_3 = np.log(weighted_densities(PI_3).sum(axis=1)).sum()
ELBO_HARD_3 = np.log(weighted_densities(PI_3)[np.arange(len(X_3)), HARD_3]).sum()   # H(q) = 0 for a sure q
GAP_3 = float(LOG_P_3 - ELBO_HARD_3)
assert math.isclose(GAP_3, -np.log(R_3[np.arange(len(X_3)), HARD_3]).sum())   # a sum of KL(sure ‖ posterior) = −ln r
R_EQUAL_3 = responsibilities(np.array([0.5, 0.5]))
R_NO_HALF_3 = responsibilities(PI_3, half=False)
MU_BY_N_3 = (R_3 * X_3[:, None]).sum(axis=0) / len(X_3)
GAP_ALL1_3 = float(-np.log(R_3[:, 0]).sum())                       # every measure put in component 1
ENTROPY_3 = float(-(R_3 * np.log(R_3)).sum())
HARD_SHARE_3 = float(np.mean(HARD_3 == 0))                         # the share of the measures put in component 1

# CP6.4: vine plots, young (0), producing (1), old (2); the mass missing from a row is the end
P_4 = fmat([["0.6", "0.33", 0], [0, "0.7", "0.2"], [0, 0, "0.4"]])
R_4 = [fr(0), fr(22), fr(6)]
START_4 = [fr(1), fr(0), fr(0)]
MU1_4 = fvecmat(START_4, P_4)
MU2_4 = fvecmat(MU1_4, P_4)
MU3_4 = fvecmat(MU2_4, P_4)
P2_4 = fmatmul(P_4, P_4)
FULL_4 = np.zeros((4, 4))                                          # the end as an absorbing fourth state
FULL_4[:3, :3] = floats(P_4)
FULL_4[:3, 3] = 1 - FULL_4[:3, :3].sum(axis=1)
FULL_4[3, 3] = 1
OUT2_4 = 1 - sum(MU2_4)
assert np.allclose(np.linalg.matrix_power(FULL_4, 2)[0], floats(MU2_4 + [OUT2_4]))
I_MINUS_4 = [[int(i == j) - P_4[i][j] for j in range(3)] for i in range(3)]
V_4 = fsolve(I_MINUS_4, R_4)
assert all(P_4[i][j] == 0 for i in range(3) for j in range(i))     # triangular: solved from V(2) up
assert np.allclose(sum(np.linalg.matrix_power(np.array(floats(P_4)), k) @ floats(R_4) for k in range(500)), floats(V_4))
YEAR2_4 = sum(m * r for m, r in zip(MU2_4, R_4))
COLUMN_4 = [row[0] for row in P2_4]                               # P² μ0ᵀ: the law put on the right of P
SQUARES_4 = [p ** 2 for p in P_4[0]]
OUT_FIRST_4, OUT_SECOND_4 = 1 - sum(MU1_4), sum(MU1_4) - sum(MU2_4)
V_NO_LOOP_4 = [fr(0)] * 3
for s in (2, 1, 0):                                                # the diagonal coefficient of each row forgotten
    V_NO_LOOP_4[s] = R_4[s] + sum(P_4[s][j] * V_NO_LOOP_4[j] for j in range(3) if j != s)
V_T_4 = fsolve(ftranspose(I_MINUS_4), R_4)
V_FUTURE_4 = [v - r for v, r in zip(V_4, R_4)]
YEARS_4 = {sum(m * r for m, r in zip(MU1_4, R_4)), sum(m * r for m, r in zip(MU3_4, R_4))}   # years 1 and 3
RENORM_4 = YEAR2_4 / sum(MU2_4)

# CP6.5 (1): the poacher (rows: north, south) and the warden (columns: north, south)
G_5 = [[-4, 6], [3, -2]]
MAXIMIN_5 = max(min(row) for row in G_5)
MINIMAX_5 = min(max(col) for col in zip(*G_5))
assert MAXIMIN_5 < MINIMAX_5                                       # no saddle point: mixed strategies
(A_5, B_5), (C_5, D_5) = G_5
KAPPA_5 = A_5 - B_5 - C_5 + D_5
P_5, Q_5, VALUE_5 = Fraction(D_5 - C_5, KAPPA_5), Fraction(D_5 - B_5, KAPPA_5), Fraction(A_5 * D_5 - B_5 * C_5, KAPPA_5)
assert P_5 * A_5 + (1 - P_5) * C_5 == P_5 * B_5 + (1 - P_5) * D_5 == VALUE_5   # the warden is indifferent
assert Q_5 * A_5 + (1 - Q_5) * B_5 == Q_5 * C_5 + (1 - Q_5) * D_5 == VALUE_5   # the poacher is indifferent
GRID_5 = [Fraction(k, 600) for k in range(601)]                    # brute force on a grid of mixed strategies
assert max(GRID_5, key=lambda p: min(p * A_5 + (1 - p) * C_5, p * B_5 + (1 - p) * D_5)) == P_5
assert min(GRID_5, key=lambda q: max(q * A_5 + (1 - q) * B_5, q * C_5 + (1 - q) * D_5)) == Q_5
COLUMN_MIN_5 = max(min(col) for col in zip(*G_5))                  # the warden's worst read as a minimum

# CP6.5 (2): the heights (cm) of five plants of each nursery
XA_5, XB_5 = [26, 19, 34, 21, 32], [29, 37, 14, 22, 18]
GAPS_5 = [abs(a - b) for a, b in zip(sorted(XA_5), sorted(XB_5))]
W1_5 = Fraction(sum(GAPS_5), len(GAPS_5))
W2_5 = math.sqrt(sum(g * g for g in GAPS_5) / len(GAPS_5))
PAIRINGS_5 = list(permutations(XB_5))                              # every pairing: the sorted one is optimal
assert W1_5 == min(Fraction(sum(abs(a - b) for a, b in zip(XA_5, p)), 5) for p in PAIRINGS_5)
assert math.isclose(W2_5, min(math.sqrt(sum((a - b) ** 2 for a, b in zip(XA_5, p)) / 5) for p in PAIRINGS_5))
UNSORTED_W1_5 = Fraction(sum(abs(a - b) for a, b in zip(XA_5, XB_5)), 5)
MEANS_5 = abs(Fraction(sum(XA_5), 5) - Fraction(sum(XB_5), 5))
UNSORTED_W2_5 = math.sqrt(sum((a - b) ** 2 for a, b in zip(XA_5, XB_5)) / 5)

# CP6.6: three buoys, the squares of their distances (hm²)
AB2_6, AC2_6, BC2_6 = 16, 121, 49
D2_6 = fmat([[0, AB2_6, AC2_6], [AB2_6, 0, BC2_6], [AC2_6, BC2_6, 0]])
N_6 = len(D2_6)
J_6 = [[int(i == j) - Fraction(1, N_6) for j in range(N_6)] for i in range(N_6)]
S_6 = Fraction(sum(map(sum, D2_6)), N_6 ** 2)
JDJ_6 = fmatmul(fmatmul(J_6, D2_6), J_6)
G_6 = [[-x / 2 for x in row] for row in JDJ_6]
ROWS_6 = [sum(row) / N_6 for row in D2_6]
assert G_6 == [[-(D2_6[i][j] - ROWS_6[i] - ROWS_6[j] + S_6) / 2 for j in range(N_6)] for i in range(N_6)]
assert all(sum(row) == 0 for row in G_6)                           # G 1 = 0
assert all(G_6[i][j] * G_6[k][l] == G_6[i][l] * G_6[k][j]          # every 2 x 2 minor is zero: G has rank 1
           for i, k in combinations(range(N_6), 2) for j, l in combinations(range(N_6), 2))
TRACE_6 = trace(G_6)                                               # rank 1: the only non-zero eigenvalue
LAMBDAS_6 = [TRACE_6] + [Fraction(0)] * (N_6 - 1)
assert np.allclose(sorted(np.linalg.eigvalsh(np.array(floats(G_6))), reverse=True), floats(LAMBDAS_6), atol=1e-9)
W_6, Q_6 = np.linalg.eigh(np.array(floats(G_6)))
COLUMNS_6 = []
for k in np.argsort(-W_6):
    if W_6[k] > 1e-9:                                              # one column per non-zero eigenvalue
        unit = Q_6[:, k] * np.sign(Q_6[np.flatnonzero(np.round(Q_6[:, k], 12))[0], k])   # first non-zero coordinate > 0
        COLUMNS_6.append(math.sqrt(W_6[k]) * unit)
MAP_6 = np.column_stack(COLUMNS_6)
V_6 = [x / fsqrt(G_6[0][0]) for x in (row[0] for row in G_6)]      # G = v vᵀ, v read on the first column
assert fmatmul([[x] for x in V_6], [V_6]) == G_6 and np.allclose(MAP_6[:, 0], floats(V_6))
assert np.allclose(((MAP_6[:, None, :] - MAP_6[None, :, :]) ** 2).sum(axis=-1), floats(D2_6))   # the distances back
OFF_DIAGONAL_6 = Fraction(sum(map(sum, D2_6)), N_6 * (N_6 - 1))
ONCE_6 = Fraction(AB2_6 + AC2_6 + BC2_6, N_6 ** 2)
SIGN_S_6 = [[-(D2_6[i][j] - ROWS_6[i] - ROWS_6[j] - S_6) / 2 for j in range(N_6)] for i in range(N_6)]
J_FLOAT_6 = np.array(floats(J_6))
DIST_6 = -0.5 * J_FLOAT_6 @ np.sqrt(np.array(floats(D2_6))) @ J_FLOAT_6   # the distances, not their squares
NONZERO_6 = [x for x in LAMBDAS_6 if x != 0]                       # the zero eigenvalues left out
DIAGONAL_6 = [G_6[i][i] for i in range(N_6)]                       # the diagonal read as eigenvalues
LAMBDA_Q_6 = MAP_6 * np.sqrt(W_6[W_6 > 1e-9][::-1])[None, :]      # λ q in place of √λ q
UNIT_6 = MAP_6 / np.sqrt(W_6[W_6 > 1e-9][::-1])[None, :]           # q alone

# CP6.7: two solar farms, daily production of two rows of panels (MWh)
MUA_7, SA_7 = np.array([18.0, 12.0]), np.array([[12.0, 2.0], [2.0, 9.0]])
MUB_7, SB_7 = np.array([21.0, 13.0]), 4 * SA_7
NA_7, NB_7, NE_7 = 20, 40, 25
LAM_AB_7 = sorted(np.linalg.eigvals(SA_7 @ SB_7).real, reverse=True)
EIG_A_7 = sorted(np.linalg.eigvalsh(SA_7), reverse=True)
assert np.allclose(LAM_AB_7, [4 * x ** 2 for x in EIG_A_7])       # Σ_B = 4 Σ_A
ROOTS_7 = [math.sqrt(x) for x in LAM_AB_7]
COV_7 = float(np.trace(SA_7) + np.trace(SB_7) - 2 * sum(ROOTS_7))


def sqrtm_sym(s):
    w, q = np.linalg.eigh(s)
    return q @ np.diag(np.sqrt(w)) @ q.T


ROOT_A_7 = sqrtm_sym(SA_7)
assert math.isclose(np.trace(SA_7 + SB_7 - 2 * sqrtm_sym(ROOT_A_7 @ SB_7 @ ROOT_A_7)), COV_7)
MEANS_7 = float(((MUA_7 - MUB_7) ** 2).sum())
W2_7 = math.sqrt(MEANS_7 + COV_7)
TRA_7, TRB_7 = float(np.trace(SA_7)), float(np.trace(SB_7))


def bias(n_a, n_b):
    """E‖x̄A − x̄B‖² for n_a days of A and n_b days of B: the mean of n days is N(μ, Σ/n)."""
    return MEANS_7 + TRA_7 / n_a + TRB_7 / n_b


BIAS_7, SAME_7 = bias(NA_7, NB_7), bias(NE_7, NE_7)
RNG_7 = np.random.default_rng(6803)
for n_a, n_b in ((NA_7, NB_7), (NE_7, NE_7)):                      # Monte Carlo: the means of n days
    bars_a = RNG_7.multivariate_normal(MUA_7, SA_7 / n_a, size=20_000)
    bars_b = RNG_7.multivariate_normal(MUB_7, SB_7 / n_b, size=20_000)
    assert abs(((bars_a - bars_b) ** 2).sum(axis=1).mean() - bias(n_a, n_b)) < 0.15


def pooled(n_a, n_b):
    """The sum of the traces divided by the total number of days, in place of tr ΣA / nA + tr ΣB / nB."""
    return MEANS_7 + (TRA_7 + TRB_7) / (n_a + n_b)


COV_ONCE_7 = float(TRA_7 + TRB_7 - sum(ROOTS_7))
COV_NO_ROOT_7 = float(TRA_7 + TRB_7 - 2 * sum(LAM_AB_7))
TRACES_7 = TRA_7 + TRB_7
NO_N_7 = MEANS_7 + TRA_7 + TRB_7
SWAP_N_7 = MEANS_7 + TRA_7 / NB_7 + TRB_7 / NA_7
NO_MEANS_7 = TRA_7 / NA_7 + TRB_7 / NB_7
GAP_NORM_7 = math.sqrt(math.sqrt(MEANS_7) + COV_7)                 # the distance of the means, not its square
SAME_A_7 = 2 * TRA_7 / NE_7                                        # two samples of farm A
ONE_TERM_7 = {MEANS_7 + TRA_7 / NE_7, MEANS_7 + TRB_7 / NE_7}      # one estimated mean only
NO_MEANS_E_7 = (TRA_7 + TRB_7) / NE_7

# CP6.9 a): the letters of the five wrong lines
LINES_9, WRONG_9 = "ABCDEFGH", "ACEGH"
RIGHT_9 = "".join(sorted(set(LINES_9) - set(WRONG_9)))
FOUR_9 = {"".join(c) for c in combinations(LINES_9, 4)}           # the messages depend on the number of letters only
SIX_9 = {"".join(c) for c in combinations(LINES_9, 6)}
FIVE_9 = {"".join(c) for c in combinations(LINES_9, 5)} - {WRONG_9}
assert (len(FOUR_9), len(SIX_9), len(FIVE_9), RIGHT_9) == (70, 28, 55, "BDF")

# CP6.10: a charging station with two waiting places, 0, 1 or 2 cars waiting, every five minutes
P_10 = fmat([["0.32", "0.60", "0.08"], ["0.21", "0.33", "0.46"], ["0.05", "0.60", "0.35"]])
M_10, U0_10 = fr("0.68"), 0
assert all(sum(row) == 1 for row in P_10)
GREEDY_10 = [max(range(3), key=lambda j: (row[j], -j)) for row in P_10]   # ties: the smallest state
COLUMN_10 = [max(range(3), key=lambda i: (P_10[i][j], -i)) for j in range(3)]
SEQ_10 = [U0_10]
while SEQ_10[-1] not in SEQ_10[:-1]:
    SEQ_10.append(GREEDY_10[SEQ_10[-1]])
PRE_10 = SEQ_10.index(SEQ_10[-1])
PERIOD_10 = len(SEQ_10) - 1 - PRE_10
LONG_10 = [U0_10]
for _ in range(30):
    LONG_10.append(GREEDY_10[LONG_10[-1]])
assert all(LONG_10[t] == LONG_10[t + PERIOD_10] for t in range(PRE_10, 25))
assert all(LONG_10[t] not in LONG_10[PRE_10:PRE_10 + PERIOD_10] for t in range(PRE_10))


def top_p(row, m=M_10):
    """The states kept, by decreasing probability (ties: the smallest state first), until their mass reaches m."""
    kept = []
    for j in sorted(range(len(row)), key=lambda j: (-row[j], j)):
        kept.append(j)
        if sum(row[k] for k in kept) >= m:
            return kept


KEPT_10 = [top_p(row) for row in P_10]
for row, kept in zip(P_10, KEPT_10):                               # the smallest set whose mass reaches m
    assert len(kept) == min(len(c) for k in range(1, 4) for c in combinations(range(3), k)
                            if sum(row[j] for j in c) >= M_10)
P_TRUNC_10 = [[row[j] / sum(row[k] for k in kept) if j in kept else fr(0) for j in range(3)]
              for row, kept in zip(P_10, KEPT_10)]
ROW1_10, KEPT1_10, PS1_10 = P_10[1], KEPT_10[1], P_TRUNC_10[1]
MASS1_10 = sum(ROW1_10[j] for j in KEPT1_10)
KL1_10 = sum(float(q) * math.log(q / p) for q, p in zip(PS1_10, ROW1_10) if q > 0)
assert math.isclose(KL1_10, -math.log(MASS1_10))                   # the cost of a truncation: −ln P(S)


def stationary(p):
    """π P = π and Σ π = 1, exactly: two equations of (Pᵀ − I) π = 0 and the sum."""
    rows = [[p[j][i] - int(i == j) for j in range(3)] for i in range(3)][:2] + [[fr(1)] * 3]
    pi = fsolve(rows, [fr(0), fr(0), fr(1)])
    assert fvecmat(pi, p) == pi
    return pi


PI_NEW_10 = stationary(P_TRUNC_10)
assert np.allclose(np.ones(3) / 3 @ np.linalg.matrix_power(np.array(floats(P_TRUNC_10)), 400), floats(PI_NEW_10))
PI_OLD_10 = stationary(P_10)
ORDER1_10 = sorted(range(3), key=lambda j: (-ROW1_10[j], j))
LONGER_10 = ORDER1_10[:len(KEPT1_10) + 1]                          # one state more than needed
SHORTER_10 = ORDER1_10[:len(KEPT1_10) - 1]                         # one state less: the mass is under m
assert sum(ROW1_10[j] for j in SHORTER_10) < M_10
KEPT_ONLY_10 = [[row[j] if j in kept else fr(0) for j in range(3)] for row, kept in zip(P_10, KEPT_10)]
SPREAD_10 = [ROW1_10[j] + (1 - MASS1_10) / len(KEPT1_10) if j in KEPT1_10 else fr(0) for j in range(3)]
ONE_HOT_10 = [[int(j == GREEDY_10[i]) for j in range(3)] for i in range(3)]
UNNORMALISED_10 = [x / PI_NEW_10[1] for x in PI_NEW_10]           # π′ scaled so that π′1 = 1, not to sum 1
SWAPPED_10 = [PI_NEW_10[0], PI_NEW_10[2], PI_NEW_10[1]]'''




def exact(message: str, value: str, right: str) -> str:
    """The source of a wrong LIST where the statement asks for exact values: the value and its roundings (as_typed),
    one message spread over several keys (same_message)."""
    return f"**same_message({message!r}, as_typed({value}, {right}))"


def number(message: str, value: str, right: str) -> str:
    """The source of a wrong NUMBER where the statement asks for an exact value: the value and its roundings, a set
    under one message."""
    return f"{message!r}: as_typed({value}, {right})"


def plain(message: str, value: str) -> str:
    """The source of a wrong value recorded as it is (the statement asks for a number of decimals, or an integer)."""
    return f"{message!r}: {value}"


def wrong(*entries: str) -> str:
    return "mistakes={" + ", ".join(entries) + "}"


EXACT_LIST = "decimals=6, "
POOLED_7 = ("chaque moyenne estimée a sa propre variance : tr Σ_A / n_A + tr Σ_B / n_B, et non la somme des "
            "traces divisée par le nombre total de jours")
PAPER = [
    Paper("CP6.1", "Un vecteur gaussien de dimension 2 : loi marginale, loi conditionnelle, et la loi de μ + Lε", [
        ("a", f"a 2 × 2 matrix, as a list of rows {EXACT}", "L_1.tolist()", EXACT_LIST + wrong(
            exact("L est triangulaire inférieure : ses coefficients au-dessus de la diagonale sont nuls", "L_1.T",
                  "L_1"),
            exact("le coefficient l₂₂ est la racine de Σ₂₂ − l₂₁², pas de Σ₂₂", "L_ROOT_1", "L_1"),
            exact("le coefficient l₂₁ vaut Σ₂₁ / l₁₁ : divise par l₁₁, pas par Σ₁₁", "L_SIGMA_1", "L_1"))),
        ("b", f"[mean, variance], a list of 2 numbers {EXACT}", "floats(MARG_1)", EXACT_LIST + wrong(
            exact("une loi marginale ne tient compte d'aucune valeur lue", "MARG_COND_1", "MARG_1"),
            exact("le second paramètre de N(μ, σ²) est une variance, pas un écart-type", "MARG_SD_1", "MARG_1"))),
        ("c", f"[mean, variance], a list of 2 numbers {EXACT}", "floats(C21_1)", EXACT_LIST + wrong(
            exact("lire x₁ réduit l'incertitude sur x₂ : la variance conditionnelle est le complément de Schur, plus "
                  "petit que Σ₂₂", "[C21_1[0], S_1[1][1]]", "C21_1"),
            exact("dans la loi de x₂ sachant x₁, on divise par la variance de la coordonnée lue", "C21_OTHER_1",
                  "C21_1"),
            exact("l'écart lu se mesure à la moyenne de la coordonnée lue", "C21_MEAN_1", "C21_1"))),
        ("d", "[mean, variance], a list of 2 numbers (4 decimals)", "floats(C12_1)", "decimals=4, " + wrong(
            plain("lire x₂ réduit l'incertitude sur x₁ : la variance conditionnelle est le complément de Schur, plus "
                  "petit que Σ₁₁", "floats([C12_1[0], S_1[0][0]])"),
            plain("dans la loi de x₁ sachant x₂, on divise par la variance de la coordonnée lue",
                  "floats(C12_OTHER_1)"),
            plain("vérifie le signe de l'écart lu, x₂ − μ₂", "floats(C12_SIGN_1)"),
            plain("dans la variance conditionnelle de x₁, on divise par la variance de la coordonnée lue, Σ₂₂",
                  "floats([C12_1[0], C12_OTHER_1[1]])"))),
        ("e", f"a list of 2 numbers {EXACT}", "DRAW_1", EXACT_LIST + wrong(
            exact("le tirage est μ + Lε, avec L, pas Lᵀ", "DRAW_T_1", "DRAW_1"),
            exact("le tirage multiplie ε par le facteur de Cholesky, pas par Σ", "DRAW_S_1", "DRAW_1"),
            exact("le tirage part de la moyenne", "DRAW_0_1", "DRAW_1"))),
        ("f", f"a 2 × 2 matrix, as a list of rows {EXACT}", "floats(COV_M_1)", EXACT_LIST + wrong(
            exact("la covariance de Mε est M Mᵀ, pas Mᵀ M", "fmatmul(ftranspose(M_1), M_1)", "COV_M_1"),
            exact("la covariance d'une image linéaire Mε est M I Mᵀ : il faut une transposée", "fmatmul(M_1, M_1)",
                  "COV_M_1"))),
    ]),
    Paper("CP6.2", "La divergence KL entre deux gaussiennes de dimension 2, et une interpolation sphérique", [
        ("a", f"a number {ONE_EXACT}", "float(TR_2)", EXACT_LIST + wrong(
            number("la trace de la formule est celle de Σ₁⁻¹Σ₀ : l'inverse de la covariance de la seconde loi",
                   "TR_SWAP_2", "TR_2"),
            number("l'inverse d'une matrice 2 × 2 est sa comatrice transposée, divisée par son déterminant",
                   "TR_COF_2", "TR_2"),
            number("la trace d'un produit n'est pas le produit des traces", "TR_PROD_2", "TR_2"))),
        ("b", f"a number {ONE_EXACT}", "float(Q_2)", EXACT_LIST + wrong(
            number("le terme des moyennes est une distance de Mahalanobis : il utilise l'inverse d'une covariance",
                   "Q_DIRECT_2", "Q_2"),
            number("le terme des moyennes se mesure à l'échelle de la seconde loi, p₁", "Q_OTHER_2", "Q_2"),
            number("la distance de Mahalanobis tient compte des covariances", "Q_PLAIN_2", "Q_2"),
            number("Σ₁ a des coefficients hors diagonale : inverse la matrice entière", "Q_DIAG_2", "Q_2"))),
        ("c", "a number (4 decimals)", "KL_2", "decimals=4, " + wrong(
            plain("le logarithme compare les déterminants dans l'ordre det Σ₁ / det Σ₀", "KL_LOG_2"),
            plain("la formule retranche la dimension d", "KL_NO_D_2"),
            plain("la formule a un facteur ½ devant le crochet", "KL_NO_HALF_2"),
            plain("la KL demandée est KL(p₀ ‖ p₁) : l'espérance se prend sous la première loi", "KL_REVERSE_2"))),
        ("d", "an angle in degrees (2 decimals)", "DEGREES_2", "decimals=2, " + wrong(
            plain("la réponse est attendue en degrés, pas en radians", "OMEGA_2"),
            plain("l'angle Ω a pour cosinus uᵀv / (‖u‖ ‖v‖)", "ASIN_2"))),
        ("e", "a list of 3 numbers (4 decimals)", "SLERP_2.tolist()", "decimals=4, " + wrong(
            plain("le coefficient de u est sin((1 − t)Ω)/sin Ω, celui de v est sin(tΩ)/sin Ω", "SWAPPED_2.tolist()"),
            plain("le slerp suit l'arc de grand cercle, pas la ligne droite", "LINE_2.tolist()"),
            plain("ramener sur la sphère le point de la ligne droite ne donne pas l'angle tΩ",
                  "PROJECTED_2.tolist()"))),
        ("f", "a number (3 decimals)", "LINE_NORM_2", "decimals=3, " + wrong(
            plain("la norme est la racine de la somme des carrés", "LINE_NORM_2 ** 2"),
            plain("le point de la ligne droite n'est pas sur la sphère : calcule sa norme", "NORM_2"),
            plain("la question porte sur le point t = 1/4 de la ligne droite, pas sur son milieu", "MIDDLE_2"))),
    ]),
    Paper("CP6.3", "Un mélange de deux gaussiennes de variances connues et trois mesures : responsabilités, un pas "
                   "d'EM sur le poids et les moyennes, et l'écart à l'ELBO d'une affectation dure", [
        ("a", "a list of 3 numbers (4 decimals)", "R_3[:, 0].tolist()", "decimals=4, " + wrong(
            plain("les responsabilités tiennent compte des poids πₖ", "R_EQUAL_3[:, 0].tolist()"),
            plain("la responsabilité demandée est celle de la composante 1, de moyenne 24 h", "R_3[:, 1].tolist()"),
            plain("dans la densité gaussienne, le carré de l'écart est divisé par 2σ²", "R_NO_HALF_3[:, 0].tolist()"))),
        ("b", "a number (4 decimals)", "PI_NEW_3", "decimals=4, " + wrong(
            plain("un poids est une proportion : les deux poids ont pour somme 1", "float(N_3[0])"),
            plain("le pas M remplace l'ancien poids : recalcule-le à partir des responsabilités", "float(PI_3[0])"),
            plain("π₁ est la moyenne des responsabilités, pas la part des graines affectées à la composante 1",
                  "HARD_SHARE_3"))),
        ("c", "[mu1, mu2], a list of 2 numbers (3 decimals)", "MU_NEW_3.tolist()", "decimals=3, " + wrong(
            plain("une moyenne pondérée se divise par la somme de ses poids", "MU_BY_N_3.tolist()"),
            plain("les moyennes se donnent dans l'ordre des composantes (24 h et 32 h au départ)",
                  "MU_NEW_3[::-1].tolist()"))),
        ("d", "a number (4 decimals)", "GAP_3", "decimals=4, " + wrong(
            plain("l'affectation dure met chaque mesure dans la composante de plus grande responsabilité",
                  "GAP_ALL1_3"),
            plain("un écart à une borne inférieure est positif ou nul", "-GAP_3"),
            plain("l'écart à l'ELBO est une divergence KL, pas une entropie", "ENTROPY_3"))),
    ]),
    Paper("CP6.4", "Une chaîne de Markov à trois états : loi à deux pas, et la valeur d'une politique fixée par le "
                   "système de Bellman, quand une ligne finit", [
        ("a", f"a list of 3 numbers {EXACT}", "floats(MU2_4)", EXACT_LIST + wrong(
            exact("en convention ligne, une loi avance par μP : elle est à gauche de P", "COLUMN_4", "MU2_4"),
            exact("un coefficient de P² se lit sur les chemins de longueur 2 : ce n'est pas le carré d'un coefficient "
                  "de P", "SQUARES_4", "MU2_4"),
            exact("la question demande la loi dans deux ans, après deux pas", "MU1_4", "MU2_4"))),
        ("b", f"a number {ONE_EXACT}", "float(OUT2_4)", EXACT_LIST + wrong(
            number("la parcelle peut sortir du domaine la première année ou la deuxième : compte les deux",
                   "OUT_FIRST_4", "OUT2_4") + " | as_typed(OUT_SECOND_4, OUT2_4)",
            number("la question demande la probabilité d'être sortie du domaine, pas d'y être encore", "sum(MU2_4)",
                   "OUT2_4"),
            number("la deuxième année, la parcelle n'est plus forcément jeune : la probabilité de sortir cette "
                   "année-là se calcule avec la loi μ₁, pas avec la seule ligne 0", "2 * OUT_FIRST_4", "OUT2_4"))),
        ("c", f"[V(0), V(1), V(2)], a list of 3 numbers {EXACT}", "floats(V_4)", EXACT_LIST + wrong(
            exact("une parcelle peut rester dans le même état : la ligne de P garde son coefficient diagonal",
                  "V_NO_LOOP_4", "V_4"),
            exact("en convention ligne, V = r + PV : la ligne s de P donne les états suivants de s", "V_T_4", "V_4"),
            exact("la valeur compte aussi la récolte de l'année en cours", "V_FUTURE_4", "V_4"),
            plain("la fin n'est pas un état de P : la liste donne V(0), V(1) et V(2)", "floats(V_4 + [0])"))),
        ("d", f"a number {ONE_EXACT}", "float(YEAR2_4)", EXACT_LIST + wrong(
            "'l\\'année 0 est l\\'année en cours : la troisième récolte est celle de l\\'année 2': "
            "set().union(*(as_typed(y, YEAR2_4) for y in YEARS_4))",
            number("une parcelle sortie du domaine ne récolte plus rien : ne renormalise pas la loi", "RENORM_4",
                   "YEAR2_4"))),
    ]),
    Paper("CP6.5", "Un jeu à somme nulle 2 × 2 en stratégies mixtes, et W₁ entre deux petits échantillons de même "
                   "taille", [
        ("a", "[maximin, minimax], a list of 2 integers", "[MAXIMIN_5, MINIMAX_5]", wrong(
            plain("le joueur des colonnes paie : son pire, dans chaque colonne, est le plus grand gain du braconnier",
                  "[MAXIMIN_5, COLUMN_MIN_5]"),
            plain("le maximin (ce que s'assure le braconnier) vient en premier, et il est au plus le minimax",
                  "[MINIMAX_5, MAXIMIN_5]"))),
        ("b", FRACTION, "str(P_5)", 'kind="fraction", simplified=True, ' + wrong(
            plain("la stratégie optimale du braconnier rend le garde indifférent : écris l'égalité des deux colonnes",
                  "str(Q_5)"),
            plain("la probabilité p est celle de la première ligne, le nord", "str(1 - P_5)"))),
        ("c", FRACTION, "str(Q_5)", 'kind="fraction", simplified=True, ' + wrong(
            plain("la stratégie optimale du garde rend le braconnier indifférent : écris l'égalité des deux lignes",
                  "str(P_5)"),
            plain("la probabilité q est celle de la première colonne, le nord", "str(1 - Q_5)"))),
        ("d", FRACTION, "str(VALUE_5)", 'kind="fraction", simplified=True, ' + wrong(
            "**same_message('sans point selle, la valeur en stratégies mixtes est strictement entre le maximin et le "
            "minimax', [MAXIMIN_5, MINIMAX_5])",
            plain("vérifie le signe de κ = a − b − c + d", "str(-VALUE_5)"))),
        ("e", f"a number {ONE_EXACT}", "float(W1_5)", EXACT_LIST + wrong(
            number("trie les deux échantillons avant d'apparier", "UNSORTED_W1_5", "W1_5"),
            number("l'écart des moyennes n'est qu'une minoration de W₁", "MEANS_5", "W1_5"),
            number("la distance W₁ est la moyenne des écarts appariés, pas leur somme", "sum(GAPS_5)", "W1_5"))),
        ("f", "a number (4 decimals)", "W2_5", "decimals=4, " + wrong(
            plain("la distance W₂ est la racine de la moyenne des carrés des écarts", "W2_5 ** 2"),
            plain("trie les deux échantillons avant d'apparier", "UNSORTED_W2_5"))),
    ]),
    Paper("CP6.6", "Des distances aux positions : double centrage, matrice de Gram, et une configuration à une isométrie "
                   "près", [
        ("a", FRACTION, "str(S_6)", 'kind="fraction", simplified=True, ' + wrong(
            plain("la moyenne porte sur les neuf coefficients de D⁽²⁾, les zéros de la diagonale compris",
                  "str(OFF_DIAGONAL_6)"),
            plain("chaque carré de distance apparaît deux fois dans D⁽²⁾", "str(ONCE_6)"))),
        ("b", f"a 3 × 3 matrix, as a list of rows {EXACT}", "floats(G_6)", EXACT_LIST + wrong(
            exact("la matrice de Gram est −½ J D⁽²⁾ J : n'oublie pas le facteur −½", "JDJ_6", "G_6"),
            exact("dans Gᵢⱼ = −½(D⁽²⁾ᵢⱼ − rᵢ − rⱼ + s), vérifie le signe de s", "SIGN_S_6", "G_6"),
            exact("le double centrage se fait sur les carrés des distances", "DIST_6", "G_6"))),
        ("c", f"a list of 3 numbers, from the largest to the smallest {EXACT}", "floats(LAMBDAS_6)", EXACT_LIST + wrong(
            exact("les valeurs propres se donnent de la plus grande à la plus petite", "LAMBDAS_6[::-1]", "LAMBDAS_6"),
            plain("G a trois valeurs propres : donne aussi les nulles", "floats(NONZERO_6)"),
            exact("les coefficients diagonaux ne sont les valeurs propres que d'une matrice diagonale", "DIAGONAL_6",
                  "LAMBDAS_6"))),
        ("d", f"{COLUMN}, as a list of rows {EXACT}", "MAP_6.tolist()", EXACT_LIST + wrong(
            exact("dans chaque colonne, la première coordonnée (celle de A) est positive", "-MAP_6", "MAP_6"),
            exact("la colonne k est √λₖ qₖ, avec qₖ unitaire", "LAMBDA_Q_6", "MAP_6"),
            exact("une colonne de la carte est le vecteur propre unitaire multiplié par la racine de sa valeur propre",
                  "UNIT_6", "MAP_6"))),
    ]),
    Paper("CP6.7", "La distance de Fréchet de deux gaussiennes du plan de covariances proportionnelles, et le biais de "
                   "la distance entre deux moyennes estimées", [
        ("a", f"a list of 2 numbers, from the largest to the smallest {EXACT}", "floats(LAM_AB_7)", EXACT_LIST + wrong(
            exact("la question porte sur Σ_A Σ_B, pas sur Σ_A seule", "EIG_A_7", "LAM_AB_7"),
            exact("la question demande les valeurs propres de Σ_A Σ_B, avant la racine", "ROOTS_7", "LAM_AB_7"))),
        ("b", f"a number {ONE_EXACT}", "COV_7", EXACT_LIST + wrong(
            number("le terme croisé est 2 Σᵢ √λᵢ", "COV_ONCE_7", "COV_7"),
            number("le terme croisé porte sur les racines des valeurs propres", "COV_NO_ROOT_7", "COV_7"),
            number("les traces des covariances ne suffisent pas : retranche le terme croisé", "TRACES_7", "COV_7"))),
        ("c", "a number (4 decimals)", "W2_7", "decimals=4, " + wrong(
            plain("la distance de Fréchet est W₂, la racine de la formule", "W2_7 ** 2"),
            plain("la distance de Fréchet tient compte des moyennes et des covariances", "math.sqrt(COV_7)"),
            plain("la part des moyennes est le carré de la distance entre elles", "GAP_NORM_7"))),
        ("d", f"a number {ONE_EXACT}", "BIAS_7", EXACT_LIST + wrong(
            number("une moyenne de n relevés a pour covariance Σ/n", "NO_N_7", "BIAS_7"),
            number("chaque trace se divise par la taille de son propre échantillon", "SWAP_N_7", "BIAS_7"),
            number("l'espérance contient aussi l'écart des vraies moyennes", "NO_MEANS_7", "BIAS_7"),
            number(POOLED_7, "pooled(NA_7, NB_7)", "BIAS_7"))),
        ("e", f"a number {ONE_EXACT}", "SAME_7", EXACT_LIST + wrong(
            number("les deux échantillons viennent de deux fermes différentes", "SAME_A_7", "SAME_7"),
            "'deux échantillons, deux moyennes estimées : deux termes tr Σ / n': "
            "set().union(*(as_typed(y, SAME_7) for y in ONE_TERM_7))",
            number("l'espérance contient aussi l'écart des vraies moyennes", "NO_MEANS_E_7", "SAME_7"),
            number(POOLED_7, "pooled(NE_7, NE_7)", "SAME_7"))),
    ]),
    Paper("CP6.9", "Corriger une copie : cinq erreurs, une par chapitre (les lettres seulement)", [
        ("a", LETTERS, "WRONG_9", wrong(
            plain("cinq lignes sont fausses : ta réponse en contient moins", "FOUR_9"),
            plain("exactement cinq lignes sont fausses", "SIX_9"),
            plain("au moins une des lignes que tu donnes est juste : relis-les une par une", "FIVE_9"),
            plain("ce sont les lignes justes : la question demande les fausses", "RIGHT_9"))),
    ]),
    Paper("CP6.10", "Problème de synthèse : une file d'attente à trois états suivie de façon gloutonne, puis "
                    "échantillonnée après la troncature top-p de ses transitions", [
        ("a", "[f(0), f(1), f(2)], a list of 3 integers", "GREEDY_10", wrong(
            plain("le glouton lit la ligne de l'état présent et y prend l'issue la plus probable", "COLUMN_10"))),
        ("b", "[preperiod, period], a list of 2 integers", "[PRE_10, PERIOD_10]", wrong(
            plain("la période est la longueur du cycle, sans la queue", "[PRE_10, PRE_10 + PERIOD_10]"),
            plain("la prépériode compte les états du début qui ne reviennent jamais", "[0, PERIOD_10]"))),
        ("c", "a list of integers, by decreasing probability", "KEPT1_10", wrong(
            "**same_message('le top-p prend les issues une à une jusqu\\'à ce que leur masse atteigne m', "
            "[LONGER_10, SHORTER_10])",
            plain("range les états gardés par probabilité décroissante", "sorted(KEPT1_10)"))),
        ("d", "a list of 3 numbers (4 decimals)", "floats(PS1_10)", "decimals=4, " + wrong(
            plain("une loi tronquée est encore une loi : sa somme vaut 1", "floats(KEPT_ONLY_10[1])"),
            plain("une loi conditionnelle garde les rapports entre les probabilités gardées", "floats(SPREAD_10)"))),
        ("e", "a number (4 decimals)", "KL1_10", "decimals=4, " + wrong(
            plain("dans le coût d'une troncature, P(S) est la masse gardée, pas la masse retirée",
                  "-math.log(1 - MASS1_10)"),
            plain("les divergences KL sont en nats : logarithme népérien", "-math.log2(MASS1_10)"),
            plain("la KL d'une troncature n'est pas la masse retirée", "float(1 - MASS1_10)"))),
        ("f", "a 3 × 3 matrix, as a list of rows (4 decimals)", "floats(P_TRUNC_10)", "decimals=4, " + wrong(
            plain("chaque ligne de P′ est une loi : sa somme vaut 1", "floats(KEPT_ONLY_10)"),
            plain("une ligne garde ses issues jusqu'à ce que leur masse atteigne m, pas seulement la plus probable",
                  "ONE_HOT_10"))),
        ("g", "a list of 3 numbers (4 decimals)", "floats(PI_NEW_10)", "decimals=4, " + wrong(
            plain("la loi demandée est celle de la chaîne tronquée", "floats(PI_OLD_10)"),
            plain("une loi stationnaire a pour somme 1", "floats(UNNORMALISED_10)"),
            plain("à l'équilibre, le flux de 1 vers 2 égale le flux de 2 vers 1 : vérifie lequel multiplie π′₁",
                  "floats(SWAPPED_10)"))),
    ]),
]

EXPECTED = [f"{p.id}{letter}" for p in PAPER for letter, *_ in p.subs]
# the answers typed as lists or matrices, and those handed to wbm as texts (fractions, letters)
LISTS = sorted(f"{p.id}{letter}" for p in PAPER for letter, hint, *_ in p.subs if "list" in hint or "matrix" in hint)
TEXTS = sorted(f"{p.id}{letter}" for p in PAPER for letter, hint, *_ in p.subs if hint in (FRACTION, LETTERS))
COLUMNS = sorted(f"{p.id}{letter}" for p in PAPER for letter, hint, *_ in p.subs if hint.startswith(COLUMN))

HELPERS = r'''EXAM_OVER = False   # set it to True once your exam is finished, then run the cells below

import math
import re
from fractions import Fraction

RESULTS = {}        # sub-ID -> result of wbm.check
_REMINDED = []      # the full reminder is printed once, then a short one
LISTS = {''' + ", ".join(map(repr, LISTS)) + r'''}   # the answers that are lists or matrices
TEXTS = {''' + ", ".join(map(repr, TEXTS)) + r'''}   # the answers read by wbm as texts (fractions, letters)
COLUMNS = {''' + ", ".join(map(repr, COLUMNS)) + r'''}   # the matrices of one column (a flat list is read so)


def exam_over():
    """True once the exam is finished; otherwise print a reminder (and the cell checks nothing)."""
    if not EXAM_OVER:
        print("⏸️ Rien n'est vérifié (EXAM_OVER vaut False)." if _REMINDED else
              "⏸️ Vérification après l'examen : passe EXAM_OVER à True dans cette cellule, puis exécute-la.")
        _REMINDED.append(True)
        return False
    if "wbm" not in globals():
        print("⚠️ Exécute d'abord la cellule de configuration, tout en haut du notebook.")
        return False
    return True


_NAMES = {"sqrt": math.sqrt, "pi": math.pi, "e": math.e, "exp": math.exp, "ln": math.log, "log": math.log,
          "cos": math.cos, "sin": math.sin, "acos": math.acos, "asin": math.asin, "atan": math.atan,
          "degrees": math.degrees, "abs": abs, "math": math, "Fraction": Fraction}
_LINE = re.compile(r"[-*•]?\s*\(?([a-z])\s*[).:]\s*(.*)")   # a lower-case letter: « A : … » is a line of CP6.9
_FRENCH_NUMBER = re.compile(r"[+-]?\d+,\d+")
_COMMAS = ("dans une liste, une virgule sépare deux éléments : « [4,1, 7,9] » se lit comme quatre nombres. Écris "
           "les décimaux avec un point, [4.1, 7.9], ou sépare les éléments par des points-virgules, (4,1 ; 7,9).")
_UNREADABLE = ("je ne lis pas « {} » comme une liste : écris-la entre crochets, avec des points décimaux et des "
               "virgules entre les éléments, comme [0.83, -2.6] (une matrice : la liste de ses lignes, "
               "[[2, -1], [4, 3]]), ou avec des points-virgules entre les éléments, comme (0,83 ; -2,6).")


class Unreadable(ValueError):
    """A value written so that it cannot be read; the message says how to write it."""


def _clean(text):
    """Typographic signs -> Python: − → -, × → *, √2 → sqrt(2), π → pi."""
    for old, new in {"−": "-", "–": "-", "×": "*", "·": "*", "÷": "/", "«": '"', "»": '"', " ": " "}.items():
        text = text.replace(old, new)
    text = re.sub(r"√\s*\(", "sqrt(", text)
    text = re.sub(r"√\s*(\d+(?:\.\d+)?)", r"sqrt(\1)", text)
    return re.sub(r"(\d)\s*π", r"\1*pi", text).replace("π", "pi").strip()


def _python(text):
    """The value of a number, a list or a calculation, as a calculator reads it (nothing else is allowed)."""
    return eval(text, {"__builtins__": {}}, dict(_NAMES))


def _split(text):
    """The parts of a text separated by semicolons outside brackets."""
    parts, depth, start = [], 0, 0
    for i, char in enumerate(text):
        depth += (char in "[(") - (char in "])")
        if char == ";" and depth == 0:
            parts.append(text[start:i])
            start = i + 1
    return parts + [text[start:]]


def _french_list(text):
    """(0,83 ; -2,6) or [0,83 ; -2,6]: elements separated by semicolons, written with decimal commas."""
    inner = text.strip()
    if inner[:1] in "[(" and inner[-1:] in "])":
        inner = inner[1:-1]
    items = []
    for item in (part.strip() for part in _split(inner)):
        if item[:1] in "[(" and ";" in item:
            items.append(_french_list(item))
        elif _FRENCH_NUMBER.fullmatch(item):
            items.append(float(item.replace(",", ".")))
        else:
            items.append(_python(item))
    return items


def _value_part(text):
    """The value of a line copied from the answer sheet: what follows the last « = » (« L = [[4, 0], [3, 2]] »),
    or the last « : » (« plus petit n : 440 »)."""
    if "=" in text:
        text = text.rsplit("=", 1)[1]
    if ":" in text:
        text = text.rsplit(":", 1)[1]
    return text.strip()


def _short(line):
    """A long line pasted from the answer sheet, cut for a warning."""
    return line if len(line) <= 70 else line[:67] + "…"


def _given(text):
    return _value_part(text) not in ("", "...", "…")


def read_value(sub_id, text):
    """The value written after a letter, as wbm.check takes it; ... for a sub-question not done."""
    text = _clean(_value_part(text))
    if text in ("", "...", "…"):
        return ...
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        text = text[1:-1].strip()                       # a text between quotes
        if sub_id in TEXTS or sub_id not in LISTS:
            return text
    if sub_id in TEXTS:
        return text                                     # a fraction, letters: wbm reads the text
    if sub_id not in LISTS:
        if _FRENCH_NUMBER.fullmatch(text):
            return text                                 # 0,83: wbm reads a decimal comma in a text
        text = re.sub(r"(\d),(\d)", r"\1.\2", text)     # -ln(0,79): a decimal comma inside a calculation
        try:
            return _python(text)
        except Exception:
            return text                                 # wbm says what it expected
    value = _read_list(text)
    if isinstance(value, (set, frozenset)):
        raise Unreadable("des accolades font un ensemble, qui n'a pas d'ordre : écris une liste entre crochets, dans "
                         "l'ordre demandé par l'énoncé, comme [0.83, -2.6].")
    if sub_id in COLUMNS and isinstance(value, (list, tuple)) and not any(isinstance(x, (list, tuple)) for x in value):
        return [[x] for x in value]                     # a matrix of one column written as the list of its values
    return value


def _read_list(text):
    """A list or a matrix: Python's writing, or semicolons with decimal commas."""
    if ";" in text:
        try:
            return _french_list(text)
        except Exception:
            raise Unreadable(_UNREADABLE.format(text)) from None
    if re.search(r"\d,\d", text) and re.search(r",\s", text):
        raise Unreadable(_COMMAS)                       # [4,1, 7,9]: decimal commas inside a list
    try:
        return _python(text)
    except Exception:
        raise Unreadable(_UNREADABLE.format(text)) from None


def check_question(question, letters, answers):
    """Read the lines « a) value » of ``answers`` and check each value with wbm.check."""
    from wbm.checker import CheckResult

    values, last = {}, None
    for line in answers.split("\n"):              # not splitlines: a pasted \f or \v is no line break
        line = line.split("#")[0].strip()
        if not line:
            continue
        match = _LINE.fullmatch(line)
        if match and match.group(1) in letters:
            last, value = match.group(1), match.group(2)
            if _given(values.get(last, "")) and _given(value) and _value_part(value) != _value_part(values[last]):
                print(f"⚠️ {question} : deux lignes {last}) ; je garde la dernière.")
            if _given(value) or last not in values:
                values[last] = value
        elif last is not None and values[last].count("[") > values[last].count("]"):
            values[last] += " " + line                  # a matrix written on several lines
        elif match:
            print(f"⚠️ {question} : ligne ignorée, « {_short(line)} » : ce notebook ne vérifie pas de "
                  f"sous-question {match.group(1)}) ici.")
        else:
            print(f"⚠️ {question} : ligne ignorée, « {_short(line)} » (pas de « a) » en tête : une démarche est "
                  f"ignorée, c'est normal ; si c'est une réponse, écris-la comme « a) 0.83 »).")
    for letter in letters:
        sub_id = f"{question}{letter}"
        try:
            value = read_value(sub_id, values.get(letter, "..."))
        except Unreadable as exc:
            print(f"❌ Ex {sub_id} : {exc}")
            RESULTS[sub_id] = CheckResult(sub_id, False, "type", str(exc))
            continue
        RESULTS[sub_id] = wbm.check(sub_id, value)'''

SUMMARY = r'''# Summary of the automatic checks
import re

EXPECTED = ''' + repr(EXPECTED) + r'''


def natural(sub_id):
    """CP6.2a before CP6.10a: the question number as a number, then the letter."""
    number, letter = re.match(r"CP6\.(\d+)(.*)", sub_id).groups()
    return int(number), letter


if exam_over():
    done = {k: r for k, r in RESULTS.items() if r.status != "pending"}
    right = sorted((k for k, r in done.items() if r), key=natural)
    wrong = sorted((k for k, r in done.items() if not r), key=natural)
    pending = sorted((k for k, r in RESULTS.items() if r.status == "pending"), key=natural)
    missing = [k for k in EXPECTED if k not in RESULTS]
    print(f"Réponses vérifiées : {len(right)} juste(s) sur {len(done)} ; pas remplies : {len(pending)}.")
    if wrong:
        print("À revoir avec le corrigé :", ", ".join(wrong))
    if missing:
        print("⚠️ Pas vérifiées (cellule pas exécutée) :", ", ".join(missing))
    print("Note ensuite ta copie avec le barème de 03_examen_corrige.md : il donne aussi les points des démarches, "
          "des justifications et des questions rédigées, que cette vérification ne voit pas.")'''

INTRO = r'''## Après l'examen : vérification automatique

**Ne commence qu'une fois ta copie terminée**, examen rendu. Ce notebook vérifie les réponses que tu as écrites sur ta feuille, question par question : ✅ juste, ❌ faux (avec une piste), ⏳ pas rempli. Il ne note pas : les démarches, les justifications, le quiz CP6.Q1, la démonstration CP6.8 et les corrections de CP6.9 b) se corrigent avec `03_examen_corrige.md`, qui donne aussi le barème.

1. Passe `EXAM_OVER` à `True` dans la cellule ci-dessous, puis exécute-la.
2. Dans la cellule de chaque question, recopie après chaque lettre **la valeur** écrite sur ta copie, pas un nouveau calcul (sinon tu ne vérifies plus ta copie). Laisse `...` pour une sous-question que tu n'as pas faite. Tu peux aussi coller les lignes de ta copie `04_mes_reponses.md` (« - a) L = … ») : seul ce qui suit le dernier « = » ou le dernier « : » est lu. Efface d'abord ce qui suit ta réponse sur la même ligne (une démarche entre parenthèses, par exemple). Garde les triples guillemets `"""` du début et de la fin : ce que tu écris entre eux est lu comme un texte, et rien de ce que tu tapes là n'arrête la cellule ; « Tout exécuter » (*Run all*) va jusqu'au bilan.
3. Les formes d'écriture, comme sur ta copie : un nombre avec une virgule ou un point (`0,83` ou `0.83`), ou un calcul (`3/8`, `sqrt(7)`, `ln(7)`) ; une liste entre crochets avec des points décimaux, `[0.83, -2.6]`, ou, si tu gardes les virgules décimales, avec des points-virgules entre les éléments, `(0,83 ; -2,6)` (dans une liste, `[4,1, 7,9]` se lit comme quatre nombres) ; une matrice comme la liste de ses lignes, `[[2, -1], [4, 3]]` ; une fraction telle quelle, `3/8` ; des lettres telles quelles, `ABCDE`.
4. Les décimales : quand l'énoncé dit « valeur exacte », donne toutes les décimales de ta valeur (elle n'en a que quelques-unes) ; quand il dit « 4 décimales » (ou 3, ou 2), arrondis à ce nombre, à la fin du calcul seulement. Quand il dit « dans n'importe quel ordre », l'ordre ne compte pas ; ailleurs, l'ordre de ta liste compte.
5. Le bilan, à la fin, dit aussi quelles réponses n'ont pas été vérifiées.'''


def paper_cell(kind: str, paper: Paper) -> list:
    """One question: the block of answers and a guarded check (exam), or the wbm.record cell (solutions)."""
    cells = [md(f"**{paper.id} — {paper.title}**")]
    if kind == "exercise":
        name = f"answers_{paper.id.replace('.', '_')}"
        width = max(len(f"{letter}) ...") for letter, *_ in paper.subs) + 4
        lines = [f"# {paper.id}: after each letter, the value written on your answer sheet (... if not done)",
                 f'{name} = r"""']
        lines += [f"{letter}) ...".ljust(width) + f"# {hint}" for letter, hint, *_ in paper.subs]
        lines += ['"""', "", "if exam_over():", f'    check_question("{paper.id}", "{paper.letters}", {name})']
        cells.append(code("\n".join(lines)))
    else:
        lines = []
        for letter, _, expr, options in paper.subs:
            args = f", {options}" if options else ""
            lines.append(f'wbm.record("{paper.id}{letter}", {expr}{args})')
        source = "\n".join(lines)
        check_unique_keys(source, paper.id)
        cells.append(code(source, tags=["answer"]))
    return cells


def header_cells(kind: str) -> list:
    rel = EXAM if kind == "exercise" else SOLUTIONS
    if kind == "exercise":
        title = "# CP6 · Examen blanc de la partie VI — vérification de ta copie"
        how = (f"L'examen se fait **sur papier** (`01_examen_sujet.md`, {MINUTES} minutes, fiches fermées). Ce notebook "
               "ne sert qu'**après** : il vérifie les réponses chiffrées de ta copie. Ses cellules ne vérifient rien "
               "tant que `EXAM_OVER` vaut `False`, et « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli (⏸️).\n\n"
               "> Travaille dans **ta copie** (`mon_travail/checkpoints/partie_6/02_examen_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py CP6`) : ce fichier-ci est mis à jour par Claude. Sur Colab, le badge "
               "ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme l'explique "
               "`00_setup/COLAB.md` §2.")
    else:
        title = "# CP6 · Examen blanc de la partie VI — solutions (notebook exécuté)"
        how = ("L'enregistrement des réponses que vérifie le notebook de l'examen (cellules marquées `answer`, "
               "récoltées par `tools/build_answers.py`), calculées à partir des nombres du sujet, avec NumPy et des "
               "fractions exactes, et recoupées par des vérifications (`assert`) ; les erreurs classiques reçoivent "
               "un message qui dit où chercher. Le corrigé détaillé et le barème sont dans `03_examen_corrige.md`.")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell("demo"))
    if kind == "exercise":
        cells.append(md(INTRO))
        cells.append(code(HELPERS))
        for paper in PAPER:
            cells += paper_cell(kind, paper)
        cells.append(md("## Bilan"))
        cells.append(code(SUMMARY))
        cells.append(md("**Ce que cette vérification ne voit pas** : les démarches et les justifications ; le quiz "
                        "CP6.Q1 ; la démonstration CP6.8 ; les corrections de CP6.9 b) (seules les lettres de a) sont "
                        "vérifiées). Tout cela se corrige avec `03_examen_corrige.md`. Remplis ensuite le tableau de "
                        "ta note, à la fin de ta copie, puis fais la remédiation du corrigé."))
    else:
        cells.append(md("## Les réponses vérifiées après l'examen"))
        cells.append(code(PAPER_CONTEXT))
        for paper in PAPER:
            cells += paper_cell(kind, paper)
    return cells


def main() -> int:
    write_notebook(EXAM, build("exercise"))
    write_notebook(SOLUTIONS, build("solution"))
    print(f"✅ {EXAM} and {SOLUTIONS} written ({len(PAPER)} questions, {len(EXPECTED)} checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
