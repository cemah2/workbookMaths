#!/usr/bin/env python
"""Build the two notebooks of chapter M27 from a single source (used by Claude).

    python tools/chapters/build_m27.py
    python tools/run_all_notebooks.py chapitres/m27_jeux_distances/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m27_jeux_distances/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M27.1 to M27.10 and 🔗 M27.16), each answer computed in the notebook from the data
of its statement (exact fractions where the calculation is exact; math, NumPy and SciPy otherwise), each wrong value
computed by the error its message names; parts A to D are the notebook exercises (M27.19 to M27.29), exactly as
02_exercices.md describes them. Wrong-answer messages state a rule, never a number of the answer, the last step that
gives it, nor another sub-question.

Data. The notebook exercises take the data of the paper exercises (a data cell of part A: the market of M27.1, the
penalty kicks of M27.2, the depots and the stores of M27.7, the bags of M27.8, the machine of M27.16), the games and the
laws of their own statements, and their own random draws. Seeds 6401 to 6449 only (the tests use 6300 to 6390, the
figures of the fiche 6391 to 6399): those of the statements, 6425 (M27.25) and 6428 (M27.28); and, for the hidden cases
of the check cells, 6423 (the cost matrix of transport_lp_23), 6426 (the hidden case of distance_bias_25), 6427 (the
hidden cases of the corrected functions of M27.27), 6441 and 6442 (the two hidden starts of the property test of
M27.28). No step η of 0.2, 0.25, 0.4, 0.5 or 1 on xy (the fiche, the stub, M22): η = 0.6, 0.3, 2.5 (statements) and 0.45
(a hidden path). The check cells use their own games and laws, never the test cases of tests/test_m27_distances.py, the
examples of the docstrings of the stub distances ([[7, -4, 1], [-1, 5, 6]], [[1, 6, 2], [4, 5, 4], [0, 8, 3]],
[[4, -2], [-1, 3]], [[-1, 2], [5, 6]], A = [[2]] with η = 0.25, (10, 1, 2, 16), (-1, 0.5, -1, 3.5)), the examples of the
fiche (the handball, the volley, the fishermen, the file formats, the earth of Monge, the two routes, the apples, the
anemometer, the orders), nor the numbers of workbookIA 27, B7 and its checkpoint VI (the notes of M27 in the syllabus and
their list « Évités »).

Every expected value of a check cell is computed at build time (reference implementation, NumPy, SciPy and private
functions of this script) and written in the cell as a literal: no check cell holds the code that solves an exercise.
"""

from __future__ import annotations

import importlib.util
import json
import math
import pprint
import re
import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (ROOT, STARS, Ex, Paper, Part, badge, check_unique_keys, guarded,  # noqa: E402,F401
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M27"
FOLDER = "chapitres/m27_jeux_distances"

FRACTION = 'an irreducible fraction, as text "p/q"'
BOOL = "True or False"


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M27.1", "Deux enseignes se partagent un marché : dominance, points selles, maximin et minimax", [
        ("a", "a list of 2 numbers: the maximin, then the minimax", "floats([max(row_minima(G_1)), min(column_maxima(G_1))])",
         '''decimals=6,
           mistakes={"le minimax se lit sur les maximums des colonnes (le pire, pour le joueur qui paie), pas sur leurs "
                     "minimums": floats([max(row_minima(G_1)), min(min(column) for column in zip(*G_1))]),
                     "le maximin se lit sur les minimums des lignes (ce que chaque ligne garantit), pas sur leurs maximums":
                         floats([max(max(row) for row in G_1), min(column_maxima(G_1))])}'''),
        ("b", "a list of pairs [row, column], numbered from 1, like [[1, 2], [3, 1]]", "saddles(G_1)",
         '''mistakes={"un point selle est le plus petit de sa ligne et le plus grand de sa colonne, pas l'inverse":
                         saddles(G_1, flipped=True),
                     "un minimum de ligne peut être atteint dans plusieurs cases : examine chacune": saddles(G_1)[:1],
                     "dans ta réponse, les lignes et les colonnes se numérotent à partir de 1":
                         [[i - 1, j - 1] for i, j in saddles(G_1)],
                     "range les points selles dans l'ordre des lignes, puis des colonnes": saddles(G_1)[::-1]}'''),
        ("c", BOOL, "dominated_column(G_1, 0)",
         '''mistakes={"dans G, on n'a encore rien rayé : une colonne n'y est strictement dominée que si elle coûte plus "
                     "qu'une même autre colonne sur les trois lignes": True}'''),
        ("d", "a matrix, as the list of its rows", "floats(reduce_dominated(G_1))",
         '''decimals=6,
           mistakes={"les dominances s'enchaînent : après chaque stratégie rayée, compare de nouveau toutes les lignes et "
                     "toutes les colonnes": floats(reduce_dominated(G_1, rounds=1)),
                     "la dominance stricte demande une inégalité stricte sur chaque ligne : une égalité ne suffit pas pour "
                     "rayer une colonne": floats(reduce_dominated(G_1, strict=False))}'''),
    ]),

    Paper("M27.2", "Tirs au but : les stratégies d'indifférence, la valeur, et une stratégie qui s'en écarte", [
        ("a", FRACTION, "str(P_2)",
         '''kind="fraction", simplified=True,
           mistakes={"p* rend l'adversaire (le gardien) indifférent : il se calcule avec les colonnes de G":
                         str(indifferent(G_2[0], G_2[1])),
                     "p est la probabilité de la première ligne (tirer à gauche)": str(1 - P_2)}'''),
        ("b", FRACTION, "str(Q_2)",
         '''kind="fraction", simplified=True,
           mistakes={"q* rend le tireur indifférent : il se calcule avec les lignes de G":
                         str(indifferent(*columns(G_2))),
                     "q est la probabilité de la première colonne (plonger à gauche)": str(1 - Q_2)}'''),
        ("c", "a number (2 decimals)", "floats(V_2)",
         '''decimals=2,
           mistakes={"la valeur n'est pas le milieu du maximin et du minimax : c'est le gain espéré quand chacun joue sa "
                     "stratégie optimale": floats((max(row_minima(G_2)) + min(column_maxima(G_2))) / 2),
                     "le gain espéré se calcule avec p* pour les lignes et q* pour les colonnes":
                         floats(expected(G_2, Q_2, P_2))}'''),
        ("d", "a number (2 decimals)", "floats(max(expected(G_2, F(1), Q_D_2), expected(G_2, F(0), Q_D_2)))",
         '''decimals=2,
           mistakes={"contre une stratégie fixée du gardien, compare les gains espérés des deux tirs purs et garde le plus "
                     "grand": floats(min(expected(G_2, F(1), Q_D_2), expected(G_2, F(0), Q_D_2))),
                     "0,65 est la probabilité de plonger à gauche : elle pondère la première colonne":
                         floats(max(expected(G_2, F(1), 1 - Q_D_2), expected(G_2, F(0), 1 - Q_D_2)))}'''),
        ("e", "a number (2 decimals)", "floats(min(expected(G_2, P_E_2, F(1)), expected(G_2, P_E_2, F(0))))",
         '''decimals=2,
           mistakes={"ce que s'assure le tireur est son plus petit gain espéré sur les choix du gardien":
                         floats(max(expected(G_2, P_E_2, F(1)), expected(G_2, P_E_2, F(0)))),
                     "0,55 est la probabilité de la première ligne (tirer à gauche)":
                         floats(min(expected(G_2, 1 - P_E_2, F(1)), expected(G_2, 1 - P_E_2, F(0))))}'''),
    ]),

    Paper("M27.3", "Un dilemme du prisonnier, un jeu de coordination asymétrique, et des allumettes", [
        ("a", "a list of 2 numbers: the gains (rows, columns) at the equilibrium",
         "[ROWS_3[i][j] for i, j in pure_nash(ROWS_3, COLS_3)] + [COLS_3[i][j] for i, j in pure_nash(ROWS_3, COLS_3)]",
         '''decimals=6,
           mistakes={"un équilibre de Nash n'est pas l'issue la meilleure pour les deux : vérifie que chaque stratégie est "
                     "une meilleure réponse à l'autre": [ROWS_3[0][0], COLS_3[0][0]]}'''),
        ("b", BOOL, "(0, 0) in pure_nash(ROWS_3, COLS_3)",
         '''mistakes={"contre M, l'autre boulangerie a-t-elle intérêt à rester sur M ?": True}'''),
        ("c", FRACTION, "str(X_3)",
         '''kind="fraction", simplified=True,
           mistakes={"x rend l'autre équipe indifférente : il se calcule avec les gains de l'équipe des colonnes":
                         str(indifferent(TEAM_ROWS_3[0], TEAM_ROWS_3[1])),
                     "x est la probabilité de X, pas celle de Y": str(1 - X_3)}'''),
        ("d", FRACTION, "str(Y_3)",
         '''kind="fraction", simplified=True,
           mistakes={"y rend l'équipe des lignes indifférente : il se calcule avec les gains de l'équipe des lignes":
                         str(indifferent(*columns(TEAM_COLS_3))),
                     "y est la probabilité de X, pas celle de Y": str(1 - Y_3)}'''),
        ("e", "a list of 2 numbers (3 decimals)", "floats(GAINS_3)",
         '''decimals=3,
           mistakes={"le gain moyen d'une équipe dépend de la stratégie de l'autre, pas de sa propre probabilité":
                         floats([TEAM_ROWS_3[0][0] * X_3, TEAM_COLS_3[0][0] * Y_3]),
                     "le premier nombre est le gain de l'équipe des lignes": floats(GAINS_3[::-1])}'''),
        ("f", "a list of integers, in increasing order", "losing(12, (1, 2), last_loses=True)",
         '''mistakes={"ici, celui qui prend la dernière allumette perd : avec 1 allumette, on est obligé de la prendre":
                         losing(12, (1, 2), last_loses=False),
                     "on retire 1 ou 2 allumettes, pas 3": losing(12, (1, 2, 3), last_loses=True)}'''),
        ("g", "an integer", "winning_move(11, (1, 2), last_loses=True)",
         '''mistakes={"dans ce jeu, celui qui prend la dernière allumette perd : laisse à l'adversaire une position perdante "
                     "de ce jeu-là": winning_move(11, (1, 2), last_loses=False)}'''),
    ]),

    Paper("M27.4", "Descente-montée sur xy : modules, angles, et deux pas différents", [
        ("a", "a number (4 decimals)", "math.sqrt(1 + ETA_4 ** 2)",
         '''decimals=4,
           mistakes={"le module de 1 ± iη est √(1 + η²), pas 1 + η²": 1 + ETA_4 ** 2,
                     "le module de 1 ± iη est √(1 + η²), pas 1 + η": 1 + ETA_4}'''),
        ("b", "a number (1 decimal)", "math.degrees(math.atan(ETA_4))",
         '''decimals=1,
           mistakes={"l'angle est demandé en degrés": math.atan(ETA_4),
                     "l'argument de 1 + iη est arctan η, pas η": math.degrees(ETA_4)}'''),
        ("c", "an integer", "math.ceil(math.log(2) / math.log(math.sqrt(1 + ETA_4 ** 2)))",
         '''mistakes={"la distance est multipliée à chaque pas par le module de a), pas par son carré":
                         math.ceil(math.log(2) / math.log(1 + ETA_4 ** 2)),
                     "il faut au moins doubler : arrondis à l'entier supérieur":
                         math.floor(math.log(2) / math.log(math.sqrt(1 + ETA_4 ** 2)))}'''),
        ("d", "a number (1 decimal)", "math.degrees(math.acos((2 - ETA_4 ** 2) / 2))",
         '''decimals=1,
           mistakes={"le pas alterné n'a pas la matrice du pas simultané : cherche les valeurs propres de M_a":
                         math.degrees(math.atan(ETA_4)),
                     "l'angle est demandé en degrés, pour le pas alterné aussi": math.acos((2 - ETA_4 ** 2) / 2)}'''),
        ("e", "a list of 2 numbers (4 decimals)", "[radius(step_matrix(1.5, 0.6)), radius(step_matrix(1.5, 0.6, True))]",
         '''decimals=4,
           mistakes={"en simultané, le déterminant vaut 1 + ab : les deux pas comptent":
                         [radius(step_matrix(1.5, 1.5)), radius(step_matrix(1.5, 0.6, True))],
                     "en alterné, le déterminant reste 1 quels que soient les pas":
                         [radius(step_matrix(1.5, 0.6)), radius(step_matrix(1.5, 0.6))]}'''),
        ("f", "a number (2 decimals)", "radius(step_matrix(4, 1.5, True))",
         '''decimals=2,
           mistakes={"avec ab > 4, les deux valeurs propres sont réelles, de produit 1 : le rayon spectral est la plus "
                     "grande en valeur absolue, pas la racine du déterminant":
                         math.sqrt(abs(np.linalg.det(step_matrix(4, 1.5, True)))),
                     "la trace du pas alterné vaut 2 − ab, pas 2 − a − b": max(abs(np.roots([1, -(2 - 4 - 1.5), 1])))}'''),
    ]),

    Paper("M27.5", "Deux fournisseurs, un défaut sur quatre niveaux : a posteriori et log-loss de trois prédicteurs", [
        ("a", "a number (3 decimals)", "floats(PX_5[0])",
         '''decimals=3,
           mistakes={"P(X = 0) pondère chaque fournisseur par sa part des pièces": floats((P0_5[0] + P1_5[0]) / 2),
                     "les pièces des deux fournisseurs peuvent avoir le niveau 0": floats(JOINT0_5[0])}'''),
        ("b", "a list of 4 numbers (3 decimals)", "floats(POST_5)",
         '''decimals=3,
           mistakes={"t*(x) est la probabilité du fournisseur B sachant le niveau, pas celle du niveau sachant B":
                         floats(P1_5),
                     "t*(x) est la probabilité du fournisseur B (Y = 1), pas celle du fournisseur A":
                         floats([1 - t for t in POST_5])}'''),
        ("c", "a number (4 decimals)", "risk_5([PI1_5] * 4)",
         '''decimals=4,
           mistakes={"−ln t est pondéré par P(Y = 1), et −ln(1 − t) par P(Y = 0)": risk_5([PI1_5] * 4, swapped=True),
                     "la log-loss se calcule avec le logarithme népérien (nats)": risk_5([PI1_5] * 4, log=math.log2)}'''),
        ("d", "a number (4 decimals)", "risk_5(POST_5)",
         '''decimals=4,
           mistakes={"la moyenne porte sur les quatre niveaux pondérés par P(X = x), pas à parts égales":
                         sum(entropy_5(t) for t in POST_5) / 4,
                     "la log-loss se calcule avec le logarithme népérien (nats), pour t* aussi": risk_5(POST_5, log=math.log2)}'''),
        ("e", "a number (4 decimals)", "risk_5(OVER_5)",
         '''decimals=4,
           mistakes={"la log-loss se calcule avec le logarithme népérien (nats), pour ce prédicteur aussi":
                         risk_5(OVER_5, log=math.log2),
                     "−ln t(x) est pondéré par P(X = x, Y = 1), et −ln(1 − t(x)) par P(X = x, Y = 0)":
                         risk_5(OVER_5, swapped=True)}'''),
    ]),

    Paper("M27.6", "Deux lois uniformes de même largeur, translatées : JS, KL et W₁", [
        ("a", "a number (3 decimals)", "js_shifted(F(1))",
         '''decimals=3,
           mistakes={"JS se calcule avec le logarithme népérien (nats)": js_shifted(F(1), log=math.log2),
                     "JS = ½ KL(p ‖ m) + ½ KL(q ‖ m) : n'oublie pas les facteurs ½": js_shifted(F(1), half=False)}'''),
        ("b", "a number (3 decimals)", "js_shifted(F(3))",
         '''decimals=3,
           mistakes={"JS se calcule avec le logarithme népérien (nats), à θ = 3 aussi": js_shifted(F(3), log=math.log2),
                     "n'oublie pas les facteurs ½ de la définition (et JS ≤ ln 2)": js_shifted(F(3), half=False)}'''),
        ("c", "a list of 2 numbers (3 decimals)", "[js_shifted(F(8)), js_shifted(F(80))]",
         '''decimals=3,
           mistakes={"à θ = 8, les supports ne se recouvrent plus : refais le calcul de m sur chaque morceau":
                         [js_shifted(F(8), capped=False), js_shifted(F(80), capped=False)],
                     "JS se calcule avec le logarithme népérien (nats), pour des supports disjoints aussi":
                         [js_shifted(F(8), log=math.log2), js_shifted(F(80), log=math.log2)]}'''),
        ("d", BOOL, "min(F(1), WIDTH_6) == 0",
         '''mistakes={"regarde s'il existe une zone où p est positive et q nulle": True}'''),
        ("e", "a list of 2 numbers", "floats([w1_shifted(F(8)), w1_shifted(F(80))])",
         '''decimals=6,
           mistakes={"W₁ est dans l'unité de la variable : c'est le décalage lui-même, pas rapporté à la largeur":
                         floats([w1_shifted(F(8)) / WIDTH_6, w1_shifted(F(80)) / WIDTH_6])}'''),
    ]),

    Paper("M27.7", "Trois dépôts et trois magasins : plans, coûts, couplage indépendant, coin nord-ouest, W₁", [
        ("a", BOOL, "is_plan(GAMMA3_7, A_7, B_7)",
         '''mistakes={"un plan doit vider chaque dépôt et remplir chaque magasin : vérifie les sommes des lignes et des "
                     "colonnes": True}'''),
        ("b", "a number", "floats(cost(GAMMA2_7, D_7))",
         '''decimals=6,
           mistakes={"γᵢⱼ va du dépôt i (ligne) au magasin j (colonne) : la distance est |xᵢ − yⱼ|":
                         floats(cost(GAMMA2_7, transpose(D_7))),
                     "chaque masse est multipliée par la distance de son trajet": floats(sum(map(sum, GAMMA2_7)))}'''),
        ("c", "a number", "floats(cost(INDEPENDENT_7, D_7))",
         '''decimals=6,
           mistakes={"un couplage doit avoir les marges a et b : vérifie les sommes des lignes de ton plan":
                         floats(cost([[a * b for b in B_7] for a in A_7], D_7))}'''),
        ("d", "a 3 × 3 matrix", "floats(northwest(A_7, B_7))",
         '''decimals=6,
           mistakes={"les lignes sont les dépôts (marges 20, 50, 30), les colonnes les magasins (40, 35, 25)":
                         floats(northwest(B_7, A_7))}'''),
        ("e", "a number (2 decimals)", "floats(area_between(X_7, A_7, Y_7, B_7))",
         '''decimals=2,
           mistakes={"W₁ est une distance entre deux lois de probabilité (des masses de somme 1), et elle s'exprime en km":
                         floats(area_between(X_7, A_7, Y_7, B_7) * sum(A_7)),
                     "W₁ est le coût minimal, pas celui du couplage indépendant":
                         floats(cost(INDEPENDENT_7, D_7) / sum(A_7))}'''),
    ]),

    Paper("M27.8", "W₁ et W₂ de deux lois uniformes, puis W₂ de deux gaussiennes", [
        ("a", FRACTION, "str(abs_linear_integral(*QUANTILE_GAP_8))",
         '''kind="fraction", simplified=True,
           mistakes={"l'écart des moyennes ne fait que minorer W₁ : l'aire se prend en valeur absolue":
                         str(abs(sum(QUANTILE_GAP_8[:1]) / 2 + QUANTILE_GAP_8[1]))}'''),
        ("b", "a number (4 decimals)", "math.sqrt(square_linear_integral(*QUANTILE_GAP_8))",
         '''decimals=4,
           mistakes={"W₂ se calcule par les fonctions quantiles : ∫₀¹ (F⁻¹ − G⁻¹)² du, pas par l'aire du carré de F − G":
                         math.sqrt(integrate.quad(lambda x: (cdf_uniform(x, 0, 4) - cdf_uniform(x, 1, 2)) ** 2, -1, 5,
                                                  points=[0, 1, 4 / 3, 2, 4])[0])}'''),
        ("c", "a number (4 decimals)", "math.hypot(BAG_AFTER_8[0] - BAG_BEFORE_8[0], BAG_AFTER_8[1] - BAG_BEFORE_8[1])",
         '''decimals=4,
           mistakes={"des écarts-types, pas des variances : (σ₁ − σ₂)²":
                         math.hypot(BAG_AFTER_8[0] - BAG_BEFORE_8[0], BAG_AFTER_8[1] ** 2 - BAG_BEFORE_8[1] ** 2),
                     "la distance est W₂, la racine de la somme des deux carrés":
                         (BAG_AFTER_8[0] - BAG_BEFORE_8[0]) ** 2 + (BAG_AFTER_8[1] - BAG_BEFORE_8[1]) ** 2,
                     "W₂ est la racine d'une somme de carrés, pas |Δμ| + |Δσ|":
                         abs(BAG_AFTER_8[0] - BAG_BEFORE_8[0]) + abs(BAG_AFTER_8[1] - BAG_BEFORE_8[1])}'''),
        ("d", "a number (4 decimals)", "abs(LINE2_AFTER_8[0] - BAG_BEFORE_8[0])",
         '''decimals=4,
           mistakes={"les deux lois ont le même écart-type : il n'entre pas dans la distance d'une translation":
                         math.hypot(LINE2_AFTER_8[0] - BAG_BEFORE_8[0], LINE2_AFTER_8[1])}'''),
    ]),

    Paper("M27.9", "La distance de Fréchet de deux gaussiennes du plan aux vecteurs propres communs", [
        ("a", "a list of 2 lists of 2 numbers", "floats([eigen_desc(S1_9), eigen_desc(S2_9)])",
         '''decimals=6,
           mistakes={"les valeurs propres annulent det(Σ − λI) = λ² − (tr Σ)λ + det Σ ; ce ne sont pas les coefficients "
                     "de la diagonale": floats([sorted([S1_9[0][0], S1_9[1][1]], reverse=True),
                                               sorted([S2_9[0][0], S2_9[1][1]], reverse=True)]),
                     "les valeurs propres de Σ sont des variances : ne prends pas leurs racines":
                         [[math.sqrt(x) for x in eigen_desc(S)] for S in (S1_9, S2_9)]}'''),
        ("b", "a number", "ROOTS_9",
         '''decimals=6,
           mistakes={"Σ₁Σ₂ a pour valeurs propres les produits des valeurs propres de Σ₁ et de Σ₂ associées au même "
                     "vecteur propre": sum(math.sqrt(a * b) for a, b in zip(eigen_desc(S1_9), eigen_desc(S2_9)[::-1])),
                     "la somme des racines, pas la racine de la somme":
                         math.sqrt(sum(np.linalg.eigvals(np.array(S1_9) @ np.array(S2_9)).real))}'''),
        ("c", "a number", "TRACE1_9 + TRACE2_9 - 2 * ROOTS_9",
         '''decimals=6,
           mistakes={"n'oublie pas le terme croisé de la formule": TRACE1_9 + TRACE2_9,
                     "dans le cas commutatif, ce sont les écarts-types qui se soustraient, pas les variances":
                         sum((a - b) ** 2 for a, b in COMMON_9)}'''),
        ("d", "a number", "float(sum(x ** 2 for x in MU2_9))",
         '''decimals=6,
           mistakes={"la part des moyennes est ‖Δμ‖², la somme des carrés des coordonnées de Δμ":
                         float(sum(abs(x) for x in MU2_9)),
                     "la part des moyennes dans W₂² est un carré, ‖Δμ‖²": math.sqrt(sum(x ** 2 for x in MU2_9))}'''),
        ("e", "a number (2 decimals)", "math.sqrt(sum(x ** 2 for x in MU2_9) + TRACE1_9 + TRACE2_9 - 2 * ROOTS_9)",
         '''decimals=2,
           mistakes={"la distance de Fréchet est W₂ (fiche §9) ; la formule en donne le carré":
                         sum(x ** 2 for x in MU2_9) + TRACE1_9 + TRACE2_9 - 2 * ROOTS_9,
                     "W₂² = ‖Δμ‖² + tr Σ₁ + tr Σ₂ − 2 Σ √λᵢ : n'oublie pas le terme croisé":
                         math.sqrt(sum(x ** 2 for x in MU2_9) + TRACE1_9 + TRACE2_9)}'''),
    ]),

    Paper("M27.10", "Une dérive : PSI, JS et leur approximation, puis KS et W₁ entre deux petits échantillons", [
        ("a", "a number (4 decimals)", "sum((p - q) * math.log(p / q) for p, q in zip(P_10, Q_10))",
         '''decimals=4,
           mistakes={"le PSI pondère ln(p_k/q_k) par la différence p_k − q_k, pas par p_k":
                         sum(p * math.log(p / q) for p, q in zip(P_10, Q_10)),
                     "le logarithme est népérien": sum((p - q) * math.log10(p / q) for p, q in zip(P_10, Q_10))}'''),
        ("b", "a number (5 decimals)", "js(P_10, Q_10)",
         '''decimals=5,
           mistakes={"le logarithme est népérien (nats)": js(P_10, Q_10, log=math.log2),
                     "JS = ½ KL(p ‖ m) + ½ KL(q ‖ m) : n'oublie pas les facteurs ½": 2 * js(P_10, Q_10)}'''),
        ("c", "a number (4 decimals)", "sum((p - q) ** 2 / q for p, q in zip(P_10, Q_10))",
         '''decimals=4,
           mistakes={"on divise par q_k, la proportion de la référence": sum((p - q) ** 2 / p for p, q in zip(P_10, Q_10)),
                     "les écarts p_k − q_k sont élevés au carré": sum(abs(p - q) / q for p, q in zip(P_10, Q_10))}'''),
        ("d", "a number (2 decimals)", "ks_samples(JAN_10, FEB_10)",
         '''decimals=2,
           mistakes={"KS est le plus grand écart vertical entre les deux fonctions de répartition, pas entre des valeurs":
                         max(abs(a - b) for a, b in zip(sorted(JAN_10), sorted(FEB_10)))}'''),
        ("e", "a number (2 decimals)", "w1_samples(JAN_10, FEB_10)",
         '''decimals=2,
           mistakes={"W₁ apparie les valeurs triées : la plus petite avec la plus petite":
                         sum(abs(a - b) for a, b in zip(JAN_10, FEB_10)) / len(JAN_10),
                     "l'écart des moyennes ne fait que minorer W₁": abs(sum(FEB_10) - sum(JAN_10)) / len(JAN_10)}'''),
    ]),

    Paper("M27.16", "Pont : la distance de Fréchet en dimension 1, avec des écarts-types ou des covariances", [
        ("a", "a number (exact value)", "floats(W2SQ_16)",
         '''decimals=6,
           mistakes={"des écarts-types, pas des variances : (σ₁ − σ₂)²":
                         floats((M1_16 - M2_16) ** 2 + (S1_16 ** 2 - S2_16 ** 2) ** 2),
                     "la question demande le carré W₂²": math.sqrt(W2SQ_16)}'''),
        ("b", "a number (4 decimals)", "math.sqrt(W2SQ_16)",
         '''decimals=4,
           mistakes={"W₂ est la racine d'une somme de carrés, pas |Δμ| + |Δσ|": floats(abs(M1_16 - M2_16) + abs(S1_16 - S2_16)),
                     "des écarts-types, pas des variances":
                         math.sqrt((M1_16 - M2_16) ** 2 + (S1_16 ** 2 - S2_16 ** 2) ** 2)}'''),
        ("c", "a number (1 decimal)", "floats(100 * (M1_16 - M2_16) ** 2 / W2SQ_16)",
         '''decimals=1,
           mistakes={"la part se rapporte à W₂², une somme de deux carrés, pas à W₂":
                         100 * float(abs(M1_16 - M2_16)) / math.sqrt(W2SQ_16),
                     "la question demande la part de la moyenne, pas celle de l'écart-type":
                         floats(100 * (S1_16 - S2_16) ** 2 / W2SQ_16)}'''),
        ("d", "a number (exact value)", "covariance_term(S1_16 ** 2, S2_16 ** 2)",
         '''decimals=6,
           mistakes={"une matrice de covariance contient des variances : Σ = [[σ²]]": covariance_term(S1_16, S2_16),
                     "n'oublie pas le terme croisé −2(Σ₁Σ₂)^{1/2}": floats(S1_16 ** 2 + S2_16 ** 2)}'''),
        ("e", "a number (4 decimals)", "floats((M1_16 - M2_16) ** 2) + covariance_term(S1_16, S2_16)",
         '''decimals=4,
           mistakes={"la fonction ajoute aussi ‖Δμ‖² au terme des covariances": covariance_term(S1_16, S2_16),
                     "la fonction rend un carré, sans racine":
                         math.sqrt(floats((M1_16 - M2_16) ** 2) + covariance_term(S1_16, S2_16))}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (exact fractions where the calculation is exact)
import math
from fractions import Fraction as F

import numpy as np
from scipy import integrate


def exact(values):
    """Decimal numbers written in the statement (0.35), as exact fractions (7/20), in a vector or a matrix."""
    if isinstance(values, (list, tuple)):
        return [exact(v) for v in values]
    return F(str(values))


def floats(values):
    """A number, a vector or a matrix of exact values (fractions) as a float or nested lists of floats."""
    return np.asarray(values, dtype=float).tolist()


def transpose(A):
    return [list(row) for row in zip(*A)]


def columns(G):
    """The columns of a matrix, as rows."""
    return transpose(G)


def row_minima(G):
    return [min(row) for row in G]


def column_maxima(G):
    return [max(column) for column in zip(*G)]


def saddles(G, flipped=False):
    """The saddle points [row, column] numbered from 1, in the order of the rows then of the columns: the smallest of its
    row and the largest of its column (flipped: the largest of its row and the smallest of its column)."""
    out = []
    for i, row in enumerate(G):
        for j, g in enumerate(row):
            column = [r[j] for r in G]
            if (g == max(row) and g == min(column)) if flipped else (g == min(row) and g == max(column)):
                out.append([i + 1, j + 1])
    return out


def dominated_column(G, j):
    """True when the column j costs strictly more than another column on every row of G."""
    return any(all(row[l] < row[j] for row in G) for l in range(len(G[0])) if l != j)


def reduce_dominated(G, strict=True, rounds=None):
    """Successive dominances: a round strikes out the dominated rows, then the dominated columns, one at a time; the
    rounds go on until nothing changes (rounds: at most that many). strict=False also strikes out a strategy that equals
    another one."""
    rows, cols = list(range(len(G))), list(range(len(G[0])))
    below = (lambda u, v: u < v) if strict else (lambda u, v: u <= v)
    done = 0
    while rounds is None or done < rounds:
        before = (list(rows), list(cols))
        for i in list(rows):                  # a row that wins less than another row on every column left
            if any(k != i and all(below(G[i][j], G[k][j]) for j in cols) for k in rows):
                rows.remove(i)
        for j in list(cols):                  # a column that costs more than another column on every row left
            if any(l != j and all(below(G[i][l], G[i][j]) for i in rows) for l in cols):
                cols.remove(j)
        done += 1
        if (rows, cols) == before:
            break
    return [[G[i][j] for j in cols] for i in rows]


def indifferent(first, second):
    """The probability x of the first move such that x first[0] + (1 − x) first[1] = x second[0] + (1 − x) second[1]: the
    two lines (two moves of the other player) give the same expected payoff."""
    return F(second[1] - first[1], (first[0] - first[1]) - (second[0] - second[1]))


def expected(G, p, q):
    """The expected payoff p q a + p (1 − q) b + (1 − p) q c + (1 − p)(1 − q) d of a 2 × 2 game."""
    return sum(pi * qj * G[i][j] for i, pi in enumerate((p, 1 - p)) for j, qj in enumerate((q, 1 - q)))


G_1 = [[5, 2, 6, 1], [4, 3, 7, 3], [0, 1, 4, 0]]                      # M27.1: rows A1, A2, A3; columns B1 to B4
G_2 = [[55, 95], [85, 60]]                                             # M27.2: rows shot left, right; keeper left, right
P_2 = indifferent(*columns(G_2))                                       # the keeper's two dives cost the same
Q_2 = indifferent(G_2[0], G_2[1])                                      # the shooter's two shots bring the same
V_2 = expected(G_2, P_2, Q_2)
Q_D_2, P_E_2 = F(65, 100), F(55, 100)
ROWS_3 = [[7, 1], [10, 2]]                                             # M27.3: the dilemma (M, B), the row bakery
COLS_3 = transpose(ROWS_3)                                             # the column bakery, the same game seen from it


def pure_nash(A, B):
    """The pure Nash equilibria (i, j): A[i][j] is a best row against j, and B[i][j] a best column against i."""
    return [(i, j) for i in range(len(A)) for j in range(len(A[0]))
            if A[i][j] == max(A[k][j] for k in range(len(A))) and B[i][j] == max(B[i])]


TEAM_ROWS_3 = [[5, 0], [0, 3]]                                         # the coordination (X, Y): the row team
TEAM_COLS_3 = [[3, 0], [0, 4]]                                         # the column team
X_3 = indifferent(*columns(TEAM_COLS_3))                               # x makes the column team indifferent
Y_3 = indifferent(TEAM_ROWS_3[0], TEAM_ROWS_3[1])                      # y makes the row team indifferent
GAINS_3 = [sum(pi * qj * T[i][j] for i, pi in enumerate((X_3, 1 - X_3)) for j, qj in enumerate((Y_3, 1 - Y_3)))
           for T in (TEAM_ROWS_3, TEAM_COLS_3)]


def winning(n, moves, last_loses):
    """True when the player who must play with n matches left wins (backward induction)."""
    table = {0: last_loses}               # 0 left: the previous player took the last one
    for k in range(1, n + 1):
        table[k] = any(not table[k - m] for m in moves if m <= k and not (last_loses and m == k))
    return table[n]


def losing(n_max, moves, last_loses):
    return [n for n in range(1, n_max + 1) if not winning(n, moves, last_loses)]


def winning_move(n, moves, last_loses):
    """The number of matches to take from n to leave a losing position (the smallest such move)."""
    return next(m for m in moves if m < n and not winning(n - m, moves, last_loses))


ETA_4 = 0.6                                                            # M27.4


def step_matrix(a, b, alternating=False):
    """The matrix of one step on xy, steps a for x and b for y: simultaneous [[1, −a], [b, 1]], alternating
    [[1, −a], [b, 1 − ab]]."""
    return np.array([[1.0, -a], [b, 1.0 - a * b if alternating else 1.0]])


def radius(M):
    """The largest modulus of an eigenvalue."""
    return float(max(abs(np.linalg.eigvals(M))))


PI1_5 = F(32, 100)                                                     # M27.5: B (Y = 1) delivers 32 %
P0_5, P1_5 = exact([0.45, 0.30, 0.20, 0.05]), exact([0.05, 0.20, 0.30, 0.45])   # levels 0 to 3 at A, at B
OVER_5 = exact([0.02, 0.08, 0.15, 0.96])                               # the overconfident predictor
JOINT0_5 = [(1 - PI1_5) * p for p in P0_5]                             # P(X = x, Y = 0)
JOINT1_5 = [PI1_5 * p for p in P1_5]                                   # P(X = x, Y = 1)
PX_5 = [a + b for a, b in zip(JOINT0_5, JOINT1_5)]
POST_5 = [b / x for b, x in zip(JOINT1_5, PX_5)]


def risk_5(t, log=math.log, swapped=False):
    """The expected log-loss −Σ_x [P(x, 1) ln t(x) + P(x, 0) ln(1 − t(x))] (swapped: the two weights exchanged)."""
    w1, w0 = (JOINT0_5, JOINT1_5) if swapped else (JOINT1_5, JOINT0_5)
    return -sum(float(a) * log(float(tx)) + float(b) * log(float(1 - tx)) for a, b, tx in zip(w1, w0, t))


def entropy_5(t):
    """The log-loss of the prediction t when the label is 1 with the probability t (nats)."""
    t = float(t)
    return -t * math.log(t) - (1 - t) * math.log(1 - t)


WIDTH_6 = F(5)                                                         # M27.6: U[0, 5] and U[θ, θ + 5] (minutes)


def js_shifted(theta, log=math.log, half=True, capped=True):
    """JS(U[0, w], U[θ, θ + w]) from its definition, piece by piece: where only one law lives (a length min(θ, w)), its
    density is 1/w and m = 1/(2w); where both live, p = q = m. capped=False: the length θ, even beyond w."""
    alone = min(theta, WIDTH_6) if capped else theta
    kl = float(alone / WIDTH_6) * log(2)          # KL(p ‖ m) = ∫ p ln(p/m) on the piece where p lives alone
    return (kl + kl) / 2 if half else kl + kl


def w1_shifted(theta):
    """W₁ of a translation: ∫₀¹ |F⁻¹(u) − G⁻¹(u)| du, with G⁻¹ = F⁻¹ + θ."""
    return abs(theta)


X_7, A_7 = [1, 4, 6], [20, 50, 30]                                     # M27.7: depots (km), stocks (t)
Y_7, B_7 = [2, 3, 8], [40, 35, 25]                                     # stores (km), orders (t)
D_7 = [[abs(x - y) for y in Y_7] for x in X_7]
GAMMA2_7 = [[10, 10, 0], [30, 20, 0], [0, 5, 25]]
GAMMA3_7 = [[0, 20, 0], [40, 10, 0], [0, 0, 30]]


def is_plan(P, a, b):
    return [sum(row) for row in P] == list(a) and [sum(col) for col in zip(*P)] == list(b)


def cost(P, D):
    return sum(P[i][j] * D[i][j] for i in range(len(P)) for j in range(len(P[0])))


INDEPENDENT_7 = [[F(a * b, sum(A_7)) for b in B_7] for a in A_7]


def northwest(a, b):
    """The north-west corner rule: from the top left cell, the largest mass possible, then down if the row is empty,
    right if the column is full."""
    a, b = [F(x) for x in a], [F(x) for x in b]
    P = [[F(0)] * len(b) for _ in a]
    i = j = 0
    while i < len(a) and j < len(b):
        t = min(a[i], b[j])
        P[i][j], a[i], b[j] = t, a[i] - t, b[j] - t
        if a[i] == 0:
            i += 1
        else:
            j += 1
    return P


def area_between(x, a, y, b):
    """∫ |F − G| for two discrete laws (points x, y; masses a, b, each brought to a total of 1), exactly."""
    a, b = [F(m, sum(a)) for m in a], [F(m, sum(b)) for m in b]
    knots = sorted(set(x) | set(y))
    total = F(0)
    for left, right in zip(knots, knots[1:]):
        Fx = sum(m for p, m in zip(x, a) if p <= left)
        Gx = sum(m for p, m in zip(y, b) if p <= left)
        total += abs(Fx - Gx) * (right - left)
    return total


QUANTILE_GAP_8 = (F(3), F(-1))          # M27.8: F⁻¹(u) = 4u for U[0, 4], G⁻¹(u) = 1 + u for U[1, 2]: a gap 3u − 1


def abs_linear_integral(alpha, beta):
    """∫₀¹ |αu + β| du, exactly (α ≠ 0)."""
    root = -beta / alpha
    primitive = lambda u: alpha * u * u / 2 + beta * u          # noqa: E731
    if not 0 < root < 1:
        return abs(primitive(F(1)) - primitive(F(0)))
    return abs(primitive(root) - primitive(F(0))) + abs(primitive(F(1)) - primitive(root))


def square_linear_integral(alpha, beta):
    """∫₀¹ (αu + β)² du = α²/3 + αβ + β², exactly."""
    return alpha * alpha / 3 + alpha * beta + beta * beta


def cdf_uniform(x, lo, hi):
    return min(max((x - lo) / (hi - lo), 0.0), 1.0)


BAG_BEFORE_8, BAG_AFTER_8, LINE2_AFTER_8 = (20.0, 1.5), (21.2, 1.0), (21.2, 1.5)   # (mean, sd) in g
S1_9, S2_9 = [[52, 36], [36, 73]], [[145, 60], [60, 180]]             # M27.9 (hundredths of mm)
MU2_9 = [5, -2]                                                        # μ₁ = (0, 0)


def eigen_desc(S):
    """The two eigenvalues of a symmetric 2 × 2 matrix, from the largest: (tr ± √(tr² − 4 det))/2."""
    tr, det = S[0][0] + S[1][1], S[0][0] * S[1][1] - S[0][1] * S[1][0]
    root = math.sqrt(tr * tr - 4 * det)
    return [(tr + root) / 2, (tr - root) / 2]


TRACE1_9, TRACE2_9 = S1_9[0][0] + S1_9[1][1], S2_9[0][0] + S2_9[1][1]
ROOTS_9 = float(sum(np.sqrt(np.linalg.eigvals(np.array(S1_9, dtype=float) @ np.array(S2_9, dtype=float)).real)))
_, U_9 = np.linalg.eigh(np.array(S1_9, dtype=float))                  # the common eigenvectors, as columns
COMMON_9 = [(float(u @ np.array(S1_9) @ u), float(u @ np.array(S2_9) @ u)) for u in U_9.T]   # (variance 1, variance 2)
Q_10, P_10 = [0.62, 0.26, 0.12], [0.55, 0.29, 0.16]                   # M27.10: March (reference), April
JAN_10, FEB_10 = [0.7, -1.5, 3.6, -0.2, 3.2], [2.3, 4.1, 1.2, 2.8, 1.9]   # temperatures (°C)


def kl(p, q, log=math.log):
    return sum(a * log(a / b) for a, b in zip(p, q) if a > 0)


def js(p, q, log=math.log):
    m = [(a + b) / 2 for a, b in zip(p, q)]
    return (kl(p, m, log) + kl(q, m, log)) / 2


def ks_samples(x, y):
    """sup |F − G| for the empirical distribution functions: the largest gap, at the points of the two samples."""
    ecdf = lambda s, t: sum(v <= t for v in s) / len(s)          # noqa: E731
    return max(abs(ecdf(x, t) - ecdf(y, t)) for t in list(x) + list(y))


def w1_samples(x, y):
    """W₁ of two samples of the same size: the mean gap of the sorted values."""
    return sum(abs(a - b) for a, b in zip(sorted(x), sorted(y))) / len(x)


M1_16, S1_16 = F("50.30"), F("0.12")                                   # M27.16: before (mm)
M2_16, S2_16 = F("50.02"), F("0.05")                                   # after
W2SQ_16 = (M1_16 - M2_16) ** 2 + (S1_16 - S2_16) ** 2


def covariance_term(c1, c2):
    """tr(Σ₁ + Σ₂ − 2 (Σ₁Σ₂)^{1/2}) for two 1 × 1 matrices [[c1]] and [[c2]]."""
    return float(c1 + c2) - 2 * math.sqrt(float(c1 * c2))'''

PAPER_FRACTIONS = sorted(f"{paper.id}{letter}" for paper in PAPER for letter, hint, _, _ in paper.subs if hint == FRACTION)

PAPER_LEARNER_CONTEXT = ('''# Part 0: a fraction asked as a text "p/q" must be a text (a float such as 5/13 is only close to it)
FRACTIONS_0 = ''' + repr(PAPER_FRACTIONS) + '''


def check_paper_0(ex_id, answer):
    """wbm.check(ex_id, answer); for a fraction asked as a text "p/q", a number is refused (❌)."""
    if ex_id in FRACTIONS_0 and answer is not ... and answer is not None and not isinstance(answer, str):
        print(f"❌ Ex {ex_id} : la question demande une fraction irréductible entre guillemets, comme \\"3/7\\" ; reçu "
              f"{answer!r} ({type(answer).__name__}) : écris la fraction exacte, en texte.")
        return None
    return wbm.check(ex_id, answer)''')


def paper_part(kind: str) -> list:
    """The cells of Part 0: in the exercise notebook, the answers are checked by check_paper_0 (PAPER_LEARNER_CONTEXT)."""
    cells = paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO,
                        learner_context=PAPER_LEARNER_CONTEXT if kind == "exercise" else None)
    if kind == "exercise":
        for cell in cells:
            if cell.cell_type == "code" and "    wbm.check(f\"M27." in cell.source:
                cell.source = cell.source.replace("    wbm.check(f\"M27.", "    check_paper_0(f\"M27.")
    return cells


PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M27.1 à M27.10 ; 🔗 M27.16)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question "
               "(« exact value » ou « a number » sans décimales : tous les chiffres, ces calculs tombent juste) ;\n"
               "- une liste `[0.2, -1]` ; une matrice comme la liste de ses **lignes**, `[[1, 0], [-2, 3]]` ;\n"
               "- une fraction irréductible entre guillemets, `\"3/7\"`, quand la question le dit ;\n"
               "- `True` ou `False` pour un vrai ou faux.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M27.19 to M27.22), and SciPy (M27.23)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to D)
import math
import numbers
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate, optimize, stats

from wbm.errors import MymathMissingError
from wbm.nbtools import StopCheck, checked, drawn, filled, fr, own_code, pair, run_pytest_group, same, verdict

TEST_M27 = "tests/test_m27_distances.py"            # the tests of mymath/distances.py
REF = wbm.load_mymath("ref", alias="mymath_ref")   # the reference: the data cells and the checks never use your code
ref_distances = REF.distances
REF_DISTANCES = {f"ref_distances.{name}": getattr(ref_distances, name)    # a check stops if your code calls one of them
                 for name in ("pure_strategy_values", "mixed_strategy_value_2x2", "descent_ascent_iterates",
                              "w2_gaussians_1d")}


def shown(value, digits=4):
    """A short text for a result of the learner's code (the check messages): numbers rounded, as lists."""
    if value is None:
        return "None"
    try:
        if isinstance(value, tuple):
            return "(" + ", ".join(str(np.round(np.asarray(v, dtype=float), digits).tolist()) for v in value) + ")"
        return str(np.round(np.asarray(value, dtype=float), digits).tolist())
    except (TypeError, ValueError):
        return repr(value)[:120]


def check_answer(ex_id, value, hint=None):
    """wbm.check(ex_id, value, computed=True). For a list that holds True or False, the message gives only how many
    elements are right, not the place of the first wrong one (it would let you guess the booleans one by one).
    hint(value), when given, may return a targeted « Piste » for a wrong answer (None otherwise)."""
    holds_bool = isinstance(value, (list, tuple)) and any(isinstance(v, (bool, np.bool_)) for v in value)
    if not holds_bool and hint is None:
        return wbm.check(ex_id, value, computed=True)
    result = wbm.check(ex_id, value, computed=True, quiet=True)
    message = result.message
    if holds_bool:
        for cut in (" Le premier faux est le ", " Premier élément faux à l'indice "):
            message = message.split(cut)[0]
    if hint is not None and result.status not in ("correct", "pending", "unknown"):
        try:
            extra = hint(value)
        except Exception:  # noqa: BLE001 - an odd answer: no targeted hint
            extra = None
        if extra:
            message = f"{message} Piste : {extra}"
    icon = {"correct": "✅", "pending": "⏳", "unknown": "❓"}.get(result.status, "❌")
    print(f"{icon} Ex {ex_id} : {message}")
    return result


def check_rounding(ex_id, label, value, limit, wrong=()):
    """A number that must be a rounding error (0 <= value < limit): ✅, ⏳ or ❌. wrong: pairs (text, number), a classic
    wrong number (to 1e-6 relative) that gets its own text."""
    if not filled(value):
        print(f"⏳ Ex {ex_id} : {label} : pas encore fait.")
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        print(f"❌ Ex {ex_id} : {label} : attendu un nombre, reçu {value!r}.")
        return False
    if 0 <= number < limit:
        print(f"✅ Ex {ex_id} : {label} : {number:.1e}, une erreur d'arrondi.")
        return True
    for text, target in wrong:
        if math.isclose(number, target, rel_tol=1e-6):
            print(f"❌ Ex {ex_id} : {label} : {text}.")
            return False
    print(f"❌ Ex {ex_id} : {label} : attendu un écart de l'ordre des arrondis (positif, moins de {limit:.0e}), reçu "
          f"{number!r}.")
    return False


def reporter(results, stop=True):
    """A function report(ok, success, failure) that prints one ✅ or ❌ line, keeps the verdict in results, and (stop)
    ends the check at the first ❌ (StopCheck, caught by checked)."""
    def report(ok, success, failure):
        results.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))
        if not ok and stop:
            raise StopCheck
    return report


