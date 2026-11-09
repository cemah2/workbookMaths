#!/usr/bin/env python
"""Build the two notebooks of chapter M05b from a single source (used by Claude).

    python tools/chapters/build_m05b.py
    python tools/run_all_notebooks.py chapitres/m05b_gradient/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m05b_gradient/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M05b.1 to M05b.10, 🔗 M05b.14, 📈 M05b.16); parts A to C are the notebook
exercises. Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it. The
functions are new: none is a test case of tests/test_m05b_multivar.py, an answer of the paper exercises, or an
example of workbookIA 5 (no Rosenbrock, no x² − y², no xy, no x² + xy (its fiche, at (1, 2), with u = (0.6, 0.8)),
no x² + 3xy (its PyTorch box), no x² + xy + 2y², no x³ − 3x − y³ + 3y, no x⁴ + y⁴ − 4xy, no x³ + y², no bowl
x² + 10y², no learning-rate study, no integer point losing h).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M05b"
FOLDER = "chapitres/m05b_gradient"

F = 'kind="fraction", simplified=True'
XY = 'kind="expr", variables=("x", "y")'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M05b.1", "Les lignes de niveau de trois fonctions", [
        ("a", "an integer", "3",
         '''mistakes={"isole y dans 3x − y + 2 = 5 : attention au signe devant y": -3}'''),
        ("b", "an integer", "3",
         '''mistakes={"isole y dans 3x − y + 2 = c : attention au signe devant y": -3}'''),
        ("c", "an integer", "6",
         '''mistakes={"la ligne de niveau coupe l'axe des x là où y = 0 : résous l'équation en x jusqu'au bout": 36}'''),
        ("d", "an integer", "2",
         '''mistakes={"la ligne de niveau coupe l'axe des y là où x = 0 : résous l'équation en y jusqu'au bout (une '''
         '''racine carrée)": 4, "tu as répondu pour l'autre axe": 6}'''),
        ("e", "an integer", "13",
         '''mistakes={"x est au carré dans f₂": 11}'''),
        ("f", "an integer", "-2",
         '''mistakes={"isole y dans y − x² = −2 : attention au signe": 2}'''),
        ("g", "True or False", "True",
         '''mistakes={"(−2)² est positif": False}'''),
        ("h", "True or False", "False",
         '''mistakes={"x² + 9y² est une somme de carrés : quel est son signe ?": True}'''),
    ]),

    Paper("M05b.2", "Dérivées partielles", [
        ("a", "an expression in x and y, as text", '"12*x**2*y + 7"',
         XY + ''', mistakes={"la dérivée de 7x par rapport à x n'est pas nulle": "12*x**2*y", '''
              '''"−y² ne dépend pas de x : sa dérivée par rapport à x est nulle": "12*x**2*y - 2*y + 7"}'''),
        ("b", "an expression in x and y, as text", '"4*x**3 - 2*y"',
         XY + ''', mistakes={"7x ne dépend pas de y : sa dérivée par rapport à y est nulle": "4*x**3 - 2*y + 7", '''
              '''"x³ est une constante quand on dérive par rapport à y, mais y, lui, se dérive": "4*x**3*y - 2*y"}'''),
        ("c", "an integer", "-17",
         '''mistakes={"remplace y par −2, avec son signe": 31}'''),
        ("d", "an integer", "8",
         '''mistakes={"remplace y par −2, avec son signe": 0}'''),
        ("e", "an integer", "2",
         '''mistakes={"applique la règle de la chaîne : dérive aussi l'exposant 2x − y par rapport à x": 1}'''),
        ("f", "an integer", "-1",
         '''mistakes={"la dérivée de l'exposant 2x − y par rapport à y est négative": 1}'''),
        ("g", "an integer", "6",
         '''mistakes={"z² est positif même si z est négatif": -6}'''),
        ("h", "an integer", "-4",
         '''mistakes={"z³ garde le signe de z": 4}'''),
    ]),

    Paper("M05b.3", "Le gradient en un point et sa norme", [
        ("a", "a list of 2 integers", "[12, 1]",
         '''mistakes={"∂f/∂y contient aussi la dérivée du terme −3y": [12, 4]}'''),
        ("b", "a number (4 decimals)", "145 ** 0.5",
         '''decimals=4, mistakes={"la norme est la racine carrée de la somme des carrés": 145, '''
         '''"la norme n'est pas la somme des composantes": 13}'''),
        ("c", "a list of 2 integers", "[0, -3]", ''),
        ("d", "a list (3 decimals)", "[-3 ** 0.5, 3 ** 0.5]",
         '''decimals=3, mistakes={"un nombre positif a deux racines carrées : garde toutes les solutions": '''
         '''[3 ** 0.5]}'''),
        ("e", "a list (4 decimals)", "[12 / 145 ** 0.5, 1 / 145 ** 0.5]",
         '''decimals=4, mistakes={"divise le gradient par sa norme pour obtenir un vecteur unitaire": [12, 1]}'''),
        ("f", "a number (4 decimals)", "8 ** 0.5",
         '''decimals=4, mistakes={"la norme est la racine carrée de la somme des carrés": 8}'''),
    ]),

    Paper("M05b.4", "La dérivée directionnelle dans plusieurs directions", [
        ("a", "an integer", "10",
         '''mistakes={"dans la direction (1, 0), c'est la dérivée partielle par rapport à x": -2}'''),
        ("b", "an integer", "2",
         '''mistakes={"relis la direction demandée, avec son signe": -2}'''),
        ("c", "a number (2 decimals)", "(70 - 48) / 25",
         '''decimals=2, mistakes={"divise le vecteur (7, 24) par sa norme avant le produit scalaire": 22}'''),
        ("d", "a number (4 decimals)", "8 / 2 ** 0.5",
         '''decimals=4, mistakes={"divise le vecteur (1, 1) par sa norme avant le produit scalaire": 8}'''),
        ("e", "a number (1 decimal)", "(-50 - 24) / 13",
         '''decimals=1, mistakes={"la direction va de P vers Q : c'est Q − P": 74 / 13, '''
         '''"divise le vecteur Q − P par sa norme": -74}'''),
        ("f", "a number (3 decimals)", "104 ** 0.5",
         '''decimals=3, mistakes={"la norme est la racine carrée de la somme des carrés": 104}'''),
        ("g", "a number (2 decimals)", "math.degrees(math.acos(8 / (104 ** 0.5 * 2 ** 0.5)))",
         '''decimals=2, mistakes={"l'angle est demandé en degrés": math.acos(8 / (104 ** 0.5 * 2 ** 0.5))}'''),
    ]),

    Paper("M05b.5", "Monter le plus vite : la direction et la valeur de la plus grande pente", [
        ("a", "a list of 2 integers", "[-5, -3]",
         '''mistakes={"le terme xy compte dans les deux dérivées partielles": [-6, -6]}'''),
        ("b", "a number (3 decimals)", "34 ** 0.5",
         '''decimals=3, mistakes={"la norme est la racine carrée de la somme des carrés": 34, '''
         '''"la norme n'est pas la somme des valeurs absolues des composantes": 8}'''),
        ("c", "a number (2 decimals)", "math.degrees(math.atan2(-3, -5)) % 360",
         '''decimals=2, mistakes={"les deux composantes du gradient sont négatives : dans quel quadrant pointe-t-il ?": '''
         '''{math.degrees(math.atan(3 / 5)), 180 - math.degrees(math.atan(3 / 5))}, '''
         '''"donne l'angle entre 0 et 360 degrés": math.degrees(math.atan2(-3, -5)), '''
         '''"l'angle est demandé en degrés": math.atan2(-3, -5) % (2 * math.pi)}'''),
        ("d", "a number (3 decimals)", "18 / 10 ** 0.5",
         '''decimals=3, mistakes={"divise le vecteur qui va de P vers O par sa norme": 18, '''
         '''"la direction va de P vers O : c'est O − P": -18 / 10 ** 0.5, '''
         '''"on demande le taux en P, la dérivée directionnelle, pas le taux moyen sur le trajet": 9 / 10 ** 0.5}'''),
        ("e", "a number (2 decimals)", "math.degrees(math.acos(18 / 340 ** 0.5))",
         '''decimals=2, mistakes={"l'angle est demandé en degrés": math.acos(18 / 340 ** 0.5)}'''),
        ("f", "an irreducible fraction, as text", "Fraction(-5, 3)",
         F + ''', mistakes={"la tangente à l'isotherme est orthogonale au gradient, pas parallèle": "3/5", '''
             '''"une droite dirigée par (p, q) a pour pente q/p : refais ce quotient avec les signes des composantes": "5/3"}'''),
    ]),

    Paper("M05b.6", "Le plan tangent et l'approximation d'une valeur", [
        ("a", "an integer", "18",
         '''mistakes={"n'oublie pas la racine carrée de y": 36}'''),
        ("b", "an integer", "12",
         '''mistakes={"√y est une constante quand on dérive par rapport à x : elle reste en facteur": 6}'''),
        ("c", "a number (2 decimals)", "9 / 4",
         '''decimals=2, mistakes={"x² est une constante quand on dérive par rapport à y : il reste en facteur": 0.25, '''
         '''"la dérivée de √y est 1/(2√y)": 4.5}'''),
        ("d", "an integer", "-27",
         '''mistakes={"C n'est pas f(3, 4) : développe z = f(3, 4) + A(x − 3) + B(y − 4)": 18}'''),
        ("e", "a number (3 decimals)", "18 + 12 * 0.1 + 2.25 * (-0.1)",
         '''decimals=3, mistakes={"le déplacement en y est négatif : de 4 à 3,9": 18 + 12 * 0.1 + 2.25 * 0.1}'''),
        ("f", "a number (4 decimals)", "3.1 ** 2 * 3.9 ** 0.5", 'decimals=4'),
        ("g", "a number (4 decimals)", "3.1 ** 2 * 3.9 ** 0.5 - (18 + 12 * 0.1 - 2.25 * 0.1)",
         '''decimals=4, mistakes={"l'erreur demandée est la valeur exacte moins l'approximation": '''
         '''-(3.1 ** 2 * 3.9 ** 0.5 - (18 + 12 * 0.1 - 2.25 * 0.1))}'''),
    ]),

    Paper("M05b.7", "Dérivées secondes croisées : le théorème de Schwarz vérifié", [
        ("a", "an expression in x and y, as text", '"6*x**2*y - exp(x*y) - x*y*exp(x*y)"',
         XY + ''', mistakes={"y e^(xy) est un produit de deux fonctions de y : sa dérivée a deux termes": '''
              '''"6*x**2*y - x*y*exp(x*y)", "y e^(xy) est un produit : il manque un des deux termes de sa '''
              '''dérivée": "6*x**2*y - exp(x*y)"}'''),
        ("b", "an expression in x and y, as text", '"2*x**3 - x**2*exp(x*y)"',
         XY + ''', mistakes={"applique la règle de la chaîne à e^(xy), à chacune des deux dérivations": '''
              '''"2*x**3 - x*exp(x*y)", "dérive encore une fois par rapport à y": "2*x**3*y - x*exp(x*y)"}'''),
        ("c", "a number (4 decimals)", "6 * 0.25 - 0.25 * math.exp(0.5)", 'decimals=4'),
        ("d", "a number (4 decimals)", "3 - math.exp(0.5) - 0.5 * math.exp(0.5)", 'decimals=4'),
        ("e", "a number (4 decimals)", "2 - math.exp(0.5)", 'decimals=4'),
        ("f", "a number (3 decimals)", "(FXX_7 + 2 * FXY_7 + FYY_7) / 2",
         '''decimals=3, mistakes={"la direction est donnée par un vecteur unitaire : u = (1, 1)/√2": '''
         '''FXX_7 + 2 * FXY_7 + FYY_7, "le terme croisé compte deux fois : 2 f_xy u₁ u₂": (FXX_7 + FXY_7 + FYY_7) / 2}'''),
        ("g", "a number (3 decimals)", "(FXX_7 - 2 * FXY_7 + FYY_7) / 2",
         '''decimals=3, mistakes={"la direction est donnée par un vecteur unitaire : u = (1, −1)/√2": '''
         '''FXX_7 - 2 * FXY_7 + FYY_7, "le terme croisé compte deux fois : 2 f_xy u₁ u₂": (FXX_7 - FXY_7 + FYY_7) / 2, '''
         '''"avec u = (1, −1)/√2, le produit u₁ u₂ est négatif": (FXX_7 + 2 * FXY_7 + FYY_7) / 2}'''),
    ]),

    Paper("M05b.8", "Les points critiques et leur nature (test du second ordre)", [
        ("a", "an integer", "-24",
         '''mistakes={"calcule f_xx en (−2, 2), avec son signe": 24}'''),
        ("b", "a letter, as text", '"A"',
         '''mistakes={"regarde le signe de f_xx en ce point": "B", '''
         '''"calcule D = f_xx f_yy − f_xy² en ce point : son signe décide": "C", '''
         '''"D n'est pas nul en ce point : le test conclut": "D", "réponds par une lettre : A, B, C ou D": {"minimum", "maximum", "selle", "point selle", "min", "max"}}'''),
        ("c", "a letter, as text", '"C"',
         '''mistakes={"calcule D = f_xx f_yy − f_xy² en (−2, 2) : son signe passe avant celui de f_xx": {"A", "B"}, '''
         '''"D n'est pas nul en ce point : le test conclut": "D", "réponds par une lettre : A, B, C ou D": {"minimum", "maximum", "selle", "point selle", "min", "max"}}'''),
        ("d", "an integer", "-20", ''),
        ("e", "an integer", "4",
         '''mistakes={"le système x² + y² = 5, xy = 2 a aussi des solutions négatives": 2}'''),
        ("f", "an integer", "2",
         '''mistakes={"calcule D = 36(x² − y²) en chacun des points critiques": {0, 1, 3, 4}}'''),
        ("g", "an integer", "28",
         '''mistakes={"c'est la valeur de g en un autre point critique": -28}'''),
        ("h", "a letter, as text", '"D"',
         '''mistakes={"le test ne voit que D et f_xx : calcule D en (0, 0)": {"A", "B", "C"}, "réponds par une lettre : A, B, C ou D": {"minimum", "maximum", "selle", "point selle", "min", "max"}}'''),
    ]),

    Paper("M05b.9", "Pourquoi un petit pas contre le gradient fait baisser f : le calcul au premier ordre", [
        ("a", "a list of 2 integers", "[2, 3]",
         '''mistakes={"∂f/∂y contient aussi la dérivée du terme y²": [2, 1]}'''),
        ("b", "a list (2 decimals)", "[1 - 0.05 * 2, 1 - 0.05 * 3]",
         '''decimals=2, mistakes={"pour descendre, on retire η ∇f(P)": [1 + 0.05 * 2, 1 + 0.05 * 3]}'''),
        ("c", "a number (3 decimals)", "0.9 ** 2 * 0.85 + 0.85 ** 2", 'decimals=3'),
        ("d", "a number (2 decimals)", "2 - 0.05 * 13",
         '''decimals=2, mistakes={"la prévision utilise le carré de la norme du gradient": 2 - 0.05 * 13 ** 0.5}'''),
        ("e", "a number (3 decimals)", "2 - (0.9 ** 2 * 0.85 + 0.85 ** 2)", 'decimals=3'),
        ("f", "a number (3 decimals)", "1.1 ** 2 * 1.15 + 1.15 ** 2",
         '''decimals=3, mistakes={"pour monter, on ajoute η ∇f(P)": 0.9 ** 2 * 0.85 + 0.85 ** 2}'''),
        ("g", "an irreducible fraction, as text", "Fraction(1, 130)",
         F + ''', mistakes={"la baisse voulue est 0,1, pas 1": "1/13"}'''),
    ]),

    Paper("M05b.10", "argmin et argmax sur un segment", [
        ("a", "a number (1 decimal)", "0.4", 'decimals=1'),
        ("b", "a list (1 decimal)", "[1.6, 1.2]", 'decimals=1'),
        ("c", "a number (1 decimal)", "0.8",
         '''decimals=1, mistakes={"c'est la valeur de t ; la question demande la valeur de f": 0.4}'''),
        ("d", "a list of 2 integers", "[4, 0]",
         '''mistakes={"compare les valeurs de f aux deux extrémités du segment": [0, 2]}'''),
        ("e", "an integer", "8",
         '''mistakes={"compare les valeurs de f aux deux extrémités du segment": 4}'''),
        ("f", "a list of 2 integers", "[1, 0]", ''),
        ("g", "an integer", "-1",
         '''mistakes={"refais le calcul de f en ce point, terme par terme": 0}'''),
        ("h", "an integer", "0",
         '''mistakes={"refais le produit scalaire, composante par composante": {1, -1}}'''),
    ]),

    Paper("M05b.14", "La loss d'un neurone à deux poids sur deux exemples : son gradient", [
        ("a", "a number (3 decimals)", "0.625",
         '''decimals=3, mistakes={"n'oublie pas le facteur 1/2 devant la somme": 1.25}'''),
        ("b", "a number (1 decimal)", "-2.5",
         '''decimals=1, mistakes={"le facteur 1/2 de L compense le 2 de la dérivée d'un carré": -5.0}'''),
        ("c", "a number (1 decimal)", "2.0",
         '''decimals=1, mistakes={"le facteur 1/2 de L compense le 2 de la dérivée d'un carré": 4.0}'''),
        ("d", "a list (2 decimals)", "[0.75, 0.3]",
         '''decimals=2, mistakes={"pour descendre, on retire η ∇L": [0.25, 0.7]}'''),
        ("e", "a number (4 decimals)", "0.0625", 'decimals=4'),
        ("f", "a list (4 decimals)", "[5 / 7, 1 / 7]",
         '''decimals=4, mistakes={"l'ordre est [w₁, w₂]": [1 / 7, 5 / 7]}'''),
    ]),

    Paper("M05b.16", "Lire une carte de lignes de niveau : estimer une dérivée partielle", [
        ("a", "an integer", "3", ''),
        ("b", "an integer", "6", ''),
        ("c", "an integer", "3", ''),
        ("d", "an integer", "5", ''),
        ("e", "an integer", "2", ''),
        ("f", "an integer", "6",
         '''mistakes={"recompte les lignes traversées une à une, en suivant le segment de P à Q": {5, 7}}'''),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math
from fractions import Fraction

FXX_7 = 6 * 0.25 - 0.25 * math.exp(0.5)                   # M05b.7 at (1, 0.5)
FXY_7 = 3 - math.exp(0.5) - 0.5 * math.exp(0.5)
FYY_7 = 2 - math.exp(0.5)'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M05b.1 à M05b.10, 🔗 M05b.14, 📈 M05b.16)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"7/9\"` ; une expression en $x$ et $y$ entre "
               "guillemets, `\"3*x**2*y - y\"`, avec `exp(u)` pour $e^u$ et `sqrt(u)` pour $\\sqrt{u}$ ;\n"
               "- une liste `[-1.5, 2.5]` (un gradient, un point, un vecteur), `True` / `False`, ou une lettre entre "
               "guillemets, `\"B\"`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M05b.18 to M05b.21)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

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

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M05b")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/multivar.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "Une fonction de plusieurs variables prend **un seul** argument, un tableau NumPy `p` (`p[0]` est $x$, "
         "`p[1]` est $y$…) : par exemple `lambda p: p[0] ** 2 * p[1]`. NumPy suffit ; SymPy et `numpy.gradient` sont "
         "interdits : les tests comparent tes résultats aux dérivées exactes calculées par SymPy, et un test vérifie "
         "que tu ne te sers d'aucun des deux. Les nombres renvoyés sont des `float` de Python, les vecteurs des tableaux NumPy.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of multivar.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_multivar_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m05b_multivar.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m05b_multivar.py", "{keyword}", impl="ref")')]


M05B_18 = Ex(
    "M05b.18", "🔨", 1, 20, "Une dérivée partielle par différence centrée · `partial_derivative`",
    "programmer une dérivée partielle par une différence centrée, en ne bougeant qu'une coordonnée d'une copie du "
    "point.", "fiche §2 ; M05a §5", tracks="C, E", mymath="multivar.py",
    body=HOWTO + """

