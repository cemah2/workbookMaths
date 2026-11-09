#!/usr/bin/env python
"""Build the two notebooks of chapter M12c from a single source (used by Claude).

    python tools/chapters/build_m12c.py
    python tools/run_all_notebooks.py chapitres/m12c_valeurs_propres/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m12c_valeurs_propres/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M12c.1 to M12c.13, 🔗 M12c.20 and M12c.21); parts A to C are the notebook
exercises. Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it. The data
are new: none is a test case of tests/test_m12c_eigen.py, an example of the fiche or of a docstring of eigen.py, data
of M09a, M12a or M12b, or an example of workbookIA 12 (no [[3, 1], [1, 3]], [[4, 5], [5, 7]], [[5, 2], [2, 2]] or
[[1, r], [r, 1]], no points A(1, 1) to E(7, 3), no x² + 100y², no principal axis of a cloud of points).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M12c"
FOLDER = "chapitres/m12c_valeurs_propres"

DESC = "l'ordre décroissant : la plus grande valeur propre d'abord"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M12c.1", "Déterminants 2 × 2 et 3 × 3 : aire, volume et signe", [
        ("a", "a number", "M_1.det()", '''mistakes={"ad − bc : le produit de la diagonale MOINS celui de l'autre diagonale": 10}'''),
        ("b", "a number", "M_1.det() / 2", '''mistakes={"un triangle est la moitié du parallélogramme construit sur deux côtés": 14}'''),
        ("c", "a number (2 decimals)", "float(4 * sympy.pi * abs(M_1.det()))",
         '''decimals=2, mistakes={"l'aire du disque de rayon 2 est π × 2², pas 2π": float(2 * sympy.pi * abs(M_1.det())), '''
         '''"l'image a pour aire celle du disque multipliée par |det M|": float(4 * sympy.pi)}'''),
        ("d", "a number", "N_1.det()",
         '''mistakes={"les signes des cofacteurs alternent : +, −, + sur une ligne": -1}'''),
        ("e", "True or False", "bool(N_1.det() > 0)",
         '''mistakes={"le signe du déterminant dit si l'orientation est conservée": False}'''),
        ("f", "a number", "-N_1.det()", '''mistakes={"échanger deux lignes change le signe du déterminant": 15}'''),
        ("g", "a number", "(2 * N_1).det()",
         '''mistakes={"det(cN) = cⁿ det N : chaque ligne est multipliée par c, et il y a n = 3 lignes": 30, '''
         '''"c est à la puissance n = 3, pas 2": 60}'''),
        ("h", "a number", "sympy.solve(T_1.det(), t)[0]",
         '''mistakes={"développe selon une ligne, signes des cofacteurs compris": -5}'''),
    ]),

    Paper("M12c.2", "Le déterminant d'une matrice 4 × 4 par élimination", [
        ("a", "a matrix", "matrix(F1_2)",
         '''mistakes={"on échange d'abord les lignes 1 et 2, puis on élimine sous le pivot 1": matrix(F_2)}'''),
        ("b", "a list of 4 numbers (1 decimal)", "[float(v) for v in DIAG_2]", "decimals=1"),
        ("c", "a number", "F_2.det()", '''mistakes={"un échange de lignes change le signe du déterminant": 28}'''),
        ("d", "a number (4 decimals)", "float(1 / F_2.det())",
         '''decimals=4, mistakes={"det(F⁻¹) = 1 / det F, signe compris": float(-1 / F_2.det())}'''),
        ("e", "a number", "(F_2.T * F_2).det()",
         '''mistakes={"det(FᵀF) = det(Fᵀ) det(F) = (det F)², jamais négatif": -784}'''),
        ("f", "a number", "G_2.det()",
         '''mistakes={"ajouter à une colonne un multiple d'une autre ne change pas le déterminant": -84}'''),
        ("g", "True or False", "bool(F_2.det() != 0)",
         '''mistakes={"det F ≠ 0 : F est inversible, et ses colonnes forment une base": False}'''),
    ]),

    Paper("M12c.3", "Les valeurs et vecteurs propres d'une matrice 2 × 2", [
        ("a", "a number", "M_3.trace()"),
        ("b", "a number", "M_3.det()", '''mistakes={"ad − bc, pas ad + bc": 8}'''),
        ("c", "a list of 2 numbers", "[7, -4]",
         f'''mistakes={{"{DESC}": [-4, 7], "les racines de λ² − (tr M) λ + det M, signes compris": [4, -7]}}'''),
        ("d", "a list of 2 numbers", "exact(V1_3)",
         '''mistakes={"résous (M − λI) v = 0 pour la plus grande valeur propre, signes compris": [3, -1]}'''),
        ("e", "a list of 2 numbers", "exact(V2_3)",
         '''mistakes={"résous (M − λI) v = 0 pour la plus petite valeur propre, signes compris": [2, 3]}'''),
        ("f", "a list of 2 numbers", "[9, -2]",
         '''mistakes={"ajouter 2I ajoute 2 à chaque valeur propre (les vecteurs propres restent)": [14, -8]}'''),
        ("g", "a list of 2 numbers", "[49, 16]", f'''mistakes={{"{DESC}": [16, 49]}}'''),
        ("h", "True or False", "V1_3.dot(V2_3) == 0",
         '''mistakes={"calcule leur produit scalaire : M n'est pas symétrique": True}'''),
    ]),

    Paper("M12c.4", "Une matrice 3 × 3 triangulaire, puis une avec une valeur propre double", [
        ("a", "a list of 3 numbers", "[4, 2, -1]", f'''mistakes={{"{DESC}": [2, -1, 4]}}'''),
        ("b", "a list of 3 numbers", "exact(VB_4)",
         '''mistakes={"résous (T + I) v = 0, en remontant depuis la dernière ligne, signes compris": [1, 3, 0]}'''),
        ("c", "a list of 3 numbers", "exact(VC_4)",
         '''mistakes={"résous (T − 4I) v = 0, en remontant depuis la dernière ligne, signes compris": [1, -3, 5]}'''),
        ("d", "a number", "T_4.det()", '''mistakes={"le produit de la diagonale, pas sa somme": 5}'''),
        ("e", "a list of 3 numbers", "[5, 3, 3]",
         f'''mistakes={{"{DESC}, la valeur propre double écrite deux fois": [3, 3, 5], '''
         f'''"les valeurs propres de K ne se lisent pas sur sa diagonale : calcule det(K − λI)": [6, 3, 2]}}'''),
        ("f", "an integer", "3 - (K_4 - 3 * sympy.eye(3)).rank()",
         '''mistakes={"dim E₃ = 3 − rang(K − 3I) : compte les lignes indépendantes de K − 3I": 1}'''),
        ("g", "a list of 3 numbers", "exact(VG_4)",
         '''mistakes={"résous (K − 5I) v = 0, signes compris": [-3, 1, 0]}'''),
        ("h", "True or False", "K_4.is_diagonalizable()",
         '''mistakes={"une valeur propre double n'empêche pas d'être diagonalisable : regarde la dimension de son espace propre": False}'''),
    ]),

    Paper("M12c.5", "Diagonaliser, puis calculer une puissance dixième", [
        ("a", "a list of 2 numbers", "[2, 1]", f'''mistakes={{"{DESC}": [1, 2]}}'''),
        ("b", "a list of 2 numbers", "[4, 1]", '''mistakes={"résous (A − 2I) v = 0, signes compris": [-4, 1]}'''),
        ("c", "a list of 2 numbers", "[3, 1]", '''mistakes={"résous (A − I) v = 0, signes compris": [-3, 1]}'''),
        ("d", "a matrix", "matrix(P_5.inv())",
         '''mistakes={"l'inverse d'une matrice 2 × 2 : échange la diagonale et change le signe des deux autres éléments": '''
         '''[[1, 3], [1, 4]], "l'inverse, pas la transposée": matrix(P_5.T)}'''),
        ("e", "a matrix", "matrix(A_5 ** 10)",
         '''mistakes={"A¹⁰ = P D¹⁰ P⁻¹ : élève chaque valeur propre à la puissance 10": matrix(10 * A_5)}'''),
        ("f", "a number", "(A_5 ** 10).det()", '''mistakes={"det(A¹⁰) = (det A)¹⁰": 20}'''),
        ("g", "a number", "(A_5 ** 10).trace()",
         '''mistakes={"la trace de A¹⁰ est la somme des valeurs propres de A¹⁰, pas (tr A)¹⁰": 59049}'''),
        ("h", "a list of 2 numbers (1 decimal)", "[1.0, 0.5]",
         f'''decimals=1, mistakes={{"{DESC}": [0.5, 1.0]}}'''),
    ]),

    Paper("M12c.6", "Une matrice non diagonalisable, et une rotation sans valeur propre réelle", [
        ("a", "a list of 2 numbers", "[2, 2]",
         '''mistakes={"les racines de λ² − (tr N) λ + det N : une racine double": [4, 0]}'''),
        ("b", "an integer", "2 - (N_6 - 2 * sympy.eye(2)).rank()",
         '''mistakes={"dim E₂ = 2 − rang(N − 2I) : la multiplicité géométrique, pas l'algébrique": 2}'''),
        ("c", "a list of 2 numbers", "[3, 1]", '''mistakes={"résous (N − 2I) v = 0, signes compris": [-3, 1]}'''),
        ("d", "True or False", "N_6.is_diagonalizable()",
         '''mistakes={"il faut deux vecteurs propres libres : regarde la question b)": True}'''),
        ("e", "a number", "sympy.simplify(R_6.trace() ** 2 - 4 * R_6.det())",
         '''mistakes={"le discriminant de λ² − (tr R) λ + det R, avec tr R = 2 cos 60°": -1, '''
         '''"(tr R)² − 4 det R, dans cet ordre": 3}'''),
        ("f", "an integer", "0", '''mistakes={"un discriminant négatif : aucune racine réelle": 2}'''),
        ("g", "a number", "sympy.simplify(R_6.det())",
         '''mistakes={"cos² + sin² = 1 : une rotation conserve les aires et l'orientation": -1}'''),
        ("h", "True or False", "sympy.simplify(R_6 ** 6) == sympy.eye(2)",
         '''mistakes={"six rotations de 60° font un tour complet": False}'''),
    ]),

    Paper("M12c.7", "Le théorème spectral sur une matrice symétrique 2 × 2 : Q, Λ et QΛQᵀ", [
        ("a", "a list of 2 numbers", "[30, 1]", f'''mistakes={{"{DESC}": [1, 30]}}'''),
        ("b", "a list of 2 numbers (4 decimals)", "exact(Q1_7)",
         '''decimals=4, mistakes={"un vecteur unitaire : divise le vecteur propre par sa norme": [2.0, 5.0]}'''),
        ("c", "a list of 2 numbers (4 decimals)", "exact(Q2_7)",
         '''decimals=4, mistakes={"le signe : la première coordonnée positive": exact(-Q2_7)}'''),
        ("d", "a number", "Q1_7.dot(Q2_7)", '''mistakes={"le produit scalaire de deux vecteurs propres unitaires": 1}'''),
        ("e", "a matrix (4 decimals)", "[[float(v) for v in row] for row in (30 * Q1_7 * Q1_7.T).tolist()]",
         '''decimals=4, mistakes={"q₁ est unitaire : q₁q₁ᵀ a ses éléments divisés par ‖(2, 5)‖²": '''
         '''[[120.0, 300.0], [300.0, 750.0]]}'''),
        ("f", "a number", "S_7.det()", '''mistakes={"le déterminant est le produit des valeurs propres, pas leur somme": 31}'''),
        ("g", "a list of 2 numbers (4 decimals)", "[1.0, float(sympy.Rational(1, 30))]",
         f'''decimals=4, mistakes={{"les valeurs propres de S⁻¹ sont les inverses 1/λ": [30.0, 1.0], '''
         f'''"{DESC}": [float(sympy.Rational(1, 30)), 1.0]}}'''),
        ("h", "True or False", "True", '''mistakes={"ses deux valeurs propres sont strictement positives": False}'''),
    ]),

    Paper("M12c.8", "Le quotient de Rayleigh : le maximum et le minimum de xᵀAx sur le cercle unité", [
        ("a", "a number", "rq_8([1, 0])"),
        ("b", "a number", "rq_8([0, 1])"),
        ("c", "a number (1 decimal)", "float(rq_8([1, 1]))",
         '''decimals=1, mistakes={"le quotient de Rayleigh divise par xᵀx": float(2 * rq_8([1, 1]))}'''),
        ("d", "a list of 2 numbers", "[18, 1]", f'''mistakes={{"{DESC}": [1, 18]}}'''),
        ("e", "a number", "18",
         '''mistakes={"le maximum est la plus grande valeur propre, pas le plus grand élément de S": 17}'''),
        ("f", "a list of 2 numbers (4 decimals)", "exact(V([4, 1]) / sympy.sqrt(17))",
         '''decimals=4, mistakes={"un vecteur unitaire : divise le vecteur propre par sa norme": [4.0, 1.0]}'''),
        ("g", "an integer", "1",
         '''mistakes={"le minimum est la plus petite valeur propre, pas le plus petit élément de S": 2}'''),
        ("h", "a number (4 decimals)", "float(rq_8([8, 15]))", "decimals=4"),
    ]),

    Paper("M12c.9", "Trois itérations de la méthode de la puissance à la main", [
        ("a", "a list of 2 numbers", "exact(A_9 * V([1, 1]))"),
        ("b", "a list of 2 numbers (4 decimals)", "exact(X_9[0])",
         '''decimals=4, mistakes={"normaliser : divise A x₀ par sa norme": exact(A_9 * V([1, 1]))}'''),
        ("c", "a list of 2 numbers (4 decimals)", "exact(X_9[1])",
         '''decimals=4, mistakes={"le signe : la coordonnée de plus grande valeur absolue doit être positive": exact(-X_9[1])}'''),
        ("d", "a list of 2 numbers (4 decimals)", "exact(X_9[2])",
         '''decimals=4, mistakes={"le signe : la coordonnée de plus grande valeur absolue doit être positive": exact(-X_9[2])}'''),
        ("e", "a number (4 decimals)", "float((X_9[2].T * A_9 * X_9[2])[0])", "decimals=4"),
        ("f", "a list of 2 numbers", "[3, -7]", f'''mistakes={{"{DESC}": [-7, 3]}}'''),
        ("g", "a list of 2 numbers (4 decimals)", "exact(V([-1, 3]) / sympy.sqrt(10))",
         '''decimals=4, mistakes={"la valeur propre de plus grand MODULE, même négative": exact(V([3, 1]) / sympy.sqrt(10)), '''
         '''"la convention de signe : la coordonnée de plus grande valeur absolue positive": exact(V([1, -3]) / sympy.sqrt(10))}'''),
        ("h", "a number (4 decimals)", "float(sympy.Rational(3, 7))",
         '''decimals=4, mistakes={"|λ₂ / λ₁|, avec λ₁ la valeur propre de plus grand module": float(sympy.Rational(7, 3))}'''),
    ]),

    Paper("M12c.10", "Définie positive ? Par les valeurs propres, les mineurs et la forme quadratique ; une hessienne qui "
                     "prouve la convexité", [
        ("a", "a list of 3 numbers", "[H1_10[:k, :k].det() for k in (1, 2, 3)]"),
        ("b", "True or False", "True", '''mistakes={"trois mineurs principaux strictement positifs": False}'''),
        ("c", "a list of 3 numbers", "[H2_10[:k, :k].det() for k in (1, 2, 3)]"),
        ("d", "a number", "(V([2, -1, 0]).T * H2_10 * V([2, -1, 0]))[0]",
         '''mistakes={"xᵀHx compte deux fois chaque terme hors de la diagonale": 3}'''),
        ("e", "a matrix", "matrix(HF_10.subs({x: 0, y: 0}))",
         '''mistakes={"la dérivée seconde de eˣ est eˣ, qui vaut 1 en x = 0": [[2, 2], [2, 6]], '''
         '''"le terme 2xy donne 2 hors de la diagonale de la hessienne": [[3, 1], [1, 6]]}'''),
        ("f", "a number (4 decimals)", "float(HF_10.subs({x: 1, y: 0}).det())", "decimals=4"),
        ("g", "True or False", "True",
         '''mistakes={"la hessienne est définie positive en tout point : écris ses mineurs en (x, y)": False}'''),
        ("h", "a list of 2 numbers", "[7, 2]", f'''mistakes={{"{DESC}": [2, 7]}}'''),
    ]),

    Paper("M12c.11", "La décomposition de Cholesky d'une matrice 3 × 3", [
        ("a", "a number", "L_11[0, 0]", '''mistakes={"l₁₁ = √a₁₁, la racine": 4}'''),
        ("b", "a list of 2 numbers", "[L_11[1, 0], L_11[2, 0]]",
         '''mistakes={"lᵢ₁ = aᵢ₁ / l₁₁ : divise par l₁₁": [-6, 2]}'''),
        ("c", "a number", "L_11[1, 1]", '''mistakes={"l₂₂ = √(a₂₂ − l₂₁²), avec l₂₁ au carré": 4}'''),
        ("d", "a number", "L_11[2, 1]", '''mistakes={"l₃₂ = (a₃₂ − l₃₁ l₂₁) / l₂₂, signes compris": -2}'''),
        ("e", "a number", "L_11[2, 2]", '''mistakes={"l₃₃ est une racine carrée": 4}'''),
        ("f", "a matrix", "matrix(L_11)",
         '''mistakes={"L est triangulaire inférieure : les zéros au-dessus de la diagonale": matrix(L_11.T)}'''),
        ("g", "a number", "A_11.det()", '''mistakes={"det A = (det L)² = (l₁₁ l₂₂ l₃₃)²": 4}'''),
        ("h", "a list of 3 numbers", "exact(A_11.solve(V([2, -7, -19])))"),
    ]),

    Paper("M12c.12", "Une forme quadratique réduite à une somme de carrés, et ses lignes de niveau", [
        ("a", "a matrix", "matrix(S_12)",
         '''mistakes={"le terme croisé 10xy se partage en deux moitiés égales, de part et d'autre de la diagonale": '''
         '''[[2, 10], [10, 26]]}'''),
        ("b", "a list of 2 numbers", "[27, 1]", f'''mistakes={{"{DESC}": [1, 27]}}'''),
        ("c", "a list of 2 numbers (4 decimals)", "exact(V([1, 5]) / sympy.sqrt(26))",
         '''decimals=4, mistakes={"un vecteur unitaire : divise le vecteur propre par sa norme": [1.0, 5.0]}'''),
        ("d", "a number", "(V([5, -1]).T * S_12 * V([5, -1]))[0]"),
        ("e", "a list of 2 numbers (4 decimals)", "[float(sympy.sqrt(27)), 1.0]",
         '''decimals=4, mistakes={"le demi-axe le long de qᵢ vaut √(27 / λᵢ), une racine": [27.0, 1.0], '''
         '''"du plus grand au plus petit": [1.0, float(sympy.sqrt(27))]}'''),
        ("f", "a number (2 decimals)", "float(sympy.pi * sympy.sqrt(27))",
         '''decimals=2, mistakes={"π a b avec les demi-axes, pas leurs carrés": float(27 * sympy.pi)}'''),
        ("g", "a number (2 decimals)", "float(sympy.sqrt(4 * 2 * 26))",
         '''decimals=2, mistakes={"la forme a pour matrice [[2, c/2], [c/2, 26]] : son déterminant s'annule pour c² = 4 × 2 × 26": '''
         '''float(sympy.sqrt(2 * 26))}'''),
        ("h", "True or False", "True",
         '''mistakes={"une forme définie positive ne s'annule qu'en 0": False}'''),
    ]),

    Paper("M12c.13", "La covariance d'un vecteur transformé, AΣAᵀ, et le blanchiment d'une covariance 2 × 2", [
        ("a", "a number", "(V([1, 1]).T * S_13 * V([1, 1]))[0]",
         '''mistakes={"V(x₁ + x₂) = V(x₁) + V(x₂) + 2 Cov(x₁, x₂)": 97, "Cov(x₁, x₂) = −30 est négative": 157}'''),
        ("b", "a matrix", "matrix(A_13 * S_13 * A_13.T)",
         '''mistakes={"V(x₁ − 2x₂) = V(x₁) + 4 V(x₂) − 4 Cov(x₁, x₂) : n'oublie pas la covariance": [[37, -56], [-56, 280]]}'''),
        ("c", "a matrix", "matrix(L_13)",
         '''mistakes={"L est triangulaire inférieure, à diagonale positive": matrix(L_13.T)}'''),
        ("d", "a matrix (4 decimals)", "[[float(v) for v in row] for row in L_13.inv().tolist()]",
         '''decimals=4, mistakes={"l'inverse d'une triangulaire inférieure : le signe de l'élément sous la diagonale": '''
         '''[[1 / 6, 0.0], [-5 / 36, 1 / 6]]}'''),
        ("e", "a list of 2 numbers", "[81, 16]", f'''mistakes={{"{DESC}": [16, 81]}}'''),
        ("f", "a matrix (4 decimals)", "[[float(v) for v in row] for row in HALF_13.tolist()]", "decimals=4"),
        ("g", "a matrix (4 decimals)", "[[float(v) for v in row] for row in ZCA_13.tolist()]",
         '''decimals=4, mistakes={"Σ^(−1/2) = Q Λ^(−1/2) Qᵀ : 1/√λ, pas √λ": '''
         '''[[float(v) for v in row] for row in HALF_13.tolist()]}'''),
        ("h", "a list of 2 numbers (4 decimals)", "exact(L_13.inv() * V([12, 0]))",
         '''decimals=4, mistakes={"z = L⁻¹(x − μ), pas L(x − μ)": exact(L_13 * V([12, 0]))}'''),
    ]),

    Paper("M12c.20", "Pont : la variance d'une somme pondérée de trois features, wᵀΣw, et pourquoi Σ doit être "
                     "semi-définie positive", [
        ("a", "a number", "S_20.trace()", '''mistakes={"la variance totale est la somme des variances, la trace": 37}'''),
        ("b", "a number", "qf(S_20, [1, 1, 1])",
         '''mistakes={"V(x₁ + x₂ + x₃) compte aussi deux fois chaque covariance": 29}'''),
        ("c", "a number", "qf(S_20, [2, -1, 0])",
         '''mistakes={"V(2x₁ − x₂) = 4 V(x₁) + V(x₂) − 4 Cov(x₁, x₂)": 25, "un facteur 2 au carré : 4 V(x₁)": 9}'''),
        ("d", "a number", "qf(S_20, [1, -1, 2])"),
        ("e", "a number", "S_20[0, 2] + S_20[1, 2]",
         '''mistakes={"Cov(x₁ + x₂, x₃) = Cov(x₁, x₃) + Cov(x₂, x₃)": 4}'''),
        ("f", "a number", "qf(PHI_20, [1, -1, 0])"),
        ("g", "True or False", "False",
         '''mistakes={"une variance n'est jamais négative : regarde la question f)": True}'''),
        ("h", "a number (4 decimals)", "float(S_20[0, 1] / sympy.sqrt(S_20[0, 0] * S_20[1, 1]))",
         '''decimals=4, mistakes={"divise par le produit des écarts-types, pas des variances": float(S_20[0, 1] / (S_20[0, 0] * S_20[1, 1]))}'''),
    ]),

    Paper("M12c.21", "Pont : après un blanchiment, la covariance est l'identité", [
        ("a", "a matrix", "matrix(L_21)", '''mistakes={"L est triangulaire inférieure": matrix(L_21.T)}'''),
        ("b", "a matrix (4 decimals)", "[[float(v) for v in row] for row in W_21.tolist()]",
         '''decimals=4, mistakes={"l'inverse d'une triangulaire inférieure : le signe de l'élément sous la diagonale": '''
         '''[[1 / 3, 0.0], [1 / 3, 0.5]]}'''),
        ("c", "a matrix", "matrix(W_21 * S_21 * W_21.T)"),
        ("d", "a list of 2 numbers (1 decimal)", "exact(W_21 * V([6, 1]))",
         '''decimals=1, mistakes={"z = W(x − μ), avec W = L⁻¹": exact(L_21 * V([6, 1]))}'''),
        ("e", "a number (1 decimal)", "float((W_21 * V([6, 1])).norm())",
         '''decimals=1, mistakes={"la norme, pas son carré": float((W_21 * V([6, 1])).norm() ** 2)}'''),
        ("f", "a matrix", "matrix(R_21 * R_21.T)",
         '''mistakes={"cov(R z) = R I Rᵀ = R Rᵀ, et R est orthogonale": [[0, -1], [1, 0]]}'''),
        ("g", "True or False", "True",
         '''mistakes={"(RW) Σ (RW)ᵀ = R (W Σ Wᵀ) Rᵀ = R Rᵀ : vérifie-le": False}'''),
        ("h", "True or False", "False",
         '''mistakes={"‖W d‖² = dᵀ (WᵀW) d, et WᵀW = Σ⁻¹ pour tout blanchiment": True}'''),
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


def qf(M, w):
    """The quadratic form wᵀ M w."""
    w = sympy.Matrix(w)
    return (w.T * M * w)[0]


V = sympy.Matrix
t, x, y = sympy.symbols("t x y")
M_1 = V([[3, -1], [2, 4]])                                                                  # M12c.1
N_1 = V([[1, 2, -1], [0, 3, 2], [2, 1, 1]])
T_1 = V([[t, 2, 1], [1, 1, 0], [3, 0, 1]])
F_2 = V([[0, 2, 1, 3], [1, 1, 0, 2], [2, 4, 3, 1], [-1, 0, 2, 2]])                           # M12c.2
F1_2 = V([[1, 1, 0, 2], [0, 2, 1, 3], [0, 2, 3, -3], [0, 1, 2, 4]])
DIAG_2 = [1, 2, 2, 7]
assert F1_2.det() == -F_2.det() and DIAG_2[0] * DIAG_2[1] * DIAG_2[2] * DIAG_2[3] == -F_2.det()
G_2 = F_2.copy()
G_2[:, 3] = G_2[:, 3] + 3 * G_2[:, 0]
M_3 = V([[5, 6], [3, -2]])                                                                  # M12c.3
V1_3, V2_3 = V([3, 1]), V([2, -3])
assert M_3 * V1_3 == 7 * V1_3 and M_3 * V2_3 == -4 * V2_3
T_4 = V([[2, 1, -1], [0, -1, 3], [0, 0, 4]])                                                # M12c.4
K_4 = V([[6, -3, 3], [1, 2, 1], [0, 0, 3]])
VB_4, VC_4, VG_4 = V([1, -3, 0]), V([-1, 3, 5]), V([3, 1, 0])
assert T_4 * VB_4 == -VB_4 and T_4 * VC_4 == 4 * VC_4 and K_4 * VG_4 == 5 * VG_4
A_5, P_5 = V([[5, -12], [1, -2]]), V([[4, 3], [1, 1]])                                       # M12c.5
assert A_5 * P_5 == P_5 * sympy.diag(2, 1)
N_6 = V([[5, -9], [1, -1]])                                                                 # M12c.6
R_6 = V([[sympy.cos(sympy.pi / 3), -sympy.sin(sympy.pi / 3)], [sympy.sin(sympy.pi / 3), sympy.cos(sympy.pi / 3)]])
S_7 = V([[5, 10], [10, 26]])                                                                # M12c.7
Q1_7, Q2_7 = V([2, 5]) / sympy.sqrt(29), V([5, -2]) / sympy.sqrt(29)
assert S_7 * V([2, 5]) == 30 * V([2, 5]) and S_7 * V([5, -2]) == V([5, -2])
S_8 = V([[17, 4], [4, 2]])                                                                  # M12c.8


def rq_8(v):
    v = V(v)
    return (v.T * S_8 * v)[0] / (v.T * v)[0]


A_9 = V([[2, 3], [3, -6]])                                                                  # M12c.9
X_9, _x = [], V([1, 1])
for _ in range(3):
    _y = A_9 * _x
    _i = max(range(2), key=lambda j: abs(_y[j]))
    _x = _y if _y[_i] > 0 else -_y
    X_9.append(_x / _x.norm())
H1_10 = V([[4, -2, 0], [-2, 3, 1], [0, 1, 2]])                                              # M12c.10
H2_10 = V([[1, 2, 0], [2, 3, 1], [0, 1, 4]])
HF_10 = sympy.hessian(x ** 2 + 2 * x * y + 3 * y ** 2 + sympy.exp(x), (x, y))
A_11 = V([[4, -6, 2], [-6, 10, 1], [2, 1, 21]])                                             # M12c.11
L_11 = A_11.cholesky()
S_12 = V([[2, 5], [5, 26]])                                                                 # M12c.12
S_13, A_13 = V([[36, -30], [-30, 61]]), V([[1, 1], [1, -2]])                                 # M12c.13
L_13 = S_13.cholesky()
Q_13 = V([[2, 3], [-3, 2]]) / sympy.sqrt(13)
HALF_13 = sympy.simplify(Q_13 * sympy.diag(9, 4) * Q_13.T)
ZCA_13 = sympy.simplify(Q_13 * sympy.diag(sympy.Rational(1, 9), sympy.Rational(1, 4)) * Q_13.T)
assert HALF_13 ** 2 == S_13 and sympy.simplify(ZCA_13 * S_13 * ZCA_13) == sympy.eye(2)
S_20 = V([[4, 2, -1], [2, 9, 3], [-1, 3, 16]])                                              # M12c.20
PHI_20 = V([[2, 3, 1], [3, 2, 0], [1, 0, 2]])
S_21 = V([[9, 6], [6, 8]])                                                                  # M12c.21
L_21 = S_21.cholesky()
W_21 = L_21.inv()
R_21 = V([[0, -1], [1, 0]])'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M12c.1 à M12c.13, 🔗 M12c.20 et M12c.21)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une liste `[0, -2, 5]` pour un vecteur (les valeurs propres par ordre décroissant), une liste de "
               "lignes `[[1, 0], [-2, 3]]` pour une matrice, ou `True` / `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M12c.26 to M12c.30)
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


def random_spd(n, seed, shift=0.5):
    """A random symmetric positive definite (n, n) matrix, drawn with default_rng(seed)."""
    X = np.random.default_rng(seed).normal(size=(n + 3, n))
    return X.T @ X / (n + 3) + shift * np.eye(n)'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12c")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/eigen.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "NumPy est permis, `@`, `.T`, `np.linalg.norm` et `np.linalg.solve` compris ; `np.linalg.det`, `slogdet`, "
         "`eig`, `eigvals`, `cholesky`, `inv`, `scipy.linalg` et SymPy sont interdits (les tests comparent tes "
         "résultats aux leurs, et un test vérifie que tu ne t'en sers pas), et `np.linalg.eigh` n'est permis que "
         "dans `sqrtm_psd` et `whitening_matrix`. Ne modifie jamais la matrice reçue : travaille sur une copie, "
         "`np.array(A, dtype=float)`. Les nombres se rendent en `float` de Python, les tests en `bool`.")

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
    """The cells that run the tests of eigen.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_eigen_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m12c_eigen.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m12c_eigen.py", "{keyword}", impl="ref")')]


