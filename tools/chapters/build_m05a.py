#!/usr/bin/env python
"""Build the two notebooks of chapter M05a from a single source (used by Claude).

    python tools/chapters/build_m05a.py
    python tools/run_all_notebooks.py chapitres/m05a_derivees_taylor/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m05a_derivees_taylor/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M05a.1 to M05a.10, 🔗 M05a.14); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer nor the calculation that gives it. The data of the
notebook are new: none is a test case of tests/test_m05a_approx.py, an answer of the paper exercises, or an example of
workbookIA 5 (no x³ − 3x, no x e^(−x), no x³ − 2x, no error curve against the step h, no Rosenbrock).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M05a"
FOLDER = "chapitres/m05a_derivees_taylor"

F = 'kind="fraction", simplified=True'
X = 'kind="expr", variables=("x",)'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M05a.1", "Dérivées secondes et convexité", [
        ("a", "an integer", "4",
         '''mistakes={"c'est f'(0) ; dérive encore une fois": 1, "la dérivée de e^(2x) est 2 e^(2x) : n'oublie pas le '''
         '''facteur 2 de la règle de la chaîne": 2}'''),
        ("b", "an interval, as text", '"[-1 ; 1]"',
         '''kind="interval", mistakes={"l'intervalle demandé est fermé : g est concave aussi à ses bornes": "]-1 ; 1[", '''
         '''"g est concave là où g'' est négative ou nulle, pas là où elle est positive": "]-oo ; -1] U [1 ; +oo["}'''),
        ("c", "a list", "[-1, 1]", ''),
        ("d", "a number (4 decimals)", "6 * math.e",
         '''decimals=4, mistakes={"c'est w'(1) ; dérive encore une fois, par la règle du produit": 2 * math.e, '''
         '''"w'(x) = 2x e^(x²) est un produit : sa dérivée a deux termes": 4 * math.e}'''),
        ("e", "True or False", "False",
         '''mistakes={"calcule la dérivée seconde de 1/(1 + x²) et étudie son signe, par exemple en 0": True}'''),
        ("f", "a number (1 decimal)", "1 / 2",
         '''decimals=1, mistakes={"c'est h'(2) = ln 2 + 1 ; dérive encore une fois": 1.0 + 0.6931471806}'''),
        ("g", "an integer", "-6",
         '''mistakes={"un point d'inflexion annule la dérivée seconde, pas la dérivée première": -3, '''
         '''"la dérivée seconde de k x² est 2k": -12}'''),
        ("h", "a number (4 decimals)", "(1 + math.e ** 2) / 2 - math.e",
         '''decimals=4, mistakes={"l'écart demandé est le milieu de la corde moins la courbe : son signe compte": '''
         '''math.e - (1 + math.e ** 2) / 2}'''),
    ]),

    Paper("M05a.2", "Extrema locaux et globaux sur un intervalle fermé", [
        ("a", "a list", "[-1, 0, 2]",
         '''mistakes={"factorise entièrement f' : il manque une racine": [-1, 2]}'''),
        ("b", "a list", "[0, 5, -27]", ''),
        ("c", "an integer", "0",
         '''mistakes={"un maximum local a f'' < 0 : calcule f'' en chaque point critique": {-1, 2}}'''),
        ("d", "an integer", "37",
         '''mistakes={"compare toutes les valeurs : les points critiques et les deux bords": {32, 5}}'''),
        ("e", "an integer", "-2",
         '''mistakes={"compare toutes les valeurs : les points critiques et les deux bords": {3, 0}}'''),
        ("f", "an integer", "-27",
         '''mistakes={"compare les deux minimums locaux, et les bords": {0, 32}}'''),
        ("g", "a number (4 decimals)", "3 * 1.5 ** 4 + 4 * 1.5 ** 3 - 12 * 1.5 ** 2 + 5",
         '''decimals=4, mistakes={"compare aussi avec les bords de [−1,5 ; 1,5]": 5}'''),
        ("h", "True or False", "False",
         '''mistakes={"quand x tend vers ±∞, le terme 3x⁴ l'emporte : f n'est pas bornée": True}'''),
    ]),

    Paper("M05a.3", "Points d'inflexion et test de la dérivée seconde", [
        ("a", "a list", "[0, 4]",
         '''mistakes={"factorise entièrement p' : il manque une racine": [4]}'''),
        ("b", "an integer", "320",
         '''mistakes={"c'est p'(4) ; dérive encore une fois": 0}'''),
        ("c", "an integer", "0", ''),
        ("d", "a letter, as text", '"A"',
         '''mistakes={"p''(0) = 0 ne permet pas de conclure : étudie le signe de p' juste avant et juste après 0": "C", '''
         '''"regarde le signe de p' juste avant et juste après 0 (par exemple en −1 et en 1)": "B"}'''),
        ("e", "a list", "[3]",
         '''mistakes={"un point d'inflexion demande que p'' change de signe : vérifie chacune de ses racines": [0, 3]}'''),
        ("f", "an integer", "-162", ''),
        ("g", "True or False", "False",
         '''mistakes={"(x⁴)'' = 12x² s'annule en 0 mais ne change pas de signe": True}'''),
    ]),

    Paper("M05a.4", "Polynômes de Taylor de trois fonctions usuelles", [
        ("a", "an expression in x, as text", '"1 - x**2/2"',
         X + ''', mistakes={"cos''(0) = −cos 0 = −1 : le terme d'ordre 2 est négatif": "1 + x**2/2", '''
             '''"divise le terme d'ordre 2 par 2! = 2": "1 - x**2"}'''),
        ("b", "an expression in x, as text", '"x - x**2/2 + x**3/3"',
         X + ''', mistakes={"recalcule f‴(0) pour ln(1 + x), puis divise-la par 3!": "x - x**2/2 + x**3/6", '''
             '''"les signes alternent": "x + x**2/2 + x**3/3"}'''),
        ("c", "an expression in x, as text", '"1 + x + x**2 + x**3"',
         X + ''', mistakes={"recalcule f″(0) et f‴(0) pour 1/(1 − x) avant de les diviser par 2! et 3!": '''
             '''"1 + x + x**2/2 + x**3/6", "dérive 1/(1 − x) avec la règle de la chaîne : (1 − x)′ = −1": '''
             '''"1 - x + x**2 - x**3"}'''),
        ("d", "a number (4 decimals)", "math.e * (1 + 0.1 + 0.1 ** 2 / 2)",
         '''decimals=4, mistakes={"le polynôme est centré en a = 1 : les puissances sont celles de (x − 1)": '''
         '''{1 + 1.1 + 1.1 ** 2 / 2, math.e * (1 + 1.1 + 1.1 ** 2 / 2)}, '''
         '''"en a = 1, les dérivées de eˣ valent e, pas 1": 1 + 0.1 + 0.1 ** 2 / 2}'''),
        ("e", "a number (5 decimals)", "0.1 - 0.1 ** 2 / 2 + 0.1 ** 3 / 3",
         '''decimals=5, mistakes={"le coefficient de x³ est 1/3": 0.1 - 0.1 ** 2 / 2 + 0.1 ** 3 / 6}'''),
        ("f", "an irreducible fraction, as text", "Fraction(1, 24)",
         F + ''', mistakes={"cos⁽⁴⁾(0) = cos 0 = 1 : le terme est positif": "-1/24", '''
             '''"divise par 4!, et non par 4": "1/4", "4! = 4 × 3 × 2 × 1": "1/12"}'''),
        ("g", "a number (3 decimals)", "1 - 0.3 ** 2 / 2",
         '''decimals=3, mistakes={"sin′(π/2) = cos(π/2) = 0 : pas de terme d'ordre 1": 1.3 - 0.3 ** 2 / 2, '''
         '''"divise le terme d'ordre 2 par 2! = 2": 1 - 0.3 ** 2}'''),
        ("h", "an integer", "1",
         '''mistakes={"le coefficient de (x − 1)² est q''(1)/2!": 2}'''),
    ]),

    Paper("M05a.5", "Le reste de Taylor : borner l'erreur d'une approximation", [
        ("a", "a number (6 decimals)", "0.5 - 0.5 ** 3 / 6",
         '''decimals=6, mistakes={"l'ordre 3 contient le terme en x³, divisé par 3! = 6": 0.5 - 0.5 ** 3 / 3}'''),
        ("b", "a number (7 decimals)", "abs(math.sin(0.5) - (0.5 - 0.5 ** 3 / 6))", 'decimals=7'),
        ("c", "a number (7 decimals)", "0.5 ** 5 / 120",
         '''decimals=7, mistakes={"le reste d'ordre 4 utilise la dérivée cinquième, avec x⁵/5!": 0.5 ** 4 / 24}'''),
        ("d", "an integer", "9",
         '''mistakes={"relis la borne : l'ordre n correspond à (n + 1)! au dénominateur": 10}'''),
        ("e", "a number (6 decimals)", "2 * 0.1 ** 3 / 6",
         '''decimals=6, mistakes={"le reste d'ordre 2 divise par 3! = 6": 2 * 0.1 ** 3 / 2}'''),
        ("f", "a number (7 decimals)", "0.2 ** 4 / 24",
         '''decimals=7, mistakes={"le terme en x³ de cos est nul : P₂ = P₃, et le reste d'ordre 3 utilise x⁴/4!": '''
         '''0.2 ** 3 / 6}'''),
        ("g", "a number (4 decimals)", "0.006 ** (1 / 3)",
         '''decimals=4, mistakes={"la borne est en x³ : quelle opération défait un cube ?": 0.006 ** (1 / 2)}'''),
    ]),

    Paper("M05a.6", "Newton à la main : une racine carrée en trois pas", [
        ("a", "an irreducible fraction, as text", "Fraction(19, 6)",
         F + ''', mistakes={"x₁ = x₀ − f(x₀)/f′(x₀) avec f(3) = −1 : le pas va vers la droite": "17/6"}'''),
        ("b", "an irreducible fraction, as text", "Fraction(721, 228)",
         F + ''', mistakes={"x₂ part de x₁, avec f′(x₁) = 2x₁": "361/114"}'''),
        ("c", "a number (10 decimals)", "float((Fraction(721, 228) + 10 / Fraction(721, 228)) / 2)",
         '''decimals=10, mistakes={"c'est x₂ ; fais encore un pas": 721 / 228}'''),
        ("d", "a number (2 decimals)", "(721 / 228 - math.sqrt(10)) * 1e6",
         '''decimals=2, mistakes={"l'erreur demandée est x₂ − √10 : x₂ est au-dessus de √10": '''
         '''-(721 / 228 - math.sqrt(10)) * 1e6, "calcule l'erreur avec la fraction exacte de b), pas avec x₂ arrondi : '''
         '''un arrondi à 4 ou 5 décimales change complètement une erreur de l'ordre de 10⁻⁶": '''
         '''{(3.1623 - math.sqrt(10)) * 1e6, (3.16228 - math.sqrt(10)) * 1e6}}'''),
        ("e", "a number (3 decimals)", "(721 / 228 - math.sqrt(10)) / (19 / 6 - math.sqrt(10)) ** 2",
         '''decimals=3, mistakes={"le dénominateur est le carré de l'erreur de x₁": '''
         '''(721 / 228 - math.sqrt(10)) / (19 / 6 - math.sqrt(10)), "garde les valeurs exactes de x₁ et x₂ (les '''
         '''fractions de a) et b)) : arrondir x₁ à 4 décimales change son erreur de quelques pour cent": '''
         '''(721 / 228 - math.sqrt(10)) / (3.1667 - math.sqrt(10)) ** 2}'''),
        ("f", "a number (4 decimals)", "-math.sqrt(10)",
         '''decimals=4, mistakes={"depuis un point négatif, la suite reste négative : elle va vers l'autre racine": '''
         '''math.sqrt(10)}'''),
        ("g", "True or False", "False",
         '''mistakes={"en 0, f′(0) = 0 : la tangente est horizontale et ne coupe pas l'axe": True}'''),
        ("h", "a number (4 decimals)", "4 - 2 * math.log(2)",
         '''decimals=4, mistakes={"le pas est g(x₀)/g′(x₀) avec g′(2) = 1/2 : diviser par 1/2, c'est multiplier par 2": '''
         '''2 - (math.log(2) - 1) / 2, "x₁ = x₀ − g(x₀)/g′(x₀) : vérifie le signe": 2 * math.log(2)}'''),
    ]),

    Paper("M05a.7", "L'erreur d'une différence avant et d'une différence centrée, par Taylor", [
        ("a", "an irreducible fraction, as text", "Fraction(1, 4)",
         F + ''', mistakes={"(√x)′ = 1/(2√x)": "1/2"}'''),
        ("b", "a number (5 decimals)", "(math.sqrt(4.2) - 2) / 0.2",
         '''decimals=5, mistakes={"divise la différence des deux valeurs par h": math.sqrt(4.2) - 2}'''),
        ("c", "a number (5 decimals)", "(math.sqrt(4.2) - 2) / 0.2 - 0.25",
         '''decimals=5, mistakes={"l'erreur est la différence avant moins f′(4) : son signe compte": '''
         '''0.25 - (math.sqrt(4.2) - 2) / 0.2}'''),
        ("d", "a number (6 decimals)", "0.1 * (-1 / 32)",
         '''decimals=6, mistakes={"f″(x) = −1/(4 x^(3/2)) est négative": 0.1 / 32, '''
         '''"la prévision est (h/2) f″(4), avec h/2 = 0,1": 0.2 * (-1 / 32)}'''),
        ("e", "a number (6 decimals)", "(math.sqrt(4.2) - math.sqrt(3.8)) / 0.4",
         '''decimals=6, mistakes={"la différence centrée divise par 2h, l'écart entre les deux points": '''
         '''(math.sqrt(4.2) - math.sqrt(3.8)) / 0.2}'''),
        ("f", "an irreducible fraction, as text", "Fraction(1, 12800)",
         F + ''', mistakes={"f‴(x) = 3/(8 x^(5/2)) est positive": "-1/12800", '''
             '''"la prévision divise h² f‴(4) par 6": "3/6400"}'''),
        ("g", "an integer", "4",
         '''mistakes={"l'erreur de la différence centrée est proportionnelle à h²": 2}'''),
        ("h", "a number (5 decimals)", "(math.sqrt(4.2) - 4 + math.sqrt(3.8)) / 0.04",
         '''decimals=5, mistakes={"la question demande la différence seconde, calculée avec les trois valeurs, pas '''
         '''f″(4)": -1 / 32}'''),
    ]),

    Paper("M05a.8", "Les flottants : 0,1 en binaire, epsilon machine, nombres représentables", [
        ("a", "a text of 3 digits, between quotes", '"101"',
         '''mistakes={"donne seulement les trois chiffres qui suivent la virgule": {"0.101", "0,101", ".101", ",101"}, '''
         '''"le premier chiffre après la virgule compte les demis, le deuxième les quarts, le troisième les huitièmes": '''
         '''"011"}'''),
        ("b", "a letter, as text", '"C"',
         '''mistakes={"écris chaque nombre comme une fraction irréductible : un développement binaire fini demande un '''
         '''dénominateur qui est une puissance de 2": {"A", "B", "D"}}'''),
        ("c", "a text of 4 digits, between quotes", '"1001"',
         '''mistakes={"le bloc commence juste après le « 0,0 » : reprends les multiplications par 2": '''
         '''{"0011", "0110", "1100"}}'''),
        ("d", "an integer", "-54",
         '''mistakes={"c'est l'écart après 1 ; entre deux puissances de 2, l'écart vaut ε fois la plus petite des deux": '''
         '''-52, "0,3 est en dessous de 0,5 : l'écart y est plus petit": -53}'''),
        ("e", "an integer", "-42",
         '''mistakes={"l'écart après 1 024 n'est pas l'écart après 1 : il grandit avec le nombre": -52, '''
         '''"l'écart grandit avec le nombre, il ne diminue pas": -62}'''),
        ("f", "an integer", "2 ** 24 + 1",
         '''mistakes={"vérifie que ton entier n'est pas lui-même représentable : une puissance de 2 l'est toujours": '''
         '''2 ** 24, "c'est pour float64 ; float32 garde 23 bits après la virgule": 2 ** 53 + 1}'''),
        ("g", "an irreducible fraction, as text", "Fraction(1, 2)",
         F + ''', mistakes={"l'écart est ε fois la puissance de 2 juste en dessous de 1 000, pas ε seul": "1/1024", '''
             '''"1 000 est en dessous de 1 024 : l'écart y est plus petit": "1"}'''),
        ("h", "an integer", "-24",
         '''mistakes={"c'est l'epsilon de float32 ; la question demande sa moitié": -23, '''
         '''"c'est pour float64 ; la question porte sur float32": -53}'''),
    ]),

    Paper("M05a.9", "Le meilleur pas par le calcul : minimiser une borne d'erreur", [
        ("a", "a number (3 decimals)", "2 * math.sqrt(1e-6 / 2) * 1000",
         '''decimals=3, mistakes={"le terme de bruit de la différence avant est 2δ/h": math.sqrt(1e-6) * 1000}'''),
        ("b", "a number (3 decimals)", "2 * math.sqrt(2 * 1e-6) * 1000",
         '''decimals=3, mistakes={"E(h*) additionne la troncature et le bruit": math.sqrt(2) * 1e-3 * 1000}'''),
        ("c", "a number (3 decimals)", "(3 * 1e-6 / 3) ** (1 / 3)",
         '''decimals=3, mistakes={"la troncature de la différence centrée est en h², pas en h : dérive la bonne borne": (1e-6) ** 0.5}'''),
        ("d", "a number (2 decimals)", "(3 / 6 * 0.01 ** 2 + 1e-6 / 0.01) * 1e4",
         '''decimals=2, mistakes={"ajoute le terme de bruit δ/h": 3 / 6 * 0.01 ** 2 * 1e4, '''
         '''"ajoute la troncature (M₃/6) h²": 1e-6 / 0.01 * 1e4}'''),
        ("e", "a number (1 decimal)", "0.1",
         '''decimals=1, mistakes={"un capteur plus précis permet un pas plus petit": 10.0}'''),
        ("f", "a number (2 decimals)", "0.01",
         '''decimals=2, mistakes={"remplace h* par son expression dans E : l'erreur au meilleur pas ne varie pas '''
         '''comme δ": 0.001, "c'est le facteur sur h* ; la question demande celui sur l'erreur": 0.1, '''
         '''"un capteur plus précis donne une erreur plus petite : le facteur est inférieur à 1": 100.0}'''),
        ("g", "a number (4 decimals)", "(4 * 1e-6) ** 0.25",
         '''decimals=4, mistakes={"dérive aussi le facteur 4 de 4δ/h²": (1e-6) ** 0.25, '''
         '''"vérifie la puissance de h qui reste dans E′(h) = 0": (4e-6) ** 0.5}'''),
        ("h", "True or False", "True",
         '''mistakes={"compare les erreurs au meilleur pas, b) et d), avec les mêmes unités": False}'''),
    ]),

    Paper("M05a.10", "log-sum-exp à la main : la softmax stable de trois scores", [
        ("a", "True or False", "True",
         '''mistakes={"le plus grand float vaut environ 1,8 × 10^308, soit e^709,78": False}'''),
        ("b", "an integer", "802", ''),
        ("c", "a number (4 decimals)", "802 + math.log(1 + math.exp(-2) + math.exp(-7))",
         '''decimals=4, mistakes={"rajoute le maximum m à la fin": math.log(1 + math.exp(-2) + math.exp(-7)), '''
         '''"le log-sum-exp dépasse le maximum : ajoute ln Σ e^(v_i − m)": 802}'''),
        ("d", "a list of 3 numbers (4 decimals)",
         "[math.exp(v - 802) / (1 + math.exp(-2) + math.exp(-7)) for v in (802, 800, 795)]",
         '''decimals=4, mistakes={"des probabilités ont une somme de 1 : divise par la somme des exponentielles": '''
         '''[1.0, math.exp(-2), math.exp(-7)]}'''),
        ("e", "a number (4 decimals)", "800 - (802 + math.log(1 + math.exp(-2) + math.exp(-7)))",
         '''decimals=4, mistakes={"le log-softmax retire le log-sum-exp, pas le seul maximum": -2, '''
         '''"le log-softmax est v₂ − LSE(v), un nombre négatif": 802 + math.log(1 + math.exp(-2) + math.exp(-7)) - 800}'''),
        ("f", "a number (4 decimals)", "802 + math.log(1 + math.exp(-2) + math.exp(-7)) - 795",
         '''decimals=4, mistakes={"la cross-entropy est −ln p₃, un nombre positif": '''
         '''795 - (802 + math.log(1 + math.exp(-2) + math.exp(-7)))}'''),
        ("g", "a number (4 decimals)", "802 + math.log(3)",
         '''decimals=4, mistakes={"le log-sum-exp de valeurs égales dépasse cette valeur (encadrement de la fiche §8)": 802}'''),
    ]),

    Paper("M05a.14", "Pourquoi les bibliothèques de ML calculent log(softmax) d'un seul coup", [
        ("a", "a number (2 decimals)", "780 + math.log(1 + math.exp(-760) + math.exp(-810))",
         '''decimals=2, mistakes={"compare les trois termes e^(z_j − m) : ils ne valent pas tous 1": 780 + math.log(3)}'''),
        ("b", "a number (2 decimals)", "20 - 780",
         '''decimals=2, mistakes={"le log-softmax est z₂ − LSE(z), un nombre négatif": 760}'''),
        ("c", "True or False", "True",
         '''mistakes={"e^(−760) est plus petit que le plus petit float positif, environ 5 × 10^−324 ≈ e^−744": False}'''),
        ("d", "a number (1 decimal)", "760",
         '''decimals=1, mistakes={"la loss est −log-softmax, un nombre positif": -760}'''),
        ("e", "True or False", "False",
         '''mistakes={"regarde ce que vaut p2 en float64 (question c)), puis son logarithme": True}'''),
        ("f", "a number (4 decimals)", "-1 - math.log(math.exp(2) + 1 + math.exp(-1))",
         '''decimals=4, mistakes={"le log-softmax retire le log-sum-exp, pas le seul maximum": -3, '''
         '''"le log-softmax est z₃ − LSE(z), un nombre négatif": 1 + math.log(math.exp(2) + 1 + math.exp(-1))}'''),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math
from fractions import Fraction'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M05a.1 à M05a.10, 🔗 M05a.14)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"7/9\"` ; une expression en $x$ entre guillemets, "
               "`\"2*x**3 - x\"` ;\n"
               "- une liste `[-1.5, 2.5]`, un intervalle entre guillemets `\"[-4, 6]\"`, `True` / `False`, une lettre "
               "entre guillemets, `\"B\"`, ou un texte de chiffres entre guillemets, `\"0111\"`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M05a.18 to M05a.23)
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

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M05a")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/approx.py`, lis la docstring "
         "de la fonction en entier, remplace la ligne `raise NotImplementedError(...)` par ton code, **enregistre** le "
         "fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. Le module `math` suffit "
         "(`math.exp`, `math.log`, `math.fsum`, `math.inf`, `math.isinf`). `numpy.finfo`, `sys.float_info` et "
         "`scipy.special.logsumexp` sont interdits : les tests comparent tes résultats à eux, et un test vérifie que "
         "tu ne t'en sers pas. Les nombres renvoyés sont des `float` de Python.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError"]


H_NOT_2H = ("ton résultat vaut le double de la dérivée : chaque différence centrée divise par 2h, l'écart entre "
            "x − h et x + h")


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of approx.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m05a_approx.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m05a_approx.py", "{keyword}", impl="ref")')]


M05A_18 = Ex(
    "M05a.18", "🔨", 1, 20, "Évaluer un polynôme de Taylor · `taylor_polynomial`",
    "programmer la valeur d'un polynôme de Taylor à partir des dérivées en un point, sans dépassement de capacité "
    "pour un grand nombre de termes.", "fiche §3", tracks="C, E", mymath="approx.py",
    body=HOWTO + """

