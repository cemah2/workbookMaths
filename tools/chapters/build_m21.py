#!/usr/bin/env python
"""Build the two notebooks of chapter M21 from a single source (used by Claude).

    python tools/chapters/build_m21.py
    python tools/run_all_notebooks.py chapitres/m21_convolution/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m21_convolution/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M21.1 to M21.11, 🔗 M21.17), each answer computed in the notebook from the data
of its statement (exact fractions and loops written in the cell, NumPy for the products and ranks; windows and
positions counted one by one, never by the formula they check); parts A to D are the notebook exercises (M21.19 to
M21.29). Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it.

Data. The notebook exercises take the data of 02_exercices.md: three 8-sided dice and their total 11, (2 − X)⁷,
twelve daily temperatures (8, 10, 13, 15, 14, 12, 11, 9, 7, 6, 8, 10) and a 5-day average (M21.19); the kernel
(1, −3, 2) of M21.4 with n = 6, a kernel of 7 non-zero coefficients (4, −2, 1, 3, −1, 2, 5) with n = 1 000, the
kernels (1, 4, −2, 3) and (2, 0, −1, 5, 1) (M21.20); a daily profile of 24 hourly temperatures, the sequences
(3, −1, 2, 5) and (1, 2, −2), the kernel (5, −2, 0, 3, 1, 4) (M21.21); the smoothing kernel of M21.8, the mean over a
cross of five cells (1/5)[[0, 1, 0], [1, 1, 1], [0, 1, 0]] (singular values 2/5, 1/5, 0), the outer product of
(1, 2, 4, 2, 1) and (2, −1, 3) plus a noise of standard deviation 0.001 (M21.22); the stacks of M21.10 (the first one
with a step s₁ = 3), four stages of length 4 and step 2, a random stack (M21.23); a signal of 30 values, zero but
(x₇, x₈, x₉) = (2, 5, −1), the weights (1, −1, 2, 1) with a step 3 (M21.24); a grid of 360 × 360 random values and
kernels of rank 1 for k = 3, 5, 9, 15, 25 (M21.25); a 6 × 6 input and (k, s) = (5, 2), (6, 2), (7, 3), (9, 3)
(M21.26); the polynomials (1 + 2X)(3 − X + 4X²), checked by the colleague on (1 + 2X)(2 + 5X + 2X²), a transposed
convolution with k = 8, s = 3, m = 6 (checked by the colleague on (k, s) = (6, 2), (9, 3), (8, 4)), the kernel
[[2, 1, 3], [4, 2, 5], [2, 1, 3]], x = (6, 2, 7, 1, 8, 3) with the weights (2, −3) (M21.27); 200 random kernels and
signals of integers (M21.28); 7 secret weights, 2 000 Gaussian values, a noise 0.05 (M21.29). Part 0 takes the data
of the corrected statements (M21.6 h: 125 positions; M21.7: y = (3, 2, −2); M21.10 c: s₁ = 3; M21.17 g: the kernel
given to scipy.signal.convolve2d).
Seeds 5511 to 5539 only (the tests use 5410 to 5500): 5532 (M21.22), 5533 (M21.23), 5535 (M21.25), 5538 (M21.28),
5539 (M21.29), and 5521 to 5529 for the hidden cases of the check cells. The check cells use their own data (random
shapes, kernels of even and odd lengths, non-palindromic polynomials, steps that divide k or not), never the test
cases of tests/test_m21_convolution.py, nor the examples of the docstrings of the stub (no (3, 1, 4, 1, 5), no
(2 + X)(1 + 3X + X²), no Laplacian sent to separable_factors, no [2, 1, 3] nor [1, 2, 3] sent to toeplitz_matrix, no
[[1, 1], [1, 1]] nor [[1, 1, 1], [1, −1]] stack), nor those of the fiche: no x = (2, 5, −1, 3, 0, 4) with
w = (3, 1, −2), no capteur (5, 11, 8, 2, 14), no chariot 2t² + 1, no w = (3, −1, 2), no h = (4, 1, 0, 2), no
altitudes Z, no lissage (1, 4, 1)/6, no grille météo 100 × 150, no pile (4, 2, 1), (3, 2, 1), (3, 1, 2), no
g = (3, −1, 2, −2), no transposée de (2, −1, 3) par (1, 3, 3, 1), no n = 26 with k = 4, s = 3.

Nothing of workbookIA 21 is used (the notes of M21 in the syllabus): no image, MNIST, Fashion-MNIST, CIFAR-10 nor
ImageNet, no layer, learned filter, network, loss, gradient nor attack, no Sobel, box blur 1/9 nor sharpening kernel,
no (2, 0, 1, 3) with (1, 2), (1, 2, 3, 4) nor (1, 0, −1), no x = (1, 2, −1, 3) with (2, −1) or (1, −1), no size 28,
32 or 224, none of the receptive fields 3, 5, 7, 9, 11, 15, 35, 6, 18 of its stacks, none of its transposed sizes, no
PyTorch. The bug (1) of M21.27 is a product of polynomials computed by np.correlate (a kernel not flipped), never a
learned filter; its bug (2) assumes regular overlaps (k // s) in a transposed convolution, never a size function
of workbookIA 21; its bug (3) separates a rank-2 kernel; no function n_positions nor sliding_sum is left. The
property test of M21.28 runs the learner's test on the reference and on a wrong « same » mode (rows from ⌊k/2⌋), built
on the reference. M21.29 estimates the kernel of a sensor by least squares (M09b), with the
Toeplitz matrix of x or the window matrix of the fiche, never a gradient.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, check_unique_keys, guarded,  # noqa: E402,F401
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M21"
FOLDER = "chapitres/m21_convolution"

SHAPE = 'a shape: a tuple (7, 2) or a text "(7, 2)"'
FRACTION = 'an irreducible fraction, as text "p/q"'
MATRIX = "a matrix (list of rows)"
BOOL = "True or False"


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M21.1", "Deux dés truqués et un produit de polynômes : la même convolution", [
        ("a", "a list of 6 integers", "POLY_1",
         '''mistakes={"le coefficient de Xᵐ rassemble les aᵢbⱼ avec i + j = m : en faisant glisser une suite sans la "
                     "retourner, on calcule une corrélation, pas un produit de polynômes": CORR_1,
                     "le coefficient de Xᵐ rassemble les aᵢbⱼ avec i + j = m : en faisant glisser une suite sans la "
                     "retourner, dans un sens ou dans l'autre, on calcule une corrélation": CORR_OTHER_1,
                     "du terme constant au terme de plus haut degré : ta liste est dans l'autre ordre": POLY_1[::-1]}'''),
        ("b", FRACTION, "str(P_S_1[5])",
         '''kind="fraction", simplified=True,
           mistakes={"l'indice du coefficient n'est pas la valeur de S : les faces commencent à 1, les indices à 0":
                         str(Fraction(POLY_1[5], 48)),
                     "chaque dé décale d'une case : l'écart entre l'indice m et la valeur de S compte les deux dés":
                         str(Fraction(POLY_1[4], 48))}'''),
        ("c", FRACTION, "str(sum(p for s, p in P_S_1.items() if s >= 6))",
         '''kind="fraction", simplified=True,
           mistakes={"S ≥ 6 : la valeur 5 n'en fait pas partie": str(sum(p for s, p in P_S_1.items() if s >= 5)),
                     "quels indices m donnent S ≥ 6 ? Chaque dé décale d'une case": str(Fraction(POLY_1[5], 48))}'''),
        ("d", FRACTION, "str(sum(s * p for s, p in P_S_1.items()))",
         '''kind="fraction", simplified=True,
           mistakes={"c'est l'espérance de l'indice m ; la valeur de S est décalée":
                         str(sum(Fraction(m * c, 48) for m, c in enumerate(POLY_1)))}'''),
        ("e", "an integer", "next(m for m, c in enumerate(POLY_1) if Fraction(c, 48) == P_S_1[5])",
         '''mistakes={"l'indice m n'est pas la valeur de S": 5}'''),
        ("f", "an integer", "max(P_S_1, key=P_S_1.get)",
         '''mistakes={"c'est l'indice du plus grand coefficient ; la valeur de S est décalée":
                         POLY_1.index(max(POLY_1))}'''),
        ("g", FRACTION, "str(sum(p for t, p in P_T_1.items() if t >= 9))",
         '''kind="fraction", simplified=True,
           mistakes={"A + B + A' ≥ 9 compte aussi la plus grande valeur possible": str(P_T_1[9])}'''),
    ]),

    Paper("M21.2", "Convoluer et corréler un signal à la main, dans les trois modes", [
        ("a", "a list of 5 integers", "CORR_VALID_2",
         '''mistakes={"la corrélation croisée ne retourne pas le noyau : tu as calculé une convolution":
                         FULL_2[K_2 - 1:N_2]}'''),
        ("b", "a list of 9 integers", "FULL_2",
         '''mistakes={"la convolution retourne le noyau : tu as calculé une corrélation en mode plein":
                         ints(fraction_convolve(X_2, W_2[::-1]))}'''),
        ("c", "a list of 5 integers", "FULL_2[K_2 - 1:N_2]",
         '''mistakes={"la convolution retourne le noyau : tu as fait glisser w sans le retourner": CORR_VALID_2}'''),
        ("d", "a list of 7 integers", "FULL_2[(K_2 - 1) // 2:(K_2 - 1) // 2 + N_2]",
         '''mistakes={"NumPy commence le mode même taille à l'indice ⌊(min(n, k) − 1)/2⌋ de la convolution pleine, pas "
                     "à l'indice 0": FULL_2[:N_2],
                     "le mode même taille garde aussi une valeur du bord gauche : il ne commence pas à l'indice k − 1":
                         FULL_2[K_2 - 1:K_2 - 1 + N_2]}'''),
        ("e", "a list of 3 integers", "W_2[::-1]",
         '''mistakes={"une corrélation par w redonne a) : il faut un autre noyau": W_2}'''),
        ("f", BOOL, "CORR_VALID_2 == FULL_2[K_2 - 1:N_2]",
         '''mistakes={"compare terme à terme : retourner un noyau qui n'est pas symétrique change le résultat": True}'''),
        ("g", "an integer", "sum(FULL_2)",
         '''mistakes={"la somme d'une convolution est le PRODUIT des sommes des deux suites, pas leur somme":
                         sum(X_2) + sum(W_2)}'''),
    ]),

    Paper("M21.3", "Des pochoirs de différences finies : dérivée et dérivée seconde d'un signal échantillonné", [
        ("a", "a list of 5 numbers", "ints(FORWARD_3)",
         '''mistakes={"chaque différence se divise par h": ints(v * H_3 for v in FORWARD_3)}'''),
        ("b", "a list of 4 numbers", "ints(CENTRED_3)",
         '''mistakes={"la différence centrée divise par 2h, l'écart entre les instants t − h et t + h":
                         ints(2 * v for v in CENTRED_3),
                     "ce sont des différences avant ; la différence centrée lit les deux voisins": ints(FORWARD_3[1:])}'''),
        ("c", "a list of 4 numbers", "ints(SECOND_3)",
         '''mistakes={"la dérivée seconde divise par h², pas par h": ints(v * H_3 for v in SECOND_3),
                     "(fᵢ₊₁ − 2fᵢ + fᵢ₋₁)/h² : as-tu bien divisé, et par le bon nombre ?":
                         ints(v * H_3 ** 2 for v in SECOND_3)}'''),
        ("d", "a number", "float(ERROR_D_3)",
         '''decimals=2, mistakes={"l'erreur est la valeur approchée MOINS la vraie valeur": float(-ERROR_D_3)}'''),
        ("e", "a list of 2 numbers", "[float(FORWARD_3[1] - df_3(2)), float(FORWARD_3[1] - df_3(3))]",
         '''decimals=2, mistakes={"dans l'ordre de l'énoncé : d'abord f′(2), puis f′(3)":
                                     [float(FORWARD_3[1] - df_3(3)), float(FORWARD_3[1] - df_3(2))]}'''),
        ("f", BOOL, "bool(np.allclose(np.convolve([float(v) for v in F_3], [-1, 0, 1], 'valid') / 4, "
                    "[float(v) for v in CENTRED_3]))",
         '''mistakes={"np.convolve retourne le noyau : regarde le signe de chaque terme": True}'''),
        ("g", "a number", "float((f_3(5) - f_3(3)) / 2 - df_3(4))",
         '''decimals=2, mistakes={"l'erreur de la différence centrée est d'ordre 2 en h": float(ERROR_D_3 / 2),
                                 "l'erreur dépend de h : relis sa formule (M05a)": float(ERROR_D_3)}'''),
    ]),

    Paper("M21.4", "La matrice de Toeplitz d'une convolution pleine et d'une convolution valide : coefficients non "
                   "nuls, rang et noyau", [
        ("a", MATRIX, "T_4.tolist()",
         '''mistakes={"chaque COLONNE est le noyau, descendu d'une ligne de plus que la précédente": T_4.T.tolist(),
                     "T[i, j] = w₍ᵢ₋ⱼ₎ : la colonne j commence par w₀ ; ta matrice est celle du noyau retourné":
                         toeplitz_4(W_4[::-1], N_4).tolist()}'''),
        ("b", "an integer", "int(np.count_nonzero(T_4))",
         '''mistakes={"compte les coefficients NON NULS, pas tous les coefficients": int(T_4.size)}'''),
        ("c", "a list of 7 integers", "(T_4 @ X_4).tolist()",
         '''mistakes={"la convolution retourne le noyau : ton calcul utilise le noyau à l'envers":
                         (toeplitz_4(W_4[::-1], N_4) @ X_4).tolist()}'''),
        ("d", MATRIX, "V_4.tolist()",
         '''mistakes={"le mode valide garde les lignes k − 1 à n − 1 de T, pas les premières":
                         T_4[:N_4 - K_4 + 1].tolist(),
                     "relis une ligne de T : le noyau y apparaît retourné":
                         toeplitz_4(W_4[::-1], N_4)[K_4 - 1:N_4].tolist()}'''),
        ("e", "an integer", "RANK_V_4",
         '''mistakes={"les trois lignes sont échelonnées : aucune n'est combinaison des autres": RANK_V_4 - 1}'''),
        ("f", "an integer", "N_4 - RANK_V_4",
         '''mistakes={"c'est le rang ; théorème du rang : dim ker = nombre de colonnes − rang": RANK_V_4,
                     "V a plus de colonnes que de lignes : son noyau n'est pas réduit à 0": 0}'''),
        ("g", BOOL, "bool(np.all(V_4 @ GEOMETRIC_4 == 0))",
         '''mistakes={"calcule les trois coordonnées de V x pour ce signal": False}'''),
        ("h", "an integer", "int(np.linalg.matrix_rank(T_4))",
         '''mistakes={"les colonnes de T sont échelonnées : chacune commence une ligne plus bas, par w₀ ≠ 0": RANK_V_4}'''),
        ("i", "a list of 3 integers", "KERNEL_VT_4",
         '''mistakes={"lis une colonne de Vᵀ : le noyau n'y est pas dans le même ordre que w": W_4}'''),
    ]),

    Paper("M21.5", "Décaler puis filtrer, ou filtrer puis décaler : l'équivariance, ses bords et son pas", [
        ("a", "a list of 8 integers", "A_5",
         '''mistakes={"la somme glissante ne retourne pas les poids : tu as calculé une convolution":
                         ints(fraction_convolve(X_5, W_5)[len(W_5) - 1:len(X_5)])}'''),
        ("b", "a list of 8 integers", "correlate_valid(delayed_5(X_5, 3), W_5)",
         '''mistakes={"τ₃ retarde le signal : sa réponse se déplace vers la droite": A_5[3:] + [0] * 3}'''),
        ("c", "an integer", "LOST_5",
         '''mistakes={"compte les valeurs non nulles de a) qui, décalées de 5 cases, n'ont plus de position, pas le "
                     "décalage": 5,
                     "compte les termes, pas les valeurs distinctes : chacun des deux −4 de a) a sa propre position":
                         len({v for i, v in enumerate(A_5) if v != 0 and i + 5 > len(A_5) - 1}
                             - set(correlate_valid(delayed_5(X_5, 5), W_5)))}'''),
        ("d", "a list of 4 integers", "STRIDE2_5[0]",
         '''mistakes={"y₀ lit la fenêtre qui commence à la case 0": A_5[1::2]}'''),
        ("e", "a list of 4 integers", "STRIDE2_5[1]",
         '''mistakes={"un décalage d'une case de l'entrée ne décale pas cette sortie d'une case : recalcule les "
                     "fenêtres 0, 2, 4 et 6": [0] + STRIDE2_5[0][:-1]}'''),
        ("f", "an integer", "shift_between_5(STRIDE2_5[4], STRIDE2_5[0])",
         '''mistakes={"c'est le décalage de l'entrée ; la sortie, qui garde une valeur sur 2, bouge moins": 4}'''),
        ("g", BOOL, "(shift_between_5(STRIDE2_5[1], STRIDE2_5[0]) is not None "
                    "or shift_between_5(STRIDE2_5[0], STRIDE2_5[1]) is not None)",
         '''mistakes={"compare e) à d) décalée d'une ou deux cases : ce ne sont pas les mêmes nombres": True}'''),
    ]),

    Paper("M21.6", "Compter les positions d'une fenêtre : pas, dilatation, padding, « même taille » avec un pas, et le "
                   "problème inverse", [
        ("a", "an integer", "count_positions(1000, 7)",
         '''mistakes={"la position 0 compte aussi": count_positions(1000, 7) - 1}'''),
        ("b", "an integer", "count_positions(1000, 7, s=3, p=2)",
         '''mistakes={"la fenêtre incomplète n'existe pas : la partie entière se prend vers le BAS":
                         math.ceil((1000 + 2 * 2 - 6 - 1) / 3) + 1,
                     "le padding est ajouté des deux côtés": count_positions(1000, 7, s=3, p=1)}'''),
        ("c", "an integer", "count_positions(1000, 7, d=4)",
         '''mistakes={"la dilatation étale la fenêtre : relis son étendue": count_positions(1000, 7)}'''),
        ("d", "an integer", "count_positions(1000, 7, s=5, p=3, d=4)",
         '''mistakes={"la dilatation étale la fenêtre : relis son étendue": count_positions(1000, 7, s=5, p=3),
                     "la fenêtre incomplète n'existe pas : la partie entière se prend vers le BAS":
                         math.ceil((1000 + 2 * 3 - 4 * 6 - 1) / 5) + 1}'''),
        ("e", "an integer", "N_OUT_6",
         '''mistakes={"une sortie par bloc de s valeurs, le dernier bloc pouvant être incomplet": 365 // 3}'''),
        ("f", "a list of 2 integers", "ZEROS_6",
         '''mistakes={"la règle met le zéro en trop à la fin": ZEROS_6[::-1],
                     "recalcule le nombre total de zéros, juste assez pour que la dernière fenêtre tienne":
                         [ZEROS_6[1], ZEROS_6[1]]}'''),
        ("g", "a list of integers", "LENGTHS_6",
         '''mistakes={"une partie entière confond plusieurs longueurs consécutives": LENGTHS_6[:1],
                     "vérifie la plus petite de tes longueurs : combien de positions donne-t-elle ?":
                         [n - 5 for n in LENGTHS_6]}'''),
        ("h", "an integer", "STEP_6",
         '''mistakes={"avec ce pas, recompte les positions : il en donne plus de 125": STEP_6 - 1,
                     "avec ce pas, recompte les positions : il en donne moins de 125": STEP_6 + 1}'''),
    ]),

    Paper("M21.7", "Sous-échantillonner et insérer des zéros : la convolution transposée d'un signal et ses "
                   "recouvrements", [
        ("a", "a list of 3 integers", "(D3_7 @ X_7).tolist()",
         '''mistakes={"D₃ garde une valeur sur 3, pas les trois premières": X_7[:3]}'''),
        ("b", "a list of 7 integers", "(D3_7.T @ D3_7 @ X_7).tolist()",
         '''mistakes={"D₃ᵀ remet chaque valeur à SA place, la case 3i": (D3_7 @ X_7).tolist() + [0] * 4}'''),
        ("c", "an integer", "len(TRANSPOSED_7)",
         '''mistakes={"compte les intervalles entre les m valeurs, puis ajoute ce que couvre le dernier tampon":
                         M_7 * S_7,
                     "la dernière valeur imprime encore tout le noyau": SIZE_7 - 1,
                     "il y a m − 1 intervalles de s cases entre m valeurs, pas m": M_7 * S_7 + K_7}'''),
        ("d", "a list of integers", "TRANSPOSED_7.tolist()",
         '''mistakes={"chaque valeur yᵢ imprime yᵢ w tel quel : ton calcul utilise le noyau retourné":
                         (strided_matrix_7(W_7[::-1], SIZE_7, S_7).T @ Y_7).tolist()}'''),
        ("e", "a list of integers", "STAMPS_7.tolist()"),
        ("f", "a list of integers", "LENGTHS_7",
         '''mistakes={"une partie entière confond plusieurs longueurs consécutives": LENGTHS_7[:1]}'''),
        ("g", "an integer", "SIZE_OUT_7",
         '''mistakes={"le padding de sortie s'ajoute une seule fois": SIZE_7 + 2 * 2,
                     "le padding de sortie allonge le résultat": SIZE_7}'''),
        ("h", "an integer", "INTERIOR_7",
         '''mistakes={"compte les i tels que 0 ≤ j − 4i ≤ 11 pour une case j loin des bords": INTERIOR_7 + 1}'''),
    ]),

    Paper("M21.8", "Une carte de températures filtrée par un laplacien discret et par un lissage séparable", [
        ("a", MATRIX, "LAP_8.tolist()",
         '''mistakes={"le laplacien discret : la somme des quatre voisines MOINS 4 fois la case": (-LAP_8).tolist()}'''),
        ("b", "a list of 2 integers", "cell_8(LAP_8.argmax())",
         '''mistakes={"c'est la position dans la sortie ; la sortie (i, j) est centrée sur la case (i + 1, j + 1) de T":
                         output_8(LAP_8.argmax()),
                     "le plus GRAND laplacien : une case plus froide que ses voisines": cell_8(LAP_8.argmin())}'''),
        ("c", "a list of 2 integers", "cell_8(LAP_8.argmin())",
         '''mistakes={"c'est la position dans la sortie ; la sortie (i, j) est centrée sur la case (i + 1, j + 1) de T":
                         output_8(LAP_8.argmin()),
                     "le plus PETIT laplacien : une case plus chaude que ses voisines": cell_8(LAP_8.argmax())}'''),
        ("d", "a 2 × 6 matrix (1 decimal)", "floats(VERTICAL_8)",
         '''decimals=1, mistakes={"la passe VERTICALE combine trois lignes consécutives, dans chaque colonne":
                                     floats(correlate2d_valid(T_8, [A_8]))}'''),
        ("e", "a 2 × 4 matrix (2 decimals)", "floats(SMOOTH_8)",
         '''decimals=2, mistakes={"K = a aᵀ, avec a = (1, 3, 1)/5 : n'oublie pas le facteur de normalisation":
                                     floats(correlate2d_valid(T_8, [[25 * a * b for b in A_8] for a in A_8]))}'''),
        ("f", "a list of 2 integers", "[SMOOTH_8.size * 9, VERTICAL_8.size * 3 + SMOOTH_8.size * 3]",
         '''mistakes={"on demande le total pour toute la sortie, pas le compte par valeur": [9, 3 + 3],
                     "dans l'ordre : en direct, puis en deux passes":
                         [VERTICAL_8.size * 3 + SMOOTH_8.size * 3, SMOOTH_8.size * 9]}'''),
        ("g", BOOL, "bool(np.linalg.matrix_rank(LAPLACIAN_8) == 1)",
         '''mistakes={"un noyau séparable a toutes ses lignes proportionnelles à une même ligne": True}'''),
    ]),

    Paper("M21.9", "Paramètres et coût d'un filtrage à plusieurs canaux : standard, groupé, par canal, 1 × 1", [
        ("a", SHAPE, "shape_of((C_OUT_9, C_IN_9, K_9, K_9))",
         '''mistakes={"l'ordre des bibliothèques : (C_out, C_in, k_h, k_w)": shape_of((C_IN_9, C_OUT_9, K_9, K_9))}'''),
        ("b", "an integer", "params_9(C_IN_9, C_OUT_9, K_9)",
         '''mistakes={"chaque sortie a aussi un biais": params_9(C_IN_9, C_OUT_9, K_9) - C_OUT_9}'''),
        ("c", "an integer", "macs_9(C_IN_9, C_OUT_9, K_9)",
         '''mistakes={"une multiplication-addition par POIDS et par position : le biais s'ajoute, il ne se multiplie pas":
                         macs_9(C_IN_9, C_OUT_9, K_9) + OUT_H_9 * OUT_W_9 * C_OUT_9}'''),
        ("d", "an integer", "params_9(C_IN_9, C_OUT_9, K_9, g=4)",
         '''mistakes={"le biais ne se divise pas par g": params_9(C_IN_9, C_OUT_9, K_9) // 4}'''),
        ("e", "an integer", "macs_9(C_IN_9, C_OUT_9, K_9, g=4)",
         '''mistakes={"chaque sortie ne lit que les canaux de son groupe": macs_9(C_IN_9, C_OUT_9, K_9)}'''),
        ("f", "an integer", "params_9(C_IN_9, C_IN_9, K_9, g=C_IN_9)",
         '''mistakes={"chaque sortie a aussi un biais": params_9(C_IN_9, C_IN_9, K_9, g=C_IN_9) - C_IN_9}'''),
        ("g", "an integer", "params_9(C_IN_9, 5, 1)",
         '''mistakes={"chaque sortie a aussi un biais": params_9(C_IN_9, 5, 1) - 5}'''),
        ("h", SHAPE, "shape_of((C_OUT_9, count_positions(H_9, K_9, s=2, p=P_9), count_positions(W_9, K_9, s=2, p=P_9)))",
         '''mistakes={"la position 0 compte aussi : n'oublie pas le + 1":
                         shape_of((C_OUT_9, (H_9 + 2 * P_9 - K_9) // 2, (W_9 + 2 * P_9 - K_9) // 2)),
                     "un pas de 2 ne garde qu'une position sur 2 dans chaque direction":
                         shape_of((C_OUT_9, OUT_H_9, OUT_W_9))}'''),
        ("i", "an integer", "C_OUT_9 * OUT_H_9 * OUT_W_9 * BYTES_9",
         '''mistakes={"c'est le nombre de valeurs ; chacune occupe 4 octets en float32": C_OUT_9 * OUT_H_9 * OUT_W_9}'''),
    ]),

    Paper("M21.10", "Le noyau équivalent de deux lissages successifs, et le champ récepteur d'une pile avec pas et "
                    "dilatation", [
        ("a", "a list of 4 integers", "ints(6 * v for v in trimmed(stack_kernel_10([A_10, B_10], [1, 1])))"),
        ("b", "a list of 4 numbers (4 decimals)", "[float(v) for v in Z_10]",
         '''decimals=4, mistakes={"c'est y, la sortie du premier étage : il reste la moyenne de 3":
                                     [float(v) for v in correlate_valid(X_10, A_10)]}'''),
        ("c", "a list of integers", "ints(6 * v for v in trimmed(stack_kernel_10([A_10, B_10], [3, 1])))",
         '''mistakes={"le pas du premier étage écarte les lectures du second : son noyau est dilaté":
                         ints(6 * v for v in trimmed(stack_kernel_10([A_10, B_10], [1, 1]))),
                     "le noyau du second étage est dilaté du pas du premier étage, s₁":
                         ints(6 * v for v in trimmed(stack_kernel_10([A_10, B_10], [2, 1])))}'''),
        ("d", "an integer", "math.prod([3, 1])",
         '''mistakes={"le pas total est le produit des pas": sum([3, 1])}'''),
        ("e", "an integer", "R_10",
         '''mistakes={"un pas multiplie les contributions des étages SUIVANTS":
                         1 + sum(d * (k - 1) for k, s, d in STACK_10),
                     "la dilatation multiplie aussi la contribution de son étage":
                         receptive_field_10([(k, s, 1) for k, s, d in STACK_10]),
                     "les étendues ne s'additionnent pas : les pas des étages précédents multiplient chaque contribution":
                         sum(d * (k - 1) + 1 for k, s, d in STACK_10)}'''),
        ("f", "an integer", "S_10",
         '''mistakes={"le pas total est le PRODUIT des pas": sum(s for k, s, d in STACK_10)}'''),
        ("g", "a list of 2 integers", "[2 * S_10, 2 * S_10 + R_10 - 1]",
         '''mistakes={"la sortie zⱼ commence à la case S j du signal d'origine": [2, 2 + R_10 - 1],
                     "le champ récepteur a r cases : la dernière est S j + r − 1": [2 * S_10, 2 * S_10 + R_10]}'''),
        ("h", BOOL, "R_10 == sum(d * (k - 1) + 1 for k, s, d in STACK_10)",
         '''mistakes={"calcule le champ récepteur par la récurrence, puis compare": True}'''),
    ]),

    Paper("M21.11", "Le pire cas d'une erreur de capteurs bornée : une forme linéaire sur les boules L∞ et L2", [
        ("a", "an integer", "L1_11",
         '''mistakes={"la norme L1 additionne les VALEURS ABSOLUES des poids": abs(sum(G_11))}'''),
        ("b", "a number", "WORST_INF_11",
         '''decimals=3, mistakes={"la boule L∞ va avec la norme L1 des poids, pas avec leur norme L∞": EPS_11 * LINF_11,
                                 "c'est le pire cas sur la boule L2 : la boule L∞ autorise plus": EPS_11 * L2_11}'''),
        ("c", "a list of 5 numbers", "DELTA_11",
         '''decimals=2, mistakes={"chaque erreur vaut au plus ε en valeur absolue : ton vecteur sort de la boule":
                                     [EPS_11 * g for g in G_11],
                                 "c'est le pire cas dans l'autre sens : le signe de chaque erreur doit être celui de "
                                 "son poids": [-v for v in DELTA_11]}'''),
        ("d", "a number (3 decimals)", "EPS_11 * L2_11",
         '''decimals=3, mistakes={"c'est le pire cas sur la boule L∞": WORST_INF_11,
                                 "ε fois la norme L2 : la RACINE de la somme des carrés des poids": EPS_11 * L2_11 ** 2}'''),
        ("e", "a number (4 decimals)", "math.sqrt(sum(v * v for v in DELTA_11))",
         '''decimals=4, mistakes={"la norme L2 d'un vecteur n'est pas la plus grande de ses coordonnées : c'est la "
                                 "racine de la somme de leurs carrés": EPS_11}'''),
        ("f", "a number", "WORST_ONE_11",
         '''decimals=3, mistakes={"la boule L1 va avec la norme L∞ des poids": WORST_INF_11}'''),
        ("g", "a number", "0.3 * float(np.abs(LAPLACIAN_8).sum())",
         '''decimals=3, mistakes={"le coefficient du centre compte aussi, en valeur absolue":
                                     0.3 * float(np.abs(LAPLACIAN_8).sum() - 4),
                                 "la norme L1 additionne les valeurs ABSOLUES des coefficients":
                                     0.3 * abs(float(LAPLACIAN_8.sum()))}'''),
        ("h", "a list of 2 numbers", "[0.01 * L1_H_11, 0.01 * L2_H_11]",
         '''decimals=3, mistakes={"la boule L2 va avec la norme L2 des poids": [0.01 * L1_H_11, 0.01 * L1_H_11],
                                 "dans l'ordre : la boule L∞, puis la boule L2": [0.01 * L2_H_11, 0.01 * L1_H_11]}'''),
    ]),

    Paper("M21.17", "Pont : filtrer une grille à trois canaux comme les bibliothèques, formes (C, H, W), poids "
                    "(C_out, C_in, k, k), et sans retournement", [
        ("a", SHAPE, "shape_of(X_17)",
         '''mistakes={"les bibliothèques rangent les canaux en premier : (C, H, W)": shape_of(X_17.transpose(1, 2, 0))}'''),
        ("b", SHAPE, "shape_of(W_17)",
         '''mistakes={"l'ordre des bibliothèques : (C_out, C_in, k_h, k_w)": shape_of(W_17.transpose(1, 0, 2, 3))}'''),
        ("c", SHAPE, "shape_of(Y_17)",
         '''mistakes={"en mode valide, chaque axe perd k − 1 cases": shape_of((len(W_17),) + X_17.shape[1:]),
                     "les canaux de sortie en premier": shape_of(Y_17.transpose(1, 2, 0))}'''),
        ("d", "an integer", "int(W_17.size + B_17.size)",
         '''mistakes={"chaque sortie a aussi un biais": int(W_17.size)}'''),
        ("e", "an integer", "int(Y_17[0, 0, 0])",
         '''mistakes={"n'oublie pas le biais de la sortie 0": int(Y_17[0, 0, 0] - B_17[0]),
                     "les bibliothèques ne retournent pas les noyaux": int(FLIPPED_17[0, 0, 0])}'''),
        ("f", "an integer", "int(Y_17[1, 2, 3])",
         '''mistakes={"n'oublie pas le biais de la sortie 1": int(Y_17[1, 2, 3] - B_17[1])}'''),
        ("g", "a 2 × 2 matrix (list of rows)", "KERNEL_2D_17.tolist()",
         '''mistakes={"retourne le noyau selon ses DEUX axes : tu n'as inversé que l'ordre des lignes":
                         W_17[0, 0, ::-1, :].tolist(),
                     "retourne le noyau selon ses DEUX axes : tu n'as inversé que l'ordre des colonnes":
                         W_17[0, 0, :, ::-1].tolist(),
                     "convolve2d retourne le noyau qu'on lui donne": W_17[0, 0].tolist()}'''),
        ("h", "an integer", "int(Y_17.size * W_17[0].size)",
         '''mistakes={"compte chaque sortie : une multiplication-addition par poids et par position, pour chaque canal "
                     "de sortie": int(Y_17[0].size * W_17[0].size),
                     "c'est le nombre de poids ; chacun sert à chaque position": int(W_17.size)}'''),
        ("i", "a list of 5 integers", "TORCH_SAME_17",
         '''mistakes={"c'est ce que rend NumPy ; PyTorch met le zéro en trop à droite": NUMPY_SAME_17}'''),
        ("j", "a list of 5 integers", "NUMPY_SAME_17",
         '''mistakes={"c'est la version de PyTorch ; NumPy met le zéro en trop au début": TORCH_SAME_17,
                     "np.convolve retourne le noyau qu'on lui donne": correlate_valid(X1D_17 + [0], [4, 1]),
                     "np.convolve retourne le noyau qu'on lui donne, et met le zéro en trop au début":
                         np.convolve(X1D_17, [1, 4], "same").tolist()}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (exact fractions, loops, NumPy)
import math
from fractions import Fraction
from itertools import product

import numpy as np
import scipy.signal


def shape_of(shape):
    """A shape (a tuple, or that of an array) written as NumPy prints it: "(3, 4, 5)", "(5,)"."""
    shape = np.shape(shape) if hasattr(shape, "shape") else shape
    return str(tuple(int(n) for n in shape))


def ints(values):
    """A list of Python ints from exact values (integers, fractions, floats equal to integers)."""
    values = list(values)
    out = [int(round(float(v))) for v in values]
    assert all(abs(float(v) - o) < 1e-9 for v, o in zip(values, out)), values
    return out


def floats(array):
    """A matrix of exact values as a list of rows of floats."""
    return [[float(v) for v in row] for row in array]


def correlate_valid(x, w, s=1):
    """The sliding sum of the libraries, valid mode, step s: y[i] = Σ_u w[u] x[s i + u] (loops)."""
    k = len(w)
    return [sum(w[u] * x[s * i + u] for u in range(k)) for i in range((len(x) - k) // s + 1)]


def fraction_convolve(a, b):
    """The exact full convolution (a * b)[m] = Σ_i a[i] b[m − i], with fractions."""
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += Fraction(ai) * Fraction(bj)
    return out


def count_positions(n, k, s=1, p=0, d=1):
    """The windows that fit in the padded signal (length n + 2p), counted one by one: no formula."""
    return sum(1 for start in range(0, n + 2 * p, s) if start + d * (k - 1) <= n + 2 * p - 1)


def correlate2d_valid(X, K):
    """The valid sliding sum of a grid X by a kernel K (no flip), with loops."""
    kh, kw = len(K), len(K[0])
    return np.array([[sum(K[u][v] * X[i + u][j + v] for u in range(kh) for v in range(kw))
                      for j in range(len(X[0]) - kw + 1)] for i in range(len(X) - kh + 1)])


FACES_A_1, FACES_B_1 = [1, 1, 1, 2, 2, 3], [1, 2, 3, 3, 4, 4, 4, 4]                           # M21.1
LAW_A_1 = [Fraction(FACES_A_1.count(v), 6) for v in (1, 2, 3)]                               # P(A = 1), ...
LAW_B_1 = [Fraction(FACES_B_1.count(v), 8) for v in (1, 2, 3, 4)]
POLY_1 = ints(fraction_convolve([3, 2, 1], [1, 1, 2, 4]))                    # (3 + 2X + X²)(1 + X + 2X² + 4X³)
CORR_1 = ints(fraction_convolve([3, 2, 1], [4, 2, 1, 1]))                    # sliding without flipping
CORR_OTHER_1 = ints(fraction_convolve([1, 2, 3], [1, 1, 2, 4]))              # the same, in the other direction
P_S_1 = {m + 2: p for m, p in enumerate(fraction_convolve(LAW_A_1, LAW_B_1))}                # index m ↔ S = m + 2
assert P_S_1 == {s: Fraction(sum(a + b == s for a, b in product(FACES_A_1, FACES_B_1)), 48) for s in P_S_1}
P_T_1 = {m + 3: p for m, p in enumerate(fraction_convolve(fraction_convolve(LAW_A_1, LAW_B_1), LAW_A_1))}  # + A'
assert sum(P_T_1.values()) == 1
X_2, W_2 = [3, -2, 0, 5, 1, -4, 2], [4, -1, 2]                                               # M21.2
N_2, K_2 = len(X_2), len(W_2)
FULL_2 = ints(fraction_convolve(X_2, W_2))                                                    # x * w, full
CORR_VALID_2 = correlate_valid(X_2, W_2)                                                      # w ⋆ x, valid
assert FULL_2 == np.convolve(X_2, W_2).tolist()
H_3 = 2                                                                                       # M21.3


def f_3(t):
    """The volume of the tank, f(t) = t³/4."""
    return Fraction(t) ** 3 / 4


def df_3(t):
    """f'(t) = 3t²/4."""
    return 3 * Fraction(t) ** 2 / 4