A_26 = "[[1, 3, 2], [-2, 0, 4], [3, 1, -1]]"
B_26 = "[[0, 2, 1], [3, -1, 2], [1, 1, 0]]"
Z_26 = "[[1, 2, 3], [2, 4, 6], [1, 0, 1]]"

M12C_26 = Ex(
    "M12c.26", "🔨", 1, 20, "Le déterminant par élimination · `det`",
    "programmer le déterminant par élimination avec pivot partiel, en suivant le signe des échanges.",
    "fiche §1", tracks="C, E", mymath="eigen.py",
    body=HOWTO + r"""

Écris `det(A)` (fiche §1), en suivant la docstring : une copie en flottants, une `ValueError` si $\mathbf{A}$ n'est pas carrée, un signe qui vaut 1 au départ ; puis, pour chaque colonne $k$ : chercher, de la ligne $k$ à la dernière, l'élément de **plus grande valeur absolue** (`np.argmax(np.abs(...))`) ; s'il est nul, rendre `0.0` aussitôt ; sinon remonter sa ligne en position $k$ (et changer le signe si c'est un vrai échange), puis retirer aux lignes du dessous le bon multiple de la ligne $k$. Le déterminant est le signe fois le produit de la diagonale, en `float` de Python.

La vérification calcule :
- a) `det(""" + A_26 + r""")` (6 décimales) ;
- b) `det(""" + B_26 + r""")` (6 décimales) ;
- c) vrai ou faux : pour une matrice $6 \times 6$ tirée au hasard (`np.random.default_rng(26)`, loi normale), `det` et `np.linalg.det` sont égaux à $10^{-10}$ près, relativement ;
- d) vrai ou faux : `d = det(""" + Z_26 + r""")` vérifie `type(d) is float and d == 0 and math.copysign(1.0, d) > 0` (un `float` de Python, égal à 0, et positif : pas `-0.0`) ;
- e) vrai ou faux : pour deux matrices $4 \times 4$ tirées au hasard (même générateur, après celle de c)), $\det(\mathbf{A}\mathbf{B}) = \det\mathbf{A}\,\det\mathbf{B}$ à $10^{-10}$ près, relativement ;
- f) le nom de l'erreur levée par `det([[1, 2, 3], [4, 5, 6]])` ;
- g) vrai ou faux : après `det(M)`, le tableau `M` (une copie en flottants de la matrice de b)) n'a pas changé.

Dans ta copie : retrouve a) et b) à la main. Pour b), quelle ligne est remontée en premier, et combien d'échanges y a-t-il ? Que rend `repr(det(...))` pour la matrice de d), et pourquoi ne doit-il afficher ni `-0.0` ni `np.float64(0.0)` ?""",
    todo=LOAD_LEARNER,
    check=f'''rng_26 = np.random.default_rng(26)
C_26 = rng_26.normal(size=(6, 6))
D_26, E_26 = rng_26.normal(size=(4, 4)), rng_26.normal(size=(4, 4))
with checked("M12c.26a"):
    wbm.check("M12c.26a", mymath.eigen.det({A_26}), computed=True)
with checked("M12c.26b"):
    wbm.check("M12c.26b", mymath.eigen.det({B_26}), computed=True)
with checked("M12c.26c"):
    wbm.check("M12c.26c", bool(abs(mymath.eigen.det(C_26) - np.linalg.det(C_26)) <= 1e-10 * max(1.0, abs(np.linalg.det(C_26)))),
              computed=True)
with checked("M12c.26d"):
    d_26 = mymath.eigen.det({Z_26})
    wbm.check("M12c.26d", bool(type(d_26) is float and d_26 == 0 and math.copysign(1.0, d_26) > 0), computed=True)
with checked("M12c.26e"):
    d_ab = mymath.eigen.det(D_26 @ E_26)
    wbm.check("M12c.26e", bool(abs(d_ab - mymath.eigen.det(D_26) * mymath.eigen.det(E_26)) <= 1e-10 * max(1.0, abs(d_ab))),
              computed=True)
with checked("M12c.26f"):
    wbm.check("M12c.26f", raised(mymath.eigen.det, [[1, 2, 3], [4, 5, 6]]), computed=True)
with checked("M12c.26g"):
    M_26 = np.array({B_26}, dtype=float)
    mymath.eigen.det(M_26)
    wbm.check("M12c.26g", bool(np.array_equal(M_26, np.array({B_26}, dtype=float))), computed=True)''',
    solution=LOAD_REF + f'''
det = mymath.eigen.det
rng_26 = np.random.default_rng(26)
C_26 = rng_26.normal(size=(6, 6))
D_26, E_26 = rng_26.normal(size=(4, 4)), rng_26.normal(size=(4, 4))
print("a)", round(det({A_26}), 6), " b)", round(det({B_26}), 6),
      " c)", bool(abs(det(C_26) - np.linalg.det(C_26)) <= 1e-10 * max(1.0, abs(np.linalg.det(C_26)))))
d_26 = det({Z_26})
print("d)", bool(type(d_26) is float and d_26 == 0 and math.copysign(1.0, d_26) > 0), repr(d_26), " e)", bool(abs(det(D_26 @ E_26) - det(D_26) * det(E_26)) <= 1e-10 * max(1.0, abs(det(D_26 @ E_26)))))
M_26 = np.array({B_26}, dtype=float)
det(M_26)
print("f)", raised(det, [[1, 2, 3], [4, 5, 6]]), " g)", bool(np.array_equal(M_26, np.array({B_26}, dtype=float))))''',
    record=f'''wbm.record("M12c.26a", 22.0, decimals=6,
           mistakes={{"le signe : chaque échange de lignes change le signe du déterminant": -22.0}})
wbm.record("M12c.26b", 8.0, decimals=6,
           mistakes={{"le signe : chaque échange de lignes change le signe du déterminant": -8.0}})
wbm.record("M12c.26c", True,
           mistakes={{"compare ton résultat avec np.linalg.det sur une petite matrice que tu sais faire à la main : le "
                      "signe des échanges et le multiple retiré à chaque ligne": False}})
wbm.record("M12c.26d", True,
           mistakes={{"rends 0.0 dès qu'une colonne n'a pas de pivot non nul (jamais -0.0), en float de Python : "
                      "affiche repr(det(...)) pour voir ce que tu rends": False}})
wbm.record("M12c.26e", True,
           mistakes={{"det(AB) = det A det B pour toutes les matrices : compare ton det à np.linalg.det": False}})
wbm.record("M12c.26f", "ValueError",
           {value_error("une matrice (2, 3) n'est pas carrée : la docstring demande une ValueError")})
wbm.record("M12c.26g", True,
           mistakes={{"travaille sur une copie : np.array(A, dtype=float), pas np.asarray(A)": False}})''',
    after=tests_cells("test_det_"),
    note=r"a) $L_2 \leftarrow L_2 + 2L_1$ et $L_3 \leftarrow L_3 - 3L_1$ (sans pivot partiel) donnent $(0, 6, 8)$ et "
         r"$(0, -8, -7)$, puis $-7 + \frac{8 \times 8}{6} = \frac{11}{3}$ : $1 \times 6 \times \frac{11}{3} = 22$. b) Le pivot "
         r"partiel remonte la ligne $(3, -1, 2)$ : un échange. d) Une colonne sans pivot non nul donne un déterminant nul, "
         r"rendu tel quel : un $-0{,}0$ viendrait du signe des échanges multiplié par un produit nul.",
)

