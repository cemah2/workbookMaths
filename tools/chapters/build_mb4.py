#!/usr/bin/env python
"""Build the two notebooks of chapter MB4 from a single source (used by Claude).

    python tools/chapters/build_mb4.py
    python tools/run_all_notebooks.py chapitres/mb4_rang_faible/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/mb4_rang_faible/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ MB4.1 to MB4.4), each answer computed in the notebook from the data of its
statement (SymPy for the reduced row echelon form and the equation of MB4.4 f, exact fractions for the odds, the
saturation and the sums of the 1/(c + rank), math elsewhere), each wrong value computed by the error its message
names; parts A to D are the notebook exercises (MB4.8 to MB4.13), exactly as 02_exercices.md describes them.
Wrong-answer messages state a rule, never a number of the answer, the last step that gives it, nor another sub-question.

Data. The notebook exercises take the data of the paper exercises (a data cell of part A, read only), the data of their
own statements (the measured table M_8 of 🔨 MB4.8, seed 7508; the 7 × 9 rankings of 🔨 MB4.9, seed 7509; the 4 × 6
rankings of 🐛 MB4.12, seed 7512; all written as literals) and their own draws (the simulation of 🔮 MB4.10, seed 7510).
Seeds 7501 to 7549 only (the tests use 7400 to 7490, the figures 7491 to 7499): 7522 (the hidden rankings of 🐛 MB4.12;
its hidden tables are written by hand, of non-dyadic floats); 7513 is the seed of the five tables of 🏆 MB4.13 (in its
module); 7540 to 7549 serve only the calibration of the challenge (scratchpad). The check cells never hold the code that solves an exercise nor a value that
gives an answer without a calculation: the expected values are recorded by the solutions as hidden sub-IDs and compared
with ``wbm.check(..., computed=True)`` (the hidden calls of 🎨 MB4.11, the hidden notebooks of recipes of 🐛 MB4.12),
computed at check time by the reference ``mymath_ref.ranks`` (the hidden tables and rankings of 🐛 MB4.12, the exact
MRR in the hint of 🔮 MB4.10 d), or given by properties. The hidden part of 🏆 MB4.13 lives in
``solutions/challenges/mb4_13.py`` (the generator of the noisy tables, of which the notebook set is
``notebook_tables()``, seed 7513, and the method of the check); the data cell takes from it the five tables only, inside a
function, and the check cell loads it inside a function too, draws five new tables at each run (one of each kind: easy,
weak signal, spread signal, very elongated, no signal or extreme scale), and reads each hidden rank only after the
learner's function has returned, so that neither a law nor a hidden rank is in the notebook or in its globals.
The check cells use their own data, never the test cases of tests/test_mb4_ranks.py, the examples of the docstrings of
the stub ranks (nor of matrices, linmaps, svd_pca), the examples of the fiche, nor the numbers of workbookIA B4, B3, B2
and B1 (the notes of MB4 in the syllabus and their list « Évités »).
"""

from __future__ import annotations

