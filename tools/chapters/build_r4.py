#!/usr/bin/env python
"""Build the two notebooks of chapter R4 from a single source (used by Claude).

    python tools/chapters/build_r4.py
    python tools/run_all_notebooks.py chapitres/r4_logique_ensembles/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/r4_logique_ensembles/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ R4.1 to R4.8, 🔗 R4.14); parts A to C are the notebook exercises. Wrong-answer
messages state a rule, never a number of the answer. A column of a truth table is answered by the list of its values
in the order VV, VF, FV, FF (all true first, like itertools.product([True, False], repeat=n)); a set by the list of its
elements, in any order; a choice among numbered sentences by its number.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, check_unique_keys, guarded, md,  # noqa: E402
                         paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "R4"
FOLDER = "chapitres/r4_logique_ensembles"
CHOICES = "choices=[1, 2, 3, 4]"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("R4.1", "Tables de vérité de « et », « ou », « non » et de l'implication", [
        ("a", "a list of 4 values (rows VV, VF, FV, FF)", "[not (p and q) for p, q in ROWS2]",
         'mistakes={"non (P et Q) est vraie dès qu\'une des deux est fausse : ce n\'est pas « ni P ni Q »": '
         '[F, F, F, T], "c\'est la colonne de « P et Q » : il reste à la nier": [T, F, F, F]}'),
        ("b", "a list of 4 values", "[(not p) or (not q) for p, q in ROWS2]",
         'mistakes={"« ou » est vraie dès qu\'au moins une des deux est vraie": [F, F, F, T]}'),
        ("c", "True or False", "True",
         'mistakes={"compare les deux colonnes ligne par ligne : ce sont les lois de De Morgan": False}'),
        ("d", "a list of 4 values", "[(not p) or q for p, q in ROWS2]",
         'mistakes={"quand P est fausse, P ⇒ Q est vraie : elle n\'est fausse que si P est vraie et Q fausse": '
         '[T, F, F, F], "c\'est la colonne de Q ⇒ P, la réciproque": [T, T, F, T], '
         '"c\'est la colonne de la négation de P ⇒ Q": [F, T, F, F]}'),
        ("e", "a list of 4 values", "[(not q) or p for p, q in ROWS2]",
         'mistakes={"Q ⇒ P n\'est fausse que si Q est vraie et P fausse : regarde la ligne FV": [T, F, T, T], '
         '"Q ⇒ P est vraie quand Q est fausse": [T, F, F, F]}'),
        ("f", "a list of 4 values", "[q or (not p) for p, q in ROWS2]",
         'mistakes={"(non Q) ⇒ (non P) n\'est fausse que si non Q est vraie et non P fausse : regarde la ligne VF": '
         '[T, T, F, T]}'),
        ("g", "two letters, as text", '"df"',
         'mistakes={"une implication a la même table que sa contraposée, pas que sa réciproque": {"de", "ef"}}'),
        ("h", "an integer", "2 ** 3",
         'mistakes={"chaque proposition double le nombre de lignes : 2 × 2 × 2": 6, "2³, pas 3²": 9}'),
        ("i", "an integer", "sum(((p or q) and not r) for p, q, r in ROWS3)",
         'mistakes={"« et (non R) » : seules les lignes où R est fausse comptent": 6, '
         '"(P ou Q) est vraie dès qu\'une des deux l\'est : trois combinaisons de P et Q sur quatre": 1}'),
    ]),
    Paper("R4.2", "Réciproque, contraposée, négation : écrire les trois", [
        ("a", "the list [implication, converse, contrapositive, negation]", "[T, F, T, F]",
         'mistakes={"la réciproque « divisible par 3 ⇒ divisible par 6 » a un contre-exemple : essaie 9": [T, T, T, F], '
         '"la contraposée a toujours la même valeur que l\'implication": [T, F, F, F], '
         '"la négation d\'une implication vraie est fausse": [T, F, T, T]}'),
        ("b", "a list of 4 values", "[F, T, F, T]",
         'mistakes={"x² > 25 vaut aussi pour des nombres négatifs : essaie-en un": [T, F, T, F], '
         '"la contraposée a toujours la même valeur que l\'implication": [F, T, T, T]}'),
        ("c", "a list of 4 values", "[F, F, F, T]",
         'mistakes={"un seul contre-exemple suffit : cherche un impair qui n\'est pas premier": [T, F, T, F], '
         '"la réciproque « premier ⇒ impair » a un contre-exemple : 2": [F, T, F, T]}'),
        ("d", "a list of 4 values", "[T, T, T, F]",
         'mistakes={"3x − 2 = 10 équivaut à x = 4 : la réciproque est vraie aussi (une équivalence)": [T, F, T, F]}'),
        ("e", "an integer", "9",
         'mistakes={"3, 5 et 7 sont premiers : la propriété est vraie pour eux": {3, 5, 7}}'),
        ("f", "an integer", "-6",
         'mistakes={"pour x = −5, x² = 25, qui n\'est pas strictement plus grand que 25": -5, '
         '"on cherche un entier négatif": 6}'),
    ]),
    Paper("R4.3", "Nier des phrases à deux quantificateurs", [
        ("a", "a number (1 to 4)", "2",
         f'{CHOICES}, mistakes={{"nier « pour tout x » donne « il existe x » : le premier quantificateur change aussi": '
         f'1, "nier « il existe y » donne « pour tout y »": 3, "on garde l\'ordre des variables : on change chaque '
         f'quantificateur, puis on nie la fin": 4}}'),
        ("b", "True or False", "True", 'mistakes={"à x donné, cherche un y plus grand : x + 1 convient": False}'),
        ("c", "a number (1 to 4)", "1",
         f'{CHOICES}, mistakes={{"nier « pour tout x » donne « il existe x »": 2, '
         f'"nier « il existe M » donne « pour tout M »": 3, "la négation de x² ≤ M est x² > M, pas x² ≥ M": 4}}'),
        ("d", "True or False", "False",
         'mistakes={"x² n\'est pas majoré : pour tout M, un x assez grand donne x² > M": True}'),
        ("e", "a list of 2 values", "[F, T]",
         'mistakes={"y² = x n\'a pas de solution réelle quand x est négatif ; et y = 0 convient pour tous les x": '
         '[T, F], "essaie x = −1 dans la première phrase": [T, T], "essaie y = 0 dans la seconde phrase": [F, F]}'),
        ("f", "a number (1 to 4)", "1",
         f'{CHOICES}, mistakes={{"nier « pour tout ε > 0 » donne « il existe ε > 0 » : la condition ε > 0 reste, '
         f'seul le quantificateur change": 3, "nier « pour tout ε » donne « il existe ε »": 2, '
         f'"nier « il existe N » donne « pour tout N »": 4}}'),
        ("g", "True or False", "True",
         'mistakes={"à ε donné, un entier N plus grand que 1/ε convient": False}'),
    ]),
    Paper("R4.4", "Union, intersection, complémentaire et cardinal", [
        ("a", "a set, as a list (empty if it is empty)", "sorted(SQUARES & PRIMES)",
         'ordered=False, mistakes={"1 n\'est pas un nombre premier": [1]}'),
        ("b", "an integer", "len(SQUARES | PRIMES)",
         'mistakes={"compte d\'abord les carrés (5) et les premiers de E, puis retire ceux qui sont les deux": 13}'),
        ("c", "a set, as a list", "sorted(PRIMES & LATE)",
         'ordered=False, mistakes={"23 est premier, et 23 ≥ 17": [17, 19], "17 ≥ 17 : 17 est dans C": [19, 23]}'),
        ("d", "an integer", "len(E - PRIMES)",
         'mistakes={"le complémentaire de B : les éléments de E qui ne sont pas premiers": 9}'),
        ("e", "an integer", "len(PRIMES | LATE)",
         'mistakes={"les éléments de B ∩ C ont été comptés deux fois : retire-les une fois": 18}'),
        ("f", "a set, as a list", "sorted(SQUARES - LATE)",
         'ordered=False, mistakes={"25 est dans C : il faut le retirer": [1, 4, 9, 16, 25], '
         '"A \\\\ C contient les éléments de A qui ne sont pas dans C": [25]}'),
        ("g", "an integer", "len(E - (SQUARES | LATE))",
         'mistakes={"on demande le complémentaire de A ∪ C, pas A ∪ C": 13, '
         '"25 est à la fois dans A et dans C : ne le compte qu\'une fois": 11}'),
        ("h", "an integer", "30 - (17 + 12 - 5)",
         'mistakes={"les 5 élèves qui font les deux sont comptés deux fois dans 17 + 12": 1, '
         '"on demande ceux qui ne font ni l\'un ni l\'autre": 24}'),
    ]),
    Paper("R4.5", "Produit cartésien et couples", [
        ("a", "an integer", "len(PAIRS_AB)",
         'mistakes={"chaque élément de A va avec chaque élément de B : on multiplie": 5}'),
        ("b", "an integer", "2 ** 3", 'mistakes={"2 choix pour chacune des trois coordonnées : 2 × 2 × 2": 6}'),
        ("c", "an integer", "sum(x < y for x in B_SET for y in B_SET)",
         'mistakes={"x < y est strict : (1, 1) ne convient pas": 6, '
         '"un couple (2, 1) n\'a pas x < y : l\'ordre des coordonnées compte": 9}'),
        ("d", "an integer", "sum(a + b == 2 for a, b in PAIRS_AB)",
         'mistakes={"pense aux deux valeurs possibles de a, 0 et 1": 1}'),
        ("e", "True or False", "(1, 0) in PAIRS_AB",
         'mistakes={"la seconde coordonnée doit appartenir à B": True}'),
        ("f", "an integer", "3 * 4 * 2", 'mistakes={"chaque choix se combine avec tous les autres : on multiplie": 9}'),
        ("g", "True or False", "False",
         'mistakes={"un couple est ordonné : (0, 2) est dans A × B, mais pas dans B × A": True}'),
    ]),
    Paper("R4.6", "Calculer des sommes Σ et des produits Π", [
        ("a", "an integer", "sum(3 * k - 2 for k in range(1, 7))",
         'mistakes={"le −2 est dans chaque terme : il est retiré six fois": 61}'),
        ("b", "an integer", "sum(j ** 2 for j in range(2, 6))",
         'mistakes={"la somme commence à j = 2": 55, "j va jusqu\'à 5 inclus": 29}'),
        ("c", "an integer", "sum((-1) ** i for i in range(0, 5))",
         'mistakes={"de i = 0 à 4, il y a 5 termes, et (−1)⁰ = 1": 0}'),
        ("d", "a fraction, as text", "sum(Fraction(1, k) for k in range(1, 5))",
         'kind="fraction", mistakes={"la somme commence à k = 1 : 1/1 = 1 compte": "13/12"}'),
        ("e", "an integer", "int(math.prod(Fraction(k, k - 1) for k in range(2, 6)))",
         'mistakes={"k va jusqu\'à 5 inclus": 4}'),
        ("f", "an integer", "math.prod(i + 2 for i in range(1, 4))",
         'mistakes={"le facteur est i + 2, pas i": 6}'),
        ("g", "an integer", "sum(2 for k in range(3, 11))",
         'mistakes={"de 3 à 10, il y a 10 − 3 + 1 = 8 termes": 14, "la somme commence à k = 3": 20}'),
        ("h", "an integer", "math.prod(-1 for k in range(1, 6))",
         'mistakes={"cinq facteurs −1 : un nombre impair de signes moins": 1, "un produit, pas une somme": -5}'),
        ("i", "an integer", "30 - 7 + 1", 'mistakes={"de 7 à 30, il y a 30 − 7 + 1 termes : 7 et 30 comptent": 23}'),
    ]),
    Paper("R4.7", "Développer, réindexer et découper une somme Σ ; calculer une somme double", [
        ("a", "an integer", "2 * 55 + 3 * 10",
         'mistakes={"la constante 3 est ajoutée à chacun des 10 termes": 113}'),
        ("b", "an integer", "210 - 55",
         'mistakes={"de 11 à 20 = de 1 à 20 moins de 1 à 10 : le terme 11 doit rester": 144, '
         '"retire la somme de 1 à 10": 210}'),
        ("c", "an integer", "sum(k ** 2 for k in range(1, 11))",
         'mistakes={"quand j va de 0 à 9, k = j + 1 va de 1 à 10": 285, "k va jusqu\'à 10, pas 11": 506}'),
        ("d", "an expression in n, as text", '"n**2 + 4*n"',
         'kind="expr", variables=("n",), mistakes={"la constante 3 est ajoutée n fois": "n**2 + n + 3", '
         '"2 × n(n + 1)/2 = n(n + 1) = n² + n": "n**2 + 3*n"}'),
        ("e", "the list [p, q]", "[1, 6]",
         'mistakes={"avec j = k − 2, les bornes diminuent de 2": [5, 10], '
         '"les bornes changent avec l\'indice": [3, 8]}'),
        ("f", "an integer", "sum(i + 2 * j for i in range(1, 3) for j in range(1, 5))",
         'mistakes={"pour chaque i, la somme sur j a 4 termes, donc i est ajouté 4 fois": 43}'),
        ("g", "an integer", "sum(i for i in range(1, 5)) * sum(2 ** j for j in range(0, 3))",
         'mistakes={"j commence à 0 : 2⁰ = 1 compte": 60}'),
        ("h", "a fraction, as text", "Fraction(1) - Fraction(1, 10)",
         'kind="fraction", mistakes={"le dernier terme est −1/10 : il reste 1 − 1/10": "8/9"}'),
    ]),
    Paper("R4.8", "Trouver un contre-exemple", [
        ("a", "an integer", "next(n for n in range(1, 100) if not 2 ** n > n ** 2)",
         'mistakes={"2² = 4 n\'est pas strictement plus grand que 2² = 4": 3}'),
        ("b", "an integer", "4",
         'mistakes={"il y a un contre-exemple plus petit : essaie les valeurs de n une par une": {6, 8, 9, 10, 11}}'),
        ("c", "an interval, as text", '"]0 ; 1["',
         'kind="interval", mistakes={"en 0 et en 1, x² = x : l\'inégalité large y est vraie": "[0 ; 1]", '
         '"pour x négatif, x² est positif, donc plus grand que x": "]-oo ; 1["}'),
        ("d", "an integer", "12",
         'mistakes={"24 est divisible par 24 : ce n\'est pas un contre-exemple": 24}'),
        ("e", "an integer", "2 + 3", 'mistakes={"2 + 2 = 4 est pair": 4}'),
        ("f", "a set, as a list", "[0]",
         'ordered=False, mistakes={"développe (x + 1)² = x² + 2x + 1 : l\'égalité devient 2x = 0": []}'),
    ]),
    Paper("R4.14", "Écrire la loss moyenne d'un modèle avec Σ", [
        ("a", "an integer", "sum(ERRORS)",
         'mistakes={"e_i = ŷ_i − y_i garde son signe : les erreurs se compensent": 4, '
         '"e_i = ŷ_i − y_i : prédiction moins vraie valeur": 2}'),
        ("b", "a number (or a fraction)", "Fraction(sum(e ** 2 for e in ERRORS), 5)",
         'kind="fraction", mistakes={"une moyenne : divise par n = 5": 6, "élève chaque erreur au carré": "-2/5"}'),
        ("c", "a number (or a fraction)", "Fraction(sum(abs(e) for e in ERRORS), 5)",
         'kind="fraction", mistakes={"une moyenne : divise par n = 5": 4, '
         '"la valeur absolue de chaque erreur, avant de les ajouter": "-2/5"}'),
        ("d", "a number (or a fraction)", "Fraction(sum(e ** 2 for e in OUTLIER), 5)",
         'kind="fraction", mistakes={"la nouvelle erreur, 16 − 6, est élevée au carré elle aussi": "16/5"}'),
        ("e", "a number (or a fraction)", "Fraction(sum(abs(e) for e in OUTLIER), 5)",
         'kind="fraction", mistakes={"une moyenne : divise par n = 5": 14}'),
        ("f", "1 or 2", "1",
         'choices=[1, 2], mistakes={"compare les facteurs : la nouvelle valeur divisée par l\'ancienne, pour chaque '
         'mesure": 2}'),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import itertools
import math
from fractions import Fraction

T, F = True, False
ROWS2 = list(itertools.product([True, False], repeat=2))          # VV, VF, FV, FF
ROWS3 = list(itertools.product([True, False], repeat=3))
E = set(range(1, 26))                                             # R4.4
SQUARES = {k * k for k in range(1, 6)}
PRIMES = {n for n in E if n > 1 and all(n % d for d in range(2, n))}
LATE = {n for n in E if n >= 17}
B_SET = {1, 2, 3}                                                 # R4.5
PAIRS_AB = {(a, b) for a in (0, 1) for b in B_SET}
TRUE_Y, PRED_Y = [3, 5, 2, 8, 6], [4, 5, 1, 6, 6]                 # R4.14
ERRORS = [p - y for p, y in zip(PRED_Y, TRUE_Y)]
OUTLIER = ERRORS[:4] + [16 - 6]'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ R4.1 à R4.8, 🔗 R4.14)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- une colonne de table de vérité par la liste de ses valeurs, dans l'ordre des lignes VV, VF, FV, FF : "
               "`[True, False, False, False]` pour « P et Q » (ou les lettres V et F, entre guillemets) ;\n"
               "- vrai ou faux par `True` ou `False` ; un numéro de réponse proposée par un entier ;\n"
               "- un ensemble par la liste de ses éléments, dans l'ordre que tu veux, la liste vide pour $\\varnothing$ ;\n"
               "- un nombre avec un point décimal, `-1.5` ; une fraction exacte entre guillemets, `\"5/7\"` ;\n"
               "- une expression entre guillemets, `\"3*n**2 + 1\"` ; un intervalle entre guillemets, `\"]-1 ; 4]\"`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Part A: logic in Python (R4.17, R4.19, R4.21)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

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
    return "aucune"


def is_prime(n):
    """True if the integer n is a prime number (it has exactly two divisors, 1 and itself)."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True'''

