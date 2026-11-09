#!/usr/bin/env python
"""Build the two notebooks of chapter M12a from a single source (used by Claude).

    python tools/chapters/build_m12a.py
    python tools/run_all_notebooks.py chapitres/m12a_espaces_vectoriels/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m12a_espaces_vectoriels/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M12a.1 to M12a.13, 🔗 M12a.20 and M12a.21); parts A to C are the notebook
exercises. Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it. The
matrices are new: none is a test case of tests/test_m12a_linmaps.py, an example of the fiche or of a docstring of
linmaps.py, a matrix of M09a or M09b, or an example of workbookIA 0B, 12, 15 and 17 (no one-hot of a weather or of
penguins, no column 2, 4, 9, no min-max or z-score, no fitted line brought back, no [[3, 1], [1, 3]] nor
[[1, r], [r, 1]], no network collapsed to one layer).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M12a"
FOLDER = "chapitres/m12a_espaces_vectoriels"

PIVOT_SIGN = "pour la colonne libre j : x_j = 1, et x_p = −R[i, j] pour le pivot de la ligne i (le signe moins)"
FROM_ONE = "les colonnes se numérotent à partir de 1"
ORDER = "garde l'ordre de l'énoncé : le premier nombre multiplie le premier vecteur"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M12a.1", "Reconnaître des sous-espaces de ℝ³ et de l'espace des polynômes", [
        ("a", "True or False", "True",
         '''mistakes={"teste les trois conditions : (0, 0, 0) vérifie-t-il l'équation ? et la somme de deux solutions ?": '''
         '''False}'''),
        ("b", "True or False", "False", '''mistakes={"teste d'abord le vecteur nul": True}'''),
        ("c", "True or False", "True",
         '''mistakes={"U₃ est formé des multiples d'un même vecteur : vérifie les trois conditions sur cette écriture": '''
         '''False}'''),
        ("d", "True or False", "False",
         '''mistakes={"cherche deux vecteurs de U₄ dont la somme n'y est pas (essaie des vecteurs faits de 0 et de 1)": '''
         '''True}'''),
        ("e", "True or False", "False", '''mistakes={"multiplie un vecteur de U₅ par −1": True}'''),
        ("f", "True or False", "True",
         '''mistakes={"si P(1) = 0 et Q(1) = 0, que vaut (λP + μQ)(1) ?": False}'''),
        ("g", "True or False", "False", '''mistakes={"le polynôme nul vérifie-t-il la condition ?": True}'''),
        ("h", "a list of 3 numbers", "[4, -2, 6]",
         '''mistakes={"la première coordonnée est 2t, pas t : trouve d'abord t": [8, -4, 12]}'''),
    ]),

    Paper("M12a.2", "Écrire un vecteur comme combinaison linéaire : un système à résoudre", [
        ("a", "a list of 2 numbers", "coords([U1_2, U2_2], B_2)", f'''mistakes={{"{ORDER}": [-1, 2]}}'''),
        ("b", "True or False", "False",
         '''mistakes={"résous avec deux équations, puis vérifie la troisième avec les nombres trouvés": True}'''),
        ("c", "a number", "1",
         '''mistakes={"la deuxième coordonnée de λ₁u₁ + λ₂u₂ est −λ₁ : attention au signe": -1}'''),
        ("d", "a list of 3 numbers", "[3 * x for x in kernel([U1_2, U2_2])[0]]",
         '''mistakes={"n doit vérifier n · u₁ = 0 et n · u₂ = 0 : vérifie les deux produits scalaires": [1, -5, 3]}'''),
        ("e", "True or False", "True",
         '''mistakes={"b combine u₁ et u₂ (question a) : u₂ combine-t-il u₁ et b ?": False}'''),
        ("f", "an integer", "1", '''mistakes={"on demande le nombre de vecteurs à ajouter, pas le total": 3}'''),
    ]),

    Paper("M12a.3", "L'indépendance de trois vecteurs de ℝ³ par le pivot de Gauss", [
        ("a", "an integer", "rank(np.column_stack([V1_3, V2_3, V3_3]))",
         '''mistakes={"fais le pivot de Gauss jusqu'au bout : une ligne peut s'annuler": 3}'''),
        ("b", "True or False", "False", '''mistakes={"compare le rang au nombre de vecteurs": True}'''),
        ("c", "a list of 2 numbers", "coords([V1_3, V2_3], V3_3)", f'''mistakes={{"{ORDER}": [-1, 2]}}'''),
        ("d", "a list of 3 numbers", "kernel(np.column_stack([V1_3, V2_3, V3_3]))[0]",
         '''mistakes={"avec x₃ = 1, recalcule x₁v₁ + x₂v₂ + v₃ : il doit valoir 0": [2, -1, 1]}'''),
        ("e", "a number", "-7",
         '''mistakes={"(1, 0, k) doit combiner v₁ et v₂ : trouve les coefficients avec les deux premières coordonnées, '''
         '''puis calcule la troisième": 7}'''),
        ("f", "True or False", "rank(np.column_stack([V1_3, V2_3, [2, 3, -4]])) == 3",
         '''mistakes={"calcule le rang de la nouvelle famille : le troisième vecteur a changé": False}'''),
    ]),

    Paper("M12a.4", "Extraire une base d'une famille génératrice, compléter une famille libre", [
        ("a", "an integer", "rank(A_4)",
         '''mistakes={"compte les pivots, pas les vecteurs : deux d'entre eux sont redondants": 5}'''),
        ("b", "a list of integers", "[p + 1 for p in sympy.Matrix(A_4).rref()[1]]",
         f'''mistakes={{"{FROM_ONE}": [0, 2, 4], "garde les colonnes qui portent un pivot, pas les premières": [1, 2, 3]}}'''),
        ("c", "a list of 2 numbers", "coords([A_4[:, 0], A_4[:, 2]], A_4[:, 3])"),
        ("d", "an integer", "rank(A_4[:, :4])",
         '''mistakes={"la dimension compte les vecteurs libres, pas tous les vecteurs": 4}'''),
        ("e", "a list of 2 numbers", "coords([U_4, V_4], [1, 0, 0])", f'''mistakes={{"{ORDER}": [-2, 1]}}'''),
        ("f", "an integer", "next(j + 1 for j in range(3) if rank(np.column_stack([U_4, V_4, np.eye(3, dtype=int)[:, j]])) == 3)",
         '''mistakes={"relis e) : un vecteur de Vect(u, v) ne complète pas la famille": 1}'''),
    ]),

    Paper("M12a.5", "Les coordonnées d'un vecteur dans une base qui n'est pas la base canonique", [
        ("a", "a list of 3 numbers", "coords(list(B_5.T), [1, 4, -1])",
         '''mistakes={"les vecteurs de base sont les colonnes de B : résous B c = v, pas Bᵀ c = v": '''
         '''exact(sympy.Matrix(B_5.T.tolist()).solve(sympy.Matrix([1, 4, -1])))}'''),
        ("b", "a list of 3 numbers", "(B_5 @ np.array([2, -1, 1])).tolist()",
         '''mistakes={"le vecteur est 2b₁ − b₂ + b₃ : B fois les coordonnées": '''
         '''exact(sympy.Matrix(B_5.tolist()).solve(sympy.Matrix([2, -1, 1])))}'''),
        ("c", "a list of 3 numbers (1 decimal)", "[float(x) for x in coords(list(B_5.T), [1, 0, 0])]", "decimals=1"),
        ("d", "a list of 2 numbers", "coords([P1_5, P2_5], [2, 7, -3])", '''mistakes={"l'ordre de la base : p₁, puis p₂": [3, 2]}'''),
        ("e", "True or False", "False",
         '''mistakes={"trouve les coefficients avec deux coordonnées, puis vérifie la troisième": True}'''),
        ("f", "a list of 3 numbers", "coords([B_5[:, 2], B_5[:, 0], B_5[:, 1]], [1, 4, -1])",
         '''mistakes={"dans la base (b₃, b₁, b₂), la première coordonnée est celle de b₃": coords(list(B_5.T), [1, 4, -1])}'''),
    ]),

    Paper("M12a.6", "Le rang par les colonnes et par les lignes, celui d'un produit, et celui d'un tableau centré", [
        ("a", "an integer", "rank(A_6)", '''mistakes={"cherche une ligne qui combine les autres": 3}'''),
        ("b", "an integer", "rank(A_6.T)", '''mistakes={"le rang de la transposée est celui de la matrice": 3}'''),
        ("c", "an integer", "rank(A_6.T @ A_6)",
         '''mistakes={"rg(AᵀA) = rg(A), même si AᵀA a la forme (4, 4)": 4}'''),
        ("d", "an integer", "rank(C_6)"),
        ("e", "an integer", "rank(A_6 @ C_6)",
         '''mistakes={"min(rg A, rg C) n'est qu'une borne : calcule A fois chaque colonne de C": 2}'''),
        ("f", "an integer", "rank(X_6)"),
        ("g", "an integer", "rank(3 * X_6 - X_6.sum(axis=0))",   # 3 X_c, of the same rank, in integers
         '''mistakes={"centrer rend les lignes liées : leur somme est nulle": 3}'''),
    ]),

    Paper("M12a.7", "La matrice d'une application linéaire : les images des vecteurs de base", [
        ("a", "a matrix", "F_7.tolist()",
         '''mistakes={"la colonne j est f(e_j) : une ligne par coordonnée d'arrivée, une colonne par coordonnée de départ": '''
         '''F_7.T.tolist()}'''),
        ("b", "a list of 2 numbers", "F_7[:, 1].tolist()"),
        ("c", "a list of 2 numbers", "(F_7 @ np.array([2, 1, -1])).tolist()"),
        ("d", "a list of 2 integers", "[2, 5]", '''mistakes={"la forme est (lignes, colonnes) = (arrivée, départ)": [5, 2]}'''),
        ("e", "a matrix", "G_7.tolist()",
         '''mistakes={"les colonnes sont g(e₁) et g(e₂), pas g(1, 1) et g(1, −1)": [[3, 1], [1, -3]], '''
         '''"g(e_j) se range dans la colonne j, pas dans la ligne j": G_7.T.tolist()}'''),
        ("f", "a matrix (1 decimal)", "[[0.5, 0.5], [0.5, 0.5]]",
         '''decimals=1, mistakes={"projeter e₁ sur la droite dirigée par u = (1, 1) : (e₁ · u / ‖u‖²) u": '''
         '''[[1.0, 1.0], [1.0, 1.0]]}'''),
        ("g", "True or False", "False", '''mistakes={"une application linéaire envoie 0 sur 0": True}'''),
    ]),

    Paper("M12a.8", "Composer deux applications du plan, c'est multiplier leurs matrices", [
        ("a", "a matrix", "(B_8 @ A_8).tolist()",
         '''mistakes={"« a, puis b » a pour matrice BA : la dernière appliquée à gauche": (A_8 @ B_8).tolist()}'''),
        ("b", "a matrix", "(A_8 @ B_8).tolist()",
         '''mistakes={"« b, puis a » a pour matrice AB : la dernière appliquée à gauche": (B_8 @ A_8).tolist()}'''),
        ("c", "a list of 2 numbers", "(B_8 @ A_8 @ np.array([1, 1])).tolist()",
         '''mistakes={"applique a d'abord, puis b": (A_8 @ B_8 @ np.array([1, 1])).tolist()}'''),
        ("d", "True or False", "False", '''mistakes={"compare les matrices de a) et de b)": True}'''),
        ("e", "a matrix", "(B_8 @ B_8).tolist()"),
        ("f", "a matrix", "matrix(sympy.Matrix(B_8.tolist()).inv())",
         '''mistakes={"l'inverse défait le cisaillement : vérifie que B fois ta matrice donne I": [[1, 2], [0, 1]]}'''),
        ("g", "a matrix (4 decimals)", "matrix(sympy.Matrix((A_8 @ B_8).tolist()).inv())",
         '''decimals=4, mistakes={"(AB)⁻¹ = B⁻¹A⁻¹ : l'ordre s'inverse": '''
         '''matrix(sympy.Matrix(A_8.tolist()).inv() * sympy.Matrix(B_8.tolist()).inv())}'''),
    ]),

    Paper("M12a.9", "Noyau et image d'une matrice 3 × 4, et le théorème du rang", [
        ("a", "an integer", "rank(A_9)"),
        ("b", "a list of integers", "[p + 1 for p in sympy.Matrix(A_9).rref()[1]]", f'''mistakes={{"{FROM_ONE}": [0, 1]}}'''),
        ("c", "an integer", "A_9.shape[1] - rank(A_9)",
         '''mistakes={"le théorème du rang : dim ker A = nombre de colonnes − rang": 1}'''),
        ("d", "a list of 4 numbers", "kernel(A_9)[0]", f'''mistakes={{"{PIVOT_SIGN}": [-1, 2, 1, 0]}}'''),
        ("e", "a list of 4 numbers", "kernel(A_9)[1]", f'''mistakes={{"{PIVOT_SIGN}": [2, 1, 0, 1]}}'''),
        ("f", "a matrix", "A_9[:, [0, 1]].tolist()",
         '''mistakes={"les colonnes de A, pas celles de la forme réduite": [[1, 0], [0, 1], [0, 0]], '''
         '''"une matrice est une liste de lignes : les colonnes à pivot de A sont les colonnes de ta matrice, de forme (3, 2)": '''
         '''A_9[:, [0, 1]].T.tolist()}'''),
        ("g", "a list of 3 numbers", "kernel(A_9[:, [0, 1]].T)[0]",
         '''mistakes={"n doit être orthogonal aux deux colonnes de f) : vérifie les deux produits scalaires": [-3, 2, 1]}'''),
        ("h", "True or False", "True",
         '''mistakes={"un vecteur est dans l'image quand son produit scalaire avec n est nul": False}'''),
    ]),

    Paper("M12a.10", "Toutes les solutions de A x = b : une solution particulière plus le noyau", [
        ("a", "a list of 4 numbers", "XP_10.tolist()"),
        ("b", "an integer", "A_10.shape[1] - rank(A_10)"),
        ("c", "a list of 4 numbers", "kernel(A_10)[0]", f'''mistakes={{"{PIVOT_SIGN}": [2, -1, 1, 0]}}'''),
        ("d", "a list of 4 numbers", "kernel(A_10)[1]", f'''mistakes={{"{PIVOT_SIGN}": [-1, 3, 0, 1]}}'''),
        ("e", "a list of 4 numbers", "(XP_10 + 2 * K1_10 - K2_10).tolist()",
         '''mistakes={"une solution est x_p + s k₁ + t k₂ : n'oublie pas la solution particulière": '''
         '''(2 * K1_10 - K2_10).tolist()}'''),
        ("f", "True or False", "bool(np.array_equal(A_10 @ np.array([2, 0, 1, 0]), B_10))",
         '''mistakes={"calcule A fois ce vecteur et compare à b": False}'''),
        ("g", "a number", "3",
         '''mistakes={"cherche la relation entre les lignes de A ; le second membre doit vérifier la même": -3}'''),
        ("h", "an integer", "0", '''mistakes={"b doit être dans l'image de A ; sinon, aucune solution": 1}'''),
    ]),

    Paper("M12a.11", "Une base adaptée qui rend diagonale la matrice d'une application : S⁻¹AS", [
        ("a", "a list of 2 numbers", "(A_11 @ S_11[:, 0]).tolist()"),
        ("b", "a list of 2 numbers", "(A_11 @ S_11[:, 1]).tolist()"),
        ("c", "a matrix", "matrix(sympy.Matrix(S_11.tolist()).inv())",
         '''mistakes={"l'inverse 2 × 2 : échange a et d, change le signe de b et de c, divise par ad − bc (ici négatif)": '''
         '''(-np.array(matrix(sympy.Matrix(S_11.tolist()).inv()))).tolist()}'''),
        ("d", "a matrix", "matrix(sympy.Matrix(S_11.tolist()).inv() * sympy.Matrix(A_11.tolist()) * sympy.Matrix(S_11.tolist()))",
         '''mistakes={"S A S⁻¹ n'est pas la matrice dans la nouvelle base : lis S⁻¹AS de droite à gauche": '''
         '''matrix(sympy.Matrix(S_11.tolist()) * sympy.Matrix(A_11.tolist()) * sympy.Matrix(S_11.tolist()).inv())}'''),
        ("e", "a list of 2 numbers", "coords(list(S_11.T), [5, 3])",
         '''mistakes={"les coordonnées sont S⁻¹x, pas Sx": (S_11 @ np.array([5, 3])).tolist()}'''),
        ("f", "a list of 2 numbers", "[2, 6]"),
        ("g", "a list of 2 numbers", "(A_11 @ np.array([5, 3])).tolist()",
         '''mistakes={"revenir à la base canonique : S fois les coordonnées de f)": [2, 6]}'''),
        ("h", "a matrix", "[[3, 0], [0, 2]]", '''mistakes={"l'ordre de la base change l'ordre des colonnes et des lignes": [[2, 0], [0, 3]]}'''),
    ]),

    Paper("M12a.12", "Une application affine du plan : partie linéaire, translation, inverse", [
        ("a", "a matrix", "A_12.tolist()"),
        ("b", "a list of 2 numbers", "B_12.tolist()", '''mistakes={"la translation est φ(0, 0), signes compris": [1, -4]}'''),
        ("c", "a list of 2 numbers", "phi_12([1, -1])"),
        ("d", "a matrix", "matrix(sympy.Matrix(A_12.tolist()).inv())"),
        ("e", "a list of 2 numbers", "exact(-sympy.Matrix(A_12.tolist()).inv() * sympy.Matrix(B_12.tolist()))",
         '''mistakes={"la translation de φ⁻¹ est −A⁻¹b, pas −b": (-B_12).tolist(), '''
         '''"la translation de φ⁻¹ est φ⁻¹(0) = A⁻¹(0 − b) : attention au signe": '''
         '''exact(sympy.Matrix(A_12.tolist()).inv() * sympy.Matrix(B_12.tolist()))}'''),
        ("f", "a list of 2 numbers", "exact(sympy.Matrix(A_12.tolist()).inv() * sympy.Matrix((np.array([3, 4]) - B_12).tolist()))",
         '''mistakes={"φ⁻¹(y) = A⁻¹(y − b) : retire b avant d'appliquer A⁻¹": '''
         '''(np.array(exact(sympy.Matrix(A_12.tolist()).inv() * sympy.Matrix([3, 4]))) - B_12).tolist()}'''),
        ("g", "a list of 2 numbers", "phi_12([1, 1])"),
        ("h", "True or False", "False", '''mistakes={"une application linéaire envoie 0 sur 0 : et φ ?": True}'''),
    ]),

    Paper("M12a.13", "La dérivation sur les polynômes de degré au plus 3 : matrice, noyau, image", [
        ("a", "a matrix", "D_13.tolist()",
         '''mistakes={"la colonne j contient les coordonnées de la dérivée du j-ième vecteur de base": D_13.T.tolist()}'''),
        ("b", "a list of 4 numbers", "[2, -1, 4, 1]",
         '''mistakes={"la base est (1, x, x², x³) : le terme constant d'abord": [1, 4, -1, 2]}'''),
        ("c", "a list of 4 numbers", "(D_13 @ np.array([2, -1, 4, 1])).tolist()"),
        ("d", "an integer", "rank(D_13)", '''mistakes={"compte les pivots : la première colonne de la matrice est nulle": 4}'''),
        ("e", "an integer", "4 - rank(D_13)"),
        ("f", "True or False", "False", '''mistakes={"la dérivée d'un polynôme de degré au plus 3 a quel degré ?": True}'''),
        ("g", "a matrix", "(D_13 @ D_13).tolist()"),
        ("h", "an integer", "next(k for k in range(1, 6) if not np.linalg.matrix_power(D_13, k).any())",
         '''mistakes={"chaque dérivation fait baisser le degré de 1 : combien en faut-il pour annuler x³ ?": 3}'''),
    ]),

    Paper("M12a.20", "Pont : une feature somme de deux autres rend XᵀX singulière, et le noyau dit laquelle", [
        ("a", "an integer", "rank(X_20)", '''mistakes={"une colonne est la somme des deux autres": 3}'''),
        ("b", "an integer", "rank(X_20.T @ X_20)", '''mistakes={"rg(XᵀX) = rg(X)": 3}'''),
        ("c", "a list of 3 numbers", "kernel(X_20)[0]",
         '''mistakes={"le vecteur demandé a sa dernière coordonnée égale à 1": [1, 1, -1]}'''),
        ("d", "an integer", "X_20.shape[1] - rank(X_20.T @ X_20)",
         '''mistakes={"ker(XᵀX) = ker X : un vecteur de c) suffit-il à décrire ce noyau ?": 0}'''),
        ("e", "a list of 4 numbers (1 decimal)", "(X_20 @ (W_20 + 2 * np.array(kernel(X_20)[0]))).tolist()",
         '''decimals=1, mistakes={"w′ = w + 2d : n'oublie pas w dans les poids": [0.0, 0.0, 0.0, 0.0]}'''),
        ("f", "True or False", "True",
         '''mistakes={"les deux colonnes restantes sont-elles libres ?": False}'''),
    ]),

    Paper("M12a.21", "Pont : projeter sur un plan puis revenir, ce que la transformation inverse ne peut pas rendre", [
        ("a", "an integer", "rank(E_21)"),
        ("b", "a list of 3 numbers", "kernel(E_21)[0]", f'''mistakes={{"{PIVOT_SIGN}": [1, -1, 1]}}'''),
        ("c", "a list of 2 numbers", "(E_21 @ np.array([0, 3, 1])).tolist()"),
        ("d", "True or False", "False",
         '''mistakes={"le rang d'un produit est au plus le rang de chaque facteur : et rg(I₃) ?": True}'''),
        ("e", "a matrix", "(D_21 @ E_21).tolist()",
         '''mistakes={"D E : la matrice de « E, puis D », de forme (3, 3)": (E_21 @ D_21).tolist()}'''),
        ("f", "a list of 3 numbers", "(D_21 @ E_21 @ np.array([0, 3, 1])).tolist()"),
        ("g", "a list of 3 numbers", "(np.array([0, 3, 1]) - D_21 @ E_21 @ np.array([0, 3, 1])).tolist()",
         '''mistakes={"l'erreur est x − DEx, dans cet ordre": (D_21 @ E_21 @ np.array([0, 3, 1]) - np.array([0, 3, 1])).tolist()}'''),
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


def rank(M):
    return int(sympy.Matrix(np.asarray(M).tolist()).rank())


def kernel(M):
    """The basis of the kernel given by the reduced form (one vector per free column), as lists."""
    return [exact(v) for v in sympy.Matrix(np.asarray(M).tolist()).nullspace()]


def coords(columns, v):
    """The exact coordinates c with [columns] c = v (independent columns, v in their span)."""
    B = sympy.Matrix(np.column_stack(columns).tolist())
    c = (B.T * B).solve(B.T * sympy.Matrix(list(v)))
    assert B * c == sympy.Matrix(list(v)), "v is not in the span"
    return exact(c)


U1_2, U2_2, B_2 = np.array([1, -1, 2]), np.array([3, 0, 1]), np.array([-1, -2, 3])                    # M12a.2
V1_3, V2_3, V3_3 = np.array([1, 2, -1]), np.array([0, 1, 3]), np.array([2, 3, -5])                    # M12a.3
A_4 = np.column_stack([[1, 0, 2], [2, 0, 4], [0, 1, 1], [1, 1, 3], [1, -1, 0]])                       # M12a.4
U_4, V_4 = np.array([1, 2, -2]), np.array([0, 1, -1])
B_5 = np.column_stack([[1, 0, 1], [1, 1, 0], [0, 1, 1]])                                              # M12a.5
P1_5, P2_5 = np.array([1, 2, 0]), np.array([0, 1, -1])
A_6 = np.array([[1, 2, 0, -1], [2, 4, 1, 1], [3, 6, 1, 0]])                                          # M12a.6
C_6 = np.array([[-2, 1, 1], [1, 0, 0], [0, -3, 0], [0, 1, 0]])
X_6 = np.array([[2, 1, 5], [4, 0, 3], [3, 2, 1]])
F_7 = np.array([[1, -2, 1], [3, 0, 1]])                                                             # M12a.7
G_7 = np.column_stack([(np.array([3, 1]) + np.array([1, -3])) // 2, (np.array([3, 1]) - np.array([1, -3])) // 2])
A_8, B_8 = np.array([[3, 0], [0, 1]]), np.array([[1, 2], [0, 1]])                                    # M12a.8
A_9 = np.array([[1, 1, 1, 3], [2, 1, 0, 5], [1, -1, -3, 1]])                                        # M12a.9
A_10 = np.array([[1, 0, 2, -1], [0, 1, -1, 3], [1, 1, 1, 2]])                                       # M12a.10
B_10 = np.array([4, -1, 3])
XP_10 = np.array([4, -1, 0, 0])
assert np.array_equal(A_10 @ XP_10, B_10)
K1_10, K2_10 = (np.array(k) for k in kernel(A_10))
A_11, S_11 = np.array([[4, -2], [1, 1]]), np.column_stack([[1, 1], [2, 1]])                          # M12a.11
A_12, B_12 = np.array([[2, 3], [1, 2]]), np.array([-1, 4])                                           # M12a.12


def phi_12(x):
    return (A_12 @ np.array(x) + B_12).tolist()


D_13 = np.array([[0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 0]])                          # M12a.13
X_20 = np.array([[12, 30, 42], [25, 15, 40], [8, 50, 58], [20, 20, 40]])                            # M12a.20
W_20 = np.array([0.5, 1, 0])
E_21, D_21 = np.array([[1, 1, 0], [0, 1, -1]]), np.array([[1, -1], [0, 1], [0, 0]])                  # M12a.21'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M12a.1 à M12a.13, 🔗 M12a.20 et M12a.21)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une liste `[0, -2, 5]` pour un vecteur, des numéros de colonnes ou une forme, une liste de lignes "
               "`[[1, 0], [-2, 3]]` pour une matrice, ou `True` / `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M12a.26 to M12a.29)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
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
    return "aucune"'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12a")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/linmaps.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "Une famille de vecteurs est donnée par les **colonnes** d'une matrice (une liste de lignes ou un tableau "
         "NumPy à deux dimensions). NumPy est permis, `@`, `.T` et `np.linalg.solve` compris ; `np.linalg.matrix_rank`, "
         "`svd`, `qr`, `lstsq`, `pinv`, `inv`, `scipy.linalg` et SymPy sont interdits : les tests comparent tes "
         "résultats aux leurs, et un test vérifie que tu ne t'en sers pas. Les pivots viennent de la forme échelonnée "
         "réduite calculée avec pivot partiel et la tolérance `tol` : tu peux recopier ta fonction `rref` de M09a dans "
         "une fonction privée `_rref` du fichier. Ne modifie jamais la matrice reçue : travaille sur une copie, "
         "`np.array(A, dtype=float)`.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError", "LinAlgError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of linmaps.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_linmaps_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m12a_linmaps.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m12a_linmaps.py", "{keyword}", impl="ref")')]


VALUE_ERROR = (f'''mistakes={{"un vecteur n'est pas une matrice : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}}''')

M12A_26 = Ex(
    "M12a.26", "🔨", 2, 20, "Tester l'indépendance et extraire une base de l'espace des colonnes · "
    "`is_independent, column_space_basis`",
    "programmer le test d'indépendance d'une famille et l'extraction d'une base de l'espace des colonnes, par les "
    "colonnes à pivot.", "fiche §2 à §4 ; M09a §6 (`rref`)", tracks="C, E", mymath="linmaps.py",
    body=HOWTO + r"""