Écris `partial_derivative(f, point, i, h=1e-5)` (fiche §2) : $\\frac{f(\\mathbf{p} + h\\,\\mathbf{e}_i) - f(\\mathbf{p} - h\\,\\mathbf{e}_i)}{2h}$, où $\\mathbf{e}_i$ vaut 1 à la place $i$ et 0 ailleurs ; une `ValueError` si `i` n'est pas entre 0 et `len(point) - 1`, ou si $h \\le 0$. Le point de l'appelant ne doit pas changer (relis le commentaire `TODO` de la fonction).

La vérification calcule :
- a) `partial_derivative(lambda p: p[0] ** 2 * np.exp(p[1]), (1.5, 0.0), 0)` (6 décimales) ;
- b) la même fonction, avec `i = 1` (6 décimales) ;
- c) `partial_derivative(lambda p: p[0] * p[1] * p[2], (2.0, -1.0, 4.0), 2)` (6 décimales) ;
- d) le nom de l'erreur levée par `partial_derivative(lambda p: p[0] + p[1] + p[2], (1.0, 2.0, 3.0), 3)` ;
- e) le nom de l'erreur levée par `partial_derivative(lambda p: p[0], (1.0, 2.0), 0, h=0)` ;
- f) `partial_derivative(lambda p: np.log(p[0] + p[1] ** 2), (1.0, 2.0), 1)` (4 décimales) ;
- g) le nom du type de `partial_derivative(lambda p: np.sin(p[0]), np.array([0.5]), 0)`, en texte.

