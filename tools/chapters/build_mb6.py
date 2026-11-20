#!/usr/bin/env python
"""Build the two notebooks of chapter MB6 from a single source (used by Claude).

    python tools/chapters/build_mb6.py
    python tools/run_all_notebooks.py chapitres/mb6_shapley_equite/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/mb6_shapley_equite/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ MB6.1 to MB6.7, 🔗 MB6.11), each answer computed in the notebook from the data of
its statement (the n! orders of itertools.permutations for the pivots and the Shapley values, exact fractions for the
indices, the dividends, the shares, the rates and the weights, SymPy for the line integrals and the models of the
plot, NumPy for the grid, math for the laboratories), each wrong value computed by the error its message names; parts
A to D are the notebook exercises (MB6.13 to MB6.22), exactly as 02_exercices.md describes them. Wrong-answer messages
state a rule, never a number of the answer, the last step that gives it, nor another sub-question; none is an error of
the corrected versions of the frontier exercises of workbookIA B6 (uniform weights of the coalitions, a single marginal
contribution, the factor of the displacement forgotten, points counted for intervals, a path started from 0 instead of
the reference, the sum of a gradient instead of its mean, the other alignment convention, Pearson's correlation of the
raw values, a rate divided by the whole group, FP and FN swapped, FPR and FNR confused, the reweighting inverted).

Data. The notebook exercises take the data of the paper exercises (a data cell of part A, read only), the data of their
own statements (the stand of 🔨 MB6.14, the minerals of 🔨 MB6.16, the triangle of 🔮 MB6.17, the landscape of 🎨 MB6.19,
the samples of 🐛 MB6.20, the council of 🏆 MB6.22, all written as literals) and their own draws (the reservoir of
🔬 MB6.18, seed 7918; the polylines of the corrected version of 🛠️ MB6.21, seed 7921). Seeds 7901 to 7949 only (the
tests use 7800 to 7890, the figures 7891 to 7899): 7918, 7921; 7940 to 7949 serve only the calibration of the challenge
(scratchpad). Never a product of two first-degree factors shared with a reference, never a background, a feature, a
model trained, a pixel or a network, never the number of steps of a rule, never the parameter α of a path (t only).
The check cells never hold the code that solves an exercise nor a value that gives an answer without a calculation: the
expected values are recorded by the solutions as hidden sub-IDs and compared with ``wbm.check(..., computed=True)``
(the fields of 🔨 MB6.15 at hidden points, the hidden cases of 🐛 MB6.20, the peaks of 🎨 MB6.19), computed at check time
by the reference ``mymath_ref.attribution`` (the cumulative integrals of 🎨 MB6.19, along the beginning of each path), or
given by properties (the hidden methods of 🛠️ MB6.21). The hidden part of 🏆 MB6.22 lives in
``solutions/challenges/mb6_22.py``: the check cell runs it in another process, which draws the hidden councils at each
run, sends them, and measures the indices it receives only at the end, so that no exact index of a hidden council
lives in the notebook's process. The check cells use their own data, never the test cases of
tests/test_mb6_attribution.py, the examples of the docstrings of the stub attribution, the examples of the fiche, nor
the numbers of workbookIA B6 to B1 (the notes of MB6 in the syllabus and their list « Évités »).
"""

from __future__ import annotations