import importlib.util
import math
import pprint
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (ROOT, STARS, Ex, Paper, Part, badge, check_unique_keys, guarded,  # noqa: E402,F401
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "MB4"
FOLDER = "chapitres/mb4_rang_faible"

BOOL = "True or False"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("MB4.1", "Les ventes de quatre boulangeries sur cinq produits : le rang, la factorisation par les colonnes "
                   "pivots, une seconde factorisation (CG)(G⁻¹F), et les nombres stockés ou libres", [
        ("a", "an integer", "R_1",
         '''mistakes={"le rang compte les colonnes indépendantes, pas les lignes du tableau": M_1.rows,
                     "une colonne qui est une combinaison d'autres colonnes n'ajoute aucune direction": M_1.cols}'''),
        ("b", "a 2 × 5 matrix, as the list of its rows (exact values)", "floats(F_1)",
         '''decimals=6,
           mistakes={"la ligne i de F porte les coordonnées sur la i-ième colonne pivot, dans chaque colonne de F":
                         floats(swapped_coefficients_1(F_1)),
                     "F ne garde que les r lignes non nulles de la forme échelonnée réduite": floats(RREF_1),
                     "la ligne i de F porte les coefficients de la i-ième colonne pivot : la première ligne est celle des "
                     "baguettes": floats(F_1)[::-1]}'''),
        ("c", "a 4 × 2 matrix, as the list of its rows", "floats(C_1 * G_1)",
         '''decimals=6,
           mistakes={"la colonne j de C G combine les colonnes de C avec les coefficients de la colonne j de G":
                         floats(C_1 * G_1.T),
                     "la seconde factorisation multiplie C par G, et F par l'inverse de G": floats(C_1 * G_1.inv())}'''),
        ("d", "a 2 × 5 matrix, as the list of its rows (exact values)", "floats(G_1.inv() * F_1)",
         '''decimals=6,
           mistakes={"F se multiplie à gauche par l'inverse de G, pas par G": floats(G_1 * F_1),
                     "l'inverse d'une matrice 2 × 2 se vérifie : G G⁻¹ = I": floats(G_1.inv().T * F_1)}'''),
        ("e", "an integer", "stored(4, 5, R_1)",
         '''mistakes={"C et F stockent r colonnes de m nombres et r lignes de n nombres : ni les m n nombres du tableau, "
                     "ni des valeurs singulières": R_1 * (4 + 5 + 1),
                     "il faut r colonnes dans C et r lignes dans F": 4 + 5,
                     "C a r colonnes de m nombres et F a r lignes de n nombres : on additionne": R_1 * 4 * 5}'''),
        ("f", "an integer", "free(4, 5, R_1)",
         '''mistakes={"l'identité des colonnes pivots fixe r² nombres de F, pas r": R_1 * (4 + 5 - 1),
                     "C compte aussi : ses m r nombres sont libres": R_1 * (5 - R_1)}'''),
        ("g", "a list of 2 integers: the numbers stored, then the free numbers", "[stored(120, 45, 3), free(120, 45, 3)]",
         '''mistakes={"l'identité des colonnes pivots fixe r² nombres de F, pas r": [stored(120, 45, 3), 3 * (120 + 45 - 1)],
                     "C et F stockent r colonnes de m nombres et r lignes de n nombres : ni les m n nombres du tableau, "
                     "ni des valeurs singulières": [3 * (120 + 45 + 1), 3 * (120 + 45 + 1 - 3)],
                     "le second nombre compte les nombres libres : retire les r² nombres que fixe l'identité des colonnes "
                     "pivots": [stored(120, 45, 3)] * 2,
                     "C et F stockent r(m + n) nombres ; r(m + n + 1) est le compte d'une SVD tronquée (M12d)":
                         [3 * (120 + 45 + 1), free(120, 45, 3)]}'''),
    ]),

    Paper("MB4.2", "Un tableau de relevés de stations météo donné par ses valeurs singulières : énergie captée, rang "
                   "effectif à 99 %, rang stable, puis le coût de C(Fx) et de (CF)x pour un et pour mille vecteurs", [
        ("a", "an integer", "ENERGY_2",
         '''mistakes={"l'énergie est la somme des carrés des valeurs singulières": sum(S_2),
                     "les 56 petites valeurs singulières comptent aussi dans l'énergie": sum(s * s for s in S_2[:4])}'''),
        ("b", "a number (4 decimals)", "share_2(2)",
         '''decimals=4,
           mistakes={"l'énergie compte les carrés des valeurs singulières": share_2(2, power=1),
                     "le total compte toutes les valeurs singulières, les 56 petites comprises":
                         share_2(2, values=S_2[:4]),
                     "la part des deux premières additionne les carrés des deux premières valeurs": share_2(1)}'''),
        ("c", "an integer", "RANK_2",
         '''mistakes={"le rang effectif à 99 % est le plus petit r dont la part atteint 0,99 : on s'arrête dès qu'elle "
                     "l'atteint": RANK_2 + 1,
                     "l'énergie compte les carrés des valeurs singulières": effective_rank_2(power=1)}'''),
        ("d", "a number (2 decimals)", "math.sqrt(sum(s * s for s in S_2[RANK_2:]))",
         '''decimals=2,
           mistakes={"‖·‖_F est la racine de la somme des carrés oubliés": float(sum(s * s for s in S_2[RANK_2:])),
                     "en norme de Frobenius, l'erreur compte toutes les valeurs singulières oubliées, pas seulement la plus "
                     "grande": float(S_2[RANK_2]),
                     "la quatrième valeur singulière est oubliée elle aussi": math.sqrt(sum(s * s for s in S_2[RANK_2 + 1:])),
                     "c'est l'erreur relative ‖M − M_r‖_F / ‖M‖_F : d) demande l'erreur ‖M − M_r‖_F elle-même":
                         math.sqrt(sum(s * s for s in S_2[RANK_2:]) / ENERGY_2),
                     "c'est la part de l'énergie oubliée (un carré) ; la question demande l'erreur en norme de Frobenius, "
                     "sa racine": sum(s * s for s in S_2[RANK_2:]) / ENERGY_2}'''),
        ("e", "a number (3 decimals)", "ENERGY_2 / S_2[0] ** 2",
         '''decimals=3,
           mistakes={"le rang stable est un rapport de carrés": sum(S_2) / S_2[0],
                     "le rang stable divise l'énergie par le carré de la plus grande valeur singulière":
                         S_2[0] ** 2 / ENERGY_2}'''),
        ("f", "an integer", "RANK_2 * (ROWS_2 + COLS_2)",
         '''mistakes={"C(Fx) ne forme jamais le produit C F : d'abord F x, puis C fois ce vecteur": ROWS_2 * COLS_2 * RANK_2,
                     "la matrice factorisée n'est pas appliquée comme une matrice pleine : F x, puis C fois ce vecteur":
                         ROWS_2 * COLS_2}'''),
        ("g", "an integer", "ROWS_2 * COLS_2 * RANK_2 + ROWS_2 * COLS_2",
         '''mistakes={"former C F coûte aussi des multiplications": ROWS_2 * COLS_2,
                     "après avoir formé C F, il reste à l'appliquer à x": ROWS_2 * COLS_2 * RANK_2}'''),
        ("h", "a list of 2 integers: C(Fx), then (CF)x", "[1000 * RANK_2 * (ROWS_2 + COLS_2), "
                                                         "ROWS_2 * COLS_2 * RANK_2 + 1000 * ROWS_2 * COLS_2]",
         '''mistakes={"C F ne se forme qu'une fois, puis s'applique aux mille vecteurs":
                         [1000 * RANK_2 * (ROWS_2 + COLS_2), 1000 * (ROWS_2 * COLS_2 * RANK_2 + ROWS_2 * COLS_2)],
                     "chacun des mille vecteurs demande son propre F x et son propre C(F x)":
                         [RANK_2 * (ROWS_2 + COLS_2), ROWS_2 * COLS_2 * RANK_2 + 1000 * ROWS_2 * COLS_2],
                     "former C F une fois coûte aussi m n r multiplications":
                         [1000 * RANK_2 * (ROWS_2 + COLS_2), 1000 * ROWS_2 * COLS_2]}'''),
    ]),

    Paper("MB4.3", "Les ingrédients d'un carnet de recettes : surprise, cote, poids corrigé par ½ et son signe, la variante "
                   "toujours positive, puis la saturation et la normalisation d'une mention répétée", [
        ("a", "a number (4 decimals)", "-math.log(F(ORANGE_3, N_3))",
         '''decimals=4,
           mistakes={"une surprise est positive : −ln p, avec p = n/N plus petit que 1": math.log(F(ORANGE_3, N_3)),
                     "le logarithme est népérien": -math.log10(F(ORANGE_3, N_3)),
                     "le logarithme est népérien, pas en base 2": -math.log2(F(ORANGE_3, N_3))}'''),
        ("b", "an irreducible fraction, between quotes", "F(ORANGE_3, N_3 - ORANGE_3)",
         '''kind="fraction", simplified=True,
           mistakes={"la cote divise le nombre de fiches qui contiennent l'ingrédient par le nombre de celles qui ne le "
                     "contiennent pas": F(ORANGE_3, N_3),
                     "la cote de présence est n/(N − n), pas son inverse": F(N_3 - ORANGE_3, ORANGE_3)}'''),
        ("c", "a number (4 decimals)", "weight_3(ORANGE_3)",
         '''decimals=4,
           mistakes={"le poids corrigé met N − n + ½ au numérateur": -weight_3(ORANGE_3),
                     "la correction ajoute ½ à chaque compte": weight_3(ORANGE_3, half=0),
                     "la correction ajoute ½, pas 1": weight_3(ORANGE_3, half=1),
                     "le logarithme est népérien, pas en base 2": weight_3(ORANGE_3) / math.log(2)}'''),
        ("d", "a number (4 decimals)", "weight_3(EGGS_3)",
         '''decimals=4,
           mistakes={"le poids corrigé met N − n + ½ au numérateur": -weight_3(EGGS_3),
                     "la correction ajoute ½ à chaque compte": weight_3(EGGS_3, half=0),
                     "la correction ajoute ½, pas 1": weight_3(EGGS_3, half=1),
                     "le logarithme est népérien, pas en base 2": weight_3(EGGS_3) / math.log(2)}'''),
        ("e", "an integer", "next(n for n in range(N_3 + 1) if weight_3(n) < 0)",
         '''mistakes={"pour n = N/2, le poids corrigé est nul : nul n'est pas négatif":
                         next(n for n in range(N_3 + 1) if weight_3(n) <= 0),
                     "la question demande le plus petit n pour lequel le poids est négatif":
                         next(n for n in range(N_3 + 1) if weight_3(n) <= 0) - 1}'''),
        ("f", "a number (4 decimals)", "variant_3(EGGS_3)",
         '''decimals=4,
           mistakes={"réduis au même dénominateur : n + ½ + N − n + ½ = N + 1": math.log(N_3 / (EGGS_3 + F(1, 2))),
                     "la variante garde le ½ au dénominateur": math.log((N_3 + 1) / EGGS_3),
                     "le logarithme est népérien, pas en base 2": variant_3(EGGS_3) / math.log(2)}'''),
        ("g", "a list of 3 numbers (4 decimals): s(1), s(2), s(10)", "floats([saturation_3(x) for x in (1, 2, 10)])",
         '''decimals=4,
           mistakes={"la saturation n'est pas le compte brut : elle plafonne": [1.0, 2.0, 10.0],
                     "s(x) = x(k₁ + 1)/(x + k₁) : le compte x est aussi au numérateur":
                         floats([F(K1_3 + 1, x + K1_3) for x in (1, 2, 10)])}'''),
        ("h", "an irreducible fraction, between quotes", "(saturation_3(10) - saturation_3(9)) / (saturation_3(1) - saturation_3(0))",
         '''kind="fraction", simplified=True,
           mistakes={"la dixième mention, c'est ce qu'elle ajoute : s(10) − s(9)": saturation_3(10) / saturation_3(1),
                     "la dixième mention fait passer de 9 à 10 mentions": saturation_3(11) - saturation_3(10)}'''),
        ("i", "a list of 2 numbers (4 decimals): b = ¼, then b = ½",
         "floats([normalised_3(3, 2, F(1, 4)), normalised_3(3, 2, F(1, 2))])",
         '''decimals=4,
           mistakes={"une fiche plus longue que la moyenne voit sa saturation baisser": floats([saturation_3(3)] * 2),
                     "le facteur est 1 − b + b ℓ : c'est b qui pèse sur ℓ":
                         floats([normalised_3(3, 2, F(1, 4), swap=True), normalised_3(3, 2, F(1, 2), swap=True)])}'''),
    ]),

    Paper("MB4.4", "Trois jurys classent cinq pâtissiers : les points de Borda, la somme des 1/(c + rang) pour c = 2 et "
                   "c = 10, et la somme des notes qui change de gagnant quand un jury passe de 20 à 100 points", [
        ("a", "a list of 5 integers: A, B, C, D, E", "borda_4()",
         '''mistakes={"un rang j rapporte n − j points : la première place rapporte le plus": rank_sums_4(),
                     "la dernière place rapporte 0 point": borda_4(start=1),
                     "le rang j rapporte n − j points : la première place n − 1, la dernière 0 (pas l'inverse)":
                         [sum(j - 1 for j in col) for col in zip(*ranks_4())]}'''),
        ("b", "a list of 5 numbers (4 decimals): A to E, for c = 2", "floats(reciprocal_sum_4(2))",
         '''decimals=4,
           mistakes={"garde 6 décimales dans chaque terme 1/(c + j), et n'arrondis que la somme": reciprocal_sum_rounded_terms_4(2),
                     "c s'ajoute au rang, il ne le multiplie pas": floats(reciprocal_sum_4(2, mode="times")),
                     "la fusion additionne les contributions des trois jurys, elle ne les moyenne pas":
                         floats(reciprocal_sum_4(2, mode="mean"))}'''),
        ("c", "a list of 5 numbers (4 decimals): A to E, for c = 10", "floats(reciprocal_sum_4(10))",
         '''decimals=4,
           mistakes={"garde 6 décimales dans chaque terme 1/(c + j), et n'arrondis que la somme": reciprocal_sum_rounded_terms_4(10),
                     "c s'ajoute au rang, il ne le multiplie pas": floats(reciprocal_sum_4(10, mode="times")),
                     "la fusion additionne les contributions des trois jurys, elle ne les moyenne pas":
                         floats(reciprocal_sum_4(10, mode="mean"))}'''),
        ("d", "a list of 5 integers: A to E", "[sum(col) for col in zip(*MARKS_4)]",
         '''mistakes={"la question demande la somme des trois notes, pas leur moyenne":
                         floats([F(sum(col), 3) for col in zip(*MARKS_4)]),
                     "on additionne les notes, pas les rangs": rank_sums_4()}'''),
        ("e", "a list of 5 integers: A to E", "[sum(col) for col in zip(*rescaled_4(2))]",
         '''mistakes={"seul le jury de la presse change d'échelle": [5 * sum(col) for col in zip(*MARKS_4)],
                     "c'est le jury de la presse qui passe sur 100": [sum(col) for col in zip(*rescaled_4(0))]}'''),
        ("f", "a number", "tie_4()",
         '''decimals=6,
           mistakes={"A reçoit aussi la contribution de sa cinquième place": tie_4(drop_last_of_a=True),
                     "c est positif : vérifie les signes quand tu développes": -tie_4()}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (SymPy for the reduced form and the equation of MB4.4 f,
# exact fractions where the calculation is exact, math elsewhere)
import math
from fractions import Fraction as F

import numpy as np
import sympy as sp


def floats(values):
    """A number, a vector or a matrix (fractions, SymPy, NumPy) as a float or nested lists of floats (-0.0 written 0.0)."""
    return (np.round(np.asarray(values, dtype=float), 12) + 0.0).tolist()


# MB4.1: four bakeries (Port, Gare, Halles, Moulin) x five products, in tens; G = [[1, 1], [0, 2]]
M_1 = sp.Matrix([[20, 6, 16, 12, 8], [8, 10, 14, 20, 7], [12, 4, 10, 8, 5], [16, 2, 10, 4, 5]])
G_1 = sp.Matrix([[1, 1], [0, 2]])
RREF_1, PIVOTS_1 = M_1.rref()
R_1 = len(PIVOTS_1)
C_1, F_1 = M_1[:, list(PIVOTS_1)], RREF_1[:R_1, :]
assert C_1 * F_1 == M_1


def swapped_coefficients_1(F_):
    """The classic error of b): in the columns that are not pivots, the coefficients of the two pivot columns swapped."""
    W = F_.copy()
    for j in range(W.cols):
        if j not in PIVOTS_1:
            W[0, j], W[1, j] = F_[1, j], F_[0, j]
    return W


def stored(m, n, r):
    return r * (m + n)


def free(m, n, r):
    return r * (m + n - r)


# MB4.2: a 60 x 450 table (60 stations, 450 days: deviations of the pressure from the normal, in hPa), singular values
# 320, 150, 60, 15, then 56 times 3
S_2 = [320, 150, 60, 15] + [3] * 56
ROWS_2, COLS_2 = 60, 450
ENERGY_2 = sum(s * s for s in S_2)


def share_2(r, values=S_2, power=2):
    """The share of the first r singular values (power 1: the classic error, values instead of squares)."""
    return sum(s ** power for s in values[:r]) / sum(s ** power for s in values)


def effective_rank_2(level=0.99, power=2):
    return next(r for r in range(1, len(S_2) + 1) if share_2(r, power=power) >= level)


RANK_2 = effective_rank_2()


# MB4.3: a notebook of N = 80 recipe cards; orange blossom in 4, eggs in 62; the saturation with k1 = 2
N_3, ORANGE_3, EGGS_3, K1_3 = 80, 4, 62, 2


def weight_3(n, N=N_3, half=F(1, 2)):
    """The corrected weight ln((N − n + half)/(n + half)); half = 0 or 1: the classic errors."""
    return math.log((N - n + half) / (n + half))


def variant_3(n, N=N_3):
    return math.log((N + 1) / (n + F(1, 2)))


def saturation_3(x, k1=K1_3):
    return F(x * (k1 + 1)) / (x + k1)


def normalised_3(x, ell, b, k1=K1_3, swap=False):
    """x (k1 + 1) / (x + k1 nu), nu = 1 − b + b ell (swap: the classic error nu = b + (1 − b) ell)."""
    nu = b + (1 - b) * ell if swap else 1 - b + b * ell
    return F(x * (k1 + 1)) / (x + k1 * nu)


# MB4.4: marks /20 of A, B, C, D, E by the juries of the chefs, of the public and of the press; c = 2 and c = 10
MARKS_4 = [[17, 15, 12, 11, 8], [16, 14, 8, 13, 11], [6, 14, 18, 10, 13]]
N_4 = 5


def ranks_4(marks=MARKS_4):
    """The rank of each candidate for each jury: 1 + the number of higher marks (no ties)."""
    return [[1 + sum(other > mine for other in row) for mine in row] for row in marks]


def rank_sums_4():
    return [sum(col) for col in zip(*ranks_4())]


def borda_4(start=0):
    """n − j points at rank j (start=1: the classic error n − j + 1)."""
    return [sum(N_4 - j + start for j in col) for col in zip(*ranks_4())]


def reciprocal_sum_4(c, mode="sum"):
    """The sum of the 1/(c + rank), exact; mode "times": 1/(c rank), "mean": divided by 3 (the classic errors)."""
    out = []
    for col in zip(*ranks_4()):
        total = sum(F(1, c * j) if mode == "times" else F(1, c + j) for j in col)
        out.append(total / 3 if mode == "mean" else total)
    return out


def reciprocal_sum_rounded_terms_4(c):
    """The classic error: each term 1/(c + j) rounded to 4 decimals before the sum."""
    return [round(sum(round(1 / (c + j), 4) for j in col), 4) for col in zip(*ranks_4())]


def rescaled_4(jury):
    """The marks with those of one jury multiplied by 5 (marked out of 100)."""
    return [[5 * x for x in row] if k == jury else row for k, row in enumerate(MARKS_4)]


def tie_4(drop_last_of_a=False):
    """The c > 0 where A and B have the same sum of the 1/(c + rank) (drop_last_of_a: A's fifth place forgotten)."""
    c = sp.symbols("c", positive=True)
    ranks = list(zip(*ranks_4()))
    a = [j for j in ranks[0] if not (drop_last_of_a and j == max(ranks[0]))]
    solutions = sp.solve(sp.together(sum(1 / (c + j) for j in a) - sum(1 / (c + j) for j in ranks[1])), c)
    assert len(solutions) == 1
    return float(solutions[0])'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ MB4.1 à MB4.4)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question "
               "(« a number » sans décimales : la valeur exacte, ce calcul tombe juste) ;\n"
               "- une fraction irréductible entre guillemets, `\"5/8\"` ;\n"
               "- une liste `[0.2, -1]`, dans l'ordre que dit la question ; une matrice comme la liste de ses **lignes**, "
               "`[[1, 0], [-2, 3]]` ; une matrice de valeurs exactes peut contenir des fractions entre guillemets.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")


def paper_part(kind: str) -> list:
    """The cells of Part 0."""
    return paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO)


# ---------------------------------------------------------------------------
# Notebook exercises: your library (MB4.8, MB4.9)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to D)
import contextlib
import math
import os
import re
import sys
import time

import matplotlib.pyplot as plt
import numpy as np

from wbm.errors import MymathMissingError
from wbm.nbtools import StopCheck, checked, drawn, filled, fr, run_pytest_group, verdict

TEST_MB4 = "tests/test_mb4_ranks.py"               # the tests of mymath/ranks.py
REF = wbm.load_mymath("ref", alias="mymath_ref")  # the reference: the checks of the hidden cases rely on it
ref_ranks = REF.ranks


def shown(value, digits=4):
    """A short text for a result of the learner's code (the check messages): numbers rounded, as lists."""
    if value is None:
        return "None"
    try:
        return str(np.round(np.asarray(value, dtype=float), digits).tolist())[:160]
    except (TypeError, ValueError):
        return repr(value)[:160]


def check_answer(ex_id, value, hint=None):
    """wbm.check(ex_id, value, computed=True). For a list that holds True or False, the message gives only how many
    elements are right, not the place of the first wrong one (it would let you guess the booleans one by one).
    hint(value), when given, may return a targeted « Piste » for a wrong answer (None otherwise)."""
    holds_bool = isinstance(value, (list, tuple)) and any(isinstance(v, (bool, np.bool_)) for v in value)
    if not holds_bool and hint is None:
        return wbm.check(ex_id, value, computed=True)
    result = wbm.check(ex_id, value, computed=True, quiet=True)
    message = result.message
    if holds_bool:
        for cut in (" Le premier faux est le ", " Premier élément faux à l'indice "):
            message = message.split(cut)[0]
    if hint is not None and result.status not in ("correct", "pending", "unknown") and "Piste" not in message:
        try:
            extra = hint(value)
        except Exception:  # noqa: BLE001 - an odd answer: no targeted hint
            extra = None
        if extra:
            message = f"{message} Piste : {extra}"
    icon = {"correct": "✅", "pending": "⏳", "unknown": "❓"}.get(result.status, "❌")
    print(f"{icon} Ex {ex_id} : {message}")
    return result


def passes(ex_id, value):
    """True when value is the hidden answer ex_id (wbm.check, computed=True, nothing printed)."""
    try:
        return bool(wbm.check(ex_id, value, computed=True, quiet=True).passed)
    except Exception:  # noqa: BLE001 - an odd value is not the answer
        return False


def reporter(results, stop=True):
    """A function report(ok, success, failure) that prints one ✅ or ❌ line, keeps the verdict in results, and (stop)
    ends the check at the first ❌ (StopCheck, caught by checked)."""
    def report(ok, success, failure):
        results.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))
        if not ok and stop:
            raise StopCheck
    return report


def as_floats(value):
    """value as a float array, or None when it is not an array of numbers."""
    try:
        return np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        return None


def matches(got, want, rtol=1e-9, atol=1e-12):
    """True when got is an array of numbers of the shape of want and equal to it up to rounding (no error for an odd
    got)."""
    arr = as_floats(got)
    want = np.asarray(want, dtype=float)
    return arr is not None and arr.shape == want.shape and bool(np.allclose(arr, want, rtol=rtol, atol=atol,
                                                                            equal_nan=True))


def line_with(ax, xs, ys, rtol=1e-7, atol=1e-9):
    """True when a line of ax has exactly the abscissas xs and the ordinates ys."""
    xs, ys = np.asarray(xs, dtype=float), np.asarray(ys, dtype=float)
    for line in ax.lines:
        x, y = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
        if x.shape == xs.shape and y.shape == ys.shape and np.allclose(x, xs, rtol=rtol, atol=atol) \\
                and np.allclose(y, ys, rtol=rtol, atol=atol, equal_nan=True):
            return True
    return False


def call_safely(label, function, *args, **kwargs):
    """function(*args, **kwargs); an error of the learner's code becomes one ❌ line naming the call (StopCheck)."""
    try:
        return function(*args, **kwargs)
    except (NotImplementedError, MymathMissingError):
        raise
    except Exception as exc:  # noqa: BLE001 - the learner's error, reported with the name of the call
        print(f"❌ {label} : ton code lève {type(exc).__name__} : {str(exc)[:200]}")
        raise StopCheck from None


class CodeFrom(BaseException):
    """Raised inside code_from when watched code starts (a BaseException: a broad except of the learner's code does
    not hide it)."""


def code_key(code):
    """What identifies a compiled function whatever its file: its bytecode, its names and its constants."""
    return (code.co_code, code.co_names, tuple(c.co_name if hasattr(c, "co_code") else repr(c) for c in code.co_consts))


def code_keys_of_file(path):
    """The code_key of every function of a Python file, compiled but not run (to recognise a copy of that file)."""
    keys, todo = set(), [compile(open(path, encoding="utf-8").read(), str(path), "exec")]
    while todo:
        code = todo.pop()
        todo += [c for c in code.co_consts if hasattr(c, "co_code")]
        if code.co_name != "<module>" and len(code.co_code) >= 40:
            keys.add(code_key(code))
    return keys


@contextlib.contextmanager
def code_from(places, twins=()):
    """Inside the block, the start of any Python code (a function or a module body) of a file among places (files, or
    folders with everything under them), or of a function whose code_key is among twins (a copy of such a function),
    stops the block; yields the list of the names seen ("ranks.borda_scores"). The learner's function must not run that
    code (mymath in a corrected function, the hidden module of a challenge). Without sys.monitoring (Python < 3.12) or
    a free tool id, nothing is watched."""
    places = [os.path.realpath(str(place)) for place in places]
    monitoring, tool, seen, inside = getattr(sys, "monitoring", None), None, [], {}
    for candidate in ((4, 3, 2) if monitoring is not None else ()):
        try:
            monitoring.use_tool_id(candidate, "code_from")
        except ValueError:                               # taken by another tool
            continue
        tool = candidate
        break
    if tool is not None:
        def on_start(code, offset):
            name = code.co_filename
            if name not in inside:
                real = os.path.realpath(name) if os.path.exists(name) else name
                inside[name] = any(real == place or real.startswith(place + os.sep) for place in places)
            if inside[name] or (twins and code_key(code) in twins):
                seen.append(f"{os.path.splitext(os.path.basename(name))[0]}.{code.co_name}")
                raise CodeFrom
            return monitoring.DISABLE                    # other code: not watched again until the end of the block

        monitoring.register_callback(tool, monitoring.events.PY_START, on_start)
        monitoring.set_events(tool, monitoring.events.PY_START)
    try:
        yield seen
    except CodeFrom:
        pass
    finally:
        if tool is not None:
            monitoring.set_events(tool, 0)
            monitoring.register_callback(tool, monitoring.events.PY_START, None)
            monitoring.free_tool_id(tool)
            monitoring.restart_events()'''

DATA = '''# The data of the paper exercises (02_exercices.md)
M_1 = np.array([[20.0, 6, 16, 12, 8], [8, 10, 14, 20, 7], [12, 4, 10, 8, 5], [16, 2, 10, 4, 5]])   # MB4.1: the sales (in
#   tens) of the bakeries Port, Gare, Halles, Moulin (rows) for baguettes, croissants, pains de campagne, pains au
#   chocolat, tartelettes (columns)
S_2 = np.array([320.0, 150.0, 60.0, 15.0] + [3.0] * 56)     # MB4.2: the singular values of the 60 x 450 table
RANKINGS_4 = np.array([[0, 1, 2, 3, 4], [0, 1, 3, 4, 2], [2, 1, 4, 3, 0]])   # MB4.4: the rankings of the juries of the
#   chefs, of the public and of the press, best first (the pastry cooks A, B, C, D, E numbered 0 to 4)
for _array in (M_1, S_2, RANKINGS_4):
    _array.setflags(write=False)   # read only: a change in place raises an error at the line that does it'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="MB4")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en MB3). Ouvre ta copie `mon_travail/mymath/ranks.py`, lis la docstring "
         "du module (ses conventions, et ce qui est permis) puis celle de la fonction, remplace chaque "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Dans le notebook, appelle tes fonctions par "
         "`mymath.ranks.<nom>` (par exemple `mymath.ranks.rank_factorization(M)`), ou donne-leur un nom court "
         "(`rank_factorization = mymath.ranks.rank_factorization`) dans une cellule exécutée après le rechargement. "
         "⚠️ Le squelette n'importe rien : ajoute en tête du fichier `import math`, `from fractions import Fraction` "
         "et `import numpy as np`, et `from .matrices import rref` si tu reprends ton `rref` de M09a (sinon, recopie-le "
         "dans une fonction privée `_rref`). NumPy est permis (`@` compris), mais rien de `np.linalg`, ni SciPy "
         "(`scipy.linalg`, `scipy.stats.rankdata`), ni SymPy : les tests comparent tes résultats aux leurs, et un test "
         "lit ton module ; dans `borda_scores`, ni `np.argsort` ni `np.lexsort`. Les candidats sont numérotés à partir "
         "de 0, un rang commence à 1 ; ne modifie jamais les tableaux reçus. Hors de `mymath`, le notebook peut se "
         "servir de tout NumPy et de SciPy.")

REMINDER = ("> Même mode d'emploi qu'en MB4.8 : écris les fonctions dans ta copie `mon_travail/mymath/ranks.py`, "
            "**enregistre**, puis exécute les cellules ci-dessous ; la première recharge ta librairie.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of ranks.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("todo", f'run_pytest_group(TEST_MB4, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_MB4, "{keyword}", impl="ref")')]


def answers_check(ex_id: str, letters: str, hints: dict | None = None) -> str:
    """The check cell of the answers a), b)... of a notebook exercise: one check_answer each. ``hints`` maps a letter to
    the code of a function value -> targeted hint (or None), written in the cell."""
    names = ", ".join(f"answer_{ex_id.replace('.', '_')}{letter}" for letter in letters)
    if not hints:
        return (f'for letter, answer in zip("{letters}", [{names}]):\n'
                f'    check_answer(f"{ex_id}{{letter}}", answer)')
    tag = ex_id.replace(".", "_")
    return "\n".join(f'check_answer("{ex_id}{letter}", answer_{tag}{letter}'
                     + (f", hint={hints[letter]})" if letter in hints else ")") for letter in letters)


def look(text: str, after: str = "") -> tuple:
    """The cell « Ce qu'il faut regarder » shown after the check (questions of 02_exercices.md; answers in 05)."""
    return ("md", f"**Ce qu'il faut regarder**{after} : {text} Les réponses sont dans `05_solutions.md`, section "
                  "Notebook.")


# ---------------------------------------------------------------------------
# MB4.8 · rank_factorization
# ---------------------------------------------------------------------------
GIVEN_8 = '''# Measurements of 5 quantities on 6 samples of the foundry's laboratory, each a mix of two base alloys: a table of
# rank 2, rounded to the thousandth
M_8 = np.array(__M_8__)
M_8.setflags(write=False)'''

NOTE_8 = (r"Les contrôles (2-D, non vide, nombres finis ; `tol` réel $\ge 0$, ni `nan` ni booléen), puis "
          r"`R, pivots = rref(M, tol)` sur une copie en flottants, `C = M[:, pivots]` (les colonnes de $\mathbf{M}$ "
          r"elle-même) et `F = R[:len(pivots)]`. a) $\mathbf{F} = \begin{pmatrix} 1 & 0 & 0{,}5 & 0 & 0{,}25 \\ 0 & 1 & 1 "
          r"& 2 & 0{,}5 \end{pmatrix}$, comme MB4.1 b). b) 5, puis 2. c) $\approx 0{,}000828$, l'ordre de grandeur de "
          r"l'arrondi au millième des mesures.")

MB4_8 = Ex(
    "MB4.8", "🔨", 1, 30, "La factorisation de rang C F : les colonnes pivots de M et les lignes non nulles de sa forme "
    "échelonnée réduite · `rank_factorization`",
    "programmer la factorisation de rang par les colonnes pivots, puis retrouver MB4.1 et voir le rôle de la tolérance "
    "sur un tableau mesuré.",
    "fiche §1 ; M09a (`rref`), M12a (colonnes pivots, rang numérique) ; Ex MB4.1", tracks="C, E", mymath="ranks.py",
    note=NOTE_8, given=GIVEN_8,
    body=HOWTO + r"""

Écris `rank_factorization(M, tol=1e-10)` (fiche §1), en suivant sa docstring : contrôle $\mathbf{M}$ (un tableau 2-D non vide de nombres finis) et `tol` (un réel $\ge 0$, ni `nan` ni un booléen) ; réduis une copie en flottants comme le fait `rref` de M09a (tu peux importer `rref` de `.matrices`, ou le recopier dans une fonction privée `_rref`), et garde ses colonnes pivots ; $\mathbf{C}$ est faite des colonnes pivots de $\mathbf{M}$ elle-même, $\mathbf{F}$ des $r$ premières lignes de la forme réduite.

**L'usage.** Le notebook fournit `M_8`, les mesures de 5 grandeurs sur 6 échantillons du laboratoire de la fonderie (fiche §2), chacun mélange de deux alliages de base (un tableau de rang 2, arrondi au millième). Avec ta fonction :
- a) `rank_factorization(M_1)`, où `M_1` est le tableau des boulangeries de MB4.1 (cellule de données) : la matrice $\mathbf{F}$ (à comparer à ta copie) ;
- b) le rang trouvé pour `M_8` avec `tol=1e-10`, puis avec `tol=1e-2` (une liste de 2 entiers) ;
- c) avec `tol=1e-2`, le plus grand écart $\lvert(\mathbf{C}\mathbf{F})_{ij} - (\mathbf{M}_8)_{ij}\rvert$ (un nombre).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `rank_factorization` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_rank_factorization_ or test_module_uses_") + [
        ("md", "**L'usage** : le tableau des boulangeries, puis les mesures du laboratoire et deux tolérances."),
        ("todo", '''answer_MB4_8a = answer_MB4_8b = answer_MB4_8c = ...
with wbm.attempt("MB4.8"):          # if you call rank_factorization here: ⏳ while it is not written
    answer_MB4_8a = ...  # a) a 2 x 5 matrix, as computed: the F of rank_factorization(M_1)
    answer_MB4_8b = ...  # b) a list of 2 integers: the rank found for M_8 with tol=1e-10, then with tol=1e-2
    answer_MB4_8c = ...  # c) a number, as computed: with tol=1e-2, the largest gap |(C F)_ij - (M_8)_ij|'''),
        ("check", answers_check("MB4.8", "abc")),
        ("solution", '''rank_factorization = mymath.ranks.rank_factorization
C_8a, F_8a = rank_factorization(M_1)
answer_MB4_8a = F_8a.tolist()
answer_MB4_8b = [rank_factorization(M_8, tol=tol)[0].shape[1] for tol in (1e-10, 1e-2)]
C_8, F_8 = rank_factorization(M_8, tol=1e-2)
answer_MB4_8c = float(np.max(np.abs(C_8 @ F_8 - M_8)))
print("a)", answer_MB4_8a, " b)", answer_MB4_8b, " c)", round(answer_MB4_8c, 7))
print("   valeurs singulières de M_8 :", np.round(np.linalg.svd(M_8, compute_uv=False), 6).tolist())'''),
        ("record", '''import sympy as sp_8r


def pivots_and_form_8r(M, tol):
    """The oracle: the reduction of rref (M09a) written again, partial pivoting, entries at most tol set to 0."""
    R = np.array(M, dtype=float)
    pivots, row = [], 0
    for col in range(R.shape[1]):
        if row == R.shape[0]:
            break
        best = row + int(np.argmax(np.abs(R[row:, col])))
        if abs(R[best, col]) <= tol:
            continue
        R[[row, best]] = R[[best, row]]
        R[row] = R[row] / R[row, col]
        for i in range(R.shape[0]):
            if i != row:
                R[i] = R[i] - R[i, col] * R[row]
        pivots.append(col)
        row += 1
    R[np.abs(R) <= tol] = 0.0
    return pivots, R


sales_8r = sp_8r.Matrix([[20, 6, 16, 12, 8], [8, 10, 14, 20, 7], [12, 4, 10, 8, 5], [16, 2, 10, 4, 5]])
reduced_8r, pivots_8r = sales_8r.rref()                                      # exact (SymPy)
wbm.record("MB4.8a", np.array(reduced_8r[:len(pivots_8r), :], dtype=float).tolist(), decimals=6,
           mistakes={"F ne garde que les r lignes non nulles de la forme réduite (relance les tests de rank_factorization)":
                         np.array(reduced_8r, dtype=float).tolist()})
measured_8r = np.array(__M_8__)
wbm.record("MB4.8b", [len(pivots_and_form_8r(measured_8r, tol)[0]) for tol in (1e-10, 1e-2)],
           mistakes={"la liste suit l'ordre de l'énoncé : tol=1e-10 d'abord, puis tol=1e-2":
                         [len(pivots_and_form_8r(measured_8r, tol)[0]) for tol in (1e-2, 1e-10)]})
pivots_c_8r, form_c_8r = pivots_and_form_8r(measured_8r, 1e-2)
gap_8r = float(np.max(np.abs(measured_8r[:, pivots_c_8r] @ form_c_8r[:len(pivots_c_8r)] - measured_8r)))
wbm.record("MB4.8c", gap_8r, decimals=6,
           mistakes={"c) se calcule avec tol=1e-2 : avec tol=1e-10, C F redonne M_8 à l'arrondi près": 0.0})'''),
        ("solution", answers_check("MB4.8", "abc")),
        look("pourquoi la tolérance $10^{-10}$ trouve-t-elle un autre rang ? D'où vient l'écart de c), et quel ordre de "
             "grandeur pouvait-on prévoir ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB4.9 · borda_scores, random_ranking_mrr
# ---------------------------------------------------------------------------
GIVEN_9 = '''# 7 judges rank 9 candidates (numbered 0 to 8): one row per judge, best first
RANKINGS_9 = np.array(__RANKINGS_9__)
RANKINGS_9.setflags(write=False)'''

NOTE_9 = (r"`borda_scores` : les contrôles, puis, pour chaque ligne, `points[row[p]] += n - 1 - p` (la position $p$ est "
          r"le rang $p + 1$ du candidat `row[p]`) ; `random_ranking_mrr` : les contrôles, puis `last = n - q + 1` (ou "
          r"`depth` s'il est plus petit) et la somme des `Fraction(math.comb(n - j, q - 1), math.comb(n, q)) / j`. a) "
          r"$(8, 9, 6, 4, 3)$, comme MB4.4 a). b) $(24, 26, 22, 31, 34, 23, 25, 42, 25)$. c) $\frac{761}{2\,240}$, "
          r"$\frac{341}{560}$ et $\frac{11}{72}$. d) Vrai.")

MB4_9 = Ex(
    "MB4.9", "🔨", 2, 35, "Les points de Borda de classements complets, et le MRR exact d'un ordre tiré au hasard, en "
    "fractions · `borda_scores`, `random_ranking_mrr`",
    "programmer les points de Borda de classements complets et le MRR exact d'un ordre tiré au hasard, puis retrouver "
    "MB4.4 et la valeur $H_n/n$.",
    "fiche §5 et §6 ; R8 (combinaisons) ; Ex MB4.4", tracks="C", mymath="ranks.py", note=NOTE_9, given=GIVEN_9,
    body=REMINDER + r"""

Écris les deux fonctions, en suivant leurs docstrings : pour `borda_scores(rankings)`, contrôle le tableau (2-D, non vide, des entiers, chaque ligne une permutation de $0, \ldots, n - 1$), puis donne au candidat placé à la position $p$ d'une ligne (positions à partir de 0) $n - 1 - p$ points, et additionne sur les lignes ; pour `random_ranking_mrr(n, n_relevant=1, depth=None)`, contrôle les trois arguments (des entiers, pas des booléens, chacun dans son domaine), puis additionne $P(R = j)/j$ en fractions, pour les rangs $j$ qui comptent. Lance les deux groupes de tests.

**L'usage.** La cellule de données de la partie A donne `RANKINGS_4`, les classements des trois jurys de MB4.4 (les pâtissiers A à E numérotés de 0 à 4) ; le notebook fournit `RANKINGS_9`, les classements de 7 juges qui classent 9 candidats. Avec tes fonctions :
- a) les points de Borda de `RANKINGS_4` (une liste de 5 entiers, à comparer à ta copie) ;
- b) les points de Borda de `RANKINGS_9` (une liste de 9 entiers) ;
- c) `random_ranking_mrr(8)`, `random_ranking_mrr(8, n_relevant=3)` et `random_ranking_mrr(12, depth=3)` (une liste de 3 fractions, des `Fraction` ou des chaînes `"p/q"`) ;
- d) vrai ou faux : `random_ranking_mrr(n)` est égal à $H_n/n$, en fractions exactes, pour $n = 1$ à 40.""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `borda_scores`, puis ceux de `random_ranking_mrr` (lis d'abord la ligne qui suit "
                  "chaque ❌ : elle dit ce qui était attendu).")]
    + tests_cells("test_borda_scores_") + tests_cells("test_random_ranking_mrr_") + [
        ("md", "**L'usage** : les trois jurys de MB4.4, sept juges, et trois ordres tirés au hasard."),
        ("todo", '''answer_MB4_9a = answer_MB4_9b = answer_MB4_9c = answer_MB4_9d = ...
with wbm.attempt("MB4.9"):          # if you call your functions here: ⏳ while they are not written
    answer_MB4_9a = ...  # a) a list of 5 integers: the Borda points of RANKINGS_4 (A to E)
    answer_MB4_9b = ...  # b) a list of 9 integers: the Borda points of RANKINGS_9
    answer_MB4_9c = ...  # c) a list of 3 fractions (Fraction, or strings "p/q"): the three calls of the statement
    answer_MB4_9d = ...  # d) True or False: random_ranking_mrr(n) equals H_n / n exactly, for n = 1 to 40'''),
        ("check", answers_check("MB4.9", "abcd")),
        ("solution", '''from fractions import Fraction

borda_scores, random_ranking_mrr = mymath.ranks.borda_scores, mymath.ranks.random_ranking_mrr
answer_MB4_9a = borda_scores(RANKINGS_4).tolist()
answer_MB4_9b = borda_scores(RANKINGS_9).tolist()
answer_MB4_9c = [random_ranking_mrr(8), random_ranking_mrr(8, n_relevant=3), random_ranking_mrr(12, depth=3)]
answer_MB4_9d = all(random_ranking_mrr(n) == sum(Fraction(1, k) for k in range(1, n + 1)) / n for n in range(1, 41))
print("a)", answer_MB4_9a, " b)", answer_MB4_9b, " (gagnant :", int(np.argmax(answer_MB4_9b)), ")")
print("c)", [str(v) for v in answer_MB4_9c], " d)", answer_MB4_9d)'''),
        ("record", '''import itertools
from fractions import Fraction as F_9r

from scipy.stats import rankdata as rankdata_9r

marks_9r = np.array([[17, 15, 12, 11, 8], [16, 14, 8, 13, 11], [6, 14, 18, 10, 13]])   # MB4.4, marks out of 20
ranks_4_9r = rankdata_9r(-marks_9r, axis=1)                                          # the oracle: scipy's ranks
wbm.record("MB4.9a", (5 - ranks_4_9r).sum(axis=0).astype(int).tolist(),
           mistakes={"un rang j rapporte n − j points, la première place le plus (relance les tests de borda_scores)":
                         ranks_4_9r.sum(axis=0).astype(int).tolist(),
                     "une ligne est un ordre (le candidat placé à chaque position), pas la liste des rangs des candidats "
                     "(relance les tests de borda_scores)": [5 * 3 - 3 - int(np.sum(np.array(
                         [[0, 1, 2, 3, 4], [0, 1, 3, 4, 2], [2, 1, 4, 3, 0]])[:, c])) for c in range(5)],
                     "la dernière place rapporte 0 point : n − j, pas n − j + 1 (relance les tests de borda_scores)":
                         (5 - ranks_4_9r + 1).sum(axis=0).astype(int).tolist()})
judges_9r = np.array(__RANKINGS_9__)
ranks_9r = np.argsort(judges_9r, axis=1) + 1                                        # the rank of each candidate
wbm.record("MB4.9b", (judges_9r.shape[1] - ranks_9r).sum(axis=0).tolist(),
           mistakes={"un rang j rapporte n − j points, la première place le plus (relance les tests de borda_scores)":
                         ranks_9r.sum(axis=0).tolist(),
                     "une ligne est un ordre (le candidat placé à chaque position), pas la liste des rangs des candidats "
                     "(relance les tests de borda_scores)": (judges_9r.shape[1] - 1 - judges_9r).sum(axis=0).tolist()})


def mrr_9r(n, q=1, depth=None):
    """The oracle: the mean of 1/R over the C(n, q) sets of positions of the q relevant items, equally likely."""
    total, count = F_9r(0), 0
    for places in itertools.combinations(range(n), q):
        first = min(places) + 1
        total += F_9r(1, first) if depth is None or first <= depth else 0
        count += 1
    return total / count


calls_9r = [mrr_9r(8), mrr_9r(8, 3), mrr_9r(12, depth=3)]
wbm.record("MB4.9c", [float(v) for v in calls_9r], decimals=6,
           mistakes={"avec n_relevant=3, R est le rang du premier des trois pertinents : P(R = j) = C(n − j, q − 1)/C(n, q) "
                     "(relance les tests de random_ranking_mrr)": [float(calls_9r[0])] * 2 + [float(calls_9r[2])],
                     "avec depth=3, les rangs au-delà de 3 comptent 0 (relance les tests de random_ranking_mrr)":
                         [float(v) for v in calls_9r[:2]] + [float(mrr_9r(12))]})
wbm.record("MB4.9d", True,
           mistakes={"random_ranking_mrr(n) vaut H_n/n : compare des Fraction exactes avec ==, pas des flottants ; si elles "
                     "diffèrent vraiment, relance les tests de random_ranking_mrr": False})'''),
        ("solution", answers_check("MB4.9", "abcd")),
        look("le classement des 9 candidats par leurs points de Borda est-il celui de la somme de leurs rangs ? Combien "
             "d'ordres faudrait-il énumérer pour c) avec $n = 12$, et combien de termes additionne ta fonction ?"),
    ],
)

PART_A = Part("A", "Ta librairie : la factorisation de rang, les points de Borda et le MRR d'un ordre au hasard",
              "Fiche §1, §5 et §6. Les trois fonctions de `mymath/ranks.py`, leurs tests, et un usage de chacune. La "
              "cellule de données ci-dessous recopie les données des exercices papier.",
              given=TOOLS + "\n\n\n" + DATA, exercises=[MB4_8, MB4_9])

# ---------------------------------------------------------------------------
# Notebook exercises: predict, draw (MB4.10, MB4.11)
# ---------------------------------------------------------------------------
HINT_10 = '''def hint_10d(value):
    """A targeted hint for d): H_n / n instead of the simulation, or plausible means of another draw."""
    if passes("MB4.10e", value):
        return "d) est la moyenne simulée de 1/R, pas H_n/n : relève la moyenne de tes 20 000 valeurs"
    values = as_floats(value)
    if values is None or values.shape != (3,):
        return None
    plausible = []
    for got, n in zip(values, (10, 100, 1000)):
        mean = float(ref_ranks.random_ranking_mrr(n))                  # the exact value, by the reference
        variance = sum(1 / k ** 2 for k in range(1, n + 1)) / n - mean ** 2
        plausible.append(abs(got - mean) <= 4 * math.sqrt(variance / 20000))
    if all(plausible):
        return ("tes moyennes sont plausibles, mais ce ne sont pas celles du tirage demandé : un seul générateur "
                "np.random.default_rng(7510), créé une fois, puis n = 10, 100 et 1 000 dans cet ordre, 20 000 fois "
                "rng.permutation(n) pour chacun, et le rang int(np.flatnonzero(order == 0)[0]) + 1")
    return None


'''

NOTE_10 = (r"Prédictions attendues : a) (C) ; b) (A) ; c) (B). La simulation : `rr = [1 / (int(np.flatnonzero(order == 0)"
           r"[0]) + 1) for order in (rng.permutation(n) for _ in range(20000))]`. d) $(0{,}292134 ;\ 0{,}051144 ;\ "
           r"0{,}007727)$, à des erreurs types $(0{,}0019 ;\ 0{,}0008 ;\ 0{,}0003)$ ; e) $(0{,}292897 ;\ 0{,}051874 ;\ "
           r"0{,}007485)$ ; f) $(0{,}230259 ;\ 0{,}046052 ;\ 0{,}006908)$ ; g) vrai.")

MB4_10 = Ex(
    "MB4.10", "🔮", 1, 20, "Prédire le MRR d'un ordre tiré au hasard parmi 10, 100 puis 1 000 candidats, puis le simuler et "
    "le comparer à H_n/n",
    "prévoir comment le MRR d'un ordre tiré au hasard décroît avec le nombre de candidats, puis le simuler et le comparer "
    "à $H_n/n$.", "fiche §6 ; M02a (rectangles), R8 ; Ex MB4.9", tracks="C", hypothesis=True, note=NOTE_10,
    body=r"""Un seul des $n$ candidats est pertinent, et l'ordre est tiré au hasard parmi les $n!$ ordres. **Avant d'exécuter quoi que ce soit**, prédis :
- a) pour $n = 10$, le MRR est le plus proche de : (A) 0,1 ; (B) 0,5 ; (C) 0,3 (une lettre) ;
- b) de $n = 100$ à $n = 1\,000$, le MRR est divisé par environ : (A) 7 ; (B) 10 ; (C) 3 (une lettre) ;
- c) de $n = 10$ à $n = 1\,000$, le produit $n \times \text{MRR}$ : (A) ne change presque pas ; (B) augmente de 4 à 5 ; (C) est multiplié par environ 100 (une lettre).

Puis, une fois tes prédictions écrites et vérifiées, simule : avec `rng = np.random.default_rng(7510)`, pour $n = 10$, 100 puis 1 000, dans cet ordre, tire 20 000 fois `order = rng.permutation(n)` ; le pertinent est l'objet 0, et son rang est `int(np.flatnonzero(order == 0)[0]) + 1`. Relève, chaque fois pour $n = 10$, 100 et 1 000 (une liste de 3 nombres) :
- d) la moyenne simulée de $1/R$ ;
- e) $H_n/n$ ;
- f) $\frac{\ln n}{n}$ ;
- g) vrai ou faux : chaque moyenne simulée est à moins de 3 erreurs types de $H_n/n$.

