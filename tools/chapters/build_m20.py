#!/usr/bin/env python
"""Build the two notebooks of chapter M20 from a single source (used by Claude).

    python tools/chapters/build_m20.py
    python tools/run_all_notebooks.py chapitres/m20_tenseurs_normalisation/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m20_tenseurs_normalisation/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M20.1 to M20.5, 🔗 M20.8), each answer computed in the notebook from the data of
its statement (NumPy, fractions); parts A to D are the notebook exercises (M20.10 to M20.18). Wrong-answer messages
state a rule, never a number of the answer nor the last step that gives it. The data are new: written in the
statements, or synthetic with the seeds 5331 to 5339 only (never 20xx): hourly temperatures of 3 stations over 5 days
(M20.10) and of 6 stations over 31 days (M20.13), the marks of 40 pupils in 6 subjects (M20.11), 25 pupils in 4
subjects (M20.13), 6 pupils in 3 subjects (M20.16), an image of shape (height, width, channels) = (120, 160, 3)
(M20.13), the inhabitants of 8 communes (M20.12), 400 firms with their headcount and turnover (M20.14), 150 communes
with their census population (M20.18), a 2 × 2 Euler step and a damped non-linear oscillator (M20.15). None is a test
case of tests/test_m20_tensors.py (seeds 5310 to 5329), an example of the docstrings of the stub, the data of a paper
exercise or an example of the fiche: no (4, 7, 24), (12, 28, 24) or (480, 640, 3) array, no forest of 5 plots, no
rotation [[0, −1], [1, 0]] or [[0, −2], [2, 0]], no pendulum. Nothing of workbookIA 20 is used (the notes of M20 in the
syllabus): no shape (N, C, H, W), (32, 3, 28, 28), (1, 512, 7, 7), (10, 3, 5), (2, 3, 5, 5), (2, 3, 5), (2, 3, 4),
(64, 20) nor (1, 1, 5, 4), no arange, none of its vectors, tables, numbers or seeds; no probability 0.5, 0.6, 0.75,
0.8, 0.2, 0.25 nor 0.4 in a sampling design (the inclusion probabilities of M20.12 are written in the statement, those
of M20.14 and M20.18 are proportional to a size); no neuron, layer (except in the bridge M20.8, which only names the
layers of workbookIA 20), mask, mini-batch, dropout, batchnorm, layer norm, γ, β, ε nor running statistics; no
derivative of the standardisation, no product of Jacobians presented as a backward pass (M20.15 is an Euler scheme at
a fixed horizon, the identity always in the factors), no composition of x/‖x‖ with the centring, no PyTorch. The
einsum formulas are new ("sdh,h->sd", "ij,j->i", "i,i->", "sij,sjk->sik" against np.matmul, "hwc,c->hw",
"sdh,sdh->s"), none of the four formulas listed in the syllabus notes. The standardisation of M20.11 is done subject by
subject (axis 0 of a table pupils × subjects), with ddof = 1, no eps; it is checked against a direct NumPy oracle and
by a renotation (one subject marked out of 100, another shifted by 2 points), never by « mean 0 and mean square 1 ».
M20.14 compares Horvitz-Thompson with π ∝ the headcount, the naive N ȳ_S and Horvitz-Thompson with π ∝ the age of the
firm (unequal probabilities unrelated to y, of the same sum), never a common probability under Poisson sampling; only
M20.18 compares with the equal probabilities n/N, under a systematic draw of fixed size. The ddof bug of M20.16 is on
the standard deviation of five repeated measurements, its axis bug on a mean per subject. The communes 2 and 3 of M20.12 are ordered so that the drawn sample is [3, 4, 5]; M20.13 h reshapes the stations of T_13 (no image put channels first) and W_13 = (2, −1, −1) is no weighting of a grey level; M20.15 c asks the lower bound (1 − hK)^L at L = 16, never the smallest L for which it holds, and nothing at a fixed step h. M20.17 passes the function under test as the first argument
of check_two_axes(moments, x, a, b), so that the check can run the learner's property test on the reference and on
three wrong functions built on it.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, check_unique_keys, guarded,  # noqa: E402,F401
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M20"
FOLDER = "chapitres/m20_tenseurs_normalisation"

SHAPE = 'a shape: a tuple (7, 2) or a text "(7, 2)"'
FORMULA = 'an einsum formula, as text: "ab,b->a"'
MATRIX = "a matrix (list of rows)"
LETTER = '"A", "B", "C" or "D"'


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M20.1", "Un tableau de mesures (stations × jours × heures) : les formes après réductions et remodelages", [
        ("a", "an integer", "int(T_1.size)"),
        ("b", SHAPE, "shape_of(T_1.mean(axis=2))",
         '''mistakes={"l'axe nommé disparaît : axis=2 est l'axe des heures": shape_of(T_1.mean(axis=1)),
                     "sans keepdims=True, l'axe réduit disparaît au lieu de garder la longueur 1":
                         shape_of(T_1.mean(axis=2, keepdims=True))}'''),
        ("c", SHAPE, "shape_of(T_1.mean(axis=(0, 2), keepdims=True))",
         '''mistakes={"keepdims=True garde les axes réduits, avec la longueur 1 : le résultat a autant d'axes que T":
                         shape_of(T_1.mean(axis=(0, 2))),
                     "keepdims=True donne la longueur 1 aux axes RÉDUITS ; les autres gardent leur longueur":
                         shape_of(T_1.mean(axis=1, keepdims=True))}'''),
        ("d", "an integer", "int(np.ravel_multi_index((3, 10, 5), SHAPE_1))",
         '''mistakes={"la position est (i₀n₁ + i₁)n₂ + i₂ : le dernier indice s'ajoute à la fin":
                         int(np.ravel_multi_index((3, 10, 0), SHAPE_1)),
                     "l'ordre C : le DERNIER indice varie le plus vite ; ton calcul fait varier le premier le plus "
                     "vite (l'ordre de Fortran)": int(np.ravel_multi_index((3, 10, 5), SHAPE_1, order="F")),
                     "les positions de la file se comptent à partir de 0, comme les indices":
                         int(np.ravel_multi_index((3, 10, 5), SHAPE_1)) + 1}'''),
        ("e", "a list of 3 integers", "[int(i) for i in np.unravel_index(1000, SHAPE_1)]",
         '''mistakes={"les indices dans l'ordre des axes, [i₀, i₁, i₂] : la station d'abord, l'heure en dernier":
                         [int(i) for i in np.unravel_index(1000, SHAPE_1)][::-1],
                     "les positions de la file se comptent à partir de 0 : la position 1 000 est le 1 001ᵉ élément":
                         [int(i) for i in np.unravel_index(999, SHAPE_1)],
                     "l'ordre C : le DERNIER indice varie le plus vite ; ton calcul fait varier le premier le plus "
                     "vite (l'ordre de Fortran)": [int(i) for i in np.unravel_index(1000, SHAPE_1, order="F")],
                     "les indices d'un tableau NumPy se comptent à partir de 0, comme les positions de la file":
                         [int(i) + 1 for i in np.unravel_index(1000, SHAPE_1)]}'''),
        ("f", "a list of 3 integers", "[int(i) for i in np.unravel_index(np.ravel_multi_index((3, 1, 3, 5), "
                                      "R_1.shape), SHAPE_1)]",
         '''mistakes={"le jour vaut 7 × semaine + jour de la semaine : l'axe 1 de R, de longueur 4, est celui des "
                     "semaines": [3, 1 + 4 * 3, 5]}'''),
        ("g", SHAPE, "shape_of(R_1.mean(axis=1))",
         '''mistakes={"l'axe nommé disparaît : quel est l'axe 1 de R = T.reshape(12, 4, 7, 24) ?":
                         shape_of(R_1.mean(axis=2))}'''),
        ("h", "True or False", "H_1",
         '''mistakes={"aligne les deux formes à droite, (12, 28, 24) contre la forme de T.mean(axis=1), et compare "
                     "les longueurs axe par axe": not H_1}'''),
        ("i", SHAPE, "shape_of(T_1.transpose(2, 0, 1))",
         '''mistakes={"transpose(2, 0, 1) met l'axe 2 en premier, puis les axes 0 et 1, dans cet ordre":
                         shape_of(T_1.transpose(2, 1, 0))}'''),
    ]),

    Paper("M20.2", "Écrire en notation d'Einstein : produit matriciel, trace, forme bilinéaire, produits de matrices "
                   "empilées le long d'un axe", [
        ("a", FORMULA, "FORMULA_AB_2",
         '''mistakes={"une lettre absente du résultat est sommée ; une lettre présente ne l'est pas": "ij,jk->ijk",
                     "écris la forme explicite, avec -> et les lettres du résultat": "ij,jk",
                     "c'est le résultat transposé : les lettres après -> donnent l'ordre des axes": "ij,jk->ki"}'''),
        ("b", "an integer", "int(AB_2[1, 2])",
         '''mistakes={"ligne 2, colonne 3 : la ligne d'abord, puis la colonne": int(AB_2[2, 1])}'''),
        ("c", FORMULA, "FORMULA_TRACE_2",
         '''mistakes={"écris (AB)ᵢᵢ en notation d'Einstein : B n'y porte pas ses indices dans le même ordre que A":
                         "ij,ij->",
                     "la trace est un nombre : aucune lettre après ->": "ij,ji->i",
                     "c'est la somme de TOUS les coefficients de AB, pas la trace : la trace ne garde que (AB)ᵢᵢ":
                         "ij,jk->",
                     "le même calcul, mais avec les lettres imposées : les axes de A se notent ij": "ji,ij->",
                     "écris la forme explicite, avec ->": "ij,ji"}'''),
        ("d", "an integer", "int(np.trace(AB_2))",
         '''mistakes={"la trace somme la seule DIAGONALE de AB": int(AB_2.sum())}'''),
        ("e", "an integer", "int(np.trace(BA_2))",
         '''mistakes={"la trace somme la seule DIAGONALE de BA, une matrice 2 × 2": int(BA_2.sum())}'''),
        ("f", "an integer", "int(X_2 @ M_2 @ Y_2)",
         '''mistakes={"xᵢMᵢⱼyⱼ : x se contracte avec l'indice de LIGNE de M, y avec son indice de colonne":
                         int(Y_2 @ M_2 @ X_2)}'''),
        ("g", MATRIX, "np.einsum('sij,sj->si', MS_2, VS_2).tolist()",
         '''mistakes={"on somme sur j, l'indice de COLONNE de chaque matrice : la ligne s du résultat est Mₛvₛ":
                         np.einsum("sji,sj->si", MS_2, VS_2).tolist()}'''),
        ("h", "an integer", "COST_H_2",
         '''mistakes={"le coût compte toutes les lettres, s comprise": COST_H_2 // 10}'''),
        ("i", "an integer", "COST_I_2",
         '''mistakes={"deux produits à compter : PQ, puis (PQ)R": 30 * 300 * 5,
                     "c'est le coût de l'autre ordre": COST_J_2}'''),
        ("j", "an integer", "COST_J_2",
         '''mistakes={"deux produits à compter : QR, puis P(QR)": 30 * 300 * 50,
                     "c'est le coût de l'autre ordre": COST_I_2}'''),
    ]),

    Paper("M20.3", "La matrice de centrage, et une standardisation qui ne voit ni translation ni dilatation", [
        ("a", "an irreducible fraction, as text", "str(C_3[0][0])",
         '''kind="fraction", simplified=True,
           mistakes={"C = I − (1/m) 11ᵀ : la diagonale vaut 1 − 1/m": "1/6"}'''),
        ("b", "an irreducible fraction, as text", "str(C_3[0][1])",
         '''kind="fraction", simplified=True,
           mistakes={"hors de la diagonale, C retranche 1/m : le coefficient est négatif": "1/6"}'''),
        ("c", "a list of 6 numbers", "fractions_list(CX_3)",
         '''mistakes={"Cx = x − x̄1 : on retranche la moyenne à chaque coordonnée, pas l'inverse":
                         fractions_list([-v for v in CX_3])}'''),
        ("d", "an integer", "int(TRACE_3)",
         '''mistakes={"la diagonale de C vaut 1 − 1/m, pas 1": M_3}'''),
        ("e", "a number", "int(NORM2_CX_3)",
         '''mistakes={"le carré de la norme est la somme des CARRÉS des coordonnées": int(sum(abs(v) for v in CX_3))}'''),
        ("f", "a number", "int(NORM2_MEAN_3)",
         '''mistakes={"x̄1 a m coordonnées, toutes égales à x̄ : ‖x̄1‖² = m x̄²": int(MEAN_3 ** 2)}'''),
        ("g", "a number (4 decimals)", "S_3",
         '''decimals=4, mistakes={"ddof = 1 : la somme des carrés des écarts se divise par m − 1, pas par m": S0_3,
                                 "l'écart type est la RACINE de la variance": S_3 ** 2}'''),
        ("h", "a number (4 decimals)", "float(Z_3[5])",
         '''decimals=4, mistakes={"ddof = 1 : l'écart type divise par m − 1, pas par m": float(Z0_3[5])}'''),
        ("i", "a number (4 decimals)", "float(Z_I_3)",
         '''decimals=4, mistakes={"une dilatation de facteur a > 0 multiplie aussi l'écart type : relis les "
                                 "invariances de la fiche (§4)": 2.5 * float(Z_3[5])}'''),
        ("j", "a number (4 decimals)", "float(Z_J_3)",
         '''decimals=4, mistakes={"un facteur a < 0 change le signe des écarts, et l'écart type est multiplié par "
                                 "|a|": float(Z_3[5])}'''),
        ("k", "True or False", "K_3",
         '''mistakes={"ajouter 10 à une seule coordonnée n'est pas une translation le long de 1": not K_3}'''),
    ]),

    Paper("M20.4", "Un sondage à probabilités inégales : l'estimateur de Horvitz-Thompson d'un total, son espérance et "
                   "sa variance", [
        ("a", "a number", "float(sum(PI_4))", "decimals=6"),
        ("b", "a number (3 decimals)", "float(1 / PI_4[4])",
         '''decimals=3, mistakes={"le poids de sondage est l'INVERSE de la probabilité d'inclusion": float(PI_4[4])}'''),
        ("c", "a number (3 decimals)", "float(HT_4)",
         '''decimals=3, mistakes={"on divise chaque valeur tirée par sa probabilité, on ne la multiplie pas":
                                     float(MULT_4),
                                 "seules les unités TIRÉES entrent dans l'estimation": float(ALL_4),
                                 "c'est l'estimateur naïf N ȳ_S, pas celui de Horvitz-Thompson": float(NAIVE_4)}'''),
        ("d", "a number", "float(NAIVE_4)",
         '''decimals=6, mistakes={"N fois la MOYENNE des valeurs tirées, pas leur somme":
                                     float(sum(Y_4[i] for i in S_4))}'''),
        ("e", "a number", "float(EXPECTATION_4)",
         '''decimals=6, mistakes={"l'espérance porte sur tous les échantillons possibles, chacun avec sa probabilité, "
                                 "pas sur celui qui a été tiré": {float(HT_4), round(float(HT_4), 3)}}'''),
        ("f", "a number (3 decimals)", "float(VAR_4)",
         '''decimals=3, mistakes={"Var(Iᵢyᵢ/πᵢ) = yᵢ² Var(Iᵢ)/πᵢ², et Var(Iᵢ) = πᵢ(1 − πᵢ) : un πᵢ se simplifie":
                                     float(VAR_PI2_4),
                                 "Var(Iᵢ) = πᵢ(1 − πᵢ) : n'oublie pas le facteur 1 − πᵢ": float(VAR_NO1_4)}'''),
        ("g", "a number (3 decimals)", "math.sqrt(VAR_4)",
         '''decimals=3, mistakes={"l'écart type est la RACINE de la variance": float(VAR_4)}'''),
        ("h", "a number (7 decimals)", "float(P_S_4)",
         '''decimals=7, mistakes={"les unités non tirées comptent aussi, chacune avec la probabilité 1 − πᵢ":
                                     float(P_IN_4)}'''),
        ("i", "a number (6 decimals)", "float(P_EMPTY_4)",
         '''decimals=6, mistakes={"l'échantillon est vide quand AUCUNE unité n'est tirée : un facteur 1 − πᵢ par "
                                 "unité": float(1 - sum(PI_4))}'''),
        ("j", "an integer (a firm numbered from 1)", "J_4",
         '''mistakes={"la plus grande valeur n'apporte pas le plus grand terme : elle est presque toujours tirée":
                         LARGEST_Y_4,
                     "compare les six termes yᵢ²(1 − πᵢ)/πᵢ": SECOND_4}'''),
    ]),

    Paper("M20.5", "Un schéma d'Euler en L pas : la jacobienne d'un pas, celle de L pas, et la limite (1 + λT/L)ᴸ", [
        ("a", "a number", "H_5", "decimals=6"),
        ("b", "a number", "FACTOR_5",
         '''decimals=6, mistakes={"λ = −1,2 est négatif : le facteur 1 + hλ est plus petit que 1":
                                     1 - H_5 * LAMBDA_5}'''),
        ("c", "a number (4 decimals)", "FACTOR_5 ** 5",
         '''decimals=4, mistakes={"x₅ = (1 + hλ)⁵ x₀ : cinq pas, cinq facteurs": FACTOR_5}'''),
        ("d", "a number (4 decimals)", "(1 + LAMBDA_5 * T_5 / 50) ** 50",
         '''decimals=4, mistakes={"h = T/L : avec L = 50 pas, chaque pas dure T/50": (1 + LAMBDA_5 / 50) ** 50,
                                 "h = T/L change avec L : pour L = 50, ce n'est plus le pas de a)": FACTOR_5 ** 50}'''),
        ("e", "a number (4 decimals)", "math.exp(LAMBDA_5 * T_5)",
         '''decimals=4, mistakes={"la limite est e^(λT), avec l'horizon T = 2": math.exp(LAMBDA_5)}'''),
        ("f", MATRIX, "ROT_STEP_5.tolist()",
         '''decimals=6, mistakes={"I + hJ garde les signes de J": ROT_STEP_5.T.tolist(),
                                 "h = T/L = 1/10 : chaque pas multiplie J par h": (np.eye(2) + J_ROT_5).tolist()}'''),
        ("g", "a number (3 decimals)", "SV_10_5",
         '''decimals=3, mistakes={"c'est la valeur singulière d'UN pas : le produit de 10 pas en a la puissance 10":
                                     math.sqrt(1 + 4 * 0.1 ** 2),
                                 "chaque pas multiplie les longueurs par √(1 + 4h²), pas par 1 + 4h²":
                                     (1 + 4 * 0.1 ** 2) ** 10}'''),
        ("h", "a number (3 decimals)", "SV_100_5",
         '''decimals=3, mistakes={"chaque pas multiplie les longueurs par √(1 + 4h²), pas par 1 + 4h²":
                                     (1 + 4 * 0.01 ** 2) ** 100}'''),
        ("i", "a number", "SV_LIMIT_5",
         '''mistakes={"la limite est e^(TJ), une rotation : relis l'exemple de la rotation (fiche §6)": 0}'''),
        ("j", MATRIX, "PEND_5.tolist()",
         '''decimals=6, mistakes={"la jacobienne d'un pas est I + h J_F : l'identité est là": (PEND_5 - np.eye(2)).tolist(),
                                 "la dérivée de −sin x est −cos x": WRONG_SIN_5.tolist(),
                                 "la dérivée de −sin x est −cos x, pas −sin x": np.round(WRONG_SIN_5, 4).tolist(),
                                 "h = 0,05 : chaque coefficient de J_F est multiplié par h":
                                     (np.eye(2) + (PEND_5 - np.eye(2)) / H_PEND_5).tolist(),
                                 "c'est J_F seule : la jacobienne d'un pas est I + h J_F":
                                     ((PEND_5 - np.eye(2)) / H_PEND_5).tolist()}'''),
        ("k", "a number", "float(np.linalg.det(PEND_5))",
         '''decimals=6, mistakes={"det [[a, b], [c, d]] = ad − bc : le produit des coefficients hors de la diagonale se "
                                 "retranche": 1 + float(PEND_5[0, 1] * PEND_5[1, 0])}'''),
    ]),

    Paper("M20.8", "Pont : où workbookIA 20 divise par une probabilité (énoncé, sans calcul)", [
        ("a", LETTER, '"C"',
         '''mistakes={"les deux normalisations divisent par un écart type, pas par une probabilité": {"A", "B"},
                     "la couche dense ne tire rien au hasard": "D"}'''),
        ("b", LETTER, '"C"',
         '''mistakes={"relis le 🔗 « Dans workbookIA » du §5 de cette fiche": {"A", "B", "D"}}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (NumPy, exact fractions)
import math
from fractions import Fraction
from itertools import product

import numpy as np
import scipy.linalg


def shape_of(array):
    """The shape of an array, written as NumPy prints it: "(12, 28)", "(5,)"."""
    return str(tuple(int(n) for n in np.shape(array)))


def fractions_list(values):
    """Exact numbers as a list: Python ints for the integers, floats for the others."""
    return [int(v) if Fraction(v).denominator == 1 else float(v) for v in values]


SHAPE_1 = (12, 28, 24)                                                                     # M20.1
T_1 = np.zeros(SHAPE_1)                      # 12 stations × 28 days × 24 hours (the values do not matter)
R_1 = T_1.reshape(12, 4, 7, 24)              # 4 weeks of 7 days
try:
    T_1 - T_1.mean(axis=1)                   # (12, 28, 24) against (12, 24)
    H_1 = False
except ValueError:
    H_1 = True
A_2 = np.array([[1, 2], [0, -1], [3, 1]])                                                   # M20.2
B_2 = np.array([[2, 0, 1], [1, -1, 4]])
M_2, X_2, Y_2 = np.array([[2, -1], [0, 3]]), np.array([1, 2]), np.array([4, -1])
MS_2 = np.array([[[1, 2], [0, 1]], [[2, 0], [1, 3]], [[0, -1], [1, 0]]])
VS_2 = np.array([[1, 1], [2, -1], [3, 2]])
FORMULA_AB_2, FORMULA_TRACE_2 = "ij,jk->ik", "ij,ji->"
AB_2, BA_2 = A_2 @ B_2, B_2 @ A_2
assert np.array_equal(np.einsum(FORMULA_AB_2, A_2, B_2), AB_2)
assert np.einsum(FORMULA_TRACE_2, A_2, B_2) == np.trace(AB_2)
COST_H_2 = 10 * 4 * 6 * 5                    # the lengths of all the letters s, i, j, k
COST_I_2 = 30 * 300 * 5 + 30 * 5 * 50        # P (30, 300), Q (300, 5), R (5, 50): PQ, then (PQ)R
COST_J_2 = 300 * 5 * 50 + 30 * 300 * 50      # QR, then P(QR)
X_3 = [Fraction(v) for v in (3, 7, 4, 9, 5, 8)]                                            # M20.3
M_3 = len(X_3)
MEAN_3 = sum(X_3) / M_3
C_3 = [[Fraction(int(i == j)) - Fraction(1, M_3) for j in range(M_3)] for i in range(M_3)]
CX_3 = [sum(C_3[i][j] * X_3[j] for j in range(M_3)) for i in range(M_3)]
TRACE_3 = sum(C_3[i][i] for i in range(M_3))
NORM2_CX_3 = sum(v * v for v in CX_3)
NORM2_MEAN_3 = M_3 * MEAN_3 ** 2
assert sum(v * v for v in X_3) == NORM2_CX_3 + NORM2_MEAN_3          # Pythagoras (König-Huygens)
S_3 = math.sqrt(NORM2_CX_3 / (M_3 - 1))
S0_3 = math.sqrt(NORM2_CX_3 / M_3)


def z_scores_3(values, ddof=1):
    """The z-scores of a series, with the standard deviation of the given ddof."""
    values = np.array([float(v) for v in values])
    return (values - values.mean()) / values.std(ddof=ddof)


Z_3, Z0_3 = z_scores_3(X_3), z_scores_3(X_3, ddof=0)
Z_I_3 = z_scores_3([Fraction(5, 2) * v - 4 for v in X_3])[5]     # the sixth coordinate
Z_J_3 = z_scores_3([-2 * v + 1 for v in X_3])[5]
K_3 = bool(np.allclose(z_scores_3([X_3[0] + 10] + X_3[1:]), Z_3))
Y_4 = [Fraction(v) for v in (2, 5, 12, 30, 8, 3)]                                          # M20.4
PI_4 = [Fraction(5, 100), Fraction(1, 10), Fraction(3, 10), Fraction(9, 10), Fraction(15, 100), Fraction(5, 100)]
S_4 = [0, 3, 5]                              # the firms 1, 4 and 6, numbered from 1 in the statement
HT_4 = sum(Y_4[i] / PI_4[i] for i in S_4)
MULT_4 = sum(Y_4[i] * PI_4[i] for i in S_4)
ALL_4 = sum(y / p for y, p in zip(Y_4, PI_4))
NAIVE_4 = len(Y_4) * sum(Y_4[i] for i in S_4) / len(S_4)
EXPECTATION_4 = sum(math.prod(p if drawn else 1 - p for drawn, p in zip(sample, PI_4))
                    * sum(y / p for drawn, y, p in zip(sample, Y_4, PI_4) if drawn)
                    for sample in product([False, True], repeat=len(Y_4)))
assert EXPECTATION_4 == sum(Y_4)             # the 64 samples, each with its probability, average to the total
VAR_4 = sum(y * y * (1 - p) / p for y, p in zip(Y_4, PI_4))
VAR_PI2_4 = sum(y * y * (1 - p) / p ** 2 for y, p in zip(Y_4, PI_4))
VAR_NO1_4 = sum(y * y / p for y, p in zip(Y_4, PI_4))
P_S_4 = math.prod(p if i in S_4 else 1 - p for i, p in enumerate(PI_4))
P_IN_4 = math.prod(PI_4[i] for i in S_4)
P_EMPTY_4 = math.prod(1 - p for p in PI_4)
TERMS_4 = [y * y * (1 - p) / p for y, p in zip(Y_4, PI_4)]
RANKS_4 = sorted(range(len(TERMS_4)), key=lambda i: TERMS_4[i], reverse=True)
J_4, SECOND_4 = RANKS_4[0] + 1, RANKS_4[1] + 1                      # the firms numbered from 1
LARGEST_Y_4 = max(range(len(Y_4)), key=lambda i: Y_4[i]) + 1
assert (J_4, SECOND_4, LARGEST_Y_4) == (5, 3, 4)
LAMBDA_5, T_5 = -1.2, 2.0                                                                  # M20.5
H_5 = T_5 / 5
FACTOR_5 = 1 + H_5 * LAMBDA_5
J_ROT_5 = np.array([[0.0, -2.0], [2.0, 0.0]])                 # the rotation, horizon T = 1
ROT_STEP_5 = np.eye(2) + J_ROT_5 / 10


def rotation_sv_5(L):
    """The singular value of (I + J/L)^L for the rotation (T = 1): both are equal."""
    values = np.linalg.svd(np.linalg.matrix_power(np.eye(2) + J_ROT_5 / L, L), compute_uv=False)
    assert math.isclose(values[0], values[1], rel_tol=1e-12)
    return float(values[0])


SV_10_5, SV_100_5 = rotation_sv_5(10), rotation_sv_5(100)
assert math.isclose(SV_10_5, 1.04 ** 5, rel_tol=1e-12)        # (1 + 4h²)^(L/2)
SV_LIMIT_5 = round(float(np.linalg.svd(scipy.linalg.expm(1.0 * J_ROT_5), compute_uv=False)[0]), 12)
assert SV_LIMIT_5 == 1                       # e^(TJ) is a rotation
X0_5, H_PEND_5 = np.array([math.pi / 3, 0.0]), 0.05     # the pendulum F(x, v) = (v, −sin x), h = 0.05
PEND_5 = np.eye(2) + H_PEND_5 * np.array([[0.0, 1.0], [-math.cos(X0_5[0]), 0.0]])
WRONG_SIN_5 = np.eye(2) + H_PEND_5 * np.array([[0.0, 1.0], [-math.sin(X0_5[0]), 0.0]])
SV_LIMIT_5 = int(SV_LIMIT_5)'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M20.1 à M20.5, 🔗 M20.8)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question (une "
               "valeur exacte se tape aussi comme une fraction, `1/8`) ;\n"
               "- une **forme** comme un tuple, `(7, 2)`, ou comme un texte, `\"(7, 2)\"` ; une forme à un seul "
               "axe s'écrit avec sa virgule, `(9,)` ;\n"
               "- une liste `[0.2, -1]` ; une matrice comme la liste de ses **lignes**, `[[1, 0], [-2, 3]]`, un "
               "nombre décimal s'y écrivant avec un point ;\n"
               "- une fraction irréductible entre guillemets, `\"3/7\"`, quand la question le dit ;\n"
               "- une formule d'`einsum` entre guillemets, `\"ab,b->a\"`, avec les lettres que l'énoncé impose (les "
               "espaces et les majuscules ne comptent pas) ;\n"
               "- une lettre entre guillemets pour un choix, `\"D\"` ; `True` ou `False` pour un vrai ou faux.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M20.10 to M20.12)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to D)
import itertools
import math

import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg

from wbm.nbtools import StopCheck, checked, drawn, filled, run_pytest_group, same, shape_text, verdict

TEST_M20 = "tests/test_m20_tensors.py"            # the tests of mymath/tensors.py'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M20")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/tensors.py`, lis la "
         "docstring du module puis celle de la fonction, remplace chaque `raise NotImplementedError(...)` par ton code, "
         "**enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. ⚠️ Le "
         "squelette n'importe rien : ajoute `import numpy as np` en tête du fichier (et `import itertools` ou "
         "`import numbers` si tu t'en sers). Ni `np.einsum`, ni `np.tensordot`, ni `np.matmul` (ni `@`), ni `np.dot`, "
         "`np.inner` ou `np.outer` dans `einsum_pair` ; ni `np.var` ni `np.std` dans `moments_along_axes` : les tests "
         "comparent tes résultats aux leurs, et un test lit ton module. Les nombres se rendent en `float` de Python, "
         "les tableaux en tableaux NumPy de flottants ; ne modifie jamais les tableaux reçus.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of tensors.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group(TEST_M20, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_M20, "{keyword}", impl="ref")')]


NOTE_10 = (r"`daily_10` coïncide avec `np.einsum` ; a) la moyenne pondérée de la station 2, le jour 4, vaut $8{,}6675$ "
           r"(la moyenne simple de la même journée, $8{,}0083$ : les heures de jour, plus chaudes, comptent double). b) "
           r'`"ij,j->i"` donne le vecteur $\mathbf{M}\mathbf{y}$, indicé par $i$ ; c) `"i,i->"` le contracte avec '
           r"$\mathbf{x}$ ; d) $\mathbf{x}^\top\mathbf{M}\mathbf{y} = 22{,}5$ (et $\mathbf{y}^\top\mathbf{M}\mathbf{x} = -16{,}5$ : "
           r"l'ordre compte). e) Vrai : le plus grand écart à "
           r"`np.matmul` est de $9 \cdot 10^{-16}$. Ta fonction fait $3 \times 5 \times 24 = 360$ multiplications pour "
           r'`daily_10` et $6 \times 3 \times 4 \times 2 = 144$ pour e). `"sdh,h->s"` somme aussi sur les jours : 5 fois '
           r"la moyenne des moyennes journalières de la station, car les poids ont pour somme 1 sur chaque journée, pas "
           r"sur la semaine. Les boucles Python paient l'interprète à chaque produit ; `np.einsum` fait les mêmes "
           r"multiplications en C.")

NOTE_11 = (r"a) L'élève 17 a 7,5 en philosophie : $z = -0{,}6288$. b) Vrai, à $4 \cdot 10^{-16}$ près : chaque colonne de "
           r"`RENOTED_11` est $a\mathbf{x} + b\mathbf{1}$ avec $a > 0$ ($a = 5$ en maths, $b = 2$ en anglais), et la "
           r"standardisation ne voit ni l'origine ni l'unité (fiche §4). c) Avec ddof = 0, $z = -0{,}6368$ : l'écart "
           r"type est multiplié par $\sqrt{39/40}$, donc chaque note standardisée par $\sqrt{40/39} \approx 1{,}012739$, "
           r"quelle que soit la case. Ajouter 2 points en anglais à un seul élève, sur 40, augmente la moyenne de "
           r"l'anglais de $\frac{2}{40} = 0{,}05$ point.")

NOTE_12 = (r"L'échantillon tiré contient les communes 3, 4 et 5 (indices NumPy) : a) $\frac{8\,600}{0{,}55} + "
           r"\frac{610}{0{,}08} + \frac{15\,400}{0{,}95} \approx 39\,471{,}89$ habitants, pour un vrai total de 33 960. b) "
           r"L'espérance sur les 256 échantillons vaut exactement $33\,960{,}00$ : l'estimateur est sans biais. La "
           r"variance par énumération, $1{,}4715 \cdot 10^8$ (un écart type de 12 131 habitants, 36 % du total), est "
           r"celle de la formule de la fiche ; la commune 3 (8 600 habitants, $\pi = 0{,}55$) en apporte 41 %, car son "
           r"terme $y_i^2\frac{1 - \pi_i}{\pi_i}$ croît comme le carré de sa taille.")

NOTE_13 = (r"a) $(3,)$ : la hauteur et la largeur disparaissent, une moyenne par canal. b) $(120, 160, 1)$ : l'axe des "
           r"canaux reste, de longueur 1. c) $(120, 160)$ : une valeur par pixel, $c$ sommé. d) $(6, 31, 24)$ : "
           r"chaque relevé moins la moyenne de sa station, diffusée. e) $(6,)$ : la somme des carrés des relevés de chaque "
           r"station. f) $(6, 744)$ : les $31 \times 24$ relevés de chaque station, dans l'ordre chronologique. g) "
           r"$(25, 25)$ : la diffusion silencieuse, toutes les différences $m_j - m_i$ ; on voulait sans doute "
           r"`NOTES_13 - NOTES_13.mean(axis=1, keepdims=True)`, de forme $(25, 4)$. h) $(31, 144)$ : une ligne par "
           r"jour, les 24 relevés de la station 0, puis ceux de la station 1, etc. ; `T_13.reshape(31, -1)` a la même "
           r"forme, mais sa première ligne contient les 144 premiers relevés de la file : les six premiers jours de la "
           r"station 0.")

NOTE_14 = (r"Les échantillons ont de 24 à 60 entreprises. Avec $\pi \propto$ effectif, l'effectif moyen des entreprises "
           r"tirées est de 125 contre 47 dans la population : c) l'estimateur naïf surestime le total de 163,2 %. "
           r"Horvitz-Thompson est sans biais dans les deux plans (biais relatifs de 0,44 % et de $-0{,}13$ %, d) à 1,7 "
           r"erreur type pour `ht_14`), mais a) son écart type relatif vaut 14,27 % avec $\pi \propto$ effectif, contre "
           r"b) 29,17 % avec $\pi$ proportionnel à l'âge ; la formule de la fiche donne 14,18 % et 29,45 %. Avec $\pi_i "
           r"\propto x_i$, $y_i/\pi_i$ ne varie que de 30 % d'une entreprise à l'autre ; avec l'âge, de 170 % : une jeune "
           r"et grande entreprise, rarement tirée, pèse énormément quand elle l'est. L'écart type qui reste pour "
           r"`ht_14` vient surtout du nombre d'entreprises tirées, environ $\frac{1}{\sqrt{40}} \approx 16$ %.")

NOTE_15 = (r"$K = \lVert\mathbf{J}\rVert_2 \approx 1{,}7401$, $KT \approx 3{,}4802$ : la borne haute vaut $e^{KT} \approx "
           r"32{,}5$, et la borne basse croît avec $L$ vers $e^{-KT} \approx 0{,}031$. a) $e^{T\mathbf{J}}$ a pour "
           r"valeurs singulières $0{,}6165$ et $0{,}4420$ (ses deux valeurs propres, de module $e^{-0{,}65} \approx "
           r"0{,}522$, ne sont pas ses valeurs singulières : $\mathbf{J}$ n'est pas symétrique). b) Pour $L = 1\,024$, "
           r"$s_{\max} \approx 0{,}6181$, à $2 \cdot 10^{-3}$ de la limite. c) Pour $L = 16$, $hK = \frac{KT}{16} "
           r"\approx 0{,}2175$ et $(1 - hK)^{16} \approx 0{,}0198$ ; la borne basse n'existe que pour $hK < 1$, ici "
           r"dès $L = 4$. Pour $L = 1$ et $2$, les pas sont si grands que le produit étire : $\lVert\mathbf{I} + "
           r"2\mathbf{J}\rVert \approx 3{,}42$, puis $2{,}64$ ; dès $L = 8$, les deux courbes sont proches de leur "
           r"limite ($0{,}9135$ et $0{,}6962$, puis $0{,}6431$ et $0{,}4666$ pour $L = 64$), et doubler $L$ ne les change "
           r"presque plus. Les bornes valent pour toute matrice de norme $K$ et ignorent la rotation : elles sont "
           r"larges, mais, à horizon fixé, la borne haute ne dépend pas de $L$, et la borne basse reste au-dessus de "
           r"$e^{-2KT}$ dès que $hK \le \frac12$. Pour l'oscillateur non linéaire, le produit des jacobiennes se "
           r"stabilise de même ($1{,}4869$ et $0{,}2099$ pour $L = 1\,024$).")

NOTE_16 = (r"(1) Sur un tableau carré, `axis=1` donne aussi 5 valeurs : la forme ne pouvait pas voir l'erreur ; il "
           r"fallait comparer les valeurs, ou essayer un tableau non carré. a) Les moyennes des matières valent $[11{,}"
           r"3333 ;\ 10{,}75 ;\ 13{,}5833]$ ; le collègue rend les 6 moyennes des élèves. (2) `T[:, 12] - T.mean(axis=1, "
           r"keepdims=True)` a la forme $(5, 5)$ : sa case $(i, j)$ est $T[j, 12] - \bar T_i$. Quatre stations au même "
           r"profil ont toutes la même moyenne et le même relevé de midi : les 16 cases sont égales, et la moyenne est "
           r"juste par chance. b) L'écart moyen de midi vaut $3{,}1258$ ; le collègue trouve $5{,}4125$. (3) `np.std` "
           r"divise par $n$ : le résultat est multiplié par $\sqrt{(n - 1)/n}$, un facteur $0{,}999995$ pour "
           r"$n = 100\,000$, invisible, mais $0{,}894$ pour 5 mesures. c) $1{,}7678$ mm, contre $1{,}5811$ chez le "
           r"collègue : un rapport $\sqrt{5/4} \approx 1{,}118$.")

NOTE_17 = (r"Pour un tableau $(n_a, n_b)$, la somme des carrés des écarts à la moyenne générale se coupe en celle des "
           r"écarts à la moyenne de chaque colonne plus $n_a$ fois celle des écarts des moyennes de colonnes à la "
           r"moyenne générale (le terme croisé est nul, puisque les écarts à une moyenne ont pour somme 0) ; divisée par "
           r"$n_an_b$, c'est la décomposition. Avec ddof = 1, les trois termes se divisent par $n_an_b - 1$, $n_a - 1$ "
           r"et $n_b - 1$, qui ne se recombinent pas : sur les 100 cas, l'écart relatif va de 0,13 à 0,75 (médiane 0,33). "
           r"Les trois fonctions fausses sont attrapées dès le premier cas, un tableau $3 \times 3$ : `wrong_count_17` "
           r"par la propriété des moyennes, `ignores_ddof_17` et `variance_of_variances_17` par la seule décomposition, "
           r"leurs moyennes étant justes. Une variance par « moyenne des carrés moins carré de la moyenne » passerait ce "
           r"test sur des valeurs de loi normale centrée ; les tests de `mymath` l'attrapent, sur des valeurs de l'ordre "
           r"de $10^8$.")

NOTE_18 = (r"Avec $n = 21$, trois communes dépassent 1 avant toute répartition ; une fois prises d'office, le reste "
           r"($n - 3$) est réparti sur des communes dont le total est plus petit, et une quatrième dépasse à son tour : a) "
           r"4 communes prises d'office ; les probabilités suivantes valent $0{,}7657$, $0{,}8321$ et $0{,}8963$. Pour "
           r"les communes qui ne sont pas prises d'office, $y_i/\pi_i$ va de 41 391 à 50 919 : chacune « vaut » à "
           r"quelques pour cent près le même nombre d'habitants, et le tirage systématique en prend exactement 17. b) "
           r"L'écart type relatif n'est que de 0,42 % (biais relatif de 0,008 %), contre c) 34,2 % avec des probabilités "
           r"égales $\frac{21}{150}$. Le tirage de Poisson de M20.14 laissait varier le nombre d'unités tirées, d'où "
           r"son écart type d'environ $\frac{1}{\sqrt{n}}$. Une grande ville qui aurait beaucoup changé depuis le "
           r"recensement ne coûterait rien si elle est prise d'office ; une commune moyenne qui aurait doublé, si.")

GIVEN_10 = '''rng_10 = np.random.default_rng(5331)
HOURS_10 = np.linspace(0.0, 23.0, 24)                          # the hours 0, 1, ..., 23
T_10 = np.round(11 + 3 * rng_10.normal(size=(3, 1, 1)) + 1.5 * rng_10.normal(size=(1, 5, 1))
                - 4 * np.cos(2 * np.pi * (HOURS_10 - 3) / 24) + rng_10.normal(0, 0.8, size=(3, 5, 24)), 1)
W_10 = np.where((HOURS_10 >= 6) & (HOURS_10 <= 21), 2.0, 1.0) / 40    # hourly weights: 6 h to 21 h count double
M_10 = np.array([[2.0, -1.0, 0.0, 3.0],
                 [1.0, 4.0, -2.0, 0.0],
                 [0.0, 2.0, 5.0, -1.0],
                 [-3.0, 0.0, 1.0, 2.0]])
X_10 = np.array([3.0, -2.0, 1.0, 0.5])
Y_10 = np.array([2.0, 1.0, -1.0, 4.0])
P_10 = rng_10.normal(size=(6, 3, 4))                            # six 3 × 4 matrices stacked along axis 0
Q_10 = rng_10.normal(size=(6, 4, 2))                            # six 4 × 2 matrices
print("T_10 :", T_10.shape, "; somme des poids W_10 :", W_10.sum())'''

M20_10 = Ex(
    "M20.10", "🔨", 2, 45, "`einsum` pour deux tableaux, avec des boucles · `einsum_pair`",
    "programmer `einsum` pour deux tableaux par des boucles sur les indices, puis s'en servir pour une moyenne "
    "pondérée le long d'un axe, une forme bilinéaire et des produits de matrices empilées.",
    "fiche §3", tracks="C, E", mymath="tensors.py", given=GIVEN_10, note=NOTE_10,
    body=HOWTO + r"""