import importlib.util
import math
import pprint
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (ROOT, STARS, Ex, Paper, Part, badge, check_unique_keys, guarded,  # noqa: E402,F401
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "MB6"
FOLDER = "chapitres/mb6_shapley_equite"


def syllabus_entry(ex_id: str) -> tuple:
    """(type, stars, minutes, title, tracks) of an exercise, read in the contract (docs/syllabus/data/partie_7.py)."""
    sys.path.insert(0, str(ROOT / "docs" / "syllabus" / "data"))
    import partie_7
    for value in vars(partie_7).values():
        if isinstance(value, list) and value and isinstance(value[0], dict) and "id" in value[0]:
            for chapter in value:
                if chapter["id"] == CHAPTER:
                    for row in chapter["exercises"]:
                        if row[0] == ex_id:
                            flags = row[6].split()
                            return row[1], row[2], row[3], row[4], "C, E" if "E" in flags else "C"
    raise KeyError(ex_id)


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("MB6.1", "Un conseil de quatre membres à vote pondéré : l'indice de Shapley-Shubik par les 24 ordres, un membre "
                   "nul, deux membres de poids différents et de même pouvoir, et le nombre d'ordres tirés au hasard qui "
                   "suffit (Hoeffding)", [
        ("a", "a list of 4 integers: the number of orders in which A, B, C, D is pivot", "pivots_1(QUOTA_1, VOTES_1)",
         '''mistakes={"une motion passe dès que ses voix atteignent le quota (au moins q), pas seulement quand elles le "
                     "dépassent": pivots_1(QUOTA_1 + 1, VOTES_1),
                     "le pivot est le membre dont l'arrivée fait passer la coalition de perdante à gagnante, pas le "
                     "dernier arrivé": last_1(VOTES_1)}'''),
        ("b", "a list of 4 numbers (4 decimals): the indices of A, B, C, D",
         "floats([F(c, math.factorial(len(VOTES_1))) for c in pivots_1(QUOTA_1, VOTES_1)])",
         '''decimals=4,
           mistakes={"le pouvoir d'un membre n'est pas sa part des voix : compte les ordres où il est pivot":
                         floats([F(w, sum(VOTES_1)) for w in VOTES_1]),
                     "être dans une coalition gagnante ne suffit pas : compte les ordres où le membre fait basculer le "
                     "vote": floats(memberships_1(QUOTA_1, VOTES_1))}'''),
        ("c", "a list of 4 integers: the pivots when D has 2 votes", "pivots_1(QUOTA_1, VOTES_1C)",
         '''mistakes={"une motion passe dès que ses voix atteignent le quota (au moins q), pas seulement quand elles le "
                     "dépassent": pivots_1(QUOTA_1 + 1, VOTES_1C),
                     "le pivot est le membre dont l'arrivée fait passer la coalition de perdante à gagnante, pas le "
                     "dernier arrivé": last_1(VOTES_1C)}'''),
        ("d", "an integer: the smallest number of orders m", "hoeffding_1()",
         '''mistakes={"la borne de Hoeffding porte sur les deux côtés de l'écart : 2 e^{−2mε²} ≤ δ":
                         hoeffding_1(two_sided=False),
                     "m est le plus petit entier qui satisfait la borne : arrondis vers le haut": hoeffding_1() - 1,
                     "l'exposant de Hoeffding contient ε², pas ε": hoeffding_1(squared=False)},
           fractional="m est un nombre d'ordres : le plus petit entier qui satisfait la borne, donc arrondi vers le haut"'''),
    ]),

    Paper("MB6.2", "Trois hameaux partagent une conduite d'eau : la valeur de Shapley par les ordres, les dividendes de "
                   "Harsanyi, le partage tronçon par tronçon, et les quatre axiomes vérifiés", [
        ("a", "a list of 3 numbers (1 decimal): the shares of H1, H2, H3", "floats(shapley_0(cost_2, 3))",
         '''decimals=1,
           mistakes={"la valeur de Shapley n'est pas un partage au prorata des besoins : moyenne les coûts marginaux sur "
                     "les six ordres": floats([F(needs_2()[-1] * b, sum(needs_2())) for b in needs_2()]),
                     "un tronçon se partage entre les hameaux qu'il dessert : celui qui est à son bout et ceux qui sont plus "
                     "loin":
                         floats([sum(F(SECTIONS_2[k], k + 1) for k in range(j, 3)) for j in range(3)]),
                     "la part d'un hameau dépend de ce qu'il ajoute au coût, pas seulement du nombre de hameaux":
                         floats([F(needs_2()[-1], 3)] * 3)}'''),
        ("b", "a list of 3 numbers: the dividends of {H1, H2}, {H1, H3}, {H2, H3}",
         "floats([dividends_0(cost_2, 3)[frozenset(p)] for p in ((0, 1), (0, 2), (1, 2))])",
         '''decimals=0,
           mistakes={"d_{ij} = c({i, j}) − c({i}) − c({j}) : retire les deux hameaux seuls":
                         [needs_2()[j] - needs_2()[i] for i, j in ((0, 1), (0, 2), (1, 2))],
                     "pour une paire, le dividende est c({i, j}) − c({i}) − c({j}) + c(∅) : regarde son signe":
                         floats([-dividends_0(cost_2, 3)[frozenset(p)] for p in ((0, 1), (0, 2), (1, 2))])}'''),
        ("c", "a number: the dividend of the three hamlets together", "int(dividends_0(cost_2, 3)[frozenset({0, 1, 2})])",
         '''mistakes={"dans la somme alternée, les coûts des paires sont soustraits et ceux des hameaux seuls ajoutés":
                         int(cost_2({0, 1, 2}) - sum(cost_2(set(p)) for p in ((0, 1), (0, 2), (1, 2)))
                             - sum(cost_2({i}) for i in range(3))),
                     "le dividende de N retire aussi les dividendes des paires, pas seulement ceux des hameaux seuls":
                         int(cost_2({0, 1, 2}) - sum(cost_2({i}) for i in range(3)))}'''),
        ("d", "a list of 3 numbers (1 decimal): the new shares", "floats(shapley_0(lambda S: cost_2(S, SECTIONS_2D), 3))",
         '''decimals=1,
           mistakes={"le surcoût du tronçon 2 ne concerne que les hameaux qui l'utilisent":
                         floats([x + F(8, 3) for x in shapley_0(cost_2, 3)]),
                     "H3, plus loin que H2, utilise aussi le tronçon de H1 à H2":
                         floats([x + (8 if i == 1 else 0) for i, x in enumerate(shapley_0(cost_2, 3))])}'''),
    ]),

    Paper("MB6.3", "Le rendement d'une parcelle selon la pluie et l'engrais : courbes ICE et dérivée croisée de deux "
                   "modèles, puis la moyenne marginale et la moyenne conditionnelle quand pluie et engrais sont corrélés", [
        ("a", "a list of 3 numbers (1 decimal): model 1, the gain for the three plots", "floats(gains_3(F1_3))",
         '''decimals=1,
           mistakes={"le gain est une différence f(p, 2) − f(p, 1), pas la dérivée en e = 1": floats(slopes_3(F1_3)),
                     "le gain se lit sur la courbe ICE de chaque parcelle : f(p, 2) − f(p, 1), et non f(p, 2)":
                         floats([F1_3.subs({p_3: p, e_3: 2}) for p in PLOTS_3])}'''),
        ("b", "a list of 3 numbers (1 decimal): model 2, the same gain", "floats(gains_3(F2_3))",
         '''decimals=1,
           mistakes={"le gain est f(p, 2) − f(p, 1), pas f(p, 1) − f(p, 2)": floats([-g for g in gains_3(F2_3)]),
                     "le gain est une différence f(p, 2) − f(p, 1), pas la dérivée en e = 1": floats(slopes_3(F2_3)),
                     "(p − e − 3)² n'est pas p² + e² + 9 : développe les doubles produits, ou garde le carré tel quel":
                         floats(gains_3(F2_WRONG_3))}'''),
        ("c", "a list of 2 numbers: the cross derivative of model 1, then of model 2",
         "floats([sp.diff(F1_3, p_3, e_3), sp.diff(F2_3, p_3, e_3)])",
         '''decimals=0,
           mistakes={"la dérivée croisée de −½(p − e − 3)² : dérive d'abord par p, puis dérive le résultat par e, sans "
                     "perdre le signe de −e":
                         floats([sp.diff(F1_3, p_3, e_3), -sp.diff(F2_3, p_3, e_3)]),
                     "la dérivée croisée dérive une fois par p et une fois par e, pas deux fois par e":
                         floats([sp.diff(F1_3, e_3, 2), sp.diff(F2_3, e_3, 2)])}'''),
        ("d", "a list of 2 numbers (3 decimals): PD(2), then M(2)",
         "floats([F1_3.subs({p_3: MP_3, e_3: 2}), F1_3.subs({p_3: rain_given_3(2), e_3: 2})])",
         '''decimals=3,
           mistakes={"la moyenne conditionnelle tient compte de la corrélation : sachant E = 2, la pluie moyenne n'est "
                     "plus 5,5": floats([F1_3.subs({p_3: MP_3, e_3: 2})] * 2),
                     "la pente de E[P | E = v] est ρ σ_P/σ_E, pas ρ σ_E/σ_P":
                         floats([F1_3.subs({p_3: MP_3, e_3: 2}),
                                 F1_3.subs({p_3: rain_given_3(2, slope=RHO_3 * SE_3 / SP_3), e_3: 2})]),
                     "la pente de E[P | E = v] est ρ σ_P/σ_E : n'oublie pas le rapport σ_P/σ_E":
                         floats([F1_3.subs({p_3: MP_3, e_3: 2}), F1_3.subs({p_3: rain_given_3(2, slope=RHO_3), e_3: 2})])}'''),
        ("e", "a number (3 decimals): the slope of M(v) − PD(v)", "floats(sp.Rational(3, 5) * RHO_3 * SP_3 / SE_3)",
         '''decimals=3,
           mistakes={"l'écart vient de la pluie : il est multiplié par l'effet 0,6 d'une unité de pluie":
                         floats(RHO_3 * SP_3 / SE_3),
                     "la pente de E[P | E = v] est ρ σ_P/σ_E : n'oublie pas le rapport σ_P/σ_E":
                         floats(sp.Rational(3, 5) * RHO_3)}'''),
    ]),

    Paper("MB6.4", "Le travail de deux forces entre deux points : un champ de gradient le long de trois chemins, puis un "
                   "champ qui n'en est pas un (Schwarz) le long de deux chemins", [
        ("a", "a number: the work of F along the segment", "floats(work_4(F_4, segment_4(A_4, B_4)))",
         '''decimals=2,
           mistakes={"le travail de A vers B est f(B) − f(A), pas f(A) − f(B)": floats(-work_4(F_4, segment_4(A_4, B_4))),
                     "le produit scalaire F · γ′ compte les deux composantes : F₁ γ₁′ + F₂ γ₂′":
                         floats(work_4((F_4[0], 0), segment_4(A_4, B_4)))}'''),
        ("b", "a list of 2 numbers: the work of F along the horizontal leg, then the vertical leg",
         "floats([work_4(F_4, segment_4(A_4, K_4)), work_4(F_4, segment_4(K_4, B_4))])",
         '''decimals=0,
           mistakes={"l'escalier va d'abord à l'horizontale, de A à (2, 0), puis à la verticale":
                         floats([work_4(F_4, segment_4(K_4, B_4)), work_4(F_4, segment_4(A_4, K_4))]),
                     "le coin de l'escalier est (2, 0), pas (1, 1)":
                         floats([work_4(F_4, segment_4(A_4, (1, 1))), work_4(F_4, segment_4((1, 1), B_4))])}'''),
        ("c", "a number: the work of F along the arc of parabola", "floats(work_4(F_4, ARC_4))",
         '''decimals=2,
           mistakes={"la vitesse de γ(t) = (1 + t, t²) est (1, 2t) : la dérivée de t² est 2t":
                         floats(work_4(F_4, ARC_4, speed=(1, t_4))),
                     "le travail de A vers B est f(B) − f(A), pas f(A) − f(B)": floats(-work_4(F_4, ARC_4))}'''),
        ("d", "a list of 2 numbers: dG1/dy and dG2/dx at A",
         "floats([sp.diff(G_4[0], y_4).subs({x_4: A_4[0], y_4: A_4[1]}), sp.diff(G_4[1], x_4).subs({x_4: A_4[0], y_4: A_4[1]})])",
         '''decimals=0,
           mistakes={"∂G₁/∂y dérive la première composante par y, ∂G₂/∂x la seconde par x : garde cet ordre":
                         floats([sp.diff(G_4[1], x_4).subs({x_4: A_4[0], y_4: A_4[1]}),
                                 sp.diff(G_4[0], y_4).subs({x_4: A_4[0], y_4: A_4[1]})]),
                     "les dérivées sont demandées au point A = (1, 0)":
                         floats([sp.diff(G_4[0], y_4).subs({x_4: B_4[0], y_4: B_4[1]}),
                                 sp.diff(G_4[1], x_4).subs({x_4: B_4[0], y_4: B_4[1]})])}'''),
        ("e", "a list of 2 numbers: the work of G along the segment, then the staircase",
         "floats([work_4(G_4, segment_4(A_4, B_4)), work_4(G_4, segment_4(A_4, K_4)) + work_4(G_4, segment_4(K_4, B_4))])",
         '''decimals=0,
           mistakes={"l'escalier est celui de b), par le coin (2, 0)":
                         floats([work_4(G_4, segment_4(A_4, B_4)),
                                 work_4(G_4, segment_4(A_4, (1, 1))) + work_4(G_4, segment_4((1, 1), B_4))]),
                     "le segment d'abord, l'escalier ensuite":
                         floats([work_4(G_4, segment_4(A_4, K_4)) + work_4(G_4, segment_4(K_4, B_4)),
                                 work_4(G_4, segment_4(A_4, B_4))])}'''),
    ]),

    Paper("MB6.5", "La variation d'un coût à trois facteurs (prix, quantité, taux de change) partagée entre les facteurs : "
                   "le long du segment, puis par la moyenne des six chemins en escalier, et pourquoi les deux partages "
                   "coïncident", [
        ("a", "a number (2 decimals): C(x) − C(r), in euros", "floats(cost_5(X_5) - cost_5(R_5))",
         '''decimals=2,
           mistakes={"la variation va du premier trimestre au second : C(x) − C(r)": floats(cost_5(R_5) - cost_5(X_5)),
                     "la variation d'un produit n'est pas le produit des variations":
                         floats(math.prod(X_5[k] - R_5[k] for k in range(3)))}'''),
        ("b", "a list of 3 numbers (2 decimals): the shares of the price, the quantity, the exchange rate",
         "floats([segment_share_5(k) for k in range(3)])",
         '''decimals=2,
           mistakes={"le produit des deux autres facteurs le long du segment a un terme en t², d'intégrale 1/3":
                         floats([segment_share_5(k, quadratic=0) for k in range(3)]),
                     "l'intégrale de t² entre 0 et 1 vaut 1/3, pas 1/2":
                         floats([segment_share_5(k, quadratic=F(1, 2)) for k in range(3)])}'''),
        ("c", "a list of 2 numbers (2 decimals): the exchange rate in the order (p, q, tau), then (tau, p, q)",
         "floats([game_5({0, 1, 2}) - game_5({0, 1}), game_5({2}) - game_5(set())])",
         '''decimals=2,
           mistakes={"dans l'ordre (p, q, τ), τ change en dernier : le prix et la quantité ont déjà leurs valeurs du "
                     "second trimestre": floats([game_5({2}) - game_5(set()), game_5({0, 1, 2}) - game_5({0, 1})]),
                     "le taux de change baisse : sa contribution est négative":
                         floats([game_5({0, 1}) - game_5({0, 1, 2}), game_5(set()) - game_5({2})])}'''),
        ("d", "a number (2 decimals): the mean contribution of the exchange rate", "floats(shapley_0(game_5, 3)[2])",
         '''decimals=2,
           mistakes={"la moyenne porte sur les six ordres, pas seulement sur un ordre et son inverse":
                         floats((game_5({2}) - game_5(set()) + game_5({0, 1, 2}) - game_5({0, 1})) / 2),
                     "la variation ne se partage pas à parts égales entre les trois facteurs":
                         floats((cost_5(X_5) - cost_5(R_5)) / 3)}'''),
    ]),

    Paper("MB6.6", "Des relevés de capteurs sur une grille 3 × 4 : la dérivée d'un indice régional par un réchauffement "
                   "uniforme, puis la grille agrandie deux fois par interpolation bilinéaire, centres ou coins alignés", [
        ("a", "a number (1 decimal): the index y", "index_6(T_6)",
         '''decimals=1,
           mistakes={"une case sous 10 °C ne compte pas : max(0, T − 10) vaut 0, pas un nombre négatif":
                         float((A_6 * (T_6 - 10)).sum()),
                     "chaque case compte avec sa surface a_ij": float(np.maximum(0, T_6 - 10).sum())}'''),
        ("b", "an integer: the derivative by a uniform warming", "int(A_6[T_6 > 10].sum())",
         '''mistakes={"une case sous 10 °C ne bouge pas l'indice : sa dérivée est nulle": int(A_6.sum()),
                     "chaque case au-dessus de 10 °C ajoute sa surface a_ij, pas 1": int((T_6 > 10).sum())}'''),
        ("c", "a number (1 decimal): the index after a warming of 1 °C", "index_6(T_6 + 1)",
         '''decimals=1,
           mistakes={"deux cases passent au-dessus de 10 °C : la dérivée ne vaut que tant qu'aucune case ne franchit "
                     "10 °C": index_6(T_6) + int(A_6[T_6 > 10].sum()),
                     "une case reste à 0 tant qu'elle est sous 10 °C, même réchauffée": float((A_6 * (T_6 + 1 - 10)).sum())}'''),
        ("d", "a list of 6 numbers (2 decimals): centres aligned, the coordinates of the 6 rows",
         "floats([centre_6(u, 3, 6) for u in range(6)])",
         '''decimals=2,
           mistakes={"la formule des centres retire ½ après la mise à l'échelle : (u + ½) h/H − ½":
                         floats([(u + F(1, 2)) * F(3, 6) for u in range(6)]),
                     "le centre de la case u est en u + ½, pas en u": floats([u * F(3, 6) - F(1, 2) for u in range(6)])}'''),
        ("e", "a list of 6 numbers (2 decimals): corners aligned, the coordinates of the 6 rows",
         "floats([corner_6(u, 3, 6) for u in range(6)])",
         '''decimals=2,
           mistakes={"les coins alignés envoient la dernière case sur la dernière : le facteur est (h − 1)/(H − 1)":
                         floats([u * F(3, 6) for u in range(6)]),
                     "le facteur des coins alignés est (h − 1)/(H − 1), pas (h − 1)/H : les centres des cases extrêmes "
                     "des deux grilles se correspondent": floats([u * F(2, 6) for u in range(6)])}'''),
        ("f", "a list of 2 numbers (2 decimals): the cell (row 4, column 5), centres aligned, then corners aligned",
         "[bilinear_6(T_6, centre_6(4, 3, 6), centre_6(5, 4, 8)), bilinear_6(T_6, corner_6(4, 3, 6), corner_6(5, 4, 8))]",
         '''decimals=2,
           mistakes={"le voisin le plus proche reçoit le plus grand poids : (1 − t) a + t b, avec t la distance à a":
                         [bilinear_6(T_6, centre_6(4, 3, 6), centre_6(5, 4, 8), swapped=True),
                          bilinear_6(T_6, corner_6(4, 3, 6), corner_6(5, 4, 8), swapped=True)],
                     "le facteur des colonnes se calcule avec les nombres de colonnes, 4 et 8 ; celui des lignes ne sert "
                     "qu'aux lignes": [bilinear_6(T_6, centre_6(4, 3, 6), centre_6(5, 4, 8)),
                                       bilinear_6(T_6, corner_6(4, 3, 6), 5 * F(2, 5))]}'''),
    ]),

    Paper("MB6.7", "Un contrôle de pièces sur deux lignes de production aux taux de défauts différents : les taux de rejet "
                   "sous la séparation, un tirage au sort entre deux seuils pour atteindre un taux de détection, et les "
                   "poids qui rendent ligne et défaut indépendants", [
        ("a", "a list of 2 numbers (4 decimals): the rejection rate of each line",
         "floats([TPR_7 * p + FPR_7 * (1 - p) for p in RATES_7])",
         '''decimals=4,
           mistakes={"une pièce rejetée est défectueuse et détectée, ou bonne et rejetée à tort : ajoute les fausses "
                     "alertes": floats([TPR_7 * p for p in RATES_7]),
                     "le taux de détection pèse la part des pièces défectueuses, p_g, et le taux de fausses alertes "
                     "celle des bonnes, 1 − p_g": floats([TPR_7 * (1 - p) + FPR_7 * p for p in RATES_7])}'''),
        ("b", "a number (4 decimals): the probability q", "floats(draw_7())",
         '''decimals=4,
           mistakes={"q est la probabilité de tirer A, le seuil qui détecte le moins, pas celle de tirer B":
                         floats(1 - draw_7()),
                     "q est une part de l'écart entre les deux taux de détection : divise par TPR_B − TPR_A":
                         floats((THRESHOLD_B_7[1] - TARGET_7) / (TARGET_7 - THRESHOLD_A_7[1]))}'''),
        ("c", "a number (4 decimals): the rate of false alarms obtained",
         "floats(draw_7() * THRESHOLD_A_7[0] + (1 - draw_7()) * THRESHOLD_B_7[0])",
         '''decimals=4,
           mistakes={"le seuil A est tiré avec la probabilité q : c'est son taux de fausses alertes qui pèse q":
                         floats((1 - draw_7()) * THRESHOLD_A_7[0] + draw_7() * THRESHOLD_B_7[0]),
                     "le tirage change aussi le taux de fausses alertes : la même combinaison des deux seuils, avec le "
                     "même q": floats(THRESHOLD_B_7[0])}'''),
        ("d", "a list of 4 numbers (4 decimals): w(1, defect), w(1, no defect), w(2, defect), w(2, no defect)",
         "floats(weights_7())",
         '''decimals=4,
           mistakes={"le poids est P(g) P(y) / P(g, y) : la probabilité jointe P(g, y) se lit sur toute la table":
                         floats(weights_7(within_line=True)),
                     "le poids divise par P(g, y), la part de la case : P(g) P(y) seul ne corrige rien":
                         floats(weights_7(divided=False))}'''),
        ("e", "a list of 2 numbers (4 decimals): the weighted defect rate of each line", "floats(weighted_rates_7())",
         '''decimals=4,
           mistakes={"chaque case reçoit le poids de sa ligne et de son label": floats(weighted_rates_7(exchanged=True)),
                     "les taux pondérés pèsent chaque case par son poids : ce ne sont plus les taux bruts":
                         floats(list(RATES_7))}'''),
    ]),

    Paper("MB6.11", "Pont : l'écart des taux de détection de deux laboratoires et son intervalle, par l'erreur type d'une "
                    "différence de deux proportions, qui se lit avec le nombre d'échantillons positifs de chacun", [
        ("a", "a list of 2 numbers (4 decimals): the detection rates of A and B", "[RATE_A_11, RATE_B_11]",
         '''decimals=4,
           mistakes={"un taux de détection est une proportion, entre 0 et 1, pas un pourcentage":
                         [100 * RATE_A_11, 100 * RATE_B_11],
                     "l'ordre demandé : A, puis B": [RATE_B_11, RATE_A_11]}'''),
        ("b", "a number (4 decimals): the standard error of TPR_B − TPR_A", "standard_error_11()",
         '''decimals=4,
           mistakes={"les variances de deux estimations indépendantes s'ajoutent, pas leurs erreurs types":
                         standard_error_11(add_errors=True),
                     "chaque taux garde sa propre proportion : pas de taux commun aux deux laboratoires":
                         standard_error_11(pooled=True)}'''),
        ("c", "a list of 2 numbers (3 decimals): the Wald interval at 95 %", "wald_11(1.96)",
         '''decimals=3,
           mistakes={"un intervalle à 95 % prend 1,96 erreur type de chaque côté": wald_11(1),
                     "un intervalle à 95 % prend 1,96 erreur type de chaque côté, pas 1,645": wald_11(1.645)}'''),
        ("d", "a number (4 decimals): the standard error with 4 times more contaminated samples in A",
         "standard_error_11(times_a=4)",
         '''decimals=4,
           mistakes={"seul le terme du laboratoire A est divisé par 4 : l'erreur type de l'écart n'est pas divisée par 2":
                         round(standard_error_11(), 4) / 2,
                     "quadrupler l'effectif divise la variance de ce terme par 4, pas par 16": standard_error_11(times_a=16)}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (the n! orders of itertools.permutations for the pivots and the
# Shapley values, exact fractions for the indices, the dividends, the shares, the rates and the weights, SymPy for the
# models of the plot and the line integrals, NumPy for the grid, math for the laboratories)
import itertools
import math
from fractions import Fraction as F

import numpy as np
import sympy as sp


def floats(values):
    """A number or a list of numbers (fractions, SymPy) as a float or a list of floats (-0.0 written 0.0)."""
    return (np.round(np.asarray([float(v) for v in values] if isinstance(values, (list, tuple)) else float(values),
                                dtype=float), 12) + 0.0).tolist()


def shapley_0(v, n):
    """The Shapley values of the game v on the players 0, ..., n - 1, averaged over the n! orders (exact)."""
    phi = [F(0)] * n
    for order in itertools.permutations(range(n)):
        before = frozenset()
        for i in order:
            phi[i] += F(v(before | {i})) - F(v(before))
            before = before | {i}
    return [p / math.factorial(n) for p in phi]


def dividends_0(v, n):
    """The Harsanyi dividends of the game v: the alternating sum over the subsets of each coalition T (exact)."""
    out = {}
    for size in range(n + 1):
        for T in itertools.combinations(range(n), size):
            out[frozenset(T)] = sum((-1) ** (len(T) - k) * F(v(frozenset(S)))
                                    for k in range(len(T) + 1) for S in itertools.combinations(T, k))
    return out


# MB6.1: the council [11; 8, 6, 3, 1] of A, B, C, D; c) D with 2 votes; d) Hoeffding, ± 0.05 with probability >= 0.96
QUOTA_1, VOTES_1, VOTES_1C, EPS_1, DELTA_1 = 11, (8, 6, 3, 1), (8, 6, 3, 2), 0.05, 0.04


def pivots_1(quota, votes):
    """The number of orders in which each member is pivot (its arrival takes the votes from below quota to quota or
    more)."""
    counts = [0] * len(votes)
    for order in itertools.permutations(range(len(votes))):
        total = 0
        for member in order:
            if total < quota <= total + votes[member]:
                counts[member] += 1
                break
            total += votes[member]
    return counts


def last_1(votes):
    """The number of orders in which each member arrives last."""
    return [math.factorial(len(votes) - 1)] * len(votes)


def memberships_1(quota, votes):
    """For each member, its share of the memberships of the winning coalitions."""
    winning = [c for k in range(len(votes) + 1) for c in itertools.combinations(range(len(votes)), k)
               if sum(votes[i] for i in c) >= quota]
    counts = [sum(1 for c in winning if i in c) for i in range(len(votes))]
    return [F(c, sum(counts)) for c in counts]


def hoeffding_1(two_sided=True, squared=True):
    """The smallest m with 2 e^(-2 m eps²) <= delta (two_sided=False: without the 2; squared=False: eps for eps²)."""
    return math.ceil(math.log((2 if two_sided else 1) / DELTA_1) / (2 * (EPS_1 ** 2 if squared else EPS_1)))


# MB6.2: three hamlets along a pipe: the sections cost 30, 21 and 17 k€; d) the section 2 costs 8 k€ more
SECTIONS_2 = (30, 21, 17)
SECTIONS_2D = (SECTIONS_2[0], SECTIONS_2[1] + 8, SECTIONS_2[2])


def needs_2(sections=SECTIONS_2):
    """The cost of the pipe up to each hamlet."""
    return list(itertools.accumulate(sections))


def cost_2(S, sections=SECTIONS_2):
    """c(S): the cost of the pipe up to the farthest hamlet of S."""
    return max((needs_2(sections)[i] for i in S), default=0)


# MB6.3: the yield (t/ha) of a plot, rain p and fertiliser e (hundreds of mm, of kg/ha); P ~ N(5.5, 1.2²),
# E ~ N(1.5, 0.5²), correlation 0.35
p_3, e_3 = sp.symbols("p e", real=True)
F1_3 = sp.Rational(3, 2) + sp.Rational(3, 5) * p_3 + sp.Rational(12, 5) * e_3 - sp.Rational(2, 5) * e_3 ** 2
F2_3 = sp.Rational(15, 2) - sp.Rational(1, 2) * (p_3 - e_3 - 3) ** 2
F2_WRONG_3 = sp.Rational(15, 2) - sp.Rational(1, 2) * (p_3 ** 2 + e_3 ** 2 + 9)      # the square developed wrongly
PLOTS_3 = [sp.Integer(4), sp.Rational(11, 2), sp.Integer(7)]
MP_3, SP_3, ME_3, SE_3, RHO_3 = sp.Rational(11, 2), sp.Rational(6, 5), sp.Rational(3, 2), sp.Rational(1, 2), sp.Rational(7, 20)


def gains_3(f):
    """f(p, 2) - f(p, 1) for the three plots."""
    return [f.subs({p_3: p, e_3: 2}) - f.subs({p_3: p, e_3: 1}) for p in PLOTS_3]


def slopes_3(f):
    """The derivative in e at e = 1, for the three plots."""
    return [sp.diff(f, e_3).subs({p_3: p, e_3: 1}) for p in PLOTS_3]


def rain_given_3(v, slope=RHO_3 * SP_3 / SE_3):
    """E[P | E = v] (M25a), affine in v."""
    return MP_3 + slope * (v - ME_3)


# MB6.4: from A = (1, 0) to B = (2, 1); F = grad(x² y² + 5x), G = (2y, 3x²); the staircase by (2, 0); the arc (1 + t, t²)
x_4, y_4, t_4 = sp.symbols("x y t", real=True)
POTENTIAL_4 = x_4 ** 2 * y_4 ** 2 + 5 * x_4
F_4 = (sp.diff(POTENTIAL_4, x_4), sp.diff(POTENTIAL_4, y_4))
G_4 = (2 * y_4, 3 * x_4 ** 2)
A_4, B_4, K_4 = (1, 0), (2, 1), (2, 0)
ARC_4 = (1 + t_4, t_4 ** 2)


def segment_4(P, Q):
    """The segment from P to Q, as a path of parameter t in [0, 1]."""
    return (P[0] + t_4 * (Q[0] - P[0]), P[1] + t_4 * (Q[1] - P[1]))


def work_4(field, path, speed=None):
    """The integral over [0, 1] of field(path(t)) . path'(t) (exact); speed: another velocity (the classic error)."""
    path = [sp.sympify(c) for c in path]
    velocity = speed if speed is not None else [sp.diff(c, t_4) for c in path]
    integrand = sum(sp.sympify(field[k]).subs({x_4: path[0], y_4: path[1]}) * velocity[k] for k in range(2))
    return sp.integrate(sp.expand(integrand), (t_4, 0, 1))


# MB6.5: the cost C = p q tau (euros): the first quarter r, the second quarter x
R_5 = (F(23, 2), F(680), F(93, 100))
X_5 = (F(27, 2), F(590), F(87, 100))


def cost_5(z):
    return z[0] * z[1] * z[2]


def game_5(S):
    """v(S) = C(x_S, r_S̄): the factors of S at their value of the second quarter, the others at the first."""
    return cost_5([X_5[k] if k in S else R_5[k] for k in range(3)])


def segment_share_5(k, quadratic=F(1, 3)):
    """The share of factor k along the segment, h_k times the integral of the product of the two others (exact);
    quadratic: the integral of t² (1/3; 0 drops the term, 1/2 is the classic error)."""
    j, l = [m for m in range(3) if m != k]
    h = [X_5[m] - R_5[m] for m in range(3)]
    return h[k] * (R_5[j] * R_5[l] + (R_5[j] * h[l] + R_5[l] * h[j]) / 2 + h[j] * h[l] * quadratic)


# MB6.6: the temperatures T (°C) and the cultivated areas a of the 3 x 4 grid; y = sum of a max(0, T - 10)
T_6 = np.array([[11.8, 9.4, 13.2, 10.8], [8.7, 12.5, 14.1, 9.9], [10.3, 7.6, 12.0, 11.4]])
A_6 = np.array([[2, 1, 3, 1], [1, 2, 2, 1], [3, 1, 1, 2]])


def index_6(T):
    return float((A_6 * np.maximum(0, T - 10)).sum())


def centre_6(u, h, H):
    """The coordinate of origin of the cell u, centres aligned (before the return to the border)."""
    return (u + F(1, 2)) * F(h, H) - F(1, 2)


def corner_6(u, h, H):
    """The coordinate of origin of the cell u, corners aligned."""
    return u * F(h - 1, H - 1)


def bilinear_6(grid, u, v, swapped=False):
    """The bilinear value of grid at the coordinates (u, v) of origin; swapped: the weights of the two neighbours
    exchanged in both directions (the classic error)."""
    i, j = int(math.floor(u)), int(math.floor(v))
    s, t = float(u) - i, float(v) - j
    if swapped:
        s, t = 1 - s, 1 - t
    top = (1 - t) * grid[i, j] + t * grid[i, j + 1]
    bottom = (1 - t) * grid[i + 1, j] + t * grid[i + 1, j + 1]
    return float((1 - s) * top + s * bottom)


# MB6.7: the defect rates of the two lines; the control (detection 0.88, false alarms 0.04); the thresholds A and B of
# line 2 as (false alarms, detection), the target 0.90; the table of counts (line, defect)
RATES_7 = (F(6, 100), F(14, 100))
TPR_7, FPR_7 = F(88, 100), F(4, 100)
THRESHOLD_A_7, THRESHOLD_B_7, TARGET_7 = (F(3, 100), F(74, 100)), (F(9, 100), F(96, 100)), F(90, 100)
COUNTS_7 = {(1, 1): 78, (1, 0): 1300 - 78, (2, 1): 154, (2, 0): 1100 - 154}


def draw_7():
    """q: the probability of drawing the threshold A that reaches the target detection rate."""
    return (THRESHOLD_B_7[1] - TARGET_7) / (THRESHOLD_B_7[1] - THRESHOLD_A_7[1])


def weights_7(within_line=False, divided=True):
    """w(g, y) = P(g) P(y) / P(g, y), in the order (1, defect), (1, none), (2, defect), (2, none); within_line: divided
    by P(y | g) instead; divided=False: P(g) P(y) alone."""
    total = sum(COUNTS_7.values())
    line = {g: F(COUNTS_7[g, 1] + COUNTS_7[g, 0], total) for g in (1, 2)}
    label = {y: F(COUNTS_7[1, y] + COUNTS_7[2, y], total) for y in (0, 1)}
    out = []
    for g, y in ((1, 1), (1, 0), (2, 1), (2, 0)):
        joint = F(COUNTS_7[g, y], COUNTS_7[g, 1] + COUNTS_7[g, 0]) if within_line else F(COUNTS_7[g, y], total)
        out.append(line[g] * label[y] / joint if divided else line[g] * label[y])
    return out


def weighted_rates_7(exchanged=False):
    """The weighted defect rate of each line (exchanged: the weights of each line applied to the counts of the other,
    the classic error)."""
    w = dict(zip(((1, 1), (1, 0), (2, 1), (2, 0)), weights_7()))
    return [w[3 - g if exchanged else g, 1] * COUNTS_7[g, 1]
            / (w[3 - g if exchanged else g, 1] * COUNTS_7[g, 1] + w[3 - g if exchanged else g, 0] * COUNTS_7[g, 0])
            for g in (1, 2)]


# MB6.11: laboratory A detected 20 of its 28 contaminated samples, laboratory B 448 of its 520
POS_A_11, HIT_A_11, POS_B_11, HIT_B_11 = 28, 20, 520, 448
RATE_A_11, RATE_B_11 = HIT_A_11 / POS_A_11, HIT_B_11 / POS_B_11


def standard_error_11(times_a=1, add_errors=False, pooled=False):
    """The standard error of the gap of the two detection rates (times_a: A with times_a times more contaminated
    samples, at the same rate; add_errors: the two standard errors added; pooled: one common rate)."""
    if pooled:
        common = (HIT_A_11 + HIT_B_11) / (POS_A_11 + POS_B_11)
        return math.sqrt(common * (1 - common) * (1 / POS_A_11 + 1 / POS_B_11))
    terms = [RATE_A_11 * (1 - RATE_A_11) / (times_a * POS_A_11), RATE_B_11 * (1 - RATE_B_11) / POS_B_11]
    return sum(math.sqrt(x) for x in terms) if add_errors else math.sqrt(sum(terms))


def wald_11(z):
    """The interval gap ± z standard errors."""
    gap = RATE_B_11 - RATE_A_11
    return [gap - z * standard_error_11(), gap + z * standard_error_11()]'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ MB6.1 à MB6.7 ; 🔗 MB6.11)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une liste `[0.2, -1]`, dans l'ordre que dit la question.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")


def paper_part(kind: str) -> list:
    """The cells of Part 0."""
    return paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO)


# ---------------------------------------------------------------------------
# Notebook exercises: your library (MB6.13 to MB6.16)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to D)
import contextlib
import dis
import math
import os
import re
import sys
import time
from types import MappingProxyType

import matplotlib.pyplot as plt
import numpy as np

from wbm.errors import MymathMissingError
from wbm.nbtools import StopCheck, checked, drawn, filled, fr, run_pytest_group, verdict

TEST_MB6 = "tests/test_mb6_attribution.py"           # the tests of mymath/attribution.py
REF = wbm.load_mymath("ref", alias="mymath_ref")       # the reference: some checks of the hidden cases rely on it
ref_att = REF.attribution


def shown(value, digits=4):
    """A short text for a result of the learner's code (the check messages): numbers rounded, as lists."""
    if value is None:
        return "None"
    try:
        return str(np.round(np.asarray(value, dtype=float), digits).tolist())[:160]
    except (TypeError, ValueError):
        return repr(value)[:160]


def check_answer(ex_id, value, hint=None):
    """wbm.check(ex_id, value, computed=True). For a list that holds True or False, the message gives only how many
    elements are right, not the place of the first wrong one (it would let you guess the booleans one by one).
    hint(value), when given, may return a targeted « Piste » for a wrong answer (None otherwise)."""
    holds_bool = isinstance(value, (list, tuple)) and any(isinstance(v, (bool, np.bool_)) or (
        isinstance(v, (list, tuple)) and any(isinstance(w, (bool, np.bool_)) for w in v)) for v in value)
    if not holds_bool and hint is None:
        return wbm.check(ex_id, value, computed=True)
    result = wbm.check(ex_id, value, computed=True, quiet=True)
    message = result.message
    if holds_bool:
        for cut in (" Le premier faux est le ", " Premier élément faux à l'indice "):
            message = message.split(cut)[0]
    if hint is not None and result.status not in ("correct", "pending", "unknown") and "Piste" not in message:
        try:
            extra = hint(value)
        except Exception:  # noqa: BLE001 - an odd answer: no targeted hint
            extra = None
        if extra:
            message = f"{message} Piste : {extra}"
    icon = {"correct": "✅", "pending": "⏳", "unknown": "❓"}.get(result.status, "❌")
    print(f"{icon} Ex {ex_id} : {message}")
    return result


def library_hint(names):
    """A hint for a wrong answer computed with the learner's library (no classic error recognised): its tests first,
    then the call."""
    return lambda value: (f"cette valeur vient de {names} de ta librairie : si ses tests passent tous (plus haut), "
                          "l'erreur est dans l'appel (les arguments, leur ordre, ce que tu lis dans le résultat) ; et "
                          "donne la valeur que rend le calcul, sans l'arrondir")


def passes(ex_id, value):
    """True when value is the hidden answer ex_id (wbm.check, computed=True, nothing printed)."""
    try:
        return bool(wbm.check(ex_id, value, computed=True, quiet=True).passed)
    except Exception:  # noqa: BLE001 - an odd value is not the answer
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


def as_floats(value):
    """value as a float array, or None when it is not an array of numbers."""
    try:
        return np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        return None


def call_safely(label, function, *args, **kwargs):
    """function(*args, **kwargs); an error of the learner's code becomes one ❌ line naming the call (StopCheck)."""
    try:
        return function(*args, **kwargs)
    except (NotImplementedError, MymathMissingError):
        raise
    except Exception as exc:  # noqa: BLE001 - the learner's error, reported with the name of the call
        print(f"❌ {label} : ton code lève {type(exc).__name__} : {str(exc)[:200]}")
        raise StopCheck from None


def frozen(array):
    """A float copy of array that refuses any change in place (the data given to the learner's functions)."""
    out = np.array(array, dtype=float)
    out.setflags(write=False)
    return out


class CodeFrom(BaseException):
    """Raised inside code_from when watched code starts (a BaseException: a broad except of the learner's code does
    not hide it)."""


_NOT_KEYED = {"CACHE", "PUSH_NULL", "RESUME", "NOP", "EXTENDED_ARG", "NOT_TAKEN"}


def code_key(code):
    """What identifies a compiled function whatever its file and the module around it: its instructions (without jump
    targets, nor what depends on the rest of the module) and the names of its variables."""
    ops = []
    for i in dis.get_instructions(code):
        if i.opname in _NOT_KEYED:
            continue
        jump = i.opcode in dis.hasjrel or i.opcode in dis.hasjabs or "JUMP" in i.opname or i.opname == "FOR_ITER"
        ops.append((i.opname, None if jump else i.argval.co_name if hasattr(i.argval, "co_code") else repr(i.argval)))
    return tuple(ops), code.co_varnames


def code_keys_of_file(path):
    """The code_key of every function of a Python file, compiled but not run (to recognise a copy of its code); an
    empty set for a file that cannot be read or compiled."""
    try:
        keys, todo = set(), [compile(open(path, encoding="utf-8").read(), str(path), "exec")]
    except (OSError, SyntaxError, ValueError, UnicodeDecodeError):
        return set()
    while todo:
        code = todo.pop()
        todo += [c for c in code.co_consts if hasattr(c, "co_code")]
        key = code_key(code)
        if code.co_name != "<module>" and len(key[0]) >= 15:
            keys.add(key)
    return keys


_ESCAPE = {"watch": None}      # what code_from(..., escapes=True) watches now (None: nothing)
_PROCESS_EVENTS = ("subprocess.Popen", "os.system", "os.posix_spawn", "os.fork", "os.forkpty", "os.exec", "os.spawn")


def _escape_hook(event, args, escape=_ESCAPE, processes=_PROCESS_EVENTS, os=os, stop=CodeFrom):
    """Audit hook, for the life of the kernel: inside code_from(..., escapes=True), opening a file of the watched places
    or starting another process stops the block (code run by another process escapes sys.monitoring). Everything it
    uses is bound when it is defined: it also runs while the kernel shuts down."""
    watch = escape["watch"]
    if watch is None:
        return
    if event == "open" and args and isinstance(args[0], (str, bytes, os.PathLike)):
        real = os.path.realpath(os.fsdecode(args[0]))
        if any(real == place or real.startswith(place + os.sep) for place in watch["places"]):
            watch["seen"].append("ouvre " + os.path.basename(real))
            raise stop
    elif event.startswith(processes):
        watch["seen"].append("lance un autre processus : " + event)
        raise stop


sys.addaudithook(_escape_hook)


@contextlib.contextmanager
def code_from(places, twins=(), escapes=False):
    """Inside the block, the start of any Python code (a function or a module body) of a file among places (files, or
    folders with everything under them), or of a function whose code_key is among twins (a copy of such a function),
    stops the block; yields the list of the names seen ("attribution.coalition_weights"). The learner's function must
    not run that code (mymath in a corrected function, the hidden module of a challenge). With escapes, opening a file
    of places or starting another process also stops it ("ouvre mb6_22.py", "lance un autre processus :
    subprocess.Popen"). Without sys.monitoring (Python < 3.12) or a free tool id, code is not watched."""
    places = [os.path.realpath(str(place)) for place in places]
    libraries = tuple({os.path.realpath(sys.prefix) + os.sep, os.path.realpath(sys.base_prefix) + os.sep})
    monitoring, tool, seen, inside = getattr(sys, "monitoring", None), None, [], {}
    for candidate in ((4, 3, 2) if monitoring is not None else ()):
        try:
            monitoring.use_tool_id(candidate, "code_from")
        except ValueError:                               # taken by another tool
            continue
        tool = candidate
        break
    if tool is not None:
        def on_start(code, offset):
            name = code.co_filename
            if name not in inside:
                real = os.path.realpath(name) if os.path.exists(name) else name
                if any(real == place or real.startswith(place + os.sep) for place in places):
                    inside[name] = True                  # watched
                elif twins and not real.startswith(libraries):
                    inside[name] = False                 # the learner's code: compared with twins
                else:
                    inside[name] = None                  # an installed library: not compared
            if inside[name]:
                seen.append(f"{os.path.splitext(os.path.basename(name))[0]}.{code.co_name}")
                raise CodeFrom
            if inside[name] is False and code_key(code) in twins:
                seen.append(f"une copie de {code.co_name}")
                raise CodeFrom
            return monitoring.DISABLE                    # other code: not watched again until the end of the block

        monitoring.register_callback(tool, monitoring.events.PY_START, on_start)
        monitoring.set_events(tool, monitoring.events.PY_START)
    if escapes:
        _ESCAPE["watch"] = {"places": places, "seen": seen}
    try:
        yield seen
    except CodeFrom:
        pass
    finally:
        _ESCAPE["watch"] = None
        if tool is not None:
            monitoring.set_events(tool, 0)
            monitoring.register_callback(tool, monitoring.events.PY_START, None)
            monitoring.free_tool_id(tool)
            monitoring.restart_events()'''

DATA = '''# The data of the paper exercises (02_exercices.md), read only
COUNCIL_1 = MappingProxyType({"quota": 11, "votes": (8, 6, 3, 1)})        # MB6.1: the votes of A, B, C, D (0 to 3)
PIPE_2 = MappingProxyType({"sections": (30, 21, 17), "needs": (30, 51, 68)})   # MB6.2: k€; needs = the pipe up to
#   each hamlet H1, H2, H3 (0 to 2)
YIELD_3 = MappingProxyType({"plots": (4.0, 5.5, 7.0), "mean_p": 5.5, "sd_p": 1.2, "mean_e": 1.5, "sd_e": 0.5,
                            "rho": 0.35})                                 # MB6.3: rain p and fertiliser e
FORCES_4 = MappingProxyType({"A": (1.0, 0.0), "B": (2.0, 1.0), "corner": (2.0, 0.0)})   # MB6.4: m; the staircase
#   goes from A to the corner, then to B
COST_5 = MappingProxyType({"r": (11.5, 680.0, 0.93), "x": (13.5, 590.0, 0.87)})   # MB6.5: (price $, quantity, €/$)
GRID_6 = MappingProxyType({"T": frozen([[11.8, 9.4, 13.2, 10.8], [8.7, 12.5, 14.1, 9.9], [10.3, 7.6, 12.0, 11.4]]),
                           "a": frozen([[2, 1, 3, 1], [1, 2, 2, 1], [3, 1, 1, 2]])})   # MB6.6: °C, hundreds of ha
LINES_7 = MappingProxyType({"defect_rates": (0.06, 0.14), "tpr": 0.88, "fpr": 0.04, "threshold_A": (0.03, 0.74),
                            "threshold_B": (0.09, 0.96), "target": 0.90, "pieces": (1300, 1100),
                            "defective": (78, 154)})                      # MB6.7: thresholds as (fpr, tpr), line 2
LABS_11 = MappingProxyType({"contaminated": (28, 520), "signalled": (20, 448)})   # MB6.11: A, B'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="MB6")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en MB5). Ouvre ta copie `mon_travail/mymath/attribution.py`, lis la "
         "docstring du module (ses conventions, et ce qui est permis) puis celle de la fonction, remplace chaque "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Dans le notebook, appelle tes fonctions par "
         "`mymath.attribution.<nom>` (par exemple `mymath.attribution.spearman_rho(x, y)`), ou donne-leur un nom court "
         "(`spearman_rho = mymath.attribution.spearman_rho`) dans une cellule exécutée après le rechargement. ⚠️ Le "
         "squelette n'importe rien : ajoute en tête du fichier `import itertools`, `import math`, `from fractions import "
         "Fraction` et `import numpy as np`, et `from .integrate import simpson` si tu reprends ta règle de Simpson de "
         "M02a. NumPy et les modules `math`, `fractions` et `itertools` sont permis, mais ni SciPy (`rankdata`, "
         "`spearmanr`, `pearsonr`, `scipy.integrate`), ni `np.corrcoef`, ni `np.cov`, ni le module `statistics`, ni "
         "pandas : les tests comparent tes résultats à `math.comb`, à `fractions`, à `scipy.integrate.quad` et à "
         "`scipy.stats.spearmanr`, et un test lit ton module. Ne modifie jamais les tableaux reçus. Hors de `mymath`, le "
         "notebook peut se servir de tout NumPy et de SciPy.")

REMINDER = ("> Même mode d'emploi qu'en MB6.13 : écris la fonction dans ta copie `mon_travail/mymath/attribution.py`, "
            "**enregistre**, puis exécute les cellules ci-dessous ; la première recharge ta librairie.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of attribution.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("todo", f'run_pytest_group(TEST_MB6, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_MB6, "{keyword}", impl="ref")')]


def answers_check(ex_id: str, letters: str, hints: dict | None = None) -> str:
    """The check cell of the answers a), b)... of a notebook exercise: one check_answer each. ``hints`` maps a letter to
    the code of a function value -> targeted hint (or None), written in the cell."""
    names = ", ".join(f"answer_{ex_id.replace('.', '_')}{letter}" for letter in letters)
    if not hints:
        return (f'for letter, answer in zip("{letters}", [{names}]):\n'
                f'    check_answer(f"{ex_id}{{letter}}", answer)')
    tag = ex_id.replace(".", "_")
    return "\n".join(f'check_answer("{ex_id}{letter}", answer_{tag}{letter}'
                     + (f", hint={hints[letter]})" if letter in hints else ")") for letter in letters)


def look(text: str, after: str = "") -> tuple:
    """The cell « Ce qu'il faut regarder » shown after the check (questions of 02_exercices.md; answers in 05)."""
    return ("md", f"**Ce qu'il faut regarder**{after} : {text} Les réponses sont dans `05_solutions.md`, section "
                  "Notebook.")


def ex(ex_id: str, goal: str, prereq: str, body: str, functions: str = "", **fields) -> Ex:
    """An exercise whose type, stars, minutes, title and tracks come from the contract (partie_7.py); a 🔨 shows the
    function it writes after its title (« · `coalition_weights` »)."""
    kind, stars, minutes, title, tracks = syllabus_entry(ex_id)
    if functions:
        title = f"{title} · {functions}"
    return Ex(ex_id, kind, stars, minutes, title, goal, prereq, body=body, tracks=tracks, **fields)


# ---------------------------------------------------------------------------
# MB6.13 · coalition_weights
# ---------------------------------------------------------------------------
CHECK_13 = '''def exact_13(value):
    """None when a) holds exact numbers (Fractions, or fractions written as text); a message when it holds floats."""
    try:
        items = list(value)
    except TypeError:
        return None
    if any(isinstance(item, (float, np.floating)) for item in items):
        return ("a) demande les poids exacts : des fractions (des Fraction, avec exact=True), pas des flottants, qui en "
                "sont des valeurs approchées")
    return None


if filled(answer_MB6_13a) and exact_13(answer_MB6_13a):
    print(f"❌ Ex MB6.13a : {exact_13(answer_MB6_13a)}")
else:
    check_answer("MB6.13a", answer_MB6_13a, hint=library_hint("coalition_weights"))
check_answer("MB6.13b", answer_MB6_13b, hint=library_hint("coalition_weights"))'''

NOTE_13 = (r"Les contrôles (`isinstance(n_players, bool)` d'abord), puis `Fraction(math.factorial(s) * math.factorial(n "
           r"- 1 - s), math.factorial(n))` pour chaque $s$, convertis en flottants dans un tableau si `exact` est faux. "
           r"a) $\big(\frac19, \frac1{72}, \frac1{252}, \frac1{504}, \frac1{630}, \frac1{504}, \frac1{252}, "
           r"\frac1{72}, \frac19\big)$. b) $\binom{24}{12} = 2\,704\,156$.")

MB6_13 = ex(
    "MB6.13", "programmer les poids des coalitions dans la valeur de Shapley, exacts ou en flottants, puis voir combien "
    "une coalition de taille moyenne pèse peu.", "fiche §1 ; R8 (factorielles, combinaisons)",
    functions="`coalition_weights`", mymath="attribution.py", note=NOTE_13,
    body=HOWTO + r"""

Écris `coalition_weights(n_players, exact=False)` (fiche §1), en suivant sa docstring : contrôle les arguments (`n_players` un entier $\ge 1$, pas un booléen ni un flottant ; `exact` un booléen), puis rends les $n$ poids $w(0), \ldots, w(n - 1)$, en `Fraction` (une liste) ou en flottants (un tableau NumPy). Lance le groupe de tests.

**L'usage.** Avec ta fonction :
- a) les 9 poids pour $n = 9$, exacts (une liste de 9 fractions : passe `exact=True`) ;
- b) pour $n = 25$, le conseil du 🏆, le rapport $\frac{w(0)}{w(12)}$ (un entier).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `coalition_weights` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_coalition_weights_ or test_module_uses_") + [
        ("md", "**L'usage** : les poids d'un jeu de 9 joueurs, puis un rapport de poids pour le conseil de 25 membres."),
        ("todo", '''answer_MB6_13a = answer_MB6_13b = ...
with wbm.attempt("MB6.13"):          # if you call coalition_weights here: ⏳ while it is not written
    answer_MB6_13a = ...  # a) a list of 9 fractions: the exact weights w(0), ..., w(8) for n = 9
    answer_MB6_13b = ...  # b) an integer: w(0) / w(12) for n = 25'''),
        ("check", CHECK_13),
        ("solution", '''coalition_weights = mymath.attribution.coalition_weights
answer_MB6_13a = coalition_weights(9, exact=True)
weights_13 = coalition_weights(25, exact=True)
answer_MB6_13b = int(weights_13[0] / weights_13[12])
print("a)", [str(w) for w in answer_MB6_13a], " b)", answer_MB6_13b)
print("   chaque taille, C(n − 1, s) w(s) :", sorted({str(math.comb(8, s) * w) for s, w in enumerate(answer_MB6_13a)}))'''),
        ("record", '''from fractions import Fraction as F_13r


def weights_13r(n, top=None):
    """The oracle: s! (n - 1 - s)! / top! in fractions (top = n; n - 1 is the classic error)."""
    top = n if top is None else top
    return [F_13r(math.factorial(s) * math.factorial(n - 1 - s), math.factorial(top)) for s in range(n)]


wbm.record("MB6.13a", [float(w) for w in weights_13r(9)], decimals=6,
           mistakes={"les poids divisent s! (n − 1 − s)! par n!, pas par (n − 1)! (relance les tests de "
                     "coalition_weights)": [float(w) for w in weights_13r(9, top=8)]})
wbm.record("MB6.13b", math.comb(24, 12),
           mistakes={"le conseil du 🏆 a 25 membres : les poids de n = 25": math.comb(23, 12),
                     "w(12) est le poids d'une coalition de 12 membres : l'élément 12 de la liste, comptée à partir de 0":
                         math.comb(24, 13)})'''),
        ("solution", CHECK_13),
        look("pourquoi une coalition de taille moyenne pèse-t-elle si peu, alors que chaque taille pèse $\\frac1n$ en "
             "tout ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB6.14 · harsanyi_dividends
# ---------------------------------------------------------------------------
GIVEN_14 = '''# Four market gardeners (0 to 3) share a stand: the weekly profit v(S) of each coalition (hundreds of euros), read only
TABLE_14 = MappingProxyType({frozenset(members): worth for members, worth in __TABLE_14__})'''

NOTE_14 = (r"Les contrôles ; les valeurs de `v` dans un dictionnaire, taille par taille (`itertools.combinations`) ; "
           r"puis, pour chaque $T$, la somme de $(-1)^{\lvert T\rvert - \lvert S\rvert}v(S)$ sur ses parties. a) "
           r"$(-30 ;\ -30 ;\ -51 ;\ 30)$, comme MB6.2. b) $(4{,}5 ;\ 6 ;\ 3 ;\ 6)$, de somme $19{,}5 = v(N)$. c) "
           r"$(-1 ;\ 1{,}5)$. d) $(1 ;\ 1 ;\ -1)$.")

HINTS_14 = {letter: 'library_hint("harsanyi_dividends")' for letter in "abcd"}

MB6_14 = ex(
    "MB6.14", "programmer les dividendes de Harsanyi d'un jeu donné par sa fonction caractéristique, puis en tirer la "
    "valeur de Shapley et lire ce que dit un dividende négatif.", "fiche §2 ; R4 (parties d'un ensemble) ; Ex MB6.1, MB6.2",
    functions="`harsanyi_dividends`", mymath="attribution.py", note=NOTE_14, given=GIVEN_14,
    body=REMINDER + r"""

Écris `harsanyi_dividends(v, n_players)` (fiche §2), en suivant sa docstring : contrôle les arguments ; appelle `v` une fois par coalition (taille par taille, avec `itertools.combinations`) et garde les valeurs ; puis, pour chaque $T$, la somme alternée sur ses parties ; rends le dictionnaire dans l'ordre de la docstring. Lance le groupe de tests.

**L'usage.** Avec ta fonction :
- a) les hameaux de MB6.2 (`PIPE_2`, cellule de données ; numérotés 0, 1, 2, besoins 30, 51 et 68) : $d_{\{0, 1\}}$, $d_{\{0, 2\}}$, $d_{\{1, 2\}}$, $d_{\{0, 1, 2\}}$ (une liste de 4 nombres, à comparer à ta copie) ;
- b) quatre maraîchers partagent un stand au marché ; le notebook fournit `TABLE_14`, le bénéfice hebdomadaire $v(S)$ de chaque coalition (en centaines d'euros), un dictionnaire indexé par des `frozenset` : leurs valeurs de Shapley par $\varphi_i = \sum_{T \ni i}\frac{d_T}{\lvert T\rvert}$ (une liste de 4 nombres) ;
- c) $d_{\{1, 2\}}$ et $d_{\{0, 1, 3\}}$ du stand (une liste de 2 nombres) ;
- d) le conseil de MB6.1 (`COUNCIL_1` ; A, B, C, D numérotés 0 à 3) : $d_{\{0, 1\}}$, $d_{\{0, 2\}}$, $d_{\{0, 1, 2\}}$ (une liste de 3 nombres).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `harsanyi_dividends` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_harsanyi_dividends_") + [
        ("md", "**L'usage** : les hameaux de MB6.2, le stand des maraîchers, puis le conseil de MB6.1."),
        ("todo", '''answer_MB6_14a = answer_MB6_14b = answer_MB6_14c = answer_MB6_14d = ...
with wbm.attempt("MB6.14"):          # if you call harsanyi_dividends here: ⏳ while it is not written
    answer_MB6_14a = ...  # a) a list of 4 numbers, as computed: the hamlets, d_{0,1}, d_{0,2}, d_{1,2}, d_{0,1,2}
    answer_MB6_14b = ...  # b) a list of 4 numbers, as computed: the Shapley values of the four gardeners
    answer_MB6_14c = ...  # c) a list of 2 numbers, as computed: d_{1,2} and d_{0,1,3} of the stand
    answer_MB6_14d = ...  # d) a list of 3 numbers, as computed: the council, d_{0,1}, d_{0,2}, d_{0,1,2}'''),
        ("check", answers_check("MB6.14", "abcd", hints=HINTS_14)),
        ("solution", '''harsanyi_dividends = mymath.attribution.harsanyi_dividends
needs_14 = PIPE_2["needs"]
hamlets_14 = harsanyi_dividends(lambda S: max((needs_14[i] for i in S), default=0), 3)
answer_MB6_14a = [hamlets_14[frozenset(T)] for T in ((0, 1), (0, 2), (1, 2), (0, 1, 2))]
stand_14 = harsanyi_dividends(lambda S: TABLE_14[S], 4)
answer_MB6_14b = [sum(d / len(T) for T, d in stand_14.items() if i in T) for i in range(4)]
answer_MB6_14c = [stand_14[frozenset({1, 2})], stand_14[frozenset({0, 1, 3})]]
votes_14 = COUNCIL_1["votes"]
council_14 = harsanyi_dividends(lambda S: 1.0 if sum(votes_14[i] for i in S) >= COUNCIL_1["quota"] else 0.0, 4)
answer_MB6_14d = [council_14[frozenset(T)] for T in ((0, 1), (0, 2), (0, 1, 2))]
print("a)", answer_MB6_14a, " b)", np.round(answer_MB6_14b, 6).tolist(), " c)", answer_MB6_14c, " d)", answer_MB6_14d)
print("   les dividendes non nuls du stand :", {tuple(sorted(T)): d for T, d in stand_14.items() if d})
print("   ceux du conseil :", {tuple(sorted(T)): d for T, d in council_14.items() if d})'''),
        ("record", '''import itertools as itertools_14r
from fractions import Fraction as F_14r


def dividends_14r(v, n):
    """The oracle: the alternating sums over the subsets of each coalition, in exact fractions."""
    out = {}
    for size in range(n + 1):
        for T in itertools_14r.combinations(range(n), size):
            out[frozenset(T)] = sum((-1) ** (size - k) * F_14r(str(v(frozenset(S))))
                                    for k in range(size + 1) for S in itertools_14r.combinations(T, k))
    return out


def shapley_14r(v, n):
    """The oracle: the Shapley values averaged over the n! orders (itertools.permutations), exact."""
    phi = [F_14r(0)] * n
    for order in itertools_14r.permutations(range(n)):
        before = frozenset()
        for i in order:
            phi[i] += F_14r(str(v(before | {i}))) - F_14r(str(v(before)))
            before = before | {i}
    return [float(p / math.factorial(n)) for p in phi]


def hamlets_14r(sections):
    needs = list(itertools_14r.accumulate(sections))
    return lambda S: max((needs[i] for i in S), default=0)


pairs_14r = ((0, 1), (0, 2), (1, 2), (0, 1, 2))
d_14r = dividends_14r(hamlets_14r((30, 21, 17)), 3)
wbm.record("MB6.14a", [float(d_14r[frozenset(T)]) for T in pairs_14r], decimals=2,
           mistakes={"les besoins des hameaux sont cumulés (30, 51 et 68) : le coût d'une coalition est le besoin du "
                     "plus éloigné, pas le prix d'un seul tronçon":
                         [float(dividends_14r(lambda S: max(((30, 21, 17)[i] for i in S), default=0), 3)[frozenset(T)])
                          for T in pairs_14r],
                     "le coût d'une coalition est celui de son membre le plus éloigné (un max), pas la somme des besoins":
                         [float(dividends_14r(lambda S: sum((30, 51, 68)[i] for i in S), 3)[frozenset(T)])
                          for T in pairs_14r]})
stand_14r = {frozenset(members): worth for members, worth in __TABLE_14__}
d_stand_14r = dividends_14r(lambda S: stand_14r[S], 4)
wbm.record("MB6.14b", shapley_14r(lambda S: stand_14r[S], 4), decimals=2,
           mistakes={"chaque dividende se partage également entre les membres de T : divise d_T par |T|":
                         [float(sum(d for T, d in d_stand_14r.items() if i in T)) for i in range(4)],
                     "d_T se partage entre les |T| membres de T, pas entre les quatre maraîchers":
                         [float(sum(d / 4 for T, d in d_stand_14r.items() if i in T)) for i in range(4)]})
wbm.record("MB6.14c", [float(d_stand_14r[frozenset({1, 2})]), float(d_stand_14r[frozenset({0, 1, 3})])], decimals=2,
           mistakes={"l'ordre demandé : d_{1,2}, puis d_{0,1,3}": [float(d_stand_14r[frozenset({0, 1, 3})]),
                                                                  float(d_stand_14r[frozenset({1, 2})])],
                     "d_T est la somme alternée sur toutes les parties de T : les trois paires de {0, 1, 3} comptent "
                     "aussi, avec le signe −": [float(d_stand_14r[frozenset({1, 2})]),
                                                float(stand_14r[frozenset({0, 1, 3})] - sum(stand_14r[frozenset({i})]
                                                                                           for i in (0, 1, 3)))]})
council_14r = dividends_14r(lambda S: 1 if sum((8, 6, 3, 1)[i] for i in S) >= 11 else 0, 4)
strict_14r = dividends_14r(lambda S: 1 if sum((8, 6, 3, 1)[i] for i in S) > 11 else 0, 4)
wbm.record("MB6.14d", [float(council_14r[frozenset(T)]) for T in ((0, 1), (0, 2), (0, 1, 2))], decimals=2,
           mistakes={"une motion passe dès que ses voix atteignent le quota (au moins 11), pas seulement quand elles le "
                     "dépassent": [float(strict_14r[frozenset(T)]) for T in ((0, 1), (0, 2), (0, 1, 2))],
                     "l'ordre demandé : d_{0,1}, d_{0,2}, puis d_{0,1,2}":
                         [float(council_14r[frozenset(T)]) for T in ((0, 1, 2), (0, 1), (0, 2))]})'''),
        ("solution", answers_check("MB6.14", "abcd", hints=HINTS_14)),
        look("quel dividende du stand est négatif, et que dit-il des maraîchers 1 et 2 ? Dans le conseil, pourquoi "
             "$d_{\\{0, 1, 2\\}}$ est-il négatif ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB6.15 · line_integral
# ---------------------------------------------------------------------------
CHECK_15 = '''HIDDEN_C15 = __HIDDEN_C15__   # hidden points, and the sub-IDs of the values of F_15 and G_15 there

fields_ok_15 = {}
with checked("MB6.15"):
    for name_c15, field_c15 in (("F_15", F_15), ("G_15", G_15)):
        got_c15 = []
        for point_c15 in HIDDEN_C15["points"]:
            value_c15 = as_floats(call_safely(f"Ex MB6.15 : {name_c15} (appel caché)", field_c15, np.array(point_c15)))
            if value_c15 is None or value_c15.shape != (2,):
                print(f"❌ Ex MB6.15 : {name_c15} rend un vecteur de 2 nombres en un point (x, y), reçu {shown(value_c15)}")
                raise StopCheck
            got_c15 += value_c15.tolist()
        fields_ok_15[name_c15] = passes(HIDDEN_C15["id_" + name_c15], got_c15)
    for name_c15, what_c15 in (("F_15", "le gradient de f(x, y) = x²y² + 5x"), ("G_15", "le champ G(x, y) = (2y, 3x²)")):
        print(f"✅ Ex MB6.15 : {name_c15}, en des points cachés : {what_c15}" if fields_ok_15[name_c15] else
              f"❌ Ex MB6.15 : {name_c15}, en des points cachés : ce n'est pas {what_c15} (MB6.4)")


def hint_15(value):
    """A targeted hint for a) to c): the fields first, then the library."""
    wrong = [name for name in ("F_15", "G_15") if not fields_ok_15.get(name, True)]
    if wrong:
        return f"les intégrales se calculent avec {' et '.join(wrong)} : corrige d'abord la ligne ❌ ci-dessus"
    return library_hint("line_integral")(value)


'''

NOTE_15 = (r"Pour chaque segment, `ts = np.linspace(0, 1, n_sub + 1)`, les produits scalaires `np.dot(field(a + t * (b - "
           r"a)), b - a)` point par point, et les poids $1, 4, 2, \ldots, 4, 1$ fois $\frac h3$. a) $(7 ;\ 7)$. b) $(8 ;\ "
           r"12)$. c) $(9{,}093750 ;\ 9{,}162109 ;\ 9{,}166382)$ : l'écart à $\frac{55}{6}$ diminue.")

MB6_15 = ex(
    "MB6.15", "programmer l'intégrale d'un champ de vecteurs le long d'une ligne brisée par la méthode de Simpson, puis "
    "retrouver MB6.4 et approcher un arc par des cordes.",
    "fiche §4 ; M02a (méthode de Simpson) ; Ex MB6.4", functions="`line_integral`", mymath="attribution.py",
    note=NOTE_15,
    body=REMINDER + r"""

Écris `line_integral(field, points, n_sub=20)` (fiche §4), en suivant sa docstring : contrôle les arguments (des points finis, deux dimensions, au moins deux lignes ; `n_sub` un entier pair $\ge 2$ ; ce que rend `field`) ; pour chaque segment de $\mathbf{a}$ à $\mathbf{b}$, la règle de Simpson (M02a) sur les $n_{\text{sub}} + 1$ valeurs de $t \mapsto \mathbf{F}(\mathbf{a} + t(\mathbf{b} - \mathbf{a}))\cdot(\mathbf{b} - \mathbf{a})$, en appelant `field` point par point ; la somme sur les segments. Lance le groupe de tests.

**L'usage.** Écris d'abord `F_15(p)` et `G_15(p)`, les champs $\mathbf{F} = \nabla f = (2xy^2 + 5,\ 2x^2y)$, $f(x, y) = x^2y^2 + 5x$, et $\mathbf{G}(x, y) = (2y, 3x^2)$ de MB6.4, en un point `p` $= (x, y)$ (la vérification les essaie en des points cachés). Puis, avec ta fonction et les points de `FORCES_4` (cellule de données) :
- a) $\mathbf{F}$ le long du segment $[AB]$, puis de l'escalier $A \to (2, 0) \to B$ (une liste de 2 nombres, à comparer à ta copie) ;
- b) $\mathbf{G}$ le long des deux mêmes chemins (une liste de 2 nombres) ;
- c) $\mathbf{G}$ le long de lignes brisées qui suivent l'arc $\boldsymbol\gamma(t) = (1 + t, t^2)$, avec 4, 16 et 64 segments de même pas en $t$ (une liste de 3 nombres ; l'intégrale de $\mathbf{G}$ le long de l'arc vaut $\frac{55}{6}$).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `line_integral` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_line_integral_") + [
        ("md", "**L'usage** : les deux forces de MB6.4, puis des cordes de plus en plus nombreuses le long d'un arc."),
        ("todo", '''def F_15(p):
    """The field F of MB6.4, the gradient of f(x, y) = x² y² + 5x, at the point p = (x, y)."""
    raise NotImplementedError("F_15 n'est pas encore écrite (04_indices.md si tu bloques)")


def G_15(p):
    """The field G(x, y) = (2y, 3x²) of MB6.4, at the point p = (x, y)."""
    raise NotImplementedError("G_15 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB6_15a = answer_MB6_15b = answer_MB6_15c = ...
with wbm.attempt("MB6.15"):          # your fields and line_integral: ⏳ while they are not written
    answer_MB6_15a = ...  # a) a list of 2 numbers, as computed: F along the segment [AB], then along the staircase
    answer_MB6_15b = ...  # b) a list of 2 numbers, as computed: G along the same two paths
    answer_MB6_15c = ...  # c) a list of 3 numbers, as computed: G along the polylines of 4, 16 and 64 segments on the arc'''),
        ("check", CHECK_15 + answers_check("MB6.15", "abc", hints={letter: "hint_15" for letter in "abc"})),
        ("solution", '''def F_15(p):
    """The field F of MB6.4, the gradient of f(x, y) = x² y² + 5x, at the point p = (x, y)."""
    x, y = p
    return np.array([2 * x * y ** 2 + 5, 2 * x ** 2 * y])


def G_15(p):
    """The field G(x, y) = (2y, 3x²) of MB6.4, at the point p = (x, y)."""
    x, y = p
    return np.array([2 * y, 3 * x ** 2])


line_integral = mymath.attribution.line_integral
segment_15 = [FORCES_4["A"], FORCES_4["B"]]
staircase_15 = [FORCES_4["A"], FORCES_4["corner"], FORCES_4["B"]]
answer_MB6_15a = [line_integral(F_15, segment_15), line_integral(F_15, staircase_15)]
answer_MB6_15b = [line_integral(G_15, segment_15), line_integral(G_15, staircase_15)]
answer_MB6_15c = [line_integral(G_15, [[1 + t, t ** 2] for t in np.linspace(0, 1, n + 1)]) for n in (4, 16, 64)]
print("a)", answer_MB6_15a, " b)", answer_MB6_15b, " c)", np.round(answer_MB6_15c, 6).tolist())
print("   écarts à 55/6 :", [float(f"{55 / 6 - value:.3g}") for value in answer_MB6_15c])'''),
        ("record", '''import sympy as sp_15r

x_15r, y_15r, t_15r = sp_15r.symbols("x y t", real=True)
F_FIELD_15r = (2 * x_15r * y_15r ** 2 + 5, 2 * x_15r ** 2 * y_15r)
G_FIELD_15r = (2 * y_15r, 3 * x_15r ** 2)


def chords_15r(field, vertices):
    """The oracle: the integral of the field along the polyline through the vertices, segment by segment (SymPy,
    exact)."""
    total = 0
    for (ax, ay), (bx, by) in zip(vertices[:-1], vertices[1:]):
        ax, ay, bx, by = (sp_15r.nsimplify(c) for c in (ax, ay, bx, by))
        point = {x_15r: ax + t_15r * (bx - ax), y_15r: ay + t_15r * (by - ay)}
        total += sp_15r.integrate(sp_15r.expand(field[0].subs(point) * (bx - ax) + field[1].subs(point) * (by - ay)),
                                  (t_15r, 0, 1))
    return float(total)


segment_15r, staircase_15r = [(1, 0), (2, 1)], [(1, 0), (2, 0), (2, 1)]
wbm.record("MB6.15a", [chords_15r(F_FIELD_15r, segment_15r), chords_15r(F_FIELD_15r, staircase_15r)], decimals=6,
           mistakes={"le travail va de A vers B : les sommets dans l'ordre A, …, B":
                         [chords_15r(F_FIELD_15r, segment_15r[::-1]), chords_15r(F_FIELD_15r, staircase_15r[::-1])]})
wbm.record("MB6.15b", [chords_15r(G_FIELD_15r, segment_15r), chords_15r(G_FIELD_15r, staircase_15r)], decimals=6,
           mistakes={"le segment d'abord, l'escalier ensuite": [chords_15r(G_FIELD_15r, staircase_15r),
                                                                chords_15r(G_FIELD_15r, segment_15r)],
                     "l'escalier passe par le coin (2, 0) de FORCES_4":
                         [chords_15r(G_FIELD_15r, segment_15r), chords_15r(G_FIELD_15r, [(1, 0), (1, 1), (2, 1)])]})
arcs_15r = [[(1 + sp_15r.Rational(k, n), sp_15r.Rational(k, n) ** 2) for k in range(n + 1)] for n in (4, 16, 64)]
wbm.record("MB6.15c", [chords_15r(G_FIELD_15r, arc) for arc in arcs_15r], decimals=6,
           mistakes={"les sommets de la ligne brisée sont sur l'arc (1 + t, t²), pas sur le segment":
                         [chords_15r(G_FIELD_15r, segment_15r)] * 3,
                     "c) intègre G, le champ qui n'est pas un gradient": [chords_15r(F_FIELD_15r, arc) for arc in arcs_15r]})
HIDDEN_15r = __HIDDEN_C15__                                                  # the hidden points of the check
wbm.record(HIDDEN_15r["id_F_15"], [float(c.subs({x_15r: sp_15r.nsimplify(x), y_15r: sp_15r.nsimplify(y)}))
                                   for x, y in HIDDEN_15r["points"] for c in F_FIELD_15r], decimals=6)
wbm.record(HIDDEN_15r["id_G_15"], [float(c.subs({x_15r: sp_15r.nsimplify(x), y_15r: sp_15r.nsimplify(y)}))
                                   for x, y in HIDDEN_15r["points"] for c in G_FIELD_15r], decimals=6)'''),
        ("solution", CHECK_15 + answers_check("MB6.15", "abc", hints={letter: "hint_15" for letter in "abc"})),
        look("la ligne brisée s'approche-t-elle de $\\frac{55}{6}$ quand les segments se multiplient ? Pourquoi "
             "$\\mathbf{F}$ donne-t-il la même valeur pour toutes ces lignes brisées ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB6.16 · spearman_rho
# ---------------------------------------------------------------------------
GIVEN_16 = '''# The hardness of nine samples of minerals: on Mohs's scale (degrees and half degrees) and by a Vickers test (HV)
MOHS_16 = frozen(__MOHS_16__)
VICKERS_16 = frozen(__VICKERS_16__)'''

NOTE_16 = (r"Les rangs par `np.argsort(x, kind=\"stable\")`, puis la moyenne des places de chaque groupe de valeurs "
           r"égales ; Pearson sur les rangs centrés ; `nan` si une somme de carrés est nulle. a) $\approx 0{,}878669$. "
           r"b) $\approx -0{,}878669$ : $v \mapsto \frac1v$ renverse l'ordre des duretés.")

HINTS_16 = {letter: 'library_hint("spearman_rho")' for letter in "ab"}

MB6_16 = ex(
    "MB6.16", "programmer la corrélation de rangs de Spearman, ex aequo compris, puis comparer deux échelles de dureté.",
    "fiche §6 ; M02c (corrélation de Pearson)", functions="`spearman_rho`", mymath="attribution.py", note=NOTE_16,
    given=GIVEN_16,
    body=REMINDER + r"""

Écris `spearman_rho(x, y)` (fiche §6), en suivant sa docstring : contrôle les arguments ; les rangs de chaque échantillon (`np.argsort`, puis le rang moyen de chaque groupe de valeurs égales, comptés à partir de 1) ; la formule de Pearson sur les rangs centrés ; `nan` quand une somme de carrés est nulle. Lance le groupe de tests.

**L'usage.** Le notebook fournit `MOHS_16` et `VICKERS_16`, la dureté de neuf échantillons de minéraux sur l'échelle de Mohs (des degrés et des demi-degrés, avec un ex aequo) et par un essai de Vickers (en HV). Avec ta fonction :
- a) $\rho_S$(Mohs, Vickers) (un nombre) ;
- b) $\rho_S$(Mohs, $\frac{1}{\text{Vickers}}$) (un nombre).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `spearman_rho` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_spearman_rho_") + [
        ("md", "**L'usage** : deux échelles de dureté des mêmes minéraux."),
        ("todo", '''answer_MB6_16a = answer_MB6_16b = ...
with wbm.attempt("MB6.16"):          # if you call spearman_rho here: ⏳ while it is not written
    answer_MB6_16a = ...  # a) a number, as computed: rho_S(Mohs, Vickers)
    answer_MB6_16b = ...  # b) a number, as computed: rho_S(Mohs, 1 / Vickers)'''),
        ("check", answers_check("MB6.16", "ab", hints=HINTS_16)),
        ("solution", '''spearman_rho = mymath.attribution.spearman_rho
answer_MB6_16a = spearman_rho(MOHS_16, VICKERS_16)
answer_MB6_16b = spearman_rho(MOHS_16, 1 / VICKERS_16)
print("a)", round(answer_MB6_16a, 6), " b)", round(answer_MB6_16b, 6))'''),
        ("record", '''from scipy import stats as stats_16r

mohs_16r, vickers_16r = np.array(__MOHS_16__), np.array(__VICKERS_16__)


def squares_16r(x, y, method="average"):
    """1 - 6 sum d² / (n (n² - 1)) on the ranks of scipy.stats.rankdata (exact only without ties)."""
    d = stats_16r.rankdata(x, method=method) - stats_16r.rankdata(y)
    n = len(x)
    return float(1 - 6 * (d ** 2).sum() / (n * (n * n - 1)))


def ordinal_16r(x, y):
    """The correlation of the ranks given in the order of appearance to the tied values."""
    return float(stats_16r.pearsonr(stats_16r.rankdata(x, method="ordinal"), stats_16r.rankdata(y))[0])


wbm.record("MB6.16a", float(stats_16r.spearmanr(mohs_16r, vickers_16r)[0]), decimals=6,
           mistakes={"avec un ex aequo, 1 − 6Σd²/(n(n² − 1)) n'est qu'une approximation : ρ_S est la corrélation des "
                     "rangs, calculée sur les rangs centrés": squares_16r(mohs_16r, vickers_16r),
                     "les deux minéraux de dureté 3 sont ex aequo : chacun reçoit la moyenne de leurs places (relance les "
                     "tests de spearman_rho)": ordinal_16r(mohs_16r, vickers_16r)})
wbm.record("MB6.16b", float(stats_16r.spearmanr(mohs_16r, 1 / vickers_16r)[0]), decimals=6,
           mistakes={"avec un ex aequo, 1 − 6Σd²/(n(n² − 1)) n'est qu'une approximation : ρ_S est la corrélation des "
                     "rangs, calculée sur les rangs centrés": squares_16r(mohs_16r, 1 / vickers_16r),
                     "les deux minéraux de dureté 3 sont ex aequo : chacun reçoit la moyenne de leurs places (relance les "
                     "tests de spearman_rho)": ordinal_16r(mohs_16r, 1 / vickers_16r)})'''),
        ("solution", answers_check("MB6.16", "ab", hints=HINTS_16)),
        look("pourquoi la formule $1 - \\frac{6\\sum d_i^2}{n(n^2 - 1)}$ n'est-elle ici qu'une approximation ? Pourquoi "
             "b) se déduit-il de a) sans calcul ?"),
    ],
)

PART_A = Part("A", "Ta librairie : les poids des coalitions, les dividendes de Harsanyi, l'intégrale le long d'une ligne "
              "brisée, la corrélation de Spearman",
              "Fiche §1, §2, §4 et §6. Les quatre fonctions de `mymath/attribution.py`, leurs tests, et un usage de "
              "chacune. La cellule de données ci-dessous recopie les données des exercices papier.",
              given=TOOLS + "\n\n\n" + DATA, exercises=[MB6_13, MB6_14, MB6_15, MB6_16])

# ---------------------------------------------------------------------------
# Notebook exercises: predict, experiment, draw (MB6.17 to MB6.19)
# ---------------------------------------------------------------------------
NOTE_17 = (r"Prédictions attendues : a) (A) ; b) (C) ; c) (B) ; d) (B). e) $(0 ;\ 8 ;\ -8 ;\ 16)$ (à $10^{-14}$ près "
           r"pour le premier) : l'aire du triangle vaut 4.")

HINT_17 = '''def hint_17(value):
    """A targeted hint for e): the fields first, then the library."""
    if not globals().get("fields_ok_15", {}).get("F_15", True):
        return "e) se calcule avec F_15 de MB6.15 : corrige-la d'abord"
    return library_hint("line_integral")(value)


'''

MB6_17 = ex(
    "MB6.17", "prédire l'intégrale d'un champ de gradient et d'un champ tournant le long d'une boucle, puis la mesurer.",
    "fiche §4 ; Ex MB6.4, MB6.15", hypothesis=True, note=NOTE_17,
    given='''TRIANGLE_17 = ((1.0, 0.0), (4.0, 1.0), (2.0, 3.0))     # the vertices A, B, C of the triangle''',
    body=r"""Le triangle $A = (1, 0)$, $B = (4, 1)$, $C = (2, 3)$ (`TRIANGLE_17`), et deux champs : $\mathbf{F}$ de MB6.4 (un gradient, ton `F_15`) et le champ tournant $\mathbf{R}(x, y) = (-y, x)$. **Avant d'exécuter quoi que ce soit**, prédis (une lettre chacune) :
- a) l'intégrale de $\mathbf{F}$ le long de la boucle $A \to B \to C \to A$ : (A) 0 ; (B) l'aire du triangle ; (C) elle dépend du triangle choisi ;
- b) celle de $\mathbf{R}$ le long de $A \to B \to C \to A$ : (A) 0 ; (B) l'aire du triangle ; (C) deux fois l'aire du triangle ;
- c) celle de $\mathbf{R}$ le long de $A \to C \to B \to A$ : (A) la même qu'en b) ; (B) l'opposée de b) ; (C) 0 ;
- d) celle de $\mathbf{R}$ quand on fait deux fois le tour $A \to B \to C \to A$ : (A) la même qu'en b) ; (B) le double de b) ; (C) le carré de b).

