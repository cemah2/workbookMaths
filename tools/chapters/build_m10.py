#!/usr/bin/env python
"""Build the two notebooks of chapter M10 from a single source (used by Claude).

    python tools/chapters/build_m10.py
    python tools/run_all_notebooks.py chapitres/m10_separabilite_convexite/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m10_separabilite_convexite/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M10.1 to M10.5, 🔗 M10.9); parts A to C are the notebook exercises. Wrong-answer
messages state a rule, never a number of the answer nor the last step that gives it. The data are new: none is a test
case of tests/test_m10_convex.py, an example of the fiche or of a docstring of convex.py, or an example of workbookIA 0B,
10 and 13 (no logic gate, no corner of the unit square labelled like a gate, no perceptron, no neuron with the weights
(0,5 ; −1 ; 2 ; 0,25) or (2, −1) and bias 0,5, no centroids (2, 3) and (0, 1), no SVM points (3, 3), (5, 4), (4, 5),
(1, 1), (0, 1), (2, 0), no images of 20 × 20 pixels, no penguins).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M10"
FOLDER = "chapitres/m10_separabilite_convexite"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M10.1", "Convexe ou non : segments, demi-plans, intersections", [
        ("a", "a list of 2 numbers", "[-1, 1]",
         '''mistakes={"t mesure l'avancée depuis a : le point vaut a + t(b − a)": [3, -1]}'''),
        ("b", "a number", "0.75",
         '''decimals=2, mistakes={"t = 0 donne a et t = 1 donne b : t mesure l'avancée depuis a": 0.25}'''),
        ("c", "letters, as text", '"ACEF"',
         '''mistakes={"F est la région au-dessus de la courbe de 1/x, convexe sur ]0, +∞[ : prends deux de ses points": '''
         '''"ACE", "D est la région sous une parabole : le milieu de (−1, 1) et (1, 1) en sort": "ACDEF", '''
         '''"B a un trou : un segment qui traverse le disque unité en sort": "ABCEF", '''
         '''"G est une croix : le segment de (3, 0) à (0, 3) passe par (1,5 ; 1,5), hors des deux bandes": "ACEFG"}'''),
        ("d", "a list of 2 numbers", "[3, 2]",
         '''mistakes={"le sommet est l'intersection des droites 2x + y = 8 et x + 2y = 7": [2, 3]}'''),
        ("e", "an integer", "4",
         '''mistakes={"compte aussi les sommets sur les axes, (0, 0) compris": {2, 3}}'''),
        ("f", "letters, as text", '"PS"',
         '''mistakes={"S est sur le bord x + 2y = 7 : K contient son bord (inégalités larges)": "P", '''
         '''"vérifie les quatre inégalités, x + 2y ≤ 7 comprise": {"PQ", "PQS"}, '''
         '''"vérifie les quatre inégalités, 2x + y ≤ 8 comprise": {"PR", "PRS"}}'''),
        ("g", "a list of 2 numbers (1 decimal)", "[1.4, 1.0]",
         '''decimals=1, mistakes={"les poids vont avec les points dans l'ordre de l'énoncé : 0,5 pour (2, 0)": [1.0, 0.8]}'''),
    ]),

    Paper("M10.2", "L'enveloppe convexe de huit points, à la main", [
        ("a", "an integer", "5",
         '''mistakes={"un point au milieu d'un côté n'est pas un sommet": 6, '''
         '''"les points intérieurs ne sont pas des sommets : seuls ceux que l'élastique touche en tournant": {7, 8}}'''),
        ("b", "a list of points", "[[-3, 1], [0, -2], [5, 0], [4, 3], [3, 5]]",
         '''mistakes={"le sens direct est le sens inverse des aiguilles d'une montre": '''
         '''[[-3, 1], [3, 5], [4, 3], [5, 0], [0, -2]], '''
         '''"(−2, 0) est au milieu d'un côté : ce n'est pas un sommet": '''
         '''[[-3, 1], [-2, 0], [0, -2], [5, 0], [4, 3], [3, 5]], '''
         '''"commence par le plus petit point : le plus petit x, puis le plus petit y": '''
         '''[[0, -2], [5, 0], [4, 3], [3, 5], [-3, 1]], '''
         '''"(4, 3) dépasse de peu la droite qui joint (5, 0) à (3, 5) : calcule le produit vectoriel, c'est un sommet": '''
         '''[[-3, 1], [0, -2], [5, 0], [3, 5]]}'''),
        ("c", "an integer", "7",
         '''mistakes={"ce point est à l'intérieur : un point sur un côté a un produit vectoriel nul avec les deux '''
         '''extrémités du côté": {2, 5}}'''),
        ("d", "a number", "1",
         '''mistakes={"u × v = u₁v₂ − u₂v₁ : l'ordre des deux vecteurs compte": -1}'''),
        ("e", "a number", "30",
         '''mistakes={"l'aire d'un triangle est la MOITIÉ de la valeur absolue du produit vectoriel": 60}'''),
        ("f", "True or False", "False",
         '''mistakes={"teste Q contre chaque côté, dans le sens direct, celui qui va de (4, 3) à (3, 5) compris": True}'''),
        ("g", "an integer", "5",
         '''mistakes={"un nouveau point peut faire disparaître un sommet : teste (4, 3) avec ses nouveaux voisins": 6}'''),
    ]),

    Paper("M10.3", "Une droite qui sépare deux petits nuages, et sa marge", [
        ("a", "a list of 6 numbers", "[16, 15, 8, -2, -5, -2]",
         '''mistakes={"le score est w · x + b : n'oublie pas b": [20, 19, 12, 2, -1, 2]}'''),
        ("b", "a number (4 decimals)", "2 / math.sqrt(5)",
         '''decimals=4, mistakes={"une marge géométrique est une distance : divise par ‖w‖": 2.0, '''
         '''"‖w‖ = √(2² + 1²), pas 2² + 1²": 0.4, '''
         '''"la marge est le minimum sur les DEUX classes, la classe −1 comprise": 8 / math.sqrt(5), '''
         '''"le score est w · x + b : avec b, tous les points sont du bon côté": -2 / math.sqrt(5)}'''),
        ("c", "a list of 2 numbers", "[0.8, 2.4]",
         '''decimals=4, mistakes={"le projeté est P₄ − (w · P₄ + b) / ‖w‖² × w, avec un score de −2 : attention au signe": '''
         '''[-0.8, 1.6], "divise le score par ‖w‖² = 5, pas par ‖w‖": [0.8 * 5 ** 0.5, 2 + 0.4 * 5 ** 0.5]}'''),
        ("d", "an interval", '"]-12 ; -2["',
         '''kind="interval", mistakes={"la séparation est stricte : aux bornes, un point est sur la droite": '''
         '''"[-12 ; -2]", "w · x + b > 0 sur la classe +1 donne b > −12, et < 0 sur la classe −1 donne b < −2": '''
         '''"]2 ; 12["}'''),
        ("e", "a number", "-7",
         '''mistakes={"le meilleur b met la droite à égale distance des deux nuages : le milieu de l'intervalle": '''
         '''{-12, -2}}'''),
        ("f", "a number (4 decimals)", "math.sqrt(5)",
         '''decimals=4, mistakes={"divise par ‖w‖ = √5": 5.0, "‖w‖ = √5, pas 5": 1.0}'''),
        ("g", "a number", "2.5",
         '''decimals=2, mistakes={"la plus grande marge est la MOITIÉ de la distance entre les enveloppes": 5.0, '''
         '''"c'est la meilleure marge pour w = (2, 1) ; en changeant aussi la direction, on fait mieux": '''
         '''math.sqrt(5)}'''),
    ]),

    Paper("M10.4", "L'astuce du biais : une droite du plan devient un plan de ℝ³ passant par l'origine", [
        ("a", "a list of 3 numbers", "[1, 0.75, -0.5]",
         '''decimals=2, mistakes={"c'est un vecteur de Δ ; la question demande celui dont la première coordonnée vaut 1 : '''
         '''divise tout par 4": [4, 3, -2], "multiplie les TROIS coordonnées par le même nombre, 1/4": [1, 3, -2], '''
         '''"le biais se place en tête : (b, w₁, w₂)": [0.75, -0.5, 1]}'''),
        ("b", "a list of 3 numbers", "[1, 3, -2]",
         '''mistakes={"la parallèle passe par p : 3 × 1 − 2 × 2 + b′ = 0 donne b′ = 1": [-1, 3, -2], '''
         '''"c'est le vecteur de Δ ; la parallèle doit passer par p": [4, 3, -2], '''
         '''"le biais se place en tête : (b′, w₁, w₂)": [3, -2, 1]}'''),
        ("c", "a number (4 decimals)", "3 / math.sqrt(13)",
         '''decimals=4, mistakes={"divise l'écart des biais par ‖w‖ = √13": 3.0, "‖w‖ = √13, pas 13": 3 / 13, '''
         '''"la distance se mesure dans le plan, avec ‖w‖ = ‖(3, −2)‖, pas avec la norme d'un vecteur relevé": '''
         '''3 / math.sqrt(14), "les biais valent 4 et 1 : leur écart est 3": 5 / math.sqrt(13)}'''),
        ("d", "a number (4 decimals)", "4 / math.sqrt(13)",
         '''decimals=4, mistakes={"la distance est |w · q + b| / ‖w‖, avec ‖w‖ = ‖(3, −2)‖ dans le plan": '''
         '''4 / math.sqrt(29), "divise par ‖w‖": 4.0, "‖w‖ = √13, pas 13": 4 / 13}'''),
        ("e", "a list of 2 numbers", "[3, 2]",
         '''mistakes={"au niveau x₀ = 1, l'équation devient −6 + 2x₁ + 3x₂ = 0 : x₁ = 3 quand x₂ = 0": [2, 3]}'''),
        ("f", "a number", "2",
         '''mistakes={"la coordonnée constante est en tête : ṽ′ = (b, w₁, w₂), avec b = 0, et l'équation devient x₁ − 3x₂ = 0": '''
         '''3, "x₁ − 3x₂ = 0 : résous en x₂, avec x₁ = 6": 18, "x₁ − 3x₂ = 0 donne x₂ = x₁ / 3, positif": -2}'''),
        ("g", "a list of 3 numbers", "[-2, 1, 2]",
         '''mistakes={"le plan doit contenir (1, 2, 0) et (1, 0, 1) : écris les deux produits scalaires nuls": '''
         '''[-2, 2, 1]}'''),
    ]),

    Paper("M10.5", "Borner une norme pas à pas : ‖v_{k+1}‖² ≤ ‖v_k‖² + c", [
        ("a", "a number", "5.0", '''decimals=2, mistakes={"la question demande le CARRÉ de la norme": math.sqrt(5)}'''),
        ("b", "a number", "-1",
         '''mistakes={"v₁ = v₀ + d₀ : calcule d'abord v₁, puis son produit scalaire avec d₁": 3}'''),
        ("c", "a number", "13",
         '''mistakes={"c'est la borne ; la question demande la valeur exacte, avec le terme 2 v₁ · d₁": 15}'''),
        ("d", "a number", "15",
         '''mistakes={"c'est la valeur exacte ; la borne ignore le terme 2 v_k · d_k, ≤ 0": 13, '''
         '''"le lemme ajoute c à chaque pas, à partir de ‖v₀‖² = 5 : deux pas": {10, 20}}'''),
        ("e", "a number (2 decimals)", "math.sqrt(505)",
         '''decimals=2, mistakes={"la question demande la norme : prends la racine carrée de la borne du carré": 505.0, '''
         '''"‖v₁₀₀‖² ≤ ‖v₀‖² + 100 c : n'oublie pas ‖v₀‖² = 5": 10 * math.sqrt(5)}'''),
        ("f", "a number", "10.0",
         '''decimals=2, mistakes={"c'est la borne de l'inégalité triangulaire, 3 + 1 + 2 + ⋯ + 6 ; le lemme s'applique ici '''
         '''au CARRÉ de la norme": 24.0, "c'est la borne de ‖v₆‖² : prends la racine carrée": 100.0, '''
         '''"chaque pas a sa propre longueur maximale : ajoute 1², 2², …, 6², pas six fois 6²": 15.0, '''
         '''"n'oublie pas le point de départ, ‖v₀‖² = 9": math.sqrt(91), '''
         '''"le lemme ajoute les CARRÉS des longueurs des pas : 1² + 2² + ⋯ + 6²": math.sqrt(30)}'''),
        ("g", "a number (2 decimals)", "math.sqrt(41)",
         '''decimals=2, mistakes={"les 5 premiers pas vont dans la direction de la position : la norme gagne 1 à chacun, la '''
         '''borne en √k ne s'applique pas à eux": math.sqrt(11), "les 5 derniers pas sont perpendiculaires à la position : '''
         '''la norme ne gagne plus que par Pythagore, ‖v_(k+1)‖² = ‖v_k‖² + 1": 11.0, '''
         '''"un pas perpendiculaire fait quand même grandir la norme : ‖v_(k+1)‖² = ‖v_k‖² + ‖d_k‖²": 6.0}'''),
    ]),

    Paper("M10.9", "Pont : seuil, sigmoïde, tanh et ReLU appliqués à un même score linéaire", [
        ("a", "a list of 3 numbers", "[0.75, 2.25, -1.75]",
         '''decimals=2, mistakes={"le score est w · x + b, avec b = −1 : n'oublie pas b": [1.75, 3.25, -0.75], '''
         '''"w = (4, −3) : le second poids est négatif": [7.5, 4.75, -0.25]}'''),
        ("b", "a list of 3 numbers", "[1, 1, 0]",
         '''mistakes={"le seuil vaut 0 ou 1 : H(z) = 0 pour z ≤ 0, jamais −1": [1, 1, -1], '''
         '''"H donne 0 ou 1, pas le score : 1 si z > 0": [0.75, 2.25, 0]}'''),
        ("c", "a list of 3 numbers (4 decimals)", "[sigmoid(0.75), sigmoid(2.25), sigmoid(-1.75)]",
         '''decimals=4, mistakes={"σ(z) = 1/(1 + e^(−z)) : le signe dans l'exponentielle": '''
         '''[sigmoid(-0.75), sigmoid(-2.25), sigmoid(1.75)]}'''),
        ("d", "a list of 3 numbers (4 decimals)", "[math.tanh(0.75), math.tanh(2.25), math.tanh(-1.75)]",
         '''decimals=4, mistakes={"tanh(z) = 2σ(2z) − 1, pas 2σ(z) − 1": '''
         '''[2 * sigmoid(0.75) - 1, 2 * sigmoid(2.25) - 1, 2 * sigmoid(-1.75) - 1]}'''),
        ("e", "a list of 3 numbers", "[0.75, 2.25, 0]",
         '''decimals=2, mistakes={"ReLU(z) = max(0, z) garde z quand il est positif": [1, 1, 0], '''
         '''"ReLU(z) = max(0, z) : un score négatif donne 0": [0.75, 2.25, -1.75]}'''),
        ("f", "a number (4 decimals)", "sigmoid(2.5)",
         '''decimals=4, mistakes={"une distance n'est pas un score : à la distance d, le score vaut d × ‖w‖ = 0,5 × 5": '''
         '''sigmoid(0.5), "le score vaut la distance MULTIPLIÉE par ‖w‖ = 5": sigmoid(0.1), '''
         '''"‖w‖ = √(4² + 3²) = 5, pas 25": sigmoid(12.5)}'''),
        ("g", "a number (4 decimals)", "math.log(17 / 3) / 5",
         '''decimals=4, mistakes={"un score n'est une distance qu'une fois divisé par ‖w‖ = 5": math.log(17 / 3), '''
         '''"‖w‖ = 5, pas 25": math.log(17 / 3) / 25, '''
         '''"σ(z) = 0,85 donne 1 + e^(−z) = 1/0,85 : isole e^(−z) avant de prendre le logarithme": math.log(1 / 0.85) / 5}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math


def sigmoid(z):
    """The logistic function 1 / (1 + exp(-z))."""
    return 1 / (1 + math.exp(-z))'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M10.1 à M10.5, 🔗 M10.9)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une liste `[2, -1]` pour un point ou un vecteur, une liste de points `[[1, 0], [-2, 3]]` ;\n"
               "- `True` / `False`, des lettres entre guillemets, `\"BD\"`, ou un intervalle entre guillemets, "
               "`\"]0 ; 4]\"` (crochet tourné vers l'extérieur : borne exclue).\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M10.12 and M10.13)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import ast
import inspect
import textwrap

import matplotlib.pyplot as plt
import numpy as np

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

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M10")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/convex.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "NumPy est permis, et `scipy.optimize.linprog` pour `is_linearly_separable` ; `scipy.spatial` est interdit "
         "(les tests comparent ton enveloppe à `scipy.spatial.ConvexHull`, et un test vérifie que tu ne t'en sers "
         "pas). Ne modifie jamais les tableaux reçus.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of convex.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_convex_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m10_convex.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m10_convex.py", "{keyword}", impl="ref")')]


NDARRAY = "la docstring demande un tableau NumPy de floats : np.array(...)"
P12 = "[[2, -1], [6, 0], [7, 4], [3, 6], [-1, 3], [4, 2], [5, 5], [0, 0], [2, 3], [4, -0.5]]"
L12 = "[[-2, 3], [4, -3], [0, 1], [2, -1]]"

M10_12 = Ex(
    "M10.12", "🔨", 2, 25, "L'enveloppe convexe dans le plan : la chaîne monotone d'Andrew · `convex_hull_2d`",
    "programmer la chaîne monotone d'Andrew, avec ses cas particuliers : points répétés, alignés, au milieu d'un côté.",
    "fiche §2", tracks="C, E", mymath="convex.py",
    body=HOWTO + rf"""