F_3 = [f_3(t) for t in range(0, 11, H_3)]                                                     # (0, 2, 16, ...)
FORWARD_3 = [(F_3[i + 1] - F_3[i]) / H_3 for i in range(len(F_3) - 1)]
CENTRED_3 = [(F_3[i + 1] - F_3[i - 1]) / (2 * H_3) for i in range(1, len(F_3) - 1)]          # t = 2 to 8
SECOND_3 = [(F_3[i + 1] - 2 * F_3[i] + F_3[i - 1]) / H_3 ** 2 for i in range(1, len(F_3) - 1)]
ERROR_D_3 = CENTRED_3[1] - df_3(4)                                                            # t = 4 is index 2
W_4, N_4 = [1, -3, 2], 5                                                                      # M21.4
K_4, X_4 = len(W_4), [2, 0, -1, 3, 1]


def toeplitz_4(w, n):
    """The matrix of x ↦ x * w, full mode: T[i, j] = w[i − j], 0 outside the kernel."""
    return np.array([[w[i - j] if 0 <= i - j < len(w) else 0 for j in range(n)] for i in range(n + len(w) - 1)])


T_4 = toeplitz_4(W_4, N_4)
V_4 = T_4[K_4 - 1:N_4]                                                                        # rows k − 1 to n − 1
assert np.array_equal(T_4 @ X_4, np.convolve(X_4, W_4))
RANK_V_4 = int(np.linalg.matrix_rank(V_4))
GEOMETRIC_4 = [2 ** i for i in range(N_4)]
KERNEL_VT_4 = V_4.T[:K_4, 0].tolist()                                                         # read on a column of Vᵀ
assert np.array_equal(toeplitz_4(KERNEL_VT_4, N_4 - K_4 + 1), V_4.T)
X_5, W_5 = [0, 0, 2, -1, 3, 0, 0, 0, 0, 0], [1, -1, 2]                                       # M21.5


def delayed_5(x, t):
    """τ_t x: t zeros enter on the left, the last t values leave on the right."""
    return [0] * t + x[:len(x) - t]


def shift_between_5(y, y0):
    """The m ≥ 0 such that y is y0 moved m places to the right (zeros entering on the left), or None."""
    return next((m for m in range(len(y0)) if y[m:] == y0[:len(y0) - m] and not any(y[:m])), None)