LOAD_LEARNER = 'mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="R4")  # reload your saved file'
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en R2 et R3). Ouvre ta copie `mon_travail/mymath/logic.py`, lis la "
         "docstring de la fonction en entier, remplace la ligne `raise NotImplementedError(...)` par ton code, "
         "**enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. Les "
         "tests comparent tes résultats à SymPy et à une évaluation directe.")

WRONG_ERROR = "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of logic.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_r4_logic.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_r4_logic.py", "{keyword}", impl="ref")')]


R4_17 = Ex(
    "R4.17", "🔨", 1, 30, "Tables de vérité et implication · `truth_table`, `implies`",
    "programmer une table de vérité pour n'importe quelle formule, et l'implication.",
    "fiche §1 et §2 ; workbookIA 0A §100.6.6 (`itertools`, aperçu)", tracks="C", mymath="logic.py",
    body=HOWTO + """

Dans `mon_travail/mymath/logic.py` :
- `truth_table(formula, n)` : une `ValueError` si `n < 1` ; sinon, pour chaque combinaison de `n` booléens, dans l'ordre de `itertools.product([True, False], repeat=n)` (toutes vraies d'abord), la ligne `(values, result)`, où `values` est le tuple des `n` booléens et `result` la valeur de la formule. Pour appeler la formule avec les `n` valeurs d'un tuple, écris `formula(*values)` : l'étoile déplie le tuple en `n` arguments.
- `implies(p, q)` : la valeur de vérité de $p \\Rightarrow q$, en une ligne, avec `not` et `or` (fiche §2).

La vérification calcule, avec tes deux fonctions, la colonne de « (p et q) ⇒ r », le nombre de lignes d'une table à quatre variables, puis le nom de l'erreur levée pour `n = 0` (avec `raised`, de la cellule des outils).""",
    todo=LOAD_LEARNER,
    check='''with checked("R4.17a"):
    rows = mymath.logic.truth_table(lambda p, q, r: mymath.logic.implies(p and q, r), 3)
    wbm.check("R4.17a", [result for values, result in rows], computed=True)
with checked("R4.17b"):
    wbm.check("R4.17b", len(mymath.logic.truth_table(lambda a, b, c, d: a or d, 4)), computed=True)
with checked("R4.17c"):
    wbm.check("R4.17c", raised(mymath.logic.truth_table, lambda: True, 0), computed=True)''',
    solution=LOAD_REF + '''
for values, result in mymath.logic.truth_table(lambda p, q, r: mymath.logic.implies(p and q, r), 3):
    print(values, "->", result)
print("lignes pour 4 variables :", len(mymath.logic.truth_table(lambda a, b, c, d: a or d, 4)))
print("n = 0 :", raised(mymath.logic.truth_table, lambda: True, 0))''',
    record=f'''wbm.record("R4.17a", [True, False, True, True, True, True, True, True],
           mistakes={{"implies(p, q) n'est fausse que si p est vraie et q fausse : ce n'est pas « p et q »":
                         [True, False, False, False, False, False, False, False],
                     "les lignes commencent par « tout vrai » : itertools.product([True, False], repeat=n)":
                         [True, True, True, True, True, True, False, True],
                     "implies(p, q) est l'implication p ⇒ q, pas sa réciproque q ⇒ p":
                         [True, True, False, True, False, True, False, True]}})
wbm.record("R4.17b", 16, mistakes={{"une table à n variables a 2**n lignes, une par combinaison": 8}})
wbm.record("R4.17c", "ValueError",
           mistakes={{"avec n < 1, la fonction doit lever une ValueError (raise), pas rendre un résultat": "aucune",
                     "{WRONG_ERROR}": {{"Exception", "TypeError", "IndexError", "AssertionError"}}}})''',
    after=tests_cells("test_truth_table_ or test_implies_"),
    note="`itertools.product([True, False], repeat=n)` énumère exactement les $2^n$ lignes, dans l'ordre usuel. Sans "
         "lui, on peut aussi compter de 0 à $2^n - 1$ et lire les chiffres binaires : c'est la même table.",
)

