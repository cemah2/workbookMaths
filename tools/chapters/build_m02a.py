#!/usr/bin/env python
"""Build the two notebooks of chapter M02a from a single source (used by Claude).

    python tools/chapters/build_m02a.py
    python tools/run_all_notebooks.py chapitres/m02a_integrales_densites/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m02a_integrales_densites/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M02a.1 to M02a.10, 🔗 M02a.13); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer nor the calculation that gives it. A primitive is
answered by an expression in x, checked up to a constant (kind="expr", up_to_constant=True); an exact value such as
√π/2 by text with sqrt and pi (kind="exact"); an irreducible fraction by text (kind="fraction", simplified=True).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M02a"
FOLDER = "chapitres/m02a_integrales_densites"

F = 'kind="fraction", simplified=True'
X = 'kind="exact"'
P = 'kind="expr", variables=("x",), up_to_constant=True'   # a primitive, up to a constant
E = 'kind="expr", variables=("x",)'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M02a.1", "Sommes de Riemann à la main : rectangles à gauche, à droite, au milieu", [
        ("a", "a number (1 decimal)", "(2 - 0) / 4",
         'decimals=1, mistakes={"h = (b − a)/n : la longueur de l\'intervalle divisée par le nombre de rectangles": '
         '{2, 0.2, 4}}'),
        ("b", "a number (2 decimals)", "0.5 * (8 + 3.375 + 1 + 0.125)",
         'decimals=2, mistakes={"à gauche : la hauteur se lit au début de chaque intervalle, x de 0 à 1,5": 2.25, '
         '"multiplie la somme des hauteurs par la largeur h des rectangles": 12.5}'),
        ("c", "a number (2 decimals)", "0.5 * (3.375 + 1 + 0.125 + 0)",
         'decimals=2, mistakes={"à droite : la hauteur se lit à la fin de chaque intervalle, x de 0,5 à 2": 6.25, '
         '"multiplie la somme des hauteurs par la largeur h des rectangles": 4.5}'),
        ("d", "a number (3 decimals)", "0.5 * (1.75 ** 3 + 1.25 ** 3 + 0.75 ** 3 + 0.25 ** 3)",
         'decimals=3, mistakes={"multiplie la somme des hauteurs par la largeur h des rectangles": 7.75, '
         '"c\'est l\'aire exacte ; la question demande la somme de Riemann au milieu, qui l\'approche": 4, '
         '"au milieu : les hauteurs se lisent aux milieux des intervalles, en 0,25, 0,75, 1,25 et 1,75": 4.25}'),
        ("e", "a number", "4",
         'mistakes={"L₄ − R₄, dans cet ordre : f est décroissante, la somme à gauche est la plus grande": -4, '
         '"L₄ et R₄ sont des aires : la différence des hauteurs se multiplie par la largeur h": 8}'),
        ("f", "a number (4 decimals)",
         "0.25 * sum((2 - 0.25 * i) ** 3 for i in range(8))",
         'decimals=4, mistakes={"multiplie la somme des huit hauteurs par la largeur h des rectangles": 20.25, '
         '"avec n = 8, le pas vaut 2/8 : les hauteurs se lisent en 0 ; 0,25 ; … ; 1,75": 6.25, '
         '"c\'est R₈ ; L₈ lit les hauteurs au début de chaque intervalle, de 0 à 1,75": 3.0625}'),
        ("g", "an integer", "160",
         'mistakes={"L_n − R_n = h (f(0) − f(2)), avec h = 2/n : la longueur de l\'intervalle compte": 80, '
         '"le plus petit entier n qui vérifie L_n − R_n ≤ 0,1 (inégalité large) : vérifie aussi l\'entier '
         'juste en dessous": 161, "l\'inégalité est L_n − R_n ≤ 0,1 : avec ce n, l\'écart est encore trop grand": '
         '159}'),
        ("h", "True or False", "True",
         'mistakes={"f décroît : chaque rectangle à gauche dépasse la courbe, chaque rectangle à droite est dessous": '
         'False}'),
    ]),

    Paper("M02a.2", "Primitives usuelles", [
        ("a", "an expression in x, as text", '"2*x**3 - 2*x**2 + 5*x"',
         P + ', mistakes={"c\'est la dérivée de la fonction : une primitive F vérifie F′ = f": "12*x - 4", '
         '"xⁿ a pour primitive xⁿ⁺¹/(n + 1) : divise par le nouvel exposant": "6*x**3 - 4*x**2 + 5*x"}'),
        ("b", "an expression in x, as text", '"-1/(2*x**2)"',
         P + ', mistakes={"x⁻³ a pour primitive x⁻²/(−2) : le signe vient de la division par −2": "1/(2*x**2)", '
         '"divise par le nouvel exposant, −2, pas par l\'ancien": "-1/(3*x**2)", '
         '"c\'est la dérivée de 1/x³ ; une primitive se dérive en 1/x³": "-3/x**4"}'),
        ("c", "an expression in x, as text", '"2*x**(3/2)/3"',
         P + ', mistakes={"√x = x^(1/2) a pour primitive x^(3/2) divisée par 3/2, donc multipliée par 2/3": '
         '"3*x**(3/2)/2", "c\'est la dérivée de √x ; une primitive se dérive en √x": "1/(2*sqrt(x))"}'),
        ("d", "an expression in x, as text", '"exp(3*x)/3"',
         P + ', mistakes={"la dérivée de e^(3x) vaut 3 e^(3x) : divise par 3": "exp(3*x)", '
         '"divise par 3, ne multiplie pas : dérive ta réponse pour vérifier": "3*exp(3*x)"}'),
        ("e", "an expression in x, as text", '"log(2*x + 1)/2"',
         P + ', mistakes={"la dérivée de ln(2x + 1) vaut 2/(2x + 1) : divise par 2": "log(2*x + 1)"}'),
        ("f", "an expression in x, as text", '"sin(2*x)/2"',
         P + ', mistakes={"la dérivée de sin vaut cos : une primitive de cos est sin, sans signe moins": '
         '"-sin(2*x)/2", "la dérivée de sin(2x) vaut 2 cos(2x) : divise par 2": "sin(2*x)"}'),
        ("g", "an expression in x, as text (with its constant)", '"x**3 + x - 2"',
         E + ', mistakes={"c\'est bien une primitive, mais pas celle qui vaut 0 en x = 1 : choisis la constante": '
         '"x**3 + x", "la constante se choisit pour que F(1) = 0 : vérifie son signe": "x**3 + x + 2"}'),
        ("h", "an expression in x, as text", '"4*log(x) - exp(-x)"',
         P + ', mistakes={"une primitive de e^(−x) est −e^(−x) : dérive-la pour vérifier le signe": '
         '"4*log(x) + exp(-x)"}'),
    ]),

    Paper("M02a.3", "Intégrales et aires : le signe, l'aire entre deux courbes", [
        ("a", "an integer", "(4 ** 2 - 4) - (1 ** 2 - 1)",
         'mistakes={"une primitive de 2x − 1 est x² − x : n\'oublie pas le −x": 15, '
         '"[F(x)] de 1 à 4 vaut F(4) − F(1), pas F(1) − F(4)": -12}'),
        ("b", "an integer", "3 - 1",
         'mistakes={"F(b) − F(a) : n\'oublie pas de retrancher e⁰ = 1": 3}'),
        ("c", "an integer", "2 * 3",
         'mistakes={"une primitive de 2/x est 2 ln x : garde le facteur 2": 3}'),
        ("d", "an integer", "0",
         'mistakes={"c\'est l\'aire géométrique ; l\'intégrale compte négativement la partie sous l\'axe": 3}'),
        ("e", "an irreducible fraction, as text", "Fraction(8, 3)",
         F + ', mistakes={"c\'est l\'intégrale ; l\'aire compte positivement la partie sous l\'axe : coupe là où la '
         'fonction change de signe": "0", "x² − 2x est sous l\'axe sur [0 ; 2] et au-dessus sur [−1 ; 0] : additionne '
         'les valeurs absolues des deux morceaux": "4/3"}'),
        ("f", "a list, in increasing order", "[0, 2]",
         'mistakes={"résous 2x = x², soit x² − 2x = 0 : deux solutions": [2]}'),
        ("g", "an irreducible fraction, as text", "Fraction(4, 3)",
         F + ', mistakes={"la courbe du haut moins celle du bas : sur [0 ; 2], 2x est au-dessus de x²": "-4/3"}'),
        ("h", "an irreducible fraction, as text", "Fraction(1, 2)",
         F + ', mistakes={"une primitive de sin est −cos, pas cos : dérive pour vérifier": "-1/2", '
         '"[−cos x] de 0 à π/3 : attention aux deux signes moins de −cos(π/3) − (−cos 0)": "-3/2", '
         '"F(π/3) − F(0) avec F = −cos : calcule chaque terme avec son signe, puis leur différence": "3/2"}'),
    ]),

    Paper("M02a.4", "Intégration par parties", [
        ("a", "1 or 2", "1",
         'choices=[1, 2], mistakes={"on dérive le facteur qui se simplifie en dérivant ; l\'autre doit s\'intégrer '
         'facilement": 2}'),
        ("b", "a number (4 decimals)", "(math.exp(2) + 1) / 4",
         'decimals=4, mistakes={"v est une primitive de e^(2x) : e^(2x)/2, pas e^(2x)": (math.exp(2) + 1) / 2, '
         '"[uv] − ∫ u′v : n\'oublie pas de retrancher la seconde intégrale": math.exp(2) / 2}'),
        ("c", "an expression in x, as text", '"x*sin(x) + cos(x)"',
         P + ', mistakes={"[uv] − ∫ u′v avec v = sin x : une primitive de sin est −cos, d\'où un signe": '
         '"x*sin(x) - cos(x)"}'),
        ("d", "an integer", "1",
         'mistakes={"u = ln x, v′ = 1 : [x ln x] de 1 à e, moins ∫ 1 dx": 3, '
         '"F(e) − F(1) : n\'oublie pas de calculer la primitive en 1, puis de la retrancher": 0}'),
        ("e", "an expression in x, as text", '"x**2*log(x)/2 - x**2/4"',
         P + ', mistakes={"[uv] − ∫ u′v avec u = ln x et v = x²/2 : la seconde intégrale se retranche": '
         '"x**2*log(x)/2 + x**2/4", "v est une primitive de x : x²/2, pas x²": "x**2*log(x) - x**2/2"}'),
        ("f", "a number (4 decimals)", "math.e - 2",
         'decimals=4, mistakes={"la dérivée de x² vaut 2x : le facteur 2 reste devant la seconde intégrale": '
         'math.e - 1, "la seconde intégration par parties se retranche aussi : attention aux signes": 2 - 3 * math.e}'),
    ]),

    Paper("M02a.5", "Changement de variable", [
        ("a", "a list", "[3, 5]",
         'mistakes={"quand x va de 0 à 1, u = 2x + 3 va de u(0) à u(1) : change les bornes": [0, 1]}'),
        ("b", "an irreducible fraction, as text", "Fraction(31, 5)",
         F + ', mistakes={"u = x³ + 1 va de 1 à 2 : change les bornes avec la variable": "1/5", '
         '"la borne du bas vaut u(0) = 1 : F(2) − F(1)": "32/5"}'),
        ("c", "an expression in x, as text", '"log(x**2 + 4)/2"',
         P + ', mistakes={"u = x² + 4 donne du = 2x dx : il reste un facteur 1/2": "log(x**2 + 4)"}'),
        ("d", "a number (4 decimals)", "(math.exp(3) - math.e) / 2",
         'decimals=4, mistakes={"u = 2x + 1 donne du = 2 dx : divise par 2": math.exp(3) - math.e, '
         '"u = 2x + 1 va de 1 à 3 : change les bornes": (math.e - 1) / 2}'),
        ("e", "a number (4 decimals)", "(1 - math.exp(-4)) / 2",
         'decimals=4, mistakes={"u = x² va de 0 à 4 : change les bornes": (1 - math.exp(-2)) / 2, '
         '"u = x² donne du = 2x dx : il reste un facteur 1/2": 1 - math.exp(-4)}'),
        ("f", "an irreducible fraction, as text", "Fraction(1, 3)",
         F + ', mistakes={"u = ln x va de ln 1 = 0 à ln e = 1 : change les bornes": "2/3"}'),
    ]),

    Paper("M02a.6", "Intégrales impropres : converge, diverge, valeur", [
        ("a", "an irreducible fraction, as text", "Fraction(1, 3)",
         F + ', mistakes={"[−1/x] de 3 à +∞ : la limite en +∞ vaut 0, moins la valeur en 3": "-1/3"}'),
        ("b", "an integer", "3", ''),
        ("c", "an integer", "4",
         'mistakes={"une primitive de x^(−1/2) est 2√x : [2√x] de 0 à 4": 2}'),
        ("d", "True or False", "False",
         'mistakes={"∫ de 1 à +∞ de 1/xᵖ converge seulement si p > 1 ; ici p = 0,9": True}'),
        ("e", "an irreducible fraction, as text", "Fraction(1, 2)",
         F + ', mistakes={"[e^(2x)/2] de −∞ à 0 : la valeur en 0, moins la limite en −∞, qui vaut 0": "-1/2"}'),
        ("f", "an interval, as text", '"]1 ; +oo["',
         'kind="interval", mistakes={"pour p = 1, ∫ de 1 à b de dx/x vaut ln b, qui tend vers +∞ : 1 est exclu": '
         '"[1 ; +oo[", "c\'est la règle de ∫ de 0 à 1 ; vers +∞, il faut décroître assez vite": "]-oo ; 1["}'),
        ("g", "an irreducible fraction, as text", "Fraction(1, 4)",
         F + ', mistakes={"x⁻⁵ a pour primitive x⁻⁴/(−4) : on divise par le nouvel exposant": "1/5", '
         '"[x⁻⁴/(−4)] de 1 à +∞ : la limite en +∞ vaut 0, moins la valeur en 1": "-1/4"}'),
        ("h", "an exact value, as text", "sp.sqrt(sp.pi) / 2",
         X + ', mistakes={"e^(−x²) est paire : de 0 à +∞, on a la moitié de l\'intégrale de Gauss": "sqrt(pi)"}'),
    ]),

    Paper("M02a.7", "Trapèzes et Simpson à la main, et leurs erreurs", [
        ("a", "a number (1 decimal)", "0.5 * (4 / 2 + 3.2 + 2 / 2)",
         'decimals=1, mistakes={"les deux extrémités comptent pour moitié dans la méthode des trapèzes": 4.6}'),
        ("b", "an irreducible fraction, as text", "Fraction(47, 15)",
         F + ', mistakes={"Simpson : (h/3) × (f(0) + 4 f(0,5) + f(1)), avec h = 0,5": "47/5"}'),
        ("c", "a number (4 decimals)", "0.25 * (4 / 2 + 4 / 1.0625 + 3.2 + 4 / 1.5625 + 2 / 2)",
         'decimals=4, mistakes={"les deux extrémités comptent pour moitié dans la méthode des trapèzes": '
         '0.25 * (4 + 4 / 1.0625 + 3.2 + 4 / 1.5625 + 2)}'),
        ("d", "a number (4 decimals)", "abs(3.1 - math.pi)",
         'decimals=4, mistakes={"l\'erreur est un écart, positif : |T₂ − π|": 3.1 - math.pi}'),
        ("e", "a number (1 decimal)",
         "abs(3.1 - math.pi) / abs(0.25 * (4 / 2 + 4 / 1.0625 + 3.2 + 4 / 1.5625 + 2 / 2) - math.pi)",
         'decimals=1, mistakes={"l\'erreur de T₂ divisée par celle de T₄, dans cet ordre": 0.2504}'),
        ("f", "a number (5 decimals)", "0.25 / 3 * (4 + 4 * 4 / 1.0625 + 2 * 3.2 + 4 * 4 / 1.5625 + 2)",
         'decimals=5, mistakes={"les poids de Simpson : 1, 4, 2, 4, 1, le tout multiplié par h/3": '
         '0.25 / 3 * (4 + 2 * 4 / 1.0625 + 4 * 3.2 + 2 * 4 / 1.5625 + 2)}'),
        ("g", "an integer", "5",
         'mistakes={"Simpson avec n intervalles utilise les n + 1 points x₀, …, xₙ": 4}'),
        ("h", "True or False", "True",
         'mistakes={"sur chaque intervalle, le segment des trapèzes suit exactement une droite": False}'),
    ]),

    Paper("M02a.8", "Vérifier qu'une fonction est une densité, trouver sa constante", [
        ("a", "an irreducible fraction, as text", "Fraction(1, 8)",
         F + ', mistakes={"c × (l\'intégrale de x de 0 à 4) = 1 : c est l\'inverse de cette intégrale": "8", '
         '"une primitive de x est x²/2 : ∫ de 0 à 4 de x dx vaut 4²/2": "1/16"}'),
        ("b", "an integer", "2", ''),
        ("c", "an integer", "1", ''),
        ("d", "an irreducible fraction, as text", "Fraction(2, 9)",
         F + ', mistakes={"c est l\'inverse de l\'intégrale de 3 − x de 0 à 3": "9/2", '
         '"une primitive de 3 − x est 3x − x²/2": "1/3"}'),
        ("e", "True or False", "False",
         'mistakes={"une densité est positive partout : regarde g sur [0 ; 1[": True}'),
        ("f", "True or False", "True",
         'mistakes={"l\'aire vaut 3 × 1/3 = 1 ; une densité peut dépasser 1, seule l\'aire compte": False}'),
        ("g", "an irreducible fraction, as text", "Fraction(1, 2)",
         F + ', mistakes={"utilise la densité de a), constante comprise, puis F(3) − F(1)": "1"}'),
        ("h", "an integer", "2",
         'mistakes={"une densité peut dépasser 1 : cherche où la densité de b), constante comprise, est la plus '
         'grande": 1}'),
    ]),

    Paper("M02a.9", "La probabilité d'un intervalle, et la valeur moyenne d'une fonction", [
        ("a", "an irreducible fraction, as text", "Fraction(1, 8)",
         F + ', mistakes={"c\'est la valeur de la densité en 1 ; la probabilité est l\'aire de 0 à 1": "3/8"}'),
        ("b", "an irreducible fraction, as text", "Fraction(7, 8)",
         F + ', mistakes={"une primitive de 3x²/8 est x³/8 : F(2) − F(1)": "1"}'),
        ("c", "a number", "0.0",
         'decimals=3, mistakes={"une valeur exacte a une probabilité nulle : l\'aire au-dessus d\'un point est nulle": '
         '3 / 8}'),
        ("d", "an irreducible fraction, as text", "Fraction(13, 32)",
         F + ', mistakes={"inégalités strictes ou larges, c\'est la même probabilité : F(1,5) − F(0,5) avec '
         'F(x) = x³/8": "1/2"}'),
        ("e", "a number (4 decimals)", "math.exp(-2)",
         'decimals=4, mistakes={"c\'est P(T ≤ 10) ; P(T > 10) est l\'aire de 10 à +∞": 1 - math.exp(-2)}'),
        ("f", "a number (4 decimals)", "math.exp(-1) - math.exp(-2)",
         'decimals=4, mistakes={"F(10) − F(5) avec F(t) = 1 − e^(−0,2t), pas l\'inverse": math.exp(-2) - math.exp(-1)}'),
        ("g", "an integer", "3",
         'mistakes={"divise l\'intégrale par la longueur de l\'intervalle": 9}'),
        ("h", "a number (4 decimals)", "1 / (math.e - 1)",
         'decimals=4, mistakes={"divise l\'intégrale par la longueur de l\'intervalle, e − 1": 1}'),
    ]),

    Paper("M02a.10", "Fonction de répartition, médiane et percentiles d'une loi donnée", [
        ("a", "an irreducible fraction, as text", "Fraction(3, 4)",
         F + ', mistakes={"c\'est P(X > 2) ; F(2) = P(X ≤ 2) est l\'aire de 1 à 2": "1/4"}'),
        ("b", "an expression in x, as text", '"1 - 1/x**2"',
         E + ', mistakes={"F(1) doit valoir 0 : ∫ de 1 à x, pas une primitive quelconque": "-1/x**2", '
         '"c\'est P(X > x) ; F(x) = P(X ≤ x)": "1/x**2"}'),
        ("c", "an exact value, as text", "sp.sqrt(2)",
         X + ', mistakes={"F(m) = 1/2 donne d\'abord une équation en m² : termine le calcul": "2"}'),
        ("d", "an integer", "10",
         'mistakes={"F(x) = 0,99 donne d\'abord une équation en x² : termine le calcul": 100}'),
        ("e", "an irreducible fraction, as text", "Fraction(1, 25)",
         F + ', mistakes={"c\'est P(X ≤ 5) ; P(X > 5) = 1 − F(5)": "24/25"}'),
        ("f", "a number (4 decimals)", "4 * math.log(2)",
         'decimals=4, mistakes={"q = −ln(1 − p)/0,25 : diviser par 0,25, c\'est multiplier par 4": math.log(2) / 4}'),
        ("g", "a number (4 decimals)", "-4 * math.log(0.75)",
         'decimals=4, mistakes={"le premier quartile : F(q) = 0,25, donc e^(−0,25q) = 0,75": -4 * math.log(0.25)}'),
        ("h", "a number (4 decimals)", "4 * math.log(10)",
         'decimals=4, mistakes={"le percentile 90 : F(q) = 0,9, donc e^(−0,25q) = 0,1": -4 * math.log(0.9)}'),
    ]),

    Paper("M02a.13", "L'aire sous une courbe ROC donnée par une formule", [
        ("a", "an irreducible fraction, as text", "Fraction(3, 4)",
         F + ', mistakes={"l\'AUC est ∫ de 1 − (1 − x)³ : 1 moins l\'intégrale de (1 − x)³": "1/4"}'),
        ("b", "an irreducible fraction, as text", "Fraction(4, 5)",
         F + ', mistakes={"x^(1/4) a pour primitive x^(5/4) divisée par 5/4": "5/4"}'),
        ("c", "a letter, as text", '"B"', 'mistakes={"compare les deux aires de a) et b)": "A"}'),
        ("d", "a number (3 decimals)", "1 - (1 - 0.5) ** 3",
         'decimals=3, mistakes={"le TPR vaut 1 − (1 − x)³ : n\'oublie pas le « 1 − »": 0.125}'),
        ("e", "a number (4 decimals)", "0.5 ** 0.25",
         'decimals=4, mistakes={"x^(1/4) est la racine quatrième, pas x divisé par 4": 0.125}'),
        ("f", "True or False", "False",
         'mistakes={"compare les TPR de d) et e) au même FPR": True}'),
        ("g", "a number (4 decimals)", "0.5 * (0 / 2 + 0.875 + 1 / 2)",
         'decimals=4, mistakes={"les deux extrémités comptent pour moitié dans la méthode des trapèzes": '
         '0.5 * (0 + 0.875 + 1)}'),
        ("h", "an irreducible fraction, as text", "Fraction(1, 3)",
         F + ', mistakes={"l\'AUC est l\'aire sous la courbe, ∫ de 0 à 1 de x² dx": "2/3"}'),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math
from fractions import Fraction

import sympy as sp'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M02a.1 à M02a.10, 🔗 M02a.13)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"5/9\"` ;\n"
               "- une valeur exacte entre guillemets, avec `sqrt`, `pi`, `exp` ou `ln`, `\"sqrt(5)/3\"` ;\n"
               "- une expression en $x$ entre guillemets, avec `**` pour les puissances et des parenthèses autour d'un "
               "dénominateur ou d'un exposant, `\"x**4/4 - 3/(2*x)\"`, `\"exp(3*x)\"` (une primitive se vérifie à une "
               "constante près) ;\n"
               "- une liste `[-1.25, 1]`, un intervalle `\"]-oo ; -7]\"`, une lettre `\"C\"`, ou `True` / `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M02a.16 to M02a.19)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy.integrate import quad

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
    return "aucune"'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M02a")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme dans les chapitres précédents). Ouvre ta copie "
         "`mon_travail/mymath/integrate.py`, lis la docstring de la fonction en entier, remplace la ligne "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. **Nouveau dans ce chapitre**, le premier de la partie I de workbookMaths : NumPy est permis dans "
         "`mymath` (importe-le en haut du fichier si tu t'en sers). Mais ni `scipy.integrate` ni `np.trapezoid` : "
         "les tests comparent tes résultats à eux, et un test vérifie que tu ne les appelles pas. Écris toi-même les "
         "sommes : c'est l'exercice. Chaque fonction renvoie un `float` de Python (`float(...)` convertit un nombre "
         "de NumPy).")

WRONG_ERROR = "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)"
OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "RecursionError", "TypeError",
                "ZeroDivisionError"]


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of integrate.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m02a_integrate.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m02a_integrate.py", "{keyword}", impl="ref")')]


M02A_16 = Ex(
    "M02a.16", "🔨", 1, 20, "Rectangles et trapèzes · `riemann_sum`, `trapezoid`",
    "programmer les trois sommes de Riemann et la méthode des trapèzes, avec leurs cas d'erreur.",
    "fiche §1 et §5", tracks="C, E", mymath="integrate.py",
    body=HOWTO + """

