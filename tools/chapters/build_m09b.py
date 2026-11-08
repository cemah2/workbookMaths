#!/usr/bin/env python
"""Build the two notebooks of chapter M09b from a single source (used by Claude).

    python tools/chapters/build_m09b.py
    python tools/run_all_notebooks.py chapitres/m09b_moindres_carres/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m09b_moindres_carres/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M09b.1 to M09b.12, 🔗 M09b.20 and M09b.21); parts A to C are the notebook
exercises. Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it. The data
are new: none is a test case of tests/test_m09b_linreg.py, an example of the fiche or of a docstring of linreg.py, or an
example of workbookIA 0B, 8, 9 and 10 (no points (0, 1), (1, 2), (2, 4), no targets 1, 4, 6 with predictions 2, 4, 3,
no targets 3, 5, 4, 8, 10, no Σxy = 6 with Σx² = 4, no S(1,8 ; 0,5), no predictions 1, 2, 4 around f = 2, no counts 9
for (3, 2), 285 for (10, 3) or 164 for (8, 3), no λ = 0,0625, no shop tempo, no California, no wind on a mountain).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M09b"
FOLDER = "chapitres/m09b_moindres_carres"

F = 'kind="fraction", simplified=True'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M09b.1", "MSE, RMSE, MAE et loss de Huber de quatre résidus", [
        ("a", "a list of 4 numbers", "R1.tolist()",
         '''decimals=1, mistakes={"un résidu est y − ŷ : la valeur réelle moins la prédiction": (-R1).tolist()}'''),
        ("b", "a number (4 decimals)", "float(np.mean(R1 ** 2))",
         '''decimals=4, mistakes={"la MSE est une moyenne : divise la somme des carrés par n": float(np.sum(R1 ** 2)), '''
         '''"c'est la RMSE ; la MSE est la moyenne des carrés, sans racine": float(np.sqrt(np.mean(R1 ** 2)))}'''),
        ("c", "a number (3 decimals)", "float(np.mean(np.abs(R1)))",
         '''decimals=3, mistakes={"la MAE est la moyenne des valeurs absolues : un résidu négatif compte en positif": '''
         '''float(np.mean(R1))}'''),
        ("d", "a number (5 decimals)", "huber_mean(R1, 1.0)",
         '''decimals=5, mistakes={"au-dessus de δ, la loss vaut δ(|r| − δ/2), pas |r|": '''
         '''float(np.mean(np.where(np.abs(R1) <= 1, R1 ** 2 / 2, np.abs(R1)))), '''
         '''"sous δ, la loss vaut r²/2 : le facteur 1/2 compte": '''
         '''float(np.mean(np.where(np.abs(R1) <= 1, R1 ** 2, np.abs(R1) - 0.5)))}'''),
        ("e", "a number (5 decimals)", "huber_mean(R1, 5.0)",
         '''decimals=5, mistakes={"sous δ, la loss vaut r²/2, pas r²": float(np.mean(R1 ** 2))}'''),
        ("f", "a number (4 decimals)", "huber_mean(R1, 0.25) / 0.25",
         '''decimals=4, mistakes={"la question demande la loss divisée par δ = 0,25": huber_mean(R1, 0.25)}'''),
        ("g", "a number", "4",
         '''mistakes={"il faut que tous les résidus soient sous le seuil, le plus grand compris": {1, 2}}'''),
    ]),

    Paper("M09b.2", "La décomposition SCT = SCE + SCR et le R² d'un ajustement donné", [
        ("a", "a number", "4"),
        ("b", "a number", "16.0",
         '''decimals=2, mistakes={"SCT est une somme de carrés, pas une moyenne": 3.2}'''),
        ("c", "a number (2 decimals)", "5.2",
         '''decimals=2, mistakes={"SCR est une somme de carrés, pas une moyenne": 1.04}'''),
        ("d", "a number (2 decimals)", "10.8",
         '''decimals=2, mistakes={"SCE compare les prédictions à la moyenne ȳ, pas aux cibles": 5.2}'''),
        ("e", "a number (3 decimals)", "0.675",
         '''decimals=3, mistakes={"R² = 1 − SCR/SCT : ce nombre est SCR/SCT": 0.325}'''),
        ("f", "a list of 2 numbers (1 decimal)", "[5.5, 7.5]",
         '''decimals=1, mistakes={"l'ordre de l'énoncé : SCR d'abord, puis SCE": [7.5, 5.5]}'''),
        ("g", "an irreducible fraction, as text", '"21/32"',
         F + ''', mistakes={"c'est SCE/SCT ; la question demande 1 − SCR/SCT, qui n'est pas égal ici": "15/32"}'''),
    ]),

    Paper("M09b.3", "Les gradients de aᵀw, wᵀAw et ‖y − Xw‖², composante par composante en dimension 2", [
        ("a", "a number", "11", '''mistakes={"a·w = a₁w₁ + a₂w₂ : attention aux deux signes moins": 5}'''),
        ("b", "a list of 2 numbers", "[4, -3]",
         '''mistakes={"le gradient de w ↦ a·w est a : il ne dépend pas de w": [8, 3]}'''),
        ("c", "a number", "5"),
        ("d", "a list of 2 numbers", "[3, -4]",
         '''mistakes={"A n'est pas symétrique : le gradient est (A + Aᵀ)w, pas 2Aw": [0, -10], '''
         '''"c'est Aw seul : chaque produit w_i w_j se dérive par rapport aux deux coordonnées": [0, -5]}'''),
        ("e", "a list of 3 numbers", "[3, 2, -1]",
         '''mistakes={"r = y − Xw, pas Xw − y": [-3, -2, 1]}'''),
        ("f", "a number", "14"),
        ("g", "a list of 2 numbers", "[-4, -18]",
         '''mistakes={"le gradient est −2Xᵀ(y − Xw) : le signe moins vient de la dérivée de y − Xw": [4, 18], '''
         '''"le facteur 2 vient de la dérivée du carré": [-2, -9]}'''),
    ]),

    Paper("M09b.4", "Les équations normales d'un modèle à deux features, sans ordonnée à l'origine", [
        ("a", "a list of 2 integers", "[2, 2]",
         '''mistakes={"XᵀX a une ligne et une colonne par feature : sa forme est (p, p)": [4, 4]}'''),
        ("b", "a matrix", "[[6, 4], [4, 6]]"),
        ("c", "a list of 2 numbers", "[12, 11]",
         '''mistakes={"Xᵀy : la ligne j de Xᵀ est la colonne j de X, multipliée par y": [11, 12]}'''),
        ("d", "a list of 2 numbers (2 decimals)", "[1.4, 0.9]",
         '''decimals=2, mistakes={"l'inverse d'une 2 × 2 change le signe des deux nombres hors de la diagonale": '''
         '''[5.8, 5.7]}'''),
        ("e", "a list of 4 numbers (2 decimals)", "[-0.2, 0.3, -0.4, 0.1]",
         '''decimals=2, mistakes={"r = y − ŷ, pas ŷ − y": [0.2, -0.3, 0.4, -0.1]}'''),
        ("f", "a list of 2 numbers (2 decimals)", "[0.0, 0.0]", "decimals=2"),
        ("g", "a number (2 decimals)", "0.3",
         '''decimals=2, mistakes={"SCR est une somme de carrés, pas une moyenne": 0.075}'''),
    ]),

    Paper("M09b.5", "La colonne de 1 : l'ordonnée à l'origine et des résidus de moyenne nulle", [
        ("a", "a matrix", "[[4, 12], [12, 50]]",
         '''mistakes={"le coin en bas à droite est la somme des x², pas le carré de la somme": [[4, 12], [12, 144]]}'''),
        ("b", "a list of 2 numbers", "[16, 69]"),
        ("c", "a list of 2 numbers (2 decimals)", "[-0.5, 1.5]",
         '''decimals=2, mistakes={"l'ordre de l'énoncé : w₀ (l'ordonnée à l'origine) d'abord, puis w₁": [1.5, -0.5]}'''),
        ("d", "a list of 4 numbers (2 decimals)", "[-1.0, 0.5, 1.0, -0.5]",
         '''decimals=2, mistakes={"r = y − ŷ, pas ŷ − y": [1.0, -0.5, -1.0, 0.5]}'''),
        ("e", "a number (2 decimals)", "4.0", "decimals=2"),
        ("f", "a list of 2 numbers", "[3, 4]", '''mistakes={"l'ordre : x̄ d'abord, puis ȳ": [4, 3]}'''),
        ("g", "a list of 2 numbers (2 decimals)", "[4.0, 1.5]",
         '''decimals=2, mistakes={"centrer x change l'ordonnée à l'origine : le nouveau w₀ est la prédiction en x = x̄": '''
         '''[-0.5, 1.5]}'''),
    ]),

    Paper("M09b.6", "La matrice chapeau d'un petit tableau : H² = H et sa trace", [
        ("a", "a matrix", "[[3, 4], [4, 10]]"),
        ("b", "a matrix of integers", "[[10, -4], [-4, 3]]",
         '''mistakes={"l'inverse d'une 2 × 2 échange les deux nombres de la diagonale": [[3, -4], [-4, 10]], '''
         '''"l'inverse d'une 2 × 2 change le signe des nombres hors de la diagonale": [[10, 4], [4, 3]], '''
         '''"la question demande 14 fois l'inverse : des entiers": [[10 / 14, -4 / 14], [-4 / 14, 3 / 14]]}'''),
        ("c", "a matrix of integers", "[[10, 6, -2], [6, 5, 3], [-2, 3, 13]]",
         '''mistakes={"la question demande 14 H : des entiers": '''
         '''[[10 / 14, 6 / 14, -2 / 14], [6 / 14, 5 / 14, 3 / 14], [-2 / 14, 3 / 14, 13 / 14]]}'''),
        ("d", "a number", "2", '''mistakes={"la trace de H vaut le nombre de colonnes de X, pas de lignes": 3}'''),
        ("e", "an integer from 1 to 3", "3",
         '''mistakes={"le levier est le nombre h_ii de la diagonale de H : prends le plus grand": 1, '''
         '''"le numéro du point, de 1 à 3 (pas un indice Python)": 2}'''),
        ("f", "a list of 3 integers", "[8, 16, 32]",
         '''mistakes={"la question demande 7 ŷ : des entiers": [8 / 7, 16 / 7, 32 / 7]}'''),
        ("g", "a list of 3 integers", "[6, -9, 3]", '''mistakes={"r = y − ŷ, pas ŷ − y": [-6, 9, -3]}'''),
    ]),

    Paper("M09b.7", "Compter les monômes des features polynomiales", [
        ("a", "an integer", "4",
         '''mistakes={"compte aussi les produits croisés, pas seulement les puissances u³ et v³": 2}'''),
        ("b", "an integer", "10", '''mistakes={"constante comprise : compte aussi le monôme 1": 9}'''),
        ("c", "an integer", "20",
         '''mistakes={"sans la constante : retire le monôme 1": 21, '''
         '''"compte aussi les cinq monômes de degré 1": 15}'''),
        ("d", "an integer", "69", '''mistakes={"sans la constante : retire le monôme 1": 70}'''),
        ("e", "an integer", "21", '''mistakes={"compte aussi les carrés x_i²": 15}'''),
        ("f", "an integer", "15",
         '''mistakes={"degré exactement 4 : sans les monômes de degré plus petit": {34, 35}, '''
         '''"compte aussi les produits croisés (x³y, x²yz…), pas seulement x⁴, y⁴ et z⁴": 3}'''),
        ("g", "an integer", "6",
         '''mistakes={"plus de 1 000 colonnes : écris le nombre de colonnes degré par degré, constante exclue": {5, 7}}'''),
    ]),

    Paper("M09b.8", "Ridge en dimension 2 : résoudre (XᵀX + λI)w = Xᵀy pour trois valeurs de λ", [
        ("a", "a matrix of 2 rows and 3 columns", "[[2, 1, 3], [1, 2, 0]]"),
        ("b", "a list of 2 numbers", "[2, -1]"),
        ("c", "a list of 2 numbers (3 decimals)", "[1.125, -0.375]", "decimals=3"),
        ("d", "a list of 2 numbers (2 decimals)", "[0.8, -0.2]",
         '''decimals=2, mistakes={"λ s'ajoute sur la diagonale de XᵀX seulement (λI), pas à chaque nombre": '''
         '''[12 / 7, -9 / 7]}'''),
        ("e", "a list of 3 numbers (4 decimals)", "[5 ** 0.5, 90 ** 0.5 / 8, 17 ** 0.5 / 5]",
         '''decimals=4, mistakes={"la norme est la racine de la somme des carrés": [5.0, 90 / 64, 17 / 25]}'''),
        ("f", "a list of 2 numbers (2 decimals)", "[3.0, 5.24]",
         '''decimals=2, mistakes={"SCR mesure seulement les résidus y − Xw, sans la pénalité λ‖w‖²": [3.0, 6.6]}'''),
        ("g", "a list of 2 numbers", "[0, 0]"),
    ]),

    Paper("M09b.9", "Ridge comme MAP : un prior gaussien et λ = σ²/τ²", [
        ("a", "a number", "16", '''mistakes={"λ = σ²/τ² : avec les carrés, au numérateur et au dénominateur": {4, 8}}'''),
        ("b", "a number", "2"),
        ("c", "a list of 2 numbers (4 decimals)", "[2 / 3, 1 / 3]",
         '''decimals=4, mistakes={"c'est l'estimation du maximum de vraisemblance : le MAP ajoute λ sur la diagonale": '''
         '''[8 / 9, 5 / 9]}'''),
        ("d", "a list of 2 numbers (4 decimals)", "[8 / 9, 5 / 9]",
         '''decimals=4, mistakes={"c'est l'estimation MAP : sans prior, λ = 0": [2 / 3, 1 / 3]}'''),
        ("e", "a number", "8", '''mistakes={"σ double : σ² est multiplié par 4": 4}'''),
        ("f", "a number (4 decimals)", "0.4 ** 0.5",
         '''decimals=4, mistakes={"λ = σ²/τ² donne τ² = σ²/λ : la question demande τ, sa racine": 0.4}'''),
        ("g", "True or False", "True",
         '''mistakes={"λ = σ²/τ² est un rapport : multiplier σ et τ par 10 multiplie σ² et τ² par 100": False}'''),
    ]),

    Paper("M09b.10", "Les pénalités L1 et L2 de trois vecteurs de poids, et leurs boules", [
        ("a", "a list of 3 numbers", "[3, 3, 3]",
         '''mistakes={"la norme L1 additionne les valeurs absolues : |−1| = 1": [3, 3, 1]}'''),
        ("b", "a list of 3 numbers", "[9, 3, 5]",
         '''decimals=4, mistakes={"la pénalité L2 est le carré de la norme : sans racine": '''
         '''[3.0, 3 ** 0.5, 5 ** 0.5]}'''),
        ("c", "a letter: \"u\", \"v\" or \"t\"", '"v"',
         '''mistakes={"compare les carrés des normes de b), pas les normes L1 (toutes égales)": {"u", "t"}}'''),
        ("d", "letters, e.g. \"AC\"", '"ABD"',
         '''mistakes={"un point est sur le bord quand |w₁| + |w₂| = 1 exactement : refais la somme des valeurs absolues '''
         '''de chaque point": {"AB", "AD", "BD", "A", "B", "D", "ABCD", "ABC", "ACD", "BCD", "AC", "BC", "CD", "C"}}'''),
        ("e", "a list of 2 numbers (4 decimals)", "[1.0, 0.5 ** 0.5]",
         '''decimals=4, mistakes={"l'ordre : la plus grande valeur d'abord": [0.5 ** 0.5, 1.0], '''
         '''"la question demande la norme ‖w‖, pas son carré": [1.0, 0.5]}'''),
        ("f", "an integer", "6",
         '''mistakes={"la boule L1 n'est pas un cube : ses coins sont sur les axes, deux par axe": 8}'''),
        ("g", "a list of 2 numbers (2 decimals)", "[0.4, 0.65]",
         '''decimals=2, mistakes={"la pénalité L2 est le carré de la norme : sans racine": [0.4, 0.1 * 6.5 ** 0.5]}'''),
    ]),

    Paper("M09b.11", "La log-vraisemblance gaussienne d'un modèle linéaire et l'estimation de σ²", [
        ("a", "a number (2 decimals)", "1.04",
         '''decimals=2, mistakes={"le maximum de vraisemblance divise SCR par n ; n − p donne l'estimateur sans biais": '''
         '''5.2 / 3}'''),
        ("b", "a number (4 decimals)", "5.2 / 3",
         '''decimals=4, mistakes={"l'estimateur sans biais divise par n − p = 5 − 2": {1.04, 1.3}}'''),
        ("c", "a number (4 decimals)", "-2.5 * (math.log(2 * math.pi * 1.04) + 1)",
         '''decimals=4, mistakes={"le logarithme népérien (ln), pas le logarithme décimal": '''
         '''-2.5 * (math.log10(2 * math.pi * 1.04) + 1)}'''),
        ("d", "a number (4 decimals)", "-2.5 * math.log(2 * math.pi) - 5.2 / 2",
         '''decimals=4, mistakes={"le terme des résidus est −SCR/(2σ²) : divise par 2": -2.5 * math.log(2 * math.pi) - 5.2}'''),
        ("e", "a number (2 decimals)", "0.15",
         '''decimals=2, mistakes={"la droite des moindres carrés a la plus petite SCR, donc la plus grande '''
         '''log-vraisemblance : la différence est positive": -0.15}'''),
        ("f", "a number (4 decimals)", "math.exp(0.15)",
         '''decimals=4, mistakes={"le rapport des vraisemblances est l'exponentielle de la différence des logs, dans le '''
         '''même ordre": math.exp(-0.15)}'''),
        ("g", "a list of 2 numbers (2 decimals)", "[4.0, 4.0]", "decimals=2"),
    ]),

    Paper("M09b.12", "L'estimateur rétréci c·x̄ : biais, variance et erreur quadratique", [
        ("a", "a number", "-1", '''mistakes={"le biais est E[c x̄] − μ : ici, il est négatif": 1}'''),
        ("b", "a number (2 decimals)", "0.25",
         '''decimals=2, mistakes={"V(c x̄) = c² V(x̄) : le facteur est au carré": 0.5, '''
         '''"V(x̄) = σ²/n : divise par n": 2.25}'''),
        ("c", "a number (2 decimals)", "1.25",
         '''decimals=2, mistakes={"l'erreur quadratique est biais² + variance : le biais au carré": -0.75}'''),
        ("d", "a number", "1", '''mistakes={"V(x̄) = σ²/n : divise par n": 9}'''),
        ("e", "a number (2 decimals)", "0.8", "decimals=2"),
        ("f", "a number (2 decimals)", "0.8", "decimals=2"),
        ("g", "a number (2 decimals)", "0.2",
         '''decimals=2, mistakes={"le c optimal fait intervenir μ²/(μ² + σ²/n) : μ au carré": 1 / 3}'''),
    ]),

    Paper("M09b.20", "Pont : la loss d'un modèle linéaire et son gradient pour un batch", [
        ("a", "a list of 4 numbers", "(X20 @ W20).tolist()", "decimals=2"),
        ("b", "a list of 4 numbers", "R20.tolist()",
         '''decimals=2, mistakes={"r = y − ŷ, pas ŷ − y": (-R20).tolist()}'''),
        ("c", "a number (2 decimals)", "float(np.mean(R20 ** 2))",
         '''decimals=2, mistakes={"la MSE est une moyenne : divise par 4": float(np.sum(R20 ** 2))}'''),
        ("d", "a list of 3 numbers", "(X20.T @ R20).tolist()", "decimals=2"),
        ("e", "a list of 3 numbers (2 decimals)", "G20.tolist()",
         '''decimals=2, mistakes={"le gradient de la MSE est −(2/n)Xᵀr : le signe moins": (-G20).tolist(), '''
         '''"la MSE divise par n = 4 : son gradient aussi": (4 * G20).tolist()}'''),
        ("f", "a list of 3 numbers (3 decimals)", "(W20 - 0.1 * G20).tolist()",
         '''decimals=3, mistakes={"on descend : w − η × gradient, pas w + η × gradient": (W20 + 0.1 * G20).tolist()}'''),
        ("g", "a number (4 decimals)", "float(np.mean((Y20 - X20 @ (W20 - 0.1 * G20)) ** 2))", "decimals=4"),
    ]),

    Paper("M09b.21", "Pont : pourquoi standardiser les colonnes avant ridge", [
        ("a", "a list of 2 numbers (2 decimals)", "[0.5, 1.0]", "decimals=2"),
        ("b", "a list of 2 numbers (2 decimals)", "[0.5, 0.5]",
         '''decimals=2, mistakes={"ridge ajoute λ sur la diagonale de XᵀX seulement, pas à chaque nombre": [0.5, 0.25]}'''),
        ("c", "a list of 2 numbers (2 decimals)", "[0.05, 1.0]",
         '''decimals=2, mistakes={"la colonne est 10 fois plus grande : son poids est 10 fois plus petit": [5.0, 1.0]}'''),
        ("d", "a list of 2 numbers (4 decimals)", "[25 / 302, 203 / 604]",
         '''decimals=4, mistakes={"ridge ne s'adapte pas à l'unité : refais le calcul avec la colonne multipliée par 10, "'''
         '''"sans diviser le poids de b) par 10": [0.05, 0.5]}'''),
        ("e", "a list of 2 numbers (4 decimals)", "[-1.0, -703 / 604]", "decimals=4"),
        ("f", "a list of 2 numbers (2 decimals)", "[-1.5, -1.5]",
         '''decimals=2, mistakes={"les moindres carrés donnent les mêmes prédictions dans les deux unités, mais ce sont "'''
         '''"celles des moindres carrés, pas de ridge": [-1.0, -1.0]}'''),
        ("g", "True or False", "True",
         '''mistakes={"après standardisation, la colonne du prix est la même quelle que soit son unité": False}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math

import numpy as np

Y1 = np.array([12, 7, 9, 15], dtype=float)                                                           # M09b.1
R1 = Y1 - np.array([10, 8, 9.5, 11])


def huber_mean(r, delta):
    """The mean Huber loss of the residuals r."""
    a = np.abs(r)
    return float(np.mean(np.where(a <= delta, r ** 2 / 2, delta * (a - delta / 2))))


X20 = np.array([[1, 2, 1], [1, 0, -1], [1, 1, 3], [1, -1, 0]], dtype=float)                       # M09b.20
Y20, W20 = np.array([3, 0, 1, 1], dtype=float), np.array([0.5, 1, -1])
R20 = Y20 - X20 @ W20
G20 = -2 / 4 * X20.T @ R20'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M09b.1 à M09b.12, 🔗 M09b.20 et M09b.21)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"4/11\"` ;\n"
               "- une liste `[2, -1, 0]` pour un vecteur ou une forme, une liste de lignes `[[1, 0], [-2, 3]]` pour une "
               "matrice, `True` / `False`, ou des lettres entre guillemets, `\"AC\"`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M09b.26 to M09b.29)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np
import sympy

from wbm.nbtools import checked, drawn, run_pytest_group


def raised(function, *args, **kwargs):
    """The name of the exception that function(*args, **kwargs) raises, or "aucune" if it returns.

    NotImplementedError (a TODO not done yet) goes through, for wbm.attempt to show ⏳; so do the errors of a code
    that cannot run (a missing import, a misspelt name such as ValueErorr), for the check to name them."""
    try:
        function(*args, **kwargs)
    except (NotImplementedError, NameError, AttributeError, ImportError):
        raise
    except Exception as exc:  # noqa: BLE001 - any other error is the answer
        return type(exc).__name__
    return "aucune"


def r2_score_np(y, y_hat):
    """The R² of the predictions y_hat, 1 - SSR / SST, with NumPy only (for the experiments)."""
    y, y_hat = np.asarray(y, dtype=float), np.asarray(y_hat, dtype=float)
    return float(1 - np.sum((y - y_hat) ** 2) / np.sum((y - y.mean()) ** 2))'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M09b")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/linreg.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "Ici, NumPy est permis en entier, `@`, `.T`, `np.eye` et `np.linalg.solve` compris : tu as écrit leurs "
         "équivalents en M09a. Sont interdits les solveurs qui font tout le travail : `np.linalg.lstsq`, "
         "`np.linalg.pinv`, `np.linalg.inv`, `scipy` et `sklearn` (les tests s'en servent comme oracles, et un test "
         "vérifie que tu ne les utilises pas). Ne modifie jamais les tableaux reçus.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError", "LinAlgError"]
LINALG = ("np.linalg.solve lève une LinAlgError sur une matrice singulière : attrape-la (try/except "
          "np.linalg.LinAlgError) et lève une ValueError, comme le demande la docstring")


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of linreg.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_linreg_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m09b_linreg.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m09b_linreg.py", "{keyword}", impl="ref")')]


NDARRAY = "la docstring demande un tableau NumPy : np.array(...)"
X26, Y26 = "[[1, 2], [1, -1], [1, 0], [1, 3]]", "[4, 0, 2, 5]"
S26 = "[[1, 2], [2, 4], [3, 6]]"

M09B_26 = Ex(
    "M09b.26", "🔨", 1, 25, "Équations normales et résolution, avec ou sans ridge · `normal_equations, "
    "solve_least_squares`",
    "programmer les équations normales et leur résolution, avec une pénalité ridge, et refuser un système singulier.",
    "fiche §3 et §5", tracks="C, E", mymath="linreg.py",
    body=HOWTO + rf"""