A_5 = correlate_valid(X_5, W_5)
LOST_5 = sum(1 for i, v in enumerate(A_5) if v != 0 and i + 5 > len(A_5) - 1)          # shifted beyond the end
assert LOST_5 == sum(v != 0 for v in A_5) - sum(v != 0 for v in correlate_valid(delayed_5(X_5, 5), W_5))
STRIDE2_5 = {t: correlate_valid(delayed_5(X_5, t), W_5, s=2) for t in (0, 1, 4)}
N_OUT_6 = -(-365 // 3)                                                                        # M21.6: ⌈365/3⌉
TOTAL_6 = max((N_OUT_6 - 1) * 3 + 6 + 1 - 365, 0)                                             # zeros in all
ZEROS_6 = [TOTAL_6 // 2, TOTAL_6 - TOTAL_6 // 2]
assert (365 + TOTAL_6 - 6 - 1) // 3 + 1 == N_OUT_6
LENGTHS_6 = [n for n in range(1, 400) if count_positions(n, 5, s=5) == 50]
STEPS_6 = [s for s in range(1, 1000) if count_positions(1000, 7, s=s) == 125]
assert len(STEPS_6) == 1
STEP_6 = STEPS_6[0]
X_7 = [5, 1, 8, -2, 0, 4, 7]                                                                  # M21.7
D3_7 = np.eye(len(X_7), dtype=int)[::3]                                                       # (D₃ x)_i = x_{3i}
Y_7, W_7, S_7 = [3, 2, -2], [2, 1, 3, -1, 1], 3
M_7, K_7 = len(Y_7), len(W_7)


def strided_matrix_7(w, n, s):
    """The matrix C of the sliding sum of weights w, step s, valid mode, on signals of length n."""
    C = np.zeros((count_positions(n, len(w), s=s), n), dtype=int)
    for i in range(len(C)):
        C[i, s * i:s * i + len(w)] = w
    return C


LENGTHS_7 = [n for n in range(1, 50) if count_positions(n, K_7, s=S_7) == M_7]               # m positions
SIZE_7 = LENGTHS_7[0]                                                                         # p_out = 0
C_7 = strided_matrix_7(W_7, SIZE_7, S_7)
TRANSPOSED_7 = C_7.T @ Y_7                                                                    # the matrix Cᵀ (definition)
STAMPS_7 = strided_matrix_7([1] * K_7, SIZE_7, S_7).T @ np.ones(M_7, dtype=int)
SIZE_OUT_7 = (M_7 - 1) * S_7 - 2 * 0 + 1 * (K_7 - 1) + 1 + 2                                 # p_out = 2 (fiche §5)
assert SIZE_OUT_7 == LENGTHS_7[2]
LONG_7 = strided_matrix_7([1] * 12, (20 - 1) * 4 + 12, 4).T @ np.ones(20, dtype=int)         # k = 12, s = 4
assert len(set(LONG_7[11:(20 - 1) * 4 + 1].tolist())) == 1                                    # constant inside
INTERIOR_7 = int(LONG_7[len(LONG_7) // 2])
T_8 = np.array([[14, 15, 17, 16, 15, 13], [15, 18, 21, 19, 12, 14],                         # M21.8
                [16, 20, 24, 22, 17, 15], [15, 17, 19, 18, 16, 14]])
LAPLACIAN_8 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
A_8 = [Fraction(1, 5), Fraction(3, 5), Fraction(1, 5)]
LAP_8 = correlate2d_valid(T_8, LAPLACIAN_8)
VERTICAL_8 = correlate2d_valid(T_8, [[a] for a in A_8])                                       # each column by a
SMOOTH_8 = correlate2d_valid(VERTICAL_8, [A_8])                                               # then each row
assert np.array_equal(SMOOTH_8, correlate2d_valid(T_8, [[a * b for b in A_8] for a in A_8]))


def output_8(flat):
    """The [i, j] in the output of a flat index of LAP_8."""
    return [int(v) for v in np.unravel_index(flat, LAP_8.shape)]


def cell_8(flat):
    """The [i, j] in T of the centre of the window of the output LAP_8.flat[flat]."""
    return [v + 1 for v in output_8(flat)]


H_9, W_9, C_IN_9, C_OUT_9, K_9, P_9, BYTES_9 = 200, 300, 12, 20, 5, 2, 4                     # M21.9
OUT_H_9, OUT_W_9 = count_positions(H_9, K_9, p=P_9), count_positions(W_9, K_9, p=P_9)


def params_9(c_in, c_out, k, g=1):
    """The parameters of a filtering with g groups: c_out (c_in/g k k + 1)."""
    return c_out * (c_in // g * k * k + 1)


def macs_9(c_in, c_out, k, g=1):
    """One multiply-accumulate per weight and per output position (step 1, padding P_9)."""
    return count_positions(H_9, k, p=P_9) * count_positions(W_9, k, p=P_9) * c_out * (c_in // g) * k * k


A_10, B_10 = [Fraction(1, 2)] * 2, [Fraction(1, 3)] * 3                                       # M21.10
X_10 = [5, 9, 2, 8, 4, 10, 1]


def stack_kernel_10(kernels, strides, length=120):
    """The equivalent kernel of a stack of sliding sums, read on impulses: K[t] = z[0] for x = e_t (exact)."""
    def first_output(x):
        for w, s in zip(kernels, strides):
            x = correlate_valid(x, w, s)
        return x[0]
    return [first_output([Fraction(int(i == t)) for i in range(length)]) for t in range(length)]


def trimmed(kernel):
    """The kernel without its trailing zeros (the impulses beyond the receptive field)."""
    last = max(t for t, v in enumerate(kernel) if v != 0)
    return kernel[:last + 1]


def receptive_field_10(stack):
    """r = 1 + Σ d(k − 1) s_1 ... s_{ℓ−1}, by the recurrence r += d (k − 1) J, J *= s."""
    r, J = 1, 1
    for k, s, d in stack:
        r, J = r + d * (k - 1) * J, J * s
    return r


Z_10 = correlate_valid(correlate_valid(X_10, A_10), B_10)
STACK_10 = [(2, 2, 1), (5, 4, 1), (3, 1, 4)]                                                  # (k, s, d)
R_10, S_10 = receptive_field_10(STACK_10), math.prod(s for k, s, d in STACK_10)
HOLED_10 = [[1, 1], [1] * 5, [1, 0, 0, 0, 1, 0, 0, 0, 1]]                                    # the dilation as holes
assert len(trimmed(stack_kernel_10(HOLED_10, [s for k, s, d in STACK_10]))) == R_10        # read on impulses
G_11, EPS_11 = [-2, 5, 1, -3, 1], 0.25                                                        # M21.11
L1_11, L2_11, LINF_11 = sum(map(abs, G_11)), math.sqrt(sum(g * g for g in G_11)), max(map(abs, G_11))
WORST_INF_11 = max(sum(g * e for g, e in zip(G_11, signs)) for signs in product((-EPS_11, EPS_11), repeat=5))
assert math.isclose(WORST_INF_11, EPS_11 * L1_11)                                             # the 32 corners
DELTA_11 = [EPS_11 * float(np.sign(g)) for g in G_11]
WORST_ONE_11 = max(sign * EPS_11 * g for g in G_11 for sign in (-1, 1))                      # the 10 vertices ± ε eᵢ
G_H_11 = [0.02 * (-1) ** i for i in range(2500)]                                              # n = 2 500, ± 0.02
L1_H_11, L2_H_11 = sum(map(abs, G_H_11)), math.sqrt(sum(g * g for g in G_H_11))
X_17 = np.array([[[2, 1, 0, 3, 1], [0, 4, 2, 1, 3], [1, 2, 5, 0, 2], [3, 0, 1, 2, 4]],      # M21.17: (C, H, W)
                 [[1, 0, 2, 2, 0], [3, 1, 0, 4, 1], [2, 2, 1, 0, 3], [0, 1, 3, 1, 2]],
                 [[0, 2, 1, 1, 4], [1, 0, 3, 2, 0], [4, 1, 0, 2, 1], [2, 3, 1, 0, 1]]])
W_17 = np.array([[[[1, 0], [2, -1]], [[0, 1], [-1, 0]], [[2, 0], [1, 1]]],                  # (C_out, C_in, k, k)
                 [[[0, -1], [1, 0]], [[1, 1], [0, 0]], [[-1, 0], [0, 2]]]])
B_17 = np.array([1, -2])


def filter_17(X, W, b):
    """The sliding sum of the libraries on channels, valid mode: Y[o] = b[o] + Σ_c X[c] ⋆ W[o, c]."""
    return np.array([b[o] + sum(correlate2d_valid(X[c], W[o, c]) for c in range(len(X))) for o in range(len(W))])


Y_17 = filter_17(X_17, W_17, B_17)
FLIPPED_17 = filter_17(X_17, W_17[:, :, ::-1, ::-1], B_17)                                  # both axes flipped
KERNEL_2D_17 = W_17[0, 0, ::-1, ::-1]                                                         # a half turn
assert np.array_equal(scipy.signal.convolve2d(X_17[0], KERNEL_2D_17, "valid"), correlate2d_valid(X_17[0], W_17[0, 0]))
X1D_17, W1D_17 = [4, 1, 3, 2, 5], [1, 4]                                                      # y_i = x_i + 4 x_{i+1}
TORCH_SAME_17 = correlate_valid(X1D_17 + [0], W1D_17)                                         # one zero on the right
NUMPY_SAME_17 = np.convolve(X1D_17, [4, 1], "same").tolist()'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M21.1 à M21.11, 🔗 M21.17)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une liste `[0.2, -1]` ; une matrice comme la liste de ses **lignes**, `[[1, 0], [-2, 3]]`, un "
               "nombre décimal s'y écrivant avec un point ;\n"
               "- une **forme** comme un tuple, `(7, 2)`, ou comme un texte, `\"(7, 2)\"` ;\n"
               "- une fraction irréductible entre guillemets, `\"3/7\"`, quand la question le dit ;\n"
               "- `True` ou `False` pour un vrai ou faux.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M21.19 to M21.23)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to D)
import itertools
import math
import re
import time
from fractions import Fraction

import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg
import scipy.signal

from wbm.errors import MymathMissingError
from wbm.nbtools import StopCheck, checked, drawn, filled, run_pytest_group, same, verdict

TEST_M21 = "tests/test_m21_convolution.py"            # the tests of mymath/convolution.py


def shown(value, digits=4):
    """A short text for a result of the learner's code (the check messages): numbers rounded, as lists."""
    if value is None:
        return "None"
    try:
        if isinstance(value, tuple):
            return "(" + ", ".join(str(np.round(np.asarray(v, dtype=float), digits).tolist()) for v in value) + ")"
        return str(np.round(np.asarray(value, dtype=float), digits).tolist())
    except (TypeError, ValueError):
        return repr(value)[:120]'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M21")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/convolution.py`, lis la "
         "docstring du module puis celle de la fonction, remplace chaque `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "⚠️ Le squelette n'importe rien : ajoute `import numpy as np` en tête du fichier (et `import numbers` si tu "
         "t'en sers). Ni `np.convolve`, ni `np.correlate`, ni `np.polymul`, ni `np.polynomial`, ni `np.fft`, aucune "
         "fonction de SciPy, et, de `np.linalg`, seulement `svd`, dans `separable_factors` : les tests comparent tes "
         "résultats aux leurs, et un test lit ton module. Les suites et les matrices se rendent en tableaux NumPy de "
         "flottants, les entiers en `int` de Python ; ne modifie jamais les tableaux reçus.")

REMINDER = ("> Même mode d'emploi qu'en M21.19 : écris la fonction dans ta copie `mon_travail/mymath/convolution.py`, "
            "**enregistre**, puis exécute les cellules ci-dessous ; la première recharge ta librairie.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of convolution.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group(TEST_M21, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_M21, "{keyword}", impl="ref")')]


NOTE_19 = (r"La convolution pleine par une boucle sur $\mathbf{b}$ (chaque $b_j$ ajoute $b_j\,\mathbf{a}$ à partir de "
           r"la case $j$), puis les lignes du mode. a) Trois dés à 8 faces totalisent 11 avec la probabilité "
           r"$\frac{42}{512} = \frac{21}{256}$ : la loi d'un dé, $(0, \frac18, \ldots, \frac18)$, convoluée deux fois "
           r"avec elle-même, l'indice étant la somme (sans la case 0, l'indice $m$ serait le total $m + 3$) ; le calcul "
           r"en flottants est exact, car $\frac18$ est une puissance de 2. b) Le coefficient de $X^5$ dans $(2 - X)^7$ vaut $\binom75 \times 2^2 \times (-1)^5 = "
           r"-84$. c) La première valeur du mode même taille vaut $\frac{8 + 10 + 13}{5} = 6{,}2$ : deux des cinq "
           r"termes sont des zéros, alors que la première moyenne complète vaut 12. d) 8 valeurs sur 12 sont des "
           r"moyennes de 5 vraies mesures, les $12 - 5 + 1$ du mode valide ; les deux premières et les deux dernières "
           r"sont tirées vers 0 par les zéros ajoutés.")

NOTE_20 = (r"La colonne $j$ reçoit le noyau à partir de la ligne $j$, puis on garde les lignes du mode, les mêmes que "
           r"`convolve`. a) Pour $(1, -3, 2)$ et $n = 6$, les rangs valent $[6, 4]$ : la matrice pleine, de forme "
           r"$(8, 6)$, est injective ; la valide, de forme $(4, 6)$, a un noyau de dimension 2 (les signaux constants "
           r"et géométriques de raison 2, comme en M21.4). b) $\frac{7 \times 1\,000}{1\,006 \times 1\,000} \approx "
           r"0{,}696$ % de coefficients non nuls. c) $[\text{vrai}, \text{faux}, \text{vrai}]$ : la transposée de la "
           r"matrice valide est la matrice pleine du noyau retourné ; en mode même taille, c'est vrai pour $k = 5$, "
           r"faux pour $k = 4$, où le zéro en trop change de côté.")

NOTE_21 = (r"Pour chaque $i$, ajouter $a_i$ fois $\mathbf{b}$ décalé circulairement de $i$ cases. a) La température "
           r"lissée à 0 h vaut $\frac{9 + 9 + 8}{3} \approx 8{,}6667$ °C : l'heure 23 entre dans la moyenne, le "
           r"profil est circulaire. b) Le maximum lissé est à 14 h, $\frac{20 + 21 + 20}{3} \approx 20{,}33$ °C. "
           r"c) Vrai : complétées jusqu'à $4 + 3 - 1 = 6$ valeurs, les suites ne se replient pas. d) $[\text{vrai}, "
           r"\text{faux}]$ : $\check{\mathbf{h}} = (5, 4, 1, 3, 0, -2)$ donne la transposée, pas le renversement "
           r"$(4, 1, 3, 0, -2, 5)$, qui n'en est qu'un décalage circulaire.")

NOTE_22 = (r"La décomposition en valeurs singulières, le test $s_2 \le \text{tol} \cdot s_1$, puis $\mathbf{v}$, le "
           r"premier vecteur singulier à droite (sa première coordonnée nettement non nulle rendue positive), et "
           r"$\mathbf{u} = \mathbf{K}\mathbf{v}$. a) Pour le lissage de M21.8, $\mathbf{v} = \frac{1}{\sqrt{11}}(1, 3, "
           r"1) \approx (0{,}3015 ;\ 0{,}9045 ;\ 0{,}3015)$ et $\mathbf{u} = \frac{\sqrt{11}}{25}(1, 3, 1)$. b) $0{,}500$ : "
           r"la moyenne en croix a pour valeurs singulières $\frac25$, $\frac15$ et 0 (rang 2), bien loin de la "
           r"tolérance, et ta fonction rend `None`. c) Le noyau bruité a pour valeurs singulières $19{,}08$, $1{,}3 \cdot 10^{-3}$ "
           r"et $1{,}0 \cdot 10^{-3}$ : rejeté avec la tolérance $10^{-10}$, accepté avec $10^{-2}$ ; l'erreur de "
           r"l'approximation de rang 1 vaut $0{,}00166 = \sqrt{s_2^2 + s_3^2}$ (Eckart-Young, M12d).")

NOTE_23 = (r"$\mathbf{K} \leftarrow \mathbf{K} * (\mathbf{w}_\ell$ dilaté de $S)$, puis $S \leftarrow S\,s_\ell$, en "
           r"partant de $\mathbf{K} = (1)$ et $S = 1$. a) $6\,\mathbf{K} = (1, 1, 0, 1, 1, 0, 1, 1)$ avec $S = 3$, "
           r"comme M21.10 c) et d) : le second étage lit une valeur sur 3 du premier. b) Quatre étages de noyaux de longueur 4 et de pas 2 : $[46, 16]$, soit $1 + 3(1 + 2 + 4 "
           r"+ 8) = 46$ (∂ M21.15). c) Le troisième étage écrit avec ses trous, $(w_0, 0, 0, 0, w_1, 0, 0, 0, w_2)$, "
           r"donne un noyau de 74 coefficients, le champ récepteur de M21.10 e) ; avec des poids égaux à 1, 44 d'entre "
           r"eux sont nuls : les trous de la plage (seuls trois blocs de 10 cases comptent). d) Vrai : la pile de noyaux de longueurs 3, 4 et 2 et de pas 2, 3 et "
           r"1 a un noyau de 15 coefficients et un pas de 6 ; sur les 31 positions de la pile, l'écart est de l'ordre "
           r"de $10^{-16}$.")

GIVEN_19 = '''TEMPERATURES_19 = np.array([8.0, 10, 13, 15, 14, 12, 11, 9, 7, 6, 8, 10])     # 12 daily temperatures (°C)
AVERAGE_19 = np.full(5, 0.2)                                                  # the moving average over 5 days'''

M21_19 = Ex(
    "M21.19", "🔨", 2, 30, "La convolution de deux suites, dans les trois modes · `convolve`",
    "programmer la convolution des mathématiciens dans les trois modes, puis s'en servir pour la loi d'une somme de "
    "dés, une puissance d'un polynôme et une moyenne mobile.",
    "fiche §1 et §2 ; R3, R5, M02b", tracks="C, E", mymath="convolution.py", given=GIVEN_19, note=NOTE_19,
    body=HOWTO + r"""

Écris `convolve(a, b, mode="full")` (fiche §1 et §2), en suivant sa docstring : la convolution des mathématiciens, $(\mathbf{a} * \mathbf{b})_m = \sum_i a_i\,b_{m-i}$, qui retourne le noyau, comme `np.convolve`. Le mode `"full"` rend les $n + m - 1$ valeurs ; `"valid"` les indices $\min(n, m) - 1$ à $\max(n, m) - 1$ de la convolution pleine ; `"same"` ses $\max(n, m)$ valeurs à partir de l'indice $\big\lfloor\frac{\min(n, m) - 1}{2}\big\rfloor$ (la convention de NumPy). Un tableau de flottants ; `ValueError` pour une suite qui n'est pas à une dimension ou qui est vide, ou un mode inconnu.

**L'usage.** Avec ta fonction :
- `law_19` : la loi de la somme de trois dés équilibrés à 8 faces, numérotées de 1 à 8, lancés indépendamment, rangée par **valeur de la somme** : un dé est la suite $(0, \frac18, \ldots, \frac18)$ de 9 termes (la case 0, de probabilité 0, puis les faces 1 à 8), et la loi de la somme, convoluée trois fois, a 25 termes, l'indice étant la somme (de 0 à 24) ;
- a) la probabilité que les trois dés totalisent 11, en fraction irréductible (`"p/q"` ; la valeur flottante de `law_19[11]`, exacte ici, est aussi acceptée) ;
- b) le coefficient de $X^5$ dans $(2 - X)^7$, par sept convolutions successives (les coefficients d'un polynôme rangés du terme constant au terme de plus haut degré) ;
- c) la première valeur du mode même taille de la moyenne mobile sur 5 jours (`AVERAGE_19`, cinq valeurs égales à 0,2) des températures `TEMPERATURES_19` (la valeur que donne le calcul, sans l'arrondir) ;
- d) le nombre de valeurs de ce mode même taille qui sont des moyennes de 5 vraies mesures.

La vérification compare aussi `law_19` à la loi calculée par `np.convolve`. Dans ta copie : pourquoi la case 0 du dé fait-elle de l'indice la valeur de la somme ? Quelles valeurs du mode même taille sont tirées vers 0 par les zéros ajoutés, et pourquoi ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_convolve_ or test_module_uses_") + [
        ("md", "**L'usage** : la loi d'une somme de dés, une puissance d'un polynôme, une moyenne mobile et ses bords."),
        ("todo", '''law_19 = answer_M21_19a = answer_M21_19b = answer_M21_19c = answer_M21_19d = ...
with wbm.attempt("M21.19"):          # if you call convolve here: ⏳ while it is not written
    law_19 = ...          # the 25 probabilities of the sum of three 8-sided dice, the index being the sum (0 to 24)
    answer_M21_19a = ...  # a) P(sum = 11): an irreducible fraction "p/q" (or the exact float law_19[11])
    answer_M21_19b = ...  # b) an integer: the coefficient of X^5 in (2 - X)^7, by seven successive convolutions
    answer_M21_19c = ...  # c) a number, as computed (not rounded): the first value of the "same" mode of the average
    answer_M21_19d = ...  # d) an integer: how many values of this "same" mode are averages of 5 true measures'''),
        ("check", '''with checked("M21.19"):
    if filled(law_19):
        die_c19 = np.r_[0.0, np.full(8, 1 / 8)]
        same("M21.19", "law_19, la loi de la somme de trois dés à 8 faces (indice = somme)", law_19,
             np.convolve(np.convolve(die_c19, die_c19), die_c19))
    else:
        print("⏳ Ex M21.19 : la comparaison attend ton tableau law_19.")
for letter, answer in zip("abc", [answer_M21_19a, answer_M21_19b, answer_M21_19c]):
    wbm.check(f"M21.19{letter}", answer, computed=True)
wbm.check("M21.19d", answer_M21_19d)'''),
        ("solution", '''convolve = mymath.convolution.convolve
die_19 = np.r_[0.0, np.full(8, 1 / 8)]                     # index = the face: the case 0, then 1/8 eight times
law_19 = convolve(convolve(die_19, die_19), die_19)        # index = the sum of the three dice
answer_M21_19a = str(Fraction(float(law_19[11])).limit_denominator(10_000))
power_19 = np.array([1.0])
for _ in range(7):
    power_19 = convolve(power_19, [2.0, -1.0])            # the coefficients of (2 - X)^k, constant term first
answer_M21_19b = int(round(power_19[5]))
same_19 = convolve(TEMPERATURES_19, AVERAGE_19, "same")
answer_M21_19c = float(same_19[0])
answer_M21_19d = len(convolve(TEMPERATURES_19, AVERAGE_19, "valid"))
print("a)", answer_M21_19a, "=", float(law_19[11]), "; somme des 25 probabilités :", law_19.sum())
print("b) (2 − X)⁷ :", np.round(power_19).astype(int).tolist(), "→", answer_M21_19b)
print("mode même taille :", np.round(same_19, 2).tolist())
print("mode valide :     ", np.round(convolve(TEMPERATURES_19, AVERAGE_19, "valid"), 2).tolist())
print("c)", round(answer_M21_19c, 4), " d)", answer_M21_19d)'''),
        ("record", '''counts_19r = [sum(sum(faces) == total for faces in itertools.product(range(1, 9), repeat=3)) for total in range(25)]
wbm.record("M21.19a", str(Fraction(counts_19r[11], 8 ** 3)), kind="fraction", simplified=True,
           mistakes={"chaque dé commence à la face 1 : l'indice d'une valeur de la convolution n'est pas le total":
                         str(Fraction(counts_19r[11 + 3], 8 ** 3)),
                     "avec la case 0 de chaque dé, l'indice de la loi est la somme elle-même : il n'y a rien à "
                     "décaler": str(Fraction(counts_19r[11 - 3], 8 ** 3))})
coefficients_19r = [math.comb(7, j) * 2 ** (7 - j) * (-1) ** j for j in range(8)]    # (2 - X)^7, constant term first
wbm.record("M21.19b", coefficients_19r[5],
           mistakes={"le terme en X⁵ de (2 − X)⁷ porte le signe de (−1)⁵": -coefficients_19r[5],
                     "dans (a + b)ⁿ, le terme en bʲ a le facteur aⁿ⁻ʲ : ici a = 2 et b = −X":
                         math.comb(7, 5) * 2 ** 5 * (-1) ** 5,
                     "la liste des coefficients commence par le terme constant : le coefficient de X⁵ est à l'indice 5":
                         coefficients_19r[2]})
temperatures_19r = [8, 10, 13, 15, 14, 12, 11, 9, 7, 6, 8, 10]
full_19r = np.convolve(temperatures_19r, [0.2] * 5)                          # NumPy, the oracle
wbm.record("M21.19c", float(full_19r[(5 - 1) // 2]), decimals=2,
           mistakes={"c'est la première moyenne COMPLÈTE (mode valide) ; le mode même taille commence plus tôt, avec "
                     "des zéros": float(full_19r[5 - 1]),
                     "c'est la première valeur du mode PLEIN : le mode même taille commence à l'indice ⌊(k − 1)/2⌋ de "
                     "la convolution pleine": float(full_19r[0])})
wbm.record("M21.19d", len(temperatures_19r) - 5 + 1,
           mistakes={"compte seulement les valeurs dont les 5 termes sont de vraies mesures": len(temperatures_19r),
                     "le mode même taille a autant de valeurs que le signal ; compte celles qui ne touchent aucun zéro "
                     "ajouté": len(full_19r)})'''),
    ],
)

GIVEN_20 = '''W4_20 = np.array([1.0, -3.0, 2.0])                                  # the kernel of M21.4
W7_20 = np.array([4.0, -2.0, 1.0, 3.0, -1.0, 2.0, 5.0])                 # a kernel of 7 non-zero coefficients
W_EVEN_20 = np.array([1.0, 4.0, -2.0, 3.0])                              # k = 4
W_ODD_20 = np.array([2.0, 0.0, -1.0, 5.0, 1.0])                          # k = 5'''

M21_20 = Ex(
    "M21.20", "🔨", 2, 25, "La matrice de Toeplitz d'une convolution · `toeplitz_matrix`",
    "programmer la matrice de Toeplitz d'une convolution, puis lire ses rangs, sa proportion de coefficients non nuls "
    "et sa transposée.",
    "fiche §3 ; M12a ; Ex M21.4", tracks="C, E", mymath="convolution.py", given=GIVEN_20, note=NOTE_20,
    body=REMINDER + r"""

Écris `toeplitz_matrix(kernel, n, mode="full")` (fiche §3), en suivant sa docstring : la matrice $\mathbf{T}$ de $\mathbf{x} \mapsto$ `convolve(x, kernel, mode)` pour $\mathbf{x}$ de longueur $n$. En mode plein, sa colonne $j$ est le noyau descendu de $j$ lignes, $T_{ij} = w_{i-j}$, de forme $(n + k - 1, n)$ ; les autres modes gardent les mêmes lignes que `convolve` ($n - k + 1$ en mode valide, $n$ en mode même taille, qui demandent $n \ge k$). Un tableau de flottants ; `ValueError` pour un noyau qui n'est pas à une dimension ou qui est vide, un $n$ qui n'est pas un entier $\ge 1$ (un booléen est refusé), $n < k$ en modes valide et même taille, ou un mode inconnu.

**L'usage.** La cellule fournie donne le noyau $(1, -3, 2)$ de M21.4 (`W4_20`), un noyau de 7 coefficients non nuls (`W7_20`), et deux noyaux pour l'énoncé de la transposée (fiche §3) : $\mathbf{w} = (1, 4, -2, 3)$, de longueur paire (`W_EVEN_20`), et $(2, 0, -1, 5, 1)$, de longueur impaire (`W_ODD_20`). Avec ta fonction :
- a) les rangs des matrices pleine et valide de `W4_20` pour $n = 6$, dans cet ordre (`np.linalg.matrix_rank` ; une liste de 2 entiers) ;
- b) le pourcentage de coefficients non nuls de la matrice pleine de `W7_20` pour $n = 1\,000$ (la valeur que donne le calcul, sans l'arrondir) ;
- c) trois vrai ou faux, dans cet ordre (`np.array_equal`) : la transposée de la matrice valide de `W_EVEN_20` pour $n = 7$ est la matrice pleine de son noyau retourné $\tilde{\mathbf{w}}$ (pour $n = 4$) ; la transposée de sa matrice même taille ($n = 7$) est la matrice même taille de $\tilde{\mathbf{w}}$ ($n = 7$) ; la même chose que la deuxième pour `W_ODD_20`.

Dans ta copie : quels signaux la matrice valide de a) ne voit-elle pas ? Que devient le pourcentage de b) quand $n$ double ? Pour c), pourquoi la transposition échange-t-elle valide et plein, et pourquoi ne garde-t-elle le mode même taille que pour un noyau de longueur impaire ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_toeplitz_matrix_") + [
        ("md", "**L'usage** : des rangs, une matrice creuse, et l'énoncé de la transposée."),
        ("todo", '''answer_M21_20a = answer_M21_20b = answer_M21_20c = ...
with wbm.attempt("M21.20"):          # if you call toeplitz_matrix here: ⏳ while it is not written
    answer_M21_20a = ...  # a) a list of 2 integers: the ranks of the full, then valid, matrix of W4_20 (n = 6)
    answer_M21_20b = ...  # b) a number, as computed (not rounded): the % of non-zero entries, full matrix of W7_20, n = 1000
    answer_M21_20c = ...  # c) a list of 3 True or False: valid (W_EVEN_20) vs full; same vs same (W_EVEN_20); same vs same (W_ODD_20)'''),
        ("check", '''for letter, answer in zip("abc", [answer_M21_20a, answer_M21_20b, answer_M21_20c]):
    wbm.check(f"M21.20{letter}", answer, computed=True)'''),
        ("solution", '''toeplitz_matrix = mymath.convolution.toeplitz_matrix
answer_M21_20a = [int(np.linalg.matrix_rank(toeplitz_matrix(W4_20, 6, mode))) for mode in ("full", "valid")]
T7_20 = toeplitz_matrix(W7_20, 1000)
answer_M21_20b = 100 * np.count_nonzero(T7_20) / T7_20.size
answer_M21_20c = [bool(np.array_equal(toeplitz_matrix(W_EVEN_20, 7, "valid").T, toeplitz_matrix(W_EVEN_20[::-1], 4))),
                  bool(np.array_equal(toeplitz_matrix(W_EVEN_20, 7, "same").T,
                                      toeplitz_matrix(W_EVEN_20[::-1], 7, "same"))),
                  bool(np.array_equal(toeplitz_matrix(W_ODD_20, 7, "same").T,
                                      toeplitz_matrix(W_ODD_20[::-1], 7, "same")))]
print("a)", answer_M21_20a, "; formes :", toeplitz_matrix(W4_20, 6).shape, toeplitz_matrix(W4_20, 6, "valid").shape)
print("b)", round(answer_M21_20b, 4), "% ; forme", T7_20.shape, "; non nuls :", np.count_nonzero(T7_20))
print("c)", answer_M21_20c)
print("même taille, k = 4 : Tᵀ =\\n", toeplitz_matrix(W_EVEN_20, 7, "same").T.astype(int))
print("même taille de w retourné :\\n", toeplitz_matrix(W_EVEN_20[::-1], 7, "same").astype(int))'''),
        ("record", '''def toeplitz_20r(kernel, n, mode="full"):
    """The matrix of x ↦ np.convolve(x, kernel, mode), built column by column (the oracle: NumPy)."""
    return np.column_stack([np.convolve(np.eye(n)[j], kernel, mode) for j in range(n)])


ranks_20r = [int(np.linalg.matrix_rank(toeplitz_20r([1, -3, 2], 6, mode))) for mode in ("full", "valid")]
wbm.record("M21.20a", ranks_20r,
           mistakes={"une matrice de 4 lignes a un rang d'au plus 4": [ranks_20r[0], ranks_20r[0]],
                     "dans l'ordre : la matrice pleine, puis la valide": ranks_20r[::-1]})
full_20r = toeplitz_20r([4, -2, 1, 3, -1, 2, 5], 1000)
wbm.record("M21.20b", 100 * np.count_nonzero(full_20r) / full_20r.size, decimals=3,
           mistakes={"le nombre de lignes de la matrice pleine est n + k − 1": 100 * 7 / 1000,
                     "le pourcentage des coefficients NON NULS": 100 - 100 * np.count_nonzero(full_20r) / full_20r.size})
even_20r, odd_20r = [1, 4, -2, 3], [2, 0, -1, 5, 1]
truths_20r = [bool(np.array_equal(toeplitz_20r(even_20r, 7, "valid").T, toeplitz_20r(even_20r[::-1], 4))),
              bool(np.array_equal(toeplitz_20r(even_20r, 7, "same").T, toeplitz_20r(even_20r[::-1], 7, "same"))),
              bool(np.array_equal(toeplitz_20r(odd_20r, 7, "same").T, toeplitz_20r(odd_20r[::-1], 7, "same")))]
wbm.record("M21.20c", truths_20r,
           mistakes={"compare les deux matrices du mode même taille pour le noyau de longueur paire : le zéro en trop "
                     "change de côté": [True, True, True],
                     "la transposée de la matrice valide (signaux de longueur n) agit sur des signaux de longueur "
                     "n − k + 1 : compare-la à la matrice pleine du noyau retourné pour ce n-là":
                         [False, truths_20r[1], truths_20r[2]]})'''),
    ],
)

