#!/usr/bin/env python
"""Build the two notebooks of chapter M25a from a single source (used by Claude).

    python tools/chapters/build_m25a.py
    python tools/run_all_notebooks.py chapitres/m25a_gaussienne/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m25a_gaussienne/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M25a.1 to M25a.9, 🔗 M25a.16), each answer computed in the notebook from the
data of its statement (exact fractions for the fractions, NumPy for the rest, SymPy for the expression of M25a.7 a));
parts A to D are the notebook exercises (M25a.20 to M25a.30), exactly as 02_exercices.md describes them. Wrong-answer
messages state a rule, never a number of the answer, the last step that gives it, nor another sub-question.

Data. The notebook exercises take the data of the paper exercises, as 02_exercices.md says: the greenhouse of M25a.1
(μ = (22, 65), Σ = [[4, −6], [−6, 34]], x_P = (24, 68), x_Q = (24, 60)), the bridge M25a.16 (μ = (5, 3),
Σ = [[4, −2], [−2, 10]], L = [[2, 0], [−1, 3]], E = [[1, 0], [0.5, −1], [−1, 2]]), the law of dimension 600 of
covariance 0.3^|i − j| at L ε, ε drawn with the seed 5920 (M25a.20); the road layers of M25a.2 (μ = (40, 60, 30),
Σ = [[4, 6, −2], [6, 13, −1], [−2, −1, 3]], cost (2, 1, 3)), 20 000 draws with the seed 5921 (M25a.21); the sensors of
M25a.4 (μ = (18, 17, 15), Σ = [[4, 3, 1], [3, 4, 2], [1, 2, 4]], readings 19.5 and 14, then 21 and 12) (M25a.22); the
thermometer of M25a.6 (Φ = [[1, 0], [1, 1]], e = (0.3, −0.6), S₀ = diag(0.25, 1), σ² = 0.04, then the prior
N(0, 0.5 I), temperatures from −50 to 250 °C) (M25a.23); 1 000 road layers and 50 greenhouse readings with the seed
5924, the two settings of M25a.8 (μ₀ = (2, −1), Σ₀ = [[4, 2], [2, 3]], μ₁ = (3, −2), Σ₁ = [[6, −1], [−1, 2]]) on the
square of half side 25 and 200 000 draws with the seed 5924 (M25a.24); the level 2 ln 10 and the covariances
0.6^|i − j| in dimension 2 to 10, 100 000 draws with the seed 5925 (M25a.25); the greenhouse, T = 24 °C, 200 000 draws
with the seed 5926, half widths 2, 1, 0.5, 0.2 and 0.05 °C (M25a.26); μ = (0, 1), standard deviations 1 and 2,
correlations 0, 0.5 and 0.9, x₁ = 1.5, ellipses at 50 % and 90 % (M25a.27); the wind of M25a.3 (μ = (2.5, 1),
Σ = [[14, 3], [3, 6]]), the greenhouse and the sensors, the colleague's checks diag(4, 9) with 50 000 draws (seed
5911) and three points (0, 0), (1.5, −1), (−2, 2) of N((−1, 0.5), [[2, −0.8], [−0.8, 1.25]]), 50 000 draws with the
seed 5928 (M25a.28); the wind, n = 2 000, 300 seeds drawn with the seed 5929, four wrong samplers, n = 200 000
(M25a.29); the road of 31 sensors, mean 14 − 0.15 s, covariance 4 exp(−|Δs|/6), noise 0.4, twelve sensors down, the
seed 5930 (M25a.30).
Seeds 5911 to 5939 only (the tests use 5810 to 5894, the figures of the fiche 5901 and 5902): those of the statements
(5920, 5921, 5924, 5925, 5926, 5928, 5929, 5930), 5911 (the colleague's check of M25a.28), and, for the hidden cases of
the check cells, 5913 (M25a.20), 5914 (M25a.22), 5917 (M25a.27), 5918 (M25a.28), 5919 and 5931 (M25a.29). The check
cells use their own data (random laws of dimension 1 to 5, other means, other readings), never the test cases of
tests/test_m25a_gaussian.py nor the examples of the docstrings of the stub (no [[2, 3], [3, 9]] with (1, −1), no
[[5, 2, 2], [2, 4, 0], [2, 0, 4]] with (1, 0, 2), no Φ = [[1, 0], [1, 1], [1, 2]] with y = (1, 2, 2)), nor the examples
of the fiche (no GPS μ = (2, −4), Σ = [[16, 4], [4, 10]], no bus [[1, 1, 1], [1, 2, 2], [1, 2, 4]], no spring, no
pieces (40, 25), no gauges (1, 2), (3, 3), (2, 5), (6, 6), no N(6, 4) against N(8, 9), no camera).

Nothing of workbookIA 25 is used (the notes of M25a in the syllabus and their list « Évités »): no encoder, latent
code, prior of a VAE, image nor network; no KL against N(0, 1), N(0, I) or N(0, τ²), no log-variance, no σ ⊙ ε, no
derivative of a KL; no ε returned and no backward pass in a sampler; no slerp function; none of the dimensions 20, 64,
100, 512, 784, nor 200 000 draws of N(2, 9) (the 200 000 draws of M25a.24 and M25a.26 are of the settings of M25a.8 and
of the greenhouse). The bug (1) of M25a.28 draws by E @ L, (2) forgets the factor 2 of ln det Σ, (3) makes the
conditional covariance depend on the reading: the three functions take a full Σ (never (mu, log_var) nor
(x, mean, var)). The property test of M25a.29 is run on the reference, on the four wrong samplers of the statement and
on two hidden wrong ones (a shifted mean, a covariance of the wrong sign) in dimension 3.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, check_unique_keys, guarded,  # noqa: E402,F401
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M25a"
FOLDER = "chapitres/m25a_gaussienne"

SHAPE = 'a shape: a tuple (7, 2) or a text "(7, 2)"'
FRACTION = 'an irreducible fraction, as text "p/q"'
EXACT = 'an exact value, as text, with sqrt, pi, ln, exp and fractions'
BOOL = "True or False"


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M25a.1", "La densité d'un couple gaussien (température et humidité d'une serre) en deux points", [
        ("a", "an integer", "DET_1",
         '''mistakes={"le déterminant d'une matrice 2 × 2 est ad − bc": int(S_1[0][0] * S_1[1][1] + S_1[0][1] * S_1[1][0])}'''),
        ("b", "a 2 × 2 matrix (exact values)", "floats(INV_1)",
         '''decimals=2,
           mistakes={"l'inverse divise la comatrice par le déterminant": floats(COMATRIX_1),
                     "dans l'inverse d'une matrice 2 × 2, les coefficients hors diagonale changent de signe : vérifie "
                     "le signe de départ": floats([[INV_1[0][0], -INV_1[0][1]], [-INV_1[1][0], INV_1[1][1]]]),
                     "dans l'inverse d'une matrice 2 × 2, les deux coefficients diagonaux s'échangent":
                         floats([[INV_1[1][1], INV_1[0][1]], [INV_1[1][0], INV_1[0][0]]])}'''),
        ("c", "a 2 × 2 matrix", "floats(L_1)",
         '''decimals=4,
           mistakes={"l₂₁ = Σ₂₁ / l₁₁ garde le signe de Σ₂₁": floats([[L_1[0][0], 0], [-L_1[1][0], L_1[1][1]]]),
                     "l₂₂ est la racine de Σ₂₂ − l₂₁²": floats([[L_1[0][0], 0], [L_1[1][0], math.sqrt(S_1[1][1])]]),
                     "le facteur de Cholesky est triangulaire inférieur : Σ = L Lᵀ": floats(np.transpose(L_1))}'''),
        ("d", "a list of 2 numbers", "floats(D2_1)",
         '''decimals=2,
           mistakes={"la distance de Mahalanobis utilise Σ⁻¹, pas Σ": [float(d @ S_1 @ d) for d in (XP_1 - MU_1, XQ_1 - MU_1)],
                     "la covariance de T et H compte : Δ² n'est pas la somme des écarts au carré divisés par les "
                     "variances": [float(np.sum(d ** 2 / np.diag(S_1))) for d in (XP_1 - MU_1, XQ_1 - MU_1)],
                     "donne les deux valeurs dans l'ordre des relevés de l'énoncé": floats(D2_1[::-1])}'''),
        ("e", EXACT, "DENSITY_MU_1",
         '''kind="exact",
           mistakes={"le facteur de la densité contient la racine de det Σ": f"1/({2 * DET_1}*pi)",
                     "en dimension d, le facteur contient (2π) à la puissance d/2": f"1/({ROOT_DET_1}*sqrt(2*pi))"}'''),
        ("f", "a list of 2 numbers (2 decimals)", "floats(LOGP_1)",
         '''decimals=2,
           mistakes={"le terme de distance de la log-densité est −½ Δ²": floats(-math.log(2 * math.pi)
                                                                            - 0.5 * math.log(DET_1) - np.array(D2_1)),
                     "la log-densité contient −½ ln det Σ, pas −ln det Σ": floats(-math.log(2 * math.pi)
                                                                                 - math.log(DET_1) - np.array(D2_1) / 2),
                     "le terme constant de la log-densité est −(d/2) ln(2π)": floats(-0.5 * math.log(2 * math.pi)
                                                                                     - 0.5 * math.log(DET_1)
                                                                                     - np.array(D2_1) / 2)}'''),
        ("g", "a number (4 decimals)", "RATIO_1",
         '''decimals=4,
           mistakes={"le rapport demandé a la densité de x_Q au numérateur": 1 / RATIO_1,
                     "une densité contient exp(−Δ²/2) : n'oublie pas le ½": RATIO_1 ** 2}'''),
        ("h", EXACT, 'f"sqrt({EUCLID2_1[1]})"',
         '''kind="exact",
           mistakes={"la distance demandée est celle de x_Q": f"sqrt({EUCLID2_1[0]})",
                     "une distance est la racine de la somme des carrés": EUCLID2_1[1]}'''),
        ("i", BOOL, "bool(EUCLID2_1[1] > EUCLID2_1[0] and D2_1[1] < D2_1[0])",
         '''mistakes={"compare les densités (ou les distances de Mahalanobis), pas les distances euclidiennes": False}'''),
    ]),

    Paper("M25a.2", "Trois mesures corrélées : une somme pondérée, une différence, un tirage μ + Lε", [
        ("a", "a 3 × 3 matrix", "floats(L_2)",
         '''decimals=4,
           mistakes={"le facteur de Cholesky est triangulaire inférieur : Σ = L Lᵀ": floats(L_2.T),
                     "l₃₂ = (Σ₃₂ − l₃₁ l₂₁) / l₂₂": floats(L32_WRONG_2)}'''),
        ("b", "an integer", "int(round(float(np.prod(np.diag(L_2)) ** 2)))",
         '''mistakes={"det Σ = (det L)²": int(round(float(np.prod(np.diag(L_2)))))}'''),
        ("c", "a list of 2 numbers", "[float(W_2 @ MU_2), float(W_2 @ S_2 @ W_2)]",
         '''decimals=4,
           mistakes={"la variance de wᵀx contient les covariances : c'est wᵀΣw":
                         [float(W_2 @ MU_2), float(np.sum(W_2 ** 2 * np.diag(S_2)))],
                     "les poids interviennent au carré dans une variance":
                         [float(W_2 @ MU_2), float(np.sum(W_2 * np.diag(S_2)))]}'''),
        ("d", "a list of 2 numbers", "[float(V_2 @ MU_2), float(V_2 @ S_2 @ V_2)]",
         '''decimals=4,
           mistakes={"Var(x₂ − x₁) = Var(x₁) + Var(x₂) − 2 Cov(x₁, x₂)":
                         [float(V_2 @ MU_2), float(S_2[0, 0] + S_2[1, 1])],
                     "vérifie le signe du terme de covariance : −2 Cov(x₁, x₂)":
                         [float(V_2 @ MU_2), float(S_2[0, 0] + S_2[1, 1] + 2 * S_2[0, 1])]}'''),
        ("e", "a 2 × 2 matrix", "floats(A_2 @ S_2 @ A_2.T)",
         '''decimals=4,
           mistakes={"le coût et l'écart sont corrélés : calcule wᵀΣv hors de la diagonale":
                         floats(np.diag(np.diag(A_2 @ S_2 @ A_2.T))),
                     "vérifie le signe de wᵀΣv, avec v = (−1, 1, 0)":
                         floats(A_2 @ S_2 @ A_2.T * np.array([[1, -1], [-1, 1]]))}'''),
        ("f", "a list of 3 numbers", "floats(MU_2 + L_2 @ EPS_2)",
         '''decimals=4,
           mistakes={"le tirage est μ + Lε, avec le facteur triangulaire inférieur L, pas Lᵀ": floats(MU_2 + L_2.T @ EPS_2),
                     "on multiplie ε par L, pas par Σ": floats(MU_2 + S_2 @ EPS_2),
                     "n'oublie pas d'ajouter μ": floats(L_2 @ EPS_2)}'''),
        ("g", "a 3 × 3 matrix", "floats(L_2.T @ L_2)",
         '''decimals=4,
           mistakes={"la covariance de Mε est M Mᵀ, avec M la matrice qui multiplie ε : chez le collègue, ce n'est pas L":
                         floats(S_2)}'''),
        ("h", BOOL, "bool(abs(float(W_2 @ S_2 @ V_2)) < 1e-12)",
         '''mistakes={"deux coordonnées d'un vecteur gaussien sont indépendantes seulement si leur covariance est nulle":
                         True}'''),
    ]),

    Paper("M25a.3", "Les ellipses à 90 % et à 95 % des composantes du vent", [
        ("a", "a list of 2 numbers", "floats(LAMBDAS_3)",
         '''decimals=4,
           mistakes={"ce sont les valeurs propres de Σ, pas celles de Σ⁻¹": floats([1 / LAMBDAS_3[1], 1 / LAMBDAS_3[0]]),
                     "de la plus grande à la plus petite": floats(LAMBDAS_3[::-1])}'''),
        ("b", FRACTION, "str(SLOPE_3)",
         '''kind="fraction", simplified=True,
           mistakes={"le grand axe suit le vecteur propre de la plus grande valeur propre": str(MINOR_SLOPE_3),
                     "la pente est v/u, la composante nord sur la composante est": str(1 / SLOPE_3)}'''),
        ("c", "a list of 2 numbers (4 decimals)", "floats(C2_3)",
         '''decimals=4,
           mistakes={"la masse 1 − β a pour niveau c² = −2 ln β : β est la part des relevés hors de l'ellipse":
                         floats([-2 * math.log(m) for m in MASSES_3]),
                     "on demande les niveaux c², pas c": floats(np.sqrt(C2_3))}'''),
        ("d", "a list of 2 numbers (4 decimals)", "floats(np.sqrt(C2_3[0] * LAMBDAS_F_3))",
         '''decimals=4,
           mistakes={"les demi-axes valent c√λ, pas cλ": floats(math.sqrt(C2_3[0]) * LAMBDAS_F_3),
                     "les demi-axes valent c√λ, avec c et non c²": floats(C2_3[0] * np.sqrt(LAMBDAS_F_3)),
                     "les demi-axes de l'ellipse Δ = c suivent √λ, pour les valeurs propres de Σ":
                         floats(math.sqrt(C2_3[0]) / np.sqrt(LAMBDAS_F_3[::-1]))}'''),
        ("e", "a list of 2 numbers (4 decimals)", "floats(np.sqrt(C2_3[1] * LAMBDAS_F_3))",
         '''decimals=4,
           mistakes={"les demi-axes valent c√λ, pas cλ": floats(math.sqrt(C2_3[1]) * LAMBDAS_F_3),
                     "les demi-axes valent c√λ, avec c et non c²": floats(C2_3[1] * np.sqrt(LAMBDAS_F_3))}'''),
        ("f", "a list of 2 numbers (2 decimals)", "floats(math.pi * np.array(C2_3) * math.sqrt(DET_3))",
         '''decimals=2,
           mistakes={"l'aire fait intervenir √(det Σ), pas det Σ": floats(math.pi * np.array(C2_3) * DET_3),
                     "l'aire de l'ellipse de niveau c est π c² √(det Σ) : c au carré":
                         floats(math.pi * np.sqrt(C2_3) * math.sqrt(DET_3))}'''),
        ("g", "a number (4 decimals)", "1 - math.exp(-C_LEVEL_3 ** 2 / 2)",
         '''decimals=4,
           mistakes={"en dimension 2, la masse d'une ellipse de niveau c n'est pas celle d'un intervalle de la droite":
                         math.erf(C_LEVEL_3 / math.sqrt(2)),
                     "le niveau c est au carré dans l'exponentielle": 1 - math.exp(-C_LEVEL_3 / 2)}'''),
        ("h", FRACTION, "str(D2_READING_3)",
         '''kind="fraction", simplified=True,
           mistakes={"Δ² utilise Σ⁻¹, pas Σ": str(fquad(DEV_3, frac_matrix(S_3))),
                     "la covariance des deux composantes compte : utilise toute la matrice Σ⁻¹":
                         str(sum(DEV_3[i] ** 2 / Fraction(S_3[i][i]) for i in range(2))),
                     "Δ² mesure l'écart à la moyenne μ": str(fquad(READING_3, finv2(frac_matrix(S_3))))}'''),
        ("i", BOOL, "bool(D2_READING_3 <= C2_3[0])",
         '''mistakes={"compare Δ² au niveau c² de l'ellipse à 90 %": False}'''),
    ]),

    Paper("M25a.4", "Un capteur en panne estimé par ses deux voisins : complément de Schur et loi conditionnelle", [
        ("a", "a 2 × 2 matrix (4 decimals)", "floats(SBB_INV_4)",
         '''decimals=4,
           mistakes={"les deux voisins sont corrélés : Σ_bb n'est pas diagonale":
                         floats([[1 / SBB_4[0][0], 0], [0, 1 / SBB_4[1][1]]]),
                     "on demande l'inverse du bloc": floats(SBB_4)}'''),
        ("b", "a list of 2 numbers (4 decimals)", "floats(WEIGHTS_4)",
         '''decimals=4,
           mistakes={"les poids utilisent Σ_bb⁻¹ entière, avec la covariance des deux voisins":
                         floats([SAB_4[j] / SBB_4[j][j] for j in range(2)]),
                     "les poids sont Σ_ab Σ_bb⁻¹, pas Σ_ab Σ_bb":
                         floats([sum(SAB_4[i] * SBB_4[i][j] for i in range(2)) for j in range(2)])}'''),
        ("c", FRACTION, "str(SCHUR_4)",
         '''kind="fraction", simplified=True,
           mistakes={"la variance conditionnelle est Σ₂₂ − Σ_ab Σ_bb⁻¹ Σ_ba, avec le bloc Σ_bb entier : les deux "
                     "voisins sont corrélés entre eux": str(S_4[1][1] - sum(SAB_4[j] ** 2 / SBB_4[j][j] for j in range(2))),
                     "sachant les voisins, la variance diminue : retire Σ_ab Σ_bb⁻¹ Σ_ba": str(S_4[1][1]),
                     "une variance est positive : Σ_bb doit être inversée":
                         str(S_4[1][1] - sum(SAB_4[i] * SBB_4[i][j] * SAB_4[j] for i in range(2) for j in range(2)))}'''),
        ("d", "a number (2 decimals)", "float(COND_MEAN_4)",
         '''decimals=2,
           mistakes={"la moyenne se corrige de l'écart x_b − μ_b, pas de x_b":
                         float(MU_4[1] + sum(WEIGHTS_4[j] * VALUES_4[j] for j in range(2))),
                     "les deux voisins sont corrélés entre eux : Σ_bb n'est pas diagonale":
                         float(MU_4[1] + sum(SAB_4[j] / SBB_4[j][j] * DEV_4[j] for j in range(2))),
                     "la moyenne conditionnelle ajoute Σ_ab Σ_bb⁻¹ (x_b − μ_b) : vérifie le signe":
                         float(MU_4[1] - sum(WEIGHTS_4[j] * DEV_4[j] for j in range(2)))}'''),
        ("e", "a number (4 decimals)", "math.sqrt(S_4[1][1]) - math.sqrt(SCHUR_4)",
         '''decimals=4,
           mistakes={"on demande l'écart des écarts-types, pas des variances": float(S_4[1][1] - SCHUR_4),
                     "on demande la différence entre l'écart-type avant et après la lecture": math.sqrt(SCHUR_4)}'''),
        ("f", "a list of 2 numbers (3 decimals)", "floats(ONE_NEIGHBOUR_4)",
         '''decimals=3,
           mistakes={"avec un seul voisin, le poids est Σ₂₁ / Σ₁₁": floats([MU_4[1] + S_4[1][0] * DEV_4[0],
                                                                          S_4[1][1] - S_4[1][0] ** 2]),
                     "la variance conditionnelle diminue de Σ₂₁² / Σ₁₁": floats([ONE_NEIGHBOUR_4[0], S_4[1][1]])}'''),
        ("g", "an integer", "int(DET_4)",
         '''mistakes={"det Σ = det Σ_bb × det(complément de Schur)": int(SBB_4[0][0] * SBB_4[1][1] - SBB_4[0][1] ** 2)}'''),
        ("h", FRACTION, "str(LAMBDA22_4)",
         '''kind="fraction", simplified=True,
           mistakes={"Λ₂₂ est le coefficient (2, 2) de l'inverse de Σ : calcule-le par la comatrice et le déterminant":
                         str(1 / LAMBDA22_4),
                     "le coefficient de l'inverse n'est pas l'inverse du coefficient": str(1 / Fraction(S_4[1][1]))}'''),
        ("i", BOOL, "False",
         '''mistakes={"la covariance conditionnelle ne dépend pas des valeurs lues": True}'''),
    ]),

    Paper("M25a.5", "Fusionner trois mesures d'une même distance : des précisions qui s'additionnent", [
        ("a", "a list of 2 numbers (4 decimals)", "floats(FUSE_TL_5)",
         '''decimals=4,
           mistakes={"on additionne les précisions (les inverses des variances), pas les variances":
                         floats([(X_5[0] + X_5[1]) / 2, V_5[0] + V_5[1]]),
                     "les poids sont les précisions 1/σ², pas 1/σ":
                         floats([(X_5[0] / SD_5[0] + X_5[1] / SD_5[1]) / (1 / SD_5[0] + 1 / SD_5[1]), FUSE_TL_5[1]]),
                     "la moyenne fusionnée est pondérée par les précisions": floats([(X_5[0] + X_5[1]) / 2, FUSE_TL_5[1]])}'''),
        ("b", "a list of 2 numbers (4 decimals)", "floats(FUSE_ALL_5)",
         '''decimals=4,
           mistakes={"on additionne les précisions, pas les variances": floats([FUSE_ALL_5[0], sum(V_5)]),
                     "la moyenne fusionnée est pondérée par les précisions": floats([sum(X_5) / 3, FUSE_ALL_5[1]])}'''),
        ("c", "a list of 2 numbers (2 decimals)", "floats(FUSE_WT_5)",
         '''decimals=2,
           mistakes={"on additionne les précisions, et la moyenne est pondérée par elles":
                         floats([(X_5[2] + X_5[0]) / 2, V_5[2] + V_5[0]])}'''),
        ("d", BOOL, "fuse(*FUSE_WT_5, X_5[1], V_5[1]) == FUSE_ALL_5",
         '''mistakes={"fusionner revient à additionner des précisions : l'ordre ne compte pas": False}'''),
        ("e", FRACTION, "str((1 / V_5[1]) / sum(1 / v for v in V_5))",
         '''kind="fraction", simplified=True,
           mistakes={"le poids d'une mesure est sa précision divisée par la somme des précisions": str(V_5[1] / sum(V_5)),
                     "les poids ne sont pas égaux : chaque mesure pèse selon sa précision": "1/3"}'''),
        ("f", "a number (4 decimals)", "math.sqrt(FUSE_ALL_5[1])",
         '''decimals=4, mistakes={"on demande l'écart-type, la racine de la variance": float(FUSE_ALL_5[1])}'''),
        ("g", BOOL, "bool(FUSE_ALL_5[1] > FUSE_TL_5[1])",
         '''mistakes={"une mesure de plus ajoute sa précision, même petite": True}'''),
    ]),

    Paper("M25a.6", "Étalonner un thermomètre par la régression linéaire bayésienne", [
        ("a", "a 2 × 2 matrix", "floats(EVIDENCE_COV_6)",
         '''decimals=2,
           mistakes={"les erreurs mesurées contiennent aussi le bruit de lecture σ²": floats(PHI_6 @ S0_6 @ PHI_6.T),
                     "la covariance des erreurs est Φ S₀ Φᵀ + σ² I, avec Φ à gauche":
                         floats(PHI_6.T @ S0_6 @ PHI_6 + NOISE_6 * np.eye(2))}'''),
        ("b", "a 2 × 2 matrix", "floats(S0_6 @ PHI_6.T)",
         '''decimals=2,
           mistakes={"Cov(θ, Φθ + w) = S₀ Φᵀ : une ligne par paramètre, une colonne par bain": floats(PHI_6 @ S0_6)}'''),
        ("c", "a number (4 decimals)", "gauss_logpdf(E_6, np.zeros(2), EVIDENCE_COV_6)",
         '''decimals=4,
           mistakes={"les deux erreurs sont corrélées par le décalage commun : garde toute la covariance":
                         gauss_logpdf(E_6, np.zeros(2), np.diag(np.diag(EVIDENCE_COV_6))),
                     "l'évidence contient le bruit de lecture σ²": gauss_logpdf(E_6, np.zeros(2), PHI_6 @ S0_6 @ PHI_6.T)}'''),
        ("d", "a 2 × 2 matrix (4 decimals)", "floats(SN_6)",
         '''decimals=4,
           mistakes={"a posteriori, ce sont les précisions qui s'additionnent":
                         floats(S0_6 + NOISE_6 * np.linalg.inv(PHI_6.T @ PHI_6)),
                     "la précision apportée par les données est σ⁻² ΦᵀΦ : on divise par σ²":
                         floats(np.linalg.inv(np.linalg.inv(S0_6) + NOISE_6 * PHI_6.T @ PHI_6))}'''),
        ("e", "a list of 2 numbers (4 decimals)", "floats(MN_6)",
         '''decimals=4,
           mistakes={"l'a priori tire aussi les paramètres vers sa moyenne : ce ne sont pas les moindres carrés":
                         floats(np.linalg.solve(PHI_6, E_6))}'''),
        ("f", "a list of 2 numbers (4 decimals)", "floats(predictive_6(50, MN_6, SN_6))",
         '''decimals=4,
           mistakes={"la prédictive d'une lecture contient le bruit σ²": floats(predictive_6(50, MN_6, SN_6, noise=False)),
                     "après l'étalonnage, la prédictive utilise m_N et S_N": floats(predictive_6(50, np.zeros(2), S0_6))}'''),
        ("g", "a list of 2 numbers (4 decimals)", "floats(predictive_6(200, MN_6, SN_6))",
         '''decimals=4,
           mistakes={"la prédictive d'une lecture contient le bruit σ²": floats(predictive_6(200, MN_6, SN_6, noise=False)),
                     "après l'étalonnage, la prédictive utilise m_N et S_N": floats(predictive_6(200, np.zeros(2), S0_6))}'''),
        ("h", "a number (4 decimals)", "float(SN_6[0, 1] / math.sqrt(SN_6[0, 0] * SN_6[1, 1]))",
         '''decimals=4,
           mistakes={"une corrélation divise la covariance par le produit des écarts-types": float(SN_6[0, 1]),
                     "vérifie le signe de la covariance a posteriori":
                         float(-SN_6[0, 1] / math.sqrt(SN_6[0, 0] * SN_6[1, 1]))}'''),
        ("i", BOOL, "bool(predictive_6(200, MN_6, SN_6)[1] < predictive_6(200, np.zeros(2), S0_6)[1])",
         '''mistakes={"les mesures réduisent l'incertitude sur les paramètres, donc partout": False}'''),
    ]),

    Paper("M25a.7", "La divergence KL continue entre deux lois exponentielles et entre deux lois uniformes", [
        ("a", 'an expression in a and b, as text', "str(KL_EXP_7)",
         '''kind="expr", variables=("a", "b"),
           mistakes={"l'espérance est prise sous la première loi, de moyenne 1/a": str(KL_EXP_7.subs({A_7: B_7, B_7: A_7},
                                                                                                     simultaneous=True)),
                     "n'oublie pas le terme constant": str(KL_EXP_7 + 1)}'''),
        ("b", "a number (3 decimals)", "kl_exp_7(1 / 3, 1 / 8)",
         '''decimals=3,
           mistakes={"le paramètre d'une loi exponentielle est l'inverse de sa moyenne, et l'espérance se prend sous "
                     "la première loi": kl_exp_7(3, 8),
                     "la KL se compte en nats, avec le logarithme népérien": kl_exp_7(1 / 3, 1 / 8) / math.log(2)}'''),
        ("c", "a number (3 decimals)", "kl_exp_7(1 / 8, 1 / 3)",
         '''decimals=3, mistakes={"KL(q ‖ p) prend l'espérance sous q, la première loi": kl_exp_7(1 / 3, 1 / 8)}'''),
        ("d", "a number (3 decimals)", "math.log(LEN_Q_7 / LEN_P_7)",
         '''decimals=3,
           mistakes={"une KL n'est jamais négative : c'est l'espérance de ln(p'/q') sous p'": math.log(LEN_P_7 / LEN_Q_7),
                     "la KL fait intervenir le rapport des densités, pas l'écart des longueurs":
                         math.log(LEN_Q_7 - LEN_P_7)}'''),
        ("e", BOOL, "False",
         '''mistakes={"quand la première loi pèse sur une région où la seconde est nulle, la KL est infinie": True}'''),
        ("f", "a number (3 decimals)", "kl_exp_7(1 / 6, 1 / 10)",
         '''decimals=3, mistakes={"l'espérance est prise sous la loi réelle, la première": kl_exp_7(1 / 10, 1 / 6)}'''),
        ("g", "a number (3 decimals)", "kl_exp_7(1 / 3, 1 / 8) + kl_exp_7(1 / 6, 1 / 10)",
         '''decimals=3,
           mistakes={"le logarithme d'un produit de densités est une somme : la KL d'une loi produit ne se multiplie "
                     "pas": kl_exp_7(1 / 3, 1 / 8) * kl_exp_7(1 / 6, 1 / 10)}'''),
        ("h", BOOL, "False",
         '''mistakes={"l'additivité demande des lois produits des deux côtés": True}'''),
    ]),

    Paper("M25a.8", "Deux réglages d'une machine de découpe : la KL entre deux gaussiennes dans les deux sens", [
        ("a", FRACTION, "str(TRACE_10_8)",
         '''kind="fraction", simplified=True,
           mistakes={"la trace demandée multiplie Σ₀ à gauche par l'inverse de Σ₁": str(TRACE_01_8)}'''),
        ("b", FRACTION, "str(QUAD_1_8)",
         '''kind="fraction", simplified=True,
           mistakes={"le décalage des moyennes se mesure avec l'inverse de la covariance de la seconde loi":
                         str(QUAD_0_8)}'''),
        ("c", EXACT, 'f"ln({DET1_8 / DET0_8})"',
         '''kind="exact",
           mistakes={"vérifie le sens du rapport : det Σ₁ au numérateur": f"ln({DET0_8 / DET1_8})",
                     "on demande le logarithme du rapport": str(DET1_8 / DET0_8)}'''),
        ("d", "a number (4 decimals)", "KL01_8",
         '''decimals=4,
           mistakes={"n'oublie pas le −d": KL01_8 + 1,
                     "la formule a un facteur ½": 2 * KL01_8,
                     "le logarithme est ln(det Σ₁ / det Σ₀), dans le même sens que la trace":
                         KL01_8 - math.log(DET1_8 / DET0_8)}'''),
        ("e", FRACTION, "str(TRACE_01_8)",
         '''kind="fraction", simplified=True,
           mistakes={"dans KL(p₁ ‖ p₀), la trace multiplie Σ₁ à gauche par l'inverse de Σ₀": str(TRACE_10_8)}'''),
        ("f", FRACTION, "str(QUAD_0_8)",
         '''kind="fraction", simplified=True,
           mistakes={"dans ce sens, le décalage se mesure avec l'inverse de Σ₀": str(QUAD_1_8)}'''),
        ("g", "a number (4 decimals)", "KL10_8",
         '''decimals=4,
           mistakes={"n'oublie pas le −d": KL10_8 + 1,
                     "la formule a un facteur ½": 2 * KL10_8,
                     "dans ce sens, le logarithme est ln(det Σ₀ / det Σ₁)": KL10_8 + math.log(DET1_8 / DET0_8)}'''),
        ("h", FRACTION, "str(QUAD_0_8 / 2)",
         '''kind="fraction", simplified=True,
           mistakes={"relis la formule de la KL quand les deux covariances sont égales : un facteur manque":
                         str(QUAD_0_8),
                     "la covariance commune est celle du réglage A": str(QUAD_1_8 / 2)}'''),
        ("i", "a number (4 decimals)", "entropy_8(S1_8) - entropy_8(S0_8)",
         '''decimals=4,
           mistakes={"l'entropie différentielle contient ½ ln det Σ, pas ln det Σ": math.log(DET1_8 / DET0_8),
                     "on demande une différence de logarithmes": float(DET1_8 / DET0_8) / 2}'''),
    ]),

    Paper("M25a.9", "La route orthodromique entre deux villes : angle au centre, slerp au tiers, corde", [
        ("a", "a list of 3 numbers (4 decimals)", "floats(U_9)",
         '''decimals=4,
           mistakes={"les fonctions trigonométriques de NumPy prennent des radians : convertis les degrés":
                         floats(unit_9(*BREST_9, radians=False)),
                     "une longitude ouest est négative": floats(unit_9(BREST_9[0], -BREST_9[1])),
                     "le vecteur est (cos φ cos λ, cos φ sin λ, sin φ), avec φ la latitude":
                         floats(unit_9(BREST_9[1], BREST_9[0]))}'''),
        ("b", "a list of 3 numbers (4 decimals)", "floats(V_9)",
         '''decimals=4, mistakes={"une longitude ouest est négative": floats(unit_9(NEW_YORK_9[0], -NEW_YORK_9[1]))}'''),
        ("c", "a number (4 decimals)", "OMEGA_9",
         '''decimals=4,
           mistakes={"on demande l'angle en radians": math.degrees(OMEGA_9),
                     "Ω est l'arc cosinus du produit scalaire": float(U_9 @ V_9)}'''),
        ("d", "an integer", "R_9 * OMEGA_9",
         '''decimals=0, mistakes={"la longueur d'un arc est R Ω, avec Ω en radians": R_9 * math.degrees(OMEGA_9)}'''),
        ("e", "an integer", "2 * R_9 * math.sin(OMEGA_9 / 2)",
         '''decimals=0, mistakes={"la corde fait intervenir le demi-angle au centre (fiche §8, « Arc et corde »)":
                                     2 * R_9 * math.sin(OMEGA_9)}'''),
        ("f", "a list of 3 numbers (4 decimals)", "floats(THIRD_9)",
         '''decimals=4,
           mistakes={"ramener sur la sphère un point de la corde ne donne pas le point du slerp":
                         floats(CHORD_THIRD_9 / np.linalg.norm(CHORD_THIRD_9)),
                     "le coefficient de u est sin((1 − t)Ω) / sin Ω": floats(slerp_9(U_9, V_9, 2 / 3))}'''),
        ("g", "a list of 2 numbers (2 decimals)", "floats(LAT_LON_9)",
         '''decimals=2,
           mistakes={"une longitude ouest est négative": floats([LAT_LON_9[0], -LAT_LON_9[1]]),
                     "la latitude d'abord": floats(LAT_LON_9[::-1])}'''),
        ("h", "an integer", "R_9 * (1 - math.cos(OMEGA_9 / 2))",
         '''decimals=0,
           mistakes={"la profondeur sous la surface est R moins la distance du milieu au centre":
                         R_9 * math.cos(OMEGA_9 / 2),
                     "le milieu de la corde est à l'angle Ω/2 de chaque ville": R_9 * (1 - math.cos(OMEGA_9))}'''),
        ("i", BOOL, "bool(abs(math.acos(float(U_9 @ CHORD_THIRD_9) / np.linalg.norm(CHORD_THIRD_9)) - OMEGA_9 / 3) < 1e-9)",
         '''mistakes={"seul le slerp avance d'un angle proportionnel à t": True}'''),
    ]),

    Paper("M25a.16", "Pont : des vecteurs rangés en lignes (n, d), tirés et évalués d'un coup", [
        ("a", SHAPE, "shape_of(E_16 @ L_16.T)",
         '''mistakes={"une ligne par tirage : E a la forme (n, d)": shape_of(L_16 @ E_16.T)}'''),
        ("b", "a 3 × 2 matrix", "floats(X_16)",
         '''decimals=4,
           mistakes={"chaque ligne est μᵀ + εᵢᵀ Lᵀ : on multiplie à droite par Lᵀ": floats(MU_16 + E_16 @ L_16),
                     "ajoute μ à chaque ligne": floats(E_16 @ L_16.T)}'''),
        ("c", "a list of 3 numbers", "floats(D2_16)",
         '''decimals=4, mistakes={"Δ² utilise Σ⁻¹, pas Σ": floats([d @ S_16 @ d for d in X_16 - MU_16])}'''),
        ("d", "a list of 3 numbers (4 decimals)", "floats(LOGP_16)",
         '''decimals=4,
           mistakes={"la log-densité contient −½ ln det Σ": floats(-math.log(2 * math.pi) - np.array(D2_16) / 2),
                     "le terme du déterminant est −½ ln det Σ, pas −ln det Σ":
                         floats(-math.log(2 * math.pi) - math.log(np.linalg.det(S_16)) - np.array(D2_16) / 2)}'''),
        ("e", "a number (4 decimals)", "float(np.sum(LOGP_16) / X_16.size)",
         '''decimals=4,
           mistakes={"on divise par n d, le nombre total de coordonnées": float(np.sum(LOGP_16) / len(X_16)),
                     "on demande une moyenne, pas une somme": float(np.sum(LOGP_16))}'''),
        ("f", SHAPE, "shape_of((X_16 - MU_16) @ np.linalg.inv(S_16) @ (X_16 - MU_16).T)",
         '''mistakes={"D a une ligne par point": shape_of(np.zeros((2, 2)))}'''),
        ("g", BOOL, "bool(np.allclose((L_16 @ E_16.T).T + MU_16, X_16))",
         '''mistakes={"la transposée d'un produit renverse l'ordre des facteurs": False}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (exact fractions, NumPy, SymPy for one expression)
import math
from fractions import Fraction

import numpy as np
import sympy as sp


def shape_of(shape):
    """A shape (a tuple, or that of an array) written as NumPy prints it: "(3, 4)"."""
    shape = np.shape(shape) if hasattr(shape, "shape") else shape
    return str(tuple(int(n) for n in shape))


def floats(values):
    """A vector or a matrix of exact values (fractions, floats) as nested lists of floats."""
    return np.asarray(values, dtype=float).tolist()


def frac_matrix(rows):
    """A matrix as nested lists of fractions."""
    return [[Fraction(v) for v in row] for row in rows]


def finv2(M):
    """The inverse of a 2 × 2 matrix of fractions: the comatrix divided by the determinant."""
    (a, b), (c, d) = M
    det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]]


def fquad(u, M):
    """uᵀ M u, exact."""
    return sum(u[i] * M[i][j] * u[j] for i in range(len(u)) for j in range(len(u)))


def gauss_logpdf(x, mean, cov):
    """ln N(x | mean, cov), by the formula of the fiche (§1), with the determinant and a linear system."""
    dev = np.asarray(x, dtype=float) - mean
    return float(-0.5 * (len(dev) * math.log(2 * math.pi) + math.log(np.linalg.det(cov))
                         + dev @ np.linalg.solve(cov, dev)))


MU_1, S_1 = np.array([22.0, 65.0]), np.array([[4.0, -6.0], [-6.0, 34.0]])                   # M25a.1
XP_1, XQ_1 = np.array([24.0, 68.0]), np.array([24.0, 60.0])
DET_1 = int(S_1[0, 0] * S_1[1, 1] - S_1[0, 1] * S_1[1, 0])
COMATRIX_1 = [[S_1[1, 1], -S_1[0, 1]], [-S_1[1, 0], S_1[0, 0]]]
INV_1 = (np.array(COMATRIX_1) / DET_1).tolist()
L11_1 = math.sqrt(S_1[0, 0])
L_1 = [[L11_1, 0.0], [S_1[1, 0] / L11_1, math.sqrt(S_1[1, 1] - (S_1[1, 0] / L11_1) ** 2)]]


def mahalanobis2_1(x):
    """Δ² by the triangular system L y = x − μ (a forward substitution)."""
    dev = x - MU_1
    y1 = dev[0] / L_1[0][0]
    y2 = (dev[1] - L_1[1][0] * y1) / L_1[1][1]
    return y1 ** 2 + y2 ** 2


D2_1 = [mahalanobis2_1(XP_1), mahalanobis2_1(XQ_1)]
assert np.allclose(D2_1, [d @ np.linalg.solve(S_1, d) for d in (XP_1 - MU_1, XQ_1 - MU_1)])
ROOT_DET_1 = math.isqrt(DET_1)
assert ROOT_DET_1 ** 2 == DET_1
DENSITY_MU_1 = f"1/({2 * ROOT_DET_1}*pi)"                                                    # 1 / (2π √det Σ)
LOGP_1 = [-math.log(2 * math.pi) - 0.5 * math.log(DET_1) - d / 2 for d in D2_1]
RATIO_1 = math.exp(LOGP_1[1] - LOGP_1[0])
EUCLID2_1 = [int(np.sum((x - MU_1) ** 2)) for x in (XP_1, XQ_1)]
MU_2 = np.array([40.0, 60.0, 30.0])                                                          # M25a.2
S_2 = np.array([[4.0, 6.0, -2.0], [6.0, 13.0, -1.0], [-2.0, -1.0, 3.0]])
W_2, V_2, EPS_2 = np.array([2.0, 1.0, 3.0]), np.array([-1.0, 1.0, 0.0]), np.array([0.5, -1.0, 2.0])
L_2 = np.linalg.cholesky(S_2)
A_2 = np.vstack([W_2, V_2])                                                                  # (c, δ) = A x
L32_WRONG_2 = L_2.copy()
L32_WRONG_2[2, 1] = S_2[2, 1] / L_2[1, 1]                                                    # l₃₁ l₂₁ forgotten
L32_WRONG_2[2, 2] = math.sqrt(S_2[2, 2] - L_2[2, 0] ** 2 - L32_WRONG_2[2, 1] ** 2)
S_3 = [[14, 3], [3, 6]]                                                                      # M25a.3
MU_3 = [Fraction(5, 2), Fraction(1)]
TRACE_3, DET_3 = S_3[0][0] + S_3[1][1], S_3[0][0] * S_3[1][1] - S_3[0][1] * S_3[1][0]
ROOT_3 = math.isqrt(TRACE_3 ** 2 - 4 * DET_3)
assert ROOT_3 ** 2 == TRACE_3 ** 2 - 4 * DET_3
LAMBDAS_3 = [Fraction(TRACE_3 + ROOT_3, 2), Fraction(TRACE_3 - ROOT_3, 2)]                  # decreasing
LAMBDAS_F_3 = np.array(LAMBDAS_3, dtype=float)
SLOPE_3 = (LAMBDAS_3[0] - S_3[0][0]) / S_3[0][1]                                             # v/u along (Σ − λ₁I)q = 0
MINOR_SLOPE_3 = (LAMBDAS_3[1] - S_3[0][0]) / S_3[0][1]
MASSES_3 = [0.90, 0.95]
C2_3 = [-2 * math.log(1 - m) for m in MASSES_3]                                              # c² = −2 ln β
C_LEVEL_3 = 1.4
READING_3 = [Fraction(17, 2), Fraction(0)]
DEV_3 = [READING_3[i] - MU_3[i] for i in range(2)]
D2_READING_3 = fquad(DEV_3, finv2(frac_matrix(S_3)))
S_4 = frac_matrix([[4, 3, 1], [3, 4, 2], [1, 2, 4]])                                         # M25a.4
MU_4, VALUES_4 = [Fraction(18), Fraction(17), Fraction(15)], [Fraction(39, 2), Fraction(14)]
B_4 = [0, 2]                                                                                 # the neighbours, a = {1}
SBB_4 = [[S_4[i][j] for j in B_4] for i in B_4]
SAB_4 = [S_4[1][j] for j in B_4]
SBB_INV_4 = finv2(SBB_4)
WEIGHTS_4 = [sum(SAB_4[i] * SBB_INV_4[i][j] for i in range(2)) for j in range(2)]          # Σ_ab Σ_bb⁻¹
DEV_4 = [VALUES_4[j] - MU_4[B_4[j]] for j in range(2)]
COND_MEAN_4 = MU_4[1] + sum(WEIGHTS_4[j] * DEV_4[j] for j in range(2))
SCHUR_4 = S_4[1][1] - sum(WEIGHTS_4[j] * SAB_4[j] for j in range(2))
ONE_NEIGHBOUR_4 = [MU_4[1] + S_4[1][0] / S_4[0][0] * DEV_4[0], S_4[1][1] - S_4[1][0] ** 2 / S_4[0][0]]
DET_4 = (S_4[0][0] * (S_4[1][1] * S_4[2][2] - S_4[1][2] * S_4[2][1])
         - S_4[0][1] * (S_4[1][0] * S_4[2][2] - S_4[1][2] * S_4[2][0])
         + S_4[0][2] * (S_4[1][0] * S_4[2][1] - S_4[1][1] * S_4[2][0]))
LAMBDA22_4 = (S_4[0][0] * S_4[2][2] - S_4[0][2] * S_4[2][0]) / DET_4                       # cofactor (2, 2) / det
assert abs(float(LAMBDA22_4) - np.linalg.inv(np.array(S_4, dtype=float))[1, 1]) < 1e-12
X_5 = [Fraction(31), Fraction(27), Fraction(36)]                                             # M25a.5: tape, laser, wheel
SD_5 = [Fraction(3), Fraction(2), Fraction(6)]
V_5 = [s ** 2 for s in SD_5]


def fuse(m1, v1, m2, v2):
    """The product of two Gaussian densities: precisions add up, means weighted by the precisions (exact)."""
    v = 1 / (1 / v1 + 1 / v2)
    return [v * (m1 / v1 + m2 / v2), v]


FUSE_TL_5 = fuse(X_5[0], V_5[0], X_5[1], V_5[1])
FUSE_ALL_5 = fuse(*FUSE_TL_5, X_5[2], V_5[2])
FUSE_WT_5 = fuse(X_5[2], V_5[2], X_5[0], V_5[0])
PHI_6, E_6 = np.array([[1.0, 0.0], [1.0, 1.0]]), np.array([0.3, -0.6])                     # M25a.6
S0_6, NOISE_6 = np.diag([0.25, 1.0]), 0.04
EVIDENCE_COV_6 = PHI_6 @ S0_6 @ PHI_6.T + NOISE_6 * np.eye(2)
SN_6 = np.linalg.inv(np.linalg.inv(S0_6) + PHI_6.T @ PHI_6 / NOISE_6)
MN_6 = SN_6 @ (PHI_6.T @ E_6 / NOISE_6)


def predictive_6(T, mean, cov, noise=True):
    """The predictive of the error of one reading at T °C: [mean, variance], φ = (1, T/100)."""
    phi = np.array([1.0, T / 100])
    return [float(phi @ mean), float(phi @ cov @ phi + (NOISE_6 if noise else 0.0))]


A_7, B_7, X_7 = sp.symbols("a b x", positive=True)                                          # M25a.7
KL_EXP_7 = sp.simplify(sp.integrate(A_7 * sp.exp(-A_7 * X_7) * sp.log((A_7 * sp.exp(-A_7 * X_7))
                                                                      / (B_7 * sp.exp(-B_7 * X_7))),
                                    (X_7, 0, sp.oo)))
kl_exp_7 = sp.lambdify((A_7, B_7), KL_EXP_7, "math")
LEN_P_7, LEN_Q_7 = 5 - 2, 10 - 0                                                            # U[2, 5] and U[0, 10]
MU0_8, S0_8 = [Fraction(2), Fraction(-1)], frac_matrix([[4, 2], [2, 3]])                    # M25a.8
MU1_8, S1_8 = [Fraction(3), Fraction(-2)], frac_matrix([[6, -1], [-1, 2]])
DELTA_8 = [MU1_8[i] - MU0_8[i] for i in range(2)]
INV0_8, INV1_8 = finv2(S0_8), finv2(S1_8)
TRACE_10_8 = sum(INV1_8[i][k] * S0_8[k][i] for i in range(2) for k in range(2))             # tr(Σ₁⁻¹Σ₀)
TRACE_01_8 = sum(INV0_8[i][k] * S1_8[k][i] for i in range(2) for k in range(2))             # tr(Σ₀⁻¹Σ₁)
QUAD_1_8, QUAD_0_8 = fquad(DELTA_8, INV1_8), fquad(DELTA_8, INV0_8)
DET0_8 = S0_8[0][0] * S0_8[1][1] - S0_8[0][1] * S0_8[1][0]
DET1_8 = S1_8[0][0] * S1_8[1][1] - S1_8[0][1] * S1_8[1][0]
KL01_8 = 0.5 * (float(TRACE_10_8 + QUAD_1_8) - 2 + math.log(DET1_8 / DET0_8))
KL10_8 = 0.5 * (float(TRACE_01_8 + QUAD_0_8) - 2 + math.log(DET0_8 / DET1_8))


def entropy_8(S):
    """½ ln((2πe)^d det Σ) in dimension 2."""
    return 0.5 * math.log((2 * math.pi * math.e) ** 2 * float(S[0][0] * S[1][1] - S[0][1] * S[1][0]))


BREST_9, NEW_YORK_9, R_9 = (48.39, -4.49), (40.71, -74.01), 6371.0                          # M25a.9


def unit_9(lat, lon, radians=True):
    """(cos φ cos λ, cos φ sin λ, sin φ) for a latitude φ and a longitude λ in degrees (radians=False: read as radians)."""
    f, l = (math.radians(lat), math.radians(lon)) if radians else (lat, lon)
    return np.array([math.cos(f) * math.cos(l), math.cos(f) * math.sin(l), math.sin(f)])


def slerp_9(u, v, t):
    omega = math.acos(float(u @ v))
    return (math.sin((1 - t) * omega) * u + math.sin(t * omega) * v) / math.sin(omega)


U_9, V_9 = unit_9(*BREST_9), unit_9(*NEW_YORK_9)
OMEGA_9 = math.acos(float(U_9 @ V_9))
THIRD_9 = slerp_9(U_9, V_9, 1 / 3)
LAT_LON_9 = [math.degrees(math.asin(THIRD_9[2])), math.degrees(math.atan2(THIRD_9[1], THIRD_9[0]))]
CHORD_THIRD_9 = (2 * U_9 + V_9) / 3                                                          # the third of the chord
MU_16, S_16 = np.array([5.0, 3.0]), np.array([[4.0, -2.0], [-2.0, 10.0]])                  # M25a.16
L_16, E_16 = np.array([[2.0, 0.0], [-1.0, 3.0]]), np.array([[1.0, 0.0], [0.5, -1.0], [-1.0, 2.0]])
assert np.allclose(L_16 @ L_16.T, S_16)
X_16 = MU_16 + E_16 @ L_16.T                                                                 # X = 1 μᵀ + E Lᵀ
D2_16 = [float(np.sum(np.linalg.solve(L_16, d) ** 2)) for d in X_16 - MU_16]               # ‖L⁻¹(x − μ)‖²
LOGP_16 = [-math.log(2 * math.pi) - 0.5 * math.log(np.linalg.det(S_16)) - d / 2 for d in D2_16]'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M25a.1 à M25a.9, 🔗 M25a.16)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une liste `[0.2, -1]` ; une matrice comme la liste de ses **lignes**, `[[1, 0], [-2, 3]]` ;\n"
               "- une fraction irréductible entre guillemets, `\"3/7\"`, quand la question le dit ;\n"
               "- une valeur exacte entre guillemets, écrite avec des entiers, des fractions, `sqrt`, `pi`, `ln` et "
               "`exp`, comme `\"sqrt(5)/3\"` ou `\"2*ln(7)\"` ;\n"
               "- une expression entre guillemets, comme `\"x*exp(-x)\"` ;\n"
               "- une **forme** comme un tuple, `(7, 2)`, ou comme un texte, `\"(7, 2)\"` ;\n"
               "- `True` ou `False` pour un vrai ou faux.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")