La vérification de l'expérience ne s'exécute qu'une fois tes trois prédictions écrites.""",
    todo='''prediction_MB4_10a = ...  # a) "A", "B" or "C": for n = 10, the MRR is closest to (A) 0.1, (B) 0.5, (C) 0.3
prediction_MB4_10b = ...  # b) "A", "B" or "C": from n = 100 to n = 1000, the MRR is divided by about (A) 7, (B) 10, (C) 3
prediction_MB4_10c = ...  # c) "A", "B" or "C": from n = 10 to n = 1000, n x MRR (A) hardly changes, (B) grows by 4 to 5, (C) is multiplied by about 100''',
    check='''for letter, prediction in zip("abc", [prediction_MB4_10a, prediction_MB4_10b, prediction_MB4_10c]):
    wbm.check(f"MB4.10{letter}", prediction)''',
    record='''from fractions import Fraction as F_10r

H_10r = {n: sum(F_10r(1, k) for k in range(1, n + 1)) for n in (10, 100, 1000)}
mrr_10r = {n: float(H_10r[n] / n) for n in H_10r}
closest_a_10r = min(zip("ABC", (0.1, 0.5, 0.3)), key=lambda pair: abs(pair[1] - mrr_10r[10]))[0]
wbm.record("MB4.10a", closest_a_10r, prediction=True,
           mistakes={"1/R vaut 1 au rang 1, 1/2 au rang 2… : sa moyenne n'est pas une chance sur n, chaque rang j apporte "
                     "1/(n j)": "A",
                     "R est uniforme sur {1, …, 10} : le rang 1 n'a qu'une chance sur 10": "B"})
closest_b_10r = min(zip("ABC", (7, 10, 3)), key=lambda pair: abs(pair[1] - mrr_10r[100] / mrr_10r[1000]))[0]
wbm.record("MB4.10b", closest_b_10r, prediction=True,
           mistakes={"le MRR vaut H_n/n : regarde ce que devient H_n quand n est multiplié par 10 (fiche §6)": "B",
                     "H_n ne grandit que comme ln n : passer de 100 à 1 000 n'ajoute qu'environ ln 10 à H_n": "C"})
gain_c_10r = float(H_10r[1000] - H_10r[10])
wbm.record("MB4.10c", "B" if 4 <= gain_c_10r <= 5 else "A", prediction=True,
           mistakes={"n × MRR = H_n : relis comment H_n grandit avec n (fiche §6, l'encadrement par des rectangles)":
                         "A",
                     "H_n grandit comme ln n, pas comme n": "C"})''',
    after=[
        ("md", "**L'expérience.** Écris-la une fois tes trois prédictions vérifiées ; sa vérification ne s'exécute qu'à cette "
               "condition."),
        ("todo", '''answer_MB4_10d = answer_MB4_10e = answer_MB4_10f = answer_MB4_10g = ...
with wbm.attempt("MB4.10"):          # your simulation
    rng = np.random.default_rng(7510)   # one generator, created once, for n = 10, 100, 1000 in this order
    answer_MB4_10d = ...  # d) a list of 3 numbers, as computed: the simulated mean of 1/R for n = 10, 100, 1000
    answer_MB4_10e = ...  # e) a list of 3 numbers, as computed: H_n / n for n = 10, 100, 1000
    answer_MB4_10f = ...  # f) a list of 3 numbers, as computed: ln(n) / n for n = 10, 100, 1000
    answer_MB4_10g = ...  # g) True or False: each simulated mean is within 3 standard errors of H_n / n'''),
        ("check", guarded(HINT_10 + answers_check("MB4.10", "defg", hints={"d": "hint_10d"}),
                          [f"prediction_MB4_10{letter}" for letter in "abc"],
                          "⏳ Écris d'abord tes trois prédictions, puis exécute à nouveau.")),
        ("solution", '''start_10 = time.perf_counter()
rng = np.random.default_rng(7510)
means_10, errors_10 = [], []
for n in (10, 100, 1000):
    reciprocal_10 = np.array([1 / (int(np.flatnonzero(rng.permutation(n) == 0)[0]) + 1) for _ in range(20000)])
    means_10.append(float(reciprocal_10.mean()))
    errors_10.append(float(reciprocal_10.std(ddof=1) / math.sqrt(len(reciprocal_10))))
answer_MB4_10d = means_10
answer_MB4_10e = [sum(1 / k for k in range(1, n + 1)) / n for n in (10, 100, 1000)]
answer_MB4_10f = [math.log(n) / n for n in (10, 100, 1000)]
answer_MB4_10g = all(abs(m - h) < 3 * e for m, h, e in zip(answer_MB4_10d, answer_MB4_10e, errors_10))
print("d)", np.round(answer_MB4_10d, 6).tolist(), " erreurs types :", np.round(errors_10, 6).tolist())
print("e)", np.round(answer_MB4_10e, 6).tolist(), " f)", np.round(answer_MB4_10f, 6).tolist(), " g)", answer_MB4_10g,
      f" ({time.perf_counter() - start_10:.2f} s)")'''),
        ("record", '''sizes_10r = (10, 100, 1000)
rng_10r = np.random.default_rng(7510)                                       # the same stream as the statement
right_d_10r, first_d_10r = [], []
for n_10r in sizes_10r:
    place_10r, head_10r = np.empty(20000, dtype=int), np.empty(20000, dtype=int)
    for t_10r in range(20000):
        order_10r = rng_10r.permutation(n_10r)
        place_10r[t_10r], head_10r[t_10r] = int(np.argmax(order_10r == 0)), int(order_10r[0])
    right_d_10r.append(float(np.mean(1 / (place_10r + 1))))
    first_d_10r.append(float(np.mean(1 / (head_10r + 1))))     # the classic error: the item at the head, not the rank
wbm.record("MB4.10d", right_d_10r, decimals=6,
           mistakes={"le rang du pertinent est sa position dans order, int(np.flatnonzero(order == 0)[0]) + 1, pas l'objet "
                     "placé en tête": first_d_10r})
wbm.record("MB4.10e", [mrr_10r[n] for n in sizes_10r], decimals=6,
           mistakes={"le MRR d'un ordre au hasard est H_n divisé par n": [float(H_10r[n]) for n in sizes_10r],
                     "1/R vaut 1 au rang 1, 1/2 au rang 2… : sa moyenne est H_n/n, pas 1/n": [1 / n for n in sizes_10r]})
wbm.record("MB4.10f", [math.log(n) / n for n in sizes_10r], decimals=5,
           mistakes={"le logarithme est népérien": [math.log10(n) / n for n in sizes_10r],
                     "f) divise ln n par n": [math.log(n) for n in sizes_10r]})
wbm.record("MB4.10g", True,
           mistakes={"compare |moyenne simulée − H_n/n| à 3 erreurs types, l'écart-type des 20 000 valeurs de 1/R divisé "
                     "par √20 000 ; si l'écart est plus grand, relis ta simulation": False})'''),
        ("solution", HINT_10 + answers_check("MB4.10", "defg", hints={"d": "hint_10d"})),
        look("pourquoi le MRR n'est-il pas divisé par 10 quand $n$ est multiplié par 10 ? Quelle ligne de base un "
             "classement doit-il battre parmi 1 000 candidats ?", " (après l'expérience)"),
    ],
)

