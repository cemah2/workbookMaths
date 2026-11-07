#!/usr/bin/env python
"""Build the two notebooks of chapter M06 from a single source (used by Claude).

    python tools/chapters/build_m06.py
    python tools/run_all_notebooks.py chapitres/m06_information/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m06_information/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M06.1 to M06.9, 🔗 M06.12 and M06.13); parts A to C are the notebook
exercises. Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it. The
laws and tables are new: none is a test case of tests/test_m06_info.py, an example of the fiche, or an example of
workbookIA 6 (no coin, no die, no letters or words, no weather, no Morse, no Huffman code or law, no rhubarb, no
law of entropy 1.75 such as [1/2, 1/4, 1/8, 1/8], no (1/2, 1/4, 1/4), no (1/2, 1/2, 0) nor (0.7, 0.2, 0.1), no
p = [0.8, 0.2] against the uniform law, no 0.7 or 0.01 log loss, no log loss of 4 examples and 3 classes, no h(0.2),
h(0.1) or h(0.25), no guess-the-number story), nor of its later chapters (no 8-example node split into (3, 1) and
(1, 3), no 50/30/20 leaf, no KL of (0.5, 0.5) and (0.25, 0.75)).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402,F401
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M06"
FOLDER = "chapitres/m06_information"

F = 'kind="fraction", simplified=True'
NATS = "la question demande des nats : ln, pas log₂"
BITS = "la question demande des bits : log₂ x = ln x / ln 2, pas ln"
ORDER = "l'écart de Jensen est E[f(X)] − f(E[X]), dans cet ordre"
POSITIVE = "l'information d'un événement de probabilité p < 1 est positive : c'est −log₂ p"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
YX = "ta valeur est H(Y | X) ; la question demande H(X | Y), l'entropie de X quand Y est connue"
IXY = "ta valeur est I(X ; Y) ; la question demande H(X | Y)"
ROW = "divise les cases de la ligne par P(X = {x}) : la loi conditionnelle doit sommer à 1"
ROW_THEN = "divise d'abord les cases de la ligne par P(X = {x}), puis calcule l'entropie de cette loi"
MEAN = "H(Y | X) est une moyenne des entropies des lignes, pondérée par P(X = x), pas leur somme"
WEIGHT = "pondère l'entropie de chaque ligne par sa probabilité P(X = x)"
CONVERT_NATS = "la question demande des nats : convertis les bits en nats (fiche §1)"
NAT_SMALLER = "1 nat vaut plus qu'un bit : le nombre de nats est plus petit que le nombre de bits"

PAPER = [
    Paper("M06.1", "L'information d'événements et l'entropie d'une loi à quatre issues", [
        ("a", "a list (2 decimals)", "[-math.log2(0.55), -math.log2(0.35), -math.log2(0.07), -math.log2(0.03)]",
         f'''decimals=2, mistakes={{"{BITS}": [-math.log(0.55), -math.log(0.35), -math.log(0.07), -math.log(0.03)], '''
         f'''"{POSITIVE}": [math.log2(0.55), math.log2(0.35), math.log2(0.07), math.log2(0.03)]}}'''),
        ("b", "a number (3 decimals)", "H1",
         '''decimals=3, mistakes={"l'entropie est la moyenne des informations, pondérée par les probabilités, pas '''
         '''leur somme": INFO_SUM_1, "l'entropie pondère chaque information par la probabilité de son issue, pas par '''
         '''1/4": INFO_SUM_1 / 4, '''
         f'''"{BITS}": H1 * math.log(2)}}'''),
        ("c", "a number (2 decimals)", "H1 * math.log(2)",
         f'''decimals=2, mistakes={{"{CONVERT_NATS}": H1, "{NAT_SMALLER}": H1 / math.log(2)}}'''),
        ("d", "a number (3 decimals)", "-math.log2(0.55) - math.log2(0.03)",
         '''decimals=3, mistakes={"les informations d'événements indépendants s'additionnent": '''
         '''math.log2(0.55) * math.log2(0.03), "la probabilité de deux événements indépendants est le produit des '''
         '''probabilités, pas leur somme": -math.log2(0.58)}'''),
        ("e", "a number (3 decimals)", "H(0.55, 0.35, 0.1)",
         '''decimals=3, mistakes={"c'est l'entropie de la loi à quatre issues : regroupe d'abord les deux erreurs '''
         '''en une seule issue, de probabilité la somme des deux": H1}'''),
        ("f", "a number (3 decimals)", "2 * H1",
         '''decimals=3, mistakes={"c'est l'entropie d'une seule requête : le couple des codes de deux requêtes a '''
         '''seize issues possibles": H1}'''),
    ]),

    Paper("M06.2", "L'entropie maximale : comparer des lois à quatre issues", [
        ("a", "a number (3 decimals)", "H(0.45, 0.3, 0.15, 0.1)",
         f'''decimals=3, mistakes={{"{BITS}": H(0.45, 0.3, 0.15, 0.1) * math.log(2)}}'''),
        ("b", "a number (3 decimals)", "H(0.4, 0.3, 0.15, 0.15)",
         f'''decimals=3, mistakes={{"{BITS}": H(0.4, 0.3, 0.15, 0.15) * math.log(2)}}'''),
        ("c", "a number (2 decimals)", "H(0.45, 0.3, 0.25)",
         f'''decimals=2, mistakes={{"{BITS}": H(0.45, 0.3, 0.25) * math.log(2)}}'''),
        ("d", "an integer", "2",
         '''mistakes={"l'entropie maximale sur n issues n'est pas n : relis « Ses valeurs extrêmes » (fiche §2)": 4}'''),
        ("e", "a number (2 decimals)", "HMAX_2",
         '''decimals=2, mistakes={"la contrainte fixe la probabilité de la première issue : la loi uniforme sur '''
         '''quatre issues ne la respecte pas": 2}'''),
        ("f", "a number (2 decimals)", "HMAX_2 * math.log(2)",
         f'''decimals=2, mistakes={{"{CONVERT_NATS}": HMAX_2, "{NAT_SMALLER}": HMAX_2 / math.log(2)}}'''),
    ]),

    Paper("M06.3", "Entropies conjointe et conditionnelle d'un tableau 2 × 3", [
        ("a", "a number (3 decimals)", "H(0.4, 0.18, 0.21, 0.21)",
         '''decimals=3, mistakes={"H(X, Y) se calcule sur les cases du tableau : elle ne vaut H(X) + H(Y) que pour '''
         '''des variables indépendantes": H(0.4, 0.6) + H(0.58, 0.21, 0.21)}'''),
        ("b", "a number (3 decimals)", "H(0.3, 0.35, 0.35)",
         f'''decimals=3, mistakes={{"{ROW.format(x="payant")}": H(0.18, 0.21, 0.21), '''
         f'''"{ROW_THEN.format(x="payant")}": H(0.18, 0.21, 0.21) / 0.6}}'''),
        ("c", "a number (3 decimals)", "0.6 * H(0.3, 0.35, 0.35)",
         '''decimals=3, mistakes={"H(Y | X) est une moyenne sur les valeurs de X, pondérée par leurs probabilités : '''
         '''la ligne « gratuit » compte aussi": H(0.3, 0.35, 0.35), '''
         f'''"{WEIGHT}": H(0.3, 0.35, 0.35) / 2, "ta valeur est H(X) ; la question demande H(Y | X)": H(0.4, 0.6)}}'''),
        ("d", "a number (2 decimals)", "H(0.58, 0.21, 0.21)",
         '''decimals=2, mistakes={"ta valeur est H(X) ; Y est la variable des colonnes": H(0.4, 0.6)}'''),
        ("e", "a number (2 decimals)", "H(0.4, 0.18, 0.21, 0.21) - H(0.58, 0.21, 0.21)",
         f'''decimals=2, mistakes={{"{YX}": 0.6 * H(0.3, 0.35, 0.35), '''
         f'''"{IXY}": H(0.4, 0.6) - (H(0.4, 0.18, 0.21, 0.21) - H(0.58, 0.21, 0.21))}}'''),
        ("f", "a number (2 decimals)", "H(0.3, 0.35, 0.35) - H(0.58, 0.21, 0.21)",
         '''decimals=2, mistakes={"l'écart demandé est H(Y | X = payant) moins H(Y), dans cet ordre": '''
         '''H(0.58, 0.21, 0.21) - H(0.3, 0.35, 0.35)}'''),
    ]),

    Paper("M06.4", "La règle de la chaîne de l'entropie, vérifiée", [
        ("a", "an integer", "1", ''),
        ("b", "a number (3 decimals)", "H(0.7, 0.3)",
         f'''decimals=3, mistakes={{"{ROW.format(x="e-mail")}": H(0.35, 0.15), '''
         f'''"{ROW_THEN.format(x="e-mail")}": H(0.35, 0.15) / 0.5}}'''),
        ("c", "a number (3 decimals)", "H(0.4, 0.6)",
         f'''decimals=3, mistakes={{"{ROW.format(x="SMS")}": H(0.2, 0.3), '''
         f'''"{ROW_THEN.format(x="SMS")}": H(0.2, 0.3) / 0.5}}'''),
        ("d", "a number (3 decimals)", "(H(0.7, 0.3) + H(0.4, 0.6)) / 2",
         f'''decimals=3, mistakes={{"{MEAN}": H(0.7, 0.3) + H(0.4, 0.6)}}'''),
        ("e", "a number (3 decimals)", "H(0.35, 0.15, 0.2, 0.3)",
         '''decimals=3, mistakes={"H(X, Y) ne vaut H(X) + H(Y) que si X et Y sont indépendantes : calcule-la sur '''
         '''les quatre cases": 1 + H(0.55, 0.45)}'''),
        ("f", "a number (3 decimals)", "H(0.55, 0.45)",
         '''decimals=3, mistakes={"la loi de Y : additionne les cases de chaque colonne": 1}'''),
        ("g", "a number (3 decimals)", "H(0.35, 0.15, 0.2, 0.3) - H(0.55, 0.45)",
         f'''decimals=3, mistakes={{"{YX}": (H(0.7, 0.3) + H(0.4, 0.6)) / 2, '''
         f'''"{IXY}": 1 - (H(0.35, 0.15, 0.2, 0.3) - H(0.55, 0.45))}}'''),
    ]),

    Paper("M06.5", "L'information mutuelle de deux variables", [
        ("a", "an irreducible fraction, as text", "Fraction(7, 16)",
         F + ''', mistakes={"« freine » est la première colonne": "9/16"}'''),
        ("b", "a number (3 decimals)", "H(7 / 16, 9 / 16)", 'decimals=3'),
        ("c", "a number (3 decimals)", "H(1 / 9, 8 / 9)",
         f'''decimals=3, mistakes={{"{ROW.format(x="vert")}": H(1 / 16, 1 / 2), '''
         f'''"{ROW_THEN.format(x="vert")}": H(1 / 16, 1 / 2) / (9 / 16)}}'''),
        ("d", "a number (3 decimals)", "HYX_5",
         f'''decimals=3, mistakes={{"{MEAN}": H(1 / 9, 8 / 9) + H(1 / 3, 2 / 3), '''
         f'''"{WEIGHT}": (H(1 / 9, 8 / 9) + H(1 / 3, 2 / 3)) / 3}}'''),
        ("e", "a number (2 decimals)", "H(7 / 16, 9 / 16) - HYX_5",
         '''decimals=2, mistakes={"I(X ; Y) est la baisse de l'incertitude sur Y quand on apprend X : elle est '''
         '''positive ou nulle": HYX_5 - H(7 / 16, 9 / 16)}'''),
        ("f", "a number (3 decimals)", "H(9 / 16, 3 / 16, 1 / 4)", 'decimals=3'),
        ("g", "a number (2 decimals)", "H(9 / 16, 3 / 16, 1 / 4) - (H(7 / 16, 9 / 16) - HYX_5)",
         f'''decimals=2, mistakes={{"{YX}": HYX_5}}'''),
        ("h", "True or False", "False",
         '''mistakes={"compare p(x, y) avec p(x) p(y), case par case": True}'''),
    ]),

    Paper("M06.6", "Cross-entropy et KL en bits perdus : un code fait pour la mauvaise loi", [
        ("a", "a number (2 decimals)", "H(*P_6)",
         '''decimals=2, mistakes={"c'est l'entropie de l'ancienne loi q ; la question demande celle de p": H(*Q_6)}'''),
        ("b", "an integer", "1",
         '''mistakes={"le compresseur a été réglé sur l'ancienne loi : la longueur est −log₂ q": 2}'''),
        ("c", "a number (3 decimals)", "CROSS_6",
         '''decimals=3, mistakes={"H(p, q) pondère les longueurs −log₂ q par les probabilités d'aujourd'hui, p": '''
         '''H(*Q_6), "H(p, q) utilise les longueurs du compresseur, −log₂ q, pas −log₂ p": H(*P_6), '''
         '''"c'est H(q, p) : les poids sont les probabilités d'aujourd'hui, p, et les longueurs celles du '''
         '''compresseur": sum(qi * -math.log2(pi) for pi, qi in zip(P_6, Q_6))}'''),
        ("d", "a number (3 decimals)", "CROSS_6 - H(*P_6)",
         '''decimals=3, mistakes={"la divergence KL est positive ou nulle": H(*P_6) - CROSS_6, '''
         '''"c'est KL(q ‖ p) : l'ordre des deux lois compte": sum(qi * math.log2(qi / pi) for pi, qi in zip(P_6, Q_6))}'''),
        ("e", "an integer", "375",
         '''mistakes={"c'est la longueur totale avec ce compresseur ; la question demande les bits perdus par '''
         '''rapport au meilleur code": 2625, "c'est la longueur totale avec le meilleur code ; la question demande '''
         '''les bits perdus": 2250}'''),
        ("f", "a number (3 decimals)", "(CROSS_6 - H(*P_6)) * math.log(2)",
         f'''decimals=3, mistakes={{"{CONVERT_NATS}": CROSS_6 - H(*P_6), "{NAT_SMALLER}": (CROSS_6 - H(*P_6)) / math.log(2)}}'''),
        ("g", "a number (2 decimals)", "0.25 * math.log2(0.25 / 0.5)",
         '''decimals=2, mistakes={"le terme d'un type est p log₂(p / q) : p devant, et p au numérateur": '''
         '''0.5 * math.log2(0.5 / 0.25), "p₁ / q₁ est-il plus grand ou plus petit que 1 ? Le signe du logarithme en '''
         '''dépend": 0.25}'''),
    ]),

    Paper("M06.7", "L'inégalité de Jensen sur trois exemples", [
        ("a", "an integer", "3", ''),
        ("b", "an integer", "11",
         '''mistakes={"E[X²] n'est pas (E[X])² : c'est la moyenne des carrés": 9}'''),
        ("c", "an integer", "2", f'''mistakes={{"{ORDER}": -2}}'''),
        ("d", "a number (4 decimals)", "(1 + math.e) / 2 - math.exp(0.5)",
         f'''decimals=4, mistakes={{"{ORDER}": math.exp(0.5) - (1 + math.e) / 2}}'''),
        ("e", "a number (1 decimal)", "(math.log2(1) + math.log2(4)) / 2", 'decimals=1'),
        ("f", "a number (4 decimals)", "math.log2(2.5)",
         '''decimals=4, mistakes={"la question demande log₂, pas ln": math.log(2.5)}'''),
        ("g", "a number (4 decimals)", "1 - math.log2(2.5)", f'''decimals=4, mistakes={{"{ORDER}": math.log2(2.5) - 1}}'''),
    ]),

    Paper("M06.8", "Kraft : ces longueurs de code sont-elles possibles ?", [
        ("a", "a fraction (or an integer), as text", "Fraction(15, 16)",
         F + ''', mistakes={"un mot de longueur ℓ compte pour 2^(−ℓ), pas pour 1/ℓ": "25/12"}'''),
        ("b", "a fraction (or an integer), as text", "Fraction(17, 16)", F),
        ("c", "a fraction (or an integer), as text", "Fraction(19, 16)", F),
        ("d", "a fraction (or an integer), as text", "Fraction(1, 1)", F),
        ("e", "a fraction (or an integer), as text", "Fraction(1, 1)",
         F + ''', mistakes={"l'alphabet a trois symboles : un mot de longueur ℓ compte pour 3^(−ℓ)": "7/4"}'''),
        ("f", "an integer", "2",
         '''mistakes={"les deux mots déjà là prennent chacun leur part de la somme de Kraft": {4, 6}}'''),
        ("g", "True or False", "False",
         '''mistakes={"un des mots est-il le début d'un autre ?": True}'''),
        ("h", "a fraction (or an integer), as text", "Fraction(1, 1)", F),
    ]),

    Paper("M06.9", "La longueur moyenne d'un code, comparée à l'entropie", [
        ("a", "a number (3 decimals)", "H(*P_9)",
         f'''decimals=3, mistakes={{"{BITS}": H(*P_9) * math.log(2)}}'''),
        ("b", "a number (2 decimals)", "L_9",
         '''decimals=2, mistakes={"la longueur moyenne pondère chaque longueur par la probabilité de son symbole": '''
         '''sum(LENGTHS_9) / 6}'''),
        ("c", "an integer", "3",
         '''mistakes={"avec ce nombre de chiffres binaires, combien de mots différents peut-on écrire ?": 2}'''),
        ("d", "a list of 6 integers", "[2, 3, 3, 4, 4, 5]",
         '''mistakes={"arrondis −log₂ pᵢ à l'entier supérieur, pas à l'entier le plus proche": [1, 2, 3, 3, 3, 4], '''
         '''"arrondis −log₂ pᵢ à l'entier supérieur, pas à l'entier inférieur": [1, 2, 2, 3, 3, 4]}'''),
        ("e", "an irreducible fraction, as text", "Fraction(21, 32)", F),
        ("f", "a number (2 decimals)", "sum(pi * li for pi, li in zip(P_9, [2, 3, 3, 4, 4, 5]))", 'decimals=2'),
        ("g", "a number (3 decimals)", "L_9 - H(*P_9)",
         '''decimals=3, mistakes={"l'écart est la longueur moyenne moins l'entropie, dans cet ordre": H(*P_9) - L_9}'''),
        ("h", "a number (2 decimals)", "sum(pi * li for pi, li in zip(P_9, [1, 3, 3, 3, 4, 4]))",
         '''decimals=2, mistakes={"la longueur moyenne pondère chaque longueur par la probabilité de son symbole": '''
         '''18 / 6}'''),
    ]),

    Paper("M06.12", "La log loss d'un classifieur, une cross-entropy moyenne", [
        ("a", "a number (3 decimals)", "-math.log(0.35)",
         '''decimals=3, mistakes={"la cross-entropy d'une image ne retient que la probabilité donnée à sa vraie '''
         '''classe": -math.log(0.5), "la question demande des nats : ln, pas log₂": -math.log2(0.35)}'''),
        ("b", "a number (3 decimals)", "LOSS_12",
         '''decimals=3, mistakes={"la log loss est une moyenne sur les images, pas une somme": 5 * LOSS_12, '''
         '''"la question demande des nats : ln, pas log₂": LOSS_12 / math.log(2)}'''),
        ("c", "a number (2 decimals)", "LOSS_12 / math.log(2)",
         '''decimals=2, mistakes={"la question demande des bits : convertis les nats en bits": LOSS_12, '''
         '''"1 nat vaut plus qu'un bit : le nombre de bits est plus grand que le nombre de nats": LOSS_12 * math.log(2)}'''),
        ("d", "a number (3 decimals)", "math.log(3)", f'''decimals=3, mistakes={{"{NATS}": math.log2(3)}}'''),
        ("e", "True or False", "True", '''mistakes={"compare b) et d)": False}'''),
        ("f", "a number (3 decimals)", "math.exp(LOSS_12)",
         '''decimals=3, mistakes={"la log loss est en nats : son exponentielle est en base e, pas 2": 2 ** LOSS_12}'''),
    ]),

    Paper("M06.13", "Choisir une feature par l'information mutuelle", [
        ("a", "a number (4 decimals)", "MI([[7, 3], [3, 7]])",
         f'''decimals=4, mistakes={{"{BITS}": MI([[7, 3], [3, 7]]) * math.log(2), '''
         '''"ta valeur est H(Y | F₁), l'incertitude qui reste ; la question demande I(F₁ ; Y)": 1 - MI([[7, 3], [3, 7]])}'''),
        ("b", "a number (4 decimals)", "MI([[6, 4], [4, 6]])",
         f'''decimals=4, mistakes={{"{BITS}": MI([[6, 4], [4, 6]]) * math.log(2), '''
         '''"ta valeur est H(Y | F₂), l'incertitude qui reste ; la question demande I(F₂ ; Y)": 1 - MI([[6, 4], [4, 6]])}'''),
        ("c", "a number (4 decimals)", "MI([[4, 0], [2, 4], [4, 6]])",
         f'''decimals=4, mistakes={{"{BITS}": MI([[4, 0], [2, 4], [4, 6]]) * math.log(2), '''
         '''"ta valeur est H(Y | F₃), l'incertitude qui reste ; la question demande I(F₃ ; Y)": '''
         '''1 - MI([[4, 0], [2, 4], [4, 6]]), "pondère l'entropie de chaque ligne par la probabilité de sa valeur de '''
         '''F₃": 1 - (H(1 / 3, 2 / 3) + H(0.4, 0.6)) / 3}'''),
        ("d", "a name, as text", '"F3"',
         '''mistakes={"compare a), b) et c)": {"F1", "F2"}, "réponds par un nom : F1, F2 ou F3": {"3", "la feature F3"}}'''),
        ("e", "a number (4 decimals)", "1 - MI([[4, 0], [2, 4], [4, 6]])",
         '''decimals=4, mistakes={"ta valeur est I(F₃ ; Y), ce que l'âge apprend ; la question demande l'incertitude qui '''
         '''reste, H(Y | F₃)": MI([[4, 0], [2, 4], [4, 6]]), "pondère l'entropie de chaque ligne par la probabilité de '''
         '''sa valeur de F₃": (H(1 / 3, 2 / 3) + H(0.4, 0.6)) / 3}'''),
        ("f", "a number (4 decimals)", "MI([[7, 3], [3, 7]]) * math.log(2)",
         f'''decimals=4, mistakes={{"{NATS}": MI([[7, 3], [3, 7]])}}'''),
        ("g", "True or False", "False",
         '''mistakes={"regrouper deux valeurs efface une distinction : calcule l'information mutuelle du tableau '''
         '''regroupé": True}'''),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math
from fractions import Fraction


def H(*probs):
    """Entropy in bits of a law given by its probabilities (0 log 0 counts as 0)."""
    return -sum(p * math.log2(p) for p in probs if p > 0)


def MI(counts):
    """Mutual information in bits of the joint law given by a table of counts (rows: the feature, columns: Y)."""
    total = sum(map(sum, counts))
    rows = [sum(row) / total for row in counts]
    cols = [sum(col) / total for col in zip(*counts)]
    return sum(c / total * math.log2(c / total / (rows[i] * cols[j]))
               for i, row in enumerate(counts) for j, c in enumerate(row) if c > 0)


H1 = H(0.55, 0.35, 0.07, 0.03)                                                  # M06.1
INFO_SUM_1 = -sum(math.log2(p) for p in (0.55, 0.35, 0.07, 0.03))
HMAX_2 = H(0.45, 0.55 / 3, 0.55 / 3, 0.55 / 3)                                  # M06.2 e)
HYX_5 = 9 / 16 * H(1 / 9, 8 / 9) + 3 / 16 * H(1 / 3, 2 / 3) + 1 / 4 * 0        # M06.5: H(Y | X)
P_6 = [1 / 4, 1 / 4, 1 / 4, 1 / 8, 1 / 8]                                       # M06.6
Q_6 = [1 / 2, 1 / 4, 1 / 16, 1 / 16, 1 / 8]
CROSS_6 = sum(pi * -math.log2(qi) for pi, qi in zip(P_6, Q_6))                  # H(p, q)
P_9 = [0.4, 0.2, 0.15, 0.1, 0.1, 0.05]                                          # M06.9
LENGTHS_9 = [2, 3, 2, 3, 3, 3]                                                  # the code {00, 100, 01, 101, 110, 111}
L_9 = sum(pi * li for pi, li in zip(P_9, LENGTHS_9))
LOSS_12 = -sum(math.log(p) for p in (0.5, 0.8, 0.35, 0.9, 0.4)) / 5            # M06.12, in nats'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M06.1 à M06.9, 🔗 M06.12 et M06.13)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"5/9\"` ;\n"
               "- une liste `[-1.5, 2.5]`, `True` / `False`, ou une lettre ou un nom entre guillemets, `\"B\"`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M06.16 to M06.19) and scikit-learn (M06.20)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np

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

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M06")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/info.py`, lis la docstring "
         "du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton code, "
         "**enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. Une "
         "loi jointe est un tableau à deux dimensions (une liste de listes ou un tableau NumPy), comme dans "
         "`conditional.py` (M03) : les lignes sont les valeurs de $X$, les colonnes celles de $Y$. NumPy suffit ; "
         "`scipy.stats.entropy` et scikit-learn sont interdits : les tests comparent tes résultats aux leurs, et un "
         "test vérifie que tu ne t'en sers pas. Les nombres renvoyés sont des `float` de Python, les réponses oui ou "
         "non des `bool` de Python.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of info.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_info_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m06_info.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m06_info.py", "{keyword}", impl="ref")')]


M06_16 = Ex(
    "M06.16", "🔨", 1, 20, "Entropies conjointe et conditionnelle d'un tableau · `joint_entropy, conditional_entropy`",
    "programmer l'entropie conjointe et l'entropie conditionnelle d'une loi jointe, avec la convention 0 log 0 = 0, "
    "dans une base au choix, en refusant ce qui n'est pas une loi.", "fiche §3 ; M03 (`conditional.py`)",
    tracks="C, E", mymath="info.py",
    body=HOWTO + r"""