Écris (fiche §3 et §5), en suivant les docstrings :
- `normal_equations(X, y)` : le couple $(\mathbf{{X}}^\top\mathbf{{X}}, \mathbf{{X}}^\top\mathbf{{y}})$, en tableaux NumPy de floats ; une `ValueError` si $\mathbf{{X}}$ n'est pas à deux dimensions, ou si $\mathbf{{y}}$ n'est pas un vecteur (à une dimension) d'une valeur par ligne de $\mathbf{{X}}$ : un $\mathbf{{y}}$ en colonne, de forme $(n, 1)$, est refusé ;
- `solve_least_squares(X, y, ridge=0.0)` : la solution de $(\mathbf{{X}}^\top\mathbf{{X}} + \lambda\mathbf{{I}})\mathbf{{w}} = \mathbf{{X}}^\top\mathbf{{y}}$, avec `np.linalg.solve` ; **tous** les poids sont pénalisés, celui d'une colonne de 1 compris. Une `ValueError` si les formes ne vont pas, si `ridge` est négatif, ou si la matrice est singulière (`np.linalg.solve` lève alors une `numpy.linalg.LinAlgError` : attrape-la).

Avec $\mathbf{{X}}$ = `{X26}` et $\mathbf{{y}}$ = `{Y26}` (une colonne de 1, puis une feature), la vérification calcule :
- a) et b) les deux éléments du couple de `normal_equations(X, y)` (une matrice, puis une liste) ;
- c) `solve_least_squares(X, y)` (une liste, 6 décimales) ;
- d) `solve_least_squares(X, y, ridge=2)` (une liste, 6 décimales) ;
- e) le nom de l'erreur levée par `solve_least_squares({S26}, [1, 2, 3])` ;
- f) `solve_least_squares({S26}, [1, 2, 3], ridge=0.5)` (une liste, 4 décimales) ;
- g) le nom de l'erreur levée par `solve_least_squares([[1, 0], [0, 1]], [1, 2], ridge=-0.5)` ;
- h) le nom du type de la valeur rendue par `solve_least_squares`, en texte.

