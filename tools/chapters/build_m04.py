#!/usr/bin/env python
"""Build the two notebooks of chapter M04 from a single source (used by Claude).

    python tools/chapters/build_m04.py
    python tools/run_all_notebooks.py chapitres/m04_bayes_beta/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m04_bayes_beta/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M04.1 to M04.10, 🔗 M04.14); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer nor the calculation that gives it. The data of the
notebook are new (parameters of Beta laws, quality-control counts, an expert's opinion): none is a test case of
tests/test_m04_bayes.py, an answer of the paper exercises, or an example of workbookIA 4 (no coin, no probe, no
medical test).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M04"
FOLDER = "chapitres/m04_bayes_beta"

F = 'kind="fraction", simplified=True'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M04.1", "Bayes avec deux hypothèses : un capteur de fuite d'eau", [
        ("a", "a number (4 decimals)", "0.01 * 0.95 + 0.99 * 0.03",
         'decimals=4, mistakes={"l\'évidence additionne les deux façons de sonner : avec une fuite, et sans fuite": '
         '0.0095, "chaque probabilité de sonner se pondère par la probabilité de son hypothèse, pour les nuits avec '
         'et sans fuite": 0.01 * 0.95 + 0.03}'),
        ("b", "a number (3 decimals)", "0.01 * 0.95 / (0.01 * 0.95 + 0.99 * 0.03)",
         'decimals=3, mistakes={"P(fuite | sonne) n\'est pas P(sonne | fuite) : parmi les nuits où il sonne, quelle '
         'part a une fuite ?": 0.95, "le produit a priori × vraisemblance se divise par l\'évidence": 0.0095}'),
        ("c", "a number (1 decimal)", "0.01 * 0.05 / (1 - (0.01 * 0.95 + 0.99 * 0.03)) * 10_000",
         'decimals=1, mistakes={"le produit a priori × vraisemblance se divise par l\'évidence de « ne sonne pas »": '
         '5.0, "P(fuite | ne sonne pas) n\'est pas P(ne sonne pas | fuite)": 500.0}'),
        ("d", "a number (1 decimal)", "1000 * (0.01 * 0.95 + 0.99 * 0.03)",
         'decimals=1, mistakes={"le capteur sonne aussi sans fuite : compte les deux sortes de nuits": 9.5}'),
        ("e", "a number (1 decimal)", "1000 * 0.99 * 0.03",
         'decimals=1, mistakes={"les fausses alertes viennent des seules nuits sans fuite": 30.0}'),
        ("f", "a number (3 decimals)", "0.01 * 0.95**2 / (0.01 * 0.95**2 + 0.99 * 0.03**2)",
         'decimals=3, mistakes={"c\'est l\'a posteriori après un seul capteur : le second le met à jour encore": '
         '0.01 * 0.95 / (0.01 * 0.95 + 0.99 * 0.03), "sans fuite aussi, les deux capteurs sonnent : la vraisemblance '
         'de « pas de fuite » est un produit de deux probabilités": 0.01 * 0.95**2 / (0.01 * 0.95**2 + 0.99 * 0.03)}'),
        ("g", "an irreducible fraction, as text", "Fraction(95, 9900)",
         F + ', mistakes={"P(sonne | pas de fuite) ne concerne que les nuits sans fuite : dans l\'évidence, elle se '
         'pondère par 0,99": "19/2000"}'),
        ("h", "a number (3 decimals)", "0.05 * 0.95 / (0.05 * 0.95 + 0.95 * 0.03)",
         'decimals=3, mistakes={"l\'a priori a changé : refais l\'évidence avec la nouvelle probabilité d\'une fuite": '
         '0.01 * 0.95 / (0.01 * 0.95 + 0.99 * 0.03)}'),
    ]),

    Paper("M04.2", "Trois hypothèses et un tableau de mise à jour", [
        ("a", "a number (2 decimals)", "float(PRIOR_2 @ VISIT_2)",
         'decimals=2, mistakes={"l\'évidence pondère la probabilité de venir de chaque type par l\'a priori du type": '
         '(0.9 + 0.4 + 0.05) / 3}'),
        ("b", "a list of 3 numbers (4 decimals)", "update(PRIOR_2, VISIT_2)",
         'decimals=4, mistakes={"les produits a priori × vraisemblance se divisent par leur somme, l\'évidence": '
         'PRIOR_2 * VISIT_2}'),
        ("c", "a list of 3 numbers (4 decimals)", "update(update(PRIOR_2, VISIT_2), 1 - VISIT_2)",
         'decimals=4, mistakes={"pour N, la vraisemblance de chaque type est sa probabilité de ne pas venir": '
         'update(update(PRIOR_2, VISIT_2), VISIT_2), "la deuxième mise à jour part de l\'a posteriori de b), pas de '
         'l\'a priori": update(PRIOR_2, 1 - VISIT_2)}'),
        ("d", "a list of 3 numbers (4 decimals)", "POST_2",
         'decimals=4, mistakes={"les produits se divisent par leur somme, l\'évidence de la suite": '
         'PRIOR_2 * VISIT_2 * (1 - VISIT_2) * VISIT_2}'),
        ("e", "a number (4 decimals)", "float(np.sum(PRIOR_2 * VISIT_2 * (1 - VISIT_2) * VISIT_2))",
         'decimals=4, mistakes={"l\'évidence de chaque étape se calcule avec l\'a posteriori de l\'étape d\'avant, pas '
         'avec l\'a priori de départ": 0.48 * 0.52 * 0.48}'),
        ("f", "a letter, as text", '"O"', 'mistakes={"compare les trois a posteriori de d)": {"R", "I"}}'),
        ("g", "a number (3 decimals)", "float(POST_2 @ VISIT_2)",
         'decimals=3, mistakes={"la prédiction pondère la probabilité de venir de chaque type par son a posteriori, '
         'pas par son a priori": 0.48, "pondère les trois types par leurs a posteriori, pas seulement le plus '
         'probable": 0.4}'),
        ("h", "an integer", "11",
         'mistakes={"I doit devenir plus probable que les deux autres types, pas seulement que R": 2, '
         '"compte seulement les semaines ajoutées après V, N, V": 12}'),
    ]),

    Paper("M04.3", "La vraisemblance d'un taux de clic", [
        ("a", "a number (2 decimals)", "3 / 20",
         'decimals=2, mistakes={"θ est le taux de clic : la proportion des affichages cliqués": 17 / 20}'),
        ("b", "a number (3 decimals)", "(0.15**3 * 0.85**17) / (0.1**3 * 0.9**17)",
         'decimals=3, mistakes={"le rapport demandé est L(0,15) divisé par L(0,10), pas l\'inverse": '
         '(0.1**3 * 0.9**17) / (0.15**3 * 0.85**17)}'),
        ("c", "a number (3 decimals)", "3 * math.log(0.15) + 17 * math.log(0.85)",
         'decimals=3, mistakes={"ℓ utilise le logarithme népérien ln, pas log₁₀": '
         '3 * math.log10(0.15) + 17 * math.log10(0.85)}'),
        ("d", "a number (4 decimals)", "math.comb(20, 3) * 0.15**3 * 0.85**17",
         'decimals=4, mistakes={"« dans n\'importe quel ordre » : multiplie par le nombre de places possibles des '
         '3 clics": 0.15**3 * 0.85**17}'),
        ("e", "a number (3 decimals)", "(0.3**3 * 0.7**17) / (0.15**3 * 0.85**17)",
         'decimals=3, mistakes={"le rapport demandé est L(0,30) divisé par L(0,15), pas l\'inverse": '
         '(0.15**3 * 0.85**17) / (0.3**3 * 0.7**17)}'),
        ("f", "a number (4 decimals)", "3 / 21",
         'decimals=4, mistakes={"un affichage sans clic ajoute 1 au nombre d\'affichages, pas au nombre de clics": '
         '4 / 21}'),
        ("g", "a number (2 decimals)", "5 / 50",
         'decimals=2, mistakes={"sur deux jours, la vraisemblance est un produit : additionne les clics et les '
         'affichages, ne fais pas la moyenne des deux fréquences": (3 / 20 + 2 / 30) / 2}'),
        ("h", "True or False", "True",
         'mistakes={"la vraisemblance d\'une suite ne dépend que du nombre de clics et de non-clics, pas de leurs '
         'places": False}'),
    ]),

    Paper("M04.4", "Maximiser une vraisemblance : dériver son logarithme", [
        ("a", "a number (2 decimals)", "5 * math.log(1) - 8 * 1",
         'decimals=2, mistakes={"ln(λ⁵ e^(−8λ)) = 5 ln λ − 8λ : le logarithme d\'une exponentielle est son '
         'exposant": 5 * math.log(1) - math.exp(-8)}'),
        ("b", "a number (2 decimals)", "5 / 1 - 8",
         'decimals=2, mistakes={"vérifie le signe : la dérivée de −8λ est −8": 3.0}'),
        ("c", "a number (3 decimals)", "5 / 8",
         'decimals=3, mistakes={"λ̂ est l\'inverse de la durée moyenne, pas la durée moyenne": 8 / 5}'),
        ("d", "a number (3 decimals)", "5 * math.log(5 / 8) - 5", 'decimals=3'),
        ("e", "a number (2 decimals)", "-5 / (5 / 8)**2",
         'decimals=2, mistakes={"vérifie le signe : la dérivée de 5/λ est −5/λ²": 5 / (5 / 8)**2}'),
        ("f", "a number (2 decimals)", "8 / 5",
         'decimals=2, mistakes={"la durée moyenne estimée est 1/λ̂, pas λ̂": 5 / 8}'),
        ("g", "a number (2 decimals)", "(2 + 0 + 3 + 1 + 4) / 5",
         'decimals=2, mistakes={"pour une loi de Poisson, μ̂ est la moyenne des comptages, pas son inverse": 0.5}'),
        ("h", "a number (2 decimals)", "7 / 25",
         'decimals=2, mistakes={"le maximum de vraisemblance est la proportion de succès": 18 / 25}'),
    ]),

    Paper("M04.5", "La loi Beta : normalisation, moyenne, mode, variance", [
        ("a", "an irreducible fraction, as text", "Fraction(1, 30)",
         F + ', mistakes={"B(a, b) = Γ(a)Γ(b)/Γ(a + b) avec Γ(n) = (n − 1)!, pas les factorielles de a et b": '
         '"1/21", "B(2, 5) est l\'intégrale ; la constante devant la densité est son inverse": "30"}'),
        ("b", "a number (4 decimals)", "30 * 0.2 * 0.8**4",
         'decimals=4, mistakes={"la densité de Beta(a, b) a pour exposants a − 1 et b − 1": 30 * 0.2**2 * 0.8**5, '
         '"n\'oublie pas la constante 1/B(2, 5) devant la densité": 0.2 * 0.8**4}'),
        ("c", "an irreducible fraction, as text", "Fraction(2, 7)",
         F + ', mistakes={"c\'est le mode ; la moyenne est a/(a + b)": "1/5"}'),
        ("d", "a number (2 decimals)", "1 / 5",
         'decimals=2, mistakes={"c\'est la moyenne ; le mode est (a − 1)/(a + b − 2)": 2 / 7}'),
        ("e", "an irreducible fraction, as text", "Fraction(5, 196)",
         F + ', mistakes={"relis la formule de la variance : le dénominateur a trois facteurs, (a + b)² et '
         '(a + b + 1)": "10/49"}'),
        ("f", "a number (4 decimals)", "57 / 64",
         'decimals=4, mistakes={"P(Θ ≤ 0,5) est l\'intégrale de la densité de 0 à 0,5, pas la densité en 0,5": '
         '30 * 0.5 * 0.5**4}'),
        ("g", "an integer", "12",
         'mistakes={"c est l\'inverse de l\'intégrale ; avec Γ(n) = (n − 1)!, B(3, 2) = Γ(3)Γ(2)/Γ(5)": 10}'),
        ("h", "a list of 2 integers", "[2, 6]",
         'mistakes={"la moyenne a/(a + b) vaut 0,25 : a est le plus petit des deux": [6, 2]}'),
    ]),

    Paper("M04.6", "Conjugaison : de Beta(a, b) à Beta(a + k, b + n − k)", [
        ("a", "a list of 2 integers", "[3 + 8, 27 + 42]",
         'mistakes={"b reçoit les échecs (les ventes gardées), pas toutes les ventes": [11, 77], '
         '"θ est le taux de retour : a reçoit les retours": [45, 35]}'),
        ("b", "a number (4 decimals)", "11 / 80",
         'decimals=4, mistakes={"c\'est la fréquence observée ; la moyenne a posteriori tient compte de l\'a priori": '
         '8 / 50, "c\'est la moyenne a priori ; les données la déplacent": 3 / 30}'),
        ("c", "a number (3 decimals)", "50 / 80",
         'decimals=3, mistakes={"le poids des données est n/(a + b + n), avec les paramètres de l\'a priori de départ": '
         '50 / 130}'),
        ("d", "a list of 2 integers", "[11 + 6, 69 + 44]",
         'mistakes={"la nouvelle mise à jour part de l\'a posteriori de a), pas de l\'a priori": [9, 71], '
         '"b reçoit les échecs (les ventes gardées), pas toutes les ventes": [17, 119]}'),
        ("e", "a number (4 decimals)", "17 / 130", 'decimals=4'),
        ("f", "a number (4 decimals)", "math.sqrt(11 * 69 / (80**2 * 81))",
         'decimals=4, mistakes={"l\'écart-type est la racine carrée de la variance": 11 * 69 / (80**2 * 81)}'),
        ("g", "a number (4 decimals)", "(1.5 + 8) / (1.5 + 13.5 + 50)",
         'decimals=4, mistakes={"recalcule avec l\'a priori Beta(1,5 ; 13,5)": 11 / 80}'),
        ("h", "an integer", "270", ''),
    ]),

    Paper("M04.7", "Lissage de Laplace : la prédictive avec Beta(1, 1)", [
        ("a", "an irreducible fraction, as text", "Fraction(1, 6)",
         F + ', mistakes={"le lissage de Laplace ajoute un succès et un échec imaginaires, donc 2 essais": "1/5", '
         '"c\'est le maximum de vraisemblance, que le lissage corrige": "0"}'),
        ("b", "an irreducible fraction, as text", "Fraction(6, 7)",
         F + ', mistakes={"le lissage de Laplace ajoute un succès et un échec imaginaires, donc 2 essais": "5/6", '
         '"c\'est le maximum de vraisemblance, que le lissage corrige": "1"}'),
        ("c", "a number (2 decimals)", "(0 + 0.5) / (4 + 2 * 0.5)",
         'decimals=2, mistakes={"avec α ajouté à chaque comptage, le dénominateur reçoit 2α": 0.5 / 4.5}'),
        ("d", "an irreducible fraction, as text", "Fraction(0 + 1, 9 + 3)",
         F + ', mistakes={"avec K = 3 catégories, le dénominateur reçoit K, pas 2": "1/11"}'),
        ("e", "an irreducible fraction, as text", "Fraction(1, 6) * Fraction(2, 7)",
         F + ', mistakes={"après un achat, la loi se met à jour : la deuxième visite n\'a plus la même probabilité": '
         '"1/36"}'),
        ("f", "an irreducible fraction, as text", "1 - Fraction(5, 6) * Fraction(6, 7)",
         F + ', mistakes={"« au moins une » est le contraire de « aucune », et la loi se met à jour entre les deux '
         'visites": "11/36"}'),
    ]),

    Paper("M04.8", "MAP, maximum de vraisemblance et moyenne a posteriori", [
        ("a", "a number (2 decimals)", "9 / 10", 'decimals=2'),
        ("b", "a number (4 decimals)", "(5 + 9 - 1) / (5 + 5 + 10 - 2)",
         'decimals=4, mistakes={"c\'est la moyenne a posteriori ; le MAP est le mode (a − 1)/(a + b − 2)": 14 / 20}'),
        ("c", "a number (2 decimals)", "14 / 20",
         'decimals=2, mistakes={"c\'est le MAP ; la moyenne est a/(a + b)": 13 / 18}'),
        ("d", "a number (2 decimals)", "9 / 10",
         'decimals=2, mistakes={"c\'est la moyenne a posteriori ; le MAP est le mode": 10 / 12}'),
        ("e", "a number (4 decimals)", "10 / 12",
         'decimals=4, mistakes={"c\'est le MAP ; la moyenne est a/(a + b)": 9 / 10}'),
        ("f", "a number (2 decimals)", "14 / 20",
         'decimals=2, mistakes={"compare les trois estimations calculées avec l\'a priori Beta(5, 5)": '
         '{13 / 18, 9 / 10}}'),
        ("g", "a number (2 decimals)", "1 / 5",
         'decimals=2, mistakes={"le MAP est le mode de l\'a posteriori, pas sa moyenne": 2 / 7, '
         '"c\'est le maximum de vraisemblance ; l\'a priori Beta(2, 2) éloigne le MAP du bord": 0.0}'),
        ("h", "an integer", "13",
         'mistakes={"le MAP doit dépasser strictement 0,8 : calcule-le exactement pour ton nombre": 12}'),
    ]),

    Paper("M04.9", "Un intervalle de crédibilité d'une loi Beta", [
        ("a", "a list of 2 integers", "[1, 9]",
         'mistakes={"θ est la probabilité de défaut : a compte les défauts, b les fabrications sans défaut": [9, 1]}'),
        ("b", "a number (4 decimals)", "1 - 0.9**9",
         'decimals=4, mistakes={"P(θ ≤ 0,1) = F(0,1) = 1 − (1 − 0,1)^b": 0.9**9}'),
        ("c", "a number (5 decimals)", "1 - 0.975**(1 / 9)",
         'decimals=5, mistakes={"la borne basse laisse 2,5 % à sa gauche : elle résout F(x) = 0,025": '
         '1 - 0.025**(1 / 9)}'),
        ("d", "a number (4 decimals)", "1 - 0.025**(1 / 9)",
         'decimals=4, mistakes={"la borne haute laisse 2,5 % à sa droite : elle résout F(x) = 0,975": '
         '1 - 0.975**(1 / 9)}'),
        ("e", "a number (4 decimals)", "1 - 0.05**(1 / 9)",
         'decimals=4, mistakes={"une borne supérieure à 95 % laisse 5 % à sa droite, tout d\'un côté": '
         '1 - 0.025**(1 / 9)}'),
        ("f", "a number (4 decimals)", "1 - 0.5**(1 / 9)",
         'decimals=4, mistakes={"c\'est la moyenne ; la médiane résout F(x) = 0,5": 0.1}'),
        ("g", "a list [low, high] (4 decimals)", "[0.025**(1 / 3), 0.975**(1 / 3)]",
         'decimals=4, mistakes={"l\'ordre est [basse, haute]": [0.975**(1 / 3), 0.025**(1 / 3)]}'),
    ]),

    Paper("M04.10", "Log-probabilités : additionner au lieu de multiplier, normaliser par log-sum-exp", [
        ("a", "a number (2 decimals)", "500 * math.log(0.2)",
         'decimals=2, mistakes={"ln(0,2^500) = 500 ln 0,2, avec le logarithme népérien": 500 * math.log10(0.2)}'),
        ("b", "a number (3 decimals)", "500 * math.log10(0.2)",
         'decimals=3, mistakes={"log₁₀, pas ln : log₁₀ x = ln x / ln 10": 500 * math.log(0.2)}'),
        ("c", "True or False", "True",
         'mistakes={"compare la puissance de 10 trouvée en b) à celle du plus petit float positif": False}'),
        ("d", "a number (3 decimals)", "-1000 + math.log(1 + math.exp(-1) + math.exp(-3))",
         'decimals=3, mistakes={"ln(eˣ + eʸ) n\'est ni x + y, ni le plus grand des deux : relis log-sum-exp (fiche §7)": '
         '{-3004.0, -1000.0}}'),
        ("e", "a list of 3 numbers (4 decimals)",
         "list(np.exp(np.array([0, -1, -3]) - math.log(1 + math.exp(-1) + math.exp(-3))))",
         'decimals=4, mistakes={"des probabilités ont une somme de 1 : divise par la somme des exponentielles": '
         '[1.0, math.exp(-1), math.exp(-3)]}'),
        ("f", "a list of 3 numbers (4 decimals)", "list(np.exp(LOG_10 - LOG_10.max()) / np.exp(LOG_10 - LOG_10.max()).sum())",
         'decimals=4, mistakes={"l\'a priori compte : ajoute le logarithme de l\'a priori à chaque log-vraisemblance": '
         'list(np.exp(np.array([0, -1, -3]) - math.log(1 + math.exp(-1) + math.exp(-3))))}'),
    ]),

    Paper("M04.14", "Un test A/B : deux taux de conversion et P(θB > θA) par simulation", [
        ("a", "a list of 2 integers", "[1 + 30, 1 + 270]",
         'mistakes={"l\'a priori uniforme est Beta(1, 1) : ajoute 1 aux deux comptages": [30, 270], '
         '"b compte les visites sans commande, pas toutes les visites": [31, 301]}'),
        ("b", "a number (4 decimals)", "46 / 302",
         'decimals=4, mistakes={"si c\'est la fréquence observée : la moyenne a posteriori tient compte de l\'a priori '
         'uniforme ; sinon, garde 4 décimales": 45 / 300}'),
        ("c", "a number (4 decimals)", "SD_B",
         'decimals=4, mistakes={"l\'écart-type est la racine carrée de la variance": SD_B**2}'),
        ("d", "a number (4 decimals)", "SD_A",
         'decimals=4, mistakes={"l\'écart-type est la racine carrée de la variance": SD_A**2}'),
        ("e", "a number (2 decimals)", "0.5 * (1 + math.erf(15 / 302 / math.sqrt(SD_A**2 + SD_B**2) / math.sqrt(2)))",
         'decimals=2, mistakes={"la variance d\'une différence de variables indépendantes est la somme des '
         'variances : l\'écart-type n\'est pas la somme des écarts-types": '
         '0.5 * (1 + math.erf(15 / 302 / (SD_A + SD_B) / math.sqrt(2)))}'),
        ("f", "a number (3 decimals)", "float(np.mean(THETA_B > THETA_A))",
         'decimals=3, mistakes={"exécute la simulation donnée, avec la graine 14, et compte la proportion des '
         'tirages où θB > θA": 0.967}'),
        ("g", "a number (4 decimals)", "float(np.mean(THETA_B - THETA_A))",
         'decimals=4, mistakes={"c\'est la différence exacte des moyennes a posteriori ; la question demande la '
         'moyenne dans la simulation": 15 / 302}'),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math
from fractions import Fraction

import numpy as np


def update(prior, likelihood):
    """Bayes' rule on a finite set of hypotheses: prior × likelihood, divided by its sum (the evidence)."""
    product = np.asarray(prior, dtype=float) * np.asarray(likelihood, dtype=float)
    return product / product.sum()