Écris (fiche §2 à §4), en suivant les docstrings :
- `is_independent(A, tol=1e-10)` : `True` si les colonnes de $\mathbf{A}$ sont libres, c'est-à-dire si **chaque** colonne porte un pivot ; un `bool` de Python ;
- `column_space_basis(A, tol=1e-10)` : les colonnes **de $\mathbf{A}$** (pas de la forme réduite) dont l'indice porte un pivot, dans l'ordre, en tableau de floats de forme $(m, r)$ ; la forme $(m, 0)$ si $\mathbf{A}$ est nulle.

Les deux lèvent une `ValueError` si $\mathbf{A}$ n'est pas à deux dimensions. Une fonction privée `_rref(A, tol)` qui rend la forme réduite et les colonnes des pivots sert aux deux (et à M12a.27).

La vérification calcule :
- a) `is_independent([[2, 1, 0], [1, -1, 3], [0, 2, 1]])` ;
- b) `is_independent([[1, 2, 4], [0, 1, 1], [3, 1, 7], [2, -1, 3]])` ;
- c) `is_independent([[1, 0, 2], [0, 1, 5]])` ;
- d) `column_space_basis([[1, 2, 4], [0, 1, 1], [3, 1, 7], [2, -1, 3]])` (une matrice) ;
- e) `column_space_basis([[0, 0, 1], [0, 0, 2]])` (une matrice) ;
- f) le nom de l'erreur levée par `is_independent([1, 2])` ;
- g) vrai ou faux : `is_independent` rend un `bool` de Python (`type(...) is bool`).