Dans ta copie : calcule a), b) et c) à la main. Pourquoi e) est-elle singulière, et pourquoi f) ne l'est-elle plus ? Vérifie que la solution de f) est proportionnelle à $(1, 2)$ : pourquoi ?""",
    todo=LOAD_LEARNER,
    check=f'''X_26, y_26 = {X26}, {Y26}
with checked("M09b.26a"):
    wbm.check("M09b.26a", np.asarray(mymath.linreg.normal_equations(X_26, y_26)[0]).tolist(), computed=True)
with checked("M09b.26b"):
    wbm.check("M09b.26b", np.asarray(mymath.linreg.normal_equations(X_26, y_26)[1]).tolist(), computed=True)
with checked("M09b.26c"):
    wbm.check("M09b.26c", np.asarray(mymath.linreg.solve_least_squares(X_26, y_26)).tolist(), computed=True)
with checked("M09b.26d"):
    wbm.check("M09b.26d", np.asarray(mymath.linreg.solve_least_squares(X_26, y_26, ridge=2)).tolist(), computed=True)
with checked("M09b.26e"):
    wbm.check("M09b.26e", raised(mymath.linreg.solve_least_squares, {S26}, [1, 2, 3]), computed=True)
with checked("M09b.26f"):
    wbm.check("M09b.26f", np.asarray(mymath.linreg.solve_least_squares({S26}, [1, 2, 3], ridge=0.5)).tolist(),
              computed=True)
with checked("M09b.26g"):
    wbm.check("M09b.26g", raised(mymath.linreg.solve_least_squares, [[1, 0], [0, 1]], [1, 2], ridge=-0.5),
              computed=True)
with checked("M09b.26h"):
    wbm.check("M09b.26h", type(mymath.linreg.solve_least_squares(X_26, y_26)).__name__, computed=True)''',
    solution=LOAD_REF + f'''
normal_equations, solve_least_squares = mymath.linreg.normal_equations, mymath.linreg.solve_least_squares
X_26, y_26 = {X26}, {Y26}
XtX_26, Xty_26 = normal_equations(X_26, y_26)
print("a)", XtX_26.tolist(), " b)", Xty_26.tolist())
print("c)", solve_least_squares(X_26, y_26), " d)", solve_least_squares(X_26, y_26, ridge=2))
print("e)", raised(solve_least_squares, {S26}, [1, 2, 3]),
      " f)", solve_least_squares({S26}, [1, 2, 3], ridge=0.5).round(4))
print("g)", raised(solve_least_squares, [[1, 0], [0, 1]], [1, 2], ridge=-0.5),
      " h)", type(solve_least_squares(X_26, y_26)).__name__)''',
    record=f'''wbm.record("M09b.26a", [[4.0, 4.0], [4.0, 14.0]], decimals=6,
           mistakes={{"XᵀX est de forme (p, p) : X.T @ X, pas X @ X.T": (np.array({X26}) @ np.array({X26}).T).tolist()}})
wbm.record("M09b.26b", [11.0, 23.0], decimals=6)
wbm.record("M09b.26c", [1.55, 1.2], decimals=6)
wbm.record("M09b.26d", [1.05, 1.175], decimals=6,
           mistakes={{"la docstring pénalise tous les poids, celui de la colonne de 1 compris": [1.75, 1.0],
                      "λ s'ajoute sur la diagonale seulement : ridge * np.eye(p)": [0.633333, 1.2]}})
wbm.record("M09b.26e", "ValueError",
           mistakes={{"XᵀX est singulière ici (une colonne est le double de l'autre) : la docstring demande une "
                      "ValueError": "aucune",
                     "{LINALG}": "LinAlgError",
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "LinAlgError")}}})
wbm.record("M09b.26f", [0.198582, 0.397163], decimals=4)
wbm.record("M09b.26g", "ValueError",
           mistakes={{"ridge doit être positif ou nul : la docstring demande une ValueError": "aucune",
                     "{LINALG}": "LinAlgError",
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "LinAlgError")}}})
wbm.record("M09b.26h", "ndarray", mistakes={{"{NDARRAY}": {{"list", "tuple"}}}})''',
    after=tests_cells("test_normal_equations_ or test_solve_least_squares_"),
    note=r"a) et b) $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 4 & 4 \\ 4 & 14 \end{pmatrix}$ (le nombre de points, "
         r"$\sum x$, $\sum x^2$) et $\mathbf{X}^\top\mathbf{y} = (11, 23)$. c) $\frac{1}{40}\begin{pmatrix} 14 & -4 \\ -4 & 4 "
         r"\end{pmatrix}\begin{pmatrix} 11 \\ 23 \end{pmatrix} = (1{,}55 ;\ 1{,}2)$. d) La diagonale devient $(6, 16)$ : les "
         r"deux poids rétrécissent, l'ordonnée à l'origine comprise. e) La seconde colonne est le double de la première : "
         r"$\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 14 & 28 \\ 28 & 56 \end{pmatrix}$ a un déterminant nul. f) Avec "
         r"$\lambda > 0$, la matrice est inversible (fiche §5) ; et $\mathbf{X}^\top\mathbf{y} = (14, 28)$ est proportionnel "
         r"à $(1, 2)$, comme toutes les colonnes de $\mathbf{X}^\top\mathbf{X}$ : la solution l'est aussi. Parmi toutes les "
         r"solutions des moindres carrés ($w_1 + 2w_2 = 1$), ridge choisit une petite norme, dans la direction $(1, 2)$.",
)

X27, Y27 = "[[1, 0], [1, 1], [1, 2], [1, 3]]", "[1, 0, 2, 5]"

M09B_27 = Ex(
    "M09b.27", "🔨", 1, 20, "La matrice chapeau et les trois sommes de carrés · `hat_matrix, residual_decomposition`",
    "programmer la matrice chapeau sans inverse, et les trois sommes de carrés d'un ajustement.",
    "fiche §1 et §3 ; Ex M09b.26", tracks="C, E", mymath="linreg.py",
    body=rf"""Écris (fiche §1 et §3), en suivant les docstrings :
- `hat_matrix(X)` : $\mathbf{{H}} = \mathbf{{X}}(\mathbf{{X}}^\top\mathbf{{X}})^{{-1}}\mathbf{{X}}^\top$, **sans** calculer d'inverse : résous $\mathbf{{X}}^\top\mathbf{{X}}\,\mathbf{{M}} = \mathbf{{X}}^\top$ (`np.linalg.solve` accepte une matrice comme second membre), puis $\mathbf{{H}} = \mathbf{{X}}\mathbf{{M}}$ ; une `ValueError` si $\mathbf{{X}}$ n'est pas à deux dimensions ou si $\mathbf{{X}}^\top\mathbf{{X}}$ est singulière ;
- `residual_decomposition(y, y_hat)` : le triplet $(\mathrm{{SCT}}, \mathrm{{SCE}}, \mathrm{{SCR}})$ (en anglais SST, SSE, SSR), autour de la moyenne de $\mathbf{{y}}$, en floats de Python ; une `ValueError` si les longueurs diffèrent ou sont nulles.

Avec $\mathbf{{X}}$ = `{X27}` (une droite sur les abscisses 0 à 3) et $\mathbf{{y}}$ = `{Y27}`, la vérification calcule :
- a) la diagonale de `hat_matrix(X)`, les leviers (une liste, 6 décimales) ;
- b) la trace de `hat_matrix(X)` (6 décimales) ;
- c) $\hat{{\mathbf{{y}}}} = \mathbf{{H}}\mathbf{{y}}$ (une liste, 6 décimales) ;
- d) `residual_decomposition(y, H @ y)` (une liste de 3 nombres, 6 décimales) ;
- e) le $R^2$ qu'on en déduit (4 décimales) ;
- f) le nom de l'erreur levée par `residual_decomposition([1, 2], [1, 2, 3])` ;
- g) le nom du type du premier nombre rendu par `residual_decomposition`, en texte ;
- h) le nom de l'erreur levée par `hat_matrix({S26})`.

Dans ta copie : pourquoi les leviers des deux points extrêmes sont-ils les plus grands ? Vérifie que $\mathrm{{SCT}} = \mathrm{{SCE}} + \mathrm{{SCR}}$ en d) : pourquoi est-ce garanti ici ?""",
    todo=LOAD_LEARNER,
    check=f'''X_27, y_27 = np.array({X27}, dtype=float), np.array({Y27}, dtype=float)
with checked("M09b.27a"):
    wbm.check("M09b.27a", np.diag(np.asarray(mymath.linreg.hat_matrix(X_27))).tolist(), computed=True)
with checked("M09b.27b"):
    wbm.check("M09b.27b", float(np.trace(np.asarray(mymath.linreg.hat_matrix(X_27)))), computed=True)
with checked("M09b.27c"):
    wbm.check("M09b.27c", (np.asarray(mymath.linreg.hat_matrix(X_27)) @ y_27).tolist(), computed=True)
with checked("M09b.27d"):
    sums_27 = mymath.linreg.residual_decomposition(y_27, np.asarray(mymath.linreg.hat_matrix(X_27)) @ y_27)
    wbm.check("M09b.27d", [float(s) for s in sums_27], computed=True)
with checked("M09b.27e"):
    sst_27, _, ssr_27 = mymath.linreg.residual_decomposition(y_27, np.asarray(mymath.linreg.hat_matrix(X_27)) @ y_27)
    wbm.check("M09b.27e", 1 - ssr_27 / sst_27, computed=True)
with checked("M09b.27f"):
    wbm.check("M09b.27f", raised(mymath.linreg.residual_decomposition, [1, 2], [1, 2, 3]), computed=True)
with checked("M09b.27g"):
    wbm.check("M09b.27g", type(mymath.linreg.residual_decomposition([1, 3], [2, 2])[0]).__name__, computed=True)
with checked("M09b.27h"):
    wbm.check("M09b.27h", raised(mymath.linreg.hat_matrix, {S26}), computed=True)''',
    solution=LOAD_REF + f'''
hat_matrix, residual_decomposition = mymath.linreg.hat_matrix, mymath.linreg.residual_decomposition
X_27, y_27 = np.array({X27}, dtype=float), np.array({Y27}, dtype=float)
H_27 = hat_matrix(X_27)
print(H_27.round(4))
print("a)", np.diag(H_27).round(6), " b)", np.trace(H_27).round(6), " c)", (H_27 @ y_27).round(6))
sst_27, sse_27, ssr_27 = residual_decomposition(y_27, H_27 @ y_27)
print("d)", (sst_27, sse_27, ssr_27), " e)", round(1 - ssr_27 / sst_27, 4))
print("f)", raised(residual_decomposition, [1, 2], [1, 2, 3]),
      " g)", type(residual_decomposition([1, 3], [2, 2])[0]).__name__, " h)", raised(hat_matrix, {S26}))''',
    record=f'''wbm.record("M09b.27a", [0.7, 0.3, 0.3, 0.7], decimals=6)
wbm.record("M09b.27b", 2.0, decimals=6,
           mistakes={{"la trace de H vaut le nombre de colonnes de X, pas de lignes": 4.0}})
wbm.record("M09b.27c", [-0.1, 1.3, 2.7, 4.1], decimals=6)
wbm.record("M09b.27d", [14.0, 9.8, 4.2], decimals=6,
           mistakes={{"l'ordre de la docstring : (SST, SSE, SSR), la somme expliquée avant la résiduelle":
                         [14.0, 4.2, 9.8],
                     "SST et SSE se calculent autour de la moyenne de y, pas autour de 0": [30.0, 25.8, 4.2]}})
wbm.record("M09b.27e", 0.7, decimals=4,
           mistakes={{"R² = 1 − SSR/SST : ce nombre est SSR/SST": 0.3,
                     "SST se calcule autour de la moyenne de y, pas autour de 0": 0.86}})
wbm.record("M09b.27f", "ValueError",
           mistakes={{"des longueurs différentes : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M09b.27g", "float",
           mistakes={{"la docstring demande des float de Python : float(...)": {{"float64", "ndarray", "int"}}}})
wbm.record("M09b.27h", "ValueError",
           mistakes={{"XᵀX est singulière : la docstring demande une ValueError": "aucune",
                     "{LINALG}": "LinAlgError",
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "LinAlgError")}}})''',
    after=tests_cells("test_hat_matrix_ or test_residual_decomposition_"),
    note=r"$\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 4 & 6 \\ 6 & 14 \end{pmatrix}$, et $h_{ij} = \frac{14 - 6x_i - "
         r"6x_j + 4x_ix_j}{20}$ : la diagonale vaut $(0{,}7 ;\ 0{,}3 ;\ 0{,}3 ;\ 0{,}7)$. Les deux points extrêmes, loin "
         r"de la moyenne des abscisses, pèsent le plus sur leur propre prédiction : déplacer un point du bord fait pivoter "
         r"la droite autour du centre. La trace vaut 2, le nombre de colonnes. La droite ajustée est $\hat{y} = -0{,}1 + "
         r"1{,}4x$ ; $\mathrm{SCT} = 14 = 9{,}8 + 4{,}2$, garanti par la colonne de 1 (fiche §3), et $R^2 = 0{,}7$.",
)

