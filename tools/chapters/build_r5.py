#!/usr/bin/env python
"""Build the two notebooks of chapter R5 from a single source (used by Claude).

    python tools/chapters/build_r5.py
    python tools/run_all_notebooks.py chapitres/r5_suites/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/r5_suites/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ R5.1 to R5.8, 🔗 R5.11 and R5.12); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer. A term or a sum is answered by its value, a formula
in n by an expression between quotes, a list of terms by a list, a choice among numbered sentences by its number.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "R5"
FOLDER = "chapitres/r5_suites"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("R5.1", "Calculer des termes : explicite et récurrence", [
        ("a", "an integer", "u1(5)",
         'mistakes={"u₅ est le terme de rang 5 : remplace n par 5 (le rang, pas la place dans la liste u₀, u₁, …)": '
         'u1(4), "remplace n par 5 partout, puis respecte les priorités : la puissance, puis les produits": 9}'),
        ("b", "an integer", "u1(10)", 'mistakes={"u₁₀ est le terme de rang 10 : remplace n par 10": u1(9)}'),
        ("c", "a list of 3 numbers", "by_rule(lambda v: 2 * v - 4, 3, 3)[1:]",
         'mistakes={"la liste commence à v₁ = 2 × v₀ − 4 : v₀ n\'en fait pas partie": by_rule(lambda v: 2 * v - 4, 3, 3)'
         '[:3], "2vₙ − 4 : on multiplie vₙ par 2, puis on retire 4 (pas 2 × (vₙ − 4))": '
         'by_rule(lambda v: 2 * (v - 4), 3, 3)[1:]}'),
        ("d", "an integer", "W[4]",
         'mistakes={"pour calculer w₂, on prend n = 1 dans la règle : w₂ = w₁ + 2 × 1 + 1": 22, '
         '"w₄ : trois pas depuis w₁, qui est le premier terme": {W[3], W[5]}}'),
        ("e", "an expression in n, as text", '"n**2"',
         'kind="expr", variables=("n",), mistakes={"vérifie ta formule en n = 1 : elle doit donner w₁ = 1": '
         '"(n + 1)**2", "vérifie ta formule en n = 2 : elle doit donner w₂": "(n - 1)**2", "2n + 1 est l\'écart entre deux termes, pas le terme lui-même": "2*n + 1"}'),
        ("f", "an expression in n, as text", '"2*n - 2"',
         'kind="expr", variables=("n",), mistakes={"(n + 1)² = n² + 2n + 1, pas n² + 1": "-2", '
         '"−3(n + 1) = −3n − 3 : le −3 multiplie aussi le 1": "2*n + 1", '
         '"on calcule u_{n+1} − uₙ, dans cet ordre": "2 - 2*n"}'),
        ("g", "an integer", "1",
         'mistakes={"compare u₁ et u₀ : la suite commence par diminuer": 0, '
         '"u_{n+1} ≥ uₙ est une inégalité large : un cas d\'égalité convient": 2}'),
    ]),
    Paper("R5.2", "Terme général d'une suite arithmétique", [
        ("a", "an expression in n, as text", '"7 + 4*n"',
         'kind="expr", variables=("n",), mistakes={"uₙ = u₀ + n r : le premier terme est 7, la raison 4": "4 + 7*n", '
         '"la suite commence au rang 0 : uₙ = u₀ + n r": "7 + 4*(n - 1)", '
         '"une suite arithmétique ajoute la raison : pas de puissance": "7*4**n"}'),
        ("b", "an integer", "7 + 4 * 25",
         'mistakes={"u₂₅ : on ajoute 25 fois la raison à u₀": {7 + 4 * 24, 7 + 4 * 26}}'),
        ("c", "a number", "-13.0",
         'decimals=2, mistakes={"la suite commence au rang 1 : aₙ = a₁ + (n − 1) r": {12 - 2.5 * 11, 12 - 2.5 * 12}, '
         '"la raison est négative : chaque pas retire 2,5": 12 + 2.5 * 10}'),
        ("d", "an integer", "next(n for n in range(1, 100) if 12 - 2.5 * (n - 1) < 0)",
         'fractional="un rang est un entier : le premier entier qui convient", '
         'mistakes={"aₙ = a₁ + (n − 1) r : calcule le terme de ce rang, il est encore positif ou nul": {4, 5}, '
         '"il y a un rang plus petit qui convient : calcule les termes un par un": 7}'),
        ("e", "an integer", "(2023 - 7) // 4",
         'mistakes={"la suite commence au rang 0 : résous 7 + 4n = 2 023": 505, '
         '"n est un rang : résous 7 + 4n = 2 023, puis vérifie avec u_n": {2016, 2023}}'),
        ("f", "True or False", "(2026 - 7) % 4 == 0",
         'mistakes={"résous 7 + 4n = 2 026 : n doit être un entier": True}'),
        ("g", "an integer", "int(24 / 1.5)",
         'mistakes={"compte la hauteur restante heure par heure : elle n\'est pas encore nulle": 15, '
         '"la bougie est consumée quand sa hauteur est nulle : pas une heure de plus": 17}'),
    ]),
    Paper("R5.3", "Terme général d'une suite géométrique", [
        ("a", "an expression in n, as text", '"5*3**n"',
         'kind="expr", variables=("n",), mistakes={"le premier terme multiplie, la raison est à la puissance n": '
         '"3*5**n", "5 × 3ⁿ n\'est pas (5 × 3)ⁿ : la puissance ne porte que sur la raison": "15**n", '
         '"la suite commence au rang 0 : vₙ = v₀ qⁿ": "5*3**(n - 1)", '
         '"une suite géométrique multiplie par la raison : on n\'ajoute pas": "5 + 3*n", '
         '"une suite géométrique : la raison est à la puissance n, elle ne multiplie pas n": "15*n"}'),
        ("b", "an integer", "5 * 3**4",
         'mistakes={"v₄ : quatre multiplications par 3 depuis v₀": {5 * 3**3, 5 * 3**5}, '
         '"3⁴, pas 3 × 4": 60, "5 × 3⁴ n\'est pas (5 × 3)⁴": 15**4}'),
        ("c", "an integer", "float(64 * Fraction(3, 4) ** 3)",
         'decimals=2, mistakes={"la suite commence au rang 1 : wₙ = w₁ q^(n − 1)": {64 * 0.75**4, 64 * 0.75**2}}'),
        ("d", "a fraction, as text", "64 * Fraction(3, 4) ** 6",
         'kind="fraction", mistakes={"la suite commence au rang 1 : wₙ = w₁ q^(n − 1), donc une puissance de moins que le rang": '
         '"2187/256", "w₇ = w₁ q^(7 − 1) : six multiplications par la raison": "243/16"}'),
        ("e", "an integer", "round(500 * 1.2**3, 2)",
         'decimals=2, mistakes={"chaque heure, on multiplie par 1,2 : les hausses se composent": 800, '
         '"p₃ : trois heures, trois multiplications par 1,2": {720, round(500 * 1.2**4, 1)}}'),
        ("f", "an integer", "2 * (-3) ** 5",
         'mistakes={"une puissance impaire d\'un nombre négatif est négative": 486, '
         '"t₅ : cinq multiplications par −3 depuis t₀": {2 * (-3) ** 4, 2 * (-3) ** 6}}'),
        ("g", "an integer", "next(n for n in range(50) if 500 * 1.2**n > 2000)",
         'mistakes={"calcule p₇ : la population n\'a pas encore dépassé 2 000": 7, '
         '"les hausses se composent : on multiplie par 1,2 chaque heure, on n\'ajoute pas 100": 16}'),
    ]),
    Paper("R5.4", "Sommes arithmétiques et géométriques", [
        ("a", "an integer", "len(range(5, 51, 3))",
         'mistakes={"de 5 à 50 par pas de 3 : il y a un terme de plus que d\'écarts": 15}'),
        ("b", "an integer", "float(sum(range(5, 51, 3)))",
         'decimals=2, mistakes={"compte les termes : un de plus que d\'écarts": 15 * 55 / 2, '
         '"nombre de termes × (premier + dernier), divisé par 2": 16 * 55}'),
        ("c", "a number", "sum(2 + 0.5 * k for k in range(20))",
         'decimals=2, mistakes={"de k = 0 à 19 : 20 termes": {19 * 13.5 / 2, 21 * 13.5 / 2}, '
         '"le dernier terme est celui de k = 19 : 2 + 0,5 × 19": 20 * 14 / 2}'),
        ("d", "an integer", "sum(4**k for k in range(6))",
         'mistakes={"de 4⁰ à 4⁵ : 6 termes, donc 4⁶ dans la formule": {(4**5 - 1) // 3, (4**7 - 1) // 3}, '
         '"(qⁿ − 1)/(q − 1) : n\'oublie pas de diviser par q − 1 = 3": 4**6 - 1}'),
        ("e", "an integer", "81.0 + 54 + 36 + 24 + 16",
         'decimals=2, mistakes={"compte les termes : il y en a cinq": {195, round(243 * (1 - (2 / 3) ** 6), 2)}, '
         '"la raison est le quotient d\'un terme par le précédent : 54/81": 81 * (1 - 1.5**5) / (1 - 1.5)}'),
        ("f", "an integer", "sum(2**k for k in range(3, 9))",
         'mistakes={"la somme commence à k = 3 : son premier terme est 2³": {2**9 - 1, 2**6 - 1}, '
         '"de k = 3 à 8, il y a 8 − 3 + 1 termes": {8 * 31, 8 * 127}}'),
        ("g", "an integer", "sum((-2) ** k for k in range(10))",
         'mistakes={"(−2)¹⁰ est positif : 1 − (−2)¹⁰ = 1 − 1 024": 341, '
         '"la raison est −2 : 1 − q = 1 + 2": 1023, "de k = 0 à 9 : 10 termes": 683}'),
        ("h", "an expression in n, as text", '"n**2 + 2*n"',
         'kind="expr", variables=("n",), mistakes={"de k = 0 à n − 1, la somme des k vaut (n − 1)n/2": "n**2 + 4*n", '
         '"la constante 3 est ajoutée n fois": "n**2 - n + 3", '
         '"le dernier terme est celui de k = n − 1 : 3 + 2(n − 1)": "n**2 + 3*n"}'),
    ]),
    Paper("R5.5", "Sommes infinies d'une suite géométrique", [
        ("a", "an integer", "int(1 / (1 - Fraction(3, 4)))",
         'mistakes={"la somme commence à k = 0 : son premier terme est 1": 3}'),
        ("b", "a fraction, as text", "2 / (1 - Fraction(1, 5))",
         'kind="fraction", mistakes={"la raison est le quotient de deux termes consécutifs : (2/5) ÷ 2": "10/3", '
         '"premier terme ÷ (1 − raison) : le premier terme est 2": "5/4"}'),
        ("c", "a fraction, as text", "9 / (1 + Fraction(2, 3))",
         'kind="fraction", mistakes={"la raison est négative : −6/9 = −2/3, donc 1 − q = 1 + 2/3": "27", '
         '"premier terme ÷ (1 − raison) : le premier terme est 9": "3/5"}'),
        ("d", "a fraction, as text", "Fraction(3, 10) / (1 - Fraction(3, 10))",
         'kind="fraction", mistakes={"la somme commence à k = 1 : son premier terme est 0,3, pas 1": "10/7"}'),
        ("e", "True or False", "False",
         'mistakes={"la raison 1,1 est plus grande que 1 : les termes grandissent, et les sommes partielles aussi": True}'),
        ("f", "an integer", "next(n for n in range(1, 100) if 4 - 4 * (1 - 0.75**n) < 0.1)",
         'mistakes={"pour ce nombre de termes, l\'écart à la limite est encore supérieur à 0,1": 12, '
         '"l\'écart entre la limite et la somme partielle vaut premier terme × qⁿ / (1 − q) (fiche §5)": 9, '
         '"un nombre de termes plus petit convient déjà : essaie les valeurs une par une": 14}'),
    ]),
    Paper("R5.6", "Intérêts composés et actualisation", [
        ("a", "a number", "3075",
         'mistakes={"le capital, pas seulement les intérêts de l\'année": 75}'),
        ("b", "a number (2 decimals)", "round(3000 * 1.025**10, 2)",
         'decimals=2, mistakes={"les intérêts se composent : on multiplie par 1,025 chaque année": 3750, '
         '"10 ans : dix multiplications par 1,025": {round(3000 * 1.025**9, 2), round(3000 * 1.025**11, 2)}}'),
        ("c", "a number", "3000.0 + 10 * 75",
         'decimals=2, mistakes={"à intérêts simples, les intérêts sont les mêmes chaque année : 2,5 % du capital de départ": '
         'round(3000 * 1.025**10, 2)}'),
        ("d", "an integer", "next(n for n in range(100) if 3000 * 1.025**n > 4000)",
         'mistakes={"calcule le capital au bout de ce nombre d\'années : il n\'a pas encore dépassé 4 000 €": 11, '
         '"les intérêts se composent : on multiplie par 1,025 chaque année": 14}'),
        ("e", "a number (2 decimals)", "round(5000 / 1.025**6, 2)",
         'decimals=2, mistakes={"actualiser, c\'est diviser par 1,025⁶, pas multiplier": round(5000 * 1.025**6, 2), '
         '"on divise par 1,025⁶ : on ne retire pas six fois des intérêts simples": 4250}'),
        ("f", "a number (2 decimals)", "round((1.01**12 - 1) * 100, 2)",
         'decimals=2, mistakes={"1 % par mois se compose : le coefficient annuel est 1,01¹²": 12, '
         '"la hausse en pourcentage, pas le coefficient multiplicateur : (coefficient − 1) × 100": '
         '{round(1.01**12, 4), round(1.01**12 * 100, 2)}}'),
        ("g", "True or False", "True",
         'mistakes={"1/1,025ⁿ = (1/1,025)ⁿ : une suite géométrique de raison comprise entre 0 et 1": False}'),
    ]),
    Paper("R5.7", "Une moyenne exponentielle à la main sur cinq valeurs", [
        ("a", "a list of 5 numbers (4 decimals)", "ema(X7, 0.8)",
         'decimals=4, mistakes={"0,8 multiplie l\'ancienne moyenne, 0,2 la nouvelle valeur": ema(X7, 0.2), '
         '"v₀ = 0, pas x₁ : la moyenne part de 0": ema(X7, 0.8, 10.0)}'),
        ("b", "a list of 3 numbers (2 decimals)", "window_means(X7, 3)",
         'decimals=2, mistakes={"5 valeurs et une fenêtre de 3 : 5 − 3 + 1 moyennes": window_means(X7, 3)[:2], '
         '"une moyenne : divise chaque somme par 3": [3 * m for m in window_means(X7, 3)]}'),
        ("c", "a number", "sum(X7) // 5", 'mistakes={"une moyenne : divise la somme par 5": sum(X7)}'),
        ("d", "True or False", "ema(X7, 0.8)[-1] < sum(X7) / 5",
         'mistakes={"compare v₅ à la moyenne de c)": False}'),
        ("e", "a number", "0.8**2 * 0.2",
         'decimals=4, mistakes={"x₁ n\'a le poids 0,2 que dans v₁ : chaque pas en arrière multiplie le poids par 0,8": '
         '0.2, "deux pas séparent x₁ de x₃ : le poids est multiplié deux fois par 0,8": 0.16, '
         '"le poids de x₁ contient aussi le facteur 0,2 avec lequel elle est entrée": 0.64}'),
        ("f", "a number", "X7[-1]",
         'mistakes={"avec ces coefficients, v_t ne garde rien du passé : v_t = x_t": {15, 5, 0}}'),
    ]),
    Paper("R5.8", "Retrouver le premier terme et la raison à partir de deux termes", [
        ("a", "an integer", "(41 - 17) / (10 - 4)",
         'decimals=2, mistakes={"u₁₀ − u₄ = 6 r : divise par le nombre de pas": 24, '
         '"entre le rang 4 et le rang 10, on ajoute 6 fois la raison, pas 10": 2.4}'),
        ("b", "an integer", "17 - 4 * 4",
         'mistakes={"de u₄ à u₀, on retire 4 fois la raison": {13, 17 - 3 * 4, 17 + 4 * 4}}'),
        ("c", "an integer", "-2",
         'mistakes={"v₄ / v₁ = q³ est négatif : la raison aussi": 2, "v₄ / v₁ = q³ : la raison est sa racine cubique": '
         '-8}'),
        ("d", "an integer", "12 // -2",
         'mistakes={"v₀ = v₁ ÷ q, et q est négatif": 6, "v₀ = v₁ ÷ q, pas v₁ × q": -24}'),
        ("e", "a number", "0.8",
         'decimals=2, mistakes={"w₃ / w₁ = q² : prends la racine carrée": 0.64, "les termes sont positifs : la raison aussi": -0.8}'),
        ("f", "a number", "50 / 0.8", 'decimals=2, mistakes={"w₀ = w₁ ÷ q, pas w₁ × q": 40}'),
        ("g", "a list (6 decimals)", "[-2 / 3, 2 / 3]",
         'decimals=6, ordered=False, mistakes={"q² = 4/9 a deux solutions, opposées": [2 / 3], '
         '"q² = 4/9 : prends les racines carrées": [-4 / 9, 4 / 9], "q² = 4/9 : la raison est une racine carrée '
         'de 4/9": [4 / 9]}'),
    ]),
    Paper("R5.11", "Actualiser : ce que vaut aujourd'hui une somme versée chaque année", [
        ("a", "a number (2 decimals)", "round(1000 / 1.04, 2)",
         'decimals=2, mistakes={"actualiser, c\'est diviser par 1,04 : la valeur actuelle est plus petite": 1040, '
         '"on divise par 1,04 : retirer 4 % ne donne pas la même chose": 960}'),
        ("b", "a number (4 decimals)", "round(1 / 1.04, 4)",
         'decimals=4, mistakes={"chaque année de plus divise la valeur actuelle par 1,04 : la raison est 1/1,04": 1.04, '
         '"1/1,04 n\'est pas 1 − 0,04": 0.96}'),
        ("c", "a number (2 decimals)", "round(present_value(1000, 0.04, 8), 2)",
         'decimals=2, mistakes={"chaque versement vaut moins aujourd\'hui : actualise-les": 8000, '
         '"le premier versement arrive dans un an : il est déjà actualisé une fois": '
         'round(present_value(1000, 0.04, 8, first=0), 2), '
         '"on cherche la valeur aujourd\'hui : on divise par les puissances de 1,04, on ne multiplie pas": '
         'round(sum(1000 * 1.04**k for k in range(8)), 2), '
         '"il y a 8 versements, de l\'année 1 à l\'année 8": {round(present_value(1000, 0.04, 7), 2), '
         'round(present_value(1000, 0.04, 9), 2)}}'),
        ("d", "1 or 2", "1", 'choices=[1, 2], mistakes={"compare 7 000 € à la valeur actuelle de c)": 2}'),
        ("e", "a number (2 decimals)", "round(present_value(1000, 0.06, 8), 2)",
         'decimals=2, mistakes={"le taux a changé : actualise avec 1,06": round(present_value(1000, 0.04, 8), 2)}'),
    ]),
    Paper("R5.12", "Une moyenne mobile qui glisse : la mettre à jour sans tout recalculer", [
        ("a", "a number", "window_means(X12, 4)[0]",
         'decimals=2, mistakes={"une moyenne : divise la somme des 4 valeurs par 4": sum(X12[:4])}'),
        ("b", "a number", "window_means(X12, 4)[1]",
         'decimals=2, mistakes={"m₅ est la moyenne de x₂ à x₅": window_means(X12, 4)[0]}'),
        ("c", "a number (1 to 4)", "1",
         'choices=[1, 2, 3, 4], mistakes={"la valeur qui sort de la fenêtre est la plus ancienne, pas la dernière": 2, '
         '"la nouvelle moyenne corrige l\'ancienne : elle ne la remplace pas": 3, '
         '"la fenêtre de mₜ va de x_{t−3} à xₜ : c\'est x_{t−3} qui en sort": 4}'),
        ("d", "a number", "window_means(X12, 4)[1] + (X12[5] - X12[1]) / 4",
         'decimals=2, mistakes={"la valeur qui sort de la fenêtre de m₅ pour former m₆ est x₂, la plus ancienne": '
         '{window_means(X12, 4)[1] + (X12[5] - X12[4]) / 4, window_means(X12, 4)[1] + (X12[5] - X12[2]) / 4, '
         'window_means(X12, 4)[1] + (X12[5] - X12[0]) / 4}, '
         '"la différence des deux valeurs est divisée par 4": window_means(X12, 4)[1] + (X12[5] - X12[1])}'),
        ("e", "a list of 2 integers", "[99, 2]",
         'mistakes={"additionner 100 nombres demande 99 additions": [100, 2], '
         '"la mise à jour fait une soustraction et une addition (la division ne compte pas ici)": [99, 3], '
         '"la mise à jour fait une soustraction, puis une addition à l\'ancienne moyenne": [99, 1], '
         '"dans l\'ordre [direct, mise à jour]": [2, 99]}'),
        ("f", "a number", "window_means(X12, 4)[-1]",
         'decimals=2, mistakes={"m₈ est la moyenne de x₅ à x₈ : la dernière fenêtre": window_means(X12, 4)[-2]}'),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
from fractions import Fraction


def u1(n):                                                    # R5.1
    return n * n - 3 * n + 1


def by_rule(rule, first, steps):
    """[first, rule(first), …]: steps + 1 terms of a sequence defined by recursion."""
    terms = [first]
    for _ in range(steps):
        terms.append(rule(terms[-1]))
    return terms


W = {1: 1}                                                    # w₁ = 1, w_{n+1} = w_n + 2n + 1
for n in range(1, 6):
    W[n + 1] = W[n] + 2 * n + 1


def ema(values, beta, v=0.0):                                 # R5.7
    averages = []
    for x in values:
        v = beta * v + (1 - beta) * x
        averages.append(round(v, 10))
    return averages


def window_means(values, k):                                  # R5.7, R5.12
    return [sum(values[i:i + k]) / k for i in range(len(values) - k + 1)]


def present_value(payment, rate, years, first=1):             # R5.11: payments at the end of years first, first + 1…
    return sum(payment / (1 + rate) ** k for k in range(first, first + years))


X7 = [10, 20, 15, 5, 25]
X12 = [12, 18, 15, 9, 21, 24, 6, 15]'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ R5.1 à R5.8, 🔗 R5.11 et R5.12)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un nombre avec un point décimal, `-1.5`, arrondi comme le demande la question ;\n"
               "- une fraction exacte entre guillemets, `\"5/7\"` ;\n"
               "- une expression en `n` entre guillemets, `\"3*n**2 + 1\"` (`*` pour multiplier, `**` pour la "
               "puissance) ;\n"
               "- une liste de nombres entre crochets, dans l'ordre demandé ;\n"
               "- vrai ou faux par `True` ou `False` ; un numéro de réponse proposée par un entier.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (R5.14 to R5.16)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math
import time

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

LOAD_LEARNER = 'mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="R5")  # reload your saved file'
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme dans les chapitres précédents). Ouvre ta copie "
         "`mon_travail/mymath/sequences.py`, lis la docstring de la fonction en entier, remplace la ligne "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Les tests comparent tes résultats à des calculs exacts "
         "(`fractions`, SymPy), à NumPy et à SciPy.")

WRONG_ERROR = "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)"
OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "TypeError", "ZeroDivisionError"]


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of sequences.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_r5_sequences.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_r5_sequences.py", "{keyword}", impl="ref")')]


R5_14 = Ex(
    "R5.14", "🔨", 1, 15, "Terme d'une suite arithmétique et somme géométrique · `arithmetic_term`, `geometric_sum`",
    "programmer le terme général d'une suite arithmétique et la somme d'une suite géométrique, sans boucle.",
    "fiche §2 et §4", tracks="C, E", mymath="sequences.py",
    body=HOWTO + """

