#!/usr/bin/env python
"""Build the two notebooks of chapter R1 from a single source (used by Claude).

    python tools/chapters/build_r1.py
    python tools/run_all_notebooks.py chapitres/r1_nombres_calcul/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/r1_nombres_calcul/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ R1.1 to R1.14 and 🔗 R1.17); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys,  # noqa: E402
                         code, guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "R1"
FOLDER = "chapitres/r1_nombres_calcul"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("R1.1", "Placer des nombres sur la droite numérique et les ranger", [
        ("a", "the six letters in increasing order, as text", '"ACEDBF"',
         'mistakes={"compare 0,6 et 2/3 : écris 2/3 en décimal, avec trois chiffres après la virgule": "ACEBDF", '
         '"parmi les négatifs, le plus petit est le plus loin de zéro": "ECADBF", '
         '"l\'ordre croissant va du plus petit au plus grand": "FBDECA"}'),
        ("b", "an integer", "len([k for k in range(-5, 5) if -2.5 < k < 1.75])",
         'mistakes={"n\'oublie pas 0, qui est un entier relatif": 3, '
         '"un entier plus petit que A n\'est pas entre A et F": 5}'),
        ("c", "the letter(s), as text", '"C"', 'mistakes={"E vaut −1,5 : ce n\'est pas un entier": "CE"}'),
        ("d", "the letter(s), as text", '"B"',
         'mistakes={"F vaut 1,75 : son écriture décimale s\'arrête, c\'est un décimal": "BF", '
         '"C vaut −2 : un entier est aussi un décimal": "BC"}'),
    ]),
    Paper("R1.2", "Calculer avec les priorités et les signes", [
        ("a", "an integer", "18 - 4 * 3 + 2",
         'mistakes={"+ et − se font de gauche à droite : la soustraction d\'abord, puis l\'addition": 4, '
         '"la multiplication passe avant la soustraction": 44}'),
        ("b", "an integer", "-6 - (-9)", 'mistakes={"soustraire un négatif, c\'est ajouter": -15}'),
        ("c", "an integer", "(-2) ** 3",
         'mistakes={"trois facteurs négatifs : le produit est négatif": 8, '
         '"une puissance est un produit de facteurs égaux, pas une multiplication par l\'exposant": -6}'),
        ("d", "an integer", "-2 ** 4",
         'mistakes={"la puissance passe avant le signe moins : seul 2 est élevé à la puissance": 16}'),
        ("e", "an integer", "20 // 4 * 5",
         'mistakes={"× et ÷ ont la même priorité : on calcule de gauche à droite": 1}'),
        ("f", "an integer", "3 - 2 * (4 - 7) ** 2",
         'mistakes={"la multiplication passe avant la soustraction": 9, '
         '"le carré d\'un nombre négatif est positif": 21}'),
        ("g", "an integer", "(-12) // (-3) - 5", 'mistakes={"moins divisé par moins donne plus": -9}'),
        ("h", "an integer", "-(5 - 11) + 2 * (-4)",
         'mistakes={"un signe moins devant une parenthèse change le signe de chaque terme": -14, '
         '"deux fois un nombre négatif donne un nombre négatif": 14}'),
    ]),
    Paper("R1.3", "Calcul mental avec la distributivité : 17 × 99, 23 × 101", [
        ("a", "an integer", "17 * 99",
         'mistakes={"99 = 100 − 1 : retire le second produit, 17 × 1": 1700}'),
        ("b", "an integer", "23 * 101",
         'mistakes={"101 = 100 + 1 : ajoute le second produit, 23 × 1": 2300}'),
        ("c", "an integer", "9 * 34 + 9 * 66", 'mistakes={"factorise par 9 : 9 × (34 + 66)": 990}'),
        ("d", "an integer", "25 * 44", ""),
        ("e", "an integer", "8 * 47 - 8 * 7", 'mistakes={"factorise par 8 : 8 × (47 − 7)": 432}'),
    ]),
    Paper("R1.4", "Simplifier des fractions avec le PGCD", [
        ("a", "an integer", "math.gcd(45, 75)",
         'mistakes={"5 divise les deux nombres, mais ce n\'est pas le plus grand diviseur commun": 5, '
         '"3 divise les deux nombres, mais ce n\'est pas le plus grand diviseur commun": 3}'),
        ("b", "an irreducible fraction, as text", "Fraction(45, 75)", 'kind="fraction", simplified=True'),
        ("c", "an integer", "math.gcd(252, 198)",
         'mistakes={"le PGCD est le dernier reste non nul : continue jusqu\'au reste 0": 36, '
         '"6 divise les deux nombres, mais ce n\'est pas le plus grand diviseur commun": 6}'),
        ("d", "an irreducible fraction, as text", "Fraction(252, 198)", 'kind="fraction", simplified=True'),
        ("e", "an irreducible fraction, as text", "Fraction(-56, 98)", 'kind="fraction", simplified=True'),
        ("f", "an irreducible fraction, as text", "Fraction(1001, 1309)", 'kind="fraction", simplified=True'),
    ]),
    Paper("R1.5", "Additionner, multiplier et diviser des fractions", [
        ("a", "an irreducible fraction, as text", "Fraction(3, 10) + Fraction(4, 15)",
         'kind="fraction", simplified=True, '
         'mistakes={"on n\'additionne ni les numérateurs ni les dénominateurs entre eux : mets au même '
         'dénominateur": "7/25"}'),
        ("b", "an irreducible fraction, as text", "Fraction(7, 12) - Fraction(5, 8)",
         'kind="fraction", simplified=True, '
         'mistakes={"on ne soustrait pas les dénominateurs : mets au même dénominateur": "1/2"}'),
        ("c", "an irreducible fraction, as text", "Fraction(14, 15) * Fraction(25, 21)",
         'kind="fraction", simplified=True'),
        ("d", "an irreducible fraction, as text", "Fraction(7, 9) / Fraction(14, 27)",
         'kind="fraction", simplified=True, '
         'mistakes={"diviser par une fraction, c\'est multiplier par son inverse": "98/243"}'),
        ("e", "an irreducible fraction, as text", "1 + 1 / (1 + Fraction(1, 2))",
         'kind="fraction", simplified=True, '
         'mistakes={"1 divisé par une fraction, c\'est l\'inverse de cette fraction": "5/2"}'),
        ("f", "an integer", "Fraction(3, 8) * 240",
         'mistakes={"prendre une fraction d\'une quantité, c\'est multiplier par cette fraction": 640}'),
    ]),
    Paper("R1.6", "Comparer des fractions", [
        ("a", "a fraction, as text", "max(Fraction(7, 9), Fraction(11, 14))",
         'kind="fraction", mistakes={"compare les produits en croix : 7 × 14 et 11 × 9": "7/9"}'),
        ("b", "the three letters in increasing order, as text", '"RQP"',
         'mistakes={"l\'ordre croissant va du plus petit au plus grand": "PQR", '
         '"compare Q et R avec le dénominateur commun 24": "QRP"}'),
        ("c", "a fraction, as text", "Fraction(5, 12)",
         'kind="fraction", mistakes={"4/12 vaut exactement 1/3 : « strictement » l\'exclut": "1/3", '
         '"6/12 vaut exactement 1/2 : « strictement » l\'exclut": "1/2"}'),
        ("d", "True or False", "Fraction(13, 40) > Fraction(1, 3)",
         'mistakes={"compare les produits en croix : 13 × 3 et 40 × 1": True}'),
    ]),
    Paper("R1.7", "Appliquer les règles des puissances", [
        ("a", "an integer", "7 ** (5 - 2 - 2)",
         'mistakes={"additionne les exposants avec leur signe : l\'exposant −2 compte en moins": 16807}'),
        ("b", "an integer", "2 ** (3 * 2 - 4)",
         'mistakes={"(a^m)^n = a^(m × n) : on multiplie les exposants": 2}'),
        ("c", "a fraction, as text", "Fraction(5 ** 3, 5 ** 4)",
         'kind="fraction", mistakes={"5 tout seul, c\'est 5 puissance 1 : compte-le au numérateur": "1/25"}'),
        ("d", "an integer", "4 ** 3 * 25 ** 3",
         'mistakes={"(ab)^n = a^n × b^n : on multiplie les bases, l\'exposant reste le même": 10 ** 12}'),
        ("e", "a fraction, as text", "Fraction(3, 2) ** 3",
         'kind="fraction", mistakes={"la puissance porte sur le numérateur ET sur le dénominateur": "27/2"}'),
        ("f", "an integer", "(-1) ** 2027",
         'mistakes={"l\'exposant est impair : un nombre impair de facteurs −1": 1}'),
    ]),
    Paper("R1.8", "Puissances négatives et puissances de 10", [
        ("a", "a fraction, as text", "Fraction(1, 4 ** 2)",
         'kind="fraction", mistakes={"un exposant négatif donne un inverse, pas un nombre négatif": "-16", '
         '"4 puissance −2, c\'est 1 sur 4 au carré, pas 1 sur 4 fois 2": "1/8"}'),
        ("b", "an integer (or a fraction as text)", "Fraction(1, 3) ** -2",
         'kind="fraction", mistakes={"un exposant négatif retourne la fraction": "1/9"}'),
        ("c", "a decimal", "1e-5",
         'decimals=6, mistakes={"10^a × 10^b = 10^(a+b) : on additionne les exposants, on ne les multiplie pas": '
         '1e-6}'),
        ("d", "the list [m, k]", "[4, -6]",
         'mistakes={"le carré porte aussi sur la mantisse 2": [2, -6], '
         '"(10^a)² = 10^(2a) : l\'exposant est multiplié par 2": [4, -5]}'),
        ("e", "an integer", "9 - (-3)",
         'mistakes={"diviser par 10^(−3), c\'est soustraire −3 à l\'exposant, donc ajouter 3": 6}'),
        ("f", "an integer", "int(0.5 ** -3)",
         'mistakes={"un exposant négatif donne un inverse, pas un nombre négatif": -8}'),
        ("g", "an integer", "-3 - (-9)",
         'mistakes={"une nanoseconde est bien plus petite qu\'une milliseconde : il y en a beaucoup dedans": -6, '
         '"une milliseconde vaut 10^(−3) s et une nanoseconde 10^(−9) s : divise l\'une par l\'autre": 3}'),
    ]),
    Paper("R1.9", "Simplifier des racines carrées", [
        ("a", "an integer", "10", 'mistakes={"√200 = √100 × √2 : sors la racine de 100": 100}'),
        ("b", "an integer", "5", 'mistakes={"√75 = √25 × √3 : sors la racine de 25": 25}'),
        ("c", "an integer", "math.isqrt(12 * 3)", 'mistakes={"√12 × √3 = √36 : prends ensuite la racine": 36}'),
        ("d", "an integer", "math.isqrt(98 // 2)", 'mistakes={"√98 ÷ √2 = √49 : prends ensuite la racine": 49}'),
        ("e", "a decimal", "0.7",
         'decimals=2, mistakes={"élève ta réponse au carré pour vérifier : elle doit redonner 0,49": 0.07}'),
        ("f", "an integer", "3 * 2 - 3",
         'mistakes={"√20 = 2√5 : n\'oublie pas de le multiplier par 3": -1}'),
        ("g", "an integer", "math.isqrt((-9) ** 2)", 'mistakes={"une racine carrée n\'est jamais négative": -9}'),
    ]),
    Paper("R1.10", "Écrire en notation scientifique et arrondir", [
        ("a", "the list [m, k]", "[7.25, 7]",
         'decimals=2, mistakes={"la mantisse doit être comprise entre 1 et 10": [72.5, 6], '
         '"compte les rangs : la mantisse fois 10^k doit redonner le nombre de départ": [7.25, 6]}'),
        ("b", "the list [m, k]", "[9.06, -5]",
         'decimals=2, mistakes={"un nombre plus petit que 1 a un exposant négatif": [9.06, 5], '
         '"compte les rangs dont la virgule avance jusqu\'au premier chiffre non nul": [9.06, -4]}'),
        ("c", "an integer", "310000",
         'mistakes={"écris le nombre arrondi en entier, avec les zéros qui gardent la place des unités": 31, '
         '"deux chiffres significatifs seulement": 314000}'),
        ("d", "a decimal", "0.0078",
         'decimals=4, mistakes={"arrondis une seule fois, depuis la valeur complète": 0.0079, '
         '"les zéros de tête ne sont pas significatifs : garde deux chiffres à partir du premier non nul": 0.01}'),
        ("e", "an integer", "-4",
         'mistakes={"écris le nombre en notation scientifique, puis compare sa mantisse à 3,16": -3}'),
        ("f", "the list [m, k]", "[7, -8]",
         'mistakes={"diviser par 10^5, c\'est soustraire 5 à l\'exposant": [7, 2]}'),
    ]),
    Paper("R1.11", "Partie entière, arrondi au plus proche, arrondi supérieur", [
        ("a", "an integer", "math.floor(4.6)", ""),
        ("b", "an integer", "math.floor(-4.6)",
         'mistakes={"le plancher d\'un négatif est l\'entier juste en dessous, plus à gauche": -4}'),
        ("c", "an integer", "math.ceil(-0.4)",
         'mistakes={"le plafond est l\'entier juste au-dessus, vers la droite": -1}'),
        ("d", "an integer", "math.ceil(7)", 'mistakes={"un entier est son propre plafond": 8}'),
        ("e", "an integer", "round(-1.49)", 'mistakes={"regarde le chiffre des dixièmes : il est inférieur à 5": -2}'),
        ("f", "an integer", "math.ceil(100 / 12)",
         'mistakes={"avec une boîte de moins, il reste des œufs sans boîte : il faut un plafond": 8}'),
        ("g", "an integer", "int(-4.6)", 'mistakes={"int coupe vers 0 : ce n\'est pas un plancher": -5}'),
    ]),
    Paper("R1.12", "Évolutions successives et évolution réciproque", [
        ("a", "a number", "64 * 1.125",
         'decimals=2, mistakes={"augmenter de 12,5 %, c\'est multiplier par 1,125, pas ajouter 12,5": 76.5}'),
        ("b", "a percentage", "(1000 - 1250) / 1250 * 100",
         'decimals=1, mistakes={"on divise la variation par la valeur de départ": -25, '
         '"une baisse donne un taux négatif": 20}'),
        ("c", "a percentage", "(1.1 * 1.2 - 1) * 100",
         'decimals=1, mistakes={"les coefficients se multiplient, les taux ne s\'additionnent pas": 30}'),
        ("d", "a percentage", "(0.9 ** 3 - 1) * 100",
         'decimals=1, mistakes={"les coefficients se multiplient : trois fois le coefficient de −10 %": -30}'),
        ("e", "a percentage", "(1 / 1.6 - 1) * 100",
         'decimals=1, mistakes={"le coefficient réciproque est l\'inverse du coefficient, pas son opposé": -60}'),
        ("f", "a percentage", "(1 / 0.7 - 1) * 100",
         'decimals=2, mistakes={"le coefficient réciproque est l\'inverse du coefficient de la baisse": 30}'),
    ]),
    Paper("R1.13", "Règle de trois et proportionnalité", [
        ("a", "a number", "7.20 / 3 * 5", 'decimals=2'),
        ("b", "a number", "10 / 4 * 6", 'decimals=2'),
        ("c", "a number", "300 / 4 * 10", 'decimals=1'),
        ("d", "a number", "135 / 1.5",
         'decimals=2, mistakes={"1 h 30 vaut une heure et demie : 1,5 h, pas 1,3 h": 135 / 1.3}'),
        ("e", "True or False", "5 / 2 == 15 / 6 == 21 / 9",
         'mistakes={"calcule les trois quotients « bas ÷ haut » : sont-ils tous égaux ?": True}'),
    ]),
    Paper("R1.14", "Moyenne pondérée : la note finale et la somme pondérée d'un neurone", [
        ("a", "a decimal", "(13 * 4 + 9 * 1 + 16 * 3) / (4 + 1 + 3)",
         'decimals=3, mistakes={"pondère chaque note par son coefficient, puis divise par la somme des '
         'coefficients": (13 + 9 + 16) / 3}'),
        ("b", "a decimal", "(14 * 10 - 109) / 2",
         'decimals=2, mistakes={"le coefficient 2 compte dans la somme pondérée ET dans la somme des '
         'coefficients": 14 * 9 - 109}'),
        ("c", "a number", "1.5 * 2 + (-2) * 0.5 + 0.5 * 6 + (-1)",
         'decimals=2, mistakes={"n\'oublie pas le biais b": 5.0, "un poids négatif fois une entrée positive donne '
         'un nombre négatif": 6.0}'),
        ("d", "a decimal", "2 / (1 / 15 + 1 / 45)",
         'decimals=1, mistakes={"la moyenne des deux vitesses oublie le temps : la montée dure plus longtemps": '
         '30.0}'),
    ]),
    Paper("R1.17", "Combien de paramètres, combien d'octets ? Un réseau en notation scientifique", [
        ("a", "an integer", "300 * 200 + 200", 'mistakes={"chaque neurone a aussi un biais": 60000}'),
        ("b", "an integer", "(300 * 200 + 200) + (200 * 50 + 50) + (50 * 4 + 4)",
         'mistakes={"n\'oublie pas les biais des trois couches": 70200}'),
        ("c", "an integer", "5", 'mistakes={"écris le total en notation scientifique, puis compare sa mantisse à '
         '3,16": 4}'),
        ("d", "the list [m, k]", "[2.8, 5]",
         'decimals=1, mistakes={"un float32 occupe 4 octets : multiplie le nombre de paramètres par 4": [7.0, 4]}'),
        ("e", "an integer", "round(1.3e11 * 2 / 1e9)",
         'mistakes={"chaque paramètre occupe 2 octets": 130, '
         '"donne la réponse en Go : 1 Go vaut 10^9 octets": 260_000_000_000}'),
    ]),
]

PAPER_CONTEXT = "# Part 0: the answers are computed exactly from the statements\nimport math\nfrom fractions import Fraction"

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ R1.1 à R1.14, 🔗 R1.17)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire (une fraction entre guillemets, `\"5/12\"` ; un décimal avec un point, "
               "`0.75` ; une liste, `[7.25, 7]` ; un texte entre guillemets, `\"ACE\"`), jamais le calcul lui-même. "
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Part A: exact fractions (R1.21, R1.22, R1.25, R1.28, R1.29)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import doctest
import math
from fractions import Fraction

import matplotlib.pyplot as plt
import numpy as np

from wbm.nbtools import run_pytest_group'''

LOAD_LEARNER = 'mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="R1")  # reload your saved file'
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en R0.9). Ouvre ta copie `mon_travail/mymath/arith.py`, lis la docstring "
         "de la fonction en entier, remplace la ligne `raise NotImplementedError(...)` par ton code, **enregistre** le "
         "fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. N'utilise ni `math.gcd` "
         "ni le module `fractions` : les tests s'en servent pour vérifier tes résultats.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of arith.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_r1_arith.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_r1_arith.py", "{keyword}", impl="ref")')]


R1_21 = Ex(
    "R1.21", "🔨", 2, 40, "PGCD par l'algorithme d'Euclide et fraction irréductible · `gcd`, `simplify_fraction`",
    "programmer l'algorithme d'Euclide, puis s'en servir pour rendre une fraction irréductible.",
    "fiche §3 (l'algorithme d'Euclide) ; workbookIA 0A §100.4.2 (boucle `while`) et §100.6.2 (`raise`)",
    tracks="C, E", mymath="arith.py",
    body=HOWTO + """

