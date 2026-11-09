#!/usr/bin/env python
"""Build the two notebooks of chapter M12d from a single source (used by Claude).

    python tools/chapters/build_m12d.py
    python tools/run_all_notebooks.py chapitres/m12d_svd_acp/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m12d_svd_acp/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M12d.1 to M12d.13, 🔗 M12d.20 and M12d.21); parts A to C are the notebook
exercises. Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it. The data
are new: none is a test case of tests/test_m12d_svd_pca.py, an example of the fiche (no [[6, 4], [1, −6]], no
X = [[2, 2], [4, 1], [4, −2]], no [[10, 7], [7, 5]], no cloud of covariance [[11, 6, 0], [6, 6, 0], [0, 0, 8]]) or of
a docstring of svd_pca.py, data of M12a to M12c, or an example of workbookIA 12 (no [[3, 1], [1, 3]], [[4, 5], [5, 7]],
[[5, 2], [2, 2]] or [[1, r], [r, 1]], no direction (1, ±1), (2, 1), (−1, 2) or (3, 4)/5, no points A(1, 1) to E(7, 3),
no MNIST number, no axis of a 2D cloud, no whitening), nor of workbookIA 25 (no percentile threshold, no ROC-AUC).
The photograph of M12d.31, M12d.32 and M12d.37 is the CC0 coffee cup of data/cards/tasse_cafe.md.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M12d"
FOLDER = "chapitres/m12d_svd_acp"

DESC = "l'ordre décroissant : la plus grande d'abord"
UNIT = "un vecteur unitaire : divise par sa norme"
SIGN = "la convention de signe : la coordonnée de plus grande valeur absolue positive"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M12d.1", "La SVD d'une matrice 2 × 2 à la main, par AᵀA", [
        ("a", "a matrix", "matrix(A_1.T * A_1)",
         '''mistakes={"AᵀA : les produits scalaires des COLONNES de A, pas des lignes": matrix(A_1 * A_1.T)}'''),
        ("b", "a list of 2 numbers", "[225, 4]", f'''mistakes={{"{DESC}": [4, 225]}}'''),
        ("c", "a list of 2 numbers", "[15, 2]",
         f'''mistakes={{"une valeur singulière est la RACINE d'une valeur propre de AᵀA": [225, 4], "{DESC}": [2, 15]}}'''),
        ("d", "a list of 2 numbers (4 decimals)", "exact(V1_1)",
         f'''decimals=4, mistakes={{"{UNIT}": [11, 10], "{SIGN}": exact(-V1_1), '''
         '''"v₁ va avec la plus GRANDE valeur propre de AᵀA": exact(V2_1)}'''),
        ("e", "a list of 2 numbers (4 decimals)", "exact(V2_1)", f'''decimals=4, mistakes={{"{SIGN}": exact(-V2_1)}}'''),
        ("f", "a list of 2 numbers (4 decimals)", "exact(U1_1)",
         '''decimals=4, mistakes={"u₁ = A v₁ / s₁ : divise par s₁": exact(A_1 * V1_1), '''
         '''"u₁ = A v₁ / s₁, avec A et non Aᵀ": exact(A_1.T * V1_1 / 15)}'''),
        ("g", "a number", "A_1.det()",
         '''mistakes={"ad − bc, pas ad + bc": 70, "le déterminant garde son signe : seule sa valeur absolue est s₁ s₂": 30}'''),
        ("h", "a list of 2 numbers (4 decimals)", "[float(6 + sq(66)), float(6 - sq(66))]",
         f'''decimals=4, mistakes={{"les valeurs propres de A elle-même : les racines de λ² − (tr A) λ + det A": [15.0, 2.0], '''
         f'''"{DESC}": [float(6 - sq(66)), float(6 + sq(66))]}}'''),
    ]),

    Paper("M12d.2", "La SVD compacte d'une matrice 3 × 2 de rang 1", [
        ("a", "an integer", "A_2.rank()", '''mistakes={"les deux colonnes sont proportionnelles": 2}'''),
        ("b", "a matrix", "matrix(A_2.T * A_2)",
         '''mistakes={"AᵀA est de forme (2, 2) : les produits scalaires des colonnes": matrix(A_2 * A_2.T)}'''),
        ("c", "a list of 2 numbers", "[5850, 0]", f'''mistakes={{"{DESC}": [0, 5850]}}'''),
        ("d", "a number (4 decimals)", "float(15 * sq(26))",
         '''decimals=4, mistakes={"une valeur singulière est la RACINE d'une valeur propre de AᵀA": 5850.0}'''),
        ("e", "a list of 2 numbers (4 decimals)", "exact(V1_2)",
         f'''decimals=4, mistakes={{"{UNIT}": [-1, 5], "{SIGN}": exact(-V1_2)}}'''),
        ("f", "a list of 3 numbers (4 decimals)", "exact(U1_2)",
         '''decimals=4, mistakes={"u₁ = A v₁ / s₁, avec le v₁ de la convention : son signe suit celui de v₁": exact(-U1_2)}'''),
        ("g", "a number", "5850",
         '''fractional="‖A‖²_F est la somme des carrés de tous les éléments, s₁² et non s₁ : un entier"'''),
        ("h", "a list of 2 numbers (4 decimals)", "exact(V2_2)",
         f'''decimals=4, mistakes={{"{SIGN}": exact(-V2_2), "{UNIT}": [5, 1]}}'''),
    ]),

    Paper("M12d.3", "Le cercle unité devient une ellipse : axes et demi-axes", [
        ("a", "a list of 2 numbers", "[9, 4]",
         f'''mistakes={{"les demi-axes sont les valeurs singulières, racines des valeurs propres de BᵀB": [81, 16], "{DESC}": [4, 9]}}'''),
        ("b", "a list of 2 numbers (4 decimals)", "exact(U1_3)",
         f'''decimals=4, mistakes={{"le grand axe est porté par u₁ = B v₁ / s₁, dans l'espace d'arrivée ; v₁ est le point de départ": exact(V1_3), '''
         f'''"{UNIT}": [7, -4]}}'''),
        ("c", "a list of 2 numbers (4 decimals)", "exact(V1_3)",
         f'''decimals=4, mistakes={{"{SIGN}": exact(-V1_3), "le point de DÉPART du cercle, v₁, pas son image": exact(U1_3)}}'''),
        ("d", "a number", "abs(B_3.det())", '''mistakes={"une aire est positive : π s₁ s₂ = π |det B|": -36}'''),
        ("e", "a number (4 decimals)", "float((B_3 * V([1, 0])).norm())", "decimals=4"),
        ("f", "a number (4 decimals)", "float((B_3 * V([0, 1])).norm())", "decimals=4"),
        ("g", "a number (2 decimals)", "2.25",
         '''decimals=2, mistakes={"le rapport des valeurs singulières, pas de leurs carrés": 81 / 16}'''),
        ("h", "True or False", "bool(B_3.det() > 0)",
         '''mistakes={"le signe du déterminant dit si l'orientation est conservée": True}'''),
    ]),

    Paper("M12d.4", "L'approximation de rang 1 d'une matrice 3 × 3 et son erreur", [
        ("a", "a number", "sum(v ** 2 for v in A_4)"),
        ("b", "a matrix", "matrix(A_4.T * A_4)",
         '''mistakes={"AᵀA : les produits scalaires des COLONNES de A": matrix(A_4 * A_4.T)}'''),
        ("c", "a list of 3 numbers (4 decimals)", "[7.0, float(2 * sq(2)), float(sq(2))]",
         f'''decimals=4, mistakes={{"une valeur singulière est la RACINE d'une valeur propre de AᵀA": [49, 8, 2], '''
         f'''"{DESC}": [float(sq(2)), float(2 * sq(2)), 7.0]}}'''),
        ("d", "a list of 3 numbers (4 decimals)", "exact(V1_4)", f'''decimals=4, mistakes={{"{UNIT}": [5, 4, 0]}}'''),
        ("e", "a list of 3 numbers (4 decimals)", "exact(U1_4)",
         '''decimals=4, mistakes={"u₁ = A v₁ / s₁ : divise par s₁": exact(A_4 * V1_4)}'''),
        ("f", "a matrix (4 decimals)", "floats(A1_4)",
         '''decimals=4, mistakes={"A₁ = s₁ u₁ v₁ᵀ : n'oublie pas le facteur s₁": floats(U1_4 * V1_4.T)}'''),
        ("g", "a number (4 decimals)", "float(sq(10))",
         '''decimals=4, mistakes={"la racine de la somme des CARRÉS des valeurs singulières oubliées": float(3 * sq(2)), '''
         '''"la norme, pas son carré": 10.0}'''),
        ("h", "a number (4 decimals)", "float(sympy.Rational(49, 59))",
         '''decimals=4, mistakes={"l'énergie se compte avec les CARRÉS des valeurs singulières": float(7 / (7 + 3 * sq(2)))}'''),
    ]),

    Paper("M12d.5", "Compter les nombres stockés : une image en rang k", [
        ("a", "an integer", "900 * 1600"),
        ("b", "an integer", "40 * (900 + 1600 + 1)",
         '''mistakes={"k(m + n + 1) : les k valeurs singulières se stockent aussi": 40 * (900 + 1600)}'''),
        ("c", "a number (4 decimals)", "float(sympy.Rational(40 * 2501, 900 * 1600))", "decimals=4"),
        ("d", "an integer", "(900 * 1600 - 1) // 2501",
         '''mistakes={"le plus grand k tel que k(m + n + 1) < mn : arrondis vers le bas": 576}'''),
        ("e", "an integer", "(900 * 1600 * 2 // 100) // 2501",
         '''mistakes={"le plus grand k tel que k(m + n + 1) ≤ 0,02 mn : arrondis vers le bas": 12}'''),
        ("f", "an integer", "3 * 40 * 2501"),
        ("g", "an integer", "40 * (900 + 4800 + 1)",
         '''mistakes={"une seule matrice de forme (900, 4 800) : k(m + n + 1) avec n = 4 800": 3 * 40 * 2501}'''),
    ]),

    Paper("M12d.6", "La pseudo-inverse d'une matrice non inversible et la solution de norme minimale", [
        ("a", "an integer", "A_6.rank()", '''mistakes={"les lignes sont proportionnelles : une seule direction": 2}'''),
        ("b", "a number (4 decimals)", "float(9 * sq(29))",
         '''decimals=4, mistakes={"pour une matrice de rang 1, s₁² = ‖A‖²_F : prends la racine": 2349.0}'''),
        ("c", "a number", "sum(v ** 2 for v in A_6)"),
        ("d", "a matrix (4 decimals)", "floats(1000 * P_6)",
         '''decimals=4, mistakes={"A⁺ = v₁ u₁ᵀ / s₁ = Aᵀ / s₁² pour une matrice de rang 1 : divise par s₁²": floats(1000 * A_6.T / (9 * sq(29))), '''
         '''"A⁺ est de forme (3, 2) : elle s'écrit avec Aᵀ": floats(1000 * A_6 / 2349)}'''),
        ("e", "a list of 3 numbers (4 decimals)", "exact(P_6 * V([18, 45]))",
         '''decimals=4, mistakes={"x⁺ = A⁺ y, avec la pseudo-inverse": exact(A_6.T * V([18, 45]))}'''),
        ("f", "a number", "(P_6 * V([18, 45])).norm()"),
        ("g", "a number", "9", '''mistakes={"la norme, pas son carré": 81}'''),
        ("h", "a list of 2 numbers (4 decimals)", "exact(A_6 * P_6 * V([1, 0]))",
         '''decimals=4, mistakes={"y′ n'est pas dans l'image de A : A A⁺ y′ est sa projection orthogonale sur cette image": [1, 0]}'''),
    ]),

    Paper("M12d.7", "Le conditionnement de trois matrices, et l'erreur relative sur une solution", [
        ("a", "a number (1 decimal)", "2.5",
         '''decimals=1, mistakes={"κ = s_max / s_min, le plus grand sur le plus petit": 0.4, '''
         '''"κ se lit sur les valeurs singulières, pas sur le déterminant": 10.0}'''),
        ("b", "a number", "1"),
        ("c", "a number (4 decimals)", "float(KAPPA_7)",
         '''decimals=4, mistakes={"κ = s₁ / s₂, les racines : pas le rapport des valeurs propres de RᵀR": float(KAPPA_7 ** 2), '''
         '''"le conditionnement ne se lit pas sur le déterminant": 1.0, '''
         '''"102 = s₁² + s₂² est ‖R‖²_F : κ = s₁ / s₂, avec s₁s₂ = |det R|": 102.0}'''),
        ("d", "a number (4 decimals)", "float(KAPPA_7 / 1000)",
         '''decimals=4, mistakes={"la borne multiplie l'erreur relative sur b par κ": 0.001}'''),
        ("e", "a list of 2 numbers", "exact(R_7.solve(V([14, 9])))"),
        ("f", "a number (2 decimals)", "float(AMPL_7)",
         '''decimals=2, mistakes={"le rapport des erreurs RELATIVES : divise ‖δx‖ par ‖x‖ et ‖δb‖ par ‖b‖": float(V([2, -5]).norm())}'''),
        ("g", "a number (1 decimal)", "float(KAPPA_7 ** 2)",
         '''decimals=1, mistakes={"κ(RᵀR) = κ(R)², le carré": float(KAPPA_7)}'''),
        ("h", "True or False", "True",
         '''mistakes={"multiplier R par c multiplie toutes ses valeurs singulières par |c| : leur rapport ne change pas": False}'''),
    ]),

    Paper("M12d.8", "Les axes principaux d'un nuage de ℝ³ : covariance, polynôme caractéristique, variances et axes", [
        ("a", "a list of 3 numbers", "exact(MU_8)"),
        ("b", "a matrix", "matrix(C_8)",
         '''mistakes={"la covariance divise par n − 1 = 6": matrix(XC_8.T * XC_8 / 7), '''
         '''"centre d'abord : retire la moyenne à chaque ligne": matrix(X_8.T * X_8 / 6)}'''),
        ("c", "a number", "C_8.trace()", '''mistakes={"la variance totale est la trace : la somme des seules variances": 42}'''),
        ("d", "a number", "C_8.det()"),
        ("e", "a list of 3 numbers", "[20, 11, 3]", f'''mistakes={{"{DESC}": [3, 11, 20]}}'''),
        ("f", "a list of 3 numbers (4 decimals)", "exact(U1_8)",
         f'''decimals=4, mistakes={{"{UNIT}": [4, 0, 1], "le bloc porte sur les mesures 1 et 3 : la deuxième coordonnée de u₁ est nulle": exact(V([4, 1, 0]) / sq(17))}}'''),
        ("g", "a list of 3 numbers (4 decimals)", "exact(U3_8)",
         f'''decimals=4, mistakes={{"{SIGN}": exact(-U3_8), "{UNIT}": [-1, 0, 4], '''
         f'''"le bloc porte sur les mesures 1 et 3 : la deuxième coordonnée de u₃ est nulle": exact(V([-1, 4, 0]) / sq(17))}}'''),
        ("h", "a number (1 decimal)", "float(qf(C_8, V([1, 0, 1]) / sq(2)))",
         '''decimals=1, mistakes={"uᵀCu avec u UNITAIRE : (1, 0, 1) a pour norme √2": 31.0}'''),
    ]),

    Paper("M12d.9", "Scores, reconstruction et erreur de reconstruction moyenne avec deux composantes sur trois", [
        ("a", "a list of 2 numbers (4 decimals)", "exact([U1_8.dot(D7_9), U2_8.dot(D7_9)])",
         '''decimals=4, mistakes={"les scores se calculent sur l'objet CENTRÉ, x₇ − μ": exact([U1_8.dot(X_8.row(6).T), U2_8.dot(X_8.row(6).T)])}'''),
        ("b", "a list of 3 numbers (4 decimals)", "exact(REC7_9)",
         '''decimals=4, mistakes={"x̂ = μ + t₁u₁ + t₂u₂ : rajoute la moyenne": exact(REC7_9 - MU_8)}'''),
        ("c", "a list of 7 numbers", "exact(XC_8 * V([4, 0, 1]))",
         '''mistakes={"les scores se calculent sur les objets CENTRÉS": exact(X_8 * V([4, 0, 1]))}'''),
        ("d", "a number", "20", '''fractional="la variance des scores se calcule avec n − 1 = 6, comme la covariance"'''),
        ("e", "a number (4 decimals)", "float(20 * U1_8[0])",
         '''decimals=4, mistakes={"Cov(t₁, x₁) = u₁ᵀ C e₁ = λ₁ u₁₁ : n'oublie pas λ₁": float(U1_8[0])}'''),
        ("f", "a number (4 decimals)", "float(sympy.Rational(18, 7))",
         '''decimals=4, mistakes={"la somme des variances oubliées, au facteur (n − 1)/n près": 3.0}'''),
        ("g", "a number (4 decimals)", "12.0",
         '''decimals=4, mistakes={"avec k = 1, on oublie λ₂ ET λ₃, au facteur (n − 1)/n près": 14.0, '''
         '''"avec k = 1, les variances oubliées sont λ₂ et λ₃": float(sympy.Rational(18, 7))}'''),
        ("h", "a number (4 decimals)", "float(sympy.Rational(31, 34))",
         '''decimals=4, mistakes={"la part GARDÉE : (λ₁ + λ₂) / (λ₁ + λ₂ + λ₃)": float(sympy.Rational(3, 34)), '''
         '''"avec deux axes sur trois, la variance λ₃ est perdue : la part gardée est sous 1": 1.0}'''),
    ]),

    Paper("M12d.10", "La variance expliquée cumulée : combien de composantes pour 95 % ?", [
        ("a", "a number", "int(sum(LAMBDA_10))"),
        ("b", "a number (4 decimals)", "float(LAMBDA_10[0] / sum(LAMBDA_10))", "decimals=4"),
        ("c", "a list of 3 numbers (4 decimals)", "[float(sum(LAMBDA_10[:k]) / sum(LAMBDA_10)) for k in (1, 2, 3)]",
         '''decimals=4, mistakes={"les parts CUMULÉES : additionne les parts des premiers axes": '''
         '''[float(v / sum(LAMBDA_10)) for v in LAMBDA_10[:3]]}'''),
        ("d", "an integer", "5", '''mistakes={"au moins 90 % : la part cumulée doit atteindre 0,90": 4}'''),
        ("e", "an integer", "6", '''mistakes={"au moins 95 % : la part cumulée doit atteindre 0,95": 5}'''),
        ("f", "a number (4 decimals)", "float(sum(LAMBDA_10[3:]))",
         '''decimals=4, mistakes={"les variances OUBLIÉES, au-delà des k = 3 premières": float(sum(LAMBDA_10[:3]))}'''),
        ("g", "a number (4 decimals)", "float(sympy.Rational(50, 51) * sum(LAMBDA_10[3:]))",
         '''decimals=4, mistakes={"le facteur (n − 1)/n de la convention 1/(n − 1)": float(sum(LAMBDA_10[3:]))}'''),
    ]),

    Paper("M12d.11", "L'ACP par la SVD de la matrice centrée : s² / (n − 1) donne les variances", [
        ("a", "a list of 3 numbers", "exact(MU_11)"),
        ("b", "a matrix", "matrix(XC_11.T * XC_11)",
         '''mistakes={"centre d'abord : retire la moyenne à chaque ligne": matrix(X_11.T * X_11)}'''),
        ("c", "a list of 3 numbers", "[48, 18, 6]"),
        ("d", "a list of 3 numbers (4 decimals)", "[float(sq(48)), float(sq(18)), float(sq(6))]",
         '''decimals=4, mistakes={"une valeur singulière est la RACINE d'une valeur propre de X_cᵀX_c": [48, 18, 6], '''
         '''"les valeurs singulières de X_c ne sont pas les variances": [16, 6, 2]}'''),
        ("e", "a list of 3 numbers", "[16, 6, 2]",
         '''mistakes={"λ = s² / (n − 1), avec n − 1 = 3": [12, 4.5, 1.5], "divise s² par n − 1": [48, 18, 6]}'''),
        ("f", "a list of 3 numbers (4 decimals)", "exact(V1_11)", f'''decimals=4, mistakes={{"{UNIT}": [5, 3, 1]}}'''),
        ("g", "a list of 4 numbers (4 decimals)", "exact(XC_11 * V1_11 / sq(48))",
         '''decimals=4, mistakes={"u₁ = X_c v₁ / s₁ : divise par s₁": exact(XC_11 * V1_11)}'''),
        ("h", "a list of 4 numbers (4 decimals)", "exact(XC_11 * V1_11)",
         '''decimals=4, mistakes={"les scores se calculent sur les données CENTRÉES": exact(X_11 * V1_11), '''
         '''"les scores sont s₁ u₁ : multiplie par s₁": exact(XC_11 * V1_11 / sq(48))}'''),
    ]),

    Paper("M12d.12", "L'ACP quand n < p : passer par la petite matrice XXᵀ", [
        ("a", "a list of 5 numbers", "exact(MU_12)"),
        ("b", "a matrix", "matrix(XC_12 * XC_12.T)",
         '''mistakes={"centre d'abord : retire la moyenne à chaque ligne": matrix(X_12 * X_12.T)}'''),
        ("c", "a list of 3 numbers", "[38, 18, 0]", f'''mistakes={{"{DESC}": [0, 18, 38]}}'''),
        ("d", "a list of 2 numbers", "[19, 9]", '''mistakes={"λ = (valeur propre de G) / (n − 1), avec n − 1 = 2": [38, 18]}'''),
        ("e", "an integer", "3", '''mistakes={"au plus n − 1 = 2 variances non nulles parmi les 5 : compte les nulles": 2}'''),
        ("f", "a list of 5 numbers (4 decimals)", "exact(V1_12)",
         f'''decimals=4, mistakes={{"{SIGN}": exact(-V1_12), "normalise X_cᵀw : divise par sa norme": exact(XC_12.T * V([1, 0, -1]))}}'''),
        ("g", "a list of 3 numbers (4 decimals)", "exact(XC_12 * V1_12)",
         '''decimals=4, mistakes={"les scores se calculent sur les données CENTRÉES": exact(X_12 * V1_12)}'''),
    ]),

    Paper("M12d.13", "Les probabilités de voisinage de t-SNE sur quatre points, et leur perplexité 2^H", [
        ("a", "a list of 3 numbers", "[1, 2, 3]", '''mistakes={"les CARRÉS des distances": [1.0, float(sq(2)), float(sq(3))]}'''),
        ("b", "a list of 3 numbers (4 decimals)", "exact(P1_13)",
         '''decimals=4, mistakes={"normalise : divise chaque poids 2^(−d²) par la somme des trois": [0.5, 0.25, 0.125]}'''),
        ("c", "a number (4 decimals)", "float(H_13)",
         '''decimals=4, mistakes={"l'entropie en BITS : log₂, pas ln": float(H_13 * sympy.log(2))}'''),
        ("d", "a number (4 decimals)", "float(2 ** H_13)",
         '''decimals=4, mistakes={"la perplexité est 2 puissance l'entropie en bits": float(sympy.exp(H_13)), '''
         '''"3 est la limite quand σ → ∞ (trois voisins équiprobables) ; ici, calcule 2^H avec les probabilités de b)": 3.0}'''),
        ("e", "a number (4 decimals)", "0.4", '''decimals=4, mistakes={"vu de x₂ : ses voisins x₁ et x₃ sont tous deux à distance 1": float(sympy.Rational(4, 7))}'''),
        ("f", "a number (4 decimals)", "float(sympy.Rational(17, 140))",
         '''decimals=4, mistakes={"p_ij = (p_{j|i} + p_{i|j}) / (2n), avec n = 4 points": float(sympy.Rational(17, 35))}'''),
        ("g", "a number", "3", '''mistakes={"σ → ∞ : les trois voisins deviennent équiprobables": 1}'''),
    ]),

    Paper("M12d.20", "Pont : détecter une anomalie par son erreur de reconstruction", [
        ("a", "a number", "err_20(V([18, 12, 7]))"),
        ("b", "a number (4 decimals)", "float(err_20(V([13, 9, 9])))",
         '''decimals=4, mistakes={"l'erreur est le CARRÉ de la distance : le carré du score sur u₃": float(13 / sq(17)), '''
         '''"l'erreur ne compte que ce qui sort du plan des deux axes : le carré du score sur u₃, pas ‖r₂ − μ‖²": 10.0}'''),
        ("c", "a number (4 decimals)", "float(max(err_20(XC_8.row(i).T + MU_8) for i in range(7)))",
         '''decimals=4, mistakes={"la PLUS GRANDE erreur des sept objets, pas leur moyenne": float(sympy.Rational(18, 7))}'''),
        ("d", "True or False", "True", '''mistakes={"compare l'erreur de r₂ à la plus grande des sept": False}'''),
        ("e", "a number (4 decimals)", "float(U1_8.dot(V([30, 9, 10]) - MU_8))",
         '''decimals=4, mistakes={"le score se calcule sur l'objet CENTRÉ, r₃ − μ": float(U1_8.dot(V([30, 9, 10]))), '''
         '''"le score sur u₁ est u₁ᵀ(r₃ − μ), pas une coordonnée de r₃ − μ": 16.0}'''),
        ("f", "a number (4 decimals)", "float(max(abs(U1_8.dot(XC_8.row(i).T)) for i in range(7)))", "decimals=4"),
        ("g", "True or False", "False",
         '''mistakes={"r₃ − μ est un multiple de u₁ : il est dans le plan des deux premiers axes": True}'''),
    ]),

    Paper("M12d.21", "Pont : un changement d'unités diagonal D change Σ en DΣD, et les axes principaux avec ; la "
                     "standardisation non", [
        ("a", "a matrix", "matrix(D_21 * C_8 * D_21)",
         '''mistakes={"(DCD)ᵢⱼ = dᵢ dⱼ cᵢⱼ : la variance de la troisième mesure est multipliée par 3² = 9": '''
         '''[[19, 0, 12], [0, 11, 0], [12, 0, 12]], "(DCD)ᵢⱼ = dᵢ dⱼ cᵢⱼ : la covariance des mesures 1 et 3 est multipliée par 3": '''
         '''[[19, 0, 4], [0, 11, 0], [4, 0, 36]]}'''),
        ("b", "a list of 3 numbers (4 decimals)", "[float((55 + sq(865)) / 2), float((55 - sq(865)) / 2), 11.0]",
         f'''decimals=4, mistakes={{"{DESC}": [11.0, float((55 - sq(865)) / 2), float((55 + sq(865)) / 2)], '''
         f'''"par ordre décroissant : (55 − √865)/2 ≈ 12,79 est plus grand que 11": [float((55 + sq(865)) / 2), 11.0, float((55 - sq(865)) / 2)]}}'''),
        ("c", "a list of 3 numbers (4 decimals)", "exact(U1_21)",
         '''decimals=4, mistakes={"le premier axe de la NOUVELLE covariance": exact(U1_8), '''
         '''"le bloc porte sur les mesures 1 et 3 : la deuxième coordonnée est nulle": [float(U1_21[0]), float(U1_21[2]), 0.0]}'''),
        ("d", "a number (4 decimals)", "float((55 + sq(865)) / 2 / 66)",
         '''decimals=4, mistakes={"la variance totale a changé aussi : 19 + 11 + 36": float((55 + sq(865)) / 2 / 34)}'''),
        ("e", "a number (4 decimals)", "float(2 / sq(19))",
         '''decimals=4, mistakes={"divise par le produit des écarts-types, pas des variances": float(sympy.Rational(4, 76))}'''),
        ("f", "a number (1 decimal)", "float(sympy.acos(U1_8.dot(U1_21)) * 180 / sympy.pi)",
         '''decimals=1, mistakes={"l'angle en DEGRÉS : arccos du produit scalaire des deux axes unitaires, puis × 180/π": float(sympy.acos(U1_8.dot(U1_21)))}'''),
        ("g", "a matrix (4 decimals)", "floats(CORR_21)",
         '''decimals=4, mistakes={"standardiser donne la matrice de CORRÉLATION, de diagonale 1": floats(D_21 * C_8 * D_21)}'''),
        ("h", "True or False", "True",
         '''mistakes={"dᵢdⱼcᵢⱼ / √(dᵢ²cᵢᵢ dⱼ²cⱼⱼ) : les dᵢ se simplifient": False}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly (SymPy) from the statements
import numpy as np
import sympy


def exact(values):
    """SymPy or NumPy numbers as Python ints when whole, else floats."""
    return [int(v) if v == int(v) else float(v) for v in values]


def matrix(M):
    """A matrix as a list of rows of exact numbers."""
    return [exact(row) for row in sympy.Matrix(M).tolist()]


def floats(M):
    """A matrix as a list of rows of floats."""
    return [[float(v) for v in row] for row in sympy.Matrix(M).tolist()]


def qf(M, w):
    """The quadratic form wᵀ M w."""
    w = sympy.Matrix(w)
    return (w.T * M * w)[0]


V, sq = sympy.Matrix, sympy.sqrt
A_1 = V([[10, 10], [5, 2]])                                                                 # M12d.1
V1_1, V2_1 = V([11, 10]) / sq(221), V([-10, 11]) / sq(221)
U1_1 = A_1 * V1_1 / 15
assert A_1.T * A_1 * V([11, 10]) == 225 * V([11, 10]) and A_1.T * A_1 * V([-10, 11]) == 4 * V([-10, 11])
A_2 = V([[2, -10], [10, -50], [11, -55]])                                                   # M12d.2
V1_2, V2_2 = V([-1, 5]) / sq(26), V([5, 1]) / sq(26)
U1_2 = A_2 * V1_2 / (15 * sq(26))
assert A_2 * V([5, 1]) == V([0, 0, 0])
B_3 = V([[1, 8], [4, -4]])                                                                  # M12d.3
V1_3 = V([-1, 8]) / sq(65)
U1_3 = B_3 * V1_3 / 9
assert B_3.T * B_3 * V([-1, 8]) == 81 * V([-1, 8])
A_4 = V([[4, 2, 1], [4, 2, -1], [1, 4, 0]])                                                 # M12d.4
V1_4 = V([5, 4, 0]) / sq(41)
U1_4 = A_4 * V1_4 / 7
A1_4 = 7 * U1_4 * V1_4.T
assert A_4.T * A_4 * V([5, 4, 0]) == 49 * V([5, 4, 0])
A_6 = V([[2, -8, 16], [5, -20, 40]])                                                        # M12d.6
P_6 = A_6.T / 2349
assert sympy.simplify(A_6 * P_6 * A_6 - A_6) == sympy.zeros(2, 3)
R_7 = V([[8, 3], [5, 2]])                                                                   # M12d.7
KAPPA_7 = 51 + 10 * sq(26)
AMPL_7 = ((R_7.solve(V([sympy.Rational(1, 100), 0]))).norm() / (R_7.solve(V([14, 9]))).norm()) / (sympy.Rational(1, 100) / V([14, 9]).norm())
assert abs(float(KAPPA_7) - np.linalg.cond(np.array([[8.0, 3.0], [5.0, 2.0]]))) < 1e-9
X_8 = V([[10, 8, 3], [9, 14, 7], [15, 4, 9], [10, 6, 4], [16, 11, 6], [18, 10, 6], [20, 10, 7]])   # M12d.8
MU_8 = V([sum(X_8[:, j]) / 7 for j in range(3)])
XC_8 = X_8 - sympy.ones(7, 1) * MU_8.T
C_8 = XC_8.T * XC_8 / 6
U1_8, U2_8, U3_8 = V([4, 0, 1]) / sq(17), V([0, 1, 0]), V([-1, 0, 4]) / sq(17)
assert C_8 * U1_8 == 20 * U1_8 and C_8 * U2_8 == 11 * U2_8 and C_8 * U3_8 == 3 * U3_8
D7_9 = X_8.row(6).T - MU_8                                                                  # M12d.9
REC7_9 = MU_8 + U1_8.dot(D7_9) * U1_8 + U2_8.dot(D7_9) * U2_8
LAMBDA_10 = [sympy.Rational(v, 10) for v in (96, 48, 24, 11, 7, 6, 5, 3)]                   # M12d.10
X_11 = V([[3, 1, 3], [3, 4, 6], [9, 4, 8], [9, 7, 3]])                                       # M12d.11
MU_11 = V([sum(X_11[:, j]) / 4 for j in range(3)])
XC_11 = X_11 - sympy.ones(4, 1) * MU_11.T
V1_11 = V([5, 3, 1]) / sq(35)
assert [XC_11.T * XC_11 * V(d) == k * V(d) for d, k in (([5, 3, 1], 48), ([0, -1, 3], 18), ([-2, 3, 1], 6))] == [True] * 3
X_12 = V([[8, 8, 4, 6, 5], [3, 8, 3, 2, 7], [4, 2, 2, 4, 9]])                                # M12d.12
MU_12 = V([sum(X_12[:, j]) / 3 for j in range(5)])
XC_12 = X_12 - sympy.ones(3, 1) * MU_12.T
V1_12 = XC_12.T * V([1, 0, -1]) / (XC_12.T * V([1, 0, -1])).norm()
assert (XC_12 * XC_12.T) * V([1, 0, -1]) == 38 * V([1, 0, -1])
P1_13 = [sympy.Rational(4, 7), sympy.Rational(2, 7), sympy.Rational(1, 7)]                  # M12d.13
H_13 = -sum(p * sympy.log(p, 2) for p in P1_13)


def err_20(x):                                                                              # M12d.20
    """The reconstruction error of x with the first two axes of the cloud of M12d.8: its squared score on u₃."""
    return U3_8.dot(x - MU_8) ** 2


D_21 = sympy.diag(1, 1, 3)                                                                  # M12d.21
_vals_21 = (D_21 * C_8 * D_21).eigenvects()
_top_21 = max(_vals_21, key=lambda e: float(e[0]))[2][0]
U1_21 = _top_21 / _top_21.norm()
U1_21 = U1_21 if max(U1_21, key=lambda v: abs(float(v))) > 0 else -U1_21
_s_21 = sympy.diag(*[1 / sq(C_8[i, i]) for i in range(3)])
CORR_21 = _s_21 * C_8 * _s_21'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M12d.1 à M12d.13, 🔗 M12d.20 et M12d.21)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une liste `[0, -2, 5]` pour un vecteur (les valeurs singulières et les variances par ordre "
               "décroissant), une liste de lignes `[[1, 0], [-2, 3]]` pour une matrice, ou `True` / `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M12d.26 to M12d.30)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np

from wbm.nbtools import StopCheck, checked, drawn, run_pytest_group


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


def make_conditioned(kappa, seed=33, m=6, n=4):
    """A (m, n) matrix of singular values 1, ..., 1/kappa (geometric), from two random orthonormal bases."""
    rng = np.random.default_rng(seed)
    Q1, _ = np.linalg.qr(rng.normal(size=(m, n)))
    Q2, _ = np.linalg.qr(rng.normal(size=(n, n)))
    return (Q1 * kappa ** (-np.arange(n) / (n - 1))) @ Q2.T'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12d")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/svd_pca.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "NumPy est permis, `@`, `.T`, `np.linalg.norm`, `np.linalg.solve` et `np.linalg.eigh` compris ; "
         "`np.linalg.svd`, `pinv`, `cond`, `lstsq`, `matrix_rank`, `scipy.linalg` et scikit-learn sont interdits "
         "(les tests comparent tes résultats aux leurs, et un test vérifie que tu ne t'en sers pas). Ne modifie "
         "jamais la matrice reçue : travaille sur une copie, `np.array(A, dtype=float)`. Les nombres se rendent en "
         "`float` de Python, les vecteurs et les matrices en tableaux NumPy de flottants.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError", "LinAlgError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def value_error(message: str) -> str:
    return (f'''mistakes={{"{message}": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}}''')


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of svd_pca.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_svd_pca_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m12d_svd_pca.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m12d_svd_pca.py", "{keyword}", impl="ref")')]


A_26 = "[[2, 3, -1], [0, 4, 2]]"
R_26 = "[[1, -3], [2, -6], [-1, 3]]"

M12D_26 = Ex(
    "M12d.26", "🔨", 2, 25, "La SVD par les valeurs propres de AᵀA · `svd`",
    "programmer la SVD compacte par les valeurs et vecteurs propres de $\\mathbf{A}^\\top\\mathbf{A}$, avec son seuil "
    "de rang numérique et sa convention de signe.", "fiche §1", tracks="C, E", mymath="svd_pca.py",
    body=HOWTO + r"""

