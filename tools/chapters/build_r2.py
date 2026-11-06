#!/usr/bin/env python
"""Build the two notebooks of chapter R2 from a single source (used by Claude).

    python tools/chapters/build_r2.py
    python tools/run_all_notebooks.py chapitres/r2_calcul_litteral/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/r2_calcul_litteral/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ R2.1 to R2.12 and 🔗 R2.16); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer. A developed or factorised expression is answered by
its list of coefficients: an equivalent expression would pass a check of kind "expr" without being developed.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys,  # noqa: E402
                         code, guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "R2"
FOLDER = "chapitres/r2_calcul_litteral"

CHOICES = "choices=[1, 2, 3]"
ORDER_XY = '"l\'ordre demandé est [x, y]"'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("R2.1", "Substituer et réduire", [
        ("a", "a number", "2 * (-3) ** 2 - 3 * (-3) + 1",
         'mistakes={"le carré d\'un nombre négatif est positif : garde les parenthèses autour de −3": -8, '
         '"−3 × (−3) est positif : moins par moins donne plus": 10}'),
        ("b", "a number", "(2 - (-1)) ** 2 - 2 * (-1)",
         'mistakes={"a − b = 2 − (−1) : soustraire un négatif, c\'est ajouter": 3, '
         '"ab est négatif : retirer un nombre négatif, c\'est ajouter": 7}'),
        ("c", "the list [alpha, beta, gamma]", "[1, -2, 1]",
         'mistakes={"−x² compte en moins : 2x² − x²": [3, -2, 1], '
         '"réduis les termes en x avec leurs signes : 5x − 7x": [1, 12, 1], '
         '"les constantes se réduisent aussi, avec leurs signes : −3 + 4": [1, -2, -7]}'),
        ("d", "the list [alpha, beta]", "[7, 3]",
         'mistakes={"−2x + 5x : additionne les coefficients avec leurs signes": [7, -7], '
         '"l\'ordre demandé est [coefficient de xy, coefficient de x]": [3, 7]}'),
        ("e", "a number", "(Fraction(1, 2) + 1) / (Fraction(1, 2) - 1)",
         'mistakes={"x − 1 est négatif pour x = 1/2 : le quotient aussi": 3}'),
    ]),
    Paper("R2.2", "Développer", [
        ("a", "the list [alpha, beta]", "[2, -11]",
         'mistakes={"un moins devant une parenthèse change le signe de chacun de ses termes : −4 × (−1)": [2, -19], '
         '"−4 × x est négatif": [10, -11]}'),
        ("b", "the list [alpha, beta, gamma]", "[3, -1, -10]",
         'mistakes={"quatre produits : n\'oublie pas les deux produits croisés": [3, 0, -10], '
         '"−2 × 3x est négatif": [3, 11, -10], "−2 × 5 est négatif": [3, -1, 10]}'),
        ("c", "the list [alpha, beta, gamma, delta]", "[2, -1, 5, 3]",
         'mistakes={"trois termes dans la seconde parenthèse : six produits en tout": [2, -2, 6, 3]}'),
        ("d", "the list [alpha, beta, gamma]", "[-1, 3, 4]",
         'mistakes={"le signe moins devant porte sur tout le produit": [1, -3, -4], '
         '"le signe moins change le signe de chaque terme du produit développé, pas seulement du premier": '
         '[-1, -3, -4]}'),
        ("e", "the list [alpha, beta, gamma]", "[1, 1, -2]",
         'mistakes={"a × (−b) est négatif": [1, 3, -2], "n\'oublie pas les produits croisés": [1, 0, -2]}'),
    ]),
    Paper("R2.3", "Factoriser par un facteur commun", [
        ("a", "the list [k, alpha, beta]", "[3, 2, 5]",
         'mistakes={"cherche le plus grand facteur commun : le PGCD des coefficients et la plus petite puissance '
         'de x": [1, 6, 15]}'),
        ("b", "the list [alpha, beta]", "[-2, 3]",
         'mistakes={"garde le signe de chaque terme en divisant par 4x": [2, 3], '
         '"divise chaque terme par 4x, coefficient compris": [-8, 12]}'),
        ("c", "the list [alpha, beta]", "[3, -2]",
         'mistakes={"additionne les deux parenthèses en gardant le signe de −5": [3, 8]}'),
        ("d", "the list [alpha, beta]", "[1, 5]",
         'mistakes={"le moins devant (x − 4) change aussi le signe de −4": [1, -3], '
         '"le second produit est soustrait : (2x + 1) − (x − 4)": [3, -3]}'),
        ("e", "the list [alpha, beta]", "[5, -3]", 'mistakes={"le −3 garde son signe": [5, 3]}'),
        ("f", "the list [alpha, beta]", "[1, 1]",
         'mistakes={"le terme x − 7 vaut 1 × (x − 7) : il reste un 1, pas un 0": [1, 0]}'),
    ]),
    Paper("R2.4", "Identités remarquables dans les deux sens", [
        ("a", "the list [alpha, beta, gamma]", "[1, 10, 25]",
         'mistakes={"il manque le double produit 2ab": [1, 0, 25], "le double produit vaut 2 × a × b": [1, 5, 25]}'),
        ("b", "the list [alpha, beta, gamma]", "[9, -24, 16]",
         'mistakes={"le carré porte sur tout 3x": [3, -24, 16], "le double produit vaut 2 × a × b": [9, -12, 16], '
         '"(a − b)² n\'est pas a² − b² : il y a un double produit": [9, 0, -16], '
         '"(a − b)² a un double produit négatif": [9, 24, 16]}'),
        ("c", "the list [alpha, beta, gamma]", "[4, 0, -49]",
         'mistakes={"(a + b)(a − b) = a² − b² : une différence": [4, 0, 49], "le carré porte sur tout 2x": '
         '[2, 0, -49]}'),
        ("d", "a number", "7",
         'mistakes={"développe (x − a)² : le double produit −2ax doit redonner le terme en x": -7, '
         '"le double produit vaut 2a, pas a": 14, "a² est le terme constant : il reste à prendre la racine": 49}'),
        ("e", "the list [alpha, beta]", "[5, 3]",
         'mistakes={"α² et β² sont les carrés : prends leurs racines carrées": [25, 9]}'),
        ("f", "the list [alpha, beta]", "[2, 5]",
         'mistakes={"α² et β² sont les carrés : prends leurs racines carrées": [4, 25]}'),
        ("g", "an integer", "101 ** 2", 'mistakes={"il manque le double produit": 10001}'),
        ("h", "an integer", "59 * 61",
         'mistakes={"(a − b)(a + b) = a² − b² : on soustrait b², on ne l\'ajoute pas": 3601}'),
    ]),
    Paper("R2.5", "Équations du premier degré", [
        ("a", "a number", "-2.0",
         'decimals=2, mistakes={"pour isoler 4x, retire 9 aux deux membres": 2.5, '
         '"divise par 4 en gardant le signe": 2.0}'),
        ("b", "a number", "-3",
         'mistakes={"retire 3x aux deux membres : −2x − 3x": 15, "divise par −5 en gardant le signe": 3}'),
        ("c", "a number", "13",
         'mistakes={"développe : le 3 multiplie les deux termes de la parenthèse": 5, '
         '"un terme qui change de membre change de signe": 1}'),
        ("d", "a number", "18",
         'mistakes={"le 2 multiplie tout le numérateur x + 4 : mets des parenthèses": 10, '
         '"le −1 aussi est multiplié par le dénominateur commun": 13}'),
        ("e", "1, 2 or 3", "1",
         f'{CHOICES}, mistakes={{"les x disparaissent : l\'égalité qui reste est-elle vraie ?": 3, '
         '"les x disparaissent : il ne reste aucune valeur de x à trouver": 2}'),
        ("f", "1, 2 or 3", "3",
         f'{CHOICES}, mistakes={{"les x disparaissent : l\'égalité qui reste est-elle vraie ou fausse ?": 1, '
         '"les x disparaissent : il ne reste aucune valeur de x à trouver": 2}'),
    ]),
    Paper("R2.6", "Équations produit nul et équations avec des fractions", [
        ("a", "a list of solutions", "[4, -1.5]",
         'ordered=False, decimals=4, mistakes={"2x + 3 = 0 donne une solution négative": [4, 1.5], '
         '"2x = −3 : divise par 2": [4, -3]}'),
        ("b", "a list of solutions", "[0, 9 / 4]",
         'ordered=False, decimals=4, mistakes={"en divisant par x, on perd une solution : factorise": [9 / 4], '
         '"4x = 9 : divise 9 par 4, pas l\'inverse": [0, 4 / 9]}'),
        ("c", "a list of solutions", "[1 / 3]",
         'ordered=False, decimals=4, mistakes={"3x = 1 : divise 1 par 3": [3], '
         '"un carré est nul seulement quand le nombre élevé au carré est nul : une seule solution": '
         '[-1 / 3, 1 / 3]}'),
        ("d", "a list of solutions", "[-4 / 3, 4 / 3]",
         'ordered=False, decimals=4, mistakes={"un carré égal à un nombre positif : deux solutions opposées": '
         '[4 / 3], "x² est connu : il reste à prendre la racine carrée": [-16 / 9, 16 / 9]}'),
        ("e", "a number", "1", 'mistakes={"une valeur interdite annule un dénominateur": -2}'),
        ("f", "a list of solutions", "[5 / 2]",
         'ordered=False, decimals=4, mistakes={"3 multiplie tout le dénominateur : 3(x − 1)": [3 / 2]}'),
        ("g", "a list of solutions", "[8]",
         'ordered=False, decimals=4, mistakes={"le moins devant la fraction porte sur tout le numérateur x − 2": '
         '[16]}'),
    ]),
    Paper("R2.7", "Inéquations et intervalles", [
        ("a", "an interval, as text", '"]-oo ; 6["',
         'kind="interval", mistakes={"l\'inégalité est stricte : la borne est exclue": "]-oo ; 6]", '
         '"pour isoler 2x, ajoute 7 aux deux membres": "]-oo ; -1["}'),
        ("b", "an interval, as text", '"]-oo ; -3]"',
         'kind="interval", mistakes={"diviser par un nombre négatif retourne le sens": "[-3 ; +oo[", '
         '"l\'inégalité est large : la borne est incluse": "]-oo ; -3["}'),
        ("c", "an interval, as text", '"[3 ; +oo["',
         'kind="interval", mistakes={"diviser par un nombre négatif retourne le sens": "]-oo ; 3]", '
         '"l\'inégalité est large : la borne est incluse": "]3 ; +oo["}'),
        ("d", "an interval, as text", '"]-3 ; 3]"',
         'kind="interval", mistakes={"chaque borne garde son inégalité : stricte à gauche, large à droite": '
         '"[-3 ; 3["}'),
        ("e", "an interval, as text", '"]-12 ; +oo["',
         'kind="interval", mistakes={"le 2 multiplie tout le numérateur x − 3": "]-9 ; +oo["}'),
    ]),
    Paper("R2.8", "Réunion et intersection d'intervalles", [
        ("a", "an interval, as text", '"[1 ; 5]"',
         'kind="interval", mistakes={"∩ garde les nombres qui sont dans les deux à la fois (la réunion, c\'est ∪)": '
         '"[-2 ; 8]"}'),
        ("b", "an interval, as text", '"[0 ; 3["',
         'kind="interval", mistakes={"un nombre exclu de l\'un des deux intervalles n\'est pas dans '
         'l\'intersection": "[0 ; 3]"}'),
        ("c", "an interval, as text", '"[-4 ; 6["',
         'kind="interval", mistakes={"∪ garde les nombres qui sont dans l\'un ou dans l\'autre (l\'intersection, '
         'c\'est ∩)": "[0 ; 1]", "les deux intervalles se chevauchent : écris leur réunion en un seul intervalle": '
         '"[-4 ; 1] U [0 ; 6["}'),
        ("d", "an interval, as text", '"vide"',
         'kind="interval", mistakes={"l\'intersection garde seulement les nombres communs aux deux": '
         '"]-oo ; -1] U [2 ; +oo["}'),
        ("e", "an interval or a union, as text", '"]-oo ; -2[ U [3 ; +oo["',
         'kind="interval", mistakes={"« ou » donne une réunion, pas une intersection": "vide", '
         '"x ≥ 3 : la borne 3 est incluse": "]-oo ; -2[ U ]3 ; +oo["}'),
        ("f", "an interval, as text", '"]2 ; 5["',
         'kind="interval", mistakes={"« et » donne une intersection, pas une réunion": "]-oo ; +oo[", '
         '"2x > 4 : divise par 2": "]4 ; 5["}'),
    ]),
    Paper("R2.9", "Équations et inéquations avec une valeur absolue, et la fonction signe", [
        ("a", "a list of solutions", "[-1, 7]",
         'ordered=False, mistakes={"une distance donnée à un point : deux solutions, une de chaque côté": [7], '
         '"|x − 3| est la distance de x à 3, pas à −3": [-7, 1]}'),
        ("b", "a list of solutions", "[-5, 4]",
         'ordered=False, mistakes={"deux cas : 2x + 1 = 9 ou 2x + 1 = −9": [4]}'),
        ("c", "an integer", "0", 'mistakes={"une valeur absolue n\'est jamais négative": 2}'),
        ("d", "an interval, as text", '"[-4 ; 2]"',
         'kind="interval", mistakes={"x + 1 = x − (−1) : c\'est la distance de x à −1": "[-2 ; 4]", '
         '"≤ : les points à distance au plus 3, donc entre les deux": "]-oo ; -4] U [2 ; +oo["}'),
        ("e", "an interval or a union, as text", '"]-oo ; -3[ U ]7 ; +oo["',
         'kind="interval", mistakes={"> : les points à distance plus grande que 5, donc à l\'extérieur": '
         '"]-3 ; 7[", "l\'inégalité est stricte : les bornes sont exclues": "]-oo ; -3] U [7 ; +oo["}'),
        ("f", "an exact decimal", "Fraction(13, 2)",
         'kind="fraction", mistakes={"la distance entre a et b est |a − b| : soustrais avec les signes": "5/2"}'),
        ("g", "a number", "-1",
         'mistakes={"(−2)² − 9 est négatif": 1, "sign ne donne que −1, 0 ou 1": -5}'),
    ]),
    Paper("R2.10", "Système 2 × 2 par substitution et par combinaison", [
        ("a", "the list [x, y]", "[2, 3]", f"mistakes={{{ORDER_XY}: [3, 2]}}"),
        ("b", "the list [x, y]", "[1, -2]", f"mistakes={{{ORDER_XY}: [-2, 1]}}"),
        ("c", "the list [x, y]", "[2, -3]", f"mistakes={{{ORDER_XY}: [-3, 2]}}"),
        ("d", "the list [x, y]", "[6, 3]", f"mistakes={{{ORDER_XY}: [3, 6]}}"),
    ]),
    Paper("R2.11", "Système 2 × 2 par la formule de Cramer", [
        ("a", "a number", "2 * (-1) - 5 * 3",
         'mistakes={"D = ad − bc : le produit bc est soustrait": 13, "d vaut −1 : garde son signe": -13}'),
        ("b", "the list [x, y]", "[3, -1]",
         f'mistakes={{{ORDER_XY}: [-1, 3], "divise par D en gardant son signe": [-3, 1]}}'),
        ("c", "1, 2 or 3", "3",
         f'{CHOICES}, mistakes={{"compare aussi les seconds membres : la seconde équation est-elle un multiple de '
         'la première, membre de droite compris ?": 1, "le déterminant est nul : pas une seule solution": 2}'),
        ("d", "1, 2 or 3", "1",
         f'{CHOICES}, mistakes={{"compare les seconds membres : sont-ils dans le même rapport que les '
         'coefficients ?": 3, "le déterminant est nul : pas une seule solution": 2}'),
    ]),
    Paper("R2.12", "Mettre en équation : trois problèmes", [
        ("a", "a number (cm²)", "8.0 * 15",
         'decimals=2, mistakes={"le périmètre compte chaque côté deux fois : 2 × (longueur + largeur)": 516.75, '
         '"on demande l\'aire, pas la longueur": 15.0, "on demande l\'aire, pas la largeur": 8.0}'),
        ("b", "a number (€)", "56 / 0.8",
         'decimals=2, mistakes={"la baisse porte sur le prix de départ, pas sur le prix réduit": 67.2}'),
        ("c", "an integer", "10", 'mistakes={"c\'est le nombre de tables de 4 places : relis la question": 12}'),
    ]),
    Paper("R2.16", "Deux mesures, deux inconnues : retrouver a et b dans y = ax + b par un système", [
        ("a", "the list [a, b]", "[25.0, -8.0]",
         'decimals=3, mistakes={"l\'ordre demandé est [a, b]": [-8.0, 25.0]}'),
        ("b", "a number (°C)", "25 * 1.4 - 8", 'decimals=2, mistakes={"T = a × u + b : n\'oublie pas b": 35.0}'),
        ("c", "a number (°C)", "51.5 - (25 * 2.4 - 8)",
         'decimals=2, mistakes={"l\'écart est la mesure moins la prédiction : son signe compte": 0.5}'),
        ("d", "1, 2 or 3", "1",
         f'{CHOICES}, mistakes={{"le point de la troisième mesure est-il sur la droite des deux premières ?": 2, '
         '"trois équations pour deux inconnues : une infinité seulement si elles disent toutes la même chose": 3}'),
    ]),
]

PAPER_CONTEXT = "# Part 0: the answers are computed exactly from the statements\nfrom fractions import Fraction"

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ R2.1 à R2.12, 🔗 R2.16)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un nombre avec un point décimal, `-1.5` ; une fraction exacte entre guillemets, `\"5/7\"` ;\n"
               "- une liste de coefficients, du plus haut degré au terme constant, zéros compris : `[2, 0, -5]` "
               "pour $2x^2 - 5$ ;\n"
               "- une liste de solutions, dans l'ordre que tu veux, où une fraction s'écrit comme un calcul : "
               "`[-2/7, 6]` ;\n"
               "- un intervalle entre guillemets, `\"]-1 ; 4]\"` ou `\"[0 ; +oo[\"` ; une réunion avec un U ; "
               "l'ensemble vide avec le mot vide entre guillemets ;\n"
               "- le nombre de solutions d'un système par son numéro : 1 pour aucune, 2 pour une seule, 3 pour une "
               "infinité.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Part A: literal calculation with SymPy (R2.22, R2.27)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from wbm.nbtools import run_pytest_group

x, y = sp.symbols("x y")


def as_interval(result):
    """(left_closed, low, high, right_closed), or None, -> the interval text that wbm.check reads."""
    if result is None:
        return "vide"
    left, low, high, right = result
    ends = ["-oo" if v == -math.inf else "+oo" if v == math.inf else repr(float(v)) for v in (low, high)]
    return f"{'[' if left else ']'}{ends[0]} ; {ends[1]}{']' if right else '['}"


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

R2_22 = Ex(
    "R2.22", "📦", 1, 15, "Vérifier développements et factorisations avec SymPy",
    "développer, tester une égalité et factoriser avec SymPy, pour vérifier un calcul fait à la main.",
    "fiche §2 et §3 ; R0 §4 (SymPy)", tracks="C, E",
    body="""Les symboles `x` et `y` sont déjà créés (cellule des outils). Trois outils de SymPy :