- a) Écris `gcd(a, b)` : tant que `b` n'est pas nul, remplace le couple `(a, b)` par `(b, a % b)` ; à la fin, `a` est le PGCD. Travaille avec les valeurs sans signe (`abs`), et vérifie à la main sur le tableau de la fiche (1071 et 462).
- b) Écris `simplify_fraction(numerator, denominator)` : divise les deux par leur PGCD (avec `//`, pour rester en entiers), puis mets le signe au numérateur ; une `ValueError` si le dénominateur est nul.

La vérification calcule `gcd(2310, 1092)` et `simplify_fraction(-1092, 2310)`, puis lance les tests.""",
    todo=LOAD_LEARNER,
    check='''with wbm.attempt("R1.21a"):
    wbm.check("R1.21a", mymath.arith.gcd(2310, 1092), computed=True)
with wbm.attempt("R1.21b"):
    wbm.check("R1.21b", list(mymath.arith.simplify_fraction(-1092, 2310)), computed=True)''',
    solution=LOAD_REF + '''
print("gcd(2310, 1092)               =", mymath.arith.gcd(2310, 1092))
print("simplify_fraction(-1092, 2310) =", mymath.arith.simplify_fraction(-1092, 2310))''',
    record='''wbm.record("R1.21a", math.gcd(2310, 1092),
           mistakes={"à la fin de la boucle, le PGCD est dans a (le dernier reste non nul), b vaut 0": 0})
wbm.record("R1.21b", [-26, 55],
           mistakes={"le signe va au numérateur : le dénominateur doit rester positif": [26, -55],
                     "divise par le PGCD, pas seulement par un diviseur commun": [-546, 1155]})''',
    after=tests_cells("test_gcd_ or test_simplify_fraction_ or test_arith_uses"),
    note="`a % b` est le reste de la division euclidienne (R0 §2). Avec une boucle `while b != 0`, l'algorithme "
         "s'arrête toujours : le reste diminue strictement à chaque tour.",
)

R1_22 = Ex(
    "R1.22", "🔨", 2, 30, "Additionner deux fractions sans passer par les décimaux · `add_fractions`",
    "additionner deux fractions exactement, avec des entiers seulement.",
    "R1.21 ; fiche §3 (additionner)", tracks="C, E", mymath="arith.py",
    body="""Écris `add_fractions(a, b)` dans `mon_travail/mymath/arith.py` : `a` et `b` sont des couples `(numérateur, dénominateur)`. Mets-les au même dénominateur (le produit des dénominateurs suffit), additionne les numérateurs, puis rends le résultat irréductible avec **ta** fonction `simplify_fraction` (R1.21). Une `ValueError` si un dénominateur est nul.