Dans ta copie : calcule a), b), c) et f) à la main avec les règles de la fiche. Pourquoi les vérifications de `i` et de `h` doivent-elles passer **avant** tout calcul (regarde d) et e)) ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M05b.18a"):
    wbm.check("M05b.18a", mymath.multivar.partial_derivative(lambda p: p[0] ** 2 * np.exp(p[1]), (1.5, 0.0), 0),
              computed=True)
with checked("M05b.18b"):
    wbm.check("M05b.18b", mymath.multivar.partial_derivative(lambda p: p[0] ** 2 * np.exp(p[1]), (1.5, 0.0), 1),
              computed=True)
with checked("M05b.18c"):
    wbm.check("M05b.18c", mymath.multivar.partial_derivative(lambda p: p[0] * p[1] * p[2], (2.0, -1.0, 4.0), 2),
              computed=True)
with checked("M05b.18d"):
    wbm.check("M05b.18d", raised(mymath.multivar.partial_derivative, lambda p: p[0] + p[1] + p[2], (1.0, 2.0, 3.0), 3),
              computed=True)
with checked("M05b.18e"):
    wbm.check("M05b.18e", raised(mymath.multivar.partial_derivative, lambda p: p[0], (1.0, 2.0), 0, h=0),
              computed=True)
with checked("M05b.18f"):
    wbm.check("M05b.18f", mymath.multivar.partial_derivative(lambda p: np.log(p[0] + p[1] ** 2), (1.0, 2.0), 1),
              computed=True)
with checked("M05b.18g"):
    wbm.check("M05b.18g", type(mymath.multivar.partial_derivative(lambda p: np.sin(p[0]), np.array([0.5]), 0)).__name__,
              computed=True)''',
    solution=LOAD_REF + '''
partial = mymath.multivar.partial_derivative
print("a)", partial(lambda p: p[0] ** 2 * np.exp(p[1]), (1.5, 0.0), 0),
      " b)", partial(lambda p: p[0] ** 2 * np.exp(p[1]), (1.5, 0.0), 1),
      " c)", partial(lambda p: p[0] * p[1] * p[2], (2.0, -1.0, 4.0), 2))
print("d)", raised(partial, lambda p: p[0] + p[1] + p[2], (1.0, 2.0, 3.0), 3),
      " e)", raised(partial, lambda p: p[0], (1.0, 2.0), 0, h=0),
      " f)", partial(lambda p: np.log(p[0] + p[1] ** 2), (1.0, 2.0), 1),
      " g)", type(partial(lambda p: np.sin(p[0]), np.array([0.5]), 0)).__name__)''',
    record=f'''wbm.record("M05b.18a", 3.0, decimals=6,
           mistakes={{"une différence avant n'est que d'ordre 1 : la docstring demande une différence centrée":
                         3.00001}})
wbm.record("M05b.18b", 2.25, decimals=6,
           mistakes={{"une différence avant n'est que d'ordre 1 : la docstring demande une différence centrée":
                         2.2500113}})
wbm.record("M05b.18c", -2.0, decimals=6,
           mistakes={{"ne bouge que la coordonnée i : les autres restent fixées": 2.0,
                     "les indices de Python commencent à 0 : i = 2 désigne la troisième coordonnée": 8.0}})
wbm.record("M05b.18d", "ValueError",
           mistakes={{"vérifie i avant de t'en servir : un indice hors de 0, …, len(point) − 1 demande une ValueError":
                         "IndexError",
                     "un point de trois coordonnées a les indices 0, 1 et 2 : lève une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "IndexError")}}})
wbm.record("M05b.18e", "ValueError",
           mistakes={{"vérifie h avant de diviser : un pas nul ou négatif demande une ValueError": "ZeroDivisionError",
                     "un pas nul est refusé : lève une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "ZeroDivisionError")}}})
wbm.record("M05b.18f", 0.8, decimals=4,
           mistakes={{"i = 1 désigne la deuxième variable, y : c'est elle qui bouge": 0.2}})
wbm.record("M05b.18g", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy": "float64",
                     "la docstring demande un float de Python, pas un tableau : f renvoie ici un nombre de NumPy, "
                     "à convertir par float(...)": "ndarray"}})''',
    after=tests_cells("test_partial_derivative_"),
    note="a) $\\frac{\\partial}{\\partial x}\\big(x^2 e^y\\big) = 2x\\,e^y = 3$ en $(1{,}5 ;\\ 0)$. b) $x^2 e^y = 2{,}25$. "
         "c) $\\frac{\\partial}{\\partial z}(xyz) = xy = -2$. d) et e) Les vérifications passent **avant** tout calcul : "
         "sans elles, d) lève une `IndexError` et e) une `ZeroDivisionError`. f) $\\frac{\\partial}{\\partial y}\\ln(x + y^2) "
         "= \\frac{2y}{x + y^2} = \\frac{4}{5}$ en $(1, 2)$.",
)

M05B_19 = Ex(
    "M05b.19", "🔨", 2, 20, "Dérivée directionnelle et direction de plus grande pente · "
    "`directional_derivative, steepest_ascent_direction`",
    "programmer la dérivée directionnelle d'une fonction et la direction de plus grande montée, en normalisant les "
    "directions et en refusant les cas sans direction.", "fiche §3 et §4 ; Ex M05b.18", tracks="C, E",
    mymath="multivar.py",
    body="""Écris (fiche §3 et §4) :
- `directional_derivative(f, point, direction, h=1e-5)` : la pente de `f` en `point` dans la direction du vecteur `direction`, **divisé d'abord par sa norme** ; une seule différence centrée le long du vecteur unitaire $\\mathbf{u}$ suffit, $\\frac{f(\\mathbf{p} + h\\mathbf{u}) - f(\\mathbf{p} - h\\mathbf{u})}{2h}$ (ou le produit scalaire du gradient avec $\\mathbf{u}$) ; une `ValueError` si les longueurs diffèrent, si la direction est le vecteur nul, ou si $h \\le 0$ ;
- `steepest_ascent_direction(f, point, h=1e-5)` : le vecteur unitaire $\\frac{\\nabla f(\\mathbf{p})}{\\|\\nabla f(\\mathbf{p})\\|}$, en tableau NumPy, avec le gradient calculé par ta fonction `partial_derivative` (une coordonnée à la fois) ; une `ValueError` si la norme du gradient calculé est inférieure à $10^{-8}$ (un point critique n'a pas de direction de plus grande pente ; numériquement, le gradient y est minuscule, pas forcément exactement nul), ou si $h \\le 0$.

La vérification calcule, pour $f(x, y) = x^2 y + 2y$ au point $(1, 3)$ :
- a) `directional_derivative(f, (1.0, 3.0), (1, 0))` (4 décimales) ;
- b) `directional_derivative(f, (1.0, 3.0), (2, 2))` (4 décimales) ;
- c) `directional_derivative(f, (1.0, 3.0), (-1, 2))` (4 décimales) ;
- d) `steepest_ascent_direction(f, (1.0, 3.0))` (une liste, 4 décimales) ;
- e) le nom de l'erreur levée par `directional_derivative(f, (1.0, 3.0), (0, 0))` ;

puis :
- f) le nom de l'erreur levée par `steepest_ascent_direction(lambda p: p[0] ** 2 + 2 * p[1] ** 2 + p[1] ** 3, (0.0, 0.0))` ;
- g) le nom du type de `steepest_ascent_direction(f, (1.0, 3.0))`, en texte ;
- h) la norme de `steepest_ascent_direction(lambda p: np.exp(p[0] - p[1]) + p[2] ** 2, (0.0, 1.0, 1.5))` (4 décimales).

Dans ta copie : calcule $\\nabla f(1, 3)$ à la main, puis a), b) et c). Que représente la direction de c) sur la carte des lignes de niveau de $f$ ? Pourquoi f) n'a-t-il pas de réponse ?""",
    todo=LOAD_LEARNER,
    check='''F_19 = lambda p: p[0] ** 2 * p[1] + 2 * p[1]                # noqa: E731
with checked("M05b.19a"):
    wbm.check("M05b.19a", mymath.multivar.directional_derivative(F_19, (1.0, 3.0), (1, 0)), computed=True)
with checked("M05b.19b"):
    wbm.check("M05b.19b", mymath.multivar.directional_derivative(F_19, (1.0, 3.0), (2, 2)), computed=True)
with checked("M05b.19c"):
    wbm.check("M05b.19c", mymath.multivar.directional_derivative(F_19, (1.0, 3.0), (-1, 2)), computed=True)
with checked("M05b.19d"):
    wbm.check("M05b.19d", np.asarray(mymath.multivar.steepest_ascent_direction(F_19, (1.0, 3.0))).tolist(),
              computed=True)
with checked("M05b.19e"):
    wbm.check("M05b.19e", raised(mymath.multivar.directional_derivative, F_19, (1.0, 3.0), (0, 0)), computed=True)
with checked("M05b.19f"):
    wbm.check("M05b.19f", raised(mymath.multivar.steepest_ascent_direction,
                                 lambda p: p[0] ** 2 + 2 * p[1] ** 2 + p[1] ** 3, (0.0, 0.0)), computed=True)
with checked("M05b.19g"):
    wbm.check("M05b.19g", type(mymath.multivar.steepest_ascent_direction(F_19, (1.0, 3.0))).__name__, computed=True)
with checked("M05b.19h"):
    wbm.check("M05b.19h", float(np.linalg.norm(mymath.multivar.steepest_ascent_direction(
        lambda p: np.exp(p[0] - p[1]) + p[2] ** 2, (0.0, 1.0, 1.5)))), computed=True)''',
    solution=LOAD_REF + '''
F_19 = lambda p: p[0] ** 2 * p[1] + 2 * p[1]                # noqa: E731 - gradient (2xy, x² + 2) = (6, 3) at (1, 3)
dd, steep = mymath.multivar.directional_derivative, mymath.multivar.steepest_ascent_direction
print("a)", dd(F_19, (1.0, 3.0), (1, 0)), " b)", dd(F_19, (1.0, 3.0), (2, 2)), " c)", dd(F_19, (1.0, 3.0), (-1, 2)))
print("d)", steep(F_19, (1.0, 3.0)), " e)", raised(dd, F_19, (1.0, 3.0), (0, 0)),
      " f)", raised(steep, lambda p: p[0] ** 2 + 2 * p[1] ** 2 + p[1] ** 3, (0.0, 0.0)),
      " g)", type(steep(F_19, (1.0, 3.0))).__name__,
      " h)", np.linalg.norm(steep(lambda p: np.exp(p[0] - p[1]) + p[2] ** 2, (0.0, 1.0, 1.5))))''',
    record=f'''wbm.record("M05b.19a", 6.0, decimals=4)
wbm.record("M05b.19b", 9 / 2 ** 0.5, decimals=4,
           mistakes={{"divise la direction par sa norme avant de dériver": 18.0}})
wbm.record("M05b.19c", 0.0, decimals=4)
wbm.record("M05b.19d", [2 / 5 ** 0.5, 1 / 5 ** 0.5], decimals=4,
           mistakes={{"divise le gradient par sa norme : la docstring demande un vecteur unitaire": [6.0, 3.0]}})
wbm.record("M05b.19e", "ValueError",
           mistakes={{"le vecteur nul ne donne aucune direction : lève une ValueError avant de diviser par sa norme":
                         {{"aucune", "ZeroDivisionError"}},
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "ZeroDivisionError")}}})
wbm.record("M05b.19f", "ValueError",
           mistakes={{"le gradient est nul en ce point : la docstring demande une ValueError quand la norme du "
                      "gradient calculé est inférieure à 1e-8 (numériquement, elle n'est pas forcément exactement 0)":
                         {{"aucune", "ZeroDivisionError"}},
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "ZeroDivisionError")}}})
wbm.record("M05b.19g", "ndarray",
           mistakes={{"la docstring demande un tableau NumPy : np.array(...)": {{"list", "tuple"}}}})