Écris `einsum_pair(subscripts, a, b)` (fiche §3), en suivant sa docstring : le résultat de `np.einsum(subscripts, a, b)` pour **deux** tableaux, calculé par des boucles sur toutes les valeurs des indices. La formule s'écrit sous sa forme explicite, `"ij,jk->ik"` : une lettre par axe de `a`, une virgule, une lettre par axe de `b`, puis `->` et les lettres du résultat, **sans espace** (contrairement à `np.einsum`, `einsum_pair` refuse les espaces, comme le dit sa docstring). Une lettre commune à `a` et à `b` est un indice partagé (les deux axes ont la même longueur) ; une lettre absente du résultat est sommée ; les autres indicent le résultat, dans l'ordre écrit. Le résultat est un **nouveau** tableau de flottants (à 0 dimension pour `"i,i->"`) ; `ValueError` pour une formule mal écrite (pas de `->`, pas exactement une virgule, un caractère qui n'est pas une lettre), un nombre de lettres qui n'est pas le nombre d'axes du tableau, une lettre répétée dans un même tableau ou dans le résultat, une lettre du résultat absente des deux tableaux, ou une lettre commune de deux longueurs différentes.

**L'usage.** La cellule fournie donne des températures synthétiques `T_10`, de forme $(3, 5, 24)$ (3 stations, 5 jours, 24 heures), des poids horaires `W_10` de somme 1 (les heures de 6 h à 21 h comptent double), la matrice $\mathbf{M}$ et les vecteurs $\mathbf{x}$ et $\mathbf{y}$ (`M_10`, `X_10`, `Y_10`), et deux piles de matrices, `P_10` de forme $(6, 3, 4)$ et `Q_10` de forme $(6, 4, 2)$. Avec ta fonction :
- `daily_10` : les moyennes journalières pondérées $\sum_h T[s, d, h]\,w_h$, de forme $(3, 5)$, en **un** appel ;
- a) celle de la station 2, le jour 4 (indices NumPy ; la valeur que donne le calcul, sans l'arrondir) ;
- la forme bilinéaire $\mathbf{x}^\top\mathbf{M}\mathbf{y}$ en **deux** appels : le premier reçoit `M_10` puis `Y_10` (les axes de `M_10` notés `ij`, celui de `Y_10` noté `j`), le second reçoit `X_10` (son axe noté `i`) puis le résultat du premier. b) La formule du premier appel ; c) celle du second (deux textes) ; d) la valeur de $\mathbf{x}^\top\mathbf{M}\mathbf{y}$ (un nombre) ;
- e) vrai ou faux : `einsum_pair("sij,sjk->sik", P_10, Q_10)` coïncide avec `np.matmul(P_10, Q_10)` à $10^{-12}$ près (`np.allclose(..., rtol=0, atol=1e-12)`).