R4_19 = Ex(
    "R4.19", "🔨", 2, 30, "Chercher un contre-exemple de 0 à N · `find_counterexample`",
    "programmer la recherche systématique d'un contre-exemple, et comprendre ce qu'elle prouve et ne prouve pas.",
    "fiche §6 ; R4.17", tracks="C, E", mymath="logic.py",
    body="""Écris `find_counterexample(predicate, n_max)` dans `mon_travail/mymath/logic.py` : essaie les entiers $n = 0, 1, \\dots, n_{\\max}$ **dans l'ordre**, et rends le premier pour lequel `predicate(n)` est faux ; si aucun ne l'est, rends `None`. `predicate` représente la phrase « pour tout $n$, $P(n)$ ».

La vérification cherche :
- a) le premier $n$ pour lequel « $n! < 10^6$ » est faux ;
- b) si « $n^3 - n$ est divisible par 3 » tient de 0 à 1 000 (ta fonction doit alors rendre `None`) ;
- c) un contre-exemple de « $n > 0$ » (attention à $n = 0$) ;
- d) un contre-exemple de « $n < 20$ » avec $n_{\\max} = 20$ (attention à $n_{\\max}$).

Puis, dans ta copie : la réponse de b) démontre-t-elle que $n^3 - n$ est toujours divisible par 3 ? Démontre-le (écris $n^3 - n = (n - 1)\\,n\\,(n + 1)$).""",
    todo=LOAD_LEARNER,
    check='''with checked("R4.19a"):
    wbm.check("R4.19a", mymath.logic.find_counterexample(lambda n: math.factorial(n) < 10**6, 50), computed=True)
with checked("R4.19b"):
    wbm.check("R4.19b", mymath.logic.find_counterexample(lambda n: (n**3 - n) % 3 == 0, 1000) is None,
              computed=True)
with checked("R4.19c"):
    wbm.check("R4.19c", mymath.logic.find_counterexample(lambda n: n > 0, 10) == 0, computed=True)
with checked("R4.19d"):
    wbm.check("R4.19d", mymath.logic.find_counterexample(lambda n: n < 20, 20) == 20, computed=True)''',
    solution=LOAD_REF + '''
print("a) n! < 10**6 échoue en n =", mymath.logic.find_counterexample(lambda n: math.factorial(n) < 10**6, 50))
print("b)", mymath.logic.find_counterexample(lambda n: (n**3 - n) % 3 == 0, 1000))
print("c)", mymath.logic.find_counterexample(lambda n: n > 0, 10))
print("d)", mymath.logic.find_counterexample(lambda n: n < 20, 20))''',
    record='''wbm.record("R4.19a", 10,
           mistakes={"la fonction rend le premier n où la propriété est FAUSSE, pas le dernier où elle est vraie": 9})
wbm.record("R4.19b", True,
           mistakes={"quand aucun n de 0 à n_max ne contredit la propriété, la fonction rend None": False})
wbm.record("R4.19c", True,
           mistakes={"0 est le premier entier à essayer : range(n_max + 1) commence à 0": False})
wbm.record("R4.19d", True,
           mistakes={"n_max est essayé lui aussi : range(n_max + 1)": False})''',
    after=tests_cells("test_find_counterexample_"),
    note="`None` après 1 000 essais ne démontre rien pour $n = 1\\,001$ : seul un argument le fait. Ici, $(n - 1)\\,n\\,"
         "(n + 1)$ est un produit de trois entiers consécutifs, dont l'un est divisible par 3 (disjonction de cas sur "
         "le reste de $n$ dans la division par 3).",
)