Dans ta copie : en b), quelle colonne combine les deux autres, et avec quels coefficients ? Pourquoi c) est-il liée sans calcul ? Pourquoi, en e), la première colonne est-elle absente du résultat ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M12a.26a"):
    wbm.check("M12a.26a", mymath.linmaps.is_independent([[2, 1, 0], [1, -1, 3], [0, 2, 1]]), computed=True)
with checked("M12a.26b"):
    wbm.check("M12a.26b", mymath.linmaps.is_independent([[1, 2, 4], [0, 1, 1], [3, 1, 7], [2, -1, 3]]), computed=True)
with checked("M12a.26c"):
    wbm.check("M12a.26c", mymath.linmaps.is_independent([[1, 0, 2], [0, 1, 5]]), computed=True)
with checked("M12a.26d"):
    wbm.check("M12a.26d", np.asarray(mymath.linmaps.column_space_basis(
        [[1, 2, 4], [0, 1, 1], [3, 1, 7], [2, -1, 3]])).tolist(), computed=True)
with checked("M12a.26e"):
    wbm.check("M12a.26e", np.asarray(mymath.linmaps.column_space_basis([[0, 0, 1], [0, 0, 2]])).tolist(),
              computed=True)
with checked("M12a.26f"):
    wbm.check("M12a.26f", raised(mymath.linmaps.is_independent, [1, 2]), computed=True)
with checked("M12a.26g"):
    wbm.check("M12a.26g", type(mymath.linmaps.is_independent([[1, 0], [0, 1]])) is bool, computed=True)''',
    solution=LOAD_REF + '''
is_independent, column_space_basis = mymath.linmaps.is_independent, mymath.linmaps.column_space_basis
print("a)", is_independent([[2, 1, 0], [1, -1, 3], [0, 2, 1]]),
      " b)", is_independent([[1, 2, 4], [0, 1, 1], [3, 1, 7], [2, -1, 3]]),
      " c)", is_independent([[1, 0, 2], [0, 1, 5]]))
print("d)", column_space_basis([[1, 2, 4], [0, 1, 1], [3, 1, 7], [2, -1, 3]]).tolist())
print("e)", column_space_basis([[0, 0, 1], [0, 0, 2]]).tolist())
print("f)", raised(is_independent, [1, 2]), " g)", type(is_independent([[1, 0], [0, 1]])) is bool)''',
    record=f'''wbm.record("M12a.26a", True,
           mistakes={{"trois pivots pour trois colonnes : la famille est libre ; relis le test de ta fonction": False}})
wbm.record("M12a.26b", False,
           mistakes={{"une colonne sans pivot rend la famille liée : compare le nombre de pivots au nombre de colonnes":
                         True}})
wbm.record("M12a.26c", False,
           mistakes={{"plus de vecteurs que de coordonnées : une colonne au moins n'a pas de pivot": True}})
wbm.record("M12a.26d", [[1.0, 2.0], [0.0, 1.0], [3.0, 1.0], [2.0, -1.0]], decimals=6,
           mistakes={{"les colonnes de A elle-même, pas celles de la forme réduite": [[1.0, 0.0], [0.0, 1.0], [0.0, 0.0],
                                                                                     [0.0, 0.0]],
                     "seulement les colonnes qui portent un pivot": [[1.0, 2.0, 4.0], [0.0, 1.0, 1.0], [3.0, 1.0, 7.0],
                                                                     [2.0, -1.0, 3.0]]}})
wbm.record("M12a.26e", [[1.0], [2.0]], decimals=6,
           mistakes={{"une colonne nulle ne porte pas de pivot": [[0.0, 1.0], [0.0, 2.0]]}})
wbm.record("M12a.26f", "ValueError",
           {VALUE_ERROR})
wbm.record("M12a.26g", True,
           mistakes={{"la docstring demande un bool de Python : bool(...), pas un booléen de NumPy": False}})''',
    after=tests_cells("test_is_independent_ or test_column_space_basis_"),
    note=r"a) Trois pivots : libre. b) La troisième colonne vaut deux fois la première plus la deuxième : "
         r"$2(1, 0, 3, 2) + (2, 1, 1, -1) = (4, 1, 7, 3)$ ; deux pivots, la famille est liée, et d) garde les colonnes 1 "
         r"et 2 de $\mathbf{A}$. c) Trois vecteurs de $\mathbb{R}^2$ sont toujours liés. e) Les deux premières colonnes sont "
         r"nulles et ne portent pas de pivot ; seule la troisième, $(1, 2)$, en porte un. "
         r"g) `np.bool_` n'est pas un `bool` de Python : `len(pivots) == n` en est un.",
)

M12A_27 = Ex(
    "M12a.27", "🔨", 2, 25, "Une base du noyau, colonne libre par colonne libre · `null_space_basis`",
    "programmer une base du noyau à partir de la forme échelonnée réduite, avec la convention de SymPy.",
    "fiche §6 ; Ex M12a.26", tracks="C, E", mymath="linmaps.py",
    body=r"""Écris `null_space_basis(A, tol=1e-10)` (fiche §6), en suivant la docstring : réduis $\mathbf{A}$ (ta fonction `_rref`), repère les colonnes **libres** (sans pivot), et, pour chacune, dans l'ordre, construis un vecteur $\mathbf{x}$ de $\mathbb{R}^n$ : $x_j = 1$ pour cette colonne libre $j$, 0 pour les autres colonnes libres, et $x_p = -R_{ij}$ pour le pivot de la ligne $i$, situé dans la colonne $p$. Rends ces vecteurs en **colonnes** d'un tableau de forme $(n, n - r)$ ; la forme $(n, 0)$ quand le noyau est $\{\mathbf{0}\}$ (`np.zeros((n, 0))`). Une `ValueError` si $\mathbf{A}$ n'est pas à deux dimensions.

La vérification calcule :
- a) `null_space_basis([[1, -1, 0, 2], [0, 0, 1, -3]])` (une matrice) ;
- b) `null_space_basis([[2, 4], [1, 2], [3, 6]])` (une matrice) ;
- c) la forme de `null_space_basis(np.eye(3))` (une liste de 2 entiers) ;
- d) `null_space_basis(np.zeros((2, 3)))` (une matrice) ;
- e) la forme de `N = null_space_basis(A)` pour une matrice `A` de forme $(5, 8)$ tirée au hasard (`np.random.default_rng(27)`, loi normale) ;
- f) vrai ou faux : pour ce même `A`, tous les nombres de `A @ N` sont inférieurs à $10^{-10}$ en valeur absolue ;
- g) le nom de l'erreur levée par `null_space_basis([1, 2, 3])`.

Dans ta copie : lis a) comme deux relations entre les colonnes de la matrice. Pourquoi c) a-t-elle zéro colonne, et d) trois ? Que dit le théorème du rang pour e) ?""",
    todo=LOAD_LEARNER,
    check='''A_27 = np.random.default_rng(27).normal(size=(5, 8))
with checked("M12a.27a"):
    wbm.check("M12a.27a", np.asarray(mymath.linmaps.null_space_basis([[1, -1, 0, 2], [0, 0, 1, -3]])).tolist(),
              computed=True)
with checked("M12a.27b"):
    wbm.check("M12a.27b", np.asarray(mymath.linmaps.null_space_basis([[2, 4], [1, 2], [3, 6]])).tolist(),
              computed=True)
with checked("M12a.27c"):
    wbm.check("M12a.27c", list(np.shape(mymath.linmaps.null_space_basis(np.eye(3)))), computed=True)
with checked("M12a.27d"):
    wbm.check("M12a.27d", np.asarray(mymath.linmaps.null_space_basis(np.zeros((2, 3)))).tolist(), computed=True)
with checked("M12a.27e"):
    wbm.check("M12a.27e", list(np.shape(mymath.linmaps.null_space_basis(A_27))), computed=True)
with checked("M12a.27f"):
    wbm.check("M12a.27f", bool(np.all(np.abs(A_27 @ np.asarray(mymath.linmaps.null_space_basis(A_27))) < 1e-10)),
              computed=True)
with checked("M12a.27g"):
    wbm.check("M12a.27g", raised(mymath.linmaps.null_space_basis, [1, 2, 3]), computed=True)''',
    solution=LOAD_REF + '''
