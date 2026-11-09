#!/usr/bin/env python
"""Build the two notebooks of chapter M12b from a single source (used by Claude).

    python tools/chapters/build_m12b.py
    python tools/run_all_notebooks.py chapitres/m12b_orthogonalite/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m12b_orthogonalite/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M12b.1 to M12b.12, 🔗 M12b.18 and M12b.19); parts A to C are the notebook
exercises. Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it. The data
are new: none is a test case of tests/test_m12b_orthogonal.py, an example of the fiche or of a docstring of
orthogonal.py, data of M07, M09b or M12a, or an example of workbookIA 0B, 9, 12 and 25 (no u = (0,6 ; 0,8), no cloud
projected on a principal axis, no covariance matrix, no [[1, r], [r, 1]], no linear autoencoder).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M12b"
FOLDER = "chapitres/m12b_orthogonalite"

FREE_SIGNS = "résous les deux équations pour x₁ et x₂ en fonction de x₃ et x₄, signes compris"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M12b.1", "Un produit scalaire défini par une matrice 2 × 2 : normes, angles, orthogonalité", [
        ("a", "True or False", "bool(M_1[0, 0] > 0 and M_1.det() > 0)",
         '''mistakes={"le critère en dimension 2 : a > 0 et ac − b² > 0": False}'''),
        ("b", "a number", "ip_1([1, 0], [0, 1])",
         '''mistakes={"⟨e₁, e₂⟩_M = e₁ᵀ M e₂ : un élément de M, pas le produit usuel": 0}'''),
        ("c", "a number (4 decimals)", "float(sympy.sqrt(ip_1([1, 0], [1, 0])))",
         '''decimals=4, mistakes={"la norme est la racine de ⟨e₁, e₁⟩_M": 3.0}'''),
        ("d", "a number (4 decimals)", "float(ip_1([1, 0], [0, 1]) / sympy.sqrt(ip_1([1, 0], [1, 0]) * ip_1([0, 1], [0, 1])))",
         '''decimals=4, mistakes={"divise par les deux normes pour ⟨·,·⟩_M, pas par les normes usuelles": 1.0, '''
         '''"l'angle se calcule avec ⟨·,·⟩_M, pas avec le produit usuel": 0.0}'''),
        ("e", "a number", "float(sympy.sqrt(ip_1([2, -1], [2, -1])))",
         '''decimals=4, mistakes={"la norme pour ⟨·,·⟩_M : la racine de xᵀMx, pas la norme usuelle": float(sympy.sqrt(5)), '''
         '''"la norme est la racine de xᵀMx": 9.0}'''),
        ("f", "True or False", "ip_1([1, -1], [0, 1]) == 0",
         '''mistakes={"calcule (1, −1)ᵀ M e₂ : l'orthogonalité dépend du produit scalaire": False}'''),
        ("g", "a number", "sympy.solve(ip_1([1, K], [1, 1]), K)[0]",
         '''mistakes={"(1, k)ᵀ M (1, 1) = 0, avec M, pas avec le produit usuel": -1}'''),
        ("h", "True or False", "bool(sympy.Matrix([[2, 3], [3, 4]]).det() > 0)",
         '''mistakes={"le critère : ac − b² doit être positif": True}'''),
    ]),

    Paper("M12b.2", "Les coordonnées dans une base orthonormée : des produits scalaires au lieu d'un système", [
        ("a", "a number", "(U_2[:, 0].T * U_2[:, 1])[0]"),
        ("b", "a number", "sympy.sqrt((U_2[:, 2].T * U_2[:, 2])[0])",
         '''mistakes={"n'oublie pas le facteur 1/5 du vecteur": 5}'''),
        ("c", "a list of 4 numbers", "exact(U_2.T * X_2)",
         '''mistakes={"les coordonnées sont les produits scalaires x · uᵢ, facteur 1/5 compris": exact(5 * U_2.T * X_2), '''
         '''"les coordonnées sont Uᵀx (des produits scalaires), pas Ux": exact(U_2 * X_2)}'''),
        ("d", "a number", "sum(c ** 2 for c in U_2.T * X_2)",
         '''mistakes={"Parseval : la somme des carrés des coordonnées": sum(U_2.T * X_2)}'''),
        ("e", "a list of 4 numbers (1 decimal)", "exact(U_2 * sympy.Matrix([1, 0, -1, 2]))",
         '''decimals=1, mistakes={"le vecteur est U c, la combinaison des colonnes, pas Uᵀ c": '''
         '''exact(U_2.T * sympy.Matrix([1, 0, -1, 2]))}'''),
        ("f", "a list of 4 numbers (1 decimal)", "exact(sympy.Matrix([3, -2, 1, sympy.Rational(1, 2)]))",
         '''decimals=1, mistakes={"la base n'est plus orthonormée : divise x · (2u₄) par ‖2u₄‖²": [3, -2, 1, 2], '''
         '''"divise par le carré de la norme de 2u₄, pas par la norme": [3, -2, 1, 1]}'''),
    ]),

    Paper("M12b.3", "Une matrice orthogonale 3 × 3 conserve normes et angles", [
        ("a", "True or False", "Q_3.T * Q_3 == sympy.eye(3)",
         '''mistakes={"vérifie QᵀQ = I : chaque colonne de norme 1, deux colonnes distinctes orthogonales": False}'''),
        ("b", "a list of 3 numbers (4 decimals)", "exact(Q_3 * X_3)",
         '''decimals=4, mistakes={"Q x combine les colonnes de Q, pas ses lignes": exact(Q_3.T * X_3)}'''),
        ("c", "a number (4 decimals)", "float(sympy.sqrt((Q_3 * X_3).dot(Q_3 * X_3)))",
         '''decimals=4, mistakes={"la norme est la racine de la somme des carrés": 2.0}'''),
        ("d", "a number", "(Q_3 * X_3).dot(Q_3 * Y_3)",
         '''mistakes={"refais le produit scalaire, signes compris": 1}'''),
        ("e", "a list of 3 numbers", "exact(Q_3.T * sympy.Matrix([7, 0, 0]))",
         '''mistakes={"z = Q⁻¹(7, 0, 0) et Q⁻¹ = Qᵀ, pas Q": exact(Q_3 * sympy.Matrix([7, 0, 0]))}'''),
        ("f", "True or False", "(2 * Q_3).T * (2 * Q_3) == sympy.eye(3)",
         '''mistakes={"(2Q)ᵀ(2Q) = 4QᵀQ : les colonnes ne sont plus de norme 1": True}'''),
        ("g", "True or False", "(Q_3 * P_3).T * (Q_3 * P_3) == sympy.eye(3)",
         '''mistakes={"P est une permutation, donc orthogonale ; et un produit de matrices orthogonales l'est aussi": False}'''),
    ]),

    Paper("M12b.4", "Gram-Schmidt sur trois vecteurs de ℝ³", [
        ("a", "a number", "sympy.sqrt(A1_4.dot(A1_4))", '''mistakes={"la norme est la racine de 16 + 1 + 64": 81}'''),
        ("b", "a number", "A2_4.dot(Q1_4)",
         '''mistakes={"a₂ · q₁ = (a₂ · a₁) / ‖a₁‖ : q₁ est unitaire": A2_4.dot(A1_4)}'''),
        ("c", "a list of 3 numbers (4 decimals)", "exact(V2_4)",
         '''decimals=4, mistakes={"a₂ · q₁ est négatif : on soustrait (a₂ · q₁) q₁, donc on ajoute un multiple de q₁": '''
         '''exact(A2_4 + A2_4.dot(Q1_4) * Q1_4), '''
         '''"on retire la projection sur q₁ (unitaire), pas sur a₁": exact(A2_4 - A2_4.dot(Q1_4) * A1_4)}'''),
        ("d", "a number", "sympy.sqrt(V2_4.dot(V2_4))", '''mistakes={"la norme, pas son carré": V2_4.dot(V2_4)}'''),
        ("e", "a list of 3 numbers (4 decimals)", "exact(Q2_4)",
         '''decimals=4, mistakes={"q₂ = v₂ / ‖v₂‖ : normer": exact(V2_4)}'''),
        ("f", "a list of 2 numbers", "[A3_4.dot(Q1_4), A3_4.dot(Q2_4)]",
         '''mistakes={"les produits scalaires avec q₁ et q₂ unitaires, pas avec a₁ et v₂": [A3_4.dot(A1_4), A3_4.dot(V2_4)]}'''),
        ("g", "a list of 3 numbers (4 decimals)", "exact(Q3_4)",
         '''decimals=4, mistakes={"q₃ = v₃ / ‖v₃‖ : normer": exact(A3_4 - A3_4.dot(Q1_4) * Q1_4 - A3_4.dot(Q2_4) * Q2_4)}'''),
        ("h", "True or False", "True",
         '''mistakes={"Gram-Schmidt garde, à chaque étape, le sous-espace engendré par les premiers vecteurs": False}'''),
    ]),

    Paper("M12b.5", "Gram-Schmidt pour un produit scalaire qui n'est pas l'usuel", [
        ("a", "a number", "ip_5(A1_5, A2_5)",
         '''mistakes={"⟨x, y⟩_D compte deux fois le produit des deuxièmes coordonnées": A1_5.dot(A2_5)}'''),
        ("b", "a number", "sympy.sqrt(ip_5(A1_5, A1_5))", '''mistakes={"la norme, pas son carré": ip_5(A1_5, A1_5)}'''),
        ("c", "a list of 3 numbers (1 decimal)", "exact(Q1_5)",
         '''decimals=1, mistakes={"divise a₁ par sa norme pour ⟨·,·⟩_D, pas par sa norme usuelle": '''
         '''exact(A1_5 / sympy.sqrt(A1_5.dot(A1_5)))}'''),
        ("d", "a list of 3 numbers (1 decimal)", "exact(V2_5)",
         '''decimals=1, mistakes={"⟨a₂, q₁⟩_D est négatif : on soustrait ⟨a₂, q₁⟩_D q₁, donc on ajoute un multiple de q₁": '''
         '''exact(A2_5 + ip_5(A2_5, Q1_5) * Q1_5)}'''),
        ("e", "a number", "sympy.sqrt(ip_5(V2_5, V2_5))", '''mistakes={"la norme, pas son carré": ip_5(V2_5, V2_5)}'''),
        ("f", "a list of 3 numbers (4 decimals)", "exact(Q2_5)", '''decimals=4, mistakes={"q₂ = v₂ / ‖v₂‖_D : normer": exact(V2_5)}'''),
        ("g", "a list of 2 numbers", "[ip_5(X_5, Q1_5), ip_5(X_5, Q2_5)]",
         '''mistakes={"l'ordre : la coordonnée sur q₁ d'abord": [ip_5(X_5, Q2_5), ip_5(X_5, Q1_5)]}'''),
        ("h", "a list of 3 numbers", "exact(ip_5(X_5, Q1_5) * Q1_5 + ip_5(X_5, Q2_5) * Q2_5)",
         '''mistakes={"le projeté, pas le résidu x − p": exact(X_5 - ip_5(X_5, Q1_5) * Q1_5 - ip_5(X_5, Q2_5) * Q2_5)}'''),
    ]),

    Paper("M12b.6", "Une base du complément orthogonal d'un plan de ℝ⁴", [
        ("a", "an integer", "4 - A_6.rank()", '''mistakes={"dim U⊥ = n − dim U, avec n = 4 et dim U = 2": 3}'''),
        ("b", "a list of 4 numbers", "exact(KERNEL_6[0])", f'''mistakes={{"{FREE_SIGNS}": [-1, 1, 1, 0]}}'''),
        ("c", "a list of 4 numbers", "exact(KERNEL_6[1])", f'''mistakes={{"{FREE_SIGNS}": [2, 1, 0, 1]}}'''),
        ("d", "True or False", "A_6 * sympy.Matrix([-3, -3, 1, 2]) == sympy.zeros(2, 1)",
         '''mistakes={"calcule w · a et w · b": False}'''),
        ("e", "a list of 2 numbers", "[1, 2]",
         '''mistakes={"les coordonnées de w dans cette base sont ses coordonnées libres (x₃, x₄), dans cet ordre": [2, 1]}'''),
        ("f", "True or False", "KERNEL_6[0].dot(KERNEL_6[1]) == 0", '''mistakes={"calcule leur produit scalaire": True}'''),
        ("g", "True or False", "all(sympy.Matrix([1, 1, 0, 3]).dot(k) == 0 for k in KERNEL_6)",
         '''mistakes={"un vecteur est dans U si et seulement s'il est orthogonal à tout U⊥ (ou : combine a et b)": False}'''),
    ]),

    Paper("M12b.7", "Projeter sur un plan de ℝ³ : avec une base quelconque, puis orthonormée", [
        ("a", "a matrix", "matrix(A_7.T * A_7)",
         '''mistakes={"AᵀA a la forme (2, 2) : les produits scalaires des colonnes a₁ et a₂": matrix(A_7 * A_7.T)}'''),
        ("b", "a list of 2 numbers", "exact(A_7.T * V_7)"),
        ("c", "a list of 2 numbers", "exact(C_7)",
         '''mistakes={"l'ordre : le coefficient de a₁ d'abord": exact(C_7[::-1])}'''),
        ("d", "a list of 3 numbers", "exact(A_7 * C_7)", '''mistakes={"le projeté p, pas le résidu v − p": exact(V_7 - A_7 * C_7)}'''),
        ("e", "a list of 2 numbers", "[V_7.dot(Q1_7), V_7.dot(Q2_7)]",
         '''mistakes={"n'oublie pas le facteur 1/9 de q₁ et de q₂": [9 * V_7.dot(Q1_7), 9 * V_7.dot(Q2_7)]}'''),
        ("f", "a list of 3 numbers", "exact(V_7 - A_7 * C_7)", '''mistakes={"le résidu est v − p, dans cet ordre": exact(A_7 * C_7 - V_7)}'''),
        ("g", "True or False", "A_7.T * (V_7 - A_7 * C_7) == sympy.zeros(2, 1)",
         '''mistakes={"calcule (v − p) · a₁ et (v − p) · a₂ ; le résidu d'une projection orthogonale est orthogonal à U": False}'''),
    ]),

    Paper("M12b.8", "La matrice de projection : P² = P, Pᵀ = P, trace et rang", [
        ("a", "True or False", "P_8.T == P_8", '''mistakes={"compare les éléments (i, j) et (j, i)": False}'''),
        ("b", "a list of 3 numbers", "exact(P_8 * sympy.Matrix([1, 1, -1]))"),
        ("c", "a list of 3 numbers", "exact(P_8 * sympy.Matrix([1, 0, 1]))"),
        ("d", "a number", "P_8.trace()", '''mistakes={"la trace de P : n'oublie pas le facteur 1/3": 3 * P_8.trace()}'''),
        ("e", "an integer", "P_8.rank()", '''mistakes={"P écrase la direction de b) : son rang est la dimension de U": 3}'''),
        ("f", "a list of 3 numbers", "exact((sympy.eye(3) - P_8) * sympy.Matrix([3, 0, 0]))",
         '''mistakes={"(I − P) v = v − P v, pas P v": exact(P_8 * sympy.Matrix([3, 0, 0]))}'''),
        ("g", "True or False", "P_8.det() != 0", '''mistakes={"un vecteur non nul a pour image 0 : relis b)": True}'''),
        ("h", "True or False", "False",
         '''mistakes={"une projection orthogonale est idempotente et symétrique : compare M et Mᵀ": True}'''),
    ]),

    Paper("M12b.9", "La distance d'un point à un sous-espace, et le résidu orthogonal", [
        ("a", "True or False", "U1_9.dot(U2_9) == 0", '''mistakes={"u₁ · u₂ = 1 − 1 + 2 − 2": False}'''),
        ("b", "a number", "V_9.dot(U1_9) / U1_9.dot(U1_9)", '''mistakes={"divise v · u₁ par ‖u₁‖²": V_9.dot(U1_9)}'''),
        ("c", "a number", "V_9.dot(U2_9) / U2_9.dot(U2_9)", '''mistakes={"divise v · u₂ par ‖u₂‖²": V_9.dot(U2_9)}'''),
        ("d", "a list of 4 numbers", "exact(P_9)", '''mistakes={"le projeté p, pas le résidu v − p": exact(V_9 - P_9)}'''),
        ("e", "a list of 4 numbers", "exact(V_9 - P_9)", '''mistakes={"le résidu est v − p, dans cet ordre": exact(P_9 - V_9)}'''),
        ("f", "a number", "sympy.sqrt((V_9 - P_9).dot(V_9 - P_9))",
         '''mistakes={"la distance est ‖v − p‖ : prends la racine": (V_9 - P_9).dot(V_9 - P_9)}'''),
        ("g", "a number (4 decimals)",
         "float(sympy.sqrt(V_9.dot(V_9) - V_9.dot(U1_9) ** 2 / U1_9.dot(U1_9)))",
         '''decimals=4, mistakes={"la distance, pas son carré": float(V_9.dot(V_9) - V_9.dot(U1_9) ** 2 / U1_9.dot(U1_9))}'''),
        ("h", "a number", "P_9.dot(P_9)", '''mistakes={"‖p‖², pas ‖v‖²": V_9.dot(V_9)}'''),
    ]),

    Paper("M12b.10", "Des moindres carrés comme une projection : y, son projeté et le résidu", [
        ("a", "a matrix", "matrix(X_10.T * X_10)"),
        ("b", "a list of 2 numbers", "exact(X_10.T * Y_10)"),
        ("c", "a list of 2 numbers (1 decimal)", "exact(W_10)",
         '''decimals=1, mistakes={"l'ordre : le biais w₀ d'abord, puis la pente": exact(W_10[::-1])}'''),
        ("d", "a list of 5 numbers (1 decimal)", "exact(X_10 * W_10)",
         '''decimals=1, mistakes={"les prédictions, pas les résidus": exact(Y_10 - X_10 * W_10)}'''),
        ("e", "a list of 5 numbers (1 decimal)", "exact(Y_10 - X_10 * W_10)",
         '''decimals=1, mistakes={"r = y − ŷ, dans cet ordre": exact(X_10 * W_10 - Y_10)}'''),
        ("f", "a list of 2 numbers", "exact(X_10.T * (Y_10 - X_10 * W_10))"),
        ("g", "a number (1 decimal)", "float((Y_10 - X_10 * W_10).dot(Y_10 - X_10 * W_10))",
         '''decimals=1, mistakes={"la somme des carrés des résidus, pas leur somme": 0.0}'''),
        ("h", "a number (1 decimal)", "float((X_10 * W_10).dot(X_10 * W_10))",
         '''decimals=1, mistakes={"‖ŷ‖², pas ‖y‖²": float(Y_10.dot(Y_10))}'''),
    ]),

    Paper("M12b.11", "La décomposition QR d'une matrice 3 × 2, puis les moindres carrés par R w = Qᵀy", [
        ("a", "a number", "R_11[0, 0]", '''mistakes={"la norme, pas son carré": R_11[0, 0] ** 2}'''),
        ("b", "a number", "R_11[0, 1]", '''mistakes={"r₁₂ = q₁ · a₂ = (a₁ · a₂) / ‖a₁‖ : q₁ est unitaire": A_11[:, 0].dot(A_11[:, 1])}'''),
        ("c", "a number", "R_11[1, 1]", '''mistakes={"r₂₂ = ‖v₂‖ : la norme, pas son carré": R_11[1, 1] ** 2}'''),
        ("d", "a list of 3 numbers (4 decimals)", "exact(Q_11[:, 1])",
         '''decimals=4, mistakes={"q₂ = v₂ / ‖v₂‖ : normer": exact(R_11[1, 1] * Q_11[:, 1])}'''),
        ("e", "a matrix", "matrix(R_11)",
         '''mistakes={"R est triangulaire supérieure : r₁₂ est au-dessus de la diagonale": matrix(R_11.T)}'''),
        ("f", "a list of 2 numbers", "exact(Q_11.T * Y_11)"),
        ("g", "a list of 2 numbers (4 decimals)", "[float(w) for w in W_11]",
         '''decimals=4, mistakes={"R est triangulaire supérieure : remonte depuis la dernière ligne": '''
         '''[float((Q_11.T * Y_11)[0] / R_11[0, 0]), float(W_11[1])]}'''),
        ("h", "a list of 3 numbers", "exact(Y_11 - A_11 * W_11)",
         '''mistakes={"le résidu est y − A w*, dans cet ordre": exact(A_11 * W_11 - Y_11)}'''),
    ]),

    Paper("M12b.12", "Le produit scalaire de fonctions sur [−1 ; 1] : orthogonaliser 1, x et x²", [
        ("a", "a number", "ip_12(1, 1)", '''mistakes={"∫ 1 dx sur [−1 ; 1] : l'intervalle a pour longueur 2": 1}'''),
        ("b", "a number (4 decimals)", "float(ip_12(1, x ** 2))",
         '''decimals=4, mistakes={"∫ x² dx de −1 à 1 : les deux moitiés de l'intervalle comptent": float(sympy.Rational(1, 3))}'''),
        ("c", "a number", "float(ip_12(x, x ** 2))",
         '''decimals=4, mistakes={"x³ est impaire : intègre-la sur un intervalle symétrique": 0.5}'''),
        ("d", "a number (4 decimals)", "float(P2_12 - x ** 2)",
         '''decimals=4, mistakes={"c = −⟨x², 1⟩/⟨1, 1⟩ : divise par ⟨1, 1⟩": float(-ip_12(1, x ** 2)), '''
         '''"le signe : on retire la projection de x² sur 1": float(x ** 2 - P2_12)}'''),
        ("e", "a number (4 decimals)", "float(ip_12(P2_12, P2_12))", "decimals=4"),
        ("f", "a number (4 decimals)", "float(ip_12(sympy.Abs(x), P2_12))", "decimals=4"),
        ("g", "a list of 3 numbers (4 decimals)", "[float(c) for c in PROJ_12]",
         '''decimals=4, mistakes={"développe le terme en p₂ = x² + c : il modifie aussi le coefficient constant": '''
         '''[float(ip_12(sympy.Abs(x), 1) / ip_12(1, 1)), 0.0, float(PROJ_12[2])]}'''),
    ]),

    Paper("M12b.18", "Pont : retirer d'une feature ce qu'explique une autre, une projection puis un résidu", [
        ("a", "a number", "T_18"),
        ("b", "a list of 4 numbers", "exact(T_18 * X1_18)"),
        ("c", "a list of 4 numbers", "exact(R_18)", '''mistakes={"r = x₂ − t x₁, dans cet ordre": exact(-R_18)}'''),
        ("d", "a number", "R_18.dot(X1_18)"),
        ("e", "a number (4 decimals)", "float((T_18 * X1_18).dot(T_18 * X1_18) / X2_18.dot(X2_18))",
         '''decimals=4, mistakes={"le rapport des carrés des normes, pas des normes": '''
         '''float(sympy.sqrt((T_18 * X1_18).dot(T_18 * X1_18) / X2_18.dot(X2_18)))}'''),
        ("f", "a number (2 decimals)", "float(Y_18.dot(R_18) / R_18.dot(R_18))",
         '''decimals=2, mistakes={"divise y · r par ‖r‖²": float(Y_18.dot(R_18))}'''),
        ("g", "a list of 2 numbers (2 decimals)", "[float(w) for w in W_18]",
         '''decimals=2, mistakes={"l'ordre : le poids de x₁ d'abord": [float(W_18[1]), float(W_18[0])], '''
         '''"w₁ n'est pas le poids de x₁ seul : résous les équations normales du modèle à deux features": '''
         '''[float(Y_18.dot(X1_18) / X1_18.dot(X1_18)), float(W_18[1])]}'''),
    ]),

    Paper("M12b.19", "Pont : projeter sur k directions orthonormées, reconstruire, et l'erreur par Pythagore", [
        ("a", "True or False", "U_19.T * U_19 == sympy.eye(2)", '''mistakes={"les colonnes de U sont orthonormées": False}'''),
        ("b", "a list of 2 numbers", "exact(Z_19)", '''mistakes={"z = Uᵀx : n'oublie pas le facteur 1/2": exact(2 * Z_19)}'''),
        ("c", "a list of 4 numbers (1 decimal)", "exact(U_19 * Z_19)",
         '''decimals=1, mistakes={"x̂ = z₁u₁ + z₂u₂, facteur 1/2 compris": exact(2 * U_19 * Z_19)}'''),
        ("d", "a list of 4 numbers (1 decimal)", "exact(E_19)", '''decimals=1, mistakes={"e = x − x̂, dans cet ordre": exact(-E_19)}'''),
        ("e", "a list of 2 numbers", "exact(U_19.T * E_19)"),
        ("f", "a number (2 decimals)", "float(E_19.dot(E_19))",
         '''decimals=2, mistakes={"‖e‖², pas ‖e‖ : ne prends pas la racine": float(sympy.sqrt(E_19.dot(E_19)))}'''),
        ("g", "a list of 2 numbers", "exact(H_19[:, 2:].T * X_19)",
         '''mistakes={"u₃ · x et u₄ · x, facteur 1/2 compris": exact(2 * H_19[:, 2:].T * X_19)}'''),
        ("h", "True or False", "U_19 * U_19.T == sympy.eye(4)",
         '''mistakes={"U Uᵀ est de rang 2 : c'est la projection sur Vect(u₁, u₂), pas l'identité": True}'''),
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


def gram_schmidt_exact(columns, ip):
    """Exact Gram-Schmidt of the columns (SymPy vectors) for the inner product ip: the orthonormal vectors."""
    qs = []
    for a in columns:
        v = a - sum((ip(a, q) * q for q in qs), sympy.zeros(*a.shape))
        qs.append(v / sympy.sqrt(ip(v, v)))
    return qs


V = sympy.Matrix
K, x = sympy.symbols("k x")
M_1 = V([[3, 1], [1, 1]])                                                                   # M12b.1


def ip_1(u, w):
    return (V(u).T * M_1 * V(w))[0]


U_2 = V([[1, 2, 2, 4], [2, -1, -4, 2], [2, 4, -1, -2], [4, -2, 2, -1]]).T / 5                # M12b.2
X_2 = V([1, 2, 3, 1])
Q_3 = V([[2, 6, 3], [3, 2, -6], [6, -3, 2]]) / 7                                            # M12b.3
X_3, Y_3 = V([1, 0, 1]), V([0, 1, -1])
P_3 = V([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
A1_4, A2_4, A3_4 = V([4, 1, 8]), V([1, 1, -4]), V([-1, 3, -1])                              # M12b.4
Q1_4, Q2_4, Q3_4 = gram_schmidt_exact([A1_4, A2_4, A3_4], lambda u, w: u.dot(w))
V2_4 = A2_4 - A2_4.dot(Q1_4) * Q1_4
D_5 = sympy.diag(1, 2, 1)                                                                   # M12b.5


def ip_5(u, w):
    return (u.T * D_5 * w)[0]


A1_5, A2_5, X_5 = V([1, 1, -1]), V([2, -1, 2]), V([4, -2, -2])
Q1_5, Q2_5 = gram_schmidt_exact([A1_5, A2_5], ip_5)
V2_5 = A2_5 - ip_5(A2_5, Q1_5) * Q1_5
A_6 = V([[1, 0, -1, 2], [0, 1, 1, 1]])                                                      # M12b.6
KERNEL_6 = A_6.nullspace()
A_7, V_7 = V([[1, 0], [0, -4], [2, 1]]), V([10, 3, -1])                                    # M12b.7
C_7 = (A_7.T * A_7).solve(A_7.T * V_7)
Q1_7, Q2_7 = V([4, 4, 7]) / 9, V([1, -8, 4]) / 9
assert Q1_7.dot(Q2_7) == 0 and Q1_7.dot(Q1_7) == 1 and A_7.T * V([8, -1, -4]) == sympy.zeros(2, 1)
P_8 = V([[2, -1, 1], [-1, 2, 1], [1, 1, 2]]) / 3                                            # M12b.8
assert P_8 * P_8 == P_8
U1_9, U2_9, V_9 = V([1, 1, 1, 1]), V([1, -1, 2, -2]), V([2, 0, 5, 1])                       # M12b.9
P_9 = V_9.dot(U1_9) / U1_9.dot(U1_9) * U1_9 + V_9.dot(U2_9) / U2_9.dot(U2_9) * U2_9
X_10, Y_10 = V([[1, k] for k in range(1, 6)]), V([3, 3, 4, 7, 8])                           # M12b.10
W_10 = (X_10.T * X_10).solve(X_10.T * Y_10)
A_11, Y_11 = V([[2, 2], [6, 3], [9, 0]]), V([9, -3, 11])                                   # M12b.11
Q_11 = V.hstack(*gram_schmidt_exact([A_11[:, 0], A_11[:, 1]], lambda u, w: u.dot(w)))
R_11 = (Q_11.T * A_11).applyfunc(sympy.nsimplify)
W_11 = R_11.solve(Q_11.T * Y_11)


def ip_12(f, g):                                                                            # M12b.12
    return sympy.integrate(f * g, (x, -1, 1))


P2_12 = sympy.expand(x ** 2 - ip_12(x ** 2, 1) / ip_12(1, 1) - ip_12(x ** 2, x) / ip_12(x, x) * x)
PROJ_12 = sympy.Poly(sympy.expand(ip_12(sympy.Abs(x), 1) / ip_12(1, 1) + ip_12(sympy.Abs(x), x) / ip_12(x, x) * x
                                  + ip_12(sympy.Abs(x), P2_12) / ip_12(P2_12, P2_12) * P2_12), x).all_coeffs()[::-1]
X1_18, X2_18, Y_18 = V([2, 2, 1, 1]), V([1, 3, 0, 2]), V([3, 6, 1, 4])                      # M12b.18
T_18 = X2_18.dot(X1_18) / X1_18.dot(X1_18)
R_18 = X2_18 - T_18 * X1_18
X_18 = V.hstack(X1_18, X2_18)
W_18 = (X_18.T * X_18).solve(X_18.T * Y_18)
H_19 = V([[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]]).T / 2              # M12b.19
U_19, X_19 = H_19[:, :2], V([4, 2, 3, -1])
Z_19 = U_19.T * X_19
E_19 = X_19 - U_19 * Z_19'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M12b.1 à M12b.12, 🔗 M12b.18 et M12b.19)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une liste `[0, -2, 5]` pour un vecteur, une liste de lignes `[[1, 0], [-2, 3]]` pour une matrice, "
               "ou `True` / `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M12b.24 to M12b.27)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
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


def orthogonality_loss(Q):
    """The largest |QᵀQ − I|: 0 for orthonormal columns, about 1 when two columns point the same way."""
    Q = np.asarray(Q, dtype=float)
    return float(np.max(np.abs(Q.T @ Q - np.eye(Q.shape[1]))))'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12b")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/orthogonal.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "Une famille de vecteurs est donnée par les **colonnes** d'une matrice. NumPy est permis, `@`, `.T`, "
         "`np.linalg.norm` et `np.linalg.solve` compris ; `np.linalg.qr`, `lstsq`, `pinv`, `inv`, `scipy.linalg` et "
         "scikit-learn sont interdits : les tests comparent tes résultats aux leurs, et un test vérifie que tu ne t'en "
         "sers pas. Ne modifie jamais la matrice reçue : travaille sur une copie, `np.array(A, dtype=float)`.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError", "LinAlgError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of orthogonal.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_orthogonal_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m12b_orthogonal.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m12b_orthogonal.py", "{keyword}", impl="ref")')]


def value_error(message: str) -> str:
    return (f'''mistakes={{"{message}": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}}''')


A_24 = "[[6, 3], [6, 2], [7, 2]]"

M12B_24 = Ex(
    "M12b.24", "🔨", 2, 25, "Gram-Schmidt, classique et modifié · `gram_schmidt`",
    "programmer le procédé de Gram-Schmidt, dans ses versions classique et modifiée, avec la convention de signe et la "
    "détection des colonnes dépendantes.", "fiche §3", tracks="C, E", mymath="orthogonal.py",
    body=HOWTO + r"""