Écris (fiche §3) :
- `joint_entropy(joint, base=2)` : $H(X, Y) = -\sum_{x, y} p(x, y) \log p(x, y)$, sur les seules cases strictement positives ;
- `conditional_entropy(joint, base=2)` : $H(Y \mid X)$, l'entropie de la variable des **colonnes** quand on connaît celle des **lignes** (par la règle de la chaîne, $H(X, Y) - H(X)$, où la loi de $X$ est faite des sommes des lignes ; ou par la double somme).

Les deux lèvent une `ValueError` si le tableau n'est pas une loi jointe (pas deux dimensions, une case négative ou `nan`, une somme différente de 1 à $10^{-9}$ près), ou si `base` n'est pas plus grande que 1.

La vérification calcule, avec `T16 = [[0.25, 0.1, 0.05], [0.05, 0.2, 0.35]]` :
- a) `joint_entropy(T16)` (4 décimales) ;
- b) `conditional_entropy(T16)` (4 décimales) ;
- c) `conditional_entropy(np.array(T16).T)` : le tableau transposé (4 décimales) ;
- d) `joint_entropy(T16, base=math.e)` (4 décimales) ;
- e) le nom de l'erreur levée par `joint_entropy([[0.5, 0.4], [0.2, -0.1]])` ;
- f) le nom de l'erreur levée par `conditional_entropy(T16, base=1)` ;
- g) `joint_entropy([[0.15, 0], [0, 0.85]])` (4 décimales) ;
- h) le nom du type de `conditional_entropy(T16)`, en texte.