La vérification compare aussi `daily_10` à `np.einsum`. Dans ta copie : combien de multiplications ta fonction fait-elle pour `daily_10`, et pour e) ? Que calcule `"sdh,h->s"`, et pourquoi n'est-ce pas la moyenne pondérée de chaque station sur ses 5 jours ? Pourquoi les boucles Python sont-elles bien plus lentes que `np.einsum` pour les mêmes multiplications ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_einsum_pair_ or test_module_uses_") + [
        ("md", "**L'usage** : une moyenne pondérée le long d'un axe, une forme bilinéaire en deux contractions, des "
               "produits de matrices empilées."),
        ("todo", '''answer_M20_10b = ...  # b) a text: the formula of the first call (M_10, then Y_10)
answer_M20_10c = ...  # c) a text: the formula of the second call (X_10, then the result of the first)
daily_10 = answer_M20_10a = answer_M20_10d = answer_M20_10e = ...
with wbm.attempt("M20.10"):          # if you call einsum_pair here: ⏳ while it is not written
    daily_10 = ...        # the (3, 5) array of the weighted daily means, in one call of einsum_pair
    answer_M20_10a = ...  # a) a number, as computed (not rounded): that of station 2, day 4
    answer_M20_10d = ...  # d) a number: xᵀ M y, in two calls of einsum_pair
    answer_M20_10e = ...  # e) True or False: einsum_pair("sij,sjk->sik", P_10, Q_10) is np.matmul(P_10, Q_10)'''),
        ("check", '''with checked("M20.10"):
    if filled(daily_10):
        same("M20.10", 'einsum_pair("sdh,h->sd", T_10, W_10)', daily_10, np.einsum("sdh,h->sd", T_10, W_10))
    else:
        print("⏳ Ex M20.10 : la comparaison attend ton tableau daily_10.")
for letter, answer in zip("bc", [answer_M20_10b, answer_M20_10c]):
    wbm.check(f"M20.10{letter}", answer)
for letter, answer in zip("ade", [answer_M20_10a, answer_M20_10d, answer_M20_10e]):
    wbm.check(f"M20.10{letter}", answer, computed=True)'''),
        ("solution", '''einsum_pair = mymath.tensors.einsum_pair
daily_10 = einsum_pair("sdh,h->sd", T_10, W_10)
answer_M20_10a = float(daily_10[2, 4])
answer_M20_10b, answer_M20_10c = "ij,j->i", "i,i->"
my_10 = einsum_pair(answer_M20_10b, M_10, Y_10)                 # the vector M y, axis i
answer_M20_10d = float(einsum_pair(answer_M20_10c, X_10, my_10))
answer_M20_10e = bool(np.allclose(einsum_pair("sij,sjk->sik", P_10, Q_10), np.matmul(P_10, Q_10), rtol=0, atol=1e-12))
print("daily_10 =", np.round(daily_10, 3).tolist())
print("a)", round(answer_M20_10a, 4), "; moyenne simple de la même journée :", round(float(T_10[2, 4].mean()), 4))
print("b)", answer_M20_10b, " c)", answer_M20_10c, " d)", answer_M20_10d, "; x @ M @ y =", X_10 @ M_10 @ Y_10)
print("e)", answer_M20_10e, "; plus grand écart :", f"{np.max(np.abs(einsum_pair('sij,sjk->sik', P_10, Q_10) - P_10 @ Q_10)):.1e}")
print("multiplications : daily_10", 3 * 5 * 24, "; e)", 6 * 3 * 4 * 2, "; \\"sdh,h->s\\" :",
      np.round(einsum_pair("sdh,h->s", T_10, W_10), 3).tolist(), "= 5 fois", np.round(daily_10.mean(axis=1), 3).tolist())'''),
        ("record", '''rng_10r = np.random.default_rng(5331)
hours_10r = np.linspace(0.0, 23.0, 24)
temperatures_10r = np.round(11 + 3 * rng_10r.normal(size=(3, 1, 1)) + 1.5 * rng_10r.normal(size=(1, 5, 1))
                            - 4 * np.cos(2 * np.pi * (hours_10r - 3) / 24) + rng_10r.normal(0, 0.8, size=(3, 5, 24)), 1)
weights_10r = np.where((hours_10r >= 6) & (hours_10r <= 21), 2.0, 1.0) / 40
wbm.record("M20.10a", float(temperatures_10r[2, 4] @ weights_10r), decimals=4,
           mistakes={"une moyenne PONDÉRÉE : chaque heure compte avec son poids wₕ, pas la moyenne simple":
                         float(temperatures_10r[2, 4].mean())})
wbm.record("M20.10b", "ij,j->i",
           mistakes={"la lettre j, partagée, est sommée : elle n'apparaît pas dans le résultat": "ij,j->j",
                     "une lettre présente dans le résultat n'est pas sommée": "ij,j->ij",
                     "écris la forme explicite, avec -> et les lettres du résultat": "ij,j",
                     "c'est Mᵀy : pour My, la lettre sommée est celle des COLONNES de M": "ij,i->j"})
wbm.record("M20.10c", "i,i->",
           mistakes={"le résultat est un nombre : aucune lettre après ->": "i,i->i",
                     "écris la forme explicite, avec ->": "i,i",
                     "x et My ont le MÊME axe : une seule lettre, répétée, est sommée (deux lettres distinctes "
                     "multiplient les deux sommes)": "i,j->"})
m_10r = np.array([[2, -1, 0, 3], [1, 4, -2, 0], [0, 2, 5, -1], [-3, 0, 1, 2]])
x_10r, y_10r = np.array([3, -2, 1, 0.5]), np.array([2, 1, -1, 4])
wbm.record("M20.10d", float(x_10r @ m_10r @ y_10r), decimals=6,
           mistakes={"xᵀMy : x se contracte avec l'indice de LIGNE de M, y avec son indice de colonne":
                         float(y_10r @ m_10r @ x_10r)})
wbm.record("M20.10e", True,
           mistakes={"si einsum_pair passe ses tests, compare les deux tableaux par np.allclose(..., rtol=0, atol=1e-12)":
                         False})'''),
    ],
)

GIVEN_11 = '''rng_11 = np.random.default_rng(5333)
SUBJECTS_11 = ["maths", "physique", "histoire", "anglais", "philosophie", "sport"]
NOTES_11 = np.clip(np.round(2 * rng_11.normal([11.0, 9.5, 12.0, 13.0, 9.0, 14.0], [3.5, 4.0, 2.5, 3.0, 3.0, 2.0],
                                              size=(40, 6))) / 2, 0, 20)      # 40 pupils × 6 subjects, marks /20
RENOTED_11 = NOTES_11 * np.array([5.0, 1, 1, 1, 1, 1]) + np.array([0.0, 0, 0, 2, 0, 0])   # maths /100, English + 2
print("NOTES_11 :", NOTES_11.shape, "; moyennes des matières :", np.round(NOTES_11.mean(axis=0), 2).tolist())'''

M20_11 = Ex(
    "M20.11", "🔨", 1, 25, "Moyennes et variances le long d'axes choisis · `moments_along_axes`",
    "programmer la moyenne et la variance d'un tableau le long d'axes choisis, les axes réduits gardés, puis "
    "standardiser un tableau de notes matière par matière et vérifier ses invariances.",
    "fiche §2 et §4 ; M02c", tracks="C, E", mymath="tensors.py", given=GIVEN_11, note=NOTE_11,
    body=r"""Écris `moments_along_axes(x, axes, ddof=0)` (fiche §2), en suivant sa docstring : le couple `(mean, var)` de la moyenne et de la variance de `x` le long des axes `axes` (un entier ou un tuple d'entiers distincts ; un axe négatif compte depuis la fin), les axes réduits **gardés** avec la longueur 1, comme avec `keepdims=True`. La variance divise la somme des carrés des écarts à la moyenne par $N - \text{ddof}$, $N$ étant le nombre de valeurs réduites ensemble. Deux tableaux de flottants de même forme ; `ValueError` pour un axe hors du tableau ou répété, ou un `ddof` qui n'est pas un entier avec $0 \le \text{ddof} < N$. Elle ne centre ni ne divise `x` : elle rend seulement les deux moments.

**L'usage : standardiser des notes, matière par matière.** La cellule fournie donne les notes sur 20 de 40 élèves dans 6 matières, `NOTES_11`, de forme $(40, 6)$ (une ligne par élève, les matières dans l'ordre de `SUBJECTS_11`), et la même classe renotée, `RENOTED_11` : les maths notées sur 100 (la colonne 0 multipliée par 5) et 2 points ajoutés à tous en anglais (la colonne 3). Avec ta fonction et la diffusion :
- `Z_11` : les notes standardisées matière par matière, avec ddof = 1, $z = \frac{x - \bar x}{s}$, où $\bar x$ et $s$ sont la moyenne et l'écart type de la colonne ;
- a) `Z_11[17, 4]`, la note standardisée de l'élève 17 en philosophie (la valeur que donne le calcul, sans l'arrondir) ;
- b) vrai ou faux : la standardisation de `RENOTED_11`, faite de même, coïncide avec `Z_11` à $10^{-12}$ près (`np.allclose(..., rtol=0, atol=1e-12)`) ;
- c) la même case qu'en a), mais standardisée avec ddof = 0 (la valeur que donne le calcul, sans l'arrondir).

La vérification compare aussi `Z_11` à un calcul direct par NumPy. Dans ta copie : pourquoi b) était-il prévisible (fiche §4) ? Quel est le rapport de c) à a), et pourquoi ne dépend-il pas de la case choisie ? Si l'on ajoutait 2 points en anglais à un **seul** élève, de combien changerait la moyenne de l'anglais ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_moments_along_axes_") + [
        ("md", "**L'usage** : standardiser chaque matière, puis vérifier que la renotation ne change rien."),
        ("todo", '''Z_11 = answer_M20_11a = answer_M20_11b = answer_M20_11c = ...
with wbm.attempt("M20.11"):          # if you call moments_along_axes here: ⏳ while it is not written
    Z_11 = ...            # the (40, 6) array of the marks standardized subject by subject, ddof = 1
    answer_M20_11a = ...  # a) a number, as computed (not rounded): Z_11[17, 4]
    answer_M20_11b = ...  # b) True or False: RENOTED_11 standardized the same way gives Z_11 (atol 1e-12)
    answer_M20_11c = ...  # c) a number, as computed: the same cell, standardized with ddof = 0'''),
        ("check", '''with checked("M20.11"):
    if filled(Z_11):
        same("M20.11", "Z_11, comparé à un calcul direct par NumPy (ddof = 1, matière par matière)", Z_11,
             (NOTES_11 - NOTES_11.mean(axis=0)) / NOTES_11.std(axis=0, ddof=1))
    else:
        print("⏳ Ex M20.11 : la vérification attend ton tableau standardisé, Z_11.")
for letter, answer in zip("abc", [answer_M20_11a, answer_M20_11b, answer_M20_11c]):
    wbm.check(f"M20.11{letter}", answer, computed=True)'''),
        ("solution", '''moments_along_axes = mymath.tensors.moments_along_axes


def standardized_11(marks, ddof=1):
    """The marks standardized column by column (subject by subject), with the given ddof."""
    mean, var = moments_along_axes(marks, 0, ddof=ddof)          # shapes (1, 6): they broadcast against (40, 6)
    return (marks - mean) / np.sqrt(var)


Z_11 = standardized_11(NOTES_11)
answer_M20_11a = float(Z_11[17, 4])
answer_M20_11b = bool(np.allclose(standardized_11(RENOTED_11), Z_11, rtol=0, atol=1e-12))
answer_M20_11c = float(standardized_11(NOTES_11, ddof=0)[17, 4])
print("a)", round(answer_M20_11a, 4), "(note", NOTES_11[17, 4], ") b)", answer_M20_11b, "; plus grand écart :",
      f"{np.max(np.abs(standardized_11(RENOTED_11) - Z_11)):.1e}")
print("c)", round(answer_M20_11c, 4), "; rapport c/a :", round(answer_M20_11c / answer_M20_11a, 6), "; √(40/39) =",
      round(math.sqrt(40 / 39), 6))'''),
        ("record", '''rng_11r = np.random.default_rng(5333)
marks_11r = np.clip(np.round(2 * rng_11r.normal([11.0, 9.5, 12.0, 13.0, 9.0, 14.0], [3.5, 4.0, 2.5, 3.0, 3.0, 2.0],
                                                size=(40, 6))) / 2, 0, 20)
z1_11r = (marks_11r - marks_11r.mean(axis=0)) / marks_11r.std(axis=0, ddof=1)
z0_11r = (marks_11r - marks_11r.mean(axis=0)) / marks_11r.std(axis=0)
rows_11r = (marks_11r - marks_11r.mean(axis=1, keepdims=True)) / marks_11r.std(axis=1, ddof=1, keepdims=True)
by_var_11r = (marks_11r - marks_11r.mean(axis=0)) / marks_11r.var(axis=0, ddof=1)
wbm.record("M20.11a", float(z1_11r[17, 4]), decimals=4,
           mistakes={"ddof = 1 : la variance divise par N − 1": float(z0_11r[17, 4]),
                     "une matière est une colonne : réduis le long de l'axe 0": float(rows_11r[17, 4]),
                     "on divise par l'écart type, la RACINE de la variance": float(by_var_11r[17, 4])})
wbm.record("M20.11b", True,
           mistakes={"chaque colonne de RENOTED_11 est a x + b avec a > 0 : relis les invariances de la fiche (§4)":
                         False})
wbm.record("M20.11c", float(z0_11r[17, 4]), decimals=4,
           mistakes={"ddof = 0 : la variance divise par N": float(z1_11r[17, 4])})'''),
    ],
)

GIVEN_12 = '''Y_12 = np.array([1250.0, 430.0, 2900.0, 8600.0, 610.0, 15400.0, 3800.0, 970.0])   # the inhabitants of 8 communes
PI_12 = np.array([0.12, 0.05, 0.3, 0.55, 0.08, 0.95, 0.35, 0.1])                    # their inclusion probabilities
INCLUDED_12 = np.random.default_rng(5334).random(8) < PI_12                          # a Poisson draw
print("échantillon :", np.flatnonzero(INCLUDED_12).tolist(), "; taille moyenne :", round(PI_12.sum(), 2))'''

M20_12 = Ex(
    "M20.12", "🔨", 1, 15, "L'estimateur de Horvitz-Thompson d'un total · `horvitz_thompson_total`",
    "programmer l'estimateur de Horvitz-Thompson, puis vérifier, en énumérant tous les échantillons, qu'il est sans "
    "biais.", "fiche §5 ; M02b, R8", tracks="C", mymath="tensors.py", given=GIVEN_12, note=NOTE_12,
    body=r"""Écris `horvitz_thompson_total(values, included, inclusion_probs)` (fiche §5), en suivant sa docstring : l'estimation $\hat Y = \sum_{i \in S} y_i/\pi_i$ du total, en `float` ; `included` contient des booléens (ou des 0 et des 1) ; seules les valeurs des unités **tirées** servent (les autres peuvent être inconnues, `nan`) ; `ValueError` si les trois tableaux ne sont pas à une dimension et de même longueur, si `included` contient autre chose, ou si une probabilité n'est pas dans $]0, 1]$.

