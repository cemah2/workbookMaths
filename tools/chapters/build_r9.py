#!/usr/bin/env python
"""Build the two notebooks of chapter R9 from a single source (used by Claude).

    python tools/chapters/build_r9.py
    python tools/run_all_notebooks.py chapitres/r9_geometrie_vecteurs/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/r9_geometrie_vecteurs/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ R9.1 to R9.10, 🔗 R9.13 and R9.14); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer nor the calculation that gives it. Coordinates, a
vector or a Cartesian equation [a, b, c] are answered by a list; a remarkable value of cos or sin, or an angle in
radians, by an exact value between quotes (kind="exact": "-sqrt(3)/2", "3*pi/4").
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "R9"
FOLDER = "chapitres/r9_geometrie_vecteurs"

F = 'kind="fraction", simplified=True'
X = 'kind="exact"'
XA = 'kind="exact", angle=True'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("R9.1", "Coordonnées et distance", [
        ("a", "a list", "[(-3 + 6) / 2, (2 + 14) / 2]",
         'decimals=1, mistakes={"le milieu a pour coordonnées les moyennes de celles de A et B, pas la moitié '
         'des écarts": [4.5, 6], "la moyenne de deux nombres : leur somme divisée par 2": [3, 16]}'),
        ("b", "an integer", "math.isqrt(9 ** 2 + 12 ** 2)",
         'mistakes={"la racine d\'une somme n\'est pas la somme des racines : élève les écarts au carré": 21, '
         '"AB est la racine carrée de la somme des carrés des écarts": 225}'),
        ("c", "an integer", "math.isqrt(8 ** 2 + 6 ** 2)",
         'mistakes={"la racine d\'une somme n\'est pas la somme des racines : élève les écarts au carré": 14, '
         '"AC est la racine carrée de la somme des carrés des écarts": 100}'),
        ("d", "a number (2 decimals)", "math.sqrt(1 + 18 ** 2)",
         'decimals=2, mistakes={"la racine d\'une somme n\'est pas la somme des racines : élève les écarts au '
         'carré": 19, "BC est la racine carrée de la somme des carrés des écarts": 325}'),
        ("e", "True or False", "True",
         'mistakes={"compare BC² à AB² + AC² (réciproque de Pythagore), avec les longueurs au carré": False}'),
        ("f", "a number (2 decimals)", "math.sqrt(6 ** 2 + 14 ** 2)",
         'decimals=2, mistakes={"la racine d\'une somme n\'est pas la somme des racines : élève les coordonnées au '
         'carré": 20}'),
        ("g", "an irreducible fraction, as text", "Fraction(219, 18)",
         F + ', mistakes={"un point de l\'axe des abscisses a une ordonnée nulle, mais celles de A et B comptent '
         'dans MA et MB": "3/2"}'),
        ("h", "a list", "[2 * 6 - (-3), 2 * 14 - 2]",
         'mistakes={"c\'est le milieu de [AB] ; A\' est de l\'autre côté de B, à la même distance": [1.5, 8], '
         '"c\'est le vecteur AB ; A\' est le point d\'arrivée quand on part de B": [9, 12]}'),
    ]),

    Paper("R9.2", "Vecteurs : somme, différence, produit par un nombre", [
        ("a", "a list", "[4 - 2, -1 + 3]", ''),
        ("b", "a list", "[4 + 2, -1 - 3]",
         'mistakes={"soustraire, c\'est ajouter l\'opposé, coordonnée par coordonnée": [2, 2]}'),
        ("c", "a list", "[3 * 4 - 2 * (-2), 3 * (-1) - 2 * 3]",
         'mistakes={"le produit de deux nombres négatifs est positif": [8, -9]}'),
        ("d", "a list", "[-3 - 1, 5 - 2]",
         'mistakes={"les coordonnées d\'un vecteur : arrivée moins départ": [4, -3]}'),
        ("e", "a list", "[1 + 4, 2 - 1]",
         'mistakes={"AC = u : on part de A et l\'on se déplace de u, donc C = A + u": [-3, 3]}'),
        ("f", "a list", "[5 - (-4), 1 - 3]",
         'mistakes={"ABCD dans cet ordre : AB = DC, pas AB = CD": [1, 4], '
         '"ABCD dans cet ordre : c\'est AB = DC qui donne D, pas AD = BC": [9, 4]}'),
        ("g", "True or False", "True",
         'mistakes={"deux vecteurs sont colinéaires quand leurs coordonnées sont proportionnelles : calcule '
         'xy\' − x\'y": False}'),
        ("h", "a number", "5 / -2", 'decimals=2, mistakes={"le signe : la première coordonnée de v est négative": 2.5}'),
    ]),

    Paper("R9.3", "Normes (euclidienne, avec un aperçu de L1 et L∞) et vecteurs unitaires", [
        ("a", "a number (2 decimals)", "math.sqrt(34)",
         'decimals=2, mistakes={"le carré d\'un nombre négatif est positif : (−3)² = 9": 4, '
         '"la norme est la racine de la somme des carrés": 34}'),
        ("b", "an integer", "8", 'mistakes={"la norme L1 additionne les valeurs absolues": 2}'),
        ("c", "an integer", "5", 'mistakes={"la norme L∞ est la plus grande valeur absolue": {3, -3}}'),
        ("d", "a number (2 decimals)", "2 * math.sqrt(34)",
         'decimals=2, mistakes={"‖ku‖ = |k| ‖u‖ : une norme n\'est jamais négative": -11.66, '
         '"multiplier un vecteur par k multiplie sa norme par |k|, pas par k²": 23.32}'),
        ("e", "a list (2 decimals)", "[-7 / 25, 24 / 25]",
         'decimals=2, mistakes={"divise par la norme euclidienne, la racine de la somme des carrés": '
         '[-7 / 31, 24 / 31], "même sens que v : on divise par un nombre positif, la norme": [0.28, -0.96]}'),
        ("f", "a list, in increasing order", "[-3, 3]",
         'mistakes={"t² = 9 a deux solutions, opposées": [3], '
         '"‖(t ; 2)‖² = t² + 4 : la norme vaut √13, donc son carré vaut 13": [-1, 1]}'),
        ("g", "a number (1 decimal)", "math.sqrt(2 ** 2 + 21 ** 2)",
         'decimals=1, mistakes={"la norme d\'une somme n\'est pas la somme des normes : additionne d\'abord les '
         'vecteurs": 30.8}'),
        ("h", "an integer", "float(4 + 6)",
         'decimals=2, mistakes={"c\'est la distance euclidienne ; la distance L1 additionne les valeurs absolues '
         'des écarts": 7.21, "les valeurs absolues des écarts : |−2 − 4| = 6": 2}'),
    ]),

    Paper("R9.4", "Équations de droites", [
        ("a", "a number", "(-2 - 4) / (3 - (-1))",
         'decimals=2, mistakes={"la pente est l\'écart des ordonnées divisé par l\'écart des abscisses": -0.67, '
         '"le point mis en premier en haut doit être en premier en bas": 1.5}'),
        ("b", "a number", "4 - (-1.5) * (-1)",
         'decimals=2, mistakes={"p = y_A − m x_A, avec les signes de m et de x_A": 5.5}'),
        ("c", "a list", "[2, -3]",
         'mistakes={"un vecteur directeur (1 ; m) : la seconde coordonnée se lit avec le signe de la pente": [2, 3]}'),
        ("d", "a list [a, b, c]", "[3, 2, -5]",
         'mistakes={"vérifie ton équation avec les coordonnées de A et de B : chacune doit donner 0": [3, -2, -5], '
         '"tout passer du même côté change le signe de p": [3, 2, 5]}'),
        ("e", "an irreducible fraction, as text", "Fraction(4, 6)",
         F + ', mistakes={"isole y : 6y = 4x + 9": "-2/3", "pour ax + by + c = 0, la pente vaut −a/b, pas −b/a": '
         '"3/2"}'),
        ("f", "a number", "1 - (-1.5) * 2",
         'decimals=2, mistakes={"une parallèle a la même pente, pas la même ordonnée à l\'origine : elle passe par '
         'C": 2.5}'),
        ("g", "a list", "[1, 1]", ''),
        ("h", "a list [a, b, c]", "[1, 0, 2]",
         'mistakes={"la droite verticale x = −2 s\'écrit x + 2 = 0": [1, 0, -2], '
         '"les deux points ont la même abscisse : la droite est verticale, son équation ne contient pas y": '
         '[0, 1, 2]}'),
    ]),

    Paper("R9.5", "Le produit scalaire en coordonnées", [
        ("a", "an integer", "2 * (-3) + 5 * 1",
         'mistakes={"multiplie les coordonnées de même rang, puis additionne les deux produits": -11}'),
        ("b", "an integer", "2 * 6 + 5 * 3", ''),
        ("c", "an integer", "-3 * 6 + 1 * 3", ''),
        ("d", "an integer", "float(2 * 2 + 5 * 5)",
         'decimals=2, mistakes={"u·u = ‖u‖², sans racine carrée": 5.39}'),
        ("e", "an integer", "(2 - 3) * 6 + (5 + 1) * 3",
         'mistakes={"additionne d\'abord u et v, coordonnée par coordonnée": 27}'),
        ("f", "an integer", "2 * (-3) * (2 * (-3) + 5 * 1)",
         'mistakes={"(2u)·(−3v) = 2 × (−3) × (u·v), avec le signe": -6}'),
        ("g", "a number", "-5 * 4 // 2",
         'mistakes={"orthogonaux : 2t + 5 × 4 = 0, puis isole t avec son signe": 10}'),
        ("h", "True or False", "True",
         'mistakes={"le signe du produit scalaire donne la nature de l\'angle : positif, aigu": False}'),
    ]),

    Paper("R9.6", "Orthogonalité et projections simples", [
        ("a", "True or False", "True", 'mistakes={"calcule le produit scalaire : nul, ils sont orthogonaux": False}'),
        ("b", "a list", "[4, 10]",
         'mistakes={"écris 5 × 4 + (−2) × y = 0, puis isole y avec son signe": [4, -10]}'),
        ("c", "a number", "-2 / 5",
         'decimals=2, mistakes={"3k + 2(k + 1) = 0 : développe 2(k + 1), puis isole k avec son signe": 0.4}'),
        ("d", "True or False", "True",
         'mistakes={"l\'angle en A est celui de AB et AC : calcule leur produit scalaire": False}'),
        ("e", "a number (2 decimals)", "20 / math.sqrt(10)",
         'decimals=2, mistakes={"la longueur de la projection est u·v divisé par ‖u‖": 20, '
         '"c\'est le coefficient k de p = k u ; la longueur se divise par ‖u‖, pas par ‖u‖²": 2}'),
        ("f", "a list", "[6, 2]",
         'mistakes={"p = (u·v / ‖u‖²) u : divise par le carré de la norme": [60, 20]}'),
        ("g", "a list", "[-1, 3]", 'mistakes={"le reste est v − p, pas p − v": [1, -3]}'),
        ("h", "True or False", "True",
         'mistakes={"compare les vecteurs directeurs (1 ; m) des deux droites par leur produit scalaire": False}'),
    ]),

    Paper("R9.7", "Degrés et radians, cosinus et sinus remarquables", [
        ("a", "an irreducible fraction, as text", "Fraction(135, 180)",
         F + ', mistakes={"θ en radians = θ en degrés × π/180 : 180° donnent π": "4/3"}'),
        ("b", "an integer", "7 * 180 // 6", ''),
        ("c", "a number (1 decimal)", "180 / math.pi",
         'decimals=1, mistakes={"de radians en degrés, on multiplie par 180/π (π radians donnent 180°)": 0.0175}'),
        ("d", "an exact value, as text", "sp.cos(5 * sp.pi / 6)",
         X + ', mistakes={"5π/6 = π − π/6 : c\'est le cosinus de π/6 (au signe près) qui compte, pas celui de '
         'π/3": "-1/2"}'),
        ("e", "an exact value, as text", "sp.sin(7 * sp.pi / 4)", X),
        ("f", "an exact value, as text", "sp.cos(3 * sp.pi / 2)",
         X + ', mistakes={"3π/2 est en bas du cercle : regarde son abscisse": "-1"}'),
        ("g", "an exact value, as text", "sp.sin(11 * sp.pi / 6)",
         X + ', mistakes={"11π/6 = 2π − π/6 : le sinus de π/6 vaut 1/2, celui de π/3 vaut √3/2": "-sqrt(3)/2"}'),
        ("h", "an exact value, as text", "sp.sin(5 * sp.pi / 2)",
         X + ', mistakes={"5π/2 = π/2 + 2π : un tour complet ramène au même point": "-1"}'),
    ]),

    Paper("R9.8", "Les courbes de cos et de sin : période, symétries, et arccos sur [0, π]", [
        ("a", "an exact value, as text", "2 * sp.pi / 3",
         XA + ', mistakes={"multiplier l\'angle par 3 fait tourner 3 fois plus vite : la période est divisée par '
         '3": "6*pi", "la période dépend du facteur 3 devant t": "2*pi"}'),
        ("b", "a list, in increasing order", "[90, 270]",
         'mistakes={"le cosinus s\'annule deux fois par tour, en haut et en bas du cercle": [90], '
         '"ce sont les zéros du sinus ; le cosinus est l\'abscisse du point": [0, 180]}'),
        ("c", "an integer", "2",
         'mistakes={"deux points du cercle ont la même ordonnée 0,3 : un de chaque côté de l\'axe vertical": 1}'),
        ("d", "an exact value, as text", "sp.pi / 4", XA),
        ("e", "an exact value, as text", "sp.pi / 3",
         XA + ', mistakes={"arccos rend toujours un angle de [0 ; π], qui a le même cosinus": "5*pi/3"}'),
        ("f", "True or False", "True",
         'mistakes={"π − x est le symétrique de x par rapport à l\'axe vertical : même ordonnée": False}'),
        ("g", "an integer", "3 + 2", 'mistakes={"cos x vaut au plus 1, et 2 cos x au plus 2": 3}'),
        ("h", "an integer", "2",
         'mistakes={"règle de la chaîne : la dérivée de sin(2x) est 2 cos(2x)": 1}'),
    ]),

    Paper("R9.9", "L'angle entre deux vecteurs", [
        ("a", "a number (4 decimals)", "1 / math.sqrt(50)",
         'decimals=4, mistakes={"divise le produit scalaire par le produit des normes": 1, '
         '"le produit des normes est √5 × √10 = √50, pas 5 × 10": 0.02}'),
        ("b", "a number (1 decimal)", "math.degrees(math.acos(1 / math.sqrt(50)))",
         'decimals=1, mistakes={"math.acos rend des radians : convertis en degrés": 1.4}'),
        ("c", "an integer", "135",
         'mistakes={"le produit scalaire est négatif : l\'angle est obtus": 45}'),
        ("d", "an integer", "150",
         'mistakes={"le produit scalaire est négatif : l\'angle est obtus": 30}'),
        ("e", "an exact value, as text", "sp.pi",
         XA + ', mistakes={"deux vecteurs de sens contraires font un angle plat, pas nul": "0"}'),
        ("f", "a number (1 decimal)", "math.degrees(math.acos(4 / (4 * math.sqrt(10))))",
         'decimals=1, mistakes={"math.acos rend des radians : convertis en degrés": 1.2}'),
        ("g", "an integer", "45",
         'mistakes={"l\'angle en B est celui des vecteurs BA et BC, qui partent de B": 135}'),
        ("h", "a number (1 decimal)", "math.degrees(math.acos(6 / math.sqrt(180)))",
         'decimals=1, mistakes={"l\'angle en C est celui de CA et CB, qui partent de C ; la somme des angles d\'un '
         'triangle vaut 180°": 116.6}'),
    ]),

    Paper("R9.10", "Distances et produits scalaires dans ℝ³ et ℝ⁴", [
        ("a", "an integer", "math.isqrt(1 + 16 + 64)",
         'mistakes={"la norme est la racine de la somme des carrés des trois coordonnées": {13, 81}}'),
        ("b", "an integer", "1 * 3 + 4 * (-2) + 8 * 1", ''),
        ("c", "an integer", "math.isqrt(2 ** 2 + 6 ** 2 + 3 ** 2)",
         'mistakes={"la racine d\'une somme n\'est pas la somme des racines : élève les écarts au carré": 11}'),
        ("d", "a number (3 decimals)", "3 / (9 * math.sqrt(14))",
         'decimals=3, mistakes={"divise par le produit des deux normes, pas par une seule": {0.333, 0.802}}'),
        ("e", "True or False", "True", 'mistakes={"calcule le produit scalaire des quatre coordonnées": False}'),
        ("f", "a number (2 decimals)", "math.sqrt(27)",
         'decimals=2, mistakes={"la norme est la racine de la somme des carrés": 27, '
         '"c\'est la norme L1 ; ‖y‖ est la norme euclidienne": 9}'),
        ("g", "an integer", "3 + 1 + 1 + 4",
         'mistakes={"la norme L1 additionne les valeurs absolues : |−1| = 1": 7}'),
        ("h", "an irreducible fraction, as text", "Fraction(4, 3)",
         F + ', mistakes={"2 + 3t − 2 − 4 = 0 : isole t avec son signe": "-4/3"}'),
    ]),

    Paper("R9.13", "Deux recettes, deux vecteurs d'ingrédients : la similarité cosinus", [
        ("a", "an integer", "5 * 5 + 1 * 5 + 1 * 5 + 10 * 0", ''),
        ("b", "a number (2 decimals)", "math.sqrt(25 + 1 + 1 + 100)",
         'decimals=2, mistakes={"la norme est la racine de la somme des carrés": 127}'),
        ("c", "a number (2 decimals)", "math.sqrt(75)",
         'decimals=2, mistakes={"la norme est la racine de la somme des carrés": 75}'),
        ("d", "a number (3 decimals)", "35 / (math.sqrt(127) * math.sqrt(75))",
         'decimals=3, mistakes={"la similarité cosinus divise le produit scalaire par le produit des normes": 35}'),
        ("e", "a number (3 decimals)", "55 / (math.sqrt(75) * 7)", 'decimals=3'),
        ("f", "a number (3 decimals)", "102 / 127", 'decimals=3'),
        ("g", "a letter, as text", '"q"',
         'mistakes={"compare les similarités cosinus, pas les produits scalaires : un grand vecteur a un grand '
         'produit scalaire avec presque tout": "p"}'),
        ("h", "a number (1 decimal)", "math.degrees(math.acos(35 / (math.sqrt(127) * math.sqrt(75))))",
         'decimals=1, mistakes={"math.acos rend des radians : convertis en degrés": 1.2}'),
    ]),

    Paper("R9.14", "Un neurone trace une droite : w₁x₁ + w₂x₂ + b = 0", [
        ("a", "an integer", "1 * 3 + 3 * 2 - 6",
         'mistakes={"n\'oublie pas le biais b dans z": 9}'),
        ("b", "an integer", "1 * 0 + 3 * 1 - 6", 'mistakes={"n\'oublie pas le biais b dans z": 3}'),
        ("c", "an irreducible fraction, as text", "Fraction(-1, 3)",
         F + ', mistakes={"isole x₂ : divise toute l\'équation par son coefficient": "-1", '
         '"3x₂ = −x₁ + 6 : la pente est négative": "1/3"}'),
        ("d", "an integer", "6 // 3",
         'mistakes={"isole x₂ : le biais aussi se divise par le coefficient de x₂": 6, '
         '"3x₂ = −x₁ + 6 : le biais change de signe en passant de l\'autre côté": -2}'),
        ("e", "True or False", "True",
         'mistakes={"calcule le produit scalaire de w et du vecteur directeur": False}'),
        ("f", "a list", "[6, 0]",
         'mistakes={"sur l\'axe des x₁, la coordonnée x₂ est nulle (et non x₁)": [0, 2]}'),
        ("g", "True or False", "False",
         'mistakes={"des équations proportionnelles décrivent la même droite": True}'),
        ("h", "an integer", "3",
         'mistakes={"z doit être strictement positif : calcule z pour chaque point, biais compris": {2, 4}}'),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math
from fractions import Fraction

import sympy as sp'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ R9.1 à R9.10, 🔗 R9.13 et R9.14)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"5/9\"` ;\n"
               "- une valeur exacte entre guillemets, avec `sqrt` et `pi`, `\"sqrt(5)/3\"` ou `\"2*pi/5\"` ;\n"
               "- des coordonnées, un vecteur ou une équation $[a, b, c]$ par une liste entre crochets, "
               "`[-1.25, 1]` ; vrai ou faux par `True` ou `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (R9.16 to R9.19)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np

from wbm.nbtools import checked, drawn, run_pytest_group, verdict


def raised(function, *args):
    """The name of the exception that function(*args) raises, or "aucune" if it returns.

    NotImplementedError (a TODO not done yet) goes through, for wbm.attempt to show ⏳."""
    try:
        function(*args)
    except NotImplementedError:
        raise
    except Exception as exc:  # noqa: BLE001 - any other error is the answer
        return type(exc).__name__
    return "aucune"


def normalized(equation):
    """The equation (a, b, c) divided by the first non-zero of a and b, rounded: one form for every equation of a line."""
    a, b, c = equation
    first = a if a != 0 else b
    return [round(x / first, 4) + 0.0 for x in (a, b, c)]'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="R9")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme dans les chapitres précédents). Ouvre ta copie "
         "`mon_travail/mymath/plane.py`, lis la docstring de la fonction en entier, remplace la ligne "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Comme dans tous les chapitres R0 à R9, Python pur et le "
         "module `math` (importe-le en haut du fichier : `import math`) : ni NumPy, ni SymPy (un test le vérifie). "
         "Écris toi-même les sommes de produits et de carrés (plutôt que `math.dist` ou `math.hypot`, qui feraient "
         "le travail à ta place) : c'est l'exercice. Les tests comparent tes résultats à NumPy et à des calculs "
         "exacts avec `Fraction`. Une cellule qui ne s'arrête pas (l'étoile `[*]` reste affichée) : interromps-la "
         "(■, *Interrupt*), puis cherche une boucle `while` dont la condition reste toujours vraie.")

WRONG_ERROR = "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)"
OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "RecursionError", "TypeError",
                "ZeroDivisionError"]


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of plane.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_r9_plane.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_r9_plane.py", "{keyword}", impl="ref")')]


R9_16 = Ex(
    "R9.16", "🔨", 1, 15, "Le vecteur entre deux points et sa norme · `vector`, `norm`",
    "programmer les coordonnées d'un vecteur et sa norme, dans n'importe quelle dimension.",
    "fiche §2, §3 et §8", tracks="C, E", mymath="plane.py",
    body=HOWTO + """