Dans ta copie : quelle entropie conditionnelle c) calcule-t-elle, et pourquoi la transposition suffit-elle ? Vérifie b) à la main, ligne par ligne. Pourquoi le tableau de e) est-il refusé alors que sa somme vaut 1 ? À quelle entropie d'une loi à deux issues g) est-elle égale ?""",
    todo=LOAD_LEARNER,
    check='''T16 = [[0.25, 0.1, 0.05], [0.05, 0.2, 0.35]]
with checked("M06.16a"):
    wbm.check("M06.16a", mymath.info.joint_entropy(T16), computed=True)
with checked("M06.16b"):
    wbm.check("M06.16b", mymath.info.conditional_entropy(T16), computed=True)
with checked("M06.16c"):
    wbm.check("M06.16c", mymath.info.conditional_entropy(np.array(T16).T), computed=True)
with checked("M06.16d"):
    wbm.check("M06.16d", mymath.info.joint_entropy(T16, base=math.e), computed=True)
with checked("M06.16e"):
    wbm.check("M06.16e", raised(mymath.info.joint_entropy, [[0.5, 0.4], [0.2, -0.1]]), computed=True)
with checked("M06.16f"):
    wbm.check("M06.16f", raised(mymath.info.conditional_entropy, T16, base=1), computed=True)
with checked("M06.16g"):
    wbm.check("M06.16g", mymath.info.joint_entropy([[0.15, 0], [0, 0.85]]), computed=True)
with checked("M06.16h"):
    wbm.check("M06.16h", type(mymath.info.conditional_entropy(T16)).__name__, computed=True)''',
    solution=LOAD_REF + '''
T16 = [[0.25, 0.1, 0.05], [0.05, 0.2, 0.35]]
info = mymath.info
print("a)", info.joint_entropy(T16), " b)", info.conditional_entropy(T16),
      " c)", info.conditional_entropy(np.array(T16).T), " d)", info.joint_entropy(T16, base=math.e))
print("e)", raised(info.joint_entropy, [[0.5, 0.4], [0.2, -0.1]]), " f)", raised(info.conditional_entropy, T16, base=1),
      " g)", info.joint_entropy([[0.15, 0], [0, 0.85]]), " h)", type(info.conditional_entropy(T16)).__name__)''',
    record=f'''wbm.record("M06.16a", 2.2588718484453607, decimals=4,
           mistakes={{"la docstring demande des bits par défaut (base=2)": 1.5657306529961337}})
wbm.record("M06.16b", 1.2879212539906917, decimals=4,
           mistakes={{"la fonction conditionne par la variable des lignes, X : tu as calculé H(X | Y)": 0.6879212539906918,
                     "c'est l'entropie de Y seule : connaître X doit la faire baisser": 1.5709505944546687,
                     "c'est l'entropie conjointe : retire l'entropie de la loi des lignes": 2.2588718484453607}})
wbm.record("M06.16c", 0.6879212539906918, decimals=4,
           mistakes={{"en transposant, les colonnes deviennent les lignes : la fonction conditionne alors par Y":
                         1.2879212539906917}})
wbm.record("M06.16d", 1.5657306529961337, decimals=4,
           mistakes={{"base=math.e donne des nats : le logarithme de base e": 2.2588718484453607}})
wbm.record("M06.16e", "ValueError",
           mistakes={{"une case négative n'est pas une probabilité : la docstring demande une ValueError, même si la "
                     "somme vaut 1": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M06.16f", "ValueError",
           mistakes={{"une base égale à 1 est refusée : lève une ValueError avant tout calcul": "aucune",
                     "vérifie la base avant de diviser par son logarithme : base <= 1 demande une ValueError":
                         "ZeroDivisionError",
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "ZeroDivisionError")}}})
wbm.record("M06.16g", 0.6098403047164005, decimals=4,
           mistakes={{"la docstring demande des bits par défaut (base=2)": 0.6098403047164005 * math.log(2)}})
wbm.record("M06.16h", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy": "float64"}})''',
    after=tests_cells("test_joint_entropy_ or test_conditional_entropy_"),
    note=r"a) Les six cases donnent $H(X, Y) \approx 2{,}2589$ bits. b) La ligne 1, divisée par 0,4, est $(\frac{5}{8}, "
         r"\frac{1}{4}, \frac{1}{8})$, d'entropie 1,2988 ; la ligne 2, divisée par 0,6, est $(\frac{1}{12}, \frac{1}{3}, "
         r"\frac{7}{12})$, d'entropie 1,2807 ; $H(Y \mid X) = 0{,}4 \times 1{,}2988 + 0{,}6 \times 1{,}2807 \approx 1{,}2879$. "
         r"c) Transposé, le tableau a $Y$ en lignes : la fonction calcule $H(X \mid Y) = H(X, Y) - H(Y) \approx 0{,}6879$. "
         r"d) En nats : $2{,}2589 \times \ln 2 \approx 1{,}5657$. e) Une case négative n'est pas une probabilité, même si "
         r"la somme vaut 1 ; sans vérification, son logarithme donnerait `nan`. f) $\ln 1 = 0$ serait au dénominateur. g) "
         r"Les cases nulles comptent pour 0 : c'est l'entropie de $(0{,}15 ;\ 0{,}85)$, environ 0,6098 bit.",
)

M06_17 = Ex(
    "M06.17", "🔨", 1, 15, "L'information mutuelle · `mutual_information`",
    "programmer l'information mutuelle d'une loi jointe, et vérifier qu'elle est symétrique, nulle pour des "
    "variables indépendantes et égale à l'entropie quand une variable détermine l'autre.",
    "fiche §4 ; Ex M06.16", tracks="C, E", mymath="info.py",
    body=r"""Écris `mutual_information(joint, base=2)` (fiche §4) : $I(X ; Y) = \sum p(x, y) \log \frac{p(x, y)}{p(x)\,p(y)}$ sur les cases strictement positives, ou $H(Y) - H(Y \mid X)$ avec ta fonction de M06.16 ; une petite valeur négative due aux arrondis (au-dessus de $-10^{-12}$) est renvoyée comme `0.0`. Mêmes `ValueError` qu'en M06.16.

La vérification calcule, avec `T17 = [[0.3, 0.1], [0.05, 0.25], [0.15, 0.15]]` :
- a) `mutual_information(T17)` (4 décimales) ;
- b) l'information mutuelle du tableau transposé est-elle égale à a), à $10^{-12}$ près ? (`True` ou `False`) ;
- c) `mutual_information(np.outer([0.2, 0.8], [0.3, 0.3, 0.4]))` (4 décimales) ;
- d) `mutual_information(np.diag([0.1, 0.4, 0.5]))` (4 décimales) ;
- e) `mutual_information(T17, base=math.e)` (4 décimales) ;
- f) le nom de l'erreur levée par `mutual_information([[0.5, np.nan], [0.25, 0.25]])` ;
- g) le nom du type de `mutual_information(T17)`, en texte.

Dans ta copie : quelle loi `np.outer` construit-elle en c), et pourquoi le résultat était-il prévisible ? Même question pour d) : que vaut $H(Y \mid X)$ pour ce tableau ? Pourquoi la vérification de f) ne peut-elle pas s'écrire `np.any(table < 0)` ?""",
    todo=LOAD_LEARNER,
    check='''T17 = [[0.3, 0.1], [0.05, 0.25], [0.15, 0.15]]
with checked("M06.17a"):
    wbm.check("M06.17a", mymath.info.mutual_information(T17), computed=True)
with checked("M06.17b"):
    wbm.check("M06.17b", math.isclose(mymath.info.mutual_information(T17),
                                      mymath.info.mutual_information(np.array(T17).T), abs_tol=1e-12), computed=True)
with checked("M06.17c"):
    wbm.check("M06.17c", mymath.info.mutual_information(np.outer([0.2, 0.8], [0.3, 0.3, 0.4])), computed=True)
with checked("M06.17d"):
    wbm.check("M06.17d", mymath.info.mutual_information(np.diag([0.1, 0.4, 0.5])), computed=True)
with checked("M06.17e"):
    wbm.check("M06.17e", mymath.info.mutual_information(T17, base=math.e), computed=True)
with checked("M06.17f"):
    wbm.check("M06.17f", raised(mymath.info.mutual_information, [[0.5, np.nan], [0.25, 0.25]]), computed=True)
with checked("M06.17g"):
    wbm.check("M06.17g", type(mymath.info.mutual_information(T17)).__name__, computed=True)''',
    solution=LOAD_REF + '''
T17 = [[0.3, 0.1], [0.05, 0.25], [0.15, 0.15]]
mi = mymath.info.mutual_information
print("a)", mi(T17), " b)", math.isclose(mi(T17), mi(np.array(T17).T), abs_tol=1e-12),
      " c)", mi(np.outer([0.2, 0.8], [0.3, 0.3, 0.4])), " d)", mi(np.diag([0.1, 0.4, 0.5])))
print("e)", mi(T17, base=math.e), " f)", raised(mi, [[0.5, np.nan], [0.25, 0.25]]), " g)", type(mi(T17)).__name__)''',
    record=f'''wbm.record("M06.17a", 0.18048202372184055, decimals=4,
           mistakes={{"la docstring demande des bits par défaut (base=2)": 0.12510060588454694,
                     "I(X ; Y) est une entropie moins l'entropie conditionnelle de la même variable, sachant "
                     "l'autre : H(Y) − H(Y | X)": -0.3904685707328279,
                     "I(X ; Y) = H(X) + H(Y) − H(X, Y) : il manque un terme": 2.5709505944546684}})
wbm.record("M06.17b", True,
           mistakes={{"I(X ; Y) est symétrique : refais la double somme, avec la somme de la ligne et celle de la "
                     "colonne de chaque case": False}})
wbm.record("M06.17c", 0.0, decimals=4)
wbm.record("M06.17d", 1.360964047443681, decimals=4)
wbm.record("M06.17e", 0.12510060588454694, decimals=4,
           mistakes={{"base=math.e donne des nats : le logarithme de base e": 0.18048202372184055}})
wbm.record("M06.17f", "ValueError",
           mistakes={{"une case nan n'est pas une probabilité : la docstring demande une ValueError (nan < 0 est "
                     "faux, comme nan >= 0)": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M06.17g", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy": "float64"}})''',
    after=tests_cells("test_mutual_information_"),
    note=r"a) $I(X ; Y) \approx 0{,}1805$ bit. b) La formule ne change pas quand on échange les lignes et les "
         r"colonnes : $I(X ; Y) = I(Y ; X)$. c) `np.outer` construit la loi jointe $p(x)\,p(y)$ de deux variables "
         r"indépendantes : $I = 0$. d) Le tableau diagonal dit que $Y = X$ : $H(Y \mid X) = 0$ et $I = H(Y) = "
         r"H(0{,}1 ;\ 0{,}4 ;\ 0{,}5) \approx 1{,}3610$. e) En nats : $0{,}1805 \times \ln 2 \approx 0{,}1251$. f) "
         r"Toute comparaison avec `nan` est fausse : `np.any(table < 0)` laisse passer `nan`, `np.all(table >= 0)` le "
         r"refuse.",
)