GIVEN_21 = '''PROFILE_21 = np.array([9.0, 8, 8, 7, 6, 7, 8, 10, 12, 14, 16, 17,
                       19, 20, 21, 20, 18, 16, 14, 13, 12, 11, 10, 9])   # °C, from 0 h to 23 h; hour 24 is hour 0
H_21 = np.zeros(24)
H_21[[0, 1, 23]] = 1 / 3                                     # the centred circular average over 3 hours
A_21, B_21 = np.array([3.0, -1.0, 2.0, 5.0]), np.array([1.0, 2.0, -2.0])
HC_21 = np.array([5.0, -2.0, 0.0, 3.0, 1.0, 4.0])'''

M21_21 = Ex(
    "M21.21", "🔨", 1, 20, "La convolution circulaire · `circular_convolve`",
    "programmer la convolution circulaire, puis lisser un profil journalier périodique et vérifier la transposée "
    "d'une matrice circulante.",
    "fiche §4", tracks="C", mymath="convolution.py", given=GIVEN_21, note=NOTE_21,
    body=REMINDER + r"""

Écris `circular_convolve(a, b)` (fiche §4), en suivant sa docstring : la convolution circulaire de deux suites de même longueur $n$, $(\mathbf{a} \circledast \mathbf{b})_m = \sum_i a_i\,b_{(m-i) \bmod n}$, les indices lus modulo $n$. Un tableau de flottants ; `ValueError` pour une suite qui n'est pas à une dimension ou qui est vide, ou deux longueurs différentes.

**L'usage.** La cellule fournie donne le profil moyen d'une journée, une température (°C) par heure de 0 h à 23 h (`PROFILE_21`) ; l'heure 24 est l'heure 0. On le lisse par la moyenne circulaire centrée sur 3 heures, le noyau $\mathbf{h}$ de 24 valeurs nulles sauf $h_0 = h_1 = h_{23} = \frac13$ (`H_21`). Avec ta fonction :
- `smooth_21` : les 24 températures lissées, la convolution circulaire de `PROFILE_21` par `H_21` ;
- a) la valeur lissée à 0 h (la valeur que donne le calcul, sans l'arrondir) ;
- b) l'heure du maximum lissé (un entier) ;
- c) vrai ou faux : en complétant $(3, -1, 2, 5)$ et $(1, 2, -2)$ (`A_21`, `B_21`) par des zéros jusqu'à la longueur 6, la convolution circulaire donne la convolution pleine (compare à ta `convolve`) ;
- d) pour $\mathbf{h} = (5, -2, 0, 3, 1, 4)$ (`HC_21`), en construisant $\operatorname{circ}(\mathbf{h})$ colonne par colonne avec ta fonction (la colonne $j$ est la convolution circulaire du $j$-ième vecteur de la base canonique par $\mathbf{h}$) : deux vrai ou faux, dans cet ordre, $\operatorname{circ}(\mathbf{h})^\top = \operatorname{circ}(\check{\mathbf{h}})$, puis $\operatorname{circ}(\mathbf{h})^\top$ égale la matrice circulante du simple renversement de $\mathbf{h}$.

La vérification compare aussi `smooth_21` au produit de la matrice circulante de SciPy par le profil. Dans ta copie : quelles heures entrent dans la valeur lissée de 0 h, et que donnerait une convolution ordinaire en mode même taille ? Écris $\check{\mathbf{h}}$, et le renversement de $\mathbf{h}$ : de combien de cases sont-ils décalés ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_circular_convolve_") + [
        ("md", "**L'usage** : lisser un profil périodique, éviter le repliement, et la transposée d'une matrice "
               "circulante."),
        ("todo", '''smooth_21 = answer_M21_21a = answer_M21_21b = answer_M21_21c = answer_M21_21d = ...
with wbm.attempt("M21.21"):          # if you call circular_convolve here: ⏳ while it is not written
    smooth_21 = ...       # the 24 smoothed temperatures: the circular convolution of PROFILE_21 by H_21
    answer_M21_21a = ...  # a) a number, as computed (not rounded): the smoothed value at 0 h
    answer_M21_21b = ...  # b) an integer: the hour of the largest smoothed value
    answer_M21_21c = ...  # c) True or False: A_21 and B_21 padded with zeros to length 6, circular = full convolution
    answer_M21_21d = ...  # d) a list of 2 True or False: circ(h)ᵀ = circ(ȟ), then circ(h)ᵀ = circ(h reversed)'''),
        ("check", '''with checked("M21.21"):
    if filled(smooth_21):
        same("M21.21", "smooth_21, comparé à scipy.linalg.circulant(H_21) @ PROFILE_21", smooth_21,
             scipy.linalg.circulant(H_21) @ PROFILE_21)
    else:
        print("⏳ Ex M21.21 : la comparaison attend ton tableau smooth_21.")
for letter, answer in zip("abcd", [answer_M21_21a, answer_M21_21b, answer_M21_21c, answer_M21_21d]):
    wbm.check(f"M21.21{letter}", answer, computed=True)'''),
        ("solution", '''circular_convolve = mymath.convolution.circular_convolve
convolve = mymath.convolution.convolve
smooth_21 = circular_convolve(PROFILE_21, H_21)
answer_M21_21a = float(smooth_21[0])
answer_M21_21b = int(np.argmax(smooth_21))
length_21 = len(A_21) + len(B_21) - 1                          # 6: nothing wraps around
answer_M21_21c = bool(np.allclose(circular_convolve(np.r_[A_21, np.zeros(length_21 - len(A_21))],
                                                    np.r_[B_21, np.zeros(length_21 - len(B_21))]),
                                  convolve(A_21, B_21)))


def circulant_21(h):
    """circ(h), column by column: column j is the circular convolution of e_j by h."""
    h = np.asarray(h, dtype=float)
    return np.column_stack([circular_convolve(np.eye(len(h))[j], h) for j in range(len(h))])


check_h_21 = HC_21[(-np.arange(len(HC_21))) % len(HC_21)]   # ȟ = (h0, h5, h4, ..., h1)
answer_M21_21d = [bool(np.allclose(circulant_21(HC_21).T, circulant_21(check_h_21))),
                  bool(np.allclose(circulant_21(HC_21).T, circulant_21(HC_21[::-1])))]
print("a)", round(answer_M21_21a, 4), " b)", answer_M21_21b, "h, valeur", round(float(smooth_21.max()), 4))
print("mode même taille d'une convolution ordinaire, à 0 h :", round(float(convolve(PROFILE_21, [1 / 3] * 3, "same")[0]), 4))
print("c)", answer_M21_21c, " d)", answer_M21_21d, "; ȟ =", check_h_21.tolist(), "; renversement :", HC_21[::-1].tolist())'''),
        ("record", '''profile_21r = [9, 8, 8, 7, 6, 7, 8, 10, 12, 14, 16, 17, 19, 20, 21, 20, 18, 16, 14, 13, 12, 11, 10, 9]
smooth_21r = [(profile_21r[t - 1] + profile_21r[t] + profile_21r[(t + 1) % 24]) / 3 for t in range(24)]
wbm.record("M21.21a", smooth_21r[0], decimals=4,
           mistakes={"la moyenne est CENTRÉE : h₂₃ = 1/3 fait entrer, dans la valeur de chaque heure, l'heure "
                     "précédente (modulo 24)": sum(profile_21r[:3]) / 3,
                     "le profil est circulaire : une convolution ordinaire met un zéro avant 0 h, au lieu de l'heure 23":
                         sum(profile_21r[:2]) / 3})
wbm.record("M21.21b", int(np.argmax(smooth_21r)),
           mistakes={"la moyenne est centrée : la valeur lissée de l'heure m lit les heures m − 1, m et m + 1, pas trois "
                     "heures d'un même côté": {int(np.argmax(smooth_21r)) - 1, int(np.argmax(smooth_21r)) + 1}})
padded_21r = np.zeros((2, 6))
padded_21r[0, :4], padded_21r[1, :3] = [3, -1, 2, 5], [1, 2, -2]
wbm.record("M21.21c", bool(np.allclose(np.fft.ifft(np.fft.fft(padded_21r[0]) * np.fft.fft(padded_21r[1])).real,
                                       np.convolve([3, -1, 2, 5], [1, 2, -2]))),
           mistakes={"complétées jusqu'à la longueur n + k − 1, les suites ne se replient plus : compare au résultat de "
                     "convolve": False})
h_21r = np.array([5, -2, 0, 3, 1, 4])
circ_21r = scipy.linalg.circulant(h_21r)                              # first column h, entries h[(i − j) mod n]
wbm.record("M21.21d", [bool(np.array_equal(circ_21r.T, scipy.linalg.circulant(h_21r[(-np.arange(6)) % 6]))),
                       bool(np.array_equal(circ_21r.T, scipy.linalg.circulant(h_21r[::-1])))],
           mistakes={"le simple renversement ne garde pas h₀ à sa place : compare les deux matrices": [True, True],
                     "relis le théorème du §4 : le retourné circulaire garde h₀ à sa place": [False, True]})'''),
    ],
)

GIVEN_22 = '''A8_22 = np.array([1.0, 3.0, 1.0]) / 5
K8_22 = np.outer(A8_22, A8_22)                                       # the smoothing kernel of M21.8
CROSS_22 = np.array([[0.0, 1, 0], [1, 1, 1], [0, 1, 0]]) / 5         # the mean over a cross of five cells
NOISY_22 = (np.outer([1.0, 2.0, 4.0, 2.0, 1.0], [2.0, -1.0, 3.0])
            + 1e-3 * np.random.default_rng(5532).standard_normal((5, 3)))   # nearly separable'''

M21_22 = Ex(
    "M21.22", "🔨", 2, 25, "Reconnaître un noyau séparable et le factoriser · `separable_factors`",
    "programmer la factorisation d'un noyau de rang 1 par la décomposition en valeurs singulières, et voir ce qu'en "
    "dit Eckart-Young sur un noyau presque séparable.",
    "fiche §6 ; M12d ; Ex M21.8", tracks="C", mymath="convolution.py", given=GIVEN_22, note=NOTE_22,
    body=REMINDER + r"""

Écris `separable_factors(kernel, tol=1e-10)` (fiche §6), en suivant sa docstring : par la décomposition en valeurs singulières (M12d, `np.linalg.svd`, la seule fonction de `np.linalg` permise, ici seulement), le noyau est séparable quand sa deuxième valeur singulière vaut au plus `tol` fois la première ; alors $\mathbf{v}$ est le premier vecteur singulier à droite, de norme 1, sa première coordonnée de valeur absolue $> 10^{-8}$ rendue positive, et $\mathbf{u} = \mathbf{K}\mathbf{v}$ ; sinon, `None`. `ValueError` pour un noyau qui n'est pas à deux dimensions, vide ou identiquement nul, ou une tolérance négative.

**L'usage.** La cellule fournie donne le lissage $\mathbf{K} = \mathbf{a}\mathbf{a}^\top$ de M21.8, avec $\mathbf{a} = \frac15(1, 3, 1)$ (`K8_22`), la moyenne en croix $\frac15\begin{pmatrix} 0 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 0 \end{pmatrix}$ (`CROSS_22`), et un noyau presque séparable, le produit extérieur de $(1, 2, 4, 2, 1)$ et de $(2, -1, 3)$ plus un bruit gaussien d'écart type 0,001 (`NOISY_22`, graine 5532). Avec ta fonction :
- a) le facteur $\mathbf{v}$ de `K8_22` (une liste de 3 nombres, la valeur que donne le calcul, sans l'arrondir) ;
- b) le rapport $s_2/s_1$ des valeurs singulières de `CROSS_22` (`np.linalg.svd` ; la valeur que donne le calcul, sans l'arrondir), et `factors_cross_22`, ce que rend ta fonction pour ce noyau ;
- `factors_default_22`, ce que rend ta fonction pour `NOISY_22` avec la tolérance par défaut, et `factors_loose_22`, avec une tolérance de $10^{-2}$ ;
- c) l'erreur $\lVert\mathbf{K} - \mathbf{u}\mathbf{v}^\top\rVert_F$ de l'approximation de rang 1 donnée par `factors_loose_22` (`np.linalg.norm` ; la valeur que donne le calcul, sans l'arrondir).

La vérification regarde aussi que `factors_cross_22` et `factors_default_22` valent `None`, que `factors_loose_22` est un couple de facteurs, et compare c) à $\sqrt{s_2^2 + s_3^2}$, calculé par NumPy. Dans ta copie : que vaut $\mathbf{u}$ en a) ? Quelles sont les valeurs singulières de la moyenne en croix, et pourquoi son rang vaut-il 2 ? Pourquoi c) vaut-il $\sqrt{s_2^2 + s_3^2}$ (Eckart-Young, M12d) ? Quel rapport $\frac{s_2}{s_1}$ sépare les deux tolérances ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_separable_factors_") + [
        ("md", "**L'usage** : un noyau séparable, un noyau qui ne l'est pas, et un noyau presque séparable."),
        ("todo", '''answer_M21_22a = answer_M21_22b = answer_M21_22c = ...
factors_cross_22 = factors_default_22 = factors_loose_22 = ...
with wbm.attempt("M21.22"):          # if you call separable_factors here: ⏳ while it is not written
    answer_M21_22a = ...      # a) a list of 3 numbers, as computed (not rounded): the factor v of K8_22
    answer_M21_22b = ...      # b) a number, as computed: s2 / s1 for CROSS_22 (np.linalg.svd)
    factors_cross_22 = ...    # what separable_factors(CROSS_22) returns
    factors_default_22 = ...  # separable_factors(NOISY_22), with the default tolerance
    factors_loose_22 = ...    # separable_factors(NOISY_22, tol=1e-2)
    answer_M21_22c = ...      # c) a number, as computed: the Frobenius norm of NOISY_22 - outer(u, v), (u, v) = factors_loose_22'''),
        ("check", '''for letter, answer in zip("abc", [answer_M21_22a, answer_M21_22b, answer_M21_22c]):
    wbm.check(f"M21.22{letter}", answer, computed=True)
if factors_cross_22 is not ...:                           # None is the right answer here: not filled() (None = ⏳)
    verdict("M21.22", factors_cross_22 is None, "la moyenne en croix, de rang 2, n'est pas séparable : None.",
            "la moyenne en croix est de rang 2 (s₂ n'est pas petit devant s₁) : ta fonction doit rendre None.")
if factors_default_22 is not ...:
    verdict("M21.22", factors_default_22 is None, "avec la tolérance par défaut, NOISY_22 n'est pas séparable.",
            "avec la tolérance par défaut (1e-10), NOISY_22 a s₂ trop grand devant s₁ : ta fonction doit rendre None.")
if filled(factors_loose_22):
    verdict("M21.22", isinstance(factors_loose_22, tuple) and len(factors_loose_22) == 2,
            "avec la tolérance 1e-2, NOISY_22 est accepté : un couple (u, v).",
            "avec la tolérance 1e-2, ta fonction doit rendre le couple (u, v).")
if filled(answer_M21_22c):
    singular_c22 = np.linalg.svd(NOISY_22, compute_uv=False)
    verdict("M21.22", abs(answer_M21_22c - math.sqrt(np.sum(singular_c22[1:] ** 2))) < 1e-12,
            "l'erreur vaut √(s₂² + s₃²), comme le dit Eckart-Young.",
            "l'erreur de la meilleure approximation de rang 1 doit valoir √(s₂² + s₃²) : relis tes facteurs.")'''),
        ("solution", '''separable_factors = mymath.convolution.separable_factors
u_22, v_22 = separable_factors(K8_22)
answer_M21_22a = v_22.tolist()
singular_cross_22 = np.linalg.svd(CROSS_22, compute_uv=False)
answer_M21_22b = float(singular_cross_22[1] / singular_cross_22[0])
factors_cross_22 = separable_factors(CROSS_22)
factors_default_22 = separable_factors(NOISY_22)
factors_loose_22 = separable_factors(NOISY_22, tol=1e-2)
answer_M21_22c = float(np.linalg.norm(NOISY_22 - np.outer(*factors_loose_22)))
singular_22 = np.linalg.svd(NOISY_22, compute_uv=False)
print("a) v =", np.round(v_22, 4).tolist(), "; u =", np.round(u_22, 4).tolist(), "; √11/25 =", round(math.sqrt(11) / 25, 4))
print("b)", round(answer_M21_22b, 6), "; valeurs singulières de la moyenne en croix :",
      np.round(singular_cross_22, 6).tolist(), "; separable_factors :", factors_cross_22)
print("NOISY_22 : s =", [f"{s:.3e}" for s in singular_22], "; s₂/s₁ =", f"{singular_22[1] / singular_22[0]:.2e}")
print("tolérance par défaut :", factors_default_22, "; tolérance 1e-2 : deux facteurs")
print("c)", f"{answer_M21_22c:.6f}", "; √(s₂² + s₃²) =", f"{math.sqrt(np.sum(singular_22[1:] ** 2)):.6f}")'''),
        ("record", '''v_22r = np.array([1.0, 3.0, 1.0]) / math.sqrt(11)                    # (1, 3, 1), of norm 1
wbm.record("M21.22a", v_22r.tolist(), decimals=4,
           mistakes={"la convention de signe rend positive la première coordonnée nettement non nulle de v":
                         (-v_22r).tolist(),
                     "v est de norme 1": (np.array([1.0, 3.0, 1.0]) / 5).tolist(),
                     "c'est u = K v ; la question demande le facteur v, de norme 1":
                         (np.outer([1, 3, 1], [1, 3, 1]) / 25 @ v_22r).tolist()})
s_cross_22r = np.linalg.svd(np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]) / 5, compute_uv=False)
assert np.allclose(s_cross_22r, [2 / 5, 1 / 5, 0])                     # the eigenvalues 2/5, −1/5 and 0, in absolute value
wbm.record("M21.22b", float(s_cross_22r[1] / s_cross_22r[0]), decimals=3,
           mistakes={"s₁ est la plus grande valeur singulière : le rapport s₂/s₁ est au plus 1":
                         float(s_cross_22r[0] / s_cross_22r[1]),
                     "s₂ est la deuxième valeur singulière, en ordre décroissant ; 0 est la troisième":
                         round(float(s_cross_22r[2] / s_cross_22r[0]), 12)})
noisy_22r = (np.outer([1.0, 2.0, 4.0, 2.0, 1.0], [2.0, -1.0, 3.0])
             + 1e-3 * np.random.default_rng(5532).standard_normal((5, 3)))
s_22r = np.linalg.svd(noisy_22r, compute_uv=False)
wbm.record("M21.22c", math.sqrt(s_22r[1] ** 2 + s_22r[2] ** 2), decimals=5,
           mistakes={"l'erreur en norme de Frobenius garde TOUTES les valeurs singulières oubliées": s_22r[1]})'''),
    ],
)

GIVEN_23 = '''rng_23 = np.random.default_rng(5533)
KERNELS_23 = [rng_23.standard_normal(k) for k in (3, 4, 2)]     # a random stack: kernels of lengths 3, 4 and 2
STRIDES_23 = [2, 3, 1]                                         # and steps 2, 3 and 1
X_23 = rng_23.standard_normal(200)                             # a signal of 200 values'''