def matches(got, want, rtol=1e-9, atol=1e-12):
    """True when got is an array of numbers of the shape of want and equal to it up to rounding (no error for an odd
    got): to recognize a classic wrong result before the comparison."""
    try:
        arr = np.asarray(got, dtype=float)
    except (TypeError, ValueError):
        return False
    want = np.asarray(want, dtype=float)
    return arr.shape == want.shape and bool(np.allclose(arr, want, rtol=rtol, atol=atol))


def as_floats(value):
    """value as a float array, or None when it is not an array of numbers."""
    try:
        return np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        return None


def line_points(line):
    """The (x, y) points of a line of matplotlib, as two float arrays."""
    return np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)


def through(ax, xs, ys, rtol=1e-7, atol=1e-12):
    """True when one line of ax passes by all the points (xs, ys), in this order."""
    xs, ys = np.asarray(xs, dtype=float), np.asarray(ys, dtype=float)
    for line in ax.lines:
        x, y = line_points(line)
        if (x.shape == xs.shape and y.shape == ys.shape and np.allclose(x, xs, rtol=rtol, atol=atol)
                and np.allclose(y, ys, rtol=rtol, atol=atol)):
            return True
    return False


def drawn_points(ax, marker_only=False):
    """All the points drawn in ax: those of its lines (marker_only: lines with a marker only) and of its scatters."""
    points = []
    for line in ax.lines:
        if marker_only and line.get_marker() in (None, "", " ", "None", "none"):
            continue
        x, y = line_points(line)
        points += list(zip(x.ravel(), y.ravel()))
    for collection in ax.collections:
        offsets = np.asarray(collection.get_offsets(), dtype=float)
        if offsets.ndim == 2 and offsets.shape[1] == 2 and type(collection).__name__ == "PathCollection":
            points += [tuple(p) for p in offsets]
    return points


def points_at(ax, xs, ys, rtol=1e-7, atol=1e-12, marker_only=False):
    """True when every point (xs[k], ys[k]) is drawn in ax (a line with or without markers, or a scatter)."""
    points = np.array(drawn_points(ax, marker_only) or [(np.nan, np.nan)], dtype=float)
    return all(np.any(np.isclose(points[:, 0], x, rtol=rtol, atol=atol) & np.isclose(points[:, 1], y, rtol=rtol, atol=atol))
               for x, y in zip(np.atleast_1d(xs), np.atleast_1d(ys)))


def follows(ax, f, lo, hi, rtol=1e-6):
    """True when one line of ax has at least two points with y = f(x), its x covering [lo, hi]."""
    for line in ax.lines:
        x, y = line_points(line)
        if (x.size >= 2 and np.all(np.isfinite(x)) and x.min() <= lo * (1 + 1e-9) and x.max() >= hi * (1 - 1e-9)
                and np.allclose(y, f(x), rtol=rtol, atol=0)):
            return True
    return False'''

DATA = '''# The data of the paper exercises (02_exercices.md), the strategies numbered from 0 as in mymath
G_MARKET = np.array([[5.0, 2, 6, 1], [4, 3, 7, 3], [0, 1, 4, 0]])     # M27.1: rows A1, A2, A3; columns B1 to B4
G_PENALTY = np.array([[55.0, 95], [85, 60]])                           # M27.2: shot left, right; keeper left, right (%)
DEPOTS_KM, DEPOTS_T = np.array([1.0, 4, 6]), np.array([20.0, 50, 30])  # M27.7: the depots (km) and their stocks (t)
STORES_KM, STORES_T = np.array([2.0, 3, 8]), np.array([40.0, 35, 25])  # the stores (km) and their orders (t)
BAGS_BEFORE, BAGS_AFTER = (20.0, 1.5), (21.2, 1.0)                     # M27.8: (mean, standard deviation) in g
SHAFTS_BEFORE, SHAFTS_AFTER = (50.30, 0.12), (50.02, 0.05)             # M27.16: (mean, standard deviation) in mm'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M27")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M26). Ouvre ta copie `mon_travail/mymath/distances.py`, lis la docstring "
         "du module (ses conventions, et ce qui est permis) puis celle de la fonction, remplace chaque "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Dans le notebook, appelle tes fonctions par "
         "`mymath.distances.<nom>` (par exemple `mymath.distances.pure_strategy_values(G)`), ou donne-leur un nom "
         "court (`pure_strategy_values = mymath.distances.pure_strategy_values`) dans une cellule exécutée après le "
         "rechargement. ⚠️ Le squelette n'importe rien : ajoute en tête du fichier `import numpy as np` (et "
         "`import math`, `import numbers` si tu t'en sers). NumPy et le module `math` sont permis, mais rien de "
         "`np.linalg` et aucune fonction de SciPy (`scipy.optimize` résout un jeu) : les tests comparent tes résultats "
         "à ceux de `scipy.optimize.linprog`, de `np.linalg.matrix_power` et de `scipy.integrate.quad`, et un test lit "
         "ton module. Rends des nombres `float`, des indices `int` et des itérés en tableaux NumPy de flottants, et ne "
         "modifie jamais les tableaux reçus. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy.")