M06_18 = Ex(
    "M06.18", "🔨", 1, 15, "Codes préfixes et somme de Kraft · `kraft_sum, is_prefix_code`",
    "programmer la somme de Kraft de longueurs de code pour un alphabet quelconque, et le test qui dit si un code "
    "est préfixe.", "fiche §7", tracks="C", mymath="info.py",
    body=r"""Écris (fiche §7) :
- `kraft_sum(lengths, alphabet=2)` : $\sum_i D^{-\ell_i}$, où $D$ est le nombre de symboles de l'alphabet du code ; une `ValueError` si la liste est vide, si une longueur est plus petite que 1, ou si $D < 2$. Les longueurs peuvent arriver dans un tableau NumPy : NumPy refuse un entier à une puissance entière négative (`np.int64(2) ** -3`), alors convertis avec `int(...)` ou `float(...)`, ou utilise `Fraction` ;
- `is_prefix_code(codewords)` : `True` si aucun mot n'est le début d'un autre (`str.startswith`), un mot répété deux fois rendant le code non préfixe ; une `ValueError` si un mot est le texte vide.

La vérification calcule :
- a) `kraft_sum([2, 2, 3, 4, 4, 4])` (4 décimales) ;
- b) `kraft_sum([1, 1, 2, 3], alphabet=3)` (4 décimales) ;
- c) le nom de l'erreur levée par `kraft_sum([2, 0, 1])` ;
- d) `is_prefix_code(["10", "110", "00", "111", "01"])` ;
- e) `is_prefix_code(["0", "101", "11", "10"])` ;
- f) `is_prefix_code(["1", "01", "1"])` ;
- g) le nom de l'erreur levée par `is_prefix_code(["0", ""])` ;
- h) `isinstance(is_prefix_code(np.array(["0", "10"])), bool)`.

Dans ta copie : pour a) et b), un code préfixe de ces longueurs existe-t-il ? Pour d), dessine l'arbre du code. Pourquoi le mot vide de g) ne peut-il pas faire partie d'un code (de quel mot est-il le début) ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M06.18a"):
    wbm.check("M06.18a", mymath.info.kraft_sum([2, 2, 3, 4, 4, 4]), computed=True)
with checked("M06.18b"):
    wbm.check("M06.18b", mymath.info.kraft_sum([1, 1, 2, 3], alphabet=3), computed=True)
with checked("M06.18c"):
    wbm.check("M06.18c", raised(mymath.info.kraft_sum, [2, 0, 1]), computed=True)
with checked("M06.18d"):
    wbm.check("M06.18d", mymath.info.is_prefix_code(["10", "110", "00", "111", "01"]), computed=True)
with checked("M06.18e"):
    wbm.check("M06.18e", mymath.info.is_prefix_code(["0", "101", "11", "10"]), computed=True)
with checked("M06.18f"):
    wbm.check("M06.18f", mymath.info.is_prefix_code(["1", "01", "1"]), computed=True)
with checked("M06.18g"):
    wbm.check("M06.18g", raised(mymath.info.is_prefix_code, ["0", ""]), computed=True)
with checked("M06.18h"):
    wbm.check("M06.18h", isinstance(mymath.info.is_prefix_code(np.array(["0", "10"])), bool), computed=True)''',
    solution=LOAD_REF + '''
info = mymath.info
print("a)", info.kraft_sum([2, 2, 3, 4, 4, 4]), " b)", info.kraft_sum([1, 1, 2, 3], alphabet=3),
      " c)", raised(info.kraft_sum, [2, 0, 1]))
print("d)", info.is_prefix_code(["10", "110", "00", "111", "01"]), " e)", info.is_prefix_code(["0", "101", "11", "10"]),
      " f)", info.is_prefix_code(["1", "01", "1"]), " g)", raised(info.is_prefix_code, ["0", ""]),
      " h)", isinstance(info.is_prefix_code(np.array(["0", "10"])), bool))''',
    record=f'''wbm.record("M06.18a", 0.8125, decimals=4,
           mistakes={{"un mot de longueur ℓ compte pour 2^(−ℓ), pas pour 1/ℓ": 1 / 2 + 1 / 2 + 1 / 3 + 3 / 4}})
wbm.record("M06.18b", 22 / 27, decimals=4,
           mistakes={{"alphabet=3 : un mot de longueur ℓ compte pour 3^(−ℓ)": 1.375}})
wbm.record("M06.18c", "ValueError",
           mistakes={{"un mot de longueur 0 n'existe pas : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M06.18d", True,
           mistakes={{"compare chaque paire de mots, dans les deux sens, avec str.startswith": False}})
wbm.record("M06.18e", False,
           mistakes={{"compare chaque paire de mots, dans les deux sens : un mot court peut être le début d'un mot "
                     "long placé avant ou après lui dans la liste": True}})
wbm.record("M06.18f", False,
           mistakes={{"un mot répété deux fois : relis ce que dit la docstring de ce cas": True}})
wbm.record("M06.18g", "ValueError",
           mistakes={{"un mot vide est refusé : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M06.18h", True,
           mistakes={{"la docstring demande un bool de Python : bool(...) convertit un booléen de NumPy, et str(...) "
                     "un texte de NumPy": False}})''',
    after=tests_cells("test_kraft_sum_ or test_is_prefix_code_"),
    note=r"a) $2 \times \frac{1}{4} + \frac{1}{8} + 3 \times \frac{1}{16} = \frac{13}{16} = 0{,}8125 \le 1$ : un code "
         r"préfixe de ces longueurs existe, avec de la place libre. b) $\frac{2}{3} + \frac{1}{9} + \frac{1}{27} = "
         r"\frac{22}{27} \approx 0{,}8148$. c) Une longueur 0 serait le mot vide. d) Aucun mot n'est le début d'un "
         r"autre : vrai (ce code a les longueurs du code de la fiche, dans un autre ordre). e) « 10 », placé après lui, est "
         r"le début de « 101 » : il faut comparer dans les deux sens. f) Un mot répété est le début de sa copie : on ne saurait pas lequel des deux symboles on lit. g) "
         r"Le mot vide est le début de tous les mots. h) Un booléen de NumPy n'est pas un `bool` de Python.",
)

M06_19 = Ex(
    "M06.19", "🔨", 1, 15, "L'écart de Jensen d'une loi discrète · `jensen_gap`",
    "programmer l'écart de Jensen d'une variable discrète, avec des poids donnés ou égaux, et lire son signe.",
    "fiche §6", tracks="C", mymath="info.py",
    body=r"""Écris `jensen_gap(f, values, weights=None)` (fiche §6) : $\mathbb{E}[f(X)] - f(\mathbb{E}[X])$ pour la variable $X$ qui prend les valeurs `values` avec les probabilités `weights` (toutes égales si `weights` vaut `None`). `f` est une fonction d'une variable réelle, comme `math.log` : applique-la valeur par valeur. Une `ValueError` si `values` est vide, ou si les poids n'ont pas la bonne longueur, ne sont pas positifs ou ne somment pas à 1 (à $10^{-9}$ près).

La vérification calcule :
- a) `jensen_gap(lambda x: x ** 2, [0, 2, 5], [0.5, 0.3, 0.2])` (4 décimales) ;
- b) `jensen_gap(math.log, [1, 2, 8])` (4 décimales) ;
- c) `jensen_gap(math.exp, [-1, 1])` (4 décimales) ;
- d) `jensen_gap(abs, [-2, 2])` (4 décimales) ;
- e) le nom de l'erreur levée par `jensen_gap(lambda x: x, [1, 2], [0.7, 0.2])` ;
- f) le nom de l'erreur levée par `jensen_gap(lambda x: x, [])` ;
- g) le nom du type de `jensen_gap(lambda x: x ** 2, np.array([1.0, 2.0]))`, en texte.

Dans ta copie : pour a) à d), dis si la fonction est convexe ou concave, et vérifie le signe. Calcule a) à la main : quelle grandeur de M02b retrouves-tu ? Pourquoi `abs`, convexe mais pas strictement convexe, donne-t-il un écart non nul en d), et pour quelles valeurs l'écart serait-il nul ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M06.19a"):
    wbm.check("M06.19a", mymath.info.jensen_gap(lambda x: x ** 2, [0, 2, 5], [0.5, 0.3, 0.2]), computed=True)
with checked("M06.19b"):
    wbm.check("M06.19b", mymath.info.jensen_gap(math.log, [1, 2, 8]), computed=True)
with checked("M06.19c"):
    wbm.check("M06.19c", mymath.info.jensen_gap(math.exp, [-1, 1]), computed=True)
with checked("M06.19d"):
    wbm.check("M06.19d", mymath.info.jensen_gap(abs, [-2, 2]), computed=True)
with checked("M06.19e"):
    wbm.check("M06.19e", raised(mymath.info.jensen_gap, lambda x: x, [1, 2], [0.7, 0.2]), computed=True)
with checked("M06.19f"):
    wbm.check("M06.19f", raised(mymath.info.jensen_gap, lambda x: x, []), computed=True)
with checked("M06.19g"):
    wbm.check("M06.19g", type(mymath.info.jensen_gap(lambda x: x ** 2, np.array([1.0, 2.0]))).__name__, computed=True)''',
    solution=LOAD_REF + '''
gap = mymath.info.jensen_gap
print("a)", gap(lambda x: x ** 2, [0, 2, 5], [0.5, 0.3, 0.2]), " b)", gap(math.log, [1, 2, 8]),
      " c)", gap(math.exp, [-1, 1]), " d)", gap(abs, [-2, 2]))
print("e)", raised(gap, lambda x: x, [1, 2], [0.7, 0.2]), " f)", raised(gap, lambda x: x, []),
      " g)", type(gap(lambda x: x ** 2, np.array([1.0, 2.0]))).__name__)''',
    record=f'''wbm.record("M06.19a", 3.64, decimals=4,
           mistakes={{"{ORDER}": -3.64,
                     "pondère par les poids donnés, pas par des poids égaux": 38 / 9}})
wbm.record("M06.19b", -0.3750867433836673, decimals=4,
           mistakes={{"{ORDER}": 0.3750867433836673}})
wbm.record("M06.19c", 0.5430806348152437, decimals=4,
           mistakes={{"{ORDER}": -0.5430806348152437}})
wbm.record("M06.19d", 2.0, decimals=4,
           mistakes={{"{ORDER}": -2.0}})
wbm.record("M06.19e", "ValueError",
           mistakes={{"des poids qui ne somment pas à 1 ne sont pas une loi : la docstring demande une ValueError":
                         "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M06.19f", "ValueError",
           mistakes={{"une liste vide n'a pas d'espérance : la docstring demande une ValueError": "aucune",
                     "vérifie la longueur avant de diviser : une liste vide demande une ValueError": "ZeroDivisionError",
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "ZeroDivisionError")}}})
wbm.record("M06.19g", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy": "float64"}})''',
    after=tests_cells("test_jensen_gap_"),
    note=r"a) $\mathbb{E}[X] = 1{,}6$, $\mathbb{E}[X^2] = 0{,}3 \times 4 + 0{,}2 \times 25 = 6{,}2$ : l'écart vaut "
         r"$6{,}2 - 2{,}56 = 3{,}64$, la variance de $X$ (M02b). b) $\ln$ est concave : $\frac{\ln 1 + \ln 2 + \ln 8}{3} - "
         r"\ln\frac{11}{3} = \frac{4}{3}\ln 2 - \ln\frac{11}{3} \approx -0{,}3751 < 0$. c) $\frac{e^{-1} + e}{2} - e^0 \approx "
         r"0{,}5431 > 0$ ($\exp$ est convexe). d) $\frac{2 + 2}{2} - |0| = 2$ : `abs` est convexe, et l'écart n'est "
         r"nul que si toutes les valeurs ont le même signe, là où `abs` est affine.",
)

M06_20_GIVEN = '''from sklearn.metrics import mutual_info_score

COUNTS_20 = np.array([[9, 3, 0], [2, 6, 4], [1, 3, 12]])     # 40 observations: rows X = 0, 1, 2; columns Y = 0, 1, 2
rows_20, cols_20 = np.indices(COUNTS_20.shape)
x_20 = np.repeat(rows_20.ravel(), COUNTS_20.ravel())         # the value of X of each observation
y_20 = np.repeat(cols_20.ravel(), COUNTS_20.ravel())         # the value of Y of the same observation
order_20 = np.random.default_rng(20).permutation(x_20.size)  # the observations in a random order
x_20, y_20 = x_20[order_20], y_20[order_20]
print("x_20[:12] =", x_20[:12], "· y_20[:12] =", y_20[:12])'''