Écris `vector(A, B)` puis `norm(u)` dans `mon_travail/mymath/plane.py` (fiche §2 et §3). Un point et un vecteur sont des tuples de coordonnées, de n'importe quelle longueur (§8). `vector` renvoie un tuple, arrivée moins départ, et lève une `ValueError` si les deux points n'ont pas le même nombre de coordonnées ; `norm` renvoie un flottant.

La vérification calcule :
- a) `vector((-1, 4), (6, -2))` ;
- b) `vector((1, 2, 3), (0, 0, 0))` ;
- c) le nom de l'erreur levée par `vector((1, 2), (1, 2, 3))` (avec `raised`, de la cellule des outils) ;
- d) la liste `[norm((7, -24)), norm((1, 1, 1, 1)), norm((0, 0))]` ;
- e) le type de `norm((7, -24))`, en texte (`"float"` pour un flottant) ;
- f) la distance entre les points $(0 ; 2)$ et $(20 ; 23)$, calculée avec tes deux fonctions.

Puis, dans ta copie : pourquoi `norm` n'a-t-elle besoin d'aucun cas particulier pour la dimension 1, où $\\lVert (x) \\rVert = \\lvert x \\rvert$ ?""",
    todo=LOAD_LEARNER,
    check='''with checked("R9.16a"):
    wbm.check("R9.16a", mymath.plane.vector((-1, 4), (6, -2)), computed=True)
with checked("R9.16b"):
    wbm.check("R9.16b", mymath.plane.vector((1, 2, 3), (0, 0, 0)), computed=True)
with checked("R9.16c"):
    wbm.check("R9.16c", raised(mymath.plane.vector, (1, 2), (1, 2, 3)), computed=True)
with checked("R9.16d"):
    wbm.check("R9.16d", [mymath.plane.norm((7, -24)), mymath.plane.norm((1, 1, 1, 1)), mymath.plane.norm((0, 0))],
              computed=True)
with checked("R9.16e"):
    wbm.check("R9.16e", type(mymath.plane.norm((7, -24))).__name__, computed=True)
with checked("R9.16f"):
    wbm.check("R9.16f", mymath.plane.norm(mymath.plane.vector((0, 2), (20, 23))), computed=True)''',
    solution=LOAD_REF + '''
vector, norm = mymath.plane.vector, mymath.plane.norm
print("a)", vector((-1, 4), (6, -2)), " b)", vector((1, 2, 3), (0, 0, 0)), " c)", raised(vector, (1, 2), (1, 2, 3)))
print("d)", [norm((7, -24)), norm((1, 1, 1, 1)), norm((0, 0))], " e)", type(norm((7, -24))).__name__)
print("f)", norm(vector((0, 2), (20, 23))))''',
    record=f'''wbm.record("R9.16a", [7, -6], mistakes={{"arrivée moins départ : B − A, pas A − B": [-7, 6]}})
wbm.record("R9.16b", [-1, -2, -3], mistakes={{"arrivée moins départ : B − A, pas A − B": [1, 2, 3]}})
wbm.record("R9.16c", "ValueError",
           mistakes={{"des dimensions différentes : lève une ValueError (zip s'arrêterait sans rien dire)": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("R9.16d", [25.0, 2.0, 0.0],
           mistakes={{"la norme est la racine carrée de la somme des carrés": [625, 4, 0],
                     "élève chaque coordonnée au carré, puis prends la racine de la somme": [31, 4, 0]}})
wbm.record("R9.16e", "float",
           mistakes={{"math.sqrt rend un flottant : renvoie la racine carrée, pas son carré": "int"}})
wbm.record("R9.16f", 29.0, decimals=4,
           mistakes={{"la distance est la norme du vecteur qui relie les deux points": 841}})''',
    after=tests_cells("test_vector_ or test_norm_ or test_plane_uses"),
    note="Les vecteurs de a) et b) ont 2 et 3 coordonnées : une boucle (ou une compréhension) sur les coordonnées "
         "marche dans toutes les dimensions. En dimension 1, $\\sqrt{x^2} = \\lvert x \\rvert$ : la formule générale "
         "couvre ce cas. La distance de f) vaut $\\sqrt{20^2 + 21^2} = \\sqrt{841} = 29$.",
)

R9_17 = Ex(
    "R9.17", "🔨", 1, 20, "Produit scalaire et angle · `dot`, `angle_between`",
    "programmer le produit scalaire et l'angle entre deux vecteurs, sans être piégé par les arrondis des flottants.",
    "fiche §5 et §7 ; Ex R9.16", tracks="C, E", mymath="plane.py",
    body="""Écris `dot(u, v)` puis `angle_between(u, v)` (fiche §5 et §7). `dot` renvoie la somme des produits des coordonnées (un entier si les coordonnées sont entières) et lève une `ValueError` si les dimensions diffèrent. `angle_between` renvoie l'angle en radians, dans $[0 ; \\pi]$, avec `math.acos` ; elle lève une `ValueError` si l'un des vecteurs est nul. Réutilise `dot` et `norm`.