Aucun flottant : pas de `/`, seulement `*`, `+` et `//`. La vérification calcule `add_fractions((7, 15), (-3, 10))`.""",
    todo=LOAD_LEARNER,
    check='''with wbm.attempt("R1.22"):
    wbm.check("R1.22", list(mymath.arith.add_fractions((7, 15), (-3, 10))), computed=True)''',
    solution=LOAD_REF + '''
print("add_fractions((7, 15), (-3, 10)) =", mymath.arith.add_fractions((7, 15), (-3, 10)))''',
    record='''wbm.record("R1.22", [1, 6],
           mistakes={"pense à rendre le résultat irréductible avec simplify_fraction": [25, 150],
                     "on n'additionne ni les numérateurs ni les dénominateurs entre eux": [4, 25]})''',
    after=tests_cells("test_add_fractions_"),
)

R1_25 = Ex(
    "R1.25", "📦", 1, 10, "Calculer exactement avec `fractions.Fraction`",
    "calculer une somme et un produit exactement avec `Fraction`, et voir ce que les flottants en font.",
    "fiche §3, « Calculer exactement avec Python »", tracks="C, E",
    body="""Avec `Fraction` (déjà importé dans la cellule des outils), calcule :
- a) la somme $S = 1 + \\dfrac{1}{2} + \\dfrac{1}{3} + \\dots + \\dfrac{1}{10}$, exactement ;
- b) le produit $P = \\left(1 - \\dfrac{1}{2}\\right)\\left(1 - \\dfrac{1}{3}\\right) \\cdots \\left(1 - \\dfrac{1}{10}\\right)$, exactement ;
- c) le même produit $P$ calculé en **flottants** (avec `1 - 1/k`) : vaut-il exactement `0.1` (`== 0.1`) ?