Écris `taylor_polynomial(derivatives, a, x)` (fiche §3) : la valeur en $x$ du polynôme $\\sum_{k} \\frac{f^{(k)}(a)}{k!}(x - a)^k$, connaissant la liste $[f(a), f'(a), f''(a), \\ldots]$ ; une `ValueError` si la liste est vide.

Un piège : pour 200 termes, $k!$ devient un entier de plus de 370 chiffres, que Python ne sait plus convertir en `float` (une `OverflowError`). Garde plutôt à jour le terme $\\frac{(x - a)^k}{k!}$ : on passe du terme $k - 1$ au terme $k$ en le multipliant par $\\frac{x - a}{k}$.

La vérification calcule :
- a) `taylor_polynomial([0, 1, 0, -1, 0, 1], 0, 0.8)` (6 décimales) ;
- b) `taylor_polynomial([1, 0, -1, 0, 1], 0, 1.0)` (6 décimales) ;
- c) `taylor_polynomial([0, 1, -1, 2], 1, 1.5)` (6 décimales) ;
- d) le nom de l'erreur levée par `taylor_polynomial([], 0, 1.0)` ;
- e) le nom du type de `taylor_polynomial([2, 3], 1, 4)`, en texte ;
- f) `taylor_polynomial([4.0], 10, -3)` (4 décimales) ;
- g) `taylor_polynomial([1.0] * 30, 0, 5.0)` (4 décimales).