M09B_28 = Ex(
    "M09b.28", "🔨", 1, 15, "Compter les monômes, et la loss de Huber · `count_monomials, huber_loss`",
    "programmer le nombre de colonnes des features polynomiales et la loss de Huber moyenne.", "fiche §1 et §4",
    tracks="C", mymath="linreg.py",
    body=r"""Écris (fiche §1 et §4), en suivant les docstrings :
- `count_monomials(p, degree, include_constant=False)` : le nombre de monômes de degré au plus `degree` en `p` variables, $\binom{p + d}{d}$, moins 1 sans la constante, en `int` de Python (`math.comb` est permis) ; une `ValueError` si $p < 1$ ou si le degré est négatif ;
- `huber_loss(residuals, delta=1.0)` : la moyenne des $\ell_\delta(r_i)$ (fiche §1), en float de Python (`np.where` évite une boucle) ; une `ValueError` si la liste est vide ou si $\delta \le 0$.

La vérification calcule :
- a) `count_monomials(6, 3)` ;
- b) `count_monomials(6, 3, include_constant=True)` ;
- c) `count_monomials(2, 0)` ;
- d) `count_monomials(30, 4)` ;
- e) `huber_loss([1.5, -0.2, 3.0, -4.0], delta=2.0)` (6 décimales) ;
- f) `huber_loss([0.3, -0.1])` (6 décimales) ;
- g) le nom de l'erreur levée par `huber_loss([1.0], delta=0)` ;
- h) le nom du type de la valeur rendue par `count_monomials(3, 2)`, en texte.

Dans ta copie : calcule e) à la main, résidu par résidu. Que vaut c), et pourquoi ? Combien de colonnes ont les features polynomiales de degré 4 de 30 variables, et combien de nombres $\mathbf{X}^\top\mathbf{X}$ ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M09b.28a"):
    wbm.check("M09b.28a", mymath.linreg.count_monomials(6, 3), computed=True)
with checked("M09b.28b"):
    wbm.check("M09b.28b", mymath.linreg.count_monomials(6, 3, include_constant=True), computed=True)
with checked("M09b.28c"):
    wbm.check("M09b.28c", mymath.linreg.count_monomials(2, 0), computed=True)
with checked("M09b.28d"):
    wbm.check("M09b.28d", mymath.linreg.count_monomials(30, 4), computed=True)
with checked("M09b.28e"):
    wbm.check("M09b.28e", mymath.linreg.huber_loss([1.5, -0.2, 3.0, -4.0], delta=2.0), computed=True)
with checked("M09b.28f"):
    wbm.check("M09b.28f", mymath.linreg.huber_loss([0.3, -0.1]), computed=True)
with checked("M09b.28g"):
    wbm.check("M09b.28g", raised(mymath.linreg.huber_loss, [1.0], delta=0), computed=True)
with checked("M09b.28h"):
    wbm.check("M09b.28h", type(mymath.linreg.count_monomials(3, 2)).__name__, computed=True)''',
    solution=LOAD_REF + '''
count_monomials, huber_loss = mymath.linreg.count_monomials, mymath.linreg.huber_loss
print("a)", count_monomials(6, 3), " b)", count_monomials(6, 3, include_constant=True), " c)", count_monomials(2, 0),
      " d)", count_monomials(30, 4))
print("e)", huber_loss([1.5, -0.2, 3.0, -4.0], delta=2.0), " f)", huber_loss([0.3, -0.1]),
      " g)", raised(huber_loss, [1.0], delta=0), " h)", type(count_monomials(3, 2)).__name__)''',
    record=f'''wbm.record("M09b.28a", 83, mistakes={{"sans la constante par défaut : retire le monôme 1": 84}})
wbm.record("M09b.28b", 84, mistakes={{"include_constant=True : garde le monôme 1": 83}})
wbm.record("M09b.28c", 0, mistakes={{"degré 0 sans la constante : il ne reste aucun monôme": 1}})
wbm.record("M09b.28d", 46375, mistakes={{"sans la constante par défaut : retire le monôme 1": 46376}})
wbm.record("M09b.28e", 2.78625, decimals=6,
           mistakes={{"au-dessus de δ, la loss vaut δ(|r| − δ/2), pas |r|": 2.13625,
                      "huber_loss rend la moyenne des losses, pas leur somme": 11.145}})
wbm.record("M09b.28f", 0.025, decimals=6,
           mistakes={{"sous δ, la loss vaut r²/2 : le facteur 1/2": 0.05}})
wbm.record("M09b.28g", "ValueError",
           mistakes={{"δ doit être strictement positif : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M09b.28h", "int",
           mistakes={{"la docstring demande un int de Python : int(...)": {{"int64", "float", "float64"}}}})''',
    after=tests_cells("test_count_monomials_ or test_huber_loss_"),
    note=r"a) $\binom{9}{3} - 1 = 83$. c) Le seul monôme de degré au plus 0 est la constante : sans elle, il n'en reste "
         r"aucun. d) $\binom{34}{4} - 1 = 46\,375$ colonnes, donc environ $2{,}2 \times 10^9$ nombres dans "
         r"$\mathbf{X}^\top\mathbf{X}$ (17 Go en `float64`). e) $1{,}5 \le 2$ donne $1{,}125$ ; $0{,}2$ donne $0{,}02$ ; $3$ "
         r"donne $2 \times (3 - 1) = 4$ ; $4$ donne $6$ : la moyenne vaut $\frac{11{,}145}{4} = 2{,}78625$.",
)

GIVEN_29 = '''rng_29 = np.random.default_rng(29)
x1_29, x2_29 = rng_29.uniform(0, 10, size=(2, 30))
y_29 = 2 + 0.5 * x1_29 - 1.2 * x2_29 + rng_29.normal(0, 1, 30)
X_29 = np.column_stack([x1_29, x2_29])                   # 30 examples, 2 features (no column of ones)
X1_29 = np.column_stack([np.ones(30), X_29])              # the same, with a column of ones first
print(X_29.shape, X1_29.shape, y_29[:3].round(3))'''

M09B_29 = Ex(
    "M09b.29", "📦", 1, 15, "`np.linalg.lstsq` et scikit-learn contre tes équations normales",
    "faire la même régression avec `np.linalg.lstsq` et scikit-learn, lire ce que rend chaque fonction, et voir comment "
    "scikit-learn traite l'ordonnée à l'origine de ridge.", "fiche §3 et §5 ; Ex M09b.26", tracks="C, E",
    body=r"""En pratique, on ne résout pas les équations normales à la main :
- `np.linalg.lstsq(X, y, rcond=None)` rend un quadruplet : la solution des moindres carrés, la somme des carrés des résidus, le **rang** de $\mathbf{X}$ et ses valeurs singulières (M12d) ; il ne forme jamais $\mathbf{X}^\top\mathbf{X}$ ;
- `sklearn.linear_model.LinearRegression()` ajoute lui-même l'ordonnée à l'origine (`fit_intercept=True` par défaut) : après `.fit(X, y)`, elle est dans `intercept_` et les autres poids dans `coef_` ;
- `sklearn.linear_model.Ridge(alpha=...)` minimise $\lVert \mathbf{y} - \mathbf{X}\mathbf{w} - b \rVert^2 + \alpha\lVert \mathbf{w} \rVert^2$ : l'ordonnée à l'origine $b$ n'est **pas** pénalisée.

La cellule fournie tire un dataset de 30 exemples à 2 features, `X_29` (sans colonne de 1) et `X1_29` (avec une colonne de 1 en premier), et les cibles `y_29`. Calcule :
- a) la solution de `np.linalg.lstsq(X1_29, y_29, rcond=None)` (une liste de 3 nombres, 4 décimales) ;
- b) `[intercept_, coef_[0], coef_[1]]` de `LinearRegression().fit(X_29, y_29)` (4 décimales) ;
- c) le rang que rend `np.linalg.lstsq` (un entier) ;
- d) `[intercept_, coef_[0], coef_[1]]` de `Ridge(alpha=5).fit(X_29, y_29)` (4 décimales) ;
- e) `mymath.linreg.solve_least_squares(X1_29, y_29, ridge=5)` (une liste, 4 décimales) ;
- f) vrai ou faux : l'ordonnée à l'origine de e) est plus proche de 0 que celle de d) (calcule-le à partir de tes réponses).

Dans ta copie : pourquoi a) et b) sont-ils égaux ? Pourquoi d) et e) diffèrent-ils, surtout sur l'ordonnée à l'origine, et pourquoi les deux autres poids changent-ils aussi ? Pourquoi `lstsq` est-il préférable aux équations normales quand des colonnes sont presque dépendantes ?""",
    given=GIVEN_29,
    todo='''from sklearn.linear_model import LinearRegression, Ridge

answer_M09b_29a = ...  # a) a list of 3 numbers (4 decimals)
answer_M09b_29b = ...  # b) a list of 3 numbers (4 decimals)
answer_M09b_29c = ...  # c) an integer
answer_M09b_29d = ...  # d) a list of 3 numbers (4 decimals)
answer_M09b_29e = ...  # e) a list of 3 numbers (4 decimals)
answer_M09b_29f = ...  # f) True or False, computed from d) and e)''',
    check='''for letter, answer in zip("abcdef", [answer_M09b_29a, answer_M09b_29b, answer_M09b_29c, answer_M09b_29d,
                                     answer_M09b_29e, answer_M09b_29f]):
    wbm.check(f"M09b.29{letter}", answer)''',
    solution='''from sklearn.linear_model import LinearRegression, Ridge

ref_29 = wbm.load_mymath("ref")
w_29, _, rank_29, _ = np.linalg.lstsq(X1_29, y_29, rcond=None)
answer_M09b_29a = w_29.tolist()
lr_29 = LinearRegression().fit(X_29, y_29)
answer_M09b_29b = [float(lr_29.intercept_), *lr_29.coef_.tolist()]
answer_M09b_29c = int(rank_29)
ridge_29 = Ridge(alpha=5).fit(X_29, y_29)
answer_M09b_29d = [float(ridge_29.intercept_), *ridge_29.coef_.tolist()]
answer_M09b_29e = ref_29.linreg.solve_least_squares(X1_29, y_29, ridge=5).tolist()
answer_M09b_29f = bool(abs(answer_M09b_29e[0]) < abs(answer_M09b_29d[0]))
print(np.round(answer_M09b_29a, 4), np.round(answer_M09b_29b, 4), answer_M09b_29c)
print(np.round(answer_M09b_29d, 4), np.round(answer_M09b_29e, 4), answer_M09b_29f)''',
    record='''wbm.record("M09b.29a", answer_M09b_29a, decimals=4)
wbm.record("M09b.29b", answer_M09b_29b, decimals=4,
           mistakes={"l'ordre de l'énoncé : intercept_ d'abord, puis les deux nombres de coef_":
                         [*answer_M09b_29b[1:], answer_M09b_29b[0]]})
wbm.record("M09b.29c", 3, mistakes={"le rang de X1_29, avec sa colonne de 1 : trois colonnes indépendantes": 2})
wbm.record("M09b.29d", answer_M09b_29d, decimals=4,
           mistakes={"Ridge ne pénalise pas l'ordonnée à l'origine : c'est le résultat de ta fonction, qui la pénalise":
                         answer_M09b_29e,
                     "l'ordre de l'énoncé : intercept_ d'abord, puis les deux nombres de coef_":
                         [*answer_M09b_29d[1:], answer_M09b_29d[0]]})
wbm.record("M09b.29e", answer_M09b_29e, decimals=4,
           mistakes={"solve_least_squares pénalise tous les poids, celui de la colonne de 1 compris : ce n'est pas le "
                     "résultat de scikit-learn": answer_M09b_29d})
wbm.record("M09b.29f", True,
           mistakes={"compare les valeurs absolues des premiers nombres de d) et de e) : lequel des deux calculs pénalise "
                     "l'ordonnée à l'origine ?": False})''',
    note=r"a) et b) La même solution des moindres carrés, à l'arrondi près : `LinearRegression` ajoute la colonne de 1 "
         r"lui-même (et centre les données pour la calculer). c) Le rang 3 dit que la solution est unique. d) et e) "
         r"`Ridge` ne pénalise pas l'ordonnée à l'origine ; `solve_least_squares` la rétrécit vers 0, et les autres poids "
         r"compensent : les deux résultats diffèrent nettement. f) L'ordonnée à l'origine passe de 3,05 (scikit-learn) à "
         r"1,59 (ta fonction) : pénalisée, elle est tirée vers 0, et la droite ne passe plus par le point moyen ; les pentes "
         r"bougent pour rattraper une partie de l'écart. workbookIA 9 montre comment s'en passer. `lstsq` passe par une "
         r"factorisation de $\mathbf{X}$ (la SVD, M12d), sans former $\mathbf{X}^\top\mathbf{X}$ : il évite de perdre "
         r"deux fois plus de chiffres significatifs qu'avec $\mathbf{X}$ seule (M09b.32).",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, two experiments, a figure (M09b.30 to M09b.33)
# ---------------------------------------------------------------------------
M09B_30_EXPERIMENT = '''rng_30 = np.random.default_rng(30)
x_train_30 = rng_30.uniform(0, 1, 20)
y_train_30 = 1 + 2 * x_train_30 + rng_30.normal(0, 0.5, 20)
x_test_30 = rng_30.uniform(0, 1, 1000)
y_test_30 = 1 + 2 * x_test_30 + rng_30.normal(0, 0.5, 1000)
noise_train_30, noise_test_30 = rng_30.normal(size=(20, 18)), rng_30.normal(size=(1000, 18))
print(" k | R² train | R² test")
for k in range(19):
    X_train = np.column_stack([np.ones(20), x_train_30, noise_train_30[:, :k]])
    X_test = np.column_stack([np.ones(1000), x_test_30, noise_test_30[:, :k]])
    w = np.linalg.lstsq(X_train, y_train_30, rcond=None)[0]
    print(f"{k:2d} | {r2_score_np(y_train_30, X_train @ w):8.4f} | {r2_score_np(y_test_30, X_test @ w):7.4f}")'''

M09B_30 = Ex(
    "M09b.30", "🔮", 1, 10, "Prédire : le R² d'entraînement quand on ajoute une feature de pur bruit",
    "prévoir l'effet de features sans aucun lien avec la cible sur le $R^2$ d'entraînement et sur celui de nouvelles "
    "données, puis le vérifier.", "fiche §1, §3 et §8", tracks="C, E", hypothesis=True,
    body=r"""On ajuste par moindres carrés une droite ($\hat{y} = w_0 + w_1x$) à 20 exemples bruités, puis on ajoute à $\mathbf{X}$, une à une, des colonnes de **pur bruit** : des nombres tirés au hasard, sans aucun lien avec la cible. On mesure le $R^2$ sur les 20 exemples d'entraînement, et sur 1 000 nouveaux exemples tirés de la même façon. Choisis, pour chaque question, le numéro de la bonne réponse :