Écris `svd(A, tol=1e-6)` (fiche §1), en suivant la docstring : une copie en flottants (`ValueError` si $\mathbf{A}$ n'est pas une matrice) ; `np.linalg.eigh` de $\mathbf{A}^\top\mathbf{A}$ ; les valeurs propres **écrêtées** à 0 (`np.clip`, avant la racine : un $-10^{-17}$ d'arrondi donnerait `nan`) et rangées par ordre décroissant, avec leurs vecteurs propres ; $s = \sqrt{\lambda}$ ; seules les valeurs **strictement** supérieures à `tol` fois la plus grande sont gardées ; la convention de signe sur chaque vecteur gardé (sa coordonnée de plus grande valeur absolue positive) ; enfin $\mathbf{U} = \mathbf{A}\mathbf{V}/s$, colonne par colonne. Une matrice nulle a $r = 0$ : `U`, `s` et `Vt` de formes $(m, 0)$, $(0,)$ et $(0, n)$.

La vérification calcule :
- a) les valeurs singulières de `svd(""" + A_26 + r""")` (une liste, 6 décimales) ;
- b) son `Vt` (une matrice, 6 décimales) ;
- c) vrai ou faux : pour une matrice $7 \times 4$ tirée au hasard (`np.random.default_rng(26)`, loi normale), `U @ np.diag(s) @ Vt` redonne $\mathbf{A}$, $\mathbf{U}^\top\mathbf{U}$ et $\mathbf{V}^\top\mathbf{V}$ valent $\mathbf{I}$, et `s` est égal aux valeurs de `np.linalg.svd`, le tout à $10^{-10}$ près ;
- d) le nombre de valeurs singulières gardées pour `""" + R_26 + r"""` ;
- e) les formes de `(U, s, Vt)` pour la matrice $3 \times 5$ `np.arange(15.0).reshape(3, 5) + np.eye(3, 5)`, en texte : `str((U.shape, s.shape, Vt.shape))` ;
- f) le nom de l'erreur levée par `svd([1, 2, 3])` ;
- g) vrai ou faux : après `svd(M)`, le tableau `M` (une copie en flottants de la matrice de a)) n'a pas changé.