M06_20_COMPARE = '''law_20 = COUNTS_20 / COUNTS_20.sum()
mine_20 = mymath.info.mutual_information(law_20, base=math.e)
theirs_20 = mutual_info_score(x_20, y_20)
print(f"mutual_information (nats): {mine_20:.6f} · mutual_info_score: {theirs_20:.6f}")
if abs(mine_20 - theirs_20) < 1e-9:
    print("✅ Ex M06.20 : ta fonction et scikit-learn donnent la même information mutuelle.")
else:
    print("❌ Ex M06.20 : ta fonction (en nats, base=math.e) et scikit-learn diffèrent : revois M06.17.")'''

M06_20 = Ex(
    "M06.20", "📦", 1, 15, "`sklearn.metrics.mutual_info_score` contre ta fonction, en nats",
    "calculer une information mutuelle avec scikit-learn à partir d'observations, en connaître l'unité et les "
    "propriétés, et voir son biais sur un petit échantillon.", "fiche §4 et §8 ; Ex M06.17", tracks="C",
    body=r"""scikit-learn calcule l'information mutuelle de deux variables catégorielles à partir de leurs **observations** (deux tableaux de valeurs de même longueur, une case par observation), pas d'une loi jointe : `mutual_info_score(x, y)` compte les paires, divise par leur nombre, et renvoie le résultat en **nats**. La cellule donnée crée `x_20` et `y_20`, 40 observations de deux variables à trois valeurs chacune. Calcule :
- a) `mutual_info_score(x_20, y_20)` (4 décimales) ;
- b) ce résultat en bits (4 décimales) ;
- c) `mutual_info_score(x_20, x_20)` (4 décimales) ;
- d) en remplaçant les valeurs 0, 1, 2 de `x_20` par les noms `"rouge"`, `"vert"`, `"bleu"` (`np.array(["rouge", "vert", "bleu"])[x_20]`), le résultat de a) change-t-il ? (`True` ou `False`) ;
- e) `mutual_info_score(x_20, rng.permutation(y_20))`, avec `rng = np.random.default_rng(620)` : les observations de $Y$ mélangées au hasard, ce qui rend les deux variables indépendantes (4 décimales).

La cellule suivante compare ensuite scikit-learn et ta fonction `mutual_information` (M06.17), en nats, sur la loi jointe des comptages.

Dans ta copie : quelle entropie c) donne-t-elle ? Pourquoi e) n'est-elle pas nulle, alors que les variables mélangées sont indépendantes ? Que deviendrait-elle avec 4 000 observations ? Pourquoi est-ce un piège quand on classe des features par information mutuelle sur peu de données (M06.13, fiche §8) ?""",
    given=M06_20_GIVEN,
    todo='''answer_M06_20a = ...  # a) a number (4 decimals)
answer_M06_20b = ...  # b) a number (4 decimals)
answer_M06_20c = ...  # c) a number (4 decimals)
answer_M06_20d = ...  # d) True or False
answer_M06_20e = ...  # e) a number (4 decimals)''',
    check='''for letter, answer in zip("abcde", [answer_M06_20a, answer_M06_20b, answer_M06_20c, answer_M06_20d,
                                    answer_M06_20e]):
    wbm.check(f"M06.20{letter}", answer)''',
    solution='''answer_M06_20a = mutual_info_score(x_20, y_20)
answer_M06_20b = answer_M06_20a / math.log(2)
answer_M06_20c = mutual_info_score(x_20, x_20)
answer_M06_20d = not math.isclose(mutual_info_score(np.array(["rouge", "vert", "bleu"])[x_20], y_20), answer_M06_20a)
rng = np.random.default_rng(620)
answer_M06_20e = mutual_info_score(x_20, rng.permutation(y_20))
print(answer_M06_20a, answer_M06_20b, answer_M06_20c, answer_M06_20d, answer_M06_20e)''',
    record='''wbm.record("M06.20a", 0.3356105802379715, decimals=4,
           mistakes={"a) demande la valeur que renvoie scikit-learn, telle quelle": 0.48418371977918906})
wbm.record("M06.20b", 0.48418371977918906, decimals=4,
           mistakes={"la question demande des bits : scikit-learn renvoie des nats": 0.3356105802379715,
                     "1 nat vaut plus qu'un bit : le nombre de bits est plus grand que le nombre de nats":
                         0.3356105802379715 * math.log(2)})
wbm.record("M06.20c", 1.0888999753452235, decimals=4,
           mistakes={"c) demande la valeur que renvoie scikit-learn, en nats, telle quelle": 1.0888999753452235 / math.log(2)})
wbm.record("M06.20d", False,
           mistakes={"essaie-le : remplace les valeurs, puis recalcule l'information mutuelle": True})
wbm.record("M06.20e", 0.09233151537307269, decimals=4,
           mistakes={"le résultat n'est pas nul : mélange les observations de Y par rng.permutation(y_20), juste "
                     "après avoir créé rng avec la graine 620": 0.0,
                     "appelle rng.permutation une seule fois, juste après avoir créé rng : un second appel donne un "
                     "autre mélange": 0.0635433181921396,
                     "mélange les observations de Y, pas celles de X": 0.14811740320162506})''',
    after=[("md", "**Ta fonction contre scikit-learn** (cette cellule utilise ta fonction de M06.17)."),
           ("todo", 'with checked("M06.20 comparaison"):\n'
                    + "\n".join("    " + line for line in M06_20_COMPARE.splitlines())),
           ("solution", M06_20_COMPARE)],
    note=r"a) et b) $0{,}3356$ nat, soit $\frac{0{,}3356}{\ln 2} \approx 0{,}4842$ bit. c) $I(X ; X) = H(X)$, ici "
         r"l'entropie de $(0{,}3 ;\ 0{,}3 ;\ 0{,}4)$ en nats, $\approx 1{,}0889$. d) Faux : l'information mutuelle ne "
         r"regarde que quelles observations ont la même valeur, pas les valeurs elles-mêmes. e) Environ 0,0923 nat, "
         r"et non 0 : sur 40 observations, les fréquences d'un tableau 3 × 3 s'écartent toujours un peu du produit des "
         r"marges, et l'information mutuelle estimée, positive ou nulle, ne peut se tromper que vers le haut. Avec 100 "
         r"fois plus d'observations, elle serait environ 100 fois plus petite (de l'ordre de $\frac{(3 - 1)(3 - 1)}{2n}$ "
         r"nat). Une feature à beaucoup de valeurs, sur peu de données, paraît donc informative même quand elle ne "
         r"l'est pas (M06.13 g)).",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M06.21 to M06.23)
# ---------------------------------------------------------------------------
M06_21_EXPERIMENT = '''ref_21 = wbm.load_mymath("ref")                        # the reference library: the same results as yours
values_21 = np.arange(-3, 4)                            # X is uniform on {-3, ..., 3}


def joint_21(g):
    """The joint law of (X, g(X)): one row per value of X, one column per value of g(X)."""
    images = sorted({int(g(v)) for v in values_21})
    table = np.zeros((len(values_21), len(images)))
    for i, v in enumerate(values_21):
        table[i, images.index(int(g(v)))] = 1 / len(values_21)
    return table


H_X_21 = ref_21.info.joint_entropy([np.full(7, 1 / 7)])  # the entropy of X: a table with a single row
print(f"H(X) = {H_X_21:.4f} bits")
for name, g in [("X³", lambda v: v ** 3), ("X²", lambda v: v ** 2)]:
    table = joint_21(g)
    r = round(float(np.corrcoef(values_21, [g(v) for v in values_21])[0, 1]), 10) + 0.0
    print(f"I(X ; {name}) = {ref_21.info.mutual_information(table):.4f} · "
          f"H({name}) = {ref_21.info.joint_entropy(table.sum(axis=0, keepdims=True)):.4f} · "
          f"H(X | {name}) = {ref_21.info.conditional_entropy(table.T):.4f} · correlation of X and {name}: {r:.4f}")'''

