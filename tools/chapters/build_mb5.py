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
(the hidden mixtures and fields of 🐛 MB5.23), or given by properties (the hidden methods of 🛠️ MB5.24, whose two right
ones live in ``solutions/challenges/mb5_24.py`` so that no cell shows a solution of 🔨 MB5.18). The hidden part
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
                         floats([bridge_3(3)[0], V_3[3]]),
                     "le pont avance au rythme des variances cumulées V_s/V_T, pas du temps s/T : les heures de chasse "
                     "comptent plus": floats([bridge_3(3, by_hours=True)[0], bridge_3(3)[1]])}'''),
        ("b", "a list of 2 numbers (3 decimals): the hour (an integer), then the variance", "floats(widest_3())",
         '''decimals=3,
           mistakes={"la variance du pont est la plus grande où V_s est le plus proche de V_T/2, pas au milieu de la "
                     "durée": floats([12, bridge_3(4)[1]]),
                     "calcule V_s(V_T − V_s)/V_T à chaque heure entière : le maximum n'est pas forcément à la première "
                     "heure où V_s dépasse V_T/2": floats([11, bridge_3(3)[1]])}'''),
        ("c", "a number (4 decimals)", "math.sqrt(V_3[2] / V_3[5])",
         '''decimals=4,
           mistakes={"les scénarios partent de 8 h sans connaître le relevé de 16 h : ce n'est pas le pont":
                         math.sqrt(float(V_3[2] * (V_3[8] - V_3[5]) / (V_3[5] * (V_3[8] - V_3[2])))),
                     "les pas de 10 h à 13 h sont indépendants des deux premiers : Cov(X_10h, X_13h) est la variance "
                     "cumulée à 10 h, pas celle des pas de 10 h à 13 h":
                         float(V_3[5] - V_3[2]) / math.sqrt(V_3[2] * V_3[5]),
                     "une corrélation 1 est celle d'un seul tirage ; la marche ajoute un déplacement frais chaque heure": 1.0}'''),
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
                     "les décibels sont en base 10, pas en base e": math.exp(0.9) / (1 + math.exp(0.9)),
                     "c'est le seuil r de SNR : e) demande la part γ qui lui correspond": 10 ** 0.9}'''),
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
                         float(gaussian_5(gain=1)),
                     "y/a ne tient compte ni de la loi de x ni du bruit : le débruiteur ramène vers la moyenne":
                         float(Y_5 / A_5)}'''),
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
                     "il reste à diviser par q(z₂ | x = 1), la somme sur z₁": floats([Q12_6[1, 0], Q12_6[1, 1]]),
                     "q(z₁ = 1 | x = 1) ignore z₂ : le pas retour qui connaît x conditionne aussi sur z₂ (Bayes)":
                         floats([Q1_6[1]] * 2)}'''),
        ("c", "a number (4 decimals)", "math.log(PX_6)",
         '''decimals=4,
           mistakes={"p(x = 1) est une probabilité : son logarithme est négatif": -math.log(PX_6),
                     "le logarithme est népérien": math.log10(PX_6),
                     "le modèle retour part de p(z₂), pas de la loi aller q(z₂ | x)":
                         math.log(sum(Q2_6[z2] * P21_6[z2][z1] * PX1_6[z1][1] for z1 in (0, 1) for z2 in (0, 1)))}'''),
        ("d", "a number (4 decimals): by its decomposition, the reconstruction minus the two KL of e)", "ELBO_6",
         '''decimals=4,
           mistakes={"l'ELBO retire les deux KL de la reconstruction, elle ne les ajoute pas":
                         terms_6()[0] + terms_6()[1] + terms_6()[2],
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
                     "la puissance 1 + w multiplie aussi la précision de p_v": float(1 / (1 / VV_7 - W1_7 / VG_7)),
                     "c'est la précision λ(w) : a) demande la variance 1/λ(w)": float(1 / guided_7(W1_7)[1])}'''),
        ("b", "a number (4 decimals)", "float(guided_7(W1_7)[0])",
         '''decimals=4,
           mistakes={"chaque moyenne compte avec sa précision et le signe de sa puissance : − w μ_g/σ_g²":
                         float(guided_7(W1_7, sign=1)[0]),
                     "la combinaison affine (1 + w) μ_v − w μ_g oublie les précisions":
                         float((1 + W1_7) * MV_7 - W1_7 * MG_7),
                     "pour w > 0, la moyenne est poussée à l'opposé de μ_g = 108": float(2 * MV_7 - guided_7(W1_7)[0])}'''),
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
           mistakes={"la vitesse est −r(T − 20), avec l'écart à la pièce":
                         floats([euler_8(5, 2, room=0), euler_8(F(5, 2), 4, room=0)]),
                     "la première valeur est celle des deux pas de 5 min": floats([euler_8(F(5, 2), 4), euler_8(5, 2)])}'''),
        ("c", "a list of 2 numbers (2 decimals): h = 5, then h = 2.5", "floats([midpoint_8(5, 2), midpoint_8(F(5, 2), 4)])",
         '''decimals=2,
           mistakes={"le point milieu fait d'abord un demi-pas d'Euler, h/2, puis lit la vitesse là":
                         floats([midpoint_8(5, 2, half=1), midpoint_8(F(5, 2), 4, half=1)]),
                     "la première valeur est celle des deux pas de 5 min":
                         floats([midpoint_8(F(5, 2), 4), midpoint_8(5, 2)])}'''),
        ("d", "a list of 2 numbers (1 decimal): Euler, then the midpoint method, from the unrounded values of a), b), c)",
         "ratios_8()",
         '''decimals=1,
           mistakes={"le rapport divise l'erreur du grand pas par celle du petit": [1 / r for r in ratios_8()],
                     "une erreur est un écart à la valeur exacte, pas la valeur approchée":
                         [float(euler_8(5, 2) / euler_8(F(5, 2), 4)), float(midpoint_8(5, 2) / midpoint_8(F(5, 2), 4))],
                     "les erreurs se calculent avec les températures non arrondies : à 2 décimales, celle du point milieu "
                     "perd presque toute sa précision": ratios_8(rounded=True),
                     "ce sont les rapports de la théorie : d) demande ceux que donnent tes valeurs de a), b) et c)":
                         [2.0, 4.0]}'''),
        ("e", "a list of 2 numbers (2 decimals): one Euler step backward, then the exact value",
         "floats([euler_8(-5, 1, start=T10_8, t0=10), exact_8(5, start=T10_8, t0=10)])",
         '''decimals=2,
           mistakes={"la solution exacte fait décroître l'écart à la pièce, 47 − 20, pas la température":
                         floats([euler_8(-5, 1, start=T10_8, t0=10), float(T10_8) * math.exp(float(K_8) * 5)]),
                     "un seul pas d'Euler n'est pas la valeur exacte": floats([euler_8(-5, 1, start=T10_8, t0=10)] * 2)}'''),
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
                         float(Z_9 + M_9),
                     "c'est le point d'arrivée exact de la trajectoire : c) demande un seul pas d'Euler, h = −1":
                         float(M_9 + TAU_9 * Z_9)}'''),
        ("d", "a number (4 decimals)", "euler_9([1, F(1, 2), 0])",
         '''decimals=4,
           mistakes={"le second pas lit le champ en s = 0,5, au point où le premier pas est arrivé, pas au départ z":
                         euler_9([1, F(1, 2), 0], frozen_point=True),
                     "le second pas lit le champ à son propre instant, s = 0,5, pas en s = 1":
                         euler_9([1, F(1, 2), 0], frozen_time=True),
                     "c'est le point d'arrivée exact de la trajectoire : d) demande deux pas d'Euler": float(M_9 + TAU_9 * Z_9)}'''),
        ("e", "a list of 2 numbers (4 decimals): the standard deviation, then the exact point reached",
         "floats([(euler_9([1, F(1, 2), 0], z=1) - euler_9([1, F(1, 2), 0], z=0)), M_9 + TAU_9 * Z_9])",
         '''decimals=4,
           mistakes={"deux pas, pas un seul : un pas depuis s = 1 enverrait tous les départs au même point":
                         floats([0, M_9 + TAU_9 * Z_9]),
                     "z = −0,7 est négatif : le point d'arrivée exact est sous m":
                         floats([(euler_9([1, F(1, 2), 0], z=1) - euler_9([1, F(1, 2), 0], z=0)), M_9 - TAU_9 * Z_9]),
                     "τ = 0,5 est la dispersion de la cible : e) demande celle de la loi obtenue en deux pas":
                         floats([TAU_9, M_9 + TAU_9 * Z_9])}'''),
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
H_2 = [F(1, 100), F(3, 100), F(7, 100), F(12, 100), F(14, 100), F(7, 100)]
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
    """The exact temperature at t: 20 + (start − 20) e^{−r (t − t0)}, with the rate r = K_8."""
    return float(ROOM_8) + float(start - ROOM_8) * math.exp(-float(K_8) * (t - t0))


def euler_8(h, n, start=T0_8, t0=0, room=ROOM_8):
    """n Euler steps of length h (exact fractions); room=0: the velocity −r T (the classic error)."""
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


def ratios_8(rounded=False):
    """The ratio of the error with h = 5 to the error with h = 2.5, for Euler, then for the midpoint method; rounded: from
    the temperatures rounded to 2 decimals, and the ratios rounded to 1 decimal, as the learner types them (unrounded,
    the ratio of the midpoint method would fall within the tolerance of the right one)."""
    temp = (lambda value: round(float(value), 2)) if rounded else float
    exact = temp(exact_8(10))
    ratios = [(exact - temp(euler_8(5, 2))) / (exact - temp(euler_8(F(5, 2), 4))),
              (exact - temp(midpoint_8(5, 2))) / (exact - temp(midpoint_8(F(5, 2), 4)))]
    return [round(r, 1) for r in ratios] if rounded else ratios


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
from wbm.nbtools import StopCheck, checked, drawn, filled, fr, refuse_peeking, run_pytest_group, verdict

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


def library_hint(names):
    """A hint for a wrong answer computed with the learner's library (no classic error recognised): its tests first,
    then the call."""
    return lambda value: (f"cette valeur vient de {names} de ta librairie : si ses tests passent tous (plus haut), "
                          "l'erreur est dans l'appel (les arguments, leur ordre, leurs unités ; quel pas tu lis) ; et "
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
TEA_8 = MappingProxyType({"r": 0.06, "room": 20.0, "T0": 85.0, "T10": 47.0})   # MB5.8: T' = -r (T - room), T(0) = T0
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


HINTS_16 = {letter: 'library_hint("linear_gaussian_recursion")' for letter in "abc"}
HINTS_17 = {letter: 'library_hint("posterior_mean_mixture")' for letter in "abc"}
HINTS_18 = {letter: 'library_hint("euler_ode et midpoint_ode")' for letter in "abcd"}
HINTS_19 = {letter: 'library_hint("euler_ode et midpoint_ode")' for letter in "bc"}
HINTS_20 = {letter: 'library_hint("posterior_mean_mixture")' for letter in "def"}


# ---------------------------------------------------------------------------
# MB5.16 · linear_gaussian_recursion
# ---------------------------------------------------------------------------
GIVEN_16 = '''# Spring: the coefficients of twelve weeks (the persistence a_t and the noise b_t change every week)
A_16 = frozen(__A_16__)
B_16 = frozen(__B_16__)'''

NOTE_16 = (r"Les contrôles, puis deux listes qui démarrent à `mean0` et `var0`, et à chaque pas `m = a_t * m` et "
           r"`v = a_t ** 2 * v + b_t ** 2`. a) $(1{,}703680 ;\ 0{,}290827)$, comme MB5.1 b). b) $(0{,}200712 ;\ "
           r"0{,}682062)$. c) $(-0{,}336149 ;\ 2{,}240571 ;\ 2{,}250744)$, après sept pas : les moyennes $5 ;\ -3{,}4 ;\ "
           r"2{,}312 ;\ \ldots$ changent de signe à chaque pas, si bien qu'après un nombre impair de pas la moyenne est "
           r"négative, et la variance approche $v_\infty$ par en dessous.")

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
- c) $a = -0{,}68$ et $b = 1{,}1$ pendant sept pas, depuis $x_0 = 5$ connu : la moyenne et la variance de $x_7$, puis $v_\infty$ (une liste de 3 nombres).""",
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
    answer_MB5_16c = ...  # c) a list of 3 numbers, as computed: the mean and the variance of x_7, then v_inf'''),
        ("check", answers_check("MB5.16", "abc", hints=HINTS_16)),
        ("solution", '''linear_gaussian_recursion = mymath.gaussian_paths.linear_gaussian_recursion
means_16, variances_16 = linear_gaussian_recursion([LAKE_1["a"]] * 3, [LAKE_1["b"]] * 3, mean0=LAKE_1["x0"])
answer_MB5_16a = [float(means_16[3]), float(variances_16[3])]
means_16, variances_16 = linear_gaussian_recursion(A_16, B_16, mean0=1.5, var0=0.3)
answer_MB5_16b = [float(means_16[-1]), float(variances_16[-1])]
means_16, variances_16 = linear_gaussian_recursion([-0.68] * 7, [1.1] * 7, mean0=5.0)
answer_MB5_16c = [float(means_16[7]), float(variances_16[7]), 1.1 ** 2 / (1 - 0.68 ** 2)]
print("a)", np.round(answer_MB5_16a, 6).tolist(), " b)", np.round(answer_MB5_16b, 6).tolist(),
      " c)", np.round(answer_MB5_16c, 6).tolist())
print("   c) les trois premières moyennes :", np.round(means_16[:3], 6).tolist())
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
wbm.record("MB5.16b", moments_16r(weeks_a_16r, weeks_b_16r, 1.5, 0.3), decimals=4,
           mistakes={"le départ n'est pas connu : sa variance 0,3 se transmet, passe var0=0.3":
                         moments_16r(weeks_a_16r, weeks_b_16r, 1.5, 0),
                     "chaque semaine ajoute le bruit b_t² à la variance : passe B_16 aux pas":
                         moments_16r(weeks_a_16r, [0] * len(weeks_b_16r), 1.5, 0.3),
                     "le départ a la moyenne 1,5 : passe mean0=1.5": moments_16r(weeks_a_16r, weeks_b_16r, 0, 0.3)})
seven_16r = moments_16r([-0.68] * 7, [1.1] * 7, 5)
limit_16r = float(F_16r("1.1") ** 2 / (1 - F_16r("0.68") ** 2))
wbm.record("MB5.16c", seven_16r + [limit_16r], decimals=2,
           mistakes={"a = −0,68 est négatif : la moyenne change de signe à chaque pas":
                         moments_16r([0.68] * 7, [1.1] * 7, 5) + [limit_16r],
                     "la variance stationnaire est le point fixe de v = a² v + b², d'où v (1 − a²) = b²":
                         seven_16r + [float(F_16r("1.1") ** 2 / (1 + F_16r("0.68") ** 2))],
                     "chaque pas ajoute le bruit b² = 1,21 à la variance : passe les b aux pas":
                         moments_16r([-0.68] * 7, [0] * 7, 5) + [limit_16r],
                     "le départ connu x_0 = 5 se passe par mean0 (sinon, mean0 vaut 0)":
                         moments_16r([-0.68] * 7, [1.1] * 7, 0) + [limit_16r]})'''),
        ("solution", answers_check("MB5.16", "abc", hints=HINTS_16)),
        look("pourquoi les moyennes de c) changent-elles de signe à chaque pas, et de combien leur valeur absolue "
             "diminue-t-elle ? Par quel côté la variance approche-t-elle $v_\\infty$ ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB5.17 · posterior_mean_mixture
# ---------------------------------------------------------------------------
NOTE_17 = (r"Les contrôles, puis, pour chaque composante, `spread = a ** 2 * s2 + b ** 2`, les logarithmes $\ln\pi_k - "
           r"\frac12\ln(2\pi\,\text{spread}) - \frac{(y - a\mu_k)^2}{2\,\text{spread}}$, une softmax par mesure (retirer "
           r"le maximum), et la moyenne des $\mu_k + \frac{as_k^2}{\text{spread}}(y - a\mu_k)$ ; pour $a = 0$, la moyenne "
           r"du mélange. a) $2{,}28$, comme MB5.5 a). b) $\approx 1{,}600998$, comme MB5.5 d). c) $(-1{,}359572 ;\ "
           r"0{,}975972 ;\ 2{,}363601)$. Pour $a = 0$, la fonction rend $1{,}375$, la moyenne du mélange, quel que soit $y$.")

MB5_17 = ex(
    "MB5.17", "programmer le débruiteur optimal d'une mesure bruitée quand le signal suit un mélange de gaussiennes (des "
    "points compris), puis retrouver MB5.5 et débruiter un signal à deux bosses.",
    "fiche §5 ; M25a §5 (modèle linéaire gaussien), M25b (responsabilités), M05a (log-sum-exp) ; Ex MB5.5",
    functions="`posterior_mean_mixture`", mymath="gaussian_paths.py", note=NOTE_17,
    body=REMINDER + r"""

Écris `posterior_mean_mixture(y, a, b, weights, means, variances)` (fiche §5), en suivant sa docstring : contrôle les arguments ; pour chaque composante de variance $v_k$ ($s_k^2$ dans la docstring), la variance $a^2v_k + b^2$ de $y$, le logarithme de $\pi_k\,\mathcal{N}(y \mid a\mu_k, a^2v_k + b^2)$ ($-\infty$ pour un poids nul) et $\mathbb{E}[x \mid y, k]$ ; les responsabilités par un log-sum-exp sur $k$, pour chaque mesure (le `logsumexp` de ton `approx.py`, M05a, ou, à défaut, un `_logsumexp` privé écrit dans `gaussian_paths.py`) ; enfin la moyenne pondérée, de la forme de `y` ; pour $a = 0$, la moyenne du mélange. Lance le groupe de tests.