Écris `gram_schmidt(A, modified=True, tol=1e-10)` (fiche §3), en suivant la docstring : une copie en flottants, une `ValueError` si $\mathbf{A}$ n'est pas à deux dimensions, puis une boucle sur les colonnes. Pour la colonne $k$ : $\mathbf{v} \leftarrow \mathbf{a}_k$, puis, pour chaque $j < k$, $\mathbf{v} \leftarrow \mathbf{v} - c\,\mathbf{q}_j$ avec $c = \mathbf{q}_j \cdot \mathbf{a}_k$ (classique, `modified=False`) ou $c = \mathbf{q}_j \cdot \mathbf{v}$ (modifié, le vecteur **courant**). Si $\lVert \mathbf{v} \rVert \le \mathrm{tol} \times \lVert \mathbf{a}_k \rVert$ (ou si $\mathbf{v}$ est nul), les colonnes sont dépendantes : `ValueError`. Sinon $\mathbf{q}_k = \mathbf{v}/\lVert \mathbf{v} \rVert$, ce qui donne $\mathbf{q}_k \cdot \mathbf{a}_k > 0$.

La vérification calcule, avec $\mathbf{A}$ = `""" + A_24 + r"""` :
- a) `gram_schmidt(A)` (une matrice, 6 décimales) ;
- b) vrai ou faux : `gram_schmidt(A, modified=False)` et `gram_schmidt(A)` sont égales à $10^{-12}$ près ;
- c) vrai ou faux : pour une matrice de forme $(6, 4)$ tirée au hasard (`np.random.default_rng(24)`, loi normale), `orthogonality_loss(gram_schmidt(...))` est inférieure à $10^{-12}$ ;
- d) `gram_schmidt([[-2, 0], [0, -3]])` (une matrice) ;
- e) le nom de l'erreur levée par `gram_schmidt([[1, 2], [2, 4], [3, 6]])` ;
- f) le nom de l'erreur levée par `gram_schmidt([1, 2, 3])` ;
- g) vrai ou faux : après `gram_schmidt(M)`, le tableau `M` (une copie en flottants de $\mathbf{A}$) n'a pas changé.

