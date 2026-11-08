#!/usr/bin/env python
"""Build the two notebooks of chapter M09a from a single source (used by Claude).

    python tools/chapters/build_m09a.py
    python tools/run_all_notebooks.py chapitres/m09a_matrices/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m09a_matrices/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M09a.1 to M09a.14, 🔗 M09a.19 and M09a.20); parts A to C are the notebook
exercises. Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it. The
matrices are new: none is a test case of tests/test_m09a_matrices.py, an example of the fiche or of a docstring of
matrices.py, or an example of workbookIA 0B, 9 and 10 (no [[1, 2, 3], [4, 5, 6]] with (1, 0, −1), no [[1, 2], [3, 4]]
with [[0, 1], [1, 0]], no [[2, 1], [5, 3]], no [[3, 1], [4, 2]], no MNIST layer (64, 784) × (784, 128), no 1000 × 1000
chain, no shop tempo, no points (0, 1), (1, 2), (2, 4), no neuron weights named AD or BE).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M09a"
FOLDER = "chapitres/m09a_matrices"

F = 'kind="fraction", simplified=True'
SHAPE = "la forme s'écrit (lignes, colonnes), dans cet ordre"
ORDER = "le produit n'est pas commutatif : garde l'ordre des matrices de l'énoncé"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M09a.1", "Un tableau de données vu comme une matrice : forme, lignes, colonnes, moyennes", [
        ("a", "a list of 2 integers", "[5, 3]", f'''mistakes={{"{SHAPE}": [3, 5]}}'''),
        ("b", "a number", "70",
         '''mistakes={"x_32 est à la ligne 3 et à la colonne 2 : la ligne d'abord": 18}'''),
        ("c", "a list of 2 integers", "[2, 1]",
         '''mistakes={"en Python, les indices commencent à 0 : retire 1 à chaque indice mathématique": [3, 2], '''
         '''"la ligne d'abord, puis la colonne": [1, 2]}'''),
        ("d", "a list of 3 numbers", "[24, 65, 15]",
         '''mistakes={"les lignes sont numérotées à partir de 1 : la ligne 4 est la quatrième": [20, 50, 7]}'''),
        ("e", "a list of 3 numbers", "X1.mean(axis=0)",
         '''decimals=1, mistakes={"une moyenne par colonne (axis=0), pas par ligne": X1.mean(axis=1)}'''),
        ("f", "a list of 3 numbers", "X1[1] - X1.mean(axis=0)",
         '''decimals=1, mistakes={"centrer retire la moyenne de chaque colonne, pas l'inverse": X1.mean(axis=0) - X1[1]}'''),
        ("g", "a number (4 decimals)", "X1[:, 0].std()",
         '''decimals=4, mistakes={"ddof = 0 : divise la somme des carrés des écarts par n = 5": X1[:, 0].std(ddof=1), '''
         '''"l'écart-type est la racine de la variance": X1[:, 0].var()}'''),
    ]),

    Paper("M09a.2", "Le produit matrice-vecteur, par les lignes puis par les colonnes", [
        ("a", "an integer", "3",
         '''mistakes={"Ax a autant de coordonnées que A a de lignes": 4}'''),
        ("b", "a list of 3 numbers", "(A2 @ X2).tolist()",
         '''mistakes={"la coordonnée i est le produit scalaire de la ligne i de A avec x, en respectant les signes": '''
         '''(np.abs(A2) @ np.abs(X2)).tolist()}'''),
        ("c", "an integer", "12",
         '''mistakes={"chaque coordonnée de Ax demande une multiplication par élément de sa ligne de A": 7}'''),
        ("d", "a list of 3 numbers", "A2[:, 2].tolist()",
         '''mistakes={"A e_3 sélectionne la colonne 3 de A, pas sa ligne 3": [-2, 0, 1, 3], '''
         '''"e_3 a son 1 en position 3, en comptant à partir de 1": [0, 5, 3]}'''),
        ("e", "a list of 4 numbers", "[1, 0, 0, 2]",
         '''mistakes={"Ay = y₁a₁ + … + y₄a₄ : y_j est le coefficient de la colonne j": [2, 0, 0, 1]}'''),
        ("f", "True or False", "False",
         '''mistakes={"A a 4 colonnes : le vecteur doit avoir 4 coordonnées": True}'''),
        ("g", "a list of 2 numbers", "(XG2 @ WG2 - 2).tolist()",
         '''decimals=1, mistakes={"le biais b = −2 s'ajoute à chaque prédiction": (XG2 @ WG2).tolist()}'''),
    ]),

    Paper("M09a.3", "Produits matriciels à la main : formes compatibles et calculs", [
        ("a", "a list of 2 integers", "[2, 2]"),
        ("b", "a matrix", "(A3 @ B3).tolist()",
         f'''mistakes={{"{ORDER} : AB, pas BA": (B3 @ A3).tolist()}}'''),
        ("c", "a list of 2 integers", "[3, 3]"),
        ("d", "a number", "int((B3 @ A3)[1, 2])",
         '''mistakes={"(BA)_23 : la ligne 2 de B avec la colonne 3 de A": int((B3 @ A3)[2, 1])}'''),
        ("e", "True or False", "False",
         '''mistakes={"A a 3 colonnes et C a 2 lignes : les dimensions intérieures diffèrent": True}'''),
        ("f", "a matrix", "(C3 @ A3).tolist()"),
        ("g", "a matrix", "(A3 @ B3 @ C3).tolist()",
         f'''mistakes={{"{ORDER} : (AB)C, avec C à droite": (C3 @ A3 @ B3).tolist()}}'''),
    ]),

    Paper("M09a.4", "Le coût d'un produit, et l'ordre des parenthèses dans ABC", [
        ("a", "an integer", "20 * 400 * 5",
         '''mistakes={"un produit (n, p) × (p, m) coûte n p m multiplications : les trois dimensions": 20 * 5}'''),
        ("b", "an integer", "20 * 400 * 5 + 20 * 5 * 300",
         '''mistakes={"le second produit, (AB)C, coûte aussi : (20, 5) × (5, 300)": 20 * 400 * 5}'''),
        ("c", "an integer", "400 * 5 * 300 + 20 * 400 * 300",
         '''mistakes={"le second produit est A fois BC, de forme (400, 300) : (20, 400) × (400, 300)": 400 * 5 * 300}'''),
        ("d", "a number (1 decimal)", "(400 * 5 * 300 + 20 * 400 * 300) / (20 * 400 * 5 + 20 * 5 * 300)",
         '''decimals=1, mistakes={"le rapport est le coût de A(BC) divisé par celui de (AB)C": '''
         '''(20 * 400 * 5 + 20 * 5 * 300) / (400 * 5 * 300 + 20 * 400 * 300), '''
         '''"le rapport des deux coûts, pas le surcoût relatif (rapport − 1)": '''
         '''(400 * 5 * 300 + 20 * 400 * 300) / (20 * 400 * 5 + 20 * 5 * 300) - 1}'''),
        ("e", "a list of 2 integers", "[20, 300]"),
        ("f", "an integer", "5 * 300 * 2 + 400 * 5 * 2 + 20 * 400 * 2",
         '''mistakes={"de gauche à droite n'est pas le meilleur ordre ici : compare les ordres possibles": '''
         '''20 * 400 * 5 + 20 * 5 * 300 + 20 * 300 * 2, '''
         '''"(AB)(CD) n'est pas le meilleur ordre : compare les cinq parenthésages possibles": '''
         '''20 * 400 * 5 + 5 * 300 * 2 + 20 * 5 * 2}'''),
        ("g", "an integer", "27", '''mistakes={"le coût d'un produit carré varie comme n³": {3, 9}}'''),
    ]),

    Paper("M09a.5", "Une couche dense Z = XW + b à la main : deux exemples, trois entrées, deux sorties", [
        ("a", "a list of 2 integers", "[3, 2]", f'''mistakes={{"{SHAPE} : 3 entrées, 2 neurones": [2, 3]}}'''),
        ("b", "a matrix", "(X5 @ W5 + B5).tolist()",
         '''decimals=1, mistakes={"le biais b s'ajoute à chaque ligne de XW": (X5 @ W5).tolist(), '''
         '''"le biais b_j s'ajoute à la colonne j (le neurone j), sur chaque ligne": (X5 @ W5 + B5[::-1]).tolist()}'''),
        ("c", "a number", "float((X5 @ W5 + B5)[1, 0])",
         '''decimals=1, mistakes={"z_21 : ligne 2 (l'exemple 2), colonne 1 (le neurone 1)": float((X5 @ W5 + B5)[0, 1])}'''),
        ("d", "a matrix", "np.maximum(X5 @ W5 + B5, 0).tolist()",
         '''decimals=1, mistakes={"ReLU met à zéro les nombres négatifs et garde les autres": np.abs(X5 @ W5 + B5).tolist()}'''),
        ("e", "an integer", "8",
         '''mistakes={"compte aussi les biais, un par neurone": 6}'''),
        ("f", "a list of 2 integers", "[2, 3]",
         '''mistakes={"PyTorch range les poids de nn.Linear en (n_out, n_in)": [3, 2]}'''),
        ("g", "an integer", "12", '''mistakes={"un produit (n, p) × (p, m) coûte n p m multiplications": 6}'''),
    ]),

    Paper("M09a.6", "Un embedding : une ligne one-hot fois une matrice", [
        ("a", "a list of 5 numbers", "[0, 0, 0, 1, 0]",
         '''mistakes={"le mot 4 a son 1 à la quatrième place (en comptant à partir de 1)": [0, 0, 0, 0, 1]}'''),
        ("b", "a list of 3 numbers", "E6[3].tolist()",
         '''decimals=1, mistakes={"les lignes de E sont numérotées à partir de 1, comme les mots": E6[2].tolist()}'''),
        ("c", "an integer", "15"),
        ("d", "an integer", "15", '''mistakes={"sans raccourci, chaque élément de E est multiplié une fois": 3}'''),
        ("e", "a list of 3 numbers", "(E6[1] + E6[4]).tolist()",
         '''decimals=1, mistakes={"un 1 en position j sélectionne la ligne j de E, en comptant à partir de 1": (E6[0] + E6[3]).tolist()}'''),
        ("f", "a list of 3 numbers (4 decimals)", "((E6[0] + 2 * E6[2]) / 3).tolist()",
         '''decimals=4, mistakes={"le mot 3 compte deux fois : le coefficient 2": ((E6[0] + E6[2]) / 3).tolist(), '''
         '''"divise la somme par 3, le nombre de mots": (E6[0] + 2 * E6[2]).tolist()}'''),
    ]),

    Paper("M09a.7", "Transposées de produits, et la matrice symétrique XᵀX", [
        ("a", "a list of 2 integers", "[3, 3]"),
        ("b", "a matrix", "(A7 @ B7).T.tolist()",
         '''mistakes={"la transposée échange lignes et colonnes : ce résultat est AB lui-même": (A7 @ B7).tolist()}'''),
        ("c", "a matrix", "(B7 @ A7).T.tolist()",
         '''mistakes={"la transposée échange lignes et colonnes : ce résultat est BA lui-même": (B7 @ A7).tolist()}'''),
        ("d", "True or False", "False",
         '''mistakes={"compare les formes : AᵀBᵀ est (2, 3) × (3, 2)": True}'''),
        ("e", "a matrix", "(X7.T @ X7).tolist()",
         '''mistakes={"XᵀX est (3, 4) × (4, 3) : une ligne et une colonne par feature, pas par exemple": '''
         '''(X7 @ X7.T).tolist()}'''),
        ("f", "a list of 2 integers", "[4, 4]",
         '''mistakes={"écris les formes des deux facteurs de XXᵀ, X puis Xᵀ": [3, 3]}'''),
        ("g", "a number", "int((X7 @ X7.T)[0, 1])",
         '''mistakes={"c'est un élément de XᵀX (colonnes) : XXᵀ fait les produits scalaires des lignes": '''
         '''int((X7.T @ X7)[0, 1])}'''),
    ]),

    Paper("M09a.8", "Le pivot de Gauss sur un système 3 × 3 à solution unique", [
        ("a", "a number", "2",
         '''fractional="le multiple est le nombre à annuler divisé par le pivot, pas l'inverse"'''),
        ("b", "a list of 4 numbers", "[0, 3, -5, -21]",
         '''mistakes={"retranche 2 fois la nouvelle première ligne, second membre compris": [0, 3, -5, -3], '''
         '''"L ← L − 2 L₁ : retranche, n'ajoute pas": [4, -1, 3, 15]}'''),
        ("c", "a list of 4 numbers", "[0, 5, -5, -25]",
         '''mistakes={"retranche 3 fois la nouvelle première ligne, second membre compris": [0, 5, -5, 2]}'''),
        ("d", "an irreducible fraction", '"5/3"',
         f'''{F}, mistakes={{"le multiple est le nombre à annuler divisé par le pivot de la deuxième ligne": "3/5"}}'''),
        ("e", "a number", "3"),
        ("f", "a list of 3 numbers", "[1, -2, 3]",
         '''mistakes={"l'ordre est (x, y, z)": [3, -2, 1]}'''),
    ]),

    Paper("M09a.9", "Un système sans solution, un système à une infinité de solutions", [
        ("a", "a list of 4 numbers", "[0, 0, 0, 1]",
         '''mistakes={"applique aussi chaque opération au second membre": [0, 0, 0, 0]}'''),
        ("b", "an integer", "0",
         '''mistakes={"relis la dernière ligne de a) comme une équation en x, y, z": 1}'''),
        ("c", "a matrix", "[[1, 0, -7, -3], [0, 1, 3, 2], [0, 0, 0, 0]]",
         '''mistakes={"c'est une forme échelonnée : la forme réduite annule aussi le nombre au-dessus du pivot de la '''
         '''deuxième ligne": [[1, 2, -1, 1], [0, 1, 3, 2], [0, 0, 0, 0]]}'''),
        ("d", "an integer", "1", '''mistakes={"les variables libres sont celles dont la colonne n'a pas de pivot": 2}'''),
        ("e", "a list of 3 numbers", "[-3, 2, 0]",
         '''mistakes={"avec z = 0, lis x et y sur la forme réduite : attention au signe du second membre": [3, 2, 0]}'''),
        ("f", "a list of 3 numbers", "[4, -1, 1]",
         '''mistakes={"exprime x et y en fonction de z : un terme en z qui passe de l'autre côté change de signe": [-10, 5, 1]}'''),
        ("g", "a number", "5",
         '''mistakes={"compare les coefficients de la troisième équation à ceux des deux premières": 6}'''),
    ]),

    Paper("M09a.10", "La forme échelonnée réduite d'une matrice 3 × 4 et la solution générale", [
        ("a", "a matrix", "[[1, 0, 3, 3], [0, 1, 1, 2], [0, 0, 0, 0]]",
         '''mistakes={"c'est une forme échelonnée : la forme réduite annule aussi le nombre au-dessus du pivot de la '''
         '''deuxième ligne": [[1, -1, 2, 1], [0, 1, 1, 2], [0, 0, 0, 0]]}'''),
        ("b", "a list of integers", "[1, 2]",
         '''mistakes={"les numéros commencent à 1": [0, 1]}'''),
        ("c", "an integer", "2",
         '''mistakes={"le rang est le nombre de pivots, pas le nombre de lignes": 3}'''),
        ("d", "a list of 3 numbers", "[3, 2, 0]"),
        ("e", "a list of 3 numbers", "[-3, 0, 2]",
         '''mistakes={"exprime x et y en fonction de z : un terme en z qui passe de l'autre côté change de signe": [9, 4, 2]}'''),
        ("f", "a list of 3 numbers", "[-3, -1, 1]",
         '''mistakes={"le système homogène a un second membre nul : la dernière colonne de la forme réduite devient 0": [0, 1, 1]}'''),
        ("g", "True or False", "True",
         '''mistakes={"remplace (6, 3, −1) dans les trois équations": False}'''),
    ]),

    Paper("M09a.11", "L'inverse d'une matrice 2 × 2, par la formule, puis vérifiée", [
        ("a", "a number", "4", '''mistakes={"ad − bc : une soustraction entre les deux produits": 16}'''),
        ("b", "a matrix", "[[1.25, -0.75], [-0.5, 0.5]]",
         '''decimals=2, mistakes={"divise par ad − bc": [[5, -3], [-2, 2]], '''
         '''"échange a et d, et change le signe de b et de c": [[1.25, 0.75], [0.5, 0.5]]}'''),
        ("c", "a list of 2 numbers", "[3, 1]", '''mistakes={"l'ordre est (x, y)": [1, 3]}'''),
        ("d", "a matrix", "[[0, 1], [1, 1]]",
         '''decimals=2, mistakes={"AX = C donne X = A⁻¹C : A⁻¹ multiplie à gauche, comme A dans AX": '''
         '''[[1.25, 0.25], [2.75, -0.25]]}'''),
        ("e", "a matrix", "[[0.625, -0.375], [-0.25, 0.25]]",
         '''decimals=3, mistakes={"(λA)⁻¹ = A⁻¹ / λ, pas λ A⁻¹": [[2.5, -1.5], [-1, 1]], '''
         '''"(2A)⁻¹ n'est pas A⁻¹ : le facteur 2 compte": [[1.25, -0.75], [-0.5, 0.5]]}'''),
        ("f", "a matrix", "[[1.25, -0.5], [-0.75, 0.5]]",
         '''decimals=2, mistakes={"(Aᵀ)⁻¹ = (A⁻¹)ᵀ : transpose l'inverse": [[1.25, -0.75], [-0.5, 0.5]]}'''),
        ("g", "a matrix", "[[31, -21], [-14, 10]]",
         '''mistakes={"c'est la transposée : (A²)⁻¹ = (A⁻¹)², calcule A⁻¹ fois A⁻¹": [[31, -14], [-21, 10]], '''
         '''"c'est A² : la question demande 16 fois son inverse": [[10, 21], [14, 31]], '''
         '''"A² est le produit A A, pas le carré de chaque nombre": [[25, 9], [4, 4]]}'''),
    ]),

    Paper("M09a.12", "L'inverse d'une matrice 3 × 3 par Gauss-Jordan", [
        ("a", "a matrix", "[[-2, 1, 3], [2, -1, -2], [-1, 1, 1]]",
         '''mistakes={"c'est la transposée de l'inverse : vérifie A A⁻¹ = I": [[-2, 2, -1], [1, -1, 1], [3, -2, 1]]}'''),
        ("b", "a list of 3 numbers", "[4, -2, 1]"),
        ("c", "a list of 3 numbers", "[1, -1, 1]",
         '''mistakes={"la solution de A x = e_2 est la colonne 2 de A⁻¹, pas sa ligne 2": [2, -1, -2]}'''),
        ("d", "a list of 3 numbers", "[-2, 2, -1]",
         '''mistakes={"(Aᵀ)⁻¹ = (A⁻¹)ᵀ : transpose ton inverse de a)": [-2, 1, 3]}'''),
        ("e", "True or False", "False",
         '''mistakes={"regarde la troisième ligne : combine-t-elle les deux autres ?": True}'''),
    ]),

    Paper("M09a.13", "Le rang de quatre matrices, et les colonnes redondantes", [
        ("a", "an integer", "1", '''mistakes={"le rang compte les pivots, pas les colonnes": 2}'''),
        ("b", "an integer", "2", '''mistakes={"cherche si une colonne combine les deux autres": 3}'''),
        ("c", "an integer", "2",
         '''mistakes={"cherche si les colonnes 3 et 4 combinent les colonnes 1 et 2": 3}'''),
        ("d", "an integer", "3"),
        ("e", "a list of 2 numbers", "[2, -1]", '''mistakes={"l'ordre est [a, b], a pour la colonne 1": [-1, 2]}'''),
        ("f", "True or False", "False", '''mistakes={"relie le rang trouvé en b) à l'inversibilité (fiche §8)": True}'''),
        ("g", "an integer", "2", '''mistakes={"le rang des lignes est égal au rang des colonnes": 3}'''),
    ]),

    Paper("M09a.14", "Mettre un problème en système : trois engrais pour trois nutriments", [
        ("a", "a matrix", "[[200, 100, 0], [100, 0, 150], [0, 200, 100]]",
         '''mistakes={"une ligne par nutriment et une colonne par engrais : c'est la transposée": '''
         '''[[200, 100, 0], [100, 0, 200], [0, 150, 100]]}'''),
        ("b", "a list of 3 numbers", "[4, 3, 2]"),
        ("c", "a number", "9"),
        ("d", "an irreducible fraction", '"16/7"', F),
        ("e", "a list of 2 numbers", "[7, -3]"),
    ]),

    Paper("M09a.19", "Pont : une passe avant à deux couches, deux produits matriciels et leurs formes", [
        ("a", "a list of 2 integers", "[64, 5]", f'''mistakes={{"{SHAPE} : un exemple par ligne, un neurone par colonne": [5, 64]}}'''),
        ("b", "a list of 2 integers", "[64, 2]"),
        ("c", "an integer", "3 * 5 + 5 + 5 * 2 + 2",
         '''mistakes={"compte aussi les biais, un par neurone de chaque couche": 3 * 5 + 5 * 2}'''),
        ("d", "an integer", "64 * 3 * 5 + 64 * 5 * 2",
         '''mistakes={"le batch compte : chaque produit est (64, n_in) × (n_in, n_out)": 3 * 5 + 5 * 2}'''),
        ("e", "a list of 3 numbers", "H19.tolist()",
         '''decimals=1, mistakes={"ReLU met à zéro les nombres négatifs": (np.array([1, -1]) @ W19 + B19).tolist(), '''
         '''"ajoute le biais b₁ avant ReLU": np.maximum(np.array([1, -1]) @ W19, 0).tolist()}'''),
        ("f", "a number", "float(H19 @ V19 + 0.5)",
         '''decimals=1, mistakes={"h passe par ReLU avant la couche de sortie : prends le h de e)": '''
         '''float((np.array([1, -1]) @ W19 + B19) @ V19 + 0.5), "ajoute le biais de sortie b₂": float(H19 @ V19)}'''),
        ("g", "a matrix", "(W19 @ V19[:, None]).tolist()",
         '''mistakes={"W₁ a la forme (2, 3) et W₂ la forme (3, 1) : W₁W₂ a la forme (2, 1)": [[-1, 0]]}'''),
    ]),

    Paper("M09a.20", "Pont : centrer et réduire un tableau en écriture matricielle", [
        ("a", "a list of 2 numbers", "[4, 20]"),
        ("b", "a list of 2 integers", "[3, 2]", f'''mistakes={{"{SHAPE} : (3, 1) × (1, 2)": [2, 3]}}'''),
        ("c", "a matrix", "(X20 - X20.mean(axis=0)).tolist()",
         '''mistakes={"centrer retire la moyenne de chaque colonne": (X20.mean(axis=0) - X20).tolist()}'''),
        ("d", "a list of 2 numbers (4 decimals)", "(1 / X20.std(axis=0)).tolist()",
         '''decimals=4, mistakes={"ddof = 0 : divise par n = 3": (1 / X20.std(axis=0, ddof=1)).tolist(), '''
         '''"la question demande les inverses des écarts-types": X20.std(axis=0).tolist()}'''),
        ("e", "a list of 2 numbers (3 decimals)", "((X20[0] - X20.mean(axis=0)) / X20.std(axis=0)).tolist()",
         '''decimals=3, mistakes={"ddof = 0 : divise par n = 3": '''
         '''((X20[0] - X20.mean(axis=0)) / X20.std(axis=0, ddof=1)).tolist()}'''),
        ("f", "a matrix (4 decimals)", "((X20 - X20.mean(axis=0)).T @ (X20 - X20.mean(axis=0)) / 3).tolist()",
         '''decimals=4, mistakes={"divise par n = 3 : la question demande (1/3) X_cᵀ X_c": '''
         '''((X20 - X20.mean(axis=0)).T @ (X20 - X20.mean(axis=0))).tolist(), '''
         '''"la question divise par n = 3, pas par n − 1": '''
         '''((X20 - X20.mean(axis=0)).T @ (X20 - X20.mean(axis=0)) / 2).tolist(), '''
         '''"centre d'abord : la formule utilise X_c, pas X": (X20.T @ X20 / 3).tolist()}'''),
        ("g", "a number", "0.5",
         '''decimals=1, mistakes={"c'est la covariance : la question porte sur les colonnes standardisées": 20 / 3, '''
         '''"c'est un élément de la diagonale : la question demande celui hors de la diagonale": 1}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import numpy as np

X1 = np.array([[22, 60, 12], [25, 55, 18], [19, 70, 8], [24, 65, 15], [20, 50, 7]], dtype=float)     # M09a.1
A2 = np.array([[3, -1, 2, 0], [1, 4, -2, 5], [-2, 0, 1, 3]])                                        # M09a.2
X2 = np.array([2, -1, 3, 1])
XG2, WG2 = np.array([[2, 1, 0], [-1, 3, 2]]), np.array([1.5, -0.5, 1])
A3 = np.array([[1, -1, 2], [0, 3, 1]])                                                              # M09a.3
B3 = np.array([[2, 1], [-1, 0], [1, 4]])
C3 = np.array([[1, 2], [-1, 1]])
X5 = np.array([[1, 0, 2], [-1, 3, 1]])                                                              # M09a.5
W5 = np.array([[2, -1], [0, 1], [1, 3]])
B5 = np.array([-1, 0.5])
E6 = np.array([[0.1, -0.4, 1.2], [0.9, 0.0, -0.3], [-1.1, 0.6, 0.2], [0.5, 1.5, -0.8], [0.0, -0.2, 0.7]])  # M09a.6
A7 = np.array([[2, 0], [1, -1], [-1, 3]])                                                           # M09a.7
B7 = np.array([[1, 4, 0], [2, -1, 1]])
X7 = np.array([[1, -1, 2], [0, 2, 1], [2, 1, 0], [1, 0, -1]])
W19, B19 = np.array([[1, 0, 2], [-1, 1, 1]]), np.array([0, 0.5, -1])                               # M09a.19
V19 = np.array([1, 2, -1])
H19 = np.maximum(np.array([1, -1]) @ W19 + B19, 0)
X20 = np.array([[2, 10], [4, 30], [6, 20]], dtype=float)                                            # M09a.20'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M09a.1 à M09a.14, 🔗 M09a.19 et M09a.20)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"7/9\"` ;\n"
               "- une liste `[2, -1, 0]` pour un vecteur ou une forme, une liste de lignes `[[1, 0], [-2, 3]]` pour une "
               "matrice, ou `True` / `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M09a.25 to M09a.29)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math
import time

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


def timed_product(A):
    """The time (seconds) of one product A @ A with NumPy."""
    start = time.perf_counter()
    A @ A
    return time.perf_counter() - start'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M09a")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/matrices.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "Une matrice est une liste de lignes ou un tableau NumPy à deux dimensions. Les opérations élément par élément "
         "de NumPy sont permises (`+`, `-`, `*` entre des lignes, le broadcasting, `np.sum`, `np.zeros`, `np.eye`, "
         "`np.hstack`) ; `@`, `np.dot`, `np.matmul`, `.T`, `np.transpose` et `np.linalg` sont interdits : les tests "
         "comparent tes résultats aux leurs, et un test vérifie que tu ne t'en sers pas. Ne modifie jamais la matrice "
         "reçue : travaille sur une copie, `np.array(A, dtype=float)`.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError", "LinAlgError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of matrices.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_matrices_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m09a_matrices.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m09a_matrices.py", "{keyword}", impl="ref")')]


NDARRAY = "la docstring demande un tableau NumPy : np.array(...)"

M09A_25 = Ex(
    "M09a.25", "🔨", 1, 20, "Le produit matriciel et la transposée · `matmul, transpose`",
    "programmer le produit matriciel et la transposée avec des opérations élément par élément, en refusant les formes "
    "incompatibles.", "fiche §3 et §4", tracks="C, E", mymath="matrices.py",
    body=HOWTO + r"""