REMINDER = ("> Même mode d'emploi qu'en M27.19 : écris la fonction dans ta copie `mon_travail/mymath/distances.py`, "
            "**enregistre**, puis exécute les cellules ci-dessous ; la première recharge ta librairie.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of distances.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group(TEST_M27, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_M27, "{keyword}", impl="ref")')]


def answers_check(ex_id: str, letters: str, hints: dict | None = None) -> str:
    """The check cell of the answers a), b)... of a notebook exercise: one check_answer each (TOOLS: wbm.check with
    computed=True, without the place of the first wrong element in a list that holds booleans). ``hints`` maps a
    letter to the code of a function value -> targeted hint (or None), written in the cell."""
    names = ", ".join(f"answer_{ex_id.replace('.', '_')}{letter}" for letter in letters)
    if not hints:
        return (f'for letter, answer in zip("{letters}", [{names}]):\n'
                f'    check_answer(f"{ex_id}{{letter}}", answer)')
    tag = ex_id.replace(".", "_")
    return "\n".join(f'check_answer("{ex_id}{letter}", answer_{tag}{letter}'
                     + (f", hint={hints[letter]})" if letter in hints else ")") for letter in letters)


NOTE_19 = (r"`G = np.array(G, dtype=float)`, les contrôles, `G.min(axis=1)`, `G.max(axis=0)`, `np.argmax`, `np.argmin`. a) "
           r"`(3.0, 3.0, 1, 1)` : A2 contre B2, le premier des deux points selles. b) `(-3.0, -3.0, 1, 1)` : "
           r"$\max_j\min_i(-g_{ij}) = -\min_j\max_i g_{ij}$. c) `(60.0, 85.0, 1, 0)` ; faux ($60 < 85$).")

M27_19 = Ex(
    "M27.19", "🔨", 1, 15, "Les valeurs d'un jeu en stratégies pures : maximin, minimax et coups prudents, points selles "
    "compris · `pure_strategy_values`",
    "programmer le maximin, le minimax et les coups qui les donnent, puis voir qu'ils forment un point selle quand il en "
    "existe un, et seulement alors.", "fiche §1 ; Ex M27.1 et M27.2", tracks="C, E", mymath="distances.py", note=NOTE_19,
    body=HOWTO + r"""

Écris `pure_strategy_values(G)` (fiche §1), en suivant sa docstring : contrôle `G` (un tableau 2-D, non vide, de nombres finis ; sinon une `ValueError`) ; calcule le minimum de chaque ligne (`axis=1`) et le maximum de chaque colonne (`axis=0`), puis le maximin, le minimax, et les plus petits indices `row` et `col` où ils sont atteints (`np.argmax` et `np.argmin` rendent le premier en cas d'égalité) ; rends `(maximin, minimax, row, col)`, deux `float` et deux `int` Python.

**L'usage.** La cellule de données de la partie A donne le marché de M27.1 (`G_MARKET`) et les tirs au but de M27.2 (`G_PENALTY`). Avec ta fonction :
- a) le marché (un tuple de 4, tel que rendu), à comparer à tes réponses a) et b) de M27.1 (les indices partent de 0) ;
- b) le même jeu vu par l'enseigne B, `-G_MARKET.T` : ses lignes sont les stratégies de B, qui maximise ce que A perd (un tuple de 4, tel que rendu) ; dans ta copie, dis pourquoi le maximin de `-G.T` est l'opposé du minimax de `G` ;
- c) les tirs au but, et vrai ou faux : `(row, col)` y est un point selle (une liste de 5 : les 4 valeurs rendues, puis le booléen).

Ce qu'il faut observer : la fonction rend un point selle quand il en existe un ; sans point selle, `row` et `col` ne sont que des coups prudents, que l'adversaire exploite s'il les connaît.""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_pure_strategy_values_ or test_module_uses_") + [
        ("md", "**L'usage** : le marché, le même jeu vu par B, et les tirs au but."),
        ("todo", '''answer_M27_19a = answer_M27_19b = answer_M27_19c = ...
with wbm.attempt("M27.19"):          # if you call pure_strategy_values here: ⏳ while it is not written
    answer_M27_19a = ...  # a) a tuple of 4, as returned: the market G_MARKET
    answer_M27_19b = ...  # b) a tuple of 4, as returned: the same game seen by B, -G_MARKET.T
    answer_M27_19c = ...  # c) a list of 5: the 4 values returned for G_PENALTY, then True or False: (row, col) is a saddle point there'''),
        ("check", answers_check("M27.19", "abc")),
        ("solution", '''pure_strategy_values = mymath.distances.pure_strategy_values
answer_M27_19a = pure_strategy_values(G_MARKET)
answer_M27_19b = pure_strategy_values(-G_MARKET.T)
maximin_19, minimax_19, row_19, col_19 = pure_strategy_values(G_PENALTY)
saddle_19 = bool(G_PENALTY[row_19].min() == G_PENALTY[row_19, col_19] == G_PENALTY[:, col_19].max())
answer_M27_19c = [maximin_19, minimax_19, row_19, col_19, saddle_19]
print("a)", answer_M27_19a, " b)", answer_M27_19b, " c)", answer_M27_19c)'''),
        ("record", '''def pure_19r(G):
    """The oracle: loops over the rows and the columns, the first index of a tie."""
    rows = [min(row) for row in G]
    cols = [max(col) for col in zip(*G)]
    return [float(max(rows)), float(min(cols)), rows.index(max(rows)), cols.index(min(cols))]


market_19r = [[5, 2, 6, 1], [4, 3, 7, 3], [0, 1, 4, 0]]
seen_by_B_19r = [[-g for g in col] for col in zip(*market_19r)]      # -G.T
penalty_19r = [[55, 95], [85, 60]]
wbm.record("M27.19a", pure_19r(market_19r), decimals=6,
           mistakes={"le minimum de chaque ligne se prend le long des colonnes (axis=1), le maximum de chaque colonne le "
                     "long des lignes (axis=0)": pure_19r([list(col) for col in zip(*market_19r)]),
                     "row et col sont les plus petits indices où le maximin et le minimax sont atteints":
                         pure_19r(market_19r)[:3] + [3],
                     "dans le code, les indices partent de 0 : la ligne A1 est la ligne 0":
                         pure_19r(market_19r)[:2] + [i + 1 for i in pure_19r(market_19r)[2:]]})
wbm.record("M27.19b", pure_19r(seen_by_B_19r), decimals=6,
           mistakes={"B maximise ce que A perd : ses gains sont −G, pas G": pure_19r([list(col) for col in zip(*market_19r)]),
                     "les lignes de -G.T sont les stratégies de B (transpose aussi −G) ; si tu as bien passé -G.T, ce sont les "
                     "axes de tes minimums et de tes maximums qui sont échangés": pure_19r([[-g for g in row] for row in market_19r])})
wbm.record("M27.19c", pure_19r(penalty_19r) + [False], decimals=6,
           mistakes={"(row, col) n'est un point selle que si le maximin égale le minimax": pure_19r(penalty_19r) + [True]})'''),
    ],
)

NOTE_20 = (r"La forme, puis `pure_strategy_values` ; si `maximin == minimax`, les stratégies pures ; sinon "
           r"`(a, b), (c, d) = G.tolist()` et les trois formules. a) $\big(\frac{5}{13}, \frac{7}{13}, \frac{955}{13}\big) "
           r"\approx (0{,}3846 ;\ 0{,}5385 ;\ 73{,}4615)$. b) Les formules donneraient $p = -2$ et $q = 4$ ; la fonction "
           r"rend `(1.0, 1.0, 4.0)`, le point selle (0, 0). c) $73{,}4615$ et $73{,}4615$.")

M27_20 = Ex(
    "M27.20", "🔨", 2, 20, "Les stratégies optimales et la valeur d'un jeu 2 × 2, avec ou sans point selle · "
    "`mixed_strategy_value_2x2`",
    "programmer les stratégies optimales d'un jeu 2 × 2, pures s'il y a un point selle, d'indifférence sinon, et voir "
    "que p* et q* garantissent la même valeur.", "fiche §2 ; Ex M27.2 et M27.19", tracks="C, E", mymath="distances.py",
    note=NOTE_20,
    body=REMINDER + r"""

Écris `mixed_strategy_value_2x2(G)` (fiche §2), en suivant sa docstring : contrôle la forme $(2, 2)$, puis appelle ta `pure_strategy_values` ; s'il y a un point selle (`maximin == minimax`, une comparaison exacte), rends les stratégies pures, `p = 1.0` si `row == 0` et `p = 0.0` sinon, de même pour `q` avec `col`, et `value = maximin` ; sinon, rends les trois formules d'indifférence de la fiche, $p^\star = \frac{d - c}{\kappa}$, $q^\star = \frac{d - b}{\kappa}$, $v = \frac{ad - bc}{\kappa}$, en `float` Python.

**L'usage.** Avec ta fonction :
- a) les tirs au but de M27.2 (`G_PENALTY`) (un tuple de 3, tel que rendu), à comparer à tes réponses a) à c) ;
- b) pour $\mathbf{G} = \begin{pmatrix} 4 & 7 \\ 1 & 3 \end{pmatrix}$ : ce que donneraient les formules de $p^\star$ et de $q^\star$, puis ce que rend ta fonction (une liste de 5 nombres : $p$ et $q$ par les formules, puis les trois nombres rendus) ;
- c) pour les tirs au but, le plus petit gain espéré de $p^\star$ contre les deux plongeons, $\min_j(\mathbf{p}^{\star\top}\mathbf{G})_j$, puis le plus grand de $q^\star$ contre les deux tirs, $\max_i(\mathbf{G}\mathbf{q}^\star)_i$, avec $\mathbf{p}^\star = (p^\star, 1 - p^\star)$ et $\mathbf{q}^\star = (q^\star, 1 - q^\star)$ (une liste de 2 nombres).

Ce qu'il faut observer : avec un point selle, les formules d'indifférence sortent de $[0, 1]$ ; sans point selle, $p^\star$ et $q^\star$ garantissent la même valeur, chacun de son côté.""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_mixed_strategy_value_2x2_") + [
        ("md", "**L'usage** : les tirs au but, un jeu à point selle, et les deux garanties."),
        ("todo", '''G_SADDLE_20 = np.array([[4.0, 7.0], [1.0, 3.0]])
answer_M27_20a = answer_M27_20b = answer_M27_20c = ...
with wbm.attempt("M27.20"):          # if you call mixed_strategy_value_2x2 here: ⏳ while it is not written
    answer_M27_20a = ...  # a) a tuple of 3, as returned: (p, q, value) for G_PENALTY
    answer_M27_20b = ...  # b) a list of 5 numbers: p and q by the indifference formulas for G_SADDLE_20, then the 3 numbers your function returns
    answer_M27_20c = ...  # c) a list of 2 numbers, as computed: min_j (p*ᵀ G)_j, then max_i (G q*)_i, for G_PENALTY'''),
        ("check", answers_check("M27.20", "abc")),
        ("solution", '''G_SADDLE_20 = np.array([[4.0, 7.0], [1.0, 3.0]])
mixed_strategy_value_2x2 = mymath.distances.mixed_strategy_value_2x2
answer_M27_20a = mixed_strategy_value_2x2(G_PENALTY)
(a_20, b_20), (c_20, d_20) = G_SADDLE_20.tolist()
kappa_20 = a_20 - b_20 - c_20 + d_20
answer_M27_20b = [(d_20 - c_20) / kappa_20, (d_20 - b_20) / kappa_20, *mixed_strategy_value_2x2(G_SADDLE_20)]
p_20, q_20, v_20 = answer_M27_20a
answer_M27_20c = [float((np.array([p_20, 1 - p_20]) @ G_PENALTY).min()), float((G_PENALTY @ np.array([q_20, 1 - q_20])).max())]
print("a)", answer_M27_20a, " b)", answer_M27_20b, " c)", answer_M27_20c)'''),
        ("record", '''from fractions import Fraction as F_20r


def strategies_20r(G):
    """The oracle: scipy.optimize.linprog on the row player's program, maximize v under (pᵀG)_j >= v, then on the
    column player's; returns (p, q, v)."""
    G = np.asarray(G, dtype=float)
    rows = optimize.linprog([0, 0, -1], A_ub=np.column_stack([-G.T, np.ones(2)]), b_ub=[0, 0], A_eq=[[1, 1, 0]],
                            b_eq=[1], bounds=[(0, 1), (0, 1), (None, None)], method="highs")
    cols = optimize.linprog([0, 0, 1], A_ub=np.column_stack([G, -np.ones(2)]), b_ub=[0, 0], A_eq=[[1, 1, 0]],
                            b_eq=[1], bounds=[(0, 1), (0, 1), (None, None)], method="highs")
    return [float(rows.x[0]), float(cols.x[0]), float(-rows.fun)]


p_20r, q_20r, v_20r = strategies_20r([[55, 95], [85, 60]])
wbm.record("M27.20a", [p_20r, q_20r, v_20r], decimals=6,
           mistakes={"p* rend le joueur des colonnes indifférent (il se calcule avec les colonnes), q* le joueur des lignes":
                         [q_20r, p_20r, v_20r],
                     "p et q sont les probabilités de la première ligne et de la première colonne":
                         [1 - p_20r, 1 - q_20r, v_20r],
                     "sans point selle, la valeur est le gain espéré des stratégies d'indifférence, pas le maximin":
                         [p_20r, q_20r, 60.0]})
formulas_20r = [float(F_20r(3 - 1, 4 - 7 - 1 + 3)), float(F_20r(3 - 7, 4 - 7 - 1 + 3))]
saddle_20r = strategies_20r([[4, 7], [1, 3]])
wbm.record("M27.20b", formulas_20r + saddle_20r, decimals=6,
           mistakes={"avec un point selle, ta fonction rend les stratégies pures de pure_strategy_values, pas les formules":
                         formulas_20r + formulas_20r + [float(F_20r(4 * 3 - 7 * 1, 4 - 7 - 1 + 3))],
                     "p* = (d − c)/κ et q* = (d − b)/κ, avec κ = a − b − c + d": formulas_20r[::-1] + saddle_20r})
G_20r = np.array([[55.0, 95.0], [85.0, 60.0]])
wbm.record("M27.20c", [float((np.array([p_20r, 1 - p_20r]) @ G_20r).min()), float((G_20r @ np.array([q_20r, 1 - q_20r])).max())],
           decimals=6,
           mistakes={"p* pondère les lignes de G (pᵀG), q* ses colonnes (G q)":
                         [float((np.array([q_20r, 1 - q_20r]) @ G_20r).min()), float((G_20r @ np.array([p_20r, 1 - p_20r])).max())]})'''),
    ],
)

GIVEN_21 = '''A_GAME_21 = np.array([[1.0, -2.0, 0.0], [0.5, 1.0, -1.0]])   # c): x in R², y in R³'''

CHECK_21 = '''WRONG_C21B = __WRONG_C21B__   # (message, value) of two classic wrong deviations of Q on xy
WRONG_C21C = __WRONG_C21C__   # the same on the game A_GAME_21

with checked("M27.21"):
    if not filled(answer_M27_21b):
        print("⏳ Ex M27.21b : pas encore fait.")
    elif not isinstance(answer_M27_21b, (list, tuple)) or len(answer_M27_21b) != 2:
        print("❌ Ex M27.21b : attendu une liste de 2 : le plus grand écart de Q (un nombre), puis le booléen.")
    else:
        check_rounding("M27.21b", "le plus grand écart de Q sur 200 pas alternés", answer_M27_21b[0], 1e-12, WRONG_C21B)
        check_answer("M27.21b", answer_M27_21b[1])

with checked("M27.21"):
    if not filled(answer_M27_21c):
        print("⏳ Ex M27.21c : pas encore fait.")
    elif not isinstance(answer_M27_21c, (list, tuple)) or len(answer_M27_21c) != 2:
        print("❌ Ex M27.21c : attendu une liste de 2 : le booléen, puis le plus grand écart (un nombre).")
    else:
        check_answer("M27.21c", answer_M27_21c[0])
        check_rounding("M27.21c", "le plus grand écart de ‖x‖² + ‖y‖² − η xᵀAy sur 100 pas alternés", answer_M27_21c[1],
                       1e-12, WRONG_C21C)'''

NOTE_21 = (r"`xs = np.empty((n_steps + 1, n))`, `ys = np.empty((n_steps + 1, m))`, puis `x_new = x - eta * (A @ y)` et "
           r"`y = y + eta * (A.T @ (x_new if alternating else x))`. a) $1{,}36^2 = 1{,}8496$ et $1{,}36^{2{,}5} \approx "
           r"2{,}1570$ : 5 pas, comme M27.4 c). b) Un écart de l'ordre de $10^{-15}$ ; vrai (la plus grande distance vaut "
           r"$\approx 1{,}195226$, sous $1/\sqrt{0{,}7} \approx 1{,}195229$). c) Vrai ($\eta\lVert\mathbf{A}\rVert_2 \approx "
           r"0{,}71$ ; la somme des carrés est multipliée par $\approx 7 \times 10^8$ en 50 pas) ; un écart de l'ordre de "
           r"$10^{-15}$, puisque $\eta\lVert\mathbf{A}\rVert_2 < 2$.")

M27_21 = Ex(
    "M27.21", "🔨", 2, 20, "Les itérés de la descente-montée simultanée ou alternée sur un jeu bilinéaire xᵀAy · "
    "`descent_ascent_iterates`",
    "programmer les deux descentes-montées, puis vérifier aux arrondis près les deux propriétés de la fiche : l'une "
    "éloigne de l'équilibre, l'autre garde une quantité constante.", "fiche §4 ; M22 ; Ex M27.4", tracks="C",
    mymath="distances.py", given=GIVEN_21, note=NOTE_21,
    body=REMINDER + r"""

Écris `descent_ascent_iterates(A, x0, y0, eta, n_steps=10, alternating=False)` (fiche §4), en suivant sa docstring : les itérés de la descente-montée sur $f(\mathbf{x}, \mathbf{y}) = \mathbf{x}^\top\mathbf{A}\mathbf{y}$, où le joueur $\mathbf{x}$ (les lignes de $\mathbf{A}$) **minimise**, comme dans MML (7.23). Contrôle `A` (2-D, non vide, de nombres finis), `x0` et `y0` (des tableaux **1-D** de $n$ et de $m$ coordonnées : `np.array([1.0])`, pas `np.array([[1.0]])`), `eta` (un nombre fini $> 0$, pas un booléen) et `n_steps` (un entier $\ge 0$, ni un booléen ni un flottant) ; prépare deux tableaux de formes $(N + 1, n)$ et $(N + 1, m)$, de lignes 0 les départs ; à chaque pas, calcule le nouveau $\mathbf{x}$ à partir de l'ancien $\mathbf{y}$, puis le nouveau $\mathbf{y}$ à partir de l'ancien $\mathbf{x}$ (simultané) ou du nouveau (alterné) ; rends `(xs, ys)`.

**L'usage.** Sur $xy$ (`A = [[1.0]]`, depuis $x_0 = 1$ et $y_0 = 0$, avec $\eta = 0{,}6$), avec ta fonction :
- a) en simultané, la distance à l'équilibre $\sqrt{x_k^2 + y_k^2}$ après 4 pas, puis après 5 pas (une liste de 2 nombres), à comparer à ta réponse c) de M27.4 ;
- b) en alterné, sur 200 pas : le plus grand écart $\lvert Q(x_k, y_k) - Q(x_0, y_0)\rvert$, avec $Q(x, y) = x^2 + y^2 - \eta xy$, et vrai ou faux, la distance à l'équilibre ne dépasse jamais $1/\sqrt{0{,}7}$, le demi-grand axe de l'ellipse $Q = 1$ (une liste de 2 : le nombre, tel que calculé, puis le booléen) ;
- c) sur le jeu de matrice $\mathbf{A} = \begin{pmatrix} 1 & -2 & 0 \\ 0{,}5 & 1 & -1 \end{pmatrix}$ (`A_GAME_21` ; $\mathbf{x} \in \mathbb{R}^2$, $\mathbf{y} \in \mathbb{R}^3$), avec $\eta = 0{,}3$, depuis $\mathbf{x}_0 = (1, 0)$ et $\mathbf{y}_0 = (0, 1, 0)$ : vrai ou faux, en simultané, $\lVert\mathbf{x}_k\rVert^2 + \lVert\mathbf{y}_k\rVert^2$ ne diminue jamais sur 50 pas ; puis, en alterné, le plus grand écart de $\lVert\mathbf{x}_k\rVert^2 + \lVert\mathbf{y}_k\rVert^2 - \eta\,\mathbf{x}_k^\top\mathbf{A}\mathbf{y}_k$ à sa valeur de départ sur 100 pas (une liste de 2 : le booléen, puis le nombre, tel que calculé).

La vérification des deux écarts attend une erreur d'arrondi (moins de $10^{-12}$). Ce qu'il faut observer : les deux propriétés de la fiche, vérifiées aux arrondis près, l'une qui éloigne de l'équilibre, l'autre qui garde une quantité constante.""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_descent_ascent_iterates_") + [
        ("md", "**L'usage** : le jeu $xy$ en simultané et en alterné, puis un jeu de $\\mathbb{R}^2 \\times \\mathbb{R}^3$."),
        ("todo", '''answer_M27_21a = answer_M27_21b = answer_M27_21c = ...
with wbm.attempt("M27.21"):          # if you call descent_ascent_iterates here: ⏳ while it is not written
    answer_M27_21a = ...  # a) a list of 2 numbers, as computed: the distance to (0, 0) after 4, then after 5 simultaneous steps (xy, η = 0.6, from (1, 0))
    answer_M27_21b = ...  # b) a list of 2: the largest |Q(x_k, y_k) − Q(x_0, y_0)| over 200 alternating steps (as computed), then True or False: the distance never exceeds 1/√0.7
    answer_M27_21c = ...  # c) a list of 2: True or False: in simultaneous steps, ‖x‖² + ‖y‖² never decreases over 50 steps (A_GAME_21, η = 0.3); then the largest gap of ‖x‖² + ‖y‖² − η xᵀAy to its start over 100 alternating steps (as computed)'''),
        ("check", "check_answer(\"M27.21a\", answer_M27_21a)\n\n" + CHECK_21),
        ("solution", '''descent_ascent_iterates = mymath.distances.descent_ascent_iterates
xs_21, ys_21 = descent_ascent_iterates([[1.0]], np.array([1.0]), np.array([0.0]), 0.6, n_steps=5)
distance_21 = np.hypot(xs_21[:, 0], ys_21[:, 0])
answer_M27_21a = [float(distance_21[4]), float(distance_21[5])]
xs_21, ys_21 = descent_ascent_iterates([[1.0]], np.array([1.0]), np.array([0.0]), 0.6, n_steps=200, alternating=True)
Q_21 = xs_21[:, 0] ** 2 + ys_21[:, 0] ** 2 - 0.6 * xs_21[:, 0] * ys_21[:, 0]
answer_M27_21b = [float(np.abs(Q_21 - Q_21[0]).max()), bool(np.hypot(xs_21[:, 0], ys_21[:, 0]).max() <= 1 / math.sqrt(0.7))]
x0_21, y0_21 = np.array([1.0, 0.0]), np.array([0.0, 1.0, 0.0])
xs_21, ys_21 = descent_ascent_iterates(A_GAME_21, x0_21, y0_21, 0.3, n_steps=50)
squares_21 = (xs_21 ** 2).sum(axis=1) + (ys_21 ** 2).sum(axis=1)
xs_21, ys_21 = descent_ascent_iterates(A_GAME_21, x0_21, y0_21, 0.3, n_steps=100, alternating=True)
kept_21 = (xs_21 ** 2).sum(axis=1) + (ys_21 ** 2).sum(axis=1) - 0.3 * np.einsum("ki,ij,kj->k", xs_21, A_GAME_21, ys_21)
answer_M27_21c = [bool(np.all(np.diff(squares_21) >= 0)), float(np.abs(kept_21 - kept_21[0]).max())]
print("a)", answer_M27_21a, " b)", answer_M27_21b, " c)", answer_M27_21c)
print("   c) la somme des carrés est multipliée par", f"{squares_21[-1] / squares_21[0]:.3g}", "en 50 pas simultanés")'''),
        ("record", '''M_21r = np.array([[1.0, -0.6], [0.6, 1.0]])                    # one simultaneous step on xy
distance_21r = [float(np.linalg.norm(np.linalg.matrix_power(M_21r, k) @ [1.0, 0.0])) for k in range(6)]
wbm.record("M27.21a", [distance_21r[4], distance_21r[5]], decimals=6,
           mistakes={"la distance à l'équilibre est la norme √(x² + y²), pas son carré":
                         [distance_21r[4] ** 2, distance_21r[5] ** 2],
                     "la ligne k du tableau est l'itéré après k pas ; la ligne 0 est le départ": distance_21r[3:5]})
wbm.record("M27.21b", True,
           mistakes={"les itérés alternés restent sur l'ellipse Q = Q(x₀, y₀) ; compare leur plus grande distance à "
                     "(0, 0) au demi-grand axe de cette ellipse": False})
wbm.record("M27.21c", True,
           mistakes={"en simultané, ‖x‖² + ‖y‖² augmente à chaque pas (fiche §4) : compare chaque valeur à la précédente":
                         False})'''),
    ],
)

NOTE_22 = (r"Les contrôles (`numbers.Real`, ni `bool` ni `np.bool_`, `math.isfinite`, écarts-types $\ge 0$), puis "
           r"`float(math.hypot(mu1 - mu2, sigma1 - sigma2))`. a) 1,3. b) $\approx 0{,}2886$. c) 2.")

M27_22 = Ex(
    "M27.22", "🔨", 1, 10, "W₂ de deux gaussiennes en dimension 1, à partir des moyennes et des écarts-types · "
    "`w2_gaussians_1d`",
    "programmer W₂ de deux gaussiennes de la droite, avec des écarts-types et sans élever au carré, et le lire comme une "
    "distance euclidienne.", "fiche §8 ; Ex M27.8 et M27.16", tracks="C, E", mymath="distances.py", note=NOTE_22,
    body=REMINDER + r"""

Écris `w2_gaussians_1d(mu1, sigma1, mu2, sigma2)` (fiche §8), en suivant sa docstring : $W_2$ entre $\mathcal{N}(\mu_1, \sigma_1^2)$ et $\mathcal{N}(\mu_2, \sigma_2^2)$ à partir des **écarts-types** ; contrôle les quatre nombres (des réels finis, pas des booléens) et le signe des écarts-types (un écart-type nul est permis : la loi est alors une masse ponctuelle) ; rends $W_2$, pas son carré, en `float` Python (`math.hypot`).

**L'usage.** Avec ta fonction :
- a) les sachets de M27.8 (`BAGS_BEFORE`, `BAGS_AFTER`, des couples (moyenne, écart-type)) (un nombre), à comparer à ta réponse c) ;
- b) la machine du 🔗 M27.16 (`SHAFTS_BEFORE`, `SHAFTS_AFTER`) (un nombre), à comparer à ta réponse b) ;
- c) $\mathcal{N}(10 ;\ 3^2)$ contre $\mathcal{N}(10 ;\ 1^2)$ (un nombre).

Ce qu'il faut observer : $W_2$ est la distance euclidienne entre les points (moyenne, écart-type) du plan.""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_w2_gaussians_1d_") + [
        ("md", "**L'usage** : les sachets, la machine, et deux gaussiennes de même moyenne."),
        ("todo", '''answer_M27_22a = answer_M27_22b = answer_M27_22c = ...
with wbm.attempt("M27.22"):          # if you call w2_gaussians_1d here: ⏳ while it is not written
    answer_M27_22a = ...  # a) a number, as returned: the bags, BAGS_BEFORE against BAGS_AFTER
    answer_M27_22b = ...  # b) a number, as returned: the machine, SHAFTS_BEFORE against SHAFTS_AFTER
    answer_M27_22c = ...  # c) a number, as returned: N(10, 3²) against N(10, 1²)'''),
        ("check", answers_check("M27.22", "abc")),
        ("solution", '''w2_gaussians_1d = mymath.distances.w2_gaussians_1d
answer_M27_22a = w2_gaussians_1d(*BAGS_BEFORE, *BAGS_AFTER)
answer_M27_22b = w2_gaussians_1d(*SHAFTS_BEFORE, *SHAFTS_AFTER)
answer_M27_22c = w2_gaussians_1d(10.0, 3.0, 10.0, 1.0)
print("a)", answer_M27_22a, " b)", answer_M27_22b, " c)", answer_M27_22c)'''),
        ("record", '''def w2_22r(m1, s1, m2, s2):
    """The oracle: √∫₀¹ (F₁⁻¹(u) − F₂⁻¹(u))² du, by scipy.integrate.quad and scipy.stats.norm.ppf."""
    gap = lambda u: (m1 + s1 * stats.norm.ppf(u) - m2 - s2 * stats.norm.ppf(u)) ** 2
    return math.sqrt(integrate.quad(gap, 0, 1, limit=200)[0])


for letter_22r, (m1_22r, s1_22r, m2_22r, s2_22r) in zip("abc", [(20.0, 1.5, 21.2, 1.0), (50.30, 0.12, 50.02, 0.05),
                                                                (10.0, 3.0, 10.0, 1.0)]):
    wrong_22r = {"des écarts-types, pas des variances : ta fonction reçoit σ, et la formule soustrait les σ":
                     math.hypot(m1_22r - m2_22r, s1_22r ** 2 - s2_22r ** 2),
                 "la fonction rend W₂, pas son carré": (m1_22r - m2_22r) ** 2 + (s1_22r - s2_22r) ** 2}
    if letter_22r != "c":
        wrong_22r["W₂ est la racine d'une somme de deux carrés, pas |Δμ| + |Δσ|"] = abs(m1_22r - m2_22r) + abs(s1_22r - s2_22r)
    wbm.record(f"M27.22{letter_22r}", w2_22r(m1_22r, s1_22r, m2_22r, s2_22r), decimals=6, mistakes=wrong_22r)'''),
    ],
)

GIVEN_23 = '''DEPOTS_MAP = np.array([[1.0, 0.0], [4.0, 3.0], [6.0, -2.0]])    # c): the depots on a map (km)
STORES_MAP = np.array([[2.0, -3.0], [3.0, 4.0], [8.0, 1.0]])    # the stores on the map (km)'''