**L'usage.** La cellule fournie donne les habitants de 8 communes, `Y_12`, leurs probabilités d'inclusion, `PI_12`, et un échantillon tiré indépendamment (tirage de Poisson), `INCLUDED_12`. Avec ta fonction :
- a) l'estimation du nombre total d'habitants sur cet échantillon (la valeur que donne le calcul, sans l'arrondir) ;
- b) son espérance exacte : la somme, sur les $2^8 = 256$ échantillons possibles, de l'estimation de chacun multipliée par sa probabilité $\prod_{i \in S}\pi_i\prod_{i \notin S}(1 - \pi_i)$ (la valeur que donne le calcul, sans l'arrondir ; `itertools.product([False, True], repeat=8)` les énumère).

Dans ta copie : compare a) et b) au vrai total. Calcule aussi, par la même énumération, la variance de l'estimateur, et compare-la à la formule de la fiche. Quelle commune pèse le plus dans cette variance, et pourquoi ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_horvitz_thompson_total_") + [
        ("md", "**L'usage** : une estimation, puis son espérance sur les 256 échantillons possibles."),
        ("todo", '''answer_M20_12a = answer_M20_12b = ...
with wbm.attempt("M20.12"):          # if you call horvitz_thompson_total here: ⏳ while it is not written
    answer_M20_12a = ...  # a) a number, as computed (not rounded): the estimate of the total on INCLUDED_12
    answer_M20_12b = ...  # b) a number, as computed: its exact expectation over the 256 samples'''),
        ("check", '''for letter, answer in zip("ab", [answer_M20_12a, answer_M20_12b]):
    wbm.check(f"M20.12{letter}", answer, computed=True)
if filled(answer_M20_12b):
    verdict("M20.12", abs(answer_M20_12b - Y_12.sum()) <= 1e-9 * Y_12.sum(),
            "l'espérance vaut le total à 1e-9 près (relatif) : l'estimateur est sans biais.",
            "l'espérance n'est pas le total : chaque échantillon compte avec sa probabilité.")'''),
        ("solution", '''horvitz_thompson_total = mymath.tensors.horvitz_thompson_total
answer_M20_12a = horvitz_thompson_total(Y_12, INCLUDED_12, PI_12)
expectation_12 = second_12 = 0.0
for sample_12 in itertools.product([False, True], repeat=8):
    probability_12 = math.prod(p if drawn else 1 - p for drawn, p in zip(sample_12, PI_12))
    estimate_12 = horvitz_thompson_total(Y_12, list(sample_12), PI_12)
    expectation_12 += probability_12 * estimate_12
    second_12 += probability_12 * estimate_12 ** 2
answer_M20_12b = expectation_12
variance_12 = second_12 - expectation_12 ** 2
terms_12 = Y_12 ** 2 * (1 - PI_12) / PI_12
print("a)", round(answer_M20_12a, 2), " b)", round(answer_M20_12b, 2), "; vrai total :", Y_12.sum())
print("variance par énumération :", round(variance_12, 1), "; formule de la fiche :", round(terms_12.sum(), 1),
      "; écart type :", round(math.sqrt(variance_12), 1))
print("termes yᵢ²(1 − πᵢ)/πᵢ :", np.round(terms_12).tolist())'''),
        ("record", '''y_12r = [1250, 430, 2900, 8600, 610, 15400, 3800, 970]
pi_12r = [0.12, 0.05, 0.3, 0.55, 0.08, 0.95, 0.35, 0.1]
drawn_12r = np.random.default_rng(5334).random(8) < np.array(pi_12r)
ht_12r = sum(y / p for y, p, d in zip(y_12r, pi_12r, drawn_12r) if d)
wbm.record("M20.12a", ht_12r, decimals=2,
           mistakes={"on divise chaque valeur tirée par sa probabilité, on ne la multiplie pas":
                         sum(y * p for y, p, d in zip(y_12r, pi_12r, drawn_12r) if d),
                     "seules les unités TIRÉES entrent dans l'estimation": sum(y / p for y, p in zip(y_12r, pi_12r)),
                     "c'est l'estimateur naïf N ȳ_S, pas celui de Horvitz-Thompson":
                         8 * float(np.mean([y for y, d in zip(y_12r, drawn_12r) if d]))})
plain_12r = np.mean([sum(y / p for y, p, d in zip(y_12r, pi_12r, sample) if d)
                     for sample in itertools.product([False, True], repeat=8)])
wbm.record("M20.12b", float(sum(y_12r)), decimals=2,
           mistakes={"chaque échantillon compte avec SA probabilité, pas avec le même poids 1/256": float(plain_12r)})'''),
    ],
)

PART_A = Part("A", "Ta librairie : `einsum` par des boucles, les moments le long d'axes, Horvitz-Thompson",
              "Fiche §2 à §5. Les trois fonctions de `mymath/tensors.py`, leurs tests, et un usage de chacune.",
              given=TOOLS, exercises=[M20_10, M20_11, M20_12])

# ---------------------------------------------------------------------------
# Notebook exercises: predict, simulate, draw (M20.13 to M20.15)
# ---------------------------------------------------------------------------
GIVEN_13 = '''rng_13 = np.random.default_rng(5335)
IMG_13 = rng_13.random((120, 160, 3))                          # an image: (height, width, channels)
T_13 = np.round(rng_13.normal(12.0, 5.0, size=(6, 31, 24)), 1)  # 6 stations × 31 days × 24 hours
W_13 = np.array([2.0, -1.0, -1.0])                             # a coefficient per channel: red against the others
NOTES_13 = np.round(rng_13.uniform(4, 19, size=(25, 4)) * 2) / 2  # 25 pupils × 4 subjects'''

EXPERIMENT_13 = '''with checked("M20.13"):
    expressions_13 = [("a", "IMG_13.mean(axis=(0, 1))", lambda: IMG_13.mean(axis=(0, 1))),
                      ("b", "IMG_13.sum(axis=2, keepdims=True)", lambda: IMG_13.sum(axis=2, keepdims=True)),
                      ("c", 'np.einsum("hwc,c->hw", IMG_13, W_13)', lambda: np.einsum("hwc,c->hw", IMG_13, W_13)),
                      ("d", "T_13 - T_13.mean(axis=(1, 2), keepdims=True)",
                       lambda: T_13 - T_13.mean(axis=(1, 2), keepdims=True)),
                      ("e", 'np.einsum("sdh,sdh->s", T_13, T_13)', lambda: np.einsum("sdh,sdh->s", T_13, T_13)),
                      ("f", "T_13.reshape(6, -1)", lambda: T_13.reshape(6, -1)),
                      ("g", "NOTES_13.mean(axis=1) - NOTES_13.mean(axis=1, keepdims=True)",
                       lambda: NOTES_13.mean(axis=1) - NOTES_13.mean(axis=1, keepdims=True)),
                      ("h", "T_13.transpose(1, 0, 2).reshape(31, -1)", lambda: T_13.transpose(1, 0, 2).reshape(31, -1))]
    for letter_13, text_13, compute_13 in expressions_13:
        print(f"{letter_13}) {text_13:62} forme {compute_13().shape}")'''

M20_13 = Ex(
    "M20.13", "🔮", 1, 10, "Prédire la forme d'une réduction ou d'un einsum, puis vérifier",
    "prévoir la forme d'un tableau après une réduction, une diffusion, un `einsum` ou un remodelage, puis la voir.",
    "fiche §1 à §3", tracks="C, E", hypothesis=True, given=GIVEN_13, note=NOTE_13,
    body=r"""La cellule fournie crée quatre tableaux : une image `IMG_13` de forme $(120, 160, 3)$ (hauteur, largeur, canaux), des températures `T_13` de forme $(6, 31, 24)$ (6 stations, 31 jours, 24 heures), un coefficient par canal, `W_13`, de forme $(3,)$, et les notes `NOTES_13` de 25 élèves dans 4 matières, de forme $(25, 4)$. Prédis, **avant d'exécuter quoi que ce soit**, la forme de chaque résultat (un tuple `(7, 2)` ou un texte `"(7, 2)"` ; `(9,)` pour un seul axe) :
- a) `IMG_13.mean(axis=(0, 1))` ;
- b) `IMG_13.sum(axis=2, keepdims=True)` ;
- c) `np.einsum("hwc,c->hw", IMG_13, W_13)` ;
- d) `T_13 - T_13.mean(axis=(1, 2), keepdims=True)` ;
- e) `np.einsum("sdh,sdh->s", T_13, T_13)` ;
- f) `T_13.reshape(6, -1)` ;
- g) `NOTES_13.mean(axis=1) - NOTES_13.mean(axis=1, keepdims=True)` ;
- h) `T_13.transpose(1, 0, 2).reshape(31, -1)`.

L'expérience calcule chaque expression et affiche sa forme.

Écris tes huit prédictions, vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M20_13a = ...  # a) a shape, (7, 2) or "(7, 2)", written BEFORE the experiment: IMG_13.mean(axis=(0, 1))
prediction_M20_13b = ...  # b) IMG_13.sum(axis=2, keepdims=True)
prediction_M20_13c = ...  # c) np.einsum("hwc,c->hw", IMG_13, W_13)
prediction_M20_13d = ...  # d) T_13 - T_13.mean(axis=(1, 2), keepdims=True)
prediction_M20_13e = ...  # e) np.einsum("sdh,sdh->s", T_13, T_13)
prediction_M20_13f = ...  # f) T_13.reshape(6, -1)
prediction_M20_13g = ...  # g) NOTES_13.mean(axis=1) - NOTES_13.mean(axis=1, keepdims=True)
prediction_M20_13h = ...  # h) T_13.transpose(1, 0, 2).reshape(31, -1)''',
    check='''for letter, prediction in zip("abcdefgh", [prediction_M20_13a, prediction_M20_13b, prediction_M20_13c,
                                             prediction_M20_13d, prediction_M20_13e, prediction_M20_13f,
                                             prediction_M20_13g, prediction_M20_13h]):
    wbm.check(f"M20.13{letter}", shape_text(prediction))     # a tuple (25,) is shown as (25,), not as 25''',
    record='''img_13r, t_13r, w_13r, notes_13r = np.zeros((120, 160, 3)), np.zeros((6, 31, 24)), np.zeros(3), np.zeros((25, 4))


def shape_13r(array):
    return str(tuple(int(n) for n in array.shape))


wbm.record("M20.13a", shape_13r(img_13r.mean(axis=(0, 1))), prediction=True,
           mistakes={"les axes NOMMÉS disparaissent : axis=(0, 1) retire la hauteur et la largeur": "(120, 160)"})
wbm.record("M20.13b", shape_13r(img_13r.sum(axis=2, keepdims=True)), prediction=True,
           mistakes={"keepdims=True garde l'axe réduit, avec la longueur 1": "(120, 160)"})
wbm.record("M20.13c", shape_13r(np.einsum("hwc,c->hw", img_13r, w_13r)), prediction=True,
           mistakes={"la lettre c, absente du résultat, est sommée": "(120, 160, 3)",
                     "le résultat a les lettres écrites après ->, dans cet ordre": "(3,)"})
wbm.record("M20.13d", shape_13r(t_13r - t_13r.mean(axis=(1, 2), keepdims=True)), prediction=True,
           mistakes={"la diffusion répète la moyenne le long des axes de longueur 1 : le résultat a la forme du plus "
                     "grand tableau": "(6, 1, 1)"})
wbm.record("M20.13e", shape_13r(np.einsum("sdh,sdh->s", t_13r, t_13r)), prediction=True,
           mistakes={"les lettres absentes du résultat, d et h, sont sommées": "(6, 31, 24)"})
wbm.record("M20.13f", shape_13r(t_13r.reshape(6, -1)), prediction=True,
           mistakes={"-1 laisse NumPy calculer la longueur qui manque : le nombre d'éléments ne change pas":
                         {"(6, 31, 24)", "(6, 31)", "(6, 24)"}})
wbm.record("M20.13g", shape_13r(notes_13r.mean(axis=1) - notes_13r.mean(axis=1, keepdims=True)), prediction=True,
           mistakes={"(25,) contre (25, 1) : les formes s'alignent à droite, et chaque axe de longueur 1 est répété":
                         {"(25,)", "(25, 1)"}})
wbm.record("M20.13h", shape_13r(t_13r.transpose(1, 0, 2).reshape(31, -1)), prediction=True,
           mistakes={"reshape(31, -1) fusionne en un seul axe tous les axes qui suivent le premier": "(31, 6, 24)",
                     "transpose(1, 0, 2) échange les deux premiers axes : l'axe des jours vient d'abord": "(6, 744)"})''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes huit prédictions écrites."),
        ("todo", guarded(EXPERIMENT_13, [f"prediction_M20_13{letter}" for letter in "abcdefgh"],
                         "⏳ Écris d'abord tes huit prédictions, puis exécute à nouveau.")),
        ("solution", EXPERIMENT_13),
        ("md", "**Après l'expérience**, dans ta copie : que contient chaque résultat, en mots ? Pour g), qu'a-t-on "
               "probablement voulu calculer, et comment l'écrire ? Pour h), que contient chaque ligne, et que "
               "contiendrait la première ligne de `T_13.reshape(31, -1)`, qui a la même forme ?"),
    ],
)

GIVEN_14 = """rng_14 = np.random.default_rng(5336)
N_14 = 400                                                         # the firms
X_14 = np.round(np.exp(rng_14.normal(np.log(25), 1.2, size=N_14))) + 1      # their headcount: known
Y_14 = np.round(0.12 * X_14 * np.exp(rng_14.normal(0, 0.3, size=N_14)), 2)  # their turnover (M€): unknown
AGE_14 = np.round(rng_14.uniform(2, 30, size=N_14))                # their age, in years: known, unrelated to y
TOTAL_14 = Y_14.sum()                                              # the true total, to judge the estimators
PI_14 = np.minimum(1.0, 40 * X_14 / X_14.sum())                    # π ∝ headcount, of sum 40, capped at 1
PI_AGE_14 = PI_14.sum() * AGE_14 / AGE_14.sum()                     # π ∝ age, of the same sum
DRAWS_14 = rng_14.random((3000, N_14)) < PI_14                      # 3 000 Poisson draws with PI_14, one per row
DRAWS_AGE_14 = rng_14.random((3000, N_14)) < PI_AGE_14              # 3 000 Poisson draws with PI_AGE_14
assert DRAWS_14.sum(axis=1).min() > 0
print("Σπ =", round(PI_14.sum(), 3), "; π = 1 pour", int(np.sum(PI_14 == 1)), "entreprise(s) ; π selon l'âge : de",
      round(PI_AGE_14.min(), 4), "à", round(PI_AGE_14.max(), 4), "; vrai total :", round(TOTAL_14, 2), "M€")"""

FIGURE_14 = """rows_14 = []
for name_f14, values_f14 in (("HT, π ∝ effectif", ht_14), ("naïf N ȳ_S", naive_14), ("HT, π ∝ âge", ht_age_14)):
    values_f14 = np.asarray(values_f14, dtype=float)
    spread_f14 = values_f14.std(ddof=1) / TOTAL_14
    rows_14.append((name_f14, 100 * (values_f14.mean() / TOTAL_14 - 1), 100 * spread_f14,
                    100 * spread_f14 / math.sqrt(len(values_f14))))
if show_table_14:                                  # only once the four answers are right: it shows them
    print(f"{'estimateur':18} {'biais relatif':>14} {'écart type relatif':>19} {'erreur type':>12}")
    for name_f14, bias_f14, spread_f14, error_f14 in rows_14:
        print(f"{name_f14:18} {bias_f14:13.2f} % {spread_f14:17.2f} % {error_f14:10.2f} %")
else:
    print("ℹ️ Le tableau des biais et des écarts types relatifs s'affichera quand tes quatre réponses seront justes.")
fig, axes = plt.subplots(1, 3, figsize=(13.5, 3.8), sharex=True)
try:
    for ax, (name_f14, values_f14), color_f14 in zip(axes, (("HT, π ∝ effectif", ht_14), ("naïf N ȳ_S, π ∝ effectif",
                                                                                          naive_14),
                                                            ("HT, π ∝ âge", ht_age_14)), ("C0", "C3", "C2")):
        ax.hist(np.asarray(values_f14, dtype=float), bins=60, color=color_f14, alpha=0.75)
        ax.axvline(TOTAL_14, color="k", ls="--", lw=1.2, label="vrai total")
        ax.set_title(name_f14, fontsize=10)
        ax.set_xlabel("estimation du total (M€)")
        ax.legend(fontsize=8)
    axes[0].set_ylabel("nombre d'échantillons")
except BaseException:
    plt.close(fig)
    raise
plt.show()"""

CHECK_14 = """with checked("M20.14"):
    if not filled(ht_14, naive_14, ht_age_14):
        print("⏳ Ex M20.14 : le tableau et la figure attendent tes trois tableaux, ht_14, naive_14 et ht_age_14.")
        raise StopCheck
    want_14 = {"ht_14": DRAWS_14 @ (Y_14 / PI_14),
               "naive_14": N_14 * (DRAWS_14 @ Y_14) / DRAWS_14.sum(axis=1),
               "ht_age_14": DRAWS_AGE_14 @ (Y_14 / PI_AGE_14)}
    ok_14 = [same("M20.14", f"{name} (une estimation par ligne de {rows})", got, want_14[name], rtol=1e-9, atol=1e-9)
             for name, rows, got in (("ht_14", "DRAWS_14", ht_14), ("naive_14", "DRAWS_14", naive_14),
                                     ("ht_age_14", "DRAWS_AGE_14", ht_age_14))]
    if not all(ok_14):
        raise StopCheck
""" + "\n".join("    " + line if line else "" for line in FIGURE_14.splitlines())

M20_14 = Ex(
    "M20.14", "🔬", 2, 20, "Simuler un sondage : Horvitz-Thompson contre la moyenne naïve, biais et variance",
    "mesurer par la simulation le biais et l'écart type de trois estimateurs d'un total, et voir ce que des "
    "probabilités proportionnelles à une taille bien choisie apportent.", "fiche §5 ; Ex M20.12", tracks="C",
    given=GIVEN_14, note=NOTE_14,
    body=r"""Une population de $N = 400$ entreprises (cellule fournie) : leur effectif $x_i$ et leur âge, connus (`X_14`, très dispersé : quelques grandes, beaucoup de petites ; `AGE_14`, de 2 à 30 ans, sans lien avec leur taille), et leur chiffre d'affaires $y_i$ en millions d'euros, à peu près proportionnel à l'effectif, que l'on veut estimer sans le connaître (`Y_14` ; le vrai total est `TOTAL_14`). Deux plans de sondage, chacun en tirage de Poisson, à probabilités inégales :
- `PI_14` : des probabilités proportionnelles à l'effectif, de somme 40, plafonnées à 1 (une entreprise atteint le plafond : la somme est un peu sous 40) ;
- `PI_AGE_14` : des probabilités proportionnelles à l'âge, de même somme.

La cellule fournie tire 3 000 échantillons avec chacun : `DRAWS_14` et `DRAWS_AGE_14`, deux tableaux de booléens de forme $(3\,000, 400)$, un échantillon par ligne. Calcule trois tableaux de 3 000 estimations du total, une par ligne, dans l'ordre des lignes :
- `ht_14` : Horvitz-Thompson avec `PI_14`, sur `DRAWS_14`, par ta `horvitz_thompson_total` ;
- `naive_14` : l'estimateur naïf $N\,\bar y_S$ (400 fois la moyenne des $y_i$ tirés), sur les mêmes échantillons `DRAWS_14` ;
- `ht_age_14` : Horvitz-Thompson avec `PI_AGE_14`, sur `DRAWS_AGE_14`.

Pour un estimateur, le **biais relatif** est $\frac{m}{Y} - 1$ et l'**écart type relatif** $\frac{s}{Y}$, où $m$ et $s$ sont la moyenne et l'écart type (ddof = 1) de ses 3 000 estimations ; l'**erreur type** de Monte-Carlo du biais relatif est $\frac{s}{Y\sqrt{3\,000}}$. La cellule de vérification vérifie d'abord tes réponses, compare tes tableaux aux estimations attendues et trace les trois histogrammes, avec le vrai total ; une fois tes quatre réponses justes, elle affiche ces trois nombres pour chaque estimateur.

Réponds, en pourcentages (la valeur que donne le calcul, sans l'arrondir) :
- a) l'écart type relatif de `ht_14` ;
- b) celui de `ht_age_14` ;
- c) le biais relatif de `naive_14` ;
- d) vrai ou faux : le biais relatif de `ht_14` est, en valeur absolue, inférieur à 3 erreurs types.""",
    todo="""ht_14 = naive_14 = ht_age_14 = ...