Écris `convex_hull_2d(points)` (fiche §2), en suivant la docstring : les points distincts triés par $x$ puis par $y$ (`np.unique(P, axis=0)` le fait), la chaîne du bas de gauche à droite, la chaîne du haut de droite à gauche, en retirant le dernier sommet tant que le produit vectoriel est $\le 0$, puis les deux chaînes bout à bout sans répéter leurs extrémités. Le résultat : un tableau NumPy de floats de forme $(h, 2)$, les sommets dans le sens direct à partir du plus petit point. Une `ValueError` si le nuage est vide ou n'a pas deux colonnes.

Avec $P$ = `{P12}`, la vérification calcule :
- a) `convex_hull_2d(P)` (une liste de points) ;
- b) le nombre de sommets de l'enveloppe de 200 points tirés par `np.random.default_rng(12).normal(size=(200, 2))` ;
- c) `convex_hull_2d({L12})` (quatre points alignés) ;
- d) le nom de l'erreur levée par `convex_hull_2d([])` ;
- e) le nom de l'erreur levée par `convex_hull_2d([[1, 2, 3], [4, 5, 6]])` ;
- f) le nom du type de la valeur rendue, en texte.

Dans ta copie : dessine $P$ et son enveloppe. Quel point de $P$ est au milieu d'un côté ? Quel test de ta boucle l'écarte ? Que rendrait ta fonction si le test était $< 0$ au lieu de $\le 0$ ?""",
    todo=LOAD_LEARNER,
    check=f'''P_12 = {P12}
with checked("M10.12a"):
    wbm.check("M10.12a", np.asarray(mymath.convex.convex_hull_2d(P_12)).tolist(), computed=True)
with checked("M10.12b"):
    cloud_12 = np.random.default_rng(12).normal(size=(200, 2))
    wbm.check("M10.12b", len(mymath.convex.convex_hull_2d(cloud_12)), computed=True)
with checked("M10.12c"):
    wbm.check("M10.12c", np.asarray(mymath.convex.convex_hull_2d({L12})).tolist(), computed=True)
with checked("M10.12d"):
    wbm.check("M10.12d", raised(mymath.convex.convex_hull_2d, []), computed=True)
with checked("M10.12e"):
    wbm.check("M10.12e", raised(mymath.convex.convex_hull_2d, [[1, 2, 3], [4, 5, 6]]), computed=True)
with checked("M10.12f"):
    wbm.check("M10.12f", type(mymath.convex.convex_hull_2d(P_12)).__name__, computed=True)''',
    solution=LOAD_REF + f'''
convex_hull_2d = mymath.convex.convex_hull_2d
P_12 = {P12}
print("a)", convex_hull_2d(P_12).tolist())
print("b)", len(convex_hull_2d(np.random.default_rng(12).normal(size=(200, 2)))))
print("c)", convex_hull_2d({L12}).tolist())
print("d)", raised(convex_hull_2d, []), " e)", raised(convex_hull_2d, [[1, 2, 3], [4, 5, 6]]),
      " f)", type(convex_hull_2d(P_12)).__name__)''',
    record=f'''wbm.record("M10.12a", [[-1.0, 3.0], [0.0, 0.0], [2.0, -1.0], [6.0, 0.0], [7.0, 4.0], [3.0, 6.0]], decimals=6,
           mistakes={{"(4 ; −0,5) est au milieu d'un côté : retire le dernier sommet quand le produit vectoriel est "
                      "≤ 0, pas seulement < 0": [[-1.0, 3.0], [0.0, 0.0], [2.0, -1.0], [4.0, -0.5], [6.0, 0.0],
                                                 [7.0, 4.0], [3.0, 6.0]],
                      "le sens direct est le sens inverse des aiguilles d'une montre : vérifie le signe du produit "
                      "vectoriel": [[-1.0, 3.0], [3.0, 6.0], [7.0, 4.0], [6.0, 0.0], [2.0, -1.0], [0.0, 0.0]],
                      "le premier sommet est le plus petit point dans l'ordre du tri : le plus petit x d'abord":
                          [[2.0, -1.0], [6.0, 0.0], [7.0, 4.0], [3.0, 6.0], [-1.0, 3.0], [0.0, 0.0]]}})
wbm.record("M10.12b", 11)
wbm.record("M10.12c", [[-2.0, 3.0], [4.0, -3.0]], decimals=6,
           mistakes={{"les points au milieu d'un segment ne sont pas des sommets : seules les deux extrémités restent":
                         [[-2.0, 3.0], [0.0, 1.0], [2.0, -1.0], [4.0, -3.0]],
                     "les deux chaînes se rejoignent à leurs extrémités : ne répète pas le premier sommet":
                         [[-2.0, 3.0], [4.0, -3.0], [-2.0, 3.0]]}})
wbm.record("M10.12d", "ValueError",
           mistakes={{"un nuage vide n'a pas d'enveloppe : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M10.12e", "ValueError",
           mistakes={{"des points à trois coordonnées ne sont pas des points du plan : la docstring demande une "
                      "ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M10.12f", "ndarray", mistakes={{"{NDARRAY}": {{"list", "tuple"}}}})''',
    after=tests_cells("convex_hull_2d"),
    note=r"a) Le point $(4 ;\ -0{,}5)$ est au milieu du côté qui joint $(2, -1)$ à $(6, 0)$ : le produit vectoriel "
         r"$(2 ;\ 0{,}5) \times (2 ;\ 0{,}5) = 0$ le fait retirer ; les points $(4, 2)$, $(5, 5)$ et $(2, 3)$ sont à "
         r"l'intérieur. b) Pour un nuage gaussien, l'enveloppe n'a que quelques sommets (de l'ordre de "
         r"$\sqrt{\ln n}$ en moyenne ; ici 11 sur 200 points) : presque tous les points sont à l'intérieur. c) Tous les "
         r"produits vectoriels sont nuls : chaque chaîne garde ses deux extrémités, et le résultat aussi.",
)

X13 = "[[-1, 2], [2, 1], [1, -2], [-2, -1], [5, 4], [6, 1], [4, 6], [7, 5]]"
Y13 = "[1, 1, 1, 1, -1, -1, -1, -1]"

M10_13 = Ex(
    "M10.13", "🔨", 2, 25, "Séparabilité par programmation linéaire, et marge géométrique · `is_linearly_separable, "
    "margin_of_separator`",
    "décider la séparabilité par un programme linéaire de faisabilité, et calculer la marge géométrique d'un "
    "séparateur.", "fiche §3 ; M07 (distance à un hyperplan)", tracks="C, E", mymath="convex.py",
    body=rf"""Écris, en suivant les docstrings (fiche §3) :