R4_21_EXPERIMENT = '''values = [(n, n * n + n + 41) for n in range(46)]
for n, value in values[:5] + values[37:44]:
    print(f"n = {n:2d} : n² + n + 41 = {value:5d}   premier : {is_prime(value)}")
first = next(n for n, value in values if not is_prime(value))
print("premier n pour lequel ce n'est pas un nombre premier :", first, "->", first * first + first + 41)'''

R4_21 = Ex(
    "R4.21", "🔮", 1, 15, "Prédire : n² + n + 41 est-il toujours un nombre premier ?",
    "voir une propriété vraie sur des dizaines de cas tomber, et comprendre pourquoi des exemples ne démontrent rien.",
    "fiche §6 ; R4.19", tracks="C, E", hypothesis=True,
    body="""Calcule de tête $n^2 + n + 41$ pour $n = 0, 1, 2, 3$ : tu obtiens 41, 43, 47, 53, tous des nombres premiers. **Avant d'exécuter quoi que ce soit**, prédis :
- a) $n^2 + n + 41$ est-il premier pour **tout** entier $n \\ge 0$ ? (`True` ou `False`)
- b) le plus petit entier $n$ pour lequel il ne l'est pas, ou `-1` si tu penses qu'il n'y en a pas.

Écris tes deux prédictions, vérifie-les, puis lance l'expérience (elle se sert de `is_prime`, de la cellule des outils ; tu pourrais aussi utiliser ta fonction `find_counterexample`).""",
    todo='''prediction_R4_21a = ...  # a) True or False, written BEFORE running the experiment below
prediction_R4_21b = ...  # b) an integer (-1 if you think there is none)''',
    check='''for letter, prediction in zip("ab", [prediction_R4_21a, prediction_R4_21b]):
    wbm.check(f"R4.21{letter}", prediction)''',
    record='''wbm.record("R4.21a", False, prediction=True,
           mistakes={"une propriété vérifiée sur beaucoup de cas n'est pas démontrée : l'expérience cherche un "
                     "contre-exemple": True})
wbm.record("R4.21b", 40, prediction=True,
           mistakes={"tu as prédit qu'il n'y en a pas : l'expérience montre le contraire": -1})''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes deux prédictions écrites."),
        ("todo", guarded(R4_21_EXPERIMENT, ["prediction_R4_21a", "prediction_R4_21b"],
                         "⏳ Écris d'abord tes deux prédictions, puis exécute à nouveau.")),
        ("solution", R4_21_EXPERIMENT),
        ("md", "**Après l'expérience.** c) Combien d'entiers $n$ de 0 à 39 donnent un nombre premier ? Puis, dans ta "
               "copie : explique **sans calculer** pourquoi $n = 41$ ne peut pas donner un nombre premier."),
        ("todo", "answer_R4_21c = ...  # c) an integer"),
        ("check", 'wbm.check("R4.21c", answer_R4_21c)'),
        ("solution", "answer_R4_21c = sum(is_prime(n * n + n + 41) for n in range(40))\nprint(answer_R4_21c)"),
        ("record", 'wbm.record("R4.21c", 40, mistakes={"de 0 à 39 inclus, il y a 40 entiers": 39})'),
    ],
    note="Pour $n = 40$, $n^2 + n + 41 = 40 \\times 41 + 41 = 41^2 = 1\\,681$. Pour $n = 41$, les trois termes sont "
         "divisibles par 41. Quarante cas vrais de suite, et pourtant la phrase « pour tout $n$ » est fausse : c'est "
         "pourquoi on démontre au lieu de vérifier.",
)

PART_A = Part("A", "La logique en Python",
              "Fiche §1, §2 et §6. Tes premières fonctions de `mymath/logic.py` : une table de vérité, l'implication, "
              "la recherche d'un contre-exemple ; puis une propriété qui tient longtemps avant de tomber.",
              given=TOOLS, exercises=[R4_17, R4_19, R4_21])

# ---------------------------------------------------------------------------
# Part B: sets (R4.20, R4.23)
# ---------------------------------------------------------------------------
R4_20 = Ex(
    "R4.20", "📦", 1, 10, "Les ensembles de Python : `set`, `|`, `&`, `-`",
    "calculer unions, intersections, différences et inclusions avec les ensembles de Python.",
    "fiche §4 ; workbookIA 0A §100.3.4 (ensembles)", tracks="C, E",
    body="""`set("mot")` est l'ensemble des **lettres** d'un mot, sans répétition ni ordre. On pose `A = set("mathematiques")` et `B = set("statistiques")`. Avec les opérateurs de Python (`|` union, `&` intersection, `-` différence, `<=` inclusion, `len` cardinal, `==` égalité), calcule en une ligne chacun :
- a) le nombre de lettres différentes du mot « anticonstitutionnellement » ;
- b) les lettres communes à A et B (un ensemble) ;
- c) le nombre d'éléments de $A \\cup B$ ;
- d) $B \\subset A$ ? (`True` ou `False`)
- e) les lettres de A qui ne sont pas dans B (un ensemble) ;
- f) les mots « algorithme » et « logarithme » ont-ils le même ensemble de lettres ?

Puis, dans ta copie : explique la réponse de c) à partir de celle de d).""",
    todo='''A = set("mathematiques")
B = set("statistiques")

answer_R4_20a = ...  # a) an integer
answer_R4_20b = ...  # b) a set
answer_R4_20c = ...  # c) an integer
answer_R4_20d = ...  # d) True or False
answer_R4_20e = ...  # e) a set
answer_R4_20f = ...  # f) True or False''',
    check='''for letter, answer in zip("abcdef", [answer_R4_20a, answer_R4_20b, answer_R4_20c, answer_R4_20d,
                                       answer_R4_20e, answer_R4_20f]):
    wbm.check(f"R4.20{letter}", answer)''',
    solution='''A = set("mathematiques")
B = set("statistiques")

answer_R4_20a = len(set("anticonstitutionnellement"))
answer_R4_20b = A & B
answer_R4_20c = len(A | B)
answer_R4_20d = B <= A
answer_R4_20e = A - B
answer_R4_20f = set("algorithme") == set("logarithme")
print(answer_R4_20a, sorted(answer_R4_20b), answer_R4_20c, answer_R4_20d, sorted(answer_R4_20e), answer_R4_20f)''',
    record='''wbm.record("R4.20a", 11, mistakes={"set garde chaque lettre une seule fois : len(set(mot))": 25})
wbm.record("R4.20b", sorted(set("mathematiques") & set("statistiques")), ordered=False,
           mistakes={"A & B : les lettres qui sont dans A et dans B": ["h", "m"]})
wbm.record("R4.20c", 9,
           mistakes={"les lettres communes ne comptent qu'une fois : |A ∪ B| = |A| + |B| − |A ∩ B|": 16})
wbm.record("R4.20d", True, mistakes={"B <= A teste si chaque lettre de B est aussi dans A": False})
wbm.record("R4.20e", ["h", "m"], ordered=False,
           mistakes={"A - B : les lettres de A qui ne sont pas dans B": []})
wbm.record("R4.20f", True, mistakes={"compare les ensembles de lettres, pas les mots": False})''',
    note="B est inclus dans A, donc $A \\cup B = A$ et $\\lvert A \\cup B \\rvert = \\lvert A \\rvert = 9$. Et "
         "« algorithme » et « logarithme » sont des anagrammes : mêmes lettres, autre ordre. Un ensemble oublie "
         "l'ordre et les répétitions ; c'est exactement ce qu'on lui demande.",
)