Dans `mon_travail/mymath/sequences.py` :
- `arithmetic_term(u0, r, n)` : le terme de rang `n` de la suite arithmétique de premier terme `u0` et de raison `r` (le rang 0 est `u0`), avec la formule explicite, sans boucle ;
- `geometric_sum(u0, q, n)` : la somme des `n` premiers termes `u0 + u0*q + … + u0*q**(n - 1)`, avec la formule de la fiche §4, sans boucle ; **`n` est le nombre de termes** (la somme de 0 terme vaut 0) ; pense au cas `q == 1`, où la formule divise par zéro.

La vérification calcule deux termes ($u_0 = -4$, $r = 7$, rang 12 ; $u_0 = 2{,}5$, $r = -0{,}5$, rang 9), la somme de 6 termes de premier terme 3 et de raison 1,5, deux cas particuliers ($q = 1$ ; $n = 0$), puis une somme de 40 termes de raison $\\frac{1}{4}$.""",
    todo=LOAD_LEARNER,
    check='''with checked("R5.14a"):
    wbm.check("R5.14a", [mymath.sequences.arithmetic_term(-4, 7, 12), mymath.sequences.arithmetic_term(2.5, -0.5, 9)],
              computed=True)
with checked("R5.14b"):
    wbm.check("R5.14b", mymath.sequences.geometric_sum(3, 1.5, 6), computed=True)
with checked("R5.14c"):
    wbm.check("R5.14c", [mymath.sequences.geometric_sum(5, 1, 7), mymath.sequences.geometric_sum(8, 3, 0)],
              computed=True)
with checked("R5.14d"):
    wbm.check("R5.14d", mymath.sequences.geometric_sum(6, 0.25, 40), computed=True)''',
    solution=LOAD_REF + '''
print("a)", [mymath.sequences.arithmetic_term(-4, 7, 12), mymath.sequences.arithmetic_term(2.5, -0.5, 9)])
print("b)", mymath.sequences.geometric_sum(3, 1.5, 6))
print("c)", [mymath.sequences.geometric_sum(5, 1, 7), mymath.sequences.geometric_sum(8, 3, 0)])
print("d)", mymath.sequences.geometric_sum(6, 0.25, 40), "à comparer à 6 / (1 - 0.25) =", 6 / (1 - 0.25))''',
    record='''wbm.record("R5.14a", [80, -2.0], decimals=4,
           mistakes={"le rang 0 est u0 : u(n) = u0 + n × r, pas (n − 1) × r": [73, -1.5],
                     "le rang 0 est u0 : u(n) = u0 + n × r, pas (n + 1) × r": [87, -2.5]})
wbm.record("R5.14b", 62.34375, decimals=5,
           mistakes={"n est le nombre de termes : la formule contient q**n (le dernier terme est u0*q**(n - 1))":
                         {96.515625, 39.5625}})
wbm.record("R5.14c", [35.0, 0], decimals=4,
           mistakes={"une somme de 0 terme vaut 0": [35.0, 8.0],
                     "q = 1 : chacun des n termes vaut u0, la somme vaut n × u0": [7, 0],
                     "q = 1 : il y a n termes égaux à u0, pas un seul": [5, 0]})
wbm.record("R5.14d", 8.0, decimals=4)''',
    after=tests_cells("test_arithmetic_term_ or test_geometric_sum_"),
    note="Avec 40 termes de raison $\\frac{1}{4}$, la somme vaut $6 \\times \\frac{1 - 0{,}25^{40}}{0{,}75}$, et "
         "$0{,}25^{40} \\approx 10^{-24}$ : on lit déjà la somme infinie $\\frac{6}{1 - 0{,}25} = 8$ (fiche §5). La "
         "formule fait le même nombre d'opérations pour 40 termes que pour 40 millions : R5.22 mesure ce que cela "
         "change.",
)

R5_15 = Ex(
    "R5.15", "🔨", 1, 15, "Itérer une récurrence · `iterate`",
    "programmer le calcul des premiers termes d'une suite définie par récurrence, pour n'importe quelle règle.",
    "fiche §1 ; workbookIA 0A (`lambda`, fonctions passées en argument)", tracks="C, E", mymath="sequences.py",
    body="""Écris `iterate(f, u0, n)` dans `mon_travail/mymath/sequences.py` : la liste `[u(0), u(1), …, u(n)]` des termes de la suite définie par `u(0) = u0` et `u(k + 1) = f(u(k))`. **`n` est le dernier rang calculé** : la liste a `n + 1` termes. `f` est une fonction, souvent une `lambda` : `iterate(lambda u: 3 * u - 1, 2, 3)` calcule les termes de rang 0 à 3 de $u_{k+1} = 3u_k - 1$ partie de 2.