Puis, une fois tes prédictions écrites et vérifiées, écris `R_17(p)`, le champ tournant en un point `p` $= (x, y)$, et mesure avec `line_integral` :
- e) les quatre intégrales de a) à d), dans cet ordre (une liste de 4 nombres).

La vérification de l'expérience ne s'exécute qu'une fois tes quatre prédictions écrites.""",
    todo='''prediction_MB6_17a = ...  # a) "A", "B" or "C": F along A -> B -> C -> A: (A) 0, (B) the area, (C) it depends on the triangle
prediction_MB6_17b = ...  # b) "A", "B" or "C": R along A -> B -> C -> A: (A) 0, (B) the area, (C) twice the area
prediction_MB6_17c = ...  # c) "A", "B" or "C": R along A -> C -> B -> A: (A) the same as b), (B) the opposite of b), (C) 0
prediction_MB6_17d = ...  # d) "A", "B" or "C": R twice around A -> B -> C -> A: (A) the same as b), (B) twice b), (C) b) squared''',
    check='''for letter, prediction in zip("abcd", [prediction_MB6_17a, prediction_MB6_17b, prediction_MB6_17c,
                                      prediction_MB6_17d]):
    if filled(prediction) and not isinstance(prediction, str):      # a number, a list...: not yet a prediction
        print(f'❌ Ex MB6.17{letter} : une prédiction est une lettre, "A", "B" ou "C", reçu {shown(prediction)}')
    else:
        wbm.check(f"MB6.17{letter}", prediction)''',
    record='''wbm.record("MB6.17a", "A", prediction=True,
           mistakes={"F est un gradient : que dit le théorème du gradient (fiche §4) pour un chemin qui revient à son "
                     "point de départ ?": {"B", "C"}})
wbm.record("MB6.17b", "C", prediction=True,
           mistakes={"R n'est pas un gradient (ses dérivées croisées diffèrent) : calcule R(a + t(b − a)) · (b − a) sur "
                     "un côté du triangle, puis somme sur les trois côtés (fiche §4)": {"A", "B"}})
wbm.record("MB6.17c", "B", prediction=True,
           mistakes={"relis ce que la fiche §4 dit d'un chemin parcouru dans l'autre sens, pour un champ quelconque":
                         {"A", "C"}})
wbm.record("MB6.17d", "B", prediction=True,
           mistakes={"relis comment l'intégrale le long d'une ligne brisée se décompose sur ses segments (fiche §4)":
                         {"A", "C"}})''',
    after=[
        ("md", "**L'expérience.** Écris-la une fois tes quatre prédictions vérifiées ; sa vérification ne s'exécute qu'à "
               "cette condition."),
        ("todo", '''def R_17(p):
    """The rotating field R(x, y) = (-y, x), at the point p = (x, y)."""
    raise NotImplementedError("R_17 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB6_17e = ...
with wbm.attempt("MB6.17"):          # your R_17, F_15 and line_integral: ⏳ while they are not written
    answer_MB6_17e = ...  # e) a list of 4 numbers, as computed: the integrals of a), b), c) and d), with line_integral'''),
        ("check", HINT_17 + guarded('check_answer("MB6.17e", answer_MB6_17e, hint=hint_17)',
                                    [f"prediction_MB6_17{letter}" for letter in "abcd"],
                                    "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", '''def R_17(p):
    """The rotating field R(x, y) = (-y, x), at the point p = (x, y)."""
    x, y = p
    return np.array([-y, x])


line_integral = mymath.attribution.line_integral
A_17, B_17, C_17 = TRIANGLE_17
answer_MB6_17e = [line_integral(F_15, [A_17, B_17, C_17, A_17]), line_integral(R_17, [A_17, B_17, C_17, A_17]),
                  line_integral(R_17, [A_17, C_17, B_17, A_17]),
                  line_integral(R_17, [A_17, B_17, C_17, A_17, B_17, C_17, A_17])]
area_17 = abs((B_17[0] - A_17[0]) * (C_17[1] - A_17[1]) - (B_17[1] - A_17[1]) * (C_17[0] - A_17[0])) / 2
print("e)", np.round(answer_MB6_17e, 9).tolist(), " l'aire du triangle :", area_17)'''),
        ("record", '''from fractions import Fraction as F_17r

triangle_17r = [(1, 0), (4, 1), (2, 3)]


def rotating_17r(vertices, sign=1):
    """The oracle: the integral of sign (-y, x) along the polyline, exactly: a1 b2 - a2 b1 on each segment."""
    return float(sum(sign * (F_17r(a[0]) * b[1] - F_17r(a[1]) * b[0]) for a, b in zip(vertices[:-1], vertices[1:])))


def potential_17r(x, y):
    return F_17r(x) ** 2 * F_17r(y) ** 2 + 5 * F_17r(x)


loop_17r = triangle_17r + triangle_17r[:1]
back_17r = [triangle_17r[0], triangle_17r[2], triangle_17r[1], triangle_17r[0]]
twice_17r = loop_17r + loop_17r[1:]
open_17r = [triangle_17r, back_17r[:3], loop_17r + loop_17r[1:3]]
wbm.record("MB6.17e", [float(potential_17r(*loop_17r[-1]) - potential_17r(*loop_17r[0])), rotating_17r(loop_17r),
                       rotating_17r(back_17r), rotating_17r(twice_17r)], decimals=6,
           mistakes={"une boucle revient à son point de départ : chaque liste de sommets finit par A":
                         [float(potential_17r(*triangle_17r[-1]) - potential_17r(*triangle_17r[0]))]
                         + [rotating_17r(path) for path in open_17r],
                     "le champ tournant est R(x, y) = (−y, x)": [0.0] + [rotating_17r(path, -1)
                                                                        for path in (loop_17r, back_17r, twice_17r)]})'''),
        ("solution", HINT_17 + 'check_answer("MB6.17e", answer_MB6_17e, hint=hint_17)'),
        look("l'aire du triangle vaut-elle ce que tu pensais ? Qu'est-ce qui, dans $\\mathbf{R}$, tourne avec la "
             "boucle ? Une boucle d'intégrale nulle suffirait-elle à prouver qu'un champ est un gradient ?",
             " (après l'expérience)"),
    ],
)