Dans ta copie : de quelles fonctions a), b) et c) sont-ils des polynômes de Taylor ? Compare a) à $\\sin 0{,}8$, b) à $\\cos 1$ et g) à $e^5$. Refais b) à la main.""",
    todo=LOAD_LEARNER,
    check='''with checked("M05a.18a"):
    wbm.check("M05a.18a", mymath.approx.taylor_polynomial([0, 1, 0, -1, 0, 1], 0, 0.8), computed=True)
with checked("M05a.18b"):
    wbm.check("M05a.18b", mymath.approx.taylor_polynomial([1, 0, -1, 0, 1], 0, 1.0), computed=True)
with checked("M05a.18c"):
    wbm.check("M05a.18c", mymath.approx.taylor_polynomial([0, 1, -1, 2], 1, 1.5), computed=True)
with checked("M05a.18d"):
    wbm.check("M05a.18d", raised(mymath.approx.taylor_polynomial, [], 0, 1.0), computed=True)
with checked("M05a.18e"):
    wbm.check("M05a.18e", type(mymath.approx.taylor_polynomial([2, 3], 1, 4)).__name__, computed=True)
with checked("M05a.18f"):
    wbm.check("M05a.18f", mymath.approx.taylor_polynomial([4.0], 10, -3), computed=True)
with checked("M05a.18g"):
    wbm.check("M05a.18g", mymath.approx.taylor_polynomial([1.0] * 30, 0, 5.0), computed=True)''',
    solution=LOAD_REF + '''
taylor = mymath.approx.taylor_polynomial
print("a)", taylor([0, 1, 0, -1, 0, 1], 0, 0.8), "· sin 0.8:", math.sin(0.8))
print("b)", taylor([1, 0, -1, 0, 1], 0, 1.0), "· cos 1:", math.cos(1.0))
print("c)", taylor([0, 1, -1, 2], 1, 1.5), "· ln 1.5:", math.log(1.5))
print("d)", raised(taylor, [], 0, 1.0), " e)", type(taylor([2, 3], 1, 4)).__name__, " f)", taylor([4.0], 10, -3))
print("g)", taylor([1.0] * 30, 0, 5.0), "· e**5:", math.exp(5))''',
    record=f'''wbm.record("M05a.18a", 0.7173973333, decimals=6,
           mistakes={{"divise chaque terme par k!": 0.61568}})
wbm.record("M05a.18b", 13 / 24, decimals=6,
           mistakes={{"divise chaque terme par k!": 1.0}})
wbm.record("M05a.18c", 5 / 12, decimals=6,
           mistakes={{"les puissances sont celles de (x − a), pas de x": 1.5}})
wbm.record("M05a.18d", "ValueError",
           mistakes={{"une liste vide ne définit aucun polynôme : lève une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M05a.18e", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit le résultat": "int",
                     "la docstring demande un float de Python : float(...) convertit un nombre de NumPy": "float64"}})
wbm.record("M05a.18f", 4.0, decimals=4,
           mistakes={{"le terme d'ordre 0 est f(a) lui-même : (x − a)⁰/0! = 1": 0.0}})
wbm.record("M05a.18g", 148.4131591026, decimals=4)''',
    after=tests_cells("test_taylor_polynomial_ or test_approx_uses_"),
    note="a) est le polynôme d'ordre 5 de $\\sin$ en 0 : $0{,}8 - \\frac{0{,}8^3}{6} + \\frac{0{,}8^5}{120} \\approx 0{,}717397$, "
         "contre $\\sin 0{,}8 \\approx 0{,}717356$. b) celui d'ordre 4 de $\\cos$ : $1 - \\frac{1}{2} + \\frac{1}{24} = "
         "\\frac{13}{24}$, contre $\\cos 1 \\approx 0{,}5403$. c) celui d'ordre 3 de $\\ln$ en 1 : $0{,}5 - 0{,}125 + "
         "\\frac{2 \\times 0{,}125}{6} = \\frac{5}{12}$, contre $\\ln 1{,}5 \\approx 0{,}4055$. f) Un seul terme : la "
         "constante $f(a)$. g) 30 termes de la série de $e^x$ suffisent à $x = 5$ : l'écart à $e^5$ vaut environ "
         "$4 \\times 10^{-12}$, de l'ordre du premier terme négligé $\\frac{5^{30}}{30!}$ (la borne de Lagrange, $\\frac{5^{30} e^5}{30!}$, "
         "donne $5 \\times 10^{-10}$).",
)

M05A_19 = Ex(
    "M05a.19", "🔨", 1, 20, "La méthode de Newton, avec ses cas d'échec · `newton`",
    "programmer la méthode de Newton avec un critère d'arrêt, et traiter ses échecs : tangente horizontale, pas de "
    "convergence.", "fiche §4", tracks="C, E", mymath="approx.py",
    body="""Écris `newton(f, fprime, x0, tol=1e-12, max_iter=50)` (fiche §4). L'ordre des tests compte ; à chaque pas :
1. si $f(x)$ vaut exactement 0, renvoie $x$ (c'est déjà un zéro) ;
2. sinon, si $f'(x)$ vaut 0, lève une `ValueError` (la tangente est horizontale) ;
3. sinon, calcule $x_{\\text{nouveau}} = x - \\frac{f(x)}{f'(x)}$, et renvoie-le si $|x_{\\text{nouveau}} - x| < \\text{tol}$.

Après `max_iter` pas sans s'arrêter, lève une `RuntimeError`.

La vérification calcule :
- a) `newton(lambda x: x * x - 7, lambda x: 2 * x, 3.0)` (10 décimales) ;
- b) `newton(lambda x: math.exp(-x) - x, lambda x: -math.exp(-x) - 1, 0.0)` (10 décimales) ;
- c) le nom de l'erreur levée par `newton(lambda x: x * x - 2 * x + 5, lambda x: 2 * x - 2, 1.0)` ;
- d) le nom de l'erreur levée par `newton(lambda x: x * x - 7, lambda x: 2 * x, 3.0, max_iter=3)` ;
- e) le nom de l'erreur levée par `newton(lambda x: (x - 2) ** 3, lambda x: 3 * (x - 2) ** 2, 2.0)`, ou `"aucune"` ;
- f) `newton(lambda x: x * x - 7, lambda x: 2 * x, 3.0, tol=0.1)` (7 décimales) ;
- g) le nom du type de `newton(lambda x: x - 5, lambda x: 1, 5)`, en texte.

Dans ta copie : écris les trois premiers pas de a) à la main. Quel nombre b) résout-il ? Pourquoi c) échoue-t-il, et ce polynôme a-t-il des racines réelles ? Pourquoi l'ordre des tests 1 et 2 compte-t-il pour e) ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M05a.19a"):
    wbm.check("M05a.19a", mymath.approx.newton(lambda x: x * x - 7, lambda x: 2 * x, 3.0), computed=True)
with checked("M05a.19b"):
    wbm.check("M05a.19b", mymath.approx.newton(lambda x: math.exp(-x) - x, lambda x: -math.exp(-x) - 1, 0.0),
              computed=True)
with checked("M05a.19c"):
    wbm.check("M05a.19c", raised(mymath.approx.newton, lambda x: x * x - 2 * x + 5, lambda x: 2 * x - 2, 1.0),
              computed=True)
with checked("M05a.19d"):
    wbm.check("M05a.19d", raised(mymath.approx.newton, lambda x: x * x - 7, lambda x: 2 * x, 3.0, max_iter=3),
              computed=True)
with checked("M05a.19e"):
    wbm.check("M05a.19e", raised(mymath.approx.newton, lambda x: (x - 2) ** 3, lambda x: 3 * (x - 2) ** 2, 2.0),
              computed=True)
with checked("M05a.19f"):
    wbm.check("M05a.19f", mymath.approx.newton(lambda x: x * x - 7, lambda x: 2 * x, 3.0, tol=0.1), computed=True)
with checked("M05a.19g"):
    wbm.check("M05a.19g", type(mymath.approx.newton(lambda x: x - 5, lambda x: 1, 5)).__name__, computed=True)''',
    solution=LOAD_REF + '''
newton = mymath.approx.newton
print("a)", newton(lambda x: x * x - 7, lambda x: 2 * x, 3.0), "· √7:", math.sqrt(7))
print("b)", newton(lambda x: math.exp(-x) - x, lambda x: -math.exp(-x) - 1, 0.0))
print("c)", raised(newton, lambda x: x * x - 2 * x + 5, lambda x: 2 * x - 2, 1.0),
      " d)", raised(newton, lambda x: x * x - 7, lambda x: 2 * x, 3.0, max_iter=3),
      " e)", raised(newton, lambda x: (x - 2) ** 3, lambda x: 3 * (x - 2) ** 2, 2.0))
print("f)", newton(lambda x: x * x - 7, lambda x: 2 * x, 3.0, tol=0.1),
      " g)", type(newton(lambda x: x - 5, lambda x: 1, 5)).__name__)''',
    record=f'''wbm.record("M05a.19a", 2.6457513111, decimals=10)
