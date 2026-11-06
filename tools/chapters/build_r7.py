#!/usr/bin/env python
"""Build the two notebooks of chapter R7 from a single source (used by Claude).

    python tools/chapters/build_r7.py
    python tools/run_all_notebooks.py chapitres/r7_limites_derivation/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/r7_limites_derivation/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ R7.1 to R7.11, 🔗 R7.15); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer nor the expression to type. A limit is answered by a
number or "+oo" / "-oo", a derivative by an expression between quotes, a tangent y = mx + p by the list [m, p], a
set of points by a list in increasing order.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "R7"
FOLDER = "chapitres/r7_limites_derivation"

X = 'kind="expr", variables=("x",)'
INF = "math.inf"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("R7.1", "Limites en l'infini des fonctions de référence", [
        ("a", "a number", "5.0", 'decimals=2, mistakes={"3/x tend vers 0 : il ne reste rien à retirer de 5": 2}'),
        ("b", "a number, or \"+oo\" / \"-oo\"", INF,
         'decimals=2, mistakes={"∞ − ∞ est une forme indéterminée, pas 0 : mets le terme de plus haut degré en facteur": 0}'),
        ("c", "a number", "2.0",
         'decimals=2, mistakes={"en l\'infini, ce sont les termes de plus haut degré qui comptent, pas les constantes": '
         '{-0.33, 0.33}}'),
        ("d", "a number", "0.0",
         'decimals=2, mistakes={"le degré du dénominateur est plus grand que celui du numérateur": math.inf, '
         '"en l\'infini, les termes de plus haut degré décident, pas les constantes": {0.5, -0.5}, '
         '"∞/∞ est une forme indéterminée, pas 1 : compare les degrés du numérateur et du dénominateur": 1}'),
        ("e", "a number", "1.0",
         'decimals=2, mistakes={"e^(−2x) tend vers 0, mais un terme constant s\'y ajoute": 0}'),
        ("f", "a number", "0.0",
         'decimals=2, mistakes={"croissances comparées : l\'exponentielle l\'emporte sur toute puissance": math.inf, '
         '"∞/∞ est une forme indéterminée, pas 1 : croissances comparées": 1}'),
        ("g", "a number, or \"+oo\" / \"-oo\"", INF,
         'decimals=2, mistakes={"croissances comparées : toute puissance de x, même √x, l\'emporte sur ln x": 0}'),
        ("h", "a number, or \"+oo\" / \"-oo\"", f"-{INF}",
         'decimals=2, mistakes={"quand x est négatif, x³ l\'est aussi : regarde le signe du terme dominant": math.inf}'),
    ]),
    Paper("R7.2", "Limites et asymptotes de fonctions rationnelles", [
        ("a", "a number", "3.0",
         'decimals=2, mistakes={"en l\'infini, les termes de plus haut degré décident, pas les constantes": -2}'),
        ("b", "a number, or \"+oo\" / \"-oo\"", f"-{INF}",
         'decimals=2, mistakes={"en −1, le dénominateur s\'annule mais pas le numérateur : la limite n\'est pas finie": '
         '{-5, 0}}'),
        ("c", "a number, or \"+oo\" / \"-oo\"", INF,
         'decimals=2, mistakes={"en −1, le dénominateur s\'annule mais pas le numérateur : la limite n\'est pas finie '
         '(et regarde son signe à gauche)": {-5, 0}}'),
        ("d", "a list [a, L]", "[-1, 3]",
         'mistakes={"l\'asymptote verticale est là où le dénominateur s\'annule, pas le numérateur": [2 / 3, 3], '
         '"la liste est [a, L] : d\'abord l\'abscisse de l\'asymptote verticale": [3, -1]}'),
        ("e", "a number", "5.0",
         'decimals=2, mistakes={"0/0 est une forme indéterminée, pas une limite : factorise le numérateur": 0, '
         '"après la factorisation, la limite se calcule en remplaçant x par 2": 3}'),
        ("f", "True or False", "False",
         'mistakes={"le numérateur s\'annule aussi en 2 : factorise avant de conclure": True}'),
        ("g", "a list (increasing order)", "[-3, 3]",
         'mistakes={"x² − 9 = 0 a deux solutions": [3], "x² = 9 : prends la racine carrée": [-9, 9]}'),
        ("h", "a number, or \"+oo\" / \"-oo\"", INF,
         'decimals=2, mistakes={"en 3, le dénominateur s\'annule mais pas le numérateur : la limite n\'est pas finie": '
         '{21, 2, 0}}'),
    ]),
    Paper("R7.3", "Taux d'accroissement et nombre dérivé", [
        ("a", "a number", "22.5",
         'decimals=2, mistakes={"une vitesse moyenne : la distance parcourue divisée par la durée, 0,5 s": 11.25, '
         '"la distance parcourue entre t = 2 et t = 2,5, pas depuis le départ": 62.5}'),
        ("b", "a number", "20.5",
         'decimals=2, mistakes={"divise la distance parcourue par la durée, 0,1 s": 2.05}'),
        ("c", "an expression in h, as text", '"20 + 5*h"',
         'kind="expr", variables=("h",), expanded=True, mistakes={"le taux dépend encore de h : garde-le dans ton expression": "20", '
         '"développe (2 + h)² en entier : il a trois termes": "5*h"}'),
        ("d", "a number", "20.0",
         'decimals=2, mistakes={"c\'est une vitesse moyenne ; la vitesse instantanée est la limite du taux quand la '
         'durée tend vers 0": {22.5, 20.5}}'),
        ("e", "a number", "14.0",
         'decimals=2, mistakes={"un taux : la variation du coût divisée par le nombre de pièces ajoutées": 28}'),
        ("f", "a number", "13.0",
         'decimals=2, mistakes={"c\'est un coût moyen entre deux quantités ; le coût marginal est la limite du taux en '
         '10": 14, "le coût marginal est une pente, pas le coût C(10)": 180}'),
        ("g", "a number", "3.0",
         'decimals=2, mistakes={"le taux d\'une fonction affine est sa pente, pas son ordonnée à l\'origine": 7}'),
        ("h", "a number", "2.5",
         'decimals=2, mistakes={"h est négatif : on divise par −0,5, pas par 0,5": -2.5}'),
    ]),
    Paper("R7.4", "Équation de la tangente", [
        ("a", "a list [m, p]", "[3, -16]",
         'mistakes={"p n\'est pas f(4) : développe f(4) + f′(4)(x − 4)": [3, -4], '
         '"p = f(a) − f′(a) × a : vérifie le signe": [3, 8], "p = f(a) − f′(a) × a : n\'oublie pas f(a)": [3, -12]}'),
        ("b", "a list [m, p] (3 decimals)", "[math.e, 0.0]",
         'decimals=3, mistakes={"la pente en 1 est e¹, pas 1": [1, math.e - 1], '
         '"p = f(a) − f′(a) × a : n\'oublie pas f(a)": [math.e, -math.e]}'),
        ("c", "a list [m, p] (3 decimals)", "[0.5, math.log(2) - 1]",
         'decimals=3, mistakes={"p = f(2) − f′(2) × 2 : f(2) = ln 2": [0.5, -1], '
         '"la pente de ln en 2 est 1/2, pas ln 2": [math.log(2), math.log(2) - 2 * math.log(2)]}'),
        ("d", "a list [m, p]", "[0.25, 1.0]",
         'decimals=2, mistakes={"la dérivée de √x est 1/(2√x), pas 1/√x": [0.5, 0], '
         '"p = f(a) − f′(a) × a : n\'oublie pas f(a)": [0.25, -1]}'),
        ("e", "a number (2 decimals)", "2.05",
         'decimals=2, mistakes={"remplace x par 4,2 dans l\'équation de la tangente de d)": 1.05, '
         '"c\'est la valeur en 4 ; on demande celle de la tangente en x = 4,2": 2}'),
        ("f", "a number (5 decimals)", "round(2.05 - math.sqrt(4.2), 5)",
         'decimals=5, mistakes={"approximation moins vraie valeur, dans cet ordre": -round(2.05 - math.sqrt(4.2), 5)}'),
        ("g", "a number", "2.5",
         'decimals=2, mistakes={"une tangente horizontale a une pente nulle : résous f′(x) = 0, pas f(x) = 0": 5}'),
        ("h", "a fraction, as text", "Fraction(2, 3)",
         'kind="fraction", mistakes={"c\'est l\'ordonnée à l\'origine de la tangente ; on demande où elle coupe l\'axe '
         'des abscisses (y = 0)": "-2"}'),
    ]),
    Paper("R7.5", "Dériver les fonctions usuelles", [
        ("a", "an expression in x, as text", '"7*x**6"',
         X + ', mistakes={"l\'exposant descend devant, et diminue de 1": "7*x**7"}'),
        ("b", "an expression in x, as text", '"12*x**5 - 21*x**2 + 1"',
         X + ', mistakes={"la dérivée de x est 1, pas 0": "12*x**5 - 21*x**2", '
         '"chaque exposant diminue de 1 après être descendu devant": "12*x**6 - 21*x**3 + x"}'),
        ("c", "an expression in x, as text", '"-3/x**4"',
         X + ', mistakes={"l\'exposant diminue de 1, aussi quand il est négatif": "-3/x**2", '
         '"1/x³ n\'est pas une puissance positive : écris-la x^(−3)": "1/(3*x**2)"}'),
        ("d", "an expression in x, as text", '"3*sqrt(x)/2"',
         X + ', mistakes={"x√x n\'est pas √x : écris-le x^(3/2)": "1/(2*sqrt(x))", '
         '"x√x est un produit, pas une somme : écris-le x^(3/2)": "1/(2*sqrt(x)) + 1"}'),
        ("e", "an expression in x, as text", '"2/(3*x**(1/3))"',
         X + ', mistakes={"l\'exposant diminue de 1 : il ne gagne pas 1": "2/3*x**(5/3)"}'),
        ("f", "an expression in x, as text", '"3*exp(x) - 4/x"',
         X + ', mistakes={"(ln x)′ = 1/x : c\'est 1/x qui a pour dérivée −1/x²": "3*exp(x) + 4/x**2", '
         '"une constante multiplicative reste devant": "exp(x) - 1/x"}'),
        ("g", "an expression in x, as text", '"1/x"',
         X + ', mistakes={"ln(5x) = ln 5 + ln x, et ln 5 est une constante": "1/(5*x)", '
         '"ln(5x) = ln 5 + ln x : la constante ln 5 disparaît en dérivant, le 5 ne sort pas": "5/x"}'),
        ("h", "an expression in x, as text", '"exp(x + 2)"',
         X + ', mistakes={"e^(x + 2) n\'est pas eˣ : c\'est une constante fois eˣ (R6)": "exp(x)"}'),
    ]),
    Paper("R7.6", "Dériver des produits et des quotients", [
        ("a", "an expression in x, as text", '"exp(x)*log(x) + exp(x)/x"',
         X + ', mistakes={"la dérivée d\'un produit n\'est pas le produit des dérivées": "exp(x)/x", '
         '"(uv)′ = u′v + uv′ : il manque un des deux termes": "exp(x)*log(x)"}'),
        ("b", "an expression in x, as text", '"9*x**2 - 4*x + 3"',
         X + ', mistakes={"la dérivée d\'un produit n\'est pas le produit des dérivées": "6*x"}'),
        ("c", "an expression in x, as text", '"log(x)/(2*sqrt(x)) + 1/sqrt(x)"',
         X + ', mistakes={"la dérivée d\'un produit n\'est pas le produit des dérivées": "1/(2*x**(3/2))"}'),
        ("d", "an expression in x, as text", '"9/(2*x + 1)**2"',
         X + ', mistakes={"u′v − uv′, dans cet ordre, au numérateur": "-9/(2*x + 1)**2", '
         '"la dérivée d\'un quotient n\'est pas le quotient des dérivées": "1/2", '
         '"le dénominateur est v², pas v": "9/(2*x + 1)"}'),
        ("e", "an expression in x, as text", '"(1 - x**2)/(x**2 + 1)**2"',
         X + ', mistakes={"u′v − uv′, dans cet ordre, au numérateur": "(x**2 - 1)/(x**2 + 1)**2", '
         '"la dérivée d\'un quotient n\'est pas le quotient des dérivées": "1/(2*x)"}'),
        ("f", "an expression in x, as text", '"x*exp(x)/(x + 1)**2"',
         X + ', mistakes={"u′v − uv′, dans cet ordre, au numérateur": "-x*exp(x)/(x + 1)**2", '
         '"la dérivée d\'un quotient n\'est pas le quotient des dérivées": "exp(x)"}'),
        ("g", "a number (3 decimals)", "round(math.e, 3)",
         'decimals=3, mistakes={"ln 1 = 0 : un seul des deux termes s\'annule": 0, '
         '"la dérivée d\'un produit n\'est pas le produit des dérivées : reprends a)": 1}'),
        ("h", "an expression in x, as text", '"-(exp(x) + 1)/(exp(x) + x)**2"',
         X + ', mistakes={"(1/v)′ = −v′/v² : n\'oublie pas v′ au numérateur": "-1/(exp(x) + x)**2", '
         '"la dérivée de 1/v n\'est pas 1/v′": "1/(exp(x) + 1)", "(1/v)′ = −v′/v² : un signe moins": '
         '"(exp(x) + 1)/(exp(x) + x)**2"}'),
    ]),
    Paper("R7.7", "Dériver des composées", [
        ("a", "an expression in x, as text", '"12*x*(2*x**2 - 1)**2"',
         X + ', mistakes={"multiplie par la dérivée de l\'étage intérieur": "3*(2*x**2 - 1)**2"}'),
        ("b", "an expression in x, as text", '"-2*exp(-x/5)"',
         X + ', mistakes={"multiplie par la dérivée de l\'étage intérieur −x/5": "10*exp(-x/5)", '
         '"l\'étage intérieur −x/5 a une dérivée négative": "2*exp(-x/5)"}'),
        ("c", "an expression in x, as text", '"3/(3*x + 2)"',
         X + ', mistakes={"(ln u)′ = u′/u : multiplie par la dérivée de l\'étage intérieur": "1/(3*x + 2)"}'),
        ("d", "an expression in x, as text", '"3*x**2/(2*sqrt(x**3 + 1))"',
         X + ', mistakes={"multiplie par la dérivée de l\'étage intérieur x³ + 1": "1/(2*sqrt(x**3 + 1))"}'),
        ("e", "an expression in x, as text", '"exp(sqrt(x))/(2*sqrt(x))"',
         X + ', mistakes={"multiplie par la dérivée de l\'étage intérieur √x": "exp(sqrt(x))"}'),
        ("f", "an expression in x, as text", '"1/(x*log(x))"',
         X + ', mistakes={"(ln u)′ = u′/u : ici u = ln x, et u′ n\'est pas 1": "1/log(x)"}'),
        ("g", "an expression in x, as text", '"-(2*x + 1)/(x**2 + x)**2"',
         X + ', mistakes={"multiplie par la dérivée de l\'étage intérieur": "-1/(x**2 + x)**2", '
         '"(u^(−1))′ = −u^(−2) × u′ : un signe moins": "(2*x + 1)/(x**2 + x)**2"}'),
        ("h", "a fraction, as text", "Fraction(4, 3)",
         'kind="fraction", mistakes={"(ln u)′ = u′/u : multiplie par u′ avant de remplacer x par 1": "1/3"}'),
    ]),
    Paper("R7.8", "Variations et tableau de variations", [
        ("a", "an expression in x, as text", '"4*x**3 - 12*x**2"',
         X + ', mistakes={"la dérivée de la constante 10 est 0, et chaque exposant diminue de 1": "4*x**3 - 12*x**2 + 10"}'),
        ("b", "a list (increasing order)", "[0, 3]",
         'mistakes={"4x³ − 12x² = 4x²(x − 3) : le facteur x² s\'annule aussi": [3]}'),
        ("c", "an interval, as text", '"]-oo ; 3]"',
         'kind="interval", mistakes={"f′ s\'annule en 0 sans changer de signe, et f continue de décroître après 0": '
         '"]-oo ; 0]", "regarde aussi le signe de f′ avant 0": "[0 ; 3]"}'),
        ("d", "an integer", "1",
         'mistakes={"un point où f′ s\'annule sans changer de signe n\'est pas un extremum": 2}'),
        ("e", "a number", "-17.0",
         'decimals=2, mistakes={"c\'est l\'abscisse du minimum ; on demande la valeur de f en ce point": 3, '
         '"f(0) n\'est pas un minimum : f décroît encore après 0": 10}'),
        ("f", "a number", "15.0",
         'decimals=2, mistakes={"sur un intervalle fermé, compare les valeurs aux bords et aux points où f′ s\'annule": '
         '10}'),
        ("g", "a number", "2.0",
         'decimals=2, mistakes={"vérifie ta résolution de g′(x) = 0 : remplace x par ta réponse dans 1 − 2/x": 0.5}'),
        ("h", "a number (3 decimals)", "round(2 - 2 * math.log(2), 3)",
         'decimals=3, mistakes={"c\'est l\'abscisse du minimum ; on demande la valeur de g en ce point": 2, '
         '"g(2) = 2 − 2 ln 2, avec ln et pas log₁₀": round(2 - 2 * math.log10(2), 3)}'),
    ]),
    Paper("R7.9", "Optimiser : la boîte de volume maximal", [
        ("a", "an interval, as text", '"]0 ; 5["',
         'kind="interval", mistakes={"en x = 0 ou x = 5, la boîte est plate : les bornes sont exclues": "[0 ; 5]", '
         '"deux découpes de x sont prises sur le côté de 10 cm : 10 − 2x doit rester positif": "]0 ; 8["}'),
        ("b", "an expression in x, as text", '"4*x**3 - 52*x**2 + 160*x"',
         X + ', expanded=True, mistakes={"développe (16 − 2x)(10 − 2x) avant de multiplier par x": "4*x**3 - 52*x**2 + 160"}'),
        ("c", "an expression in x, as text", '"12*x**2 - 104*x + 160"',
         X + ', mistakes={"chaque exposant diminue de 1 après être descendu devant": "12*x**3 - 104*x**2 + 160*x"}'),
        ("d", "a number", "2.0",
         'decimals=2, mistakes={"cette racine n\'est pas dans le domaine : la largeur 10 − 2x serait négative": '
         'round(20 / 3, 2)}'),
        ("e", "a number", "144.0",
         'decimals=2, mistakes={"le volume est V(x) au point trouvé, pas V′": 0}'),
        ("f", "a list", "[12, 6, 2]",
         'mistakes={"la longueur et la largeur perdent 2x, pas x": [14, 8, 2], '
         '"longueur, largeur, hauteur, dans cet ordre": [6, 12, 2]}'),
    ]),
    Paper("R7.10", "La règle de la chaîne en série : trois étages, et l'ordre qui compte", [
        ("a", "an expression in x, as text", '"6*x*(x**2 + 1)**2*exp((x**2 + 1)**3)"',
         X + ', mistakes={"trois étages : il manque la dérivée du plus intérieur, x² + 1": '
         '"3*(x**2 + 1)**2*exp((x**2 + 1)**3)"}'),
        ("b", "an expression in x, as text", '"1/(2*x*sqrt(log(x)))"',
         X + ', mistakes={"multiplie par la dérivée de l\'étage intérieur ln x": "1/(2*sqrt(log(x)))"}'),
        ("c", "an expression in x, as text", '"3*exp(x)*(2 + exp(x))**2"',
         X + ', mistakes={"multiplie par la dérivée de l\'étage intérieur 2 + eˣ": "3*(2 + exp(x))**2"}'),
        ("d", "an expression in x, as text", '"4/(2*x + 1)"',
         X + ', mistakes={"ln(a²) = 2 ln a : le 2 de l\'exposant reste devant": "2/(2*x + 1)", '
         '"(ln u)′ = u′/u, avec u = (2x + 1)² : calcule u′ en entier, avec la règle de la chaîne": "1/(2*x + 1)**2"}'),
        ("e", "a number", "20.0",
         'decimals=2, mistakes={"multiplie par la dérivée de l\'étage intérieur x² − 3, en x = 2": 5}'),
        ("f", "a number (3 decimals)", "round((2 + math.e) / (1 + math.e), 3)",
         'decimals=3, mistakes={"(ln u)′ = u′/u : multiplie par la dérivée de l\'étage intérieur": '
         'round(1 / (1 + math.e), 3)}'),
        ("g", "a number", "0.5",
         'decimals=2, mistakes={"l\'exposant 2x a pour dérivée 2 : un étage de plus": 0.25}'),
        ("h", "a list (3 decimals)", "[2 * math.exp(4), 4 * math.exp(4)]",
         'decimals=3, mistakes={"(eˣ)² = e^(2x) : multiplie par la dérivée de 2x": [math.exp(4), 4 * math.exp(4)], '
         '"e^(x²) : multiplie par la dérivée de x²": [2 * math.exp(4), math.exp(4)]}'),
    ]),
    Paper("R7.11", "Dériver par rapport à une lettre, les autres fixées : A e^(kt), π r² h, ½ m v²", [
        ("a", "an expression in A, k, t, as text", '"A*k*exp(k*t)"',
         'kind="expr", variables=("A", "k", "t"), mistakes={"l\'exposant kt a pour dérivée k par rapport à t": '
         '"A*exp(k*t)", "par rapport à t, la lettre A est une constante qui reste devant": "k*exp(k*t)"}'),
        ("b", "an expression in A, k, t, as text", '"A*t*exp(k*t)"',
         'kind="expr", variables=("A", "k", "t"), mistakes={"par rapport à k, t est une constante : la dérivée de kt '
         'est t": "A*k*exp(k*t)", "l\'exposant kt dépend de k : multiplie par sa dérivée": "A*exp(k*t)"}'),
        ("c", "an expression in A, k, t, as text", '"exp(k*t)"',
         'kind="expr", variables=("A", "k", "t"), mistakes={"par rapport à A, N est de la forme A × constante": '
         '"A*exp(k*t)"}'),
        ("d", "an expression in r, h, as text", '"2*pi*r*h"',
         'kind="expr", variables=("r", "h"), mistakes={"h est une constante : elle reste en facteur": "2*pi*r", '
         '"la dérivée de r² est 2r, pas r²": "pi*r**2"}'),
        ("e", "an expression in r, h, as text", '"pi*r**2"',
         'kind="expr", variables=("r", "h"), mistakes={"c\'est V elle-même : dérive-la par rapport à h": '
         '"pi*r**2*h", "par rapport à h, le facteur r² ne se dérive pas": "2*pi*r"}'),
        ("f", "a number (2 decimals)", "round(60 * math.pi, 2)",
         'decimals=2, mistakes={"remplace r et h dans dV/dr, pas dans V": round(90 * math.pi, 2), '
         '"π fait partie de la formule": 60}'),
        ("g", "an expression in m, v, as text", '"m*v"',
         'kind="expr", variables=("m", "v"), mistakes={"le facteur 1/2 et m sont des constantes qui restent": "v", '
         '"la dérivée de v² est 2v, pas v": "m*v/2"}'),
        ("h", "an expression in m, v, as text", '"v**2/2"',
         'kind="expr", variables=("m", "v"), mistakes={"par rapport à m, v est une constante : on ne dérive pas v²": '
         '"m*v"}'),
    ]),
    Paper("R7.15", "Minimiser une fonction de coût donnée par une formule : dériver, annuler, vérifier", [
        ("a", "an expression in a, as text", '"2 - 8/a**2"',
         'kind="expr", variables=("a",), mistakes={"(8/a)′ = 8 × (−1/a²) : un signe moins": "2 + 8/a**2", '
         '"(1/a)′ = −1/a², pas ln a ni 1/a": "2 - 8/a"}'),
        ("b", "a number", "2.0",
         'decimals=2, mistakes={"a > 0 : la solution négative n\'est pas dans le domaine": -2, '
         '"tu as trouvé a², pas a": 4}'),
        ("c", "a number", "9.0",
         'decimals=2, mistakes={"remplace a par a* dans E, pas dans E′": 0, "n\'oublie pas le terme constant 1": 8, '
         '"c\'est a*, l\'abscisse du minimum ; on demande la valeur de E en ce point": 2}'),
        ("d", "a number", "-6.0",
         'decimals=2, mistakes={"(8/a)′ = −8/a² : un signe moins": 10}'),
        ("e", "a number (3 decimals)", "round(math.log(2), 3)",
         'decimals=3, mistakes={"tu as trouvé 2t, pas t": round(math.log(4), 3), '
         '"(e^(−t))′ = −e^(−t) : un signe moins": round(-math.log(2), 3)}'),
        ("f", "a number", "4.0",
         'decimals=2, mistakes={"remplace t par t* dans L, pas dans L′": 0, "c\'est L(0) : on demande L en t*": 5, '
         '"c\'est t*, l\'abscisse du minimum ; on demande la valeur de L en ce point": round(math.log(2), 2)}'),
        ("g", "a list (3 decimals)", "[math.exp(math.log(2) - 0.1) + 4 * math.exp(-(math.log(2) - 0.1)), "
                                     "math.exp(math.log(2) + 0.1) + 4 * math.exp(-(math.log(2) + 0.1))]",
         'decimals=3'),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math
from fractions import Fraction'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ R7.1 à R7.11, 🔗 R7.15)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un nombre avec un point décimal, `-1.5`, arrondi comme le demande la question ; une limite infinie "
               "par `\"+oo\"` ou `\"-oo\"` ;\n"
               "- une fraction exacte entre guillemets, `\"5/7\"` ;\n"
               "- une expression entre guillemets, `\"3*x**2 - 1\"` (`*` pour multiplier, `**` pour la puissance ; "
               "`exp(x)`, `log(x)` pour ln x, `sqrt(x)`, `pi`) ;\n"
               "- un intervalle entre guillemets, `\"[-2 ; 4[\"` (`-oo` et `+oo` pour l'infini) ;\n"
               "- une liste de nombres entre crochets (une tangente $y = mx + p$ par `[m, p]`) ; vrai ou faux par "
               "`True` ou `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (R7.17 to R7.19)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from wbm.nbtools import checked, drawn, run_pytest_group


def counted(f, limit=10_000):
    """f, but a loop that calls it more than `limit` times stops with an error (a bisection needs far fewer)."""
    calls = 0

    def wrapped(x):
        nonlocal calls
        calls += 1
        if calls > limit:
            raise RuntimeError(f"f appelée plus de {limit} fois : ta boucle s'arrête-t-elle ? (tol, max_iter)")
        return f(x)

    return wrapped


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

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="R7")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme dans les chapitres précédents). Ouvre ta copie "
         "`mon_travail/mymath/deriv.py`, lis la docstring de la fonction en entier, remplace la ligne "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Comme dans tous les chapitres R0 à R9, Python pur et le module "
         "`math` seulement (un test le vérifie) : `f` est une fonction que tu reçois en argument, et tu l'appelles "
         "comme n'importe quelle fonction (workbookIA 0A §100.5.3). Les autres tests comparent tes résultats à des "
         "valeurs exactes, à SymPy et à SciPy.")

WRONG_ERROR = "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)"
OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "TypeError", "ZeroDivisionError"]


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of deriv.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_r7_deriv.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_r7_deriv.py", "{keyword}", impl="ref")')]


R7_17 = Ex(
    "R7.17", "🔨", 1, 15, "Le taux d'accroissement · `difference_quotient`",
    "programmer le taux d'accroissement d'une fonction reçue en argument, et s'en servir pour estimer une dérivée.",
    "fiche §3", tracks="C, E", mymath="deriv.py",
    body=HOWTO + """

