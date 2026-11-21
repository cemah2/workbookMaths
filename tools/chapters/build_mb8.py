#!/usr/bin/env python
"""Build the two notebooks of chapter MB8 from a single source (used by Claude).

    python tools/chapters/build_mb8.py
    python tools/run_all_notebooks.py chapitres/mb8_gradient_politique/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/mb8_gradient_politique/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ MB8.1 to MB8.7, 🔗 MB8.11), each answer computed in the notebook from the data of
its statement (closed forms for the waits on the phone, exact fractions for the pots and the panel, NumPy for the truck,
the road, the tournament and the canteen), each wrong value computed by the error its message names; parts A to D are
the notebook exercises (MB8.13 to MB8.21), exactly as 02_exercices.md describes them. Wrong-answer messages state a
rule, never a number of the answer, the last step that gives it, nor another sub-question; none replays an error of the
corrected versions of the frontier exercises of workbookIA B8 nor of their neighbours (the dynamics differentiated,
the positivity of the probabilities, causality, a baseline that depends on the action or is computed on the draw itself, e_a forgotten, the sign of
an advantage, the next value read at the wrong index, λ alone, the max for the min, a sum for a mean, the inverted
difference, a naive computation that overflows, β forgotten, the decimal logarithm, normalisation taken for a
baseline, an unbiased estimate believed to be enough).

Data. The notebook exercises take the data of the paper exercises (a data cell of part A, read only), the data of their
own statements (the MDP of 🔨 MB8.14, the log-densities of 🔨 MB8.15, the league of 🔨 MB8.16, the tournaments of
🐛 MB8.19, the trial case of 🏆 MB8.21, written as literals) and their own draws: 8113 (the waits of 🔨 MB8.13), 8117
(the samples of 🔮 MB8.17), 8118 to 8120 (🔬 MB8.18), 8121 to 8123 and 8126 (🐛 MB8.19 and the colleague's check), 8124
(the MDPs of the corrected version of 🛠️ MB8.20), 8125 (the draws of the trial case of 🏆 MB8.21). Seeds 8101 to 8149
only (the tests use 8000 to 8090, the figures 8091 to 8099). The γ are 0.6 and 0.7 (the MDPs of 🛠️ MB8.20 included).
The check cells never hold the code that solves an exercise nor a value that gives an answer without a calculation: the
expected values are recorded by the solutions as hidden sub-IDs and compared with ``wbm.check(..., computed=True)``
(the hidden cases of 🐛 MB8.19, the order of size of the deviations of 🔬 MB8.18), or given by properties (the hidden
methods of 🛠️ MB8.20, which live in ``solutions/challenges/mb8_20.py`` so that no cell shows a solution of 🔨 MB8.14).
The hidden part of 🏆 MB8.21 lives in ``solutions/challenges/mb8_21.py``: the check cell runs it in another process,
which draws the hidden laws at each run, serves the draws and counts them, and measures the estimates it receives only
at the end, so that no hidden law, parameter nor derivative lives in the notebook's process. The check cells use their
own data, never the test cases of tests/test_mb8_policy_gradient.py, the examples of the docstrings of the stub
policy_gradient, the examples of the fiche, nor the numbers of workbookIA B8 to B1 (the notes of MB8 in the syllabus
and their list « Évités »).
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

CHAPTER = "MB8"
FOLDER = "chapitres/mb8_gradient_politique"


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
    Paper("MB8.1", syllabus_entry("MB8.1")[3], [
        ("a", "a number (4 decimals): P(X > c)", "TAIL_1",
         '''decimals=4,
           mistakes={"ici θ est un taux : la moyenne de X vaut 1/θ, pas θ": math.exp(-C_1 / RATE_1),
                     "P(X > c) est la probabilité de dépasser c, le complément de la fonction de répartition en c":
                         1 - TAIL_1}'''),
        ("b", "a number (4 decimals): d/dθ P(X > c), by the closed form", "DERIV_1",
         '''decimals=4,
           mistakes={"la dérivée de e^{−θc} par rapport à θ fait sortir le facteur −c": -TAIL_1,
                     "ici θ est un taux : on dérive par rapport au taux, pas par rapport à la moyenne 1/θ":
                         C_1 * RATE_1 ** 2 * TAIL_1}'''),
        ("c", "a list of 2 numbers (4 decimals): E[1{X > c}] / θ, then E[X 1{X > c}]",
         "[TAIL_1 / RATE_1, (C_1 + 1 / RATE_1) * TAIL_1]",
         '''decimals=4,
           mistakes={"sachant X > c, la moyenne de X n'est pas la moyenne 1/θ de la loi entière":
                         [TAIL_1 / RATE_1, TAIL_1 / RATE_1],
                     "sachant X > c, X dépasse c, puis attend encore : sa moyenne conditionnelle dépasse c":
                         [TAIL_1 / RATE_1, C_1 * TAIL_1]}'''),
        ("d", "a list of 2 numbers (2 decimals): the path derivatives of E[X], then of P(X > c)",
         "[-1 / RATE_1 ** 2, 0.0]",
         '''decimals=2,
           mistakes={"la dérivée de 1/θ par rapport à θ est −1/θ², pas −1/θ": [-1 / RATE_1, 0.0],
                     "ici X = ξ/θ : on dérive par rapport au taux θ, pas par rapport à la moyenne": [1.0, 0.0]}'''),
        ("e", "a number (2 decimals): the variance of g(X), at one draw", "SQUARE_1 - DERIV_1 ** 2",
         '''decimals=2,
           mistakes={"une variance retranche le carré de l'espérance de l'estimateur": SQUARE_1,
                     "sachant X > c, 1/θ − X n'est pas centré : son carré moyen ajoute le carré de sa moyenne":
                         TAIL_1 / RATE_1 ** 2 - DERIV_1 ** 2,
                     "la variance d'un produit de deux variables dépendantes n'est pas le produit de leurs variances":
                         TAIL_1 * (1 - TAIL_1) / RATE_1 ** 2}'''),
    ]),

    Paper("MB8.2", syllabus_entry("MB8.2")[3], [
        ("a", "a list of 3 numbers (2 decimals): the scores s(0), s(1), s(2)", "floats(SCORE_2)",
         '''decimals=2,
           mistakes={"ln p_θ(x) contient aussi (2 − x) ln(1 − θ), qui dépend de θ": floats([k / THETA_2 for k in range(3)]),
                     "la dérivée de ln(1 − θ) par rapport à θ est −1/(1 − θ)":
                         floats([k / THETA_2 + (2 - k) / (1 - THETA_2) for k in range(3)])}'''),
        ("b", "a number (2 decimals): d/dθ E[f(X)]", "floats(DERIV_2)",
         '''decimals=2,
           mistakes={"P(X = 1) = 2θ(1 − θ) : il y a deux façons d'avoir une seule pousse":
                         floats(PRICE_2[1] * (1 - 2 * THETA_2) + 2 * PRICE_2[2] * THETA_2),
                     "P(X = 2) = θ² n'est pas linéaire en θ : sa dérivée est 2θ":
                         floats(2 * PRICE_2[1] * (1 - 2 * THETA_2) + PRICE_2[2])}'''),
        ("c", "a number (2 decimals): the variance without baseline (b = 0), at one draw", "floats(variance_2(0))",
         '''decimals=2,
           mistakes={"une variance retranche le carré de la moyenne de f s, qui est la dérivée":
                         floats(variance_2(0) + DERIV_2 ** 2),
                     "f et s viennent du même tirage : E[f² s²] n'est pas le produit E[f²] E[s²]":
                         floats(mean_2([f * f for f in PRICE_2]) * mean_2([s * s for s in SCORE_2]) - DERIV_2 ** 2)}'''),
        ("d", "a number (2 decimals): the variance with b = E[f(X)], at one draw", "floats(variance_2(mean_2(PRICE_2)))",
         '''decimals=2,
           mistakes={"une variance retranche le carré de la moyenne de (f − b) s, qui est encore la dérivée":
                         floats(variance_2(mean_2(PRICE_2)) + DERIV_2 ** 2),
                     "l'estimateur est (f − b) s : la variance porte sur ce produit, pas sur f − b seul":
                         floats(mean_2([f * f for f in PRICE_2]) - mean_2(PRICE_2) ** 2)}'''),
        ("e", "a list of 2 numbers (3 decimals): b*, then the variance with b*",
         "floats([bstar_2(), variance_2(bstar_2())])",
         '''decimals=3,
           mistakes={"les espérances de b* sont pondérées par les probabilités des trois issues":
                         floats([bstar_2(weighted=False), variance_2(bstar_2(weighted=False))]),
                     "une variance retranche le carré de la dérivée, même avec la baseline optimale":
                         floats([bstar_2(), variance_2(bstar_2()) + DERIV_2 ** 2])}'''),
    ]),

    Paper("MB8.3", syllabus_entry("MB8.3")[3], [
        ("a", "a 2 x 2 matrix (3 decimals), as a list of rows: P_pi (market, park)", "P_3.tolist()",
         '''decimals=3,
           mistakes={"rester ne garantit pas de rester : le placier renvoie parfois le camion au parc":
                         chain_3(stay=np.array([1.0, 0.0]))[0].tolist(),
                     "P_π mélange les lignes des deux actions avec les probabilités π(a | marché), pas à parts égales":
                         chain_3(pi=np.array([0.5, 0.5]))[0].tolist()}'''),
        ("b", "a list of 2 numbers (2 decimals): V(market), V(park)", "V_3.tolist()",
         '''decimals=2,
           mistakes={"V(s) somme les récompenses actualisées de tous les jours à venir, pas seulement celle du jour":
                         R_3.tolist(),
                     "le camion passe d'un emplacement à l'autre : V = r_π + γ P_π V couple les deux équations":
                         (R_3 / (1 - GAMMA_3)).tolist()}'''),
        ("c", "a list of 2 numbers (3 decimals): M[market, market], then M[park, market]", "M_3[:, 0].tolist()",
         '''decimals=3,
           mistakes={"la question demande (I − γ P_π)⁻¹ elle-même, sans le facteur 1 − γ de la loi d'occupation":
                         ((1 - GAMMA_3) * M_3[:, 0]).tolist(),
                     "la colonne du marché garde l'état d'arrivée fixe et fait varier l'état de départ": M_3[0, :].tolist()}'''),
        ("d", "a list of 4 numbers (4 decimals): Q(market, stay), Q(market, leave), A(market, stay), A(market, leave)",
         "Q_3.tolist() + A_3.tolist()",
         '''decimals=4,
           mistakes={"rester mène parfois au parc : l'espérance de V au lendemain mélange les deux emplacements":
                         [SALES_3[0] + GAMMA_3 * V_3[0], Q_3[1], SALES_3[0] + GAMMA_3 * V_3[0] - V_3[0], A_3[1]],
                     "V(marché) moyenne les deux Q avec les probabilités de la politique, pas à parts égales":
                         Q_3.tolist() + (Q_3 - Q_3.mean()).tolist()}'''),
        ("e", "a list of 4 numbers (4 decimals): dV(market)/dz(market, stay), dV(market)/dz(market, leave), "
              "dV(park)/dz(market, stay), dV(park)/dz(market, leave)", "GRAD_3.ravel().tolist()",
         '''decimals=4,
           mistakes={"∂V(s₀)/∂z(s, a) = ν_{s₀}(s) π(a | s) A(s, a) / (1 − γ) : le facteur 1/(1 − γ) compte":
                         ((1 - GAMMA_3) * GRAD_3).ravel().tolist(),
                     "V(s₀) dépend du logit par toutes les visites futures du marché : le facteur M[s₀, marché] compte":
                         (PI_3 * A_3).tolist() * 2}'''),
    ]),

    Paper("MB8.4", syllabus_entry("MB8.4")[3], [
        ("a", "a list of 3 numbers (3 decimals): the bias of the 1-step return from each state (good, worn, works)",
         "(GAMMA_4 * P_4 @ ERR_4).tolist()",
         '''decimals=3,
           mistakes={"l'erreur du retour à 1 pas vient de l'état du lendemain, tiré selon P : pas de l'état de départ":
                         (GAMMA_4 * ERR_4).tolist(),
                     "l'état du lendemain se tire avec la ligne de l'état de départ : les lois sont les lignes de P_π":
                         (GAMMA_4 * P_4.T @ ERR_4).tolist()}'''),
        ("b", "a list of 3 numbers (4 decimals): the bias of the 2-step return from each state",
         "(GAMMA_4 ** 2 * P_4 @ P_4 @ ERR_4).tolist()",
         '''decimals=4,
           mistakes={"deux pas plus loin, l'état suit la loi P², et l'erreur est actualisée par γ²":
                         (GAMMA_4 ** 2 * P_4 @ ERR_4).tolist(),
                     "le retour à 2 pas actualise l'erreur deux fois, par γ²": (GAMMA_4 * P_4 @ P_4 @ ERR_4).tolist()}'''),
        ("c", "a list of 2 numbers: the weight of the 5-step return (4 decimals), then an integer k",
         "[(1 - LAMBDA_4) * LAMBDA_4 ** 4, tail_k_4()]",
         '''decimals=4,
           mistakes={"le poids d'un retour à k pas porte aussi le facteur 1 − λ": [LAMBDA_4 ** 4, tail_k_4()],
                     "le poids du retour à k pas est (1 − λ)λ^{k−1} : l'exposant de λ est k − 1":
                         [(1 - LAMBDA_4) * LAMBDA_4 ** 5, tail_k_4()],
                     "les retours de plus de k pas pèsent ensemble la somme de tous les poids suivants, pas le seul poids "
                     "suivant": [(1 - LAMBDA_4) * LAMBDA_4 ** 4, tail_k_4(lambda k: (1 - LAMBDA_4) * LAMBDA_4 ** k)]}'''),
        ("d", "a number (4 decimals): the bias of the lambda-return when the error is 2 everywhere",
         "CONST_4 * (1 - LAMBDA_4) * GAMMA_4 / (1 - GAMMA_4 * LAMBDA_4)",
         '''decimals=4,
           mistakes={"les poids (1 − λ)λ^{k−1} somment à 1 : n'oublie pas le facteur 1 − λ":
                         CONST_4 * GAMMA_4 / (1 - GAMMA_4 * LAMBDA_4),
                     "le poids du retour à k pas est (1 − λ)λ^{k−1} : l'exposant de λ est k − 1":
                         CONST_4 * (1 - LAMBDA_4) * GAMMA_4 * LAMBDA_4 / (1 - GAMMA_4 * LAMBDA_4)}'''),
    ]),

    Paper("MB8.5", syllabus_entry("MB8.5")[3], [
        ("a", "a list of 3 numbers (2 decimals): the weights w = p/q of the three classes", "floats(W_5)",
         '''decimals=2,
           mistakes={"un poids d'importance est un rapport de deux probabilités, pas leur différence":
                         floats([p - q for p, q in zip(P_5, Q_5)]),
                     "le poids d'une classe compare sa part dans le recensement à sa part dans le panel, pas à 1/3":
                         floats([3 * p for p in P_5])}'''),
        ("b", "a list of 2 numbers (2 decimals): the raw mean spending of the panel, then the reweighted one",
         "floats([mean_5(F_5), mean_5([w * f for w, f in zip(W_5, F_5)])])",
         '''decimals=2,
           mistakes={"la moyenne repondérée pondère encore chaque classe par sa part q dans le panel : Σ q w f":
                         floats([mean_5(F_5), sum(w * f for w, f in zip(W_5, F_5))]),
                     "la moyenne brute du panel pondère chaque classe par sa part dans le panel, pas à parts égales":
                         floats([sum(F_5) / 3, mean_5([w * f for w, f in zip(W_5, F_5)])])}'''),
        ("c", "a number (2 decimals): Kish's effective size of the six panelists", "floats(kish_5())",
         '''decimals=2,
           mistakes={"la somme des poids n'est pas une taille effective : divise son carré par la somme des carrés":
                         floats(sum(W_5[k] for k in SAMPLE_5)),
                     "une taille effective est comprise entre 1 et n : vérifie l'ordre du quotient":
                         floats(sum(W_5[k] ** 2 for k in SAMPLE_5) / sum(W_5[k] for k in SAMPLE_5))}'''),
        ("d", "a list of 2 numbers (2 decimals): the reweighted mean with the weights min(w, 1.6), then its bias",
         "floats([capped_5(), capped_5() - mean_5([w * f for w, f in zip(W_5, F_5)])])",
         '''decimals=2,
           mistakes={"le biais se mesure par rapport à la vraie moyenne, celle du recensement":
                         floats([capped_5(), capped_5() - mean_5(F_5)]),
                     "la question demande les poids tronqués sans les diviser par leur somme":
                         floats([capped_5(True), capped_5(True) - mean_5([w * f for w, f in zip(W_5, F_5)])])}'''),
        ("e", "a number (5 decimals): KL(q || p)", "KL_5",
         '''decimals=5,
           mistakes={"la KL moyenne les ln(q/p) avec les poids q de chaque classe":
                         sum(math.log(q / p) for q, p in zip(Q_5, P_5)),
                     "la KL moyenne des logarithmes de rapports, pas les rapports moins 1":
                         sum(float(q) * float(q / p - 1) for q, p in zip(Q_5, P_5))}'''),
        ("f", "a list of 3 numbers (4 decimals): k1 for a panelist of each class", "K1_5",
         '''decimals=4,
           mistakes={"k₁ est la valeur d'un tirage de la classe, pas sa contribution q k₁ à la moyenne":
                         [float(q) * k for q, k in zip(Q_5, K1_5)],
                     "k₁ est un logarithme : il prend −ln w, pas w − 1": floats([w - 1 for w in W_5])}'''),
        ("g", "a list of 3 numbers (4 decimals): k3 for a panelist of each class", "K3_5",
         '''decimals=4,
           mistakes={"k₃ est la valeur d'un tirage de la classe, pas sa contribution q k₃ à la moyenne":
                         [float(q) * k for q, k in zip(Q_5, K3_5)],
                     "k₃ retranche aussi 1 : (w − 1) − ln w s'annule quand le poids vaut 1":
                         [float(w) - math.log(w) for w in W_5]}'''),
    ]),

    Paper("MB8.6", syllabus_entry("MB8.6")[3], [
        ("a", "a number (4 decimals): A and B alone, beta_A - beta_B", "math.log(WINS_6[0, 1] / WINS_6[1, 0])",
         '''decimals=4,
           mistakes={"les forces sont des logits : σ(β_A − β_B) vaut la part des victoires de A, pas β_A − β_B lui-même":
                         float((WINS_6[0, 1] - WINS_6[1, 0]) / MATCHES_6[0, 1]),
                     "σ(d) = 2/7 : d est le logit de 2/7, pas le logarithme de 2/7":
                         math.log(WINS_6[0, 1] / MATCHES_6[0, 1])}'''),
        ("b", "a list of 3 numbers (2 decimals): the expected wins of A against B, of A against C, of B against C",
         "expected_6(PROPOSED_6)",
         '''decimals=2,
           mistakes={"les victoires attendues se calculent avec les forces proposées, pas en recopiant le tableau":
                         [WINS_6[0, 1], WINS_6[0, 2], WINS_6[1, 2]],
                     "les nombres proposés sont les p_i = e^{β_i}, pas les forces : σ(β_i − β_j) = p_i/(p_i + p_j)":
                         expected_6(np.exp(PROPOSED_6))}'''),
        ("c", "a list of 3 numbers (4 decimals): the centred strengths beta_A, beta_B, beta_C", "BETA_6.tolist()",
         '''decimals=4,
           mistakes={"chaque paire seule ne suffit pas : les forces se lisent sur toutes les rencontres du tournoi à la fois":
                         centred_6([math.log(WINS_6[0, 1] / WINS_6[1, 0]), 0.0, math.log(WINS_6[2, 1] / WINS_6[1, 2])]),
                     "le rapport victoires sur défaites de chaque club ne tient pas compte de la force de ses adversaires":
                         centred_6(np.log(WINS_6.sum(axis=1) / WINS_6.sum(axis=0)))}'''),
        ("d", "a number (4 decimals): the probability that C beats A at a next match",
         "PROPOSED_6[2] / (PROPOSED_6[2] + PROPOSED_6[0])",
         '''decimals=4,
           mistakes={"C n'a jamais battu A, mais le modèle prédit à partir de tout le tournoi": 0,
                     "σ(β_C − β_A) = e^{β_C}/(e^{β_C} + e^{β_A}), pas e^{β_C}/e^{β_A}": PROPOSED_6[2] / PROPOSED_6[0]}'''),
        ("e", "a list of 2 numbers (1 decimal): the Elo gap R_A - R_C, then the points C wins if it beats A",
         "[GAP_6, K_6 * (1 - PROPOSED_6[2] / (PROPOSED_6[2] + PROPOSED_6[0]))]",
         '''decimals=1,
           mistakes={"un vainqueur outsider gagne d'autant plus de points que sa victoire était improbable":
                         [GAP_6, K_6 * PROPOSED_6[2] / (PROPOSED_6[2] + PROPOSED_6[0])],
                     "la probabilité de victoire se lit sur l'écart des cotes, elle ne vaut pas ½": [GAP_6, K_6 / 2]}'''),
    ]),

    Paper("MB8.7", syllabus_entry("MB8.7")[3], [
        ("a", "a list of 3 numbers (4 decimals): beta = 1, the law pi* (gratin, couscous, lasagne)",
         "gibbs_7(1.0)[0].tolist()",
         '''decimals=4,
           mistakes={"π* multiplie π_ref par e^{r/β}, pas par r": (REF_7 * R_7 / (REF_7 * R_7).sum()).tolist(),
                     "π* garde le facteur π_ref : la loi actuelle compte": (np.exp(R_7) / np.exp(R_7).sum()).tolist()}'''),
        ("b", "a number (4 decimals): beta = 1, the value beta ln Z", "gibbs_7(1.0)[1]",
         '''decimals=4,
           mistakes={"la valeur est β ln Z, le logarithme de la constante de normalisation, pas Z": math.exp(gibbs_7(1.0)[1]),
                     "la valeur retranche β KL(π* ‖ π_ref) à la satisfaction moyenne sous π*":
                         float(gibbs_7(1.0)[0] @ R_7)}'''),
        ("c", "a list of 2 numbers (4 decimals): beta = 1, F(pi_ref), then F for the best dish alone",
         "[objective_7(REF_7, 1.0), objective_7([0.0, 0.0, 1.0], 1.0)]",
         '''decimals=4,
           mistakes={"le meilleur plat seul s'écarte de π_ref : il paie aussi β KL": [objective_7(REF_7, 1.0), float(R_7.max())],
                     "sous π_ref, la satisfaction moyenne pondère chaque plat par sa part dans la loi actuelle":
                         [float(R_7.mean()), objective_7([0.0, 0.0, 1.0], 1.0)]}'''),
        ("d", "a list of 4 numbers (4 decimals): beta = 3, the law pi*, then the value beta ln Z",
         "gibbs_7(3.0)[0].tolist() + [gibbs_7(3.0)[1]]",
         '''decimals=4,
           mistakes={"la valeur retranche β KL(π* ‖ π_ref) à la satisfaction moyenne sous π*":
                         gibbs_7(3.0)[0].tolist() + [float(gibbs_7(3.0)[0] @ R_7)],
                     "avec β = 3, les exposants sont r/β, pas β r": gibbs_7(1 / 3.0)[0].tolist() + [3 * math.log(
                         float((REF_7 * np.exp(3 * R_7)).sum()))]}'''),
    ]),

    Paper("MB8.11", syllabus_entry("MB8.11")[3], [
        ("a", "a list of 8 numbers (2 decimals): the eight scores at theta = 2.5", "S_11.tolist()",
         '''decimals=2,
           mistakes={"le score de la loi de Poisson est x/θ − 1 : la dérivée de −θ compte": (X_11 / THETA_11).tolist(),
                     "la dérivée de x ln θ par rapport à θ est x/θ, pas x/θ²": (X_11 / THETA_11 ** 2 - 1).tolist()}'''),
        ("b", "a number (4 decimals): dL/dtheta at theta = 2.5, with b = 1", "derivative_11(1.0)",
         '''decimals=4,
           mistakes={"le score de la loi de Poisson contient −1, la dérivée de −θ": derivative_11(1.0, X_11 / THETA_11),
                     "le score se calcule au paramètre θ de la loi, pas à la moyenne des huit tirages":
                         derivative_11(1.0, X_11 / X_11.mean() - 1)}'''),
        ("c", "a number (4 decimals): the same derivative, with b = 0", "derivative_11(0.0)",
         '''decimals=4,
           mistakes={"le score de la loi de Poisson contient −1, la dérivée de −θ": derivative_11(0.0, X_11 / THETA_11),
                     "le score se calcule au paramètre θ de la loi, pas à la moyenne des huit tirages":
                         derivative_11(0.0, X_11 / X_11.mean() - 1)}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (closed forms for the waits, exact fractions for the pots and
# the panel, NumPy for the truck, the road, the tournament and the canteen)
import math
from fractions import Fraction as F

import numpy as np


def floats(values):
    """A number or a list of numbers (fractions) as a float or a list of floats (-0.0 written 0.0)."""
    return (np.round(np.asarray([float(v) for v in values] if isinstance(values, (list, tuple)) else float(values),
                                dtype=float), 12) + 0.0).tolist()


# MB8.1: the wait X, exponential of rate 0.1 per minute; a voucher beyond c = 18 minutes; g(X) = 1{X > c} s(X)
RATE_1, C_1 = 0.1, 18.0
TAIL_1 = math.exp(-RATE_1 * C_1)                        # P(X > c)
DERIV_1 = -C_1 * TAIL_1                                  # its derivative in the rate
SQUARE_1 = TAIL_1 * (1 / RATE_1 ** 2 + C_1 ** 2)        # E[g(X)²]: beyond c, X = c + Y, Y exponential of rate θ

# MB8.2: two seeds per pot, X ~ B(2, 3/4); the prices 0, 3.50 and 5 euros
THETA_2, PRICE_2 = F(3, 4), (F(0), F(7, 2), F(5))
LAW_2 = ((1 - THETA_2) ** 2, 2 * THETA_2 * (1 - THETA_2), THETA_2 ** 2)
SCORE_2 = tuple((k - 2 * THETA_2) / (THETA_2 * (1 - THETA_2)) for k in range(3))


def mean_2(values):
    """E[values(X)] under B(2, 3/4), exactly."""
    return sum(p * v for p, v in zip(LAW_2, values))


DERIV_2 = mean_2([f * s for f, s in zip(PRICE_2, SCORE_2)])


def variance_2(b):
    """The variance of (f(X) - b) s(X) at one draw, exactly."""
    return mean_2([((f - b) * s) ** 2 for f, s in zip(PRICE_2, SCORE_2)]) - DERIV_2 ** 2


def bstar_2(weighted=True):
    """b* = E[f s²] / E[s²]; weighted=False: the three outcomes without their probabilities (a classic error)."""
    if weighted:
        return mean_2([f * s * s for f, s in zip(PRICE_2, SCORE_2)]) / mean_2([s * s for s in SCORE_2])
    return sum(f * s * s for f, s in zip(PRICE_2, SCORE_2)) / sum(s * s for s in SCORE_2)


# MB8.3: the crêpe truck; state 0 the market (stay or leave), state 1 the park (fixed); gamma = 0.7
STAY_3, LEAVE_3, PARK_3 = np.array([0.86, 0.14]), np.array([0.0, 1.0]), np.array([0.3, 0.7])
SALES_3, PARK_SALES_3, GAMMA_3 = np.array([3.0, 0.0]), 4.0, 0.7
PI_3 = np.exp([math.log(3), 0.0]) / np.exp([math.log(3), 0.0]).sum()     # pi(stay | market), pi(leave | market)


def chain_3(pi=PI_3, stay=STAY_3):
    """P_pi and r_pi (rows and entries: market, park)."""
    return np.array([pi[0] * stay + pi[1] * LEAVE_3, PARK_3]), np.array([pi @ SALES_3, PARK_SALES_3])


P_3, R_3 = chain_3()
M_3 = np.linalg.inv(np.eye(2) - GAMMA_3 * P_3)
V_3 = M_3 @ R_3
Q_3 = np.array([SALES_3[0] + GAMMA_3 * STAY_3 @ V_3, SALES_3[1] + GAMMA_3 * LEAVE_3 @ V_3])
A_3 = Q_3 - V_3[0]
GRAD_3 = np.array([[M_3[s0, 0] * PI_3[a] * A_3[a] for a in range(2)] for s0 in range(2)])

# MB8.4: the road (good, worn, works); gamma = 0.6, lambda = 0.7; the errors e of the estimated values
P_4 = np.array([[0.85, 0.15, 0.0], [0.0, 0.7, 0.3], [0.85, 0.0, 0.15]])
GAMMA_4, LAMBDA_4, ERR_4, CONST_4 = 0.6, 0.7, np.array([3.0, 0.0, 2.0]), 2.0


def tail_k_4(weight=lambda k: LAMBDA_4 ** k, threshold=0.05):
    """The smallest k whose weight is below the threshold: the returns of more than k steps weigh lambda^k together
    (weight=(1 - lambda) lambda^k: the next weight alone, a classic error)."""
    return next(k for k in range(1, 200) if weight(k) < threshold)


# MB8.5: the panel q against the census p, three age classes; the monthly spending f; six panelists; c = 1.6
Q_5, P_5 = (F(50, 100), F(25, 100), F(25, 100)), (F(26, 100), F(41, 100), F(33, 100))
F_5 = (F(36), F(50), F(44))
W_5 = tuple(p / q for p, q in zip(P_5, Q_5))
SAMPLE_5, CUT_5 = (0, 0, 0, 1, 2, 2), F(16, 10)


def mean_5(values):
    """E_q[values] over the three classes, exactly."""
    return sum(q * v for q, v in zip(Q_5, values))


def kish_5():
    """Kish's effective size of the six panelists."""
    weights = [W_5[k] for k in SAMPLE_5]
    return sum(weights) ** 2 / sum(w * w for w in weights)


