#!/usr/bin/env python
"""Build the two notebooks of chapter R8 from a single source (used by Claude).

    python tools/chapters/build_r8.py
    python tools/run_all_notebooks.py chapitres/r8_probabilites/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/r8_probabilites/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ R8.1 to R8.10, 🔗 R8.13); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer nor the calculation that gives it. An exact
probability is answered by an irreducible fraction between quotes, a count by an integer, a law by the list of its
probabilities in the increasing order of the values.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "R8"
FOLDER = "chapitres/r8_probabilites"

F = 'kind="fraction", simplified=True'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("R8.1", "Décrire univers et événements : dés, cartes, pièces", [
        ("a", "an integer", "2 ** 4",
         'mistakes={"chaque pièce a 2 issues, et l\'ordre des lancers compte : principe multiplicatif": 8, '
         '"une issue est la suite des quatre résultats, pas le nombre de piles": 5}'),
        ("b", "an integer", "6",
         'mistakes={"une issue est une suite ordonnée : PPFF, PFPF et FFPP sont trois issues différentes": {1, 2, 4}}'),
        ("c", "an integer", "15",
         'mistakes={"passe par le contraire, « aucun pile », et retire-le de toutes les issues": {1, 16}}'),
        ("d", "an integer", "5",
         'mistakes={"« au plus un pile » : zéro pile ou un pile, les deux cas comptent": {1, 4}, '
         '"« au plus un » n\'est pas « au moins un »": 15}'),
        ("e", "an integer", "2",
         'mistakes={"A ∩ B : les cartes qui sont à la fois des as et noires": {4, 16, 18}}'),
        ("f", "an integer", "18",
         'mistakes={"des cartes sont comptées deux fois : retire celles qui sont dans A et dans B": 20, '
         '"c\'est A ∩ B ; A ∪ B contient les as, les cartes noires, et celles qui sont les deux": 2}'),
        ("g", "an integer", "14",
         'mistakes={"c\'est A ∪ B ; « ni l\'un ni l\'autre » en est le contraire": 18, '
         '"les as rouges sont des as : ils sont exclus aussi": 16}'),
        ("h", "True or False", "False",
         'mistakes={"incompatibles veut dire sans issue commune : cherche une carte qui soit un as et rouge": True}'),
    ]),

    Paper("R8.2", "Probabilités par équiprobabilité", [
        ("a", "a fraction, as text", "Fraction(2, 11)",
         F + ', mistakes={"compte chaque lettre autant de fois qu\'elle apparaît dans le mot": "1/11"}'),
        ("b", "a fraction, as text", "Fraction(5, 11)",
         F + ', mistakes={"compte chaque voyelle autant de fois qu\'elle apparaît (une voyelle revient)": "4/11"}'),
        ("c", "a fraction, as text", "Fraction(4, 11)",
         F + ', mistakes={"ce sont toutes les consonnes : retire aussi les B": "6/11", '
         '"ce sont toutes les lettres sauf les B : retire aussi les voyelles": "9/11"}'),
        ("d", "an integer", "6 * 4",
         'mistakes={"principe multiplicatif : on multiplie les issues des deux dés, on ne les additionne pas": 10}'),
        ("e", "a fraction, as text", "Fraction(4, 24)",
         F + ', mistakes={"liste les couples (dé à 6 faces, dé à 4 faces) de somme 5, sans en oublier : le dé à 4 '
         'faces va de 1 à 4": "1/8"}'),
        ("f", "a fraction, as text", "Fraction(3, 24)",
         F + ', mistakes={"« au moins 9 » compte la somme 9 et la somme 10": "1/12"}'),
        ("g", "a fraction, as text", "Fraction(14, 24)",
         F + ', mistakes={"« strictement plus grand » exclut les couples où les deux dés sont égaux": "3/4", '
         '"c\'est le dé à 4 faces qui dépasse ; on demande le dé à 6 faces": "1/4"}'),
        ("h", "a fraction, as text", "Fraction(3, 4)",
         F + ', mistakes={"c\'est la probabilité que le produit soit impair : le produit est pair dès qu\'un des deux '
         'nombres l\'est": "1/4"}'),
    ]),

    Paper("R8.3", "P(A ∪ B) et le complémentaire", [
        ("a", "a number", "0.45 + 0.3 - 0.15",
         'decimals=2, mistakes={"retire P(A ∩ B), comptée deux fois": 0.75}'),
        ("b", "a number", "1 - 0.6",
         'decimals=2, mistakes={"c\'est P(A ∪ B) ; « ni A ni B » en est le contraire": 0.6, '
         '"le contraire de A ∩ B n\'est pas « ni A ni B » (De Morgan)": 0.85}'),
        ("c", "a number", "0.45 - 0.15",
         'decimals=2, mistakes={"retire de P(A) la part commune avec B": 0.45}'),
        ("d", "a number", "0.65 - 0.2",
         'decimals=2, mistakes={"incompatibles : P(A ∪ B) = P(A) + P(B), donc P(B) se déduit par une soustraction": '
         '0.85}'),
        ("e", "True or False", "False",
         'mistakes={"incompatibles : P(A ∪ B) = P(A) + P(B), qui ne peut pas dépasser 1": True}'),
        ("f", "a number", "0.6 + 0.45 - (1 - 0.2)",
         'decimals=2, mistakes={"« l\'appli ou la newsletter » est le contraire de « ni l\'une ni l\'autre » : sa '
         'probabilité n\'est pas 1": 0.05}'),
        ("g", "a fraction, as text", "Fraction(15, 16)",
         F + ', mistakes={"le contraire de « au moins un face » est « que des piles »": "1/16", '
         '"quatre pièces : compte toutes les suites de quatre résultats": "7/8"}'),
        ("h", "a number", "0.55 + 0.35 - 0.7",
         'decimals=2, mistakes={"rien ne dit que A et B sont indépendants : pars de la formule de la réunion": 0.19}'),
    ]),

    Paper("R8.4", "Principe multiplicatif et factorielles", [
        ("a", "an integer", "26 ** 6",
         'mistakes={"les lettres peuvent revenir : 26 possibilités à chaque position": 26 * 25 * 24 * 23 * 22 * 21, '
         '"principe multiplicatif : on multiplie les possibilités des positions, on ne les additionne pas": 156}'),
        ("b", "an integer", "26 * 25 * 24 * 23 * 22 * 21",
         'mistakes={"les lettres toutes différentes : une possibilité de moins à chaque position": 26 ** 6}'),
        ("c", "an integer", "5040",
         'mistakes={"7! a sept facteurs, de 1 à 7": 720}'),
        ("d", "an integer", "8 * 7 * 6",
         'mistakes={"sur un podium, l\'ordre compte : arrangements, pas combinaisons": 56, '
         '"trois places seulement : on ne range pas les huit coureurs": 40320}'),
        ("e", "an integer", "4 * 5 * 3",
         'mistakes={"principe multiplicatif : on multiplie, on n\'additionne pas": 12}'),
        ("f", "an integer", "24",
         'mistakes={"la tâche A est fixée : on ne range que les autres": 120}'),
        ("g", "an integer", "72", ''),
        ("h", "an integer", "26 * 26 * 1000",
         'mistakes={"les lettres et les chiffres peuvent se répéter": 26 * 25 * 10 * 9 * 8}'),
    ]),

    Paper("R8.5", "Combinaisons et triangle de Pascal", [
        ("a", "an integer", "35",
         'mistakes={"une combinaison ne tient pas compte de l\'ordre : divise les arrangements par 3!": 210}'),
        ("b", "an integer", "105",
         'mistakes={"une poignée de main par paire : (a, b) et (b, a) sont la même": 210}'),
        ("c", "an integer", "190",
         'mistakes={"une combinaison ne tient pas compte de l\'ordre : divise les arrangements par 2!": 380}'),
        ("d", "a list", "[1, 7, 21, 35, 35, 21, 7, 1]",
         'mistakes={"c\'est la ligne n = 6 : la ligne n = 7 a 8 nombres, de C(7, 0) à C(7, 7)": '
         '[1, 6, 15, 20, 15, 6, 1], "c\'est la ligne n = 8 : la première ligne du triangle est la ligne n = 0": '
         '[1, 8, 28, 56, 70, 56, 28, 8, 1]}'),
        ("e", "an integer", "2 ** 9",
         'mistakes={"compte bien : la première ligne du triangle est la ligne n = 0": {256, 1024}}'),
        ("f", "an integer", "201376",
         'mistakes={"l\'ordre des cartes d\'une main ne compte pas : combinaisons, pas arrangements": '
         '32 * 31 * 30 * 29 * 28}'),
        ("g", "a fraction, as text", "Fraction(28, 201376)",
         F + ', mistakes={"une main qui contient les 4 as a une 5ᵉ carte quelconque : combien de mains conviennent ?": '
         '"1/201376"}'),
        ("h", "an integer", "70",
         'mistakes={"un chemin a exactement 4 pas vers la droite et 4 vers le haut : toutes les suites de 8 pas ne '
         'conviennent pas": 256}'),
    ]),

    Paper("R8.6", "Arbres pondérés : tirages successifs", [
        ("a", "a number", "0.6 * 0.1",
         'decimals=2, mistakes={"c\'est la probabilité du retard sachant A : multiplie par P(A)": 0.1, '
         '"on multiplie le long d\'un chemin, on n\'additionne pas": 0.7}'),
        ("b", "a number", "0.6 * 0.1 + 0.4 * 0.25",
         'decimals=2, mistakes={"le retard arrive par deux chemins : additionne-les": {0.06, 0.1}, '
         '"additionne les probabilités des chemins, pas les pourcentages de retard": 0.35}'),
        ("c", "a number", "0.4 * 0.75",
         'decimals=2, mistakes={"c\'est la probabilité d\'arriver à l\'heure sachant B : multiplie par P(B)": 0.75}'),
        ("d", "a fraction, as text", "Fraction(4, 10) * Fraction(3, 9)",
         F + ', mistakes={"sans remise, la composition du tiroir change entre les deux tirages": "4/25"}'),
        ("e", "a fraction, as text", "Fraction(4, 10) * Fraction(3, 9) + Fraction(6, 10) * Fraction(5, 9)",
         F + ', mistakes={"c\'est « deux noires » : « même couleur » compte aussi deux grises": "2/15", '
         '"c\'est « deux grises » : « même couleur » compte aussi deux noires": "1/3", '
         '"sans remise, la composition du tiroir change entre les deux tirages": "13/25"}'),
        ("f", "a fraction, as text", "Fraction(2, 5)",
         F + ', mistakes={"c\'est la probabilité sachant que la première est noire : il y a un second chemin": "1/3", '
         '"c\'est « deux noires » : la seconde est noire aussi après une grise": "2/15"}'),
        ("g", "a fraction, as text", "Fraction(4, 25)",
         F + ', mistakes={"avec remise, le second tirage se fait dans le même tiroir que le premier": "2/15"}'),
        ("h", "a fraction, as text", "1 - Fraction(3, 4) ** 3",
         F + ', mistakes={"c\'est la probabilité de trois mauvaises réponses : passe au contraire": "27/64", '
         '"les trois bonnes réponses ne sont pas incompatibles : on n\'additionne pas leurs probabilités": "3/4"}'),
    ]),

    Paper("R8.7", "Indépendance : tester P(A ∩ B) = P(A) P(B) avec des cartes et des pièces", [
        ("a", "a fraction, as text", "Fraction(1, 32)",
         F + ', mistakes={"c\'est P(A ∪ B) ; A ∩ B contient les cartes à la fois as et cœur": "11/32", '
         '"c\'est P(A) + P(B) ; on demande l\'intersection": "3/8"}'),
        ("b", "True or False", "True",
         'mistakes={"compare P(A ∩ B) au produit P(A) P(B)": False}'),
        ("c", "True or False", "False",
         'mistakes={"un as n\'est jamais une figure : A et C sont incompatibles, donc pas indépendants": True}'),
        ("d", "True or False", "False",
         'mistakes={"tous les cœurs sont rouges : savoir que la carte est rouge change la probabilité de « cœur »": '
         'True}'),
        ("e", "a fraction, as text", "Fraction(1, 4)",
         F + ', mistakes={"c\'est P(F) ; E ∩ F demande en plus que la première pièce donne pile": "1/2"}'),
        ("f", "True or False", "True",
         'mistakes={"compare P(E ∩ F) au produit P(E) P(F)": False}'),
        ("g", "a fraction, as text", "Fraction(3, 8)",
         F + ', mistakes={"c\'est P(G) P(H) ; calcule P(G ∩ H) en listant les issues": "1/4", '
         '"c\'est P(G) ; G ∩ H demande en plus que la première pièce donne pile": "1/2"}'),
        ("h", "True or False", "False",
         'mistakes={"compare P(G ∩ H) au produit P(G) P(H)": True}'),
    ]),

    Paper("R8.8", "La loi d'une variable aléatoire", [
        ("a", "a list (3 decimals)", "[1 / 8, 3 / 8, 3 / 8, 1 / 8]",
         'decimals=3, mistakes={"les nombres de piles ne sont pas équiprobables : compte les suites qui donnent chaque '
         'valeur": [0.25, 0.25, 0.25, 0.25]}'),
        ("b", "a number (3 decimals)", "4 / 8",
         'decimals=3, mistakes={"« au moins 2 » : deux piles ou trois piles, les deux cas comptent": {0.375, 0.125}}'),
        ("c", "a list (4 decimals)", "[1 / 16, 3 / 16, 5 / 16, 7 / 16]",
         'decimals=4, mistakes={"Y est le plus grand des deux numéros : compte les couples qui donnent chaque valeur": '
         '[0.25, 0.25, 0.25, 0.25], "c\'est la loi du plus petit des deux numéros, pas du plus grand": '
         '[7 / 16, 5 / 16, 3 / 16, 1 / 16]}'),
        ("d", "a number (2 decimals)", "4 / 16",
         'decimals=2, mistakes={"« au plus 2 » compte aussi Y = 1": 0.19}'),
        ("e", "a number (2 decimals)", "1 - 0.15 - 0.35 - 0.2",
         'decimals=2, mistakes={"c\'est la somme des probabilités connues ; les probabilités d\'une loi ont une somme '
         'de 1": 0.7}'),
        ("f", "a number (2 decimals)", "1 - 0.15",
         'decimals=2, mistakes={"Z > 1 : toutes les valeurs sauf 1": 0.15}'),
        ("g", "a list (3 decimals)", "[16 / 32, 12 / 32, 4 / 32]",
         'decimals=3, mistakes={"les figures sont les valets, les dames et les rois : trois par couleur": '
         '[0.625, 0.25, 0.125]}'),
        ("h", "a number (3 decimals)", "28 / 32",
         'decimals=3, mistakes={"« au plus 2 » compte W = −1 et W = 2": 0.375}'),
    ]),

    Paper("R8.9", "Espérance, variance (avec V = E[X²] − E[X]²) et écart-type", [
        ("a", "a number (2 decimals)", "0 * 0.2 + 1 * 0.4 + 2 * 0.3 + 3 * 0.1",
         'decimals=2, mistakes={"pondère chaque valeur par sa probabilité, au lieu de faire la moyenne des valeurs": '
         '1.5}'),
        ("b", "a number (2 decimals)", "0 * 0.2 + 1 * 0.4 + 4 * 0.3 + 9 * 0.1",
         'decimals=2, mistakes={"E[X²] est la moyenne des carrés, pas le carré de la moyenne": 1.69}'),
        ("c", "a number (2 decimals)", "2.5 - 1.3 ** 2",
         'decimals=2, mistakes={"retire le carré de l\'espérance, pas l\'espérance": 1.2}'),
        ("d", "a number (2 decimals)", "0.9",
         'decimals=2, mistakes={"l\'écart-type est la racine carrée de la variance": 0.81}'),
        ("e", "a number (2 decimals)", "10 * 1.3 - 4",
         'decimals=2, mistakes={"E[aX + b] = a E[X] + b : la pénalité se retire de l\'espérance": 13}'),
        ("f", "a number (2 decimals)", "100 * 0.81",
         'decimals=2, mistakes={"V(aX + b) = a² V(X) : le coefficient est élevé au carré": 8.1, '
         '"une constante ajoutée ne change pas la variance": 77}'),
        ("g", "a fraction, as text", "Fraction(25, 8)",
         F + ', mistakes={"pondère chaque valeur par sa probabilité, avec la loi de Y de R8.8": "5/2"}'),
        ("h", "a fraction, as text", "Fraction(85, 8) - Fraction(25, 8) ** 2",
         F + ', mistakes={"c\'est E[Y²] : retire encore le carré de l\'espérance": "85/8"}'),
    ]),

    Paper("R8.10", "Un jeu est-il équitable ?", [
        ("a", "a number", "8 / 4 + 1 / 2",
         'decimals=2, mistakes={"un seul pile arrive de deux façons (PF ou FP)": 2.25, '
         '"« deux piles », « un pile » et « aucun pile » ne sont pas équiprobables": 3}'),
        ("b", "a number", "2.5 - 3",
         'decimals=2, mistakes={"le gain net est le prix moins la mise": 5.5}'),
        ("c", "a number", "200 * 0.5",
         'decimals=2, mistakes={"ce que gagne l\'organisateur, c\'est ce que perd le joueur": -100}'),
        ("d", "a number", "64 / 4 + 1 / 2 - 2.5 ** 2",
         'decimals=2, mistakes={"V = E[X²] − E[X]² : retire le carré de l\'espérance": 16.5}'),
        ("e", "a number", "(64 / 4 + 1 / 2 - 2.5 ** 2) ** 0.5",
         'decimals=2, mistakes={"l\'écart-type est la racine carrée de la variance": 10.25}'),
        ("f", "a number", "6 / 6",
         'decimals=2, mistakes={"pondère le prix par la probabilité de le gagner": 6}'),
        ("g", "a number", "36 / 6 - 1",
         'decimals=2, mistakes={"V = E[X²] − E[X]² : retire le carré de l\'espérance": 6}'),
        ("h", "a number", "1.5 * 6",
         'decimals=2, mistakes={"équitable : l\'espérance du prix est égale à la mise": 1.5}'),
    ]),

    Paper("R8.13", "Comparer toutes les paires : un tournoi, C(n, 2) et une croissance en n²", [
        ("a", "an integer", "16 * 15 // 2",
         'mistakes={"un match par paire d\'équipes : (A, B) et (B, A) sont le même match": 240}'),
        ("b", "an integer", "16 * 15",
         'mistakes={"aller et retour : deux matchs par paire d\'équipes": 120}'),
        ("c", "an integer", "1000 * 999 // 2",
         'mistakes={"une comparaison par paire, pas par couple ordonné": 999000, '
         '"une comparaison par paire de deux exemples différents": 1000000}'),
        ("d", "an integer", "round((10000 * 9999 / 2) / (1000 * 999 / 2))",
         'mistakes={"le nombre de paires ne grandit pas comme n : regarde la formule de C(n, 2)": 10}'),
        ("e", "a number (1 decimal)", "(10 ** 6 * (10 ** 6 - 1) / 2) / 10 ** 6 / 3600",
         'decimals=1, mistakes={"c\'est en minutes : une heure fait 60 minutes": 8333.3, '
         '"une comparaison par paire : C(n, 2), pas n²": 277.8}'),
        ("f", "an integer", "100 * 99 * 98 // 6",
         'mistakes={"un groupe ne dépend pas de l\'ordre : divise les arrangements par 3!": 970200}'),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math
from fractions import Fraction'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ R8.1 à R8.10, 🔗 R8.13)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.5`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"5/7\"` ;\n"
               "- une liste de nombres entre crochets, `[0.25, 0.5, 0.25]` ; vrai ou faux par `True` ou `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (R8.16 to R8.19)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
from fractions import Fraction

import matplotlib.pyplot as plt
import numpy as np

from wbm.nbtools import checked, drawn, run_pytest_group


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

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="R8")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme dans les chapitres précédents). Ouvre ta copie "
         "`mon_travail/mymath/proba_basics.py`, lis la docstring de la fonction en entier, remplace la ligne "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Comme dans tous les chapitres R0 à R9, Python pur : "
         "`fractions.Fraction` est permis, mais ni `math.factorial`, ni `math.comb`, ni le module `statistics` "
         "(la docstring du module le dit, et un test le vérifie) ; seule `simulate_frequency` se sert du générateur "
         "de NumPy. Les tests comparent tes résultats à `math.factorial`, `math.comb`, à des comptages exacts avec "
         "`Fraction` et à NumPy.")

WRONG_ERROR = "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)"
OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "TypeError", "ZeroDivisionError"]


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of proba_basics.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_r8_proba_basics.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_r8_proba_basics.py", "{keyword}", impl="ref")')]


R8_16 = Ex(
    "R8.16", "🔨", 1, 15, "Factorielle et combinaisons · `factorial`, `binomial`",
    "programmer la factorielle et le coefficient binomial, exactement, avec leurs cas limites.",
    "fiche §3", tracks="C, E", mymath="proba_basics.py",
    body=HOWTO + """