- `is_linearly_separable(X, y)` : `True` si et seulement si le système $y_i(\mathbf{{w}} \cdot \mathbf{{x}}_i + b) \ge 1$ a une solution $(\mathbf{{w}}, b)$, décidé par `scipy.optimize.linprog` (objectif nul, contraintes $-y_i(\mathbf{{w}} \cdot \mathbf{{x}}_i + b) \le -1$ écrites ligne par ligne, inconnues libres : `bounds=(None, None)`) ; un `bool` de Python ; une `ValueError` si les longueurs diffèrent ou si un label n'est ni $-1$ ni $+1$ ;
- `margin_of_separator(X, y, w, b)` : $\min_i \frac{{y_i(\mathbf{{w}} \cdot \mathbf{{x}}_i + b)}}{{\lVert \mathbf{{w}} \rVert}}$, un `float` de Python ; une `ValueError` si les longueurs ne vont pas, si un label n'est ni $-1$ ni $+1$, ou si $\mathbf{{w}}$ est nul.

Avec $\mathbf{{X}}$ = `{X13}` et $\mathbf{{y}}$ = `{Y13}`, la vérification calcule :
- a) `is_linearly_separable(X, y)` ;
- b) la même chose après avoir ajouté le point $(0{{,}}5 ;\ 1{{,}}5)$ avec le label $-1$ ;
- c) `is_linearly_separable([[0], [2], [3], [5], [6]], [1, 1, -1, 1, -1])` ;
- d) `margin_of_separator(X, y, [-1, -1], 4)` (4 décimales) ;
- e) `margin_of_separator(X, y, [2, 2], -8)` (4 décimales) ;
- f) le nom de l'erreur levée par `margin_of_separator(X, y, [0, 0], 1)` ;
- g) le nom de l'erreur levée par `is_linearly_separable([[0, 0], [1, 1]], [0, 1])` ;
- h) vrai ou faux : `is_linearly_separable` rend un `bool` de Python et `margin_of_separator` un `float` de Python (`type(r) is bool and type(m) is float`).