PRIOR_2, VISIT_2 = np.array([0.3, 0.5, 0.2]), np.array([0.9, 0.4, 0.05])     # M04.2: R, O, I
POST_2 = update(update(update(PRIOR_2, VISIT_2), 1 - VISIT_2), VISIT_2)        # after V, N, V
LOG_10 = np.log([0.2, 0.5, 0.3]) + np.array([-1000, -1001, -1003])           # M04.10 f): log(prior × likelihood)
SD_A = math.sqrt(31 * 271 / (302**2 * 303))                                    # M04.14: posterior standard deviations
SD_B = math.sqrt(46 * 256 / (302**2 * 303))
rng = np.random.default_rng(14)                                                # M04.14 f) and g): the simulation
THETA_A = rng.beta(31, 271, 100_000)
THETA_B = rng.beta(46, 256, 100_000)'''

SIMULATION_14 = '''# Ex M04.14 f) and g): the simulation of the statement (replace the ... by the parameters of the two posteriors)
import numpy as np

a_A, b_A = ..., ...                      # the parameters of the posterior of θA (your answer to a)
a_B, b_B = ..., ...                      # the parameters of the posterior of θB
if any(value is ... for value in (a_A, b_A, a_B, b_B)):
    print("⏳ Remplis d'abord les paramètres des deux a posteriori, puis exécute à nouveau.")