wbm.record("M05b.19h", 1.0, decimals=4,
           mistakes={{"divise le gradient par sa norme : la docstring demande un vecteur unitaire":
                         float(np.linalg.norm([math.exp(-1), -math.exp(-1), 3.0]))}})''',
    after=tests_cells("test_directional_derivative_ or test_steepest_ascent_direction_"),
    note="$\\nabla f = (2xy,\\ x^2 + 2) = (6, 3)$ en $(1, 3)$. a) $\\frac{\\partial f}{\\partial x} = 6$. b) $\\frac{(6, 3) "
         "\\cdot (2, 2)}{\\|(2, 2)\\|} = \\frac{18}{2\\sqrt{2}} \\approx 6{,}3640$ (et 18 si l'on oublie de normaliser). c) "
         "$(6, 3) \\cdot (-1, 2) = 0$ : la direction $(-1, 2)$ est orthogonale au gradient, c'est celle de la ligne de "
         "niveau de $f$ qui passe par $(1, 3)$. d) $\\frac{(6, 3)}{\\sqrt{45}} = \\frac{(2, 1)}{\\sqrt{5}} \\approx "
         "(0{,}8944 ;\\ 0{,}4472)$. f) Le point $(0, 0)$ est un minimum local de $x^2 + 2y^2 + y^3$ : le gradient y est "
         "nul, aucune direction ne monte plus qu'une autre au premier ordre. Les différences centrées y donnent "
         "$(0, h^2) \\approx (0, 10^{-10})$, pas exactement $(0, 0)$ : d'où la tolérance $10^{-8}$ de la docstring.",
)

M05B_20 = Ex(
    "M05b.20", "🔨", 1, 15, "Le plan tangent · `tangent_plane`",
    "programmer le plan tangent à une surface en un point, et mesurer l'écart entre la surface et ce plan.",
    "fiche §5 ; Ex M05b.18", tracks="C", mymath="multivar.py",
    body="""Écris `tangent_plane(f, point, h=1e-5)` (fiche §5) : les coefficients $(A, B, C)$ du plan tangent $z = Ax + By + C$ à la surface $z = f(x, y)$ au point $(x_0, y_0)$, avec $A$ et $B$ les deux dérivées partielles (ta fonction `partial_derivative`) et $C$ choisi pour que le plan passe par $(x_0, y_0, f(x_0, y_0))$ ; une `ValueError` si le point n'a pas exactement deux coordonnées, ou si $h \\le 0$. Renvoie un tuple de trois `float` de Python.

La vérification calcule :
- a) `tangent_plane(lambda p: p[0] * np.exp(p[1]), (2.0, 0.0))` (une liste, 4 décimales) ;
- b) `tangent_plane(lambda p: np.log(p[0] ** 2 + p[1] ** 2), (1.0, 1.0))` (une liste, 4 décimales) ;
- c) le nom de l'erreur levée par `tangent_plane(lambda p: p[0] + p[1] + p[2], (1.0, 2.0, 3.0))` ;
- d) l'écart entre la surface de a) et son plan tangent au point $(2 ;\\ 0{,}1)$, $f - (Ax + By + C)$ (5 décimales) ;
- e) les trois nombres renvoyés en a) sont-ils des `float` de Python ? (`True` ou `False`)

Dans ta copie : écris les deux plans à la main, sous la forme $z = f(x_0, y_0) + \\ldots$, puis développés. L'écart de d) est-il positif ou négatif, et que dit son signe sur la surface près du point, dans la direction de $y$ ? Calcule $D = f_{xx}f_{yy} - f_{xy}^2$ en $(2, 0)$ : la surface reste-t-elle du même côté de son plan dans toutes les directions ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M05b.20a"):
    wbm.check("M05b.20a", list(mymath.multivar.tangent_plane(lambda p: p[0] * np.exp(p[1]), (2.0, 0.0))),
              computed=True)
with checked("M05b.20b"):
    wbm.check("M05b.20b", list(mymath.multivar.tangent_plane(lambda p: np.log(p[0] ** 2 + p[1] ** 2), (1.0, 1.0))),
              computed=True)
with checked("M05b.20c"):
    wbm.check("M05b.20c", raised(mymath.multivar.tangent_plane, lambda p: p[0] + p[1] + p[2], (1.0, 2.0, 3.0)),
              computed=True)
with checked("M05b.20d"):
    A_20, B_20, C_20 = mymath.multivar.tangent_plane(lambda p: p[0] * np.exp(p[1]), (2.0, 0.0))
    wbm.check("M05b.20d", 2 * math.exp(0.1) - (A_20 * 2 + B_20 * 0.1 + C_20), computed=True)
with checked("M05b.20e"):
    wbm.check("M05b.20e", all(type(v) is float for v in mymath.multivar.tangent_plane(
        lambda p: p[0] * np.exp(p[1]), (2.0, 0.0))), computed=True)''',
    solution=LOAD_REF + '''
plane = mymath.multivar.tangent_plane
A_20, B_20, C_20 = plane(lambda p: p[0] * np.exp(p[1]), (2.0, 0.0))
print("a)", (A_20, B_20, C_20), " b)", plane(lambda p: np.log(p[0] ** 2 + p[1] ** 2), (1.0, 1.0)),
      " c)", raised(plane, lambda p: p[0] + p[1] + p[2], (1.0, 2.0, 3.0)))
print("d)", 2 * math.exp(0.1) - (A_20 * 2 + B_20 * 0.1 + C_20),
      " e)", all(type(v) is float for v in (A_20, B_20, C_20)))''',
    record=f'''wbm.record("M05b.20a", [1.0, 2.0, 0.0], decimals=4,
           mistakes={{"C n'est pas f(x₀, y₀) : développe z = f(x₀, y₀) + A (x − x₀) + B (y − y₀)":
                         [1.0, 2.0, 2.0]}})
wbm.record("M05b.20b", [1.0, 1.0, math.log(2) - 2], decimals=4,
           mistakes={{"C n'est pas f(x₀, y₀) : développe z = f(x₀, y₀) + A (x − x₀) + B (y − y₀)":
                         [1.0, 1.0, math.log(2)]}})
wbm.record("M05b.20c", "ValueError",
           mistakes={{"un plan tangent est celui d'une surface z = f(x, y) : un point de trois coordonnées demande une "
                      "ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M05b.20d", 2 * math.exp(0.1) - 2.2, decimals=5,
           mistakes={{"l'écart demandé est f moins le plan, pas le plan moins f": 2.2 - 2 * math.exp(0.1)}})
wbm.record("M05b.20e", True,
           mistakes={{"la docstring demande des float de Python : float(...) convertit un nombre de NumPy": False}})''',
    after=tests_cells("test_tangent_plane_"),
    note="a) $f(2, 0) = 2$, $f_x = e^y = 1$, $f_y = x\\,e^y = 2$ : $z = 2 + (x - 2) + 2y$, soit $z = x + 2y$, et $C = 0$. "
         "b) $f(1, 1) = \\ln 2$, $f_x = \\frac{2x}{x^2 + y^2} = 1$, $f_y = 1$ : $z = \\ln 2 + (x - 1) + (y - 1)$, donc "
         "$C = \\ln 2 - 2 \\approx -1{,}3069$. d) $2\\,e^{0{,}1} \\approx 2{,}210342$ contre $2 + 0{,}2 = 2{,}2$ : un "
         "écart d'environ $0{,}01034$, positif. Dans la direction de $y$, la tranche $y \\mapsto 2e^y$ est convexe "
         "($f_{yy} = 2 > 0$) : la surface est au-dessus de son plan, l'écart valant environ $\\frac{1}{2}f_{yy}\\,\\Delta y^2 "
         "= 0{,}01$. Mais $D = 0 \\times 2 - 1^2 = -1 < 0$ : dans d'autres directions, comme $(2, -1)$, la surface passe "
         "au-dessous de son plan (elle le traverse, comme une selle).",
)