- a) chaque fois qu'on ajoute une colonne de bruit, le $R^2$ d'**entraînement** : (1) baisse ; (2) monte ou reste égal, jamais ne baisse ; (3) ne change pas ; (4) monte ou baisse selon le tirage ;
- b) combien de colonnes de bruit faut-il ajouter pour un $R^2$ d'entraînement exactement égal à 1 : (1) 2 ; (2) 10 ; (3) 18 ; (4) aucun nombre n'y suffit ;
- c) avec 18 colonnes de bruit, le $R^2$ sur les **nouvelles** données, comparé à celui de la droite seule : (1) plus grand ; (2) à peu près égal ; (3) nettement plus petit.

**Avant d'exécuter quoi que ce soit**, écris tes trois prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M09b_30a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M09b_30b = ...  # b) 1, 2, 3 or 4
prediction_M09b_30c = ...  # c) 1, 2 or 3''',
    check='''for letter, prediction in zip("abc", [prediction_M09b_30a, prediction_M09b_30b, prediction_M09b_30c]):
    wbm.check(f"M09b.30{letter}", prediction)''',
    record='''wbm.record("M09b.30a", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M09b.30b", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M09b.30c", 3, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes trois prédictions écrites."),
        ("todo", guarded(M09B_30_EXPERIMENT, [f"prediction_M09b_30{letter}" for letter in "abc"],
                         "⏳ Écris d'abord tes trois prédictions, puis exécute à nouveau.")),
        ("solution", M09B_30_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : pourquoi le $R^2$ d'entraînement ne peut-il jamais baisser quand "
               "on ajoute une colonne (pense à ce que peut faire le poids de la nouvelle colonne) ? Que se passe-t-il pour "
               "$k = 18$ : combien de colonnes, combien d'exemples, combien de solutions a $\\mathbf{X}\\mathbf{w} = "
               "\\mathbf{y}$ ? Pourquoi le $R^2$ de test, lui, baisse-t-il ? Quel terme de la fiche §8 grandit ?"),
    ],
    note=r"a) Ajouter une colonne ne retire aucun modèle possible : il suffit de donner le poids 0 à la nouvelle colonne "
         r"pour retrouver l'ancien ajustement ; le minimum de la somme des carrés ne peut donc que baisser ou rester égal, et "
         r"le $R^2$ d'entraînement monter. b) Avec 18 colonnes de bruit, $\mathbf{X}$ a 20 colonnes pour 20 exemples : "
         r"carrée, et inversible pour un tirage au hasard ; $\mathbf{X}\mathbf{w} = \mathbf{y}$ a alors une solution "
         r"exacte, les résidus sont nuls et $R^2 = 1$. c) Le modèle a appris le bruit des 20 exemples (des poids non nuls "
         r"pour des colonnes sans lien avec la cible) : sur de nouvelles données, ces poids ne font qu'ajouter des "
         r"erreurs, et le $R^2$ de test devient négatif. C'est la variance de la fiche §8. Un $R^2$ d'entraînement ne "
         r"suffit jamais à comparer des modèles qui n'ont pas le même nombre de colonnes.",
)

M09B_31 = Ex(
    "M09b.31", "🔬", 2, 20, "Simuler l'estimateur rétréci c·x̄ : le c qui minimise l'erreur quadratique",
    "mesurer par simulation l'erreur quadratique d'un estimateur rétréci pour toute une grille de facteurs, et la "
    "comparer à la formule biais² + variance.", "fiche §8 ; Ex M09b.12", tracks="C",
    body=r"""On observe $n = 5$ valeurs d'une loi normale de moyenne $\mu = 1$ et d'écart-type $\sigma = 3$, et l'on estime $\mu$ par $c\,\bar{x}$. La fiche (§8) et M09b.12 donnent l'erreur quadratique moyenne $E(c) = (c - 1)^2\mu^2 + c^2\frac{\sigma^2}{n}$. On la mesure ici par simulation. Écris :
- `simulated_mse(cs, mu, sigma, n, reps=200_000, seed=31)` : avec `rng = np.random.default_rng(seed)`, tire **une fois** un tableau d'échantillons `rng.normal(mu, sigma, size=(reps, n))`, calcule les `reps` moyennes $\bar{x}$ (une par ligne), puis rends, pour chaque $c$ de `cs`, la moyenne des $(c\,\bar{x} - \mu)^2$ (un tableau NumPy, un nombre par $c$) ;
- `formula_mse(c, mu, sigma, n)` : $E(c)$ par la formule.

La vérification calcule, avec la grille `cs = np.linspace(0, 1, 101)` :
- a) le $c$ de la grille où ta simulation est la plus petite, comparé au $c^*$ de la formule : vrai ou faux, ils diffèrent de moins de 0,02 ;
- b) vrai ou faux : sur toute la grille, ta simulation et ta formule diffèrent de moins de 0,02 (mais pas de 0 : une simulation n'est jamais exactement la formule) ;
- c) le $c^*$ exact de la formule, $\frac{\mu^2}{\mu^2 + \sigma^2/n}$ (4 décimales) ;
- d) le rapport $\frac{E(1)}{E(c^*)}$ (2 décimales).

Une cellule trace ensuite les deux courbes.

Dans ta copie : quel est le gain d'erreur quadratique de $c^*\bar{x}$ par rapport à $\bar{x}$ ? Pourquoi un $c$ plus petit que 1 aide-t-il surtout quand $\sigma^2/n$ est grand devant $\mu^2$ ? Quel est le lien avec ridge ?""",
    todo='''def simulated_mse(cs, mu, sigma, n, reps=200_000, seed=31):
    """The simulated mean squared error of c * x̄ as an estimator of mu, for each c of cs (one draw of samples)."""
    raise NotImplementedError("les échantillons une seule fois, les moyennes par ligne, puis une erreur par c")


def formula_mse(c, mu, sigma, n):
    """The mean squared error (c - 1)² mu² + c² sigma² / n of c * x̄."""
    raise NotImplementedError("biais² + variance")


answer_M09b_31c = ...  # c) the exact c* of the formula (4 decimals)
answer_M09b_31d = ...  # d) E(1) / E(c*) (2 decimals)''',
    check='''CS_31 = np.linspace(0, 1, 101)
with checked("M09b.31a"):
    sim_31 = np.asarray(simulated_mse(CS_31, 1.0, 3.0, 5), dtype=float)
    c_star_31 = 1.0 / (1.0 + 9.0 / 5)
    wbm.check("M09b.31a", bool(sim_31.shape == CS_31.shape and abs(CS_31[np.argmin(sim_31)] - c_star_31) < 0.02),
              computed=True)
with checked("M09b.31b"):
    formula_31 = np.array([formula_mse(c, 1.0, 3.0, 5) for c in CS_31], dtype=float)
    sim_31 = np.asarray(simulated_mse(CS_31, 1.0, 3.0, 5), dtype=float)
    wbm.check("M09b.31b", bool(sim_31.shape == CS_31.shape and 0 < np.max(np.abs(sim_31 - formula_31)) < 0.02),
              computed=True)
wbm.check("M09b.31c", answer_M09b_31c)
wbm.check("M09b.31d", answer_M09b_31d)''',
    solution='''def simulated_mse(cs, mu, sigma, n, reps=200_000, seed=31):
    """The simulated mean squared error of c * x̄ as an estimator of mu, for each c of cs (one draw of samples)."""
    rng = np.random.default_rng(seed)
    means = rng.normal(mu, sigma, size=(reps, n)).mean(axis=1)
    return np.array([np.mean((c * means - mu) ** 2) for c in cs])


def formula_mse(c, mu, sigma, n):
    """The mean squared error (c - 1)² mu² + c² sigma² / n of c * x̄."""
    return (c - 1) ** 2 * mu ** 2 + c ** 2 * sigma ** 2 / n


CS_31 = np.linspace(0, 1, 101)
sim_31 = simulated_mse(CS_31, 1.0, 3.0, 5)
formula_31 = np.array([formula_mse(c, 1.0, 3.0, 5) for c in CS_31])
c_star_31 = 1.0 / (1.0 + 9.0 / 5)
print("best c of the simulation:", CS_31[np.argmin(sim_31)], "· c* =", round(c_star_31, 4),
      "· largest gap:", round(float(np.max(np.abs(sim_31 - formula_31))), 4))
answer_M09b_31c = c_star_31
answer_M09b_31d = formula_mse(1.0, 1.0, 3.0, 5) / formula_mse(c_star_31, 1.0, 3.0, 5)
print(round(answer_M09b_31c, 4), round(answer_M09b_31d, 2))''',
    record='''wbm.record("M09b.31a", True,
           mistakes={"le meilleur c de ta simulation est loin de c* : tire les échantillons une seule fois (forme "
                     "(reps, n)), moyenne par ligne, puis une erreur par c": False})
wbm.record("M09b.31b", True,
           mistakes={"ta simulation et ta formule doivent être proches (à 0,02 près) sans être identiques : vérifie "
                     "(c x̄ − μ)² dans la simulation, tirée au hasard, et (c − 1)² μ² + c² σ²/n dans la formule": False})
wbm.record("M09b.31c", 5 / 14, decimals=4,
           mistakes={"c* = μ²/(μ² + σ²/n) : σ est l'écart-type, σ² = 9": 1 / (1 + 3 / 5)})
wbm.record("M09b.31d", 2.8, decimals=2,
           mistakes={"le rapport E(1)/E(c*), dans cet ordre : plus grand que 1": 1 / 2.8})''',
    after=[("md", "**La figure** (elle utilise tes deux fonctions)."),
           ("code", '''with checked("M09b.31 figure"):
    sim_fig_31 = np.asarray(simulated_mse(CS_31, 1.0, 3.0, 5), dtype=float)
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(CS_31, sim_fig_31, lw=3, alpha=0.6, label="simulation (200 000 échantillons)")
    ax.plot(CS_31, [formula_mse(c, 1.0, 3.0, 5) for c in CS_31], "k--", label="formule biais² + variance")
    ax.axvline(1.0 / (1.0 + 9.0 / 5), color="gray", lw=0.8)
    ax.set(xlabel="c", ylabel="erreur quadratique moyenne de c x̄", title="μ = 1, σ = 3, n = 5")
    ax.legend()
    plt.show()''')],
    note=r"$E(c)$ est un polynôme du second degré en $c$ : $E'(c) = 2(c - 1)\mu^2 + 2c\frac{\sigma^2}{n} = 0$ donne $c^* = "
         r"\frac{\mu^2}{\mu^2 + \sigma^2/n} = \frac{1}{2{,}8} \approx 0{,}3571$, et $E(c^*) = c^*\frac{\sigma^2}{n} \approx "
         r"0{,}643$, contre $E(1) = 1{,}8$ : 2,8 fois moins. Le rétrécissement paie quand la variance $\sigma^2/n$ de "
         r"$\bar{x}$ est grande devant le carré du signal $\mu^2$ : on accepte un biais pour couper la variance. C'est ce "
         r"que fait ridge sur les poids. Mais $c^*$ dépend de $\mu$, inconnu : en pratique on règle la force du "
         r"rétrécissement par validation (comme le $\lambda$ de ridge, workbookIA 9).",
)

GIVEN_32 = '''x_32 = np.linspace(0, 20, 50)                  # 50 abscissas between 0 and 20
t_32 = (x_32 - 10) / 10                           # the same, scaled to [-1, 1]'''

