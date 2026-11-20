#!/usr/bin/env python
"""Build the two notebooks of chapter MB5 from a single source (used by Claude).

    python tools/chapters/build_mb5.py
    python tools/run_all_notebooks.py chapitres/mb5_diffusion/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/mb5_diffusion/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ MB5.1 to MB5.9, 🔗 MB5.14), each answer computed in the notebook from the data of
its statement (exact fractions for the moments, the survival, the bridge, the chain of relays, the guided precisions and
the steps of the tea; SymPy for the mean field of MB5.9; math elsewhere), each wrong value computed by the error its
message names; parts A to D are the notebook exercises (MB5.16 to MB5.25), exactly as 02_exercices.md describes them.
Wrong-answer messages state a rule, never a number of the answer, the last step that gives it, nor another sub-question;
none is an error of the corrected versions of workbookIA B5.20 and B5.22 (a step of Euler in the wrong direction, the
target x_0 − ε, s drawn in [0, 1), the scale, the shifted index, a square root, the noise of the last step).

Data. The notebook exercises take the data of the paper exercises (a data cell of part A, read only), the data of their
own statements (the twelve weeks of 🔨 MB5.16, chosen by hand; the levels of 🔮 MB5.20; the two-bump laws of 🎨 MB5.22 and
🏆 MB5.25, all written as literals) and their own draws (the noise of 🔬 MB5.21, seed 7721; the noise and the large sample
of 🏆 MB5.25, seeds 7725 and 7726). Seeds 7701 to 7749 only (the tests use 7600 to 7690, the figures 7691 to 7699): 7721,
7725, 7726; 7740 to 7749 serve only the calibration of the challenge (scratchpad). Never a pair of coefficients with
a² + b² = 1 (asserted), never a coefficient in arithmetic progression presented as a schedule, never β, ᾱ, ε_θ or x̂_0.
The check cells never hold the code that solves an exercise nor a value that gives an answer without a calculation: the
expected values are recorded by the solutions as hidden sub-IDs and compared with ``wbm.check(..., computed=True)``
(the mean fields of 🔬 MB5.21 and 🏆 MB5.25 at hidden points, the guided densities of 🎨 MB5.22, the hidden bridges of
🐛 MB5.23, the two Euler distances of 🏆 MB5.25 b), computed at check time by the reference ``mymath_ref.gaussian_paths``
(the hidden mixtures and fields of 🐛 MB5.23), or given by properties (the hidden methods of 🛠️ MB5.24). The hidden part
of 🏆 MB5.25 lives in ``solutions/challenges/mb5_25.py``: the check cell runs it in another process, which draws the
hidden laws at each run, answers the field requests (and counts them) and measures the points reached only at the end,
so that no hidden law (nor a seed, nor a kind) lives in the notebook's process while the learner's function runs.
The check cells use their own data, never the test cases of tests/test_mb5_gaussian_paths.py, the examples of the
docstrings of the stub gaussian_paths, the examples of the fiche, nor the numbers of workbookIA B5 to B1 (the notes of MB5
in the syllabus and their list « Évités »).
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

CHAPTER = "MB5"
FOLDER = "chapitres/mb5_diffusion"


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
    Paper("MB5.1", "L'anomalie de température d'un lac, un processus autorégressif : sa loi sachant aujourd'hui, sa loi "
                   "stationnaire, le nombre de jours pour oublier le départ, et sa loi sachant un jour passé", [
        ("a", "a list of 2 numbers (4 decimals): the mean, then the variance of x_1", "floats(moments_1(1))",
         '''decimals=4,
           mistakes={"x_0 est connu : sa variance est 0, pas celle de la loi stationnaire": floats([moments_1(1)[0], VINF_1]),
                     "même avec un départ connu, le bruit du jour 1 ajoute sa variance": floats([moments_1(1)[0], 0]),
                     "la moyenne aussi change d'un jour à l'autre : elle est multipliée par a":
                         floats([X0_1, moments_1(1)[1]])}'''),
        ("b", "a list of 2 numbers (4 decimals): the mean, then the variance of x_3", "floats(moments_1(3))",
         '''decimals=4,
           mistakes={"x_0 est connu : la variance part de 0 et n'a pas encore atteint la variance stationnaire":
                         floats([moments_1(3)[0], VINF_1]),
                     "les bruits des premiers jours sont atténués par les jours suivants : chacun est multiplié par des a²":
                         floats([moments_1(3)[0], 3 * B_1 ** 2]),
                     "après trois jours, la moyenne est a³ x_0, pas a x_0": floats([A_1 * X0_1, moments_1(3)[1]])}'''),
        ("c", "a number (4 decimals)", "float(VINF_1)",
         '''decimals=4,
           mistakes={"la variance stationnaire est le point fixe de v = a² v + b², d'où v (1 − a²) = b²":
                         float(B_1 ** 2 / (1 + A_1 ** 2)),
                     "le point fixe de v = a² v + b² se trouve en divisant b² par 1 − a², pas en multipliant":
                         float(B_1 ** 2 * (1 - A_1 ** 2))}'''),
        ("d", "an integer", "days_1(0.1 * math.sqrt(VINF_1))",
         '''mistakes={"k est le premier jour où la moyenne est déjà sous le seuil, pas le dernier où elle est au-dessus":
                         days_1(0.1 * math.sqrt(VINF_1)) - 1,
                     "le seuil ne dépend pas du départ : c'est un dixième de la dispersion de la loi stationnaire":
                         days_1(0.1 * X0_1)}'''),
        ("e", "a list of 2 numbers (4 decimals): the mean, then the variance of x_25 given x_20", "floats(moments_1(5, X20_1))",
         '''decimals=4,
           mistakes={"sachant x_20, la variance part de 0 : elle n'a pas encore atteint la variance stationnaire":
                         floats([moments_1(5, X20_1)[0], VINF_1]),
                     "les bruits des jours 21 à 25 sont atténués par les jours qui les suivent":
                         floats([moments_1(5, X20_1)[0], 5 * B_1 ** 2]),
                     "sachant x_20, on repart de x_20 pour cinq jours, pas de x_0 pour vingt-cinq":
                         floats([A_1 ** 25 * X0_1, VINF_1 * (1 - A_1 ** 50)])}'''),
    ]),

    Paper("MB5.2", "La survie d'une ruche à six mois de risques différents : le produit exact, son logarithme, le risque "
                   "mensuel constant équivalent, et l'encadrement par deux exponentielles", [
        ("a", "a number (4 decimals)", "float(P_2)",
         '''decimals=4,
           mistakes={"survivre six mois, c'est survivre à chaque mois : un produit des 1 − h, pas 1 moins la somme des "
                     "risques": float(1 - S1_2),
                     "chaque mois a son propre risque : le produit des six 1 − h, pas (1 − la moyenne des risques)⁶":
                         float((1 - S1_2 / 6) ** 6),
                     "la probabilité de survie est un produit, pas une moyenne des 1 − h": float(1 - S1_2 / 6)}'''),
        ("b", "a number (4 decimals)", "math.log(P_2)",
         '''decimals=4,
           mistakes={"P est plus petit que 1 : son logarithme est négatif": -math.log(P_2),
                     "le logarithme est népérien": math.log10(P_2),
                     "ln P est la somme des ln(1 − h), pas −Σh": float(-S1_2)}'''),
        ("c", "a number (4 decimals)", "1 - float(P_2) ** (1 / 6)",
         '''decimals=4,
           mistakes={"le risque constant équivalent vérifie (1 − h)⁶ = P : ce n'est pas la moyenne des six risques":
                         float(S1_2 / 6),
                     "(1 − h)⁶ = P donne 1 − h = P^{1/6} : la question demande h": float(P_2) ** (1 / 6),
                     "six mois de risque h laissent (1 − h)⁶, pas 1 − 6h": float((1 - P_2) / 6)}'''),
        ("d", "a number (4 decimals)", "math.exp(-S1_2)",
         '''decimals=4,
           mistakes={"le risque cumulé est la somme des six risques, pas leur moyenne": math.exp(-S1_2 / 6),
                     "1 − h ≤ e^{−h} donne un produit d'exponentielles, e^{−Σh}, pas 1 − Σh": float(1 - S1_2)}'''),
        ("e", "a number (4 decimals)", "math.exp(-S1_2 - S2_2)",
         '''decimals=4,
           mistakes={"la borne inférieure vient de ln(1 − h) ≥ −h − h², pas −h − h²/2": math.exp(-S1_2 - S2_2 / 2),
                     "Σh² est la somme des carrés des risques, pas le carré de leur somme": math.exp(-S1_2 - S1_2 ** 2),
                     "l'exposant −Σh − Σh² est négatif : on retire la somme des carrés": math.exp(-S1_2 + S2_2)}'''),
    ]),

    Paper("MB5.3", "Un phoque balisé entre deux relevés : sa loi à une heure intermédiaire (le pont d'une marche "
                   "aléatoire), puis la corrélation de deux heures pour des scénarios aux mêmes lois", [
        ("a", "a list of 2 numbers (4 decimals): the mean, then the variance at 11 h", "floats(bridge_3(3))",
         '''decimals=4,
           mistakes={"la moyenne pondère par les variances cumulées V_s/V_T, pas par les durées":
                         floats(bridge_3(3, by_hours=True)),
                     "le poids V_s/V_T va avec la position de 16 h, et 1 − V_s/V_T avec celle de 8 h":
                         floats(bridge_3(3, swapped=True)),
                     "sachant aussi la position de 16 h, la variance devient V_s(V_T − V_s)/V_T, plus petite que V_s":
                         floats([bridge_3(3)[0], V_3[3]])}'''),
        ("b", "a list of 2 numbers (3 decimals): the hour (an integer), then the variance", "floats(widest_3())",
         '''decimals=3,
           mistakes={"la variance du pont est la plus grande où V_s est le plus proche de V_T/2, pas au milieu de la "
                     "durée": floats([12, bridge_3(4)[1]]),
                     "V_s = V_T/2 tombe entre 10 h et 11 h : compare les variances des deux heures entières voisines":
                         floats([11, bridge_3(3)[1]])}'''),
        ("c", "a number (4 decimals)", "math.sqrt(V_3[2] / V_3[5])",
         '''decimals=4,
           mistakes={"les variances cumulées ne croissent pas comme les heures : 2 par heure jusqu'à 11 h, puis 0,5":
                         math.sqrt(2 / 5),
                     "les pas de 11 h à 13 h sont indépendants des deux premiers : Cov(X_10h, X_13h) = V_2, pas V_5 − V_2":
                         float(V_3[5] - V_3[2]) / math.sqrt(V_3[2] * V_3[5])}'''),
        ("d", "a number (4 decimals)", "fresh_3()",
         '''decimals=4,
           mistakes={"Z_10h et Z_13h sont deux tirages frais, indépendants : seul U est commun aux deux heures":
                         fresh_3(common_noise=True),
                     "une corrélation est une covariance normalisée : elle reste entre −1 et 1": fresh_3(normalised=False)}'''),
    ]),

    Paper("MB5.4", "Une voix mêlée à un bruit de fond : SNR, part de variance de la voix, logit et décibels, puis la voix "
                   "retrouvée à partir d'une estimation du bruit, et l'erreur amplifiée", [
        ("a", "a number (2 decimals)", "SNR_4",
         '''decimals=2,
           mistakes={"la question porte sur l'enregistrement 1, de gains 1,2 et 0,5": A2_4 ** 2 / B2_4 ** 2,
                     "le SNR met la variance du signal au numérateur": B_4 ** 2 / A_4 ** 2}'''),
        ("b", "a number (4 decimals)", "SNR_4 / (1 + SNR_4)",
         '''decimals=4,
           mistakes={"γ est la part du signal dans la variance totale, a²/(a² + b²)": B_4 ** 2 / (A_4 ** 2 + B_4 ** 2),
                     "la question porte sur l'enregistrement 1, de gains 1,2 et 0,5": A2_4 ** 2 / (A2_4 ** 2 + B2_4 ** 2)}'''),
        ("c", "a number (4 decimals)", "math.log(SNR_4)",
         '''decimals=4,
           mistakes={"le logit est un logarithme népérien": math.log10(SNR_4),
                     "logit γ = ln(γ/(1 − γ)), pas ln γ": math.log(SNR_4 / (1 + SNR_4))}'''),
        ("d", "a number (1 decimal)", "10 * math.log10(SNR_4)",
         '''decimals=1,
           mistakes={"les décibels sont 10 log₁₀ SNR, pas 10 ln SNR": 10 * math.log(SNR_4),
                     "un décibel est un dixième de bel : on multiplie log₁₀ SNR par 10": math.log10(SNR_4)}'''),
        ("e", "a number (4 decimals)", "10 ** 0.9 / (1 + 10 ** 0.9)",
         '''decimals=4,
           mistakes={"un seuil r de SNR correspond à γ = r/(1 + r), pas 1/(1 + r)": 1 / (1 + 10 ** 0.9),
                     "9 dB ne sont pas un SNR de 9 : r se tire de 10 log₁₀ r = 9": 9 / (1 + 9),
                     "les décibels sont en base 10, pas en base e": math.exp(0.9) / (1 + math.exp(0.9))}'''),
        ("f", "a number (4 decimals)", "(Y2_4 - B2_4 * NHAT_4) / A2_4",
         '''decimals=4,
           mistakes={"on retire b n̂, le bruit multiplié par son gain": (Y2_4 - NHAT_4) / A2_4,
                     "x̂ = (y − b n̂)/a : il reste à diviser par a": Y2_4 - B2_4 * NHAT_4,
                     "on retire le bruit estimé : y − b n̂, pas y + b n̂": (Y2_4 + B2_4 * NHAT_4) / A2_4}'''),
        ("g", "a list of 2 numbers (4 decimals): recording 1, then recording 2", "[B_4 / A_4, B2_4 / A2_4]",
         '''decimals=4,
           mistakes={"retire x = (y − b n)/a de x̂ = (y − b n̂)/a : le rapport est b/a, pas a/b": [A_4 / B_4, A2_4 / B2_4],
                     "x̂ = (y − b n̂)/a : le gain b du bruit est encore divisé par a": [B_4, B2_4]}'''),
    ]),

    Paper("MB5.5", "Débruiter un signal reçu, d'abord gaussien, puis émis à deux niveaux ±c : E[x | y] par M25a et par la "
                   "formule de Tweedie, et la limite quand le bruit tend vers 0", [
        ("a", "a number (4 decimals)", "float(gaussian_5())",
         '''decimals=4,
           mistakes={"la variance de y est a² τ² + b², pas τ² + b²": float(gaussian_5(spread=TAU2_5 + B_5 ** 2)),
                     "l'écart à la moyenne de y est y − a m, pas y − m": float(gaussian_5(centre=M_5)),
                     "le gain du modèle linéaire gaussien a le facteur a au numérateur : a τ²/(a² τ² + b²)":
                         float(gaussian_5(gain=1))}'''),
        ("b", "a number (4 decimals)", "float(SCORE_5)",
         '''decimals=4,
           mistakes={"le score est négatif au-dessus de la moyenne a m : il pointe vers elle": float(-SCORE_5),
                     "la loi de y a pour moyenne a m, pas m": float(-(Y_5 - M_5) / (A_5 ** 2 * TAU2_5 + B_5 ** 2))}'''),
        ("c", "a number (4 decimals)", "float(-B_5 * SCORE_5)",
         '''decimals=4,
           mistakes={"E[n | y] = −b (ln p_Y)′(y), avec le signe moins": float(B_5 * SCORE_5),
                     "E[n | y] = (y − a E[x | y])/b, avec E[x | y], pas la moyenne a priori m":
                         float((Y_5 - A_5 * M_5) / B_5)}'''),
        ("d", "a number (4 decimals)", "two_levels_5()",
         '''decimals=4,
           mistakes={"l'argument de la tanh est a c y/b², avec le gain a": two_levels_5(gain=1),
                     "les niveaux sont ±c : E[x | y] = c tanh(…), pas tanh(…)": two_levels_5() / C_5}'''),
        ("e", "a number (4 decimals)", "(YB_5 - AB_5 * two_levels_5()) / BB_5",
         '''decimals=4,
           mistakes={"y = a x + b n : on retire a E[x | y], pas E[x | y]": (YB_5 - two_levels_5()) / BB_5,
                     "E[n | y] = (y − a E[x | y])/b, avec un signe moins": (YB_5 + AB_5 * two_levels_5()) / BB_5}'''),
        ("f", "a number (4 decimals)", "float(C_5)",
         '''decimals=4,
           mistakes={"quand b → 0, le débruiteur rend l'un des deux niveaux, ±c, pas y/a": YB_5 / AB_5,
                     "les niveaux émis sont ±c ; ±a c sont ceux de a x": AB_5 * C_5,
                     "y = 1,1 est positif : le niveau le plus plausible est celui de même signe": float(-C_5)}'''),
    ]),

    Paper("MB5.6", "Un bit altéré par deux relais, puis reconstitué par un modèle retour : ln p(x), l'ELBO de la loi aller "
                   "et sa décomposition en reconstruction, KL finale et KL d'un pas retour", [
        ("a", "a list of 2 numbers (4 decimals): q(z2 = 0 | x = 1), then q(z2 = 1 | x = 1)", "floats(Q2_6)",
         '''decimals=4,
           mistakes={"z₂ passe par z₁ : additionne sur les deux valeurs de z₁ (un produit de deux matrices)":
                         floats(FLIP_6(R2_6)[1]),
                     "la première composante est q(z₂ = 0 | x = 1)": floats(Q2_6[::-1])}'''),
        ("b", "a list of 2 numbers (4 decimals): q(z1 = 1 | z2 = 0, x = 1), then q(z1 = 1 | z2 = 1, x = 1)",
         "floats([QPOST_6[1, 0], QPOST_6[1, 1]])",
         '''decimals=4,
           mistakes={"Bayes multiplie la vraisemblance q(z₂ | z₁) par l'a priori q(z₁ | x = 1) avant de normaliser":
                         floats([FLIP_6(R2_6)[1][z2] / (FLIP_6(R2_6)[0][z2] + FLIP_6(R2_6)[1][z2]) for z2 in (0, 1)]),
                     "il reste à diviser par q(z₂ | x = 1), la somme sur z₁": floats([Q12_6[1, 0], Q12_6[1, 1]])}'''),
        ("c", "a number (4 decimals)", "math.log(PX_6)",
         '''decimals=4,
           mistakes={"p(x = 1) est une probabilité : son logarithme est négatif": -math.log(PX_6),
                     "le logarithme est népérien": math.log10(PX_6),
                     "le modèle retour part de p(z₂), pas de la loi aller q(z₂ | x)":
                         math.log(sum(Q2_6[z2] * P21_6[z2][z1] * PX1_6[z1][1] for z1 in (0, 1) for z2 in (0, 1)))}'''),
        ("d", "a number (4 decimals)", "ELBO_6",
         '''decimals=4,
           mistakes={"l'ELBO retire aussi E_q[ln q(z₁, z₂ | x)] : il manque l'entropie de q": ELBO_6 - ENTROPY_6,
                     "l'ELBO est sous ln p(x) : ln p(x) moins l'écart, pas plus": 2 * math.log(PX_6) - ELBO_6}'''),
        ("e", "a list of 3 numbers (4 decimals): the reconstruction, the final KL, the KL of the backward step",
         "terms_6()",
         '''decimals=4,
           mistakes={"la KL finale est KL(q(z₂ | x) ‖ p(z₂)), q en premier": terms_6(final_reversed=True),
                     "la KL du pas retour se moyenne sous q(z₂ | x), pas avec des poids égaux": terms_6(equal_weights=True),
                     "les logarithmes sont népériens": [t / math.log(2) for t in terms_6()]}'''),
    ]),

    Paper("MB5.7", "La date de floraison d'une variété et celle de tout le verger : la loi p_v^{1+w} p_g^{−w} pour deux "
                   "valeurs de w, son score, sa condition d'existence et le w limite", [
        ("a", "a number (4 decimals)", "float(guided_7(W1_7)[1])",
         '''decimals=4,
           mistakes={"la précision de p_v^{1+w} p_g^{−w} est (1 + w)/σ_v² − w/σ_g², avec un signe moins":
                         float(1 / ((1 + W1_7) / VV_7 + W1_7 / VG_7)),
                     "on combine les précisions 1/σ², pas les variances": float((1 + W1_7) * VV_7 - W1_7 * VG_7),
                     "la puissance 1 + w multiplie aussi la précision de p_v": float(1 / (1 / VV_7 - W1_7 / VG_7))}'''),
        ("b", "a number (4 decimals)", "float(guided_7(W1_7)[0])",
         '''decimals=4,
           mistakes={"chaque moyenne compte avec sa précision et le signe de sa puissance : − w μ_g/σ_g²":
                         float(guided_7(W1_7, sign=1)[0]),
                     "la combinaison affine (1 + w) μ_v − w μ_g oublie les précisions":
                         float((1 + W1_7) * MV_7 - W1_7 * MG_7)}'''),
        ("c", "a list of 2 numbers (4 decimals): the mean, then the variance", "floats(guided_7(W2_7))",
         '''decimals=4,
           mistakes={"la combinaison affine (1 + w) μ_v − w μ_g oublie les précisions":
                         floats([(1 + W2_7) * MV_7 - W2_7 * MG_7, guided_7(W2_7)[1]]),
                     "la précision est (1 + w)/σ_v² − w/σ_g², avec un signe moins": floats(guided_7(W2_7, sign=1))}'''),
        ("d", "a number (4 decimals)", "float((1 + W2_7) * score_7(MV_7, VV_7) - W2_7 * score_7(MG_7, VG_7))",
         '''decimals=4,
           mistakes={"le score de N(μ, σ²) est −(x − μ)/σ², avec un signe moins":
                         float(-((1 + W2_7) * score_7(MV_7, VV_7) - W2_7 * score_7(MG_7, VG_7))),
                     "le score de p_g^{−w} est −w fois celui de p_g":
                         float((1 + W2_7) * score_7(MV_7, VV_7) + W2_7 * score_7(MG_7, VG_7)),
                     "la puissance 1 + w multiplie aussi le score de p_v":
                         float(score_7(MV_7, VV_7) - W2_7 * score_7(MG_7, VG_7))}'''),
        ("e", "a number (4 decimals)", "float(VG_7 / (VL_7 - VG_7))",
         '''decimals=4,
           mistakes={"le w limite annule (1 + w)/σ_v² − w/σ_g² : σ_g² au numérateur": float(VL_7 / (VL_7 - VG_7)),
                     "(1 + w)/σ_v² = w/σ_g² donne w(σ_v² − σ_g²) = σ_g²": float(VG_7 / VL_7)}'''),
    ]),

    Paper("MB5.8", "Une tasse de thé qui refroidit : Euler et point milieu contre la solution exacte, l'erreur quand le pas "
                   "est divisé par deux, et un calcul à rebours", [
        ("a", "a number (2 decimals)", "exact_8(10)",
         '''decimals=2,
           mistakes={"la solution exacte fait décroître l'écart à la pièce, T − 20, pas la température":
                         float(T0_8) * math.exp(-float(K_8) * 10),
                     "un seul pas d'Euler n'est pas la solution exacte": float(euler_8(10, 1))}'''),
        ("b", "a list of 2 numbers (2 decimals): h = 5, then h = 2.5", "floats([euler_8(5, 2), euler_8(F(5, 2), 4)])",
         '''decimals=2,
           mistakes={"la vitesse est −k(T − 20), avec l'écart à la pièce":
                         floats([euler_8(5, 2, room=0), euler_8(F(5, 2), 4, room=0)]),
                     "la première valeur est celle des deux pas de 5 min": floats([euler_8(F(5, 2), 4), euler_8(5, 2)])}'''),
        ("c", "a list of 2 numbers (2 decimals): h = 5, then h = 2.5", "floats([midpoint_8(5, 2), midpoint_8(F(5, 2), 4)])",
         '''decimals=2,
           mistakes={"le point milieu fait d'abord un demi-pas d'Euler, h/2, puis lit la vitesse là":
                         floats([midpoint_8(5, 2, half=1), midpoint_8(F(5, 2), 4, half=1)]),
                     "la première valeur est celle des deux pas de 5 min":
                         floats([midpoint_8(F(5, 2), 4), midpoint_8(5, 2)])}'''),
        ("d", "a list of 2 numbers (1 decimal): Euler, then the midpoint method", "ratios_8()",
         '''decimals=1,
           mistakes={"le rapport divise l'erreur du grand pas par celle du petit": [1 / r for r in ratios_8()],
                     "une erreur est un écart à la valeur exacte, pas la valeur approchée":
                         [float(euler_8(5, 2) / euler_8(F(5, 2), 4)), float(midpoint_8(5, 2) / midpoint_8(F(5, 2), 4))]}'''),
        ("e", "a list of 2 numbers (2 decimals): one Euler step backward, then the exact value",
         "floats([euler_8(-5, 1, start=T10_8, t0=10), exact_8(5, start=T10_8, t0=10)])",
         '''decimals=2,
           mistakes={"la solution exacte fait décroître l'écart à la pièce, 47 − 20, pas la température":
                         floats([euler_8(-5, 1, start=T10_8, t0=10), float(T10_8) * math.exp(float(K_8) * 5)]),
                     "remonter le temps multiplie l'écart à la pièce par e^{+k Δt}":
                         floats([euler_8(-5, 1, start=T10_8, t0=10), exact_8(15, start=T10_8, t0=10)])}'''),
    ]),

    Paper("MB5.9", "Le chemin droit d'un bruit N(0, 1) vers une loi N(m, τ²) : le champ moyen, un pas d'Euler depuis s = 1, "
                   "puis deux pas, et l'écart-type obtenu contre τ", [
        ("a", "a number (4 decimals)", "float(SIGMA2_9.subs(s_9, sp.Rational(1, 2)))",
         '''decimals=4,
           mistakes={"x_s contient aussi le bruit s ε, dont la variance s'ajoute": float((1 - F(1, 2)) ** 2 * TAU_9 ** 2),
                     "x_s contient aussi la donnée (1 − s) x_0, dont la variance s'ajoute": float(F(1, 2) ** 2)}'''),
        ("b", "a number (4 decimals)", "float(FIELD_9.subs({x_9: sp.Rational(3, 2), s_9: sp.Rational(1, 2)}))",
         '''decimals=4,
           mistakes={"v = (x − E[x_0 | x_s = x])/s : il reste à diviser par s":
                         float((x_9 - POSTERIOR_9).subs({x_9: sp.Rational(3, 2), s_9: sp.Rational(1, 2)})),
                     "x_s a pour moyenne (1 − s) m : l'écart de x à la moyenne est x − (1 − s) m":
                         float(FIELD_CENTRED_AT_M_9.subs({x_9: sp.Rational(3, 2), s_9: sp.Rational(1, 2)}))}'''),
        ("c", "a number (4 decimals)", "euler_9([1, 0])",
         '''decimals=4,
           mistakes={"un seul pas va de s = 1 à s = 0 : il dure 1, pas 1/2": euler_9([1, F(1, 2)]),
                     "en s = 1, x_0 et x_s sont indépendants : E[x_0 | x_1 = x] = m, donc v(x, 1) = x − m, pas −m":
                         float(Z_9 + M_9)}'''),
        ("d", "a number (4 decimals)", "euler_9([1, F(1, 2), 0])",
         '''decimals=4,
           mistakes={"le second pas lit le champ en s = 0,5, au point où le premier pas est arrivé, pas au départ z":
                         euler_9([1, F(1, 2), 0], frozen_point=True),
                     "le second pas lit le champ à son propre instant, s = 0,5, pas en s = 1":
                         euler_9([1, F(1, 2), 0], frozen_time=True)}'''),
        ("e", "a list of 2 numbers (4 decimals): the standard deviation, then the exact point reached",
         "floats([(euler_9([1, F(1, 2), 0], z=1) - euler_9([1, F(1, 2), 0], z=0)), M_9 + TAU_9 * Z_9])",
         '''decimals=4,
           mistakes={"deux pas, pas un seul : un pas depuis s = 1 enverrait tous les départs au même point":
                         floats([0, M_9 + TAU_9 * Z_9]),
                     "z = −0,7 est négatif : le point d'arrivée exact est sous m":
                         floats([(euler_9([1, F(1, 2), 0], z=1) - euler_9([1, F(1, 2), 0], z=0)), M_9 - TAU_9 * Z_9])}'''),
    ]),

    Paper("MB5.14", "Pont : une loss de débruitage à trois niveaux de bruit, son minimiseur à chaque niveau, et les MSE "
                    "minimales sur le signal et sur le bruit", [
        ("a", "a number (4 decimals)", "float(LEVELS_14[1][1] / (LEVELS_14[1][0] ** 2 + LEVELS_14[1][1] ** 2))",
         '''decimals=4,
           mistakes={"on prédit le bruit n : c'est Cov(n, y) qui compte, pas Cov(x, y)":
                         float(LEVELS_14[1][0] / (LEVELS_14[1][0] ** 2 + LEVELS_14[1][1] ** 2)),
                     "le niveau 2 a les gains (1,1 ; 1,7)":
                         float(LEVELS_14[2][1] / (LEVELS_14[2][0] ** 2 + LEVELS_14[2][1] ** 2))}'''),
        ("b", "a list of 3 numbers (4 decimals): levels 1, 2, 3", "floats(GAMMA_14)",
         '''decimals=4,
           mistakes={"la MSE minimale est celle de E[n | y], pas celle de la prédiction 0": [1, 1, 1],
                     "connaître y réduit la MSE : on retire Cov(n, y)²/Var(y) de Var(n)":
                         floats([1 + b ** 2 / (a ** 2 + b ** 2) for a, b in LEVELS_14])}'''),
        ("c", "a list of 3 numbers (4 decimals): levels 1, 2, 3", "floats([1 - g for g in GAMMA_14])",
         '''decimals=4,
           mistakes={"la MSE minimale est celle de E[x | y], pas celle de la prédiction 0": [1, 1, 1],
                     "connaître y réduit la MSE : on retire Cov(x, y)²/Var(y) de Var(x)":
                         floats([1 + a ** 2 / (a ** 2 + b ** 2) for a, b in LEVELS_14])}'''),
        ("d", "a number (4 decimals)", "float(sum(w * g for w, g in zip(OMEGA_14, GAMMA_14)))",
         '''decimals=4,
           mistakes={"la loss moyenne pondère les MSE minimales sur le bruit, pas sur le signal":
                         float(sum(w * (1 - g) for w, g in zip(OMEGA_14, GAMMA_14))),
                     "chaque niveau compte avec sa probabilité, pas avec un poids égal": float(sum(GAMMA_14) / 3),
                     "la loss est une moyenne pondérée, pas une somme": float(sum(GAMMA_14))}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (exact fractions where the calculation is exact, SymPy for the
# mean field of MB5.9, math elsewhere)
import itertools
import math
from fractions import Fraction as F

import numpy as np
import sympy as sp


def floats(values):
    """A number or a list of numbers (fractions, SymPy) as a float or a list of floats (-0.0 written 0.0)."""
    return (np.round(np.asarray([float(v) for v in values] if isinstance(values, (list, tuple)) else float(values),
                                dtype=float), 12) + 0.0).tolist()


# MB5.1: the anomaly of a lake, x_t = 0.88 x_{t-1} + 0.35 eps_t, x_0 = 2.5; e) x_20 = -1.4
A_1, B_1, X0_1, X20_1 = F(88, 100), F(35, 100), F(5, 2), F(-7, 5)
VINF_1 = B_1 ** 2 / (1 - A_1 ** 2)


def moments_1(t, start=X0_1):
    """The mean and the variance of x_t given x_0 = start (exact): m <- a m, v <- a² v + b², t times."""
    m, v = start, F(0)
    for _ in range(t):
        m, v = A_1 * m, A_1 ** 2 * v + B_1 ** 2
    return [m, v]


def days_1(level):
    """The smallest k for which the mean a^k x_0 is under level."""
    return next(k for k in range(1000) if float(A_1) ** k * float(X0_1) < float(level))


# MB5.2: the monthly risks of a hive, October to March
H_2 = [F(1, 100), F(4, 100), F(7, 100), F(12, 100), F(10, 100), F(6, 100)]
P_2 = math.prod(1 - h for h in H_2)
S1_2, S2_2 = float(sum(H_2)), float(sum(h * h for h in H_2))

# MB5.3: a seal, hourly variances 2 (8 h to 11 h) then 0.5 (11 h to 16 h); 3 km at 8 h, 9 km at 16 h
V_3 = [F(0)] + list(itertools.accumulate([F(2)] * 3 + [F(1, 2)] * 5))   # V_3[s]: the cumulated variance s hours after 8 h
X0_3, XT_3, SIGMA2_3 = F(3), F(9), F(3, 2)


def bridge_3(s, by_hours=False, swapped=False):
    """The mean and the variance at 8 h + s hours given both positions (the bridge); by_hours: the weight s/8 instead of
    V_s/V_T; swapped: the weight on the position of 8 h."""
    Vs, VT = (F(s, 8) * V_3[8], V_3[8]) if by_hours else (V_3[s], V_3[8])
    mean = XT_3 + Vs / VT * (X0_3 - XT_3) if swapped else X0_3 + Vs / VT * (XT_3 - X0_3)
    return [mean, Vs * (VT - Vs) / VT]


def widest_3():
    """The whole hour from 9 h to 15 h where the variance of the bridge is the largest, and that variance."""
    s = max(range(1, 8), key=lambda h: bridge_3(h)[1])
    return [8 + s, bridge_3(s)[1]]


def fresh_3(common_noise=False, normalised=True):
    """The correlation of the positions at 10 h and 13 h with a fresh noise of variance 1.5 (common_noise: the same Z at
    both hours; normalised=False: the covariance alone)."""
    v10, v13 = V_3[2], V_3[5]
    cov = math.sqrt((v10 - SIGMA2_3) * (v13 - SIGMA2_3)) + (float(SIGMA2_3) if common_noise else 0)
    return cov / math.sqrt(v10 * v13) if normalised else cov


# MB5.4: a voice and a noise, y = 1.2 x + 0.5 n (recording 1) and y = 0.3 x + 1.8 n (recording 2); y = 0.9, n̂ = 0.7
A_4, B_4, A2_4, B2_4, Y2_4, NHAT_4 = 1.2, 0.5, 0.3, 1.8, 0.9, 0.7
SNR_4 = A_4 ** 2 / B_4 ** 2

# MB5.5: A, x ~ N(1, 4), y = 2x + 3n, y = 6; B, x = ±2 (1/2 each), y = 0.5 x + n, y = 1.1
M_5, TAU2_5, A_5, B_5, Y_5 = F(1), F(4), F(2), F(3), F(6)
C_5, AB_5, BB_5, YB_5 = 2, 0.5, 1.0, 1.1
SCORE_5 = -(Y_5 - A_5 * M_5) / (A_5 ** 2 * TAU2_5 + B_5 ** 2)       # the score of the law N(a m, a² tau² + b²) of y


def gaussian_5(spread=None, centre=None, gain=None):
    """E[x | y] by the linear Gaussian model (M25a), m + a tau² (y − a m)/(a² tau² + b²); the arguments change one piece."""
    spread = A_5 ** 2 * TAU2_5 + B_5 ** 2 if spread is None else spread
    centre = A_5 * M_5 if centre is None else centre
    gain = A_5 if gain is None else gain
    return M_5 + gain * TAU2_5 * (Y_5 - centre) / spread


def two_levels_5(gain=AB_5):
    """E[x | y] for x = ±c, equally likely: c tanh(a c y / b²)."""
    return C_5 * math.tanh(gain * C_5 * YB_5 / BB_5 ** 2)


# MB5.6: a bit through two relays (flips 0.22 and 0.4); the backward model p(z2 = 1) = 0.3, flips 0.16 and 0.32; x = 1
R1_6, R2_6, PZ2_6, R21_6, RX1_6 = F(22, 100), F(4, 10), F(3, 10), F(16, 100), F(32, 100)


def FLIP_6(r):
    """The 2 x 2 table of a relay that flips with the probability r (rows: the input)."""
    return [[1 - r, r], [r, 1 - r]]


Q1_6 = FLIP_6(R1_6)[1]                                                   # q(z1 | x = 1)
Q12_6 = {(z1, z2): Q1_6[z1] * FLIP_6(R2_6)[z1][z2] for z1 in (0, 1) for z2 in (0, 1)}
Q2_6 = [Q12_6[0, z2] + Q12_6[1, z2] for z2 in (0, 1)]                    # q(z2 | x = 1)
QPOST_6 = {(z1, z2): Q12_6[z1, z2] / Q2_6[z2] for z1 in (0, 1) for z2 in (0, 1)}   # q(z1 | z2, x = 1), Bayes
PZ_6 = [1 - PZ2_6, PZ2_6]
P21_6, PX1_6 = FLIP_6(R21_6), FLIP_6(RX1_6)                              # p(z1 | z2), p(x | z1)
JOINT_6 = {(z1, z2): PZ_6[z2] * P21_6[z2][z1] * PX1_6[z1][1] for z1 in (0, 1) for z2 in (0, 1)}
PX_6 = sum(JOINT_6.values())
ELBO_6 = sum(float(Q12_6[k]) * (math.log(JOINT_6[k]) - math.log(Q12_6[k])) for k in Q12_6)
ENTROPY_6 = -sum(float(Q12_6[k]) * math.log(Q12_6[k]) for k in Q12_6)


def terms_6(final_reversed=False, equal_weights=False):
    """The reconstruction, the final KL and the KL of the backward step averaged under q(z2 | x)."""
    reconstruction = sum(float(Q1_6[z1]) * math.log(PX1_6[z1][1]) for z1 in (0, 1))
    if final_reversed:
        final = sum(float(PZ_6[z]) * math.log(PZ_6[z] / Q2_6[z]) for z in (0, 1))
    else:
        final = sum(float(Q2_6[z]) * math.log(Q2_6[z] / PZ_6[z]) for z in (0, 1))
    step = sum((0.5 if equal_weights else float(Q2_6[z2]))
               * sum(float(QPOST_6[z1, z2]) * math.log(QPOST_6[z1, z2] / P21_6[z2][z1]) for z1 in (0, 1))
               for z2 in (0, 1))
    return [reconstruction, final, step]


# MB5.7: flowering dates, a variety N(102, 25) and the orchard N(108, 81); w = 0.4 and 1.25; a late variety N(115, 144)
MV_7, VV_7, MG_7, VG_7, VL_7, W1_7, W2_7 = 102, 25, 108, 81, 144, F(2, 5), F(5, 4)


def guided_7(w, sign=-1):
    """The mean and the variance of the law proportional to p_v^(1+w) p_g^(−w): precision (1 + w)/v_v − w/v_g (sign=1:
    the sign of the second term changed)."""
    precision = (1 + w) / F(VV_7) + sign * w / F(VG_7)
    return [((1 + w) * MV_7 / F(VV_7) + sign * w * MG_7 / F(VG_7)) / precision, 1 / precision]


def score_7(mean, variance, x=96):
    """The score of N(mean, variance) at x."""
    return -F(x - mean, variance)


# MB5.8: a cup of tea, T' = −0.06 (T − 20), T(0) = 85; e) 47 °C at 10 min, back to 5 min
K_8, ROOM_8, T0_8, T10_8 = F(6, 100), F(20), F(85), F(47)


def exact_8(t, start=T0_8, t0=0):
    """The exact temperature at t: 20 + (start − 20) e^{−k (t − t0)}."""
    return float(ROOM_8) + float(start - ROOM_8) * math.exp(-float(K_8) * (t - t0))


def euler_8(h, n, start=T0_8, t0=0, room=ROOM_8):
    """n Euler steps of length h (exact fractions); room=0: the velocity −k T (the classic error)."""
    T = start
    for _ in range(n):
        T = T - F(h) * K_8 * (T - room)
    return T


def midpoint_8(h, n, start=T0_8, half=F(1, 2)):
    """n midpoint steps of length h (exact fractions); half=1: the first half step made with the whole step."""
    T = start
    for _ in range(n):
        middle = T - half * F(h) * K_8 * (T - ROOM_8)
        T = T - F(h) * K_8 * (middle - ROOM_8)
    return T


def ratios_8():
    """The ratio of the error with h = 5 to the error with h = 2.5, for Euler, then for the midpoint method."""
    exact = exact_8(10)
    return [(exact - float(euler_8(5, 2))) / (exact - float(euler_8(F(5, 2), 4))),
            (exact - float(midpoint_8(5, 2))) / (exact - float(midpoint_8(F(5, 2), 4)))]


# MB5.9: the straight path to N(4, 0.25) (m = 4, tau = 0.5); z = −0.7
M_9, TAU_9, Z_9 = sp.Rational(4), sp.Rational(1, 2), sp.Rational(-7, 10)
x_9, s_9 = sp.symbols("x s", real=True)
SIGMA2_9 = (1 - s_9) ** 2 * TAU_9 ** 2 + s_9 ** 2                         # the variance of x_s
POSTERIOR_9 = M_9 + (1 - s_9) * TAU_9 ** 2 * (x_9 - (1 - s_9) * M_9) / SIGMA2_9   # E[x_0 | x_s = x], M25a
FIELD_9 = (x_9 - POSTERIOR_9) / s_9                                        # the mean field v(x, s)
FIELD_CENTRED_AT_M_9 = (x_9 - (M_9 + (1 - s_9) * TAU_9 ** 2 * (x_9 - M_9) / SIGMA2_9)) / s_9   # x − m, not x − (1 − s) m


def euler_9(times, z=Z_9, frozen_point=False, frozen_time=False):
    """Euler's method on x' = v(x, s) through the times given (from s = 1), from z (exact); frozen_point: the field read
    at z; frozen_time: the field read at s = 1."""
    x = sp.Rational(z)
    for s0, s1 in zip(times[:-1], times[1:]):
        where = {x_9: sp.Rational(z) if frozen_point else x, s_9: 1 if frozen_time else sp.Rational(s0)}
        x = x + (sp.Rational(s1) - sp.Rational(s0)) * FIELD_9.subs(where)
    return float(x)


# MB5.14: x ~ N(0, 1) measured at three levels (a, b), drawn with the probabilities 0.5, 0.3, 0.2
LEVELS_14 = [(F(11, 5), F(1)), (F(11, 10), F(17, 10)), (F(1, 2), F(5, 2))]
OMEGA_14 = [F(1, 2), F(3, 10), F(1, 5)]
GAMMA_14 = [a ** 2 / (a ** 2 + b ** 2) for a, b in LEVELS_14]          # the minimal MSE on the noise, level by level'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ MB5.1 à MB5.9 ; 🔗 MB5.14)\n\n"
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
# Notebook exercises: your library (MB5.16 to MB5.18)
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

TEST_MB5 = "tests/test_mb5_gaussian_paths.py"          # the tests of mymath/gaussian_paths.py
REF = wbm.load_mymath("ref", alias="mymath_ref")       # the reference: the checks of the hidden cases rely on it
ref_gp = REF.gaussian_paths


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


def matches(got, want, rtol=1e-9, atol=1e-12):
    """True when got is an array of numbers of the shape of want and equal to it up to rounding (no error for an odd
    got)."""
    arr = as_floats(got)
    want = np.asarray(want, dtype=float)
    return arr is not None and arr.shape == want.shape and bool(np.allclose(arr, want, rtol=rtol, atol=atol,
                                                                            equal_nan=True))


def line_with(ax, xs, ys, rtol=1e-7, atol=1e-9):
    """The first line of ax that has exactly the abscissas xs and the ordinates ys, or None."""
    xs, ys = np.asarray(xs, dtype=float), np.asarray(ys, dtype=float)
    for line in ax.lines:
        x, y = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
        if x.shape == xs.shape and y.shape == ys.shape and np.allclose(x, xs, rtol=rtol, atol=atol) \\
                and np.allclose(y, ys, rtol=rtol, atol=atol, equal_nan=True):
            return line
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
    """The code_key of every function of a Python file, compiled but not run (to recognise a copy of its code)."""
    keys, todo = set(), [compile(open(path, encoding="utf-8").read(), str(path), "exec")]
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
    stops the block; yields the list of the names seen ("gaussian_paths.euler_ode"). The learner's function must not run
    that code (mymath in a corrected function, the hidden module of a challenge). With escapes, opening a file of places
    or starting another process also stops it ("ouvre mb5_25.py", "lance un autre processus : subprocess.Popen").
    Without sys.monitoring (Python < 3.12) or a free tool id, code is not watched."""
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
LAKE_1 = MappingProxyType({"a": 0.88, "b": 0.35, "x0": 2.5})       # MB5.1: x_t = a x_{t-1} + b eps_t, x_0 known (°C)
SEAL_3 = MappingProxyType({"x8h": 3.0, "x16h": 9.0, "var_8h_11h": 2.0, "var_11h_16h": 0.5})   # MB5.3: positions (km)
#   at 8 h and 16 h, and the variance (km²) that each hour adds, from 8 h to 11 h, then from 11 h to 16 h
SIGNAL_5A = MappingProxyType({"m": 1.0, "v": 4.0, "a": 2.0, "b": 3.0, "y": 6.0})   # MB5.5 A: x ~ N(m, v), y = a x + b n
SIGNAL_5B = MappingProxyType({"c": 2.0, "a": 0.5, "b": 1.0, "y": 1.1})   # MB5.5 B: x = +c or -c (1/2 each), y = a x + b n
TEA_8 = MappingProxyType({"k": 0.06, "room": 20.0, "T0": 85.0, "T10": 47.0})   # MB5.8: T' = -k (T - room), T(0) = T0
#   (°C, minutes); e) another cup at T10 at 10 min
DATA_9 = MappingProxyType({"m": 4.0, "tau": 0.5})                      # MB5.9: the data x_0 ~ N(m, tau²)'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="MB5")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en MB4). Ouvre ta copie `mon_travail/mymath/gaussian_paths.py`, lis la "
         "docstring du module (ses conventions, et ce qui est permis) puis celle de la fonction, remplace chaque "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Dans le notebook, appelle tes fonctions par "
         "`mymath.gaussian_paths.<nom>` (par exemple `mymath.gaussian_paths.euler_ode(f, 1.0, 0.0, 2.0, 4)`), ou "
         "donne-leur un nom court (`euler_ode = mymath.gaussian_paths.euler_ode`) dans une cellule exécutée après le "
         "rechargement. ⚠️ Le squelette n'importe rien : ajoute en tête du fichier `import math` et "
         "`import numpy as np`, et `from .approx import logsumexp` si tu reprends ton log-sum-exp de M05a. NumPy et "
         "`math` sont permis, mais aucune SciPy (`solve_ivp`, `odeint`, `quad`, `norm`, `logsumexp`, `softmax`) : les "
         "tests comparent tes résultats à SciPy et à des simulations, et un test lit ton module. Ne modifie jamais les "
         "tableaux reçus. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy.")