S_27 = "[[4, 1, 0], [1, 3, 1], [0, 1, 2]]"

M12C_27 = Ex(
    "M12c.27", "🔨", 2, 25, "La méthode de la puissance et le quotient de Rayleigh · `power_iteration, rayleigh_quotient`",
    "programmer la méthode de la puissance, avec sa normalisation, sa convention de signe et son critère d'arrêt, et le "
    "quotient de Rayleigh.", "fiche §5 et §6 ; Ex M12c.26", tracks="C, E", mymath="eigen.py",
    body=r"""Écris, en suivant les docstrings :
- `rayleigh_quotient(A, x)` (fiche §6) : vérifie les formes et que $\mathbf{x} \ne \mathbf{0}$ (sinon `ValueError`), puis $\mathbf{x}^\top\mathbf{A}\mathbf{x}/\mathbf{x}^\top\mathbf{x}$ ;
- `power_iteration(A, x0=None, n_iter=1000, tol=1e-12)` (fiche §5) : $\mathbf{x}_0$ (des 1 par défaut) normalisé, avec la convention de signe (la coordonnée de plus grande valeur absolue positive) ; puis, au plus `n_iter` fois : $\mathbf{y} = \mathbf{A}\mathbf{x}$ (`ValueError` s'il est nul), $\mathbf{x}_{\text{new}} = \mathbf{y}/\lVert \mathbf{y} \rVert$ avec la convention de signe, et arrêt dès que $\lVert \mathbf{x}_{\text{new}} - \mathbf{x} \rVert \le$ `tol`. Rends `(valeur, vecteur, itérations)`, la valeur étant $\mathbf{x}^\top\mathbf{A}\mathbf{x}$ pour le dernier $\mathbf{x}$ (unitaire), et les itérations le nombre de produits $\mathbf{A}\mathbf{x}$ calculés.

La vérification calcule, avec $\mathbf{S}$ = `""" + S_27 + r"""` :
- a) la valeur propre rendue par `power_iteration(S)` (6 décimales) ;
- b) le vecteur propre rendu par `power_iteration(S)` (une liste, 6 décimales) ;
- c) `rayleigh_quotient(S, [1, 1, 1])` (6 décimales) ;
- d) vrai ou faux : pour une matrice symétrique définie positive $8 \times 8$ tirée au hasard (`random_spd(8, 27)`, des outils), la valeur rendue est la plus grande valeur propre de `np.linalg.eigvalsh` à $10^{-8}$ près, et $\lVert \mathbf{A}\mathbf{v} - \lambda\mathbf{v} \rVert \le 10^{-6}$ ;
- e) la valeur et le vecteur rendus par `power_iteration(np.diag([-5.0, 2.0, 1.0]), x0=[1, 1, 1])` (une liste de 4 nombres : la valeur, puis les trois coordonnées du vecteur, 6 décimales) ;
- f) le nom de l'erreur levée par `power_iteration([[1, 2], [3, 4]], x0=[0, 0])` ;
- g) le nom de l'erreur levée par `rayleigh_quotient([[1, 2], [3, 4]], [0, 0])`.

Dans ta copie : combien d'itérations demande a), et pourquoi est-ce cohérent avec le rapport des deux plus grandes valeurs propres de $\mathbf{S}$ (calcule-les avec `np.linalg.eigvalsh`) ? Pourquoi c) est-il proche de a), sans lui être égal ? Que ferait $\mathbf{x}$ dans e) sans la convention de signe ?""",
    todo=LOAD_LEARNER,
    check=f'''A_27 = random_spd(8, 27)
with checked("M12c.27a"):
    wbm.check("M12c.27a", mymath.eigen.power_iteration({S_27})[0], computed=True)
with checked("M12c.27b"):
    wbm.check("M12c.27b", np.asarray(mymath.eigen.power_iteration({S_27})[1]).tolist(), computed=True)
with checked("M12c.27c"):
    wbm.check("M12c.27c", mymath.eigen.rayleigh_quotient({S_27}, [1, 1, 1]), computed=True)
with checked("M12c.27d"):
    value_27, vector_27, _ = mymath.eigen.power_iteration(A_27)
    wbm.check("M12c.27d", bool(abs(value_27 - np.linalg.eigvalsh(A_27)[-1]) <= 1e-8
                               and np.linalg.norm(A_27 @ vector_27 - value_27 * vector_27) <= 1e-6), computed=True)
with checked("M12c.27e"):
    value_27e, vector_27e, _ = mymath.eigen.power_iteration(np.diag([-5.0, 2.0, 1.0]), x0=[1, 1, 1])
    wbm.check("M12c.27e", [value_27e, *np.asarray(vector_27e).tolist()], computed=True)
with checked("M12c.27f"):
    wbm.check("M12c.27f", raised(mymath.eigen.power_iteration, [[1, 2], [3, 4]], x0=[0, 0]), computed=True)
with checked("M12c.27g"):
    wbm.check("M12c.27g", raised(mymath.eigen.rayleigh_quotient, [[1, 2], [3, 4]], [0, 0]), computed=True)''',
    solution=LOAD_REF + f'''
power_iteration, rayleigh_quotient = mymath.eigen.power_iteration, mymath.eigen.rayleigh_quotient
value, vector, iterations = power_iteration({S_27})
print("a)", round(value, 6), " b)", np.round(vector, 6).tolist(), " (", iterations, "iterations ; eigvalsh:",
      np.round(np.linalg.eigvalsh(np.array({S_27}, dtype=float)), 6).tolist(), ")")
print("c)", round(rayleigh_quotient({S_27}, [1, 1, 1]), 6))
A_27 = random_spd(8, 27)
value_27, vector_27, _ = power_iteration(A_27)
print("d)", bool(abs(value_27 - np.linalg.eigvalsh(A_27)[-1]) <= 1e-8
                 and np.linalg.norm(A_27 @ vector_27 - value_27 * vector_27) <= 1e-6))
value_27e, vector_27e, _ = power_iteration(np.diag([-5.0, 2.0, 1.0]), x0=[1, 1, 1])
print("e)", [round(value_27e, 6), *np.round(vector_27e, 6).tolist()],
      " f)", raised(power_iteration, [[1, 2], [3, 4]], x0=[0, 0]), " g)", raised(rayleigh_quotient, [[1, 2], [3, 4]], [0, 0]))''',
    record=f'''S_27 = np.array({S_27}, dtype=float)
values_27, vectors_27 = np.linalg.eigh(S_27)
v_27 = vectors_27[:, -1] * np.sign(vectors_27[np.argmax(np.abs(vectors_27[:, -1])), -1])
wbm.record("M12c.27a", float(values_27[-1]), decimals=6,
           mistakes={{"la valeur propre est le quotient de Rayleigh xᵀA x du dernier x unitaire": float(np.linalg.norm(S_27 @ v_27) ** 2)}})
wbm.record("M12c.27b", v_27.tolist(), decimals=6,
           mistakes={{"normalise x à chaque pas, et rends-le unitaire": (v_27 * 2).tolist(),
                     "la convention de signe : la coordonnée de plus grande valeur absolue positive": (-v_27).tolist()}})
wbm.record("M12c.27c", 13 / 3, decimals=6,
           mistakes={{"divise xᵀA x par xᵀx": 13.0}})
wbm.record("M12c.27d", True,
           mistakes={{"compare ta fonction à np.linalg.eigvalsh sur une petite matrice : normalisation, signe, arrêt": False}})
wbm.record("M12c.27e", [-5.0, 1.0, 0.0, 0.0], decimals=6,
           mistakes={{"la convention de signe : x doit garder sa coordonnée de plus grande valeur absolue positive": [-5.0, -1.0, 0.0, 0.0],
                     "la valeur propre est xᵀA x, pas ‖A x‖ : elle peut être négative": [5.0, 1.0, 0.0, 0.0]}})
wbm.record("M12c.27f", "ValueError",
           {value_error("x0 est nul : la docstring demande une ValueError")})
wbm.record("M12c.27g", "ValueError",
           {value_error("x est nul : la docstring demande une ValueError")})''',
    after=tests_cells("test_power_iteration_ or test_rayleigh_quotient_"),
    note=r"Les valeurs propres de $\mathbf{S}$ sont $3 + \sqrt{3} \approx 4{,}732$, $3$ et $3 - \sqrt{3}$ : le rapport "
         r"$3/4{,}732 \approx 0{,}63$ fait gagner un chiffre tous les 5 pas environ, d'où quelques dizaines d'itérations "
         r"pour $10^{-12}$. c) Le quotient de Rayleigh de $(1, 1, 1)$, $13/3$, est une moyenne pondérée des valeurs propres "
         r"(fiche §6) : proche de la plus grande parce que $(1, 1, 1)$ est proche de son vecteur propre. e) Sans la "
         r"convention, $\mathbf{x}$ changerait de signe à chaque pas ($\lambda_1 = -5 < 0$) et le critère d'arrêt ne serait "
         r"jamais atteint.",
)