wbm.record("M05a.19b", 0.5671432904, decimals=10)
wbm.record("M05a.19c", "ValueError",
           mistakes={{"teste la pente avant de diviser : si f′(x) = 0, lève une ValueError": "ZeroDivisionError",
                     "en x = 1, la tangente est horizontale : lève une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "ZeroDivisionError")}}})
wbm.record("M05a.19d", "RuntimeError",
           mistakes={{"après max_iter pas sans s'arrêter, lève une RuntimeError": "aucune",
                     "pour x² − 7 depuis 3, la pente 2x ne s'annule jamais le long de la suite de Newton : vérifie le "
                     "pas, x − f(x)/f′(x), puis lève la RuntimeError après max_iter pas": "ValueError",
                     "{wrong_error("RuntimeError")}": {errors_source("RuntimeError", "ValueError")}}})
wbm.record("M05a.19e", "aucune",
           mistakes={{"x₀ = 2 est déjà un zéro de f : renvoie-le avant de regarder la pente": "ValueError",
                     "x₀ est déjà un zéro de f : renvoie-le avant tout calcul":
                         {errors_source("ValueError")}}})
wbm.record("M05a.19f", 2.6458333333, decimals=7,
           mistakes={{"tu renvoies la valeur d'avant : renvoie la nouvelle valeur dès que |x_(k+1) − x_k| < tol":
                         2.6666666667,
                     "arrête-toi dès que deux valeurs successives sont à moins de tol": 2.6457513123}})
wbm.record("M05a.19g", "float",
           mistakes={{"renvoie un float de Python, même quand x₀ est déjà un zéro : float(x0)": "int"}})''',
    after=tests_cells("test_newton_ or test_approx_uses_"),
    note="a) $x_1 = 3 - \\frac{2}{6} = \\frac{8}{3}$, $x_2 = \\frac{127}{48} \\approx 2{,}645833$, $x_3 \\approx "
         "2{,}6457513$ : $\\sqrt{7}$ à $1{,}3 \\times 10^{-9}$ près dès le troisième pas. b) Le nombre $x$ tel que $e^{-x} = x$, "
         "environ 0,567. c) $f'(1) = 0$ ; le polynôme $x^2 - 2x + 5 = (x - 1)^2 + 4$ n'a d'ailleurs aucune racine "
         "réelle. d) Trois pas ne suffisent pas pour $\\text{tol} = 10^{-12}$. e) $f(2) = 0$ **et** $f'(2) = 0$ : "
         "tester la pente d'abord lèverait une erreur sur un zéro déjà trouvé. f) Le deuxième pas ne bouge que de "
         "0,02 : on renvoie $x_2 = \\frac{127}{48}$. g) `float(x0)` au début suffit.",
)

M05A_20 = Ex(
    "M05a.20", "🔨", 2, 20, "L'extrapolation de Richardson : annuler le terme d'erreur en h² · `richardson_derivative`",
    "programmer l'extrapolation de Richardson de la différence centrée, et mesurer son ordre.",
    "fiche §5 ; Ex M05a.7", tracks="C", mymath="approx.py",
    body="""Écris `richardson_derivative(f, x, h=0.01)` (fiche §5) : avec la différence centrée $D(h) = \\frac{f(x + h) - f(x - h)}{2h}$, renvoie $\\frac{4D(h/2) - D(h)}{3}$ ; une `ValueError` si $h \\le 0$ (pense à $h = 0$ et à un $h$ négatif).

La vérification calcule :
- a) `richardson_derivative(math.cos, 0.6, 0.1)` (8 décimales) ;
- b) `richardson_derivative(math.log, 3.0)` (10 décimales) ;
- c) le nom de l'erreur levée par `richardson_derivative(math.exp, 1.0, -0.5)` ;
- d) `richardson_derivative(lambda t: t ** 4, 2.0, 0.5)` (4 décimales) ;
- e) le rapport des erreurs de `richardson_derivative(math.exp, 1.0, h)` pour $h = 0{,}2$ et $h = 0{,}1$ (1 décimale) ;
- f) le nom du type de `richardson_derivative(np.sin, 0.5, 0.1)`, en texte ;
- g) l'erreur de a), `richardson_derivative(math.cos, 0.6, 0.1) + math.sin(0.6)`, multipliée par $10^7$ (2 décimales).

Dans ta copie : quelle est la dérivée exacte en a) et en b) ? Calcule la différence centrée $D(0{,}1)$ de a) et son erreur : combien de fois plus grande que g) ? Pourquoi d) est-il exact, alors que $D(0{,}5)$ ne l'est pas (M05a.11, question 7) ? Que dit e) de l'ordre de la méthode ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M05a.20a"):
    wbm.check("M05a.20a", mymath.approx.richardson_derivative(math.cos, 0.6, 0.1), computed=True)
with checked("M05a.20b"):
    wbm.check("M05a.20b", mymath.approx.richardson_derivative(math.log, 3.0), computed=True)
with checked("M05a.20c"):
    wbm.check("M05a.20c", raised(mymath.approx.richardson_derivative, math.exp, 1.0, -0.5), computed=True)
with checked("M05a.20d"):
    wbm.check("M05a.20d", mymath.approx.richardson_derivative(lambda t: t ** 4, 2.0, 0.5), computed=True)
with checked("M05a.20e"):
    errors_20 = [abs(mymath.approx.richardson_derivative(math.exp, 1.0, h) - math.e) for h in (0.2, 0.1)]
    wbm.check("M05a.20e", errors_20[0] / errors_20[1], computed=True)
with checked("M05a.20f"):
    wbm.check("M05a.20f", type(mymath.approx.richardson_derivative(np.sin, 0.5, 0.1)).__name__, computed=True)
with checked("M05a.20g"):
    wbm.check("M05a.20g", (mymath.approx.richardson_derivative(math.cos, 0.6, 0.1) + math.sin(0.6)) * 1e7,
              computed=True)''',
    solution=LOAD_REF + '''
richardson = mymath.approx.richardson_derivative
centred_20 = (math.cos(0.7) - math.cos(0.5)) / 0.2
print("a)", richardson(math.cos, 0.6, 0.1), "· -sin 0.6:", -math.sin(0.6), "· D(0.1):", centred_20)
print("b)", richardson(math.log, 3.0), " c)", raised(richardson, math.exp, 1.0, -0.5),
      " d)", richardson(lambda t: t ** 4, 2.0, 0.5))
errors_20 = [abs(richardson(math.exp, 1.0, h) - math.e) for h in (0.2, 0.1)]
print("e)", errors_20[0] / errors_20[1], " f)", type(richardson(np.sin, 0.5, 0.1)).__name__)
print("g)", (richardson(math.cos, 0.6, 0.1) + math.sin(0.6)) * 1e7,
      "· error of D(0.1) × 1e7:", (centred_20 + math.sin(0.6)) * 1e7)''',
    record=f'''wbm.record("M05a.20a", -0.5646423558, decimals=8,
           mistakes={{"c'est la différence centrée D(h) ; combine D(h) et D(h/2)": -0.5637018730,
                     "le poids 4 va à D(h/2), le plus petit pas": -0.5634667523,
                     "{H_NOT_2H}": -1.1292847116}})
wbm.record("M05a.20b", 0.3333333333, decimals=10,
           mistakes={{"{H_NOT_2H}": 0.6666666667}})
wbm.record("M05a.20c", "ValueError",
           mistakes={{"un pas négatif ou nul est refusé : lève une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M05a.20d", 32.0, decimals=4,
           mistakes={{"c'est la différence centrée D(h) ; combine D(h) et D(h/2)": 34.0,
                     "le poids 4 va à D(h/2), le plus petit pas": 34.5,
                     "{H_NOT_2H}": 64.0}})
wbm.record("M05a.20e", 16.0142919864, decimals=1,
           mistakes={{"c'est le rapport d'une différence centrée, d'ordre 2 : combine D(h) et D(h/2)": 4.0060041442}})
wbm.record("M05a.20f", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy": "float64"}})
wbm.record("M05a.20g", 1.1759884333, decimals=2,
           mistakes={{"c'est l'erreur de la différence centrée D(h) ; combine D(h) et D(h/2)": 9406.0036561405}})''',
    after=tests_cells("test_richardson_derivative_ or test_approx_uses_"),
    note="a) La dérivée exacte est $-\\sin 0{,}6 \\approx -0{,}56464247$ ; $D(0{,}1)$ se trompe d'environ "
         "$9{,}4 \\times 10^{-4}$, Richardson d'environ $1{,}2 \\times 10^{-7}$, 8 000 fois moins. b) $\\frac{1}{3}$ à "
         "$2 \\times 10^{-12}$ près. d) Pour un polynôme de degré 4, $D(h) = f'(x) + c_2 h^2$ exactement ($D(h)$ n'a "
         "que des puissances paires de $h$, et $f^{(5)} = 0$) : la combinaison annule $c_2 h^2$ et donne $4x^3 = 32$, alors que "
         "$D(0{,}5) = 34$. e) Diviser $h$ par 2 divise l'erreur par $2^4 = 16$ : la méthode est d'ordre 4.",
)

M05A_21 = Ex(
    "M05a.21", "🔨", 1, 15, "L'epsilon machine, en float64, float32 et float16 · `machine_epsilon`",
    "calculer l'epsilon machine d'un type de flottants en le cherchant, puis relier l'écart entre deux flottants à "
    "la puissance de 2 du nombre.", "fiche §6 ; Ex M05a.8", tracks="C", mymath="approx.py",
    body="""Écris `machine_epsilon(dtype=float)` (fiche §6) : en partant de `eps = dtype(1)`, divise `eps` par 2 tant que `1 + eps / 2` est différent de 1, puis renvoie `eps`, converti en `float` de Python. Fais **chaque calcul dans le type demandé** : `one = dtype(1)`, `two = dtype(2)`, et `dtype(...)` autour de chaque résultat, pour qu'aucune opération ne passe en `float64` sans que tu le voies. `dtype` vaut `float`, `np.float32` ou `np.float16`.

`np.spacing(x)` donne l'écart entre $x$ et le flottant suivant.

La vérification calcule :
- a) `machine_epsilon() == 2 ** -52` ;
- b) `math.log2(machine_epsilon(np.float32))` (1 décimale) ;
- c) `machine_epsilon(np.float16)` (10 décimales) ;
- d) le nom du type de `machine_epsilon(np.float32)`, en texte ;
- e) `1 + machine_epsilon() / 2 == 1` ;
- f) `math.log2(np.spacing(1000.0) / machine_epsilon())` (1 décimale).

Dans ta copie : combien de fois la boucle tourne-t-elle pour chaque type ? Explique e) : où tombe $1 + \\frac{\\varepsilon}{2}$, exactement à mi-chemin entre deux flottants, et vers lequel est-il arrondi ? Explique f) avec la puissance de 2 juste en dessous de 1 000.""",
    todo=LOAD_LEARNER,
    check='''with checked("M05a.21a"):
    wbm.check("M05a.21a", mymath.approx.machine_epsilon() == 2 ** -52, computed=True)
with checked("M05a.21b"):
    wbm.check("M05a.21b", math.log2(mymath.approx.machine_epsilon(np.float32)), computed=True)
with checked("M05a.21c"):
    wbm.check("M05a.21c", mymath.approx.machine_epsilon(np.float16), computed=True)
with checked("M05a.21d"):
    wbm.check("M05a.21d", type(mymath.approx.machine_epsilon(np.float32)).__name__, computed=True)
with checked("M05a.21e"):
    wbm.check("M05a.21e", 1 + mymath.approx.machine_epsilon() / 2 == 1, computed=True)
with checked("M05a.21f"):
    wbm.check("M05a.21f", math.log2(np.spacing(1000.0) / mymath.approx.machine_epsilon()), computed=True)''',
    solution=LOAD_REF + '''
eps = mymath.approx.machine_epsilon
for dtype in (float, np.float32, np.float16):
    print(dtype.__name__, eps(dtype), "= 2 **", math.log2(eps(dtype)), "· finfo:", np.finfo(dtype).eps)
print("a)", eps() == 2 ** -52, " d)", type(eps(np.float32)).__name__, " e)", 1 + eps() / 2 == 1,
      " f)", math.log2(np.spacing(1000.0) / eps()))''',
    record='''wbm.record("M05a.21a", True,
           mistakes={"divise eps par 2 tant que 1 + eps/2 est différent de 1, et renvoie le dernier eps": False})
wbm.record("M05a.21b", -23.0, decimals=1,
           mistakes={"fais chaque calcul dans le type demandé : one = dtype(1), et dtype(...) autour de chaque "
                     "résultat": -52.0,
                     "renvoie eps, pas eps/2 : l'epsilon est l'écart entre 1 et le flottant suivant": -24.0})
wbm.record("M05a.21c", 2 ** -10, decimals=10,
           mistakes={"fais chaque calcul dans le type demandé : one = dtype(1), et dtype(...) autour de chaque "
                     "résultat": 2 ** -52,
                     "renvoie eps, pas eps/2 : l'epsilon est l'écart entre 1 et le flottant suivant": 2 ** -11})
wbm.record("M05a.21d", "float",
           mistakes={"la docstring demande un float de Python : float(eps) convertit un nombre de NumPy": "float32"})
wbm.record("M05a.21e", True,
           mistakes={"renvoie l'écart entre 1 et le flottant suivant, pas son double": False})
wbm.record("M05a.21f", 9.0, decimals=1,
           mistakes={"vérifie d'abord ton epsilon (question a)) : l'écart après 1 000 est ε fois une puissance de 2":
                         {8.0, 10.0}})''',
    after=tests_cells("test_machine_epsilon_ or test_approx_uses_"),
    note="La boucle tourne 52 fois pour `float64`, 23 pour `float32` et 10 pour `float16` : autant que de bits après "
         "la virgule. e) $1 + \\frac{\\varepsilon}{2}$ tombe exactement au milieu de 1 et $1 + \\varepsilon$ ; "
         "l'arrondi « au plus proche, à égalité vers le chiffre pair » le ramène à 1, dont le dernier bit est 0. f) "
         "$512 = 2^9 \\le 1000 < 2^{10}$ : entre 512 et 1 024, les flottants sont espacés de $2^9\\,\\varepsilon = "
         "2^{-43}$.",
)

M05A_22 = Ex(
    "M05a.22", "🔨", 1, 15, "Un log-sum-exp stable · `logsumexp`",
    "programmer un log-sum-exp qui ne déborde jamais, cas limites compris.", "fiche §8 ; Ex M05a.10",
    tracks="C, E", mymath="approx.py",
    body="""Écris `logsumexp(values)` (fiche §8) : $\\ln(e^{v_1} + \\cdots + e^{v_n}) = m + \\ln\\sum_i e^{v_i - m}$, avec $m$ le plus grand des $v_i$. Deux cas à part : une liste vide (une `ValueError`), et une liste dont toutes les valeurs valent `-math.inf` (renvoie `-math.inf` sans calculer $-\\infty - (-\\infty)$, qui donne `nan`). `math.fsum` additionne une liste de flottants avec un seul arrondi, à la fin.

La vérification calcule :
- a) `logsumexp([2, -1, 0.5])` (6 décimales) ;
- b) `logsumexp([1200, 1199])` (6 décimales) ;
- c) `logsumexp([-1500, -1502])` (6 décimales) ;
- d) `logsumexp([-math.inf, 0.0])` (4 décimales) ;
- e) `logsumexp([-math.inf, -math.inf]) == -math.inf` ;
- f) le nom de l'erreur levée par `logsumexp([])` ;
- g) le nom du type de `logsumexp(np.array([1.0, 2.0]))`, en texte ;
- h) `logsumexp([5.0] * 1000)` (6 décimales).

Dans ta copie : que donnerait le calcul direct `math.log(sum(math.exp(v) for v in values))` pour b) et pour c) ? Vérifie b) et h) avec l'encadrement $m \\le \\text{LSE} \\le m + \\ln n$.""",
    todo=LOAD_LEARNER,
    check='''with checked("M05a.22a"):
    wbm.check("M05a.22a", mymath.approx.logsumexp([2, -1, 0.5]), computed=True)
with checked("M05a.22b"):
    wbm.check("M05a.22b", mymath.approx.logsumexp([1200, 1199]), computed=True)
with checked("M05a.22c"):
    wbm.check("M05a.22c", mymath.approx.logsumexp([-1500, -1502]), computed=True)
with checked("M05a.22d"):
    wbm.check("M05a.22d", mymath.approx.logsumexp([-math.inf, 0.0]), computed=True)
with checked("M05a.22e"):
    wbm.check("M05a.22e", mymath.approx.logsumexp([-math.inf, -math.inf]) == -math.inf, computed=True)
with checked("M05a.22f"):
    wbm.check("M05a.22f", raised(mymath.approx.logsumexp, []), computed=True)
with checked("M05a.22g"):
    wbm.check("M05a.22g", type(mymath.approx.logsumexp(np.array([1.0, 2.0]))).__name__, computed=True)
with checked("M05a.22h"):
    wbm.check("M05a.22h", mymath.approx.logsumexp([5.0] * 1000), computed=True)''',
    solution=LOAD_REF + '''
lse = mymath.approx.logsumexp
print("a)", lse([2, -1, 0.5]), " b)", lse([1200, 1199]), " c)", lse([-1500, -1502]))
print("d)", lse([-math.inf, 0.0]), " e)", lse([-math.inf, -math.inf]) == -math.inf, " f)", raised(lse, []),
      " g)", type(lse(np.array([1.0, 2.0]))).__name__, " h)", lse([5.0] * 1000), "· 5 + ln 1000:", 5 + math.log(1000))
for values in ([1200, 1199], [-1500, -1502]):                     # the direct computation
    try:
        print(values, "direct:", math.log(sum(math.exp(v) for v in values)))
    except (OverflowError, ValueError) as exc:
        print(values, "direct:", type(exc).__name__, exc)''',
    record=f'''wbm.record("M05a.22a", 2.2413112967, decimals=6,
           mistakes={{"rajoute m à la fin : ln Σ e^(v_i − m) n'est que l'écart au maximum": 0.2413112967}})
wbm.record("M05a.22b", 1200.3132616875, decimals=6,
           mistakes={{"rajoute m à la fin : ln Σ e^(v_i − m) n'est que l'écart au maximum": 0.3132616875}})
wbm.record("M05a.22c", -1499.873071989, decimals=6,
           mistakes={{"rajoute m à la fin : ln Σ e^(v_i − m) n'est que l'écart au maximum": 0.126928011}})
wbm.record("M05a.22d", 0.0, decimals=4)
wbm.record("M05a.22e", True,
           mistakes={{"si toutes les valeurs valent -inf, renvoie -math.inf tout de suite : -inf − (-inf) donne nan":
                         False}})
wbm.record("M05a.22f", "ValueError",
           mistakes={{"une liste vide n'a pas de log-sum-exp : lève une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M05a.22g", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy": "float64"}})
wbm.record("M05a.22h", 11.907755279, decimals=6,
           mistakes={{"les 1 000 valeurs s'additionnent : le résultat dépasse le maximum": 5.0}})''',
    after=tests_cells("test_logsumexp_ or test_approx_uses_"),
    note="a) $2 + \\ln(1 + e^{-3} + e^{-1{,}5}) \\approx 2{,}2413$. b) Le calcul direct lève une `OverflowError` "
         "(`math.exp(1200)`) ; la version stable donne $1200 + \\ln(1 + e^{-1}) \\approx 1200{,}3133$, entre 1 200 et "
         "$1200 + \\ln 2$. c) Le calcul direct donne $\\ln 0$, une `ValueError` (*math domain error*) : les deux "
         "exponentielles s'effacent. h) 1 000 valeurs égales : $5 + \\ln 1000 \\approx 11{,}9078$, la borne de droite.",
)

M05A_23 = Ex(
    "M05a.23", "📦", 1, 15, "SymPy `series` et `numpy.finfo` contre tes fonctions",
    "obtenir des développements de Taylor avec SymPy et les limites des flottants avec `numpy.finfo`, et les comparer "
    "à tes fonctions.", "fiche §3 et §6", tracks="C",
    body="""Deux outils tout faits :
- `sp.series(expr, x, a, n)` donne le développement de Taylor de `expr` en `a`, jusqu'au terme de degré $n - 1$, suivi d'un $O(\\ldots)$ ; `.removeO()` l'enlève, et `.coeff(x, k)` lit le coefficient de $x^k$. `sp.diff(expr, x, k)` donne la dérivée $k$-ième, et `.subs(x, 0)` sa valeur en 0. Commence par `x = sp.Symbol("x")`.
- `np.finfo(dtype)` décrit un type de flottants : `.eps` (l'epsilon), `.max` (le plus grand), `.tiny` (le plus petit nombre positif **normal**). `np.nextafter(a, b)` donne le flottant qui suit `a` en allant vers `b`.

Calcule :
- a) le coefficient de $x^5$ dans le développement de $\\tan x$ en 0 (une fraction irréductible, en texte) ;
- b) le coefficient de $x^3$ dans le développement de $\\sqrt{1 + x}$ en 0 (une fraction irréductible, en texte) ;
- c) $\\log_2$ du plus petit `float16` positif normal (1 décimale) ;
- d) $\\log_{10}$ du plus petit `float64` positif normal (2 décimales) ;
- e) `np.nextafter(1.0, 2.0) - 1.0 == np.finfo(float).eps` (`True` ou `False`) ;
- f) la valeur en $x = 0{,}3$ du polynôme de Taylor d'ordre 4 de $e^{\\sin x}$ en 0, avec ses dérivées en 0 calculées par SymPy et ta fonction `taylor_polynomial` (5 décimales).

Dans ta copie : comment SymPy affiche-t-il le développement de $\\tan x$ ? Que valent les dérivées de f) ? Compare f) à $e^{\\sin 0{,}3}$. Pourquoi le plus grand `float16` est-il si petit ? Qu'y a-t-il entre 0 et `tiny` ?""",
    todo='''answer_M05a_23a = ...  # a) an irreducible fraction, as text
answer_M05a_23b = ...  # b) an irreducible fraction, as text
answer_M05a_23c = ...  # c) a number (1 decimal)
answer_M05a_23d = ...  # d) a number (2 decimals)
answer_M05a_23e = ...  # e) True or False
answer_M05a_23f = ...  # f) a number (5 decimals)''',
    check='''for letter, answer in zip("abcdef", [answer_M05a_23a, answer_M05a_23b, answer_M05a_23c, answer_M05a_23d,
                                     answer_M05a_23e, answer_M05a_23f]):
    wbm.check(f"M05a.23{letter}", answer)''',
    solution='''x = sp.Symbol("x")
print(sp.series(sp.tan(x), x, 0, 8))
answer_M05a_23a = str(sp.series(sp.tan(x), x, 0, 7).removeO().coeff(x, 5))
answer_M05a_23b = str(sp.series(sp.sqrt(1 + x), x, 0, 5).removeO().coeff(x, 3))
answer_M05a_23c = math.log2(np.finfo(np.float16).tiny)
answer_M05a_23d = math.log10(np.finfo(float).tiny)
answer_M05a_23e = bool(np.nextafter(1.0, 2.0) - 1.0 == np.finfo(float).eps)
derivatives_23 = [float(sp.diff(sp.exp(sp.sin(x)), x, k).subs(x, 0)) for k in range(5)]
answer_M05a_23f = mymath.approx.taylor_polynomial(derivatives_23, 0, 0.3)
print(answer_M05a_23a, answer_M05a_23b, answer_M05a_23c, round(answer_M05a_23d, 4), answer_M05a_23e,
      derivatives_23, answer_M05a_23f, "· exp(sin 0.3):", math.exp(math.sin(0.3)))
print("smallest positive float64 (subnormal):", np.nextafter(0.0, 1.0), "· tiny:", np.finfo(float).tiny)
print("float16: largest", int(np.finfo(np.float16).max), "· tiny", float(np.finfo(np.float16).tiny),
      "· smallest subnormal", float(np.finfo(np.float16).smallest_subnormal))''',
    record='''wbm.record("M05a.23a", Fraction(2, 15), kind="fraction", simplified=True,
           mistakes={"c'est le coefficient de x³ ; la question demande celui de x⁵": "1/3"})
wbm.record("M05a.23b", Fraction(1, 16), kind="fraction", simplified=True,
           mistakes={"c'est le coefficient de x² ; la question demande celui de x³": "-1/8"})
wbm.record("M05a.23c", -14.0, decimals=1,
           mistakes={"tiny est le plus petit float16 normal ; les nombres « sous-normaux » descendent plus bas": -24.0,
                     "c'est l'epsilon de float16 ; tiny est le plus petit nombre positif normal": -10.0})
wbm.record("M05a.23d", -307.6526555686, decimals=2,
           mistakes={"tiny est le plus petit flottant normal ; les nombres « sous-normaux » descendent plus bas":
                         -323.3062153431,
                     "log₁₀, pas ln : log₁₀ x = ln x / ln 10": -708.3964185322})
wbm.record("M05a.23e", True,
           mistakes={"np.nextafter(1.0, 2.0) est le flottant qui suit 1 : relis la définition de l'epsilon": False})
wbm.record("M05a.23f", 1.3439875, decimals=5,
           mistakes={"la question demande la valeur du polynôme d'ordre 4, pas celle de la fonction": 1.3438252437})''',
    note="a) $\\tan x = x + \\frac{x^3}{3} + \\frac{2x^5}{15} + O(x^7)$. b) $\\sqrt{1 + x} = 1 + \\frac{x}{2} - "
         "\\frac{x^2}{8} + \\frac{x^3}{16} + \\cdots$. c) `float16` n'a que 5 bits d'exposant : son plus petit normal vaut "
         "$2^{-14} \\approx 6{,}1 \\times 10^{-5}$ et son plus grand $(2 - 2^{-10}) \\times 2^{15} = 65\\,504$, d'où les "
         "débordements et les effacements faciles en demi-précision. d) `tiny` vaut "
         "environ $2{,}2 \\times 10^{-308}$ ; en dessous, les nombres « sous-normaux » perdent peu à peu leurs chiffres, "
         "jusqu'à environ $4{,}9 \\times 10^{-324}$. f) Les dérivées valent $1, 1, 1, 0, -3$ : $1 + 0{,}3 + 0{,}045 - "
         "\\frac{3 \\times 0{,}3^4}{24} \\approx 1{,}34399$, contre $e^{\\sin 0{,}3} \\approx 1{,}34383$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M05a.24 to M05a.26)
# ---------------------------------------------------------------------------
M05A_24_EXPERIMENT = '''def iterates(f, fprime, x0, steps):
    """The first values of Newton's sequence from x0 (it stops early on a horizontal tangent)."""
    values = [x0]
    for _ in range(steps):
        x = values[-1]
        slope = fprime(x)
        if slope == 0:
            break
        values.append(x - f(x) / slope)
    return values


def signed_cube_root(x):
    return math.copysign(abs(x) ** (1 / 3), x)


def arctan_slope(x):
    return 1 / (1 + x * x)


print("a) arctan from 1:      ", [round(v, 5) for v in iterates(math.atan, arctan_slope, 1.0, 6)])
print("b) arctan from 1.5:    ", [round(v, 2) for v in iterates(math.atan, arctan_slope, 1.5, 5)])
print("c) x³ − 2x + 2 from 0: ", iterates(lambda x: x ** 3 - 2 * x + 2, lambda x: 3 * x ** 2 - 2, 0.0, 6))
print("d) cube root from 1:   ", [round(v, 3) for v in iterates(signed_cube_root, lambda x: abs(x) ** (-2 / 3) / 3,
                                                               1.0, 6)])
print("e) x² from 1:          ", iterates(lambda x: x * x, lambda x: 2 * x, 1.0, 8))'''

M05A_24 = Ex(
    "M05a.24", "🔮", 1, 10, "Prédire : Newton depuis un mauvais point de départ",
    "prévoir le comportement de la méthode de Newton selon la fonction et le point de départ, puis le vérifier.",
    "fiche §4", tracks="C", hypothesis=True,
    body="""On applique la méthode de Newton (sans critère d'arrêt, quelques pas) à cinq cas. Pour a), b) et c), choisis : (1) la suite converge vers une racine ; (2) elle s'éloigne de plus en plus ; (3) elle alterne entre deux valeurs, sans fin ; (4) elle s'arrête : la tangente est horizontale.
- a) $f(x) = \\arctan x$ (sa seule racine est 0, et $f'(x) = \\frac{1}{1 + x^2}$), depuis $x_0 = 1$ ;
- b) la même fonction, depuis $x_0 = 1{,}5$ ;
- c) $f(x) = x^3 - 2x + 2$, depuis $x_0 = 0$.

Pour d) et e), choisis : (1) la suite converge vers 0, le nombre de décimales justes doublant à chaque pas ; (2) elle converge vers 0, l'erreur divisée par 2 à chaque pas ; (3) elle s'éloigne de 0, la distance doublant à chaque pas ; (4) elle alterne entre 1 et $-1$.
- d) $f(x) = \\sqrt[3]{x}$, la racine cubique (négative pour $x < 0$), depuis $x_0 = 1$ ;
- e) $f(x) = x^2$ (une racine double en 0), depuis $x_0 = 1$.

**Avant d'exécuter quoi que ce soit**, écris tes cinq prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M05a_24a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M05a_24b = ...  # b) 1, 2, 3 or 4
prediction_M05a_24c = ...  # c) 1, 2, 3 or 4
prediction_M05a_24d = ...  # d) 1, 2, 3 or 4
prediction_M05a_24e = ...  # e) 1, 2, 3 or 4''',
    check='''for letter, prediction in zip("abcde", [prediction_M05a_24a, prediction_M05a_24b, prediction_M05a_24c,
                                       prediction_M05a_24d, prediction_M05a_24e]):
    wbm.check(f"M05a.24{letter}", prediction)''',
    record='''wbm.record("M05a.24a", 1, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M05a.24b", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M05a.24c", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M05a.24d", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M05a.24e", 2, prediction=True, choices=[1, 2, 3, 4])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes cinq prédictions écrites."),
        ("todo", guarded(M05A_24_EXPERIMENT, ["prediction_M05a_24a", "prediction_M05a_24b", "prediction_M05a_24c",
                                               "prediction_M05a_24d", "prediction_M05a_24e"],
                         "⏳ Écris d'abord tes cinq prédictions, puis exécute à nouveau.")),
        ("solution", M05A_24_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : pour a) et b), dessine la courbe de $\\arctan$ et deux "
               "tangentes : pourquoi la tangente en 1,5 renvoie-t-elle plus loin de l'autre côté ? Pour c), fais les "
               "deux pas à la main. Pour d), montre que le pas de Newton vaut $x_{k+1} = -2x_k$. Pour e), montre que "
               "$x_{k+1} = \\frac{x_k}{2}$ : pourquoi la racine double fait-elle perdre la convergence quadratique "
               "(fiche §4) ?"),
    ],
    note="a) Depuis 1, la tangente coupe l'axe en $-0{,}57$, puis $0{,}12$, $-0{,}001$… : la suite converge vers 0, "
         "très vite. b) Depuis 1,5, la courbe est déjà aplatie : la tangente renvoie en $-1{,}69$, puis $2{,}32$, "
         "$-5{,}11$, $32{,}3$… : la suite s'éloigne. Le seuil se situe vers 1,39. c) $0 \\to 1 \\to 0 \\to 1 \\ldots$ : un "
         "cycle de période 2. d) $\\frac{f(x)}{f'(x)} = 3x$, donc $x_{k+1} = -2x_k$ : la tangente d'une courbe presque "
         "verticale en 0 renvoie toujours plus loin. e) $x_{k+1} = x_k - \\frac{x_k^2}{2x_k} = \\frac{x_k}{2}$ : en une "
         "racine double, $f'$ s'annule aussi, et la convergence devient linéaire (fiche §4).",
)

M05A_25_CHECK = '''with checked("M05a.25a"):
    wbm.check("M05a.25a", abs(log1p_taylor(0.5, 5) - math.log1p(0.5)), computed=True)
with checked("M05a.25b"):
    wbm.check("M05a.25b", abs(log1p_taylor(0.5, 20) - math.log1p(0.5)) * 1e8, computed=True)
with checked("M05a.25c"):
    wbm.check("M05a.25c", abs(log1p_taylor(1.5, 5) - math.log1p(1.5)), computed=True)
with checked("M05a.25d"):
    wbm.check("M05a.25d", abs(log1p_taylor(1.5, 20) - math.log1p(1.5)), computed=True)
with checked("M05a.25e"):
    wbm.check("M05a.25e", next((n for n in range(1, 1001) if abs(log1p_taylor(0.9, n) - math.log1p(0.9)) < 1e-3), -1),
              computed=True)
with checked("M05a.25f"):
    wbm.check("M05a.25f", abs(log1p_taylor(1.0, 100) - math.log(2)), computed=True)'''

M05A_25_FIGURE = '''with checked("M05a.25 figure"):
    ns_25 = range(1, 41)
    errors_25 = {x0: [abs(log1p_taylor(x0, n) - math.log1p(x0)) for n in ns_25] for x0 in (0.5, 0.9, 1.0, 1.5)}
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    for x0, errors in errors_25.items():
        ax.semilogy(ns_25, errors, marker=".", label=f"x = {x0}")
    ax.set(xlabel="n (nombre de termes)", ylabel="erreur", title="ln(1 + x) et son polynôme de Taylor d'ordre n")
    ax.legend()
    plt.show()'''

M05A_25 = Ex(
    "M05a.25", "🔬", 2, 20, "Taylor de plus en plus loin : où le polynôme décroche",
    "mesurer l'erreur du polynôme de Taylor de $\\ln(1 + x)$ selon le nombre de termes et le point, et voir où la "
    "série cesse de converger.", "fiche §3", tracks="C",
    body="""La fiche (§3) annonce que $\\ln(1 + x) = x - \\frac{x^2}{2} + \\frac{x^3}{3} - \\cdots$ seulement pour $-1 < x \\le 1$. Vérifie-le.

Écris `log1p_taylor(x, n)`, qui renvoie le polynôme de Taylor d'ordre $n$ de $\\ln(1 + x)$ en 0, évalué en $x$ : $\\sum_{k=1}^{n} \\frac{(-1)^{k+1} x^k}{k}$ ($n$ termes, en `float`).

La vérification compare ta fonction à `math.log1p(x)`, qui calcule $\\ln(1 + x)$, et calcule :
- a) l'erreur (la valeur absolue de l'écart) pour $x = 0{,}5$ et $n = 5$ (6 décimales) ;
- b) l'erreur pour $x = 0{,}5$ et $n = 20$, multipliée par $10^8$ (2 décimales) ;
- c) l'erreur pour $x = 1{,}5$ et $n = 5$ (4 décimales) ;
- d) l'erreur pour $x = 1{,}5$ et $n = 20$ (1 décimale) ;
- e) le plus petit $n$ pour lequel l'erreur en $x = 0{,}9$ passe sous $10^{-3}$ (un entier) ;
- f) l'erreur pour $x = 1$ et $n = 100$ (6 décimales).