Écris (fiche §3 et §4) :
- `matmul(A, B)` : le produit $\mathbf{A}\mathbf{B}$, $(\mathbf{A}\mathbf{B})_{ij} = \sum_k a_{ik}b_{kj}$, en tableau NumPy de floats ; une `ValueError` si une des deux n'est pas à deux dimensions, ou si $\mathbf{A}$ n'a pas autant de colonnes que $\mathbf{B}$ a de lignes. Une boucle sur les éléments marche ; plus rapide : une boucle sur les lignes de $\mathbf{A}$, chaque ligne de $\mathbf{A}\mathbf{B}$ étant la combinaison des lignes de $\mathbf{B}$ pondérées par la ligne de $\mathbf{A}$ (fiche §3) ;
- `transpose(A)` : la transposée, de forme $(m, n)$ pour $\mathbf{A}$ de forme $(n, m)$, dans un **nouveau** tableau ; une `ValueError` si $\mathbf{A}$ n'est pas à deux dimensions.

La vérification calcule :
- a) `matmul([[2, -1, 0], [1, 3, 2]], [[1, 4], [0, -2], [3, 1]])` (une matrice) ;
- b) `matmul([[0.5, -2, 1]], [[4], [1], [-3]])` (une matrice) ;
- c) `transpose([[1.5, -2], [0, 4], [3, 1]])` (une matrice) ;
- d) le nom de l'erreur levée par `matmul([[1, 2, 3]], [[1, 2, 3]])` ;
- e) le nom du type de `matmul([[1]], [[2]])`, en texte ;
- f) vrai ou faux : `transpose(matmul(A, B))` est égal à `matmul(transpose(B), transpose(A))` pour les matrices de a) (calculé avec tes fonctions).