answer_M20_14a = answer_M20_14b = answer_M20_14c = answer_M20_14d = ...
with wbm.attempt("M20.14"):          # horvitz_thompson_total: ⏳ while it is not written
    ht_14 = ...           # the 3 000 Horvitz-Thompson estimates with PI_14, one per row of DRAWS_14
    naive_14 = ...        # the 3 000 naive estimates N ȳ_S on the same rows
    ht_age_14 = ...       # the 3 000 Horvitz-Thompson estimates with PI_AGE_14, one per row of DRAWS_AGE_14
    answer_M20_14a = ...  # a) a number, as computed (not rounded): the relative standard deviation of ht_14, in %
    answer_M20_14b = ...  # b) a number, as computed: that of ht_age_14, in %
    answer_M20_14c = ...  # c) a number, as computed: the relative bias of naive_14, in %
    answer_M20_14d = ...  # d) True or False: |relative bias of ht_14| < 3 standard errors""",
    check="""right_14 = [wbm.check(f"M20.14{letter}", answer, computed=True)
            for letter, answer in zip("abcd", [answer_M20_14a, answer_M20_14b, answer_M20_14c, answer_M20_14d])]
show_table_14 = all(right_14)

""" + CHECK_14,
    solution="""horvitz_thompson_total = mymath.tensors.horvitz_thompson_total
ht_14 = np.array([horvitz_thompson_total(Y_14, row, PI_14) for row in DRAWS_14])
naive_14 = np.array([N_14 * Y_14[row].mean() for row in DRAWS_14])
ht_age_14 = np.array([horvitz_thompson_total(Y_14, row, PI_AGE_14) for row in DRAWS_AGE_14])


def relative_14(values):
    \"\"\"(relative bias, relative standard deviation, standard error of the bias), as fractions of the total.\"\"\"
    spread = values.std(ddof=1) / TOTAL_14
    return values.mean() / TOTAL_14 - 1, spread, spread / math.sqrt(len(values))


bias_14, spread_14, error_14 = relative_14(ht_14)
answer_M20_14a = 100 * spread_14
answer_M20_14b = 100 * relative_14(ht_age_14)[1]
answer_M20_14c = 100 * relative_14(naive_14)[0]
answer_M20_14d = bool(abs(bias_14) < 3 * error_14)
sizes_14 = DRAWS_14.sum(axis=1)
print("taille des échantillons : de", sizes_14.min(), "à", sizes_14.max(), "; effectif moyen tiré :",
      round(float(np.mean([X_14[row].mean() for row in DRAWS_14])), 1), "contre", round(X_14.mean(), 1),
      "dans la population")
for label_14, pi_s14 in (("π ∝ effectif", PI_14), ("π ∝ âge", PI_AGE_14)):
    ratios_14 = Y_14 / pi_s14
    print(f"yᵢ/πᵢ, {label_14} : écart type relatif sur la population {np.std(ratios_14) / np.mean(ratios_14):.3f} ; "
          f"variance de la fiche : écart type relatif {math.sqrt(np.sum(Y_14 ** 2 * (1 - pi_s14) / pi_s14)) / TOTAL_14:.4f}")
print("biais relatif de ht_14 :", f"{100 * bias_14:.2f} %, soit {bias_14 / error_14:.2f} erreurs types ; de ht_age_14 :",
      f"{100 * relative_14(ht_age_14)[0]:.2f} %")
show_table_14 = True

""" + CHECK_14,
    record="""rng_14r = np.random.default_rng(5336)
x_14r = np.round(np.exp(rng_14r.normal(np.log(25), 1.2, size=400))) + 1
y_14r = np.round(0.12 * x_14r * np.exp(rng_14r.normal(0, 0.3, size=400)), 2)
age_14r = np.round(rng_14r.uniform(2, 30, size=400))
pi_14r = np.minimum(1.0, 40 * x_14r / x_14r.sum())
pi_age_14r = pi_14r.sum() * age_14r / age_14r.sum()
draws_14r = rng_14r.random((3000, 400)) < pi_14r
draws_age_14r = rng_14r.random((3000, 400)) < pi_age_14r
total_14r = y_14r.sum()
ht_14r = (draws_14r * (y_14r / pi_14r)).sum(axis=1)
naive_14r = 400 * (draws_14r * y_14r).sum(axis=1) / draws_14r.sum(axis=1)
age_ht_14r = (draws_age_14r * (y_14r / pi_age_14r)).sum(axis=1)
wbm.record("M20.14a", 100 * ht_14r.std(ddof=1) / total_14r, decimals=2,
           mistakes={"l'écart type des estimations de ht_14, pas celui de ht_age_14":
                         100 * age_ht_14r.std(ddof=1) / total_14r})
wbm.record("M20.14b", 100 * age_ht_14r.std(ddof=1) / total_14r, decimals=2,
           mistakes={"l'écart type des estimations de ht_age_14, pas celui de ht_14": 100 * ht_14r.std(ddof=1) / total_14r})
wbm.record("M20.14c", 100 * (naive_14r.mean() / total_14r - 1), decimals=1,
           mistakes={"le biais relatif est m/Y − 1, en % : retire 1 avant de multiplier par 100":
                         100 * naive_14r.mean() / total_14r})
assert abs(ht_14r.mean() / total_14r - 1) < 3 * ht_14r.std(ddof=1) / total_14r / math.sqrt(3000)
wbm.record("M20.14d", True,
           mistakes={"compare |m/Y − 1| à 3 s/(Y√3 000), avec les estimations de ht_14": False})""",
    after=[
        ("md", "**Après la figure**, dans ta copie : pourquoi l'estimateur naïf surestime-t-il autant (compare "
               "l'effectif moyen des entreprises tirées à celui de la population) ? Les deux estimateurs de "
               "Horvitz-Thompson sont sans biais : pourquoi `ht_14` est-il deux fois plus précis que `ht_age_14` ? "
               "Que vaut à peu près $y_i/\\pi_i$ avec $\\pi_i \\propto x_i$, et avec $\\pi_i$ proportionnel à l'âge "
               "(une jeune et grande entreprise, si elle est tirée) ? D'où vient l'écart type qui reste pour `ht_14` "
               "(pense au nombre d'entreprises tirées, qui change d'un échantillon à l'autre) ? Le défi M20.18 le fait "
               "disparaître."),
    ],
)

GIVEN_15 = '''J_15 = np.array([[-0.3, -1.7],
                 [0.95, -0.35]])                # a rotation and a contraction
T_15 = 2.0                                      # the horizon
LS_15 = [2 ** k for k in range(11)]             # L = 1, 2, 4, ..., 1024'''

CHECK_15 = '''with checked("M20.15"):
    def report_15(ok, success, failure):
        \"\"\"One ✅ line, or one ❌ line that stops the check there (the figure is still shown).\"\"\"
        print(("✅ " + success) if ok else ("❌ " + failure))
        if not ok:
            raise StopCheck

    K_c15 = np.linalg.norm(J_15, 2)
    values_c15 = np.array([np.linalg.svd(np.linalg.matrix_power(np.eye(2) + (T_15 / L) * J_15, L), compute_uv=False)
                           for L in LS_15])
    limit_c15 = np.linalg.svd(scipy.linalg.expm(T_15 * J_15), compute_uv=False)
    lower_c15 = [(L, (1 - T_15 / L * K_c15) ** L) for L in LS_15 if T_15 / L * K_c15 < 1]
    fig_15, ax_15 = plt.subplots(figsize=(7.5, 4.8))
    try:
        opened_15 = drawn(draw_products, ax_15, J_15.copy(), T_15, list(LS_15))
        lines_15 = [(np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float),
                     line.get_linestyle()) for line in ax_15.lines]

        def line_through_15(points, dashed=False):
            \"\"\"The (xs, ys) of the first line of ax that passes by all the points (x, y), dashed or dotted when
            asked; None when there is none.\"\"\"
            for xs, ys, style in lines_15:
                if dashed and style not in ("--", ":", "-."):
                    continue
                if xs.shape == ys.shape and all(np.any(np.isclose(xs, x, rtol=1e-9) & np.isclose(ys, y, rtol=1e-6))
                                                for x, y in points):
                    return xs, ys
            return None

        def level_15(value, dashed=False):
            \"\"\"True when one line of ax is horizontal at value (ax.axhline, or a constant line).\"\"\"
            return any(ys.size >= 2 and np.all(np.isclose(ys[np.isfinite(ys)], value, rtol=1e-6))
                       and (not dashed or style in ("--", ":", "-.")) for _, ys, style in lines_15)

        report_15(not opened_15, "draw_products dessine dans l'axe reçu",
                  "draw_products doit dessiner dans l'axe reçu, sans ouvrir de figure (ni plt.figure ni plt.subplots)")
        report_15(line_through_15(list(zip(LS_15, values_c15[:, 0]))) is not None
                  and line_through_15(list(zip(LS_15, values_c15[:, 1]))) is not None,
                  "les deux valeurs singulières du produit sont tracées en fonction de L",
                  "il manque une courbe des valeurs singulières du produit (I + (T/L) J)^L : une ligne par valeur "
                  "singulière, une valeur par L de Ls")
        report_15(level_15(limit_c15[0]) and level_15(limit_c15[1]),
                  "les deux valeurs singulières de exp(TJ) sont des droites horizontales",
                  "il manque une droite horizontale aux valeurs singulières de scipy.linalg.expm(T * J) (ax.axhline)")
        report_15(level_15(math.exp(K_c15 * T_15), dashed=True), "la borne e^(KT) est en pointillés",
                  "il manque la borne e^(KT), K = np.linalg.norm(J, 2), en pointillés (ls=\\"--\\")")
        lower_line_15 = line_through_15(lower_c15, dashed=True)
        report_15(lower_line_15 is not None, "la borne (1 − hK)^L est en pointillés, aux L où hK < 1",
                  "il manque la borne (1 − hK)^L, h = T/L, en pointillés, aux L de Ls pour lesquels hK < 1")
        outside_15 = sorted({int(x) if float(x).is_integer() else float(x) for x, y in zip(*lower_line_15)
                             if np.isfinite(y) and (x <= 0 or T_15 / x * K_c15 >= 1)})
        report_15(not outside_15, "la borne (1 − hK)^L n'est tracée qu'aux L où hK < 1",
                  f"la borne (1 − hK)^L est aussi tracée pour L = {outside_15}, où hK ≥ 1 : la fiche ne la donne que "
                  "pour hK < 1, ne la trace qu'à ces L")
        report_15(ax_15.get_xscale() == "log", "L est en échelle logarithmique",
                  "mets L en échelle logarithmique : ax.set_xscale(\\"log\\", base=2)")
    except StopCheck:
        plt.show()
        raise
    except BaseException:
        plt.close(fig_15)
        raise
    plt.show()
    verdict("M20.15", True, "les deux courbes, leurs limites et les deux bornes sont dessinées.", "")'''