- `sp.expand(e)` développe et réduit ; `sp.factor(e)` factorise ;
- `sp.Poly(e, x).all_coeffs()` donne la liste des coefficients d'un polynôme en $x$, du plus haut degré au terme constant (comme dans la partie 0) ;
- deux expressions $A$ et $B$ sont égales pour **tout** $x$ exactement quand `sp.expand(A - B)` vaut `0` : c'est une preuve, pas un test sur quelques valeurs.

Avec eux :
- a) développe $(3x - 2)(x^2 + 4x - 1)$, et donne la liste de ses coefficients ;
- b) parmi ces quatre égalités, lesquelles sont vraies pour tout $x$ ? Donne leurs lettres dans un texte.

| | Égalité |
|---|---|
| A | $(x - 3)^2 = x^2 - 9$ |
| B | $(2x + 1)^2 - (2x - 1)^2 = 8x$ |
| C | $(x + 1)^3 = x^3 + 3x^2 + 3x + 1$ |
| D | $(x + 2)(x^2 - 2x + 4) = x^3 + 4$ |

- c) factorise $x^2 + x - 12$, puis donne la liste des valeurs de $x$ qui l'annulent (fiche §4, équation produit nul).

Fais d'abord a) et c) à la main : SymPy est là pour vérifier.""",
    todo='''answer_R2_22a = ...  # a) the list of coefficients
answer_R2_22b = ...  # b) the letters of the true equalities, as text
answer_R2_22c = ...  # c) the list of the values of x that make x² + x − 12 equal to 0''',
    check='''for letter, answer in zip("abc", [answer_R2_22a, answer_R2_22b, answer_R2_22c]):
    wbm.check(f"R2.22{letter}", answer)''',
    solution='''expanded = sp.expand((3*x - 2)*(x**2 + 4*x - 1))
print("a)", expanded, "->", sp.Poly(expanded, x).all_coeffs())
claims = {"A": ((x - 3)**2, x**2 - 9),
          "B": ((2*x + 1)**2 - (2*x - 1)**2, 8*x),
          "C": ((x + 1)**3, x**3 + 3*x**2 + 3*x + 1),
          "D": ((x + 2)*(x**2 - 2*x + 4), x**3 + 4)}
for letter, (left, right) in claims.items():
    gap = sp.expand(left - right)
    print("b)", letter, "vraie" if gap == 0 else f"fausse : gauche − droite = {gap}")
print("c)", sp.factor(x**2 + x - 12), "->", sp.solve(x**2 + x - 12, x))
answer_R2_22a = sp.Poly(expanded, x).all_coeffs()
answer_R2_22b = "".join(letter for letter, (left, right) in claims.items() if sp.expand(left - right) == 0)
answer_R2_22c = sp.solve(x**2 + x - 12, x)''',
    record='''wbm.record("R2.22a", [3, 10, -11, 2],
           mistakes={"all_coeffs commence par le terme de plus haut degré": [2, -11, 10, 3],
                     "le terme en x vient de deux produits, chacun avec son signe": [3, 10, 5, 2]})
wbm.record("R2.22b", "BC",
           mistakes={"A est fausse : le carré d'une différence a un double produit": "ABC",
                     "D est fausse : développe le produit, puis regarde le terme constant": "BCD",
                     "B est vraie : développe l'écart gauche − droite, il vaut 0": "C",
                     "C est vraie : développe l'écart gauche − droite, il vaut 0": "B"})
wbm.record("R2.22c", [3, -4], ordered=False,
           mistakes={"un facteur x − a s'annule pour x = a, avec le signe opposé à celui de la parenthèse": [-3, 4]})''',
    note="L'égalité D est fausse de peu : $(x + 2)(x^2 - 2x + 4) = x^3 + 8$, une identité « somme de deux cubes ». "
         "Essayer $x = 0$ suffit à la réfuter ($8 \\ne 4$) ; un test réussi, lui, n'aurait rien prouvé.",
)