# ---------------------------------------------------------------------------
# MB4.11 · the saturation curves
# ---------------------------------------------------------------------------
CHECK_11 = '''HIDDEN_C11 = __HIDDEN_C11__   # hidden arguments, and the sub-IDs of the values expected

_NAMES_C11 = r"(?:k_?\\{?1\\}?|k₁|k1|\\\\nu|ν|nu|\\bb)"


def label_value_c11(label, drop):
    """The first number written in a label of the legend (½ is 0.5, ∞ or inf is the infinity), after the names k₁ and,
    for drop=True, the parameters k₁ = …, b = … and ν = … with their values are set aside; None when there is none."""
    text = str(label)
    if not text or text.startswith("_"):
        return None
    text = re.sub(r"\\\\frac\\{(\\d+)\\}\\{(\\d+)\\}", r" \\1/\\2 ", text)
    text = text.replace("½", " 0.5 ").replace("¼", " 0.25 ").replace("¾", " 0.75 ").replace(",", ".")
    if drop:
        text = re.sub(_NAMES_C11 + r"\\s*(?:=|:)\\s*[-+]?[\\d.]+(?:/\\d+)?", " ", text)
    text = re.sub(r"k_?\\{?1\\}?|k₁|k1", " ", text)
    match = re.search(r"(∞|\\binf(?:ty|ini|inity)?\\b)|(?<![\\w.])(\\d+(?:\\.\\d+)?)(?:/(\\d+))?", text,
                      flags=re.IGNORECASE)
    if match is None:
        return None
    if match.group(1):
        return math.inf
    return float(match.group(2)) / float(match.group(3) or 1)


def legend_names_c11(ax, grid, curves, values, drop):
    """True when each curve (drawn at grid) is a line of ax whose label names its value first."""
    for curve, value in zip(curves, values):
        found = False
        for line in ax.lines:
            x, y = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
            if x.shape == grid.shape and y.shape == grid.shape and np.allclose(x, grid) \\
                    and np.allclose(y, curve, equal_nan=True):
                named = label_value_c11(line.get_label(), drop)
                found = found or (named is not None and (named == value or math.isclose(named, value)))
        if not found:
            return False
    return True


def curves_why_c11(ax, values, xmax, curves, right, what, name):
    """What is wrong in a call of a drawing function (French phrases); right(curves) tells whether the curves returned
    are the right ones."""
    if not isinstance(curves, (list, tuple)) or len(curves) != len(values):
        return [f"{what} doit rendre la liste des {len(values)} tableaux tracés (un par valeur), reçu {shown(curves)}"]
    grid = np.linspace(0, xmax, 241)
    curves = [as_floats(c) for c in curves]
    if any(c is None or c.shape != grid.shape for c in curves):
        return [f"chaque tableau rendu par {what} doit avoir 241 valeurs, une par point de np.linspace(0, xmax, 241)"]
    problems = []
    if not right(curves):
        problems.append(f"les tableaux rendus doivent être les courbes de chaque {name} reçu, dans l'ordre reçu")
    if not all(line_with(ax, grid, c) for c in curves):
        problems.append("chaque courbe doit être tracée en fonction des 241 points de [0, xmax], np.linspace(0, xmax, 241)")
    if ax.get_legend() is None:
        problems.append("il faut une légende (label=…, puis ax.legend())")
    elif not legend_names_c11(ax, grid, curves, values, drop=(name == "ℓ")):
        problems.append(f"la légende doit nommer le {name} de chaque courbe (label=f\\"{name} = {{valeur}}\\")")
    if not ax.get_xlabel() or not ax.get_ylabel():
        problems.append("il faut des noms d'axes")
    return problems


with checked("MB4.11"):
    results_11 = []
    report_11 = reporter(results_11, stop=False)
    x_c11 = np.array(HIDDEN_C11["x"])                          # non-dyadic floats: a change in place would show
    got_c11, changed_c11 = [], False
    for k1_c11 in HIDDEN_C11["k1"]:
        received_c11 = x_c11.copy()
        got_c11.append(as_floats(call_safely("Ex MB4.11 : saturation_11 (appel caché)", saturation_11, received_c11,
                                             k1_c11)))
        changed_c11 = changed_c11 or not np.array_equal(received_c11, x_c11)
    if changed_c11:
        report_11(False, "", "saturation_11 modifie le tableau x reçu : calcule sur une copie")
    elif any(g is None or g.shape != x_c11.shape for g in got_c11):
        report_11(False, "", "saturation_11 rend un tableau de la forme de x")
    else:
        report_11(passes(HIDDEN_C11["id_s"], [g.tolist() for g in got_c11]),
                  "saturation_11 : des appels cachés (d'autres x, et k₁ = 0, 1, 3 et l'infini) sont justes",
                  "saturation_11 sur des appels cachés : ce n'est pas s(x) = x(k₁ + 1)/(x + k₁) ; relis les deux cas à "
                  "part, k₁ = 0 (la seule présence) et k₁ infini (le compte brut)")

    def saturations_right_c11(k1s, xmax):
        grid = np.linspace(0, xmax, 241)
        return lambda curves: all(matches(c, saturation_11(grid.copy(), k1), rtol=1e-9, atol=1e-12)
                                  for c, k1 in zip(curves, k1s))

    def lengths_right_c11(sub_id):
        return lambda curves: passes(sub_id, [c[HIDDEN_C11["idx"]].tolist() for c in curves])

    fig_11, axes_11 = plt.subplots(1, 2, figsize=(12, 4.5))
    try:
        drawn_11 = []
        opened_11 = drawn(lambda: drawn_11.append(call_safely("Ex MB4.11 : draw_saturations_11", draw_saturations_11,
                                                              axes_11[0], (0, 1, 2, 3, np.inf), 12)))
        problems_11 = curves_why_c11(axes_11[0], (0, 1, 2, 3, math.inf), 12, drawn_11[0],
                                     saturations_right_c11((0, 1, 2, 3, np.inf), 12), "draw_saturations_11", "k₁")
        report_11(not problems_11, "draw_saturations_11 (k₁ = 0, 1, 2, 3 et l'infini, sur [0, 12]) : les courbes, la "
                  "légende et les noms d'axes", "draw_saturations_11 : " + " ; ".join(problems_11))
        lengths_11 = []
        opened_11 += drawn(lambda: lengths_11.append(call_safely("Ex MB4.11 : draw_lengths_11", draw_lengths_11,
                                                                 axes_11[1], 1, 0.5, (0.5, 1, 2), 12)))
        problems_11 = curves_why_c11(axes_11[1], (0.5, 1, 2), 12, lengths_11[0], lengths_right_c11(HIDDEN_C11["id_l"]),
                                     "draw_lengths_11", "ℓ")
        report_11(not problems_11, "draw_lengths_11 (k₁ = 1, b = ½, ℓ = ½, 1 et 2, sur [0, 12]) : les courbes, la "
                  "légende et les noms d'axes", "draw_lengths_11 : " + " ; ".join(problems_11))
        fig_c11, axes_c11 = plt.subplots(1, 3)          # the 3rd axes is the current one: plt.plot would draw there
        try:
            hidden_s_c11, hidden_l_c11 = [], []
            opened_11 += drawn(lambda: hidden_s_c11.append(call_safely(
                "Ex MB4.11 : draw_saturations_11 (appel caché)", draw_saturations_11, axes_c11[0],
                tuple(HIDDEN_C11["draw_k1"]), HIDDEN_C11["draw_xmax"])))
            problems_c11 = curves_why_c11(axes_c11[0], HIDDEN_C11["draw_k1"], HIDDEN_C11["draw_xmax"], hidden_s_c11[0],
                                          saturations_right_c11(HIDDEN_C11["draw_k1"], HIDDEN_C11["draw_xmax"]),
                                          "draw_saturations_11", "k₁")
            opened_11 += drawn(lambda: hidden_l_c11.append(call_safely(
                "Ex MB4.11 : draw_lengths_11 (appel caché)", draw_lengths_11, axes_c11[1], HIDDEN_C11["k1_l"],
                HIDDEN_C11["b_l"], tuple(HIDDEN_C11["ells"]), HIDDEN_C11["xmax_l"])))
            problems_c11 += curves_why_c11(axes_c11[1], HIDDEN_C11["ells"], HIDDEN_C11["xmax_l"], hidden_l_c11[0],
                                           lengths_right_c11(HIDDEN_C11["id_h"]), "draw_lengths_11", "ℓ")
            elsewhere_11 = bool(axes_c11[2].lines or axes_c11[2].collections or axes_c11[2].get_legend())
        finally:
            plt.close(fig_c11)
        report_11(not problems_c11, "des appels cachés (les k₁ dans un autre ordre, d'autres longueurs, un autre b) sont justes aussi",
                  "des appels cachés (les k₁ dans un autre ordre, d'autres longueurs, un autre b) : "
                  + " ; ".join(dict.fromkeys(problems_c11)))
        report_11(not opened_11 and not elsewhere_11, "tes fonctions dessinent dans les axes reçus",
                  "tes fonctions doivent dessiner dans les axes reçus (ax.plot, ax.legend…), sans ouvrir de figure ni "
                  "dessiner dans l'axe courant (plt.plot, plt.legend…)")
    except BaseException:
        plt.close(fig_11)
        raise
    fig_11.tight_layout()
    plt.show()
    verdict("MB4.11", all(results_11) and len(results_11) == 5, "ta saturation et tes deux figures sont justes, sur les "
            "appels du notebook et sur des appels cachés.", "relis les lignes ❌ ci-dessus.")'''