M09B_32_EXPERIMENT = '''rng_32 = np.random.default_rng(32)
V6 = np.column_stack([x_32 ** k for k in range(7)])            # degree 6, raw powers
T6 = np.column_stack([t_32 ** k for k in range(7)])            # degree 6, scaled abscissas
target = np.sin(x_32 / 4)
nudged = target + 1e-8 * rng_32.normal(size=x_32.size)         # a change of 1e-8 in the data
for name, D in (("raw", V6), ("scaled", T6)):
    w0 = np.linalg.solve(D.T @ D, D.T @ target)
    w1 = np.linalg.solve(D.T @ D, D.T @ nudged)
    print(f"{name:6s} · largest relative change of a weight: {np.max(np.abs(w1 - w0) / np.abs(w0)):.1e}"
          f" · largest change of a prediction: {np.max(np.abs(D @ (w1 - w0))):.1e}")'''

M09B_32 = Ex(
    "M09b.32", "🔬", 2, 20, "Le conditionnement de XᵀX avec des puissances non standardisées",
    "mesurer le conditionnement de $\\mathbf{X}^\\top\\mathbf{X}$ pour des features polynomiales, avec et sans mise à "
    "l'échelle de l'abscisse, et voir ce qu'il fait aux poids.", "fiche §4 ; Ex M09b.26", tracks="C",
    body=r"""Le **conditionnement** d'une matrice carrée, `np.linalg.cond(A)`, dit à peu près par combien une petite erreur relative sur les données peut être multipliée dans la solution de $\mathbf{A}\mathbf{x} = \mathbf{b}$ (M12d en donnera la définition). Un `float64` a environ 16 chiffres significatifs : un conditionnement de $10^{16}$ peut tous les perdre. La cellule fournie définit 50 abscisses `x_32` entre 0 et 20, et les mêmes ramenées à $[-1, 1]$, `t_32`. Écris :
- `powers(x, degree)` : la matrice des colonnes $1, x, x^2, \ldots, x^{d}$ (forme $(n, d + 1)$) ;
- `cond_xtx(x, degree)` : le conditionnement de $\mathbf{X}^\top\mathbf{X}$ pour $\mathbf{X}$ = `powers(x, degree)`.

La vérification calcule :
- a) l'ordre de grandeur du conditionnement pour `x_32` et le degré 5 : la vérification compare l'exposant, `round(math.log10(...))` ;
- b) le même pour `t_32` et le degré 5 ;
- c) le plus petit degré de 1 à 8 pour lequel le conditionnement dépasse $10^{15}$ avec `x_32` ;
- d) vrai ou faux : avec `t_32`, il reste sous $10^6$ pour tous les degrés de 1 à 8.

Une dernière cellule modifie les cibles de $10^{-8}$ et compare la variation des poids et celle des prédictions, pour le degré 6.

Dans ta copie : pourquoi les colonnes $x^4$ et $x^5$ sur $[0, 20]$ sont-elles presque proportionnelles (fiche §4) ? Pourquoi les poids bougent-ils beaucoup, et les prédictions presque pas ? Quand cela devient-il grave ?""",
    given=GIVEN_32,
    todo='''def powers(x, degree):
    """The matrix whose columns are 1, x, x², ..., x**degree (shape (n, degree + 1))."""
    raise NotImplementedError("une colonne par puissance, de 0 à degree")


def cond_xtx(x, degree):
    """The condition number of XᵀX for X = powers(x, degree)."""
    raise NotImplementedError("le conditionnement de XᵀX, par une fonction de np.linalg")''',
    check='''with checked("M09b.32a"):
    if np.shape(powers(x_32, 5)) != (50, 6):
        print(f"❌ Ex M09b.32 : powers(x_32, 5) a la forme {np.shape(powers(x_32, 5))}, pas (50, 6) : une colonne par "
              "puissance, de x⁰ = 1 à x⁵.")
    wbm.check("M09b.32a", round(math.log10(max(cond_xtx(x_32, 5), 1e-300))), computed=True)
with checked("M09b.32b"):
    wbm.check("M09b.32b", round(math.log10(max(cond_xtx(t_32, 5), 1e-300))), computed=True)
with checked("M09b.32c"):
    wbm.check("M09b.32c", next((d for d in range(1, 9) if cond_xtx(x_32, d) > 1e15), 0), computed=True)
with checked("M09b.32d"):
    wbm.check("M09b.32d", bool(all(cond_xtx(t_32, d) < 1e6 for d in range(1, 9))), computed=True)''',
    solution='''def powers(x, degree):
    """The matrix whose columns are 1, x, x², ..., x**degree (shape (n, degree + 1))."""
    x = np.asarray(x, dtype=float)
    return np.column_stack([x ** k for k in range(degree + 1)])


def cond_xtx(x, degree):
    """The condition number of XᵀX for X = powers(x, degree)."""
    X = powers(x, degree)
    return float(np.linalg.cond(X.T @ X))


for d in range(1, 9):
    print(f"degree {d}: raw {cond_xtx(x_32, d):.1e} · scaled {cond_xtx(t_32, d):.1e}")''',
    record='''wbm.record("M09b.32a", 14,
           mistakes={"le conditionnement de XᵀX, pas celui de X (il en est à peu près le carré)": 7,
                     "powers(x, d) a d + 1 colonnes, de x⁰ à x^d : le degré 5 va jusqu'à x⁵": 11})
wbm.record("M09b.32b", 3, mistakes={"le conditionnement de XᵀX, pas celui de X": 2})
wbm.record("M09b.32c", 6, mistakes={"le premier degré où le conditionnement dépasse 1e15 = 10¹⁵": {5, 7}})
wbm.record("M09b.32d", True,
           mistakes={"avec t_32 (entre −1 et 1), les puissances restent du même ordre de grandeur : vérifie powers et "
                     "cond_xtx": False})''',
    after=[("md", "**Ce que cela fait aux poids** (une expérience fournie, avec NumPy)."),
           ("code", M09B_32_EXPERIMENT)],
    note=r"Sur $[0, 20]$, $x^5$ va jusqu'à $3{,}2 \times 10^6$ et la colonne de 1 reste à 1 ; surtout, les colonnes "
         r"$x^4$ et $x^5$ pointent presque dans la même direction (fiche §4) : $\mathbf{X}^\top\mathbf{X}$ est presque "
         r"singulière, avec un conditionnement de l'ordre de $10^{14}$ au degré 5 et de $10^{17}$ au degré 6. Ramener "
         r"l'abscisse à $[-1, 1]$ le fait tomber à $10^3$ : c'est le rôle de la standardisation. Les poids bougent "
         r"beaucoup, car beaucoup de combinaisons de colonnes presque dépendantes donnent presque les mêmes prédictions ; "
         r"les prédictions, elles, restent stables. C'est grave quand on lit les poids (pour interpréter un modèle), quand "
         r"on extrapole hors des données, ou quand le conditionnement atteint $10^{16}$ : `solve` peut alors rendre "
         r"n'importe quoi. `lstsq` (sans former $\mathbf{X}^\top\mathbf{X}$) ne subit que la racine de ce conditionnement.",
)

DATA_33 = '''x_33 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y_33 = np.array([1.5, 2.0, 3.5, 3.0, 5.0])
X_33 = np.column_stack([np.ones(5), x_33])               # w = (w0, w1): ordinate at the origin, slope
Xc_33 = np.column_stack([np.ones(5), x_33 - x_33.mean()])  # the same with a centered abscissa'''

M09B_33_CHECK = '''with checked("M09b.33 vérifications"):
    import matplotlib.contour as mcontour
    import matplotlib.quiver as mquiver
    problems = []
    X_t = np.array([[1.0, -1.0], [1.0, 0.5], [1.0, 2.0], [1.0, 3.0]])    # another dataset
    y_t = np.array([0.0, 2.0, 1.0, 4.0])
    w_t = np.linalg.solve(X_t.T @ X_t, X_t.T @ y_t)
    fig_t, ax_t = plt.subplots()
    try:
        created = drawn(draw_loss, ax_t, X_t, y_t, (w_t[0] - 2, w_t[0] + 2), (w_t[1] - 1, w_t[1] + 1))
    finally:
        plt.close(fig_t)
    if created:
        problems.append("draw_loss ouvre sa propre figure : dessine dans l'axe reçu")
    else:
        contours = [c for c in ax_t.collections if isinstance(c, mcontour.ContourSet)]
        quivers = [c for c in ax_t.collections if isinstance(c, mquiver.Quiver)]
        points = [line for line in ax_t.get_lines() if len(line.get_xdata()) == 1]
        if not contours or len(contours[0].levels) < 8:
            problems.append("trace au moins 8 lignes de niveau de la loss (ax.contour)")
        if not any(np.allclose([line.get_xdata()[0], line.get_ydata()[0]], w_t, atol=1e-6) for line in points):
            problems.append("marque le minimum par un seul point (ax.plot(w0, w1, marker)), placé à la solution des "
                            "équations normales")
        if not quivers:
            problems.append("il manque les flèches de la descente (ax.quiver)")
        else:
            q = quivers[0]
            xy = np.asarray(q.get_offsets(), dtype=float)
            u, v = np.ravel(q.U), np.ravel(q.V)
            grads = np.array([-2 * X_t.T @ (y_t - X_t @ w) for w in xy])
            norms = np.hypot(grads[:, 0], grads[:, 1]) * np.hypot(u, v)
            keep = norms > 1e-12
            cosines = -(u * grads[:, 0] + v * grads[:, 1])[keep] / norms[keep]
            if xy.shape[0] < 16:
                problems.append("dessine au moins 16 flèches, sur une grille")
            elif cosines.size == 0 or np.min(cosines) < 0.999:
                problems.append("chaque flèche doit pointer dans la direction de descente, −∇L(w), en son point de "
                                "départ")
    if problems:
        print("❌ Ex M09b.33 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M09b.33 : lignes de niveau, minimum et flèches de descente justes.")'''