Dans ta copie : calcule a) et b) à la main. Combien de multiplications fait ta fonction pour a) ? Pourquoi `transpose` doit-elle renvoyer un nouveau tableau ?""",
    todo=LOAD_LEARNER,
    check='''A_25, B_25 = [[2, -1, 0], [1, 3, 2]], [[1, 4], [0, -2], [3, 1]]
with checked("M09a.25a"):
    wbm.check("M09a.25a", np.asarray(mymath.matrices.matmul(A_25, B_25)).tolist(), computed=True)
with checked("M09a.25b"):
    wbm.check("M09a.25b", np.asarray(mymath.matrices.matmul([[0.5, -2, 1]], [[4], [1], [-3]])).tolist(),
              computed=True)
with checked("M09a.25c"):
    wbm.check("M09a.25c", np.asarray(mymath.matrices.transpose([[1.5, -2], [0, 4], [3, 1]])).tolist(), computed=True)
with checked("M09a.25d"):
    wbm.check("M09a.25d", raised(mymath.matrices.matmul, [[1, 2, 3]], [[1, 2, 3]]), computed=True)
with checked("M09a.25e"):
    wbm.check("M09a.25e", type(mymath.matrices.matmul([[1]], [[2]])).__name__, computed=True)
with checked("M09a.25f"):
    left_25 = np.asarray(mymath.matrices.transpose(mymath.matrices.matmul(A_25, B_25)), dtype=float)
    right_25 = np.asarray(mymath.matrices.matmul(mymath.matrices.transpose(B_25), mymath.matrices.transpose(A_25)),
                          dtype=float)
    wbm.check("M09a.25f", bool(left_25.shape == right_25.shape and np.allclose(left_25, right_25)), computed=True)''',
    solution=LOAD_REF + '''
matmul, transpose = mymath.matrices.matmul, mymath.matrices.transpose
A_25, B_25 = [[2, -1, 0], [1, 3, 2]], [[1, 4], [0, -2], [3, 1]]
print("a)", matmul(A_25, B_25).tolist(), " b)", matmul([[0.5, -2, 1]], [[4], [1], [-3]]).tolist())
print("c)", transpose([[1.5, -2], [0, 4], [3, 1]]).tolist(), " d)", raised(matmul, [[1, 2, 3]], [[1, 2, 3]]),
      " e)", type(matmul([[1]], [[2]])).__name__)
print("f)", np.allclose(transpose(matmul(A_25, B_25)), matmul(transpose(B_25), transpose(A_25))))''',
    record=f'''wbm.record("M09a.25a", [[2.0, 10.0], [7.0, 0.0]], decimals=6,
           mistakes={{"(AB)_ij est le produit scalaire de la ligne i de A et de la colonne j de B, pas de la ligne j":
                         [[2.0, 7.0], [10.0, 0.0]]}})
wbm.record("M09a.25b", [[-3.0]], decimals=6)
wbm.record("M09a.25c", [[1.5, 0.0, 3.0], [-2.0, 4.0, 1.0]], decimals=6)
wbm.record("M09a.25d", "ValueError",
           mistakes={{"(1, 3) × (1, 3) n'existe pas : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M09a.25e", "ndarray",
           mistakes={{"{NDARRAY}": {{"list", "tuple"}}}})
wbm.record("M09a.25f", True,
           mistakes={{"tes deux fonctions doivent vérifier (AB)ᵀ = BᵀAᵀ : relance leurs tests": False}})''',
    after=tests_cells("test_matmul_ or test_transpose_"),
    note=r"a) $\begin{pmatrix} 2 - 0 + 0 & 8 + 2 + 0 \\ 1 + 0 + 6 & 4 - 6 + 2 \end{pmatrix} = \begin{pmatrix} 2 & 10 \\ 7 & 0 "
         r"\end{pmatrix}$ : $2 \times 3 \times 2 = 12$ multiplications. b) $2 - 2 - 3 = -3$, un produit $(1, 3) \times "
         r"(3, 1)$, c'est-à-dire un produit scalaire. `transpose` renvoie un nouveau tableau : une vue de NumPy partagerait "
         r"ses nombres avec la matrice reçue, et modifier le résultat modifierait la matrice de l'appelant.",
)

M09A_26 = Ex(
    "M09a.26", "🔨", 2, 35, "La forme échelonnée réduite et le rang · `rref, rank`",
    "programmer l'élimination de Gauss-Jordan avec pivot partiel, et en déduire le rang.", "fiche §6 et §8",
    tracks="C, E", mymath="matrices.py",
    body=r"""Écris (fiche §6 et §8), en suivant la docstring :
- `rref(A, tol=1e-10)` : la forme échelonnée réduite et le tuple des colonnes des pivots. Colonne par colonne depuis la gauche, avec une ligne courante $r$ (au début 0) : dans la colonne courante, prends la ligne (à partir de $r$) dont l'élément a la plus grande valeur absolue ; s'il vaut au plus `tol`, la colonne n'a pas de pivot ; sinon échange cette ligne avec la ligne $r$, divise-la par le pivot, retranche-en des multiples à **toutes** les autres lignes, note la colonne et passe à la ligne $r + 1$. À la fin, mets à 0 les nombres au plus égaux à `tol` en valeur absolue ;
- `rank(A, tol=1e-10)` : le nombre de pivots, en `int` de Python.

Les deux lèvent une `ValueError` si $\mathbf{A}$ n'est pas à deux dimensions. La forme réduite est unique : les tests la comparent à celle de SymPy.

La vérification calcule :
- a) la forme réduite de `rref([[1, 2, -1, 3], [2, 4, 1, 0], [-1, -2, 2, -3]])` (une matrice) ;
- b) ses colonnes des pivots (une liste) ;
- c) la forme réduite de `rref([[0, 0, 2], [0, 3, 1], [0, 6, 4]])` (une matrice) ;
- d) `rank([[1, -1, 2, 0], [2, -2, 4, 0], [0, 1, 1, 1], [1, 0, 3, 1]])` ;
- e) le nom de l'erreur levée par `rank([1, 2, 3])` ;
- f) le nom du type de la valeur rendue par `rank`, en texte.

Dans ta copie : pourquoi la deuxième colonne (indice 1) n'a-t-elle pas de pivot en a) ? Quelles lignes de d) sont des combinaisons des autres ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M09a.26a"):
    wbm.check("M09a.26a", np.asarray(mymath.matrices.rref([[1, 2, -1, 3], [2, 4, 1, 0], [-1, -2, 2, -3]])[0]).tolist(),
              computed=True)
with checked("M09a.26b"):
    wbm.check("M09a.26b", list(mymath.matrices.rref([[1, 2, -1, 3], [2, 4, 1, 0], [-1, -2, 2, -3]])[1]),
              computed=True)
with checked("M09a.26c"):
    wbm.check("M09a.26c", np.asarray(mymath.matrices.rref([[0, 0, 2], [0, 3, 1], [0, 6, 4]])[0]).tolist(),
              computed=True)
with checked("M09a.26d"):
    wbm.check("M09a.26d", mymath.matrices.rank([[1, -1, 2, 0], [2, -2, 4, 0], [0, 1, 1, 1], [1, 0, 3, 1]]),
              computed=True)
with checked("M09a.26e"):
    wbm.check("M09a.26e", raised(mymath.matrices.rank, [1, 2, 3]), computed=True)
with checked("M09a.26f"):
    wbm.check("M09a.26f", type(mymath.matrices.rank([[1, 3], [2, 5]])).__name__, computed=True)''',
    solution=LOAD_REF + '''
rref, rank = mymath.matrices.rref, mymath.matrices.rank
R_26, pivots_26 = rref([[1, 2, -1, 3], [2, 4, 1, 0], [-1, -2, 2, -3]])
print("a)", R_26.tolist(), " b)", pivots_26)
print("c)", rref([[0, 0, 2], [0, 3, 1], [0, 6, 4]])[0].tolist(),
      " d)", rank([[1, -1, 2, 0], [2, -2, 4, 0], [0, 1, 1, 1], [1, 0, 3, 1]]))
