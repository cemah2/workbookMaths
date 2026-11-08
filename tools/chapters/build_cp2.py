#!/usr/bin/env python
"""Build the two notebooks of the mock exam CP2 from a single source (used by Claude).

    python tools/chapters/build_cp2.py
    python tools/run_all_notebooks.py checkpoints/partie_2/03_examen_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py checkpoints/partie_2/02_examen_notebook.ipynb

Same mechanism as build_cp1.py: the exam of CP2 is on paper only (01_examen_sujet.md), and the exam notebook is the
check done AFTER the exam; nothing is checked while EXAM_OVER is False, so that « Run all » goes to the end.
Wrong-answer messages state a rule or ask a question, never the calculation that gives the answer nor its last step.
The solutions notebook records the answers, computed from the numbers of the statements (cells tagged `answer`, read
by build_answers.py). The final summary lists the sub-IDs that were not checked (a cell that did not run, or that
stopped on an error such as a decimal comma).

The data are new: none comes from the exercises, fiches, quizzes or flashcards of M07 to M11, from CP0 or CP1, from
workbookIA 0B and chapters 7 to 11, its checkpoint II or its mini-project II (no k-means, no hyper-orange or volume of a
cube, no evaluation plan or folds, no ridge in dimension 1, no learning curves, no perceptron, NAND or XOR, no
syllogisms, no leakage, no ε-greedy, no incremental mean, no spam filter, no California; not the 12 wins out of 15 of
the fiche M08, nor its p = 0.03, nor the p-values of M08.7, nor the norms [9, 5, 4] of M07.24, nor the systems of
M09a.9, nor a perpendicular bisector as maximum-margin separator (frontier 7.7), nor the matrix [[2, 1], [4, 3]] of 0B;
no « Bonferroni à l'envers » nor unnormalised margin, which are bugs of M08.24 and M10.16).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import Paper, check_unique_keys, md  # noqa: E402
from nbbuild import badge, code, setup_cell, write_notebook  # noqa: E402

FOLDER = "checkpoints/partie_2"
EXAM = f"{FOLDER}/02_examen_notebook.ipynb"
SOLUTIONS = f"{FOLDER}/03_examen_solutions.ipynb"


def _letter_sets():
    """CP2.10 a: wrong sets of letters, by kind, with messages that name no line (the corrigé explains each line)."""
    from itertools import combinations

    wrong, right = "BCEGH", "ADF"
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
from math import comb


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def solve2(m, v):
    """The solution of the 2 x 2 system m w = v (Cramer)."""
    (a, b), (c, d) = m
    det = a * d - b * c
    return [(d * v[0] - b * v[1]) / det, (a * v[1] - c * v[0]) / det]


# CP2.1: u, v, the hyperplane w · x + b = 0 and the point P
U_1, V_1 = (3, -1, 1, 5), (2, 4, 0, 1)
W_1, B_1, P_1 = (2, -4, 5, 6), -39, (2, 1, 3, 1)
PROJ_1 = [dot(U_1, V_1) / dot(U_1, U_1) * x for x in U_1]
S_1 = dot(W_1, P_1) + B_1

# CP2.2: 16 winning games out of 19 under H0: p = 1/2, then the Wilson and Wald intervals
N_2, K_2, Z = 19, 16, 1.96


def tail_2(k):
    """P(K >= k) for K of law B(19, 1/2)."""
    return sum(comb(N_2, j) for j in range(k, N_2 + 1)) / 2 ** N_2


TAIL_2 = tail_2(K_2)
PH_2 = K_2 / N_2
CENTER_2 = (PH_2 + Z ** 2 / (2 * N_2)) / (1 + Z ** 2 / N_2)
HALF_2 = Z / (1 + Z ** 2 / N_2) * math.sqrt(PH_2 * (1 - PH_2) / N_2 + Z ** 2 / (4 * N_2 ** 2))
WALD_HIGH_2 = PH_2 + Z * math.sqrt(PH_2 * (1 - PH_2) / N_2)

# CP2.3: fourteen p-values, then three models (k, ln L) on n = 60 examples
P_3 = [0.0021, 0.0034, 0.0062, 0.012, 0.024, 0.036, 0.047, 0.058, 0.09, 0.16, 0.27, 0.44, 0.61, 0.92]
MODELS_3, N_3 = [(3, -201.4), (5, -196.0), (8, -190.9)], 60
AIC_3 = [2 * k - 2 * ll for k, ll in MODELS_3]
BIC_3 = [k * math.log(N_3) - 2 * ll for k, ll in MODELS_3]

# CP2.5: X (4 x 2), y, least squares and ridge with lambda = 3
X_5 = [(1, 0), (1, 1), (0, 2), (2, 1)]
Y_5 = [2, 3, 4, 3]
G_5 = [[sum(r[i] * r[j] for r in X_5) for j in range(2)] for i in range(2)]
XY_5 = [sum(r[i] * y for r, y in zip(X_5, Y_5)) for i in range(2)]
W_5 = solve2(G_5, XY_5)
R_5 = [y - dot(r, W_5) for r, y in zip(X_5, Y_5)]
WR_5 = solve2([[G_5[0][0] + 3, G_5[0][1]], [G_5[1][0], G_5[1][1] + 3]], XY_5)
XR_5 = [sum(r[i] * (y - dot(r, WR_5)) for r, y in zip(X_5, Y_5)) for i in range(2)]   # X^T (y - X w_ridge)


# CP2.6: p̃ = (K + 1)/(n + 2) for n = 8 Bernoulli(p) trials
def laplace_6(p, n=8):
    """Bias, variance and mean squared error of (K + 1)/(n + 2)."""
    bias = (n * p + 1) / (n + 2) - p
    variance = n * p * (1 - p) / (n + 2) ** 2
    return bias, variance, variance + bias ** 2


# CP2.7: the margin of a separator for the two labelled clouds
POS_7, NEG_7 = [(4, 1), (6, 7), (8, 2)], [(2, 5), (0, 3), (1, 7)]


def margin_7(w, b):
    scores = [dot(w, x) + b for x in POS_7] + [-(dot(w, x) + b) for x in NEG_7]
    return min(scores) / math.hypot(*w)


# CP2.11: six nights, the line by the normal equations, then three AIC
X_11, Y_11 = [1, 2, 4, 5, 7, 11], [7, 9, 14, 15, 18, 27]
N_11 = len(X_11)
G_11 = [[N_11, sum(X_11)], [sum(X_11), sum(x * x for x in X_11)]]
XY_11 = [sum(Y_11), sum(x * y for x, y in zip(X_11, Y_11))]
A_11, B_11 = solve2(G_11, XY_11)
SCR_11 = sum((y - A_11 - B_11 * x) ** 2 for x, y in zip(X_11, Y_11))
SCT_11 = sum((y - sum(Y_11) / N_11) ** 2 for y in Y_11)


def aic_11(scr, k):
    return N_11 * math.log(scr / N_11) + 2 * k


LOW_11 = 344 / 400 - math.sqrt(math.log(1 / 0.05) / (2 * 400))'''

PAPER = [
    Paper("CP2.1", "Normes, cosinus, projection et distance à un hyperplan", [
        ("a", "[norm 1, norm 2, norm inf]", "[10, 6, 5]",
         'mistakes={"‖u‖₂ est la racine de la somme des carrés": [10, 36, 5], '
         '"‖u‖₁ additionne les valeurs absolues des coordonnées": [8, 6, 5]}'),
        ("b", "a number", "dot(U_1, V_1)",
         'mistakes={"attention au signe de la deuxième coordonnée de u": 15}'),
        ("c", "a number (3 decimals)", "dot(U_1, V_1) / math.sqrt(dot(U_1, U_1) * dot(V_1, V_1))",
         'decimals=3, mistakes={"le cosinus divise le produit scalaire par le produit des deux normes": '
         '{7 / 36, 7 / 21}, "les normes sont des racines carrées : ‖v‖ n\'est pas la somme des carrés": 7 / 126}'),
        ("d", "a list (2 decimals)", "PROJ_1",
         'decimals=2, mistakes={"projeter sur la droite dirigée par u divise u · v par ‖u‖², pas par ‖u‖": '
         '[7 / 6 * x for x in U_1], "c\'est la projection de u sur v ; la question projette v sur u": '
         '[7 / 21 * x for x in V_1], "c\'est la composante orthogonale ; la question demande la projection": '
         '[v - p for v, p in zip(V_1, PROJ_1)]}'),
        ("e", "a number (3 decimals)", "math.dist(V_1, PROJ_1)",
         'decimals=3, mistakes={"c\'est le carré de la distance": dot(V_1, V_1) - 49 / 36, '
         '"c\'est la norme de la projection ; la distance est celle de v à sa projection": 7 / 6}'),
        ("f", "a number (1 decimal)", "S_1 / math.sqrt(dot(W_1, W_1))",
         'decimals=1, mistakes={"la distance signée divise w · P + b par ‖w‖, pas par ‖w‖²": S_1 / 81, '
         '"divise w · P + b par la norme de w": float(S_1), "la distance est signée : le signe de w · P + b dit de quel '
         'côté de H est P": -S_1 / 9, "l\'équation s\'écrit w · x + b = 0, avec b = −39": 60 / 9}'),
        ("g", "a list (2 decimals)", "[p - S_1 / dot(W_1, W_1) * w for p, w in zip(P_1, W_1)]",
         'decimals=2, mistakes={"P est du côté où w · x + b < 0 : on avance dans le sens de w": '
         '[p + S_1 / 81 * w for p, w in zip(P_1, W_1)], "le coefficient de w est (w · P + b) / ‖w‖², pour arriver '
         'sur H": [p - S_1 / 9 * w for p, w in zip(P_1, W_1)]}'),
    ]),
    Paper("CP2.2", "Un test binomial et un intervalle de Wilson", [
        ("a", "a number (4 decimals)", "TAIL_2",
         'decimals=4, mistakes={"« au moins 16 » compte aussi 17, 18 et 19 parties gagnantes": comb(19, 16) / 2 ** 19, '
         '"P(K ≥ 16) contient le cas K = 16": tail_2(17), '
         '"compte toutes les façons de placer les parties gagnantes : les coefficients binomiaux": '
         '4 / 2 ** 19}'),
        ("b", "a number (4 decimals)", "2 * TAIL_2",
         'decimals=4, mistakes={"le test bilatéral compte aussi le côté opposé, aussi extrême": TAIL_2, '
         '"la loi de K est symétrique sous H0 : les deux côtés ont la même probabilité": TAIL_2 / 2}'),
        ("c", "True or False", "True",
         'mistakes={"compare la p-valeur bilatérale au seuil de 0,05": False}'),
        ("d", "an integer", "14",
         'mistakes={"calcule P(K ≥ 13) sous H0 et compare-la à 0,05": 13, '
         '"P(K ≥ 14) est-elle déjà sous 0,05 ?": 15}'),
        ("e", "[low, high] (3 decimals)", "[CENTER_2 - HALF_2, CENTER_2 + HALF_2]",
         'decimals=3, mistakes={"c\'est l\'intervalle de Wald ; Wilson décale le centre vers 1/2 et change la '
         'demi-largeur": [PH_2 - Z * math.sqrt(PH_2 * (1 - PH_2) / N_2), WALD_HIGH_2]}'),
        ("f", "a number (3 decimals)", "WALD_HIGH_2",
         'decimals=3, mistakes={"c\'est la borne haute de Wilson ; la question demande celle de Wald": '
         'CENTER_2 + HALF_2, "l\'erreur type de Wald divise p̂ (1 − p̂) par n": '
         'PH_2 + Z * math.sqrt(PH_2 * (1 - PH_2) / (N_2 - 1)), "la borne de Wald se donne telle que la formule la '
         'calcule, sans la couper à 1 : c\'est elle que la copie commente": 1.0}'),
    ]),
    Paper("CP2.3", "Comparaisons multiples, AIC et BIC", [
        ("a", "an integer", "sum(p <= 0.05 for p in P_3)",
         'mistakes={"compte toutes les p-valeurs inférieures à 0,05, la plus grande comprise": 6, '
         '"0,058 dépasse 0,05": 8}'),
        ("b", "an integer", "sum(p <= 0.05 / 14 for p in P_3)",
         'mistakes={"Bonferroni compare chaque p-valeur au seuil divisé par le nombre de tests": {1, 7}, '
         '"Bonferroni utilise le même seuil α/m pour toutes les p-valeurs, pas un seuil qui grandit avec le rang": 3}'),
        ("c", "a number (3 decimals)", "min(1, 14 * P_3[2])",
         'decimals=3, mistakes={"la p-valeur ajustée de Bonferroni multiplie la p-valeur (sans dépasser 1)": '
         'P_3[2] / 14, "Bonferroni multiplie par le nombre total de tests, pas par le rang": 3 * P_3[2]}'),
        ("d", "a list (1 decimal)", "AIC_3",
         'decimals=1, mistakes={"AIC = 2k − 2 ln L : la log-vraisemblance est multipliée par −2": '
         '[2 * k - ll for k, ll in MODELS_3], "AIC = 2k − 2 ln L : les deux termes ont un facteur 2": '
         '[k - ll for k, ll in MODELS_3], "la pénalité de l\'AIC est 2k": [k - 2 * ll for k, ll in MODELS_3], '
         '"la log-vraisemblance entre avec le signe moins": [2 * k + 2 * ll for k, ll in MODELS_3]}'),
        ("e", "a list (1 decimal)", "BIC_3",
         'decimals=1, mistakes={"le BIC utilise le logarithme népérien de n": '
         '[k * math.log10(N_3) - 2 * ll for k, ll in MODELS_3], "la pénalité du BIC est k ln n": AIC_3, '
         '"BIC = k ln n − 2 ln L : la log-vraisemblance a un facteur 2": '
         '[k * math.log(N_3) - ll for k, ll in MODELS_3]}'),
        ("f", "[AIC choice, BIC choice]", "[3, 2]",
         'mistakes={"on retient le modèle de plus petit AIC, et de plus petit BIC": [1, 1], '
         '"le BIC pénalise chaque paramètre plus fort que l\'AIC : compare tes trois BIC": [3, 3]}'),
    ]),
    Paper("CP2.4", "Pivot de Gauss, rang et inverse", [
        ("a", "a list of 4 numbers", "[0, 3, 7, 4]",
         'mistakes={"L₃ ← L₃ + 2L₁ : on ajoute deux fois la première ligne": [-4, -1, -1, -8], '
         '"l\'opération porte aussi sur le second membre": [0, 3, 7, -2]}'),
        ("b", "a list of 4 numbers", "[0, 0, 10, 10]",
         'mistakes={"la troisième ligne est L₃ − 3 L₂, avec la ligne L₂ obtenue après l\'élimination de x : '
         'vérifie le signe de chaque coefficient": [0, 6, 4, -2]}'),
        ("c", "[x, y, z]", "[2, -1, 1]",
         'mistakes={"la liste est [x, y, z], dans cet ordre": [1, -1, 2]}'),
        ("d", "[[a, b], [c, d]]", "[[2, -2.5], [-1, 1.5]]",
         'decimals=2, mistakes={"la formule de l\'inverse divise par le déterminant ad − bc": [[4, -5], [-2, 3]], '
         '"la formule échange a et d et change le signe de b et c, sans transposer": [[2, -1], [-2.5, 1.5]], '
         '"la formule change le signe de b et de c": [[2, 2.5], [1, 1.5]], '
         '"la formule échange les coefficients a et d": [[1.5, -2.5], [-1, 2]]}'),
        ("e", "a list of 2 numbers", "[-3, 2]",
         'mistakes={"la solution est B⁻¹ (1, 2), pas B (1, 2)": [13, 10]}'),
        ("f", "an integer", "2",
         'mistakes={"cherche une ligne qui est une combinaison des autres": 3, '
         '"le rang d\'une matrice à 3 lignes est au plus 3": 4}'),
        ("g", "a number", "4", ""),
    ]),
    Paper("CP2.5", "Les équations normales d'un petit modèle, avec et sans ridge", [
        ("a", "[[a, b], [c, d]]", "G_5", ""),
        ("b", "a list of 2 numbers", "XY_5",
         'mistakes={"Xᵀy multiplie chaque colonne de X par y, exemple par exemple": [8, 13]}'),
        ("c", "a list (4 decimals)", "W_5",
         'decimals=4, mistakes={"l\'inverse de XᵀX divise par son déterminant": [24, 51], '
         '"la liste est [w₁, w₂]": W_5[::-1]}'),
        ("d", "a list (4 decimals)", "R_5",
         'decimals=4, mistakes={"le résidu est y − Xw, pas Xw − y": [-r for r in R_5]}'),
        ("e", "a number (4 decimals)", "sum(r * r for r in R_5)",
         'decimals=4, mistakes={"la SCR additionne les carrés des résidus": sum(R_5), '
         '"la SCR est une somme, pas une moyenne": sum(r * r for r in R_5) / 4}'),
        ("f", "a list (4 decimals)", "WR_5",
         'decimals=4, mistakes={"λI n\'ajoute λ que sur la diagonale de XᵀX": solve2([[9, 6], [6, 9]], XY_5), '
         '"la loss ‖y − Xw‖² + λ‖w‖² donne (XᵀX + λI) w = Xᵀy, sans facteur 2 sur λ": '
         'solve2([[12, 3], [3, 12]], XY_5), "ce sont les poids sans pénalité : λ change la matrice à inverser": W_5}'),
        ("g", "a list (3 decimals)", "XR_5",
         'decimals=3, mistakes={"le résidu est y − X w_ridge, pas X w_ridge − y": [-x for x in XR_5], '
         '"le calcul demande les poids de ridge, pas ceux des moindres carrés": [0, 0]}'),
    ]),
    Paper("CP2.6", "Biais, variance et erreur quadratique d'un estimateur", [
        ("a", "a number (2 decimals)", "laplace_6(0.2)[0]",
         'decimals=2, mistakes={"le biais est E[p̃] − p, dans cet ordre": -laplace_6(0.2)[0], '
         '"le biais est E[p̃] − p, pas E[p̃]": laplace_6(0.2)[0] + 0.2, '
         '"la question porte sur p̃ = (K + 1)/(n + 2)": 0}'),
        ("b", "a number (4 decimals)", "laplace_6(0.2)[1]",
         'decimals=4, mistakes={"V(K + 1) = V(K) = n p (1 − p), et diviser par n + 2 divise la variance par '
         '(n + 2)²": 8 * 0.2 * 0.8 / 10, "V(K) = n p (1 − p), avec n = 8": 0.2 * 0.8 / 100, '
         '"la question porte sur p̃ = (K + 1)/(n + 2)": 0.2 * 0.8 / 8}'),
        ("c", "a number (4 decimals)", "laplace_6(0.2)[2]",
         'decimals=4, mistakes={"l\'erreur quadratique ajoute le carré du biais à la variance": laplace_6(0.2)[1], '
         '"le biais entre au carré": laplace_6(0.2)[1] + laplace_6(0.2)[0]}'),
        ("d", "a number (4 decimals)", "0.2 * 0.8 / 8",
         'decimals=4, mistakes={"la variance de K/n est p (1 − p) / n": 0.2 * 0.8}'),
        ("e", "a number (4 decimals)", "laplace_6(0.05)[2]",
         'decimals=4, mistakes={"l\'erreur quadratique ajoute le carré du biais à la variance": laplace_6(0.05)[1], '
         '"le biais entre au carré": laplace_6(0.05)[1] + laplace_6(0.05)[0], '
         '"la question porte sur p̃ = (K + 1)/(n + 2)": 0.05 * 0.95 / 8}'),
        ("f", "1 or 2", "1",
         'choices=[1, 2], mistakes={"compare e) à l\'erreur quadratique de p̂ pour p = 0,05": 2}'),
    ]),
    Paper("CP2.7", "Convexité, enveloppe convexe et marge", [
        ("a", "[[x, y], ...]", "[[0, 0], [4, 0], [5, 3], [2, 5]]",
         'mistakes={"le sens direct tourne vers la gauche, comme le sens contraire des aiguilles": '
         '[[0, 0], [2, 5], [5, 3], [4, 0]], "un point intérieur n\'est pas un sommet : teste (1, 2) avec un produit '
         'vectoriel": [[0, 0], [4, 0], [5, 3], [2, 5], [1, 2]]}'),
        ("b", "True or False", "True",
         'mistakes={"teste (3, 4) contre chaque côté avec un produit vectoriel, sens direct : il est dedans s\'il est '
         'à gauche de chacun": False}'),
        ("c", "a number (3 decimals)", "margin_7((2, -1), -2)",
         'decimals=3, mistakes={"la marge géométrique divise par ‖w‖": 3, "‖w‖ est la racine de 2² + (−1)²": 3 / 5}'),
        ("d", "a number (3 decimals)", "margin_7((3, -1), -6)",
         'decimals=3, mistakes={"la marge maximale est la moitié de la distance entre les deux enveloppes": '
         '2 * margin_7((3, -1), -6), "la distance entre deux enveloppes peut être celle d\'un sommet à un côté, '
         'pas seulement entre deux sommets": math.dist((2, 5), (4, 1)) / 2}'),
        ("e", "[w1, w2, b]", "[0.6, -0.2, -1.2]",
         'decimals=2, mistakes={"dans ta forme, le plus petit yᵢ (w · xᵢ + b) vaut-il 1 ?": [3, -1, -6], '
         '"la classe +1 doit être du côté où w · x + b > 0": [-0.6, 0.2, 1.2]}'),
    ]),
    Paper("CP2.8", "Markov, Tchebychev et Hoeffding", [
        ("a", "a number (1 decimal)", "120 / 300",
         'decimals=1, mistakes={"Markov divise la moyenne par le seuil": 300 / 120}'),
        ("b", "a number (4 decimals)", "30 ** 2 / (300 - 120) ** 2",
         'decimals=4, mistakes={"Tchebychev divise la variance par le carré de l\'écart": 30 / 180, '
         '"l\'écart à la moyenne est 300 − 120": 900 / 300 ** 2, '
         '"la question demande Tchebychev : P(|T − μ| ≥ t) ≤ σ²/t²": 900 / (900 + 180 ** 2)}'),
        ("c", "an integer", "720",
         'mistakes={"Tchebychev utilise la variance de T̄, σ²/n, avec σ² = 900": {24, 120}, '
         '"Tchebychev divise par le carré de l\'écart": 3600}'),
        ("d", "a number (3 decimals)", "math.sqrt(math.log(2 / 0.02) / (2 * 1200))",
         'decimals=3, mistakes={"le rayon bilatéral utilise ln(2/δ)": math.sqrt(math.log(1 / 0.02) / 2400), '
         '"ln(2/δ) se divise par 2n": math.sqrt(math.log(100) / 1200)}'),
        ("e", "a number (4 decimals)", "2 * math.exp(-2 * 1200 * 0.05 ** 2)",
         'decimals=4, mistakes={"la borne bilatérale a un facteur 2": math.exp(-6)}'),
        ("f", "an integer", "math.ceil(math.log(2 / 0.02) / (2 * 0.025 ** 2))",
         'mistakes={"n doit être au moins égal à la formule : arrondis au-dessus": 3684, '
         '"le rayon bilatéral utilise ln(2/δ)": 3130, "ln(2/δ) se divise par 2 t²": 7369}'),
    ]),
    Paper("CP2.10", "Corriger une copie : cinq erreurs (les lettres seulement)", [
        ("a", 'the letters, as text (like "ABCDE")', '"BCEGH"', f"mistakes={LETTERS}"),
    ]),
    Paper("CP2.11", "Problème de synthèse : ajuster un modèle, mesurer son erreur, décider", [
        ("a", "[sum of x², sum of x y]", "[G_11[1][1], XY_11[1]]",
         'mistakes={"Σxᵢ² additionne les carrés des tailles, et Σxᵢyᵢ les produits nuit par nuit": [30 ** 2, 30 * 90]}'),
        ("b", "[a, b] (4 decimals)", "[A_11, B_11]",
         'decimals=4, mistakes={"la liste est [a, b] : l\'ordonnée à l\'origine d\'abord": [B_11, A_11]}'),
        ("c", "a number (2 decimals)", "SCR_11",
         'decimals=2, mistakes={"la SCR mesure les résidus du modèle, pas les écarts à la moyenne de y": SCT_11}'),
        ("d", "a number (3 decimals)", "1 - SCR_11 / SCT_11",
         'decimals=3, mistakes={"R² = 1 − SCR / SCT": SCR_11 / SCT_11, '
         '"R² = 1 − SCR / SCT, pas sa racine": math.sqrt(1 - SCR_11 / SCT_11)}'),
        ("e", "a number (1 decimal)", "aic_11(SCR_11, 2)",
         'decimals=1, mistakes={"l\'AIC prend le logarithme de SCR / n": N_11 * math.log(SCR_11) + 4, '
         '"ln est le logarithme népérien": N_11 * math.log10(SCR_11 / N_11) + 4, '
         '"l\'AIC ajoute 2k": N_11 * math.log(SCR_11 / N_11)}'),
        ("f", "0, 1 or 2", "1",
         'choices=[0, 1, 2], mistakes={"un coefficient de plus coûte 2 dans l\'AIC : la SCR baisse-t-elle assez ?": 2, '
         '"compare les trois AIC : le plus petit est retenu": 0}'),
        ("g", "a number (3 decimals)", "LOW_11",
         'decimals=3, mistakes={"une borne d\'un seul côté utilise ln(1/δ), pas ln(2/δ)": '
         '344 / 400 - math.sqrt(math.log(2 / 0.05) / 800), "ln(1/δ) se divise par 2n": '
         '344 / 400 - math.sqrt(math.log(20) / 400), "garde les décimales jusqu\'à la comparaison : ici, c\'est la '
         'troisième décimale qui décide de la question suivante": 0.8}'),
        ("h", "True or False", "False",
         'mistakes={"compare à 0,80 la borne de g) sans l\'arrondir davantage": True}'),
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
    """CP2.2a before CP2.10a: the question number as a number, then the letter."""
    number, letter = re.match(r"CP2\.(\d+)(.*)", sub_id).groups()
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

**Ne commence qu'une fois ta copie terminée**, examen rendu. Ce notebook vérifie les réponses que tu as écrites sur ta feuille, question par question : ✅ juste, ❌ faux (avec une piste), ⏳ pas rempli. Il ne note pas : les démarches, les justifications, le quiz CP2.Q1, la démonstration CP2.9 et les corrections de CP2.10 b) se corrigent avec `03_examen_corrige.md`, qui donne aussi le barème.

1. Passe `EXAM_OVER` à `True` dans la cellule ci-dessous, puis exécute-la.
2. Reporte chaque réponse de ta feuille : **la valeur** que tu as écrite, pas un nouveau calcul (sinon tu ne vérifies plus ta copie). Laisse `...` pour une question que tu n'as pas faite.
3. Les formes d'écriture : en Python, le séparateur décimal est un **point** (`2.75`) : une virgule arrête toute la cellule (`0,027`), et aucune réponse de la question n'est vérifiée, ou donne un couple de nombres (`0,75`) ; une liste s'écrit entre crochets (`[-1.5, 4]`), une matrice comme une liste de lignes (`[[1, -2], [0.5, 3]]`) ; un texte entre guillemets (`"XYZ"`) ; vrai ou faux par `True` ou `False`.
4. Le bilan, à la fin, dit aussi quelles réponses n'ont pas été vérifiées.'''


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
        title = "# CP2 · Examen blanc de la partie II — vérification de ta copie"
        how = ("L'examen se fait **sur papier** (`01_examen_sujet.md`, 117 minutes, fiches fermées). Ce notebook ne "
               "sert qu'**après** : il vérifie les réponses chiffrées de ta copie. Ses cellules ne vérifient rien tant "
               "que `EXAM_OVER` vaut `False`, et « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli (⏸️).\n\n"
               "> Travaille dans **ta copie** (`mon_travail/checkpoints/partie_2/02_examen_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py CP2`) : ce fichier-ci est mis à jour par Claude. Sur Colab, le badge "
               "ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme l'explique "
               "`00_setup/COLAB.md` §2.")
    else:
        title = "# CP2 · Examen blanc de la partie II — solutions (notebook exécuté)"
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
                        "CP2.Q1 ; la démonstration CP2.9 ; les corrections de CP2.10 b) (seules les lettres de a) sont "
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