La vérification calcule :
- a) les termes de rang 0 à 4 de $u_{k+1} = 10 - \\frac{u_k}{2}$, partie de 0 ;
- b) le nombre de termes de `iterate(abs, -3, 10)` ;
- c) `iterate(abs, -3, 0)` ;
- d) le terme de rang 10 de $u_{k+1} = 1 + \\frac{1}{u_k}$, partie de 1.

Puis, dans ta copie : si la suite de d) converge vers une limite $\\ell$, quelle équation $\\ell$ vérifie-t-elle (fiche §5) ? Résous-la (R3, second degré) et compare à d).""",
    todo=LOAD_LEARNER,
    check='''with checked("R5.15"):
    iterate = mymath.sequences.iterate
    wbm.check("R5.15a", iterate(lambda u: 10 - u / 2, 0, 4), computed=True)
    wbm.check("R5.15b", len(iterate(abs, -3, 10)), computed=True)
    wbm.check("R5.15c", iterate(abs, -3, 0), computed=True)
    wbm.check("R5.15d", iterate(lambda u: 1 + 1 / u, 1, 10)[-1], computed=True)''',
    solution=LOAD_REF + '''
iterate = mymath.sequences.iterate
print("a)", iterate(lambda u: 10 - u / 2, 0, 4))
print("b)", len(iterate(abs, -3, 10)), " c)", iterate(abs, -3, 0))
print("d)", iterate(lambda u: 1 + 1 / u, 1, 10)[-1], "et (1 + √5) / 2 =", (1 + math.sqrt(5)) / 2)''',
    record='''wbm.record("R5.15a", [0, 10.0, 5.0, 7.5, 6.25], decimals=4,
           mistakes={"la liste commence par u0 lui-même": [10.0, 5.0, 7.5, 6.25],
                     "n est le dernier rang : n + 1 termes, de u(0) à u(n)": [0, 10.0, 5.0, 7.5, 6.25, 6.875]})
wbm.record("R5.15b", 11, mistakes={"n + 1 termes, du rang 0 au rang n": {10, 12}})
wbm.record("R5.15c", [-3],
           mistakes={"n = 0 : la liste contient le seul terme u0": [],
                     "u0 entre tel quel dans la liste : f ne sert qu'à calculer les termes suivants": [3]})
wbm.record("R5.15d", 89 / 55, decimals=4,
           mistakes={"le terme de rang 10 : f est appliquée 10 fois à partir de u0": {55 / 34, 144 / 89}})''',
    after=tests_cells("test_iterate_"),
    note="Les termes de d) sont des quotients de nombres de Fibonacci consécutifs ($\\frac{89}{55}$ au rang 10). La "
         "limite vérifie $\\ell = 1 + \\frac{1}{\\ell}$, soit $\\ell^2 - \\ell - 1 = 0$ : sa solution positive est "
         "le **nombre d'or** $\\frac{1 + \\sqrt{5}}{2} \\approx 1{,}618$. Ici la règle n'est pas affine, mais l'idée "
         "du point fixe marche encore.",
)

R5_16 = Ex(
    "R5.16", "🔨", 2, 25, "Moyennes mobile et exponentielle · `moving_average`, `exponential_moving_average`",
    "programmer les deux lissages de la fiche, avec leurs cas limites et leurs erreurs.",
    "fiche §6 ; R5.7 et R5.12", tracks="C, E", mymath="sequences.py",
    body="""Dans `mon_travail/mymath/sequences.py` :