La fonction `orthogonality_loss(Q)` des outils rend le plus grand $|(\mathbf{Q}^\top\mathbf{Q} - \mathbf{I})_{ij}|$. Dans ta copie : retrouve a) à la main (les colonnes de $\mathbf{Q}$ sont des onzièmes). Pourquoi d) a-t-il des $-1$ sur la diagonale ? Pourquoi e) lève-t-elle une erreur, et que vaut $\mathbf{v}_2$ dans ce cas ?""",
    todo=LOAD_LEARNER,
    check=f'''M_24 = np.array({A_24}, dtype=float)
with checked("M12b.24a"):
    wbm.check("M12b.24a", np.asarray(mymath.orthogonal.gram_schmidt({A_24})).tolist(), computed=True)
with checked("M12b.24b"):
    wbm.check("M12b.24b", bool(np.allclose(mymath.orthogonal.gram_schmidt({A_24}, modified=False),
                                           mymath.orthogonal.gram_schmidt({A_24}), rtol=0, atol=1e-12)), computed=True)
with checked("M12b.24c"):
    wbm.check("M12b.24c", orthogonality_loss(mymath.orthogonal.gram_schmidt(
        np.random.default_rng(24).normal(size=(6, 4)))) < 1e-12, computed=True)
with checked("M12b.24d"):
    wbm.check("M12b.24d", np.asarray(mymath.orthogonal.gram_schmidt([[-2, 0], [0, -3]])).tolist(), computed=True)
with checked("M12b.24e"):
    wbm.check("M12b.24e", raised(mymath.orthogonal.gram_schmidt, [[1, 2], [2, 4], [3, 6]]), computed=True)
with checked("M12b.24f"):
    wbm.check("M12b.24f", raised(mymath.orthogonal.gram_schmidt, [1, 2, 3]), computed=True)
with checked("M12b.24g"):
    mymath.orthogonal.gram_schmidt(M_24)
    wbm.check("M12b.24g", bool(np.array_equal(M_24, np.array({A_24}, dtype=float))), computed=True)''',
    solution=LOAD_REF + f'''
gram_schmidt = mymath.orthogonal.gram_schmidt
M_24 = np.array({A_24}, dtype=float)
print("a)", np.round(gram_schmidt(M_24), 6).tolist(), " (11 Q =", np.round(11 * gram_schmidt(M_24), 9).tolist(), ")")
print("b)", bool(np.allclose(gram_schmidt(M_24, modified=False), gram_schmidt(M_24), rtol=0, atol=1e-12)),
      " c)", orthogonality_loss(gram_schmidt(np.random.default_rng(24).normal(size=(6, 4)))) < 1e-12)
print("d)", gram_schmidt([[-2, 0], [0, -3]]).tolist(), " e)", raised(gram_schmidt, [[1, 2], [2, 4], [3, 6]]),
      " f)", raised(gram_schmidt, [1, 2, 3]))
gram_schmidt(M_24)
print("g)", bool(np.array_equal(M_24, np.array({A_24}, dtype=float))))''',
    record=f'''Q_24 = np.array([[6, 9], [6, -2], [7, -6]]) / 11
wbm.record("M12b.24a", Q_24.tolist(), decimals=6,
           mistakes={{"normer chaque v_k : divise-le par sa norme": [[6.0, 9 / 11], [6.0, -2 / 11], [7.0, -6 / 11]],
                     "le signe : chaque q_k a un produit scalaire positif avec a_k": (Q_24 * [1, -1]).tolist()}})
wbm.record("M12b.24b", True,
           mistakes={{"sur des colonnes bien séparées, les deux procédés donnent le même résultat (aux arrondis près) : "
                      "relis la ligne qui calcule le coefficient retiré": False}})
wbm.record("M12b.24c", True,
           mistakes={{"chaque q_k doit être de norme 1 et orthogonal aux précédents : relis la projection retirée": False}})
wbm.record("M12b.24d", [[-1.0, 0.0], [0.0, -1.0]], decimals=6,
           mistakes={{"le signe : q_k = v_k / ‖v_k‖ a le sens de a_k ; ne prends pas de valeur absolue": [[1.0, 0.0], [0.0, 1.0]]}})
wbm.record("M12b.24e", "ValueError",
           {value_error("des colonnes dépendantes : la norme de v tombe sous tol × ‖a_k‖, et la docstring demande une ValueError")})
wbm.record("M12b.24f", "ValueError",
           {value_error("un vecteur n'est pas une matrice : la docstring demande une ValueError")})
wbm.record("M12b.24g", True,
           mistakes={{"travaille sur une copie, np.array(A, dtype=float) : np.asarray ne copie pas un tableau de flottants": False}})''',
    after=tests_cells("gram_schmidt"),
    note=r"a) $\mathbf{a}_1 = (6, 6, 7)$ a pour norme 11 ; $\mathbf{a}_2 \cdot \mathbf{q}_1 = \frac{18 + 12 + 14}{11} = 4$, "
         r"$\mathbf{v}_2 = \mathbf{a}_2 - 4\mathbf{q}_1 = \frac{1}{11}(9, -2, -6)$, déjà de norme 1. b) et c) Sur des "
         r"colonnes bien séparées, classique et modifié ne diffèrent que d'arrondis de l'ordre de $10^{-16}$. d) "
         r"$\mathbf{q}_1 = \mathbf{a}_1/\lVert \mathbf{a}_1 \rVert = (-1, 0)$ : la convention $\mathbf{q}_k \cdot \mathbf{a}_k "
         r"> 0$ garde le sens de $\mathbf{a}_k$. e) La deuxième colonne est le double de la première : $\mathbf{v}_2 = "
         r"\mathbf{0}$ (aux arrondis près), sous la tolérance.",
)

M12B_25 = Ex(
    "M12b.25", "🔨", 1, 15, "La projection orthogonale sur un sous-espace · `project`",
    "programmer la projection orthogonale sur l'espace des colonnes d'une matrice, par une base orthonormée.",
    "fiche §5 ; Ex M12b.24", tracks="C, E", mymath="orthogonal.py",
    body=r"""Écris `project(v, A)` (fiche §5), en suivant la docstring : vérifie que $\mathbf{v}$ est à une dimension, $\mathbf{A}$ à deux, et que $\mathbf{A}$ a autant de lignes que $\mathbf{v}$ a de coordonnées (sinon `ValueError`) ; puis $\mathbf{Q}$ = `gram_schmidt(A)` (qui lève elle-même la `ValueError` des colonnes dépendantes), et $\mathbf{p} = \mathbf{Q}(\mathbf{Q}^\top\mathbf{v})$. Pas d'équations normales ici : M09b les a déjà programmées.