Écris `riemann_sum(f, a, b, n, rule="left")` puis `trapezoid(f, a, b, n)` dans `mon_travail/mymath/integrate.py` (fiche §1 et §5). Les deux découpent $[a ; b]$ en $n$ intervalles de largeur $h = \\frac{b - a}{n}$ ; `rule` vaut `"left"`, `"right"` ou `"midpoint"`. Elles lèvent une `ValueError` si $n < 1$, et `riemann_sum` aussi pour une règle inconnue.

La vérification calcule :
- a) `riemann_sum(lambda x: x ** 3, 1, 3, 4)`, b) la même avec `rule="right"`, c) avec `rule="midpoint"` ;
- d) `trapezoid(math.exp, 0, 1, 10)` (4 décimales) ;
- e) le nom de l'erreur levée par `riemann_sum(math.exp, 0, 1, 0)` (avec `raised`, de la cellule des outils) ;
- f) le nom de l'erreur levée par `riemann_sum(math.exp, 0, 1, 4, "center")` ;
- g) le type de `riemann_sum(lambda x: 2, 0, 1, 3)`, en texte (`"float"` pour un flottant) ;
- h) `trapezoid(lambda x: x ** 3, 1, 3, 4)`.

Puis, dans ta copie : compare h) à a) et b). Quelle relation entre les trapèzes et les deux sommes de Riemann le résultat montre-t-il ? L'intégrale exacte vaut 20 : laquelle des quatre valeurs en est la plus proche ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M02a.16a"):
    wbm.check("M02a.16a", mymath.integrate.riemann_sum(lambda x: x ** 3, 1, 3, 4), computed=True)