⚠️ Avec des flottants, le cosinus calculé peut valoir 1,0000000000000002 pour deux vecteurs de même direction : `math.acos` lève alors une erreur. Ramène le quotient dans $[-1 ; 1]$ avant de l'appeler (`max(-1.0, min(1.0, cosine))`).

La vérification calcule :
- a) `dot((2, -3, 1), (4, 1, -5))` ;
- b) le type de `dot((1, 2), (3, 4))`, en texte ;
- c) le nom de l'erreur levée par `dot((1, 2), (1, 2, 3))` ;
- d) `angle_between((1, 0), (-1, 1))` (4 décimales) ;
- e) le nom de l'erreur levée par `angle_between((1, 5), (2, 10))` (`"aucune"` si elle n'en lève pas), puis f) sa valeur ;
- g) le nom de l'erreur levée par `angle_between((0, 0), (1, 2))` ;
- h) l'angle entre $(-2 ; 1)$ et $(1 ; 3)$, en degrés (`math.degrees`, 4 décimales).

Puis, dans ta copie : pourquoi le cosinus de e) dépasse-t-il 1, alors que les deux vecteurs ont exactement la même direction ?""",
    todo=LOAD_LEARNER,
    check='''with checked("R9.17a"):
    wbm.check("R9.17a", mymath.plane.dot((2, -3, 1), (4, 1, -5)), computed=True)
with checked("R9.17b"):
    wbm.check("R9.17b", type(mymath.plane.dot((1, 2), (3, 4))).__name__, computed=True)
with checked("R9.17c"):
    wbm.check("R9.17c", raised(mymath.plane.dot, (1, 2), (1, 2, 3)), computed=True)
with checked("R9.17d"):
    wbm.check("R9.17d", mymath.plane.angle_between((1, 0), (-1, 1)), computed=True)
with checked("R9.17e"):
    wbm.check("R9.17e", raised(mymath.plane.angle_between, (1, 5), (2, 10)), computed=True)
with checked("R9.17f"):
    wbm.check("R9.17f", mymath.plane.angle_between((1, 5), (2, 10)), computed=True)
with checked("R9.17g"):
    wbm.check("R9.17g", raised(mymath.plane.angle_between, (0, 0), (1, 2)), computed=True)
with checked("R9.17h"):
    wbm.check("R9.17h", math.degrees(mymath.plane.angle_between((-2, 1), (1, 3))), computed=True)''',
    solution=LOAD_REF + '''
dot, angle_between = mymath.plane.dot, mymath.plane.angle_between
print("a)", dot((2, -3, 1), (4, 1, -5)), " b)", type(dot((1, 2), (3, 4))).__name__,
      " c)", raised(dot, (1, 2), (1, 2, 3)))
print("d)", angle_between((1, 0), (-1, 1)), " e)", raised(angle_between, (1, 5), (2, 10)),
      " f)", angle_between((1, 5), (2, 10)), " g)", raised(angle_between, (0, 0), (1, 2)))
print("h)", math.degrees(angle_between((-2, 1), (1, 3))))
print("the rounded cosine of e):", dot((1, 5), (2, 10)) / (mymath.plane.norm((1, 5)) * mymath.plane.norm((2, 10))))''',
    record=f'''wbm.record("R9.17a", 0, mistakes={{"multiplie les coordonnées de même rang, puis additionne les produits": 8}})
wbm.record("R9.17b", "int",
           mistakes={{"avec des entiers, la somme des produits reste un entier : pas de float(...) ni de /": "float"}})
wbm.record("R9.17c", "ValueError",
           mistakes={{"des dimensions différentes : lève une ValueError (zip s'arrêterait sans rien dire)": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("R9.17d", 3 * math.pi / 4, decimals=4,
           mistakes={{"angle_between rend des radians, pas des degrés": 135,
                     "divise le produit scalaire par le produit des normes avant math.acos": math.pi}})
wbm.record("R9.17e", "aucune",
           mistakes={{"ramène le cosinus dans [-1, 1] avant math.acos : max(-1.0, min(1.0, cosine))": "ValueError",
                     "aucune erreur ici : les deux vecteurs sont non nuls, le cosinus est ramené dans [-1, 1]":
                         {errors_source()}}})
wbm.record("R9.17f", 0.0, decimals=4)
wbm.record("R9.17g", "ValueError",
           mistakes={{"un vecteur nul : lève une ValueError avant de diviser par sa norme": {{"ZeroDivisionError",
                                                                                        "aucune"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("R9.17h", math.degrees(math.acos(1 / math.sqrt(50))), decimals=4)''',
    after=tests_cells("test_dot_ or test_angle_between_ or test_plane_uses"),
    note="Le cosinus de e) se calcule avec deux racines carrées arrondies : $\\sqrt{26} \\times \\sqrt{104}$ ne "
         "redonne pas exactement 52 en flottants, et le quotient tombe à 1,0000000000000002. L'erreur est minuscule, "
         "mais `math.acos` refuse tout ce qui sort de $[-1 ; 1]$ : on ramène donc le quotient dans l'intervalle.",
)

R9_18 = Ex(
    "R9.18", "🔨", 1, 15, "La droite qui passe par deux points, et les radians · `line_through`, `deg_to_rad`",
    "programmer une équation cartésienne de la droite qui passe par deux points, verticales comprises, et la "
    "conversion en radians.", "fiche §4 et §6", tracks="C", mymath="plane.py",
    body="""Écris `line_through(A, B)` puis `deg_to_rad(degrees)` (fiche §4 et §6). `line_through` renvoie un triplet $(a, b, c)$ tel que $ax + by + c = 0$ pour les deux points, avec $(a, b) \\ne (0, 0)$, des entiers quand les coordonnées sont entières, et lève une `ValueError` si les deux points sont égaux. Méthode : un vecteur directeur $(d_x ; d_y)$, tourné d'un quart de tour, donne un vecteur normal $(-d_y ; d_x)$, soit $(a ; b)$ ; puis $c$ s'obtient en écrivant que $A$ est sur la droite.