CHECK_23 = '''NW_C23 = __NW_C23__   # masses you do not see, and the north-west plans expected
LP_C23 = __LP_C23__   # a cost matrix you do not see, its masses, and the optimal cost

with checked("M27.23"):
    results_23 = []
    report_23 = reporter(results_23)
    for case_c23 in NW_C23:
        a_c23, b_c23 = np.array(case_c23["a"]), np.array(case_c23["b"])
        got_c23 = northwest_23(a_c23.copy(), b_c23.copy())
        if matches(got_c23, case_c23["want"], rtol=1e-9, atol=1e-9):
            continue
        arr_c23 = as_floats(got_c23)
        if arr_c23 is not None and arr_c23.shape == (len(b_c23), len(a_c23)):
            why_c23 = "ton plan a la forme (n, m) : une ligne par masse de a (les départs), une colonne par masse de b"
        elif arr_c23 is not None and arr_c23.shape == (len(a_c23), len(b_c23)) and not np.allclose(arr_c23.sum(axis=1), a_c23):
            why_c23 = ("les sommes des lignes doivent redonner a, celles des colonnes b : descends quand la ligne est "
                       "vide, va à droite quand la colonne est pleine")
        else:
            why_c23 = f"attendu {shown(case_c23['want'])}, reçu {shown(got_c23)[:160]}"
        report_23(False, "", f"northwest_23, des masses que tu ne vois pas (a = {case_c23['a']}, b = {case_c23['b']}) : "
                  f"{why_c23}")
    report_23(True, "northwest_23 : des masses que tu ne vois pas, dont une ligne et une colonne qui se vident ensemble", "")
    C_c23, a_c23, b_c23 = (np.array(LP_C23[key]) for key in ("C", "a", "b"))
    plan_c23, cost_c23 = pair("M27.23", "transport_lp_23", transport_lp_23(C_c23.copy(), a_c23.copy(), b_c23.copy()),
                              names=("plan", "cost"))
    plan_c23 = np.asarray(plan_c23, dtype=float)
    report_23(plan_c23.shape == C_c23.shape, "transport_lp_23 rend un plan de la forme de C",
              f"transport_lp_23 : le plan doit avoir la forme de C, {C_c23.shape}, reçu {plan_c23.shape}")
    report_23(np.allclose(plan_c23.sum(axis=1), a_c23, atol=1e-7) and np.allclose(plan_c23.sum(axis=0), b_c23, atol=1e-7)
              and plan_c23.min() >= -1e-9, "son plan respecte les deux marges et reste positif",
              "transport_lp_23 : le plan doit avoir pour sommes des lignes a, pour sommes des colonnes b, et des "
              "coefficients ≥ 0 (les inconnues sont rangées ligne par ligne : γ_ij est l'inconnue i n + j)")
    report_23(abs(float(cost_c23) - float((plan_c23 * C_c23).sum())) <= 1e-7,
              "le coût rendu est celui du plan rendu", "transport_lp_23 : cost doit être le coût du plan rendu, Σ γᵢⱼ cᵢⱼ")
    report_23(abs(float(cost_c23) - LP_C23["optimum"]) <= 1e-7,
              f"une matrice de coûts que tu ne vois pas (3 × 4) : le coût optimal, {fr(LP_C23['optimum'], 4)}",
              f"une matrice de coûts que tu ne vois pas : attendu le coût optimal {fr(LP_C23['optimum'], 4)}, reçu "
              f"{fr(float(cost_c23), 4)} (le programme minimise Σ γᵢⱼ cᵢⱼ)")
    verdict("M27.23", all(results_23), "tes deux fonctions passent les cas cachés.", "")'''

NOTE_23 = (r"a) 155 t·km, $W_1 = 1{,}55$ km ; vrai. `linprog` peut rendre un autre plan optimal : pour le coût "
           r"$\lvert x - y\rvert$, l'optimum n'est pas unique (un trajet de 4 à 3 puis de 6 à 2 coûte autant qu'un trajet "
           r"de 4 à 2 puis de 6 à 3). b) 275 t·km², $W_2 = \sqrt{2{,}75} \approx 1{,}6583$ km ; vrai : pour un coût "
           r"strictement convexe, le plan optimal est unique, et c'est le plan monotone. c) $\approx 298{,}34$ t·km pour "
           r"`linprog`, $\approx 355{,}84$ pour le coin nord-ouest dans l'ordre des abscisses.")

M27_23 = Ex(
    "M27.23", "📦", 2, 25, "`scipy.optimize.linprog` : le transport optimal entre deux lois discrètes de la droite comme "
    "programme linéaire, comparé au plan monotone et à l'aire entre les fonctions de répartition",
    "écrire le transport optimal comme un programme linéaire, le résoudre par une bibliothèque, et voir que sur la droite "
    "le plan monotone suffit, pas dans le plan.", "fiche §7 et §8 ; M10 ; Ex M27.7", tracks="C", given=GIVEN_23,
    note=NOTE_23,
    body=r"""Écris `transport_lp_23(C, a, b)`, qui résout le programme linéaire du transport (fiche §7) par `scipy.optimize.linprog(..., method="highs")` : les $mn$ inconnues $\gamma_{ij}$ rangées ligne par ligne ($\gamma_{ij}$ est l'inconnue $i\,n + j$), le coût $\sum\gamma_{ij}c_{ij}$, les $m + n$ contraintes d'égalité des marges (l'une est redondante : `linprog` s'en accommode) et $\gamma_{ij} \ge 0$ ; elle rend `(plan, cost)`, le plan de forme $(m, n)$ et son coût. Écris aussi `northwest_23(a, b)`, qui rend le plan du coin nord-ouest (fiche §8) pour deux tableaux de masses de même somme, les points étant supposés rangés dans l'ordre croissant.

Avec les dépôts et les magasins de M27.7 (la cellule de données de la partie A : `DEPOTS_KM`, `DEPOTS_T`, `STORES_KM`, `STORES_T`, masses en tonnes) :
- a) pour le coût $c_{ij} = \lvert x_i - y_j\rvert$ : le coût optimal (t·km), $W_1$ (km), et vrai ou faux, le plan du coin nord-ouest a le même coût, à $10^{-9}$ près (une liste de 3 : les deux nombres, puis le booléen) ;
- b) pour le coût $(x_i - y_j)^2$ : le coût optimal (t·km²), $W_2$ (km), et vrai ou faux, le plan de `linprog` est le plan du coin nord-ouest, à $10^{-6}$ près (une liste de 3 : les deux nombres, puis le booléen) ;
- c) on quitte la route : les dépôts sont aux points $(1, 0)$, $(4, 3)$ et $(6, -2)$ d'une carte, les magasins aux points $(2, -3)$, $(3, 4)$ et $(8, 1)$ (en km ; `DEPOTS_MAP`, `STORES_MAP`), avec les mêmes masses et le coût $\lVert\mathbf{x}_i - \mathbf{y}_j\rVert$ : le coût optimal, puis le coût du plan du coin nord-ouest pris dans l'ordre des abscisses (une liste de 2 nombres, t·km ; 2 décimales dans ta copie).

Compare enfin a) à ton $W_1$ de M27.7, obtenu aussi par l'aire entre les fonctions de répartition. La vérification essaie aussi `northwest_23` et `transport_lp_23` sur des cas que tu ne vois pas. Ce qu'il faut observer : sur la droite, le plan monotone est optimal pour les deux coûts, et l'aire entre les fonctions de répartition donne $W_1$ sans programme linéaire ; pour le coût $\lvert x - y\rvert$, l'optimum n'est pas toujours unique, et `linprog` peut rendre un autre plan de même coût ; dans le plan, l'ordre ne veut plus rien dire, et il faut le programme linéaire.""",
    todo='''def transport_lp_23(C, a, b):
    """The optimal transport plan by scipy.optimize.linprog(..., method="highs"): the m n unknowns γ_ij row by row (γ_ij is
    the unknown i n + j), the cost Σ γ_ij c_ij, the m + n equalities of the margins, γ_ij >= 0. Returns (plan, cost): the
    (m, n) plan and its cost."""
    raise NotImplementedError("transport_lp_23 n'est pas encore écrite (04_indices.md si tu bloques)")


def northwest_23(a, b):
    """The plan of the north-west corner rule for two arrays of masses of the same sum (the points in increasing order):
    from the top left cell, the largest mass possible, then down if the row is empty, right if the column is full."""
    raise NotImplementedError("northwest_23 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M27_23a = answer_M27_23b = answer_M27_23c = ...
with wbm.attempt("M27.23"):          # your two functions: ⏳ while they are not written
    answer_M27_23a = ...  # a) a list of 3: the optimal cost for |x − y| (t·km), W1 (km), then True or False: the north-west plan has the same cost (to 1e-9)
    answer_M27_23b = ...  # b) a list of 3: the optimal cost for (x − y)² (t·km²), W2 (km), then True or False: the plan of linprog is the north-west plan (to 1e-6)
    answer_M27_23c = ...  # c) a list of 2 numbers, as computed: on the map, the optimal cost, then the cost of the north-west plan in the order of the abscissas (t·km)''',
    check=answers_check("M27.23", "abc") + "\n\n" + CHECK_23,
    solution='''def transport_lp_23(C, a, b):
    """The optimal transport plan by scipy.optimize.linprog(..., method="highs"): the m n unknowns γ_ij row by row (γ_ij is
    the unknown i n + j), the cost Σ γ_ij c_ij, the m + n equalities of the margins, γ_ij >= 0. Returns (plan, cost): the
    (m, n) plan and its cost."""
    C, a, b = (np.asarray(v, dtype=float) for v in (C, a, b))
    m, n = C.shape
    margins = np.vstack([np.kron(np.eye(m), np.ones(n)),          # Σ_j γ_ij = a_i
                         np.kron(np.ones(m), np.eye(n))])         # Σ_i γ_ij = b_j
    result = optimize.linprog(C.ravel(), A_eq=margins, b_eq=np.concatenate([a, b]), bounds=(0, None), method="highs")
    return result.x.reshape(m, n), float(result.fun)


def northwest_23(a, b):
    """The plan of the north-west corner rule for two arrays of masses of the same sum (the points in increasing order):
    from the top left cell, the largest mass possible, then down if the row is empty, right if the column is full."""
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    plan = np.zeros((len(a), len(b)))
    i = j = 0
    while i < len(a) and j < len(b):
        row_first = a[i] <= b[j]                                    # the row empties first (or both at once)
        plan[i, j] = min(a[i], b[j])
        a[i], b[j] = a[i] - plan[i, j], b[j] - plan[i, j]
        i, j = (i + 1, j) if row_first else (i, j + 1)
    return plan


total_23 = DEPOTS_T.sum()
C1_23 = np.abs(DEPOTS_KM[:, None] - STORES_KM[None, :])
plan1_23, cost1_23 = transport_lp_23(C1_23, DEPOTS_T, STORES_T)
nw_23 = northwest_23(DEPOTS_T, STORES_T)
answer_M27_23a = [cost1_23, float(cost1_23 / total_23), bool(abs((nw_23 * C1_23).sum() - cost1_23) <= 1e-9)]
C2_23 = C1_23 ** 2
plan2_23, cost2_23 = transport_lp_23(C2_23, DEPOTS_T, STORES_T)
answer_M27_23b = [cost2_23, math.sqrt(cost2_23 / total_23), bool(np.allclose(plan2_23, nw_23, rtol=0, atol=1e-6))]
C3_23 = np.linalg.norm(DEPOTS_MAP[:, None, :] - STORES_MAP[None, :, :], axis=2)
order_d_23, order_s_23 = np.argsort(DEPOTS_MAP[:, 0]), np.argsort(STORES_MAP[:, 0])
nw3_23 = northwest_23(DEPOTS_T[order_d_23], STORES_T[order_s_23])
answer_M27_23c = [transport_lp_23(C3_23, DEPOTS_T, STORES_T)[1], float((nw3_23 * C3_23[order_d_23][:, order_s_23]).sum())]
print("a)", answer_M27_23a, " b)", answer_M27_23b, " c)", np.round(answer_M27_23c, 4).tolist())
print("le plan de linprog pour |x − y| :", np.round(plan1_23, 6).tolist(), "; le coin nord-ouest :", nw_23.tolist())

''' + CHECK_23,
    record='''from scipy.optimize import linear_sum_assignment


def assignment_23r(cost_of, a, b, unit=5):
    """The oracle: the masses split into units of 5 t (all are multiples of 5), then an assignment problem between the
    units (scipy.optimize.linear_sum_assignment): its cost times 5."""
    rows = np.repeat(np.arange(len(a)), np.asarray(a) // unit)
    cols = np.repeat(np.arange(len(b)), np.asarray(b) // unit)
    C = cost_of[np.ix_(rows, cols)]
    r, c = linear_sum_assignment(C)
    return float(C[r, c].sum() * unit)


x_23r, a_23r = np.array([1.0, 4, 6]), np.array([20, 50, 30])
y_23r, b_23r = np.array([2.0, 3, 8]), np.array([40, 35, 25])
c1_23r = assignment_23r(np.abs(x_23r[:, None] - y_23r[None, :]), a_23r, b_23r)
c2_23r = assignment_23r((x_23r[:, None] - y_23r[None, :]) ** 2, a_23r, b_23r)
wbm.record("M27.23a", [c1_23r, c1_23r / 100, True], decimals=6,
           mistakes={"W₁ est le coût minimal pour deux lois de masse totale 1 : divise par la masse totale (100 t)":
                         [c1_23r, c1_23r, True],
                     "compare les coûts, pas les plans : pour le coût |x − y|, plusieurs plans peuvent être optimaux":
                         [c1_23r, c1_23r / 100, False]})
wbm.record("M27.23b", [c2_23r, math.sqrt(c2_23r / 100), True], decimals=6,
           mistakes={"W₂ est la racine du coût minimal par tonne (W₂² est le coût minimal)": [c2_23r, c2_23r / 100, True],
                     "divise par la masse totale avant de prendre la racine": [c2_23r, math.sqrt(c2_23r), True],
                     "pour le coût (x − y)², strictement convexe, le plan optimal est unique : compare les deux plans "
                     "coefficient par coefficient": [c2_23r, math.sqrt(c2_23r / 100), False]})
xm_23r, ym_23r = np.array([[1.0, 0], [4, 3], [6, -2]]), np.array([[2.0, -3], [3, 4], [8, 1]])
d_23r = np.linalg.norm(xm_23r[:, None, :] - ym_23r[None, :, :], axis=2)
nw_23r = np.array([[20.0, 0, 0], [20, 30, 0], [0, 5, 25]])              # the abscissas are already in increasing order
wbm.record("M27.23c", [assignment_23r(d_23r, a_23r, b_23r), float((nw_23r * d_23r).sum())], decimals=6,
           mistakes={"le coût optimal d'abord, puis celui du coin nord-ouest":
                         [float((nw_23r * d_23r).sum()), assignment_23r(d_23r, a_23r, b_23r)],
                     "le coût est la distance ‖xᵢ − yⱼ‖, pas son carré":
                         [assignment_23r(d_23r ** 2, a_23r, b_23r), float((nw_23r * d_23r ** 2).sum())]})''',
    after=[
        ("md", "**Après la vérification**, dans ta copie : pourquoi le plan du coin nord-ouest est-il optimal sur la route, "
               "pour les deux coûts ? Pourquoi `linprog` peut-il rendre un autre plan pour $\\lvert x - y\\rvert$, et pas "
               "pour $(x - y)^2$ ? Que perd-on sur la carte en rangeant les points par abscisse ?"),
    ],
)

PART_A = Part("A", "Ta librairie : les valeurs d'un jeu, ses stratégies optimales, la descente-montée et W₂ ; puis le "
              "transport optimal par SciPy",
              "Fiche §1, §2, §4, §7 et §8. Les quatre fonctions de `mymath/distances.py`, leurs tests, et un usage de "
              "chacune sur les données des exercices papier ; puis le transport optimal comme programme linéaire. La "
              "cellule de données ci-dessous recopie les données des exercices papier.",
              given=TOOLS + "\n\n\n" + DATA, exercises=[M27_19, M27_20, M27_21, M27_22, M27_23])

# ---------------------------------------------------------------------------
# Notebook exercises: predict, measure, draw (M27.24 to M27.26)
# ---------------------------------------------------------------------------
CHECK_24 = '''PATHS_C24 = __PATHS_C24__   # the iterates expected, [xs, ys], for each call of the check


def look_24(ax, eta, n_steps, alternating, key):
    """What is missing in a drawing of draw_paths_24 (French phrases)."""
    xs, ys = PATHS_C24[key]
    missing = []
    if not through(ax, xs, ys, rtol=1e-9, atol=1e-12):
        missing.append(f"les {n_steps + 1} itérés depuis (1, 0), reliés dans l'ordre (x en abscisse, y en ordonnée)")
    if not points_at(ax, [0.0], [0.0], marker_only=True):
        missing.append("l'équilibre (0, 0), marqué par un point")
    if ax.get_aspect() != 1.0:
        missing.append('des axes de même échelle (ax.set_aspect("equal"))')
    title = ax.get_title().lower()
    eta_texts = (f"{eta:g}", f"{eta:g}".replace(".", ","))
    if not any(text in title for text in eta_texts) or ("altern" if alternating else "simultan") not in title:
        missing.append(f"un titre qui donne η ({eta_texts[1]}) et le mode ({'alterné' if alternating else 'simultané'})")
    if not ax.get_xlabel() or not ax.get_ylabel():
        missing.append("des noms d'axes")
    return missing


with checked("M27.24"):
    results_24 = []
    report_24 = reporter(results_24, stop=False)
    fig_c24, ax_c24 = plt.subplots()
    try:
        with own_code("M27.24", "draw_paths_24", REF_DISTANCES):
            opened_c24 = drawn(draw_paths_24, ax_c24, 0.45, 12, True)
        missing_c24 = look_24(ax_c24, 0.45, 12, True, "hidden")
    finally:
        plt.close(fig_c24)
    fig_24, axes_24 = plt.subplots(1, 3, figsize=(15, 4.6))
    try:
        opened_24 = list(opened_c24)
        for ax_24, (eta_24, alternating_24, key_24) in zip(axes_24, ((0.3, False, "0.3-s"), (0.3, True, "0.3-a"),
                                                                     (2.5, True, "2.5-a"))):
            with own_code("M27.24", "draw_paths_24", REF_DISTANCES):
                opened_24 += drawn(draw_paths_24, ax_24, eta_24, 40, alternating_24)
            missing_24 = look_24(ax_24, eta_24, 40, alternating_24, key_24)
            mode_24 = "alterné" if alternating_24 else "simultané"
            report_24(not missing_24, f"η = {fr(eta_24, 1)}, {mode_24} : les 41 itérés, l'équilibre, l'échelle, le titre et "
                      "les axes sont là", f"η = {fr(eta_24, 1)}, {mode_24} : il manque " + " ; ".join(missing_24))
        report_24(not missing_c24, "un appel que tu ne vois pas (un autre pas, 12 pas alternés) est dessiné juste aussi",
                  "un appel que tu ne vois pas (un autre pas, 12 pas alternés) : il manque " + " ; ".join(missing_c24))
        report_24(not opened_24, "draw_paths_24 dessine dans l'axe reçu",
                  "draw_paths_24 doit dessiner dans l'axe reçu, sans ouvrir de figure")
    except BaseException:
        plt.close(fig_24)
        raise
    fig_24.tight_layout()
    plt.show()
    verdict("M27.24", all(results_24), "tes trois trajectoires sont dessinées.", "relis les lignes ❌ ci-dessus.")'''

NOTE_24 = (r"Prédictions attendues : a) (C) ; b) (B) ; c) (B). d) $1{,}09^{20} \approx 5{,}6044$. e) "
           r"$\frac{40\arctan 0{,}3}{2\pi} \approx 1{,}8555$ tour. f) $\approx 23{,}95$ : pour $\eta = 2{,}5$, la trace vaut "
           r"$-4{,}25$ et les valeurs propres $-0{,}25$ et $-4$ ; la distance est multipliée par 4 environ à chaque pas, en "
           r"changeant de côté.")

M27_24 = Ex(
    "M27.24", "🔮", 1, 15, "Prédire la trajectoire de la descente-montée simultanée puis alternée sur xy, puis la tracer : "
    "spirale qui s'éloigne ou courbe fermée ?",
    "prévoir par le module et l'argument des valeurs propres d'un pas la trajectoire de la descente-montée, puis la "
    "tracer, et voir le pas alterné quitter sa courbe fermée pour η > 2.", "fiche §4 ; M22 ; Ex M27.4 et M27.21",
    tracks="C", hypothesis=True, note=NOTE_24,
    body=r"""On joue la descente-montée sur $f(x, y) = xy$ depuis $(x_0, y_0) = (1, 0)$, pendant 40 pas. **Avant d'exécuter quoi que ce soit**, prédis :
- a) avec $\eta = 0{,}3$, en simultané, la distance à l'équilibre après 40 pas vaut environ : (A) 1 ; (B) 1,5 ; (C) 5,6 ; (D) 40 (une lettre) ;
- b) avec $\eta = 0{,}3$, en simultané, le nombre de tours que font les itérés autour de l'équilibre en 40 pas : (A) moins d'un ; (B) entre 1 et 2 ; (C) entre 3 et 4 ; (D) aucun, ils partent en ligne droite (une lettre) ;
- c) avec $\eta = 2{,}5$, en alterné : (A) une courbe fermée ; (B) des itérés qui s'éloignent ; (C) des itérés qui convergent vers $(0, 0)$ (une lettre).

Puis, une fois tes prédictions écrites et vérifiées, écris `draw_paths_24(ax, eta, n_steps, alternating)`, qui dessine sur l'**axe reçu** (sans ouvrir de figure), avec ta `descent_ascent_iterates` (M27.21), les itérés depuis $(1, 0)$ reliés dans l'ordre ($x$ en abscisse, $y$ en ordonnée), l'équilibre marqué par un point, des axes de même échelle (`ax.set_aspect("equal")`), un titre qui donne $\eta$ et le mode (« simultané » ou « alterné »), et des noms d'axes. La vérification l'appelle pour $\eta = 0{,}3$ (simultané, puis alterné) et pour $\eta = 2{,}5$ (alterné), et affiche la figure ; elle l'appelle aussi avec un autre pas, que tu ne vois pas. Relève :
- d) la distance à l'équilibre après 40 pas simultanés avec $\eta = 0{,}3$ (un nombre ; 4 décimales dans ta copie) ;
- e) le nombre de tours de ces 40 pas : l'angle total parcouru, `np.unwrap(np.arctan2(y, x))` du premier au dernier itéré, divisé par $2\pi$ (un nombre ; 4 décimales dans ta copie) ;
- f) $\log_{10}$ de la distance à l'équilibre après 40 pas alternés avec $\eta = 2{,}5$ (un nombre ; 2 décimales dans ta copie).

La vérification de l'expérience ne s'exécute qu'une fois tes trois prédictions écrites. Ce qu'il faut observer : la spirale est réglée par le module et l'argument de $1 \pm i\eta$ ; le pas alterné ne reste sur une courbe fermée que pour $\eta < 2$.""",
    todo='''prediction_M27_24a = ...  # a) "A", "B", "C" or "D", written BEFORE the experiment: η = 0.3, simultaneous, the distance after 40 steps is about...
prediction_M27_24b = ...  # b) "A", "B", "C" or "D": the number of turns of these 40 steps
prediction_M27_24c = ...  # c) "A", "B" or "C": η = 2.5, alternating''',
    check='''for letter, prediction in zip("abc", [prediction_M27_24a, prediction_M27_24b, prediction_M27_24c]):
    wbm.check(f"M27.24{letter}", prediction)''',
    record='''def path_24r(eta, n_steps, alternating):
    """The iterates on xy from (1, 0) by the powers of the matrix of one step (the oracle)."""
    M = np.array([[1.0, -eta], [eta, 1.0 - eta ** 2 if alternating else 1.0]])
    return np.array([np.linalg.matrix_power(M, k) @ [1.0, 0.0] for k in range(n_steps + 1)])


far_24r = float(np.linalg.norm(path_24r(0.3, 40, False)[-1]))
options_24r = {"A": 1.0, "B": 1.5, "C": 5.6, "D": 40.0}
wbm.record("M27.24a", min(options_24r, key=lambda k: abs(math.log(options_24r[k] / far_24r))), prediction=True,
           mistakes={"le module √(1 + η²) des valeurs propres dépasse 1 : la distance est multipliée par lui à chaque pas": "A",
                     "un même facteur √(1 + η²) à chaque pas, 40 fois : la distance croît comme une puissance": {"B", "D"}})
turns_24r = 40 * math.atan(0.3) / (2 * math.pi)
wbm.record("M27.24b", "B" if 1 <= turns_24r < 2 else "A", prediction=True,
           mistakes={"chaque pas fait tourner (x, y) de l'argument de 1 + iη, arctan η : compte les tours de 40 pas": {"A", "C"},
                     "M_s est une rotation suivie d'un agrandissement : les itérés tournent autour de l'équilibre": "D"})
grows_24r = float(np.linalg.norm(path_24r(2.5, 40, True)[-1])) > 1e3
wbm.record("M27.24c", "B" if grows_24r else "A", prediction=True,
           mistakes={"pour η > 2, la trace 2 − η² du pas alterné sort de [−2, 2] : ses valeurs propres sont réelles, de "
                     "produit 1": "A",
                     "le déterminant du pas alterné reste 1 : ses deux valeurs propres ne peuvent pas être toutes deux de "
                     "module < 1": "C"})''',
    after=[
        ("md", "**L'expérience.** Écris-la une fois tes trois prédictions vérifiées ; sa vérification ne s'exécute qu'à cette "
               "condition."),
        ("todo", '''def draw_paths_24(ax, eta, n_steps, alternating):
    """In ax, with your descent_ascent_iterates: the iterates on xy from (1, 0), joined in order (x horizontal, y
    vertical); the equilibrium (0, 0) marked by a point; axes of the same scale (ax.set_aspect("equal")); a title that
    gives eta and the mode (« simultané » or « alterné »); axis labels. No other axes."""
    raise NotImplementedError("draw_paths_24 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M27_24d = answer_M27_24e = answer_M27_24f = ...
with wbm.attempt("M27.24"):          # your descent_ascent_iterates: ⏳ while it is not written
    answer_M27_24d = ...  # d) a number, as computed: the distance to (0, 0) after 40 simultaneous steps, η = 0.3
    answer_M27_24e = ...  # e) a number, as computed: the number of turns of these 40 steps (unwrapped angle / 2π)
    answer_M27_24f = ...  # f) a number, as computed: log10 of the distance after 40 alternating steps, η = 2.5'''),
        ("check", guarded(CHECK_24 + "\n\n" + answers_check("M27.24", "def"),
                          [f"prediction_M27_24{letter}" for letter in "abc"],
                          "⏳ Écris d'abord tes trois prédictions, puis exécute à nouveau.")),
        ("solution", '''descent_ascent_iterates = mymath.distances.descent_ascent_iterates


def draw_paths_24(ax, eta, n_steps, alternating):
    """In ax, with your descent_ascent_iterates: the iterates on xy from (1, 0), joined in order (x horizontal, y
    vertical); the equilibrium (0, 0) marked by a point; axes of the same scale (ax.set_aspect("equal")); a title that
    gives eta and the mode (« simultané » or « alterné »); axis labels. No other axes."""
    xs, ys = descent_ascent_iterates([[1.0]], np.array([1.0]), np.array([0.0]), eta, n_steps=n_steps,
                                     alternating=alternating)
    ax.plot(xs[:, 0], ys[:, 0], "-", lw=1, marker=".", ms=4, label="itérés")
    ax.plot([0.0], [0.0], "k*", ms=10, label="équilibre")
    ax.set_aspect("equal")
    mode = "alterné" if alternating else "simultané"
    ax.set_title(f"η = {eta:g}".replace(".", ",") + f", pas {mode}, {n_steps} pas", fontsize=10)
    ax.set_xlabel("x (le joueur qui minimise)")
    ax.set_ylabel("y (le joueur qui maximise)")
    ax.legend(fontsize=8)


xs_24, ys_24 = descent_ascent_iterates([[1.0]], np.array([1.0]), np.array([0.0]), 0.3, n_steps=40)
answer_M27_24d = float(np.hypot(xs_24[-1, 0], ys_24[-1, 0]))
angles_24 = np.unwrap(np.arctan2(ys_24[:, 0], xs_24[:, 0]))
answer_M27_24e = float((angles_24[-1] - angles_24[0]) / (2 * math.pi))
xs_24, ys_24 = descent_ascent_iterates([[1.0]], np.array([1.0]), np.array([0.0]), 2.5, n_steps=40, alternating=True)
answer_M27_24f = float(math.log10(np.hypot(xs_24[-1, 0], ys_24[-1, 0])))
print("d)", round(answer_M27_24d, 6), " e)", round(answer_M27_24e, 6), " f)", round(answer_M27_24f, 6))
print("   valeurs propres du pas alterné pour η = 2,5 :", np.round(np.linalg.eigvals([[1, -2.5], [2.5, 1 - 6.25]]), 4).tolist())

''' + CHECK_24),
        ("record", '''end_24r = path_24r(0.3, 40, False)
wbm.record("M27.24d", float(np.linalg.norm(end_24r[-1])), decimals=6,
           mistakes={"la distance à l'équilibre est la norme √(x² + y²), pas son carré": float(end_24r[-1] @ end_24r[-1]),
                     "d) porte sur les 40 pas simultanés": float(np.linalg.norm(path_24r(0.3, 40, True)[-1]))})
total_24r = float(np.unwrap(np.arctan2(end_24r[:, 1], end_24r[:, 0]))[-1])
wbm.record("M27.24e", total_24r / (2 * math.pi), decimals=6,
           mistakes={"un tour vaut 2π radians : divise l'angle total par 2π": total_24r,
                     "l'angle total se lit sur l'angle déroulé (np.unwrap), pas sur le seul angle du dernier itéré":
                         float(np.arctan2(end_24r[-1, 1], end_24r[-1, 0])) / (2 * math.pi)})
far_alt_24r = float(np.linalg.norm(path_24r(2.5, 40, True)[-1]))
wbm.record("M27.24f", math.log10(far_alt_24r), decimals=6,
           mistakes={"log₁₀, pas le logarithme népérien": math.log(far_alt_24r),
                     "le logarithme de la distance, pas de son carré": math.log10(far_alt_24r ** 2)})'''),
        ("md", "**Après l'expérience**, dans ta copie : pourquoi la spirale fait-elle presque deux tours en 40 pas ? Que "
               "deviennent la spirale et l'ellipse avec $\\eta = 0{,}1$ ? Pourquoi le pas alterné saute-t-il d'un côté à "
               "l'autre de l'équilibre pour $\\eta = 2{,}5$ ?"),
    ],
)