Écris `difference_quotient(f, a, h)` dans `mon_travail/mymath/deriv.py` : le taux d'accroissement $\\frac{f(a + h) - f(a)}{h}$ de `f` entre `a` et `a + h`, en flottant. Un `h` négatif est permis ; un `h` nul lève une `ValueError`.

La vérification calcule :
- a) les taux de $\\sqrt{x}$ entre 4 et $4 + h$, pour $h = 1$, puis 0,1, puis 0,01 (une liste) ;
- b) le même taux pour $h = -0{,}01$ ;
- c) le nom de l'erreur levée pour $h = 0$ (avec `raised`, de la cellule des outils) ;
- d) le taux de $x \\mapsto x^x$ entre 1 et $1 + 10^{-6}$, une fonction que tu ne sais pas encore dériver.

Puis, dans ta copie : vers quel nombre les taux de a) semblent-ils aller, et quelle dérivée de la fiche le confirme ? Quelle valeur de la dérivée de $x^x$ en 1 devines-tu avec d) ? Vérifie-la par la règle de la chaîne, en écrivant $x^x = e^{x \\ln x}$ (fiche §7).""",
    todo=LOAD_LEARNER,
    check='''with checked("R7.17a"):
    wbm.check("R7.17a", [mymath.deriv.difference_quotient(math.sqrt, 4, h) for h in (1, 0.1, 0.01)], computed=True)
with checked("R7.17b"):
    wbm.check("R7.17b", mymath.deriv.difference_quotient(math.sqrt, 4, -0.01), computed=True)
with checked("R7.17c"):
    wbm.check("R7.17c", raised(mymath.deriv.difference_quotient, math.sqrt, 4, 0), computed=True)
with checked("R7.17d"):
    wbm.check("R7.17d", mymath.deriv.difference_quotient(lambda x: x ** x, 1, 1e-6), computed=True)''',
    solution=LOAD_REF + '''
difference_quotient = mymath.deriv.difference_quotient
print("a)", [difference_quotient(math.sqrt, 4, h) for h in (1, 0.1, 0.01)])
print("b)", difference_quotient(math.sqrt, 4, -0.01), " c)", raised(difference_quotient, math.sqrt, 4, 0))
print("d)", difference_quotient(lambda x: x ** x, 1, 1e-6))''',
    record=f'''wbm.record("R7.17a", [(math.sqrt(4 + h) - 2) / h for h in (1, 0.1, 0.01)], decimals=4,
           mistakes={{"le taux divise la différence f(a + h) − f(a) par h": [math.sqrt(4 + h) - 2 for h in (1, 0.1, 0.01)],
                     "le taux est (f(a + h) − f(a)) / h, dans cet ordre": [(2 - math.sqrt(4 + h)) / h
                                                                          for h in (1, 0.1, 0.01)]}})
wbm.record("R7.17b", (math.sqrt(3.99) - 2) / -0.01, decimals=4,
           mistakes={{"h est négatif : divise par h tel quel (pas par sa valeur absolue), et calcule f(a + h) − f(a) dans "
                     "cet ordre": (math.sqrt(3.99) - 2) / 0.01}})
wbm.record("R7.17c", "ValueError",
           mistakes={{"h = 0 : lève une ValueError (raise) avant de diviser": {{"ZeroDivisionError", "aucune"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("R7.17d", ((1 + 1e-6) ** (1 + 1e-6) - 1) / 1e-6, decimals=3)''',
    after=tests_cells("test_difference_quotient_ or test_deriv_uses"),
    note="Les taux de a) valent 0,2361, 0,2485 et 0,2498 : ils se rapprochent de $(\\sqrt{x})'(4) = \\frac{1}{2\\sqrt{4}} "
         "= 0{,}25$, par en dessous ; celui de b), pour $h < 0$, est juste au-dessus. Pour d), $x^x = e^{x \\ln x}$ a "
         "pour dérivée $(\\ln x + 1)\\,x^x$, qui vaut 1 en $x = 1$ : le taux 1,000001 le montrait.",
)

R7_18 = Ex(
    "R7.18", "🔨", 2, 20, "La tangente à partir de f et de sa dérivée · `tangent_line`",
    "programmer l'équation de la tangente à partir d'une fonction et de sa dérivée, reçues en arguments.",
    "fiche §4", tracks="C", mymath="deriv.py",
    body="""Écris `tangent_line(f, df, a)` : le couple `(m, c)` tel que la tangente à la courbe de `f` au point d'abscisse `a` soit $y = mx + c$, `df` étant la dérivée de `f` (fiche §4 : développe $y = f(a) + f'(a)(x - a)$). Quand `f`, `df` et `a` donnent des entiers, le résultat doit rester en entiers : pas de `float(...)` ni de division.