def capped_5(normalized=False):
    """E_q[min(w, c) f]; normalized: divided by E_q[min(w, c)] (a classic error)."""
    value = mean_5([min(w, CUT_5) * f for w, f in zip(W_5, F_5)])
    return value / mean_5([min(w, CUT_5) for w in W_5]) if normalized else value


KL_5 = sum(float(q) * math.log(q / p) for q, p in zip(Q_5, P_5))
K1_5 = [-math.log(w) for w in W_5]
K3_5 = [float(w) - 1 - math.log(w) for w in W_5]

# MB8.6: the table-football tournament (wins of the row against the column), the proposed p_i, Elo with k = 32
WINS_6 = np.array([[0, 2, 10], [5, 0, 1], [0, 3, 0]], dtype=float)
MATCHES_6, PROPOSED_6, K_6 = WINS_6 + WINS_6.T, np.array([4.0, 3.0, 1.0]), 32


def expected_6(p):
    """The expected wins of A against B, of A against C, of B against C, with p_i / (p_i + p_j)."""
    return [MATCHES_6[i, j] * p[i] / (p[i] + p[j]) for i, j in ((0, 1), (0, 2), (1, 2))]


def centred_6(beta):
    beta = np.asarray(beta, dtype=float)
    return (beta - beta.mean()).tolist()


BETA_6 = np.array(centred_6(np.log(PROPOSED_6)))
GAP_6 = 400 / math.log(10) * (BETA_6[0] - BETA_6[2])

# MB8.7: the canteen, pi_ref and the satisfactions r; beta = 1 and beta = 3
REF_7, R_7 = np.array([0.45, 0.40, 0.15]), np.array([2.0, 4.0, 5.0])


def gibbs_7(beta):
    """pi* proportional to pi_ref e^{r/beta}, and the value beta ln Z."""
    tilted = REF_7 * np.exp(R_7 / beta)
    return tilted / tilted.sum(), beta * math.log(tilted.sum())


def objective_7(pi, beta):
    """F(pi) = E_pi[r] - beta KL(pi || pi_ref)."""
    pi = np.asarray(pi, dtype=float)
    return float(pi @ R_7) - beta * sum(x * math.log(x / y) for x, y in zip(pi, REF_7) if x > 0)


# MB8.11: the launderette, X ~ Poisson of mean 2.5, f(x) = max(0, x - 2); the batch of eight quarters of an hour
THETA_11, X_11 = 2.5, np.array([3, 1, 4, 2, 5, 1, 3, 4])
F_11, S_11 = np.maximum(0, X_11 - 2).astype(float), X_11 / 2.5 - 1


def derivative_11(b, scores=S_11):
    """dL/dtheta = -(1/n) sum (f(x_i) - b) s(x_i), the f(x_i) and b held fixed (scores: another score, an error)."""
    return -float(np.mean((F_11 - b) * scores))'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ MB8.1 à MB8.7 ; 🔗 MB8.11)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une liste `[0.2, -1]`, dans l'ordre que dit la question ; une matrice comme la liste de ses lignes, "
               "`[[1, 0], [0.5, 0.5]]`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")


def paper_part(kind: str) -> list:
    """The cells of Part 0."""
    return paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO)


# ---------------------------------------------------------------------------
# Notebook exercises: your library (MB8.13 to MB8.16)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to D)
import contextlib
import dis
import math
import numbers
import os
import re
import sys
import time
from fractions import Fraction
from types import MappingProxyType

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from wbm.errors import MymathMissingError
from wbm.nbtools import StopCheck, checked, drawn, filled, fr, refuses, run_pytest_group, verdict

TEST_MB8 = "tests/test_mb8_policy_gradient.py"       # the tests of mymath/policy_gradient.py
REF = wbm.load_mymath("ref", alias="mymath_ref")       # the reference: the colleague's code of MB8.19 relies on it
ref_pg = REF.policy_gradient


def shown(value, digits=4):
    """A short text for a result of the learner's code (the check messages): numbers rounded, as lists."""
    if value is None:
        return "None"
    try:
        return str(np.round(np.asarray(value, dtype=float), digits).tolist())[:160]
    except (TypeError, ValueError):
        return repr(value)[:160]


GENERIC_COMPUTED = "Ta fonction, ou le calcul qui l'utilise, ne donne pas la bonne valeur ici."


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
            if message.startswith(GENERIC_COMPUTED):            # one text, not two: the hint says what to look at
                message = GENERIC_COMPUTED
            message = f"{message} Piste : {extra}"
    icon = {"correct": "✅", "pending": "⏳", "unknown": "❓"}.get(result.status, "❌")
    print(f"{icon} Ex {ex_id} : {message}")
    return result