Écris `factorial(n)` puis `binomial(n, k)` dans `mon_travail/mymath/proba_basics.py` (fiche §3). `factorial` lève une `ValueError` pour un `n` négatif ; `binomial(n, k)` vaut 0 quand $k < 0$ ou $k > n$, et doit rester un **entier exact**, même pour de grands nombres : pas de division `/`, qui donne un flottant arrondi, mais la division entière `//`.

La vérification calcule :
- a) la liste `[factorial(n) for n in (0, 1, 8, 13)]` ;
- b) le nom de l'erreur levée par `factorial(-2)` (avec `raised`, de la cellule des outils) ;
- c) la ligne $n = 12$ du triangle de Pascal, `[binomial(12, k) for k in range(13)]` ;
- d) la liste `[binomial(9, 11), binomial(9, -1)]` ;
- e) le type de `binomial(60, 30)`, en texte (`"int"` pour un entier).

Puis, dans ta copie : comment calcules-tu `factorial(20) // factorial(18)` de tête ? Pourquoi `binomial(n, k)` gagne-t-il à multiplier et diviser au fur et à mesure, plutôt qu'à calculer trois factorielles, quand $n$ vaut 10 000 et $k$ vaut 3 ?""",
    todo=LOAD_LEARNER,
    check='''with checked("R8.16a"):
    wbm.check("R8.16a", [mymath.proba_basics.factorial(n) for n in (0, 1, 8, 13)], computed=True)
with checked("R8.16b"):
    wbm.check("R8.16b", raised(mymath.proba_basics.factorial, -2), computed=True)
with checked("R8.16c"):
    wbm.check("R8.16c", [mymath.proba_basics.binomial(12, k) for k in range(13)], computed=True)
with checked("R8.16d"):
    wbm.check("R8.16d", [mymath.proba_basics.binomial(9, 11), mymath.proba_basics.binomial(9, -1)], computed=True)
with checked("R8.16e"):
    wbm.check("R8.16e", type(mymath.proba_basics.binomial(60, 30)).__name__, computed=True)''',
    solution=LOAD_REF + '''
factorial, binomial = mymath.proba_basics.factorial, mymath.proba_basics.binomial
print("a)", [factorial(n) for n in (0, 1, 8, 13)], " b)", raised(factorial, -2))
print("c)", [binomial(12, k) for k in range(13)])
print("d)", [binomial(9, 11), binomial(9, -1)], " e)", type(binomial(60, 30)).__name__, binomial(60, 30))''',
    record=f'''wbm.record("R8.16a", [1, 1, 40320, 6227020800],
           mistakes={{"0! vaut 1 : c'est le produit vide": [0, 1, 40320, 6227020800],
                     "range(1, n) s'arrête avant n : le dernier facteur manque": [1, 1, 5040, 479001600]}})
wbm.record("R8.16b", "ValueError",
           mistakes={{"n négatif : lève une ValueError avant la boucle": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("R8.16c", [math.comb(12, k) for k in range(13)])
wbm.record("R8.16d", [0, 0])
wbm.record("R8.16e", "int",
           mistakes={{"une division / donne un flottant : utilise la division entière //": "float"}})''',
    after=tests_cells("test_factorial_ or test_binomial_ or test_proba_basics_does"),
    note="La ligne 12 du triangle est 1, 12, 66, 220, 495, 792, 924, 792, …, 1, symétrique. Pour "
         "`factorial(20) // factorial(18)`, tous les facteurs de 1 à 18 se simplifient : il reste $20 \\times 19 = 380$. "
         "Pour $\\binom{10\\,000}{3}$, trois multiplications et trois divisions suffisent, alors que $10\\,000!$ a plus "
         "de 35 000 chiffres.",
)
R8_16.record = "import math\n" + R8_16.record