Dans ta copie : où est l'origine par rapport aux quatre points de la classe $+1$ ? Pourquoi a) serait-il faux sans la colonne de 1 (sans le biais $b$) ? Pourquoi b) est-il faux, sans aucun calcul de droite (fiche §3) ? Écris d) à la main : quel point est le plus proche de la droite $-x_1 - x_2 + 4 = 0$ ? Pourquoi e) est-il négatif, et pourquoi n'est-il pas l'opposé de d) ? Que rendrait `is_linearly_separable` avec des contraintes $\ge 0$ au lieu de $\ge 1$ ?""",
    todo=LOAD_LEARNER,
    check=f'''X_13, y_13 = {X13}, {Y13}
with checked("M10.13a"):
    wbm.check("M10.13a", mymath.convex.is_linearly_separable(X_13, y_13), computed=True)
with checked("M10.13b"):
    wbm.check("M10.13b", mymath.convex.is_linearly_separable(X_13 + [[0.5, 1.5]], y_13 + [-1]), computed=True)
with checked("M10.13c"):
    wbm.check("M10.13c", mymath.convex.is_linearly_separable([[0], [2], [3], [5], [6]], [1, 1, -1, 1, -1]),
              computed=True)
with checked("M10.13d"):
    wbm.check("M10.13d", mymath.convex.margin_of_separator(X_13, y_13, [-1, -1], 4), computed=True)
with checked("M10.13e"):
    wbm.check("M10.13e", mymath.convex.margin_of_separator(X_13, y_13, [2, 2], -8), computed=True)
with checked("M10.13f"):
    wbm.check("M10.13f", raised(mymath.convex.margin_of_separator, X_13, y_13, [0, 0], 1), computed=True)
with checked("M10.13g"):
    wbm.check("M10.13g", raised(mymath.convex.is_linearly_separable, [[0, 0], [1, 1]], [0, 1]), computed=True)
with checked("M10.13h"):
    wbm.check("M10.13h", type(mymath.convex.is_linearly_separable(X_13, y_13)) is bool
              and type(mymath.convex.margin_of_separator(X_13, y_13, [-1, -1], 4)) is float, computed=True)''',
    solution=LOAD_REF + f'''
is_linearly_separable, margin_of_separator = mymath.convex.is_linearly_separable, mymath.convex.margin_of_separator
X_13, y_13 = {X13}, {Y13}
print("a)", is_linearly_separable(X_13, y_13), " b)", is_linearly_separable(X_13 + [[0.5, 1.5]], y_13 + [-1]),
      " c)", is_linearly_separable([[0], [2], [3], [5], [6]], [1, 1, -1, 1, -1]))
print("d)", round(margin_of_separator(X_13, y_13, [-1, -1], 4), 4),
      " e)", round(margin_of_separator(X_13, y_13, [2, 2], -8), 4))
print("f)", raised(margin_of_separator, X_13, y_13, [0, 0], 1),
      " g)", raised(is_linearly_separable, [[0, 0], [1, 1]], [0, 1]))
print("h)", type(is_linearly_separable(X_13, y_13)) is bool and type(margin_of_separator(X_13, y_13, [-1, -1], 4)) is float)''',
    record=f'''wbm.record("M10.13a", True,
           mistakes={{"ces deux nuages sont séparables, mais aucune droite qui passe par l'origine ne les sépare : garde le "
                      "biais b parmi les inconnues (une colonne de 1), et des inconnues libres, bounds=(None, None)": False}})
wbm.record("M10.13b", False,
           mistakes={{"(0,5 ; 1,5) est le milieu de deux points de la classe +1 : exige y_i(w · x_i + b) ≥ 1, pas ≥ 0":
                         True}})
wbm.record("M10.13c", False,
           mistakes={{"en dimension 1, le point 3, de la classe −1, est entre deux points de la classe +1 : exige "
                      "y_i(w · x_i + b) ≥ 1": True}})
wbm.record("M10.13d", 1 / 2 ** 0.5, decimals=4,
           mistakes={{"divise par ‖w‖ = √2": 1.0, "‖w‖ = √2, pas 2": 0.5,
                     "la marge est le MINIMUM des y_i(w · x_i + b) / ‖w‖": 8 / 2 ** 0.5,
                     "multiplie chaque score par le label y_i": -12 / 2 ** 0.5}})
wbm.record("M10.13e", -8 / 2 ** 0.5, decimals=4,
           mistakes={{"la marge est signée : un point du mauvais côté compte en négatif": 8 / 2 ** 0.5,
                     "la marge est le minimum, ici atteint par le point le plus loin du mauvais côté": -1 / 2 ** 0.5}})
wbm.record("M10.13f", "ValueError",
           mistakes={{"w = 0 ne définit aucun hyperplan : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M10.13g", "ValueError",
           mistakes={{"les labels doivent valoir −1 ou +1 : la docstring demande une ValueError pour 0": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M10.13h", True,
           mistakes={{"la docstring demande un bool et un float de Python : un booléen ou un nombre de NumPy s'affiche "
                      "autrement (np.True_, np.float64(...)) ; écris bool(...) et float(...)": False}})''',
    after=tests_cells("is_linearly_separable or margin_of_separator"),
    note=r"a) L'origine est à l'intérieur de l'enveloppe de la classe $+1$ (un carré autour d'elle) : une droite qui passe "
         r"par l'origine laisse toujours un de ses sommets de l'autre côté ou dessus ; sans la colonne de 1, le programme "
         r"linéaire n'a pas de solution, et la fonction rendrait `False`. b) Le point $(0{,}5 ;\ 1{,}5)$ est le milieu de "
         r"$(-1, 2)$ et $(2, 1)$, deux points de la classe $+1$ : il est dans les deux enveloppes, aucune droite ne sépare "
         r"(fiche §3). c) Le point 3, de la classe $-1$, est dans l'intervalle $[0, 5]$, l'enveloppe de la classe $+1$. "
         r"d) Les scores "
         r"$-x_1 - x_2 + 4$ valent $3, 1, 5, 7$ sur la classe $+1$ et $-5, -3, -6, -8$ sur l'autre : le plus petit $y_i s_i$ "
         r"est 1, atteint en $(2, 1)$, et $\frac{1}{\sqrt{2}} \approx 0{,}7071$. e) $(2, 2)$ et $-8$ font $-2$ fois le couple "
         r"de d) : les côtés sont échangés, et le minimum des $y_i s_i$ devient moins le **maximum** de ceux de d), "
         r"$-\frac{16}{2\sqrt{2}}$, atteint en $(7, 5)$. Avec $\ge 0$, $\mathbf{w} = \mathbf{0}$ et $b = 0$ satisfont "
         r"toutes les contraintes : la fonction rendrait toujours `True`.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction and a figure (M10.14 and M10.15)
# ---------------------------------------------------------------------------
GIVEN_14 = '''reference_14 = wbm.load_mymath("ref", alias="mymath_ref")     # the experiment uses the reference of convex.py


def separable_fraction(n, d, trials=300, seed=14):
    """The fraction of `trials` draws of n Gaussian points of R^d, with labels -1 or +1 drawn at random, that are
    linearly separable."""
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(trials):
        X = rng.normal(size=(n, d))
        y = rng.choice([-1, 1], size=n)
        count += reference_14.convex.is_linearly_separable(X, y)
    return count / trials'''

M10_14_EXPERIMENT = '''for letter, (n, d) in zip("abcd", [(3, 1), (6, 2), (22, 10), (30, 2)]):
    print(f"{letter}) n = {n:2d} points, dimension d = {d:2d} : séparables dans {separable_fraction(n, d):.0%} des "
          f"tirages")'''