def library_hint(names):
    """A hint for a wrong answer computed with the learner's library (no classic error recognised): its tests first,
    then the call."""
    return lambda value: (f"si tu t'es servi de {names} de ta librairie et que ses tests passent tous (plus haut), "
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
    stops the block; yields the list of the names seen ("policy_gradient.importance_weights"). The learner's function
    must not run that code (mymath in a corrected function, the hidden module of a challenge). With escapes, opening a
    file of places or starting another process also stops it ("ouvre mb8_21.py", "lance un autre processus :
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
PHONE_1 = MappingProxyType({"rate": 0.1, "c": 18.0})                      # MB8.1: per minute; the voucher beyond c
POTS_2 = MappingProxyType({"theta": 0.75, "price": (0.0, 3.5, 5.0)})      # MB8.2: euros for 0, 1, 2 seedlings
TRUCK_3 = MappingProxyType({"stay": (0.86, 0.14), "leave": (0.0, 1.0), "sales_market": (3.0, 0.0),
                            "park": (0.3, 0.7), "sales_park": 4.0, "logits_market": (math.log(3), 0.0),
                            "gamma": 0.7})        # MB8.3: states (market, park); at the market, actions (stay, leave)
ROAD_4 = MappingProxyType({"P": frozen([[0.85, 0.15, 0.0], [0.0, 0.7, 0.3], [0.85, 0.0, 0.15]]), "gamma": 0.6,
                           "e": (3.0, 0.0, 2.0), "lambda": 0.7})          # MB8.4: (good, worn, works)
PANEL_5 = MappingProxyType({"q": (0.50, 0.25, 0.25), "p": (0.26, 0.41, 0.33), "f": (36.0, 50.0, 44.0),
                            "sample": (0, 0, 0, 1, 2, 2), "c": 1.6})       # MB8.5: (18-34, 35-59, 60 and more)
FOOTBALL_6 = MappingProxyType({"wins": frozen([[0, 2, 10], [5, 0, 1], [0, 3, 0]]), "proposed": (4.0, 3.0, 1.0),
                               "k": 32})                                  # MB8.6: clubs (A, B, C); row beats column
CANTEEN_7 = MappingProxyType({"pi_ref": (0.45, 0.40, 0.15), "r": (2.0, 4.0, 5.0), "betas": (1.0, 3.0)})   # MB8.7
LAUNDRY_11 = MappingProxyType({"theta": 2.5, "x": (3, 1, 4, 2, 5, 1, 3, 4)})   # MB8.11: customers per quarter hour'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="MB8")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en MB6). Ouvre ta copie `mon_travail/mymath/policy_gradient.py`, lis la "
         "docstring du module (ses conventions, et ce qui est permis) puis celle de la fonction, remplace chaque "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Dans le notebook, appelle tes fonctions par "
         "`mymath.policy_gradient.<nom>` (par exemple `mymath.policy_gradient.importance_weights(lp, lq)`), ou "
         "donne-leur un nom court (`importance_weights = mymath.policy_gradient.importance_weights`) dans une cellule "
         "exécutée après le rechargement. ⚠️ Le squelette n'importe rien : ajoute en tête du fichier `import math` et "
         "`import numpy as np`, et `from .markov import bellman_linear_solve` si tu reprends ta fonction de M26. NumPy "
         "et le module `math` sont permis ; de `np.linalg`, seulement `solve` et `matrix_rank` (dans "
         "`policy_gradient_exact`) ; ni SciPy (`scipy.optimize`, `scipy.special`…), ni scikit-learn : les tests "
         "comparent tes résultats à des sommes exactes, à des différences finies de valeurs calculées par "
         "`np.linalg.solve`, à `scipy.optimize.minimize` et à scikit-learn, et un test lit ton module. Rien n'y tire "
         "au hasard ; ne modifie jamais les tableaux reçus. Hors de `mymath`, le notebook peut se servir de tout NumPy "
         "et de SciPy.")

REMINDER = ("> Même mode d'emploi qu'en MB8.13 : écris la fonction dans ta copie `mon_travail/mymath/policy_gradient.py`, "
            "**enregistre**, puis exécute les cellules ci-dessous ; la première recharge ta librairie.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of policy_gradient.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("todo", f'run_pytest_group(TEST_MB8, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_MB8, "{keyword}", impl="ref")')]


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
    function it writes after its title (« · `importance_weights` »)."""
    kind, stars, minutes, title, tracks = syllabus_entry(ex_id)
    if functions:
        title = f"{title} · {functions}"
    return Ex(ex_id, kind, stars, minutes, title, goal, prereq, body=body, tracks=tracks, **fields)


# ---------------------------------------------------------------------------
# MB8.13 · score_function_gradient
# ---------------------------------------------------------------------------
GIVEN_13 = '''# 2 000 waits on the phone of MB8.1 (rate 0.1 per minute; seed 8113), their values f(x_i) = 1{x_i > 18} and their
# scores in the rate, read only
WAITS_13 = frozen(np.random.default_rng(8113).exponential(1 / PHONE_1["rate"], 2000))
F_13 = frozen(WAITS_13 > PHONE_1["c"])
S_13 = frozen(1 / PHONE_1["rate"] - WAITS_13)'''

NOTE_13 = (r"Les contrôles, puis `b = (f.sum() - f) / (n - 1)` pour `\"leave-one-out\"`, `g = (f - b) * s`, sa moyenne "
           r"et `g.std(axis=0, ddof=1) / math.sqrt(n)`. a) $\approx (-2{,}85551 ;\ 0{,}17076)$. b) $\approx (-2{,}90554 "
           r";\ 0{,}14063)$. c) $\frac{1\,999}{2\,000} = 0{,}9995$, exactement, quel que soit le tirage.")

HINTS_13 = {letter: 'library_hint("score_function_gradient")' for letter in "abc"}

MB8_13 = ex(
    "MB8.13", "programmer l'estimateur score d'une dérivée et son erreur type, avec une baseline constante ou la moyenne "
    "des autres tirages, puis le comparer à la dérivée exacte de MB8.1.", "fiche §2 et §3 ; M02c (erreur type) ; Ex MB8.1",
    functions="`score_function_gradient`", mymath="policy_gradient.py", note=NOTE_13, given=GIVEN_13,
    body=HOWTO + r"""

Écris `score_function_gradient(f_values, scores, baseline=0.0)` (fiche §2 et §3), en suivant sa docstring : contrôle les arguments (au moins deux valeurs finies ; des scores à 1 ou 2 dimensions, avec une ligne par valeur ; une baseline qui est un nombre fini ou `"leave-one-out"`, pas un booléen) ; puis les termes $g_i = (f_i - b_i)\,s_i$, leur moyenne, et leur écart-type (`ddof=1`) divisé par $\sqrt n$. Lance le groupe de tests.

**L'usage.** Le notebook fournit `WAITS_13`, 2 000 attentes au téléphone de MB8.1 (taux $0{,}1$ par minute ; graine fixée), `F_13`, les $f(x_i) = \mathbf{1}\{x_i > 18\}$, et `S_13`, leurs scores. Avec ta fonction :
- a) l'estimation sans baseline, puis son erreur type (une liste de 2 nombres) ;
- b) l'estimation avec la moyenne des autres tirages, puis son erreur type (une liste de 2 nombres) ;
- c) le rapport de l'estimation avec la moyenne du groupe, `baseline=float(np.mean(F_13))`, à celle de b) (un nombre).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `score_function_gradient` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui "
                  "était attendu).")]
    + tests_cells("test_score_function_gradient_ or test_module_uses_") + [
        ("md", "**L'usage** : 2 000 attentes au téléphone, sans baseline, avec la moyenne des autres tirages, avec la "
               "moyenne du groupe."),
        ("todo", '''answer_MB8_13a = answer_MB8_13b = answer_MB8_13c = ...
with wbm.attempt("MB8.13"):          # if you call score_function_gradient here: ⏳ while it is not written
    answer_MB8_13a = ...  # a) a list of 2 numbers, as computed: the estimate without baseline, then its standard error
    answer_MB8_13b = ...  # b) a list of 2 numbers, as computed: with the mean of the other draws, the estimate, then its standard error
    answer_MB8_13c = ...  # c) a number, as computed: the estimate with baseline=float(np.mean(F_13)), divided by the estimate of b)'''),
        ("check", answers_check("MB8.13", "abc", hints=HINTS_13)),
        ("solution", '''score_function_gradient = mymath.policy_gradient.score_function_gradient
answer_MB8_13a = list(score_function_gradient(F_13, S_13))
answer_MB8_13b = list(score_function_gradient(F_13, S_13, baseline="leave-one-out"))
answer_MB8_13c = score_function_gradient(F_13, S_13, baseline=float(np.mean(F_13)))[0] / answer_MB8_13b[0]
print("a)", np.round(answer_MB8_13a, 6).tolist(), " b)", np.round(answer_MB8_13b, 6).tolist(), " c)",
      round(answer_MB8_13c, 6))'''),
        ("record", '''waits_13r = np.random.default_rng(8113).exponential(10.0, 2000)     # the same draws as WAITS_13
f_13r, s_13r = (waits_13r > 18.0).astype(float), 10.0 - waits_13r
n_13r = len(f_13r)


def mean_and_error_13r(terms):
    """The oracle: the mean of the terms and their standard deviation (n - 1) over sqrt(n), by NumPy."""
    return [float(terms.mean()), float(terms.std(ddof=1) / math.sqrt(len(terms)))]


plain_13r = mean_and_error_13r(f_13r * s_13r)
others_13r = mean_and_error_13r((f_13r - (f_13r.sum() - f_13r) / (n_13r - 1)) * s_13r)
group_13r = float(np.mean((f_13r - f_13r.mean()) * s_13r))
wbm.record("MB8.13a", plain_13r, decimals=5,
           mistakes={"l'erreur type d'une moyenne de n termes est leur écart-type divisé par √n (relance les tests de "
                     "score_function_gradient)": [plain_13r[0], float((f_13r * s_13r).std(ddof=1))]})
wbm.record("MB8.13b", others_13r, decimals=5)
wbm.record("MB8.13c", group_13r / others_13r[0], decimals=4,
           mistakes={"c) est l'estimation avec la moyenne du groupe, au numérateur, sur celle de b), au dénominateur":
                         others_13r[0] / group_13r,
                     "le rapport compare l'estimation avec la moyenne du groupe à celle de b), avec la moyenne des "
                     "autres tirages": group_13r / plain_13r[0]})'''),
        ("solution", answers_check("MB8.13", "abc", hints=HINTS_13)),
        look("la dérivée exacte (ta réponse à MB8.1 b) est-elle à moins de deux erreurs types de a) ? de b) ? Pourquoi "
             "l'erreur type de b) est-elle plus petite ? Pourquoi le rapport c) ne dépend-il pas du tirage ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB8.14 · policy_gradient_exact
# ---------------------------------------------------------------------------
GIVEN_14 = '''# A Markov decision process of three states and two actions (the conventions of M26.14), read only
P_14 = frozen(__P_14__)            # P_14[a, s, t]
R_14 = frozen(__R_14__)            # R_14[a, s]
LOGITS_14 = frozen(__LOGITS_14__)  # LOGITS_14[s, a]
GAMMA_14 = 0.6'''

NOTE_14 = (r"$\pi$ par une softmax stable ligne par ligne, `P_pi = np.einsum(\"sa,ast->st\", pi, P)`, `r_pi = "
           r"np.einsum(\"sa,as->s\", pi, r)`, $\mathbf{M}$ par `np.linalg.solve`, puis `M[:, :, None] * (pi * A)[None, :, "
           r":]`. a) $(9{,}4111 ;\ 11{,}7183 ;\ 0{,}6770 ;\ -0{,}6770 ;\ 0{,}2788 ;\ -0{,}2788)$, comme MB8.3. b) "
           r"$(0{,}161768 ;\ -0{,}161768 ;\ -0{,}278655 ;\ 0{,}278655 ;\ 0 ;\ 0)$. c) $(0{,}04034 ;\ -0{,}04034 ;\ "
           r"-0{,}17645 ;\ 0{,}17645 ;\ 1{,}04353 ;\ -1{,}04353)$.")

HINTS_14 = {letter: 'library_hint("policy_gradient_exact")' for letter in "abc"}

MB8_14 = ex(
    "MB8.14", "programmer le gradient exact de la valeur d'une politique softmax tabulaire, retrouver MB8.3, puis lire "
    "quels logits comptent pour un état de départ.", "fiche §4 ; M26 §4 et §5 (MDP, système de Bellman), M17 §7 "
    "(softmax) ; Ex MB8.3", functions="`policy_gradient_exact`", mymath="policy_gradient.py", note=NOTE_14,
    given=GIVEN_14,
    body=REMINDER + r"""

Écris `policy_gradient_exact(P, r, logits, gamma)` (fiche §4), en suivant sa docstring : contrôle les arguments ; $\pi$, la softmax de chaque ligne des logits (retranche d'abord le maximum de la ligne) ; $\mathbf{P}_\pi$ et $\mathbf{r}_\pi$ ; $\mathbf{M}$ par `np.linalg.solve` ; $\mathbf{V}$, $Q$, puis la formule de la fiche §4 pour tous les $(s_0, s, a)$ d'un coup ; refuse $\gamma = 1$ quand $\mathbf{I} - \mathbf{P}_\pi$ est singulière. Lance le groupe de tests.

**L'usage.** Avec ta fonction :
- a) le camion de crêpes de MB8.3 (`TRUCK_3`, cellule de données), écrit comme un MDP à deux états (marché, parc) et deux actions (rester, partir) ; au parc, les deux actions font la même chose (mêmes lignes de $\mathbf{P}[a]$, même recette) : $V(\text{marché})$, $V(\text{parc})$, puis les dérivées de $V(\text{marché})$ par rapport aux deux logits du marché (rester, partir), puis celles de $V(\text{parc})$ (une liste de 6 nombres, à comparer à ta copie) ;
- b) le notebook fournit `P_14`, `R_14` et `LOGITS_14`, un MDP à trois états et deux actions, avec $\gamma = 0{,}6$ (`GAMMA_14`) : les dérivées de $V(0)$ par rapport aux six logits, état par état (les deux logits de l'état 0, puis de l'état 1, puis de l'état 2 ; une liste de 6 nombres) ;
- c) celles de $V(2)$, dans le même ordre (une liste de 6 nombres).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `policy_gradient_exact` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_policy_gradient_exact_") + [
        ("md", "**L'usage** : le camion de crêpes de MB8.3, puis un MDP à trois états."),
        ("todo", '''answer_MB8_14a = answer_MB8_14b = answer_MB8_14c = ...
with wbm.attempt("MB8.14"):          # if you call policy_gradient_exact here: ⏳ while it is not written
    answer_MB8_14a = ...  # a) a list of 6 numbers, as computed: V(market), V(park), the 2 derivatives of V(market), the 2 of V(park)
    answer_MB8_14b = ...  # b) a list of 6 numbers, as computed: the derivatives of V(0), state by state
    answer_MB8_14c = ...  # c) a list of 6 numbers, as computed: the derivatives of V(2), state by state'''),
        ("check", answers_check("MB8.14", "abc", hints=HINTS_14)),
        ("solution", '''policy_gradient_exact = mymath.policy_gradient.policy_gradient_exact
park_14 = list(TRUCK_3["park"])
P_truck_14 = [[list(TRUCK_3["stay"]), park_14],               # P[a, s, t]: action « stay », from the market, the park
              [list(TRUCK_3["leave"]), park_14]]              # action « leave »
r_truck_14 = [[TRUCK_3["sales_market"][0], TRUCK_3["sales_park"]],   # r[a, s]
              [TRUCK_3["sales_market"][1], TRUCK_3["sales_park"]]]
logits_truck_14 = [list(TRUCK_3["logits_market"]), [0.0, 0.0]]       # logits[s, a]
V_truck_14, grad_truck_14 = policy_gradient_exact(P_truck_14, r_truck_14, logits_truck_14, TRUCK_3["gamma"])
answer_MB8_14a = V_truck_14.tolist() + grad_truck_14[0, 0].tolist() + grad_truck_14[1, 0].tolist()
V_14, grad_14 = policy_gradient_exact(P_14, R_14, LOGITS_14, GAMMA_14)
answer_MB8_14b = grad_14[0].ravel().tolist()
answer_MB8_14c = grad_14[2].ravel().tolist()
print("a)", np.round(answer_MB8_14a, 6).tolist())
print("b)", np.round(answer_MB8_14b, 6).tolist(), " c)", np.round(answer_MB8_14c, 6).tolist())
print("   les logits du parc :", np.round(grad_truck_14[:, 1, :], 12).tolist(), "; V du MDP :", np.round(V_14, 6).tolist())'''),
        ("record", '''def gradient_14r(P, r, logits, gamma):
    """The oracle, written with loops: V from np.linalg.solve, then dV(s0)/dz(s, a) = M[s0, s] pi(a | s) A(s, a) entry by
    entry, and checked against centred finite differences of the values (Richardson)."""
    P, r, logits = (np.array(x, dtype=float) for x in (P, r, logits))
    K, m = r.shape

    def values(z):
        pi = np.exp(z - z.max(axis=1, keepdims=True))
        pi = pi / pi.sum(axis=1, keepdims=True)
        P_pi = sum(pi[:, a][:, None] * P[a] for a in range(K))
        r_pi = sum(pi[:, a] * r[a] for a in range(K))
        return np.linalg.solve(np.eye(m) - gamma * P_pi, r_pi), pi, P_pi

    V, pi, P_pi = values(logits)
    M = np.linalg.solve(np.eye(m) - gamma * P_pi, np.eye(m))
    grad = np.zeros((m, m, K))
    for s0 in range(m):
        for s in range(m):
            for a in range(K):
                advantage = r[a, s] + gamma * P[a, s] @ V - V[s]
                grad[s0, s, a] = M[s0, s] * pi[s, a] * advantage
    for s in range(m):
        for a in range(K):
            def fd(h):
                step = np.zeros((m, K))
                step[s, a] = h
                return (values(logits + step)[0] - values(logits - step)[0]) / (2 * h)
            assert np.allclose((4 * fd(5e-4) - fd(1e-3)) / 3, grad[:, s, a], atol=1e-9)
    return V, grad


park_14r = [0.3, 0.7]
truck_14r = ([[[0.86, 0.14], park_14r], [[0.0, 1.0], park_14r]], [[3.0, 4.0], [0.0, 4.0]], [[math.log(3), 0.0],
                                                                                           [0.0, 0.0]], 0.7)
V_14r, G_14r = gradient_14r(*truck_14r)
swapped_14r = gradient_14r(np.transpose(truck_14r[0], (1, 0, 2)), np.transpose(truck_14r[1]), truck_14r[2], 0.7)
wbm.record("MB8.14a", V_14r.tolist() + G_14r[0, 0].tolist() + G_14r[1, 0].tolist(), decimals=4,
           mistakes={"P se range P[a, s, t] et r se range r[a, s] : l'action d'abord, puis l'état (comme en M26.14)":
                         swapped_14r[0].tolist() + swapped_14r[1][0, 0].tolist() + swapped_14r[1][1, 0].tolist(),
                     "l'ordre demandé : V(marché), V(parc), les deux dérivées de V(marché) (rester, partir), puis "
                     "celles de V(parc)": V_14r.tolist() + G_14r[:, 0, :].T.ravel().tolist()})
mdp_14r = (__P_14__, __R_14__, __LOGITS_14__, 0.6)
V3_14r, G3_14r = gradient_14r(*mdp_14r)
wbm.record("MB8.14b", G3_14r[0].ravel().tolist(), decimals=6,
           mistakes={"état par état : les deux dérivées des logits de l'état 0, puis de l'état 1, puis de l'état 2":
                         G3_14r[0].T.ravel().tolist()})
wbm.record("MB8.14c", G3_14r[2].ravel().tolist(), decimals=5,
           mistakes={"état par état : les deux dérivées des logits de l'état 0, puis de l'état 1, puis de l'état 2":
                         G3_14r[2].T.ravel().tolist()})'''),
        ("solution", answers_check("MB8.14", "abc", hints=HINTS_14)),
        look("pourquoi, en b), les dérivées par rapport aux logits de l'état 2 sont-elles nulles, et pas en c) ? "
             "Pourquoi les deux dérivées d'un même état ont-elles une somme nulle ? Pourquoi, en a), les logits du parc "
             "ne comptent-ils pas ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB8.15 · importance_weights
# ---------------------------------------------------------------------------
GIVEN_15 = '''# Five draws of a proposal in dimension 900: the logarithms of the target and proposal densities there, read only
LOG_P_15 = frozen(__LOG_P_15__)
LOG_Q_15 = frozen(__LOG_Q_15__)'''

NOTE_15 = (r"`d = lt - lq`, `np.minimum(d, math.log(c))` avec `max_weight`, `u = np.exp(d - d.max())` et `ess = "
           r"u.sum() ** 2 / (u ** 2).sum()`, puis `np.exp(d)` ou `u / u.sum()`. a) $(5{,}84 ;\ 4{,}8823)$, comme "
           r"MB8.5. b) Le quotient direct rend `nan` partout ($\frac00$) ; avec `self_normalize=True` : "
           r"$\approx (0{,}39574 ;\ 3{,}65348)$.")

HINTS_15 = {letter: 'library_hint("importance_weights")' for letter in "ab"}

MB8_15 = ex(
    "MB8.15", "programmer des poids d'importance calculés en logarithmes, tronqués ou auto-normalisés, avec leur taille "
    "effective, puis les essayer sur des densités qui sortent des flottants.", "fiche §6 ; M05a (log-sum-exp) ; Ex MB8.5",
    functions="`importance_weights`", mymath="policy_gradient.py", note=NOTE_15, given=GIVEN_15,
    body=REMINDER + r"""

Écris `importance_weights(log_target, log_proposal, self_normalize=False, max_weight=None)` (fiche §6), en suivant sa docstring : contrôle les arguments ; les différences $d_i = \ln p(x_i) - \ln q(x_i)$, ramenées à $\ln c$ au plus avec `max_weight` $= c$ ; la taille effective à partir de $e^{d_i - \max d}$ ; puis les poids $e^{d_i}$, ou divisés par leur somme. Lance le groupe de tests.

**L'usage.** Avec ta fonction :
- a) les six panélistes de MB8.5 (`PANEL_5`, cellule de données ; les $\ln p$ et $\ln q$ de leurs classes) : la somme des poids, puis la taille effective (une liste de 2 nombres, à comparer à ta copie) ;
- b) le notebook fournit `LOG_P_15` et `LOG_Q_15`, les log-densités de cinq tirages d'une proposition en dimension 900, de l'ordre de $-1\,300$ : calcule d'abord `np.exp(LOG_P_15) / np.exp(LOG_Q_15)` et regarde ce que rend NumPy ; puis, avec `self_normalize=True`, le plus grand poids normalisé et la taille effective (une liste de 2 nombres).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `importance_weights` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_importance_weights_") + [
        ("md", "**L'usage** : les six panélistes de MB8.5, puis cinq tirages en dimension 900."),
        ("todo", '''answer_MB8_15a = answer_MB8_15b = naive_15 = ...
with wbm.attempt("MB8.15"):          # if you call importance_weights here: ⏳ while it is not written
    answer_MB8_15a = ...  # a) a list of 2 numbers, as computed: the sum of the weights of the six panelists, then the effective size
    naive_15 = ...        # b) first: np.exp(LOG_P_15) / np.exp(LOG_Q_15), and look at what NumPy returns
    answer_MB8_15b = ...  # b) a list of 2 numbers, as computed: with self_normalize=True, the largest weight, then the effective size'''),
        ("check", answers_check("MB8.15", "ab", hints=HINTS_15)),
        ("solution", '''importance_weights = mymath.policy_gradient.importance_weights
classes_15 = list(PANEL_5["sample"])
weights_15, ess_15 = importance_weights(np.log(np.array(PANEL_5["p"])[classes_15]),
                                        np.log(np.array(PANEL_5["q"])[classes_15]))
answer_MB8_15a = [float(weights_15.sum()), ess_15]
with np.errstate(under="ignore", invalid="ignore"):
    naive_15 = np.exp(LOG_P_15) / np.exp(LOG_Q_15)
normalized_15, ess_b_15 = importance_weights(LOG_P_15, LOG_Q_15, self_normalize=True)
answer_MB8_15b = [float(normalized_15.max()), ess_b_15]
print("a)", np.round(answer_MB8_15a, 6).tolist(), " b) le quotient direct :", naive_15.tolist(), " ; ",
      np.round(answer_MB8_15b, 6).tolist())
print("   les poids normalisés :", np.round(normalized_15, 4).tolist(), " ; les écarts ln p - ln q :",
      np.round(LOG_P_15 - LOG_Q_15, 4).tolist())'''),
        ("record", '''from fractions import Fraction as F_15r

from scipy.special import logsumexp as logsumexp_15r

panel_15r = [F_15r(p, 100) / F_15r(q, 100) for p, q in ((26, 50), (41, 25), (33, 25))]
sample_15r = [panel_15r[k] for k in (0, 0, 0, 1, 2, 2)]
sum_15r = sum(sample_15r)
kish_15r = float(sum_15r ** 2 / sum(w * w for w in sample_15r))
wbm.record("MB8.15a", [float(sum_15r), kish_15r], decimals=4,
           mistakes={"la taille effective divise le carré de la somme des poids par la somme de leurs carrés":
                         [float(sum_15r), float(sum_15r)],
                     "une taille effective est comprise entre 1 et n : vérifie l'ordre du quotient":
                         [float(sum_15r), 1 / kish_15r]})
gaps_15r = np.array(__LOG_P_15__) - np.array(__LOG_Q_15__)
ess_15r = float(np.exp(2 * logsumexp_15r(gaps_15r) - logsumexp_15r(2 * gaps_15r)))
wbm.record("MB8.15b", [float(np.exp(gaps_15r.max() - logsumexp_15r(gaps_15r))), ess_15r], decimals=5,
           mistakes={"b) demande les poids divisés par leur somme (self_normalize=True), pas les poids bruts":
                         [float(np.exp(gaps_15r.max())), ess_15r]})'''),
        ("solution", answers_check("MB8.15", "ab", hints=HINTS_15)),
        look("pourquoi le quotient direct ne donne-t-il rien d'utilisable ? Pourquoi les poids de b) sont-ils pourtant "
             "bien définis ? Que dit la taille effective trouvée, pour cinq tirages ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB8.16 · bradley_terry_fit
# ---------------------------------------------------------------------------
GIVEN_16 = '''# A season of six table-football clubs (0 to 5): WINS_16[i, j] is the number of wins of club i against club j, read only
WINS_16 = frozen(__WINS_16__)'''

CHECK_16C = '''with checked("MB8.16"):                                     # c) a club that never lost
    if not filled(wins_16c):
        print("⏳ Ex MB8.16c : pas encore fait (remplace `...` par ta copie de WINS_16).")
    else:
        mine_16c, expected_16c = as_floats(wins_16c), np.array(WINS_16)
        expected_16c[:, 1] = 0.0
        if mine_16c is None or mine_16c.shape != expected_16c.shape or not np.array_equal(mine_16c, expected_16c):
            print("❌ Ex MB8.16c : wins_16c doit être une copie de WINS_16 (6 lignes, 6 colonnes) dont seule la colonne 1, "
                  "les défaites du club 1, vaut 0")
        else:
            refuses("MB8.16c", "bradley_terry_fit(wins_16c), le club 1 sans défaite",
                    lambda: mymath.policy_gradient.bradley_terry_fit(wins_16c))'''

NOTE_16 = (r"La forte connexité par `R = (W > 0) | np.eye(K, dtype=bool)` multipliée par elle-même, puis les balayages de "
           r"Zermelo sur $p = e^\beta$, centrés. a) $(0{,}5580 ;\ 0{,}2703 ;\ -0{,}8283)$, comme MB8.6. b) "
           r"$(0{,}9224034 ;\ 0{,}7085111 ;\ 0{,}2381504 ;\ 0{,}0860997 ;\ -1{,}0427788 ;\ -0{,}9123858 ;\ "
           r"0{,}8623313)$. c) `ValueError` : personne n'a battu le club 1.")

HINTS_16 = {letter: 'library_hint("bradley_terry_fit")' for letter in "ab"}

MB8_16 = ex(
    "MB8.16", "programmer les forces d'un modèle de Bradley-Terry par l'algorithme de Zermelo, retrouver MB8.6, puis "
    "ajuster une saison de six clubs et voir quand les forces n'existent pas.", "fiche §7 ; M16 (chemins d'un graphe), "
    "M13a (sigmoïde) ; Ex MB8.6", functions="`bradley_terry_fit`", mymath="policy_gradient.py", note=NOTE_16,
    given=GIVEN_16,
    body=REMINDER + r"""

Écris `bradley_terry_fit(wins, tol=1e-10, max_iter=10_000)` (fiche §7), en suivant sa docstring : contrôle les arguments ; la forte connexité (la matrice booléenne « $i$ atteint $j$ » et ses produits par elle-même, M16) ; puis les balayages de Zermelo sur $p = e^\beta$, centrés à chaque balayage, jusqu'à ce que le plus grand changement de $\beta$ passe sous `tol`. Lance le groupe de tests.

**L'usage.** Avec ta fonction :
- a) le tournoi de MB8.6 (`FOOTBALL_6`, cellule de données) : les forces centrées de A, B, C (une liste de 3 nombres, à comparer à ta copie) ;
- b) le notebook fournit `WINS_16`, une saison de six clubs, qui n'ont pas tous joué le même nombre de matchs : les six forces, puis la probabilité que le club 0 batte le club 5 (une liste de 7 nombres) ;
- c) dans une copie de `WINS_16`, mets à 0 toutes les défaites du club 1 (sa colonne) : que fait ta fonction ? (la vérification attend une `ValueError`).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `bradley_terry_fit` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_bradley_terry_fit_") + [
        ("md", "**L'usage** : le tournoi de MB8.6, une saison de six clubs, puis un club sans défaite."),
        ("todo", '''answer_MB8_16a = answer_MB8_16b = wins_16c = ...
with wbm.attempt("MB8.16"):          # if you call bradley_terry_fit here: ⏳ while it is not written
    answer_MB8_16a = ...  # a) a list of 3 numbers, as computed: the centred strengths of A, B, C
    answer_MB8_16b = ...  # b) a list of 7 numbers, as computed: the six strengths, then the probability that club 0 beats club 5
wins_16c = ...            # c) a copy of WINS_16 whose column 1 (the defeats of club 1) is set to 0'''),
        ("check", answers_check("MB8.16", "ab", hints=HINTS_16) + "\n\n" + CHECK_16C),
        ("solution", '''bradley_terry_fit = mymath.policy_gradient.bradley_terry_fit
answer_MB8_16a = bradley_terry_fit(FOOTBALL_6["wins"]).tolist()
strengths_16 = bradley_terry_fit(WINS_16)
answer_MB8_16b = strengths_16.tolist() + [float(1 / (1 + np.exp(strengths_16[5] - strengths_16[0])))]
wins_16c = np.array(WINS_16)
wins_16c[:, 1] = 0.0
print("a)", np.round(answer_MB8_16a, 6).tolist(), " b)", np.round(answer_MB8_16b, 7).tolist())
print("   victoires :", WINS_16.sum(axis=1).tolist(), " ; matchs par paire :", (WINS_16 + WINS_16.T).tolist())'''),
        ("record", '''def newton_16r(wins):
    """The oracle: the maximum of the log-likelihood by Newton's method on beta_0..beta_{K-2} (beta_{K-1} = minus their
    sum), exact gradient and Hessian, 60 steps; then the likelihood equations checked (wins = expected wins)."""
    W = np.array(wins, dtype=float)
    K, N = len(W), W + W.T
    B = np.vstack([np.eye(K - 1), -np.ones((1, K - 1))])            # beta = B u, sum 0
    u = np.zeros(K - 1)
    for _ in range(60):
        beta = B @ u
        S = 1 / (1 + np.exp(-(beta[:, None] - beta[None, :])))
        grad = B.T @ (W.sum(axis=1) - (N * S).sum(axis=1))
        H = N * S * S.T
        hess = B.T @ (np.diag(H.sum(axis=1)) - H) @ B
        u = u + np.linalg.solve(hess, grad)
    beta = B @ u
    S = 1 / (1 + np.exp(-(beta[:, None] - beta[None, :])))
    assert np.allclose((N * S).sum(axis=1), W.sum(axis=1), atol=1e-11)
    return beta


beta_16r = newton_16r([[0, 2, 10], [5, 0, 1], [0, 3, 0]])
wbm.record("MB8.16a", beta_16r.tolist(), decimals=4)
league_16r = newton_16r(__WINS_16__)
wbm.record("MB8.16b", league_16r.tolist() + [float(1 / (1 + np.exp(league_16r[5] - league_16r[0])))], decimals=7,
           mistakes={"P(club 0 bat club 5) = e^{β₀}/(e^{β₀} + e^{β₅}), pas e^{β₀}/e^{β₅}":
                         league_16r.tolist() + [float(np.exp(league_16r[0] - league_16r[5]))]})'''),
        ("solution", answers_check("MB8.16", "ab", hints=HINTS_16) + "\n\n" + CHECK_16C),
        look("le classement par les forces suit-il ici celui des victoires ? Pourquoi n'est-ce pas garanti quand les "
             "clubs n'ont pas joué autant de matchs ? Pourquoi un club qui n'a jamais perdu n'a-t-il pas de force "
             "finie ?"),
    ],
)

PART_A = Part("A", "Ta librairie : l'estimateur score, le gradient exact d'une valeur, les poids d'importance, les forces "
              "de Bradley-Terry",
              "Fiche §2, §3, §4, §6 et §7. Les quatre fonctions de `mymath/policy_gradient.py`, leurs tests, et un usage "
              "de chacune. La cellule de données ci-dessous recopie les données des exercices papier.",
              given=TOOLS + "\n\n\n" + DATA, exercises=[MB8_13, MB8_14, MB8_15, MB8_16])

# ---------------------------------------------------------------------------
# Notebook exercises: predict, experiment (MB8.17, MB8.18)
# ---------------------------------------------------------------------------
GIVEN_17 = '''# X ~ Poisson of mean 3.5 and f(x) = 1{x >= 5}: 2 000 samples of n = 40 draws (seed 8117), one per row, and the optimal
# baseline b* = E[f s²] / E[s²] by exact sums over the law, read only
THETA_17, N_17 = 3.5, 40
_rng_17 = np.random.default_rng(8117)
DRAWS_17 = frozen(np.array([_rng_17.poisson(THETA_17, N_17) for _ in range(2000)]))
del _rng_17
_support_17 = np.arange(80)
_law_17 = stats.poisson.pmf(_support_17, THETA_17)
_f_17, _s_17 = (_support_17 >= 5).astype(float), _support_17 / THETA_17 - 1
B_STAR_17 = float(np.sum(_law_17 * _f_17 * _s_17 ** 2) / np.sum(_law_17 * _s_17 ** 2))
del _support_17, _law_17, _f_17, _s_17'''

NOTE_17 = (r"Prédictions attendues : a) (C) ; b) (B). c) $\approx (0{,}0550 ;\ 0{,}0385 ;\ 0{,}0294)$, un rapport "
           r"d'environ $1{,}87$ (la théorie donne $1{,}885$).")

CHECK_17 = '''for letter, prediction in zip("ab", [prediction_MB8_17a, prediction_MB8_17b]):
    if filled(prediction) and not isinstance(prediction, str):      # a number, a list...: not yet a prediction
        print(f'❌ Ex MB8.17{letter} : une prédiction est une lettre, "A", "B" ou "C", reçu {shown(prediction)}')
    else:
        wbm.check(f"MB8.17{letter}", prediction)'''

MB8_17 = ex(
    "MB8.17", "prédire l'ordre des dispersions de l'estimateur score d'une même dérivée pour trois baselines, puis les "
    "mesurer.", "fiche §3 ; Ex MB8.2, MB8.13", hypothesis=True, note=NOTE_17, given=GIVEN_17,
    body=r"""$X$ suit une loi de Poisson de moyenne $\theta = 3{,}5$ ; on estime $\frac{\mathrm{d}}{\mathrm{d}\theta}P_\theta(X \ge 5)$ par l'estimateur score sur $n = 40$ tirages, de trois façons : sans baseline, avec la moyenne des autres tirages, et avec la baseline optimale $b^\star$, que le notebook calcule par des sommes exactes sur la loi (`B_STAR_17`). On répète l'estimation 2 000 fois : le notebook fournit `DRAWS_17`, 2 000 échantillons de 40 tirages, un par ligne (le score d'un tirage est $\frac{x}{\theta} - 1$). **Avant d'exécuter quoi que ce soit**, prédis (une lettre chacune) :
- a) l'ordre des trois écarts-types : (A) ils sont égaux, puisque les trois estimations ont la même espérance ; (B) sans baseline < moyenne des autres < baseline optimale ; (C) sans baseline > moyenne des autres > baseline optimale ;
- b) le rapport de l'écart-type sans baseline à celui avec $b^\star$ : (A) entre 1 et $1{,}5$ ; (B) entre $1{,}5$ et $2{,}5$ ; (C) plus de $2{,}5$.

Puis, une fois tes prédictions écrites et vérifiées, mesure avec `score_function_gradient` :
- c) les trois écarts-types des 2 000 estimations, dans l'ordre de a) (une liste de 3 nombres).