Dans ta copie : retrouve a) à la main par $\mathbf{A}\mathbf{A}^\top$ (de forme $2 \times 2$, plus petite que $\mathbf{A}^\top\mathbf{A}$) : pourquoi a-t-elle les mêmes valeurs propres non nulles ? Pourquoi la matrice de d) n'a-t-elle qu'une valeur singulière, et que vaut-elle ?""",
    todo=LOAD_LEARNER,
    check=f'''A_26r = np.random.default_rng(26).normal(size=(7, 4))
with checked("M12d.26a"):
    wbm.check("M12d.26a", np.asarray(mymath.svd_pca.svd({A_26})[1]).tolist(), computed=True)
with checked("M12d.26b"):
    wbm.check("M12d.26b", np.asarray(mymath.svd_pca.svd({A_26})[2]).tolist(), computed=True)
with checked("M12d.26c"):
    U_26, s_26, Vt_26 = (np.asarray(x) for x in mymath.svd_pca.svd(A_26r))
    wbm.check("M12d.26c", bool(s_26.shape == (4,) and np.allclose(U_26 @ np.diag(s_26) @ Vt_26, A_26r, rtol=0, atol=1e-10)
                               and np.allclose(U_26.T @ U_26, np.eye(4), rtol=0, atol=1e-10)
                               and np.allclose(Vt_26 @ Vt_26.T, np.eye(4), rtol=0, atol=1e-10)
                               and np.allclose(s_26, np.linalg.svd(A_26r, compute_uv=False), rtol=0, atol=1e-10)),
              computed=True)
with checked("M12d.26d"):
    wbm.check("M12d.26d", len(mymath.svd_pca.svd({R_26})[1]), computed=True)
with checked("M12d.26e"):
    wbm.check("M12d.26e", str(tuple(np.asarray(x).shape for x in mymath.svd_pca.svd(np.arange(15.0).reshape(3, 5) + np.eye(3, 5)))),
              computed=True)
with checked("M12d.26f"):
    wbm.check("M12d.26f", raised(mymath.svd_pca.svd, [1, 2, 3]), computed=True)
with checked("M12d.26g"):
    M_26 = np.array({A_26}, dtype=float)
    mymath.svd_pca.svd(M_26)
    wbm.check("M12d.26g", bool(np.array_equal(M_26, np.array({A_26}, dtype=float))), computed=True)''',
    solution=LOAD_REF + f'''
svd = mymath.svd_pca.svd
A_26r = np.random.default_rng(26).normal(size=(7, 4))
U_26, s_26, Vt_26 = svd({A_26})
print("a)", np.round(s_26, 6).tolist(), " b)", np.round(Vt_26, 6).tolist())
U_26, s_26, Vt_26 = svd(A_26r)
print("c)", bool(np.allclose(U_26 @ np.diag(s_26) @ Vt_26, A_26r, rtol=0, atol=1e-10)
                 and np.allclose(U_26.T @ U_26, np.eye(4), rtol=0, atol=1e-10)
                 and np.allclose(Vt_26 @ Vt_26.T, np.eye(4), rtol=0, atol=1e-10)
                 and np.allclose(s_26, np.linalg.svd(A_26r, compute_uv=False), rtol=0, atol=1e-10)))
print("d)", len(svd({R_26})[1]), " e)", str(tuple(x.shape for x in svd(np.arange(15.0).reshape(3, 5) + np.eye(3, 5)))),
      " f)", raised(svd, [1, 2, 3]))
M_26 = np.array({A_26}, dtype=float)
svd(M_26)
print("g)", bool(np.array_equal(M_26, np.array({A_26}, dtype=float))))''',
    record=f'''A_26n = np.array({A_26}, dtype=float)
s_26n = np.linalg.svd(A_26n, compute_uv=False)
_, vectors_26n = np.linalg.eigh(A_26n.T @ A_26n)
Vt_26n = vectors_26n[:, ::-1][:, :2].T
Vt_26n = Vt_26n * np.where(Vt_26n[np.arange(2), np.argmax(np.abs(Vt_26n), axis=1)] < 0, -1.0, 1.0)[:, None]
wbm.record("M12d.26a", s_26n.tolist(), decimals=6,
           mistakes={{"une valeur singulière est la RACINE d'une valeur propre de AᵀA": (s_26n ** 2).tolist(),
                     "l'ordre décroissant : eigh rend les valeurs propres par ordre croissant, retourne-les": s_26n[::-1].tolist()}})
wbm.record("M12d.26b", Vt_26n.tolist(), decimals=6,
           mistakes={{"la convention de signe : la coordonnée de plus grande valeur absolue de chaque LIGNE de Vt positive":
                         (-Vt_26n).tolist(),
                     "l'ordre décroissant : la première ligne de Vt va avec la plus grande valeur singulière": Vt_26n[::-1].tolist()}})
wbm.record("M12d.26c", True,
           mistakes={{"compare tes U, s, Vt à np.linalg.svd sur une matrice que tu sais faire à la main : l'ordre, la "
                      "racine, U = A V / s (en divisant chaque colonne)": False}})
wbm.record("M12d.26d", 1,
           mistakes={{"garde seulement les s STRICTEMENT supérieures à tol fois la plus grande : la seconde n'est qu'un arrondi": 2}})
wbm.record("M12d.26e", "((3, 3), (3,), (3, 5))",
           mistakes={{"U est de forme (m, r) et Vt de forme (r, n), avec r = 3 valeurs gardées": "((3, 5), (5,), (5, 5))"}})
wbm.record("M12d.26f", "ValueError",
           {value_error("un vecteur n'est pas une matrice 2-D : la docstring demande une ValueError")})
wbm.record("M12d.26g", True,
           mistakes={{"travaille sur une copie : np.array(A, dtype=float), pas np.asarray(A)": False}})''',
    after=tests_cells("test_svd_"),
    note=r"a) $\mathbf{A}\mathbf{A}^\top = \begin{pmatrix} 14 & 10 \\ 10 & 20 \end{pmatrix}$ : trace 34, déterminant 180, "
         r"donc $\lambda = 17 \pm \sqrt{109}$ et $s = \sqrt{17 \pm \sqrt{109}} \approx 5{,}238$ et $2{,}561$ ; "
         r"$\mathbf{A}^\top\mathbf{A}$, de forme $3 \times 3$, a ces deux valeurs propres et 0 (fiche §1). d) Les deux "
         r"colonnes sont proportionnelles : $\mathbf{A} = (1, 2, -1)^\top(1, -3)$, de rang 1, $s_1 = \sqrt{6}\sqrt{10} = "
         r"\sqrt{60}$ ; la seconde valeur propre de $\mathbf{A}^\top\mathbf{A}$ n'est qu'un arrondi, sous le seuil.",
)

A_27 = "[[4, 1, -2], [1, 3, 2]]"
K_27 = "[[5, 3], [4, 2.5]]"
Z_27 = "[[3, -6], [-1, 2]]"

M12D_27 = Ex(
    "M12d.27", "🔨", 1, 20, "Approximation de rang faible et conditionnement · `low_rank_approximation, condition_number`",
    "programmer la meilleure approximation de rang $k$ et le conditionnement à partir de ta fonction `svd`.",
    "fiche §3 et §4 ; Ex M12d.26", tracks="C, E", mymath="svd_pca.py",
    body=r"""Écris, en suivant les docstrings, avec ta fonction `svd` :
- `low_rank_approximation(A, k)` (fiche §3) : `ValueError` si `k` n'est pas un entier (un `bool` non plus) entre 0 et $\min(m, n)$ ; puis $\sum_{i \le k} s_i\mathbf{u}_i\mathbf{v}_i^\top$ (les $k$ premières colonnes de `U`, valeurs de `s`, lignes de `Vt` ; si `svd` en garde moins de $k$, toutes) ;
- `condition_number(A)` (fiche §4) : `ValueError` si $\mathbf{A}$ est nulle ; `math.inf` si `svd` garde moins de $\min(m, n)$ valeurs ; sinon $s_1/s_r$, en `float` de Python.

La vérification calcule :
- a) `low_rank_approximation(""" + A_27 + r""", 1)` (une matrice, 6 décimales) ;
- b) vrai ou faux : pour une matrice $6 \times 5$ tirée au hasard (`np.random.default_rng(27)`), $\lVert \mathbf{A} - \mathbf{A}_k \rVert_F^2 = \sum_{i > k} s_i^2$ à $10^{-9}$ près, relativement à $\lVert \mathbf{A} \rVert_F^2$, pour $k = 0, 1, \ldots, 5$ (les $s_i$ de `np.linalg.svd`) ;
- c) `condition_number(""" + K_27 + r""")` (4 décimales) ;
- d) vrai ou faux : `condition_number(""" + Z_27 + r""") == math.inf` ;
- e) le nom de l'erreur levée par `low_rank_approximation([[1, 2], [3, 4]], 3)` ;
- f) le nom de l'erreur levée par `condition_number([[0, 0], [0, 0]])` ;
- g) vrai ou faux : `type(condition_number(""" + K_27 + r"""))` est `float`.