else:
    rng = np.random.default_rng(14)
    theta_A = rng.beta(a_A, b_A, 100_000)    # 100 000 draws from the posterior of A, first
    theta_B = rng.beta(a_B, b_B, 100_000)    # then 100 000 draws from the posterior of B
    print(np.mean(theta_B > theta_A), np.mean(theta_B - theta_A))'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M04.1 à M04.10, 🔗 M04.14)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"7/9\"` ;\n"
               "- une liste `[-1.5, 2.5]`, `True` / `False`, ou une lettre entre guillemets, `\"B\"`.\n\n"
               "Pour M04.14 f) et g), exécute d'abord la simulation de l'énoncé : sa cellule précède celle des réponses. Les "
               "réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M04.18 to M04.21)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize, special, stats

from wbm.nbtools import checked, drawn, run_pytest_group


def raised(function, *args):
    """The name of the exception that function(*args) raises, or "aucune" if it returns.

    NotImplementedError (a TODO not done yet) goes through, for wbm.attempt to show ⏳; so do the errors of a code
    that cannot run (a missing import, a misspelt name such as ValueErorr), for the check to name them."""
    try:
        function(*args)
    except (NotImplementedError, NameError, AttributeError, ImportError):
        raise
    except Exception as exc:  # noqa: BLE001 - any other error is the answer
        return type(exc).__name__
    return "aucune"'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M04")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/bayes.py`, lis la docstring "
         "de la fonction en entier, remplace la ligne `raise NotImplementedError(...)` par ton code, **enregistre** le "
         "fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. Le module `math` suffit ; "
         "`math.lgamma(x)` donne $\\ln\\Gamma(x)$ et `math.comb(n, k)` le coefficient binomial. `scipy.stats` et "
         "`scipy.special` sont interdits : les tests comparent tes résultats à eux, et un test vérifie que tu ne t'en "
         "sers pas. Les nombres renvoyés sont des `float` de Python, sauf les paramètres de "
         "`conjugate_beta_update`.")

WRONG_ERROR = "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)"
OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ZeroDivisionError"]


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of bayes.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m04_bayes.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m04_bayes.py", "{keyword}", impl="ref")')]


M04_18 = Ex(
    "M04.18", "🔨", 1, 20, "Densité et moments de la loi Beta (avec `math.lgamma`) · `beta_pdf, beta_moments`",
    "programmer la densité d'une loi Beta, bords compris, sans dépassement de capacité, et ses deux premiers moments.",
    "fiche §4 et §7", tracks="C, E", mymath="bayes.py",
    body=HOWTO + """

Écris, dans cet ordre (fiche §4) :
- `beta_pdf(x, a, b)` : la densité $\\frac{x^{a - 1}(1 - x)^{b - 1}}{B(a, b)}$, avec $B(a, b) = \\frac{\\Gamma(a)\\Gamma(b)}{\\Gamma(a + b)}$ ; `0.0` hors de $[0, 1]$ ; aux bords 0 et 1, les valeurs que donne la docstring ; une `ValueError` si $a \\le 0$ ou $b \\le 0$ ;
- `beta_moments(a, b)` : le couple (moyenne, variance).

Un piège : `math.gamma(700)` dépasse le plus grand `float` (environ $1{,}8 \\times 10^{308}$) et lève une `OverflowError`. Calcule donc le **logarithme** de la densité, $(a - 1)\\ln x + (b - 1)\\ln(1 - x) - \\ln B(a, b)$ avec $\\ln B(a, b) = \\ln\\Gamma(a) + \\ln\\Gamma(b) - \\ln\\Gamma(a + b)$ (fiche §7), et prends l'exponentielle à la fin. Une fonction auxiliaire `_check_parameters(a, b)` évite d'écrire plusieurs fois la même vérification.

La vérification calcule :
- a) `beta_pdf(0.3, 2, 6)` (4 décimales) ;
- b) `beta_pdf(1.2, 2, 6)` (4 décimales) ;
- c) `beta_pdf(0, 1, 6)` (4 décimales) ;
- d) `math.isinf(beta_pdf(1, 2, 0.6))` : la densité est-elle infinie en 1 ?
- e) `beta_pdf(0.43, 300, 400)` (3 décimales) ;
- f) `beta_moments(3, 9)` (4 décimales) ;
- g) le nom de l'erreur levée par `beta_pdf(0.3, -2, 3)` ;
- h) le nom du type de `beta_pdf(1.2, 2, 6)`, en texte.

Dans ta copie : refais a), c) et f) à la main. Pourquoi la densité de e) dépasse-t-elle 20, alors qu'une probabilité ne dépasse jamais 1 ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M04.18a"):
    wbm.check("M04.18a", mymath.bayes.beta_pdf(0.3, 2, 6), computed=True)
with checked("M04.18b"):
    wbm.check("M04.18b", mymath.bayes.beta_pdf(1.2, 2, 6), computed=True)
with checked("M04.18c"):
    wbm.check("M04.18c", mymath.bayes.beta_pdf(0, 1, 6), computed=True)
with checked("M04.18d"):
    wbm.check("M04.18d", math.isinf(mymath.bayes.beta_pdf(1, 2, 0.6)), computed=True)
with checked("M04.18e"):
    wbm.check("M04.18e", mymath.bayes.beta_pdf(0.43, 300, 400), computed=True)
with checked("M04.18f"):
    wbm.check("M04.18f", mymath.bayes.beta_moments(3, 9), computed=True)
with checked("M04.18g"):
    wbm.check("M04.18g", raised(mymath.bayes.beta_pdf, 0.3, -2, 3), computed=True)
with checked("M04.18h"):
    wbm.check("M04.18h", type(mymath.bayes.beta_pdf(1.2, 2, 6)).__name__, computed=True)''',
    solution=LOAD_REF + '''
bayes = mymath.bayes
print("a)", bayes.beta_pdf(0.3, 2, 6), " b)", bayes.beta_pdf(1.2, 2, 6), " c)", bayes.beta_pdf(0, 1, 6),
      " d)", math.isinf(bayes.beta_pdf(1, 2, 0.6)))
print("e)", bayes.beta_pdf(0.43, 300, 400), "· scipy:", stats.beta(300, 400).pdf(0.43))
print("f)", bayes.beta_moments(3, 9), " g)", raised(bayes.beta_pdf, 0.3, -2, 3),
      " h)", type(bayes.beta_pdf(1.2, 2, 6)).__name__)''',
    record=f'''wbm.record("M04.18a", 2.117682, decimals=4,
           mistakes={{"divise par B(a, b) : une densité a une aire de 1": 0.050421,
                     "les exposants de la densité sont a − 1 et b − 1": 0.44471322}})
wbm.record("M04.18b", 0.0, decimals=4,
           mistakes={{"hors de [0, 1], la densité vaut 0.0 : renvoie-le avant tout calcul": -0.016128}})
wbm.record("M04.18c", 6.0, decimals=4,
           mistakes={{"en x = 0 avec a = 1, le facteur x^(a − 1) vaut 1 : la densité vaut 1/B(1, b)": 0.0}})
wbm.record("M04.18d", True,
           mistakes={{"avec b < 1, (1 − x)^(b − 1) tend vers l'infini en 1 : la docstring demande math.inf": False}})
wbm.record("M04.18e", 21.2413908287, decimals=3)
wbm.record("M04.18f", [0.25, 27 / 1872], decimals=4,
           mistakes={{"relis la formule de la variance : le dénominateur est (a + b)²(a + b + 1)": [0.25, 27 / 144]}})
wbm.record("M04.18g", "ValueError",
           mistakes={{"a = −2 n'est pas un paramètre d'une loi Beta : lève une ValueError": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M04.18h", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy": "float64",
                     "la docstring demande un float de Python, même hors de [0, 1] : renvoie 0.0, pas 0": "int"}})''',
    after=tests_cells("test_beta_pdf_ or test_beta_moments_ or test_bayes_uses_"),
    note="a) $B(2, 6) = \\frac{1!\\,5!}{7!} = \\frac{1}{42}$, donc $42 \\times 0{,}3 \\times 0{,}7^5 \\approx 2{,}1177$. "
         "c) Avec $a = 1$, le facteur $x^0$ vaut 1 : la densité en 0 est $\\frac{1}{B(1, 6)} = 6$. d) $(1 - x)^{-0{,}4}$ "
         "tend vers l'infini en 1. e) Une densité n'est pas une probabilité : $\\mathrm{Beta}(300, 400)$ est très "
         "concentrée (écart-type d'environ 0,019 autour de 0,43), donc sa densité est haute, et son aire vaut "
         "toujours 1. `math.gamma(700)` lève une `OverflowError`, alors que `math.lgamma(700)` vaut environ 3 883. "
         "f) Moyenne $\\frac{3}{12} = 0{,}25$, variance $\\frac{27}{144 \\times 13} = \\frac{27}{1872} \\approx 0{,}0144$.",
)

M04_19 = Ex(
    "M04.19", "🔨", 2, 25, "Mise à jour conjuguée et loi prédictive des prochains essais · "
    "`conjugate_beta_update, posterior_predictive`",
    "programmer la mise à jour conjuguée d'une loi Beta et la probabilité de $k$ succès dans les $n$ prochains essais, "
    "sans dépassement de capacité.", "fiche §5 ; Ex M04.18", tracks="C, E", mymath="bayes.py",
    body="""Écris (fiche §5) :
- `conjugate_beta_update(a, b, successes, failures)` : les paramètres $(a + \\text{succès},\\ b + \\text{échecs})$ de l'a posteriori ; des entiers restent des entiers ; une `ValueError` pour des paramètres invalides ou un comptage négatif ;
- `posterior_predictive(a, b, k=1, n=1)` : la probabilité de $k$ succès dans les $n$ prochains essais quand la proportion suit $\\mathrm{Beta}(a, b)$, $\\binom{n}{k}\\frac{B(a + k,\\ b + n - k)}{B(a, b)}$ ; `0.0` si $k < 0$ ou $k > n$ ; une `ValueError` si $a \\le 0$, $b \\le 0$ ou $n < 0$.

Attention : dans `posterior_predictive`, $k$ et $n$ comptent les essais **futurs** (notés $j$ et $m$ dans la fiche, §5), pas les données déjà vues. Comme en M04.18, additionne des logarithmes ($\\ln\\binom{n}{k}$ par `math.lgamma`, puis $\\ln B$) et prends l'exponentielle à la fin.

La vérification calcule :
- a) `conjugate_beta_update(2, 3, 5, 10)` ;
- b) les deux paramètres renvoyés par a) sont-ils des `int` ? (`True` ou `False`)
- c) `posterior_predictive(7, 13)` (4 décimales) ;
- d) `posterior_predictive(7, 13, 2, 3)` (4 décimales) ;
- e) `posterior_predictive(7, 13, 4, 3)` (4 décimales) ;
- f) la somme des `posterior_predictive(7, 13, k, 3)` pour $k$ de 0 à 3 (4 décimales) ;
- g) le nom de l'erreur levée par `conjugate_beta_update(2, 3, -1, 4)` ;
- h) `posterior_predictive(300, 700, 12, 40)` (4 décimales).