R2_27_MISSING = {"A": "le carré d'une différence qui a perdu son double produit",
                 "C": "un carré qui ne porte pas sur tout le produit",
                 "D": "un moins devant une parenthèse qui ne change pas tous ses signes",
                 "F": "une division par un nombre négatif qui garde le sens",
                 "G": "une équation divisée par l'inconnue",
                 "H": "une fraction multipliée sans parenthèses autour de son numérateur"}

R2_27 = Ex(
    "R2.27", "🐛", 2, 20, "Chasse à l'erreur : six erreurs de calcul littéral",
    "repérer les erreurs classiques de calcul littéral, et les corriger.",
    "fiche §2 à §5, « Les pièges classiques »", tracks="C, E",
    body="""Un camarade a fait huit calculs. **Sans rien exécuter d'abord**, trouve les six qui sont faux.

| | Calcul |
|---|---|
| A | $(x - 5)^2 = x^2 - 25$ |
| B | $-(2x - 3) = -2x + 3$ |
| C | $(3x)^2 = 3x^2$ |
| D | $2(x + 4) - 3(x - 1) = -x + 5$ |
| E | $(x + 2)(x - 2) = x^2 - 4$ |
| F | $-4x < 10 \\iff x < -2{,}5$ |
| G | $3x^2 = 6x \\iff x = 2$ |
| H | $\\dfrac{x + 1}{2} \\times 4 = 2x + 1$ |

- a) Les lettres des calculs faux, dans un texte.
- b) Le bon résultat de D : la liste $[\\alpha, \\beta]$ de $\\alpha x + \\beta$.
- c) Le bon ensemble des solutions de l'inéquation de F, en intervalle.
- d) La bonne liste des solutions de l'équation de G.

Puis, si tu veux, confirme avec SymPy (`sp.expand`, `sp.solveset`) : la solution montre comment.""",
    todo='''answer_R2_27a = ...  # a) the letters of the wrong calculations, as text
answer_R2_27b = ...  # b) the list [alpha, beta]
answer_R2_27c = ...  # c) an interval, as text
answer_R2_27d = ...  # d) a list of solutions''',
    check='''for letter, answer in zip("abcd", [answer_R2_27a, answer_R2_27b, answer_R2_27c, answer_R2_27d]):
    wbm.check(f"R2.27{letter}", answer)''',
    solution='''identities = {"A": ((x - 5)**2, x**2 - 25), "B": (-(2*x - 3), -2*x + 3), "C": ((3*x)**2, 3*x**2),
              "D": (2*(x + 4) - 3*(x - 1), -x + 5), "E": ((x + 2)*(x - 2), x**2 - 4),
              "H": ((x + 1) / 2 * 4, 2*x + 1)}
for letter, (left, right) in identities.items():
    print(letter, "juste" if sp.expand(left - right) == 0 else f"faux : le calcul donne {sp.expand(left)}")
print("F : faux, les solutions sont", sp.solve_univariate_inequality(-4*x < 10, x, relational=False))
print("G : faux, les solutions sont", sp.solveset(3*x**2 - 6*x, x, sp.S.Reals))''',
    record=f'''wbm.record("R2.27a", "ACDFGH",
           mistakes={bug_letters_mistakes("ACDFGH", "BE", R2_27_MISSING)})
wbm.record("R2.27b", [-1, 11],
           mistakes={{"un moins devant une parenthèse change le signe de chacun de ses termes": [-1, 5],
                     "−3 × x est négatif": [5, 11]}})
wbm.record("R2.27c", "]-2.5 ; +oo[", kind="interval",
           mistakes={{"diviser par un nombre négatif retourne le sens": "]-oo ; -2.5[",
                     "la borne est 10 divisé par −4 : un nombre négatif": "]2.5 ; +oo["}})
wbm.record("R2.27d", [0, 2], ordered=False,
           mistakes={{"en divisant par x, on perd une solution : factorise 3x² − 6x": [2]}})''',
    note="Les deux calculs justes ont chacun leur piège apparent : B change bien les deux signes, et E est "
         "l'identité $(a + b)(a - b) = a^2 - b^2$. Pour H, le 4 multiplie tout le numérateur : "
         "$\\frac{x + 1}{2} \\times 4 = 2(x + 1) = 2x + 2$.",
)