M10_14 = Ex(
    "M10.14", "🔮", 1, 10, "Prédire : n points aux labels tirés au hasard en dimension d sont-ils séparables ?",
    "prévoir à quelle vitesse la séparabilité devient rare quand le nombre de points grandit devant la dimension, "
    "puis le mesurer.", "fiche §3", tracks="C, E", hypothesis=True,
    given=GIVEN_14,
    body=r"""On tire $n$ points au hasard dans $\mathbb{R}^d$ (des coordonnées gaussiennes : presque sûrement en position générale), et on donne à chacun un label $-1$ ou $+1$ à pile ou face. Les deux classes sont-elles linéairement séparables ? La fiche (§3) dit que $d + 1$ points le sont toujours. Pour chaque cas, choisis le numéro de la bonne réponse : la proportion des tirages séparables est (1) 100 % ; (2) entre 65 % et 95 % ; (3) entre 35 % et 65 % ; (4) moins de 5 % :
- a) $n = 3$ points sur une droite ($d = 1$) ;
- b) $n = 6$ points dans le plan ($d = 2$) ;
- c) $n = 22$ points en dimension $d = 10$ ;
- d) $n = 30$ points dans le plan.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience : 300 tirages par cas, décidés par la référence de `is_linearly_separable`.""",
    todo='''prediction_M10_14a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M10_14b = ...  # b) 1, 2, 3 or 4
prediction_M10_14c = ...  # c) 1, 2, 3 or 4
prediction_M10_14d = ...  # d) 1, 2, 3 or 4''',
    check='''for letter, prediction in zip("abcd", [prediction_M10_14a, prediction_M10_14b, prediction_M10_14c,
                                         prediction_M10_14d]):
    wbm.check(f"M10.14{letter}", prediction)''',
    record='''wbm.record("M10.14a", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M10.14b", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M10.14c", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M10.14d", 4, prediction=True, choices=[1, 2, 3, 4])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(M10_14_EXPERIMENT, [f"prediction_M10_14{letter}" for letter in "abcd"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", M10_14_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : pour a), écris les huit étiquetages de trois points d'une "
               "droite ; lesquels ne sont pas séparables (pense au critère des enveloppes, fiche §3) ? "
               "Que remarques-tu en b) et en c), qui ont tous deux $n = 2(d + 1)$ ? Combien de points faut-il, en "
               "dimension $d$, pour que des labels au hasard ne soient presque jamais séparables ? Qu'est-ce que cela "
               "dit d'un classifieur linéaire qui sépare parfaitement ses données d'entraînement quand $d$ est grand "
               "devant $n$ ?"),
    ],
    note=r"T. M. Cover (1965) a compté les étiquetages séparables : pour $n$ points en position générale de "
         r"$\mathbb{R}^d$, avec un biais, la proportion est $P(n, d) = 2^{1-n}\sum_{k=0}^{d} \binom{n-1}{k}$. a) "
         r"$P(3, 1) = \frac{1 + 2}{4} = \frac{3}{4}$ : deux étiquetages sur 8 échouent, les deux où le point du milieu "
         r"est seul de sa classe (il est dans l'enveloppe de l'autre classe, le segment des deux extrêmes). b) et c) $n = 2(d + 1)$ donne exactement $\frac{1}{2}$, quelle "
         r"que soit la dimension (la somme prend la moitié des coefficients binomiaux, par symétrie). d) $P(30, 2) = "
         r"\frac{1 + 29 + 406}{2^{29}} \approx 8 \times 10^{-7}$. Avec l'astuce du biais, tout se passe en dimension "
         r"$d + 1$ : la « capacité » d'un classifieur linéaire est d'environ $2(d + 1)$ points. Quand $d$ est grand devant "
         r"$n$, séparer parfaitement l'entraînement ne prouve rien : n'importe quels labels le sont.",
)

DATA_15 = f'''X_15 = np.array({X13}, dtype=float)
y_15 = np.array({Y13})
w_15, b_15 = np.array([-1.0, -1.0]), 4.0                 # a separator of the two clouds (the one of M10.13 d)'''

M10_15_CHECK = '''with checked("M10.15 vérifications"):
    from matplotlib.patches import Polygon as PolygonPatch
    reference_15 = wbm.load_mymath("ref", alias="mymath_ref")
    problems = []
    X_t = np.array([[0.0, 4.0], [1.0, 7.0], [3.0, 6.0], [2.0, 5.0], [-1.0, 6.0],         # other data: hulls of 5 and 4
                    [4.0, 1.0], [6.0, 2.0], [5.0, -1.0], [7.0, 0.0], [5.5, 0.5]])        # vertices, one point inside
    y_t = np.array([1, 1, 1, 1, 1, -1, -1, -1, -1, -1])

    def same_polygon(ring, hull):
        """True if the closed ring visits the vertices of hull in a cyclic order (either way round)."""
        if len(ring) < 2 or not np.allclose(ring[0], ring[-1]) or len(ring) - 1 != len(hull):
            return False
        r = ring[:-1]
        return any(np.allclose(np.roll(seq, -s, axis=0), hull) for seq in (r, r[::-1]) for s in range(len(r)))

    w_t, b_t = np.array([-1.0, 2.0]), -3.0
    gamma_t = reference_15.convex.margin_of_separator(X_t, y_t, w_t, b_t)
    fig_t, ax_t = plt.subplots()
    try:
        created = drawn(draw_15, ax_t, X_t, y_t, w_t, b_t)
    finally:
        plt.close(fig_t)
    if created:
        problems.append("draw_15 ouvre sa propre figure : dessine dans l'axe reçu")
    else:
        rings = [np.asarray(line.get_xydata(), dtype=float) for line in ax_t.get_lines()]
        rings += [np.asarray(patch.get_xy(), dtype=float) for patch in ax_t.patches if isinstance(patch, PolygonPatch)]
        for label, name in ((1, "+1"), (-1, "−1")):
            hull_t = reference_15.convex.convex_hull_2d(X_t[y_t == label])
            if not any(same_polygon(r, hull_t) for r in rings):
                problems.append(f"l'enveloppe de la classe {name} doit être un polygone fermé qui suit, dans l'ordre, les "
                                f"sommets de convex_hull_2d (ax.plot en répétant le premier sommet à la fin)")
        norm_t = float(np.linalg.norm(w_t))
        levels = []
        for line in ax_t.get_lines():
            xy = np.asarray(line.get_xydata(), dtype=float)
            if len(xy) >= 2 and np.ptp(xy[:, 0]) + np.ptp(xy[:, 1]) > 0:
                distances = (xy @ w_t + b_t) / norm_t
                if np.ptp(distances) < 1e-6:
                    levels.append(float(distances[0]))
        for target, what in ((0.0, "la droite séparatrice w · x + b = 0"),
                             (gamma_t, "le bord de la marge du côté +1, à la distance γ"),
                             (-gamma_t, "le bord de la marge du côté −1, à la distance γ")):
            if not any(abs(level - target) < 1e-6 for level in levels):
                problems.append(f"il manque {what} (une droite tracée avec ax.plot)")
        offsets = [np.asarray(c.get_offsets(), dtype=float) for c in ax_t.collections if len(c.get_offsets())]
        shown = {tuple(np.round(p, 6)) for o in offsets for p in o}
        if not {tuple(np.round(p, 6)) for p in X_t} <= shown:
            problems.append("dessine tous les points (ax.scatter), une couleur par classe")
    if problems:
        print("❌ Ex M10.15 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M10.15 : les points, les deux enveloppes, la droite et les deux bords de la marge sont à leur "
              "place.")'''

M10_15 = Ex(
    "M10.15", "🎨", 1, 15, "Deux nuages, leurs enveloppes convexes et un hyperplan séparateur avec sa marge",
    "dessiner d'un coup tout le §3 : deux nuages, leurs enveloppes convexes, une droite séparatrice et la bande de sa "
    "marge.", "fiche §2 et §3 ; Ex M10.12 et M10.13", tracks="C",
    given=DATA_15,
    body=r"""Écris `draw_15(ax, X, y, w, b)`, qui dessine dans l'axe `ax` :
- les points, avec `ax.scatter`, une couleur par classe ;
- l'enveloppe convexe de chaque classe (calculée par `mymath.convex.convex_hull_2d`), comme un **polygone fermé** : `ax.plot` sur ses sommets, en répétant le premier à la fin ;
- la droite $\mathbf{w} \cdot \mathbf{x} + b = 0$ et les deux droites parallèles à la distance $\gamma$ de part et d'autre, où $\gamma$ est la marge de $(\mathbf{w}, b)$ (`mymath.convex.margin_of_separator`) : chacune avec `ax.plot`, sur deux points ou plus (sur la droite $\mathbf{w} \cdot \mathbf{x} + b = c$, résous en $x_2$ si $w_2 \ne 0$).

La cellule de la figure s'en sert sur les données de M10.13 ; une cellule de vérification l'essaie sur d'autres données, dans des axes neufs.

Dans ta copie : quels points touchent les bords de la bande ? Pourquoi la bande ne contient-elle aucun point ? Déplace la droite sans changer sa direction pour élargir la bande : jusqu'où peux-tu aller (M10.3 e) ?""",
    todo='''def draw_15(ax, X, y, w, b):
    """In ax: the two clouds (one color per class), their convex hulls as closed polygons, the line w · x + b = 0 and
    the two parallel lines at the distance of the margin, on each side."""
    raise NotImplementedError("ax.scatter ; convex_hull_2d et ax.plot fermé ; la marge, puis trois droites")''',
    check='''with checked("M10.15 figure"):
    fig, ax = plt.subplots(figsize=(6, 5))
    try:
        created = drawn(draw_15, ax, X_15, y_15, w_15, b_15)
    except BaseException:
        plt.close(fig)
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M10.15 : draw_15 ouvre sa propre figure : dessine dans l'axe reçu.")
    else:
        ax.set_aspect("equal")
        plt.show()''',
    solution='''def draw_15(ax, X, y, w, b):
    """In ax: the two clouds (one color per class), their convex hulls as closed polygons, the line w · x + b = 0 and
    the two parallel lines at the distance of the margin, on each side."""
    X, y, w = np.asarray(X, dtype=float), np.asarray(y), np.asarray(w, dtype=float)
    for label, color in ((1, "tab:blue"), (-1, "tab:orange")):
        cloud = X[y == label]
        ax.scatter(cloud[:, 0], cloud[:, 1], color=color, zorder=3)
        hull = mymath.convex.convex_hull_2d(cloud)
        ring = np.vstack([hull, hull[:1]])
        ax.plot(ring[:, 0], ring[:, 1], color=color)
    gamma = mymath.convex.margin_of_separator(X, y, w, b)
    norm = float(np.linalg.norm(w))
    xs = np.array([X[:, 0].min() - 1, X[:, 0].max() + 1])
    for level, style in ((0.0, "-"), (gamma * norm, "--"), (-gamma * norm, "--")):   # w · x + b = level
        ax.plot(xs, (level - b - w[0] * xs) / w[1], color="k", linestyle=style)


fig, ax = plt.subplots(figsize=(6, 5))
draw_15(ax, X_15, y_15, w_15, b_15)
ax.set_aspect("equal")
plt.show()''',
    after=[("md", "**Vérifications automatiques** (sur d'autres données, dans des axes neufs)."),
           ("code", M10_15_CHECK)],
    note=r"La marge de $(-1, -1)$ et $b = 4$ vaut $\frac{1}{\sqrt{2}} \approx 0{,}71$ : le bord du côté $+1$ passe par "
         r"$(2, 1)$ ; celui du côté $-1$ est à la même distance de la droite, mais aucun point de la classe $-1$ ne le touche "
         r"(le plus proche, $(6, 1)$, est à $\frac{3}{\sqrt{2}}$). En gardant la direction, le meilleur $b$ place la droite "
         r"au milieu : $b = 5$, de marge $\frac{2}{\sqrt{2}} = \sqrt{2} \approx 1{,}41$. Toutes directions confondues, la "
         r"plus grande marge vaut environ $1{,}86$, la moitié de la distance entre les deux enveloppes.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M10.16 to M10.18)
# ---------------------------------------------------------------------------
M10_16_MISTAKES = bug_letters_mistakes(
    "AF", "BCDE",
    {"A": "calcule cette ligne pour o = (0, 0), a = (1, 0), b = (0, 1) : quel signe attends-tu ?",
     "F": "une marge géométrique est une distance : que manque-t-il au score ?"},
    name_correct=False)

M10_16 = Ex(
    "M10.16", "🐛", 1, 15, "Chasse à l'erreur : un produit vectoriel de signe inversé, une marge non normalisée",
    "repérer dans du code les deux erreurs classiques de ce chapitre, et calculer ce qu'elles font.",
    "fiche §2 et §3", tracks="C",
    body=r"""Un collègue a écrit le code ci-dessous, ligne par ligne commentée. Deux lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter de code**, trouve-les.

```python
def cross(o, a, b):
    return (a[1] - o[1]) * (b[0] - o[0]) - (a[0] - o[0]) * (b[1] - o[1])   # (A) the cross product (a - o) × (b - o)

def half_hull(points):
    chain = []
    for p in points:
        while len(chain) >= 2 and cross(chain[-2], chain[-1], p) <= 0:     # (B) drop the last vertex unless left turn
            chain.pop()
        chain.append(p)
    return chain

def hull(points):
    pts = sorted(set(map(tuple, points)))                                   # (C) distinct points, by x then by y
    lower, upper = half_hull(pts), half_hull(pts[::-1])
    return lower[:-1] + upper[:-1]                                          # (D) the vertices, counterclockwise

def margin(X, y, w, b):
    scores = [yi * (np.dot(w, xi) + b) for xi, yi in zip(X, y)]             # (E) y_i (w · x_i + b) for each point
    return min(scores)                                                      # (F) the geometric margin
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) ce que rend `hull([[1, 0], [4, 1], [3, 4], [0, 3], [2, 2]])` avec ce code **tel quel** (une liste de points) ;
- c) ce que rend `margin([[1, 2], [3, 3], [0, -1], [2, -2]], [1, 1, -1, -1], [1, 2], -1)` avec ce code tel quel ;
- d) la vraie marge géométrique de ce séparateur (4 décimales).

Dans ta copie : corrige les deux lignes. Pourquoi b) donne-t-il quand même les bons sommets ? Quel test de M10.12 attrape la ligne (A), et lequel de M10.13 attrape la ligne (F) ?""",
    todo='''answer_M10_16a = ...  # a) letters, as text
answer_M10_16b = ...  # b) a list of points
answer_M10_16c = ...  # c) a number
answer_M10_16d = ...  # d) a number (4 decimals)''',
    check='''wbm.check("M10.16a", answer_M10_16a)
wbm.check("M10.16b", answer_M10_16b)
wbm.check("M10.16c", answer_M10_16c)
wbm.check("M10.16d", answer_M10_16d)''',
    solution='''def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])   # (A) corrected: a₁b₂ − a₂b₁, relative to o


def cross_as_written(o, a, b):
    return (a[1] - o[1]) * (b[0] - o[0]) - (a[0] - o[0]) * (b[1] - o[1])   # (A) as written: the opposite sign


def half_hull(points, turn):
    chain = []
    for p in points:
        while len(chain) >= 2 and turn(chain[-2], chain[-1], p) <= 0:      # (B) correct
            chain.pop()
        chain.append(p)
    return chain


def hull(points, turn=cross):
    pts = sorted(set(map(tuple, points)))                                   # (C) correct
    lower, upper = half_hull(pts, turn), half_hull(pts[::-1], turn)
    return [list(p) for p in lower[:-1] + upper[:-1]]                       # (D) correct


def margin(X, y, w, b):
    scores = [yi * (np.dot(w, xi) + b) for xi, yi in zip(X, y)]             # (E) correct
    return min(scores) / np.linalg.norm(w)                                  # (F) corrected: divided by ‖w‖


P_16 = [[1, 0], [4, 1], [3, 4], [0, 3], [2, 2]]
X_16, y_16 = [[1, 2], [3, 3], [0, -1], [2, -2]], [1, 1, -1, -1]
answer_M10_16a = "AF"
answer_M10_16b = hull(P_16, turn=cross_as_written)
answer_M10_16c = min(yi * (np.dot([1, 2], xi) - 1) for xi, yi in zip(X_16, y_16))
answer_M10_16d = margin(X_16, y_16, [1, 2], -1)
print(answer_M10_16a, answer_M10_16b, "corrected:", hull(P_16), answer_M10_16c, round(answer_M10_16d, 4))''',
    record=f'''wbm.record("M10.16a", "AF",
           mistakes={M10_16_MISTAKES})
wbm.record("M10.16b", [[0, 3], [3, 4], [4, 1], [1, 0]],
           mistakes={{"c'est l'enveloppe juste ; la question demande ce que rend le code tel quel : refais la chaîne "
                      "du bas avec le signe de la ligne (A)": [[0, 3], [1, 0], [4, 1], [3, 4]]}})
wbm.record("M10.16c", 3.0, decimals=4,
           mistakes={{"c'est la vraie marge ; la question demande ce que rend le code tel quel, sans division": 3 / 5 ** 0.5}})
wbm.record("M10.16d", 3 / 5 ** 0.5, decimals=4,
           mistakes={{"divise le plus petit y_i(w · x_i + b) par ‖w‖ = √5": 3.0, "‖w‖ = √5, pas 5": 0.6}})''',
    note=r"(A) calcule $u_2v_1 - u_1v_2$, l'opposé du produit vectoriel : chaque « à gauche » devient « à droite ». (B) à "
         r"(E) sont justes. (F) rend la plus petite marge fonctionnelle, 3 (atteinte par les deux points de la classe "
         r"$-1$), et non une distance : il faut diviser par $\lVert (1, 2) \rVert = \sqrt{5}$, d'où $\frac{3}{\sqrt{5}} "
         r"\approx 1{,}3416$. Avec le signe inversé, la chaîne du bas garde les virages à droite et construit en fait la "
         r"chaîne du haut, et réciproquement : on obtient les bons sommets, $(0, 3)$, $(3, 4)$, $(4, 1)$, $(1, 0)$, mais "
         r"dans le sens des aiguilles d'une montre. Les tests de M10.12 sur le sens direct (aire signée positive, virages à "
         r"gauche) attrapent (A) ; ceux de M10.13 qui comparent la marge à des distances attrapent (F).",
)

M10_17_CHECK = '''with checked("M10.17 vérifications"):
    reference_17 = wbm.load_mymath("ref", alias="mymath_ref")
    problems = []
    for seed in range(1700, 1720):                       # correct hulls: no problem may be reported
        rng_t = np.random.default_rng(seed)
        cloud = rng_t.normal(size=(30, 2)) if seed % 2 else rng_t.integers(0, 6, size=(40, 2)).astype(float)
        found = hull_problems(cloud, reference_17.convex.convex_hull_2d(cloud))
        if list(found) != []:
            problems.append(f"sur une enveloppe juste (graine {seed}), hull_problems rend {list(found)} au lieu de []")
            break
    grid_t = np.array([[0, 0], [2, 0], [4, 0], [4, 3], [2, 4], [0, 3], [1, 1], [2, 2], [3, 1], [0, 1]], dtype=float)
    good_t = reference_17.convex.convex_hull_2d(grid_t)                # [[0,0],[4,0],[4,3],[2,4],[0,3]]
    broken = {
        "dans le sens des aiguilles d'une montre": (np.vstack([good_t[:1], good_t[:0:-1]]), ["gauche", "dedans"]),
        "un sommet oublié": (np.delete(good_t, 2, axis=0), ["dedans"]),
        "le dernier sommet oublié": (np.delete(good_t, 4, axis=0), ["dedans"]),
        "le point (2, 0), au milieu d'un côté, ajouté comme sommet": (np.insert(good_t, 1, [2.0, 0.0], axis=0),
                                                                     ["gauche"]),
        "le point (0, 1), au milieu du dernier côté, ajouté à la fin": (np.vstack([good_t, [[0.0, 1.0]]]), ["gauche"]),
        "un départ ailleurs qu'au plus petit point": (np.roll(good_t, 1, axis=0), ["depart"]),
        "un sommet déplacé en (4, 4), qui n'est pas un point du nuage": (
            np.where(np.arange(5)[:, None] == 2, [[4.0, 4.0]], good_t), ["sommets"]),
    }
    for what, (hull_t, expected) in broken.items():
        found = list(hull_problems(grid_t, hull_t))
        if found != expected:
            problems.append(f"pour une enveloppe avec {what}, hull_problems rend {found} au lieu de {expected}")
    if problems:
        print("❌ Ex M10.17 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M10.17 : tes tests de propriétés acceptent les 20 enveloppes justes et attrapent les sept fausses, "
              "chacune pour la bonne raison.")'''

M10_17 = Ex(
    "M10.17", "🛠️", 1, 15, "Des tests de propriétés pour l'enveloppe convexe",
    "vérifier une enveloppe convexe sans en connaître la réponse, par ses propriétés, comme le font les tests "
    "automatiques.", "fiche §2 ; Ex M10.12", tracks="C",
    body=r"""Pour tester une fonction sans connaître la réponse exacte, on vérifie des **propriétés** que toute bonne réponse doit avoir (*property-based testing*). Écris `hull_problems(points, hull)`, qui rend la liste des noms des propriétés **non** respectées par `hull`, dans cet ordre, parmi :
- `"sommets"` : chaque sommet de `hull` est l'un des `points` ;
- `"gauche"` : à chaque sommet, le chemin tourne **strictement** à gauche (produit vectoriel $> 0$, en faisant le tour : le dernier sommet suivi du premier) ;
- `"dedans"` : chaque point est à gauche de chaque côté, ou dessus (produit vectoriel $\ge -10^{-9}$, fiche §2) ;
- `"depart"` : le premier sommet est le plus petit point (le plus petit $x$, puis le plus petit $y$).

Une enveloppe juste donne `[]`. On suppose que l'enveloppe a au moins trois sommets.

La cellule de vérification essaie ta fonction sur 20 enveloppes justes (`[]` attendu à chaque fois), puis sur sept enveloppes faussées : chacune doit être prise en défaut, et pour la bonne raison (le tour complet compte : le dernier sommet suivi du premier).

Dans ta copie : pourquoi une enveloppe tournée dans le sens des aiguilles d'une montre échoue-t-elle à **deux** propriétés ? Laquelle de ces propriétés attrape un point au milieu d'un côté ? Une enveloppe qui passe tes quatre tests est-elle forcément juste ? (Pense à un polygone qui oublie un sommet très proche d'un côté.)""",
    todo='''def hull_problems(points, hull):
    """The names of the properties that hull breaks, in the order "sommets", "gauche", "dedans", "depart" ([] for a
    correct convex hull of points, given counterclockwise from the smallest point)."""
    raise NotImplementedError("un test par propriété ; le produit vectoriel ; le tour complet avec le modulo")''',
    check=M10_17_CHECK,
    solution='''def hull_problems(points, hull):
    """The names of the properties that hull breaks, in the order "sommets", "gauche", "dedans", "depart" ([] for a
    correct convex hull of points, given counterclockwise from the smallest point)."""
    P, H = np.asarray(points, dtype=float), np.asarray(hull, dtype=float)
    h = len(H)

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    problems = []
    if not all(any(np.array_equal(v, p) for p in P) for v in H):
        problems.append("sommets")
    if not all(cross(H[i - 1], H[i], H[(i + 1) % h]) > 0 for i in range(h)):
        problems.append("gauche")
    if not all(cross(H[i], H[(i + 1) % h], p) >= -1e-9 for i in range(h) for p in P):
        problems.append("dedans")
    smallest = min(map(tuple, P))
    if tuple(H[0]) != smallest:
        problems.append("depart")
    return problems''',
    after=[("solution", M10_17_CHECK)],
    note=r"Une enveloppe tournée dans le mauvais sens tourne à droite à chaque sommet (« gauche » échoue) et laisse les "
         r"points intérieurs à droite de ses côtés (« dedans » échoue). Un point au milieu d'un côté fait un virage nul : "
         r"« gauche » l'attrape, grâce au **strictement**. Les quatre tests ensemble suffisent en fait : un polygone convexe "
         r"(« gauche ») dont les sommets sont des points du nuage (« sommets ») et qui contient tous les points (« dedans ») "
         r"est l'enveloppe convexe ; « depart » fixe le point de départ. Mais chaque test seul laisse passer des enveloppes "
         r"fausses : il en faut plusieurs, choisis pour attraper des erreurs différentes, comme les mutants de M09a.",
)

GIVEN_18 = '''def clouds_18(seed):
    """Two separable clouds of 25 points each in the plane (labels +1 and -1), from a seed."""
    rng = np.random.default_rng(seed)
    angle = rng.uniform(0, 2 * np.pi)
    u = np.array([np.cos(angle), np.sin(angle)])
    A = rng.normal(size=(25, 2)) * [1.6, 0.9] + 3.2 * u
    B = rng.normal(size=(25, 2)) * [1.0, 1.5] - 3.2 * u
    return np.round(np.vstack([A, B]), 2), np.array([1] * 25 + [-1] * 25)


DATASETS_18 = [clouds_18(seed) for seed in (1801, 1802, 1803)]
BEST_18 = [1.316342, 1.028871, 0.96]      # the largest possible margin of each dataset


def margin_18(X, y, w, b):
    """The geometric margin min_i y_i (w · x_i + b) / ‖w‖ (computed here with NumPy, for the check)."""
    w = np.asarray(w, dtype=float).ravel()
    return float(np.min(y * (X @ w + float(b))) / np.linalg.norm(w))'''

M10_18_CHECK = '''with checked("M10.18 défi"):
    ok_18 = False
    tree_18 = ast.parse(textwrap.dedent(inspect.getsource(best_separator_18)))
    imported_18 = {alias.name.split(".")[0] for node in ast.walk(tree_18) if isinstance(node, ast.Import)
                   for alias in node.names}
    imported_18 |= {node.module.split(".")[0] for node in ast.walk(tree_18)
                    if isinstance(node, ast.ImportFrom) and node.module}
    names_18 = set(best_separator_18.__code__.co_names)
    if "sklearn" in imported_18 or names_18 & {"sklearn", "svm", "SVC", "LinearSVC"}:
        print("❌ Ex M10.18 : le défi se fait sans scikit-learn : la fiche §3 donne de quoi trouver la meilleure droite.")
    else:
        ratios = []
        for (X, y), best in zip(DATASETS_18, BEST_18):
            w, b = best_separator_18(X, y)
            ratios.append(margin_18(X, y, w, b) / best)
        print("ta marge / la plus grande marge :", ", ".join(f"{r:.4f}" for r in ratios))
        if min(ratios) >= 0.99:
            ok_18 = True
            print("✅ Ex M10.18 : défi réussi : à 1 % de la plus grande marge sur les trois datasets.")
        else:
            print("❌ Ex M10.18 : au moins un dataset est à plus de 1 % de la plus grande marge (ou ta droite ne "
                  "sépare pas : un rapport négatif).")
with checked("M10.18"):
    best_separator_18(*DATASETS_18[0])                    # ⏳ while best_separator_18 is not written
    wbm.check("M10.18", bool(ok_18), computed=True)'''

M10_18 = Ex(
    "M10.18", "🏆", 3, 20, "Défi : la plus grande marge possible entre deux nuages donnés, à 1 % près",
    "trouver une droite séparatrice dont la marge est à 1 % de la plus grande possible, sur trois paires de nuages.",
    "fiche §2 et §3 ; Ex M10.12 et M10.13", tracks="C",
    given=GIVEN_18,
    body=r"""Trois datasets du plan, chacun fait de deux nuages séparables de 25 points (`DATASETS_18`, une liste de couples `(X, y)`) ; `BEST_18` donne la plus grande marge possible de chacun. **L'objectif** : écrire `best_separator_18(X, y)`, qui rend un couple `(w, b)` (un vecteur de 2 nombres et un nombre) dont la marge est d'au moins 99 % de la plus grande, sur les trois datasets. Sans scikit-learn ; NumPy, SciPy et ta librairie `mymath` sont permis.

Commence par le plus simple : la médiatrice des deux barycentres. Mesure sa marge avec `margin_18`, et compare à `BEST_18`. Puis sers-toi de la fiche (§3) : à direction fixée, le meilleur décalage $b$ est connu ; et la plus grande marge a une description géométrique. La vérification affiche le rapport de ta marge à la plus grande, pour chaque dataset.

Dans ta copie : quelle marge donnait la médiatrice des barycentres, et pourquoi est-elle si loin du compte ? Quelle méthode as-tu choisie ? Combien de points touchent les bords de la bande de ta meilleure droite ?""",
    todo='''def best_separator_18(X, y):
    """A couple (w, b) whose geometric margin on (X, y) is at least 99 % of the largest possible."""
    raise NotImplementedError("une direction w, le meilleur b pour elle ; ou les deux enveloppes et leurs points les plus "
                              "proches")''',
    check=M10_18_CHECK,
    solution='''def closest_on_segment(p, a, b):
    """The point of the segment [a, b] closest to p."""
    ab = b - a
    t = np.clip(np.dot(p - a, ab) / np.dot(ab, ab), 0.0, 1.0) if np.dot(ab, ab) > 0 else 0.0
    return a + t * ab


def best_separator_18(X, y):
    """A couple (w, b) whose geometric margin on (X, y) is at least 99 % of the largest possible."""
    X, y = np.asarray(X, dtype=float), np.asarray(y)
    hulls = [mymath.convex.convex_hull_2d(X[y == label]) for label in (1, -1)]
    best = (np.inf, None, None)
    for P, Q, swap in ((hulls[0], hulls[1], False), (hulls[1], hulls[0], True)):
        for p in P:                                      # each vertex against each side of the other hull
            for k in range(len(Q)):
                q = closest_on_segment(p, Q[k], Q[(k + 1) % len(Q)])
                d = float(np.linalg.norm(p - q))
                if d < best[0]:
                    best = (d, q, p) if swap else (d, p, q)
    _, p, q = best                                       # p in conv(A), q in conv(B): the closest pair
    w = p - q
    return w, -float(w @ (p + q) / 2)                    # the perpendicular bisector of [p, q]


mymath = wbm.load_mymath("ref")
for (X, y), best in zip(DATASETS_18, BEST_18):
    mean_A, mean_B = X[y == 1].mean(axis=0), X[y == -1].mean(axis=0)
    w_means = mean_A - mean_B
    first = margin_18(X, y, w_means, -w_means @ (mean_A + mean_B) / 2)
    w, b = best_separator_18(X, y)
    print(f"bisector of the means: {first:.4f} · closest pair of the hulls: {margin_18(X, y, w, b):.6f} · best {best}")''',
    after=[("solution", M10_18_CHECK.split('with checked("M10.18"):')[0].rstrip())],
    record='''wbm.record("M10.18", True,
           mistakes={"le défi n'est pas réussi : la cellule du défi dit pourquoi (un rapport sous 0,99, ou "
                     "scikit-learn)": False})''',
    note=r"La médiatrice des barycentres ne fait que 49 à 86 % de la plus grande marge : les barycentres résument mal les "
         r"bords des nuages, qui seuls comptent. Deux méthodes passent. (1) **À direction fixée**, le meilleur $b$ met la "
         r"droite à égale distance des deux nuages (fiche §3) : la marge vaut $\frac{\min_A \mathbf{u} \cdot \mathbf{x} - "
         r"\max_B \mathbf{u} \cdot \mathbf{x}}{2}$ pour $\mathbf{u} = (\cos\theta, \sin\theta)$, et il suffit de balayer "
         r"$\theta$ (720 angles donnent plus de 99,7 %). (2) **La géométrie** (le corrigé) : la plus grande marge est la "
         r"moitié de la distance entre les deux enveloppes convexes, atteinte par la médiatrice du plus court segment qui "
         r"les joint ; entre deux polygones convexes disjoints, ce segment part d'un sommet de l'un vers un côté de "
         r"l'autre, et `convex_hull_2d` réduit la recherche à quelques dizaines de couples. On peut aussi minimiser "
         r"$\lVert \mathbf{w} \rVert$ sous les contraintes $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ "
         r"(`scipy.optimize.minimize`, méthode SLSQP) : c'est le SVM à marge dure de M13b.",
)


PART_A = Part("A", "Ta librairie : enveloppe convexe, séparabilité, marge",
              "Fiche §2 et §3. Les trois fonctions de `mymath/convex.py`.",
              given=TOOLS, exercises=[M10_12, M10_13])

PART_B = Part("B", "Une prédiction et une figure",
              "Fiche §2 et §3. La séparabilité de labels tirés au hasard, puis tout le §3 sur une seule figure.",
              exercises=[M10_14, M10_15])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §2 et §3. Deux erreurs à trouver, des tests de propriétés, puis la plus grande marge.",
              exercises=[M10_16, M10_17, M10_18])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M10.1 à M10.5, M10.9 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M10 · Séparabilité linéaire et convexité — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m10_separabilite_convexite/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M10`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M10 · Séparabilité linéaire et convexité — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : segments et convexes, enveloppe convexe et produit vectoriel, "
               "séparateur et marge, astuce du biais, récurrence sur une norme, activations.\n"
               "- Écrire les trois fonctions de `mymath/convex.py` et les tester.\n"
               "- Prédire la séparabilité de labels au hasard, dessiner une marge, chasser deux erreurs, écrire des "
               "tests de propriétés, trouver la plus grande marge.\n\n"
               r"**Rappel express.** Convexe : $(1 - t)\mathbf{a} + t\mathbf{b} \in C$ ; $\mathbf{u} \times \mathbf{v} = "
               r"u_1v_2 - u_2v_1$, positif à gauche ; séparable $\iff$ $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ a une "
               r"solution $\iff$ enveloppes disjointes ; $\tilde{\mathbf{x}} = (1, \mathbf{x})$, $\tilde{\mathbf{w}} = (b, "
               r"\mathbf{w})$ ; marge $\min_i \frac{y_i(\mathbf{w} \cdot \mathbf{x}_i + b)}{\lVert \mathbf{w} \rVert}$, la "
               r"plus grande $= \frac{1}{2}\operatorname{dist}(\operatorname{conv} A, \operatorname{conv} B)$ ; "
               r"$\lVert \mathbf{v}_{k+1} \rVert^2 \le \lVert \mathbf{v}_k \rVert^2 + c \Rightarrow \lVert \mathbf{v}_k "
               r"\rVert^2 \le \lVert \mathbf{v}_0 \rVert^2 + kc$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu reconnaître un ensemble convexe, et démontrer qu'un demi-espace et une intersection de "
               "convexes le sont ?\n"
               "2. Sais-tu construire l'enveloppe convexe d'un nuage du plan, à la main et en code ?\n"
               "3. Sais-tu prouver que deux nuages ne sont pas séparables, et le décider par un programme linéaire ?\n"
               "4. Sais-tu calculer la marge d'un séparateur et la plus grande marge possible, et réécrire un hyperplan "
               "avec l'astuce du biais ?\n"
               "5. Sais-tu borner une norme pas à pas, et opposer une croissance linéaire à une croissance en √k ?\n\n"
               "**La suite** : le chapitre 10 de workbookIA (le neurone, du perceptron au neurone moderne), puis M11, "
               "la logique, l'induction et les inégalités de concentration.")]


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