M20_15 = Ex(
    "M20.15", "🎨", 1, 20, "Le produit de L jacobiennes I + hJ : ses valeurs singulières extrêmes quand L grandit, à "
    "hL fixé",
    "dessiner les valeurs singulières de $(\\mathbf{I} + \\frac TL\\mathbf{J})^L$ quand $L$ grandit à horizon fixé, "
    "leur limite $e^{T\\mathbf{J}}$ et les deux bornes de la fiche.", "fiche §6 ; M12d, M14", tracks="C, E",
    given=GIVEN_15, note=NOTE_15,
    body=r"""Un pas d'Euler pour $\mathbf{x}' = \mathbf{J}\mathbf{x}$ multiplie par $\mathbf{I} + h\mathbf{J}$ ; $L$ pas de durée $h = T/L$, à horizon $T$ fixé, multiplient par $(\mathbf{I} + \frac TL\mathbf{J})^L$, qui tend vers $e^{T\mathbf{J}}$ quand $L$ grandit (fiche §6). La cellule fournie donne $\mathbf{J} = \begin{pmatrix} -0{,}3 & -1{,}7 \\ 0{,}95 & -0{,}35 \end{pmatrix}$ (`J_15` : une rotation et une contraction), l'horizon $T = 2$ (`T_15`) et les onze nombres de pas $L = 1, 2, 4, \ldots, 1\,024$ (`LS_15`).

Écris `draw_products(ax, J, T, Ls)`, qui dessine dans l'axe `ax` (sans en ouvrir d'autre) :
- les deux valeurs singulières de $(\mathbf{I} + \frac TL\mathbf{J})^L$ en fonction de $L$, chacune par **une** ligne avec des points, une valeur par $L$ de `Ls`, dans l'ordre (`np.linalg.matrix_power`, puis `np.linalg.svd(..., compute_uv=False)`, qui les rend en ordre décroissant) ;
- les deux valeurs singulières de $e^{T\mathbf{J}}$ (`scipy.linalg.expm`), par deux droites horizontales (`ax.axhline`) ;
- en pointillés (`ls="--"`), les bornes de la fiche, avec $K = \lVert\mathbf{J}\rVert_2$ (`np.linalg.norm(J, 2)`) : la droite horizontale $e^{KT}$, et $(1 - hK)^L$ aux seuls $L$ de `Ls` pour lesquels $hK < 1$ (une ligne) ;
- $L$ en échelle logarithmique (`ax.set_xscale("log", base=2)`) ; une échelle logarithmique en ordonnée aussi, une légende et un titre.

Réponds :
- a) les deux valeurs singulières de $e^{T\mathbf{J}}$, en ordre décroissant (une liste, 4 décimales) ;
- b) la plus grande valeur singulière du produit pour $L = 1\,024$ (4 décimales) ;
- c) la borne $(1 - hK)^L$ pour $L = 16$, avec $h = T/L$ (4 décimales).

La vérification appelle ta fonction et regarde le dessin, dans cet ordre, en s'arrêtant au premier ❌ : les deux courbes, les deux droites de $e^{T\mathbf{J}}$, les deux bornes en pointillés (la borne basse aux seuls $L$ où $hK < 1$) et l'échelle logarithmique en $L$.""",
    todo='''def draw_products(ax, J, T, Ls):
    """In ax (and no other axes): the two singular values of (I + (T/L) J)^L against L (one line each, one point per
    L of Ls), those of expm(T J) as horizontal lines, the bounds e^(KT) and (1 − hK)^L (where hK < 1) dashed,
    K = ‖J‖₂ and h = T/L; L on a log scale."""
    raise NotImplementedError("draw_products n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M20_15a = ...  # a) a list of 2 numbers (4 decimals), decreasing: the singular values of expm(T_15 * J_15)
answer_M20_15b = ...  # b) a number (4 decimals): the largest singular value of the product for L = 1024
answer_M20_15c = ...  # c) a number (4 decimals): the bound (1 − hK)^L for L = 16''',
    check='''for letter, answer in zip("abc", [answer_M20_15a, answer_M20_15b, answer_M20_15c]):
    wbm.check(f"M20.15{letter}", answer)
if filled(answer_M20_15a, answer_M20_15b):
    verdict("M20.15", abs(answer_M20_15b - answer_M20_15a[0]) < 1e-2,
            "pour L = 1 024, la plus grande valeur singulière du produit est à moins de 1e-2 de celle de exp(TJ).",
            "pour L = 1 024, le produit devrait être à moins de 1e-2 de exp(TJ) : relis a) et b).")

''' + CHECK_15,
    solution='''def draw_products(ax, J, T, Ls):
    """In ax (and no other axes): the two singular values of (I + (T/L) J)^L against L (one line each, one point per
    L of Ls), those of expm(T J) as horizontal lines, the bounds e^(KT) and (1 − hK)^L (where hK < 1) dashed,
    K = ‖J‖₂ and h = T/L; L on a log scale."""
    J = np.asarray(J, dtype=float)
    K = np.linalg.norm(J, 2)
    identity = np.eye(len(J))
    values = np.array([np.linalg.svd(np.linalg.matrix_power(identity + (T / L) * J, L), compute_uv=False) for L in Ls])
    limit = np.linalg.svd(scipy.linalg.expm(T * J), compute_uv=False)
    ax.plot(Ls, values[:, 0], "o-", color="C0", label="$s_{\\\\max}$ du produit")
    ax.plot(Ls, values[:, -1], "s-", color="C1", label="$s_{\\\\min}$ du produit")
    ax.axhline(limit[0], color="C0", lw=0.8, label="$s_{\\\\max}$ de exp(TJ)")
    ax.axhline(limit[-1], color="C1", lw=0.8, label="$s_{\\\\min}$ de exp(TJ)")
    ax.axhline(math.exp(K * T), color="C3", ls="--", label="borne e^(KT)")
    lower = [(L, (1 - T / L * K) ** L) for L in Ls if T / L * K < 1]
    ax.plot([L for L, _ in lower], [v for _, v in lower], "--", color="C2", marker=".", label="borne (1 − hK)^L")
    ax.set_xscale("log", base=2)
    ax.set_yscale("log")
    ax.set_xlabel("nombre de pas L (échelle log)")
    ax.set_ylabel("valeur singulière (échelle log)")
    ax.set_title(f"(I + (T/L) J)^L à horizon T = {T:g} : K = {K:.3f}", fontsize=10)
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=7, loc="center right")


K_15 = np.linalg.norm(J_15, 2)
answer_M20_15a = np.linalg.svd(scipy.linalg.expm(T_15 * J_15), compute_uv=False).tolist()
answer_M20_15b = float(np.linalg.svd(np.linalg.matrix_power(np.eye(2) + (T_15 / 1024) * J_15, 1024), compute_uv=False)[0])
answer_M20_15c = (1 - T_15 / 16 * K_15) ** 16
print("K =", round(K_15, 4), "; KT =", round(K_15 * T_15, 4), "; e^(KT) =", round(math.exp(K_15 * T_15), 3),
      "; e^(−KT) =", round(math.exp(-K_15 * T_15), 4))
print("a)", np.round(answer_M20_15a, 4).tolist(), "; valeurs propres de J :", np.round(np.linalg.eigvals(J_15), 4).tolist(),
      "; e^(T Re λ) =", round(math.exp(T_15 * np.linalg.eigvals(J_15).real[0]), 4))
print("b)", round(answer_M20_15b, 4), " c)", round(answer_M20_15c, 4), "; hK =", round(T_15 / 16 * K_15, 4),
      "; la borne basse existe dès L =", min(L for L in LS_15 if T_15 / L * K_15 < 1))
for L in (1, 2, 4, 8, 64, 1024):
    print(f"L = {L:4d} :", np.round(np.linalg.svd(np.linalg.matrix_power(np.eye(2) + (T_15 / L) * J_15, L),
                                                  compute_uv=False), 4).tolist())

''' + CHECK_15,
    record='''j_15r = np.array([[-0.3, -1.7], [0.95, -0.35]])
limit_15r = np.linalg.svd(scipy.linalg.expm(2.0 * j_15r), compute_uv=False)
eigen_15r = np.abs(np.linalg.eigvals(scipy.linalg.expm(2.0 * j_15r)))
wbm.record("M20.15a", limit_15r.tolist(), decimals=4,
           mistakes={"en ordre DÉCROISSANT, comme les rend np.linalg.svd": limit_15r[::-1].tolist(),
                     "les modules des valeurs propres de exp(TJ) ne sont pas ses valeurs singulières : J n'est pas "
                     "symétrique": eigen_15r.tolist()})
product_15r = np.linalg.svd(np.linalg.matrix_power(np.eye(2) + (2.0 / 1024) * j_15r, 1024), compute_uv=False)
wbm.record("M20.15b", float(product_15r[0]), decimals=4,
           mistakes={"le produit pour L = 1 024, pas sa limite exp(TJ)": float(limit_15r[0]),
                     "la PLUS GRANDE valeur singulière du produit": float(product_15r[1])})
k_15r = np.linalg.norm(j_15r, 2)
h_15r = 2.0 / 16
wbm.record("M20.15c", (1 - h_15r * k_15r) ** 16, decimals=4,
           mistakes={"la borne BASSE est (1 − hK)^L : le signe moins": (1 + h_15r * k_15r) ** 16,
                     "la borne pour L = 16, pas sa limite quand L grandit": math.exp(-2.0 * k_15r),
                     "h = T/L = 2/16 : n'oublie pas l'horizon T": (1 - k_15r / 16) ** 16})''',
    after=[
        ("md", "**Pour aller plus loin** (facultatif). Le même dessin pour un champ non linéaire, l'oscillateur amorti "
               "$F(x, v) = (v,\\ -x - x^3 - 0{,}3\\,v)$ depuis $(1{,}2 ;\\ 0)$, à horizon $T = 4$ : pour chaque $L$, "
               "le produit des jacobiennes $\\mathbf{I} + h\\mathbf{J}_F(\\mathbf{x}_k)$ le long des points d'Euler "
               "$\\mathbf{x}_0, \\ldots, \\mathbf{x}_{L-1}$, celle du dernier pas à gauche (fiche §6). Le notebook de "
               "solutions le trace.\n\n"
               "**Dans ta copie** : pourquoi les deux courbes se stabilisent-elles quand $L$ grandit, alors que le "
               "nombre de facteurs double d'un point au suivant ? Pourquoi les valeurs singulières dépassent-elles 1 "
               "pour $L = 1$ et $L = 2$ (calcule $\\lVert\\mathbf{I} + 2\\mathbf{J}\\rVert$), et pourquoi les bornes "
               "sont-elles si loin des courbes ?"),
        ("solution", '''def field_15(state):
    """The damped non-linear oscillator F(x, v) = (v, −x − x³ − 0.3 v)."""
    x, v = state
    return np.array([v, -x - x ** 3 - 0.3 * v])


def jacobian_15(state):
    """The Jacobian of field_15 at state."""
    x, _ = state
    return np.array([[0.0, 1.0], [-1.0 - 3.0 * x ** 2, -0.3]])


def euler_product_15(L, horizon=4.0, start=(1.2, 0.0)):
    """The product of the L Jacobians I + h J_F(x_k) along the Euler points, the last step on the left."""
    h, state, product_ = horizon / L, np.array(start, dtype=float), np.eye(2)
    for _ in range(L):
        product_ = (np.eye(2) + h * jacobian_15(state)) @ product_
        state = state + h * field_15(state)
    return product_


values_n15 = np.array([np.linalg.svd(euler_product_15(L), compute_uv=False) for L in LS_15])
fig, ax = plt.subplots(figsize=(7.0, 4.2))
ax.plot(LS_15, values_n15[:, 0], "o-", label="$s_{\\\\max}$ du produit")
ax.plot(LS_15, values_n15[:, 1], "s-", label="$s_{\\\\min}$ du produit")
ax.set_xscale("log", base=2)
ax.set_yscale("log")
ax.set_xlabel("nombre de pas L (échelle log)")
ax.set_ylabel("valeur singulière (échelle log)")
ax.set_title("oscillateur amorti non linéaire, T = 4 : le produit des jacobiennes le long des points d'Euler",
             fontsize=9)
ax.grid(True, which="both", alpha=0.3)
ax.legend(fontsize=8)
plt.show()
print("L = 1 024 :", np.round(values_n15[-1], 4).tolist(), "; L = 512 :", np.round(values_n15[-2], 4).tolist())'''),
    ],
)

PART_B = Part("B", "Prédire, simuler, dessiner",
              "Fiche §1, §3, §5 et §6. Les formes de huit expressions, prédites puis vues ; trois estimateurs d'un total "
              "comparés par la simulation ; le produit de $L$ pas d'Euler à horizon fixé.",
              exercises=[M20_13, M20_14, M20_15])

# ---------------------------------------------------------------------------
# Notebook exercises: debug and test (M20.16, M20.17)
# ---------------------------------------------------------------------------
GIVEN_C = ('ref_tensors = wbm.load_mymath("ref", alias="mymath_ref").tensors   # the reference: the check of M20.17')

GIVEN_16 = '''NOTES_16 = np.array([[12.0, 8.5, 15.0],
                     [9.5, 11.0, 13.0],
                     [14.0, 10.0, 16.5],
                     [7.0, 12.5, 11.0],
                     [15.5, 9.0, 14.0],
                     [10.0, 13.5, 12.0]])            # 6 pupils × 3 subjects
HOURS_16 = np.linspace(0.0, 23.0, 24)
rng_16 = np.random.default_rng(5332)
T_16 = np.round(np.array([[8.0], [12.5], [5.0], [15.0], [10.0]])
                + np.array([[3.0], [6.0], [2.0], [8.0], [4.5]]) * np.cos(2 * np.pi * (HOURS_16 - [[14], [15], [13], [16], [14]]) / 24)
                + rng_16.normal(0, 0.5, size=(5, 24)), 1)    # one day of 5 stations, hour by hour
SMALL_16 = np.array([12.5, 14.0, 9.5, 11.0, 13.0])     # five repeated measurements of one length, in mm


# The colleague's code
def subject_means_16(notes):
    """The mean of each subject of a table (pupils, subjects): one value per subject."""
    return notes.mean(axis=1)


def noon_gap_16(T):
    """T of shape (stations, 24): one day, hour by hour. The mean, over the stations, of |T[s, 12] − daily mean of s|."""
    return float(np.mean(np.abs(T[:, 12] - T.mean(axis=1, keepdims=True))))


def sample_sd_16(x):
    """The standard deviation of a sample: the square root of its unbiased variance (ddof = 1)."""
    return float(np.std(x))


# The colleague's checks: all pass
square_16 = np.round(np.random.default_rng(5332).uniform(5, 18, size=(5, 5)), 1)
print("(1) forme des moyennes d'un tableau de 5 élèves et 5 matières :", subject_means_16(square_16).shape,
      "(attendu (5,))")
profile_16 = 10 + 4 * np.cos(2 * np.pi * (HOURS_16 - 14) / 24)
print("(2) quatre stations au même profil :", round(noon_gap_16(np.tile(profile_16, (4, 1))), 6), "; attendu",
      round(abs(profile_16[12] - profile_16.mean()), 6))
print("(3) 100 000 tirages d'écart type 2 :", round(sample_sd_16(np.random.default_rng(5332).normal(15, 2, 100_000)), 2))'''

CHECK_16 = '''results_16, parts_16 = [], []


def report_16(ok, success, failure):
    results_16.append(bool(ok))
    print(("✅ " + success) if ok else ("❌ " + failure))


def call_16(part, name, function, *args):
    """function(*args); an error of the learner's code becomes one ❌ line that names the function (the check of this
    part stops there, the final verdict stays)."""
    try:
        return function(*args)
    except NotImplementedError:
        raise
    except Exception as exc:  # noqa: BLE001 - the learner's error, reported with the name of the function
        report_16(False, "", f"({part}) {name} : ton code lève {type(exc).__name__} : {str(exc)[:200]}")
        parts_16.append(part)
        raise StopCheck from None


def close_16(got, want):
    """True when got is a number (or an array of numbers) of the shape of want, equal to it up to rounding."""
    try:
        got = np.asarray(got, dtype=float)
    except (TypeError, ValueError):
        return False
    return got.shape == np.shape(want) and bool(np.allclose(got, want, rtol=1e-9, atol=1e-12))


with checked("M20.16"):                                       # (1) subject_means_16_fixed
    rng_c16 = np.random.default_rng(5332)
    wrong_16 = []
    for shape_c16 in ((7, 3), (4, 6), (5, 5), (12, 2)):
        notes_c16 = np.round(rng_c16.uniform(2, 19, size=shape_c16), 1)
        got_16 = call_16(1, "subject_means_16_fixed", subject_means_16_fixed, notes_c16.copy())
        want_16 = np.array([np.mean(notes_c16[:, j]) for j in range(shape_c16[1])])
        if got_16 is None or not close_16(got_16, want_16):
            wrong_16.append(f"un tableau {shape_c16[0]} × {shape_c16[1]} : attendu {np.round(want_16, 3).tolist()}, "
                            f"reçu {got_16!r}"[:220])
    report_16(not wrong_16, "(1) subject_means_16_fixed : quatre tableaux de formes variées",
              "(1) subject_means_16_fixed : " + " ; ".join(wrong_16[:2]))
    parts_16.append(1)

with checked("M20.16"):                                       # (2) noon_gap_16_fixed
    wrong_16 = []
    for n_c16 in (2, 3, 7):
        T_c16 = np.round(rng_c16.uniform(0, 20, size=(n_c16, 1)) + rng_c16.uniform(1, 8, size=(n_c16, 1))
                         * np.cos(2 * np.pi * (HOURS_16 - rng_c16.uniform(10, 18, size=(n_c16, 1))) / 24)
                         + rng_c16.normal(0, 1, size=(n_c16, 24)), 1)
        want_16 = float(np.mean([abs(T_c16[s, 12] - np.mean(T_c16[s])) for s in range(n_c16)]))
        got_16 = call_16(2, "noon_gap_16_fixed", noon_gap_16_fixed, T_c16.copy())
        if got_16 is None or not close_16(got_16, want_16):
            wrong_16.append(f"{n_c16} stations aux profils différents : attendu {want_16:.6g}, reçu {got_16!r}"[:200])
    report_16(not wrong_16, "(2) noon_gap_16_fixed : des stations aux profils différents",
              "(2) noon_gap_16_fixed : " + " ; ".join(wrong_16[:2]))
    parts_16.append(2)

with checked("M20.16"):                                       # (3) sample_sd_16_fixed
    wrong_16 = []
    for size_c16 in (2, 3, 5, 9, 40):
        x_c16 = np.round(rng_c16.normal(10, 3, size=size_c16), 2)
        want_16 = math.sqrt(sum((v - x_c16.mean()) ** 2 for v in x_c16) / (size_c16 - 1))
        got_16 = call_16(3, "sample_sd_16_fixed", sample_sd_16_fixed, x_c16.copy())
        if got_16 is None or not close_16(got_16, want_16):
            wrong_16.append(f"{size_c16} valeurs : attendu {want_16:.6g}, reçu {got_16!r}"[:160])
    report_16(not wrong_16, "(3) sample_sd_16_fixed : des échantillons de 2 à 40 valeurs",
              "(3) sample_sd_16_fixed : " + " ; ".join(wrong_16[:2]))
    parts_16.append(3)

if len(set(parts_16)) == 3:
    verdict("M20.16", all(results_16), "les trois fonctions corrigées passent tous les cas.",
            "relis les lignes ❌ ci-dessus.")'''