NOTE_11 = (r"`saturation_11` : `(x > 0).astype(float)` pour $k_1 = 0$, `x.copy()` pour $k_1$ infini, sinon "
           r"`x * (k1 + 1) / (x + k1)`. a) $(1{,}714286 ;\ 2{,}25 ;\ 2{,}666667)$. b) $(9, 18, 27)$ : $s(x) = "
           r"0{,}9(k_1 + 1)$ pour $x = 9k_1$. c) $(1{,}684211 ;\ 1{,}6 ;\ 1{,}454545)$. d) Vrai : le plafond reste $k_1 + 1 = 2$.")

MB4_11 = Ex(
    "MB4.11", "🎨", 1, 30, "Les courbes de saturation x ↦ x(k₁ + 1)/(x + k₁) de k₁ = 0 à l'infini, et ce que la "
    "normalisation par la longueur leur fait",
    "tracer la saturation pour plusieurs $k_1$, entre la seule présence et le compte brut, et voir ce que la "
    "normalisation par la longueur lui fait.", "fiche §4 ; R7, M05a (concavité) ; Ex MB4.3", tracks="C", note=NOTE_11,
    body=r"""Écris `saturation_11(x, k1)`, qui rend $s(x) = \frac{x(k_1 + 1)}{x + k_1}$ pour un tableau `x` de nombres $\ge 0$ (avec $k_1 = 0$, la seule présence : 1 pour $x > 0$, 0 pour $x = 0$ ; avec `k1=np.inf`, le compte brut $x$) ; puis `draw_saturations_11(ax, k1s, xmax)`, qui trace dans les axes reçus, sur 241 points de $[0, x_{\max}]$ (`np.linspace(0, xmax, 241)`), une courbe pour chaque $k_1$ de `k1s`, avec une légende qui nomme chaque $k_1$ et des noms d'axes, et rend la liste des tableaux tracés ; puis `draw_lengths_11(ax, k1, b, ells, xmax)`, qui trace de même, pour chaque $\ell$ de `ells`, la courbe de la saturation normalisée $x \mapsto \frac{x(k_1 + 1)}{x + k_1\nu}$, avec $\nu = 1 - b + b\ell$, avec une légende qui nomme chaque $\ell$. Les fonctions dessinent dans les axes reçus, sans ouvrir de figure (tu peux borner l'axe des ordonnées, `ax.set_ylim(0, 5)` : la droite du compte brut écrase les autres courbes).

La vérification les appelle avec $k_1 = 0$, 1, 2, 3 et l'infini, puis avec $k_1 = 1$, $b = \frac12$ et $\ell = \frac12$, 1, 2, sur $[0, 12]$, affiche la figure, et les essaie sur des appels cachés (d'autres $x$, les $k_1$ dans un autre ordre, d'autres longueurs, un autre $b$) ; `saturation_11` ne modifie pas le tableau reçu. Relève :
- a) $s(6)$ pour $k_1 = 1$, 2 et 3 (une liste de 3 nombres) ;
- b) pour $k_1 = 1$, 2 et 3, la valeur de $x$ où $s$ atteint 90 % de sa limite (une liste de 3 nombres) ;
- c) pour $k_1 = 1$ et $b = \frac12$, la valeur en $x = 4$ pour $\ell = \frac12$, 1 et 2 (une liste de 3 nombres) ;
- d) vrai ou faux : les trois courbes de c) ($\ell = \frac12$, 1 et 2) tendent vers la même limite quand $x \to \infty$.""",
    todo='''def saturation_11(x, k1):
    """s(x) = x (k1 + 1) / (x + k1) for an array x of numbers >= 0: with k1 = 0, the presence alone (1 for x > 0, 0 for
    x = 0); with k1 = np.inf, the raw count x. Returns an array of the shape of x."""
    raise NotImplementedError("saturation_11 n'est pas encore écrite (04_indices.md si tu bloques)")


def draw_saturations_11(ax, k1s, xmax):
    """In the axes ax: for each k1 of k1s, the curve of saturation_11 on the 241 points np.linspace(0, xmax, 241), with
    a legend that names each k1 and axis labels. Returns the list of the arrays drawn (one per k1). Opens no figure."""
    raise NotImplementedError("draw_saturations_11 n'est pas encore écrite (04_indices.md si tu bloques)")


def draw_lengths_11(ax, k1, b, ells, xmax):
    """In the axes ax: for each length ell of ells (relative to the mean length), the curve of
    x -> x (k1 + 1) / (x + k1 nu), nu = 1 - b + b ell, on np.linspace(0, xmax, 241), with a legend that names each ell
    and axis labels. Returns the list of the arrays drawn (one per ell). Opens no figure."""
    raise NotImplementedError("draw_lengths_11 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB4_11a = answer_MB4_11b = answer_MB4_11c = answer_MB4_11d = ...
with wbm.attempt("MB4.11"):          # your functions: ⏳ while they are not written
    answer_MB4_11a = ...  # a) a list of 3 numbers, as computed: s(6) for k1 = 1, 2, 3
    answer_MB4_11b = ...  # b) a list of 3 numbers: for k1 = 1, 2, 3, the x where s reaches 90 % of its limit
    answer_MB4_11c = ...  # c) a list of 3 numbers, as computed: k1 = 1, b = 0.5, the value at x = 4 for ell = 0.5, 1, 2
    answer_MB4_11d = ...  # d) True or False: the three curves of c) (ell = 0.5, 1, 2) tend to the same limit as x -> infinity''',
    check=answers_check("MB4.11", "abcd") + "\n\n" + CHECK_11,
    solution='''from scipy.optimize import brentq


def saturation_11(x, k1):
    """s(x) = x (k1 + 1) / (x + k1) for an array x of numbers >= 0: with k1 = 0, the presence alone (1 for x > 0, 0 for
    x = 0); with k1 = np.inf, the raw count x. Returns an array of the shape of x."""
    x = np.asarray(x, dtype=float)
    if k1 == 0:
        return (x > 0).astype(float)
    if math.isinf(k1):
        return x.copy()
    return x * (k1 + 1) / (x + k1)


def k1_name_11(k1):
    if math.isinf(k1):
        return "∞ (le compte brut)"
    return "0 (la seule présence)" if k1 == 0 else f"{k1:g}".replace(".", ",")


def draw_saturations_11(ax, k1s, xmax):
    """In the axes ax: for each k1 of k1s, the curve of saturation_11 on the 241 points np.linspace(0, xmax, 241), with
    a legend that names each k1 and axis labels. Returns the list of the arrays drawn (one per k1). Opens no figure."""
    x = np.linspace(0, xmax, 241)
    curves = []
    for k1 in k1s:
        y = saturation_11(x, k1)
        ax.plot(x, y, lw=1.6, label=f"$k_1$ = {k1_name_11(k1)}")
        curves.append(y)
    ax.set_xlabel("nombre de mentions x")
    ax.set_ylabel("saturation s(x)")
    ax.set_ylim(-0.1, 4.6)                         # the raw count goes on, out of the frame
    ax.legend(fontsize=8)
    return curves


def draw_lengths_11(ax, k1, b, ells, xmax):
    """In the axes ax: for each length ell of ells (relative to the mean length), the curve of
    x -> x (k1 + 1) / (x + k1 nu), nu = 1 - b + b ell, on np.linspace(0, xmax, 241), with a legend that names each ell
    and axis labels. Returns the list of the arrays drawn (one per ell). Opens no figure."""
    x = np.linspace(0, xmax, 241)
    curves = []
    for ell in ells:
        nu = 1 - b + b * ell
        y = x * (k1 + 1) / (x + k1 * nu)
        ax.plot(x, y, lw=1.6, label=f"ℓ = {ell:g}".replace(".", ","))
        curves.append(y)
    ax.set_xlabel("nombre de mentions x")
    ax.set_ylabel(f"saturation normalisée ($k_1$ = {k1:g}, b = {b:g})".replace(".", ","))
    ax.legend(fontsize=8)
    return curves


answer_MB4_11a = [float(saturation_11(np.array([6.0]), k1)[0]) for k1 in (1, 2, 3)]
answer_MB4_11b = [brentq(lambda x, k1=k1: saturation_11(np.array([x]), k1)[0] - 0.9 * (k1 + 1), 0.0, 1000.0, xtol=1e-12)
                  for k1 in (1, 2, 3)]
answer_MB4_11c = [4 * 2 / (4 + 1 * (1 - 0.5 + 0.5 * ell)) for ell in (0.5, 1, 2)]
far_11 = 1e9                                       # the curves of c) far to the right: their limits as x -> infinity
answer_MB4_11d = all(abs(far_11 * 2 / (far_11 + 1 * (1 - 0.5 + 0.5 * ell)) - 2) < 1e-6 for ell in (0.5, 1, 2))
print("a)", np.round(answer_MB4_11a, 6).tolist(), " b)", np.round(answer_MB4_11b, 6).tolist(),
      " c)", np.round(answer_MB4_11c, 6).tolist(), " d)", answer_MB4_11d)''',
    record='''from fractions import Fraction as F_11r

import sympy as sp_11r


def s_11r(x, k1, nu=1):
    """The oracle: x (k1 + 1) / (x + k1 nu) in exact fractions (k1 = 0: the presence; k1 = None: the raw count)."""
    x = F_11r(x)
    if k1 is None:
        return x
    if k1 == 0:
        return F_11r(int(x > 0))
    return x * (k1 + 1) / (x + k1 * F_11r(nu))


wbm.record("MB4.11a", [float(s_11r(6, k1)) for k1 in (1, 2, 3)], decimals=6,
           mistakes={"s(x) = x(k₁ + 1)/(x + k₁) : le compte x est aussi au numérateur":
                         [float(F_11r(k1 + 1, 6 + k1)) for k1 in (1, 2, 3)]})
wbm.record("MB4.11b", [9 * k1 for k1 in (1, 2, 3)], decimals=6,
           mistakes={"la limite de s est k₁ + 1, pas k₁ : 90 % de k₁ + 1":
                         [float(F_11r(9, 10) * k1 ** 2 / (1 + F_11r(1, 10) * k1)) for k1 in (1, 2, 3)],
                     "en x = k₁, s atteint la moitié de sa limite ; b) demande 90 % de la limite k₁ + 1": [1, 2, 3]})
wbm.record("MB4.11c", [float(s_11r(4, 1, 1 - F_11r(1, 2) + F_11r(1, 2) * F_11r(ell))) for ell in ("1/2", 1, 2)],
           decimals=6,
           mistakes={"la normalisation multiplie k₁ seul, au dénominateur : x(k₁ + 1)/(x + k₁ ν)":
                         [float(s_11r(4, 1) / (1 - F_11r(1, 2) + F_11r(1, 2) * F_11r(ell))) for ell in ("1/2", 1, 2)]})
x_11r = sp_11r.symbols("x", positive=True)
limits_11r = {sp_11r.limit(x_11r * 2 / (x_11r + sp_11r.Rational(1 - F_11r(1, 2) + F_11r(1, 2) * F_11r(ell))), x_11r, sp_11r.oo)
              for ell in ("1/2", 1, 2)}                                    # the oracle: the limits of the curves of c), SymPy
wbm.record("MB4.11d", len(limits_11r) == 1,
           mistakes={"la normalisation multiplie k₁ par ν au dénominateur : le plafond reste k₁ + 1, seule la "
                     "demi-saturation bouge": False})
HIDDEN_11r = __HIDDEN_C11__                                                  # the hidden calls of the check
wbm.record(HIDDEN_11r["id_s"], [[float(s_11r(x, None if math.isinf(k1) else k1)) for x in HIDDEN_11r["x"]]
                                for k1 in HIDDEN_11r["k1"]], decimals=6)


def lengths_11r(k1, b, ells, xmax):
    """The oracle: the normalised curves at the points of index HIDDEN_11r["idx"] of np.linspace(0, xmax, 241)."""
    grid = [F_11r(xmax) * i / 240 for i in HIDDEN_11r["idx"]]
    return [[float(s_11r(x, k1, 1 - F_11r(b) + F_11r(b) * F_11r(ell))) for x in grid] for ell in ells]


wbm.record(HIDDEN_11r["id_l"], lengths_11r(1, "1/2", ("1/2", 1, 2), 12), decimals=6)
wbm.record(HIDDEN_11r["id_h"], lengths_11r(HIDDEN_11r["k1_l"], str(F_11r(HIDDEN_11r["b_l"])),
                                          [str(F_11r(ell).limit_denominator(1000)) for ell in HIDDEN_11r["ells"]],
                                          HIDDEN_11r["xmax_l"]), decimals=6)''',
    after=[
        ("solution", answers_check("MB4.11", "abcd") + "\n\n" + CHECK_11),
        look("entre quelles deux courbes extrêmes se placent les autres ? Que fait une fiche longue à sa courbe, et une "
             "fiche courte ?"),
    ],
)