R8_17_GIVEN = '''three_d4 = [(a, b, c) for a in range(1, 5) for b in range(1, 5) for c in range(1, 5)]   # 64 triplets'''

R8_17 = Ex(
    "R8.17", "🔨", 2, 25, "Une probabilité exacte par énumération · `enumerate_probability`",
    "calculer une probabilité exacte en énumérant des issues équiprobables, avec un événement donné par une fonction.",
    "fiche §2 ; R1 (fractions) ; workbookIA 0A §100.5.3 (fonctions en argument)", tracks="C", mymath="proba_basics.py",
    body="""Écris `enumerate_probability(outcomes, event)` : la probabilité exacte de l'événement quand toutes les issues de `outcomes` sont équiprobables, sous la forme d'une `Fraction` (fiche §2). `event` est une **fonction** qui reçoit une issue et renvoie `True` si elle est favorable (workbookIA 0A §100.5.3). Attention : `outcomes` peut être une liste, mais aussi un **générateur**, qui n'a pas de `len()` et ne se lit qu'une fois ; compte donc les issues en les parcourant. Sans aucune issue, lève une `ValueError`.

La cellule fournie définit `three_d4`, les 64 triplets de trois lancers d'un dé à 4 faces. La vérification calcule :
- a) la probabilité que la somme des trois dés vaille 6 ;
- b) la probabilité qu'au moins deux des trois dés montrent le même numéro ;
- c) avec le générateur `(n for n in range(1, 1001))`, la probabilité qu'un entier de 1 à 1 000 tiré au hasard s'écrive avec au moins un chiffre 7 ;
- d) le nom de l'erreur levée pour une liste d'issues vide ;
- e) le type du résultat de a), en texte.

Puis, dans ta copie : retrouve a) en dénombrant à la main les triplets de somme 6, et b) par le contraire (« trois numéros différents »).""",
    given=R8_17_GIVEN,
    todo=LOAD_LEARNER,
    check='''with checked("R8.17a"):
    wbm.check("R8.17a", mymath.proba_basics.enumerate_probability(three_d4, lambda t: sum(t) == 6), computed=True)
with checked("R8.17b"):
    wbm.check("R8.17b", mymath.proba_basics.enumerate_probability(three_d4, lambda t: len(set(t)) < 3),
              computed=True)
with checked("R8.17c"):
    wbm.check("R8.17c", mymath.proba_basics.enumerate_probability((n for n in range(1, 1001)),
                                                                 lambda n: "7" in str(n)), computed=True)
with checked("R8.17d"):
    wbm.check("R8.17d", raised(mymath.proba_basics.enumerate_probability, [], lambda o: True), computed=True)
with checked("R8.17e"):
    result = mymath.proba_basics.enumerate_probability(three_d4, lambda t: sum(t) == 6)
    wbm.check("R8.17e", type(result).__name__, computed=True)''',
    solution=LOAD_REF + '''
enumerate_probability = mymath.proba_basics.enumerate_probability
print("a)", enumerate_probability(three_d4, lambda t: sum(t) == 6))
print("b)", enumerate_probability(three_d4, lambda t: len(set(t)) < 3))
print("c)", enumerate_probability((n for n in range(1, 1001)), lambda n: "7" in str(n)))
print("d)", raised(enumerate_probability, [], lambda o: True),
      " e)", type(enumerate_probability(three_d4, lambda t: sum(t) == 6)).__name__)''',
    record=f'''wbm.record("R8.17a", Fraction(10, 64), kind="fraction")
wbm.record("R8.17b", Fraction(40, 64), kind="fraction",
           mistakes={{"« au moins deux égaux » est le contraire de « trois différents »": "3/8"}})
wbm.record("R8.17c", Fraction(271, 1000), kind="fraction")
wbm.record("R8.17d", "ValueError",
           mistakes={{"sans issue, lève une ValueError avant de diviser": {{"ZeroDivisionError", "aucune"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("R8.17e", "Fraction",
           mistakes={{"renvoie une Fraction exacte, pas un flottant : Fraction(favorables, total)": "float"}})''',
    after=tests_cells("test_enumerate_probability_ or test_proba_basics_does"),
    note="10 triplets de somme 6 : les 3 rangements de (1, 1, 4), les 6 de (1, 2, 3) et le triplet (2, 2, 2), soit "
         "$\\frac{10}{64} = \\frac{5}{32}$. Trois numéros différents : "
         "$4 \\times 3 \\times 2 = 24$ triplets, d'où $1 - \\frac{24}{64} = \\frac{5}{8}$. De 1 à 1 000, 271 entiers "
         "s'écrivent avec un 7 (le contraire : $9 \\times 9 \\times 9 = 729$ entiers de 000 à 999 sans 7, dont 000, "
         "remplacé par 1 000).",
)
R8_17.record = "from fractions import Fraction\n" + R8_17.record