null_space_basis = mymath.linmaps.null_space_basis
A_27 = np.random.default_rng(27).normal(size=(5, 8))
print("a)", null_space_basis([[1, -1, 0, 2], [0, 0, 1, -3]]).tolist())
print("b)", null_space_basis([[2, 4], [1, 2], [3, 6]]).tolist(), " c)", null_space_basis(np.eye(3)).shape)
print("d)", null_space_basis(np.zeros((2, 3))).tolist())
N_27 = null_space_basis(A_27)
print("e)", N_27.shape, " f)", bool(np.all(np.abs(A_27 @ N_27) < 1e-10)), " g)", raised(null_space_basis, [1, 2, 3]))''',
    record=f'''wbm.record("M12a.27a", [[1.0, -2.0], [1.0, 0.0], [0.0, 3.0], [0.0, 1.0]], decimals=6,
           mistakes={{"{PIVOT_SIGN}": [[-1.0, 2.0], [1.0, 0.0], [0.0, -3.0], [0.0, 1.0]],
                     "un vecteur par colonne libre, rangé en colonne : le résultat a la forme (n, n − r)":
                         [[1.0, 1.0, 0.0, 0.0], [-2.0, 0.0, 3.0, 1.0]]}})
wbm.record("M12a.27b", [[-2.0], [1.0]], decimals=6, mistakes={{"{PIVOT_SIGN}": [[2.0], [1.0]]}})
wbm.record("M12a.27c", [3, 0],
           mistakes={{"le noyau de l'identité est {{0}} : aucune colonne, mais n = 3 lignes, np.zeros((3, 0))": [0, 3]}})
wbm.record("M12a.27d", [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]], decimals=6)
wbm.record("M12a.27e", [8, 3], mistakes={{"le théorème du rang : n − r colonnes, avec n = 8": [8, 5]}})
wbm.record("M12a.27f", True,
           mistakes={{"A fois chaque vecteur de base doit donner 0 : relis le signe et les colonnes de pivot": False}})
wbm.record("M12a.27g", "ValueError",
           {VALUE_ERROR})''',
    after=tests_cells("test_null_space_basis_"),
    note=r"a) La forme est déjà réduite, avec des pivots dans les colonnes 1 et 3 : les colonnes 2 et 4 sont libres. "
         r"$\mathbf{k}_1 = (1, 1, 0, 0)$ dit « colonne 1 + colonne 2 = 0 », et $\mathbf{k}_2 = (-2, 0, 3, 1)$ dit "
         r"« $-2 \times$ colonne 1 $+ 3 \times$ colonne 3 + colonne 4 = 0 ». b) La seconde colonne est le double de la "
         r"première : $(-2, 1)$. c) L'identité est injective : le noyau est $\{\mathbf{0}\}$, de base vide. d) Toutes les "
         r"colonnes sont libres, et la base est la base canonique. e) Une matrice $(5, 8)$ tirée au hasard est de rang 5 : "
         r"$\dim\ker = 8 - 5 = 3$.",
)

M12A_28 = Ex(
    "M12a.28", "🔨", 1, 20, "Coordonnées dans une base et changement de base · `coordinates, change_of_basis`",
    "programmer le calcul des coordonnées dans une base et la matrice d'une application dans de nouvelles bases.",
    "fiche §3 et §7 ; Ex M12a.26", tracks="C", mymath="linmaps.py",
    body=r"""Écris, en suivant les docstrings :
- `coordinates(B, v, tol=1e-10)` (fiche §3) : les coordonnées $\mathbf{c}$ de $\mathbf{v}$ dans la base formée par les colonnes de $\mathbf{B}$. Vérifie les formes, puis que les colonnes sont libres (`is_independent`), résous $\mathbf{B}^\top\mathbf{B}\,\mathbf{c} = \mathbf{B}^\top\mathbf{v}$ (`np.linalg.solve`), et vérifie que $\mathbf{B}\mathbf{c}$ redonne $\mathbf{v}$, à $\mathrm{tol} \times \max(1, \lVert \mathbf{v} \rVert)$ près : sinon $\mathbf{v}$ n'est pas dans le sous-espace engendré, et c'est une `ValueError` ;
- `change_of_basis(A, S, T=None)` (fiche §7) : la matrice $\mathbf{T}^{-1}\mathbf{A}\mathbf{S}$ ($\mathbf{T} = \mathbf{S}$ par défaut), calculée en résolvant $\mathbf{T}\mathbf{M} = \mathbf{A}\mathbf{S}$, jamais avec une inverse. Une `ValueError` si les formes ne vont pas, ou si $\mathbf{S}$ ou $\mathbf{T}$ est singulière, **même** quand $\mathbf{T}$ est donnée et inversible (`np.linalg.solve(T, A @ S)` ne voit pas une $\mathbf{S}$ singulière : teste-la).

La vérification calcule :
- a) `coordinates([[1, 2], [1, 3]], [5, 7])` (une liste, 6 décimales) ;
- b) `coordinates([[1, 0], [2, 1], [0, 3]], [3, 8, 6])` (une liste, 6 décimales) ;
- c) le nom de l'erreur levée par `coordinates([[1, 0], [2, 1], [0, 3]], [1, 1, 1])` ;
- d) `change_of_basis([[3, 1], [0, 2]], [[1, 1], [0, -1]])` (une matrice, 6 décimales) ;
- e) `change_of_basis([[1, 2, 0], [0, 1, 1]], np.eye(3), [[1, 1], [1, -1]])` (une matrice, 6 décimales) ;
- f) le nom de l'erreur levée par `change_of_basis([[1, 0], [0, 1]], [[2, -6], [-1, 3]])`.

Dans ta copie : vérifie a) en recalculant la combinaison des colonnes. Pourquoi c) lève-t-elle une erreur ? Que remarques-tu en d) sur les colonnes de $\mathbf{S}$ ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M12a.28a"):
    wbm.check("M12a.28a", np.asarray(mymath.linmaps.coordinates([[1, 2], [1, 3]], [5, 7])).tolist(), computed=True)
with checked("M12a.28b"):
    wbm.check("M12a.28b", np.asarray(mymath.linmaps.coordinates([[1, 0], [2, 1], [0, 3]], [3, 8, 6])).tolist(),
              computed=True)
with checked("M12a.28c"):
    wbm.check("M12a.28c", raised(mymath.linmaps.coordinates, [[1, 0], [2, 1], [0, 3]], [1, 1, 1]), computed=True)
with checked("M12a.28d"):
    wbm.check("M12a.28d", np.asarray(mymath.linmaps.change_of_basis([[3, 1], [0, 2]], [[1, 1], [0, -1]])).tolist(),
              computed=True)
with checked("M12a.28e"):
    wbm.check("M12a.28e", np.asarray(mymath.linmaps.change_of_basis([[1, 2, 0], [0, 1, 1]], np.eye(3),
                                                                    [[1, 1], [1, -1]])).tolist(), computed=True)
with checked("M12a.28f"):
    wbm.check("M12a.28f", raised(mymath.linmaps.change_of_basis, [[1, 0], [0, 1]], [[2, -6], [-1, 3]]),
              computed=True)''',
    solution=LOAD_REF + '''
coordinates, change_of_basis = mymath.linmaps.coordinates, mymath.linmaps.change_of_basis
print("a)", coordinates([[1, 2], [1, 3]], [5, 7]).tolist(), " b)", coordinates([[1, 0], [2, 1], [0, 3]], [3, 8, 6]).tolist())
print("c)", raised(coordinates, [[1, 0], [2, 1], [0, 3]], [1, 1, 1]))
print("d)", change_of_basis([[3, 1], [0, 2]], [[1, 1], [0, -1]]).tolist())
print("e)", change_of_basis([[1, 2, 0], [0, 1, 1]], np.eye(3), [[1, 1], [1, -1]]).tolist())
print("f)", raised(change_of_basis, [[1, 0], [0, 1]], [[2, -6], [-1, 3]]))''',
    record=f'''wbm.record("M12a.28a", [1.0, 2.0], decimals=6,
           mistakes={{"les vecteurs de base sont les colonnes de B : B c = v, pas Bᵀ c = v": [8.0, -3.0]}})
wbm.record("M12a.28b", [3.0, 2.0], decimals=6)
wbm.record("M12a.28c", "ValueError",
           mistakes={{"(1, 1, 1) n'est pas dans le plan engendré : vérifie que B c redonne v, et lève une ValueError sinon":
                         "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M12a.28d", [[3.0, 0.0], [0.0, 2.0]], decimals=6,
           mistakes={{"S⁻¹AS, pas SAS⁻¹ : résous S M = A S": [[3.0, 2.0], [0.0, 2.0]]}})
wbm.record("M12a.28e", [[0.5, 1.5, 0.5], [0.5, 0.5, -0.5]], decimals=6,
           mistakes={{"T⁻¹A, pas TA : résous T M = A S": [[1.0, 3.0, 1.0], [1.0, 1.0, -1.0]]}})
wbm.record("M12a.28f", "ValueError",
           mistakes={{"S est singulière : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})''',
    after=tests_cells("test_coordinates_ or test_change_of_basis_"),
    note=r"a) $(1, 2)$ : $1 \times (1, 1) + 2 \times (2, 3) = (5, 7)$. b) $(3, 2)$ : $3 \times (1, 2, 0) + 2 \times (0, 1, 3) "
         r"= (3, 8, 6)$. c) La première coordonnée impose $c_1 = 1$, la deuxième $c_2 = -1$, et la troisième vaudrait alors "
         r"$-3 \ne 1$ : le vecteur n'est pas dans le plan. d) $\mathbf{A}(1, 0) = 3\,(1, 0)$ et $\mathbf{A}(1, -1) = (2, -2) = "
         r"2\,(1, -1)$ : dans la base des colonnes de $\mathbf{S}$, la matrice est diagonale. e) Avec $\mathbf{S} = \mathbf{I}$, "
         r"c'est $\mathbf{T}^{-1}\mathbf{A}$ : les colonnes de $\mathbf{A}$ exprimées dans la base $(1, 1), (1, -1)$ de "
         r"l'arrivée.",
)

P_29 = "[[1, 3, 0, 2], [2, 6, 1, 3], [-1, -3, 2, -4]]"