M06_21 = Ex(
    "M06.21", "🔮", 1, 10, "Prédire : l'information mutuelle de X et X³, de X et X²",
    "prévoir l'information mutuelle d'une variable avec une fonction d'elle-même, et la comparer à la corrélation.",
    "fiche §4", tracks="C, E", hypothesis=True,
    body=r"""Soit $X$ uniforme sur $\{-3, -2, \ldots, 3\}$ (sept valeurs), d'entropie $H(X) = \log_2 7$. Choisis, pour chaque question :
- a) $I(X ; X^3)$ : (1) égale à $H(X)$ ; (2) 0 ; (3) strictement entre 0 et $H(X)$ ; (4) plus grande que $H(X)$ ;
- b) la corrélation de $X$ et $X^3$ : (1) 0 ; (2) 1 ; (3) strictement entre 0 et 1 ; (4) négative ;
- c) $I(X ; X^2)$ : (1) 0 ; (2) égale à $H(X)$ ; (3) strictement entre 0 et $H(X)$ ; (4) plus grande que $H(X)$ ;
- d) $I(X ; X^2)$ est égale à : (1) $H(X) - H(X^2)$ ; (2) $H(X^2)$ ; (3) $H(X \mid X^2)$ ; (4) $2\,H(X^2)$.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience. Elle utilise les fonctions de la référence (les tiennes, M06.16 et M06.17, font la même chose).""",
    todo='''prediction_M06_21a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M06_21b = ...  # b) 1, 2, 3 or 4
prediction_M06_21c = ...  # c) 1, 2, 3 or 4
prediction_M06_21d = ...  # d) 1, 2, 3 or 4''',
    check='''for letter, prediction in zip("abcd", [prediction_M06_21a, prediction_M06_21b, prediction_M06_21c,
                                      prediction_M06_21d]):
    wbm.check(f"M06.21{letter}", prediction)''',
    record='''wbm.record("M06.21a", 1, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M06.21b", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M06.21c", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M06.21d", 2, prediction=True, choices=[1, 2, 3, 4])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(M06_21_EXPERIMENT, ["prediction_M06_21a", "prediction_M06_21b", "prediction_M06_21c",
                                              "prediction_M06_21d"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", M06_21_EXPERIMENT),
        ("md", r"**Après l'expérience**, dans ta copie : pourquoi $I(X ; X^3) = H(X)$, alors que la corrélation n'est pas "
               r"1 ? Pourquoi $I(X ; X^2) = H(X^2)$ (que vaut $H(X^2 \mid X)$) ? Que reste-t-il d'inconnu sur $X$ quand on "
               r"connaît $X^2$, et combien de bits cela fait-il ? Que mesure la corrélation, que l'information mutuelle "
               r"ne mesure pas, et inversement ?"),
    ],
    note=r"a) $X^3$ est une fonction injective de $X$ : chacune détermine l'autre, $H(X \mid X^3) = 0$ et $I = H(X) = "
         r"\log_2 7 \approx 2{,}807$. b) La relation n'est pas linéaire : la corrélation vaut environ 0,930, entre 0 et 1, "
         r"alors que la dépendance est totale. c) et d) $X^2$ est une fonction de $X$ : $H(X^2 \mid X) = 0$, donc "
         r"$I(X ; X^2) = H(X^2) = H(\frac{1}{7}, \frac{2}{7}, \frac{2}{7}, \frac{2}{7}) \approx 1{,}950$, strictement "
         r"entre 0 et $H(X)$ : connaître $X^2$ laisse inconnu le signe de $X$, soit $H(X \mid X^2) = \frac{6}{7} \approx "
         r"0{,}857$ bit. La corrélation de $X$ et $X^2$ est nulle, par symétrie : elle ne voit que les liens linéaires.",
)

M06_22_GIVEN = '''P_22 = np.array([0.34, 0.24, 0.16, 0.13, 0.09, 0.04])    # a law on 6 outcomes, 0 to 5
H_22 = float(-np.sum(P_22 * np.log2(P_22)))                 # its entropy, in bits
rng_22 = np.random.default_rng(622)
SAMPLES_22 = {n: rng_22.choice(6, size=(2000, n), p=P_22) for n in (10, 20, 50, 100, 1000)}   # 2000 samples of each size


def plugin_entropy(sample, k):
    """The plug-in estimate: the entropy, in bits, of the frequencies of sample (integers from 0 to k - 1)."""
    freq = np.bincount(sample, minlength=k) / len(sample)
    freq = freq[freq > 0]
    return float(-np.sum(freq * np.log2(freq)))


print(f"H = {H_22:.4f} bits ·", {n: samples.shape for n, samples in SAMPLES_22.items()})'''

M06_22_CHECK = '''with checked("M06.22a"):
    wbm.check("M06.22a", mean_bias(plugin_entropy, 10), computed=True)
with checked("M06.22b"):
    wbm.check("M06.22b", mean_bias(plugin_entropy, 100), computed=True)
with checked("M06.22c"):
    wbm.check("M06.22c", mean_bias(miller_madow, 10), computed=True)
with checked("M06.22d"):
    wbm.check("M06.22d", mean_bias(miller_madow, 100), computed=True)
with checked("M06.22e"):
    wbm.check("M06.22e", miller_madow(SAMPLES_22[10][0], 6), computed=True)'''

M06_22_TABLE = '''rows_22 = []
for n_22 in SAMPLES_22:
    rows_22.append((n_22, mean_bias(plugin_entropy, n_22), -(6 - 1) / (2 * n_22 * math.log(2)),
                    mean_bias(miller_madow, n_22)))
print("    n · plug-in bias · −(k − 1)/(2n ln 2) · Miller-Madow bias")
for n_22, plug_22, approx_22, mm_22 in rows_22:
    print(f"{n_22:5d} · {plug_22:14.4f} · {approx_22:18.4f} · {mm_22:17.4f}")'''

M06_22 = Ex(
    "M06.22", "🔬", 2, 20, "Estimer une entropie à partir d'un échantillon : le biais des petits échantillons",
    "mesurer le biais de l'entropie estimée par les fréquences d'un échantillon, voir comment il diminue avec la "
    "taille de l'échantillon, et le corriger.", "fiche §2 ; M02c (biais d'un estimateur)", tracks="C",
    body=r"""On estime souvent une entropie à partir d'un échantillon : on remplace chaque probabilité par sa fréquence observée, puis on applique la formule. C'est l'estimateur « plug-in », donné dans la cellule ci-dessous (`plugin_entropy`). Il se trompe en moyenne, et toujours dans le même sens : mesure ce biais (M02c), puis corrige-le.

La cellule donnée tire aussi, pour la loi `P_22` (6 issues, d'entropie `H_22`), 2 000 échantillons de chaque taille $n$ = 10, 20, 50, 100 et 1 000 : `SAMPLES_22[n]` est un tableau de forme `(2000, n)`, un échantillon par ligne. Écris :
- `mean_bias(estimator, n)` : la moyenne des 2 000 estimations `estimator(sample, 6)` sur les échantillons de taille `n`, moins la vraie entropie `H_22`, en `float` ;
- `miller_madow(sample, k)` : l'estimation corrigée de Miller-Madow, `plugin_entropy(sample, k)` plus $\frac{m - 1}{2n\ln 2}$ bit, où $n$ est la taille de l'échantillon et $m$ le nombre de valeurs **différentes** qu'il contient.

La vérification calcule, avec tes fonctions :
- a) le biais du plug-in pour $n = 10$ (3 décimales) ;
- b) le biais du plug-in pour $n = 100$ (3 décimales) ;
- c) le biais de Miller-Madow pour $n = 10$ (3 décimales) ;
- d) le biais de Miller-Madow pour $n = 100$ (4 décimales) ;
- e) `miller_madow(SAMPLES_22[10][0], 6)`, l'estimation corrigée du premier échantillon de taille 10 (4 décimales).

Une dernière cellule affiche les biais pour les cinq tailles.

Dans ta copie : dans quel sens le plug-in se trompe-t-il, et pourquoi (que devient une issue de probabilité 0,04 dans un échantillon de taille 10) ? Compare a) et b) avec l'approximation $-\frac{k - 1}{2n\ln 2}$ : pour quelle taille est-elle la meilleure ? Pourquoi la correction de Miller-Madow, qui compte les valeurs observées, laisse-t-elle un biais pour $n = 10$ ? Qu'en conclure pour une information mutuelle estimée sur peu de données (M06.20 e)) ?""",
    given=M06_22_GIVEN,
    todo='''def mean_bias(estimator, n):
    """The mean of estimator(sample, 6) over the 2000 samples of size n of SAMPLES_22, minus H_22."""
    raise NotImplementedError("relis la définition du biais d'un estimateur (M02c)")


def miller_madow(sample, k):
    """plugin_entropy(sample, k) + (m - 1) / (2 n ln 2), with n the size of sample and m its number of distinct values."""
    raise NotImplementedError("relis la formule de l'énoncé : que valent n et m pour un échantillon ?")''',
    check=M06_22_CHECK,
    solution='''def mean_bias(estimator, n):
    """The mean of estimator(sample, 6) over the 2000 samples of size n of SAMPLES_22, minus H_22."""
    return float(np.mean([estimator(sample, 6) for sample in SAMPLES_22[n]]) - H_22)


def miller_madow(sample, k):
    """plugin_entropy(sample, k) + (m - 1) / (2 n ln 2), with n the size of sample and m its number of distinct values."""
    m = np.count_nonzero(np.bincount(sample, minlength=k))
    return plugin_entropy(sample, k) + (m - 1) / (2 * len(sample) * math.log(2))


print("plug-in bias, n = 10:", mean_bias(plugin_entropy, 10), "· Miller-Madow:", mean_bias(miller_madow, 10))''',
    record='''wbm.record("M06.22a", -0.4024603628852439, decimals=3,
           mistakes={"le biais est la moyenne des estimations moins la vraie entropie, dans cet ordre":
                         0.4024603628852439})
wbm.record("M06.22b", -0.034618511809517916, decimals=3,
           mistakes={"le biais est la moyenne des estimations moins la vraie entropie, dans cet ordre":
                         0.034618511809517916})
wbm.record("M06.22c", -0.1540643442201861, decimals=3,
           mistakes={"m est le nombre de valeurs différentes observées dans l'échantillon, pas le nombre k d'issues "
                     "possibles": -0.041786602663002714,
                     "la correction est en bits : (m − 1)/(2n ln 2), avec le ln 2 au dénominateur":
                         -0.23028536288524393})
wbm.record("M06.22d", 0.0013370553470379853, decimals=4,
           mistakes={"m est le nombre de valeurs différentes observées dans l'échantillon, pas le nombre k d'issues "
                     "possibles": 0.0014488642127066242})
wbm.record("M06.22e", 1.5731839055803842, decimals=4,
           mistakes={"m est le nombre de valeurs différentes observées dans l'échantillon, pas le nombre k d'issues "
                     "possibles": 1.3567796494470397 + 5 / (20 * math.log(2))})''',
    after=[("md", "**Les biais pour les cinq tailles** (cette cellule utilise tes fonctions)."),
           ("todo", 'with checked("M06.22 tableau"):\n' + "\n".join("    " + line for line in M06_22_TABLE.splitlines())),
           ("solution", M06_22_TABLE)],
    note=r"Le plug-in sous-estime l'entropie : une issue rare, absente d'un petit échantillon, compte pour 0, et les "
         r"fréquences observées sont en moyenne plus inégales que les vraies probabilités. Son biais vaut environ "
         r"$-0{,}402$ pour $n = 10$ et $-0{,}035$ pour $n = 100$ ; l'approximation $-\frac{k - 1}{2n\ln 2}$ ($-0{,}361$ "
         r"et $-0{,}036$) décrit bien les grands échantillons. Miller-Madow, avec $m$ valeurs observées, ramène le "
         r"biais à environ $-0{,}154$ pour $n = 10$ (il reste des issues jamais vues, que la correction ne compte pas) et à "
         r"presque rien pour $n = 100$. L'information mutuelle estimée, qui se calcule avec des entropies estimées, a un "
         r"biais du même ordre, mais vers le haut (M06.20 e)).",
)

M06_23_CHECK = '''with checked("M06.23 vérifications"):
    from matplotlib.patches import Rectangle
    problems = []
    joint_t = np.array([[0.25, 0.05], [0.15, 0.15], [0.05, 0.35]])     # another example


    def entropy_t(p):
        p = np.asarray(p, dtype=float).ravel()
        p = p[p > 0]
        return float(-np.sum(p * np.log2(p)))


    hx, hy, hxy = entropy_t(joint_t.sum(axis=1)), entropy_t(joint_t.sum(axis=0)), entropy_t(joint_t)
    fig, ax = plt.subplots(figsize=(7, 3))
    try:
        created = drawn(draw_information_bars, ax, joint_t)
        fig.canvas.draw()
        labels = " ".join(t.get_text() for t in [*ax.get_yticklabels(), *ax.texts]).replace(" ", "")
        xlabel = ax.get_xlabel()
        rows = {}
        widths = [abs(patch.get_width()) for patch in ax.patches if isinstance(patch, Rectangle)]
        heights = [abs(patch.get_height()) for patch in ax.patches if isinstance(patch, Rectangle)]
        vertical = bool(widths) and max(heights) > hxy - 1e-6 and max(widths) < hxy - 1e-6
        for patch in ax.patches:
            if isinstance(patch, Rectangle) and abs(patch.get_width()) > 1e-9:
                key = round(patch.get_y() + patch.get_height() / 2, 6)
                rows.setdefault(key, []).append((patch.get_x(), patch.get_x() + patch.get_width()))
    finally:
        plt.close(fig)                                                     # only the checks below are shown here
    rows = [sorted(row) for row in rows.values()]

    def has_row(*intervals):
        return any(len(row) == len(intervals) and all(abs(a - c) < 1e-6 and abs(b - d) < 1e-6
                                                      for (a, b), (c, d) in zip(row, intervals)) for row in rows)

    if created:
        problems.append("draw_information_bars ouvre sa propre figure : dessine dans l'axe reçu")
    elif not rows:
        problems.append("il manque les barres horizontales (ax.barh)")
    elif vertical:
        problems.append("les barres doivent être horizontales : ax.barh(position, largeur, left=début), pas ax.bar")
    else:
        if not has_row((0, hxy - hy), (hxy - hy, hx)):
            problems.append("la barre de H(X) a deux morceaux : H(X | Y), de 0 à H(X | Y), puis I(X ; Y), jusqu'à H(X)")
        if not has_row((hxy - hy, hx), (hx, hxy)):
            problems.append("la barre de H(Y) commence à H(X | Y), sous le morceau I(X ; Y) de la barre de H(X), puis "
                            "continue par H(Y | X)")
        if not (has_row((0, hxy)) or has_row((0, hxy - hy), (hxy - hy, hx), (hx, hxy))):
            problems.append("la barre de H(X, Y) va de 0 à H(X, Y)")
        if not all(name in labels for name in ("H(X)", "H(Y)", "H(X,Y)")):
            problems.append("écris le nom de chaque barre sur l'axe vertical : H(X), H(Y), H(X, Y)")
        if "bit" not in xlabel.lower():
            problems.append("l'axe horizontal est en bits : écris-le (ax.set_xlabel)")
    if problems:
        print("❌ Ex M06.23 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M06.23 : les trois barres sont justes et alignées, avec leurs noms et leur unité.")'''

M06_23 = Ex(
    "M06.23", "🎨", 1, 20, "Un diagramme de l'information : H(X), H(Y), H(X | Y), I(X ; Y)",
    "dessiner les entropies d'un couple de variables en barres alignées, et y lire les règles de la chaîne et "
    "l'information mutuelle.", "fiche §3 et §4 ; R0 (matplotlib)", tracks="C",
    body=r"""Le diagramme de la fiche (§4) se dessine aussi en barres horizontales, à la même échelle :
- une barre « H(X) », faite de deux morceaux : $H(X \mid Y)$ puis $I(X ; Y)$ ;
- une barre « H(Y) », faite de $I(X ; Y)$ puis $H(Y \mid X)$, décalée pour que les deux morceaux $I(X ; Y)$ soient exactement l'un au-dessus de l'autre ;
- une barre « H(X, Y) », de 0 à $H(X, Y)$ (en un morceau, ou en trois).

Écris `draw_information_bars(ax, joint)`, qui dessine ces barres dans l'axe `ax` (`ax.barh(position, largeur, left=début)`), en bits, avec le nom de chaque barre sur l'axe vertical (`ax.set_yticks(positions, labels=[...])`, avec les noms `H(X)`, `H(Y)` et `H(X, Y)`) et le mot « bits » dans le nom de l'axe horizontal. Calcule les entropies avec tes fonctions de `mymath.info` (M06.16 et M06.17) ou avec NumPy. Puis dessine le diagramme du tableau `T23 = [[0.3, 0.05, 0.05], [0.1, 0.2, 0.3]]`.

Dans ta copie : lis sur ta figure les deux règles de la chaîne et les trois écritures de $I(X ; Y)$. À quoi ressemble la figure pour deux variables indépendantes ? Et si $Y = X$ ?""",
    todo='''def draw_information_bars(ax, joint):
    """In ax, three horizontal bars, in bits: H(X) = H(X | Y) + I(X ; Y), H(Y) = I(X ; Y) + H(Y | X) shifted so that
    the two I(X ; Y) pieces are aligned, and H(X, Y); the names of the bars on the vertical axis."""
    raise NotImplementedError("les entropies, puis ax.barh(..., left=...), ax.set_yticks et ax.set_xlabel")''',
    check='''with checked("M06.23 figure"):
    fig, ax = plt.subplots(figsize=(7, 3))
    try:
        created = drawn(draw_information_bars, ax, [[0.3, 0.05, 0.05], [0.1, 0.2, 0.3]])
    except BaseException:
        plt.close(fig)                                     # no empty figure while the function is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M06.23 : draw_information_bars ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans "
              "l'axe reçu.")
    else:
        plt.show()''',
    solution='''def draw_information_bars(ax, joint):
    """In ax, three horizontal bars, in bits: H(X) = H(X | Y) + I(X ; Y), H(Y) = I(X ; Y) + H(Y | X) shifted so that
    the two I(X ; Y) pieces are aligned, and H(X, Y); the names of the bars on the vertical axis."""
    joint = np.asarray(joint, dtype=float)
    h_xy = mymath.info.joint_entropy(joint)
    h_y_given_x = mymath.info.conditional_entropy(joint)
    h_x_given_y = mymath.info.conditional_entropy(joint.T)
    mi = mymath.info.mutual_information(joint)
    ax.barh(2, h_x_given_y, color="#4c72b0", label="H(X | Y)")
    ax.barh(2, mi, left=h_x_given_y, color="#8c8c8c", label="I(X ; Y)")
    ax.barh(1, mi, left=h_x_given_y, color="#8c8c8c")
    ax.barh(1, h_y_given_x, left=h_x_given_y + mi, color="#dd8452", label="H(Y | X)")
    ax.barh(0, h_xy, color="#55a868", label="H(X, Y)")
    ax.set_yticks([2, 1, 0], labels=["H(X)", "H(Y)", "H(X, Y)"])
    ax.set(xlabel="bits", title="Le diagramme de l'information")
    ax.legend(loc="lower right", fontsize=8)