R8_18_GIVEN = '''sixes_values = [0, 1, 2]                                          # number of 6 in two rolls of a die
sixes_probs = [Fraction(25, 36), Fraction(10, 36), Fraction(1, 36)]
float_values = [-1.5, 0, 2.5]
float_probs = [0.3, 0.45, 0.25]'''

R8_18 = Ex(
    "R8.18", "🔨", 1, 15, "Espérance et variance d'une loi · `expectation`, `variance`",
    "programmer l'espérance et la variance d'une loi finie, exactes avec des fractions, et vérifier la loi d'abord.",
    "fiche §7", tracks="C, E", mymath="proba_basics.py",
    body="""Écris `expectation(values, probabilities)` puis `variance(values, probabilities)` (fiche §7). Les deux commencent par **vérifier la loi** : autant de valeurs que de probabilités, aucune probabilité négative, une somme égale à 1 (à $10^{-9}$ près, pour les flottants) ; sinon, une `ValueError`. Le résultat est une `Fraction` quand toutes les valeurs et toutes les probabilités sont des entiers ou des fractions, un flottant sinon. Pour la variance, pars de la définition $\\mathbb{E}\\big[(X - \\mathbb{E}[X])^2\\big]$, en réutilisant `expectation`.

La cellule fournie définit la loi du nombre de 6 en deux lancers d'un dé (`sixes_values`, `sixes_probs`, en fractions) et une loi en flottants (`float_values`, `float_probs`). La vérification calcule :
- a) et b) l'espérance et la variance de la loi du nombre de 6 ;
- c) et d) l'espérance et la variance de la loi en flottants ;
- e) le nom de l'erreur levée par `expectation([1, 2, 3], [0.5, 0.5])`, puis f) par `variance([1, 2], [0.7, 0.2])` ;
- g) le type du résultat de b), en texte.

Puis, dans ta copie : retrouve a) et b) à la main, avec la formule $\\mathbb{V}(X) = \\mathbb{E}[X^2] - \\mathbb{E}[X]^2$.""",
    given=R8_18_GIVEN,
    todo=LOAD_LEARNER,
    check='''with checked("R8.18a"):
    wbm.check("R8.18a", mymath.proba_basics.expectation(sixes_values, sixes_probs), computed=True)
with checked("R8.18b"):
    wbm.check("R8.18b", mymath.proba_basics.variance(sixes_values, sixes_probs), computed=True)
with checked("R8.18c"):
    wbm.check("R8.18c", mymath.proba_basics.expectation(float_values, float_probs), computed=True)
with checked("R8.18d"):
    wbm.check("R8.18d", mymath.proba_basics.variance(float_values, float_probs), computed=True)
with checked("R8.18e"):
    wbm.check("R8.18e", raised(mymath.proba_basics.expectation, [1, 2, 3], [0.5, 0.5]), computed=True)
with checked("R8.18f"):
    wbm.check("R8.18f", raised(mymath.proba_basics.variance, [1, 2], [0.7, 0.2]), computed=True)
with checked("R8.18g"):
    wbm.check("R8.18g", type(mymath.proba_basics.variance(sixes_values, sixes_probs)).__name__, computed=True)''',
    solution=LOAD_REF + '''
expectation, variance = mymath.proba_basics.expectation, mymath.proba_basics.variance
print("a)", expectation(sixes_values, sixes_probs), " b)", variance(sixes_values, sixes_probs))
print("c)", expectation(float_values, float_probs), " d)", variance(float_values, float_probs))
print("e)", raised(expectation, [1, 2, 3], [0.5, 0.5]), " f)", raised(variance, [1, 2], [0.7, 0.2]),
      " g)", type(variance(sixes_values, sixes_probs)).__name__)''',
    record=f'''wbm.record("R8.18a", Fraction(1, 3), kind="fraction")
wbm.record("R8.18b", Fraction(5, 18), kind="fraction",
           mistakes={{"c'est E[X²] : retire encore le carré de l'espérance": "7/18"}})
wbm.record("R8.18c", 0.175, decimals=4)
wbm.record("R8.18d", 2.2375 - 0.175 ** 2, decimals=4,
           mistakes={{"c'est E[X²] : retire encore le carré de l'espérance": 2.2375}})
wbm.record("R8.18e", "ValueError",
           mistakes={{"des longueurs différentes : lève une ValueError avant de calculer (zip s'arrête sans rien dire)":
                         "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("R8.18f", "ValueError",
           mistakes={{"des probabilités de somme 0,9 ne forment pas une loi : lève une ValueError": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("R8.18g", "Fraction",
           mistakes={{"avec des entiers et des fractions, le résultat reste une Fraction exacte : pas de float(...)":
                         "float"}})''',
    after=tests_cells("test_expectation_ or test_variance_ or test_proba_basics_does"),
    note="$\\mathbb{E} = \\frac{0 \\times 25 + 1 \\times 10 + 2 \\times 1}{36} = \\frac{12}{36} = \\frac{1}{3}$ et "
         "$\\mathbb{E}[X^2] = \\frac{10 + 4}{36} = \\frac{7}{18}$, d'où $\\mathbb{V} = \\frac{7}{18} - \\frac{1}{9} = "
         "\\frac{5}{18}$. `zip` s'arrête sans rien dire à la plus courte des deux listes : sans vérification, des "
         "longueurs différentes donneraient un résultat faux, sans erreur.",
)
R8_18.record = "from fractions import Fraction\n" + R8_18.record