GIVEN_25 = '''MU_25 = np.array([80.0, 25.0, 6.0])                       # the mean of the three dimensions of a shim (mm)
SIGMA_25 = np.array([[0.09, 0.03, 0.0], [0.03, 0.04, 0.01], [0.0, 0.01, 0.01]])   # their covariance (mm²), tr = 0.14
SIZES_25 = [(5, 5), (20, 20), (80, 80), (5, 80), (80, 5)]  # (n1, n2): two series of the same machine
SHIFT_25 = np.array([0.05, 0.0, 0.0])                     # a true shift of the first dimension (mm)
N_REP_25 = 4000                                           # the number of simulated pairs of series'''

HINTS_25 = '''MEANS_C25 = __MEANS_C25__   # the means of a) for (5, 5), (20, 20), (80, 80), rounded to 4 decimals (the figure, a hint)


def means_hint_25(value):
    """a): means close to the expected ones (within 10 %), not equal to them: the order of the draws."""
    got = np.asarray(value, dtype=float)
    if got.shape == (3, 5) and np.all(np.abs(got[0, :3] / np.array(MEANS_C25) - 1) < 0.1):
        return ("tes moyennes ont le bon ordre de grandeur : les valeurs exactes demandent les tirages dans l'ordre de "
                "l'énoncé (à chaque appel, la série 1 puis la série 2 ; les appels dans l'ordre de SIZES_25), avec le "
                "même rng")
    return None'''

CHECK_25 = '''HIDDEN_C25 = __HIDDEN_C25__   # a case you do not see: its data, the value expected, three classic wrong values

with checked("M27.25"):
    results_25 = []
    report_25 = reporter(results_25, stop=False)
    h_c25 = HIDDEN_C25
    got_c25 = distance_bias_25(np.array(h_c25["mu1"]), np.array(h_c25["mu2"]), np.array(h_c25["Sigma"]), h_c25["n1"],
                               h_c25["n2"], h_c25["n_rep"], np.random.default_rng(h_c25["seed"]))
    try:
        value_c25 = float(got_c25)
    except (TypeError, ValueError):
        value_c25 = float("nan")
    why_c25 = next((text for key, text in (
        ("second_first", "tu tires la série 2 avant la série 1 : la série 1 d'abord, avec le même rng"),
        ("no_cholesky", "les tirages passent par L = np.linalg.cholesky(Sigma) : x = mu + z @ L.T a pour covariance "
                        "L Lᵀ = Σ"),
        ("norm", "la moyenne porte sur ‖x̄₁ − x̄₂‖², le carré de la norme")) if math.isclose(value_c25, h_c25[key],
                                                                                          rel_tol=1e-9)),
                   f"attendu {h_c25['want']:.6g}, reçu {shown(got_c25)}")
    report_25(math.isclose(value_c25, h_c25["want"], rel_tol=1e-9),
              "distance_bias_25 : un cas que tu ne vois pas (deux moyennes différentes, n1 = 7, n2 = 3), comme attendu",
              f"distance_bias_25, un cas que tu ne vois pas (n1 = 7, n2 = 3, default_rng({h_c25['seed']})) : {why_c25}")
    fig_c25, ax_c25 = plt.subplots()
    try:
        opened_c25 = drawn(draw_bias_25, ax_c25, [3, 9, 27, 81], [0.4, 0.12, 0.035, 0.013], 0.5)
        hidden_ok_c25 = (points_at(ax_c25, [3, 9, 27, 81], [0.4, 0.12, 0.035, 0.013], marker_only=True)
                         and follows(ax_c25, lambda n: 2 * 0.5 / n, 3, 81))
    finally:
        plt.close(fig_c25)
    fig_25, ax_25 = plt.subplots(figsize=(6.5, 4.2))
    try:
        opened_25 = drawn(draw_bias_25, ax_25, [5, 20, 80], list(MEANS_C25), 0.14)
        report_25(not opened_25 and not opened_c25, "draw_bias_25 dessine dans l'axe reçu",
                  "draw_bias_25 doit dessiner dans l'axe reçu, sans ouvrir de figure")
        report_25(points_at(ax_25, [5, 20, 80], MEANS_C25, marker_only=True),
                  "les trois moyennes des séries de même taille sont des points",
                  "il manque les moyennes contre n, en points (un marqueur : ax.plot(ns, means, \\"o\\"), ou ax.scatter)")
        report_25(follows(ax_25, lambda n: 2 * 0.14 / n, 5, 80), "la droite 2 tr Σ / n est tracée de n = 5 à n = 80",
                  "il manque la courbe y = 2 trace / n, tracée sur toute l'étendue des n reçus")
        report_25(ax_25.get_xscale() == "log" and ax_25.get_yscale() == "log", "les deux échelles sont logarithmiques",
                  "les deux échelles doivent être logarithmiques (ax.set_xscale(\\"log\\"), ax.set_yscale(\\"log\\"))")
        report_25(ax_25.get_legend() is not None and ax_25.get_xlabel() != "" and ax_25.get_ylabel() != "",
                  "des noms d'axes et une légende", "draw_bias_25 doit nommer les axes et mettre une légende")
        report_25(hidden_ok_c25, "un appel que tu ne vois pas (d'autres tailles, une autre trace) est dessiné juste aussi",
                  "un appel que tu ne vois pas (ns = [3, 9, 27, 81], trace = 0,5) : il manque les points ou la courbe "
                  "2 trace / n")
    except BaseException:
        plt.close(fig_25)
        raise
    fig_25.tight_layout()
    plt.show()
    verdict("M27.25", all(results_25), "ta simulation et ta figure sont justes.", "relis les lignes ❌ ci-dessus.")'''

NOTE_25 = (r"a) Moyennes $\approx 0{,}0560$ ; $0{,}0138$ ; $0{,}0036$ ; $0{,}0298$ ; $0{,}0291$, contre 0,056 ; 0,014 ; "
           r"0,0035 ; 0,02975 ; 0,02975 : des rapports 0,999 ; 0,986 ; 1,018 ; 1,001 ; 0,978. b) Vrai. c) $\approx 0{,}0585$ "
           r"et $0{,}0061$, puis $0{,}0025$ et $0{,}0026$ une fois le biais retiré, à comparer à 0,0025. d) Vrai : "
           r"$0{,}0585 / 0{,}0025 \approx 23$. Sur la figure, les trois points suivent la droite $2\operatorname{tr}"
           r"\boldsymbol{\Sigma}/n$, de pente $-1$ en échelles logarithmiques.")

M27_25 = Ex(
    "M27.25", "🔬", 2, 20, "Le biais d'une distance estimée : ‖x̄₁ − x̄₂‖² entre deux échantillons d'une même loi de ℝ³, "
    "selon leurs tailles, contre tr Σ₁/n₁ + tr Σ₂/n₂",
    "mesurer par simulation le biais d'une distance estimée entre deux moyennes, le comparer à tr Σ (1/n₁ + 1/n₂), et "
    "voir un petit décalage réel s'y noyer.", "fiche §9 ; M02c ; Ex M27.15", tracks="C", given=GIVEN_25, note=NOTE_25,
    body=r"""Une machine fabrique des cales ; on mesure trois cotes de chacune (en mm), de moyenne $\boldsymbol{\mu} = (80, 25, 6)$ (`MU_25`) et de covariance
$$\boldsymbol{\Sigma} = \begin{pmatrix} 0{,}09 & 0{,}03 & 0 \\ 0{,}03 & 0{,}04 & 0{,}01 \\ 0 & 0{,}01 & 0{,}01 \end{pmatrix}, \qquad \operatorname{tr}\boldsymbol{\Sigma} = 0{,}14\ \text{mm}^2$$
(`SIGMA_25`). Écris `distance_bias_25(mu1, mu2, Sigma, n1, n2, n_rep, rng)`, qui simule `n_rep` paires de séries indépendantes, toutes à la fois avec des tableaux, dans cet ordre : `L = np.linalg.cholesky(Sigma)`, puis la série 1, `mu1 + rng.standard_normal((n_rep, n1, 3)) @ L.T`, puis la série 2, `mu2 + rng.standard_normal((n_rep, n2, 3)) @ L.T` ; elle rend la moyenne, sur les `n_rep` paires, de $\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2$. Écris aussi `draw_bias_25(ax, ns, means, trace)`, qui trace dans l'axe reçu, en échelles logarithmiques, les moyennes des séries de même taille $n$ contre $n$ (des points) et la courbe $2\,\text{trace}/n$ sur toute l'étendue des `ns`, avec des noms d'axes et une légende.

Avec `rng = np.random.default_rng(6425)`, `n_rep = 4000` (`N_REP_25`) et ce même `rng` pour tous les appels, dans l'ordre : deux séries de la même machine (`mu1 = mu2 = MU_25`) pour $(n_1, n_2) = (5, 5)$, $(20, 20)$, $(80, 80)$, $(5, 80)$ et $(80, 5)$ (`SIZES_25`) ; puis, avec `mu2 = MU_25 + SHIFT_25` (un vrai décalage $\boldsymbol{\delta} = (0{,}05 ;\ 0 ;\ 0)$ de la première cote), pour $(5, 5)$ et $(80, 80)$. Relève :
- a) les cinq moyennes, les cinq valeurs $\operatorname{tr}\boldsymbol{\Sigma}\,(\frac{1}{n_1} + \frac{1}{n_2})$, et leurs rapports, moyenne divisée par valeur (une liste de 3 listes de 5 nombres ; 3 décimales pour les rapports dans ta copie) ;
- b) vrai ou faux : les cinq rapports sont à moins de 5 % de 1 ;
- c) avec le décalage, les deux moyennes, puis les mêmes moins $\operatorname{tr}\boldsymbol{\Sigma}\,(\frac{1}{n_1} + \frac{1}{n_2})$, à comparer à $\lVert\boldsymbol{\delta}\rVert^2 = 0{,}0025$ (une liste de 4 nombres) ;
- d) vrai ou faux : avec 5 cales par série, la distance estimée moyenne dépasse vingt fois la vraie distance $\lVert\boldsymbol{\delta}\rVert^2$.

La vérification essaie `distance_bias_25` sur un cas que tu ne vois pas, puis appelle `draw_bias_25` sur les trois tailles égales (avec les moyennes attendues, arrondies) et affiche la figure. Ce qu'il faut conclure : la distance estimée entre deux séries d'une même machine n'est pas nulle, elle suit $\operatorname{tr}\boldsymbol{\Sigma}\,(\frac{1}{n_1} + \frac{1}{n_2})$ ; un petit décalage réel se noie dans ce biais sur de petites séries ; deux distances estimées ne se comparent qu'à tailles égales, ou après avoir retiré le biais.""",
    todo='''def distance_bias_25(mu1, mu2, Sigma, n1, n2, n_rep, rng):
    """n_rep pairs of independent series at once: L = np.linalg.cholesky(Sigma), then the series 1,
    mu1 + rng.standard_normal((n_rep, n1, 3)) @ L.T, then the series 2, mu2 + rng.standard_normal((n_rep, n2, 3)) @ L.T;
    returns the mean over the n_rep pairs of ‖x̄1 − x̄2‖²."""
    raise NotImplementedError("distance_bias_25 n'est pas encore écrite (04_indices.md si tu bloques)")


def draw_bias_25(ax, ns, means, trace):
    """In ax, in log scales on both axes: the means against n (points), and the curve 2 trace / n over the whole range of
    ns; axis labels and a legend. No other axes."""
    raise NotImplementedError("draw_bias_25 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M27_25a = answer_M27_25b = answer_M27_25c = answer_M27_25d = ...
with wbm.attempt("M27.25"):          # your distance_bias_25: ⏳ while it is not written
    answer_M27_25a = ...  # a) a list of 3 lists of 5 numbers, as computed: the five means, the five values tr Σ (1/n1 + 1/n2), their ratios (mean / value)
    answer_M27_25b = ...  # b) True or False: the five ratios are within 5 % of 1
    answer_M27_25c = ...  # c) a list of 4 numbers, as computed: with the shift, the means for (5, 5) and (80, 80), then the same minus tr Σ (1/n1 + 1/n2)
    answer_M27_25d = ...  # d) True or False: with 5 shims per series, the mean estimated distance exceeds twenty times ‖δ‖²''',
    check=HINTS_25 + "\n\n\n" + answers_check("M27.25", "abcd", hints={"a": "means_hint_25"}) + "\n\n" + CHECK_25,
    solution='''def distance_bias_25(mu1, mu2, Sigma, n1, n2, n_rep, rng):
    """n_rep pairs of independent series at once: L = np.linalg.cholesky(Sigma), then the series 1,
    mu1 + rng.standard_normal((n_rep, n1, 3)) @ L.T, then the series 2, mu2 + rng.standard_normal((n_rep, n2, 3)) @ L.T;
    returns the mean over the n_rep pairs of ‖x̄1 − x̄2‖²."""
    L = np.linalg.cholesky(np.asarray(Sigma, dtype=float))
    first = np.asarray(mu1, dtype=float) + rng.standard_normal((n_rep, n1, 3)) @ L.T
    second = np.asarray(mu2, dtype=float) + rng.standard_normal((n_rep, n2, 3)) @ L.T
    gap = first.mean(axis=1) - second.mean(axis=1)                       # (n_rep, 3)
    return float((gap ** 2).sum(axis=1).mean())


def draw_bias_25(ax, ns, means, trace):
    """In ax, in log scales on both axes: the means against n (points), and the curve 2 trace / n over the whole range of
    ns; axis labels and a legend. No other axes."""
    n_line = np.geomspace(min(ns), max(ns), 50)
    ax.plot(ns, means, "o", label="moyenne simulée de ‖x̄₁ − x̄₂‖²")
    ax.plot(n_line, 2 * trace / n_line, "-", label="2 tr Σ / n")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("taille n de chaque série")
    ax.set_ylabel("distance estimée moyenne (mm²)")
    ax.set_title("Deux séries d'une même machine", fontsize=10)
    ax.legend(fontsize=8)


rng_25 = np.random.default_rng(6425)
trace_25 = float(np.trace(SIGMA_25))
means_25 = [distance_bias_25(MU_25, MU_25, SIGMA_25, n1, n2, N_REP_25, rng_25) for n1, n2 in SIZES_25]
values_25 = [trace_25 * (1 / n1 + 1 / n2) for n1, n2 in SIZES_25]
ratios_25 = [m / v for m, v in zip(means_25, values_25)]
answer_M27_25a = [means_25, values_25, ratios_25]
answer_M27_25b = bool(all(abs(r - 1) < 0.05 for r in ratios_25))
shifted_25 = [distance_bias_25(MU_25, MU_25 + SHIFT_25, SIGMA_25, n, n, N_REP_25, rng_25) for n in (5, 80)]
answer_M27_25c = shifted_25 + [s - trace_25 * 2 / n for s, n in zip(shifted_25, (5, 80))]
answer_M27_25d = bool(shifted_25[0] > 20 * float(SHIFT_25 @ SHIFT_25))
print("a)", np.round(answer_M27_25a, 5).tolist())
print("b)", answer_M27_25b, " c)", np.round(answer_M27_25c, 5).tolist(), " d)", answer_M27_25d,
      f"(rapport {shifted_25[0] / float(SHIFT_25 @ SHIFT_25):.1f})")

''' + HINTS_25 + "\n\n\n" + CHECK_25,
    record='''def series_25r(mu1, mu2, n1, n2, rng):
    """The procedure of the statement, written again: (the mean of ‖x̄1 − x̄2‖², the mean of ‖x̄1 − x̄2‖)."""
    L = np.linalg.cholesky(np.array([[0.09, 0.03, 0.0], [0.03, 0.04, 0.01], [0.0, 0.01, 0.01]]))
    first = mu1 + rng.standard_normal((4000, n1, 3)) @ L.T
    second = mu2 + rng.standard_normal((4000, n2, 3)) @ L.T
    squares = ((first.mean(axis=1) - second.mean(axis=1)) ** 2).sum(axis=1)
    return float(squares.mean()), float(np.sqrt(squares).mean())


mu_25r, sizes_25r = np.array([80.0, 25.0, 6.0]), [(5, 5), (20, 20), (80, 80), (5, 80), (80, 5)]
rng_25r = np.random.default_rng(6425)
both_25r = [series_25r(mu_25r, mu_25r, n1, n2, rng_25r) for n1, n2 in sizes_25r]
shifted_25r = [series_25r(mu_25r, mu_25r + [0.05, 0.0, 0.0], n, n, rng_25r)[0] for n in (5, 80)]
means_25r = [m for m, _ in both_25r]
values_25r = [0.14 * (1 / n1 + 1 / n2) for n1, n2 in sizes_25r]
wbm.record("M27.25a", [means_25r, values_25r, [m / v for m, v in zip(means_25r, values_25r)]], decimals=5,
           mistakes={"le rapport est la moyenne simulée divisée par tr Σ (1/n₁ + 1/n₂)":
                         [means_25r, values_25r, [v / m for m, v in zip(means_25r, values_25r)]],
                     "la moyenne porte sur ‖x̄₁ − x̄₂‖², le carré de la norme":
                         [[r for _, r in both_25r], values_25r, [r / v for (_, r), v in zip(both_25r, values_25r)]],
                     "1/n₁ + 1/n₂ : les deux séries comptent, chacune avec sa taille":
                         [means_25r, [0.14 / n1 for n1, _ in sizes_25r], [m * n1 / 0.14 for m, (n1, _) in zip(means_25r, sizes_25r)]]})
wbm.record("M27.25b", bool(all(abs(m / v - 1) < 0.05 for m, v in zip(means_25r, values_25r))),
           mistakes={"compare chaque rapport à 1 : |rapport − 1| < 0,05": False})
wbm.record("M27.25c", shifted_25r + [s - 0.14 * 2 / n for s, n in zip(shifted_25r, (5, 80))], decimals=6,
           mistakes={"retire tr Σ (1/n₁ + 1/n₂), avec les deux tailles": shifted_25r + [s - 0.14 / n for s, n in zip(shifted_25r, (5, 80))],
                     "les deux moyennes d'abord, puis les mêmes moins le biais":
                         [s - 0.14 * 2 / n for s, n in zip(shifted_25r, (5, 80))] + shifted_25r})
wbm.record("M27.25d", bool(shifted_25r[0] > 20 * 0.0025),
           mistakes={"compare la distance estimée moyenne (5 cales par série, avec le décalage) à vingt fois ‖δ‖²": False})''',
    after=[
        ("md", "**Après la figure**, dans ta copie : pourquoi la distance estimée moyenne est-elle divisée par 4 quand $n$ "
               "est multiplié par 4 ? Pourquoi $(5, 80)$ et $(80, 5)$ donnent-ils presque la même chose ? Avec 5 cales "
               "par série, pourrais-tu voir le décalage de 0,05 mm ?"),
    ],
)

GIVEN_26 = '''GRID_C_26 = np.linspace(10, 32, 4401)                     # the translation: a room, in °C
ROOM_A_26, ROOM_B_26 = stats.norm(20, 2).cdf, stats.norm(21.2, 2).cdf
GRID_MIN_26 = np.linspace(0, 80, 16001)                   # the dilatation: a wait at a counter, in minutes
WAIT_A_26, WAIT_B_26 = stats.expon(scale=2).cdf, stats.expon(scale=5).cdf
GRID_F_26 = 1.8 * GRID_C_26 + 32                           # the same translation in °F
ROOM_A_F_26, ROOM_B_F_26 = stats.norm(68, 3.6).cdf, stats.norm(70.16, 3.6).cdf'''

CHECK_26 = '''CASES_C26 = __CASES_C26__   # for each call: (w1, ks) expected, and the abscissa of the largest gap on the grid
HIDDEN_C26 = __HIDDEN_C26__   # a call you do not see: (w1, ks) expected and the abscissa of the largest gap


def vertical_at(ax, x, low, high, tol):
    """True when a segment of ax is vertical at x (within tol) and goes from low to high (a line or ax.vlines)."""
    segments = [np.column_stack(line_points(line)) for line in ax.lines]
    for collection in ax.collections:
        if type(collection).__name__ == "LineCollection":
            segments += [np.asarray(s, dtype=float) for s in collection.get_segments()]
    for s in segments:
        if (len(s) >= 2 and np.all(np.abs(s[:, 0] - x) <= tol) and s[:, 1].min() <= low + 1e-6
                and s[:, 1].max() >= high - 1e-6):
            return True
    return False


def look_26(ax, cdf_a, cdf_b, grid, label_a, label_b, unit, x_star):
    """What is missing in a drawing of draw_cdf_gaps_26 (French phrases)."""
    missing = []
    if not (through(ax, grid, cdf_a(grid), rtol=1e-9, atol=1e-12) and through(ax, grid, cdf_b(grid), rtol=1e-9, atol=1e-12)):
        missing.append("les deux fonctions de répartition, évaluées sur grid (une courbe chacune)")
    if not any(type(c).__name__ in ("PolyCollection", "FillBetweenPolyCollection") for c in ax.collections):
        missing.append("l'aire entre elles, colorée (ax.fill_between)")
    low, high = sorted((float(cdf_a(x_star)), float(cdf_b(x_star))))
    if not vertical_at(ax, x_star, low, high, 0.51 * (grid[1] - grid[0])):
        missing.append("le segment vertical du plus grand écart, d'une courbe à l'autre")
    title = ax.get_title()
    if "ks" not in title.lower() or "w" not in title.lower() or unit not in title:
        missing.append(f"un titre avec W₁ (et son unité, {unit}) et KS")
    legend = ax.get_legend()
    texts = [t.get_text() for t in legend.get_texts()] if legend is not None else []
    if label_a not in texts or label_b not in texts:
        missing.append("une légende avec label_a et label_b")
    return missing


def returned_26(label, result, want):
    """The (w1, ks) returned compared with want: '' when right, else the reason."""
    try:
        w1, ks = (float(v) for v in result)
    except (TypeError, ValueError):
        return f"draw_cdf_gaps_26 doit rendre le couple (w1, ks), reçu {shown(result)}"
    if math.isclose(w1, want[1], abs_tol=1e-6) and math.isclose(ks, want[0], abs_tol=1e-6):
        return "tu rends (ks, w1) : rends (w1, ks), dans cet ordre"
    if not math.isclose(w1, want[0], abs_tol=1e-6):
        return f"W₁ attendu {want[0]:.6f}, reçu {w1:.6f} (l'aire entre les deux courbes, np.trapezoid sur grid)"
    if not math.isclose(ks, want[1], abs_tol=1e-6):
        return f"KS attendu {want[1]:.6f}, reçu {ks:.6f} (le plus grand |F − G| sur grid)"
    return ""


with checked("M27.26"):
    results_26 = []
    report_26 = reporter(results_26, stop=False)
    hidden_a_c26, hidden_b_c26 = stats.uniform(0, 4).cdf, stats.triang(0.5, loc=1, scale=2).cdf
    hidden_grid_c26 = np.linspace(-1, 5, 3001)
    fig_c26, ax_c26 = plt.subplots()
    try:
        result_c26 = []
        opened_c26 = drawn(lambda: result_c26.append(draw_cdf_gaps_26(ax_c26, hidden_a_c26, hidden_b_c26,
                                                                      hidden_grid_c26.copy(), "loi A", "loi B", "m")))
        missing_c26 = look_26(ax_c26, hidden_a_c26, hidden_b_c26, hidden_grid_c26, "loi A", "loi B", "m", HIDDEN_C26[2])
        why_c26 = returned_26("caché", result_c26[0], HIDDEN_C26)
    finally:
        plt.close(fig_c26)
    calls_26 = [("une translation (°C)", ROOM_A_26, ROOM_B_26, GRID_C_26, "N(20 ; 2²)", "N(21,2 ; 2²)", "°C"),
                ("une dilatation (minutes)", WAIT_A_26, WAIT_B_26, GRID_MIN_26, "moyenne 2 min", "moyenne 5 min", "min"),
                ("la translation en °F", ROOM_A_F_26, ROOM_B_F_26, GRID_F_26, "N(68 ; 3,6²)", "N(70,16 ; 3,6²)", "°F")]
    fig_26, axes_26 = plt.subplots(1, 3, figsize=(16, 4.4))
    try:
        opened_26 = list(opened_c26)
        for ax_26, (label_26, cdf_a_26, cdf_b_26, grid_26, la_26, lb_26, unit_26), case_26 in zip(axes_26, calls_26,
                                                                                                    CASES_C26):
            result_26 = []
            opened_26 += drawn(lambda: result_26.append(draw_cdf_gaps_26(ax_26, cdf_a_26, cdf_b_26, grid_26.copy(), la_26,
                                                                          lb_26, unit_26)))
            why_26 = returned_26(label_26, result_26[0], case_26)
            report_26(not why_26, f"{label_26} : (w1, ks) rendus comme attendu", f"{label_26} : {why_26}")
            missing_26 = look_26(ax_26, cdf_a_26, cdf_b_26, grid_26, la_26, lb_26, unit_26, case_26[2])
            report_26(not missing_26, f"{label_26} : les deux courbes, l'aire, le segment, le titre et la légende sont là",
                      f"{label_26} : il manque " + " ; ".join(missing_26))
        report_26(not why_c26 and not missing_c26, "un appel que tu ne vois pas (deux autres lois, une autre grille) est "
                  "juste aussi", "un appel que tu ne vois pas (deux autres lois, unité « m ») : "
                  + " ; ".join(([why_c26] if why_c26 else []) + (["il manque " + " ; ".join(missing_c26)] if missing_c26 else [])))
        report_26(not opened_26, "draw_cdf_gaps_26 dessine dans l'axe reçu",
                  "draw_cdf_gaps_26 doit dessiner dans l'axe reçu, sans ouvrir de figure")
    except BaseException:
        plt.close(fig_26)
        raise
    fig_26.tight_layout()
    plt.show()
    verdict("M27.26", all(results_26), "tes trois figures sont justes.", "relis les lignes ❌ ci-dessus.")'''

NOTE_26 = (r"a) $(1{,}200 ;\ 0{,}236)$ : $W_1$ est le décalage, et $\mathrm{KS} = 2\Phi(0{,}3) - 1 \approx 0{,}2358$, atteint au "
           r"milieu, en 20,6 °C. b) $(3{,}000 ;\ 0{,}326)$ : $W_1 = 3$ (l'écart des moyennes : les quantiles $-2\ln(1 - u)$ "
           r"et $-5\ln(1 - u)$ ne se croisent pas), et l'écart maximal est en $x = \frac{10}{3}\ln 2{,}5 \approx 3{,}05$ min. "
           r"c) $(2{,}160 ;\ 0{,}236)$.")