CHECK_23 = '''with checked("M21.23"):
    rng_c23 = np.random.default_rng(5523)
    wrong_23 = []
    for n_c23, k_c23, s_c23 in ((17, 4, 3), (12, 1, 2), (9, 9, 4), (20, 3, 1)):
        x_c23, w_c23 = rng_c23.standard_normal(n_c23), rng_c23.standard_normal(k_c23)
        want_c23 = np.correlate(x_c23, w_c23, "valid")[::s_c23]
        got_c23 = strided_sum(x_c23.copy(), w_c23.copy(), s_c23)
        if got_c23 is None or np.shape(got_c23) != want_c23.shape or not np.allclose(got_c23, want_c23):
            wrong_23.append(f"n = {n_c23}, k = {k_c23}, s = {s_c23} : attendu {np.round(want_c23, 4).tolist()}, "
                            f"reçu {shown(got_c23)}"[:260])
    verdict("M21.23", not wrong_23, "strided_sum : juste sur quatre cas que tu ne vois pas (noyaux de longueur 1 à 9).",
            "strided_sum, " + " ; ".join(wrong_23[:2]))
    if wrong_23:
        raise StopCheck
    if filled(stack_23, direct_23):
        want_stack_23 = X_23
        for w_c23, s_c23 in zip(KERNELS_23, STRIDES_23):
            want_stack_23 = np.correlate(want_stack_23, w_c23, "valid")[::s_c23]
        same("M21.23", "stack_23, la pile appliquée étage par étage", stack_23, want_stack_23)
        common_23 = min(len(stack_23), len(direct_23))
        same("M21.23", "direct_23, le noyau équivalent et le pas total (positions communes)",
             np.asarray(direct_23, dtype=float)[:common_23], want_stack_23[:common_23])
    else:
        print("⏳ Ex M21.23 : la comparaison attend tes tableaux stack_23 et direct_23.")'''

M21_23 = Ex(
    "M21.23", "🔨", 2, 30, "Le noyau équivalent et le pas d'une pile de sommes glissantes · `equivalent_kernel`",
    "programmer le noyau équivalent et le pas total d'une pile de sommes glissantes, et le vérifier en appliquant la "
    "pile étage par étage.",
    "fiche §7 ; Ex M21.10 et M21.19", tracks="C, E", mymath="convolution.py", given=GIVEN_23, note=NOTE_23,
    body=REMINDER + r"""

Écris `equivalent_kernel(kernels, strides=None)` (fiche §7), en suivant sa docstring, avec ta `convolve` : l'étage $\ell$ calcule la somme glissante des bibliothèques $y_i = \sum_u w_{\ell,u}\,x_{s_\ell i + u}$ (sans retournement ni padding), et toute la pile est une seule somme glissante $z_j = \sum_t K_t\,x_{Sj+t}$, de pas $S = s_1 \cdots s_L$. En partant de $\mathbf{K} = (1)$ et $S = 1$, chaque étage remplace $\mathbf{K}$ par sa convolution avec $\mathbf{w}_\ell$ **dilaté** de $S$ ($S - 1$ zéros entre deux coefficients), puis $S$ par $S\,s_\ell$. Le couple `(K, S)` : un tableau de flottants, de longueur $1 + \sum_\ell (k_\ell - 1)\,s_1 \cdots s_{\ell-1}$ (zéros compris), et un `int` ; `ValueError` sans noyau, pour un noyau qui n'est pas à une dimension ou qui est vide, ou des pas qui ne sont pas $L$ entiers $\ge 1$.

**L'usage.** Écris aussi `strided_sum(x, w, s)`, la somme glissante de pas $s$ en mode valide, avec ta `convolve` (une somme glissante est une convolution valide par le noyau retourné, dont on garde une valeur sur $s$). La cellule fournie tire (graine 5533) une pile de trois étages, de noyaux de longueurs 3, 4 et 2 (`KERNELS_23`) et de pas 2, 3 et 1 (`STRIDES_23`), et un signal de 200 valeurs (`X_23`). Avec tes fonctions :
- a) $6\,\mathbf{K}$ pour la pile de M21.10 c) : $\frac12(1, 1)$ avec un pas de 3, puis $\frac13(1, 1, 1)$ avec un pas de 1 (une liste de nombres, la valeur que donne le calcul) ;
- b) la longueur du noyau équivalent et le pas total de quatre étages identiques, de noyaux de longueur 4 et de pas 2 (une liste de 2 entiers) ;
- c) le champ récepteur de la pile de M21.10 e), $(k, s, d) = (2, 2, 1)$, $(5, 4, 1)$, $(3, 1, 4)$, en écrivant le troisième étage, dilaté, comme le noyau à trous $(w_0, 0, 0, 0, w_1, 0, 0, 0, w_2)$ (un entier : la longueur du noyau équivalent) ;
- `stack_23` : `X_23` passé dans les trois étages, l'un après l'autre, par `strided_sum` ; `direct_23` : `X_23` passé dans la seule somme glissante du noyau équivalent, avec le pas total ;
- d) vrai ou faux : `stack_23` et `direct_23` coïncident à $10^{-12}$ près sur leurs positions communes (`np.allclose(..., rtol=0, atol=1e-12)`).

La vérification essaie aussi `strided_sum` sur des cas que tu ne vois pas, et compare `stack_23` et `direct_23` à la pile calculée par `np.correlate`. Dans ta copie : pourquoi le noyau de c) a-t-il des coefficients nuls, et pourquoi faut-il les garder ? Combien de positions ont `stack_23` et `direct_23`, et pourquoi la seconde peut-elle en avoir plus ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_equivalent_kernel_") + [
        ("md", "**L'usage** : trois piles, et une pile tirée au hasard, appliquée de deux façons."),
        ("todo", '''def strided_sum(x, w, s=1):
    """The sliding sum of the libraries with the step s, valid mode: y[i] = Σ_u w[u] x[s i + u] for every i whose
    window fits (with your convolve)."""
    raise NotImplementedError("strided_sum n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M21_23a = answer_M21_23b = answer_M21_23c = answer_M21_23d = stack_23 = direct_23 = ...
with wbm.attempt("M21.23"):          # equivalent_kernel and strided_sum: ⏳ while they are not written
    answer_M21_23a = ...  # a) a list of numbers, as computed: 6 K for (1, 1)/2 with a step 3, then (1, 1, 1)/3 with a step 1
    answer_M21_23b = ...  # b) a list of 2 integers: [len(K), S] for four stages of kernels of length 4 and step 2
    answer_M21_23c = ...  # c) an integer: len(K) for the stack of M21.10 e), its third stage written with its holes
    stack_23 = ...        # X_23 through the three stages of KERNELS_23 and STRIDES_23, one after the other
    direct_23 = ...       # X_23 through the single sliding sum of the equivalent kernel, with the total step
    answer_M21_23d = ...  # d) True or False: they coincide to 1e-12 on their common positions'''),
        ("check", '''for letter, answer in zip("abcd", [answer_M21_23a, answer_M21_23b, answer_M21_23c, answer_M21_23d]):
    wbm.check(f"M21.23{letter}", answer, computed=True)

''' + CHECK_23),
        ("solution", '''equivalent_kernel = mymath.convolution.equivalent_kernel
convolve = mymath.convolution.convolve


def strided_sum(x, w, s=1):
    """The sliding sum of the libraries with the step s, valid mode: y[i] = Σ_u w[u] x[s i + u] for every i whose
    window fits (with your convolve)."""
    return convolve(x, np.asarray(w, dtype=float)[::-1], "valid")[::s]      # flip, keep one value in s


K_a23, S_a23 = equivalent_kernel([[0.5, 0.5], [1 / 3, 1 / 3, 1 / 3]], strides=[3, 1])
answer_M21_23a = (6 * K_a23).tolist()
K_b23, S_b23 = equivalent_kernel([[1.0, 1.0, 1.0, 1.0]] * 4, strides=[2] * 4)
answer_M21_23b = [len(K_b23), S_b23]
K_c23, S_c23 = equivalent_kernel([[1.0, 1.0], [1.0] * 5, [1.0, 0, 0, 0, 1.0, 0, 0, 0, 1.0]], strides=[2, 4, 1])
answer_M21_23c = len(K_c23)
stack_23 = X_23
for w_23, s_23 in zip(KERNELS_23, STRIDES_23):
    stack_23 = strided_sum(stack_23, w_23, s_23)
K_d23, S_d23 = equivalent_kernel(KERNELS_23, STRIDES_23)
direct_23 = strided_sum(X_23, K_d23, S_d23)
common_23 = min(len(stack_23), len(direct_23))
answer_M21_23d = bool(np.allclose(stack_23[:common_23], direct_23[:common_23], rtol=0, atol=1e-12))
print("a) 6K =", np.round(6 * K_a23, 12).tolist(), "; S =", S_a23)
print("b)", answer_M21_23b, "; 1 + 3 (1 + 2 + 4 + 8) =", 1 + 3 * (1 + 2 + 4 + 8))
print("c)", answer_M21_23c, "; S =", S_c23, "; coefficients nuls :", int(np.sum(K_c23 == 0)))
print("d)", answer_M21_23d, "; noyau de", len(K_d23), "coefficients, pas", S_d23, "; positions :", len(stack_23), "et",
      len(direct_23), "; plus grand écart :", f"{np.max(np.abs(stack_23[:common_23] - direct_23[:common_23])):.1e}")'''),
        ("record", '''def stack_kernel_23r(kernels, strides, length=120):
    """K[t] = z[0] for x = e_t: the stack applied to impulses (np.correlate, the oracle), without the trailing zeros."""
    def first_output(x):
        for w, s in zip(kernels, strides):
            x = np.correlate(x, w, "valid")[::s]
        return x[0]
    kernel = [first_output(np.eye(length)[t]) for t in range(length)]
    return kernel[:max(t for t, v in enumerate(kernel) if v != 0) + 1]


def receptive_field_23r(stack):
    """r = 1 + Σ d (k − 1) s_1 ... s_{ℓ−1}, by the recurrence of the fiche."""
    r, J = 1, 1
    for k, s, d in stack:
        r, J = r + d * (k - 1) * J, J * s
    return r


wbm.record("M21.23a", np.round(6 * np.array(stack_kernel_23r([[0.5, 0.5], [1 / 3] * 3], [3, 1])), 9).tolist(),
           mistakes={"le pas du premier étage dilate le noyau du second":
                         np.round(6 * np.array(stack_kernel_23r([[0.5, 0.5], [1 / 3] * 3], [1, 1])), 9).tolist(),
                     "le noyau du second étage est dilaté du pas du premier étage, s₁":
                         np.round(6 * np.array(stack_kernel_23r([[0.5, 0.5], [1 / 3] * 3], [2, 1])), 9).tolist()})
wbm.record("M21.23b", [receptive_field_23r([(4, 2, 1)] * 4), 2 ** 4],
           mistakes={"un pas multiplie les contributions des étages SUIVANTS": [1 + 4 * 3, 2 ** 4],
                     "le pas total est le PRODUIT des pas": [receptive_field_23r([(4, 2, 1)] * 4), 4 * 2]})
wbm.record("M21.23c", receptive_field_23r([(2, 2, 1), (5, 4, 1), (3, 1, 4)]),
           mistakes={"écris le troisième étage avec ses trous : d − 1 zéros entre deux poids":
                         receptive_field_23r([(2, 2, 1), (5, 4, 1), (3, 1, 1)])})
wbm.record("M21.23d", True,
           mistakes={"si tes fonctions passent leurs vérifications, compare les deux sorties sur leurs positions "
                     "communes, par np.allclose(..., rtol=0, atol=1e-12)": False})'''),
    ],
)

PART_A = Part("A", "Ta librairie : la convolution, sa matrice, la convolution circulaire, les noyaux séparables et "
                   "le noyau équivalent",
              "Fiche §1 à §4, §6 et §7. Les cinq fonctions de `mymath/convolution.py`, leurs tests, et un usage de "
              "chacune.",
              given=TOOLS, exercises=[M21_19, M21_20, M21_21, M21_22, M21_23])

# ---------------------------------------------------------------------------
# Notebook exercises: predict, measure, draw (M21.24 to M21.26)
# ---------------------------------------------------------------------------
NOTE_24 = (r"La sortie d'origine vaut $(0, 0, 7, -1, 0, \ldots)$ : la fenêtre 2 lit $x_6, \ldots, x_9 = (0, 2, 5, -1)$, "
           r"d'où $0 - 2 + 10 - 1 = 7$. a) Pour $t = 3$, la sortie est décalée d'une position ; b) pour $t = 6$, de "
           r"deux. c) et d) Faux : $t = 1$ donne $(0, 0, 9, 6, 0, \ldots)$ et $t = 2$ donne $(0, 0, 2, -5, 0, "
           r"\ldots)$, d'autres nombres. e) $(0, 0, 9, 6, 0, 0, 0, 0, 0)$ : la fenêtre 2 lit $(0, 0, 2, 5)$, d'où "
           r"$4 + 5 = 9$, et la fenêtre 3 lit $(5, -1, 0, 0)$, d'où $5 + 1 = 6$. Avec un pas $s$, seuls les décalages "
           r"multiples de $s$ décalent la sortie ; les autres font lire au filtre d'autres paquets de valeurs.")

NOTE_25 = (r"a) $[625, 50]$ multiplications par valeur de sortie pour $k = 25$, selon les comptes de la fiche (en deux "
           r"passes, la passe intermédiaire a un peu plus de valeurs que la sortie). b) (B) : le rapport mesuré pour "
           r"$k = 25$ est de l'ordre de 12 à 17 (il dépend de la machine), proche de $\frac k2 = 12{,}5$ ; pour "
           r"$k = 3$, il n'est que de 1,5 à 2. c) Vrai : l'écart est de l'ordre de $10^{-13}$. Chaque passe est une "
           r"addition de tranches de même taille : le temps suit le nombre de tranches, $k^2$ contre $2k$, et le "
           r"séparable ne vaut la peine qu'à partir de noyaux moyens.")

NOTE_26 = (r"Pour $(5, 2)$ et $(7, 3)$, $s$ ne divise pas $k$ : le long de chaque axe, les cases intérieures sont "
           r"couvertes tantôt par 2, tantôt par 3 tampons, et la carte, produit des deux axes, mélange 4, 6 et 9 : un "
           r"damier. Pour $(6, 2)$ et $(9, 3)$, chaque axe donne 3 partout à l'intérieur, et la carte vaut 9 sur tout "
           r"l'intérieur. Les cartes ont $15 \times 15$, $16 \times 16$, $22 \times 22$ et $24 \times 24$ cases, "
           r"$(m - 1)s + k$ avec $m = 6$ ; les bords reçoivent moins de tampons dans tous les cas.")

GIVEN_24 = '''X_24 = np.zeros(30)
X_24[7:10] = [2.0, 5.0, -1.0]                       # a signal of 30 values, zero except x7, x8 and x9
W_24 = np.array([1.0, -1.0, 2.0, 1.0])              # the weights of the sliding sum
STEP_24 = 3                                          # valid mode: 9 positions'''

EXPERIMENT_24 = '''with checked("M21.24"):
    convolve_24 = mymath.convolution.convolve

    def strided_24(x):
        """The sliding sum of weights W_24 with the step STEP_24: a valid convolution by the flipped kernel, one value
        in STEP_24."""
        return convolve_24(x, W_24[::-1], "valid")[::STEP_24]

    def delayed_24(x, t):
        """x delayed by t places: t zeros enter on the left, the last t values leave on the right."""
        return np.concatenate([np.zeros(t), x[:len(x) - t]])

    def shift_of_24(y, y0):
        """The m ≥ 0 such that y is y0 moved m places to the right, or None."""
        return next((m for m in range(len(y0)) if np.allclose(y[m:], y0[:len(y0) - m]) and np.allclose(y[:m], 0)),
                    None)

    y0_24 = strided_24(X_24)
    for t_24 in (0, 1, 2, 3, 6):
        y_24 = strided_24(delayed_24(X_24, t_24))
        m_24 = shift_of_24(y_24, y0_24)
        print(f"t = {t_24} : {np.round(y_24).astype(int).tolist()}  →  "
              + (f"la sortie d'origine décalée de {m_24} position(s)" if m_24 is not None
                 else "pas un décalage de la sortie d'origine"))'''

M21_24 = Ex(
    "M21.24", "🔮", 1, 15, "Prédire l'effet d'un décalage de l'entrée sur un filtrage avec pas, puis vérifier",
    "prévoir ce qu'un décalage de l'entrée fait à un filtrage avec pas, puis le voir.",
    "fiche §4 et §5 ; Ex M21.19", tracks="C, E", hypothesis=True, given=GIVEN_24, note=NOTE_24,
    body=r"""Un signal de 30 valeurs, nul sauf $x_7 = 2$, $x_8 = 5$ et $x_9 = -1$ (`X_24`), est filtré par la somme glissante de poids $(1, -1, 2, 1)$ (`W_24`) avec un pas de 3, en mode valide : $y_i = \sum_u w_u\,x_{3i+u}$, pour les 9 positions $i = 0, \ldots, 8$. On le retarde de $t$ cases : $t$ zéros entrent à gauche, et les $t$ dernières valeurs sortent à droite. Prédis, **avant d'exécuter quoi que ce soit** :
- a) pour $t = 3$, de combien de positions la sortie est décalée (un entier) ;
- b) la même chose pour $t = 6$ ;
- c) vrai ou faux : pour $t = 1$, la sortie est un décalage de la sortie d'origine ;
- d) la même question pour $t = 2$ ;
- e) les 9 valeurs de la sortie pour $t = 1$, calculées à la main (une liste de 9 entiers).

L'expérience calcule, avec ta `convolve` (une somme glissante est une convolution valide par le noyau retourné, dont on garde une valeur sur 3), la sortie pour $t = 0, 1, 2, 3$ et $6$, et dit pour chacune si c'est un décalage de la sortie d'origine.

Écris tes cinq prédictions, vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M21_24a = ...  # a) an integer, written BEFORE the experiment: for t = 3, by how many positions the output moves
prediction_M21_24b = ...  # b) an integer: the same for t = 6
prediction_M21_24c = ...  # c) True or False: for t = 1, the output is a shift of the original output
prediction_M21_24d = ...  # d) True or False: the same for t = 2
prediction_M21_24e = ...  # e) a list of 9 integers, computed by hand: the output for t = 1''',
    check='''for letter, prediction in zip("abcde", [prediction_M21_24a, prediction_M21_24b, prediction_M21_24c,
                                          prediction_M21_24d, prediction_M21_24e]):
    wbm.check(f"M21.24{letter}", prediction)''',
    record='''def strided_24r(x, w=(1, -1, 2, 1), s=3):
    """y[i] = Σ_u w[u] x[s i + u], valid mode (loops)."""
    return [sum(w[u] * x[s * i + u] for u in range(len(w))) for i in range((len(x) - len(w)) // s + 1)]


def shift_24r(y, y0):
    """The m ≥ 0 such that y is y0 moved m places to the right, or None."""
    return next((m for m in range(len(y0)) if y[m:] == y0[:len(y0) - m] and not any(y[:m])), None)


signal_24r = [0] * 30
signal_24r[7:10] = [2, 5, -1]
outputs_24r = {t: strided_24r([0] * t + signal_24r[:30 - t]) for t in (0, 1, 2, 3, 6)}
wbm.record("M21.24a", shift_24r(outputs_24r[3], outputs_24r[0]), prediction=True,
           mistakes={"la sortie ne garde qu'une valeur sur 3 : compte le décalage en positions de sortie, pas en cases "
                     "du signal": 3})
wbm.record("M21.24b", shift_24r(outputs_24r[6], outputs_24r[0]), prediction=True,
           mistakes={"la sortie ne garde qu'une valeur sur 3 : un décalage de l'entrée se compte, à la sortie, en "
                     "positions de fenêtre": 6})
wbm.record("M21.24c", shift_24r(outputs_24r[1], outputs_24r[0]) is not None, prediction=True,
           mistakes={"relis le §4 : avec un pas s, seuls certains décalages de l'entrée décalent la sortie": True})
wbm.record("M21.24d", shift_24r(outputs_24r[2], outputs_24r[0]) is not None, prediction=True,
           mistakes={"avec un pas s, un décalage de l'entrée décale la sortie seulement s'il est multiple de s": True})
wbm.record("M21.24e", outputs_24r[1], prediction=True,
           mistakes={"un décalage d'une case de l'entrée n'est pas un décalage d'une position de la sortie : recalcule "
                     "chaque fenêtre": [0] + outputs_24r[0][:-1],
                     "c'est la sortie d'origine : avec le signal retardé, chaque fenêtre lit d'autres valeurs":
                         outputs_24r[0]})''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes cinq prédictions écrites."),
        ("todo", guarded(EXPERIMENT_24, [f"prediction_M21_24{letter}" for letter in "abcde"],
                         "⏳ Écris d'abord tes cinq prédictions, puis exécute à nouveau.")),
        ("solution", EXPERIMENT_24),
        ("md", "**Après l'expérience**, dans ta copie : quels décalages de l'entrée décalent la sortie, et de combien ? "
               "Pour $t = 1$, quelles valeurs du signal lit chaque fenêtre ? Que deviendrait l'expérience avec un pas "
               "de 1 ? Pourquoi dit-on qu'un filtrage avec pas n'est équivariant que pour les décalages multiples du "
               "pas ?"),
    ],
)

GIVEN_25 = '''rng_25 = np.random.default_rng(5535)
GRID_25 = rng_25.standard_normal((360, 360))                    # a grid of 360 × 360 random values
KS_25 = [3, 5, 9, 15, 25]
FACTORS_25 = {k: (rng_25.standard_normal(k), rng_25.standard_normal(k)) for k in KS_25}   # K = outer(a, b) for each k