R8_19 = Ex(
    "R8.19", "🔨", 2, 20, "Estimer une probabilité par simulation · `simulate_frequency`",
    "programmer une simulation reproductible : un générateur créé une fois, une expérience répétée, une fréquence.",
    "fiche §8 ; workbookIA 0A §100.8.7 (default_rng)", tracks="C, E", mymath="proba_basics.py",
    body="""Écris `simulate_frequency(experiment, n_trials, seed=0)` (fiche §8) : crée **un** générateur `np.random.default_rng(seed)`, appelle `experiment(rng)` `n_trials` fois avec lui, et renvoie la fréquence des succès (le nombre de `True` divisé par `n_trials`), en flottant. Un `n_trials` nul ou négatif lève une `ValueError`. `experiment` est une fonction qui fait **un** essai avec le générateur qu'elle reçoit, par exemple `lambda rng: rng.integers(1, 5) == 4` (« le dé à 4 faces donne 4 »).

La vérification calcule :
- a) la fréquence de « le dé à 4 faces donne 4 » sur 1 000 essais, avec la graine 5 ;
- b) si deux appels avec la même graine donnent la même fréquence (vrai ou faux) ;
- c) si les graines 5 et 6 donnent des fréquences différentes (vrai ou faux) ;
- d) le nom de l'erreur levée pour 0 essai ;
- e) si la fréquence de « la somme de deux dés à 4 faces vaut au moins 6 », sur 20 000 essais avec la graine 0, est à moins de 0,02 de la probabilité $\\frac{3}{8}$ du §6 (vrai ou faux).

Puis, dans ta copie : pourquoi la fréquence de a) n'est-elle pas exactement $\\frac{1}{4}$ ? Que se passerait-il si tu créais le générateur **dans** la boucle, avec la même graine à chaque essai ?""",
    todo=LOAD_LEARNER,
    check='''one_four = lambda rng: rng.integers(1, 5) == 4                                  # noqa: E731
with checked("R8.19a"):
    wbm.check("R8.19a", mymath.proba_basics.simulate_frequency(one_four, 1000, seed=5), computed=True)
with checked("R8.19b"):
    first = mymath.proba_basics.simulate_frequency(one_four, 1000, seed=5)
    second = mymath.proba_basics.simulate_frequency(one_four, 1000, seed=5)
    wbm.check("R8.19b", bool(first == second), computed=True)
with checked("R8.19c"):
    other = mymath.proba_basics.simulate_frequency(one_four, 1000, seed=6)
    wbm.check("R8.19c", bool(first != other), computed=True)
with checked("R8.19d"):
    wbm.check("R8.19d", raised(mymath.proba_basics.simulate_frequency, one_four, 0), computed=True)
with checked("R8.19e"):
    sum_at_least_6 = lambda rng: rng.integers(1, 5) + rng.integers(1, 5) >= 6       # noqa: E731
    frequency = mymath.proba_basics.simulate_frequency(sum_at_least_6, 20_000, seed=0)
    wbm.check("R8.19e", bool(abs(frequency - 3 / 8) < 0.02), computed=True)''',
    solution=LOAD_REF + '''
simulate_frequency = mymath.proba_basics.simulate_frequency
one_four = lambda rng: rng.integers(1, 5) == 4                                  # noqa: E731
sum_at_least_6 = lambda rng: rng.integers(1, 5) + rng.integers(1, 5) >= 6       # noqa: E731
print("a)", simulate_frequency(one_four, 1000, seed=5), " b)", simulate_frequency(one_four, 1000, seed=5),
      " c)", simulate_frequency(one_four, 1000, seed=6))
print("d)", raised(simulate_frequency, one_four, 0), " e)", simulate_frequency(sum_at_least_6, 20_000, seed=0))''',
    record=f'''rng = np.random.default_rng(5)                     # the replayed generator: the exact frequency of a)
wbm.record("R8.19a", sum(bool(rng.integers(1, 5) == 4) for _ in range(1000)) / 1000, decimals=3,
           mistakes={{"crée le générateur une seule fois, avant la boucle : recréé à chaque essai avec la même graine, il "
                     "redonne le même tirage": {{0.0, 1.0}}}})
wbm.record("R8.19b", True,
           mistakes={{"la même graine doit redonner la même fréquence : crée le générateur avec default_rng(seed)": False}})
wbm.record("R8.19c", True,
           mistakes={{"deux graines différentes donnent deux suites différentes : passe seed à default_rng": False}})
wbm.record("R8.19d", "ValueError",
           mistakes={{"0 essai : lève une ValueError avant de diviser": {{"ZeroDivisionError", "aucune"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("R8.19e", True,
           mistakes={{"avec 20 000 essais, la fréquence doit être proche de 3/8 : relis la boucle (un seul générateur, "
                     "le nombre de succès divisé par n_trials) ; les tests disent quel cas pose problème": False}})''',
    after=tests_cells("test_simulate_frequency_ or test_proba_basics_does"),
    note="La fréquence de a) vaut 0,238 avec la graine 5 : une autre graine donne une autre fréquence, proche de 0,25 "
         "elle aussi, à quelques centièmes près sur 1 000 essais. Un générateur recréé à chaque essai avec la même "
         "graine redonne le même premier tirage : la « fréquence » vaut alors 0 ou 1.",
)
R8_19.record = "import numpy as np\n" + R8_19.record

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a plot (R8.20 to R8.22)
# ---------------------------------------------------------------------------
R8_20_EXPERIMENT = '''rng = np.random.default_rng(2026)
for n_students in (10, 23, 30, 60):
    classes = rng.integers(0, 365, size=(20_000, n_students))     # 20 000 classes, one birthday per student
    shared = np.any(np.diff(np.sort(classes, axis=1), axis=1) == 0, axis=1)
    print(f"{n_students:>2} élèves : fréquence d'un anniversaire partagé = {shared.mean():.3f}")'''