M05B_21 = Ex(
    "M05b.21", "📦", 1, 20, "SymPy : dérivées partielles, gradient, points critiques",
    "calculer avec SymPy des dérivées partielles, un gradient, les points critiques et la matrice des dérivées "
    "secondes d'une fonction de deux variables, et les classer.", "fiche §2, §6 et §7", tracks="C, E",
    body="""SymPy (M02a, M05a) dérive aussi en plusieurs variables :
- `x, y = sp.symbols("x y")`, puis `sp.diff(k, x)` donne $\\frac{\\partial k}{\\partial x}$, et `sp.diff(k, x, y)` donne $\\frac{\\partial^2 k}{\\partial y\\,\\partial x}$ ;
- `sp.solve([kx, ky], [x, y], dict=True)` résout le système $\\nabla k = \\mathbf{0}$ : une liste de dictionnaires `{x: ..., y: ...}` ;
- `sp.hessian(k, (x, y))` donne la matrice des dérivées secondes, `.det()` son déterminant $D$, et `.subs({x: 1, y: 2})` remplace les variables par des nombres.

Avec $k(x, y) = x^2 y + y^2 - y$, calcule :
- a) le nombre de points critiques de $k$ (un entier) ;
- b) la valeur de $k$ en son minimum local (une fraction irréductible, en texte) ;
- c) le déterminant $D$ de la matrice des dérivées secondes en $(1, 0)$ (un entier) ;
- d) $\\frac{\\partial^2 k}{\\partial x\\,\\partial y}(3, 1)$ (un entier) ;
- e) $\\nabla k(2, 1)$ (une liste de 2 entiers) ;
- f) $\\frac{\\partial k}{\\partial y}$ (une expression en $x$ et $y$, en texte).

Dans ta copie : classe les points critiques par le test du second ordre (un tableau : point, $k_{xx}$, $k_{yy}$, $k_{xy}$, $D$, nature). Vérifie a) et c) à la main. Le minimum local est-il global (regarde $k(x, -1)$) ?""",
    todo='''answer_M05b_21a = ...  # a) an integer
answer_M05b_21b = ...  # b) an irreducible fraction, as text
answer_M05b_21c = ...  # c) an integer
answer_M05b_21d = ...  # d) an integer
answer_M05b_21e = ...  # e) a list of 2 integers
answer_M05b_21f = ...  # f) an expression in x and y, as text''',
    check='''for letter, answer in zip("abcdef", [answer_M05b_21a, answer_M05b_21b, answer_M05b_21c, answer_M05b_21d,
                                     answer_M05b_21e, answer_M05b_21f]):
    wbm.check(f"M05b.21{letter}", answer)''',
    solution='''x, y = sp.symbols("x y")
k = x ** 2 * y + y ** 2 - y
kx, ky = sp.diff(k, x), sp.diff(k, y)
critical = sp.solve([kx, ky], [x, y], dict=True)
H = sp.hessian(k, (x, y))
for point in critical:
    print(point, "· k =", k.subs(point), "· D =", H.det().subs(point), "· k_xx =", H[0, 0].subs(point))
answer_M05b_21a = len(critical)
answer_M05b_21b = str(k.subs({x: 0, y: sp.Rational(1, 2)}))
answer_M05b_21c = int(H.det().subs({x: 1, y: 0}))
answer_M05b_21d = int(sp.diff(k, x, y).subs({x: 3, y: 1}))
answer_M05b_21e = [int(kx.subs({x: 2, y: 1})), int(ky.subs({x: 2, y: 1}))]
answer_M05b_21f = str(ky)
print(answer_M05b_21a, answer_M05b_21b, answer_M05b_21c, answer_M05b_21d, answer_M05b_21e, answer_M05b_21f)''',
    record='''wbm.record("M05b.21a", 3,
           mistakes={"compte toutes les solutions que renvoie sp.solve, une par dictionnaire": {1, 2}})
wbm.record("M05b.21b", "-1/4", kind="fraction", simplified=True,
           mistakes={"refais le calcul de k au point critique, terme par terme": "1/4",
                     "c'est la valeur de k en un point selle": "0"})
wbm.record("M05b.21c", -4,
           mistakes={"le terme k_xy² se retranche dans D": 4, "k_xy est au carré dans D": -2})
wbm.record("M05b.21d", 6)
wbm.record("M05b.21e", [4, 5],
           mistakes={"l'ordre est [∂k/∂x, ∂k/∂y]": [5, 4]})
wbm.record("M05b.21f", "x**2 + 2*y - 1", kind="expr", variables=("x", "y"),
           mistakes={"c'est ∂k/∂x ; la question demande ∂k/∂y": "2*x*y"})''',
    note="$\\nabla k = (2xy,\\ x^2 + 2y - 1)$ s'annule si $x = 0$ et $y = \\frac{1}{2}$, ou si $y = 0$ et $x = \\pm 1$ : "
         "trois points critiques. La matrice des dérivées secondes est $\\begin{pmatrix} 2y & 2x \\\\ 2x & 2 "
         "\\end{pmatrix}$ : en $(0, \\frac{1}{2})$, $D = 2 > 0$ et $k_{xx} = 1 > 0$, un minimum local, où $k = \\frac{1}{4} "
         "- \\frac{1}{2} = -\\frac{1}{4}$ ; en $(\\pm 1, 0)$, $D = 0 \\times 2 - 4 = -4 < 0$, deux points selles. Le minimum "
         "n'est pas global : $k(x, -1) = 2 - x^2$ tend vers $-\\infty$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M05b.22 to M05b.24)
# ---------------------------------------------------------------------------
M05B_22_EXPERIMENT = '''ref_22 = wbm.load_mymath("ref", alias="mymath_ref")   # the reference library: the same results as yours
f_22 = lambda p: p[0] ** 2 + 3 * p[1] ** 2          # noqa: E731
P_22 = np.array([3.0, 1.0])
grad_22 = np.array([2 * P_22[0], 6 * P_22[1]])            # (6, 6)
tangent_22 = np.array([1.0, -1.0]) / math.sqrt(2)          # orthogonal to the gradient
print("a) slope along the level line:", round(ref_22.multivar.directional_derivative(f_22, P_22, tangent_22), 6) + 0.0)
print("b) f(P) =", f_22(P_22), "· f(P + 0.5 u) =", f_22(P_22 + 0.5 * tangent_22))
print("c) slope along the gradient:", round(ref_22.multivar.directional_derivative(f_22, P_22, grad_22), 6),
      "· ||grad f|| =", round(float(np.linalg.norm(grad_22)), 6))
angles_22 = np.linspace(0, 2 * np.pi, 3601)[:-1]
slopes_22 = grad_22[0] * np.cos(angles_22) + grad_22[1] * np.sin(angles_22)
print("d) angles (in degrees) where the slope is zero:",
      np.degrees(angles_22[np.isclose(slopes_22, 0, atol=1e-9)]).round(1))'''

M05B_22 = Ex(
    "M05b.22", "🔮", 1, 10, "Prédire : la dérivée directionnelle le long d'une ligne de niveau",
    "prévoir la pente d'une fonction le long d'une ligne de niveau et le long du gradient, puis le vérifier.",
    "fiche §3 et §4", tracks="C, E", hypothesis=True,
    body="""Soit $f(x, y) = x^2 + 3y^2$ et le point $P = (3, 1)$, où $f(P) = 12$ et $\\nabla f(P) = (6, 6)$. On note $\\mathbf{u} = \\frac{(1, -1)}{\\sqrt{2}}$, la direction de la ligne de niveau 12 en $P$. Choisis, pour chaque question :
- a) la dérivée directionnelle de $f$ en $P$ dans la direction $\\mathbf{u}$ : (1) positive ; (2) nulle ; (3) négative ; (4) cela dépend du sens de $\\mathbf{u}$ ;
- b) en avançant de 0,5 depuis $P$, en ligne droite dans la direction $\\mathbf{u}$, $f$ : (1) reste exactement égale à 12 ; (2) augmente un peu ; (3) diminue un peu ; (4) ne peut pas se prévoir ;
- c) la dérivée directionnelle de $f$ en $P$ dans la direction du gradient : (1) 0 ; (2) $\\|\\nabla f(P)\\| \\approx 8{,}49$ ; (3) 1 ; (4) 6 ;
- d) combien de directions (vecteurs unitaires) donnent une dérivée directionnelle nulle en $P$ : (1) aucune ; (2) exactement une ; (3) exactement deux ; (4) une infinité.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience. Elle utilise la fonction `directional_derivative` de la référence (la tienne, M05b.19, fait la même chose).""",
    todo='''prediction_M05b_22a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M05b_22b = ...  # b) 1, 2, 3 or 4
prediction_M05b_22c = ...  # c) 1, 2, 3 or 4
prediction_M05b_22d = ...  # d) 1, 2, 3 or 4''',
    check='''for letter, prediction in zip("abcd", [prediction_M05b_22a, prediction_M05b_22b, prediction_M05b_22c,
                                      prediction_M05b_22d]):
    wbm.check(f"M05b.22{letter}", prediction)''',
    record='''wbm.record("M05b.22a", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M05b.22b", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M05b.22c", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M05b.22d", 3, prediction=True, choices=[1, 2, 3, 4])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(M05B_22_EXPERIMENT, ["prediction_M05b_22a", "prediction_M05b_22b", "prediction_M05b_22c",
                                               "prediction_M05b_22d"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", M05B_22_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : pourquoi la pente est-elle nulle dans la direction de la ligne "
               "de niveau, alors que $f$ augmente quand on avance en ligne droite (calcule $f(P + t\\,\\mathbf{u})$ en "
               "fonction de $t$) ? Dessine l'ellipse $x^2 + 3y^2 = 12$, sa tangente en $P$ et le gradient. Que "
               "deviennent ces réponses pour une fonction affine ?"),
    ],
    note="a) $\\nabla f(P) \\cdot \\mathbf{u} = \\frac{6 - 6}{\\sqrt{2}} = 0$ : la direction de la ligne de niveau est "
         "orthogonale au gradient, et ce dans les deux sens. b) $f(P + t\\,\\mathbf{u}) = 12 + 0 \\times t + 2t^2$ : la "
         "pente est nulle, mais la droite tangente sort de l'ellipse, vers des valeurs plus grandes (la surface est un "
         "bol) ; en $t = 0{,}5$, $f = 12{,}5$. c) La pente dans la direction du gradient est la plus grande, "
         "$\\|\\nabla f(P)\\| = 6\\sqrt{2} \\approx 8{,}49$. d) Les deux vecteurs unitaires orthogonaux au gradient, "
         "$\\pm\\mathbf{u}$ : la pente $\\|\\nabla f\\|\\cos\\theta$ ne s'annule que pour $\\theta = \\pm 90°$.",
)

M05B_23_CHECK = '''F_23 = lambda p: math.exp(p[0] - p[1])                  # noqa: E731 - tangent plane at (0, 0): z = 1 + x − y
with checked("M05b.23a"):
    wbm.check("M05b.23a", plane_error(F_23, (0.0, 0.0), (1, 0), 0.1), computed=True)
with checked("M05b.23b"):
    wbm.check("M05b.23b", plane_error(F_23, (0.0, 0.0), (1, 0), 0.2) / plane_error(F_23, (0.0, 0.0), (1, 0), 0.1),
              computed=True)
with checked("M05b.23c"):
    rs_23 = np.array([0.01, 0.02, 0.04, 0.08])
    errors_23 = [plane_error(F_23, (0.0, 0.0), (1, 0), r) for r in rs_23]
    wbm.check("M05b.23c", np.polyfit(np.log(rs_23), np.log(errors_23), 1)[0], computed=True)
with checked("M05b.23d"):
    wbm.check("M05b.23d", plane_error(F_23, (0.0, 0.0), (1, 1), 0.5), computed=True)
with checked("M05b.23e"):
    wbm.check("M05b.23e", plane_error(F_23, (0.0, 0.0), (1, -1), 0.1), computed=True)'''

M05B_23 = Ex(
    "M05b.23", "🔬", 2, 20, "L'erreur du plan tangent quand on s'éloigne du point",
    "mesurer comment l'écart entre une surface et son plan tangent grandit avec la distance au point, et selon la "
    "direction.", "fiche §5 ; Ex M05b.20 ; M05a §3", tracks="C",
    body="""La fiche (§5) annonce que l'erreur de l'approximation par le plan tangent est d'ordre 2 : elle se comporte comme le carré de la distance au point. Vérifie-le.

Écris `plane_error(f, point, direction, r)`, qui renvoie l'écart, en valeur absolue, entre $f$ et son plan tangent en `point` (ta fonction `mymath.multivar.tangent_plane` : écris d'abord M05b.20), au point situé à la distance `r` de `point` dans la direction du vecteur `direction` (à normaliser), en `float`.

La vérification prend $f(x, y) = e^{x - y}$, dont le plan tangent en $(0, 0)$ est $z = 1 + x - y$, et calcule :
- a) l'erreur dans la direction $(1, 0)$, à la distance $r = 0{,}1$ (6 décimales) ;
- b) le rapport des erreurs pour $r = 0{,}2$ et $r = 0{,}1$, dans la direction $(1, 0)$ (2 décimales) ;
- c) la pente de la droite qui ajuste $\\ln(\\text{erreur})$ en fonction de $\\ln r$, pour $r = 0{,}01$ ; 0,02 ; 0,04 ; 0,08 dans la direction $(1, 0)$, par `np.polyfit` (2 décimales) ;
- d) l'erreur dans la direction $(1, 1)$, à la distance $r = 0{,}5$ (6 décimales) ;
- e) l'erreur dans la direction $(1, -1)$, à la distance $r = 0{,}1$ (6 décimales).

Dans ta copie : que dit c) de l'ordre de l'erreur ? Que vaut d), et pourquoi, même loin du point (regarde $f$ le long de la droite $y = x$) ? Compare e) et a) avec le terme d'ordre 2 de Taylor, $\\frac{s^2}{2}$, où $s = x - y$ au point d'arrivée.""",
    todo='''def plane_error(f, point, direction, r):
    """|f(q) - plane(q)| where q is at distance r from point in the direction of the vector direction, and plane is
    the tangent plane of f at point (mymath.multivar.tangent_plane)."""
    raise NotImplementedError("le vecteur unitaire, le point q, le plan tangent, puis l'écart en valeur absolue")''',
    check=M05B_23_CHECK,
    solution='''def plane_error(f, point, direction, r):
    """|f(q) - plane(q)| where q is at distance r from point in the direction of the vector direction, and plane is
    the tangent plane of f at point (mymath.multivar.tangent_plane)."""
    p = np.array(point, dtype=float)
    u = np.array(direction, dtype=float)
    u = u / np.linalg.norm(u)
    q = p + r * u
    a, b, c = mymath.multivar.tangent_plane(f, p)
    return float(abs(f(q) - (a * q[0] + b * q[1] + c)))


F_23 = lambda p: math.exp(p[0] - p[1])                  # noqa: E731
for direction in [(1, 0), (0, 1), (1, 1), (1, -1)]:
    print(direction, [f"{plane_error(F_23, (0.0, 0.0), direction, r):.3e}" for r in (0.1, 0.2, 0.4)])
rs_23 = np.array([0.01, 0.02, 0.04, 0.08])
print("slope:", np.polyfit(np.log(rs_23), np.log([plane_error(F_23, (0.0, 0.0), (1, 0), r) for r in rs_23]), 1)[0])''',
    record='''wbm.record("M05b.23a", 0.0051709181, decimals=6,
           mistakes={"l'erreur est l'écart entre f et son plan tangent, pas entre f et f(point)": 0.1051709181})
wbm.record("M05b.23b", 4.1390634791, decimals=2)
wbm.record("M05b.23c", 2.0111414941, decimals=2)
wbm.record("M05b.23d", 0.0, decimals=6)
wbm.record("M05b.23e", 0.0104885539, decimals=6,
           mistakes={"divise la direction par sa norme : le point est à la distance r du point de départ":
                         0.0214027582})''',
    note="a) $e^{0{,}1} - 1{,}1 \\approx 0{,}005171$. b) et c) Doubler la distance multiplie l'erreur par environ 4 : "
         "elle est d'ordre 2 ($r^2$), comme le terme $\\frac{s^2}{2}$ de Taylor, avec $s = x - y$. d) Le long de la "
         "droite $y = x$, $f = e^0 = 1$ et le plan vaut $1 + x - x = 1$ : la surface et le plan s'y confondent. e) Dans "
         "la direction $(1, -1)$, $s = r\\sqrt{2}$ est le plus grand possible à distance $r$ : $e^{s} - 1 - s \\approx "
         "\\frac{s^2}{2} = r^2 = 0{,}01$ (exactement $0{,}010489$), deux fois l'erreur de a) environ.",
)

M05B_24_CHECK = '''with checked("M05b.24 vérifications"):
    import matplotlib.contour as mcontour
    import matplotlib.quiver as mquiver
    problems = []
    f_t = lambda x, y: np.exp(-(x ** 2 + 2 * y ** 2) / 4)                      # noqa: E731 - another example
    grad_t = lambda x, y: (-x / 2 * f_t(x, y), -y * f_t(x, y))                 # noqa: E731
    fig, ax = plt.subplots(figsize=(6, 5))
    try:
        created = drawn(draw_gradient_map, ax, f_t, grad_t, (-3, 3), (-2, 2))
    finally:
        plt.close(fig)                                                         # only the checks below are shown here
    if created:
        problems.append("draw_gradient_map ouvre sa propre figure : dessine dans l'axe reçu")
    else:
        contours = [c for c in ax.collections if isinstance(c, mcontour.ContourSet)]
        quivers = [c for c in ax.collections if isinstance(c, mquiver.Quiver)]
        if not contours:
            problems.append("il manque les lignes de niveau (ax.contour)")
        elif len(contours[0].levels) < 5:
            problems.append("trace au moins 5 lignes de niveau")
        elif not getattr(contours[0], "labelTexts", None):
            problems.append("écris la valeur des lignes de niveau (ax.clabel)")
        if not quivers:
            problems.append("il manque les flèches du gradient (ax.quiver)")
        else:
            q = quivers[0]
            xy = np.asarray(q.get_offsets(), dtype=float)
            u, v = np.ravel(q.U), np.ravel(q.V)
            gx, gy = grad_t(xy[:, 0], xy[:, 1])
            norms = np.hypot(gx, gy) * np.hypot(u, v)
            keep = norms > 1e-12
            cosines = (u * gx + v * gy)[keep] / norms[keep]
            if xy.shape[0] < 20:
                problems.append("dessine au moins 20 flèches, sur une grille")
            elif xy.shape[0] > 1000:
                problems.append("dessine les flèches sur une grille plus grossière que celle des lignes de niveau "
                                "(quelques centaines au plus) : sinon elles se recouvrent")
            elif cosines.size == 0 or np.min(cosines) < 0.999:
                problems.append("les flèches doivent avoir la direction et le sens du gradient en leur point de départ "
                                "(ax.quiver(X, Y, U, V), avec U et V les deux composantes du gradient)")
            if xy.size and (xy[:, 0].min() > -2.5 or xy[:, 0].max() < 2.5 or xy[:, 1].min() > -1.5
                            or xy[:, 1].max() < 1.5):
                problems.append("répartis les flèches sur tout le rectangle reçu")
        if ax.get_aspect() not in (1.0, "equal"):
            problems.append("prends la même échelle sur les deux axes (ax.set_aspect(\\"equal\\")) : sans elle, un "
                            "cercle paraît ovale et les angles sont déformés")
    if problems:
        print("❌ Ex M05b.24 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M05b.24 : lignes de niveau et flèches du gradient justes, à la même échelle.")'''

M05B_24 = Ex(
    "M05b.24", "🎨", 1, 20, "Lignes de niveau et flèches du gradient sur la même figure",
    "tracer une carte de lignes de niveau et les flèches du gradient, et voir qu'elles coupent les lignes à angle "
    "droit et s'allongent là où les lignes se serrent.", "fiche §1 et §4 ; R0 (matplotlib)", tracks="C, E",
    body="""Écris `draw_gradient_map(ax, f, grad, xlim, ylim)`, qui dessine dans l'axe `ax`, sur le rectangle $[x_{\\min}, x_{\\max}] \\times [y_{\\min}, y_{\\max}]$ donné par `xlim` et `ylim` :
- au moins 5 lignes de niveau de `f` (`ax.contour(X, Y, Z, levels=...)`, sur une grille fine faite par `np.meshgrid`), avec leurs valeurs (`ax.clabel`) ;
- les flèches du gradient sur une grille plus grossière, d'au moins 20 points répartis sur tout le rectangle (`ax.quiver(X, Y, U, V)`, où `U` et `V` sont les deux composantes du gradient) ;
- la même échelle sur les deux axes (`ax.set_aspect("equal")`) : sans elle, un cercle paraît ovale, et l'angle entre une flèche et une ligne de niveau est déformé.

Ici, `f(x, y)` et `grad(x, y)` prennent **deux** arguments, qui peuvent être des tableaux : `f` renvoie un tableau de valeurs, et `grad` un couple de tableaux `(U, V)`.

Puis trace la carte de $f(x, y) = \\sin x + \\cos y$, de gradient $(\\cos x, -\\sin y)$, sur $[-4, 4] \\times [-4, 4]$.

Dans ta copie : repère sur ta figure les maxima, les minima et les points selles de $f$ (que font les flèches autour de chacun ?). Où les flèches sont-elles les plus longues, et que font les lignes de niveau à cet endroit ?""",
    todo='''def draw_gradient_map(ax, f, grad, xlim, ylim):
    """In ax, on the rectangle xlim × ylim: at least 5 level lines of f with their values, the arrows of grad on a
    coarser grid (at least 20 points), and the same scale on both axes."""
    raise NotImplementedError("np.meshgrid, ax.contour et ax.clabel, puis ax.quiver, et ax.set_aspect(\\"equal\\")")''',
    check='''with checked("M05b.24 figure"):
    fig, ax = plt.subplots(figsize=(6.5, 6))
    try:
        created = drawn(draw_gradient_map, ax, lambda x, y: np.sin(x) + np.cos(y),
                        lambda x, y: (np.cos(x), -np.sin(y)), (-4, 4), (-4, 4))
    except BaseException:
        plt.close(fig)                                     # no empty figure while the function is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M05b.24 : draw_gradient_map ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans l'axe "
              "reçu.")
    else:
        plt.show()''',
    solution='''def draw_gradient_map(ax, f, grad, xlim, ylim):
    """In ax, on the rectangle xlim × ylim: at least 5 level lines of f with their values, the arrows of grad on a
    coarser grid (at least 20 points), and the same scale on both axes."""
    X, Y = np.meshgrid(np.linspace(*xlim, 200), np.linspace(*ylim, 200))
    contours = ax.contour(X, Y, f(X, Y), levels=10, cmap="viridis")
    ax.clabel(contours, fontsize=7)
    XA, YA = np.meshgrid(np.linspace(*xlim, 13), np.linspace(*ylim, 13))
    U, V = grad(XA, YA)
    ax.quiver(XA, YA, U, V, color="gray")
    ax.set(xlabel="x", ylabel="y", title="Lignes de niveau et gradient")
    ax.set_aspect("equal")


fig, ax = plt.subplots(figsize=(6.5, 6))
draw_gradient_map(ax, lambda x, y: np.sin(x) + np.cos(y), lambda x, y: (np.cos(x), -np.sin(y)), (-4, 4), (-4, 4))
plt.show()''',
    after=[("md", "**Vérifications automatiques** (sur un autre exemple ; la figure elle-même se juge à l'œil)."),
           ("code", M05B_24_CHECK)],
    note="Sur $[-4, 4]^2$, $\\sin x + \\cos y$ a un maximum en $(\\frac{\\pi}{2}, 0)$ (où $f = 2$), deux minima en "
         "$(-\\frac{\\pi}{2}, \\pm\\pi)$ (où $f = -2$) et trois points selles, en $(-\\frac{\\pi}{2}, 0)$ et "
         "$(\\frac{\\pi}{2}, \\pm\\pi)$ (où $f = 0$). Les flèches convergent vers le maximum, s'éloignent des minima, "
         "et, près d'une selle, arrivent de deux côtés et repartent des deux autres. Elles coupent toutes les lignes de "
         "niveau à angle droit, et elles sont les plus longues là où les lignes se serrent : $\\|\\nabla f\\|^2 = "
         "\\cos^2 x + \\sin^2 y$ est le plus grand vers $x = 0$ ou $\\pm\\pi$ et $y = \\pm\\frac{\\pi}{2}$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M05b.25 to M05b.27)
# ---------------------------------------------------------------------------
M05B_25_MISTAKES = bug_letters_mistakes(
    "BDF", "ACE",
    {"B": "refais chaque calcul de dérivée sur un petit exemple",
     "D": "refais chaque calcul de pente sur un petit exemple",
     "F": "refais chaque mise à jour de coordonnée sur un petit exemple"},
    name_correct=False)

M05B_25 = Ex(
    "M05b.25", "🐛", 1, 15, "Chasse à l'erreur : la mauvaise variable dérivée, une direction non unitaire",
    "repérer dans du code les erreurs classiques sur les dérivées partielles, les directions et le pas de descente, "
    "puis calculer les bonnes valeurs.", "fiche §2, §3 et §8", tracks="C",
    body="""Soit $f(x, y) = x^3 y - 2y^2$ et le point $P = (1, 3)$. Une collègue a écrit six lignes, chacune avec un commentaire qui dit ce qu'elle veut calculer ; chaque ligne utilise les variables des lignes précédentes telles qu'elles **devraient** être (on suppose les lignes précédentes justes). Trois lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter de code**, trouve-les.

```python
x, y, h = 1.0, 3.0, 1e-5
dfdx = 3 * x ** 2 * y                                  # (A) ∂f/∂x at P
dfdy = (f(x + h, y) - f(x - h, y)) / (2 * h)           # (B) ∂f/∂y at P, by a centred difference
norm = math.sqrt(dfdx ** 2 + dfdy ** 2)                # (C) the norm of the gradient at P
slope = 3 * dfdx + 4 * dfdy                            # (D) the slope of f at P in the direction of (3, 4)
change = 0.01 * (dfdx + dfdy)                          # (E) about how much f changes from P to (1.01, 3.01)
x_new = x + 0.1 * dfdx                                 # (F) x after one step of gradient descent, η = 0.1
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire (une liste de 6 nombres, 3 décimales).

Dans ta copie : pour chaque ligne fausse, quelle erreur a été faite, et comment la corriger ? Laquelle des lignes justes utilise l'approximation linéaire du §5 ?""",
    todo='''answer_M05b_25a = ...  # a) letters, as text
answer_M05b_25b = ...  # b) a list of 6 values (3 decimals)''',
    check='''wbm.check("M05b.25a", answer_M05b_25a)
wbm.check("M05b.25b", answer_M05b_25b)''',
    solution='''answer_M05b_25a = "BDF"
x, y = 1.0, 3.0
dfdx = 3 * x ** 2 * y                                  # (A) correct: 9
dfdy = x ** 3 - 4 * y                                  # (B) the y-coordinate must move: -11
norm = math.sqrt(dfdx ** 2 + dfdy ** 2)                # (C) correct: √202
slope = (3 * dfdx + 4 * dfdy) / 5                      # (D) the direction divided by its norm
change = 0.01 * (dfdx + dfdy)                          # (E) correct: ∇f · (0.01, 0.01)
x_new = x - 0.1 * dfdx                                 # (F) descent: minus
answer_M05b_25b = [dfdx, dfdy, norm, slope, change, x_new]
print(answer_M05b_25a, [round(value, 4) for value in answer_M05b_25b])''',
    record=f'''wbm.record("M05b.25a", "BDF",
           mistakes={M05B_25_MISTAKES})
wbm.record("M05b.25b", [9, -11, 202 ** 0.5, -3.4, -0.02, 0.1], decimals=3,
           mistakes={{"(B) : ∂f/∂y demande de déplacer y": [9, 9, 202 ** 0.5, -3.4, -0.02, 0.1],
                     "(D) : la direction (3, 4) se divise par sa norme": [9, -11, 202 ** 0.5, -17, -0.02, 0.1],
                     "(F) : un pas de descente retire η ∂f/∂x": [9, -11, 202 ** 0.5, -3.4, -0.02, 1.9]}})''',
    note="(B) déplace $x$ au lieu de $y$ : elle calcule $\\frac{\\partial f}{\\partial x}$, qui vaut 9 ; la bonne valeur "
         "est $\\frac{\\partial f}{\\partial y} = x^3 - 4y = -11$. (D) oublie de diviser $(3, 4)$ par sa norme 5 : "
         "$\\frac{27 - 44}{5} = -3{,}4$, et non $-17$. (F) monte au lieu de descendre : $x - 0{,}1 \\times 9 = 0{,}1$. "
         "(A), (C) et (E) sont justes ; (E) est l'approximation linéaire $\\nabla f \\cdot (0{,}01 ;\\ 0{,}01) = "
         "0{,}01 \\times (9 - 11) = -0{,}02$ (la vraie variation vaut environ $-0{,}019$).",
)