Dans ta copie : retrouve c) à la main, avec $s_1^2 + s_2^2 = \lVert \mathbf{A} \rVert_F^2$ et $s_1s_2 = \lvert\det\mathbf{A}\rvert$. Pourquoi la matrice de d) a-t-elle un conditionnement infini ? Que rend `low_rank_approximation(A, min(m, n))`, et pourquoi pas exactement $\mathbf{A}$ ?""",
    todo=LOAD_LEARNER,
    check=f'''A_27r = np.random.default_rng(27).normal(size=(6, 5))
s_27r = np.linalg.svd(A_27r, compute_uv=False)
with checked("M12d.27a"):
    wbm.check("M12d.27a", np.asarray(mymath.svd_pca.low_rank_approximation({A_27}, 1)).tolist(), computed=True)
with checked("M12d.27b"):
    errors_27 = [float(np.sum((A_27r - np.asarray(mymath.svd_pca.low_rank_approximation(A_27r, k))) ** 2)) for k in range(6)]
    wbm.check("M12d.27b", all(abs(e - float(np.sum(s_27r[k:] ** 2))) <= 1e-9 * float(np.sum(s_27r ** 2))
                              for k, e in enumerate(errors_27)), computed=True)
with checked("M12d.27c"):
    wbm.check("M12d.27c", mymath.svd_pca.condition_number({K_27}), computed=True)
with checked("M12d.27d"):
    wbm.check("M12d.27d", bool(mymath.svd_pca.condition_number({Z_27}) == math.inf), computed=True)
with checked("M12d.27e"):
    wbm.check("M12d.27e", raised(mymath.svd_pca.low_rank_approximation, [[1, 2], [3, 4]], 3), computed=True)
with checked("M12d.27f"):
    wbm.check("M12d.27f", raised(mymath.svd_pca.condition_number, [[0, 0], [0, 0]]), computed=True)
with checked("M12d.27g"):
    wbm.check("M12d.27g", type(mymath.svd_pca.condition_number({K_27})) is float, computed=True)''',
    solution=LOAD_REF + f'''
low_rank_approximation, condition_number = mymath.svd_pca.low_rank_approximation, mymath.svd_pca.condition_number
A_27r = np.random.default_rng(27).normal(size=(6, 5))
s_27r = np.linalg.svd(A_27r, compute_uv=False)
errors_27 = [float(np.sum((A_27r - low_rank_approximation(A_27r, k)) ** 2)) for k in range(6)]
print("a)", np.round(low_rank_approximation({A_27}, 1), 6).tolist())
print("b)", all(abs(e - float(np.sum(s_27r[k:] ** 2))) <= 1e-9 * float(np.sum(s_27r ** 2)) for k, e in enumerate(errors_27)))
print("c)", round(condition_number({K_27}), 4), " d)", condition_number({Z_27}) == math.inf,
      " e)", raised(low_rank_approximation, [[1, 2], [3, 4]], 3), " f)", raised(condition_number, [[0, 0], [0, 0]]),
      " g)", type(condition_number({K_27})) is float)''',
    record=f'''A_27n = np.array({A_27}, dtype=float)
U_27n, s_27n, Vt_27n = np.linalg.svd(A_27n, full_matrices=False)
best_27 = s_27n[0] * np.outer(U_27n[:, 0], Vt_27n[0])
wbm.record("M12d.27a", best_27.tolist(), decimals=6,
           mistakes={{"A₁ = s₁ u₁ v₁ᵀ : n'oublie pas la valeur singulière": (best_27 / s_27n[0]).tolist(),
                     "garde la PLUS GRANDE valeur singulière, la première de svd": (s_27n[1] * np.outer(U_27n[:, 1], Vt_27n[1])).tolist()}})
wbm.record("M12d.27b", True,
           mistakes={{"l'erreur au carré est la somme des s² oubliés : vérifie k = 0 (A elle-même) et k = min(m, n) (zéro)": False}})
s_27k = np.linalg.svd(np.array({K_27}), compute_uv=False)
wbm.record("M12d.27c", float(s_27k[0] / s_27k[-1]), decimals=4,
           mistakes={{"κ = s_max / s_min, avec les valeurs singulières (les racines)": float((s_27k[0] / s_27k[-1]) ** 2),
                     "le plus grand sur le plus petit": float(s_27k[-1] / s_27k[0])}})
wbm.record("M12d.27d", True,
           mistakes={{"une matrice de rang 1 : svd ne garde qu'une valeur singulière, rends math.inf": False}})
wbm.record("M12d.27e", "ValueError",
           {value_error("k = 3 dépasse min(m, n) = 2 : la docstring demande une ValueError")})
wbm.record("M12d.27f", "ValueError",
           {value_error("une matrice nulle n'a pas de conditionnement : la docstring demande une ValueError")})
wbm.record("M12d.27g", True,
           mistakes={{"rends un float de Python : float(s[0] / s[-1]), pas un np.float64": False}})''',
    after=tests_cells("test_low_rank_ or test_condition_number_"),
    note=r"c) $s_1^2 + s_2^2 = 25 + 9 + 16 + 6{,}25 = 56{,}25$ et $s_1s_2 = \lvert 12{,}5 - 12 \rvert = 0{,}5$ : $s_1^2$ "
         r"et $s_2^2$ sont les racines de $x^2 - 56{,}25\,x + 0{,}25$, et $\kappa = s_1/s_2 \approx 56{,}25/0{,}5 = 112{,}5$ "
         r"à peu près. d) $(3, -6) = -3\,(-1, 2)$ : les lignes sont proportionnelles, la seconde valeur singulière est nulle. "
         r"Le rang plein redonne $\mathbf{A}$ aux arrondis près : $\mathbf{U}$ vient de $\mathbf{A}\mathbf{V}/s$.",
)

A_28 = "[[2, 0, 1], [0, 3, 0]]"

M12D_28 = Ex(
    "M12d.28", "🔨", 1, 15, "La pseudo-inverse · `pinv`",
    "programmer la pseudo-inverse par la SVD, avec son seuil sur les petites valeurs singulières.",
    "fiche §4 ; Ex M12d.26", tracks="C", mymath="svd_pca.py",
    body=r"""Écris `pinv(A, rcond=1e-6)` (fiche §4), en suivant la docstring : `svd(A, tol=rcond)`, puis $\mathbf{V}\operatorname{diag}(1/s)\mathbf{U}^\top$ (divise les colonnes de `Vt.T` par `s`, sans former de matrice diagonale), de forme $(n, m)$ ; une matrice nulle donne des zéros.

La vérification calcule :
- a) `pinv(""" + A_28 + r""")` (une matrice, 6 décimales) ;
- b) vrai ou faux : pour une matrice $\mathbf{A}$ de forme $5 \times 3$ et de rang 2 tirée au hasard (cellule de vérification), $\mathbf{A}^+$ vérifie les quatre conditions de Penrose à $10^{-8}$ près : $\mathbf{A}\mathbf{A}^+\mathbf{A} = \mathbf{A}$, $\mathbf{A}^+\mathbf{A}\mathbf{A}^+ = \mathbf{A}^+$, $\mathbf{A}\mathbf{A}^+$ et $\mathbf{A}^+\mathbf{A}$ symétriques ;
- c) vrai ou faux : pour la même matrice et $\mathbf{b} = (1, 2, 3, 4, 5)$, `pinv(A) @ b` est la solution de `np.linalg.lstsq(A, b)` à $10^{-8}$ près ;
- d) la forme de `pinv(np.zeros((2, 3)))`, en texte : `str(pinv(...).shape)` ;
- e) l'élément `[1, 1]` de `pinv(np.diag([1.0, 1e-8]))`, puis de `pinv(np.diag([1.0, 1e-8]), rcond=1e-10)` (une liste de 2 nombres, 2 décimales) ;
- f) le nom de l'erreur levée par `pinv([1, 2])`.

Dans ta copie : retrouve a) à la main (les lignes de $\mathbf{A}$ sont orthogonales : $\mathbf{A}\mathbf{A}^\top$ est diagonale, et $\mathbf{A}^+ = \mathbf{A}^\top(\mathbf{A}\mathbf{A}^\top)^{-1}$). Que vaut $\mathbf{A}\mathbf{A}^+$ ? Pourquoi e) donne-t-il deux valeurs si différentes, et laquelle préférer si $10^{-8}$ est une erreur de mesure ?""",
    todo=LOAD_LEARNER,
    check=f'''rng_28 = np.random.default_rng(28)
A_28r = rng_28.normal(size=(5, 2)) @ rng_28.normal(size=(2, 3))
b_28 = np.arange(1.0, 6.0)
with checked("M12d.28a"):
    wbm.check("M12d.28a", np.asarray(mymath.svd_pca.pinv({A_28})).tolist(), computed=True)
with checked("M12d.28b"):
    P_28 = np.asarray(mymath.svd_pca.pinv(A_28r))
    wbm.check("M12d.28b", bool(P_28.shape == (3, 5) and np.allclose(A_28r @ P_28 @ A_28r, A_28r, rtol=0, atol=1e-8)
                               and np.allclose(P_28 @ A_28r @ P_28, P_28, rtol=0, atol=1e-8)
                               and np.allclose(A_28r @ P_28, (A_28r @ P_28).T, rtol=0, atol=1e-8)
                               and np.allclose(P_28 @ A_28r, (P_28 @ A_28r).T, rtol=0, atol=1e-8)), computed=True)
with checked("M12d.28c"):
    wbm.check("M12d.28c", bool(np.allclose(np.asarray(mymath.svd_pca.pinv(A_28r)) @ b_28,
                                           np.linalg.lstsq(A_28r, b_28, rcond=None)[0], rtol=0, atol=1e-8)), computed=True)
with checked("M12d.28d"):
    wbm.check("M12d.28d", str(np.asarray(mymath.svd_pca.pinv(np.zeros((2, 3)))).shape), computed=True)
with checked("M12d.28e"):
    wbm.check("M12d.28e", [float(np.asarray(mymath.svd_pca.pinv(np.diag([1.0, 1e-8])))[1, 1]),
                           float(np.asarray(mymath.svd_pca.pinv(np.diag([1.0, 1e-8]), rcond=1e-10))[1, 1])], computed=True)
with checked("M12d.28f"):
    wbm.check("M12d.28f", raised(mymath.svd_pca.pinv, [1, 2]), computed=True)''',
    solution=LOAD_REF + f'''
pinv = mymath.svd_pca.pinv
rng_28 = np.random.default_rng(28)
A_28r = rng_28.normal(size=(5, 2)) @ rng_28.normal(size=(2, 3))
b_28 = np.arange(1.0, 6.0)
P_28 = pinv(A_28r)
print("a)", np.round(pinv({A_28}), 6).tolist())
print("b)", bool(np.allclose(A_28r @ P_28 @ A_28r, A_28r, rtol=0, atol=1e-8) and np.allclose(P_28 @ A_28r @ P_28, P_28, rtol=0, atol=1e-8)
                 and np.allclose(A_28r @ P_28, (A_28r @ P_28).T, rtol=0, atol=1e-8) and np.allclose(P_28 @ A_28r, (P_28 @ A_28r).T, rtol=0, atol=1e-8)),
      " c)", bool(np.allclose(P_28 @ b_28, np.linalg.lstsq(A_28r, b_28, rcond=None)[0], rtol=0, atol=1e-8)))
print("d)", str(pinv(np.zeros((2, 3))).shape),
      " e)", [float(pinv(np.diag([1.0, 1e-8]))[1, 1]), float(pinv(np.diag([1.0, 1e-8]), rcond=1e-10)[1, 1])],
      " f)", raised(pinv, [1, 2]))''',
    record=f'''P_28n = np.linalg.pinv(np.array({A_28}, dtype=float))
wbm.record("M12d.28a", P_28n.tolist(), decimals=6,
           mistakes={{"A⁺ est de forme (n, m) : V diag(1/s) Uᵀ, pas sa transposée": P_28n.T.tolist(),
                     "A⁺ divise par les valeurs singulières : V diag(1/s) Uᵀ, pas V diag(s) Uᵀ": np.array({A_28}, dtype=float).T.tolist()}})
wbm.record("M12d.28b", True,
           mistakes={{"une matrice de rang 2 : svd ne garde que 2 valeurs, et V diag(1/s) Uᵀ les inverse seules": False}})
wbm.record("M12d.28c", True,
           mistakes={{"A⁺ b est la solution des moindres carrés de plus petite norme : celle de lstsq": False}})
wbm.record("M12d.28d", "(3, 2)",
           mistakes={{"une matrice nulle : A⁺ est nulle, de forme (n, m)": "(2, 3)"}})
wbm.record("M12d.28e", [0.0, 1e8], decimals=2,
           mistakes={{"passe rcond à svd (tol=rcond) : avec rcond = 1e−6, la valeur 1e−8 est traitée comme nulle": [1e8, 1e8],
                     "avec rcond = 1e−10, la valeur 1e−8 est gardée, et inversée": [0.0, 0.0]}})
wbm.record("M12d.28f", "ValueError",
           {value_error("un vecteur n'est pas une matrice 2-D : la docstring demande une ValueError")})''',
    after=tests_cells("test_pinv_"),
    note=r"a) $\mathbf{A}\mathbf{A}^\top = \operatorname{diag}(5, 9)$, donc $\mathbf{A}^+ = \mathbf{A}^\top\operatorname{diag}"
         r"(\frac{1}{5}, \frac{1}{9}) = \begin{pmatrix} 0{,}4 & 0 \\ 0 & \frac{1}{3} \\ 0{,}2 & 0 \end{pmatrix}$, et "
         r"$\mathbf{A}\mathbf{A}^+ = \mathbf{I}_2$ (lignes libres). e) Avec le seuil par défaut, $10^{-8} < 10^{-6} \times 1$ : "
         r"la valeur est traitée comme nulle, et la pseudo-inverse l'ignore ; avec $10^{-10}$, elle est gardée et inversée en "
         r"$10^8$. Si $10^{-8}$ est du bruit, le seuil évite d'amplifier ce bruit cent millions de fois.",
)

C_29 = "[[10, 0, -15], [0, 6, 0], [-15, 0, 26]]"

M12D_29 = Ex(
    "M12d.29", "🔨", 2, 25, "Les axes principaux d'une matrice de covariance, et la variance expliquée · "
    "`principal_axes, explained_variance_ratio`",
    "programmer les axes principaux d'une matrice de covariance, avec leurs contrôles et leur convention de signe, et "
    "la part de variance expliquée.", "fiche §5 à §7", tracks="C, E", mymath="svd_pca.py",
    body=r"""Écris, en suivant les docstrings :
- `principal_axes(C, k=None)` (fiche §5) : `ValueError` si $\mathbf{C}$ n'est pas carrée, pas symétrique (relativement, comme dit la docstring), ou a une valeur propre sous $-10^{-12}\max(1, \lambda_{\max})$, ou si `k` n'est pas un entier entre 1 et $p$ ; puis `np.linalg.eigh`, l'ordre **décroissant**, les $k$ premiers axes **en colonnes** avec la convention de signe, et les variances (une valeur propre négative minuscule rendue comme 0, jamais $-0{,}0$) ;
- `explained_variance_ratio(variances)` (fiche §7) : `ValueError` si le tableau n'est pas 1-D, est vide, a une valeur négative ou une somme nulle ; sinon les parts, dans le même ordre.

La vérification calcule, avec $\mathbf{C}$ = `""" + C_29 + r"""` :
- a) les axes rendus par `principal_axes(C)` (une matrice, 6 décimales) ;
- b) les variances rendues (une liste, 6 décimales) ;
- c) `explained_variance_ratio` de ces variances (une liste, 6 décimales) ;
- d) vrai ou faux : pour la covariance (`np.cov(..., rowvar=False)`) de $300$ exemples de $\mathbb{R}^5$ tirés au hasard (cellule de vérification), les axes sont orthonormés, vérifient $\mathbf{C}\mathbf{u}_j = \lambda_j\mathbf{u}_j$, et sont égaux aux lignes de `PCA().fit(X).components_` de scikit-learn, le tout à $10^{-8}$ près ;
- e) la forme des axes rendus par `principal_axes(C, k=1)`, en texte ;
- f) le nom de l'erreur levée par `principal_axes([[1, 2], [3, 4]])` ;
- g) le nom de l'erreur levée par `principal_axes([[1, 0], [0, -1]])` ;
- h) le nom de l'erreur levée par `explained_variance_ratio([0, 0])`.