R8_20 = Ex(
    "R8.20", "🔮", 2, 15, "Prédire : dans une classe de 30, deux élèves ont-ils le même anniversaire ?",
    "prévoir une probabilité contre-intuitive, la vérifier par simulation, puis la calculer exactement.",
    "fiche §2, §3 et §8", tracks="C, E", hypothesis=True,
    body="""On suppose que les 365 jours de l'année (sans 29 février) sont équiprobables pour une date d'anniversaire, et que les élèves d'une classe sont nés indépendamment les uns des autres. **Avant d'exécuter quoi que ce soit**, prédis :
- a) dans une classe de 30 élèves, la probabilité qu'au moins deux élèves aient le même anniversaire : 1 moins de 10 % ; 2 entre 10 % et 50 % ; 3 plus de 50 % ;
- b) le plus petit nombre d'élèves pour lequel cette probabilité dépasse 50 % est proche de : 1 23 ; 2 60 ; 3 183 ;
- c) avec 60 élèves, la probabilité est : 1 environ 70 % ; 2 environ 85 % ; 3 plus de 99 %.

Écris tes trois prédictions, vérifie-les, puis lance l'expérience, qui simule 20 000 classes de chaque taille. Ensuite, calcule la probabilité **exacte** :
- d) écris `p_shared(n)`, la probabilité qu'au moins deux élèves sur $n$ aient le même anniversaire. Passe par le contraire, « tous les anniversaires sont différents » : le premier élève a 365 jours possibles sur 365, le deuxième 364 sur 365, le troisième 363 sur 365… (une boucle, ou un produit Π). La vérification calcule `p_shared(30)` (3 décimales) ;
- e) le plus petit nombre d'élèves $n$ pour lequel `p_shared(n)` dépasse 0,5 (un entier, cherché avec une boucle).""",
    todo='''prediction_R8_20a = ...  # a) 1, 2 or 3, written BEFORE running the experiment below
prediction_R8_20b = ...  # b) 1, 2 or 3
prediction_R8_20c = ...  # c) 1, 2 or 3''',
    check='''for letter, prediction in zip("abc", [prediction_R8_20a, prediction_R8_20b, prediction_R8_20c]):
    wbm.check(f"R8.20{letter}", prediction)''',
    record='''wbm.record("R8.20a", 3, prediction=True, choices=[1, 2, 3])
wbm.record("R8.20b", 1, prediction=True, choices=[1, 2, 3])
wbm.record("R8.20c", 3, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes trois prédictions écrites."),
        ("todo", guarded(R8_20_EXPERIMENT, ["prediction_R8_20a", "prediction_R8_20b", "prediction_R8_20c"],
                         "⏳ Écris d'abord tes trois prédictions, puis exécute à nouveau.")),
        ("solution", R8_20_EXPERIMENT),
        ("md", "**d) et e)** La probabilité exacte, par le contraire."),
        ("todo", '''def p_shared(n):
    """The probability that at least two of n students share a birthday (365 equally likely days)."""
    raise NotImplementedError("passe par le contraire : le produit des (365 - k) / 365")


answer_R8_20e = ...  # e) an integer, found with a loop'''),
        ("solution", '''def p_shared(n):
    """The probability that at least two of n students share a birthday (365 equally likely days)."""
    all_different = 1.0
    for k in range(n):
        all_different *= (365 - k) / 365
    return 1 - all_different


answer_R8_20e = next(n for n in range(1, 366) if p_shared(n) > 0.5)
print(round(p_shared(30), 4), answer_R8_20e)'''),
        ("check", '''with checked("R8.20d"):
    wbm.check("R8.20d", p_shared(30), computed=True)
wbm.check("R8.20e", answer_R8_20e)'''),
        ("record", '''all_different = 1.0
for k in range(30):
    all_different *= (365 - k) / 365
wbm.record("R8.20d", 1 - all_different, decimals=3,
           mistakes={"c'est la probabilité que tous les anniversaires soient différents : passe au contraire":
                         all_different})
wbm.record("R8.20e", 23, mistakes={"le premier n pour lequel la probabilité dépasse 0,5, pas le dernier qui reste "
                                   "en dessous": 22})'''),
        ("md", "**Après l'expérience**, dans ta copie : combien de **paires** d'élèves une classe de 30 contient-elle "
               "(§3) ? Pourquoi ce nombre explique-t-il que la probabilité soit si grande, alors que chaque paire n'a "
               "qu'une chance sur 365 de partager un anniversaire ?"),
    ],
    note="Les fréquences simulées sont proches de 0,12 (10 élèves), 0,51 (23), 0,71 (30) et 0,99 (60). La probabilité "
         "exacte pour 30 élèves vaut $1 - \\frac{365 \\times 364 \\times \\cdots \\times 336}{365^{30}} \\approx 0{,}706$, "
         "et 23 élèves suffisent à dépasser une chance sur deux. L'intuition se trompe parce qu'elle pense à **son** "
         "anniversaire, alors que la question porte sur toutes les paires : une classe de 30 en contient "
         "$\\binom{30}{2} = 435$.",
)

R8_21 = Ex(
    "R8.21", "🔬", 2, 20, "La loi des grands nombres : fréquence et nombre de lancers",
    "mesurer comment la probabilité qu'une fréquence s'écarte de la probabilité diminue quand le nombre d'essais "
    "grandit.", "fiche §8 ; workbookIA 0A §100.8.7 (default_rng) et §100.8.3 (calcul vectorisé)", tracks="C, E",
    body="""On lance un dé à 6 faces, et l'on s'intéresse à l'événement « le dé donne 5 ou 6 », de probabilité $\\frac{1}{3}$. Pour chaque nombre de lancers $n$ de `sizes = [10, 100, 1000, 10000]`, **dans cet ordre**, et avec **un seul** générateur `rng = np.random.default_rng(81)`, créé avant la boucle :
- tire 500 séries de $n$ lancers : `freqs = (rng.integers(1, 7, size=(500, n)) >= 5).mean(axis=1)`, les 500 fréquences de l'événement ;
- calcule la proportion des 500 séries dont la fréquence s'écarte de $\\frac{1}{3}$ de plus de 0,05 : `np.mean(np.abs(freqs - 1 / 3) > 0.05)`.

Questions :
- a) `far` : la liste des quatre proportions, dans l'ordre des $n$ (3 décimales) ;
- b) `mean_10000` : pour $n = 10\\,000$, la moyenne des 500 fréquences (4 décimales) ;
- c) vers quel nombre la proportion de a) semble-t-elle tendre quand $n$ grandit ?

Trace aussi, côte à côte, l'histogramme des 500 fréquences pour $n = 100$ et pour $n = 10\\,000$, sur le même axe horizontal de 0 à 1 (garde ces fréquences dans un dictionnaire pendant la boucle).

Dans ta copie : que dit la loi des grands nombres, et que ne dit-elle pas ? Avec $n = 10\\,000$, que deviendrait la proportion de a) pour un écart de 0,01 au lieu de 0,05 ?""",
    given='''sizes = [10, 100, 1000, 10000]''',
    todo='''far = ...           # a) a list of 4 proportions
mean_10000 = ...    # b) a number
answer_R8_21c = ... # c) a number''',
    check='''wbm.check("R8.21a", far, computed=True)
wbm.check("R8.21b", mean_10000, computed=True)
wbm.check("R8.21c", answer_R8_21c)''',
    solution='''rng = np.random.default_rng(81)
far, kept = [], {}
for n in sizes:
    freqs = (rng.integers(1, 7, size=(500, n)) >= 5).mean(axis=1)
    far.append(float(np.mean(np.abs(freqs - 1 / 3) > 0.05)))
    kept[n] = freqs
mean_10000 = float(kept[10000].mean())
answer_R8_21c = 0
print("a)", far, " b)", round(mean_10000, 4))

fig, axes = plt.subplots(1, 2, figsize=(10, 3.2), sharex=True)
for ax, n in zip(axes, (100, 10000)):
    ax.hist(kept[n], bins=40, range=(0, 1))
    ax.axvline(1 / 3, color="0.3", linestyle="--")
    ax.set_title(f"500 fréquences, n = {n}")
    ax.set_xlabel("fréquence de « 5 ou 6 »")
plt.show()''',
    record='''rng = np.random.default_rng(81)
proportions, means = [], []
for n in [10, 100, 1000, 10000]:
    freqs = (rng.integers(1, 7, size=(500, n)) >= 5).mean(axis=1)
    proportions.append(float(np.mean(np.abs(freqs - 1 / 3) > 0.05)))
    means.append(float(freqs.mean()))
renewed = []                                    # the classic slip: a generator created again for each n
for n in [10, 100, 1000, 10000]:
    freqs = (np.random.default_rng(81).integers(1, 7, size=(500, n)) >= 5).mean(axis=1)
    renewed.append(float(np.mean(np.abs(freqs - 1 / 3) > 0.05)))
wbm.record("R8.21a", proportions, decimals=3,
           mistakes={"un seul générateur, créé avant la boucle avec la graine 81 : recréé à chaque n, il repart du "
                     "même point": renewed})
wbm.record("R8.21b", means[-1], decimals=4)
wbm.record("R8.21c", 0.0, decimals=2, mistakes={"c'est la proportion des séries qui s'écartent de plus de 0,05 : "
                                                "regarde comment elle évolue quand n grandit": {0.05, 0.33}})''',
    note="Les proportions valent 0,772, 0,28, 0,002 et 0 : avec 10 lancers, une série sur quatre seulement reste à "
         "moins de 0,05 de $\\frac{1}{3}$ ; avec 10 000, toutes. La loi des grands nombres dit exactement cela : la "
         "probabilité que la fréquence s'écarte de la probabilité de plus d'un écart donné tend vers 0. Elle ne dit pas "
         "que la fréquence **égale** la probabilité, ni à partir de quel $n$ on est tranquille : pour un écart de "
         "0,01, environ 3 % des séries de 10 000 lancers resteraient au-delà (l'écart typique y vaut environ 0,005).",
)
R8_21.record = "import numpy as np\n" + R8_21.record