R4_23_GIVEN = '''def show_regions(xs, ys, regions, titles):
    """Draw four boolean masks of the grid (xs, ys) as shaded Venn diagrams, in a 2 × 2 figure."""
    fig, axes = plt.subplots(2, 2, figsize=(9, 5.4))
    for ax, mask, title in zip(axes.ravel(), regions, titles):
        ax.contourf(xs, ys, np.asarray(mask, dtype=float), levels=[0.5, 1.5], colors=["C0"], alpha=0.45)
        for centre, name in ((-0.55, "A"), (0.55, "B")):
            ax.add_patch(plt.Circle((centre, 0), 1, fill=False, linewidth=1.6))
            ax.text(centre * 2.3, 0.8, name, fontsize=12, ha="center", fontweight="bold")
        ax.add_patch(plt.Rectangle((-2.2, -1.5), 4.4, 3, fill=False, linewidth=1.4))
        ax.set_title(title, fontsize=11)
        ax.set_xlim(-2.3, 2.3)
        ax.set_ylim(-1.6, 1.6)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.tight_layout()
    plt.show()


# the universe E: a grid of points; A and B: two discs
xs, ys = np.meshgrid(np.linspace(-2.2, 2.2, 300), np.linspace(-1.5, 1.5, 200))
in_a = (xs + 0.55) ** 2 + ys**2 <= 1
in_b = (xs - 0.55) ** 2 + ys**2 <= 1
TITLES = ["non A et non B", "non (A ou B)", "non A ou non B", "non (A et B)"]'''

R4_23_CHECK = '''with checked("R4.23 vérifications"):
    regions = [np.asarray(mask, dtype=bool) for mask in venn_regions(in_a, in_b)]
    outside, only_a, both = (0, 140), (100, 60), (100, 150)      # three points of the grid (row, column)
    problems = []
    if len(regions) != 4 or any(mask.shape != in_a.shape for mask in regions):
        problems.append("quatre tableaux de booléens de la forme de in_a")
    else:
        if not regions[0][outside] or regions[0][only_a]:
            problems.append("le 1ᵉʳ : les points qui ne sont ni dans A ni dans B")
        if not regions[2][only_a] or regions[2][both]:
            problems.append("le 3ᵉ : les points qui manquent à A ou à B")
        if not np.array_equal(regions[0], regions[1]) or not np.array_equal(regions[2], regions[3]):
            problems.append("le 2ᵉ égal au 1ᵉʳ, et le 4ᵉ égal au 3ᵉ, point par point")
    if problems:
        print("❌ Ex R4.23 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex R4.23 : les deux paires de régions coïncident point par point ; écris dans ta copie la loi "
              "qu'elles illustrent.")'''