Une dernière cellule trace l'erreur en fonction de $n$ pour quatre points, sur une échelle logarithmique.

Dans ta copie : comment l'erreur évolue-t-elle avec $n$ pour chaque point ? Pour $|x| < 1$, compare l'erreur au premier terme négligé, $\\frac{|x|^{n+1}}{n+1}$. Pourquoi la série ne peut-elle pas converger pour $x = 1{,}5$ (regarde la taille du terme $\\frac{x^k}{k}$) ? Combien de termes faudrait-il, en $x = 1$, pour une erreur de $10^{-6}$ ?""",
    todo='''def log1p_taylor(x, n):
    """The Taylor polynomial of order n of ln(1 + x) at 0, evaluated at x: the sum of (-1)**(k+1) x**k / k for k
    from 1 to n."""
    raise NotImplementedError("une boucle sur k de 1 à n, ou sum(...)")''',
    check=M05A_25_CHECK,
    solution='''def log1p_taylor(x, n):
    """The Taylor polynomial of order n of ln(1 + x) at 0, evaluated at x: the sum of (-1)**(k+1) x**k / k for k
    from 1 to n."""
    return float(sum((-1) ** (k + 1) * x ** k / k for k in range(1, n + 1)))


for x0, n in [(0.5, 5), (0.5, 20), (1.5, 5), (1.5, 20), (1.0, 100)]:
    error = abs(log1p_taylor(x0, n) - math.log1p(x0))
    print(f"x = {x0}, n = {n}: error {error:.6g} · first term left out {abs(x0) ** (n + 1) / (n + 1):.6g}")
print("e)", next(n for n in range(1, 1001) if abs(log1p_taylor(0.9, n) - math.log1p(0.9)) < 1e-3))''',
    record='''wbm.record("M05a.25a", 0.0018265586, decimals=6,
           mistakes={"les signes alternent : (−1)^(k+1)": 0.2830765586,
                     "n termes : k va de 1 à n inclus, range(1, n + 1)": 0.0044234414})
wbm.record("M05a.25b", 1.5373987361, decimals=2,
           mistakes={"n termes : k va de 1 à n inclus, range(1, n + 1)": 3.2309728448})
wbm.record("M05a.25c", 0.8368342681, decimals=4,
           mistakes={"les signes alternent : (−1)^(k+1)": 5.6180842681,
                     "n termes : k va de 1 à n inclus, range(1, n + 1)": 0.6819157319})
wbm.record("M05a.25d", 97.7448750532, decimals=1,
           mistakes={"n termes : k va de 1 à n inclus, range(1, n + 1)": 68.5179614508})
wbm.record("M05a.25e", 28,
           mistakes={"n termes : k va de 1 à n inclus, range(1, n + 1)": 29})
wbm.record("M05a.25f", 0.0049750012, decimals=6,
           mistakes={"n termes : k va de 1 à n inclus, range(1, n + 1)": 0.0050249988})''',
    after=[("md", "**La figure** (elle utilise ta fonction)."),
           ("code", M05A_25_FIGURE)],
    note="Pour $0 < x < 1$, l'erreur décroît comme le premier terme négligé, $\\frac{|x|^{n+1}}{n+1}$ (une série alternée "
         "dont les termes décroissent : l'erreur est plus petite que le premier terme négligé) : 15 termes de plus "
         "gagnent 5 décimales en 0,5, mais il en faut 28 en 0,9. En $x = 1$, l'erreur ne décroît que comme "
         "$\\frac{1}{2n}$ environ : $0{,}005$ pour 100 termes, et il faudrait environ 500 000 termes pour $10^{-6}$. En "
         "$x = 1{,}5$, le terme $\\frac{1{,}5^k}{k}$ grandit sans limite : chaque terme ajouté éloigne davantage la "
         "somme, qui oscille de plus en plus fort (97,7 pour 20 termes).",
)

M05A_26_CHECK = '''with checked("M05a.26 vérifications"):
    problems = []
    a_t = 0.5                                                          # another example: exp at 0.5, orders 1 and 3
    ders_t = [math.exp(a_t)] * 4

    def poly_t(order, xs):
        return sum(ders_t[k] * (xs - a_t) ** k / math.factorial(k) for k in range(order + 1))

    expected = {"la fonction": np.exp, "le polynôme d'ordre 1": lambda xs: poly_t(1, xs),
                "le polynôme d'ordre 3": lambda xs: poly_t(3, xs)}
    fig, ax = plt.subplots(figsize=(6, 4))
    try:
        created = drawn(draw_taylor, ax, np.exp, ders_t, a_t, (1, 3))
    finally:
        plt.close(fig)                                                 # only the checks below are shown here
    if created:
        problems.append("draw_taylor ouvre sa propre figure : dessine dans l'axe reçu")
    else:
        curves = []
        for line in ax.get_lines():
            xs = np.asarray(line.get_xdata(), dtype=float)
            ys = np.asarray(line.get_ydata(), dtype=float)
            if xs.size >= 50:
                curves.append((line, xs, ys))
        for name, function in expected.items():
            match = [line for line, xs, ys in curves if np.allclose(ys, function(xs), rtol=1e-6, atol=1e-9)]
            if not match:
                problems.append(f"aucune courbe d'au moins 50 points n'est {name}" + (
                    "" if name == "la fonction" else " (le terme d'ordre k est f⁽ᵏ⁾(a) (x − a)^k / k!, pour k de 0 "
                                                     "à l'ordre)"))
            elif not match[0].get_label() or match[0].get_label().startswith("_"):
                problems.append(f"{name} : donne-lui un label, pour la légende")
        if curves and max(xs.max() - xs.min() for _, xs, _ in curves) < 3.9:
            problems.append("trace les courbes sur tout l'intervalle [a − 2, a + 2]")
        marked = any(np.any(np.isclose(np.asarray(line.get_xdata(), dtype=float), a_t))
                     and np.any(np.isclose(np.asarray(line.get_ydata(), dtype=float), math.exp(a_t)))
                     and len(line.get_xdata()) < 5 for line in ax.get_lines())
        marked = marked or any(np.any(np.all(np.isclose(c.get_offsets(), [a_t, math.exp(a_t)]), axis=1))
                               for c in ax.collections if len(c.get_offsets()))
        if not marked:
            problems.append("marque le point (a, f(a)) par un point, par exemple ax.plot(a, f(a), \\"o\\")")
        if ax.get_legend() is None:
            problems.append("il manque la légende (ax.legend())")
    if problems:
        print("❌ Ex M05a.26 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M05a.26 : la fonction, ses polynômes de Taylor et le point de contact sont justes, avec une "
              "légende.")'''

M05A_26 = Ex(
    "M05a.26", "🎨", 1, 20, "Une fonction et ses polynômes de Taylor d'ordre 1, 2 et 3",
    "tracer une fonction et ses polynômes de Taylor en un point, et voir l'approximation s'améliorer près du point "
    "et se dégrader loin de lui.", "fiche §3 ; Ex M05a.18 ; R0 (matplotlib)", tracks="C, E",
    body="""Écris `draw_taylor(ax, f, derivatives, a, orders)`, qui dessine dans l'axe `ax`, sur une grille d'au moins 200 points de $[a - 2, a + 2]$ :