Dans ta copie : retrouve a) et b) à la main, par la structure par blocs de $\mathbf{C}$ (fiche §5). Pourquoi la première colonne de a) a-t-elle une première coordonnée négative ? Que vaut la part cumulée des deux premiers axes ?""",
    todo=LOAD_LEARNER,
    check=f'''from sklearn.decomposition import PCA

X_29 = np.random.default_rng(29).normal(size=(300, 5)) @ np.diag([3.0, 2.0, 1.5, 1.0, 0.5])
cov_29 = np.cov(X_29, rowvar=False)
with checked("M12d.29a"):
    wbm.check("M12d.29a", np.asarray(mymath.svd_pca.principal_axes({C_29})[0]).tolist(), computed=True)
with checked("M12d.29b"):
    wbm.check("M12d.29b", np.asarray(mymath.svd_pca.principal_axes({C_29})[1]).tolist(), computed=True)
with checked("M12d.29c"):
    wbm.check("M12d.29c", np.asarray(mymath.svd_pca.explained_variance_ratio(
        mymath.svd_pca.principal_axes({C_29})[1])).tolist(), computed=True)
with checked("M12d.29d"):
    axes_29, values_29 = (np.asarray(x) for x in mymath.svd_pca.principal_axes(cov_29))
    wbm.check("M12d.29d", bool(axes_29.shape == (5, 5) and np.allclose(axes_29.T @ axes_29, np.eye(5), rtol=0, atol=1e-8)
                               and np.allclose(cov_29 @ axes_29, axes_29 * values_29, rtol=0, atol=1e-8)
                               and np.allclose(axes_29.T, PCA().fit(X_29).components_, rtol=0, atol=1e-8)), computed=True)
with checked("M12d.29e"):
    wbm.check("M12d.29e", str(np.asarray(mymath.svd_pca.principal_axes({C_29}, k=1)[0]).shape), computed=True)
with checked("M12d.29f"):
    wbm.check("M12d.29f", raised(mymath.svd_pca.principal_axes, [[1, 2], [3, 4]]), computed=True)
with checked("M12d.29g"):
    wbm.check("M12d.29g", raised(mymath.svd_pca.principal_axes, [[1, 0], [0, -1]]), computed=True)
with checked("M12d.29h"):
    wbm.check("M12d.29h", raised(mymath.svd_pca.explained_variance_ratio, [0, 0]), computed=True)''',
    solution=LOAD_REF + f'''
from sklearn.decomposition import PCA

principal_axes, explained_variance_ratio = mymath.svd_pca.principal_axes, mymath.svd_pca.explained_variance_ratio
X_29 = np.random.default_rng(29).normal(size=(300, 5)) @ np.diag([3.0, 2.0, 1.5, 1.0, 0.5])
cov_29 = np.cov(X_29, rowvar=False)
axes_c29, values_c29 = principal_axes({C_29})
print("a)", np.round(axes_c29, 6).tolist(), " b)", np.round(values_c29, 6).tolist(),
      " c)", np.round(explained_variance_ratio(values_c29), 6).tolist())
axes_29, values_29 = principal_axes(cov_29)
print("d)", bool(np.allclose(axes_29.T @ axes_29, np.eye(5), rtol=0, atol=1e-8)
                 and np.allclose(cov_29 @ axes_29, axes_29 * values_29, rtol=0, atol=1e-8)
                 and np.allclose(axes_29.T, PCA().fit(X_29).components_, rtol=0, atol=1e-8)))
print("e)", str(principal_axes({C_29}, k=1)[0].shape), " f)", raised(principal_axes, [[1, 2], [3, 4]]),
      " g)", raised(principal_axes, [[1, 0], [0, -1]]), " h)", raised(explained_variance_ratio, [0, 0]))''',
    record=f'''AXES_29 = (np.array([[-3.0, 0.0, 5.0], [0.0, 34 ** 0.5, 0.0], [5.0, 0.0, 3.0]]) / 34 ** 0.5).T
wbm.record("M12d.29a", AXES_29.tolist(), decimals=6,
           mistakes={{"la convention de signe : la coordonnée de plus grande valeur absolue de chaque axe positive":
                         (AXES_29 * np.array([-1.0, 1.0, 1.0])).tolist(),
                     "l'ordre décroissant des variances : eigh range par ordre croissant": AXES_29[:, ::-1].tolist()}})
wbm.record("M12d.29b", [35.0, 6.0, 1.0], decimals=6,
           mistakes={{"l'ordre décroissant : eigh rend les valeurs propres par ordre croissant": [1.0, 6.0, 35.0]}})
wbm.record("M12d.29c", [35 / 42, 6 / 42, 1 / 42], decimals=6,
           mistakes={{"divise par la somme de TOUTES les variances": [1.0, 6 / 35, 1 / 35]}})
wbm.record("M12d.29d", True,
           mistakes={{"compare tes axes à np.linalg.eigh sur une matrice diagonale : l'ordre, les colonnes, le signe": False}})
wbm.record("M12d.29e", "(3, 1)",
           mistakes={{"un axe par COLONNE : la forme est (p, k)": "(1, 3)"}})
wbm.record("M12d.29f", "ValueError",
           {value_error("une matrice non symétrique n'est pas une covariance : la docstring demande une ValueError")})
wbm.record("M12d.29g", "ValueError",
           {value_error("une valeur propre négative : pas une covariance, la docstring demande une ValueError")})
wbm.record("M12d.29h", "ValueError",
           {value_error("des variances de somme nulle : la docstring demande une ValueError")})''',
    after=tests_cells("test_principal_axes_ or test_explained_variance_ratio_"),
    note=r"La deuxième mesure est isolée (variance 6, axe $\mathbf{e}_2$) ; le bloc $\begin{pmatrix} 10 & -15 \\ -15 & 26 "
         r"\end{pmatrix}$ a pour trace 36 et déterminant 35 : valeurs propres 35 et 1, de vecteurs propres $(3, -5)$ et "
         r"$(5, 3)$. La convention retourne $(3, -5)$ en $(-3, 5)$ : sa coordonnée de plus grande valeur absolue est "
         r"$-5$. Parts : $\frac{35}{42} \approx 83{,}3\,\%$, puis $\frac{41}{42} \approx 97{,}6\,\%$ en cumulé.",
)

M30_30 = "[[3, -1, 2], [0, 4, -2], [1, 1, 5], [-2, 3, 0], [4, 0, 1]]"

M12D_30 = Ex(
    "M12d.30", "📦", 1, 15, "`np.linalg.svd`, `np.linalg.cond` et `sklearn.decomposition.PCA` contre tes fonctions : "
    "les signes",
    "utiliser `np.linalg.svd`, `np.linalg.cond` et `sklearn.decomposition.PCA`, lire ce qu'elles rendent, aligner "
    "leurs signes sur la convention, et comparer avec ta librairie.", "fiche §1, §4 et §6 ; Ex M12d.26 à M12d.29",
    tracks="C, E",
    given='''from sklearn.decomposition import PCA

M_30 = np.array(''' + M30_30 + ''', dtype=float)
X_30 = (np.random.default_rng(30).normal(size=(200, 4))
        @ np.array([[2.0, 0.5, 0.0, 0.0], [0.0, 1.0, 0.8, 0.0], [0.0, 0.0, 0.6, 0.3], [0.4, 0.0, 0.0, 0.2]])
        + np.array([10.0, -3.0, 5.0, 1.0]))''',
    body=r"""En pratique, on ne réécrit pas ces fonctions :
- `np.linalg.svd(A, full_matrices=False)` rend `(U, s, Vt)`, les $\mathbf{v}_i$ en **lignes** de `Vt`, avec des signes **arbitraires** (ceux de LAPACK) ; `compute_uv=False` ne rend que `s` ;
- `np.linalg.cond(A)` rend $s_{\max}/s_{\min}$ ;
- `PCA().fit(X)` (scikit-learn) centre, fait la SVD de $\mathbf{X}_c$ (ou diagonalise sa covariance, selon la taille), et range les axes en **lignes** de `components_`, avec la convention de signe de la fiche ; `explained_variance_` donne les variances (en $n - 1$), `transform(X)` les scores.

Avec `M_30` et `X_30` (la cellule fournie), calcule :
- a) les valeurs singulières de `M_30` par `np.linalg.svd` (une liste, 6 décimales) ;
- b) vrai ou faux : après avoir multiplié chaque ligne de `Vt` (et la colonne de `U` qui va avec) par le signe qui rend positive sa coordonnée de plus grande valeur absolue, `U` et `Vt` de NumPy sont égaux à ceux de ta fonction `svd(M_30)`, à $10^{-8}$ près ;
- c) vrai ou faux : ta fonction `condition_number(M_30)` est égale à `np.linalg.cond(M_30)` à $10^{-10}$ près, relativement ;
- d) la forme de `np.cov(X_30)`, **sans** argument `rowvar` (une liste de 2 entiers) ;
- e) vrai ou faux : `PCA().fit(X_30).components_` est égal à la transposée des axes de ta fonction `principal_axes(np.cov(X_30, rowvar=False))`, à $10^{-8}$ près ;
- f) vrai ou faux : `PCA().fit(X_30).explained_variance_` est égal aux variances de ta fonction, à $10^{-8}$ près, relativement ;
- g) l'entier `d` tel que `np.var(scores, axis=0, ddof=d)` redonne `explained_variance_`, pour `scores = PCA().fit(X_30).transform(X_30)`.

Dans ta copie : pourquoi deux SVD justes peuvent-elles différer par des signes, et lesquels exactement (pourquoi faut-il changer **à la fois** $\mathbf{u}_i$ et $\mathbf{v}_i$) ? Que calcule `np.cov(X_30)` sans `rowvar=False`, et pourquoi est-ce un piège ? Pourquoi `explained_variance_` ne dépend-il pas de la moyenne $(10, -3, 5, 1)$ ajoutée aux données ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12d")
answer_M12d_30a = ...  # a) a list of 3 numbers (6 decimals)
answer_M12d_30d = ...  # d) a list of 2 integers
answer_M12d_30g = ...  # g) an integer
answer_M12d_30b = answer_M12d_30c = answer_M12d_30e = answer_M12d_30f = ...
# Each block stands alone: compute inside it what it needs, so that "Run all" goes on when a function is not written.
with wbm.attempt("M12d.30b"):        # your svd is called here: ⏳ while it is not written
    answer_M12d_30b = ...  # b) True or False
with wbm.attempt("M12d.30c"):        # your condition_number
    answer_M12d_30c = ...  # c) True or False
with wbm.attempt("M12d.30e"):        # your principal_axes
    answer_M12d_30e = ...  # e) True or False
with wbm.attempt("M12d.30f"):        # your principal_axes
    answer_M12d_30f = ...  # f) True or False''',
    check='''for letter, answer in zip("abcdefg", [answer_M12d_30a, answer_M12d_30b, answer_M12d_30c, answer_M12d_30d,
                                       answer_M12d_30e, answer_M12d_30f, answer_M12d_30g]):
    wbm.check(f"M12d.30{letter}", answer)''',
    solution='''ref_30 = wbm.load_mymath("ref", alias="mymath_ref").svd_pca
answer_M12d_30a = np.round(np.linalg.svd(M_30, compute_uv=False), 6).tolist()
U_30, s_30, Vt_30 = np.linalg.svd(M_30, full_matrices=False)
signs_30 = np.where(Vt_30[np.arange(len(s_30)), np.argmax(np.abs(Vt_30), axis=1)] < 0, -1.0, 1.0)
U_ref30, s_ref30, Vt_ref30 = ref_30.svd(M_30)
answer_M12d_30b = bool(np.allclose(U_30 * signs_30, U_ref30, rtol=0, atol=1e-8)
                       and np.allclose(Vt_30 * signs_30[:, None], Vt_ref30, rtol=0, atol=1e-8))
answer_M12d_30c = bool(abs(ref_30.condition_number(M_30) - np.linalg.cond(M_30)) <= 1e-10 * np.linalg.cond(M_30))
answer_M12d_30d = list(np.cov(X_30).shape)
pca_30 = PCA().fit(X_30)
axes_30, variances_30 = ref_30.principal_axes(np.cov(X_30, rowvar=False))
answer_M12d_30e = bool(np.allclose(pca_30.components_, axes_30.T, rtol=0, atol=1e-8))
answer_M12d_30f = bool(np.allclose(pca_30.explained_variance_, variances_30, rtol=1e-8, atol=0))
scores_30 = pca_30.transform(X_30)
answer_M12d_30g = next(d for d in (0, 1) if np.allclose(np.var(scores_30, axis=0, ddof=d), pca_30.explained_variance_))
print(answer_M12d_30a, answer_M12d_30b, answer_M12d_30c, answer_M12d_30d, answer_M12d_30e, answer_M12d_30f, answer_M12d_30g)
print("signes de LAPACK sur les lignes de Vt :", signs_30.tolist())''',
    record='''s_30r = np.linalg.svd(np.array(''' + M30_30 + ''', dtype=float), compute_uv=False)
wbm.record("M12d.30a", s_30r.tolist(), decimals=6,
           mistakes={"np.linalg.svd rend les valeurs singulières par ordre décroissant : garde l'ordre rendu": s_30r[::-1].tolist()})
wbm.record("M12d.30b", True,
           mistakes={"change le signe de la LIGNE de Vt et de la COLONNE de U qui va avec, ensemble ; sinon relis ta fonction svd (M12d.26)": False})
wbm.record("M12d.30c", True,
           mistakes={"relis ta fonction condition_number (M12d.27) : ses tests disent ce qui ne va pas": False})
wbm.record("M12d.30d", [200, 200],
           mistakes={"np.cov range par défaut les VARIABLES en lignes : sans rowvar=False, les 200 exemples sont pris pour des variables":
                         [4, 4]})
wbm.record("M12d.30e", True,
           mistakes={"components_ range les axes en LIGNES, ta fonction en colonnes : compare avec la transposée ; sinon relis principal_axes (M12d.29)": False})
wbm.record("M12d.30f", True,
           mistakes={"explained_variance_ utilise n − 1, comme np.cov(..., rowvar=False) : relis principal_axes (M12d.29)": False})
wbm.record("M12d.30g", 1, mistakes={"scikit-learn divise par n − 1 : ddof=1": 0})''',
    note=r"Une SVD est unique au signe près de chaque couple $(\mathbf{u}_i, \mathbf{v}_i)$ : $s_i\mathbf{u}_i\mathbf{v}_i^\top"
         r" = s_i(-\mathbf{u}_i)(-\mathbf{v}_i)^\top$, il faut donc changer les deux à la fois. `np.cov(X)` sans "
         r"`rowvar=False` prend les **lignes** pour des variables : une matrice $200 \times 200$, sans erreur ni "
         r"avertissement. Les variances le long des axes ne dépendent pas de la moyenne : l'ACP centre d'abord.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, two experiments, a figure (M12d.31 to M12d.34)
# ---------------------------------------------------------------------------
M12D_31_GIVEN = '''A_31 = wbm.datasets.load_image("tasse")      # the coffee cup: 400 × 600 grey levels (data/cards/tasse_cafe.md)
NOISE_31 = np.random.default_rng(31).normal(loc=A_31.mean(), scale=A_31.std(), size=A_31.shape)   # pure noise
plt.figure(figsize=(5, 3.4))
plt.imshow(A_31, cmap="gray", vmin=0, vmax=255)
plt.axis("off")
plt.title("La tasse de café (400 × 600, CC0)")
plt.show()'''

M12D_31_EXPERIMENT = '''def rank_for(A, share):
    """The smallest rank k whose approximation keeps at least `share` of the energy of A − mean(A)."""
    s = np.linalg.svd(A - A.mean(), compute_uv=False)
    return int(np.searchsorted(np.cumsum(s ** 2) / np.sum(s ** 2), share) + 1)


s_photo = np.linalg.svd(A_31 - A_31.mean(), compute_uv=False)
s_noise = np.linalg.svd(NOISE_31 - NOISE_31.mean(), compute_uv=False)
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.semilogy(np.arange(1, 401), s_photo, label="la photo, centrée")
ax.semilogy(np.arange(1, 401), s_noise, label="du bruit de même taille, centré")
ax.set_xlabel("rang i")
ax.set_ylabel("valeur singulière s_i")
ax.legend()
plt.show()
s_raw = np.linalg.svd(A_31, compute_uv=False)
print(f"rang pour 90 % de l'énergie : photo {rank_for(A_31, 0.9)}, bruit {rank_for(NOISE_31, 0.9)}")
print(f"part de l'énergie de la photo NON centrée gardée au rang 1 : {s_raw[0] ** 2 / np.sum(s_raw ** 2):.1%}".replace(".", ","))'''

M12D_31 = Ex(
    "M12d.31", "🔮", 1, 10, "Prédire l'allure des valeurs singulières d'une image, et le rang qui suffit",
    "prévoir la décroissance des valeurs singulières d'une photo et d'un bruit, et le rang qui garde 90 % de leur "
    "énergie, puis le vérifier.", "fiche §3", tracks="C, E", hypothesis=True, given=M12D_31_GIVEN,
    body=r"""La cellule fournie charge la photo de la tasse de café (`wbm.datasets.load_image("tasse")`, niveaux de gris de 0 à 255, licence CC0) et fabrique une image `NOISE_31` de **bruit pur**, de même taille, même moyenne et même écart-type (des niveaux tirés au hasard, indépendants). On retire à chaque image son niveau de gris moyen avant la SVD (fiche §3, ⚠️). Pour chaque question, choisis le numéro de la bonne réponse :
- a) l'allure des 400 valeurs singulières de la photo centrée, en échelle logarithmique : (1) quelques grandes valeurs, puis exactement zéro ; (2) une chute rapide, puis une longue traîne qui décroît lentement ; (3) toutes à peu près égales ;
- b) le plus petit rang qui garde au moins 90 % de l'énergie de la photo centrée : (1) de 1 à 4 ; (2) de 5 à 30 ; (3) de 31 à 150 ; (4) plus de 150 ;
- c) la même question pour le bruit : mêmes choix ;
- d) la part de l'énergie de la photo **non centrée** gardée au rang 1 : (1) moins de 30 % ; (2) entre 30 et 70 % ; (3) plus de 70 %.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M12d_31a = ...  # a) 1, 2 or 3, written BEFORE running the experiment below
prediction_M12d_31b = ...  # b) 1, 2, 3 or 4
prediction_M12d_31c = ...  # c) 1, 2, 3 or 4
prediction_M12d_31d = ...  # d) 1, 2 or 3''',
    check='''for letter, prediction in zip("abcd", [prediction_M12d_31a, prediction_M12d_31b, prediction_M12d_31c,
                                      prediction_M12d_31d]):
    wbm.check(f"M12d.31{letter}", prediction)''',
    record='''wbm.record("M12d.31a", 2, prediction=True, choices=[1, 2, 3])
wbm.record("M12d.31b", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M12d.31c", 4, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M12d.31d", 3, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience** (avec `np.linalg.svd`). Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(M12D_31_EXPERIMENT, [f"prediction_M12d_31{letter}" for letter in "abcd"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", M12D_31_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : pourquoi la photo n'a-t-elle aucune valeur singulière nulle, "
               "alors que quelques couches suffisent à la reconnaître ? Pourquoi le bruit demande-t-il presque toutes "
               "ses couches, et quel lien avec le débruitage par troncature (fiche §3, en machine learning) ? Que dit "
               "d) sur le piège de l'image non centrée ?"),
    ],
    note=r"a) Une photo a des zones lisses et des contours qui se répètent d'une ligne à l'autre : quelques couches "
         r"portent l'essentiel, mais la texture fine (le grain du bois) et les arrondis des niveaux de gris donnent une "
         r"longue traîne, jamais nulle. b) 13 couches gardent 90 % de l'énergie de la photo centrée. c) Le bruit n'a "
         r"aucune structure : ses valeurs singulières sont du même ordre (un rapport d'environ 10 entre la première et "
         r"la dernière), et il en faut environ 240 sur 400. d) Sans centrer, la première couche rend surtout le niveau "
         r"moyen : 82 % de l'énergie, sans rien dire de la qualité.",
)

M12D_32 = Ex(
    "M12d.32", "🔬", 2, 20, "Compresser une image du domaine public : l'erreur en fonction du rang",
    "mesurer l'énergie gardée, l'erreur et le coût de stockage d'une approximation de rang $k$ d'une photo, et "
    "regarder les reconstructions.", "fiche §3 ; Ex M12d.5 et M12d.31", tracks="C",
    given='''A_32 = wbm.datasets.load_image("tasse")      # 400 × 600 grey levels, CC0''',
    body=r"""Avec la photo `A_32` (la même qu'en M12d.31), écris :
- `reconstruct(A, k)` : l'image reconstruite au rang $k$ : on retire le niveau moyen $\bar{a}$, on prend l'approximation de rang $k$ de $\mathbf{A} - \bar{a}$ (`np.linalg.svd`, ou ta fonction `low_rank_approximation`), et l'on rajoute $\bar{a}$ ;
- `energy_kept(A)` : le tableau des parts d'énergie gardées aux rangs $1, 2, \ldots, \min(m, n)$, pour l'image **centrée** : $\sum_{i \le k} s_i^2 / \sum_i s_i^2$ (`np.cumsum`).

Puis calcule :
- a) le niveau de gris moyen $\bar{a}$ (2 décimales) ;
- b) la part d'énergie gardée au rang 10 (4 décimales) ;
- c) le plus petit rang qui garde au moins 90 % de l'énergie ;
- d) le plus petit rang qui garde au moins 99 % ;
- e) l'erreur relative $\lVert \mathbf{A} - \hat{\mathbf{A}}_{50} \rVert_F / \lVert \mathbf{A} - \bar{a} \rVert_F$, calculée **sur les matrices** avec `reconstruct` (4 décimales) ;
- f) la part des nombres stockés au rang de c), $k(m + n + 1)/(mn)$ (4 décimales) ;
- g) la part d'énergie gardée au rang 1 par l'image **non centrée** (sa SVD à elle, 4 décimales).