M27_26 = Ex(
    "M27.26", "🎨", 1, 20, "Deux fonctions de répartition sur une même figure : l'aire entre elles (W₁) et leur plus grand "
    "écart vertical (KS), pour une translation puis une dilatation",
    "dessiner deux fonctions de répartition, l'aire entre elles et leur plus grand écart, et voir ce que W₁ et KS "
    "mesurent et ce qu'un changement d'unité leur fait.", "fiche §8 et §10 ; Ex M27.8 et M27.10", tracks="C, E",
    given=GIVEN_26, note=NOTE_26,
    body=r"""Écris `draw_cdf_gaps_26(ax, cdf_a, cdf_b, grid, label_a, label_b, unit)`, qui dessine sur l'**axe reçu** (sans ouvrir de figure) les deux fonctions de répartition `cdf_a` et `cdf_b` évaluées sur `grid` (une courbe chacune, de labels `label_a` et `label_b`, avec une légende), colore l'aire entre elles (`ax.fill_between`), trace un segment vertical d'une courbe à l'autre là où leur écart $\lvert F - G\rvert$ est le plus grand sur la grille, et met en titre les deux nombres $W_1$ (l'aire entre les courbes, par la méthode des trapèzes, `np.trapezoid`), avec son unité `unit`, et KS (le plus grand écart sur la grille) ; elle rend `(w1, ks)`.

La vérification l'appelle trois fois et affiche les figures : une **translation**, la température d'un local, $\mathcal{N}(20 ;\ 2^2)$ contre $\mathcal{N}(21{,}2 ;\ 2^2)$ en °C, sur `np.linspace(10, 32, 4401)` (`ROOM_A_26`, `ROOM_B_26`, `GRID_C_26`) ; une **dilatation**, une attente à un guichet, la loi exponentielle de moyenne 2 contre celle de moyenne 5, en minutes, sur `np.linspace(0, 80, 16001)` (`WAIT_A_26`, `WAIT_B_26`, `GRID_MIN_26` ; `scipy.stats.expon(scale=2).cdf`) ; la même translation en °F, $\mathcal{N}(68 ;\ 3{,}6^2)$ contre $\mathcal{N}(70{,}16 ;\ 3{,}6^2)$, sur la grille $1{,}8 \times$ `grid` $+ 32$ (`ROOM_A_F_26`, `ROOM_B_F_26`, `GRID_F_26`) ; elle l'appelle aussi sur deux autres lois, que tu ne vois pas. Relève, avec ta fonction (appelle-la sur l'axe d'une figure que tu fermes aussitôt, `fig, ax = plt.subplots()` puis `plt.close(fig)`, pour ne pas afficher la figure deux fois) :
- a) `(w1, ks)` pour la translation (une liste de 2 nombres ; 3 décimales dans ta copie) ;
- b) `(w1, ks)` pour la dilatation (une liste de 2 nombres ; 3 décimales dans ta copie) ;
- c) `(w1, ks)` en °F (une liste de 2 nombres ; 3 décimales dans ta copie).

Ce qu'il faut observer : pour la translation, l'aire vaut le décalage, et l'écart vertical est le plus grand au milieu ; pour la dilatation, les deux courbes partent du même point et s'écartent, puis se rejoignent ; un changement d'unité multiplie $W_1$ et laisse KS intact.""",
    todo='''def draw_cdf_gaps_26(ax, cdf_a, cdf_b, grid, label_a, label_b, unit):
    """In ax: the two distribution functions on grid (labels label_a and label_b, and a legend), the area between them
    colored (ax.fill_between), a vertical segment from one curve to the other where |F − G| is largest on the grid, and a
    title with W1 (the area, np.trapezoid, with its unit) and KS (the largest gap on the grid). Returns (w1, ks). No other
    axes."""
    raise NotImplementedError("draw_cdf_gaps_26 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M27_26a = answer_M27_26b = answer_M27_26c = ...
with wbm.attempt("M27.26"):          # your function: ⏳ while it is not written
    answer_M27_26a = ...  # a) a list of 2 numbers, as computed: (w1, ks) for the translation (°C)
    answer_M27_26b = ...  # b) a list of 2 numbers, as computed: (w1, ks) for the dilatation (minutes)
    answer_M27_26c = ...  # c) a list of 2 numbers, as computed: (w1, ks) for the translation in °F''',
    check=answers_check("M27.26", "abc") + "\n\n" + CHECK_26,
    solution='''def draw_cdf_gaps_26(ax, cdf_a, cdf_b, grid, label_a, label_b, unit):
    """In ax: the two distribution functions on grid (labels label_a and label_b, and a legend), the area between them
    colored (ax.fill_between), a vertical segment from one curve to the other where |F − G| is largest on the grid, and a
    title with W1 (the area, np.trapezoid, with its unit) and KS (the largest gap on the grid). Returns (w1, ks). No other
    axes."""
    grid = np.asarray(grid, dtype=float)
    F, G = cdf_a(grid), cdf_b(grid)
    gap = np.abs(F - G)
    w1, k = float(np.trapezoid(gap, grid)), int(np.argmax(gap))
    ks = float(gap[k])
    ax.plot(grid, F, label=label_a)
    ax.plot(grid, G, label=label_b)
    ax.fill_between(grid, F, G, color="tab:orange", alpha=0.25, label="aire = W₁")
    ax.plot([grid[k], grid[k]], [F[k], G[k]], "k-", lw=2, label="plus grand écart = KS")
    ax.set_title(f"W₁ = {w1:.3f} {unit} ; KS = {ks:.3f}".replace(".", ","), fontsize=10)
    ax.set_xlabel(unit)
    ax.set_ylabel("fonction de répartition")
    ax.legend(fontsize=8)
    return w1, ks


answers_26 = []
for cdf_a_26, cdf_b_26, grid_26, unit_26 in ((ROOM_A_26, ROOM_B_26, GRID_C_26, "°C"), (WAIT_A_26, WAIT_B_26, GRID_MIN_26, "min"),
                                             (ROOM_A_F_26, ROOM_B_F_26, GRID_F_26, "°F")):
    fig_26, ax_26 = plt.subplots()
    answers_26.append(list(draw_cdf_gaps_26(ax_26, cdf_a_26, cdf_b_26, grid_26, "A", "B", unit_26)))
    plt.close(fig_26)
answer_M27_26a, answer_M27_26b, answer_M27_26c = answers_26
print("a)", np.round(answer_M27_26a, 6).tolist(), " b)", np.round(answer_M27_26b, 6).tolist(), " c)",
      np.round(answer_M27_26c, 6).tolist())

''' + CHECK_26,
    record='''def gaps_26r(cdf_a, cdf_b, grid):
    """(w1, ks) on the grid, as the statement defines them: the trapezoid area of |F − G|, its largest value."""
    gap = np.abs(cdf_a(grid) - cdf_b(grid))
    return [float(np.sum((gap[1:] + gap[:-1]) / 2 * np.diff(grid))), float(gap.max())]


grid_c_26r = np.linspace(10, 32, 4401)
cases_26r = {"a": gaps_26r(stats.norm(20, 2).cdf, stats.norm(21.2, 2).cdf, grid_c_26r),
             "b": gaps_26r(stats.expon(scale=2).cdf, stats.expon(scale=5).cdf, np.linspace(0, 80, 16001)),
             "c": gaps_26r(stats.norm(68, 3.6).cdf, stats.norm(70.16, 3.6).cdf, 1.8 * grid_c_26r + 32)}
for letter_26r, (w1_26r, ks_26r) in cases_26r.items():
    wrong_26r = {"la fonction rend (w1, ks), dans cet ordre": [ks_26r, w1_26r]}
    if letter_26r == "c":
        wrong_26r["c) se calcule en °F : les lois et la grille sont en °F, et W₁ a l'unité de la variable"] = cases_26r["a"]
    wbm.record(f"M27.26{letter_26r}", [w1_26r, ks_26r], decimals=4, mistakes=wrong_26r)''',
    after=[
        ("md", "**Après les figures**, dans ta copie : pourquoi l'écart vertical de la translation est-il le plus grand au "
               "milieu ? Pourquoi $W_1$ vaut-il exactement l'écart des moyennes pour la dilatation ? Que mesure KS que "
               "$W_1$ ne mesure pas, et inversement ?"),
    ],
)

PART_B = Part("B", "Prédire, mesurer, dessiner",
              "Fiche §4, §8, §9 et §10. La trajectoire de la descente-montée, prédite puis tracée ; le biais d'une distance "
              "estimée, simulé ; deux fonctions de répartition, l'aire entre elles et leur plus grand écart, dessinés.",
              exercises=[M27_24, M27_25, M27_26])

# ---------------------------------------------------------------------------
# Notebook exercises: debug and test (M27.27, M27.28)
# ---------------------------------------------------------------------------
GIVEN_27 = '''SHAFTS_27 = np.array([20.03, 19.98, 20.01, 19.96, 20.05])   # c): the diameters of five shafts (mm)
SLEEVES_27 = np.array([20.10, 20.04, 20.13, 20.07, 20.06])  # and of five sleeves (mm)


# The colleague's code
def penalty_kick_mix(G):
    """p*, the optimal probability of the first row of a 2 × 2 game without a saddle point."""
    (a, b), (c, d) = np.asarray(G, dtype=float).tolist()
    return (d - b) / (a - b - c + d)


def w2_settings(mu1, sd1, mu2, sd2):
    """W2 between two settings of a machine, summed up by their mean and their standard deviation."""
    return math.sqrt((mu1 - mu2) ** 2 + (sd1 ** 2 - sd2 ** 2) ** 2)


def pair_parts(shafts, sleeves):
    """partner[i], the index of the sleeve mounted on the shaft i, so that Σ (sleeve − shaft)² is smallest."""
    return np.argsort(sleeves)


# The colleague's checks: all pass
p_check_27 = penalty_kick_mix([[50, 90], [90, 60]])
print("(1) 0 ≤ p ≤ 1 :", 0 <= p_check_27 <= 1, "; les deux colonnes coûtent autant :",
      math.isclose(50 * p_check_27 + 90 * (1 - p_check_27), 90 * p_check_27 + 60 * (1 - p_check_27)), "(attendu True, True)")
print("(2)", w2_settings(0, 1, 3, 1) == 3, w2_settings(2, 0, 2, 1) == 1, "(attendu True, True)")
shafts_check_27, sleeves_check_27 = np.array([10.00, 10.02, 10.05]), np.array([10.09, 10.06, 10.11])
partner_check_27 = pair_parts(shafts_check_27, sleeves_check_27)
print("(3)", partner_check_27.tolist() == [1, 0, 2], "; jeux :",
      np.round(sleeves_check_27[partner_check_27] - shafts_check_27, 2).tolist(), "(attendu True ; [0.06, 0.07, 0.06])")'''

CHECK_27 = '''CASES_C27 = __CASES_C27__   # the cases you do not see, with what each corrected function must give

results_27, parts_27 = [], []


def report_27(ok, success, failure):
    results_27.append(bool(ok))
    print(("✅ " + success) if ok else ("❌ " + failure))


def call_27(part, name, function, *args):
    \"\"\"function(*args); an error of the learner's code becomes one ❌ line that names the function (the check of this
    part stops there, the final verdict stays).\"\"\"
    try:
        return function(*args)
    except (NotImplementedError, MymathMissingError):
        raise
    except Exception as exc:  # noqa: BLE001 - the learner's error, reported with the name of the function
        report_27(False, "", f"({part}) {name} : ton code lève {type(exc).__name__} : {str(exc)[:200]}")
        parts_27.append(part)
        raise StopCheck from None


with checked("M27.27"):                                       # (1) penalty_kick_mix_fixed
    wrong_27 = []
    for case_c27 in CASES_C27["kicks"]:
        got_c27 = call_27(1, "penalty_kick_mix_fixed", penalty_kick_mix_fixed, np.array(case_c27["G"]))
        try:
            value_c27 = float(got_c27)
        except (TypeError, ValueError):
            value_c27 = float("nan")
        if math.isclose(value_c27, case_c27["want"], rel_tol=1e-9):
            continue
        if math.isclose(value_c27, case_c27["q"], rel_tol=1e-9):
            wrong_27.append("ta fonction rend encore la probabilité qui rend le joueur des LIGNES indifférent ; p* rend "
                            "l'adversaire indifférent (ce que coûtent les deux colonnes)")
        elif math.isclose(value_c27, 1 - case_c27["want"], rel_tol=1e-9):
            wrong_27.append("p* est la probabilité de la première ligne, pas de la seconde")
        else:
            wrong_27.append(f"un jeu sans symétrie : attendu {case_c27['want']:.6f}, reçu {shown(got_c27)}")
    report_27(not wrong_27, "(1) penalty_kick_mix_fixed : trois jeux que tu ne vois pas, sans symétrie",
              "(1) penalty_kick_mix_fixed : " + " ; ".join(list(dict.fromkeys(wrong_27))[:2]))
    parts_27.append(1)

with checked("M27.27"):                                       # (2) w2_settings_fixed
    wrong_27 = []
    for case_c27 in CASES_C27["settings"]:
        got_c27 = call_27(2, "w2_settings_fixed", w2_settings_fixed, *case_c27["args"])
        try:
            value_c27 = float(got_c27)
        except (TypeError, ValueError):
            value_c27 = float("nan")
        if math.isclose(value_c27, case_c27["want"], rel_tol=1e-9):
            continue
        if math.isclose(value_c27, case_c27["variances"], rel_tol=1e-9):
            wrong_27.append("tu mets encore des variances : la formule soustrait les écarts-types")
        elif math.isclose(value_c27, case_c27["want"] ** 2, rel_tol=1e-9):
            wrong_27.append("ta fonction rend W₂², pas W₂")
        else:
            wrong_27.append(f"(moyenne, écart-type) = {case_c27['args'][:2]} et {case_c27['args'][2:]} : attendu "
                            f"{case_c27['want']:.6f}, reçu {shown(got_c27)}")
    report_27(not wrong_27, "(2) w2_settings_fixed : trois réglages que tu ne vois pas, aux écarts-types différents",
              "(2) w2_settings_fixed : " + " ; ".join(list(dict.fromkeys(wrong_27))[:2]))
    parts_27.append(2)

with checked("M27.27"):                                       # (3) pair_parts_fixed
    wrong_27 = []
    for case_c27 in CASES_C27["parts"]:
        shafts_c27, sleeves_c27 = np.array(case_c27["shafts"]), np.array(case_c27["sleeves"])
        got_c27 = call_27(3, "pair_parts_fixed", pair_parts_fixed, shafts_c27.copy(), sleeves_c27.copy())
        arr_c27 = np.asarray(got_c27)
        n_c27 = len(shafts_c27)
        if arr_c27.shape != (n_c27,) or not np.issubdtype(arr_c27.dtype, np.integer):
            wrong_27.append(f"pair_parts_fixed doit rendre un tableau NumPy d'entiers de {n_c27} indices, reçu "
                            f"{shown(got_c27)[:120]} (dtype {getattr(arr_c27, 'dtype', '?')})")
            continue
        if sorted(arr_c27.tolist()) != list(range(n_c27)):
            wrong_27.append("chaque bague est montée une fois : partner doit contenir chacun des indices 0, …, n − 1")
            continue
        total_c27 = float(((sleeves_c27[arr_c27] - shafts_c27) ** 2).sum())
        if total_c27 <= case_c27["best"] + 1e-12:
            continue
        if arr_c27.tolist() == case_c27["sleeves_only"]:
            wrong_27.append("tu ne ranges encore que les bagues : la k-ième plus petite bague va sur le k-ième plus petit "
                            "axe, quel que soit l'ordre des mesures")
        elif arr_c27.tolist() == case_c27["composed"]:
            wrong_27.append("partner[i] est la bague de l'axe i : la k-ième plus petite bague va sur l'axe de rang k "
                            "(l'indice argsort(shafts)[k]), pas sur l'axe d'indice k")
        else:
            wrong_27.append(f"{n_c27} axes dans le désordre : ta somme des carrés vaut {total_c27:.6f}, la plus petite "
                            f"{case_c27['best']:.6f}")
    report_27(not wrong_27, "(3) pair_parts_fixed : des axes dans le désordre, et des diamètres égaux",
              "(3) pair_parts_fixed : " + " ; ".join(list(dict.fromkeys(wrong_27))[:2]))
    parts_27.append(3)

if len(set(parts_27)) == 3:
    verdict("M27.27", all(results_27), "les trois fonctions corrigées passent tous les cas.", "relis les lignes ❌ ci-dessus.")'''

NOTE_27 = (r"(1) `penalty_kick_mix` calcule `(d - b) / κ`, la formule de $q^\star$ : elle rend le joueur des lignes "
           r"indifférent, au lieu de l'adversaire. Sur le jeu symétrique du collègue ($b = c = 90$), $p^\star = q^\star$ : "
           r"la vérification ne pouvait rien voir. Correction : `(d - c) / κ`. a) $\frac{5}{13} \approx 0{,}3846$ ; la version "
           r"fautive rend $\frac{7}{13} \approx 0{,}5385$. (2) `w2_settings` met les variances $\sigma^2$ là où la formule "
           r"veut les écarts-types ; les vérifications prenaient des écarts-types égaux, ou 0 et 1, pour lesquels "
           r"$\sigma^2 = \sigma$. b) $0{,}2886$ contre $0{,}2803$ pour la machine ; 3 contre 21. (3) `pair_parts` ne trie que "
           r"les bagues : juste seulement si les axes arrivent déjà triés, comme dans la vérification. Correction : "
           r"`partner = np.empty(n, dtype=int)` puis `partner[np.argsort(shafts)] = np.argsort(sleeves)`. c) "
           r"`[0, 4, 3, 1, 2]` ; 0,0277 mm² contre 0,0361 mm².")

M27_27 = Ex(
    "M27.27", "🐛", 1, 25, "Chasse à l'erreur : une stratégie d'indifférence calculée sur ses propres gains, W₂ de deux "
    "gaussiennes avec des variances, des échantillons appariés sans être triés",
    "reconnaître trois erreurs classiques sur l'indifférence, W₂ et l'appariement trié, qui passent une vérification mal "
    "choisie, puis les corriger.", "fiche §2 et §8 ; Ex M27.2, M27.14, M27.16 et M27.20", tracks="C", given=GIVEN_27,
    note=NOTE_27,
    body=r"""Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe (cellule fournie) :
1. `penalty_kick_mix(G)` doit rendre $p^\star$, la probabilité optimale de la première ligne d'un jeu $2 \times 2$ sans point selle ; elle rend `(d - b) / (a - b - c + d)`. Il l'a vérifiée sur le jeu $\begin{pmatrix} 50 & 90 \\ 90 & 60 \end{pmatrix}$ : $p$ est entre 0 et 1, et les deux colonnes coûtent alors autant au joueur des colonnes, $50p + 90(1 - p) = 90p + 60(1 - p)$. Il l'applique aux tirs au but de M27.2.
2. `w2_settings(mu1, sd1, mu2, sd2)` doit rendre $W_2$ entre deux réglages d'une machine, résumés par leur moyenne et leur écart-type ; elle rend `math.sqrt((mu1 - mu2) ** 2 + (sd1 ** 2 - sd2 ** 2) ** 2)`. Il l'a vérifiée par `w2_settings(0, 1, 3, 1) == 3` et `w2_settings(2, 0, 2, 1) == 1`.
3. `pair_parts(shafts, sleeves)` doit apparier $n$ axes et $n$ bagues, dont on a mesuré les diamètres (en mm), pour que les jeux bague − axe soient aussi réguliers que possible : elle rend un tableau d'entiers `partner`, où `partner[i]` est l'indice de la bague montée sur l'axe `i`, qui minimise $\sum_i(\text{bague} - \text{axe})^2$ (la fiche, §8, et ∂ M27.14 : trier puis apparier). Elle rend `np.argsort(sleeves)`. Il l'a vérifiée avec les axes `[10.00, 10.02, 10.05]` et les bagues `[10.09, 10.06, 10.11]` : elle rend `[1, 0, 2]`, et les jeux valent 0,06 ; 0,07 ; 0,06.

À faire : trouve et corrige chaque erreur ; les fonctions corrigées s'appellent `penalty_kick_mix_fixed`, `w2_settings_fixed` et `pair_parts_fixed`, avec les mêmes arguments (`pair_parts_fixed` rend aussi un tableau NumPy d'entiers). Puis réponds :
- a) $p^\star$ pour les tirs au but (`G_PENALTY`) par `penalty_kick_mix_fixed`, puis ce que rend `penalty_kick_mix` (une liste de 2 nombres) ;
- b) $W_2$ par `w2_settings_fixed` puis par `w2_settings`, pour la machine du 🔗 M27.16 (`SHAFTS_BEFORE`, `SHAFTS_AFTER`), puis de même pour $\mathcal{N}(100 ;\ 5^2)$ contre $\mathcal{N}(100 ;\ 2^2)$ (une liste de 4 nombres) ;
- c) pour les axes `[20.03, 19.98, 20.01, 19.96, 20.05]` et les bagues `[20.10, 20.04, 20.13, 20.07, 20.06]` (`SHAFTS_27`, `SLEEVES_27`) : ce que rend `pair_parts_fixed`, puis $\sum_i(\text{bague} - \text{axe})^2$ (mm²) pour l'appariement corrigé, puis pour celui du collègue (une liste de 7 : les 5 indices, puis les deux sommes).

Dans ta copie : pour chacune des trois erreurs, pourquoi la vérification du collègue ne la voyait pas. La vérification essaie tes corrections sur des cas que tu ne vois pas : des jeux sans symétrie, des écarts-types différents, des axes dans le désordre et des diamètres égaux.""",
    todo='''def penalty_kick_mix_fixed(G):
    """p*, the optimal probability of the first row of a 2 × 2 game without a saddle point."""
    raise NotImplementedError("penalty_kick_mix_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def w2_settings_fixed(mu1, sd1, mu2, sd2):
    """W2 between two settings of a machine, summed up by their mean and their standard deviation."""
    raise NotImplementedError("w2_settings_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def pair_parts_fixed(shafts, sleeves):
    """partner[i], the index of the sleeve mounted on the shaft i, so that Σ (sleeve − shaft)² is smallest (an array of
    integers)."""
    raise NotImplementedError("pair_parts_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M27_27a = answer_M27_27b = answer_M27_27c = ...
with wbm.attempt("M27.27"):          # your three functions: ⏳ while they are not written
    answer_M27_27a = ...  # a) a list of 2 numbers, as computed: p* for G_PENALTY by penalty_kick_mix_fixed, then what the WRONG penalty_kick_mix returns
    answer_M27_27b = ...  # b) a list of 4 numbers, as computed: the machine by w2_settings_fixed, then by the WRONG w2_settings; then N(100, 5²) against N(100, 2²), the same two ways
    answer_M27_27c = ...  # c) a list of 7: the 5 indices of pair_parts_fixed(SHAFTS_27, SLEEVES_27), then Σ (sleeve − shaft)² for your pairing, then for the colleague's''',
    check=answers_check("M27.27", "abc") + "\n\n" + CHECK_27,
    solution='''def penalty_kick_mix_fixed(G):
    """p*, the optimal probability of the first row of a 2 × 2 game without a saddle point."""
    (a, b), (c, d) = np.asarray(G, dtype=float).tolist()
    return (d - c) / (a - b - c + d)                 # p* makes the column player indifferent: the columns of G


def w2_settings_fixed(mu1, sd1, mu2, sd2):
    """W2 between two settings of a machine, summed up by their mean and their standard deviation."""
    return math.sqrt((mu1 - mu2) ** 2 + (sd1 - sd2) ** 2)          # standard deviations, not variances


def pair_parts_fixed(shafts, sleeves):
    """partner[i], the index of the sleeve mounted on the shaft i, so that Σ (sleeve − shaft)² is smallest (an array of
    integers)."""
    shafts, sleeves = np.asarray(shafts, dtype=float), np.asarray(sleeves, dtype=float)
    partner = np.empty(len(shafts), dtype=int)
    partner[np.argsort(shafts)] = np.argsort(sleeves)              # the k-th smallest sleeve on the k-th smallest shaft
    return partner


answer_M27_27a = [penalty_kick_mix_fixed(G_PENALTY), penalty_kick_mix(G_PENALTY)]
answer_M27_27b = [w2_settings_fixed(*SHAFTS_BEFORE, *SHAFTS_AFTER), w2_settings(*SHAFTS_BEFORE, *SHAFTS_AFTER),
                  w2_settings_fixed(100, 5, 100, 2), w2_settings(100, 5, 100, 2)]
partner_27 = pair_parts_fixed(SHAFTS_27, SLEEVES_27)
answer_M27_27c = (partner_27.tolist() + [float(((SLEEVES_27[partner_27] - SHAFTS_27) ** 2).sum())]
                  + [float(((SLEEVES_27[pair_parts(SHAFTS_27, SLEEVES_27)] - SHAFTS_27) ** 2).sum())])
print("a)", np.round(answer_M27_27a, 6).tolist(), " b)", np.round(answer_M27_27b, 6).tolist())
print("c)", partner_27.tolist(), np.round(answer_M27_27c[5:], 6).tolist(), "; jeux corrigés :",
      np.round(SLEEVES_27[partner_27] - SHAFTS_27, 2).tolist())

''' + CHECK_27,
    record='''from fractions import Fraction as F_27r
from itertools import permutations

(a_27r, b_27r), (c_27r, d_27r) = (55, 95), (85, 60)
p_27r, q_27r = F_27r(d_27r - c_27r, a_27r - b_27r - c_27r + d_27r), F_27r(d_27r - b_27r, a_27r - b_27r - c_27r + d_27r)
wbm.record("M27.27a", [float(p_27r), float(q_27r)], decimals=6,
           mistakes={"penalty_kick_mix_fixed rend encore la probabilité qui rend le joueur des lignes indifférent":
                         [float(q_27r), float(q_27r)],
                     "la seconde valeur est ce que rend la version FAUSSE, penalty_kick_mix": [float(p_27r), float(p_27r)],
                     "p* est la probabilité de la première ligne": [float(1 - p_27r), float(q_27r)]})
right_27r = lambda m1, s1, m2, s2: math.hypot(m1 - m2, s1 - s2)           # noqa: E731
squares_27r = lambda m1, s1, m2, s2: math.hypot(m1 - m2, s1 ** 2 - s2 ** 2)   # noqa: E731
settings_27r = [(50.30, 0.12, 50.02, 0.05), (100, 5, 100, 2)]
wbm.record("M27.27b", [f(*s) for s in settings_27r for f in (right_27r, squares_27r)], decimals=6,
           mistakes={"w2_settings_fixed met encore des variances : la formule soustrait les écarts-types":
                         [squares_27r(*s) for s in settings_27r for _ in range(2)],
                     "la deuxième et la quatrième valeurs sont celles de la version FAUSSE, w2_settings":
                         [right_27r(*s) for s in settings_27r for _ in range(2)],
                     "w2_settings_fixed doit rendre W₂, pas son carré":
                         [v for s in settings_27r for v in (right_27r(*s) ** 2, squares_27r(*s))]})
shafts_27r, sleeves_27r = [20.03, 19.98, 20.01, 19.96, 20.05], [20.10, 20.04, 20.13, 20.07, 20.06]
total_27r = lambda partner: sum((sleeves_27r[j] - x) ** 2 for x, j in zip(shafts_27r, partner))   # noqa: E731
best_27r = list(min(permutations(range(5)), key=total_27r))              # the oracle: the 120 pairings
colleague_27r = sorted(range(5), key=lambda j: sleeves_27r[j])
wbm.record("M27.27c", best_27r + [total_27r(best_27r), total_27r(colleague_27r)], decimals=6,
           mistakes={"pair_parts_fixed ne range encore que les bagues : les axes aussi arrivent dans le désordre":
                         colleague_27r + [total_27r(colleague_27r), total_27r(colleague_27r)],
                     "la somme de ton appariement d'abord, puis celle du collègue":
                         best_27r + [total_27r(colleague_27r), total_27r(best_27r)]})''',
    after=[
        ("md", "**Après la vérification**, dans ta copie : pour chaque erreur, pourquoi la vérification du collègue ne la "
               "voyait-elle pas (un jeu symétrique, des écarts-types égaux ou valant 0 et 1, des axes déjà triés), et "
               "quelle vérification l'aurait vue ?"),
    ],
)

