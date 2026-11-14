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
         '''mistakes={"une colonne est strictement dominée si elle coûte plus qu'une autre sur toutes les lignes de G, y "
                     "compris celles qu'on n'a pas encore rayées": True}'''),
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
         '''mistakes={"la distance est multipliée par √(1 + η²) à chaque pas, pas par 1 + η²":
                         math.ceil(math.log(2) / math.log(1 + ETA_4 ** 2)),
                     "il faut au moins doubler : arrondis à l'entier supérieur":
                         math.floor(math.log(2) / math.log(math.sqrt(1 + ETA_4 ** 2)))}'''),
        ("d", "a number (1 decimal)", "math.degrees(math.acos((2 - ETA_4 ** 2) / 2))",
         '''decimals=1,
           mistakes={"pour le pas alterné, cos θ = tr(M_a)/2 : ce n'est pas l'angle du pas simultané":
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
           mistakes={"avec des masses en tonnes, le couplage indépendant est γᵢⱼ = aᵢbⱼ divisé par la masse totale":
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
        ("d", "a number", "sum(x ** 2 for x in MU2_9)",
         '''decimals=6,
           mistakes={"la part des moyennes est ‖Δμ‖², la somme des carrés des coordonnées de Δμ": sum(abs(x) for x in MU2_9),
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
                     "JS compare chaque loi au mélange m = (p + q)/2, pas à l'autre loi":
                         (kl(P_10, Q_10) + kl(Q_10, P_10)) / 2}'''),
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
        ("f", "a list of 2 numbers (3 decimals)",
         "[w1_samples(fahrenheit(JAN_10), fahrenheit(FEB_10)), ks_samples(fahrenheit(JAN_10), fahrenheit(FEB_10))]",
         '''decimals=3,
           mistakes={"une translation commune des deux échantillons ne change pas la distance entre eux":
                         [w1_samples(fahrenheit(JAN_10), fahrenheit(FEB_10)) + 32, ks_samples(JAN_10, FEB_10)],
                     "KS compare des probabilités cumulées : regarde ce qu'un changement d'unité fait à l'ordre des "
                     "valeurs": [w1_samples(fahrenheit(JAN_10), fahrenheit(FEB_10)), 1.8 * ks_samples(JAN_10, FEB_10)]}'''),
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


def fahrenheit(x):
    return [1.8 * v + 32 for v in x]


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
                         pure_19r(market_19r)[:3] + [3]})
wbm.record("M27.19b", pure_19r(seen_by_B_19r), decimals=6,
           mistakes={"B maximise ce que A perd : ses gains sont −G, pas G": pure_19r([list(col) for col in zip(*market_19r)]),
                     "les lignes de -G.T sont les stratégies de B : transpose aussi −G": pure_19r([[-g for g in row] for row in market_19r])})
wbm.record("M27.19c", pure_19r(penalty_19r) + [False], decimals=6,
           mistakes={"(row, col) n'est un point selle que si le maximin égale le minimax": pure_19r(penalty_19r) + [True]})'''),
    ],
)

NOTE_20 = (r"La forme, puis `pure_strategy_values` ; si `maximin == minimax`, les stratégies pures ; sinon "
           r"`(a, b), (c, d) = G.tolist()` et les trois formules. a) $\big(\frac{5}{13}, \frac{7}{13}, \frac{955}{13}\big) "
           r"\approx (0{,}3846 ;\ 0{,}5385 ;\ 73{,}4615)$. b) Les formules donneraient $p = -1$ et $q = 3$ ; la fonction "
           r"rend `(1.0, 1.0, 3.0)`, le point selle (0, 0). c) $73{,}4615$ et $73{,}4615$.")