- `moving_average(values, window)` : la liste des `len(values) - window + 1` moyennes de `window` valeurs consécutives (la moyenne de `values[0:window]`, puis de `values[1:window + 1]`, etc.) ; une `ValueError` si `window` n'est pas compris entre 1 et `len(values)` ;
- `exponential_moving_average(values, beta)` : la liste `[v(1), …, v(T)]` de la moyenne exponentielle $v_0 = 0$, $v_t = \\beta\\,v_{t-1} + (1 - \\beta)\\,x_t$ ; une `ValueError` si `beta` n'est pas dans $[0 \\;;\\; 1[$.

La vérification calcule :
- a) les moyennes mobiles sur 3 valeurs de `[4, 8, 6, 10, 2, 12]` ;
- b) le nombre de moyennes mobiles sur 7 valeurs d'une liste de 50 valeurs ;
- c) le nom de l'erreur levée pour une fenêtre de 3 sur 2 valeurs (avec `raised`, de la cellule des outils), puis d) pour une fenêtre de 0 ;
- e) la moyenne exponentielle de `[40, 0, 20, 20]` avec $\\beta = 0{,}75$ ;
- f) la moyenne exponentielle de `[3, 1, 4]` avec $\\beta = 0$ ;
- g) le nom de l'erreur levée pour $\\beta = 1$.""",
    todo=LOAD_LEARNER,
    check='''with checked("R5.16a"):
    wbm.check("R5.16a", mymath.sequences.moving_average([4, 8, 6, 10, 2, 12], 3), computed=True)
with checked("R5.16b"):
    wbm.check("R5.16b", len(mymath.sequences.moving_average(list(range(50)), 7)), computed=True)
with checked("R5.16c"):
    wbm.check("R5.16c", raised(mymath.sequences.moving_average, [1, 2], 3), computed=True)
with checked("R5.16d"):
    wbm.check("R5.16d", raised(mymath.sequences.moving_average, [1, 2], 0), computed=True)
with checked("R5.16e"):
    wbm.check("R5.16e", mymath.sequences.exponential_moving_average([40, 0, 20, 20], 0.75), computed=True)
with checked("R5.16f"):
    wbm.check("R5.16f", mymath.sequences.exponential_moving_average([3, 1, 4], 0), computed=True)
with checked("R5.16g"):
    wbm.check("R5.16g", raised(mymath.sequences.exponential_moving_average, [1], 1), computed=True)''',
    solution=LOAD_REF + '''
seq = mymath.sequences
print("a)", seq.moving_average([4, 8, 6, 10, 2, 12], 3), " b)", len(seq.moving_average(list(range(50)), 7)))
print("c)", raised(seq.moving_average, [1, 2], 3), " d)", raised(seq.moving_average, [1, 2], 0))
print("e)", seq.exponential_moving_average([40, 0, 20, 20], 0.75))
print("f)", seq.exponential_moving_average([3, 1, 4], 0), " g)", raised(seq.exponential_moving_average, [1], 1))''',
    record=f'''wbm.record("R5.16a", [6.0, 8.0, 6.0, 8.0], decimals=4,
           mistakes={{"len(values) − window + 1 moyennes : la dernière fenêtre se termine sur la dernière valeur":
                         [6.0, 8.0, 6.0],
                     "une moyenne : divise chaque somme par window": [18, 24, 18, 24]}})
wbm.record("R5.16b", 44, mistakes={{"len(values) − window + 1 moyennes": {{43, 45, 50}}}})
wbm.record("R5.16c", "ValueError",
           mistakes={{"une fenêtre plus longue que la liste doit lever une ValueError (raise), pas rendre une liste":
                         "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("R5.16d", "ValueError",
           mistakes={{"une fenêtre de 0 doit lever une ValueError (raise), pas rendre une liste": "aucune",
                     "teste la fenêtre avant de calculer : une fenêtre de 0 doit lever une ValueError, pas une "
                     "division par zéro": "ZeroDivisionError",
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("R5.16e", [10.0, 7.5, 10.625, 12.96875], decimals=5,
           mistakes={{"beta multiplie l'ancienne moyenne, 1 − beta la nouvelle valeur": [30.0, 7.5, 16.875, 19.21875],
                     "v(0) = 0 : la moyenne part de 0, pas de la première valeur": [40.0, 30.0, 27.5, 25.625]}})
wbm.record("R5.16f", [3.0, 1.0, 4.0], decimals=4)
wbm.record("R5.16g", "ValueError",
           mistakes={{"beta = 1 est exclu (la moyenne ne bougerait plus) : lève une ValueError": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})''',
    after=tests_cells("test_moving_average_ or test_exponential_moving_average_"),
    note="La moyenne mobile a besoin de toute sa fenêtre ; la moyenne exponentielle, de sa seule dernière valeur. "
         "Avec $\\beta = 0{,}75$, la moyenne de d) part de 10 alors que la série commence à 40 : c'est le démarrage "
         "trop bas de la fiche §6.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: NumPy, prediction, experiments (R5.17 to R5.20)