REMINDER = ("> Même mode d'emploi qu'en MB5.16 : écris les fonctions dans ta copie `mon_travail/mymath/gaussian_paths.py`, "
            "**enregistre**, puis exécute les cellules ci-dessous ; la première recharge ta librairie.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of gaussian_paths.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("todo", f'run_pytest_group(TEST_MB5, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_MB5, "{keyword}", impl="ref")')]


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
    functions it writes after its title (« · `euler_ode`, `midpoint_ode` »)."""
    kind, stars, minutes, title, tracks = syllabus_entry(ex_id)
    if functions:
        title = f"{title} · {functions}"
    return Ex(ex_id, kind, stars, minutes, title, goal, prereq, body=body, tracks=tracks, **fields)


# ---------------------------------------------------------------------------
# MB5.16 · linear_gaussian_recursion
# ---------------------------------------------------------------------------
GIVEN_16 = '''# Spring: the coefficients of twelve weeks (the persistence a_t and the noise b_t change every week)
A_16 = frozen(__A_16__)
B_16 = frozen(__B_16__)'''

NOTE_16 = (r"Les contrôles, puis deux listes qui démarrent à `mean0` et `var0`, et à chaque pas `m = a_t * m` et "
           r"`v = a_t ** 2 * v + b_t ** 2`. a) $(1{,}703680 ;\ 0{,}290827)$, comme MB5.1 b). b) $(0{,}205032 ;\ "
           r"0{,}593080)$. c) $(0{,}696570 ;\ 2{,}463696 ;\ 2{,}512458)$ : les moyennes $5 ;\ -3{,}6 ;\ 2{,}592 ;\ "
           r"\ldots$ changent de signe à chaque pas, et la variance approche $v_\infty$ par en dessous.")

MB5_16 = ex(
    "MB5.16", "programmer la propagation de la moyenne et de la variance d'une récurrence linéaire gaussienne, puis "
    "retrouver MB5.1 et suivre des coefficients qui changent à chaque pas, ou négatifs.",
    "fiche §1 ; M25a (image affine d'une gaussienne), R5 (suite géométrique) ; Ex MB5.1",
    functions="`linear_gaussian_recursion`", mymath="gaussian_paths.py", note=NOTE_16, given=GIVEN_16,
    body=HOWTO + r"""

Écris `linear_gaussian_recursion(a, b, mean0=0.0, var0=0.0)` (fiche §1), en suivant sa docstring : contrôle les arguments (deux tableaux 1-D de même longueur, de nombres finis ; `mean0` et `var0` réels finis, ni booléens, `var0` $\ge 0$), puis propage $m_t = a_tm_{t-1}$ et $v_t = a_t^2v_{t-1} + b_t^2$, et rends les deux tableaux de longueur $T + 1$ (l'entrée 0 est celle de $x_0$). Lance le groupe de tests.

**L'usage.** Avec ta fonction :
- a) le lac de MB5.1 (`LAKE_1`, cellule de données) sur trois jours : la moyenne et la variance de $x_3$ (une liste de 2 nombres, à comparer à ta copie) ;
- b) au printemps, la persistance et le bruit changent chaque semaine : le notebook fournit `A_16` et `B_16`, les coefficients de douze semaines, et le départ suit $x_0 \sim \mathcal{N}(1{,}5 ;\ 0{,}3)$ : la moyenne et la variance de $x_{12}$ (une liste de 2 nombres) ;
- c) $a = -0{,}72$ et $b = 1{,}1$ pendant six pas, depuis $x_0 = 5$ connu : la moyenne et la variance de $x_6$, puis $v_\infty$ (une liste de 3 nombres).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `linear_gaussian_recursion` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui "
                  "était attendu).")]
    + tests_cells("test_linear_gaussian_recursion_ or test_module_uses_") + [
        ("md", "**L'usage** : le lac de MB5.1, douze semaines de printemps, puis un coefficient négatif."),
        ("todo", '''answer_MB5_16a = answer_MB5_16b = answer_MB5_16c = ...
with wbm.attempt("MB5.16"):          # if you call linear_gaussian_recursion here: ⏳ while it is not written
    answer_MB5_16a = ...  # a) a list of 2 numbers, as computed: the mean and the variance of x_3 (the lake of MB5.1)
    answer_MB5_16b = ...  # b) a list of 2 numbers, as computed: the mean and the variance of x_12 (A_16, B_16, the start)
    answer_MB5_16c = ...  # c) a list of 3 numbers, as computed: the mean and the variance of x_6, then v_inf'''),
        ("check", answers_check("MB5.16", "abc")),
        ("solution", '''linear_gaussian_recursion = mymath.gaussian_paths.linear_gaussian_recursion
means_16, variances_16 = linear_gaussian_recursion([LAKE_1["a"]] * 3, [LAKE_1["b"]] * 3, mean0=LAKE_1["x0"])
answer_MB5_16a = [float(means_16[3]), float(variances_16[3])]
means_16, variances_16 = linear_gaussian_recursion(A_16, B_16, mean0=1.5, var0=0.3)
answer_MB5_16b = [float(means_16[-1]), float(variances_16[-1])]
means_16, variances_16 = linear_gaussian_recursion([-0.72] * 6, [1.1] * 6, mean0=5.0)
answer_MB5_16c = [float(means_16[6]), float(variances_16[6]), 1.1 ** 2 / (1 - 0.72 ** 2)]
print("a)", np.round(answer_MB5_16a, 6).tolist(), " b)", np.round(answer_MB5_16b, 6).tolist(),
      " c)", np.round(answer_MB5_16c, 6).tolist())
print("   c) les moyennes :", np.round(means_16, 6).tolist())
print("   c) les variances :", np.round(variances_16, 6).tolist())'''),
        ("record", '''from fractions import Fraction as F_16r


def moments_16r(a, b, mean0, var0=0):
    """The oracle: the recursion of the two moments in exact fractions (each coefficient read from its decimal
    writing)."""
    m, v = F_16r(str(mean0)), F_16r(str(var0))
    for at, bt in zip(a, b):
        at, bt = F_16r(str(at)), F_16r(str(bt))
        m, v = at * m, at * at * v + bt * bt
    return [float(m), float(v)]


wbm.record("MB5.16a", moments_16r([0.88] * 3, [0.35] * 3, 2.5), decimals=6,
           mistakes={"le départ connu x_0 = 2,5 se passe par mean0 (sinon, mean0 vaut 0)":
                         moments_16r([0.88] * 3, [0.35] * 3, 0)})
weeks_a_16r, weeks_b_16r = __A_16__, __B_16__
wbm.record("MB5.16b", moments_16r(weeks_a_16r, weeks_b_16r, 1.5, 0.3), decimals=6,
           mistakes={"le départ n'est pas connu : sa variance 0,3 se transmet, passe var0=0.3":
                         moments_16r(weeks_a_16r, weeks_b_16r, 1.5, 0),
                     "le départ a la moyenne 1,5 : passe mean0=1.5": moments_16r(weeks_a_16r, weeks_b_16r, 0, 0.3)})
six_16r = moments_16r([-0.72] * 6, [1.1] * 6, 5)
limit_16r = float(F_16r("1.1") ** 2 / (1 - F_16r("0.72") ** 2))
wbm.record("MB5.16c", six_16r + [limit_16r], decimals=6,
           mistakes={"la variance stationnaire est le point fixe de v = a² v + b², d'où v (1 − a²) = b²":
                         six_16r + [float(F_16r("1.1") ** 2 / (1 + F_16r("0.72") ** 2))],
                     "le départ connu x_0 = 5 se passe par mean0 (sinon, mean0 vaut 0)":
                         moments_16r([-0.72] * 6, [1.1] * 6, 0) + [limit_16r]})'''),
        ("solution", answers_check("MB5.16", "abc")),
        look("pourquoi les moyennes de c) changent-elles de signe à chaque pas, et de combien leur valeur absolue "
             "diminue-t-elle ? Par quel côté la variance approche-t-elle $v_\\infty$ ?"),
    ],
)