M27_20 = Ex(
    "M27.20", "🔨", 2, 20, "Les stratégies optimales et la valeur d'un jeu 2 × 2, avec ou sans point selle · "
    "`mixed_strategy_value_2x2`",
    "programmer les stratégies optimales d'un jeu 2 × 2, pures s'il y a un point selle, d'indifférence sinon, et voir "
    "que p* et q* garantissent la même valeur.", "fiche §2 ; Ex M27.2 et M27.19", tracks="C, E", mymath="distances.py",
    note=NOTE_20,
    body=REMINDER + r"""

Écris `mixed_strategy_value_2x2(G)` (fiche §2), en suivant sa docstring : contrôle la forme $(2, 2)$, puis appelle ta `pure_strategy_values` ; s'il y a un point selle (`maximin == minimax`, une comparaison exacte), rends les stratégies pures, `p = 1.0` si `row == 0` et `0.0` sinon, de même pour `q` avec `col`, et `value = maximin` ; sinon, rends les trois formules d'indifférence de la fiche, $p^\star = \frac{d - c}{\kappa}$, $q^\star = \frac{d - b}{\kappa}$, $v = \frac{ad - bc}{\kappa}$, en `float` Python.

**L'usage.** Avec ta fonction :
- a) les tirs au but de M27.2 (`G_PENALTY`) (un tuple de 3, tel que rendu), à comparer à tes réponses a) à c) ;
- b) pour $\mathbf{G} = \begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$ : ce que donneraient les formules de $p^\star$ et de $q^\star$, puis ce que rend ta fonction (une liste de 5 nombres : $p$ et $q$ par les formules, puis les trois nombres rendus) ;
- c) pour les tirs au but, le plus petit gain espéré de $p^\star$ contre les deux plongeons, $\min_j(\mathbf{p}^{\star\top}\mathbf{G})_j$, puis le plus grand de $q^\star$ contre les deux tirs, $\max_i(\mathbf{G}\mathbf{q}^\star)_i$, avec $\mathbf{p}^\star = (p^\star, 1 - p^\star)$ et $\mathbf{q}^\star = (q^\star, 1 - q^\star)$ (une liste de 2 nombres).

Ce qu'il faut observer : avec un point selle, les formules d'indifférence sortent de $[0, 1]$ ; sans point selle, $p^\star$ et $q^\star$ garantissent la même valeur, chacun de son côté.""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_mixed_strategy_value_2x2_") + [
        ("md", "**L'usage** : les tirs au but, un jeu à point selle, et les deux garanties."),
        ("todo", '''G_SADDLE_20 = np.array([[3.0, 5.0], [1.0, 2.0]])
answer_M27_20a = answer_M27_20b = answer_M27_20c = ...
with wbm.attempt("M27.20"):          # if you call mixed_strategy_value_2x2 here: ⏳ while it is not written
    answer_M27_20a = ...  # a) a tuple of 3, as returned: (p, q, value) for G_PENALTY
    answer_M27_20b = ...  # b) a list of 5 numbers: p and q by the indifference formulas for G_SADDLE_20, then the 3 numbers your function returns
    answer_M27_20c = ...  # c) a list of 2 numbers, as computed: min_j (p*ᵀ G)_j, then max_i (G q*)_i, for G_PENALTY'''),
        ("check", answers_check("M27.20", "abc")),
        ("solution", '''G_SADDLE_20 = np.array([[3.0, 5.0], [1.0, 2.0]])
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
formulas_20r = [float(F_20r(2 - 1, 3 - 5 - 1 + 2)), float(F_20r(2 - 5, 3 - 5 - 1 + 2))]
saddle_20r = strategies_20r([[3, 5], [1, 2]])
wbm.record("M27.20b", formulas_20r + saddle_20r, decimals=6,
           mistakes={"avec un point selle, ta fonction rend les stratégies pures de pure_strategy_values, pas les formules":
                         formulas_20r + formulas_20r + [float(F_20r(3 * 2 - 5 * 1, 3 - 5 - 1 + 2))],
                     "p* = (d − c)/κ et q* = (d − b)/κ, avec κ = a − b − c + d": formulas_20r[::-1] + saddle_20r})
G_20r = np.array([[55.0, 95.0], [85.0, 60.0]])
wbm.record("M27.20c", [float((np.array([p_20r, 1 - p_20r]) @ G_20r).min()), float((G_20r @ np.array([q_20r, 1 - q_20r])).max())],
           decimals=6,
           mistakes={"p* pondère les lignes de G (pᵀG), q* ses colonnes (G q)":
                         [float((np.array([q_20r, 1 - q_20r]) @ G_20r).min()), float((G_20r @ np.array([p_20r, 1 - p_20r])).max())]})'''),
    ],
)