La vérification calcule :
- a) `project([2, 0, 1, 5], [[1, 0], [1, 1], [1, 2], [1, 3]])` (une liste, 6 décimales) ;
- b) `project([4, 3], [[1], [3]])` (une liste, 6 décimales) ;
- c) vrai ou faux : pour une matrice $\mathbf{A}$ de forme $(6, 3)$ et un vecteur $\mathbf{v}$ tirés au hasard (`np.random.default_rng(25)`), projeter une seconde fois $\mathbf{p}$ = `project(v, A)` redonne $\mathbf{p}$, à $10^{-12}$ près ;
- d) vrai ou faux : pour les mêmes, $\mathbf{A}^\top(\mathbf{v} - \mathbf{p})$ est nul à $10^{-10}$ près ;
- e) vrai ou faux : `project(v, A @ M)`, avec une matrice $\mathbf{M}$ de forme $(3, 3)$ tirée au hasard (inversible), redonne $\mathbf{p}$ à $10^{-10}$ près ;
- f) le nom de l'erreur levée par `project([1, 2], [[1, 0], [0, 1], [0, 0]])` ;
- g) le nom de l'erreur levée par `project([1, 2, 3], [[1, 2], [1, 2], [1, 2]])`.

Dans ta copie : quelle droite de régression a) calcule-t-il, et que représentent les quatre nombres ? Vérifie b) avec la formule de la projection sur une droite (M07). Pourquoi e) était-il prévisible ?""",
    todo=LOAD_LEARNER,
    check='''rng_25 = np.random.default_rng(25)
A_25, v_25, M_25 = rng_25.normal(size=(6, 3)), rng_25.normal(size=6), rng_25.normal(size=(3, 3))
with checked("M12b.25a"):
    wbm.check("M12b.25a", np.asarray(mymath.orthogonal.project([2, 0, 1, 5], [[1, 0], [1, 1], [1, 2], [1, 3]])).tolist(),
              computed=True)
with checked("M12b.25b"):
    wbm.check("M12b.25b", np.asarray(mymath.orthogonal.project([4, 3], [[1], [3]])).tolist(), computed=True)
with checked("M12b.25c"):
    p_25 = mymath.orthogonal.project(v_25, A_25)
    wbm.check("M12b.25c", bool(np.allclose(mymath.orthogonal.project(p_25, A_25), p_25, rtol=0, atol=1e-12)),
              computed=True)
with checked("M12b.25d"):
    p_25 = mymath.orthogonal.project(v_25, A_25)
    wbm.check("M12b.25d", bool(np.allclose(A_25.T @ (v_25 - p_25), 0, rtol=0, atol=1e-10)), computed=True)
with checked("M12b.25e"):
    p_25 = mymath.orthogonal.project(v_25, A_25)
    wbm.check("M12b.25e", bool(np.allclose(mymath.orthogonal.project(v_25, A_25 @ M_25), p_25, rtol=0, atol=1e-10)),
              computed=True)
with checked("M12b.25f"):
    wbm.check("M12b.25f", raised(mymath.orthogonal.project, [1, 2], [[1, 0], [0, 1], [0, 0]]), computed=True)
with checked("M12b.25g"):
    wbm.check("M12b.25g", raised(mymath.orthogonal.project, [1, 2, 3], [[1, 2], [1, 2], [1, 2]]), computed=True)''',
    solution=LOAD_REF + '''
project = mymath.orthogonal.project
rng_25 = np.random.default_rng(25)
A_25, v_25, M_25 = rng_25.normal(size=(6, 3)), rng_25.normal(size=6), rng_25.normal(size=(3, 3))
p_25 = project(v_25, A_25)
print("a)", np.round(project([2, 0, 1, 5], [[1, 0], [1, 1], [1, 2], [1, 3]]), 6).tolist(),
      " b)", np.round(project([4, 3], [[1], [3]]), 6).tolist())
print("c)", bool(np.allclose(project(p_25, A_25), p_25, rtol=0, atol=1e-12)),
      " d)", bool(np.allclose(A_25.T @ (v_25 - p_25), 0, rtol=0, atol=1e-10)),
      " e)", bool(np.allclose(project(v_25, A_25 @ M_25), p_25, rtol=0, atol=1e-10)))
print("f)", raised(project, [1, 2], [[1, 0], [0, 1], [0, 0]]), " g)", raised(project, [1, 2, 3], [[1, 2], [1, 2], [1, 2]]))''',
    record=f'''A_25a = np.array([[1, 0], [1, 1], [1, 2], [1, 3]], dtype=float)
wbm.record("M12b.25a", [0.5, 1.5, 2.5, 3.5], decimals=6,
           mistakes={{"A Aᵀ v n'est une projection que si les colonnes de A sont orthonormées : Q = gram_schmidt(A), puis Q (Qᵀ v)":
                         (A_25a @ (A_25a.T @ np.array([2.0, 0.0, 1.0, 5.0]))).tolist(),
                     "la projection, pas le résidu v − p": [1.5, -1.5, -1.5, 1.5]}})
wbm.record("M12b.25b", [1.3, 3.9], decimals=6,
           mistakes={{"projeter sur une droite : divise par ‖a‖², ou norme a d'abord": [13.0, 39.0]}})
wbm.record("M12b.25c", True,
           mistakes={{"un vecteur du sous-espace est son propre projeté : relis Q (Qᵀ v), avec Q orthonormée": False}})
wbm.record("M12b.25d", True,
           mistakes={{"le résidu v − p doit être orthogonal aux colonnes de A : Q doit avoir des colonnes orthonormées": False}})
wbm.record("M12b.25e", True,
           mistakes={{"la projection ne dépend que du sous-espace, pas de la base : vérifie que tu projettes sur Vect(colonnes)": False}})
wbm.record("M12b.25f", "ValueError",
           {value_error("v a 2 coordonnées et A a 3 lignes : vérifie les formes, la docstring demande une ValueError")})
wbm.record("M12b.25g", "ValueError",
           {value_error("des colonnes dépendantes : gram_schmidt lève la ValueError, laisse-la passer")})''',
    after=tests_cells("test_project_"),
    note=r"a) Le projeté de $\mathbf{y} = (2, 0, 1, 5)$ sur $\operatorname{Im}\mathbf{X}$, $\mathbf{X} = [\mathbf{1} \mid \mathbf{x}]$ "
         r"et $\mathbf{x} = (0, 1, 2, 3)$ : les prédictions de la droite des moindres carrés $0{,}5 + x$. b) $\frac{4 + 9}{1 + 9}"
         r"(1, 3) = (1{,}3 ;\ 3{,}9)$. e) La projection ne dépend que du sous-espace : $\mathbf{A}\mathbf{M}$, avec $\mathbf{M}$ "
         r"inversible, a le même espace des colonnes que $\mathbf{A}$.",
)

A_26 = "[[12, 6], [3, 2], [4, 0]]"
X_26 = "[[1, 0], [1, 1], [1, 2], [1, 3]]"

M12B_26 = Ex(
    "M12b.26", "🔨", 2, 25, "La décomposition QR et les moindres carrés par QR · `qr, least_squares_qr`",
    "programmer la décomposition QR à partir de Gram-Schmidt, puis les moindres carrés par un système triangulaire.",
    "fiche §7 ; Ex M12b.24", tracks="C", mymath="orthogonal.py",
    body=r"""Écris, en suivant les docstrings :
- `qr(A)` (fiche §7) : $\mathbf{Q}$ = `gram_schmidt(A)` (modifié), puis $\mathbf{R} = \mathbf{Q}^\top\mathbf{A}$, dont tu mets **exactement** à 0 les éléments sous la diagonale (`np.triu`) ; rends le couple `(Q, R)` ;
- `least_squares_qr(X, y)` (fiche §7) : vérifie les formes (`ValueError`), calcule `qr(X)`, le second membre $\mathbf{Q}^\top\mathbf{y}$, puis résous $\mathbf{R}\mathbf{w} = \mathbf{Q}^\top\mathbf{y}$ **en remontant** depuis la dernière ligne : $w_i = \big(z_i - \sum_{j > i} r_{ij}w_j\big)/r_{ii}$. Ni `np.linalg.solve` ni `inv` : la boucle.

La vérification calcule :
- a) la matrice $\mathbf{R}$ de `qr(""" + A_26 + r""")` (6 décimales) ;
- b) vrai ou faux : pour cette matrice, $\mathbf{Q}\mathbf{R}$ redonne $\mathbf{A}$ à $10^{-12}$ près ;
- c) vrai ou faux : pour une matrice de forme $(5, 3)$ tirée au hasard (`np.random.default_rng(26)`), les éléments de $\mathbf{R}$ sous la diagonale sont **exactement** nuls ;
- d) `least_squares_qr(""" + X_26 + r""", [1, 3, 2, 6])` (une liste, 6 décimales) ;
- e) vrai ou faux : pour $\mathbf{X}$ de forme $(30, 4)$ et $\mathbf{y}$ tirés au hasard (`np.random.default_rng(26)`, après la matrice de c), `least_squares_qr(X, y)` et `np.linalg.solve(X.T @ X, X.T @ y)` sont égaux à $10^{-9}$ près ;
- f) le nom de l'erreur levée par `least_squares_qr([[1, 0], [0, 1]], [1, 2, 3])` ;
- g) le nom de l'erreur levée par `qr([[1, 2], [2, 4]])`.

Dans ta copie : retrouve a) à la main (les colonnes de $\mathbf{Q}$ sont des treizièmes). Pour d), écris $\mathbf{R}$ et $\mathbf{Q}^\top\mathbf{y}$, puis résous à la main. Pourquoi c) demande-t-il `np.triu`, alors que $\mathbf{Q}^\top\mathbf{A}$ est « déjà » triangulaire ?""",
    todo=LOAD_LEARNER,
    check=f'''rng_26 = np.random.default_rng(26)
B_26 = rng_26.normal(size=(5, 3))
X_26r, y_26r = rng_26.normal(size=(30, 4)), rng_26.normal(size=30)
with checked("M12b.26a"):
    wbm.check("M12b.26a", np.asarray(mymath.orthogonal.qr({A_26})[1]).tolist(), computed=True)
with checked("M12b.26b"):
    Q_26, R_26 = mymath.orthogonal.qr({A_26})
    wbm.check("M12b.26b", bool(np.allclose(Q_26 @ R_26, {A_26}, rtol=0, atol=1e-12)), computed=True)
with checked("M12b.26c"):
    wbm.check("M12b.26c", bool(np.all(np.tril(mymath.orthogonal.qr(B_26)[1], -1) == 0)), computed=True)
with checked("M12b.26d"):
    wbm.check("M12b.26d", np.asarray(mymath.orthogonal.least_squares_qr({X_26}, [1, 3, 2, 6])).tolist(), computed=True)
with checked("M12b.26e"):
    wbm.check("M12b.26e", bool(np.allclose(mymath.orthogonal.least_squares_qr(X_26r, y_26r),
                                           np.linalg.solve(X_26r.T @ X_26r, X_26r.T @ y_26r), rtol=0, atol=1e-9)),
              computed=True)
with checked("M12b.26f"):
    wbm.check("M12b.26f", raised(mymath.orthogonal.least_squares_qr, [[1, 0], [0, 1]], [1, 2, 3]), computed=True)
with checked("M12b.26g"):
    wbm.check("M12b.26g", raised(mymath.orthogonal.qr, [[1, 2], [2, 4]]), computed=True)''',
    solution=LOAD_REF + f'''
qr, least_squares_qr = mymath.orthogonal.qr, mymath.orthogonal.least_squares_qr
rng_26 = np.random.default_rng(26)
B_26 = rng_26.normal(size=(5, 3))
X_26r, y_26r = rng_26.normal(size=(30, 4)), rng_26.normal(size=30)
Q_26, R_26 = qr({A_26})
print("a)", np.round(R_26, 6).tolist(), " 13 Q =", np.round(13 * Q_26, 9).tolist())
print("b)", bool(np.allclose(Q_26 @ R_26, {A_26}, rtol=0, atol=1e-12)),
      " c)", bool(np.all(np.tril(qr(B_26)[1], -1) == 0)), " (without np.triu:",
      float(np.abs(np.tril(mymath.orthogonal.gram_schmidt(B_26).T @ B_26, -1)).max()), ")")
print("d)", np.round(least_squares_qr({X_26}, [1, 3, 2, 6]), 6).tolist(),
      " e)", bool(np.allclose(least_squares_qr(X_26r, y_26r), np.linalg.solve(X_26r.T @ X_26r, X_26r.T @ y_26r),
                              rtol=0, atol=1e-9)))
print("f)", raised(least_squares_qr, [[1, 0], [0, 1]], [1, 2, 3]), " g)", raised(qr, [[1, 2], [2, 4]]))''',
    record=f'''wbm.record("M12b.26a", [[13.0, 6.0], [0.0, 2.0]], decimals=6,
           mistakes={{"R = QᵀA est triangulaire supérieure : r_jk = q_j · a_k pour j ≤ k": [[13.0, 0.0], [6.0, 2.0]],
                     "le signe : la diagonale de R est positive (r_kk = ‖v_k‖)": [[-13.0, -6.0], [0.0, -2.0]]}})
wbm.record("M12b.26b", True, mistakes={{"Q R doit redonner A : R = QᵀA, avec Q = gram_schmidt(A)": False}})
wbm.record("M12b.26c", True,
           mistakes={{"QᵀA n'a sous sa diagonale que des arrondis, pas des zéros exacts : np.triu les met à 0": False}})
wbm.record("M12b.26d", [0.9, 1.4], decimals=6,
           mistakes={{"R est triangulaire supérieure : remonte depuis la dernière ligne": [3.0, 1.4],
                     "l'ordre : le biais w₀ d'abord, puis la pente": [1.4, 0.9]}})
wbm.record("M12b.26e", True,
           mistakes={{"tes poids doivent résoudre les équations normales : relis Qᵀy et la remontée": False}})
wbm.record("M12b.26f", "ValueError",
           {value_error("X a 2 lignes et y 3 valeurs : vérifie les formes, la docstring demande une ValueError")})
wbm.record("M12b.26g", "ValueError",
           {value_error("des colonnes dépendantes : gram_schmidt lève la ValueError, laisse-la passer")})''',
    after=tests_cells("test_qr_ or test_least_squares_qr_"),
    note=r"a) $\lVert (12, 3, 4) \rVert = 13$, $r_{12} = \frac{72 + 6 + 0}{13} = 6$, $\mathbf{v}_2 = (6, 2, 0) - "
         r"\frac{6}{13}(12, 3, 4) = \frac{2}{13}(3, 4, -12)$, de norme 2. c) Calculé en flottants, $\mathbf{q}_2 \cdot "
         r"\mathbf{a}_1$ vaut un arrondi de l'ordre de $10^{-16}$, pas 0 : `np.triu` impose la forme exacte. d) "
         r"$\mathbf{R} = \begin{pmatrix} 2 & 3 \\ 0 & \sqrt{5} \end{pmatrix}$, $\mathbf{Q}^\top\mathbf{y} = (6, 7/\sqrt{5})$ : "
         r"$w_1 = 7/5 = 1{,}4$, puis $2w_0 + 3 \times 1{,}4 = 6$, $w_0 = 0{,}9$.",
)

A_27 = "[[2, -1, 0], [1, 3, -2], [0, 1, 4], [-3, 2, 1], [1, 0, 2]]"
Y_27 = "[1, 0, 2, -1, 3]"

M12B_27 = Ex(
    "M12b.27", "📦", 1, 15, "`np.linalg.qr` et `lstsq` contre ta projection et ta QR : les signes de Q et de R",
    "utiliser `np.linalg.qr` et `np.linalg.lstsq`, lire ce qu'elles rendent, et comparer avec ta librairie au signe "
    "près.", "fiche §7 ; Ex M12b.26", tracks="C",
    body=r"""En pratique, on ne réécrit pas ces fonctions :