A_28 = "[[25, -10, 15], [-10, 5, -4], [15, -4, 17]]"
MATRICES_28 = "[[[5, 2, 0], [2, 3, 1], [0, 1, 4]], [[2, 4], [4, 7]], [[1, 0], [0, 0]], [[2, 1], [0, 2]], [[6]]]"

M12C_28 = Ex(
    "M12c.28", "🔨", 2, 25, "La décomposition de Cholesky et le test « définie positive » · `cholesky, is_positive_definite`",
    "programmer la décomposition de Cholesky colonne par colonne, avec ses contrôles, et s'en servir pour tester qu'une "
    "matrice est définie positive.", "fiche §7 ; Ex M12c.26", tracks="C, E", mymath="eigen.py",
    body=r"""Écris, en suivant les docstrings :
- `cholesky(A)` (fiche §7) : une copie en flottants, une `ValueError` si $\mathbf{A}$ n'est pas carrée ou pas symétrique (au sens de la docstring du module : $|a_{ij} - a_{ji}| \le 10^{-12} \max(1, \max|\mathbf{A}|)$) ; puis, colonne par colonne, $l_{jj} = \sqrt{a_{jj} - \sum_{k<j} l_{jk}^2}$ (une `ValueError` si la quantité sous la racine n'est pas **strictement** positive) et $l_{ij} = (a_{ij} - \sum_{k<j} l_{ik}l_{jk})/l_{jj}$ sous la diagonale ; des zéros exacts au-dessus ;
- `is_positive_definite(A)` (fiche §7) : `ValueError` si $\mathbf{A}$ n'est pas carrée ; sinon essaie `cholesky` dans un `try`, et rends `True` ou `False` (des `bool` de Python).

La vérification calcule :
- a) `cholesky(""" + A_28 + r""")` (une matrice, 6 décimales) ;
- b) vrai ou faux : pour `random_spd(6, 28)`, $\mathbf{L}\mathbf{L}^\top = \mathbf{A}$ à $10^{-10}$ près, et les éléments au-dessus de la diagonale de $\mathbf{L}$ sont **exactement** nuls ;
- c) `[is_positive_definite(M) for M in """ + MATRICES_28 + r"""]` (une liste de 5 booléens) ;
- d) le nom de l'erreur levée par `cholesky([[1, 2], [3, 4]])` ;
- e) le nom de l'erreur levée par `cholesky([[1, 3], [3, 4]])` ;
- f) le nom de l'erreur levée par `is_positive_definite([[1, 0, 0], [0, 1, 0]])` ;
- g) vrai ou faux : `type(is_positive_definite(...))` est `bool` pour la première et la deuxième matrice de c).

Dans ta copie : retrouve a) à la main. Pour chaque matrice de c), dis pourquoi elle est, ou n'est pas, définie positive (et laquelle n'est pas symétrique). Pourquoi d) et e) lèvent-elles la même erreur pour deux raisons différentes ?""",
    todo=LOAD_LEARNER,
    check=f'''A_28r = random_spd(6, 28)
with checked("M12c.28a"):
    wbm.check("M12c.28a", np.asarray(mymath.eigen.cholesky({A_28})).tolist(), computed=True)
with checked("M12c.28b"):
    L_28 = np.asarray(mymath.eigen.cholesky(A_28r))
    wbm.check("M12c.28b", bool(np.allclose(L_28 @ L_28.T, A_28r, rtol=0, atol=1e-10) and np.all(np.triu(L_28, 1) == 0)),
              computed=True)
with checked("M12c.28c"):
    wbm.check("M12c.28c", [mymath.eigen.is_positive_definite(M) for M in {MATRICES_28}], computed=True)
with checked("M12c.28d"):
    wbm.check("M12c.28d", raised(mymath.eigen.cholesky, [[1, 2], [3, 4]]), computed=True)
with checked("M12c.28e"):
    wbm.check("M12c.28e", raised(mymath.eigen.cholesky, [[1, 3], [3, 4]]), computed=True)
with checked("M12c.28f"):
    wbm.check("M12c.28f", raised(mymath.eigen.is_positive_definite, [[1, 0, 0], [0, 1, 0]]), computed=True)
with checked("M12c.28g"):
    wbm.check("M12c.28g", all(type(mymath.eigen.is_positive_definite(M)) is bool for M in {MATRICES_28}[:2]),
              computed=True)''',
    solution=LOAD_REF + f'''
cholesky, is_positive_definite = mymath.eigen.cholesky, mymath.eigen.is_positive_definite
A_28r = random_spd(6, 28)
L_28 = cholesky(A_28r)
print("a)", np.round(cholesky({A_28}), 6).tolist(),
      " b)", bool(np.allclose(L_28 @ L_28.T, A_28r, rtol=0, atol=1e-10) and np.all(np.triu(L_28, 1) == 0)))
print("c)", [is_positive_definite(M) for M in {MATRICES_28}])
print("d)", raised(cholesky, [[1, 2], [3, 4]]), " e)", raised(cholesky, [[1, 3], [3, 4]]),
      " f)", raised(is_positive_definite, [[1, 0, 0], [0, 1, 0]]),
      " g)", all(type(is_positive_definite(M)) is bool for M in {MATRICES_28}[:2]))''',
    record=f'''wbm.record("M12c.28a", [[5.0, 0.0, 0.0], [-2.0, 1.0, 0.0], [3.0, 2.0, 2.0]], decimals=6,
           mistakes={{"L est triangulaire INFÉRIEURE : rends L, pas Lᵀ": [[5.0, -2.0, 3.0], [0.0, 1.0, 2.0], [0.0, 0.0, 2.0]],
                     "l_ij = (a_ij − Σ l_ik l_jk) / l_jj : divise par l_jj": [[5.0, 0.0, 0.0], [-10.0, 1.0, 0.0], [15.0, 2.0, 2.0]]}})
wbm.record("M12c.28b", True,
           mistakes={{"L Lᵀ doit redonner A, et L doit partir de np.zeros((n, n)) : rien au-dessus de la diagonale": False}})
wbm.record("M12c.28c", [True, False, False, False, True],
           mistakes={{"une matrice non symétrique n'est jamais définie positive au sens de la docstring": [True, False, False, True, True],
                     "semi-définie n'est pas définie : un pivot nul n'est pas strictement positif": [True, False, True, False, True]}})
wbm.record("M12c.28d", "ValueError",
           {value_error("une matrice non symétrique : la docstring demande une ValueError")})
wbm.record("M12c.28e", "ValueError",
           {value_error("une matrice qui n'est pas définie positive : un pivot n'est pas strictement positif, ValueError")})
wbm.record("M12c.28f", "ValueError",
           {value_error("une matrice non carrée : is_positive_definite lève une ValueError au lieu de répondre False")})
wbm.record("M12c.28g", True,
           mistakes={{"rends True ou False, des bool de Python, pas des np.bool_": False}})''',
    after=tests_cells("test_cholesky_ or test_is_positive_definite_"),
    note=r"a) $l_{11} = 5$, $l_{21} = -2$, $l_{31} = 3$ ; $l_{22} = \sqrt{5 - 4} = 1$, $l_{32} = (-4 + 6)/1 = 2$ ; "
         r"$l_{33} = \sqrt{17 - 9 - 4} = 2$. c) La première a pour mineurs 5, 11 et 39 ; $\det\begin{pmatrix} 2 & 4 \\ 4 & 7 "
         r"\end{pmatrix} = -2$ ; $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ est seulement semi-définie ; "
         r"$\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ n'est pas symétrique ; $(6)$ est définie positive. d) n'est pas "
         r"symétrique ; e) est symétrique mais indéfinie ($\det = -5$).",
)