Une boucle `for k in range(...)` fait l'affaire (0A §100.4.2). Pour b), écris les premiers facteurs sur papier : devines-tu le résultat avant de l'exécuter ?""",
    todo='''answer_R1_25a = ...  # a) a Fraction (computed with a loop)
answer_R1_25b = ...  # b) a Fraction
answer_R1_25c = ...  # c) True or False (computed with floats)''',
    check='''for letter, answer in zip("abc", [answer_R1_25a, answer_R1_25b, answer_R1_25c]):
    wbm.check(f"R1.25{letter}", answer)''',
    solution='''total = Fraction(0)
for k in range(1, 11):
    total += Fraction(1, k)
product = Fraction(1)
product_float = 1.0
for k in range(2, 11):
    product *= 1 - Fraction(1, k)
    product_float *= 1 - 1 / k
print("S =", total, "≈", float(total))
print("P =", product, "; en flottants :", product_float, "; == 0.1 :", product_float == 0.1)
answer_R1_25a, answer_R1_25b, answer_R1_25c = total, product, product_float == 0.1''',
    record='''wbm.record("R1.25a", sum(Fraction(1, k) for k in range(1, 11)), kind="fraction",
           mistakes={"la somme commence à 1 (k = 1) et va jusqu'à 1/10 compris": "4861/2520"})
wbm.record("R1.25b", math.prod(1 - Fraction(1, k) for k in range(2, 11)), kind="fraction",
           mistakes={"le produit va jusqu'au facteur (1 − 1/10) compris : range(2, 11)": "1/9"})
wbm.record("R1.25c", math.prod(1 - 1 / k for k in range(2, 11)) == 0.1,
           mistakes={"affiche le produit en flottants : ses derniers chiffres s'écartent de 0.1": True})''',
    note="Le produit se « télescope » : $\\frac{1}{2} \\times \\frac{2}{3} \\times \\frac{3}{4} \\times \\dots \\times "
         "\\frac{9}{10} = \\frac{1}{10}$, chaque numérateur s'annule avec le dénominateur précédent. `Fraction` le "
         "trouve exactement ; les flottants arrivent à `0.10000000000000002`.",
)

R1_28_MISSING = {"a": "une addition de fractions qui additionne aussi les dénominateurs",
                 "c": "un produit de puissances de même base, dont la base a changé",
                 "e": "une division par une fraction qui ne passe pas par l'inverse"}

R1_28 = Ex(
    "R1.28", "🐛", 1, 15, "Chasse à l'erreur : cinq calculs de fractions et de puissances",
    "repérer les erreurs classiques de calcul sur les fractions et les puissances, et les corriger.",
    "fiche §3 et §4", tracks="C, E",
    body="""Un camarade a fait cinq calculs. **Sans calculatrice**, trouve ceux qui sont faux.