fig, ax = plt.subplots(figsize=(7, 3))
draw_information_bars(ax, [[0.3, 0.05, 0.05], [0.1, 0.2, 0.3]])
plt.show()''',
    after=[("md", "**Vérifications automatiques** (sur un autre exemple ; la figure elle-même se juge à l'œil)."),
           ("code", M06_23_CHECK)],
    note=r"On lit $H(X) = H(X \mid Y) + I(X ; Y)$ sur la première barre, $H(Y) = I(X ; Y) + H(Y \mid X)$ sur la "
         r"deuxième, et $H(X, Y) = H(X \mid Y) + I(X ; Y) + H(Y \mid X)$ sur la troisième ; d'où les deux règles de la "
         r"chaîne, et $I = H(X) - H(X \mid Y) = H(Y) - H(Y \mid X) = H(X) + H(Y) - H(X, Y)$. Pour des variables "
         r"indépendantes, le morceau commun disparaît : les deux barres se suivent sans se chevaucher. Si $Y = X$, "
         r"$H(X \mid Y) = H(Y \mid X) = 0$ et les trois barres ont la même longueur.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M06.24 to M06.26)
# ---------------------------------------------------------------------------
M06_24_MISTAKES = bug_letters_mistakes(
    "ACD", "BEF",
    {"A": "refais chaque calcul avec une probabilité nulle : que vaut 0 × log₂ 0 pour NumPy ?",
     "C": "regarde la base de chaque logarithme",
     "D": "relis l'ordre des deux lois dans chaque formule"},
    name_correct=False)

M06_24 = Ex(
    "M06.24", "🐛", 1, 15, "Chasse à l'erreur : log en base 10, 0 log 0, KL à l'envers",
    "repérer dans du code les erreurs classiques sur l'entropie, la cross-entropy et la divergence KL, puis "
    "calculer les bonnes valeurs.", "fiche §1, §2, §5 et §8", tracks="C",
    body=r"""Des données suivent la loi `p`, un modèle la loi `q`. Un collègue a écrit six lignes, chacune avec un commentaire qui dit ce qu'elle veut calculer ; chaque ligne utilise les variables des lignes précédentes telles qu'elles **devraient** être (on suppose les lignes précédentes justes). Trois lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter de code**, trouve-les.

```python
p = np.array([0.5, 0.375, 0.125, 0.0])        # the law of the data
q = np.array([0.25, 0.5, 0.125, 0.125])       # the law of the model
H_p = -np.sum(p * np.log2(p))                 # (A) the entropy of p, in bits
H_p_nats = H_p * math.log(2)                  # (B) the same entropy, in nats
H_pq = -np.sum(p * np.log10(q))               # (C) the cross-entropy H(p, q), in bits
KL = np.sum(q * np.log2(q / p))               # (D) the divergence KL(p ‖ q), in bits
info_4 = -math.log2(q[3])                     # (E) the information of the 4th outcome under the model, in bits
perplexity = 2 ** H_pq                        # (F) the perplexity of the model on the data, 2 ** H(p, q)
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire (une liste de 6 nombres, 3 décimales).

Dans ta copie : pour chaque ligne fausse, que renvoie-t-elle (un nombre faux, `nan` ou `inf`), et comment la corriger ? Pourquoi le résultat d'une ligne fausse peut-il passer inaperçu ?""",
    todo='''answer_M06_24a = ...  # a) letters, as text
answer_M06_24b = ...  # b) a list of 6 values (3 decimals)''',
    check='''wbm.check("M06.24a", answer_M06_24a)
wbm.check("M06.24b", answer_M06_24b)''',
    solution='''answer_M06_24a = "ACD"
p = np.array([0.5, 0.375, 0.125, 0.0])
q = np.array([0.25, 0.5, 0.125, 0.125])
seen = p > 0                                            # 0 log 0 counts as 0: keep the outcomes seen in the data
H_p = -np.sum(p[seen] * np.log2(p[seen]))               # (A) without the filter: 0 × (−inf) = nan
H_p_nats = H_p * math.log(2)                            # (B) correct
H_pq = -np.sum(p[seen] * np.log2(q[seen]))              # (C) log2, not log10
KL = np.sum(p[seen] * np.log2(p[seen] / q[seen]))       # (D) p in front, p / q: KL(q ‖ p) would be infinite here
info_4 = -math.log2(q[3])                               # (E) correct
perplexity = 2 ** H_pq                                  # (F) correct
answer_M06_24b = [float(value) for value in (H_p, H_p_nats, H_pq, KL, info_4, perplexity)]
print(answer_M06_24a, [round(value, 4) for value in answer_M06_24b])''',
    record=f'''wbm.record("M06.24a", "ACD",
           mistakes={M06_24_MISTAKES})
wbm.record("M06.24b", [1.4056390622295665, 0.9743147528693494, 1.75, 0.34436093777043353, 3.0, 3.363585661014858],
           decimals=3,
           mistakes={{"une de tes valeurs reprend ce que calcule une ligne fausse, pas ce que dit son commentaire : "
                     "refais le calcul de chaque ligne fausse à partir de son commentaire":
                         [1.4056390622295665, 0.9743147528693494, 0.5268024924119671, 0.34436093777043353, 3.0,
                          3.363585661014858],
                     "une de tes valeurs utilise l'entropie là où le commentaire demande une autre quantité : relis "
                     "chaque commentaire":
                         [1.4056390622295665, 0.9743147528693494, 1.75, 0.34436093777043353, 3.0, 2 ** 1.4056390622295665]}})''',
    note=r"(A) $0 \times \log_2 0$ vaut `nan` pour NumPy ($0 \times (-\infty)$) : la somme est `nan` ; il faut ne garder "
         r"que les probabilités non nulles (ou `xlogy`, M06.25). La bonne valeur : $0{,}5 + 0{,}375\log_2\frac{8}{3} + "
         r"0{,}375 \approx 1{,}406$ bit. (C) `log10` donne la cross-entropy en « bans », $1{,}75 \log_{10} 2 \approx 0{,}527$ : "
         r"la bonne valeur est $H(p, q) = 0{,}5 \times 2 + 0{,}375 \times 1 + 0{,}125 \times 3 = 1{,}75$ bit. (D) Les deux "
         r"lois sont échangées : c'est $\mathrm{KL}(q \,\|\, p)$, infinie ici car $q$ donne une probabilité à la 4ᵉ "
         r"issue et $p$ non ; $\mathrm{KL}(p \,\|\, q) = 1{,}75 - 1{,}406 \approx 0{,}344$. (B), (E) et (F) sont justes : "
         r"$1{,}406 \ln 2 \approx 0{,}974$ nat, $-\log_2 0{,}125 = 3$ bits, $2^{1{,}75} \approx 3{,}364$. Une ligne "
         r"fausse qui renvoie un nombre plausible, comme (C), passe facilement inaperçue ; `nan` et `inf` se voient.",
)

M06_25_CHECK = """with checked("M06.25 vérifications"):
    import inspect
    import re
    import warnings
    problems = []
    tables_t = [[[0.5, 0.0], [0.2, 0.3]], [[0.1, 0.1, 0.0], [0.0, 0.0, 0.8]], [[0.25], [0.75]],
                [[0.05, 0.15, 0.2], [0.3, 0.1, 0.2]]]
    for table in tables_t:
        array_t = np.asarray(table, dtype=float)
        expected = []
        for row in array_t:
            law = row[row > 0] / row.sum()
            expected.append(float(-np.sum(law * np.log2(law))) + 0.0)
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            got = row_entropies(table)
        if got is None:
            problems.append("row_entropies ne renvoie rien : il manque return")
            break
        if caught:
            problems.append(f"row_entropies({table}) émet un avertissement ({caught[0].category.__name__}) : xlogy "
                            "n'en émet pas, même pour une probabilité nulle")
            break
        if not isinstance(got, np.ndarray) or got.dtype != float:
            problems.append(f"renvoie un tableau NumPy de flottants, pas un {type(got).__name__}")
            break
        if got.shape != (len(table),) or not np.allclose(got, expected, atol=1e-12):
            problems.append(f"row_entropies({table}) devrait valoir {np.round(expected, 6).tolist()}, pas "
                            f"{np.round(np.asarray(got, dtype=float), 6).tolist()} : chaque ligne divisée par sa somme, "
                            "puis son entropie")
            break
    if not problems:
        nats_t = row_entropies([[0.2, 0.3, 0.5]], base=math.e)
        if not np.allclose(nats_t, [-sum(v * math.log(v) for v in (0.2, 0.3, 0.5))], atol=1e-12):
            problems.append("avec base=math.e, le résultat est en nats : divise par ln(base)")
    if not problems:
        try:
            source_t = inspect.getsource(row_entropies)
        except (OSError, TypeError):
            source_t = ""
        code_t = "\\n".join(line.split("#")[0] for line in source_t.splitlines()[1:])
        if source_t and "xlogy" not in code_t:
            problems.append("l'exercice demande xlogy : sers-t'en pour les termes p log p")
        elif source_t and (re.search(r"\\bfor\\b|\\bwhile\\b", code_t) or re.search(r"[<>]=?\\s*0\\b", code_t)):
            problems.append("ni boucle ni filtre : xlogy s'occupe des probabilités nulles, et NumPy de toutes les lignes "
                            "à la fois (axis=1)")
    if problems:
        print("❌ Ex M06.25 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M06.25 : row_entropies est juste, avec xlogy, sans boucle ni avertissement.")"""