def best_time_25(function, *args, repeat=3):
    """The best of `repeat` runs of function(*args), in seconds (time.perf_counter)."""
    best = math.inf
    for _ in range(repeat):
        start = time.perf_counter()
        function(*args)
        best = min(best, time.perf_counter() - start)
    return best'''

CHECK_25 = '''with checked("M21.25"):
    results_25 = []

    def report_25(ok, success, failure):
        """One ✅ line, or one ❌ line that stops the check there (the figure is shown when it exists)."""
        results_25.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))
        if not ok:
            raise StopCheck

    rng_c25 = np.random.default_rng(5525)
    for name_c25, function_c25 in (("direct_25", direct_25), ("separable_25", separable_25)):
        wrong_c25 = []
        for shape_c25, k_c25 in (((12, 10), 3), ((9, 14), 4), ((8, 8), 8), ((7, 11), 1)):
            X_c25 = rng_c25.standard_normal(shape_c25)
            a_c25, b_c25 = rng_c25.standard_normal(k_c25), rng_c25.standard_normal(k_c25)
            want_c25 = scipy.signal.correlate2d(X_c25, np.outer(a_c25, b_c25), "valid")
            got_c25 = function_c25(X_c25.copy(), a_c25.copy(), b_c25.copy())
            where_c25 = f"une grille {shape_c25[0]} × {shape_c25[1]}, k = {k_c25}"
            if got_c25 is None or np.shape(got_c25) != want_c25.shape:
                wrong_c25.append(f"{where_c25} : attendu la forme {want_c25.shape}, reçu "
                                 + ("None" if got_c25 is None else f"la forme {np.shape(got_c25)}"))
            elif not np.allclose(np.asarray(got_c25, dtype=float), want_c25):
                wrong_c25.append(f"{where_c25} : la bonne forme, mais un écart de "
                                 f"{np.max(np.abs(np.asarray(got_c25, dtype=float) - want_c25)):.3g} avec "
                                 "scipy.signal.correlate2d")
        report_25(not wrong_c25, f"{name_c25} : juste sur quatre grilles que tu ne vois pas (comparé à "
                  "scipy.signal.correlate2d)", f"{name_c25}, " + " ; ".join(wrong_c25[:2]))
    if not filled(direct_times_25, separable_times_25):
        print("⏳ Ex M21.25 : la figure attend tes temps, direct_times_25 et separable_times_25.")
        raise StopCheck
    times_c25 = [np.asarray(times, dtype=float).ravel() for times in (direct_times_25, separable_times_25)]
    report_25(all(t.shape == (len(KS_25),) and np.all(t > 0) for t in times_c25),
              "tes temps : cinq nombres positifs par fonction, un par k de KS_25",
              "direct_times_25 et separable_times_25 doivent avoir un temps positif par k de KS_25")
    fig_25, (ax_time_25, ax_ratio_25) = plt.subplots(1, 2, figsize=(12, 4.2))
    try:
        opened_25 = drawn(draw_costs_25, ax_time_25, ax_ratio_25, list(KS_25), times_c25[0].tolist(),
                          times_c25[1].tolist())

        def through_25(ax, ys):
            """True when one line of ax passes by all the points (k, y) of KS_25 and ys."""
            return any(np.asarray(line.get_xdata(), dtype=float).shape == (len(KS_25),)
                       and np.allclose(np.asarray(line.get_xdata(), dtype=float), KS_25)
                       and np.allclose(np.asarray(line.get_ydata(), dtype=float), ys, rtol=1e-9) for line in ax.lines)

        report_25(not opened_25, "draw_costs_25 dessine dans les axes reçus",
                  "draw_costs_25 doit dessiner dans les deux axes reçus, sans ouvrir de figure")
        report_25(through_25(ax_time_25, times_c25[0]) and through_25(ax_time_25, times_c25[1]),
                  "les deux temps sont tracés contre k", "il manque, dans le premier axe, une courbe des temps contre k "
                  "(une par fonction, une valeur par k de KS_25)")
        report_25(ax_time_25.get_xscale() == "log" and ax_time_25.get_yscale() == "log",
                  "les temps sont en échelles logarithmiques", "mets les deux échelles du premier axe en logarithmique "
                  "(ax.set_xscale(\\"log\\"), ax.set_yscale(\\"log\\"))")
        report_25(through_25(ax_ratio_25, times_c25[0] / times_c25[1]) and through_25(ax_ratio_25, np.array(KS_25) / 2),
                  "le rapport des temps est tracé à côté de k/2", "il manque, dans le second axe, le rapport des temps "
                  "(direct / séparable) contre k, ou la droite k/2")
    except StopCheck:
        plt.show()
        raise
    except BaseException:
        plt.close(fig_25)
        raise
    plt.show()
    verdict("M21.25", all(results_25), "tes deux filtrages sont justes, et leurs coûts sont dessinés.", "")'''

M21_25 = Ex(
    "M21.25", "🔬", 2, 20, "Le coût d'un filtrage direct ou séparable, selon la taille du noyau : mesurer, puis "
    "comparer à k² et 2k",
    "mesurer le coût d'un filtrage direct et d'un filtrage séparable selon la taille du noyau, et le comparer aux "
    "comptes $k^2$ et $2k$ de la fiche.", "fiche §6 ; Ex M21.8", tracks="C", given=GIVEN_25, note=NOTE_25,
    body=r"""Une grille de $360 \times 360$ valeurs tirées au hasard (`GRID_25`, graine 5535) est filtrée, en mode valide, par des noyaux de rang 1, $\mathbf{K} = \mathbf{a}\mathbf{b}^\top$ (fiche §6), de taille $k \times k$ pour $k = 3, 5, 9, 15, 25$ (`KS_25` ; les facteurs $\mathbf{a}$ et $\mathbf{b}$ de chaque $k$ sont dans `FACTORS_25[k]`). Écris :
- `direct_25(X, a, b)` : la somme glissante valide de la grille $\mathbf{X}$ par $\mathbf{K} = \mathbf{a}\mathbf{b}^\top$, qui ajoute les $k^2$ tranches de $\mathbf{X}$ décalées de $(u, v)$, chacune multipliée par $K_{u,v}$ ;
- `separable_25(X, a, b)` : la même chose en deux passes, $k$ tranches le long des colonnes (décalées de $u$ lignes) multipliées par $a_u$, puis $k$ tranches du résultat le long des lignes (décalées de $v$ colonnes) multipliées par $b_v$ ;
- `draw_costs_25(ax_time, ax_ratio, ks, direct_times, separable_times)`, qui dessine dans les deux axes reçus (sans en ouvrir d'autre) : dans `ax_time`, les deux temps contre $k$, une ligne avec des points pour chacun, les deux échelles logarithmiques ; dans `ax_ratio`, le rapport des temps (direct / séparable) contre $k$, et la droite $\frac k2$ ; des légendes et des titres.

Puis mesure, avec `best_time_25` (fournie : le meilleur de 3 essais, `time.perf_counter`), `direct_times_25` et `separable_times_25`, les temps de tes deux fonctions sur `GRID_25`, un par $k$ de `KS_25`. Réponds :
- a) le nombre de multiplications par valeur de sortie pour $k = 25$, selon les comptes de la fiche ($k_hk_w$ en direct, environ $k_h + k_w$ en deux passes), dans cet ordre (une liste de 2 entiers) ;
- b) le rapport mesuré des temps pour $k = 25$ est le plus proche, en ordre de grandeur (sur une échelle logarithmique), de : (A) 2 ; (B) 12,5 ; (C) 625 (une lettre) ;
- c) vrai ou faux : pour $k = 25$, les deux sorties coïncident à $10^{-9}$ près (`np.allclose(..., rtol=0, atol=1e-9)`).

La vérification essaie tes deux filtrages sur des grilles que tu ne vois pas (comparés à `scipy.signal.correlate2d`), puis appelle `draw_costs_25` et regarde le dessin, en s'arrêtant au premier ❌. (La transformée de Fourier, qui accélère encore les très grands noyaux, n'est qu'évoquée dans la fiche, §4.)""",
    todo='''def direct_25(X, a, b):
    """The valid sliding sum of the grid X by the k × k kernel K = outer(a, b): the sum of the k² slices of X shifted
    by (u, v), each multiplied by K[u, v]."""
    raise NotImplementedError("direct_25 n'est pas encore écrite (04_indices.md si tu bloques)")


def separable_25(X, a, b):
    """The same in two passes: k slices along the columns (shifted by u rows) multiplied by a[u], then k slices of
    the result along the rows (shifted by v columns) multiplied by b[v]."""
    raise NotImplementedError("separable_25 n'est pas encore écrite (04_indices.md si tu bloques)")


def draw_costs_25(ax_time, ax_ratio, ks, direct_times, separable_times):
    """In ax_time: the two times against k (one line with points each), both scales logarithmic; in ax_ratio: the
    ratio direct / separable against k, and the line k / 2. No other axes."""
    raise NotImplementedError("draw_costs_25 n'est pas encore écrite (04_indices.md si tu bloques)")


direct_times_25 = separable_times_25 = answer_M21_25a = answer_M21_25b = answer_M21_25c = ...
with wbm.attempt("M21.25"):          # your functions: ⏳ while they are not written
    direct_times_25 = ...     # the 5 best times of direct_25 on GRID_25, one per k of KS_25 (best_time_25)
    separable_times_25 = ...  # the same for separable_25
    answer_M21_25a = ...  # a) a list of 2 integers: multiplications per output value for k = 25, direct then two passes
    answer_M21_25b = ...  # b) "A", "B" or "C": your measured ratio for k = 25 is closest, on a log scale, to (A) 2, (B) 12.5, (C) 625
    answer_M21_25c = ...  # c) True or False: for k = 25, the two outputs coincide to 1e-9''',
    check='''wbm.check("M21.25a", answer_M21_25a)
wbm.check("M21.25b", answer_M21_25b)
wbm.check("M21.25c", answer_M21_25c, computed=True)

''' + CHECK_25,
    solution='''def direct_25(X, a, b):
    """The valid sliding sum of the grid X by the k × k kernel K = outer(a, b): the sum of the k² slices of X shifted
    by (u, v), each multiplied by K[u, v]."""
    K = np.outer(a, b)
    rows, cols = X.shape[0] - K.shape[0] + 1, X.shape[1] - K.shape[1] + 1
    out = np.zeros((rows, cols))
    for u in range(K.shape[0]):
        for v in range(K.shape[1]):
            out += K[u, v] * X[u:u + rows, v:v + cols]
    return out


def separable_25(X, a, b):
    """The same in two passes: k slices along the columns (shifted by u rows) multiplied by a[u], then k slices of
    the result along the rows (shifted by v columns) multiplied by b[v]."""
    rows, cols = X.shape[0] - len(a) + 1, X.shape[1] - len(b) + 1
    middle = np.zeros((rows, X.shape[1]))
    for u in range(len(a)):
        middle += a[u] * X[u:u + rows, :]                 # along the columns: k slices
    out = np.zeros((rows, cols))
    for v in range(len(b)):
        out += b[v] * middle[:, v:v + cols]               # then along the rows: k slices
    return out


def draw_costs_25(ax_time, ax_ratio, ks, direct_times, separable_times):
    """In ax_time: the two times against k (one line with points each), both scales logarithmic; in ax_ratio: the
    ratio direct / separable against k, and the line k / 2. No other axes."""
    ks = np.asarray(ks, dtype=float)
    direct, separable = np.asarray(direct_times, dtype=float), np.asarray(separable_times, dtype=float)
    ax_time.plot(ks, direct, "o-", color="C3", label="direct (k² tranches)")
    ax_time.plot(ks, separable, "s-", color="C0", label="séparable (2k tranches)")
    ax_time.set_xscale("log")
    ax_time.set_yscale("log")
    ax_time.set_xticks(ks, [f"{k:g}" for k in ks])
    ax_time.xaxis.set_minor_locator(plt.NullLocator())
    ax_time.set_xlabel("taille du noyau k (échelle log)")
    ax_time.set_ylabel("temps (s, échelle log)")
    ax_time.set_title("filtrage d'une grille 360 × 360 par un noyau k × k de rang 1", fontsize=10)
    ax_time.grid(True, which="both", alpha=0.3)
    ax_time.legend(fontsize=8)
    ax_ratio.plot(ks, direct / separable, "o-", color="C2", label="rapport mesuré (direct / séparable)")
    ax_ratio.plot(ks, ks / 2, "--", color="0.4", label="k/2")
    ax_ratio.set_xscale("log")
    ax_ratio.set_yscale("log")
    ax_ratio.set_xticks(ks, [f"{k:g}" for k in ks])
    ax_ratio.xaxis.set_minor_locator(plt.NullLocator())
    ax_ratio.set_xlabel("taille du noyau k (échelle log)")
    ax_ratio.set_ylabel("rapport des temps (échelle log)")
    ax_ratio.set_title("le gain du séparable, comparé à k/2", fontsize=10)
    ax_ratio.grid(True, which="both", alpha=0.3)
    ax_ratio.legend(fontsize=8)


direct_times_25 = [best_time_25(direct_25, GRID_25, *FACTORS_25[k]) for k in KS_25]
separable_times_25 = [best_time_25(separable_25, GRID_25, *FACTORS_25[k]) for k in KS_25]
answer_M21_25a = [25 * 25, 2 * 25]
ratio_25 = direct_times_25[-1] / separable_times_25[-1]
offered_25 = {"A": 2, "B": 12.5, "C": 625}
answer_M21_25b = min(offered_25, key=lambda letter: abs(math.log(offered_25[letter] / ratio_25)))
a_25, b_25 = FACTORS_25[25]
answer_M21_25c = bool(np.allclose(direct_25(GRID_25, a_25, b_25), separable_25(GRID_25, a_25, b_25), rtol=0, atol=1e-9))
for k_25, t_direct_25, t_separable_25 in zip(KS_25, direct_times_25, separable_times_25):
    print(f"k = {k_25:2d} : direct {1000 * t_direct_25:7.2f} ms, séparable {1000 * t_separable_25:6.2f} ms, rapport "
          f"{t_direct_25 / t_separable_25:5.1f} (k/2 = {k_25 / 2})")
print("a)", answer_M21_25a, " b)", answer_M21_25b, f"(rapport mesuré {ratio_25:.1f})", " c)", answer_M21_25c,
      "; plus grand écart :", f"{np.max(np.abs(direct_25(GRID_25, a_25, b_25) - separable_25(GRID_25, a_25, b_25))):.1e}")

''' + CHECK_25,
    record='''wbm.record("M21.25a", [25 * 25, 25 + 25],
           mistakes={"deux passes de k multiplications chacune": [25 * 25, 25],
                     "dans l'ordre : en direct, puis en deux passes": [25 + 25, 25 * 25]})
wbm.record("M21.25b", "B",
           mistakes={"relis tes deux temps pour k = 25 : le rapport se calcule direct / séparable, et se compare aux "
                     "trois valeurs sur une échelle logarithmique (par leurs rapports, pas par leurs différences)": "A",
                     "625 est le nombre de multiplications du filtrage direct, pas le rapport des temps": "C"})
rng_25r = np.random.default_rng(5535)
grid_25r = rng_25r.standard_normal((360, 360))
a_25r, b_25r = {k: (rng_25r.standard_normal(k), rng_25r.standard_normal(k)) for k in [3, 5, 9, 15, 25]}[25]
two_passes_25r = scipy.signal.correlate2d(scipy.signal.correlate2d(grid_25r, a_25r[:, None], "valid"), b_25r[None, :],
                                          "valid")
wbm.record("M21.25c", bool(np.allclose(scipy.signal.correlate2d(grid_25r, np.outer(a_25r, b_25r), "valid"),
                                       two_passes_25r, rtol=0, atol=1e-9)),
           mistakes={"si tes deux fonctions passent la vérification, compare leurs sorties par np.allclose(..., rtol=0, "
                     "atol=1e-9)": False})''',
    after=[
        ("md", "**Après la figure**, dans ta copie : pourquoi le temps suit-il le nombre de tranches ? Pour quels $k$ "
               "le séparable vaut-il la peine ? Pourquoi la passe intermédiaire a-t-elle un peu plus de valeurs que "
               "la sortie, et que devient le compte « environ $2k$ » pour une très grande grille ? Que ferais-tu pour "
               "un noyau de rang 2 ?"),
    ],
)

GIVEN_26 = '''M_26 = 6                                                   # a 6 × 6 input
PAIRS_26 = [(5, 2), (6, 2), (7, 3), (9, 3)]                # (k, s): k × k kernels, step s along both axes'''

CHECK_26 = '''with checked("M21.26"):
    results_26 = []

    def report_26(ok, success, failure):
        """One ✅ line, or one ❌ line that stops the check there."""
        results_26.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))
        if not ok:
            raise StopCheck

    def stamps_c26(m, k, s):
        """The stamps on each cell of a 1-D transposed convolution, put one by one."""
        counts = np.zeros((m - 1) * s + k, dtype=int)
        for i in range(m):
            counts[s * i:s * i + k] += 1
        return counts

    cases_c26 = [(M_26, k, s) for k, s in PAIRS_26] + [(3, 4, 4), (5, 2, 3), (4, 1, 1), (2, 7, 5)]
    wrong_c26 = []
    for m_c26, k_c26, s_c26 in cases_c26:
        want_c26 = np.outer(stamps_c26(m_c26, k_c26, s_c26), stamps_c26(m_c26, k_c26, s_c26))
        got_c26 = coverage_map_26(m_c26, k_c26, s_c26)
        if got_c26 is None or np.shape(got_c26) != want_c26.shape or not np.array_equal(got_c26, want_c26):
            wrong_c26.append(f"m = {m_c26}, k = {k_c26}, s = {s_c26} : attendu une carte {want_c26.shape}, reçu "
                             + ("None" if got_c26 is None else f"une carte {np.shape(got_c26)}"
                                + (" aux comptes différents" if np.shape(got_c26) == want_c26.shape else "")))
    report_26(not wrong_c26, f"coverage_map_26 : juste sur {len(cases_c26)} cas (tampons posés un par un)",
              "coverage_map_26, " + " ; ".join(wrong_c26[:2]))
    fig_26, axes_26 = plt.subplots(1, len(PAIRS_26), figsize=(16, 3.9))
    try:
        opened_26 = drawn(draw_maps_26, fig_26, list(axes_26), M_26, list(PAIRS_26))
        report_26(not opened_26, "draw_maps_26 dessine dans la figure reçue",
                  "draw_maps_26 doit dessiner dans les axes reçus, sans ouvrir de figure")
        for ax_c26, (k_c26, s_c26) in zip(axes_26, PAIRS_26):
            want_c26 = np.outer(stamps_c26(M_26, k_c26, s_c26), stamps_c26(M_26, k_c26, s_c26))
            images_c26 = [image for image in ax_c26.images if np.shape(image.get_array()) == want_c26.shape
                          and np.array_equal(np.asarray(image.get_array()), want_c26)]
            report_26(images_c26, f"(k, s) = ({k_c26}, {s_c26}) : la carte est dessinée",
                      f"il manque, dans l'axe de (k, s) = ({k_c26}, {s_c26}), l'image de coverage_map_26 "
                      f"({want_c26.shape[0]} × {want_c26.shape[1]} cases ; ax.imshow)")
            report_26(images_c26[0].colorbar is not None, "… avec sa barre de couleurs",
                      f"il manque la barre de couleurs de (k, s) = ({k_c26}, {s_c26}) (fig.colorbar(image, ax=ax))")
            numbers_c26 = [int(n) for n in re.findall(r"\\d+", ax_c26.get_title())]
            report_26(k_c26 in numbers_c26 and s_c26 in numbers_c26, "… et un titre qui donne (k, s)",
                      f"le titre de l'axe de (k, s) = ({k_c26}, {s_c26}) doit donner k et s")
    except StopCheck:
        plt.show()
        raise
    except BaseException:
        plt.close(fig_26)
        raise
    plt.show()
    verdict("M21.26", all(results_26), "les quatre cartes des recouvrements sont dessinées.", "")'''

M21_26 = Ex(
    "M21.26", "🎨", 1, 15, "La carte des recouvrements d'une convolution transposée : un damier ou pas, selon k et s",
    "dessiner, en chaque case de la sortie d'une convolution transposée en deux dimensions, le nombre de tampons qui "
    "la couvrent, et voir quand apparaît un damier.", "fiche §5 ; Ex M21.7", tracks="C, E", given=GIVEN_26,
    note=NOTE_26,
    body=r"""Une convolution transposée de pas $s$ imprime, pour chaque valeur d'entrée $y_i$, un tampon $y_i\,\mathbf{w}$ à partir de la case $s\,i$ (fiche §5) ; une case de la sortie reçoit un tampon de chaque $i$ tel que $0 \le j - s\,i \le k - 1$. En deux dimensions, avec une entrée de $m \times m$ valeurs et des noyaux $k \times k$ de pas $s$ selon les deux axes, le nombre de tampons qui couvrent la case $(j, j')$ est le **produit** des comptes des deux axes. Écris :
- `coverage_26(m, k, s)` : en une dimension, le nombre de tampons qui couvrent chaque case, un tableau d'entiers de longueur $(m - 1)s + k$ ;
- `coverage_map_26(m, k, s)` : la carte en deux dimensions, le tableau des produits des comptes des deux axes ;
- `draw_maps_26(fig, axes, m, pairs)` : une carte par couple $(k, s)$ de `pairs`, dans les axes de `axes`, dans cet ordre : l'image de `coverage_map_26(m, k, s)` (`ax.imshow`), sa barre de couleurs (`fig.colorbar(image, ax=ax)`) et un titre qui donne $(k, s)$ ; sans ouvrir d'autre figure.

La cellule fournie donne $m = 6$ (`M_26`) et les couples $(k, s) = (5, 2)$, $(6, 2)$, $(7, 3)$ et $(9, 3)$ (`PAIRS_26`). La vérification compare ta carte à des tampons posés un par un, sur ces quatre couples et sur des cas que tu ne vois pas, puis appelle `draw_maps_26` et regarde le dessin, en s'arrêtant au premier ❌ : chaque carte, sa barre de couleurs et son titre.""",
    todo='''def coverage_26(m, k, s):
    """The number of stamps that cover each cell of a 1-D transposed convolution: m inputs, a kernel of length k,
    the step s, no padding. A 1-D array of integers, of length (m - 1) s + k."""
    raise NotImplementedError("coverage_26 n'est pas encore écrite (04_indices.md si tu bloques)")


def coverage_map_26(m, k, s):
    """The same for an m × m input, k × k kernels and the step s along both axes: the 2-D array of the products of
    the counts of the two axes."""
    raise NotImplementedError("coverage_map_26 n'est pas encore écrite (04_indices.md si tu bloques)")


def draw_maps_26(fig, axes, m, pairs):
    """One map per (k, s) of pairs, in the axes of `axes` (in this order): the image of coverage_map_26(m, k, s),
    its colour bar and a title that gives (k, s). No other figure."""
    raise NotImplementedError("draw_maps_26 n'est pas encore écrite (04_indices.md si tu bloques)")''',
    check=CHECK_26,
    solution='''def coverage_26(m, k, s):
    """The number of stamps that cover each cell of a 1-D transposed convolution: m inputs, a kernel of length k,
    the step s, no padding. A 1-D array of integers, of length (m - 1) s + k."""
    counts = np.zeros((m - 1) * s + k, dtype=int)
    for i in range(m):
        counts[s * i:s * i + k] += 1                   # the stamp of the input i covers the cells s i to s i + k - 1
    return counts


def coverage_map_26(m, k, s):
    """The same for an m × m input, k × k kernels and the step s along both axes: the 2-D array of the products of
    the counts of the two axes."""
    counts = coverage_26(m, k, s)
    return np.outer(counts, counts)


def draw_maps_26(fig, axes, m, pairs):
    """One map per (k, s) of pairs, in the axes of `axes` (in this order): the image of coverage_map_26(m, k, s),
    its colour bar and a title that gives (k, s). No other figure."""
    for ax, (k, s) in zip(axes, pairs):
        counts = coverage_map_26(m, k, s)
        image = ax.imshow(counts, cmap="viridis", interpolation="nearest")
        fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
        ax.set_title(f"(k, s) = ({k}, {s}) : " + ("uniforme à l'intérieur" if k % s == 0 else "un damier"), fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])


for k_26, s_26 in PAIRS_26:
    counts_26 = coverage_26(M_26, k_26, s_26)
    inside_26 = counts_26[k_26 - 1:(M_26 - 1) * s_26 + 1]
    print(f"(k, s) = ({k_26}, {s_26}) : {len(counts_26)} cases par axe, comptes {counts_26.tolist()} ; à l'intérieur, "
          f"la carte prend les valeurs {sorted(set(np.outer(inside_26, inside_26).ravel().tolist()))}")

''' + CHECK_26,
    after=[
        ("md", "**Après la figure**, dans ta copie : pour quels couples la carte est-elle uniforme à l'intérieur, et "
               "quelle valeur y prend-elle ? Pourquoi un damier apparaît-il quand $s$ ne divise pas $k$ ? Quelles "
               "valeurs prend la carte à l'intérieur pour $(5, 2)$ ? Pourquoi les bords reçoivent-ils moins de "
               "tampons dans tous les cas ?"),
    ],
)

PART_B = Part("B", "Prédire, mesurer, dessiner",
              "Fiche §4 à §6. Un décalage de l'entrée d'un filtrage avec pas, prédit puis vu ; le coût d'un filtrage "
              "direct ou séparable, mesuré ; les recouvrements d'une convolution transposée, dessinés.",
              exercises=[M21_24, M21_25, M21_26])