M12C_29 = Ex(
    "M12c.29", "🔨", 2, 25, "La racine carrée d'une matrice symétrique positive et la matrice de blanchiment · "
    "`sqrtm_psd, whitening_matrix`",
    "programmer la racine carrée d'une matrice symétrique positive par le théorème spectral, et les blanchiments ZCA et "
    "de Cholesky.", "fiche §6 et §8 ; Ex M12c.28", tracks="C, E", mymath="eigen.py",
    body=r"""Écris, en suivant les docstrings (ici, et seulement ici, `np.linalg.eigh` est permis) :
- `sqrtm_psd(A, tol=1e-12)` (fiche §8) : `ValueError` si $\mathbf{A}$ n'est pas carrée ou pas symétrique ; `np.linalg.eigh` ; une `ValueError` si une valeur propre est inférieure à $-\mathrm{tol} \cdot \max(1, \lambda_{\max})$ ; les petites valeurs propres négatives (des arrondis) remplacées par 0 ; puis $\mathbf{Q}\operatorname{diag}(\sqrt{\lambda_i})\mathbf{Q}^\top$ ;
- `whitening_matrix(cov, method="zca")` (fiche §8) : `ValueError` si la méthode n'est ni `"zca"` ni `"cholesky"`, si `cov` n'est pas carrée ou pas symétrique ; pour `"zca"`, $\mathbf{Q}\operatorname{diag}(1/\sqrt{\lambda_i})\mathbf{Q}^\top$ (une `ValueError` si une valeur propre est $\le 0$) ; pour `"cholesky"`, $\mathbf{L}$ = `cholesky(cov)` (ta fonction de M12c.28), puis $\mathbf{W}$ solution de $\mathbf{L}\mathbf{W} = \mathbf{I}$ par `np.linalg.solve`.

La vérification calcule :
- a) `sqrtm_psd([[17, 6], [6, 5]])` (une matrice, 6 décimales) ;
- b) `sqrtm_psd([[9, 3], [3, 1]])` (une matrice, 6 décimales) ;
- c) `whitening_matrix([[4, -2], [-2, 2]])` (une matrice, 6 décimales) ;
- d) `whitening_matrix([[4, -2], [-2, 2]], method="cholesky")` (une matrice, 6 décimales) ;
- e) vrai ou faux : pour des données $\mathbf{X}$ corrélées de forme $(500, 3)$ (cellule de vérification), les données blanchies `(X - X.mean(axis=0)) @ W.T` ont pour covariance (`np.cov`) l'identité à $10^{-9}$ près, avec les deux méthodes, quand `W = whitening_matrix(np.cov(X, rowvar=False), method=...)` ;
- f) le nom de l'erreur levée par `whitening_matrix([[4, 0], [0, 1]], method="pca")` ;
- g) le nom de l'erreur levée par `sqrtm_psd([[1, 3], [3, 4]])`.

Dans ta copie : vérifie a) par le carré. Pourquoi b) existe-t-il, alors que $\begin{pmatrix} 9 & 3 \\ 3 & 1 \end{pmatrix}$ n'est pas inversible ? Écris la matrice $\mathbf{L}$ de d) et vérifie $\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top = \mathbf{I}$ à la main. Pourquoi c) est-elle symétrique et pas d) ?""",
    todo=LOAD_LEARNER,
    check='''X_29 = np.random.default_rng(29).normal(size=(500, 3)) @ np.array([[2.0, 0.0, 0.0], [1.0, 1.5, 0.0], [-0.5, 1.0, 0.5]])
cov_29 = np.cov(X_29, rowvar=False)
with checked("M12c.29a"):
    wbm.check("M12c.29a", np.asarray(mymath.eigen.sqrtm_psd([[17, 6], [6, 5]])).tolist(), computed=True)
with checked("M12c.29b"):
    wbm.check("M12c.29b", np.asarray(mymath.eigen.sqrtm_psd([[9, 3], [3, 1]])).tolist(), computed=True)
with checked("M12c.29c"):
    wbm.check("M12c.29c", np.asarray(mymath.eigen.whitening_matrix([[4, -2], [-2, 2]])).tolist(), computed=True)
with checked("M12c.29d"):
    wbm.check("M12c.29d", np.asarray(mymath.eigen.whitening_matrix([[4, -2], [-2, 2]], method="cholesky")).tolist(),
              computed=True)
with checked("M12c.29e"):
    whitened_29 = [np.cov((X_29 - X_29.mean(axis=0)) @ np.asarray(mymath.eigen.whitening_matrix(cov_29, method=m)).T,
                          rowvar=False) for m in ("zca", "cholesky")]
    wbm.check("M12c.29e", all(np.allclose(C, np.eye(3), rtol=0, atol=1e-9) for C in whitened_29), computed=True)
with checked("M12c.29f"):
    wbm.check("M12c.29f", raised(mymath.eigen.whitening_matrix, [[4, 0], [0, 1]], method="pca"), computed=True)
with checked("M12c.29g"):
    wbm.check("M12c.29g", raised(mymath.eigen.sqrtm_psd, [[1, 3], [3, 4]]), computed=True)''',
    solution=LOAD_REF + '''
sqrtm_psd, whitening_matrix = mymath.eigen.sqrtm_psd, mymath.eigen.whitening_matrix
X_29 = np.random.default_rng(29).normal(size=(500, 3)) @ np.array([[2.0, 0.0, 0.0], [1.0, 1.5, 0.0], [-0.5, 1.0, 0.5]])
cov_29 = np.cov(X_29, rowvar=False)
print("a)", np.round(sqrtm_psd([[17, 6], [6, 5]]), 6).tolist(), " b)", np.round(sqrtm_psd([[9, 3], [3, 1]]), 6).tolist())
print("c)", np.round(whitening_matrix([[4, -2], [-2, 2]]), 6).tolist(),
      " d)", np.round(whitening_matrix([[4, -2], [-2, 2]], method="cholesky"), 6).tolist())
whitened_29 = [np.cov((X_29 - X_29.mean(axis=0)) @ whitening_matrix(cov_29, method=m).T, rowvar=False)
               for m in ("zca", "cholesky")]
print("e)", all(np.allclose(C, np.eye(3), rtol=0, atol=1e-9) for C in whitened_29),
      " f)", raised(whitening_matrix, [[4, 0], [0, 1]], method="pca"), " g)", raised(sqrtm_psd, [[1, 3], [3, 4]]))''',
    record='''import scipy.linalg
ZCA_29 = np.linalg.inv(np.real(scipy.linalg.sqrtm(np.array([[4.0, -2.0], [-2.0, 2.0]]))))
wbm.record("M12c.29a", [[4.0, 1.0], [1.0, 2.0]], decimals=6,
           mistakes={"la racine carrée d'une matrice n'est pas celle de ses éléments : Q diag(√λ) Qᵀ":
                         np.sqrt([[17.0, 6.0], [6.0, 5.0]]).tolist()})
wbm.record("M12c.29b", (np.array([[9.0, 3.0], [3.0, 1.0]]) / np.sqrt(10)).tolist(), decimals=6,
           mistakes={"la racine carrée d'une matrice n'est pas celle de ses éléments : Q diag(√λ) Qᵀ":
                         np.sqrt([[9.0, 3.0], [3.0, 1.0]]).tolist()})
wbm.record("M12c.29c", ZCA_29.tolist(), decimals=6,
           mistakes={"W = Σ^(−1/2) = Q diag(1/√λ) Qᵀ, pas Σ^(1/2)":
                         np.real(scipy.linalg.sqrtm(np.array([[4.0, -2.0], [-2.0, 2.0]]))).tolist()})
wbm.record("M12c.29d", [[0.5, 0.0], [0.5, 1.0]], decimals=6,
           mistakes={"W = L⁻¹ (triangulaire inférieure), pas L⁻ᵀ": [[0.5, 0.5], [0.0, 1.0]],
                     "W = L⁻¹, pas L": [[2.0, 0.0], [-1.0, 1.0]]})
wbm.record("M12c.29e", True,
           mistakes={"W Σ Wᵀ doit valoir I : relis les deux méthodes sur une matrice diagonale, où tout se fait à la main": False})
wbm.record("M12c.29f", "ValueError",
           {"une méthode inconnue : la docstring demande une ValueError": "aucune",
            "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)":
                {"AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError", "TypeError",
                 "RuntimeError", "ZeroDivisionError", "LinAlgError"}})
wbm.record("M12c.29g", "ValueError",
           {"une valeur propre négative : la matrice n'est pas semi-définie positive, ValueError": "aucune",
            "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)":
                {"AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError", "TypeError",
                 "RuntimeError", "ZeroDivisionError", "LinAlgError"}})''',
    after=tests_cells("test_sqrtm_psd_ or test_whitening_matrix_"),
    note=r"a) $\begin{pmatrix} 4 & 1 \\ 1 & 2 \end{pmatrix}^2 = \begin{pmatrix} 17 & 6 \\ 6 & 5 \end{pmatrix}$, et "
         r"$\begin{pmatrix} 4 & 1 \\ 1 & 2 \end{pmatrix}$ est symétrique définie positive. b) La matrice vaut "
         r"$\mathbf{v}\mathbf{v}^\top$ avec $\mathbf{v} = (3, 1)$ : valeurs propres 10 et 0 ; la racine garde la valeur propre 0, "
         r"$\sqrt{10}\,\mathbf{u}\mathbf{u}^\top = \mathbf{v}\mathbf{v}^\top/\sqrt{10}$, avec $\mathbf{u} = \mathbf{v}/\sqrt{10}$. "
         r"d) $\mathbf{L} = \begin{pmatrix} 2 & 0 \\ -1 & 1 \end{pmatrix}$, d'inverse $\begin{pmatrix} 1/2 & 0 \\ 1/2 & 1 "
         r"\end{pmatrix}$. ZCA est symétrique par construction ($\mathbf{Q}\mathbf{D}\mathbf{Q}^\top$), Cholesky triangulaire.",
)

S_30 = "[[6, 2, 1, 0], [2, 5, 2, 1], [1, 2, 4, 2], [0, 1, 2, 3]]"