R4_23 = Ex(
    "R4.23", "🎨", 1, 15, "Diagrammes de Venn",
    "voir les opérations sur les ensembles, et vérifier les lois de De Morgan sur une figure.",
    "fiche §4 ; R0 (matplotlib)", tracks="C",
    body="""La cellule ci-dessous fabrique l'univers $E$ (une grille de points) et deux disques $A$ et $B$ : `in_a` et `in_b` sont des tableaux de booléens qui disent, pour chaque point, s'il est dans $A$ ou dans $B$. Sur ces tableaux, NumPy calcule point par point : `~` est « non », `&` est « et », `|` est « ou » (mets des parenthèses : `~in_a & ~in_b`).

Complète `venn_regions(in_a, in_b)`, qui rend la liste des quatre tableaux :
1. $\\bar{A} \\cap \\bar{B}$ (ni dans $A$, ni dans $B$) ;
2. $\\overline{A \\cup B}$ ;
3. $\\bar{A} \\cup \\bar{B}$ ;
4. $\\overline{A \\cap B}$.

La vérification les dessine, puis regarde quelques points. Dans ta copie : quelles régions coïncident, et quelle loi de la fiche cela illustre-t-il ?""",
    given=R4_23_GIVEN,
    todo='''def venn_regions(in_a, in_b):
    """[not A and not B, not (A or B), not A or not B, not (A and B)]: four boolean arrays, point by point."""
    raise NotImplementedError("combine in_a and in_b with ~, & and |")''',
    check='''with checked("R4.23"):
    show_regions(xs, ys, venn_regions(in_a, in_b), TITLES)''',
    solution='''def venn_regions(in_a, in_b):
    """[not A and not B, not (A or B), not A or not B, not (A and B)]: four boolean arrays, point by point."""
    return [~in_a & ~in_b, ~(in_a | in_b), ~in_a | ~in_b, ~(in_a & in_b)]


show_regions(xs, ys, venn_regions(in_a, in_b), TITLES)''',
    after=[("md", "**Vérifications automatiques** (la figure elle-même se juge à l'œil)."), ("code", R4_23_CHECK)],
    note="Les régions 1 et 2 coïncident, et 3 et 4 aussi : ce sont les lois de De Morgan, "
         "$\\overline{A \\cup B} = \\bar{A} \\cap \\bar{B}$ et $\\overline{A \\cap B} = \\bar{A} \\cup \\bar{B}$. La "
         "figure ne démontre rien pour tous les ensembles ; la table de vérité de R4.1 le fait, parce qu'un point est "
         "dans $A$ ou non, et dans $B$ ou non : quatre cas, tous vérifiés.",
)

PART_B = Part("B", "Les ensembles", "Fiche §4. Les ensembles de Python, puis les lois de De Morgan en image.",
              exercises=[R4_20, R4_23])

# ---------------------------------------------------------------------------
# Part C: Σ and Π, induction (R4.18, R4.22, R4.24, R4.25)
# ---------------------------------------------------------------------------
R4_18 = Ex(
    "R4.18", "🔨", 1, 25, "Σ et Π en Python · `sum_over`, `prod_over`",
    "programmer Σ et Π avec leurs bornes incluses, et les cas de la somme et du produit vides.",
    "fiche §5", tracks="C, E", mymath="logic.py",
    body=HOWTO + """

Écris `sum_over(f, start, stop)` et `prod_over(f, start, stop)` : la somme et le produit des `f(k)` pour `k` allant de `start` à `stop`, **les deux bornes incluses**, comme $\\sum_{k=\\text{start}}^{\\text{stop}} f(k)$ et $\\prod_{k=\\text{start}}^{\\text{stop}} f(k)$. Une boucle `for` sur un `range` et un total suffisent ; réfléchis à la valeur de départ du total, et à ce que rendent les deux fonctions quand `stop < start` (fiche §5).

La vérification calcule $\\sum_{k=1}^{5} k(k+1)$, une somme vide, $\\prod_{k=1}^{10} 2$ et un produit vide, puis $\\sum_{k=1}^{10} \\frac{1}{2^k}$.""",
    todo=LOAD_LEARNER,
    check='''with checked("R4.18a"):
    wbm.check("R4.18a", [mymath.logic.sum_over(lambda k: k * (k + 1), 1, 5), mymath.logic.sum_over(lambda k: k, 5, 4),
                         mymath.logic.prod_over(lambda k: 2, 1, 10), mymath.logic.prod_over(lambda k: k, 3, 2)],
              computed=True)
with checked("R4.18b"):
    wbm.check("R4.18b", mymath.logic.sum_over(lambda k: 1 / 2**k, 1, 10), computed=True)''',
    solution=LOAD_REF + '''
print("a)", [mymath.logic.sum_over(lambda k: k * (k + 1), 1, 5), mymath.logic.sum_over(lambda k: k, 5, 4),
             mymath.logic.prod_over(lambda k: 2, 1, 10), mymath.logic.prod_over(lambda k: k, 3, 2)])
print("b)", mymath.logic.sum_over(lambda k: 1 / 2**k, 1, 10))''',
    record='''wbm.record("R4.18a", [70, 0, 1024, 1],
           mistakes={"stop est inclus : range(start, stop + 1)": [40, 0, 512, 1],
                     "un produit part de 1, pas de 0": [70, 0, 0, 0],
                     "un produit vide vaut 1, l'élément neutre de la multiplication": [70, 0, 1024, 0]})
wbm.record("R4.18b", 0.9990234375, decimals=6,
           mistakes={"stop est inclus : range(start, stop + 1)": 0.998046875})''',
    after=tests_cells("test_sum_over_ or test_prod_over_"),
    note="La somme part de 0 et le produit de 1 : ce sont les éléments neutres, et c'est aussi ce que valent une "
         "somme et un produit vides. Et $\\sum_{k=1}^{n} \\frac{1}{2^k} = 1 - \\frac{1}{2^n}$ (tu le démontreras en "
         "R5) : ici $1 - \\frac{1}{1\\,024}$.",
)

R4_22_PLOT = '''with checked("R4.22 figure"):
    ns = list(range(1, 13))
    cubes, proposed = [sum_of_cubes(n) for n in ns], [formula_b(n) for n in ns]   # before the figure
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(ns, cubes, "o-", label="1³ + 2³ + … + n³")
    ax.plot(ns, proposed, "s--", label="formule B")
    ax.set_yscale("log")
    ax.set_xlabel("n")
    ax.set_ylabel("valeur (échelle logarithmique)")
    ax.set_title("La formule B colle au début, puis décroche")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.show()'''