M12A_29 = Ex(
    "M12a.29", "📦", 1, 15, "`sympy.Matrix.nullspace`, `columnspace` et `rank` contre tes fonctions",
    "faire les mêmes calculs avec SymPy (exact) et NumPy (flottant), lire ce que rend chaque fonction, et comparer "
    "avec ta librairie.", "fiche §4 et §6 ; Ex M12a.26 et M12a.27", tracks="C, E",
    body=r"""En pratique, on ne réécrit pas ces fonctions :
- `sympy.Matrix(A).rank()`, `.nullspace()` et `.columnspace()` calculent **exactement** (avec des fractions) le rang, une base du noyau (une liste de vecteurs colonnes, un par colonne libre, avec la même convention que `null_space_basis`) et une base de l'espace des colonnes (les colonnes à pivot) ;
- `np.linalg.matrix_rank(A)` calcule le rang en virgule flottante, par une autre méthode (la SVD, M12d) ; `scipy.linalg.null_space(A)` rend une base du noyau, mais **orthonormée** (M12b), donc d'autres vecteurs que ceux de SymPy.

Avec $\mathbf{P}$ = `""" + P_29 + r"""`, calcule :
- a) `sympy.Matrix(P).rank()` ;
- b) le nombre de vecteurs que rend `sympy.Matrix(P).nullspace()` ;
- c) le premier de ces vecteurs (une liste) ;
- d) les vecteurs de `sympy.Matrix(P).columnspace()`, côte à côte (une matrice : `sympy.Matrix.hstack(*...)`) ;
- e) vrai ou faux : ta fonction `null_space_basis(P)` donne les mêmes vecteurs que SymPy, à $10^{-9}$ près (calcule-le) ;
- f) `np.linalg.matrix_rank` de la transposée de $\mathbf{P}$.

Dans ta copie : quelles relations entre les colonnes de $\mathbf{P}$ les vecteurs du noyau expriment-ils ? Pourquoi f) donne-t-il le même nombre que a) ?""",
    todo='''answer_M12a_29a = ...  # a) an integer
answer_M12a_29b = ...  # b) an integer
answer_M12a_29c = ...  # c) a list
answer_M12a_29d = ...  # d) a matrix
answer_M12a_29e = ...  # e) True or False, computed with your null_space_basis
answer_M12a_29f = ...  # f) an integer''',
    check='''for letter, answer in zip("abcdef", [answer_M12a_29a, answer_M12a_29b, answer_M12a_29c, answer_M12a_29d,
                                     answer_M12a_29e, answer_M12a_29f]):
    wbm.check(f"M12a.29{letter}", answer)''',
    solution=f'''ref_29 = wbm.load_mymath("ref")
P_29 = sympy.Matrix({P_29})
answer_M12a_29a = int(P_29.rank())
answer_M12a_29b = len(P_29.nullspace())
answer_M12a_29c = [int(x) for x in P_29.nullspace()[0]]
answer_M12a_29d = sympy.Matrix.hstack(*P_29.columnspace()).tolist()
exact_29 = np.array(sympy.Matrix.hstack(*P_29.nullspace()).tolist(), dtype=float)
answer_M12a_29e = bool(np.allclose(ref_29.linmaps.null_space_basis({P_29}), exact_29, rtol=0, atol=1e-9))
answer_M12a_29f = int(np.linalg.matrix_rank(np.array({P_29}).T))
print(answer_M12a_29a, answer_M12a_29b, answer_M12a_29c, answer_M12a_29d, answer_M12a_29e, answer_M12a_29f)''',
    record='''wbm.record("M12a.29a", 2, mistakes={"la colonne 2 est le triple de la colonne 1, et les lignes sont liées": 3})
wbm.record("M12a.29b", 2, mistakes={"le théorème du rang : 4 colonnes moins le rang": 1})
wbm.record("M12a.29c", [-3, 1, 0, 0],
           mistakes={"le premier vecteur correspond à la première colonne libre ; attention au signe": [3, 1, 0, 0]})
wbm.record("M12a.29d", [[1, 0], [2, 1], [-1, 2]],
           mistakes={"columnspace() rend des colonnes de P : mets-les côte à côte, une par colonne": [[1, 2, -1], [0, 1, 2]]})
wbm.record("M12a.29e", True,
           mistakes={"relis ta fonction null_space_basis (M12a.27) : ses tests disent ce qui ne va pas": False})
wbm.record("M12a.29f", 2, mistakes={"le rang de la transposée est celui de la matrice": 3})''',
    note=r"La forme réduite de $\mathbf{P}$ est $\begin{pmatrix} 1 & 3 & 0 & 2 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ : "
         r"pivots dans les colonnes 1 et 3, rang 2. Le noyau a pour base $(-3, 1, 0, 0)$ (colonne 2 = 3 × colonne 1) et "
         r"$(-2, 0, 1, 1)$ (colonne 4 = 2 × colonne 1 − colonne 3). L'espace des colonnes a pour base les colonnes 1 et 3 "
         r"de $\mathbf{P}$, $(1, 2, -1)$ et $(0, 1, 2)$. f) $\operatorname{rg}(\mathbf{P}^\top) = \operatorname{rg}(\mathbf{P})$ : "
         r"la ligne 3 de $\mathbf{P}$ vaut 5 fois la ligne 1 moins 3 fois la ligne 2.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M12a.30 to M12a.32)
# ---------------------------------------------------------------------------
M12A_30_EXPERIMENT = '''rng_30 = np.random.default_rng(30)
M_a = rng_30.normal(size=(4, 6))
M_b = rng_30.normal(size=(5, 2)) @ rng_30.normal(size=(2, 5))
base_c = rng_30.normal(size=(4, 3))
M_c = np.column_stack([base_c, base_c[:, 0] + base_c[:, 1]])
base_d = rng_30.normal(size=(3, 5))
M_d = base_d - base_d.mean(axis=0)
i_e, j_e = np.indices((6, 6))
M_e = (i_e + j_e).astype(float)
for label, M in [("a) normale (4, 6)", M_a), ("b) (5, 2) @ (2, 5)", M_b), ("c) (4, 3) + une somme", M_c),
                 ("d) (3, 5) centrée", M_d), ("e) M[i, j] = i + j", M_e)]:
    print(f"{label:24s} forme {M.shape} → rang {np.linalg.matrix_rank(M)}")'''

M12A_30 = Ex(
    "M12a.30", "🔮", 1, 10, "Prédire le rang : matrices aléatoires, produits, colonnes répétées",
    "prévoir le rang de matrices construites de différentes façons, puis le vérifier.", "fiche §4", tracks="C, E",
    hypothesis=True,
    body=r"""Pour chaque matrice, choisis le numéro de la bonne réponse :
- a) une matrice de forme $(4, 6)$ dont les nombres sont tirés au hasard (loi normale) : (1) rang 4 ; (2) rang 6 ; (3) rang inférieur à 4 ;
- b) le produit d'une matrice aléatoire $(5, 2)$ par une matrice aléatoire $(2, 5)$, de forme $(5, 5)$ : (1) rang 5 ; (2) rang 2 ; (3) rang 4 ;
- c) une matrice aléatoire $(4, 3)$, à laquelle on ajoute une quatrième colonne égale à la somme des deux premières : (1) rang 3 ; (2) rang 4 ; (3) rang 2 ;
- d) une matrice aléatoire $(3, 5)$ (3 exemples, 5 features), centrée colonne par colonne : (1) rang 1 ; (2) rang 3 ; (3) rang 2 ;
- e) la matrice $(6, 6)$ de terme général $m_{ij} = i + j$ : (1) rang 6 ; (2) rang 1 ; (3) rang 2.

**Avant d'exécuter quoi que ce soit**, écris tes cinq prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M12a_30a = ...  # a) 1, 2 or 3, written BEFORE running the experiment below
prediction_M12a_30b = ...  # b) 1, 2 or 3
prediction_M12a_30c = ...  # c) 1, 2 or 3
prediction_M12a_30d = ...  # d) 1, 2 or 3
prediction_M12a_30e = ...  # e) 1, 2 or 3''',
    check='''for letter, prediction in zip("abcde", [prediction_M12a_30a, prediction_M12a_30b, prediction_M12a_30c,
                                       prediction_M12a_30d, prediction_M12a_30e]):
    wbm.check(f"M12a.30{letter}", prediction)''',
    record='''wbm.record("M12a.30a", 1, prediction=True, choices=[1, 2, 3])
wbm.record("M12a.30b", 2, prediction=True, choices=[1, 2, 3])
wbm.record("M12a.30c", 1, prediction=True, choices=[1, 2, 3])
wbm.record("M12a.30d", 3, prediction=True, choices=[1, 2, 3])
wbm.record("M12a.30e", 3, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes cinq prédictions écrites."),
        ("todo", guarded(M12A_30_EXPERIMENT, [f"prediction_M12a_30{letter}" for letter in "abcde"],
                         "⏳ Écris d'abord tes cinq prédictions, puis exécute à nouveau.")),
        ("solution", M12A_30_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : pourquoi une matrice tirée au hasard est-elle (presque sûrement) "
               "de rang plein ? Quelle règle du cours explique b) ? En e), écris chaque ligne comme une combinaison de "
               "deux vecteurs fixes."),
    ],
    note=r"a) Tirée au hasard, une matrice est de rang plein, $\min(4, 6) = 4$ : une relation exacte entre des nombres "
         r"tirés d'une loi continue a une probabilité nulle. b) $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \operatorname{rg}"
         r"(\mathbf{A}) \le 2$, et il vaut 2. c) La colonne ajoutée ne crée aucune direction : rang 3. d) Les trois lignes "
         r"centrées ont une somme nulle : rang $3 - 1 = 2$. e) La ligne $i$ vaut $i\,(1, \ldots, 1) + (1, 2, \ldots, 6)$ : "
         r"toutes les lignes sont des combinaisons de deux vecteurs fixes, rang 2.",
)

M12A_31_GIVEN = '''def make_almost_redundant(k, scale=1.0):
    """A (50, 3) table whose third column is the sum of the first two plus 10**(-k) times some noise, all times scale."""
    rng = np.random.default_rng(31)
    X = rng.normal(size=(50, 2))
    noise = rng.normal(size=50)
    return scale * np.column_stack([X, X[:, 0] + X[:, 1] + 10.0 ** (-k) * noise])


KS_31 = list(range(1, 17))'''

M12A_31_SHOW = '''for scale_t, tol_t in [(1.0, 1e-10), (1e6, 1e-10), (1.0, 1e-6)]:
    numpy_t, pivots_t = rank_table(scale=scale_t, tol=tol_t)
    print(f"échelle {scale_t:g}, tol {tol_t:g}")
    print("   k          :", " ".join(f"{k:2d}" for k in KS_31))
    print("   matrix_rank:", " ".join(f"{r:2d}" for r in numpy_t))
    print("   pivots     :", " ".join(f"{r:2d}" for r in pivots_t))'''

M12A_31 = Ex(
    "M12a.31", "🔬", 2, 20, "Le rang numérique : une colonne presque redondante et le choix de la tolérance",
    "mesurer à partir de quand une relation presque exacte est vue comme exacte, par le pivot de Gauss et par NumPy, et "
    "comprendre le rôle de la tolérance et de l'échelle.", "fiche §4 ; Ex M12a.26", tracks="C",
    body=r"""La fonction fournie `make_almost_redundant(k, scale)` fabrique un tableau de 50 exemples et 3 features dont la troisième colonne vaut la somme des deux premières **plus** $10^{-k}$ fois un bruit, le tout multiplié par `scale`. Pour $k$ petit, les trois colonnes sont libres ; pour $k$ grand, la relation est exacte à la précision des flottants près. Écris :
- `rank_table(scale=1.0, tol=1e-10)` : pour $k = 1, \ldots, 16$ (la liste `KS_31`), deux listes de 16 entiers : le rang du tableau donné par `np.linalg.matrix_rank`, et le nombre de colonnes de `mymath.linmaps.column_space_basis(..., tol=tol)` (ta fonction de M12a.26, avec la tolérance absolue `tol`).

La cellule suivante affiche les deux listes pour trois réglages : l'échelle 1 avec la tolérance $10^{-10}$, l'échelle $10^6$ avec la même tolérance, et l'échelle 1 avec la tolérance $10^{-6}$. Lis-les, puis réponds :
- a) le plus petit $k$ pour lequel `matrix_rank` donne 2, à l'échelle 1 ;
- b) le plus petit $k$ pour lequel tes pivots (tolérance $10^{-10}$) donnent 2, à l'échelle 1 ;
- c) le rang donné par tes pivots pour $k = 16$, à l'échelle $10^6$ (tolérance $10^{-10}$) ;
- d) le rang donné par `matrix_rank` pour $k = 16$, à l'échelle $10^6$ ;
- e) le plus petit $k$ pour lequel tes pivots donnent 2 avec la tolérance $10^{-6}$, à l'échelle 1.