PART_A = Part("A", "Calcul littéral : vérifier avec SymPy, chasser les erreurs",
              "Fiche §1 à §3. SymPy comme outil de vérification de tes calculs papier, et une chasse aux erreurs "
              "classiques du calcul littéral.", given=TOOLS, exercises=[R2_22, R2_27])

# ---------------------------------------------------------------------------
# Part B: equations and inequalities (R2.18, R2.19, R2.20, R2.23, R2.28)
# ---------------------------------------------------------------------------
LOAD_LEARNER = 'mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="R2")  # reload your saved file'
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en R1). Ouvre ta copie `mon_travail/mymath/algebra.py`, lis la docstring "
         "du module **et** celle de la fonction en entier, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "N'utilise ni SymPy ni NumPy dans `algebra.py` : les tests s'en servent pour vérifier tes résultats.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of algebra.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_r2_algebra.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_r2_algebra.py", "{keyword}", impl="ref")')]


R2_18 = Ex(
    "R2.18", "🔨", 1, 25, "Résoudre ax + b = 0 dans tous les cas · `solve_linear`",
    "programmer la résolution de ax + b = 0, cas dégénérés compris.",
    "fiche §4, « L'équation ax + b = 0 » ; workbookIA 0A §100.4.2", tracks="C, E", mymath="algebra.py",
    body=HOWTO + """

Écris `solve_linear(a, b)` : les **trois cas** de la fiche (§4). Une solution se rend dans une liste, `[x]` (divise avec `/`, pour obtenir un flottant) ; aucune solution, la liste vide `[]` ; tous les réels, la chaîne `"all"`. Compare `a` (et `b`) à 0 avec `==` : les tests des cas dégénérés utilisent des entiers.

La vérification calcule `solve_linear(-5, 2)`, la longueur de `solve_linear(0, -3)` et `solve_linear(0, 0)`, puis lance les tests.""",
    todo=LOAD_LEARNER,
    check='''with wbm.attempt("R2.18a"):
    wbm.check("R2.18a", mymath.algebra.solve_linear(-5, 2), computed=True)
with wbm.attempt("R2.18b"):
    wbm.check("R2.18b", len(mymath.algebra.solve_linear(0, -3)), computed=True)
with wbm.attempt("R2.18c"):
    wbm.check("R2.18c", mymath.algebra.solve_linear(0, 0), computed=True)''',
    solution=LOAD_REF + '''
for a, b in [(-5, 2), (0, -3), (0, 0)]:
    print(f"solve_linear({a}, {b}) =", mymath.algebra.solve_linear(a, b))''',
    record='''wbm.record("R2.18a", [0.4], decimals=4,
           mistakes={"la solution de ax + b = 0 est −b/a : attention au signe": [-0.4],
                     "la solution est −b/a, pas −a/b": [2.5]})
wbm.record("R2.18b", 0,
           mistakes={"0x − 3 = 0 n'est jamais vrai : aucune solution, la liste vide (pas \\"all\\")": 3,
                     "aucune solution : la liste vide, sans élément": 1})
wbm.record("R2.18c", "all")''',
    after=tests_cells("test_solve_linear_ and not inequality"),
    note="L'ordre des tests compte : on regarde d'abord si `a == 0`, sinon la division `-b / a` lèverait "
         "`ZeroDivisionError`. C'est la même démarche que sur papier : avant de diviser, s'assurer qu'on ne divise "
         "pas par 0.",
)