M06_25 = Ex(
    "M06.25", "🛠️", 1, 10, "Calculer 0 log 0 proprement (`scipy.special.xlogy`)",
    "calculer d'un coup les entropies des lignes d'une loi jointe, sans `nan` ni avertissement quand des "
    "probabilités sont nulles, avec la fonction de SciPy faite pour cela.", "fiche §2 et §3 ; Ex M06.24", tracks="C",
    body=r"""`p * np.log2(p)` vaut `nan` dès qu'une probabilité est nulle ($0 \times (-\infty)$), avec un avertissement. Le filtre `p[p > 0]` règle le problème pour un vecteur, mais il aplatit le tableau : il ne convient plus quand on veut une entropie **par ligne**. SciPy a une fonction faite pour cela : `scipy.special.xlogy(x, y)` calcule $x \ln y$ case par case, et renvoie 0 quand $x = 0$, même si $y = 0$, sans avertissement.

Écris `row_entropies(joint, base=2)`, qui renvoie, pour une loi jointe `joint` dont aucune ligne n'est nulle, le tableau NumPy des entropies $H(Y \mid X = x)$ de ses lignes, chacune divisée par sa somme (fiche §3) : avec `xlogy`, sans boucle ni filtre (`keepdims=True` garde la forme d'une somme par ligne, `axis=1` somme chaque ligne). La vérification compare ta fonction à un calcul de référence sur plusieurs tableaux, dont des probabilités nulles, vérifie qu'elle n'émet aucun avertissement et qu'elle utilise `xlogy` sans boucle ni filtre ; puis elle calcule `row_entropies(T25)` pour `T25 = [[0.2, 0, 0.1], [0.14, 0.2, 0.06], [0, 0.3, 0]]` (une liste de 3 nombres, 4 décimales).

Dans ta copie : pourquoi la convention $0 \log 0 = 0$ est-elle la bonne (quelle est la limite de $x \ln x$ quand $x$ tend vers 0 ?) ? Calcule $H(Y \mid X)$ pour `T25` à partir de ta liste. Pourquoi la troisième ligne a-t-elle une entropie nulle ?""",
    todo='''from scipy.special import xlogy


def row_entropies(joint, base=2):
    """The entropies H(Y | X = x) of the rows of joint, each divided by its sum, with xlogy: no loop, no filter."""
    raise NotImplementedError("relis ce que calcule xlogy(x, y), puis pense à une somme par ligne")''',
    check=M06_25_CHECK + """
with checked("M06.25"):
    wbm.check("M06.25", [float(v) for v in row_entropies([[0.2, 0, 0.1], [0.14, 0.2, 0.06], [0, 0.3, 0]])],
              computed=True)""",
    solution='''from scipy.special import xlogy


def row_entropies(joint, base=2):
    """The entropies H(Y | X = x) of the rows of joint, each divided by its sum, with xlogy: no loop, no filter."""
    table = np.asarray(joint, dtype=float)
    conditional = table / table.sum(axis=1, keepdims=True)
    return -xlogy(conditional, conditional).sum(axis=1) / math.log(base) + 0.0


T25 = [[0.2, 0, 0.1], [0.14, 0.2, 0.06], [0, 0.3, 0]]
print(row_entropies(T25), "· H(Y | X) =", float(np.sum(np.sum(T25, axis=1) * row_entropies(T25))))''',
    after=[("solution", M06_25_CHECK)],
    record='''wbm.record("M06.25", [0.9182958340544894, 1.440645449615346, 0.0], decimals=4,
           mistakes={"la fonction donne des bits par défaut (base=2) : divise par ln 2":
                         [0.6365141682948128, 0.9985793315873919, 0.0],
                     "divise d'abord chaque ligne par sa somme : les entropies portent sur les lois conditionnelles":
                         [0.7965784284662087, 1.1050294178010835, 0.5210896782498619]})''',
    note=r"$x \ln x \to 0$ quand $x \to 0^+$ (avec $x = \frac{1}{t}$, $x \ln x = -\frac{\ln t}{t}$ tend vers 0, R6) : "
         r"une issue impossible n'apporte rien à l'entropie, d'où la convention. Les lignes de `T25`, divisées par leur "
         r"somme, sont $(\frac{2}{3}, 0, \frac{1}{3})$, $(0{,}35 ;\ 0{,}5 ;\ 0{,}15)$ et $(0, 1, 0)$ : leurs entropies "
         r"valent environ 0,9183, 1,4406 et 0 (la troisième loi est certaine). $H(Y \mid X) \approx 0{,}3 \times 0{,}9183 "
         r"+ 0{,}4 \times 1{,}4406 \approx 0{,}8517$.",
)

M06_26_GIVEN = """PROBS_UNIFORM_26 = np.full(100, 0.01)                      # probs[k]: the probability of the server k + 1
PROBS_AGE_26 = 1 / np.arange(1, 101)
PROBS_AGE_26 = PROBS_AGE_26 / PROBS_AGE_26.sum()               # the probability of server n is proportional to 1/n"""

M06_26_CHECK = """with checked("M06.26 défi"):
    problems, results = [], {}
    for law_name, probs_t in [("uniforme", PROBS_UNIFORM_26), ("en 1/n", PROBS_AGE_26)]:
        counts_t = []
        for faulty in range(1, 101):
            questions = []

            def is_at_most(t, faulty=faulty, questions=questions):
                questions.append(t)
                if len(questions) > 200:
                    raise RuntimeError("plus de 200 questions : ta stratégie tourne en rond")
                return faulty <= t

            try:
                got = locate_fault(is_at_most, list(probs_t))
            except NotImplementedError:
                raise
            except Exception as exc:  # noqa: BLE001
                problems.append(f"loi {law_name}, serveur {faulty} : locate_fault lève {type(exc).__name__} ({exc})")
                break
            if got != faulty:
                problems.append(f"loi {law_name} : pour une panne sur le serveur {faulty}, locate_fault renvoie {got!r}")
                break
            counts_t.append(len(questions))
        if problems:
            break
        results[law_name] = (max(counts_t), float(np.dot(probs_t, counts_t)))
    if problems:
        print("❌ Ex M06.26 : " + problems[0] + ".")
    else:
        worst_u, mean_u = results["uniforme"]
        mean_a = results["en 1/n"][1]
        print(f"loi uniforme : {worst_u} questions au plus, {mean_u:.3f} en moyenne · loi en 1/n : {mean_a:.3f} en "
              "moyenne")
        failures = []
        if worst_u > 7:
            failures.append("plus de 7 questions pour un des serveurs, avec la loi uniforme")
        if mean_u > 6.72 + 1e-9:
            failures.append("plus de 6,72 questions en moyenne avec la loi uniforme")
        if mean_a > 5.50 + 1e-9:
            failures.append("plus de 5,50 questions en moyenne avec la loi en 1/n : sers-toi des probabilités pour "
                            "choisir chaque question")
        if failures:
            print("❌ Ex M06.26 : objectif pas encore atteint : " + " ; ".join(failures) + ".")
        else:
            print("✅ Ex M06.26 : défi réussi, les deux objectifs sont atteints.")"""

M06_26 = Ex(
    "M06.26", "🏆", 3, 25, "Défi : localiser une panne parmi 100 serveurs en un minimum de questions",
    "concevoir une stratégie de questions par oui ou non qui approche l'entropie, pour une loi uniforme et pour une "
    "loi inégale.", "fiche §2 et §7", tracks="C",
    body=r"""Cent serveurs, numérotés de 1 à 100, sont branchés à la suite ; l'un d'eux est en panne. Un test indique si la panne est sur l'un des serveurs 1 à $t$ (« oui » ou « non ») : chaque test est une question. Chaque suite de réponses est un mot d'un code préfixe binaire (fiche §7) : en moyenne, il faut donc au moins $H$ questions, où $H$ est l'entropie de la loi du serveur en panne. Des questions de cette forme, qui coupent toujours la liste en deux morceaux, permettent toujours de faire moins de $H + 2$ en moyenne, et souvent bien mieux… à condition de bien les choisir.

Écris `locate_fault(is_at_most, probs)`, qui trouve le serveur en panne en appelant `is_at_most(t)` (qui renvoie `True` si la panne est sur l'un des serveurs 1 à `t`), et renvoie son numéro. `probs[k]` est la probabilité que la panne soit sur le serveur `k + 1` : ta stratégie peut s'en servir. **Les objectifs** :
- quand tous les serveurs ont la même probabilité : au plus 7 questions pour chaque serveur, et au plus 6,72 en moyenne ;
- quand la probabilité du serveur $n$ est proportionnelle à $\frac{1}{n}$ (les premiers, les plus anciens, tombent plus souvent en panne) : au plus 5,50 questions en moyenne, pondérée par les probabilités.

La vérification essaie ta fonction sur les 100 serveurs, pour les deux lois, en comptant les questions. Elle vérifie aussi `bound_26`, l'entropie en bits de la seconde loi, que tu calcules (4 décimales) : le nombre moyen de questions ne peut pas descendre en dessous.

Dans ta copie : pourquoi 6,72 est-il le mieux possible pour la loi uniforme (combien de serveurs peut-on distinguer avec 6 questions ? avec 7 ?) ? Pourquoi couper la liste en deux moitiés de même longueur ne suffit-il pas pour la seconde loi ? Compare ton score à `bound_26`.""",
    given=M06_26_GIVEN,
    todo='''def locate_fault(is_at_most, probs):
    """The faulty server (1 to len(probs)), found with tests is_at_most(t) -> bool; probs[k] is the probability of k + 1."""
    raise NotImplementedError("garde la liste des serveurs encore possibles, et coupe-la en deux parts bien choisies")


bound_26 = ...  # the entropy, in bits, of PROBS_AGE_26 (4 decimals)''',
    check=M06_26_CHECK + """
with checked("M06.26"):
    wbm.check("M06.26", bound_26)""",
    solution='''def locate_fault(is_at_most, probs):
    """The faulty server (1 to len(probs)), found with tests is_at_most(t) -> bool; probs[k] is the probability of k + 1."""
    lo, hi = 1, len(probs)                                   # the faulty server is in lo..hi
    cumulative = np.concatenate([[0.0], np.cumsum(probs)])   # cumulative[k] = P(faulty server <= k)
    while lo < hi:
        middle = (cumulative[lo - 1] + cumulative[hi]) / 2   # half of the probability left
        candidates = np.arange(lo, hi)
        t = int(candidates[np.argmin(np.abs(cumulative[candidates] - middle))])
        if is_at_most(t):
            hi = t
        else:
            lo = t + 1
    return lo


p_26 = PROBS_AGE_26
bound_26 = float(-np.sum(p_26 * np.log2(p_26)))
print("entropy of the 1/n law:", bound_26, "· of the uniform law:", math.log2(100))''',
    after=[("solution", M06_26_CHECK)],
    record='''wbm.record("M06.26", 5.310239799410162, decimals=4,
           mistakes={"la question demande des bits : log₂, pas ln": 3.680777745058364,
                     "c'est l'entropie de la loi uniforme : calcule celle de PROBS_AGE_26": 6.643856189774724})''',
    note=r"Avec 6 questions, on distingue au plus $2^6 = 64$ serveurs, avec 7, $2^7 = 128$ : pour 100 serveurs, il faut "
         r"7 questions pour certains ; au mieux, 28 serveurs en demandent 6 et 72 en demandent 7, soit $\frac{28 \times 6 "
         r"+ 72 \times 7}{100} = 6{,}72$ en moyenne (l'entropie vaut $\log_2 100 \approx 6{,}64$). Pour la loi en "
         r"$\frac{1}{n}$, couper la liste en deux moitiés de même longueur pose autant de questions pour le serveur 1, très "
         r"probable, que pour le 100, très rare : environ 6,83 en moyenne. Couper la **probabilité** restante en deux "
         r"parts aussi égales que possible donne environ 5,37 questions en moyenne, tout près de l'entropie, environ "
         r"5,31 bits : les serveurs probables reçoivent des mots courts, comme dans un bon code.",
)

PART_A = Part("A", "Ta librairie : entropies d'un tableau, information mutuelle, Kraft, Jensen ; scikit-learn",
              "Fiche §3, §4, §6 et §7. Les six fonctions de `mymath/info.py`, puis l'information mutuelle de "
              "scikit-learn.",
              given=TOOLS, exercises=[M06_16, M06_17, M06_18, M06_19, M06_20])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §2, §3 et §4. L'information mutuelle d'une variable avec une fonction d'elle-même, le biais de "
              "l'entropie estimée sur un petit échantillon, le diagramme de l'information en barres.",
              exercises=[M06_21, M06_22, M06_23])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §1, §2, §5 et §7. Trois erreurs à trouver, 0 log 0 calculé proprement, puis une panne à localiser "
              "en un minimum de questions.",
              exercises=[M06_24, M06_25, M06_26])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M06.1 à M06.9, M06.12, M06.13 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M06 · Théorie de l'information — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m06_information/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M06`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M06 · Théorie de l'information — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : information et entropie, entropies conjointe et "
               "conditionnelle, information mutuelle, cross-entropy et KL, inégalité de Jensen, Kraft, longueur "
               "moyenne d'un code, log loss d'un classifieur, choix d'une feature.\n"
               "- Écrire les six fonctions de `mymath/info.py` et les tester, puis utiliser scikit-learn.\n"
               "- Prédire l'information mutuelle de $X$ avec $X^3$ et $X^2$, mesurer le biais de l'entropie estimée, "
               "dessiner le diagramme de l'information, chasser des erreurs, calculer $0 \\log 0$ proprement, localiser "
               "une panne en un minimum de questions.\n\n"
               "**Rappel express.** $H(X) = -\\sum p \\log_2 p$ ; $H(X, Y) = H(X) + H(Y \\mid X)$ ; $I(X ; Y) = "
               "H(Y) - H(Y \\mid X) = H(X) + H(Y) - H(X, Y) \\ge 0$ ; $H(p, q) = -\\sum p \\log_2 q = H(p) + "
               "\\mathrm{KL}(p \\,\\|\\, q)$ ; Jensen : $\\mathbb{E}[f(X)] \\ge f(\\mathbb{E}[X])$ pour $f$ convexe ; "
               "Kraft : $\\sum 2^{-\\ell_i} \\le 1$ ; le meilleur code préfixe vérifie $H \\le \\bar{L} < H + 1$ ; "
               "1 nat $\\approx 1{,}443$ bit.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu calculer l'information d'un événement et l'entropie d'une loi, en bits et en nats ?\n"
               "2. Sais-tu calculer des entropies conjointe et conditionnelle et une information mutuelle à partir "
               "d'un tableau, et dire ce que mesure chacune ?\n"
               "3. Sais-tu calculer une cross-entropy et une divergence KL, les lire en bits perdus, et dire pourquoi "
               "la KL est positive (Jensen) ?\n"
               "4. Sais-tu dire si des longueurs de code sont possibles (Kraft), et comparer la longueur moyenne d'un "
               "code à l'entropie ?\n\n"
               "**La suite** : le chapitre 6 de workbookIA (entropie, cross-entropy, KL, codes), puis CP1, l'examen "
               "blanc de la partie I.")]


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
