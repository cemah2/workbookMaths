#!/usr/bin/env python
"""Build the two notebooks of the mock exam CP5 from a single source (used by Claude).

    python tools/chapters/build_cp5.py
    python tools/run_all_notebooks.py checkpoints/partie_5/03_examen_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py checkpoints/partie_5/02_examen_notebook.ipynb

Same mechanism as build_cp4.py: the exam of CP5 is on paper only (01_examen_sujet.md), and the exam notebook is the
check done AFTER the exam; nothing is checked while EXAM_OVER is False, so that « Run all » goes to the end.
Wrong-answer messages state a rule or ask a question, never a number of the answer, the calculation that gives it,
its last step, nor another sub-question. The solutions notebook records the answers, each one computed from the
numbers of the statement, with NumPy (convolutions, matrix powers, eigenvalues, norms) and exact fractions (the
recurrences, the jacobians, the limits and bounds), cross-checked by asserts (brute force on the windows, the stamps,
the receptive field, the vertices of the cube, finite differences); the cells are tagged `answer` and read by
build_answers.py. 60 checks: CP5.1 to CP5.7, the letters of CP5.9 a) and CP5.10 a) to g). Not in the notebook: the
true/false quiz CP5.Q1, the proof CP5.8 and the corrections of CP5.9 b) (only its letters are checked).

Accepted forms: a tuple for a list, a fraction or a decimal for a number (a fraction typed between quotes is read),
a complex number a + bj for the list [a, b] of CP5.6 a) (converted in the check cell), the window lengths of CP5.2 d)
and the values of CP5.2 h) in any order (sets); the behaviour of powers is a code 1, 2 or 3 (a word would refuse
correct synonyms), the argument of CP5.6 c) an exact angle (degrees are recognised and refused with a message), the
limit of CP5.10 g) an irreducible fraction, as the statement asks; M⁶ of CP5.6 e) is exact with 6 decimals and is
checked on 4, so that its value rounded to 4 decimals passes too.

The data are those of 01_examen_sujet.md, version 2 of session 59, after the two reviews (sharing rule, exam taken
blind): w = (3, 0, −2, 1) in CP5.1; the window lengths k that give 110 positions (CP5.2 d) and k = 10, s = 3
(CP5.2 h); in CP5.3, the two orders of the two passes (c), kernels 3 × 5 with a padding of 1 in height and 2 in width
(d to g) and the stack (2, 1, 1), (4, 3, 1), (2, 1, 3), (3, 4, 1) (h); strain gauges on the five blades of a rotor
with h = (1, −4, 2, 3, −2) and the largest INCREASE of z₁ (CP5.4); a drug between blood and tissues, same numbers,
the eigenvalues in c) (CP5.5); M = [[0, −1], [0.75, 1.5]], M³, M⁶ and (2/√3) M (CP5.6); new lines in CP5.9, same
letters; no γ-stability in CP5.10 (h and i removed). The data were chosen and checked against both repositories by
the author of the statement: none comes from M21, M22, CP0 to CP4, chapters 21 to 24 of workbookIA, its checkpoint V
or its mini-project V. No seed: no random draw.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import Paper, check_unique_keys, md  # noqa: E402
from nbbuild import badge, code, setup_cell, write_notebook  # noqa: E402

FOLDER = "checkpoints/partie_5"
EXAM = f"{FOLDER}/02_examen_notebook.ipynb"
SOLUTIONS = f"{FOLDER}/03_examen_solutions.ipynb"
MINUTES = 112                       # the sum of the durations of CP5.Q1 to CP5.10 in the syllabus

MATRIX = "a matrix, as a list of rows"
COMPLEX = "a list [a, b] for a + ib"
ANGLE = 'an exact angle in radians, as text (like "pi/5")'
FRACTION = 'an irreducible fraction, as text (like "3/8")'


def _letter_sets():
    """CP5.9 a: wrong sets of letters, by kind, with messages that name no line (the corrigé explains each line)."""
    from itertools import combinations

    wrong, right = "ABDEG", "CFH"
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

PAPER_CONTEXT = r'''# The answers are computed from the numbers of the statements (01_examen_sujet.md), with NumPy and exact fractions
import math
from fractions import Fraction
from itertools import product

import numpy as np


def ints(a):
    """An array (or nested lists) of whole numbers as lists of int, after checking that every value is whole."""
    arr = np.asarray(a, dtype=float)
    assert np.allclose(arr, np.round(arr)), arr
    return np.round(arr).astype(int).tolist()


def floats(a):
    """Fractions or floats (a number, nested lists or an array) as plain floats."""
    return np.asarray(a, dtype=float).tolist()


def fmat(rows):
    """A matrix written with the decimals of the statement ("0.5"), as exact fractions."""
    return [[Fraction(x) for x in row] for row in rows]


def fmatmul(p, q):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*q)] for row in p]


def fmatvec(p, v):
    return [sum(a * b for a, b in zip(row, v)) for row in p]


def fpow(p, k):
    out = [[Fraction(int(i == j)) for j in range(len(p))] for i in range(len(p))]
    for _ in range(k):
        out = fmatmul(p, out)                          # one product per step
    return out


def ftranspose(p):
    return [list(col) for col in zip(*p)]


def finv2(p):
    """The inverse of a 2 x 2 matrix of fractions."""
    (a, b), (c, d) = p
    det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]]


def fsqrt(q):
    """The exact square root of a fraction that is a perfect square (16/25 -> 4/5)."""
    q = Fraction(q)
    num, den = math.isqrt(q.numerator), math.isqrt(q.denominator)
    assert num * num == q.numerator and den * den == q.denominator, q
    return Fraction(num, den)


def eig2(p):
    """The two eigenvalues of a 2 x 2 matrix of fractions when they are rational: from the trace and the determinant."""
    tr, det = p[0][0] + p[1][1], p[0][0] * p[1][1] - p[0][1] * p[1][0]
    root = fsqrt(tr * tr - 4 * det)
    return sorted([(tr - root) / 2, (tr + root) / 2])


def norm_1(p):
    return max(sum(abs(x) for x in col) for col in zip(*p))


def norm_inf(p):
    return max(sum(abs(x) for x in row) for row in p)


def rho(m):
    return float(np.abs(np.linalg.eigvals(np.asarray(m, dtype=float))).max())


def behaviour(m, steps=600):
    """1: the powers tend to 0; 2: bounded without tending to 0; 3: not bounded (read on the first powers)."""
    m = np.asarray(m, dtype=float)
    power, norms = np.eye(len(m)), []
    for _ in range(steps):
        power = m @ power
        norms.append(np.linalg.norm(power, 2))
    if norms[-1] < 1e-9:
        return 1
    return 2 if max(norms) < 1e3 else 3


def as_pi(angle):
    """An angle that is a rational multiple of pi, written exactly: "pi/4", "-3*pi/4"."""
    q = Fraction(angle / math.pi).limit_denominator(24)
    assert abs(float(q) * math.pi - angle) < 1e-9, angle
    top = {1: "pi", -1: "-pi"}.get(q.numerator, f"{q.numerator}*pi")
    return top if q.denominator == 1 else f"{top}/{q.denominator}"


def toeplitz(w, n):
    """The (n + k - 1, n) matrix of y -> y * w (full mode): T_ij = w_(i-j), 0 outside the kernel."""
    k = len(w)
    return np.array([[w[i - j] if 0 <= i - j < k else 0 for j in range(n)] for i in range(n + k - 1)])


# CP5.1 (1): the polynomials P and Q, from the constant term up
A_1, B_1 = np.array([2, 3, -1]), np.array([1, 0, -2, 1])
AB_1 = np.convolve(A_1, B_1)                               # the coefficients of PQ
SLID_1 = np.convolve(A_1, B_1[::-1])                       # b slid along a without being reversed
SIGNS_1 = (-1) ** np.arange(len(AB_1))
ALT_1 = int(SIGNS_1 @ AB_1)
P_1, Q_1 = (int(np.polynomial.polynomial.polyval(-1, c)) for c in (A_1, B_1))
assert ALT_1 == P_1 * Q_1                                  # the value of PQ at X = -1
SUM_1 = int(AB_1.sum())                                    # PQ at X = 1, no alternation

# CP5.1 (2): the signal x and the kernel w
X_1, W_1 = np.array([3, -2, 4, 1, 0, -1]), np.array([3, 0, -2, 1])
N_1, K_1 = len(X_1), len(W_1)
CORR_1 = np.correlate(X_1, W_1, "valid")                   # (w ⋆ x)_i = Σ_u w_u x_(i+u)
assert CORR_1.tolist() == [sum(W_1[u] * X_1[i + u] for u in range(K_1)) for i in range(N_1 - K_1 + 1)]
VALID_1 = np.convolve(X_1, W_1, "valid")                   # the kernel reversed: a convolution
FULL_1 = np.convolve(X_1, W_1)
assert FULL_1.tolist() == [sum(X_1[i] * W_1[m - i] for i in range(N_1) if 0 <= m - i < K_1)
                           for m in range(N_1 + K_1 - 1)]
FULLCORR_1 = np.convolve(X_1, W_1[::-1])                   # a full correlation: the kernel not reversed
SAME_1 = np.convolve(X_1, W_1, "same")
START_1 = (min(N_1, K_1) - 1) // 2
assert SAME_1.tolist() == FULL_1[START_1:START_1 + N_1].tolist()
T3_1 = toeplitz(W_1, 3)
assert all((T3_1 @ y).tolist() == np.convolve(y, W_1).tolist() for y in np.eye(3, dtype=int))
T40_1 = toeplitz(W_1, 40)
NNZ_1 = int(np.count_nonzero(T40_1))
T6_1 = toeplitz(W_1, N_1)
V_1 = T6_1[K_1 - 1:N_1]                                    # valid mode: the rows of the complete windows
assert (V_1 @ X_1).tolist() == VALID_1.tolist()
V_ORDER_1 = np.zeros(N_1)
V_ORDER_1[1:1 + K_1] = W_1                                 # row 1 with the kernel in order


# CP5.2 (1): the windows of k = 9 weights on n = 472 samples
def positions(n, k, s=1, p=0, d=1):
    """The number of positions of a window of k weights (stride s, padding p, dilation d) on n cases."""
    return (n + 2 * p - d * (k - 1) - 1) // s + 1


def positions_counted(n, k, s=1, p=0, d=1):
    """The same number, by brute force: the windows whose last case stays in the padded signal."""
    return sum(1 for i in range(n + 2 * p) if s * i + d * (k - 1) <= n + 2 * p - 1)


N_2, K_2, S_2 = 472, 9, 4
POS_A_2 = positions(N_2, K_2, S_2)
POS_B_2 = positions(N_2, K_2, S_2, p=5, d=3)
assert POS_A_2 == positions_counted(N_2, K_2, S_2) and POS_B_2 == positions_counted(N_2, K_2, S_2, p=5, d=3)
CEIL_A_2 = -(-(N_2 - K_2) // S_2) + 1                      # rounded up
NODIL_B_2 = positions(N_2, K_2, S_2, p=5)
B_SLIPS_2 = {(N_2 + 5 - 3 * (K_2 - 1) - 1) // S_2 + 1,      # the padding counted once
             (N_2 + 10 - 3 * K_2) // S_2 + 1,              # the span d k
             (N_2 + 10 - 3 * (K_2 - 1) - 1) // S_2}        # the + 1 forgotten
B_UP_2 = {-(-(N_2 + 10 - 3 * (K_2 - 1) - 1) // S_2) + 1, POS_A_2}   # rounded up, or neither p nor d
NOPAD_B_2 = positions(N_2, K_2, S_2, d=3)
LAST_2 = S_2 * (POS_A_2 - 1) + K_2 - 1                     # the last case read by the last window
UNREAD_2 = N_2 - 1 - LAST_2
assert positions(LAST_2 + 1, K_2, S_2) == POS_A_2 and all(
    positions(n, K_2, S_2) == POS_A_2 for n in range(LAST_2 + 1, N_2 + 1))
UNREAD_LONG_2 = N_2 - 1 - (S_2 * (POS_A_2 - 1) + K_2)      # a window that ends at s i + k
UNREAD_SHORT_2 = N_2 - 1 - (S_2 * (POS_A_2 - 1) + K_2 - 2)
UNREAD_STEP_2 = N_2 - S_2 * POS_A_2                        # counted from the start of a window that does not exist
WINDOWS_2 = [k for k in range(1, N_2 + 1) if positions(N_2, k, S_2) == 110]       # the window lengths k
assert all(positions_counted(N_2, k, S_2) == 110 for k in WINDOWS_2)
NO_ONE_2 = [k for k in range(1, N_2 + 1) if (N_2 - k) // S_2 == 110]             # the + 1 forgotten
NO_MINUS_2 = [k for k in range(1, N_2 + 1) if (N_2 - k + 1) // S_2 + 1 == 110]   # the − 1 forgotten: n − k + 1
OUT_2 = -(-N_2 // S_2)                                     # TensorFlow and Keras: ceil(n / s)
TOTAL_2 = max((OUT_2 - 1) * S_2 + K_2 - N_2, 0)            # d = 1: (n_out − 1) s + d(k − 1) + 1 − n zeros
SAME_2 = [OUT_2, TOTAL_2 // 2, TOTAL_2 - TOTAL_2 // 2]
assert (N_2 + TOTAL_2 - (K_2 - 1) - 1) // S_2 + 1 == OUT_2 > (N_2 + TOTAL_2 - 1 - (K_2 - 1) - 1) // S_2 + 1

# CP5.2 (2): the transposed convolution of y by w with a stride 2
Y_2, WT_2, ST_2 = np.array([1, -2, 3, 2]), np.array([3, -2, 2]), 2
UP_2 = np.zeros((len(Y_2) - 1) * ST_2 + 1, dtype=int)
UP_2[::ST_2] = Y_2                                         # s − 1 zeros inserted between the values
TRANS_2 = np.convolve(UP_2, WT_2)                          # then the full convolution by w
STAMPS_2 = np.zeros(len(TRANS_2), dtype=int)
OVERWRITTEN_2 = np.zeros(len(TRANS_2), dtype=int)
for i, y in enumerate(Y_2):                                # each y_i prints y_i w from the case s i
    STAMPS_2[ST_2 * i:ST_2 * i + len(WT_2)] += y * WT_2
    OVERWRITTEN_2[ST_2 * i:ST_2 * i + len(WT_2)] = y * WT_2
C_2 = np.array([[WT_2[j - ST_2 * i] if 0 <= j - ST_2 * i < len(WT_2) else 0 for j in range(len(TRANS_2))]
                for i in range(len(Y_2))])                 # the sliding sum of stride 2 by w, on 9 cases
assert STAMPS_2.tolist() == TRANS_2.tolist() == (C_2.T @ Y_2).tolist()
REVERSED_2 = np.convolve(UP_2, WT_2[::-1])


def transposed_size(m, k, s, p=0, d=1, p_out=0):
    return (m - 1) * s - 2 * p + d * (k - 1) + 1 + p_out


SIZE_2 = transposed_size(50, 5, 3, p=2, p_out=1)
assert positions(SIZE_2, 5, 3, p=2) == 50                  # the sliding sum of the same settings gives back 50
SIZE_SLIPS_2 = {"no p_out": transposed_size(50, 5, 3, p=2), "p added": 49 * 3 + 2 * 2 + 4 + 1 + 1,
                "p once": transposed_size(50, 5, 3, p=1, p_out=1), "p ignored": transposed_size(50, 5, 3, p_out=1)}
KH_2, SH_2, MH_2 = 10, 3, 30                               # k = 10, s = 3, on 30 input values
STAMPS_COUNT_2 = [sum(1 for i in range(MH_2) if 0 <= j - SH_2 * i <= KH_2 - 1) for j in range((MH_2 - 1) * SH_2 + KH_2)]
COUNTS_2 = sorted(set(STAMPS_COUNT_2[KH_2:(MH_2 - 1) * SH_2]))   # the interior cases, far from both edges

# CP5.3 (1): the grid G and the kernel K, a cross-correlation in valid mode
G_3 = np.array([[3, 1, 0, 2, 4], [1, 4, 2, 0, 1], [2, 0, 3, 1, 2], [0, 2, 1, 3, 1]])
K_3 = np.array([[2, -2, 6], [1, -1, 3], [-1, 1, -3]])
assert np.linalg.matrix_rank(K_3) == 1
B_3 = K_3[0] / K_3[0, 0]                                   # b_0 = 1: the row 0 divided by K_00
A_3 = K_3[:, 0] / B_3[0]
assert (np.outer(A_3, B_3) == K_3).all()


def correlate2d(g, k):
    """Y_ij = Σ_u Σ_v K_uv G_(i+u, j+v), valid mode, no flip."""
    g, k = np.asarray(g), np.asarray(k)
    rows, cols = g.shape[0] - k.shape[0] + 1, g.shape[1] - k.shape[1] + 1
    return np.array([[np.sum(k * g[i:i + k.shape[0], j:j + k.shape[1]]) for j in range(cols)] for i in range(rows)])


Y_3 = correlate2d(G_3, K_3)
HORIZONTAL_3 = correlate2d(G_3, B_3[None, :])              # the horizontal pass by b, on every row of G
VERTICAL_3 = correlate2d(G_3, A_3[:, None])                # the vertical pass by a, on every column of G
assert (correlate2d(HORIZONTAL_3, A_3[:, None]) == Y_3).all() and (correlate2d(VERTICAL_3, B_3[None, :]) == Y_3).all()
CONV_3 = correlate2d(G_3, K_3[::-1, ::-1])                 # the 2D convolution: a half-turn of the kernel
TRANSPOSED_3 = correlate2d(G_3, K_3.T)
DIRECT_3 = Y_3.size * K_3.size                             # for the copy: one product per weight and per output
H_FIRST_3 = HORIZONTAL_3.size * len(B_3) + Y_3.size * len(A_3)
V_FIRST_3 = VERTICAL_3.size * len(A_3) + Y_3.size * len(B_3)
NARROW_3 = Y_3.size * len(B_3) + Y_3.size * len(A_3)       # the first pass on the rows or columns of the output only

# CP5.3 (2): the thermal camera, (5, 96, 144) -> 12 channels, kernels 3 x 5, bias, padding 1 in height and 2 in
# width, stride 2 along both axes
C_IN_3, C_OUT_3, H_3, W_3, KH_3, KW_3, PH_3, PW_3, S_3 = 5, 12, 96, 144, 3, 5, 1, 2, 2
PARAMS_3 = C_OUT_3 * (C_IN_3 * KH_3 * KW_3 + 1)


def out_shape(stride=S_3, ph=PH_3, pw=PW_3, kh=KH_3, kw=KW_3, c=C_OUT_3):
    """The shape (C, H, W) of the output, each axis counted with its own kernel size and padding."""
    return [c, positions(H_3, kh, stride, p=ph), positions(W_3, kw, stride, p=pw)]


SHAPE_3 = out_shape()
assert SHAPE_3[1:] == [positions_counted(H_3, KH_3, S_3, p=PH_3), positions_counted(W_3, KW_3, S_3, p=PW_3)]
SHAPE_SLIPS_3 = {"stride": out_shape(stride=1), "padding": out_shape(ph=0, pw=0), "channels": out_shape(c=C_IN_3),
                 "one side": [C_OUT_3, (H_3 + PH_3 - KH_3) // S_3 + 1, (W_3 + PW_3 - KW_3) // S_3 + 1],
                 "padding swapped": out_shape(ph=PW_3, pw=PH_3), "kernel swapped": out_shape(kh=KW_3, kw=KH_3),
                 "order": SHAPE_3[1:] + SHAPE_3[:1]}


def macs(rows, cols, c_out=C_OUT_3, c_in=C_IN_3):
    """One multiplication-addition per weight and per output position."""
    return rows * cols * c_out * c_in * KH_3 * KW_3


MACS_3 = macs(*SHAPE_3[1:])
NOSTRIDE_3 = macs(*SHAPE_SLIPS_3["stride"][1:])
NOPAD_3 = macs(*SHAPE_SLIPS_3["padding"][1:])
NO_CIN_3 = macs(*SHAPE_3[1:], c_in=1)
WITH_BIAS_3 = SHAPE_3[1] * SHAPE_3[2] * PARAMS_3
DEPTH_3, POINT_3 = C_IN_3 * (KH_3 * KW_3 + 1), C_OUT_3 * (C_IN_3 + 1)
SEP_3 = DEPTH_3 + POINT_3
NO_BIAS_3 = {DEPTH_3 - C_IN_3 + POINT_3, DEPTH_3 + POINT_3 - C_OUT_3, DEPTH_3 - C_IN_3 + POINT_3 - C_OUT_3}

# CP5.3 (3): the stack (k, s, d) of four sliding sums
STACK_3 = [(2, 1, 1), (4, 3, 1), (2, 1, 3), (3, 4, 1)]


def field(stack, dilation=True, own_stride=False):
    """r_l = r_(l-1) + d_l (k_l − 1) J_(l-1), J_l = J_(l-1) s_l (own_stride: J_l in place of J_(l-1))."""
    r, jump = 1, 1
    for k, s, d in stack:
        if own_stride:
            jump *= s
        r += (d if dilation else 1) * (k - 1) * jump
        if not own_stride:
            jump *= s
    return r


def read_cases(stack, output=0):
    """The cases of the original signal that the calculations of one output read, layer by layer, by brute force."""
    cases = {output}
    for k, s, d in reversed(stack):
        cases = {s * i + d * u for i in cases for u in range(k)}
    return cases


STRIDE_3 = math.prod(s for _, s, _ in STACK_3)
RF_3 = field(STACK_3)
assert max(read_cases(STACK_3)) - min(read_cases(STACK_3)) + 1 == RF_3 and min(read_cases(STACK_3, 1)) == STRIDE_3
KSUM_3 = sum(k for k, _, _ in STACK_3)                     # the sizes of the kernels added
SPANS_3 = sum(d * (k - 1) + 1 for k, _, d in STACK_3)      # the spans of the windows added
NOJUMP_3 = 1 + sum(d * (k - 1) for k, _, d in STACK_3)     # the strides of the previous layers forgotten
NOJUMP_NODIL_3 = 1 + sum(k - 1 for k, _, _ in STACK_3)     # the strides and the dilations forgotten

# CP5.4: five strain gauges on the five blades of a rotor, indices modulo 5; the largest INCREASE of z_1
X_4, H_4, EPS_4 = np.array([1, 3, -2, 0, 2]), np.array([1, -4, 2, 3, -2]), Fraction("0.2")
N_4 = len(X_4)
CIRC_4 = np.array([[H_4[(i - j) % N_4] for j in range(N_4)] for i in range(N_4)])
Z_4 = CIRC_4 @ X_4
assert Z_4.tolist() == [sum(X_4[i] * H_4[(m - i) % N_4] for i in range(N_4)) for m in range(N_4)]
FULL_4 = np.convolve(X_4, H_4)
assert Z_4.tolist() == [FULL_4[m] + (FULL_4[m + N_4] if m + N_4 < len(FULL_4) else 0) for m in range(N_4)]
UNFOLDED_4 = FULL_4[:N_4]                                  # the full convolution, nothing folded back
CIRC_CORR_4 = [sum(H_4[u] * X_4[(m + u) % N_4] for u in range(N_4)) for m in range(N_4)]   # h ⋆ x, made circular
PLUS_4 = [sum(X_4[i] * H_4[(m + i) % N_4] for i in range(N_4)) for m in range(N_4)]       # h_((m+i) mod n)
SHIFT_4 = np.array([[int(j == (i - 1) % N_4) for j in range(N_4)] for i in range(N_4)])  # (P x)_i = x_(i−1)
ZP2_4 = CIRC_4 @ (SHIFT_4 @ SHIFT_4 @ X_4)
assert ZP2_4.tolist() == (SHIFT_4 @ SHIFT_4 @ Z_4).tolist() and (CIRC_4 @ SHIFT_4 == SHIFT_4 @ CIRC_4).all()
BACK_4 = SHIFT_4.T @ SHIFT_4.T @ Z_4                       # shifted the other way
ONCE_4 = SHIFT_4 @ Z_4
ROW_4 = CIRC_4[1]                                          # z_1 = (row 1 of circ(h)) · x
DELTA_4 = [EPS_4 * int(np.sign(r)) for r in ROW_4]
WORST_INF_4 = EPS_4 * int(np.abs(ROW_4).sum())
VERTICES_4 = [(int(sum(r * e for r, e in zip(ROW_4, signs))), signs) for signs in product((-1, 1), repeat=N_4)]
assert max(VERTICES_4)[0] * EPS_4 == WORST_INF_4 and [EPS_4 * e for e in max(VERTICES_4)[1]] == DELTA_4
assert sum(v == max(VERTICES_4)[0] for v, _ in VERTICES_4) == 1   # a unique vertex: no weight is zero
WORST_TWO_4 = float(EPS_4) * float(np.linalg.norm(ROW_4))
H_SIGNS_4 = [EPS_4 * int(np.sign(h)) for h in H_4]
ROW0_SIGNS_4 = [EPS_4 * int(np.sign(r)) for r in CIRC_4[0]]
assert H_SIGNS_4 == ROW0_SIGNS_4                           # two mistakes, one value: one message
SCALED_4 = [EPS_4 * int(r) for r in ROW_4]                 # ε r: out of the cube
L2_4 = float(EPS_4) * float(np.linalg.norm(ROW_4))
MAX_H_4 = float(EPS_4 * int(np.abs(H_4).max()))           # the largest weight only
SIGNED_SUM_4 = float(EPS_4 * int(H_4.sum()))               # the weights with their signs

# CP5.5: a drug between blood and tissues, x_(t+1) = A x_t + B u_t, y_t = C x_t
A_5, B_5, C_5 = fmat([["0.5", "0.1"], ["0.3", "0.7"]]), [1, 0], [0, 1]
X0_5, U_5 = [Fraction(20), Fraction(4)], [6, 0, 2]


def run_5(a=A_5, inputs=U_5, steps=3):
    """The states x_0, ..., x_steps (an input missing from the list is 0)."""
    xs = [X0_5]
    for t in range(steps):
        u = inputs[t] if t < len(inputs) else 0
        xs.append([v + b * u for v, b in zip(fmatvec(a, xs[-1]), B_5)])
    return xs


XS_5 = run_5()
XS_T_5 = run_5(ftranspose(A_5))                            # A transposed
XS_NO_U0_5 = run_5(inputs=[0] + U_5[1:])
XS_LATE_5 = run_5(inputs=U_5[1:])                          # u_(t+1) used for x_(t+1): one step late
LAM_5 = eig2(A_5)                                          # 2/5 and 4/5
VEC_5 = {lam: [1, (lam - A_5[0][0]) / A_5[0][1]] for lam in LAM_5}   # (1, v): the first row of (A − λI) v = 0
assert all(fmatvec(A_5, v) == [lam * c for c in v] for lam, v in VEC_5.items())
assert np.allclose(sorted(np.linalg.eigvals(np.array(floats(A_5))).real), floats(LAM_5))
DIAG_5 = sorted([A_5[0][0], A_5[1][1]])                    # the diagonal coefficients
NEG_5 = sorted(-lam for lam in LAM_5)                      # the roots of λ² + tr λ + det
COEF_B_5 = np.linalg.solve(np.array([floats(VEC_5[lam]) for lam in LAM_5]).T, floats(B_5))   # B on the eigenvectors
H_5 = [sum(c * v for c, v in zip(C_5, fmatvec(fpow(A_5, k), B_5))) for k in range(20)]
assert np.allclose(floats(H_5), [sum(b * float(lam) ** k * float(VEC_5[lam][1]) for b, lam in zip(COEF_B_5, LAM_5))
                                 for k in range(20)])      # h_k = Σ (coefficient of B) λ^k (C v)
H12_5 = [fpow(A_5, k)[0][1] for k in range(20)]           # the coefficient (1, 2) of A^k
FIRST_5 = [fmatvec(fpow(A_5, k), B_5)[0] for k in range(20)]          # C = (1 0): the other coordinate
GEOM_5 = LAM_5[1] ** 15 - LAM_5[0] ** 15                   # B taken with coefficients 1 on the eigenvectors
FORCED_5 = sum(H_5[2 - k] * U_5[k] for k in range(3))      # y_3 = (h * u)_2 + C A^3 x_0
FREE_Y3_5 = sum(c * v for c, v in zip(C_5, fmatvec(fpow(A_5, 3), X0_5)))
assert FORCED_5 + FREE_Y3_5 == XS_5[3][1]
CARRIED_5 = H_5[3] * U_5[0]                                # u_0 carried by A^3 instead of A^2
I_MINUS_5 = [[int(i == j) - A_5[i][j] for j in range(2)] for i in range(2)]
EQ_5 = fmatvec(finv2(I_MINUS_5), [4 * b for b in B_5])
assert fmatvec(A_5, EQ_5) == [x - 4 * b for x, b in zip(EQ_5, B_5)]
EQ_T_5 = fmatvec(finv2(ftranspose(I_MINUS_5)), [4 * b for b in B_5])
COLUMNS_5 = [sum(col) for col in zip(*A_5)]
assert len(set(COLUMNS_5)) == 1                            # (1, 1) A = c (1, 1): the total is multiplied by c
FACTOR_5 = COLUMNS_5[0]
TOTAL_EQ_5 = 4 / (1 - FACTOR_5)                            # the total at equilibrium

# CP5.6: M, of trace 3/2 and determinant 3/4
M_6 = np.array([[0, -1], [0.75, 1.5]])
MF_6 = fmat([["0", "-1"], ["0.75", "1.5"]])
EIG_6 = np.linalg.eigvals(M_6)
LAM_6 = complex(EIG_6[np.argmax(EIG_6.imag)])
RHO_6 = float(np.abs(EIG_6).max())
assert abs(RHO_6 ** 2 - np.linalg.det(M_6)) < 1e-12        # two conjugate eigenvalues: |λ|² = λ λ̄ = det
THETA_6 = float(np.angle(LAM_6))
DET_6 = MF_6[0][0] * MF_6[1][1] - MF_6[0][1] * MF_6[1][0]
TR_6 = MF_6[0][0] + MF_6[1][1]
assert abs(LAM_6.real - float(TR_6 / 2)) < 1e-12
M2_6, M3_6, M6_6 = fpow(MF_6, 2), fpow(MF_6, 3), fpow(MF_6, 6)
assert M6_6 == [[-DET_6 ** 3, 0], [0, -DET_6 ** 3]]        # six steps of π/6: a half-turn, and a factor |λ|⁶
assert fpow(MF_6, 12) == [[DET_6 ** 6, 0], [0, DET_6 ** 6]]   # ((2/√3) M)^12 = (4/3)^6 M^12 = I: bounded powers
CUBED_6 = [[x ** 3 for x in row] for row in MF_6]          # each coefficient cubed
N1_6, NINF_6, N2_6 = (float(np.linalg.norm(M_6, o)) for o in (1, np.inf, 2))
assert N1_6 == float(norm_1(MF_6)) and NINF_6 == float(norm_inf(MF_6))
SIGNED_6 = [max(float(sum(c)) for c in zip(*MF_6)), max(float(sum(r)) for r in MF_6)]   # the signs kept
SMALLEST_6 = [min(float(sum(abs(x) for x in c)) for c in zip(*MF_6)), min(float(sum(abs(x) for x in r)) for r in MF_6)]
SV_6 = np.linalg.svd(M_6, compute_uv=False)
assert abs(SV_6[0] - N2_6) < 1e-12
GRAM_MAX_6 = float(np.linalg.eigvalsh(M_6.T @ M_6)[-1])
FROB_6 = float(np.linalg.norm(M_6))
SCALE_6 = 2 / math.sqrt(3)
CODES_6 = [behaviour(M_6), behaviour(SCALE_6 * M_6)]

# CP5.7 (1): f(x, y) = (0.5 x + y², x − 0.5 y) from p_0 = (2, 1)
HALF_7 = Fraction(1, 2)


def f_7(p):
    x, y = p
    return [HALF_7 * x + y * y, x - HALF_7 * y]


def jac_7(p):
    """One row per output: [[∂f1/∂x, ∂f1/∂y], [∂f2/∂x, ∂f2/∂y]]."""
    _, y = p
    return [[HALF_7, 2 * y], [Fraction(1), -HALF_7]]


PS_7 = [[Fraction(2), Fraction(1)]]
for _ in range(2):
    PS_7.append(f_7(PS_7[-1]))
J0_7, J1_7, J2_7 = (jac_7(p) for p in PS_7)
D2_7 = fmatmul(J1_7, J0_7)                                 # the jacobian of the last step on the left
STEP_7 = 1e-6
P0_7 = np.array(floats(PS_7[0]))
FD_7 = np.column_stack([(np.array(f_7(f_7(P0_7 + e))) - np.array(f_7(f_7(P0_7 - e)))) / (2 * STEP_7)
                        for e in STEP_7 * np.eye(2)])      # column j: the derivative along the input j
assert np.allclose(FD_7, floats(D2_7), atol=1e-6)          # finite differences on f∘f
NORMS_7 = [float(norm_inf(J1_7) * norm_inf(J0_7)), float(norm_inf(D2_7))]
SLIPS_C_7 = {"columns": [float(norm_1(J1_7) * norm_1(J0_7)), float(norm_1(D2_7))],
             "order": [float(norm_inf(J1_7) * norm_inf(J0_7)), float(norm_inf(fmatmul(J0_7, J1_7)))]}
assert SLIPS_C_7["columns"] == SLIPS_C_7["order"]          # two mistakes, one value: one message

# CP5.7 (2): the tank x_(t+1) = x_t − β √x_t + 1, x_0 = 36, β = 2
X0_7, BETA_7, DBETA_7 = 36, 2, Fraction("0.1")


def tank(beta, steps=3):
    xs = [float(X0_7)]
    for _ in range(steps):
        xs.append(xs[-1] - beta * math.sqrt(xs[-1]) + 1)
    return xs


XT_7 = [int(x) for x in tank(BETA_7)]
ROOTS_7 = [math.isqrt(x) for x in XT_7]
assert all(r * r == x for r, x in zip(ROOTS_7, XT_7))      # 36, 25, 16, 9: exact square roots
JT_7 = [1 - Fraction(BETA_7, 2 * r) for r in ROOTS_7[:3]]  # ∂f/∂x = 1 − β/(2√x)
BT_7 = [Fraction(-r) for r in ROOTS_7[:3]]                 # ∂f/∂β = −√x
TERMS_7 = [math.prod(JT_7[k + 1:3], start=Fraction(1)) * BT_7[k] for k in range(3)]
S3_7 = sum(TERMS_7)
s_t = Fraction(0)
for J_t, b_t in zip(JT_7, BT_7):
    s_t = J_t * s_t + b_t                                  # s_(t+1) = J_t s_t + b_t, s_0 = 0
assert s_t == S3_7
assert abs((tank(BETA_7 + 1e-6)[3] - tank(BETA_7 - 1e-6)[3]) / 2e-6 - float(S3_7)) < 1e-6
OWN_7 = [math.prod(JT_7[k:3], start=Fraction(1)) * BT_7[k] for k in range(3)]   # its own jacobian included
DX3_7 = DBETA_7 * S3_7
EXACT_7 = tank(BETA_7 + float(DBETA_7))[3] - tank(BETA_7)[3]

# CP5.10: the recursive filter, A = [[0.6, −0.5], [0.4, 0.6]], B = (1, 0), C = (0 1), x_0 = 0
A_10, B_10, C_10 = fmat([["0.6", "-0.5"], ["0.4", "0.6"]]), [1, 0], [0, 1]


def impulse(a, b, c, n):
    """h_k = C A^k B for k = 0, ..., n − 1, one product per step."""
    out, v = [], [Fraction(x) for x in b]
    for _ in range(n):
        out.append(sum(ci * vi for ci, vi in zip(c, v)))
        v = fmatvec(a, v)
    return out


H_10 = impulse(A_10, B_10, C_10, 80)
H12_10 = [fpow(A_10, k)[0][1] for k in range(5)]
FIRST_10 = impulse(A_10, B_10, [1, 0], 5)                  # C = (1 0): the other coordinate
U_10 = [4, -2, 0, 3]
XS_10 = [[Fraction(0), Fraction(0)]]
for t in range(7):
    u = U_10[t] if t < len(U_10) else 0
    XS_10.append([v + b * u for v, b in zip(fmatvec(A_10, XS_10[-1]), B_10)])
OUT_10 = [sum(c * v for c, v in zip(C_10, x)) for x in XS_10]           # y_t = C x_t
CONV_10 = np.convolve(floats(H_10[:8]), U_10)              # (h * u)_t
assert np.allclose(floats(OUT_10[1:7]), CONV_10[:6])       # y_(t+1) = (h * u)_t
RHO_10 = rho(A_10)
DET_10 = A_10[0][0] * A_10[1][1] - A_10[0][1] * A_10[1][0]
TR_10 = A_10[0][0] + A_10[1][1]
assert TR_10 ** 2 < 4 * DET_10 and abs(RHO_10 ** 2 - float(DET_10)) < 1e-12
GRAM_10 = fmatmul(ftranspose(A_10), A_10)
NORM2_10 = fsqrt(max(eig2(GRAM_10)))                       # the largest singular value, exact
NORMS_10 = [float(norm_1(A_10)), float(norm_inf(A_10)), float(NORM2_10)]
assert np.allclose(NORMS_10, [np.linalg.norm(np.array(floats(A_10)), o) for o in (1, np.inf, 2)])
SIGNED_10 = [max(float(sum(c)) for c in zip(*A_10)), max(float(sum(r)) for r in A_10)]
SMALLEST_10 = [min(float(norm_1([[x] for x in c])) for c in zip(*A_10)), min(float(norm_inf([r])) for r in A_10)]
assert SIGNED_10 == SMALLEST_10                            # two mistakes, one value: one message
FROB_10 = float(np.linalg.norm(np.array(floats(A_10))))
TARGET_10 = Fraction(1, 100)
K_10 = next(K for K in range(1, 500) if NORM2_10 ** K / (1 - NORM2_10) <= TARGET_10)
assert sum(abs(h) for h in H_10[K_10:]) <= TARGET_10       # the true tail is under the bound
NO_FACTOR_10 = next(K for K in range(1, 500) if NORM2_10 ** K <= TARGET_10)
WITH_RHO_10 = next(K for K in range(1, 500) if RHO_10 ** K / (1 - RHO_10) <= 0.01)
assert NO_FACTOR_10 == WITH_RHO_10                         # two mistakes, one value: one message
RHO_ONLY_10 = next(K for K in range(1, 500) if RHO_10 ** K <= 0.01)
G6_10 = H_10[:6]
WORST_10 = sum(abs(h) for h in G6_10)
assert max(abs(sum(g * u for g, u in zip(G6_10, signs))) for signs in product((-1, 1), repeat=6)) == WORST_10
WORST_SLIPS_10 = {"signs": sum(G6_10), "four": sum(abs(h) for h in H_10[:4]), "five": sum(abs(h) for h in H_10[:5]),
                  "seven": sum(abs(h) for h in H_10[:7])}
I_MINUS_10 = [[int(i == j) - A_10[i][j] for j in range(2)] for i in range(2)]
LIMIT_10 = sum(c * v for c, v in zip(C_10, fmatvec(finv2(I_MINUS_10), B_10)))
assert abs(float(sum(H_10)) - float(LIMIT_10)) < 1e-8      # also the sum of the impulse response
LIMIT_T_10 = sum(c * v for c, v in zip(C_10, fmatvec(finv2(ftranspose(I_MINUS_10)), B_10)))
PARTIAL_10 = sum(H_10[:5])'''

PAPER = [
    Paper("CP5.1", "Convolution de deux suites, corrélation croisée et matrice de Toeplitz", [
        ("a", "a list of 6 integers", "ints(AB_1)",
         'mistakes={"la convolution retourne l\'un des deux facteurs : dans (a * b)ₘ = Σ aᵢ bₘ₋ᵢ, la somme des deux '
         'indices vaut m": ints(SLID_1), "la liste va du terme constant au terme de plus haut degré": '
         'ints(AB_1[::-1])}'),
        ("b", "an integer", "ALT_1",
         'mistakes={"une somme alternée change le signe d\'un terme sur deux : relis sa définition": SUM_1, '
         '"vérifie le signe du premier terme, (−1)⁰ = 1 ; et la valeur d\'un produit de polynômes est le produit de '
         'leurs valeurs, pas leur somme": {-ALT_1, P_1 + Q_1}}'),
        ("c", "a list of 3 integers", "ints(CORR_1)",
         'mistakes={"la corrélation croisée ne retourne pas le noyau : la fenêtre i calcule Σᵤ wᵤ x_(i+u)": '
         'ints(VALID_1)}'),
        ("d", "a list of 9 integers", "ints(FULL_1)",
         'mistakes={"la convolution retourne le noyau : (x * w)ₘ = Σᵢ xᵢ w_(m−i)": ints(FULLCORR_1), '
         '"le mode plein garde toutes les positions où le noyau touche le signal, pas seulement les fenêtres '
         'complètes": ints(VALID_1)}'),
        ("e", "a list of 6 integers", "ints(SAME_1)",
         'mistakes={"le mode \\"same\\" de NumPy ne commence pas au début de la convolution pleine : relis la règle '
         'de son indice de départ": ints(FULL_1[:N_1]), "pour un noyau de longueur paire, NumPy enlève une valeur de '
         'moins au début qu\'à la fin": ints(FULL_1[START_1 + 1:START_1 + 1 + N_1])}'),
        ("f", "a 6 × 3 matrix, as a list of rows", "ints(T3_1)",
         'mistakes={"Tᵢⱼ = w_(i−j) : dans une colonne, l\'indice du noyau croît avec l\'indice de ligne": '
         'ints(toeplitz(W_1[::-1], 3)), "la matrice a une ligne par valeur de la sortie et une colonne par valeur '
         'de l\'entrée": ints(T3_1.T)}'),
        ("g", "an integer", "NNZ_1",
         'mistakes={"un coefficient nul du noyau ne donne aucun coefficient non nul dans la matrice": K_1 * 40, '
         '"la question compte les coefficients non nuls, pas tous les coefficients de la matrice": int(T40_1.size)}'),
        ("h", "a list of 6 integers", "ints(V_1[1])",
         'mistakes={"dans une ligne, Tᵢⱼ = w_(i−j) : quand j croît, l\'indice du noyau décroît": ints(V_ORDER_1), '
         '"V ne garde que les lignes des fenêtres complètes : sa ligne 1 n\'est pas la ligne 1 de la matrice '
         'pleine": ints(T6_1[1]), "les lignes sont numérotées à partir de 0 : la ligne 1 est la deuxième": '
         'ints(V_1[0])}'),
    ]),
    Paper("CP5.2", "Positions d'une fenêtre, pas, dilatation, et la convolution transposée d'un signal", [
        ("a", "an integer", "POS_A_2",
         'mistakes={"le nombre de positions est une partie entière plus 1 : la première position compte": '
         'POS_A_2 - 1, "la partie entière est inférieure : une fenêtre qui dépasse du signal n\'est pas une '
         'position": CEIL_A_2}'),
        ("b", "an integer", "POS_B_2",
         'mistakes={"avec une dilatation d, la fenêtre s\'étend sur d(k − 1) + 1 cases": NODIL_B_2, '
         '"vérifie chaque terme de la formule : le padding est ajouté des deux côtés, l\'étendue d\'une fenêtre '
         'dilatée est d(k − 1) + 1, et le nombre est la partie entière plus 1": B_SLIPS_2, '
         '"la partie entière est inférieure, et la formule tient compte du padding et de la dilatation de la '
         'question": B_UP_2, "le padding p ajoute p zéros de chaque côté du signal avant de compter les positions": '
         'NOPAD_B_2}'),
        ("c", "an integer", "UNREAD_2",
         'mistakes={"la fenêtre numéro i lit les cases si à si + k − 1 : où finit la dernière ?": UNREAD_LONG_2, '
         '"une fenêtre lit k cases, sa première case comprise": UNREAD_SHORT_2, "compte à partir de la dernière '
         'case lue par la dernière fenêtre, pas à partir du début d\'une fenêtre suivante, qui n\'existe pas": '
         'UNREAD_STEP_2}'),
        ("d", "the window lengths k, as a list of integers", "WINDOWS_2",
         'ordered=False, mistakes={"le nombre de positions est la partie entière plus 1": NO_ONE_2, '
         '"une position existe quand la dernière case de sa fenêtre, si + k − 1, reste dans le signal : vérifie le '
         '− 1 de la formule": NO_MINUS_2, "la question demande la liste de toutes les longueurs, pas seulement les '
         'deux bornes": [WINDOWS_2[0], WINDOWS_2[-1]], "la partie entière confond plusieurs longueurs : donne-les '
         'toutes": [WINDOWS_2[0]], "plusieurs longueurs donnent ce nombre de positions : la question les demande '
         'toutes": [WINDOWS_2[-1]]}'),
        ("e", "a list of 3 integers", "SAME_2",
         'mistakes={"TensorFlow et Keras mettent le zéro en trop à la fin": [OUT_2, SAME_2[2], SAME_2[1]], '
         '"avec un pas, le padding « même taille » ne vaut pas k − 1 zéros : il en faut juste assez pour que la '
         'dernière fenêtre tienne": [OUT_2, (K_2 - 1) // 2, (K_2 - 1) // 2], "un nombre de zéros est entier : '
         'quand le total est impair, un côté en reçoit un de plus": [OUT_2, TOTAL_2 / 2, TOTAL_2 / 2]}'),
        ("f", "a list of 9 integers", "ints(TRANS_2)",
         'mistakes={"chaque entrée yᵢ dépose le tampon yᵢ w, le noyau dans l\'ordre, à partir de la case s·i": '
         'ints(REVERSED_2), "là où deux tampons se recouvrent, leurs valeurs s\'additionnent": ints(OVERWRITTEN_2)}'),
        ("g", "an integer", "SIZE_2",
         'mistakes={"le padding de sortie ajoute p_out valeurs à la fin": SIZE_SLIPS_2["no p_out"], '
         '"dans une convolution transposée, le padding p retire des valeurs au lieu d\'en ajouter": '
         'SIZE_SLIPS_2["p added"], "le padding p retire p valeurs à chaque bout": SIZE_SLIPS_2["p once"], '
         '"le padding change aussi la taille d\'une convolution transposée": SIZE_SLIPS_2["p ignored"]}'),
        ("h", "the different values, as a list of integers", "COUNTS_2",
         'ordered=False, mistakes={"quand s ne divise pas k, les cases intérieures ne reçoivent pas toutes le même '
         'nombre de tampons : donne toutes les valeurs": [COUNTS_2[0]], "les cases intérieures ne reçoivent pas '
         'toutes le même nombre de tampons quand s ne divise pas k : donne chacune des valeurs": [COUNTS_2[-1]]}'),
    ]),
    Paper("CP5.3", "Une grille filtrée par un noyau séparable : paramètres, coût et champ récepteur", [
        ("a", "[a, b], a list of 2 lists", "[ints(A_3), ints(B_3)]",
         'mistakes={"K_(u,v) = a_u b_v : a donne les lignes de K, b ses colonnes": [ints(B_3), ints(A_3)], '
         '"la normalisation demandée porte sur b : b₀ = 1": floats([A_3 / A_3[0], B_3 * A_3[0]])}'),
        ("b", "a 2 × 3 matrix, as a list of rows", "ints(Y_3)",
         'mistakes={"une corrélation croisée ne retourne pas le noyau : Y_(i,j) = Σ K_(u,v) G_(i+u, j+v)": '
         'ints(CONV_3), "u est l\'indice de ligne : K_(u,v) multiplie la case située u lignes plus bas et v '
         'colonnes plus à droite": ints(TRANSPOSED_3)}'),
        ("c", "a list of 2 integers", "[H_FIRST_3, V_FIRST_3]",
         'mistakes={"vérifie l\'ordre de ta liste : d\'abord le calcul qui commence par la passe horizontale": '
         '[V_FIRST_3, H_FIRST_3], "la première passe doit fournir à la seconde toutes les valeurs qu\'elle lit, pas '
         'seulement celles des lignes ou des colonnes de la sortie": [NARROW_3, NARROW_3], "quand la passe verticale '
         'vient en premier, elle doit fournir toutes les colonnes que lit la passe horizontale": '
         '[H_FIRST_3, NARROW_3], "quand la passe horizontale vient en premier, elle doit fournir toutes les lignes '
         'que lit la passe verticale": [NARROW_3, V_FIRST_3], "compte les valeurs que calcule chaque passe, dans '
         'chacun des deux ordres : les deux calculs ne coûtent pas autant": [DIRECT_3, DIRECT_3]}'),
        ("d", "a list of 3 integers", "SHAPE_3",
         'mistakes={"avec un pas, la sortie a moins de lignes et de colonnes : compte ses positions": '
         'SHAPE_SLIPS_3["stride"], "le padding (1 en hauteur, 2 en largeur) s\'ajoute de chaque côté avant de compter '
         'les positions": SHAPE_SLIPS_3["padding"], "la sortie a un canal par filtre": SHAPE_SLIPS_3["channels"], '
         '"le padding s\'ajoute des deux côtés de chaque axe : en haut et en bas, à gauche et à droite": '
         'SHAPE_SLIPS_3["one side"], "le padding vaut 1 en hauteur (le long des lignes) et 2 en largeur (le long des '
         'colonnes)": SHAPE_SLIPS_3["padding swapped"], "un noyau 3 × 5 a 3 lignes et 5 colonnes : 3 en hauteur, 5 en '
         'largeur": SHAPE_SLIPS_3["kernel swapped"], "la forme demandée est (C, H, W) : les canaux d\'abord": '
         'SHAPE_SLIPS_3["order"]}'),
        ("e", "an integer", "PARAMS_3",
         'mistakes={"chaque canal de sortie a un biais": PARAMS_3 - C_OUT_3, '
         '"un biais par canal de sortie, pas par canal d\'entrée": PARAMS_3 - C_OUT_3 + C_IN_3}'),
        ("f", "an integer", "MACS_3",
         'mistakes={"avec un pas, la sortie a moins de lignes et de colonnes : compte ses positions": NOSTRIDE_3, '
         '"le padding s\'ajoute de chaque côté avant de compter les positions de sortie": NOPAD_3, "chaque noyau de '
         'sortie a C_in × k_h × k_w poids, un par canal d\'entrée": NO_CIN_3, "un biais s\'ajoute sans '
         'multiplication : le coût compte une multiplication-addition par poids": WITH_BIAS_3}'),
        ("g", "an integer", "SEP_3",
         'mistakes={"chacune des deux convolutions a un biais par canal de sortie": NO_BIAS_3}'),
        ("h", "a list of 2 integers", "[RF_3, STRIDE_3]",
         'mistakes={"un étage dilaté ajoute d(k − 1) fois le produit des pas précédents, pas k − 1 fois": '
         '[field(STACK_3, dilation=False), STRIDE_3], "chaque étage ajoute d(k − 1) cases de son entrée, et une case '
         'de son entrée vaut le produit des pas précédents en cases du signal d\'origine": [NOJUMP_NODIL_3, STRIDE_3], '
         '"une case de l\'entrée d\'un étage vaut le produit des pas précédents en cases du signal d\'origine": '
         '[NOJUMP_3, STRIDE_3], "additionner les tailles des noyaux oublie les pas : les pas des étages précédents '
         'multiplient ce qu\'ajoute chaque étage": [KSUM_3, STRIDE_3], "additionner les étendues des fenêtres oublie '
         'les pas, et chaque étage n\'ajoute que d(k − 1) cases de son entrée": [SPANS_3, STRIDE_3], "le pas total '
         'est le produit des pas, pas leur somme": [RF_3, sum(s for _, s, _ in STACK_3)], "un pas ne change pas la '
         'contribution de son propre étage : seuls les pas des étages précédents la multiplient": '
         '[field(STACK_3, own_stride=True), STRIDE_3]}'),
    ]),
    Paper("CP5.4", "Équivariance, matrice circulante et le pire cas d'une perturbation bornée", [
        ("a", "a list of 5 integers", "ints(Z_4)",
         'mistakes={"dans une convolution circulaire, les indices se lisent modulo n : les termes qui dépassent '
         'n − 1 reviennent au début": ints(UNFOLDED_4), "la convolution circulaire retourne aussi le noyau : '
         '(x ⊛ h)ₘ = Σᵢ xᵢ h_((m−i) mod n)": ints(CIRC_CORR_4), "l\'indice de h est (m − i) mod n, pas (m + i) mod n '
         ': la convolution retourne le noyau": ints(PLUS_4)}'),
        ("b", "a list of 5 integers", "ints(CIRC_4[0])",
         'mistakes={"h est la première colonne de circ(h) ; la question demande la première ligne": ints(H_4), '
         '"le coefficient (0, j) vaut h_((0−j) mod n) : le retourné circulaire n\'est pas le simple renversement": '
         'ints(H_4[::-1])}'),
        ("c", "a list of 5 integers", "ints(ZP2_4)",
         'mistakes={"décaler l\'entrée d\'une convolution circulaire laisse-t-il sa sortie à sa place ?": ints(Z_4), '
         '"(Px)ᵢ = x_((i−1) mod n) : P pousse les valeurs vers les indices croissants": ints(BACK_4), '
         '"P² décale deux fois": ints(ONCE_4)}'),
        ("d", "a list of 5 numbers", "floats(DELTA_4)",
         'decimals=2, mistakes={"le changement de z₁ est le produit scalaire de δ avec la ligne 1 de circ(h) (les '
         'lignes sont numérotées à partir de 0), pas avec h": floats(H_SIGNS_4), "on cherche le changement le plus '
         'grand vers le haut : z₁ doit augmenter": floats([-d for d in DELTA_4]), "chaque |δᵢ| doit rester au plus '
         '0,2 : ce δ sort des tolérances": floats(SCALED_4)}'),
        ("e", "a number", "float(WORST_INF_4)",
         'decimals=4, mistakes={"chaque δᵢ se choisit indépendamment des autres : tous les poids comptent, pas '
         'seulement le plus grand": MAX_H_4, "aucun terme ne doit en compenser un autre : le signe de chaque δᵢ se '
         'choisit séparément": SIGNED_SUM_4, "ici chaque coordonnée de δ est bornée séparément (|δᵢ| ≤ 0,2) : ce '
         'n\'est pas la boule L2": {L2_4, round(L2_4, 3)}, "une augmentation est positive : δ = 0 donne déjà un '
         'changement nul": -float(WORST_INF_4)}'),
        ("f", "a number (3 decimals)", "WORST_TWO_4",
         'decimals=3, mistakes={"la contrainte porte cette fois sur ‖δ‖₂ : δ ne peut plus prendre ±0,2 sur chaque '
         'coordonnée à la fois": float(WORST_INF_4), "la norme L2 est la racine carrée de la somme des carrés": '
         'float(EPS_4) * float(ROW_4 @ ROW_4), "sur une boule L2, tous les poids comptent, pas seulement le plus '
         'grand": float(EPS_4) * float(np.abs(ROW_4).max())}'),
    ]),
    Paper("CP5.5", "Une récurrence avec entrée : solution et réponse impulsionnelle", [
        ("a", "a list of 2 numbers", "floats(XS_5[2])",
         'decimals=4, mistakes={"en convention colonne, la ligne i de A donne la coordonnée i de A xₜ": '
         'floats(XS_T_5[2]), "la perfusion u₀ entre dans x₁ = A x₀ + B u₀": floats(XS_NO_U0_5[2]), "l\'entrée uₜ '
         'sert à calculer xₜ₊₁, pas xₜ": floats(XS_LATE_5[2]), "la question demande x₂ : deux pas depuis '
         'x₀": floats(XS_5[1])}'),
        ("b", "a list of 2 numbers", "floats(XS_5[3])",
         'decimals=4, mistakes={"chaque pas ajoute B uₜ, pour chaque entrée reçue": floats(fmatvec(A_5, XS_5[2])), '
         '"en convention colonne, la ligne i de A donne la coordonnée i de A xₜ": floats(XS_T_5[3]), '
         '"l\'entrée uₜ sert à calculer xₜ₊₁, pas xₜ": floats(XS_LATE_5[3])}'),
        ("c", "a list of 2 numbers, in increasing order", "floats(LAM_5)",
         'decimals=4, mistakes={"les valeurs propres d\'une matrice non triangulaire ne sont pas ses coefficients '
         'diagonaux : résous λ² − tr(A) λ + det(A) = 0": floats(DIAG_5), "vérifie les signes du polynôme '
         'caractéristique λ² − tr(A) λ + det(A)": floats(NEG_5), "la question demande l\'ordre croissant": '
         'floats(LAM_5[::-1])}'),
        ("d", "a list of 4 numbers", "floats(H_5[:4])",
         'decimals=4, mistakes={"la réponse impulsionnelle commence à h₀ = C B": floats(H_5[1:5]), '
         '"dans hₖ = C Aᵏ B, B choisit une colonne de Aᵏ et C une ligne : vérifie lesquelles": floats(H12_5[:4]), '
         '"hₖ est une sortie : relis quelle coordonnée de l\'état C lit": floats(FIRST_5[:4])}'),
        ("e", "a number (4 decimals)", "float(H_5[15])",
         'decimals=4, mistakes={"vérifie l\'indice : h₁₅ = C A¹⁵ B": {float(H_5[14]), float(H_5[16])}, '
         '"écris B sur les vecteurs propres de A : ses coefficients sur ces vecteurs ne valent pas 1": '
         'float(GEOM_5)}'),
        ("f", "a number", "float(FORCED_5)",
         'decimals=4, mistakes={"la part due à la perfusion est la réponse forcée ; la réponse libre vient de x₀": '
         'float(FREE_Y3_5), "y₃ contient aussi la réponse libre : la question n\'en demande qu\'une part": '
         'float(XS_5[3][1]), "l\'entrée uₖ est portée par A^(t−1−k) jusqu\'à xₜ": float(CARRIED_5)}'),
        ("g", "a list of 2 numbers", "floats(EQ_5)",
         'decimals=4, mistakes={"l\'équilibre vérifie x⋆ = A x⋆ + B u : la matrice du système est I − A, pas sa '
         'transposée": floats(EQ_T_5), "ta réponse donne-t-elle à chaque compartiment la quantité totale ? Résous '
         '(I − A) x⋆ = B u coordonnée par coordonnée": floats([TOTAL_EQ_5, TOTAL_EQ_5])}'),
        ("h", "a number", "float(FACTOR_5)",
         'decimals=4, mistakes={"ce facteur vaut pour tout xₜ : lis-le sur les sommes des colonnes de A": '
         'float(min(LAM_5)), "la trace est la somme des valeurs propres, pas le facteur appliqué à la quantité '
         'totale": float(A_5[0][0] + A_5[1][1]), "le facteur multiplie la quantité qui reste : la part éliminée '
         'n\'en est que le complément": float(1 - FACTOR_5)}'),
    ]),
    Paper("CP5.6", "Valeurs propres complexes, rayon spectral, normes et croissance transitoire", [
        ("a", COMPLEX + " (4 decimals)", "[LAM_6.real, LAM_6.imag]",
         'decimals=4, mistakes={"la question demande la valeur propre de partie imaginaire positive": '
         '[LAM_6.real, -LAM_6.imag], "λ = (tr ± √Δ)/2 : vérifie la division par 2": [2 * LAM_6.real, '
         '2 * LAM_6.imag]}'),
        ("b", "a number (4 decimals)", "RHO_6",
         'decimals=4, mistakes={"le module de a + ib est √(a² + b²) : il tient compte de la partie imaginaire, et '
         'c\'est une racine carrée": {float(TR_6 / 2), float(DET_6)}}'),
        ("c", ANGLE, "as_pi(THETA_6)",
         'kind="exact", angle=True, mistakes={"l\'argument d\'une valeur propre de partie imaginaire positive est '
         'dans ]0, π[": as_pi(-THETA_6), "cos θ = Re(λ)/|λ| et sin θ = Im(λ)/|λ| : vérifie lequel tu as utilisé": '
         'as_pi(math.pi / 2 - THETA_6), "ton angle est celui de la valeur propre conjuguée : l\'argument de λ, de '
         'partie imaginaire positive, est dans ]0, π[": as_pi(2 * math.pi - THETA_6), "le cosinus de l\'argument a '
         'le signe de la partie réelle": as_pi(math.pi - THETA_6)}'),
        ("d", MATRIX, "floats(M3_6)",
         'decimals=4, mistakes={"M³ est le produit matriciel M × M × M, pas le cube de chaque coefficient": '
         'floats(CUBED_6), "M³ a trois facteurs : multiplie encore une fois par M": floats(M2_6)}'),
        ("e", MATRIX, "floats(M6_6)",
         'decimals=4, mistakes={"vérifie les signes : fais chaque produit ligne par colonne": '
         'floats([[-x for x in row] for row in M6_6])}'),
        ("f", "a list of 2 numbers", "[N1_6, NINF_6]",
         'decimals=4, mistakes={"les normes ‖·‖₁ et ‖·‖∞ additionnent les valeurs absolues des coefficients, pas les '
         'coefficients avec leurs signes": SIGNED_6, "‖·‖₁ prend les sommes de colonnes, ‖·‖∞ les sommes de lignes": '
         '[NINF_6, N1_6], "‖·‖₁ et ‖·‖∞ prennent la plus grande des sommes, colonne par colonne ou ligne par ligne": '
         'SMALLEST_6}'),
        ("g", "a number (4 decimals)", "N2_6",
         'decimals=4, mistakes={"‖M‖₂ est une valeur singulière : la racine carrée d\'une valeur propre de MᵀM": '
         'GRAM_MAX_6, "le nombre que tu donnes est-il le plus grand facteur d\'allongement ‖M x‖/‖x‖ ? Essaie '
         'quelques vecteurs": RHO_6, "la norme de Frobenius n\'est pas la norme induite ‖·‖₂": FROB_6, "‖M‖₂ est la '
         'PLUS GRANDE valeur singulière": float(SV_6[-1])}'),
        ("h", "a list of 2 codes (1, 2 or 3)", "CODES_6",
         'mistakes={"multiplier une matrice par 2/√3 multiplie ses valeurs propres par 2/√3 : regarde leur nouveau '
         'module": [CODES_6[0], 1], "que deviennent les puissances d\'une matrice diagonalisable dont les valeurs '
         'propres ont un module égal à 1 ?": [CODES_6[0], 3], "Aᵗ → 0 si et seulement si ρ(A) < 1, même quand une '
         'norme de A dépasse 1": [2, CODES_6[1]], "le comportement des puissances se lit sur le rayon spectral, pas '
         'sur une norme": [2, 3]}'),
    ]),
    Paper("CP5.7", "Produits de jacobiennes le long d'une trajectoire, et sensibilité à un paramètre utilisé à "
                   "chaque pas", [
        ("a", "a list of 2 numbers", "floats(PS_7[2])",
         'decimals=4, mistakes={"la question demande p₂ : f s\'applique deux fois": floats(PS_7[1])}'),
        ("b", MATRIX, "floats(D2_7)",
         'decimals=4, mistakes={"un produit de jacobiennes se range le dernier pas à gauche": '
         'floats(fmatmul(J0_7, J1_7)), "chaque jacobienne s\'évalue en son propre point : le second pas part de '
         'p₁": floats(fmatmul(J0_7, J0_7)), "la jacobienne du pas t s\'évalue au point de départ de ce pas, pₜ": '
         'floats(fmatmul(J2_7, J1_7)), "une jacobienne a une ligne par coordonnée de sortie": '
         'floats(ftranspose(D2_7)), "le premier pas part de p₀ : sa jacobienne s\'évalue en p₀": '
         'floats(fmatmul(J1_7, J1_7))}'),
        ("c", "a list of 2 numbers", "NORMS_7",
         'decimals=4, mistakes={"‖·‖∞ prend la plus grande somme des valeurs absolues d\'une ligne, sur le produit '
         'rangé le dernier pas à gauche": SLIPS_C_7["columns"], "l\'ordre demandé : le produit des normes, puis la '
         'norme du produit": NORMS_7[::-1]}'),
        ("d", "a list of 3 numbers", "floats(TERMS_7)",
         'decimals=4, mistakes={"chaque effet de β est ensuite porté jusqu\'à x₃ par les jacobiennes des pas '
         'suivants": floats(BT_7), "range les termes du pas 0 au pas 2": floats(TERMS_7[::-1]), "la jacobienne du '
         'pas où β sert ne porte pas son propre effet : seules celles des pas suivants le portent": floats(OWN_7)}'),
        ("e", "a number", "float(S3_7)",
         'decimals=4, mistakes={"chaque effet de β est porté jusqu\'à x₃ par les jacobiennes des pas suivants": '
         'float(sum(BT_7)), "s₃ additionne les effets de β à tous les pas où il sert": float(BT_7[-1]), '
         '"la jacobienne du pas où β sert ne porte pas son propre effet : seules celles des pas suivants le '
         'portent": float(sum(OWN_7))}'),
        ("f", "a number", "float(DX3_7)",
         'decimals=4, mistakes={"ta réponse est-elle un changement de hauteur, en cm, pour la variation de β '
         'donnée ?": float(S3_7), "un orifice qui laisse sortir plus d\'eau fait-il monter ou baisser le niveau ? '
         'Vérifie le signe": -float(DX3_7), "c\'est le changement exact ; la question demande l\'approximation au '
         'premier ordre, par la sensibilité": {EXACT_7, round(EXACT_7, 3)}}'),
    ]),
    Paper("CP5.9", "Corriger une copie : cinq erreurs (les lettres seulement)", [
        ("a", 'the letters, as text (like "ABCDE")', '"ABDEG"', f"mistakes={LETTERS}"),
    ]),
    Paper("CP5.10", "Problème de synthèse : un filtre récursif et un filtre à réponse finie, du signal à la stabilité", [
        ("a", "a list of 5 numbers", "floats(H_10[:5])",
         'decimals=4, mistakes={"dans hₖ = C Aᵏ B, B choisit une colonne de Aᵏ et C une ligne : vérifie lesquelles":'
         ' floats(H12_10), "la réponse impulsionnelle commence à h₀ = C B": floats(H_10[1:6]), "hₖ est une sortie : '
         'relis quelle coordonnée de l\'état C lit": floats(FIRST_10)}'),
        ("b", "a list of 5 numbers", "floats(OUT_10[1:6])",
         'decimals=4, mistakes={"yₜ₊₁ = (h * u)ₜ : un pas de décalage entre la sortie et la convolution": '
         'CONV_10[1:6].tolist()}'),
        ("c", "a number (4 decimals)", "RHO_10",
         'decimals=4, mistakes={"le module d\'une valeur propre complexe tient compte de sa partie imaginaire": '
         'float(TR_10 / 2), "un module est une racine carrée : |λ|² = λ λ̄": float(DET_10)}'),
        ("d", "a list of 3 numbers", "NORMS_10",
         'decimals=4, mistakes={"‖A‖₂ est une valeur singulière : la racine carrée d\'une valeur propre de AᵀA": '
         'NORMS_10[:2] + [float(NORM2_10 ** 2)], "ta troisième valeur est-elle le plus grand facteur d\'allongement '
         '‖A x‖₂/‖x‖₂ ?": NORMS_10[:2] + [RHO_10], "‖·‖₁ et ‖·‖∞ prennent la plus grande des sommes des valeurs '
         'absolues, colonne par colonne ou ligne par ligne": SIGNED_10 + NORMS_10[2:], "la norme de Frobenius '
         'n\'est pas la norme induite ‖·‖₂": NORMS_10[:2] + [FROB_10]}'),
        ("e", "an integer", "K_10",
         'fractional="K est un nombre de termes : arrondis à l\'entier qui garantit l\'inégalité.", '
         'mistakes={"le plus petit K qui convient doit vérifier l\'inégalité : arrondis vers le haut": K_10 - 1, '
         '"la majoration porte sur toute la queue, ‖A‖ᴷ/(1 − ‖A‖), avec une norme induite : le rayon spectral ne '
         'majore pas chaque pas": NO_FACTOR_10, "le rayon spectral ne majore pas chaque |hₖ| : la majoration se fait '
         'avec une norme induite, sur toute la queue": RHO_ONLY_10}'),
        ("f", "a number", "float(WORST_10)",
         'decimals=4, mistakes={"sur la boule L∞, le pire cas prend chaque poids en valeur absolue": '
         'float(WORST_SLIPS_10["signs"]), "avec K = 6, le filtre garde six termes de la réponse impulsionnelle": '
         'float(WORST_SLIPS_10["four"]), "g = (h₀, …, h_(K−1)) : compte les termes, h₀ compris": '
         '{float(WORST_SLIPS_10["five"]), float(WORST_SLIPS_10["seven"])}}'),
        ("g", FRACTION, "str(LIMIT_10)",
         'kind="fraction", simplified=True, mistakes={"l\'équilibre vérifie x⋆ = A x⋆ + B u : la matrice du système '
         'est I − A, pas sa transposée": str(LIMIT_T_10), "la limite fait intervenir toute la réponse '
         'impulsionnelle, pas seulement ses premiers termes": str(PARTIAL_10)}'),
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
    return True


def as_written(answer):
    """A complex number typed as such (0.5 + 2j) is read as the list [a, b] that the statement asks for."""
    if isinstance(answer, complex):
        return [answer.real, answer.imag]
    return answer'''

SUMMARY = r'''# Summary of the automatic checks
import re

EXPECTED = ''' + repr(EXPECTED) + r'''


def natural(sub_id):
    """CP5.2a before CP5.10a: the question number as a number, then the letter."""
    number, letter = re.match(r"CP5\.(\d+)(.*)", sub_id).groups()
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

**Ne commence qu'une fois ta copie terminée**, examen rendu. Ce notebook vérifie les réponses que tu as écrites sur ta feuille, question par question : ✅ juste, ❌ faux (avec une piste), ⏳ pas rempli. Il ne note pas : les démarches, les justifications, le quiz CP5.Q1, la démonstration CP5.8 et les corrections de CP5.9 b) se corrigent avec `03_examen_corrige.md`, qui donne aussi le barème.

1. Passe `EXAM_OVER` à `True` dans la cellule ci-dessous, puis exécute-la.
2. Reporte chaque réponse de ta feuille : **la valeur** que tu as écrite, pas un nouveau calcul (sinon tu ne vérifies plus ta copie). Laisse `...` pour une question que tu n'as pas faite.
3. Si une cellule s'arrête sur une erreur, « Tout exécuter » s'arrête avec elle : corrige-la, puis relance cette cellule et les suivantes, jusqu'au bilan.
4. Les formes d'écriture : en Python, le séparateur décimal est un **point** (`2.75`) : une virgule arrête toute la cellule (`0,027`), et aucune réponse de la question n'est vérifiée, ou donne un couple de nombres (`0,75`) ; une liste s'écrit entre crochets (`[-1.5, 4]`), une matrice comme la liste de ses lignes (`[[1, -2], [0.5, 3]]`), un nombre complexe $a + ib$ comme la liste `[a, b]` (ou `a + bj`, à la manière de Python) ; un texte entre guillemets (`"XYZ"`), comme une fraction (`"3/8"`) ou un angle exact (`"pi/5"`) ; un code de comportement (1, 2 ou 3) s'écrit sans guillemets.
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
                  f"        RESULTS[f\"{paper.id}{{letter}}\"] = wbm.check(f\"{paper.id}{{letter}}\", as_written(answer))"]
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
        title = "# CP5 · Examen blanc de la partie V — vérification de ta copie"
        how = (f"L'examen se fait **sur papier** (`01_examen_sujet.md`, {MINUTES} minutes, fiches fermées). Ce notebook "
               "ne sert qu'**après** : il vérifie les réponses chiffrées de ta copie. Ses cellules ne vérifient rien "
               "tant que `EXAM_OVER` vaut `False`, et « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli (⏸️).\n\n"
               "> Travaille dans **ta copie** (`mon_travail/checkpoints/partie_5/02_examen_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py CP5`) : ce fichier-ci est mis à jour par Claude. Sur Colab, le badge "
               "ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme l'explique "
               "`00_setup/COLAB.md` §2.")
    else:
        title = "# CP5 · Examen blanc de la partie V — solutions (notebook exécuté)"
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
                        "CP5.Q1 ; la démonstration CP5.8 ; les corrections de CP5.9 b) (seules les lettres de a) sont "
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