| | Calcul |
|---|---|
| a | $\\dfrac{2}{3} + \\dfrac{4}{5} = \\dfrac{6}{8}$ |
| b | $\\dfrac{3}{4} \\times \\dfrac{8}{9} = \\dfrac{2}{3}$ |
| c | $5^3 \\times 5^2 = 25^5$ |
| d | $\\left(\\dfrac{2}{5}\\right)^{-1} = \\dfrac{5}{2}$ |
| e | $\\dfrac{10}{3} \\div \\dfrac{5}{6} = \\dfrac{50}{18}$ |

- a) Donne les lettres des calculs faux, dans un texte : par exemple `"bd"`.
- b) Le bon résultat du calcul e (un entier).
- c) Le bon résultat du calcul a (une fraction irréductible, entre guillemets).""",
    todo='''answer_R1_28a = ...  # a) the letters of the wrong lines, as text, e.g. "bd"
answer_R1_28b = ...  # b) an integer
answer_R1_28c = ...  # c) an irreducible fraction, as text''',
    check='''for letter, answer in zip("abc", [answer_R1_28a, answer_R1_28b, answer_R1_28c]):
    wbm.check(f"R1.28{letter}", answer)''',
    solution='''claims = {"a": (Fraction(2, 3) + Fraction(4, 5), Fraction(6, 8)),
          "b": (Fraction(3, 4) * Fraction(8, 9), Fraction(2, 3)),
          "c": (5**3 * 5**2, 25**5),
          "d": (Fraction(2, 5) ** -1, Fraction(5, 2)),
          "e": (Fraction(10, 3) / Fraction(5, 6), Fraction(50, 18))}
for letter, (right, claimed) in claims.items():
    print(letter, "juste" if right == claimed else f"faux : le bon résultat est {right}")''',
    record=f'''wbm.record("R1.28a", "ace",
           mistakes={bug_letters_mistakes("ace", "bd", R1_28_MISSING)})
wbm.record("R1.28b", Fraction(10, 3) / Fraction(5, 6),
           mistakes={{"diviser par une fraction, c'est multiplier par son inverse": Fraction(50, 18)}})
wbm.record("R1.28c", Fraction(2, 3) + Fraction(4, 5), kind="fraction", simplified=True,
           mistakes={{"mets au même dénominateur (15) avant d'additionner": "6/8"}})''',
    note="Le calcul c additionne bien les exposants, mais garde la base 5 : $5^3 \\times 5^2 = 5^5 = 3125$, alors "
         "que $25^5$ dépasse neuf millions.",
)

R1_29_LINES = '''a = -x**2            # ligne 1 :  (−x)²
b = (x + 1) / 2 * x  # ligne 2 :  (x + 1)x / 2
c = 2 ** -1          # ligne 3 :  1/2
d = x / 2 * 3        # ligne 4 :  x / 6
e = (-2) ** 4        # ligne 5 :  (−2)⁴
f = 10 - (x - 4)     # ligne 6 :  10 − x + 4
g = 1 / 2 + x        # ligne 7 :  1 / (2 + x)'''

R1_29 = Ex(
    "R1.29", "🐛", 1, 10, "Chasse à l'erreur : `-3**2` et les parenthèses",
    "repérer les formules que Python calcule autrement que prévu, faute de parenthèses.",
    "fiche §2 ; R0 §2", tracks="C, E",
    body=f"""Chaque ligne veut calculer la formule écrite en commentaire, pour un nombre `x` déjà défini. **Sans rien exécuter**, trouve les lignes qui calculent **autre chose** que leur formule (pour certaines valeurs de `x`).

```python
{R1_29_LINES}
```

- a) Donne la liste des numéros des lignes fausses, par exemple `[1, 2]`.
- b) Écris la fonction `line4` corrigée, qui calcule vraiment $\\dfrac{{x}}{{6}}$ ; la vérification calcule `line4(3)`.""",
    todo='''answer_R1_29a = ...  # a) the list of the faulty lines, e.g. [1, 2]


def line4(x):
    """Line 4, corrected: return x / 6."""
    raise NotImplementedError("écris la formule corrigée")''',
    check='''wbm.check("R1.29a", answer_R1_29a)
with wbm.attempt("R1.29b"):
    wbm.check("R1.29b", line4(3), computed=True)''',
    solution=f'''x = 3
{R1_29_LINES}
print("avec x = 3 :", a, b, c, d, e, f, g)
print("les formules :", (-x)**2, (x + 1) * x / 2, 1 / 2, x / 6, (-2)**4, 10 - x + 4, 1 / (2 + x))


def line4(x):
    """Line 4, corrected: return x / 6."""
    return x / (2 * 3)


print("line4(3) =", line4(3))''',
    record='''wbm.record("R1.29a", [1, 4, 7], ordered=False,
           mistakes={"il manque une ligne fausse : la puissance passe avant le signe moins": [4, 7],
                     "il manque une ligne fausse : / et * se calculent de gauche à droite": [1, 7],
                     "il manque une ligne fausse : la division passe avant l'addition": [1, 4],
                     "la ligne 2 est juste : ((x + 1) / 2) × x vaut bien (x + 1)x / 2": [1, 2, 4, 7],
                     "la ligne 6 est juste : 10 − (x − 4) vaut bien 10 − x + 4": [1, 4, 6, 7],
                     "la ligne 3 est juste : 2 ** -1 vaut 1/2": [1, 3, 4, 7],
                     "la ligne 5 est juste : les parenthèses portent sur −2": [1, 4, 5, 7]})
wbm.record("R1.29b", 3 / 6, decimals=4,
           mistakes={"sans parenthèses, x / 2 * 3 divise par 2 puis multiplie par 3 : protège le dénominateur": 4.5})''',
    note="La ligne 2 est juste malgré les apparences : `(x + 1) / 2 * x` se lit $\\left(\\frac{x + 1}{2}\\right) "
         "\\times x$, qui vaut bien $\\frac{(x + 1)x}{2}$. Dans le doute, une paire de parenthèses en plus ne coûte rien.",
)

PART_A = Part("A", "Calculer exactement : PGCD, fractions, priorités",
              "Fiche §2 à §4. Tes deux premières fonctions de `mymath` (le PGCD et l'addition de fractions), le calcul "
              "exact avec `Fraction`, et deux chasses à l'erreur.",
              given=TOOLS, exercises=[R1_21, R1_22, R1_25, R1_28, R1_29])

# ---------------------------------------------------------------------------
# Part B: scientific notation and rounding (R1.23, R1.26, R1.30)
# ---------------------------------------------------------------------------
R1_23 = Ex(
    "R1.23", "🔨", 2, 40, "La notation scientifique à n chiffres significatifs · `scientific_notation`",
    "programmer le passage d'un nombre à sa notation scientifique arrondie, cas limites compris.",
    "fiche §6", tracks="C", mymath="arith.py",
    body="""Écris `scientific_notation(x, digits=3)` dans `mon_travail/mymath/arith.py` : elle renvoie le couple `(mantisse, exposant)` avec $1 \\le |\\text{mantisse}| < 10$, la mantisse arrondie à `digits` chiffres significatifs (`round(m, digits - 1)`).