PART_B = Part("B", "Prédire, dessiner",
              "Fiche §4 et §6. Le MRR d'un ordre tiré au hasard, prédit puis simulé ; les courbes de saturation et l'effet "
              "de la longueur d'une fiche.", exercises=[MB4_10, MB4_11])

# ---------------------------------------------------------------------------
# Notebook exercise: debug (MB4.12)
# ---------------------------------------------------------------------------
GIVEN_12 = '''import sympy as sp

# 4 judges rank 6 candidates (numbered 0 to 5): one row per judge, best first
RANK_12 = np.array(__RANK_12__)
RANK_12.setflags(write=False)


# The colleague's code
def exact_rref_12(M):
    """The reduced row echelon form of M, computed exactly (SymPy, the entries read as decimal fractions), as an array
    of floats, and the list of its pivot columns."""
    R, pivots = sp.Matrix([[sp.Rational(str(x)) for x in row] for row in np.asarray(M, dtype=float)]).rref()
    return np.array(R, dtype=float), list(pivots)


def rank_factorization_bad(M):
    """The rank factorization (C, F) of M: C the pivot columns of M, F the non-zero rows of its reduced form."""
    R, pivots = exact_rref_12(M)
    return R[:, pivots], R[:len(pivots)]


def borda_bad(rankings):
    """The Borda points of complete rankings (each row lists the candidates, best first)."""
    R = np.asarray(rankings)
    m, n = R.shape
    points = np.zeros(n, dtype=int)
    for row in R:
        for c in range(n):
            points[c] += n - 1 - row[c]
    return points


def rarity_bad(n, N):
    """The surprise of an ingredient found in n recipe cards out of N."""
    return math.log(n / N)


# The colleague's checks: all pass
E_12 = np.array([[1.0, 0, 5, 0, -2], [0, 1, 3, 0, 4], [0, 0, 0, 1, 7]])   # a matrix already in reduced row echelon form
C_12, F_12 = rank_factorization_bad(E_12)
print("(1)", bool(np.allclose(C_12 @ F_12, E_12)), "(attendu True : C F redonne la matrice)")
print("(2)", borda_bad([[1, 0, 3, 2], [2, 3, 0, 1], [0, 1, 3, 2]]).tolist() == [6, 5, 3, 4],
      "(attendu True : trois jurys, quatre candidats, les points comptés à la main)")
print("(3)", rarity_bad(90, 90) == 0, "(attendu True : un ingrédient présent dans toutes les fiches ne surprend pas)")'''

CHECK_12 = '''CASES_C12 = __CASES_C12__   # the hidden tables, rankings and notebooks of recipes, and the sub-ID expected

results_12, parts_12 = [], []
MYMATH_C12 = list(getattr(mymath, "__path__", [])) + list(getattr(REF, "__path__", []))   # the folders of mymath


def report_12(ok, success, failure):
    results_12.append(bool(ok))
    print(("✅ " + success) if ok else ("❌ " + failure))


def call_12(part, name, function, *args):
    """function(*args), without mymath; an error of the learner's code becomes one ❌ line that names the function."""
    try:
        with code_from(MYMATH_C12) as seen:
            got = function(*args)
    except (NotImplementedError, MymathMissingError):
        raise
    except Exception as exc:  # noqa: BLE001 - the learner's error, reported with the name of the function
        report_12(False, "", f"({part}) {name} : ton code lève {type(exc).__name__} : {str(exc)[:160]}")
        parts_12.append(part)
        raise StopCheck from None
    if seen:
        report_12(False, "", f"({part}) {name} appelle mymath ({seen[0]}) : l'énoncé demande la correction sans mymath, "
                  "en corrigeant le code du collègue (exact_rref_12 reste permise)")
        parts_12.append(part)
        raise StopCheck
    return got


def factors_12(got):
    """(C, F) as two 2-D float arrays, or None when got is not such a pair."""
    try:
        C, F = got
        C, F = np.asarray(C, dtype=float), np.asarray(F, dtype=float)
    except (TypeError, ValueError):
        return None
    return (C, F) if C.ndim == 2 and F.ndim == 2 else None


with checked("MB4.12"):                                      # (1) rank_factorization_fixed
    wrong_c12 = []
    for table_c12 in CASES_C12["tables"]:
        M_c12 = np.array(table_c12)                          # non-dyadic floats: a change in place would show
        before_c12 = M_c12.copy()
        got_c12 = factors_12(call_12(1, "rank_factorization_fixed", rank_factorization_fixed, M_c12))
        want_c12 = ref_ranks.rank_factorization(before_c12)
        if not np.array_equal(M_c12, before_c12):
            wrong_c12.append("ta fonction modifie le tableau reçu : travaille sur une copie")
        elif got_c12 is None:
            wrong_c12.append("rank_factorization_fixed rend le couple (C, F) de deux tableaux 2-D")
        elif all(matches(g, w, rtol=1e-9, atol=1e-9) for g, w in zip(got_c12, want_c12)):
            continue
        elif matches(got_c12[0], rank_factorization_bad(before_c12)[0], atol=1e-9):
            wrong_c12.append("ta correction prend encore C dans la forme réduite : C est faite des colonnes pivots de M "
                             "elle-même")
        elif matches(got_c12[0], want_c12[0]) and got_c12[1].shape[0] > want_c12[1].shape[0]:
            wrong_c12.append("F ne garde que les r lignes non nulles de la forme réduite, une par colonne pivot")
        elif got_c12[0].shape == want_c12[0].shape and matches(got_c12[0], before_c12[:, :got_c12[0].shape[1]]):
            wrong_c12.append("sur des tableaux dont les colonnes pivots ne sont pas les premières, C n'est pas faite des "
                             "colonnes pivots de M")
        else:
            wrong_c12.append("sur d'autres tableaux (de rang 1, des colonnes pivots qui ne sont pas les premières), ce "
                             "n'est pas la factorisation par les colonnes pivots : C les colonnes pivots de M, F les "
                             "lignes non nulles de sa forme réduite")
    report_12(not wrong_c12, "(1) rank_factorization_fixed : des tableaux cachés, de rang 1 ou de colonnes pivots qui ne "
              "sont pas les premières", "(1) rank_factorization_fixed : " + " ; ".join(dict.fromkeys(wrong_c12)))
    parts_12.append(1)

with checked("MB4.12"):                                      # (2) borda_fixed, compared with the reference
    wrong_c12 = []
    for rankings_c12 in CASES_C12["rankings"]:
        R_c12 = np.array(rankings_c12)
        before_c12 = R_c12.copy()
        got_c12 = as_floats(call_12(2, "borda_fixed", borda_fixed, R_c12))
        want_c12 = ref_ranks.borda_scores(before_c12)
        if not np.array_equal(R_c12, before_c12):
            wrong_c12.append("ta fonction modifie le tableau reçu : travaille sur une copie")
        elif got_c12 is None or got_c12.shape != want_c12.shape:
            wrong_c12.append(f"borda_fixed rend un tableau de {before_c12.shape[1]} points, un par candidat")
        elif np.array_equal(got_c12, want_c12):
            continue
        elif np.array_equal(got_c12, borda_bad(before_c12)):
            wrong_c12.append("ta correction lit encore chaque ligne comme la liste des rangs des candidats : une ligne "
                             "est un ordre, le candidat placé à chaque position")
        else:
            wrong_c12.append("sur des classements dont aucune ligne n'est sa propre inverse, ce ne sont pas les points de "
                             "Borda : le candidat placé à la position p d'une ligne (à partir de 0) reçoit n − 1 − p "
                             "points")
    report_12(not wrong_c12, "(2) borda_fixed : des classements cachés, dont aucune ligne n'est sa propre inverse",
              "(2) borda_fixed : " + " ; ".join(dict.fromkeys(wrong_c12)))
    parts_12.append(2)

with checked("MB4.12"):                                      # (3) rarity_fixed
    got_c12 = [call_12(3, "rarity_fixed", rarity_fixed, n_c12, N_c12) for n_c12, N_c12 in CASES_C12["notebooks"]]
    numbers_c12 = as_floats(got_c12)
    if numbers_c12 is None or numbers_c12.shape != (len(got_c12),):
        why_c12 = f"rarity_fixed rend un nombre, reçu {shown(got_c12)}"
    elif passes(CASES_C12["id"], numbers_c12.tolist()):
        why_c12 = ""
    elif all(math.isclose(g, rarity_bad(n, N), abs_tol=1e-9) for g, (n, N) in zip(numbers_c12, CASES_C12["notebooks"])):
        why_c12 = "ta correction rend encore ln(n/N), négatif pour un ingrédient rare"
    else:
        why_c12 = ("sur d'autres carnets, ce n'est pas la surprise d'un ingrédient présent dans n fiches sur N, un nombre "
                   "positif, en nats")
    report_12(not why_c12, "(3) rarity_fixed : d'autres carnets", f"(3) rarity_fixed : {why_c12}")
    parts_12.append(3)

if len(set(parts_12)) == 3:
    verdict("MB4.12", all(results_12), "les trois fonctions corrigées passent tous les cas.", "relis les lignes ❌ ci-dessus.")'''

NOTE_12 = (r"(1) La forme réduite a l'identité dans ses colonnes pivots : prise pour $\mathbf{C}$, elle donne $\mathbf{C}"
           r"\mathbf{F}$ = la forme réduite, pas $\mathbf{M}$ ; correction : `C = np.asarray(M, dtype=float)[:, pivots]`. "
           r"a) $(0, 19)$. (2) Une ligne est un ordre ; correction : `points[row[p]] += n - 1 - p`. b) $(15, 9, 10, 2, "
           r"18, 6)$, puis $(10, 12, 8, 15, 11, 4)$. (3) Le signe : correction `-math.log(n / N)`. c) $(3{,}401197 ;\ "
           r"1{,}098612 ;\ -3{,}401197 ;\ -1{,}098612)$.")

MB4_12 = Ex(
    "MB4.12", "🐛", 1, 20, "Chasse à l'erreur : C pris dans la forme réduite au lieu de M, un classement lu comme la liste "
    "des rangs des candidats, un poids de rareté écrit ln(n/N)",
    "reconnaître trois erreurs classiques (C pris dans la forme réduite, un classement lu comme la liste des rangs, un "
    "poids de rareté de signe faux), qui passent une vérification mal choisie, puis les corriger.",
    "fiche §1, §3 et §5 ; Ex MB4.1, MB4.3 et MB4.4", tracks="C", given=GIVEN_12, note=NOTE_12,
    body=r"""Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe (cellule fournie) :
1. `rank_factorization_bad(M)` doit rendre la factorisation par les colonnes pivots ; elle prend $\mathbf{C}$ dans les colonnes pivots de la **forme réduite** au lieu de celles de $\mathbf{M}$. Il l'a vérifiée sur une matrice déjà sous forme échelonnée réduite.
2. `borda_bad(rankings)` doit rendre les points de Borda ; elle lit chaque ligne comme la liste des **rangs** des candidats (la valeur d'indice $c$ comme la position du candidat $c$), au lieu de la liste des candidats dans l'ordre. Il l'a vérifiée sur trois jurys et quatre candidats, `[[1, 0, 3, 2], [2, 3, 0, 1], [0, 1, 3, 2]]`.
3. `rarity_bad(n, N)` doit rendre la surprise d'un ingrédient présent dans $n$ fiches sur $N$ ; elle rend $\ln\frac nN$. Il l'a vérifiée sur un ingrédient présent dans toutes les fiches, de surprise nulle.

À faire : trouve et corrige chaque erreur ; les fonctions corrigées s'appellent `rank_factorization_fixed`, `borda_fixed` et `rarity_fixed`, avec les mêmes arguments (sans `mymath` ; `exact_rref_12`, la réduction exacte de la cellule fournie, reste permise). Puis réponds :
- a) pour le tableau `M_1` des boulangeries, le plus grand écart $\lvert(\mathbf{C}\mathbf{F})_{ij} - M_{ij}\rvert$ par la fonction corrigée, puis par la fonction fautive (une liste de 2 nombres) ;
- b) pour les classements `RANK_12` de 4 juges et 6 candidats, que fournit le notebook : les points de Borda par la fonction corrigée, puis par la fonction fautive (une liste de 2 listes de 6 entiers) ;
- c) les surprises d'ingrédients présents dans 3 et dans 30 fiches sur 90, par la fonction corrigée, puis par la fonction fautive (une liste de 4 nombres).

Dans ta copie : pour chacune des trois erreurs, pourquoi la vérification du collègue ne la voyait pas. La vérification essaie aussi tes fonctions corrigées sur des cas cachés : d'autres tableaux, dont des tableaux de rang 1 et des tableaux dont les colonnes pivots ne sont pas les premières, des classements dont aucune ligne n'est sa propre inverse, et d'autres carnets.""",
    todo='''def rank_factorization_fixed(M):
    """The rank factorization (C, F) of M: C the pivot columns of M, F the non-zero rows of its reduced form."""
    raise NotImplementedError("rank_factorization_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def borda_fixed(rankings):
    """The Borda points of complete rankings (each row lists the candidates, best first)."""
    raise NotImplementedError("borda_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def rarity_fixed(n, N):
    """The surprise of an ingredient found in n recipe cards out of N."""
    raise NotImplementedError("rarity_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB4_12a = answer_MB4_12b = answer_MB4_12c = ...
with wbm.attempt("MB4.12"):          # your three functions: ⏳ while they are not written
    answer_MB4_12a = ...  # a) a list of 2 numbers, as computed: max |CF - M_1| by rank_factorization_fixed, then by the WRONG rank_factorization_bad
    answer_MB4_12b = ...  # b) a list of 2 lists of 6 integers: borda_fixed(RANK_12), then the WRONG borda_bad(RANK_12)
    answer_MB4_12c = ...  # c) a list of 4 numbers, as computed: rarity_fixed for 3 and 30 cards out of 90, then the WRONG rarity_bad''',
    check=answers_check("MB4.12", "abc") + "\n\n" + CHECK_12,
    solution='''def rank_factorization_fixed(M):
    """The rank factorization (C, F) of M: C the pivot columns of M, F the non-zero rows of its reduced form."""
    R, pivots = exact_rref_12(M)
    return np.asarray(M, dtype=float)[:, pivots], R[:len(pivots)]     # the columns of M itself, not of R


def borda_fixed(rankings):
    """The Borda points of complete rankings (each row lists the candidates, best first)."""
    R = np.asarray(rankings)
    m, n = R.shape
    points = np.zeros(n, dtype=int)
    for row in R:
        for p, c in enumerate(row):                                    # the candidate c is at the position p
            points[c] += n - 1 - p
    return points


def rarity_fixed(n, N):
    """The surprise of an ingredient found in n recipe cards out of N."""
    return -math.log(n / N)                                            # ln(N / n) > 0 for n < N


answer_MB4_12a = [float(np.max(np.abs(np.matmul(*rank_factorization_fixed(M_1)) - M_1))),
                  float(np.max(np.abs(np.matmul(*rank_factorization_bad(M_1)) - M_1)))]
answer_MB4_12b = [borda_fixed(RANK_12).tolist(), borda_bad(RANK_12).tolist()]
answer_MB4_12c = [rarity_fixed(3, 90), rarity_fixed(30, 90), rarity_bad(3, 90), rarity_bad(30, 90)]
print("a)", answer_MB4_12a, " b)", answer_MB4_12b, " c)", np.round(answer_MB4_12c, 6).tolist())''',
    record='''import sympy as sp_12r

sales_12r = sp_12r.Matrix([[20, 6, 16, 12, 8], [8, 10, 14, 20, 7], [12, 4, 10, 8, 5], [16, 2, 10, 4, 5]])
form_12r, pivots_12r = sales_12r.rref()
right_a_12r = float(max(abs(x) for x in sales_12r[:, list(pivots_12r)] * form_12r[:len(pivots_12r), :] - sales_12r))
bad_a_12r = float(max(abs(x) for x in form_12r[:, list(pivots_12r)] * form_12r[:len(pivots_12r), :] - sales_12r))
wbm.record("MB4.12a", [right_a_12r, bad_a_12r], decimals=6,
           mistakes={"rank_factorization_fixed prend encore C dans la forme réduite : C est faite des colonnes pivots de M "
                     "elle-même": [bad_a_12r, bad_a_12r],
                     "le second nombre est celui de la version FAUSSE, rank_factorization_bad": [right_a_12r, right_a_12r],
                     "la version corrigée d'abord, puis la version fautive": [bad_a_12r, right_a_12r]})
judges_12r = np.array(__RANK_12__)
inverse_12r = np.argsort(judges_12r, axis=1)                          # the oracle: the position of each candidate
right_b_12r = (judges_12r.shape[1] - 1 - inverse_12r).sum(axis=0).tolist()
bad_b_12r = (judges_12r.shape[1] - 1 - judges_12r).sum(axis=0).tolist()
wbm.record("MB4.12b", [right_b_12r, bad_b_12r],
           mistakes={"borda_fixed lit encore chaque ligne comme la liste des rangs : une ligne est un ordre, le candidat "
                     "placé à chaque position": [bad_b_12r, bad_b_12r],
                     "la seconde liste est celle de la version FAUSSE, borda_bad": [right_b_12r, right_b_12r],
                     "la version corrigée d'abord, puis la version fautive": [bad_b_12r, right_b_12r]})
right_c_12r, bad_c_12r = [math.log(90 / n) for n in (3, 30)], [-math.log(90 / n) for n in (3, 30)]
wbm.record("MB4.12c", right_c_12r + bad_c_12r, decimals=6,
           mistakes={"rarity_fixed rend encore ln(n/N), négatif pour un ingrédient rare": bad_c_12r + bad_c_12r,
                     "les deux derniers nombres sont ceux de la version FAUSSE, rarity_bad": right_c_12r + right_c_12r,
                     "tes valeurs sont celles de la fonction fautive puis de la corrigée : la corrigée d'abord ; et "
                     "rarity(n, N) prend d'abord n, le nombre de fiches qui contiennent l'ingrédient":
                         bad_c_12r + right_c_12r,
                     "la surprise se mesure avec le logarithme népérien, en nats":
                         [math.log10(90 / n) for n in (3, 30)] + bad_c_12r})
CASES_12r = __CASES_C12__                                                   # the hidden notebooks of recipes of the check
wbm.record(CASES_12r["id"], [math.log(N / n) for n, N in CASES_12r["notebooks"]], decimals=6)''',
    after=[
        ("solution", answers_check("MB4.12", "abc") + "\n\n" + CHECK_12),
        ("md", "**Après la vérification**, dans ta copie : pour chacune des trois erreurs, pourquoi la vérification du "
               "collègue ne la voyait-elle pas, et quelle vérification l'aurait vue ?"),
    ],
)