La vérification de l'expérience ne s'exécute qu'une fois tes deux prédictions écrites.""",
    todo='''prediction_MB8_17a = ...  # a) "A", "B" or "C": (A) equal, (B) none < others < optimal, (C) none > others > optimal
prediction_MB8_17b = ...  # b) "A", "B" or "C": the standard deviation none / optimal: (A) 1 to 1.5, (B) 1.5 to 2.5, (C) more than 2.5''',
    check=CHECK_17,
    record='''wbm.record("MB8.17a", "C", prediction=True,
           mistakes={"relis ce que la fiche §3 dit de la variance de (f − b) s en fonction de b, et où se trouvent b = 0 "
                     "et b ≈ E[f] par rapport à son minimum b*": {"A", "B"}})
wbm.record("MB8.17b", "B", prediction=True,
           mistakes={"le rapport des écarts-types est la racine du rapport des variances : compare, sur le trinôme de "
                     "la fiche §3, la variance en b = 0 à la variance minimale": {"A", "C"}})''',
    after=[
        ("md", "**L'expérience.** Écris-la une fois tes deux prédictions vérifiées ; sa vérification ne s'exécute qu'à "
               "cette condition."),
        ("todo", '''answer_MB8_17c = ...
with wbm.attempt("MB8.17"):          # your score_function_gradient: ⏳ while it is not written
    answer_MB8_17c = ...  # c) a list of 3 numbers, as computed: the standard deviations of the 2 000 estimates, without baseline, with the mean of the other draws, with B_STAR_17'''),
        ("check", guarded('check_answer("MB8.17c", answer_MB8_17c, hint=library_hint("score_function_gradient"))',
                          ["prediction_MB8_17a", "prediction_MB8_17b"],
                          "⏳ Écris d'abord tes deux prédictions, puis exécute à nouveau.")),
        ("solution", '''score_function_gradient = mymath.policy_gradient.score_function_gradient
estimates_17 = np.zeros((len(DRAWS_17), 3))
for k, x_17 in enumerate(DRAWS_17):
    f_17, s_17 = (x_17 >= 5).astype(float), x_17 / THETA_17 - 1
    estimates_17[k] = [score_function_gradient(f_17, s_17)[0],
                       score_function_gradient(f_17, s_17, baseline="leave-one-out")[0],
                       score_function_gradient(f_17, s_17, baseline=B_STAR_17)[0]]
answer_MB8_17c = estimates_17.std(axis=0, ddof=1).tolist()
print("c)", np.round(answer_MB8_17c, 5).tolist(), " rapport sans / optimale :", round(answer_MB8_17c[0] / answer_MB8_17c[2], 3))
print("   moyennes des estimations :", np.round(estimates_17.mean(axis=0), 4).tolist(), " ; b* :", round(B_STAR_17, 4),
      " ; P(X >= 5) :", round(float(stats.poisson.sf(4, THETA_17)), 4))'''),
        ("record", '''draws_17r = np.array(DRAWS_17)
f_17r, s_17r = (draws_17r >= 5).astype(float), draws_17r / 3.5 - 1
others_17r = (f_17r.sum(axis=1, keepdims=True) - f_17r) / (draws_17r.shape[1] - 1)
spread_17r = [float(np.mean(terms, axis=1).std(ddof=1)) for terms in
              (f_17r * s_17r, (f_17r - others_17r) * s_17r, (f_17r - B_STAR_17) * s_17r)]
wbm.record("MB8.17c", spread_17r, decimals=4,
           mistakes={"dans l'ordre de a) : sans baseline, avec la moyenne des autres tirages, avec la baseline optimale":
                         spread_17r[::-1]})'''),
        ("solution", 'check_answer("MB8.17c", answer_MB8_17c, hint=library_hint("score_function_gradient"))'),
        look("les trois moyennes des estimations sont-elles proches de la même valeur ? $b^\\star$ est-il proche de "
             "$P_\\theta(X \\ge 5)$ ? Pourquoi la moyenne des autres tirages, proche de $\\mathbb{E}[f]$, ne fait-elle pas "
             "aussi bien que $b^\\star$ ?", " (après l'expérience)"),
    ],
)

GIVEN_18 = '''# Z ~ N(0, 1), the event Z > 4 and its probability; the draws of the experiment, read only: a) 100 000 draws of N(0, 1)
# (seed 8118); b) 10 000 draws of the proposal q = N(4, 1) (seed 8119); c) 400 rows of 10 000 draws of q (seed 8120)
TAIL_18 = float(stats.norm.sf(4.0))
DRAWS_18A = frozen(np.random.default_rng(8118).normal(size=100_000))
DRAWS_18B = frozen(np.random.default_rng(8119).normal(4.0, 1.0, 10_000))
_rng_18 = np.random.default_rng(8120)
DRAWS_18C = frozen(np.array([_rng_18.normal(4.0, 1.0, 10_000) for _ in range(400)]))
del _rng_18
C_18 = (1e-4, 2e-4, 3.35e-4, 1.0)            # the truncation levels of c)'''

CHECK_18 = r'''check_answer("MB8.18a", answer_MB8_18a)
check_answer("MB8.18b", answer_MB8_18b, hint=library_hint("importance_weights"))
with checked("MB8.18"):
    results_18 = []
    report_18 = reporter(results_18, stop=False)
    curves_18 = [as_floats(rel_bias_18), as_floats(rel_sd_18)] if filled(rel_bias_18, rel_sd_18) else None
    if curves_18 is None:
        print("⏳ Ex MB8.18 : rel_bias_18 et rel_sd_18 ne sont pas encore calculés.")
        raise StopCheck
    if any(c is None or c.shape != (len(C_18),) or not np.all(np.isfinite(c)) for c in curves_18):
        print(f"❌ Ex MB8.18 : rel_bias_18 et rel_sd_18 sont deux tableaux de {len(C_18)} nombres finis, un par niveau c "
              f"de C_18, reçu {shown(rel_bias_18)} et {shown(rel_sd_18)}")
        raise StopCheck
    fig_18, (ax_18, spare_18) = plt.subplots(1, 2, figsize=(11, 4))            # spare_18: the current axes
    try:
        opened_18 = drawn(lambda: call_safely("Ex MB8.18 : draw_18", draw_18, ax_18, C_18, curves_18[0], curves_18[1]))
        found_18 = []
        for values_18 in curves_18:
            found_18.append(next((line for line in ax_18.lines
                                  if np.asarray(line.get_xdata(), dtype=float).shape == (len(C_18),)
                                  and np.allclose(np.asarray(line.get_xdata(), dtype=float), C_18, rtol=1e-12, atol=0)
                                  and np.allclose(np.asarray(line.get_ydata(), dtype=float), values_18, rtol=1e-12,
                                                  atol=1e-15)), None))
        report_18(all(line is not None for line in found_18),
                  "deux courbes en fonction de c : le biais relatif et l'écart-type relatif",
                  "il faut deux courbes dans ax, en fonction de c (les niveaux de C_18, dans l'ordre) : le biais relatif "
                  "(rel_bias_18) et l'écart-type relatif (rel_sd_18)")
        legend_18 = ax_18.get_legend()
        report_18(legend_18 is not None and all(line is not None and line.get_label() and not
                                                line.get_label().startswith("_") for line in found_18)
                  and bool(ax_18.get_xlabel()) and bool(ax_18.get_ylabel()),
                  "une légende qui nomme chaque courbe, et des noms d'axes",
                  "il faut une légende (label=…, puis ax.legend()) qui nomme chaque courbe, et des noms d'axes"
                  if all(line is not None for line in found_18) else
                  "la légende et les noms d'axes se jugent sur les deux courbes : trace-les d'abord dans ax")
        elsewhere_18 = bool(spare_18.lines or spare_18.collections or spare_18.get_legend())
        report_18(not opened_18 and not elsewhere_18, "draw_18 dessine dans l'axe reçu",
                  "draw_18 doit dessiner dans l'axe reçu (ax.plot…), sans ouvrir de figure ni dessiner dans l'axe "
                  "courant (plt.plot, plt.legend…)")
        fig_18.delaxes(spare_18)
    except BaseException:
        plt.close(fig_18)
        raise
    fig_18.tight_layout()
    plt.show()
    sizes_18 = np.round(np.log10(np.abs(curves_18[1]) + 1e-300)).tolist()
    report_18(bool(np.all(curves_18[1] > 0)) and passes(HIDDEN_C18["id_sizes"], sizes_18),
              "les écarts-types relatifs ont l'ordre de grandeur attendu",
              "les écarts-types relatifs n'ont pas l'ordre de grandeur de ceux de l'estimation : l'écart-type des 400 "
              "estimations (une par ligne de DRAWS_18C), divisé par TAIL_18")
    verdict("MB8.18", all(results_18) and len(results_18) == 4, "ta figure et tes mesures de c) sont justes.",
            "relis les lignes ❌ ci-dessus.")
if filled(answer_MB8_18c) and filled(rel_bias_18) and as_floats(answer_MB8_18c) is not None \
        and as_floats(answer_MB8_18c).shape == (2,) and as_floats(rel_bias_18) is not None \
        and as_floats(rel_bias_18).shape == (len(C_18),) \
        and not np.allclose(as_floats(answer_MB8_18c), as_floats(rel_bias_18)[:2], rtol=1e-9, atol=1e-12):
    print("❌ Ex MB8.18c : c) relève les deux premiers biais relatifs de rel_bias_18 (c = 10⁻⁴, puis 2·10⁻⁴), sans les "
          "arrondir")
else:
    check_answer("MB8.18c", answer_MB8_18c, hint=library_hint("importance_weights"))'''

NOTE_18 = (r"a) $(0{,}00002 ;\ 2)$. b) $\approx (0{,}9931 ;\ 0{,}0210 ;\ 7{,}8498)$. c) $\approx (-0{,}3588 ;\ "
           r"-0{,}1018)$ (exactement : $-0{,}3581$ et $-0{,}1007$) ; les écarts-types relatifs valent environ "
           r"$0{,}0109$, $0{,}0175$, $0{,}0209$ et $0{,}0209$.")