print("e)", raised(rank, [1, 2, 3]), " f)", type(rank([[1, 3], [2, 5]])).__name__)''',
    record=f'''wbm.record("M09a.26a", [[1.0, 2.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], decimals=6,
           mistakes={{"une forme échelonnée ne suffit pas : annule aussi les nombres au-dessus de chaque pivot (retranche "
                      "des multiples à toutes les autres lignes)": [[1.0, 2.0, 0.5, 0.0], [0.0, 0.0, 1.0, -1.2],
                                                                     [0.0, 0.0, 0.0, 1.0]]}})
wbm.record("M09a.26b", [0, 2, 3],
           mistakes={{"rref rend les indices Python des colonnes, à partir de 0": [1, 3, 4]}})
wbm.record("M09a.26c", [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]], decimals=6)
wbm.record("M09a.26d", 2, mistakes={{"le rang compte les pivots, pas les lignes non nulles du départ": {{3, 4}}}})
wbm.record("M09a.26e", "ValueError",
           mistakes={{"un vecteur n'est pas une matrice : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M09a.26f", "int",
           mistakes={{"la docstring demande un int de Python : int(...)": {{"int64", "float", "float64"}}}})''',
    after=tests_cells("test_rref_ or test_rank_"),
    note=r"a) La deuxième colonne est le double de la première : après l'élimination dans la colonne 1, elle ne contient plus que "
         r"des zéros sous la ligne courante, et n'a pas de pivot. Les pivots sont dans les colonnes 0, 2 et 3 (indices "
         r"Python). c) La première colonne est nulle : aucun pivot, on passe à la suivante. d) La ligne 2 est le double de "
         r"la ligne 1, et la ligne 4 est la somme des lignes 1 et 3 : rang 2.",
)

M09A_27 = Ex(
    "M09a.27", "🔨", 2, 30, "Résoudre un système par le pivot de Gauss · `solve`",
    "programmer la résolution d'un système carré par élimination avec pivot partiel puis remontée, et refuser une "
    "matrice singulière.", "fiche §5 et §6", tracks="C, E", mymath="matrices.py",
    body=r"""Écris `solve(A, b)` (fiche §6), en suivant la docstring : sur la matrice augmentée $[\mathbf{A} \mid \mathbf{b}]$ (`np.hstack`), pour chaque colonne $k$, prends pour pivot la ligne (à partir de $k$) dont l'élément a la plus grande valeur absolue, échange-la avec la ligne $k$, et annule les éléments **sous** le pivot ; puis remonte, de la dernière ligne à la première. Une `ValueError` si $\mathbf{A}$ n'est pas carrée, si $\mathbf{b}$ n'a pas $n$ coordonnées, ou si un pivot vaut au plus $10^{-12}$ fois la plus grande valeur absolue de $\mathbf{A}$ (matrice singulière).

La vérification calcule :
- a) `solve([[3, -1, 2], [1, 2, -1], [2, 1, 1]], [1, 5, 4])` (une liste, 6 décimales) ;
- b) `solve([[0, 2, 1], [1, 1, 1], [2, 0, 3]], [5, 6, 13])` (un pivot nul au départ ; une liste, 6 décimales) ;
- c) `solve([[1e-18, 1], [1, 2]], [1, 3])` (une liste, 6 décimales) ;
- d) le nom de l'erreur levée par `solve([[1, 2, 3], [2, 4, 6], [1, 0, 1]], [1, 2, 3])` ;
- e) le nom de l'erreur levée par `solve([[1, 2], [3, 5]], [1, 2, 3])` ;
- f) le nom du type de la solution rendue, en texte.

Dans ta copie : vérifie a) dans les trois équations. Que vaudrait c) sans pivot partiel ? Pourquoi d) est-elle singulière ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M09a.27a"):
    wbm.check("M09a.27a", np.asarray(mymath.matrices.solve([[3, -1, 2], [1, 2, -1], [2, 1, 1]], [1, 5, 4])).tolist(),
              computed=True)
with checked("M09a.27b"):
    wbm.check("M09a.27b", np.asarray(mymath.matrices.solve([[0, 2, 1], [1, 1, 1], [2, 0, 3]], [5, 6, 13])).tolist(),
              computed=True)
with checked("M09a.27c"):
    wbm.check("M09a.27c", np.asarray(mymath.matrices.solve([[1e-18, 1], [1, 2]], [1, 3])).tolist(), computed=True)
with checked("M09a.27d"):
    wbm.check("M09a.27d", raised(mymath.matrices.solve, [[1, 2, 3], [2, 4, 6], [1, 0, 1]], [1, 2, 3]), computed=True)
with checked("M09a.27e"):
    wbm.check("M09a.27e", raised(mymath.matrices.solve, [[1, 2], [3, 5]], [1, 2, 3]), computed=True)
with checked("M09a.27f"):
    wbm.check("M09a.27f", type(mymath.matrices.solve([[2, 1], [1, 1]], [3, 2])).__name__, computed=True)''',
    solution=LOAD_REF + '''
solve = mymath.matrices.solve
print("a)", solve([[3, -1, 2], [1, 2, -1], [2, 1, 1]], [1, 5, 4]).round(6), " b)",
      solve([[0, 2, 1], [1, 1, 1], [2, 0, 3]], [5, 6, 13]), " c)", solve([[1e-18, 1], [1, 2]], [1, 3]))
print("d)", raised(solve, [[1, 2, 3], [2, 4, 6], [1, 0, 1]], [1, 2, 3]), " e)", raised(solve, [[1, 2], [3, 5]], [1, 2, 3]),
      " f)", type(solve([[2, 1], [1, 1]], [3, 2])).__name__)''',
    record=f'''wbm.record("M09a.27a", [1.0, 2.0, 0.0], decimals=6)
wbm.record("M09a.27b", [2.0, 1.0, 3.0], decimals=6)
wbm.record("M09a.27c", [1.0, 1.0], decimals=6,
           mistakes={{"le pivot 1e-18 est minuscule : prends dans chaque colonne la ligne dont l'élément a la plus grande "
                      "valeur absolue (pivot partiel)": [0.0, 1.0]}})
wbm.record("M09a.27d", "ValueError",
           mistakes={{"cette matrice est singulière : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M09a.27e", "ValueError",
           mistakes={{"b doit avoir n = 2 coordonnées : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M09a.27f", "ndarray", mistakes={{"{NDARRAY}": {{"list", "tuple"}}}})''',
    after=tests_cells("test_solve_"),
    note=r"a) $(1, 2, 0)$ : $3 - 2 + 0 = 1$, $1 + 4 - 0 = 5$, $2 + 2 + 0 = 4$. b) La colonne 1 commence par un 0 : le pivot "
         r"partiel prend la ligne 3 (élément 2). c) Sans pivot partiel, l'élimination divise par $10^{-18}$, et les arrondis "
         r"donnent $(0, 1)$, alors que la solution exacte, $x = \frac{1}{1 - 2\varepsilon}$ et $y = \frac{1 - 3\varepsilon}"
         r"{1 - 2\varepsilon}$ avec $\varepsilon = 10^{-18}$, vaut $(1, 1)$ à $10^{-17}$ près. d) La ligne 2 est le double de la ligne 1 : après élimination, un pivot nul apparaît.",
)

M09A_28 = Ex(
    "M09a.28", "🔨", 1, 20, "L'inverse par Gauss-Jordan · `inverse`",
    "programmer l'inverse d'une matrice carrée en réduisant $[\\mathbf{A} \\mid \\mathbf{I}]$, et refuser une matrice "
    "singulière.", "fiche §7 ; Ex M09a.26", tracks="C", mymath="matrices.py",
    body=r"""Écris `inverse(A)` (fiche §7) : construis $[\mathbf{A} \mid \mathbf{I}_n]$ (`np.hstack` et `np.eye` sont permis), réduis-la avec **ta** fonction `rref` (écris d'abord M09a.26), vérifie que la partie gauche est l'identité (les $n$ premiers pivots sont dans les colonnes $0, \ldots, n - 1$), et rends la partie droite. Une `ValueError` si $\mathbf{A}$ n'est pas carrée ou est singulière.

La vérification calcule :
- a) `inverse([[2, 0, 1], [1, 1, 0], [0, 2, 1]])` (une matrice, 6 décimales) ;
- b) `inverse([[0, 0, 1], [1, 0, 0], [0, 1, 0]])` (une matrice) ;
- c) le nom de l'erreur levée par `inverse([[1, -1, 2], [0, 1, 1], [1, 0, 3]])` ;
- d) le nom de l'erreur levée par `inverse([[1, 0, 2], [3, 1, 1]])` ;
- e) vrai ou faux : `matmul(A, inverse(A))` est l'identité, à $10^{-12}$ près, pour la matrice de a) (avec tes fonctions).

Dans ta copie : que remarques-tu en comparant b) à la transposée de la matrice ? Pourquoi c) est-elle singulière ?""",
    todo=LOAD_LEARNER,
    check='''A_28 = [[2, 0, 1], [1, 1, 0], [0, 2, 1]]
with checked("M09a.28a"):
    wbm.check("M09a.28a", np.asarray(mymath.matrices.inverse(A_28)).tolist(), computed=True)
with checked("M09a.28b"):
    wbm.check("M09a.28b", np.asarray(mymath.matrices.inverse([[0, 0, 1], [1, 0, 0], [0, 1, 0]])).tolist(),
              computed=True)
with checked("M09a.28c"):
    wbm.check("M09a.28c", raised(mymath.matrices.inverse, [[1, -1, 2], [0, 1, 1], [1, 0, 3]]), computed=True)
with checked("M09a.28d"):
    wbm.check("M09a.28d", raised(mymath.matrices.inverse, [[1, 0, 2], [3, 1, 1]]), computed=True)
with checked("M09a.28e"):
    product_28 = np.asarray(mymath.matrices.matmul(A_28, mymath.matrices.inverse(A_28)), dtype=float)
    wbm.check("M09a.28e", bool(np.allclose(product_28, np.eye(3), rtol=0, atol=1e-12)), computed=True)''',
    solution=LOAD_REF + '''
inverse = mymath.matrices.inverse
A_28 = [[2, 0, 1], [1, 1, 0], [0, 2, 1]]
print("a)", inverse(A_28).tolist(), " b)", inverse([[0, 0, 1], [1, 0, 0], [0, 1, 0]]).tolist())
print("c)", raised(inverse, [[1, -1, 2], [0, 1, 1], [1, 0, 3]]), " d)", raised(inverse, [[1, 0, 2], [3, 1, 1]]),
      " e)", np.allclose(mymath.matrices.matmul(A_28, inverse(A_28)), np.eye(3), rtol=0, atol=1e-12))''',
    record=f'''wbm.record("M09a.28a", [[0.25, 0.5, -0.25], [-0.25, 0.5, 0.25], [0.5, -1.0, 0.5]], decimals=6,
           mistakes={{"c'est la transposée de l'inverse : garde la partie droite telle quelle":
                         [[0.25, -0.25, 0.5], [0.5, 0.5, -1.0], [-0.25, 0.25, 0.5]]}})
wbm.record("M09a.28b", [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]], decimals=6,
           mistakes={{"c'est la matrice elle-même : l'inverse de cette permutation est sa transposée":
                         [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]}})
wbm.record("M09a.28c", "ValueError",
           mistakes={{"cette matrice est singulière (une colonne combine les deux autres) : la docstring demande une "
                      "ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M09a.28d", "ValueError",
           mistakes={{"une matrice non carrée n'a pas d'inverse : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M09a.28e", True,
           mistakes={{"A A⁻¹ doit valoir I : relance les tests de inverse et de matmul": False}})''',
    after=tests_cells("test_inverse_"),
    note=r"a) $\mathbf{A}^{-1} = \frac{1}{4}\begin{pmatrix} 1 & 2 & -1 \\ -1 & 2 & 1 \\ 2 & -4 & 2 \end{pmatrix}$. b) La matrice "
         r"permute les coordonnées ; son inverse est sa transposée (une matrice de permutation est orthogonale, M12b). c) La "
         r"colonne 3 vaut 3 fois la colonne 1 plus la colonne 2 : $(3 - 1, 0 + 1, 3 + 0) = (2, 1, 3)$.",
)

A_29, B_29 = "[[1, -2, 0, 3], [2, 1, -1, 0]]", "[[0, 1], [2, -1], [1, 1], [-1, 2]]"
P_29 = "[[2, 4, 1, 3], [1, 2, 0, 1], [3, 6, 1, 4]]"

M09A_29 = Ex(
    "M09a.29", "📦", 1, 15, "`@`, `*`, `.T`, `np.linalg.solve`, `matrix_rank` et `sympy.Matrix.rref` contre tes "
    "fonctions",
    "faire les mêmes calculs avec NumPy et SymPy, lire ce que rend chaque fonction, et comparer avec ta librairie.",
    "fiche §3, §6 et §8 ; Ex M09a.25 à M09a.27", tracks="C, E",
    body=r"""En pratique, on ne réécrit pas ces fonctions :
- `A @ B` est le produit matriciel, `A * B` le produit de Hadamard (élément par élément, avec broadcasting), `A.T` la transposée ;
- `np.linalg.solve(A, b)` résout un système carré, `np.linalg.matrix_rank(A)` donne le rang (par une autre méthode que le pivot, la SVD de M12d), `np.linalg.inv(A)` l'inverse ;
- `sympy.Matrix(A).rref()` rend la forme échelonnée réduite **exacte** (avec des fractions) et le tuple des colonnes des pivots.

Avec $\mathbf{A}$ = `[[1, -2, 0, 3], [2, 1, -1, 0]]`, $\mathbf{B}$ = `[[0, 1], [2, -1], [1, 1], [-1, 2]]` et $\mathbf{P}$ = `[[2, 4, 1, 3], [1, 2, 0, 1], [3, 6, 1, 4]]`, calcule :
- a) `A @ B` (une matrice) ;
- b) `np.array([[2, -1], [3, 0]]) * np.array([[0, 1], [-1, 2]])` (une matrice) ;
- c) `np.linalg.matrix_rank(P)` ;
- d) les colonnes des pivots de `sympy.Matrix(P).rref()` (une liste) ;
- e) `np.linalg.solve([[4, 1], [2, 3]], [9, 7])` (une liste, 6 décimales) ;
- f) vrai ou faux : pour 20 systèmes $5 \times 5$ tirés au hasard (`np.random.default_rng(29)`), ta fonction `solve` donne la même solution que `np.linalg.solve` à $10^{-9}$ près (calcule-le avec une boucle).

Dans ta copie : calcule à la main l'élément $(1, 2)$ de a). Que donnerait `A * B`, et pourquoi ?""",
    todo='''answer_M09a_29a = ...  # a) a matrix
answer_M09a_29b = ...  # b) a matrix
answer_M09a_29c = ...  # c) an integer
answer_M09a_29d = ...  # d) a list
answer_M09a_29e = ...  # e) a list (6 decimals)
answer_M09a_29f = ...  # f) True or False, computed with a loop''',
    check='''for letter, answer in zip("abcdef", [answer_M09a_29a, answer_M09a_29b, answer_M09a_29c, answer_M09a_29d,
                                     answer_M09a_29e, answer_M09a_29f]):
    wbm.check(f"M09a.29{letter}", answer)''',
    solution=f'''ref_29 = wbm.load_mymath("ref")
A_29, B_29 = np.array({A_29}), np.array({B_29})
P_29 = np.array({P_29})
answer_M09a_29a = (A_29 @ B_29).tolist()
answer_M09a_29b = (np.array([[2, -1], [3, 0]]) * np.array([[0, 1], [-1, 2]])).tolist()
answer_M09a_29c = int(np.linalg.matrix_rank(P_29))
answer_M09a_29d = list(sympy.Matrix(P_29).rref()[1])
answer_M09a_29e = np.linalg.solve([[4, 1], [2, 3]], [9, 7]).tolist()
rng_29 = np.random.default_rng(29)
systems_29 = [(rng_29.normal(size=(5, 5)), rng_29.normal(size=5)) for _ in range(20)]
answer_M09a_29f = all(np.allclose(ref_29.matrices.solve(A, b), np.linalg.solve(A, b), rtol=0, atol=1e-9)
                      for A, b in systems_29)
print(answer_M09a_29a, answer_M09a_29b, answer_M09a_29c, answer_M09a_29d, answer_M09a_29e, answer_M09a_29f)''',
    record=f'''wbm.record("M09a.29a", (np.array({A_29}) @ np.array({B_29})).tolist(),
           mistakes={{"A @ B : A à gauche, de forme (2, 4), fois B, de forme (4, 2)":
                         (np.array({B_29}) @ np.array({A_29})).tolist()}})
wbm.record("M09a.29b", [[0, -1], [-3, 0]],
           mistakes={{"* est le produit élément par élément (Hadamard), pas le produit matriciel":
                         (np.array([[2, -1], [3, 0]]) @ np.array([[0, 1], [-1, 2]])).tolist()}})
wbm.record("M09a.29c", 2,
           mistakes={{"cherche une colonne proportionnelle à une autre, et une ligne qui combine les autres": 3}})
wbm.record("M09a.29d", [0, 2], mistakes={{"rref() de SymPy rend des indices à partir de 0": [1, 3]}})
wbm.record("M09a.29e", [2.0, 1.0], decimals=6)
wbm.record("M09a.29f", True,
           mistakes={{"relis ta fonction solve (M09a.27) : ses tests disent ce qui ne va pas": False}})''',
    note=r"a) $\begin{pmatrix} -7 & 9 \\ 1 & 0 \end{pmatrix}$, de forme $(2, 2)$ ; l'élément $(1, 2)$ vaut "
         r"$1 \times 1 + (-2) \times (-1) + 0 \times 1 + 3 \times 2 = 9$. `A * B` lève une erreur : des formes $(2, 4)$ et "
         r"$(4, 2)$ ne se combinent pas par broadcasting. b) $\begin{pmatrix} 0 & -1 \\ -3 & 0 \end{pmatrix}$. c) et d) La colonne 2 de "
         r"$\mathbf{P}$ est le double de la colonne 1, et sa ligne 3 la somme des deux autres : rang 2, pivots dans les "
         r"colonnes 0 et 2. e) $(2, 1)$ : $8 + 1 = 9$ et $4 + 3 = 7$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, two experiments, a figure (M09a.30 to M09a.33)
# ---------------------------------------------------------------------------
M09A_30_EXPERIMENT = '''for label, make in [("a) ones((2, 3)) @ ones((3, 1))", lambda: np.ones((2, 3)) @ np.ones((3, 1))),
                    ("b) ones((3, 4)) @ ones(4)", lambda: np.ones((3, 4)) @ np.ones(4)),
                    ("c) ones(4) @ ones((4, 2))", lambda: np.ones(4) @ np.ones((4, 2))),
                    ("d) ones((2, 3)) * ones(3)", lambda: np.ones((2, 3)) * np.ones(3)),
                    ("e) ones((2, 3)) * ones(2)", lambda: np.ones((2, 3)) * np.ones(2))]:
    try:
        print(f"{label:32s} → shape {make().shape}")
    except ValueError as exc:
        print(f"{label:32s} → ValueError: {str(exc)[:60]}")'''

M09A_30 = Ex(
    "M09a.30", "🔮", 1, 10, "Prédire la forme du résultat : `@`, `*` et broadcasting",
    "prévoir la forme du résultat de `@` et de `*` sur des tableaux de formes différentes, puis la vérifier.",
    "fiche §1 et §3", tracks="C, E", hypothesis=True,
    body=r"""NumPy applique deux règles différentes. Pour `@`, celle du produit matriciel (un tableau à une dimension y joue le rôle d'un vecteur). Pour `*`, le **broadcasting** : les formes se comparent en partant de la droite, et une dimension égale à 1 est répétée autant qu'il faut ; si deux dimensions diffèrent et qu'aucune ne vaut 1, c'est une erreur. Choisis, pour chaque expression, le numéro de la bonne réponse :
- a) `np.ones((2, 3)) @ np.ones((3, 1))` : (1) la forme `(2,)` ; (2) une erreur ; (3) la forme `(2, 1)` ;
- b) `np.ones((3, 4)) @ np.ones(4)` : (1) la forme `(3,)` ; (2) une erreur ; (3) la forme `(3, 4)` ;
- c) `np.ones(4) @ np.ones((4, 2))` : (1) une erreur ; (2) la forme `(4, 2)` ; (3) la forme `(2,)` ;
- d) `np.ones((2, 3)) * np.ones(3)` : (1) une erreur ; (2) la forme `(2, 3)` ; (3) la forme `(3,)` ;
- e) `np.ones((2, 3)) * np.ones(2)` : (1) la forme `(2, 3)` ; (2) la forme `(2,)` ; (3) une erreur.

**Avant d'exécuter quoi que ce soit**, écris tes cinq prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M09a_30a = ...  # a) 1, 2 or 3, written BEFORE running the experiment below
prediction_M09a_30b = ...  # b) 1, 2 or 3
prediction_M09a_30c = ...  # c) 1, 2 or 3
prediction_M09a_30d = ...  # d) 1, 2 or 3
prediction_M09a_30e = ...  # e) 1, 2 or 3''',
    check='''for letter, prediction in zip("abcde", [prediction_M09a_30a, prediction_M09a_30b, prediction_M09a_30c,
                                       prediction_M09a_30d, prediction_M09a_30e]):
    wbm.check(f"M09a.30{letter}", prediction)''',
    record='''wbm.record("M09a.30a", 3, prediction=True, choices=[1, 2, 3])
wbm.record("M09a.30b", 1, prediction=True, choices=[1, 2, 3])
wbm.record("M09a.30c", 3, prediction=True, choices=[1, 2, 3])
wbm.record("M09a.30d", 2, prediction=True, choices=[1, 2, 3])
wbm.record("M09a.30e", 3, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes cinq prédictions écrites."),
        ("todo", guarded(M09A_30_EXPERIMENT, [f"prediction_M09a_30{letter}" for letter in "abcde"],
                         "⏳ Écris d'abord tes cinq prédictions, puis exécute à nouveau.")),
        ("solution", M09A_30_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : pourquoi a) rend-il un tableau à deux dimensions, et b) un "
               "tableau à une seule ? Pourquoi d) marche-t-il et pas e) ? Comment écrire, pour e), un tableau de forme "
               "`(2, 1)` qui ajoute un nombre à chaque ligne ?"),
    ],
    note=r"a) $(2, 3) \times (3, 1) \to (2, 1)$ : deux tableaux à deux dimensions donnent un tableau à deux dimensions, "
         r"une colonne. b) $(3, 4)$ fois un tableau à une dimension de 4 nombres : NumPy le traite comme un vecteur et rend un "
         r"tableau à une dimension de 3 nombres. c) Un "
         r"vecteur de 4 fois $(4, 2)$ : un vecteur de 2 (le vecteur joue le rôle d'une ligne). d) $(2, 3)$ et $(3,)$ : la "
         r"dimension de droite coïncide, le vecteur est répété sur les 2 lignes. e) $(2, 3)$ et $(2,)$ : à droite, 3 et 2 "
         r"diffèrent et aucun ne vaut 1 : erreur. Pour ajouter un nombre par ligne, il faut une colonne `(2, 1)` : `v[:, None]` ou `v.reshape(2, 1)`.",
)

M09A_31_SIZES = "(40, 80, 160)"
M09A_31_COMPARE = '''A_big = np.random.default_rng(1).normal(size=(120, 120))
start = time.perf_counter()
naive_matmul(A_big.tolist(), A_big.tolist())
loop_seconds = time.perf_counter() - start
numpy_seconds = min(timed_product(A_big) for _ in range(5))   # the best of 5 runs
print(f"triple loop: {loop_seconds:.3f} s · @: {numpy_seconds:.6f} s · ratio ≈ {loop_seconds / max(numpy_seconds, 1e-9):.0f}")'''

M09A_31 = Ex(
    "M09a.31", "🔬", 2, 20, "Le temps d'un produit matriciel en fonction de n : une pente de 3 en échelle log-log",
    "mesurer le temps d'un produit matriciel naïf en fonction de la taille, et lire l'exposant $3$ sur une droite en "
    "échelle log-log.", "fiche §3 ; R6 (logarithmes)", tracks="C",
    body=r"""Un produit de deux matrices carrées de taille $n$ coûte $n^3$ multiplications (fiche §3) : son temps devrait varier comme $n^3$, et, en échelle log-log, $\ln t \approx 3\ln n + c$, une droite de pente 3. Écris :
- `naive_matmul(A, B)` : le produit de deux listes de listes par une **triple boucle** Python (sans NumPy), qui rend une liste de listes ;
- `time_once(n, seed=0)` : le temps (en secondes, `time.perf_counter()`) de `naive_matmul(A, A)` pour une matrice $n \times n$ `A = np.random.default_rng(seed).normal(size=(n, n)).tolist()` ;
- `loglog_slope(ns, times)` : la pente de la droite qui ajuste $\ln t$ en fonction de $\ln n$ (`np.polyfit(..., 1)[0]`).

La vérification mesure trois fois le temps pour chaque $n$ = 40, 80 et 160, et garde le plus petit (un temps mesuré varie d'une exécution à l'autre) ; puis elle vérifie : a) que `naive_matmul` donne le même résultat que `@` sur une petite matrice ; b) que la pente mesurée est entre 2,3 et 3,5. Une dernière cellule compare le temps de ta triple boucle à celui de `@` pour $n = 120$.

Dans ta copie : quelle pente as-tu mesurée ? Pourquoi n'est-elle pas exactement 3 (pense au temps qui ne dépend pas de $n^3$) ? Pourquoi garder le plus petit de trois temps plutôt que leur moyenne ? Combien de fois `@` est-il plus rapide que ta triple boucle ?""",
    todo='''def naive_matmul(A, B):
    """The product of two lists of lists, by a triple Python loop (no NumPy), as a list of lists."""
    raise NotImplementedError("trois boucles imbriquées : lignes de A, colonnes de B, puis la somme sur k")


def time_once(n, seed=0):
    """The time (seconds) of naive_matmul(A, A) for an n × n matrix A drawn with np.random.default_rng(seed)."""
    raise NotImplementedError("time.perf_counter() avant et après le calcul")


def loglog_slope(ns, times):
    """The slope of the line that fits ln(time) as a function of ln(n)."""
    raise NotImplementedError("np.polyfit(np.log(ns), np.log(times), 1)[0]")''',
    check=f'''ok_product_31, slope_31 = False, float("nan")
with checked("M09a.31 vérifications"):
    small_31 = [[1.0, -2.0, 0.5], [3.0, 0.0, -1.0]]
    other_31 = [[2.0, 1.0], [0.0, -1.0], [4.0, 3.0]]
    got_31 = naive_matmul(small_31, other_31)
    try:
        ok_product_31 = bool(np.allclose(np.array(got_31, dtype=float), np.array(small_31) @ np.array(other_31)))
    except (TypeError, ValueError):
        ok_product_31 = False
    times_31 = [min(time_once(n) for _ in range(3)) for n in {M09A_31_SIZES}]   # the best of 3 runs
    slope_31 = float(loglog_slope({M09A_31_SIZES}, times_31))
    print("temps (s) :", [round(t, 4) for t in times_31], "· pente :", round(slope_31, 2))
    if not ok_product_31:
        print("❌ Ex M09a.31 : naive_matmul ne donne pas le produit matriciel (compare avec @ sur une petite matrice).")
    elif not 2.3 <= slope_31 <= 3.5:
        print(f"❌ Ex M09a.31 : la pente mesurée, {{slope_31:.2f}}, n'est pas entre 2,3 et 3,5 : vérifie time_once (le "
              "temps du seul produit) et loglog_slope (logarithmes des deux listes).")
    else:
        print("✅ Ex M09a.31 : le temps varie à peu près comme n³.")
with checked("M09a.31"):
    naive_matmul([[1.0]], [[1.0]])                     # ⏳ while naive_matmul is not written
    wbm.check("M09a.31", bool(ok_product_31 and 2.3 <= slope_31 <= 3.5), computed=True)''',
    solution=f'''def naive_matmul(A, B):
    """The product of two lists of lists, by a triple Python loop (no NumPy), as a list of lists."""
    n, p, m = len(A), len(B), len(B[0])
    C = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            total = 0.0
            for k in range(p):
                total += A[i][k] * B[k][j]
            C[i][j] = total
    return C


def time_once(n, seed=0):
    """The time (seconds) of naive_matmul(A, A) for an n × n matrix A drawn with np.random.default_rng(seed)."""
    A = np.random.default_rng(seed).normal(size=(n, n)).tolist()
    start = time.perf_counter()
    naive_matmul(A, A)
    return time.perf_counter() - start


def loglog_slope(ns, times):
    """The slope of the line that fits ln(time) as a function of ln(n)."""
    return float(np.polyfit(np.log(ns), np.log(times), 1)[0])


times_31 = [min(time_once(n) for _ in range(3)) for n in {M09A_31_SIZES}]   # the best of 3 runs
print("times:", [round(t, 4) for t in times_31], "· slope:", round(loglog_slope({M09A_31_SIZES}, times_31), 2))''',
    after=[("solution", 'ok_product_31, slope_31 = True, loglog_slope(' + M09A_31_SIZES + ', times_31)'),
           ("record", '''wbm.record("M09a.31", True,
           mistakes={"la pente doit être entre 2,3 et 3,5, et naive_matmul doit donner le produit : la cellule de "
                     "vérification dit ce qui ne va pas": False})'''),
           ("md", "**La comparaison avec `@`** (cette cellule utilise ta fonction)."),
           ("todo", 'with checked("M09a.31 comparaison"):\n' + "\n".join("    " + line for line in M09A_31_COMPARE.splitlines())),
           ("solution", M09A_31_COMPARE)],
    note=r"La pente mesurée est en général entre 2,8 et 3 : à petite taille, le temps qui ne dépend pas de $n^3$ (créer les "
         r"listes, appeler la fonction) pèse un peu, et la pente est un peu sous 3. Le plus petit de trois temps est celui "
         r"qu'a le moins dérangé le reste de la machine (une autre tâche, le ramasse-miettes) : les perturbations ne font "
         r"qu'allonger un temps, jamais le raccourcir. `@` est des centaines de fois plus "
         r"rapide dès $n = 120$, et l'écart grandit avec $n$ : il appelle une bibliothèque optimisée (BLAS) écrite en langage compilé, qui utilise les instructions "
         r"vectorielles, le cache et plusieurs cœurs. Sa pente, mesurée de la même façon sur de petites tailles, ne vaut "
         r"pas 3 : le temps y est dominé par le lancement et par les accès à la mémoire.",
)