PART_C = Part("C", "Déboguer", "Fiche §1, §3 et §5. Trois erreurs classiques à corriger, qui passent une vérification mal "
              "choisie.", exercises=[MB4_12])

# ---------------------------------------------------------------------------
# Notebook exercise: the challenge (MB4.13)
# ---------------------------------------------------------------------------
GIVEN_13 = '''def _tables_13():
    """The five tables of the notebook, read in solutions/challenges/mb4_13.py (the hidden part of the challenge: the law
    of the tables and their hidden ranks stay there; reading it spoils the challenge)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("mb4_13_tables",
                                                  wbm.repo_root() / "solutions" / "challenges" / "mb4_13.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return [np.array(table, dtype=float) for table in module.notebook_tables()]


TABLES_13 = _tables_13()   # five noisy tables of measurements: shapes (90, 60), (70, 110), (120, 120), (80, 50), (100, 75)
del _tables_13
for _array in TABLES_13:
    _array.setflags(write=False)
print("formes :", [table.shape for table in TABLES_13])'''

CHECK_13 = """def check_c13():
    \"\"\"The check of MB4.13, in a function. The hidden tables come from another process (the hidden module run as a
    script), which gives their ranks only once hidden_rank_13 has seen all of them: neither a hidden rank nor what makes
    it (a seed, a kind) lives in this process while the learner's function runs. Each call runs under code_from: the
    learner's function may not run code of the hidden module.\"\"\"
    import io
    import json
    import struct
    import subprocess
    import sys
    hidden_file = wbm.repo_root() / "solutions" / "challenges" / "mb4_13.py"   # reading it spoils the challenge
    twins = code_keys_of_file(hidden_file)                      # its functions, to recognise a copy run from elsewhere
    results, elapsed = [], [0.0]
    report = reporter(results, stop=False)

    def rank_of(label, M):
        start = time.perf_counter()
        with code_from([hidden_file], twins=twins) as seen:
            got = call_safely(label, hidden_rank_13, M.copy())
        elapsed[0] += time.perf_counter() - start
        if seen:
            print(f"❌ {label} : hidden_rank_13 exécute du code de solutions/challenges/mb4_13.py ({seen[0]}), la partie "
                  "cachée du défi, ou une copie de ce code : la vérification mesurerait sa méthode, pas la tienne")
            raise StopCheck
        if isinstance(got, (bool, np.bool_)) or not isinstance(got, (int, np.integer)) or got < 0:
            print(f"❌ {label} : hidden_rank_13 rend un entier ≥ 0 (un int), reçu {shown(got)}")
            raise StopCheck
        return int(got)

    found = [rank_of(f"Ex MB4.13 : hidden_rank_13 (tableau {k} du notebook)", table)
             for k, table in enumerate(TABLES_13, start=1)]
    report(passes("MB4.13a", found), "les cinq tableaux du notebook : les cinq rangs cachés",
           "les cinq tableaux du notebook : ta fonction ne retrouve pas tous les rangs cachés ; compare chaque valeur "
           "singulière au niveau du bruit, que tu estimes sur le tableau lui-même")
    if not filled(answer_MB4_13a):
        print("⏳ Ex MB4.13a : pas encore fait.")
    else:
        mine = as_floats(answer_MB4_13a)
        report(mine is not None and mine.shape == (5,) and mine.tolist() == found,
               "Ex MB4.13a : ta réponse est ce que rend ta fonction sur les cinq tableaux",
               "Ex MB4.13a : ta réponse n'est pas ce que rend hidden_rank_13 sur les cinq tableaux de TABLES_13 "
               "maintenant (la vérification les recalcule) : exécute à nouveau ta cellule")

    def exactly(stream, size):
        data = stream.read(size)
        if len(data) != size:
            raise OSError("échange interrompu")
        return data

    server = subprocess.Popen([sys.executable, "-I", str(hidden_file), "--serve"], stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        tables = []
        while True:                                              # three new series of five tables, at each run
            size = struct.unpack("<Q", exactly(server.stdout, 8))[0]
            if not size:
                break
            tables.append(np.load(io.BytesIO(exactly(server.stdout, size)), allow_pickle=False))
        got = [rank_of(f"Ex MB4.13 : hidden_rank_13 (tableau caché {k})", M) for k, M in enumerate(tables, start=1)]
        server.stdin.write(b"ranks\\n")                          # only now: the hidden ranks
        server.stdin.flush()
        truth = json.loads(exactly(server.stdout, 1) + server.stdout.readline())
        ranks, kinds = truth["ranks"], truth["kinds"]
        assert len(ranks) == len(kinds) == len(tables) == 15
    except (OSError, ValueError, KeyError, TypeError, AssertionError, struct.error) as exc:
        print("❌ Ex MB4.13 : la vérification n'a pas pu échanger les tableaux cachés et leurs rangs avec le processus qui "
              f"les tire ({type(exc).__name__} ; ta fonction a-t-elle touché à ce processus ?) : exécute à nouveau la "
              "cellule")
        raise StopCheck from None
    finally:
        if server.poll() is None:
            server.kill()
        server.wait()
    for series in range(3):                                      # each series: five tables, one of each kind
        wrong = []
        for k in range(5 * series, 5 * series + 5):
            if got[k] < ranks[k]:
                wrong.append(f"le tableau « {kinds[k]} » ({tables[k].shape[0]} × {tables[k].shape[1]}) : rendu {got[k]}, "
                             f"rang caché {ranks[k]} : ta fonction coupe trop tôt, une valeur singulière du signal reste "
                             "au-dessus du niveau du bruit")
            elif got[k] > ranks[k]:
                wrong.append(f"le tableau « {kinds[k]} » ({tables[k].shape[0]} × {tables[k].shape[1]}) : rendu {got[k]}, "
                             f"rang caché {ranks[k]} : ta fonction garde des valeurs singulières du bruit ; le bruit seul "
                             "monte jusqu'à σ(√m + √n) environ, et le dépasse parfois de peu (fiche §2) : estime σ sur le "
                             "tableau lui-même, et garde une marge")
        report(not wrong, f"série {series + 1} (cinq tableaux cachés, un de chaque type) : les cinq rangs, cinq fois sur "
               "cinq", f"série {series + 1} (cinq tableaux cachés, un de chaque type) : " + " ; ".join(wrong))
    report(elapsed[0] < 15, f"en {fr(elapsed[0], 2)} s pour les vingt tableaux",
           f"trop lent : {fr(elapsed[0], 1)} s pour les vingt tableaux, il faut moins de 15 s")
    verdict("MB4.13", all(results) and len(results) >= 5, "critère atteint : le bon rang pour les cinq tableaux du "
            "notebook et pour trois séries de cinq tableaux cachés, en moins de 15 secondes.",
            "critère pas encore atteint : relis les lignes ❌ ci-dessus.")


with checked("MB4.13"):
    check_c13()"""

NOTE_13 = (r"a) $(3, 1, 5, 2, 4)$ ; b) $(60, 70, 120, 50, 75)$, le rang plein ; c) $(48, 62, 67, 43, 58)$. La méthode "
           r"ci-dessus estime le bruit sur ce que le rang laisse de côté, $\hat\sigma^2 = \sum_{i > r}s_i^2/((m - r)(n - "
           r"r))$, compte les $s_i$ au-dessus de $1{,}2\,\hat\sigma(\sqrt m + \sqrt n)$, et recommence jusqu'à ce que "
           r"$r$ ne change plus. Le piège : ni une tolérance fixe ni une part d'énergie ne savent où s'arrête le bruit, "
           r"dont l'échelle change d'un tableau à l'autre.")

MB4_13 = Ex(
    "MB4.13", "🏆", 3, 40, "Défi : retrouver le rang caché de cinq tableaux bruités, cinq fois sur cinq, par leurs valeurs "
    "singulières",
    "retrouver le rang caché d'un tableau bruité en comparant ses valeurs singulières au niveau du bruit, estimé sur le "
    "tableau lui-même, et le vérifier sur des tableaux cachés.", "fiche §2 ; M12d (SVD, Eckart-Young) ; Ex MB4.2",
    tracks="C", given=GIVEN_13, note=NOTE_13,
    body=r"""Le notebook fournit `TABLES_13`, cinq tableaux de mesures de formes différentes. Chacun est la somme d'un tableau de rang $r$ (caché) et d'un bruit : chaque case reçoit un bruit indépendant, de moyenne nulle et de même écart-type $\sigma$ dans tout le tableau ; $\sigma$ change d'un tableau à l'autre, et n'est pas donné. Écris `hidden_rank_13(M)`, qui rend le rang caché d'un tableau (un entier $\ge 0$ : un tableau peut n'avoir aucun signal), en lisant ses valeurs singulières ; tout NumPy et SciPy sont permis (`np.linalg.svd(M, compute_uv=False)` donne les valeurs singulières).

**Critère de réussite** (les « cinq fois sur cinq » du titre) **:** le bon rang pour trois séries de cinq tableaux cachés, tirés à nouveau à chaque exécution ; chaque série a un tableau de chacun de ces cinq types (l'un facile, l'un dont le signal dépasse à peine le bruit, l'un dont les valeurs singulières du signal s'étalent sur un facteur 10 ou plus, l'un très allongé, et l'un sans signal ou à une échelle extrême), et doit être réussie cinq fois sur cinq ; le bon rang pour les cinq tableaux du notebook : la vérification recalcule ta réponse a) avec ta fonction ; le tout en moins de 15 secondes pour les vingt tableaux. Ta fonction n'exécute aucun code de la partie cachée du défi (`solutions/challenges/mb4_13.py`). Relève :
- a) les rangs que rend ta fonction pour les cinq tableaux (une liste de 5 entiers) ;
- b) `np.linalg.matrix_rank` de chacun (une liste de 5 entiers) ;
- c) le rang effectif à 99 % de chacun (une liste de 5 entiers).

Point de départ : le bruit seul a des valeurs singulières qui ne dépassent guère $\sigma(\sqrt m + \sqrt n)$ (fiche §2) ; $\sigma$ n'est pas donné, mais ce que le rang laisse de côté est presque tout du bruit, et tu sais ce que vaut son énergie (Eckart-Young).""",
    todo='''def hidden_rank_13(M):
    """The hidden rank of a noisy table M (an integer >= 0), read on its singular values."""
    raise NotImplementedError("hidden_rank_13 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB4_13a = answer_MB4_13b = answer_MB4_13c = ...
with wbm.attempt("MB4.13"):          # your function: ⏳ while it is not written
    answer_MB4_13a = ...  # a) a list of 5 integers: hidden_rank_13 of each table of TABLES_13
    answer_MB4_13b = ...  # b) a list of 5 integers: np.linalg.matrix_rank of each table
    answer_MB4_13c = ...  # c) a list of 5 integers: the effective rank at 99 % of each table''',
    check=answers_check("MB4.13", "bc") + "\n\n" + CHECK_13,
    solution='''def hidden_rank_13(M):
    """The hidden rank of a noisy table M (an integer >= 0), read on its singular values."""
    M = np.asarray(M, dtype=float)
    m, n = M.shape
    s = np.linalg.svd(M, compute_uv=False)
    r = 0
    for _ in range(50):
        if r >= min(m, n):
            break
        sigma = math.sqrt(float(np.sum(s[r:] ** 2)) / ((m - r) * (n - r)))     # the noise, on what the rank leaves aside
        r_new = int(np.sum(s > 1.2 * sigma * (math.sqrt(m) + math.sqrt(n))))   # above the level of the noise
        if r_new == r:
            break
        r = r_new
    return r


def effective_rank_13(M, level=0.99):
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.searchsorted(np.cumsum(s ** 2) / np.sum(s ** 2), level) + 1)


start_13 = time.perf_counter()
answer_MB4_13a = [hidden_rank_13(table) for table in TABLES_13]
answer_MB4_13b = [int(np.linalg.matrix_rank(table)) for table in TABLES_13]
answer_MB4_13c = [effective_rank_13(table) for table in TABLES_13]
print("a)", answer_MB4_13a, " b)", answer_MB4_13b, " c)", answer_MB4_13c, f" ({time.perf_counter() - start_13:.2f} s)")''',
    record='''import importlib.util as importlib_util_13r

spec_13r = importlib_util_13r.spec_from_file_location("mb4_13_record",
                                                      wbm.repo_root() / "solutions" / "challenges" / "mb4_13.py")
challenge_13r = importlib_util_13r.module_from_spec(spec_13r)
spec_13r.loader.exec_module(challenge_13r)
tables_13r = challenge_13r.notebook_tables()


def shares_13r(table, power=2):
    s = np.linalg.svd(table, compute_uv=False) ** power
    return np.cumsum(s) / np.sum(s)


wbm.record("MB4.13a", challenge_13r.notebook_ranks())
def numerical_rank_13r(table):
    """The oracle: the singular values above the default tolerance of np.linalg.matrix_rank, s1 max(m, n) eps."""
    s = np.linalg.svd(table, compute_uv=False)
    return int(np.sum(s > s[0] * max(table.shape) * np.finfo(float).eps))


wbm.record("MB4.13b", [numerical_rank_13r(t) for t in tables_13r],
           mistakes={"le rang ne dépasse pas le plus petit des deux côtés du tableau": [max(t.shape) for t in tables_13r]})
wbm.record("MB4.13c", [int(np.argmax(shares_13r(t) >= 0.99)) + 1 for t in tables_13r],
           mistakes={"le rang effectif à 99 % est le plus petit r dont la part atteint 0,99 : compte r à partir de 1":
                         [int(np.argmax(shares_13r(t) >= 0.99)) for t in tables_13r],
                     "l'énergie compte les carrés des valeurs singulières":
                         [int(np.argmax(shares_13r(t, power=1) >= 0.99)) + 1 for t in tables_13r]})''',
    after=[
        ("solution", answers_check("MB4.13", "bc") + "\n\n" + CHECK_13),
        ("md", "**Pour réfléchir** : pourquoi b) et c) ne trouvent-ils pas le rang caché ? Pourquoi une tolérance ou un "
               "seuil choisis sur les cinq tableaux du notebook ne suffisent-ils pas pour les tableaux cachés ? Les "
               "réponses sont dans `05_solutions.md`, section Notebook."),
    ],
)