M12C_30 = Ex(
    "M12c.30", "📦", 1, 15, "`np.linalg.eigh`, `det`, `cholesky` et `scipy.linalg.sqrtm` contre tes fonctions",
    "utiliser `np.linalg.eigh`, `det`, `cholesky` et `scipy.linalg.sqrtm`, lire ce qu'elles rendent, et comparer avec ta "
    "librairie.", "fiche §1, §6 et §7 ; Ex M12c.26 à M12c.29", tracks="C, E",
    body=r"""En pratique, on ne réécrit pas ces fonctions :
- `np.linalg.eigh(S)` (matrices **symétriques**) rend `(valeurs, vecteurs)` : les valeurs propres réelles par ordre **croissant**, et une matrice dont les **colonnes** sont des vecteurs propres orthonormés ; `np.linalg.eig(A)` (toute matrice carrée) rend la même chose sans ordre garanti, éventuellement en nombres complexes ;
- `np.linalg.det(A)` et `np.linalg.cholesky(S)` (qui ne vérifie pas la symétrie : elle ne lit que le triangle inférieur) ;
- `scipy.linalg.sqrtm(A)`, la racine carrée de toute matrice qui en a une.

Avec $\mathbf{S}$ = `""" + S_30 + r"""`, calcule :
- a) les valeurs propres rendues par `np.linalg.eigh(S)` (une liste, 4 décimales, dans l'ordre rendu) ;
- b) vrai ou faux : les colonnes de la matrice de vecteurs propres rendue par `eigh` sont orthonormées, à $10^{-12}$ près ;
- c) vrai ou faux : la valeur rendue par ta fonction `power_iteration(S)` est la plus grande valeur de a), à $10^{-8}$ près ;
- d) vrai ou faux : ta fonction `det(S)` est égale à `np.linalg.det(S)` et au produit des valeurs de a), à $10^{-10}$ près, relativement ;
- e) vrai ou faux : ta fonction `cholesky(S)` est égale à `np.linalg.cholesky(S)` à $10^{-12}$ près ;
- f) vrai ou faux : ta fonction `sqrtm_psd(S)` est égale à `scipy.linalg.sqrtm(S)` à $10^{-10}$ près ;
- g) le type (`dtype`, en texte : `str(values.dtype)`) des valeurs propres rendues par `np.linalg.eig([[0, -1], [1, 0]])`.

Dans ta copie : pourquoi `eigh` plutôt que `eig` pour une matrice symétrique (deux raisons) ? Que rendrait `np.linalg.cholesky([[4, 7], [-3, 5]])`, et pourquoi est-ce dangereux ? Pourquoi g) n'est-il pas un type de nombres réels ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12c")
import scipy.linalg

S_30 = np.array(''' + S_30 + ''', dtype=float)
answer_M12c_30a = ...  # a) a list of 4 numbers (4 decimals), in the order returned by eigh
answer_M12c_30b = ...  # b) True or False
answer_M12c_30g = ...  # g) a text: str(values.dtype)
answer_M12c_30c = answer_M12c_30d = answer_M12c_30e = answer_M12c_30f = None
# Each block stands alone: compute inside it what it needs, so that "Run all" goes on when a function is not written.
with wbm.attempt("M12c.30c"):        # your power_iteration is called here: ⏳ while it is not written
    answer_M12c_30c = ...  # c) True or False
with wbm.attempt("M12c.30d"):        # your det
    answer_M12c_30d = ...  # d) True or False
with wbm.attempt("M12c.30e"):        # your cholesky
    answer_M12c_30e = ...  # e) True or False
with wbm.attempt("M12c.30f"):        # your sqrtm_psd
    answer_M12c_30f = ...  # f) True or False''',
    check='''for letter, answer in zip("abcdefg", [answer_M12c_30a, answer_M12c_30b, answer_M12c_30c, answer_M12c_30d,
                                       answer_M12c_30e, answer_M12c_30f, answer_M12c_30g]):
    wbm.check(f"M12c.30{letter}", answer)''',
    solution='''ref_30 = wbm.load_mymath("ref", alias="mymath_ref").eigen
import scipy.linalg

S_30 = np.array(''' + S_30 + ''', dtype=float)
values_30, vectors_30 = np.linalg.eigh(S_30)
answer_M12c_30a = np.round(values_30, 4).tolist()
answer_M12c_30b = bool(np.allclose(vectors_30.T @ vectors_30, np.eye(4), rtol=0, atol=1e-12))
answer_M12c_30c = bool(abs(ref_30.power_iteration(S_30)[0] - values_30[-1]) <= 1e-8)
d_30 = ref_30.det(S_30)
answer_M12c_30d = bool(abs(d_30 - np.linalg.det(S_30)) <= 1e-10 * abs(d_30) and abs(d_30 - np.prod(values_30)) <= 1e-10 * abs(d_30))
answer_M12c_30e = bool(np.allclose(ref_30.cholesky(S_30), np.linalg.cholesky(S_30), rtol=0, atol=1e-12))
answer_M12c_30f = bool(np.allclose(ref_30.sqrtm_psd(S_30), np.real(scipy.linalg.sqrtm(S_30)), rtol=0, atol=1e-10))
answer_M12c_30g = str(np.linalg.eig(np.array([[0.0, -1.0], [1.0, 0.0]]))[0].dtype)
print(answer_M12c_30a, answer_M12c_30b, answer_M12c_30c, answer_M12c_30d, answer_M12c_30e, answer_M12c_30f, answer_M12c_30g)
print("np.linalg.cholesky([[4, 7], [-3, 5]]):", np.linalg.cholesky(np.array([[4.0, 7.0], [-3.0, 5.0]])).tolist())''',
    record='''values_30r = np.linalg.eigvalsh(np.array(''' + S_30 + ''', dtype=float))
wbm.record("M12c.30a", values_30r.tolist(), decimals=4,
           mistakes={"eigh rend les valeurs propres par ordre CROISSANT : garde l'ordre rendu": values_30r[::-1].tolist()})
wbm.record("M12c.30b", True, mistakes={"Vᵀ V = I : les vecteurs propres d'une matrice symétrique sont orthonormés": False})
wbm.record("M12c.30c", True,
           mistakes={"relis ta fonction power_iteration (M12c.27) : ses tests disent ce qui ne va pas": False})
wbm.record("M12c.30d", True, mistakes={"relis ta fonction det (M12c.26) : ses tests disent ce qui ne va pas": False})
wbm.record("M12c.30e", True, mistakes={"relis ta fonction cholesky (M12c.28) : ses tests disent ce qui ne va pas": False})
wbm.record("M12c.30f", True, mistakes={"relis ta fonction sqrtm_psd (M12c.29) : ses tests disent ce qui ne va pas": False})
wbm.record("M12c.30g", "complex128",
           mistakes={"une rotation n'a pas de valeur propre réelle : eig rend des nombres complexes": "float64"})''',
    note=r"`eigh` exploite la symétrie : plus rapide, des valeurs propres réelles garanties et rangées, des vecteurs "
         r"orthonormés même pour une valeur propre multiple. `np.linalg.cholesky` sur une matrice non symétrique "
         r"factorise silencieusement la matrice symétrique construite sur son triangle inférieur : un résultat faux sans "
         r"erreur (M12c.34). g) La rotation d'un quart de tour a pour valeurs propres $\pm i$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M12c.31 to M12c.33)
# ---------------------------------------------------------------------------
M12C_31_GIVEN = '''A_FAR_31 = np.diag([10.0, 5.0, 1.0])       # λ₂ / λ₁ = 0.5
A_CLOSE_31 = np.diag([10.0, 9.9, 1.0])     # λ₂ / λ₁ = 0.99
START_31 = np.ones(3)'''

M12C_31_EXPERIMENT = '''for name, A in (("éloignées", A_FAR_31), ("proches", A_CLOSE_31)):
    value, vector, iterations = power_31(A, x0=START_31)
    print(f"{name:10s} : {iterations:5d} itérations, valeur {value:.12f}, écart du vecteur à e₁ "
          f"{np.linalg.norm(vector - np.array([1.0, 0.0, 0.0])):.1e}")'''

M12C_31 = Ex(
    "M12c.31", "🔮", 1, 10, "Prédire : la méthode de la puissance quand les deux plus grandes valeurs propres sont "
    "proches",
    "prévoir la vitesse de la méthode de la puissance et la précision du vecteur et de la valeur propre quand les deux "
    "plus grandes valeurs propres sont proches, puis le vérifier.", "fiche §5 et §6 ; Ex M12c.27", tracks="C, E",
    hypothesis=True, given=M12C_31_GIVEN,
    body=r"""La cellule fournie définit deux matrices diagonales : $\operatorname{diag}(10, 5, 1)$, dont les deux plus grandes valeurs propres sont **éloignées** ($|\lambda_2/\lambda_1| = 0{,}5$), et $\operatorname{diag}(10 ;\ 9{,}9 ;\ 1)$, dont elles sont **proches** ($0{,}99$). On lance `power_iteration` sur chacune depuis $(1, 1, 1)$, avec les réglages par défaut (`n_iter=1000`, `tol=1e-12`). Pour chaque question, choisis le numéro de la bonne réponse :
- a) le nombre d'itérations pour la matrice éloignée : (1) moins de 100 ; (2) entre 100 et 999 ; (3) 1000, le maximum, sans atteindre la tolérance ;
- b) le nombre d'itérations pour la matrice proche : mêmes choix ;
- c) pour la matrice proche, l'écart entre la valeur rendue et 10 : (1) moins de $10^{-6}$ ; (2) entre $10^{-6}$ et $10^{-2}$ ; (3) plus de $10^{-2}$ ;
- d) pour la matrice proche, l'écart $\lVert \mathbf{v} - \mathbf{e}_1 \rVert$ du vecteur rendu : (1) moins de $10^{-8}$ ; (2) entre $10^{-8}$ et $10^{-3}$ ; (3) plus de $10^{-3}$.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M12c_31a = ...  # a) 1, 2 or 3, written BEFORE running the experiment below
prediction_M12c_31b = ...  # b) 1, 2 or 3
prediction_M12c_31c = ...  # c) 1, 2 or 3
prediction_M12c_31d = ...  # d) 1, 2 or 3''',
    check='''for letter, prediction in zip("abcd", [prediction_M12c_31a, prediction_M12c_31b, prediction_M12c_31c,
                                      prediction_M12c_31d]):
    wbm.check(f"M12c.31{letter}", prediction)''',
    record='''wbm.record("M12c.31a", 1, prediction=True, choices=[1, 2, 3])
wbm.record("M12c.31b", 3, prediction=True, choices=[1, 2, 3])
wbm.record("M12c.31c", 1, prediction=True, choices=[1, 2, 3])
wbm.record("M12c.31d", 2, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience** (avec ta fonction `power_iteration`, ou la référence si elle n'est pas encore écrite). "
               "Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded('''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12c")
try:                                             # your power_iteration if it runs, else the reference
    mymath.eigen.power_iteration(A_FAR_31, x0=START_31)
    power_31 = mymath.eigen.power_iteration
    print("avec ta fonction power_iteration")
except Exception:  # noqa: BLE001 - not written yet (NotImplementedError), missing file, or a bug
    power_31 = wbm.load_mymath("ref", alias="mymath_ref").eigen.power_iteration
    print("ℹ️ ta fonction power_iteration n'est pas encore écrite (ou lève une erreur) : l'expérience utilise la référence")
''' + M12C_31_EXPERIMENT, [f"prediction_M12c_31{letter}" for letter in "abcd"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", LOAD_REF + "\npower_31 = mymath.eigen.power_iteration\n" + M12C_31_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : combien d'itérations aurait-il fallu à la matrice proche pour "
               "atteindre la tolérance (résous $0{,}99^k \\approx 10^{-12}$) ? Pourquoi la valeur propre est-elle si "
               "précise alors que le vecteur ne l'est pas (écris le quotient de Rayleigh avec les coordonnées de "
               "$\\mathbf{x}$, fiche §6) ? Qu'en conclure sur un critère d'arrêt qui ne regarde que la valeur propre ?"),
    ],
    note=r"a) L'écart est divisé par 2 à chaque pas : environ 40 pas pour $10^{-12}$. b) $0{,}99^k = 10^{-12}$ demande "
         r"$k \approx 2\,750$ : la méthode s'arrête à 1 000 sans avoir convergé. d) Après 1 000 pas, la composante sur "
         r"$\mathbf{e}_2$ vaut environ $0{,}99^{1000} \approx 4 \times 10^{-5}$. c) Le quotient de Rayleigh d'une matrice "
         r"symétrique a une erreur de l'ordre du **carré** de celle du vecteur (fiche §5 et §6) : environ "
         r"$0{,}1 \times (4 \times 10^{-5})^2 \approx 2 \times 10^{-10}$.",
)

M12C_32_GIVEN = '''RATIOS_32 = [0.1, 0.3, 0.5, 0.7, 0.9, 0.95, 0.99]


def ratio_matrix(r):
    """A 3 × 3 diagonal matrix whose two largest eigenvalues have the ratio r: diag(1, r, r / 2)."""
    return np.diag([1.0, r, r / 2])'''

M12C_32_SHOW = '''counts = iteration_table()
print("  r      itérations   itérations × (−log₁₀ r)")
for r, k in zip(RATIOS_32, counts):
    print(f"{r:5.2f}   {k:10d}   {k * -np.log10(r):10.1f}")'''

M12C_32 = Ex(
    "M12c.32", "🔬", 2, 20, "La vitesse de la méthode de la puissance et le rapport |λ₂ / λ₁|",
    "mesurer le nombre d'itérations de la méthode de la puissance en fonction du rapport des deux plus grandes valeurs "
    "propres, et retrouver la loi $|\\lambda_2/\\lambda_1|^k$.", "fiche §5 ; Ex M12c.27 et M12c.31", tracks="C",
    given=M12C_32_GIVEN,
    body=r"""Pour chaque rapport $r$ de `RATIOS_32`, la fonction fournie `ratio_matrix(r)` rend $\operatorname{diag}(1, r, r/2)$, dont les deux plus grandes valeurs propres ont le rapport $r$. Écris :
- `iteration_table()` : la liste des nombres d'itérations de `mymath.eigen.power_iteration(ratio_matrix(r), x0=np.ones(3), n_iter=10_000)` (tolérance par défaut, $10^{-12}$), pour chaque $r$ de `RATIOS_32`.

La cellule suivante affiche le tableau, avec le produit $k \times (-\log_{10} r)$ : le nombre de chiffres décimaux gagnés en $k$ pas si l'écart est multiplié par $r$ à chaque pas. Lis-le, puis réponds :
- a) le nombre d'itérations pour $r = 0{,}5$ ;
- b) le plus petit $r$ du tableau qui demande plus de 1 000 itérations ;
- c) vrai ou faux : pour tous les $r$ du tableau, $k \times (-\log_{10} r)$ est compris entre 9 et 14 ;
- d) vrai ou faux : passer de $r = 0{,}9$ à $r = 0{,}99$ multiplie le nombre d'itérations par plus de 9.

Dans ta copie : pourquoi le produit $k \times (-\log_{10} r)$ est-il presque constant, et que vaut-il en théorie pour une tolérance de $10^{-12}$ ? Pourquoi $r = 0{,}1$ ne demande-t-il pas exactement 12 itérations ? Pour une matrice $10^6 \times 10^6$ avec $r = 0{,}999$, combien de produits matrice-vecteur faudrait-il, et que faire à la place (fiche §5, 💻) ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12c")


def iteration_table():
    """For r in RATIOS_32: the number of iterations of power_iteration on ratio_matrix(r), from (1, 1, 1)."""
    raise NotImplementedError("une liste de 7 entiers : le troisième élément rendu par power_iteration")''',
    check=f'''with checked("M12c.32 tableau"):
{chr(10).join("    " + line for line in M12C_32_SHOW.splitlines())}''' + '''

answer_M12c_32a = ...  # a) an integer, read in the table above
answer_M12c_32b = ...  # b) a number of RATIOS_32
answer_M12c_32c = ...  # c) True or False
answer_M12c_32d = ...  # d) True or False
for letter, answer in zip("abcd", [answer_M12c_32a, answer_M12c_32b, answer_M12c_32c, answer_M12c_32d]):
    wbm.check(f"M12c.32{letter}", answer)''',
    solution=LOAD_REF + '''


def iteration_table():
    """For r in RATIOS_32: the number of iterations of power_iteration on ratio_matrix(r), from (1, 1, 1)."""
    return [mymath.eigen.power_iteration(ratio_matrix(r), x0=np.ones(3), n_iter=10_000)[2] for r in RATIOS_32]


''' + M12C_32_SHOW,
    record='''counts_32 = iteration_table()
first_32 = next(r for r, k in zip(RATIOS_32, counts_32) if k > 1000)
products_32 = [k * -np.log10(r) for r, k in zip(RATIOS_32, counts_32)]
wbm.record("M12c.32a", counts_32[2],
           mistakes={"lis la ligne r = 0,5 de la colonne des itérations": counts_32[1]})
wbm.record("M12c.32b", first_32, decimals=2,
           mistakes={"le premier r qui DÉPASSE 1 000 itérations, pas le dernier en dessous": RATIOS_32[RATIOS_32.index(first_32) - 1]})
wbm.record("M12c.32c", bool(all(9 <= p <= 14 for p in products_32)),
           mistakes={"lis la dernière colonne, pour chaque ligne": not all(9 <= p <= 14 for p in products_32)})
wbm.record("M12c.32d", bool(counts_32[6] > 9 * counts_32[4]),
           mistakes={"compare les itérations des lignes r = 0,9 et r = 0,99": not counts_32[6] > 9 * counts_32[4]})''',
    note=r"Si l'écart est multiplié par $r$ à chaque pas, il faut $k \approx 12/(-\log_{10} r)$ pas pour gagner les 12 "
         r"chiffres de la tolérance : $k \times (-\log_{10} r) \approx 12$, aux constantes près (l'écart de départ, la "
         r"troisième valeur propre, et le critère qui compare deux itérés). $\log_{10} 0{,}99 \approx -0{,}0044$ contre "
         r"$\log_{10} 0{,}9 \approx -0{,}046$ : environ 10 fois plus d'itérations. Avec $r = 0{,}999$, environ 28 000 "
         r"produits ; on passe alors à des méthodes de Krylov (Lanczos, `scipy.sparse.linalg.eigsh`).",
)