Dans ta copie : refais c) et d) à la main, avec $\\Gamma(n) = (n - 1)!$. Calcule aussi la probabilité binomiale de 2 succès en 3 essais de probabilité $\\frac{7}{20}$ : pourquoi est-elle différente de d) ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M04.19a"):
    wbm.check("M04.19a", mymath.bayes.conjugate_beta_update(2, 3, 5, 10), computed=True)
with checked("M04.19b"):
    wbm.check("M04.19b", all(isinstance(v, int) for v in mymath.bayes.conjugate_beta_update(2, 3, 5, 10)),
              computed=True)
with checked("M04.19c"):
    wbm.check("M04.19c", mymath.bayes.posterior_predictive(7, 13), computed=True)
with checked("M04.19d"):
    wbm.check("M04.19d", mymath.bayes.posterior_predictive(7, 13, 2, 3), computed=True)
with checked("M04.19e"):
    wbm.check("M04.19e", mymath.bayes.posterior_predictive(7, 13, 4, 3), computed=True)
with checked("M04.19f"):
    wbm.check("M04.19f", sum(mymath.bayes.posterior_predictive(7, 13, k, 3) for k in range(4)), computed=True)
with checked("M04.19g"):
    wbm.check("M04.19g", raised(mymath.bayes.conjugate_beta_update, 2, 3, -1, 4), computed=True)
with checked("M04.19h"):
    wbm.check("M04.19h", mymath.bayes.posterior_predictive(300, 700, 12, 40), computed=True)''',
    solution=LOAD_REF + '''
bayes = mymath.bayes
print("a)", bayes.conjugate_beta_update(2, 3, 5, 10), " c)", bayes.posterior_predictive(7, 13),
      " d)", bayes.posterior_predictive(7, 13, 2, 3), " e)", bayes.posterior_predictive(7, 13, 4, 3))
print("f)", sum(bayes.posterior_predictive(7, 13, k, 3) for k in range(4)),
      " g)", raised(bayes.conjugate_beta_update, 2, 3, -1, 4),
      " h)", bayes.posterior_predictive(300, 700, 12, 40), "· scipy:", stats.betabinom(40, 300, 700).pmf(12))
print("binomial with p = 7/20:", stats.binom(3, 7 / 20).pmf(2))''',
    record=f'''wbm.record("M04.19a", [7, 13],
           mistakes={{"a reçoit les succès, b les échecs": [12, 8],
                     "b reçoit les échecs, pas le nombre total d'essais": [7, 18]}})
wbm.record("M04.19b", True,
           mistakes={{"des comptages entiers donnent des paramètres entiers : n'appelle pas float(...)": False}})
wbm.record("M04.19c", 0.35, decimals=4,
           mistakes={{"le succès suivant a pour probabilité la moyenne de la loi, pas son mode": 6 / 18}})
wbm.record("M04.19d", 13 / 55, decimals=4,
           mistakes={{"n'oublie pas C(n, k), le nombre de places des k succès": 13 / 165,
                     "les essais futurs ne sont pas indépendants sachant les seules données : la binomiale de "
                     "probabilité a/(a + b) ne convient pas": 0.238875}})
wbm.record("M04.19e", 0.0, decimals=4)
wbm.record("M04.19f", 1.0, decimals=4)
wbm.record("M04.19g", "ValueError",
           mistakes={{"un comptage négatif est impossible : lève une ValueError": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M04.19h", 0.1339200346, decimals=4)''',
    after=tests_cells("test_conjugate_beta_update_ or test_posterior_predictive_"),
    note="c) $\\frac{a}{a + b} = \\frac{7}{20}$. d) $3 \\times \\frac{B(9, 14)}{B(7, 13)} = 3 \\times \\frac{7 \\times 8 "
         "\\times 13}{20 \\times 21 \\times 22} = \\frac{13}{55} \\approx 0{,}2364$, contre 0,2389 pour la binomiale de "
         "probabilité $\\frac{7}{20}$ : sachant les seules données, les essais futurs ne sont pas indépendants (un "
         "succès rend le suivant plus probable), et la prédictive tient compte de l'incertitude sur $\\theta$. "
         "e) 4 succès en 3 essais : impossible. f) Une loi de probabilité sur $k = 0, 1, 2, 3$ : somme 1. h) "
         "$\\Gamma(1000)$ dépasse le plus grand `float` : seule la somme de logarithmes passe.",
)

M04_20 = Ex(
    "M04.20", "🔨", 2, 15, "Le MAP d'une loi Beta, cas limites compris · `map_estimate_beta`",
    "programmer le mode d'une loi Beta dans tous les cas : intérieur, aux bords, ou pas de mode unique.",
    "fiche §6 ; Ex M04.13", tracks="C", mymath="bayes.py",
    body="""Écris `map_estimate_beta(a, b)` (fiche §6) : le mode de $\\mathrm{Beta}(a, b)$, c'est-à-dire le MAP d'une proportion d'a posteriori $\\mathrm{Beta}(a, b)$. La formule $\\frac{a - 1}{a + b - 2}$ ne vaut que si $a > 1$ et $b > 1$. Sinon, la docstring dit, cas par cas, si la densité décroît (mode 0), croît (mode 1), ou n'a pas de mode unique (une `ValueError`). L'exercice ∂ M04.13 démontre chacun de ces cas ; un croquis des densités suffit pour les retrouver.

La vérification calcule :
- a) `map_estimate_beta(7, 13)` (4 décimales) ;
- b) `map_estimate_beta(0.6, 3)` (4 décimales) ;
- c) `map_estimate_beta(3, 0.8)` (4 décimales) ;
- d) `map_estimate_beta(0.6, 1)` (4 décimales) ;
- e) le nom de l'erreur levée par `map_estimate_beta(0.8, 0.6)` ;
- f) `map_estimate_beta(12.5, 50.5)` (4 décimales) ;
- g) le nom du type de `map_estimate_beta(1, 6)`, en texte ;
- h) `map_estimate_beta(5, 17)` (4 décimales).

Dans ta copie : esquisse les densités de b), c), d) et e). h) est l'a posteriori de l'a priori uniforme après 4 succès en 20 essais : que retrouves-tu ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M04.20a"):
    wbm.check("M04.20a", mymath.bayes.map_estimate_beta(7, 13), computed=True)
with checked("M04.20b"):
    wbm.check("M04.20b", mymath.bayes.map_estimate_beta(0.6, 3), computed=True)
with checked("M04.20c"):
    wbm.check("M04.20c", mymath.bayes.map_estimate_beta(3, 0.8), computed=True)
with checked("M04.20d"):
    wbm.check("M04.20d", mymath.bayes.map_estimate_beta(0.6, 1), computed=True)
with checked("M04.20e"):
    wbm.check("M04.20e", raised(mymath.bayes.map_estimate_beta, 0.8, 0.6), computed=True)
with checked("M04.20f"):
    wbm.check("M04.20f", mymath.bayes.map_estimate_beta(12.5, 50.5), computed=True)
with checked("M04.20g"):
    wbm.check("M04.20g", type(mymath.bayes.map_estimate_beta(1, 6)).__name__, computed=True)
with checked("M04.20h"):
    wbm.check("M04.20h", mymath.bayes.map_estimate_beta(5, 17), computed=True)''',
    solution=LOAD_REF + '''
mode = mymath.bayes.map_estimate_beta
print("a)", mode(7, 13), " b)", mode(0.6, 3), " c)", mode(3, 0.8), " d)", mode(0.6, 1),
      " e)", raised(mode, 0.8, 0.6), " f)", mode(12.5, 50.5), " g)", type(mode(1, 6)).__name__, " h)", mode(5, 17))''',
    record=f'''wbm.record("M04.20a", 6 / 18, decimals=4,
           mistakes={{"le MAP est le mode (a − 1)/(a + b − 2), pas la moyenne": 0.35}})
wbm.record("M04.20b", 0.0, decimals=4,
           mistakes={{"avec a < 1 < b, la densité décroît sur ]0, 1[ : la formule (a − 1)/(a + b − 2) ne vaut que pour "
                      "a > 1 et b > 1": -0.25}})
wbm.record("M04.20c", 1.0, decimals=4,
           mistakes={{"avec b < 1 < a, la densité croît sur ]0, 1[ : la formule (a − 1)/(a + b − 2) ne vaut que pour "
                      "a > 1 et b > 1": 2 / 1.8}})
wbm.record("M04.20d", 0.0, decimals=4,
           mistakes={{"avec a < 1 = b, la densité est proportionnelle à θ^(a − 1), qui décroît": 1.0}})
wbm.record("M04.20e", "ValueError",
           mistakes={{"avec a < 1 et b < 1, la densité a deux maximums, en 0 et en 1 : lève une ValueError":
                         {{"aucune", "ZeroDivisionError"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("M04.20f", 11.5 / 61, decimals=4,
           mistakes={{"le MAP est le mode (a − 1)/(a + b − 2), pas la moyenne": 12.5 / 63}})
wbm.record("M04.20g", "float",
           mistakes={{"la docstring demande un float de Python : renvoie 0.0, pas 0": "int"}})
wbm.record("M04.20h", 0.2, decimals=4,
           mistakes={{"le MAP est le mode (a − 1)/(a + b − 2), pas la moyenne": 5 / 22}})''',
    after=tests_cells("test_map_estimate_beta_"),
    note="a) $\\frac{6}{18} \\approx 0{,}3333$ (la moyenne vaut 0,35). b) et d) La densité décroît : mode 0 ; la "
         "formule donnerait $-0{,}25$ en b) et 1 en d), deux réponses absurdes. c) Elle croît : mode 1. e) Une densité "
         "en U a deux maximums, aux bords : pas de MAP unique. h) $\\frac{4}{20} = 0{,}2$, le maximum de "
         "vraisemblance : avec l'a priori uniforme, MAP et maximum de vraisemblance coïncident (fiche §6).",
)

M04_21 = Ex(
    "M04.21", "📦", 1, 15, "La fonction Beta avec `scipy.special` : `beta`, `betaln` et l'underflow",
    "calculer la fonction Beta et son logarithme avec `scipy.special`, voir l'underflow, et calculer un rapport de "
    "fonctions Beta par les logarithmes.", "fiche §4 et §7", tracks="C",
    body="""`scipy.special` regroupe les fonctions spéciales des mathématiques : `special.beta(a, b)` calcule $B(a, b)$, `special.betaln(a, b)` calcule $\\ln B(a, b)$ sans passer par $B(a, b)$, et `special.gammaln(x)` calcule $\\ln\\Gamma(x)$ (comme `math.lgamma`, mais sur des arrays). Lis `help(special.betaln)` avant de commencer.

Calcule avec ces fonctions :
- a) $\\frac{1}{B(4, 7)}$, arrondi à l'entier ;
- b) `special.beta(600, 900) == 0` : le résultat est-il nul en `float64` ? (`True` ou `False`)
- c) $\\ln B(600, 900)$ (2 décimales) ;
- d) $\\log_{10} B(600, 900)$ (2 décimales) ;
- e) $\\frac{B(602,\\ 900)}{B(600,\\ 900)}$, calculé par les logarithmes (4 décimales) ;
- f) $\\ln B(0{,}5 ;\\ 0{,}5)$ (4 décimales).

