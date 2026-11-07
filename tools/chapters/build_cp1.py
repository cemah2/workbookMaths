#!/usr/bin/env python
"""Build the two notebooks of the mock exam CP1 from a single source (used by Claude).

    python tools/chapters/build_cp1.py
    python tools/run_all_notebooks.py checkpoints/partie_1/03_examen_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py checkpoints/partie_1/02_examen_notebook.ipynb

Same mechanism as build_cp0.py: the exam of CP1 is on paper only (01_examen_sujet.md), and the exam notebook is the
check done AFTER the exam; nothing is checked while EXAM_OVER is False, so that « Run all » goes to the end.
Wrong-answer messages state a rule or ask a question, never the calculation that gives the answer nor its last step.
The solutions notebook records the answers, computed from the numbers of the statements (cells tagged `answer`, read
by build_answers.py). The final summary lists the sub-IDs that were not checked (a cell that did not run, or that
stopped on an error such as a decimal comma).

The data are new: none comes from the exercises, fiches, quizzes or flashcards of M02a to M06, from the placement
test, from CP0, from workbookIA chapters 2 to 6, its checkpoint I or its mini-project I (no screening test at
0.90/0.92, no coin with three biases, no (x - 1)² - (y + 2)²/2 nor x² - y², no 3x², no law [0.4, 0.3, 0.2, 0.1], no
c(3 - x) or c/x² density, no Beta(2, 8) nor Beta(3, 7), no log-sum-exp of -1000, 710 or -760, no Poisson of parameter
2.5 or 3, no p = 0.1, no 1 - Φ(2) nor Φ(1) as an answer, no N(10, 4), no Newton on x² - 5 or x² - 10, no point (1, 2)
nor direction (8, 15), no churn, no defective parts, no click rate, no customer service, no thermometers, no bugs per
file, no random-alarm precision, no « 95 times out of 100 » reading of an interval).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import Paper, check_unique_keys, md  # noqa: E402
from nbbuild import badge, code, setup_cell, write_notebook  # noqa: E402

FOLDER = "checkpoints/partie_1"
EXAM = f"{FOLDER}/02_examen_notebook.ipynb"
SOLUTIONS = f"{FOLDER}/03_examen_solutions.ipynb"

F = 'kind="fraction", simplified=True'
FRACTION = "an irreducible fraction, as text"
NATS = "les entropies sont en bits : log₂, pas ln"


def _letter_sets():
    """CP1.11 a: wrong sets of letters, by kind, with messages that name no line (the corrigé explains each line)."""
    from itertools import combinations

    wrong, right = "ACDFG", "BEH"
    missing = {"".join(c) for c in combinations(wrong, 4)}
    extra = {"".join(sorted(wrong + r)) for r in right}
    swapped = {"".join(sorted(set(wrong) - {w} | {r})) for w in wrong for r in right}

    def literal(values):
        return "{" + ", ".join(repr(v) for v in sorted(values)) + "}"

    return (f'{{"il manque une des lignes fausses : il y en a exactement cinq": {literal(missing)}, '
            f'"une des lignes citées est juste : relis-les une par une, avec la règle qu\'elle utilise": '
            f'{literal(extra)}, "une ligne juste est citée à la place d\'une ligne fausse": {literal(swapped)}, '
            f'"ce sont les trois lignes justes ; la question demande les cinq lignes fausses": {right!r}}}')


LETTERS = _letter_sets()

PAPER_CONTEXT = r'''# The answers are computed from the numbers of the statements (01_examen_sujet.md)
import math
from fractions import Fraction


def H(*probs):
    """Entropy in bits of a law given by its probabilities (0 log 0 counts as 0)."""
    return -sum(p * math.log2(p) for p in probs if p > 0)


# CP1.2: the binomial B(12, 0.08), the Poisson law of 1.8 alerts per hour, and the table values of Φ
P_2 = 0.08
PHI_1, PHI_2 = 0.8413, 0.9772

# CP1.3: the joint law of (X, Y), X = 0, 1, 2 (rows), Y = 0, 1 (columns)
JOINT_3 = {(0, 0): 0.1, (0, 1): 0.2, (1, 0): 0.2, (1, 1): 0.1, (2, 0): 0.1, (2, 1): 0.3}
E_X3 = sum(x * p for (x, y), p in JOINT_3.items())
E_Y3 = sum(y * p for (x, y), p in JOINT_3.items())
V_X3 = sum(x * x * p for (x, y), p in JOINT_3.items()) - E_X3 ** 2
V_Y3 = sum(y * y * p for (x, y), p in JOINT_3.items()) - E_Y3 ** 2
COV_3 = sum(x * y * p for (x, y), p in JOINT_3.items()) - E_X3 * E_Y3

# CP1.4: 50 lengths, their sum and the sum of the squared deviations
N_4, SUM_4, SS_4 = 50, 1230, 1911
MEAN_4 = SUM_4 / N_4
S_4 = math.sqrt(SS_4 / (N_4 - 1))                 # ddof = 1
SE_4 = S_4 / math.sqrt(N_4)
P_4 = 18 / 50
SE_P4 = math.sqrt(P_4 * (1 - P_4) / N_4)

# CP1.6: the prior Beta(4, 8), then 7 acceptances out of 30, then 3 out of 10
A_6, B_6 = 4, 8

# CP1.7: Newton on x³ + x − 3 from 1, and a log-sum-exp of very negative scores
NEWTON_7 = [1.0]
for _ in range(2):
    x = NEWTON_7[-1]
    NEWTON_7.append(x - (x ** 3 + x - 3) / (3 * x ** 2 + 1))
SCORES_7 = [-790, -787, -785]
LSE_7 = max(SCORES_7) + math.log(sum(math.exp(s - max(SCORES_7)) for s in SCORES_7))

# CP1.8: f(x, y) = x³ − 6xy + 3y², at the point (1, −1)
GRAD_8 = [3 * 1 ** 2 - 6 * (-1), -6 * 1 + 6 * (-1)]

# CP1.9: the frequencies p, the old model q, and the joint law of (F, Y)
P_9, Q_9 = (0.45, 0.4, 0.15), (0.6, 0.35, 0.05)
CROSS_9 = -sum(p * math.log2(q) for p, q in zip(P_9, Q_9))
H_Y_F9 = 0.4 * H(0.35 / 0.4, 0.05 / 0.4) + 0.6 * H(0.10 / 0.6, 0.50 / 0.6)

# CP1.12: Newton on g(lam) = lam − 1.6 (1 − e^(−lam)) from 1.6, then the root
XBAR_12 = 32 / 20
NEWTON_12 = [1.6]
for _ in range(30):
    lam = NEWTON_12[-1]
    NEWTON_12.append(lam - (lam - XBAR_12 * (1 - math.exp(-lam))) / (1 - XBAR_12 * math.exp(-lam)))
LAM_12 = NEWTON_12[-1]'''

PAPER = [
    Paper("CP1.1", "Intégrales et densité : une aire, une fonction de répartition, un quantile", [
        ("a", "a number (exact, or 3 decimals)", "4.0",
         'decimals=3, mistakes={"par parties : ∫u v\' = [u v] − ∫u\' v, avec le signe moins": 8 * math.e - 4, '
         '"une primitive de e^(x/2) n\'est pas e^(x/2) : dérive ta primitive pour vérifier": math.e + 1, '
         '"évalue aussi chaque crochet en 0 : e⁰ = 1": 0, '
         '"l\'intégration par parties laisse une seconde intégrale à calculer": 4 * math.e}'),
        ("b", FRACTION, "Fraction(1, 4)",
         F + ', mistakes={"intègre les deux termes de x + 1 sur [0 ; 2]": "1/2", '
         '"c\'est l\'aire sous x + 1 ; l\'aire sous f = c (x + 1) doit valoir 1": "4"}'),
        ("c", 'an expression in x (between quotes, "x**2" for x²)', '"(x**2 + 2*x)/8"',
         'kind="expr", variables=("x",), mistakes={"la densité est c (x + 1), pas x + 1 : F(2) doit valoir 1": '
         '"x**2/2 + x", "F est la primitive de f qui vaut 0 en 0, pas f elle-même": "(x + 1)/4", '
         '"F(0) doit valoir 0 : choisis la primitive qui s\'annule en 0": "(x + 1)**2/8"}'),
        ("d", FRACTION, "Fraction(1) - Fraction(3, 8)",
         F + ', mistakes={"c\'est P(X ≤ 1) ; la question demande la probabilité de l\'intervalle ]1 ; 2]": "3/8", '
         '"c\'est une différence de valeurs de la densité, pas de la fonction de répartition": "1/4"}'),
        ("e", "a number (3 decimals)", "-1 + math.sqrt(5)",
         'decimals=3, mistakes={"la médiane vérifie F(m) = 1/2 ; ce n\'est pas l\'espérance": 7 / 6, '
         '"une médiane est une valeur que X peut prendre : dans quel intervalle doit-elle tomber ?": '
         '-1 - math.sqrt(5), '
         '"la densité n\'est pas constante : la médiane n\'est pas le milieu de l\'intervalle": 1, '
         '"résous F(m) = 1/2 avec la fonction de répartition de c), constante comprise": -1 + math.sqrt(2)}'),
        ("f", FRACTION, "Fraction(1, 4) * (Fraction(8, 3) + Fraction(2))",
         F + ', mistakes={"E[X] = ∫ x f(x) dx : la densité n\'est pas constante": "1", '
         '"la densité est c (x + 1), pas x + 1": "14/3"}'),
    ]),
    Paper("CP1.2", "Lois usuelles : binomiale, Poisson, normale", [
        ("a", "a number (4 decimals)", "(1 - P_2) ** 12",
         'decimals=4, mistakes={"aucune erreur : chaque case doit être lue juste": P_2 ** 12}'),
        ("b", "a number (4 decimals)", "1 - (1 - P_2) ** 12 - 12 * P_2 * (1 - P_2) ** 11",
         'decimals=4, mistakes={"« au moins deux » exclut aussi le cas d\'une seule erreur": 1 - (1 - P_2) ** 12, '
         '"l\'erreur unique peut être sur n\'importe laquelle des 12 cases : le coefficient binomial": '
         '1 - (1 - P_2) ** 12 - P_2 * (1 - P_2) ** 11, '
         '"« au moins deux » compte aussi 3, 4… erreurs : passe par l\'événement contraire": '
         '66 * P_2 ** 2 * (1 - P_2) ** 10}'),
        ("c", "a number (4 decimals)", "math.exp(-1.8) * 1.8 ** 2 / 2",
         'decimals=4, mistakes={"la loi de Poisson divise par k!": math.exp(-1.8) * 1.8 ** 2, '
         '"« exactement 2 » ne compte pas les heures à 0 ou 1 alerte": math.exp(-1.8) * (1 + 1.8 + 1.8 ** 2 / 2)}'),
        ("d", "a number (4 decimals)", "1 - math.exp(-1.8 / 3)",
         'decimals=4, mistakes={"le paramètre 1,8 est celui d\'une heure : quel est le nombre moyen d\'alertes '
         'sur une autre durée ?": 1 - math.exp(-1.8), "le paramètre est proportionnel à la durée : quelle fraction '
         'd\'heure font 20 minutes ?": 1 - math.exp(-1.8 / 20), "« au moins une » compte aussi 2, 3… alertes": '
         '0.6 * math.exp(-0.6)}'),
        ("e", "a number (2 decimals)", "PHI_2 - (1 - PHI_1)",
         'decimals=2, mistakes={"12,5 minutes est sous la moyenne : son z est négatif": PHI_2 - PHI_1, '
         '"c\'est la probabilité d\'être en dehors de l\'intervalle": 1 - (PHI_2 - (1 - PHI_1))}'),
        ("f", "a number (2 decimals)", "14 - 1.2816 * 1.5",
         'decimals=2, mistakes={"dépassée par 90 % des batteries : seules 10 % font moins, la valeur est sous la '
         'moyenne": 14 + 1.2816 * 1.5, "90 % au-dessus laisse 10 % en dessous : cherche z tel que Φ(z) = 0,10": '
         '14 - 1.645 * 1.5, "z s\'exprime en écarts-types : repasse en minutes": 14 - 1.2816}'),
    ]),
    Paper("CP1.3", "Un couple de variables : marginales, indépendance, variance d'une somme", [
        ("a", "a list [P(X = 0), P(X = 1), P(X = 2)]", "[0.3, 0.3, 0.4]",
         'decimals=2, mistakes={"la loi de X additionne les deux cases de chaque ligne": [0.1, 0.2, 0.1]}'),
        ("b", "True or False", "False",
         'mistakes={"compare chaque case au produit de ses deux marginales": True}'),
        ("c", "a number (2 decimals)", "COV_3",
         'decimals=2, mistakes={"c\'est E[XY] ; la covariance compare E[XY] à ce que donneraient des variables '
         'indépendantes": COV_3 + E_X3 * E_Y3, '
         '"X et Y ne sont pas indépendantes : calcule E[XY] avec la loi jointe": 0}'),
        ("d", "a number (2 decimals)", "V_X3",
         'decimals=2, mistakes={"c\'est E[X²] ; la variance mesure la dispersion autour de l\'espérance": '
         'V_X3 + E_X3 ** 2, "c\'est l\'espérance ; la variance mesure l\'écart à l\'espérance": E_X3, '
         '"la variance retranche le carré de l\'espérance, pas l\'espérance": V_X3 + E_X3 ** 2 - E_X3}'),
        ("e", "a number (2 decimals)", "V_X3 + V_Y3 + 2 * COV_3",
         'decimals=2, mistakes={"X et Y ne sont pas indépendantes : la variance d\'une somme ajoute 2 Cov(X, Y)": '
         'V_X3 + V_Y3, "relis la formule de la variance d\'une somme : combien de fois la covariance y '
         'apparaît-elle ?": V_X3 + V_Y3 + COV_3, "la variance de Y n\'est pas E[Y²] : Y vaut 0 ou 1, c\'est une '
         'Bernoulli": V_X3 + E_Y3 + 2 * COV_3}'),
    ]),
    Paper("CP1.4", "Estimer une moyenne : erreur type et intervalle de confiance", [
        ("a", "a number (1 decimal)", "MEAN_4",
         'decimals=1, mistakes={"la moyenne divise la somme par n, pas par n − 1": SUM_4 / (N_4 - 1)}'),
        ("b", "a number (3 decimals)", "S_4",
         'decimals=3, mistakes={"ddof = 1 : divise la somme des carrés des écarts par n − 1": '
         'math.sqrt(SS_4 / N_4), "c\'est la variance ; la question demande l\'écart-type": SS_4 / (N_4 - 1)}'),
        ("c", "a number (3 decimals)", "SE_4",
         'decimals=3, mistakes={"l\'erreur type divise l\'écart-type par √n, pas par n": S_4 / N_4, '
         '"l\'erreur type part de l\'écart-type s, pas de la variance": SS_4 / (N_4 - 1) / N_4, '
         '"prends l\'écart-type avec ddof = 1": math.sqrt(SS_4 / N_4) / math.sqrt(N_4), '
         '"l\'erreur type divise par √n, avec n = 50 mesures": S_4 / math.sqrt(N_4 - 1)}'),
        ("d", "[low, high] (2 decimals)", "[MEAN_4 - 1.96 * SE_4, MEAN_4 + 1.96 * SE_4]",
         'decimals=2, mistakes={"l\'intervalle de la moyenne utilise l\'erreur type, pas l\'écart-type des données": '
         '[MEAN_4 - 1.96 * S_4, MEAN_4 + 1.96 * S_4], "à 95 %, le quantile est 1,96": '
         '[MEAN_4 - 1.645 * SE_4, MEAN_4 + 1.645 * SE_4], "un intervalle à 95 % s\'étend de combien d\'erreurs '
         'types de part et d\'autre ?": [MEAN_4 - SE_4, MEAN_4 + SE_4]}'),
        ("e", "a number (2 decimals)", "1.645 * SE_4",
         'decimals=2, mistakes={"l\'intervalle de la moyenne utilise l\'erreur type, pas l\'écart-type des '
         'données": 1.645 * S_4, "à 90 %, le quantile est 1,645": 1.96 * SE_4, '
         '"la demi-largeur est la moitié de la largeur de l\'intervalle": 2 * 1.645 * SE_4}'),
        ("f", "[low, high] (3 decimals)", "[P_4 - 1.96 * SE_P4, P_4 + 1.96 * SE_P4]",
         'decimals=3, mistakes={"l\'erreur type d\'une proportion est la racine de p̂ (1 − p̂) / n": '
         '[P_4 - 1.96 * P_4 * (1 - P_4) / N_4, P_4 + 1.96 * P_4 * (1 - P_4) / N_4], '
         '"l\'erreur type d\'une proportion divise par n, pas par n − 1": '
         '[P_4 - 1.96 * math.sqrt(P_4 * (1 - P_4) / (N_4 - 1)), P_4 + 1.96 * math.sqrt(P_4 * (1 - P_4) / (N_4 - 1))]}'),
    ]),
    Paper("CP1.5", "Un tableau de contingence et des métriques comme probabilités", [
        ("a", FRACTION, "Fraction(45 + 30, 500)",
         F + ', mistakes={"compte toutes les alertes, vraies et fausses": "9/100", '
         '"c\'est la part des vraies chutes ; la question demande la part des alertes": "3/25"}'),
        ("b", FRACTION, "Fraction(45, 45 + 30)",
         F + ', mistakes={"la precision conditionne par l\'alerte : parmi les alertes, la part de vraies chutes": '
         '"3/4"}'),
        ("c", FRACTION, "Fraction(45, 60)",
         F + ', mistakes={"le recall conditionne par la vérité : parmi les vraies chutes, la part qui a donné '
         'l\'alerte": "3/5"}'),
        ("d", FRACTION, "2 * Fraction(3, 5) * Fraction(3, 4) / (Fraction(3, 5) + Fraction(3, 4))",
         F + ', mistakes={"le F1 est la moyenne harmonique de la precision et du recall, pas leur moyenne '
         'arithmétique": "27/40", "relis la formule du F1 : il manque une partie de la fraction": "9/10", '
         '"le produit de la precision et du recall n\'est pas le F1 : relis la formule de la moyenne harmonique": '
         '"9/20"}'),
        ("e", "a number (4 decimals)", "410 / 440",
         'decimals=4, mistakes={"la spécificité conditionne par la vérité (pas de chute), pas par la réponse de la '
         'montre (pas d\'alerte)": 410 / 425, "la spécificité est une probabilité conditionnelle : parmi quels '
         'événements ?": 410 / 500}'),
        ("f", "True or False", "False",
         'mistakes={"compare P(alerte et chute) au produit P(alerte) × P(chute)": True}'),
    ]),
    Paper("CP1.6", "Bayes et la loi Beta : une mise à jour conjuguée", [
        ("a", FRACTION, "Fraction(A_6, A_6 + B_6)",
         F + ', mistakes={"la moyenne de Beta(a, b) n\'est pas a/b : relis sa formule (M04 §4)": "1/2", '
         '"c\'est le mode de la loi ; la question demande sa moyenne": "3/10"}'),
        ("b", "[a, b]", "[A_6 + 7, B_6 + 23]",
         'mistakes={"b reçoit le nombre d\'échecs, pas le nombre d\'essais": [11, 38], '
         '"a reçoit les succès, b les échecs": [31, 11], '
         '"ajoute les succès et les échecs aux paramètres de l\'a priori": [7, 23]}'),
        ("c", FRACTION, "Fraction(A_6 + 7, A_6 + B_6 + 30)",
         F + ', mistakes={"c\'est la fréquence observée ; la moyenne a posteriori tient compte aussi de '
         'l\'a priori": "7/30", "c\'est le mode ; la question demande la moyenne": "1/4"}'),
        ("d", FRACTION, "Fraction(A_6 + 7 - 1, A_6 + B_6 + 30 - 2)",
         F + ', mistakes={"c\'est la moyenne ; le MAP est le mode de la loi a posteriori": "11/42", '
         '"le MAP tient compte de l\'a priori : c\'est le mode de la loi a posteriori": "7/30"}'),
        ("e", FRACTION, "Fraction(A_6 + 10, A_6 + B_6 + 40)",
         F + ', mistakes={"l\'a priori de la deuxième mise à jour est l\'a posteriori de la première": "7/22", '
         '"ajoute aussi les 10 nouvelles propositions": "11/42", '
         '"b reçoit le nombre d\'échecs, pas le nombre d\'essais": "14/55"}'),
        ("f", "a number (4 decimals)", "14 / 52 * 15 / 53",
         'decimals=4, mistakes={"la deuxième acceptation se calcule avec la loi mise à jour par la première, pas '
         'avec la même moyenne": (14 / 52) ** 2, "la question demande que les deux soient acceptées": 14 / 52}'),
    ]),
    Paper("CP1.7", "Taylor, Newton et un calcul stable", [
        ("a", 'an expression in x (between quotes)', '"2 + x/4 - x**2/64"',
         'kind="expr", variables=("x",), mistakes={"le terme d\'ordre 2 est f\'\'(0) x² / 2 : n\'oublie pas le 2": '
         '"2 + x/4 - x**2/32", "ce sont les coefficients de √(1 + x) : ici la racine porte sur 4 + x": '
         '"2 + x/2 - x**2/8", "l\'ordre 2 ajoute un terme en x²": "2 + x/4", '
         '"la dérivée seconde de √(4 + x) est négative": "2 + x/4 + x**2/64"}'),
        ("b", "a number (4 decimals)", "2 + 0.4 / 4 - 0.4 ** 2 / 64",
         'decimals=4, mistakes={"l\'ordre 2 ajoute un terme en x²": 2.1, '
         '"le terme d\'ordre 2 est f\'\'(0) x² / 2 : n\'oublie pas le 2": 2 + 0.4 / 4 - 0.4 ** 2 / 32, '
         '"c\'est la valeur exacte ; la question demande celle que donne le polynôme": math.sqrt(4.4)}'),
        ("c", "a number (2 decimals)", "NEWTON_7[1]",
         'decimals=2, mistakes={"le pas de Newton est f(x)/f\'(x), pas l\'inverse": 1 - 4 / (-1), '
         '"x₁ = x₀ − f(x₀)/f\'(x₀) : attention au signe de f(1)": 0.75}'),
        ("d", "a number (4 decimals)", "NEWTON_7[2]",
         'decimals=4, mistakes={"c\'est (presque) la racine ; la question demande le deuxième pas, seulement": '
         '1.213411662762183}'),
        ("e", "a number (3 decimals)", "LSE_7",
         'decimals=3, mistakes={"le log-sum-exp est un peu plus grand que le plus grand des scores": -785, '
         '"le terme du plus grand score compte aussi : e⁰ = 1 dans la somme des écarts": '
         '-785 + math.log(math.exp(-2) + math.exp(-5))}'),
        ("f", "a number (4 decimals)", "math.exp(-785 - LSE_7)",
         'decimals=4, mistakes={"c\'est la probabilité d\'un autre score : relis lequel est −785": '
         'math.exp(-787 - LSE_7), "la softmax prend l\'exponentielle des scores avant de normaliser": '
         '785 / (790 + 787 + 785)}'),
    ]),
    Paper("CP1.8", "Gradient, dérivée directionnelle et point critique", [
        ("a", "[df/dx, df/dy]", "GRAD_8",
         'mistakes={"∂f/∂x dérive aussi −6xy, où y est une constante": [3, -12], '
         '"le gradient est [∂f/∂x, ∂f/∂y], dans cet ordre": [-12, 9], '
         '"attention aux signes : y vaut −1": [-3, 0]}'),
        ("b", FRACTION, "Fraction(GRAD_8[0] * 20 + GRAD_8[1] * 21, 29)",
         F + ', mistakes={"une dérivée directionnelle se calcule avec un vecteur de norme 1": "-72"}'),
        ("c", "a number", "math.hypot(*GRAD_8)",
         'decimals=3, mistakes={"la plus grande pente est la norme du gradient, pas son carré": 225, '
         '"la norme d\'un vecteur n\'est pas la somme des valeurs absolues de ses coordonnées": 21}'),
        ("d", "[x1, y1, x2, y2]", "[0, 0, 2, 2]",
         'mistakes={"range les points dans l\'ordre des x croissants": [2, 2, 0, 0]}'),
        ("e", "1, 2 or 3", "3",
         'choices=[1, 2, 3], mistakes={"calcule f_xx f_yy − (f_xy)² en ce point : son signe décide": 1}'),
        ("f", "a number", "2 ** 3 - 6 * 2 * 2 + 3 * 2 ** 2",
         'mistakes={"c\'est la valeur au premier point critique ; la question porte sur le second": 0, '
         '"attention au signe du terme −6xy": 44}'),
    ]),
    Paper("CP1.9", "Entropie, information mutuelle et KL", [
        ("a", "a number (3 decimals)", "H(*P_9)",
         f'decimals=3, mistakes={{"{NATS}": H(*P_9) * math.log(2)}}'),
        ("b", "a number (3 decimals)", "CROSS_9",
         'decimals=3, mistakes={"H(p, q) pondère par p les longueurs −log₂ q": '
         '-sum(q * math.log2(p) for p, q in zip(P_9, Q_9)), "c\'est l\'entropie de q ; la question demande la '
         f'cross-entropy": H(*Q_9), "{NATS}": CROSS_9 * math.log(2)}}'),
        ("c", "a number (3 decimals)", "CROSS_9 - H(*P_9)",
         'decimals=3, mistakes={"KL(p ‖ q) pondère par p : l\'ordre des deux lois compte": '
         'sum(q * math.log2(q / p) for p, q in zip(P_9, Q_9)), "une divergence KL est positive ou nulle": '
         f'H(*P_9) - CROSS_9, "{NATS}": (CROSS_9 - H(*P_9)) * math.log(2)}}'),
        ("d", FRACTION, "Fraction(35, 40)",
         F + ', mistakes={"P(question | F = 1) se lit dans la ligne F = 1, pas dans la colonne « question »": '
         '"7/9", "c\'est la probabilité jointe P(question et F = 1)": "7/20"}'),
        ("e", "a number (2 decimals)", "H_Y_F9",
         'decimals=2, mistakes={"H(Y | F) est une moyenne des entropies des lignes, pondérée par P(F), pas leur '
         'somme": H(0.875, 0.125) + H(1 / 6, 5 / 6), "c\'est H(F) ; la question demande H(Y | F)": H(0.4, 0.6), '
         '"c\'est H(F | Y) : la variable connue est à droite de la barre": '
         '0.45 * H(35 / 45, 10 / 45) + 0.55 * H(5 / 55, 50 / 55), '
         f'"{NATS}": H_Y_F9 * math.log(2)}}'),
        ("f", "a number (2 decimals)", "H(0.45, 0.55) - H_Y_F9",
         'decimals=2, mistakes={"c\'est H(Y | F), l\'incertitude qui reste ; la question demande ce que F '
         'apprend sur Y": H_Y_F9, '
         '"garde au moins 3 décimales dans H(Y) et H(Y | F) avant de les soustraire": 0.38, '
         f'"{NATS}": (H(0.45, 0.55) - H_Y_F9) * math.log(2)}}'),
    ]),
    Paper("CP1.11", "Corriger une copie : cinq erreurs (les lettres seulement)", [
        ("a", 'the letters, as text (like "ABCDE")', '"ACDFG"', f"mistakes={LETTERS}"),
    ]),
    Paper("CP1.12", "Problème de synthèse : estimer un paramètre de bout en bout", [
        ("a", "a number (3 decimals)", "2 * math.exp(-2) / (1 - math.exp(-2))",
         'decimals=3, mistakes={"le journal ne garde que les jours qui ont au moins un signalement : divise par '
         '1 − e^(−λ)": 2 * math.exp(-2)}'),
        ("b", 'an expression in lam (between quotes, exp(-lam) for e^(−λ))', '"32/lam - 20/(1 - exp(-lam))"',
         'kind="expr", variables=("lam",), mistakes={"dérive aussi le terme −20 ln(1 − e^(−λ))": "32/lam - 20", '
         '"la dérivée de ln(1 − e^(−λ)) est e^(−λ) / (1 − e^(−λ)) : attention au signe": '
         '"32/lam - 20 + 20*exp(-lam)/(1 - exp(-lam))", "la log-vraisemblance somme les 20 jours": '
         '"1.6/lam - 1/(1 - exp(-lam))"}'),
        ("c", "a number (3 decimals)", "NEWTON_12[1]",
         'decimals=3, mistakes={"un pas de Newton retranche g(λ)/g\'(λ)": '
         '1.6 + (1.6 - XBAR_12 * (1 - math.exp(-1.6))) / (1 - XBAR_12 * math.exp(-1.6)), '
         '"la dérivée de −1,6 (1 − e^(−λ)) est −1,6 e^(−λ)": '
         '1.6 - (1.6 - XBAR_12 * (1 - math.exp(-1.6))) / (1 + XBAR_12 * math.exp(-1.6))}'),
        ("d", "a number (3 decimals)", "NEWTON_12[2]",
         'decimals=3, mistakes={"le deuxième pas part de λ₁, avec g et g\' recalculés en λ₁": NEWTON_12[1]}'),
        ("e", "a number (3 decimals)", "LAM_12",
         'decimals=3, mistakes={"la moyenne des jours du journal ne compte pas les jours sans signalement : résous '
         'g(λ) = 0": XBAR_12, "continue les pas jusqu\'à ce que les trois décimales ne bougent plus": NEWTON_12[2]}'),
        ("f", "True or False", "True",
         'mistakes={"calcule ℓ\'(1) avec ton expression de b)": False}'),
        ("g", "a number (3 decimals)", "math.exp(-LAM_12)",
         'decimals=3, mistakes={"la proportion de jours sans signalement se calcule avec le paramètre estimé, pas '
         'avec la moyenne observée": math.exp(-XBAR_12)}'),
        ("h", "[low, high] (2 decimals)", "[LAM_12 - 1.96 * 0.28, LAM_12 + 1.96 * 0.28]",
         'decimals=2, mistakes={"l\'intervalle est centré sur l\'estimation de λ, pas sur la moyenne observée": '
         '[XBAR_12 - 1.96 * 0.28, XBAR_12 + 1.96 * 0.28], "un intervalle à 95 % s\'étend de combien '
         'd\'écarts-types de part et d\'autre ?": [LAM_12 - 0.28, LAM_12 + 0.28], '
         '"0,28 est déjà l\'écart-type de l\'estimation : ne le divise pas par √n": '
         '[LAM_12 - 1.96 * 0.28 / math.sqrt(20), LAM_12 + 1.96 * 0.28 / math.sqrt(20)]}'),
    ]),
]

EXPECTED = [f"{p.id}{letter}" for p in PAPER for letter, *_ in p.subs]

HELPERS = r'''EXAM_OVER = False   # set it to True once your exam is finished, then run the cells below

RESULTS = {}        # sub-ID -> result of wbm.check
_REMINDED = []      # the full reminder is printed once, then a short one


def exam_over():
    """True once the exam is finished; otherwise print a reminder (and the cell checks nothing)."""
    if not EXAM_OVER:
        print("⏸️ Rien n'est vérifié (EXAM_OVER vaut False)." if _REMINDED else
              "⏸️ Vérification après l'examen : passe EXAM_OVER à True dans cette cellule, puis exécute-la.")
        _REMINDED.append(True)
        return False
    if "wbm" not in globals():
        print("⚠️ Exécute d'abord la cellule de configuration, tout en haut du notebook.")
        return False
    return True'''

SUMMARY = r'''# Summary of the automatic checks
import re

EXPECTED = ''' + repr(EXPECTED) + r'''


def natural(sub_id):
    """CP1.2a before CP1.10a: the question number as a number, then the letter."""
    number, letter = re.match(r"CP1\.(\d+)(.*)", sub_id).groups()
    return int(number), letter


if exam_over():
    done = {k: r for k, r in RESULTS.items() if r.status != "pending"}
    right = sorted((k for k, r in done.items() if r), key=natural)
    wrong = sorted((k for k, r in done.items() if not r), key=natural)
    pending = sorted((k for k, r in RESULTS.items() if r.status == "pending"), key=natural)
    missing = [k for k in EXPECTED if k not in RESULTS]
    print(f"Réponses vérifiées : {len(right)} juste(s) sur {len(done)} ; pas remplies : {len(pending)}.")
    if wrong:
        print("À revoir avec le corrigé :", ", ".join(wrong))
    if missing:
        print("⚠️ Pas vérifiées (cellule pas exécutée, ou arrêtée par une erreur, par exemple une virgule décimale) :",
              ", ".join(missing))
    print("Note ensuite ta copie avec le barème de 03_examen_corrige.md : il donne aussi les points des démarches, "
          "des justifications et des questions rédigées, que cette vérification ne voit pas.")'''

INTRO = r'''## Après l'examen : vérification automatique

**Ne commence qu'une fois ta copie terminée**, examen rendu. Ce notebook vérifie les réponses que tu as écrites sur ta feuille, question par question : ✅ juste, ❌ faux (avec une piste), ⏳ pas rempli. Il ne note pas : les démarches, les justifications, le quiz CP1.Q1, la démonstration CP1.10 et les corrections de CP1.11 b) se corrigent avec `03_examen_corrige.md`, qui donne aussi le barème.

1. Passe `EXAM_OVER` à `True` dans la cellule ci-dessous, puis exécute-la.
2. Reporte chaque réponse de ta feuille : **la valeur** que tu as écrite, pas un nouveau calcul (sinon tu ne vérifies plus ta copie). Laisse `...` pour une question que tu n'as pas faite.
3. Les formes d'écriture : en Python, le séparateur décimal est un **point** (`2.5`) : une virgule (`0,023`) arrête toute la cellule, et aucune réponse de la question n'est vérifiée ; une fraction et une expression s'écrivent **entre guillemets** (`"-7/3"`, `"2*x**2 - 1"`, `"exp(-lam)"`) ; une liste entre crochets, sans guillemets (`[-1.5, 4]`) ; vrai ou faux par `True` ou `False`.
4. Le bilan, à la fin, dit aussi quelles réponses n'ont pas été vérifiées.'''


def paper_cell(kind: str, paper: Paper) -> list:
    """One question: the answers and a guarded wbm.check (exam), or the wbm.record cell (solutions)."""
    cells = [md(f"**{paper.id} — {paper.title}**")]
    stem = f"answer_{paper.id.replace('.', '_')}"
    if kind == "exercise":
        lines = [f"# {paper.id}: the values written on your answer sheet"]
        lines += [f"{stem}{letter} = ...  # {letter}) {hint}" for letter, hint, _, _ in paper.subs]
        names = ", ".join(f"{stem}{letter}" for letter, *_ in paper.subs)
        lines += ["", "if exam_over():",
                  f"    for letter, answer in zip(\"{paper.letters}\", [{names}]):",
                  f"        RESULTS[f\"{paper.id}{{letter}}\"] = wbm.check(f\"{paper.id}{{letter}}\", answer)"]
        cells.append(code("\n".join(lines)))
    else:
        lines = []
        for letter, _, expr, options in paper.subs:
            args = f", {options}" if options else ""
            lines.append(f'wbm.record("{paper.id}{letter}", {expr}{args})')
        source = "\n".join(lines)
        check_unique_keys(source, paper.id)
        cells.append(code(source, tags=["answer"]))
    return cells


def header_cells(kind: str) -> list:
    rel = EXAM if kind == "exercise" else SOLUTIONS
    if kind == "exercise":
        title = "# CP1 · Examen blanc de la partie I — vérification de ta copie"
        how = ("L'examen se fait **sur papier** (`01_examen_sujet.md`, 124 minutes, fiches fermées). Ce notebook ne "
               "sert qu'**après** : il vérifie les réponses chiffrées de ta copie. Ses cellules ne vérifient rien tant "
               "que `EXAM_OVER` vaut `False`, et « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli (⏸️).\n\n"
               "> Travaille dans **ta copie** (`mon_travail/checkpoints/partie_1/02_examen_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py CP1`) : ce fichier-ci est mis à jour par Claude. Sur Colab, le badge "
               "ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme l'explique "
               "`00_setup/COLAB.md` §2.")
    else:
        title = "# CP1 · Examen blanc de la partie I — solutions (notebook exécuté)"
        how = ("L'enregistrement des réponses que vérifie le notebook de l'examen (cellules marquées `answer`, "
               "récoltées par `tools/build_answers.py`), calculées à partir des nombres du sujet ; les erreurs "
               "classiques reçoivent un message qui dit où chercher. Le corrigé détaillé et le barème sont dans "
               "`03_examen_corrige.md`.")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell("demo"))
    if kind == "exercise":
        cells.append(md(INTRO))
        cells.append(code(HELPERS))
        for paper in PAPER:
            cells += paper_cell(kind, paper)
        cells.append(md("## Bilan"))
        cells.append(code(SUMMARY))
        cells.append(md("**Ce que cette vérification ne voit pas** : les démarches et les justifications ; le quiz "
                        "CP1.Q1 ; la démonstration CP1.10 ; les corrections de CP1.11 b) (seules les lettres de a) sont "
                        "vérifiées). Tout cela se corrige avec `03_examen_corrige.md`. Remplis ensuite le tableau de "
                        "ta note, à la fin de ta copie, puis fais la remédiation du corrigé."))
    else:
        cells.append(md("## Les réponses vérifiées après l'examen"))
        cells.append(code(PAPER_CONTEXT))
        for paper in PAPER:
            cells += paper_cell(kind, paper)
    return cells


def main() -> int:
    write_notebook(EXAM, build("exercise"))
    write_notebook(SOLUTIONS, build("solution"))
    print(f"✅ {EXAM} and {SOLUTIONS} written ({len(PAPER)} questions, {len(EXPECTED)} checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