# ---------------------------------------------------------------------------
# Notebook exercises: debug and test (M21.27, M21.28)
# ---------------------------------------------------------------------------
NOTE_27 = (r"(1) Un produit de polynômes est une convolution : `np.correlate` ne retourne pas son second argument, "
           r"il faut `np.convolve(p, q)`. La vérification du collègue prenait un facteur palindrome, $(2, 5, 2)$, que "
           r"le retournement ne change pas. a) $(1 + 2X)(3 - X + 4X^2) = 3 + 5X + 2X^2 + 8X^3$ ; la version fausse "
           r"rend $(4, 7, 1, 6)$. (2) `k // s` ne vaut que si $s$ divise $k$ : sinon, le nombre de tampons change "
           r"d'une case à l'autre, et il faut compter, pour la case $j$, les $i$ tels que $0 \le j - s\,i \le k - 1$. "
           r"Les trois cas du collègue avaient $s$ qui divise $k$. b) $(3, 3, 2)$ pour les cases 9, 10 et 11 ; la "
           r"carte complète vaut $(1, 1, 1, 2, 2, 2, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 2, 2, 2, 1, 1, 1)$, et la "
           r"version fausse dit 2 partout. (3) Une première colonne et une première ligne ne suffisent que pour un "
           r"noyau de rang 1 (et avec $K_{0,0} \ne 0$) : il faut tester le rang, par exemple avec "
           r"`separable_factors`. c) L'écart maximal vaut 1, en ligne 1, colonne 2 ($5$ contre $6$), sans aucun "
           r"message d'erreur. d) Vrai : le noyau est de rang 2, avec $\frac{s_2}{s_1} \approx 0{,}043$. e) "
           r"$(-18, 6, -17, 11, -22, 7)$, alors que PyTorch donne $(6, -17, 11, -22, 7, 6)$ : les mêmes nombres, "
           r"décalés d'une case.")

NOTE_28 = (r"Le test passe sur la référence (202 cas, 606 appels de `toeplitz_matrix`), et attrape la version fausse "
           r"dès le premier noyau de longueur paire tiré : pour $k$ impair, $\lfloor k/2\rfloor = \lfloor\frac{k-1}{2}"
           r"\rfloor$, et les deux versions coïncident. Son message dit d'abord ce qui était attendu, puis $k$, $n$ et "
           r"le mode. Un test sur des noyaux tous impairs, ou sur les seuls modes plein et valide, ne l'aurait jamais "
           r"vue.")

GIVEN_C = 'ref_conv = wbm.load_mymath("ref", alias="mymath_ref").convolution   # the reference: the check of M21.28'

GIVEN_27 = '''P_27, Q_27 = np.array([1.0, 2.0]), np.array([3.0, -1.0, 4.0])      # (1 + 2X)(3 − X + 4X²)
K_27 = np.array([[2.0, 1.0, 3.0], [4.0, 2.0, 5.0], [2.0, 1.0, 3.0]])
X_27, W_27 = np.array([6.0, 2.0, 7.0, 1.0, 8.0, 3.0]), np.array([2.0, -3.0])


# The colleague's code
def poly_product(p, q):
    """The coefficients of the product of two polynomials, from the constant term to the highest degree."""
    return np.correlate(p, q, "full")


def n_covers(k, s):
    """The number of stamps that cover an inner cell of a transposed convolution: kernel of length k, step s."""
    return k // s


def separate(K):
    """The two factors (u, v) of a separable kernel, K = outer(u, v)."""
    K = np.asarray(K, dtype=float)
    return K[:, 0].copy(), K[0, :] / K[0, 0]


# The colleague's checks: all pass
print("(1) (1 + 2X)(2 + 5X + 2X²) :", poly_product([1, 2], [2, 5, 2]).tolist(), "(attendu [2, 9, 12, 4])")
print("(2) n_covers : (k, s) = (6, 2) →", n_covers(6, 2), "; (9, 3) →", n_covers(9, 3), "; (8, 4) →", n_covers(8, 4),
      "(comptés à la main sur une case intérieure : k/s)")
u_c27, v_c27 = separate(np.outer([1, 2], [3, 1, 2]))
print("(3) un produit extérieur reconstruit :", bool(np.allclose(np.outer(u_c27, v_c27), np.outer([1, 2], [3, 1, 2]))))'''

CHECK_27 = '''results_27, parts_27 = [], []


def report_27(ok, success, failure):
    results_27.append(bool(ok))
    print(("✅ " + success) if ok else ("❌ " + failure))


def call_27(part, name, function, *args):
    """function(*args); an error of the learner's code becomes one ❌ line that names the function (the check of this
    part stops there, the final verdict stays)."""
    try:
        return function(*args)
    except (NotImplementedError, MymathMissingError):
        raise
    except Exception as exc:  # noqa: BLE001 - the learner's error, reported with the name of the function
        report_27(False, "", f"({part}) {name} : ton code lève {type(exc).__name__} : {str(exc)[:200]}")
        parts_27.append(part)
        raise StopCheck from None


rng_c27 = np.random.default_rng(5521)
with checked("M21.27"):                                       # (1) poly_product_fixed
    wrong_27 = []
    for n_c27, m_c27 in ((2, 4), (4, 2), (3, 3), (5, 1), (1, 3)):
        p_c27 = rng_c27.integers(-5, 6, size=n_c27).astype(float)
        q_c27 = rng_c27.integers(-5, 6, size=m_c27).astype(float)
        q_c27[0], q_c27[-1] = 2.0, -3.0 if m_c27 > 1 else 2.0         # never a palindrome
        want_c27 = np.array([sum(p_c27[i] * q_c27[d - i] for i in range(n_c27) if 0 <= d - i < m_c27)
                             for d in range(n_c27 + m_c27 - 1)])          # the product, expanded term by term
        got_c27 = call_27(1, "poly_product_fixed", poly_product_fixed, p_c27.copy(), q_c27.copy())
        if got_c27 is None or np.shape(got_c27) != want_c27.shape or not np.allclose(got_c27, want_c27):
            wrong_27.append(f"p = {p_c27.astype(int).tolist()}, q = {q_c27.astype(int).tolist()} : attendu "
                            f"{want_c27.astype(int).tolist()}, reçu {shown(got_c27, 3)}"[:260])
    report_27(not wrong_27, "(1) poly_product_fixed : des polynômes aux coefficients non palindromes, de degrés variés "
              "(comparé au développement terme à terme)", "(1) poly_product_fixed : " + " ; ".join(wrong_27[:2]))
    parts_27.append(1)

with checked("M21.27"):                                       # (2) n_covers_fixed
    wrong_27 = []
    for k_c27, s_c27, m_c27 in ((8, 3, 6), (5, 2, 4), (7, 3, 5), (6, 2, 3), (4, 5, 3), (1, 1, 4)):
        stamps_c27 = np.zeros((m_c27 - 1) * s_c27 + k_c27, dtype=int)
        for i_c27 in range(m_c27):
            stamps_c27[s_c27 * i_c27:s_c27 * i_c27 + k_c27] += 1          # the stamps, put one by one
        got_c27 = [call_27(2, "n_covers_fixed", n_covers_fixed, j_c27, k_c27, s_c27, m_c27)
                   for j_c27 in range(len(stamps_c27))]
        if got_c27 != stamps_c27.tolist():
            wrong_27.append(f"(k, s, m) = ({k_c27}, {s_c27}, {m_c27}), toutes les cases : attendu "
                            f"{stamps_c27.tolist()}, reçu {got_c27!r}"[:220])
    report_27(not wrong_27, "(2) n_covers_fixed : toutes les cases de six convolutions transposées, s divisant k ou "
              "pas (tampons posés un par un)", "(2) n_covers_fixed : " + " ; ".join(wrong_27[:2]))
    parts_27.append(2)

with checked("M21.27"):                                       # (3) separate_fixed
    wrong_27 = []
    rank_one_c27 = [np.outer([0.0, 2.0, -1.0], [3.0, 1.0, 2.0]), np.outer([1.5, -2.0], [0.0, 3.0, 1.0, -2.0]),
                    np.outer(rng_c27.normal(size=4), rng_c27.normal(size=3))]
    rank_two_c27 = [np.array([[1.0, 2.0, 1.0], [2.0, 4.0, 3.0]]), rng_c27.normal(size=(3, 3))]
    for kernel_c27 in rank_one_c27:
        got_c27 = call_27(3, "separate_fixed", separate_fixed, kernel_c27.copy())
        if (not isinstance(got_c27, tuple) or len(got_c27) != 2
                or np.shape(np.outer(*got_c27)) != kernel_c27.shape or not np.allclose(np.outer(*got_c27), kernel_c27)):
            wrong_27.append(f"un noyau de rang 1, {np.round(kernel_c27, 2).tolist()} : attendu deux facteurs dont "
                            f"le produit extérieur le redonne, reçu {shown(got_c27, 3)}"[:260])
    for kernel_c27 in rank_two_c27:
        got_c27 = call_27(3, "separate_fixed", separate_fixed, kernel_c27.copy())
        if got_c27 is not None:
            wrong_27.append(f"un noyau de rang 2 ou plus, {np.round(kernel_c27, 2).tolist()} : attendu None"[:160])
    report_27(not wrong_27, "(3) separate_fixed : des noyaux de rang 1 (dont un avec K[0, 0] = 0) et de rang 2 ou plus",
              "(3) separate_fixed : " + " ; ".join(wrong_27[:2]))
    parts_27.append(3)

if len(set(parts_27)) == 3:
    verdict("M21.27", all(results_27), "les trois fonctions corrigées passent tous les cas.",
            "relis les lignes ❌ ci-dessus.")'''

M21_27 = Ex(
    "M21.27", "🐛", 1, 20, "Chasse à l'erreur : un noyau non retourné, des recouvrements supposés réguliers, un noyau "
    "de rang 2 « séparé »",
    "reconnaître trois erreurs classiques qui ne lèvent aucune erreur Python et passent une vérification mal "
    "choisie, puis les corriger.", "fiche §1, §5 et §6 ; Ex M21.7 et M21.22", tracks="C, E", given=GIVEN_27,
    note=NOTE_27,
    body=r"""Un collègue a écrit trois fonctions (cellule fournie) ; chacune a l'erreur que nomme le titre, aucune ne lève d'erreur Python, et chacune a passé la vérification qu'il a faite :
1. `poly_product(p, q)` doit rendre les coefficients du produit de deux polynômes, du terme constant au terme de plus haut degré ; elle renvoie `np.correlate(p, q, "full")`. Il l'a vérifiée sur $(1 + 2X)(2 + 5X + 2X^2)$, dont le second facteur a des coefficients palindromes, et l'applique à $(1 + 2X)(3 - X + 4X^2)$ (`P_27`, `Q_27`).
2. `n_covers(k, s)` doit rendre le nombre de tampons qui couvrent une case intérieure d'une convolution transposée de noyau de longueur $k$ et de pas $s$ (fiche §5) ; elle renvoie `k // s`. Il l'a vérifiée sur $(k, s) = (6, 2)$, $(9, 3)$ et $(8, 4)$.
3. `separate(K)` doit rendre les deux facteurs d'un noyau séparable ; elle rend la première colonne de $\mathbf{K}$ et sa première ligne divisée par $K_{0,0}$, sans regarder le rang. Il l'a vérifiée sur un produit extérieur, et l'applique au noyau $\begin{pmatrix} 2 & 1 & 3 \\ 4 & 2 & 5 \\ 2 & 1 & 3 \end{pmatrix}$ (`K_27`).

À faire : écris `poly_product_fixed(p, q)`, `n_covers_fixed(j, k, s, m)` (le nombre de tampons qui couvrent la case $j$ d'une convolution transposée de $m$ valeurs d'entrée, de noyau de longueur $k$ et de pas $s$ : le nombre de $i \in \{0, \ldots, m - 1\}$ tels que $0 \le j - s\,i \le k - 1$) et `separate_fixed(K)` (qui rend les deux facteurs d'un noyau de rang 1, et `None` sinon), puis réponds :
- a) les coefficients de $(1 + 2X)(3 - X + 4X^2)$, avec `poly_product_fixed` (la valeur que donne le calcul) ;
- b) pour une convolution transposée de noyau de longueur $k = 8$, de pas $s = 3$ et de $m = 6$ valeurs d'entrée, les nombres de tampons qui couvrent les cases 9, 10 et 11, avec `n_covers_fixed` (une liste de 3 entiers) ;
- c) le plus grand écart, en valeur absolue, entre `K_27` et le produit extérieur des deux facteurs que rend le `separate` du collègue (la valeur que donne le calcul) ;
- d) vrai ou faux : ta `separable_factors` (M21.22) rend `None` pour ce noyau ;
- e) une question à part, sur le mode « même taille » d'un noyau de longueur paire, où NumPy et PyTorch diffèrent d'une case : pour la somme glissante de poids $(2, -3)$ et $\mathbf{x} = (6, 2, 7, 1, 8, 3)$ (`W_27`, `X_27`), ce que rend `np.convolve` en mode même taille, avec les poids retournés (la valeur que donne le calcul).

La vérification essaie tes corrections sur des cas que tu ne vois pas : des polynômes aux coefficients non palindromes, toutes les cases de convolutions transposées où $s$ divise $k$ ou pas, des noyaux de rang 1 (dont un avec $K_{0,0} = 0$) et de rang 2.""",
    todo='''def poly_product_fixed(p, q):
    """The coefficients of the product of two polynomials, from the constant term to the highest degree."""
    raise NotImplementedError("poly_product_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def n_covers_fixed(j, k, s, m):
    """The number of stamps that cover the cell j of a transposed convolution of m inputs, kernel of length k, step s:
    the number of i in {0, ..., m - 1} such that 0 <= j - s i <= k - 1."""
    raise NotImplementedError("n_covers_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def separate_fixed(K):
    """The two factors (u, v) of K = outer(u, v) when K has rank 1; None otherwise."""
    raise NotImplementedError("separate_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M21_27a = answer_M21_27b = answer_M21_27c = answer_M21_27d = answer_M21_27e = ...
with wbm.attempt("M21.27"):          # your three functions: ⏳ while they are not written
    answer_M21_27a = ...  # a) a list of 4 numbers, as computed: poly_product_fixed(P_27, Q_27)
    answer_M21_27b = ...  # b) a list of 3 integers: the stamps on the cells 9, 10 and 11 (k = 8, s = 3, m = 6)
    answer_M21_27c = ...  # c) a number, as computed: the largest |K_27 - outer(u, v)|, (u, v) from the colleague's separate
    answer_M21_27d = ...  # d) True or False: your separable_factors(K_27) is None
    answer_M21_27e = ...  # e) a list of 6 numbers, as computed: np.convolve(X_27, W_27[::-1], "same")''',
    check='''for letter, answer in zip("abcde", [answer_M21_27a, answer_M21_27b, answer_M21_27c, answer_M21_27d, answer_M21_27e]):
    wbm.check(f"M21.27{letter}", answer, computed=True)

''' + CHECK_27,
    solution='''def poly_product_fixed(p, q):
    """The coefficients of the product of two polynomials, from the constant term to the highest degree."""
    return np.convolve(p, q)              # a product of polynomials is a convolution: np.correlate does not flip q


def n_covers_fixed(j, k, s, m):
    """The number of stamps that cover the cell j of a transposed convolution of m inputs, kernel of length k, step s:
    the number of i in {0, ..., m - 1} such that 0 <= j - s i <= k - 1."""
    return sum(1 for i in range(m) if 0 <= j - s * i <= k - 1)


def separate_fixed(K):
    """The two factors (u, v) of K = outer(u, v) when K has rank 1; None otherwise."""
    return mymath.convolution.separable_factors(K)         # tests the rank, and works when K[0, 0] = 0


answer_M21_27a = poly_product_fixed(P_27, Q_27).tolist()
answer_M21_27b = [n_covers_fixed(j, 8, 3, 6) for j in (9, 10, 11)]
u_27, v_27 = separate(K_27)
answer_M21_27c = float(np.max(np.abs(K_27 - np.outer(u_27, v_27))))
answer_M21_27d = mymath.convolution.separable_factors(K_27) is None
answer_M21_27e = np.convolve(X_27, W_27[::-1], "same").tolist()
pytorch_27 = [float(W_27[0] * X_27[i] + W_27[1] * (X_27[i + 1] if i + 1 < len(X_27) else 0)) for i in range(len(X_27))]
print("a)", answer_M21_27a, "; le collègue :", poly_product(P_27, Q_27).tolist())
print("b)", answer_M21_27b, "; le collègue :", n_covers(8, 3), "partout ; la carte des 23 cases :",
      [n_covers_fixed(j, 8, 3, 6) for j in range((6 - 1) * 3 + 8)])
print("c)", answer_M21_27c, "; produit extérieur du collègue :\\n", np.outer(u_27, v_27))
print("d)", answer_M21_27d, "; s₂/s₁ =", round(float(np.divide(*np.linalg.svd(K_27, compute_uv=False)[[1, 0]])), 4))
print("e)", answer_M21_27e, "; PyTorch (zéro en trop à droite) :", pytorch_27)


''' + CHECK_27,
    record='''p_27r, q_27r = [1, 2], [3, -1, 4]
product_27r = [sum(p_27r[i] * q_27r[m - i] for i in range(len(p_27r)) if 0 <= m - i < len(q_27r))
               for m in range(len(p_27r) + len(q_27r) - 1)]                    # the coefficients, by the definition
wbm.record("M21.27a", product_27r,
           mistakes={"le produit de deux polynômes est une convolution : np.correlate ne retourne pas son second "
                     "argument": np.correlate(p_27r, q_27r, "full").tolist()})
stamps_27r = np.zeros((6 - 1) * 3 + 8, dtype=int)
for i_27r in range(6):
    stamps_27r[3 * i_27r:3 * i_27r + 8] += 1                                   # the stamps, put one by one
wbm.record("M21.27b", stamps_27r[[9, 10, 11]].tolist(),
           mistakes={"s ne divise pas k : le nombre de tampons change d'une case à l'autre ; compte les i tels que "
                     "0 ≤ j − s i ≤ k − 1": [8 // 3] * 3,
                     "s ne divise pas k : les cases intérieures ne reçoivent pas toutes le même nombre de tampons ; "
                     "compte les i tels que 0 ≤ j − s i ≤ k − 1": [8 // 3 + 1] * 3})
kernel_27r = np.array([[2.0, 1.0, 3.0], [4.0, 2.0, 5.0], [2.0, 1.0, 3.0]])
bogus_27r = np.outer(kernel_27r[:, 0], kernel_27r[0, :] / kernel_27r[0, 0])
wbm.record("M21.27c", float(np.max(np.abs(kernel_27r - bogus_27r))), decimals=2,
           mistakes={"compare K au produit extérieur case par case : le noyau n'est pas de rang 1": 0.0})
wbm.record("M21.27d", bool(np.linalg.matrix_rank(kernel_27r) > 1),
           mistakes={"le noyau est de rang 2 : sa deuxième valeur singulière n'est pas négligeable devant la première":
                         False})
x_27r, w_27r = [6, 2, 7, 1, 8, 3], [2, -3]
wbm.record("M21.27e", np.convolve(x_27r, w_27r[::-1], "same").tolist(),
           mistakes={"c'est la version de PyTorch, le zéro en trop à droite ; NumPy le met au début":
                         [w_27r[0] * x_27r[i] + w_27r[1] * (x_27r[i + 1] if i + 1 < 6 else 0) for i in range(6)],
                     "np.convolve retourne les poids qu'on lui donne": np.convolve(x_27r, w_27r, "same").tolist()})''',
    after=[
        ("md", "**Après la vérification**, dans ta copie : pour chaque erreur, pourquoi la vérification du collègue "
               "ne la voyait-elle pas (un facteur palindrome, des couples où $s$ divise $k$, un noyau de rang 1), et "
               "quelle vérification l'aurait vue ? Écris la carte complète des tampons pour $k = 8$, $s = 3$, $m = 6$. "
               "Pour (3), quelle case de `K_27` le produit extérieur du collègue manque-t-il, et que se passerait-il "
               "avec $K_{0,0} = 0$ ? Pour e), de quel côté est le zéro en trop dans chaque bibliothèque ?"),
    ],
)

GIVEN_28 = '''def toeplitz_wrong_same_28(kernel, n, mode="full"):
    """Wrong: in the mode "same", the rows kept start at k // 2 instead of (k - 1) // 2 (built on the reference)."""
    if mode != "same":
        return ref_conv.toeplitz_matrix(kernel, n, mode)
    k = len(kernel)
    return ref_conv.toeplitz_matrix(kernel, n, "full")[k // 2:k // 2 + max(n, k)]'''

CHECK_28 = r'''with checked("M21.28"):
    results_28 = []

    def report_28(ok, success, failure):
        results_28.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))

    calls_28 = []

    def counted_28(toeplitz):
        """toeplitz, its calls recorded in calls_28 as (k, n, mode)."""
        def wrapper(kernel, n, mode="full"):
            calls_28.append((len(kernel), int(n), mode))
            return toeplitz(kernel, n, mode)
        return wrapper

    try:
        cases_28 = property_test_28(counted_28(ref_conv.toeplitz_matrix), ref_conv.convolve)
    except AssertionError as exc:
        print(f"❌ Ex M21.28 : ton test échoue sur la référence, qui est juste : {exc}"[:400])
        raise StopCheck from None
    report_28(isinstance(cases_28, int) and cases_28 >= 202 and len(calls_28) >= 3 * 202,
              f"sur la référence, ton test passe : {cases_28} cas, {len(calls_28)} appels de toeplitz_matrix",
              f"sur la référence, ton test rend {cases_28!r} et fait {len(calls_28)} appels de toeplitz_matrix : au "
              "moins 200 cas tirés et les deux cas limites, chacun dans les trois modes, et le nombre de cas rendu")
    report_28({mode for _, _, mode in calls_28} == {"full", "valid", "same"}, "les trois modes sont testés",
              "ton test doit appeler toeplitz_matrix dans les trois modes, \"full\", \"valid\" et \"same\"")
    report_28(any(k == 1 for k, _, _ in calls_28) and any(k == n for k, n, _ in calls_28),
              "les cas limites k = 1 et n = k sont testés", "ajoute les cas limites k = 1 et n = k")
    try:
        property_test_28(toeplitz_wrong_same_28, ref_conv.convolve)
        report_28(False, "", "ton test n'attrape pas toeplitz_wrong_same_28 (son mode même taille garde les lignes "
                  "à partir de ⌊k/2⌋)")
    except AssertionError as exc:
        message_28 = str(exc)
        k_28 = re.search(r"\bk\s*=\s*(\d+)", message_28)
        n_28 = re.search(r"\bn\s*=\s*(\d+)", message_28)
        report_28(True, "ton test attrape toeplitz_wrong_same_28 par un assert", "")
        report_28(message_28.strip().lower().startswith(("expected", "attendu")),
                  "son message dit d'abord ce qui était attendu",
                  f"le message doit commencer par ce qui était attendu (« expected … »), reçu : {message_28[:160]!r}")
        report_28(k_28 is not None and n_28 is not None and "same" in message_28,
                  "… puis le cas fautif : k, n et le mode",
                  f"le message doit donner le cas fautif, « k = …, n = … » et le mode, reçu : {message_28[:160]!r}")
        if k_28 is not None:
            report_28(int(k_28.group(1)) % 2 == 0, f"le cas fautif a un noyau de longueur paire, k = {k_28.group(1)}",
                      f"le cas fautif montré a k = {k_28.group(1)} : pour un noyau de longueur impaire, les deux "
                      "versions coïncident ; ton message donne-t-il bien la longueur du noyau ?")
    except Exception as exc:  # noqa: BLE001 - another error than an assert
        report_28(False, "", f"sur toeplitz_wrong_same_28, ton test lève {type(exc).__name__} au lieu d'un assert : "
                  f"{str(exc)[:160]}")
    try:
        property_test_28(mymath.convolution.toeplitz_matrix, mymath.convolution.convolve)
        print("✅ ta librairie (toeplitz_matrix et convolve) passe ton test de propriété")
    except (NotImplementedError, MymathMissingError):
        print("⏳ ta librairie : toeplitz_matrix ou convolve n'est pas encore écrite (M21.19, M21.20)")
    except AssertionError as exc:
        print(f"❌ ta librairie échoue à ton test ({str(exc)[:200]}) : si ton test passe sur la référence, l'erreur est "
              "dans ta toeplitz_matrix ou ta convolve (lance aussi leurs tests, M21.19 et M21.20)")
    verdict("M21.28", all(results_28), "ton test passe sur la référence et attrape la version fausse.",
            "relis les lignes ❌ ci-dessus.")'''