- `np.linalg.qr(A)` rend la décomposition QR réduite `(Q, R)`, calculée par des réflexions de Householder (LAPACK) ; `np.linalg.qr(A, mode="complete")` rend la forme complète. Les signes ne suivent pas la convention $r_{kk} > 0$ ;
- `np.linalg.lstsq(X, y, rcond=None)` rend **quatre** objets : les poids, la somme des carrés des résidus (dans un tableau, vide si le rang n'est pas plein ou s'il y a autant de colonnes que de lignes), le rang de $\mathbf{X}$, et ses valeurs singulières (M12d). Elle passe par la SVD, et accepte des colonnes dépendantes.

Avec $\mathbf{A}$ = `""" + A_27 + r"""` et $\mathbf{y}$ = `""" + Y_27 + r"""`, calcule :
- a) les formes de $\mathbf{Q}$ et de $\mathbf{R}$ rendues par `np.linalg.qr(A)` (une liste de deux formes, `[[.., ..], [.., ..]]`) ;
- b) la forme de $\mathbf{Q}$ avec `mode="complete"` (une liste de 2 entiers) ;
- c) vrai ou faux : les valeurs absolues des $\mathbf{R}$ de NumPy et de ta fonction `qr` sont égales à $10^{-10}$ près ;
- d) vrai ou faux : avec $\mathbf{D}$ = `np.diag(np.sign(np.diag(R_numpy)))`, `Q_numpy @ D` et `D @ R_numpy` sont égales à ton $\mathbf{Q}$ et à ton $\mathbf{R}$, à $10^{-10}$ près ;
- e) le rang rendu par `np.linalg.lstsq(A, y, rcond=None)` ;
- f) vrai ou faux : les poids de `lstsq` et ceux de ta fonction `least_squares_qr(A, y)` sont égaux à $10^{-10}$ près ;
- g) le rang rendu par `lstsq` pour la matrice $\mathbf{A}_4$ = `np.column_stack([A, A[:, 0] + A[:, 1]])` (quatre colonnes) ;
- h) le nom de l'erreur levée par ta fonction `least_squares_qr(A_4, y)`.

Dans ta copie : pourquoi les valeurs absolues de $\mathbf{R}$ sont-elles les mêmes alors que les signes diffèrent ? Que vérifie d) ? Pourquoi `lstsq` accepte-t-elle $\mathbf{A}_4$, et que peut-elle bien rendre, puisqu'une infinité de poids conviennent (M12a §6) ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12b")
A_27 = np.array(''' + A_27 + ''', dtype=float)
y_27 = np.array(''' + Y_27 + ''', dtype=float)
A4_27 = np.column_stack([A_27, A_27[:, 0] + A_27[:, 1]])
answer_M12b_27a = ...  # a) [shape of Q, shape of R]
answer_M12b_27b = ...  # b) a list of 2 integers
answer_M12b_27e = ...  # e) an integer
answer_M12b_27g = ...  # g) an integer
answer_M12b_27c = answer_M12b_27d = answer_M12b_27f = answer_M12b_27h = None
with wbm.attempt("M12b.27c"):        # your qr is called here: ⏳ while it is not written
    answer_M12b_27c = ...  # c) True or False
with wbm.attempt("M12b.27d"):
    answer_M12b_27d = ...  # d) True or False
with wbm.attempt("M12b.27f"):        # your least_squares_qr is called here
    answer_M12b_27f = ...  # f) True or False
with wbm.attempt("M12b.27h"):
    answer_M12b_27h = ...  # h) the name of the error: raised(mymath.orthogonal.least_squares_qr, A4_27, y_27)''',
    check='''for letter, answer in zip("abcdefgh", [answer_M12b_27a, answer_M12b_27b, answer_M12b_27c, answer_M12b_27d,
                                       answer_M12b_27e, answer_M12b_27f, answer_M12b_27g, answer_M12b_27h]):
    wbm.check(f"M12b.27{letter}", answer)''',
    solution='''ref_27 = wbm.load_mymath("ref").orthogonal
A_27 = np.array(''' + A_27 + ''', dtype=float)
y_27 = np.array(''' + Y_27 + ''', dtype=float)
A4_27 = np.column_stack([A_27, A_27[:, 0] + A_27[:, 1]])
Q_np, R_np = np.linalg.qr(A_27)
Q_me, R_me = ref_27.qr(A_27)
D_27 = np.diag(np.sign(np.diag(R_np)))
answer_M12b_27a = [list(Q_np.shape), list(R_np.shape)]
answer_M12b_27b = list(np.linalg.qr(A_27, mode="complete")[0].shape)
answer_M12b_27c = bool(np.allclose(np.abs(R_np), np.abs(R_me), rtol=0, atol=1e-10))
answer_M12b_27d = bool(np.allclose(Q_np @ D_27, Q_me, rtol=0, atol=1e-10) and np.allclose(D_27 @ R_np, R_me, rtol=0, atol=1e-10))
answer_M12b_27e = int(np.linalg.lstsq(A_27, y_27, rcond=None)[2])
answer_M12b_27f = bool(np.allclose(np.linalg.lstsq(A_27, y_27, rcond=None)[0], ref_27.least_squares_qr(A_27, y_27),
                                   rtol=0, atol=1e-10))
answer_M12b_27g = int(np.linalg.lstsq(A4_27, y_27, rcond=None)[2])
answer_M12b_27h = raised(ref_27.least_squares_qr, A4_27, y_27)
print("diag of R by NumPy:", np.round(np.diag(R_np), 4).tolist(), " by gram_schmidt:", np.round(np.diag(R_me), 4).tolist())
print(answer_M12b_27a, answer_M12b_27b, answer_M12b_27c, answer_M12b_27d, answer_M12b_27e, answer_M12b_27f,
      answer_M12b_27g, answer_M12b_27h)''',
    record=f'''wbm.record("M12b.27a", [[5, 3], [3, 3]],
           mistakes={{"la forme réduite par défaut : Q a autant de colonnes que A": [[5, 5], [5, 3]],
                     "Q a la forme de A, R est carrée": [[3, 3], [5, 3]]}})
wbm.record("M12b.27b", [5, 5], mistakes={{"mode=\\"complete\\" : Q devient carrée, de la taille du nombre de lignes": [5, 3]}})
wbm.record("M12b.27c", True,
           mistakes={{"relis ta fonction qr (M12b.26) : ses tests disent ce qui ne va pas": False}})
wbm.record("M12b.27d", True,
           mistakes={{"changer le signe d'une colonne de Q et de la ligne de R correspondante ne change pas QR ; "
                      "relis ta fonction qr si l'égalité échoue": False}})
wbm.record("M12b.27e", 3, mistakes={{"le rang est le nombre de colonnes libres, pas le nombre de lignes": 5}})
wbm.record("M12b.27f", True,
           mistakes={{"relis ta fonction least_squares_qr (M12b.26) : ses tests disent ce qui ne va pas": False}})
wbm.record("M12b.27g", 3, mistakes={{"la quatrième colonne est la somme des deux premières : elle n'ajoute pas de rang": 4}})
wbm.record("M12b.27h", "ValueError",
           {value_error("des colonnes dépendantes : ta fonction doit lever une ValueError (par gram_schmidt)")})''',
    note=r"`np.linalg.qr` travaille par réflexions de Householder : chaque $r_{kk}$ peut sortir négatif, et la colonne $k$ de "
         r"$\mathbf{Q}$ est alors l'opposée de la tienne. $\mathbf{D}$, diagonale de $\pm 1$, vérifie $\mathbf{D}^2 = "
         r"\mathbf{I}$ : $\mathbf{Q}\mathbf{R} = (\mathbf{Q}\mathbf{D})(\mathbf{D}\mathbf{R})$, et $\mathbf{D}\mathbf{R}$ a une "
         r"diagonale positive ; par unicité, c'est ta décomposition. Avec des colonnes dépendantes, `lstsq` rend, parmi "
         r"tous les poids de mêmes prédictions, celui de plus petite norme (M12d).",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M12b.28 to M12b.30)
# ---------------------------------------------------------------------------
M12B_28_GIVEN = '''rng_28 = np.random.default_rng(28)
base_28 = rng_28.normal(size=5)
A_28 = base_28[:, None] + 1e-9 * rng_28.normal(size=(5, 3))     # three columns that differ by about 1e-9
B_28 = rng_28.normal(size=(50, 3))                               # three columns well apart'''

M12B_28_EXPERIMENT = '''Q_classical = mymath.orthogonal.gram_schmidt(A_28, modified=False)
Q_modified = mymath.orthogonal.gram_schmidt(A_28)
print(f"a) classique, colonnes presque colinéaires : écart {orthogonality_loss(Q_classical):.1e}")
print(f"b) modifié, mêmes colonnes                : écart {orthogonality_loss(Q_modified):.1e}")
print(f"c) classique, colonnes bien séparées      : écart "
      f"{orthogonality_loss(mymath.orthogonal.gram_schmidt(B_28, modified=False)):.1e}")
print(f"d) normes des colonnes (classique)        : {np.round(np.linalg.norm(Q_classical, axis=0), 12).tolist()}")
print("   Qᵀ Q (classique) :")
print(np.round(Q_classical.T @ Q_classical, 6))'''