Une démarche, à suivre dans la docstring :
1. `x == 0` est un cas à part (docstring) ;
2. l'exposant est l'entier $k$ tel que $10^k \\le |x| < 10^{k+1}$ : `math.floor(math.log10(abs(x)))` le donne presque toujours (vérifie que la mantisse obtenue est bien entre 1 et 10, et corrige d'un rang sinon) ;
3. la mantisse est $x / 10^k$, puis on l'arrondit ;
4. **le piège** : l'arrondi peut donner 10 (9,996 à trois chiffres) ; on écrit alors 1,00 et l'exposant augmente de 1.

La vérification calcule `scientific_notation(299792458, digits=4)` et `scientific_notation(-0.0009996)`.""",
    todo=LOAD_LEARNER,
    check='''with wbm.attempt("R1.23a"):
    wbm.check("R1.23a", list(mymath.arith.scientific_notation(299792458, digits=4)), computed=True)
with wbm.attempt("R1.23b"):
    wbm.check("R1.23b", list(mymath.arith.scientific_notation(-0.0009996)), computed=True)''',
    solution=LOAD_REF + '''
print("scientific_notation(299792458, digits=4) =", mymath.arith.scientific_notation(299792458, digits=4))
print("scientific_notation(-0.0009996)          =", mymath.arith.scientific_notation(-0.0009996))''',
    record='''wbm.record("R1.23a", [2.998, 8], decimals=3,
           mistakes={"la mantisse doit être comprise entre 1 et 10": [29.98, 7],
                     "arrondis la mantisse avec round, ne la tronque pas": [2.997, 8]})
wbm.record("R1.23b", [-1.0, -3], decimals=3,
           mistakes={"quand l'arrondi donne 10, écris 1,00 et ajoute 1 à l'exposant": [-10.0, -4],
                     "le signe du nombre reste sur la mantisse": [1.0, -3]})''',
    after=tests_cells("test_scientific_notation_"),
)

R1_26_EXPERIMENT = '''print("round(3.46, 1)        =", round(3.46, 1))
print("round(round(3.46, 1)) =", round(round(3.46, 1)))
print("round(3.46)           =", round(3.46))'''

R1_26 = Ex(
    "R1.26", "🔮", 1, 10, "Prédire : arrondir deux fois, est-ce arrondir une fois ?",
    "voir sur un exemple qu'arrondir un arrondi peut changer le résultat.",
    "fiche §6, « Chiffres significatifs et arrondis »", tracks="C", hypothesis=True,
    body="""`round(x, 1)` arrondit au dixième, `round(x)` à l'unité. **Avant d'exécuter quoi que ce soit**, prédis :
- a) `round(round(3.46, 1))` : on arrondit d'abord 3,46 au dixième, puis ce résultat à l'unité ;
- b) `round(3.46)` : on arrondit directement à l'unité.

Écris tes deux prédictions (des entiers), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_R1_26a = ...  # a) an integer, written BEFORE running the experiment below
prediction_R1_26b = ...  # b) an integer''',
    check='''wbm.check("R1.26a", prediction_R1_26a)
wbm.check("R1.26b", prediction_R1_26b)''',
    record='''wbm.record("R1.26a", round(round(3.46, 1)), prediction=True,
           mistakes={"arrondis d'abord au dixième : regarde le chiffre des centièmes, puis arrondis ce résultat": 3})
wbm.record("R1.26b", round(3.46), prediction=True,
           mistakes={"arrondis directement à l'unité : seul le chiffre des dixièmes compte": 4})''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes deux prédictions écrites."),
        ("todo", guarded(R1_26_EXPERIMENT, ["prediction_R1_26a", "prediction_R1_26b"],
                         "⏳ Écris d'abord tes deux prédictions (des entiers), puis exécute à nouveau.")),
        ("solution", R1_26_EXPERIMENT),
    ],
    note="3,46 arrondi au dixième donne 3,5, qui, arrondi à l'unité, donne 4 ; mais 3,46 est plus près de 3 que de "
         "4 : l'arrondi direct donne 3. Le premier arrondi a « poussé » le nombre vers le milieu. Règle : on arrondit "
         "une seule fois, à la fin, depuis la valeur complète.",
)

R1_30_DATA = '''# Approximate values (orders of magnitude only): label -> value
quantities = {
    "diamètre d'un atome (m)": 1e-10,
    "épaisseur d'un cheveu (m)": 7e-5,
    "secondes dans une journée": 8.64e4,
    "secondes dans une vie de 80 ans": 2.5e9,
    "êtres humains sur Terre": 8e9,
    "neurones d'un cerveau humain": 8.6e10,
    "paramètres d'un grand modèle de langage": 1e12,
}'''

R1_30 = Ex(
    "R1.30", "🎨", 1, 15, "Les ordres de grandeur sur une échelle : de l'atome aux paramètres d'un LLM",
    "placer des nombres de toutes tailles sur une même échelle, en puissances de 10.",
    "fiche §6, « Ordres de grandeur »", tracks="C",
    body="""Sur une échelle ordinaire, $10^{-10}$ et $10^{12}$ ne tiennent pas sur le même dessin. On place plutôt l'**exposant** : chaque graduation est une puissance de 10, et un pas vers la droite multiplie par 10.

Complète `plot_magnitudes` : pour chaque nombre du dictionnaire `quantities` (cellule suivante), place un point à l'abscisse $\\log_{10}(\\text{valeur})$ (`math.log10`, qui donne l'exposant, à une décimale près) et écris son nom à côté. Un titre, l'axe horizontal nommé « puissance de 10 », une graduation par entier de −10 à 12 (`ax.set_xticks(range(-10, 13))`).

Puis lis ta figure : combien de puissances de 10 séparent l'épaisseur d'un cheveu du nombre de paramètres du modèle ? Note ta réponse dans ta copie de `06_mes_reponses.md`, et compare ta figure à celle de `05_solutions.ipynb`.

$\\log_{10}$ est le **logarithme décimal** : $\\log_{10}(10^k) = k$. R6 l'étudiera ; ici, retiens seulement qu'il donne l'exposant.""",
    given=R1_30_DATA,
    todo='''def plot_magnitudes(quantities):
    """Draw each quantity as a point at x = log10(value), with its label; title, axis label, ticks."""
    raise NotImplementedError("place les points, puis les étiquettes")''',
    check='''with wbm.attempt("R1.30"):
    plot_magnitudes(quantities)''',
    solution='''def plot_magnitudes(quantities):
    """Draw each quantity as a point at x = log10(value), with its label; title, axis label, ticks."""
    fig, ax = plt.subplots(figsize=(9, 3.8))
    for i, (label, value) in enumerate(quantities.items()):
        x = math.log10(value)
        ax.plot(x, i, "o")
        ax.annotate(label, (x, i), xytext=(6, -3), textcoords="offset points", fontsize=9)
    ax.set_xticks(range(-10, 13))
    ax.set_yticks([])
    ax.set_xlim(-11, 16)
    ax.set_xlabel("puissance de 10")
    ax.set_title("Des nombres de toutes tailles, en ordres de grandeur")
    ax.grid(True, axis="x", alpha=0.4)
    plt.show()


