#!/usr/bin/env python
"""Build the two notebooks of the mock exam CP3 from a single source (used by Claude).

    python tools/chapters/build_cp3.py
    python tools/run_all_notebooks.py checkpoints/partie_3/03_examen_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py checkpoints/partie_3/02_examen_notebook.ipynb

Same mechanism as build_cp2.py: the exam of CP3 is on paper only (01_examen_sujet.md), and the exam notebook is the
check done AFTER the exam; nothing is checked while EXAM_OVER is False, so that « Run all » goes to the end.
Wrong-answer messages state a rule or ask a question, never the calculation that gives the answer nor its last step.
The solutions notebook records the answers, computed from the numbers of the statements (cells tagged `answer`, read
by build_answers.py). The final summary lists the sub-IDs that were not checked (a cell that did not run, or that
stopped on an error such as a decimal comma). Not in the notebook: the true/false quiz CP3.Q1, the proof CP3.8 and the
corrections of CP3.9 b) (only its letters are checked).

The data are new: none comes from the exercises, fiches, quizzes or flashcards of M12a to M14, from CP0 to CP2, from
chapters 12 to 15 of workbookIA, its checkpoint III or its mini-project III (no penguins, no California, no fraud, no
Adult, no AdaBoost nor gradient boosting, no kNN nor Gini on six points; not the sequel of 12.7 (a given vector then
checked, reconstruction, whitening), nor the variance of a mean of correlated models; no 2D eigendirection already
used; the matrices S, B, A of CP3.3 and CP3.4, the 3 x 5 matrix of CP3.1 and the axes of CP3.10 are absent from both
repositories). No seed: no random draw.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import Paper, check_unique_keys, md  # noqa: E402
from nbbuild import badge, code, setup_cell, write_notebook  # noqa: E402

FOLDER = "checkpoints/partie_3"
EXAM = f"{FOLDER}/02_examen_notebook.ipynb"
SOLUTIONS = f"{FOLDER}/03_examen_solutions.ipynb"


def _letter_sets():
    """CP3.9 a: wrong sets of letters, by kind, with messages that name no line (the corrigé explains each line)."""
    from itertools import combinations

    wrong, right = "ACDFH", "BEG"
    missing = {"".join(c) for c in combinations(wrong, 4)}
    extra = {"".join(sorted(wrong + r)) for r in right}
    swapped = {"".join(sorted(set(wrong) - {w} | {r})) for w in wrong for r in right}

    def literal(values):
        return "{" + ", ".join(repr(v) for v in sorted(values)) + "}"

    return (f'{{"il manque une des lignes fausses : il y en a exactement cinq": {literal(missing)}, '
            f'"une des lignes citées est juste : relis-les une par une, avec la règle qu\'elle utilise": '
            f'{literal(extra)}, "une ligne juste est citée à la place d\'une ligne fausse": {literal(swapped)}, '
            f'"ce sont les trois lignes justes ; la question demande les cinq lignes fausses": {right!r}}}')


LETTERS = _letter_sets()

PAPER_CONTEXT = r'''# The answers are computed from the numbers of the statements (01_examen_sujet.md)
import math
from fractions import Fraction
from math import comb


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def transpose(a):
    return [list(col) for col in zip(*a)]


def matmul(a, b):
    """The product of two matrices given as lists of rows."""
    return [[dot(row, col) for col in zip(*b)] for row in a]


def whole(x):
    """x (a number, or a list of them) as int(s), after checking that it is a whole number: 6.000000000000001 -> 6."""
    if isinstance(x, (list, tuple)):
        return [whole(y) for y in x]
    assert abs(x - round(x)) < 1e-9, x
    return round(x)


def rank(m):
    """The rank of m (a list of rows), by Gaussian elimination on exact fractions."""
    rows, r = [[Fraction(x) for x in row] for row in m], 0
    for j in range(len(rows[0])):
        pivot = next((i for i in range(r, len(rows)) if rows[i][j] != 0), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for i in range(r + 1, len(rows)):
            factor = rows[i][j] / rows[r][j]
            rows[i] = [a - factor * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r


# CP3.1: the 3 x 5 matrix A (columns c1, ..., c5), then V and W in R_2[X], a polynomial a + bX + cX² written (a, b, c)
A_1 = [[1, 0, 2, 3, -1], [0, 1, -3, 2, 4], [2, -1, 7, 4, -6]]
C_1 = transpose(A_1)
RANK_1 = rank(A_1)
COEF_1 = [A_1[0][2], A_1[1][2]]                # c3 = alpha c1 + beta c2, read on rows 1 and 2 (they begin with I)
COORD_1 = [C_1[4][0], C_1[4][1]]               # c5 = a c1 + b c2, read on rows 1 and 2 for the same reason
EQ_1 = [2, -1, -1]                             # z with A^T z = 0 and z1 = 2: z1 + 2 z3 = 0, z2 - z3 = 0
assert [COEF_1[0] * x + COEF_1[1] * y for x, y in zip(C_1[0], C_1[1])] == C_1[2]
assert [COORD_1[0] * x + COORD_1[1] * y for x, y in zip(C_1[0], C_1[1])] == C_1[4]
assert all(dot(EQ_1, c) == 0 for c in C_1)
SOLVABLE_1 = rank([row + [b] for row, b in zip(A_1, (3, 1, 4))]) == RANK_1


def at_1(t):
    """P(t) = a + b t + c t², as a row acting on (a, b, c)."""
    return [1, t, t * t]


COND_V_1 = [p - q for p, q in zip(at_1(2), at_1(-1))]    # P(2) - P(-1) = 0
DIM_V_1, DIM_W_1 = 3 - rank([COND_V_1]), 3 - rank([COND_V_1, at_1(0)])
P_1 = (7, -2, 2)
assert dot(COND_V_1, P_1) == 0                          # P is in V
H_1 = [P_1[0], P_1[2]]                                  # P = 7 * 1 + 2 * (X² - X)
assert [H_1[0], -H_1[1], H_1[1]] == list(P_1)

# CP3.2: Gram-Schmidt on (v1, v2), then the least squares by R x = Q^T y
V1_2, V2_2, Y_2 = (1, 1, 3, 5), (6, 0, 10, 0), (11, -6, 17, -4)
R11_2 = math.sqrt(dot(V1_2, V1_2))
Q1_2 = [x / R11_2 for x in V1_2]
R12_2 = dot(Q1_2, V2_2)
W_2 = [x - R12_2 * q for x, q in zip(V2_2, Q1_2)]       # v2 - r12 q1
R22_2 = math.sqrt(dot(W_2, W_2))
Q2_2 = [x / R22_2 for x in W_2]
QY_2 = [dot(Q1_2, Y_2), dot(Q2_2, Y_2)]
XH2_2 = QY_2[1] / R22_2                                 # back substitution: the last row first
XH_2 = [(QY_2[0] - R12_2 * XH2_2) / R11_2, XH2_2]
YH_2 = [QY_2[0] * a + QY_2[1] * b for a, b in zip(Q1_2, Q2_2)]     # Q Q^T y
assert all(abs(p - (XH_2[0] * a + XH_2[1] * b)) < 1e-9 for p, a, b in zip(YH_2, V1_2, V2_2))
RES_2 = [y - p for y, p in zip(Y_2, YH_2)]

# CP3.3: the eigenvalues of S from its trace and determinant; the Cholesky factor of B
S_3 = [[11, 15], [15, 27]]
TR_3, DET_3 = S_3[0][0] + S_3[1][1], S_3[0][0] * S_3[1][1] - S_3[0][1] * S_3[1][0]
EIG_3 = [TR_3 / 2 - math.sqrt(TR_3 ** 2 / 4 - DET_3), TR_3 / 2 + math.sqrt(TR_3 ** 2 / 4 - DET_3)]


def unit_eigenvector(m, lam):
    """The unit eigenvector of the symmetric 2 x 2 matrix m for lam, of positive first coordinate (first row of
    (m - lam I) v = 0)."""
    v = [m[0][1], lam - m[0][0]]
    n = math.hypot(*v)
    return [x / n for x in v] if v[0] > 0 else [-x / n for x in v]


B_3, X_3 = [[9, 3, -6], [3, 5, 0], [-6, 0, 9]], (1, -1, 1)


def cholesky(a):
    """The lower triangular L, of positive diagonal, such that a = L L^T."""
    n = len(a)
    low = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = a[i][j] - sum(low[i][k] * low[j][k] for k in range(j))
            low[i][j] = math.sqrt(s) if i == j else s / low[j][j]
    return low


L_3 = cholesky(B_3)
assert whole(matmul(L_3, transpose(L_3))) == B_3
LTX_3 = [dot(col, X_3) for col in transpose(L_3)]      # L^T x
LX_3 = [dot(row, X_3) for row in L_3]                   # L x
BOUND_3 = whole(math.sqrt(2 * 8))                       # [[2, a], [a, 8]]: 2 > 0 and 2 * 8 - a² > 0
INTERVAL_3 = f"]{-BOUND_3} ; {BOUND_3}["

# CP3.4: A = s1 u1 v1^T + s2 u2 v2^T, from the eigenvalues of A^T A
A_4 = [[9, 6], [2, -6]]
ATA_4, AAT_4 = matmul(transpose(A_4), A_4), matmul(A_4, transpose(A_4))
TR_4, DET_4 = ATA_4[0][0] + ATA_4[1][1], ATA_4[0][0] * ATA_4[1][1] - ATA_4[0][1] * ATA_4[1][0]
LAM_4 = [TR_4 / 2 + math.sqrt(TR_4 ** 2 / 4 - DET_4), TR_4 / 2 - math.sqrt(TR_4 ** 2 / 4 - DET_4)]
S_4 = [math.sqrt(lam) for lam in LAM_4]                 # s1 >= s2
V1_4, V2_4 = unit_eigenvector(ATA_4, LAM_4[0]), unit_eigenvector(ATA_4, LAM_4[1])
AV1_4 = [dot(row, V1_4) for row in A_4]
U1_4 = [x / S_4[0] for x in AV1_4]
U2_4 = [dot(row, V2_4) / S_4[1] for row in A_4]
A1_4 = [[S_4[0] * u * v for v in V1_4] for u in U1_4]
B_4 = [99, -22]                                         # = 11 sqrt(85) u1, so A^-1 b = sqrt(85) v1
SOL_4 = [math.sqrt(85) * v for v in V1_4]
assert all(abs(dot(row, SOL_4) - b) < 1e-9 for row, b in zip(A_4, B_4))
D_4 = [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A_4, A1_4)]    # A - A1
ERR_4 = math.sqrt(sum(x * x for row in D_4 for x in row))
FRO2_4 = sum(x * x for row in A_4 for x in row)
TRA_4, DETA_4 = A_4[0][0] + A_4[1][1], A_4[0][0] * A_4[1][1] - A_4[0][1] * A_4[1][0]
EIGA_4 = sorted((abs(TRA_4 / 2 + s * math.sqrt(TRA_4 ** 2 / 4 - DETA_4)) for s in (1, -1)), reverse=True)   # |λ| of A

# CP3.5: four small situations
T_5 = [3.2, 0.7, 6.1, 4.4, 2.9, 5.3]
N0_5, N1_5, N2_5 = 4, 10, 16
N_5 = N0_5 + N1_5 + N2_5
THETA_5 = Fraction(N0_5 + N1_5, 3 * N_5)                # (n0 + n1)/θ = 3 n2/(1 - 3θ)


def entropy(counts, log=math.log2):
    """The entropy of the frequencies of the counts (in bits by default)."""
    n = sum(counts)
    return -sum(c / n * log(c / n) for c in counts if c)


LAW_5 = (40, 25, 20, 15)                                # p = (0.4, 0.25, 0.2, 0.15), as counts out of 100
P_5 = [c / sum(LAW_5) for c in LAW_5]
KL_UNIFORM_5 = sum(p * math.log2(p / 0.25) for p in P_5)          # KL(p ‖ u) = log2(4) - H(p)
assert abs(KL_UNIFORM_5 - (2 - entropy(LAW_5))) < 1e-12
KL_REVERSED_5 = sum(0.25 * math.log2(0.25 / p) for p in P_5)      # KL(u ‖ p)
GINI_SQUARES_5 = sum(p ** 2 for p in P_5)
Z_5, LABEL_5 = [1.3, -1.2, -0.5, 2.2, 0.9], [1, 0, 1, 1, 0]
LOSSES_5 = [math.log(1 + math.exp(z)) - y * z for z, y in zip(Z_5, LABEL_5)]
LOGLOSS_5 = sum(LOSSES_5) / len(LOSSES_5)
CONSTANT_5 = (sum(LABEL_5), len(LABEL_5) - sum(LABEL_5))    # the best constant q is the frequency of the 1s

# CP3.6 (1): f = x + 2y on x²/8 + y²/2 = 1; ∇f + λ∇g = 0 gives x = -8/(2λ), y = -2 * 2/(2λ), then λ² from the constraint
C_6, AX_6, AY_6 = (1, 2), 8, 2
LAMS_6 = [s * math.sqrt(C_6[0] ** 2 * AX_6 + C_6[1] ** 2 * AY_6) / 2 for s in (1, -1)]
CANDIDATES_6 = [(-C_6[0] * AX_6 / (2 * lam), -C_6[1] * AY_6 / (2 * lam), lam) for lam in LAMS_6]
assert all(abs(x * x / AX_6 + y * y / AY_6 - 1) < 1e-12 for x, y, _ in CANDIDATES_6)
X_6, Y_6, LAM_6 = max(CANDIDATES_6, key=lambda c: dot(C_6, c[:2]))
XMIN_6, YMIN_6, _ = min(CANDIDATES_6, key=lambda c: dot(C_6, c[:2]))

# CP3.6 (2): the soft-margin SVM on three examples
W_6, B_6, CSVM_6 = (2, 1), -3, 1
DATA_6 = [((1, 3), 1), ((2, 0), -1), ((1, 0.5), 1)]


def hinge_6(data):
    return sum(max(0, 1 - y * (dot(W_6, x) + B_6)) for x, y in data)


HINGE_6 = hinge_6(DATA_6)
J_6 = dot(W_6, W_6) / 2 + CSVM_6 * HINGE_6
ACTIVE_6 = [(x, y) for x, y in DATA_6 if y * (dot(W_6, x) + B_6) < 1]   # the examples of margin below 1


def subgradient_6(examples, reg=1, sign=-1):
    """[g_w1, g_w2, g_b]: reg * w (the gradient of ½‖w‖²) + sign * C * y * (x1, x2, 1), summed over the examples."""
    g = [reg * W_6[0], reg * W_6[1], 0]
    for x, y in examples:
        for k, v in enumerate((*x, 1)):
            g[k] += sign * CSVM_6 * y * v
    return g


# CP3.6 (3): the Gram matrix of k(x, z) = (x + z)² on 1, 2, 3
PTS_6, VEC_6 = (1, 2, 3), (3, -2, 0)
K_6 = [[(x + z) ** 2 for z in PTS_6] for x in PTS_6]
VKV_6 = sum(VEC_6[i] * VEC_6[j] * K_6[i][j] for i in range(3) for j in range(3))
VKV_ONCE_6 = sum(VEC_6[i] * VEC_6[j] * K_6[i][j] for i in range(3) for j in range(i, 3))   # crossed terms once

# CP3.7: X of law B(18, 0.06), the Chernoff exponent and the Hoeffding bound of P(X >= 5); a limit; Hedge
N_7, P_7, K_7 = 18, 0.06, 5
A_7 = K_7 / N_7


def pmf_7(k):
    return comb(N_7, k) * P_7 ** k * (1 - P_7) ** (N_7 - k)


def kl(a, p):
    """KL(a ‖ p) between two Bernoulli laws, in nats."""
    return a * math.log(a / p) + (1 - a) * math.log((1 - a) / (1 - p))


TAIL_7 = sum(pmf_7(k) for k in range(K_7, N_7 + 1))
X_7, M_7 = -2.4, 45
D_7, LIMIT_7 = (1 + X_7 / M_7) ** M_7, math.exp(X_7)
GAP_7 = M_7 * math.log(1 + X_7 / M_7) - X_7                       # n ln(1 + x/n) - x
ETA_7, L_7 = 0.7, [3, 1, 2, 2]


def weights_7(exponents):
    """The weights proportional to exp(exponents), normalised to sum 1."""
    e = [math.exp(s) for s in exponents]
    return [x / sum(e) for x in e]


# CP3.10: six examples, three axes (the rows of U, divided by 21), the regression on the scores
X_10 = [[17, 13, 6], [17, 1, 12], [21, 6, 19], [7, 3, 24], [7, 15, 18], [3, 10, 11]]
Y_10 = [18, 18, 27, 20, 24, 13]
U_10 = [[19, -4, -8], [4, -13, 16], [8, 16, 11]]
assert all(dot(u, v) == (441 if i == j else 0) for i, u in enumerate(U_10) for j, v in enumerate(U_10))
N_10 = len(X_10)
MEAN_10 = [sum(col) / N_10 for col in zip(*X_10)]
YBAR_10 = sum(Y_10) / N_10


def scores_10(x, center=True):
    """[t1, t2, t3] of x: u_j · (x - mean), or u_j · x when center is False."""
    d = [a - m for a, m in zip(x, MEAN_10)] if center else x
    return [dot(u, d) / 21 for u in U_10]


T_10 = [scores_10(x) for x in X_10]
assert whole(T_10[1:]) == [[7, 3, -5], [7, 6, 4], [-7, 9, -1], [-7, -3, 5], [-7, -6, -4]]   # the table of the statement
SS_10 = [sum(t[j] ** 2 for t in T_10) for j in range(3)]                       # Σ t_j²
TY_10 = [sum(t[j] * (y - YBAR_10) for t, y in zip(T_10, Y_10)) for j in range(3)]
W_10 = [ty / ss for ty, ss in zip(TY_10, SS_10)]                                # the normal equations are diagonal
SCT_10 = sum((y - YBAR_10) ** 2 for y in Y_10)
R2_10 = [sum(W_10[j] * TY_10[j] for j in range(k)) / SCT_10 for k in (1, 2, 3)]   # with 1, 2 and 3 axes
NEW_10 = (26, 5, 13)


def predict_10(x, k, center=True):
    t = scores_10(x, center)
    return YBAR_10 + sum(W_10[j] * t[j] for j in range(k))'''

PAPER = [
    Paper("CP3.1", "Indépendance, base, rang et noyau", [
        ("a", "an integer", "RANK_1",
         'mistakes={"le rang compte les lignes (ou les colonnes) indépendantes : une ligne est-elle une combinaison '
         'des autres ?": 3, "le rang ne dépasse ni le nombre de lignes, ni celui des colonnes": 5}'),
        ("b", "an integer", "len(C_1) - RANK_1",
         'mistakes={"théorème du rang : le rang plus la dimension du noyau donne le nombre de colonnes": {0, 1}, '
         '"c\'est le rang ; le théorème du rang relie le rang et la dimension du noyau": RANK_1}'),
        ("c", "[alpha, beta]", "COEF_1",
         'mistakes={"vérifie la relation sur la première ligne de A": [-x for x in COEF_1], '
         '"l\'ordre suit celui de l\'énoncé : α multiplie c₁, β multiplie c₂": COEF_1[::-1]}'),
        ("d", "a list of 2 numbers", "COORD_1",
         'mistakes={"l\'ordre des coordonnées suit celui de la base (c₁, c₂)": COORD_1[::-1], '
         '"vérifie le signe sur la première ligne": [-x for x in COORD_1]}'),
        ("e", "[z1, z2, z3]", "EQ_1",
         'mistakes={"Aᵀz = 0 dit que z est orthogonal à chaque colonne : vérifie z · c₁ et z · c₂": [2, 1, -1], '
         '"l\'énoncé fixe z₁ = 2 : ta première coordonnée le respecte-t-elle ?": [-2, 1, 1], '
         '"la première coordonnée de z est fixée par l\'énoncé : relis-le": [1, -0.5, -0.5]}'),
        ("f", "True or False", "SOLVABLE_1",
         'mistakes={"un vecteur b n\'est atteint par A que s\'il est orthogonal à tout z de ker Aᵀ": True}'),
        ("g", "an integer", "DIM_W_1",
         'mistakes={"W ajoute une condition à celle qui définit V": DIM_V_1, '
         '"P(2) = P(−1) est une condition linéaire sur les coefficients, et ℝ₂[X] est de dimension 3": 3}'),
        ("h", "a list of 2 numbers", "H_1",
         'mistakes={"le coefficient de X dans X² − X est −1": [H_1[0], -H_1[1]], '
         '"l\'ordre des coordonnées suit celui de la base (1, X² − X)": H_1[::-1]}'),
    ]),
    Paper("CP3.2", "Gram-Schmidt, projection et moindres carrés", [
        ("a", "a number", "whole(R11_2)",
         'mistakes={"la norme est la racine carrée de la somme des carrés": dot(V1_2, V1_2)}'),
        ("b", "a number", "whole(R12_2)",
         'mistakes={"r₁₂ = q₁ · v₂, avec q₁ unitaire": dot(V1_2, V2_2), '
         '"r₁₂ est la coordonnée de v₂ sur q₁ : le produit scalaire q₁ · v₂": 1}'),
        ("c", "a list of 4 numbers", "whole(W_2)",
         'mistakes={"c\'est q₂ ; la question demande le vecteur avant normalisation": Q2_2, '
         '"on retire r₁₂ q₁, où q₁ est v₁ divisé par sa norme": whole([x - R12_2 * v for x, v in zip(V2_2, V1_2)])}'),
        ("d", "[[a, b], [c, d]]", "whole([[R11_2, R12_2], [0, R22_2]])",
         'mistakes={"R est triangulaire supérieure": whole([[R11_2, 0], [R12_2, R22_2]]), '
         '"r₂₂ est une norme, pas un carré de norme": whole([[R11_2, R12_2], [0, R22_2 ** 2]])}'),
        ("e", "a list of 2 numbers", "whole(QY_2)",
         'mistakes={"c\'est Xᵀy ; la question demande Qᵀy, avec les vecteurs orthonormés": '
         '[dot(V1_2, Y_2), dot(V2_2, Y_2)]}'),
        ("f", "a list of 4 numbers", "whole(YH_2)",
         'mistakes={"c\'est le résidu y − ŷ ; la question demande la projection": whole(RES_2)}'),
        ("g", "a list of 2 numbers", "whole(XH_2)",
         'mistakes={"l\'ordre des inconnues : x̂₁ multiplie la première colonne de R": whole(XH_2[::-1]), '
         '"R x̂ = Qᵀy se résout de bas en haut : la dernière ligne donne x̂₂, puis on remonte": '
         'whole([QY_2[0] / R11_2, QY_2[1] / R22_2])}'),
        ("h", "a number", "float(whole(dot(RES_2, RES_2)))",
         'decimals=2, mistakes={"la question demande le carré de la distance": math.sqrt(dot(RES_2, RES_2)), '
         '"c\'est ‖ŷ‖² ; la question porte sur le résidu y − ŷ": float(whole(dot(YH_2, YH_2)))}'),
    ]),
    Paper("CP3.3", "Valeurs propres, matrice définie positive et Cholesky", [
        ("a", "a list of 2 numbers", "whole(EIG_3)",
         'mistakes={"la question demande l\'ordre croissant": whole(EIG_3[::-1])}'),
        ("b", "a list (4 decimals)", "unit_eigenvector(S_3, EIG_3[1])",
         'decimals=4, mistakes={"c\'est un vecteur propre de la plus petite valeur propre": '
         'unit_eigenvector(S_3, EIG_3[0]), "le vecteur demandé est unitaire : divise-le par sa norme": [3, 5], '
         '"la question demande la première coordonnée positive": [-x for x in unit_eigenvector(S_3, EIG_3[1])]}'),
        ("c", "a number", "1 / EIG_3[0]",
         'decimals=4, mistakes={"S⁻¹ a pour valeurs propres les inverses de celles de S": EIG_3[1], '
         '"c\'est la plus petite valeur propre de S⁻¹": 1 / EIG_3[1]}'),
        ("d", "an integer", "rank([[S_3[0][0] - 2, S_3[0][1]], [S_3[1][0], S_3[1][1] - 2]])",
         'mistakes={"2 est valeur propre de S, donc S − 2I est singulière ; mais elle n\'est pas nulle": {0, 2}}'),
        ("e", "a list of 3 lists", "whole(L_3)",
         'mistakes={"L est triangulaire inférieure": whole(transpose(L_3))}'),
        ("f", "a number", "whole(math.prod(L_3[i][i] for i in range(3)) ** 2)",
         'mistakes={"det B = det L × det Lᵀ": whole(math.prod(L_3[i][i] for i in range(3)))}'),
        ("g", "a number", "dot(LTX_3, LTX_3)",
         'decimals=2, mistakes={"xᵀBx = xᵀLLᵀx = ‖Lᵀx‖² : c\'est Lᵀ, pas L, qui s\'applique à x": dot(LX_3, LX_3), '
         '"la question demande un carré de norme": math.sqrt(dot(LTX_3, LTX_3))}'),
        ("h", 'an interval, written like "]-1 ; 2["', "INTERVAL_3",
         'kind="interval", mistakes={"définie positive demande des inégalités strictes": "[-4 ; 4]", '
         '"une inégalité sur un carré se résout avec une racine : que donne a² < 16 pour a ?": "]-16 ; 16[", '
         '"a peut être négatif : seul a² compte": "]0 ; 4["}'),
    ]),
    Paper("CP3.4", "SVD, rang faible et variance expliquée", [
        ("a", "[[a, b], [c, d]]", "ATA_4",
         'mistakes={"c\'est AAᵀ ; la question demande AᵀA": AAT_4}'),
        ("b", "[s1, s2]", "whole(S_4)",
         'mistakes={"les valeurs singulières sont les racines carrées des valeurs propres de AᵀA": whole(LAM_4), '
         '"la convention range les valeurs singulières dans l\'ordre décroissant": whole(S_4[::-1]), '
         '"A n\'est pas symétrique : ses valeurs singulières ne sont pas ses valeurs propres ; passe par AᵀA": EIGA_4}'),
        ("c", "a list (3 decimals)", "V1_4",
         'decimals=3, mistakes={"c\'est v₂ : v₁ est associé à la plus grande valeur propre de AᵀA": V2_4, '
         '"v₁ doit être unitaire : divise-le par sa norme": [7, 6]}'),
        ("d", "a list (3 decimals)", "U1_4",
         'decimals=3, mistakes={"divise A v₁ par s₁": AV1_4, '
         '"c\'est u₂ ; la question demande u₁ = A v₁ / s₁": U2_4}'),
        ("e", "a list of 2 numbers", "whole(SOL_4)",
         'mistakes={"A n\'est pas orthogonale : son inverse n\'est pas Aᵀ, il divise par les valeurs singulières": '
         '[dot(col, B_4) for col in transpose(A_4)], "la solution s\'écrit avec v₁, pas avec u₁": '
         'whole([9, -2]), "A⁻¹ divise la composante sur u₁ par s₁": whole([11 * x for x in SOL_4])}'),
        ("f", "a number", "whole(ERR_4)",
         'mistakes={"c\'est le carré de l\'erreur": whole(ERR_4 ** 2), '
         '"l\'erreur vient de la valeur singulière retirée, pas de celle qui est gardée": whole(S_4[0])}'),
        ("g", "a number (3 decimals)", "S_4[0] ** 2 / FRO2_4",
         'decimals=3, mistakes={"la part d\'énergie se calcule avec les carrés des valeurs singulières": '
         'S_4[0] / sum(S_4), "c\'est la part perdue ; la question demande la part gardée": 1 - S_4[0] ** 2 / FRO2_4}'),
        ("h", "a number (3 decimals)", "S_4[0] / S_4[1]",
         'decimals=3, mistakes={"c\'est le conditionnement de AᵀA ; la question porte sur A": LAM_4[0] / LAM_4[1], '
         '"κ₂ divise la plus grande valeur singulière par la plus petite, pas l\'inverse": S_4[1] / S_4[0], '
         '"A n\'est pas symétrique : κ₂ se calcule avec les valeurs singulières, pas avec les valeurs propres": '
         'EIGA_4[0] / EIGA_4[1]}'),
    ]),
    Paper("CP3.5", "Maximum de vraisemblance, log-loss et entropie", [
        ("a", "a number", "max(T_5)",
         'decimals=1, mistakes={"la vraisemblance est nulle dès que θ est plus petit qu\'une observation": '
         'sum(T_5) / len(T_5), "c\'est l\'estimateur des moments ; la question demande le maximum de '
         'vraisemblance": 2 * sum(T_5) / len(T_5)}'),
        ("b", 'an irreducible fraction, as text (like "3/8")', "THETA_5",
         'kind="fraction", simplified=True, mistakes={"les observations 1 et 2 dépendent aussi de θ : la fréquence '
         'des 0 ne suffit pas": Fraction(N0_5, N_5), "la fréquence des 1 ne suffit pas non plus : les trois comptes '
         'dépendent de θ": Fraction(N1_5, 2 * N_5), "vérifie la dérivée de ln(1 − 3θ)": '
         'Fraction(N0_5 + N1_5, 3 * (N0_5 + N1_5) + N2_5), '
         '"c\'est l\'estimateur des moments ; la question demande le maximum de vraisemblance": '
         'Fraction(2 * N_5 - (N1_5 + 2 * N2_5), 4 * N_5)}'),
        ("c", "a number (3 decimals)", "entropy(LAW_5)",
         'decimals=3, mistakes={"en bits : le logarithme de base 2": {entropy(LAW_5, math.log), 1.319}}'),
        ("d", "a number (3 decimals)", "1 - GINI_SQUARES_5",
         'decimals=3, mistakes={"l\'indice de Gini est 1 − Σ p²": GINI_SQUARES_5}'),
        ("e", "a number (3 decimals)", "KL_UNIFORM_5",
         'decimals=3, mistakes={"la KL n\'est pas symétrique : la question demande KL(p ‖ u)": KL_REVERSED_5, '
         '"en bits : le logarithme de base 2": KL_UNIFORM_5 * math.log(2)}'),
        ("f", "a number (3 decimals)", "LOGLOSS_5",
         'decimals=3, mistakes={"la log-loss moyenne divise la somme par le nombre d\'exemples": sum(LOSSES_5), '
         '"en nats : le logarithme népérien": LOGLOSS_5 / math.log(2), '
         '"le terme d\'un exemple est s(z) − yz : as-tu retranché yz ?": '
         'sum(math.log(1 + math.exp(z)) for z in Z_5) / len(Z_5)}'),
        ("g", "a number (3 decimals)", "entropy(CONSTANT_5, math.log)",
         'decimals=3, mistakes={"la question demande des nats : le logarithme népérien": entropy(CONSTANT_5), '
         '"0,5 n\'est pas la meilleure probabilité constante pour ces labels": math.log(2)}'),
    ]),
    Paper("CP3.6", "Lagrange, hinge loss et noyau", [
        ("a", "[x, y]", "whole([X_6, Y_6])",
         'mistakes={"c\'est le point du minimum de f sur l\'ellipse": whole([XMIN_6, YMIN_6])}'),
        ("b", "a number", "whole(dot(C_6, (X_6, Y_6)))",
         'mistakes={"c\'est le minimum de f sur l\'ellipse": whole(dot(C_6, (XMIN_6, YMIN_6)))}'),
        ("c", "a number", "whole(LAM_6)",
         'mistakes={"avec la convention ∇f + λ∇g = 0, vérifie le signe": whole(-LAM_6), '
         '"vérifie ∇g : quelle est la dérivée de x²/8 ?": -4}'),
        ("d", "a number", "HINGE_6",
         'decimals=2, mistakes={"la marge d\'un exemple est y (w · x + b) : quel est le label de P₂ ?": '
         'hinge_6([(x, abs(y)) for x, y in DATA_6])}'),
        ("e", "a number", "J_6",
         'decimals=2, mistakes={"le terme de régularisation est la moitié de ‖w‖²": dot(W_6, W_6) + CSVM_6 * HINGE_6, '
         '"n\'oublie pas le terme ½‖w‖²": CSVM_6 * HINGE_6}'),
        ("f", "[g_w1, g_w2, g_b]", "subgradient_6(ACTIVE_6)",
         'decimals=2, mistakes={"n\'oublie pas le gradient de ½‖w‖², qui est w": subgradient_6(ACTIVE_6, reg=0), '
         '"seuls les exemples de marge strictement inférieure à 1 ont un terme non nul": subgradient_6(DATA_6), '
         '"le gradient du terme d\'un exemple actif est −y x, pas +y x": subgradient_6(ACTIVE_6, sign=1)}'),
        ("g", "a number", "VKV_6",
         'mistakes={"vᵀKv = Σᵢ Σⱼ vᵢ vⱼ Kᵢⱼ : les termes croisés comptent deux fois": VKV_ONCE_6, '
         '"vᵀKv = Σᵢ Σⱼ vᵢ vⱼ Kᵢⱼ : vérifie le signe de chaque produit vᵢ vⱼ": -VKV_6}'),
    ]),
    Paper("CP3.7", "Queue binomiale et borne de Chernoff, limite et poids exponentiels", [
        ("a", "a number (5 decimals)", "TAIL_7",
         'decimals=5, mistakes={"P(X ≥ 5) compte aussi le cas X = 5": TAIL_7 - pmf_7(5), '
         '"P(X ≥ 5) additionne P(X = k) pour tous les k ≥ 5, pas seulement k = 5": pmf_7(5)}'),
        ("b", "a number (3 decimals)", "N_7 * kl(A_7, P_7)",
         'decimals=3, mistakes={"la KL n\'est pas symétrique : KL(a ‖ p), avec a en premier": N_7 * kl(P_7, A_7), '
         '"la question demande l\'exposant n KL(a ‖ p), pas la borne": {math.exp(-N_7 * kl(A_7, P_7)), 0.015}, '
         '"la KL de la borne de Chernoff est en nats : logarithme népérien": N_7 * kl(A_7, P_7) / math.log(2)}'),
        ("c", "a number (2 decimals)", "math.exp(-2 * N_7 * (A_7 - P_7) ** 2)",
         'decimals=2, mistakes={"la borne de Hoeffding est e^(−2n(a − p)²), avec le facteur 2": '
         'math.exp(-N_7 * (A_7 - P_7) ** 2)}'),
        ("d", "a number (4 decimals)", "D_7",
         'decimals=4, mistakes={"c\'est la limite ; la question demande la valeur pour n = 45": LIMIT_7}'),
        ("e", "a number (4 decimals)", "GAP_7",
         'decimals=4, mistakes={"n ln(1 + x/n) est-il au-dessus ou au-dessous de x ? Pense à ln(1 + u) ≤ u": -GAP_7, '
         '"c\'est l\'erreur relative ; la question demande l\'écart des logarithmes": (D_7 - LIMIT_7) / LIMIT_7, '
         '"c\'est le premier terme du développement, −x²/(2n) ; la question demande l\'écart exact": '
         '-X_7 ** 2 / (2 * M_7)}'),
        ("f", "a list (4 decimals)", "weights_7([-ETA_7 * x for x in L_7])",
         'decimals=4, mistakes={"les poids décroissent quand L grandit : e^(−η L)": weights_7([ETA_7 * x for x in L_7]), '
         '"n\'oublie pas η dans l\'exponentielle": weights_7([-x for x in L_7]), '
         '"normalise : la somme des poids vaut 1": [math.exp(-ETA_7 * (x - min(L_7))) for x in L_7], '
         '"les poids demandés sont normalisés : leur somme vaut 1": [math.exp(-ETA_7 * x) for x in L_7]}'),
    ]),
    Paper("CP3.9", "Corriger une copie : cinq erreurs (les lettres seulement)", [
        ("a", 'the letters, as text (like "ABCDE")', '"ACDFH"', f"mistakes={LETTERS}"),
    ]),
    Paper("CP3.10", "Problème de synthèse : des données centrées, leurs axes principaux, un modèle sur les scores", [
        ("a", "a list of 3 numbers", "whole(MEAN_10)", ""),
        ("b", "[t11, t12, t13]", "whole(T_10[0])",
         'mistakes={"le score se calcule sur l\'exemple centré, x₁ − x̄": scores_10(X_10[0], center=False), '
         '"les axes sont les vecteurs donnés divisés par 21": whole([21 * t for t in T_10[0]])}'),
        ("c", "a list (1 decimal)", "[ss / (N_10 - 1) for ss in SS_10]",
         'decimals=1, mistakes={"l\'énoncé demande la variance avec n − 1": [ss / N_10 for ss in SS_10], '
         '"ce sont les variances des features ; la question porte sur les scores": '
         '[sum((x[j] - MEAN_10[j]) ** 2 for x in X_10) / (N_10 - 1) for j in range(3)]}'),
        ("d", "a number (3 decimals)", "(SS_10[0] + SS_10[1]) / sum(SS_10)",
         'decimals=3, mistakes={"deux axes, pas un seul": SS_10[0] / sum(SS_10), '
         '"c\'est la part perdue ; la question demande la part gardée": SS_10[2] / sum(SS_10)}'),
        ("e", "[w1, w2] (3 decimals)", "W_10[:2]",
         'decimals=3, mistakes={"les équations normales divisent t_j · y par Σ t_j², pas par la variance": '
         '[ty / (ss / (N_10 - 1)) for ty, ss in zip(TY_10[:2], SS_10[:2])]}'),
        ("f", "a number (3 decimals)", "R2_10[1]",
         'decimals=3, mistakes={"deux axes, pas un seul": R2_10[0], '
         '"c\'est le R² à trois axes ; la question demande celui à deux axes": R2_10[2], '
         '"la somme des carrés totale se calcule sur y − ȳ": R2_10[1] * SCT_10 / sum(y * y for y in Y_10)}'),
        ("g", "a number", "whole(W_10[2])",
         'mistakes={"les équations normales divisent t₃ · y par Σ t₃², pas par la variance": '
         'whole(TY_10[2] / (SS_10[2] / (N_10 - 1)))}'),
        ("h", "a number (3 decimals)", "R2_10[2]",
         'decimals=3, mistakes={"c\'est le R² à deux axes ; la question demande celui à trois axes": R2_10[1]}'),
        ("i", "[two axes, three axes]", "whole([predict_10(NEW_10, 2), predict_10(NEW_10, 3)])",
         'mistakes={"le nouvel exemple se centre avec la moyenne d\'entraînement avant de calculer ses scores": '
         '[predict_10(NEW_10, k, center=False) for k in (2, 3)], '
         '"l\'ordre : la prédiction à deux axes, puis celle à trois axes": '
         'whole([predict_10(NEW_10, 3), predict_10(NEW_10, 2)]), '
         '"le nouvel exemple se centre avec la moyenne d\'entraînement, pas avec ses propres valeurs": '
         'whole([YBAR_10, YBAR_10]), "le modèle prédit ȳ plus les termes en t : as-tu ajouté ȳ ?": '
         'whole([predict_10(NEW_10, k) - YBAR_10 for k in (2, 3)])}'),
    ]),
]

EXPECTED = [f"{p.id}{letter}" for p in PAPER for letter, *_ in p.subs]

HELPERS = r'''EXAM_OVER = False   # set it to True once your exam is finished, then run the cells below

RESULTS = {}        # sub-ID -> result of wbm.check
_REMINDED = []      # the full reminder is printed once, then a short one


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
    return True'''

SUMMARY = r'''# Summary of the automatic checks
import re

EXPECTED = ''' + repr(EXPECTED) + r'''


def natural(sub_id):
    """CP3.2a before CP3.10a: the question number as a number, then the letter."""
    number, letter = re.match(r"CP3\.(\d+)(.*)", sub_id).groups()
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
        print("⚠️ Pas vérifiées (cellule pas exécutée, ou arrêtée par une erreur, par exemple une virgule décimale) :",
              ", ".join(missing))
    print("Note ensuite ta copie avec le barème de 03_examen_corrige.md : il donne aussi les points des démarches, "
          "des justifications et des questions rédigées, que cette vérification ne voit pas.")'''

INTRO = r'''## Après l'examen : vérification automatique

**Ne commence qu'une fois ta copie terminée**, examen rendu. Ce notebook vérifie les réponses que tu as écrites sur ta feuille, question par question : ✅ juste, ❌ faux (avec une piste), ⏳ pas rempli. Il ne note pas : les démarches, les justifications, le quiz CP3.Q1, la démonstration CP3.8 et les corrections de CP3.9 b) se corrigent avec `03_examen_corrige.md`, qui donne aussi le barème.

1. Passe `EXAM_OVER` à `True` dans la cellule ci-dessous, puis exécute-la.
2. Reporte chaque réponse de ta feuille : **la valeur** que tu as écrite, pas un nouveau calcul (sinon tu ne vérifies plus ta copie). Laisse `...` pour une question que tu n'as pas faite.
3. Si une cellule s'arrête sur une erreur, « Tout exécuter » s'arrête avec elle : corrige-la, puis relance cette cellule et les suivantes, jusqu'au bilan.
4. Les formes d'écriture : en Python, le séparateur décimal est un **point** (`2.75`) : une virgule arrête toute la cellule (`0,027`), et aucune réponse de la question n'est vérifiée, ou donne un couple de nombres (`0,75`) ; une liste s'écrit entre crochets (`[-1.5, 4]`), une matrice comme une liste de lignes (`[[1, -2], [0.5, 3]]`) ; un texte entre guillemets (`"XYZ"`), comme une fraction (`"3/8"`) ou un intervalle (`"]-1 ; 2["`) ; vrai ou faux par `True` ou `False`.
5. Le bilan, à la fin, dit aussi quelles réponses n'ont pas été vérifiées.'''


def paper_cell(kind: str, paper: Paper) -> list:
    """One question: the answers and a guarded wbm.check (exam), or the wbm.record cell (solutions)."""
    cells = [md(f"**{paper.id} — {paper.title}**")]
    stem = f"answer_{paper.id.replace('.', '_')}"
    if kind == "exercise":
        lines = [f"# {paper.id}: the values written on your answer sheet"]
        lines += [f"{stem}{letter} = ...  # {letter}) {hint}" for letter, hint, *_ in paper.subs]
        names = ", ".join(f"{stem}{letter}" for letter, *_ in paper.subs)
        lines += ["", "if exam_over():",
                  f"    for letter, answer in zip(\"{paper.letters}\", [{names}]):",
                  f"        RESULTS[f\"{paper.id}{{letter}}\"] = wbm.check(f\"{paper.id}{{letter}}\", answer)"]
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
        title = "# CP3 · Examen blanc de la partie III — vérification de ta copie"
        how = ("L'examen se fait **sur papier** (`01_examen_sujet.md`, 110 minutes, fiches fermées). Ce notebook ne "
               "sert qu'**après** : il vérifie les réponses chiffrées de ta copie. Ses cellules ne vérifient rien tant "
               "que `EXAM_OVER` vaut `False`, et « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli (⏸️).\n\n"
               "> Travaille dans **ta copie** (`mon_travail/checkpoints/partie_3/02_examen_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py CP3`) : ce fichier-ci est mis à jour par Claude. Sur Colab, le badge "
               "ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme l'explique "
               "`00_setup/COLAB.md` §2.")
    else:
        title = "# CP3 · Examen blanc de la partie III — solutions (notebook exécuté)"
        how = ("L'enregistrement des réponses que vérifie le notebook de l'examen (cellules marquées `answer`, "
               "récoltées par `tools/build_answers.py`), calculées à partir des nombres du sujet ; les erreurs "
               "classiques reçoivent un message qui dit où chercher. Le corrigé détaillé et le barème sont dans "
               "`03_examen_corrige.md`.")
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
                        "CP3.Q1 ; la démonstration CP3.8 ; les corrections de CP3.9 b) (seules les lettres de a) sont "
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