MB8_18 = ex(
    "MB8.18", "estimer la probabilité d'un événement rare par Monte-Carlo naïf et par échantillonnage d'importance, lire "
    "la taille effective, puis mesurer ce que la troncature des poids fait au biais et à la dispersion.",
    "fiche §6 ; M20 §5 (Horvitz-Thompson) ; Ex MB8.5, MB8.15", note=NOTE_18, given=GIVEN_18,
    body=r"""$Z$ suit la loi normale centrée réduite, et l'on estime $P(Z > 4)$, connue par ailleurs (`scipy.stats.norm.sf(4)`, que le notebook range dans `TAIL_18`).
- a) Monte-Carlo naïf sur les 100 000 tirages `DRAWS_18A` : l'estimation, puis le nombre de tirages au-delà de 4 (une liste de 2 nombres) ;
- b) échantillonnage d'importance sous la proposition $q = \mathcal{N}(4, 1)$, avec les 10 000 tirages `DRAWS_18B` et `importance_weights` (les log-densités par `scipy.stats.norm.logpdf`) : l'estimation divisée par la vraie valeur, l'erreur type relative (l'erreur type divisée par la vraie valeur), puis la taille effective des 10 000 poids (une liste de 3 nombres) ;
- c) des poids tronqués à $c$, pour les quatre niveaux $c = 10^{-4}$, $2 \cdot 10^{-4}$, $3{,}35 \cdot 10^{-4}$ et 1 (`C_18`) : sur les 400 répétitions de 10 000 tirages `DRAWS_18C` (une par ligne), le biais relatif (la moyenne des 400 estimations moins la vraie valeur, divisée par la vraie valeur) et l'écart-type relatif (l'écart-type des 400 estimations divisé par la vraie valeur) pour chaque $c$, en deux tableaux `rel_bias_18` et `rel_sd_18` ; écris `draw_18(ax, c_values, rel_bias, rel_sd)`, qui les trace en deux courbes en fonction de $c$ dans l'axe `ax` (avec une légende et des noms d'axes ; une échelle logarithmique en $c$ se lit mieux), sans ouvrir de figure ; relève les biais relatifs pour $c = 10^{-4}$ et $2 \cdot 10^{-4}$ (une liste de 2 nombres).

La vérification appelle `draw_18` avec tes deux tableaux et affiche la figure.""",
    todo='''def draw_18(ax, c_values, rel_bias, rel_sd):
    """In ax: the relative bias and the relative standard deviation of the estimate against the truncation level c (two
    curves, with a legend and axis labels). Opens no figure."""
    raise NotImplementedError("draw_18 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB8_18a = answer_MB8_18b = answer_MB8_18c = rel_bias_18 = rel_sd_18 = ...
with wbm.attempt("MB8.18"):          # if you call importance_weights here: ⏳ while it is not written
    answer_MB8_18a = ...  # a) a list of 2 numbers: on DRAWS_18A, the naive estimate, then the number of draws beyond 4
    answer_MB8_18b = ...  # b) a list of 3 numbers, as computed: on DRAWS_18B, the estimate / TAIL_18, the relative standard error, the effective size
    rel_bias_18 = ...     # c) the 4 relative biases, one per level of C_18 (the 400 rows of DRAWS_18C)
    rel_sd_18 = ...       # c) the 4 relative standard deviations, one per level of C_18
    answer_MB8_18c = ...  # c) a list of 2 numbers, as computed: the relative biases for c = 1e-4, then 2e-4''',
    check="HIDDEN_C18 = __HIDDEN_C18__   # the sub-ID of the orders of size of the deviations\n\n" + CHECK_18,
    solution='''def draw_18(ax, c_values, rel_bias, rel_sd):
    """In ax: the relative bias and the relative standard deviation of the estimate against the truncation level c (two
    curves, with a legend and axis labels). Opens no figure."""
    ax.plot(c_values, rel_bias, "o-", label="biais relatif")
    ax.plot(c_values, rel_sd, "s--", label="écart-type relatif")
    ax.axhline(0.0, color="grey", lw=0.8)
    ax.axvline(math.exp(-8), color="grey", lw=0.8, ls=":")
    ax.set_xscale("log")
    ax.set_xlabel("niveau de troncature c")
    ax.set_ylabel("rapport à P(Z > 4)")
    ax.legend(fontsize=8)


importance_weights = mymath.policy_gradient.importance_weights
beyond_18 = DRAWS_18A > 4
answer_MB8_18a = [float(beyond_18.mean()), int(beyond_18.sum())]
weights_18, ess_18 = importance_weights(stats.norm.logpdf(DRAWS_18B), stats.norm.logpdf(DRAWS_18B, 4.0, 1.0))
terms_18 = weights_18 * (DRAWS_18B > 4)
answer_MB8_18b = [float(terms_18.mean()) / TAIL_18, float(terms_18.std(ddof=1) / math.sqrt(len(terms_18))) / TAIL_18, ess_18]
log_p_18, log_q_18 = stats.norm.logpdf(DRAWS_18C), stats.norm.logpdf(DRAWS_18C, 4.0, 1.0)
estimates_18 = np.zeros((len(DRAWS_18C), len(C_18)))
for k in range(len(DRAWS_18C)):
    for j, c in enumerate(C_18):
        w = importance_weights(log_p_18[k], log_q_18[k], max_weight=c)[0]
        estimates_18[k, j] = np.mean(w * (DRAWS_18C[k] > 4))
rel_bias_18 = (estimates_18.mean(axis=0) - TAIL_18) / TAIL_18
rel_sd_18 = estimates_18.std(axis=0, ddof=1) / TAIL_18
answer_MB8_18c = rel_bias_18[:2].tolist()
fig_18s, ax_18s = plt.subplots(figsize=(6, 4))
draw_18(ax_18s, C_18, rel_bias_18, rel_sd_18)
plt.show()
print("a)", answer_MB8_18a, " b)", np.round(answer_MB8_18b, 5).tolist(), " c)", np.round(answer_MB8_18c, 5).tolist())
print("   biais relatifs :", np.round(rel_bias_18, 5).tolist(), " ; écarts-types relatifs :", np.round(rel_sd_18, 4).tolist(),
      " ; le plus grand poids au-delà de 4 :", f"{math.exp(-8):.3e}")''',
    record='''from scipy import stats as stats_18r
from scipy.special import logsumexp as logsumexp_18r

tail_18r = float(stats_18r.norm.sf(4.0))
naive_18r = np.random.default_rng(8118).normal(size=100_000)
wbm.record("MB8.18a", [float((naive_18r > 4).mean()), float((naive_18r > 4).sum())], decimals=6)
proposal_18r = np.random.default_rng(8119).normal(4.0, 1.0, 10_000)
logw_18r = stats_18r.norm.logpdf(proposal_18r) - stats_18r.norm.logpdf(proposal_18r, 4.0, 1.0)
terms_18r = np.exp(logw_18r) * (proposal_18r > 4)
ess_18r = float(np.exp(2 * logsumexp_18r(logw_18r) - logsumexp_18r(2 * logw_18r)))
selfnorm_18r = float(np.sum(np.exp(logw_18r - logsumexp_18r(logw_18r)) * (proposal_18r > 4)))
wbm.record("MB8.18b", [float(terms_18r.mean()) / tail_18r, float(terms_18r.std(ddof=1) / 100) / tail_18r, ess_18r],
           decimals=4,
           mistakes={"b) demande l'estimation sans biais, la moyenne des w_i f(z_i), avec les poids bruts (pas divisés "
                     "par leur somme)": [selfnorm_18r / tail_18r, float(terms_18r.std(ddof=1) / 100) / tail_18r, ess_18r]})
rng_18r = np.random.default_rng(8120)
levels_18r = (1e-4, 2e-4, 3.35e-4, 1.0)
means_18r = np.zeros((400, 4))
for k in range(400):
    z_18r = rng_18r.normal(4.0, 1.0, 10_000)
    for j, c_18r in enumerate(levels_18r):
        means_18r[k, j] = np.mean(np.minimum(np.exp(8 - 4 * z_18r), c_18r) * (z_18r > 4))
bias_18r = (means_18r.mean(axis=0) - tail_18r) / tail_18r
wbm.record("MB8.18c", bias_18r[:2].tolist(), decimals=4)
HIDDEN_18r = __HIDDEN_C18__
wbm.record(HIDDEN_18r["id_sizes"], np.round(np.log10(means_18r.std(axis=0, ddof=1) / tail_18r)).tolist())''',
    after=[
        ("solution", "HIDDEN_C18 = __HIDDEN_C18__   # the sub-ID of the orders of size of the deviations\n\n" + CHECK_18),
        look("pourquoi le Monte-Carlo naïf ne donne-t-il presque rien ? Que vaut le poids $\\frac pq$ d'un tirage $z$, et "
             "quel est le plus grand poids d'un tirage au-delà de 4 ? Pourquoi la taille effective de b) est-elle si "
             "petite, alors que l'estimation est précise ? À partir de quel $c$ la troncature ne biaise-t-elle plus ?"),
    ],
)

PART_B = Part("B", "Prédire, mesurer",
              "Fiche §3 et §6. Trois baselines pour une même dérivée ; un événement rare, l'échantillonnage d'importance "
              "et des poids tronqués.", exercises=[MB8_17, MB8_18])

# ---------------------------------------------------------------------------
# Notebook exercises: debug, test (MB8.19, MB8.20)
# ---------------------------------------------------------------------------
GIVEN_19 = '''# The colleague's code
def score_exp_bad(x, theta):
    """The score s_θ(x) = ∂_θ ln p_θ(x) of the exponential law of rate theta, at each point of x."""
    x = np.asarray(x, dtype=float)
    return (x - theta) / theta ** 2


def weights_bad(log_p, log_q):
    """The importance weights p(x_i) / q(x_i) of draws x_i of q, from the logarithms of the two densities."""
    return np.exp(np.asarray(log_q, dtype=float) - np.asarray(log_p, dtype=float))


def estimate_bad(f, s):
    """The score estimate (1/n) Σ (f_i - b_i) s_i of a batch, each baseline b_i computed on the batch, unbiased."""
    f, s = np.asarray(f, dtype=float), np.asarray(s, dtype=float)
    return float(np.mean((f - f.mean()) * s))


def strongest_bad(wins_a, wins_b):
    """The strongest club of two tournaments put together, A (clubs A0, A1, ...) and B (clubs B0, B1, ...), as "A0",
    "B2"...; ValueError when the data do not allow to say."""
    beta_a = ref_pg.bradley_terry_fit(wins_a)            # the strengths of each tournament (the reference's fit)
    beta_b = ref_pg.bradley_terry_fit(wins_b)
    if beta_a.max() >= beta_b.max():
        return f"A{int(np.argmax(beta_a))}"
    return f"B{int(np.argmax(beta_b))}"


# The data, read only: (1) 100 000 draws at the rate 0.4 (seed 8121); (2) 50 000 draws of q = N(0, 1.5²) (seed 8122)
# and the logarithms of the target p = N(0.8, 1) and of q there; (3) 20 000 batches of 4 draws of a Poisson law of mean
# 1.5 (seed 8123); (4) the tournaments A and B (wins of the row against the column), and B with a weak club B3
X_19A = frozen(np.random.default_rng(8121).exponential(1 / 0.4, 100_000))
X_19B = frozen(np.random.default_rng(8122).normal(0.0, 1.5, 50_000))
LOG_P_19B, LOG_Q_19B = frozen(stats.norm.logpdf(X_19B, 0.8, 1.0)), frozen(stats.norm.logpdf(X_19B, 0.0, 1.5))
BATCHES_19C = frozen(np.random.default_rng(8123).poisson(1.5, (20_000, 4)))
TOURNAMENT_A = frozen(__TOURNAMENT_A__)
TOURNAMENT_B = frozen(__TOURNAMENT_B__)
TOURNAMENT_B3 = frozen(__TOURNAMENT_B3__)

# The colleague's checks: all pass
_check_x_19 = np.random.default_rng(8121).exponential(1.0, 100_000)
print("(1)", bool(abs(np.mean(score_exp_bad(_check_x_19, 1.0))) < 0.025), "(attendu True : au taux 1, la moyenne des "
      "scores est proche de 0)")
print("(2)", bool(np.allclose(weights_bad(LOG_Q_19B, LOG_Q_19B), 1.0)), "(attendu True : avec la même loi pour p et "
      "pour q, tous les poids valent 1)")
_check_batch_19 = np.random.default_rng(8126).poisson(1.5, 10_000)
print("(3)", bool(abs(estimate_bad(_check_batch_19 >= 2, _check_batch_19 / 1.5 - 1) - 1.5 * math.exp(-1.5)) < 0.025),
      "(attendu True : sur un batch de 10 000 tirages, l'estimation est proche de la dérivée exacte)")
print("(4)", strongest_bad(TOURNAMENT_A, TOURNAMENT_A) == "A0", "(attendu True : deux fois le même tableau de matchs, "
      "le meilleur club de ce tableau)")
del _check_x_19, _check_batch_19'''

CHECK_19 = '''CASES_C19 = __CASES_C19__   # the hidden cases, and the sub-IDs of the values expected

results_19, parts_19 = [], []
MYMATH_C19 = list(getattr(mymath, "__path__", [])) + list(getattr(REF, "__path__", []))   # the folders of mymath
TWINS_C19 = set()                                  # the functions of policy_gradient.py (yours, the reference's)
for _folder_c19 in MYMATH_C19:
    TWINS_C19 |= code_keys_of_file(os.path.join(_folder_c19, "policy_gradient.py"))


def report_19(ok, success, failure):
    results_19.append(bool(ok))
    print(("✅ " + success) if ok else ("❌ " + failure))


def call_19(part, name, function, *args):
    """function(*args), without mymath; an error of the learner's code becomes one ❌ line that names the function."""
    try:
        with code_from(MYMATH_C19, twins=TWINS_C19) as seen:
            got = function(*args)
    except (NotImplementedError, MymathMissingError):
        raise
    except Exception as exc:  # noqa: BLE001 - the learner's error, reported with the name of the function
        report_19(False, "", f"({part}) {name} : ton code lève {type(exc).__name__} : {str(exc)[:160]}")
        parts_19.append(part)
        raise StopCheck from None
    if seen:
        report_19(False, "", f"({part}) {name} appelle mymath ({seen[0]}) : l'énoncé demande la correction sans mymath, "
                  "en corrigeant le code du collègue")
        parts_19.append(part)
        raise StopCheck
    return got


def unchanged_19(arrays, originals):
    return all(np.array_equal(a, np.array(o)) for a, o in zip(arrays, originals))


with checked("MB8.19"):                                       # (1) score_exp_fixed
    got_c19, bad_c19, why_c19 = [], [], ""
    for theta_c19, points_c19 in CASES_C19["scores"]:
        x_c19 = np.array(points_c19)                          # non-dyadic floats: a change in place would show
        value_c19 = as_floats(call_19(1, "score_exp_fixed", score_exp_fixed, x_c19, theta_c19))
        if not unchanged_19([x_c19], [points_c19]):
            why_c19 = "ta fonction modifie le tableau reçu : travaille sur une copie"
            break
        if value_c19 is None or value_c19.shape != x_c19.shape:
            why_c19 = "score_exp_fixed rend un score par point de x, de la forme de x"
            break
        got_c19 += value_c19.tolist()
        bad_c19 += score_exp_bad(np.array(points_c19), theta_c19).tolist()
    if not why_c19 and not passes(CASES_C19["id_scores"], got_c19):
        why_c19 = ("ta correction rend encore ce que rend score_exp_bad" if np.allclose(got_c19, bad_c19, rtol=1e-12)
                   else "pour d'autres taux (ni 1, ni 0,4) et d'autres points, ce n'est pas le score en θ de la loi "
                        "exponentielle de taux θ")
    report_19(not why_c19, "(1) score_exp_fixed : d'autres taux, d'autres points", f"(1) score_exp_fixed : {why_c19}")
    parts_19.append(1)

with checked("MB8.19"):                                       # (2) weights_fixed
    got_c19, bad_c19, why_c19 = [], [], ""
    for lp_c19, lq_c19 in CASES_C19["weights"]:
        left_c19, right_c19 = np.array(lp_c19), np.array(lq_c19)
        value_c19 = as_floats(call_19(2, "weights_fixed", weights_fixed, left_c19, right_c19))
        if not unchanged_19([left_c19, right_c19], [lp_c19, lq_c19]):
            why_c19 = "ta fonction modifie un tableau reçu : travaille sur une copie"
            break
        if value_c19 is None or value_c19.shape != left_c19.shape:
            why_c19 = "weights_fixed rend un poids par tirage, de la forme de log_p"
            break
        got_c19 += value_c19.tolist()
        bad_c19 += weights_bad(np.array(lp_c19), np.array(lq_c19)).tolist()
    if not why_c19 and not passes(CASES_C19["id_weights"], got_c19):
        why_c19 = ("ta correction rend encore ce que rend weights_bad" if np.allclose(got_c19, bad_c19, rtol=1e-12)
                   else "pour d'autres log-densités, ce ne sont pas les poids p(x_i)/q(x_i) des tirages de q")
    report_19(not why_c19, "(2) weights_fixed : d'autres log-densités", f"(2) weights_fixed : {why_c19}")
    parts_19.append(2)

with checked("MB8.19"):                                       # (3) estimate_fixed
    got_c19, bad_c19, why_c19 = [], [], ""
    for f_c19, s_c19 in CASES_C19["batches"]:
        left_c19, right_c19 = np.array(f_c19), np.array(s_c19)
        value_c19 = call_19(3, "estimate_fixed", estimate_fixed, left_c19, right_c19)
        if not unchanged_19([left_c19, right_c19], [f_c19, s_c19]):
            why_c19 = "ta fonction modifie un tableau reçu : travaille sur une copie"
            break
        number_c19 = as_floats(value_c19)
        if number_c19 is None or number_c19.shape != ():
            why_c19 = f"estimate_fixed rend un nombre (l'estimation du batch), reçu {shown(value_c19)}"
            break
        got_c19.append(float(number_c19))
        bad_c19.append(estimate_bad(np.array(f_c19), np.array(s_c19)))
    if not why_c19 and not passes(CASES_C19["id_batches"], got_c19):
        why_c19 = ("ta correction rend encore ce que rend estimate_bad" if np.allclose(got_c19, bad_c19, rtol=1e-12)
                   else "sur d'autres batches (de 2 à 7 tirages, des valeurs f quelconques), l'estimation n'est pas "
                        "celle d'une baseline qui garde l'estimateur sans biais")
    report_19(not why_c19, "(3) estimate_fixed : d'autres batches, de tailles différentes",
              f"(3) estimate_fixed : {why_c19}")
    parts_19.append(3)

with checked("MB8.19"):                                       # (4) strongest_fixed
    why_c19 = ""
    for wins_a_c19, wins_b_c19 in [(TOURNAMENT_A, TOURNAMENT_B), (TOURNAMENT_A, TOURNAMENT_B3)] + CASES_C19["pairs"]:
        try:
            with code_from(MYMATH_C19, twins=TWINS_C19) as seen_c19:
                answer_c19 = strongest_fixed(np.array(wins_a_c19), np.array(wins_b_c19))
        except (NotImplementedError, MymathMissingError):
            raise
        except ValueError:
            answer_c19 = ValueError
        except Exception as exc:  # noqa: BLE001 - the learner's error
            why_c19 = f"ton code lève {type(exc).__name__} : {str(exc)[:160]}"
            break
        if seen_c19:
            why_c19 = (f"appelle mymath ({seen_c19[0]}) : l'énoncé demande la correction sans mymath, en corrigeant le "
                       "code du collègue")
            break
        if answer_c19 is not ValueError:
            why_c19 = (f"pour deux tournois sans club commun ni match entre eux, ta fonction désigne encore un club "
                       f"({shown(answer_c19)}) : relis ce que la fiche §7 dit de l'existence des forces et de ce "
                       "qu'elles identifient")
            break
    report_19(not why_c19, "(4) strongest_fixed : les deux tournois, et d'autres paires de tournois",
              f"(4) strongest_fixed : {why_c19}")
    parts_19.append(4)

if len(set(parts_19)) == 4:
    verdict("MB8.19", all(results_19), "les quatre fonctions corrigées passent tous les cas.",
            "relis les lignes ❌ ci-dessus.")'''

