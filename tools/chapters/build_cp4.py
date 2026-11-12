#!/usr/bin/env python
"""Build the two notebooks of the mock exam CP4 from a single source (used by Claude).

    python tools/chapters/build_cp4.py
    python tools/run_all_notebooks.py checkpoints/partie_4/03_examen_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py checkpoints/partie_4/02_examen_notebook.ipynb

Same mechanism as build_cp3.py: the exam of CP4 is on paper only (01_examen_sujet.md), and the exam notebook is the
check done AFTER the exam; nothing is checked while EXAM_OVER is False, so that « Run all » goes to the end.
Wrong-answer messages state a rule or ask a question, never the calculation that gives the answer nor its last step.
The solutions notebook records the answers, computed from the numbers of the statements (cells tagged `answer`, read
by build_answers.py). The final summary lists the sub-IDs that were not checked (a cell that did not run, or that
stopped on an error such as a decimal comma). Not in the notebook: the true/false quiz CP4.Q1, the proof CP4.8 and the
corrections of CP4.9 b) (only its letters are checked).

The data are new: none comes from the exercises, fiches, quizzes or flashcards of M16 to M20, from CP0 to CP3, from
chapters 16 to 20 of workbookIA, its checkpoint IV or its mini-project IV (no network, no MLP nor count of the
parameters of a network, no named optimiser (momentum, Adam), no dropout, no batchnorm; no chain of sigmoids; the
exponential fit of CP4.10 is outside any network, on three measurements at x = -1, 0, 2). CP4.1: the paths go from
vertex 5 to vertex 1 (A strictly lower triangular), and the variance of a product is the volume V = DT pumped into a
tank (no rectangle); CP4.3: the graph v1 = x + y², v2 = x v1, v3 = ln v1, f = v2 v3 at (5, -2) (not (3, 1), the point
of M18.4); CP4.4 g: the gradient of (Xa) · (Xb); CP4.5: f = x³ − 27x + 3y² + yz + 3z², the natures answered by number
(1 to 4); CP4.7: T[1] = [[3, 0, 6], [8, 1, 9]] (with the former T[1], mixing up the axes (0, 2) gave the right answer
of b), and the apiaries y = (50, 26, 14, 22, 7), π = (1, 0.65, 0.35, 0.55, 0.1). The homogeneous matrices of CP4.1,
the jacobians of CP4.2, X of CP4.4, the hessian of CP4.5, A of CP4.6 and the hessian of CP4.10 are absent from both
repositories. No seed: no random draw.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import Paper, check_unique_keys, md  # noqa: E402
from nbbuild import badge, code, setup_cell, write_notebook  # noqa: E402

FOLDER = "checkpoints/partie_4"
EXAM = f"{FOLDER}/02_examen_notebook.ipynb"
SOLUTIONS = f"{FOLDER}/03_examen_solutions.ipynb"

SHAPE = 'a shape, as text (like "(4, 5)")'
MATRIX = "[[a, b], [c, d]]"
NATURE = "an integer: 1, 2, 3 or 4"


def _letter_sets():
    """CP4.9 a: wrong sets of letters, by kind, with messages that name no line (the corrigé explains each line)."""
    from itertools import combinations

    wrong, right = "ACDGH", "BEF"
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


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def transpose(a):
    return [list(col) for col in zip(*a)]


def matmul(a, b):
    """The product of two matrices given as lists of rows."""
    return [[dot(row, col) for col in zip(*b)] for row in a]


def add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def outer(u, v):
    """The matrix u vᵀ."""
    return [[x * y for y in v] for x in u]


def whole(x):
    """x (a number, or a list of them) as int(s), after checking that it is a whole number: 6.000000000000001 -> 6."""
    if isinstance(x, (list, tuple)):
        return [whole(y) for y in x]
    assert abs(x - round(x)) < 1e-9, x
    return round(x)


def floats(x):
    """x (a fraction, or a list of them) as float(s)."""
    if isinstance(x, (list, tuple)):
        return [floats(y) for y in x]
    return float(x)


def inverse(m):
    """The inverse of the square matrix m (a list of rows), by Gauss-Jordan elimination on exact fractions."""
    n = len(m)
    rows = [[Fraction(x) for x in row] + [Fraction(int(i == j)) for j in range(n)] for i, row in enumerate(m)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j] != 0)
        rows[j], rows[pivot] = rows[pivot], rows[j]
        rows[j] = [x / rows[j][j] for x in rows[j]]
        for i in range(n):
            if i != j:
                factor = rows[i][j]
                rows[i] = [a - factor * b for a, b in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def eig2(m):
    """The eigenvalues of a symmetric 2 x 2 matrix, in increasing order (from its trace and its determinant)."""
    tr, det = m[0][0] + m[1][1], m[0][0] * m[1][1] - m[0][1] * m[1][0]
    root = math.sqrt(tr ** 2 / 4 - det)
    return [tr / 2 - root, tr / 2 + root]


# CP4.1 (1): f, then g; a point is a row [x, y, 1], and [x, 1] H = [f(x), 1]
def homogeneous(lin, shift):
    """The 3 x 3 matrix (row convention) of (x, y) -> (lin[0] · (x, y) + shift[0], lin[1] · (x, y) + shift[1])."""
    return [[lin[0][0], lin[1][0], 0], [lin[0][1], lin[1][1], 0], [shift[0], shift[1], 1]]


HF_1 = homogeneous([[2, -1], [1, 0]], [1, 3])          # f(x, y) = (2x - y + 1, x + 3)
HG_1 = homogeneous([[0, 1], [-3, 1]], [-2, 4])         # g(x, y) = (y - 2, -3x + y + 4)
assert HF_1 == [[2, 1, 0], [-1, 0, 0], [1, 3, 1]] and HG_1 == [[0, -3, 0], [1, 1, 0], [-2, 4, 1]]
H_1 = matmul(HF_1, HG_1)                               # f first, then g: [x, 1] H_f H_g
P_1 = [-1, 3, 1]
IMAGE_1 = matmul([P_1], H_1)[0]
F_OF_G_1 = matmul([P_1], matmul(HG_1, HF_1))[0]        # g first, then f
COLUMN_1 = [dot(row, P_1) for row in H_1]              # H [x, y, 1]ᵀ: the column convention
INV_1 = inverse(H_1)                                   # exact fractions (its linear part is not whole)
assert matmul([IMAGE_1], INV_1)[0] == P_1              # the inverse sends the image back to P
F_ONLY_1 = matmul([P_1], HF_1)[0]                      # f alone
NUM_1 = [[x.numerator for x in row[:2]] for row in INV_1[:2]]          # W⁻¹ with its denominator 3 dropped
NODIV_1 = [-dot(H_1[2][:2], col) for col in zip(*NUM_1)] + [1]

# CP4.1 (2): the graph, its adjacency matrix A and its weight matrix W
EDGES_1 = {(5, 4): 2, (5, 3): -1, (5, 2): 1, (4, 2): 3, (4, 1): 1, (3, 2): 2, (3, 1): 4, (2, 1): -2}
A_1 = [[int((i, j) in EDGES_1) for j in range(1, 6)] for i in range(1, 6)]
W_1 = [[EDGES_1.get((i, j), 0) for j in range(1, 6)] for i in range(1, 6)]
FROM_1, TO_1 = 5 - 1, 1 - 1                            # from vertex 5 to vertex 1 (indices from 0)


def powers(m, k_max):
    """[m, m², ..., m^k_max]."""
    out = [m]
    for _ in range(k_max - 1):
        out.append(matmul(out[-1], m))
    return out


AK_1, WK_1 = powers(A_1, len(A_1)), powers(W_1, len(W_1))
NILPOTENT_1 = next(k for k, p in enumerate(AK_1, start=1) if all(x == 0 for row in p for x in row))
COUNT_1 = sum(p[FROM_1][TO_1] for p in AK_1)           # every path from 5 to 1, of every length
WEIGHT_1 = sum(p[FROM_1][TO_1] for p in WK_1)          # (W + W² + ... + W⁵)[5, 1]


def paths_1(i, j):
    """Every path from i to j, as a list of vertices."""
    if i == j:
        return [[j]]
    return [[i] + p for (a, b) in EDGES_1 if a == i for p in paths_1(b, j)]


PATHS_1 = paths_1(5, 1)
assert len(PATHS_1) == COUNT_1 and sum(math.prod(EDGES_1[e] for e in zip(p, p[1:])) for p in PATHS_1) == WEIGHT_1
ADDED_1 = sum(sum(EDGES_1[e] for e in zip(p, p[1:])) for p in PATHS_1)    # the weights of the edges added

# CP4.1 (3): the volume V = D T, with the flow D and the duration T independent
MD_1, SD_1, MT_1, ST_1 = Fraction(5), Fraction("0.3"), Fraction("1.5"), Fraction("0.1")
VD_1, VT_1 = SD_1 ** 2, ST_1 ** 2
MEAN_V_1 = MD_1 * MT_1
VAR_1 = VD_1 * VT_1 + VD_1 * MT_1 ** 2 + VT_1 * MD_1 ** 2

# CP4.2: f from R² to R³, g from R³ to R², at p = (2, -2)
P_2, U_2, Q_2 = (2, -2), (1, -2), (2.1, -2.05)


def f_2(x, y):
    return [x * y, x + 2 * y, math.exp(x + y)]


def g_2(a, b, c):
    return [a * c + b * b, b - a * a]


def jf_2(x, y):
    return [[y, x], [1, 2], [math.exp(x + y), math.exp(x + y)]]


def jg_2(a, b, c):
    return [[c, 2 * b, a], [-2 * a, 1, 0]]


F_2 = whole(f_2(*P_2))
JF_2, JG_2 = whole(jf_2(*P_2)), whole(jg_2(*F_2))
J_2 = matmul(JG_2, JF_2)                               # one row per output of g∘f
VJP_2 = matmul([U_2], J_2)[0]                          # uᵀ J
JVP_2 = [dot(row, U_2) for row in J_2]                 # J u


def cost(p, q, r):
    """The number of multiplications of a (p, q) matrix by a (q, r) one."""
    return p * q * r


N_OUT_2, N_MID_2, N_IN_2 = len(JG_2), len(JF_2), len(JF_2[0])
COSTS_2 = [cost(1, N_OUT_2, N_MID_2) + cost(1, N_MID_2, N_IN_2),      # (uᵀ J_g) J_f
           cost(N_OUT_2, N_MID_2, N_IN_2) + cost(1, N_OUT_2, N_IN_2)]  # uᵀ (J_g J_f)
H_2 = [q - p for q, p in zip(Q_2, P_2)]
GF_2 = g_2(*f_2(*P_2))
STEP_2 = [dot(row, H_2) for row in J_2]
LIN_2 = [v + s for v, s in zip(GF_2, STEP_2)]
POINT_2 = [v + dot(row, Q_2) for v, row in zip(GF_2, J_2)]           # J times the point, not the displacement
SIGN_H_2 = [v + dot(row, [H_2[0], -H_2[1]]) for v, row in zip(GF_2, J_2)]   # the sign of h2 lost
EXACT_2 = g_2(*f_2(*Q_2))
PHI_2 = [[3 * t ** 2 * x for x in row] for t, row in zip(F_2, JF_2)]  # diag(φ′(f(p))) J_f, φ′(t) = 3t²

# CP4.3: v1 = x + y² (the square is no node: the local derivative of y -> v1 is 2y), v2 = x v1, v3 = ln v1,
# f = v2 v3, at (5, -2)
X_3, Y_3 = 5, -2
V1_3 = X_3 + Y_3 ** 2
V2_3 = X_3 * V1_3
V3_3 = math.log(V1_3)
F_3 = V2_3 * V3_3
PARENTS_3 = {"v1": ("x", "y"), "v2": ("x", "v1"), "v3": ("v1",), "f": ("v2", "v3")}


def paths_3(start, end):
    """The number of paths from start to end in the graph."""
    if start == end:
        return 1
    return sum(paths_3(start, parent) for parent in PARENTS_3.get(end, ()))


USES_X_3 = sum("x" in parents for parents in PARENTS_3.values())     # x feeds two nodes


def tangents_3(dx, dy, direct=True, chained=True):
    """Forward mode from the seed (dx, dy): [v̇1, v̇2, v̇3, ḟ] (direct=False forgets the edge x -> v2 in v̇2,
    chained=False the edge v1 -> v2)."""
    d1 = dx + 2 * Y_3 * dy
    d2 = (dx * V1_3 if direct else 0) + (X_3 * d1 if chained else 0)
    d3 = d1 / V1_3
    return [d1, d2, d3, d2 * V3_3 + V2_3 * d3]


T_3 = tangents_3(1, 0)
DX_3, DY_3 = T_3[3], tangents_3(0, 1)[3]
B3_3 = V2_3                                            # reverse mode from f̄ = 1: f = v2 v3
B2_3 = V3_3
FROM_V2_3, FROM_V3_3 = B2_3 * X_3, B3_3 / V1_3         # v1 feeds v2 = x v1 and v3 = ln v1
B1_3 = FROM_V2_3 + FROM_V3_3
assert abs(B2_3 * V1_3 + B1_3 * 1 - DX_3) < 1e-12 and abs(B1_3 * 2 * Y_3 - DY_3) < 1e-12
N_IN_3, N_OUT_3 = 6, 25

# CP4.4: gradients with respect to X (each has the shape of X)
X_4 = [[4, 3], [5, 4]]
VA_4, VB_4 = (3, -1), (2, 5)
MA_4, MB_4 = [[-1, 4], [2, 1]], [[3, 1], [-5, 2]]
GA_4 = outer(VA_4, VB_4)                               # ∇(aᵀXb) = a bᵀ
GB_4 = transpose(MA_4)                                 # ∇tr(AX) = Aᵀ
GC_4 = matmul(add(MB_4, transpose(MB_4)), X_4)         # ∇tr(XᵀBX) = (B + Bᵀ) X
INV_4 = whole(inverse(X_4))
GD_4 = transpose(INV_4)                                # ∇ ln det X = X⁻ᵀ
H_4 = [[0, 0], [0.05, 0]]


def inner(a, b):
    """tr(aᵀ b) = Σ a_ij b_ij."""
    return sum(x * y for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


LIN_4 = inner(GD_4, H_4)
EXACT_4 = math.log(det2(add(X_4, H_4)) / det2(X_4))
Z_4 = [(2, 1), (0, 2), (1, -1), (1, 2)]
SUMZ_4 = [[sum(z[i] * z[j] for z in Z_4) for j in range(2)] for i in range(2)]   # Σ z zᵀ
GF_4 = floats(scale(Fraction(1, len(Z_4)), SUMZ_4))
XA_4, XB_4 = [dot(row, VA_4) for row in X_4], [dot(row, VB_4) for row in X_4]
TERM_A_4 = outer(XA_4, VB_4)                           # (dX a) · (Xb) gives (Xb) aᵀ; (Xa) · (dX b) gives (Xa) bᵀ
TERM_B_4 = outer(XB_4, VA_4)
GG_4 = add(TERM_A_4, TERM_B_4)                         # X (a bᵀ + b aᵀ)
SYM_4 = add(outer(VA_4, VB_4), outer(VB_4, VA_4))
assert GG_4 == matmul(X_4, SYM_4)
LEFT_4 = matmul(SYM_4, X_4)                            # X on the wrong side

# CP4.5: f(x, y, z) = x³ - 27x + 3y² + yz + 3z²
K_5 = 27


def f_5(x, y, z):
    return x ** 3 - K_5 * x + 3 * y ** 2 + y * z + 3 * z ** 2


def grad_5(x, y, z):
    return [3 * x ** 2 - K_5, 6 * y + z, y + 6 * z]


def hess_5(x, y, z, cross=1):
    return [[6 * x, 0, 0], [0, 6, cross], [0, cross, 6]]


P_5, H_5 = (1, 1, -1), (0.1, -0.1, 0.2)
G_5, HP_5 = grad_5(*P_5), hess_5(*P_5)


def quad_5(cross_weight=2):
    """hᵀ H h, with each crossed term H_ij h_i h_j (i < j) counted cross_weight times."""
    diagonal = sum(HP_5[i][i] * H_5[i] ** 2 for i in range(3))
    return diagonal + cross_weight * sum(HP_5[i][j] * H_5[i] * H_5[j] for i in range(3) for j in range(i + 1, 3))


QUAD_5 = quad_5()
assert abs(QUAD_5 - dot(H_5, [dot(row, H_5) for row in HP_5])) < 1e-12
T1_5 = f_5(*P_5) + dot(G_5, H_5)
T2_5 = T1_5 + QUAD_5 / 2
ERR_5 = f_5(*(p + h for p, h in zip(P_5, H_5))) - T2_5
assert abs(ERR_5 - H_5[0] ** 3) < 1e-12
ROOT_5 = whole(math.sqrt(K_5 / 3))
CRIT_5 = [[x, 0, 0] for x in (-ROOT_5, ROOT_5)]         # 3x² = 27; 6y + z = 0 = y + 6z (determinant 35): y = z = 0
assert all(grad_5(*c) == [0, 0, 0] for c in CRIT_5)


def eigenvalues_5(x, cross=1):
    """The eigenvalues of the hessian at (x, ., .), in increasing order: 6x, then those of the block in (y, z)."""
    h = hess_5(x, 0, 0, cross)
    return sorted([h[0][0]] + whole(eig2([row[1:] for row in h[1:]])))


def nature(eigs):
    if all(e > 0 for e in eigs):
        return "minimum"
    if all(e < 0 for e in eigs):
        return "maximum"
    if any(e > 0 for e in eigs) and any(e < 0 for e in eigs):
        return "selle"
    return "indéterminé"


EIG_5 = eigenvalues_5(CRIT_5[1][0])                     # the critical point of abscissa x > 0
CODES_5 = {"minimum": 1, "maximum": 2, "selle": 3, "indéterminé": 4}   # the numbers of the statement
NATURE_5 = [CODES_5[nature(EIG_5)], CODES_5[nature(eigenvalues_5(CRIT_5[0][0]))]]

# CP4.6 (1): Richardson x_{k+1} = x_k + ω(b − A x_k), from x_0 = 0
A_6, B_6, OMEGA_6 = [[7, -4], [-4, 7]], (-1, 10), Fraction(1, 10)
LAM_6 = whole(eig2(A_6))
assert LAM_6 == [3, 11]


def richardson_6(x, omega=OMEGA_6, sign=1):
    """One step x + ω(b − A x) (sign=-1: x + ω(A x − b))."""
    return [xi + sign * omega * (bi - dot(row, x)) for xi, bi, row in zip(x, B_6, A_6)]


X1_6 = richardson_6([0, 0])
X2_6 = richardson_6(X1_6)
SIGN_6 = [richardson_6([0, 0], sign=-1), richardson_6(richardson_6([0, 0], sign=-1), sign=-1)]
CRITICAL_6 = Fraction(2, max(LAM_6))
FACTORS_6 = [abs(1 - OMEGA_6 * lam) for lam in LAM_6]
KAPPA_6 = Fraction(max(LAM_6), min(LAM_6))
RATE_6 = (KAPPA_6 - 1) / (KAPPA_6 + 1)


def steps_6(rate, target=10 ** 4):
    """The smallest number of steps k with rate^k <= 1/target (exact, on fractions)."""
    k = 0
    while rate ** k * target > 1:
        k += 1
    return k


STEPS_6 = steps_6(RATE_6)
DOWN_6 = math.floor(math.log(10 ** 4) / -math.log(RATE_6))   # the real quotient rounded down

# CP4.6 (2): u_{k+2} = p u_{k+1} + q u_k, of characteristic polynomial r² − p r − q
P1_6, Q1_6 = Fraction("0.2"), Fraction("0.48")         # (R1)
P2_6, Q2_6 = 1, Fraction("-0.41")                      # (R2)


def roots_6(p, q):
    """The real roots of r² − p r − q, in increasing order."""
    disc = p * p + 4 * q
    return sorted([(p - math.sqrt(disc)) / 2, (p + math.sqrt(disc)) / 2])


ROOTS_6 = roots_6(P1_6, Q1_6)
DISC2_6 = P2_6 ** 2 + 4 * Q2_6
assert DISC2_6 < 0                                     # two conjugate roots p/2 ± i √(−disc)/2
RE_6, IM_6 = P2_6 / 2, math.sqrt(-DISC2_6) / 2
MOD_6 = math.hypot(RE_6, IM_6)
assert abs(MOD_6 ** 2 + Q2_6) < 1e-12                  # |z|² = z z̄ = −q

# CP4.7 (1): T[i, j, k]: building i, floor j, aisle k
T_7 = [[[4, 7, 1], [2, 4, 6]], [[3, 0, 6], [8, 1, 9]]]
W_7 = (1, -1, 2)
SHAPE_7 = (len(T_7), len(T_7[0]), len(T_7[0][0]))


def reduced(shape, axes, keepdims=False):
    """The shape after a reduction along the axes, written as NumPy prints it: "(2, 3)", "(3,)"."""
    return str(tuple(1 if i in axes else n for i, n in enumerate(shape) if keepdims or i not in axes))


def var(values, ddof=0):
    m = sum(values) / len(values)
    return sum((v - m) ** 2 for v in values) / (len(values) - ddof)


SUM_7 = [sum(x for row in b for x in row) for b in T_7]
MEAN_7 = [s / (SHAPE_7[1] * SHAPE_7[2]) for s in SUM_7]                        # T.mean(axis=(1, 2))
MEAN01_7 = [sum(T_7[i][j][k] for i in range(2) for j in range(2)) / 4 for k in range(3)]   # T.mean(axis=(0, 1))
MEAN02_7 = [sum(T_7[i][j][k] for i in range(2) for k in range(3)) / 6 for j in range(2)]   # T.mean(axis=(0, 2))
VAR_7 = [[var([floor[k] for floor in b], ddof=1) for k in range(3)] for b in T_7]          # T.var(axis=1, ddof=1)
VAR0_7 = [[var([floor[k] for floor in b]) for k in range(3)] for b in T_7]
VAR2_7 = [[var(floor, ddof=1) for floor in b] for b in T_7]                               # along axis 2
VARB_7 = [[var([b[j][k] for b in T_7], ddof=1) for k in range(3)] for j in range(2)]       # along axis 0
STD_7 = [[math.sqrt(v) for v in row] for row in VAR_7]
EIN_7 = [[dot(floor, W_7) for floor in b] for b in T_7]
SUMK_7 = [[sum(floor) for floor in b] for b in T_7]
assert all(abs(v - (a - b) ** 2 / 2) < 1e-12 for vb, b0 in zip(VAR_7, T_7) for v, a, b in zip(vb, *b0))

# CP4.7 (2): Poisson sampling, Ŷ = Σ_S y_i / π_i
Y_7 = [50, 26, 14, 22, 7]
PI_7 = [Fraction(p) for p in ("1", "0.65", "0.35", "0.55", "0.1")]
S_7 = [1, 3, 5]
HT_7 = sum(Y_7[i - 1] / PI_7[i - 1] for i in S_7)
RAW_7 = sum(Y_7[i - 1] for i in S_7)
TIMES_7 = sum(Y_7[i - 1] * PI_7[i - 1] for i in S_7)
ALL_7 = sum(y / p for y, p in zip(Y_7, PI_7))
VAR_HT_7 = sum(y * y * (1 - p) / p for y, p in zip(Y_7, PI_7))                # Σ y² (1 − π)/π
VAR_S_7 = sum(Y_7[i - 1] ** 2 * (1 - PI_7[i - 1]) / PI_7[i - 1] for i in S_7)
VAR_SQ_7 = sum(y * y * (1 - p) / p ** 2 for y, p in zip(Y_7, PI_7))
NO_COMPLEMENT_7 = sum(y * y / p for y, p in zip(Y_7, PI_7))                     # Σ y²/π
EST_7 = sum(Y_7[i - 1] ** 2 * (1 - PI_7[i - 1]) / PI_7[i - 1] ** 2 for i in S_7)   # the estimate from S

# CP4.10: L(a, b) = ½ Σ (e^{a + b x_i} − y_i)²; u_i = a + b x_i, v_i = e^{u_i}, r_i = v_i − y_i
X_10, Y_10, ETA_10 = (-1, 0, 2), (0.5, 1, 4), 0.1


def forward_10(a, b):
    """u, v, r and L at (a, b)."""
    u = [a + b * x for x in X_10]
    v = [math.exp(t) for t in u]
    r = [vi - yi for vi, yi in zip(v, Y_10)]
    return u, v, r, sum(ri * ri for ri in r) / 2


_, V0_10, R0_10, L0_10 = forward_10(0, 0)
UBAR_10 = [ri * vi for ri, vi in zip(R0_10, V0_10)]   # ū_i = r̄_i ∂r/∂v ∂v/∂u = r_i e^{u_i}
GRAD_10 = [sum(UBAR_10), dot(X_10, UBAR_10)]          # ∂u_i/∂a = 1, ∂u_i/∂b = x_i
A1_10 = [-ETA_10 * g for g in GRAD_10]
L1_10 = forward_10(*A1_10)[3]
UP_10 = forward_10(*[ETA_10 * g for g in GRAD_10])[3]  # a step up the gradient
B_STAR_10 = (math.log(Y_10[2]) - math.log(Y_10[0])) / (X_10[2] - X_10[0])
STAR_10 = [math.log(Y_10[1]) - B_STAR_10 * X_10[1], B_STAR_10]
assert forward_10(*STAR_10)[3] < 1e-20                 # the three measurements are on the curve


def hessian_10(a, b):
    """The hessian of L: Σ w_i [[1, x_i], [x_i, x_i²]], with w_i = v_i (v_i + r_i)."""
    _, v, r, _ = forward_10(a, b)
    w = [vi * (vi + ri) for vi, ri in zip(v, r)]
    return [[sum(wi * x ** (i + j) for wi, x in zip(w, X_10)) for j in range(2)] for i in range(2)]


HS_10 = hessian_10(*STAR_10)
SY_10 = [[sum(y * x ** (i + j) for y, x in zip(Y_10, X_10)) for j in range(2)] for i in range(2)]   # Σ y_i [1, x_i; ...]
EIG_10 = eig2(HS_10)
B_ROUNDED_10 = round(B_STAR_10, 3)                     # b* rounded to 0.693 before the hessian
V_ROUNDED_10 = forward_10(STAR_10[0], B_ROUNDED_10)[1]
H_ROUNDED_10 = [[sum(v * v * x ** (i + j) for v, x in zip(V_ROUNDED_10, X_10)) for j in range(2)] for i in range(2)]
EIG_ROUNDED_10 = eig2(H_ROUNDED_10)'''

PAPER = [
    Paper("CP4.1", "Coordonnées homogènes, chemins d'un graphe et variance d'un produit", [
        ("a", "a list of 3 lists", "H_1",
         'mistakes={"avec des points en lignes, [x, 1] H_f applique f : dans quel ordre multiplier H_f et H_g pour '
         'faire f, puis g ?": matmul(HG_1, HF_1), "en convention ligne, la translation est dans la dernière ligne": '
         'transpose(H_1)}'),
        ("b", "a list of 2 numbers", "IMAGE_1[:2]",
         'mistakes={"on applique f d\'abord, puis g": F_OF_G_1[:2], "en convention ligne, le point est une ligne '
         'qui multiplie la matrice à gauche : [x, y, 1] H": COLUMN_1[:2], "on applique f, puis g": F_ONLY_1[:2]}'),
        ("c", "a list of 3 numbers", "whole(INV_1[2])",
         'mistakes={"c\'est la dernière ligne de la matrice de g∘f ; la question porte sur la réciproque": H_1[2], '
         '"la translation de la réciproque n\'est pas l\'opposée de celle de g∘f": [-H_1[2][0], -H_1[2][1], 1], '
         '"la translation de la réciproque est −b W⁻¹ : as-tu inversé W ?": NODIV_1}'),
        ("d", "an integer", "AK_1[1][FROM_1][TO_1]",
         'mistakes={"un chemin de longueur 2 a deux arêtes (et un seul sommet intermédiaire)": AK_1[2][FROM_1][TO_1], '
         '"seulement les chemins de deux arêtes : la question ne compte pas les autres longueurs": COUNT_1, '
         '"le sens compte : des chemins qui partent de 5 et arrivent en 1": AK_1[1][TO_1][FROM_1]}'),
        ("e", "an integer", "NILPOTENT_1",
         'mistakes={"un graphe sans cycle à 5 sommets vérifie toujours A⁵ = 0, mais une puissance plus petite peut '
         'déjà être nulle": len(A_1), "Aᵏ compte les chemins de longueur k : en existe-t-il un de longueur 3 ?": '
         'NILPOTENT_1 - 1}'),
        ("f", "a number", "WEIGHT_1",
         'mistakes={"tous les chemins, de toutes les longueurs": {WK_1[1][FROM_1][TO_1], WK_1[2][FROM_1][TO_1]}, '
         '"la question demande la somme des poids, pas le nombre de chemins": COUNT_1, '
         '"le poids d\'un chemin est le produit des poids de ses arêtes": ADDED_1}'),
        ("g", "a number", "float(MEAN_V_1)", "decimals=6"),
        ("h", "a number (4 decimals)", "float(VAR_1)",
         'decimals=4, mistakes={"Var(DT) n\'est pas le produit des variances : les moyennes comptent aussi": '
         'float(VD_1 * VT_1), "Var(DT) a trois termes : en as-tu oublié un ?": float(VAR_1 - VD_1 * VT_1), '
         '"la question demande la variance, pas l\'écart-type": math.sqrt(VAR_1), '
         '"la formule utilise les variances, pas les écarts-types": '
         'float(SD_1 * ST_1 + SD_1 * MT_1 ** 2 + ST_1 * MD_1 ** 2), '
         '"la formule utilise les variances et les carrés des moyennes": float(SD_1 * MT_1 + ST_1 * MD_1 + SD_1 * ST_1), '
         '"chaque variance est multipliée par le carré de la moyenne de l\'autre facteur": '
         'float(VD_1 * MD_1 ** 2 + VT_1 * MT_1 ** 2 + VD_1 * VT_1)}'),
    ]),
    Paper("CP4.2", "Jacobienne d'une composée et produit vecteur-jacobienne", [
        ("a", "a list of 3 numbers", "F_2", ""),
        ("b", "a list of 3 lists", "JF_2",
         'mistakes={"une ligne par sortie, une colonne par entrée": transpose(JF_2), "vérifie ∂(xy)/∂x et ∂(xy)/∂y": '
         '[list(P_2)] + JF_2[1:]}'),
        ("c", "a list of 2 lists", "JG_2",
         'mistakes={"une ligne par sortie, une colonne par entrée": transpose(JG_2), "vérifie la dérivée de −a²": '
         '[JG_2[0], [-JG_2[1][0]] + JG_2[1][1:]]}'),
        ("d", MATRIX, "J_2",
         'mistakes={"une ligne par sortie de g∘f, une colonne par entrée": transpose(J_2), '
         '"g∘f a 2 sorties et 2 entrées : dans quel ordre se multiplient les deux jacobiennes ?": matmul(JF_2, JG_2)}'),
        ("e", "a list of 2 numbers", "VJP_2",
         'mistakes={"uᵀJ combine les lignes de J ; J u combine ses colonnes": JVP_2}'),
        ("f", "a list of 2 integers", "COSTS_2",
         'mistakes={"l\'ordre : (uᵀJ_g)J_f d\'abord, puis uᵀ(J_gJ_f)": COSTS_2[::-1], '
         '"uᵀ(J_gJ_f) demande deux produits : J_gJ_f, puis uᵀ par le résultat": [COSTS_2[0], '
         'cost(N_OUT_2, N_MID_2, N_IN_2)]}'),
        ("g", "a list of 2 numbers", "LIN_2",
         'decimals=2, mistakes={"l\'approximation linéaire part de la valeur en p : (g∘f)(p + h) ≈ (g∘f)(p) + J h": '
         'STEP_2, "la question demande l\'approximation linéaire, pas la valeur exacte": EXACT_2, '
         '"J multiplie le déplacement h = (2,1 ; −2,05) − p, pas le point": POINT_2, '
         '"vérifie le déplacement h = (2,1 − 2 ; −2,05 − (−2))": SIGN_H_2}'),
        ("h", "a list of 3 lists", "PHI_2",
         'mistakes={"la dérivée de t³ est 3t²": [[3 * t * x for x in row] for t, row in zip(F_2, JF_2)], '
         '"la jacobienne de φ est diagonale, de coefficients φ′(tᵢ) : la dérivée de t³, pas t³": '
         '[[t ** 3 * x for x in row] for t, row in zip(F_2, JF_2)]}'),
    ]),
    Paper("CP4.3", "Mode direct et mode inverse sur un graphe de calcul", [
        ("a", "a number (4 decimals)", "F_3",
         'decimals=4, mistakes={"ln est le logarithme népérien": V2_3 * math.log10(V1_3)}'),
        ("b", "an integer", 'paths_3("x", "f")',
         'mistakes={"x sert deux fois, dans v₁ et dans v₂ : chaque usage ouvre au moins un chemin vers f": 1, '
         '"v₁ sert aussi deux fois, dans v₂ et dans v₃ : suis chaque chemin jusqu\'à f": USES_X_3}'),
        ("c", "a list (4 decimals)", "T_3[:3]",
         'decimals=4, mistakes={"v₂ = x v₁ : sa tangente a deux termes": tangents_3(1, 0, direct=False)[:3], '
         '"la graine est sur x : ẋ = 1 et ẏ = 0": tangents_3(0, 1)[:3], '
         '"v₂ = x v₁ : sa tangente a deux termes, un pour chaque facteur": tangents_3(1, 0, chained=False)[:3]}'),
        ("d", "a number (3 decimals)", "DX_3",
         'decimals=3, mistakes={"x sert deux fois : as-tu suivi l\'arête directe x → v₂ ?": '
         'tangents_3(1, 0, direct=False)[3], "f = v₂ v₃ : sa tangente a deux termes": '
         '{T_3[1] * V3_3, V2_3 * T_3[2]}, "c\'est ∂f/∂y ; la graine sur x donne ∂f/∂x": DY_3}'),
        ("e", "a list (4 decimals)", "[B3_3, B2_3]",
         'decimals=4, mistakes={"relis l\'ordre demandé, [v̄₃, v̄₂] : l\'adjoint de v₃ est ∂f/∂v₃": [B2_3, B3_3]}'),
        ("f", "a number (4 decimals)", "B1_3",
         'decimals=4, mistakes={"v₁ sert deux fois (dans v₂ et dans v₃) : additionne les deux contributions": '
         '{FROM_V2_3, FROM_V3_3}, "la dérivée de ln v est 1/v": FROM_V2_3 + B3_3 * V1_3}'),
        ("g", "a number (4 decimals)", "B1_3 * 2 * Y_3",
         'decimals=4, mistakes={"y entre dans v₁ avec la dérivée locale 2y": {B1_3, -B1_3}, '
         '"y = −2 : vérifie le signe de la dérivée locale 2y": -B1_3 * 2 * Y_3, '
         '"c\'est ∂f/∂x ; la question demande ∂f/∂y": DX_3, "v₁ sert deux fois : as-tu reçu les deux '
         'contributions ?": {2 * Y_3 * FROM_V2_3, 2 * Y_3 * FROM_V3_3}}'),
        ("h", "a list of 2 integers", "[N_IN_3, N_OUT_3]",
         'mistakes={"le mode direct donne une colonne de la jacobienne par passage, le mode inverse une ligne": '
         '[N_OUT_3, N_IN_3]}'),
    ]),
    Paper("CP4.4", "Gradients par rapport à une matrice", [
        ("a", MATRIX, "GA_4",
         'mistakes={"le coefficient (i, j) est ∂f/∂X_ij, et X_ij multiplie a_i b_j : la ligne vient de a": '
         'transpose(GA_4)}'),
        ("b", MATRIX, "GB_4",
         'mistakes={"tr(AX) = Σ A_ji X_ij : relis l\'ordre des indices": MA_4}'),
        ("c", MATRIX, "GC_4",
         'mistakes={"B n\'est pas symétrique : quelle matrice symétrique remplace 2B ?": scale(2, matmul(MB_4, X_4)), '
         '"X apparaît deux fois dans XᵀBX : la différentielle a deux termes": matmul(MB_4, X_4), '
         '"X apparaît deux fois dans XᵀBX : chaque X donne un terme": matmul(transpose(MB_4), X_4), '
         '"l\'ordre des facteurs : le gradient de xᵀSx est Sx": matmul(X_4, add(MB_4, transpose(MB_4)))}'),
        ("d", MATRIX, "GD_4",
         'mistakes={"regarde un coefficient hors de la diagonale : ∂ ln det X / ∂X₁₂ vaut-il (X⁻¹)₁₂ ou (X⁻¹)₂₁ ?": '
         'INV_4}'),
        ("e", "a number", "LIN_4",
         'decimals=2, mistakes={"H ne touche que X₂₁ : ∂ ln det X / ∂X₂₁ vaut-il (X⁻¹)₂₁ ou (X⁻¹)₁₂ ?": '
         'inner(INV_4, H_4), "la question demande l\'approximation au premier ordre, pas la valeur exacte": EXACT_4}'),
        ("f", MATRIX, "GF_4",
         'decimals=2, mistakes={"F est une moyenne : son gradient aussi": SUMZ_4}'),
        ("g", MATRIX, "GG_4",
         'mistakes={"X apparaît deux fois : d(XᵀX) a deux termes": TERM_A_4, '
         '"X apparaît deux fois : d(XᵀX) a deux termes, garde les deux": TERM_B_4, '
         '"dans d(Xa) = dX a, la matrice X est à gauche": LEFT_4}'),
    ]),
    Paper("CP4.5", "Hessienne, Taylor d'ordre 2 et nature d'un point critique", [
        ("a", "a list of 3 numbers", "G_5", ""),
        ("b", "a list of 3 lists", "HP_5",
         'mistakes={"dérive yz par rapport à y, puis par rapport à z : que vaut ∂²(yz)/∂y∂z ?": '
         'hess_5(*P_5, cross=2)}'),
        ("c", "a number", "T2_5",
         'decimals=2, mistakes={"le terme d\'ordre 2 a un facteur ½ : relis la formule de T₂": T1_5 + QUAD_5, '
         '"c\'est le développement d\'ordre 1 ; T₂ ajoute le terme ½ hᵀHh": T1_5, '
         '"hᵀHh compte aussi les termes croisés H_ij h_i h_j (i ≠ j)": T1_5 + quad_5(0) / 2, '
         '"hᵀHh = Σᵢ Σⱼ H_ij h_i h_j : chaque terme croisé compte deux fois": T1_5 + quad_5(1) / 2}'),
        ("d", "a number", "ERR_5",
         'decimals=3, mistakes={"l\'erreur est f(P + h) − T₂(P + h), dans cet ordre": -ERR_5}'),
        ("e", "a list of points [x, y, z]", "CRIT_5",
         'mistakes={"la question demande les points rangés par x croissant": CRIT_5[::-1], '
         '"3x² = 27 a deux solutions": [CRIT_5[1]], '
         '"3x² = 27 a deux solutions : la liste demandée a un point par solution": CRIT_5[1]}'),
        ("f", "a list of 3 numbers", "EIG_5",
         'mistakes={"la question demande l\'ordre croissant": EIG_5[::-1], '
         '"la question porte sur le point critique d\'abscisse x > 0 : as-tu calculé la hessienne en ce point ?": '
         'eigenvalues_5(CRIT_5[0][0]), "la hessienne se calcule au point critique, pas en P": '
         'eigenvalues_5(P_5[0]), "le bloc en (y, z) n\'est pas diagonal : ses valeurs propres ne sont pas ses '
         'coefficients diagonaux": eigenvalues_5(CRIT_5[1][0], cross=0)}'),
        ("g", NATURE, "NATURE_5[0]",
         'choices=list(CODES_5.values()), mistakes={"un point selle demande des valeurs propres de signes opposés : '
         'quels sont leurs signes ici ?": CODES_5["selle"], "un maximum local demande que toutes les valeurs propres '
         'soient négatives : quel est leur signe ici ?": CODES_5["maximum"], "le test ne conclut pas quand une valeur '
         'propre est nulle (et que les autres ont le même signe) : en est-il une ici ?": CODES_5["indéterminé"]}'),
        ("h", NATURE, "NATURE_5[1]",
         'choices=list(CODES_5.values()), mistakes={"un minimum local demande que toutes les valeurs propres de la '
         'hessienne soient positives : est-ce le cas en ce point ?": CODES_5["minimum"], "un maximum local demande '
         'que toutes les valeurs propres soient négatives : est-ce le cas en ce point ?": CODES_5["maximum"], '
         '"le test ne conclut pas quand une valeur propre est nulle : en est-il une ici ?": CODES_5["indéterminé"]}'),
    ]),
    Paper("CP4.6", "Itération de Richardson et récurrence d'ordre 2", [
        ("a", "a list of 2 numbers", "floats(X1_6)",
         'decimals=1, mistakes={"le pas ajoute ω fois le résidu b − A x, dans cet ordre": floats(SIGN_6[0]), '
         '"x₁ = x₀ + ω(b − A x₀) : où est ω dans ton calcul ?": list(B_6)}'),
        ("b", "a list of 2 numbers", "floats(X2_6)",
         'decimals=2, mistakes={"le résidu se recalcule au nouveau point x₁": '
         'floats([x + OMEGA_6 * b for x, b in zip(X1_6, B_6)]), '
         '"le pas ajoute ω fois le résidu b − A x, dans cet ordre": floats(SIGN_6[1]), '
         '"le résidu est b − A x₁, dans cet ordre": floats(richardson_6(X1_6, sign=-1)), '
         '"l\'itération part de x₁ : où est x₁ dans ton calcul ?": '
         'floats([x2 - x1 for x2, x1 in zip(X2_6, X1_6)])}'),
        ("c", 'an irreducible fraction, as text (like "3/8")', "CRITICAL_6",
         'kind="fraction", simplified=True, mistakes={"le pas critique se règle sur la plus grande valeur propre": '
         'Fraction(2, min(LAM_6)), "le pas critique est la borne des ω tels que |1 − ωλ| < 1 pour toute valeur '
         'propre λ": Fraction(1, max(LAM_6)), "c\'est le pas optimal ; la question demande le pas critique": '
         'Fraction(2, sum(LAM_6))}'),
        ("d", "a number", "float(max(FACTORS_6))",
         'decimals=2, mistakes={"le facteur est le plus grand des |1 − ωλᵢ|, pas le plus petit": '
         'float(min(FACTORS_6)), "les λᵢ sont les valeurs propres de A, pas ses coefficients diagonaux": '
         'float(abs(1 - OMEGA_6 * A_6[0][0]))}'),
        ("e", "an integer", "STEPS_6",
         'fractional="k est un nombre de pas : arrondis à l\'entier qui garantit 10⁻⁴.", '
         'mistakes={"avec ce nombre de pas, l\'erreur est-elle bien divisée par 10⁴ ? Le nombre de pas doit le '
         'garantir": DOWN_6, "au pas optimal, pas à ω = 0,1": steps_6(max(FACTORS_6)), '
         '"le facteur au pas optimal est (κ − 1)/(κ + 1)": steps_6(1 - 1 / KAPPA_6)}'),
        ("f", "a list of 2 numbers", "ROOTS_6",
         'decimals=1, mistakes={"u_{k+2} = a u_{k+1} + b u_k donne r² − a r − b : vérifie les signes": '
         'roots_6(-P1_6, Q1_6), "la question demande l\'ordre croissant": ROOTS_6[::-1]}'),
        ("g", "a number (4 decimals)", "MOD_6",
         'decimals=4, mistakes={"le module d\'une racine complexe n\'est ni sa partie réelle, ni sa partie '
         'imaginaire": {RE_6, IM_6}, '
         '"le produit z z̄ des deux racines conjuguées n\'est pas leur module : quel lien entre z z̄ et |z| ?": '
         'float(-Q2_6), '
         '"|a + ib| = √(a² + b²)": RE_6 + IM_6}'),
    ]),
    Paper("CP4.7", "Moments le long d'axes, einsum et estimateur de Horvitz-Thompson", [
        ("a", SHAPE, "reduced(SHAPE_7, (1,))",
         'mistakes={"sans keepdims=True, l\'axe réduit disparaît au lieu de garder la longueur 1": '
         'reduced(SHAPE_7, (1,), keepdims=True), "axis=1 est l\'axe des étages (les axes se comptent à partir de 0) : '
         'c\'est lui qui disparaît": reduced(SHAPE_7, (2,)), "axis=1 ne réduit qu\'un seul axe : les autres gardent '
         'leur longueur": {reduced(SHAPE_7, (0, 1)), reduced(SHAPE_7, (1, 2))}, "sum(axis=1) somme le long de l\'axe '
         '1 : cet axe disparaît du résultat": str(SHAPE_7)}'),
        ("b", "a list of 2 numbers", "MEAN_7",
         'decimals=2, mistakes={"mean divise par le nombre de valeurs réduites": SUM_7, "axis=(1, 2) réduit les '
         'étages et les allées : il reste une valeur par bâtiment": MEAN01_7, '
         '"quels axes portent les étages et les allées ?": MEAN02_7}'),
        ("c", "a list of 2 lists of 3 numbers", "VAR_7",
         'decimals=2, mistakes={"ddof=1 divise par n − 1": VAR0_7, '
         '"axis=1 est l\'axe des étages (les axes se comptent à partir de 0)": VAR2_7, '
         '"quel axe porte les étages ?": VARB_7, "la question demande la variance, pas l\'écart-type": STD_7}'),
        ("d", "a list of 2 lists of 2 numbers", "EIN_7",
         'mistakes={"einsum multiplie par w avant de sommer sur k": SUMK_7}'),
        ("e", "a number", "float(HT_7)",
         'decimals=2, mistakes={"chaque observation est divisée par sa probabilité d\'inclusion": '
         '{float(RAW_7), float(TIMES_7)}, "Ŷ ne lit que les unités tirées": {sum(Y_7), float(ALL_7)}}'),
        ("f", "a number", "whole(VAR_HT_7)",
         'mistakes={"la variance porte sur tous les tirages possibles : elle somme sur toute la population": '
         'whole(VAR_S_7), "vérifie le facteur (1 − πᵢ)/πᵢ": {whole(VAR_SQ_7), whole(NO_COMPLEMENT_7)}, "c\'est l\'estimation de la variance '
         'à partir de l\'échantillon tiré ; la question demande la variance elle-même": whole(EST_7)}'),
    ]),
    Paper("CP4.9", "Corriger une copie : cinq erreurs (les lettres seulement)", [
        ("a", 'the letters, as text (like "ABCDE")', '"ACDGH"', f"mistakes={LETTERS}"),
    ]),
    Paper("CP4.10", "Problème de synthèse : ajuster une loi exponentielle, du graphe de calcul au pas critique", [
        ("a", "a number", "L0_10",
         'decimals=6, mistakes={"relis la définition de L : quel facteur précède la somme ?": 2 * L0_10}'),
        ("b", "a list of 3 numbers", "UBAR_10",
         'decimals=1, mistakes={"r_i = v_i − y_i : vérifie le signe": [-u for u in UBAR_10]}'),
        ("c", "a list of 2 numbers", "GRAD_10",
         'decimals=1, mistakes={"vérifie le signe des résidus r_i = v_i − y_i": [-g for g in GRAD_10], '
         '"u_i = a + b x_i : quelle est la dérivée locale de l\'arête b → u_i ?": [GRAD_10[0], GRAD_10[0]]}'),
        ("d", "a list of 2 numbers", "A1_10",
         'decimals=2, mistakes={"on descend : un pas de descente retire η∇L": [ETA_10 * g for g in GRAD_10]}'),
        ("e", "a number (3 decimals)", "L1_10",
         'decimals=3, mistakes={"relis la définition de L : quel facteur précède la somme ?": 2 * L1_10, '
         '"vérifie le point (a₁, b₁) : un pas de descente retire η∇L": UP_10}'),
        ("f", "a list (3 decimals)", "STAR_10",
         'decimals=3, mistakes={"quand x augmente de 1, le modèle e^(a + bx) multiplie y par e^b : as-tu donné b, '
         'ou e^b ?": '
         '[STAR_10[0], math.exp(STAR_10[1])], "a est un exposant : le modèle vaut e^(a + bx)": '
         '[math.exp(STAR_10[0]), STAR_10[1]], "le modèle utilise l\'exponentielle de base e : le logarithme '
         'népérien": [STAR_10[0], STAR_10[1] / math.log(10)], '
         '"b est le logarithme du facteur de croissance": [STAR_10[0], math.exp(-STAR_10[1])]}'),
        ("g", MATRIX, "HS_10",
         'decimals=2, mistakes={"la hessienne demandée est celle du minimum (a⋆, b⋆)": hessian_10(0, 0), '
         '"au minimum, les résidus sont nuls : que devient v_i(v_i + r_i) ?": SY_10, '
         '"relis la définition de L : quel facteur précède la somme ?": scale(2, HS_10), '
         '"calcule la hessienne avec les valeurs exactes en (a*, b*) : que valent les vᵢ ?": H_ROUNDED_10}'),
        ("h", "a list (3 decimals)", "EIG_10",
         'decimals=3, mistakes={"la question demande l\'ordre croissant": EIG_10[::-1], '
         '"calcule la hessienne avec les valeurs exactes en (a*, b*) : que valent les vᵢ ?": EIG_ROUNDED_10}'),
        ("i", "a number (4 decimals)", "2 / EIG_10[1]",
         'decimals=4, mistakes={"le pas critique se règle sur la plus grande valeur propre": 2 / EIG_10[0], '
         '"le pas critique est la borne des η tels que |1 − ηλ| < 1 pour toute valeur propre λ": 1 / EIG_10[1], '
         '"c\'est le pas optimal ; la question demande le pas critique": 2 / sum(EIG_10)}'),
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
    """CP4.2a before CP4.10a: the question number as a number, then the letter."""
    number, letter = re.match(r"CP4\.(\d+)(.*)", sub_id).groups()
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

**Ne commence qu'une fois ta copie terminée**, examen rendu. Ce notebook vérifie les réponses que tu as écrites sur ta feuille, question par question : ✅ juste, ❌ faux (avec une piste), ⏳ pas rempli. Il ne note pas : les démarches, les justifications, le quiz CP4.Q1, la démonstration CP4.8 et les corrections de CP4.9 b) se corrigent avec `03_examen_corrige.md`, qui donne aussi le barème.

1. Passe `EXAM_OVER` à `True` dans la cellule ci-dessous, puis exécute-la.
2. Reporte chaque réponse de ta feuille : **la valeur** que tu as écrite, pas un nouveau calcul (sinon tu ne vérifies plus ta copie). Laisse `...` pour une question que tu n'as pas faite.
3. Si une cellule s'arrête sur une erreur, « Tout exécuter » s'arrête avec elle : corrige-la, puis relance cette cellule et les suivantes, jusqu'au bilan.
4. Les formes d'écriture : en Python, le séparateur décimal est un **point** (`2.75`) : une virgule arrête toute la cellule (`0,027`), et aucune réponse de la question n'est vérifiée, ou donne un couple de nombres (`0,75`) ; une liste s'écrit entre crochets (`[-1.5, 4]`), une matrice comme une liste de lignes (`[[1, -2], [0.5, 3]]`) ; un texte entre guillemets (`"XYZ"`), comme une fraction (`"3/8"`) ou une forme (`"(4, 5)"`) ; un numéro de choix s'écrit sans guillemets.
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
        title = "# CP4 · Examen blanc de la partie IV — vérification de ta copie"
        how = ("L'examen se fait **sur papier** (`01_examen_sujet.md`, 110 minutes, fiches fermées). Ce notebook ne "
               "sert qu'**après** : il vérifie les réponses chiffrées de ta copie. Ses cellules ne vérifient rien tant "
               "que `EXAM_OVER` vaut `False`, et « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli (⏸️).\n\n"
               "> Travaille dans **ta copie** (`mon_travail/checkpoints/partie_4/02_examen_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py CP4`) : ce fichier-ci est mis à jour par Claude. Sur Colab, le badge "
               "ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme l'explique "
               "`00_setup/COLAB.md` §2.")
    else:
        title = "# CP4 · Examen blanc de la partie IV — solutions (notebook exécuté)"
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
                        "CP4.Q1 ; la démonstration CP4.8 ; les corrections de CP4.9 b) (seules les lettres de a) sont "
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