- la fonction `f` (une fonction qui accepte un array, comme `np.sin`) ;
- pour chaque ordre $n$ de `orders`, le polynôme de Taylor d'ordre $n$ en `a`, construit avec les $n + 1$ premières valeurs de `derivatives` ($[f(a), f'(a), \\ldots]$) ;
- le point de contact $(a, f(a))$, marqué par un point ;

chaque courbe avec un label, puis la légende. Ta fonction `mymath.approx.taylor_polynomial` donne la valeur d'un polynôme en un point (une compréhension de liste la calcule sur toute la grille), ou bien une somme de termes sur un array.

Puis trace $\\sin$ et ses polynômes d'ordre 1, 2 et 3 en $a = \\frac{\\pi}{4}$, dont les dérivées valent $\\frac{\\sqrt{2}}{2}, \\frac{\\sqrt{2}}{2}, -\\frac{\\sqrt{2}}{2}, -\\frac{\\sqrt{2}}{2}$.

Dans ta copie : sur quelle largeur autour de $\\frac{\\pi}{4}$ chaque polynôme reste-t-il proche de la courbe, à l'œil ? La tangente (l'ordre 1) est-elle au-dessus ou au-dessous de la courbe près de $\\frac{\\pi}{4}$, et pourquoi (signe de $f''$, §1) ? Et le polynôme d'ordre 2 : de quel côté de la courbe est-il juste à gauche de $\\frac{\\pi}{4}$, puis juste à droite (regarde le premier terme négligé, en $(x - a)^3$) ? Pourquoi chaque ordre de plus améliore-t-il l'approximation près de $a$ et pas forcément loin de $a$ ?""",
    todo='''def draw_taylor(ax, f, derivatives, a, orders):
    """In ax, on [a - 2, a + 2]: f, its Taylor polynomials at a of the given orders (from derivatives = [f(a), f'(a),
    ...]) and the point (a, f(a)), each with a label; then the legend."""
    raise NotImplementedError("une grille, ax.plot pour f puis pour chaque ordre, le point (a, f(a)), ax.legend()")''',
    check='''with checked("M05a.26 figure"):
    fig, ax = plt.subplots(figsize=(7, 4))
    root_half = math.sqrt(2) / 2
    try:
        created = drawn(draw_taylor, ax, np.sin, [root_half, root_half, -root_half, -root_half], math.pi / 4,
                        (1, 2, 3))
    except BaseException:
        plt.close(fig)                                     # no empty figure while the function is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M05a.26 : draw_taylor ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans l'axe reçu.")
    else:
        plt.show()''',
    solution='''def draw_taylor(ax, f, derivatives, a, orders):
    """In ax, on [a - 2, a + 2]: f, its Taylor polynomials at a of the given orders (from derivatives = [f(a), f'(a),
    ...]) and the point (a, f(a)), each with a label; then the legend."""
    xs = np.linspace(a - 2, a + 2, 401)
    ax.plot(xs, f(xs), color="black", linewidth=2.5, label="la fonction")
    for order in orders:
        values = [mymath.approx.taylor_polynomial(derivatives[:order + 1], a, x) for x in xs]
        ax.plot(xs, values, linewidth=1.6, label=f"Taylor d'ordre {order}")
    ax.plot(a, f(a), "o", color="black", label="(a, f(a))")
    ax.set(xlabel="x", ylim=(-2, 2), title="Une fonction et ses polynômes de Taylor en a")
    ax.legend(fontsize=8)


fig, ax = plt.subplots(figsize=(7, 4))
root_half = math.sqrt(2) / 2
draw_taylor(ax, np.sin, [root_half, root_half, -root_half, -root_half], math.pi / 4, (1, 2, 3))
plt.show()''',
    after=[("md", "**Vérifications automatiques** (sur un autre exemple ; la figure elle-même se juge à l'œil)."),
           ("code", M05A_26_CHECK)],
    note="Près de $\\frac{\\pi}{4}$, les trois polynômes collent à la courbe, et chaque ordre de plus élargit la zone où "
         "l'écart reste invisible (environ $\\pm 0{,}3$, $\\pm 0{,}6$ et $\\pm 1$ à l'œil). La tangente est au-dessus "
         "de la courbe : $\\sin'' = -\\sin < 0$ près de $\\frac{\\pi}{4}$, la courbe y est concave (§1). Le polynôme "
         "d'ordre 2, lui, traverse la courbe en $\\frac{\\pi}{4}$ : $\\sin x - P_2(x)$ commence par le terme "
         "$-\\frac{\\sqrt{2}}{12}(x - a)^3$, positif à gauche de $a$ (le polynôme est au-dessous) et négatif à droite "
         "(il est au-dessus). Loin de $a$, chaque polynôme part "
         "vers l'infini (un polynôme non constant n'est pas borné), alors que $\\sin$ reste entre $-1$ et 1 : Taylor "
         "est une approximation **locale**.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M05a.27 to M05a.29)
# ---------------------------------------------------------------------------
M05A_27_MISTAKES = bug_letters_mistakes(
    "ACEF", "BD",
    {"A": "vérifie quel score chaque ligne retire avant de prendre l'exponentielle",
     "C": "vérifie que chaque log-sum-exp revient à l'échelle des scores",
     "E": "vérifie que chaque calcul reste représentable en float64 à chaque étape",
     "F": "vérifie ce que somme chaque ligne, et par quoi elle divise"},
    name_correct=False)

M05A_27 = Ex(
    "M05a.27", "🐛", 1, 15, "Chasse à l'erreur : une softmax qui renvoie `nan`",
    "repérer dans du code les erreurs classiques d'une softmax et d'un log-sum-exp, de formule ou de calcul en "
    "flottants, puis calculer les bonnes valeurs.", "fiche §6 et §8 ; Ex M05a.10", tracks="C",
    body="""Un modèle donne trois scores $\\mathbf{v} = (1000,\\ 999,\\ 200)$. Une collègue a écrit six lignes, chacune avec un commentaire qui dit ce qu'elle veut calculer ; chaque ligne utilise les variables des lignes précédentes telles qu'elles **devraient** être (on suppose les lignes précédentes justes). Quatre lignes ne calculent pas ce que dit leur commentaire : une erreur de formule, ou un calcul qui échoue en `float64`. **Sans exécuter de code**, trouve-les.