La vérification calcule :
- a) la tangente de ln en $e$ (`math.e`), une liste `[m, c]` ;
- b) la tangente de $x \\mapsto x^3 - x$ en 2, de dérivée $3x^2 - 1$ ;
- c) les types des deux nombres de b), en texte (`"int int"` si ce sont deux entiers) ;
- d) la tangente de exp en −1.

Puis, dans ta copie : où la tangente de d) coupe-t-elle l'axe des abscisses ? Recommence pour la tangente de exp en un autre point $a$ : que remarques-tu ?""",
    todo=LOAD_LEARNER,
    check='''with checked("R7.18a"):
    wbm.check("R7.18a", list(mymath.deriv.tangent_line(math.log, lambda x: 1 / x, math.e)), computed=True)
with checked("R7.18b"):
    wbm.check("R7.18b", list(mymath.deriv.tangent_line(lambda x: x ** 3 - x, lambda x: 3 * x ** 2 - 1, 2)),
              computed=True)
with checked("R7.18c"):
    result = mymath.deriv.tangent_line(lambda x: x ** 3 - x, lambda x: 3 * x ** 2 - 1, 2)
    wbm.check("R7.18c", " ".join(type(value).__name__ for value in result), computed=True)
with checked("R7.18d"):
    wbm.check("R7.18d", list(mymath.deriv.tangent_line(math.exp, math.exp, -1)), computed=True)''',
    solution=LOAD_REF + '''
tangent_line = mymath.deriv.tangent_line
print("a)", tangent_line(math.log, lambda x: 1 / x, math.e))
b = tangent_line(lambda x: x ** 3 - x, lambda x: 3 * x ** 2 - 1, 2)
print("b)", b, " c)", " ".join(type(value).__name__ for value in b))
print("d)", tangent_line(math.exp, math.exp, -1))''',
    record='''wbm.record("R7.18a", [1 / math.e, 0.0], decimals=4,
           mistakes={"c = f(a) − m × a : vérifie le signe": [1 / math.e, 2.0],
                     "c n'est pas f(a) : développe f(a) + f′(a)(x − a)": [1 / math.e, 1.0]})
wbm.record("R7.18b", [11, -16],
           mistakes={"c n'est pas f(a) : développe f(a) + f′(a)(x − a)": [11, 6],
                     "c = f(a) − m × a : vérifie le signe": [11, 28]})
wbm.record("R7.18c", "int int",
           mistakes={"garde les entiers : pas de float(...) ni de division /": {"float float", "int float",
                                                                                "float int"}})
wbm.record("R7.18d", [math.exp(-1), 2 * math.exp(-1)], decimals=4,
           mistakes={"c = f(a) − m × a, avec a = −1 : vérifie le signe": [math.exp(-1), 0.0]})''',
    after=tests_cells("test_tangent_line_ or test_deriv_uses"),
    note="La tangente de ln en $e$ est $y = \\frac{x}{e}$ : elle passe par l'origine. La tangente de exp en $a$ est "
         "$y = e^a x + e^a(1 - a)$ ; elle coupe l'axe des abscisses en $x = a - 1$, "
         "toujours une unité à gauche du point de contact. En $a = -1$, c'est en −2.",
)