M05B_26_CHECK = '''with checked("M05b.26 vérifications"):
    problems = []
    xs_t, ys_t = np.linspace(-1, 2, 7), np.linspace(0, 1, 4)              # different lengths: a transposition shows
    for name, f_t in [("x + 10 y", lambda x, y: x + 10 * y), ("x² y − y", lambda x, y: x ** 2 * y - y),
                      ("cos(x y)", lambda x, y: np.cos(x * y))]:
        expected = np.array([[f_t(xv, yv) for xv in xs_t] for yv in ys_t])
        try:
            got = grid_values(f_t, xs_t, ys_t)
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"grid_values pour {name} lève {type(exc).__name__} ({exc})")
            continue
        if got is None:
            problems.append("grid_values ne renvoie rien : il manque return")
            break
        got = np.asarray(got)
        if got.shape != expected.shape:
            problems.append(f"pour {name}, la forme attendue est (len(ys), len(xs)) = {expected.shape}, pas {got.shape}"
                            + (" : la ligne j correspond à ys[j] (np.meshgrid fait cela par défaut)"
                               if got.shape == expected.T.shape else ""))
            break
        elif not np.allclose(got, expected):
            problems.append(f"pour {name}, Z[j, i] doit valoir f(xs[i], ys[j])"
                            + (" : tu as échangé x et y" if np.allclose(got, np.array(
                                [[f_t(yv, xv) for xv in xs_t] for yv in ys_t]), equal_nan=True) else ""))
            break
    if problems:
        print("❌ Ex M05b.26 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M05b.26 : grid_values donne Z[j, i] = f(xs[i], ys[j]), avec la bonne forme, pour trois fonctions.")'''