plot_magnitudes(quantities)
print("cheveu -> paramètres :", round(math.log10(1e12) - math.log10(7e-5)), "puissances de 10 environ")''',
)

PART_B = Part("B", "Notation scientifique, arrondis et ordres de grandeur",
              "Fiche §6. La notation scientifique programmée, un arrondi qui surprend, et une échelle des ordres de "
              "grandeur.", exercises=[R1_23, R1_26, R1_30])

# ---------------------------------------------------------------------------
# Part C: percentages and means (R1.24, R1.27, R1.31)
# ---------------------------------------------------------------------------
R1_24 = Ex(
    "R1.24", "🔨", 1, 30, "Évolutions successives et moyenne pondérée · `successive_changes`, `weighted_mean`",
    "programmer le taux global d'évolutions successives et la moyenne pondérée, avec leurs cas d'erreur.",
    "fiche §7 et §8 ; workbookIA 0A §100.6.2 (`raise`)", tracks="C, E", mymath="arith.py",
    body="""Dans `mon_travail/mymath/arith.py` :
- a) `successive_changes(rates)` : les taux sont écrits en décimal (`0.10` pour +10 %). Multiplie les coefficients $1 + t$, puis repasse du coefficient global au taux global. Une liste vide donne `0.0` ; un taux inférieur à −1 (−100 %) lève une `ValueError`.
- b) `weighted_mean(values, weights)` : la somme des valeur × poids, divisée par la somme des poids. Trois cas lèvent une `ValueError` : des longueurs différentes, un poids négatif, des poids de somme nulle.

La vérification calcule `successive_changes([0.3, -0.2, 0.05])` et `weighted_mean([11, 17, 8], [2, 3, 5])`.""",
    todo=LOAD_LEARNER,
    check='''with wbm.attempt("R1.24a"):
    wbm.check("R1.24a", mymath.arith.successive_changes([0.3, -0.2, 0.05]), computed=True)
with wbm.attempt("R1.24b"):
    wbm.check("R1.24b", mymath.arith.weighted_mean([11, 17, 8], [2, 3, 5]), computed=True)''',
    solution=LOAD_REF + '''
print("successive_changes([0.3, -0.2, 0.05]) =", mymath.arith.successive_changes([0.3, -0.2, 0.05]))
print("weighted_mean([11, 17, 8], [2, 3, 5]) =", mymath.arith.weighted_mean([11, 17, 8], [2, 3, 5]))''',
    record='''wbm.record("R1.24a", 1.3 * 0.8 * 1.05 - 1, decimals=4,
           mistakes={"les coefficients se multiplient, les taux ne s'additionnent pas": 0.15,
                     "renvoie le taux global (le coefficient moins 1), pas le coefficient": 1.3 * 0.8 * 1.05})
wbm.record("R1.24b", (11 * 2 + 17 * 3 + 8 * 5) / (2 + 3 + 5), decimals=4,
           mistakes={"divise par la somme des poids, pas par le nombre de valeurs": (11 * 2 + 17 * 3 + 8 * 5) / 3,
                     "c'est une moyenne pondérée, pas une moyenne simple": (11 + 17 + 8) / 3})''',
    after=tests_cells("test_successive_changes_ or test_weighted_mean_"),
)

R1_27 = Ex(
    "R1.27", "🔬", 2, 20, "Après n hausses de 10 % : tracer et comparer à une hausse de 10n %",
    "voir qu'une évolution répétée suit une puissance, qui finit par écraser une croissance de taux additionnés.",
    "fiche §7, « Évolutions successives »", tracks="C",
    body="""Un prix de 1 € augmente de 10 % chaque année. Après $n$ années, il vaut $1{,}1^n$ euros. Un camarade pense qu'il vaut $1 + 0{,}1n$ (« 10 % par an, donc $10n$ % en $n$ ans »).

- Trace les deux courbes, $1{,}1^n$ et $1 + 0{,}1n$, pour $n$ entier de 0 à 30 (points reliés, une légende, un titre, des axes nommés).
- a) Au bout de combien d'années le prix a-t-il **doublé** pour la première fois ($1{,}1^n \\ge 2$) ? Un entier.
- b) Que vaut $1{,}1^{30}$, arrondi au centième ?

Pour a), une boucle `while` qui multiplie par 1,1 tant que le prix est inférieur à 2 suffit.""",
    todo='''def plot_growth(n_max=30):
    """Plot 1.1**n and 1 + 0.1*n for n = 0, 1, ..., n_max (legend, title, axis labels)."""
    raise NotImplementedError("trace les deux courbes")