Une cellule affiche ensuite les reconstructions aux rangs 5, 20 et 50.

Dans ta copie : vérifie que e) est $\sqrt{1 - (\text{part gardée au rang } 50)}$, et dis pourquoi (Eckart-Young). À partir de quel rang la tasse est-elle reconnaissable ? Le grain du bois ? Combien de nombres faudrait-il pour garder 99 %, et est-ce encore une compression ? Pourquoi un JPEG fait-il beaucoup mieux (il travaille par petits blocs, et compte des bits) ?""",
    todo='''def reconstruct(A, k):
    """The rank-k approximation of A − mean(A), plus mean(A)."""
    raise NotImplementedError("np.linalg.svd(A - A.mean(), full_matrices=False), les k premières couches, puis + A.mean()")


def energy_kept(A):
    """The shares of the energy of A − mean(A) kept at ranks 1, 2, ..., min(m, n)."""
    raise NotImplementedError("np.linalg.svd(..., compute_uv=False), puis np.cumsum(s ** 2) / np.sum(s ** 2)")


answer_M12d_32a = ...  # a) a number (2 decimals)
answer_M12d_32b = answer_M12d_32c = answer_M12d_32d = answer_M12d_32e = answer_M12d_32f = answer_M12d_32g = ...
with wbm.attempt("M12d.32b"):        # your energy_kept is called here: ⏳ while it is not written
    answer_M12d_32b = ...  # b) a number (4 decimals)
    answer_M12d_32c = ...  # c) an integer
    answer_M12d_32d = ...  # d) an integer
with wbm.attempt("M12d.32e"):        # your reconstruct
    answer_M12d_32e = ...  # e) a number (4 decimals)
answer_M12d_32f = ...  # f) a number (4 decimals)
answer_M12d_32g = ...  # g) a number (4 decimals)''',
    check='''for letter, answer in zip("abcdefg", [answer_M12d_32a, answer_M12d_32b, answer_M12d_32c, answer_M12d_32d,
                                       answer_M12d_32e, answer_M12d_32f, answer_M12d_32g]):
    wbm.check(f"M12d.32{letter}", answer)

with checked("M12d.32 figure"):
    fig, axes = plt.subplots(1, 4, figsize=(15, 3))
    try:
        for ax, k in zip(axes, (None, 5, 20, 50)):
            ax.imshow(A_32 if k is None else np.clip(reconstruct(A_32, k), 0, 255), cmap="gray", vmin=0, vmax=255)
            ax.set_title("l'original" if k is None else f"rang {k}")
            ax.axis("off")
    except BaseException:
        plt.close(fig)
        raise
    plt.show()''',
    solution='''def reconstruct(A, k):
    """The rank-k approximation of A − mean(A), plus mean(A)."""
    mean = A.mean()
    U, s, Vt = np.linalg.svd(A - mean, full_matrices=False)
    return (U[:, :k] * s[:k]) @ Vt[:k] + mean


def energy_kept(A):
    """The shares of the energy of A − mean(A) kept at ranks 1, 2, ..., min(m, n)."""
    s = np.linalg.svd(A - A.mean(), compute_uv=False)
    return np.cumsum(s ** 2) / np.sum(s ** 2)


shares_32 = energy_kept(A_32)
m_32, n_32 = A_32.shape
answer_M12d_32a = round(float(A_32.mean()), 2)
answer_M12d_32b = round(float(shares_32[9]), 4)
answer_M12d_32c = int(np.argmax(shares_32 >= 0.90) + 1)
answer_M12d_32d = int(np.argmax(shares_32 >= 0.99) + 1)
answer_M12d_32e = round(float(np.linalg.norm(A_32 - reconstruct(A_32, 50)) / np.linalg.norm(A_32 - A_32.mean())), 4)
answer_M12d_32f = round(answer_M12d_32c * (m_32 + n_32 + 1) / (m_32 * n_32), 4)
s_raw32 = np.linalg.svd(A_32, compute_uv=False)
answer_M12d_32g = round(float(s_raw32[0] ** 2 / np.sum(s_raw32 ** 2)), 4)
print(answer_M12d_32a, answer_M12d_32b, answer_M12d_32c, answer_M12d_32d, answer_M12d_32e, answer_M12d_32f, answer_M12d_32g)
print("√(1 − part au rang 50) :", round(float(np.sqrt(1 - shares_32[49])), 4))
fig, axes = plt.subplots(1, 4, figsize=(15, 3))
for ax, k in zip(axes, (None, 5, 20, 50)):
    ax.imshow(A_32 if k is None else np.clip(reconstruct(A_32, k), 0, 255), cmap="gray", vmin=0, vmax=255)
    ax.set_title("l'original" if k is None else f"rang {k}")
    ax.axis("off")
plt.show()''',
    record='''A_32r = wbm.datasets.load_image("tasse")
s_32r = np.linalg.svd(A_32r - A_32r.mean(), compute_uv=False)
shares_32r = np.cumsum(s_32r ** 2) / np.sum(s_32r ** 2)
raw_32r = np.linalg.svd(A_32r, compute_uv=False)
k90_32r, k99_32r = int(np.argmax(shares_32r >= 0.90) + 1), int(np.argmax(shares_32r >= 0.99) + 1)
wbm.record("M12d.32a", float(A_32r.mean()), decimals=2)
wbm.record("M12d.32b", float(shares_32r[9]), decimals=4,
           mistakes={"l'énergie se compte avec les CARRÉS des valeurs singulières": float(np.sum(s_32r[:10]) / np.sum(s_32r)),
                     "le rang 10 est le dixième élément, d'indice 9": float(shares_32r[10])})
wbm.record("M12d.32c", k90_32r,
           mistakes={"le plus petit rang k, compté à partir de 1 : l'indice NumPy plus 1": k90_32r - 1})
wbm.record("M12d.32d", k99_32r,
           mistakes={"le plus petit rang k, compté à partir de 1 : l'indice NumPy plus 1": k99_32r - 1})
wbm.record("M12d.32e", float(np.sqrt(1 - shares_32r[49])), decimals=4,
           mistakes={"l'erreur relative : divise par la norme de l'image CENTRÉE": float(np.sqrt(np.sum(s_32r[50:] ** 2)) / np.linalg.norm(A_32r)),
                     "la norme, pas son carré : prends la racine": float(1 - shares_32r[49])})
wbm.record("M12d.32f", k90_32r * 1001 / 240000, decimals=4)
wbm.record("M12d.32g", float(raw_32r[0] ** 2 / np.sum(raw_32r ** 2)), decimals=4,
           mistakes={"l'image NON centrée : la SVD de A elle-même, sans retirer la moyenne": float(shares_32r[0])})''',
    note=r"Eckart-Young : $\lVert \mathbf{A}_c - (\mathbf{A}_c)_k \rVert_F^2 = \sum_{i > k} s_i^2$, donc l'erreur relative "
         r"est $\sqrt{1 - \text{part gardée}}$ ; rajouter la moyenne ne change pas l'écart. La tasse se reconnaît dès le "
         r"rang 5, le grain du bois demande plusieurs dizaines de couches. 99 % demandent 125 couches, soit 52 % des "
         r"nombres : la SVD globale n'est plus une compression. Un JPEG découpe l'image en blocs de $8 \times 8$, dans "
         r"une base fixe (cosinus), et quantifie : il compte des bits, pas des nombres (🏆 M12d.37 pour une idée voisine).",
)

M12D_33_GIVEN = '''KAPPAS_33 = [1e2, 1e4, 1e6, 1e8]       # make_conditioned(kappa) (the tools): singular values 1, ..., 1/kappa'''

M12D_33_SHOW = '''table_33 = error_table()
print("    κ      erreur relative sur s_min : ta svd    np.linalg.svd")
for kappa, (mine, lapack) in zip(KAPPAS_33, table_33):
    print(f"{kappa:8.0e}   {mine:24.1e}   {lapack:14.1e}")'''

M12D_33 = Ex(
    "M12d.33", "🔬", 2, 20, "La SVD par AᵀA contre `np.linalg.svd` : ce qu'on perd quand κ est grand",
    "mesurer la précision de la SVD par $\\mathbf{A}^\\top\\mathbf{A}$ et de celle de LAPACK quand le conditionnement "
    "grandit, et voir ce qu'une bonne reconstruction cache.", "fiche §1 et §4 ; Ex M12d.26", tracks="C",
    given=M12D_33_GIVEN,
    body=r"""La fonction `make_conditioned(kappa)` (cellule des outils) fabrique une matrice $6 \times 4$ dont les valeurs singulières, **connues**, vont de 1 à $1/\kappa$ (géométriquement) : son conditionnement est $\kappa$. Écris :
- `error_table()` : pour chaque $\kappa$ de `KAPPAS_33`, le couple des erreurs relatives sur la plus petite valeur singulière, $\lvert \hat{s}_{\min} - 1/\kappa \rvert \cdot \kappa$, obtenues par ta fonction `mymath.svd_pca.svd(A, tol=1e-12)` (pour qu'elle garde les quatre valeurs) et par `np.linalg.svd(A, compute_uv=False)`.

La cellule suivante affiche le tableau. Lis-le, puis réponds :
- a) le plus petit $\kappa$ de `KAPPAS_33` pour lequel l'erreur relative de **ta** fonction dépasse $10^{-6}$ ;
- b) vrai ou faux : l'erreur relative de `np.linalg.svd` reste sous $10^{-6}$ pour les quatre $\kappa$ ;
- c) vrai ou faux : pour $\kappa = 10^6$, ta fonction redonne quand même la matrice : $\lVert \mathbf{U}\operatorname{diag}(s)\mathbf{V}^\top - \mathbf{A} \rVert_F \le 10^{-12}\lVert \mathbf{A} \rVert_F$ (avec `tol=1e-12`) ;
- d) vrai ou faux : pour $\kappa = 10^6$, les colonnes du $\mathbf{U}$ de ta fonction sont orthonormées à $10^{-8}$ près (le plus grand écart de $\mathbf{U}^\top\mathbf{U}$ à $\mathbf{I}$) ;
- e) le nombre de valeurs singulières gardées par ta fonction **avec son seuil par défaut** pour $\kappa = 10^8$ ;
- f) `np.linalg.matrix_rank(make_conditioned(1e8))`.

Si ta fonction `svd` n'est pas encore écrite, la cellule utilise la référence et le dit.

Dans ta copie : de combien de puissances de 10 ton erreur grandit-elle quand $\kappa$ est multiplié par 100, et pourquoi (fiche §4, $\kappa^2$) ? Pourquoi c) reste-t-il vrai alors que $s_{\min}$ est faux : quelle part de $\mathbf{A}$ porte la couche fausse ? Que disent e) et f) du « rang » d'une matrice en flottants ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12d")
try:                                             # your svd if it runs, else the reference
    mymath.svd_pca.svd(make_conditioned(1e2))
    svd_33 = mymath.svd_pca.svd
    print("avec ta fonction svd")
except Exception:  # noqa: BLE001 - not written yet (NotImplementedError), missing file, or a bug
    svd_33 = wbm.load_mymath("ref", alias="mymath_ref").svd_pca.svd
    print("ℹ️ ta fonction svd n'est pas encore écrite (ou lève une erreur) : l'expérience utilise la référence")


def error_table():
    """For each kappa of KAPPAS_33: (relative error on s_min of svd_33(A, tol=1e-12), the same for np.linalg.svd)."""
    raise NotImplementedError("une liste de 4 couples : |s_min − 1/κ| × κ pour svd_33 et pour np.linalg.svd")''',
    check=f'''with checked("M12d.33 tableau"):
{chr(10).join("    " + line for line in M12D_33_SHOW.splitlines())}''' + '''

answer_M12d_33a = ...  # a) a number of KAPPAS_33
answer_M12d_33b = ...  # b) True or False
answer_M12d_33c = ...  # c) True or False, computed with svd_33
answer_M12d_33d = ...  # d) True or False, computed with svd_33
answer_M12d_33e = ...  # e) an integer
answer_M12d_33f = ...  # f) an integer
for letter, answer in zip("abcdef", [answer_M12d_33a, answer_M12d_33b, answer_M12d_33c, answer_M12d_33d,
                                     answer_M12d_33e, answer_M12d_33f]):
    wbm.check(f"M12d.33{letter}", answer)''',
    solution=LOAD_REF + '''
svd_33 = mymath.svd_pca.svd


def error_table():
    """For each kappa of KAPPAS_33: (relative error on s_min of svd_33(A, tol=1e-12), the same for np.linalg.svd)."""
    rows = []
    for kappa in KAPPAS_33:
        A = make_conditioned(kappa)
        mine = svd_33(A, tol=1e-12)[1][-1]
        lapack = np.linalg.svd(A, compute_uv=False)[-1]
        rows.append((abs(mine - 1 / kappa) * kappa, abs(lapack - 1 / kappa) * kappa))
    return rows


''' + M12D_33_SHOW + '''
A_33 = make_conditioned(1e6)
U_33, s_33, Vt_33 = svd_33(A_33, tol=1e-12)
answer_M12d_33a = next(kappa for kappa, (mine, _) in zip(KAPPAS_33, table_33) if mine > 1e-6)
answer_M12d_33b = all(lapack < 1e-6 for _, lapack in table_33)
answer_M12d_33c = bool(np.linalg.norm(U_33 @ np.diag(s_33) @ Vt_33 - A_33) <= 1e-12 * np.linalg.norm(A_33))
answer_M12d_33d = bool(np.max(np.abs(U_33.T @ U_33 - np.eye(4))) <= 1e-8)
answer_M12d_33e = len(svd_33(make_conditioned(1e8))[1])
answer_M12d_33f = int(np.linalg.matrix_rank(make_conditioned(1e8)))
print(answer_M12d_33a, answer_M12d_33b, answer_M12d_33c, answer_M12d_33d, answer_M12d_33e, answer_M12d_33f)''',
    record='''wbm.record("M12d.33a", 1e6, decimals=0,
           mistakes={"le PREMIER κ dont l'erreur DÉPASSE 1e−6, pas le dernier en dessous": 1e4,
                     "lis la colonne de TA fonction : l'erreur est relative, |ŝ − 1/κ| × κ": 1e8})
wbm.record("M12d.33b", True, mistakes={"lis la dernière colonne : LAPACK ne forme jamais AᵀA": False})
wbm.record("M12d.33c", True,
           mistakes={"U diag(s) Vᵀ avec tol=1e−12 : la couche fausse ne pèse que s_min, un millionième de A": False})
wbm.record("M12d.33d", False,
           mistakes={"U = A V / s divise par un s_min faux : UᵀU s'écarte de I d'environ 1e−16 × κ²": True})
wbm.record("M12d.33e", 3,
           mistakes={"le seuil par défaut, tol = 1e−6, retire la valeur 1e−8 (et garde 4,6e−6)": 4})