M09B_33 = Ex(
    "M09b.33", "🎨", 1, 20, "Les lignes de niveau de la loss des moindres carrés en dimension 2, et son gradient",
    "tracer la loss des moindres carrés comme une fonction des deux poids, avec son minimum et les directions de "
    "descente, et voir l'effet du centrage sur sa forme.", "fiche §2 et §3 ; M05b (lignes de niveau)", tracks="C",
    body=r"""Pour une droite $\hat{y} = w_0 + w_1x$, la loss $L(w_0, w_1) = \lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2$ est une fonction de **deux** variables : on peut tracer ses lignes de niveau dans le plan des poids. Écris `draw_loss(ax, X, y, w0_lim, w1_lim)`, qui dessine dans l'axe `ax`, sur le rectangle des poids $[w_0^{\min}, w_0^{\max}] \times [w_1^{\min}, w_1^{\max}]$ :
- au moins 8 lignes de niveau de $L$ (`ax.contour`, sur une grille fine faite par `np.meshgrid`) ; des niveaux en progression géométrique au-dessus du minimum, `L_min + np.geomspace(...)`, montrent mieux la forme ;
- le minimum, la solution des équations normales, par un seul point (`ax.plot(w0, w1, "*")`) ;
- les flèches de la **direction de descente** $-\nabla L(\mathbf{w}) = 2\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w})$ sur une grille grossière d'au moins 16 points (`ax.quiver`).

La cellule de la figure s'en sert deux fois sur les cinq points fournis : avec l'abscisse $x$ brute, puis centrée ($x - \bar{x}$). Une cellule de vérification essaie ta fonction sur un autre dataset.

Dans ta copie : pourquoi les lignes de niveau sont-elles des ellipses (pense au degré de $L$) ? Pourquoi sont-elles si allongées et penchées avec $x$ brut, et alignées sur les axes avec $x$ centré (calcule $\mathbf{X}^\top\mathbf{X}$ dans les deux cas) ? Les flèches pointent-elles vers le minimum ? Qu'en déduis-tu pour une descente de gradient sur des données non centrées ?""",
    given=DATA_33,
    todo='''def draw_loss(ax, X, y, w0_lim, w1_lim):
    """In ax: level lines of L(w) = ‖y - Xw‖² over the rectangle w0_lim × w1_lim, the minimum (one point), and the
    descent directions -∇L(w) on a coarse grid (quiver)."""
    raise NotImplementedError("une grille de poids, L sur la grille, ax.contour ; le minimum ; ax.quiver")''',
    check='''with checked("M09b.33 figure"):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))
    try:
        created = drawn(draw_loss, axes[0], X_33, y_33, (-2.5, 3.5), (0.0, 1.6))
        drawn(draw_loss, axes[1], Xc_33, y_33, (1.0, 5.0), (0.0, 1.6))
    except BaseException:
        plt.close(fig)
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M09b.33 : draw_loss ouvre sa propre figure : dessine dans l'axe reçu.")
    else:
        axes[0].set(title="x brut", xlabel="w0", ylabel="w1")
        axes[1].set(title="x centré", xlabel="w0", ylabel="w1")
        plt.show()''',
    solution='''def draw_loss(ax, X, y, w0_lim, w1_lim):
    """In ax: level lines of L(w) = ‖y - Xw‖² over the rectangle w0_lim × w1_lim, the minimum (one point), and the
    descent directions -∇L(w) on a coarse grid (quiver)."""
    X, y = np.asarray(X, dtype=float), np.asarray(y, dtype=float)
    W0, W1 = np.meshgrid(np.linspace(*w0_lim, 200), np.linspace(*w1_lim, 200))
    residuals = y[None, None, :] - (W0[..., None] * X[:, 0] + W1[..., None] * X[:, 1])
    L = np.sum(residuals ** 2, axis=-1)
    w_star = np.linalg.solve(X.T @ X, X.T @ y)
    L_min = float(np.sum((y - X @ w_star) ** 2))
    ax.contour(W0, W1, L, levels=L_min + np.geomspace(0.05, 50, 10), cmap="viridis")
    ax.plot(w_star[0], w_star[1], "*", color="crimson", markersize=14)
    G0, G1 = np.meshgrid(np.linspace(*w0_lim, 6), np.linspace(*w1_lim, 6))
    descent = np.array([2 * X.T @ (y - X @ np.array([a, b])) for a, b in zip(G0.ravel(), G1.ravel())])
    ax.quiver(G0.ravel(), G1.ravel(), descent[:, 0], descent[:, 1], color="gray", angles="xy")


fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))
draw_loss(axes[0], X_33, y_33, (-2.5, 3.5), (0.0, 1.6))
draw_loss(axes[1], Xc_33, y_33, (1.0, 5.0), (0.0, 1.6))
axes[0].set(title="x brut", xlabel="w0", ylabel="w1")
axes[1].set(title="x centré", xlabel="w0", ylabel="w1")
plt.show()
print("XᵀX raw:", (X_33.T @ X_33).tolist(), "· XᵀX centered:", (Xc_33.T @ Xc_33).tolist())''',
    after=[("md", "**Vérifications automatiques** (sur un autre dataset, dans des axes neufs)."),
           ("code", M09B_33_CHECK)],
    note=r"$L$ est un polynôme du second degré en $(w_0, w_1)$, de partie quadratique $\mathbf{w}^\top\mathbf{X}^\top"
         r"\mathbf{X}\mathbf{w}$ : ses lignes de niveau sont des ellipses centrées au minimum $(0{,}6 ;\ 0{,}8)$. Avec $x$ "
         r"brut, $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 5 & 15 \\ 15 & 55 \end{pmatrix}$ a un terme croisé : les "
         r"ellipses sont penchées, et très allongées (le rapport de leurs axes est d'environ 8). Avec $x$ centré, "
         r"$\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 5 & 0 \\ 0 & 10 \end{pmatrix}$ est diagonale : les axes des ellipses "
         r"sont ceux du repère, et le minimum devient $(3 ;\ 0{,}8)$ (la même pente). Les flèches sont perpendiculaires aux "
         r"lignes de niveau, pas dirigées vers le minimum : dans une vallée étroite, une descente de gradient zigzague "
         r"d'un bord à l'autre et avance lentement (M19). Centrer, et standardiser, arrondit la vallée.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M09b.34 to M09b.36)
# ---------------------------------------------------------------------------
M09B_34_MISTAKES = bug_letters_mistakes(
    "ACE", "BDF",
    {"A": "écris la forme de chaque matrice",
     "C": "dérive à nouveau ‖y − Xw‖² : d'où vient le signe ?",
     "E": "écris la définition du R² de la fiche §1"},
    name_correct=False)

M09B_34 = Ex(
    "M09b.34", "🐛", 1, 15, "Chasse à l'erreur : XXᵀ au lieu de XᵀX, un gradient de mauvais signe, un R² sans centrer",
    "repérer dans du code les erreurs classiques des moindres carrés, puis calculer les bonnes valeurs.",
    "fiche §1, §2 et §3", tracks="C",
    body=r"""Un collègue a écrit six lignes, chacune avec un commentaire qui dit ce qu'elle doit calculer. Trois lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter de code**, trouve-les.

```python
X = np.array([[1.0, 2.0], [1.0, -1.0], [1.0, 0.0]])    # 3 examples: a column of ones, then one feature
y = np.array([3.0, 0.0, 2.0])
w = np.array([1.0, 0.5])
G = X @ X.T                                   # (A) the 2 × 2 matrix XᵀX of the normal equations: G[0, 1]
r = y - X @ w                                 # (B) the residuals of the predictions Xw: r[0]
g = 2 * X.T @ (y - X @ w)                     # (C) the gradient of ‖y − Xw‖² at w: g[1]
w_new = w + 0.1 * 2 * X.T @ r                 # (D) one gradient descent step on ‖y − Xw‖², with η = 0.1: w_new[1]
r2 = 1 - np.sum(r ** 2) / np.sum(y ** 2)      # (E) the R² of the predictions Xw
mse = np.mean(r ** 2)                         # (F) the MSE of the predictions Xw
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire (une liste de 6 nombres, 4 décimales).

Dans ta copie : pour chaque ligne fausse, quelle erreur a été faite, et comment la corriger ? La ligne (A) s'exécute sans erreur : quelle est la forme de son résultat, et pourquoi Python ne signale-t-il rien ? La ligne (D) ajoute au lieu de retrancher : pourquoi est-elle juste ?""",
    todo='''answer_M09b_34a = ...  # a) letters, as text
answer_M09b_34b = ...  # b) a list of 6 values (4 decimals)''',
    check='''wbm.check("M09b.34a", answer_M09b_34a)
wbm.check("M09b.34b", answer_M09b_34b)''',
    solution='''answer_M09b_34a = "ACE"
X = np.array([[1.0, 2.0], [1.0, -1.0], [1.0, 0.0]])
y = np.array([3.0, 0.0, 2.0])
w = np.array([1.0, 0.5])
G = X.T @ X                                   # (A) XᵀX, of shape (2, 2): X @ X.T is the (3, 3) matrix of the examples
r = y - X @ w                                 # (B) correct
g = -2 * X.T @ (y - X @ w)                    # (C) the gradient has a minus sign
w_new = w + 0.1 * 2 * X.T @ r                 # (D) correct: w − η ∇L = w + 2η Xᵀr
r2 = 1 - np.sum(r ** 2) / np.sum((y - y.mean()) ** 2)   # (E) SST is around the mean of y
mse = np.mean(r ** 2)                         # (F) correct
answer_M09b_34b = [float(G[0, 1]), float(r[0]), float(g[1]), float(w_new[1]), float(r2), float(mse)]
print(answer_M09b_34a, np.round(answer_M09b_34b, 4))''',
    record=f'''wbm.record("M09b.34a", "ACE",
           mistakes={M09B_34_MISTAKES})
VALUES_34 = [1.0, 1.0, -5.0, 1.0, 1 - 2.25 / (42 / 9), 0.75]
wbm.record("M09b.34b", VALUES_34, decimals=4,
           mistakes={{"(A) : XᵀX a une ligne et une colonne par feature ; X @ X.T en a une par exemple":
                         [-1.0] + VALUES_34[1:],
                     "(C) : le gradient de ‖y − Xw‖² est −2Xᵀ(y − Xw)": VALUES_34[:2] + [5.0] + VALUES_34[3:],
                     "(E) : le R² compare la somme des carrés des résidus à celle des écarts à la moyenne de y":
                         VALUES_34[:4] + [1 - 2.25 / 13] + VALUES_34[5:]}})''',
    note=r"(A) `X @ X.T` est de forme $(3, 3)$ : la matrice des produits scalaires des **exemples**, dont l'élément $(1, 2)$ "
         r"existe, d'où l'absence d'erreur ; $\mathbf{X}^\top\mathbf{X}$ s'écrit `X.T @ X`, et son élément $(1, 2)$ vaut "
         r"$\sum_i x_i = 1$. (B) est juste : $\hat{\mathbf{y}} = (2 ;\ 0{,}5 ;\ 1)$, $r_1 = 1$. (C) Il manque le signe moins : "
         r"$\nabla L = -2\mathbf{X}^\top\mathbf{r} = -2(1{,}5 ;\ 2{,}5) = (-3, -5)$. (D) est juste : $\mathbf{w} - \eta"
         r"\nabla L = \mathbf{w} + 2\eta\mathbf{X}^\top\mathbf{r}$, et $0{,}5 + 0{,}2 \times 2{,}5 = 1$. (E) $\sum y_i^2 = 13$ "
         r"compare à la prédiction 0 ; avec $\bar{y} = \frac{5}{3}$, $\mathrm{SCT} = \frac{42}{9}$ et $R^2 = 1 - "
         r"\frac{2{,}25}{42/9} \approx 0{,}5179$, au lieu de $0{,}8269$. (F) est juste : $\frac{2{,}25}{3} = 0{,}75$.",
)

M09B_35_CHECK = '''with checked("M09b.35 vérifications"):
    problems = []
    w_t = np.array([0.3, -1.2, 2.0])
    approx_t = np.asarray(numerical_gradient(lambda v: float(np.sum(np.sin(v))), w_t), dtype=float)
    if approx_t.shape != w_t.shape or not np.allclose(approx_t, np.cos(w_t), rtol=0, atol=1e-8):
        problems.append("numerical_gradient ne donne pas le gradient de sum(sin(w)), qui vaut cos(w) : différence "
                        "centrée (f(w + h e_k) − f(w − h e_k)) / (2h), une coordonnée à la fois")
    else:
        rng_t = np.random.default_rng(35)
        A_t, X_t, y_t = rng_t.normal(size=(3, 3)), rng_t.normal(size=(6, 3)), rng_t.normal(size=6)
        quad_t = lambda v: float(v @ A_t @ v)                                    # noqa: E731
        good_t = gradient_error(quad_t, lambda v: (A_t + A_t.T) @ v, w_t)
        bad_t = gradient_error(quad_t, lambda v: 2 * A_t @ v, w_t)
        ls_t = gradient_error(lambda v: float(np.sum((y_t - X_t @ v) ** 2)), lambda v: -2 * X_t.T @ (y_t - X_t @ v), w_t)
        print(f"(A + Aᵀ)w : {good_t:.1e} · 2Aw : {bad_t:.1e} · −2Xᵀ(y − Xw) : {ls_t:.1e}")
        if not (good_t < 1e-8 and ls_t < 1e-8):
            problems.append("gradient_error doit être minuscule pour un gradient juste : compare numerical_gradient(f, "
                            "w) et grad(w), puis divise le plus grand écart par max(1, la plus grande valeur absolue)")
        elif not bad_t > 1e-2:
            problems.append("gradient_error doit être grand pour 2Aw, faux quand A n'est pas symétrique")
    try:
        same = symbolic_check(3)
    except NotImplementedError:
        raise
    if same is not True:
        problems.append("symbolic_check(3) doit rendre True : le gradient de SymPy et (A + Aᵀ)w, simplifiés, doivent "
                        "coïncider (renvoie un bool de Python)")
    if problems:
        print("❌ Ex M09b.35 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M09b.35 : le gradient numérique, la mesure d'erreur et la vérification symbolique sont justes.")'''

M09B_35 = Ex(
    "M09b.35", "🛠️", 1, 15, "Vérifier un gradient matriciel avec SymPy et par différences finies",
    "vérifier une formule de gradient de deux façons : numériquement, par des différences finies centrées, et "
    "exactement, avec SymPy.", "fiche §2 ; M05a (différences finies) ; Ex M09b.13", tracks="C",
    body=r"""Une formule de gradient fausse ne fait pas planter le code : la descente converge mal, ou vers le mauvais point. Avant de s'en servir, on la vérifie : c'est la **vérification du gradient** (*gradient checking*). Écris :
- `numerical_gradient(f, w, h=1e-6)` : le gradient de `f` en `w` par différences finies **centrées**, $\frac{f(\mathbf{w} + h\mathbf{e}_k) - f(\mathbf{w} - h\mathbf{e}_k)}{2h}$ pour chaque coordonnée $k$ (un tableau NumPy) ;
- `gradient_error(f, grad, w)` : le plus grand écart, en valeur absolue, entre `numerical_gradient(f, w)` et `grad(w)`, divisé par $\max(1, \text{la plus grande valeur absolue du gradient numérique})$ ;
- `symbolic_check(p)` : avec SymPy, un vecteur $\mathbf{w}$ de $p$ symboles et une matrice $\mathbf{A}$ de $p^2$ symboles (`sympy.symbols`, `sympy.Matrix`), le gradient de $\mathbf{w}^\top\mathbf{A}\mathbf{w}$ (`sympy.diff` sur chaque $w_k$) ; rends `True` si sa différence avec $(\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$, développée (`sympy.expand`), est nulle, en `bool` de Python.

La vérification essaie `numerical_gradient` sur une fonction de gradient connu, puis `gradient_error` sur $(\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$ (juste), sur $2\mathbf{A}\mathbf{w}$ (faux, $\mathbf{A}$ n'étant pas symétrique) et sur le gradient des moindres carrés ; enfin `symbolic_check(3)`.

Dans ta copie : pourquoi des différences **centrées** plutôt que $\frac{f(\mathbf{w} + h\mathbf{e}_k) - f(\mathbf{w})}{h}$ (M05a) ? Pourquoi pas $h = 10^{-12}$ ? Pourquoi `gradient_error` divise-t-il par la taille du gradient ? Combien d'évaluations de `f` coûte un gradient numérique, et pourquoi ne s'en sert-on pas pour entraîner un réseau ?""",
    todo='''def numerical_gradient(f, w, h=1e-6):
    """The gradient of f at w by centered finite differences, one coordinate at a time."""
    raise NotImplementedError("pour chaque k : (f(w + h e_k) − f(w − h e_k)) / (2h)")


def gradient_error(f, grad, w):
    """max |numerical gradient − grad(w)|, divided by max(1, max |numerical gradient|)."""
    raise NotImplementedError("numerical_gradient, puis le plus grand écart relatif")


def symbolic_check(p):
    """True if the SymPy gradient of wᵀAw (w: p symbols, A: p² symbols) equals (A + Aᵀ)w."""
    raise NotImplementedError("sympy.symbols, sympy.Matrix, sympy.diff, puis sympy.expand de la différence")''',
    solution='''def numerical_gradient(f, w, h=1e-6):
    """The gradient of f at w by centered finite differences, one coordinate at a time."""
    w = np.asarray(w, dtype=float)
    grad = np.zeros_like(w)
    for k in range(w.size):
        step = np.zeros_like(w)
        step[k] = h
        grad[k] = (f(w + step) - f(w - step)) / (2 * h)
    return grad


def gradient_error(f, grad, w):
    """max |numerical gradient − grad(w)|, divided by max(1, max |numerical gradient|)."""
    approx = numerical_gradient(f, w)
    return float(np.max(np.abs(approx - np.asarray(grad(w), dtype=float))) / max(1.0, np.max(np.abs(approx))))


def symbolic_check(p):
    """True if the SymPy gradient of wᵀAw (w: p symbols, A: p² symbols) equals (A + Aᵀ)w."""
    w = sympy.Matrix(sympy.symbols(f"w1:{p + 1}"))
    A = sympy.Matrix(p, p, sympy.symbols(f"a1:{p * p + 1}"))
    f = (w.T * A * w)[0, 0]
    gradient = sympy.Matrix([sympy.diff(f, wk) for wk in w])
    return bool(sympy.expand(gradient - (A + A.T) * w) == sympy.zeros(p, 1))


print(symbolic_check(2), symbolic_check(3))''',
    after=[("code", M09B_35_CHECK)],
    note=r"La différence centrée a une erreur d'ordre $h^2$ (les termes en $h$ du développement de Taylor se compensent, "
         r"M05a), contre $h$ pour la différence avant : avec $h = 10^{-6}$, environ $10^{-12}$ contre $10^{-6}$. Un $h$ "
         r"trop petit fait perdre des chiffres : $f(\mathbf{w} + h\mathbf{e}_k)$ et $f(\mathbf{w} - h\mathbf{e}_k)$ sont "
         r"presque égaux, et leur différence est dominée par les arrondis (environ $10^{-16}/h$). Diviser par la taille du "
         r"gradient rend la mesure indépendante de l'échelle de $f$. Un gradient numérique coûte $2p$ évaluations de $f$ : "
         r"pour un réseau à un million de poids, deux millions de passes avant par pas, alors que la rétropropagation "
         r"(M18) donne le gradient exact pour environ le coût de deux passes. On ne s'en sert que pour vérifier.",
)

GIVEN_36 = '''def target_36(x):
    """The function to approximate on [0, 40]."""
    return 20 / (20 + np.asarray(x, dtype=float))


GRID_36 = np.linspace(0, 40, 4001)                # where the maximal error is measured


def evaluate_36(coefficients, x):
    """The polynomial sum_k coefficients[k] * t**k, with t = (x - 20) / 20 (t goes from -1 to 1)."""
    t = (np.asarray(x, dtype=float) - 20) / 20
    return sum(c * t ** k for k, c in enumerate(coefficients))'''

M09B_36_CHECK = '''with checked("M09b.36 défi"):
    ok_36 = False
    coefficients_36 = fit_36()
    coefficients_36 = np.asarray(coefficients_36, dtype=float).ravel()
    if coefficients_36.size == 0 or coefficients_36.size > 6:
        print(f"❌ Ex M09b.36 : {coefficients_36.size} coefficients : un polynôme de degré au plus 5 en a au plus 6.")
    elif not np.all(np.isfinite(coefficients_36)):
        print("❌ Ex M09b.36 : des coefficients non finis.")
    else:
        error_36 = float(np.max(np.abs(evaluate_36(coefficients_36, GRID_36) - target_36(GRID_36))))
        worst_36 = float(GRID_36[np.argmax(np.abs(evaluate_36(coefficients_36, GRID_36) - target_36(GRID_36)))])
        print(f"erreur maximale : {error_36:.2e}, atteinte en x = {worst_36:g}")
        if error_36 < 1e-3:
            ok_36 = True
            print("✅ Ex M09b.36 : défi réussi : l'erreur maximale est sous 1e-3.")
        else:
            print("❌ Ex M09b.36 : l'erreur maximale dépasse 1e-3. Regarde où elle est atteinte : les moindres carrés "
                  "minimisent une somme de carrés, pas l'erreur maximale.")
with checked("M09b.36"):
    fit_36()                                              # ⏳ while fit_36 is not written
    wbm.check("M09b.36", bool(ok_36), computed=True)'''

M09B_36 = Ex(
    "M09b.36", "🏆", 3, 25, "Défi : approcher une fonction par un polynôme de degré au plus 5, avec une erreur maximale "
    "sous 1e−3",
    "construire, avec tes moindres carrés, un polynôme de degré au plus 5 dont l'erreur maximale sur tout un intervalle "
    "passe sous $10^{-3}$.", "fiche §3 et §4 ; Ex M09b.26 et M09b.32", tracks="C",
    body=r"""La fonction $f(x) = \frac{20}{20 + x}$ décroît de 1 à $\frac{1}{3}$ sur $[0, 40]$. **L'objectif** : un polynôme $p$ de degré au plus 5 tel que $\max_{x \in [0, 40]} |p(x) - f(x)| < 10^{-3}$, l'erreur étant mesurée sur la grille `GRID_36` de 4 001 points. Le polynôme s'écrit dans la variable $t = \frac{x - 20}{20}$, qui va de $-1$ à $1$ (M09b.32 dit pourquoi) : $p = c_0 + c_1t + \cdots + c_5t^5$.

Écris `fit_36()`, qui rend les coefficients $(c_0, \ldots, c_5)$ (au plus 6 nombres), calculés avec **ta** fonction `mymath.linreg.solve_least_squares` (sans `np.polyfit` ni `lstsq`) à partir de points $(x_i, f(x_i))$ que tu choisis. La cellule fournie définit `target_36`, `GRID_36` et `evaluate_36(coefficients, x)`, qui évalue ton polynôme.

Commence par le plus simple : les moindres carrés sur les 4 001 points de la grille. Mesure l'erreur maximale et regarde **où** elle est atteinte. La vérification affiche ton erreur maximale et l'endroit où elle est atteinte.

Dans ta copie : quelle erreur donnait ta première version, et où était-elle la plus grande ? Qu'as-tu changé ? Pourquoi les moindres carrés ne minimisent-ils pas l'erreur maximale ? Un degré 4 pourrait-il suffire (essaie) ?""",
    given=GIVEN_36,
    todo='''def fit_36():
    """At most 6 coefficients c_0, ..., c_5 of a polynomial in t = (x - 20) / 20 that approximates target_36 on
    [0, 40] with a maximal error below 1e-3, computed with mymath.linreg.solve_least_squares."""
    raise NotImplementedError("des points x_i, la matrice des puissances de t_i, puis solve_least_squares")''',
    check=M09B_36_CHECK,
    solution='''def fit_36():
    """At most 6 coefficients c_0, ..., c_5 of a polynomial in t = (x - 20) / 20 that approximates target_36 on
    [0, 40] with a maximal error below 1e-3, computed with mymath.linreg.solve_least_squares."""
    k = np.arange(30)
    t = np.cos((2 * k + 1) * np.pi / 60)              # 30 Chebyshev points: denser near the ends of [-1, 1]
    T = np.column_stack([t ** j for j in range(6)])
    return mymath.linreg.solve_least_squares(T, target_36(20 + 20 * t))


mymath = wbm.load_mymath("ref")
t_uniform = (GRID_36 - 20) / 20
first = mymath.linreg.solve_least_squares(np.column_stack([t_uniform ** j for j in range(6)]), target_36(GRID_36))
print("first try, least squares on the 4001 points of the grid:",
      f"{np.max(np.abs(evaluate_36(first, GRID_36) - target_36(GRID_36))):.2e}")
print("Chebyshev points:", f"{np.max(np.abs(evaluate_36(fit_36(), GRID_36) - target_36(GRID_36))):.2e}")''',
    after=[("solution", M09B_36_CHECK.split('with checked("M09b.36"):')[0].rstrip())],
    record='''wbm.record("M09b.36", True,
           mistakes={"l'erreur maximale n'est pas sous 1e-3 : la cellule du défi dit où elle est atteinte": False})''',
    note=r"Les moindres carrés sur une grille uniforme donnent une erreur maximale d'environ $1{,}3 \times 10^{-3}$, "
         r"atteinte en $x = 0$ : ils minimisent la **somme** des carrés, où les deux bords comptent peu (peu de points y "
         r"sont « coincés » d'un seul côté), et l'erreur s'y concentre. Il faut donner plus de poids aux bords : des "
         r"points plus serrés près de $-1$ et $1$, comme les **points de Tchebychev** $t_k = \cos\frac{(2k + 1)\pi}{2m}$ "
         r"(environ $5{,}8 \times 10^{-4}$), des poids plus grands près des bords (multiplier les lignes de $\mathbf{X}$ et "
         r"de $\mathbf{y}$ par $\sqrt{\text{poids}}$), ou des passes successives qui augmentent le poids des points mal "
         r"approchés. Un degré 4 ne suffit pas : même le meilleur polynôme de degré 4 a une erreur maximale d'environ "
         r"$1{,}7 \times 10^{-3}$. La meilleure erreur maximale possible en degré 5 est d'environ $4{,}6 \times 10^{-4}$ "
         r"(le polynôme « minimax », que des passes successives approchent).",
)


PART_A = Part("A", "Ta librairie : équations normales, ridge, matrice chapeau, sommes de carrés, monômes, Huber ; NumPy "
              "et scikit-learn",
              "Fiche §1, §3, §4 et §5. Les six fonctions de `mymath/linreg.py`, puis la même régression avec "
              "`np.linalg.lstsq` et scikit-learn.",
              given=TOOLS, exercises=[M09B_26, M09B_27, M09B_28, M09B_29])

PART_B = Part("B", "Une prédiction, deux expériences et une figure",
              "Fiche §1, §2, §4 et §8. Le $R^2$ et les features de bruit, l'estimateur rétréci, le conditionnement des "
              "puissances, les lignes de niveau de la loss.",
              exercises=[M09B_30, M09B_31, M09B_32, M09B_33])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §1 à §4. Trois erreurs à trouver, la vérification d'un gradient, puis une approximation polynomiale "
              "sous une erreur maximale.",
              exercises=[M09B_34, M09B_35, M09B_36])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M09b.1 à M09b.12, M09b.20, M09b.21 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M09b · Moindres carrés et régularisation — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m09b_moindres_carres/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M09b`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M09b · Moindres carrés et régularisation — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : losses et $R^2$, sommes de carrés, gradients, équations "
               "normales, colonne de 1, matrice chapeau, monômes, ridge et MAP, pénalités L1 et L2, log-vraisemblance, "
               "estimateur rétréci, un pas de descente de gradient, la standardisation avant ridge.\n"
               "- Écrire les six fonctions de `mymath/linreg.py` et les tester, puis comparer avec `lstsq` et "
               "scikit-learn.\n"
               "- Prédire l'effet de features de bruit, simuler un estimateur rétréci, mesurer un conditionnement, "
               "tracer une loss, chasser des erreurs, vérifier un gradient, approcher une fonction.\n\n"
               r"**Rappel express.** $\mathrm{MSE} = \frac{1}{n}\lVert \mathbf{r} \rVert^2$, $R^2 = 1 - "
               r"\frac{\mathrm{SCR}}{\mathrm{SCT}}$ ; $\nabla(\mathbf{a}^\top\mathbf{w}) = \mathbf{a}$, "
               r"$\nabla(\mathbf{w}^\top\mathbf{A}\mathbf{w}) = (\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$, "
               r"$\nabla\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2 = -2\mathbf{X}^\top(\mathbf{y} - "
               r"\mathbf{X}\mathbf{w})$ ; $\mathbf{X}^\top\mathbf{X}\,\mathbf{w} = \mathbf{X}^\top\mathbf{y}$ ; $\mathbf{H} = "
               r"\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$ ; $\binom{p + d}{d}$ monômes ; ridge : "
               r"$(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\mathbf{w} = \mathbf{X}^\top\mathbf{y}$, $\lambda = "
               r"\sigma^2/\tau^2$ ; erreur = biais² + variance + bruit.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu calculer une MSE, une MAE, une loss de Huber et un $R^2$, et dire ce que mesure chacun ?\n"
               "2. Sais-tu calculer les gradients de $\\mathbf{a}^\\top\\mathbf{w}$, de $\\mathbf{w}^\\top\\mathbf{A}"
               "\\mathbf{w}$ et de $\\lVert \\mathbf{y} - \\mathbf{X}\\mathbf{w} \\rVert^2$, et en tirer les équations "
               "normales ?\n"
               "3. Sais-tu expliquer les moindres carrés comme une projection, et les propriétés de la matrice chapeau ?\n"
               "4. Sais-tu résoudre un problème ridge, dire pourquoi il a toujours une solution, et le relier à un prior "
               "gaussien ?\n"
               "5. Sais-tu relier les moindres carrés au bruit gaussien, et décomposer une erreur en biais², variance et "
               "bruit ?\n\n"
               "**La suite** : le chapitre 9 de workbookIA (overfitting, underfitting et régularisation, avec ses "
               "propres implémentations), puis M10, la séparabilité linéaire et la convexité.")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter=CHAPTER) if kind == "exercise" else setup_cell(kind))
    cells += objectives_cell()
    cells += paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO,
                         learner_context="from fractions import Fraction   # Fraction(3, 4) is accepted too, as \"3/4\"")
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