M05B_26_TIME = '''import time
xs_26, ys_26 = np.linspace(-3, 3, 600), np.linspace(-2, 2, 400)
f_26 = lambda x, y: np.sin(x) * np.exp(-y ** 2)          # noqa: E731
start = time.perf_counter()
Z_loop = np.array([[f_26(xv, yv) for xv in xs_26] for yv in ys_26])
loop_seconds = time.perf_counter() - start
start = time.perf_counter()
Z_grid = np.asarray(grid_values(f_26, xs_26, ys_26))
grid_seconds = time.perf_counter() - start
same = Z_grid.shape == Z_loop.shape and np.allclose(Z_loop, Z_grid)
print(f"double loop: {loop_seconds:.3f} s · grid_values: {grid_seconds:.4f} s · same values: {same}")
if same and grid_seconds > loop_seconds / 5:
    print("💡 grid_values n'est guère plus rapide qu'une double boucle : calcule f sur toute la grille d'un coup.")'''

M05B_26 = Ex(
    "M05b.26", "🛠️", 1, 15, "Vectoriser : une fonction de deux variables sur une grille (`np.meshgrid`)",
    "calculer les valeurs d'une fonction de deux variables sur toute une grille d'un coup, avec `np.meshgrid`, dans "
    "la bonne orientation.", "fiche §1 ; R0 (NumPy)", tracks="C",
    body="""Pour tracer une carte de lignes de niveau, il faut les valeurs de $f$ en chaque point d'une grille, souvent des centaines de milliers. Une double boucle en Python est lente ; NumPy calcule tout d'un coup, à condition de lui donner deux tableaux de même forme : `X, Y = np.meshgrid(xs, ys)` donne `X[j, i] = xs[i]` et `Y[j, i] = ys[j]`, de forme `(len(ys), len(xs))`. La ligne `j` correspond à `ys[j]` : c'est l'orientation qu'attendent `plt.contour` et `plt.imshow` (les $y$ en lignes, les $x$ en colonnes).

Écris `grid_values(f, xs, ys)`, qui renvoie le tableau `Z` de forme `(len(ys), len(xs))` tel que `Z[j, i] = f(xs[i], ys[j])`, pour une fonction `f(x, y)` écrite avec NumPy (qui accepte des tableaux). La vérification compare ta fonction à une double boucle, sur des grilles de tailles différentes en $x$ et en $y$ (une transposition s'y voit), puis une dernière cellule compare les temps de calcul.

Dans ta copie : pourquoi la vérification prend-elle des grilles de tailles différentes ? Que se passerait-il avec une fonction écrite avec `math.sin` au lieu de `np.sin` ? Combien de fois plus rapide est `grid_values` sur la grille de la dernière cellule ?""",
    todo='''def grid_values(f, xs, ys):
    """Z with shape (len(ys), len(xs)) and Z[j, i] = f(xs[i], ys[j]), for f(x, y) written with NumPy."""
    raise NotImplementedError("X, Y = np.meshgrid(xs, ys), puis f(X, Y)")''',
    solution='''def grid_values(f, xs, ys):
    """Z with shape (len(ys), len(xs)) and Z[j, i] = f(xs[i], ys[j]), for f(x, y) written with NumPy."""
    X, Y = np.meshgrid(xs, ys)
    return np.asarray(f(X, Y), dtype=float)''',
    after=[("code", M05B_26_CHECK),
           ("md", "**Le temps de calcul** (cette cellule utilise ta fonction)."),
           ("todo", 'with checked("M05b.26 temps"):\n' + "\n".join("    " + line for line in M05B_26_TIME.splitlines())),
           ("solution", M05B_26_TIME)],
    note="`np.meshgrid(xs, ys)` range les $y$ en lignes et les $x$ en colonnes, comme une carte ; `np.meshgrid(xs, ys, "
         "indexing=\"ij\")` ferait l'inverse, et une grille carrée cacherait l'erreur, d'où les tailles différentes. Une "
         "fonction écrite avec `math.sin` refuse un tableau (`TypeError: only length-1 arrays…`) : il faut les "
         "fonctions de NumPy. Sur la grille de 600 × 400 points, la version vectorisée est en général des centaines de "
         "fois plus rapide que la double boucle.",
)