R2_19 = Ex(
    "R2.19", "🔨", 2, 40, "Résoudre ax + b ≤ 0 et rendre l'intervalle des solutions · `solve_linear_inequality`",
    "programmer la résolution d'une inéquation du premier degré, changement de sens et cas dégénérés compris.",
    "R2.18 ; fiche §5 ; workbookIA 0A §100.6.2 (`raise`)", tracks="C", mymath="algebra.py",
    body="""Écris `solve_linear_inequality(a, b, sense="<")` : l'ensemble des solutions de $ax + b < 0$ (ou `"<="`, `">"`, `">="`), rendu comme un **intervalle** `(left_closed, low, high, right_closed)`, ou `None` pour l'ensemble vide (la docstring du module explique la convention). Une démarche :
1. un `sense` qui n'est pas l'un des quatre symboles lève une `ValueError` ;
2. si `a == 0`, l'inéquation dit « $b < 0$ » (ou $b \\le 0$…), vraie pour tout $x$ (toute la droite) ou jamais (`None`) ;
3. sinon, la borne est $-\\frac{b}{a}$, et diviser par un $a$ **négatif** retourne le sens (fiche §5) ;
4. `"<"` et `"<="` donnent $]-\\infty \\;;\\; r[$ ou $]-\\infty \\;;\\; r]$ ; `">"` et `">="` donnent $]r \\;;\\; +\\infty[$ ou $[r \\;;\\; +\\infty[$, avec `math.inf` pour l'infini, toujours ouvert.

La vérification transforme ton tuple en texte avec `as_interval` (cellule des outils) pour `wbm.check` : `solve_linear_inequality(-4, -6, ">=")`, puis `solve_linear_inequality(0, 3, "<=")`.""",
    todo=LOAD_LEARNER,
    check='''with wbm.attempt("R2.19a"):
    wbm.check("R2.19a", as_interval(mymath.algebra.solve_linear_inequality(-4, -6, ">=")), computed=True)
with wbm.attempt("R2.19b"):
    wbm.check("R2.19b", as_interval(mymath.algebra.solve_linear_inequality(0, 3, "<=")), computed=True)''',
    solution=LOAD_REF + '''
for a, b, sense in [(-4, -6, ">="), (0, 3, "<=")]:
    result = mymath.algebra.solve_linear_inequality(a, b, sense)
    print(f"solve_linear_inequality({a}, {b}, {sense!r}) = {result}, soit {as_interval(result)}")''',
    record='''wbm.record("R2.19a", "]-oo ; -1.5]", kind="interval",
           mistakes={"a est négatif : diviser par a retourne le sens": "[-1.5 ; +oo[",
                     "l'inégalité est large : la borne est incluse": "]-oo ; -1.5[",
                     "la borne est −b/a : attention au signe": "]-oo ; 1.5]"})
wbm.record("R2.19b", "vide", kind="interval",
           mistakes={"avec a = 0, l'inéquation ne dépend plus de x : elle est vraie pour tout x, ou jamais ; ici ?":
                     "]-oo ; +oo["})''',
    after=tests_cells("test_solve_linear_inequality_"),
    note="Un dictionnaire évite une cascade de `if` : `{\"<\": \">\", \"<=\": \">=\", \">\": \"<\", \">=\": \"<=\"}"
         "[sense]` donne le sens retourné. Les cas où l'inéquation ne dépend plus de $x$ se règlent de la même façon, "
         "avec `{\"<\": b < 0, \"<=\": b <= 0, ...}[sense]`.",
)

R2_20 = Ex(
    "R2.20", "🔨", 2, 30, "Résoudre |x − a| = c · `solve_abs_equation`",
    "programmer la résolution de |x − a| = c en lisant la valeur absolue comme une distance.",
    "fiche §6", tracks="C", mymath="algebra.py",
    body="""Écris `solve_abs_equation(a, c)` : les points à distance `c` de `a` (fiche §6, le tableau des cas), rendus dans une liste de flottants **dans l'ordre croissant** : deux solutions, une seule, ou aucune.

La vérification calcule `solve_abs_equation(-1.5, 4)` et `solve_abs_equation(7, 0)`.""",
    todo=LOAD_LEARNER,
    check='''with wbm.attempt("R2.20a"):
    wbm.check("R2.20a", mymath.algebra.solve_abs_equation(-1.5, 4), computed=True)
with wbm.attempt("R2.20b"):
    wbm.check("R2.20b", mymath.algebra.solve_abs_equation(7, 0), computed=True)''',
    solution=LOAD_REF + '''
print("solve_abs_equation(-1.5, 4) =", mymath.algebra.solve_abs_equation(-1.5, 4))
print("solve_abs_equation(7, 0)    =", mymath.algebra.solve_abs_equation(7, 0))''',
    record='''wbm.record("R2.20a", [-5.5, 2.5], decimals=4,
           mistakes={"rends les solutions dans l'ordre croissant": [2.5, -5.5],
                     "les points à distance c de a sont a − c et a + c": [-2.5, 5.5]})
wbm.record("R2.20b", [7.0], decimals=4,
           mistakes={"à distance 0 de a, il n'y a qu'un point : a, une seule fois": [7.0, 7.0]})''',
    after=tests_cells("test_solve_abs_equation_"),
)

R2_23 = Ex(
    "R2.23", "📦", 1, 15, "Résoudre avec `sympy.solve` et lire son résultat",
    "résoudre des équations et un système avec SymPy, et savoir lire (et se méfier de) ce qu'il renvoie.",
    "fiche §4 et §7 (les cellules SymPy)", tracks="C",
    body="""`sp.solve(e, x)` résout « $e = 0$ » et renvoie une **liste** de solutions ; pour une équation $A = B$, on lui donne `A - B` (fiche §4). `sp.solveset(e, x, sp.S.Reals)` renvoie un **ensemble** de SymPy, qui sait dire « aucune solution » (`EmptySet`) et « tous les réels » (`Reals`).

- a) Résous $4x - 7 = x + 5$ avec `sp.solve`, et donne **la solution** (un nombre, pas la liste).
- b) Résous $3(x - 2) = 3x - 6$ avec `sp.solve` : combien d'éléments la liste renvoyée a-t-elle ? Fais de même avec $5(x - 1) = 5x - 2$. Combien de solutions chacune de ces deux équations a-t-elle vraiment (fiche §4) ?
- c) Résous à nouveau $3(x - 2) = 3x - 6$, avec `sp.solveset` sur les réels, et donne l'ensemble obtenu (tu peux le passer tel quel à `wbm.check`).
- d) Résous le système $\\begin{cases} 7x - 2y = 3 \\\\ x + y = 3 \\end{cases}$ avec `sp.solve([e1, e2], [x, y])` : le résultat est un **dictionnaire**. Donne la liste $[x, y]$ lue dedans.""",
    todo='''answer_R2_23a = ...  # a) a number
answer_R2_23b = ...  # b) an integer: the length of the list returned for 3(x − 2) = 3x − 6
answer_R2_23c = ...  # c) the set returned by sp.solveset (the SymPy object itself is fine)
answer_R2_23d = ...  # d) the list [x, y]''',
    check='''for letter, answer in zip("abcd", [answer_R2_23a, answer_R2_23b, answer_R2_23c, answer_R2_23d]):
    wbm.check(f"R2.23{letter}", answer)''',
    solution='''print("a)", sp.solve(4*x - 7 - (x + 5), x))
always = sp.solve(3*(x - 2) - (3*x - 6), x)
never = sp.solve(5*(x - 1) - (5*x - 2), x)
print("b) 3(x − 2) = 3x − 6 :", always, " ; 5(x − 1) = 5x − 2 :", never, " -> la même liste vide !")
print("c)", sp.solveset(3*(x - 2) - (3*x - 6), x, sp.S.Reals), "et", sp.solveset(5*(x - 1) - (5*x - 2), x, sp.S.Reals))
system = sp.solve([7*x - 2*y - 3, x + y - 3], [x, y])
print("d)", system)
answer_R2_23a = sp.solve(4*x - 7 - (x + 5), x)[0]
answer_R2_23b = len(always)
answer_R2_23c = sp.solveset(3*(x - 2) - (3*x - 6), x, sp.S.Reals)
answer_R2_23d = [system[x], system[y]]''',
    record='''wbm.record("R2.23a", 4.0, decimals=2,
           mistakes={"pour une équation A = B, donne A − B à sp.solve, pas A seul": 1.75})
wbm.record("R2.23b", 0,
           mistakes={"compte les éléments de la liste que renvoie sp.solve (len), pas les solutions de l'équation": 1})
wbm.record("R2.23c", "]-oo ; +oo[", kind="interval",
           mistakes={"tout réel vérifie 3(x − 2) = 3x − 6 : ce n'est pas l'ensemble vide": "vide"})
wbm.record("R2.23d", [1, 2], mistakes={"l'ordre demandé est [x, y]": [2, 1]})''',
    note="`sp.solve` renvoie la **même** liste vide pour une équation sans solution et pour une équation vraie pour "
         "tout $x$ : sa réponse seule ne permet pas de les distinguer. `sp.solveset` renvoie `EmptySet` ou `Reals`. "
         "C'est pour cette raison que `solve_linear` (R2.18) rend la chaîne `\"all\"` et pas `[]` quand tous les "
         "réels sont solutions.",
)