# ---------------------------------------------------------------------------
# MB6.18 · the marginal and the conditional mean of a reservoir
# ---------------------------------------------------------------------------
GIVEN_18 = '''# The reservoir in summer: the temperature T of the water (°C) and the phosphorus U (µg/L), a Gaussian couple of
# correlation rho; 300 000 draws for each rho (seed 7918), read only
def draws_18(rho, size, rng):
    """size draws of the couple (T, U): T ~ N(22, 3²), U ~ N(70, 8²), of correlation rho (two float arrays)."""
    pairs = rng.multivariate_normal([22.0, 70.0], [[9.0, 24.0 * rho], [24.0 * rho, 64.0]], size=size)
    return pairs[:, 0], pairs[:, 1]


_rng_18 = np.random.default_rng(7918)
SAMPLES_18 = MappingProxyType({rho: tuple(frozen(column) for column in draws_18(rho, 300_000, _rng_18))
                               for rho in (0.0, 0.5, 0.9)})          # rho: (T, U)
del _rng_18


def growth_18(T, U):
    """The relative growth of the algae, exp(0.1 (T - 22) + 0.05 (U - 70)) (numbers or arrays)."""
    return np.exp(0.1 * (np.asarray(T) - 22) + 0.05 * (np.asarray(U) - 70))'''