PART_D = Part("D", "Défi", "Fiche §2. Le rang caché de tableaux bruités, retrouvé par leurs valeurs singulières, vérifié "
              "sur des tableaux cachés tirés à chaque exécution.", exercises=[MB4_13])

PARTS = [PART_A, PART_B, PART_C, PART_D]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | MB4.1 à MB4.4 | Les exercices papier (vérification) | ✏️ | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            rows.append(ex.table_row(part.key if i == 0 else ""))
    if kind == "exercise":
        title = "# MB4 · Rang faible et recherche d'information — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). Dans "
               "les parties A à D, donne les valeurs que rend le calcul, **sans les arrondir** : les décimales "
               "demandées sont celles de ta copie. « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli : ce qui n'est pas fait affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/mb4_rang_faible/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py MB4`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# MB4 · Rang faible et recherche d'information — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : les ventes de quatre boulangeries, les relevés de stations "
               "météo, les ingrédients d'un carnet de recettes, et trois jurys d'un concours de pâtisserie.\n"
               "- Écrire les trois fonctions de `mymath/ranks.py` (`rank_factorization`, `borda_scores`, "
               "`random_ranking_mrr`) et les tester.\n"
               "- Prédire puis simuler le MRR d'un ordre tiré au hasard, tracer des courbes de saturation, corriger trois "
               "erreurs classiques, et relever un défi.\n\n"
               r"**Rappel express.** Une matrice $(m, n)$ de rang $r$ est un produit $\mathbf{C}\mathbf{F}$ : "
               r"$\mathbf{C}$ ses $r$ colonnes pivots, $\mathbf{F}$ les $r$ lignes non nulles de sa forme échelonnée "
               r"réduite ; $r(m + n)$ nombres stockés, $r(m + n - r)$ libres ; $\mathbf{C}(\mathbf{F}\mathbf{x})$ coûte "
               r"$r(m + n)$ multiplications. L'énergie $\lVert\mathbf{M}\rVert_F^2 = \sum_is_i^2$ ; le rang effectif à "
               r"$\tau$, le plus petit $r$ dont la part atteint $\tau$ ; le rang stable $\sum_is_i^2/s_1^2$. La surprise "
               r"$-\ln\frac nN$, le poids corrigé $\ln\frac{N - n + 1/2}{n + 1/2}$. La saturation $s(x) = "
               r"\frac{x(k_1 + 1)}{x + k_1}$, et la normalisation $\nu = 1 - b + b\ell$, qui remplace $k_1$ par "
               r"$k_1\nu$. Borda : $n - j$ points au rang $j$ ; la somme des $\frac{1}{c + \text{rang}}$. Pour un ordre "
               r"tiré au hasard, $P(R = j) = \binom{n - j}{q - 1}\big/\binom nq$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu factoriser une matrice de rang $r$ par ses colonnes pivots, en trouver une autre "
               "factorisation, et compter les nombres stockés et libres ?\n"
               "2. Sais-tu mesurer le rang effectif et le rang stable d'un tableau mesuré, et appliquer une matrice "
               "factorisée dans l'ordre le moins coûteux ?\n"
               "3. Sais-tu calculer le poids d'un indice rare, et dire quand le poids corrigé devient négatif ?\n"
               "4. Sais-tu étudier la saturation et la normalisation par la longueur, et prévoir l'effet de $k_1$ et de "
               "$b$ ?\n"
               "5. Sais-tu fusionner des classements par Borda et par la somme des $\\frac{1}{c + \\text{rang}}$, et dire "
               "pourquoi ces fusions ne dépendent pas des échelles ?\n"
               "6. Sais-tu calculer recall@k, precision@k et le MRR, et leur valeur pour un ordre tiré au hasard ?\n\n"
               "**La suite** : le chapitre bonus B4 de workbookIA, qui applique ces outils.")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter=CHAPTER) if kind == "exercise" else setup_cell(kind))
    cells += objectives_cell()
    cells += paper_part(kind)
    for part in PARTS:
        cells += part_cells(part, kind)
    cells += footer_cells(kind)
    return cells


# ---------------------------------------------------------------------------
# Build-time literals of the data and of the hidden cases, computed here by private functions (never the answer of a
# question), and the assertions that make them fair (the reference passes, the classic wrong versions are seen)
# ---------------------------------------------------------------------------
def load_module(path: Path, name: str):
    """A Python file of the repository, loaded as a module of its own (its relative imports are not used)."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def literal(value) -> str:
    """A Python literal of value (floats by repr: exact; inf written math.inf), wrapped for reading."""
    text = pprint.pformat(value, width=112, compact=True, sort_dicts=False)
    return re.sub(r"(?<![\w.])inf\b", "math.inf", text)


def _rref_exact(np, M):
    """The reduced form of M, exactly (SymPy on the decimal fractions), and its pivots (the colleague's exact_rref_12)."""
    import sympy as sp
    R, pivots = sp.Matrix([[sp.Rational(str(x)) for x in row] for row in np.asarray(M, dtype=float)]).rref()
    return np.array(R, dtype=float), list(pivots)


def _borda(np, R):
    R = np.asarray(R)
    return (R.shape[1] - 1 - np.argsort(R, axis=1)).sum(axis=0)


def _borda_bad(np, R):
    R = np.asarray(R)
    return (R.shape[1] - 1 - R).sum(axis=0)


def _is_involution(np, row):
    row = np.asarray(row)
    return bool(np.array_equal(row[row], np.arange(len(row))))


def build_constants() -> dict:
    """The literals written in the cells, by placeholder, with the assertions that make the data and the hidden cases
    fair."""
    import numpy as np

    sys.path.insert(0, str(ROOT / "solutions"))
    from mymath_ref import ranks as ref                     # noqa: E402 - the reference, for the assertions
    out = {}

    # MB4.8: measurements of the foundry's laboratory, a table of rank 2 (seed 7508, the data of work_c/nb_values.py)
    rng = np.random.default_rng(7508)
    C0, F0 = rng.integers(1, 10, (6, 2)), rng.integers(1, 10, (2, 5))
    M8 = np.round(C0 @ F0 / 7, 3)
    assert M8[0].tolist() == [8.286, 12.286, 4.0, 2.571, 4.857]
    assert [ref.rank_factorization(M8, tol=t)[0].shape[1] for t in (1e-10, 1e-2)] == [5, 2]
    C8, F8 = ref.rank_factorization(M8, tol=1e-2)
    assert abs(float(np.max(np.abs(C8 @ F8 - M8))) - 0.000828) < 5e-7
    out["__M_8__"] = literal(M8.tolist())

    # MB4.9: 7 judges rank 9 candidates (seed 7509); the Borda winner is unique
    rng = np.random.default_rng(7509)
    R9 = np.array([rng.permutation(9) for _ in range(7)])
    b9 = ref.borda_scores(R9)
    assert b9.tolist() == [24, 26, 22, 31, 34, 23, 25, 42, 25] and (b9 == b9.max()).sum() == 1
    assert not np.array_equal(b9, _borda_bad(np, R9))
    out["__RANKINGS_9__"] = literal(R9.tolist())

    # MB4.11: hidden calls (non-dyadic x, k1 = 0, 3, 1 and the infinity; a hidden call of each drawing); the curves
    # of draw_lengths_11 are compared at the points of the grid of index 0, 8, 16..., dropping a point where a value of either
    # call is within 0.025 of a rounding limit at 6 decimals (so that no ⚠️ and no rounding chance decide)
    from fractions import Fraction

    def near_limit(value, decimals=6):
        scaled = abs(float(value)) * 10 ** decimals
        return abs(scaled - math.floor(scaled) - 0.5) < 0.025

    def normalised(x, k1, b, ell):
        return x * (k1 + 1) / (x + k1 * (1 - b + b * ell))

    calls = [(1, Fraction(1, 2), (Fraction(1, 2), 1, 2), 12), (2, Fraction(1, 4), (Fraction(3, 5), 3), 15)]
    idx = [i for i in range(0, 241, 8)
           if not any(near_limit(normalised(Fraction(xmax) * i / 240, k1, b, ell))
                      for k1, b, ells, xmax in calls for ell in ells)]
    assert len(idx) >= 24, idx
    xs11, k1s11 = [0.0, 0.4, 1.0, 2.5, 7.0, 31.0], [0, 3, 1, math.inf]       # k1 in {1, 2, 3} (syllabus), 0 and the
    for k1 in k1s11[1:3]:                                                    # infinity, in another order
        assert not any(near_limit(x * (k1 + 1) / (x + k1)) for x in xs11)
    out["__HIDDEN_C11__"] = literal({"x": xs11, "k1": k1s11, "id_s": "MB4.11e", "draw_k1": [3, 1, math.inf],
                                     "draw_xmax": 9, "id_l": "MB4.11f", "k1_l": 2, "b_l": 0.25, "ells": [0.6, 3],
                                     "xmax_l": 15, "id_h": "MB4.11g", "idx": idx})

    # MB4.12: the 4 x 6 rankings (seed 7512): no row is its own inverse, and the colleague's Borda differs
    rng = np.random.default_rng(7512)
    while True:
        R12 = np.array([rng.permutation(6) for _ in range(4)])
        if all(not _is_involution(np, row) for row in R12) and not np.array_equal(_borda(np, R12), _borda_bad(np, R12)):
            break
    assert _borda(np, R12).tolist() == [15, 9, 10, 2, 18, 6] and _borda_bad(np, R12).tolist() == [10, 12, 8, 15, 11, 4]
    out["__RANK_12__"] = literal(R12.tolist())
    # its hidden cases: tables of non-dyadic floats (rank 1 without a pivot in column 0; pivots 0 and 2; pivots 0, 1
    # and 3), rankings (seed 7522) with no row its own inverse, and other notebooks of recipes
    tables = [[[0.0, 0.3, 0.6, -0.9], [0.0, 0.7, 1.4, -2.1], [0.0, -1.1, -2.2, 3.3]],
              [[1.3, -1.95, 0.4, 2.1, 0.25], [0.2, -0.3, 1.1, 2.4, -1.0], [-0.7, 1.05, 0.9, 1.1, -1.25],
               [2.1, -3.15, -0.6, 0.9, 1.65]],
              [[0.9, 0.5, 0.4, -0.3], [-0.4, 1.6, -2.0, 0.6], [1.7, -0.8, 2.5, 1.4], [0.3, 2.2, -1.9, -0.5],
               [-1.2, 0.1, -1.3, 0.8]]]
    for table, pivots in zip(tables, ([1], [0, 2], [0, 1, 3])):
        A = np.array(table)
        R, piv = _rref_exact(np, A)
        assert piv == pivots, (piv, pivots)
        C, F = ref.rank_factorization(A)
        assert np.allclose(A[:, piv] @ R[:len(piv)], A) and np.allclose(C, A[:, piv]) and np.allclose(F, R[:len(piv)])
        assert not np.allclose(R[:, piv] @ R[:len(piv)], A)                    # the colleague's version fails
        assert not np.allclose(A[:, :len(piv)] @ R[:len(piv)], A)              # the first r columns fail
        assert any(abs(x * 2 ** 20 - round(x * 2 ** 20)) > 1e-9 for x in A.ravel())   # not dyadic
    rng = np.random.default_rng(7522)
    rankings = []
    for judges, candidates in ((5, 7), (3, 5), (6, 8)):
        while True:
            R = np.array([rng.permutation(candidates) for _ in range(judges)])
            if all(not _is_involution(np, row) for row in R) and not np.array_equal(_borda(np, R), _borda_bad(np, R)):
                break
        assert np.array_equal(ref.borda_scores(R), _borda(np, R))
        rankings.append(R.tolist())
    notebooks = [[7, 130], [33, 61], [260, 410], [1, 13]]
    assert not any(near_limit(math.log(N / n)) for n, N in notebooks)
    out["__CASES_C12__"] = literal({"tables": tables, "rankings": rankings, "notebooks": notebooks, "id": "MB4.12d"})

    # MB4.13: the notebook tables of solutions/challenges/mb4_13.py; the method of the check finds their ranks; the naive
    # methods (np.linalg.matrix_rank, a fixed tolerance) and the naive inverse ones (a share of the energy, s > s1/2)
    # fail on them; c) is far from a limit of its threshold
    challenge = load_module(ROOT / "solutions" / "challenges" / "mb4_13.py", "mb4_13_build")
    tables13, truth13 = challenge.notebook_tables(), challenge.notebook_ranks()
    assert [challenge.reference(t) for t in tables13] == truth13 == [3, 1, 5, 2, 4]
    for name, method in (("matrix_rank", lambda t, s: int(np.linalg.matrix_rank(t))),
                         ("fixed tolerance", lambda t, s: int(np.sum(s > 1e-6))),
                         ("energy 99 %", lambda t, s: int(np.argmax(np.cumsum(s ** 2) / np.sum(s ** 2) >= 0.99)) + 1),
                         ("energy 90 %", lambda t, s: int(np.argmax(np.cumsum(s ** 2) / np.sum(s ** 2) >= 0.90)) + 1),
                         ("half of s1", lambda t, s: int(np.sum(s > s[0] / 2)))):
        found = [method(t, np.linalg.svd(t, compute_uv=False)) for t in tables13]
        assert found != truth13, name
    for t in tables13:
        shares = np.cumsum(np.linalg.svd(t, compute_uv=False) ** 2)
        shares = shares / shares[-1]
        k = int(np.argmax(shares >= 0.99))
        assert shares[k] - 0.99 > 1e-6 and 0.99 - shares[k - 1] > 1e-6
    return out


PREPARED = []


def prepare() -> None:
    """Write the build-time literals in every cell text (placeholders __NAME__). Idempotent."""
    if PREPARED:
        return
    constants = build_constants()

    def fill(text):
        for key, value in constants.items():
            text = text.replace(key, value)
        return text

    for part in PARTS:
        part.given = fill(part.given)
        for ex in part.exercises:
            for field_name in ("body", "todo", "check", "solution", "record", "given", "note"):
                setattr(ex, field_name, fill(getattr(ex, field_name)))
            ex.after = [(kind, fill(text)) for kind, text in ex.after]
    left = {match for part in PARTS for ex in part.exercises
            for text in (ex.body, ex.todo, ex.check, ex.solution, ex.record, ex.given, *(t for _, t in ex.after))
            for match in re.findall(r"__[A-Z][A-Z0-9_]*__", text)}
    assert not left, f"placeholders left: {sorted(left)}"
    PREPARED.append(True)


def main() -> int:
    prepare()
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