M20_16 = Ex(
    "M20.16", "🐛", 1, 15, "Chasse à l'erreur : une moyenne sur le mauvais axe, une diffusion silencieuse, un ddof "
    "oublié",
    "reconnaître trois erreurs classiques des réductions le long d'axes qui ne lèvent aucune erreur Python et passent "
    "une vérification mal choisie, puis les corriger.", "fiche §2", tracks="C, E", given=GIVEN_16, note=NOTE_16,
    body=r"""Un collègue a écrit trois fonctions (cellule fournie) ; chacune a l'erreur que nomme le titre, aucune ne lève d'erreur Python, et chacune a passé la vérification qu'il a faite :
1. `subject_means_16(notes)` doit rendre la moyenne de chaque **matière** d'un tableau (élèves, matières). Il l'a vérifiée sur un tableau de 5 élèves et 5 matières : le résultat a bien la forme $(5,)$.
2. `noon_gap_16(T)` reçoit une journée de relevés, `T` de forme (stations, 24), et doit rendre l'écart moyen, sur les stations, entre le relevé de midi (l'heure 12) de chaque station et sa moyenne journalière, en valeur absolue : $\frac1n\sum_s \lvert T[s, 12] - \bar T_s\rvert$. Il l'a vérifiée sur quatre stations au même profil : la valeur attendue.
3. `sample_sd_16(x)` doit rendre l'écart type d'un échantillon de mesures répétées (l'incertitude d'une mesure), la racine de sa variance sans biais (ddof = 1). Il l'a vérifiée sur 100 000 tirages d'écart type 2 : à peu près 2.

À faire : écris `subject_means_16_fixed`, `noon_gap_16_fixed` et `sample_sd_16_fixed`, puis, avec elles (la valeur que donne le calcul, sans l'arrondir) :
- a) les moyennes des 3 matières du tableau `NOTES_16` (6 élèves, 3 matières ; une liste de 3 nombres) ;
- b) l'écart moyen de midi des 5 stations de `T_16` ;
- c) l'écart type des 5 mesures répétées d'une même longueur de `SMALL_16`, en mm.

La vérification essaie tes corrections sur des cas que tu ne vois pas : des tableaux de formes variées, des stations aux profils différents, de petits échantillons.""",
    todo='''def subject_means_16_fixed(notes):
    """The mean of each subject of a table (pupils, subjects): one value per subject."""
    raise NotImplementedError("subject_means_16_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def noon_gap_16_fixed(T):
    """T of shape (stations, 24): one day, hour by hour. The mean, over the stations, of |T[s, 12] − daily mean of s|."""
    raise NotImplementedError("noon_gap_16_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def sample_sd_16_fixed(x):
    """The standard deviation of a sample: the square root of its unbiased variance (ddof = 1)."""
    raise NotImplementedError("sample_sd_16_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M20_16a = answer_M20_16b = answer_M20_16c = ...
with wbm.attempt("M20.16"):          # your three functions: ⏳ while they are not written
    answer_M20_16a = ...  # a) a list of 3 numbers, as computed (not rounded): the means of the subjects of NOTES_16
    answer_M20_16b = ...  # b) a number, as computed: the mean noon gap of T_16
    answer_M20_16c = ...  # c) a number, as computed: the standard deviation of SMALL_16''',
    check='''for letter, answer in zip("abc", [answer_M20_16a, answer_M20_16b, answer_M20_16c]):
    wbm.check(f"M20.16{letter}", answer, computed=True)

''' + CHECK_16,
    solution='''def subject_means_16_fixed(notes):
    """The mean of each subject of a table (pupils, subjects): one value per subject."""
    return np.asarray(notes, dtype=float).mean(axis=0)          # axis 0 runs over the pupils: one mean per column


def noon_gap_16_fixed(T):
    """T of shape (stations, 24): one day, hour by hour. The mean, over the stations, of |T[s, 12] − daily mean of s|."""
    T = np.asarray(T, dtype=float)
    return float(np.mean(np.abs(T[:, 12] - T.mean(axis=1))))     # (n,) − (n,): one gap per station


def sample_sd_16_fixed(x):
    """The standard deviation of a sample: the square root of its unbiased variance (ddof = 1)."""
    return float(np.std(x, ddof=1))


answer_M20_16a = subject_means_16_fixed(NOTES_16).tolist()
answer_M20_16b = noon_gap_16_fixed(T_16)
answer_M20_16c = sample_sd_16_fixed(SMALL_16)
print("a)", np.round(answer_M20_16a, 4).tolist(), "; le collègue :", np.round(subject_means_16(NOTES_16), 4).tolist())
print("b)", round(answer_M20_16b, 4), "; le collègue :", round(noon_gap_16(T_16), 4), "; forme de son tableau :",
      (T_16[:, 12] - T_16.mean(axis=1, keepdims=True)).shape)
print("c)", round(answer_M20_16c, 4), "; le collègue :", round(sample_sd_16(SMALL_16), 4), "; rapport √(5/4) =",
      round(math.sqrt(5 / 4), 4))


''' + CHECK_16,
    record='''notes_16r = np.array([[12.0, 8.5, 15.0], [9.5, 11.0, 13.0], [14.0, 10.0, 16.5], [7.0, 12.5, 11.0],
                      [15.5, 9.0, 14.0], [10.0, 13.5, 12.0]])
wbm.record("M20.16a", [sum(notes_16r[:, j]) / 6 for j in range(3)], decimals=4,
           mistakes={"une valeur par élève : c'est l'axe 1 ; une matière est une colonne":
                         [sum(notes_16r[i]) / 3 for i in range(6)]})
hours_16r = np.linspace(0.0, 23.0, 24)
day_16r = np.round(np.array([[8.0], [12.5], [5.0], [15.0], [10.0]])
                   + np.array([[3.0], [6.0], [2.0], [8.0], [4.5]])
                   * np.cos(2 * np.pi * (hours_16r - [[14], [15], [13], [16], [14]]) / 24)
                   + np.random.default_rng(5332).normal(0, 0.5, size=(5, 24)), 1)
gaps_16r = [abs(day_16r[s, 12] - day_16r[s].mean()) for s in range(5)]
wbm.record("M20.16b", float(np.mean(gaps_16r)), decimals=4,
           mistakes={"(n,) moins (n, 1) donne (n, n) : retire à chaque station SA moyenne, un vecteur (n,) contre un "
                     "vecteur (n,)": float(np.mean(np.abs(day_16r[:, 12] - day_16r.mean(axis=1, keepdims=True))))})
small_16r = [12.5, 14.0, 9.5, 11.0, 13.0]
squares_16r = sum((v - sum(small_16r) / 5) ** 2 for v in small_16r)
wbm.record("M20.16c", math.sqrt(squares_16r / 4), decimals=4,
           mistakes={"ddof = 1 : la variance d'un échantillon divise par n − 1 ; np.std divise par n par défaut":
                         math.sqrt(squares_16r / 5),
                     "l'écart type est la RACINE de la variance": squares_16r / 4})''',
    after=[
        ("md", "**Après la vérification**, dans ta copie : pourquoi la vérification (1) ne pouvait-elle pas voir "
               "l'erreur, et quelle vérification l'aurait vue ? Quelle est la forme de `T[:, 12] - T.mean(axis=1, "
               "keepdims=True)` pour 5 stations, et que contient sa case $(i, j)$ ? Pourquoi quatre stations au même "
               "profil cachent-elles l'erreur (2) ? Pour (3), de quel facteur le résultat du collègue s'écarte-t-il "
               "sur $n$ valeurs, et pourquoi ne le voit-on pas sur 100 000 ?"),
    ],
)

GIVEN_17 = '''def ignores_ddof_17(x, axes, ddof=0):
    """Wrong: the variance always divides by N − 1, whatever ddof (built on the reference)."""
    return ref_tensors.moments_along_axes(x, axes, ddof=1)


def variance_of_variances_17(x, axes, ddof=0):
    """Wrong: along several axes, the variance is the mean, over the other reduced axes, of the variances along the
    first one (built on the reference)."""
    axes = (int(axes),) if np.ndim(axes) == 0 else tuple(int(a) for a in axes)
    mean, var = ref_tensors.moments_along_axes(x, axes, ddof=ddof)
    if len(axes) > 1:
        var = ref_tensors.moments_along_axes(ref_tensors.moments_along_axes(x, axes[0], ddof=ddof)[1], axes[1:])[0]
    return mean, var


def wrong_count_17(x, axes, ddof=0):
    """Wrong: along several axes, the sum is divided by the length of the first axis only (built on the reference)."""
    axes = (int(axes),) if np.ndim(axes) == 0 else tuple(int(a) for a in axes)
    mean, var = ref_tensors.moments_along_axes(x, axes, ddof=ddof)
    if len(axes) > 1:
        mean = mean * np.prod([np.shape(x)[a] for a in axes]) / np.shape(x)[axes[0]]
    return mean, var


WRONG_17 = {"ignores_ddof_17": ignores_ddof_17, "variance_of_variances_17": variance_of_variances_17,
            "wrong_count_17": wrong_count_17}'''

CHECK_17 = '''with checked("M20.17"):
    results_17 = []

    def report_17(ok, success, failure):
        results_17.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))

    calls_17 = [0]

    def counted_17(function):
        """function, its calls counted in calls_17."""
        def wrapper(x, axes, ddof=0):
            calls_17[0] += 1
            return function(x, axes, ddof=ddof)
        return wrapper

    try:
        gaps_17 = property_test_17(counted_17(ref_tensors.moments_along_axes))
    except AssertionError as exc:
        print(f"❌ Ex M20.17 : ton test échoue sur la référence, qui est juste : {exc}"[:400])
        raise StopCheck from None
    try:
        gaps_17 = np.asarray(gaps_17, dtype=float).ravel()
    except (TypeError, ValueError):
        print(f"❌ Ex M20.17 : property_test_17 doit rendre la liste des écarts, reçu {gaps_17!r}"[:200])
        raise StopCheck from None
    report_17(calls_17[0] >= 400 and gaps_17.size >= 100,
              f"sur la référence, ton test passe : {gaps_17.size} cas, {calls_17[0]} appels de moments",
              f"sur la référence, ton test ne fait que {gaps_17.size} cas et {calls_17[0]} appels de moments : au moins "
              "100 cas, et au moins quatre appels par cas")
    report_17(gaps_17.size > 0 and np.all(np.isfinite(gaps_17)) and np.all(gaps_17 >= 0) and np.min(gaps_17) > 1e-9,
              f"avec ddof = 1, la décomposition n'est jamais exacte : écart relatif de {np.min(gaps_17):.1e} à "
              f"{np.max(gaps_17):.1e}" if gaps_17.size else "",
              "les écarts rendus avec ddof = 1 doivent être des nombres positifs, non nuls : |v₁ − (moyenne des "
              "variances + variance des moyennes)| / v₁")
    for name_17, wrong_function_17 in WRONG_17.items():
        try:
            property_test_17(wrong_function_17)
            outcome_17 = "il passe"
        except AssertionError:
            outcome_17 = None
        except Exception as exc:  # noqa: BLE001 - another error than an assert
            outcome_17 = f"il lève {type(exc).__name__} : {str(exc)[:120]}"
        report_17(outcome_17 is None, f"ton test attrape {name_17} par un assert",
                  f"ton test n'attrape pas {name_17} par un assert ({outcome_17})")
    try:
        property_test_17(mymath.tensors.moments_along_axes)
        mine_17 = None
    except AssertionError as exc:
        mine_17 = str(exc)[:200]
    print("✅ ta moments_along_axes passe ton test de propriété" if mine_17 is None else
          f"❌ ta moments_along_axes échoue à ton test ({mine_17}) : si ton test passe sur la référence, l'erreur est "
          "dans ta fonction (lance aussi les tests de M20.11)")
    verdict("M20.17", all(results_17), "ton test passe sur la référence et attrape les trois fonctions fausses.",
            "relis les lignes ❌ ci-dessus.")'''

M20_17 = Ex(
    "M20.17", "🛠️", 1, 25, "Un test de propriété : réduire sur deux axes d'un coup, ou l'un après l'autre",
    "écrire un test de propriété pour les moments le long de deux axes, et s'assurer qu'il attrape trois fonctions "
    "fausses.", "fiche §2 ; Ex M20.11", tracks="C", given=GIVEN_17, note=NOTE_17,
    body=r"""Un **test de propriété** vérifie, sur beaucoup de cas tirés au hasard, une loi que tout résultat juste respecte, sans connaître la réponse de chaque cas (M17, M18). La loi, ici (fiche §2) : pour un tableau `x` et deux axes distincts $a$ et $b$,
- réduire sur $a$ et $b$ d'un coup, ou l'un après l'autre (d'abord $a$, puis $b$ sur le tableau des moyennes, les axes réduits étant gardés), donne la même **moyenne** ;
- la **variance** d'un coup, avec ddof = 0, est la moyenne, le long de $b$, des variances le long de $a$, plus la variance, le long de $b$, des moyennes le long de $a$ ;
- avec ddof = 1 partout, cette décomposition n'est plus exacte.

Écris deux fonctions, qui reçoivent la fonction à tester, `moments`, de même contrat que `moments_along_axes`. Toutes les réductions, d'un coup comme l'une après l'autre, passent par `moments` (au moins 4 appels par cas : la vérification les compte) :
- `check_two_axes(moments, x, a, b)` lève une `AssertionError` (un `assert` avec un message qui dit le cas) si les moyennes ne coïncident pas, ou si la décomposition de la variance avec ddof = 0 n'est pas exacte (`np.allclose`, `rtol=1e-9`, `atol=1e-12`) ; sinon, elle rend l'écart relatif de la même décomposition avec ddof = 1, $\frac{\lvert v_1 - (\text{moyenne des variances} + \text{variance des moyennes})\rvert}{v_1}$, le plus grand sur les valeurs des autres axes (un `float`) ;
- `property_test_17(moments)` tire 100 cas avec un générateur `np.random.default_rng(5337)`, créé dans la fonction : un tableau de 2 à 4 axes, de longueurs 2 à 5, de valeurs de loi normale, et deux axes distincts tirés au hasard ; elle rend la liste des 100 écarts de `check_two_axes`.

La cellule fournie donne trois fonctions **fausses**, construites sur la référence (`ref_tensors`) : `ignores_ddof_17` divise toujours par $N - 1$ ; `variance_of_variances_17` rend, le long de plusieurs axes, la moyenne des variances le long du premier ; `wrong_count_17` divise la somme le long de plusieurs axes par la longueur du premier seulement. La vérification lance ton test sur la référence, où il doit passer ; sur chacune des trois fonctions fausses, où il doit échouer par un `assert` ; puis sur **ta** `moments_along_axes`.""",
    todo='''def check_two_axes(moments, x, a, b):
    """For the function under test moments (the contract of moments_along_axes): assert that the mean along (a, b)
    is the mean along a then b, and that the variance along (a, b) with ddof = 0 is the mean along b of the variances
    along a plus the variance along b of the means along a. Return the largest relative gap of the same decomposition
    with ddof = 1."""
    raise NotImplementedError("check_two_axes n'est pas encore écrite (04_indices.md si tu bloques)")


def property_test_17(moments):
    """check_two_axes on 100 random cases drawn with np.random.default_rng(5337): arrays of 2 to 4 axes of lengths 2
    to 5, two distinct axes. Return the list of the 100 gaps."""
    raise NotImplementedError("property_test_17 n'est pas encore écrite (04_indices.md si tu bloques)")''',
    check=CHECK_17,
    solution='''def check_two_axes(moments, x, a, b):
    """For the function under test moments (the contract of moments_along_axes): assert that the mean along (a, b)
    is the mean along a then b, and that the variance along (a, b) with ddof = 0 is the mean along b of the variances
    along a plus the variance along b of the means along a. Return the largest relative gap of the same decomposition
    with ddof = 1."""
    gaps = []
    for ddof in (0, 1):
        mean, var = moments(x, (a, b), ddof=ddof)
        mean_a, var_a = moments(x, a, ddof=ddof)                  # axis a kept with length 1: b does not move
        mean_ab, var_of_means = moments(mean_a, b, ddof=ddof)
        mean_of_vars, _ = moments(var_a, b, ddof=ddof)
        if ddof == 0:
            assert np.allclose(mean, mean_ab, rtol=1e-9, atol=1e-12), (
                f"shape {x.shape}, axes ({a}, {b}): the mean in one go differs from the mean along {a} then {b}")
            assert np.allclose(var, mean_of_vars + var_of_means, rtol=1e-9, atol=1e-12), (
                f"shape {x.shape}, axes ({a}, {b}): the variance (ddof = 0) is not the mean of the variances plus "
                f"the variance of the means")
        else:
            gaps.append(float(np.max(np.abs(var - (mean_of_vars + var_of_means)) / var)))
    return gaps[0]


def property_test_17(moments):
    """check_two_axes on 100 random cases drawn with np.random.default_rng(5337): arrays of 2 to 4 axes of lengths 2
    to 5, two distinct axes. Return the list of the 100 gaps."""
    rng = np.random.default_rng(5337)
    gaps = []
    for _ in range(100):
        shape = tuple(int(n) for n in rng.integers(2, 6, size=int(rng.integers(2, 5))))
        a, b = (int(axis) for axis in rng.choice(len(shape), size=2, replace=False))
        gaps.append(check_two_axes(moments, rng.normal(size=shape), a, b))
    return gaps


gaps_s17 = property_test_17(ref_tensors.moments_along_axes)
print("ddof = 1 : écart relatif de la décomposition, de", f"{min(gaps_s17):.1e}", "à", f"{max(gaps_s17):.1e}",
      "; médiane", f"{np.median(gaps_s17):.2f}")
for name_s17, wrong_s17 in WRONG_17.items():
    try:
        property_test_17(wrong_s17)
        print(name_s17, ": pas attrapée")
    except AssertionError as exc:
        print(name_s17, ":", exc)


''' + CHECK_17,
    after=[
        ("md", "**Après la vérification**, dans ta copie : écris la décomposition pour un tableau de forme $(n_a, "
               "n_b)$ et démontre-la (le terme croisé s'annule). Avec ddof = 1, quels dénominateurs apparaissent, et "
               "pourquoi ne se recombinent-ils pas ? Laquelle des trois fonctions fausses la propriété des moyennes "
               "attrape-t-elle, et lesquelles seule la décomposition attrape-t-elle ? Une fonction qui calcule la "
               "variance par « moyenne des carrés moins carré de la moyenne » passerait-elle ton test, et que "
               "verraient les tests de `mymath` ?"),
    ],
)

PART_C = Part("C", "Déboguer, tester",
              "Fiche §2. Trois erreurs classiques des réductions le long d'axes ; un test de propriété pour les moments "
              "le long de deux axes. La vérification de M20.17 s'appuie sur la référence (`ref_tensors`), pour ne pas "
              "dépendre de ton code.",
              given=GIVEN_C, exercises=[M20_16, M20_17])

# ---------------------------------------------------------------------------
# Notebook exercises: the challenge (M20.18)
# ---------------------------------------------------------------------------
GIVEN_18 = '''rng_18 = np.random.default_rng(5338)
N_18, n_18 = 150, 21                                                       # 150 communes, a sample of 21
X_18 = np.round(np.exp(rng_18.normal(np.log(2500), 1.5, size=N_18)))      # the population at the last census: known
Y_18 = np.round(X_18 * (1 + rng_18.normal(0.03, 0.04, size=N_18)))        # the population today: unknown
TOTAL_18 = Y_18.sum()                                                      # the true total, to judge the estimates


def systematic_sample(pi, rng):
    """The systematic draw: the π_i laid end to end on a segment of length n = Σ π_i (an integer), u drawn uniform in
    [0, 1[ (one rng.random() per call), and the units whose interval holds one of the points u, u + 1, ..., u + n − 1.
    Each unit is drawn with the probability π_i, and exactly n units are. Returns a boolean array."""
    pi = np.asarray(pi, dtype=float)
    if pi.ndim != 1 or np.any(~(pi > 0)) or np.any(pi > 1 + 1e-12):
        raise ValueError("every π_i must be in ]0, 1]")
    n = pi.sum()
    if abs(n - round(n)) > 1e-9:
        raise ValueError(f"the sum of the π_i must be an integer, got {n!r}")
    bounds = np.concatenate([[0.0], np.cumsum(pi)])
    bounds *= round(n) / bounds[-1]                                         # exactly n at the end
    points = rng.random() + np.arange(round(n))
    units = np.minimum(np.searchsorted(bounds, points, side="right") - 1, len(pi) - 1)
    included = np.zeros(len(pi), dtype=bool)
    included[units] = True
    return included


print("les 5 plus grandes communes :", np.sort(X_18)[-5:].astype(int).tolist(), "; total au recensement :",
      int(X_18.sum()), "; n x_i / Σx > 1 pour", int(np.sum(n_18 * X_18 / X_18.sum() > 1)), "commune(s)")'''