R7_19 = Ex(
    "R7.19", "🔨", 2, 25, "Trouver un zéro par dichotomie · `bisection`",
    "programmer la dichotomie, avec ses cas limites, et compter les étapes qu'elle demande.",
    "fiche §2 ; R6 §4", tracks="C, E", mymath="deriv.py",
    body="""Écris `bisection(f, a, b, tol=1e-10, max_iter=200)` (fiche §2) : tant que l'intervalle n'est pas plus court que `tol` (et au plus `max_iter` fois), coupe-le en deux et garde la moitié où le signe de `f` change ; renvoie le milieu du dernier intervalle. Si `f` vaut exactement 0 en `a`, en `b` ou en un milieu, renvoie ce point tout de suite ; la docstring dit aussi quand lever une `ValueError`. Dans la vérification, `counted(f)` (cellule des outils) arrête une boucle qui ne finirait jamais.

La vérification calcule :
- a) le zéro de $e^x - 3x$ sur $[0 \\;;\\; 1]$ ;
- b) le zéro de $\\ln x + x - 2$ sur $[1 \\;;\\; 2]$ ;
- c) le nom de l'erreur levée pour $x^2 + 1$ sur $[-1 \\;;\\; 1]$, puis d) pour $a = 2$ et $b = 1$ ;
- e) le résultat pour $x - 1$ sur $[1 \\;;\\; 3]$ ;
- f) si le zéro de $x^2 - 3$ sur $[0 \\;;\\; 2]$, trouvé avec `tol=1e-3`, est à moins de $10^{-3}$ de $\\sqrt{3}$.

Puis g), à la main (fiche §2) : partant d'un intervalle de longueur 1, combien de coupes faut-il pour qu'il mesure moins de $10^{-10}$, la valeur par défaut de `tol` ?""",
    todo=LOAD_LEARNER,
    check='''with checked("R7.19a"):
    wbm.check("R7.19a", mymath.deriv.bisection(counted(lambda x: math.exp(x) - 3 * x), 0, 1), computed=True)
with checked("R7.19b"):
    wbm.check("R7.19b", mymath.deriv.bisection(counted(lambda x: math.log(x) + x - 2), 1, 2), computed=True)
with checked("R7.19c"):
    wbm.check("R7.19c", raised(mymath.deriv.bisection, counted(lambda x: x ** 2 + 1), -1, 1), computed=True)
with checked("R7.19d"):
    wbm.check("R7.19d", raised(mymath.deriv.bisection, counted(lambda x: x), 2, 1), computed=True)
with checked("R7.19e"):
    wbm.check("R7.19e", mymath.deriv.bisection(counted(lambda x: x - 1), 1, 3), computed=True)
with checked("R7.19f"):
    root = mymath.deriv.bisection(counted(lambda x: x ** 2 - 3), 0, 2, tol=1e-3)
    wbm.check("R7.19f", bool(abs(root - math.sqrt(3)) < 1e-3), computed=True)''',
    solution=LOAD_REF + '''
bisection = mymath.deriv.bisection
print("a)", bisection(lambda x: math.exp(x) - 3 * x, 0, 1), " b)", bisection(lambda x: math.log(x) + x - 2, 1, 2))
print("c)", raised(bisection, lambda x: x ** 2 + 1, -1, 1), " d)", raised(bisection, lambda x: x, 2, 1))
print("e)", bisection(lambda x: x - 1, 1, 3), " f)", abs(bisection(lambda x: x ** 2 - 3, 0, 2, tol=1e-3) - math.sqrt(3)) < 1e-3)''',
    record=f'''from scipy.optimize import brentq
wbm.record("R7.19a", brentq(lambda x: math.exp(x) - 3 * x, 0, 1, xtol=1e-14), decimals=6)
wbm.record("R7.19b", brentq(lambda x: math.log(x) + x - 2, 1, 2, xtol=1e-14), decimals=6)
wbm.record("R7.19c", "ValueError",
           mistakes={{"f(a) et f(b) ont le même signe : lève une ValueError avant de chercher": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("R7.19d", "ValueError",
           mistakes={{"a ≥ b : lève une ValueError avant de chercher": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("R7.19e", 1.0, decimals=6)
wbm.record("R7.19f", True,
           mistakes={{"avec tol = 1e-3, le résultat doit être à moins de 1e-3 du zéro : relis ta boucle (la moitié "
                     "gardée, la condition d'arrêt, le milieu renvoyé) ; les tests ci-dessous disent quel cas pose "
                     "problème": False}})''',
    after=tests_cells("test_bisection_ or test_deriv_uses") + [
        ("md", "**g)** Le nombre de coupes, calculé à la main."),
        ("todo", "answer_R7_19g = ...  # g) an integer"),
        ("check", 'wbm.check("R7.19g", answer_R7_19g)'),
        ("solution", "answer_R7_19g = math.ceil(math.log2(1e10))\nprint(answer_R7_19g)"),
        ("record", 'wbm.record("R7.19g", 34, fractional="un nombre de coupes entier : le premier qui convient, pas un '
                   'arrondi", mistakes={"après ce nombre de coupes, l\'intervalle mesure encore plus de 10^(−10)": 33, '
                   '"le nombre de coupes vient de log₂, pas de log₁₀": 10})'),
    ],
    note="Le zéro de $e^x - 3x$ est 0,619061, celui de $\\ln x + x - 2$ est 1,557146. Il faut 34 coupes pour passer "
         "sous $10^{-10}$ : $2^{33} \\approx 8{,}6 \\times 10^9$ ne suffit pas, $2^{34} \\approx 1{,}7 \\times 10^{10}$ "
         "suffit. Si $f$ vaut exactement 0 en une borne, on la renvoie tout de suite ; sinon les deux signes stricts "
         "doivent être contraires.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: SymPy, prediction, experiments, plot (R7.20 to R7.23)
# ---------------------------------------------------------------------------
R7_20_GIVEN = '''x = sp.symbols("x")
proposals = [  # (function, a derivative proposed by a student)
    (x / (x + 2), 2 / (x + 2) ** 2),
    ((x ** 3 + 1) ** 2, 6 * x ** 2 * (x ** 3 + 1)),
    (sp.sqrt(x) * sp.exp(2 * x), sp.exp(2 * x) / (2 * sp.sqrt(x)) + sp.sqrt(x) * sp.exp(2 * x)),
]'''

R7_20 = Ex(
    "R7.20", "📦", 1, 15, "Vérifier ses dérivées avec `sympy.diff`",
    "calculer des dérivées, leurs zéros et une limite avec SymPy, et tester si deux dérivées sont égales.",
    "fiche §5 à §7 ; R0 (SymPy)", tracks="C, E",
    body="""SymPy (R0) dérive exactement : `sp.diff(expression, x)`. Deux écritures d'une même dérivée peuvent différer : pour tester si deux expressions sont égales, on regarde si leur différence **se simplifie en 0** (`sp.simplify(a - b) == 0`). `sp.solve(expression, x)` donne les solutions de `expression = 0`, et `sp.limit(expression, x, 0)` la limite quand $x$ tend vers 0.

- a) La dérivée de $(x^2 - 3)\\,e^{x}$, calculée par SymPy (`sp.exp`).
- b) La liste des points où cette dérivée s'annule, dans l'ordre croissant (des entiers Python : `int(...)`).
- c) La liste `proposals` (cellule ci-dessous) contient trois fonctions, chacune avec une dérivée proposée par un élève. Pour chacune, la dérivée proposée est-elle juste ? Une liste de trois booléens, dans l'ordre.
- d) $\\lim_{x \\to 0} \\frac{\\sqrt{x + 4} - 2}{x}$, avec `sp.limit` (`sp.sqrt`). De quel nombre dérivé de la fiche est-ce la limite ?""",
    given=R7_20_GIVEN,
    todo='''answer_R7_20a = ...  # a) a SymPy expression
answer_R7_20b = ...  # b) a list of integers, in increasing order
answer_R7_20c = ...  # c) a list of 3 booleans
answer_R7_20d = ...  # d) a SymPy number''',
    check='''for letter, answer in zip("abcd", [answer_R7_20a, answer_R7_20b, answer_R7_20c, answer_R7_20d]):
    wbm.check(f"R7.20{letter}", answer)''',
    solution='''answer_R7_20a = sp.diff((x ** 2 - 3) * sp.exp(x), x)
answer_R7_20b = sorted(int(value) for value in sp.solve(answer_R7_20a, x))
answer_R7_20c = [bool(sp.simplify(sp.diff(f, x) - proposed) == 0) for f, proposed in proposals]
answer_R7_20d = sp.limit((sp.sqrt(x + 4) - 2) / x, x, 0)
print(answer_R7_20a, answer_R7_20b, answer_R7_20c, answer_R7_20d, sep="\\n")''',
    record='''wbm.record("R7.20a", "(x**2 + 2*x - 3)*exp(x)", kind="expr", variables=("x",),
           mistakes={"des parenthèses : c'est tout le facteur (x² − 3) qui multiplie eˣ": "2*x - 3*exp(x)"})
wbm.record("R7.20b", [-3, 1], mistakes={"ce sont les zéros de la dérivée, pas ceux de la fonction": [-1, 1]})
wbm.record("R7.20c", [True, True, False],
           mistakes={"compare la dérivée de SymPy à la proposée avec sp.simplify(a - b) == 0, pas avec ==":
                         [False, True, False]})
wbm.record("R7.20d", Fraction(1, 4), kind="fraction",
           mistakes={"la limite quand x tend vers 0, pas vers l'infini": "0"})''',
    note="La dérivée de $(x^2 - 3)e^{x}$ est $(x^2 + 2x - 3)e^{x} = (x + 3)(x - 1)e^{x}$, nulle en −3 et en 1. "
         "Seule la troisième "
         "dérivée proposée est fausse : le produit $\\sqrt{x}\\,e^{2x}$ demande $2e^{2x}$ (règle de la chaîne) dans "
         "son second terme. La limite de d) est le nombre dérivé de $\\sqrt{x}$ en 4, $\\frac{1}{4}$ ; et `==` "
         "compare des écritures, pas des valeurs : il dit faux pour la première proposition, juste pourtant.",
)

R7_21_EXPERIMENT = '''functions = [("a) e^|x| en 0", lambda x: math.exp(abs(x)), 0),
             ("b) partie entière en 2", math.floor, 2),
             ("c) max(0, x)² en 0", lambda x: max(0, x) ** 2, 0)]
for name, f, a in functions:
    print(name)
    for sign, side in ((1, "h > 0"), (-1, "h < 0")):
        steps = [sign * 10.0 ** -k for k in range(1, 7)]
        rates = [(f(a + h) - f(a)) / h for h in steps]
        print(f"   {side} :", "   ".join(f"{rate + 0.0:.6g}" for rate in rates))   # + 0.0: no "-0"'''

R7_21 = Ex(
    "R7.21", "🔮", 2, 15,
    "Prédire : le taux d'accroissement a-t-il toujours une limite quand h tend vers 0 ?",
    "prévoir, pour une fonction avec un coin, une avec un saut et une avec un raccord lisse, si le taux "
    "d'accroissement a une limite des deux côtés.", "fiche §2 et §3",
    tracks="C", hypothesis=True,
    body="""Pour chacune des trois fonctions ci-dessous, l'expérience calcule le taux d'accroissement $\\frac{f(a + h) - f(a)}{h}$ au point $a$ indiqué, pour $h = 10^{-1}, 10^{-2}, \\dots, 10^{-6}$ (donc $h > 0$), puis pour les mêmes $h$ précédés d'un signe moins ($h < 0$). **Avant d'exécuter quoi que ce soit**, prédis :
- a) pour $f(x) = e^{\\lvert x \\rvert}$ en $a = 0$, les taux : 1 tendent vers 0 des deux côtés ; 2 tendent vers 1 quand $h > 0$ et vers −1 quand $h < 0$ ; 3 deviennent de plus en plus grands ;
- b) pour la partie entière $f(x) = \\lfloor x \\rfloor$ (`math.floor`, fiche §2) en $a = 2$, les taux **quand $h < 0$** : 1 tendent vers 0 ; 2 tendent vers 1 ; 3 deviennent de plus en plus grands ;
- c) pour $f(x) = \\big(\\max(0, x)\\big)^2$ en $a = 0$, les taux : 1 tendent vers 0 des deux côtés ; 2 tendent vers 1 quand $h > 0$ et vers 0 quand $h < 0$ ; 3 n'ont de limite d'aucun côté.

Écris tes trois prédictions, vérifie-les, puis lance l'expérience.""",
    todo='''prediction_R7_21a = ...  # a) 1, 2 or 3, written BEFORE running the experiment below
prediction_R7_21b = ...  # b) 1, 2 or 3
prediction_R7_21c = ...  # c) 1, 2 or 3''',
    check='''for letter, prediction in zip("abc", [prediction_R7_21a, prediction_R7_21b, prediction_R7_21c]):
    wbm.check(f"R7.21{letter}", prediction)''',
    record='''wbm.record("R7.21a", 2, prediction=True, choices=[1, 2, 3])
wbm.record("R7.21b", 3, prediction=True, choices=[1, 2, 3])
wbm.record("R7.21c", 1, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes trois prédictions écrites."),
        ("todo", guarded(R7_21_EXPERIMENT, ["prediction_R7_21a", "prediction_R7_21b", "prediction_R7_21c"],
                         "⏳ Écris d'abord tes trois prédictions, puis exécute à nouveau.")),
        ("solution", R7_21_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : laquelle des trois fonctions est dérivable en son point, et que "
               "vaut sa dérivée ? Pour la partie entière, que donnent les taux quand $h > 0$, et pourquoi un saut "
               "empêche-t-il toute dérivée ? Dessine l'allure des trois courbes près de leur point."),
    ],
    note="a) Les taux tendent vers 1 à droite et vers −1 à gauche : $e^{\\lvert x \\rvert}$ fait un coin en 0, comme "
         "$\\lvert x \\rvert$, et n'y est pas dérivable. b) Juste à gauche de 2, la partie entière vaut 1 : le taux "
         "vaut $\\frac{1 - 2}{h} = \\frac{1}{\\lvert h \\rvert}$ et grandit sans limite (à droite, il vaut 0) ; une "
         "fonction qui saute n'est pas dérivable, elle n'est même pas continue. c) Les taux valent $h$ à droite et 0 à "
         "gauche : ils tendent vers 0 des deux côtés. $\\big(\\max(0, x)\\big)^2$ est dérivable en 0, de dérivée 0, "
         "alors que $\\max(0, x)$ y fait un coin.",
)

R7_22 = Ex(
    "R7.22", "🔬", 2, 20, "Zoomer sur une courbe jusqu'à voir une droite",
    "mesurer l'écart entre une courbe et sa tangente sur des fenêtres de plus en plus étroites, et voir ce qu'un coin "
    "change.", "fiche §3 et §4 ; workbookIA 0A §100.8.3 (calcul vectorisé)", tracks="C, E",
    body="""Écris `max_gap(f, line, a, w)`, qui renvoie le plus grand écart $\\lvert f(x) - \\text{line}(x) \\rvert$ pour $x$ parcourant 1 001 points également espacés de $[a - w \\;;\\; a + w]$ (bornes comprises : `np.linspace`). `f` et `line` reçoivent un tableau NumPy et renvoient un tableau.

La vérification calcule, pour les quatre largeurs $w$ de `widths` (0,5 ; 0,1 ; 0,01 ; 0,001) :
- a) l'écart entre ln et sa tangente en 3, $y = \\frac{x}{3} + \\ln 3 - 1$, divisé par $w$ (une liste de quatre nombres) ;
- b) le même écart, divisé par $w^2$ ;
- c) l'écart entre $\\lvert x \\rvert$ et la droite $y = 0$ autour de 0, divisé par $w$.

Puis :
- d) vers quel nombre semblent tendre les rapports de b) ? (un nombre, 3 décimales)

Dans ta copie : que disent a) et b) de la vitesse à laquelle la courbe de ln se confond avec sa tangente ? Et c) : y a-t-il une droite qui « colle » à $\\lvert x \\rvert$ quand on zoome sur 0 ?""",
    given='''widths = np.array([0.5, 0.1, 0.01, 0.001])


def tangent22(x):
    """The tangent of ln at 3: y = x/3 + ln 3 − 1."""
    return x / 3 + math.log(3) - 1''',
    todo='''def max_gap(f, line, a, w):
    """The largest |f(x) − line(x)| for 1001 evenly spaced x in [a − w, a + w] (ends included)."""
    raise NotImplementedError("calcule l'écart sur la grille de np.linspace, puis son maximum")


answer_R7_22d = ...  # d) a number (3 decimals)''',
    check='''with checked("R7.22a"):
    wbm.check("R7.22a", [max_gap(np.log, tangent22, 3, w) / w for w in widths], computed=True)
with checked("R7.22b"):
    wbm.check("R7.22b", [max_gap(np.log, tangent22, 3, w) / w ** 2 for w in widths], computed=True)
with checked("R7.22c"):
    wbm.check("R7.22c", [max_gap(np.abs, lambda x: 0 * x, 0, w) / w for w in widths], computed=True)
wbm.check("R7.22d", answer_R7_22d)''',
    solution='''def max_gap(f, line, a, w):
    """The largest |f(x) − line(x)| for 1001 evenly spaced x in [a − w, a + w] (ends included)."""
    xs = np.linspace(a - w, a + w, 1001)
    return float(np.max(np.abs(f(xs) - line(xs))))


for w in widths:
    gap = max_gap(np.log, tangent22, 3, w)
    print(f"w = {w:<6}  écart = {gap:.3e}   écart / w = {gap / w:.5f}   écart / w² = {gap / w ** 2:.4f}")
answer_R7_22d = 0.056''',
    record='''gaps = [-w / 3 - math.log(1 - w / 3) for w in (0.5, 0.1, 0.01, 0.001)]   # largest at the left end
wbm.record("R7.22a", [g / w for g, w in zip(gaps, (0.5, 0.1, 0.01, 0.001))], decimals=5,
           mistakes={"l'écart est une valeur absolue : np.abs avant le maximum": [0.0, 0.0, 0.0, 0.0]})
wbm.record("R7.22b", [g / w ** 2 for g, w in zip(gaps, (0.5, 0.1, 0.01, 0.001))], decimals=4,
           mistakes={"l'écart est une valeur absolue : np.abs avant le maximum": [0.0, 0.0, 0.0, 0.0]})
wbm.record("R7.22c", [1.0, 1.0, 1.0, 1.0], decimals=4)
wbm.record("R7.22d", 1 / 18, decimals=3, mistakes={"regarde les rapports de b), pas ceux de a)": 0})''',
    note="Les rapports de a) tendent vers 0 : l'écart devient négligeable devant la largeur de la fenêtre, la courbe "
         "se confond avec sa tangente. Ceux de b) se stabilisent vers 0,0556 (c'est $\\frac{1}{18}$) : l'écart est "
         "de l'ordre de $w^2$, comme le petit carré du coin de la fiche (§4, §9). Pour $\\lvert x \\rvert$, le "
         "rapport reste 1 à toutes les échelles : aucune droite ne colle à un coin.",
)

R7_23_CHECK = '''with checked("R7.23 vérifications"):
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
    try:
        created = drawn(plot_f_and_tangents, axes, f23, df23, points23)
    finally:
        plt.close(fig)                                     # only the checks below are shown here
    problems = []
    if created:
        problems.append("ta fonction ouvre sa propre figure : dessine dans les axes reçus (axes[0].plot, …)")
    else:
        lines0 = [(np.asarray(l.get_xdata(), dtype=float), np.asarray(l.get_ydata(), dtype=float))
                  for l in axes[0].lines]
        lines1 = [(np.asarray(l.get_xdata(), dtype=float), np.asarray(l.get_ydata(), dtype=float))
                  for l in axes[1].lines]
        if not any(len(xs) >= 20 and np.allclose(ys, f23(xs)) for xs, ys in lines0):
            problems.append("la courbe de f n'est pas tracée dans axes[0] (au moins 20 points)")
        for p in points23:
            if not any(len(xs) >= 2 and np.allclose(ys, f23(p) + df23(p) * (xs - p)) and xs.min() < p < xs.max()
                       for xs, ys in lines0):
                problems.append(f"pas de tangente en {p} dans axes[0] : la droite y = f(p) + f′(p)(x − p), "
                                f"tracée avec plot de part et d'autre de p (pas axline)")
        if not any(len(xs) >= 20 and np.allclose(ys, df23(xs)) for xs, ys in lines1):
            problems.append("la courbe de f′ n'est pas tracée dans axes[1] (au moins 20 points)")
        if not any(len(ys) >= 2 and np.allclose(ys, 0) for xs, ys in lines1):
            problems.append("la droite y = 0 dans axes[1] (axes[1].axhline(0))")
        if not all(ax.get_title() for ax in axes):
            problems.append("un titre pour chaque graphique (ax.set_title)")
    if problems:
        print("❌ Ex R7.23 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex R7.23 : f, ses trois tangentes et f′, avec la droite y = 0.")'''

R7_23 = Ex(
    "R7.23", "🎨", 2, 20, "Tracer f, f′ et des tangentes",
    "tracer une fonction avec des tangentes et sa dérivée, et relier le signe de f′ aux variations de f.",
    "fiche §4 et §8 ; R0 (matplotlib)", tracks="C",
    body="""Pour $f(x) = (x^2 - 1)^3$ (fournie : `f23`, et sa dérivée `df23`, que tu peux vérifier à la main), complète `plot_f_and_tangents(axes, f, df, points)`, qui reçoit **deux axes** côte à côte :
- dans `axes[0]` : la courbe de `f` sur $[-1{,}6 \\;;\\; 1{,}6]$ (au moins 20 points), et, pour chaque abscisse $p$ de `points`, la tangente en $p$ tracée sur $[p - 0{,}3 \\;;\\; p + 0{,}3]$, avec le point de contact ;
- dans `axes[1]` : la courbe de `df` sur le même intervalle, et la droite $y = 0$ (`axes[1].axhline(0)`) ;
- un titre pour chacun.

La cellule suivante trace la figure pour `points23 = [-1.5, -0.5, 1]`, puis une autre la vérifie. Ensuite, en lisant tes graphiques **et** en le justifiant par le calcul :
- a) les abscisses où la tangente à la courbe de $f$ est horizontale, dans l'ordre croissant ;
- b) le nombre de minimums locaux de $f$.

Dans ta copie : sur le graphique de droite, où lis-tu que $f$ monte ? La tangente en 1 est horizontale : $f$ a-t-elle pour autant un extremum en 1 ? Que fait la courbe de part et d'autre de sa tangente, et comment le lis-tu sur le graphique de droite ?""",
    given='''def f23(x):
    return (x ** 2 - 1) ** 3


def df23(x):
    return 6 * x * (x ** 2 - 1) ** 2


points23 = [-1.5, -0.5, 1]''',
    todo='''def plot_f_and_tangents(axes, f, df, points):
    """axes[0]: f on [-1.6, 1.6] and its tangent at each p of points (on [p − 0.3, p + 0.3]); axes[1]: df and y = 0."""
    raise NotImplementedError("trace f et ses tangentes dans axes[0], f′ et y = 0 dans axes[1]")


answer_R7_23a = ...  # a) a list, in increasing order
answer_R7_23b = ...  # b) an integer''',
    check='''with checked("R7.23 figure"):
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
    try:
        created = drawn(plot_f_and_tangents, axes, f23, df23, points23)
    except BaseException:
        plt.close(fig)                                     # no empty figure while the function is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex R7.23 : ta fonction ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans les axes "
              "qu'elle reçoit.")
    else:
        fig.tight_layout()
        plt.show()
for letter, answer in zip("ab", [answer_R7_23a, answer_R7_23b]):
    wbm.check(f"R7.23{letter}", answer)''',
    solution='''def plot_f_and_tangents(axes, f, df, points):
    """axes[0]: f on [-1.6, 1.6] and its tangent at each p of points (on [p − 0.3, p + 0.3]); axes[1]: df and y = 0."""
    xs = np.linspace(-1.6, 1.6, 300)
    axes[0].plot(xs, f(xs), linewidth=2, label="f")
    for p in points:
        segment = np.linspace(p - 0.3, p + 0.3, 2)
        axes[0].plot(segment, f(p) + df(p) * (segment - p), "--", linewidth=1.2)
        axes[0].plot([p], [f(p)], "o", color="black", markersize=4)
    axes[0].set_title("f et trois tangentes")
    axes[1].plot(xs, df(xs), linewidth=2, color="C1")
    axes[1].axhline(0, color="gray", linewidth=0.8)
    axes[1].set_title("f′")
    for ax in axes:
        ax.grid(True, alpha=0.3)
        ax.set_xlabel("x")


fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
plot_f_and_tangents(axes, f23, df23, points23)
fig.tight_layout()
plt.show()
answer_R7_23a = [-1, 0, 1]
answer_R7_23b = 1''',
    record='''wbm.record("R7.23a", [-1, 0, 1],
           mistakes={"f′(x) = 6x(x² − 1)² : chacun de ses facteurs peut s'annuler": [0],
                     "ce sont les zéros de f ; une tangente horizontale, c'est f′ qui s'annule": [-1, 1]})
wbm.record("R7.23b", 1, mistakes={"un point où f′ s'annule sans changer de signe n'est pas un extremum ; compte "
                                 "seulement ceux où f′ passe de − à +": {2, 3}})''',
    after=[("md", "**Vérifications automatiques** (la figure elle-même se juge à l'œil)."), ("code", R7_23_CHECK)],
    note="$f'(x) = 6x(x^2 - 1)^2$ s'annule en −1, 0 et 1, mais ne change de signe qu'en 0, car le facteur "
         "$(x^2 - 1)^2$ n'est jamais négatif : un seul minimum local, $f(0) = -1$. En −1 et en 1, la tangente est "
         "horizontale et la courbe la traverse : pas d'extremum, comme $x^5$ en 0 (fiche §8). Sur le graphique de "
         "droite, la courbe de $f'$ touche l'axe en ±1 sans le traverser.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: bugs, and a tool (R7.24, R7.25)
# ---------------------------------------------------------------------------
R7_24_BUGGY = '''def d_a(x):  # derivative of x**2 * sqrt(x + 1)
    return 2 * x * (1 / (2 * math.sqrt(x + 1)))                   # (A)


def d_b(x):  # derivative of (x + 2) / (x - 3)
    return -5 / (x - 3) ** 2                                      # (B)


def d_c(x):  # derivative of exp(3 * x)
    return math.exp(3 * x)                                        # (C)


def d_d(x):  # derivative of ln(x**3 + 1)
    return 1 / (x ** 3 + 1)                                       # (D)


def d_e(x):  # derivative of sqrt(2 * x)
    return 1 / (2 * math.sqrt(2 * x))                             # (E)


def d_f(x):  # derivative of x**3 - 1 / x
    return 3 * x ** 2 + 1 / x ** 2                                # (F)'''

R7_24_FIXED = '''def d_a(x):  # derivative of x**2 * sqrt(x + 1)
    return 2 * x * math.sqrt(x + 1) + x ** 2 / (2 * math.sqrt(x + 1))   # (A) corrected: the product rule


def d_b(x):  # derivative of (x + 2) / (x - 3)
    return -5 / (x - 3) ** 2                                      # (B)


def d_c(x):  # derivative of exp(3 * x)
    return 3 * math.exp(3 * x)                                    # (C) corrected: times the derivative of 3x


def d_d(x):  # derivative of ln(x**3 + 1)
    return 3 * x ** 2 / (x ** 3 + 1)                              # (D) corrected: u'/u


def d_e(x):  # derivative of sqrt(2 * x)
    return 2 / (2 * math.sqrt(2 * x))                             # (E) corrected: times the derivative of 2x


def d_f(x):  # derivative of x**3 - 1 / x
    return 3 * x ** 2 + 1 / x ** 2                                # (F)'''

R7_24_MISTAKES = bug_letters_mistakes(
    "ACDE", "BF",
    {"A": "x²√(x + 1) est un produit : sa dérivée n'est pas le produit des dérivées",
     "C": "e^(3x) est une composée : multiplie par la dérivée de l'étage intérieur",
     "D": "ln(x³ + 1) est une composée : (ln u)′ = u′/u",
     "E": "√(2x) est une composée : l'étage intérieur 2x a pour dérivée 2"})

R7_24 = Ex(
    "R7.24", "🐛", 2, 20, "Chasse à l'erreur : quatre dérivées fausses",
    "repérer des dérivées fausses dans du code (règle du produit, règle de la chaîne), les corriger et les vérifier "
    "par un taux d'accroissement.", "fiche §6 et §7", tracks="C, E",
    body="""Six fonctions Python calculent les dérivées de six fonctions (écrites en commentaire). Certaines lignes sont fausses. **Sans rien exécuter d'abord**, trouve-les.

```python
""" + R7_24_BUGGY + """
```

- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;

Puis corrige-les dans la cellule ci-dessous (elle contient le code fautif). La fonction `slope(f, x)` de la cellule fournie calcule un taux d'accroissement avec $h = 10^{-6}$ : compare-le à chacune de tes dérivées en $x = 2$ pour les vérifier. La vérification calcule b), la liste des six valeurs `[d_a(2), d_b(2), …, d_f(2)]`.

Dans ta copie : pour chaque ligne fausse, quelle règle a été oubliée ? Laquelle des deux lignes justes pouvait sembler fausse, et pourquoi ne l'est-elle pas ?""",
    given='''def slope(f, x, h=1e-6):
    """A rate of change of f between x and x + h: close to f'(x) for a small h (fiche §3)."""
    return (f(x + h) - f(x)) / h''',
    todo='''answer_R7_24a = ...  # a) letters, as text


# correct the six functions below (the wrong lines only)
''' + R7_24_BUGGY,
    check='''wbm.check("R7.24a", answer_R7_24a)
if answer_R7_24a is ...:
    print("⏳ Ex R7.24b : trouve d'abord les lignes fausses (a), puis corrige les fonctions.")
else:
    with checked("R7.24b"):
        wbm.check("R7.24b", [d_a(2), d_b(2), d_c(2), d_d(2), d_e(2), d_f(2)], computed=True)''',
    solution='''answer_R7_24a = "ACDE"

''' + R7_24_FIXED + '''


print(answer_R7_24a, [d_a(2), d_b(2), d_c(2), d_d(2), d_e(2), d_f(2)])
print("vérification par des taux :", [slope(lambda x: x ** 2 * math.sqrt(x + 1), 2), slope(lambda x: math.exp(3 * x), 2),
                                      slope(lambda x: math.log(x ** 3 + 1), 2), slope(lambda x: math.sqrt(2 * x), 2)])''',
    record=f'''wbm.record("R7.24a", "ACDE",
           mistakes={R7_24_MISTAKES})
wbm.record("R7.24b", [4 * math.sqrt(3) + 2 / math.sqrt(3), -5, 3 * math.exp(6), 4 / 3, 0.5, 12.25], decimals=4,
           mistakes={{"aucune ligne n'est encore corrigée : corrige les lignes fausses dans la cellule où tu as écrit a)":
                         [2 / math.sqrt(3), -5, math.exp(6), 1 / 9, 1 / (2 * math.sqrt(4)), 12.25],
                     "d_a : la règle du produit donne deux termes": [4 * math.sqrt(3), -5, 3 * math.exp(6), 4 / 3, 0.5,
                                                                    12.25]}})''',
    note="(A) $(x^2 \\sqrt{x + 1})' = 2x\\sqrt{x + 1} + \\frac{x^2}{2\\sqrt{x + 1}}$, la règle du produit. (C) "
         "$(e^{3x})' = 3e^{3x}$. (D) $(\\ln(x^3 + 1))' = \\frac{3x^2}{x^3 + 1}$. (E) $(\\sqrt{2x})' = "
         "\\frac{2}{2\\sqrt{2x}} = \\frac{1}{\\sqrt{2x}}$. (B) est juste, malgré son signe moins : "
         "$\\frac{1 \\times (x - 3) - (x + 2) \\times 1}{(x - 3)^2} = \\frac{-5}{(x - 3)^2}$. (F) aussi : la dérivée "
         "de $-\\frac{1}{x}$ est $+\\frac{1}{x^2}$.",
)

R7_25 = Ex(
    "R7.25", "🛠️", 1, 15, "Tester une dérivée avec pytest et SymPy",
    "écrire un test qui compare une dérivée calculée à la main à celle de SymPy, et vérifier qu'il sait dire non.",
    "fiche §5 et §6 ; R0 (pytest)", tracks="C",
    body="""Une dérivée calculée à la main se vérifie par un **test** : une fonction `test_...` que pytest exécute, et qui échoue si la dérivée est fausse. Ici :
1. Écris `dg(x)`, la dérivée de $g(x) = \\frac{x^2 + 1}{x + 3}$, **calculée à la main** (règle du quotient, simplifiée) ;
2. Écris `test_dg_matches_sympy()`, **sans argument** : il crée son propre symbole (`X = sp.symbols("x")`, **dans** la fonction), calcule la dérivée de $g$ avec SymPy (`sp.diff`), puis vérifie avec `assert` et `math.isclose` que `dg` donne la même valeur qu'elle en au moins quatre points (pense à un point négatif ; évite −3). Pour évaluer une expression SymPy en un point : `float(expression.subs(X, point))`. Un message après l'`assert` (`assert ..., f"en {point} : {dg(point)}"`) dira où ça coince.

pytest exécute ta fonction de test **seule**, sans les autres cellules du notebook : tout ce qu'elle utilise (son symbole, l'expression de $g$) doit être défini dedans ; seuls `math`, `sp` et `dg` lui sont fournis.

La vérification lance ton test avec pytest (`wbm.run_pytest`) deux fois : sur ta `dg`, où il doit passer ; puis sur `dg_bug` (fournie), une dérivée fausse, où il doit **échouer**. Un test qui ne sait pas dire non ne vérifie rien.
- a) ton test passe-t-il sur `dg` ? ; b) échoue-t-il sur `dg_bug` ?""",
    given='''def dg_bug(x):
    """A wrong derivative of g(x) = (x**2 + 1) / (x + 3): u'v + uv' over v², with a + instead of a −."""
    return (2 * x * (x + 3) + (x ** 2 + 1)) / (x + 3) ** 2''',
    todo='''def dg(x):
    """The derivative of g(x) = (x**2 + 1) / (x + 3), computed by hand (x != -3)."""
    raise NotImplementedError("écris la dérivée de g, calculée à la main")


def test_dg_matches_sympy():
    """dg agrees with the derivative of g computed by SymPy, at four points or more."""
    raise NotImplementedError("écris le test : compare dg à sp.diff en quelques points")''',
    check='''with checked("R7.25"):
    dg(1.0)                        # ⏳ while dg is not written
    test_dg_matches_sympy()        # your test runs here first: ⏳ while it is not written
    good = wbm.run_pytest(test_dg_matches_sympy, subject=dg, preamble="import sympy as sp", quiet=True)
    bad = wbm.run_pytest(test_dg_matches_sympy, subject=dg_bug, name="dg", preamble="import sympy as sp", quiet=True)
    print(f"sur dg : {good.summary} ; sur dg_bug : {bad.summary}")
    if "NameError" in good.output + bad.output:
        print("⚠️ Ton test utilise un nom défini hors de lui (NameError) : pytest l'exécute seul, sans les autres "
              "cellules. Définis dedans tout ce qu'il utilise (son symbole X, l'expression de g).")
    wbm.check("R7.25a", good.ok, computed=True)
    wbm.check("R7.25b", bad.failed > 0 and "NameError" not in bad.output, computed=True)''',
    solution='''def dg(x):
    """The derivative of g(x) = (x**2 + 1) / (x + 3), computed by hand (x != -3)."""
    return (x ** 2 + 6 * x - 1) / (x + 3) ** 2


def test_dg_matches_sympy():
    """dg agrees with the derivative of g computed by SymPy, at four points or more."""
    X = sp.symbols("x")
    exact = sp.diff((X ** 2 + 1) / (X + 3), X)
    for point in (-2.5, -1, 0, 0.5, 2, 10):
        assert math.isclose(dg(point), float(exact.subs(X, point)), rel_tol=1e-12, abs_tol=1e-12)


good = wbm.run_pytest(test_dg_matches_sympy, subject=dg, preamble="import sympy as sp", quiet=True)
bad = wbm.run_pytest(test_dg_matches_sympy, subject=dg_bug, name="dg", preamble="import sympy as sp", quiet=True)
print(f"sur dg : {good.summary} ; sur dg_bug : {bad.summary}")''',
    record='''wbm.record("R7.25a", True,
           mistakes={"ton test échoue sur ta propre dg : relis ta dérivée (u′v − uv′ sur v²) ou ton test (lis la sortie "
                     "de pytest : print(good.output))": False})
wbm.record("R7.25b", True,
           mistakes={"ton test ne voit pas l'erreur de dg_bug (ou il échoue pour une autre raison qu'un assert) : "
                     "compare en plusieurs points, avec une tolérance serrée (math.isclose)": False})''',
    note="$g'(x) = \\frac{2x(x + 3) - (x^2 + 1)}{(x + 3)^2} = \\frac{x^2 + 6x - 1}{(x + 3)^2}$. Un test qui compare en "
         "un seul point peut tomber sur un point où une dérivée fausse est juste par hasard ; plusieurs points, dont "
         "un négatif, rendent ce hasard très improbable.",
)


PART_A = Part("A", "Ta librairie : taux d'accroissement, tangente, dichotomie",
              "Fiche §2 à §4. Les trois fonctions de `mymath/deriv.py`.",
              given=TOOLS, exercises=[R7_17, R7_18, R7_19])

PART_B = Part("B", "SymPy, une prédiction, un zoom et une figure",
              "Fiche §2 à §8. Dériver avec SymPy, trois taux d'accroissement dont il faut prévoir la limite, une "
              "courbe qui se confond avec sa tangente, puis f, f′ et des tangentes en image.",
              exercises=[R7_20, R7_21, R7_22, R7_23])

PART_C = Part("C", "Dérivées fausses et tests",
              "Fiche §5 à §7. Quatre dérivées fausses à trouver, puis un test qui vérifie une dérivée.",
              exercises=[R7_24, R7_25])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | R7.1 à R7.11, R7.15 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# R7 · Limites et dérivation — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/r7_limites_derivation/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py R7`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# R7 · Limites et dérivation — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : limites et asymptotes, taux d'accroissement, tangentes, "
               "dérivées (usuelles, produits, quotients, composées, une lettre à la fois), variations et "
               "optimisation.\n"
               "- Écrire les trois fonctions de `mymath/deriv.py` et les tester.\n"
               "- Dériver avec SymPy, prévoir quand un taux d'accroissement a une limite, zoomer sur une courbe, "
               "tracer f et f′, chasser des dérivées fausses et écrire un test.\n\n"
               "**Rappel express.** $f'(a) = \\lim_{h \\to 0} \\frac{f(a + h) - f(a)}{h}$ ; tangente : "
               "$y = f(a) + f'(a)(x - a)$. $(x^n)' = n x^{n-1}$, $(e^x)' = e^x$, $(\\ln x)' = \\frac{1}{x}$, "
               "$(\\sqrt{x})' = \\frac{1}{2\\sqrt{x}}$. $(uv)' = u'v + uv'$, "
               "$\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$, $\\big(g(u)\\big)' = g'(u) \\times u'$. "
               "$f' > 0$ : $f$ croît ; un extremum intérieur annule $f'$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Calcules-tu une limite en l'infini ou en un point, et repères-tu une asymptote ?\n"
               "2. Dérives-tu sans hésiter un produit, un quotient et une composée, et écris-tu une tangente ?\n"
               "3. Sais-tu étudier les variations d'une fonction et trouver son minimum, y compris aux bords ?\n\n"
               "**La suite** : R8, *Probabilités de base*. Dans workbookIA, continue le chapitre 0A au rythme de ton "
               "tableau de bord.")]


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