R2_28_FAULTY = '''# Three faulty versions of solve_linear: a good test catches each one
def solve_linear_wrong_sign(a, b):
    if a == 0:
        return "all" if b == 0 else []
    return [b / a]


def solve_linear_divides_by_zero(a, b):
    return [-b / a]


def solve_linear_forgets_all(a, b):
    if a == 0:
        return []
    return [-b / a]'''

R2_28_CHECK = '''with wbm.attempt("R2.28"):
    reference = wbm.load_mymath("ref", alias="mymath_ref").algebra.solve_linear
    try:
        check_solve_linear(reference)
    except NotImplementedError:
        raise
    except Exception as exc:  # noqa: BLE001 - a test that fails on a right function
        print(f"❌ Ex R2.28 : ton test échoue sur une fonction juste ({type(exc).__name__} {exc}) : relis tes assert.")
    else:
        missed = []
        for faulty in (solve_linear_wrong_sign, solve_linear_divides_by_zero, solve_linear_forgets_all):
            try:
                check_solve_linear(faulty)
            except Exception:  # noqa: BLE001 - an AssertionError or any other error: the fault is caught
                continue
            missed.append(faulty.__name__)
        if missed:
            print("❌ Ex R2.28 : ton test passe sur une version fausse :", ", ".join(missed),
                  "; ajoute le cas qu'elle rate.")
        else:
            print("✅ Ex R2.28 : ton test passe sur la fonction juste et attrape les trois versions fausses.")'''

R2_28 = Ex(
    "R2.28", "🛠️", 1, 15, "Écrire un test pytest pour une fonction qui résout une équation",
    "écrire un test qui vérifie une fonction de résolution, en substituant la solution plutôt qu'en la recopiant.",
    "R2.18 ; fiche §4", tracks="C",
    body="""Un **test** appelle une fonction sur des cas dont on connaît la réponse, et échoue (`assert`) si elle se trompe. `pytest` exécute toutes les fonctions `test_...` d'un fichier `tests/test_....py` : c'est ce que lance `run_pytest_group`.

Écris le corps de `check_solve_linear(solve_linear)` : des `assert` qui vérifient la fonction `solve_linear` qu'on lui passe, dans les trois cas de la fiche (§4) :
1. un cas à une solution, **vérifié en substituant** : la liste rendue a un seul élément `s`, et `a * s + b` est presque nul (`abs(...) < 1e-9`). C'est plus sûr que de comparer à une valeur que tu aurais calculée (et peut-être mal) ;
2. un cas sans solution : la liste vide ;
3. un cas où tous les réels sont solutions : la chaîne `"all"`.

La vérification lance ton test sur une version juste (la référence), où il doit **passer**, puis sur trois versions fausses (cellule suivante), où il doit **échouer** à chaque fois : un test qui ne rate aucune erreur ne sert à rien. Dans un fichier de tests, tu écrirais ensuite `def test_solve_linear(): check_solve_linear(mymath.algebra.solve_linear)`.""",
    given=R2_28_FAULTY,
    todo='''def check_solve_linear(solve_linear):
    """Fail (assert) if solve_linear is wrong in one of the three cases of the sheet (§4)."""
    raise NotImplementedError("écris tes assert")''',
    check=R2_28_CHECK,
    solution='''def check_solve_linear(solve_linear):
    """Fail (assert) if solve_linear is wrong in one of the three cases of the sheet (§4)."""
    for a, b in [(3, -7), (-2, 5), (0.5, 4)]:            # one solution: substitute it back
        result = solve_linear(a, b)
        assert isinstance(result, list) and len(result) == 1, f"one solution expected for {a}x + {b} = 0"
        assert abs(a * result[0] + b) < 1e-9, f"{result[0]} is not a solution of {a}x + {b} = 0"
    assert solve_linear(0, 4) == [], "0x + 4 = 0 has no solution"
    assert solve_linear(0, 0) == "all", "0x + 0 = 0 holds for every x"


''' + R2_28_CHECK,
    note="Trois cas suffisent ici parce que la fiche en compte trois. Un bon test vise les **cas limites** "
         "(un coefficient nul) et vérifie une **propriété** (la solution annule l'expression) plutôt qu'une valeur "
         "recopiée : c'est ainsi que sont écrits les tests de `tests/test_r2_algebra.py`.",
)

PART_B = Part("B", "Équations et inéquations",
              "Fiche §4 à §6. Trois fonctions de `mymath/algebra.py` (équation, inéquation, valeur absolue), "
              "SymPy et ses pièges, et un test que tu écris toi-même.",
              exercises=[R2_18, R2_19, R2_20, R2_23, R2_28])

# ---------------------------------------------------------------------------
# Part C: 2 × 2 systems (R2.21, R2.26, R2.24, R2.25)
# ---------------------------------------------------------------------------
R2_21 = Ex(
    "R2.21", "🔨", 2, 40, "Système 2 × 2 par la formule de Cramer · `solve_2x2`",
    "programmer la formule de Cramer, et refuser un système de déterminant nul.",
    "fiche §7, « Par la formule de Cramer » ; workbookIA 0A §100.6.2 (`raise`)", tracks="C, E", mymath="algebra.py",
    body=HOWTO + """

Écris `solve_2x2(A, b)` : `A` contient les coefficients ligne par ligne, `[[a, b], [c, d]]`, et `b` les seconds membres, `[e, f]` (attention : dans le code, `b` est la liste des seconds membres, pas le coefficient ; dépaquette avec `(a11, a12), (a21, a22) = A`).
1. Calcule le déterminant $D = ad - bc$.
2. Si $D = 0$, lève une `ValueError` avec un message clair : le système n'a pas **une seule** solution.
3. Sinon, calcule $x$ et $y$ par la formule de Cramer, et rends le **tuple** `(x, y)`.

La vérification calcule `solve_2x2([[3, 4], [5, -2]], [5.5, 13.5])`, puis le nom de l'erreur levée pour un système de déterminant nul (avec `raised`, de la cellule des outils).""",
    todo=LOAD_LEARNER,
    check='''with wbm.attempt("R2.21a"):
    wbm.check("R2.21a", list(mymath.algebra.solve_2x2([[3, 4], [5, -2]], [5.5, 13.5])), computed=True)
with wbm.attempt("R2.21b"):
    wbm.check("R2.21b", raised(mymath.algebra.solve_2x2, [[2, -5], [-4, 10]], [1, 3]), computed=True)''',
    solution=LOAD_REF + '''
print("solve_2x2([[3, 4], [5, -2]], [5.5, 13.5]) =", mymath.algebra.solve_2x2([[3, 4], [5, -2]], [5.5, 13.5]))
print("déterminant nul :", raised(mymath.algebra.solve_2x2, [[2, -5], [-4, 10]], [1, 3]))''',
    record='''wbm.record("R2.21a", [2.5, -0.5], decimals=4,
           mistakes={"rends le couple dans l'ordre (x, y)": [-0.5, 2.5],
                     "D = ad − bc : le produit bc est soustrait": [-65 / 14, 13 / 14],
                     "les numérateurs sont ed − bf (pour x) et af − ec (pour y) : l'ordre des produits compte":
                     [-2.5, 0.5]})
wbm.record("R2.21b", "ValueError",
           mistakes={"teste D == 0 avant de diviser, et lève une ValueError": "ZeroDivisionError",
                     "un déterminant nul : pas une seule solution, lève une ValueError au lieu de rendre un couple":
                     "aucune"})''',
    after=tests_cells("test_solve_2x2_"),
)