CHECK_18 = '''with checked("M20.18"):
    results_18 = []

    def report_18(ok, success, failure):
        results_18.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))

    def expected_18(x, n):
        """min(1, c x), with c such that Σ min(1, c x) = n, by bisection: another method than the statement's."""
        low, high = 0.0, 1.0 / np.min(x)
        for _ in range(200):
            middle = (low + high) / 2
            low, high = (middle, high) if np.minimum(1.0, middle * x).sum() < n else (low, middle)
        return np.minimum(1.0, high * x)

    rng_c18 = np.random.default_rng(5338)
    cases_18 = [("la population de l'énoncé", X_18, n_18)]
    for size_c18, count_c18, spread_c18 in ((30, 6, 1.6), (60, 12, 0.3), (80, 9, 2.0), (12, 11, 1.0)):
        cases_18.append((f"{size_c18} unités, n = {count_c18}",
                         np.round(np.exp(rng_c18.normal(5, spread_c18, size=size_c18))) + 1, count_c18))
    wrong_18 = []
    for label_c18, x_c18, n_c18 in cases_18:
        copy_c18 = x_c18.copy()
        got_c18 = pps_probabilities(copy_c18, n_c18)
        want_c18 = expected_18(x_c18, n_c18)
        if not np.array_equal(copy_c18, x_c18):
            wrong_18.append(f"{label_c18} : x a été modifié")
        elif got_c18 is None or np.shape(got_c18) != x_c18.shape:
            wrong_18.append(f"{label_c18} : attendu un tableau de forme {x_c18.shape}, reçu {got_c18!r}"[:160])
        elif not np.allclose(np.asarray(got_c18, dtype=float), want_c18, rtol=1e-9, atol=1e-12):
            got_c18 = np.asarray(got_c18, dtype=float)
            wrong_18.append(f"{label_c18} : ce ne sont pas les probabilités attendues (somme attendue {n_c18}, reçu "
                            f"une somme {got_c18.sum():.6g} et un plus grand π de {got_c18.max():.6g})")
    report_18(not wrong_18, f"pps_probabilities : juste sur {len(cases_18)} populations", "pps_probabilities, "
              + " ; ".join(wrong_18[:2]))
    if wrong_18:
        raise StopCheck
    pi_c18 = np.asarray(pps_probabilities(X_18, n_18), dtype=float)
    certain_c18 = pi_c18 >= 1 - 1e-12
    report_18(abs(pi_c18.sum() - n_18) < 1e-9 and np.all((pi_c18 > 0) & (pi_c18 <= 1 + 1e-12)),
              f"tes probabilités sont dans ]0, 1] et ont pour somme {n_18}", "tes probabilités doivent être dans ]0, 1] "
              f"et avoir pour somme {n_18}")
    report_18(certain_c18.any() and X_18[certain_c18].min() > X_18[~certain_c18].max(),
              "les communes prises d'office sont les plus grandes",
              "les communes prises d'office doivent être les plus grandes")
    pi_c18 = np.where(certain_c18, 1.0, pi_c18)
    equal_c18 = np.full(N_18, n_18 / N_18)
    for label_c18, probabilities_c18 in (("tes probabilités", pi_c18), ("des probabilités égales", equal_c18)):
        rng_s18 = np.random.default_rng(5339)
        estimates_c18 = np.empty(2000)
        for k_c18 in range(2000):
            drawn_c18 = systematic_sample(probabilities_c18, rng_s18)
            estimates_c18[k_c18] = np.sum(Y_18[drawn_c18] / probabilities_c18[drawn_c18])
        spread_c18 = estimates_c18.std(ddof=1) / TOTAL_18
        bias_c18 = estimates_c18.mean() / TOTAL_18 - 1
        if probabilities_c18 is pi_c18:
            report_18(spread_c18 < 0.02, f"avec {label_c18}, l'écart type relatif reste sous 2 %",
                      f"avec {label_c18}, l'écart type relatif dépasse 2 %")
            report_18(abs(bias_c18) < 3 * spread_c18 / math.sqrt(2000),
                      "le biais relatif reste sous 3 erreurs types", "le biais relatif dépasse 3 erreurs types")
        else:
            report_18(spread_c18 > 0.10, f"avec {label_c18}, l'écart type relatif dépasse 10 %",
                      f"avec {label_c18}, l'écart type relatif reste sous 10 %")
    verdict("M20.18", all(results_18), "tes probabilités rendent l'estimation de Horvitz-Thompson presque exacte.",
            "relis les lignes ❌ ci-dessus.")'''

M20_18 = Ex(
    "M20.18", "🏆", 3, 25, "Défi : des probabilités d'inclusion proportionnelles à la taille, et un estimateur presque "
    "sans variance",
    "construire des probabilités d'inclusion proportionnelles à une taille, plafonnées à 1, et mesurer avec un tirage "
    "systématique la précision qu'elles donnent à l'estimateur de Horvitz-Thompson.",
    "fiche §5 ; Ex M20.12 et M20.14", tracks="C", given=GIVEN_18, note=NOTE_18,
    body=r"""Une population de $N = 150$ communes (cellule fournie) : leur population au dernier recensement, $x_i$ (`X_18`, connue ; quelques très grandes villes), et leur population actuelle, $y_i$, à quelques pour cent près la même (`Y_18`, inconnue de celui qui sonde ; le vrai total est `TOTAL_18`). On veut estimer le total en visitant $n = 21$ communes (`n_18`).

La cellule fournie donne aussi `systematic_sample(pi, rng)`, le **tirage systématique** : on aligne les $\pi_i$ bout à bout sur un segment de longueur $n = \sum_i\pi_i$, on tire $u$ uniforme dans $[0, 1[$ (un seul `rng.random()` par appel), et l'on prend les unités dont l'intervalle contient l'un des points $u, u + 1, \ldots, u + n - 1$. Chaque unité est tirée avec la probabilité $\pi_i$, et **exactement** $n$ unités le sont ; elle refuse (`ValueError`) un $\pi_i$ hors de $]0, 1]$ ou une somme qui n'est pas entière.

Écris `pps_probabilities(x, n)` : des probabilités proportionnelles à $x$, de somme $n$. Une unité dont la probabilité dépasserait 1 est prise d'office ($\pi_i = 1$), et le reste, $n$ moins le nombre d'unités prises d'office, est réparti à nouveau, proportionnellement à $x$, entre les autres ; on recommence jusqu'à ce qu'aucune ne dépasse 1. Un tableau de flottants ; `x` n'est pas modifié.

Puis, avec tes probabilités `pi_18` pour `X_18` et `n_18` :
- `estimates_18` : les 2 000 estimations de Horvitz-Thompson de 2 000 tirages systématiques, faits avec un générateur `np.random.default_rng(5339)` créé une fois, un appel de `systematic_sample` par tirage ;
- `equal_18` : de même, avec les probabilités égales $n/N$ et un second générateur `np.random.default_rng(5339)`.

Réponds :
- a) le nombre de communes prises d'office ($\pi_i = 1$) ;
- b) l'écart type relatif de `estimates_18`, en % (l'écart type avec ddof = 1, divisé par le vrai total ; la valeur que donne le calcul, sans l'arrondir) ;
- c) celui de `equal_18`, en % (la valeur que donne le calcul, sans l'arrondir).

La vérification essaie `pps_probabilities` sur d'autres populations et regarde la somme, l'intervalle $]0, 1]$ et les communes prises d'office ; puis elle refait la simulation avec tes probabilités : l'écart type relatif doit rester sous 2 %, celui des probabilités égales dépasser 10 %, et le biais relatif rester sous 3 erreurs types.""",
    todo='''def pps_probabilities(x, n):
    """Inclusion probabilities proportional to x, of sum n: a unit whose probability would exceed 1 is taken with
    certainty (π = 1), and what remains of n is shared again among the others in proportion to x, until none
    exceeds 1. Returns a new array of floats."""
    raise NotImplementedError("pps_probabilities n'est pas encore écrite (04_indices.md si tu bloques)")


pi_18 = estimates_18 = equal_18 = ...
answer_M20_18a = answer_M20_18b = answer_M20_18c = ...
with wbm.attempt("M20.18"):          # pps_probabilities: ⏳ while it is not written
    pi_18 = ...           # your probabilities for X_18 and n_18
    estimates_18 = ...    # the 2 000 Horvitz-Thompson estimates, systematic draws, np.random.default_rng(5339)
    equal_18 = ...        # the same with the equal probabilities n_18 / N_18 and a second np.random.default_rng(5339)
    answer_M20_18a = ...  # a) an integer: the number of communes with π = 1
    answer_M20_18b = ...  # b) a number, as computed (not rounded): the relative standard deviation of estimates_18, in %
    answer_M20_18c = ...  # c) a number, as computed: that of equal_18, in %''',
    check='''for letter, answer in zip("abc", [answer_M20_18a, answer_M20_18b, answer_M20_18c]):
    wbm.check(f"M20.18{letter}", answer, computed=True)

''' + CHECK_18,
    solution='''def pps_probabilities(x, n):
    """Inclusion probabilities proportional to x, of sum n: a unit whose probability would exceed 1 is taken with
    certainty (π = 1), and what remains of n is shared again among the others in proportion to x, until none
    exceeds 1. Returns a new array of floats."""
    x = np.asarray(x, dtype=float)
    certain = np.zeros(len(x), dtype=bool)
    while True:
        rest = ~certain
        pi = np.where(certain, 1.0, (n - certain.sum()) * x / x[rest].sum())
        over = rest & (pi > 1)
        if not over.any():
            return pi
        certain |= over                                         # taken with certainty; share the rest again


def simulate_18(probabilities, draws=2000):
    """The Horvitz-Thompson estimates of `draws` systematic draws, one generator np.random.default_rng(5339)."""
    rng = np.random.default_rng(5339)
    estimates = np.empty(draws)
    for k in range(draws):
        drawn = systematic_sample(probabilities, rng)
        estimates[k] = np.sum(Y_18[drawn] / probabilities[drawn])
    return estimates


pi_18 = pps_probabilities(X_18, n_18)
estimates_18 = simulate_18(pi_18)
equal_18 = simulate_18(np.full(N_18, n_18 / N_18))
answer_M20_18a = int(np.sum(pi_18 == 1))
answer_M20_18b = 100 * estimates_18.std(ddof=1) / TOTAL_18
answer_M20_18c = 100 * equal_18.std(ddof=1) / TOTAL_18
print("dépassent 1 avant toute répartition :", int(np.sum(n_18 * X_18 / X_18.sum() > 1)), "; prises d'office à la fin :",
      answer_M20_18a, "; les π suivants :", np.round(np.sort(pi_18[pi_18 < 1])[-3:], 4).tolist())
print("yᵢ/πᵢ des communes qui ne sont pas prises d'office : de", round(float(np.min((Y_18 / pi_18)[pi_18 < 1]))),
      "à", round(float(np.max((Y_18 / pi_18)[pi_18 < 1]))))
print("b)", round(answer_M20_18b, 2), "% ; biais relatif :", f"{100 * (estimates_18.mean() / TOTAL_18 - 1):.3f} %")
print("c)", round(answer_M20_18c, 1), "% ; biais relatif :", f"{100 * (equal_18.mean() / TOTAL_18 - 1):.2f} %")


''' + CHECK_18,
    record='''rng_18r = np.random.default_rng(5338)
x_18r = np.round(np.exp(rng_18r.normal(np.log(2500), 1.5, size=150)))
y_18r = np.round(x_18r * (1 + rng_18r.normal(0.03, 0.04, size=150)))
order_18r = np.argsort(x_18r)[::-1]                 # the largest first: k certain units, c = (n − k) / Σ of the others
for k_18r in range(21):
    c_18r = (21 - k_18r) / x_18r[order_18r[k_18r:]].sum()
    if c_18r * x_18r[order_18r[k_18r]] <= 1:
        break
pi_18r = np.minimum(1.0, c_18r * x_18r)
assert abs(pi_18r.sum() - 21) < 1e-9 and int(np.sum(21 * x_18r / x_18r.sum() > 1)) < k_18r
wbm.record("M20.18a", k_18r,
           mistakes={"on recommence : après une répartition, d'autres communes peuvent dépasser 1":
                         int(np.sum(21 * x_18r / x_18r.sum() > 1))})


def systematic_18r(pi, rng):
    bounds = np.concatenate([[0.0], np.cumsum(pi)])
    bounds *= round(pi.sum()) / bounds[-1]
    units = np.minimum(np.searchsorted(bounds, rng.random() + np.arange(round(pi.sum())), side="right") - 1, len(pi) - 1)
    return units


def spread_18r(pi):
    rng = np.random.default_rng(5339)
    estimates = []
    for _ in range(2000):
        units = systematic_18r(pi, rng)
        estimates.append(np.sum(y_18r[units] / pi[units]))
    return 100 * np.std(estimates, ddof=1) / y_18r.sum()


wbm.record("M20.18b", spread_18r(pi_18r), decimals=2,
           mistakes={"l'écart type des estimations faites avec TES probabilités, pas avec les probabilités égales":
                         spread_18r(np.full(150, 21 / 150)),
                     "un écart type nul : tes tirages sont identiques ; crée le générateur une seule fois, avant la "
                     "boucle": 0.0})
wbm.record("M20.18c", spread_18r(np.full(150, 21 / 150)), decimals=1)''',
    after=[
        ("md", "**Dans ta copie** : combien de communes dépassaient 1 avant toute répartition, et combien à la fin ? "
               "Pourquoi une répartition peut-elle en faire dépasser de nouvelles ? Pourquoi l'estimation est-elle "
               "presque exacte (que vaut $y_i/\\pi_i$, à quelques pour cent près, pour une commune qui n'est pas prise "
               "d'office ?), et pourquoi le tirage de Poisson de M20.14 ne pouvait-il pas faire aussi bien ? Que "
               "deviendrait la précision si une grande ville avait beaucoup changé depuis le recensement ?"),
    ],
)

PART_D = Part("D", "Défi", "Fiche §5. Des probabilités proportionnelles à la taille, plafonnées à 1, et un tirage "
                           "systématique : un estimateur sans biais et presque sans variance.",
              exercises=[M20_18])

PARTS = [PART_A, PART_B, PART_C, PART_D]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M20.1 à M20.5, M20.8 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            rows.append(ex.table_row(part.key if i == 0 else ""))
    if kind == "exercise":
        title = "# M20 · Tenseurs, axes et estimateurs pondérés — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m20_tenseurs_normalisation/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M20`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M20 · Tenseurs, axes et estimateurs pondérés — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : des formes après réductions et remodelages, la notation "
               "d'Einstein et le coût d'une contraction, la matrice de centrage et la standardisation, un sondage de "
               "Horvitz-Thompson, un schéma d'Euler en $L$ pas, et un pont.\n"
               "- Écrire les trois fonctions de `mymath/tensors.py` (`einsum_pair`, `moments_along_axes`, "
               "`horvitz_thompson_total`) et les tester.\n"
               "- Prédire des formes puis les voir, comparer trois estimateurs d'un total par la simulation, dessiner "
               "le produit de $L$ pas d'Euler à horizon fixé, corriger trois erreurs classiques, écrire un test de "
               "propriété, et relever un défi : des probabilités proportionnelles à la taille.\n\n"
               r"**Rappel express.** Un tableau de forme $(n_0, \ldots, n_{k-1})$ ; en ordre C, $[i_0, i_1, i_2]$ est à "
               r"la position $(i_0n_1 + i_1)\,n_2 + i_2$ ; `reshape` relit la file dans l'ordre C, `transpose` change "
               r"l'ordre des axes. Réduire fait disparaître l'axe nommé ; `keepdims=True` le garde, de longueur 1. "
               r"Diffusion : formes alignées à droite, longueurs égales ou 1 ; $(n,)$ contre $(n, 1)$ donne $(n, n)$. "
               r"Variance : $\frac{1}{N - \text{ddof}}\sum (x - \bar x)^2$. `einsum` : une lettre absente du résultat "
               r"est sommée ; coût, le produit des longueurs de toutes les lettres. $\mathbf{C} = \mathbf{I} - "
               r"\frac1m\mathbf{1}\mathbf{1}^\top$, projection orthogonale de trace $m - 1$ ; la standardisation de "
               r"$a\mathbf{x} + b\mathbf{1}$, $a > 0$, est celle de $\mathbf{x}$. Horvitz-Thompson : $\hat Y = \sum_{i "
               r"\in S} y_i/\pi_i$, sans biais ; $\mathbb{V}(\hat Y) = \sum_i y_i^2\frac{1 - \pi_i}{\pi_i}$ en "
               r"tirage de Poisson. Euler : $\mathbf{I} + h\mathbf{J}$ ; $L$ pas à horizon $T = hL$ fixé restent "
               r"entre $(1 - hK)^L$ et $e^{KT}$, et $(\mathbf{I} + \frac TL\mathbf{J})^L \to e^{T\mathbf{J}}$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu suivre la forme d'un tableau à travers des réductions, des remodelages, des transpositions "
               "et la diffusion ?\n"
               "2. Sais-tu écrire un calcul d'indices en notation d'Einstein, le calculer avec `einsum` et compter son "
               "coût ?\n"
               "3. Sais-tu calculer moyennes et variances le long d'axes, avec le bon ddof, et standardiser le long "
               "du bon axe ?\n"
               "4. Sais-tu construire un estimateur sans biais en divisant par une probabilité d'inclusion, et choisir "
               "des probabilités qui le rendent précis ?\n"
               "5. Sais-tu borner le produit de $L$ facteurs $\\mathbf{I} + h\\mathbf{J}$ à horizon fixé ?\n\n"
               "**La suite** : le chapitre 20 de workbookIA, qui range ses données dans des tenseurs, standardise le "
               "long d'axes choisis, divise par une probabilité et enchaîne des applications proches de l'identité ; "
               "puis l'examen blanc CP4, qui clôt la partie IV, et M21 (la convolution).")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter=CHAPTER) if kind == "exercise" else setup_cell(kind))
    cells += objectives_cell()
    cells += paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO)
    for part in PARTS:
        cells += part_cells(part, kind)
    cells += footer_cells(kind)
    return cells


def main() -> int:
    for paper in PAPER:
        lines = [f'wbm.record("{paper.id}{letter}", {expr}{", " + options if options else ""})'
                 for letter, _, expr, options in paper.subs]
        check_unique_keys("\n".join(lines), paper.id)
    for ex in [e for part in PARTS for e in part.exercises]:
        for source in (ex.record, *(text for kind, text in ex.after if kind == "record")):
            if source:
                check_unique_keys(source, ex.id)
    write_notebook(f"{FOLDER}/03_notebook.ipynb", build("exercise"))
    write_notebook(f"{FOLDER}/05_solutions.ipynb", build("solution"))
    n_checks = sum(len(p.subs) for p in PAPER)
    n_ex = sum(len(part.exercises) for part in PARTS)
    print(f"✅ {FOLDER}/03_notebook.ipynb and 05_solutions.ipynb written ({len(PAPER)} paper exercises, "
          f"{n_checks} paper checks, {n_ex} notebook exercises)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