M12C_33_GIVEN = '''MATRICES_33 = {"définie positive": np.array([[3.0, -1.0], [-1.0, 4.0]]),
               "semi-définie positive": np.array([[1.0, 3.0], [3.0, 9.0]]),
               "indéfinie": np.array([[1.0, 2.0], [2.0, -2.0]])}'''

M12C_33_FIGURE = '''fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.6))
try:
    for ax, (name, A) in zip(axes, MATRICES_33.items()):
        draw_levels(ax, A)
        ax.set_title(f"{name} : {classify(A)}")
except BaseException:
    plt.close(fig)
    raise
plt.show()'''

M12C_33_CHECK = '''with checked("M12c.33 vérifications"):
    cases_33 = [([[2.0, 0.0], [0.0, 5.0]], "définie positive"), ([[0.0, 0.0], [0.0, 3.0]], "semi-définie positive"),
                ([[-2.0, 1.0], [1.0, -3.0]], "définie négative"), ([[0.0, 1.0], [1.0, 0.0]], "indéfinie"),
                ([[4.0, 2.0], [2.0, 1.0]], "semi-définie positive"), ([[1.0, 0.0], [0.0, 1e-9]], "définie positive")]
    wrong_33 = [(A, expected, classify(np.array(A))) for A, expected in cases_33 if classify(np.array(A)) != expected]
    if wrong_33:
        A, expected, got = wrong_33[0]
        print(f"❌ Ex M12c.33 : classify({A}) rend {got!r}, on attendait {expected!r} : regarde les signes des valeurs "
              f"propres (np.linalg.eigvalsh), avec une tolérance pour zéro.")
    else:
        print("✅ Ex M12c.33 : classify range correctement six matrices, dont deux semi-définies.")'''

M12C_33 = Ex(
    "M12c.33", "🎨", 1, 20, "Les lignes de niveau de xᵀAx : définie positive, semi-définie positive, indéfinie",
    "dessiner les lignes de niveau d'une forme quadratique avec ses axes propres, et classer une matrice symétrique "
    "d'après les signes de ses valeurs propres.", "fiche §6 et §7", tracks="C, E", given=M12C_33_GIVEN,
    body=r"""Écris :
- `classify(A)` : pour une matrice symétrique $2 \times 2$, le texte `"définie positive"`, `"semi-définie positive"`, `"définie négative"`, `"semi-définie négative"` ou `"indéfinie"`, d'après les signes de ses valeurs propres (`np.linalg.eigvalsh`) ; une valeur propre de valeur absolue inférieure à $10^{-12}$ fois la plus grande compte comme nulle ;
- `draw_levels(ax, A)` : dans l'axe `ax`, les lignes de niveau de $q(\mathbf{x}) = \mathbf{x}^\top\mathbf{A}\mathbf{x}$ sur $[-2 ; 2]^2$ (`ax.contour` sur une grille `np.meshgrid`, avec quelques niveaux positifs et, si la forme en prend, négatifs), et les deux vecteurs propres unitaires de $\mathbf{A}$ en flèches (`ax.annotate` ou `ax.arrow`), avec `ax.set_aspect("equal")`.

La cellule de la figure s'en sert pour les trois matrices fournies ; une cellule de vérification essaie `classify` sur six autres matrices.

Dans ta copie : pour la matrice définie positive, le long de quel vecteur propre l'ellipse est-elle la plus allongée, et pourquoi (fiche §7) ? Pour la matrice semi-définie, dans quelle direction $q$ reste-t-elle nulle, et quel est le lien avec son noyau ? Pour l'indéfinie, le long de quelles droites $q$ s'annule-t-elle ? Pourquoi $\operatorname{diag}(1 ;\ 10^{-9})$ est-elle « définie positive » pour `classify`, alors qu'à l'écran elle ressemble à la semi-définie ?""",
    todo='''def classify(A):
    """The kind of the symmetric 2 × 2 matrix A, from the signs of its eigenvalues (zero within 1e-12 · max |λ|)."""
    raise NotImplementedError("np.linalg.eigvalsh, puis les signes")


def draw_levels(ax, A):
    """In ax: the level curves of xᵀAx on [-2, 2]², and the two unit eigenvectors of A as arrows."""
    raise NotImplementedError("np.meshgrid, ax.contour, puis deux flèches")''',
    check='''with checked("M12c.33 figure"):
''' + "\n".join("    " + line for line in M12C_33_FIGURE.splitlines()),
    solution='''def classify(A):
    """The kind of the symmetric 2 × 2 matrix A, from the signs of its eigenvalues (zero within 1e-12 · max |λ|)."""
    values = np.linalg.eigvalsh(np.asarray(A, dtype=float))
    scale = max(1e-300, float(np.max(np.abs(values))))
    signs = {int(np.sign(v)) if abs(v) > 1e-12 * scale else 0 for v in values}
    if signs == {1}:
        return "définie positive"
    if signs == {-1}:
        return "définie négative"
    if -1 not in signs:
        return "semi-définie positive"
    if 1 not in signs:
        return "semi-définie négative"
    return "indéfinie"


def draw_levels(ax, A):
    """In ax: the level curves of xᵀAx on [-2, 2]², and the two unit eigenvectors of A as arrows."""
    A = np.asarray(A, dtype=float)
    grid = np.linspace(-2, 2, 201)
    X, Y = np.meshgrid(grid, grid)
    Q = A[0, 0] * X ** 2 + 2 * A[0, 1] * X * Y + A[1, 1] * Y ** 2
    levels = [v for v in (-8, -4, -2, -1, -0.5, 0.5, 1, 2, 4, 8) if Q.min() < v < Q.max()]
    ax.contour(X, Y, Q, levels=levels, cmap="viridis")
    values, vectors = np.linalg.eigh(A)
    for value, vector, color in zip(values, vectors.T, ("C1", "C3")):
        ax.annotate("", xy=vector, xytext=(0, 0), arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2})
        ax.text(*(1.15 * vector), f"λ = {value:.2f}".replace(".", ","), color=color)
    ax.axhline(0, color="0.7", lw=0.6)
    ax.axvline(0, color="0.7", lw=0.6)
    ax.set_aspect("equal")


''' + M12C_33_FIGURE,
    after=[("md", "**Vérifications automatiques** (six autres matrices pour `classify`)."), ("code", M12C_33_CHECK)],
    note=r"L'ellipse est la plus allongée le long du vecteur propre de la **plus petite** valeur propre : $q$ y monte le "
         r"moins vite. Pour $\begin{pmatrix} 1 & 3 \\ 3 & 9 \end{pmatrix} = (1, 3)(1, 3)^\top$, $q(\mathbf{x}) = (x + 3y)^2$ est "
         r"nulle sur la droite $x + 3y = 0$, le noyau. Pour l'indéfinie, $x^2 + 4xy - 2y^2 = 0$ donne deux droites, les "
         r"asymptotes des hyperboles. $\operatorname{diag}(1 ;\ 10^{-9})$ a deux valeurs propres positives : définie "
         r"positive, mais si près de la semi-définie qu'un arrondi peut la faire basculer (son conditionnement, M12d).",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M12c.34 to M12c.36)
# ---------------------------------------------------------------------------
M12C_34_MISTAKES = bug_letters_mistakes(
    "ACE", "BDF",
    {"A": "refais chaque ligne à la main, avec ses propres nombres",
     "C": "vérifie chaque résultat : un vecteur propre se vérifie en un produit",
     "E": "regarde les hypothèses de chaque fonction appelée"},
    name_correct=False)

M12C_34 = Ex(
    "M12c.34", "🐛", 1, 15, "Chasse à l'erreur : det(A + B) = det A + det B, un vecteur propre nul, Cholesky d'une "
    "matrice non symétrique",
    "repérer dans du code les erreurs classiques sur le déterminant, les vecteurs propres et Cholesky, puis calculer les "
    "bonnes valeurs.", "fiche §1, §3 et §7", tracks="C",
    body=r"""Un collègue a écrit le code suivant ; six lignes portent une lettre et un commentaire qui dit ce qu'elles doivent calculer. Trois lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter de code**, trouve-les.

```python
A = np.array([[1.0, 2.0], [3.0, 1.0]])
B = np.array([[2.0, 0.0], [1.0, -1.0]])
C = np.array([[4.0, 2.0], [-2.0, 5.0]])
x = np.array([1.0, 1.0])
d = np.linalg.det(A) + np.linalg.det(B)                   # (A) det(A + B)
t = np.trace(A) + np.trace(B)                             # (B) tr(A + B)
lam = 1 + np.sqrt(6)                                      # an eigenvalue of A
v = np.linalg.solve(A - lam * np.eye(2), np.zeros(2))     # (C) an eigenvector of A for lam: v[1] / v[0]
p = np.prod(np.linalg.eigvals(A))                         # (D) det A
L = np.linalg.cholesky(C)                                 # (E) the Cholesky factor of C, with C = L L^T: L[1, 0]
r = (x @ A @ x) / (x @ x)                                 # (F) the Rayleigh quotient of A at x
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour les lignes (A), (B), (C), (D) et (F), la bonne valeur de ce que dit leur commentaire (une liste de 5 nombres, 4 décimales) ;
- c) vrai ou faux : `np.linalg.cholesky(C)` lève une erreur.

Dans ta copie : pour chaque ligne fausse, quelle erreur a été faite, et comment la corriger ? Que rend la ligne (C), et pourquoi un résultat de ce genre devrait-il toujours alerter ? Que factorise réellement la ligne (E) ? Laquelle des trois est la plus dangereuse, et pourquoi ?""",
    todo='''answer_M12c_34a = ...  # a) letters, as text
answer_M12c_34b = ...  # b) a list of 5 values (4 decimals)
answer_M12c_34c = ...  # c) True or False''',
    check='''wbm.check("M12c.34a", answer_M12c_34a)
wbm.check("M12c.34b", answer_M12c_34b)
wbm.check("M12c.34c", answer_M12c_34c)''',
    solution='''answer_M12c_34a = "ACE"
A = np.array([[1.0, 2.0], [3.0, 1.0]])
B = np.array([[2.0, 0.0], [1.0, -1.0]])
C = np.array([[4.0, 2.0], [-2.0, 5.0]])
x = np.array([1.0, 1.0])
d = np.linalg.det(A + B)                                  # (A) the determinant of the sum
t = np.trace(A) + np.trace(B)                             # (B) correct: the trace is linear
lam = 1 + np.sqrt(6)
v = np.array([2.0, lam - 1.0])                            # (C) (A − λI) v = 0: −√6 v₀ + 2 v₁ = 0
p = np.prod(np.linalg.eigvals(A))                         # (D) correct
r = (x @ A @ x) / (x @ x)                                 # (F) correct
answer_M12c_34b = [float(d), float(t), float(v[1] / v[0]), float(np.real(p)), float(r)]
try:
    np.linalg.cholesky(C)
    answer_M12c_34c = False
except np.linalg.LinAlgError:
    answer_M12c_34c = True
print(answer_M12c_34a, np.round(answer_M12c_34b, 4).tolist(), answer_M12c_34c)
print("what (C) returns:", np.linalg.solve(A - lam * np.eye(2), np.zeros(2)).tolist(),
      " what (E) returns:", np.linalg.cholesky(C).tolist())''',
    record=f'''wbm.record("M12c.34a", "ACE",
           mistakes={M12C_34_MISTAKES})
VALUES_34 = [-8.0, 3.0, float(np.sqrt(6) / 2), -5.0, 3.5]
wbm.record("M12c.34b", VALUES_34, decimals=4,
           mistakes={{"(A) : le déterminant n'est pas additif, calcule det(A + B)": [-7.0] + VALUES_34[1:],
                      "(C) : un vecteur propre n'est jamais nul ; résous (A − λI) v = 0 à la main": VALUES_34[:2] + [0.0] + VALUES_34[3:]}})
wbm.record("M12c.34c", False,
           mistakes={{"np.linalg.cholesky ne vérifie pas la symétrie : elle ne lit que le triangle inférieur": True}})''',
    note=r"(A) $\det(\mathbf{A} + \mathbf{B}) = \det\begin{pmatrix} 3 & 2 \\ 4 & 0 \end{pmatrix} = -8$, et non "
         r"$-5 + (-2) = -7$. (C) $\mathbf{A} - \lambda\mathbf{I}$ est singulière en théorie, mais l'arrondi de $\lambda$ la "
         r"rend inversible : `solve` rend la seule solution, $\mathbf{0}$ ; un vecteur propre nul doit toujours alerter. "
         r"Le bon vecteur vérifie $-\sqrt{6}\,v_0 + 2v_1 = 0$ : $v_1/v_0 = \sqrt{6}/2$. (E) `cholesky` ne lit que le triangle "
         r"inférieur : elle factorise $\begin{pmatrix} 4 & -2 \\ -2 & 5 \end{pmatrix}$ sans rien dire, alors que $\mathbf{C}$, "
         r"non symétrique, n'a pas de décomposition de Cholesky. C'est la plus dangereuse : aucune erreur, un résultat "
         r"plausible. (B), (D) et (F) sont justes : $3$, $(1 + \sqrt{6})(1 - \sqrt{6}) = -5$ et $\frac{7}{2}$.",
)

M12C_35_GIVEN = '''import sympy

M35_DIAG = sympy.Matrix([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
M35_DEFECTIVE = sympy.Matrix([[2, 0, 1], [1, 3, 1], [1, 0, 2]])
lam = sympy.symbols("lambda")'''