Dans ta copie : e) est la probabilité que les deux prochains essais soient des succès quand la proportion suit $\\mathrm{Beta}(600, 900)$ (fiche §5). Retrouve-la avec la formule $\\frac{a(a + 1)}{(a + b)(a + b + 1)}$, puis avec ta fonction `posterior_predictive`. Que donne `special.beta(602, 900) / special.beta(600, 900)`, et pourquoi ? Que vaut $\\mathrm{e}^{f}$, où $f$ est la réponse f) ?""",
    todo='''answer_M04_21a = ...  # a) an integer
answer_M04_21b = ...  # b) True or False
answer_M04_21c = ...  # c) a number (2 decimals)
answer_M04_21d = ...  # d) a number (2 decimals)
answer_M04_21e = ...  # e) a number (4 decimals)
answer_M04_21f = ...  # f) a number (4 decimals)''',
    check='''for letter, answer in zip("abcdef", [answer_M04_21a, answer_M04_21b, answer_M04_21c, answer_M04_21d,
                                     answer_M04_21e, answer_M04_21f]):
    wbm.check(f"M04.21{letter}", answer)''',
    solution='''answer_M04_21a = round(1 / special.beta(4, 7))
answer_M04_21b = bool(special.beta(600, 900) == 0)               # about 10**-439: below the smallest positive float64
answer_M04_21c = special.betaln(600, 900)
answer_M04_21d = special.betaln(600, 900) / math.log(10)         # log10 x = ln x / ln 10
answer_M04_21e = math.exp(special.betaln(602, 900) - special.betaln(600, 900))
answer_M04_21f = special.betaln(0.5, 0.5)
print([answer_M04_21a, answer_M04_21b] + [round(float(v), 4) for v in [answer_M04_21c, answer_M04_21d,
                                                                      answer_M04_21e, answer_M04_21f]])
print("formula:", 600 * 601 / (1500 * 1501), "· predictive:", mymath.bayes.posterior_predictive(600, 900, 2, 2))
with np.errstate(invalid="ignore"):                               # 0.0 / 0.0 gives nan, with a warning
    print("the direct ratio:", special.beta(602, 900) / special.beta(600, 900), "· exp(f):", math.exp(answer_M04_21f))''',
    record='''wbm.record("M04.21a", 840)
wbm.record("M04.21b", True,
           mistakes={"B(600, 900) est plus petit que le plus petit float positif : regarde ce que renvoie "
                     "special.beta(600, 900)": False})
wbm.record("M04.21c", -1011.5414380705, decimals=2,
           mistakes={"special.betaln donne le logarithme népérien, pas log₁₀": -439.3068647705})
wbm.record("M04.21d", -439.3068647705, decimals=2,
           mistakes={"log₁₀ x = ln x / ln 10": -1011.5414380705})
wbm.record("M04.21e", 600 * 601 / (1500 * 1501), decimals=4,
           mistakes={"le rapport demandé est B(602, 900)/B(600, 900), pas l'inverse": 1500 * 1501 / (600 * 601)})
wbm.record("M04.21f", 1.1447298858, decimals=4,
           mistakes={"special.betaln donne le logarithme ; c'est special.beta qui donne B": 3.1415926536})''',
    note="a) $B(4, 7) = \\frac{3!\\,6!}{10!} = \\frac{1}{840}$. b) à d) $B(600, 900) \\approx 10^{-439{,}3}$, bien "
         "en dessous du plus petit `float64` positif (environ $5 \\times 10^{-324}$) : `special.beta` renvoie 0, alors "
         "que `special.betaln` donne $-1011{,}54$ sans difficulté. e) Le quotient direct vaut $\\frac{0}{0}$, donc "
         "`nan` ; la différence des logarithmes donne $\\frac{600 \\times 601}{1500 \\times 1501} \\approx 0{,}1602$, "
         "comme la formule et `posterior_predictive(600, 900, 2, 2)`. f) $B(\\frac{1}{2}, \\frac{1}{2}) = \\pi$, donc "
         "$\\ln B = \\ln \\pi \\approx 1{,}1447$ : la constante de la loi en U, $\\mathrm{Beta}(\\frac{1}{2}, \\frac{1}{2})$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M04.22 to M04.24)
# ---------------------------------------------------------------------------
M04_22_EXPERIMENT = '''grid_22 = np.linspace(0, 1, 100_001)
posterior_22 = stats.beta(1 + 0, 1 + 3)                  # Beta(1, 1), then 0 success and 3 failures
print("a) MAP (maximum of the density on a grid):", grid_22[np.argmax(posterior_22.pdf(grid_22))])
print("b) posterior mean:", posterior_22.mean())
print("c) MAP with the prior Beta(2, 2):", grid_22[np.argmax(stats.beta(2 + 0, 2 + 3).pdf(grid_22))])
print("d) P(the next two trials are successes):", special.beta(1 + 2, 4) / special.beta(1, 4),
      "· the square of b):", posterior_22.mean() ** 2)
print("e) P(θ < 0.5):", posterior_22.cdf(0.5))'''

M04_22 = Ex(
    "M04.22", "🔮", 1, 10, "Prédire : le MAP avec Beta(1, 1) après trois échecs",
    "prévoir le MAP, la moyenne et la prédictive après des observations toutes identiques, puis le vérifier.",
    "fiche §5 et §6", tracks="C", hypothesis=True,
    body="""Un nouveau bouton « Partager » vient d'être ajouté à une application. On note $\\theta$ la probabilité qu'un utilisateur qui le voit s'en serve, avec l'a priori uniforme $\\mathrm{Beta}(1, 1)$. Les trois premiers utilisateurs ne s'en servent pas. Choisis, pour chaque question :
- a) le MAP de $\\theta$ : (1) 0 ; (2) 0,2 ; (3) 0,25 ; (4) il n'est pas défini ;
- b) la moyenne a posteriori de $\\theta$ : (1) 0 ; (2) 0,2 ; (3) 0,25 ; (4) $\\frac{1}{3}$ ;
- c) le MAP si l'a priori avait été $\\mathrm{Beta}(2, 2)$ : (1) 0 ; (2) 0,2 ; (3) $\\frac{2}{7}$ ; (4) 0,25 ;
- d) avec l'a priori uniforme, la probabilité que les **deux** utilisateurs suivants se servent du bouton : (1) 0 ; (2) 0,04 ; (3) environ 0,067 ; (4) 0,2 ;
- e) avec l'a priori uniforme, la probabilité a posteriori que $\\theta < 0{,}5$ : (1) environ 0,5 ; (2) environ 0,75 ; (3) environ 0,94 ; (4) 1.

**Avant d'exécuter quoi que ce soit**, écris tes cinq prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M04_22a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M04_22b = ...  # b) 1, 2, 3 or 4
prediction_M04_22c = ...  # c) 1, 2, 3 or 4
prediction_M04_22d = ...  # d) 1, 2, 3 or 4
prediction_M04_22e = ...  # e) 1, 2, 3 or 4''',
    check='''for letter, prediction in zip("abcde", [prediction_M04_22a, prediction_M04_22b, prediction_M04_22c,
                                       prediction_M04_22d, prediction_M04_22e]):
    wbm.check(f"M04.22{letter}", prediction)''',
    record='''wbm.record("M04.22a", 1, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M04.22b", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M04.22c", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M04.22d", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M04.22e", 3, prediction=True, choices=[1, 2, 3, 4])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes cinq prédictions écrites."),
        ("todo", guarded(M04_22_EXPERIMENT, ["prediction_M04_22a", "prediction_M04_22b", "prediction_M04_22c",
                                              "prediction_M04_22d", "prediction_M04_22e"],
                         "⏳ Écris d'abord tes cinq prédictions, puis exécute à nouveau.")),
        ("solution", M04_22_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : explique chaque résultat avec la loi a posteriori "
               "$\\mathrm{Beta}(1, 4)$ et sa densité $4(1 - \\theta)^3$. Pourquoi le MAP avec l'a priori uniforme "
               "est-il une mauvaise estimation à annoncer, et que fait l'a priori $\\mathrm{Beta}(2, 2)$ ? Pourquoi "
               "d) n'est-il pas le carré de b) ?"),
    ],
    note="L'a posteriori est $\\mathrm{Beta}(1, 4)$, de densité $4(1 - \\theta)^3$, décroissante : a) son maximum est en "
         "0, comme le maximum de vraisemblance $\\frac{0}{3}$ (« personne ne se servira jamais du bouton »). b) Sa "
         "moyenne vaut $\\frac{1}{5} = 0{,}2$, l'estimation de Laplace. c) $\\mathrm{Beta}(2, 5)$ a pour mode "
         "$\\frac{1}{5}$ : un a priori qui n'aime pas les bords suffit à écarter le MAP de 0. d) "
         "$\\frac{1}{5} \\times \\frac{2}{6} = \\frac{1}{15} \\approx 0{,}067$ (Laplace, mis à jour après le premier "
         "succès), plus que $0{,}2^2 = 0{,}04$ : un succès rend le suivant plus probable. e) $1 - 0{,}5^4 = 0{,}9375$.",
)

M04_23_CHECK = '''NS_23 = [10, 40, 160, 640, 2560]                     # numbers of trials, each with 30 % of successes
with checked("M04.23a"):
    wbm.check("M04.23a", credible_width(3, 10), computed=True)
with checked("M04.23b"):
    wbm.check("M04.23b", credible_width(768, 2560), computed=True)
with checked("M04.23c"):
    wbm.check("M04.23c", credible_width(12, 40) / credible_width(48, 160), computed=True)