R2_26 = Ex(
    "R2.26", "🎨", 2, 20, "Un système, deux droites : voir la solution",
    "tracer les deux droites d'un système et lire sa solution, dans les trois cas.",
    "fiche §7, « Le regard géométrique » ; R0 (matplotlib)", tracks="C, E",
    body="""Complète `plot_system(A, b, ax=None)`, qui dessine le système $a_1 x + b_1 y = c_1$, $a_2 x + b_2 y = c_2$ (avec `A = [[a1, b1], [a2, b2]]` et `b = [c1, c2]`) :
- chaque équation est une droite, tracée pour $x$ de $-5$ à $5$ : si son coefficient de $y$ n'est pas nul, $y = \\frac{c - a x}{b}$ ; sinon, la droite est **verticale**, $x = \\frac{c}{a}$ (`ax.axvline`) ;
- si le déterminant n'est pas nul, marque le point commun (calculé avec `np.linalg.solve(A, b)`) et écris ses coordonnées dans le titre ;
- sinon, le titre dit « une infinité de solutions » quand les droites sont confondues, ce qui arrive quand, en plus, $a_1 c_2 - a_2 c_1 = 0$ et $b_1 c_2 - b_2 c_1 = 0$ (R2.15), et « aucune solution » dans l'autre cas ;
- une légende avec les deux équations, une grille, les axes nommés, une fenêtre $[-5 ; 5] \\times [-5 ; 5]$ ;
- si on lui donne `ax` (une case d'une figure à plusieurs graphiques), elle dessine dedans ; sinon, elle crée sa figure (`fig, ax = plt.subplots()`) et l'affiche.

La vérification dessine $\\begin{cases} x + 3y = 5 \\\\ 2x = -2 \\end{cases}$ (une droite verticale). Lis la solution sur ta figure, note-la dans ta copie, et compare ta figure à celle de `05_solutions.ipynb`. R2.24 se servira de ta fonction.""",
    todo='''def plot_system(A, b, ax=None):
    """Draw the two lines of the system A·(x, y) = b, and their common point when there is exactly one."""
    raise NotImplementedError("trace les deux droites, puis le point commun")''',
    check='''with wbm.attempt("R2.26"):
    plot_system([[1, 3], [2, 0]], [5, -2])''',
    solution='''def plot_system(A, b, ax=None):
    """Draw the two lines of the system A·(x, y) = b, and their common point when there is exactly one."""
    own_figure = ax is None
    if own_figure:
        fig, ax = plt.subplots(figsize=(5, 4.2))
    xs = np.linspace(-5, 5, 200)
    for k, ((p, q), c) in enumerate(zip(A, b)):
        label = f"{p}x {'+' if q >= 0 else '−'} {abs(q)}y = {c}"
        style = "-" if k == 0 else "--"
        if q != 0:
            ax.plot(xs, (c - p * xs) / q, style, color=f"C{k}", label=label)
        else:
            ax.axvline(c / p, linestyle=style, color=f"C{k}", label=label)
    (a1, b1), (a2, b2) = A
    c1, c2 = b
    if a1 * b2 - b1 * a2 != 0:
        px, py = np.linalg.solve(np.array(A, dtype=float), np.array(b, dtype=float))
        ax.plot(px, py, "o", color="black", zorder=3)
        ax.set_title(f"une seule solution : ({px:g} ; {py:g})")
    elif a1 * c2 - a2 * c1 == 0 and b1 * c2 - b2 * c1 == 0:
        ax.set_title("une infinité de solutions (droites confondues)")
    else:
        ax.set_title("aucune solution (droites parallèles)")
    ax.axhline(0, color="gray", linewidth=0.6)
    ax.axvline(0, color="gray", linewidth=0.6)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8, loc="lower left")
    if own_figure:
        plt.show()


plot_system([[1, 3], [2, 0]], [5, -2])''',
    note="La seconde équation, $2x = -2$, ne contient pas $y$ : c'est la droite verticale $x = -1$. Le point commun "
         "est $(-1 \\;;\\; 2)$, et la substitution le confirme : $-1 + 3 \\times 2 = 5$.",
)

R2_24_SYSTEMS = '''# The three systems of R2.24: name -> (A, b), for a1·x + b1·y = c1, a2·x + b2·y = c2
SYSTEMS_24 = {
    "S1": ([[5, 1], [10, 2]], [2, 7]),
    "S2": ([[1, 2], [3, -1]], [4, 5]),
    "S3": ([[3, -2], [-6, 4]], [1, -2]),
}'''

R2_24_EXPERIMENT = '''for name, (A, b) in SYSTEMS_24.items():
    (a1, b1), (a2, b2) = A
    print(f"{name} : déterminant D = ad − bc = {a1 * b2 - b1 * a2}")
with wbm.attempt("R2.24 figure"):
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.2))
    for ax, (name, (A, b)) in zip(axes, SYSTEMS_24.items()):
        plot_system(A, b, ax=ax)
        ax.set_title(f"{name} : {ax.get_title()}", fontsize=10)
    fig.tight_layout()
    plt.show()'''