M09A_32_NOPIVOT = '''def solve_no_pivot(A, b):
    """Gaussian elimination WITHOUT row swaps, then back substitution (the pivots are taken on the diagonal)."""
    M = np.hstack([np.array(A, dtype=float), np.array(b, dtype=float)[:, None]])
    n = len(b)
    for k in range(n):
        for i in range(k + 1, n):
            M[i] = M[i] - M[i, k] / M[k, k] * M[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (M[i, n] - np.sum(M[i, i + 1:n] * x[i + 1:])) / M[i, i]
    return x'''

M09A_32 = Ex(
    "M09a.32", "🔬", 2, 20, "Pourquoi le pivot partiel : un petit pivot et les arrondis",
    "mesurer l'erreur d'une élimination de Gauss sans échange de lignes quand le pivot devient minuscule, et la comparer "
    "au pivot partiel.", "fiche §6 ; R1 (arrondis) ; Ex M09a.27", tracks="C",
    body=r"""Le système $\varepsilon x + y = 1$, $x + y = 2$ a, pour tout petit $\varepsilon > 0$, une solution proche de $(1, 1)$. La cellule fournie définit `solve_no_pivot(A, b)`, une élimination de Gauss **sans** échange de lignes. Écris `errors(k_values)`, qui rend, pour chaque $k$ de la liste, le couple `(erreur sans pivot, erreur avec pivot)` pour $\varepsilon = 10^{-k}$ : l'erreur est le plus grand écart, en valeur absolue, entre la solution calculée et celle de `np.linalg.solve` ; « avec pivot » utilise ta fonction `mymath.matrices.solve` (M09a.27).

La vérification calcule :
- a) l'erreur sans pivot pour $k = 18$ (4 décimales) ;
- b) l'erreur sans pivot pour $k = 8$, par son ordre de grandeur : la vérification compare l'exposant, `round(math.log10(erreur))` ;
- c) le plus petit $k$ parmi 2, 4, …, 18 pour lequel l'erreur sans pivot dépasse $10^{-2}$ (0 s'il n'y en a aucun) ;
- d) vrai ou faux : avec le pivot partiel, l'erreur reste sous $10^{-14}$ pour tous ces $k$.

Dans ta copie : que vaut le multiplicateur $\frac{1}{\varepsilon}$ de l'élimination sans pivot, et que fait-il à la seconde équation ? Pourquoi échanger les lignes règle-t-il le problème ? Pourquoi l'erreur croît-elle à peu près comme $\varepsilon^{-1} \times 10^{-16}$ ?""",
    given=M09A_32_NOPIVOT,
    todo='''def errors(k_values):
    """For each k, (max error without pivoting, max error with partial pivoting) for epsilon = 10**(-k)."""
    raise NotImplementedError("pour chaque k : A, b, la solution de np.linalg.solve, puis les deux écarts")''',
    check='''K_32 = range(2, 19, 2)
with checked("M09a.32a"):
    wbm.check("M09a.32a", errors([18])[0][0], computed=True)
with checked("M09a.32b"):
    wbm.check("M09a.32b", round(math.log10(max(errors([8])[0][0], 1e-300))), computed=True)
with checked("M09a.32c"):
    wbm.check("M09a.32c", next((k for k, (e_no, _) in zip(K_32, errors(K_32)) if e_no > 1e-2), 0), computed=True)
with checked("M09a.32d"):
    wbm.check("M09a.32d", bool(all(e_yes < 1e-14 for _, e_yes in errors(K_32))), computed=True)''',
    solution='''def errors(k_values):
    """For each k, (max error without pivoting, max error with partial pivoting) for epsilon = 10**(-k)."""
    table = []
    for k in k_values:
        A, b = np.array([[10.0 ** -k, 1.0], [1.0, 1.0]]), np.array([1.0, 2.0])
        exact = np.linalg.solve(A, b)
        table.append((float(np.max(np.abs(solve_no_pivot(A, b) - exact))),
                      float(np.max(np.abs(mymath.matrices.solve(A, b) - exact)))))
    return table


table_32 = errors(range(2, 19, 2))
for k, (e_no, e_yes) in zip(range(2, 19, 2), table_32):
    print(f"k = {k:2d} · error without pivoting {e_no:.1e} · with partial pivoting {e_yes:.1e}")''',
    record='''wbm.record("M09a.32a", table_32[-1][0], decimals=4,
           mistakes={"c'est l'erreur avec pivot : la question porte sur la première valeur du couple": table_32[-1][1]})
wbm.record("M09a.32b", round(math.log10(table_32[3][0])))
wbm.record("M09a.32c", 16, mistakes={"compare l'erreur au seuil 1e-2 = 0,01, pas à un seuil plus petit": 14,
                                      "mesure l'écart à la solution de np.linalg.solve, pas à (1, 1)": 2})
wbm.record("M09a.32d", True,
           mistakes={"avec ta fonction solve, l'erreur devrait rester minuscule : mesure l'écart à la solution de "
                     "np.linalg.solve (pas à (1, 1)), puis vérifie le pivot partiel (M09a.27)": False})''',
    note=r"Sans pivot, l'élimination retranche $\frac{1}{\varepsilon}$ fois la première ligne à la seconde : celle-ci devient "
         r"$(0, 1 - \frac{1}{\varepsilon} \mid 2 - \frac{1}{\varepsilon})$, et pour $\varepsilon$ minuscule, les nombres 1 et 2 "
         r"disparaissent dans les arrondis de $\frac{1}{\varepsilon}$ (environ 16 chiffres significatifs, R1). $y$ reste "
         r"juste, mais $x = \frac{1 - y}{\varepsilon}$ divise une erreur d'arrondi par $\varepsilon$ : l'erreur sur $x$ croît "
         r"comme $\frac{10^{-16}}{\varepsilon}$, jusqu'à donner $x = 0$ pour $\varepsilon = 10^{-18}$. Avec le pivot partiel, "
         r"on élimine avec la ligne $x + y = 2$ et un multiplicateur $\varepsilon$, minuscule : les erreurs ne sont plus "
         r"amplifiées.",
)