R8_22_CHECK = '''with checked("R8.22 vérifications"):
    fig, ax = plt.subplots(figsize=(6, 3.5))
    try:
        created = drawn(plot_law, ax, piles_values, piles_probs)
    finally:
        plt.close(fig)                                     # only the checks below are shown here
    problems = []
    if created:
        problems.append("ta fonction ouvre sa propre figure : dessine dans l'axe reçu (ax.bar, …)")
    else:
        heights = sorted((round(float(p.get_x() + p.get_width() / 2), 6), round(float(p.get_height()), 6))
                         for p in ax.patches)
        expected = sorted((float(v), round(float(p), 6)) for v, p in zip(piles_values, piles_probs))
        if heights != expected:
            problems.append("un bâton par valeur, centré sur la valeur, de hauteur sa probabilité (ax.bar)")
        mean = sum(v * p for v, p in zip(piles_values, piles_probs))
        verticals = [l for l in ax.lines if len(set(np.round(np.asarray(l.get_xdata(), dtype=float), 6))) == 1]
        if not any(np.isclose(float(np.asarray(l.get_xdata(), dtype=float)[0]), mean) for l in verticals):
            problems.append("une droite verticale à l'espérance (ax.axvline), calculée dans la fonction")
        if not ax.get_title() or not ax.get_xlabel() or not ax.get_ylabel():
            problems.append("un titre et le nom des deux axes (ax.set_title, ax.set_xlabel, ax.set_ylabel)")
    if problems:
        print("❌ Ex R8.22 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex R8.22 : les bâtons, l'espérance, le titre et les axes.")'''

R8_22 = Ex(
    "R8.22", "🎨", 1, 10, "Le diagramme en bâtons d'une loi",
    "tracer la loi d'une variable aléatoire discrète et y placer son espérance.",
    "fiche §6 et §7 ; R0 (matplotlib)", tracks="C",
    body="""Complète `plot_law(ax, values, probabilities)`, qui dessine dans l'axe `ax` qu'elle reçoit :
- un bâton par valeur, centré sur la valeur, de hauteur sa probabilité (`ax.bar(values, probabilities, width=0.2)`) ;
- une droite verticale en pointillés à l'espérance, **calculée dans la fonction** à partir de `values` et `probabilities` (`ax.axvline`) ;
- un titre, et le nom des deux axes.

La cellule suivante trace la loi du nombre de piles en quatre lancers d'une pièce (`piles_values`, `piles_probs`, fournies), puis une autre la vérifie.

Dans ta copie : où se trouve l'espérance, et pourquoi pouvait-on la prévoir sans calcul ? Pourquoi la loi n'est-elle pas « plate », alors que les 16 suites de quatre lancers sont équiprobables ?""",
    given='''piles_values = [0, 1, 2, 3, 4]                       # number of piles in four coin flips
piles_probs = [1 / 16, 4 / 16, 6 / 16, 4 / 16, 1 / 16]''',
    todo='''def plot_law(ax, values, probabilities):
    """Draw the law (one bar per value) in ax, with a dashed vertical line at the expectation."""
    raise NotImplementedError("ax.bar, puis ax.axvline à l'espérance, un titre et les axes")''',
    check='''with checked("R8.22 figure"):
    fig, ax = plt.subplots(figsize=(6, 3.5))
    try:
        created = drawn(plot_law, ax, piles_values, piles_probs)
    except BaseException:
        plt.close(fig)                                     # no empty figure while the function is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex R8.22 : ta fonction ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans l'axe "
              "qu'elle reçoit.")
    else:
        plt.show()''',
    solution='''def plot_law(ax, values, probabilities):
    """Draw the law (one bar per value) in ax, with a dashed vertical line at the expectation."""
    mean = sum(v * p for v, p in zip(values, probabilities))
    ax.bar(values, probabilities, width=0.2)
    ax.axvline(mean, color="C1", linestyle="--", label=f"espérance = {mean:g}")
    ax.set_title("Loi du nombre de piles en quatre lancers")
    ax.set_xlabel("nombre de piles")
    ax.set_ylabel("probabilité")
    ax.legend()


fig, ax = plt.subplots(figsize=(6, 3.5))
plot_law(ax, piles_values, piles_probs)
plt.show()''',
    after=[("md", "**Vérifications automatiques** (la figure elle-même se juge à l'œil)."), ("code", R8_22_CHECK)],
    note="La loi est symétrique autour de 2 : l'espérance vaut 2, au centre. Elle n'est pas plate parce que les "
         "valeurs de la variable regroupent des nombres différents de suites équiprobables : 1, 4, 6, 4, 1, les "
         "coefficients binomiaux $\\binom{4}{k}$ (§3).",
)

# ---------------------------------------------------------------------------
# Notebook exercises: bugs and reproducibility (R8.23, R8.24)
# ---------------------------------------------------------------------------
R8_23_MISTAKES = bug_letters_mistakes(
    "ABE", "CD",
    {"A": "deux événements qui peuvent se réaliser ensemble ne s'additionnent pas : passe par le contraire",
     "B": "les trois nombres de piles ne sont pas équiprobables : distingue les deux pièces",
     "E": "incompatibles n'est pas indépendants : l'un empêche l'autre"})