Dans ta copie : lequel des deux rangs est « le bon » pour $k = 12$ ? Pourquoi multiplier tout le tableau par $10^6$ change-t-il le rang de tes pivots, mais pas celui de `matrix_rank` (relis la fiche, §4) ? Des features mesurées avec 4 chiffres significatifs : quelle tolérance choisirais-tu, et sur quel tableau (pense à mettre les colonnes à la même échelle) ?""",
    given=M12A_31_GIVEN,
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12a")


def rank_table(scale=1.0, tol=1e-10):
    """For k in KS_31: the ranks of make_almost_redundant(k, scale) by np.linalg.matrix_rank and by your pivots."""
    raise NotImplementedError("deux listes : np.linalg.matrix_rank, puis column_space_basis(..., tol=tol).shape[1]")''',
    check=f'''with checked("M12a.31 tableaux"):
{chr(10).join("    " + line for line in M12A_31_SHOW.splitlines())}''' + '''

answer_M12a_31a = ...  # a) an integer, read in the tables above
answer_M12a_31b = ...  # b) an integer
answer_M12a_31c = ...  # c) an integer
answer_M12a_31d = ...  # d) an integer
answer_M12a_31e = ...  # e) an integer
for letter, answer in zip("abcde", [answer_M12a_31a, answer_M12a_31b, answer_M12a_31c, answer_M12a_31d,
                                    answer_M12a_31e]):
    wbm.check(f"M12a.31{letter}", answer)''',
    solution=LOAD_REF + '''


def rank_table(scale=1.0, tol=1e-10):
    """For k in KS_31: the ranks of make_almost_redundant(k, scale) by np.linalg.matrix_rank and by your pivots."""
    numpy_ranks, pivot_ranks = [], []
    for k in KS_31:
        X = make_almost_redundant(k, scale)
        numpy_ranks.append(int(np.linalg.matrix_rank(X)))
        pivot_ranks.append(int(mymath.linmaps.column_space_basis(X, tol=tol).shape[1]))
    return numpy_ranks, pivot_ranks


''' + M12A_31_SHOW,
    record='''def first_rank_2(ranks):
    return next(k for k, r in zip(KS_31, ranks) if r == 2)


numpy_1, pivots_1 = rank_table()
numpy_big, pivots_big = rank_table(scale=1e6)
_, pivots_6 = rank_table(tol=1e-6)
wbm.record("M12a.31a", first_rank_2(numpy_1),
           mistakes={"le premier k où matrix_rank donne 2, pas le dernier où il donne 3": first_rank_2(numpy_1) - 1})
wbm.record("M12a.31b", first_rank_2(pivots_1),
           mistakes={"le premier k où tes pivots donnent 2, pas le dernier où ils donnent 3": first_rank_2(pivots_1) - 1})
wbm.record("M12a.31c", pivots_big[-1], mistakes={"lis la ligne des pivots du réglage à l'échelle 1e6, colonne k = 16": 2})
wbm.record("M12a.31d", numpy_big[-1], mistakes={"lis la ligne de matrix_rank du réglage à l'échelle 1e6, colonne k = 16": 3})
wbm.record("M12a.31e", first_rank_2(pivots_6),
           mistakes={"le premier k où tes pivots donnent 2 avec tol = 1e-6": first_rank_2(pivots_6) - 1})''',
    note=r"`matrix_rank` voit la colonne comme libre jusqu'à $k = 13$, et le pivot de Gauss à tolérance absolue $10^{-10}$ "
         r"jusqu'à $k = 10$ : le pivot résiduel vaut environ $10^{-k}$ fois quelques unités, et la tolérance décide. Aucun "
         r"des deux n'est « le bon » : pour $k = 12$, la relation est vraie à $10^{-12}$ près, et c'est la précision des "
         r"données qui dit s'il faut la tenir pour exacte. Multiplié par $10^6$, le tableau garde la même structure, mais "
         r"les erreurs d'arrondi (environ $10^{-16}$ fois la taille des nombres) dépassent $10^{-10}$ : la tolérance "
         r"**absolue** ne voit plus jamais la relation. `matrix_rank` utilise une tolérance **relative** à la taille des "
         r"nombres : son verdict ne dépend pas de l'échelle. Avec des mesures à 4 chiffres significatifs, on met les "
         r"colonnes à la même échelle (chacune divisée par sa norme) et l'on prend une tolérance de l'ordre de $10^{-4}$.",
)

M12A_32_CHECK = '''with checked("M12a.32 vérifications"):
    problems = []
    for M_t, singular_t in [([[1, -2], [-0.5, 1]], True), ([[1.5, 0.5], [-0.5, 1]], False), ([[0, 0], [3, 1]], True)]:
        fig_t, ax_t = plt.subplots()
        try:
            created = drawn(lambda: draw_kernel_and_image(ax_t, M_t))
            labels_t = {line.get_label(): line for line in ax_t.lines}
            polygons_t = [p for p in ax_t.patches if hasattr(p, "get_xy")]
        finally:
            plt.close(fig_t)
        M_arr = np.array(M_t, dtype=float)
        if created:
            problems.append("draw_kernel_and_image ouvre sa propre figure : dessine dans l'axe reçu")
            break
        corners = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)
        if not polygons_t or not np.allclose(np.asarray(polygons_t[0].get_xy(), dtype=float)[:4], corners @ M_arr.T,
                                             atol=1e-9):
            problems.append(f"pour M = {M_t}, le premier polygone n'a pas pour sommets les images de (0, 0), (1, 0), "
                            "(1, 1), (0, 1), dans cet ordre")
            break
        if singular_t:
            if "noyau" not in labels_t or "image" not in labels_t:
                problems.append(f"pour M = {M_t}, il manque une ligne de label « noyau » ou « image »")
                break
            ker_pts = np.column_stack([labels_t["noyau"].get_xdata(), labels_t["noyau"].get_ydata()]).astype(float)
            img_pts = np.column_stack([labels_t["image"].get_xdata(), labels_t["image"].get_ydata()]).astype(float)
            if len(ker_pts) < 2 or np.ptp(ker_pts, axis=0).max() < 1e-9 or not np.allclose(ker_pts @ M_arr.T, 0, atol=1e-9):
                problems.append(f"pour M = {M_t}, les points de la ligne « noyau » ne vérifient pas M x = 0 (ou la "
                                "ligne est réduite à un point)")
                break
            column = M_arr[:, np.argmax(np.abs(M_arr).sum(axis=0))]
            cross = img_pts[:, 0] * column[1] - img_pts[:, 1] * column[0]
            if len(img_pts) < 2 or np.ptp(img_pts, axis=0).max() < 1e-9 or not np.allclose(cross, 0, atol=1e-9):
                problems.append(f"pour M = {M_t}, la ligne « image » n'est pas portée par une colonne de M")
                break
        elif "noyau" in labels_t:
            problems.append(f"pour M = {M_t}, inversible, le noyau est {{0}} : pas de ligne « noyau »")
            break
    if problems:
        print("❌ Ex M12a.32 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M12a.32 : le carré, le noyau et l'image sont justes, pour trois matrices.")'''

M12A_32_FIGURE = '''matrices_32 = [("rang 1", [[1, -2], [-0.5, 1]]), ("inversible", [[1.5, 0.5], [-0.5, 1]])]
fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
try:
    for ax, (name, M) in zip(axes, matrices_32):
        draw_kernel_and_image(ax, M)
        ax.set(title=f"{name} : M = {M}", aspect="equal", xlim=(-3, 3), ylim=(-3, 3))
        if ax.get_legend_handles_labels()[0]:
            ax.legend(loc="lower right", fontsize=8)
except BaseException:
    plt.close(fig)
    raise
plt.show()'''

M12A_32 = Ex(
    "M12a.32", "🎨", 1, 20, "Une application linéaire du plan : l'image du carré unité, et ce qu'elle écrase quand son "
    "noyau n'est pas nul",
    "dessiner l'image du carré unité par une application linéaire du plan, et, quand elle n'est pas inversible, son "
    "noyau, son image et les droites qu'elle écrase en un point.", "fiche §5 et §6 ; M09a.33", tracks="C, E",
    body=r"""Écris `draw_kernel_and_image(ax, M)`, qui trace dans l'axe `ax`, pour une matrice $\mathbf{M}$ de forme $(2, 2)$ :
- l'image du carré unité, de sommets $(0, 0)$, $(1, 0)$, $(1, 1)$, $(0, 1)$ **dans cet ordre**, avec `matplotlib.patches.Polygon` et `ax.add_patch` (le premier polygone de l'axe) ;
- si $\mathbf{M}$ n'est **pas** inversible (rang 1) : le noyau, une droite par l'origine de direction $\mathbf{k}$ (`mymath.linmaps.null_space_basis`, ou à la main), tracée pour $t$ entre $-2$ et $2$ avec `label="noyau"` ; l'image, la droite par l'origine portée par une colonne non nulle de $\mathbf{M}$, tracée avec `label="image"` ; et, pour les trois sommets $(1, 0)$, $(0, 1)$, $(1, 1)$ du carré, le segment $\mathbf{p} + t\,\mathbf{k}$, $t \in [-1, 1]$, en pointillés, avec un point en $\mathbf{M}\mathbf{p}$ ;
- si $\mathbf{M}$ est inversible : aucune ligne de label « noyau ».

La cellule de la figure s'en sert pour une matrice de rang 1 et pour une matrice inversible ; une cellule de vérification essaie ta fonction sur trois matrices, dans des axes neufs. Pour savoir si $\mathbf{M}$ est inversible, regarde la forme de la base du noyau.

Dans ta copie : que devient le carré unité par la matrice de rang 1 ? Pourquoi chaque segment en pointillés est-il envoyé sur un seul point ? Où sont ces points ? Pourquoi aucune matrice ne peut-elle défaire la première transformation (fiche §8) ?""",
    todo='''from matplotlib.patches import Polygon

mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12a")


def draw_kernel_and_image(ax, M):
    """In ax: the image of the unit square (a Polygon), and for a singular M its kernel, its image and three segments."""
    raise NotImplementedError("le carré : Polygon ; puis, si le noyau n'est pas {0}, les lignes « noyau » et « image »")''',
    check='''with checked("M12a.32 figure"):
''' + "\n".join("    " + line for line in M12A_32_FIGURE.splitlines()),
    solution='''from matplotlib.patches import Polygon

''' + LOAD_REF + '''


def draw_kernel_and_image(ax, M):
    """In ax: the image of the unit square (a Polygon), and for a singular M its kernel, its image and three segments."""
    M = np.asarray(M, dtype=float)
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float) @ M.T
    ax.add_patch(Polygon(square, closed=True, facecolor="C0", alpha=0.35, edgecolor="C0"))
    ax.axhline(0, color="0.7", lw=0.6)
    ax.axvline(0, color="0.7", lw=0.6)
    N = mymath.linmaps.null_space_basis(M)
    if N.shape[1] == 0:                                    # invertible: the kernel is {0}
        return
    k = N[:, 0]
    t = np.array([-2.0, 2.0])
    ax.plot(t * k[0], t * k[1], color="C3", lw=2, label="noyau")
    column = M[:, np.argmax(np.abs(M).sum(axis=0))]        # a non-zero column spans the image
    s = 3 / np.linalg.norm(column) * np.array([-1.0, 1.0])
    ax.plot(s * column[0], s * column[1], color="C2", lw=2, label="image")
    for i, p in enumerate(np.array([[1, 0], [0, 1], [1, 1]], dtype=float)):
        segment = p + np.outer([-1.0, 1.0], k)
        ax.plot(segment[:, 0], segment[:, 1], color=f"C{i + 4}", ls="--", lw=1, label="_nolegend_")
        image = M @ p
        ax.plot(image[0], image[1], "o", color=f"C{i + 4}", label="_nolegend_")


''' + M12A_32_FIGURE,
    after=[("md", "**Vérifications automatiques** (sur trois matrices, dans des axes neufs)."),
           ("code", M12A_32_CHECK)],
    note=r"Pour $\mathbf{M} = \begin{pmatrix} 1 & -2 \\ -0{,}5 & 1 \end{pmatrix}$, la seconde colonne vaut $-2$ fois la "
         r"première : rang 1. Le noyau est la droite dirigée par $(2, 1)$, l'image celle dirigée par $(1 ;\ -0{,}5)$. Le "
         r"carré unité devient un segment de l'image. Chaque segment $\mathbf{p} + t\,\mathbf{k}$ est envoyé sur "
         r"$\mathbf{M}\mathbf{p} + t\,\mathbf{M}\mathbf{k} = \mathbf{M}\mathbf{p}$ : un seul point, sur la droite image. "
         r"Les points d'un tel segment ont tous la même image : aucune application ne peut les séparer après coup, donc "
         r"aucune ne défait $\mathbf{M}$. La matrice inversible déforme le carré en un parallélogramme, sans rien écraser.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M12a.33 to M12a.35)
# ---------------------------------------------------------------------------
M12A_33_MISTAKES = bug_letters_mistakes(
    "ABD", "CEF",
    {"A": "calcule le rang de chaque famille appelée « base »",
     "B": "vérifie A fois chaque vecteur appelé « noyau »",
     "D": "relis l'ordre des facteurs d'un changement de base"},
    name_correct=False)

M12A_33 = Ex(
    "M12a.33", "🐛", 1, 15, "Chasse à l'erreur : une « base » liée, un noyau faux, S⁻¹AS écrit à l'envers",
    "repérer dans du code les erreurs classiques sur les bases, les noyaux et les changements de base, puis calculer "
    "les bonnes valeurs.", "fiche §2, §6, §7 et §8", tracks="C",
    body=r"""Un collègue a écrit six lignes, chacune avec un commentaire qui dit ce qu'elle doit calculer. Trois lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter de code**, trouve-les.