M21_28 = Ex(
    "M21.28", "🛠️", 1, 15, "Un test de propriété : la matrice de Toeplitz fois x égale la convolution, pour des "
    "longueurs tirées au hasard",
    "écrire un test de propriété pour `toeplitz_matrix`, et s'assurer qu'il attrape une version fausse du mode même "
    "taille.", "fiche §3 ; Ex M21.20", tracks="C", given=GIVEN_28, note=NOTE_28,
    body=r"""Un **test de propriété** vérifie, sur beaucoup de cas tirés au hasard, une loi que tout résultat juste respecte, sans connaître la réponse de chaque cas (M17, M18). La loi, ici (fiche §3) : pour tout noyau $\mathbf{w}$ de longueur $k$, tout signal $\mathbf{x}$ de longueur $n \ge k$ et chacun des trois modes, `toeplitz_matrix(w, n, mode) @ x` égale `convolve(x, w, mode)`.

Écris `property_test_28(toeplitz_matrix, convolve)`, qui reçoit les deux fonctions à tester :
- elle tire 200 cas avec un générateur `np.random.default_rng(5538)`, créé dans la fonction : une longueur de noyau $k$ de 1 à 6, une longueur de signal $n$ de $k$ à 12, un noyau et un signal d'entiers ; puis elle ajoute les cas limites $k = 1$ et $n = k$ ;
- pour chaque cas et chaque mode (`"full"`, `"valid"`, `"same"`), elle vérifie la loi par un `assert` (avec `np.allclose`), dont le message dit **d'abord** ce qui était attendu (il commence par « expected »), **puis** le cas fautif, écrit `k = …, n = …` avec le mode ;
- elle rend le nombre de cas vérifiés.

La cellule fournie donne une version **fausse** de `toeplitz_matrix`, construite sur la référence (`ref_conv`) : `toeplitz_wrong_same_28`, dont le mode même taille garde les lignes à partir de $\lfloor k/2\rfloor$ au lieu de $\lfloor\frac{k-1}{2}\rfloor$. La vérification lance ton test sur la référence, où il doit passer (elle compte les appels, les modes et les cas limites) ; sur la version fausse, où il doit échouer par un `assert` dont le message montre un noyau de longueur paire ; puis sur **ta** librairie.""",
    todo='''def property_test_28(toeplitz_matrix, convolve):
    """200 random cases drawn with np.random.default_rng(5538), created inside: k from 1 to 6, n from k to 12, a
    kernel and a signal of integers; then the edge cases k = 1 and n = k. For each case and each mode ("full",
    "valid", "same"), assert that toeplitz_matrix(w, n, mode) @ x equals convolve(x, w, mode), with a message that
    says first what was expected, then the case (k = ..., n = ..., the mode). Return the number of cases checked."""
    raise NotImplementedError("property_test_28 n'est pas encore écrite (04_indices.md si tu bloques)")''',
    check=CHECK_28,
    solution='''def property_test_28(toeplitz_matrix, convolve):
    """200 random cases drawn with np.random.default_rng(5538), created inside: k from 1 to 6, n from k to 12, a
    kernel and a signal of integers; then the edge cases k = 1 and n = k. For each case and each mode ("full",
    "valid", "same"), assert that toeplitz_matrix(w, n, mode) @ x equals convolve(x, w, mode), with a message that
    says first what was expected, then the case (k = ..., n = ..., the mode). Return the number of cases checked."""
    rng = np.random.default_rng(5538)
    cases = []
    for _ in range(200):
        k = int(rng.integers(1, 7))
        n = int(rng.integers(k, 13))
        cases.append((rng.integers(-5, 6, size=k).astype(float), rng.integers(-5, 6, size=n).astype(float)))
    cases.append((np.array([3.0]), np.array([2.0, -1.0, 4.0, 0.0])))                       # k = 1
    cases.append((np.array([1.0, -2.0, 3.0, 2.0]), np.array([4.0, 0.0, -1.0, 5.0])))      # n = k
    for w, x in cases:
        for mode in ("full", "valid", "same"):
            got = toeplitz_matrix(w, len(x), mode) @ x
            want = convolve(x, w, mode)
            assert np.shape(got) == np.shape(want) and np.allclose(got, want), (
                f"expected toeplitz_matrix(w, n, {mode!r}) @ x = {np.round(want, 6).tolist()}, got "
                f"{np.round(got, 6).tolist()} (k = {len(w)}, n = {len(x)}, mode {mode!r}, w = {w.tolist()}, "
                f"x = {x.tolist()})")
    return len(cases)


print("sur la référence :", property_test_28(ref_conv.toeplitz_matrix, ref_conv.convolve), "cas")
try:
    property_test_28(toeplitz_wrong_same_28, ref_conv.convolve)
except AssertionError as exc:
    print("la version fausse :", str(exc)[:300])


''' + CHECK_28,
    after=[
        ("md", "**Après la vérification**, dans ta copie : pourquoi la version fausse passe-t-elle tous les cas de "
               "noyau impair, et les modes plein et valide ? Pourquoi les cas limites $k = 1$ et $n = k$ "
               "valent-ils d'être écrits à part ? Pourquoi un test de propriété tire-t-il des **entiers** ?"),
    ],
)

PART_C = Part("C", "Déboguer, tester",
              "Fiche §2, §3, §5 et §6. Trois erreurs classiques qui ne lèvent aucune erreur Python ; un test de "
              "propriété pour la matrice de Toeplitz. La vérification de M21.28 s'appuie sur la référence "
              "(`ref_conv`), pour ne pas dépendre de ton code.",
              given=GIVEN_C, exercises=[M21_27, M21_28])

# ---------------------------------------------------------------------------
# Notebook exercises: the challenge (M21.29)
# ---------------------------------------------------------------------------
NOTE_29 = (r"a) Les poids secrets, $(-0{,}46 ;\ 0{,}18 ;\ 0{,}92 ;\ 0{,}03 ;\ 0{,}75 ;\ -0{,}35 ;\ 0{,}59)$, sont "
           r"retrouvés à $2 \cdot 10^{-3}$ près. b) L'écart type du bruit estimé vaut $0{,}049$, soit $0{,}05$ à 2 "
           r"décimales. c) Avec 10, 20, 50, 100, 200 et 500 valeurs, les erreurs maximales valent environ $0{,}069$, "
           r"$0{,}029$, $0{,}020$, $0{,}009$, $0{,}005$ et $0{,}003$ : 50 valeurs suffisent pour une erreur sous "
           r"0,025. L'erreur décroît à peu près comme $\frac{1}{\sqrt m}$ : c'est la précision des moindres carrés, "
           r"et la sortie est **linéaire en $\mathbf{w}$**, ce qui rend le problème si simple.")

GIVEN_29 = '''def _sensor_29():
    """The filtered and noisy sensor (seed 5539): 7 secret weights, x of 2 000 Gaussian values, y = w ⋆ x + 0.05 η."""
    rng = np.random.default_rng(5539)
    secret = np.round(rng.uniform(-1, 1, 7), 2)
    x = rng.standard_normal(2000)
    y = np.correlate(x, secret, "valid") + 0.05 * rng.standard_normal(2000 - 7 + 1)
    return x, y


X_29, Y_29 = _sensor_29()                                  # the secret weights are not kept
M_CHOICES_29 = [10, 20, 50, 100, 200, 500]
print("x :", X_29.shape, "; y :", Y_29.shape)'''

CHECK_29 = '''with checked("M21.29"):
    rng_c29 = np.random.default_rng(5529)
    wrong_29 = []
    for n_c29, k_c29, noise_c29 in ((60, 3, 0.0), (400, 5, 0.01), (30, 1, 0.0)):
        w_c29 = np.round(rng_c29.uniform(-2, 2, k_c29), 2)
        x_c29 = rng_c29.standard_normal(n_c29)
        y_c29 = np.correlate(x_c29, w_c29, "valid") + noise_c29 * rng_c29.standard_normal(n_c29 - k_c29 + 1)
        got_c29 = estimate_kernel_29(x_c29.copy(), y_c29.copy(), k_c29)
        tolerance_c29 = 1e-9 if noise_c29 == 0 else 0.01
        if got_c29 is None or np.shape(got_c29) != (k_c29,) or not np.allclose(got_c29, w_c29, rtol=0, atol=tolerance_c29):
            wrong_29.append(f"{k_c29} poids, {n_c29} valeurs, bruit {noise_c29} : attendu {w_c29.tolist()} à "
                            f"{tolerance_c29} près, reçu {shown(got_c29)}"[:260])
    verdict("M21.29", not wrong_29, "estimate_kernel_29 retrouve trois noyaux que tu ne vois pas (dont deux sans bruit, "
            "exactement).", "estimate_kernel_29, " + " ; ".join(wrong_29[:2]))'''

M21_29 = Ex(
    "M21.29", "🏆", 3, 25, "Défi : retrouver un noyau inconnu à partir d'un signal et de sa version filtrée bruitée, "
    "par les moindres carrés",
    "retrouver un noyau inconnu par les moindres carrés, à partir d'un signal et de sa version filtrée et bruitée.",
    "fiche §3 ; M09b ; Ex M21.20", tracks="C", given=GIVEN_29, note=NOTE_29,
    body=r"""Un capteur a été filtré par une somme glissante de 7 poids inconnus, puis bruité. La cellule fournie tire (graine 5539) les poids secrets, un signal $\mathbf{x}$ de 2 000 valeurs gaussiennes (`X_29`), et la sortie $\mathbf{y} = \mathbf{w} \star \mathbf{x} + 0{,}05\,\boldsymbol{\eta}$ (`Y_29`, 1 994 valeurs, $\boldsymbol{\eta}$ gaussien) ; elle ne garde pas les poids secrets.

La sortie est **linéaire en $\mathbf{w}$** (fiche §3) : retrouver $\mathbf{w}$, c'est minimiser $\lVert\mathbf{A}\mathbf{c} - \mathbf{y}\rVert^2$, un problème de moindres carrés (M09b). Écris `estimate_kernel_29(x, y, k)`, l'estimation des $k$ poids d'une somme glissante valide $\mathbf{y} \approx \mathbf{w} \star \mathbf{x}$, avec ta `toeplitz_matrix` et `np.linalg.lstsq` : les lignes $k - 1$ à $n - 1$ de la matrice pleine de $\mathbf{x}$, pris comme noyau, pour des signaux de longueur $k$, envoient $\tilde{\mathbf{w}}$ (le noyau retourné) sur $\mathbf{w} \star \mathbf{x}$ (tu peux aussi prendre la matrice des fenêtres $\mathbf{X}_{\text{f}}$ de la fiche §3, qui envoie $\mathbf{w}$ sur $\mathbf{w} \star \mathbf{x}$). Puis :
- `w_hat_29` : ton estimation des 7 poids, à partir de `X_29` et `Y_29`.

**Critère de réussite :** a) ton estimation, arrondie à 2 décimales, redonne exactement les 7 poids secrets (une liste de 7 nombres). Puis :
- b) l'écart type du bruit estimé par $\frac{\lVert\mathbf{y} - \mathbf{X}_{\text{f}}\hat{\mathbf{w}}\rVert}{\sqrt{1\,994 - 7}}$ (la valeur que donne le calcul) ;
- c) le plus petit nombre $m$ de valeurs de $\mathbf{y}$, parmi 10, 20, 50, 100, 200 et 500 (`M_CHOICES_29`), pour lequel l'estimation faite avec les $m$ premières valeurs de $\mathbf{y}$ (et leurs fenêtres) a tous ses poids à moins de 0,025 des poids secrets (ceux de a), une fois a) juste).

La vérification essaie aussi `estimate_kernel_29` sur des noyaux que tu ne vois pas. Dans ta copie : pourquoi la matrice de Toeplitz de $\mathbf{x}$ donne-t-elle le noyau **retourné** ? Comment l'erreur de c) décroît-elle avec $m$ ? Pourquoi divise-t-on par $\sqrt{1\,994 - 7}$ en b), et non par $\sqrt{1\,994}$ ?""",
    todo='''def estimate_kernel_29(x, y, k):
    """The least-squares estimate of the k weights w of a valid sliding sum y ≈ w ⋆ x (len(y) = len(x) - k + 1),
    with your toeplitz_matrix and np.linalg.lstsq."""
    raise NotImplementedError("estimate_kernel_29 n'est pas encore écrite (04_indices.md si tu bloques)")


w_hat_29 = answer_M21_29a = answer_M21_29b = answer_M21_29c = ...
with wbm.attempt("M21.29"):          # estimate_kernel_29 and your toeplitz_matrix: ⏳ while they are not written
    w_hat_29 = ...        # your estimate of the 7 weights, from X_29 and Y_29
    answer_M21_29a = ...  # a) a list of 7 numbers: w_hat_29 rounded to 2 decimals
    answer_M21_29b = ...  # b) a number, as computed: the estimated standard deviation of the noise
    answer_M21_29c = ...  # c) an integer of M_CHOICES_29: the smallest m whose estimate is within 0.025 of a)''',
    check='''right_29 = wbm.check("M21.29a", answer_M21_29a)
wbm.check("M21.29b", answer_M21_29b, computed=True)
wbm.check("M21.29c", answer_M21_29c)
if filled(answer_M21_29a):
    verdict("M21.29", right_29, "critère atteint : ton estimation redonne les 7 poids secrets.",
            "critère pas encore atteint : ton estimation, arrondie à 2 décimales, ne redonne pas les poids secrets.")

''' + CHECK_29,
    solution='''toeplitz_matrix = mymath.convolution.toeplitz_matrix


def estimate_kernel_29(x, y, k):
    """The least-squares estimate of the k weights w of a valid sliding sum y ≈ w ⋆ x (len(y) = len(x) - k + 1),
    with your toeplitz_matrix and np.linalg.lstsq."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    A = toeplitz_matrix(x, k)[k - 1:len(x)]            # (n - k + 1, k): A @ (flipped w) = w ⋆ x
    flipped, *_ = np.linalg.lstsq(A, y, rcond=None)
    return flipped[::-1]


w_hat_29 = estimate_kernel_29(X_29, Y_29, 7)
answer_M21_29a = np.round(w_hat_29, 2).tolist()
windows_29 = np.array([X_29[i:i + 7] for i in range(len(Y_29))])     # the window matrix X_f: X_f @ w = w ⋆ x
answer_M21_29b = float(np.linalg.norm(Y_29 - windows_29 @ w_hat_29) / math.sqrt(len(Y_29) - 7))
errors_29 = {m: float(np.max(np.abs(estimate_kernel_29(X_29[:m + 6], Y_29[:m], 7) - np.array(answer_M21_29a))))
             for m in M_CHOICES_29}
answer_M21_29c = min(m for m in M_CHOICES_29 if errors_29[m] < 0.025)
print("a)", answer_M21_29a, "; plus grand écart avant l'arrondi :", f"{np.max(np.abs(w_hat_29 - answer_M21_29a)):.4f}")
print("b)", round(answer_M21_29b, 4))
print("c)", answer_M21_29c, "; erreurs maximales :", {m: round(e, 4) for m, e in errors_29.items()})

''' + CHECK_29,
    record='''rng_29r = np.random.default_rng(5539)
secret_29r = np.round(rng_29r.uniform(-1, 1, 7), 2)
x_29r = rng_29r.standard_normal(2000)
y_29r = np.correlate(x_29r, secret_29r, "valid") + 0.05 * rng_29r.standard_normal(1994)
windows_29r = np.array([x_29r[i:i + 7] for i in range(1994)])
estimate_29r = np.linalg.lstsq(windows_29r, y_29r, rcond=None)[0]
assert np.array_equal(np.round(estimate_29r, 2), secret_29r)
wbm.record("M21.29a", secret_29r.tolist(), decimals=2,
           mistakes={"la matrice de Toeplitz de x envoie le noyau RETOURNÉ sur w ⋆ x : retourne ton estimation":
                         secret_29r[::-1].tolist()})
residual_29r = y_29r - windows_29r @ estimate_29r
wbm.record("M21.29b", float(np.linalg.norm(residual_29r) / math.sqrt(1994 - 7)), decimals=2,
           mistakes={"l'écart type du bruit, pas la moyenne du résidu": 0.0,
                     "divise la norme du résidu par la racine du nombre de degrés de liberté":
                         float(np.linalg.norm(residual_29r))})
errors_29r = [float(np.max(np.abs(np.linalg.lstsq(windows_29r[:m], y_29r[:m], rcond=None)[0] - secret_29r)))
              for m in [10, 20, 50, 100, 200, 500]]
first_29r = next(m for m, e in zip([10, 20, 50, 100, 200, 500], errors_29r) if e < 0.025)
assert min(abs(e - 0.025) for e in errors_29r) > 0.003
wbm.record("M21.29c", first_29r, choices=[10, 20, 50, 100, 200, 500],
           mistakes={"vérifie les valeurs plus petites de la liste : on cherche la plus petite qui convient":
                         [10, 20, 50, 100, 200, 500][[10, 20, 50, 100, 200, 500].index(first_29r) + 1],
                     "pour cette valeur de m, regarde l'écart du plus mauvais poids, pas leur écart moyen":
                         [10, 20, 50, 100, 200, 500][[10, 20, 50, 100, 200, 500].index(first_29r) - 1]})''',
    after=[
        ("md", "**Dans ta copie** : trace l'erreur maximale contre $m$ en échelles logarithmiques ; quelle pente "
               "vois-tu ? Que deviendrait le problème si l'on ne connaissait pas $k$ ? Pourquoi un filtrage par une "
               "couche apprise, dans workbookIA 21, se règle-t-il par une autre méthode, alors que celui-ci se résout "
               "en une ligne ?"),
    ],
)

PART_D = Part("D", "Défi", "Fiche §3. Un noyau inconnu, retrouvé par les moindres carrés à partir d'un signal et de "
                           "sa version filtrée et bruitée.",
              exercises=[M21_29])

PARTS = [PART_A, PART_B, PART_C, PART_D]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M21.1 à M21.11, M21.17 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            rows.append(ex.table_row(part.key if i == 0 else ""))
    if kind == "exercise":
        title = "# M21 · Convolution, matrices de Toeplitz et équivariance — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m21_convolution/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M21`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M21 · Convolution, matrices de Toeplitz et équivariance — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : une loi de somme de dés, des convolutions et des "
               "corrélations dans les trois modes, des pochoirs, une matrice de Toeplitz, l'équivariance avec un pas, "
               "des positions, une convolution transposée, une carte filtrée, des paramètres et des coûts, un champ "
               "récepteur, un pire cas, et un pont.\n"
               "- Écrire les cinq fonctions de `mymath/convolution.py` (`convolve`, `toeplitz_matrix`, "
               "`circular_convolve`, `separable_factors`, `equivalent_kernel`) et les tester.\n"
               "- Prédire l'effet d'un décalage sur un filtrage avec pas, mesurer le gain d'un noyau séparable, "
               "dessiner les recouvrements d'une convolution transposée, corriger trois erreurs classiques, écrire un "
               "test de propriété, et relever un défi : retrouver un noyau par les moindres carrés.\n\n"
               r"**Rappel express.** Convolution $(\mathbf{a} * \mathbf{b})_m = \sum_i a_i\,b_{m-i}$, noyau retourné "
               r"(`np.convolve`) ; corrélation croisée $(\mathbf{w} \star \mathbf{x})_i = \sum_u w_u\,x_{i+u}$, sans "
               r"retournement (les bibliothèques) : c'est la convolution valide par $\tilde{\mathbf{w}}$. Modes : "
               r"plein $n + k - 1$, valide $n - k + 1$, même taille $n$ à partir de l'indice $\lfloor\frac{k-1}{2}"
               r"\rfloor$ de la pleine. Toeplitz : $T_{ij} = w_{i-j}$, $nk$ coefficients non nuls ; la transposée de "
               r"la valide est la pleine par $\tilde{\mathbf{w}}$. Circulaire : $\operatorname{circ}(\mathbf{h})^\top "
               r"= \operatorname{circ}(\check{\mathbf{h}})$, $\check{\mathbf{h}} = (h_0, h_{n-1}, \ldots, h_1)$. "
               r"Positions : $\lfloor\frac{n + 2p - d(k-1) - 1}{s}\rfloor + 1$. Transposée : $(m - 1)s - 2p + d(k - 1) "
               r"+ 1 + p_{\text{out}}$ valeurs, un damier si $s$ ne divise pas $k$. Paramètres "
               r"$C_{\text{out}}(\frac{C_{\text{in}}}{g}k_hk_w + 1)$, coût $H_{\text{out}}W_{\text{out}}C_{\text{out}}"
               r"\frac{C_{\text{in}}}{g}k_hk_w$ ; un noyau de rang 1 se fait en deux passes. Champ récepteur $1 + "
               r"\sum_\ell d_\ell(k_\ell - 1)s_1\cdots s_{\ell-1}$, pas $S = s_1\cdots s_L$. Pire cas : "
               r"$\varepsilon\lVert\mathbf{g}\rVert_1$ sur la boule L∞, en $\varepsilon\operatorname{signe}"
               r"(\mathbf{g})$ ; $\varepsilon\lVert\mathbf{g}\rVert_2$ sur la boule L2.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu calculer une convolution et une corrélation croisée dans les trois modes, et passer de "
               "l'une à l'autre par le noyau retourné ?\n"
               "2. Sais-tu écrire la matrice de Toeplitz d'une convolution, lire son rang, son noyau et sa "
               "transposée ?\n"
               "3. Sais-tu dire ce qu'un décalage fait à un filtrage, avec ou sans pas, et reconnaître une "
               "convolution circulaire ?\n"
               "4. Sais-tu compter les positions d'une fenêtre, la taille d'une convolution transposée, les "
               "paramètres et le coût d'un filtrage à plusieurs canaux ?\n"
               "5. Sais-tu composer des convolutions, calculer un champ récepteur, séparer un noyau de rang 1, et "
               "trouver le pire cas d'une perturbation bornée ?\n\n"
               "**La suite** : le chapitre 21 de workbookIA, qui fait glisser des noyaux appris sur des images, règle "
               "leur pas, leur padding et leur dilatation, compte paramètres et opérations, calcule des champs "
               "récepteurs et agrandit des cartes par des convolutions transposées ; puis M22 (récurrences "
               "vectorielles, rayon spectral et normes de matrices).")]


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