# ---------------------------------------------------------------------------
R5_17 = Ex(
    "R5.17", "📦", 1, 15, "Les mêmes calculs avec NumPy : `np.cumsum`, `np.cumprod`, `np.convolve`",
    "calculer des sommes partielles, des produits cumulés et des moyennes mobiles en une ligne avec NumPy.",
    "fiche §4 et §6 ; workbookIA 0A §100.8.1 à §100.8.5 (arrays, calcul vectorisé, réductions)", tracks="C",
    body="""Trois fonctions de NumPy font en une ligne ce que tu as programmé avec des boucles :
- `np.cumsum(a)` rend les **sommes partielles** de `a` : `np.cumsum([2, 7, 1])` vaut `[2, 9, 10]` ;
- `np.cumprod(a)` rend les **produits cumulés** : `np.cumprod([2, 7, 1])` vaut `[2, 14, 14]` ;
- `np.convolve(a, w, mode="valid")` fait glisser la liste de poids `w` le long de `a` et rend, à chaque position où `w` tient en entier, la somme des produits : avec `w = np.ones(k) / k`, c'est la moyenne mobile sur `k` valeurs.

Et `3 + 2 * np.arange(5)` calcule d'un coup les termes $3 + 2k$ pour $k = 0$ à 4 (calcul vectorisé, 0A §100.8.3). Calcule, chacun **en une ligne** :
- a) les 10 premières sommes partielles de la suite arithmétique $u_k = 4 + 3k$ (de $u_0$ à $u_9$) ;
- b) les 6 premières sommes partielles de la suite géométrique $5 \\times 1{,}2^k$ ;
- c) le capital à la fin de chacune des quatre années d'un placement de 1 000 €, dont le taux change chaque année : +2 %, +5 %, −3 %, +4 % (les taux sont dans `rates`) ;
- d) la moyenne mobile sur 2 valeurs de `x`.

Puis, dans ta copie : pourquoi la suite des capitaux de c) n'est-elle pas géométrique ?""",
    todo='''rates = np.array([0.02, 0.05, -0.03, 0.04])
x = np.array([5, 7, 3, 9, 11, 1, 8])

answer_R5_17a = ...  # a) an array of 10 partial sums
answer_R5_17b = ...  # b) an array of 6 partial sums
answer_R5_17c = ...  # c) an array of 4 capitals
answer_R5_17d = ...  # d) an array of moving averages''',
    check='''for letter, answer in zip("abcd", [answer_R5_17a, answer_R5_17b, answer_R5_17c, answer_R5_17d]):
    wbm.check(f"R5.17{letter}", answer)''',
    solution='''rates = np.array([0.02, 0.05, -0.03, 0.04])
x = np.array([5, 7, 3, 9, 11, 1, 8])

answer_R5_17a = np.cumsum(4 + 3 * np.arange(10))
answer_R5_17b = np.cumsum(5 * 1.2 ** np.arange(6))
answer_R5_17c = 1000 * np.cumprod(1 + rates)
answer_R5_17d = np.convolve(x, np.ones(2) / 2, mode="valid")
print(answer_R5_17a, answer_R5_17b.round(4), answer_R5_17c.round(2), answer_R5_17d, sep="\\n")''',
    record='''wbm.record("R5.17a", [4, 11, 21, 34, 50, 69, 91, 116, 144, 175],
           mistakes={"chaque terme contient 4 : cumule les termes 4 + 3k eux-mêmes":
                         [4, 7, 13, 22, 34, 49, 67, 88, 112, 139],
                     "k commence à 0 : np.arange(10)": [7, 17, 30, 46, 65, 87, 112, 140, 171, 205],
                     "les sommes partielles, pas les termes : np.cumsum": [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]})
wbm.record("R5.17b", [5.0, 11.0, 18.2, 26.84, 37.208, 49.6496], decimals=4,
           mistakes={"les sommes partielles, pas les termes : np.cumsum": [5.0, 6.0, 7.2, 8.64, 10.368, 12.4416],
                     "k commence à 0 : le premier terme est 5": [6.0, 13.2, 21.84, 32.208, 44.6496, 59.57952]})
wbm.record("R5.17c", [1020.0, 1071.0, 1038.87, 1080.4248], decimals=2,
           mistakes={"les évolutions se composent : le produit des coefficients 1 + taux, avec np.cumprod":
                         [1020.0, 1070.0, 1040.0, 1080.0],
                     "on multiplie par le coefficient 1 + taux, pas par le taux": [20.0, 1.0, -0.03, -0.0012]})
wbm.record("R5.17d", [6.0, 5.0, 6.0, 10.0, 6.0, 4.5], decimals=4,
           mistakes={"mode=\\"valid\\" ne garde que les positions où la fenêtre tient en entier":
                         [2.5, 6.0, 5.0, 6.0, 10.0, 6.0, 4.5, 4.0],
                     "mode=\\"valid\\" : la fenêtre doit tenir en entier, même au début": [2.5, 6.0, 5.0, 6.0, 10.0, 6.0, 4.5],
                     "les poids d'une moyenne sur 2 valeurs valent 1/2 : np.ones(2) / 2": [12, 10, 12, 20, 12, 9]})''',
    note="La suite de c) multiplie par un nombre différent chaque année : ce n'est pas une suite géométrique, mais "
         "le produit cumulé fait le même travail. Et $1{,}02 \\times 1{,}05 \\times 0{,}97 \\times 1{,}04 \\approx "
         "1{,}080$ : quatre ans à ces taux rapportent autant que quatre ans à environ 1,95 % par an (tu sauras le "
         "calculer avec une racine quatrième).",
)

R5_18_EXPERIMENT = '''def run(u0, steps=40):
    terms = [u0]
    for _ in range(steps):
        terms.append(0.75 * terms[-1] + 2)
    return terms


from_0, from_100 = run(0), run(100)
print("depuis 0   :", [round(u, 3) for u in from_0[:6]], "…", round(from_0[-1], 6))
print("depuis 100 :", [round(u, 3) for u in from_100[:6]], "…", round(from_100[-1], 6))
print("premier rang où |u_n - 8| < 0,01, depuis 0 :", next(n for n, u in enumerate(from_0) if abs(u - 8) < 0.01))
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.plot(from_0, "o-", markersize=3, label="u₀ = 0")
ax.plot(from_100, "o-", markersize=3, label="u₀ = 100")
ax.axhline(8, color="gray", linestyle=":", label="y = 8")
ax.set_xlabel("n")
ax.set_ylabel("uₙ")
ax.set_title("u(n + 1) = 0,75 u(n) + 2, depuis deux premiers termes")
ax.grid(True, alpha=0.3)
ax.legend()
plt.show()'''