```python
A = np.array([[1.0, 2.0, 1.0], [2.0, 4.0, 3.0]])                     # a 2 × 3 matrix
u, v = np.array([1.0, 0.0, 1.0]), np.array([0.0, 1.0, 1.0])
B = np.column_stack([u, v, u + v])           # (A) a basis of R^3 that completes (u, v): its rank
R = np.array([[1.0, 2.0, 0.0], [0.0, 0.0, 1.0]])                     # the reduced form of A
k = np.array([R[0, 1], 1.0, 0.0])            # (B) the basis vector of ker A with x2 = 1: k[0]
e3 = np.array([0.0, 0.0, 1.0])
c = np.linalg.solve(np.column_stack([u, v, e3]), np.array([2.0, 3.0, 4.0]))   # (C) coordinates of (2, 3, 4) in (u, v, e3): c[2]
M = np.array([[2.0, 1.0], [0.0, 3.0]])
S = np.array([[1.0, 1.0], [0.0, 1.0]])
D = S @ M @ np.linalg.inv(S)                 # (D) the matrix of x -> M x in the basis of the columns of S: D[0, 1]
n = A.shape[1] - 2                           # (E) dim ker A, by the rank theorem (A has rank 2)
y = np.linalg.solve(M, np.array([5.0, 6.0]) - np.array([1.0, 0.0]))         # (F) phi^-1(5, 6) for phi(x) = M x + (1, 0): y[0]
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire (une liste de 6 nombres).

Dans ta copie : pour chaque ligne fausse, quelle erreur a été faite, et comment la corriger ? Laquelle des trois s'exécute sans erreur **et** sans valeur absurde, et pourquoi est-elle la plus dangereuse ?""",
    todo='''answer_M12a_33a = ...  # a) letters, as text
answer_M12a_33b = ...  # b) a list of 6 values''',
    check='''wbm.check("M12a.33a", answer_M12a_33a)
wbm.check("M12a.33b", answer_M12a_33b)''',
    solution='''answer_M12a_33a = "ABD"
A = np.array([[1.0, 2.0, 1.0], [2.0, 4.0, 3.0]])
u, v = np.array([1.0, 0.0, 1.0]), np.array([0.0, 1.0, 1.0])
B = np.column_stack([u, v, np.array([1.0, 0.0, 0.0])])   # (A) u + v is in Vect(u, v): complete with e1 instead
R = np.array([[1.0, 2.0, 0.0], [0.0, 0.0, 1.0]])
k = np.array([-R[0, 1], 1.0, 0.0])           # (B) x_p = −R[i, j]: the minus sign
e3 = np.array([0.0, 0.0, 1.0])
c = np.linalg.solve(np.column_stack([u, v, e3]), np.array([2.0, 3.0, 4.0]))   # (C) correct
M = np.array([[2.0, 1.0], [0.0, 3.0]])
S = np.array([[1.0, 1.0], [0.0, 1.0]])
D = np.linalg.solve(S, M @ S)                # (D) S⁻¹MS, not SMS⁻¹
n = A.shape[1] - 2                           # (E) correct
y = np.linalg.solve(M, np.array([5.0, 6.0]) - np.array([1.0, 0.0]))         # (F) correct
answer_M12a_33b = [int(np.linalg.matrix_rank(B)), float(k[0]), float(c[2]), float(D[0, 1]), n, float(y[0])]
print(answer_M12a_33a, answer_M12a_33b)''',
    record=f'''wbm.record("M12a.33a", "ABD",
           mistakes={M12A_33_MISTAKES})
VALUES_33 = [3.0, -2.0, -1.0, 0.0, 1.0, 1.0]
wbm.record("M12a.33b", VALUES_33, decimals=4,
           mistakes={{"(A) : u + v est dans Vect(u, v) ; une vraie base de ℝ³ a pour rang 3": [2.0] + VALUES_33[1:],
                      "(B) : x_p = −R[i, j], avec le signe moins": VALUES_33[:1] + [2.0] + VALUES_33[2:],
                      "(D) : la matrice dans la base S est S⁻¹MS, pas SMS⁻¹": VALUES_33[:3] + [2.0] + VALUES_33[4:]}})''',
    note=r"(A) $\mathbf{u} + \mathbf{v}$ est dans $\operatorname{Vect}(\mathbf{u}, \mathbf{v})$ : la « base » est liée, de rang 2 ; "
         r"$\mathbf{e}_1$ complète $(\mathbf{u}, \mathbf{v})$, et une base de $\mathbb{R}^3$ a pour rang 3. (B) Le vecteur "
         r"du noyau a $x_1 = -R_{12} = -2$ : $(-2, 1, 0)$, et $\mathbf{A}(2, 1, 0) = (4, 8) \ne \mathbf{0}$ trahit l'erreur "
         r"de signe. (C) est juste : $c_1 = 2$, $c_2 = 3$, $c_1 + c_2 + c_3 = 4$, donc $c_3 = -1$. (D) $\mathbf{S}\mathbf{M}"
         r"\mathbf{S}^{-1} = \begin{pmatrix} 2 & 2 \\ 0 & 3 \end{pmatrix}$ ; la bonne matrice, $\mathbf{S}^{-1}\mathbf{M}"
         r"\mathbf{S} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$, est diagonale, car $\mathbf{M}(1, 0) = 2\,(1, 0)$ et "
         r"$\mathbf{M}(1, 1) = 3\,(1, 1)$. C'est l'erreur la plus dangereuse : elle s'exécute et rend une matrice "
         r"plausible. (E) $3 - 2 = 1$. (F) $\varphi^{-1}(5, 6) = \mathbf{M}^{-1}(4, 6) = (1, 2)$.",
)

M12A_34_GIVEN = '''def null_space_zeros(A, tol=1e-10):          # a copy with a bug: the right shape, but only zeros
    A = np.asarray(A, dtype=float)
    rank = np.linalg.matrix_rank(A)
    return np.zeros((A.shape[1], A.shape[1] - rank))


def column_space_all(A, tol=1e-10):          # a copy with another bug: every column, pivot or not
    return np.array(A, dtype=float)'''

M12A_34_CHECK = '''with checked("M12a.34 vérifications"):
    problems = []
    ref_34 = wbm.load_mymath("ref").linmaps

    def outcome(null_space_t, column_space_t, seed):
        """None if check_kernel_and_rank passes, else the message of its AssertionError."""
        try:
            check_kernel_and_rank(null_space_t, column_space_t, seed)
        except AssertionError as exc:
            return str(exc)
        return None

    passed = sum(outcome(ref_34.null_space_basis, ref_34.column_space_basis, seed) is None for seed in range(20))
    caught_zeros = [outcome(null_space_zeros, ref_34.column_space_basis, seed) for seed in range(20)]
    caught_all = [outcome(ref_34.null_space_basis, column_space_all, seed) for seed in range(20)]
    print(f"la bonne paire passe ton test {passed} fois sur 20 ; le noyau fait de zéros est attrapé "
          f"{sum(m is not None for m in caught_zeros)} fois sur 20 ; l'image faite de toutes les colonnes, "
          f"{sum(m is not None for m in caught_all)} fois sur 20")
    if passed < 20:
        problems.append("ton test échoue sur les bonnes fonctions : compare avec np.allclose (des flottants), et "
                        "vérifie tes formes")
    if sum(m is not None for m in caught_zeros) < 20:
        problems.append("ton test laisse passer un noyau fait de zéros : vérifie aussi que ses colonnes sont libres")
    if sum(m is not None for m in caught_all) < 20:
        problems.append("ton test laisse passer une image faite de toutes les colonnes : vérifie le théorème du rang, "
                        "nombre de colonnes de la base de l'image + nombre de colonnes de la base du noyau = n")
    if not problems and any(not (m or "").strip() for m in caught_zeros + caught_all):
        problems.append("ajoute un message à chaque assert (assert condition, message)")
    if not problems:
        try:
            test_kernel_and_rank()
        except AssertionError as exc:
            problems.append(f"test_kernel_and_rank échoue sur ta librairie : {exc}")
    if problems:
        print("❌ Ex M12a.34 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M12a.34 : ton test passe sur les bonnes fonctions et attrape les deux copies fausses.")'''

M12A_34 = Ex(
    "M12a.34", "🛠️", 1, 15, "Un test de propriété : A fois une base du noyau donne 0, et le théorème du rang sur des "
    "matrices aléatoires",
    "écrire un test fondé sur des propriétés vérifiées sur des matrices aléatoires de rang choisi, et voir quelle "
    "propriété attrape quelle erreur.", "fiche §6 ; Ex M12a.26 et M12a.27", tracks="C",
    body=r"""Les tests de `mymath` comparent tes fonctions à SymPy. On peut aussi vérifier des **propriétés** que tout résultat juste doit avoir. Écris :
- `check_kernel_and_rank(null_space_basis, column_space_basis, seed, trials=10)` : avec `rng = np.random.default_rng(seed)`, répète `trials` fois : tire $m$ et $n$ entre 1 et 6 (`rng.integers(1, 7, size=2)`), un rang $r$ entre 0 et $\min(m, n)$ (`rng.integers(0, min(m, n) + 1)`), et la matrice entière $\mathbf{A} = \mathbf{L}\mathbf{C}$, produit de deux matrices d'entiers tirés entre $-3$ et 3, de formes $(m, r)$ et $(r, n)$ (`rng.integers(-3, 4, size=...)`, converties en floats). Avec `N = null_space_basis(A)` et `Q = column_space_basis(A)`, vérifie par des `assert` (avec un message) : (1) $\mathbf{A}\mathbf{N} = \mathbf{0}$ à $10^{-9}$ près ; (2) le théorème du rang, `N.shape[1] + Q.shape[1] == n` ; (3) les colonnes de `N` sont libres (`np.linalg.matrix_rank(N) == N.shape[1]`, permis ici : c'est le test, pas `linmaps.py` ; `matrix_rank` refuse un tableau sans colonne, et un noyau $\{\mathbf{0}\}$ n'a rien à vérifier) ;
- `test_kernel_and_rank()` : le test au format pytest, sans argument, qui appelle `check_kernel_and_rank` avec les fonctions de **ta** librairie (`mymath.linmaps`) et une graine fixe.

La cellule fournie définit deux copies fausses : un noyau qui a la bonne forme mais ne contient que des zéros, et une « base de l'image » qui garde toutes les colonnes. La vérification lance ton test sur les bonnes fonctions (la référence) et sur chaque copie fausse, pour 20 graines.

Dans ta copie : quelle propriété attrape le noyau fait de zéros, et pourquoi les deux autres le laissent-elles passer ? Quelle propriété attrape l'image faite de toutes les colonnes ? Une fonction fausse pourrait-elle passer les trois propriétés ? (Pense à un noyau juste, mais rendu avec ses colonnes multipliées par 2.)""",
    given=M12A_34_GIVEN,
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12a")


def check_kernel_and_rank(null_space_basis, column_space_basis, seed, trials=10):
    """Assert A N = 0, the rank theorem and independent kernel columns, on `trials` random integer matrices."""
    raise NotImplementedError("tire m, n, r, puis A = L C ; trois assert, chacun avec un message")


def test_kernel_and_rank():
    """The pytest test: check_kernel_and_rank on your null_space_basis and column_space_basis, with a fixed seed."""
    raise NotImplementedError("un appel à check_kernel_and_rank")''',
    solution=LOAD_REF + '''


def check_kernel_and_rank(null_space_basis, column_space_basis, seed, trials=10):
    """Assert A N = 0, the rank theorem and independent kernel columns, on `trials` random integer matrices."""
    rng = np.random.default_rng(seed)
    for _ in range(trials):
        m, n = rng.integers(1, 7, size=2)
        r = rng.integers(0, min(m, n) + 1)
        A = (rng.integers(-3, 4, size=(m, r)) @ rng.integers(-3, 4, size=(r, n))).astype(float)
        N = np.asarray(null_space_basis(A), dtype=float)
        Q = np.asarray(column_space_basis(A), dtype=float)
        assert N.shape[0] == n and np.allclose(A @ N, 0, rtol=0, atol=1e-9), (
            f"expected A N = 0 for A of shape {A.shape}, got a largest |A N| of {np.max(np.abs(A @ N), initial=0):.1e}")
        assert N.shape[1] + Q.shape[1] == n, (
            f"expected dim ker + rank = {n} for A of shape {A.shape}, got {N.shape[1]} + {Q.shape[1]}")
        assert N.shape[1] == 0 or np.linalg.matrix_rank(N) == N.shape[1], (
            f"expected independent kernel columns for A of shape {A.shape}, got a family of rank "
            f"{np.linalg.matrix_rank(N)} for {N.shape[1]} columns")


def test_kernel_and_rank():
    """The pytest test: check_kernel_and_rank on your null_space_basis and column_space_basis, with a fixed seed."""
    check_kernel_and_rank(mymath.linmaps.null_space_basis, mymath.linmaps.column_space_basis, seed=34)


test_kernel_and_rank()
print("the three properties hold for the reference")''',
    after=[("code", M12A_34_CHECK)],
    note=r"Le noyau fait de zéros vérifie $\mathbf{A}\mathbf{N} = \mathbf{0}$ et le théorème du rang (il a la bonne forme) : "
         r"seule la troisième propriété, des colonnes libres, l'attrape. L'image faite de toutes les colonnes a $n$ "
         r"colonnes : avec un noyau non nul, la somme dépasse $n$, et le théorème du rang l'attrape (une matrice de rang "
         r"plein en colonnes passe, d'où les tirages de rangs variés). Une base du noyau multipliée par 2 passe les trois "
         r"propriétés : elle est fausse au sens de la docstring (la convention de SymPy), mais c'est encore une base du "
         r"noyau. Un test de propriétés vérifie des conséquences de la bonne réponse ; pour la réponse elle-même, il faut "
         r"un oracle, comme le font les tests de `mymath`.",
)

M12A_35_GIVEN = '''def make_hidden_table(seed, n=150):
    """A (n, p) table whose columns hide exact linear relations, and one relation that is only almost exact."""
    rng = np.random.default_rng(seed)
    q, k = int(rng.integers(3, 5)), int(rng.integers(1, 4))      # q free directions, k exact relations
    G = np.zeros((q, q + k + 1))
    G[:, :q] = np.eye(q)
    for j in range(q, q + k + 1):
        column = np.zeros(q)
        while np.count_nonzero(column) < 2:
            column = rng.integers(-3, 4, size=q).astype(float)
        G[:, j] = column
    scales = 10.0 ** rng.integers(-2, 4, size=q + k + 1)
    scales[q], scales[q + k] = 1e6, 1e-4
    X = (rng.normal(size=(n, q)) @ G) * scales
    X[:, q + k] += 1e-6 * np.linalg.norm(X[:, q + k]) / np.sqrt(n) * rng.normal(size=n)   # almost, not exactly
    return X[:, rng.permutation(q + k + 1)]'''

M12A_35_CHECK = '''with checked("M12a.35 défi"):
    problems, ok_35 = [], False
    for seed_t in (35, 36, 37):
        X_t = make_hidden_table(seed_t)
        rng_t = np.random.default_rng(seed_t)
        rng_t.integers(3, 5)
        k_true = int(rng_t.integers(1, 4))
        try:
            N_t = np.asarray(hidden_relations(X_t.copy()), dtype=float)
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"hidden_relations lève {type(exc).__name__} ({exc})")
            break
        p_t = X_t.shape[1]
        if N_t.ndim != 2 or N_t.shape[0] != p_t:
            problems.append(f"table {seed_t} : hidden_relations rend la forme {N_t.shape}, pas ({p_t}, k)")
            break
        norms_t = np.linalg.norm(X_t, axis=0)
        scaled_t = N_t * norms_t[:, None]                  # the relations between the normalized columns
        if N_t.shape[1] < k_true:
            problems.append(f"table {seed_t} : {N_t.shape[1]} relation(s) trouvée(s), il en manque : une colonne d'une "
                            "échelle très différente des autres cache peut-être une relation exacte")
            break
        if N_t.shape[1] > k_true:
            problems.append(f"table {seed_t} : {N_t.shape[1]} relations, c'est trop : une relation vraie à 1e-6 près "
                            "seulement n'est pas exacte ; ta tolérance est trop large, ou elle dépend de l'échelle")
            break
        if k_true:
            col_norms_t = np.linalg.norm(scaled_t, axis=0)
            residual_t = np.linalg.norm((X_t / norms_t) @ scaled_t, axis=0) / col_norms_t
            if np.any(col_norms_t == 0) or residual_t.max() > 1e-8:
                problems.append(f"table {seed_t} : une relation rendue n'est pas exacte (résidu relatif "
                                f"{residual_t.max():.1e})")
                break
            if np.linalg.matrix_rank(scaled_t / col_norms_t, tol=1e-6) < k_true:
                problems.append(f"table {seed_t} : les relations rendues ne sont pas libres")
                break
        print(f"table {seed_t} : {X_t.shape}, {N_t.shape[1]} relation(s) exacte(s) retrouvée(s)")
    if problems:
        print("❌ Ex M12a.35 : " + " ; ".join(problems) + ".")
    else:
        ok_35 = True
        print("✅ Ex M12a.35 : défi réussi : toutes les relations exactes, et aucune de trop, dans les trois tables.")
with checked("M12a.35"):
    hidden_relations(make_hidden_table(35))                   # ⏳ while hidden_relations is not written
    wbm.check("M12a.35", bool(ok_35), computed=True)'''

M12A_35 = Ex(
    "M12a.35", "🏆", 3, 30, "Défi : retrouver les relations linéaires exactes cachées entre les colonnes d'un tableau, "
    "sans en inventer",
    "trouver toutes les relations linéaires exactes entre les colonnes d'un tableau de données, quelles que soient les "
    "échelles des colonnes, sans prendre une relation approchée pour une relation exacte.",
    "fiche §4 et §6 ; Ex M12a.27 et M12a.31", tracks="C",
    body=r"""La fonction fournie `make_hidden_table(seed)` fabrique un tableau de 150 exemples dont certaines colonnes sont des combinaisons **exactes** des autres (aux arrondis des flottants près), et une colonne qui n'est une combinaison des autres qu'**à $10^{-6}$ près** en relatif. Les colonnes ont des ordres de grandeur très différents (de $10^{-4}$ à $10^{6}$), et sont mélangées.

**L'objectif** : écrire `hidden_relations(X)`, qui rend une matrice de forme $(p, k)$ dont les colonnes forment une base de l'espace des relations **exactes** $\{\mathbf{c} : \mathbf{X}\mathbf{c} = \mathbf{0}\}$ : toutes les relations exactes, et aucune de trop (la relation à $10^{-6}$ près n'en est pas une). La vérification essaie ta fonction sur trois tableaux (`seed` = 35, 36 et 37) ; une dernière cellule enregistre si l'objectif est atteint sur les trois.

`null_space_basis(X)` avec sa tolérance absolue par défaut échoue : les arrondis d'une colonne de l'ordre de $10^6$ dépassent $10^{-10}$, et le bruit d'une colonne de l'ordre de $10^{-4}$ passe sous $10^{-10}$ (M12a.31). Pistes : mettre les colonnes à la même échelle (diviser chaque colonne par sa norme, une matrice diagonale $\mathbf{D}$ : $\mathbf{X}\mathbf{D}^{-1}$), chercher le noyau de ce tableau avec une tolérance bien choisie entre les arrondis (vers $10^{-15}$) et le bruit (vers $10^{-6}$), puis revenir aux relations du tableau de départ (si $\mathbf{X}\mathbf{D}^{-1}\mathbf{y} = \mathbf{0}$, alors $\mathbf{c} = \mathbf{D}^{-1}\mathbf{y}$ vérifie $\mathbf{X}\mathbf{c} = \mathbf{0}$).

Dans ta copie : quelle tolérance as-tu choisie, et pourquoi ? Que se passe-t-il avec une tolérance de $10^{-5}$, et avec la tolérance par défaut sans changer d'échelle ? Sur de vraies données mesurées, comment choisirais-tu la tolérance ?""",
    given=M12A_35_GIVEN,
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M12a")


def hidden_relations(X):
    """A (p, k) matrix whose columns are a basis of the exact relations X c = 0 between the columns of X."""
    raise NotImplementedError("mettre les colonnes à la même échelle, un noyau avec une tolérance choisie, revenir")''',
    check=M12A_35_CHECK,
    solution=LOAD_REF + '''


def hidden_relations(X):
    """A (p, k) matrix whose columns are a basis of the exact relations X c = 0 between the columns of X."""
    X = np.asarray(X, dtype=float)
    norms = np.linalg.norm(X, axis=0)                  # D: every column brought to norm 1
    Y = mymath.linmaps.null_space_basis(X / norms, tol=1e-9)
    return Y / norms[:, None]                          # c = D⁻¹ y


for seed in (35, 36, 37):
    X_35 = make_hidden_table(seed)
    print(seed, X_35.shape, "default tol, raw columns:", mymath.linmaps.null_space_basis(X_35).shape[1],
          "· scaled, tol 1e-9:", hidden_relations(X_35).shape[1],
          "· scaled, tol 1e-5:", mymath.linmaps.null_space_basis(X_35 / np.linalg.norm(X_35, axis=0), tol=1e-5).shape[1])''',
    after=[("solution", M12A_35_CHECK.split('with checked("M12a.35"):')[0].rstrip())],
    record='''wbm.record("M12a.35", True,
           mistakes={"l'objectif n'est pas atteint sur les trois tables : la cellule du défi dit pourquoi": False})''',
    note=r"Sur les colonnes brutes, la tolérance absolue $10^{-10}$ se trompe dans les deux sens : elle manque des relations "
         r"(les arrondis d'une colonne de l'ordre de $10^6$ font des pivots de l'ordre de $10^{-10}$) et peut en inventer "
         r"(le bruit d'une colonne de l'ordre de $10^{-4}$ tombe sous la tolérance). Une fois chaque colonne divisée par "
         r"sa norme, les pivots résiduels des relations exactes valent environ $10^{-15}$ et celui de la relation "
         r"approchée environ $10^{-7}$ : toute tolérance entre $10^{-12}$ et $10^{-8}$ les sépare ; $10^{-5}$ prend la "
         r"relation approchée pour exacte. Sur des données mesurées, la tolérance se règle sur la précision des mesures, "
         r"après avoir mis les colonnes à la même échelle.",
)

PART_A = Part("A", "Ta librairie : indépendance, image, noyau, coordonnées, changement de base ; SymPy et NumPy",
              "Fiche §2 à §7. Les cinq fonctions de `mymath/linmaps.py`, puis les mêmes calculs avec SymPy et NumPy.",
              given=TOOLS, exercises=[M12A_26, M12A_27, M12A_28, M12A_29])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §4 à §6. Le rang de matrices construites, le rang numérique et la tolérance, une application du plan "
              "qui écrase une direction.",
              exercises=[M12A_30, M12A_31, M12A_32])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §2, §6, §7 et §8. Trois erreurs à trouver, un test de propriétés, puis des relations cachées à "
              "retrouver sans en inventer.",
              exercises=[M12A_33, M12A_34, M12A_35])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M12a.1 à M12a.13, M12a.20, M12a.21 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M12a · Espaces vectoriels et applications linéaires — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m12a_espaces_vectoriels/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M12a`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M12a · Espaces vectoriels et applications linéaires — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : sous-espaces, combinaisons et indépendance, bases et "
               "coordonnées, rangs, matrices d'applications et composées, noyaux, images et solutions d'un système, "
               "changement de base, application affine et sa réciproque, dérivation des polynômes, une feature "
               "redondante, un encodeur qui écrase une direction.\n"
               "- Écrire les cinq fonctions de `mymath/linmaps.py` et les tester, puis comparer avec SymPy et NumPy.\n"
               "- Prédire des rangs, mesurer le rang numérique, dessiner ce qu'écrase une application, chasser des "
               "erreurs, tester des propriétés, retrouver des relations cachées.\n\n"
               r"**Rappel express.** Sous-espace : $\mathbf{0}$ dedans, stable par $\lambda\mathbf{x} + \mu\mathbf{y}$ ; "
               r"libre : chaque colonne de $[\mathbf{v}_1 \cdots \mathbf{v}_k]$ porte un pivot ; coordonnées : "
               r"$\mathbf{B}\mathbf{c} = \mathbf{v}$ ; $\operatorname{rg}\mathbf{A} = \operatorname{rg}\mathbf{A}^\top$, "
               r"$\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \min(\operatorname{rg}\mathbf{A}, \operatorname{rg}\mathbf{B})$ ; "
               r"colonne $j$ de la matrice de $f$ = $f(\mathbf{e}_j)$ ; « $f$ puis $g$ » = $\mathbf{B}\mathbf{A}$ ; "
               r"$\dim\ker\mathbf{A} + \operatorname{rg}\mathbf{A} = n$ ; solutions de $\mathbf{A}\mathbf{x} = \mathbf{b}$ = "
               r"$\mathbf{x}_p + \ker\mathbf{A}$ ; nouvelle base : $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ ; "
               r"$\varphi^{-1}(\mathbf{y}) = \mathbf{A}^{-1}(\mathbf{y} - \mathbf{b})$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu reconnaître un sous-espace, et décider si une famille est libre ?\n"
               "2. Sais-tu extraire une base, et calculer des coordonnées dans une base ?\n"
               "3. Sais-tu calculer un rang, et majorer celui d'un produit ?\n"
               "4. Sais-tu écrire la matrice d'une application linéaire, et calculer un noyau et une image ?\n"
               "5. Sais-tu changer de base, et inverser une application affine ?\n\n"
               "**La suite** : le chapitre 12 de workbookIA (préparation des données), en parallèle de M12b, "
               "l'orthogonalité et les projections.")]


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