M05B_27_CHECK = '''with checked("M05b.27 défi"):
    rng_27 = np.random.default_rng(527)
    problems, worst_calls = [], 0
    for trial in range(6):
        coefs = rng_27.uniform(-3, 3, 5).round(2)

        def grad_t(p, coefs=coefs, calls=[]):
            calls.append(1)
            x, y = float(p[0]), float(p[1])
            a, b, c, d, e = coefs
            return np.array([2 * a * x + b * y + d, b * x + 2 * c * y + e])

        counter = grad_t.__defaults__[1]
        try:
            got = fit_quadratic(grad_t)
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"fit_quadratic lève {type(exc).__name__} ({exc})")
            break
        worst_calls = max(worst_calls, len(counter))
        if np.shape(got) != (5,) or not np.allclose(got, coefs, atol=1e-9):
            problems.append(f"pour les coefficients {coefs.tolist()}, fit_quadratic renvoie {np.round(got, 6).tolist()}")
            break
    if problems:
        print("❌ Ex M05b.27 : " + problems[0] + ".")
    elif worst_calls > 3:
        print(f"❌ Ex M05b.27 : coefficients justes, mais {worst_calls} appels au gradient (objectif : 3 au plus) : "
              "choisis des points où le gradient se lit le plus simplement.")
    else:
        print(f"✅ Ex M05b.27 : défi réussi, les cinq coefficients de six fonctions retrouvés en {worst_calls} appels "
              "au plus.")
with checked("M05b.27"):
    wbm.check("M05b.27", list(np.asarray(fit_quadratic(GRAD_27), dtype=float)), computed=True)'''

M05B_27_GIVEN = '''def GRAD_27(p):
    """The gradient of an unknown function a x² + b xy + c y² + d x + e y + g."""
    x, y = float(p[0]), float(p[1])
    return np.array([3 * x - 2 * y + 0.5, -2 * x + 6 * y - 4])'''

M05B_27 = Ex(
    "M05b.27", "🏆", 3, 25, "Défi : retrouver une fonction du second degré à partir de son gradient",
    "retrouver les coefficients d'une fonction du second degré de deux variables à partir de son gradient, avec le "
    "moins d'évaluations possible, puis en tirer son point critique.", "fiche §2, §3 et §7", tracks="C",
    body="""On ne connaît pas la fonction $f(x, y) = a x^2 + b\\,xy + c y^2 + d x + e y + g$, mais on peut calculer son gradient en n'importe quel point, grâce à une fonction `grad(p)` qui renvoie le tableau $\\nabla f(\\mathbf{p})$ (et qui coûte cher : chaque appel compte).

Écris `fit_quadratic(grad)`, qui renvoie la liste `[a, b, c, d, e]` (la constante $g$ ne se voit pas dans le gradient). **L'objectif** : des coefficients justes à $10^{-9}$ près, avec **au plus 3 appels** à `grad`. Commence par écrire $\\nabla f(x, y)$ en fonction des cinq coefficients, puis choisis des points où il se lit simplement.

La vérification essaie ta fonction sur six fonctions tirées au hasard (en comptant les appels), puis vérifie tes coefficients pour le gradient `GRAD_27` donné ci-dessous (une liste, 4 décimales).

Dans ta copie : pour la fonction de `GRAD_27`, écris $f$, trouve son point critique (un système de deux équations) et dis s'il s'agit d'un minimum, d'un maximum ou d'un point selle. Pourquoi deux appels ne peuvent-ils pas suffire en général ?""",
    given=M05B_27_GIVEN,
    todo='''def fit_quadratic(grad):
    """The coefficients [a, b, c, d, e] of f = a x² + b xy + c y² + d x + e y + g, from its gradient grad(p), with at
    most 3 calls to grad."""
    raise NotImplementedError("écris ∇f en fonction de a, b, c, d, e, puis choisis trois points bien placés")''',
    check=M05B_27_CHECK,
    solution='''def fit_quadratic(grad):
    """The coefficients [a, b, c, d, e] of f = a x² + b xy + c y² + d x + e y + g, from its gradient grad(p), with at
    most 3 calls to grad."""
    g0 = grad(np.array([0.0, 0.0]))          # (d, e)
    gx = grad(np.array([1.0, 0.0]))          # (2a + d, b + e)
    gy = grad(np.array([0.0, 1.0]))          # (b + d, 2c + e)
    d, e = g0
    a = (gx[0] - d) / 2
    b = gx[1] - e
    c = (gy[1] - e) / 2
    return [float(a), float(b), float(c), float(d), float(e)]


coefs_27 = fit_quadratic(GRAD_27)
a, b, c, d, e = coefs_27
critical_27 = np.linalg.solve([[2 * a, b], [b, 2 * c]], [-d, -e])
print("coefficients:", coefs_27, "· critical point:", critical_27, "· D =", (2 * a) * (2 * c) - b ** 2)''',
    after=[("solution", M05B_27_CHECK.split('with checked("M05b.27"):')[0].rstrip())],
    record='''wbm.record("M05b.27", [1.5, -2.0, 3.0, 0.5, -4.0], decimals=4,
           mistakes={"dérive a x² par rapport à x : quel coefficient obtiens-tu devant x ?":
                         [3.0, -2.0, 6.0, 0.5, -4.0]})''',
    note="$\\nabla f = (2ax + by + d,\\ bx + 2cy + e)$. En $(0, 0)$ : $(d, e)$ ; en $(1, 0)$ : $(2a + d,\\ b + e)$ ; en "
         "$(0, 1)$ : $(b + d,\\ 2c + e)$. Trois appels donnent six nombres, assez pour les cinq coefficients (avec une "
         "vérification gratuite : $b$ apparaît deux fois). Deux appels ne donnent que quatre nombres, pour cinq "
         "inconnues. Pour `GRAD_27` : $f = 1{,}5x^2 - 2xy + 3y^2 + 0{,}5x - 4y + g$ ; son point critique résout "
         "$3x - 2y = -0{,}5$ et $-2x + 6y = 4$, soit $(\\frac{5}{14}, \\frac{11}{14}) \\approx (0{,}357 ;\\ 0{,}786)$ ; "
         "avec $D = 3 \\times 6 - 4 = 14 > 0$ et $f_{xx} = 3 > 0$, c'est un minimum (global, la fonction est un bol).",
)


PART_A = Part("A", "Ta librairie : dérivées partielles, dérivée directionnelle, plan tangent ; SymPy",
              "Fiche §2 à §7. Les quatre fonctions de `mymath/multivar.py`, puis SymPy en plusieurs variables.",
              given=TOOLS, exercises=[M05B_18, M05B_19, M05B_20, M05B_21])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §1, §4 et §5. La pente le long d'une ligne de niveau, l'erreur du plan tangent, la carte des "
              "lignes de niveau avec les flèches du gradient.",
              exercises=[M05B_22, M05B_23, M05B_24])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §1 à §3 et §8. Trois erreurs à trouver, une grille de valeurs calculée d'un coup, puis une "
              "fonction retrouvée à partir de son gradient.",
              exercises=[M05B_25, M05B_26, M05B_27])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M05b.1 à M05b.10, M05b.14, M05b.16 | Les exercices papier (vérification) | ✏️ 🔗 📈 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M05b · Fonctions de plusieurs variables et gradient — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m05b_gradient/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M05b`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M05b · Fonctions de plusieurs variables et gradient — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : lignes de niveau, dérivées partielles, gradient, dérivée "
               "directionnelle, plus grande pente, plan tangent, dérivées secondes, points critiques, pas de descente, "
               "argmin sur un segment, gradient d'une loss, lecture d'une carte.\n"
               "- Écrire les quatre fonctions de `mymath/multivar.py` et les tester, puis utiliser SymPy.\n"
               "- Prédire la pente le long d'une ligne de niveau, mesurer l'erreur du plan tangent, tracer une carte "
               "avec les flèches du gradient, chasser des erreurs, vectoriser une grille, retrouver une fonction à "
               "partir de son gradient.\n\n"
               "**Rappel express.** $\\nabla f = (f_x, f_y)$ ; $D_{\\mathbf{u}} f = \\nabla f \\cdot \\mathbf{u}$ avec "
               "$\\|\\mathbf{u}\\| = 1$ ; plus grande montée $\\frac{\\nabla f}{\\|\\nabla f\\|}$, de pente $\\|\\nabla f\\|$ ; "
               "plan tangent $z = f(a, b) + f_x\\,(x - a) + f_y\\,(y - b)$ ; $D = f_{xx}f_{yy} - f_{xy}^2$ : $D > 0$ et "
               "$f_{xx} > 0$ minimum, $D > 0$ et $f_{xx} < 0$ maximum, $D < 0$ selle ; descente : $\\mathbf{x} - "
               "\\eta\\,\\nabla f(\\mathbf{x})$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu lire une carte de lignes de niveau, et calculer des dérivées partielles et un gradient ?\n"
               "2. Sais-tu calculer une dérivée directionnelle, et dire pourquoi le gradient donne la plus grande "
               "pente, à angle droit des lignes de niveau ?\n"
               "3. Sais-tu écrire un plan tangent, et classer un point critique par le test du second ordre ?\n"
               "4. Sais-tu expliquer pourquoi un petit pas contre le gradient fait baisser une fonction ?\n\n"
               "**La suite** : le chapitre 5 de workbookIA (gradient numérique, lignes de niveau, descente de "
               "gradient), puis M06, la théorie de l'information.")]


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