R5_18 = Ex(
    "R5.18", "🔮", 1, 10, "Prédire : vers quoi tend u(n + 1) = 0,75 u(n) + 2 ?",
    "prédire le comportement d'une récurrence affine avec le point fixe et l'écart géométrique, puis le confronter "
    "à l'expérience.",
    "fiche §1 et §5", tracks="C, E", hypothesis=True,
    body="""On étudie la suite définie par $u_{n+1} = 0{,}75\\,u_n + 2$, avec deux premiers termes possibles : $u_0 = 0$ ou $u_0 = 100$. **Avant d'exécuter quoi que ce soit**, prédis avec la fiche §5, sans calculer de termes :
- a) la limite de la suite partie de $u_0 = 0$ ;
- b) la limite de la suite partie de $u_0 = 100$ ;
- c) partie de $u_0 = 0$, combien de pas faut-il pour que $u_n$ soit à moins de 0,01 de sa limite ? 1 : moins de 10 ; 2 : entre 10 et 50 ; 3 : plus de 50.

Écris tes trois prédictions, vérifie-les, puis lance l'expérience.""",
    todo='''prediction_R5_18a = ...  # a) a number, written BEFORE running the experiment below
prediction_R5_18b = ...  # b) a number
prediction_R5_18c = ...  # c) 1, 2 or 3''',
    check='''for letter, prediction in zip("abc", [prediction_R5_18a, prediction_R5_18b, prediction_R5_18c]):
    wbm.check(f"R5.18{letter}", prediction)''',
    record='''wbm.record("R5.18a", 8.0, decimals=2, prediction=True,
           mistakes={"la limite d'une récurrence affine qui converge est son point fixe, la solution de ℓ = 0,75 ℓ + 2":
                         {0, 2, 0.75}})
wbm.record("R5.18b", 8.0, decimals=2, prediction=True,
           mistakes={"l'écart au point fixe est multiplié par 0,75 à chaque pas, quel que soit le premier terme : la "
                     "limite ne dépend pas de u₀": {100, 0, 2}})
wbm.record("R5.18c", 2, prediction=True, choices=[1, 2, 3],
           mistakes={"l'écart est multiplié par 0,75 à chaque pas : le diviser par 800 demande plus de 10 pas": 1,
                     "0,75ⁿ diminue plus vite qu'on ne le croit : 0,75⁵⁰ est de l'ordre de 10⁻⁶": 3})''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes trois prédictions écrites."),
        ("todo", guarded(R5_18_EXPERIMENT, ["prediction_R5_18a", "prediction_R5_18b", "prediction_R5_18c"],
                         "⏳ Écris d'abord tes trois prédictions, puis exécute à nouveau.")),
        ("solution", R5_18_EXPERIMENT),
        ("md", "**Après l'expérience.** d) Le premier rang $n$ pour lequel $\\lvert u_n - 8 \\rvert < 0{,}01$, "
               "partie de $u_0 = 0$ (lis-le dans la sortie). Puis, dans ta copie : écris $u_n$ en fonction de $n$ "
               "pour $u_0 = 0$ (fiche §5), et explique pourquoi les deux courbes se rejoignent."),
        ("todo", "answer_R5_18d = ...  # d) an integer"),
        ("check", 'wbm.check("R5.18d", answer_R5_18d)'),
        ("solution", "answer_R5_18d = next(n for n, u in enumerate(run(0)) if abs(u - 8) < 0.01)\nprint(answer_R5_18d)"),
        ("record", 'wbm.record("R5.18d", 24, mistakes={"le premier rang où l\'écart passe sous 0,01 : lis la ligne '
                   '« premier rang » de la sortie": {23, 25}})'),
    ],
    note="Le point fixe vérifie $\\ell = 0{,}75\\,\\ell + 2$, soit $\\ell = 8$, et $u_n = 8 + (u_0 - 8) \\times "
         "0{,}75^n$ : depuis 0, $u_n = 8 - 8 \\times 0{,}75^n$ ; depuis 100, $u_n = 8 + 92 \\times 0{,}75^n$. "
         "L'écart à 8 passe sous 0,01 quand $8 \\times 0{,}75^n < 0{,}01$ : 24 pas. Les logarithmes (R6) donneront "
         "ce rang sans essais.",
)

R5_19_GIVEN = '''from scipy.signal import lfilter

rng = np.random.default_rng(2026)
t = np.arange(300)
trend = 10 + 4 * np.sin(2 * np.pi * t / 120)           # the true signal, unknown in practice
x = trend + rng.normal(0, 1.5, size=t.size)             # what we measure: the signal plus noise


def moving(x, k):
    """Moving average over k values, aligned on time: entry t is the mean of x[t-k+1..t] (NaN for t < k - 1)."""
    out = np.full(len(x), np.nan)
    out[k - 1:] = np.convolve(x, np.ones(k) / k, mode="valid")
    return out


def ema(x, beta):
    """Exponential moving average v(t) = beta v(t-1) + (1 - beta) x(t), v(0) = 0 (one line of SciPy)."""
    return lfilter([1 - beta], [1, -beta], x)


def error(smoothed, start=60):
    """Root mean square gap between a smoothed curve and the true trend, from time `start` on."""
    return float(np.sqrt(np.mean((smoothed[start:] - trend[start:]) ** 2)))


windows = [1, 3, 9, 25, 61]
betas = [0, 0.5, 0.75, 0.9, 0.99]'''

R5_19_PLOT = '''with checked("R5.19 figure"):
    if window_errors is ... or beta_errors is ...:
        print("⏳ Calcule d'abord window_errors et beta_errors.")
    else:
        fig, axes = plt.subplots(1, 3, figsize=(15, 3.8))
        axes[0].plot(windows, window_errors, "o-")
        axes[0].set_xlabel("fenêtre k")
        axes[0].set_title("Erreur de la moyenne mobile")
        axes[1].plot(betas, beta_errors, "o-", color="C1")
        axes[1].set_xlabel("β")
        axes[1].set_title("Erreur de la moyenne exponentielle")
        axes[2].plot(t, x, ".", color="gray", markersize=2, label="mesures")
        axes[2].plot(t, trend, color="black", linewidth=1, label="vraie tendance")
        axes[2].plot(t, moving(x, 9), color="C0", label="fenêtre 9")
        axes[2].plot(t, moving(x, 61), color="C3", label="fenêtre 61")
        axes[2].set_xlabel("t")
        axes[2].set_title("Deux fenêtres")
        axes[2].legend(fontsize=8)
        for ax in axes[:2]:
            ax.set_ylabel("erreur")
            ax.grid(True, alpha=0.3)
        fig.tight_layout()
        plt.show()'''

R5_19 = Ex(
    "R5.19", "🔬", 2, 20, "Lisser un signal bruité : l'effet de la fenêtre et de β",
    "mesurer le compromis d'un lissage : trop peu, il reste du bruit ; trop, la courbe est en retard.",
    "fiche §6 ; R5.16, R5.17", tracks="C",
    body="""La cellule ci-dessous fabrique un signal : une **vraie tendance** (une sinusoïde, qu'on ne connaît pas en pratique) à laquelle s'ajoute du **bruit**. Elle donne trois outils : `moving(x, k)` (la moyenne mobile, alignée sur le temps : sa valeur à l'instant $t$ utilise $x_{t-k+1}, \\dots, x_t$), `ema(x, beta)` (la moyenne exponentielle) et `error(smoothed)`, l'écart moyen (la racine de la moyenne des carrés des écarts) entre une courbe lissée et la vraie tendance, à partir de $t = 60$.

Calcule :
- a) `window_errors`, la liste des erreurs `error(moving(x, k))` pour chaque fenêtre de `windows` (dans cet ordre) ;
- b) `beta_errors`, la liste des erreurs `error(ema(x, beta))` pour chaque valeur de `betas`.

Puis, en lisant tes listes et la figure :
- c) la fenêtre de `windows` qui donne la plus petite erreur ;
- d) la valeur de `betas` qui donne la plus petite erreur ;
- e) avec une fenêtre de 61, la courbe lissée est-elle en avance (1) ou en retard (2) sur la vraie tendance ?

Dans ta copie : pourquoi l'erreur diminue-t-elle d'abord, puis augmente-t-elle, quand la fenêtre grandit ?""",
    given=R5_19_GIVEN,
    todo='''window_errors = ...  # a) a list: error(moving(x, k)) for each k of windows
beta_errors = ...    # b) a list: error(ema(x, beta)) for each beta of betas
answer_R5_19c = ...  # c) a window of windows
answer_R5_19d = ...  # d) a value of betas
answer_R5_19e = ...  # e) 1 (ahead) or 2 (behind)''',
    check='''with checked("R5.19"):
    wbm.check("R5.19a", window_errors, computed=True)
    wbm.check("R5.19b", beta_errors, computed=True)
for letter, answer in zip("cde", [answer_R5_19c, answer_R5_19d, answer_R5_19e]):
    wbm.check(f"R5.19{letter}", answer)''',
    solution='''window_errors = [error(moving(x, k)) for k in windows]
beta_errors = [error(ema(x, beta)) for beta in betas]
answer_R5_19c = windows[int(np.argmin(window_errors))]
answer_R5_19d = betas[int(np.argmin(beta_errors))]
answer_R5_19e = 2
print("fenêtres :", dict(zip(windows, np.round(window_errors, 3))))
print("β        :", dict(zip(betas, np.round(beta_errors, 3))))''',
    record='''wbm.record("R5.19a", [error(moving(x, k)) for k in windows], decimals=4,
           mistakes={"une erreur par fenêtre, dans l'ordre de windows : error(moving(x, k))":
                         [error(moving(x, k)) for k in reversed(windows)]})
wbm.record("R5.19b", [error(ema(x, beta)) for beta in betas], decimals=4,
           mistakes={"une erreur par valeur de β, dans l'ordre de betas : error(ema(x, beta))":
                         [error(ema(x, beta)) for beta in reversed(betas)]})
wbm.record("R5.19c", 9, choices=[1, 3, 9, 25, 61],
           mistakes={"la plus grande fenêtre lisse le plus, mais la courbe prend du retard : lis la liste des erreurs":
                         61, "une fenêtre de 1 ne lisse rien : l'erreur est celle du bruit": 1,
                     "cherche la plus petite erreur de window_errors": {3, 25}})
wbm.record("R5.19d", 0.75, decimals=2,
           mistakes={"un β proche de 1 lisse fort, mais réagit lentement : lis la liste des erreurs": {0.99, 0.9},
                     "β = 0 ne lisse rien : v_t = x_t": 0, "cherche la plus petite erreur de beta_errors": 0.5})
wbm.record("R5.19e", 2, choices=[1, 2],
           mistakes={"la moyenne à l'instant t n'utilise que des valeurs passées : regarde où sont ses sommets": 1})''',
    after=[("md", "**La figure** : les erreurs en fonction de la fenêtre et de β, puis deux lissages."),
           ("code", R5_19_PLOT)],
    note="Une petite fenêtre garde le bruit ; une grande moyenne sur des valeurs trop anciennes : la courbe lissée "
         "est **en retard** (la moyenne sur 61 valeurs décrit, à peu près, la tendance d'il y a 30 instants) et "
         "aplatit les sommets. Le meilleur réglage est entre les deux, et il dépend du signal : plus la tendance "
         "change vite, plus il faut une petite fenêtre (ou un petit β).",
)