CHECK_19D = '''if not filled(answer_MB8_19d):
    print("⏳ Ex MB8.19d : pas encore fait.")
elif not (isinstance(answer_MB8_19d, (list, tuple)) and len(answer_MB8_19d) == 2
          and all(isinstance(name, str) for name in answer_MB8_19d)):
    print(f"❌ Ex MB8.19d : une liste de 2 noms de clubs (des chaînes comme \\"A1\\"), reçu {shown(answer_MB8_19d)}")
else:
    wbm.check("MB8.19d", " ".join(name.strip() for name in answer_MB8_19d))'''

NOTE_19 = (r"(1) `1 / theta - x` (le collègue avait écrit le score de la loi paramétrée par sa moyenne). a) $\approx "
           r"(-0{,}01125 ;\ 13{,}19531)$. (2) `np.exp(log_p - log_q)`. b) $\approx (0{,}7993 ;\ -1\,022{,}1135)$. (3) "
           r"La moyenne des autres tirages du batch, `(f.sum() - f) / (len(f) - 1)`. c) $\approx (0{,}33579 ;\ "
           r"0{,}25184)$, exactement dans le rapport $\frac34$. (4) Lever `ValueError` : sans club commun ni match "
           r"entre eux, les deux échelles de forces n'ont rien en commun. d) `[\"A0\", \"B1\"]`.")