with checked("M02a.16b"):
    wbm.check("M02a.16b", mymath.integrate.riemann_sum(lambda x: x ** 3, 1, 3, 4, rule="right"), computed=True)
with checked("M02a.16c"):
    wbm.check("M02a.16c", mymath.integrate.riemann_sum(lambda x: x ** 3, 1, 3, 4, rule="midpoint"), computed=True)
with checked("M02a.16d"):
    wbm.check("M02a.16d", mymath.integrate.trapezoid(math.exp, 0, 1, 10), computed=True)
with checked("M02a.16e"):
    wbm.check("M02a.16e", raised(mymath.integrate.riemann_sum, math.exp, 0, 1, 0), computed=True)
with checked("M02a.16f"):
    wbm.check("M02a.16f", raised(mymath.integrate.riemann_sum, math.exp, 0, 1, 4, "center"), computed=True)
with checked("M02a.16g"):
    wbm.check("M02a.16g", type(mymath.integrate.riemann_sum(lambda x: 2, 0, 1, 3)).__name__, computed=True)
with checked("M02a.16h"):
    wbm.check("M02a.16h", mymath.integrate.trapezoid(lambda x: x ** 3, 1, 3, 4), computed=True)''',
    solution=LOAD_REF + '''
riemann_sum, trapezoid = mymath.integrate.riemann_sum, mymath.integrate.trapezoid
cube = lambda x: x ** 3   # noqa: E731
print("a)", riemann_sum(cube, 1, 3, 4), " b)", riemann_sum(cube, 1, 3, 4, rule="right"),
      " c)", riemann_sum(cube, 1, 3, 4, rule="midpoint"))
print("d)", trapezoid(math.exp, 0, 1, 10), " e)", raised(riemann_sum, math.exp, 0, 1, 0),
      " f)", raised(riemann_sum, math.exp, 0, 1, 4, "center"))
print("g)", type(riemann_sum(lambda x: 2, 0, 1, 3)).__name__, " h)", trapezoid(cube, 1, 3, 4))''',
    record=f'''wbm.record("M02a.16a", 14.0, decimals=4,
           mistakes={{"rule=\\"left\\" par défaut : la hauteur se lit au début de chaque intervalle": 27.0,
                     "multiplie la somme des hauteurs par la largeur h": 28.0}})
wbm.record("M02a.16b", 27.0, decimals=4,
           mistakes={{"rule=\\"right\\" : la hauteur se lit à la fin de chaque intervalle": 14.0,
                     "multiplie la somme des hauteurs par la largeur h": 54.0}})
wbm.record("M02a.16c", 19.75, decimals=4,
           mistakes={{"au milieu : la hauteur se lit en a + (i + 1/2) h": 14.0,
                     "multiplie la somme des hauteurs par la largeur h": 39.5}})
wbm.record("M02a.16d", 1.7197134913893146, decimals=4,
           mistakes={{"les extrémités comptent pour moitié dans la méthode des trapèzes": 1.9056275828122669,
                     "c'est la somme à gauche ; la méthode des trapèzes fait la moyenne des sommes à gauche et à droite":
                         1.6337993999663625}})