R5_20_CHECK = '''with checked("R5.20 vérifications"):
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.2))
    try:
        created = drawn(plot_sequences, axes)
    finally:
        plt.close(fig)                                     # only the checks below are shown here
    rules = [lambda n: 5 - 4 * 0.7**n, lambda n: 2 + 3 * (-0.75) ** n, lambda n: (-1) ** n * n / (n + 1),
             lambda n: math.sqrt(n)]
    problems = []
    if created:
        problems.append("un dessin dans les axes reçus (axes[0].plot, …), sans créer de figure")
    else:
        for name, ax, rule in zip("abcd", axes, rules):
            points = []
            for line in ax.lines:
                points += list(zip(np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)))
            for collection in ax.collections:
                points += [tuple(p) for p in np.asarray(collection.get_offsets(), dtype=float)]
            missing = [n for n in range(21) if not any(abs(px - n) < 1e-9 and abs(py - rule(n)) < 1e-6 for px, py in points)]
            if missing:
                problems.append(f"les termes de ({name}) dans axes[{'abcd'.index(name)}] (il manque au moins le rang {missing[0]})")
    if problems:
        print("❌ Ex R5.20 : il manque " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex R5.20 : les quatre suites sont tracées, chacune dans son graphique.")'''

R5_20 = Ex(
    "R5.20", "🎨", 1, 15, "Des suites qui convergent, divergent, oscillent",
    "voir les comportements d'une suite (converger, osciller, diverger), et reconnaître une limite sur un graphique.",
    "fiche §5 ; R0 (matplotlib)", tracks="C",
    body="""Complète `plot_sequences(axes)`, qui reçoit **quatre axes** côte à côte et trace, pour $n = 0$ à 30, les termes de :
- (a) $5 - 4 \\times 0{,}7^n$ dans `axes[0]` ;
- (b) $2 + 3 \\times (-0{,}75)^n$ dans `axes[1]` ;
- (c) $(-1)^n \\times \\frac{n}{n + 1}$ dans `axes[2]` ;
- (d) $\\sqrt{n}$ dans `axes[3]`.

Trace des **points** (une suite n'est définie qu'aux entiers) : `ax.plot(ns, values, "o")`, avec `ns = np.arange(31)` et le calcul vectorisé de NumPy ; un titre par graphique. La cellule de vérification crée les axes, puis la figure s'affiche. Puis :
- a) les lettres des suites qui convergent, dans l'ordre alphabétique (un texte, comme `"bd"`) ;
- b) la liste de leurs limites, dans le même ordre ;
- c) la suite (c) se rapproche tour à tour de deux nombres : la liste de ces deux nombres.

Dans ta copie : pour chaque suite, une phrase qui décrit son comportement (converge en restant du même côté, converge en oscillant, oscille sans limite, tend vers $+\\infty$).""",
    todo='''def plot_sequences(axes):
    """Draw the terms of (a), (b), (c), (d) for n = 0 to 30 as points, one sequence in each of the four axes."""
    raise NotImplementedError("trace les quatre suites dans axes[0] à axes[3]")


answer_R5_20a = ...  # a) letters, as text
answer_R5_20b = ...  # b) a list of limits
answer_R5_20c = ...  # c) a list of two numbers''',
    check='''with checked("R5.20 figure"):
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.2))
    try:
        created = drawn(plot_sequences, axes)
    except BaseException:
        plt.close(fig)                                     # no empty figure while plot_sequences is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex R5.20 : ta fonction ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans les axes "
              "qu'elle reçoit, avec axes[0].plot(...), …")
    else:
        fig.tight_layout()
        plt.show()
for letter, answer in zip("abc", [answer_R5_20a, answer_R5_20b, answer_R5_20c]):
    wbm.check(f"R5.20{letter}", answer)''',
    solution='''def plot_sequences(axes):
    """Draw the terms of (a), (b), (c), (d) for n = 0 to 30 as points, one sequence in each of the four axes."""
    ns = np.arange(31)
    terms = [5 - 4 * 0.7**ns, 2 + 3 * (-0.75) ** ns, (-1.0) ** ns * ns / (ns + 1), np.sqrt(ns)]
    titles = ["(a) 5 − 4 × 0,7ⁿ", "(b) 2 + 3 × (−0,75)ⁿ", "(c) (−1)ⁿ n / (n + 1)", "(d) √n"]
    for ax, values, title in zip(axes, terms, titles):
        ax.plot(ns, values, "o", markersize=3)
        ax.axhline(0, color="gray", linewidth=0.6)
        ax.set_title(title)
        ax.set_xlabel("n")
        ax.grid(True, alpha=0.3)


fig, axes = plt.subplots(1, 4, figsize=(14, 3.2))
plot_sequences(axes)
fig.tight_layout()
plt.show()
answer_R5_20a, answer_R5_20b, answer_R5_20c = "ab", [5, 2], [-1, 1]''',
    record='''wbm.record("R5.20a", "ab",
           mistakes={"(c) se rapproche tour à tour de deux nombres différents : elle n'a pas de limite": {"abc", "c"},
                     "√n grandit sans fin, lentement : elle tend vers +∞, elle ne converge pas": {"abd", "d"},
                     "(b) oscille, mais de moins en moins : l'écart à sa limite est multiplié par −0,75 à chaque pas":
                         "a",
                     "(a) converge : l'écart à sa limite est multiplié par 0,7 à chaque pas": "b"})
wbm.record("R5.20b", [5, 2],
           mistakes={"0,7ⁿ tend vers 0, pas vers 1 : dans (a), le terme 4 × 0,7ⁿ disparaît": [1, 2],
                     "(−0,75)ⁿ tend vers 0, pas vers 1 : dans (b), le terme 3 × (−0,75)ⁿ disparaît": [5, 5],
                     "les limites, pas les coefficients des puissances": [-4, 3]})
wbm.record("R5.20c", [-1, 1], ordered=False,
           mistakes={"n / (n + 1) tend vers 1 : (c) saute entre des valeurs proches de −1 et de 1": [0, 1],
                     "(c) n'a pas de limite : ses termes se rapprochent tour à tour de deux nombres": [0]})''',
    after=[("md", "**Vérifications automatiques** (la figure elle-même se juge à l'œil)."), ("code", R5_20_CHECK)],
    note="(a) converge vers 5 en restant en dessous ; (b) converge vers 2 en oscillant autour ; (c) n'a pas de "
         "limite : ses termes pairs tendent vers 1, ses termes impairs vers −1 ; (d) tend vers $+\\infty$, si "
         "lentement qu'on pourrait croire, sur 30 termes, qu'elle se stabilise : il faut $n = 10\\,000$ pour "
         "atteindre 100.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: an index shift, and timing (R5.21, R5.22)
# ---------------------------------------------------------------------------
R5_21_BUGGY = '''def total_savings(first, rate, years):
    """The total of `years` yearly deposits that grow by `rate` each year: first, first*(1 + rate), …"""
    q = 1 + rate                                        # (A)
    total = 0                                           # (B)
    for k in range(1, years):                           # (C)
        total += first * q**k                           # (D)
    return total                                        # (E)


def total_formula(first, rate, years):
    """The same total, with the formula of the sum of a geometric sequence."""
    q = 1 + rate                                        # (F)
    return first * (1 - q ** (years - 1)) / (1 - q)    # (G)'''

R5_21_FIXED = '''def total_savings(first, rate, years):
    """The total of `years` yearly deposits that grow by `rate` each year: first, first*(1 + rate), …"""
    q = 1 + rate                                        # (A)
    total = 0                                           # (B)
    for k in range(years):                              # (C) corrected: k = 0, 1, …, years - 1
        total += first * q**k                           # (D)
    return total                                        # (E)


def total_formula(first, rate, years):
    """The same total, with the formula of the sum of a geometric sequence."""
    q = 1 + rate                                        # (F)
    return first * (1 - q**years) / (1 - q)            # (G) corrected: years terms, so q**years'''

R5_21_MISTAKES = bug_letters_mistakes(
    "CG", "ABDEF",
    {"C": "compte les tours de la boucle pour years = 3 : combien de dépôts sont ajoutés ?",
     "G": "dans la formule, l'exposant est le nombre de termes"},
    special={("C", "D"): "la ligne (D) est juste si la boucle part de k = 0 : c'est la boucle qui saute un dépôt"})

R5_21 = Ex(
    "R5.21", "🐛", 1, 15, "Chasse à l'erreur : un décalage d'indice dans une somme",
    "repérer un décalage d'indice dans une boucle et dans une formule de somme, puis le corriger.",
    "fiche §4 ; R4 §5 (bornes d'un range)", tracks="C, E",
    body="""Une épargnante dépose `first` euros la première année, puis augmente son dépôt de `rate` (2 % s'écrit `0.02`) chaque année : ses dépôts sont `first`, `first*(1 + rate)`, `first*(1 + rate)**2`, … Les deux fonctions ci-dessous doivent calculer le total de ses `years` premiers dépôts, l'une avec une boucle, l'autre avec la formule de la fiche §4. Elles contiennent chacune une erreur d'indice. **Sans rien exécuter d'abord**, trouve-les.

```python
""" + R5_21_BUGGY + """
```

- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) combien de dépôts la boucle fautive additionne-t-elle pour `years = 10` ?

Puis corrige les deux fonctions dans la cellule ci-dessous (elle contient le code fautif) : la vérification calcule c), la liste `[total_savings(1000, 0.02, 5), total_formula(1000, 0.02, 5)]`, qui doit donner deux fois le même total.""",
    todo='''answer_R5_21a = ...  # a) letters, as text
answer_R5_21b = ...  # b) an integer


# correct the two functions below
''' + R5_21_BUGGY,
    check='''for letter, answer in zip("ab", [answer_R5_21a, answer_R5_21b]):
    wbm.check(f"R5.21{letter}", answer)
with checked("R5.21c"):
    wbm.check("R5.21c", [total_savings(1000, 0.02, 5), total_formula(1000, 0.02, 5)], computed=True)''',
    solution='''answer_R5_21a = "CG"
answer_R5_21b = len(range(1, 10))

''' + R5_21_FIXED + '''


print(answer_R5_21a, answer_R5_21b, [total_savings(1000, 0.02, 5), total_formula(1000, 0.02, 5)])''',
    record=f'''wbm.record("R5.21a", "CG",
           mistakes={R5_21_MISTAKES})
wbm.record("R5.21b", 9,
           mistakes={{"range(1, years) va de 1 à years − 1 : la borne de droite est exclue": {{10, 11}}}})
wbm.record("R5.21c", [5204.04016, 5204.04016], decimals=4,
           mistakes={{"la boucle saute encore le premier dépôt : k doit partir de 0": [4204.04016, 5204.04016],
                     "la formule : l'exposant de q est le nombre de dépôts": [5204.04016, 4121.608],
                     "les deux fonctions sont encore fausses : relis a)": [4204.04016, 4121.608]}})''',
    note="Les deux erreurs sont le même décalage d'indice, sous deux formes : `range(1, years)` n'a que `years − 1` "
         "tours et oublie le dépôt de rang 0 ; la formule utilise $q^{n-1}$ au lieu de $q^n$, où $n$ est le "
         "**nombre** de termes. Le réflexe qui les attrape : tester avec `years = 1` (un seul dépôt, le total vaut "
         "`first`) et `years = 2`.",
)

R5_22_TODO = '''def loop_sum(q, n):
    """1 + q + … + q**(n - 1), added term by term."""
    total = 0.0
    for k in range(n):
        total += q**k
    return total


def formula_sum(q, n):
    """The same sum with the formula (q != 1)."""
    return (1 - q**n) / (1 - q)


# For n = 10**3, 10**4, 10**5 and 10**6, with q = 0.999999: measure the time of each function with
# time.perf_counter() (before and after the call), and print n, the two times and the gap between the two results.
'''

R5_22_SOLUTION = R5_22_TODO + '''for n in [10**3, 10**4, 10**5, 10**6]:
    start = time.perf_counter()
    by_loop = loop_sum(0.999999, n)
    middle = time.perf_counter()
    by_formula = formula_sum(0.999999, n)
    end = time.perf_counter()
    print(f"n = {n:>9,} : boucle {middle - start:.5f} s, formule {end - middle:.7f} s, "
          f"écart {abs(by_loop - by_formula):.1e}")'''

R5_22 = Ex(
    "R5.22", "🛠️", 1, 15, "Une boucle ou une formule ? Mesurer le temps de calcul",
    "mesurer le temps d'un calcul avec `time.perf_counter`, et voir ce qu'une formule fait gagner sur une boucle.",
    "fiche §4 ; R5.14", tracks="C",
    body="""`time.perf_counter()` rend un temps en secondes, très précis : la durée d'un calcul est la différence entre la valeur lue juste après et la valeur lue juste avant. Complète la cellule : pour $n = 10^3$, $10^4$, $10^5$ et $10^6$, et $q = 0{,}999\\,999$, mesure le temps de `loop_sum(q, n)` et celui de `formula_sum(q, n)`, et affiche $n$, les deux temps et l'écart entre les deux résultats.

Puis, dans ta copie :
1. Quand $n$ est multiplié par 10, par combien le temps de la boucle est-il (à peu près) multiplié ? Et celui de la formule ?
2. Les deux résultats sont-ils exactement égaux ? D'où vient l'écart (R1 : les flottants) ?
3. Pourquoi les temps changent-ils un peu d'une exécution à l'autre ?""",
    after=[("todo", R5_22_TODO), ("solution", R5_22_SOLUTION)],
    note="Le temps de la boucle est proportionnel à $n$ (chaque terme coûte une puissance et une addition) ; celui de "
         "la formule ne dépend presque pas de $n$. Les résultats diffèrent dans les derniers chiffres : les arrondis "
         "des flottants ne tombent pas au même endroit. Les temps varient d'une exécution à l'autre, parce que "
         "l'ordinateur fait autre chose en même temps : on mesure plusieurs fois (le module `timeit` le fait) et "
         "l'on garde l'ordre de grandeur.",
)


PART_A = Part("A", "Ta librairie : termes, sommes, récurrences et lissages",
              "Fiche §1, §2, §4 et §6. Les cinq fonctions de `mymath/sequences.py`.",
              given=TOOLS, exercises=[R5_14, R5_15, R5_16])

PART_B = Part("B", "NumPy, une prédiction et des expériences",
              "Fiche §4 à §6. Les mêmes calculs en une ligne avec NumPy, une récurrence à prédire, le réglage d'un "
              "lissage, puis des suites qui convergent ou non, en image.", exercises=[R5_17, R5_18, R5_19, R5_20])

PART_C = Part("C", "Indices et temps de calcul",
              "Fiche §4. Deux décalages d'indice à trouver, puis une boucle et une formule chronométrées.",
              exercises=[R5_21, R5_22])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | R5.1 à R5.8, R5.11, R5.12 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# R5 · Suites — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/r5_suites/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py R5`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# R5 · Suites — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : termes, raisons, sommes, sommes infinies, intérêts "
               "composés, moyennes mobiles et exponentielles.\n"
               "- Écrire les cinq fonctions de `mymath/sequences.py` et les tester.\n"
               "- Refaire ces calculs avec NumPy, prédire le comportement d'une récurrence, régler un lissage, tracer "
               "des suites, chasser un décalage d'indice et chronométrer une formule.\n\n"
               "**Rappel express.** Arithmétique : $u_n = u_0 + n\\,r$ ; géométrique : $u_n = u_0\\,q^n$. Somme "
               "arithmétique : nombre de termes × (premier + dernier) / 2 ; somme géométrique de $n$ termes : premier "
               "× $\\frac{1 - q^n}{1 - q}$ ($q \\ne 1$). Si $\\lvert q \\rvert < 1$ : $q^n \\to 0$ et la somme infinie "
               "vaut premier ÷ $(1 - q)$. Moyenne exponentielle : $v_0 = 0$, $v_t = \\beta\\,v_{t-1} + "
               "(1 - \\beta)\\,x_t$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Calcules-tu les termes d'une suite explicite ou par récurrence, et reconnais-tu une suite "
               "arithmétique ou géométrique ?\n"
               "2. Calcules-tu une somme de termes, et une somme infinie géométrique, en comptant bien les termes ?\n"
               "3. Sais-tu dire si une suite converge, et calculer une moyenne mobile et une moyenne exponentielle ?\n\n"
               "**La suite** : R6, *Exponentielle et logarithmes*. Dans workbookIA, continue le chapitre 0A au rythme "
               "de ton tableau de bord.")]


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