Une droite a une infinité d'équations : la vérification les compare toutes sous une même forme, avec `normalized` (de la cellule des outils), qui divise $a$, $b$ et $c$ par le premier nombre non nul parmi $a$ et $b$.

La vérification calcule :
- a) `normalized(line_through((1, -1), (3, 5)))` ;
- b) `normalized(line_through((4, 1), (4, -7)))`, une droite verticale ;
- c) le nom de l'erreur levée par `line_through((2, 3), (2, 3))` ;
- d) le type du coefficient $a$ de `line_through((0, 1), (1, 3))`, en texte ;
- e) la liste `[deg_to_rad(d) for d in (180, 90, 45, -30)]` (4 décimales).

Puis, dans ta copie : pourquoi la méthode du quart de tour marche-t-elle aussi pour une droite verticale, alors que la pente n'existe pas ?""",
    todo=LOAD_LEARNER,
    check='''with checked("R9.18a"):
    wbm.check("R9.18a", normalized(mymath.plane.line_through((1, -1), (3, 5))), computed=True)
with checked("R9.18b"):
    wbm.check("R9.18b", normalized(mymath.plane.line_through((4, 1), (4, -7))), computed=True)
with checked("R9.18c"):
    wbm.check("R9.18c", raised(mymath.plane.line_through, (2, 3), (2, 3)), computed=True)
with checked("R9.18d"):
    wbm.check("R9.18d", type(mymath.plane.line_through((0, 1), (1, 3))[0]).__name__, computed=True)
with checked("R9.18e"):
    wbm.check("R9.18e", [mymath.plane.deg_to_rad(d) for d in (180, 90, 45, -30)], computed=True)''',
    solution=LOAD_REF + '''
line_through, deg_to_rad = mymath.plane.line_through, mymath.plane.deg_to_rad
print("a)", line_through((1, -1), (3, 5)), normalized(line_through((1, -1), (3, 5))))
print("b)", line_through((4, 1), (4, -7)), normalized(line_through((4, 1), (4, -7))))
print("c)", raised(line_through, (2, 3), (2, 3)), " d)", type(line_through((0, 1), (1, 3))[0]).__name__)
print("e)", [deg_to_rad(d) for d in (180, 90, 45, -30)])''',
    record=f'''wbm.record("R9.18a", [1.0, round(-1 / 3, 4), round(-4 / 3, 4)], decimals=4,
           mistakes={{"(a ; b) est un vecteur normal, pas un vecteur directeur : tourne (dx ; dy) d'un quart de tour":
                         [1.0, 3.0, 2.0]}})
wbm.record("R9.18b", [1.0, 0.0, -4.0], decimals=4)
wbm.record("R9.18c", "ValueError",
           mistakes={{"deux points égaux ne définissent pas une droite : lève une ValueError": {{"aucune",
                                                                                             "ZeroDivisionError"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("R9.18d", "int",
           mistakes={{"avec des coordonnées entières, pas de division : les coefficients restent entiers": "float"}})
wbm.record("R9.18e", [math.pi, math.pi / 2, math.pi / 4, -math.pi / 6], decimals=4,
           mistakes={{"de degrés en radians, on multiplie par π/180 (180° donnent π)":
                         [10313.2403, 5156.6202, 2578.3101, -1718.8734]}})''',
    after=tests_cells("test_line_through_ or test_deg_to_rad_ or test_plane_uses"),
    note="Pour a), le vecteur directeur $(2 ; 6)$ donne le vecteur normal $(-6 ; 2)$, puis $c = -(-6 \\times 1 + 2 "
         "\\times (-1)) = 8$ : l'équation $-6x + 2y + 8 = 0$, qui devient $x - \\frac{1}{3}y - \\frac{4}{3} = 0$ "
         "une fois normalisée. Le quart de tour ne divise jamais : pour deux points de même abscisse, $(0 ; d_y)$ "
         "donne $(-d_y ; 0)$, une équation sans $y$, celle d'une droite verticale.",
)