wbm.record("M12d.33f", 4,
           mistakes={"matrix_rank compare à un seuil d'environ 1e−15 × s_max : il garde 1e−8": 3})''',
    note=r"L'erreur sur une valeur propre de $\mathbf{A}^\top\mathbf{A}$ est d'environ $10^{-16} \times s_{\max}^2$ : sur "
         r"$s_{\min}^2 = \kappa^{-2}$, une erreur relative d'environ $10^{-16}\kappa^2$, qui grandit de 4 puissances de 10 "
         r"quand $\kappa$ est multiplié par 100 (pour $\kappa = 10^8$, $\kappa^2 \times 10^{-16} \approx 1$ : il ne reste "
         r"rien). LAPACK travaille sur $\mathbf{A}$ et perd environ $10^{-16}\kappa$. La reconstruction reste bonne parce "
         r"que la couche fausse pèse $s_{\min}\lVert \mathbf{u}\mathbf{v}^\top \rVert = 10^{-6}$ de la matrice : une SVD se "
         r"juge aussi sur l'orthogonalité de $\mathbf{U}$. Le rang numérique dépend du seuil : 3 pour `svd`, 4 pour "
         r"`matrix_rank`.",
)

A_34 = "[[1.5, 1.0], [-0.5, 2.0]]"

M12D_34_FIGURE = '''fig, axes = plt.subplots(1, 4, figsize=(16, 4.2))
try:
    draw_svd_steps(axes, np.array(''' + A_34 + '''))
except BaseException:
    plt.close(fig)
    raise
plt.show()'''

M12D_34 = Ex(
    "M12d.34", "🎨", 1, 20, "La SVD en images : Vᵀ, Σ puis U appliqués au cercle unité, étape par étape",
    "dessiner les trois étapes de la SVD d'une matrice $2 \\times 2$ sur le cercle unité et ses vecteurs "
    "singuliers.", "fiche §2 ; Ex M12d.3", tracks="C, E",
    body=r"""Écris `draw_svd_steps(axes, A)` : avec `U, s, Vt = np.linalg.svd(A)` (ou ta fonction `svd`) et 200 points $\mathbf{x}$ du cercle unité, dessine dans les quatre axes reçus (sans en ouvrir d'autres) :
1. le cercle, et les vecteurs $\mathbf{v}_1$ et $\mathbf{v}_2$ (deux flèches) ;
2. l'image du cercle par $\mathbf{V}^\top$ (encore un cercle), et les images de $\mathbf{v}_1$ et $\mathbf{v}_2$ : $\mathbf{e}_1$ et $\mathbf{e}_2$ ;
3. l'image par $\mathbf{S}\mathbf{V}^\top$ : une ellipse alignée sur les axes, de demi-axes $s_1\mathbf{e}_1$ et $s_2\mathbf{e}_2$ ;
4. l'image par $\mathbf{U}\mathbf{S}\mathbf{V}^\top = \mathbf{A}$ : l'ellipse finale, et ses demi-axes $s_1\mathbf{u}_1$ et $s_2\mathbf{u}_2$.

Colore les points du cercle selon leur angle (`ax.scatter(..., c=angles, cmap="hsv", s=6)`) pour suivre chacun d'une étape à l'autre, mets le même cadre aux quatre axes, `ax.set_aspect("equal")` et un titre par axe. La cellule de la figure s'en sert pour $\mathbf{A}$ = `""" + A_34 + r"""`.

Dans ta copie : la deuxième étape est-elle une rotation ou une symétrie ($\det\mathbf{V}$) ? Les couleurs tournent-elles dans le même sens dans le premier et le dernier dessin, et quel lien avec le signe de $\det\mathbf{A}$ ? Vérifie que l'aire de l'ellipse finale vaut $\pi\lvert\det\mathbf{A}\rvert$.""",
    todo='''def draw_svd_steps(axes, A):
    """In the four axes: the unit circle, then its images by Vᵀ, by S Vᵀ and by U S Vᵀ = A, with the singular vectors."""
    raise NotImplementedError("np.linalg.svd(A), 200 points du cercle, puis quatre dessins")''',
    check='''with checked("M12d.34 figure"):
''' + "\n".join("    " + line for line in M12D_34_FIGURE.splitlines()),
    solution='''def draw_svd_steps(axes, A):
    """In the four axes: the unit circle, then its images by Vᵀ, by S Vᵀ and by U S Vᵀ = A, with the singular vectors."""
    U, s, Vt = np.linalg.svd(A)
    angles = np.linspace(0, 2 * np.pi, 200, endpoint=False)
    circle = np.vstack([np.cos(angles), np.sin(angles)])
    steps = [("le cercle et v₁, v₂", circle, Vt.T),
             ("après Vᵀ : e₁, e₂", Vt @ circle, np.eye(2)),
             ("après S : s₁e₁, s₂e₂", np.diag(s) @ Vt @ circle, np.diag(s)),
             ("après U : A x, s₁u₁, s₂u₂", A @ circle, U * s)]
    limit = 1.15 * max(1.0, s[0])
    for ax, (title, points, arrows) in zip(axes, steps):
        ax.scatter(points[0], points[1], c=angles, cmap="hsv", s=6)
        for column, color in zip(arrows.T, ("C0", "C3")):
            ax.annotate("", xy=column, xytext=(0, 0), arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2})
        ax.axhline(0, color="0.8", lw=0.6)
        ax.axvline(0, color="0.8", lw=0.6)
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect("equal")
        ax.set_title(title)


''' + M12D_34_FIGURE + '''
U_34, s_34, Vt_34 = np.linalg.svd(np.array(''' + A_34 + '''))
print("s :", np.round(s_34, 4).tolist(), " det V :", round(float(np.linalg.det(Vt_34)), 4),
      " det A :", round(float(np.linalg.det(np.array(''' + A_34 + '''))), 4), " π s₁ s₂ / π :", round(float(s_34[0] * s_34[1]), 4))''',
    note=r"$\det\mathbf{A} = 3 + 0{,}5 = 3{,}5 > 0$ : l'orientation est conservée, les couleurs tournent dans le même "
         r"sens au début et à la fin ; si $\det\mathbf{V} = -1$ (cela dépend des signes rendus par LAPACK), la deuxième "
         r"étape est une symétrie, et $\det\mathbf{U} = -1$ aussi. L'aire de l'ellipse est $\pi s_1s_2 = 3{,}5\,\pi$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M12d.35 to M12d.37)
# ---------------------------------------------------------------------------
M12D_35_GIVEN = '''X = (np.random.default_rng(35).normal(size=(40, 3))
     @ np.array([[3.0, 1.0, 0.0], [0.0, 1.5, 0.5], [0.0, 0.0, 0.7]]) + np.array([20.0, -8.0, 4.0]))   # 40 examples'''

M12D_35_MISTAKES = bug_letters_mistakes(
    "AEG", "BCDF",
    {"A": "regarde ce que mesure chaque formule : autour de quel point ?",
     "E": "regarde comment eigh range ses vecteurs propres, et ce que sélectionne chaque indexation",
     "G": "regarde les conventions par défaut des fonctions de NumPy"},
    name_correct=False)

M12D_35 = Ex(
    "M12d.35", "🐛", 1, 15, "Chasse à l'erreur : une ACP sans centrer, n et n − 1 mélangés, des axes lus en lignes au "
    "lieu de colonnes",
    "repérer dans une ACP écrite à la main les trois erreurs classiques, puis calculer les bonnes valeurs.",
    "fiche §5 et §6", tracks="C", given=M12D_35_GIVEN,
    body=r"""Un collègue a écrit cette ACP des données `X` (la cellule fournie) ; sept lignes portent une lettre et un commentaire qui dit ce qu'elles doivent calculer. Trois lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter son code**, trouve-les.

```python
n = len(X)
mu = X.mean(axis=0)
C = X.T @ X / (n - 1)                            # (A) the covariance matrix of the data
values, vectors = np.linalg.eigh(C)              # (B) the eigenvalues, in increasing order, and the eigenvectors
order = np.argsort(values)[::-1]                 # (C) the indices, from the largest eigenvalue
variances = values[order]                        # (D) the variances along the axes, in decreasing order
axes = vectors[order]                            # (E) the principal axes, in columns, in the same order
scores = (X - mu) @ axes[:, :2]                  # (F) the scores on the first two axes
check = scores.var(axis=0)                       # (G) the variances of the scores, equal to variances[:2]
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) les bonnes variances le long des trois axes (une liste, 4 décimales) ;
- c) le bon premier axe principal, avec la convention de signe (une liste, 4 décimales) ;
- d) une fois les deux autres lignes corrigées, le rapport entre ce que calcule la ligne (G) et `variances[:2]` (le même pour les deux, 4 décimales).

Pour b) et c), écris le code corrigé dans la cellule (c'est permis : seule la recherche des lignes fausses se fait sans exécuter).

Dans ta copie : pour chaque ligne fausse, quelle erreur a été faite, et comment la corriger ? Laquelle donne le résultat le plus trompeur (regarde la première variance qu'elle produit), et laquelle passerait inaperçue sans la ligne (G) ? Quel contrôle simple (fiche §6, ⚠️) aurait détecté chacune ?""",
    todo='''answer_M12d_35a = ...  # a) letters, as text
answer_M12d_35b = ...  # b) a list of 3 numbers (4 decimals)
answer_M12d_35c = ...  # c) a list of 3 numbers (4 decimals)
answer_M12d_35d = ...  # d) a number (4 decimals)''',
    check='''for letter, answer in zip("abcd", [answer_M12d_35a, answer_M12d_35b, answer_M12d_35c, answer_M12d_35d]):
    wbm.check(f"M12d.35{letter}", answer)''',
    solution='''answer_M12d_35a = "AEG"
n = len(X)
mu = X.mean(axis=0)
C = (X - mu).T @ (X - mu) / (n - 1)              # (A) centered
values, vectors = np.linalg.eigh(C)
order = np.argsort(values)[::-1]
variances = values[order]
axes = vectors[:, order]                         # (E) the columns
axes = axes * np.where(axes[np.argmax(np.abs(axes), axis=0), np.arange(3)] < 0, -1.0, 1.0)
scores = (X - mu) @ axes[:, :2]
check = scores.var(axis=0, ddof=1)               # (G) n − 1, as the covariance
answer_M12d_35b = np.round(variances, 4).tolist()
answer_M12d_35c = np.round(axes[:, 0], 4).tolist()
answer_M12d_35d = round(float(scores.var(axis=0)[0] / variances[0]), 4)
print(answer_M12d_35a, answer_M12d_35b, answer_M12d_35c, answer_M12d_35d, " check:", np.round(check, 4).tolist())
C_wrong = X.T @ X / (n - 1)
print("ce que donne la ligne (A) fausse : première variance", round(float(np.linalg.eigvalsh(C_wrong)[-1]), 2))''',
    record=f'''wbm.record("M12d.35a", "AEG",
           mistakes={M12D_35_MISTAKES})
X_35r = (np.random.default_rng(35).normal(size=(40, 3))
         @ np.array([[3.0, 1.0, 0.0], [0.0, 1.5, 0.5], [0.0, 0.0, 0.7]]) + np.array([20.0, -8.0, 4.0]))
C_35r = np.cov(X_35r, rowvar=False)
values_35r, vectors_35r = np.linalg.eigh(C_35r)
axis_35r = vectors_35r[:, -1] * (1.0 if vectors_35r[np.argmax(np.abs(vectors_35r[:, -1])), -1] > 0 else -1.0)
wbm.record("M12d.35b", values_35r[::-1].tolist(), decimals=4,
           mistakes={{"la covariance des données CENTRÉES : corrige (A)": np.linalg.eigvalsh(X_35r.T @ X_35r / 39)[::-1].tolist(),
                     "la covariance divise par n − 1, comme np.cov": (values_35r[::-1] * 39 / 40).tolist()}})
wbm.record("M12d.35c", axis_35r.tolist(), decimals=4,
           mistakes={{"le premier axe est une COLONNE de vectors, la dernière (eigh range par ordre croissant)":
                         (vectors_35r[-1] * np.sign(vectors_35r[-1][np.argmax(np.abs(vectors_35r[-1]))])).tolist(),
                     "la convention de signe : la coordonnée de plus grande valeur absolue positive": (-axis_35r).tolist()}})
wbm.record("M12d.35d", 39 / 40, decimals=4,
           mistakes={{"np.var divise par n, la covariance par n − 1 : le rapport est (n − 1)/n, avec n = 40": 40 / 39,
                     "le commentaire de (G) se trompe : np.var divise par n par défaut, la covariance par n − 1": 1.0}})''',
    note=r"(A) $\mathbf{X}^\top\mathbf{X}/(n-1)$ mesure la dispersion autour de l'**origine** : sa plus grande valeur "
         r"propre (environ 506) est dominée par la moyenne $(20, -8, 4)$, et le « premier axe » pointe vers elle. "
         r"(E) `vectors[order]` permute les **lignes** : il faut `vectors[:, order]`. (G) `np.var` divise par $n$ par "
         r"défaut ; avec `ddof=1`, on retrouve exactement les variances : sans (G), cette incohérence passerait inaperçue. "
         r"Contrôles : $\mathbf{C}\mathbf{u} = \lambda\mathbf{u}$ (attrape (E)), des scores de moyenne nulle et de variances "
         r"$\lambda_j$ (attrapent (A) et (G)).",
)

M12D_36_GIVEN = '''X_36 = (np.random.default_rng(36).normal(size=(30, 4))
        @ np.array([[2.0, 0.3, 0.0, 0.1], [0.0, 1.2, 0.4, 0.0], [0.0, 0.0, 0.7, 0.2], [0.0, 0.0, 0.0, 0.3]])
        + np.array([5.0, -2.0, 1.0, 7.0]))


def pca_reconstruct(X, k):
    """The reconstruction of the rows of X by a PCA with k components (eigenvectors of the covariance)."""
    mu = X.mean(axis=0)
    _, W = np.linalg.eigh(np.cov(X, rowvar=False))
    W = W[:, ::-1][:, :k]                        # the k axes of largest variance, in columns
    return mu + (X - mu) @ W @ W.T'''

M12D_36_CHECK = '''with checked("M12d.36 vérifications"):
    def _no_mean(X, k):                          # forgets to add the mean back
        mu = X.mean(axis=0)
        _, W = np.linalg.eigh(np.cov(X, rowvar=False))
        W = W[:, ::-1][:, :k]
        return (X - mu) @ W @ W.T

    def _increasing(X, k):                       # the columns of eigh in its (increasing) order
        mu = X.mean(axis=0)
        _, W = np.linalg.eigh(np.cov(X, rowvar=False))
        W = W[:, :k]
        return mu + (X - mu) @ W @ W.T

    def _not_centered(X, k):                     # the eigenvectors of XᵀX / (n − 1), without centering
        _, W = np.linalg.eigh(X.T @ X / (len(X) - 1))
        W = W[:, ::-1][:, :k]
        return X @ W @ W.T

    results_36 = []
    for name, function, should_pass in (("la bonne ACP, pca_reconstruct", pca_reconstruct, True),
                                        ("une ACP qui oublie de rajouter la moyenne", _no_mean, False),
                                        ("une ACP qui garde l'ordre CROISSANT de eigh", _increasing, False),
                                        ("une ACP sans centrer", _not_centered, False)):
        try:
            check_reconstruction(function, X_36.copy())
            passed = True
        except AssertionError:
            passed = False
        results_36.append(passed == should_pass)
        verdict = ("✅" if passed == should_pass else "❌") + (" ton test accepte" if passed else " ton test refuse")
        print(f"{verdict} {name}")
    if all(results_36):
        print("✅ Ex M12d.36 : ton test accepte la bonne ACP et attrape les trois erreurs.")
    else:
        print("❌ Ex M12d.36 : ton test doit accepter la bonne ACP et refuser (AssertionError) les trois autres : "
              "relis les trois propriétés de l'énoncé.")'''