R4_22 = Ex(
    "R4.22", "🔬", 2, 20, "Vérifier une formule de somme de 1 à 1 000, puis la démontrer",
    "vérifier une formule sur mille cas, voir une formule fausse qui colle aux premiers cas, puis démontrer la vraie.",
    "fiche §5 et §7 ; R4.12", tracks="C",
    body="""On conjecture la **formule A** : pour tout entier $n \\ge 1$, $\\displaystyle\\sum_{k=1}^{n} k^3 = \\left(\\frac{n(n+1)}{2}\\right)^2$. Un camarade propose la **formule B** : $\\displaystyle\\sum_{k=1}^{n} k^3 = \\frac{n^2(n+1)^2}{4} + (n - 1)(n - 2)(n - 3)$.

Complète les trois fonctions (avec `//` pour les divisions, qui tombent juste : les résultats restent des entiers exacts). La vérification calcule :
- a) $\\sum_{k=1}^{1000} k^3$ ;
- b) le nombre d'entiers $n$ de 1 à 1 000 pour lesquels la formule A **diffère** de la somme ;
- c) le plus petit $n \\ge 1$ pour lequel la formule B diffère de la somme.

Puis l'expérience trace les deux courbes. Dans ta copie : démontre la formule A par récurrence (comme R4.12 : isole le dernier terme, puis factorise par $(n + 1)^2$), et explique pourquoi la formule B est juste pour $n = 1, 2, 3$.""",
    todo='''def sum_of_cubes(n):
    """1³ + 2³ + … + n³, added term by term (a loop, or sum over a range)."""
    raise NotImplementedError("add the cubes from 1 to n")


def formula_a(n):
    """(n(n + 1)/2)², computed with // so that it stays an exact integer."""
    raise NotImplementedError("write formula A")


def formula_b(n):
    """The classmate's formula: n²(n + 1)²/4 + (n − 1)(n − 2)(n − 3), with //."""
    raise NotImplementedError("write formula B")''',
    check='''with checked("R4.22a"):
    wbm.check("R4.22a", sum_of_cubes(1000), computed=True)
with checked("R4.22b"):
    wbm.check("R4.22b", sum(sum_of_cubes(n) != formula_a(n) for n in range(1, 1001)), computed=True)
with checked("R4.22c"):
    wbm.check("R4.22c", next(n for n in range(1, 1001) if sum_of_cubes(n) != formula_b(n)), computed=True)''',
    solution='''def sum_of_cubes(n):
    """1³ + 2³ + … + n³, added term by term (a loop, or sum over a range)."""
    return sum(k**3 for k in range(1, n + 1))


def formula_a(n):
    """(n(n + 1)/2)², computed with // so that it stays an exact integer."""
    return (n * (n + 1) // 2) ** 2


def formula_b(n):
    """The classmate's formula: n²(n + 1)²/4 + (n − 1)(n − 2)(n − 3), with //."""
    return n**2 * (n + 1) ** 2 // 4 + (n - 1) * (n - 2) * (n - 3)


print("a)", sum_of_cubes(1000))
print("b)", sum(sum_of_cubes(n) != formula_a(n) for n in range(1, 1001)))
print("c)", next(n for n in range(1, 1001) if sum_of_cubes(n) != formula_b(n)))''',
    record='''wbm.record("R4.22a", 250500250000,
           mistakes={"n est inclus : range(1, n + 1)": 249500250000})
wbm.record("R4.22b", 0,
           mistakes={"attention aux priorités : (n * (n + 1) // 2) ** 2, avec des parenthèses autour du produit": 1000})
wbm.record("R4.22c", 4,
           mistakes={"pour n = 1, 2 et 3, le produit (n − 1)(n − 2)(n − 3) est nul : la formule B y est juste": 1})''',
    after=[("md", "**L'expérience** : la somme et la formule B pour $n = 1$ à 12."), ("code", R4_22_PLOT)],
    note="La formule A est vraie pour tout $n$ (la récurrence le démontre) ; mille vérifications ne le démontraient "
         "pas, mais rendaient la conjecture crédible. La formule B montre le danger inverse : elle colle à la somme "
         "pour $n = 1, 2, 3$, car son terme en trop $(n - 1)(n - 2)(n - 3)$ s'annule en ces trois valeurs, puis s'en "
         "écarte.",
)

R4_24 = Ex(
    "R4.24", "🐛", 2, 20, "Chasse à l'erreur : une « démonstration » par récurrence qui prouve le faux",
    "repérer ce qui manque ou ce qui ne marche pas dans une récurrence.",
    "fiche §7 et §8 ; R4.12", tracks="C, E",
    body="""Deux « démonstrations » par récurrence prouvent des choses fausses. **Sans rien exécuter d'abord**, trouve ce qui ne va pas.

**Preuve 1.** « Pour tout entier $n \\ge 0$, $5^n + 1$ est divisible par 4. *Hérédité* : soit $n \\ge 0$ tel que $5^n + 1 = 4m$, avec $m$ entier. Alors $5^{n+1} + 1 = 5 \\times 5^n + 1 = 5(5^n + 1) - 4 = 20m - 4 = 4(5m - 1)$, divisible par 4. Donc, par récurrence, la propriété est vraie pour tout $n \\ge 0$. »

**Preuve 2.** « Dans tout groupe de $n \\ge 1$ boules, toutes les boules ont la même couleur. »

| | Ligne |
|---|---|
| A | Pour $n \\ge 1$, notons $P(n)$ : « dans tout groupe de $n$ boules, toutes ont la même couleur ». |
| B | Initialisation : un groupe d'une seule boule n'a qu'une couleur, donc $P(1)$ est vraie. |
| C | Hérédité : soit $n \\ge 1$ tel que $P(n)$ est vraie, et un groupe de $n + 1$ boules numérotées de 1 à $n + 1$. |
| D | Les boules 1 à $n$ forment un groupe de $n$ boules : d'après $P(n)$, elles ont toutes la même couleur. |
| E | Les boules 2 à $n + 1$ forment aussi un groupe de $n$ boules : elles ont toutes la même couleur. |
| F | La boule 2 appartient aux deux groupes, donc les deux groupes ont la même couleur, et les $n + 1$ boules aussi. |
| G | Par récurrence, $P(n)$ est vraie pour tout $n \\ge 1$. |

- a) Preuve 1 : quelle étape manque ? 1 pour l'initialisation, 2 pour l'hérédité.
- b) Preuve 1 : combien d'entiers $n$ de 0 à 20 rendent $5^n + 1$ divisible par 4 ?
- c) Preuve 2 : la lettre de la ligne fausse (un texte).
- d) Preuve 2 : la plus petite valeur de $n$ pour laquelle le texte ne démontre pas « $P(n) \\Rightarrow P(n + 1)$ ».
- e) Preuve 2 : $P(2)$ est-elle vraie ?

Puis, dans ta copie : pourquoi la preuve 1 ne peut-elle pas être réparée, alors que son hérédité est juste ? Et que montre la preuve 2 sur l'hérédité ?""",
    todo='''answer_R4_24a = ...  # a) 1 or 2
answer_R4_24b = ...  # b) an integer
answer_R4_24c = ...  # c) a letter, as text
answer_R4_24d = ...  # d) an integer
answer_R4_24e = ...  # e) True or False''',
    check='''for letter, answer in zip("abcde", [answer_R4_24a, answer_R4_24b, answer_R4_24c, answer_R4_24d, answer_R4_24e]):
    wbm.check(f"R4.24{letter}", answer)''',
    solution='''print("Preuve 1, 5**n + 1 pour n = 0 à 5 :", [5**n + 1 for n in range(6)])
print("divisibles par 4 de 0 à 20 :", sum((5**n + 1) % 4 == 0 for n in range(21)))
print("Preuve 2, n = 1 : les boules 1 à 1 et 2 à 2 forment les groupes", [1], "et", [2], "-> aucune boule commune")''',
    record='''wbm.record("R4.24a", 1, choices=[1, 2],
           mistakes={"l'hérédité est écrite, et son calcul est juste : refais-le": 2})
wbm.record("R4.24b", 0,
           mistakes={"teste n = 0 : 5⁰ + 1 = 2 ; puis regarde le reste de 5ⁿ dans la division par 4": 21})
wbm.record("R4.24c", "F",
           mistakes={"cette ligne est juste : cherche celle qui ne vaut pas pour toutes les valeurs de n":
                         {"A", "B", "C", "D", "E", "G"}})
wbm.record("R4.24d", 1,
           mistakes={"pour n = 2, les boules 1 à 2 et 2 à 3 partagent bien la boule 2 : essaie une valeur plus "
                     "petite": 2,
                     "l'hérédité part de n ≥ 1": 0})
wbm.record("R4.24e", False, mistakes={"deux boules peuvent avoir deux couleurs différentes": True})''',
    note="Preuve 1 : $5 \\equiv 1$ modulo 4, donc $5^n + 1$ laisse toujours le reste 2 ; aucun domino ne tombe. "
         "Preuve 2 : pour passer de 1 à 2 boules, les groupes « boules 1 à 1 » et « boules 2 à 2 » n'ont aucune boule "
         "commune, et la ligne F est fausse ; un seul domino qui ne fait pas tomber le suivant suffit à tout arrêter.",
)