GIVEN_28 = '''def swapped_pq(G):
    """WRONG: (q, p, v) instead of (p, q, v) (built on the reference)."""
    p, q, v = ref_distances.mixed_strategy_value_2x2(G)
    return q, p, v


def formulas_always(G):
    """WRONG: the indifference formulas even when there is a saddle point (the reference only when κ = 0)."""
    (a, b), (c, d) = np.asarray(G, dtype=float).tolist()
    kappa = a - b - c + d
    if kappa == 0:
        return ref_distances.mixed_strategy_value_2x2(G)
    return (d - c) / kappa, (d - b) / kappa, (a * d - b * c) / kappa


def maximin_as_value(G):
    """WRONG: the right strategies, but the maximin as value."""
    p, q, v = ref_distances.mixed_strategy_value_2x2(G)
    return p, q, ref_distances.pure_strategy_values(G)[0]


def rounded_value(G):
    """WRONG: the value rounded to an integer (Python's round: to the even integer on a tie, round(2.5) = 2)."""
    p, q, v = ref_distances.mixed_strategy_value_2x2(G)
    return p, q, float(round(v))'''

SOLUTION_28 = '''def game_property_test_28(n_trials, rng, solver=None, tol=1e-9):
    """n_trials random games: G = rng.integers(-9, 10, size=(2, 2)).astype(float), then c = float(rng.integers(-5, 6)),
    then k = float(rng.integers(2, 6)); solver defaults to mymath.distances.mixed_strategy_value_2x2, looked up at the
    call; the maximin and the minimax of G by G.min(axis=1).max() and G.max(axis=0).min(). Returns the numbers of trials
    "bounds", "shift", "scale", "transpose", "swap_rows" that fail (the last two only for games without a saddle point)."""
    solver = solver or mymath.distances.mixed_strategy_value_2x2     # looked up at each call: the check replaces it
    counts = {"bounds": 0, "shift": 0, "scale": 0, "transpose": 0, "swap_rows": 0}

    def off(result, expected):
        """True when one coordinate of result differs from expected by more than tol."""
        return bool(np.max(np.abs(np.asarray(result, dtype=float) - np.asarray(expected, dtype=float))) > tol)

    for _ in range(n_trials):
        G = rng.integers(-9, 10, size=(2, 2)).astype(float)
        c = float(rng.integers(-5, 6))
        k = float(rng.integers(2, 6))
        p, q, v = solver(G)
        maximin, minimax = G.min(axis=1).max(), G.max(axis=0).min()
        counts["bounds"] += int(not (maximin - tol <= v <= minimax + tol and -tol <= p <= 1 + tol and -tol <= q <= 1 + tol))
        counts["shift"] += int(off(solver(G + c), (p, q, v + c)))
        counts["scale"] += int(off(solver(k * G), (p, q, k * v)))
        if maximin < minimax:                                       # optimal strategies unique: no saddle point
            counts["transpose"] += int(off(solver(-G.T), (q, p, -v)))
            counts["swap_rows"] += int(off(solver(G[::-1]), (1 - p, q, v)))
    return counts'''

HIDDEN_STARTS_28 = (6441, 6442)
HIDDEN_TRIALS_28 = 150
COUNTERS_28 = ("bounds", "shift", "scale", "transpose", "swap_rows")
WRONG_NAMES_28 = ("swapped_pq", "formulas_always", "maximin_as_value", "rounded_value")

WRONG_C28 = """def absolute_kappa_c28(G):
    \"\"\"WRONG: without a saddle point, the value (ad − bc)/|κ| (the sign of κ lost).\"\"\"
    p, q, v = ref_distances.mixed_strategy_value_2x2(G)
    maximin, minimax, _, _ = ref_distances.pure_strategy_values(G)
    if maximin == minimax:
        return p, q, v
    (a, b), (c, d) = np.asarray(G, dtype=float).tolist()
    return p, q, (a * d - b * c) / abs(a - b - c + d)"""


def reference_counts_28() -> dict:
    """The counters of the property test on the two hidden starts, by the reference implementation: the same source
    (GIVEN_28, WRONG_C28 and SOLUTION_28) run at build time, so that the check cell holds numbers, never the test."""
    import numpy as np

    ref = load_reference_distances()
    namespace = {"np": np, "ref_distances": ref, "mymath": SimpleNamespace(distances=ref)}
    exec(GIVEN_28, namespace)
    exec(WRONG_C28, namespace)
    exec(SOLUTION_28, namespace)
    test = namespace["game_property_test_28"]
    counts = {}
    for i, seed in enumerate(HIDDEN_STARTS_28):
        counts[seed] = {"ref": test(HIDDEN_TRIALS_28, np.random.default_rng(seed))}
        for name in WRONG_NAMES_28 + (("absolute_kappa_c28",) if i == 0 else ()):
            counts[seed][name] = test(HIDDEN_TRIALS_28, np.random.default_rng(seed), solver=namespace[name])
    first = counts[HIDDEN_STARTS_28[0]]
    assert all(v == 0 for v in first["ref"].values())
    for prop in COUNTERS_28:                                     # each property is demanded by at least one wrong version
        assert any(first[name][prop] > 0 for name in WRONG_NAMES_28 + ("absolute_kappa_c28",)), prop
    return counts


def check_28(counts: dict) -> str:
    """The check cell of M27.28, with the reference counters of the hidden starts written in it."""
    literal_counts = json.dumps({str(seed): value for seed, value in counts.items()}, indent=None)
    return WRONG_C28 + r'''


with checked("M27.28"):
    results_28 = []
    report_28 = reporter(results_28, stop=False)
    COUNTERS_28 = ''' + repr(COUNTERS_28) + r'''
    EXPECTED_C28 = ''' + literal_counts + r'''   # the reference, per hidden start
    PROPERTIES_C28 = {
        "bounds": "que v est entre maximin − tol et minimax + tol, et p, q entre −tol et 1 + tol",
        "shift": "que solver(G + c) redonne (p, q, v + c) à tol près",
        "scale": "que solver(k G) redonne (p, q, k v) à tol près",
        "transpose": "que solver(−Gᵀ) redonne (q, p, −v), sans point selle",
        "swap_rows": "que solver(G[::-1]) redonne (1 − p, q, v), sans point selle",
    }

    def run_c28(label, seed, **kwargs):
        """Your game_property_test_28 on the hidden start seed (''' + str(HIDDEN_TRIALS_28) + r''' trials): its dictionary."""
        try:
            counts = game_property_test_28(''' + str(HIDDEN_TRIALS_28) + r''', np.random.default_rng(seed), **kwargs)
        except (NotImplementedError, MymathMissingError):
            raise
        except AssertionError as exc:
            print(f"❌ Ex M27.28 : game_property_test_28 ({label}) lève AssertionError ({str(exc)[:120]}) : l'erreur sort de "
                  "ta fonction ; elle doit compter les essais qui échouent et rendre le dictionnaire, sans assert.")
            raise StopCheck from None
        except Exception as exc:  # noqa: BLE001 - the learner's error
            print(f"❌ Ex M27.28 : game_property_test_28 ({label}) lève {type(exc).__name__} : {str(exc)[:200]}")
            raise StopCheck from None
        if not isinstance(counts, dict) or set(counts) != set(COUNTERS_28):
            print("❌ Ex M27.28 : game_property_test_28 doit rendre un dictionnaire de clés " + ", ".join(COUNTERS_28)
                  + f", reçu {shown(counts)[:160]}")
            raise StopCheck
        for key in COUNTERS_28:
            value = counts[key]
            if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)):
                print(f"❌ Ex M27.28 : le compteur \"{key}\" doit être un nombre entier d'essais (un entier NumPy convient), "
                      f"reçu {type(value).__name__} {value!r}")
                raise StopCheck
        return {key: int(v) for key, v in counts.items()}

    def compare_c28(label, got, want):
        """One ✅ when the five counters equal the reference's; else one ❌ per counter, naming the property."""
        wrong = [k for k in COUNTERS_28 if got[k] != want[k]]
        if not wrong:
            seen = [f"\"{k}\" {want[k]}" for k in COUNTERS_28 if want[k]]
            report_28(True, f"{label} : les cinq compteurs valent ceux de la référence"
                      + (" (" + ", ".join(seen) + ", les autres nuls)" if seen else " (0)"), "")
        for k in wrong:
            if got[k] == 0:
                why = f"ton test ne vérifie pas {PROPERTIES_C28[k]}"
            elif want[k] == 0:
                why = ("cette version ne fausse pas cette propriété : ton contrôle compte trop (sa tolérance, ce qu'il "
                       "compare, ou les jeux sur lesquels il porte)")
            else:
                why = ("un essai compte une fois s'il échoue ; les deux dernières propriétés ne portent que sur les jeux "
                       "sans point selle")
            report_28(False, "", f"{label} : \"{k}\" = {got[k]}, la référence {want[k]} : {why}")

    for seed_c28 in ''' + repr(HIDDEN_STARTS_28) + r''':
        expected_c28 = EXPECTED_C28[str(seed_c28)]
        mine_c28 = run_c28(f"départ caché {seed_c28}", seed_c28)
        wrong_c28 = [k for k in COUNTERS_28 if mine_c28[k] != expected_c28["ref"][k]]
        report_28(not wrong_c28, f"départ caché {seed_c28}, ta fonction : les cinq compteurs valent ceux de la référence (0)",
                  f"départ caché {seed_c28}, ta fonction : " + ", ".join(f"{k} = {mine_c28[k]}" for k in wrong_c28)
                  + " au lieu de 0 : vérifie l'ordre des tirages (G, puis c, puis k), tes tolérances, puis ta "
                  "mixed_strategy_value_2x2 (ses tests, M27.20)")
        for name_c28, function_c28 in (("swapped_pq", swapped_pq), ("formulas_always", formulas_always),
                                       ("maximin_as_value", maximin_as_value), ("rounded_value", rounded_value)):
            got_c28 = run_c28(f"{name_c28}, départ caché {seed_c28}", seed_c28, solver=function_c28)
            compare_c28(f"{name_c28}, départ caché {seed_c28}", got_c28, expected_c28[name_c28])

    original_c28 = mymath.distances.mixed_strategy_value_2x2
    aliases_c28 = [alias for alias, value in list(globals().items()) if value is original_c28]
    calls_c28 = [0]

    def replaced_c28(G):
        calls_c28[0] += 1
        return absolute_kappa_c28(G)

    mymath.distances.mixed_strategy_value_2x2 = replaced_c28
    for alias_c28 in aliases_c28:
        globals()[alias_c28] = replaced_c28
    try:
        patched_c28 = run_c28("une valeur calculée avec |κ|", ''' + str(HIDDEN_STARTS_28[0]) + r''')
    finally:
        mymath.distances.mixed_strategy_value_2x2 = original_c28
        for alias_c28 in aliases_c28:
            globals()[alias_c28] = original_c28
    if calls_c28[0] == 0:
        report_28(False, "", "une version fausse remplace un instant ta mixed_strategy_value_2x2, mais ton test ne l'appelle "
                  "jamais : avec solver=None, il doit prendre mymath.distances.mixed_strategy_value_2x2 au moment de "
                  "l'appel, sans en garder une copie")
    else:
        compare_c28("une valeur calculée avec |κ| à la place de ta mixed_strategy_value_2x2", patched_c28,
                    EXPECTED_C28["''' + str(HIDDEN_STARTS_28[0]) + r'''"]["absolute_kappa_c28"])
    verdict("M27.28", all(results_28), "ton test compte juste sur la référence et sur les versions fausses, et prend ta "
            "fonction au moment de l'appel.", "relis les lignes ❌ ci-dessus.")'''


NOTE_28 = (r"a) Avec des entiers, les calculs sont exacts ou presque : la détection du point selle (une comparaison exacte) "
           r"ne bascule pas quand on ajoute $c$ ou qu'on multiplie par $k$ ; avec des flottants quelconques, un jeu presque "
           r"à point selle pourrait changer de cas, et le test compterait une fausse alerte. Pour "
           r"$\begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$, la règle des plus petits indices rend $(1, 1, 2)$ pour "
           r"$\mathbf{G}$ comme pour $\mathbf{G}$ retournée, alors que la propriété attend $(0, 1, 2)$ ; sans point selle, "
           r"les stratégies optimales sont uniques. b) Vrai (260 des 400 jeux ont un point selle). c) `swapped_pq` : "
           r"`\"swap_rows\"` = 138 ; `formulas_always` : `\"bounds\"` = 222 ; `maximin_as_value` : `\"transpose\"` = 140 ; "
           r"`rounded_value` : `\"scale\"` = 98 et `\"shift\"` = 3 (un arrondi au pair) ; les autres compteurs nuls. d) "
           r"`swapped_pq` et `maximin_as_value`.")

M27_28 = Ex(
    "M27.28", "🛠️", 1, 20, "Un test de propriété : la valeur d'un jeu 2 × 2 tiré au hasard est entre maximin et minimax, "
    "et devient v + c pour G + c et k v pour k G (k > 0)",
    "écrire un test de propriété qui compte ses échecs sur des jeux tirés au hasard, voir que les propriétés du titre "
    "laissent passer des versions fausses, et en ajouter deux qui les attrapent.", "fiche §2 ; Ex M27.20", tracks="C",
    given=GIVEN_28, note=NOTE_28,
    body=r"""La cellule fournie donne quatre versions fausses de `mixed_strategy_value_2x2` : `swapped_pq` (elle rend $(q, p, v)$), `formulas_always` (les formules d'indifférence même quand il y a un point selle, sauf si $\kappa = 0$), `maximin_as_value` (les bonnes stratégies, mais le maximin comme valeur) et `rounded_value` (la valeur arrondie à l'entier).

Écris `game_property_test_28(n_trials, rng, solver=None, tol=1e-9)` ; quand `solver` vaut `None`, le test prend `mymath.distances.mixed_strategy_value_2x2` **au moment de l'appel**. Pour chacun des `n_trials` essais, dans cet ordre : `G = rng.integers(-9, 10, size=(2, 2)).astype(float)`, `c = float(rng.integers(-5, 6))`, `k = float(rng.integers(2, 6))` ; puis `p, q, v = solver(G)`, et le maximin et le minimax de `G`, calculés dans le test par `G.min(axis=1).max()` et `G.max(axis=0).min()`, sans appeler `mymath`. La fonction rend un dictionnaire de cinq compteurs d'essais (un essai compte une fois s'il échoue) :
- `"bounds"` : $v$ sort de $[\text{maximin} - \text{tol} ;\ \text{minimax} + \text{tol}]$, ou $p$ ou $q$ sort de $[-\text{tol} ;\ 1 + \text{tol}]$ ;
- `"shift"` : `solver(G + c)` s'écarte de $(p, q, v + c)$ de plus de `tol` en une coordonnée ;
- `"scale"` : `solver(k * G)` s'écarte de $(p, q, kv)$ de plus de `tol` en une coordonnée ;
- et, **seulement pour les jeux sans point selle** (maximin $<$ minimax), `"transpose"` : `solver(-G.T)` s'écarte de $(q, p, -v)$, et `"swap_rows"` : `solver(G[::-1])` s'écarte de $(1 - p, q, v)$.

Puis :
- a) Dans ta copie : pourquoi des gains entiers, et des $c$ et $k$ entiers ? Pourquoi les deux dernières propriétés seulement sans point selle (essaie $\mathbf{G} = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$) ?
- b) Avec `rng = np.random.default_rng(6428)` et 400 essais, avec ta fonction : vrai ou faux, les cinq compteurs sont nuls ;
- c) avec le même départ (un nouveau `default_rng(6428)` chaque fois, 400 essais) et chacune des quatre versions fausses, dans l'ordre `swapped_pq`, `formulas_always`, `maximin_as_value`, `rounded_value` : les cinq compteurs, dans l'ordre `"bounds"`, `"shift"`, `"scale"`, `"transpose"`, `"swap_rows"` (une liste de 4 listes de 5 entiers) ;
- d) les noms des versions fausses qui passent les trois propriétés du titre (`"bounds"`, `"shift"` et `"scale"` nuls) (une liste de noms, dans n'importe quel ordre, comme `["formulas_always"]`).

La vérification lance ton test sur deux départs que tu ne vois pas (150 essais chacun) : avec ta fonction, où ses cinq compteurs doivent valoir ceux de la référence (0), puis avec chacune des quatre versions fausses, où ils doivent valoir **exactement** ceux de la référence. Elle remplace aussi un instant `mymath.distances.mixed_strategy_value_2x2` par une version fausse (une valeur calculée avec $\lvert\kappa\rvert$) : tes compteurs doivent alors compter, comme ceux de la référence. Chacune des cinq propriétés est ainsi exigée par au moins une version fausse. Un entier NumPy convient pour un compteur ; un test qui échoue ne lève pas d'`AssertionError` : il compte. Ce qu'il faut retenir : les propriétés du titre, déjà vérifiées par `tests/test_m27_distances.py`, laissent passer des versions fausses ; l'échange des rôles et l'échange des lignes, qui ne valent que si les stratégies optimales sont uniques, les attrapent ; un test se juge aux erreurs qu'il attrape.""",
    todo='''def game_property_test_28(n_trials, rng, solver=None, tol=1e-9):
    """n_trials random games: G = rng.integers(-9, 10, size=(2, 2)).astype(float), then c = float(rng.integers(-5, 6)),
    then k = float(rng.integers(2, 6)); solver defaults to mymath.distances.mixed_strategy_value_2x2, looked up at the
    call; the maximin and the minimax of G by G.min(axis=1).max() and G.max(axis=0).min(). Returns the numbers of trials
    "bounds", "shift", "scale", "transpose", "swap_rows" that fail (the last two only for games without a saddle point)."""
    raise NotImplementedError("game_property_test_28 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M27_28b = answer_M27_28c = answer_M27_28d = ...
with wbm.attempt("M27.28"):          # your test and your library: ⏳ while they are not written
    answer_M27_28b = ...  # b) True or False: the five counters are 0 (default_rng(6428), 400 trials, your function)
    answer_M27_28c = ...  # c) a list of 4 lists of 5 integers: the counters ("bounds", "shift", "scale", "transpose", "swap_rows") for swapped_pq, formulas_always, maximin_as_value, rounded_value (a new default_rng(6428) each time, 400 trials)
    answer_M27_28d = ...  # d) a list of names (strings, any order): the wrong versions whose "bounds", "shift" and "scale" are 0''',
    check="",                                                          # filled in prepare() with the reference counters
    solution=SOLUTION_28 + '''


mine_28 = game_property_test_28(400, np.random.default_rng(6428))
wrong_28 = {name: game_property_test_28(400, np.random.default_rng(6428), solver=function)
            for name, function in (("swapped_pq", swapped_pq), ("formulas_always", formulas_always),
                                   ("maximin_as_value", maximin_as_value), ("rounded_value", rounded_value))}
COUNTERS_28 = ("bounds", "shift", "scale", "transpose", "swap_rows")
answer_M27_28b = all(mine_28[k] == 0 for k in COUNTERS_28)
answer_M27_28c = [[counts[k] for k in COUNTERS_28] for counts in wrong_28.values()]
answer_M27_28d = [name for name, counts in wrong_28.items() if counts["bounds"] == counts["shift"] == counts["scale"] == 0]
for name_28, counts_28 in {"ta fonction": mine_28, **wrong_28}.items():
    print(f"{name_28:18s}", counts_28)
print("b)", answer_M27_28b, " c)", answer_M27_28c, " d)", answer_M27_28d)
print("la bonne fonction sur [[2, 2], [2, 2]] et sur ses lignes échangées :",
      mymath.distances.mixed_strategy_value_2x2([[2, 2], [2, 2]]))
''',
    record='''def variant_28r(seed, solver, all_games=False, order="ck"):
    """The test of the statement written again on 400 trials, with two classic variants: the last two properties on every
    game (all_games), or c and k drawn in the other order (order="kc")."""
    rng, counts = np.random.default_rng(seed), dict.fromkeys(("bounds", "shift", "scale", "transpose", "swap_rows"), 0)
    for _ in range(400):
        G = rng.integers(-9, 10, size=(2, 2)).astype(float)
        if order == "ck":
            c, k = float(rng.integers(-5, 6)), float(rng.integers(2, 6))
        else:
            k, c = float(rng.integers(2, 6)), float(rng.integers(-5, 6))
        p, q, v = solver(G)
        low, high = G.min(axis=1).max(), G.max(axis=0).min()
        far = lambda got, want: bool(np.max(np.abs(np.asarray(got, dtype=float) - want)) > 1e-9)   # noqa: E731
        counts["bounds"] += int(not (low - 1e-9 <= v <= high + 1e-9 and -1e-9 <= p <= 1 + 1e-9 and -1e-9 <= q <= 1 + 1e-9))
        counts["shift"] += int(far(solver(G + c), [p, q, v + c]))
        counts["scale"] += int(far(solver(k * G), [p, q, k * v]))
        if low < high or all_games:
            counts["transpose"] += int(far(solver(-G.T), [q, p, -v]))
            counts["swap_rows"] += int(far(solver(G[::-1]), [1 - p, q, v]))
    return list(counts.values())


versions_28r = [swapped_pq, formulas_always, maximin_as_value, rounded_value]
table_28r = [variant_28r(6428, f) for f in versions_28r]
wbm.record("M27.28b", True,
           mistakes={"avec une fonction juste, aucun compteur ne compte : un compteur non nul vient de ton test (ses "
                     "tolérances, ses comparaisons) ou de ta fonction": False})
wbm.record("M27.28c", table_28r,
           mistakes={"les deux dernières propriétés ne portent que sur les jeux sans point selle":
                         [variant_28r(6428, f, all_games=True) for f in versions_28r],
                     "tire dans l'ordre de l'énoncé : G, puis c, puis k": [variant_28r(6428, f, order="kc") for f in versions_28r],
                     "ton test ne compte encore ni \\"transpose\\" ni \\"swap_rows\\" : les deux dernières propriétés, sur les "
                     "jeux sans point selle": [row[:3] + [0, 0] for row in table_28r]})
passing_28r = {name for name, row in zip(("swapped_pq", "formulas_always", "maximin_as_value", "rounded_value"), table_28r)
               if row[0] == row[1] == row[2] == 0}
missing_28r = sorted(passing_28r)
wbm.record("M27.28d", passing_28r,
           mistakes={"il en manque une : une version passe si ses trois compteurs \\"bounds\\", \\"shift\\" et \\"scale\\" sont "
                     "nuls (relis tes compteurs de c)": {missing_28r[0]},
                     "il en manque une : relis, dans c), les trois premiers compteurs de chaque version": {missing_28r[1]},
                     "rounded_value fausse \\"scale\\" (et parfois \\"shift\\") : elle ne passe pas les trois propriétés":
                         passing_28r | {"rounded_value"},
                     "formulas_always fausse \\"bounds\\" : elle ne passe pas les trois propriétés":
                         passing_28r | {"formulas_always"}})''',
    after=[
        ("todo_md", "**Dans ta copie** : a) pourquoi des gains entiers, et des $c$ et $k$ entiers ; pourquoi les deux "
                    "dernières propriétés seulement sans point selle."),
        ("md", "**Après la vérification**, dans ta copie : pourquoi `swapped_pq` et `maximin_as_value` passent-elles les "
               "trois propriétés du titre ? Quelles propriétés, prises ensemble, caractérisent la solution d'un jeu "
               "$2 \\times 2$ sans point selle ?"),
    ],
)

PART_C = Part("C", "Déboguer, tester",
              "Fiche §2 et §8. Trois erreurs classiques, qui passent une vérification mal choisie ; un test de propriété "
              "des stratégies optimales d'un jeu $2 \\times 2$. Les données et les vérifications s'appuient sur la "
              "référence (`ref_distances`), pour ne pas dépendre de ton code.",
              exercises=[M27_27, M27_28])

# ---------------------------------------------------------------------------
# Notebook exercises: the challenge (M27.29)
# ---------------------------------------------------------------------------
GIVEN_29 = '''def counter_quantile_29(u):
    """The quantile function of the wait at the counter, the exponential law of mean 2 minutes: F⁻¹(u) = −2 ln(1 − u)."""
    return -2.0 * np.log1p(-np.asarray(u, dtype=float))


VARIANCE_29 = 4.0                                          # the variance of this law (min²)'''

CHECK_29 = '''LAWS_C29 = __LAWS_C29__   # per law: the exact (mu, sigma, w2), and the standard deviation of the law

with checked("M27.29"):
    results_29 = []
    report_29 = reporter(results_29, stop=False)
    laws_29 = (("l'attente au guichet", counter_quantile_29),
               ("une loi uniforme que tu ne vois pas", lambda u: 1.0 + 3.0 * np.asarray(u, dtype=float)),
               ("une loi Gamma que tu ne vois pas", stats.gamma(2, scale=1.5).ppf))
    runs_29 = []
    for (label_29, quantile_29), law_29 in zip(laws_29, LAWS_C29):
        start_29 = time.perf_counter()
        result_29 = closest_gaussian_29(quantile_29)
        elapsed_29 = time.perf_counter() - start_29
        triple_29 = pair("M27.29", "closest_gaussian_29", result_29, names=("mu", "sigma", "w2"))
        try:
            triple_29 = tuple(float(v) for v in triple_29)
        except (TypeError, ValueError):
            verdict("M27.29", False, "", f"closest_gaussian_29 doit rendre trois nombres (mu, sigma, w2), reçu {shown(result_29)}")
            raise StopCheck from None
        runs_29.append((label_29, triple_29, elapsed_29, law_29))
    if len({run[1] for run in runs_29}) == 1:
        verdict("M27.29", False, "", "closest_gaussian_29 rend les mêmes nombres pour trois lois différentes : elle doit les "
                "calculer à partir de la fonction quantile reçue")
        raise StopCheck
    for k_29, (label_29, (mu_29, sigma_29, w2_29), elapsed_29, law_29) in enumerate(runs_29):
        (mu_e29, sigma_e29, w2_e29), sd_29 = law_29
        close_29 = [abs(got - want) < 1e-3 for got, want in ((mu_29, mu_e29), (sigma_29, sigma_e29), (w2_29, w2_e29))]
        if all(close_29):
            why_29 = ""
        elif k_29 > 0 and all(abs(a - b) < 1e-9 for a, b in zip((mu_29, sigma_29, w2_29), runs_29[0][1])):
            why_29 = "tu rends les nombres de l'attente au guichet : calcule-les à partir de la fonction quantile reçue"
        elif abs(sigma_29 - sigma_e29 ** 2) < 1e-3 * max(1.0, sigma_e29 ** 2):
            why_29 = "sigma est un écart-type, pas une variance"
        elif close_29[0] and close_29[1] and abs(w2_29 - w2_e29 ** 2) < 1e-3:
            why_29 = "w2 est la distance W₂, pas son carré"
        elif abs(sigma_29 - sd_29) < 1e-3:
            why_29 = ("ton sigma est l'écart-type de la loi : il ne minimise pas W₂ ; écris W₂²(μ, σ) et annule sa dérivée "
                      "en σ")
        elif all(abs(got - want) < 1e-2 for got, want in ((mu_29, mu_e29), (sigma_29, sigma_e29), (w2_29, w2_e29))):
            why_29 = ("à plus de 10⁻³ des valeurs exactes, mais à moins de 10⁻² : une somme sur une grille régulière de u "
                      "converge trop lentement à cause des queues (scipy.integrate.quad, ou une grille resserrée vers 0 et 1)")
        else:
            names_29 = [name for name, ok in zip(("mu", "sigma", "w2"), close_29) if not ok]
            why_29 = ", ".join(names_29) + " à plus de 10⁻³ de la valeur exacte"
            if k_29 > 0:
                why_29 += f" (attendu ≈ ({mu_e29:.4f}, {sigma_e29:.4f}, {w2_e29:.4f}), reçu ({mu_29:.4f}, {sigma_29:.4f}, {w2_29:.4f}))"
        report_29(not why_29 and elapsed_29 < 10, f"{label_29} : (mu, sigma, w2) à moins de 10⁻³ des valeurs exactes, en "
                  f"{fr(elapsed_29, 2)} s", f"{label_29} : " + (why_29 or f"trop lent ({fr(elapsed_29, 1)} s, il faut moins de "
                                                                       "10 s)"))
    verdict("M27.29", all(results_29), "critère atteint : les trois lois à 10⁻³ près, en moins de 10 secondes chacune.",
            "critère pas encore atteint : relis les lignes ❌ ci-dessus.")'''