M09A_33_CHECK = '''with checked("M09a.33 vérifications"):
    from matplotlib.patches import Polygon
    problems = []
    for M_t in ([[0, -1], [1, 0]], [[1, 1.5], [0, 1]], [[2, 0], [0, 0.5]], [[1, 2], [0.5, 1]]):
        fig_t, ax_t = plt.subplots()
        try:
            created = drawn(draw_transform, ax_t, M_t)
        except NotImplementedError:
            plt.close(fig_t)
            raise
        polygons = [patch for patch in ax_t.patches if isinstance(patch, Polygon)]
        lines_t = [line for line in ax_t.get_lines() if len(line.get_xdata()) > 1]
        plt.close(fig_t)
        if created:
            problems.append("draw_transform ouvre sa propre figure : dessine dans l'axe reçu")
            break
        if len(lines_t) < 10:
            problems.append(f"pour M = {M_t}, {len(lines_t)} lignes seulement : trace l'image des lignes de la grille "
                            "(au moins 5 verticales et 5 horizontales)")
            break
        if not polygons:
            problems.append("aucun polygone : trace l'image du carré unité avec matplotlib.patches.Polygon")
            break
        corners = np.asarray(polygons[0].get_xy(), dtype=float)[:4]
        expected = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float) @ np.array(M_t, dtype=float).T
        if corners.shape != (4, 2) or not np.allclose(corners, expected, atol=1e-9):
            problems.append(f"pour M = {M_t}, les sommets du polygone ne sont pas les images de (0, 0), (1, 0), "
                            "(1, 1), (0, 1), dans cet ordre (l'image d'un point x est M x)")
            break
        image_lines = np.concatenate([np.column_stack([line.get_xdata(), line.get_ydata()]) for line in lines_t])
        if not np.all(np.isfinite(image_lines)):
            problems.append("des points non finis dans les lignes tracées")
            break
    if problems:
        print("❌ Ex M09a.33 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M09a.33 : l'image de la grille et du carré unité est juste, pour quatre matrices.")'''