M12B_28 = Ex(
    "M12b.28", "🔮", 1, 10, "Prédire : Gram-Schmidt classique sur des vecteurs presque colinéaires, QᵀQ vaut-il encore I ?",
    "prévoir ce que deviennent l'orthogonalité et les normes calculées par Gram-Schmidt quand les colonnes sont presque "
    "colinéaires, puis le vérifier.", "fiche §3 ; Ex M12b.24", tracks="C, E", hypothesis=True,
    given=M12B_28_GIVEN,
    body=r"""La cellule fournie fabrique $\mathbf{A}$, de forme $(5, 3)$, dont les trois colonnes sont un même vecteur plus des écarts de l'ordre de $10^{-9}$ : libres, mais presque colinéaires. $\mathbf{B}$, de forme $(50, 3)$, a des colonnes tirées au hasard, bien séparées. L'« écart à l'orthogonalité » est le plus grand $|(\mathbf{Q}^\top\mathbf{Q} - \mathbf{I})_{ij}|$ (la fonction `orthogonality_loss` des outils). Pour chaque question, choisis le numéro de la bonne réponse :
- a) l'écart de Gram-Schmidt **classique** sur $\mathbf{A}$ : (1) de l'ordre de $10^{-15}$ ; (2) entre $10^{-12}$ et $10^{-4}$ ; (3) au-dessus de $0{,}1$ ;
- b) l'écart de Gram-Schmidt **modifié** sur $\mathbf{A}$ : mêmes choix ;
- c) l'écart du **classique** sur $\mathbf{B}$ : mêmes choix ;
- d) les normes des colonnes de $\mathbf{Q}$ (classique, sur $\mathbf{A}$) : (1) toutes égales à 1 à $10^{-12}$ près ; (2) certaines loin de 1 ; (3) certaines nulles.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M12b_28a = ...  # a) 1, 2 or 3, written BEFORE running the experiment below
prediction_M12b_28b = ...  # b) 1, 2 or 3
prediction_M12b_28c = ...  # c) 1, 2 or 3
prediction_M12b_28d = ...  # d) 1, 2 or 3''',
    check='''for letter, prediction in zip("abcd", [prediction_M12b_28a, prediction_M12b_28b, prediction_M12b_28c,
                                      prediction_M12b_28d]):
    wbm.check(f"M12b.28{letter}", prediction)''',
    record='''wbm.record("M12b.28a", 3, prediction=True, choices=[1, 2, 3])
wbm.record("M12b.28b", 2, prediction=True, choices=[1, 2, 3])
wbm.record("M12b.28c", 1, prediction=True, choices=[1, 2, 3])
wbm.record("M12b.28d", 1, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience** (avec ta fonction `gram_schmidt`, ou la référence si elle n'est pas encore écrite). Elle "
               "ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12b")\n'
                         + M12B_28_EXPERIMENT, [f"prediction_M12b_28{letter}" for letter in "abcd"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", LOAD_REF + "\n" + M12B_28_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : quel élément de $\\mathbf{Q}^\\top\\mathbf{Q}$ est loin de 0 "
               "avec le procédé classique, et que dit-il des colonnes 2 et 3 de $\\mathbf{Q}$ ? Pourquoi les normes "
               "restent-elles égales à 1 ? En retirant les projections sur $\\mathbf{a}_3$ d'origine, que perd le "
               "procédé classique que le modifié garde ?"),
    ],
    note=r"a) Les colonnes ne diffèrent que de $10^{-9}$ : $\mathbf{v}_2$ et $\mathbf{v}_3$ sont de l'ordre de $10^{-9}$, "
         r"faits de différences de nombres presque égaux, et chacun porte des erreurs d'arrondi de l'ordre de $10^{-16}$, "
         r"énormes à cette échelle. Le procédé classique calcule les coefficients de $\mathbf{a}_3$ avec $\mathbf{q}_2$, "
         r"lui-même déjà faux : $\mathbf{q}_3$ ressort presque parallèle à $\mathbf{q}_2$, et $\mathbf{q}_2 \cdot \mathbf{q}_3$ "
         r"vaut presque $\pm 1$. b) Le modifié retire la projection sur $\mathbf{q}_2$ du vecteur **courant**, ce qui "
         r"corrige au passage l'erreur de la première étape : l'écart reste de l'ordre de $10^{-16}/10^{-9} = 10^{-7}$. "
         r"c) Sur des colonnes bien séparées, $10^{-16}$. d) Chaque $\mathbf{q}_k$ est divisé par sa norme : les normes "
         r"valent 1, et c'est l'orthogonalité qui se perd.",
)

M12B_29_GIVEN = '''X_POINTS_29 = np.linspace(0, 1, 50)
DEGREES_29 = list(range(1, 13))


def polynomial_features(degree):
    """The (50, degree + 1) matrix of the columns 1, x, x², …, x^degree for 50 points x of [0 ; 1]."""
    return np.vander(X_POINTS_29, degree + 1, increasing=True)'''

M12B_29_SHOW = '''classical_t, modified_t, twice_t = loss_table()
print(" d  classique   modifié    classique deux fois")
for d, c, m, t in zip(DEGREES_29, classical_t, modified_t, twice_t):
    print(f"{d:2d}  {c:9.1e}  {m:9.1e}  {t:9.1e}")'''

M12B_29 = Ex(
    "M12b.29", "🔬", 2, 20, "Gram-Schmidt classique contre modifié : l'orthogonalité perdue quand les colonnes sont "
    "presque dépendantes",
    "mesurer comment l'écart à l'orthogonalité des deux procédés grandit quand les colonnes deviennent presque "
    "dépendantes, et voir qu'orthogonaliser deux fois la répare.", "fiche §3, §7 et §8 ; Ex M12b.24 et M12b.28",
    tracks="C", given=M12B_29_GIVEN,
    body=r"""Les features polynomiales $1, x, x^2, \ldots, x^d$, calculées en 50 points de $[0 ; 1]$ (la fonction fournie `polynomial_features(d)`), sont libres, mais de plus en plus **presque dépendantes** quand $d$ grandit : sur $[0 ; 1]$, $x^{10}$ et $x^{11}$ se ressemblent beaucoup (fiche §8). Écris :
- `loss_table()` : pour $d$ dans `DEGREES_29` (de 1 à 12), trois listes de 12 nombres : l'écart à l'orthogonalité (`orthogonality_loss`) de `mymath.orthogonal.gram_schmidt(..., modified=False)`, celle du procédé modifié, et celle du classique appliqué **deux fois** (`gram_schmidt(gram_schmidt(A, modified=False), modified=False)`).

La cellule suivante affiche le tableau. Lis-le, puis réponds :
- a) le plus petit degré $d$ pour lequel l'écart du classique dépasse $10^{-3}$ ;
- b) vrai ou faux : l'écart du modifié reste sous $10^{-6}$ pour tous les degrés du tableau ;
- c) vrai ou faux : l'écart du classique appliqué deux fois reste sous $10^{-12}$ pour tous les $d \le 10$ ;
- d) vrai ou faux : pour $d = 10$, l'écart du classique dépasse $0{,}5$.

Dans ta copie : de combien l'écart du classique est-il multiplié, à peu près, d'un degré au suivant ? Et celui du modifié ? Pourquoi orthogonaliser une seconde fois des colonnes déjà presque orthogonales répare-t-il presque tout ? Pour une régression polynomiale de degré 10, que choisirais-tu : les monômes et les équations normales, ou une autre base (fiche §8) ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12b")


def loss_table():
    """For d in DEGREES_29: the losses of orthogonality of classical, modified and twice-classical Gram-Schmidt."""
    raise NotImplementedError("trois listes : classique, modifié, puis classique appliqué deux fois")''',
    check=f'''with checked("M12b.29 tableau"):
{chr(10).join("    " + line for line in M12B_29_SHOW.splitlines())}''' + '''

answer_M12b_29a = ...  # a) an integer, read in the table above
answer_M12b_29b = ...  # b) True or False
answer_M12b_29c = ...  # c) True or False
answer_M12b_29d = ...  # d) True or False
for letter, answer in zip("abcd", [answer_M12b_29a, answer_M12b_29b, answer_M12b_29c, answer_M12b_29d]):
    wbm.check(f"M12b.29{letter}", answer)''',
    solution=LOAD_REF + '''


def loss_table():
    """For d in DEGREES_29: the losses of orthogonality of classical, modified and twice-classical Gram-Schmidt."""
    gram_schmidt = mymath.orthogonal.gram_schmidt
    classical, modified, twice = [], [], []
    for d in DEGREES_29:
        A = polynomial_features(d)
        classical.append(orthogonality_loss(gram_schmidt(A, modified=False)))
        modified.append(orthogonality_loss(gram_schmidt(A)))
        twice.append(orthogonality_loss(gram_schmidt(gram_schmidt(A, modified=False), modified=False)))
    return classical, modified, twice


''' + M12B_29_SHOW,
    record='''classical_29, modified_29, twice_29 = loss_table()
first_29 = next(d for d, c in zip(DEGREES_29, classical_29) if c > 1e-3)
wbm.record("M12b.29a", first_29,
           mistakes={"le premier degré où l'écart dépasse 1e-3, pas le dernier où il est en dessous": first_29 - 1,
                     "lis la colonne du classique, pas celle du modifié": 13})
wbm.record("M12b.29b", bool(max(modified_29) < 1e-6),
           mistakes={"lis la colonne du modifié, jusqu'au degré 12": not max(modified_29) < 1e-6})
wbm.record("M12b.29c", bool(max(twice_29[:10]) < 1e-12),
           mistakes={"lis la dernière colonne, pour d de 1 à 10": not max(twice_29[:10]) < 1e-12})