M12D_36 = Ex(
    "M12d.36", "🛠️", 1, 15, "Un test : la reconstruction de rang plein redonne X, et l'erreur décroît avec k",
    "écrire un test de propriétés pour une ACP, et vérifier qu'il attrape des erreurs plausibles.",
    "fiche §3 et §7 ; Ex M12d.18 ; M12b.32 (un test de propriétés)", tracks="C", given=M12D_36_GIVEN,
    body=r"""Un test de **propriétés** ne compare pas à des valeurs connues d'avance : il vérifie ce que tout résultat juste doit satisfaire. Écris `check_reconstruction(reconstruct, X)`, qui lève une `AssertionError` (avec `assert` ou `np.testing.assert_allclose`) si la fonction `reconstruct(X, k)`, censée rendre la reconstruction des lignes de `X` par une ACP à `k` composantes, ne vérifie pas les trois propriétés suivantes, avec $p$ le nombre de colonnes de `X`, et $e(k) = \frac{1}{n}\sum_i \lVert \mathbf{x}_i - \hat{\mathbf{x}}_i \rVert^2$ l'erreur de reconstruction moyenne :
1. **le rang plein redonne $\mathbf{X}$** : `reconstruct(X, p)` est égal à `X` à $10^{-10}$ près ;
2. **l'erreur décroît avec $k$** : $e(0) \ge e(1) \ge \cdots \ge e(p)$ (à $10^{-12}$ près) ;
3. **l'erreur est celle de la fiche** : $e(k) = \frac{n - 1}{n}\sum_{j > k}\lambda_j$ pour chaque $k$, avec $\lambda_j$ les valeurs propres de `np.cov(X, rowvar=False)` (`np.linalg.eigvalsh`, à remettre dans l'ordre décroissant), à $10^{-8}$ près relativement à la variance totale.

La cellule de vérification essaie ton test sur la bonne ACP `pca_reconstruct` (fournie) et sur trois ACP fausses : il doit accepter la première et refuser les trois autres.

Dans ta copie : laquelle des trois propriétés attrape chacune des trois ACP fausses ? La propriété 3 seule suffirait-elle, et pourquoi garder quand même les deux autres ? Quelle propriété ajouterais-tu pour tester des scores (moyenne nulle, variances $\lambda_j$, covariances nulles) ?""",
    todo='''def check_reconstruction(reconstruct, X):
    """Raise AssertionError unless reconstruct(X, k) behaves as a PCA reconstruction: full rank gives X back, the mean
    error e(k) does not increase with k, and e(k) = (n − 1)/n × (sum of the forgotten eigenvalues of np.cov)."""
    raise NotImplementedError("trois propriétés, avec assert ou np.testing.assert_allclose")''',
    check=M12D_36_CHECK,
    solution='''def check_reconstruction(reconstruct, X):
    """Raise AssertionError unless reconstruct(X, k) behaves as a PCA reconstruction: full rank gives X back, the mean
    error e(k) does not increase with k, and e(k) = (n − 1)/n × (sum of the forgotten eigenvalues of np.cov)."""
    X = np.asarray(X, dtype=float)
    n, p = X.shape
    np.testing.assert_allclose(reconstruct(X, p), X, rtol=0, atol=1e-10)
    errors = [float(np.mean(np.sum((X - reconstruct(X, k)) ** 2, axis=1))) for k in range(p + 1)]
    assert all(later <= earlier + 1e-12 for earlier, later in zip(errors, errors[1:])), errors
    variances = np.linalg.eigvalsh(np.cov(X, rowvar=False))[::-1]
    expected = [(n - 1) / n * float(np.sum(variances[k:])) for k in range(p + 1)]
    np.testing.assert_allclose(errors, expected, rtol=0, atol=1e-8 * float(np.sum(variances)))


''' + M12D_36_CHECK,
    note=r"L'ACP sans moyenne échoue dès la propriété 1 ; celle qui garde l'ordre croissant de `eigh`, et celle qui "
         r"ne centre pas, passent les propriétés 1 et 2 (des sous-espaces emboîtés donnent des erreurs décroissantes) "
         r"mais échouent à la propriété 3, la seule qui dise **quel** sous-espace est choisi : elle attrape donc, seule, "
         r"les trois erreurs. Les deux autres ne supposent aucun théorème, et leur échec dit où chercher. Pour des "
         r"scores : moyenne nulle, variances $\lambda_j$ (avec `ddof=1`), covariances nulles (M12d.19).",
)

M12D_37_GIVEN = '''IMAGE_37 = wbm.datasets.load_image("tasse")       # 400 × 600 grey levels, CC0
BUDGET_37 = int(0.05 * IMAGE_37.size)               # at most 12 000 numbers'''

M12D_37_CHECK = '''with checked("M12d.37 défi"):
    import inspect
    import re
    problems, ok_37, ran_37 = [], False, False
    try:
        source_37 = inspect.getsource(compress) + inspect.getsource(decompress)
    except (OSError, TypeError):
        source_37 = ""
    banned_37 = sorted(set(re.findall(r"\\b(fft|dct|scipy|sklearn|PIL|imageio|cv2|zlib|pickle|bz2|lzma|gzip|load_image|"
                                      r"IMAGE_37|view|frombuffer|tobytes|struct|bytes|u?int8|u?int16|u?int32|float16|"
                                      r"float32|half|single)\\b", source_37)))
    if banned_37:
        ran_37 = True
        problems.append(f"compress ou decompress utilise {', '.join(banned_37)}, interdit dans ce défi")
    images_37 = [("la photo", IMAGE_37), ("la photo retournée de gauche à droite", IMAGE_37[:, ::-1].copy())]
    for name_t, A_t in (images_37 if not banned_37 else ()):
        try:
            parts_t = list(compress(A_t.copy()))
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            ran_37 = True
            problems.append(f"compress lève {type(exc).__name__} ({exc})")
            break
        ran_37 = True
        arrays_t = [np.asarray(part) for part in parts_t]
        if not arrays_t or not all((np.issubdtype(a.dtype, np.integer) or np.issubdtype(a.dtype, np.floating))
                                   and a.dtype.itemsize == 8 for a in arrays_t):
            problems.append("compress doit rendre une liste de tableaux NumPy de nombres sur 64 bits (float64 ou int64)")
            break
        count_t = sum(a.size for a in arrays_t)
        try:
            B_t = np.asarray(decompress([a.copy() for a in arrays_t], A_t.shape), dtype=float)
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"decompress lève {type(exc).__name__} ({exc})")
            break
        if B_t.shape != A_t.shape:
            problems.append(f"decompress rend la forme {B_t.shape}, pas {A_t.shape}")
            break
        kept_t = 1 - float(np.sum((A_t - B_t) ** 2) / np.sum((A_t - A_t.mean()) ** 2))
        print(f"{name_t} : {count_t} nombres ({count_t / A_t.size:.2%}), énergie gardée {kept_t:.2%}".replace(".", ","))
        if count_t > BUDGET_37:
            problems.append(f"{name_t} : {count_t} nombres stockés, au-dessus du budget de {BUDGET_37}")
        if not kept_t >= 0.935:
            problems.append(f"{name_t} : {kept_t:.2%} de l'énergie gardée, sous les 93,5 %".replace(".", ","))
        if problems:
            break
    if problems:
        print("❌ Ex M12d.37 : " + " ; ".join(problems) + ".")
    elif ran_37:
        ok_37 = True
        print("✅ Ex M12d.37 : défi réussi : au moins 93,5 % de l'énergie avec au plus 5 % des nombres, sur les deux images.")'''

M12D_37 = Ex(
    "M12d.37", "🏆", 3, 30, "Défi : compresser une image centrée en gardant 93,5 % de son énergie avec au plus 5 % des "
    "nombres",
    "trouver une représentation de rang faible d'une photo plus économe que la SVD de l'image entière.",
    "fiche §3 et §6 ; Ex M12d.31 et M12d.32", tracks="C", given=M12D_37_GIVEN,
    body=r"""La photo de la tasse (`IMAGE_37`, $400 \times 600$ niveaux de gris) a $240\,000$ pixels. **L'objectif** : écrire
- `compress(A)`, qui rend une **liste de tableaux NumPy** (la représentation compressée), et
- `decompress(parts, shape)`, qui reconstruit à partir de cette liste seule une image $\hat{\mathbf{A}}$ de forme `shape`,

de sorte que l'**énergie gardée** $1 - \lVert \mathbf{A} - \hat{\mathbf{A}} \rVert_F^2 / \lVert \mathbf{A} - \bar{a} \rVert_F^2$ (avec $\bar{a}$ le niveau de gris moyen : l'énergie de l'image **centrée**) soit d'au moins 93,5 %, avec au plus 5 % des nombres : la somme des tailles (`.size`) des tableaux rendus par `compress` ne doit pas dépasser `BUDGET_37` $= 12\,000$. Chaque tableau est de nombres sur 64 bits (`float64` ou `int64`), chaque élément comptant pour un nombre : pas de types plus petits (`uint8`, `float32`…) ni de réinterprétation d'octets (`view`, `frombuffer`, `tobytes`). La forme `shape` et les constantes écrites dans ton code (une taille, un rang) ne comptent pas ; le niveau moyen, s'il est stocké, compte pour un nombre. La vérification essaie aussi la photo retournée de gauche à droite (une compression honnête y fait aussi bien). NumPy est permis, `np.linalg.svd` et ta librairie compris ; les transformées de Fourier ou en cosinus (`np.fft`, `scipy`), scikit-learn et les bibliothèques d'images ou de compression sont interdits.

Point de départ (M12d.32) : la SVD de l'image entière centrée, au plus grand rang qui tient dans le budget ($k(m + n + 1) + 1 \le 12\,000$, soit $k = 11$), ne garde qu'environ 89 % de l'énergie. Il faut une **autre matrice** que l'image elle-même, dont les valeurs singulières décroissent plus vite. Une dernière cellule enregistre si l'objectif est atteint.

Dans ta copie : quelle matrice as-tu décomposée, et pourquoi ses valeurs singulières décroissent-elles plus vite que celles de l'image ? Comment as-tu choisi les réglages (une taille, un rang), et que gardes-tu au mieux ? Regarde ta reconstruction : quels défauts voit-on (des blocs ?), que la norme de Frobenius ne mesure pas ?""",
    todo='''def compress(A):
    """A list of NumPy arrays from which decompress(parts, A.shape) rebuilds an approximation of A."""
    raise NotImplementedError("une liste de tableaux : au plus BUDGET_37 nombres en tout")


def decompress(parts, shape):
    """The approximation of the image of the given shape, from the list of arrays returned by compress."""
    raise NotImplementedError("reconstruis l'image à partir de parts seulement")''',
    check=M12D_37_CHECK + '''
with checked("M12d.37"):
    if not ran_37:                               # ⏳ while compress is not written
        raise NotImplementedError("compress, ou une fonction qu'elle appelle, n'est pas encore écrite")
    wbm.check("M12d.37", bool(ok_37), computed=True)''',
    solution='''def compress(A):
    """A list of NumPy arrays from which decompress(parts, A.shape) rebuilds an approximation of A."""
    b, k = 8, 3                                   # 8 × 8 squares, 3 components
    m, n = A.shape
    patches = A.reshape(m // b, b, n // b, b).transpose(0, 2, 1, 3).reshape(-1, b * b)   # one square per row
    mean = patches.mean(axis=0)                   # the mean square (64 numbers)
    _, _, Vt = np.linalg.svd(patches - mean, full_matrices=False)
    return [mean, Vt[:k], (patches - mean) @ Vt[:k].T]   # 64 + 3 × 64 + 3 750 × 3 = 11 506 numbers


def decompress(parts, shape):
    """The approximation of the image of the given shape, from the list of arrays returned by compress."""
    mean, W, Z = parts
    b = int(round(np.sqrt(W.shape[1])))
    m, n = shape
    patches = Z @ W + mean
    return patches.reshape(m // b, n // b, b, b).transpose(0, 2, 1, 3).reshape(m, n)


fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
axes[0].imshow(IMAGE_37, cmap="gray", vmin=0, vmax=255)
axes[0].set_title("l'original")
axes[1].imshow(np.clip(decompress(compress(IMAGE_37), IMAGE_37.shape), 0, 255), cmap="gray", vmin=0, vmax=255)
axes[1].set_title("carrés 8 × 8, 3 composantes")
for ax in axes:
    ax.axis("off")
plt.show()''',
    after=[("solution", M12D_37_CHECK)],
    record='''wbm.record("M12d.37", True,
           mistakes={"l'objectif n'est pas atteint : la cellule du défi dit pourquoi": False})''',
    note=r"L'idée : découper l'image en carrés de $8 \times 8$ pixels, et ranger chaque carré en ligne d'une matrice de "
         r"forme $(3\,750, 64)$. Les carrés se ressemblent (des zones lisses, des bords, du grain) : cette matrice a des "
         r"valeurs singulières qui décroissent bien plus vite que celles de l'image, et son ACP (fiche §6 : centrer par le "
         r"carré moyen, puis la SVD) garde 94 % de l'énergie avec 3 composantes, pour $64 + 3 \times 64 + 3\,750 \times 3 "
         r"= 11\,506$ nombres. Des carrés de $10 \times 10$ ou $20 \times 20$ font presque aussi bien. Des tuiles "
         r"$50 \times 50$ décomposées chacune par sa propre SVD, au rang choisi au mieux, ne dépassent pas 90 % : leurs "
         r"bases ne sont pas partagées. La seule moyenne de chaque rectangle de $4 \times 5$ pixels (tout le budget) garde "
         r"93,3 % : d'où l'objectif de 93,5 %. Les défauts visibles sont des bords de carrés : JPEG les atténue, et "
         r"compte des bits plutôt que des nombres.",
)

PART_A = Part("A", "Ta librairie : SVD, rang faible, conditionnement, pseudo-inverse, axes principaux ; NumPy et "
                   "scikit-learn",
              "Fiche §1 à §7. Les six fonctions de `mymath/svd_pca.py`, puis les mêmes calculs avec NumPy et "
              "scikit-learn.",
              given=TOOLS, exercises=[M12D_26, M12D_27, M12D_28, M12D_29, M12D_30])

PART_B = Part("B", "Une prédiction, deux expériences et une figure",
              "Fiche §1 à §4. Les valeurs singulières d'une photo, sa compression par le rang faible, la précision de "
              "la SVD par AᵀA, et la géométrie de la SVD.",
              exercises=[M12D_31, M12D_32, M12D_33, M12D_34])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §3, §5 à §7. Trois erreurs à trouver dans une ACP, un test de propriétés, puis la compression "
              "d'une photo.",
              exercises=[M12D_35, M12D_36, M12D_37])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M12d.1 à M12d.13, M12d.20, M12d.21 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M12d · SVD et analyse en composantes principales — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m12d_svd_acp/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M12d`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M12d · SVD et analyse en composantes principales — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : SVD à la main, SVD compacte, image du cercle unité, "
               "approximation de rang faible et son erreur, coût de stockage, pseudo-inverse, conditionnement, axes "
               "principaux, scores et reconstruction, variance expliquée, ACP par la SVD et en grande dimension, "
               "voisinages de t-SNE, anomalies, changement d'unités.\n"
               "- Écrire les six fonctions de `mymath/svd_pca.py` et les tester, puis comparer avec NumPy et "
               "scikit-learn.\n"
               "- Prédire et mesurer la compression d'une photo, mesurer la précision de la SVD par AᵀA, dessiner la "
               "SVD, chasser des erreurs dans une ACP, écrire un test de propriétés, relever un défi de compression.\n\n"
               r"**Rappel express.** $\mathbf{A} = \mathbf{U}\mathbf{S}\mathbf{V}^\top = \sum_i s_i\mathbf{u}_i\mathbf{v}_i^\top$, "
               r"$s_i = \sqrt{\lambda_i(\mathbf{A}^\top\mathbf{A})}$, $\mathbf{u}_i = \mathbf{A}\mathbf{v}_i/s_i$ ; "
               r"$\lVert \mathbf{A}\mathbf{x} \rVert \le s_1\lVert \mathbf{x} \rVert$ ; $\lVert \mathbf{A} - \mathbf{A}_k \rVert_F^2 = "
               r"\sum_{i > k} s_i^2$, $k(m + n + 1)$ nombres ; $\mathbf{A}^+ = \mathbf{V}\mathbf{S}^{-1}\mathbf{U}^\top$, "
               r"$\mathbf{x}^+ = \mathbf{A}^+\mathbf{b}$ ; $\kappa = s_{\max}/s_{\min}$, $\kappa(\mathbf{A}^\top\mathbf{A}) = "
               r"\kappa^2$ ; $\mathbf{C} = \frac{1}{n-1}\mathbf{X}_c^\top\mathbf{X}_c$, axes = vecteurs propres, "
               r"$\lambda_j = s_j^2/(n - 1)$ ; scores $\mathbf{Z} = \mathbf{X}_c\mathbf{W}_k$, $\hat{\mathbf{X}} = "
               r"\mathbf{Z}\mathbf{W}_k^\top + \boldsymbol{\mu}$ ; erreur moyenne $\frac{n-1}{n}\sum_{j > k}\lambda_j$ ; "
               r"perplexité $2^{H}$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu calculer la SVD d'une petite matrice par AᵀA, et l'interpréter comme rotation, étirement, "
               "rotation ?\n"
               "2. Sais-tu calculer une approximation de rang faible, son erreur et son coût de stockage ?\n"
               "3. Sais-tu calculer une pseudo-inverse et un conditionnement, et dire ce qu'ils signifient ?\n"
               "4. Sais-tu faire une ACP à la main (covariance, axes, scores, reconstruction) et lire une variance "
               "expliquée ?\n"
               "5. Sais-tu dire ce que t-SNE et UMAP gardent, et ce qu'une de leurs cartes ne permet pas de conclure ?\n\n"
               "**La suite** : le chapitre 12 de workbookIA (préparation des données), puis M13a, vraisemblance et "
               "régression logistique.")]


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