R4_25_TEMPLATE = '''✍️ **Ma démonstration** (double-clique sur cette cellule pour l'écrire, puis Maj + Entrée pour l'afficher)

**Propriété.** Pour tout entier $n \\ge 1$, …

*Démonstration.* …'''

R4_25_MODEL = '''**Un modèle** (d'autres rédactions sont justes : compare la structure, pas les mots).

**Propriété.** Pour tout entier $n \\ge 1$, $\\displaystyle\\sum_{k=1}^{n} k = \\frac{n(n+1)}{2}$.

*Démonstration.* Pour tout entier $n \\ge 1$, notons $P(n)$ la propriété « $\\sum_{k=1}^{n} k = \\frac{n(n+1)}{2}$ ».

*Initialisation.* Pour $n = 1$, la somme vaut $1$ et $\\frac{1 \\times 2}{2} = 1$ : $P(1)$ est vraie.

*Hérédité.* Soit $n \\ge 1$ un entier tel que $P(n)$ est vraie. En isolant le dernier terme, puis en utilisant $P(n)$ :
$$\\sum_{k=1}^{n+1} k = \\sum_{k=1}^{n} k + (n + 1) = \\frac{n(n+1)}{2} + (n + 1) = \\frac{(n + 1)(n + 2)}{2}.$$
C'est $P(n + 1)$.

*Conclusion.* $P(1)$ est vraie et, pour tout $n \\ge 1$, $P(n) \\Rightarrow P(n + 1)$ : par récurrence, $P(n)$ est vraie pour tout entier $n \\ge 1$. $\\blacksquare$'''

R4_25 = Ex(
    "R4.25", "🛠️", 1, 20, "Rédiger une démonstration propre en LaTeX",
    "mettre au propre une démonstration, avec ses formules en LaTeX, comme dans un rapport ou un notebook partagé.",
    "fiche §8 ; R4.12 ; R0 (LaTeX)", tracks="C",
    body="""Recopie **au propre**, dans la cellule Markdown ci-dessous, ta démonstration par récurrence de R4.12 ($\\sum_{k=1}^{n} k = \\frac{n(n+1)}{2}$), en LaTeX. Elle doit contenir :
- l'énoncé de la propriété, avec son quantificateur, et la définition de $P(n)$ ;
- trois paragraphes titrés *Initialisation*, *Hérédité*, *Conclusion* ;
- dans l'hérédité, un calcul centré entre `$$`, qui fait apparaître la somme jusqu'à $n$ et l'endroit où l'hypothèse de récurrence sert ;
- un signe de fin, `$\\blacksquare$`.

Commandes utiles : `\\sum_{k=1}^{n} k`, `\\frac{n(n+1)}{2}`, `\\ge`, `\\Rightarrow`, `\\displaystyle`. Exécute la cellule pour voir le rendu, corrige ce qui s'affiche mal, puis compare avec le modèle de `05_solutions.ipynb`.""",
    after=[("todo_md", R4_25_TEMPLATE), ("solution_md", R4_25_MODEL)],
)

PART_C = Part("C", "Σ, Π et récurrence",
              "Fiche §5, §7 et §8. Σ et Π dans `mymath/logic.py`, une formule vérifiée mille fois puis démontrée, "
              "deux récurrences fausses, et une démonstration mise au propre.",
              exercises=[R4_18, R4_22, R4_24, R4_25])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | R4.1 à R4.8, R4.14 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# R4 · Logique, ensembles, Σ et Π — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/r4_logique_ensembles/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py R4`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# R4 · Logique, ensembles, Σ et Π — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : tables de vérité, implications, quantificateurs, "
               "ensembles, sommes Σ et produits Π, contre-exemples, une loss moyenne.\n"
               "- Écrire les cinq fonctions de `mymath/logic.py` et les tester.\n"
               "- Voir une propriété tenir 40 fois puis tomber, vérifier une formule mille fois puis la démontrer, "
               "chasser l'erreur dans deux récurrences.\n\n"
               "**Rappel express.** $P \\Rightarrow Q$ n'est fausse que si P est vraie et Q fausse ; elle équivaut à sa "
               "contraposée $\\text{non } Q \\Rightarrow \\text{non } P$, pas à sa réciproque. Nier : « pour tout » "
               "devient « il existe », « et » devient « ou ». $\\lvert A \\cup B \\rvert = \\lvert A \\rvert + "
               "\\lvert B \\rvert - \\lvert A \\cap B \\rvert$. $\\sum_{k=m}^{n}$ a $n - m + 1$ termes, bornes "
               "incluses : `range(m, n + 1)`. Récurrence : initialisation, hérédité, conclusion.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Dresses-tu une table de vérité, et nies-tu une phrase avec « et », « ou », « pour tout », « il "
               "existe » ?\n"
               "2. Distingues-tu implication, réciproque et contraposée, et calcules-tu unions, intersections, "
               "cardinaux, sommes Σ et produits Π ?\n"
               "3. Choisis-tu un raisonnement adapté, et sais-tu rédiger une récurrence complète ?\n\n"
               "**La suite** : R5, *Suites*. Dans workbookIA, continue le chapitre 0A au rythme de ton tableau de "
               "bord.")]


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