R8_23 = Ex(
    "R8.23", "🐛", 2, 20, "Chasse à l'erreur : trois raisonnements de probabilités faux",
    "repérer des raisonnements faux (réunion, équiprobabilité, indépendance), puis calculer les bonnes probabilités.",
    "fiche §2 et §5", tracks="C, E",
    body="""Voici cinq raisonnements. Trois sont faux. **Sans calculer d'abord**, trouve-les.

- **(A)** « On lance deux fois un dé à 4 faces. La probabilité d'obtenir au moins un 4 est $\\frac{1}{4} + \\frac{1}{4} = \\frac{1}{2}$. »
- **(B)** « On lance deux pièces. On obtient 0, 1 ou 2 piles : trois cas, donc $P(\\text{exactement un pile}) = \\frac{1}{3}$. »
- **(C)** « $P(A) = 0{,}5$, $P(B) = 0{,}4$, et $A$ et $B$ sont indépendants, donc $P(A \\cap B) = 0{,}5 \\times 0{,}4 = 0{,}2$. »
- **(D)** « Une roue a 10 secteurs égaux, dont 3 rouges et 2 verts. Un secteur n'est jamais rouge et vert à la fois, donc $P(\\text{rouge ou vert}) = \\frac{3}{10} + \\frac{2}{10} = \\frac{1}{2}$. »
- **(E)** « $A$ et $B$ sont incompatibles, avec $P(A) = 0{,}3$ et $P(B) = 0{,}5$. Ils sont donc indépendants, et $P(A \\cap B) = 0{,}3 \\times 0{,}5 = 0{,}15$. »

Questions :
- a) les lettres des raisonnements faux, dans l'ordre alphabétique (un texte) ;
- b) les **bonnes** valeurs des probabilités que calculent les trois raisonnements faux, dans l'ordre alphabétique de leurs lettres (une liste, 4 décimales).

Dans ta copie : pour chaque raisonnement faux, quelle règle a été oubliée ? Lequel des deux raisonnements justes pouvait sembler faux, et pourquoi ne l'est-il pas ?""",
    todo='''answer_R8_23a = ...  # a) letters, as text
answer_R8_23b = ...  # b) a list of 3 probabilities (4 decimals)''',
    check='''wbm.check("R8.23a", answer_R8_23a)
wbm.check("R8.23b", answer_R8_23b)''',
    solution='''answer_R8_23a = "ABE"
answer_R8_23b = [1 - (3 / 4) ** 2, 2 / 4, 0.0]
print(answer_R8_23a, answer_R8_23b)''',
    record=f'''wbm.record("R8.23a", "ABE",
           mistakes={R8_23_MISTAKES})
wbm.record("R8.23b", [7 / 16, 0.5, 0.0], decimals=4,
           mistakes={{"ce sont les valeurs des raisonnements faux : calcule les bonnes": [0.5, 1 / 3, 0.15],
                     "(A) : « au moins un 4 » est le contraire de « aucun 4 »": [0.5, 0.5, 0.0],
                     "(E) : deux événements incompatibles ne se réalisent jamais ensemble": [7 / 16, 0.5, 0.15]}})''',
    note="(A) « Au moins un 4 » est le contraire de « aucun 4 » : $1 - \\left(\\frac{3}{4}\\right)^2 = \\frac{7}{16}$ "
         "(les deux « 4 » peuvent arriver ensemble, d'où l'erreur de l'addition). (B) Deux pièces font 4 suites "
         "équiprobables, dont 2 avec un seul pile : $\\frac{1}{2}$. (E) Incompatibles : $P(A \\cap B) = 0$. (D) est "
         "juste : rouge et vert sont incompatibles, on additionne. (C) aussi : c'est la définition de l'indépendance.",
)

R8_24_GIVEN = '''def measure(rng):
    """A noisy score: the accuracy of a model measured on 200 test examples drawn with rng."""
    return float((rng.random(200) < 0.85).mean())


def buggy_runs(n_runs, seed):
    """n_runs measures... with a classic bug."""
    results = []
    for _ in range(n_runs):
        rng = np.random.default_rng(seed)
        results.append(measure(rng))
    return results'''

R8_24_CHECK = '''with checked("R8.24 vérifications"):
    runs = run_experiments(5, seed=42)
    problems = []
    if not isinstance(runs, list) or len(runs) != 5:
        problems.append("run_experiments(5, seed) renvoie une liste de 5 mesures")
    else:
        if run_experiments(5, seed=42) != runs:
            problems.append("la même graine doit redonner exactement les mêmes mesures")
        if len(set(runs)) < 5:
            problems.append("les 5 mesures doivent différer : un seul générateur, créé avant la boucle, qui avance")
        if run_experiments(5, seed=43) == runs:
            problems.append("une autre graine doit donner d'autres mesures")
    if problems:
        print("❌ Ex R8.24 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex R8.24 : reproductible avec la même graine, différent d'une mesure à l'autre et d'une graine à "
              "l'autre.")
    print("buggy_runs(5, 42) :", buggy_runs(5, 42))'''

R8_24 = Ex(
    "R8.24", "🛠️", 1, 15, "Reproductibilité : générateur aléatoire et graine",
    "écrire une expérience aléatoire reproductible, et reconnaître le bug du générateur recréé à chaque tour.",
    "fiche §8 ; workbookIA 0A §100.8.7", tracks="C, E",
    body="""Dans workbookIA, chaque expérience fixe sa graine, pour que tes résultats soient ceux du corrigé. La fonction `measure(rng)` (fournie) simule un score bruité : l'accuracy d'un modèle mesurée sur 200 exemples de test tirés avec le générateur `rng`.

1. Écris `run_experiments(n_runs, seed)`, qui renvoie la liste de `n_runs` mesures, avec **un seul** générateur `np.random.default_rng(seed)`, créé avant la boucle.
2. La cellule de vérification contrôle que la même graine redonne les mêmes mesures, que les mesures diffèrent entre elles, et qu'une autre graine donne d'autres mesures ; puis elle affiche le résultat de `buggy_runs(5, 42)` (fournie).

Dans ta copie : que remarques-tu sur les mesures de `buggy_runs` ? Quelle ligne cause ce bug, et pourquoi ? Que mesure l'écart entre tes 5 mesures, et pourquoi ne faut-il pas comparer deux modèles sur une seule mesure ?""",
    given=R8_24_GIVEN,
    todo='''def run_experiments(n_runs, seed):
    """n_runs measures, with ONE generator default_rng(seed) created before the loop."""
    raise NotImplementedError("un générateur, puis une boucle qui appelle measure(rng)")''',
    check=R8_24_CHECK,
    solution='''def run_experiments(n_runs, seed):
    """n_runs measures, with ONE generator default_rng(seed) created before the loop."""
    rng = np.random.default_rng(seed)
    return [measure(rng) for _ in range(n_runs)]


print("run_experiments(5, 42) :", run_experiments(5, 42))
print("buggy_runs(5, 42)      :", buggy_runs(5, 42))''',
    note="`buggy_runs` recrée le générateur avec la même graine à chaque tour : il repart du même point, et les 5 "
         "mesures sont identiques. Ce n'est pas « plus reproductible », c'est une seule mesure répétée. Les 5 mesures "
         "de `run_experiments` varient de quelques points : c'est la fluctuation d'un score mesuré sur 200 exemples ; "
         "une différence de cet ordre entre deux modèles peut venir du seul hasard.",
)


PART_A = Part("A", "Ta librairie : dénombrer, énumérer, espérance et variance, simuler",
              "Fiche §2, §3, §7 et §8. Les six fonctions de `mymath/proba_basics.py`.",
              given=TOOLS, exercises=[R8_16, R8_17, R8_18, R8_19])

PART_B = Part("B", "Une prédiction, la loi des grands nombres et une figure",
              "Fiche §2 à §8. Une probabilité qui surprend presque tout le monde, des fréquences qui se resserrent "
              "autour d'une probabilité, puis une loi en image.",
              exercises=[R8_20, R8_21, R8_22])

PART_C = Part("C", "Raisonnements faux et reproductibilité",
              "Fiche §2, §5 et §8. Trois raisonnements faux à trouver, puis une expérience aléatoire reproductible.",
              exercises=[R8_23, R8_24])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | R8.1 à R8.10, R8.13 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# R8 · Probabilités de base — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/r8_probabilites/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py R8`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# R8 · Probabilités de base — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : univers et événements, probabilités, dénombrement, arbres, "
               "indépendance, lois, espérance et variance.\n"
               "- Écrire les six fonctions de `mymath/proba_basics.py` et les tester.\n"
               "- Prédire une probabilité qui surprend, mesurer la loi des grands nombres, tracer une loi, chasser "
               "des raisonnements faux et rendre une expérience reproductible.\n\n"
               "**Rappel express.** Équiprobabilité : $P(A) = \\frac{|A|}{|\\Omega|}$ ; $P(\\bar{A}) = 1 - P(A)$ ; "
               "$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$. $n!$ rangements, $\\binom{n}{k} = \\frac{n!}{k!\\,(n-k)!}$ "
               "choix sans ordre. Indépendance : $P(A \\cap B) = P(A)\\,P(B)$. $\\mathbb{E}[X] = \\sum x\\,P(X = x)$, "
               "$\\mathbb{V}(X) = \\mathbb{E}[X^2] - \\mathbb{E}[X]^2$. Un générateur `np.random.default_rng(graine)`, "
               "créé une fois.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Calcules-tu une probabilité par équiprobabilité, par le contraire ou avec un arbre ?\n"
               "2. Sais-tu choisir entre $n^k$, les arrangements, $n!$ et $\\binom{n}{k}$, et tester une "
               "indépendance ?\n"
               "3. Calcules-tu l'espérance et la variance d'une loi, et sais-tu dire ce qu'affirme la loi des grands "
               "nombres ?\n\n"
               "**La suite** : R9, *Géométrie du plan, vecteurs et trigonométrie*. Dans workbookIA, continue le "
               "chapitre 0A au rythme de ton tableau de bord.")]


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