wbm.record("M02a.16e", "ValueError",
           mistakes={{"n < 1 : aucun rectangle, lève une ValueError avant de diviser par n": {{"aucune",
                                                                                          "ZeroDivisionError"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("M02a.16f", "ValueError",
           mistakes={{"une règle inconnue : lève une ValueError, plutôt que de choisir une règle au hasard": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M02a.16g", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un entier ou un nombre de NumPy":
                         {{"int", "float64"}}}})
wbm.record("M02a.16h", 20.5, decimals=4,
           mistakes={{"les deux extrémités comptent pour moitié dans la méthode des trapèzes": 27.5}})''',
    after=tests_cells("test_riemann_sum_ or test_trapezoid_ or test_integrate_uses"),
    note="Les trapèzes valent la moyenne des sommes à gauche et à droite : $\\frac{14 + 27}{2} = 20{,}5$. Pour $x^3$, "
         "le point milieu (19,75) et les trapèzes (20,5) encadrent l'intégrale exacte, 20, et le milieu en est deux "
         "fois plus près : c'est la règle générale pour une courbe tournée vers le haut (convexe, dira M05a), l'erreur du milieu valant environ la "
         "moitié de celle des trapèzes, avec le signe opposé.",
)

M02A_17 = Ex(
    "M02a.17", "🔨", 2, 15, "La méthode de Simpson · `simpson`",
    "programmer la méthode de Simpson, et vérifier son exactitude et son ordre.",
    "fiche §5 ; Ex M02a.16", tracks="C", mymath="integrate.py",
    body="""Écris `simpson(f, a, b, n)` (fiche §5) : poids $1, 4, 2, 4, \\ldots, 2, 4, 1$, le tout multiplié par $\\frac{h}{3}$. Elle lève une `ValueError` si $n$ est impair ou plus petit que 2.

La vérification calcule :
- a) `simpson(math.exp, 0, 1, 4)` (6 décimales), à comparer avec $e - 1 \\approx 1{,}718282$ ;
- b) le nom de l'erreur levée par `simpson(math.exp, 0, 1, 3)` ;
- c) `simpson(lambda x: x ** 3 - 2 * x, -1, 2, 2)` (4 décimales) ;
- d) le rapport des erreurs de `simpson(math.sin, 0, math.pi, n)` pour $n = 4$ et $n = 8$ (l'intégrale exacte vaut 2 ; 1 décimale) ;
- e) le type de `simpson(lambda x: 1, 0, 2, 2)`, en texte.

Dans ta copie : calcule c) à la main avec une primitive. Pourquoi Simpson tombe-t-il juste avec seulement deux intervalles ? Le rapport de d) est-il proche de la valeur annoncée par la fiche ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M02a.17a"):
    wbm.check("M02a.17a", mymath.integrate.simpson(math.exp, 0, 1, 4), computed=True)
with checked("M02a.17b"):
    wbm.check("M02a.17b", raised(mymath.integrate.simpson, math.exp, 0, 1, 3), computed=True)
with checked("M02a.17c"):
    wbm.check("M02a.17c", mymath.integrate.simpson(lambda x: x ** 3 - 2 * x, -1, 2, 2), computed=True)
with checked("M02a.17d"):
    error_4 = abs(mymath.integrate.simpson(math.sin, 0, math.pi, 4) - 2)
    error_8 = abs(mymath.integrate.simpson(math.sin, 0, math.pi, 8) - 2)
    wbm.check("M02a.17d", error_4 / error_8, computed=True)
with checked("M02a.17e"):
    wbm.check("M02a.17e", type(mymath.integrate.simpson(lambda x: 1, 0, 2, 2)).__name__, computed=True)''',
    solution=LOAD_REF + '''
simpson = mymath.integrate.simpson
error_4, error_8 = abs(simpson(math.sin, 0, math.pi, 4) - 2), abs(simpson(math.sin, 0, math.pi, 8) - 2)
print("a)", round(simpson(math.exp, 0, 1, 4), 6), " b)", raised(simpson, math.exp, 0, 1, 3),
      " c)", simpson(lambda x: x ** 3 - 2 * x, -1, 2, 2))
print("d)", error_4, error_8, round(error_4 / error_8, 1), " e)", type(simpson(lambda x: 1, 0, 2, 2)).__name__)''',
    record=f'''wbm.record("M02a.17a", 1.718318841921747, decimals=6,
           mistakes={{"les poids de Simpson : 1 aux extrémités, 4 aux indices impairs, 2 aux indices pairs intérieurs":
                         1.4262681481550326,
                     "multiplie la somme pondérée par h/3": 5.154956525765241,
                     "c'est la méthode des trapèzes ; Simpson pondère les points par 1, 4, 2, 4, 1": 1.7272219045575166}})
wbm.record("M02a.17b", "ValueError",
           mistakes={{"un nombre impair d'intervalles : lève une ValueError (Simpson les groupe par deux)": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M02a.17c", 0.75, decimals=4)
wbm.record("M02a.17d", 16.940059660175127, decimals=1,
           mistakes={{"l'erreur avec n = 4 divisée par l'erreur avec n = 8, dans cet ordre": 0.059}})
wbm.record("M02a.17e", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un entier ou un nombre de NumPy":
                         {{"int", "float64"}}}})''',
    after=tests_cells("test_simpson_"),
    note="Pour c), $\\int_{-1}^2 (x^3 - 2x)\\,dx = \\left[\\frac{x^4}{4} - x^2\\right]_{-1}^2 = 0 - \\left(-\\frac{3}{4}\\right) "
         "= 0{,}75$ : Simpson est exacte pour les polynômes de degré au plus 3. Le rapport de d), environ 16,9, est "
         "proche de 16 : avec $n$ plus grand, il s'en rapproche encore (l'ordre 4 est un comportement limite).",
)

M02A_18_GIVEN = '''def pdf(t):
    """A density on [0, 1]: 6 t (1 − t), and 0 elsewhere."""
    return 6 * t * (1 - t) if 0 <= t <= 1 else 0.0


def cdf_exact(x):
    """Its CDF, written with a primitive: 3x² − 2x³ on [0, 1]."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    return 3 * x ** 2 - 2 * x ** 3'''

M02A_18 = Ex(
    "M02a.18", "🔨", 2, 25, "De la densité à la fonction de répartition, puis au quantile par dichotomie · "
    "`cdf_from_pdf`, `quantile`",
    "calculer une fonction de répartition par la méthode des trapèzes, puis un quantile par dichotomie.",
    "fiche §5 et §7 ; Ex M02a.16 ; R7 (dichotomie)", tracks="C, E", mymath="integrate.py",
    body="""Écris `cdf_from_pdf(pdf, x, lower, n=1000)`, qui calcule $F(x) = \\int_{\\text{lower}}^x \\text{pdf}(t)\\,dt$ par ta méthode des trapèzes (elle rend 0,0 si $x \\le \\text{lower}$), puis `quantile(cdf, p, low, high, tol=1e-10)`, qui trouve par dichotomie le plus petit $x$ de $[\\text{low} ; \\text{high}]$ tel que $\\text{cdf}(x) \\ge p$ (fiche §7 ; R7). Lis les docstrings : elles disent les cas d'erreur.

La cellule fournie définit la densité $6t(1 - t)$ sur $[0 ; 1]$ et sa fonction de répartition exacte. La vérification calcule :
- a) `cdf_from_pdf(pdf, 0.3, 0)` (3 décimales) ;
- b) `cdf_from_pdf(pdf, -0.5, 0)` ;
- c) `cdf_from_pdf(pdf, 0.3, 0, n=1)`, avec un seul trapèze (3 décimales) ;
- d) `quantile(cdf_exact, 0.5, 0, 1)`, la médiane (6 décimales) ;
- e) le quantile d'ordre 0,9 de la loi de fonction de répartition $1 - e^{-2x}$ (pour $x \\ge 0$), cherché dans $[0 ; 10]$ (6 décimales) ;
- f) le nom de l'erreur levée par `quantile(cdf_exact, 1.2, 0, 1)` ;
- g) le percentile 95 de la densité `pdf`, en ne te servant **que de la densité** : `quantile` appliquée à `lambda x: cdf_from_pdf(pdf, x, 0)` (3 décimales).

Dans ta copie : compare e) à la formule $-\\frac{\\ln(1 - p)}{\\lambda}$ de la fiche. Pourquoi c) est-il loin de a) ?""",
    given=M02A_18_GIVEN,
    todo=LOAD_LEARNER,
    check='''with checked("M02a.18a"):
    wbm.check("M02a.18a", mymath.integrate.cdf_from_pdf(pdf, 0.3, 0), computed=True)
with checked("M02a.18b"):
    wbm.check("M02a.18b", mymath.integrate.cdf_from_pdf(pdf, -0.5, 0), computed=True)
with checked("M02a.18c"):
    wbm.check("M02a.18c", mymath.integrate.cdf_from_pdf(pdf, 0.3, 0, n=1), computed=True)
with checked("M02a.18d"):
    wbm.check("M02a.18d", mymath.integrate.quantile(cdf_exact, 0.5, 0, 1), computed=True)
with checked("M02a.18e"):
    wbm.check("M02a.18e", mymath.integrate.quantile(lambda x: 1 - math.exp(-2 * x), 0.9, 0, 10), computed=True)
with checked("M02a.18f"):
    wbm.check("M02a.18f", raised(mymath.integrate.quantile, cdf_exact, 1.2, 0, 1), computed=True)
with checked("M02a.18g"):
    numerical_cdf = lambda x: mymath.integrate.cdf_from_pdf(pdf, x, 0)   # noqa: E731
    wbm.check("M02a.18g", mymath.integrate.quantile(numerical_cdf, 0.95, 0, 1), computed=True)''',
    solution=LOAD_REF + '''
cdf_from_pdf, quantile = mymath.integrate.cdf_from_pdf, mymath.integrate.quantile
print("a)", round(cdf_from_pdf(pdf, 0.3, 0), 6), "exact:", cdf_exact(0.3), " b)", cdf_from_pdf(pdf, -0.5, 0),
      " c)", cdf_from_pdf(pdf, 0.3, 0, n=1))
print("d)", quantile(cdf_exact, 0.5, 0, 1), " e)", quantile(lambda x: 1 - math.exp(-2 * x), 0.9, 0, 10),
      "formula:", -math.log(1 - 0.9) / 2)
print("f)", raised(quantile, cdf_exact, 1.2, 0, 1),
      " g)", quantile(lambda x: cdf_from_pdf(pdf, x, 0), 0.95, 0, 1))''',
    record=f'''wbm.record("M02a.18a", 0.216, decimals=3,
           mistakes={{"c'est la densité en 0,3 ; F(0,3) est l'aire sous la densité de 0 à 0,3": 1.26}})
wbm.record("M02a.18b", 0.0, decimals=4,
           mistakes={{"x ≤ lower : aucune aire à gauche, F vaut 0": {{-0.5, 0.5}}}})
wbm.record("M02a.18c", 0.189, decimals=3,
           mistakes={{"n=1 : un seul trapèze, (x − lower) × (pdf(lower) + pdf(x))/2 ; tient compte de n": 0.216}})
wbm.record("M02a.18d", 0.5, decimals=6)
wbm.record("M02a.18e", math.log(10) / 2, decimals=6,
           mistakes={{"le quantile est l'abscisse x où la CDF atteint p, pas la valeur de la CDF": 0.9}})
wbm.record("M02a.18f", "ValueError",
           mistakes={{"p doit être strictement entre 0 et 1 : lève une ValueError": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M02a.18g", 0.8646496378284156, decimals=3,
           mistakes={{"c'est le percentile 5 ; le percentile 95 laisse 95 % de l'aire à sa gauche": 0.1354}})''',
    after=tests_cells("test_cdf_from_pdf_ or test_quantile_"),
    note="Pour e), $-\\frac{\\ln(0{,}1)}{2} = \\frac{\\ln 10}{2} \\approx 1{,}151293$ : la dichotomie retrouve la formule. "
         "Un seul trapèze (c) remplace l'arc de la densité entre 0 et 0,3 par une corde : 0,189 au lieu de 0,216 ; avec "
         "1 000 trapèzes, l'écart tombe sous $10^{-7}$. La dichotomie de g) appelle `cdf_from_pdf` une quarantaine de "
         "fois, chacune avec 1 000 trapèzes : environ 40 000 évaluations de la densité, en une fraction de seconde.",
)

M02A_19_GIVEN = '''x = sp.Symbol("x")'''

M02A_19 = Ex(
    "M02a.19", "📦", 1, 15, "Vérifier avec `scipy.integrate.quad` et SymPy",
    "calculer des intégrales avec SciPy (numériquement) et SymPy (exactement), et lire ce que chacun rend.",
    "fiche §2, §4 et §5", tracks="C, E",
    body="""Deux outils calculent des intégrales. `quad(f, a, b)`, de `scipy.integrate`, rend un couple `(valeur, estimation_de_l_erreur)` et accepte des bornes infinies (`-math.inf`, `math.inf`). `sp.integrate(expression, x)` rend une primitive exacte, et `sp.integrate(expression, (x, a, b))` une intégrale exacte (`sp.oo` pour $+\\infty$).

Calcule :
- a) avec `quad`, $\\int_{-\\infty}^{+\\infty} e^{-x^2}\\,dx$ (la valeur, 6 décimales) ;
- b) un booléen : l'estimation d'erreur rendue par `quad` en a) est-elle inférieure à $10^{-6}$ ?
- c) avec SymPy, $\\int_0^{+\\infty} x\\,e^{-x}\\,dx$ (un entier) ;
- d) avec SymPy, $\\int_0^1 \\frac{4}{1 + x^2}\\,dx$ (une valeur exacte : le résultat de SymPy tel quel, ou converti en texte avec `str(...)`) ;
- e) avec `quad`, $\\int_0^1 \\frac{dx}{\\sqrt{x}}$ (6 décimales), une intégrale impropre : la fonction explose en 0 ;
- f) le nom de la fonction spéciale que SymPy utilise pour écrire une primitive de $e^{-x^2}$ (un texte de trois lettres : regarde `sp.integrate(sp.exp(-x ** 2), x)`).

Dans ta copie : la primitive de f) contredit-elle la fiche, qui dit que $e^{-x^2}$ n'a pas de primitive écrite avec les fonctions usuelles ?""",
    given=M02A_19_GIVEN,
    todo='''answer_M02a_19a = ...  # a) the value of quad(...)
answer_M02a_19b = ...  # b) True or False
answer_M02a_19c = ...  # c) sp.integrate(...)
answer_M02a_19d = ...  # d) sp.integrate(...), or its str(...)
answer_M02a_19e = ...  # e) the value of quad(...)
answer_M02a_19f = ...  # f) a name, as text''',
    check='''for letter, answer in zip("abcdef", [answer_M02a_19a, answer_M02a_19b, answer_M02a_19c, answer_M02a_19d,
                                      answer_M02a_19e, answer_M02a_19f]):
    wbm.check(f"M02a.19{letter}", answer)''',
    solution='''value, error = quad(lambda t: math.exp(-t ** 2), -math.inf, math.inf)
answer_M02a_19a = value
answer_M02a_19b = bool(error < 1e-6)
answer_M02a_19c = int(sp.integrate(x * sp.exp(-x), (x, 0, sp.oo)))
answer_M02a_19d = str(sp.integrate(4 / (1 + x ** 2), (x, 0, 1)))
answer_M02a_19e = quad(lambda t: 1 / math.sqrt(t), 0, 1)[0]
answer_M02a_19f = "erf"
print(value, error, answer_M02a_19b, answer_M02a_19c, answer_M02a_19d, answer_M02a_19e)
print(sp.integrate(sp.exp(-x ** 2), x), "|", sp.integrate(4 / (1 + x ** 2), x))''',
    record='''wbm.record("M02a.19a", math.sqrt(math.pi), decimals=6,
           mistakes={"quad rend un couple (valeur, erreur) : garde le premier élément": 1.4e-08})
wbm.record("M02a.19b", True, mistakes={"compare le second élément du couple rendu par quad à 1e-6": False})
wbm.record("M02a.19c", 1)
wbm.record("M02a.19d", sp.pi, kind="exact",
           mistakes={"l'intégrande vaut 4/(1 + x²) : n'oublie pas le facteur 4": "pi/4"})
wbm.record("M02a.19e", 2.0, decimals=6)
wbm.record("M02a.19f", "erf",
           mistakes={"le nom de la fonction seul, sans parenthèses ni variable": "erf(x)"})''',
    note="SymPy écrit la primitive de $e^{-x^2}$ avec `erf`, la **fonction d'erreur**, définie justement comme "
         "$\\frac{2}{\\sqrt{\\pi}}\\int_0^x e^{-t^2}\\,dt$ : ce n'est pas une fonction usuelle, mais un nom donné à cette "
         "intégrale. Pas de contradiction avec la fiche. Tu la retrouveras en M02b : la fonction de répartition de la "
         "loi normale s'écrit avec `erf`. Pour d), SymPy connaît la primitive $4\\arctan x$, d'où "
         "$4\\arctan 1 = \\pi$, la valeur admise en M02a.7.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M02a.20 to M02a.22)
# ---------------------------------------------------------------------------
M02A_20_EXPERIMENT = '''def trapezoids(f, a, b, n):
    xs = np.linspace(a, b, n + 1)
    ys = np.array([f(x) for x in xs])
    return (b - a) / n * (ys[0] / 2 + ys[1:-1].sum() + ys[-1] / 2)


def simpsons(f, a, b, n):
    xs = np.linspace(a, b, n + 1)
    ys = np.array([f(x) for x in xs])
    return (b - a) / n / 3 * (ys[0] + ys[-1] + 4 * ys[1:-1:2].sum() + 2 * ys[2:-1:2].sum())


cases = {
    "a) trapèzes, e^x sur [0 ; 1]": (trapezoids, math.exp, 0, 1, math.e - 1),
    "b) Simpson, e^x sur [0 ; 1]": (simpsons, math.exp, 0, 1, math.e - 1),
    "c) Simpson, √x sur [0 ; 1]": (simpsons, math.sqrt, 0, 1, 2 / 3),
    "d) trapèzes, e^(cos x) sur [0 ; 2π]": (trapezoids, lambda x: math.exp(math.cos(x)), 0, 2 * math.pi,
                                           quad(lambda x: math.exp(math.cos(x)), 0, 2 * math.pi, epsabs=1e-14)[0]),
}
for name, (method, f, a, b, exact) in cases.items():
    error_4, error_8 = abs(method(f, a, b, 4) - exact), abs(method(f, a, b, 8) - exact)
    print(f"{name:38} erreur n = 4 : {error_4:.1e}   n = 8 : {error_8:.1e}   rapport : {error_4 / error_8:.1f}")'''

M02A_20 = Ex(
    "M02a.20", "🔮", 1, 10, "Prédire : le pas divisé par 2, l'erreur divisée par combien ?",
    "prévoir de combien l'erreur d'une méthode diminue quand le pas est divisé par 2, et voir quand la règle de la "
    "fiche ne s'applique plus.", "fiche §5", tracks="C, E", hypothesis=True,
    body="""On passe de $n = 4$ à $n = 8$ intervalles (le pas est divisé par 2). Pour chaque cas, de combien l'erreur est-elle divisée ? Choisis : (1) moins de 4 ; (2) environ 4 ; (3) environ 16 ; (4) bien plus que 16.
- a) la méthode des trapèzes pour $\\int_0^1 e^x\\,dx$ ;
- b) la méthode de Simpson pour la même intégrale ;
- c) la méthode de Simpson pour $\\int_0^1 \\sqrt{x}\\,dx$ (attention : la dérivée de $\\sqrt{x}$ devient infinie en 0) ;
- d) la méthode des trapèzes pour $\\int_0^{2\\pi} e^{\\cos x}\\,dx$, une fonction **périodique** intégrée sur une période entière.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions, vérifie-les, puis lance l'expérience. Réponds par le **numéro du choix**, de 1 à 4, et non par le facteur : pour « environ 4 », écris 2.""",
    todo='''prediction_M02a_20a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M02a_20b = ...  # b) 1, 2, 3 or 4
prediction_M02a_20c = ...  # c) 1, 2, 3 or 4
prediction_M02a_20d = ...  # d) 1, 2, 3 or 4''',
    check='''for letter, prediction in zip("abcd", [prediction_M02a_20a, prediction_M02a_20b, prediction_M02a_20c,
                                      prediction_M02a_20d]):
    wbm.check(f"M02a.20{letter}", prediction)''',
    record='''wbm.record("M02a.20a", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M02a.20b", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M02a.20c", 1, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M02a.20d", 4, prediction=True, choices=[1, 2, 3, 4])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(M02A_20_EXPERIMENT, ["prediction_M02a_20a", "prediction_M02a_20b", "prediction_M02a_20c",
                                               "prediction_M02a_20d"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", M02A_20_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : quelle hypothèse de la fiche (« pour une fonction régulière ») "
               "n'est pas remplie en c) ? Dessine $e^{\\cos x}$ sur $[0 ; 2\\pi]$ et les quatre trapèzes : pourquoi "
               "leurs erreurs se compensent-elles si bien en d) ?"),
    ],
    note="a) et b) suivent la fiche : environ 4 et 16. En c), la dérivée de $\\sqrt{x}$ est infinie en 0 : près de 0, "
         "aucune parabole n'imite bien la courbe, et l'erreur n'est divisée que par $2^{1{,}5} \\approx 2{,}8$, pour "
         "Simpson comme pour les trapèzes. En d), l'erreur passe de $3 \\times 10^{-2}$ à environ $10^{-6}$ : pour une "
         "fonction régulière et périodique intégrée sur une période, les erreurs des trapèzes se compensent presque "
         "exactement, et la méthode converge bien plus vite que $h^2$. La règle « ÷ 4, ÷ 16 » est un cas typique, pas "
         "une loi universelle.",
)

M02A_21_GIVEN = '''bounds = [1, 2, 3, 4, 5]
gauss = math.sqrt(math.pi)'''

M02A_21 = Ex(
    "M02a.21", "🔬", 2, 20, "L'intégrale de Gauss par le calcul : la borne qui s'éloigne",
    "vérifier numériquement la valeur de l'intégrale de Gauss en reculant les bornes, et mesurer à quelle vitesse "
    "la queue devient négligeable.", "fiche §4 et §5 ; Ex M02a.19", tracks="C",
    body="""On admet $\\int_{-\\infty}^{+\\infty} e^{-x^2}\\,dx = \\sqrt{\\pi}$ (fiche §4). Une machine ne peut pas aller jusqu'à l'infini : on calcule $I(B) = \\int_{-B}^{B} e^{-x^2}\\,dx$ pour des bornes $B$ de plus en plus grandes, avec `quad`. La cellule fournie définit la liste `bounds` et la valeur `gauss` $= \\sqrt{\\pi}$.

Calcule :
- a) $I(1)$ (4 décimales) ;
- b) le plus petit $B$ de `bounds` pour lequel $\\lvert I(B) - \\sqrt{\\pi} \\rvert < 10^{-6}$ (un entier) ;
- c) le rapport $\\frac{I(3)}{\\sqrt{\\pi}}$ (6 décimales) ;
- d) $\\int_{-6}^{6} e^{-x^2/2}\\,dx$ (4 décimales), à comparer avec $\\sqrt{2\\pi}$.

Puis trace l'écart $\\lvert I(B) - \\sqrt{\\pi} \\rvert$ en fonction de $B$, de 0,5 à 5, avec une échelle **logarithmique** en ordonnée (`ax.semilogy`).

Dans ta copie : pour $\\lvert x \\rvert \\ge B \\ge 1$, $e^{-x^2} \\le e^{-B\\lvert x \\rvert}$. Déduis-en une borne de l'écart $\\sqrt{\\pi} - I(B)$ (deux queues), et compare-la à ce que montre ta courbe. Pourquoi un ordinateur peut-il remplacer $+\\infty$ par 6 pour la densité normale ?""",
    given=M02A_21_GIVEN,
    todo='''I_1 = ...          # a) a number
first_bound = ...  # b) an integer of bounds
ratio_3 = ...      # c) a number
normal_area = ...  # d) a number''',
    check='''wbm.check("M02a.21a", I_1)
wbm.check("M02a.21b", first_bound)
wbm.check("M02a.21c", ratio_3)
wbm.check("M02a.21d", normal_area)''',
    solution='''def I(B):
    return quad(lambda x: math.exp(-x ** 2), -B, B)[0]


I_1 = I(1)
first_bound = next(B for B in bounds if abs(I(B) - gauss) < 1e-6)
ratio_3 = I(3) / gauss
normal_area = quad(lambda x: math.exp(-x ** 2 / 2), -6, 6)[0]
print("a)", round(I_1, 4), " b)", first_bound, " c)", round(ratio_3, 6), " d)", round(normal_area, 4),
      " √(2π) =", round(math.sqrt(2 * math.pi), 4))
print([f"{abs(I(B) - gauss):.1e}" for B in bounds])''',
    record='''wbm.record("M02a.21a", 1.493648265624854, decimals=4,
           mistakes={"I(B) va de −B à B : de −1 à 1, pas de 0 à 1": 0.7468})
wbm.record("M02a.21b", 4,
           mistakes={"calcule l'écart |I(B) − √π| pour chaque B de la liste, et garde le premier qui passe sous "
                     "1e-6": {3, 5}})
wbm.record("M02a.21c", 0.9999779095030017, decimals=6)
wbm.record("M02a.21d", math.sqrt(2 * math.pi), decimals=4,
           mistakes={"e^(−x²/2) : le carré divisé par 2, pas le carré seul": 1.7725})''',
    after=[("md", "**Le tracé** de $\\lvert I(B) - \\sqrt{\\pi} \\rvert$ pour $B$ de 0,5 à 5 (`np.linspace`, `ax.semilogy`)."),
           ("todo", "# the plot of |I(B) − √π| against B, log scale on the y-axis"),
           ("solution", '''Bs = np.linspace(0.5, 5, 40)
gaps = [max(abs(I(B) - gauss), 1e-17) for B in Bs]
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.semilogy(Bs, gaps, marker=".")
ax.set_xlabel("B")
ax.set_ylabel("|I(B) − √π| (échelle log)")
ax.set_title("La queue de e^(−x²) devient vite négligeable")
ax.grid(True, which="both", alpha=0.3)
plt.show()''')],
    note="L'écart vaut environ 0,28 pour $B = 1$, $8 \\times 10^{-3}$ pour $B = 2$, $4 \\times 10^{-5}$ pour $B = 3$, "
         "$3 \\times 10^{-8}$ pour $B = 4$ : il s'effondre plus vite qu'une exponentielle (la courbe en échelle log "
         "plonge de plus en plus vite). La borne : $\\sqrt{\\pi} - I(B) \\le 2\\int_B^{+\\infty} e^{-Bx}\\,dx = "
         "\\frac{2e^{-B^2}}{B}$, soit environ $5 \\times 10^{-8}$ pour $B = 4$. Pour la densité normale, la masse au-delà "
         "de 6 écarts types vaut environ $2 \\times 10^{-9}$ : couper à 6 ne change rien en pratique.",
)

M02A_22_CHECK = '''with checked("M02a.22 vérifications"):
    problems = []
    f_test, F_test = (lambda x: math.cos(x) + 1.5), (lambda x: math.sin(x) + 1.5 * x + 2)   # F(0) = 2, not 0
    fig, ax = plt.subplots(figsize=(5, 3))
    try:
        created = drawn(draw_riemann, ax, f_test, 0, 3, 6)
    finally:
        plt.close(fig)                                   # only the checks below are shown here
    if created:
        problems.append("draw_riemann ouvre sa propre figure : dessine dans l'axe reçu (ax.bar, ax.plot)")
    else:
        bars = [p for p in ax.patches if hasattr(p, "get_width")]
        mids = [0.25 + 0.5 * i for i in range(6)]
        if len(bars) != 6:
            problems.append(f"draw_riemann : n = 6 rectangles avec ax.bar (j'en compte {len(bars)})")
        else:
            widths = sorted(round(b.get_width(), 6) for b in bars)
            heights = sorted(round(b.get_height(), 6) for b in bars)
            lefts = sorted(round(b.get_x(), 6) for b in bars)
            if widths != [0.5] * 6 or lefts != [0.5 * i for i in range(6)]:
                problems.append("draw_riemann : des rectangles de largeur h = (b − a)/n, qui partent de a + i h "
                                "(ax.bar(..., width=h, align=\\"edge\\"))")
            elif heights != sorted(round(f_test(m), 6) for m in mids):
                problems.append("draw_riemann : la hauteur de chaque rectangle est f au milieu de son intervalle")
        if not ax.lines:
            problems.append("draw_riemann : la courbe de f, avec ax.plot")
        total = 0.5 * sum(f_test(m) for m in mids)
        if f"{total:.4f}" not in ax.get_title().replace(",", "."):
            problems.append("draw_riemann : la somme des aires des rectangles dans le titre, avec 4 décimales")
    fig, ax = plt.subplots(figsize=(5, 3))
    try:
        created = drawn(draw_area_function, ax, f_test, F_test, 0, 3)
    finally:
        plt.close(fig)
    if created:
        problems.append("draw_area_function ouvre sa propre figure : dessine dans l'axe reçu")
    else:
        exact = F_test(3) - F_test(0)
        curves = [line for line in ax.lines if len(np.atleast_1d(line.get_ydata())) >= 50]
        good = [line for line in curves if abs(float(np.atleast_1d(line.get_ydata())[0])) < 1e-9
                and abs(float(np.atleast_1d(line.get_ydata())[-1]) - exact) < 1e-3]
        if len(curves) < 2:
            problems.append("draw_area_function : deux courbes sur la grille de 200 points, l'aire calculée et "
                            "F(x) − F(a)")
        elif len(good) < 2:
            problems.append("draw_area_function : les deux courbes partent de 0 en x = a (une aire de a à a) et "
                            "finissent à F(b) − F(a), l'intégrale de a à b : trace F(x) − F(a), pas F(x)")
    if problems:
        print("❌ Ex M02a.22 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M02a.22 : les rectangles, leur somme, et la fonction aire qui suit F(x) − F(a).")'''

M02A_22 = Ex(
    "M02a.22", "🎨", 1, 20, "L'aire qui se remplit : la courbe, les rectangles et la primitive",
    "dessiner une somme de Riemann, puis la fonction aire, et voir qu'elle coïncide avec une primitive.",
    "fiche §1 et §2 ; R0 (matplotlib)", tracks="C, E",
    body="""Complète deux fonctions, qui dessinent dans l'axe `ax` qu'elles reçoivent :
- `draw_riemann(ax, f, a, b, n)` : la courbe de $f$ sur $[a ; b]$ (`ax.plot`), les $n$ rectangles **au milieu** (`ax.bar(lefts, heights, width=h, align="edge", alpha=0.4)`, où `lefts` sont les abscisses $a + ih$ des bords gauches) et, dans le titre, la somme des aires des rectangles avec 4 décimales (`f"somme = {total:.4f}"`) ;
- `draw_area_function(ax, f, F, a, b)` : sur une grille de 200 points de $[a ; b]$, deux courbes : la **fonction aire** $A(x) = \\int_a^x f$, calculée numériquement (méthode des trapèzes cumulée : `np.cumsum`), et $F(x) - F(a)$, calculée avec la primitive `F` ; avec une légende.

⚠️ `f` et `F` prennent **un** nombre (elles sont écrites avec `math`) : sur une grille `xs`, calcule `ys = np.array([f(x) for x in xs])`, pas `f(xs)`.

La cellule suivante les essaie sur $f(x) = 1 + x\\,e^{-x}$ entre 0 et 4 (une primitive est $F(x) = x - (x + 1)e^{-x}$, par parties) ; une autre les vérifie sur une autre fonction.

Dans ta copie : les deux courbes de droite se superposent-elles ? Quel théorème cela illustre-t-il ? Où la fonction aire monte-t-elle le plus vite, et pourquoi là ?""",
    todo='''def draw_riemann(ax, f, a, b, n):
    """Draw f on [a, b], its n midpoint rectangles (ax.bar) and their total area in the title (4 decimals)."""
    raise NotImplementedError("ax.plot pour la courbe, ax.bar pour les rectangles, puis le titre avec la somme")


def draw_area_function(ax, f, F, a, b):
    """Draw the area function x -> ∫_a^x f (cumulative trapezoids) and F(x) − F(a) on 200 points of [a, b]."""
    raise NotImplementedError("une grille, np.cumsum des aires des trapèzes, puis les deux courbes et une légende")''',
    check='''with checked("M02a.22 figure"):
    f_demo = lambda x: 1 + x * math.exp(-x)              # noqa: E731
    F_demo = lambda x: x - (x + 1) * math.exp(-x)        # noqa: E731
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5))
    try:
        created = drawn(draw_riemann, ax1, f_demo, 0, 4, 8) or drawn(draw_area_function, ax2, f_demo, F_demo, 0, 4)
    except BaseException:
        plt.close(fig)                                     # no empty figure while the functions are not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M02a.22 : une de tes fonctions ouvre sa propre figure (plt.figure ou plt.subplots) : dessine "
              "dans l'axe qu'elle reçoit.")
    else:
        plt.show()''',
    solution='''def draw_riemann(ax, f, a, b, n):
    """Draw f on [a, b], its n midpoint rectangles (ax.bar) and their total area in the title (4 decimals)."""
    h = (b - a) / n
    lefts = [a + i * h for i in range(n)]
    heights = [f(left + h / 2) for left in lefts]
    xs = np.linspace(a, b, 300)
    ax.bar(lefts, heights, width=h, align="edge", alpha=0.4, edgecolor="C0")
    ax.plot(xs, [f(x) for x in xs], color="black")
    ax.set_title(f"rectangles au milieu : somme = {h * sum(heights):.4f}")
    ax.grid(True, alpha=0.3)


def draw_area_function(ax, f, F, a, b):
    """Draw the area function x -> ∫_a^x f (cumulative trapezoids) and F(x) − F(a) on 200 points of [a, b]."""
    xs = np.linspace(a, b, 200)
    ys = np.array([f(x) for x in xs])
    pieces = (xs[1:] - xs[:-1]) * (ys[1:] + ys[:-1]) / 2       # the area of each trapezoid
    area = np.concatenate([[0.0], np.cumsum(pieces)])
    ax.plot(xs, area, linewidth=3, alpha=0.5, label="aire de a à x (trapèzes cumulés)")
    ax.plot(xs, [F(x) - F(a) for x in xs], "--", color="black", label="F(x) − F(a)")
    ax.set_title("La fonction aire et une primitive")
    ax.legend()
    ax.grid(True, alpha=0.3)


f_demo = lambda x: 1 + x * math.exp(-x)              # noqa: E731
F_demo = lambda x: x - (x + 1) * math.exp(-x)        # noqa: E731
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5))
draw_riemann(ax1, f_demo, 0, 4, 8)
draw_area_function(ax2, f_demo, F_demo, 0, 4)
plt.show()''',
    after=[("md", "**Vérifications automatiques** (les figures elles-mêmes se jugent à l'œil)."), ("code", M02A_22_CHECK)],
    note="Les deux courbes de droite se superposent : la fonction aire est une primitive de $f$ (théorème fondamental, "
         "§2). Elle monte le plus vite là où $f$ est la plus haute, vers $x = 1$ (le maximum de $1 + x\\,e^{-x}$) : sa "
         "pente est $f(x)$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M02a.23 to M02a.25)
# ---------------------------------------------------------------------------
M02A_23_MISTAKES = bug_letters_mistakes(
    "ACD", "BE",
    {"A": "relis l'ordre des bornes dans chaque crochet [F(x)] : la borne du haut d'abord",
     "C": "dérive chaque primitive annoncée : redonne-t-elle la fonction ? Une fonction positive a une intégrale "
          "positive",
     "D": "relis chaque phrase qui parle d'aire : l'intégrale compte négativement ce qui est sous l'axe"})

M02A_23 = Ex(
    "M02a.23", "🐛", 1, 15, "Chasse à l'erreur : bornes inversées, primitive fausse, aire négative",
    "repérer trois erreurs classiques du calcul intégral, puis calculer les bonnes valeurs.",
    "fiche §1 et §2", tracks="C",
    body="""Voici cinq calculs, chacun avec ce qu'en dit son auteur. Trois sont faux. **Sans exécuter de code**, trouve-les.

- **(A)** « $\\int_0^2 3x^2\\,dx = \\big[x^3\\big]_2^0 = 0 - 8 = -8$. »
- **(B)** « Une primitive de $\\frac{1}{x^2}$ est $-\\frac{1}{x}$, donc $\\int_1^2 \\frac{dx}{x^2} = -\\frac{1}{2} - (-1) = \\frac{1}{2}$. »
- **(C)** « Une primitive de $e^{-3x}$ est $e^{-3x}$, donc $\\int_0^1 e^{-3x}\\,dx = e^{-3} - 1 \\approx -0{,}9502$. »
- **(D)** « L'aire de la région comprise entre la courbe de $x^2 - 1$ et l'axe des abscisses, pour $x$ de 0 à 2, vaut $\\int_0^2 (x^2 - 1)\\,dx = \\frac{8}{3} - 2 = \\frac{2}{3}$. »
- **(E)** « $\\int_1^e \\frac{2}{x}\\,dx = \\big[2\\ln x\\big]_1^e = 2$. »

Questions :
- a) les lettres des calculs faux, dans l'ordre alphabétique (un texte) ;
- b) pour chacun des cinq, de (A) à (E), la bonne valeur de ce que décrit la phrase de son auteur (une liste de 5 nombres, 4 décimales).

Dans ta copie : pour chaque calcul faux, quelle règle a été oubliée ? Quel signe aurait dû alerter l'auteur de (C) ?""",
    todo='''answer_M02a_23a = ...  # a) letters, as text
answer_M02a_23b = ...  # b) a list of 5 values (4 decimals)''',
    check='''wbm.check("M02a.23a", answer_M02a_23a)
wbm.check("M02a.23b", answer_M02a_23b)''',
    solution='''answer_M02a_23a = "ACD"
answer_M02a_23b = [8, 0.5, (1 - math.exp(-3)) / 3, 2, 2]
print(answer_M02a_23a, [round(v, 4) for v in answer_M02a_23b])
x = sp.Symbol("x")
print(sp.integrate(3 * x ** 2, (x, 0, 2)), sp.integrate(1 / x ** 2, (x, 1, 2)), sp.integrate(sp.exp(-3 * x), (x, 0, 1)),
      -sp.integrate(x ** 2 - 1, (x, 0, 1)) + sp.integrate(x ** 2 - 1, (x, 1, 2)), sp.integrate(2 / x, (x, 1, sp.E)))''',
    record=f'''wbm.record("M02a.23a", "ACD",
           mistakes={M02A_23_MISTAKES})
wbm.record("M02a.23b", [8.0, 0.5, (1 - math.exp(-3)) / 3, 2.0, 2.0], decimals=4,
           mistakes={{"ce sont les valeurs que donnent les calculs ; donne celles que décrit chaque phrase":
                         [-8.0, 0.5, math.exp(-3) - 1, 2 / 3, 2.0],
                     "(D) demande une aire : la partie sous l'axe compte positivement":
                         [8.0, 0.5, (1 - math.exp(-3)) / 3, 2 / 3, 2.0]}})''',
    note="(A) Les bornes sont inversées dans le crochet : $\\big[x^3\\big]_0^2 = 8$. (C) La primitive est fausse : la "
         "dérivée de $e^{-3x}$ vaut $-3e^{-3x}$ ; une primitive de $e^{-3x}$ est $-\\frac{1}{3}e^{-3x}$, d'où "
         "$\\frac{1 - e^{-3}}{3} \\approx 0{,}3167$. Le signe négatif devait alerter : une fonction positive a une "
         "intégrale positive. (D) $x^2 - 1$ est négative sur $[0 ; 1[$ : l'aire vaut $\\frac{2}{3} + \\frac{4}{3} = 2$, "
         "alors que l'intégrale vaut $\\frac{2}{3}$. (B) et (E) sont justes.",
)

M02A_24_CHECK = '''with checked("M02a.24 vérifications"):
    problems = []
    cases = [
        (sp.sin(x) ** 2 / 2, sp.sin(x) * sp.cos(x), True, "sin²x/2 est une primitive de sin x cos x"),
        (-sp.cos(2 * x) / 4, sp.sin(x) * sp.cos(x), True, "−cos(2x)/4 aussi (elle diffère de la précédente d'une "
                                                         "constante)"),
        (sp.exp(x ** 2), sp.exp(x ** 2), False, "e^(x²) n'est pas une primitive de e^(x²) (règle de la chaîne)"),
        (sp.atan(x), 1 / (1 + x ** 2), True, "arctan est une primitive de 1/(1 + x²)"),
        (x * sp.exp(x), x * sp.exp(x), False, "x eˣ n'est pas une primitive de x eˣ"),
    ]
    for F_case, f_case, expected, why in cases:
        result = is_primitive(F_case, f_case)
        if result is None:
            problems.append("is_primitive ne renvoie rien (None) : il manque un return")
            break
        if not isinstance(result, bool):
            problems.append(f"is_primitive doit renvoyer un booléen de Python, True ou False, et non un objet de type "
                            f"{type(result).__name__} : convertis avec bool(...)")
            break
        if result is not expected:
            problems.append(f"is_primitive se trompe : {why}")
    if problems:
        print("❌ Ex M02a.24 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M02a.24 : is_primitive reconnaît une primitive, même écrite sous une autre forme.")'''

M02A_24 = Ex(
    "M02a.24", "🛠️", 1, 10, "Vérifier une primitive avec SymPy : dériver le résultat",
    "écrire une petite fonction qui vérifie une primitive en la dérivant, réflexe professionnel avant d'utiliser un "
    "résultat.", "fiche §2", tracks="C",
    body="""Une primitive se vérifie toujours en la **dérivant** : c'est plus sûr que de la recalculer, et cela marche quelle que soit sa forme. Écris `is_primitive(F, f)`, qui reçoit deux expressions SymPy en `x` et renvoie `True` si $F' = f$, `False` sinon. Outils : `sp.diff(F, x)` dérive, `sp.simplify(expression)` simplifie ; teste si la simplification de $F' - f$ vaut 0, et renvoie un booléen de Python (`bool(...)`).

⚠️ Ne compare pas $F'$ et $f$ avec `==` sans simplifier : SymPy compare alors l'**écriture** des expressions, pas leurs valeurs, et $\\sin x \\cos x$ n'est pas écrit comme la dérivée de $-\\frac{\\cos(2x)}{4}$.

Dans ta copie : `sin²x/2` et `−cos(2x)/4` sont toutes deux des primitives de $\\sin x \\cos x$. Que vaut leur différence ? Est-ce une contradiction ?""",
    given='''x = sp.Symbol("x")''',
    todo='''def is_primitive(F, f):
    """True when the SymPy expression F is an antiderivative of f in x (F' − f simplifies to 0)."""
    raise NotImplementedError("sp.diff, puis sp.simplify de la différence, comparée à 0")''',
    solution='''def is_primitive(F, f):
    """True when the SymPy expression F is an antiderivative of f in x (F' − f simplifies to 0)."""
    return bool(sp.simplify(sp.diff(F, x) - f) == 0)


print(is_primitive(-sp.cos(2 * x) / 4, sp.sin(x) * sp.cos(x)), sp.diff(-sp.cos(2 * x) / 4, x) == sp.sin(x) * sp.cos(x),
      sp.simplify(sp.sin(x) ** 2 / 2 - (-sp.cos(2 * x) / 4)))''',
    after=[("code", M02A_24_CHECK)],
    note="$\\frac{\\sin^2 x}{2} - \\left(-\\frac{\\cos 2x}{4}\\right) = \\frac{1}{4}$, une constante (car "
         "$\\cos 2x = 1 - 2\\sin^2 x$) : deux primitives d'une même fonction diffèrent d'une constante, pas de "
         "contradiction. La comparaison directe avec `==` rend `False`, alors que la primitive est juste : c'est le "
         "piège que `sp.simplify` évite.",
)

M02A_25_GIVEN = '''CHALLENGE = [
    ("e^(−x²) sur [0 ; 2]", lambda x: math.exp(-x ** 2), 0, 2),
    ("1/(1 + x) sur [0 ; 1]", lambda x: 1 / (1 + x), 0, 1),
    ("√(1 + x³) sur [0 ; 2]", lambda x: math.sqrt(1 + x ** 3), 0, 2),
]
TARGET = 1e-8


def counted(f):
    """f, with a counter of its calls (counted_f.calls)."""
    def wrapper(x):
        wrapper.calls += 1
        return f(x)
    wrapper.calls = 0
    return wrapper'''

M02A_25_CHECK = '''with checked("M02a.25"):
    worst, calls_max = 0.0, 0
    for name, f, a, b in CHALLENGE:
        g = counted(f)
        value = best_integral(g, a, b)
        exact = quad(f, a, b, epsabs=1e-13, epsrel=1e-13)[0]
        worst, calls_max = max(worst, abs(value - exact)), max(calls_max, g.calls)
        print(f"{name:24} erreur : {abs(value - exact):.1e}   évaluations : {g.calls}")
    achieved = bool(worst < TARGET and calls_max <= 10)
    if calls_max > 10:
        print(f"❌ {calls_max} évaluations : 10 au plus.")
    wbm.check("M02a.25", achieved, computed=True)'''

M02A_25 = Ex(
    "M02a.25", "🏆", 3, 30, "Défi : la meilleure précision avec dix évaluations de la fonction",
    "calculer trois intégrales à $10^{-8}$ près en n'évaluant chaque fonction que dix fois au plus.",
    "fiche §3 et §5 ; Ex M02a.16 et M02a.17", tracks="C",
    body="""Écris `best_integral(f, a, b)`, qui approche $\\int_a^b f$ en appelant `f` **au plus 10 fois**. **Objectif** : une erreur inférieure à $10^{-8}$ sur chacune des trois intégrales de la cellule fournie (comparées à `quad`, très précis). La cellule de vérification compte les appels.

Simpson avec 8 intervalles (9 évaluations) donne des erreurs de l'ordre de $10^{-5}$ : loin du compte. Il faut une idée de plus. Pistes, de la plus simple à la plus efficace (`04_indices.md` les détaille) :
1. combiner deux résultats de Simpson, avec 4 et 8 intervalles, pour annuler le terme d'erreur principal (tous les points de l'un sont parmi ceux de l'autre) ;
2. renoncer aux points régulièrement espacés : il existe des points et des poids **choisis** pour être exacts sur des polynômes de degré bien plus élevé (cherche « quadrature de Gauss-Legendre » ; `np.polynomial.legendre.leggauss(n)` donne ces points et ces poids sur $[-1 ; 1]$, à ramener sur $[a ; b]$ par un changement de variable affine, §3).

Dans ta copie : quelle meilleure erreur obtiens-tu sur chaque intégrale, avec quelle méthode ? Pourquoi la troisième est-elle la plus difficile pour les méthodes à points réguliers ?""",
    given=M02A_25_GIVEN,
    todo='''def best_integral(f, a, b):
    """Approximate ∫_a^b f with at most 10 calls of f."""
    raise NotImplementedError("10 évaluations au plus : une combinaison de Simpson, ou des points de Gauss")''',
    check=M02A_25_CHECK,
    solution='''def best_integral(f, a, b):
    """Approximate ∫_a^b f with at most 10 calls of f: Gauss-Legendre quadrature with 10 points."""
    nodes, weights = np.polynomial.legendre.leggauss(10)        # exact for polynomials of degree up to 19 on [-1, 1]
    half, middle = (b - a) / 2, (a + b) / 2                      # x = middle + half t maps [-1, 1] onto [a, b]
    return float(half * sum(w * f(middle + half * t) for t, w in zip(nodes, weights)))


worst = 0.0
for name, f, a, b in CHALLENGE:
    g = counted(f)
    value = best_integral(g, a, b)
    error = abs(value - quad(f, a, b, epsabs=1e-13, epsrel=1e-13)[0])
    worst = max(worst, error)
    print(f"{name:24} erreur : {error:.1e}   évaluations : {g.calls}")
print("objectif atteint :", worst < TARGET)''',
    record='''wbm.record("M02a.25", True,
           mistakes={"l'objectif n'est pas atteint : relis les pistes de l'énoncé et de 04_indices.md": False})''',
    note="Avec 10 points de Gauss-Legendre, les erreurs tombent à $3 \\times 10^{-13}$, $10^{-15}$ et $2 \\times "
         "10^{-9}$. La combinaison $\\frac{16 S_8 - S_4}{15}$ (piste 1, la méthode de Boole) donne environ $10^{-6}$ sur "
         "les deux premières, mais $4 \\times 10^{-5}$ sur la troisième. Les points de Gauss sont choisis pour que la "
         "formule soit exacte sur les polynômes de degré au plus 19 : avec le même nombre d'évaluations, c'est bien "
         "mieux que Simpson (degré 3). La troisième fonction, $\\sqrt{1 + x^3}$, a des dérivées d'ordre 4 et plus qui "
         "grandissent vite sur $[0 ; 2]$ : c'est elle qui limite les méthodes de Newton-Cotes (rectangles, trapèzes, "
         "Simpson, Boole).",
)

PART_A = Part("A", "Ta librairie : sommes de Riemann, trapèzes, Simpson, fonction de répartition et quantile",
              "Fiche §1, §2, §5 et §7. Les cinq fonctions de `mymath/integrate.py`, puis les mêmes calculs avec SciPy "
              "et SymPy.",
              given=TOOLS, exercises=[M02A_16, M02A_17, M02A_18, M02A_19])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §1, §2, §4 et §5. Quand la règle « ÷ 4, ÷ 16 » s'applique, et quand elle ne s'applique pas ; "
              "l'intégrale de Gauss par le calcul ; l'aire qui se remplit.",
              exercises=[M02A_20, M02A_21, M02A_22])

PART_C = Part("C", "Erreurs classiques, vérification et défi",
              "Fiche §1, §2, §3 et §5. Trois erreurs à trouver, une primitive vérifiée par SymPy, puis le défi des dix "
              "évaluations.",
              exercises=[M02A_23, M02A_24, M02A_25])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M02a.1 à M02a.10, M02a.13 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M02a · Intégrales et densités — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m02a_integrales_densites/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M02a`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M02a · Intégrales et densités — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : sommes de Riemann, primitives, intégrales et aires, "
               "intégration par parties et changement de variable, intégrales impropres, trapèzes et Simpson, "
               "densités, probabilités, fonctions de répartition et quantiles, AUC.\n"
               "- Écrire les cinq fonctions de `mymath/integrate.py` et les tester, puis comparer avec SciPy et SymPy.\n"
               "- Prédire l'effet d'un pas divisé par 2, approcher l'intégrale de Gauss, dessiner l'aire qui se "
               "remplit, chasser des erreurs de calcul intégral, vérifier une primitive, relever le défi des dix "
               "évaluations.\n\n"
               "**Rappel express.** $\\int_a^b f = F(b) - F(a)$ avec $F' = f$. $h = \\frac{b - a}{n}$ ; trapèzes : "
               "$h\\big(\\frac{f_0}{2} + f_1 + \\cdots + \\frac{f_n}{2}\\big)$ ; Simpson ($n$ pair) : $\\frac{h}{3}(f_0 + "
               "4f_1 + 2f_2 + \\cdots + 4f_{n-1} + f_n)$. Densité : $f \\ge 0$, $\\int f = 1$, $P(a \\le X \\le b) = "
               "\\int_a^b f$ ; $F(x) = P(X \\le x)$ ; quantile $q_p$ : $F(q_p) = p$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Calcules-tu une intégrale avec une primitive, et sais-tu la distinguer d'une aire géométrique ?\n"
               "2. Sais-tu programmer les rectangles, les trapèzes et Simpson, et prévoir leur erreur ?\n"
               "3. Passes-tu d'une densité à des probabilités, à la fonction de répartition et aux quantiles ?\n\n"
               "**La suite** : M02b, les variables aléatoires et les lois usuelles, puis M02c, avant le chapitre 2 de "
               "workbookIA.")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter=CHAPTER) if kind == "exercise" else setup_cell(kind))
    cells += objectives_cell()
    cells += paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO,
                         learner_context="from fractions import Fraction   # Fraction(5, 9) is accepted too, as \"5/9\"\n"
                                         "import sympy as sp\n"
                                         "x = sp.Symbol(\"x\")                  # an expression typed without quotes works too")
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