R2_24 = Ex(
    "R2.24", "🔮", 1, 15, "Prédire le nombre de solutions de trois systèmes, puis tracer leurs droites",
    "prévoir le nombre de solutions d'un système en regardant ses coefficients, puis le voir sur les droites.",
    "fiche §7 ; R2.26 (ta fonction `plot_system`)", tracks="C, E", hypothesis=True,
    body="""Trois systèmes :

$$S_1 : \\begin{cases} 5x + y = 2 \\\\ 10x + 2y = 7 \\end{cases} \\qquad S_2 : \\begin{cases} x + 2y = 4 \\\\ 3x - y = 5 \\end{cases} \\qquad S_3 : \\begin{cases} 3x - 2y = 1 \\\\ -6x + 4y = -2 \\end{cases}$$

**Avant d'exécuter quoi que ce soit**, et sans les résoudre, prédis le nombre de solutions de chacun : 1 pour aucune, 2 pour une seule, 3 pour une infinité. Regarde les coefficients de $x$ et de $y$ d'une équation à l'autre, puis les seconds membres (fiche §7). Écris tes trois prédictions, vérifie-les, puis lance l'expérience : elle calcule les trois déterminants et trace les trois systèmes avec ta fonction `plot_system` (R2.26).""",
    given=R2_24_SYSTEMS,
    todo='''prediction_R2_24a = ...  # S1: 1, 2 or 3, written BEFORE running the experiment below
prediction_R2_24b = ...  # S2: 1, 2 or 3
prediction_R2_24c = ...  # S3: 1, 2 or 3''',
    check='''for letter, prediction in zip("abc", [prediction_R2_24a, prediction_R2_24b, prediction_R2_24c]):
    wbm.check(f"R2.24{letter}", prediction)''',
    record='''wbm.record("R2.24a", 1, choices=[1, 2, 3], prediction=True,
           mistakes={"les coefficients sont proportionnels : compare aussi les seconds membres": 3,
                     "des coefficients proportionnels donnent un déterminant nul : pas une seule solution": 2})
wbm.record("R2.24b", 2, choices=[1, 2, 3], prediction=True,
           mistakes={"les coefficients ne sont pas proportionnels : les droites ne sont pas parallèles": 1,
                     "les coefficients ne sont pas proportionnels : les deux équations ne disent pas la même chose": 3})
wbm.record("R2.24c", 3, choices=[1, 2, 3], prediction=True,
           mistakes={"compare les seconds membres : sont-ils dans le même rapport que les coefficients ?": 1,
                     "des coefficients proportionnels donnent un déterminant nul : pas une seule solution": 2})''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes trois prédictions écrites."),
        ("todo", guarded(R2_24_EXPERIMENT, ["prediction_R2_24a", "prediction_R2_24b", "prediction_R2_24c"],
                         "⏳ Écris d'abord tes trois prédictions (1, 2 ou 3), puis exécute à nouveau.")),
        ("solution", R2_24_EXPERIMENT),
    ],
    note="Dans $S_1$, la seconde équation a les coefficients de la première multipliés par 2, mais pas son second "
         "membre ($2 \\times 2 \\ne 7$) : deux droites parallèles. Dans $S_3$, tout est multiplié par $-2$, second "
         "membre compris : la même droite. Seul $S_2$ a des coefficients non proportionnels, donc un déterminant non "
         "nul ($-7$) et une seule solution, $(2 \\;;\\; 1)$.",
)

R2_25_PLOT = '''with wbm.attempt("R2.25 figure"):
    gaps = np.logspace(-4, -2, 60)                    # c − 1, from 0.0001 to 0.01
    ys = [solve_near(1 + gap)[1] for gap in gaps]
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.loglog(gaps, ys, "o-", markersize=3)
    ax.set_xlabel("c − 1, le déterminant (échelle logarithmique)")
    ax.set_ylabel("y, la solution (échelle logarithmique)")
    ax.set_title("Quand le déterminant tend vers 0, la solution s'envole")
    ax.grid(True, which="both", alpha=0.3)
    plt.show()'''

R2_25 = Ex(
    "R2.25", "🔬", 2, 20,
    "Expérience : un système presque dégénéré, un coefficient bouge de 0,001 et la solution s'envole",
    "voir qu'un système de déterminant presque nul est très sensible à ses coefficients.",
    "fiche §7 ; R2.24", tracks="C",
    body="""On étudie le système $\\begin{cases} x + y = 2 \\\\ x + c\\,y = 2{,}001 \\end{cases}$ pour des valeurs de $c$ proches de 1. Ses deux droites sont presque parallèles.

- Écris `solve_near(c)` : la solution `[x, y]`, calculée avec `np.linalg.solve`.
- a) Sa solution pour $c = 1{,}001$.
- b) Sa solution pour $c = 1{,}002$ : le coefficient n'a bougé que de 0,001.
- c) Son déterminant pour $c = 1{,}001$ (calcule-le dans ta tête, puis en Python).
- d) La valeur de $y$ pour $c = 1{,}0001$.

Puis lance l'expérience : elle trace $y$ en fonction de $c - 1$, de $10^{-4}$ à $10^{-2}$, sur deux échelles logarithmiques. Dans ta copie, dis en une phrase ce que la courbe montre, et pourquoi un déterminant presque nul est un signal d'alarme.""",
    todo='''def solve_near(c):
    """Solution [x, y] of x + y = 2, x + c·y = 2.001 (with np.linalg.solve)."""
    raise NotImplementedError("pose la matrice A et le second membre, puis appelle np.linalg.solve")


answer_R2_25c = ...  # c) the determinant for c = 1.001 (a number)''',
    check='''with wbm.attempt("R2.25a"):
    wbm.check("R2.25a", list(solve_near(1.001)), computed=True)
with wbm.attempt("R2.25b"):
    wbm.check("R2.25b", list(solve_near(1.002)), computed=True)
wbm.check("R2.25c", answer_R2_25c)
with wbm.attempt("R2.25d"):
    wbm.check("R2.25d", solve_near(1.0001)[1], computed=True)''',
    solution='''def solve_near(c):
    """Solution [x, y] of x + y = 2, x + c·y = 2.001 (with np.linalg.solve)."""
    return list(np.linalg.solve(np.array([[1, 1], [1, c]], dtype=float), np.array([2, 2.001])))


for c in (1.001, 1.002, 1.0001):
    print(f"c = {c} : (x, y) = ({solve_near(c)[0]:.6g}, {solve_near(c)[1]:.6g}) ; déterminant = {c - 1:.6g}")
answer_R2_25c = 1 * 1.001 - 1 * 1''',
    record='''wbm.record("R2.25a", [1.0, 1.0], decimals=4,
           mistakes={"le second membre de la seconde équation est 2,001, pas 2": [2.0, 0.0]})
wbm.record("R2.25b", [1.5, 0.5], decimals=4,
           mistakes={"le coefficient c est celui de y dans la seconde équation, pas celui de x": [0.5, 1.5]})
wbm.record("R2.25c", 1.001 - 1, decimals=6,
           mistakes={"D = ad − bc : le produit de la diagonale moins l'autre produit, dans cet ordre": -0.001})
wbm.record("R2.25d", 10.0, decimals=3)''',
    after=[
        ("md", "**L'expérience** : $y$ en fonction de $c - 1$."),
        ("code", R2_25_PLOT),
    ],
    note="Un coefficient qui bouge de 0,001 (une erreur de mesure, un arrondi) fait passer $y$ de 1 à 0,5 : le "
         "système est **mal conditionné**. Ici $y = \\frac{0{,}001}{c - 1}$ : diviser par un déterminant minuscule "
         "amplifie la moindre erreur. Sur la figure, la droite de pente −1 en échelles logarithmiques le dit : $y$ "
         "est multiplié par 10 quand $c - 1$ est divisé par 10. Le chapitre 9 de workbookIA parle du "
         "**conditionnement** d'un problème de moindres carrés, et des colonnes redondantes qui le dégradent.",
)

PART_C = Part("C", "Systèmes de deux équations à deux inconnues",
              "Fiche §7. La formule de Cramer programmée, les deux droites d'un système, trois systèmes à prédire, "
              "et un système presque dégénéré.", exercises=[R2_21, R2_26, R2_24, R2_25])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | R2.1 à R2.12, R2.16 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# R2 · Calcul littéral et équations — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/r2_calcul_litteral/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py R2`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# R2 · Calcul littéral et équations — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : développer, factoriser, résoudre équations, inéquations, "
               "valeurs absolues et systèmes, mettre en équation.\n"
               "- Écrire les quatre fonctions de `mymath/algebra.py` et les tester.\n"
               "- Vérifier un calcul avec SymPy et savoir lire sa réponse ; voir les droites d'un système, et un "
               "système presque dégénéré.\n\n"
               "**Rappel express.** $(a \\pm b)^2 = a^2 \\pm 2ab + b^2$ et $(a + b)(a - b) = a^2 - b^2$ ; "
               "$ax + b = 0$ a la solution $-\\frac{b}{a}$ si $a \\ne 0$ ; diviser une inéquation par un négatif "
               "retourne le sens ; $|x - a| = c$ donne $a \\pm c$ si $c > 0$ ; un système 2 × 2 a une seule "
               "solution exactement quand $D = ad - bc \\ne 0$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Développes-tu et factorises-tu sans erreur de signe, identités remarquables comprises, et "
               "vérifies-tu ton résultat (valeur test ou SymPy) ?\n"
               "2. Résous-tu une équation ou une inéquation du premier degré, une équation produit nul et une "
               "valeur absolue, en écrivant l'ensemble des solutions (intervalles compris) ?\n"
               "3. Résous-tu un système 2 × 2 de trois façons, et sais-tu dire, avec le déterminant, s'il a une "
               "seule solution ?\n\n"
               "**La suite** : R3, *Fonctions*. Dans workbookIA, continue le chapitre 0A au rythme de ton tableau "
               "de bord.")]


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