NOTE_29 = (r"a) $(2{,}000 ;\ 1{,}806 ;\ 0{,}858)$ (plus précisément $\sigma \approx 1{,}80639$ et $W_2 \approx 0{,}85845$). b) "
           r"Vrai. c) $\frac{0{,}85845^2}{4} \approx 18{,}4$ %. La méthode la plus sûre : dans l'espace des fonctions de carré "
           r"intégrable sur $]0, 1[$, les fonctions 1 et $\Phi^{-1}$ sont orthogonales ($\int_0^1\Phi^{-1} = 0$) et "
           r"$\int_0^1(\Phi^{-1})^2 = 1$ ; la meilleure approximation de $F^{-1}$ par $\mu + \sigma\Phi^{-1}$ est sa "
           r"projection : $\mu = \int_0^1F^{-1} = \mathbb{E}[X]$, $\sigma = \int_0^1F^{-1}\Phi^{-1}$ (positif, puisque "
           r"$F^{-1}$ et $\Phi^{-1}$ croissent toutes deux), et $W_2^2 = \mathbb{V}(X) - \sigma^2$ ; trois intégrales par "
           r"`scipy.integrate.quad`. Sur 1 000 points milieux de $u$, la moyenne de $F^{-1}\Phi^{-1}$ donne $\sigma \approx "
           r"1{,}8022$, et les moindres carrés $\approx 1{,}8046$ : à $4 \times 10^{-3}$ et $1{,}8 \times 10^{-3}$, trop loin "
           r"(les queues).")

M27_29 = Ex(
    "M27.29", "🏆", 3, 30, "Défi : la gaussienne la plus proche d'une loi exponentielle au sens de W₂, et cette distance, "
    "à 10⁻³ près",
    "trouver la loi normale la plus proche d'une loi donnée par sa fonction quantile, au sens de W₂, et la distance qui "
    "reste, à 10⁻³ près.", "fiche §8 ; M02a, M02b ; Ex M27.8 et M27.22", tracks="C", given=GIVEN_29, note=NOTE_29,
    body=r"""Le temps d'attente à un guichet suit la loi exponentielle de moyenne 2 minutes : $F(x) = 1 - e^{-x/2}$ pour $x \ge 0$, de fonction quantile $F^{-1}(u) = -2\ln(1 - u)$ (`counter_quantile_29`) et de variance 4 (`VARIANCE_29`). On cherche la loi normale $\mathcal{N}(\mu, \sigma^2)$, $\sigma \ge 0$, la plus proche de cette loi au sens de $W_2$, et cette distance.

Écris `closest_gaussian_29(quantile)`, qui reçoit la fonction quantile d'une loi de moment d'ordre 2 fini (une fonction NumPy de $u \in\ ]0, 1[$, qui accepte un tableau) et rend `(mu, sigma, w2)`. Tout NumPy et SciPy sont permis (`scipy.integrate.quad`, `scipy.optimize`, `scipy.stats.norm.ppf`), mais la fonction ne reçoit que la fonction quantile : aucune formule propre à la loi exponentielle.

**Critère de réussite :** `mu`, `sigma` et `w2` à moins de $10^{-3}$ des valeurs exactes pour l'attente au guichet, et pour deux lois de la vérification que tu ne vois pas, en moins de 10 secondes par loi. La vérification refuse une fonction qui rend les mêmes nombres pour trois lois différentes, et reconnaît une variance à la place d'un écart-type, un carré à la place de $W_2$, l'écart-type de la loi à la place du meilleur $\sigma$, et une intégrale trop grossière. Relève :
- a) `(mu, sigma, w2)` pour l'attente au guichet (un tuple de 3, tel que rendu ; 3 décimales dans ta copie) ;
- b) vrai ou faux : $\mu$ est la moyenne de la loi exponentielle ;
- c) $W_2^2$ divisé par la variance de la loi exponentielle (4) : la part de la variance que la meilleure gaussienne ne peut pas rendre (un nombre, en %, tel que calculé ; 1 décimale dans ta copie).

Point de départ : $W_2^2(\mu, \sigma) = \int_0^1\big(F^{-1}(u) - \mu - \sigma\Phi^{-1}(u)\big)^2\,\mathrm{d}u$ (fiche §8) ; une somme sur une grille régulière de $u$ converge lentement, à cause des queues.""",
    todo='''def closest_gaussian_29(quantile):
    """The normal law N(mu, sigma²), sigma >= 0, closest in W2 to the law of quantile function quantile (a NumPy function
    of u in ]0, 1[ that accepts an array), and this distance: returns (mu, sigma, w2). No formula of a particular law."""
    raise NotImplementedError("closest_gaussian_29 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M27_29a = answer_M27_29b = answer_M27_29c = ...
with wbm.attempt("M27.29"):          # your function: ⏳ while it is not written
    answer_M27_29a = ...  # a) a tuple of 3, as returned: (mu, sigma, w2) for the wait at the counter
    answer_M27_29b = ...  # b) True or False: mu is the mean of the exponential law
    answer_M27_29c = ...  # c) a number, as computed: 100 W2² / 4, in %''',
    check=answers_check("M27.29", "abc") + "\n\n" + CHECK_29,
    solution='''def closest_gaussian_29(quantile):
    """The normal law N(mu, sigma²), sigma >= 0, closest in W2 to the law of quantile function quantile (a NumPy function
    of u in ]0, 1[ that accepts an array), and this distance: returns (mu, sigma, w2). No formula of a particular law."""
    f = lambda u: float(quantile(u))
    mu = integrate.quad(f, 0, 1, limit=200)[0]                                   # the projection on the constant 1
    sigma = integrate.quad(lambda u: f(u) * stats.norm.ppf(u), 0, 1, limit=200)[0]   # on Φ⁻¹ (norm 1, orthogonal to 1)
    second = integrate.quad(lambda u: f(u) ** 2, 0, 1, limit=200)[0]
    return mu, max(sigma, 0.0), math.sqrt(max(second - mu ** 2 - sigma ** 2, 0.0))   # W₂² = 𝕍(X) − σ²


start_29 = time.perf_counter()
answer_M27_29a = closest_gaussian_29(counter_quantile_29)
print(f"a) {answer_M27_29a} en {time.perf_counter() - start_29:.3f} s")
answer_M27_29b = bool(abs(answer_M27_29a[0] - 2.0) < 1e-6)
answer_M27_29c = 100 * answer_M27_29a[2] ** 2 / VARIANCE_29
midpoints_29 = (np.arange(1000) + 0.5) / 1000                                    # the coarse way, for comparison
x_29, z_29 = counter_quantile_29(midpoints_29), stats.norm.ppf(midpoints_29)
print("b)", answer_M27_29b, " c)", round(answer_M27_29c, 4))
print("   σ sur 1 000 points milieux de u : la moyenne de F⁻¹Φ⁻¹", round(float(np.mean(x_29 * z_29)), 5),
      "; les moindres carrés", round(float(np.sum((x_29 - x_29.mean()) * z_29) / np.sum(z_29 ** 2)), 5))

''' + CHECK_29,
    record='''def projection_29r(quantile):
    """The oracle: μ = ∫ F⁻¹, σ = ∫ F⁻¹ Φ⁻¹, W₂² = ∫ (F⁻¹ − μ − σΦ⁻¹)², by scipy.integrate.quad (high accuracy)."""
    f = lambda u: float(quantile(u))
    mu = integrate.quad(f, 0, 1, limit=400, epsabs=1e-13)[0]
    sigma = integrate.quad(lambda u: f(u) * stats.norm.ppf(u), 0, 1, limit=400, epsabs=1e-13)[0]
    w2sq = integrate.quad(lambda u: (f(u) - mu - sigma * stats.norm.ppf(u)) ** 2, 0, 1, limit=400, epsabs=1e-13)[0]
    return mu, sigma, math.sqrt(w2sq)


mu_29r, sigma_29r, w2_29r = projection_29r(lambda u: -2.0 * math.log1p(-u))
moment_29r = math.sqrt(4 + 4 - 2 * 2 * sigma_29r)                    # W₂ with σ = the standard deviation of the law
wbm.record("M27.29a", [mu_29r, sigma_29r, w2_29r], decimals=2,
           mistakes={"sigma est un écart-type, pas une variance": [mu_29r, sigma_29r ** 2, w2_29r],
                     "w2 est la distance W₂, pas son carré": [mu_29r, sigma_29r, w2_29r ** 2],
                     "le meilleur σ n'est pas l'écart-type de la loi : écris W₂²(μ, σ) et annule sa dérivée en σ":
                         [mu_29r, 2.0, moment_29r]})
wbm.record("M27.29b", bool(abs(mu_29r - 2.0) < 1e-9),
           mistakes={"la dérivée de W₂²(μ, σ) en μ s'annule quand ∫₀¹ (F⁻¹(u) − μ − σΦ⁻¹(u)) du = 0, et ∫₀¹ Φ⁻¹ = 0": False})
wbm.record("M27.29c", 100 * w2_29r ** 2 / 4, decimals=0,
           mistakes={"la part se lit sur W₂², une variance, pas sur W₂": 100 * w2_29r / 4,
                     "divise par la variance de la loi exponentielle, 4 (min²), pas par son écart-type": 100 * w2_29r ** 2 / 2,
                     "la part que la meilleure gaussienne ne peut pas rendre est W₂²/𝕍(X), pas 1 − W₂²/𝕍(X)":
                         100 * (1 - w2_29r ** 2 / 4)})''',
    after=[
        ("todo_md", "**Dans ta copie** : a) avec 3 décimales, et ta méthode ; pourquoi la meilleure gaussienne ne peut-elle "
                    "pas rendre toute la variance de la loi exponentielle ?"),
        ("md", "**Pour réfléchir** : pourquoi $\\sigma$ est-il plus petit que l'écart-type de la loi (2) ? Que vaudrait "
               "$W_2$ pour une loi normale ? Que devient la part de c) pour une loi uniforme ?"),
    ],
)

PART_D = Part("D", "Défi", "Fiche §8. La loi normale la plus proche d'une loi exponentielle au sens de W₂, calculée à "
              "partir de sa seule fonction quantile, et jugée sur les valeurs exactes de trois lois.", exercises=[M27_29])

PARTS = [PART_A, PART_B, PART_C, PART_D]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M27.1 à M27.10, M27.16 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            rows.append(ex.table_row(part.key if i == 0 else ""))
    if kind == "exercise":
        title = "# M27 · Jeux et distances entre lois — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). Dans "
               "les parties A à D, donne les valeurs que rend le calcul, **sans les arrondir** : les décimales "
               "demandées sont celles de ta copie. « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli : ce qui n'est pas fait affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m27_jeux_distances/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M27`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M27 · Jeux et distances entre lois — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : dominance et points selles, un jeu 2 × 2 par indifférence, "
               "des équilibres de Nash et des allumettes, la descente-montée sur $xy$, une probabilité a posteriori et "
               "trois log-loss, JS de deux lois uniformes, un plan de transport, $W_1$ et $W_2$ en dimension 1, une "
               "distance de Fréchet, une dérive, et un pont vers la convention des bibliothèques.\n"
               "- Écrire les quatre fonctions de `mymath/distances.py` (`pure_strategy_values`, "
               "`mixed_strategy_value_2x2`, `descent_ascent_iterates`, `w2_gaussians_1d`) et les tester.\n"
               "- Résoudre un transport optimal par `linprog`, prédire puis tracer une descente-montée, simuler le biais "
               "d'une distance estimée, dessiner $W_1$ et KS, corriger trois erreurs classiques, écrire un test de "
               "propriété, et relever un défi.\n\n"
               r"**Rappel express.** Maximin $\max_i\min_j g_{ij}$ $\le$ minimax $\min_j\max_i g_{ij}$, égalité si et "
               r"seulement s'il y a un point selle. Jeu $2 \times 2$ sans point selle : $\kappa = a - b - c + d$, "
               r"$p^\star = \frac{d - c}{\kappa}$, $q^\star = \frac{d - b}{\kappa}$, $v = \frac{ad - bc}{\kappa}$. "
               r"Descente-montée sur $xy$ : simultanée, valeurs propres $1 \pm i\eta$ de module $\sqrt{1 + \eta^2}$ ; "
               r"alternée, déterminant 1 et trace $2 - \eta^2$. Transport : $W_p^p = \min\sum\gamma_{ij}\lvert x_i - "
               r"y_j\rvert^p$ sur les plans de marges $\mathbf{a}$ et $\mathbf{b}$ ; sur la droite, $W_1 = \int\lvert F - "
               r"G\rvert$ et $W_p^p = \int_0^1\lvert F^{-1} - G^{-1}\rvert^p$ ; $W_2^2 = (\mu_1 - \mu_2)^2 + (\sigma_1 - "
               r"\sigma_2)^2$ pour deux gaussiennes. Biais : $\mathbb{E}\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2 "
               r"= \lVert\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2\rVert^2 + \frac{\operatorname{tr}\boldsymbol{\Sigma}_1}{n_1} "
               r"+ \frac{\operatorname{tr}\boldsymbol{\Sigma}_2}{n_2}$. Dérive : $\mathrm{KS} = \sup\lvert F - G\rvert$, sans "
               r"unité ; $W_1$ dans l'unité de la variable.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu trouver le maximin, le minimax et les points selles d'une matrice de gains, et réduire un jeu "
               "par dominance ?\n"
               "2. Sais-tu calculer les stratégies optimales et la valeur d'un jeu $2 \\times 2$, avec ou sans point "
               "selle ?\n"
               "3. Sais-tu prévoir par les valeurs propres d'un pas ce que fait la descente-montée sur un jeu bilinéaire ?\n"
               "4. Sais-tu calculer un plan de transport, $W_1$ et $W_2$ en dimension 1, et $W_2$ de deux gaussiennes ?\n"
               "5. Sais-tu dire pourquoi une distance estimée sur des échantillons est biaisée, et ce que mesurent KS et "
               "$W_1$ ?\n\n"
               "**La suite** : M28, sur la matrice de Gram, la montée sur l'entrée et les lois tronquées, puis le "
               "chapitre 27 de workbookIA, qui applique ces outils aux réseaux génératifs adverses.")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter=CHAPTER) if kind == "exercise" else setup_cell(kind))
    cells += objectives_cell()
    cells += paper_part(kind)
    for part in PARTS:
        cells += part_cells(part, kind)
    cells += footer_cells(kind)
    return cells


# ---------------------------------------------------------------------------
# Build-time literals: the expected values of the checks, computed here (reference implementation, NumPy, SciPy and
# private functions of this script), so that no check cell holds the code that solves an exercise
# ---------------------------------------------------------------------------
def load_reference_distances():
    """solutions/mymath_ref/distances.py, loaded as a module of its own."""
    spec = importlib.util.spec_from_file_location("distances_ref_m27", ROOT / "solutions" / "mymath_ref" / "distances.py")
    ref = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ref)
    return ref


def literal(value) -> str:
    """A Python literal of value (floats by repr: exact), wrapped for reading."""
    return pprint.pformat(value, width=112, compact=True, sort_dicts=False)


def _northwest(np, a, b):
    """The north-west corner plan (the row first when the row and the column empty together)."""
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    plan = np.zeros((len(a), len(b)))
    i = j = 0
    while i < len(a) and j < len(b):
        row_first = a[i] <= b[j]
        plan[i, j] = min(a[i], b[j])
        a[i], b[j] = a[i] - plan[i, j], b[j] - plan[i, j]
        i, j = (i + 1, j) if row_first else (i, j + 1)
    return plan


def _bias_25(np, mu1, mu2, Sigma, n1, n2, n_rep, rng, variant=""):
    """The procedure of M27.25 (variant: "second_first", "no_cholesky", "norm"): the mean of ‖x̄1 − x̄2‖² (or ‖·‖)."""
    L = np.asarray(Sigma, dtype=float) if variant == "no_cholesky" else np.linalg.cholesky(np.asarray(Sigma, dtype=float))
    if variant == "second_first":
        second = np.asarray(mu2) + rng.standard_normal((n_rep, n2, 3)) @ L.T
        first = np.asarray(mu1) + rng.standard_normal((n_rep, n1, 3)) @ L.T
    else:
        first = np.asarray(mu1) + rng.standard_normal((n_rep, n1, 3)) @ L.T
        second = np.asarray(mu2) + rng.standard_normal((n_rep, n2, 3)) @ L.T
    squares = ((first.mean(axis=1) - second.mean(axis=1)) ** 2).sum(axis=1)
    return float(np.sqrt(squares).mean() if variant == "norm" else squares.mean())


def _gaps_26(np, cdf_a, cdf_b, grid):
    """(w1, ks, x*) on a grid: the trapezoid area of |F − G|, its largest value and where."""
    gap = np.abs(cdf_a(grid) - cdf_b(grid))
    return [float(np.trapezoid(gap, grid)), float(gap.max()), float(grid[int(np.argmax(gap))])]


def build_constants() -> dict:
    """The literals written in the check cells, by placeholder."""
    import numpy as np
    from scipy import integrate, optimize, stats

    ref = load_reference_distances()
    out = {}

    # M27.21: two classic wrong deviations of the kept quantity (simultaneous steps; the + sign of the cross term)
    def deviations(A, x0, y0, eta, n, kept_sign=-1.0):
        A = np.asarray(A, dtype=float)
        result = []
        for alternating, sign in ((False, -1.0), (True, 1.0)):
            xs, ys = ref.descent_ascent_iterates(A, x0, y0, eta, n, alternating=alternating)
            Q = (xs ** 2).sum(axis=1) + (ys ** 2).sum(axis=1) + sign * eta * np.einsum("ki,ij,kj->k", xs, A, ys)
            result.append(float(np.abs(Q - Q[0]).max()))
        return result

    sim_b, plus_b = deviations([[1.0]], [1.0], [0.0], 0.6, 200)
    sim_c, plus_c = deviations([[1.0, -2.0, 0.0], [0.5, 1.0, -1.0]], [1.0, 0.0], [0.0, 1.0, 0.0], 0.3, 100)
    simultaneous = "c'est l'écart des itérés simultanés : la quantité n'est constante que pour le pas alterné (alternating=True)"
    sign = "Q = ‖x‖² + ‖y‖² − η xᵀAy : le signe du terme croisé compte"
    out["__WRONG_C21B__"] = literal([(simultaneous, sim_b), (sign, plus_b)])
    out["__WRONG_C21C__"] = literal([(simultaneous, sim_c), (sign, plus_c)])

    # M27.23: hidden masses for the north-west rule, and a hidden cost matrix for the linear program
    nw_cases = []
    for a, b in (([3.0, 5.0, 2.0, 6.0], [4.0, 4.0, 8.0]), ([7.0, 1.0, 4.0], [5.0, 2.0, 5.0])):
        nw_cases.append({"a": a, "b": b, "want": _northwest(np, a, b).tolist()})
    out["__NW_C23__"] = literal(nw_cases)
    C = np.round(np.random.default_rng(6423).uniform(0, 10, size=(3, 4)), 1)
    a, b = np.array([0.15, 0.6, 0.25]), np.array([0.35, 0.1, 0.3, 0.25])
    m, n = C.shape
    margins = np.vstack([np.kron(np.eye(m), np.ones(n)), np.kron(np.ones(m), np.eye(n))])
    lp = optimize.linprog(C.ravel(), A_eq=margins, b_eq=np.concatenate([a, b]), bounds=(0, None), method="highs")
    out["__LP_C23__"] = literal({"C": C.tolist(), "a": a.tolist(), "b": b.tolist(), "optimum": float(lp.fun)})

    # M27.24: the iterates of the four calls of the check
    paths = {}
    for key, (eta, steps, alternating) in {"0.3-s": (0.3, 40, False), "0.3-a": (0.3, 40, True),
                                           "2.5-a": (2.5, 40, True), "hidden": (0.45, 12, True)}.items():
        xs, ys = ref.descent_ascent_iterates([[1.0]], [1.0], [0.0], eta, steps, alternating=alternating)
        paths[key] = [xs[:, 0].tolist(), ys[:, 0].tolist()]
    out["__PATHS_C24__"] = literal(paths)

    # M27.25: the means of a) for the equal sizes, rounded to 4 decimals (the figure), and a hidden case
    namespace = {"np": np}
    exec(GIVEN_25, namespace)
    rng = np.random.default_rng(6425)
    means = [_bias_25(np, namespace["MU_25"], namespace["MU_25"], namespace["SIGMA_25"], n1, n2, namespace["N_REP_25"], rng)
             for n1, n2 in namespace["SIZES_25"]]
    out["__MEANS_C25__"] = literal([round(x, 4) for x in means[:3]])
    hidden = {"mu1": [1.0, 2.0, 3.0], "mu2": [1.1, 2.0, 2.9], "Sigma": [[0.5, 0.1, 0.0], [0.1, 0.3, 0.0], [0.0, 0.0, 0.2]],
              "n1": 7, "n2": 3, "n_rep": 500, "seed": 6426}
    args = [np.array(hidden[k]) for k in ("mu1", "mu2", "Sigma")] + [hidden["n1"], hidden["n2"], hidden["n_rep"]]
    for variant, key in (("", "want"), ("second_first", "second_first"), ("no_cholesky", "no_cholesky"), ("norm", "norm")):
        hidden[key] = _bias_25(np, *args, np.random.default_rng(hidden["seed"]), variant=variant)
    out["__HIDDEN_C25__"] = literal(hidden)

    # M27.26: (w1, ks, x*) of the three calls, and of a hidden call (U[0, 4] against a triangular law on [1, 3])
    namespace = {"np": np, "stats": stats}
    exec(GIVEN_26, namespace)
    ns = namespace
    out["__CASES_C26__"] = literal([_gaps_26(np, ns["ROOM_A_26"], ns["ROOM_B_26"], ns["GRID_C_26"]),
                                    _gaps_26(np, ns["WAIT_A_26"], ns["WAIT_B_26"], ns["GRID_MIN_26"]),
                                    _gaps_26(np, ns["ROOM_A_F_26"], ns["ROOM_B_F_26"], ns["GRID_F_26"])])
    out["__HIDDEN_C26__"] = literal(_gaps_26(np, stats.uniform(0, 4).cdf, stats.triang(0.5, loc=1, scale=2).cdf,
                                             np.linspace(-1, 5, 3001)))

    # M27.27: hidden cases of the three corrected functions
    kicks = []
    for G in ([[2.0, 7.0], [6.0, 3.0]], [[9.0, 0.0], [2.0, 5.0]], [[-4.0, 5.0], [3.0, -1.0]]):
        (ga, gb), (gc, gd) = G
        kappa = ga - gb - gc + gd
        assert ref.pure_strategy_values(G)[0] < ref.pure_strategy_values(G)[1]      # no saddle point
        kicks.append({"G": G, "want": (gd - gc) / kappa, "q": (gd - gb) / kappa})
    settings = []
    for args in ((5.0, 0.3, 5.4, 0.8), (-2.0, 4.0, 1.0, 1.5), (0.0, 0.5, 0.0, 2.5)):
        m1, s1, m2, s2 = args
        settings.append({"args": list(args), "want": math.hypot(m1 - m2, s1 - s2),
                         "variances": math.hypot(m1 - m2, s1 ** 2 - s2 ** 2)})
    parts = []
    rng = np.random.default_rng(6427)
    for size in (6, 7):
        while True:
            shafts = np.round(30 + rng.normal(0, 0.03, size), 2)
            sleeves = np.round(30.08 + rng.normal(0, 0.03, size), 2)
            order = np.argsort(shafts)
            right = np.empty(size, dtype=int)
            right[order] = np.argsort(sleeves)
            composed = np.argsort(sleeves)[order]
            if (len(set(shafts)) == size and len(set(sleeves)) == size and not np.array_equal(composed, right)
                    and not np.array_equal(np.argsort(sleeves), right)):
                break
        parts.append({"shafts": shafts.tolist(), "sleeves": sleeves.tolist(),
                      "best": float(((sleeves[right] - shafts) ** 2).sum()),
                      "sleeves_only": np.argsort(sleeves).tolist(), "composed": composed.tolist()})
    tie_shafts, tie_sleeves = np.array([5.00, 5.00, 4.98, 5.02]), np.array([5.06, 5.05, 5.06, 5.04])
    import itertools
    best_tie = min(float(((tie_sleeves[list(p)] - tie_shafts) ** 2).sum()) for p in itertools.permutations(range(4)))
    parts.append({"shafts": tie_shafts.tolist(), "sleeves": tie_sleeves.tolist(), "best": best_tie,
                  "sleeves_only": np.argsort(tie_sleeves).tolist(), "composed": np.argsort(tie_sleeves)[np.argsort(tie_shafts)].tolist()})
    out["__CASES_C27__"] = literal({"kicks": kicks, "settings": settings, "parts": parts})

    # M27.29: the exact (mu, sigma, w2) of the three laws, and their standard deviations
    def projection(quantile):
        f = lambda u: float(quantile(u))                                       # noqa: E731
        mu = integrate.quad(f, 0, 1, limit=400, epsabs=1e-13)[0]
        sigma = integrate.quad(lambda u: f(u) * stats.norm.ppf(u), 0, 1, limit=400, epsabs=1e-13)[0]
        w2sq = integrate.quad(lambda u: (f(u) - mu - sigma * stats.norm.ppf(u)) ** 2, 0, 1, limit=400, epsabs=1e-13)[0]
        return [mu, sigma, math.sqrt(w2sq)]

    laws = [(projection(lambda u: -2.0 * math.log1p(-u)), 2.0),
            (projection(lambda u: 1.0 + 3.0 * u), 3.0 / math.sqrt(12)),
            (projection(stats.gamma(2, scale=1.5).ppf), 1.5 * math.sqrt(2))]
    out["__LAWS_C29__"] = literal(laws)
    return out


PREPARED = []


def prepare() -> dict:
    """Write the build-time literals in every cell text (placeholders __NAME__), and the check of M27.28 with its
    reference counters. Idempotent; returns the counters of M27.28."""
    if PREPARED:
        return PREPARED[0]
    constants = build_constants()

    def fill(text):
        for key, value in constants.items():
            text = text.replace(key, value)
        return text

    for part in PARTS:
        part.given = fill(part.given)
        for ex in part.exercises:
            for field_name in ("body", "todo", "check", "solution", "record", "given", "note"):
                setattr(ex, field_name, fill(getattr(ex, field_name)))
            ex.after = [(kind, fill(text)) for kind, text in ex.after]
    counts = reference_counts_28()
    M27_28.check = answers_check("M27.28", "bcd") + "\n\n" + check_28(counts)
    M27_28.solution = M27_28.solution.rstrip("\n") + "\n\n\n" + check_28(counts)
    left = {match for part in PARTS for ex in part.exercises
            for text in (ex.body, ex.todo, ex.check, ex.solution, ex.record, ex.given, *(t for _, t in ex.after))
            for match in re.findall(r"__[A-Z][A-Z0-9_]*__", text)}
    assert not left, f"placeholders left: {sorted(left)}"
    PREPARED.append(counts)
    return counts


def main() -> int:
    counts = prepare()
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
    first = counts[HIDDEN_STARTS_28[0]]
    print(f"✅ {FOLDER}/03_notebook.ipynb and 05_solutions.ipynb written ({len(PAPER)} paper exercises, "
          f"{n_checks} paper checks, {n_ex} notebook exercises); reference counters of M27.28 on {HIDDEN_STARTS_28[0]}: "
          + "; ".join(f"{name} {first[name]}" for name in WRONG_NAMES_28 + ("absolute_kappa_c28",)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