M09A_33 = Ex(
    "M09a.33", "🎨", 1, 20, "Une matrice 2 × 2 comme transformation du plan : la grille et le carré unité",
    "tracer l'image de la grille et du carré unité par une matrice $2 \\times 2$, et voir les colonnes de la matrice "
    "comme les images des vecteurs de base.", "fiche §2 et §3 ; R0 (matplotlib)", tracks="C",
    body=r"""Une matrice $\mathbf{M}$ de forme $(2, 2)$ envoie chaque point $\mathbf{x}$ du plan sur $\mathbf{M}\mathbf{x}$. Par la lecture en colonnes (fiche §2), $\mathbf{M}\mathbf{e}_1$ et $\mathbf{M}\mathbf{e}_2$ sont les deux colonnes de $\mathbf{M}$ : elles disent où vont les vecteurs de base, et donc tout le reste. Écris `draw_transform(ax, M)`, qui trace dans l'axe `ax` :
- l'image par $\mathbf{M}$ des lignes de la grille $x = -2, -1, 0, 1, 2$ et $y = -2, -1, 0, 1, 2$ (pour $x$ ou $y$ entre $-2$ et $2$), en gris ;
- l'image du carré unité, de sommets $(0, 0)$, $(1, 0)$, $(1, 1)$, $(0, 1)$ **dans cet ordre**, avec `matplotlib.patches.Polygon` et `ax.add_patch`, en couleur.

L'image d'une ligne est encore une ligne : il suffit de transformer ses deux extrémités (ou quelques points). La cellule de la figure s'en sert pour quatre matrices : une rotation d'un quart de tour, un cisaillement, une dilatation, et une matrice singulière. Une cellule de vérification essaie ta fonction sur les mêmes matrices, dans des axes neufs.

Dans ta copie : où vont $\mathbf{e}_1$ et $\mathbf{e}_2$ pour chaque matrice ? Que devient le carré unité pour la matrice singulière, et pourquoi (pense à ses colonnes) ? Quelle matrice ramènerait la figure de la rotation à la grille de départ ?""",
    todo='''from matplotlib.patches import Polygon


def draw_transform(ax, M):
    """In ax, the image by M of the grid lines x, y in {-2, ..., 2} (grey) and of the unit square (a Polygon)."""
    raise NotImplementedError("les extrémités de chaque ligne, transformées par M, puis ax.plot ; le carré : Polygon")''',
    check='''with checked("M09a.33 figure"):
    matrices_33 = [("rotation", [[0, -1], [1, 0]]), ("cisaillement", [[1, 1.5], [0, 1]]),
                   ("dilatation", [[2, 0], [0, 0.5]]), ("singulière", [[1, 2], [0.5, 1]])]
    fig, axes = plt.subplots(1, 4, figsize=(13, 3.6))
    try:
        for ax, (name, M) in zip(axes, matrices_33):
            created = drawn(draw_transform, ax, M)
            ax.set(title=f"{name} : M = {M}", aspect="equal", xlim=(-4, 4), ylim=(-4, 4))
    except BaseException:
        plt.close(fig)
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M09a.33 : draw_transform ouvre sa propre figure : dessine dans l'axe reçu.")
    else:
        plt.show()''',
    solution='''from matplotlib.patches import Polygon


def draw_transform(ax, M):
    """In ax, the image by M of the grid lines x, y in {-2, ..., 2} (grey) and of the unit square (a Polygon)."""
    M = np.asarray(M, dtype=float)
    for c in range(-2, 3):
        for start, end in (((c, -2), (c, 2)), ((-2, c), (2, c))):    # a vertical, then a horizontal line
            ends = np.array([start, end], dtype=float) @ M.T            # each row x becomes M x
            ax.plot(ends[:, 0], ends[:, 1], color="0.75", lw=0.8)
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float) @ M.T
    ax.add_patch(Polygon(square, closed=True, facecolor="C0", alpha=0.5, edgecolor="C0"))
    ax.axhline(0, color="black", lw=0.5)
    ax.axvline(0, color="black", lw=0.5)


matrices_33 = [("rotation", [[0, -1], [1, 0]]), ("cisaillement", [[1, 1.5], [0, 1]]),
               ("dilatation", [[2, 0], [0, 0.5]]), ("singulière", [[1, 2], [0.5, 1]])]
fig, axes = plt.subplots(1, 4, figsize=(13, 3.6))
for ax, (name, M) in zip(axes, matrices_33):
    draw_transform(ax, M)
    ax.set(title=f"{name} : M = {M}", aspect="equal", xlim=(-4, 4), ylim=(-4, 4))
plt.show()''',
    after=[("md", "**Vérifications automatiques** (sur les mêmes matrices, dans des axes neufs)."),
           ("code", M09A_33_CHECK)],
    note=r"Les colonnes de $\mathbf{M}$ sont les images de $\mathbf{e}_1$ et $\mathbf{e}_2$ : la rotation envoie $\mathbf{e}_1$ "
         r"sur $(0, 1)$ et $\mathbf{e}_2$ sur $(-1, 0)$ ; le cisaillement garde $\mathbf{e}_1$ et penche $\mathbf{e}_2$ en "
         r"$(1{,}5 ;\ 1)$ ; la dilatation étire l'axe des $x$ par 2 et écrase celui des $y$ par 2. La matrice singulière a "
         r"deux colonnes proportionnelles, $(1 ;\ 0{,}5)$ et $(2, 1)$ : tout le plan est envoyé sur une droite, et le carré "
         r"unité devient un segment (un parallélogramme aplati). Aucune matrice ne peut défaire cela : c'est pourquoi elle "
         r"n'a pas d'inverse. La rotation d'un quart de tour dans l'autre sens, $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, "
         r"défait la première : c'est son inverse, et aussi sa transposée.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M09a.34 to M09a.36)
# ---------------------------------------------------------------------------
M09A_34_MISTAKES = bug_letters_mistakes(
    "ADE", "BCF",
    {"A": "refais à la main chaque produit de deux matrices",
     "D": "écris la forme de chaque résultat",
     "E": "refais à la main chaque étape du pivot de Gauss"},
    name_correct=False)

M09A_34 = Ex(
    "M09a.34", "🐛", 1, 15, "Chasse à l'erreur : `*` au lieu de `@`, une transposée oubliée, un pivot nul",
    "repérer dans du code les erreurs classiques sur les produits, les formes et le pivot de Gauss, puis calculer les "
    "bonnes valeurs.", "fiche §3, §4 et §6", tracks="C",
    body=r"""Un collègue a écrit six lignes, chacune avec un commentaire qui dit ce qu'elle doit calculer. Trois lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter de code**, trouve-les.

```python
A = np.array([[1.0, 2.0], [3.0, -1.0]])
B = np.array([[0.0, 1.0], [2.0, 2.0]])
X = np.array([[1.0, 0.0, 2.0], [-1.0, 1.0, 1.0]])      # 2 examples, 3 features
w = np.array([1.0, -2.0, 0.5])                           # weights of a linear model
P = A * B                                    # (A) the matrix product AB: its entry (2, 1), P[1, 0]
S = A + A.T                                  # (B) a symmetric matrix: S[0, 1]
y = X @ w - 0.5                              # (C) the predictions X w − 0.5 for the 2 examples: y[1]
G = X @ X.T                                  # (D) the 3 × 3 matrix XᵀX (one row per feature): G[0, 1]
M = np.array([[0.0, 2.0, 4.0], [1.0, 1.0, 3.0]])         # the augmented matrix of 2y = 4, x + y = 3
M[1] = M[1] - M[1, 0] / M[0, 0] * M[0]       # (E) an echelon form of M, x eliminated below the first pivot: M[1, 2]
R = np.diag(1 / np.array([2.0, 4.0])) @ A    # (F) D⁻¹A with D = diag(2, 4): row 1 halved, row 2 quartered: R[1, 0]
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire (une liste de 6 nombres, 4 décimales).

Dans ta copie : pour chaque ligne fausse, quelle erreur a été faite, et comment la corriger ? La ligne (D) s'exécute sans erreur : quelle est la forme de son résultat, et pourquoi Python ne signale-t-il rien ?""",
    todo='''answer_M09a_34a = ...  # a) letters, as text
answer_M09a_34b = ...  # b) a list of 6 values (4 decimals)''',
    check='''wbm.check("M09a.34a", answer_M09a_34a)
wbm.check("M09a.34b", answer_M09a_34b)''',
    solution='''answer_M09a_34a = "ADE"
A = np.array([[1.0, 2.0], [3.0, -1.0]])
B = np.array([[0.0, 1.0], [2.0, 2.0]])
X = np.array([[1.0, 0.0, 2.0], [-1.0, 1.0, 1.0]])
w = np.array([1.0, -2.0, 0.5])
P = A @ B                                    # (A) the matrix product, not the Hadamard product
S = A + A.T                                  # (B) correct
y = X @ w - 0.5                              # (C) correct
G = X.T @ X                                  # (D) XᵀX, of shape (3, 3): X @ X.T is the (2, 2) matrix of the examples
M = np.array([[1.0, 1.0, 3.0], [0.0, 2.0, 4.0]])         # (E) swap the rows first: the pivot 0 cannot be used
M[1] = M[1] - M[1, 0] / M[0, 0] * M[0]
R = np.diag(1 / np.array([2.0, 4.0])) @ A    # (F) correct
answer_M09a_34b = [float(P[1, 0]), float(S[0, 1]), float(y[1]), float(G[0, 1]), float(M[1, 2]), float(R[1, 0])]
print(answer_M09a_34a, answer_M09a_34b)''',
    record=f'''wbm.record("M09a.34a", "ADE",
           mistakes={M09A_34_MISTAKES})
VALUES_34 = [-2.0, 5.0, -3.0, -1.0, 4.0, 0.75]
wbm.record("M09a.34b", VALUES_34, decimals=4,
           mistakes={{"(A) : le produit matriciel est @ ; * multiplie élément par élément": [6.0] + VALUES_34[1:],
                      "(D) : XᵀX a une ligne et une colonne par feature ; X @ X.T en a une par exemple":
                          VALUES_34[:3] + [1.0] + VALUES_34[4:]}})''',
    note=r"(A) `A * B` est le produit de Hadamard : son élément $(2, 1)$ vaut $3 \times 2 = 6$, alors que celui de "
         r"$\mathbf{A}\mathbf{B}$ vaut $3 \times 0 + (-1) \times 2 = -2$ ; il faut `A @ B`. (B) est juste : $2 + 3 = 5$. "
         r"(C) est juste : $-1 - 2 + 0{,}5 - 0{,}5 = -3$. (D) `X @ X.T` est de forme $(2, 2)$ : c'est la matrice des "
         r"produits scalaires des **exemples**, et son élément $(1, 2)$ existe, d'où l'absence d'erreur ; $\mathbf{X}^\top"
         r"\mathbf{X}$, de forme $(3, 3)$, s'écrit `X.T @ X`, et son élément $(1, 2)$ est le produit scalaire des colonnes 1 "
         r"et 2, $1 \times 0 + (-1) \times 1 = -1$. (E) Le pivot $M_{11}$ vaut 0 : la ligne divise par zéro (`inf` et "
         r"`nan`) ; il faut d'abord échanger les deux lignes, et l'on trouve $4$. (F) est juste : $\frac{3}{4} = 0{,}75$.",
)

M09A_35_GIVEN = '''def transpose_reshape(A):          # a copy with a bug
    A = np.asarray(A, dtype=float)
    return A.reshape(A.shape[1], A.shape[0])


def matmul_square_hadamard(A, B):    # a copy with another bug
    A, B = np.asarray(A, dtype=float), np.asarray(B, dtype=float)
    if A.shape == B.shape:
        return A * B
    return A @ B'''

M09A_35_CHECK = '''with checked("M09a.35 vérifications"):
    problems = []
    ref_35 = wbm.load_mymath("ref").matrices

    def outcome(matmul_t, transpose_t, seed):
        """None if check_transpose_of_product passes, else the message of its AssertionError."""
        try:
            check_transpose_of_product(matmul_t, transpose_t, seed)
        except AssertionError as exc:
            return str(exc)
        return None

    passed = sum(outcome(ref_35.matmul, ref_35.transpose, seed) is None for seed in range(20))
    caught_reshape = [outcome(ref_35.matmul, transpose_reshape, seed) for seed in range(20)]
    caught_hadamard = [outcome(matmul_square_hadamard, ref_35.transpose, seed) for seed in range(20)]
    print(f"la bonne paire passe ton test {passed} fois sur 20 ; la transposée par reshape est attrapée "
          f"{sum(m is not None for m in caught_reshape)} fois sur 20 ; le produit de Hadamard pour des matrices carrées, "
          f"{sum(m is not None for m in caught_hadamard)} fois sur 20")
    if passed < 20:
        problems.append("ton test échoue sur les bonnes fonctions : compare avec np.allclose (des flottants), pas avec ==")
    if sum(m is not None for m in caught_reshape) < 20:
        problems.append("ton test laisse passer la transposée par reshape : tire des matrices de formes aléatoires, "
                        "avec au moins deux lignes et deux colonnes")
    if not problems and any(not (m or "").strip() for m in caught_reshape):
        problems.append("ajoute un message à ton assert (assert condition, message)")
    if not problems:
        try:
            test_transpose_of_product()
        except AssertionError as exc:
            problems.append(f"test_transpose_of_product échoue sur ta librairie : {exc}")
    if problems:
        print("❌ Ex M09a.35 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M09a.35 : ton test passe sur les bonnes fonctions et attrape la transposée fausse.")'''

M09A_35 = Ex(
    "M09a.35", "🛠️", 1, 15, "Tester une propriété : un pytest pour (AB)ᵀ = BᵀAᵀ sur des matrices aléatoires",
    "écrire un test fondé sur une propriété, vérifiée sur des matrices aléatoires de formes variées, et voir ce qu'un tel "
    "test ne peut pas attraper.", "fiche §4 ; Ex M09a.15 et M09a.25", tracks="C",
    body=r"""Un test peut comparer une fonction à un **oracle** (une fonction de confiance, comme `@` dans les tests de `mymath`), ou vérifier une **propriété** que le résultat doit avoir : ici, $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$ (M09a.15), pour des matrices tirées au hasard. Écris :
- `check_transpose_of_product(matmul, transpose, seed, trials=10)` : avec `rng = np.random.default_rng(seed)`, répète `trials` fois : tire trois dimensions $n, p, m$ entre 1 et 5 (`rng.integers(1, 6, size=3)`), deux matrices $\mathbf{A}$ $(n, p)$ et $\mathbf{B}$ $(p, m)$ de loi normale, et vérifie par `assert` (avec un message) que `transpose(matmul(A, B))` et `matmul(transpose(B), transpose(A))` ont la même forme et sont égales à $10^{-12}$ près (`np.allclose`) ;
- `test_transpose_of_product()` : le test au format pytest, sans argument, qui appelle `check_transpose_of_product` avec les fonctions de **ta** librairie (`mymath.matrices.matmul` et `mymath.matrices.transpose`) et une graine fixe.

La cellule fournie définit deux copies fausses : une transposée par `reshape`, et un produit qui rend le produit de Hadamard quand les deux matrices ont la même forme. La vérification lance ton test sur les bonnes fonctions (la référence) et sur chaque copie fausse, pour 20 graines.

Dans ta copie : pour quelles formes la transposée par `reshape` rend-elle le bon résultat, et pourquoi un test qui ne tirerait que ces formes la laisserait-il passer ? La copie au produit de Hadamard passe ton test : pourquoi la propriété est-elle vraie pour elle aussi ? Que faut-il ajouter pour l'attraper ?""",
    given=M09A_35_GIVEN,
    todo='''def check_transpose_of_product(matmul, transpose, seed, trials=10):
    """Assert (AB)ᵀ = BᵀAᵀ on `trials` pairs of random matrices of random shapes, drawn with default_rng(seed)."""
    raise NotImplementedError("tire n, p, m, puis A et B, puis assert np.allclose(...), message")


def test_transpose_of_product():
    """The pytest test: check_transpose_of_product on your matmul and transpose, with a fixed seed."""
    raise NotImplementedError("un appel à check_transpose_of_product")''',
    solution='''def check_transpose_of_product(matmul, transpose, seed, trials=10):
    """Assert (AB)ᵀ = BᵀAᵀ on `trials` pairs of random matrices of random shapes, drawn with default_rng(seed)."""
    rng = np.random.default_rng(seed)
    for _ in range(trials):
        n, p, m = rng.integers(1, 6, size=3)
        A, B = rng.normal(size=(n, p)), rng.normal(size=(p, m))
        left = np.asarray(transpose(matmul(A, B)), dtype=float)
        right = np.asarray(matmul(transpose(B), transpose(A)), dtype=float)
        assert left.shape == right.shape and np.allclose(left, right, rtol=0, atol=1e-12), (
            f"expected (AB)ᵀ = BᵀAᵀ for A of shape {A.shape} and B of shape {B.shape}, got shapes {left.shape} and "
            f"{right.shape}")


def test_transpose_of_product():
    """The pytest test: check_transpose_of_product on your matmul and transpose, with a fixed seed."""
    check_transpose_of_product(mymath.matrices.matmul, mymath.matrices.transpose, seed=35)


test_transpose_of_product()
print("the property holds for the reference")''',
    after=[("code", M09A_35_CHECK)],
    note=r"La transposée par `reshape` garde l'ordre des nombres ligne par ligne : elle rend la bonne forme, mais de mauvais "
         r"nombres, sauf pour une seule ligne ou une seule colonne, où les deux coïncident. Un test qui ne tirerait que des "
         r"vecteurs la laisserait passer ; des formes aléatoires, avec au moins deux lignes et deux colonnes, la démasquent "
         r"(une matrice carrée suffit : `reshape` la rend inchangée). Le produit de Hadamard de deux matrices carrées vérifie la propriété, car $(\mathbf{A} "
         r"\odot \mathbf{B})^\top = \mathbf{A}^\top \odot \mathbf{B}^\top = \mathbf{B}^\top \odot \mathbf{A}^\top$ : un test de "
         r"propriété ne vérifie qu'une conséquence de la bonne réponse, et une fonction fausse peut la partager. Pour "
         r"l'attraper, il faut aussi comparer à un oracle (`@`) ou à quelques produits calculés à la main, comme le font "
         r"les tests de `mymath`.",
)

M09A_36_CHECK = '''with checked("M09a.36 défi"):
    problems, worst_error, slowest, ok_36 = [], 0.0, 0.0, False
    for seed_t, kind_t in [(36, "random"), (37, "random"), (38, "needs-pivoting")]:
        rng_t = np.random.default_rng(seed_t)
        A_t = rng_t.normal(size=(400, 400))
        if kind_t == "needs-pivoting":
            A_t[np.arange(400), np.arange(400)] = 1e-14          # tiny diagonal: elimination without swaps fails
        b_t = rng_t.normal(size=400)
        exact_t = np.linalg.solve(A_t, b_t)
        start_t = time.perf_counter()
        try:
            x_t = mymath.matrices.solve(A_t.copy(), b_t.copy())
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"solve lève {type(exc).__name__} ({exc})")
            break
        seconds_t = time.perf_counter() - start_t
        slowest = max(slowest, seconds_t)
        x_t = np.asarray(x_t, dtype=float)
        if x_t.shape != (400,):
            problems.append(f"solve rend la forme {x_t.shape}, pas (400,)")
            break
        worst_error = max(worst_error, float(np.max(np.abs(x_t - exact_t))))
        if seconds_t > 1:
            break                                                # too slow: the other systems would be too
    if not problems:
        print(f"plus grande erreur : {worst_error:.1e} · temps le plus long : {slowest:.3f} s")
        if worst_error > 1e-9:
            problems.append("l'erreur dépasse 1e-9 : vérifie le pivot partiel (le troisième système a une diagonale "
                            "minuscule)")
        if slowest > 1:
            problems.append(f"plus d'une seconde ({slowest:.1f} s) : remplace les boucles sur les éléments par des "
                            "opérations NumPy sur des lignes entières, ou sur tout le bloc M[k + 1:] d'un coup")
    if problems:
        print("❌ Ex M09a.36 : " + " ; ".join(problems) + ".")
    else:
        ok_36 = True
        print("✅ Ex M09a.36 : défi réussi : trois systèmes 400 × 400, à 1e-9 près, en moins d'une seconde chacun.")
with checked("M09a.36"):
    mymath.matrices.solve([[2, 1], [1, 1]], [3, 2])          # ⏳ while solve is not written
    wbm.check("M09a.36", bool(ok_36), computed=True)'''

M09A_36 = Ex(
    "M09a.36", "🏆", 3, 30, "Défi : un système 400 × 400 résolu par ton `solve`, à 1e−9 près de NumPy, en moins d'une "
    "seconde",
    "rendre ta fonction `solve` à la fois précise et rapide sur un grand système, en vectorisant l'élimination.",
    "fiche §6 ; Ex M09a.27 et M09a.32", tracks="C",
    body=r"""Ta fonction `solve` (M09a.27) passe ses tests sur de petits systèmes. **L'objectif** : qu'elle résolve trois systèmes $400 \times 400$ (deux tirés au hasard, un troisième dont la diagonale est minuscule) à $10^{-9}$ près de `np.linalg.solve`, en **moins d'une seconde** chacun, sans `np.linalg` ni `@` (la règle de `matrices.py`).

Une élimination qui traite les nombres un par un (une boucle Python sur les lignes sous le pivot, puis une sur les colonnes) fait de l'ordre de $\frac{2}{3}n^3 \approx 4 \times 10^7$ opérations Python pour $n = 400$ : plusieurs secondes. Pistes : traiter chaque ligne d'un coup (une opération NumPy sur une ligne entière), ou mieux toutes les lignes sous le pivot d'un coup (une opération sur le bloc `M[k + 1:]`, avec le broadcasting d'une colonne de multiplicateurs), et garder le pivot partiel. La vérification s'arrête au premier système trop lent.

La vérification essaie ta fonction sur les trois systèmes ; une dernière cellule enregistre si l'objectif est atteint sur les trois.

Dans ta copie : combien de temps prenait ta première version, et combien la version finale ? Quelle opération as-tu vectorisée ? Pourquoi le troisième système échoue-t-il sans pivot partiel ?""",
    check=M09A_36_CHECK,
    solution='''print("the reference solve (mymath_ref/matrices.py) eliminates below each pivot in one NumPy operation:")
print("    factors = M[k + 1:, k] / M[k, k]")
print("    M[k + 1:] = M[k + 1:] - factors[:, None] * M[k]")''',
    after=[("solution", M09A_36_CHECK.split('with checked("M09a.36"):')[0].rstrip())],
    record='''wbm.record("M09a.36", True,
           mistakes={"l'objectif n'est pas atteint sur les trois systèmes : la cellule du défi dit pourquoi": False})''',
    note=r"La boucle sur les lignes sous le pivot se remplace par une seule opération sur le bloc : la colonne des "
         r"multiplicateurs `M[k + 1:, k] / M[k, k]`, de forme $(n - k - 1,)$, devient une colonne par `[:, None]`, et le "
         r"broadcasting la multiplie par la ligne du pivot. Il reste une boucle Python sur les $n$ colonnes (et une pour la "
         r"remontée) : le système $400 \times 400$ se résout en moins d'un dixième de seconde. Une boucle sur les lignes, chaque ligne "
         r"traitée d'un coup, passe aussi ; une boucle sur chaque nombre, non : de l'ordre de $4 \times 10^7$ opérations Python. Le troisième système a une diagonale de $10^{-14}$ : "
         r"sans échange de lignes, chaque élimination divise par ces pivots minuscules, et l'erreur explose (M09a.32).",
)


PART_A = Part("A", "Ta librairie : produit, transposée, forme réduite, rang, systèmes, inverse ; NumPy et SymPy",
              "Fiche §3 à §8. Les six fonctions de `mymath/matrices.py`, puis les mêmes calculs avec NumPy et SymPy.",
              given=TOOLS, exercises=[M09A_25, M09A_26, M09A_27, M09A_28, M09A_29])

PART_B = Part("B", "Une prédiction, deux expériences et une figure",
              "Fiche §1, §2, §3 et §6. Les formes de `@` et de `*`, le temps d'un produit, le pivot partiel, une matrice "
              "vue comme une transformation du plan.",
              exercises=[M09A_30, M09A_31, M09A_32, M09A_33])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §3, §4 et §6. Trois erreurs à trouver, un test de propriété, puis un grand système résolu vite et "
              "bien.",
              exercises=[M09A_34, M09A_35, M09A_36])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M09a.1 à M09a.14, M09a.19, M09a.20 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M09a · Matrices et systèmes linéaires — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m09a_matrices/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M09a`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M09a · Matrices et systèmes linéaires — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : formes et moyennes d'un tableau, produits matrice-vecteur et "
               "matriciels, coût des parenthèses, couche dense, embedding, transposées et $\\mathbf{X}^\\top\\mathbf{X}$, "
               "pivot de Gauss, formes réduites, inverses, rangs, un problème mis en système, passe avant, "
               "standardisation.\n"
               "- Écrire les six fonctions de `mymath/matrices.py` et les tester, puis comparer avec NumPy et SymPy.\n"
               "- Prédire des formes, mesurer le coût $n^3$ et l'effet du pivot partiel, voir une matrice comme une "
               "transformation du plan, chasser des erreurs, tester une propriété, résoudre un grand système.\n\n"
               r"**Rappel express.** $(n, p) \times (p, m) \to (n, m)$ ; $(\mathbf{A}\mathbf{B})_{ij} = \sum_k a_{ik}b_{kj}$, "
               r"$n\,p\,m$ multiplications ; $\mathbf{A}\mathbf{x} = \sum_j x_j\mathbf{a}_j$ ; $\mathbf{Z} = \mathbf{X}\mathbf{W} "
               r"+ \mathbf{b}$ ; $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$ ; opérations élémentaires : "
               r"échanger, multiplier par $\lambda \ne 0$, ajouter un multiple d'une autre ligne ; $\mathbf{A}\mathbf{A}^{-1} = "
               r"\mathbf{I}$, $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b "
               r"\\ -c & a \end{pmatrix}$ ; rang = nombre de pivots.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu prévoir la forme d'un produit, et calculer un produit matrice-vecteur sous ses deux lectures ?\n"
               "2. Sais-tu calculer un produit matriciel, son coût, et écrire une couche $\\mathbf{Z} = \\mathbf{X}\\mathbf{W} "
               "+ \\mathbf{b}$ ?\n"
               "3. Sais-tu appliquer les règles de la transposée, et calculer $\\mathbf{X}^\\top\\mathbf{X}$ ?\n"
               "4. Sais-tu résoudre un système par le pivot de Gauss, et décrire toutes ses solutions ?\n"
               "5. Sais-tu calculer une inverse et un rang, et dire quand une matrice est singulière ?\n\n"
               "**La suite** : le chapitre 9 de workbookIA (overfitting et régularisation, avec des régressions écrites "
               "en produits matriciels), puis M09b, les moindres carrés.")]


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