R9_19 = Ex(
    "R9.19", "📦", 1, 15, "Les mêmes calculs avec NumPy (`np.linalg.norm`, `@`)",
    "refaire avec NumPy les calculs de norme, de produit scalaire, de distance et d'angle.",
    "fiche §3, §5, §7 et §8 ; workbookIA 0A §100.8.1 et §100.8.3", tracks="C, E",
    body="""La cellule fournie définit deux vecteurs de $\\mathbb{R}^4$, sous forme d'arrays de NumPy. Calcule, **avec NumPy** (`np.linalg.norm`, l'opérateur `@`, `np.arccos`, `np.degrees`), sans écrire de boucle :
- a) la norme de `x` ;
- b) le produit scalaire de `x` et `y` ;
- c) la norme L1 de `x` (`ord=1`) ;
- d) la norme L∞ de `x` (`ord=np.inf`) ;
- e) la similarité cosinus de `x` et `y` (4 décimales) ;
- f) la distance entre `x` et `y` (4 décimales) ;
- g) l'angle entre `x` et `y`, en degrés (2 décimales).

Puis vérifie que tes fonctions `norm` et `dot` de `mymath` donnent les mêmes valeurs que NumPy sur `x` et `y` (passe-leur `tuple(x)`). Dans ta copie : l'angle de g) est-il aigu ou obtus ? Comment le savoir dès b) ?""",
    given='''x = np.array([2.0, -1.0, 4.0, 2.0])
y = np.array([1.0, 3.0, -1.0, 0.5])''',
    todo='''answer_R9_19a = ...  # a) np.linalg.norm(...)
answer_R9_19b = ...  # b) with @
answer_R9_19c = ...  # c) ord=1
answer_R9_19d = ...  # d) ord=np.inf
answer_R9_19e = ...  # e) the cosine similarity
answer_R9_19f = ...  # f) the distance
answer_R9_19g = ...  # g) the angle in degrees''',
    check='''for letter, answer in zip("abcdefg", [answer_R9_19a, answer_R9_19b, answer_R9_19c, answer_R9_19d,
                                       answer_R9_19e, answer_R9_19f, answer_R9_19g]):
    wbm.check(f"R9.19{letter}", answer)''',
    solution='''answer_R9_19a = np.linalg.norm(x)
answer_R9_19b = x @ y
answer_R9_19c = np.linalg.norm(x, ord=1)
answer_R9_19d = np.linalg.norm(x, ord=np.inf)
answer_R9_19e = x @ y / (np.linalg.norm(x) * np.linalg.norm(y))
answer_R9_19f = np.linalg.norm(x - y)
answer_R9_19g = np.degrees(np.arccos(answer_R9_19e))
print(answer_R9_19a, answer_R9_19b, answer_R9_19c, answer_R9_19d)
print(round(float(answer_R9_19e), 4), round(float(answer_R9_19f), 4), round(float(answer_R9_19g), 2))''',
    record='''wbm.record("R9.19a", 5.0, decimals=4, mistakes={"np.linalg.norm calcule la norme L2 par défaut": 9.0})
wbm.record("R9.19b", -4.0, decimals=4,
           mistakes={"x @ y est le produit scalaire, un nombre ; x * y multiplie case par case": 4.0})
wbm.record("R9.19c", 9.0, decimals=4, mistakes={"ord=1 donne la norme L1 : la somme des valeurs absolues": 7.0})
wbm.record("R9.19d", 4.0, decimals=4, mistakes={"ord=np.inf donne la plus grande valeur absolue": -1.0})
wbm.record("R9.19e", -4 / (5 * math.sqrt(11.25)), decimals=4,
           mistakes={"divise le produit scalaire par le produit des deux normes": -4.0})
wbm.record("R9.19f", math.sqrt(44.25), decimals=4,
           mistakes={"la distance est la norme de la différence x − y": math.sqrt(25) - math.sqrt(11.25)})
wbm.record("R9.19g", math.degrees(math.acos(-4 / (5 * math.sqrt(11.25)))), decimals=2,
           mistakes={"np.arccos rend des radians : np.degrees les convertit": 1.81})''',
    after=[("md", "**Comparer avec ta librairie** (la cellule s'exécute aussi tant que `mymath` n'est pas écrite)."),
           ("code", '''with checked("R9.19 mymath"):
    same_norm = math.isclose(mymath.plane.norm(tuple(x)), float(np.linalg.norm(x)))
    same_dot = math.isclose(mymath.plane.dot(tuple(x), tuple(y)), float(x @ y))
    verdict("R9.19 mymath", same_norm and same_dot, "norm et dot donnent les mêmes valeurs que NumPy.",
            "norm ou dot ne donne pas la même valeur que NumPy : relance leurs tests (R9.16, R9.17).")''')],
    note="Le produit scalaire de b) est négatif : l'angle est obtus, avant même de calculer g) (environ 103,8°). "
         "NumPy calcule ces sommes en C, sur tout l'array d'un coup : c'est le calcul vectorisé de workbookIA 0A.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, a figure, an experiment (R9.20 to R9.22)
# ---------------------------------------------------------------------------
R9_20_EXPERIMENT = '''u = np.array([3, -1, 4, 1, -5])


def cosine(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


print("cos(u, 2u)   =", round(cosine(u, 2 * u), 6))
print("cos(u, -u)   =", round(cosine(u, -u), 6))
print("‖-3u‖ / ‖u‖ =", round(float(np.linalg.norm(-3 * u) / np.linalg.norm(u)), 6))'''

R9_20 = Ex(
    "R9.20", "🔮", 1, 10, "Prédire le cosinus entre un vecteur et son double, puis son opposé",
    "prévoir l'effet d'une multiplication par un nombre sur la similarité cosinus et sur la norme.",
    "fiche §3 et §7", tracks="C, E", hypothesis=True,
    body="""Le vecteur $\\mathbf{u} = (3, -1, 4, 1, -5)$ a cinq coordonnées. **Avant d'exécuter quoi que ce soit**, prédis :
- a) la similarité cosinus de $\\mathbf{u}$ et $2\\mathbf{u}$ : (1) 0,5 ; (2) 1 ; (3) 2 ;
- b) la similarité cosinus de $\\mathbf{u}$ et $-\\mathbf{u}$ : (1) $-1$ ; (2) 0 ; (3) 1 ;
- c) la norme de $-3\\mathbf{u}$, comparée à celle de $\\mathbf{u}$ : (1) $-3$ fois plus grande ; (2) 3 fois plus grande ; (3) 9 fois plus grande.

Réponds par le numéro du choix : 1, 2 ou 3. Écris tes trois prédictions, vérifie-les, puis lance l'expérience, qui calcule les trois valeurs avec NumPy.""",
    todo='''prediction_R9_20a = ...  # a) 1, 2 or 3, written BEFORE running the experiment below
prediction_R9_20b = ...  # b) 1, 2 or 3
prediction_R9_20c = ...  # c) 1, 2 or 3''',
    check='''for letter, prediction in zip("abc", [prediction_R9_20a, prediction_R9_20b, prediction_R9_20c]):
    wbm.check(f"R9.20{letter}", prediction)''',
    record='''wbm.record("R9.20a", 2, prediction=True, choices=[1, 2, 3])
wbm.record("R9.20b", 1, prediction=True, choices=[1, 2, 3])
wbm.record("R9.20c", 2, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes trois prédictions écrites."),
        ("todo", guarded(R9_20_EXPERIMENT, ["prediction_R9_20a", "prediction_R9_20b", "prediction_R9_20c"],
                         "⏳ Écris d'abord tes trois prédictions, puis exécute à nouveau.")),
        ("solution", R9_20_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : explique les trois résultats avec les formules "
               "$\\lVert k\\mathbf{u} \\rVert = \\lvert k \\rvert\\,\\lVert \\mathbf{u} \\rVert$ et "
               "$(k\\mathbf{u}) \\cdot \\mathbf{u} = k\\,(\\mathbf{u} \\cdot \\mathbf{u})$. Que vaudrait la similarité "
               "cosinus de $\\mathbf{u}$ et $k\\mathbf{u}$ pour un nombre $k$ négatif quelconque ?"),
    ],
    note="Multiplier un vecteur par $k > 0$ ne change pas sa direction : la similarité cosinus reste 1. Par $k < 0$, "
         "la direction s'inverse : elle vaut $-1$. La norme, elle, est multipliée par $\\lvert k \\rvert$ : 3 fois, "
         "jamais $-3$ fois. Sans l'arrondi de l'affichage, NumPy donne parfois 1,0000000000000002 pour a) : un cosinus "
         "calculé en flottants peut sortir très légèrement de $[-1 ; 1]$ (R9.17).",
)

R9_21_CHECK = '''with checked("R9.21 vérifications"):
    problems = []
    for u, v, angle in [((2, -1), (-1, 3), "135.0"), ((4, 0), (1, 3), "71.6")]:
        fig, ax = plt.subplots(figsize=(5, 5))
        try:
            created = drawn(draw_vectors, ax, u, v)
        finally:
            plt.close(fig)                                 # only the checks below are shown here
        if created:
            problems.append("ta fonction ouvre sa propre figure : dessine dans l'axe reçu (ax.quiver, …)")
            break
        arrows = set()
        for q in ax.collections:
            if hasattr(q, "U") and hasattr(q, "V"):
                for a, b in zip(np.ravel(q.U), np.ravel(q.V)):
                    arrows.add((round(float(a), 6), round(float(b), 6)))
        wanted = {tuple(float(c) for c in u), tuple(float(c) for c in v),
                  tuple(float(a + b) for a, b in zip(u, v))}
        if not wanted <= arrows:
            problems.append("trois flèches avec ax.quiver, parties de l'origine : u, v et u + v")
        if ax.get_aspect() not in (1, 1.0, "equal"):
            problems.append("la même unité sur les deux axes : ax.set_aspect(\\"equal\\")")
        title = ax.get_title().replace(",", ".")
        if angle not in title:
            problems.append("l'angle entre u et v dans le titre, en degrés, avec 1 décimale (calculé dans la "
                            "fonction)")
        if problems:
            break
    if problems:
        print("❌ Ex R9.21 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex R9.21 : les trois flèches, la même unité sur les deux axes et l'angle dans le titre.")'''

R9_21 = Ex(
    "R9.21", "🎨", 2, 20, "Dessiner des vecteurs, leur somme et un angle",
    "dessiner deux vecteurs, leur somme et la valeur de leur angle, dans des axes de même unité.",
    "fiche §2 et §7 ; R0 (matplotlib)", tracks="C, E",
    body="""Complète `draw_vectors(ax, u, v)`, qui dessine dans l'axe `ax` qu'elle reçoit :
- trois flèches parties de l'origine, $\\vec{u}$, $\\vec{v}$ et $\\vec{u} + \\vec{v}$, avec `ax.quiver(xs, ys, us, vs, angles="xy", scale_units="xy", scale=1)` : `xs` et `ys` sont les points de départ (ici des 0), `us` et `vs` les coordonnées des vecteurs, et les trois derniers réglages font que chaque flèche a exactement la longueur de son vecteur ;
- en pointillés, les deux autres côtés du parallélogramme (facultatif) ;
- la même unité sur les deux axes (`ax.set_aspect("equal")`), des limites qui laissent voir les trois flèches, et une grille ;
- un titre qui donne l'angle entre $\\vec{u}$ et $\\vec{v}$, en degrés, avec 1 décimale, **calculé dans la fonction** (par exemple `f"angle = {angle:.1f}°"`).

La cellule suivante dessine $\\vec{u} = (2 ; -1)$ et $\\vec{v} = (-1 ; 3)$, les vecteurs de la fiche ; une autre la vérifie, sur ces vecteurs et sur une autre paire.

Dans ta copie : sans la ligne `ax.set_aspect("equal")`, l'angle **dessiné** a-t-il encore l'air de valoir 135° ? Pourquoi ?""",
    todo='''def draw_vectors(ax, u, v):
    """Draw u, v and u + v from the origin in ax (ax.quiver), with equal axes and the angle in the title."""
    raise NotImplementedError("ax.quiver pour les trois flèches, ax.set_aspect, puis le titre avec l'angle")''',
    check='''with checked("R9.21 figure"):
    fig, ax = plt.subplots(figsize=(5, 5))
    try:
        created = drawn(draw_vectors, ax, (2, -1), (-1, 3))
    except BaseException:
        plt.close(fig)                                     # no empty figure while the function is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex R9.21 : ta fonction ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans l'axe "
              "qu'elle reçoit.")
    else:
        plt.show()''',
    solution='''def draw_vectors(ax, u, v):
    """Draw u, v and u + v from the origin in ax (ax.quiver), with equal axes and the angle in the title."""
    s = (u[0] + v[0], u[1] + v[1])
    ax.quiver([0, 0, 0], [0, 0, 0], [u[0], v[0], s[0]], [u[1], v[1], s[1]], color=["C0", "C1", "C2"],
              angles="xy", scale_units="xy", scale=1)
    ax.plot([u[0], s[0]], [u[1], s[1]], "C1--", linewidth=1)
    ax.plot([v[0], s[0]], [v[1], s[1]], "C0--", linewidth=1)
    xs, ys = [0, u[0], v[0], s[0]], [0, u[1], v[1], s[1]]
    ax.set_xlim(min(xs) - 1, max(xs) + 1)
    ax.set_ylim(min(ys) - 1, max(ys) + 1)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    dot = u[0] * v[0] + u[1] * v[1]
    cosine = dot / (math.hypot(*u) * math.hypot(*v))
    angle = math.degrees(math.acos(max(-1.0, min(1.0, cosine))))
    ax.set_title(f"u, v et u + v ; angle = {angle:.1f}°")


fig, ax = plt.subplots(figsize=(5, 5))
draw_vectors(ax, (2, -1), (-1, 3))
plt.show()''',
    after=[("md", "**Vérifications automatiques** (la figure elle-même se juge à l'œil)."), ("code", R9_21_CHECK)],
    note="Sans `ax.set_aspect(\"equal\")`, matplotlib étire les axes pour remplir la figure : une unité horizontale "
         "n'a plus la même longueur qu'une unité verticale, et les angles dessinés sont faux (un angle droit n'a plus "
         "l'air droit). Le calcul, lui, ne change pas : l'angle vaut toujours 135°.",
)

R9_22_GIVEN = '''degrees = np.arange(360) + 0.5          # 0.5°, 1.5°, ..., 359.5°: no angle where cos = sin exactly
whole = np.arange(360)                   # 0°, 1°, ..., 359°'''

R9_22 = Ex(
    "R9.22", "🔬", 2, 20, "Le cercle trigonométrique : cos et sin d'un angle qui tourne",
    "explorer numériquement le cosinus et le sinus sur un tour complet : la relation cos² + sin² = 1, leurs "
    "comparaisons, leur maximum et la dérivée du sinus.", "fiche §6 ; workbookIA 0A §100.8.3 (calcul vectorisé)",
    tracks="C",
    body="""La cellule fournie définit `degrees`, 360 angles en degrés (0,5°, 1,5°, …, 359,5°), et `whole`, les angles entiers de 0° à 359°. Avec NumPy (`np.radians`, `np.cos`, `np.sin`, `np.max`, `np.abs`, `np.sum`, `np.argmax`) :
- a) `close_to_1` : vrai si, pour tous les angles de `degrees`, $\\lvert \\cos^2\\theta + \\sin^2\\theta - 1 \\rvert$ reste inférieur à $10^{-12}$ (un booléen) ;
- b) `count_cos_above` : le nombre d'angles de `degrees` pour lesquels $\\cos\\theta > \\sin\\theta$ ;
- c) `argmax_sin` : l'angle de `whole`, en degrés, pour lequel $\\sin\\theta$ est le plus grand ;
- d) `slope` : le taux d'accroissement $\\frac{\\sin(1 + h) - \\sin 1}{h}$, avec $h = 10^{-5}$ (4 décimales), à comparer avec $\\cos 1$.

Trace aussi, sur un même graphique, $\\cos$ et $\\sin$ entre 0 et $4\\pi$, avec une légende et l'abscisse en radians.

Dans ta copie : sur quels intervalles d'angles a-t-on $\\cos\\theta > \\sin\\theta$ ? Dessine-les sur le cercle. Que montre d) sur la dérivée de $\\sin$ ?""",
    given=R9_22_GIVEN,
    todo='''close_to_1 = ...       # a) a boolean
count_cos_above = ...  # b) an integer
argmax_sin = ...       # c) an angle in degrees
slope = ...            # d) a number''',
    check='''wbm.check("R9.22a", close_to_1)
wbm.check("R9.22b", count_cos_above)
wbm.check("R9.22c", argmax_sin)
wbm.check("R9.22d", slope)''',
    solution='''theta = np.radians(degrees)
close_to_1 = bool(np.max(np.abs(np.cos(theta) ** 2 + np.sin(theta) ** 2 - 1)) < 1e-12)
count_cos_above = int(np.sum(np.cos(theta) > np.sin(theta)))
argmax_sin = int(whole[np.argmax(np.sin(np.radians(whole)))])
h = 1e-5
slope = (math.sin(1 + h) - math.sin(1)) / h
print("a)", close_to_1, " b)", count_cos_above, " c)", argmax_sin, " d)", round(slope, 4), " cos 1 =", round(math.cos(1), 4))

t = np.linspace(0, 4 * np.pi, 400)
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(t, np.cos(t), label="cos")
ax.plot(t, np.sin(t), label="sin")
ax.axhline(0, color="0.5", linewidth=0.8)
ax.set_xlabel("angle (radians)")
ax.legend()
ax.set_title("cos et sin sur deux tours")
plt.show()''',
    record='''wbm.record("R9.22a", True, mistakes={"compare la plus grande valeur de |cos² + sin² − 1| à 1e-12": False})
wbm.record("R9.22b", 180, mistakes={"compare cos θ et sin θ angle par angle, puis compte les True": {360, 0}})
wbm.record("R9.22c", 90, mistakes={"np.sin attend des radians : convertis les degrés avec np.radians": 322})
wbm.record("R9.22d", (math.sin(1 + 1e-5) - math.sin(1)) / 1e-5, decimals=4,
           mistakes={"le taux d'accroissement se divise par h": math.sin(1 + 1e-5) - math.sin(1)})''',
    note="$\\cos\\theta > \\sin\\theta$ pour $\\theta$ entre $-135°$ et $45°$, soit 180 des 360 angles : les deux "
         "courbes se croisent en 45° et 225°. Le taux d'accroissement de d) vaut environ 0,5403, la valeur de "
         "$\\cos 1$ : la pente de la courbe de $\\sin$ en 1 est $\\cos 1$, comme le dit $\\sin' = \\cos$ (en radians).",
)

# ---------------------------------------------------------------------------
# Notebook exercises: bugs and floats (R9.23, R9.24)
# ---------------------------------------------------------------------------
R9_23_MISTAKES = bug_letters_mistakes(
    "ADE", "BC",
    {"A": "relis chaque appel à une fonction trigonométrique : reçoit-elle bien des radians ?",
     "D": "relis chaque ligne qui annonce une valeur : dans quelle unité la fonction répond-elle ?",
     "E": "relis chaque conversion : 180° doivent donner π"})

R9_23 = Ex(
    "R9.23", "🐛", 1, 15, "Chasse à l'erreur : radians et degrés",
    "repérer les confusions entre degrés et radians dans du code, puis calculer les bonnes valeurs.",
    "fiche §6", tracks="C, E",
    body="""Voici cinq lignes de code, chacune avec ce qu'en attend son auteur. Trois sont fausses. **Sans exécuter d'abord**, trouve-les.

- **(A)** « Le sinus de 45° : `math.sin(45)`. »
- **(B)** « Le sinus de 45° : `math.sin(math.radians(45))`. »
- **(C)** « Un angle `rad` en radians, converti en degrés : `rad * 180 / math.pi`. »
- **(D)** « L'angle dont le cosinus vaut 0,5 : `math.acos(0.5)` vaut 60. »
- **(E)** « 30° en radians : `30 * 180 / math.pi`. »

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) les **bonnes** valeurs, dans l'ordre alphabétique des trois lignes fausses : celle que voulait l'auteur de (A), la vraie valeur de `math.acos(0.5)` et 30° en radians (une liste, 4 décimales).

Tu peux exécuter les lignes après avoir répondu, pour vérifier. Dans ta copie : pour chaque ligne fausse, quelle règle a été oubliée ?""",
    todo='''answer_R9_23a = ...  # a) letters, as text
answer_R9_23b = ...  # b) a list of 3 values (4 decimals)''',
    check='''wbm.check("R9.23a", answer_R9_23a)
wbm.check("R9.23b", answer_R9_23b)''',
    solution='''answer_R9_23a = "ADE"
answer_R9_23b = [math.sin(math.radians(45)), math.acos(0.5), math.radians(30)]
print(answer_R9_23a, [round(v, 4) for v in answer_R9_23b])
print("the wrong lines give:", math.sin(45), math.acos(0.5), 30 * 180 / math.pi)''',
    record=f'''wbm.record("R9.23a", "ADE",
           mistakes={R9_23_MISTAKES})
wbm.record("R9.23b", [math.sqrt(2) / 2, math.pi / 3, math.pi / 6], decimals=4,
           mistakes={{"ce sont les valeurs des lignes fausses : calcule les bonnes": [math.sin(45), 60,
                                                                                   30 * 180 / math.pi],
                     "math.acos rend des radians : sa vraie valeur n'est pas 60": [math.sqrt(2) / 2, 60, math.pi / 6]}})''',
    note="(A) `math.sin(45)` calcule le sinus de 45 radians, environ 0,851, au lieu de $\\frac{\\sqrt{2}}{2} \\approx "
         "0{,}7071$. (D) `math.acos` rend des radians : $\\frac{\\pi}{3} \\approx 1{,}0472$, qui vaut bien 60°. (E) "
         "La conversion est à l'envers : de degrés en radians, on multiplie par $\\frac{\\pi}{180}$, ce qui donne "
         "$\\frac{\\pi}{6} \\approx 0{,}5236$. (B) et (C) sont justes.",
)

R9_24_GIVEN = '''u = (0.1, 0.7)
v = (2.1, -0.3)                          # 0.1 × 2.1 − 0.7 × 0.3 = 0.21 − 0.21 = 0: orthogonal on paper
print("u·v =", u[0] * v[0] + u[1] * v[1])'''

R9_24_CHECK = '''with checked("R9.24 vérifications"):
    problems = []
    if is_orthogonal(u, v) is not True:
        problems.append("is_orthogonal(u, v) doit être True : sur papier, u·v vaut 0")
    if is_orthogonal((1, 0), (1e-6, 1)) is not False:
        problems.append("is_orthogonal((1, 0), (1e-6, 1)) doit être False : 1e-6 dépasse la tolérance")
    if is_orthogonal((3, 4), (-4, 3)) is not True:
        problems.append("is_orthogonal((3, 4), (-4, 3)) doit être True")
    if is_orthogonal((2, 1), (1, 1), tol=10) is not True:
        problems.append("le paramètre tol doit être utilisé : avec tol=10, (2 ; 1) et (1 ; 1) passent")
    if problems:
        print("❌ Ex R9.24 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex R9.24 : is_orthogonal tolère les arrondis des flottants, et seulement eux.")'''

R9_24 = Ex(
    "R9.24", "🛠️", 1, 10, "Comparer deux flottants : `np.isclose`",
    "tester l'orthogonalité de vecteurs à coordonnées décimales sans être trompé par les arrondis.",
    "fiche §5 ; R0 (les flottants)", tracks="C",
    body="""Sur papier, $\\vec{u} = (0{,}1 ; 0{,}7)$ et $\\vec{v} = (2{,}1 ; -0{,}3)$ sont orthogonaux : $0{,}21 - 0{,}21 = 0$. La cellule fournie calcule leur produit scalaire en flottants : il ne vaut pas exactement 0 (R0 : les flottants forment une grille). Un test `u·v == 0` se tromperait donc.

1. Écris `is_orthogonal(u, v, tol=1e-9)`, qui renvoie `True` quand le produit scalaire est nul **à `tol` près**, en valeur absolue. Deux outils font cette comparaison : `math.isclose(x, 0, abs_tol=tol)` et `np.isclose(x, 0, atol=tol)` (qui renvoie un booléen de NumPy : convertis-le avec `bool(...)`).
2. La cellule de vérification essaie ta fonction sur quatre cas.

Dans ta copie : que renvoie `math.isclose(1e-17, 0)`, sans `abs_tol` ? Pourquoi une tolérance **relative** (« à 1e-9 près de la valeur ») ne peut-elle pas servir pour comparer à 0 ?""",
    given=R9_24_GIVEN,
    todo='''def is_orthogonal(u, v, tol=1e-9):
    """True when u·v is 0 up to tol (in absolute value): a float dot product is rarely exactly 0."""
    raise NotImplementedError("le produit scalaire, puis math.isclose(..., 0, abs_tol=tol)")''',
    solution='''def is_orthogonal(u, v, tol=1e-9):
    """True when u·v is 0 up to tol (in absolute value): a float dot product is rarely exactly 0."""
    dot = sum(a * b for a, b in zip(u, v))
    return math.isclose(dot, 0, abs_tol=tol)


print(is_orthogonal(u, v), u[0] * v[0] + u[1] * v[1] == 0, math.isclose(1e-17, 0), bool(np.isclose(1e-17, 0)))''',
    after=[("code", R9_24_CHECK)],
    note="`math.isclose(1e-17, 0)` vaut `False` : sa tolérance par défaut est relative (`rel_tol=1e-9`, « à un "
         "milliardième de la plus grande des deux valeurs près »), et un milliardième de 0 vaut 0. Pour comparer à 0, "
         "il faut une tolérance absolue (`abs_tol`) ; `np.isclose` en a une par défaut (`atol=1e-8`).",
)

PART_A = Part("A", "Ta librairie : vecteurs, norme, produit scalaire, angle, droites, radians",
              "Fiche §2 à §8. Les six fonctions de `mymath/plane.py`, puis les mêmes calculs avec NumPy.",
              given=TOOLS, exercises=[R9_16, R9_17, R9_18, R9_19])

PART_B = Part("B", "Une prédiction, une figure et une expérience",
              "Fiche §2, §3, §6 et §7. La similarité cosinus d'un vecteur et de ses multiples, deux vecteurs et leur "
              "somme en image, puis le cosinus et le sinus sur un tour complet.",
              exercises=[R9_20, R9_21, R9_22])

PART_C = Part("C", "Radians, degrés et flottants",
              "Fiche §5 et §6. Trois confusions entre degrés et radians à trouver, puis un test d'orthogonalité qui "
              "résiste aux arrondis.",
              exercises=[R9_23, R9_24])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | R9.1 à R9.10, R9.13, R9.14 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# R9 · Géométrie du plan, vecteurs et trigonométrie — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/r9_geometrie_vecteurs/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py R9`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# R9 · Géométrie du plan, vecteurs et trigonométrie — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : distances, vecteurs, normes, droites, produit scalaire, "
               "radians, cosinus et sinus, angles, vecteurs de ℝ³ et ℝ⁴.\n"
               "- Écrire les six fonctions de `mymath/plane.py` et les tester, puis refaire les calculs avec NumPy.\n"
               "- Prédire l'effet d'un multiple sur la similarité cosinus, dessiner des vecteurs, explorer le cercle "
               "trigonométrique, chasser des confusions entre degrés et radians, comparer des flottants.\n\n"
               "**Rappel express.** $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$ ; $\\overrightarrow{AB} = B - A$ ; "
               "$\\lVert \\vec{u} \\rVert = \\sqrt{x^2 + y^2}$ ; $\\vec{u} \\cdot \\vec{v} = xx' + yy' = "
               "\\lVert \\vec{u} \\rVert\\,\\lVert \\vec{v} \\rVert \\cos\\theta$. $ax + by + c = 0$ : $(-b ; a)$ "
               "directeur, $(a ; b)$ normal. $180° = \\pi$ rad ; `math.cos` attend des radians.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Calcules-tu une distance, un vecteur, une norme et l'équation d'une droite ?\n"
               "2. Sais-tu calculer un produit scalaire, reconnaître des vecteurs orthogonaux et en déduire un "
               "angle ?\n"
               "3. Passes-tu des degrés aux radians, et lis-tu cos et sin sur le cercle trigonométrique ?\n\n"
               "**La suite** : l'examen blanc CP0, le bilan de la remise à niveau. Puis, dans workbookIA, le chapitre "
               "0B.")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter=CHAPTER) if kind == "exercise" else setup_cell(kind))
    cells += objectives_cell()
    cells += paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO,
                         learner_context="from fractions import Fraction   # Fraction(5, 9) is accepted too, as \"5/9\"")
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