wbm.record("M12b.29d", bool(classical_29[9] > 0.5),
           mistakes={"lis la colonne du classique, à la ligne d = 10": not classical_29[9] > 0.5})''',
    note=r"L'écart du classique est multiplié par environ 100 à chaque degré (il suit le carré de la « presque "
         r"dépendance »), celle du modifié par environ 10 : à $d = 9$, le classique a déjà perdu $10^{-2}$, le modifié "
         r"seulement $10^{-11}$. Appliqué une seconde fois à des colonnes presque orthogonales, le classique ne retire que "
         r"de petites projections, calculées avec précision : l'écart retombe à $10^{-15}$ (« deux fois suffit », tant "
         r"que la première passe n'a pas tout perdu). Pour une régression polynomiale de degré 10, on évite les monômes "
         r"et les équations normales : une base de polynômes orthogonaux, ou QR.",
)

M12B_30_GIVEN = '''rng_30 = np.random.default_rng(30)
CLOUD_30 = rng_30.normal(size=(30, 3)) * np.array([2.0, 1.5, 1.0])     # 30 points of ℝ³
PLANE_30 = np.array([[1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])             # its columns span a plane through the origin'''

M12B_30_CHECK = '''with checked("M12b.30 vérifications"):
    problems = []
    ref_30 = wbm.load_mymath("ref").orthogonal
    rng_t = np.random.default_rng(300)
    for X_t, A_t in [(rng_t.normal(size=(6, 3)), np.array([[1.0, 2.0], [0.0, 1.0], [1.0, -1.0]])),
                     (rng_t.normal(size=(4, 3)), np.array([[0.0, 1.0], [2.0, 0.0], [1.0, 1.0]]))]:
        fig_t = plt.figure()
        ax_t = fig_t.add_subplot(projection="3d")
        try:
            created = drawn(lambda: draw_projection(ax_t, X_t, A_t))
            segments = [np.column_stack(line.get_data_3d()).astype(float) for line in ax_t.lines]
        finally:
            plt.close(fig_t)
        if created:
            problems.append("draw_projection ouvre sa propre figure : dessine dans l'axe reçu")
            break
        segments = [s for s in segments if s.shape == (2, 3)]
        expected = [(x, ref_30.project(x, A_t)) for x in X_t]
        missing = [i for i, (x, p) in enumerate(expected)
                   if not any(np.allclose(s, [x, p], atol=1e-9) or np.allclose(s, [p, x], atol=1e-9) for s in segments)]
        if missing:
            problems.append(f"pour {len(X_t)} points, {len(missing)} segment(s) du point à son projeté manque(nt) ou "
                            "sont faux : un segment par point, ax.plot([x[0], p[0]], [x[1], p[1]], [x[2], p[2]])")
            break
    if problems:
        print("❌ Ex M12b.30 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M12b.30 : un segment juste par point, du point à son projeté, sur deux nuages et deux plans.")'''

M12B_30_FIGURE = '''fig = plt.figure(figsize=(7.5, 6.5))
ax = fig.add_subplot(projection="3d")
try:
    draw_projection(ax, CLOUD_30, PLANE_30)
    ax.set(xlabel="x", ylabel="y", zlabel="z", title="Un nuage de ℝ³, ses projetés sur un plan, et les résidus")
    ax.view_init(elev=20, azim=-60)
except BaseException:
    plt.close(fig)
    raise
plt.show()'''

M12B_30 = Ex(
    "M12b.30", "🎨", 1, 20, "Projeter un nuage de ℝ³ sur un plan : les résidus orthogonaux en image",
    "dessiner un nuage de points, ses projetés orthogonaux sur un plan par l'origine et les segments qui les relient, "
    "et voir que ces segments sont tous perpendiculaires au plan.", "fiche §5 ; Ex M12b.25", tracks="C, E",
    given=M12B_30_GIVEN,
    body=r"""Écris `draw_projection(ax, X, A)`, qui trace dans l'axe 3D `ax` (créé par `add_subplot(projection="3d")`), pour un nuage $\mathbf{X}$ de forme $(n, 3)$ (un point par ligne) et une matrice $\mathbf{A}$ de forme $(3, 2)$ dont les colonnes engendrent un plan $U$ :
- les points du nuage (`ax.scatter`) ;
- leurs projetés orthogonaux sur $U$, avec `mymath.orthogonal.project` (ta fonction de M12b.25), dans une autre couleur ;
- pour chaque point $\mathbf{x}$, le **segment** de $\mathbf{x}$ à son projeté $\mathbf{p}$, par un appel `ax.plot([x[0], p[0]], [x[1], p[1]], [x[2], p[2]])` (une ligne de deux points) ;
- un morceau du plan, si tu veux (`plot_surface` sur une grille de combinaisons $s\,\mathbf{a}_1 + t\,\mathbf{a}_2$).

La cellule de la figure s'en sert pour le nuage fourni ; une cellule de vérification essaie ta fonction sur deux autres nuages et deux autres plans, dans des axes neufs.

Dans ta copie : les segments paraissent-ils tous perpendiculaires au plan ? Pourquoi certains semblent-ils ne pas l'être (pense à la perspective, et tourne la figure avec `ax.view_init`) ? Quel point du nuage est le plus loin du plan, et comment le trouver par le calcul ? Remplace $\mathbf{A}$ par une autre base du même plan : que change la figure ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12b")


def draw_projection(ax, X, A):
    """In the 3D axis ax: the points of X (one per row), their projections on the plane spanned by the columns of A,
    and one segment from each point to its projection."""
    raise NotImplementedError("scatter des points, scatter des projetés, puis un ax.plot par segment")''',
    check='''with checked("M12b.30 figure"):
''' + "\n".join("    " + line for line in M12B_30_FIGURE.splitlines()),
    solution=LOAD_REF + '''


def draw_projection(ax, X, A):
    """In the 3D axis ax: the points of X (one per row), their projections on the plane spanned by the columns of A,
    and one segment from each point to its projection."""
    X, A = np.asarray(X, dtype=float), np.asarray(A, dtype=float)
    P = np.array([mymath.orthogonal.project(x, A) for x in X])
    s, t = np.meshgrid(np.linspace(-3, 3, 2), np.linspace(-3, 3, 2))
    ax.plot_surface(s * A[0, 0] + t * A[0, 1], s * A[1, 0] + t * A[1, 1], s * A[2, 0] + t * A[2, 1],
                    alpha=0.15, color="C0")
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], color="C1", s=18, label="points")
    ax.scatter(P[:, 0], P[:, 1], P[:, 2], color="C0", s=18, label="projetés")
    for x, p in zip(X, P):
        ax.plot([x[0], p[0]], [x[1], p[1]], [x[2], p[2]], color="C3", lw=0.9)
    ax.legend(loc="upper left", fontsize=8)


''' + M12B_30_FIGURE,
    after=[("md", "**Vérifications automatiques** (deux autres nuages, deux autres plans, dans des axes neufs)."),
           ("code", M12B_30_CHECK)],
    note=r"Chaque segment $\mathbf{x} - \mathbf{p}$ est orthogonal au plan : sur la figure, ils sont tous parallèles à la "
         r"normale $(1, -1, 1)$ du plan engendré par $(1, 1, 0)$ et $(0, 1, 1)$, ce que la perspective cache sous certains "
         r"angles. Le point le plus loin du plan a le plus grand $|\mathbf{x} \cdot \mathbf{n}|/\lVert \mathbf{n} \rVert$ "
         r"(M07). Changer de base du même plan ne change ni les projetés ni la figure : la projection ne dépend que du "
         r"sous-espace.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M12b.31 to M12b.33)
# ---------------------------------------------------------------------------
M12B_31_MISTAKES = bug_letters_mistakes(
    "ABD", "CEF",
    {"A": "refais chaque ligne à la main, avec ses propres nombres",
     "B": "recalcule ce que fait chaque ligne, puis compare à son commentaire",
     "D": "vérifie chaque résultat sur un petit exemple que tu sais faire à la main"},
    name_correct=False)

M12B_31 = Ex(
    "M12b.31", "🐛", 1, 15, "Chasse à l'erreur : une normalisation oubliée, QQᵀ sur une base non orthonormée, R w = Qᵀy "
    "résolu dans le mauvais sens",
    "repérer dans du code les erreurs classiques de Gram-Schmidt, de projection et de QR, puis calculer les bonnes "
    "valeurs.", "fiche §3, §5 et §7", tracks="C",
    body=r"""Un collègue a écrit le code suivant ; six lignes portent une lettre et un commentaire qui dit ce qu'elles doivent calculer. Trois lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter de code**, trouve-les.

```python
A = np.array([[2.0, 0.0], [1.0, 3.0], [2.0, 3.0]])      # columns a1 = (2, 1, 2), a2 = (0, 3, 3)
q1 = A[:, 0] / np.linalg.norm(A[:, 0])
q2 = A[:, 1] - (A[:, 1] @ q1) * q1           # (A) the second vector of the orthonormal basis: its norm
P = A @ A.T                                  # (B) the matrix of the projection on Vect(a1, a2): P[0, 0]
Q = np.column_stack([q1, q2 / np.linalg.norm(q2)])
v = np.array([3.0, 0.0, 0.0])
r = v - Q @ (Q.T @ v)                        # (C) the residual of v after projection on Vect(a1, a2): r[0]
R = np.triu(Q.T @ A)
y = np.array([3.0, 3.0, 6.0])
z = Q.T @ y
w = np.zeros(2)
for i in range(2):                           # (D) the least squares weights, from R w = Q^T y: w[0]
    w[i] = (z[i] - R[i, :i] @ w[:i]) / R[i, i]
loss = np.abs(Q.T @ Q - np.eye(2)).max()     # (E) the loss of orthogonality of Q: about 0
c = Q.T @ A[:, 1]                            # (F) the coordinates of a2 in the basis (q1, q2): c[1]
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire (une liste de 6 nombres, 4 décimales).

Dans ta copie : pour chaque ligne fausse, quelle erreur a été faite, et comment la corriger ? Laquelle des trois s'exécute sans erreur **et** rend un résultat plausible, et pourquoi est-elle la plus dangereuse ?""",
    todo='''answer_M12b_31a = ...  # a) letters, as text
answer_M12b_31b = ...  # b) a list of 6 values (4 decimals)''',
    check='''wbm.check("M12b.31a", answer_M12b_31a)
wbm.check("M12b.31b", answer_M12b_31b)''',
    solution='''answer_M12b_31a = "ABD"
A = np.array([[2.0, 0.0], [1.0, 3.0], [2.0, 3.0]])
q1 = A[:, 0] / np.linalg.norm(A[:, 0])
v2 = A[:, 1] - (A[:, 1] @ q1) * q1
q2 = v2 / np.linalg.norm(v2)                 # (A) normalize
Q = np.column_stack([q1, q2])
P = Q @ Q.T                                  # (B) Q Qᵀ with the orthonormal basis, not A Aᵀ
v = np.array([3.0, 0.0, 0.0])
r = v - Q @ (Q.T @ v)                        # (C) correct
R = np.triu(Q.T @ A)
y = np.array([3.0, 3.0, 6.0])
z = Q.T @ y
w = np.zeros(2)
for i in reversed(range(2)):                 # (D) back substitution, from the last row
    w[i] = (z[i] - R[i, i + 1:] @ w[i + 1:]) / R[i, i]
loss = np.abs(Q.T @ Q - np.eye(2)).max()     # (E) correct
c = Q.T @ A[:, 1]                            # (F) correct
answer_M12b_31b = [float(np.linalg.norm(q2)), float(P[0, 0]), float(r[0]), float(w[0]), float(loss), float(c[1])]
print(answer_M12b_31a, np.round(answer_M12b_31b, 4).tolist())''',
    record=f'''wbm.record("M12b.31a", "ABD",
           mistakes={M12B_31_MISTAKES})
VALUES_31 = [1.0, 8 / 9, 1 / 3, 5 / 3, 0.0, 3.0]
wbm.record("M12b.31b", VALUES_31, decimals=4,
           mistakes={{"(A) : q₂ doit être normé, sa norme vaut 1": [3.0] + VALUES_31[1:],
                      "(B) : la projection est Q Qᵀ avec une base orthonormée, pas A Aᵀ": VALUES_31[:1] + [4.0] + VALUES_31[2:],
                      "(D) : R est triangulaire supérieure, on remonte depuis la dernière ligne": VALUES_31[:3] + [7 / 3] + VALUES_31[4:]}})''',
    note=r"(A) $\mathbf{a}_2 \cdot \mathbf{q}_1 = 3$ et $\mathbf{v}_2 = (0, 3, 3) - (2, 1, 2) = (-2, 2, 1)$, de norme 3 : il "
         r"faut le diviser par 3. (B) $\mathbf{A}\mathbf{A}^\top$ n'est pas une projection ($\mathbf{a}_1$ et $\mathbf{a}_2$ ne "
         r"sont ni unitaires ni orthogonaux) ; $\mathbf{Q}\mathbf{Q}^\top$ a pour coin $\frac{4}{9} + \frac{4}{9} = \frac{8}{9}$. "
         r"(C) Juste : le résidu de $(3, 0, 0)$ est sa composante sur la normale $\frac{1}{3}(1, 2, -2)$, soit "
         r"$\frac{1}{3}(1, 2, -2)$. (D) La boucle descend et ignore $r_{12}$ : elle donne $w_0 = \frac{7}{3}$ ; en remontant, "
         r"$w_1 = \frac{2}{3}$ puis $w_0 = \frac{7 - 3 \times 2/3}{3} = \frac{5}{3}$. C'est la plus dangereuse : elle "
         r"s'exécute et rend des poids plausibles. (E) Juste : 0 aux arrondis près. (F) Juste : $\mathbf{a}_2 = 3\mathbf{q}_1 "
         r"+ 3\mathbf{q}_2$.",
)

M12B_32_GIVEN = '''def project_oblique(v, A):                      # a copy with a bug: idempotent, but not orthogonal
    A = np.asarray(A, dtype=float)
    B = A + 0.5 * np.cos(np.arange(A.size)).reshape(A.shape)    # another basis, used to "aim" the projection
    return A @ np.linalg.solve(B.T @ A, B.T @ np.asarray(v, dtype=float))


def project_no_gram_schmidt(v, A):              # another bug: A Aᵀ v, without orthonormalizing A
    A = np.asarray(A, dtype=float)
    return A @ (A.T @ np.asarray(v, dtype=float))'''

M12B_32_CHECK = '''with checked("M12b.32 vérifications"):
    problems = []
    ref_32 = wbm.load_mymath("ref").orthogonal

    def outcome(project_t, seed):
        """None if check_projection passes, else the message of its AssertionError."""
        try:
            check_projection(project_t, seed)
        except AssertionError as exc:
            return str(exc)
        return None

    passed = sum(outcome(ref_32.project, seed) is None for seed in range(20))
    caught_oblique = [outcome(project_oblique, seed) for seed in range(20)]
    caught_aat = [outcome(project_no_gram_schmidt, seed) for seed in range(20)]
    print(f"la bonne projection passe ton test {passed} fois sur 20 ; la projection oblique est attrapée "
          f"{sum(m is not None for m in caught_oblique)} fois sur 20 ; A Aᵀ v, "
          f"{sum(m is not None for m in caught_aat)} fois sur 20")
    if passed < 20:
        problems.append("ton test échoue sur la bonne projection : compare avec np.allclose (des flottants), et "
                        "vérifie tes formes")
    if sum(m is not None for m in caught_oblique) < 20:
        problems.append("ton test laisse passer la projection oblique : vérifie aussi la symétrie, ou que le résidu "
                        "est orthogonal aux colonnes")
    if sum(m is not None for m in caught_aat) < 20:
        problems.append("ton test laisse passer A Aᵀ v : vérifie aussi que projeter deux fois ne change rien")
    if not problems and any(not (m or "").strip() for m in caught_oblique + caught_aat):
        problems.append("ajoute un message à chaque assert (assert condition, message)")
    if not problems:
        try:
            test_projection()
        except AssertionError as exc:
            problems.append(f"test_projection échoue sur ta librairie : {exc}")
    if problems:
        print("❌ Ex M12b.32 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M12b.32 : ton test passe sur la bonne projection et attrape les deux copies fausses.")'''

M12B_32 = Ex(
    "M12b.32", "🛠️", 1, 15, "Un test de propriétés pour la projection : idempotente, symétrique, résidu orthogonal",
    "écrire un test fondé sur les propriétés d'une projection orthogonale, vérifiées sur des matrices aléatoires, et "
    "voir quelle propriété attrape quelle erreur.", "fiche §5 ; Ex M12b.25", tracks="C",
    given=M12B_32_GIVEN,
    body=r"""Les tests de `mymath` comparent `project` à une référence. On peut aussi vérifier des **propriétés** que toute projection orthogonale doit avoir (fiche §5). Écris :
- `check_projection(project, seed, trials=10)` : avec `rng = np.random.default_rng(seed)`, répète `trials` fois : tire $m$ entre 2 et 6 (`rng.integers(2, 7)`), $k$ entre 1 et $m - 1$ (`rng.integers(1, m)`), une matrice $\mathbf{A}$ de forme $(m, k)$ et deux vecteurs $\mathbf{u}$, $\mathbf{v}$ de $\mathbb{R}^m$ (loi normale). Avec $\mathbf{p}$ = `project(v, A)`, vérifie par des `assert` (avec un message), à $10^{-9}$ près : (1) **idempotence** : `project(p, A)` redonne $\mathbf{p}$ ; (2) **symétrie** : $\mathbf{P}\mathbf{u} \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{P}\mathbf{v}$ ; (3) **résidu orthogonal** : $\mathbf{A}^\top(\mathbf{v} - \mathbf{p}) = \mathbf{0}$ ;
- `test_projection()` : le test au format pytest, sans argument, qui appelle `check_projection` avec **ta** fonction (`mymath.orthogonal.project`) et une graine fixe.

La cellule fournie définit deux copies fausses : une projection **oblique** (elle envoie bien sur $\operatorname{Im}\mathbf{A}$, mais pas perpendiculairement) et $\mathbf{A}\mathbf{A}^\top\mathbf{v}$ sans Gram-Schmidt. La vérification lance ton test sur la bonne projection (la référence) et sur chaque copie fausse, pour 20 graines.

Dans ta copie : quelles propriétés attrapent la projection oblique, et laquelle la laisse passer ? Même question pour $\mathbf{A}\mathbf{A}^\top\mathbf{v}$. Pourquoi $k$ doit-il rester inférieur à $m$ (que deviendrait la projection oblique pour $k = m$) ? Une fonction fausse pourrait-elle passer les trois propriétés ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12b")


def check_projection(project, seed, trials=10):
    """Assert idempotence, symmetry and an orthogonal residual for `project`, on `trials` random cases."""
    raise NotImplementedError("tire m, k, A, u, v ; trois assert, chacun avec un message")


def test_projection():
    """The pytest test: check_projection on your project, with a fixed seed."""
    raise NotImplementedError("un appel à check_projection")''',
    solution=LOAD_REF + '''


def check_projection(project, seed, trials=10):
    """Assert idempotence, symmetry and an orthogonal residual for `project`, on `trials` random cases."""
    rng = np.random.default_rng(seed)
    for _ in range(trials):
        m = int(rng.integers(2, 7))
        k = int(rng.integers(1, m))
        A = rng.normal(size=(m, k))
        u, v = rng.normal(size=m), rng.normal(size=m)
        p = np.asarray(project(v, A), dtype=float)
        assert np.allclose(project(p, A), p, rtol=0, atol=1e-9), (
            f"expected project(p, A) = p (idempotence) for A of shape {A.shape}, got a gap of "
            f"{np.max(np.abs(np.asarray(project(p, A)) - p)):.1e}")
        left, right = float(np.asarray(project(u, A)) @ v), float(u @ p)
        assert abs(left - right) <= 1e-9 * max(1.0, abs(left)), (
            f"expected P u · v = u · P v (symmetry) for A of shape {A.shape}, got {left:.6f} and {right:.6f}")
        assert np.allclose(A.T @ (v - p), 0, rtol=0, atol=1e-9), (
            f"expected Aᵀ(v − p) = 0 (orthogonal residual) for A of shape {A.shape}, got a largest "
            f"|Aᵀ(v − p)| of {np.max(np.abs(A.T @ (v - p))):.1e}")


def test_projection():
    """The pytest test: check_projection on your project, with a fixed seed."""
    check_projection(mymath.orthogonal.project, seed=32)


test_projection()
print("the three properties hold for the reference")''',
    after=[("code", M12B_32_CHECK)],
    note=r"La projection oblique est idempotente ($\mathbf{P}^2 = \mathbf{P}$) : (1) la laisse passer ; elle n'est pas "
         r"symétrique, et son résidu n'est pas orthogonal aux colonnes : (2) et (3) l'attrapent. $\mathbf{A}\mathbf{A}^\top$ "
         r"est symétrique : (2) la laisse passer ; elle n'est pas idempotente (sauf si $\mathbf{A}$ a des colonnes "
         r"orthonormées), et son résidu n'est pas orthogonal : (1) et (3) l'attrapent. Pour $k = m$, $\operatorname{Im}"
         r"\mathbf{A} = \mathbb{R}^m$ et toute projection sur $\mathbb{R}^m$ est l'identité : la copie oblique serait juste. "
         r"Une matrice symétrique et idempotente est une projection orthogonale ; (3) vérifie en plus que c'est la bonne : "
         r"sur $\operatorname{Im}\mathbf{A}$. Les trois propriétés ensemble caractérisent la projection orthogonale sur "
         r"$\operatorname{Im}\mathbf{A}$ dès que $\mathbf{p} \in \operatorname{Im}\mathbf{A}$, ce qu'un test pourrait vérifier "
         r"aussi.",
)

M12B_33_GIVEN = '''def make_nearly_dependent(seed, n=200, p=6):
    """A (n, p) design matrix whose last column is the one before plus 1e-6 times some noise, and noisy targets."""
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, p))
    X[:, p - 1] = X[:, p - 2] + 1e-6 * rng.normal(size=n)
    w_true = rng.normal(size=p)
    y = X @ w_true + 1e-6 * rng.normal(size=n)
    return X, y'''

M12B_33_CHECK = '''with checked("M12b.33 défi"):
    problems, ok_33 = [], False
    ref_33 = wbm.load_mymath("ref").orthogonal
    for seed_t in (33, 34, 35):
        X_t, y_t = make_nearly_dependent(seed_t)
        w_ref = np.linalg.lstsq(X_t, y_t, rcond=None)[0]
        try:
            w_t = np.asarray(least_squares_stable(X_t.copy(), y_t.copy()), dtype=float)
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"least_squares_stable lève {type(exc).__name__} ({exc})")
            break
        if w_t.shape != w_ref.shape:
            problems.append(f"données {seed_t} : least_squares_stable rend la forme {w_t.shape}, pas {w_ref.shape}")
            break
        gap = float(np.max(np.abs(w_t - w_ref)))
        gap_normal = float(np.max(np.abs(np.linalg.solve(X_t.T @ X_t, X_t.T @ y_t) - w_ref)))
        gap_qr = float(np.max(np.abs(ref_33.least_squares_qr(X_t, y_t) - w_ref)))
        print(f"données {seed_t} : écart à lstsq {gap:.1e} (équations normales {gap_normal:.1e}, "
              f"least_squares_qr {gap_qr:.1e})")
        if not gap <= 1e-8:
            problems.append(f"données {seed_t} : écart {gap:.1e} à lstsq, au-dessus de 1e-8")
            break
    if problems:
        print("❌ Ex M12b.33 : " + " ; ".join(problems) + ".")
    else:
        ok_33 = True
        print("✅ Ex M12b.33 : défi réussi : à moins de 1e-8 de lstsq sur les trois datasets.")
with checked("M12b.33"):
    least_squares_stable(*make_nearly_dependent(33))         # ⏳ while least_squares_stable is not written
    wbm.check("M12b.33", bool(ok_33), computed=True)'''

M12B_33 = Ex(
    "M12b.33", "🏆", 3, 30, "Défi : des colonnes presque dépendantes, des moindres carrés à 1e−8 près de `lstsq` par "
    "l'orthogonalisation de [X | y]",
    "résoudre des moindres carrés aussi précisément qu'une bibliothèque sur des données dont deux colonnes sont presque "
    "dépendantes, là où les équations normales et la QR naïve échouent.",
    "fiche §6 et §7 ; Ex M12b.24, M12b.26 et M12b.29", tracks="C",
    given=M12B_33_GIVEN,
    body=r"""La fonction fournie `make_nearly_dependent(seed)` fabrique un tableau de 200 exemples et 6 features dont les deux dernières ne diffèrent que de $10^{-6}$ fois un bruit, et une cible presque exactement linéaire. Sur ces données, les équations normales et ta fonction `least_squares_qr` (Gram-Schmidt modifié, $\mathbf{R} = \mathbf{Q}^\top\mathbf{X}$, puis $\mathbf{Q}^\top\mathbf{y}$) s'écartent de `np.linalg.lstsq` d'environ $10^{-5}$ à $10^{-3}$ : la vérification l'affiche.

**L'objectif** : écrire `least_squares_stable(X, y)`, qui rend des poids à moins de $10^{-8}$ (le plus grand écart, coordonnée par coordonnée) de ceux de `np.linalg.lstsq` sur les trois datasets `seed` = 33, 34 et 35, **sans** `np.linalg.lstsq`, `qr`, `pinv`, `inv`, `svd`, `cholesky` ni `scipy`. Une dernière cellule enregistre si l'objectif est atteint.

Pistes (Björck, 1967) : applique le procédé **modifié** à la matrice augmentée $[\mathbf{X} \mid \mathbf{y}]$, de forme $(n, p + 1)$, en gardant les coefficients **au moment où tu les retires** : pour la colonne $k$, $r_{jk} = \mathbf{q}_j \cdot \mathbf{v}$ (le vecteur courant) pour $j < k$, puis $r_{kk} = \lVert \mathbf{v} \rVert$. La dernière colonne de ce $\mathbf{R}$ de forme $(p + 1, p + 1)$ contient, au-dessus de la diagonale, le second membre $\mathbf{z}$ ; résous $\mathbf{R}_{[:p, :p]}\,\mathbf{w} = \mathbf{z}_{[:p]}$ en remontant. Ne recalcule ni $\mathbf{R}$ par $\mathbf{Q}^\top\mathbf{X}$ ni $\mathbf{z}$ par $\mathbf{Q}^\top\mathbf{y}$ : c'est là que la QR naïve perd sa précision.

Dans ta copie : pourquoi $\mathbf{R} = \mathbf{Q}^\top\mathbf{X}$, recalculé après coup, est-il moins précis que les coefficients gardés pendant le procédé (pense à M12b.28 : $\mathbf{Q}$ n'est plus tout à fait orthonormée) ? Que représente le dernier élément diagonal de $\mathbf{R}$, $r_{p+1,p+1}$ ? Une autre voie marche-t-elle (pense à M12b.29) ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12b")


def least_squares_stable(X, y):
    """The least squares weights of y on X, within 1e-8 of np.linalg.lstsq even for nearly dependent columns."""
    raise NotImplementedError("Gram-Schmidt modifié sur [X | y], en gardant les coefficients, puis la remontée")''',
    check=M12B_33_CHECK,
    solution=LOAD_REF + '''


def least_squares_stable(X, y):
    """The least squares weights of y on X, within 1e-8 of np.linalg.lstsq even for nearly dependent columns."""
    V = np.column_stack([np.asarray(X, dtype=float), np.asarray(y, dtype=float)])   # a copy: [X | y]
    n, p1 = V.shape
    R = np.zeros((p1, p1))
    for k in range(p1):                          # modified Gram-Schmidt, the coefficients kept as they are removed
        for j in range(k):
            R[j, k] = V[:, j] @ V[:, k]
            V[:, k] -= R[j, k] * V[:, j]
        R[k, k] = np.linalg.norm(V[:, k])
        V[:, k] /= R[k, k]
    p = p1 - 1
    w = np.zeros(p)
    for i in reversed(range(p)):                 # back substitution: R[:p, :p] w = z, z = R[:p, p]
        w[i] = (R[i, p] - R[i, i + 1:p] @ w[i + 1:]) / R[i, i]
    return w


X_33, y_33 = make_nearly_dependent(33)
print("|y − X w| :", float(np.linalg.norm(y_33 - X_33 @ least_squares_stable(X_33, y_33))))''',
    after=[("solution", M12B_33_CHECK.split('with checked("M12b.33"):')[0].rstrip())],
    record='''wbm.record("M12b.33", True,
           mistakes={"l'objectif n'est pas atteint sur les trois datasets : la cellule du défi dit pourquoi": False})''',
    note=r"La QR naïve calcule $\mathbf{Q}$ par le procédé modifié, qui perd un peu d'orthogonalité (de l'ordre de "
         r"$10^{-10}$ ici, M12b.28) ; recalculer $\mathbf{R} = \mathbf{Q}^\top\mathbf{X}$ après coup mélange cet écart au "
         r"petit élément $r_{66} \approx 10^{-5}$, qui mesure la presque dépendance des deux dernières colonnes, et "
         r"l'erreur relative sur $r_{66}$ devient de l'ordre de $10^{-4}$. Les coefficients gardés pendant le procédé, "
         r"eux, vérifient $\mathbf{X} = \mathbf{Q}\mathbf{R}$ aux arrondis près, même quand $\mathbf{Q}$ n'est plus tout à "
         r"fait orthonormée, et traiter $\mathbf{y}$ comme une colonne de plus donne un $\mathbf{z}$ cohérent avec eux : "
         r"c'est le résultat de Björck (1967). $r_{p+1,p+1} = \lVert \mathbf{y} - \mathbf{X}\mathbf{w}^* \rVert$ est la "
         r"norme du résidu. Autre voie : orthogonaliser deux fois (M12b.29), pour un $\mathbf{Q}$ orthonormé à $10^{-16}$ "
         r"près ; alors $\mathbf{Q}^\top\mathbf{X}$ et $\mathbf{Q}^\top\mathbf{y}$ redeviennent précis.",
)

PART_A = Part("A", "Ta librairie : Gram-Schmidt, projection, QR et moindres carrés ; NumPy",
              "Fiche §3, §5 et §7. Les quatre fonctions de `mymath/orthogonal.py`, puis les mêmes calculs avec NumPy.",
              given=TOOLS, exercises=[M12B_24, M12B_25, M12B_26, M12B_27])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §3, §5 et §8. Gram-Schmidt sur des colonnes presque colinéaires, l'écart à l'orthogonalité des deux "
              "procédés, un nuage projeté sur un plan.",
              exercises=[M12B_28, M12B_29, M12B_30])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §3, §5, §6 et §7. Trois erreurs à trouver, un test de propriétés, puis des moindres carrés précis "
              "sur des colonnes presque dépendantes.",
              exercises=[M12B_31, M12B_32, M12B_33])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M12b.1 à M12b.12, M12b.18, M12b.19 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M12b · Orthogonalité et projections — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m12b_orthogonalite/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M12b`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M12b · Orthogonalité et projections — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : produit scalaire défini par une matrice, coordonnées dans "
               "une base orthonormée, matrice orthogonale, Gram-Schmidt (usuel et pondéré), complément orthogonal, "
               "projections et matrice de projection, distance à un sous-espace, moindres carrés et QR, polynômes "
               "orthogonaux, une feature résidualisée, un codage sur deux directions.\n"
               "- Écrire les quatre fonctions de `mymath/orthogonal.py` et les tester, puis comparer avec NumPy.\n"
               "- Prédire et mesurer l'écart à l'orthogonalité, dessiner une projection, chasser des erreurs, tester "
               "des propriétés, résoudre des moindres carrés difficiles.\n\n"
               r"**Rappel express.** Produit scalaire : bilinéaire, symétrique, défini positif ; "
               r"$\langle \mathbf{x}, \mathbf{y} \rangle_{\mathbf{M}} = \mathbf{x}^\top\mathbf{M}\mathbf{y}$ ; base "
               r"orthonormée : $c_i = \langle \mathbf{v}, \mathbf{q}_i \rangle$ ; $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}$, "
               r"$\mathbf{Q}^{-1} = \mathbf{Q}^\top$ ; Gram-Schmidt : $\mathbf{v}_k = \mathbf{a}_k - \sum_{j<k} "
               r"\langle \mathbf{a}_k, \mathbf{q}_j \rangle\,\mathbf{q}_j$, $\mathbf{q}_k = \mathbf{v}_k/\lVert \mathbf{v}_k \rVert$ ; "
               r"$(\operatorname{Im}\mathbf{A})^\perp = \ker\mathbf{A}^\top$ ; projeté : $\mathbf{Q}\mathbf{Q}^\top\mathbf{v}$ ou "
               r"$\mathbf{A}^\top\mathbf{A}\,\mathbf{c} = \mathbf{A}^\top\mathbf{v}$ ; $\mathbf{P}^2 = \mathbf{P} = \mathbf{P}^\top$ ; "
               r"moindres carrés : $\hat{\mathbf{y}}$ = projeté de $\mathbf{y}$ sur $\operatorname{Im}\mathbf{X}$ ; QR : "
               r"$\mathbf{R}\mathbf{w} = \mathbf{Q}^\top\mathbf{y}$, en remontant.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu reconnaître un produit scalaire, et calculer normes et angles avec ?\n"
               "2. Sais-tu lire des coordonnées dans une base orthonormée, et reconnaître une matrice orthogonale ?\n"
               "3. Sais-tu orthonormaliser une famille par Gram-Schmidt ?\n"
               "4. Sais-tu calculer un complément orthogonal, une projection et une distance à un sous-espace ?\n"
               "5. Sais-tu résoudre des moindres carrés par une projection, puis par QR ?\n\n"
               "**La suite** : le chapitre 12 de workbookIA (préparation des données), en parallèle de M12c, "
               "les valeurs propres et les matrices symétriques.")]


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