```python
v = [1000.0, 999.0, 200.0]
m = min(v)                                        # (A) the largest score
total = sum(math.exp(x - m) for x in v)           # (B) Σ exp(v_i − m), with m the largest score
lse = math.log(total)                             # (C) log-sum-exp of v
p1 = math.exp(v[0] - m) / total                   # (D) softmax(v)[0]
log_p3 = math.log(math.exp(v[2] - m) / total)     # (E) log-softmax of the third score
s = sum(math.exp(x - m) for x in v) / len(v)      # (F) the sum of the three probabilities of softmax(v)
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire (une liste de 6 nombres, 3 décimales).

Dans ta copie : pour chaque ligne fausse, quelle erreur a été faite, et comment la corriger ? Laquelle donne une erreur à l'exécution plutôt qu'une valeur fausse ? D'où peut venir le `nan` du titre (pense à `inf / inf` en NumPy) ?""",
    todo='''answer_M05a_27a = ...  # a) letters, as text
answer_M05a_27b = ...  # b) a list of 6 values (3 decimals)''',
    check='''wbm.check("M05a.27a", answer_M05a_27a)
wbm.check("M05a.27b", answer_M05a_27b)''',
    solution='''answer_M05a_27a = "ACEF"
v = [1000.0, 999.0, 200.0]
m = max(v)                                              # (A) the largest score
total = sum(math.exp(x - m) for x in v)                 # (B) correct
lse = m + math.log(total)                               # (C) add m back
p1 = math.exp(v[0] - m) / total                         # (D) correct
log_p3 = v[2] - lse                                     # (E) exp(-800) underflows to 0: use v_i − LSE
s = sum(math.exp(x - m) / total for x in v)             # (F) divide by the total, not by n
answer_M05a_27b = [m, total, lse, p1, log_p3, s]
print(answer_M05a_27a, [round(value, 4) for value in answer_M05a_27b])
with np.errstate(over="ignore"):                       # NumPy warns of the overflow; the warning is hidden here
    print("exp(-800):", math.exp(-800), "· in NumPy, exp(800):", np.exp(np.float64(800)))''',
    record=f'''wbm.record("M05a.27a", "ACEF",
           mistakes={M05A_27_MISTAKES})
wbm.record("M05a.27b", [1000, 1.3678794412, 1000.3132616875, 0.7310585786, -800.3132616875, 1.0], decimals=3,
           mistakes={{"(C) : le log-sum-exp de v rajoute le maximum m": [1000, 1.3678794412, 0.3132616875,
                                                                        0.7310585786, -800.3132616875, 1.0],
                     "(E) : le log-softmax est v₃ − LSE(v), et LSE(v) n'est pas le seul maximum":
                         [1000, 1.3678794412, 1000.3132616875, 0.7310585786, -800.0, 1.0]}})''',
    note="(A) Il faut retirer le **maximum** : avec le minimum, `math.exp(1000 - 200)` lève une `OverflowError` (en "
         "NumPy, il donne `inf`, puis `inf / inf` donne `nan`). (C) Le log-sum-exp est $m + \\ln(\\text{total})$, "
         "environ 1 000,313. (E) La formule est juste sur le papier, mais $e^{-800}$ s'efface en `float64` (il est "
         "plus petit que $5 \\times 10^{-324}$) : la ligne calcule `math.log(0.0)` et lève une `ValueError`. Le "
         "log-softmax se calcule directement, $v_3 - \\text{LSE}(\\mathbf{v}) \\approx -800{,}313$ (M05a.14). (F) La "
         "somme des probabilités divise chaque exponentielle par le total, pas par $n$ : elle vaut 1. Les lignes (B) "
         "et (D) sont justes.",
)

M05A_28_CHECK = '''with checked("M05a.28 vérifications"):
    problems = []
    cases = [((1.0, 1.0 + 1e-10), {}), ((1e20, 1e20 + 1e5), {}), ((1e-20, 2e-20), {}), ((0.0, 1e-12), {}),
             ((0.0, 1e-12), {"abs_tol": 1e-9}), ((100.0, 101.0), {"rel_tol": 0.01}),
             ((100.0, 102.0), {"rel_tol": 0.01}), ((1.0, 1.1), {"rel_tol": 0.091}), ((1.1, 1.0), {"rel_tol": 0.091}),
             ((5.0, 5.0), {"rel_tol": 0.0}), ((math.inf, math.inf), {}), ((math.inf, 1e308), {"rel_tol": 0.5}),
             ((math.nan, math.nan), {}), ((-3.0, 3.0), {"rel_tol": 2.5})]
    for (got, expected), options in cases:
        reference = math.isclose(got, expected, **options)
        call = f"close_enough({got!r}, {expected!r}" + "".join(f", {k}={v!r}" for k, v in options.items()) + ")"
        try:
            answer = close_enough(got, expected, **options)
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{call} lève {type(exc).__name__} ({exc}) ; attendu {reference}")
            continue
        if answer is not reference:
            problems.append(f"{call} : attendu {reference}, obtenu {answer!r}")
    for options in ({"rel_tol": -1e-9}, {"abs_tol": -1.0}):
        try:
            close_enough(1.0, 1.0, **options)
        except ValueError:
            pass
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"une tolérance négative ({options}) lève {type(exc).__name__} : attendu une ValueError")
        else:
            problems.append(f"une tolérance négative ({options}) est acceptée : attendu une ValueError")
    if problems:
        print("❌ Ex M05a.28 : à revoir : " + " ; ".join(problems[:5]) + ("…" if len(problems) > 5 else "."))
    else:
        print("✅ Ex M05a.28 : close_enough donne les mêmes réponses que math.isclose, cas limites compris.")'''

M05A_28 = Ex(
    "M05a.28", "🛠️", 1, 10, "Erreur relative ou absolue : choisir la tolérance d'un test",
    "écrire la comparaison de deux flottants qu'utilisent les tests, avec une tolérance relative et une tolérance "
    "absolue, et savoir laquelle choisir.", "fiche §6", tracks="C",
    body="""On ne compare jamais deux flottants calculés avec `==` : `0.1 + 0.2 == 0.3` est faux (R0). On vérifie qu'ils sont **proches**. Mais proches comment ?
- Une tolérance **absolue**, $|a - b| \\le 10^{-9}$, est absurde pour des nombres de l'ordre de $10^{20}$, où deux flottants voisins sont déjà distants de plus de 10 000 (§6).
- Une tolérance **relative**, $|a - b| \\le 10^{-9}\\,\\max(|a|, |b|)$, est absurde près de 0 : un résultat qui devrait valoir 0 et vaut $10^{-17}$ (une annulation, §6) n'est « proche » d'aucun nombre.

Les bibliothèques combinent donc les deux. Écris `close_enough(got, expected, rel_tol=1e-9, abs_tol=0.0)`, qui renvoie `True` si et seulement si

$$|\\text{got} - \\text{expected}| \\le \\max\\big(\\text{rel\\_tol} \\times \\max(|\\text{got}|, |\\text{expected}|),\\ \\text{abs\\_tol}\\big),$$

avec trois règles : deux valeurs égales (même infinies) sont proches ; `nan` n'est proche de rien, pas même de lui-même ; une infinie n'est proche que d'elle-même. Une tolérance négative lève une `ValueError`. C'est la définition de `math.isclose`, qui est donc interdite ici : la vérification compare tes réponses aux siennes, sur des cas choisis.

Dans ta copie : quelle tolérance choisirais-tu pour tester que `logsumexp([1000, 1000])` vaut $1000 + \\ln 2$ ? Pour tester qu'une erreur d'arrondi, qui devrait être nulle, est négligeable ? `numpy.isclose(a, b)` utilise $|a - b| \\le \\text{atol} + \\text{rtol}\\,|b|$, avec par défaut `atol=1e-8` : pourquoi n'est-elle pas symétrique, et quel piège cache son `atol` pour de très petits nombres ?""",
    todo='''def close_enough(got, expected, rel_tol=1e-9, abs_tol=0.0):
    """True when |got - expected| <= max(rel_tol * max(|got|, |expected|), abs_tol), like math.isclose (without
    using it). ValueError for a negative tolerance."""
    raise NotImplementedError("les tolérances, puis l'égalité, nan et les infinis, puis l'inégalité")''',
    solution='''def close_enough(got, expected, rel_tol=1e-9, abs_tol=0.0):
    """True when |got - expected| <= max(rel_tol * max(|got|, |expected|), abs_tol), like math.isclose (without
    using it). ValueError for a negative tolerance."""
    if rel_tol < 0 or abs_tol < 0:
        raise ValueError("the tolerances must be non-negative")
    if got == expected:                       # exact equality, infinities included
        return True
    if math.isinf(got) or math.isinf(expected) or math.isnan(got) or math.isnan(expected):
        return False                          # an infinity is close only to itself; nan to nothing
    return abs(got - expected) <= max(rel_tol * max(abs(got), abs(expected)), abs_tol)


print(close_enough(1e20, 1e20 + 1e5), close_enough(0.0, 1e-17), close_enough(0.0, 1e-17, abs_tol=1e-12))''',
    after=[("code", M05A_28_CHECK)],
    note="Pour `logsumexp([1000, 1000])`, une tolérance relative (par exemple $10^{-12}$) : le résultat est de l'ordre "
         "de 1 000, et l'erreur d'arrondi lui est proportionnelle. Pour une valeur qui devrait être nulle, il faut une "
         "tolérance absolue, choisie selon l'échelle des nombres qui l'ont produite (par exemple $10^{-12}$ si l'on "
         "a soustrait des nombres de l'ordre de 1). `numpy.isclose(a, b)` multiplie `rtol` par $|b|$ seulement : "
         "`isclose(a, b)` et `isclose(b, a)` peuvent différer ; et son `atol=1e-8` par défaut déclare « proches » "
         "$10^{-10}$ et $10^{-20}$, deux nombres que rien ne rapproche : pour de petites grandeurs, il faut le "
         "baisser.",
)

M05A_29_DEFI = '''CASES_29 = [50.0, 2.0, 0.008, 1e-30, 3.7e25, 123456.789, 1e300, 5e-300, 0.9999, 7.0e-5, 1.0]
with checked("M05a.29 défi"):
    worst_error, worst_steps, failed = 0.0, 0, []
    for a in CASES_29:
        try:
            root, steps = cube_root(a)
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001 - reported below, case by case
            failed.append(f"cube_root({a!r}) lève {type(exc).__name__} ({exc})")
            continue
        exact = float(np.cbrt(a))                      # the cube root to the last bit (a ** (1/3) loses 1e-14)
        worst_error = max(worst_error, abs(root - exact) / exact)
        worst_steps = max(worst_steps, steps)
    if failed:
        print("❌ Ex M05a.29 : " + " ; ".join(failed[:3]) + ". Pour un nombre extrême, x * x peut s'effacer à 0 ou "
              "déborder quand x est loin de la racine : un point de départ proche de la racine (math.frexp) évite ces "
              "valeurs, sans test particulier.")
    elif not worst_error < 1e-12:
        print(f"Pire erreur relative : {worst_error:.1e} · pire nombre d'itérations : {worst_steps}")
        print("❌ Ex M05a.29 : la précision n'est pas atteinte (objectif : erreur relative < 1e-12) : continue les pas "
              "de Newton jusqu'à ce que deux valeurs successives soient presque égales.")
    elif worst_steps > 6:
        print(f"Pire erreur relative : {worst_error:.1e} · pire nombre d'itérations : {worst_steps}")
        print("❌ Ex M05a.29 : précision atteinte, mais trop d'itérations (objectif : 6 au plus) : soigne le point de "
              "départ (math.frexp).")
    else:
        print(f"Pire erreur relative : {worst_error:.1e} · pire nombre d'itérations : {worst_steps}")
        print("✅ Ex M05a.29 : défi réussi, une précision de 1e-12 en 6 itérations au plus, de 1e-300 à 1e300.")'''

M05A_29_CHECK = M05A_29_DEFI + '''
with checked("M05a.29"):
    wbm.check("M05a.29", cube_root(50.0)[0], computed=True)'''

M05A_29 = Ex(
    "M05a.29", "🏆", 3, 25, "Défi : une racine cubique à 10⁻¹² en le moins d'itérations possible",
    "programmer une racine cubique par la méthode de Newton, avec un point de départ assez bon pour converger en "
    "quelques pas, quelle que soit la taille du nombre.", "fiche §4 et §6 ; Ex M05a.12 et M05a.19", tracks="C",
    body="""Écris `cube_root(a)`, qui renvoie le couple `(x, steps)` : une approximation de $\\sqrt[3]{a}$ pour $a > 0$, obtenue par la méthode de Newton sur $f(x) = x^3 - a$, et le nombre de pas de Newton effectués. Un pas s'écrit $x \\leftarrow x - \\frac{x^3 - a}{3x^2} = \\frac{1}{3}\\big(2x + \\frac{a}{x^2}\\big)$. Arrête-toi quand deux valeurs successives sont presque égales (par exemple $|x_{k+1} - x_k| \\le 10^{-15}\\,x_{k+1}$).

**L'objectif** : une erreur relative inférieure à $10^{-12}$ en **6 pas au plus**, pour des nombres de $10^{-300}$ à $10^{300}$. Tout se joue au point de départ : la convergence quadratique (M05a.12) n'opère que près de la racine, et partir de $x_0 = a$ ou de $x_0 = 1$ coûte plus de cent pas pour $a = 10^{30}$. Une piste : `m, e = math.frexp(a)` écrit $a = m \\times 2^e$ avec $0{,}5 \\le m < 1$ ; avec $e = 3q + r$ (`divmod(e, 3)`), $\\sqrt[3]{a} = \\sqrt[3]{m \\times 2^r} \\times 2^q$, et il ne reste qu'à approcher $\\sqrt[3]{y}$ pour $y = m \\times 2^r$ entre 0,5 et 4, par exemple par une droite.

La vérification calcule ta racine pour onze nombres, de $5 \\times 10^{-300}$ à $10^{300}$, affiche la pire erreur relative (mesurée par rapport à `np.cbrt`, la racine cubique de NumPy) et le pire nombre de pas, puis vérifie `cube_root(50.0)[0]` (10 décimales).

Dans ta copie : l'erreur relative de ton point de départ, au pire ? Combien de pas faut-il alors, d'après $\\varepsilon_{k+1} \\approx \\varepsilon_k^2$ (pour $x^3 - a$, l'erreur relative est à peu près élevée au carré à chaque pas) ? Pourquoi, depuis $x_0 = 1$ et pour $a = 10^{30}$, la suite ne fait-elle que se multiplier par environ $\\frac{2}{3}$ pendant des dizaines de pas ?""",
    todo='''def cube_root(a):
    """The cube root of a > 0 by Newton's method on x**3 - a, and the number of Newton steps taken: (x, steps)."""
    raise NotImplementedError("un bon point de départ (math.frexp), puis des pas de Newton jusqu'à l'arrêt")''',
    check=M05A_29_CHECK,
    solution='''ROOTS_OF_2 = (1.0, 2 ** (1 / 3), 2 ** (2 / 3))           # cube roots of 2**r for r = 0, 1, 2


def cube_root(a):
    """The cube root of a > 0 by Newton's method on x**3 - a, and the number of Newton steps taken: (x, steps)."""
    if not a > 0:
        raise ValueError(f"a must be positive, got {a!r}")
    m, e = math.frexp(a)                       # a = m × 2**e with 0.5 <= m < 1
    q, r = divmod(e, 3)                        # 2**e = 2**(3q) × 2**r
    x = (0.6 + 0.4 * m) * ROOTS_OF_2[r] * 2.0 ** q    # 0.6 + 0.4 m is within 1 % of the cube root of m
    for steps in range(1, 51):
        x_new = (2 * x + a / (x * x)) / 3
        if abs(x_new - x) <= 1e-15 * x_new:
            return x_new, steps
        x = x_new
    raise RuntimeError("no convergence after 50 steps")


def steps_from(a, x):
    """The number of Newton steps from the starting point x (the naive start)."""
    for steps in range(1, 1001):
        x_new = (2 * x + a / (x * x)) / 3
        if abs(x_new - x) <= 1e-15 * x_new:
            return steps
        x = x_new


print("cube_root(50):", cube_root(50.0), "· np.cbrt(50):", float(np.cbrt(50.0)))
print("steps from x0 = 1 for a = 1e30:", steps_from(1e30, 1.0), "· with the good start:", cube_root(1e30)[1])''',
    after=[("solution", M05A_29_DEFI)],
    record='''wbm.record("M05a.29", 3.6840314986, decimals=10)''',
    note="Avec $x_0 = (0{,}6 + 0{,}4\\,m) \\times 2^{r/3} \\times 2^q$, l'erreur relative de départ reste sous 1 % "
         "($0{,}6 + 0{,}4\\,m$ approche $\\sqrt[3]{m}$ à 0,9 % près sur $[0{,}5 ;\\ 1[$). Les pas donnent alors environ "
         "$10^{-4}$, $10^{-8}$, $10^{-16}$ : trois pas suffisent, plus un quatrième qui constate que la valeur ne bouge "
         "plus. Depuis $x_0 = 1$ pour $a = 10^{30}$, il faut 118 pas : tant que $x^3 \\gg a$, le pas vaut à peu près "
         "$x \\leftarrow \\frac{2x}{3}$, une décroissance géométrique lente, et la convergence quadratique ne commence "
         "qu'une fois arrivé près de $10^{10}$.",
)


PART_A = Part("A", "Ta librairie : Taylor, Newton, Richardson, epsilon machine et log-sum-exp",
              "Fiche §3 à §8. Les cinq fonctions de `mymath/approx.py`, puis SymPy `series` et `numpy.finfo`.",
              given=TOOLS, exercises=[M05A_18, M05A_19, M05A_20, M05A_21, M05A_22, M05A_23])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §3 et §4. Newton depuis de mauvais points de départ, le domaine de convergence d'une série de "
              "Taylor, une fonction et ses polynômes de Taylor.",
              exercises=[M05A_24, M05A_25, M05A_26])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §4, §6 et §8. Quatre erreurs d'une softmax à trouver, la tolérance d'un test de flottants, puis "
              "une racine cubique en quelques pas.",
              exercises=[M05A_27, M05A_28, M05A_29])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M05a.1 à M05a.10, M05a.14 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M05a · Dérivées, Taylor et calcul numérique — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m05a_derivees_taylor/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M05a`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M05a · Dérivées, Taylor et calcul numérique — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : dérivée seconde et convexité, extrema, polynômes de Taylor "
               "et reste, méthode de Newton, erreur des différences finies, flottants, meilleur pas, log-sum-exp.\n"
               "- Écrire les cinq fonctions de `mymath/approx.py` et les tester, puis utiliser SymPy et "
               "`numpy.finfo`.\n"
               "- Prédire Newton depuis un mauvais départ, voir une série de Taylor décrocher, tracer des polynômes de "
               "Taylor, chasser les erreurs d'une softmax, comparer des flottants, calculer une racine cubique en "
               "quelques pas.\n\n"
               "**Rappel express.** $f'' \\ge 0$ : convexe ; $P_n(x) = \\sum_{k=0}^{n} \\frac{f^{(k)}(a)}{k!}(x - a)^k$, "
               "reste $\\le \\frac{M}{(n+1)!}|x - a|^{n+1}$ ; Newton : $x_{k+1} = x_k - \\frac{f(x_k)}{f'(x_k)}$ ; "
               "différence avant : erreur $\\approx \\frac{h}{2}f''$, centrée : $\\approx \\frac{h^2}{6}f'''$, "
               "Richardson : $\\frac{4D(h/2) - D(h)}{3}$ ; `float64` : $\\varepsilon = 2^{-52}$ ; "
               "$\\text{LSE}(\\mathbf{v}) = m + \\ln\\sum_i e^{v_i - m}$, $m = \\max_i v_i$, entre $m$ et $m + \\ln n$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu étudier la convexité d'une fonction et trouver ses extrema globaux sur un intervalle ?\n"
               "2. Sais-tu écrire un polynôme de Taylor, borner son erreur, et dire à quel ordre une différence finie "
               "approche une dérivée ?\n"
               "3. Sais-tu utiliser la méthode de Newton, et dire quand elle converge vite ?\n"
               "4. Sais-tu ce qu'un `float64` représente exactement, et calculer un log-sum-exp ou une softmax sans "
               "overflow ?\n\n"
               "**La suite** : le chapitre 5 de workbookIA (dérivées, différences finies, gradient), puis M05b, les "
               "fonctions de plusieurs variables et le gradient.")]


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