M12C_35_CHECK = '''with checked("M12c.35 vérifications"):
    problems_35 = []
    if sympy.expand(charpoly_35 - (M35_DIAG - lam * sympy.eye(3)).det()) != 0:
        problems_35.append("charpoly_35 doit être det(M − λI), en fonction du symbole lam")
    if sorted(eigenvalues_35, key=lambda e: float(e)) != sorted(sympy.roots(charpoly_35, lam).keys(), key=lambda e: float(e)):
        problems_35.append("eigenvalues_35 : les trois racines exactes du polynôme caractéristique (sympy.solve ou .eigenvals())")
    if P_35 is None or D_35 is None or sympy.simplify(P_35 * D_35 * P_35.inv() - M35_DIAG) != sympy.zeros(3):
        problems_35.append("P_35 et D_35 : M35_DIAG.diagonalize() rend (P, D) avec M = P D P⁻¹")
    if defective_35 is not False:
        problems_35.append("defective_35 : M35_DEFECTIVE.is_diagonalizable()")
    if problems_35:
        print("❌ Ex M12c.35 : à revoir : " + " ; ".join(problems_35) + ".")
    else:
        print("✅ Ex M12c.35 : polynôme caractéristique, valeurs propres exactes, diagonalisation et cas défectif vérifiés.")'''

M12C_35 = Ex(
    "M12c.35", "🛠️", 1, 15, "Vérifier avec SymPy : polynôme caractéristique, valeurs propres exactes, diagonalisation",
    "vérifier un calcul de valeurs propres et une diagonalisation avec SymPy, en valeurs exactes, et reconnaître une "
    "matrice défective.", "fiche §3 et §4 ; R0 (SymPy)", tracks="C", given=M12C_35_GIVEN,
    body=r"""SymPy calcule en valeurs **exactes** : racines carrées et fractions restent écrites telles quelles, ce qui permet de vérifier un calcul papier sans arrondi. Avec les deux matrices fournies, écris :
- `charpoly_35` : le polynôme caractéristique $\det(\mathbf{M} - \lambda\mathbf{I})$ de `M35_DIAG`, en fonction du symbole `lam` (`(M35_DIAG - lam * sympy.eye(3)).det()`, puis `sympy.factor` pour le lire) ;
- `eigenvalues_35` : la liste de ses trois valeurs propres exactes (`sympy.solve(charpoly_35, lam)`, ou `M35_DIAG.eigenvals()`) ;
- `P_35, D_35` : la diagonalisation `M35_DIAG.diagonalize()` ;
- `defective_35` : `M35_DEFECTIVE.is_diagonalizable()`.

La cellule de vérification contrôle tes quatre résultats (✅ ou ❌, sans `wbm.check`).

Dans ta copie : écris les valeurs propres exactes de `M35_DIAG`, et vérifie que leur somme et leur produit sont la trace et le déterminant. Que rend `M35_DEFECTIVE.eigenvects()`, et pourquoi la matrice n'est-elle pas diagonalisable ? Pourquoi ne faut-il pas utiliser SymPy pour une matrice $100 \times 100$ ?""",
    todo='''charpoly_35 = ...     # the characteristic polynomial of M35_DIAG, in lam
eigenvalues_35 = ...  # a list of 3 exact eigenvalues
P_35 = D_35 = None    # the diagonalization of M35_DIAG
defective_35 = ...    # M35_DEFECTIVE.is_diagonalizable()''',
    check=M12C_35_CHECK,
    solution='''charpoly_35 = (M35_DIAG - lam * sympy.eye(3)).det()
eigenvalues_35 = sympy.solve(charpoly_35, lam)
P_35, D_35 = M35_DIAG.diagonalize()
defective_35 = M35_DEFECTIVE.is_diagonalizable()
print("charpoly:", sympy.factor(charpoly_35), " eigenvalues:", eigenvalues_35)
print("D:", D_35.tolist(), " defective is diagonalizable:", defective_35, " eigenvects:", M35_DEFECTIVE.eigenvects())

''' + M12C_35_CHECK,
    note=r"$\det(\mathbf{M} - \lambda\mathbf{I}) = (2 - \lambda)\big((2 - \lambda)^2 - 2\big)$ : valeurs propres $2$ et "
         r"$2 \pm \sqrt{2}$, de somme 6 (la trace) et de produit $2 \times (4 - 2) = 4$ (le déterminant). La matrice défective "
         r"a la valeur propre 3 double, mais $\mathbf{M} - 3\mathbf{I}$ est de rang 2 : un seul vecteur propre, $(0, 1, 0)$. "
         r"SymPy calcule en exact : pour une grande matrice, les expressions explosent ; on prend NumPy.",
)

M12C_36_GIVEN = '''def make_spectrum_matrix(seed, n=300):
    """A symmetric positive semi-definite (n, n) matrix, of eigenvalues 10, 8, 6.5 and n − 3 others in [0, 5]."""
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    values = np.concatenate([[10.0, 8.0, 6.5], rng.uniform(0.0, 5.0, size=n - 3)])
    A = (Q * values) @ Q.T
    return (A + A.T) / 2'''

M12C_36_CHECK = '''with checked("M12c.36 défi"):
    problems, ok_36 = [], False
    for seed_t in (36, 37, 38):
        A_t = make_spectrum_matrix(seed_t)
        expected = np.linalg.eigvalsh(A_t)[::-1][:3]
        try:
            got = np.asarray(top_three(A_t.copy()), dtype=float)
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"top_three lève {type(exc).__name__} ({exc})")
            break
        if got.shape != (3,):
            problems.append(f"matrice {seed_t} : top_three rend la forme {got.shape}, pas (3,)")
            break
        gap = float(np.max(np.abs(got - expected)))
        print(f"matrice {seed_t} : {np.round(got, 8).tolist()}, écart à eigvalsh {gap:.1e}")
        if not gap <= 1e-6:
            problems.append(f"matrice {seed_t} : écart {gap:.1e} à eigvalsh, au-dessus de 1e-6")
            break
    if problems:
        print("❌ Ex M12c.36 : " + " ; ".join(problems) + ".")
    else:
        ok_36 = True
        print("✅ Ex M12c.36 : défi réussi : les trois plus grandes valeurs propres à moins de 1e-6, sur les trois matrices.")'''

M12C_36 = Ex(
    "M12c.36", "🏆", 3, 30, "Défi : les trois plus grandes valeurs propres d'une matrice symétrique semi-définie "
    "positive 300 × 300, par la puissance avec déflation, à 1e−6 près",
    "trouver les plus grandes valeurs propres d'une grande matrice symétrique avec des produits matrice-vecteur "
    "seulement, par la méthode de la puissance et la déflation.", "fiche §5 et §6 ; Ex M12c.27 et M12c.32", tracks="C",
    given=M12C_36_GIVEN,
    body=r"""La fonction fournie `make_spectrum_matrix(seed)` fabrique une matrice symétrique semi-définie positive $300 \times 300$, dont les trois plus grandes valeurs propres valent 10, 8 et 6,5, et les 297 autres sont entre 0 et 5 (tu ne connais pas ses vecteurs propres).

**L'objectif** : écrire `top_three(A)`, qui rend la liste de ses trois plus grandes valeurs propres, par ordre décroissant, à moins de $10^{-6}$ de celles de `np.linalg.eigvalsh` sur les trois matrices `seed` = 36, 37 et 38, **sans** `np.linalg.eigh`, `eigvalsh`, `eig`, `eigvals`, `svd`, ni `scipy`. Une dernière cellule enregistre si l'objectif est atteint.

Pistes (fiche §5 et §6) : la méthode de la puissance (ta fonction `power_iteration`, ou ta propre boucle) donne $\lambda_1$ et $\mathbf{q}_1$ ; la **déflation** $\mathbf{A} \leftarrow \mathbf{A} - \lambda_1\mathbf{q}_1\mathbf{q}_1^\top$ (produit extérieur : `np.outer`) remplace $\lambda_1$ par 0 sans changer les autres ; recommence. Pense au point de départ (pas orthogonal au vecteur cherché) et au nombre d'itérations : quel est le rapport $|\lambda_2/\lambda_1|$ à chaque étape ?

Dans ta copie : combien d'itérations demande chaque étape, et pourquoi la deuxième est-elle la plus lente ? Pourquoi la déflation ne marcherait-elle pas telle quelle sur une matrice non symétrique ? Comment trouverais-tu la plus **petite** valeur propre avec la même méthode (indice : $c\mathbf{I} - \mathbf{A}$) ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12c")


def top_three(A):
    """The three largest eigenvalues of the symmetric positive semi-definite matrix A, in decreasing order."""
    raise NotImplementedError("la puissance, puis la déflation A − λ q qᵀ, trois fois")''',
    check=M12C_36_CHECK + '''
with checked("M12c.36"):
    top_three(make_spectrum_matrix(36))         # ⏳ while top_three is not written
    wbm.check("M12c.36", bool(ok_36), computed=True)''',
    solution=LOAD_REF + '''


def top_three(A):
    """The three largest eigenvalues of the symmetric positive semi-definite matrix A, in decreasing order."""
    A = np.array(A, dtype=float)
    start = np.random.default_rng(0).normal(size=A.shape[0])     # a random start: not orthogonal to q₁
    values = []
    for _ in range(3):
        value, vector, iterations = mymath.eigen.power_iteration(A, x0=start, n_iter=5000)
        values.append(value)
        A = A - value * np.outer(vector, vector)                  # deflation: λ is replaced by 0
    return values


print([round(v, 8) for v in top_three(make_spectrum_matrix(36))])''',
    after=[("solution", M12C_36_CHECK)],
    record='''wbm.record("M12c.36", True,
           mistakes={"l'objectif n'est pas atteint sur les trois matrices : la cellule du défi dit pourquoi": False})''',
    note=r"Les rapports successifs sont $8/10 = 0{,}8$, $6{,}5/8 \approx 0{,}81$ et environ $5/6{,}5 \approx 0{,}77$ (la "
         r"plus grande des valeurs restantes est proche de 5) : quelques dizaines à une centaine d'itérations par étape "
         r"pour le vecteur, et la valeur propre d'une matrice symétrique converge deux fois plus vite. Pour une matrice "
         r"non symétrique, $\mathbf{A} - \lambda_1\mathbf{v}_1\mathbf{v}_1^\top$ ne garde pas les autres vecteurs propres "
         r"(ils ne sont pas orthogonaux à $\mathbf{v}_1$). La plus petite valeur propre : la plus grande de "
         r"$c\mathbf{I} - \mathbf{A}$ avec $c \ge \lambda_{\max}$, ou la méthode appliquée à $\mathbf{A}^{-1}$ (itération inverse).",
)

PART_A = Part("A", "Ta librairie : déterminant, puissance, Cholesky, racine carrée et blanchiment ; NumPy",
              "Fiche §1, §5 à §8. Les sept fonctions de `mymath/eigen.py`, puis les mêmes calculs avec NumPy et SciPy.",
              given=TOOLS, exercises=[M12C_26, M12C_27, M12C_28, M12C_29, M12C_30])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §5 à §7. La méthode de la puissance quand les valeurs propres sont proches, sa vitesse, et les "
              "lignes de niveau des formes quadratiques.",
              exercises=[M12C_31, M12C_32, M12C_33])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §1, §3 à §7. Trois erreurs à trouver, une vérification avec SymPy, puis les trois plus grandes "
              "valeurs propres d'une grande matrice.",
              exercises=[M12C_34, M12C_35, M12C_36])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M12c.1 à M12c.13, M12c.20, M12c.21 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M12c · Valeurs propres et matrices symétriques — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m12c_valeurs_propres/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M12c`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M12c · Valeurs propres et matrices symétriques — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : déterminants, valeurs et vecteurs propres, diagonalisation et "
               "puissances, matrices défectives et rotations, théorème spectral, quotient de Rayleigh, méthode de la "
               "puissance, matrices définies positives et hessienne, Cholesky, formes quadratiques, covariance "
               "transformée et blanchiment.\n"
               "- Écrire les sept fonctions de `mymath/eigen.py` et les tester, puis comparer avec NumPy et SciPy.\n"
               "- Prédire et mesurer la vitesse de la méthode de la puissance, dessiner des formes quadratiques, chasser "
               "des erreurs, vérifier avec SymPy, trouver les plus grandes valeurs propres d'une grande matrice.\n\n"
               r"**Rappel express.** $\det$ : volume orienté, $\det(\mathbf{A}\mathbf{B}) = \det\mathbf{A}\det\mathbf{B}$, "
               r"$\det\mathbf{A} \ne 0 \iff$ inversible ; $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}"
               r"(\mathbf{B}\mathbf{A})$ ; $\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$, $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$, "
               r"$\sum\lambda_i = \operatorname{tr}\mathbf{A}$, $\prod\lambda_i = \det\mathbf{A}$ ; $\mathbf{A} = "
               r"\mathbf{P}\mathbf{D}\mathbf{P}^{-1}$, $\mathbf{A}^k = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$ ; puissance : "
               r"$\mathbf{x} \leftarrow \mathbf{A}\mathbf{x}/\lVert \mathbf{A}\mathbf{x} \rVert$, vitesse $|\lambda_2/\lambda_1|$ ; "
               r"symétrique : $\mathbf{A} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$, $\lambda_{\min} \le R(\mathbf{x}) \le "
               r"\lambda_{\max}$ ; définie positive $\iff$ $\lambda_i > 0$ $\iff$ $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$ ; "
               r"$\operatorname{Cov}(\mathbf{A}\mathbf{x}) = \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top$ ; blanchir : "
               r"$\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top = \mathbf{I}$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu calculer un déterminant et l'interpréter comme un volume orienté ?\n"
               "2. Sais-tu calculer les valeurs et vecteurs propres d'une petite matrice, et diagonaliser ?\n"
               "3. Sais-tu appliquer le théorème spectral et le quotient de Rayleigh à une matrice symétrique ?\n"
               "4. Sais-tu programmer et régler la méthode de la puissance ?\n"
               "5. Sais-tu reconnaître une matrice définie positive, calculer sa décomposition de Cholesky, et blanchir "
               "une covariance ?\n\n"
               "**La suite** : M12d, la SVD et l'analyse en composantes principales, puis le chapitre 12 de workbookIA "
               "(préparation des données).")]


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