**L'usage.** Avec ta fonction :
- a) la partie A de MB5.5 (`SIGNAL_5A`, cellule de données), comme un mélange à une composante : $\mathbb{E}[x \mid y = 6]$ (un nombre, à comparer à ta copie) ;
- b) la partie B de MB5.5 (`SIGNAL_5B`), comme deux points de poids $\frac12$ (des variances nulles) : $\mathbb{E}[x \mid y = 1{,}1]$ (un nombre) ;
- c) un signal reçu qui suit le mélange $0{,}25\,\mathcal{N}(-1{,}4 ;\ 0{,}2) + 0{,}75\,\mathcal{N}(2{,}3 ;\ 0{,}5)$, mesuré par $y = 0{,}7\,x + 0{,}5\,n$ : $\mathbb{E}[x \mid y]$ pour $y = -0{,}9$, $0{,}3$ et $1{,}7$ (une liste de 3 nombres).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `posterior_mean_mixture` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_posterior_mean_mixture_") + [
        ("md", "**L'usage** : les deux signaux de MB5.5, puis un signal à deux bosses."),
        ("todo", '''answer_MB5_17a = answer_MB5_17b = answer_MB5_17c = ...
with wbm.attempt("MB5.17"):          # if you call posterior_mean_mixture here: ⏳ while it is not written
    answer_MB5_17a = ...  # a) a number, as computed: E[x | y = 6] for the part A of MB5.5 (a mixture of one component)
    answer_MB5_17b = ...  # b) a number, as computed: E[x | y = 1.1] for the part B of MB5.5 (two points, weights 1/2)
    answer_MB5_17c = ...  # c) a list of 3 numbers, as computed: E[x | y] for y = -0.9, 0.3, 1.7 (the mixture of c)'''),
        ("check", answers_check("MB5.17", "abc", hints=HINTS_17)),
        ("solution", '''posterior_mean_mixture = mymath.gaussian_paths.posterior_mean_mixture
answer_MB5_17a = float(posterior_mean_mixture(SIGNAL_5A["y"], SIGNAL_5A["a"], SIGNAL_5A["b"], [1.0], [SIGNAL_5A["m"]],
                                              [SIGNAL_5A["v"]]))
answer_MB5_17b = float(posterior_mean_mixture(SIGNAL_5B["y"], SIGNAL_5B["a"], SIGNAL_5B["b"], [0.5, 0.5],
                                              [-SIGNAL_5B["c"], SIGNAL_5B["c"]], [0.0, 0.0]))
answer_MB5_17c = posterior_mean_mixture([-0.9, 0.3, 1.7], 0.7, 0.5, [0.25, 0.75], [-1.4, 2.3], [0.2, 0.5]).tolist()
print("a)", round(answer_MB5_17a, 6), " b)", round(answer_MB5_17b, 6), " c)", np.round(answer_MB5_17c, 6).tolist())
print("   avec a = 0 :", float(posterior_mean_mixture(0.3, 0.0, 0.5, [0.25, 0.75], [-1.4, 2.3], [0.2, 0.5])))'''),
        ("record", '''from scipy import integrate as integrate_17r
from scipy import stats as stats_17r


def posterior_17r(y, a, b, weights, means, variances, alone=False, centre=True):
    """The oracle: E[x | y] by integrating x against the posterior density (scipy.integrate.quad), point masses by
    exact sums; alone: the responsibilities computed with the variance of the signal alone (the classic error);
    centre=False: the responsibilities compare y with mu_k instead of a mu_k."""
    def likelihood(k):
        spread = variances[k] if alone else a * a * variances[k] + b * b
        return weights[k] * stats_17r.norm.pdf(y, (a if centre else 1) * means[k], spread ** 0.5)

    if alone or not centre or all(v == 0 for v in variances):
        within = [means[k] + (a * variances[k] / (a * a * variances[k] + b * b)) * (y - a * means[k])
                  for k in range(len(weights))]                       # E[x | y, k], M25a
        resp = [likelihood(k) for k in range(len(weights))]
        return sum(r * e for r, e in zip(resp, within)) / sum(resp)

    def density(x):
        prior = sum(w * stats_17r.norm.pdf(x, m, v ** 0.5) for w, m, v in zip(weights, means, variances))
        return prior * stats_17r.norm.pdf(y, a * x, b)

    top = integrate_17r.quad(lambda x: x * density(x), -40, 40, points=list(means), limit=400)[0]
    return top / integrate_17r.quad(density, -40, 40, points=list(means), limit=400)[0]


wbm.record("MB5.17a", posterior_17r(6.0, 2.0, 3.0, [1.0], [1.0], [4.0]), decimals=6,
           mistakes={"l'écart à la moyenne de y est y − a μ_k, pas y − μ_k (relance les tests de posterior_mean_mixture)":
                         1.0 + 2.0 * 4.0 * (6.0 - 1.0) / (4.0 * 4.0 + 9.0)})
wbm.record("MB5.17b", posterior_17r(1.1, 0.5, 1.0, [0.5, 0.5], [-2.0, 2.0], [0.0, 0.0]), decimals=6,
           mistakes={"les responsabilités comparent y à a μ_k, la moyenne de y sachant la composante (relance les tests "
                     "de posterior_mean_mixture)": posterior_17r(1.1, 0.5, 1.0, [0.5, 0.5], [-2.0, 2.0], [0.0, 0.0],
                                                                centre=False)})
mixture_17r = ([0.25, 0.75], [-1.4, 2.3], [0.2, 0.5])
wbm.record("MB5.17c", [posterior_17r(y, 0.7, 0.5, *mixture_17r) for y in (-0.9, 0.3, 1.7)], decimals=6,
           mistakes={"les responsabilités demandent la loi de y sachant la composante, de variance a² s_k² + b² (relance "
                     "les tests de posterior_mean_mixture)":
                         [posterior_17r(y, 0.7, 0.5, *mixture_17r, alone=True) for y in (-0.9, 0.3, 1.7)],
                     "les responsabilités comparent y à a μ_k, la moyenne de y sachant la composante (relance les tests "
                     "de posterior_mean_mixture)":
                         [posterior_17r(y, 0.7, 0.5, *mixture_17r, centre=False) for y in (-0.9, 0.3, 1.7)]})'''),
        ("solution", answers_check("MB5.17", "abc", hints=HINTS_17)),
        look("pour $y = -0{,}9$, quelle composante l'emporte, malgré son petit poids, et pourquoi $\\mathbb{E}[x \\mid y]$ "
             "n'est-il pas $\\frac ya$ ? Que rend ta fonction pour $a = 0$ ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB5.18 · euler_ode, midpoint_ode
# ---------------------------------------------------------------------------
NOTE_18 = (r"$h = \frac{t_N - t_0}{N}$, puis `x = x + h * f(t, x)` (Euler) ou `x = x + h * f(t + h / 2, x + h / 2 * "
           r"f(t, x))` (point milieu), avec `t = t0 + k * h` à chaque pas. a) $(51{,}85 ;\ 56{,}076625)$, comme MB5.8. "
           r"b) $\approx 56{,}2857$, contre $56{,}4462$ exactement et $55{,}1$ en un pas. c) $(5{,}25 ;\ 7{,}875)$, contre "
           r"8 : la somme de Riemann à gauche de $3t^2$, puis la règle du point milieu de M02a. d) $(0{,}102486 ;\ "
           r"0{,}029453)$, autour de la valeur exacte $2{,}149361$.")

MB5_18 = ex(
    "MB5.18", "programmer la méthode d'Euler et celle du point milieu pour un champ qui dépend du temps, dans les deux "
    "sens du temps, puis retrouver MB5.8 et voir quand chacune est exacte.",
    "fiche §8 ; M20 §6 (Euler), M02a (sommes de Riemann, point milieu) ; Ex MB5.8",
    functions="`euler_ode`, `midpoint_ode`", mymath="gaussian_paths.py", note=NOTE_18,
    body=REMINDER + r"""

Écris `euler_ode(f, x0, t0, t1, n_steps)` et `midpoint_ode(f, x0, t0, t1, n_steps)` (fiche §8), en suivant leurs docstrings : contrôle `n_steps` (un entier $\ge 1$, pas un booléen ni un flottant), `t0` et `t1` (des réels finis) et la forme de chaque vitesse ; $h = \frac{t_N - t_0}{N}$, négatif si $t_N < t_0$ (l'argument `t1`, comme celui de `solve_ivp`, est l'instant final $t_N$) ; une évaluation de `f` par pas pour Euler, deux pour le point milieu ; rends les $N + 1$ points, départ compris. Lance les deux groupes de tests.

**L'usage.** Avec tes fonctions :
- a) le thé de MB5.8 (`TEA_8`, cellule de données), à 10 min, par Euler puis par le point milieu, avec deux pas (une liste de 2 nombres, à comparer à ta copie) ;
- b) la tasse à 47 °C de MB5.8 e), remontée de 10 min à 5 min en dix pas d'Euler : sa température à 5 min (un nombre) ;
- c) $x' = 3t^2$, $x(0) = 0$, sur $[0, 2]$ en quatre pas : $x(2)$ par Euler, puis par le point milieu (une liste de 2 nombres) ;
- d) $x' = t - x$, $x(0) = 2$, sur $[0, 3]$ en six pas : l'erreur d'Euler, puis celle du point milieu, en $t = 3$, par rapport à la solution exacte $t - 1 + 3e^{-t}$ (une liste de 2 nombres, positifs).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `euler_ode`, puis ceux de `midpoint_ode` (lis d'abord la ligne qui suit chaque ❌ : elle "
                  "dit ce qui était attendu).")]
    + tests_cells("test_euler_ode_") + tests_cells("test_midpoint_ode_") + [
        ("md", "**L'usage** : le thé de MB5.8, dans un sens puis dans l'autre, puis deux champs dont on connaît la solution."),
        ("todo", '''answer_MB5_18a = answer_MB5_18b = answer_MB5_18c = answer_MB5_18d = ...
with wbm.attempt("MB5.18"):          # if you call your functions here: ⏳ while they are not written
    answer_MB5_18a = ...  # a) a list of 2 numbers, as computed: the tea at 10 min in two steps, Euler then midpoint
    answer_MB5_18b = ...  # b) a number, as computed: the cup at 47 °C at 10 min, taken back to 5 min in ten Euler steps
    answer_MB5_18c = ...  # c) a list of 2 numbers, as computed: x(2) for x' = 3t², four steps, Euler then midpoint
    answer_MB5_18d = ...  # d) a list of 2 numbers, as computed: the errors at t = 3 (positive), Euler then midpoint'''),
        ("check", answers_check("MB5.18", "abcd", hints=HINTS_18)),
        ("solution", '''euler_ode, midpoint_ode = mymath.gaussian_paths.euler_ode, mymath.gaussian_paths.midpoint_ode


def tea_18(t, T):
    """Newton's cooling of the tea of MB5.8 (°C, minutes)."""
    return -TEA_8["r"] * (T - TEA_8["room"])


answer_MB5_18a = [float(euler_ode(tea_18, TEA_8["T0"], 0.0, 10.0, 2)[-1]),
                  float(midpoint_ode(tea_18, TEA_8["T0"], 0.0, 10.0, 2)[-1])]
answer_MB5_18b = float(euler_ode(tea_18, TEA_8["T10"], 10.0, 5.0, 10)[-1])
answer_MB5_18c = [float(euler_ode(lambda t, x: 3 * t ** 2, 0.0, 0.0, 2.0, 4)[-1]),
                  float(midpoint_ode(lambda t, x: 3 * t ** 2, 0.0, 0.0, 2.0, 4)[-1])]
exact_18 = 3 - 1 + 3 * math.exp(-3)
answer_MB5_18d = [abs(float(euler_ode(lambda t, x: t - x, 2.0, 0.0, 3.0, 6)[-1]) - exact_18),
                  abs(float(midpoint_ode(lambda t, x: t - x, 2.0, 0.0, 3.0, 6)[-1]) - exact_18)]
print("a)", np.round(answer_MB5_18a, 6).tolist(), " b)", round(answer_MB5_18b, 6), " c)", answer_MB5_18c,
      " d)", np.round(answer_MB5_18d, 6).tolist(), f" (exact en t = 3 : {exact_18:.6f})")'''),
        ("record", '''from fractions import Fraction as F_18r


def path_18r(field, x, t, h, n, midpoint=False, half=F_18r(1, 2), late=False):
    """The oracle: n steps of Euler or of the midpoint method in exact fractions (the fields of the statement are
    polynomials); half: the length of the first half step (1: the classic error); late: Euler reading the velocity at
    the end of each step (the classic error)."""
    x, t, h = F_18r(x), F_18r(t), F_18r(h)
    for _ in range(n):
        if midpoint:
            x = x + h * field(t + h / 2, x + half * h * field(t, x))
        else:
            x = x + h * field(t + h if late else t, x)
        t = t + h
    return x


def tea_18r(t, T):
    return -F_18r(6, 100) * (T - 20)


tea_18r_both = [float(path_18r(tea_18r, 85, 0, 5, 2)), float(path_18r(tea_18r, 85, 0, 5, 2, midpoint=True))]
wbm.record("MB5.18a", tea_18r_both, decimals=6,
           mistakes={"la liste suit l'ordre de l'énoncé : Euler d'abord, puis le point milieu": tea_18r_both[::-1],
                     "le point milieu fait d'abord un demi-pas d'Euler, h/2, puis lit la vitesse là (relance les tests de "
                     "midpoint_ode)": [tea_18r_both[0], float(path_18r(tea_18r, 85, 0, 5, 2, midpoint=True, half=1))]})
wbm.record("MB5.18b", float(path_18r(tea_18r, 47, 10, F_18r(-1, 2), 10)), decimals=6,
           mistakes={"dix pas d'Euler de 0,5 min, pas un seul pas de 5 min": float(path_18r(tea_18r, 47, 10, -5, 1))})
square_18r = lambda t, x: 3 * t * t                                              # noqa: E731
wbm.record("MB5.18c", [float(path_18r(square_18r, 0, 0, F_18r(1, 2), 4)),
                       float(path_18r(square_18r, 0, 0, F_18r(1, 2), 4, midpoint=True))], decimals=6,
           mistakes={"la liste suit l'ordre de l'énoncé : Euler d'abord, puis le point milieu":
                         [float(path_18r(square_18r, 0, 0, F_18r(1, 2), 4, midpoint=True)),
                          float(path_18r(square_18r, 0, 0, F_18r(1, 2), 4))],
                     "Euler lit la vitesse au début de chaque pas, en t_k (relance les tests de euler_ode)":
                         [float(path_18r(square_18r, 0, 0, F_18r(1, 2), 4, late=True)),
                          float(path_18r(square_18r, 0, 0, F_18r(1, 2), 4, midpoint=True))]})
exact_18r = 2 + 3 * math.exp(-3)
signed_18r = [float(path_18r(lambda t, x: t - x, 2, 0, F_18r(1, 2), 6)) - exact_18r,
              float(path_18r(lambda t, x: t - x, 2, 0, F_18r(1, 2), 6, midpoint=True)) - exact_18r]
wbm.record("MB5.18d", [abs(e) for e in signed_18r], decimals=6,
           mistakes={"une erreur se donne ici positive : la valeur absolue de l'écart à la solution exacte": signed_18r,
                     "la liste suit l'ordre de l'énoncé : Euler d'abord, puis le point milieu":
                         [abs(e) for e in signed_18r[::-1]]})'''),
        ("solution", answers_check("MB5.18", "abcd", hints=HINTS_18)),
        look("à quelle somme de M02a correspondent les deux valeurs de c), et pourquoi le point milieu n'y est-il pas "
             "exact ? De combien l'erreur de b) en dix pas est-elle plus petite que celle d'un seul pas, en MB5.8 e) ?"),
    ],
)

PART_A = Part("A", "Ta librairie : une récurrence linéaire gaussienne, le débruiteur d'un mélange, Euler et le point milieu",
              "Fiche §1, §5 et §8. Les quatre fonctions de `mymath/gaussian_paths.py`, leurs tests, et un usage de "
              "chacune. La cellule de données ci-dessous recopie les données des exercices papier.",
              given=TOOLS + "\n\n\n" + DATA, exercises=[MB5_16, MB5_17, MB5_18])

# ---------------------------------------------------------------------------
# Notebook exercises: a library, predict, experiment, draw (MB5.19 to MB5.22)
# ---------------------------------------------------------------------------
NOTE_19 = (r"a) $P(8) \approx 39{,}247917$ (l'écart à la solution exacte est de l'ordre de $10^{-9}$). b) Euler : "
           r"$0{,}477 ;\ 0{,}156 ;\ 0{,}0655 ;\ 0{,}0302 ;\ 0{,}0145 ;\ 0{,}00710$ ; point milieu : $0{,}430 ;\ 0{,}0843 ;\ "
           r"0{,}0194 ;\ 0{,}00470 ;\ 0{,}00116 ;\ 0{,}000289$. c) $(-1{,}067 ;\ -2{,}022)$, soit $(-1{,}1 ;\ -2{,}0)$ ; "
           r"à 64 évaluations, $0{,}0302$ pour Euler (64 pas) contre $0{,}0194$ pour le point milieu (32 pas).")

MB5_19 = ex(
    "MB5.19", "suivre une croissance logistique par `solve_ivp` et par tes deux méthodes, et mesurer l'ordre de leur "
    "erreur en échelles logarithmiques.", "fiche §8 ; M02a §5 (ordre d'une méthode) ; Ex MB5.18", note=NOTE_19,
    body=r"""Une culture de levures suit $P' = 0{,}9\,P\big(1 - \frac{P}{40}\big)$ (en millions de cellules, $t$ en heures), depuis $P(0) = 1{,}5$ ; la fiche §8 donne la solution exacte de la croissance logistique. Avec `scipy.integrate.solve_ivp` et tes fonctions `euler_ode` et `midpoint_ode`, relève :
- a) $P(8)$ par `solve_ivp(…, rtol=1e-10, atol=1e-10)` (un nombre), à comparer à la solution exacte ;
- b) pour $N = 8$, 16, 32, 64, 128 et 256 pas, l'erreur de `euler_ode`, puis celle de `midpoint_ode`, en $t = 8$, par rapport à la solution exacte (deux listes de 6 nombres positifs : les valeurs absolues des écarts), et trace-les contre $N$ en échelles logarithmiques (`ax.loglog`) ;
- c) les pentes des deux droites, ajustées sur $N = 32$ à 256 par `np.polyfit` sur les logarithmes (une liste de 2 nombres, Euler puis le point milieu), puis lis dans b), à 64 évaluations du champ, l'erreur d'Euler (64 pas) et celle du point milieu (32 pas).""",
    todo='''answer_MB5_19a = answer_MB5_19b = answer_MB5_19c = ...
with wbm.attempt("MB5.19"):          # solve_ivp, then your euler_ode and midpoint_ode: ⏳ while they are not written
    answer_MB5_19a = ...  # a) a number, as computed: P(8) by solve_ivp(..., rtol=1e-10, atol=1e-10)
    answer_MB5_19b = ...  # b) two lists of 6 numbers, as computed: the errors at t = 8 of euler_ode, then of midpoint_ode, for N = 8 to 256
    answer_MB5_19c = ...  # c) a list of 2 numbers, as computed: the slopes fitted on N = 32 to 256, Euler then midpoint
    # and your figure: the errors of b) against N, in logarithmic scales''',
    check=answers_check("MB5.19", "abc", hints=HINTS_19),
    solution='''from scipy.integrate import solve_ivp


def yeast_19(t, P):
    """The logistic growth of the yeast: P' = 0.9 P (1 - P / 40)."""
    return 0.9 * P * (1 - P / 40)


exact_19 = 40 / (1 + (40 / 1.5 - 1) * math.exp(-0.9 * 8))          # the exact solution of the fiche, at t = 8
answer_MB5_19a = float(solve_ivp(yeast_19, (0.0, 8.0), [1.5], rtol=1e-10, atol=1e-10).y[0, -1])
steps_19 = [8, 16, 32, 64, 128, 256]
answer_MB5_19b = [[abs(float(method(yeast_19, 1.5, 0.0, 8.0, n)[-1]) - exact_19) for n in steps_19]
                  for method in (mymath.gaussian_paths.euler_ode, mymath.gaussian_paths.midpoint_ode)]
answer_MB5_19c = [float(np.polyfit(np.log(steps_19[2:]), np.log(errors[2:]), 1)[0]) for errors in answer_MB5_19b]
fig_19, ax_19 = plt.subplots(figsize=(6, 4))
ax_19.loglog(steps_19, answer_MB5_19b[0], "o-", label="Euler")
ax_19.loglog(steps_19, answer_MB5_19b[1], "s-", label="point milieu")
ax_19.set_xlabel("nombre de pas N")
ax_19.set_ylabel("erreur en t = 8")
ax_19.legend()
plt.show()
print("a)", round(answer_MB5_19a, 6), f"(exacte : {exact_19:.6f})")
print("b) Euler :", [float(f"{e:.6g}") for e in answer_MB5_19b[0]])
print("   point milieu :", [float(f"{e:.6g}") for e in answer_MB5_19b[1]])
print("c)", np.round(answer_MB5_19c, 3).tolist(), " à 64 évaluations :", round(answer_MB5_19b[0][3], 6), "et",
      round(answer_MB5_19b[1][2], 6))''',
    record='''from scipy.integrate import solve_ivp as solve_ivp_19r


def growth_19r(t, P):
    return 0.9 * P * (1 - P / 40)


exact_19r = 40 / (1 + (40 / 1.5 - 1) * math.exp(-7.2))                  # the oracle: the exact logistic solution


def final_19r(n, midpoint):
    """Euler or the midpoint method written again (floats), n steps from 0 to 8: the point at t = 8."""
    P, h = 1.5, 8 / n
    for k in range(n):
        t = k * h
        P = P + h * (growth_19r(t + h / 2, P + h / 2 * growth_19r(t, P)) if midpoint else growth_19r(t, P))
    return P


wbm.record("MB5.19a", exact_19r, decimals=6,
           mistakes={"solve_ivp prend ici rtol=1e-10 et atol=1e-10 : ses tolérances par défaut laissent une erreur de "
                     "l'ordre de 10⁻³": float(solve_ivp_19r(growth_19r, (0.0, 8.0), [1.5]).y[0, -1])})
sizes_19r = [8, 16, 32, 64, 128, 256]
signed_19r = [[final_19r(n, midpoint) - exact_19r for n in sizes_19r] for midpoint in (False, True)]
errors_19r = [[abs(e) for e in row] for row in signed_19r]
wbm.record("MB5.19b", errors_19r, decimals=8,
           mistakes={"une erreur se donne ici positive : la valeur absolue de l'écart à la solution exacte": signed_19r,
                     "les deux listes suivent l'ordre de l'énoncé : Euler d'abord, puis le point milieu":
                         errors_19r[::-1]})
slopes_19r = [float(np.polyfit(np.log(sizes_19r[2:]), np.log(row[2:]), 1)[0]) for row in errors_19r]
wbm.record("MB5.19c", slopes_19r, decimals=2,
           mistakes={"c) ajuste les pentes sur N = 32 à 256 seulement": [float(np.polyfit(np.log(sizes_19r),
                                                                                      np.log(row), 1)[0])
                                                                       for row in errors_19r],
                     "les pentes sont celles de ln(erreur) contre ln N : l'erreur diminue quand N grandit":
                         [-s for s in slopes_19r]})''',
    after=[
        ("solution", answers_check("MB5.19", "abc", hints=HINTS_19)),
        look("pourquoi ajuster les pentes sur les grands $N$ seulement ? À nombre d'évaluations égal, quelle méthode "
             "gagne, et de combien ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB5.20 · the denoiser of five records when the noise tends to 0
# ---------------------------------------------------------------------------
NOTE_20 = (r"Prédictions attendues : a) (B) ; b) (A) ; c) (C). d) $(2{,}43201 ;\ 1{,}95272 ;\ 2{,}00735 ;\ 1{,}90001 ;\ "
           r"1{,}9)$ ; e) $(2{,}67385 ;\ 2{,}93404 ;\ 2{,}95 ;\ 2{,}95 ;\ 2{,}95)$ ; f) $\approx 2{,}59993$, presque la "
           r"moyenne $2{,}6$ des relevés.")

MB5_20 = ex(
    "MB5.20", "prévoir ce que rend le débruiteur optimal d'un nuage de points quand le bruit s'efface, puis le mesurer.",
    "fiche §5 ; M04 (Bayes), MB3 (moyenne pondérée par une softmax) ; Ex MB5.5, MB5.17", hypothesis=True, note=NOTE_20,
    body=r"""Un marégraphe a relevé cinq fois la hauteur de la mer, en m : $1{,}2$ ; $1{,}9$ ; $2{,}3$ ; $3{,}6$ ; $4{,}0$ (`RECORDS_20`), de poids égaux ; un capteur mesure $y = 0{,}5\,x + b\,n$, où $x$ est l'un des cinq relevés. **Avant d'exécuter quoi que ce soit**, prédis, quand $b$ tend vers 0 :
- a) pour $y = 1$ (donc $\frac ya = 2$), $\mathbb{E}[x \mid y]$ tend vers : (A) 2 ; (B) $1{,}9$ ; (C) $2{,}6$, la moyenne des relevés (une lettre) ;
- b) pour $y = 1{,}475$ (donc $\frac ya = 2{,}95$, à égale distance de $2{,}3$ et de $3{,}6$) : (A) $2{,}95$ ; (B) $2{,}3$ ; (C) $3{,}6$ (une lettre) ;
- c) pour $y = 1$ et un bruit énorme, $b = 50$ : (A) $1{,}9$ ; (B) 2 ; (C) $2{,}6$ (une lettre).

Puis, une fois tes prédictions écrites et vérifiées, mesure avec `posterior_mean_mixture` (les cinq relevés comme des points : des variances nulles) :
- d) $\mathbb{E}[x \mid y = 1]$ pour $b = 1$, $0{,}3$, $0{,}1$, $0{,}03$ et $0{,}01$, dans cet ordre (une liste de 5 nombres) ;
- e) la même chose pour $y = 1{,}475$ (une liste de 5 nombres) ;
- f) $\mathbb{E}[x \mid y = 1]$ pour $b = 50$ (un nombre).

La vérification de l'expérience ne s'exécute qu'une fois tes trois prédictions écrites.""",
    given='''RECORDS_20 = frozen([1.2, 1.9, 2.3, 3.6, 4.0])     # five heights of the sea read by a tide gauge (m), equal weights''',
    todo='''prediction_MB5_20a = ...  # a) "A", "B" or "C": for y = 1 and b -> 0, E[x | y] tends to (A) 2, (B) 1.9, (C) 2.6
prediction_MB5_20b = ...  # b) "A", "B" or "C": for y = 1.475 and b -> 0, (A) 2.95, (B) 2.3, (C) 3.6
prediction_MB5_20c = ...  # c) "A", "B" or "C": for y = 1 and b = 50, (A) 1.9, (B) 2, (C) 2.6''',
    check='''for letter, prediction in zip("abc", [prediction_MB5_20a, prediction_MB5_20b, prediction_MB5_20c]):
    if filled(prediction) and not isinstance(prediction, str):      # a number, a list...: not yet a prediction
        print(f'❌ Ex MB5.20{letter} : une prédiction est une lettre, "A", "B" ou "C", reçu {shown(prediction)}')
    else:
        wbm.check(f"MB5.20{letter}", prediction)''',
    record='''def limit_20r(y, b, a=0.5, records=(1.2, 1.9, 2.3, 3.6, 4.0)):
    """The oracle: E[x | y] for points of equal weights, by Bayes (the largest log subtracted before the exponentials)."""
    logs = [-(y - a * x) ** 2 / (2 * b * b) for x in records]
    top = max(logs)
    weights = [math.exp(v - top) for v in logs]
    return sum(w * x for w, x in zip(weights, records)) / sum(weights)


wbm.record("MB5.20a", "B" if abs(limit_20r(1.0, 1e-3) - 1.9) < 1e-9 else "?", prediction=True,
           mistakes={"y/a = 2 est ce qu'on lirait sans rien savoir de x ; le débruiteur, lui, sait que x est l'un des cinq "
                     "relevés : compare leurs vraisemblances quand b est petit (fiche §5)": "A",
                     "quand b tend vers 0, la mesure devient de plus en plus précise : le débruiteur ne peut pas "
                     "l'ignorer": "C"})
wbm.record("MB5.20b", "A" if abs(limit_20r(1.475, 1e-3) - 2.95) < 1e-9 else "?", prediction=True,
           mistakes={"y/a = 2,95 tombe entre deux relevés : écris leurs deux vraisemblances quand b est petit, et "
                     "regarde ce que devient la moyenne qu'elles pondèrent (fiche §5)": "B",
                     "y/a = 2,95 tombe entre deux relevés : écris les responsabilités des cinq relevés quand b tend vers "
                     "0, et ce qu'il reste de la moyenne pondérée (fiche §5)": "C"})
wbm.record("MB5.20c", "C" if abs(limit_20r(1.0, 50.0) - 2.6) < 1e-3 else "?", prediction=True,
           mistakes={"avec b = 50, la mesure est noyée dans le bruit : regarde ce que deviennent les cinq "
                     "responsabilités": "A",
                     "y/a n'a de sens que si le bruit est faible : avec b = 50, que dit encore la mesure ?": "B"})''',
    after=[
        ("md", "**L'expérience.** Écris-la une fois tes trois prédictions vérifiées ; sa vérification ne s'exécute qu'à cette "
               "condition."),
        ("todo", '''answer_MB5_20d = answer_MB5_20e = answer_MB5_20f = ...
with wbm.attempt("MB5.20"):          # your posterior_mean_mixture: ⏳ while it is not written
    answer_MB5_20d = ...  # d) a list of 5 numbers, as computed: E[x | y = 1] for b = 1, 0.3, 0.1, 0.03, 0.01
    answer_MB5_20e = ...  # e) a list of 5 numbers, as computed: E[x | y = 1.475] for the same b
    answer_MB5_20f = ...  # f) a number, as computed: E[x | y = 1] for b = 50'''),
        ("check", guarded(answers_check("MB5.20", "def", hints=HINTS_20), [f"prediction_MB5_20{letter}" for letter in "abc"],
                          "⏳ Écris d'abord tes trois prédictions, puis exécute à nouveau.")),
        ("solution", '''posterior_mean_mixture = mymath.gaussian_paths.posterior_mean_mixture
noises_20 = [1.0, 0.3, 0.1, 0.03, 0.01]
points_20 = ([0.2] * 5, RECORDS_20, [0.0] * 5)                        # five points of equal weights
answer_MB5_20d = [float(posterior_mean_mixture(1.0, 0.5, b, *points_20)) for b in noises_20]
answer_MB5_20e = [float(posterior_mean_mixture(1.475, 0.5, b, *points_20)) for b in noises_20]
answer_MB5_20f = float(posterior_mean_mixture(1.0, 0.5, 50.0, *points_20))
print("d)", np.round(answer_MB5_20d, 6).tolist(), " e)", np.round(answer_MB5_20e, 6).tolist(),
      " f)", round(answer_MB5_20f, 6))'''),
        ("record", '''noises_20r = [1.0, 0.3, 0.1, 0.03, 0.01]
wbm.record("MB5.20d", [limit_20r(1.0, b) for b in noises_20r], decimals=6,
           mistakes={"d) passe la mesure y = 1 elle-même : la fonction divise par a, pas toi":
                         [limit_20r(2.0, b) for b in noises_20r],
                     "la liste suit l'ordre de l'énoncé : b = 1, 0,3, 0,1, 0,03, puis 0,01":
                         [limit_20r(1.0, b) for b in noises_20r[::-1]]})
wbm.record("MB5.20e", [limit_20r(1.475, b) for b in noises_20r], decimals=6,
           mistakes={"e) passe la mesure y = 1,475 elle-même : la fonction divise par a, pas toi":
                         [limit_20r(2.95, b) for b in noises_20r],
                     "la liste suit l'ordre de l'énoncé : b = 1, 0,3, 0,1, 0,03, puis 0,01":
                         [limit_20r(1.475, b) for b in noises_20r[::-1]]})
wbm.record("MB5.20f", limit_20r(1.0, 50.0), decimals=4,
           mistakes={"f) passe la mesure y = 1 elle-même : la fonction divise par a, pas toi": limit_20r(2.0, 50.0)})'''),
        ("solution", answers_check("MB5.20", "def", hints=HINTS_20)),
        look("à partir de quel $b$ le débruiteur rend-il presque exactement un relevé ? Pourquoi ne rend-il jamais 2, la "
             "valeur $\\frac ya$ ? Qu'est-ce qu'un débruiteur optimal fabrique de nouveau à partir d'un nuage de points ?",
             " (après l'expérience)"),
    ],
)

# ---------------------------------------------------------------------------
# MB5.21 · the straight path to a Gaussian law
# ---------------------------------------------------------------------------
CHECK_21 = '''HIDDEN_C21 = __HIDDEN_C21__   # hidden times and points, and the sub-ID of the values expected

with checked("MB5.21"):
    results_21 = []
    report_21 = reporter(results_21, stop=False)
    got_c21, changed_c21 = [], False
    for s_c21, points_c21 in HIDDEN_C21["calls"]:
        x_c21 = np.array(points_c21)                     # non-dyadic floats: a change in place would show
        got_c21.append(as_floats(call_safely("Ex MB5.21 : field_21 (appel caché)", field_21, s_c21, x_c21)))
        changed_c21 = changed_c21 or not np.array_equal(x_c21, np.array(points_c21))
    if changed_c21:
        report_21(False, "", "field_21 modifie le tableau x reçu : calcule sur une copie")
    elif any(g is None or g.shape != np.shape(p) for g, (_, p) in zip(got_c21, HIDDEN_C21["calls"])):
        report_21(False, "", "field_21 rend un tableau de la forme de x (euler_ode lui passe un tableau de points)")
    else:
        report_21(passes(HIDDEN_C21["id"], [v for g in got_c21 for v in g.tolist()]),
                  "field_21 en des points cachés (d'autres instants, d'autres points) : le champ moyen exact",
                  "field_21 en des points cachés : ce n'est pas le champ moyen v(x, s) = (x − E[x_0 | x_s = x])/s du chemin "
                  "droit x_s = (1 − s) x_0 + s ε vers N(4 ; 0,25) (fiche §9) ; essaie-la en s = 1, où elle vaut x − 4 "
                  "(MB5.9)")

field_ok_21 = bool(results_21) and all(results_21)


def hint_21(value):
    """A targeted hint for a) and b): field_21 first, then the library."""
    if not field_ok_21:
        return "les écarts-types se calculent avec field_21 : corrige-la d'abord (ligne ❌ ci-dessus)"
    return library_hint("euler_ode et midpoint_ode")(value)


def means_21():
    """a) checks the means too: np.mean of the points reached from Z_21 with your field_21, by Euler's method then the
    midpoint method of the reference, for N = 1, 2, 4, 8, 16, 32 (None if field_21 cannot be run)."""
    try:
        return [float(np.mean(method(field_21, Z_21, 1.0, 0.0, n)[-1])) for method in (ref_gp.euler_ode,
                                                                                        ref_gp.midpoint_ode)
                for n in (1, 2, 4, 8, 16, 32)]
    except Exception:  # noqa: BLE001 - field_21 fails: its own line says why
        return None


'''

ANSWERS_21 = '''means_c21 = means_21() if filled(answer_MB5_21a) else None
means_wrong_c21 = means_c21 is not None and not passes(HIDDEN_C21["id_means"], means_c21)
if means_wrong_c21 and wbm.check("MB5.21a", answer_MB5_21a, computed=True, quiet=True).passed:   # right spreads only
    print("❌ Ex MB5.21a : la moyenne (np.mean) des points que ta field_21 fait atteindre n'est pas celle du transport "
          "exact : un terme qui ne dépend que de s déplace tous les points sans changer leur dispersion (ligne ❌ de "
          "field_21 ci-dessus)")
else:
    check_answer("MB5.21a", answer_MB5_21a, hint=hint_21)
check_answer("MB5.21b", answer_MB5_21b, hint=hint_21)'''

NOTE_21 = (r"`field_21(s, x)` $= -4 + \frac{s - 0{,}25(1 - s)}{0{,}25(1 - s)^2 + s^2}\big(x - 4(1 - s)\big)$. a) Euler : "
           r"$(0 ;\ 0{,}200173 ;\ 0{,}340834 ;\ 0{,}415142 ;\ 0{,}456076 ;\ 0{,}477775)$ ; point milieu : $(0{,}400345 ;\ "
           r"0{,}494813 ;\ 0{,}498721 ;\ 0{,}500208 ;\ 0{,}500403 ;\ 0{,}500428)$. b) $0{,}500431$. L'écart à "
           r"l'écart-type exact est divisé par environ 2 quand $N$ double pour Euler, et par environ 8 pour le point "
           r"milieu : mieux que l'ordre 2 de la fiche, qui est une garantie.")

MB5_21 = ex(
    "MB5.21", "suivre le champ moyen exact d'un chemin droit vers une loi gaussienne par Euler et par le point milieu, "
    "et mesurer comment l'écart-type obtenu approche celui de la cible.",
    "fiche §8 et §9 ; Ex MB5.9, MB5.18", note=NOTE_21,
    given='''Z_21 = frozen(np.random.default_rng(7721).normal(size=100_000))   # 100 000 draws of N(0, 1), at s = 1''',
    body=r"""Les données suivent $\mathcal{N}(4 ;\ 0{,}25)$, comme en MB5.9 (`DATA_9`), et le chemin droit est $x_s = (1 - s)\,x_0 + s\,\varepsilon$. Écris `field_21(s, x)`, le champ moyen exact $v(x, s)$, affine en $x$, pour $0 < s \le 1$ : une fonction du temps $s$ puis du point $x$ (un tableau de points), pour `euler_ode` et `midpoint_ode`, qui l'appellent `f(t, x)`. La vérification la compare au débruiteur de `posterior_mean_mixture` avec $a = 1 - s$ et $b = s$, en des points cachés.

Le notebook fournit `Z_21`, 100 000 tirages de $\mathcal{N}(0, 1)$. Transporte-les de $s = 1$ à $s = 0$ (`t0=1.0`, `t1=0.0`) par Euler, puis par le point milieu, avec $N = 1$, 2, 4, 8, 16 et 32 pas. Relève :
- a) l'écart-type (`np.std`) des points obtenus, pour Euler, puis pour le point milieu (deux listes de 6 nombres ; la vérification regarde aussi leur moyenne, `np.mean`) ;
- b) l'écart-type obtenu en transportant exactement : celui de `4 + 0.5 * Z_21` (un nombre).""",
    todo='''def field_21(s, x):
    """The exact mean field v(x, s) of the straight path to the data N(4, 0.25), for 0 < s <= 1: the time s first, then
    the points x (an array), as euler_ode and midpoint_ode call it."""
    raise NotImplementedError("field_21 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB5_21a = answer_MB5_21b = ...
with wbm.attempt("MB5.21"):          # your field and your euler_ode, midpoint_ode: ⏳ while they are not written
    answer_MB5_21a = ...  # a) two lists of 6 numbers, as computed: np.std of the points reached from Z_21 for N = 1, 2, 4, 8, 16, 32, Euler then midpoint
    answer_MB5_21b = ...  # b) a number, as computed: np.std(4 + 0.5 * Z_21)''',
    check=CHECK_21 + ANSWERS_21,
    solution='''def field_21(s, x):
    """The exact mean field v(x, s) of the straight path to the data N(4, 0.25), for 0 < s <= 1: the time s first, then
    the points x (an array), as euler_ode and midpoint_ode call it."""
    m, tau2 = DATA_9["m"], DATA_9["tau"] ** 2
    sigma2 = (1 - s) ** 2 * tau2 + s ** 2                     # the variance of x_s
    return -m + (s - (1 - s) * tau2) / sigma2 * (np.asarray(x, dtype=float) - (1 - s) * m)


steps_21 = [1, 2, 4, 8, 16, 32]
answer_MB5_21a = [[float(np.std(method(field_21, Z_21, 1.0, 0.0, n)[-1])) for n in steps_21]
                  for method in (mymath.gaussian_paths.euler_ode, mymath.gaussian_paths.midpoint_ode)]
answer_MB5_21b = float(np.std(4 + 0.5 * Z_21))
print("a) Euler :", np.round(answer_MB5_21a[0], 6).tolist())
print("   point milieu :", np.round(answer_MB5_21a[1], 6).tolist(), " b)", round(answer_MB5_21b, 6))
for name_21, sds_21 in zip(("Euler", "point milieu"), answer_MB5_21a):
    gaps_21 = [abs(sd - answer_MB5_21b) for sd in sds_21]
    print(f"   {name_21} : écarts {[float(f'{g:.3g}') for g in gaps_21]}, divisés par "
          f"{[round(gaps_21[k] / gaps_21[k + 1], 2) for k in range(5)]}")
print("   moyennes (Euler, 1 pas ; point milieu, 32 pas) :",
      round(float(np.mean(mymath.gaussian_paths.euler_ode(field_21, Z_21, 1.0, 0.0, 1)[-1])), 6),
      round(float(np.mean(mymath.gaussian_paths.midpoint_ode(field_21, Z_21, 1.0, 0.0, 32)[-1])), 6))''',
    record='''from fractions import Fraction as F_21r

M_21r, TAU2_21r = F_21r(4), F_21r(1, 4)


def field_parts_21r(s):
    """The oracle: v(x, s) = intercept(s) + gain(s) x, exactly (the linear Gaussian model of M25a, for N(4, 1/4))."""
    sigma2 = (1 - s) ** 2 * TAU2_21r + s ** 2
    gain = (s - (1 - s) * TAU2_21r) / sigma2
    return -M_21r - gain * (1 - s) * M_21r, gain


def slope_21r(n, midpoint):
    """The transport from s = 1 to s = 0 in n steps is affine in z: its slope, exactly."""
    slope, s, h = F_21r(1), F_21r(1), F_21r(-1, n)
    for _ in range(n):
        if midpoint:
            _, gain_start = field_parts_21r(s)
            _, gain_middle = field_parts_21r(s + h / 2)
            slope = slope * (1 + h * gain_middle * (1 + h / 2 * gain_start))
        else:
            slope = slope * (1 + h * field_parts_21r(s)[1])
        s += h
    return slope


spread_21r = float(np.std(Z_21))                     # the points reached are a + slope z: np.std is |slope| np.std(z)
sds_21r = [[abs(float(slope_21r(n, midpoint))) * spread_21r for n in (1, 2, 4, 8, 16, 32)] for midpoint in (False, True)]
wbm.record("MB5.21a", sds_21r, decimals=7,
           mistakes={"les deux listes suivent l'ordre de l'énoncé : Euler d'abord, puis le point milieu": sds_21r[::-1]})
wbm.record("MB5.21b", float(np.std(4 + 0.5 * Z_21)), decimals=6,
           mistakes={"b) se mesure sur l'échantillon 4 + 0,5 Z_21, avec np.std : Z_21 n'a pas exactement la dispersion 1":
                         0.5})
HIDDEN_21r = __HIDDEN_C21__                                                  # the hidden calls of the check


def field_21r(s, x):
    intercept, gain = field_parts_21r(F_21r(str(s)))
    return [float(intercept) + float(gain) * v for v in x]


wbm.record(HIDDEN_21r["id"], [v for s, x in HIDDEN_21r["calls"] for v in field_21r(s, x)], decimals=6)


def transport_21r(n, midpoint):
    """The transport from s = 1 to s = 0 in n steps is affine in z: (its intercept, its slope), exactly."""
    intercept, slope, s, h = F_21r(0), F_21r(1), F_21r(1), F_21r(-1, n)
    for _ in range(n):
        c_start, g_start = field_parts_21r(s)
        if midpoint:
            c_mid, g_mid = field_parts_21r(s + h / 2)
            probe_intercept = intercept + h / 2 * (c_start + g_start * intercept)
            probe_slope = slope * (1 + h / 2 * g_start)
            intercept, slope = intercept + h * (c_mid + g_mid * probe_intercept), slope + h * g_mid * probe_slope
        else:
            intercept, slope = intercept + h * (c_start + g_start * intercept), slope * (1 + h * g_start)
        s += h
    return intercept, slope


centre_21r = float(np.mean(Z_21))                    # the points reached are intercept + slope z: their mean
wbm.record(HIDDEN_21r["id_means"], [float(c) + float(g) * centre_21r for midpoint in (False, True)
                                    for c, g in (transport_21r(n, midpoint) for n in (1, 2, 4, 8, 16, 32))], decimals=6)''',
    after=[
        ("solution", CHECK_21 + ANSWERS_21),
        look("pourquoi la moyenne des points (`np.mean`) est-elle juste dès un seul pas, et l'écart-type pas ? Par combien "
             "l'écart à l'écart-type exact est-il divisé quand $N$ double, pour Euler, puis pour le point milieu ? Est-ce "
             "l'ordre que donne la fiche ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB5.22 · guided laws on a grid
# ---------------------------------------------------------------------------
GIVEN_22 = '''# The general law p_u, a mixture with two bumps (weights, means, variances), the law p_c of the class (mean, variance),
# and the grid
GENERAL_22 = ((0.55, 0.45), (-1.8, 1.6), (0.5, 0.7))
CLASS_22 = (1.6, 0.7)
XS_22 = frozen(np.linspace(-8, 8, 3201))'''

CHECK_22 = r'''HIDDEN_C22 = __HIDDEN_C22__   # hidden calls, the points of the grids compared, and the sub-IDs of the values expected

_GENERAL_NAME_C22 = re.compile(r"p_?\{?u\}?|\bpu\b|génér|gener|incond|uncond", re.IGNORECASE)
_CLASS_NAME_C22 = re.compile(r"p_?\{?c\}?|\bpc\b|classe|\bclass|\bcond", re.IGNORECASE)


def label_w_c22(label):
    """The value of w written in a label of the legend (« w = 0,25 », « $w=1.75$ », « 3,5 »), or None."""
    text = str(label)
    if not text or text.startswith("_"):
        return None
    text = text.replace("{,}", ".").replace(",", ".")
    found = re.search(r"w\s*[=:]\s*\$?\s*([-+]?\d+(?:\.\d+)?)", text)
    if found:
        return float(found.group(1))
    text = re.sub(r"1\s*\+\s*w|[-−]\s*w|p_?\{?[cu]\}?|\^\{[^}]*\}", " ", text)
    found = re.search(r"(?<![\w.])(\d+(?:\.\d+)?)", text)
    return float(found.group(1)) if found else None


def density_c22(label, xs, w, **kwargs):
    """guided_22(xs, w, **kwargs) on a copy of xs, as a float array of the shape of xs (one ❌ line otherwise)."""
    grid = np.array(xs, dtype=float)
    got = as_floats(call_safely(label, guided_22, grid, w, **kwargs))
    if not np.array_equal(grid, np.asarray(xs, dtype=float)):
        print(f"❌ {label} : guided_22 modifie la grille xs reçue : calcule sur une copie")
        raise StopCheck
    if got is None or got.shape != grid.shape:
        print(f"❌ {label} : guided_22 rend un tableau de la forme de xs, reçu {shown(got)}")
        raise StopCheck
    return got


def figure_why_c22(ax, ws, curves, sub_id):
    """What is wrong in a call of draw_guided_22 (French phrases)."""
    idx = HIDDEN_C22["idx"]
    if not isinstance(curves, (list, tuple)) or len(curves) != len(ws):
        return [f"draw_guided_22 doit rendre la liste des {len(ws)} densités guidées tracées (une par w), reçu "
                f"{shown(curves)}"]
    curves = [as_floats(c) for c in curves]
    if any(c is None or c.shape != XS_22.shape for c in curves):
        return ["chaque densité rendue par draw_guided_22 doit avoir une valeur par point de XS_22"]
    problems = []
    if not passes(sub_id, [c[idx].tolist() for c in curves]):
        problems.append("les densités rendues doivent être celles de la loi guidée pour chaque w reçu, dans l'ordre reçu")
    lines = [line_with(ax, XS_22, c) for c in curves]
    if any(line is None for line in lines):
        problems.append("chaque loi guidée doit être tracée en fonction des points de XS_22")
    on_grid = [line for line in ax.lines if np.asarray(line.get_xdata(), dtype=float).shape == XS_22.shape
               and np.allclose(np.asarray(line.get_xdata(), dtype=float), XS_22)]
    general = [line for line in on_grid if passes(HIDDEN_C22["id_u"], np.asarray(line.get_ydata(), dtype=float)[idx].tolist())]
    cls = [line for line in on_grid if passes(HIDDEN_C22["id_c"], np.asarray(line.get_ydata(), dtype=float)[idx].tolist())]
    if not general or not cls:
        problems.append("il faut tracer aussi p_u et p_c, sur XS_22")
    if ax.get_legend() is None:
        problems.append("il faut une légende (label=…, puis ax.legend())")
    else:
        if (general and not _GENERAL_NAME_C22.search(general[0].get_label())) or (
                cls and not _CLASS_NAME_C22.search(cls[0].get_label())):
            problems.append("la légende doit nommer p_u et p_c")
        if any(line is not None and not math.isclose(label_w_c22(line.get_label()) or math.nan, w)
               for line, w in zip(lines, ws)):
            problems.append("la légende doit nommer le w de chaque loi guidée (label=f\"w = {w}\")")
    if not ax.get_xlabel() or not ax.get_ylabel():
        problems.append("il faut des noms d'axes")
    return problems


with checked("MB5.22"):
    results_22 = []
    report_22 = reporter(results_22, stop=False)
    idx_c22 = HIDDEN_C22["idx"]
    main_c22 = [density_c22("Ex MB5.22 : guided_22", XS_22, w) for w in (0.25, 1.75, 3.5)]
    report_22(passes(HIDDEN_C22["id_main"], [d[idx_c22].tolist() for d in main_c22]),
              "guided_22 (w = 0,25, 1,75 et 3,5, sur XS_22) : les trois densités",
              "guided_22 (w = 0,25, 1,75 et 3,5, sur XS_22) : ce ne sont pas les densités de p_c^{1+w} p_u^{−w}, "
              "normalisées par np.trapezoid sur la grille reçue")
    hidden_c22 = [density_c22("Ex MB5.22 : guided_22 (appel caché)", XS_22, w) for w in HIDDEN_C22["ws"]]
    grid_c22 = np.linspace(*HIDDEN_C22["grid"])
    other_c22 = [density_c22("Ex MB5.22 : guided_22 (appel caché)", grid_c22, w, general=HIDDEN_C22["general"],
                             cls=HIDDEN_C22["cls"]) for w in HIDDEN_C22["other_ws"]]
    report_22(passes(HIDDEN_C22["id_hidden"], [d[idx_c22].tolist() for d in hidden_c22])
              and passes(HIDDEN_C22["id_other"], [d[HIDDEN_C22["idx_other"]].tolist() for d in other_c22]),
              "des appels cachés de guided_22 (d'autres w, dans un autre ordre ; un autre mélange, sur une autre grille)",
              "des appels cachés de guided_22 (d'autres w, dans un autre ordre ; un autre mélange, sur une autre grille) : "
              "ta fonction doit se servir des xs, w, general et cls reçus")
    fig_22, ax_22 = plt.subplots(figsize=(9, 4.5))
    try:
        drawn_22 = []
        opened_22 = drawn(lambda: drawn_22.append(call_safely("Ex MB5.22 : draw_guided_22", draw_guided_22, ax_22,
                                                              (0.25, 1.75, 3.5))))
        problems_22 = figure_why_c22(ax_22, (0.25, 1.75, 3.5), drawn_22[0], HIDDEN_C22["id_main"])
        report_22(not problems_22, "draw_guided_22 (w = 0,25, 1,75 et 3,5) : p_u, p_c, les trois lois guidées, la légende "
                  "et les noms d'axes", "draw_guided_22 : " + " ; ".join(problems_22))
        fig_c22, axes_c22 = plt.subplots(1, 3)          # the 3rd axes is the current one: plt.plot would draw there
        try:
            hidden_drawn_c22 = []
            opened_22 += drawn(lambda: hidden_drawn_c22.append(call_safely(
                "Ex MB5.22 : draw_guided_22 (appel caché)", draw_guided_22, axes_c22[0], tuple(HIDDEN_C22["ws"]))))
            problems_c22 = figure_why_c22(axes_c22[0], HIDDEN_C22["ws"], hidden_drawn_c22[0], HIDDEN_C22["id_hidden"])
            elsewhere_22 = bool(axes_c22[2].lines or axes_c22[2].collections or axes_c22[2].get_legend())
        finally:
            plt.close(fig_c22)
        report_22(not problems_c22, "un appel caché de draw_guided_22 (d'autres w, dans un autre ordre) est juste aussi",
                  "un appel caché de draw_guided_22 (d'autres w, dans un autre ordre) : " + " ; ".join(problems_c22))
        report_22(not opened_22 and not elsewhere_22, "draw_guided_22 dessine dans les axes reçus",
                  "draw_guided_22 doit dessiner dans les axes reçus (ax.plot, ax.legend…), sans ouvrir de figure ni "
                  "dessiner dans l'axe courant (plt.plot, plt.legend…)")
    except BaseException:
        plt.close(fig_22)
        raise
    fig_22.tight_layout()
    plt.show()
    verdict("MB5.22", all(results_22) and len(results_22) == 5, "ta loi guidée et ta figure sont justes, sur les appels du "
            "notebook et sur des appels cachés.", "relis les lignes ❌ ci-dessus.")

guided_ok_22 = bool(results_22) and all(results_22[:2])


def hint_22(value):
    """A targeted hint for a) to c): guided_22 first."""
    return None if guided_ok_22 else "les moments se calculent sur les densités de guided_22 : corrige-la d'abord"


'''

NOTE_22 = (r"`guided_22` : `lg = (1 + w) * log p_c - w * log p_u` (le logarithme de $p_u$ par un log-sum-exp), "
           r"`d = np.exp(lg - lg.max())`, puis `d / np.trapezoid(d, xs)`. a) $(1{,}617613 ;\ 1{,}657115 ;\ 1{,}676298)$ ; "
           r"b) $(0{,}818055 ;\ 0{,}782353 ;\ 0{,}767596)$ ; c) $\approx 0{,}0027$, contre $0{,}0279$ pour $p_c$.")

MB5_22 = ex(
    "MB5.22", "calculer et tracer des lois guidées $p_c^{1+w}p_u^{-w}$ sur une grille, et voir ce que $w$ resserre et "
    "déplace.", "fiche §7 ; M02a (méthode des trapèzes), M05a (log-sum-exp) ; Ex MB5.7", note=NOTE_22, given=GIVEN_22,
    body=r"""La loi générale est le mélange $p_u = 0{,}55\,\mathcal{N}(-1{,}8 ;\ 0{,}5) + 0{,}45\,\mathcal{N}(1{,}6 ;\ 0{,}7)$, à deux bosses (`GENERAL_22`), et la loi de la classe est $p_c = \mathcal{N}(1{,}6 ;\ 0{,}7)$ (`CLASS_22`). Sur la grille `XS_22` (`np.linspace(-8, 8, 3201)`), écris `guided_22(xs, w, general=GENERAL_22, cls=CLASS_22)`, qui rend la densité normalisée de $p_c^{1+w}p_u^{-w}$ sur la grille `xs` reçue : calcule son logarithme, retire son maximum avant l'exponentielle, puis normalise par `np.trapezoid` (SciPy est permis, `scipy.stats.norm` et `scipy.special.logsumexp` compris) ; puis `draw_guided_22(ax, ws)`, qui trace dans les axes reçus, sur `XS_22`, $p_u$, $p_c$ et la loi guidée pour chaque $w$ de `ws`, avec une légende qui nomme chaque courbe ($p_u$, $p_c$, et la valeur de $w$ de chaque loi guidée) et des noms d'axes, et rend la liste des densités guidées tracées (une par $w$, dans l'ordre de `ws`). La fonction dessine dans les axes reçus, sans ouvrir de figure.

Sur une échelle linéaire, les trois lois guidées se superposent presque à $p_c$ : tu peux ajouter un second axe en échelle logarithmique, `ax.set_yscale("log")`, pour voir la masse quitter le côté de l'autre bosse.

La vérification appelle `draw_guided_22` avec $w = 0{,}25$, $1{,}75$ et $3{,}5$, affiche la figure, et essaie tes fonctions sur des appels cachés (d'autres $w$, dans un autre ordre ; un autre mélange, sur une autre grille) ; `guided_22` ne modifie pas la grille reçue. Relève, pour $w = 0{,}25$, $1{,}75$ et $3{,}5$, avec `np.trapezoid` sur `XS_22` :
- a) la moyenne de la loi guidée, $\int x\,d(x)\,\mathrm{d}x$ (une liste de 3 nombres) ;
- b) son écart-type, la racine de $\int (x - \text{moyenne})^2\,d(x)\,\mathrm{d}x$ (une liste de 3 nombres) ;
- c) pour $w = 3{,}5$ seulement, sa masse sur $x < 0$, le côté de l'autre bosse : `np.trapezoid(np.where(XS_22 < 0, d, 0), XS_22)`, où `d` est la densité sur la grille (un nombre).""",
    todo='''def guided_22(xs, w, general=GENERAL_22, cls=CLASS_22):
    """The density on the grid xs of the guided law, proportional to p_c^(1 + w) p_u^(-w), normalized by np.trapezoid:
    p_u is the mixture general = (weights, means, variances), p_c the Gaussian cls = (mean, variance)."""
    raise NotImplementedError("guided_22 n'est pas encore écrite (04_indices.md si tu bloques)")


def draw_guided_22(ax, ws):
    """In the axes ax, on the grid XS_22: p_u, p_c and the guided law for each w of ws, with a legend that names each
    curve and axis labels. Returns the list of the guided densities drawn (one per w, in the order of ws). Opens no
    figure."""
    raise NotImplementedError("draw_guided_22 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB5_22a = answer_MB5_22b = answer_MB5_22c = ...
with wbm.attempt("MB5.22"):          # your functions: ⏳ while they are not written
    answer_MB5_22a = ...  # a) a list of 3 numbers, as computed: the means of the guided laws for w = 0.25, 1.75, 3.5
    answer_MB5_22b = ...  # b) a list of 3 numbers, as computed: their standard deviations
    answer_MB5_22c = ...  # c) a number, as computed: for w = 3.5, the mass on x < 0''',
    check=CHECK_22 + answers_check("MB5.22", "abc", hints={letter: "hint_22" for letter in "abc"}),
    solution='''from scipy.special import logsumexp
from scipy.stats import norm


def log_mixture_22(xs, weights, means, variances):
    """ln of the density of a mixture of Gaussians at the points xs (a log-sum-exp over the components)."""
    return logsumexp([math.log(p) + norm.logpdf(xs, m, math.sqrt(v)) for p, m, v in zip(weights, means, variances)],
                     axis=0)


def guided_22(xs, w, general=GENERAL_22, cls=CLASS_22):
    """The density on the grid xs of the guided law, proportional to p_c^(1 + w) p_u^(-w), normalized by np.trapezoid:
    p_u is the mixture general = (weights, means, variances), p_c the Gaussian cls = (mean, variance)."""
    xs = np.asarray(xs, dtype=float)
    lg = (1 + w) * norm.logpdf(xs, cls[0], math.sqrt(cls[1])) - w * log_mixture_22(xs, *general)
    d = np.exp(lg - lg.max())
    return d / np.trapezoid(d, xs)


def draw_guided_22(ax, ws):
    """In the axes ax, on the grid XS_22: p_u, p_c and the guided law for each w of ws, with a legend that names each
    curve and axis labels. Returns the list of the guided densities drawn (one per w, in the order of ws). Opens no
    figure."""
    ax.plot(XS_22, np.exp(log_mixture_22(XS_22, *GENERAL_22)), color="0.55", lw=1.6, label="$p_u$, la loi générale")
    ax.plot(XS_22, norm.pdf(XS_22, CLASS_22[0], math.sqrt(CLASS_22[1])), "k--", lw=1.4, label="$p_c$, la classe")
    curves = []
    for w in ws:
        d = guided_22(XS_22, w)
        ax.plot(XS_22, d, lw=1.6, label=f"loi guidée, w = {w:g}".replace(".", ","))
        curves.append(d)
    ax.set_xlim(-5, 5)
    ax.set_xlabel("x")
    ax.set_ylabel("densité")
    ax.legend(fontsize=8)
    return curves


def moments_22(d):
    mean = float(np.trapezoid(XS_22 * d, XS_22))
    return mean, math.sqrt(float(np.trapezoid((XS_22 - mean) ** 2 * d, XS_22)))


densities_22 = [guided_22(XS_22, w) for w in (0.25, 1.75, 3.5)]
answer_MB5_22a = [moments_22(d)[0] for d in densities_22]
answer_MB5_22b = [moments_22(d)[1] for d in densities_22]
answer_MB5_22c = float(np.trapezoid(np.where(XS_22 < 0, densities_22[2], 0), XS_22))
class_mass_22 = float(norm.cdf(0, CLASS_22[0], math.sqrt(CLASS_22[1])))
print("a)", np.round(answer_MB5_22a, 6).tolist(), " b)", np.round(answer_MB5_22b, 6).tolist(),
      " c)", round(answer_MB5_22c, 6), f"(p_c : {class_mass_22:.4f})")''',
    record='''from scipy.stats import norm as norm_22r


def density_22r(xs, w, general=((0.55, 0.45), (-1.8, 1.6), (0.5, 0.7)), cls=(1.6, 0.7), normalise=True):
    """The oracle: the densities themselves, p_c^(1 + w) p_u^(-w) (no logarithm: on these grids no density underflows),
    normalized by the trapezoids; normalise=False: divided by their maximum only (the logarithm minus its maximum,
    exponentiated, and never normalized)."""
    xs = np.asarray(xs, dtype=float)
    pu = sum(p * norm_22r.pdf(xs, m, math.sqrt(v)) for p, m, v in zip(*general))
    pc = norm_22r.pdf(xs, cls[0], math.sqrt(cls[1]))
    d = pc ** (1 + w) * pu ** (-w)
    return d / np.trapezoid(d, xs) if normalise else d / d.max()


grid_22r = np.linspace(-8, 8, 3201)


def moments_22r(d):
    mean = float(np.trapezoid(grid_22r * d, grid_22r))
    return [mean, math.sqrt(float(np.trapezoid((grid_22r - mean) ** 2 * d, grid_22r)))]


weights_22r = (0.25, 1.75, 3.5)
right_22r = [moments_22r(density_22r(grid_22r, w)) for w in weights_22r]
raw_22r = [moments_22r(density_22r(grid_22r, w, normalise=False)) for w in weights_22r]
wbm.record("MB5.22a", [m[0] for m in right_22r], decimals=7,
           mistakes={"la loi guidée se normalise : divise par `np.trapezoid(d, xs)` avant de calculer ses moments": [m[0] for m in raw_22r]})
wbm.record("MB5.22b", [m[1] for m in right_22r], decimals=6,
           mistakes={"la loi guidée se normalise : divise par `np.trapezoid(d, xs)` avant de calculer ses moments": [m[1] for m in raw_22r]})
mass_22r = float(np.trapezoid(np.where(grid_22r < 0, density_22r(grid_22r, 3.5), 0), grid_22r))
wbm.record("MB5.22c", mass_22r, decimals=6,
           mistakes={"c) demande la masse de la loi guidée pour w = 3,5, pas celle de p_c":
                         float(np.trapezoid(np.where(grid_22r < 0, norm_22r.pdf(grid_22r, 1.6, math.sqrt(0.7)), 0),
                                            grid_22r)),
                     "c) demande la masse sur x < 0, le côté de l'autre bosse": 1 - mass_22r,
                     "la loi guidée se normalise : divise par `np.trapezoid(d, xs)` avant de calculer ses moments":
                         float(np.trapezoid(np.where(grid_22r < 0, density_22r(grid_22r, 3.5, normalise=False), 0),
                                            grid_22r))})
HIDDEN_22r = __HIDDEN_C22__                                                  # the hidden calls of the check
idx_22r = HIDDEN_22r["idx"]
wbm.record(HIDDEN_22r["id_main"], [density_22r(grid_22r, w)[idx_22r].tolist() for w in weights_22r], decimals=6)
wbm.record(HIDDEN_22r["id_hidden"], [density_22r(grid_22r, w)[idx_22r].tolist() for w in HIDDEN_22r["ws"]], decimals=6)
other_grid_22r = np.linspace(*HIDDEN_22r["grid"])
wbm.record(HIDDEN_22r["id_other"], [density_22r(other_grid_22r, w, HIDDEN_22r["general"], HIDDEN_22r["cls"])[
    HIDDEN_22r["idx_other"]].tolist() for w in HIDDEN_22r["other_ws"]], decimals=6)
wbm.record(HIDDEN_22r["id_u"], sum(p * norm_22r.pdf(grid_22r, m, math.sqrt(v)) for p, m, v in
                                   zip((0.55, 0.45), (-1.8, 1.6), (0.5, 0.7)))[idx_22r].tolist(), decimals=6)
wbm.record(HIDDEN_22r["id_c"], norm_22r.pdf(grid_22r, 1.6, math.sqrt(0.7))[idx_22r].tolist(), decimals=6)''',
    after=[
        ("solution", CHECK_22 + answers_check("MB5.22", "abc", hints={letter: "hint_22" for letter in "abc"})),
        look("que devient, pour $w = 3{,}5$, la masse du côté de l'autre bosse, comparée à celle de $p_c$ ? Pourquoi la "
             "moyenne s'écarte-t-elle de $1{,}6$, et de quel côté ? Pourquoi ces lois existent-elles pour tout "
             "$w \\ge 0$ ?"),
    ],
)

PART_B = Part("B", "Une bibliothèque, prédire, mesurer, dessiner",
              "Fiche §5, §7, §8 et §9. Une croissance logistique suivie par `solve_ivp` et par tes deux méthodes ; le "
              "débruiteur d'un nuage de points quand le bruit s'efface ; le chemin droit vers une loi gaussienne ; des lois "
              "guidées sur une grille.", exercises=[MB5_19, MB5_20, MB5_21, MB5_22])

# ---------------------------------------------------------------------------
# Notebook exercises: debug, test (MB5.23, MB5.24)
# ---------------------------------------------------------------------------
GIVEN_23 = '''# The colleague's code
def bridge_bad(x0, xT, Vs, VT):
    """The mean and the variance of a random walk at the time of cumulated variance Vs, given its value x0 at the start
    (cumulated variance 0) and its value xT at the time of cumulated variance VT (the bridge)."""
    weight = Vs / VT
    return weight * x0 + (1 - weight) * xT, Vs * (VT - Vs) / VT


def denoiser_bad(y, a, b, weights, means, variances):
    """E[x | y] for the measurement y = a x + b n, when x follows the mixture of the Gaussians N(means[k], variances[k])
    of weights weights[k] (variances > 0)."""
    y = np.asarray(y, dtype=float)
    w, m, v = (np.asarray(part, dtype=float) for part in (weights, means, variances))
    gap = y.reshape(-1, 1) - a * m                                       # y - a mu_k, one row per measurement
    logs = np.log(w) - 0.5 * np.log(2 * np.pi * v) - gap ** 2 / (2 * v)  # the responsibilities, by logarithms
    resp = np.exp(logs - logs.max(axis=1, keepdims=True))
    resp = resp / resp.sum(axis=1, keepdims=True)
    inside = m + a * v / (a ** 2 * v + b ** 2) * gap                     # E[x | y, k]
    return (resp * inside).sum(axis=1).reshape(y.shape)


def euler_bad(f, x0, t0, t1, n_steps):
    """The points of Euler's method for x' = f(t, x), from x(t0) = x0 to the final time t1, in n_steps steps."""
    h = (t1 - t0) / n_steps
    x = np.array(x0, dtype=float)
    points = [x.copy()]
    for k in range(n_steps):
        x = x + h * f(t0, x)
        points.append(x.copy())
    return np.array(points)


# The colleague's checks: all pass
mean_23, var_23 = bridge_bad(1.0, 7.0, 3.0, 6.0)          # halfway through a walk of equal steps
print("(1)", math.isclose(mean_23, 4.0) and math.isclose(var_23, 1.5),
      "(attendu True : à mi-chemin, la moyenne des deux valeurs et la variance V_s(V_T − V_s)/V_T)")
one_23 = float(denoiser_bad(2.0, 1.5, 0.7, [1.0], [0.4], [0.9]))   # one Gaussian: the linear Gaussian model of M25a
print("(2)", math.isclose(one_23, 0.4 + 1.5 * 0.9 * (2.0 - 1.5 * 0.4) / (1.5 ** 2 * 0.9 + 0.7 ** 2)),
      "(attendu True : une seule gaussienne, la formule de M25a)")
path_23 = euler_bad(lambda t, x: -x / 3, 3.0, 0.0, 2.0, 5)          # each step multiplies x by 1 - h/3
print("(3)", bool(np.allclose(path_23, 3.0 * (1 - 0.4 / 3) ** np.arange(6))),
      "(attendu True : chaque pas multiplie x par 1 − h/3)")'''

CHECK_23 = '''CASES_C23 = __CASES_C23__   # the hidden bridges, mixtures and fields, and the sub-ID of the bridges expected

results_23, parts_23 = [], []
MYMATH_C23 = list(getattr(mymath, "__path__", [])) + list(getattr(REF, "__path__", []))   # the folders of mymath
TWINS_C23 = set()                                  # the functions of gaussian_paths.py (yours, the reference's)
for _folder_c23 in MYMATH_C23:
    _file_c23 = os.path.join(_folder_c23, "gaussian_paths.py")
    if os.path.exists(_file_c23):
        TWINS_C23 |= code_keys_of_file(_file_c23)
FIELDS_C23 = {"wave": lambda t, x: 0.75 * np.cos(1.3 * t) - 0.45 * x,     # hidden fields that depend on the time
              "ramp": lambda t, x: 0.6 * t - 0.25 * x * x}


def report_23(ok, success, failure):
    results_23.append(bool(ok))
    print(("✅ " + success) if ok else ("❌ " + failure))


def call_23(part, name, function, *args):
    """function(*args), without mymath; an error of the learner's code becomes one ❌ line that names the function."""
    try:
        with code_from(MYMATH_C23, twins=TWINS_C23) as seen:
            got = function(*args)
    except (NotImplementedError, MymathMissingError):
        raise
    except Exception as exc:  # noqa: BLE001 - the learner's error, reported with the name of the function
        report_23(False, "", f"({part}) {name} : ton code lève {type(exc).__name__} : {str(exc)[:160]}")
        parts_23.append(part)
        raise StopCheck from None
    if seen:
        report_23(False, "", f"({part}) {name} appelle mymath ({seen[0]}) : l'énoncé demande la correction sans mymath, "
                  "en corrigeant le code du collègue")
        parts_23.append(part)
        raise StopCheck
    return got


def unchanged_23(arrays, copies):
    return all(np.array_equal(a, c) for a, c in zip(arrays, copies))


with checked("MB5.23"):                                       # (1) bridge_fixed
    got_c23 = []
    for case_c23 in CASES_C23["bridges"]:
        pair_c23 = as_floats(call_23(1, "bridge_fixed", bridge_fixed, *case_c23))
        got_c23.append(pair_c23.tolist() if pair_c23 is not None and pair_c23.shape == (2,) else None)
    if any(pair is None for pair in got_c23):
        why_c23 = "bridge_fixed rend un couple (moyenne, variance) de deux nombres"
    elif passes(CASES_C23["id"], got_c23):
        why_c23 = ""
    elif all(math.isclose(pair[0], bridge_bad(*case)[0], rel_tol=1e-9, abs_tol=1e-12)
             for pair, case in zip(got_c23, CASES_C23["bridges"])):
        why_c23 = "ta correction met encore le poids V_s/V_T sur x_0 : il va avec x_T, la valeur à l'instant de V_T"
    else:
        why_c23 = ("sur d'autres ponts, ce n'est pas la moyenne x_0 + (V_s/V_T)(x_T − x_0) et la variance "
                   "V_s(V_T − V_s)/V_T du pont d'une marche aléatoire")
    report_23(not why_c23, "(1) bridge_fixed : d'autres ponts, dont des instants proches de la fin",
              f"(1) bridge_fixed : {why_c23}")
    parts_23.append(1)

with checked("MB5.23"):                                       # (2) denoiser_fixed, compared with the reference
    wrong_c23 = []
    for y_c23, a_c23, b_c23, w_c23, m_c23, v_c23 in CASES_C23["mixtures"]:
        inputs_c23 = [np.array(y_c23), np.array(w_c23), np.array(m_c23), np.array(v_c23)]   # non-dyadic floats
        copies_c23 = [x.copy() for x in inputs_c23]
        got_c23 = as_floats(call_23(2, "denoiser_fixed", denoiser_fixed, inputs_c23[0], a_c23, b_c23, *inputs_c23[1:]))
        want_c23 = ref_gp.posterior_mean_mixture(copies_c23[0], a_c23, b_c23, *copies_c23[1:])
        if not unchanged_23(inputs_c23, copies_c23):
            wrong_c23.append("ta fonction modifie un tableau reçu : travaille sur une copie")
        elif got_c23 is None or got_c23.shape != want_c23.shape:
            wrong_c23.append("denoiser_fixed rend un tableau de la forme de y")
        elif matches(got_c23, want_c23, rtol=1e-9, atol=1e-9):
            continue
        elif matches(got_c23, denoiser_bad(copies_c23[0], a_c23, b_c23, *copies_c23[1:]), rtol=1e-9, atol=1e-9):
            wrong_c23.append("ta correction calcule encore les responsabilités avec la variance s_k² du signal seule : la "
                             "loi de y sachant la composante k a la variance a² s_k² + b²")
        else:
            wrong_c23.append("sur des mélanges de deux composantes ou plus, ce n'est pas E[x | y] : les responsabilités "
                             "viennent de la loi N(a μ_k, a² s_k² + b²) de y sachant la composante k")
    report_23(not wrong_c23, "(2) denoiser_fixed : des mélanges cachés de deux à quatre composantes, des mesures en "
              "tableau", "(2) denoiser_fixed : " + " ; ".join(dict.fromkeys(wrong_c23)))
    parts_23.append(2)

with checked("MB5.23"):                                       # (3) euler_fixed, compared with the reference
    wrong_c23 = []
    for name_c23, x0_c23, t0_c23, t1_c23, n_c23 in CASES_C23["fields"]:
        start_c23 = np.array(x0_c23)                          # non-dyadic floats: a change in place would show
        got_c23 = as_floats(call_23(3, "euler_fixed", euler_fixed, FIELDS_C23[name_c23], start_c23, t0_c23, t1_c23,
                                    n_c23))
        want_c23 = ref_gp.euler_ode(FIELDS_C23[name_c23], np.array(x0_c23), t0_c23, t1_c23, n_c23)
        if not np.array_equal(start_c23, np.array(x0_c23)):
            wrong_c23.append("ta fonction modifie le point de départ reçu : travaille sur une copie")
        elif got_c23 is None or got_c23.shape != want_c23.shape:
            wrong_c23.append("euler_fixed rend les N + 1 points, de forme (N + 1,) + la forme de x0")
        elif matches(got_c23, want_c23, rtol=1e-9, atol=1e-9):
            continue
        elif matches(got_c23, euler_bad(FIELDS_C23[name_c23], np.array(x0_c23), t0_c23, t1_c23, n_c23), rtol=1e-9,
                     atol=1e-9):
            wrong_c23.append("le temps du champ n'avance pas encore : le pas k lit la vitesse en t_k = t_0 + k h")
        else:
            wrong_c23.append("sur des champs qui dépendent du temps, ce ne sont pas les points de la méthode d'Euler, "
                             "x_{k+1} = x_k + h f(t_k, x_k)")
    report_23(not wrong_c23, "(3) euler_fixed : des champs cachés qui dépendent du temps, dans les deux sens du temps",
              "(3) euler_fixed : " + " ; ".join(dict.fromkeys(wrong_c23)))
    parts_23.append(3)

if len(set(parts_23)) == 3:
    verdict("MB5.23", all(results_23), "les trois fonctions corrigées passent tous les cas.", "relis les lignes ❌ ci-dessus.")'''

NOTE_23 = (r"(1) Le poids $\frac{V_s}{V_T}$ va avec $x_T$ : `(1 - weight) * x0 + weight * xT`. a) $(7{,}235294 ;\ "
           r"4{,}764706)$. (2) Les responsabilités demandent la loi de $y$ sachant la composante, de variance `a ** 2 * v "
           r"+ b ** 2`. b) $(0{,}086508 ;\ 1{,}608911 ;\ -0{,}127978 ;\ 1{,}811618)$. (3) Le temps du champ avance : "
           r"`f(t0 + k * h, x)`. c) $(1{,}175583 ;\ 0{,}087791)$.")

MB5_23 = ex(
    "MB5.23", "reconnaître trois erreurs classiques (des poids inversés dans un pont, le bruit oublié dans les "
    "responsabilités, un temps qui n'avance pas), qui passent une vérification mal choisie, puis les corriger.",
    "fiche §2, §5 et §8 ; Ex MB5.3, MB5.17, MB5.18", note=NOTE_23, given=GIVEN_23,
    body=r"""Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe (cellule fournie) :
1. `bridge_bad(x0, xT, Vs, VT)` doit rendre la moyenne et la variance du pont d'une marche aléatoire. Près de la fin de la marche ($V_s$ proche de $V_T$), sa moyenne reste près de $x_0$ au lieu de rejoindre $x_T$. Il l'a vérifiée au milieu d'une marche de pas égaux.
2. `denoiser_bad(y, a, b, weights, means, variances)` doit rendre $\mathbb{E}[x \mid y]$ pour un mélange. Sur un mélange de deux composantes, ses responsabilités ne changent pas quand le bruit $b$ grandit : elle fait autant confiance à une mesure très bruitée qu'à une mesure presque exacte. Il l'a vérifiée sur un mélange à une seule composante.
3. `euler_bad(f, x0, t0, t1, n_steps)` doit suivre la méthode d'Euler. Sur $x' = t$ depuis $t_0 = 0$, elle rend $x_0$ quelle que soit la durée. Il l'a vérifiée sur $x' = -\frac x3$.

À faire : trouve et corrige chaque erreur dans le code du collègue lui-même : les fonctions corrigées s'appellent `bridge_fixed`, `denoiser_fixed` et `euler_fixed`, avec les mêmes arguments, et n'appellent **pas** `mymath` (la vérification le contrôle). Puis réponds :
- a) pour le phoque de MB5.3 (`SEAL_3`, cellule de données), la moyenne de la position à 11 h par la fonction corrigée, puis par la fonction fautive (une liste de 2 nombres) ;
- b) pour le mélange $0{,}4\,\mathcal{N}(-1 ;\ 0{,}3) + 0{,}6\,\mathcal{N}(2{,}5 ;\ 0{,}6)$ mesuré par $y = 1{,}2\,x + 0{,}9\,n$, $\mathbb{E}[x \mid y]$ pour $y = 0{,}4$ et $1{,}4$, par la fonction corrigée, puis par la fonction fautive (une liste de 4 nombres) ;
- c) $x' = t - x$, $x(0) = 1$, sur $[0, 2]$ en six pas : le point atteint en $t = 2$ par la fonction corrigée, puis par la fonction fautive (une liste de 2 nombres).

Dans ta copie : pour chacune des trois erreurs, pourquoi la vérification du collègue ne la voyait pas. La vérification essaie aussi tes fonctions corrigées sur des cas cachés : d'autres ponts, des mélanges de deux composantes ou plus, des champs qui dépendent du temps, et des tableaux qu'elles ne doivent pas modifier.""",
    todo='''def bridge_fixed(x0, xT, Vs, VT):
    """The mean and the variance of a random walk at the time of cumulated variance Vs, given its value x0 at the start
    (cumulated variance 0) and its value xT at the time of cumulated variance VT (the bridge)."""
    raise NotImplementedError("bridge_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def denoiser_fixed(y, a, b, weights, means, variances):
    """E[x | y] for the measurement y = a x + b n, when x follows the mixture of the Gaussians N(means[k], variances[k])
    of weights weights[k] (variances > 0)."""
    raise NotImplementedError("denoiser_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def euler_fixed(f, x0, t0, t1, n_steps):
    """The points of Euler's method for x' = f(t, x), from x(t0) = x0 to the final time t1, in n_steps steps."""
    raise NotImplementedError("euler_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB5_23a = answer_MB5_23b = answer_MB5_23c = ...
with wbm.attempt("MB5.23"):          # your three functions: ⏳ while they are not written
    answer_MB5_23a = ...  # a) a list of 2 numbers, as computed: the mean at 11 h by bridge_fixed, then by the WRONG bridge_bad
    answer_MB5_23b = ...  # b) a list of 4 numbers, as computed: denoiser_fixed at y = 0.4 and 1.4, then the WRONG denoiser_bad
    answer_MB5_23c = ...  # c) a list of 2 numbers, as computed: the point at t = 2 by euler_fixed, then by the WRONG euler_bad''',
    check=answers_check("MB5.23", "abc") + "\n\n" + CHECK_23,
    solution='''def bridge_fixed(x0, xT, Vs, VT):
    """The mean and the variance of a random walk at the time of cumulated variance Vs, given its value x0 at the start
    (cumulated variance 0) and its value xT at the time of cumulated variance VT (the bridge)."""
    weight = Vs / VT
    return (1 - weight) * x0 + weight * xT, Vs * (VT - Vs) / VT               # the weight Vs / VT goes with xT


def denoiser_fixed(y, a, b, weights, means, variances):
    """E[x | y] for the measurement y = a x + b n, when x follows the mixture of the Gaussians N(means[k], variances[k])
    of weights weights[k] (variances > 0)."""
    y = np.asarray(y, dtype=float)
    w, m, v = (np.asarray(part, dtype=float) for part in (weights, means, variances))
    spread = a ** 2 * v + b ** 2                                         # the variance of y given the component
    gap = y.reshape(-1, 1) - a * m
    logs = np.log(w) - 0.5 * np.log(2 * np.pi * spread) - gap ** 2 / (2 * spread)
    resp = np.exp(logs - logs.max(axis=1, keepdims=True))
    resp = resp / resp.sum(axis=1, keepdims=True)
    inside = m + a * v / spread * gap
    return (resp * inside).sum(axis=1).reshape(y.shape)


def euler_fixed(f, x0, t0, t1, n_steps):
    """The points of Euler's method for x' = f(t, x), from x(t0) = x0 to the final time t1, in n_steps steps."""
    h = (t1 - t0) / n_steps
    x = np.array(x0, dtype=float)
    points = [x.copy()]
    for k in range(n_steps):
        x = x + h * f(t0 + k * h, x)                                     # the time of step k
        points.append(x.copy())
    return np.array(points)


hours_8_11_23 = 3 * SEAL_3["var_8h_11h"]                                  # V at 11 h
hours_8_16_23 = hours_8_11_23 + 5 * SEAL_3["var_11h_16h"]                 # V at 16 h
answer_MB5_23a = [bridge_fixed(SEAL_3["x8h"], SEAL_3["x16h"], hours_8_11_23, hours_8_16_23)[0],
                  bridge_bad(SEAL_3["x8h"], SEAL_3["x16h"], hours_8_11_23, hours_8_16_23)[0]]
mixture_23 = ([0.4, 0.6], [-1.0, 2.5], [0.3, 0.6])
answer_MB5_23b = (denoiser_fixed([0.4, 1.4], 1.2, 0.9, *mixture_23).tolist()
                  + denoiser_bad([0.4, 1.4], 1.2, 0.9, *mixture_23).tolist())
answer_MB5_23c = [float(euler_fixed(lambda t, x: t - x, 1.0, 0.0, 2.0, 6)[-1]),
                  float(euler_bad(lambda t, x: t - x, 1.0, 0.0, 2.0, 6)[-1])]
print("a)", np.round(answer_MB5_23a, 6).tolist(), " b)", np.round(answer_MB5_23b, 6).tolist(),
      " c)", np.round(answer_MB5_23c, 6).tolist())''',
    record='''from fractions import Fraction as F_23r

from scipy import integrate as integrate_23r
from scipy import stats as stats_23r


def bridge_23r(x0, xT, Vs, VT, swapped=False):
    """The oracle: the bridge in exact fractions (swapped: the weight Vs/VT on x0, the colleague's error)."""
    x0, xT, Vs, VT = (F_23r(str(v)) for v in (x0, xT, Vs, VT))
    mean = xT + Vs / VT * (x0 - xT) if swapped else x0 + Vs / VT * (xT - x0)
    return [float(mean), float(Vs * (VT - Vs) / VT)]


right_a_23r, bad_a_23r = bridge_23r(3, 9, 6, "8.5")[0], bridge_23r(3, 9, 6, "8.5", swapped=True)[0]
wbm.record("MB5.23a", [right_a_23r, bad_a_23r], decimals=6,
           mistakes={"bridge_fixed met encore le poids V_s/V_T sur x_0 : il va avec x_T": [bad_a_23r, bad_a_23r],
                     "le second nombre est celui de la version FAUSSE, bridge_bad": [right_a_23r, right_a_23r],
                     "la version corrigée d'abord, puis la version fautive": [bad_a_23r, right_a_23r]})


def denoised_23r(y, alone=False, a=1.2, b=0.9, weights=(0.4, 0.6), means=(-1.0, 2.5), variances=(0.3, 0.6)):
    """The oracle: E[x | y] by integrating against the posterior density (scipy.integrate.quad); alone: the colleague's
    responsibilities, with the variance of the signal alone (written again)."""
    if alone:
        resp = [w * stats_23r.norm.pdf(y, a * m, math.sqrt(v)) for w, m, v in zip(weights, means, variances)]
        inside = [m + a * v / (a * a * v + b * b) * (y - a * m) for m, v in zip(means, variances)]
        return sum(r * e for r, e in zip(resp, inside)) / sum(resp)

    def density(x):
        return sum(w * stats_23r.norm.pdf(x, m, math.sqrt(v)) for w, m, v in zip(weights, means, variances)) \\
            * stats_23r.norm.pdf(y, a * x, b)

    top = integrate_23r.quad(lambda x: x * density(x), -30, 30, points=list(means), limit=400)[0]
    return top / integrate_23r.quad(density, -30, 30, points=list(means), limit=400)[0]


right_b_23r = [denoised_23r(y) for y in (0.4, 1.4)]
bad_b_23r = [denoised_23r(y, alone=True) for y in (0.4, 1.4)]
wbm.record("MB5.23b", right_b_23r + bad_b_23r, decimals=6,
           mistakes={"denoiser_fixed calcule encore les responsabilités avec la variance s_k² du signal seule":
                         bad_b_23r + bad_b_23r,
                     "les deux derniers nombres sont ceux de la version FAUSSE, denoiser_bad": right_b_23r + right_b_23r,
                     "la version corrigée d'abord, puis la version fautive": bad_b_23r + right_b_23r})


def euler_23r(times="start"):
    """The oracle: Euler for x' = t - x from x(0) = 1 on [0, 2] in six steps, exactly; times="frozen": the field read
    at t0 at every step (the colleague's error); "end": read at the end of each step; "middle": a midpoint step."""
    x, h = F_23r(1), F_23r(1, 3)
    for k in range(6):
        t = k * h
        if times == "middle":
            x = x + h * ((t + h / 2) - (x + h / 2 * (t - x)))
        else:
            x = x + h * ({"start": t, "frozen": 0, "end": t + h}[times] - x)
    return float(x)


right_c_23r, bad_c_23r = euler_23r(), euler_23r("frozen")
wbm.record("MB5.23c", [right_c_23r, bad_c_23r], decimals=4,
           mistakes={"euler_fixed lit encore le champ en t_0 à chaque pas": [bad_c_23r] * 2,
                     "le second nombre est celui de la version FAUSSE, euler_bad": [right_c_23r] * 2,
                     "la version corrigée d'abord, puis la version fautive": [bad_c_23r, right_c_23r],
                     "le pas k d'Euler lit le champ au début du pas, en (t_k, x_k), pas en t_(k+1)":
                         [euler_23r("end"), bad_c_23r],
                     "euler_fixed corrige le temps du champ, sans changer de méthode : un seul appel du champ par pas, "
                     "en (t_k, x_k)": [euler_23r("middle"), bad_c_23r]})
CASES_23r = __CASES_C23__                                                   # the hidden bridges of the check
wbm.record(CASES_23r["id"], [bridge_23r(*case) for case in CASES_23r["bridges"]], decimals=6)''',
    after=[
        ("solution", answers_check("MB5.23", "abc") + "\n\n" + CHECK_23),
        ("md", "**Après la vérification**, dans ta copie : pour chacune des trois erreurs, pourquoi la vérification du "
               "collègue ne la voyait-elle pas, et quelle vérification l'aurait vue ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB5.24 · a property test of a method of integration
# ---------------------------------------------------------------------------
CHECK_24 = '''def load_hidden_c24():
    """The two right methods of the check (solutions/challenges/mb5_24.py: reading it spoils 🔨 MB5.18)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("hidden_methods_c24", wbm.repo_root() / "solutions" / "challenges"
                                                  / "mb5_24.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


HIDDEN_C24 = load_hidden_c24()
euler_twin_c24, midpoint_twin_c24 = HIDDEN_C24.euler_twin, HIDDEN_C24.midpoint_twin


def middle_points_off_c24(f, x0, t0, t1, n_steps):
    """WRONG: the points of the midpoint method, those in between moved by 1e-3 k (N - k) (the first and the last are
    right)."""
    points = ref_gp.midpoint_ode(f, x0, t0, t1, n_steps)
    k = np.arange(n_steps + 1, dtype=float).reshape((-1,) + (1,) * (points.ndim - 1))
    return points + 1e-3 * k * (n_steps - k)


def one_step_only_c24(f, x0, t0, t1, n_steps):
    """WRONG from two steps on: the midpoint method with steps of length (t1 - t0) / N² (right for one step)."""
    return ref_gp.midpoint_ode(f, x0, t0, t0 + (t1 - t0) / n_steps, n_steps)


def unit_speed_c24(f, x0, t0, t1, n_steps):
    """WRONG unless the velocity is 0 or 1: Euler's method with the velocity squared."""
    return ref_gp.euler_ode(lambda t, x: np.asarray(f(t, x), dtype=float) ** 2, x0, t0, t1, n_steps)


def unit_slope_c24(f, x0, t0, t1, n_steps):
    """WRONG unless the field grows by 1 per unit of time: Euler's method plus h²/2 at each step."""
    h = (t1 - t0) / n_steps
    return ref_gp.euler_ode(lambda t, x: np.asarray(f(t, x), dtype=float) + h / 2, x0, t0, t1, n_steps)


def slightly_off_c24(f, x0, t0, t1, n_steps):
    """WRONG by more than 1e-9, but less than np.allclose's default tolerance (1e-8 + 1e-5 |x|): the points of the
    midpoint method, each point after the first moved by 5e-9 + 5e-6 |x_k|."""
    points = ref_gp.midpoint_ode(f, x0, t0, t1, n_steps)
    moved = points + 5e-9 + 5e-6 * np.abs(points)
    moved[0] = points[0]
    return moved


def frozen_time_c24(f, x0, t0, t1, n_steps):
    """WRONG for a field that depends on the time: Euler's method reading the field at t0 at each step."""
    return ref_gp.euler_ode(lambda t, x: f(t0, x), x0, t0, t1, n_steps)


def frozen_point_c24(f, x0, t0, t1, n_steps):
    """WRONG for a field that depends on x: Euler's method reading the field at the start x0 at each step."""
    start = np.array(x0, dtype=float)
    return ref_gp.euler_ode(lambda t, x: f(t, start.copy()), x0, t0, t1, n_steps)


def halfway_c24(f, x0, t0, t1, n_steps):
    """WRONG: Euler's method that stops halfway, at (t0 + t1) / 2 (its error does not tend to 0)."""
    return ref_gp.euler_ode(f, x0, t0, (t0 + t1) / 2, n_steps)


WRONG_C24 = [   # a hidden wrong method, the test that must refuse it, and the clause of the statement it tries
    (middle_points_off_c24, "constant_is_exact_24", "aux points intermédiaires (le premier et le dernier sont justes) : "
                                                    "vérifie chaque point rendu, avec plusieurs pas"),
    (middle_points_off_c24, "affine_is_exact_24", "aux points intermédiaires (le premier et le dernier sont justes) : "
                                                  "vérifie chaque point rendu, avec plusieurs pas"),
    (one_step_only_c24, "constant_is_exact_24", "dès deux pas (un seul pas est juste) : essaie plusieurs nombres de pas"),
    (one_step_only_c24, "affine_is_exact_24", "dès deux pas (un seul pas est juste) : essaie plusieurs nombres de pas"),
    (unit_speed_c24, "constant_is_exact_24", "sauf pour les vitesses 0 et 1 : essaie plusieurs vitesses, dont des "
                                             "négatives et des non entières"),
    (unit_slope_c24, "affine_is_exact_24", "sauf pour une pente κ₁ = 1 : essaie plusieurs champs κ₀ + κ₁ t"),
    (slightly_off_c24, "constant_is_exact_24", "de 5·10⁻⁹ + 5·10⁻⁶ |x| : la tolérance de l'énoncé est 10⁻⁹ (np.allclose a "
                                               "par défaut rtol = 1e-5 et atol = 1e-8)"),
    (slightly_off_c24, "affine_is_exact_24", "de 5·10⁻⁹ + 5·10⁻⁶ |x| : la tolérance de l'énoncé est 10⁻⁹ (np.allclose a "
                                             "par défaut rtol = 1e-5 et atol = 1e-8)"),
    (frozen_time_c24, "error_halves_24", "pour un champ qui dépend du temps (elle lit le champ en t_0, et son erreur ne "
                                         "tend pas vers 0) : ton champ dépend-il de t, et ton test exige-t-il un rapport "
                                         "entre 1,8 et 2,2 ?"),
    (frozen_point_c24, "error_halves_24", "pour un champ qui dépend de x (elle lit le champ au point de départ, et son "
                                          "erreur ne tend pas vers 0) : ton champ dépend-il de x, et ton test exige-t-il "
                                          "un rapport entre 1,8 et 2,2 ?"),
    (halfway_c24, "error_halves_24", "partout : son erreur au temps final ne tend pas vers 0 ; le rapport des erreurs "
                                     "doit être entre 1,8 et 2,2, pas seulement plus grand que 1"),
]

with checked("MB5.24"):
    results_24 = []
    report_24 = reporter(results_24, stop=False)
    TESTS_C24 = {"constant_is_exact_24": constant_is_exact_24, "affine_is_exact_24": affine_is_exact_24,
                 "error_halves_24": error_halves_24}
    # a test runs the method: it reads neither the method, nor the stack, nor the names of this cell
    refuse_peeking("MB5.24", TESTS_C24, globals(), private=("_c24", "_C24"))

    def anonymous_c24(method):
        """method under a neutral name: a test must judge what the method does, not what it is called."""
        def method_c24(f, x0, t0, t1, n_steps):
            return method(f, x0, t0, t1, n_steps)
        method_c24.__name__ = method_c24.__qualname__ = "method"
        return method_c24

    def verdict_c24(name, label, method):
        got = call_safely(f"Ex MB5.24 : {name}({label})", TESTS_C24[name], anonymous_c24(method))
        if not isinstance(got, (bool, np.bool_)):
            if isinstance(got, (int, np.integer)):
                what = f"{int(got)} (un entier)"
            elif isinstance(got, (float, np.floating)):
                what = f"{float(got):g} (un nombre)"
            else:
                what = shown(got)
            print(f"❌ Ex MB5.24 : {name}({label}) rend {what}, pas True ou False")
            raise StopCheck
        return bool(got)

    def verdicts_c24(label, method):
        return [verdict_c24(name, label, method) for name in TESTS_C24]

    on_ref_c24 = [verdicts_c24("euler_ode de la référence", ref_gp.euler_ode),
                  verdicts_c24("midpoint_ode de la référence", ref_gp.midpoint_ode)]
    report_24(passes("MB5.24a", on_ref_c24), "tes trois tests, sur euler_ode et midpoint_ode de la référence",
              "tes trois tests ne rendent pas, sur euler_ode et midpoint_ode de la référence, ce que dit la fiche §8 de "
              "ces deux méthodes : relis les propriétés de chacune (et, pour error_halves_24, prends N assez grand)")
    LIBRARY_FILES_C24 = [REF.gaussian_paths.__file__]
    try:
        LIBRARY_FILES_C24.append(mymath.gaussian_paths.__file__)          # your own gaussian_paths.py too
    except Exception:  # noqa: BLE001 - no module of yours yet: only the reference is watched
        pass

    def no_reference_c24(label, method):
        """The verdicts on a method that never calls gaussian_paths.py: a call comes from the test."""
        with code_from(LIBRARY_FILES_C24) as seen:
            got = verdicts_c24(label, method)
        if seen:
            print(f"❌ Ex MB5.24 : un de tes tests appelle {seen[0]} : il doit comparer la méthode à la solution exacte "
                  "de son champ, pas à euler_ode ou midpoint_ode (ceux de la référence ou les tiens)")
            raise StopCheck
        return got

    twins_c24 = [no_reference_c24("une autre écriture juste d'Euler", euler_twin_c24),
                 no_reference_c24("une autre écriture juste du point milieu", midpoint_twin_c24)]
    report_24(twins_c24 == on_ref_c24, "deux autres écritures justes des deux méthodes reçoivent les mêmes verdicts",
              "deux autres écritures justes des deux méthodes (les instants accumulés pas à pas : des arrondis de l'ordre de "
              "10⁻¹⁶) ne reçoivent pas les mêmes verdicts que euler_ode et midpoint_ode : ta tolérance est-elle trop "
              "stricte ?")
    for number_c24, (method_c24, name_c24, clause_c24) in enumerate(WRONG_C24, start=1):
        refused_c24 = not verdict_c24(name_c24, f"méthode fausse cachée n° {number_c24}", method_c24)
        report_24(refused_c24, f"{name_c24} refuse la méthode fausse cachée n° {number_c24}",
                  f"{name_c24} accepte la méthode fausse cachée n° {number_c24}, fausse {clause_c24}")
    verdict("MB5.24", all(results_24) and len(results_24) == 2 + len(WRONG_C24), "tes trois tests jugent juste les deux "
            "méthodes de la référence, deux autres écritures justes, et refusent les méthodes fausses cachées.",
            "relis les lignes ❌ ci-dessus.")'''

NOTE_24 = (r"Une correction possible : `constant_is_exact_24` essaie trois vitesses (dont une négative), $N = 1$, 3 et "
           r"7, et compare chaque point à `x0 + c * (t_k - t0)` ; `affine_is_exact_24` compare chaque point à `x0 + k0 * "
           r"(t_k - t0) + k1 * (t_k ** 2 - t0 ** 2) / 2` pour plusieurs couples $(\kappa_0, \kappa_1)$ ; "
           r"`error_halves_24` prend $x' = t - x$, $x(0) = 2$, sur $[0, 3]$, avec $N = 64$ et 128. a) Euler : "
           r"`[True, False, True]` ; point milieu : `[True, True, False]`.")

MB5_24 = ex(
    "MB5.24", "écrire trois tests de propriété d'une méthode d'intégration, et voir ce que chacun attrape.",
    "fiche §8 ; M02a (sommes de Riemann, point milieu) ; Ex MB5.18", note=NOTE_24,
    body=r"""Écris trois fonctions qui testent une méthode d'intégration `method(f, x0, t0, t1, n_steps)` qu'on leur passe (de la forme de `euler_ode` : elle rend les $N + 1$ points), et rendent `True` si la propriété tient, `False` sinon :
- `constant_is_exact_24(method)` vérifie qu'avec un champ constant (plusieurs valeurs, plusieurs nombres de pas, avec $t_0 < t_N$), **chaque** point rendu est sur la droite exacte, à $10^{-9}$ près en valeur absolue (plus fin que la tolérance par défaut de `np.allclose`, `rtol=1e-5` et `atol=1e-8`) ;
- `affine_is_exact_24(method)` vérifie de même qu'avec un champ $f(t, x) = \kappa_0 + \kappa_1t$, chaque point rendu est sur la parabole exacte, à $10^{-9}$ près en valeur absolue ;
- `error_halves_24(method)` vérifie que, pour un champ qui dépend de $t$ et de $x$ dont tu connais la solution exacte, l'erreur au temps final est divisée par un nombre entre $1{,}8$ et $2{,}2$ quand le nombre de pas passe de $N$ à $2N$ (avec $N$ assez grand).

La vérification lance tes trois tests sur `euler_ode` et `midpoint_ode` de la référence (`ref_gp.euler_ode`, `ref_gp.midpoint_ode`), sur deux autres écritures justes de ces méthodes, puis sur des méthodes fausses cachées, passées sous un nom neutre (un test juge ce que fait la méthode, pas son nom), une par clause de l'énoncé, que chaque test doit refuser quand sa propriété est fausse. Un test exécute la méthode sur ses champs et compare ses résultats à ce que dit la propriété : il ne lit ni la méthode, ni la pile d'appels, ni les noms de la vérification, et n'appelle pas `euler_ode` ni `midpoint_ode` (ni ceux de la référence, ni les tiens : la vérification le contrôle). Relève :
- a) les résultats de tes trois tests sur `euler_ode`, puis sur `midpoint_ode` de la référence (deux listes de 3 booléens, dans l'ordre constant, affine, erreur).""",
    todo='''def constant_is_exact_24(method):
    """True when, for constant velocity fields (several values, several numbers of steps, t0 < t1), every point returned
    by method(f, x0, t0, t1, n_steps) is on the exact line, up to 1e-9; False otherwise."""
    raise NotImplementedError("constant_is_exact_24 n'est pas encore écrite (04_indices.md si tu bloques)")


def affine_is_exact_24(method):
    """True when, for fields f(t, x) = k0 + k1 t (several fields, several numbers of steps, t0 < t1), every point
    returned by method is on the exact parabola, up to 1e-9; False otherwise."""
    raise NotImplementedError("affine_is_exact_24 n'est pas encore écrite (04_indices.md si tu bloques)")


def error_halves_24(method):
    """True when, for a field that depends on t and on x and whose exact solution you know, the error of method at the
    final time is divided by a number between 1.8 and 2.2 when the number of steps goes from N to 2N (N large enough);
    False otherwise."""
    raise NotImplementedError("error_halves_24 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB5_24a = ...
with wbm.attempt("MB5.24"):          # your three tests: ⏳ while they are not written
    answer_MB5_24a = ...  # a) two lists of 3 booleans: your three tests on ref_gp.euler_ode, then on ref_gp.midpoint_ode''',
    check=answers_check("MB5.24", "a") + "\n\n" + CHECK_24,
    solution='''def constant_is_exact_24(method):
    """True when, for constant velocity fields (several values, several numbers of steps, t0 < t1), every point returned
    by method(f, x0, t0, t1, n_steps) is on the exact line, up to 1e-9; False otherwise."""
    for c in (1.7, -0.45, 3.2):
        for n in (1, 3, 7):
            t0, t1, x0 = 0.4, 2.9, -1.3
            points = np.asarray(method(lambda t, x: c + 0 * x, x0, t0, t1, n), dtype=float)
            times = t0 + (t1 - t0) / n * np.arange(n + 1)
            if points.shape != (n + 1,) or not np.allclose(points, x0 + c * (times - t0), rtol=0, atol=1e-9):
                return False
    return True


def affine_is_exact_24(method):
    """True when, for fields f(t, x) = k0 + k1 t (several fields, several numbers of steps, t0 < t1), every point
    returned by method is on the exact parabola, up to 1e-9; False otherwise."""
    for k0, k1 in ((0.6, -1.3), (-2.1, 0.75), (0.0, 2.4)):
        for n in (1, 4, 9):
            t0, t1, x0 = -0.5, 1.8, 0.9
            points = np.asarray(method(lambda t, x: k0 + k1 * t + 0 * x, x0, t0, t1, n), dtype=float)
            times = t0 + (t1 - t0) / n * np.arange(n + 1)
            exact = x0 + k0 * (times - t0) + k1 * (times ** 2 - t0 ** 2) / 2
            if points.shape != (n + 1,) or not np.allclose(points, exact, rtol=0, atol=1e-9):
                return False
    return True


def error_halves_24(method):
    """True when, for a field that depends on t and on x and whose exact solution you know, the error of method at the
    final time is divided by a number between 1.8 and 2.2 when the number of steps goes from N to 2N (N large enough);
    False otherwise."""
    exact = 3 - 1 + 3 * math.exp(-3)                         # x' = t - x, x(0) = 2: x(t) = t - 1 + 3 e^-t
    errors = [abs(float(np.asarray(method(lambda t, x: t - x, 2.0, 0.0, 3.0, n), dtype=float)[-1]) - exact)
              for n in (64, 128)]
    return errors[1] > 0 and 1.8 <= errors[0] / errors[1] <= 2.2


answer_MB5_24a = [[test(method) for test in (constant_is_exact_24, affine_is_exact_24, error_halves_24)]
                  for method in (ref_gp.euler_ode, ref_gp.midpoint_ode)]
print("a)", answer_MB5_24a)''',
    record='''def properties_24r(method):
    """The oracle: the three properties, measured with other fields, steps and times than any test of the notebook (exact
    values computed in fractions for the first two)."""
    from fractions import Fraction as F_24r
    exact_line = all(abs(float(p) - float(F_24r("0.25") + F_24r(str(c)) * (F_24r("1.5") + k * F_24r("2.25") / n
                                                                            - F_24r("1.5"))))
                     < 1e-10 for c in (2.5, -0.8) for n in (2, 5)
                     for k, p in enumerate(method(lambda t, x: c + 0 * x, 0.25, 1.5, 3.75, n)))
    exact_parabola = all(abs(float(p) - (1.1 + 0.3 * (t - 0.2) - 1.4 * (t * t - 0.04) / 2)) < 1e-10
                         for n in (2, 6) for t, p in zip(0.2 + 2.6 / n * np.arange(n + 1),
                                                         method(lambda t, x: 0.3 - 1.4 * t + 0 * x, 1.1, 0.2, 2.8, n)))
    exact = 1 / (1 + math.exp(-2.0))                          # the logistic field from 1/2: its solution is the sigmoid
    errors = [abs(float(method(lambda t, x: x * (1 - x) * (1 + 0 * t), 0.5, 0.0, 2.0, n)[-1]) - exact)
              for n in (200, 400)]
    halving = 1.8 <= errors[0] / errors[1] <= 2.2
    return [bool(exact_line), bool(exact_parabola), bool(halving)]


wbm.record("MB5.24a", [properties_24r(ref_gp.euler_ode), properties_24r(ref_gp.midpoint_ode)],
           mistakes={"un test qui rend toujours True ne teste rien : chacune des deux méthodes a une propriété qui lui "
                     "manque (fiche §8)": [[True, True, True], [True, True, True]],
                     "la première liste est celle de euler_ode, la seconde celle de midpoint_ode":
                         [properties_24r(ref_gp.midpoint_ode), properties_24r(ref_gp.euler_ode)]})''',
    after=[
        ("solution", answers_check("MB5.24", "a") + "\n\n" + CHECK_24),
        look("pourquoi `affine_is_exact_24` refuse-t-il la méthode d'Euler, et `error_halves_24` le point milieu ? "
             "Pourquoi tester chaque point rendu, et pas seulement le dernier ?"),
    ],
)

PART_C = Part("C", "Déboguer, tester",
              "Fiche §2, §5 et §8. Trois erreurs classiques, qui passent une vérification mal choisie ; trois tests de "
              "propriété d'une méthode d'intégration. Les méthodes cachées s'appuient sur la référence (`ref_gp`), pour ne "
              "pas dépendre de ton code.", exercises=[MB5_23, MB5_24])

# ---------------------------------------------------------------------------
# Notebook exercise: the challenge (MB5.25)
# ---------------------------------------------------------------------------
GIVEN_25 = '''# The two-bump law of the challenge: the weights, the means and the variances of a mixture of two Gaussians
MIX_25 = ((0.38, 0.62), (-1.6, 2.1), (0.14, 0.3))
Z_25 = frozen(np.random.default_rng(7725).normal(size=20_000))      # 20 000 draws of N(0, 1): the points at s = 1
_rng_25 = np.random.default_rng(7726)                                # 200 000 draws of MIX_25
_bump_25 = _rng_25.choice(2, size=200_000, p=MIX_25[0])
TARGET_25 = frozen(np.array(MIX_25[1])[_bump_25] + np.sqrt(np.array(MIX_25[2]))[_bump_25] * _rng_25.normal(size=200_000))
del _rng_25, _bump_25'''

CHECK_25 = """FIELD_CASES_C25 = __FIELD_CASES_C25__   # hidden points, times and mixtures for field_25, and the sub-ID expected


def check_c25():
    \"\"\"The check of MB5.25, in a function. The hidden laws live in another process (the hidden module run as a script):
    it answers each call of the field, counts the calls, and measures the points reached only once transport_25 has
    seen all the laws; neither a hidden law nor what makes it (a seed, a kind) lives in this process while the learner's
    function runs. Each call runs under code_from: the learner's function may not run code of the hidden module.\"\"\"
    import json
    import subprocess
    import sys
    from scipy.stats import wasserstein_distance
    refuse_peeking("MB5.25", {"field_25": field_25, "transport_25": transport_25}, globals(),
                   private=("_c25", "_C25"))            # it computes, it never reads the check
    hidden_file = wbm.repo_root() / "solutions" / "challenges" / "mb5_25.py"   # reading it spoils the challenge
    twins = code_keys_of_file(hidden_file)                      # its functions, to recognise a copy run from elsewhere
    results = []
    report = reporter(results, stop=False)

    # a) field_25 at hidden points (other times, other mixtures)
    got = []
    for case_points, case_s, case_parts in FIELD_CASES_C25["cases"]:
        x = np.array(case_points)                               # non-dyadic floats: a change in place would show
        out = as_floats(call_safely("Ex MB5.25 : field_25 (appel caché)", field_25, x, case_s, *case_parts))
        if not np.array_equal(x, np.array(case_points)):
            print("❌ Ex MB5.25 : field_25 modifie le tableau x reçu : calcule sur une copie")
            raise StopCheck
        if out is None or out.shape != x.shape:
            print(f"❌ Ex MB5.25 : field_25 rend un tableau de la forme de x, reçu {shown(out)}")
            raise StopCheck
        got += out.tolist()
    field_ok = passes(FIELD_CASES_C25["id"], got)
    report(field_ok, "Ex MB5.25a : field_25 en des points cachés (d'autres instants, d'autres mélanges)",
           "Ex MB5.25a : field_25 en des points cachés : ce n'est pas le champ moyen v(x, s) = (x − E[x_0 | x_s = x])/s, "
           "avec le débruiteur posterior_mean_mixture de gains a = 1 − s et b = s (fiche §9) ; si c'est bien ce que tu "
           "calcules, les tests de ta posterior_mean_mixture passent-ils tous ?")

    def exactly(stream, size):
        data = stream.read(size)
        if len(data) != size:
            raise OSError("échange interrompu")
        return data

    def transport(label, field, z):
        \"\"\"transport_25(field, z) under code_from: the points reached, as a float array of the shape of z.\"\"\"
        with code_from([hidden_file], twins=twins, escapes=True) as seen:
            out = call_safely(label, transport_25, field, z.copy())
        if seen and seen[0].startswith("lance "):
            print(f"❌ {label} : transport_25 {seen[0].replace(' : ', ' (', 1)}) : le transport se calcule dans ta "
                  "fonction ; ce qu'exécute un autre processus échappe à la vérification")
            raise StopCheck
        if seen:
            what = "lit" if seen[0].startswith("ouvre ") else "exécute du code de"
            where = "" if seen[0].startswith("ouvre ") else f" ({seen[0]})"
            print(f"❌ {label} : transport_25 {what} solutions/challenges/mb5_25.py{where}, la partie cachée du défi, ou "
                  "une copie de son code : la vérification mesurerait sa méthode, pas la tienne")
            raise StopCheck
        points = as_floats(out)
        if points is None or points.shape != z.shape:
            print(f"❌ {label} : transport_25 rend un tableau de {z.size} points, un par point de z, reçu {shown(out)}")
            raise StopCheck
        return points

    server = subprocess.Popen([sys.executable, "-I", str(hidden_file), "--serve"], stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)   # this kernel's Python, here or on Colab
    try:
        count = json.loads(exactly(server.stdout, 1) + server.stdout.readline())["count"]

        def field_of(k):
            \"\"\"The field v(x, s) of the law k, computed by the other process (each call is counted there).\"\"\"
            def field(x, s):
                if isinstance(s, (bool, np.bool_)) or np.ndim(s) != 0 or not 0 < float(s) <= 1:
                    raise ValueError(f"le champ prend un instant s de ]0, 1] (un nombre), reçu {shown(s)}")
                x = np.asarray(x, dtype=float)
                flat = np.ascontiguousarray(x.ravel(), dtype="<f8")
                server.stdin.write(f"F {k} {float(s)!r} {flat.size}\\n".encode() + flat.tobytes())
                server.stdin.flush()
                return np.frombuffer(exactly(server.stdout, 8 * flat.size), dtype="<f8").reshape(x.shape).copy()
            return field

        def send(k, points):
            flat = np.ascontiguousarray(points.ravel(), dtype="<f8")
            server.stdin.write(f"R {k} {flat.size}\\n".encode() + flat.tobytes())
            server.stdin.flush()

        mine = transport("Ex MB5.25 : transport_25 (le mélange du notebook)", field_of(count - 1), np.array(Z_25))
        send(count - 1, mine)
        rng = np.random.default_rng()                           # new noise points at each run
        for k in range(count - 1):
            send(k, transport(f"Ex MB5.25 : transport_25 (loi cachée {k + 1})", field_of(k), rng.normal(size=20_000)))
        server.stdin.write(b"verdict\\n")                       # only now: the measures, the kinds and the counts
        server.stdin.flush()
        laws = json.loads(exactly(server.stdout, 1) + server.stdout.readline())
        assert len(laws) == count
    except (OSError, ValueError, KeyError, TypeError, AssertionError) as exc:
        print("❌ Ex MB5.25 : la vérification n'a pas pu échanger les points et les champs avec le processus qui tire les "
              f"lois cachées ({type(exc).__name__} ; ta fonction a-t-elle touché à ce processus ?) : exécute à nouveau la "
              "cellule")
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

    advice = (" : avec ce budget, ta méthode ne suit pas les trajectoires d'assez près ; la fiche §8 dit quelle méthode "
              "est la plus précise à nombre d'évaluations égal")
    notebook, hidden = laws[-1], laws[:-1]
    if notebook["rel"] is None:
        report(False, "", "le mélange du notebook : transport_25 rend des points qui ne sont pas tous finis")
    else:
        report(notebook["rel"] <= 0.07 and notebook["calls"] <= 8,
               f"le mélange du notebook : W₁ = {fr(notebook['rel'], 3)} fois l'écart-type, en {notebook['calls']} appels "
               "du champ", "le mélange du notebook : " + " et ".join(
                   ([f"{notebook['calls']} appels du champ, plus que 8"] if notebook["calls"] > 8 else [])
                   + ([f"W₁ = {fr(notebook['rel'], 3)} fois l'écart-type, au-dessus de 0,07" + advice]
                      if notebook["rel"] > 0.07 else [])))
    for number in sorted({law["series"] for law in hidden}):        # what each hidden law measured (no verdict)
        series = [law for law in hidden if law["series"] == number]
        print(f"   série {number} : " + " ; ".join(
            f"« {law['kind']} » {'non finis' if law['rel'] is None else fr(law['rel'], 3)} ({law['calls']} appels)"
            for law in series))
    over = [law for law in hidden if law["calls"] > 8]
    broken = [law for law in hidden if law["rel"] is None]
    report(not over and not broken, f"les {len(hidden)} lois cachées : huit appels du champ au plus pour chacune, des "
           "points finis", f"les {len(hidden)} lois cachées : " + " ; ".join(
               ([f"{len(over)} lois avec plus de 8 appels du champ (jusqu'à {max(law['calls'] for law in over)})"]
                if over else []) + ([f"{len(broken)} lois avec des points qui ne sont pas tous finis"] if broken else [])))
    mean = float(np.mean([law["rel"] for law in hidden])) if not broken else math.inf
    calls_nb = notebook["calls"]
    if calls_nb == 0:
        tuned = " ; ta fonction n'appelle jamais field : elle ne connaît du mélange que ce que le notebook lui montre"
    elif notebook["rel"] is not None and notebook["rel"] <= 0.07 and notebook["rel"] < 0.25 * mean:
        tuned = (" ; elle réussit pourtant le mélange du notebook, bien mieux que les lois cachées : se règle-t-elle sur "
                 "MIX_25 au lieu de suivre field ?")
    elif calls_nb < 8:
        tuned = f" ; elle n'emploie que {calls_nb} des 8 appels permis : des pas plus courts réduiraient l'erreur"
    else:
        tuned = ""
    report(mean <= 0.07, f"les {len(hidden)} lois cachées : W₁ moyen = {fr(mean, 3)} fois l'écart-type, au plus 0,07",
           f"les {len(hidden)} lois cachées : W₁ moyen = {fr(mean, 3)} fois l'écart-type, au-dessus de 0,07" + advice
           + tuned if math.isfinite(mean) else f"les {len(hidden)} lois cachées : W₁ ne se mesure pas sur des points non finis")
    criterion = all(results) and len(results) == 4               # field_25, the notebook, the budget, the mean

    # b) and c): the two Euler distances (hidden sub-ID), the third and the count recomputed with your function
    if not filled(answer_MB5_25b):
        print("⏳ Ex MB5.25b : pas encore fait.")
    else:
        mine_b = as_floats(answer_MB5_25b)
        if mine_b is None or mine_b.shape != (3,):
            report(False, "", f"Ex MB5.25b : une liste de 3 nombres, reçu {shown(answer_MB5_25b)}")
        else:
            report(passes(FIELD_CASES_C25["id_b"], mine_b[:2].tolist()),
                   "Ex MB5.25b : les distances d'un pas et de huit pas d'Euler",
                   "Ex MB5.25b : les deux premières distances ne sont pas celles d'un pas, puis de huit pas égaux de "
                   "euler_ode, de s = 1 à s = 0, depuis Z_25, avec ton field_25 pour MIX_25"
                   + ("" if field_ok else " (corrige d'abord field_25)"))
            again = float(wasserstein_distance(mine, TARGET_25))
            report(math.isclose(float(mine_b[2]), again, rel_tol=1e-6, abs_tol=1e-9),
                   "Ex MB5.25b : la troisième distance est celle des points de ta fonction",
                   "Ex MB5.25b : la troisième distance n'est pas celle des points que rend transport_25 maintenant, avec "
                   "le champ exact (la vérification la recalcule) : exécute à nouveau ta cellule"
                   + ("" if field_ok else " (et corrige d'abord field_25)"))
    if not filled(answer_MB5_25c):
        print("⏳ Ex MB5.25c : pas encore fait.")
    else:
        report(isinstance(answer_MB5_25c, (int, np.integer)) and not isinstance(answer_MB5_25c, (bool, np.bool_))
               and int(answer_MB5_25c) == notebook["calls"], "Ex MB5.25c : le nombre d'appels de ta fonction",
               "Ex MB5.25c : ta réponse n'est pas le nombre d'appels de field que fait transport_25 sur le mélange du "
               "notebook (un entier ; la vérification les compte)")
    verdict("MB5.25", criterion, "critère atteint : en huit appels du champ au plus, W₁ au plus 0,07 fois l'écart-type "
            "pour le mélange du notebook, et en moyenne pour les quinze lois cachées.",
            "critère pas encore atteint : relis les lignes ❌ ci-dessus.")


with checked("MB5.25"):
    check_c25()"""

NOTE_25 = (r"`field_25` : `(x - posterior_mean_mixture(x, 1 - s, s, weights, means, variances)) / s`. `transport_25` : la "
           r"méthode du point milieu avec quatre pas égaux de $s = 1$ à $s = 0$ (huit appels). b) Un pas d'Euler : "
           r"$W_1 \approx 1{,}744$ ; huit pas d'Euler : $\approx 0{,}173$ ($0{,}093$ fois l'écart-type $1{,}86$ du "
           r"mélange, au-dessus du seuil $0{,}07$) ; le point milieu : $\approx 0{,}032$ ($0{,}017$ fois "
           r"l'écart-type). c) 8. Le piège : huit pas d'Euler semblent le meilleur usage du budget, mais l'erreur "
           r"d'Euler n'est que d'ordre 1 ; quatre pas du point milieu, d'ordre 2, font bien mieux pour le même nombre "
           r"d'évaluations (la fiche §8).")

MB5_25 = ex(
    "MB5.25", "transporter un bruit vers une loi à deux bosses par son champ moyen exact, avec un budget d'évaluations du "
    "champ, et le vérifier sur des lois cachées.", "fiche §8 et §9 ; M27 (distance de Wasserstein) ; Ex MB5.17, MB5.21",
    note=NOTE_25, given=GIVEN_25,
    body=r"""Le notebook fournit `MIX_25`, une loi à deux bosses (les poids, les moyennes et les variances d'un mélange de deux gaussiennes de dimension 1), `Z_25`, 20 000 tirages de $\mathcal{N}(0, 1)$, et `TARGET_25`, 200 000 tirages de `MIX_25`.
- a) Écris `field_25(x, s, weights, means, variances)`, le champ moyen exact $v(x, s)$ du chemin droit vers ce mélange, avec `posterior_mean_mixture` (pour $0 < s \le 1$ ; `x` est un tableau de points).
- Puis écris `transport_25(field, z)` : depuis les points `z` (en $s = 1$), suis $x' = v(x, s)$ jusqu'en $s = 0$, en appelant `field(x, s)` **au plus huit fois** (un appel sur un tableau entier compte pour un ; `field` prend le point d'abord, puis l'instant), et rends les points atteints. Ta fonction ne connaît le mélange que par `field` ; tout NumPy et SciPy sont permis.

**Critère de réussite :** avec au plus huit appels du champ pour chaque loi, la distance de Wasserstein $W_1$ (M27) entre tes points et la loi à deux bosses, divisée par l'écart-type de cette loi, est au plus $0{,}07$ pour `MIX_25`, et au plus $0{,}07$ en moyenne pour trois séries de cinq lois cachées, tirées à nouveau à chaque exécution (la moyenne des quinze rapports) ; chaque série a une loi de chacun de ces cinq types : facile ; deux bosses très étroites ; une bosse légère d'une autre largeur ; deux bosses plus écartées que le bruit n'est large ; deux bosses qui se chevauchent. La vérification passe à `transport_25` un `field` qu'elle calcule elle-même, et compte ses appels. Ta fonction ne doit ni exécuter le code du module caché du défi (`solutions/challenges/mb5_25.py`), ni lire la vérification (sa pile d'appels, le processus à part) : la vérification le contrôle. Relève :
- b) avec `scipy.stats.wasserstein_distance` entre tes points et `TARGET_25`, la distance obtenue par un seul pas d'Euler (`euler_ode`, de $s = 1$ à $s = 0$, avec ton `field_25` ; `euler_ode` appelle `f(s, x)` : passe-lui `lambda s, x: field_25(x, s, *MIX_25)`), puis par huit pas d'Euler, puis par ta fonction (une liste de 3 nombres) ;
- c) le nombre d'appels de `field` que fait ta fonction (un entier).

Point de départ : huit pas d'Euler ne suffisent pas ; la fiche §8 dit comment comparer deux méthodes qui ont droit au même nombre d'évaluations.""",
    todo='''def field_25(x, s, weights, means, variances):
    """The exact mean field v(x, s) of the straight path to the mixture (weights, means, variances), at the points x (an
    array), for 0 < s <= 1."""
    raise NotImplementedError("field_25 n'est pas encore écrite (04_indices.md si tu bloques)")


def transport_25(field, z):
    """From the points z (at s = 1), follow x' = v(x, s) down to s = 0, calling field(x, s) at most 8 times (one call for
    a whole array counts once); returns the points reached."""
    raise NotImplementedError("transport_25 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB5_25b = answer_MB5_25c = ...
with wbm.attempt("MB5.25"):          # your functions: ⏳ while they are not written
    answer_MB5_25b = ...  # b) a list of 3 numbers, as computed: wasserstein_distance to TARGET_25 of one Euler step, of eight Euler steps, of transport_25
    answer_MB5_25c = ...  # c) an integer: the number of calls of field made by transport_25''',
    check=CHECK_25,
    solution='''from scipy.stats import wasserstein_distance


def field_25(x, s, weights, means, variances):
    """The exact mean field v(x, s) of the straight path to the mixture (weights, means, variances), at the points x (an
    array), for 0 < s <= 1."""
    x = np.asarray(x, dtype=float)
    return (x - mymath.gaussian_paths.posterior_mean_mixture(x, 1 - s, s, weights, means, variances)) / s


def transport_25(field, z):
    """From the points z (at s = 1), follow x' = v(x, s) down to s = 0, calling field(x, s) at most 8 times (one call for
    a whole array counts once); returns the points reached."""
    x = np.array(z, dtype=float)
    h, s = -0.25, 1.0                                         # four steps of the midpoint method: eight calls
    for _ in range(4):
        x = x + h * field(x + h / 2 * field(x, s), s + h / 2)
        s = s + h
    return x


calls_25 = [0]


def counted_field_25(x, s):
    calls_25[0] += 1
    return field_25(x, s, *MIX_25)


def euler_25(n):
    return mymath.gaussian_paths.euler_ode(lambda s, x: field_25(x, s, *MIX_25), Z_25, 1.0, 0.0, n)[-1]


start_25 = time.perf_counter()
mine_25 = transport_25(counted_field_25, Z_25)
answer_MB5_25b = [float(wasserstein_distance(points, TARGET_25)) for points in (euler_25(1), euler_25(8), mine_25)]
answer_MB5_25c = calls_25[0]
weights_25, means_25, variances_25 = (np.array(part) for part in MIX_25)
sd_25 = math.sqrt(float(weights_25 @ (variances_25 + means_25 ** 2)) - float(weights_25 @ means_25) ** 2)
print("b)", np.round(answer_MB5_25b, 6).tolist(), " soit", np.round(np.array(answer_MB5_25b) / sd_25, 4).tolist(),
      "fois l'écart-type", round(sd_25, 4), " c)", answer_MB5_25c, f" ({time.perf_counter() - start_25:.2f} s)")''',
    record='''from scipy.special import logsumexp as logsumexp_25r
from scipy.stats import norm as norm_25r
from scipy.stats import wasserstein_distance as wasserstein_25r


def posterior_25r(y, a, b, weights, means, variances):
    """The oracle: E[x_0 | a x_0 + b eps = y] for a mixture, the responsibilities by scipy (norm.logpdf, logsumexp)."""
    y = np.asarray(y, dtype=float).reshape(-1, 1)
    w, m, v = (np.asarray(part, dtype=float) for part in (weights, means, variances))
    if a == 0:
        return np.full(y.shape[0], float(w @ m))
    logs = np.log(w) + norm_25r.logpdf(y, a * m, np.sqrt(a * a * v + b * b))
    resp = np.exp(logs - logsumexp_25r(logs, axis=1, keepdims=True))
    return (resp * (m + a * v / (a * a * v + b * b) * (y - a * m))).sum(axis=1)


def field_25r(x, s, law):
    x = np.asarray(x, dtype=float)
    return (x.ravel() - posterior_25r(x, 1 - s, s, *law)) / s


law_25r = ((0.38, 0.62), (-1.6, 2.1), (0.14, 0.3))
noise_25r = np.random.default_rng(7725).normal(size=20_000)
rng_25r = np.random.default_rng(7726)
bump_25r = rng_25r.choice(2, size=200_000, p=law_25r[0])
target_25r = np.array(law_25r[1])[bump_25r] + np.sqrt(np.array(law_25r[2]))[bump_25r] * rng_25r.normal(size=200_000)


def euler_25r(n):
    """n equal Euler steps from s = 1 to s = 0 (written again)."""
    x = noise_25r.copy()
    for k in range(n):
        s = 1 - k / n
        x = x - field_25r(x, s, law_25r) / n
    return x


FIELD_CASES_25r = __FIELD_CASES_C25__                                    # the hidden calls of the check
wbm.record(FIELD_CASES_25r["id_b"], [float(wasserstein_25r(euler_25r(n), target_25r)) for n in (1, 8)], decimals=5)
wbm.record(FIELD_CASES_25r["id"], [v for points, s, law in FIELD_CASES_25r["cases"] for v in field_25r(points, s, law)],
           decimals=6)''',
    after=[
        ("solution", CHECK_25),
        ("md", "**Pour réfléchir** (une fois le critère atteint) : pourquoi huit pas d'Euler ne suffisent-ils pas, alors "
               "que ta méthode, pour le même nombre d'appels, suffit ? Pourquoi une méthode réglée sur `MIX_25` seul (ses quantiles, "
               "par exemple) ne suffit-elle pas pour les lois cachées ? Les réponses sont dans `05_solutions.md`, section "
               "Notebook."),
    ],
)

PART_D = Part("D", "Défi", "Fiche §8 et §9. Transporter un bruit vers une loi à deux bosses par son champ moyen exact, avec "
              "huit évaluations du champ, vérifié sur des lois cachées tirées à chaque exécution.", exercises=[MB5_25])

PARTS = [PART_A, PART_B, PART_C, PART_D]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | MB5.1 à MB5.9, MB5.14 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, exercise in enumerate(part.exercises):
            rows.append(exercise.table_row(part.key if i == 0 else ""))
    if kind == "exercise":
        title = "# MB5 · Les maths de la diffusion — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). Dans "
               "les parties A à D, donne les valeurs que rend le calcul, **sans les arrondir** : les décimales "
               "demandées sont celles de ta copie. « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli : ce qui n'est pas fait affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/mb5_diffusion/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py MB5`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# MB5 · Les maths de la diffusion — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : l'anomalie de température d'un lac, la survie d'une ruche, un "
               "phoque balisé, une voix et un bruit de fond, un signal reçu, un bit relayé, la floraison d'un verger, une "
               "tasse de thé, un chemin droit vers une loi gaussienne, et un pont vers une loss de débruitage.\n"
               "- Écrire les quatre fonctions de `mymath/gaussian_paths.py` (`linear_gaussian_recursion`, "
               "`posterior_mean_mixture`, `euler_ode`, `midpoint_ode`) et les tester.\n"
               "- Mesurer l'ordre de deux méthodes avec `solve_ivp`, prédire puis mesurer le débruiteur d'un nuage de "
               "points, transporter une loi par un champ moyen, tracer des lois guidées, corriger trois erreurs "
               "classiques, écrire trois tests de propriété, et relever un défi.\n\n"
               r"**Rappel express.** Pour $x_t = a_tx_{t-1} + b_t\varepsilon_t$ : $m_t = a_tm_{t-1}$ et $v_t = "
               r"a_t^2v_{t-1} + b_t^2$ ; pour $a_t = a$, $\lvert a\rvert < 1$, $b_t = b$ : $v_\infty = \frac{b^2}{1 - "
               r"a^2}$. Pour $y = ax + bn$ et $x$ de loi $\sum_k\pi_k\mathcal{N}(\mu_k, v_k)$, avec la variance $v_k$ "
               r"de la fiche ($s_k^2$ dans la docstring, et dans les énoncés qui la suivent) : la composante $k$ a la "
               r"responsabilité $\propto \pi_k\,\mathcal{N}(y \mid a\mu_k, a^2v_k + b^2)$, et $\mathbb{E}[x \mid y, k] = "
               r"\mu_k + \frac{av_k}{a^2v_k + b^2}(y - a\mu_k)$. La loi guidée est proportionnelle à "
               r"$p_c^{1+w}p_u^{-w}$. Euler : $x_{k+1} = x_k + h\,f(t_k, x_k)$, d'ordre 1 ; le point milieu : $x_{k+1} = "
               r"x_k + h\,f\big(t_k + \frac h2, x_k + \frac h2f(t_k, x_k)\big)$, d'ordre 2, deux évaluations par pas ; "
               r"$h = \frac{t_N - t_0}{N}$. Le chemin droit $x_s = (1 - s)\,x_0 + s\,\varepsilon$ a le champ moyen "
               r"$v(x, s) = \frac{x - \mathbb{E}[x_0 \mid x_s = x]}{s}$, que l'on suit de $s = 1$ à $s = 0$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu propager la moyenne et la variance d'une récurrence linéaire gaussienne, trouver sa loi "
               "stationnaire, et dire combien de pas il faut pour oublier le départ ?\n"
               "2. Sais-tu conditionner une marche aléatoire sur deux instants, et construire des trajectoires de mêmes "
               "lois marginales mais de corrélations différentes ?\n"
               "3. Sais-tu passer du SNR à la part de variance, au logit et aux décibels ?\n"
               "4. Sais-tu dire ce qu'apprend la MSE, calculer le débruiteur optimal d'un mélange, et le relier au score "
               "par la formule de Tweedie ?\n"
               "5. Sais-tu écrire l'ELBO d'une chaîne de latents, et calculer une loi guidée et sa condition "
               "d'existence ?\n"
               "6. Sais-tu suivre une équation différentielle par Euler et par le point milieu, comparer leurs erreurs à "
               "nombre d'évaluations égal, et transporter une loi par le champ moyen d'un chemin droit ?\n\n"
               "**La suite** : le chapitre bonus B5 de workbookIA, qui applique ces outils.")]


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
    return any(abs(x * 2 ** 20 - round(x * 2 ** 20)) > 1e-9 for x in values)


def build_constants() -> dict:
    """The literals written in the cells, by placeholder, with the assertions that make the data and the hidden cases
    fair."""
    import numpy as np
    from scipy.stats import norm

    sys.path.insert(0, str(ROOT / "solutions"))
    from mymath_ref import gaussian_paths as ref             # noqa: E402 - the reference, for the assertions
    out = {}

    # MB5.16: the twelve weeks of spring (the data of work_c/nb_values.py, chosen by hand): no pair with a² + b² = 1, no
    # arithmetic progression; the reference finds the values of 05_solutions.md
    a16 = [0.96, 0.93, 0.88, 0.71, 0.58, 1.04, 0.99, 0.83, 0.66, 0.91, 1.02, 0.79]
    b16 = [0.36, 0.21, 0.57, 0.52, 0.38, 0.26, 0.34, 0.41, 0.55, 0.48, 0.28, 0.44]
    assert all(abs(a * a + b * b - 1) >= 0.05 for a, b in zip(a16, b16))
    for seq in (a16, b16):
        steps = np.diff(seq)
        assert not np.allclose(steps, steps[0]) and not np.allclose(np.diff(sorted(seq)), np.diff(sorted(seq))[0])
    m16, v16 = ref.linear_gaussian_recursion(a16, b16, mean0=1.5, var0=0.3)
    assert [round(float(m16[-1]), 6), round(float(v16[-1]), 6)] == [0.200712, 0.682062]
    for a, b in ((0.88, 0.35), (-0.68, 1.1), (0.7, 0.5), (0.5, 1.0), (2.0, 3.0), (1.2, 0.9), (1.5, 0.7)):
        assert abs(a * a + b * b - 1) >= 0.05                  # the pairs of the notebook exercises
    out["__A_16__"], out["__B_16__"] = literal(a16), literal(b16)

    # MB5.21: hidden times and points (non-dyadic; never s = 0.5 nor x = 1.5, the question b of MB5.9), the exact field
    # far from a rounding limit at 6 decimals
    def field21(s, x):
        sigma2 = (1 - s) ** 2 * 0.25 + s * s
        return -4 + (s - (1 - s) * 0.25) / sigma2 * (np.asarray(x) - (1 - s) * 4)

    calls21 = [(0.93, [-2.31, 0.47, 1.06, 3.41]), (0.61, [-1.13, 0.29, 2.74, 4.09, 5.91]), (0.27, [2.17, 3.43, 4.74]),
               (0.08, [3.52, 3.97, 4.33, 4.71]), (1.0, [-0.83, 0.62, 2.29])]
    for s, xs in calls21:
        assert not_dyadic(xs) and s != 0.5 and 1.5 not in xs
        assert not any(near_limit(v) for v in field21(s, xs)), (s, xs)
        expected = (np.array(xs) - ref.posterior_mean_mixture(xs, 1 - s, s, [1.0], [4.0], [0.25])) / s
        assert np.allclose(expected, field21(s, xs), rtol=1e-12, atol=1e-12)
    out["__HIDDEN_C21__"] = literal({"calls": calls21, "id": "MB5.21d", "id_means": "MB5.21e"})

    # MB5.22: the points of the grid compared (every 32nd, far from a rounding limit at 6 decimals for every density
    # recorded), hidden w (none of 0, 1, 3, 7, 0.5, 2 nor the w of the fiche and of MB5.7), another mixture on another grid
    def guided(xs, w, general=((0.55, 0.45), (-1.8, 1.6), (0.5, 0.7)), cls=(1.6, 0.7)):
        pu = sum(p * norm.pdf(xs, m, math.sqrt(v)) for p, m, v in zip(*general))
        d = norm.pdf(xs, cls[0], math.sqrt(cls[1])) ** (1 + w) * pu ** (-w)
        return d / np.trapezoid(d, xs)

    grid = np.linspace(-8, 8, 3201)
    hidden_ws, other_ws = [2.8, 0.45, 1.1], [0.9, 2.2]
    forbidden_w = {0, 1, 3, 7, 0.5, 2, 1.5, 0.4, 1.25, -0.3, 0.07, 0.17, 0.22, 0.05, 0.15, 0.25, 1.75, 3.5}
    assert not (set(hidden_ws) | set(other_ws)) & (forbidden_w - {0.25, 1.75, 3.5})
    general_o, cls_o, grid_o = ((0.47, 0.53), (-2.3, 0.9), (0.6, 0.45)), (0.9, 0.45), (-7.0, 6.0, 2601)
    assert cls_o[1] <= max(general_o[2])                      # the guided laws exist for every w >= 0
    curves = [guided(grid, w) for w in (0.25, 1.75, 3.5, *hidden_ws)]
    curves += [sum(p * norm.pdf(grid, m, math.sqrt(v)) for p, m, v in zip((0.55, 0.45), (-1.8, 1.6), (0.5, 0.7))),
               norm.pdf(grid, 1.6, math.sqrt(0.7))]
    idx = [i for i in range(0, 3201, 32) if not any(near_limit(c[i]) for c in curves)]
    assert len(idx) >= 60, len(idx)
    other_grid = np.linspace(*grid_o)
    others = [guided(other_grid, w, general_o, cls_o) for w in other_ws]
    idx_o = [i for i in range(0, 2601, 26) if not any(near_limit(c[i]) for c in others)]
    assert len(idx_o) >= 60, len(idx_o)
    for w in (0.25, 1.75, 3.5):                               # the exchanged powers differ on the points compared
        swapped = guided(grid, -1 - w)
        assert not np.allclose(swapped[idx], guided(grid, w)[idx], atol=1e-5)
    out["__HIDDEN_C22__"] = literal({"idx": idx, "ws": hidden_ws, "grid": grid_o, "general": general_o, "cls": cls_o,
                                     "other_ws": other_ws, "idx_other": idx_o, "id_main": "MB5.22d",
                                     "id_hidden": "MB5.22e", "id_other": "MB5.22f", "id_u": "MB5.22g",
                                     "id_c": "MB5.22h"})

    # MB5.23: hidden bridges (never V_s/V_T = 1/2), mixtures of 2 to 4 components with measurements in arrays (non-dyadic
    # floats), fields that depend on the time, forward and backward; the colleague's versions fail on each
    bridges = [[-2.3, 4.1, 0.7, 5.3], [6.2, 1.9, 4.35, 4.9], [0.35, -1.15, 2.65, 3.1], [10.5, 12.25, 0.9, 7.8]]
    for x0, xT, Vs, VT in bridges:
        assert abs(Vs / VT - 0.5) > 0.05 and abs(x0 - xT) > 1
        mean = x0 + Vs / VT * (xT - x0)
        assert not near_limit(mean) and not near_limit(Vs * (VT - Vs) / VT)
    mixtures = [[[-1.1, 0.35, 2.05, 3.3], 1.3, 0.6, [0.27, 0.73], [-0.6, 1.9], [0.45, 0.2]],
                [[-1.7, -0.2, 0.9, 2.6], 0.85, 1.15, [0.2, 0.5, 0.3], [-2.1, 0.4, 2.7], [0.15, 0.6, 0.35]],
                [[[-1.3, 0.45], [1.15, -2.2]], -0.75, 0.55, [0.1, 0.25, 0.4, 0.25], [-3.2, -1.0, 0.7, 2.9],
                 [0.3, 0.12, 0.5, 0.25]]]
    for y, a, b, w, m, v in mixtures:
        assert abs(a * a + b * b - 1) > 0.05 and abs(sum(w) - 1) < 1e-12 and not_dyadic(np.ravel(y)) and not_dyadic(w)
        right = ref.posterior_mean_mixture(y, a, b, w, m, v)
        y_, w_, m_, v_ = (np.asarray(p, dtype=float) for p in (y, w, m, v))
        gap = y_.reshape(-1, 1) - a * m_
        logs = np.log(w_) - 0.5 * np.log(2 * np.pi * v_) - gap ** 2 / (2 * v_)
        resp = np.exp(logs - logs.max(axis=1, keepdims=True))
        resp = resp / resp.sum(axis=1, keepdims=True)
        bad = (resp * (m_ + a * v_ / (a * a * v_ + b * b) * gap)).sum(axis=1).reshape(y_.shape)
        assert not np.allclose(right, bad, atol=1e-6)         # the colleague's version fails
    fields = {"wave": lambda t, x: 0.75 * np.cos(1.3 * t) - 0.45 * x, "ramp": lambda t, x: 0.6 * t - 0.25 * x * x}
    cases_fields = [["wave", [0.3, -1.7, 2.45], 0.0, 2.6, 7], ["ramp", [1.15, 0.05], 0.5, 3.1, 5],
                    ["wave", [0.9, -0.35], 2.2, -0.4, 6]]
    for name, x0, t0, t1, n in cases_fields:
        right = ref.euler_ode(fields[name], np.array(x0), t0, t1, n)
        frozen = ref.euler_ode(lambda t, x, name=name, t0=t0: fields[name](t0, x), np.array(x0), t0, t1, n)
        assert not np.allclose(right, frozen, atol=1e-6) and not_dyadic(x0)
    out["__CASES_C23__"] = literal({"bridges": bridges, "mixtures": mixtures, "fields": cases_fields, "id": "MB5.23d"})

    # MB5.25: the notebook law is the one of the hidden module; hidden points, times and mixtures for field_25 (never the
    # data of MB5.9), far from a rounding limit; the reference method passes the notebook law
    challenge = load_module(ROOT / "solutions" / "challenges" / "mb5_25.py", "mb5_25_build")
    law25 = ((0.38, 0.62), (-1.6, 2.1), (0.14, 0.3))
    assert challenge.NOTEBOOK_LAW == law25
    cases25 = [[[-2.13, -0.41, 0.76, 2.58], 1.0, law25], [[-1.87, 0.33, 1.97], 0.63, law25],
               [[-1.52, 0.18, 2.27], 0.21, law25], [[-1.71, 1.98, 2.36], 0.047, law25],
               [[-0.94, 0.61, 1.83], 0.38, ((0.26, 0.74), (-0.7, 1.45), (0.09, 0.4))],
               [[-2.6, -0.15, 1.2, 3.05], 0.82, ((0.3, 0.45, 0.25), (-1.9, 0.35, 2.4), (0.2, 0.05, 0.33))]]
    for points, s, law in cases25:
        values = challenge.mean_field(np.array(points), s, law)
        expected = (np.array(points) - ref.posterior_mean_mixture(points, 1 - s, s, *law)) / s
        assert np.allclose(values, expected, rtol=1e-12, atol=1e-10) and not any(near_limit(v) for v in values), points
        assert not_dyadic(points)
    z25 = np.random.default_rng(7725).normal(size=20_000)
    reached = challenge.reference(lambda x, s: challenge.mean_field(x, s, law25), z25)
    assert challenge.w1_to_mixture(reached, law25) / challenge.mixture_sd(law25) < 0.03
    out["__FIELD_CASES_C25__"] = literal({"cases": cases25, "id": "MB5.25e", "id_b": "MB5.25d"})
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