NOTE_18 = (r"a) $\operatorname{PD}(26) = e^{0{,}4 + 0{,}08} \approx 1{,}616074$ ; $M(26) \approx 1{,}616074$, "
           r"$2{,}068175$, $2{,}447825$. b) La fenêtre garde environ 8 200 points pour chaque $\rho$ : les estimations de "
           r"$\operatorname{PD}$ sont à $0{,}002$ près, celles de $M$ à $0{,}012$ près.")

MB6_18 = ex(
    "MB6.18", "comparer la moyenne marginale (la dépendance partielle) et la moyenne conditionnelle d'une même fonction de "
    "deux mesures corrélées, par les formules gaussiennes et par simulation.",
    "fiche §3 ; M25a (loi conditionnelle d'un couple gaussien), M11 (dispersion d'une moyenne) ; Ex MB6.3",
    note=NOTE_18, given=GIVEN_18,
    body=r"""En été, la température de l'eau $T$ (°C) et la concentration en phosphore $U$ (µg/L) d'un réservoir d'eau forment un couple gaussien : $T \sim \mathcal{N}(22, 3^2)$, $U \sim \mathcal{N}(70, 8^2)$, de corrélation $\rho$. Une fonction écrite donne la croissance relative des algues : $f(T, U) = \exp\big(0{,}1\,(T - 22) + 0{,}05\,(U - 70)\big)$ (`growth_18`). On fixe $T = 26$. Pour $\rho = 0$ ; $0{,}5$ et $0{,}9$ :
- a) calcule par les formules $\operatorname{PD}(26) = \mathbb{E}[f(26, U)]$ et $M(26) = \mathbb{E}[f(T, U) \mid T = 26]$ (une liste de 4 nombres : $\operatorname{PD}(26)$, puis $M(26)$ pour les trois $\rho$) ; tu peux utiliser $\mathbb{E}[e^{cZ}] = e^{c\mu + c^2\sigma^2/2}$ pour $Z \sim \mathcal{N}(\mu, \sigma^2)$ ;
- b) le notebook fournit `SAMPLES_18`, 300 000 couples tirés pour chaque $\rho$ (`SAMPLES_18[rho]` rend les tableaux `T` et `U`) ; estime $\operatorname{PD}(26)$ par la moyenne des $f(26, U_i)$, et $M(26)$ par la moyenne des $f(T_i, U_i)$ sur les points où $\lvert T_i - 26\rvert \le 0{,}25$ (une liste de 6 nombres : pour chaque $\rho$, l'estimation de $\operatorname{PD}$ puis celle de $M$).""",
    todo='''answer_MB6_18a = ...  # a) a list of 4 numbers, by the formulas: PD(26), then M(26) for rho = 0, 0.5, 0.9
answer_MB6_18b = ...  # b) a list of 6 numbers, as computed on SAMPLES_18: for each rho, the estimate of PD(26), then of M(26)''',
    check=answers_check("MB6.18", "ab"),
    solution='''def conditional_18(rho, v=26.0):
    """M(v) = E[f(T, U) | T = v]: given T = v, U ~ N(70 + rho (8/3)(v - 22), 64 (1 - rho²)), and E[e^{cZ}]."""
    mean_u, var_u = 70 + rho * 8 / 3 * (v - 22), 64 * (1 - rho ** 2)
    return math.exp(0.1 * (v - 22) + 0.05 * (mean_u - 70) + 0.05 ** 2 * var_u / 2)


answer_MB6_18a = [math.exp(0.1 * 4 + 0.05 ** 2 * 64 / 2)] + [conditional_18(rho) for rho in (0.0, 0.5, 0.9)]
answer_MB6_18b = []
for rho in (0.0, 0.5, 0.9):
    T_18, U_18 = SAMPLES_18[rho]
    window_18 = np.abs(T_18 - 26) <= 0.25
    answer_MB6_18b += [float(growth_18(26.0, U_18).mean()), float(growth_18(T_18[window_18], U_18[window_18]).mean())]
    print(f"rho = {rho} : {int(window_18.sum())} points dans la fenêtre ;",
          f"PD {answer_MB6_18b[-2]:.4f} (formule {answer_MB6_18a[0]:.4f}),",
          f"M {answer_MB6_18b[-1]:.4f} (formule {conditional_18(rho):.4f})")
print("a)", np.round(answer_MB6_18a, 6).tolist())''',
    record='''from scipy import integrate as integrate_18r
from scipy import stats as stats_18r


def conditional_18r(rho, v=26.0, half=True, slope=8 / 3):
    """The oracle: E[f(v, U)] under the law of U given T = v, by scipy.integrate.quad; half=False: c² sigma² instead of
    c² sigma²/2 (the classic error); slope: the slope of E[U | T = v] (rho sigma_U/sigma_T)."""
    mean_u, sd_u = 70 + rho * slope * (v - 22), 8 * math.sqrt(1 - rho ** 2)
    if not half:
        return math.exp(0.1 * (v - 22) + 0.05 * (mean_u - 70) + 0.05 ** 2 * sd_u ** 2)
    return integrate_18r.quad(lambda u: math.exp(0.1 * (v - 22) + 0.05 * (u - 70)) * stats_18r.norm.pdf(u, mean_u, sd_u),
                              mean_u - 14 * sd_u, mean_u + 14 * sd_u)[0]


rhos_18r = (0.0, 0.5, 0.9)
wbm.record("MB6.18a", [conditional_18r(0.0)] + [conditional_18r(rho) for rho in rhos_18r], decimals=6,
           mistakes={"E[e^{cZ}] = e^{cμ + c²σ²/2} : le terme de la variance est divisé par 2":
                         [conditional_18r(0.0, half=False)] + [conditional_18r(rho, half=False) for rho in rhos_18r],
                     "sachant T = 26, U a la moyenne 70 + ρ (σ_U/σ_T)(26 − 22) : la pente est ρ σ_U/σ_T, pas ρ σ_T/σ_U":
                         [conditional_18r(0.0)] + [conditional_18r(rho, slope=3 / 8) for rho in rhos_18r]})
rng_18r = np.random.default_rng(7918)                                       # the same draws as SAMPLES_18
pd_18r, m_18r, all_18r = [], [], []
for rho in rhos_18r:
    pairs_18r = rng_18r.multivariate_normal([22.0, 70.0], [[9.0, 24.0 * rho], [24.0 * rho, 64.0]], size=300_000)
    t_18r, u_18r = pairs_18r[:, 0], pairs_18r[:, 1]
    keep_18r = np.abs(t_18r - 26) <= 0.25
    pd_18r.append(float(np.exp(0.4 + 0.05 * (u_18r - 70)).mean()))
    m_18r.append(float(np.exp(0.1 * (t_18r[keep_18r] - 22) + 0.05 * (u_18r[keep_18r] - 70)).mean()))
    all_18r.append(float(np.exp(0.1 * (t_18r - 22) + 0.05 * (u_18r - 70)).mean()))
wbm.record("MB6.18b", [v for pair in zip(pd_18r, m_18r) for v in pair], decimals=7,
           mistakes={"la moyenne conditionnelle se calcule sur les seuls points de la fenêtre |T − 26| ≤ 0,25":
                         [v for pair in zip(pd_18r, all_18r) for v in pair],
                     "la moyenne marginale fixe T à 26 dans f : la moyenne des f(26, U_i), sur tous les points":
                         [v for pair in zip(all_18r, m_18r) for v in pair]})''',
    after=[
        ("solution", answers_check("MB6.18", "ab")),
        look("pour quel $\\rho$ les deux moyennes sont-elles égales ? Pourquoi l'estimation de $M$ est-elle plus "
             "dispersée que celle de $\\operatorname{PD}$ ? Que deviendrait-elle avec une fenêtre dix fois plus étroite ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB6.19 · two paths in a landscape
# ---------------------------------------------------------------------------
GIVEN_19 = '''# The landscape of the exercise, its gradient, and the two ends of the paths
A_19, B_19 = (-2.5, -1.0), (2.0, 2.0)
CORNERS_19 = ((0.0, -2.0), (2.5, 0.0))            # the two inner vertices of the polyline A_19 -> ... -> B_19


def f_19(x, y):
    """3 e^{-((x - 1)² + (y - 1)²)} - 2 e^{-((x + 1)² + y²)/2} + 0.2 x (numbers or arrays)."""
    return 3 * np.exp(-((x - 1) ** 2 + (y - 1) ** 2)) - 2 * np.exp(-((x + 1) ** 2 + y ** 2) / 2) + 0.2 * x


def grad_19(p):
    """The gradient of f_19 at the point p = (x, y)."""
    x, y = p
    bump, hollow = np.exp(-((x - 1) ** 2 + (y - 1) ** 2)), np.exp(-((x + 1) ** 2 + y ** 2) / 2)
    return np.array([-6 * (x - 1) * bump + 2 * (x + 1) * hollow + 0.2, -6 * (y - 1) * bump + 2 * y * hollow])'''

CHECK_19 = r'''import matplotlib.contour as contour_c19

_SEGMENT_NAME_C19 = re.compile(r"segment|droit|direct", re.IGNORECASE)
_POLYLINE_NAME_C19 = re.compile(r"bris|poly|détour|detour|coud|zig", re.IGNORECASE)
PATHS_C19 = (("segment", np.array([A_19, B_19])), ("ligne brisée", np.array([A_19, *CORNERS_19, B_19])))


def distance_c19(points, vertices):
    """The distance of each point to the polyline through the vertices."""
    best = np.full(len(points), np.inf)
    for a, b in zip(vertices[:-1], vertices[1:]):
        t = np.clip(((points - a) @ (b - a)) / ((b - a) @ (b - a)), 0, 1)
        best = np.minimum(best, np.linalg.norm(points - (a + t[:, None] * (b - a)), axis=1))
    return best


def follows_c19(line, vertices):
    """True when the drawn line lies on the polyline and passes through each of its vertices."""
    points = np.column_stack([np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)])
    if points.ndim != 2 or len(points) < 2 or not np.all(np.isfinite(points)):
        return False
    return bool(distance_c19(points, vertices).max() < 1e-6
                and all(np.linalg.norm(points - v, axis=1).min() < 1e-6 for v in vertices))


def point_at_c19(vertices, length):
    """The point of the polyline at the given length from its start, and the vertices of its beginning up to it."""
    for k, (a, b) in enumerate(zip(vertices[:-1], vertices[1:])):
        step = float(np.linalg.norm(b - a))
        if length <= step + 1e-12 or k == len(vertices) - 2:
            return a + min(length / step, 1.0) * (b - a), vertices[:k + 1]
        length -= step


def cumul_why_c19(curve, vertices, values):
    """What is wrong in one curve of ax_cum (French phrases), against the integrals of the reference along the
    beginning of the path."""
    lengths = np.asarray(curve.get_xdata(), dtype=float)
    total = float(np.linalg.norm(np.diff(vertices, axis=0), axis=1).sum())
    if abs(lengths[0]) > 1e-9 or np.any(np.diff(lengths) < -1e-12) or abs(lengths[-1] - total) > 1e-6 * total:
        return ["en abscisse, la longueur parcourue depuis A_19 : de 0 à la longueur du chemin, croissante"]
    if abs(values[0]) > 1e-9:
        return ["le cumul vaut 0 au départ, en A_19"]
    ends = np.concatenate([[0.0], np.cumsum(np.linalg.norm(np.diff(vertices, axis=0), axis=1))])
    if any(np.count_nonzero((lengths >= lo - 1e-9) & (lengths <= hi + 1e-9)) < 50 for lo, hi in zip(ends, ends[1:])):
        return ["trop peu de points : il en faut au moins 50 sur chaque segment du chemin, ses deux bouts compris"]
    picks =np.unique(np.linspace(0, len(values) - 1, min(len(values), 60)).astype(int))
    expected = []
    for k in picks:
        point, start = point_at_c19(vertices, float(lengths[k]))
        expected.append(0.0 if lengths[k] == 0 else ref_att.line_integral(grad_19, np.vstack([start, point])))
    if np.abs(values[picks] - np.array(expected)).max() > 0.005:
        return ["les cumuls ne sont pas l'intégrale de grad_19 depuis A_19 jusqu'au point courant, à 0,005 près "
                "(line_integral sur le début du chemin, dont les sommets précédents, jusqu'au point courant)"]
    return []


with checked("MB6.19"):
    results_19 = []
    report_19 = reporter(results_19, stop=False)
    fig_19, (ax_map_19, ax_cum_19, spare_19) = plt.subplots(1, 3, figsize=(12, 4.5))   # spare_19: the current axes
    try:
        drawn_19 = []
        opened_19 = drawn(lambda: drawn_19.append(call_safely("Ex MB6.19 : draw_19", draw_19, ax_map_19, ax_cum_19)))
        cumuls_19 = drawn_19[0]
        arrays_19 = None
        if isinstance(cumuls_19, (list, tuple)) and len(cumuls_19) == 2:
            arrays_19 = [as_floats(c) for c in cumuls_19]
        if arrays_19 is None or any(a is None or a.ndim != 1 or a.size < 20 or not np.all(np.isfinite(a))
                                    for a in arrays_19):
            print("❌ Ex MB6.19 : draw_19 doit rendre les deux tableaux de cumuls tracés (le segment, puis la ligne "
                  f"brisée), chacun d'au moins 20 nombres finis, reçu {shown(cumuls_19)}")
            raise StopCheck
        sets_c19 = [c for c in ax_map_19.collections if isinstance(c, contour_c19.ContourSet)]
        spans_c19 = []
        for cs_c19 in sets_c19:
            vertices_c19 = [p.vertices for p in cs_c19.get_paths() if len(p.vertices)]
            if vertices_c19:
                stacked_c19 = np.vstack(vertices_c19)
                spans_c19.append((stacked_c19.min(axis=0), stacked_c19.max(axis=0)))
        report_19(any(lo.min() >= -3.05 and hi.max() <= 3.05 and (hi - lo).min() >= 4 for lo, hi in spans_c19),
                  "les lignes de niveau de f_19 sur [−3, 3]²",
                  "il faut les lignes de niveau de f_19 sur [−3, 3]², par ax_map.contour (une grille np.meshgrid)")
        lines_c19 = [next((line for line in ax_map_19.lines if follows_c19(line, v)), None) for _, v in PATHS_C19]
        report_19(all(line is not None for line in lines_c19), "les deux chemins, de A_19 à B_19",
                  "il faut tracer dans ax_map le segment de A_19 à B_19 et la ligne brisée A_19 → (0, −2) → (2,5 ; 0) "
                  "→ B_19, chacun par ses sommets")
        legend_c19 = ax_map_19.get_legend()
        named_c19 = (legend_c19 is not None and lines_c19[0] is not None and lines_c19[1] is not None
                     and bool(_SEGMENT_NAME_C19.search(lines_c19[0].get_label()))
                     and bool(_POLYLINE_NAME_C19.search(lines_c19[1].get_label())))
        report_19(named_c19, "une légende qui nomme chaque chemin",
                  "il faut une légende (label=…, puis ax_map.legend()) qui nomme chaque chemin : « segment » et "
                  "« ligne brisée »")
        problems_c19 = []
        for (name_c19, vertices_c19), values_c19 in zip(PATHS_C19, arrays_19):
            curve_c19 = next((line for line in ax_cum_19.lines
                              if np.asarray(line.get_ydata(), dtype=float).shape == values_c19.shape
                              and np.allclose(np.asarray(line.get_ydata(), dtype=float), values_c19, rtol=0, atol=1e-12)),
                             None)
            if curve_c19 is None:
                problems_c19.append(f"le tableau rendu pour le {name_c19} doit être tracé dans ax_cum")
            else:
                problems_c19 += [f"{name_c19} : {why}" for why in cumul_why_c19(curve_c19, vertices_c19, values_c19)]
        if not ax_cum_19.get_xlabel() or not ax_cum_19.get_ylabel():
            problems_c19.append("il faut des noms d'axes dans ax_cum")
        report_19(not problems_c19, "les deux cumuls, en fonction de la longueur parcourue, avec des noms d'axes",
                  "ax_cum : " + " ; ".join(problems_c19))
        elsewhere_19 = bool(spare_19.lines or spare_19.collections or spare_19.get_legend())
        report_19(not opened_19 and not elsewhere_19, "draw_19 dessine dans les axes reçus",
                  "draw_19 doit dessiner dans les axes reçus (ax_map.plot, ax_cum.plot…), sans ouvrir de figure ni "
                  "dessiner dans l'axe courant (plt.plot, plt.legend…)")
        fig_19.delaxes(spare_19)
    except BaseException:
        plt.close(fig_19)
        raise
    fig_19.tight_layout()
    plt.show()
    verdict("MB6.19", all(results_19) and len(results_19) == 5, "ta figure est juste : les lignes de niveau, les deux "
            "chemins, la légende et les deux cumuls.", "relis les lignes ❌ ci-dessus.")

check_answer("MB6.19a", answer_MB6_19a)
if not filled(answer_MB6_19b):
    print("⏳ Ex MB6.19b : pas encore fait.")
elif not results_19 or not all(results_19):
    print("❌ Ex MB6.19b : b) se lit sur les cumuls de draw_19 : corrige d'abord ta figure (lignes ❌ ci-dessus)")
else:
    mine_19 = as_floats(answer_MB6_19b)
    peaks_19 = [float(np.max(a)) for a in arrays_19]
    if mine_19 is None or mine_19.shape != (2,):
        print(f"❌ Ex MB6.19b : une liste de 2 nombres, reçu {shown(answer_MB6_19b)}")
    elif not np.allclose(mine_19, peaks_19, rtol=1e-9, atol=1e-12):
        print("❌ Ex MB6.19b : b) relève le plus grand cumul de chacun des deux tableaux que rend draw_19 (le segment, "
              "puis la ligne brisée), sans l'arrondir")
    elif not passes("MB6.19b", peaks_19):
        print("❌ Ex MB6.19b : tes plus grands cumuls sont loin de ceux des deux chemins : répartis tes points sur toute "
              "la longueur de chaque segment (np.linspace), pour ne pas manquer le haut de la bosse")
    else:
        print("✅ Ex MB6.19b : les plus grands cumuls de tes deux tableaux, assez denses pour trouver les sommets.")'''

NOTE_19 = (r"a) $f(B) - f(A) \approx 1{,}696822$. b) Avec 100 points par segment : $\approx 3{,}694$ (le segment passe "
           r"près du sommet de la bosse) et $\approx 2{,}014$ (la ligne brisée la contourne).")

MB6_19 = ex(
    "MB6.19", "tracer les lignes de niveau d'une fonction, deux chemins entre les mêmes points, et l'intégrale du "
    "gradient cumulée le long de chacun.", "fiche §4 ; M05b (lignes de niveau) ; Ex MB6.15", note=NOTE_19,
    given=GIVEN_19,
    body=r"""Le notebook fournit `f_19(x, y)` $= 3e^{-((x - 1)^2 + (y - 1)^2)} - 2e^{-((x + 1)^2 + y^2)/2} + 0{,}2\,x$, son gradient `grad_19`, les extrémités $A$ = `A_19` $= (-2{,}5 ;\ -1)$ et $B$ = `B_19` $= (2, 2)$, et `CORNERS_19`. Écris `draw_19(ax_map, ax_cum)`, qui trace :
- dans `ax_map`, les lignes de niveau de $f$ sur $[-3, 3]^2$ (`ax_map.contour`) et deux chemins de $A$ à $B$, le segment et la ligne brisée $A \to (0, -2) \to (2{,}5 ;\ 0) \to B$, chacun par ses sommets, avec une légende qui nomme chaque chemin (« segment » et « ligne brisée ») ;
- dans `ax_cum`, pour chaque chemin, l'intégrale du gradient de $f$ depuis $A$ jusqu'au point courant (avec `line_integral` sur le début du chemin), en fonction de la longueur parcourue depuis $A$ (au moins 50 points par segment), avec des noms d'axes ;

et qui rend les deux tableaux de cumuls tracés (le segment, puis la ligne brisée). La fonction dessine dans les axes reçus, sans ouvrir de figure. La vérification l'appelle, affiche la figure, et compare tes cumuls à ceux de `line_integral` de la référence, à $0{,}005$ près. Relève :
- a) $f(B) - f(A)$ (un nombre) ;
- b) le plus grand cumul le long du segment, puis le long de la ligne brisée (une liste de 2 nombres, les maximums de tes deux tableaux).""",
    todo='''def draw_19(ax_map, ax_cum):
    """In ax_map: the level lines of f_19 on [-3, 3]², the segment from A_19 to B_19 and the polyline A_19 -> (0, -2)
    -> (2.5, 0) -> B_19, by their vertices, with a legend that names each path. In ax_cum: for each path, the integral
    of grad_19 from A_19 to the current point (line_integral on the beginning of the path) against the length travelled
    from A_19, with axis labels. Returns the two arrays of cumulative integrals drawn (the segment's, then the
    polyline's). Opens no figure."""
    raise NotImplementedError("draw_19 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB6_19a = answer_MB6_19b = ...
with wbm.attempt("MB6.19"):          # your draw_19 and line_integral: ⏳ while they are not written
    answer_MB6_19a = ...  # a) a number: f(B) - f(A)
    answer_MB6_19b = ...  # b) a list of 2 numbers, as computed: the largest cumulative integral along the segment, then along the polyline''',
    check=CHECK_19,
    solution='''def draw_19(ax_map, ax_cum):
    """In ax_map: the level lines of f_19 on [-3, 3]², the segment from A_19 to B_19 and the polyline A_19 -> (0, -2)
    -> (2.5, 0) -> B_19, by their vertices, with a legend that names each path. In ax_cum: for each path, the integral
    of grad_19 from A_19 to the current point (line_integral on the beginning of the path) against the length travelled
    from A_19, with axis labels. Returns the two arrays of cumulative integrals drawn (the segment's, then the
    polyline's). Opens no figure."""
    grid = np.linspace(-3, 3, 241)
    X, Y = np.meshgrid(grid, grid)
    levels = ax_map.contour(X, Y, f_19(X, Y), levels=16, cmap="coolwarm", linewidths=0.8)
    ax_map.clabel(levels, fontsize=6)
    cumuls = []
    for name, vertices in (("segment", [A_19, B_19]), ("ligne brisée", [A_19, *CORNERS_19, B_19])):
        vertices = np.array(vertices, dtype=float)
        ax_map.plot(vertices[:, 0], vertices[:, 1], "o-", lw=1.8, label=name)
        lengths, values, travelled = [0.0], [0.0], 0.0
        for k in range(len(vertices) - 1):
            a, b = vertices[k], vertices[k + 1]
            for t in np.linspace(0, 1, 101)[1:]:
                lengths.append(travelled + t * float(np.linalg.norm(b - a)))
                values.append(mymath.attribution.line_integral(grad_19, np.vstack([vertices[:k + 1], a + t * (b - a)])))
            travelled += float(np.linalg.norm(b - a))
        ax_cum.plot(lengths, values, lw=1.8, label=name)
        cumuls.append(np.array(values))
    ax_map.set_aspect("equal")
    ax_map.set_xlabel("x")
    ax_map.set_ylabel("y")
    ax_map.legend(fontsize=8)
    ax_cum.set_xlabel("longueur parcourue depuis A")
    ax_cum.set_ylabel("intégrale du gradient depuis A")
    ax_cum.legend(fontsize=8)
    return cumuls


fig_19s, axes_19s = plt.subplots(1, 2, figsize=(11, 4.5))
cumuls_19s = draw_19(*axes_19s)
plt.show()
answer_MB6_19a = float(f_19(*B_19) - f_19(*A_19))
answer_MB6_19b = [float(np.max(c)) for c in cumuls_19s]
print("a)", round(answer_MB6_19a, 6), " b)", np.round(answer_MB6_19b, 4).tolist(),
      " fins des deux cumuls :", [round(float(c[-1]), 4) for c in cumuls_19s])''',
    record='''def landscape_19r(x, y):
    """The oracle: f_19 written again."""
    return 3 * np.exp(-((x - 1) ** 2 + (y - 1) ** 2)) - 2 * np.exp(-((x + 1) ** 2 + y ** 2) / 2) + 0.2 * x


ends_19r = (np.array([-2.5, -1.0]), np.array([2.0, 2.0]))
wbm.record("MB6.19a", float(landscape_19r(*ends_19r[1]) - landscape_19r(*ends_19r[0])), decimals=4,
           mistakes={"le travail du gradient va de A vers B : f(B) − f(A), pas f(A) − f(B)":
                         float(landscape_19r(*ends_19r[0]) - landscape_19r(*ends_19r[1]))})
peaks_19r = []
for vertices_19r in ([ends_19r[0], ends_19r[1]], [ends_19r[0], np.array([0.0, -2.0]), np.array([2.5, 0.0]), ends_19r[1]]):
    t_19r = np.linspace(0, 1, 20_001)
    peaks_19r.append(max(float((landscape_19r(*(a + t_19r[:, None] * (b - a)).T) - landscape_19r(*ends_19r[0])).max())
                         for a, b in zip(vertices_19r[:-1], vertices_19r[1:])))
wbm.record("MB6.19b", peaks_19r, decimals=1)       # by the gradient theorem, at 1 decimal (the learner's points vary)''',
    after=[
        ("solution", CHECK_19),
        look("où chaque chemin monte-t-il et descend-il ? Pourquoi les deux cumuls finissent-ils au même nombre ?"),
    ],
)

PART_B = Part("B", "Prédire, mesurer, dessiner",
              "Fiche §3 et §4. Un champ de gradient et un champ tournant le long d'une boucle ; la moyenne marginale et "
              "la moyenne conditionnelle de deux mesures corrélées ; deux chemins dans un paysage.",
              exercises=[MB6_17, MB6_18, MB6_19])

# ---------------------------------------------------------------------------
# Notebook exercises: debug, test (MB6.20, MB6.21)
# ---------------------------------------------------------------------------
GIVEN_20 = '''# The colleague's code
def weights_bad(n):
    """The weights w(s) of the Shapley value of n players, s = 0, ..., n - 1 (floats)."""
    return [math.factorial(s) * math.factorial(n - 1 - s) / math.factorial(n - 1) for s in range(n)]


def ranks_bad(x):
    """The ranks of the values of x, from 1 (the smallest), tied values sharing the mean of the places they occupy."""
    x = np.asarray(x, dtype=float)
    order = np.argsort(x, kind="stable")
    ranks = np.empty(len(x))
    ranks[order] = np.arange(1, len(x) + 1)
    return ranks


def lerp_bad(a, b, t):
    """The value at t of the linear interpolation between a (at t = 0) and b (at t = 1), to read a value between two
    cells of a grid."""
    return (1 - t) * b + t * a


X_20 = frozen(__X_20__)                # two samples with ties (b)
Y_20 = frozen(__Y_20__)

# The colleague's checks: all pass
print("(1)", weights_bad(1) == [1.0], "(attendu True : un joueur seul reçoit tout)")
print("(2)", ranks_bad([2.7, 0.4, 1.9, 3.6]).tolist() == [3.0, 1.0, 2.0, 4.0], "(attendu True : des valeurs toutes "
      "différentes)")
print("(3)", lerp_bad(4.0, 10.0, 0.5) == 7.0, "(attendu True : au milieu, la moyenne des deux valeurs)")'''

CHECK_20 = '''CASES_C20 = __CASES_C20__   # the hidden cases, and the sub-IDs of the values expected

results_20, parts_20 = [], []
MYMATH_C20 = list(getattr(mymath, "__path__", [])) + list(getattr(REF, "__path__", []))   # the folders of mymath
TWINS_C20 = set()                                  # the functions of attribution.py (yours, the reference's)
for _folder_c20 in MYMATH_C20:
    TWINS_C20 |= code_keys_of_file(os.path.join(_folder_c20, "attribution.py"))


def report_20(ok, success, failure):
    results_20.append(bool(ok))
    print(("✅ " + success) if ok else ("❌ " + failure))


def call_20(part, name, function, *args):
    """function(*args), without mymath; an error of the learner's code becomes one ❌ line that names the function."""
    try:
        with code_from(MYMATH_C20, twins=TWINS_C20) as seen:
            got = function(*args)
    except (NotImplementedError, MymathMissingError):
        raise
    except Exception as exc:  # noqa: BLE001 - the learner's error, reported with the name of the function
        report_20(False, "", f"({part}) {name} : ton code lève {type(exc).__name__} : {str(exc)[:160]}")
        parts_20.append(part)
        raise StopCheck from None
    if seen:
        report_20(False, "", f"({part}) {name} appelle mymath ({seen[0]}) : l'énoncé demande la correction sans mymath, "
                  "en corrigeant le code du collègue")
        parts_20.append(part)
        raise StopCheck
    return got


with checked("MB6.20"):                                       # (1) weights_fixed
    got_c20, bad_c20, shapes_c20 = [], [], True
    for n_c20 in CASES_C20["players"]:
        weights_c20 = as_floats(call_20(1, "weights_fixed", weights_fixed, n_c20))
        shapes_c20 = shapes_c20 and weights_c20 is not None and weights_c20.shape == (n_c20,)
        got_c20 += weights_c20.tolist() if shapes_c20 else []
        bad_c20 += weights_bad(n_c20)
    if not shapes_c20:
        why_c20 = "weights_fixed(n) rend les n poids w(0), …, w(n − 1)"
    elif passes(CASES_C20["id_weights"], got_c20):
        why_c20 = ""
    elif np.allclose(got_c20, bad_c20, rtol=1e-9, atol=0):
        why_c20 = "ta correction divise encore s! (n − 1 − s)! par (n − 1)!"
    else:
        why_c20 = "pour d'autres nombres de joueurs, ce ne sont pas les poids w(s) de la valeur de Shapley"
    report_20(not why_c20, "(1) weights_fixed : d'autres nombres de joueurs", f"(1) weights_fixed : {why_c20}")
    parts_20.append(1)

with checked("MB6.20"):                                       # (2) ranks_fixed
    got_c20, bad_c20, why_c20 = [], [], ""
    for sample_c20 in CASES_C20["samples"]:
        x_c20 = np.array(sample_c20)                          # non-dyadic floats: a change in place would show
        ranks_c20 = as_floats(call_20(2, "ranks_fixed", ranks_fixed, x_c20))
        if not np.array_equal(x_c20, np.array(sample_c20)):
            why_c20 = "ta fonction modifie l'échantillon reçu : travaille sur une copie"
            break
        if ranks_c20 is None or ranks_c20.shape != x_c20.shape:
            why_c20 = "ranks_fixed rend un rang par valeur, de la forme de x"
            break
        got_c20 += ranks_c20.tolist()
        bad_c20 += ranks_bad(sample_c20).tolist()
    if not why_c20 and not passes(CASES_C20["id_ranks"], got_c20):
        why_c20 = ("ta correction donne encore aux ex aequo des rangs différents" if got_c20 == bad_c20 else
                   "sur d'autres échantillons (des groupes de 2 et de 3 valeurs égales), ce ne sont pas les rangs "
                   "moyens : chaque groupe de valeurs égales reçoit la moyenne des places qu'il occupe")
    report_20(not why_c20, "(2) ranks_fixed : d'autres échantillons, avec des groupes d'ex aequo de tailles différentes",
              f"(2) ranks_fixed : {why_c20}")
    parts_20.append(2)

with checked("MB6.20"):                                       # (3) lerp_fixed, read directly
    got_c20, bad_c20, why_c20 = [], [], ""
    for a_c20, b_c20, t_c20 in CASES_C20["lerps"]:
        left_c20, right_c20 = np.array(a_c20), np.array(b_c20)   # non-dyadic floats: a change in place would show
        value_c20 = as_floats(call_20(3, "lerp_fixed", lerp_fixed, left_c20, right_c20, t_c20))
        if not (np.array_equal(left_c20, np.array(a_c20)) and np.array_equal(right_c20, np.array(b_c20))):
            why_c20 = "ta fonction modifie un tableau reçu : travaille sur une copie"
            break
        if value_c20 is None or value_c20.shape != np.shape(a_c20):
            why_c20 = "lerp_fixed rend une valeur de la forme de a"
            break
        got_c20 += np.ravel(value_c20).tolist()
        bad_c20 += np.ravel(lerp_bad(np.array(a_c20), np.array(b_c20), t_c20)).tolist()
    if not why_c20 and not passes(CASES_C20["id_lerps"], got_c20):
        why_c20 = ("ta correction rend encore la valeur b en t = 0" if np.allclose(got_c20, bad_c20, rtol=1e-12) else
                   "en d'autres t (ni 0, ni ½, ni 1), ce n'est pas l'interpolation qui vaut a en t = 0 et b en t = 1")
    report_20(not why_c20, "(3) lerp_fixed : d'autres valeurs lues entre deux cases, en nombres et en tableaux",
              f"(3) lerp_fixed : {why_c20}")
    parts_20.append(3)

if len(set(parts_20)) == 3:
    verdict("MB6.20", all(results_20), "les trois fonctions corrigées passent tous les cas.", "relis les lignes ❌ ci-dessus.")'''

NOTE_20 = (r"(1) Diviser par $n!$ : `math.factorial(s) * math.factorial(n - 1 - s) / math.factorial(n)`. a) $(1 ;\ 7)$. "
           r"(2) Donner à chaque groupe de valeurs égales la moyenne de ses places. b) $\approx (0{,}5988 ;\ 0{,}5357)$. "
           r"(3) `(1 - t) * a + t * b`. c) $(14{,}4 ;\ 17{,}6)$.")

MB6_20 = ex(
    "MB6.20", "reconnaître trois erreurs (des poids sans le facteur $\\frac1n$, des ex aequo rangés dans l'ordre "
    "d'apparition, une interpolation aux poids échangés), qui passent une vérification mal choisie, puis les corriger.",
    "fiche §1, §5 et §6 ; Ex MB6.13, MB6.16", note=NOTE_20, given=GIVEN_20,
    body=r"""Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe (cellule fournie) :
1. `weights_bad(n)` doit rendre les poids $w(s)$ de la valeur de Shapley ; elle divise $s!\,(n - 1 - s)!$ par $(n - 1)!$ au lieu de $n!$. Il l'a vérifiée pour $n = 1$.
2. `ranks_bad(x)` doit rendre les rangs, rangs moyens aux ex aequo ; elle donne aux ex aequo des rangs différents, dans l'ordre où ils apparaissent. Il l'a vérifiée sur un échantillon sans ex aequo.
3. `lerp_bad(a, b, t)` doit interpoler entre $a$ (en $t = 0$) et $b$ (en $t = 1$) ; elle rend $(1 - t)\,b + t\,a$. Elle sert à lire une valeur entre deux cases d'une grille (fiche §5). Il l'a vérifiée en $t = \frac12$.

À faire : trouve et corrige chaque erreur dans le code du collègue lui-même : les fonctions corrigées s'appellent `weights_fixed`, `ranks_fixed` et `lerp_fixed`, avec les mêmes arguments, et n'appellent **pas** `mymath` (la vérification le contrôle). Puis réponds :
- a) pour $n = 7$, $\sum_s\binom{6}{s}w(s)$ avec la fonction corrigée, puis avec la fonction fautive (une liste de 2 nombres) ;
- b) $\rho_S$ des deux échantillons `X_20` et `Y_20` (avec des ex aequo), calculée par la corrélation de Pearson des rangs de la fonction corrigée, puis de ceux de la fonction fautive (une liste de 2 nombres ; hors de `mymath`, `np.corrcoef` est permis) ;
- c) l'interpolation en $t = 0{,}3$ entre 12 et 20, corrigée puis fautive (une liste de 2 nombres).

Dans ta copie : pour chacune des trois erreurs, pourquoi la vérification du collègue ne la voyait pas. La vérification essaie aussi tes fonctions corrigées sur des cas cachés : d'autres nombres de joueurs, d'autres échantillons avec des ex aequo, d'autres valeurs lues entre deux cases, et des tableaux qu'elles ne doivent pas modifier.""",
    todo='''def weights_fixed(n):
    """The weights w(s) of the Shapley value of n players, s = 0, ..., n - 1 (floats)."""
    raise NotImplementedError("weights_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def ranks_fixed(x):
    """The ranks of the values of x, from 1 (the smallest), tied values sharing the mean of the places they occupy."""
    raise NotImplementedError("ranks_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def lerp_fixed(a, b, t):
    """The value at t of the linear interpolation between a (at t = 0) and b (at t = 1), to read a value between two
    cells of a grid."""
    raise NotImplementedError("lerp_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB6_20a = answer_MB6_20b = answer_MB6_20c = ...
with wbm.attempt("MB6.20"):          # your three functions: ⏳ while they are not written
    answer_MB6_20a = ...  # a) a list of 2 numbers, as computed: for n = 7, sum of C(6, s) w(s) by weights_fixed, then by the WRONG weights_bad
    answer_MB6_20b = ...  # b) a list of 2 numbers, as computed: rho_S of X_20, Y_20 on the ranks of ranks_fixed, then of the WRONG ranks_bad
    answer_MB6_20c = ...  # c) a list of 2 numbers, as computed: at t = 0.3 between 12 and 20, by lerp_fixed, then by the WRONG lerp_bad''',
    check=answers_check("MB6.20", "abc") + "\n\n" + CHECK_20,
    solution='''def weights_fixed(n):
    """The weights w(s) of the Shapley value of n players, s = 0, ..., n - 1 (floats)."""
    return [math.factorial(s) * math.factorial(n - 1 - s) / math.factorial(n) for s in range(n)]   # n!, not (n - 1)!


def ranks_fixed(x):
    """The ranks of the values of x, from 1 (the smallest), tied values sharing the mean of the places they occupy."""
    x = np.asarray(x, dtype=float)
    order = np.argsort(x, kind="stable")
    ranks = np.empty(len(x))
    ranks[order] = np.arange(1, len(x) + 1)
    for value in np.unique(x):                                 # each group of equal values: the mean of its places
        tied = x == value
        ranks[tied] = ranks[tied].mean()
    return ranks


def lerp_fixed(a, b, t):
    """The value at t of the linear interpolation between a (at t = 0) and b (at t = 1), to read a value between two
    cells of a grid."""
    return (1 - t) * a + t * b                                 # the weight 1 - t goes with a


def correlation_20(r, s):
    return float(np.corrcoef(r, s)[0, 1])


answer_MB6_20a = [sum(math.comb(6, s) * w for s, w in enumerate(weights(7))) for weights in (weights_fixed, weights_bad)]
answer_MB6_20b = [correlation_20(ranks(X_20), ranks(Y_20)) for ranks in (ranks_fixed, ranks_bad)]
answer_MB6_20c = [lerp_fixed(12.0, 20.0, 0.3), lerp_bad(12.0, 20.0, 0.3)]
print("a)", answer_MB6_20a, " b)", np.round(answer_MB6_20b, 6).tolist(), " c)", np.round(answer_MB6_20c, 6).tolist())''',
    record='''from fractions import Fraction as F_20r

from scipy import stats as stats_20r

sum_20r = [float(sum(math.comb(6, s) * F_20r(math.factorial(s) * math.factorial(6 - s), math.factorial(top))
                     for s in range(7))) for top in (7, 6)]
wbm.record("MB6.20a", sum_20r, decimals=4,
           mistakes={"le second nombre est celui de la version FAUSSE, weights_bad": [sum_20r[0]] * 2,
                     "la version corrigée d'abord, puis la version fautive": sum_20r[::-1]})
x_20r, y_20r = np.array(__X_20__), np.array(__Y_20__)


def rho_20r(method):
    """The correlation of the ranks of scipy.stats.rankdata (method for x_20r, average for y_20r when method is
    average, the same method for both otherwise)."""
    return float(stats_20r.pearsonr(stats_20r.rankdata(x_20r, method=method), stats_20r.rankdata(y_20r, method=method))[0])


right_20r, bad_20r = rho_20r("average"), rho_20r("ordinal")
wbm.record("MB6.20b", [right_20r, bad_20r], decimals=4,
           mistakes={"ranks_fixed donne encore aux ex aequo des rangs différents": [bad_20r] * 2,
                     "le second nombre est celui de la version FAUSSE, ranks_bad": [right_20r] * 2,
                     "la version corrigée d'abord, puis la version fautive": [bad_20r, right_20r],
                     "les ex aequo reçoivent la moyenne de leurs places, pas la plus petite": [rho_20r("min"), bad_20r],
                     "les ex aequo reçoivent la moyenne de leurs places, pas la plus grande": [rho_20r("max"), bad_20r],
                     "les ex aequo reçoivent la moyenne de leurs places : les rangs vont de 1 à n, sans se resserrer "
                     "après un groupe d'ex aequo": [rho_20r("dense"), bad_20r]})
right_c_20r, bad_c_20r = float(F_20r(7, 10) * 12 + F_20r(3, 10) * 20), float(F_20r(7, 10) * 20 + F_20r(3, 10) * 12)
wbm.record("MB6.20c", [right_c_20r, bad_c_20r], decimals=2,
           mistakes={"lerp_fixed rend encore (1 − t) b + t a": [bad_c_20r] * 2,
                     "le second nombre est celui de la version FAUSSE, lerp_bad": [right_c_20r] * 2,
                     "la version corrigée d'abord, puis la version fautive": [bad_c_20r, right_c_20r]})
CASES_20r = __CASES_C20__                                                   # the hidden cases of the check
wbm.record(CASES_20r["id_weights"], [float(F_20r(math.factorial(s) * math.factorial(n - 1 - s), math.factorial(n)))
                                     for n in CASES_20r["players"] for s in range(n)], decimals=11)
wbm.record(CASES_20r["id_ranks"], [float(r) for sample in CASES_20r["samples"]
                                   for r in stats_20r.rankdata(sample, method="average")], decimals=6)
wbm.record(CASES_20r["id_lerps"], [float((1 - F_20r(str(t))) * F_20r(str(a)) + F_20r(str(t)) * F_20r(str(b)))
                                   for left, right, t in CASES_20r["lerps"]
                                   for a, b in zip(np.ravel(left).tolist(), np.ravel(right).tolist())], decimals=9)''',
    after=[
        ("solution", answers_check("MB6.20", "abc") + "\n\n" + CHECK_20),
        ("md", "**Après la vérification**, dans ta copie : pour chacune des trois erreurs, pourquoi la vérification du "
               "collègue ne la voyait-elle pas, et quelle vérification l'aurait vue ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB6.21 · a property test of line_integral
# ---------------------------------------------------------------------------
CHECK_21 = '''def simpson_twin_c21(field, points):
    """RIGHT: Simpson's rule with 40 intervals on each segment, written another way (the nodes accumulated)."""
    pts = np.asarray(points, dtype=float)
    total = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        values = [float(np.dot(np.asarray(field(a + (k / 40) * (b - a)), dtype=float), b - a)) for k in range(41)]
        total += (values[0] + values[-1] + 4 * sum(values[1:-1:2]) + 2 * sum(values[2:-1:2])) / 120
    return total


def gauss_twin_c21(field, points):
    """RIGHT: the three-point Gauss-Legendre rule on 8 equal pieces of each segment (exact for degrees up to 5)."""
    nodes, weights = np.polynomial.legendre.leggauss(3)
    pts = np.asarray(points, dtype=float)
    total = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        for piece in range(8):
            for x, w in zip(nodes, weights):
                t = (piece + (x + 1) / 2) / 8
                total += w / 16 * float(np.dot(np.asarray(field(a + t * (b - a)), dtype=float), b - a))
    return total


def left_sums_c21(field, points):
    """WRONG: left Riemann sums with 64 intervals on each segment (its nodes are not symmetric)."""
    pts = np.asarray(points, dtype=float)
    return sum(sum(float(np.dot(np.asarray(field(a + (k / 64) * (b - a)), dtype=float), b - a)) for k in range(64)) / 64
               for a, b in zip(pts[:-1], pts[1:]))


def absolute_c21(field, points):
    """WRONG: the absolute value of the integral (a path backwards keeps its sign)."""
    return abs(ref_att.line_integral(field, points))


def first_segment_c21(field, points):
    """WRONG from two segments on: the integral along the first segment only."""
    return ref_att.line_integral(field, np.asarray(points, dtype=float)[:2])


def trapezoid_c21(field, points):
    """WRONG unless the field is affine: the trapezoid rule with 20 intervals on each segment."""
    pts = np.asarray(points, dtype=float)
    total = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        values = [float(np.dot(np.asarray(field(a + (k / 20) * (b - a)), dtype=float), b - a)) for k in range(21)]
        total += (sum(values) - (values[0] + values[-1]) / 2) / 20
    return total


def swapped_c21(field, points):
    """WRONG for a field whose components differ: F₂ dx + F₁ dy instead of F₁ dx + F₂ dy."""
    return ref_att.line_integral(lambda p: np.asarray(field(p), dtype=float)[::-1], points)


def plus_offset_c21(field, points):
    """WRONG by more than 1e-9, but within np.allclose's default tolerance (1e-8 + 1e-5 |x|): the integral plus
    2e-9 + 2e-6 |integral|."""
    value = ref_att.line_integral(field, points)
    return value + 2e-9 + 2e-6 * abs(value)


def per_vertex_c21(field, points):
    """WRONG by more than 1e-9, but within np.allclose's default tolerance: the integral times 1 + 2e-6 (k - 2), k the
    number of vertices (one vertex more changes the result)."""
    value = ref_att.line_integral(field, points)
    return value * (1 + 2e-6 * (len(points) - 2))


WRONG_C21 = [   # a hidden wrong method, the test that must refuse it, and the clause of the statement it tries
    (left_sums_c21, "reversed_changes_sign_21", "dès qu'on parcourt le chemin à l'envers (ses points d'évaluation ne "
                                                "sont pas symétriques) : ton champ fait-il varier F · γ′ le long d'un "
                                                "segment ? Le champ tournant (−y, x) le garde constant"),
    (absolute_c21, "reversed_changes_sign_21", "sur le signe : elle rend la même valeur dans les deux sens"),
    (first_segment_c21, "reversed_changes_sign_21", "dès deux segments (un seul segment est juste) : tes lignes brisées "
                                                    "en ont-elles plusieurs ?"),
    (plus_offset_c21, "reversed_changes_sign_21", "de 2·10⁻⁹ + 2·10⁻⁶ |valeur| : la tolérance de l'énoncé est 10⁻⁹ en "
                                                  "valeur relative (np.allclose a par défaut rtol = 1e-5 et atol = 1e-8)"),
    (trapezoid_c21, "split_changes_nothing_21", "sauf pour un champ affine (la méthode des trapèzes) : prends un champ "
                                                "dont les coordonnées sont de degré 2 ou 3"),
    (per_vertex_c21, "split_changes_nothing_21", "d'un facteur 1 + 2·10⁻⁶ par sommet ajouté : la tolérance de l'énoncé "
                                                 "est 10⁻⁹ en valeur relative (np.allclose a par défaut rtol = 1e-5 et "
                                                 "atol = 1e-8)"),
    (trapezoid_c21, "gradient_gives_difference_21", "sauf pour un champ affine (la méthode des trapèzes) : prends le "
                                                    "gradient d'un polynôme de degré 3"),
    (first_segment_c21, "gradient_gives_difference_21", "dès deux segments (un seul segment est juste) : tes lignes "
                                                        "brisées en ont-elles plusieurs ?"),
    (swapped_c21, "gradient_gives_difference_21", "pour un gradient dont les deux coordonnées diffèrent (elle échange "
                                                  "les composantes du champ) : prends une fonction qui n'est pas "
                                                  "symétrique en x et y"),
    (plus_offset_c21, "gradient_gives_difference_21", "de 2·10⁻⁹ + 2·10⁻⁶ |valeur| : la tolérance de l'énoncé est 10⁻⁹ "
                                                      "en valeur relative (np.allclose a par défaut rtol = 1e-5 et "
                                                      "atol = 1e-8)"),
]

with checked("MB6.21"):
    results_21 = []
    report_21 = reporter(results_21, stop=False)
    TESTS_C21 = {"reversed_changes_sign_21": reversed_changes_sign_21, "split_changes_nothing_21": split_changes_nothing_21,
                 "gradient_gives_difference_21": gradient_gives_difference_21}

    def anonymous_c21(method):
        """method under a neutral name: a test must judge what the method does, not what it is called."""
        def method_c21(field, points):
            return method(field, points)
        method_c21.__name__ = method_c21.__qualname__ = "method"
        return method_c21

    def verdict_c21(name, label, method):
        got = call_safely(f"Ex MB6.21 : {name}({label})", TESTS_C21[name], anonymous_c21(method))
        if not isinstance(got, (bool, np.bool_)):
            if isinstance(got, (int, np.integer)):
                what = f"{int(got)} (un entier)"
            elif isinstance(got, (float, np.floating)):
                what = f"{float(got):g} (un nombre)"
            else:
                what = shown(got)
            print(f"❌ Ex MB6.21 : {name}({label}) rend {what}, pas True ou False")
            raise StopCheck
        return bool(got)

    def verdicts_c21(label, method):
        return [verdict_c21(name, label, method) for name in TESTS_C21]

    on_ref_c21 = verdicts_c21("line_integral de la référence", ref_att.line_integral)
    report_21(passes("MB6.21a", on_ref_c21), "tes trois tests, sur line_integral de la référence",
              "tes trois tests ne rendent pas True sur line_integral de la référence, qui vérifie les trois propriétés : "
              "relis le choix des champs (fiche §4, et la règle de Simpson, exacte pour un polynôme de degré au plus 3)")
    twins_c21 = [verdicts_c21("une autre écriture juste de Simpson", simpson_twin_c21),
                 verdicts_c21("une règle de Gauss juste", gauss_twin_c21)]
    report_21(all(all(t) for t in twins_c21), "deux autres méthodes justes reçoivent aussi True",
              "deux autres méthodes justes (Simpson à 40 intervalles écrite autrement, Gauss à trois points ; des "
              "arrondis de l'ordre de 10⁻¹⁵) ne reçoivent pas toutes True : ta tolérance est-elle trop stricte, ou un "
              "champ trop éloigné d'un polynôme de degré au plus 3 ?")
    for number_c21, (method_c21, name_c21, clause_c21) in enumerate(WRONG_C21, start=1):
        refused_c21 = not verdict_c21(name_c21, f"méthode fausse cachée n° {number_c21}", method_c21)
        report_21(refused_c21, f"{name_c21} refuse la méthode fausse cachée n° {number_c21}",
                  f"{name_c21} accepte la méthode fausse cachée n° {number_c21}, fausse {clause_c21}")
    verdict("MB6.21", all(results_21) and len(results_21) == 2 + len(WRONG_C21), "tes trois tests jugent juste "
            "line_integral de la référence et deux autres méthodes justes, et refusent les méthodes fausses cachées.",
            "relis les lignes ❌ ci-dessus.")'''

NOTE_21 = (r"Une correction possible : `reversed_changes_sign_21` tire cinq lignes brisées de 2 à 5 segments et compare "
           r"`method(F, P)` à `-method(F, P[::-1])` pour $\mathbf{F}(x, y) = (\sin x + y^2,\ x\cos y)$, qui n'est pas un "
           r"gradient ; `split_changes_nothing_21` insère un sommet en un point tiré au hasard d'un segment, pour "
           r"$\mathbf{F}(x, y) = (x^3 - 2y,\ x^2 + y^3)$ ; `gradient_gives_difference_21` prend le gradient de "
           r"$f(x, y) = x^3 - 4y^3 + 5xy$ ; chaque comparaison à $10^{-9}$ près en valeur relative. a) `[True, True, "
           r"True]`.")

MB6_21 = ex(
    "MB6.21", "écrire trois tests de propriété d'une intégrale le long d'une ligne brisée, et voir ce que chacun attrape.",
    "fiche §4 ; M02a (méthode de Simpson) ; Ex MB6.15", note=NOTE_21,
    body=r"""Écris trois fonctions qui testent une méthode qu'on leur passe, de la même signature que `line_integral(field, points)`, et rendent `True` si la propriété tient, `False` sinon :
- `reversed_changes_sign_21(method)` vérifie, sur plusieurs lignes brisées tirées au hasard dans le plan et un champ qui n'est pas un gradient, que parcourir la ligne à l'envers change le signe ;
- `split_changes_nothing_21(method)` vérifie qu'ajouter un sommet à l'intérieur d'un segment (en un point tiré au hasard sur ce segment) ne change pas le résultat ;
- `gradient_gives_difference_21(method)` vérifie, pour le gradient d'une fonction dont tu connais l'expression, que le résultat vaut $f(\text{fin}) - f(\text{début})$.

Chaque comparaison se fait à $10^{-9}$ près en valeur relative, plus finement que la tolérance par défaut de `np.allclose` (`rtol=1e-5`, `atol=1e-8`). Choisis tes champs pour que chaque propriété tienne à l'arrondi près pour `line_integral` de la référence (`ref_att.line_integral`) : parcourir un segment à l'envers garde les mêmes points de Simpson, pour tout champ, mais une méthode aux points non symétriques ne se voit que si $\mathbf{F}\cdot\boldsymbol\gamma'$ varie le long d'un segment (ce n'est pas le cas du champ tournant $(-y, x)$) ; la règle de Simpson n'est exacte que si $t \mapsto \mathbf{F}(\boldsymbol\gamma(t))\cdot\boldsymbol\gamma'(t)$ est un polynôme de degré au plus 3 sur chaque segment, et, pour un autre champ, couper un segment en deux change le résultat d'environ $10^{-5}$ : pour les deux derniers tests, prends des champs dont les coordonnées sont des polynômes de degré 2 ou 3.

La vérification lance tes trois tests sur `line_integral` de la référence, sur deux autres méthodes justes, puis sur des méthodes fausses cachées, passées sous un nom neutre (un test juge ce que fait la méthode, pas son nom), une par clause de l'énoncé, que chaque test doit refuser quand sa propriété est fausse. Relève :
- a) les résultats de tes trois tests sur `line_integral` de la référence (une liste de 3 booléens, dans l'ordre sens inversé, segment coupé, gradient).""",
    todo='''def reversed_changes_sign_21(method):
    """True when, on several polylines drawn at random and a field that is not a gradient, method(field, points[::-1])
    is -method(field, points) up to 1e-9 in relative value; False otherwise."""
    raise NotImplementedError("reversed_changes_sign_21 n'est pas encore écrite (04_indices.md si tu bloques)")


def split_changes_nothing_21(method):
    """True when adding a vertex inside a segment (at a point drawn at random on it) does not change method(field,
    points), up to 1e-9 in relative value, on several polylines drawn at random; False otherwise."""
    raise NotImplementedError("split_changes_nothing_21 n'est pas encore écrite (04_indices.md si tu bloques)")


def gradient_gives_difference_21(method):
    """True when, for the gradient of a function f you know, method(gradient, points) is f(last point) - f(first
    point) up to 1e-9 in relative value, on several polylines drawn at random; False otherwise."""
    raise NotImplementedError("gradient_gives_difference_21 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB6_21a = ...
with wbm.attempt("MB6.21"):          # your three tests: ⏳ while they are not written
    answer_MB6_21a = ...  # a) a list of 3 booleans: your three tests on ref_att.line_integral''',
    check=answers_check("MB6.21", "a") + "\n\n" + CHECK_21,
    solution='''rng_21 = np.random.default_rng(7921)


def close_21(u, v):
    """u and v equal up to 1e-9 in relative value."""
    return abs(u - v) <= 1e-9 * max(1.0, abs(u), abs(v))


def polylines_21(count=5):
    """count polylines of 2 to 5 segments, their vertices drawn at random in the plane."""
    return [rng_21.normal(size=(int(rng_21.integers(3, 7)), 2)) for _ in range(count)]


def reversed_changes_sign_21(method):
    """True when, on several polylines drawn at random and a field that is not a gradient, method(field, points[::-1])
    is -method(field, points) up to 1e-9 in relative value; False otherwise."""
    def field(p):                                       # not a gradient: dF1/dy = 2y, dF2/dx = cos y
        return np.array([math.sin(p[0]) + p[1] ** 2, p[0] * math.cos(p[1])])
    return all(close_21(method(field, P), -method(field, P[::-1])) for P in polylines_21())


def split_changes_nothing_21(method):
    """True when adding a vertex inside a segment (at a point drawn at random on it) does not change method(field,
    points), up to 1e-9 in relative value, on several polylines drawn at random; False otherwise."""
    def field(p):                                       # coordinates of degree 3: Simpson's rule is exact
        return np.array([p[0] ** 3 - 2 * p[1], p[0] ** 2 + p[1] ** 3])
    for P in polylines_21():
        j = int(rng_21.integers(0, len(P) - 1))
        Q = np.insert(P, j + 1, P[j] + rng_21.uniform(0.1, 0.9) * (P[j + 1] - P[j]), axis=0)
        if not close_21(method(field, P), method(field, Q)):
            return False
    return True


def gradient_gives_difference_21(method):
    """True when, for the gradient of a function f you know, method(gradient, points) is f(last point) - f(first
    point) up to 1e-9 in relative value, on several polylines drawn at random; False otherwise."""
    def f(x, y):
        return x ** 3 - 4 * y ** 3 + 5 * x * y

    def gradient(p):
        return np.array([3 * p[0] ** 2 + 5 * p[1], -12 * p[1] ** 2 + 5 * p[0]])
    return all(close_21(method(gradient, P), f(*P[-1]) - f(*P[0])) for P in polylines_21())


answer_MB6_21a = [test(ref_att.line_integral) for test in (reversed_changes_sign_21, split_changes_nothing_21,
                                                           gradient_gives_difference_21)]
print("a)", answer_MB6_21a)''',
    record='''def properties_21r(method):
    """The oracle: the three properties, measured on other polylines and fields than any test of the notebook."""
    rng = np.random.default_rng(7922)
    lines = [rng.uniform(-2, 2, size=(k, 2)) for k in (3, 4, 6)]
    bent = lambda p: np.array([np.cos(p[1]) * p[0], np.exp(p[0] / 3) - p[1]])          # noqa: E731, not a gradient
    cubic = lambda p: np.array([p[1] ** 3 - p[0], 2 * p[0] ** 2 * p[1]])              # noqa: E731, degree 3
    potential = lambda x, y: 2 * x ** 4 - x * y ** 3 + y                              # noqa: E731
    gradient = lambda p: np.array([8 * p[0] ** 3 - p[1] ** 3, -3 * p[0] * p[1] ** 2 + 1])   # noqa: E731
    near = lambda u, v: abs(u - v) <= 1e-10 * max(1.0, abs(u))                        # noqa: E731
    reverse = all(near(method(bent, P), -method(bent, P[::-1])) for P in lines)
    split = all(near(method(cubic, P), method(cubic, np.insert(P, 1, P[0] + 0.37 * (P[1] - P[0]), axis=0))) for P in lines)
    difference = all(near(method(gradient, P), potential(*P[-1]) - potential(*P[0])) for P in lines)
    return [bool(reverse), bool(split), bool(difference)]


wbm.record("MB6.21a", properties_21r(ref_att.line_integral),
           mistakes={"line_integral de la référence vérifie les trois propriétés : un test qui la refuse a un champ ou "
                     "une tolérance qui ne conviennent pas (relis le choix des champs)": [True, False, True]})''',
    after=[
        ("solution", answers_check("MB6.21", "a") + "\n\n" + CHECK_21),
        look("pourquoi un champ non polynomial ferait-il refuser `line_integral` de la référence par ton deuxième test ? "
             "Pourquoi un champ affine laisserait-il passer la méthode des trapèzes ? Pourquoi tirer les lignes brisées "
             "au hasard, et plusieurs fois ?"),
    ],
)

PART_C = Part("C", "Déboguer, tester",
              "Fiche §1, §4, §5 et §6. Trois erreurs, qui passent une vérification mal choisie ; trois tests de propriété "
              "d'une intégrale le long d'une ligne brisée. Les méthodes cachées s'appuient sur la référence (`ref_att`), "
              "pour ne pas dépendre de ton code.", exercises=[MB6_20, MB6_21])

# ---------------------------------------------------------------------------
# Notebook exercise: the challenge (MB6.22)
# ---------------------------------------------------------------------------
GIVEN_22 = '''# The council of the challenge: the votes of its 25 members (0 to 24), and the quota
WEIGHTS_22 = (12, 9, 9, 7, 6, 6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1)
QUOTA_22 = 66'''

CHECK_22 = """def check_c22():
    \"\"\"The check of MB6.22, in a function. The hidden councils come from another process (the hidden module run as a
    script): it draws them, sends their weights and quotas, and measures the indices it receives only at the end;
    no exact index of a hidden council lives in this process while the learner's function runs. Each call runs under
    code_from (the learner's function may not run code of the hidden module) and under a time limit where the system
    allows one (it only stops a runaway computation).\"\"\"
    import json
    import signal
    import subprocess
    import sys
    import threading
    hidden_file = wbm.repo_root() / "solutions" / "challenges" / "mb6_22.py"   # reading it spoils the challenge
    twins = code_keys_of_file(hidden_file)                      # its functions, to recognise a copy run from elsewhere
    results = []
    report = reporter(results, stop=False)
    budget = 300.0                                              # seconds for the fifteen hidden councils

    class TimeUp(BaseException):
        \"\"\"Raised by the alarm: a BaseException, so that a broad except of the learner's code does not hide it.\"\"\"

    @contextlib.contextmanager
    def time_limit(seconds):
        usable = hasattr(signal, "setitimer") and threading.current_thread() is threading.main_thread()
        if not usable:
            yield
            return

        def ring(signum, frame):
            raise TimeUp

        before = signal.signal(signal.SIGALRM, ring)
        signal.setitimer(signal.ITIMER_REAL, max(seconds, 0.01))
        try:
            yield
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
            signal.signal(signal.SIGALRM, before)

    def indices(label, weights, quota, seconds):
        \"\"\"shapley_shubik_22 on a council, under code_from and a time limit: (a float array of one index per member,
        the time taken).\"\"\"
        start = time.perf_counter()
        try:
            with time_limit(seconds):
                with code_from([hidden_file], twins=twins, escapes=True) as seen:
                    out = call_safely(label, shapley_shubik_22, list(weights), int(quota))
        except TimeUp:
            print(f"❌ {label} : ta fonction n'a pas fini en {fr(seconds, 0)} s : parcourt-elle les coalitions une à une ? "
                  "Compte-les par taille et par poids total")
            raise StopCheck from None
        elapsed = time.perf_counter() - start
        if seen and seen[0].startswith("lance "):
            print(f"❌ {label} : shapley_shubik_22 {seen[0].replace(' : ', ' (', 1)}) : les indices se calculent dans ta "
                  "fonction ; ce qu'exécute un autre processus échappe à la vérification")
            raise StopCheck
        if seen:
            what = "lit" if seen[0].startswith("ouvre ") else "exécute du code de"
            where = "" if seen[0].startswith("ouvre ") else f" ({seen[0]})"
            print(f"❌ {label} : shapley_shubik_22 {what} solutions/challenges/mb6_22.py{where}, la partie cachée du "
                  "défi, ou une copie de son code : la vérification mesurerait sa méthode, pas la tienne")
            raise StopCheck
        values = as_floats(out)
        if values is None or values.shape != (len(weights),):
            print(f"❌ {label} : shapley_shubik_22 rend un indice par membre du conseil reçu ({len(weights)} nombres), reçu "
                  f"{shown(out)}")
            raise StopCheck
        if not np.all(np.isfinite(values)):
            print(f"❌ {label} : shapley_shubik_22 rend des nombres qui ne sont pas tous finis")
            raise StopCheck
        return values, elapsed

    def probe(n):
        \"\"\"A council of n members of 1, 2, ..., 8, 1, 2, ... votes, simple majority (a probe of the time, not a hidden
        case): the smaller of two timings.\"\"\"
        votes = [k % 8 + 1 for k in range(n)]
        label = f"Ex MB6.22 : shapley_shubik_22 (un conseil d'essai de {n} membres)"
        return min(indices(label, votes, sum(votes) // 2 + 1, 60)[1] for _ in range(2))

    mine, spent = indices("Ex MB6.22 : shapley_shubik_22 (le conseil du notebook)", WEIGHTS_22, QUOTA_22, 30)
    if spent > 30:
        print(f"❌ Ex MB6.22 : ta fonction met {fr(spent, 1)} s pour les 25 membres du notebook ; les conseils cachés en "
              "ont 30 à 50 : à ce rythme, ils dépasseraient de loin les cinq minutes permises")
        raise StopCheck
    if spent >= 0.2:                                            # a slow function: does its time double with each member?
        times = [probe(n) for n in (16, 22)]                    # 2^6 = 64 times more coalitions; a polynomial: 3 to 5 times
        if times[1] > 0.05 and times[1] > 15 * max(times[0], 1e-3):
            print(f"❌ Ex MB6.22 : ta fonction semble parcourir les coalitions : son temps est multiplié par "
                  f"{fr(times[1] / max(times[0], 1e-3), 0)} quand le conseil passe de 16 à 22 membres ({fr(times[0], 3)} s, "
                  f"puis {fr(times[1], 2)} s) ; pour 30 à 50 membres, il lui faudrait des heures : compte les coalitions "
                  "par taille et par poids total")
            raise StopCheck

    def exactly_line(stream):
        line = stream.readline()
        if not line.endswith(b"\\n"):
            raise OSError("échange interrompu")
        return json.loads(line)

    server = subprocess.Popen([sys.executable, "-I", str(hidden_file), "--serve"], stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)   # this kernel's Python, here or on Colab
    try:
        councils = exactly_line(server.stdout)["councils"]
        answers, total = [], 0.0
        for k, (weights, quota) in enumerate(councils, start=1):
            values, spent = indices(f"Ex MB6.22 : shapley_shubik_22 (conseil caché {k})", weights, quota,
                                    max(budget - total, 1.0))
            answers.append(values.tolist())
            total += spent
        server.stdin.write((json.dumps(answers + [mine.tolist()]) + "\\n").encode())
        server.stdin.flush()
        measured = exactly_line(server.stdout)                    # only now: the gaps, the kinds
        assert len(measured) == len(councils) + 1
    except (OSError, ValueError, KeyError, TypeError, AssertionError) as exc:
        print("❌ Ex MB6.22 : la vérification n'a pas pu échanger les conseils et les indices avec le processus qui tire "
              f"les conseils cachés ({type(exc).__name__} ; ta fonction a-t-elle touché à ce processus ?) : exécute à "
              "nouveau la cellule")
        raise StopCheck from None
    finally:                                                    # always, even on an error or an interruption
        if server.poll() is None:
            server.kill()
        server.wait()
        for pipe in (server.stdin, server.stdout):
            try:
                pipe.close()
            except OSError:                                     # a pipe already broken
                pass

    def tens(x):
        \"\"\"A gap written the French way, in powers of ten (9,0·10⁻³).\"\"\"
        if x == 0:
            return "0"
        mantissa, exponent = f"{x:.1e}".split("e")
        if int(exponent) == 0:
            return mantissa.replace(".", ",")
        return mantissa.replace(".", ",") + "·10" + str(int(exponent)).translate(str.maketrans("-0123456789",
                                                                                                "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))

    notebook, hidden = measured[-1], measured[:-1]
    notebook_ok = notebook["gap"] is not None and notebook["gap"] <= 1e-9
    report(notebook_ok, "le conseil du notebook : chaque indice à 10⁻⁹ près",
           "le conseil du notebook : " + ("des indices qui ne sont pas des nombres finis" if notebook["gap"] is None
                                          else f"un indice à {tens(notebook['gap'])} de l'indice exact, plus que 10⁻⁹"))
    for number in sorted({c["series"] for c in hidden}):        # what each hidden council measured (no index)
        series = [c for c in hidden if c["series"] == number]
        print(f"   série {number} : " + " ; ".join(f"« {c['kind']} » ({c['n']} membres) écart "
                                                  + ("non mesuré" if c["gap"] is None else tens(c["gap"]))
                                                  for c in series))
    wrong = [c for c in hidden if c["gap"] is None or c["gap"] > 1e-9]
    largest = max((c["gap"] for c in wrong if c["gap"] is not None), default=None)
    if not wrong:
        why = ""
    elif largest is not None and largest < 1e-6 and all(c["gap"] is not None for c in wrong):
        why = (f" (écart jusqu'à {tens(largest)}) : presque juste, mais les comptes de coalitions vont jusqu'à 10¹⁴ ; "
               "des flottants de 32 bits n'en gardent pas assez de chiffres : garde des flottants de 64 bits ou des "
               "entiers")
    elif notebook_ok:
        why = (" : ta fonction est exacte pour le conseil du notebook, mais pas pour ces conseils ; se sert-elle de "
               "nombres du conseil du notebook (25 membres, le quota 66, ses voix) au lieu de ceux du conseil reçu ?")
    else:
        why = ("" if largest is None else f" (écart jusqu'à {tens(largest)})") + (" : ce ne sont pas les indices de "
               "Shapley-Shubik ; relis la condition du pivot et les poids w(s) des coalitions (fiche §1)")
    report(not wrong, f"les {len(hidden)} conseils cachés : chaque indice à 10⁻⁹ près, en {fr(total, 2)} s",
           f"les {len(hidden)} conseils cachés : {len(wrong)} ont un indice à plus de 10⁻⁹ de l'indice exact" + why)
    report(total <= budget, "le temps : moins de cinq minutes pour les quinze conseils cachés",
           f"le temps : {fr(total, 1)} s pour les quinze conseils cachés, plus que les cinq minutes permises")
    verdict("MB6.22", all(results) and len(results) == 3, "critère atteint : les indices exacts du conseil du notebook "
            "et des quinze conseils cachés, à 10⁻⁹ près, en moins de cinq minutes.",
            "critère pas encore atteint : relis les lignes ❌ ci-dessus.")


with checked("MB6.22"):
    check_c22()"""

NOTE_22 = (r"`shapley_shubik_22` : pour chaque membre $i$, un tableau `counts[s, t]` des coalitions des autres membres de "
           r"taille $s$ et de poids total $t < q$, rempli membre par membre (`counts[1:, w:] += counts[:-1, :q - w]`, "
           r"avec une copie) ; puis les colonnes $\max(q - \omega_i, 0)$ à $q - 1$, et $\varphi_i = \sum_sw(s)\,N_i(s)$ "
           r"avec `coalition_weights(n)`. a) $\varphi_0 \approx 0{,}131430$. b) Les 25 indices, de $0{,}131430$ (12 "
           r"voix) à $0{,}009681$ (une voix), de somme 1.")

MB6_22 = ex(
    "MB6.22", "calculer les indices de Shapley-Shubik exacts d'un grand conseil par un comptage, et le vérifier sur des "
    "conseils cachés.", "fiche §1 ; Ex MB6.1, MB6.13", note=NOTE_22, given=GIVEN_22,
    body=r"""Le notebook fournit `WEIGHTS_22`, les voix des 25 membres d'un conseil (des entiers de 1 à 12, 98 voix en tout), et `QUOTA_22` $= 66$. Écris `shapley_shubik_22(weights, quota)`, qui rend les indices de Shapley-Shubik de tous les membres, exacts (des flottants), sans parcourir les coalitions une à une : pour chaque membre $i$, compte les coalitions des autres membres par taille et par poids total (un tableau rempli membre par membre), garde celles où $i$ est pivot, et pondère par `coalition_weights`.

**Critère de réussite :** pour le conseil du notebook et pour trois séries de cinq conseils cachés de 30 à 50 membres, tirés à nouveau à chaque exécution (une majorité simple, une majorité qualifiée, un membre au veto, quelques grands et beaucoup de petits, des poids presque égaux), chaque indice est à $10^{-9}$ près l'indice exact, et ta fonction traite les quinze conseils cachés en moins de cinq minutes. Elle ne doit pas exécuter le code du module caché du défi (`solutions/challenges/mb6_22.py`) : la vérification le contrôle. Relève :
- a) l'indice du membre 0, qui a 12 voix (un nombre) ;
- b) les 25 indices (une liste de 25 nombres).

Point de départ : pour un conseil de 30 membres, les coalitions sans un membre sont $2^{29}$, plus de 500 millions ; mais leurs poids totaux sont des entiers de 0 à quelques centaines.""",
    todo='''def shapley_shubik_22(weights, quota):
    """The Shapley-Shubik indices of all the members of the council [quota ; weights] (positive integers), exact
    (floats), without going through the coalitions one by one."""
    raise NotImplementedError("shapley_shubik_22 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB6_22a = answer_MB6_22b = ...
with wbm.attempt("MB6.22"):          # your shapley_shubik_22: ⏳ while it is not written
    answer_MB6_22a = ...  # a) a number, as computed: the index of member 0 (12 votes)
    answer_MB6_22b = ...  # b) a list of 25 numbers, as computed: the 25 indices''',
    check=answers_check("MB6.22", "ab") + "\n\n\n" + CHECK_22,
    solution='''def shapley_shubik_22(weights, quota):
    """The Shapley-Shubik indices of all the members of the council [quota ; weights] (positive integers), exact
    (floats), without going through the coalitions one by one."""
    weights = [int(w) for w in weights]
    n, q = len(weights), int(quota)
    w = mymath.attribution.coalition_weights(n)              # w[s]: the weight of one coalition of s other members
    phi = []
    for i in range(n):
        counts = np.zeros((n, q))                            # counts[s, t]: coalitions of s others, total weight t < q
        counts[0, 0] = 1.0
        for j in range(n):
            if j != i and weights[j] < q:
                counts[1:, weights[j]:] = counts[1:, weights[j]:] + counts[:-1, :q - weights[j]]
        swings = counts[:, max(q - weights[i], 0):q].sum(axis=1)    # losing without i, winning with i
        phi.append(float(w @ swings))
    return phi


start_22 = time.perf_counter()
indices_22 = shapley_shubik_22(WEIGHTS_22, QUOTA_22)
answer_MB6_22a = indices_22[0]
answer_MB6_22b = indices_22
print("a)", round(answer_MB6_22a, 6), " b)", np.round(answer_MB6_22b, 6).tolist())
print(f"   somme {sum(indices_22):.12f} ; part des voix du membre 0 : {12 / 98:.4f} ({time.perf_counter() - start_22:.3f} s)")''',
    record='''import itertools as itertools_22r
from fractions import Fraction as F_22r


def swings_22r(weights, quota):
    """The oracle's counts, in Python integers: for each member i, the numbers of coalitions of s other members whose
    total weight t is in [q - w_i, q - 1] (i pivot), and in [q - w_i, q] (q included: a classic error)."""
    n, q = len(weights), quota
    pivot, wider = [], []
    for i in range(n):
        table = [[0] * (q + 1) for _ in range(n)]
        table[0][0] = 1
        for j in range(n):
            if j == i:
                continue
            for s in range(n - 1, 0, -1):
                row, below = table[s], table[s - 1]
                for t in range(q, weights[j] - 1, -1):
                    row[t] += below[t - weights[j]]
        lo = max(q - weights[i], 0)
        pivot.append([sum(table[s][lo:q]) for s in range(n)])
        wider.append([sum(table[s][lo:q + 1]) for s in range(n)])
    return pivot, wider


def weighted_22r(counts, shift=0):
    """sum over s of w(s + shift) counts[s] for each member, in exact fractions (shift=1: a classic error)."""
    n = len(counts)
    size = lambda s: min(s + shift, n - 1)                                                 # noqa: E731
    return [float(sum(F_22r(math.factorial(size(s)) * math.factorial(n - 1 - size(s)), math.factorial(n)) * c
                      for s, c in enumerate(row))) for row in counts]


votes_22r = list(__WEIGHTS_22__)
pivot_22r, wider_22r = swings_22r(votes_22r, 66)
right_22r = weighted_22r(pivot_22r)
shares_22r = [w / sum(votes_22r) for w in votes_22r]
few_22r = [float(sum(F_22r(math.factorial(s) * math.factorial(23 - s), math.factorial(24)) * c   # the weights of
                     for s, c in enumerate(row[:24]))) for row in pivot_22r]                  # 24 players: an error
wbm.record("MB6.22a", right_22r[0], decimals=6,
           mistakes={"le pouvoir d'un membre n'est pas sa part des voix : compte les ordres où il est pivot": shares_22r[0],
                     "i est pivot quand la coalition des autres perd sans lui (poids total au plus q − 1) et gagne avec "
                     "lui": weighted_22r(wider_22r)[0],
                     "w(s) se lit à la taille s de la coalition des autres membres, sans compter i":
                         weighted_22r(pivot_22r, shift=1)[0],
                     "le conseil a 25 membres : les poids sont ceux de coalition_weights(25), même si i n'est pas dans "
                     "la coalition": few_22r[0]})
wbm.record("MB6.22b", right_22r, decimals=6,
           mistakes={"le pouvoir d'un membre n'est pas sa part des voix : compte les ordres où il est pivot": shares_22r,
                     "i est pivot quand la coalition des autres perd sans lui (poids total au plus q − 1) et gagne avec "
                     "lui": weighted_22r(wider_22r),
                     "w(s) se lit à la taille s de la coalition des autres membres, sans compter i":
                         weighted_22r(pivot_22r, shift=1),
                     "le conseil a 25 membres : les poids sont ceux de coalition_weights(25), même si i n'est pas dans "
                     "la coalition": few_22r})''',
    after=[
        ("solution", answers_check("MB6.22", "ab") + "\n\n\n" + CHECK_22),
        ("md", "**Pour réfléchir** (une fois le critère atteint) : pourquoi deux membres de mêmes voix ont-ils le même "
               "indice ? Le membre de 12 voix a-t-il un pouvoir proportionnel à ses voix ? Pourquoi les conseils cachés "
               "de 30 à 50 membres sont-ils hors de portée d'une énumération des coalitions ? Les réponses sont dans "
               "`05_solutions.md`, section Notebook."),
    ],
)

PART_D = Part("D", "Défi", "Fiche §1. Les indices de Shapley-Shubik exacts d'un conseil de 25 membres, par un comptage par "
              "taille et par poids, vérifiés sur des conseils cachés tirés à chaque exécution.", exercises=[MB6_22])

PARTS = [PART_A, PART_B, PART_C, PART_D]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | MB6.1 à MB6.7, MB6.11 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, exercise in enumerate(part.exercises):
            rows.append(exercise.table_row(part.key if i == 0 else ""))
    if kind == "exercise":
        title = "# MB6 · Shapley, intégrales de chemin et équité — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). Dans "
               "les parties A à D, donne les valeurs que rend le calcul, **sans les arrondir** : les décimales "
               "demandées sont celles de ta copie. « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli : ce qui n'est pas fait affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/mb6_shapley_equite/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py MB6`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# MB6 · Shapley, intégrales de chemin et équité — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : un conseil à vote pondéré, trois hameaux et une conduite d'eau, "
               "le rendement d'une parcelle, le travail de deux forces, un coût à trois facteurs, une grille de capteurs, "
               "un contrôle de pièces sur deux lignes de production, et un pont vers l'écart de deux taux de détection.\n"
               "- Écrire les quatre fonctions de `mymath/attribution.py` (`coalition_weights`, `harsanyi_dividends`, "
               "`line_integral`, `spearman_rho`) et les tester.\n"
               "- Prédire puis mesurer l'intégrale d'un champ le long d'une boucle, comparer une moyenne marginale et une "
               "moyenne conditionnelle, tracer deux chemins dans un paysage, corriger trois erreurs, écrire trois tests "
               "de propriété, et relever un défi.\n\n"
               r"**Rappel express.** La valeur de Shapley : $\varphi_i = \sum_{S \not\ni i}w(s)\big[v(S \cup \{i\}) - "
               r"v(S)\big]$, avec $w(s) = \frac{s!\,(n - 1 - s)!}{n!}$, le poids d'**une** coalition de taille $s$ ; dans "
               r"un vote pondéré $[q ;\ \omega_1, \ldots, \omega_n]$, $i$ est pivot quand $S$ perd et $S \cup \{i\}$ "
               r"gagne. Les dividendes : $d_T = \sum_{S \subseteq T}(-1)^{\lvert T\rvert - \lvert S\rvert}v(S)$ et "
               r"$\varphi_i = \sum_{T \ni i}\frac{d_T}{\lvert T\rvert}$. Le long d'un chemin $\boldsymbol\gamma$ de "
               r"paramètre $t \in [0, 1]$ : $\int_{\boldsymbol\gamma}\mathbf{F}\cdot\mathrm{d}\boldsymbol\gamma = "
               r"\int_0^1\mathbf{F}(\boldsymbol\gamma(t))\cdot\boldsymbol\gamma'(t)\,\mathrm{d}t$, et "
               r"$\int_{\boldsymbol\gamma}\nabla f\cdot\mathrm{d}\boldsymbol\gamma = f(\text{fin}) - f(\text{début})$. "
               r"Spearman : la corrélation de Pearson des rangs, rangs moyens aux ex aequo. Fixer une variable : "
               r"$\operatorname{PD}_j(v) = \mathbb{E}[f(v, \mathbf{X}_{-j})]$ ou $M_j(v) = \mathbb{E}[f(\mathbf{X}) "
               r"\mid X_j = v]$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu calculer une valeur de Shapley par les ordres et par les poids des coalitions, et dire combien "
               "d'ordres tirés au hasard suffisent ?\n"
               "2. Sais-tu calculer les dividendes de Harsanyi d'un jeu, et en tirer la valeur de Shapley ?\n"
               "3. Sais-tu distinguer la moyenne marginale et la moyenne conditionnelle d'une fonction de variables "
               "corrélées ?\n"
               "4. Sais-tu intégrer un champ le long d'une ligne brisée, reconnaître un champ de gradient, et partager une "
               "variation entre les coordonnées ?\n"
               "5. Sais-tu agrandir une grille par interpolation bilinéaire, et calculer une corrélation de rangs avec "
               "des ex aequo ?\n"
               "6. Sais-tu écrire les critères d'équité comme des indépendances, et dire ce qui est incompatible quand "
               "les taux de base diffèrent ?\n\n"
               "**La suite** : le chapitre bonus B6 de workbookIA, qui applique ces outils.")]


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
# Build-time literals of the data and of the hidden cases, computed here by private functions (never the answer of a
# question), and the assertions that make them fair (the reference passes, the classic wrong versions are seen)
# ---------------------------------------------------------------------------
def load_module(path: Path, name: str):
    """A Python file of the repository, loaded as a module of its own (its relative imports are not used)."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def literal(value) -> str:
    """A Python literal of value (floats by repr: exact), wrapped for reading."""
    return pprint.pformat(value, width=112, compact=True, sort_dicts=False)


def near_limit(value, decimals=6, margin=0.05) -> bool:
    """True when value is within margin units of its last decimal from a rounding limit."""
    scaled = abs(float(value)) * 10 ** decimals
    return abs(scaled - math.floor(scaled) - 0.5) < margin


def not_dyadic(values) -> bool:
    return all(abs(x * 2 ** 20 - round(x * 2 ** 20)) > 1e-9 for x in values)


def build_constants() -> dict:
    """The literals written in the cells, by placeholder, with the assertions that make the data and the hidden cases
    fair."""
    import itertools
    from fractions import Fraction

    import numpy as np
    from scipy import stats

    out = {}

    # MB6.14: the stand of four market gardeners, built from dividends (one negative pair, one triple), given as worths
    dividends14 = {(0,): 3, (1,): 5, (2,): 2, (3,): 4, (0, 1): 2, (1, 2): -1, (2, 3): 3, (0, 1, 3): Fraction(3, 2)}
    table14 = [(T, float(sum(d for D, d in dividends14.items() if set(D) <= set(T))))
               for size in range(5) for T in itertools.combinations(range(4), size)]
    assert dict(table14)[(0, 1, 2, 3)] == 19.5
    out["__TABLE_14__"] = literal(table14)

    # MB6.15: hidden points (non-dyadic), the fields far from a rounding limit at 6 decimals
    points15 = [(1.37, -0.62), (-0.83, 1.94), (2.41, 0.29), (0.56, -1.73)]
    for x, y in points15:
        assert not_dyadic([x, y])
        for value in (2 * x * y * y + 5, 2 * x * x * y, 2 * y, 3 * x * x):
            assert not near_limit(value), (x, y, value)
    out["__HIDDEN_C15__"] = literal({"points": points15, "id_F_15": "MB6.15d", "id_G_15": "MB6.15e"})

    # MB6.16: the minerals of work_c/nb_values.py (one tie on Mohs's scale)
    mohs, vickers = [2, 3, 3, 4, 5, 5.5, 6, 7, 8], [32, 110, 150, 600, 540, 190, 1400, 800, 1100]
    rho16 = stats.spearmanr(mohs, vickers)[0]
    assert round(rho16, 4) == 0.8787 and not near_limit(rho16)
    out["__MOHS_16__"], out["__VICKERS_16__"] = literal(mohs), literal(vickers)

    # MB6.18: the estimates of b) are far from a rounding limit at 7 decimals
    rng = np.random.default_rng(7918)
    for rho in (0.0, 0.5, 0.9):
        pairs = rng.multivariate_normal([22.0, 70.0], [[9.0, 24.0 * rho], [24.0 * rho, 64.0]], size=300_000)
        keep = np.abs(pairs[:, 0] - 26) <= 0.25
        for value in (np.exp(0.4 + 0.05 * (pairs[:, 1] - 70)).mean(),
                      np.exp(0.1 * (pairs[keep, 0] - 22) + 0.05 * (pairs[keep, 1] - 70)).mean()):
            assert not near_limit(value, 7), (rho, value)

    # MB6.20: the samples of b) (work_c/nb_values.py), and the hidden cases: other numbers of players (never 1, 2, 3,
    # 4, 5, 6, 7, 8, 9: the colleague's check, the stub, the Évités, the questions), samples with groups of 2 and 3
    # ties (non-dyadic), values read between two cells (t never 0, 1/2 or 1; arrays non-dyadic)
    x20, y20 = [5.1, 3.5, 4.3, 5.1, 4.7, 4.7, 4.7], [3.0, 1.0, 2.0, 4.5, 5.0, 1.5, 4.0]
    out["__X_20__"], out["__Y_20__"] = literal(x20), literal(y20)
    players = [11, 14, 17]
    for n in players:                                     # far from a rounding limit at 11 decimals
        assert not any(near_limit(math.factorial(s) * math.factorial(n - 1 - s) / math.factorial(n), 11, 0.02)
                       for s in range(n))
    samples = [[3.71, 1.94, 3.71, 2.58, 1.94, 3.71, 0.66], [-0.37, 2.15, 2.15, -1.08, 0.94, 2.15, 0.94, 5.26],
               [7.3, 6.1, 6.1, 8.9, 7.3, 6.1, 5.2, 9.4, 7.3]]
    for sample in samples:
        assert not_dyadic(sample)
        average = stats.rankdata(sample)
        for method in ("min", "max", "dense", "ordinal"):
            assert not np.allclose(stats.rankdata(sample, method=method), average)
        counts = sorted({sample.count(v) for v in sample if sample.count(v) > 1})
        assert counts, sample
    assert any(set(sorted(sample.count(v) for v in set(sample))) >= {2, 3} for sample in samples)
    lerps = [(-3.7, 5.9, 0.23), (12.4, 2.3, 0.85), (0.61, 8.43, 0.38), ([1.37, -0.64, 2.91], [4.03, 0.29, -1.58], 0.35)]
    for a, b, t in lerps:
        assert t not in (0, 0.5, 1) and not_dyadic(np.ravel([a, b]).tolist())
        right, bad = (1 - t) * np.array(a) + t * np.array(b), (1 - t) * np.array(b) + t * np.array(a)
        assert not np.allclose(right, bad) and not any(near_limit(v, 9) for v in np.ravel(right))
    out["__CASES_C20__"] = literal({"players": players, "samples": samples, "lerps": lerps, "id_weights": "MB6.20d",
                                    "id_ranks": "MB6.20e", "id_lerps": "MB6.20f"})

    # MB6.22: the notebook council is the one of the hidden module; its exact indices by integers and fractions agree
    # with the floats of the hidden module, and the solution's function is not a copy of the module's
    challenge = load_module(ROOT / "solutions" / "challenges" / "mb6_22.py", "mb6_22_build")
    weights22 = (12, 9, 9, 7, 6, 6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1)
    assert challenge.NOTEBOOK_WEIGHTS == weights22 and challenge.NOTEBOOK_QUOTA == 66 and sum(weights22) == 98
    exact = challenge.exact_fractions(weights22, 66)
    assert sum(exact) == 1 and np.allclose([float(x) for x in exact], challenge.exact_indices(weights22, 66),
                                           rtol=0, atol=1e-15)
    assert not any(near_limit(float(x)) for x in exact)
    out["__WEIGHTS_22__"] = literal(weights22)
    return out


PREPARED = []


def prepare() -> None:
    """Write the build-time literals in every cell text (placeholders __NAME__). Idempotent."""
    if PREPARED:
        return
    constants = build_constants()

    def fill(text):
        for key, value in constants.items():
            text = text.replace(key, value)
        return text

    for part in PARTS:
        part.given = fill(part.given)
        for exercise in part.exercises:
            for field_name in ("body", "todo", "check", "solution", "record", "given", "note"):
                setattr(exercise, field_name, fill(getattr(exercise, field_name)))
            exercise.after = [(kind, fill(text)) for kind, text in exercise.after]
    left = {match for part in PARTS for exercise in part.exercises
            for text in (exercise.body, exercise.todo, exercise.check, exercise.solution, exercise.record,
                         exercise.given, *(t for _, t in exercise.after))
            for match in re.findall(r"__[A-Z][A-Z0-9_]*__", text)}
    assert not left, f"placeholders left: {sorted(left)}"
    PREPARED.append(True)


def main() -> int:
    prepare()
    for paper in PAPER:
        lines = [f'wbm.record("{paper.id}{letter}", {expr}{", " + options if options else ""})'
                 for letter, _, expr, options in paper.subs]
        check_unique_keys("\n".join(lines), paper.id)
    for exercise in [e for part in PARTS for e in part.exercises]:
        for source in (exercise.record, *(text for kind, text in exercise.after if kind == "record")):
            if source:
                check_unique_keys(source, exercise.id)
    write_notebook(f"{FOLDER}/03_notebook.ipynb", build("exercise"))
    write_notebook(f"{FOLDER}/05_solutions.ipynb", build("solution"))
    n_checks = sum(len(p.subs) for p in PAPER)
    n_ex = sum(len(part.exercises) for part in PARTS)
    print(f"✅ {FOLDER}/03_notebook.ipynb and 05_solutions.ipynb written ({len(PAPER)} paper exercises, "
          f"{n_checks} paper checks, {n_ex} notebook exercises)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