MB8_19 = ex(
    "MB8.19", "reconnaître quatre erreurs à leurs symptômes, qui passent une vérification trop faible, puis les corriger.",
    "fiche §1, §3, §6 et §7 ; Ex MB8.13, MB8.15, MB8.16", note=NOTE_19, given=GIVEN_19,
    body=r"""Un collègue a écrit quatre fonctions, chacune accompagnée d'une vérification qui passe (cellule fournie) :
1. `score_exp_bad(x, theta)` doit rendre le score $s_\theta(x)$ de la loi exponentielle de taux $\theta$ en chaque point de `x`. Sur 100 000 tirages au taux $0{,}4$ (`X_19A`), la moyenne des scores est loin de 0. Il l'a vérifiée au taux 1, où la moyenne des scores est proche de 0.
2. `weights_bad(log_p, log_q)` doit rendre les poids d'importance de tirages de $q$. Avec la cible $\mathcal{N}(0{,}8 ;\ 1)$ et la proposition $\mathcal{N}(0 ;\ 1{,}5^2)$ (`X_19B`, `LOG_P_19B`, `LOG_Q_19B`), la moyenne des $w_ix_i$, qui devrait estimer $\mathbb{E}_p[X] = 0{,}8$, est énorme et négative. Il l'a vérifiée avec la même loi pour $p$ et pour $q$.
3. `estimate_bad(f, s)` doit rendre l'estimateur score d'un batch, avec pour chaque tirage une baseline calculée sur le batch, et rester sans biais. Sur 20 000 batches de 4 tirages (`BATCHES_19C` : loi de Poisson de moyenne $1{,}5$, $f(x) = \mathbf{1}\{x \ge 2\}$, le score $\frac{x}{1{,}5} - 1$), la moyenne des estimations reste nettement sous la dérivée exacte, $1{,}5\,e^{-1{,}5}$. Il l'a vérifiée sur un seul batch de 10 000 tirages.
4. `strongest_bad(wins_a, wins_b)` doit dire quel est le club le plus fort de deux tournois réunis, A (clubs A0, A1, A2 ; `TOURNAMENT_A`) et B (clubs B0, B1, B2 ; `TOURNAMENT_B`), ou lever une `ValueError` quand les données ne permettent pas de le dire. Quand on ajoute au tournoi B un club faible, B3, sans rien changer aux matchs des autres (`TOURNAMENT_B3`), sa réponse change. Il l'a vérifiée en lui donnant deux fois le même tableau de matchs : elle a bien désigné le meilleur club de ce tableau.

À faire : trouve et corrige chaque erreur dans le code du collègue lui-même : les fonctions corrigées s'appellent `score_exp_fixed`, `weights_fixed`, `estimate_fixed` et `strongest_fixed`, avec les mêmes arguments, et n'appellent **pas** `mymath` (la vérification le contrôle, copies de son code comprises). Puis réponds :
- a) la moyenne des scores de `X_19A` au taux $0{,}4$, avec la fonction corrigée, puis avec la fonction fautive (une liste de 2 nombres) ;
- b) l'estimation de $\mathbb{E}_p[X]$, la moyenne des $w_ix_i$, corrigée puis fautive (une liste de 2 nombres) ;
- c) la moyenne des 20 000 estimations, corrigée puis fautive (une liste de 2 nombres) ;
- d) les réponses de la fonction fautive avant, puis après l'ajout de B3 (une liste de 2 noms de clubs, comme `"A1"`).

Pour chacune des quatre erreurs, dis aussi, dans ta copie, pourquoi la vérification du collègue ne la voyait pas. La vérification essaie aussi tes fonctions corrigées sur des cas cachés : d'autres taux, d'autres log-densités, d'autres batches, d'autres paires de tournois, et des tableaux qu'elles ne doivent pas modifier.""",
    todo='''def score_exp_fixed(x, theta):
    """The score s_θ(x) = ∂_θ ln p_θ(x) of the exponential law of rate theta, at each point of x."""
    raise NotImplementedError("score_exp_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def weights_fixed(log_p, log_q):
    """The importance weights p(x_i) / q(x_i) of draws x_i of q, from the logarithms of the two densities."""
    raise NotImplementedError("weights_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def estimate_fixed(f, s):
    """The score estimate (1/n) Σ (f_i - b_i) s_i of a batch, each baseline b_i computed on the batch, unbiased."""
    raise NotImplementedError("estimate_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def strongest_fixed(wins_a, wins_b):
    """The strongest club of two tournaments put together, A (clubs A0, A1, ...) and B (clubs B0, B1, ...), as "A0",
    "B2"...; ValueError when the data do not allow to say."""
    raise NotImplementedError("strongest_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB8_19a = answer_MB8_19b = answer_MB8_19c = answer_MB8_19d = ...
with wbm.attempt("MB8.19"):          # your four functions: ⏳ while they are not written
    answer_MB8_19a = ...  # a) a list of 2 numbers, as computed: the mean of the scores of X_19A at the rate 0.4 by score_exp_fixed, then by the WRONG score_exp_bad
    answer_MB8_19b = ...  # b) a list of 2 numbers, as computed: the mean of w_i x_i on X_19B by weights_fixed, then by the WRONG weights_bad
    answer_MB8_19c = ...  # c) a list of 2 numbers, as computed: the mean of the 20 000 estimates on BATCHES_19C by estimate_fixed, then by the WRONG estimate_bad
    answer_MB8_19d = ...  # d) a list of 2 names: the answers of the WRONG strongest_bad, before then after adding B3''',
    check=answers_check("MB8.19", "abc") + "\n" + CHECK_19D + "\n\n" + CHECK_19,
    solution='''def score_exp_fixed(x, theta):
    """The score s_θ(x) = ∂_θ ln p_θ(x) of the exponential law of rate theta, at each point of x."""
    x = np.asarray(x, dtype=float)
    return 1 / theta - x                                       # ln p = ln θ − θ x, derived in the rate θ


def weights_fixed(log_p, log_q):
    """The importance weights p(x_i) / q(x_i) of draws x_i of q, from the logarithms of the two densities."""
    return np.exp(np.asarray(log_p, dtype=float) - np.asarray(log_q, dtype=float))   # ln p − ln q


def estimate_fixed(f, s):
    """The score estimate (1/n) Σ (f_i - b_i) s_i of a batch, each baseline b_i computed on the batch, unbiased."""
    f, s = np.asarray(f, dtype=float), np.asarray(s, dtype=float)
    others = (f.sum() - f) / (len(f) - 1)                      # b_i: the mean of the n − 1 OTHER values of the batch
    return float(np.mean((f - others) * s))


def strongest_fixed(wins_a, wins_b):
    """The strongest club of two tournaments put together, A (clubs A0, A1, ...) and B (clubs B0, B1, ...), as "A0",
    "B2"...; ValueError when the data do not allow to say."""
    raise ValueError("deux tournois sans club commun ni match entre eux : leurs forces n'ont pas d'échelle commune")


f_19, s_19 = (BATCHES_19C >= 2).astype(float), BATCHES_19C / 1.5 - 1
answer_MB8_19a = [float(np.mean(score(X_19A, 0.4))) for score in (score_exp_fixed, score_exp_bad)]
answer_MB8_19b = [float(np.mean(weights(LOG_P_19B, LOG_Q_19B) * X_19B)) for weights in (weights_fixed, weights_bad)]
answer_MB8_19c = [float(np.mean([estimate(f, s) for f, s in zip(f_19, s_19)])) for estimate in (estimate_fixed, estimate_bad)]
answer_MB8_19d = [strongest_bad(TOURNAMENT_A, TOURNAMENT_B), strongest_bad(TOURNAMENT_A, TOURNAMENT_B3)]
print("a)", np.round(answer_MB8_19a, 6).tolist(), " b)", np.round(answer_MB8_19b, 4).tolist(), " c)",
      np.round(answer_MB8_19c, 6).tolist(), " d)", answer_MB8_19d)
print("   forces de A :", np.round(ref_pg.bradley_terry_fit(TOURNAMENT_A), 4).tolist(), " de B :",
      np.round(ref_pg.bradley_terry_fit(TOURNAMENT_B), 4).tolist(), " de B avec B3 :",
      np.round(ref_pg.bradley_terry_fit(TOURNAMENT_B3), 4).tolist())''',
    record='''from scipy import stats as stats_19r

rate_19r = np.random.default_rng(8121).exponential(2.5, 100_000)
scores_19r = [float(np.mean(0.4 ** -1 - rate_19r)), float(np.mean((rate_19r - 0.4) / 0.4 ** 2))]
wbm.record("MB8.19a", scores_19r, decimals=5,
           mistakes={"la version corrigée d'abord, puis la version fautive": scores_19r[::-1],
                     "le second nombre est celui de la version FAUSSE, score_exp_bad": [scores_19r[0]] * 2,
                     "le premier nombre est celui de ta version corrigée, score_exp_fixed : ici elle rend encore ce que "
                     "rend la version fautive": [scores_19r[1]] * 2})
normal_19r = np.random.default_rng(8122).normal(0.0, 1.5, 50_000)
gap_19r = stats_19r.norm.logpdf(normal_19r, 0.8, 1.0) - stats_19r.norm.logpdf(normal_19r, 0.0, 1.5)
estimates_19r = [float(np.mean(np.exp(gap_19r) * normal_19r)), float(np.mean(np.exp(-gap_19r) * normal_19r))]
wbm.record("MB8.19b", estimates_19r, decimals=4,
           mistakes={"la version corrigée d'abord, puis la version fautive": estimates_19r[::-1],
                     "le second nombre est celui de la version FAUSSE, weights_bad": [estimates_19r[0]] * 2,
                     "le premier nombre est celui de ta version corrigée, weights_fixed : ici elle rend encore ce que rend "
                     "la version fautive": [estimates_19r[1]] * 2})
counts_19r = np.random.default_rng(8123).poisson(1.5, (20_000, 4))
hits_19r, slopes_19r = (counts_19r >= 2).astype(float), counts_19r / 1.5 - 1
total_19r = hits_19r.sum(axis=1, keepdims=True)
batch_19r = [float(np.mean(((hits_19r - (total_19r - hits_19r) / 3) * slopes_19r).mean(axis=1))),
             float(np.mean(((hits_19r - total_19r / 4) * slopes_19r).mean(axis=1)))]
wbm.record("MB8.19c", batch_19r, decimals=5,
           mistakes={"la version corrigée d'abord, puis la version fautive": batch_19r[::-1],
                     "le second nombre est celui de la version FAUSSE, estimate_bad": [batch_19r[0]] * 2,
                     "le premier nombre est celui de ta version corrigée, estimate_fixed : ici elle rend encore ce que "
                     "rend la version fautive": [batch_19r[1]] * 2,
                     "la moyenne des autres tirages d'un batch de n tirages porte sur n − 1 valeurs":
                         [float(np.mean(((hits_19r - (total_19r - hits_19r) / 4) * slopes_19r).mean(axis=1))),
                          batch_19r[1]]})
wbm.record("MB8.19d", "A0 B1", mistakes={"avant l'ajout de B3, puis après": "B1 A0"})
CASES_19r = __CASES_C19__                                                  # the hidden cases of the check
wbm.record(CASES_19r["id_scores"], [1 / theta - x for theta, xs in CASES_19r["scores"] for x in xs], decimals=9)
wbm.record(CASES_19r["id_weights"], [math.exp(a - b) for lp, lq in CASES_19r["weights"] for a, b in zip(lp, lq)],
           decimals=9)
wbm.record(CASES_19r["id_batches"], [sum((fi - (sum(f) - fi) / (len(f) - 1)) * si for fi, si in zip(f, s)) / len(f)
                                     for f, s in CASES_19r["batches"]], decimals=9)''',
    after=[
        ("solution", answers_check("MB8.19", "abc") + "\n" + CHECK_19D + "\n\n" + CHECK_19),
        ("md", "**Après la vérification**, dans ta copie : pour chacune des quatre erreurs, pourquoi la vérification du "
               "collègue ne la voyait-elle pas, et quelle vérification l'aurait vue ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB8.20 · two property tests of policy_gradient_exact
# ---------------------------------------------------------------------------
CHECK_20 = '''def load_hidden_c20():
    """The hidden methods (solutions/challenges/mb8_20.py: reading it spoils the exercise), as a module of its own."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("hidden_methods_c20", wbm.repo_root() / "solutions" / "challenges"
                                                  / "mb8_20.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


HIDDEN_C20 = load_hidden_c20()
WRONG_C20 = [   # a hidden wrong method, the test that must refuse it, and the clause of the statement it tries
    (HIDDEN_C20.occupancy, "matches_finite_differences_20", "d'un facteur 1 − γ sur chaque dérivée : ton test compare-t-il "
                                                            "bien les dérivées rendues aux différences finies ?"),
    (HIDDEN_C20.zeros, "matches_finite_differences_20", "partout (elle rend des zéros, de somme nulle) : ton test "
                                                        "compare-t-il bien les dérivées rendues aux différences finies ?"),
    (HIDDEN_C20.transposed, "matches_finite_differences_20", "dès que M n'est pas symétrique : tes MDP sont-ils tirés au "
                                                             "hasard, avec des P[a] quelconques ?"),
    (HIDDEN_C20.uniform, "matches_finite_differences_20", "dès que la politique d'un état n'est pas uniforme : tes "
                                                          "logits sont-ils quelconques (différents d'une action à "
                                                          "l'autre) ?"),
    (HIDDEN_C20.three_actions, "matches_finite_differences_20", "seulement avec 3 actions : tes MDP ont-ils parfois 3 "
                                                                "actions ?"),
    (HIDDEN_C20.four_states, "matches_finite_differences_20", "seulement à partir de 4 états : tes MDP vont-ils jusqu'à "
                                                              "5 états ?"),
    (HIDDEN_C20.mixed_rewards, "matches_finite_differences_20", "dès que les récompenses d'un état diffèrent d'une action "
                                                                "à l'autre : tes récompenses sont-elles quelconques ?"),
    (HIDDEN_C20.relative_8e6, "matches_finite_differences_20", "de 8·10⁻⁶ en valeur relative, ce que np.allclose laisse "
                                                               "passer par défaut (rtol = 1e-5) : ta tolérance est-elle "
                                                               "10⁻⁶ en valeur absolue, sur des dérivées de l'ordre de "
                                                               "1 (des récompenses de l'ordre de 1) ?"),
    (HIDDEN_C20.offset_large, "matches_finite_differences_20", "de 2,5·10⁻⁶ sur les dérivées d'au moins 0,25 en valeur "
                                                               "absolue : ta tolérance est-elle 10⁻⁶ en valeur absolue "
                                                               "(pas plus large, pas relative) ?"),
    (HIDDEN_C20.last_entry, "matches_finite_differences_20", "sur une seule dérivée, de 4·10⁻⁶ : ton test compare-t-il "
                                                             "chaque dérivée rendue, pour tous les s₀, s et a ?"),
    (HIDDEN_C20.values_not_advantages, "sums_to_zero_20", "sur la somme de chaque état (elle prend Q au lieu de "
                                                          "l'avantage) : ton test somme-t-il sur les actions ?"),
    (HIDDEN_C20.offset_sum, "sums_to_zero_20", "de 3·10⁻¹⁰ sur chaque dérivée, ce que np.allclose laisse passer par "
                                               "défaut (atol = 1e-8) : ta tolérance sur la somme est-elle 10⁻¹⁰ ?"),
    (HIDDEN_C20.one_pair, "sums_to_zero_20", "sur la somme d'un seul couple (s₀, s), de 5·10⁻¹⁰ : vérifies-tu tous les s₀ "
                                             "et tous les s, à 10⁻¹⁰ près ?"),
]

with checked("MB8.20"):
    results_20 = []
    report_20 = reporter(results_20, stop=False)
    TESTS_C20 = {"matches_finite_differences_20": matches_finite_differences_20, "sums_to_zero_20": sums_to_zero_20}

    def anonymous_c20(method):
        """method under a neutral name: a test must judge what the method does, not what it is called."""
        def method_c20(P, r, logits, gamma):
            return method(P, r, logits, gamma)
        method_c20.__name__ = method_c20.__qualname__ = "method"
        return method_c20

    def verdict_c20(name, label, method):
        got = call_safely(f"Ex MB8.20 : {name}({label})", TESTS_C20[name], anonymous_c20(method))
        if not isinstance(got, (bool, np.bool_)):
            if isinstance(got, (int, np.integer)):
                what = f"{int(got)} (un entier)"
            elif isinstance(got, (float, np.floating)):
                what = f"{float(got):g} (un nombre)"
            else:
                what = shown(got)
            print(f"❌ Ex MB8.20 : {name}({label}) rend {what}, pas True ou False")
            raise StopCheck
        return bool(got)

    PEEK_C20 = {"__closure__", "cell_contents", "__code__", "__wrapped__", "__defaults__", "__globals__", "__name__",
                "__qualname__", "__doc__", "__module__", "_getframe", "currentframe", "f_back", "f_locals", "f_globals",
                "inspect", "getsource", "get_objects", "WRONG_C20", "TESTS_C20", "HIDDEN_C20", "mb8_20"}

    def peeks_c20(function, seen=None):
        """The names of PEEK_C20 that the learner's function (or a function of the notebook it calls) uses, as a name
        or as a string."""
        seen = set() if seen is None else seen
        code = getattr(function, "__code__", None)
        if code is None or code in seen:
            return set()
        seen.add(code)
        found, todo = set(), [code]
        while todo:
            c = todo.pop()
            found |= PEEK_C20 & (set(c.co_names) | {k for k in c.co_consts if isinstance(k, str)})
            for name in c.co_names:
                target = globals().get(name)
                if callable(target) and getattr(target, "__module__", None) == "__main__":
                    found |= peeks_c20(target, seen)
            todo += [k for k in c.co_consts if hasattr(k, "co_code")]
        return found

    peeked_c20 = {name: sorted(peeks_c20(test)) for name, test in TESTS_C20.items()}
    peeked_c20 = {name: names for name, names in peeked_c20.items() if names}
    if peeked_c20:
        name_c20, names_c20 = next(iter(peeked_c20.items()))
        print(f"❌ Ex MB8.20 : {name_c20} lit la méthode ou la pile d'appels ({', '.join(names_c20)}) au lieu de "
              "l'exécuter : un test juge ce que fait la méthode sur tes MDP")
        raise StopCheck

    LIBRARY_FILES_C20 = [REF.policy_gradient.__file__]
    try:
        LIBRARY_FILES_C20.append(mymath.policy_gradient.__file__)          # your own policy_gradient.py too
    except Exception:  # noqa: BLE001 - no module of yours yet: only the reference is watched
        pass

    def watched_c20(name, label, method):
        """The verdict of one test on a method that never calls policy_gradient.py: a call comes from the test."""
        with code_from(LIBRARY_FILES_C20) as seen:
            got = verdict_c20(name, label, method)
        if seen:
            print(f"❌ Ex MB8.20 : {name} appelle policy_gradient_exact ({seen[0]}) : un test compare la méthode à des "
                  "différences finies centrées de valeurs calculées par np.linalg.solve, ou à 0 pour la somme, pas à "
                  "une autre version de la fonction")
            raise StopCheck
        return got

    on_ref_c20 = [verdict_c20(name, "policy_gradient_exact de la référence", ref_pg.policy_gradient_exact)
                  for name in TESTS_C20]
    report_20(passes("MB8.20a", on_ref_c20), "tes deux tests, sur policy_gradient_exact de la référence",
              "tes deux tests ne rendent pas True sur policy_gradient_exact de la référence, qui vérifie les deux "
              "propriétés : relis le choix du pas h (l'arrondi et la troncature, M05a §7) et des tolérances")
    twins_c20 = [watched_c20(name, label, method) for label, method in (("le système dérivé, logit par logit",
                                                                         HIDDEN_C20.per_logit),
                                                                        ("la formule, M par np.linalg.inv",
                                                                         HIDDEN_C20.inverse_formula))
                 for name in TESTS_C20]
    report_20(all(twins_c20), "deux autres méthodes justes reçoivent aussi True",
              "deux autres méthodes justes (le système de Bellman dérivé logit par logit, la formule avec M par "
              "np.linalg.inv ; des arrondis de l'ordre de 10⁻¹⁵) ne reçoivent pas toutes True : ta tolérance est-elle "
              "trop stricte, ou ton pas h mal choisi ?")
    for number_c20, (method_c20, name_c20, clause_c20) in enumerate(WRONG_C20, start=1):
        refused_c20 = not watched_c20(name_c20, f"méthode fausse cachée n° {number_c20}", method_c20)
        report_20(refused_c20, f"{name_c20} refuse la méthode fausse cachée n° {number_c20}",
                  f"{name_c20} accepte la méthode fausse cachée n° {number_c20}, fausse {clause_c20}")
    verdict("MB8.20", all(results_20) and len(results_20) == 2 + len(WRONG_C20), "tes deux tests jugent juste "
            "policy_gradient_exact de la référence et deux autres méthodes justes, et refusent les méthodes fausses "
            "cachées.", "relis les lignes ❌ ci-dessus.")'''

NOTE_20 = (r"Une correction possible : `matches_finite_differences_20` tire cinq MDP (les tailles $(2, 3)$, $(3, 2)$, "
           r"$(4, 3)$, $(5, 2)$ et $(5, 3)$ ; des lignes de $\mathbf{P}[a]$ tirées dans une loi de Dirichlet, des "
           r"récompenses et des logits normaux, $\gamma$ parmi $0{,}6$ et $0{,}7$), calcule les valeurs par "
           r"`np.linalg.solve` en $z \pm h\,\mathbf{e}_{s,a}$ avec $h = 10^{-5}$, et compare à $10^{-6}$ près en valeur "
           r"absolue ; `sums_to_zero_20` compare `grad.sum(axis=2)` à 0 à $10^{-10}$ près. a) `[True, True]`.")

MB8_20 = ex(
    "MB8.20", "écrire deux tests de propriété du gradient exact, et voir ce que chacun attrape.",
    "fiche §4 ; M05a §7 (différences finies, choix du pas) ; Ex MB8.14", note=NOTE_20,
    body=r"""Écris deux fonctions qui testent une méthode qu'on leur passe, de la même signature que `policy_gradient_exact(P, r, logits, gamma)` (elle rend `(V, grad)`), et rendent `True` si la propriété tient, `False` sinon :
- `matches_finite_differences_20(method)` tire au hasard plusieurs MDP (de 2 à 5 états, 2 ou 3 actions, des matrices $\mathbf{P}[a]$ stochastiques, des récompenses et des logits quelconques, $\gamma$ parmi $0{,}6$ et $0{,}7$) et compare chaque dérivée rendue à la différence finie centrée des valeurs calculées par `np.linalg.solve`, à $10^{-6}$ près en valeur absolue (plus finement que la tolérance par défaut de `np.allclose`, `rtol=1e-5`, `atol=1e-8`) ;
- `sums_to_zero_20(method)` vérifie, sur des MDP tirés au hasard, que pour tout $s_0$ et tout $s$ la somme des dérivées sur les actions de $s$ est nulle à $10^{-10}$ près.

Choisis le pas de tes différences finies pour que la référence passe : l'erreur d'une différence finie centrée a deux parts, la troncature, de l'ordre de $h^2$, et l'arrondi, de l'ordre de $\frac{\varepsilon}{h}$ (M05a §7).

La vérification lance tes deux tests sur `policy_gradient_exact` de la référence (`ref_pg.policy_gradient_exact`), sur deux autres méthodes justes, puis sur des méthodes fausses cachées, passées sous un nom neutre (un test juge ce que fait la méthode, pas son nom), une au moins par clause de l'énoncé, que chaque test doit refuser quand sa propriété est fausse. Un test exécute la méthode sur ses MDP et compare ses résultats à ce que dit la propriété : il ne lit ni la méthode ni la pile d'appels, et n'appelle pas `policy_gradient_exact` (ni celle de la référence, ni la tienne : la vérification le contrôle). Relève :
- a) les résultats de tes deux tests sur `policy_gradient_exact` de la référence (une liste de 2 booléens, dans l'ordre différences finies, somme nulle).""",
    todo='''def matches_finite_differences_20(method):
    """True when, on several MDPs drawn at random, every derivative of method(P, r, logits, gamma)[1] is within 1e-6
    of the centred finite difference of the values computed by np.linalg.solve; False otherwise."""
    raise NotImplementedError("matches_finite_differences_20 n'est pas encore écrite (04_indices.md si tu bloques)")


def sums_to_zero_20(method):
    """True when, on several MDPs drawn at random, the derivatives of method(P, r, logits, gamma)[1] sum to 0 over the
    actions of each state s, for every s0 and s, within 1e-10; False otherwise."""
    raise NotImplementedError("sums_to_zero_20 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB8_20a = ...
with wbm.attempt("MB8.20"):          # your two tests: ⏳ while they are not written
    answer_MB8_20a = ...  # a) a list of 2 booleans: your two tests on ref_pg.policy_gradient_exact''',
    check=answers_check("MB8.20", "a") + "\n\n" + CHECK_20,
    solution='''rng_20 = np.random.default_rng(8124)
SIZES_20 = ((2, 3), (3, 2), (4, 3), (5, 2), (5, 3))        # (states, actions): every size of the statement


def random_mdp_20(m, K):
    """A random MDP of m states and K actions: stochastic rows of P[a] (Dirichlet), normal rewards and logits, γ among
    0.6 and 0.7."""
    P = rng_20.dirichlet(np.ones(m), size=(K, m))
    return P, rng_20.normal(size=(K, m)), rng_20.normal(size=(m, K)), float(rng_20.choice([0.6, 0.7]))


def values_20(P, r, logits, gamma):
    """The values V, by np.linalg.solve on (I - γ P_π) V = r_π."""
    pi = np.exp(logits - logits.max(axis=1, keepdims=True))
    pi = pi / pi.sum(axis=1, keepdims=True)
    P_pi, r_pi = np.einsum("sa,ast->st", pi, P), np.einsum("sa,as->s", pi, r)
    return np.linalg.solve(np.eye(len(r_pi)) - gamma * P_pi, r_pi)


def matches_finite_differences_20(method, h=1e-5):
    """True when, on several MDPs drawn at random, every derivative of method(P, r, logits, gamma)[1] is within 1e-6
    of the centred finite difference of the values computed by np.linalg.solve; False otherwise."""
    for m, K in SIZES_20:
        P, r, logits, gamma = random_mdp_20(m, K)
        grad = np.asarray(method(P, r, logits, gamma)[1], dtype=float)
        if grad.shape != (m, m, K):
            return False
        for s in range(m):
            for a in range(K):
                step = np.zeros((m, K))
                step[s, a] = h
                fd = (values_20(P, r, logits + step, gamma) - values_20(P, r, logits - step, gamma)) / (2 * h)
                if np.max(np.abs(grad[:, s, a] - fd)) > 1e-6:
                    return False
    return True


def sums_to_zero_20(method):
    """True when, on several MDPs drawn at random, the derivatives of method(P, r, logits, gamma)[1] sum to 0 over the
    actions of each state s, for every s0 and s, within 1e-10; False otherwise."""
    for m, K in SIZES_20:
        P, r, logits, gamma = random_mdp_20(m, K)
        grad = np.asarray(method(P, r, logits, gamma)[1], dtype=float)
        if grad.shape != (m, m, K) or np.max(np.abs(grad.sum(axis=2))) > 1e-10:
            return False
    return True


answer_MB8_20a = [matches_finite_differences_20(ref_pg.policy_gradient_exact), sums_to_zero_20(ref_pg.policy_gradient_exact)]
P_h_20, r_h_20, z_h_20, g_h_20 = random_mdp_20(4, 3)
exact_h_20 = ref_pg.policy_gradient_exact(P_h_20, r_h_20, z_h_20, g_h_20)[1][:, 1, 2]
gaps_h_20 = {}
for h in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-8, 1e-10, 1e-12):
    step = np.zeros((4, 3))
    step[1, 2] = h
    gaps_h_20[h] = float(np.max(np.abs((values_20(P_h_20, r_h_20, z_h_20 + step, g_h_20)
                                        - values_20(P_h_20, r_h_20, z_h_20 - step, g_h_20)) / (2 * h) - exact_h_20)))
print("a)", answer_MB8_20a)
print("   écart à la différence finie selon h :", {f"{h:.0e}": f"{gap:.1e}" for h, gap in gaps_h_20.items()})''',
    record='''def properties_20r(method):
    """The oracle: the two properties, measured on other MDPs than any test of the notebook (seed 8127), with
    Richardson-extrapolated centred differences."""
    rng = np.random.default_rng(8127)
    ok_fd, ok_sum = True, True
    for m, K in ((3, 3), (5, 2), (4, 2)):
        P = rng.dirichlet(np.ones(m), size=(K, m))
        r, z, gamma = rng.normal(size=(K, m)), rng.normal(size=(m, K)), 0.7

        def values(logits):
            pi = np.exp(logits - logits.max(axis=1, keepdims=True))
            pi = pi / pi.sum(axis=1, keepdims=True)
            return np.linalg.solve(np.eye(m) - gamma * np.einsum("sa,ast->st", pi, P), np.einsum("sa,as->s", pi, r))
        grad = method(P, r, z, gamma)[1]
        for s in range(m):
            for a in range(K):
                def fd(h):
                    step = np.zeros((m, K))
                    step[s, a] = h
                    return (values(z + step) - values(z - step)) / (2 * h)
                ok_fd = ok_fd and bool(np.max(np.abs((4 * fd(5e-4) - fd(1e-3)) / 3 - grad[:, s, a])) < 1e-8)
        ok_sum = ok_sum and bool(np.max(np.abs(grad.sum(axis=2))) < 1e-12)
    return [ok_fd, ok_sum]


wbm.record("MB8.20a", properties_20r(ref_pg.policy_gradient_exact),
           mistakes={"policy_gradient_exact de la référence est juste : un test de différences finies qui la refuse a un "
                     "pas h ou une tolérance qui ne conviennent pas": [False, True],
                     "policy_gradient_exact de la référence est juste : un test de somme nulle qui la refuse a une "
                     "tolérance trop fine, ou somme sur le mauvais axe": [True, False]})''',
    after=[
        ("solution", answers_check("MB8.20", "a") + "\n\n" + CHECK_20),
        look("quel pas $h$ donne le plus petit écart, et pourquoi pas $h = 10^{-12}$ ? Quelle méthode fausse passerait "
             "le test de somme nulle seul ? Pourquoi tirer les MDP au hasard, avec des logits non nuls ?"),
    ],
)

PART_C = Part("C", "Déboguer, tester",
              "Fiche §1, §3, §4, §6 et §7. Quatre erreurs, qui passent une vérification trop faible ; deux tests de "
              "propriété du gradient exact. Le code du collègue s'appuie sur la référence (`ref_pg`), pour ne pas "
              "dépendre de ton code.", exercises=[MB8_19, MB8_20])

# ---------------------------------------------------------------------------
# Notebook exercise: the challenge (MB8.21)
# ---------------------------------------------------------------------------
GIVEN_21 = '''# The trial case of the challenge: the waits on the phone of MB8.1 (an exponential law of rate 0.1), the threshold 18
# minutes and a budget of 10 000 draws; trial_draw_21() returns a new draw function for it (seed 8125), which counts the
# draws it serves
TRIAL_21 = MappingProxyType({"rate": 0.1, "c": 18.0, "budget": 10_000})


def trial_draw_21(seed=8125):
    """A new function draw(k, delta=0.0) for the trial case: k draws of the exponential law of rate 0.1 + delta and their
    scores at that rate (two float arrays); beyond TRIAL_21["budget"] draws in all, NaNs."""
    rng, used = np.random.default_rng(seed), [0]

    def draw(k, delta=0.0):
        if isinstance(k, (bool, np.bool_)) or not isinstance(k, numbers.Integral) or k < 0:
            raise ValueError(f"draw(k) prend un nombre entier de tirages k >= 0, reçu {k!r}")
        if isinstance(delta, (bool, np.bool_)) or not isinstance(delta, numbers.Real) or not math.isfinite(delta):
            raise ValueError(f"draw(k, delta) prend un décalage delta réel et fini, reçu {delta!r}")
        k, rate = int(k), TRIAL_21["rate"] + float(delta)
        if used[0] + k > TRIAL_21["budget"]:
            used[0] = TRIAL_21["budget"] + 1
            return np.full(k, np.nan), np.full(k, np.nan)
        used[0] += k
        if rate <= 0:
            return np.full(k, np.nan), np.full(k, np.nan)
        x = rng.exponential(1 / rate, k)
        return x, 1 / rate - x
    return draw'''

CHECK_21 = """def check_c21():
    \"\"\"The check of MB8.21, in a function. The hidden laws come from another process (the hidden module run as a
    script): it draws them, serves the draws of each case and counts them, and compares the estimates it receives with
    the exact derivatives only at the end; no hidden law, parameter nor derivative lives in this process while the
    learner's function runs. Each call runs under code_from (the learner's function may not run code of the hidden
    module, nor open it, nor start a process) and under a time limit where the system allows one (it only stops a
    runaway computation).\"\"\"
    import json
    import signal
    import subprocess
    import sys
    import threading
    hidden_file = wbm.repo_root() / "solutions" / "challenges" / "mb8_21.py"   # reading it spoils the challenge
    twins = code_keys_of_file(hidden_file)                      # its functions, to recognise a copy run from elsewhere
    results = []
    report = reporter(results, stop=False)
    largest_request = 1_000_000                                 # the most draws asked to the other process at once

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

    def exactly(stream, size):
        data = stream.read(size)
        if len(data) != size:
            raise OSError("échange interrompu")
        return data

    def send(line):
        server.stdin.write((line + "\\n").encode())
        server.stdin.flush()

    def draw_of(k, budget):
        \"\"\"The function draw(n, delta=0.0) of case k: its draws come from the other process, which counts them.\"\"\"
        used = [0]

        def draw(n, delta=0.0):
            if isinstance(n, (bool, np.bool_)) or not isinstance(n, numbers.Integral) or n < 0:
                raise ValueError(f"draw(k) prend un nombre entier de tirages k >= 0, reçu {n!r}")
            if isinstance(delta, (bool, np.bool_)) or not isinstance(delta, numbers.Real) or not math.isfinite(delta):
                raise ValueError(f"draw(k, delta) prend un décalage delta réel et fini, reçu {delta!r}")
            n = int(n)
            if used[0] + n > budget:
                used[0] = budget + 1
                send(f"O {k}")
                if n > 10 * budget + 10:
                    raise ValueError(f"draw({n}) : {n} tirages, bien plus que le budget de {budget}")
                return np.full(n, np.nan), np.full(n, np.nan)
            used[0] += n
            xs, ss, left = [], [], n
            while True:
                part = min(left, largest_request)
                send(f"D {k} {part} {float(delta)!r}")
                data = np.frombuffer(exactly(server.stdout, 16 * part), dtype="<f8")
                xs.append(data[:part])
                ss.append(data[part:])
                left -= part
                if left <= 0:
                    break
            return np.concatenate(xs).copy(), np.concatenate(ss).copy()
        return draw

    def estimate(label, k, c, budget):
        \"\"\"derivative_21 on case k, under code_from and a time limit: a float, or None (not a finite number).\"\"\"
        try:
            with time_limit(120):
                with code_from([hidden_file], twins=twins, escapes=True) as seen:
                    out = call_safely(label, derivative_21, draw_of(k, budget), float(c), int(budget))
        except TimeUp:
            print(f"❌ {label} : ta fonction n'a pas fini en 120 s : une boucle s'arrête-t-elle ?")
            raise StopCheck from None
        if seen and seen[0].startswith("lance "):
            print(f"❌ {label} : derivative_21 {seen[0].replace(' : ', ' (', 1)}) : l'estimation se calcule dans ta "
                  "fonction ; ce qu'exécute un autre processus échappe à la vérification")
            raise StopCheck
        if seen:
            what = "lit" if seen[0].startswith("ouvre ") else "exécute du code de"
            where = "" if seen[0].startswith("ouvre ") else f" ({seen[0]})"
            print(f"❌ {label} : derivative_21 {what} solutions/challenges/mb8_21.py{where}, la partie cachée du défi, "
                  "ou une copie de son code : la vérification mesurerait sa méthode, pas la tienne")
            raise StopCheck
        value = as_floats(out)
        if value is None or value.shape != ():
            print(f"❌ {label} : derivative_21 rend un nombre, l'estimation de J'(θ), reçu {shown(out)}")
            raise StopCheck
        return float(value) if math.isfinite(float(value)) else None

    server = subprocess.Popen([sys.executable, "-I", str(hidden_file), "--serve"], stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)   # this kernel's Python, here or on Colab
    try:
        head = json.loads(server.stdout.readline())
        count, thresholds, budgets = head["count"], head["c"], head["budget"]
        estimates = []
        for k in range(count):
            label = ("Ex MB8.21 : derivative_21 (le cas d'essai, des tirages de l'autre processus)" if k == count - 1
                     else f"Ex MB8.21 : derivative_21 (cas caché {k + 1})")
            value = estimate(label, k, thresholds[k], budgets[k])
            estimates.append(value)
            send(f"R {k} {value!r}" if value is not None else f"R {k} nan")
        given = filled(answer_MB8_21a) and as_floats(answer_MB8_21a) is not None \\
            and as_floats(answer_MB8_21a).shape == () and math.isfinite(float(as_floats(answer_MB8_21a)))
        if given:
            send(f"A {float(as_floats(answer_MB8_21a))!r}")
        send("verdict")                                        # only now: the families, the errors, the verdicts
        measured = json.loads(server.stdout.readline())
        cases, answer = measured["cases"], measured["answer"]
        assert len(cases) == count
    except (OSError, ValueError, KeyError, TypeError, AssertionError) as exc:
        print("❌ Ex MB8.21 : la vérification n'a pas pu échanger les tirages et les estimations avec le processus qui "
              f"tire les lois cachées ({type(exc).__name__} ; ta fonction a-t-elle touché à ce processus ?) : exécute à "
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

    def percent(rel):
        return "non fini" if rel is None else f"{fr(100 * rel, 0)} %"

    notebook, hidden = cases[-1], cases[:-1]
    report(notebook["ok"], "le cas d'essai, avec des tirages de l'autre processus : à 10 % près de J'(θ)",
           "le cas d'essai, avec des tirages de l'autre processus : " + (
               "ta fonction dépasse le budget de 10 000 tirages" if notebook["over_budget"] else
               "ton estimation n'est pas un nombre fini" if estimates[-1] is None else
               "ton estimation est à plus de 10 % de J'(θ)"))
    for number in sorted({case["series"] for case in hidden}):  # what each series of hidden cases measured
        series = [case for case in hidden if case["series"] == number]
        missed = [case for case in series if not case["ok"]]
        kinds = [kind for kind in ("très fréquent", "fréquent", "moyen", "rare") if any(c["kind"] == kind for c in missed)]
        gaps = [case["rel"] for case in missed if case["rel"] is not None and not case["over_budget"]]
        print(f"   série {number} : {len(series) - len(missed)} sur {len(series)} à 10 % près"
              + ("" if not missed else " ; manqués : " + ", ".join(
                  f"« {kind} » ×{sum(c['kind'] == kind for c in missed)}" for kind in kinds)
                 + (f" (écart le plus grand : {percent(max(gaps))})" if gaps else "")
                 + (f" ; {sum(c['over_budget'] for c in missed)} au-delà du budget"
                    if any(c["over_budget"] for c in missed) else "")))
    succeeded = sum(case["ok"] for case in hidden)
    needed = math.ceil(0.9 * len(hidden))
    over = [case for case in hidden if case["over_budget"]]
    hidden_values = [value for value in estimates[:-1] if value is not None]
    if succeeded >= needed:
        why = ""
    elif over:
        why = (f" ; {len(over)} cas dépassent leur budget : les appels de draw, réunis, ne doivent pas demander plus de "
               "budget tirages (au-delà, des nan)")
    elif sum(case["used"] for case in hidden) == 0:
        why = " ; ta fonction n'appelle jamais draw : elle ne connaît des lois cachées que ce que le notebook lui montre"
    elif len(hidden_values) >= 3 and max(hidden_values.count(value) for value in hidden_values) >= 3:
        why = (" ; ta fonction rend la même valeur pour plusieurs cas différents : se sert-elle de nombres du cas "
               "d'essai au lieu des tirages qu'elle reçoit ?")
    else:
        failed = [case for case in hidden if not case["ok"]]
        share = {kind: sum(case["kind"] == kind for case in failed) / len(failed) for kind in
                 ("très fréquent", "fréquent", "moyen", "rare")}
        if share["très fréquent"] + share["fréquent"] >= 0.7:
            why = (" ; la plupart de tes échecs sont des cas « très fréquents » ou « fréquents », où P(X > c) est proche "
                   "de 1 : que vaut alors f(x_i) pour presque tous les tirages, et que devient ton estimateur ?")
        elif share["rare"] >= 0.7:
            why = (" ; la plupart de tes échecs sont des cas « rares », où peu de tirages dépassent c : que vaut alors "
                   "f(x_i) pour presque tous les tirages, et que devient ton estimateur ?")
        else:
            why = (" ; tes échecs touchent toutes les sortes de cas : l'espérance de ton estimation est-elle bien J'(θ), "
                   "et sa dispersion assez petite avec ce budget (fiche §2 et §3) ?")
    report(succeeded >= needed, f"les {len(hidden)} cas cachés : {succeeded} à 10 % près (au moins {needed} demandés)",
           f"les {len(hidden)} cas cachés : {succeeded} à 10 % près, moins que les {needed} demandés" + why)
    report(not over, f"le budget : aucun des {len(hidden)} cas cachés n'en demande plus",
           f"le budget : {len(over)} cas cachés en demandent plus (au-delà, draw rend des nan)")
    if not given:
        print("⏳ Ex MB8.21a : pas encore fait." if not filled(answer_MB8_21a) else
              f"❌ Ex MB8.21a : a) est un nombre fini, ton estimation pour le cas d'essai, reçu {shown(answer_MB8_21a)}")
    else:
        print("✅ Ex MB8.21a : ton estimation pour le cas d'essai est à 10 % près de la dérivée exacte." if answer["ok"]
              else "❌ Ex MB8.21a : ton estimation pour le cas d'essai est à plus de 10 % de la dérivée exacte (ta "
                   "réponse à MB8.1 b) : relis-la, et la méthode de ta fonction")
    verdict("MB8.21", all(results) and len(results) == 3, "critère atteint : le cas d'essai, et au moins neuf cas cachés "
            "sur dix, à 10 % près, sans dépasser les budgets.", "critère pas encore atteint : relis les lignes ❌ "
            "ci-dessus.")


with checked("MB8.21"):
    check_c21()"""

NOTE_21 = (r"`derivative_21` : tout le budget en $\delta = 0$ ; $f_i = \mathbf{1}\{x_i > c\}$ ; la baseline optimale "
           r"estimée sur les mêmes tirages, $\hat b = \frac{\sum_if_is_i^2}{\sum_is_i^2}$ (la moyenne des autres "
           r"tirages fait aussi bien) ; puis la moyenne des $(f_i - \hat b)\,s_i$. a) Une estimation à quelques "
           r"pour cent de la dérivée exacte. Sur les cas cachés, l'estimateur sans baseline échoue sur les cas où "
           r"$P(X > c)$ est proche de 1, une baseline constante $\frac12$ aussi, une baseline constante 1 sur les cas "
           r"rares.")

MB8_21 = ex(
    "MB8.21", "estimer avec un budget de tirages la dérivée d'une probabilité de dépassement pour une loi qu'on ne "
    "connaît pas, et le vérifier sur des lois cachées.", "fiche §2 et §3 ; Ex MB8.1, MB8.13, MB8.17", note=NOTE_21,
    given=GIVEN_21,
    body=r"""Écris `derivative_21(draw, c, budget)`, qui estime $J'(\theta) = \frac{\mathrm{d}}{\mathrm{d}\theta}P_\theta(X > c)$ pour une loi $p_\theta$ que tu ne connais pas. Ta fonction peut appeler `draw(k, delta=0.0)`, qui rend deux tableaux de `k` flottants : `k` tirages indépendants $x_i$ de $p_{\theta + \delta}$, puis leurs scores $s_{\theta + \delta}(x_i)$, au paramètre du tirage ; ses appels réunis ne doivent pas dépasser `budget` tirages (au-delà, `draw` rend des `nan`, et le cas échoue). Ni la famille de la loi ni $\theta$ ne sont donnés : la loi est exponentielle, de Poisson, normale ou binomiale, et le seuil $c$ donne une probabilité $P_\theta(X > c)$ qui va de presque 0 à presque 1. Le notebook fournit un cas d'essai, les attentes au téléphone de MB8.1 (`TRIAL_21` : taux $0{,}1$, seuil 18 minutes, budget de 10 000 tirages), et une fonction `draw` pour lui (`trial_draw_21()` en rend une nouvelle, qui compte ses tirages).

**Critère de réussite :** ton estimation est à 10 % près (en valeur relative) de $J'(\theta)$ pour le cas d'essai, et pour au moins 90 % des 120 cas cachés (douze séries de dix), tirés à nouveau à chaque exécution par un processus à part, qui sert les tirages et compte ceux de chaque cas. Ta fonction ne doit pas exécuter le code du module caché du défi (`solutions/challenges/mb8_21.py`) : la vérification le contrôle. Relève :
- a) ton estimation pour le cas d'essai (un nombre ; la vérification la compare à la dérivée exacte, à 10 % près).

Point de départ : la dérivée par le chemin d'une indicatrice est nulle ; des différences finies entre deux échantillons indépendants, à $\theta + h$ et à $\theta - h$, noient l'écart de deux probabilités voisines dans leur bruit ; l'estimateur score sans baseline est sans biais, mais est-il assez précis dans tous les cas ?""",
    todo='''def derivative_21(draw, c, budget):
    """An estimate of J'(θ) = d/dθ P_θ(X > c) for a law p_θ you do not know: draw(k, delta=0.0) returns k draws of
    p_{θ+δ} and their scores at θ + δ (two float arrays); at most budget draws in all."""
    raise NotImplementedError("derivative_21 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB8_21a = ...
with wbm.attempt("MB8.21"):          # your derivative_21: ⏳ while it is not written
    answer_MB8_21a = ...  # a) a number, as computed: your estimate for the trial case (a new trial_draw_21(), TRIAL_21["c"], TRIAL_21["budget"])''',
    check=CHECK_21,
    solution='''def derivative_21(draw, c, budget):
    """An estimate of J'(θ) = d/dθ P_θ(X > c) for a law p_θ you do not know: draw(k, delta=0.0) returns k draws of
    p_{θ+δ} and their scores at θ + δ (two float arrays); at most budget draws in all."""
    x, s = draw(int(budget))                                   # the whole budget at θ: no difference of two samples
    f = (x > c).astype(float)
    b = float(np.sum(f * s ** 2) / np.sum(s ** 2))             # the optimal baseline, estimated on the same draws
    return float(np.mean((f - b) * s))


answer_MB8_21a = derivative_21(trial_draw_21(), TRIAL_21["c"], TRIAL_21["budget"])
print("a)", round(answer_MB8_21a, 4))''',
    after=[
        ("solution", CHECK_21),
        ("md", "**Pour réfléchir** (une fois le critère atteint) : sur quelles sortes de cas cachés (les lignes de chaque "
               "série) ta première idée a-t-elle échoué, et pourquoi ? Que vaut $f(x_i)$ pour presque tous les tirages "
               "d'un cas « très fréquent », d'un cas « rare » ? Ta fonction a-t-elle eu besoin de connaître la famille "
               "de la loi ? Les réponses sont dans `05_solutions.md`, section Notebook."),
    ],
)

PART_D = Part("D", "Défi", "Fiche §2 et §3. La dérivée d'une probabilité de dépassement pour une loi inconnue, avec un "
              "budget de tirages, vérifiée sur des lois cachées tirées à chaque exécution.", exercises=[MB8_21])

PARTS = [PART_A, PART_B, PART_C, PART_D]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | MB8.1 à MB8.7, MB8.11 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, exercise in enumerate(part.exercises):
            rows.append(exercise.table_row(part.key if i == 0 else ""))
    if kind == "exercise":
        title = "# MB8 · Gradient de politique — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). Dans "
               "les parties A à D, donne les valeurs que rend le calcul, **sans les arrondir** : les décimales "
               "demandées sont celles de ta copie. « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli : ce qui n'est pas fait affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/mb8_gradient_politique/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py MB8`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# MB8 · Gradient de politique — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : une attente au téléphone, des graines en godet, un camion de "
               "crêpes, l'état d'une route, un panel de sondage, un tournoi de babyfoot, une cantine, et un pont vers la "
               "loss de substitution.\n"
               "- Écrire les quatre fonctions de `mymath/policy_gradient.py` (`score_function_gradient`, "
               "`policy_gradient_exact`, `importance_weights`, `bradley_terry_fit`) et les tester.\n"
               "- Prédire puis mesurer la dispersion de l'estimateur score pour trois baselines, estimer un événement "
               "rare par échantillonnage d'importance, corriger quatre erreurs, écrire deux tests de propriété, et "
               "relever un défi.\n\n"
               r"**Rappel express.** Le score en $\theta$ : $s_\theta(x) = \partial_\theta\ln p_\theta(x)$, d'espérance "
               r"nulle quand le support ne dépend pas de $\theta$ ; $\frac{\mathrm{d}}{\mathrm{d}\theta}"
               r"\mathbb{E}_\theta[f(X)] = \mathbb{E}_\theta[f(X)\,s_\theta(X)]$, et toute constante $b$ garde "
               r"$(f - b)\,s$ sans biais ; $b^\star = \frac{\mathbb{E}[fs^2]}{\mathbb{E}[s^2]}$. Une politique softmax "
               r"tabulaire : $\frac{\partial V(s_0)}{\partial z(s, a)} = \mathbf{M}[s_0, s]\,\pi(a \mid s)\,A(s, a)$, "
               r"avec $\mathbf{M} = (\mathbf{I} - \gamma\mathbf{P}_\pi)^{-1}$. L'échantillonnage d'importance : "
               r"$\mathbb{E}_p[f] = \mathbb{E}_q\big[\frac pq f\big]$, la taille effective "
               r"$\frac{(\sum w_i)^2}{\sum w_i^2}$. Bradley-Terry : $P(i \text{ bat } j) = \sigma(\beta_i - \beta_j)$, "
               r"victoires observées = victoires attendues au maximum.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu calculer la fonction score d'une loi usuelle, et son information de Fisher ?\n"
               "2. Sais-tu dériver l'espérance d'une indicatrice par la méthode du score, et dire pourquoi la dérivée "
               "par le chemin y échoue ?\n"
               "3. Sais-tu réduire la variance d'un estimateur score par une baseline, et dire laquelle garde "
               "l'estimateur sans biais ?\n"
               "4. Sais-tu calculer le gradient de la valeur d'une politique softmax tabulaire par le système de "
               "Bellman ?\n"
               "5. Sais-tu repondérer des tirages d'une loi pour estimer une moyenne sous une autre, et lire la taille "
               "effective ?\n"
               "6. Sais-tu ajuster les forces d'un modèle de Bradley-Terry, et dire quand elles n'existent pas ?\n\n"
               "**La suite** : le chapitre bonus B8 de workbookIA, qui applique ces outils.")]


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
    import numpy as np

    out = {}
    ref = load_module(ROOT / "solutions" / "mymath_ref" / "policy_gradient.py", "policy_gradient_build")

    # MB8.14: the MDP of three states and two actions of work_c/nb_values.py (state 2 unreachable from states 0 and 1)
    P14 = [[[0.7, 0.3, 0.0], [0.4, 0.6, 0.0], [0.5, 0.0, 0.5]], [[0.2, 0.8, 0.0], [0.9, 0.1, 0.0], [0.0, 0.3, 0.7]]]
    R14 = [[1.0, 0.0, 2.0], [0.5, 2.0, -1.0]]
    Z14 = [[0.2, -0.3], [0.0, 0.6], [-0.5, 0.4]]
    V14, G14 = ref.policy_gradient_exact(P14, R14, Z14, 0.6)
    assert np.allclose(G14[0, 2], 0) and not np.allclose(G14[2, 2], 0)
    assert not any(near_limit(v, 6) for v in G14[0].ravel() if abs(v) > 1e-12)
    assert not any(near_limit(v, 5) for v in G14[2].ravel())
    out["__P_14__"], out["__R_14__"], out["__LOGITS_14__"] = literal(P14), literal(R14), literal(Z14)

    # MB8.15: the log-densities of work_c/nb_values.py (rounded to 4 decimals there)
    lp15 = [-1311.7703, -1280.1143, -1290.4471, -1286.6555, -1244.938]
    lq15 = [-1310.5853, -1278.9503, -1289.6596, -1286.9464, -1244.907]
    with np.errstate(under="ignore", invalid="ignore"):
        assert np.all(np.isnan(np.exp(lp15) / np.exp(lq15)))
    w15, e15 = ref.importance_weights(lp15, lq15, self_normalize=True)
    assert not near_limit(w15.max(), 5) and not near_limit(e15, 5)
    out["__LOG_P_15__"], out["__LOG_Q_15__"] = literal(lp15), literal(lq15)

    # MB8.16: the league of six clubs (unequal numbers of matches)
    W16 = [[0, 3, 4, 2, 5, 6], [2, 0, 3, 3, 4, 5], [1, 2, 0, 3, 4, 4], [3, 2, 2, 0, 3, 3], [0, 1, 1, 2, 0, 2],
           [1, 0, 1, 2, 3, 0]]
    b16 = ref.bradley_terry_fit(W16)
    assert not any(near_limit(v, 7, 0.1) for v in list(b16) + [1 / (1 + math.exp(b16[5] - b16[0]))])
    out["__WINS_16__"] = literal(W16)

    # MB8.18: the sub-ID of the orders of size of the relative standard deviations
    out["__HIDDEN_C18__"] = literal({"id_sizes": "MB8.18d"})

    # MB8.19: the tournaments of work_c/nb_values.py; the faulty answer changes when B3 joins B
    TA, TB = [[0, 5, 6], [3, 0, 4], [2, 4, 0]], [[0, 4, 3], [4, 0, 5], [5, 3, 0]]
    TB3 = [[0, 4, 3, 5], [4, 0, 5, 5], [5, 3, 0, 5], [1, 1, 1, 0]]

    def faulty(a, b):
        ba, bb = ref.bradley_terry_fit(a), ref.bradley_terry_fit(b)
        return f"A{int(np.argmax(ba))}" if ba.max() >= bb.max() else f"B{int(np.argmax(bb))}"
    assert (faulty(TA, TB), faulty(TA, TB3), faulty(TA, TA)) == ("A0", "B1", "A0")
    out["__TOURNAMENT_A__"], out["__TOURNAMENT_B__"], out["__TOURNAMENT_B3__"] = literal(TA), literal(TB), literal(TB3)

    # MB8.19: the hidden cases: other rates (never 1, 0.4, nor the rates of the fiche), non-dyadic points; moderate
    # log-densities (non-dyadic); batches of 2 to 7 draws with any values f; pairs of tournaments without a common club
    scores = [(0.53, [0.87, 2.41, 5.06, 0.17, 3.38]), (3.65, [0.091, 0.462, 0.257, 0.738, 0.118]),
              (8.6, [0.0213, 0.164, 0.0587, 0.311, 0.0942])]
    weights = [([-1.37, -0.62, -2.91, -0.23], [-0.97, -1.04, -1.33, -0.47]),
               ([-3.61, -2.07, -4.83], [-2.94, -2.88, -3.17])]
    batches = [([0.7, 1.85], [0.43, -1.13]), ([1.0, 0.0, 1.0], [0.62, -0.87, 1.31]),
               ([2.35, 0.4, 1.65, 3.15, 0.9], [0.27, -0.79, 0.55, 1.42, -0.63]),
               ([1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0], [0.38, 1.27, -0.89, 0.71, -1.33, -0.52, 2.06])]
    pairs = [([[0, 3], [2, 0]], [[0, 1, 4], [2, 0, 3], [3, 1, 0]]),
             ([[0, 2, 1, 3], [1, 0, 2, 2], [3, 1, 0, 1], [2, 2, 3, 0]], [[0, 6], [5, 0]])]
    for theta, xs in scores:
        assert not_dyadic(xs) and not_dyadic([theta])
        good, bad = np.array([1 / theta - x for x in xs]), np.array([(x - theta) / theta ** 2 for x in xs])
        assert not np.allclose(good, bad) and not any(near_limit(v, 9) for v in good)
    for lp, lq in weights:
        assert not_dyadic(lp + lq)
        good, bad = np.exp(np.array(lp) - lq), np.exp(np.array(lq) - lp)
        assert not np.allclose(good, bad) and not any(near_limit(v, 9) for v in good)
    for f, s in batches:
        assert not_dyadic(s)
        f, s = np.array(f), np.array(s)
        good = float(np.mean((f - (f.sum() - f) / (len(f) - 1)) * s))
        bad = float(np.mean((f - f.mean()) * s))
        assert abs(good - bad) > 1e-6 and not near_limit(good, 9)
    for a, b in pairs:
        ref.bradley_terry_fit(a)
        ref.bradley_terry_fit(b)                         # each tournament has its strengths, the union none
    out["__CASES_C19__"] = literal({"scores": scores, "weights": weights, "batches": batches, "pairs": pairs,
                                    "id_scores": "MB8.19e", "id_weights": "MB8.19f", "id_batches": "MB8.19g"})

    # MB8.20: the hidden methods are right where they must be, wrong where they must be, and pass or fail np.allclose
    # as their clause says (on a few random MDPs, seed 8128)
    hidden = load_module(ROOT / "solutions" / "challenges" / "mb8_20.py", "mb8_20_build")
    rng = np.random.default_rng(8128)
    for m, K in ((2, 3), (4, 2), (5, 3)):
        P = rng.dirichlet(np.ones(m), size=(K, m))
        r, z, g = rng.normal(size=(K, m)), rng.normal(size=(m, K)), 0.7
        exact = ref.policy_gradient_exact(P, r, z, g)[1]
        for right in hidden.RIGHT:
            assert np.allclose(right(P, r, z, g)[1], exact, rtol=0, atol=1e-12)
        assert np.allclose(hidden.relative_8e6(P, r, z, g)[1], exact) and np.allclose(hidden.offset_large(P, r, z, g)[1],
                                                                                         exact)
        assert np.allclose(hidden.offset_sum(P, r, z, g)[1].sum(axis=2), 0)
        assert np.max(np.abs(hidden.offset_sum(P, r, z, g)[1].sum(axis=2))) > 1e-10

    # MB8.21: the notebook's case is the one of the hidden module, and the solution's function is not a copy of the
    # module's method
    challenge = load_module(ROOT / "solutions" / "challenges" / "mb8_21.py", "mb8_21_build")
    assert challenge.NOTEBOOK_CASE["family"] == "exponentielle" and challenge.NOTEBOOK_CASE["theta"] == 0.1
    assert challenge.NOTEBOOK_CASE["c"] == 18.0 and challenge.NOTEBOOK_CASE["budget"] == 10_000
    import dis

    def keys(code):                                      # the code_key of the cell of tools, on every function
        found, todo = set(), [code]
        while todo:
            c = todo.pop()
            todo += [k for k in c.co_consts if hasattr(k, "co_code")]
            if c.co_name != "<module>":
                ops = tuple((i.opname, None if "JUMP" in i.opname or i.opname == "FOR_ITER" else repr(i.argval))
                            for i in dis.get_instructions(c) if i.opname not in {"CACHE", "PUSH_NULL", "RESUME", "NOP",
                                                                                 "EXTENDED_ARG", "NOT_TAKEN"})
                found.add((ops, c.co_varnames))
        return found
    hidden_keys = keys(compile((ROOT / "solutions" / "challenges" / "mb8_21.py").read_text(encoding="utf-8"), "h", "exec"))
    solution_keys = keys(compile(MB8_21.solution, "s", "exec"))
    assert not hidden_keys & solution_keys, "the solution of MB8.21 is a copy of a function of the hidden module"
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