with checked("M04.23d"):
    widths_23 = [credible_width(3 * n // 10, n) for n in NS_23]
    wbm.check("M04.23d", np.polyfit(np.log(NS_23), np.log(widths_23), 1)[0], computed=True)
with checked("M04.23e"):
    wbm.check("M04.23e", credible_width(768, 2560) * math.sqrt(2560), computed=True)
with checked("M04.23f"):
    wbm.check("M04.23f", next(n for n in range(10, 5001, 10) if credible_width(3 * n // 10, n) < 0.05),
              computed=True)
with checked("M04.23g"):
    wbm.check("M04.23g", credible_width(3, 10, 30, 70), computed=True)'''

M04_23 = Ex(
    "M04.23", "🔬", 2, 20, "Le posterior se resserre : la largeur de l'intervalle en 1/√n",
    "mesurer comment la largeur d'un intervalle de crédibilité diminue avec le nombre d'essais, et comparer à "
    "$\\frac{1}{\\sqrt{n}}$.", "fiche §6 ; M02c §5", tracks="C",
    body="""Écris `credible_width(k, n, a=1, b=1)`, qui renvoie la **largeur** de l'intervalle de crédibilité à 95 % à queues égales de la proportion, après $k$ succès en $n$ essais à partir de l'a priori $\\mathrm{Beta}(a, b)$, en `float`. La méthode `ppf` d'une loi de `scipy.stats` donne ses quantiles : `stats.beta(a, b).ppf([0.025, 0.975])` renvoie les deux bornes de l'intervalle de $\\mathrm{Beta}(a, b)$ (fiche §6).

La vérification appelle ta fonction pour $n = 10, 40, 160, 640, 2560$ essais, avec chaque fois 30 % de succès, et calcule :
- a) la largeur pour 3 succès en 10 essais (3 décimales) ;
- b) la largeur pour 768 succès en 2 560 essais (4 décimales) ;
- c) le rapport des largeurs pour 40 et pour 160 essais (2 décimales) ;
- d) la pente de la droite qui ajuste $\\ln(\\text{largeur})$ en fonction de $\\ln n$ sur les cinq valeurs de $n$, par `np.polyfit` (2 décimales) ;
- e) la largeur pour 2 560 essais, multipliée par $\\sqrt{2560}$ (2 décimales) ;
- f) le plus petit $n$, multiple de 10 (avec $\\frac{3n}{10}$ succès), pour lequel la largeur passe sous 0,05 (un entier) ;
- g) la largeur pour 3 succès en 10 essais avec l'a priori $\\mathrm{Beta}(30, 70)$ (3 décimales).

Dans ta copie : quand $n$ est multiplié par 4, par combien la largeur est-elle divisée ? Explique d) et e) avec l'écart-type d'une loi Beta, à peu près $\\sqrt{\\frac{p(1 - p)}{n}}$ pour $n$ grand, et la règle « $\\pm 1{,}96$ écart-type » de la loi normale (M02b). Pourquoi la pente de d) n'est-elle pas exactement $-0{,}5$ ? Pourquoi g) est-il bien plus petit que a) ?""",
    todo='''def credible_width(k, n, a=1, b=1):
    """The width of the equal-tailed 95 % credible interval of a proportion, after k successes in n trials from the
    prior Beta(a, b)."""
    raise NotImplementedError("l'a posteriori Beta(a + k, b + n - k), puis ses quantiles 0.025 et 0.975")''',
    check=M04_23_CHECK,
    solution='''def credible_width(k, n, a=1, b=1):
    """The width of the equal-tailed 95 % credible interval of a proportion, after k successes in n trials from the
    prior Beta(a, b)."""
    low, high = stats.beta(a + k, b + n - k).ppf([0.025, 0.975])
    return float(high - low)


NS_23 = [10, 40, 160, 640, 2560]
widths_23 = [credible_width(3 * n // 10, n) for n in NS_23]
print("widths:", [round(w, 4) for w in widths_23])
print("ratios for n × 4:", [round(widths_23[i] / widths_23[i + 1], 3) for i in range(4)])
print("slope:", np.polyfit(np.log(NS_23), np.log(widths_23), 1)[0], "· width × √n:",
      [round(w * math.sqrt(n), 3) for w, n in zip(widths_23, NS_23)], "· 2 × 1.96 × √(0.3 × 0.7):",
      2 * 1.96 * math.sqrt(0.21))
print("f)", next(n for n in range(10, 5001, 10) if credible_width(3 * n // 10, n) < 0.05),
      " g)", credible_width(3, 10, 30, 70))''',
    record='''wbm.record("M04.23a", 0.5004791158, decimals=3,
           mistakes={"un intervalle à 95 % laisse 2,5 % de chaque côté : les quantiles 0,025 et 0,975": 0.4292987154,
                     "l'a posteriori ajoute l'a priori Beta(a, b) aux comptages : Beta(a + k, b + n − k)":
                         0.5252389423})
wbm.record("M04.23b", 0.0354838698, decimals=4,
           mistakes={"un intervalle à 95 % laisse 2,5 % de chaque côté : les quantiles 0,025 et 0,975": 0.0297820239})
wbm.record("M04.23c", 1.9499296222, decimals=2,
           mistakes={"un intervalle à 95 % laisse 2,5 % de chaque côté : les quantiles 0,025 et 0,975": 1.9589221591})
wbm.record("M04.23d", -0.4795102559, decimals=2)
wbm.record("M04.23e", 1.7953575820, decimals=2)
wbm.record("M04.23f", 1290,
           mistakes={"un intervalle à 95 % laisse 2,5 % de chaque côté : les quantiles 0,025 et 0,975": 910})
wbm.record("M04.23g", 0.1700663483, decimals=3,
           mistakes={"l'a posteriori est Beta(a + k, b + n − k) : a reçoit les succès, b les échecs": 0.1753776755})''',
    note="Chaque fois que $n$ est multiplié par 4, la largeur est à peu près divisée par 2 (c : 1,95) : elle décroît "
         "comme $\\frac{1}{\\sqrt{n}}$ (d : pente $-0{,}48$). Pour $n$ grand, l'a posteriori ressemble à une loi "
         "normale d'écart-type $\\sqrt{\\frac{p(1 - p)}{n}}$, donc la largeur vaut environ $2 \\times 1{,}96 \\times "
         "\\sqrt{\\frac{0{,}21}{n}}$ : e) $1{,}795$, contre $2 \\times 1{,}96 \\times \\sqrt{0{,}21} \\approx 1{,}796$. La "
         "pente n'est pas exactement $-0{,}5$ parce que, pour $n = 10$, l'approximation normale est grossière (et "
         "l'a priori pèse encore). f) Diviser la largeur par 2 coûte 4 fois plus d'essais : 1 290 pour passer sous "
         "0,05. g) L'a priori $\\mathrm{Beta}(30, 70)$ vaut 100 essais imaginaires : l'a posteriori "
         "$\\mathrm{Beta}(33, 77)$ est aussi resserré qu'après 110 essais.",
)

M04_24_CHECK = '''with checked("M04.24 vérifications"):
    problems = []
    a_t, b_t, k_t, n_t = 3, 3, 2, 10                                       # another example
    expected = {"l'a priori": stats.beta(a_t, b_t), "la vraisemblance normalisée": stats.beta(k_t + 1, n_t - k_t + 1),
                "l'a posteriori": stats.beta(a_t + k_t, b_t + n_t - k_t)}
    fig, ax = plt.subplots(figsize=(6, 4))
    try:
        created = drawn(draw_update, ax, a_t, b_t, k_t, n_t)
    finally:
        plt.close(fig)                                                     # only the checks below are shown here
    if created:
        problems.append("draw_update ouvre sa propre figure : dessine dans l'axe reçu")
    else:
        curves = []
        for line in ax.get_lines():
            xs = np.asarray(line.get_xdata(), dtype=float)
            ys = np.asarray(line.get_ydata(), dtype=float)
            inside = (xs > 0.005) & (xs < 0.995)
            if inside.sum() >= 50:
                curves.append((line, xs[inside], ys[inside]))
        for name, law in expected.items():
            match = [line for line, xs, ys in curves if np.allclose(ys, law.pdf(xs), rtol=1e-6, atol=1e-6)]
            if not match:
                raw = [line for line, xs, ys in curves
                       if name == "la vraisemblance normalisée" and np.all(ys > 0)
                       and np.std(ys / (xs ** k_t * (1 - xs) ** (n_t - k_t))) < 1e-6 * np.mean(ys / (xs ** k_t * (1 - xs) ** (n_t - k_t)))]
                problems.append(f"{name} : la vraisemblance θ^k (1 − θ)^(n − k) doit être divisée par "
                                "B(k + 1, n − k + 1), pour avoir une aire de 1 comme les deux densités" if raw else
                                f"aucune courbe d'au moins 50 points sur ]0, 1[ n'est la densité de {name}"
                                + (" (a reçoit les succès, b les échecs)" if name == "l'a posteriori" else ""))
            else:
                if match[0].get_drawstyle() != "default" or match[0].get_linestyle() in ("None", "none", "", " "):
                    problems.append(f"{name} : trace une courbe continue (ax.plot), pas des points ni des marches")
                if not match[0].get_label() or match[0].get_label().startswith("_"):
                    problems.append(f"{name} : donne-lui un label, pour la légende")
        if ax.get_legend() is None:
            problems.append("il manque la légende (ax.legend())")
        if not ax.get_xlabel():
            problems.append("nomme l'axe des abscisses (θ)")
    if problems:
        print("❌ Ex M04.24 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M04.24 : l'a priori, la vraisemblance normalisée et l'a posteriori sont justes, avec une légende.")'''

M04_24 = Ex(
    "M04.24", "🎨", 1, 20, "Prior, vraisemblance et posterior sur une même figure",
    "tracer sur un même graphique l'a priori, la vraisemblance normalisée et l'a posteriori d'une mise à jour Beta, "
    "et y lire le compromis entre l'a priori et les données.", "fiche §5 ; R0 (matplotlib)", tracks="C, E",
    body="""Écris `draw_update(ax, a, b, k, n)`, qui dessine dans l'axe `ax`, sur une grille de $\\theta$ d'au moins 200 points entre 0 et 1 :
- la densité de l'a priori $\\mathrm{Beta}(a, b)$ ;
- la vraisemblance de $k$ succès en $n$ essais, **normalisée** pour avoir une aire de 1 : $\\frac{\\theta^k(1 - \\theta)^{n - k}}{B(k + 1,\\ n - k + 1)}$, qui est la densité de $\\mathrm{Beta}(k + 1,\\ n - k + 1)$ ;
- la densité de l'a posteriori $\\mathrm{Beta}(a + k,\\ b + n - k)$ ;

chaque courbe avec un label, puis la légende et le nom de l'axe des abscisses. Ta fonction `mymath.bayes.beta_pdf` ou `stats.beta(a, b).pdf` (qui accepte un array) donnent les densités. Si tu le veux, ajoute en pointillés verticaux les moyennes des trois lois (`ax.axvline`).

Puis trace la mise à jour d'une équipe qui pense qu'un nouveau bouton sera utilisé par 30 % des visiteurs, avec la force de 20 observations (a priori $\\mathrm{Beta}(6, 14)$), et qui observe 9 utilisations sur 15 visites.

Dans ta copie : où se trouve le sommet de l'a posteriori par rapport aux deux autres ? Lequel des deux tire le plus fort, et pourquoi ? Que deviendrait la figure avec 90 utilisations sur 150 visites ?""",
    todo='''def draw_update(ax, a, b, k, n):
    """In ax: the prior Beta(a, b), the normalised likelihood of k successes in n trials, and the posterior, each
    with a label; then the legend and the name of the x axis."""
    raise NotImplementedError("une grille de θ, trois ax.plot avec label=..., ax.legend(), ax.set_xlabel(...)")''',
    check='''with checked("M04.24 figure"):
    fig, ax = plt.subplots(figsize=(7, 4))
    try:
        created = drawn(draw_update, ax, 6, 14, 9, 15)
    except BaseException:
        plt.close(fig)                                     # no empty figure while the function is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M04.24 : draw_update ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans l'axe reçu.")
    else:
        plt.show()''',
    solution='''def draw_update(ax, a, b, k, n):
    """In ax: the prior Beta(a, b), the normalised likelihood of k successes in n trials, and the posterior, each
    with a label; then the legend and the name of the x axis."""
    theta = np.linspace(0, 1, 501)
    laws = [(stats.beta(a, b), f"a priori Beta({a}, {b})", "tab:blue", "--"),
            (stats.beta(k + 1, n - k + 1), f"vraisemblance normalisée ({k} sur {n})", "tab:orange", ":"),
            (stats.beta(a + k, b + n - k), f"a posteriori Beta({a + k}, {b + n - k})", "tab:green", "-")]
    for law, label, color, style in laws:
        ax.plot(theta, law.pdf(theta), style, color=color, linewidth=2, label=label)
        ax.axvline(law.mean(), color=color, linewidth=0.8, alpha=0.6)
    ax.set(xlabel="θ", ylabel="densité", title="Une mise à jour Beta : l'a posteriori entre l'a priori et les données")
    ax.legend(fontsize=8)


fig, ax = plt.subplots(figsize=(7, 4))
draw_update(ax, 6, 14, 9, 15)
plt.show()
print("means: prior", 6 / 20, "· data", 9 / 15, "· posterior", 15 / 35)''',
    after=[("md", "**Vérifications automatiques** (sur un autre exemple ; la figure elle-même se juge à l'œil)."),
           ("code", M04_24_CHECK)],
    note="L'a posteriori $\\mathrm{Beta}(15, 20)$ a sa moyenne $\\frac{15}{35} \\approx 0{,}43$ entre celle de l'a priori "
         "(0,3) et la fréquence observée (0,6), plus près de l'a priori : il vaut 20 observations, les données 15 "
         "(poids $\\frac{15}{35}$ pour les données). L'a posteriori est aussi plus étroit que les deux autres courbes : "
         "il réunit les deux sources d'information. Avec 90 sur 150, les données pèseraient $\\frac{150}{170}$ et "
         "l'a posteriori se collerait à la vraisemblance, autour de 0,56.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M04.25 to M04.27)
# ---------------------------------------------------------------------------
M04_25_MISTAKES = bug_letters_mistakes(
    "ABDF", "CE",
    {"A": "vérifie, pour la mise à jour, quel paramètre reçoit les pièces défectueuses et lequel les bonnes",
     "B": "vérifie que chaque a posteriori est bien divisé par l'évidence",
     "D": "vérifie que chaque estimation utilise sa propre formule : le mode d'une loi Beta n'est pas sa moyenne",
     "F": "vérifie que chaque prédiction tient compte de l'a priori, et pas des seules données"},
    name_correct=False)

M04_25 = Ex(
    "M04.25", "🐛", 1, 15, "Chasse à l'erreur : évidence oubliée, mise à jour à l'envers, mode et moyenne",
    "repérer dans du code les erreurs classiques d'une mise à jour bayésienne, puis calculer les bonnes valeurs.",
    "fiche §1, §5 et §6", tracks="C",
    body="""Un atelier contrôle les pièces d'un fournisseur.
- Sur le taux de défaut $\\theta$ de ses pièces, l'atelier a l'a priori $\\mathrm{Beta}(2, 18)$ ; sur 40 pièces contrôlées, 3 sont défectueuses (une pièce défectueuse est un « succès » pour $\\theta$).
- Par ailleurs, un autre fournisseur est soit **fiable** (a priori 0,8 ; 5 % de pièces défectueuses), soit **douteux** (a priori 0,2 ; 20 % de pièces défectueuses). On tire une de ses pièces : elle est défectueuse.

Un analyste a écrit six lignes, chacune avec un commentaire qui dit ce qu'elle veut calculer. Quatre lignes sont fausses. **Sans exécuter de code**, trouve-les.

```python
b_A = 18 + 3                                   # (A) parameter b of the posterior of θ
p_B = 0.2 * 0.2                                # (B) P(douteux | défectueuse)
p_C = 0.8 * 0.05 + 0.2 * 0.2                   # (C) P(défectueuse), for the second supplier
mode_D = (2 + 3) / (2 + 18 + 40)               # (D) MAP of θ
mean_E = 5 / (5 + 55)                          # (E) posterior mean of θ
pred_F = 3 / 40                                # (F) P(the next piece is defective), for the first supplier
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire (une liste de 6 nombres, 3 décimales).

Dans ta copie : pour chaque ligne fausse, quelle confusion a été faite ? Laquelle des lignes justes aurait permis de corriger (B) ?""",
    todo='''answer_M04_25a = ...  # a) letters, as text
answer_M04_25b = ...  # b) a list of 6 values (3 decimals)''',
    check='''wbm.check("M04.25a", answer_M04_25a)
wbm.check("M04.25b", answer_M04_25b)''',
    solution='''answer_M04_25a = "ABDF"
a_post, b_post = 2 + 3, 18 + 37                       # defective pieces go to a, good ones to b
evidence = 0.8 * 0.05 + 0.2 * 0.2                      # P(défectueuse): total probability
answer_M04_25b = [b_post,                              # (A)
                  0.2 * 0.2 / evidence,                # (B) divided by the evidence
                  evidence,                            # (C)
                  (a_post - 1) / (a_post + b_post - 2),  # (D) the mode
                  a_post / (a_post + b_post),          # (E) the mean
                  a_post / (a_post + b_post)]          # (F) the predictive is the posterior mean
print(answer_M04_25a, [round(v, 4) for v in answer_M04_25b])''',
    record=f'''wbm.record("M04.25a", "ABDF",
           mistakes={M04_25_MISTAKES})
wbm.record("M04.25b", [55, 0.5, 0.08, 4 / 58, 5 / 60, 5 / 60], decimals=3,
           mistakes={{"ce sont les valeurs des lignes ; donne les bonnes valeurs de ce que disent les commentaires":
                         [21, 0.04, 0.08, 5 / 60, 5 / 60, 3 / 40]}})''',
    note="(A) met à l'envers la mise à jour : les 3 pièces défectueuses vont à $a$, les 37 bonnes à $b$, donc "
         "$b = 18 + 37 = 55$. (B) oublie l'évidence : $\\frac{0{,}2 \\times 0{,}2}{0{,}08} = 0{,}5$ ; l'évidence est la "
         "ligne (C), juste. (D) calcule la moyenne $\\frac{5}{60}$ au lieu du mode $\\frac{5 - 1}{5 + 55 - 2} = "
         "\\frac{4}{58} \\approx 0{,}069$. (F) est le maximum de vraisemblance, sans l'a priori ; la probabilité que la "
         "pièce suivante soit défectueuse est la moyenne a posteriori $\\frac{5}{60} \\approx 0{,}083$, la ligne (E), "
         "juste.",
)

M04_26_GIVEN = '''# The naive computation: 0.4 ** 4100 underflows to 0.0, then a huge integer times 0.0 overflows
try:
    naive_26 = math.comb(10_000, 4100) * 0.4 ** 4100 * 0.6 ** 5900
except OverflowError as exc:
    naive_26 = f"OverflowError: {exc}"
print("naive:", naive_26)'''

M04_26_CHECK = '''with checked("M04.26 vérifications"):
    problems = []
    cases = [(3, 10, 0.2), (0, 6, 0.0), (2, 6, 0.0), (7, 7, 1.0), (6, 7, 1.0), (4100, 10_000, 0.4),
             (12, 10, 0.3), (-1, 5, 0.5), (0, 0, 0.7)]
    for k, n, p in cases:
        expected = float(stats.binom.logpmf(k, n, p))
        try:
            got = log_binom_pmf(k, n, p)
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"log_binom_pmf({k}, {n}, {p}) lève {type(exc).__name__} ({exc}) ; attendu {expected:.6g}"
                            + (" : 0 × ln 0 vaut 0 par convention, traite p = 0 et p = 1 à part" if p in (0.0, 1.0)
                               else ""))
            continue
        if not isinstance(got, float):
            problems.append(f"log_binom_pmf({k}, {n}, {p}) doit renvoyer un float de Python, pas {type(got).__name__}")
        elif math.isinf(expected):
            if got != -math.inf:
                problems.append(f"log_binom_pmf({k}, {n}, {p}) : attendu -math.inf (une probabilité nulle), "
                                f"obtenu {got!r}")
        elif not math.isclose(got, expected, rel_tol=1e-9, abs_tol=1e-9):
            problems.append(f"log_binom_pmf({k}, {n}, {p}) : attendu {expected:.10g}, obtenu {got!r}")
    for p in (1.2, -0.1, float("nan")):
        try:
            log_binom_pmf(2, 5, p)
        except ValueError:
            pass
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"p = {p} : lève {type(exc).__name__} ; une probabilité hors de [0, 1] demande une ValueError")
        else:
            problems.append(f"p = {p} est accepté : une probabilité hors de [0, 1] demande une ValueError")
    if problems:
        print("❌ Ex M04.26 : à revoir : " + " ; ".join(problems[:5]) + ("…" if len(problems) > 5 else "."))
    else:
        print("✅ Ex M04.26 : des log-probabilités justes, cas limites compris, même pour n = 10 000.")'''

M04_26_COMPARE = '''# Three hypotheses on p, equal priors: the posteriors from the log-likelihoods, by log-sum-exp
P_26 = [0.38, 0.40, 0.42]
log_like_26 = np.array([log_binom_pmf(4100, 10_000, p) for p in P_26])
print("log-likelihoods:", log_like_26.round(3))
print("posteriors (equal priors):", np.exp(log_like_26 - special.logsumexp(log_like_26)).round(4))'''

M04_26 = Ex(
    "M04.26", "🛠️", 1, 15, "Un calcul stable : comparer des vraisemblances en logarithmes (`math.lgamma`)",
    "écrire une log-probabilité binomiale qui ne déborde jamais, cas limites compris, et s'en servir pour comparer "
    "des hypothèses sur de grands échantillons.", "fiche §7 ; R6", tracks="C",
    body="""Avec 10 000 essais, la probabilité binomiale $\\binom{n}{k}p^k(1 - p)^{n - k}$ ne se calcule pas directement : $p^k$ vaut 0 en `float64`, et $\\binom{n}{k}$ est un entier de plus de 2 900 chiffres. La cellule fournie le montre. Les bibliothèques calculent donc son **logarithme** :

$$\\ln P(K = k) = \\ln\\Gamma(n + 1) - \\ln\\Gamma(k + 1) - \\ln\\Gamma(n - k + 1) + k\\ln p + (n - k)\\ln(1 - p).$$

Écris `log_binom_pmf(k, n, p)`, qui renvoie ce logarithme en `float`, avec ces cas particuliers :
- $k < 0$ ou $k > n$ : la probabilité est nulle, renvoie `-math.inf` ;
- $p = 0$ ou $p = 1$ : `math.log(0)` lève une `ValueError`, mais $0 \\times \\ln 0$ vaut 0 par convention ; la probabilité vaut alors 1 ou 0 selon $k$ ;
- $p$ hors de $[0, 1]$, ou `nan` : une `ValueError` (teste `0 <= p <= 1` au début, ce qui refuse aussi `nan`).

La vérification compare ta fonction à `stats.binom.logpmf` sur neuf cas, puis une dernière cellule compare trois hypothèses sur $p$ pour 4 100 succès en 10 000 essais.

Dans ta copie : écris les trois log-vraisemblances, puis les a posteriori de la dernière cellule à la main, par log-sum-exp (fiche §7). Un écart $d$ entre deux log-vraisemblances fait un rapport $e^{d}$ entre leurs a posteriori (a priori égaux) : que donnent ici l'écart entre la première hypothèse et les deux autres, et l'écart entre les deux dernières ?""",
    given=M04_26_GIVEN,
    todo='''def log_binom_pmf(k, n, p):
    """The natural logarithm of the binomial probability P(K = k) for n trials of probability p; -math.inf when the
    probability is 0. ValueError if p is outside [0, 1]."""
    raise NotImplementedError("math.lgamma pour le coefficient, puis k ln p + (n - k) ln(1 - p), et les cas p = 0 ou 1")''',
    solution='''def log_binom_pmf(k, n, p):
    """The natural logarithm of the binomial probability P(K = k) for n trials of probability p; -math.inf when the
    probability is 0. ValueError if p is outside [0, 1]."""
    if not 0 <= p <= 1:
        raise ValueError(f"a probability is in [0, 1], got p = {p!r}")
    if k < 0 or k > n:
        return -math.inf
    log_coef = math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
    if p == 0:
        return 0.0 if k == 0 else -math.inf           # 0 × ln 0 = 0: only k = 0 is possible
    if p == 1:
        return 0.0 if k == n else -math.inf
    return float(log_coef + k * math.log(p) + (n - k) * math.log1p(-p))


print(log_binom_pmf(4100, 10_000, 0.4), "· scipy:", stats.binom.logpmf(4100, 10_000, 0.4))''',
    after=[("code", M04_26_CHECK),
           ("md", "**Comparer trois hypothèses.** Cette cellule utilise ta fonction (elle affiche une erreur tant "
                  "que `log_binom_pmf` n'est pas écrite)."),
           ("todo", f'with checked("M04.26 comparaison"):\n' + "\n".join("    " + line for line in
                                                                    M04_26_COMPARE.splitlines())),
           ("solution", M04_26_COMPARE)],
    note="Les log-vraisemblances valent environ $-23{,}73$, $-6{,}89$ et $-6{,}87$ : 0,40 et 0,42 sont presque à égale "
         "distance de la fréquence 0,41, et 0,38 en est trois fois plus loin. Avec des a priori égaux, l'a posteriori "
         "de chaque hypothèse est $\\frac{e^{\\ell_j}}{\\sum_i e^{\\ell_i}}$ : environ 0,495 et 0,505 pour 0,40 et "
         "0,42, et un écart de 16,8 entre log-vraisemblances fait un rapport $e^{16{,}8} \\approx 2 \\times 10^7$, "
         "d'où un a posteriori d'environ $2{,}4 \\times 10^{-8}$ pour 0,38. Le cas "
         "$p = 0$ est le piège classique : `k * math.log(p)` lève une erreur même pour $k = 0$, alors que la "
         "probabilité de 0 succès vaut 1.",
)

M04_27_CHECK = '''with checked("M04.27 cohérence"):
    if answer_M04_27b is not ... and answer_M04_27b is not None:
        a_27, b_27 = answer_M04_27b
        low_27, high_27 = stats.beta(a_27, b_27).ppf([0.05, 0.95])
        print(f"Ta loi de b) : intervalle à 90 % à queues égales [{low_27:.4f} ; {high_27:.4f}], "
              f"moyenne {a_27 / (a_27 + b_27):.4f}.")
for letter, answer in zip("abcde", [answer_M04_27a, answer_M04_27b, answer_M04_27c, answer_M04_27d, answer_M04_27e]):
    wbm.check(f"M04.27{letter}", answer)'''

M04_27 = Ex(
    "M04.27", "🏆", 3, 25, "Défi : traduire l'avis d'un expert en une loi Beta (moyenne, écart-type, intervalle)",
    "construire un a priori Beta à partir d'une moyenne et d'un écart-type, puis à partir d'un intervalle, et mesurer "
    "ce qu'il pèse face aux données.", "fiche §4 à §6 ; M02a §6 (quantiles)", tracks="C",
    body="""Avant de lancer une nouvelle ligne de production, l'atelier interroge deux experts sur son taux de défaut $\\theta$.
- Le premier dit : « environ 20 %, avec un écart-type de 5 points ».
- Le second dit : « j'ai 90 % de chances de ne pas me tromper en disant entre 10 % et 32 % », et l'on comprend que chaque queue laisse 5 %.

Traduis chaque avis en une loi Beta, puis calcule :
- a) les paramètres `[a, b]` de la loi Beta de moyenne 0,2 et d'écart-type 0,05 (1 décimale) ; pense à écrire la variance d'une loi Beta avec $m = \\frac{a}{a + b}$ et $s = a + b$ : $\\frac{m(1 - m)}{s + 1}$ ;
- b) les paramètres `[a, b]` de la loi Beta dont l'intervalle à 90 % à queues égales est $[0{,}10 ;\\ 0{,}32]$ (1 décimale) ; aucune formule ne les donne : cherche-les par le calcul, par une recherche sur une grille ou avec `optimize.fsolve(f, x0)` (importé dans la cellule d'outils), qui part du point `x0` et cherche où la fonction `f`, qui renvoie une liste de deux nombres, vaut `[0, 0]` ;
- c) la probabilité $P(0{,}10 \\le \\theta \\le 0{,}32)$ selon la loi de a) (4 décimales) ;
- d) la moyenne a posteriori après 7 pièces défectueuses sur 50, à partir de la loi de b), avec ses paramètres **non arrondis** (3 décimales) ;
- e) le nombre de pseudo-observations $a + b$ de la loi de b), avec ses paramètres non arrondis (1 décimale).

La vérification affiche l'intervalle et la moyenne de ta loi de b), puis vérifie tes réponses.

Dans ta copie : les deux experts sont-ils d'accord ? Lequel est le plus sûr de lui, et comment le lis-tu sur $a + b$ ? Après 50 pièces, que pèse chaque avis face aux données ?""",
    todo='''answer_M04_27a = ...  # a) [a, b] from the mean and the standard deviation (1 decimal)
answer_M04_27b = ...  # b) [a, b] whose equal-tailed 90 % interval is [0.10, 0.32] (1 decimal)
answer_M04_27c = ...  # c) P(0.10 <= θ <= 0.32) for the law of a) (4 decimals)
answer_M04_27d = ...  # d) the posterior mean after 7 defects in 50, from the law of b) (3 decimals)
answer_M04_27e = ...  # e) a + b for the law of b) (1 decimal)''',
    check=M04_27_CHECK,
    solution='''# a) The method of moments: s = a + b solves m(1 − m)/(s + 1) = sd², then a = m s and b = (1 − m) s
m_27, sd_27 = 0.2, 0.05
s_27 = m_27 * (1 - m_27) / sd_27 ** 2 - 1
answer_M04_27a = [m_27 * s_27, (1 - m_27) * s_27]


# b) Two equations, two unknowns: the quantiles 0.05 and 0.95 must be 0.10 and 0.32. The unknowns are the logarithms
# of a and b, so that the solver never tries a negative parameter.
def gaps_27(log_parameters):
    a, b = np.exp(log_parameters)
    low, high = stats.beta(a, b).ppf([0.05, 0.95])
    return [low - 0.10, high - 0.32]


answer_M04_27b = list(np.exp(optimize.fsolve(gaps_27, np.log([5.0, 15.0]))))
a_b, b_b = answer_M04_27b
answer_M04_27c = stats.beta(*answer_M04_27a).cdf(0.32) - stats.beta(*answer_M04_27a).cdf(0.10)
answer_M04_27d = (a_b + 7) / (a_b + b_b + 50)
answer_M04_27e = a_b + b_b
print("a)", [round(v, 3) for v in answer_M04_27a], " b)", [round(float(v), 3) for v in answer_M04_27b],
      " c)", round(float(answer_M04_27c), 4), " d)", round(answer_M04_27d, 4), " e)", round(float(answer_M04_27e), 3))
print("check of b):", stats.beta(a_b, b_b).ppf([0.05, 0.95]), "· mean of b):", a_b / (a_b + b_b))''',
    record='''wbm.record("M04.27a", [12.6, 50.4], decimals=1,
           mistakes={"l'écart-type est 0,05 : la variance est son carré": [0.44, 1.76]})
wbm.record("M04.27b", [6.8673766, 27.4771525], decimals=1,
           mistakes={"un intervalle à 90 % à queues égales laisse 5 % de chaque côté : les quantiles 0,05 et 0,95":
                         [9.6399566, 38.9785348]})
wbm.record("M04.27c", 0.9744893644, decimals=4)
wbm.record("M04.27d", (6.8673766 + 7) / (34.3445291 + 50), decimals=3,
           mistakes={"la moyenne a posteriori part de la loi de b), pas de celle de a)": 19.6 / 113,
                     "garde les paramètres non arrondis de b) pour ce calcul": (6.9 + 7) / (34.4 + 50)})
wbm.record("M04.27e", 34.3445291, decimals=1,
           mistakes={"additionne les paramètres non arrondis de b), pas leurs arrondis": 34.4})''',
    note="a) $s + 1 = \\frac{0{,}2 \\times 0{,}8}{0{,}05^2} = 64$, donc $s = 63$, $a = 12{,}6$ et $b = 50{,}4$. b) "
         "$\\mathrm{Beta}(6{,}9 ;\\ 27{,}5)$ environ, de moyenne 0,20 elle aussi : les deux experts sont d'accord sur "
         "le centre. c) La loi du premier met 97 % de probabilité dans l'intervalle du second, contre 90 % pour la loi "
         "du second : le premier est plus sûr de lui, ce que dit aussi $a + b$ (63 contre 34). d) Avec 50 pièces, les "
         "données pèsent $\\frac{50}{84{,}3} \\approx 0{,}59$ face au second avis, et $\\frac{50}{113} \\approx 0{,}44$ "
         "face au premier : $\\frac{6{,}87 + 7}{84{,}34} \\approx 0{,}164$, contre $\\frac{19{,}6}{113} \\approx 0{,}173$.",
)


PART_A = Part("A", "Ta librairie : la loi Beta, la conjugaison, la prédictive et le MAP",
              "Fiche §4 à §7. Les cinq fonctions de `mymath/bayes.py`, puis la fonction Beta avec `scipy.special`.",
              given=TOOLS, exercises=[M04_18, M04_19, M04_20, M04_21])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §5 et §6. Le MAP face à des données extrêmes, le resserrement de l'a posteriori, la figure d'une "
              "mise à jour.",
              exercises=[M04_22, M04_23, M04_24])

PART_C = Part("C", "Erreurs classiques, calcul stable et défi",
              "Fiche §1, §5 à §7. Quatre erreurs de mise à jour à trouver, une log-probabilité qui ne déborde jamais, "
              "puis l'avis d'un expert à traduire en loi Beta.",
              exercises=[M04_25, M04_26, M04_27])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M04.1 à M04.10, M04.14 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M04 · Bayes, vraisemblance et loi Beta — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m04_bayes_beta/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M04`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M04 · Bayes, vraisemblance et loi Beta — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : formule de Bayes à deux et trois hypothèses, vraisemblance "
               "et maximum de vraisemblance, loi Beta, conjugaison, lissage de Laplace, MAP, intervalle de "
               "crédibilité, log-sum-exp, test A/B.\n"
               "- Écrire les cinq fonctions de `mymath/bayes.py` et les tester, puis utiliser `scipy.special`.\n"
               "- Prédire le MAP face à des données extrêmes, mesurer le resserrement de l'a posteriori, tracer une "
               "mise à jour, chasser des erreurs, calculer en logarithmes, traduire un avis en loi Beta.\n\n"
               "**Rappel express.** $P(H \\mid O) = \\frac{P(O \\mid H)\\,P(H)}{P(O)}$, avec $P(O) = \\sum_j "
               "P(O \\mid H_j)\\,P(H_j)$ ; $\\mathrm{Beta}(a, b)$ : densité $\\frac{\\theta^{a - 1}(1 - \\theta)^{b - 1}}"
               "{B(a, b)}$, moyenne $\\frac{a}{a + b}$, mode $\\frac{a - 1}{a + b - 2}$ ($a, b > 1$), variance "
               "$\\frac{ab}{(a + b)^2(a + b + 1)}$ ; $k$ succès et $n - k$ échecs : $\\mathrm{Beta}(a, b) \\to "
               "\\mathrm{Beta}(a + k,\\ b + n - k)$ ; Laplace : $\\frac{k + 1}{n + 2}$ ; log-sum-exp : $\\ln\\sum_j "
               "e^{\\ell_j} = m + \\ln\\sum_j e^{\\ell_j - m}$, avec $m = \\max_j \\ell_j$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu appliquer la formule de Bayes à plusieurs hypothèses, une fois ou en boucle, et calculer "
               "l'évidence ?\n"
               "2. Sais-tu écrire une vraisemblance, trouver son maximum, et mettre à jour une loi Beta par "
               "conjugaison (moyenne, MAP, prédictive, intervalle) ?\n"
               "3. Sais-tu calculer en logarithmes (log-sum-exp, `lgamma`, `betaln`) quand les probabilités "
               "deviennent minuscules ?\n\n"
               "**La suite** : le chapitre 4 de workbookIA (la règle de Bayes, le posterior sur une grille, la loi "
               "Beta), puis M05a, les nombres en machine et l'encadrement.")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter=CHAPTER) if kind == "exercise" else setup_cell(kind))
    cells += objectives_cell()
    paper = paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO,
                        learner_context="from fractions import Fraction   # Fraction(3, 4) is accepted too, as \"3/4\"")
    if kind == "exercise":                       # the simulation of M04.14, before its answers
        where = next(i for i, cell in enumerate(paper) if cell.source.startswith("**Ex M04.14"))
        paper.insert(where + 1, code(SIMULATION_14))
    cells += paper
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