answer_R1_27a = ...  # a) an integer (computed with a loop)
answer_R1_27b = ...  # b) a number rounded to 2 decimals''',
    check='''with wbm.attempt("R1.27 plot"):
    plot_growth()
wbm.check("R1.27a", answer_R1_27a)
wbm.check("R1.27b", answer_R1_27b)''',
    solution='''def plot_growth(n_max=30):
    """Plot 1.1**n and 1 + 0.1*n for n = 0, 1, ..., n_max (legend, title, axis labels)."""
    n = np.arange(n_max + 1)
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    ax.plot(n, 1.1**n, "o-", markersize=3, label="10 % par an : 1,1ⁿ")
    ax.plot(n, 1 + 0.1 * n, "o-", markersize=3, label="taux additionnés : 1 + 0,1n")
    ax.set_xlabel("années n")
    ax.set_ylabel("prix (€)")
    ax.set_title("Hausses successives de 10 % ou taux additionnés")
    ax.grid(True)
    ax.legend()
    plt.show()


plot_growth()
price, years = 1.0, 0
while price < 2:
    price *= 1.1
    years += 1
answer_R1_27a, answer_R1_27b = years, round(1.1**30, 2)
print("doublement après", years, "ans ; 1,1^30 =", answer_R1_27b, "; 1 + 0,1 × 30 =", 1 + 0.1 * 30)''',
    record='''wbm.record("R1.27a", 8,
           mistakes={"au bout de 7 ans, le prix n'a pas encore atteint 2 € : un an de plus": 7,
                     "les taux ne s'additionnent pas : les hausses se multiplient, le doublement vient plus tôt": 10})
wbm.record("R1.27b", round(1.1**30, 2), decimals=2,
           mistakes={"c'est une puissance, pas une somme de taux : multiplie trente fois par 1,1": 4.0})''',
    note="Doubler en 8 ans à 10 % par an : c'est la « règle de 72 » des financiers (72 ÷ 10 ≈ 7,2 ans, une "
         "approximation). Les deux courbes sont proches au début, puis la puissance s'envole : à 30 ans, 17,45 € "
         "contre 4 €. Tu retrouveras cette croissance au chapitre R5 (suites géométriques) et R6 (exponentielle).",
)

R1_31_FUNCTION = '''def harmonic_mean(values):
    values = list(values)
    if len(values) == 0:
        raise ValueError("cannot compute the harmonic mean of an empty sequence")
    if any(v <= 0 for v in values):
        raise ValueError("the harmonic mean needs positive values")
    return len(values) / sum(1 / v for v in values)'''

R1_31_CHECK = '''with wbm.attempt("R1.31"):
    doc = harmonic_mean.__doc__ or ""
    missing = [section for section in ("Parameters", "Returns", "Raises", "Examples") if section not in doc]
    if missing:
        print("❌ Ex R1.31 : il manque ces sections dans la docstring :", ", ".join(missing))
    else:
        failures = doctest.run_docstring_examples(harmonic_mean, {"harmonic_mean": harmonic_mean}, verbose=False)
        n_examples = doc.count(">>>")
        if n_examples >= 2:
            print(f"✅ Ex R1.31 : quatre sections, et {n_examples} exemples (aucun message au-dessus = ils passent).")
        else:
            print(f"❌ Ex R1.31 : {n_examples} exemple(s) >>> dans la docstring ; il en faut au moins deux.")'''

R1_31 = Ex(
    "R1.31", "🛠️", 1, 15, "Écrire la docstring d'une fonction (format NumPy)",
    "écrire une docstring complète, au format NumPy, avec des exemples exécutables.",
    "fiche §8 (moyenne harmonique) ; workbookIA 0A §100.5.5 (docstrings)", tracks="C",
    body="""La fonction `harmonic_mean` (fiche §8, la moyenne harmonique) marche, mais personne ne sait comment s'en servir : elle n'a pas de docstring. Écris-la, **en anglais** comme tout le code du dépôt, au format NumPy que tu as vu dans 0A (§100.5.5) et dans les fichiers de `mymath` :
- une première ligne qui dit ce que fait la fonction ;
- `Parameters`, `Returns` et `Raises` (les deux cas d'erreur du code) ;
- `Examples` : au moins deux exemples `>>>` avec leur résultat, que tu calcules à la main (par exemple la moyenne harmonique de 90 et de 60 de la fiche).

La vérification regarde que les quatre sections sont là, puis **exécute tes exemples** (`doctest`) : un exemple faux affiche un message. Compare ensuite ta docstring à celle de `05_solutions.ipynb` : plusieurs rédactions sont justes.""",
    todo=R1_31_FUNCTION.replace("def harmonic_mean(values):\n",
                                'def harmonic_mean(values):\n    """TODO: write the docstring (NumPy format)."""\n'),
    check=R1_31_CHECK,
    solution=R1_31_FUNCTION.replace("def harmonic_mean(values):\n", '''def harmonic_mean(values):
    """Return the harmonic mean of positive numbers: the inverse of the mean of their inverses.

    Parameters
    ----------
    values : sequence of float
        Strictly positive numbers (a speed, a rate...).

    Returns
    -------
    float
        ``n / (1/x1 + ... + 1/xn)``, never larger than the arithmetic mean.

    Raises
    ------
    ValueError
        If ``values`` is empty, or if a value is zero or negative.

    Examples
    --------
    >>> harmonic_mean([90, 60])
    72.0
    >>> harmonic_mean([5, 5, 5])
    5.0
    """
''') + "\n\n\n" + R1_31_CHECK,
)

PART_C = Part("C", "Pourcentages et moyennes",
              "Fiche §7 et §8. Tes deux dernières fonctions de `arith.py`, une expérience sur les hausses répétées, "
              "et une docstring.", exercises=[R1_24, R1_27, R1_31])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | R1.1 à R1.14, R1.17 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# R1 · Nombres et calcul — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/r1_nombres_calcul/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py R1`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# R1 · Nombres et calcul — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : priorités, fractions, puissances, racines, notation "
               "scientifique, pourcentages, moyennes.\n"
               "- Écrire les six fonctions de `mymath/arith.py` et les tester.\n"
               "- Calculer exactement avec `Fraction`, repérer les erreurs de calcul classiques, voir une hausse "
               "répétée s'envoler.\n\n"
               "**Rappel express.** $\\frac{a}{b} + \\frac{c}{d} = \\frac{ad + cb}{bd}$ ; diviser, c'est multiplier "
               "par l'inverse ; $a^{-n} = \\frac{1}{a^n}$ ; $\\sqrt{ab} = \\sqrt{a}\\sqrt{b}$ ; une évolution de "
               "$t$ multiplie par $1 + t$, et les coefficients successifs se multiplient.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Calcules-tu sans erreur avec des priorités, des négatifs, des fractions et des puissances, et "
               "repères-tu les « règles » qui n'existent pas ?\n"
               "2. Sais-tu écrire un nombre en notation scientifique, l'arrondir et donner son ordre de grandeur ?\n"
               "3. Sais-tu enchaîner des évolutions en pourcentage et calculer une moyenne pondérée, à la main et "
               "avec `mymath` ?\n\n"
               "**La suite** : R2, *Calcul littéral et équations*. Dans workbookIA, continue le chapitre 0A au "
               "rythme de ton tableau de bord.")]


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
