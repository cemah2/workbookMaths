#!/usr/bin/env python
"""Build the two notebooks of chapter MB3 from a single source (used by Claude).

    python tools/chapters/build_mb3.py
    python tools/run_all_notebooks.py chapitres/mb3_rotations_attention/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/mb3_rotations_attention/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ MB3.1 to MB3.7 and 🔗 MB3.11), each answer computed in the notebook from the data of
its statement (SymPy for the exact cosines, exact fractions for the softmax of multiples of ln 2 and the normalised
exponential means, math and NumPy otherwise), each wrong value computed by the error its message names; parts A to D are
the notebook exercises (MB3.14 to MB3.22), exactly as 02_exercices.md describes them. Wrong-answer messages state a rule,
never a number of the answer, the last step that gives it, nor another sub-question.

Data. The notebook exercises take the data of the paper exercises (a data cell of part A), the data of their own
statements (the stations of 🔮 MB3.17, seed 7317; the scores of 🔨 MB3.16, seed 7316; the scores and the 300 orders of
🔬 MB3.18, seed 7318; the relevés of 🏆 MB3.22, seed 7328, written as literals) and their own draws. Seeds 7301 to 7349
only (the tests use 7200 to 7290, the figures 7291 to 7299): 7321 (🛠️ MB3.21, statement); 7331 (the hidden stations of
MB3.17), 7341 and 7342 (the hidden starts of MB3.21), 7343 (the pool of hidden turbines of MB3.22: turbine k is drawn by
default_rng([7343, k])), 7344 (the hidden scores of 🐛 MB3.20). The check cells never hold the code that solves an
exercise nor a value that gives an answer without a calculation: the expected values are recorded by the solutions as
hidden sub-IDs and compared with ``wbm.check(..., computed=True)`` (the hidden calls of MB3.17, MB3.18, MB3.19 and
MB3.20, the counters of the hidden wrong versions of MB3.21, the bandwidths of MB3.22), computed at check time by the
reference ``mymath_ref.positional`` (the online softmax of the hidden cases of MB3.20), or given by properties. The
threshold of 🏆 MB3.22 is 1.3 times the error of the method of the check (Nadaraya-Watson on the cyclic encoding, its
bandwidth chosen by leave-one-out on 30 values from 0.03 to 1.5): computed here, at build time, for a pool of hidden
turbines and written in the check cell as thresholds only, so that the check cell does not hold the method; three of
them are drawn at each run. The check cells use their own data, never the test cases of tests/test_mb3_positional.py,
the examples of the docstrings of the stub positional, the examples of the fiche, nor the numbers of workbookIA B3, B2
and B1 (the notes of MB3 in the syllabus and their list « Évités »).
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

CHAPTER = "MB3"
FOLDER = "chapitres/mb3_rotations_attention"

BOOL = "True or False"


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("MB3.1", "Un bras articulé à deux segments : la pince en valeurs exactes par les formules d'addition, les deux "
                   "rotations enchaînées en une seule, et le retour par la rotation inverse", [
        ("a", 'an exact value, between quotes, with sqrt', "exact(sp.cos(deg(SHOULDER_1 + ELBOW_1)))",
         '''kind="exact",
           mistakes={"le cosinus d'une somme n'est pas la somme des cosinus":
                         exact(sp.cos(deg(SHOULDER_1)) + sp.cos(deg(ELBOW_1))),
                     "105° est un angle obtus : son cosinus est négatif": exact(-sp.cos(deg(SHOULDER_1 + ELBOW_1)))}'''),
        ("b", 'an exact value, between quotes, with sqrt', "exact(sp.sin(deg(SHOULDER_1 + ELBOW_1)))",
         '''kind="exact",
           mistakes={"dans sin(a + b), les deux produits s'ajoutent":
                         exact(sp.sin(deg(SHOULDER_1)) * sp.cos(deg(ELBOW_1)) - sp.cos(deg(SHOULDER_1)) * sp.sin(deg(ELBOW_1))),
                     "le sinus d'une somme n'est pas la somme des sinus":
                         exact(sp.sin(deg(SHOULDER_1)) + sp.sin(deg(ELBOW_1)))}'''),
        ("c", "a list of 2 numbers (3 decimals): x, then y", "floats(gripper_1(SHOULDER_1, SHOULDER_1 + ELBOW_1))",
         '''decimals=3,
           mistakes={"l'avant-bras tourne de l'angle de l'épaule plus celui du coude":
                         floats(gripper_1(SHOULDER_1, ELBOW_1)),
                     "le bras mesure 4 dm, l'avant-bras 2 dm":
                         floats(gripper_1(SHOULDER_1, SHOULDER_1 + ELBOW_1, ARM_1[::-1])),
                     "les angles sont en degrés : convertis-les en radians avant d'appeler cos et sin":
                         floats(ARM_1[0] * np.array([math.cos(SHOULDER_1), math.sin(SHOULDER_1)])
                                + ARM_1[1] * np.array([math.cos(SHOULDER_1 + ELBOW_1), math.sin(SHOULDER_1 + ELBOW_1)]))}'''),
        ("d", "a number, in degrees", "float((SHOULDER_1 + ELBOW_1) % 360)",
         '''decimals=6,
           mistakes={"les angles de deux rotations enchaînées s'ajoutent, ils ne se multiplient pas":
                         float(SHOULDER_1 * ELBOW_1),
                     "les angles de deux rotations enchaînées s'ajoutent, ils ne se soustraient pas":
                         float(SHOULDER_1 - ELBOW_1)}'''),
        ("e", BOOL, "bool(np.allclose(rot(SHOULDER_1) @ rot(ELBOW_1), rot(ELBOW_1) @ rot(SHOULDER_1)))",
         '''mistakes={"deux rotations du plan ont pour produit la rotation de la somme des angles, dans les deux ordres":
                         False}'''),
        ("f", "a list of 2 numbers (4 decimals)", "floats(rot(SHOULDER_1).T @ P_1)",
         '''decimals=4,
           mistakes={"R_θᵀ est la rotation inverse : elle tourne de −θ": floats(rot(SHOULDER_1) @ P_1),
                     "la caméra tourne avec le bras seulement, de 60°": floats(rot(SHOULDER_1 + ELBOW_1).T @ P_1)}'''),
        ("g", "a number (4 decimals)", "float(np.linalg.norm(P_1))",
         '''decimals=4,
           mistakes={"le bras et l'avant-bras ne sont pas alignés : la distance n'est pas la somme de leurs longueurs":
                         float(sum(ARM_1)),
                     "la distance est la racine carrée de x² + y²": float(P_1 @ P_1)}'''),
    ]),

    Paper("MB3.2", "Rotations de Givens : deux rotations de l'espace qui ne commutent pas, deux rotations de ℝ⁴ dans des "
                   "plans disjoints qui commutent, leur matrice diagonale par blocs, et la même rotation après une "
                   "permutation des coordonnées", [
        ("a", "a list of 3 numbers (4 decimals)", "floats(givens(3, 2, 3, math.pi / 2) @ givens(3, 1, 2, math.pi / 3) @ E2_2)",
         '''decimals=4,
           mistakes={"R₁₂(θ) envoie e₂ sur −sin θ e₁ + cos θ e₂":
                         floats(givens(3, 2, 3, math.pi / 2) @ givens(3, 1, 2, -math.pi / 3) @ E2_2),
                     "R₂₃(θ) tourne autour de e₁ : elle fixe e₁ et tourne le plan (e₂, e₃)":
                         floats(givens(3, 1, 2, math.pi / 2) @ givens(3, 1, 2, math.pi / 3) @ E2_2)}'''),
        ("b", "a list of 3 numbers (4 decimals)", "floats(givens(3, 1, 2, math.pi / 3) @ givens(3, 2, 3, math.pi / 2) @ E2_2)",
         '''decimals=4,
           mistakes={"R₂₃(θ) tourne e₂ vers e₃ quand θ > 0":
                         floats(givens(3, 1, 2, math.pi / 3) @ givens(3, 2, 3, -math.pi / 2) @ E2_2),
                     "c'est R₂₃(π/2) qui agit d'abord sur e₂ : calcule son image avant d'appliquer R₁₂":
                         floats(givens(3, 1, 2, math.pi / 3) @ E2_2)}'''),
        ("c", BOOL, "commute(givens(3, 2, 3, math.pi / 2), givens(3, 1, 2, math.pi / 3))",
         '''mistakes={"deux rotations de l'espace dont les plans se coupent ne commutent pas en général": True}'''),
        ("d", "a 4 × 4 matrix, as the list of its rows (4 decimals)", "floats(D_2)",
         '''decimals=4,
           mistakes={"R_ij(θ) a −sin θ à la ligne i, colonne j, et sin θ à la ligne j, colonne i": floats(D_2.T),
                     "le premier bloc tourne de π/3, le second de π/2":
                         floats(givens(4, 1, 2, math.pi / 2) @ givens(4, 3, 4, math.pi / 3))}'''),
        ("e", BOOL, "commute(givens(4, 1, 2, math.pi / 3), givens(4, 3, 4, math.pi / 2))",
         '''mistakes={"deux rotations dans des plans disjoints agissent sur des coordonnées différentes": False}'''),
        ("f", "a list of 2 pairs of integers, numbered from 1: [[i, j], [k, l]]", "planes_2(SIGMA_2)",
         '''decimals=0,
           mistakes={"PᵀDP tourne d'autres plans que D : applique σ aux deux indices de chaque plan":
                         [list(plane) for plane in PLANES_2],
                     "garde l'ordre (σ(3), σ(4)) : échanger les deux indices change le sens de la rotation":
                         [sorted(plane) for plane in planes_2(SIGMA_2)],
                     "P échange les coordonnées 2 et 4, pas 2 et 3": planes_2({1: 1, 2: 3, 3: 2, 4: 4})}'''),
        ("g", 'an exact angle in radians, between quotes, with pi', "exact(quarter_turn_angle_2())",
         '''kind="exact", angle=True,
           mistakes={"R₂₃(θ) tourne e₂ vers e₃ quand θ > 0 : regarde où va e₂": exact(-quarter_turn_angle_2()),
                     "P échange les coordonnées 2 et 4 : le bloc du plan (2, 3) de PᵀDP vient du plan (3, 4) de D":
                         exact(-sp.pi / 3)}'''),
    ]),

    Paper("MB3.3", "La direction du vent : l'encoder par (cos, sin), la distance entre deux encodages, un vent qui tourne "
                   "comme une rotation de l'encodage, et la direction moyenne de trois relevés", [
        ("a", "a list of 2 numbers (4 decimals)", "floats(wind(150))",
         '''decimals=4,
           mistakes={"l'encodage est (cos θ, sin θ) : le cosinus d'abord": floats(wind(150)[::-1]),
                     "les angles sont en degrés : convertis-les en radians avant cos et sin":
                         floats([math.cos(150), math.sin(150)])}'''),
        ("b", "a number (4 decimals)", "float(np.sum((wind(340) - wind(20)) ** 2))",
         '''decimals=4,
           mistakes={"la question demande le carré de la distance": float(np.linalg.norm(wind(340) - wind(20))),
                     "pour deux vecteurs unitaires, ‖u − v‖² = 2 − 2 u·v": float(1 - wind(340) @ wind(20)),
                     "les angles sont en degrés : convertis-les en radians avant cos et sin":
                         2 - 2 * math.cos(340 - 20)}'''),
        ("c", "a list of 2 numbers (4 decimals)", "floats(rot(45) @ wind(150))",
         '''decimals=4,
           mistakes={"le vent tourne dans le sens inverse des aiguilles d'une montre : son angle augmente":
                         floats(rot(-45) @ wind(150)),
                     "le cosinus d'une somme n'est pas la somme des cosinus": floats(wind(150) + wind(45))}'''),
        ("d", BOOL, "all(np.allclose(wind(t + 45), rot(45) @ wind(t)) for t in range(0, 360, 15))",
         '''mistakes={"e(θ + 45°) = R_{45°} e(θ), et R_{45°} ne dépend pas de θ": False}'''),
        ("e", "a number, in degrees", "mean_direction_3(READINGS_3)",
         '''decimals=6,
           mistakes={"on moyenne les vecteurs (cos θ, sin θ), pas les angles": float(np.mean(READINGS_3)),
                     "la question demande des degrés": math.radians(mean_direction_3(READINGS_3))}'''),
        ("f", "a number (3 decimals)", "float(np.linalg.norm(np.mean([wind(t) for t in READINGS_3], axis=0)))",
         '''decimals=3,
           mistakes={"c'est la norme du vecteur moyen, pas celle de la somme des trois vecteurs":
                         float(np.linalg.norm(np.sum([wind(t) for t in READINGS_3], axis=0))),
                     "la norme est la racine de la somme des carrés":
                         float(np.sum(np.mean([wind(t) for t in READINGS_3], axis=0) ** 2))}'''),
    ]),

    Paper("MB3.4", "L'estimateur de Nadaraya-Watson : la température d'un refuge à partir de quatre stations de montagne, "
                   "pour deux largeurs de bande, et ses deux limites", [
        ("a", "a list of 4 numbers: Val, Bergerie, Col, Pic", "floats(scores_4(200))",
         '''decimals=6,
           mistakes={"le noyau gaussien divise par 2h², pas par h²": floats(2 * scores_4(200)),
                     "le score d'un noyau gaussien est un carré changé de signe : il est négatif ou nul":
                         floats(-scores_4(200)),
                     "le noyau divise le carré de l'écart par 2h², pas l'écart lui-même":
                         floats(-np.abs(REFUGE_4 - ALT_4) / (2 * 200))}'''),
        ("b", "a number (3 decimals)", "float(softmax(scores_4(200))[1])",
         '''decimals=3,
           mistakes={"un poids se normalise : divise par la somme des quatre noyaux": float(np.exp(scores_4(200))[1]),
                     "le poids est l'exponentielle du score, pas le score divisé par la somme des scores":
                         float(scores_4(200)[1] / scores_4(200).sum())}'''),
        ("c", "a number (2 decimals), in °C", "float(softmax(scores_4(200)) @ TEMP_4)",
         '''decimals=2,
           mistakes={"la prévision divise par la somme des noyaux": float(np.exp(scores_4(200)) @ TEMP_4),
                     "le score d'un noyau gaussien est négatif : une station lointaine pèse moins":
                         float(softmax(-scores_4(200)) @ TEMP_4)}'''),
        ("d", "a list of 4 numbers (4 decimals): Val, Bergerie, Col, Pic", "floats(softmax(scores_4(400)))",
         '''decimals=4,
           mistakes={"doubler h divise les scores par 4, pas par 2": floats(softmax(scores_4(200) / 2)),
                     "les poids d'une loi somment à 1": floats(np.exp(scores_4(400)))}'''),
        ("e", "a number (2 decimals), in °C", "float(softmax(scores_4(400)) @ TEMP_4)",
         '''decimals=2,
           mistakes={"doubler h divise les scores par 4, pas par 2": float(softmax(scores_4(200) / 2) @ TEMP_4),
                     "la prévision est une moyenne pondérée : divise par la somme des noyaux":
                         float(np.exp(scores_4(400)) @ TEMP_4)}'''),
        ("f", "a number (2 decimals), in °C", "float(TEMP_4[np.argmin(np.abs(ALT_4 - REFUGE_4))])",
         '''decimals=2,
           mistakes={"quand h → 0, le rapport des poids de deux stations d'écarts différents tend vers l'infini":
                         float(np.mean(TEMP_4[np.argsort(np.abs(ALT_4 - REFUGE_4))[:2]])),
                     "les poids se renormalisent : leur somme reste 1 même quand h → 0": 0.0}'''),
        ("g", "a number (2 decimals), in °C", "float(np.mean(TEMP_4))",
         '''decimals=2,
           mistakes={"quand h → ∞, les quatre scores tendent vers 0 : les poids deviennent égaux":
                         float(np.mean(TEMP_4[np.argsort(np.abs(ALT_4 - REFUGE_4))[:2]])),
                     "quand h → ∞, aucune station ne l'emporte, pas même la plus lointaine":
                         float(TEMP_4[np.argmax(np.abs(ALT_4 - REFUGE_4))])}'''),
    ]),

    Paper("MB3.5", "Masques : une moyenne exponentielle normalisée vue comme une softmax sur les jours passés, puis la même "
                   "quand un capteur tombe en panne un jour (un score −∞)", [
        ("a", "a list of 4 exact values (fractions between quotes allowed): days 1 to 4", "floats(weights_5(4))",
         '''decimals=6,
           mistakes={"le jour le plus récent a le plus grand poids": floats(weights_5(4)[::-1]),
                     "les poids d'une loi somment à 1": floats(raw_weights_5(4))}'''),
        ("b", 'an irreducible fraction, between quotes', "smoothed_5(weights_5(4))",
         '''kind="fraction", simplified=True,
           mistakes={"le jour le plus récent a le plus grand poids": smoothed_5(weights_5(4)[::-1]),
                     "la moyenne pondérée divise par la somme des poids": smoothed_5(raw_weights_5(4))}'''),
        ("c", "a list of 4 exact values: days 1 to 4", "floats(weights_5(2))",
         '''decimals=6,
           mistakes={"les deux jours connus gardent des scores différents, linéaires en le temps":
                         floats([F(1, 2), F(1, 2), 0, 0]),
                     "au jour 2, le jour 2 a le score 0 et le jour 1 le score −ln 2": floats(weights_5(2)[1::-1] + [0, 0])}'''),
        ("d", "a list of 4 exact values: days 1 to 4", "floats(weights_5(4, broken=BROKEN_5))",
         '''decimals=6,
           mistakes={"le jour de la panne est retiré : son poids est nul, et les autres se renormalisent":
                         floats(kept_but_renormalised_5()),
                     "la panne ne décale pas les jours : le jour 1 garde son score −3 ln 2":
                         floats(shifted_weights_5())}'''),
        ("e", 'an irreducible fraction, between quotes', "smoothed_5(weights_5(4, broken=BROKEN_5))",
         '''kind="fraction", simplified=True,
           mistakes={"un relevé manquant n'est pas un relevé nul : on retire le jour":
                         sum(w * (0 if day == BROKEN_5 else t) for day, (w, t) in enumerate(zip(weights_5(4), POOL_5), start=1)),
                     "la panne ne décale pas les jours : le jour 1 garde son score −3 ln 2": smoothed_5(shifted_weights_5())}'''),
        ("f", BOOL, "weights_5(4, broken=BROKEN_5) == conditioned_5(weights_5(4), BROKEN_5)",
         '''mistakes={"un score −∞ restreint la loi à un sous-ensemble et la renormalise : c'est une loi conditionnelle":
                         False}'''),
    ]),

    Paper("MB3.6", "La saturation d'une softmax : trois scores multipliés par un facteur c croissant, le poids maximal, la "
                   "sensibilité 1 − Σ pᵢ² et la borne (K − 1) e^{−cΔ}", [
        ("a", "a list of 3 numbers (4 decimals): c = 1, 2, 6", "[float(softmax(c * ROUTES_6).max()) for c in (1, 2, 6)]",
         '''decimals=4,
           mistakes={"multiplier les scores par c n'est pas multiplier les poids par c":
                         [c * float(softmax(ROUTES_6).max()) for c in (1, 2, 6)],
                     "les poids se normalisent par la somme des trois exponentielles":
                         [float(np.exp(c * ROUTES_6).max()) for c in (1, 2, 6)],
                     "multiplier les scores par c change les poids : on reprend la softmax de c·s":
                         [float(softmax(ROUTES_6).max())] * 3}'''),
        ("b", "a number (4 decimals)", "float(1 - np.sum(softmax(6 * ROUTES_6) ** 2))",
         '''decimals=4,
           mistakes={"c'est 1 moins la somme des carrés des poids, pas 1 moins le carré de leur somme":
                         float(1 - np.sum(softmax(6 * ROUTES_6)) ** 2),
                     "la sensibilité est 1 − Σ pᵢ², pas Σ pᵢ²": float(np.sum(softmax(6 * ROUTES_6) ** 2)),
                     "c'est 1 − Σ pᵢ², pas 1 − p_max": float(1 - softmax(6 * ROUTES_6).max())}'''),
        ("c", "a number (5 decimals)", "(K_6 - 1) * math.exp(-6 * GAP_6)",
         '''decimals=5,
           mistakes={"Δ est l'écart entre le plus grand score et le suivant, pas le dernier":
                         (K_6 - 1) * math.exp(-6 * (ROUTES_6.max() - ROUTES_6.min())),
                     "il y a K − 1 = 2 autres scores": K_6 * math.exp(-6 * GAP_6),
                     "l'exposant de la borne contient c": (K_6 - 1) * math.exp(-GAP_6)}'''),
        ("d", "a number (2 decimals)", "math.log((K_6 - 1) / (1 - TARGET_6)) / GAP_6",
         '''decimals=2,
           mistakes={"la borne vaut (K − 1) e^{−cΔ} : il reste le facteur 2": math.log(1 / (1 - TARGET_6)) / GAP_6,
                     "on résout avec le logarithme népérien": math.log10((K_6 - 1) / (1 - TARGET_6)) / GAP_6,
                     "Δ = 0,8 est l'écart entre les deux plus grands scores":
                         math.log((K_6 - 1) / (1 - TARGET_6)) / (ROUTES_6.max() - ROUTES_6.min())}'''),
        ("e", BOOL, "bool(1 - np.sum(softmax(60 * ROUTES_6) ** 2) < 1e-12)",
         '''mistakes={"quand c grandit, la loi tend vers le one-hot du plus grand score, dont Σ pᵢ² vaut 1": False}'''),
    ]),

    Paper("MB3.7", "La softmax en ligne à la main : neuf scores (des multiples de ln 2) lus par blocs de trois, l'état "
                   "(m, l, a) après chaque bloc, la moyenne pondérée finale, puis la fusion de deux états", [
        ("a", "a list of 3 exact values: [m / ln 2, l, a]", "floats(states_7(K_7, V_7)[0])",
         '''decimals=6,
           mistakes={"l et a s'écrivent par rapport au plus grand score lu : chaque terme est e^{s_j − m}":
                         floats(absolute_state_7(K_7[:3], V_7[:3])),
                     "a pondère chaque valeur par e^{s_j − m}": floats(states_7(K_7, V_7)[0][:2] + [sum(V_7[:3])])}'''),
        ("b", "a list of 3 exact values: [m / ln 2, l, a]", "floats(states_7(K_7, V_7)[1])",
         '''decimals=6,
           mistakes={"quand le maximum change, l'ancien l et l'ancien a se multiplient par e^{m_ancien − m_nouveau}":
                         floats(states_7(K_7, V_7, mode="none")[1]),
                     "l et a se remettent tous les deux à l'échelle": floats(states_7(K_7, V_7, mode="l only")[1])}'''),
        ("c", "a list of 3 exact values: [m / ln 2, l, a]", "floats(states_7(K_7, V_7)[2])",
         '''decimals=6,
           mistakes={"on ne remet à l'échelle que si le maximum augmente strictement":
                         floats(states_7(K_7, V_7, mode="halve on ties")[2]),
                     "quand le maximum change, l'ancien l et l'ancien a se multiplient par e^{m_ancien − m_nouveau}":
                         floats(states_7(K_7, V_7, mode="none")[2]),
                     "l et a se remettent tous les deux à l'échelle": floats(states_7(K_7, V_7, mode="l only")[2])}'''),
        ("d", 'an irreducible fraction, between quotes', "states_7(K_7, V_7)[2][2] / states_7(K_7, V_7)[2][1]",
         '''kind="fraction", simplified=True,
           mistakes={"la moyenne pondérée est a/l, pas a": states_7(K_7, V_7)[2][2],
                     "la moyenne pondérée par la softmax n'est pas la moyenne simple des valeurs": F(sum(V_7), len(V_7))}'''),
        ("e", "a list of 3 exact values: [m / ln 2, l, a]", "floats(states_7(K_7[3:], V_7[3:])[-1])",
         '''decimals=6,
           mistakes={"chaque terme est e^{s_j − m}, avec m le plus grand score lu par B":
                         floats(absolute_state_7(K_7[3:], V_7[3:])),
                     "la machine B ne connaît pas l'état de A : son m est le plus grand des scores qu'elle lit":
                         floats(relative_state_7(K_7[3:], V_7[3:], max(K_7[:3])))}'''),
        ("f", "a list of 3 exact values: [m / ln 2, l, a]",
         "floats(merge_7(states_7(K_7[:3], V_7[:3])[-1], states_7(K_7[3:], V_7[3:])[-1]))",
         '''decimals=6,
           mistakes={"chaque état se remet à l'échelle du maximum commun avant d'additionner":
                         floats(merge_7(states_7(K_7[:3], V_7[:3])[-1], states_7(K_7[3:], V_7[3:])[-1], mode="none")),
                     "la fusion additionne les l et les a, elle ne les moyenne pas":
                         floats(merge_7(states_7(K_7[:3], V_7[:3])[-1], states_7(K_7[3:], V_7[3:])[-1], mode="mean"))}'''),
        ("g", "a number (4 decimals)", "lse_7(states_7(K_7, V_7)[2])",
         '''decimals=4,
           mistakes={"m vaut 4 ln 2, pas 4": float(states_7(K_7, V_7)[2][0] + math.log(states_7(K_7, V_7)[2][1])),
                     "le log-sum-exp ajoute ln l à m":
                         float(states_7(K_7, V_7)[2][0] * math.log(2) * states_7(K_7, V_7)[2][1])}'''),
    ]),

    Paper("MB3.11", "Pont : à normes égales, les poids d'un noyau gaussien sont une softmax des produits scalaires divisés "
                    "par h², sur quatre pluviomètres d'un même cercle", [
        ("a", "a list of 4 integers", "floats(GAUGES_11 @ X_11)",
         '''decimals=0,
           mistakes={"le produit scalaire additionne les produits des coordonnées de même rang":
                         floats(GAUGES_11 @ X_11[::-1]),
                     "x·xᵢ = ‖x‖ ‖xᵢ‖ cos(φ − φᵢ) : le cosinus compte":
                         floats(np.linalg.norm(GAUGES_11, axis=1) * np.linalg.norm(X_11))}'''),
        ("b", "a list of 4 integers", "floats(np.sum((GAUGES_11 - X_11) ** 2, axis=1))",
         '''decimals=0,
           mistakes={"‖x − xᵢ‖² = ‖x‖² − 2 x·xᵢ + ‖xᵢ‖² : le double produit compte deux fois":
                         floats(X_11 @ X_11 + np.sum(GAUGES_11 ** 2, axis=1) - GAUGES_11 @ X_11),
                     "la question demande le carré de la distance": floats(np.linalg.norm(GAUGES_11 - X_11, axis=1))}'''),
        ("c", "a list of 4 numbers (4 decimals)", "floats(softmax(gauge_scores_11(5)))",
         '''decimals=4,
           mistakes={"le noyau gaussien divise par 2h², pas par h²": floats(softmax(2 * gauge_scores_11(5))),
                     "les poids d'une loi somment à 1": floats(np.exp(gauge_scores_11(5))),
                     "le score est −‖x − xᵢ‖²/(2h²) : il est négatif": floats(softmax(-gauge_scores_11(5)))}'''),
        ("d", BOOL, "bool(np.allclose(softmax(gauge_scores_11(5)), softmax(GAUGES_11 @ X_11 / 5 ** 2)))",
         '''mistakes={"‖x‖² et ‖xᵢ‖² sont les mêmes pour les quatre pluviomètres : ils disparaissent dans la softmax":
                         False}'''),
        ("e", "a number (2 decimals), in mm", "float(softmax(gauge_scores_11(5)) @ RAIN_11)",
         '''decimals=2,
           mistakes={"la prévision pondère les pluies relevées par les poids du noyau": float(np.mean(RAIN_11)),
                     "la prévision est une moyenne pondérée : divise par la somme des noyaux":
                         float(np.exp(gauge_scores_11(5)) @ RAIN_11)}'''),
        ("f", "a number (3 decimals)", "float(softmax(gauge_scores_11(2.5)).max())",
         '''decimals=3,
           mistakes={"diviser h par 2 multiplie les scores par 4, pas par 2": float(softmax(2 * gauge_scores_11(5)).max()),
                     "diviser h par 2 multiplie les scores x·xᵢ/h² : les poids changent":
                         float(softmax(gauge_scores_11(5)).max())}'''),
        ("g", BOOL, "bool(np.allclose(softmax(gauge_scores_11(5, INSIDE_11)), softmax(GAUGES_11 @ INSIDE_11 / 5 ** 2)))",
         '''mistakes={"seuls les ‖xᵢ‖² doivent être égaux : ‖x‖² est le même pour les quatre termes": False}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (SymPy and exact fractions where the calculation is exact)
import math
from fractions import Fraction as F

import numpy as np
import sympy as sp


def floats(values):
    """A number, a vector or a matrix (fractions, NumPy) as a float or nested lists of floats (-0.0 written 0.0)."""
    return (np.round(np.asarray(values, dtype=float), 12) + 0.0).tolist()


def exact(expr):
    """An exact value (SymPy) as the text the learner types (sqrt, pi)."""
    return str(sp.nsimplify(expr))


def deg(angle):
    """An angle in degrees as an exact number of radians (SymPy)."""
    return sp.pi * sp.Rational(angle) / 180


def rot(angle):
    """The rotation R_θ of the plane, θ in degrees (NumPy)."""
    t = math.radians(angle)
    return np.array([[math.cos(t), -math.sin(t)], [math.sin(t), math.cos(t)]])


def softmax(s):
    """The softmax of a vector of scores, the largest score subtracted first."""
    s = np.asarray(s, dtype=float)
    w = np.exp(s - s.max())
    return w / w.sum()


# MB3.1: an arm of 4 dm and a forearm of 2 dm; the shoulder turns by 60°, the elbow by 45° more
ARM_1 = np.array([4.0, 2.0])
SHOULDER_1, ELBOW_1 = 60, 45


def gripper_1(arm_angle, forearm_angle, arm=ARM_1):
    """R_{arm angle} (arm, 0) + R_{forearm angle} (forearm, 0), the angles in degrees."""
    return rot(arm_angle) @ np.array([arm[0], 0.0]) + rot(forearm_angle) @ np.array([arm[1], 0.0])


P_1 = gripper_1(SHOULDER_1, SHOULDER_1 + ELBOW_1)


# MB3.2: Givens rotations R_ij(θ), coordinates numbered from 1 as on paper (e_i turned towards e_j)
def givens(n, i, j, theta):
    G = np.eye(n)
    G[i - 1, i - 1] = G[j - 1, j - 1] = math.cos(theta)
    G[j - 1, i - 1], G[i - 1, j - 1] = math.sin(theta), -math.sin(theta)
    return G


def commute(A, B):
    return bool(np.allclose(A @ B, B @ A))


E2_2 = np.array([0.0, 1.0, 0.0])
D_2 = givens(4, 1, 2, math.pi / 3) @ givens(4, 3, 4, math.pi / 2)
SIGMA_2 = {1: 1, 2: 4, 3: 3, 4: 2}                                       # sigma swaps the coordinates 2 and 4
P_2 = np.array([[1.0 if j == SIGMA_2[i] else 0.0 for j in range(1, 5)] for i in range(1, 5)])   # rows e_sigma(i)
PDP_2 = P_2.T @ D_2 @ P_2
PLANES_2 = [(1, 2), (3, 4)]                                              # the planes of D, angles pi/3 then pi/2


def planes_2(sigma):
    """The planes (sigma(i), sigma(j)) of PᵀDP, numbered from 1."""
    return [[sigma[i], sigma[j]] for i, j in PLANES_2]


assert np.allclose(PDP_2, givens(4, *planes_2(SIGMA_2)[0], math.pi / 3) @ givens(4, *planes_2(SIGMA_2)[1], math.pi / 2))


def quarter_turn_angle_2():
    """The angle theta of R_23(theta) in PᵀDP = R_14(pi/3) R_23(theta), read on the block of the coordinates 2 and 3."""
    theta = math.atan2(PDP_2[2, 1], PDP_2[1, 1])
    angle = sp.nsimplify(round(theta / math.pi, 12)) * sp.pi
    assert np.allclose(PDP_2, givens(4, 1, 4, math.pi / 3) @ givens(4, 2, 3, float(angle)))
    return angle


# MB3.3: wind directions in degrees (east 0°, north 90°)
def wind(theta):
    return np.array([math.cos(math.radians(theta)), math.sin(math.radians(theta))])


READINGS_3 = [330, 20, 70]


def mean_direction_3(angles):
    mean = np.mean([wind(t) for t in angles], axis=0)
    return math.degrees(math.atan2(mean[1], mean[0])) % 360


# MB3.4: a refuge at 2 300 m; stations Val, Bergerie, Col, Pic
REFUGE_4 = 2300.0
ALT_4 = np.array([1700.0, 2100.0, 2700.0, 3100.0])
TEMP_4 = np.array([10.4, 6.3, 2.2, -1.7])


def scores_4(h):
    return -(REFUGE_4 - ALT_4) ** 2 / (2 * h ** 2)


# MB3.5: the water of a pond, days 1 to 4; lambda = 1/2; the sensor broken on day 3
POOL_5 = [18, 15, 21, 17]
LAMBDA_5, BROKEN_5 = F(1, 2), 3


def raw_weights_5(t):
    """lambda^(t - u) for the days u <= t, 0 for the later days (exact)."""
    return [LAMBDA_5 ** (t - u) if u <= t else F(0) for u in range(1, 5)]


def weights_5(t, broken=None):
    """The softmax of the scores u ln 2 over the days u <= t (and u != broken): exact fractions."""
    raw = [0 if u == broken else w for u, w in enumerate(raw_weights_5(t), start=1)]
    return [F(w) / sum(raw) for w in raw]


def kept_but_renormalised_5():
    """The classic error: the others renormalised without the broken day, but its weight kept."""
    kept = sum(w for u, w in enumerate(raw_weights_5(4), start=1) if u != BROKEN_5)
    return [w / kept for w in raw_weights_5(4)]


def shifted_weights_5():
    """The classic error: the days after the broken one moved back one day (day 1 weighted lambda², not lambda³)."""
    ages = {4: 0, 2: 1, 1: 2}
    raw = [LAMBDA_5 ** ages[u] if u in ages else F(0) for u in range(1, 5)]
    return [w / sum(raw) for w in raw]


def smoothed_5(weights):
    return sum(F(w) * t for w, t in zip(weights, POOL_5))


def conditioned_5(weights, day):
    """The law of weights conditioned on « the day is not day »."""
    return [F(0) if u == day else F(w) / (1 - weights[day - 1]) for u, w in enumerate(weights, start=1)]


# MB3.6: three routes, scores s; K = 3; Delta, the gap between the largest score and the next
ROUTES_6 = np.array([1.3, 0.5, -0.8])
K_6, TARGET_6 = 3, 0.99
GAP_6 = float(np.sort(ROUTES_6)[-1] - np.sort(ROUTES_6)[-2])


# MB3.7: nine beacons, s_j = k_j ln 2, read by blocks of 3; a state written [m / ln 2, l, a] with exact fractions
K_7 = [1, 3, 0, 2, -1, 4, 0, 4, 2]
V_7 = [4, 10, 6, 3, 8, 2, 9, 5, 7]


def states_7(ks, vs, size=3, mode="right"):
    """The states [m / ln 2, l, a] after each block (e^(s - m) = 2^(k - m / ln 2), exact). mode: "right"; the classic
    errors "none" (nothing rescaled), "l only" (a never rescaled), "halve on ties" (rescaled by 1/2 even when the
    maximum does not change)."""
    m, l, a, out = None, F(0), F(0), []
    for start in range(0, len(ks), size):
        block_k, block_v = ks[start:start + size], vs[start:start + size]
        new = max(block_k) if m is None else max(m, max(block_k))
        if m is None:
            factor = F(0)
        elif mode == "none":
            factor = F(1)
        elif mode == "halve on ties" and new == m:
            factor = F(1, 2)
        else:
            factor = F(2) ** (m - new)
        weights = [F(2) ** (k - new) for k in block_k]
        l = l * factor + sum(weights)
        a = a * (F(1) if mode == "l only" and m is not None else factor) + sum(w * v for w, v in zip(weights, block_v))
        m = new
        out.append([m, l, a])
    return out


def absolute_state_7(ks, vs):
    """The classic error: [m / ln 2, sum of e^s, sum of e^s v], without subtracting m."""
    return [max(ks), sum(F(2) ** k for k in ks), sum(F(2) ** k * v for k, v in zip(ks, vs))]


def relative_state_7(ks, vs, m0):
    """The classic error: the sums relative to m0 / ln 2, the maximum of another machine."""
    return [m0, sum(F(2) ** (k - m0) for k in ks), sum(F(2) ** (k - m0) * v for k, v in zip(ks, vs))]


def merge_7(s1, s2, mode="right"):
    """The merge of two states [m / ln 2, l, a]; the classic errors "none" (no rescaling) and "mean"."""
    m = max(s1[0], s2[0])
    f1, f2 = (F(1), F(1)) if mode == "none" else (F(2) ** (s1[0] - m), F(2) ** (s2[0] - m))
    l, a = s1[1] * f1 + s2[1] * f2, s1[2] * f1 + s2[2] * f2
    return [m, l / 2, a / 2] if mode == "mean" else [m, l, a]


def lse_7(state):
    return float(state[0] * math.log(2) + math.log(state[1]))


# MB3.11: four rain gauges on the shore of a circular lake of radius 5 km; the point x on the shore; a point inside
GAUGES_11 = np.array([[5.0, 0], [0, 5], [-3, -4], [4, -3]])
RAIN_11 = np.array([18.0, 30, 11, 22])
X_11, INSIDE_11 = np.array([3.0, -4.0]), np.array([1.0, 2.0])


def gauge_scores_11(h, x=X_11):
    return -np.sum((GAUGES_11 - x) ** 2, axis=1) / (2 * h ** 2)'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ MB3.1 à MB3.7 ; 🔗 MB3.11)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question "
               "(« a number » sans décimales : la valeur exacte, ces calculs tombent juste) ;\n"
               "- une valeur exacte entre guillemets, avec `sqrt`, `pi` et des fractions, `\"sqrt(5)/3\"` ;\n"
               "- une fraction irréductible entre guillemets, `\"5/8\"` ;\n"
               "- une liste `[0.2, -1]`, dans l'ordre que dit la question ; une liste de valeurs exactes peut contenir "
               "des fractions entre guillemets, `[\"1/6\", 0, \"5/6\"]` ; une matrice comme la liste de ses **lignes**, "
               "`[[1, 0], [-2, 3]]` (une liste de couples s'écrit de même) ;\n"
               "- `True` ou `False` pour un vrai ou faux.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")


def paper_part(kind: str) -> list:
    """The cells of Part 0."""
    return paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO)


# ---------------------------------------------------------------------------
# Notebook exercises: your library (MB3.14, MB3.15, MB3.16)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to D)
import math
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np

from wbm.errors import MymathMissingError
from wbm.nbtools import StopCheck, checked, drawn, filled, fr, run_pytest_group, verdict

TEST_MB3 = "tests/test_mb3_positional.py"           # the tests of mymath/positional.py
REF = wbm.load_mymath("ref", alias="mymath_ref")  # the reference: the checks of the hidden cases rely on it
ref_pos = REF.positional
LN2 = math.log(2)


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
    """True when got is an array of numbers of the shape of want and equal to it up to rounding, an infinity equal to
    the same infinity (no error for an odd got)."""
    arr = as_floats(got)
    want = np.asarray(want, dtype=float)
    return arr is not None and arr.shape == want.shape and bool(np.allclose(arr, want, rtol=rtol, atol=atol))


def state_parts(state):
    """(m, l, acc as a float array or None) of a state (m, l, acc), or None when it is not one."""
    try:
        m, l, acc = state
        return float(m), float(l), None if acc is None else np.atleast_1d(np.asarray(acc, dtype=float))
    except (TypeError, ValueError):
        return None


def same_state(got, want, rtol=1e-9):
    """True when got is a state equal to want: the m both -inf or within rtol·max(1, |m|), the l within rtol·max(1, l),
    the acc equal by np.allclose (no error for an odd got)."""
    a, b = state_parts(got), state_parts(want)
    if a is None or b is None:
        return False
    (m1, l1, c1), (m2, l2, c2) = a, b
    if (m1 == -math.inf) != (m2 == -math.inf):
        return False
    if m2 != -math.inf and not abs(m1 - m2) <= rtol * max(1.0, abs(m2)):
        return False
    if not abs(l1 - l2) <= rtol * max(1.0, abs(l2)):
        return False
    if (c1 is None) != (c2 is None):
        return False
    return c1 is None or (c1.shape == c2.shape and bool(np.allclose(c1, c2, rtol=rtol,
                                                                     atol=rtol * max(1.0, float(np.abs(c2).max())))))


def drawn_points(ax):
    """All the points drawn in ax: those of its lines with a marker and of its scatters."""
    points = []
    for line in ax.lines:
        if line.get_marker() in (None, "", " ", "None", "none"):
            continue
        points += list(zip(np.asarray(line.get_xdata(), dtype=float).ravel(),
                           np.asarray(line.get_ydata(), dtype=float).ravel()))
    for collection in ax.collections:
        offsets = np.asarray(collection.get_offsets(), dtype=float)
        if offsets.ndim == 2 and offsets.shape[1] == 2 and type(collection).__name__ == "PathCollection":
            points += [tuple(p) for p in offsets]
    return points


def points_at(ax, xs, ys, rtol=1e-7, atol=1e-9):
    """True when every point (xs[k], ys[k]) is drawn in ax (a line with markers, or a scatter)."""
    points = np.array(drawn_points(ax) or [(np.nan, np.nan)], dtype=float)
    return all(np.any(np.isclose(points[:, 0], x, rtol=rtol, atol=atol) & np.isclose(points[:, 1], y, rtol=rtol, atol=atol))
               for x, y in zip(np.atleast_1d(xs), np.atleast_1d(ys)))


def line_with(ax, xs, ys, rtol=1e-7, atol=1e-9):
    """True when a line of ax has exactly the abscissas xs and the ordinates ys."""
    xs, ys = np.asarray(xs, dtype=float), np.asarray(ys, dtype=float)
    for line in ax.lines:
        x, y = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
        if x.shape == xs.shape and y.shape == ys.shape and np.allclose(x, xs, rtol=rtol, atol=atol) \\
                and np.allclose(y, ys, rtol=rtol, atol=atol):
            return True
    return False


def name_near(ax, name, x, y, span):
    """True when a text of ax writes name next to the point (x, y): the point annotated (ax.annotate) or the position
    of the text (ax.text), within a tenth of span."""
    for text in ax.texts:
        if text.get_text().strip() != name:
            continue
        px, py = (text.xy if hasattr(text, "xy") else text.get_position())
        if abs(float(px) - x) <= 0.1 * span and abs(float(py) - y) <= 0.1 * span:
            return True
    return False


def call_safely(label, function, *args, **kwargs):
    """function(*args, **kwargs); an error of the learner's code becomes one ❌ line naming the call (StopCheck)."""
    try:
        return function(*args, **kwargs)
    except (NotImplementedError, MymathMissingError):
        raise
    except Exception as exc:  # noqa: BLE001 - the learner's error, reported with the name of the call
        print(f"❌ {label} : ton code lève {type(exc).__name__} : {str(exc)[:200]}")
        raise StopCheck from None'''

DATA = '''# The data of the paper exercises (02_exercices.md)
ARM = {"arm": 4.0, "forearm": 2.0, "shoulder_deg": 60, "elbow_deg": 45}       # MB3.1: lengths in dm, angles in degrees
E2 = np.array([0.0, 1.0, 0.0])                                             # MB3.2: the basis vector e_2 of space
WINDS = np.array([150.0, 340.0, 20.0, 330.0, 70.0])                        # MB3.3: directions in degrees (east 0°)
ALTITUDES = np.array([1700.0, 2100.0, 2700.0, 3100.0])                     # MB3.4: Val, Bergerie, Col, Pic (m), the
TEMPERATURES = np.array([10.4, 6.3, 2.2, -1.7])                            # temperatures (°C); the refuge at 2 300 m
POND = np.array([18.0, 15.0, 21.0, 17.0])                                  # MB3.5: days 1 to 4 (°C), lambda = 1/2
ROUTES = np.array([1.3, 0.5, -0.8])                                        # MB3.6: the scores of the three routes
K_7 = np.array([1.0, 3, 0, 2, -1, 4, 0, 4, 2])                             # MB3.7: the beacons, s_j = k_j ln 2,
S_7 = K_7 * LN2                                                            # read by blocks of 3
V_7 = np.array([4.0, 10, 6, 3, 8, 2, 9, 5, 7])                             # their values
GAUGES = np.array([[5.0, 0.0], [0.0, 5.0], [-3.0, -4.0], [4.0, -3.0]])     # MB3.11: the rain gauges (km), their
RAIN = np.array([18.0, 30.0, 11.0, 22.0])                                  # rain (mm); the point x = (3, -4)
for _array in (E2, WINDS, ALTITUDES, TEMPERATURES, POND, ROUTES, K_7, S_7, V_7, GAUGES, RAIN):
    _array.setflags(write=False)   # read only: a change in place raises an error at the line that does it'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="MB3")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en MB2). Ouvre ta copie `mon_travail/mymath/positional.py`, lis la "
         "docstring du module (ses conventions, et ce qui est permis) puis celle de la fonction, remplace chaque "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Dans le notebook, appelle tes fonctions par "
         "`mymath.positional.<nom>` (par exemple `mymath.positional.givens_rotation(3, 0, 1, 0.2)`), ou donne-leur un "
         "nom court (`givens_rotation = mymath.positional.givens_rotation`) dans une cellule exécutée après le "
         "rechargement. ⚠️ Le squelette n'importe rien : ajoute en tête du fichier `import math` et `import numpy as "
         "np`. NumPy et le module `math` sont permis, mais aucune fonction de SciPy (`scipy.special.softmax`, "
         "`scipy.special.logsumexp`, `scipy.spatial.transform.Rotation`) ni `np.logaddexp` : les tests comparent tes "
         "résultats aux leurs, et un test lit ton module. Les indices des coordonnées partent de 0 ; ne modifie "
         "jamais les tableaux reçus. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy.")

REMINDER = ("> Même mode d'emploi qu'en MB3.14 : écris la fonction dans ta copie `mon_travail/mymath/positional.py`, "
            "**enregistre**, puis exécute les cellules ci-dessous ; la première recharge ta librairie.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of positional.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("todo", f'run_pytest_group(TEST_MB3, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_MB3, "{keyword}", impl="ref")')]


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


# « Ce qu'il faut regarder » of 02_exercices.md (questions only), shown after the checks; the answers are in
# 05_solutions.md, never in the notebook
LOOK_14 = ("que fait `givens_rotation(3, 0, 2, 0.4)` par rapport à la matrice (3.78) ? Qu'ont en commun les plans des deux "
           "rotations qui ne commutent pas ?")
LOOK_15 = ("combien de fois $m$ change-t-il dans a), et à quels blocs ? Que rend le calcul direct de c), et pourquoi le "
           "tien n'a-t-il pas ce problème ? Que vaudrait, pour d), la moyenne des quatre angles ?")
LOOK_16 = "quel grand calcul ces égalités permettent-elles de partager, et entre quoi ?"

# ---------------------------------------------------------------------------
# MB3.14 · givens_rotation
# ---------------------------------------------------------------------------
NOTE_14 = (r"Les contrôles (entiers refusés s'ils sont booléens, `math.isfinite(theta)`), puis `G = np.eye(n)`, "
           r"`G[i, i] = G[j, j] = math.cos(theta)`, `G[j, i] = math.sin(theta)`, `G[i, j] = -math.sin(theta)`. a) "
           r"$(-0{,}866025 ;\ 0 ;\ 0{,}5 ;\ 0 ;\ 0 ;\ 1)$, comme MB3.2 a) et b). b) $(2, 0)$ : (3.78) tourne "
           r"$\mathbf{e}_3$ vers $\mathbf{e}_1$, et `givens_rotation(3, 0, 2, 0.4)` est sa transposée. c) "
           r"$\approx 0{,}7211$, puis 0 : les plans qui partagent la coordonnée d'indice 2 ne commutent pas, les plans "
           r"disjoints commutent.")

MB3_14 = Ex(
    "MB3.14", "🔨", 1, 15, "La matrice d'une rotation de Givens de ℝⁿ · `givens_rotation`",
    "programmer la matrice d'une rotation de Givens, puis s'en servir pour retrouver MB3.2, une matrice de MML et la "
    "commutation de deux rotations.",
    "fiche §3 ; MML §3.9.3 ; Ex MB3.2", tracks="C, E", mymath="positional.py", note=NOTE_14,
    body=HOWTO + r"""

Écris `givens_rotation(n, i, j, theta)` (fiche §3), en suivant sa docstring : contrôle $n$ (un entier $\ge 2$, ni un booléen ni un flottant comme `3.0`), $i$ et $j$ (deux entiers différents de $[0, n - 1]$) et $\theta$ (un réel fini, pas un booléen) ; pars de `np.eye(n)` et change les quatre coefficients du plan $(i, j)$.

**L'usage.** Avec ta fonction :
- a) les deux vecteurs de MB3.2 a) et b), avec `givens_rotation(3, 1, 2, np.pi / 2)` pour $\mathbf{R}_{23}(\frac\pi2)$ et `givens_rotation(3, 0, 1, np.pi / 3)` pour $\mathbf{R}_{12}(\frac\pi3)$, et le vecteur `E2` de la cellule de données (une liste de 6 nombres : le vecteur de a), puis celui de b), à comparer à ta copie) ;
- b) écris la matrice (3.78) de MML pour $\theta = 0{,}4$, puis cherche le couple $(i, j)$ tel que `givens_rotation(3, i, j, 0.4)` lui est égale (une liste de 2 entiers) ;
- c) la norme de Frobenius de $\mathbf{G}\mathbf{H} - \mathbf{H}\mathbf{G}$ pour `G = givens_rotation(5, 0, 2, 0.9)` et `H = givens_rotation(5, 2, 4, -0.6)`, puis pour le même `G` et `givens_rotation(5, 1, 3, -0.6)` (une liste de 2 nombres).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `givens_rotation` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_givens_rotation_ or test_module_uses_") + [
        ("md", "**L'usage** : les vecteurs de MB3.2, une matrice de MML, et deux commutateurs."),
        ("todo", '''answer_MB3_14a = answer_MB3_14b = answer_MB3_14c = ...
with wbm.attempt("MB3.14"):          # if you call givens_rotation here: ⏳ while it is not written
    answer_MB3_14a = ...  # a) a list of 6 numbers, as computed: the vector of MB3.2 a), then the vector of MB3.2 b)
    answer_MB3_14b = ...  # b) a list of 2 integers: (i, j) such that givens_rotation(3, i, j, 0.4) equals (3.78) of MML
    answer_MB3_14c = ...  # c) a list of 2 numbers, as computed: the Frobenius norm of GH - HG for the two H'''),
        ("check", answers_check("MB3.14", "abc")),
        ("solution", '''givens_rotation = mymath.positional.givens_rotation
R23_14, R12_14 = givens_rotation(3, 1, 2, np.pi / 2), givens_rotation(3, 0, 1, np.pi / 3)
answer_MB3_14a = np.concatenate([R23_14 @ R12_14 @ E2, R12_14 @ R23_14 @ E2]).tolist()
t_14 = 0.4
R2_mml_14 = np.array([[math.cos(t_14), 0, math.sin(t_14)], [0, 1, 0], [-math.sin(t_14), 0, math.cos(t_14)]])   # (3.78)
answer_MB3_14b = next([i, j] for i in range(3) for j in range(3)
                      if i != j and np.allclose(givens_rotation(3, i, j, t_14), R2_mml_14))
G_14 = givens_rotation(5, 0, 2, 0.9)
answer_MB3_14c = [float(np.linalg.norm(G_14 @ H - H @ G_14))
                  for H in (givens_rotation(5, 2, 4, -0.6), givens_rotation(5, 1, 3, -0.6))]
print("a)", np.round(answer_MB3_14a, 6).tolist(), " b)", answer_MB3_14b, " c)", np.round(answer_MB3_14c, 6).tolist())'''),
        ("record", '''def givens_14r(n, i, j, t):
    """The oracle, MML (3.80)-(3.81) with indices from 0: e_i turned towards e_j."""
    G = np.eye(n)
    G[i, i] = G[j, j] = math.cos(t)
    G[j, i], G[i, j] = math.sin(t), -math.sin(t)
    return G


e2_14r = np.array([0.0, 1.0, 0.0])


def vectors_14r(sign):
    A, B = givens_14r(3, 1, 2, sign * math.pi / 2), givens_14r(3, 0, 1, sign * math.pi / 3)
    return np.round(np.concatenate([A @ B @ e2_14r, B @ A @ e2_14r]), 12).tolist()


a_14r = vectors_14r(1)
wbm.record("MB3.14a", a_14r, decimals=6,
           mistakes={"dans R₂₃(π/2) R₁₂(π/3) e₂, c'est la matrice de droite qui agit la première : a), puis b), dans cet "
                     "ordre": a_14r[3:] + a_14r[:3],
                     "givens_rotation(n, i, j, θ) tourne e_i vers e_j : R₂₃ est givens_rotation(3, 1, 2, …), avec i et j "
                     "dans cet ordre": vectors_14r(-1)})
wbm.record("MB3.14b", [2, 0],
           mistakes={"(3.78) a +sin θ en haut à droite : compare avec G[i, j] = −sin θ de la docstring": [0, 2],
                     "les indices du code partent de 0 : la coordonnée k de MML est l'indice k − 1": [3, 1],
                     "les indices du code partent de 0, et (3.78) a +sin θ en haut à droite : compare avec G[i, j] = −sin θ":
                         [1, 3]})
G_14r = givens_14r(5, 0, 2, 0.9)
commutators_14r = [G_14r @ H - H @ G_14r for H in (givens_14r(5, 2, 4, -0.6), givens_14r(5, 1, 3, -0.6))]
c_14r = [float(np.sqrt(np.sum(C ** 2))) for C in commutators_14r]
wbm.record("MB3.14c", c_14r, decimals=6,
           mistakes={"la liste suit l'ordre de l'énoncé : H = givens_rotation(5, 2, 4, -0.6) d'abord": c_14r[::-1],
                     "la norme de Frobenius est la racine de la somme des carrés des coefficients (np.linalg.norm(M), "
                     "sans ord=2)": [float(np.linalg.norm(C, 2)) for C in commutators_14r],
                     "c'est la norme, pas son carré": [float(np.sum(C ** 2)) for C in commutators_14r]})'''),
        ("solution", answers_check("MB3.14", "abc")),
        look(LOOK_14),
    ],
)

# ---------------------------------------------------------------------------
# MB3.15 · online_softmax
# ---------------------------------------------------------------------------
CHECK_15C = '''with checked("MB3.15"):                  # c): the log-sum-exp, then the direct calculation, which gives -inf
    if not filled(answer_MB3_15c):
        print("⏳ Ex MB3.15c : pas encore fait.")
    elif as_floats(answer_MB3_15c) is None or as_floats(answer_MB3_15c).shape != (2,):
        print(f"❌ Ex MB3.15c : attendu une liste de 2 nombres (m + ln l, puis ce que rend le calcul direct), reçu "
              f"{shown(answer_MB3_15c)}")
    elif not np.isneginf(as_floats(answer_MB3_15c)[1]):
        print("❌ Ex MB3.15c : le second nombre est ce que rend vraiment np.log(np.sum(np.exp(s))) en float64 : "
              "exécute-le et recopie son résultat (-np.inf s'il le faut), sans le corriger")
    else:
        check_answer("MB3.15c", float(as_floats(answer_MB3_15c)[0]))'''

NOTE_15 = (r"`s = np.asarray(scores, dtype=float)` après les contrôles ; `m, l = -math.inf, 0.0` et un accumulateur nul ; "
           r"pour chaque bloc, `mb = s_b.max()`, et si `mb > -inf` : `m_new = max(m, mb)`, `f = math.exp(m - m_new)` "
           r"(0 au premier bloc), `w = np.exp(s_b - m_new)`, `l = l * f + w.sum()`, `acc = acc * f + w @ v_b` ; une "
           r"copie de l'état par bloc avec `history`. a) $(3 ;\ 1{,}375 ;\ 11{,}75 ;\ 4 ;\ 1{,}96875 ;\ 8{,}875 ;\ 4 ;\ "
           r"3{,}28125 ;\ 16{,}1875)$ et vrai ; la moyenne vaut $\frac{74}{15}$. b) Vrai. c) $m + \ln l \approx "
           r"-1\,200{,}702880$, et `-inf` pour le calcul direct. d) $\approx (0{,}738354 ;\ -0{,}091732)$, de direction "
           r"$\approx 352{,}92°$.")

MB3_15 = Ex(
    "MB3.15", "🔨", 2, 35, "La softmax en ligne : l'état (m, l, a) de scores et de valeurs lus par blocs, et l'état après "
    "chaque bloc · `online_softmax`",
    "programmer la softmax en ligne avec son état après chaque bloc, puis retrouver MB3.7, l'indépendance de la taille "
    "des blocs, un log-sum-exp qui déborderait, et une direction moyenne pondérée.",
    "fiche §8 ; M05a ; Ex MB3.3 et MB3.7", tracks="C, E", mymath="positional.py", note=NOTE_15,
    body=REMINDER + r"""

Écris `online_softmax(scores, values=None, block_size=1, history=False)` (fiche §8), en suivant sa docstring : contrôle les scores (un tableau 1-D non vide de réels, $-\infty$ permis, ni `nan` ni $+\infty$), les valeurs ($n$ lignes, 1-D ou 2-D, finies), `block_size` (un entier $\ge 1$, pas un booléen) et `history` (un booléen) ; pars de l'état vide ; pour chaque bloc, saute-le si tous ses scores valent $-\infty$, sinon calcule le nouveau maximum, le facteur $e^{m - m'}$ et les poids $e^{s_j - m'}$ du bloc, puis mets $l$ et l'accumulateur à jour ; avec `history=True`, garde une copie de l'état après chaque bloc. Rends des `float` Python (et un `float` pour `acc` quand les valeurs sont 1-D).

**L'usage.** La cellule de données de la partie A donne les balises de MB3.7 (`S_7`, les scores $k_j\ln 2$, et `V_7`, leurs valeurs). Avec ta fonction :
- a) les neuf balises, par blocs de 3 avec `history=True` : les trois états, avec $m$ divisé par $\ln 2$, puis vrai ou faux, ils sont égaux à tes réponses a) à c) de MB3.7 à $10^{-12}$ près (une liste de 10 : les 9 nombres, état par état, puis le booléen) ;
- b) vrai ou faux : l'état final est le même, à $10^{-12}$ près, pour des blocs de 1, 2, 3, 4 et 9 ;
- c) pour les scores $(-1\,203{,}5 ;\ -1\,201 ;\ -1\,204{,}2 ;\ -1\,202{,}5)$ : $m + \ln l$, puis ce que rend `np.log(np.sum(np.exp(s)))` (une liste de 2) ;
- d) quatre relevés de vent, de directions 300°, 330°, 20° et 70° et de scores de fiabilité $(0{,}8 ;\ 0 ;\ 1{,}2 ;\ -0{,}4)$, encodés par $(\cos, \sin)$ : avec ces encodages comme valeurs 2-D et des blocs de 2, la moyenne pondérée $a/l$, puis sa direction en degrés dans $[0, 360[$ (une liste de 3 nombres).""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `online_softmax` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_online_softmax_") + [
        ("md", "**L'usage** : les balises de MB3.7, la taille des blocs, un log-sum-exp lointain, et des vents."),
        ("todo", '''answer_MB3_15a = answer_MB3_15b = answer_MB3_15c = answer_MB3_15d = ...
with wbm.attempt("MB3.15"):          # if you call online_softmax here: ⏳ while it is not written
    answer_MB3_15a = ...  # a) a list of 10: the three states [m / ln 2, l, acc] one after the other (9 numbers), then True or False
    answer_MB3_15b = ...  # b) True or False: the same final state, to 1e-12, for blocks of 1, 2, 3, 4 and 9
    answer_MB3_15c = ...  # c) a list of 2, as computed: m + ln l, then what np.log(np.sum(np.exp(s))) returns
    answer_MB3_15d = ...  # d) a list of 3, as computed: the weighted mean a / l (2 numbers), then its direction in degrees in [0, 360)'''),
        ("check", answers_check("MB3.15", "ab") + "\n" + CHECK_15C + "\n" + answers_check("MB3.15", "d")),
        ("solution", '''online_softmax = mymath.positional.online_softmax
states_15 = online_softmax(S_7, V_7, block_size=3, history=True)
paper_15 = [(3, 11 / 8, 47 / 4), (4, 63 / 32, 71 / 8), (4, 105 / 32, 259 / 16)]      # my answers a) to c) of MB3.7
flat_15 = [x for m, l, acc in states_15 for x in (m / LN2, l, acc)]
answer_MB3_15a = flat_15 + [all(abs(m / LN2 - p[0]) <= 1e-12 and abs(l - p[1]) <= 1e-12 and abs(acc - p[2]) <= 1e-12
                                for (m, l, acc), p in zip(states_15, paper_15))]
finals_15 = [online_softmax(S_7, V_7, block_size=b) for b in (1, 2, 3, 4, 9)]
answer_MB3_15b = all(math.isclose(m, finals_15[0][0], rel_tol=1e-12) and math.isclose(l, finals_15[0][1], rel_tol=1e-12)
                     and math.isclose(acc, finals_15[0][2], rel_tol=1e-12) for m, l, acc in finals_15)
s_15 = np.array([-1203.5, -1201.0, -1204.2, -1202.5])
m_15, l_15, _ = online_softmax(s_15)
with np.errstate(divide="ignore"):
    direct_15 = float(np.log(np.sum(np.exp(s_15))))
answer_MB3_15c = [m_15 + math.log(l_15), direct_15]
angles_15 = np.radians([300.0, 330.0, 20.0, 70.0])
codes_15 = np.column_stack([np.cos(angles_15), np.sin(angles_15)])
m_15, l_15, acc_15 = online_softmax([0.8, 0.0, 1.2, -0.4], codes_15, block_size=2)
mean_15 = acc_15 / l_15
answer_MB3_15d = mean_15.tolist() + [math.degrees(math.atan2(mean_15[1], mean_15[0])) % 360]
print("a)", np.round(answer_MB3_15a[:9], 6).tolist(), answer_MB3_15a[9], " b)", answer_MB3_15b)
print("c)", answer_MB3_15c, " d)", np.round(answer_MB3_15d, 6).tolist())'''),
        ("record", '''from fractions import Fraction as F_15r
from scipy.special import logsumexp as logsumexp_15r, softmax as softmax_15r


def states_15r(ks, vs, size=3, rescale_acc=True):
    """The oracle: the states [m / ln 2, l, acc] of s = k ln 2 by blocks, exact (powers of 2); rescale_acc=False is the
    classic error (l rescaled, not acc)."""
    m, l, a, out = None, F_15r(0), F_15r(0), []
    for start in range(0, len(ks), size):
        bk, bv = ks[start:start + size], vs[start:start + size]
        new = max(bk) if m is None else max(m, max(bk))
        f = F_15r(0) if m is None else F_15r(2) ** (m - new)
        w = [F_15r(2) ** (k - new) for k in bk]
        l = l * f + sum(w)
        a = (a * f if rescale_acc or m is None else a) + sum(x * v for x, v in zip(w, bv))
        m = new
        out += [m, l, a]
    return [float(x) for x in out]


k_15r, v_15r = [1, 3, 0, 2, -1, 4, 0, 4, 2], [4, 10, 6, 3, 8, 2, 9, 5, 7]
right_15r = states_15r(k_15r, v_15r)
wbm.record("MB3.15a", right_15r + [True], decimals=6,
           mistakes={"m s'écrit divisé par ln 2 : chaque état commence par m / ln 2":
                         [x * math.log(2) if k % 3 == 0 else x for k, x in enumerate(right_15r)] + [True],
                     "quand le maximum change, l ET l'accumulateur se remettent à l'échelle (relance les tests de "
                     "online_softmax)": states_15r(k_15r, v_15r, rescale_acc=False) + [False]})
wbm.record("MB3.15b", True,
           mistakes={"l'état final ne dépend pas de la taille des blocs : compare m, l et acc à 10⁻¹² près (relatif, "
                     "math.isclose), pas avec ==": False})
s_15r = np.array([-1203.5, -1201.0, -1204.2, -1202.5])
lse_15r = float(logsumexp_15r(s_15r))
wbm.record("MB3.15c", lse_15r, decimals=6,
           mistakes={"le log-sum-exp est m + ln l : n'oublie pas m": lse_15r - float(s_15r.max()),
                     "le log-sum-exp est m + ln l, avec le logarithme népérien":
                         float(s_15r.max() + math.log10(math.exp(lse_15r - s_15r.max())))})
a_15r = np.radians([300.0, 330.0, 20.0, 70.0])
codes_15r = np.column_stack([np.cos(a_15r), np.sin(a_15r)])
mean_15r = softmax_15r([0.8, 0.0, 1.2, -0.4]) @ codes_15r
direction_15r = math.degrees(math.atan2(mean_15r[1], mean_15r[0]))
wbm.record("MB3.15d", mean_15r.tolist() + [direction_15r % 360], decimals=6,
           mistakes={"les encodages se pondèrent par la softmax des scores de fiabilité, pas tous également":
                         codes_15r.mean(axis=0).tolist()
                         + [math.degrees(math.atan2(*codes_15r.mean(axis=0)[::-1])) % 360],
                     "la direction est dans [0, 360[ : ajoute 360 à un angle négatif": mean_15r.tolist() + [direction_15r],
                     "la direction se donne en degrés": mean_15r.tolist() + [math.radians(direction_15r % 360)],
                     "la direction est celle du vecteur a/l, pas la moyenne des angles":
                         mean_15r.tolist() + [float(np.mean([300.0, 330.0, 20.0, 70.0]))]})'''),
        ("solution", answers_check("MB3.15", "ab") + "\n" + CHECK_15C + "\n" + answers_check("MB3.15", "d")),
        look(LOOK_15),
    ],
)

# ---------------------------------------------------------------------------
# MB3.16 · merge_softmax_states
# ---------------------------------------------------------------------------
GIVEN_16 = '''S_16 = np.array(__S_16__)   # twelve scores
V_16 = np.array(__V_16__)   # their values, of length 2
CUTS_16 = [0, 2, 7, 8, 12]   # the four pieces A, B, C, D: scores 0-1, 2-6, 7, 8-11
for _array in (S_16, V_16):
    _array.setflags(write=False)'''

NOTE_16 = (r"Les contrôles des deux états ; deux états vides rendent l'état vide ; sinon `m = max(m1, m2)`, "
           r"`f1 = math.exp(m1 - m)` (0 si `m1 = -inf`), de même `f2`, puis `(m, l1 * f1 + l2 * f2, acc1 * f1 + acc2 * f2)`, "
           r"dans un nouveau tableau. a) $(4 ;\ 3{,}28125 ;\ 16{,}1875)$, comme MB3.7 f), et vrai. b) Vrai pour les trois "
           r"groupements ; la moyenne vaut $\approx (0{,}998801 ;\ 0{,}192926)$. c) Vrai.")

MB3_16 = Ex(
    "MB3.16", "🔨", 2, 25, "La fusion de deux états de la softmax en ligne · `merge_softmax_states`",
    "programmer la fusion de deux états, puis vérifier qu'elle redonne l'état de la réunion dans n'importe quel ordre et "
    "groupement, et que l'état vide est neutre.",
    "fiche §8 ; Ex MB3.7 et MB3.15", tracks="C, E", mymath="positional.py", note=NOTE_16, given=GIVEN_16,
    body=REMINDER + r"""

Écris `merge_softmax_states(state1, state2)` (fiche §8), en suivant sa docstring : contrôle les deux états (des triplets ; $m$ réel ou $-\infty$ ; $l$ fini, $\ge 1$ quand $m$ est fini ; $l = 0$ et `acc` nul ou `None` quand $m = -\infty$ ; des `acc` de même nature et de même longueur) ; deux états vides donnent l'état vide ; sinon, remets chaque état à l'échelle du maximum commun et additionne. Rends un nouveau tableau, sans modifier les arguments.

**L'usage.** Le notebook fournit `S_16` et `V_16`, douze scores et douze valeurs de longueur 2, et `CUTS_16`, les bornes de quatre morceaux $A$, $B$, $C$, $D$ de 2, 5, 1 et 4 scores. Avec tes fonctions :
- a) les balises de MB3.7 : l'état $A$ du bloc 1, l'état $B$ des blocs 2 et 3, chacun par `online_softmax`, et leur fusion, avec $m$ divisé par $\ln 2$, à comparer à ta réponse f) de MB3.7 ; puis vrai ou faux, cette fusion égale l'état final de MB3.15 a) à $10^{-12}$ près (une liste de 4 : les 3 nombres de la fusion, puis le booléen) ;
- b) les états des quatre morceaux de `S_16` et `V_16` (chacun par `online_softmax`), puis vrai ou faux, les groupements $(A \oplus B) \oplus (C \oplus D)$, $A \oplus (B \oplus (C \oplus D))$ et $(D \oplus C) \oplus (B \oplus A)$ égalent tous `online_softmax(S_16, V_16, block_size=5)` à $10^{-12}$ près, puis la moyenne pondérée $a/l$ (une liste de 3 : le booléen, puis les 2 nombres) ;
- c) vrai ou faux : l'état vide `(-np.inf, 0.0, np.zeros(2))` est neutre pour l'état $A$ de b), des deux côtés.""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `merge_softmax_states` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était "
                  "attendu).")]
    + tests_cells("test_merge_softmax_states_") + [
        ("md", "**L'usage** : la fusion des balises, quatre morceaux groupés de trois façons, et l'état vide."),
        ("todo", '''answer_MB3_16a = answer_MB3_16b = answer_MB3_16c = ...
with wbm.attempt("MB3.16"):          # if you call merge_softmax_states here: ⏳ while it is not written
    answer_MB3_16a = ...  # a) a list of 4: the merged state [m / ln 2, l, acc] (3 numbers), then True or False
    answer_MB3_16b = ...  # b) a list of 3: True or False for the three groupings, then the weighted mean a / l (2 numbers)
    answer_MB3_16c = ...  # c) True or False: the empty state (-np.inf, 0.0, np.zeros(2)) is neutral for A, on both sides'''),
        ("check", answers_check("MB3.16", "abc")),
        ("solution", '''online_softmax, merge = mymath.positional.online_softmax, mymath.positional.merge_softmax_states


def same_16(s1, s2, rtol=1e-12):
    """Two states equal to rtol: m (relative), l (relative) and acc (np.allclose)."""
    return (math.isclose(s1[0], s2[0], rel_tol=rtol) and math.isclose(s1[1], s2[1], rel_tol=rtol)
            and bool(np.allclose(s1[2], s2[2], rtol=rtol, atol=0)))


A_16, B_16 = online_softmax(S_7[:3], V_7[:3]), online_softmax(S_7[3:], V_7[3:])
AB_16 = merge(A_16, B_16)
answer_MB3_16a = [AB_16[0] / LN2, AB_16[1], AB_16[2], same_16(AB_16, online_softmax(S_7, V_7, block_size=3))]
A, B, C, D = (online_softmax(S_16[a:b], V_16[a:b]) for a, b in zip(CUTS_16[:-1], CUTS_16[1:]))
whole_16 = online_softmax(S_16, V_16, block_size=5)
groupings_16 = [merge(merge(A, B), merge(C, D)), merge(A, merge(B, merge(C, D))), merge(merge(D, C), merge(B, A))]
answer_MB3_16b = [all(same_16(g, whole_16) for g in groupings_16)] + (whole_16[2] / whole_16[1]).tolist()
empty_16 = (-np.inf, 0.0, np.zeros(2))
answer_MB3_16c = same_16(merge(empty_16, A), A) and same_16(merge(A, empty_16), A)
print("a)", answer_MB3_16a, " b)", answer_MB3_16b, " c)", answer_MB3_16c)'''),
        ("record", '''from scipy.special import softmax as softmax_16r

wbm.record("MB3.16a", [4.0, 105 / 32, 259 / 16, True], decimals=6,
           mistakes={"chaque état se remet à l'échelle du maximum commun avant d'additionner (relance les tests de "
                     "merge_softmax_states)": [4.0, 11 / 8 + 83 / 32, 47 / 4 + 165 / 16, False],
                     "la fusion additionne les l et les acc, elle ne les moyenne pas (relance les tests)":
                         [4.0, 105 / 64, 259 / 32, False],
                     "m s'écrit divisé par ln 2 : la liste commence par m / ln 2": [4 * math.log(2), 105 / 32, 259 / 16, True]})
S_16r, V_16r = np.array(__S_16__), np.array(__V_16__)
mean_16r = (softmax_16r(S_16r) @ V_16r).tolist()
wbm.record("MB3.16b", [True] + mean_16r, decimals=6,
           mistakes={"la moyenne pondérée est acc / l, pas acc":
                         [True] + (np.exp(S_16r - S_16r.max()) @ V_16r).tolist(),
                     "la moyenne est pondérée par la softmax des scores, pas la moyenne simple des valeurs":
                         [True] + V_16r.mean(axis=0).tolist(),
                     "la fusion est associative et commutative : compare les états à 10⁻¹² près (m, l et acc), pas avec ==":
                         [False] + mean_16r})
wbm.record("MB3.16c", True,
           mistakes={"l'état vide est neutre des deux côtés : compare les états à 10⁻¹² près (relance les tests de "
                     "merge_softmax_states)": False})'''),
        ("solution", answers_check("MB3.16", "abc")),
        look(LOOK_16),
    ],
)

PART_A = Part("A", "Ta librairie : la rotation de Givens, la softmax en ligne et la fusion de deux états",
              "Fiche §3 et §8. Les trois fonctions de `mymath/positional.py`, leurs tests, et un usage de chacune sur les "
              "données des exercices papier. La cellule de données ci-dessous recopie les données des exercices papier.",
              given=TOOLS + "\n\n\n" + DATA, exercises=[MB3_14, MB3_15, MB3_16])

# ---------------------------------------------------------------------------
# Notebook exercises: predict, measure, draw (MB3.17, MB3.18, MB3.19)
# ---------------------------------------------------------------------------
GIVEN_17 = '''X_17 = np.array(__X_17__)   # the altitudes of 24 stations (km)
Y_17 = np.array(__Y_17__)   # their temperatures at noon (°C)
GRID_17 = np.linspace(1.0, 2.6, 321)   # the grid of the curves (321 altitudes, km)
H_17 = (0.025, 0.25, 2.5)              # h / 10, the reference width h, and 10 h (km)
X0_17 = 1.85                           # the altitude of d) and e) (km)
for _array in (X_17, Y_17, GRID_17):
    _array.setflags(write=False)'''

CHECK_17 = '''HIDDEN_C17 = __HIDDEN_C17__   # hidden stations, altitudes, widths, and the sub-ID of the predictions expected

with checked("MB3.17"):
    results_17 = []
    report_17 = reporter(results_17, stop=False)
    X_c17, Y_c17, x_c17 = (np.array(HIDDEN_C17[key]) for key in ("X", "Y", "x"))
    got_c17 = [as_floats(call_safely("Ex MB3.17 : nw_predict_17 (appel caché)", nw_predict_17, x_c17.copy(), X_c17.copy(),
                                     Y_c17.copy(), h)) for h in HIDDEN_C17["hs"]]
    if any(g is None or g.shape != x_c17.shape for g in got_c17):
        report_17(False, "", "nw_predict_17 rend une prévision par altitude de x : un tableau de forme (len(x),)")
    elif any(np.isnan(g).any() for g in got_c17):
        report_17(False, "", "nw_predict_17 rend nan sur un appel caché : avec une très petite largeur, toutes les "
                             "exponentielles valent 0 en float64 ; retranche le plus grand score de chaque altitude avant "
                             "l'exponentielle (une softmax stable)")
    else:
        report_17(passes(HIDDEN_C17["id"], [g.tolist() for g in got_c17]),
                  "nw_predict_17 : un appel caché (d'autres stations, d'autres largeurs, dont une très petite) est juste",
                  "nw_predict_17 sur un appel caché : ce n'est pas la prévision de Nadaraya-Watson à noyau gaussien "
                  "exp(−(x − xᵢ)²/(2h²)), une softmax des scores sur les stations, pour chaque altitude de x")

    def curves_why_c17(ax, X, Y, hs, curves):
        """What is wrong in a call of draw_bandwidths_17 (French phrases)."""
        if not isinstance(curves, (list, tuple)) or len(curves) != len(hs):
            return [f"draw_bandwidths_17 doit rendre la liste des {len(hs)} courbes tracées, reçu {shown(curves)}"]
        curves = [as_floats(c) for c in curves]
        if any(c is None or c.shape != GRID_17.shape for c in curves):
            return ["chaque courbe rendue est un tableau des prévisions sur GRID_17, de forme (321,)"]
        problems = []
        if not all(matches(c, nw_predict_17(GRID_17, X, Y, h), rtol=1e-9, atol=1e-9) for c, h in zip(curves, hs)):
            problems.append("les courbes rendues sont les prévisions nw_predict_17(GRID_17, X, Y, h), une par h, "
                            "dans l'ordre de hs")
        if not all(line_with(ax, GRID_17, c) for c in curves):
            problems.append("chaque courbe tracée en fonction de GRID_17 (ax.plot(GRID_17, courbe))")
        if not points_at(ax, X, Y):
            problems.append("les stations, un point par station (ax.scatter, ou ax.plot avec un marqueur et "
                            'linestyle="none")')
        if ax.get_legend() is None or len(ax.get_legend().get_texts()) < len(hs):
            problems.append("une légende qui nomme chaque largeur (label=…, puis ax.legend())")
        if not ax.get_xlabel() or not ax.get_ylabel():
            problems.append("des noms d'axes")
        return problems

    fig_17, ax_17 = plt.subplots(figsize=(8, 4.5))
    try:
        result_17 = []
        opened_17 = drawn(lambda: result_17.append(call_safely("Ex MB3.17 : draw_bandwidths_17", draw_bandwidths_17,
                                                               ax_17, X_17, Y_17, H_17)))
        problems_17 = curves_why_c17(ax_17, X_17, Y_17, H_17, result_17[0])
        report_17(not problems_17, "draw_bandwidths_17 (h = 0,025 ; 0,25 ; 2,5) : les courbes, les stations, la légende et "
                  "les noms d'axes", "draw_bandwidths_17 : il manque " + " ; ".join(problems_17))
        fig_c17, axes_c17 = plt.subplots(1, 2)        # the 2nd axes is the current one: plt.plot would draw there
        try:
            hidden_c17 = []
            opened_17 += drawn(lambda: hidden_c17.append(call_safely("Ex MB3.17 : draw_bandwidths_17 (appel caché)",
                                                                     draw_bandwidths_17, axes_c17[0], X_c17, Y_c17,
                                                                     tuple(HIDDEN_C17["draw_hs"]))))
            problems_c17 = curves_why_c17(axes_c17[0], X_c17, Y_c17, HIDDEN_C17["draw_hs"], hidden_c17[0])
            elsewhere_17 = bool(axes_c17[1].lines or axes_c17[1].collections or axes_c17[1].get_legend())
        finally:
            plt.close(fig_c17)
        report_17(not problems_c17, "un appel caché de draw_bandwidths_17 (d'autres stations, deux largeurs) est juste aussi",
                  "un appel caché de draw_bandwidths_17 (d'autres stations, deux largeurs) : il manque "
                  + " ; ".join(problems_c17))
        report_17(not opened_17 and not elsewhere_17, "draw_bandwidths_17 dessine dans les axes reçus",
                  "draw_bandwidths_17 doit dessiner dans les axes reçus (ax.plot, ax.legend…), sans ouvrir de figure ni "
                  "dessiner dans l'axe courant (plt.plot, plt.legend…)")
    except BaseException:
        plt.close(fig_17)
        raise
    fig_17.tight_layout()
    plt.show()
    verdict("MB3.17", all(results_17) and len(results_17) == 4, "tes deux fonctions sont justes, sur les stations du "
            "notebook et sur des appels cachés.", "relis les lignes ❌ ci-dessus.")'''

NOTE_17 = (r"Prédictions attendues : a) (A) ; b) (B) ; c) (A). `nw_predict_17` : les scores "
           r"`-(x[:, None] - X[None, :]) ** 2 / (2 * h ** 2)`, moins leur maximum par ligne, puis `np.exp`, la "
           r"normalisation par ligne et le produit par `Y`. d) $(0{,}9653 ;\ 0{,}1099 ;\ 0{,}0424)$ ; e) $(5{,}343 ;\ "
           r"4{,}186 ;\ 4{,}427)$ °C ; f) $(0{,}033 ;\ 1{,}220 ;\ 10{,}146)$ ; g) $(11{,}887 ;\ 8{,}095 ;\ 0{,}380)$ °C.")

MB3_17 = Ex(
    "MB3.17", "🔮", 1, 20, "Prédire ce que deviennent les poids et la prévision de Nadaraya-Watson quand la largeur de bande "
    "est divisée ou multipliée par 10, puis tracer",
    "prévoir l'effet de la largeur de bande sur les poids et sur la courbe de Nadaraya-Watson, puis le mesurer et le "
    "tracer.", "fiche §5 et §7 ; M05a, M28 ; Ex MB3.4", tracks="C, E", hypothesis=True, given=GIVEN_17, note=NOTE_17,
    body=r"""Le notebook fournit `X_17` et `Y_17`, les altitudes (en km, de 1,0 à 2,6) et les températures de midi de 24 stations d'un massif. On prévoit la température en une altitude $x$ par Nadaraya-Watson à noyau gaussien, avec une largeur de bande de référence $h = 0{,}25$ km, puis $h/10 = 0{,}025$ km et $10h = 2{,}5$ km (`H_17`). **Avant d'exécuter quoi que ce soit**, prédis :
- a) quand $h$ est divisé par 10, le plus grand poids à 1,85 km : (A) proche de 1 ; (B) proche de $\frac{1}{24}$ ; (C) à peu près le même qu'avec $h$ (une lettre) ;
- b) quand $h$ est multiplié par 10, la courbe des prévisions de 1,0 à 2,6 km : (A) elle passe près de chaque station, en dents de scie ; (B) elle est presque plate, près de la moyenne des températures ; (C) c'est la droite qui suit la baisse de la température avec l'altitude (une lettre) ;
- c) quand $h$ est divisé par 10, l'erreur quadratique moyenne de la prévision aux altitudes des stations elles-mêmes : (A) proche de 0 ; (B) proche de celle obtenue avec $h$ ; (C) plus grande qu'avec $h$ (une lettre).

Puis, une fois tes prédictions écrites et vérifiées, écris `nw_predict_17(x, X, Y, h)`, qui rend la prévision en chaque altitude du tableau `x` (un tableau de forme `(len(x),)`), par une softmax stable, et `draw_bandwidths_17(ax, X, Y, hs)`, qui trace les stations (un point chacune) et, pour chaque largeur de `hs`, la courbe des prévisions sur la grille `GRID_17` (321 altitudes de 1,0 à 2,6 km), dans les axes reçus, avec une légende et des noms d'axes, et rend la liste des courbes tracées (un tableau de 321 prévisions par largeur). Relève, pour $h = 0{,}025$ ; $0{,}25$ ; $2{,}5$ km (chaque fois une liste de 3 nombres ; 3 ou 4 décimales dans ta copie) :
- d) le plus grand poids à 1,85 km ;
- e) la prévision à 1,85 km ;
- f) l'erreur quadratique moyenne aux stations (la prévision aux altitudes `X_17`, comparée à `Y_17`) ;
- g) l'amplitude (le maximum moins le minimum) de la courbe sur la grille `GRID_17`.

La vérification de l'expérience ne s'exécute qu'une fois tes trois prédictions écrites ; elle essaie aussi tes fonctions sur d'autres stations et d'autres largeurs, dont une très petite.""",
    todo='''prediction_MB3_17a = ...  # a) "A", "B" or "C": with h / 10, the largest weight at 1.85 km
prediction_MB3_17b = ...  # b) "A", "B" or "C": with 10 h, the curve of the predictions
prediction_MB3_17c = ...  # c) "A", "B" or "C": with h / 10, the mean squared error at the stations''',
    check='''for letter, prediction in zip("abc", [prediction_MB3_17a, prediction_MB3_17b, prediction_MB3_17c]):
    wbm.check(f"MB3.17{letter}", prediction)''',
    record='''from scipy.special import softmax as softmax_17r

X_17r, Y_17r = np.array(__X_17__), np.array(__Y_17__)
GRID_17r, H_17r = np.linspace(1.0, 2.6, 321), (0.025, 0.25, 2.5)


def weights_17r(x, X, h, two=2.0):
    """The oracle: the weights of the Gaussian kernel, one row per altitude of x (scipy.special.softmax)."""
    return softmax_17r(-(np.atleast_1d(np.asarray(x, dtype=float))[:, None] - np.asarray(X)[None, :]) ** 2
                       / (two * h ** 2), axis=1)


def measures_17r(two=2.0):
    """d) to g) for the three widths (two = 1: the classic error h² instead of 2h²)."""
    out = {"d": [], "e": [], "f": [], "g": [], "rmse": [], "stations": []}
    for h in H_17r:
        out["d"].append(float(weights_17r(1.85, X_17r, h, two).max()))
        out["e"].append(float((weights_17r(1.85, X_17r, h, two) @ Y_17r)[0]))
        at_stations = weights_17r(X_17r, X_17r, h, two) @ Y_17r
        out["f"].append(float(np.mean((at_stations - Y_17r) ** 2)))
        out["rmse"].append(float(np.sqrt(np.mean((at_stations - Y_17r) ** 2))))
        out["g"].append(float(np.ptp(weights_17r(GRID_17r, X_17r, h, two) @ Y_17r)))
        out["stations"].append(float(np.ptp(at_stations)))
    return out


right_17r, h2_17r = measures_17r(), measures_17r(two=1.0)
wbm.record("MB3.17a", "A" if right_17r["d"][0] > 0.9 else "B" if abs(right_17r["d"][0] - 1 / 24) < 0.01 else "C",
           prediction=True,
           mistakes={"diviser h par 10 multiplie l'échelle 1/(2h²) des scores par 100 : l'écart entre les scores de deux "
                     "stations devient énorme": "B",
                     "les scores −(x − xᵢ)²/(2h²) dépendent de h : diviser h par 10 change leurs écarts, donc les poids": "C"})
wbm.record("MB3.17b", "B" if right_17r["g"][2] < 0.1 * np.ptp(Y_17r) else "A", prediction=True,
           mistakes={"multiplier h par 10 divise l'échelle des scores par 100 : regarde ce que deviennent des scores "
                     "presque égaux": "A",
                     "une moyenne pondérée n'est pas une régression : avec des poids presque égaux, que vaut-elle en "
                     "chaque altitude ?": "C"})
wbm.record("MB3.17c", "A" if right_17r["f"][0] < 0.1 * right_17r["f"][1] else "B", prediction=True,
           mistakes={"à l'altitude d'une station, une très petite largeur donne presque tout le poids à cette station "
                     "elle-même": "B",
                     "la prévision en une station se rapproche de sa propre température quand h diminue": "C"})''',
    after=[
        ("md", "**L'expérience.** Écris-la une fois tes trois prédictions vérifiées ; sa vérification ne s'exécute qu'à cette "
               "condition."),
        ("todo", '''def nw_predict_17(x, X, Y, h):
    """The Nadaraya-Watson prediction at each altitude of the array x (shape (len(x),)), from the stations X (altitudes)
    and Y (temperatures), with the Gaussian kernel of width h, by a stable softmax."""
    raise NotImplementedError("nw_predict_17 n'est pas encore écrite (04_indices.md si tu bloques)")


def draw_bandwidths_17(ax, X, Y, hs):
    """In the axes ax: the stations (X, Y) as points and, for each width of hs, the curve of the predictions on
    GRID_17, with a legend and axis labels. Returns the list of the curves drawn (one array of 321 predictions per
    width). Opens no figure."""
    raise NotImplementedError("draw_bandwidths_17 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB3_17d = answer_MB3_17e = answer_MB3_17f = answer_MB3_17g = ...
with wbm.attempt("MB3.17"):          # your functions: ⏳ while they are not written
    answer_MB3_17d = ...  # d) a list of 3 numbers, as computed: the largest weight at 1.85 km, for each width of H_17
    answer_MB3_17e = ...  # e) a list of 3 numbers, as computed: the prediction at 1.85 km
    answer_MB3_17f = ...  # f) a list of 3 numbers, as computed: the mean squared error at the stations
    answer_MB3_17g = ...  # g) a list of 3 numbers, as computed: the range (max - min) of the curve on GRID_17'''),
        ("check", guarded(answers_check("MB3.17", "defg") + "\n\n" + CHECK_17,
                          [f"prediction_MB3_17{letter}" for letter in "abc"],
                          "⏳ Écris d'abord tes trois prédictions, puis exécute à nouveau.")),
        ("solution", '''def nw_weights_17(x, X, h):
    """The weights of the Gaussian kernel, one row per altitude of x: a softmax of the scores, stable."""
    scores = -(np.asarray(x, dtype=float)[:, None] - np.asarray(X, dtype=float)[None, :]) ** 2 / (2 * h ** 2)
    weights = np.exp(scores - scores.max(axis=1, keepdims=True))
    return weights / weights.sum(axis=1, keepdims=True)


def nw_predict_17(x, X, Y, h):
    """The Nadaraya-Watson prediction at each altitude of the array x (shape (len(x),)), from the stations X (altitudes)
    and Y (temperatures), with the Gaussian kernel of width h, by a stable softmax."""
    return nw_weights_17(np.atleast_1d(x), X, h) @ np.asarray(Y, dtype=float)


def draw_bandwidths_17(ax, X, Y, hs):
    """In the axes ax: the stations (X, Y) as points and, for each width of hs, the curve of the predictions on
    GRID_17, with a legend and axis labels. Returns the list of the curves drawn (one array of 321 predictions per
    width). Opens no figure."""
    ax.scatter(X, Y, s=16, color="k", zorder=3, label="stations")
    curves = []
    for h in hs:
        curve = nw_predict_17(GRID_17, X, Y, h)
        ax.plot(GRID_17, curve, lw=1.6, label=f"h = {h:g} km".replace(".", ","))
        curves.append(curve)
    ax.set_xlabel("altitude (km)")
    ax.set_ylabel("température de midi (°C)")
    ax.legend()
    return curves


answer_MB3_17d = [float(nw_weights_17([X0_17], X_17, h).max()) for h in H_17]
answer_MB3_17e = [float(nw_predict_17([X0_17], X_17, Y_17, h)[0]) for h in H_17]
answer_MB3_17f = [float(np.mean((nw_predict_17(X_17, X_17, Y_17, h) - Y_17) ** 2)) for h in H_17]
answer_MB3_17g = [float(np.ptp(nw_predict_17(GRID_17, X_17, Y_17, h))) for h in H_17]
for letter, values in zip("defg", (answer_MB3_17d, answer_MB3_17e, answer_MB3_17f, answer_MB3_17g)):
    print(f"{letter})", np.round(values, 4).tolist())
print("   moyenne des températures :", round(float(Y_17.mean()), 3), " ; 1/24 =", round(1 / 24, 4))'''),
        ("record", '''wbm.record("MB3.17d", right_17r["d"], decimals=6,
           mistakes={"le noyau gaussien divise par 2h², pas par h²": h2_17r["d"],
                     "la liste suit l'ordre de H_17 : h = 0,025 ; 0,25 ; 2,5": right_17r["d"][::-1]})
wbm.record("MB3.17e", right_17r["e"], decimals=6,
           mistakes={"le noyau gaussien divise par 2h², pas par h²": h2_17r["e"],
                     "la liste suit l'ordre de H_17 : h = 0,025 ; 0,25 ; 2,5": right_17r["e"][::-1]})
wbm.record("MB3.17f", right_17r["f"], decimals=6,
           mistakes={"l'erreur quadratique moyenne est la moyenne des carrés des écarts, sans racine": right_17r["rmse"],
                     "le noyau gaussien divise par 2h², pas par h²": h2_17r["f"]})
wbm.record("MB3.17g", right_17r["g"], decimals=6,
           mistakes={"l'amplitude se mesure sur la courbe de la grille GRID_17, pas aux seules stations":
                         right_17r["stations"],
                     "le noyau gaussien divise par 2h², pas par h²": h2_17r["g"]})
HIDDEN_17r = __HIDDEN_C17__                                                  # the hidden call of the check
wbm.record(HIDDEN_17r["id"], [(weights_17r(HIDDEN_17r["x"], HIDDEN_17r["X"], h) @ np.array(HIDDEN_17r["Y"])).tolist()
                              for h in HIDDEN_17r["hs"]], decimals=6)'''),
        ("solution", answers_check("MB3.17", "defg") + "\n\n" + CHECK_17),
        look("à quoi ressemblent les trois courbes, et laquelle choisirais-tu ? Que dit d) sur la température du modèle ?",
             " (après l'expérience)"),
    ],
)

# ---------------------------------------------------------------------------
# MB3.18 · rescalings according to the order and the size of the blocks
# ---------------------------------------------------------------------------
GIVEN_18 = '''rng_18 = np.random.default_rng(7318)
S_18 = rng_18.normal(0, 1, 600)                                         # 600 scores
V_18 = rng_18.normal(0, 1, (600, 3))                                    # their values, of length 3
ORDERS_18 = np.array([rng_18.permutation(600) for _ in range(300)])     # the 300 random orders of c), drawn once here
BLOCKS_18 = (1, 6, 60)                                                  # B: N = 600, 100 and 10 blocks
for _array in (S_18, V_18, ORDERS_18):
    _array.setflags(write=False)'''

CHECK_18 = '''HIDDEN_C18 = __HIDDEN_C18__   # hidden scores and block sizes, and the sub-IDs of their numbers of rescalings

with checked("MB3.18"):
    results_18 = []
    report_18 = reporter(results_18, stop=False)
    for k_c18, (scores_c18, size_c18, id_c18) in enumerate(HIDDEN_C18, start=1):
        states_c18 = ref_pos.online_softmax(np.array(scores_c18), block_size=size_c18, history=True)
        got_c18 = call_safely(f"Ex MB3.18 : count_rescalings_18 (cas caché {k_c18})", count_rescalings_18, states_c18)
        report_18(passes(id_c18, got_c18), f"count_rescalings_18 : cas caché {k_c18} (des blocs masqués, un maximum "
                  "atteint deux fois), comme attendu",
                  f"count_rescalings_18, cas caché {k_c18} (des blocs masqués, un maximum atteint deux fois) : rendu "
                  f"{shown(got_c18)} ; une remise à l'échelle a lieu quand m change d'un état au suivant, après le premier "
                  "bloc qui a un score fini (rien n'était accumulé avant)")
    Ns_c18, means_c18, harmonic_c18 = [700, 70, 7], [5.2, 3.4, 1.6], [5.6, 3.8, 1.5]     # a test of the drawing only
    fig_c18, axes_c18 = plt.subplots(1, 2)            # the 2nd axes is the current one: plt.plot would draw there
    try:
        opened_c18 = drawn(lambda: call_safely("Ex MB3.18 : draw_rescalings_18", draw_rescalings_18, axes_c18[0],
                                               Ns_c18, means_c18, harmonic_c18))
        ax_c18 = axes_c18[0]
        missing_c18 = []
        for values_c18, what_c18 in ((means_c18, "les moyennes"), (harmonic_c18, "H_N − 1")):
            if not (points_at(ax_c18, Ns_c18, values_c18) or line_with(ax_c18, Ns_c18, values_c18)):
                missing_c18.append(f"{what_c18} en fonction de N (ax.plot(Ns, …), avec ou sans marqueurs)")
        if ax_c18.get_xscale() != "log":
            missing_c18.append('l\\'abscisse logarithmique (ax.set_xscale("log"))')
        if ax_c18.get_legend() is None:
            missing_c18.append("une légende")
        if not ax_c18.get_xlabel() or not ax_c18.get_ylabel():
            missing_c18.append("des noms d'axes")
        elsewhere_c18 = bool(axes_c18[1].lines or axes_c18[1].collections)
    finally:
        plt.close(fig_c18)
    report_18(not missing_c18, "draw_rescalings_18 trace les deux séries, en abscisse logarithmique",
              "draw_rescalings_18 (sur des nombres de test) : il manque " + " ; ".join(missing_c18))
    report_18(not opened_c18 and not elsewhere_c18, "draw_rescalings_18 dessine dans les axes reçus",
              "draw_rescalings_18 doit dessiner dans les axes reçus, sans ouvrir de figure ni dessiner dans l'axe courant")
    if filled(answer_MB3_18c, answer_MB3_18d):                    # your figure, with your answers c) and d)
        fig_18, ax_18 = plt.subplots(figsize=(6, 4))
        call_safely("Ex MB3.18 : draw_rescalings_18", draw_rescalings_18, ax_18, [600 // B for B in BLOCKS_18],
                    answer_MB3_18c, answer_MB3_18d)
        plt.show()
    verdict("MB3.18", all(results_18) and len(results_18) == len(HIDDEN_C18) + 2,
            "count_rescalings_18 et draw_rescalings_18 sont justes sur les cas cachés.", "relis les lignes ❌ ci-dessus.")'''

NOTE_18 = (r"`count_rescalings_18` : `ms = [m for m, _, _ in states]`, puis le nombre de `k` tels que `ms[k - 1] > -inf` et "
           r"`ms[k] != ms[k - 1]`. a) 599, 99 et 9. b) 0, 0 et 0. c) $\approx 5{,}72$, $4{,}01$ et $1{,}85$. d) "
           r"$H_N - 1 \approx 5{,}975$ ; $4{,}187$ ; $1{,}929$. e) 9, 29 et 245 flottants, contre 2 400. f) Vrai.")

MB3_18 = Ex(
    "MB3.18", "🔬", 2, 25, "La softmax en ligne selon l'ordre et la taille des blocs : le nombre de remises à l'échelle "
    "(les états après chaque bloc) pour des scores croissants, décroissants ou mélangés, comparé à H_N − 1, et la mémoire "
    "gardée",
    "compter les remises à l'échelle de la softmax en ligne selon l'ordre des scores et la taille des blocs, comparer à "
    "H_N − 1, et mesurer la mémoire gardée.", "fiche §8 et §9 ; R8, M02b ; Ex MB3.15", tracks="C", given=GIVEN_18,
    note=NOTE_18,
    body=r"""Le notebook fournit `S_18`, 600 scores, `V_18`, leurs valeurs, de forme $(600, 3)$, et `ORDERS_18`, 300 ordres de lecture tirés au hasard une fois pour toutes (300 permutations de `range(600)`, tirées par la graine 7318). Une remise à l'échelle a lieu quand $m$ change d'un état au suivant (après le premier bloc qui a un score fini). Écris `count_rescalings_18(states)`, qui la compte sur une liste d'états rendue par `mymath.positional.online_softmax(..., history=True)`, puis `draw_rescalings_18(ax, Ns, means, harmonic)`, qui trace dans les axes reçus `means` et `harmonic` en fonction de `Ns`, en abscisse logarithmique, avec une légende et des noms d'axes. Pour des blocs de $B = 1$, 6 et 60 scores (`BLOCKS_18`, soit $N = 600$, 100 et 10 blocs), relève (chaque fois une liste de 3, dans l'ordre de `BLOCKS_18`) :
- a) le nombre de remises à l'échelle quand les scores sont lus en ordre croissant (les valeurs permutées avec leurs scores) ;
- b) en ordre décroissant ;
- c) leur moyenne sur les 300 ordres de `ORDERS_18` (les valeurs permutées avec leurs scores, le même ordre pour les trois tailles de blocs) ;
- d) $H_N - 1$ pour chaque $N$, où $H_N = 1 + \frac12 + \cdots + \frac1N$ ;
- e) le nombre de flottants que la lecture garde à la fois : l'état ($2 + 3$ nombres) et un bloc ($B$ scores et $B$ valeurs de longueur 3), à comparer aux $600 \times 4 = 2\,400$ d'une lecture qui garde tout ;
- f) vrai ou faux : les neuf états finaux (croissant, décroissant et l'ordre de `S_18`, pour les trois tailles) sont égaux à $10^{-12}$ près (relatif, $m$, $l$ et l'accumulateur).

La vérification essaie `count_rescalings_18` sur des cas cachés, puis trace c) et d) en fonction de $N$ par ta fonction `draw_rescalings_18`.""",
    todo='''def count_rescalings_18(states):
    """The number of rescalings in a list of states (m, l, acc) returned by online_softmax(..., history=True): the
    number of times m changes from one state to the next, after the first block that holds a finite score."""
    raise NotImplementedError("count_rescalings_18 n'est pas encore écrite (04_indices.md si tu bloques)")


def draw_rescalings_18(ax, Ns, means, harmonic):
    """In the axes ax: means and harmonic as functions of Ns, the abscissa on a logarithmic scale, with a legend and
    axis labels. Opens no figure."""
    raise NotImplementedError("draw_rescalings_18 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB3_18a = answer_MB3_18b = answer_MB3_18c = answer_MB3_18d = answer_MB3_18e = answer_MB3_18f = ...
with wbm.attempt("MB3.18"):          # your functions: ⏳ while they are not written
    answer_MB3_18a = ...  # a) a list of 3 integers: the rescalings for the increasing order, B = 1, 6, 60
    answer_MB3_18b = ...  # b) a list of 3 integers: for the decreasing order
    answer_MB3_18c = ...  # c) a list of 3 numbers, as computed: their mean over the 300 orders of ORDERS_18
    answer_MB3_18d = ...  # d) a list of 3 numbers: H_N - 1 for N = 600, 100, 10
    answer_MB3_18e = ...  # e) a list of 3 integers: the floats held at once (the state and one block)
    answer_MB3_18f = ...  # f) True or False: the nine final states are equal to 1e-12''',
    check=answers_check("MB3.18", "abcdef") + "\n\n" + CHECK_18,
    solution='''def count_rescalings_18(states):
    """The number of rescalings in a list of states (m, l, acc) returned by online_softmax(..., history=True): the
    number of times m changes from one state to the next, after the first block that holds a finite score."""
    ms = [m for m, _, _ in states]
    return sum(1 for before, after in zip(ms[:-1], ms[1:]) if before > -math.inf and after != before)


def draw_rescalings_18(ax, Ns, means, harmonic):
    """In the axes ax: means and harmonic as functions of Ns, the abscissa on a logarithmic scale, with a legend and
    axis labels. Opens no figure."""
    ax.plot(Ns, means, "o-", label="moyenne des remises à l'échelle (300 ordres)")
    ax.plot(Ns, harmonic, "s--", label="$H_N - 1$")
    ax.set_xscale("log")
    ax.set_xlabel("nombre de blocs N")
    ax.set_ylabel("remises à l'échelle")
    ax.legend()


online_softmax = mymath.positional.online_softmax
up_18, down_18 = np.argsort(S_18), np.argsort(S_18)[::-1]
answer_MB3_18a = [count_rescalings_18(online_softmax(S_18[up_18], V_18[up_18], block_size=B, history=True))
                  for B in BLOCKS_18]
answer_MB3_18b = [count_rescalings_18(online_softmax(S_18[down_18], V_18[down_18], block_size=B, history=True))
                  for B in BLOCKS_18]
counts_18 = np.array([[count_rescalings_18(online_softmax(S_18[order], V_18[order], block_size=B, history=True))
                       for B in BLOCKS_18] for order in ORDERS_18])
answer_MB3_18c = counts_18.mean(axis=0).tolist()
answer_MB3_18d = [sum(1 / k for k in range(1, 600 // B + 1)) - 1 for B in BLOCKS_18]
answer_MB3_18e = [5 + 4 * B for B in BLOCKS_18]
finals_18 = [online_softmax(S_18[order], V_18[order], block_size=B)
             for order in (up_18, down_18, np.arange(600)) for B in BLOCKS_18]
answer_MB3_18f = all(math.isclose(m, finals_18[0][0], rel_tol=1e-12) and math.isclose(l, finals_18[0][1], rel_tol=1e-12)
                     and np.allclose(acc, finals_18[0][2], rtol=1e-12, atol=0) for m, l, acc in finals_18)
print("a)", answer_MB3_18a, " b)", answer_MB3_18b, " c)", np.round(answer_MB3_18c, 4).tolist(),
      " (erreurs types :", np.round(counts_18.std(axis=0, ddof=1) / math.sqrt(300), 3).tolist(), ")")
print("d)", np.round(answer_MB3_18d, 4).tolist(), " e)", answer_MB3_18e, " f)", answer_MB3_18f)''',
    record='''def rescalings_18r(scores, size):
    """The oracle: the block maxima read in order; a rescaling when the running maximum grows, after the first finite
    block (no mymath function)."""
    running, count = -math.inf, 0
    for start in range(0, len(scores), size):
        top = max(scores[start:start + size])
        if top > running:
            count += running > -math.inf
            running = top
    return int(count)


rng_18r = np.random.default_rng(7318)
S_18r = rng_18r.normal(0, 1, 600)
rng_18r.normal(0, 1, (600, 3))                                         # the values: drawn, not needed here
orders_18r = [rng_18r.permutation(600) for _ in range(300)]
sizes_18r = (1, 6, 60)
up_18r = np.sort(S_18r)
a_18r = [rescalings_18r(up_18r, B) for B in sizes_18r]
wbm.record("MB3.18a", a_18r,
           mistakes={"la lecture du premier bloc n'est pas une remise à l'échelle : rien n'était accumulé avant":
                         [a + 1 for a in a_18r],
                     "la liste suit l'ordre de BLOCKS_18 : B = 1, 6, 60": a_18r[::-1]})
wbm.record("MB3.18b", [rescalings_18r(up_18r[::-1], B) for B in sizes_18r],
           mistakes={"la lecture du premier bloc n'est pas une remise à l'échelle : rien n'était accumulé avant": [1, 1, 1]})
c_18r = [float(np.mean([rescalings_18r(S_18r[order], B) for order in orders_18r])) for B in sizes_18r]
wbm.record("MB3.18c", c_18r, decimals=6,
           mistakes={"la lecture du premier bloc n'est pas une remise à l'échelle : rien n'était accumulé avant":
                         [c + 1 for c in c_18r],
                     "la liste suit l'ordre de BLOCKS_18 : B = 1, 6, 60": c_18r[::-1]})
harmonic_18r = [sum(1 / k for k in range(1, 600 // B + 1)) for B in sizes_18r]
wbm.record("MB3.18d", [h - 1 for h in harmonic_18r], decimals=6,
           mistakes={"c'est H_N − 1 : le premier bloc ne compte pas": harmonic_18r,
                     "H_N est la somme 1 + 1/2 + … + 1/N, pas ln N": [math.log(600 // B) - 1 for B in sizes_18r]})
wbm.record("MB3.18e", [5 + 4 * B for B in sizes_18r],
           mistakes={"l'état compte aussi : m, l et les 3 nombres de l'accumulateur": [4 * B for B in sizes_18r],
                     "chaque valeur est un vecteur de longueur 3 : B scores et 3B nombres": [5 + 2 * B for B in sizes_18r]})
wbm.record("MB3.18f", True,
           mistakes={"l'état final ne dépend ni de l'ordre ni de la taille des blocs : compare m, l et l'accumulateur à "
                     "10⁻¹² près (relatif), pas avec ==": False})
for scores_18r, size_18r, id_18r in __HIDDEN_C18__:                # the hidden cases of count_rescalings_18
    wbm.record(id_18r, rescalings_18r(scores_18r, size_18r))''',
    after=[
        ("solution", answers_check("MB3.18", "abcdef") + "\n\n" + CHECK_18),
        look("comment la moyenne de c) grandit-elle avec $N$ ? Qu'est-ce que l'ordre change, et qu'est-ce qu'il ne change "
             "pas ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB3.19 · three clocks
# ---------------------------------------------------------------------------
GIVEN_19 = '''PERIODS_19 = np.array([24.0, 168.0, 8760.0])      # the day, the week, the year (hours)
W_19 = 2 * np.pi / PERIODS_19                         # their angular frequencies omega_k
DATES_19 = {"3 mars 8 h": 1472, "3 mars 20 h": 1484, "10 mars 8 h": 1640, "3 septembre 8 h": 5888}   # t in hours
DELTAS_19 = np.arange(0, 8761)                        # the gaps of the curve (hours)
for _array in (PERIODS_19, W_19, DELTAS_19):
    _array.setflags(write=False)'''

CHECK_19 = '''HIDDEN_C19 = __HIDDEN_C19__   # hidden times and the sub-ID of their encodings; hidden dates and gaps for the figures


def on_unit_circle_c19(ax):
    """True when ax shows the unit circle: a Circle patch of radius 1 at (0, 0), or a line of at least 50 points of
    norm 1 that goes around."""
    for patch in ax.patches:
        if type(patch).__name__ == "Circle" and abs(patch.get_radius() - 1) < 1e-9 and np.allclose(patch.center, 0):
            return True
    for line in ax.lines:
        x, y = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
        if x.size >= 50 and np.allclose(x ** 2 + y ** 2, 1, atol=1e-6) and np.ptp(np.arctan2(y, x)) > 6:
            return True
    return False


def clocks_why_c19(axes, times, labels, arrays):
    """What is wrong in a call of draw_clocks_19 (French phrases)."""
    if not isinstance(arrays, (list, tuple)) or len(arrays) != 3:
        return [f"draw_clocks_19 doit rendre la liste des 3 tableaux tracés (un par horloge), reçu {shown(arrays)}"]
    arrays = [as_floats(a) for a in arrays]
    if any(a is None or a.shape != (len(times), 2) for a in arrays):
        return [f"chaque tableau tracé a une ligne par date et deux colonnes (cos, sin) : la forme ({len(times)}, 2)"]
    codes = np.array([as_floats(encode_19(t)) for t in times])
    problems = []
    if not all(matches(a, codes[:, 2 * k:2 * k + 2]) for k, a in enumerate(arrays)):
        problems.append("les tableaux tracés sont les points (cos ω_k t, sin ω_k t) de chaque date, horloge par horloge, "
                        "dans l'ordre journée, semaine, année")
    for k, (ax, a) in enumerate(zip(axes, arrays)):
        missing = []
        if not on_unit_circle_c19(ax):
            missing.append("le cercle unité (une courbe d'au moins 50 points, ou plt.Circle)")
        if not points_at(ax, a[:, 0], a[:, 1]):
            missing.append("un point par date (ax.scatter, ou ax.plot avec un marqueur)")
        if not all(name_near(ax, name, x, y, 2.0) for name, (x, y) in zip(labels, a)):
            missing.append("le nom de chaque date près de son point (ax.annotate ou ax.text)")
        if ax.get_aspect() not in (1.0, "equal"):
            missing.append('la même échelle sur les deux axes (ax.set_aspect("equal"))')
        if missing:
            problems.append(f"horloge {k + 1} : il manque " + " ; ".join(missing))
    return problems


def curve_why_c19(ax, deltas, dots):
    """What is wrong in a call of draw_dot_curve_19 (French phrases)."""
    dots = as_floats(dots)
    if dots is None or dots.shape != (len(deltas),):
        return [f"draw_dot_curve_19 rend le tableau des produits scalaires, de forme ({len(deltas)},), reçu {shown(dots)}"]
    problems = []
    e0 = as_floats(encode_19(0))
    if not matches(dots, [float(e0 @ as_floats(encode_19(d))) for d in deltas], rtol=1e-9, atol=1e-9):
        problems.append("le tableau rendu est E(0)·E(δ) pour chaque écart δ de deltas")
    if not line_with(ax, np.asarray(deltas, dtype=float) / 24, dots):
        problems.append("la courbe en fonction de l'écart en jours, δ/24, en abscisse (ax.plot(deltas / 24, …))")
    if not ax.get_xlabel():
        problems.append("un nom pour l'axe des abscisses")
    return problems


with checked("MB3.19"):
    results_19 = []
    report_19 = reporter(results_19, stop=False)
    codes_c19 = [as_floats(call_safely("Ex MB3.19 : encode_19 (appel caché)", encode_19, t)) for t in HIDDEN_C19["t"]]
    if any(c is None or c.shape != (6,) for c in codes_c19):
        report_19(False, "", "encode_19(t) rend les six nombres (cos ω₁t, sin ω₁t, cos ω₂t, sin ω₂t, cos ω₃t, sin ω₃t)")
    else:
        report_19(passes(HIDDEN_C19["id"], [c.tolist() for c in codes_c19]), "encode_19 : des instants cachés, comme attendu",
                  "encode_19 sur des instants cachés : relis l'ordre (cos, sin) par horloge, et ω_k = 2π/τ_k, t en heures")
    fig_19, axes_19 = plt.subplots(1, 4, figsize=(17, 4.4), gridspec_kw={"width_ratios": [1, 1, 1, 1.6]})
    try:
        names_19, times_19 = list(DATES_19), list(DATES_19.values())
        drawn_19 = []
        opened_19 = drawn(lambda: drawn_19.append(call_safely("Ex MB3.19 : draw_clocks_19", draw_clocks_19, axes_19[:3],
                                                              times_19, names_19)))
        problems_19 = clocks_why_c19(axes_19[:3], times_19, names_19, drawn_19[0])
        report_19(not problems_19, "draw_clocks_19 : les trois horloges, les cercles, les points, les noms et l'échelle",
                  "draw_clocks_19 : " + " ; ".join(problems_19))
        dots_19 = []
        opened_19 += drawn(lambda: dots_19.append(call_safely("Ex MB3.19 : draw_dot_curve_19", draw_dot_curve_19,
                                                              axes_19[3], DELTAS_19)))
        problems_19 = curve_why_c19(axes_19[3], DELTAS_19, dots_19[0])
        report_19(not problems_19, "draw_dot_curve_19 : E(0)·E(δ) en fonction de l'écart en jours",
                  "draw_dot_curve_19 : " + " ; ".join(problems_19))
        fig_c19, axes_c19 = plt.subplots(1, 5)          # the 5th axes is the current one: plt.plot would draw there
        try:
            hidden_19 = []
            opened_19 += drawn(lambda: hidden_19.append(call_safely("Ex MB3.19 : draw_clocks_19 (appel caché)",
                                                                    draw_clocks_19, axes_c19[:3], HIDDEN_C19["dates"],
                                                                    HIDDEN_C19["labels"])))
            problems_c19 = clocks_why_c19(axes_c19[:3], HIDDEN_C19["dates"], HIDDEN_C19["labels"], hidden_19[0])
            hidden_dots_19 = []
            opened_19 += drawn(lambda: hidden_dots_19.append(call_safely("Ex MB3.19 : draw_dot_curve_19 (appel caché)",
                                                                         draw_dot_curve_19, axes_c19[3],
                                                                         np.array(HIDDEN_C19["deltas"]))))
            problems_c19 += curve_why_c19(axes_c19[3], HIDDEN_C19["deltas"], hidden_dots_19[0])
            elsewhere_19 = bool(axes_c19[4].lines or axes_c19[4].collections or axes_c19[4].texts or axes_c19[4].patches)
        finally:
            plt.close(fig_c19)
        report_19(not problems_c19, "des appels cachés (deux autres dates, d'autres écarts) sont justes aussi",
                  "des appels cachés (deux autres dates, d'autres écarts) : " + " ; ".join(problems_c19))
        report_19(not opened_19 and not elsewhere_19, "tes fonctions dessinent dans les axes reçus",
                  "tes fonctions doivent dessiner dans les axes reçus (ax.plot, ax.annotate…), sans ouvrir de figure ni "
                  "dessiner dans l'axe courant (plt.plot, plt.text…)")
    except BaseException:
        plt.close(fig_19)
        raise
    fig_19.tight_layout()
    plt.show()
    verdict("MB3.19", all(results_19) and len(results_19) == 5, "ton encodage et tes deux figures sont justes.",
            "relis les lignes ❌ ci-dessus.")'''

NOTE_19 = (r"`encode_19` : `np.array([f(w * t) for w in W_19 for f in (np.cos, np.sin)])`. a) $(-0{,}5 ;\ 0{,}866025 ;\ "
           r"0{,}074730 ;\ -0{,}997204 ;\ 0{,}492528 ;\ 0{,}870297)$. b) $(0{,}900932 ;\ -1{,}001814 ;\ -1{,}099031 ;\ "
           r"2{,}623490)$. c) $\delta = 8\,736$ h (52 semaines), où le produit vaut $\approx 2{,}999852$. d) Vrai.")

MB3_19 = Ex(
    "MB3.19", "🎨", 1, 20, "Trois horloges (la journée, la semaine, l'année) : l'encodage d'une date sur trois cercles, un "
    "décalage comme trois rotations, et le produit scalaire de deux encodages en fonction de l'écart",
    "encoder une date par trois horloges, la dessiner sur trois cercles, lire un décalage comme trois rotations, et "
    "tracer le produit scalaire de deux encodages en fonction de leur écart.", "fiche §3 et §4 ; Ex MB3.3 et MB3.14",
    tracks="C, E", given=GIVEN_19, note=NOTE_19,
    body=r"""Une date est repérée par $t$, le nombre d'heures écoulées depuis le lundi 1ᵉʳ janvier à 0 h d'une année de 365 jours. Elle est encodée par trois horloges de périodes 24 h, 168 h et 8 760 h (`PERIODS_19`), de pulsations $\omega_k = 2\pi/\tau_k$ (`W_19`) : `encode_19(t)` rend les six nombres $\mathbf{E}(t) = (\cos\omega_1t, \sin\omega_1t, \cos\omega_2t, \sin\omega_2t, \cos\omega_3t, \sin\omega_3t)$. Écris `encode_19(t)`, puis `draw_clocks_19(axes, times, labels)`, qui reçoit une ligne de trois axes (une horloge par axe) et y trace le cercle unité, le point de chaque date de `times` avec son nom (pris dans `labels`) et une même échelle sur les deux axes (`ax.set_aspect("equal")`), et rend la liste des trois tableaux tracés (un tableau de forme `(len(times), 2)` par horloge) ; puis `draw_dot_curve_19(ax, deltas)`, qui trace $\mathbf{E}(0)\cdot\mathbf{E}(\delta)$ en fonction de l'écart $\delta$, en jours sur l'axe des abscisses ($\delta/24$), et rend le tableau des produits scalaires. Les fonctions dessinent dans les axes reçus, sans ouvrir de figure.

La vérification appelle `draw_clocks_19` avec les quatre dates de `DATES_19` (le 3 mars à 8 h, $t = 1\,472$, le 3 mars à 20 h, le 10 mars à 8 h et le 3 septembre à 8 h), puis `draw_dot_curve_19` avec `DELTAS_19` ($\delta = 0, 1, \ldots, 8\,760$ h), affiche la figure, et essaie tes fonctions sur des appels cachés. Relève :
- a) `encode_19(1472)` (6 nombres) ;
- b) $\mathbf{E}(0)\cdot\mathbf{E}(\delta)$ pour $\delta = 12$, 84, 4 380 et 8 760 h (une liste de 4 nombres) ;
- c) l'écart $\delta \in \{1, \ldots, 8\,760\}$ (en heures entières) où ce produit scalaire est le plus grand, puis sa valeur (une liste de 2) ;
- d) vrai ou faux : `encode_19(1472 + 30)` égale $\mathbf{M}$ fois `encode_19(1472)` à $10^{-12}$ près, où $\mathbf{M}$ est le produit des trois rotations `givens_rotation(6, 0, 1, 30 * W_19[0])`, `givens_rotation(6, 2, 3, 30 * W_19[1])` et `givens_rotation(6, 4, 5, 30 * W_19[2])` (ta fonction de MB3.14).""",
    todo='''def encode_19(t):
    """The six numbers (cos w1 t, sin w1 t, cos w2 t, sin w2 t, cos w3 t, sin w3 t) of the time t (hours), w = W_19."""
    raise NotImplementedError("encode_19 n'est pas encore écrite (04_indices.md si tu bloques)")


def draw_clocks_19(axes, times, labels):
    """axes: a row of 3 axes (the day, the week, the year). In each: the unit circle, the point of each time of times on
    that clock, with its name (labels) next to it, the same scale on both axes. Returns the list of the 3 arrays drawn,
    each of shape (len(times), 2). Opens no figure."""
    raise NotImplementedError("draw_clocks_19 n'est pas encore écrite (04_indices.md si tu bloques)")


def draw_dot_curve_19(ax, deltas):
    """In the axes ax: E(0)·E(delta) as a function of the gap delta in days (delta / 24), with axis labels. Returns the
    array of the dot products. Opens no figure."""
    raise NotImplementedError("draw_dot_curve_19 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB3_19a = answer_MB3_19b = answer_MB3_19c = answer_MB3_19d = ...
with wbm.attempt("MB3.19"):          # your functions: ⏳ while they are not written
    answer_MB3_19a = ...  # a) a list of 6 numbers, as computed: encode_19(1472)
    answer_MB3_19b = ...  # b) a list of 4 numbers, as computed: E(0)·E(delta) for delta = 12, 84, 4380, 8760 h
    answer_MB3_19c = ...  # c) a list of 2: the gap delta in {1, ..., 8760} (whole hours) of the largest dot product, then its value
    answer_MB3_19d = ...  # d) True or False: encode_19(1472 + 30) equals M encode_19(1472) to 1e-12''',
    check=answers_check("MB3.19", "abcd") + "\n\n" + CHECK_19,
    solution='''def encode_19(t):
    """The six numbers (cos w1 t, sin w1 t, cos w2 t, sin w2 t, cos w3 t, sin w3 t) of the time t (hours), w = W_19."""
    return np.array([f(w * t) for w in W_19 for f in (np.cos, np.sin)])


def draw_clocks_19(axes, times, labels):
    """axes: a row of 3 axes (the day, the week, the year). In each: the unit circle, the point of each time of times on
    that clock, with its name (labels) next to it, the same scale on both axes. Returns the list of the 3 arrays drawn,
    each of shape (len(times), 2). Opens no figure."""
    codes = np.array([encode_19(t) for t in times])
    angles = np.linspace(0, 2 * np.pi, 361)
    arrays = []
    for k, (ax, name) in enumerate(zip(axes, ("la journée (24 h)", "la semaine (168 h)", "l'année (8 760 h)"))):
        points = codes[:, 2 * k:2 * k + 2]
        ax.plot(np.cos(angles), np.sin(angles), color="0.7", lw=1)
        ax.scatter(points[:, 0], points[:, 1], s=30, zorder=3)
        for label, (x, y) in zip(labels, points):
            ax.annotate(label, (x, y), textcoords="offset points", xytext=(4, 4), fontsize=7)
        ax.set_aspect("equal")
        ax.set_title(name, fontsize=10)
        arrays.append(points)
    return arrays


def draw_dot_curve_19(ax, deltas):
    """In the axes ax: E(0)·E(delta) as a function of the gap delta in days (delta / 24), with axis labels. Returns the
    array of the dot products. Opens no figure."""
    e0 = encode_19(0)
    dots = np.array([e0 @ encode_19(d) for d in deltas])
    ax.plot(np.asarray(deltas) / 24, dots, lw=0.6)
    ax.set_xlabel("écart (jours)")
    ax.set_ylabel("E(0)·E(δ)")
    return dots


givens_rotation = mymath.positional.givens_rotation
answer_MB3_19a = encode_19(1472).tolist()
answer_MB3_19b = [float(encode_19(0) @ encode_19(d)) for d in (12, 84, 4380, 8760)]
dots_19 = np.array([encode_19(0) @ encode_19(d) for d in range(1, 8761)])
answer_MB3_19c = [int(np.argmax(dots_19)) + 1, float(dots_19.max())]
M_19 = (givens_rotation(6, 0, 1, 30 * W_19[0]) @ givens_rotation(6, 2, 3, 30 * W_19[1])
        @ givens_rotation(6, 4, 5, 30 * W_19[2]))
answer_MB3_19d = bool(np.allclose(encode_19(1472 + 30), M_19 @ encode_19(1472), rtol=0, atol=1e-12))
print("a)", np.round(answer_MB3_19a, 6).tolist(), " b)", np.round(answer_MB3_19b, 6).tolist())
print("c)", answer_MB3_19c, " d)", answer_MB3_19d)''',
    record='''W_19r = [2 * math.pi / p for p in (24.0, 168.0, 8760.0)]


def encode_19r(t, w=W_19r, swap=False):
    """The oracle: (cos, sin) of w_k t for the three clocks, with math (swap: the classic error (sin, cos))."""
    return [f(x * t) for x in w for f in ((math.sin, math.cos) if swap else (math.cos, math.sin))]


def dot_19r(delta, w=W_19r):
    return sum(math.cos(x * delta) for x in w)


wbm.record("MB3.19a", encode_19r(1472), decimals=6,
           mistakes={"pour chaque horloge, (cos ω_k t, sin ω_k t), le cosinus d'abord": encode_19r(1472, swap=True),
                     "ω_k = 2π/τ_k : un tour par période": encode_19r(1472, w=[1 / p for p in (24.0, 168.0, 8760.0)])})
gaps_19r = (12, 84, 4380, 8760)
wbm.record("MB3.19b", [dot_19r(d) for d in gaps_19r], decimals=6,
           mistakes={"le produit scalaire de deux encodages est la somme des produits des six coordonnées, pas leur "
                     "moyenne": [dot_19r(d) / 3 for d in gaps_19r],
                     "E(0) = (1, 0, 1, 0, 1, 0) : le produit scalaire garde les trois cosinus, de toutes les horloges":
                         [math.cos(W_19r[0] * d) for d in gaps_19r]})
values_19r = [dot_19r(d) for d in range(1, 8761)]
best_19r = max(range(8760), key=lambda k: values_19r[k])
wbm.record("MB3.19c", [best_19r + 1, values_19r[best_19r]], decimals=6,
           mistakes={"cherche le plus grand produit scalaire sur tous les écarts de 1 à 8 760 h, pas seulement l'année "
                     "exacte": [8760, values_19r[-1]],
                     "l'écart se donne en heures": [(best_19r + 1) / 24, values_19r[best_19r]]})
wbm.record("MB3.19d", True,
           mistakes={"chaque horloge tourne de 30 ω_k dans son propre plan : compare les deux vecteurs à 10⁻¹² près, "
                     "avec np.allclose": False})
HIDDEN_19r = __HIDDEN_C19__                                                  # the hidden times of the check
wbm.record(HIDDEN_19r["id"], [encode_19r(t) for t in HIDDEN_19r["t"]], decimals=6)''',
    after=[
        ("solution", answers_check("MB3.19", "abcd") + "\n\n" + CHECK_19),
        look("quelle horloge sépare le 3 mars à 8 h du 3 mars à 20 h ? Et du 3 septembre ? Que vaut le produit scalaire "
             "après un an exactement, et pourquoi ? Quand s'approche-t-il le plus de 3 ?"),
    ],
)

PART_B = Part("B", "Prédire, mesurer, dessiner",
              "Fiche §4, §5, §7, §8 et §9. La largeur de bande de Nadaraya-Watson, prédite puis tracée ; les remises à "
              "l'échelle de la softmax en ligne selon l'ordre et la taille des blocs ; une date sur trois horloges.",
              exercises=[MB3_17, MB3_18, MB3_19])

# ---------------------------------------------------------------------------
# Notebook exercises: debug and test (MB3.20, MB3.21)
# ---------------------------------------------------------------------------
GIVEN_20 = '''# The colleague's code
def R12(t):
    """The rotation of space by t about e_3 (in the plane of e_1 and e_2)."""
    return np.array([[math.cos(t), -math.sin(t), 0.0], [math.sin(t), math.cos(t), 0.0], [0.0, 0.0, 1.0]])


def R23(t):
    """The rotation of space by t about e_1 (in the plane of e_2 and e_3)."""
    return np.array([[1.0, 0.0, 0.0], [0.0, math.cos(t), -math.sin(t)], [0.0, math.sin(t), math.cos(t)]])


def rotate_e3_then_e1(x, alpha, beta):
    """x turned first by alpha about e_3, then by beta about e_1."""
    return R12(alpha) @ R23(beta) @ np.asarray(x, dtype=float)


def mean_direction_bad(angles):
    """The mean direction of directions given in degrees, in [0, 360)."""
    return float(np.mean(angles)) % 360


def online_softmax_bad(scores, values, block_size):
    """The state (m, l, acc) of the online softmax of the scores and the values read by blocks of block_size."""
    s, v = np.asarray(scores, dtype=float), np.asarray(values, dtype=float)
    m, l, acc = -math.inf, 0.0, 0.0
    for start in range(0, len(s), block_size):
        block, block_values = s[start:start + block_size], v[start:start + block_size]
        m_new = max(m, float(block.max()))
        factor = math.exp(m - m_new)
        weights = np.exp(block - m_new)
        l = l * factor + float(weights.sum())
        acc = acc + weights @ block_values
        m = m_new
    return m, l, acc


# The colleague's checks: all pass
print("(1)", bool(np.allclose(rotate_e3_then_e1([1.0, 2.0, 3.0], np.pi, np.pi), [-1.0, 2.0, -3.0])),
      "(attendu True : avec alpha = beta = pi, à la main)")
print("(2)", math.isclose(mean_direction_bad([40, 60, 80]), 60.0), "(attendu True : sur 40°, 60° et 80°)")
s_20, v_20 = np.array([3.2, 2.7, 2.0, 1.1, 0.4, -0.5]), np.array([2.0, 3.0, 1.0, 4.0, 5.0, 6.0])
m_20, l_20, acc_20 = online_softmax_bad(s_20, v_20, 2)
direct_20 = float(np.exp(s_20 - s_20.max()) @ v_20 / np.exp(s_20 - s_20.max()).sum())
print("(3)", math.isclose(acc_20 / l_20, direct_20), "(attendu True : des scores rangés en ordre décroissant)")'''

CHECK_20 = '''CASES_C20 = __CASES_C20__   # the hidden cases of the three corrected functions, and the sub-IDs expected

results_20, parts_20 = [], []


def report_20(ok, success, failure):
    results_20.append(bool(ok))
    print(("✅ " + success) if ok else ("❌ " + failure))


def call_20(part, name, function, *args):
    """function(*args); an error of the learner's code becomes one ❌ line that names the function."""
    try:
        return function(*args)
    except (NotImplementedError, MymathMissingError):
        raise
    except Exception as exc:  # noqa: BLE001 - the learner's error, reported with the name of the function
        report_20(False, "", f"({part}) {name} : ton code lève {type(exc).__name__} : {str(exc)[:160]}")
        parts_20.append(part)
        raise StopCheck from None


with checked("MB3.20"):                                      # (1) rotate_e3_then_e1_fixed
    got_c20, wrong_c20 = [], []
    for x_c20, alpha_c20, beta_c20 in CASES_C20["rotations"]:
        x_c20 = np.array(x_c20)                              # floats: a change in place would show
        before_c20 = x_c20.copy()
        got_c20.append(as_floats(call_20(1, "rotate_e3_then_e1_fixed", rotate_e3_then_e1_fixed, x_c20, alpha_c20, beta_c20)))
        if not np.array_equal(x_c20, before_c20):
            wrong_c20.append("ta fonction modifie le vecteur reçu : travaille sur une copie")
    if any(g is None or g.shape != (3,) for g in got_c20):
        wrong_c20.append("rotate_e3_then_e1_fixed rend un vecteur de 3 nombres")
    elif not passes(CASES_C20["ids"][0], [g.tolist() for g in got_c20]):
        same_c20 = all(np.allclose(g, rotate_e3_then_e1(x, a, b)) for g, (x, a, b) in zip(got_c20, CASES_C20["rotations"]))
        wrong_c20.append("ta correction rend encore le résultat de la version du collègue : dans un produit de matrices "
                         "appliqué à x, c'est la matrice de droite qui agit la première" if same_c20 else
                         "sur d'autres angles et d'autres vecteurs, ce n'est pas x tourné d'abord de alpha autour de e₃, "
                         "puis de beta autour de e₁")
    report_20(not wrong_c20, "(1) rotate_e3_then_e1_fixed : trois cas cachés (d'autres angles, d'autres vecteurs)",
              "(1) rotate_e3_then_e1_fixed : " + " ; ".join(dict.fromkeys(wrong_c20)))
    parts_20.append(1)

with checked("MB3.20"):                                      # (2) mean_direction_fixed
    got_c20 = [call_20(2, "mean_direction_fixed", mean_direction_fixed, list(angles)) for angles in CASES_C20["directions"]]
    numbers_c20 = as_floats(got_c20)
    if numbers_c20 is None or numbers_c20.shape != (len(got_c20),):
        why_c20 = f"mean_direction_fixed rend un nombre (des degrés), reçu {shown(got_c20)}"
    elif np.any(numbers_c20 < 0) or np.any(numbers_c20 >= 360):
        why_c20 = "la direction moyenne est dans [0, 360[ : ajoute 360 à un angle négatif (ou % 360)"
    elif passes(CASES_C20["ids"][1], numbers_c20.tolist()):
        why_c20 = ""
    elif all(math.isclose(g, mean_direction_bad(a), abs_tol=1e-6) for g, a in zip(numbers_c20, CASES_C20["directions"])):
        why_c20 = "ta correction rend encore la moyenne des angles : moyenne les vecteurs (cos θ, sin θ)"
    else:
        why_c20 = ("sur des directions de part et d'autre de 0°, ou autour de 180°, ce n'est pas l'angle du vecteur moyen "
                   "des (cos θ, sin θ), en degrés (np.arctan2 garde le bon quadrant)")
    report_20(not why_c20, "(2) mean_direction_fixed : des directions cachées, de part et d'autre de 0° et autour de 180°",
              f"(2) mean_direction_fixed : {why_c20}")
    parts_20.append(2)

with checked("MB3.20"):                                      # (3) online_softmax_fixed, compared with the reference
    wrong_c20 = []
    for scores_c20, values_c20, size_c20 in CASES_C20["softmax"]:
        scores_c20, values_c20 = np.array(scores_c20), np.array(values_c20)
        before_c20 = (scores_c20.copy(), values_c20.copy())
        got_c20 = call_20(3, "online_softmax_fixed", online_softmax_fixed, scores_c20, values_c20, size_c20)
        want_c20 = ref_pos.online_softmax(before_c20[0], before_c20[1], block_size=size_c20)
        if not (np.array_equal(scores_c20, before_c20[0]) and np.array_equal(values_c20, before_c20[1])):
            wrong_c20.append("ta fonction modifie les tableaux reçus : travaille sur des copies")
        elif state_parts(got_c20) is None:
            wrong_c20.append(f"online_softmax_fixed rend l'état (m, l, acc), reçu {shown(got_c20)}")
        elif not same_state(got_c20, want_c20, rtol=1e-9):
            bad_c20 = online_softmax_bad(before_c20[0], before_c20[1], size_c20)
            wrong_c20.append("l'accumulateur n'est toujours pas remis à l'échelle quand le maximum change"
                             if same_state(got_c20, bad_c20) else
                             "sur des scores dans un ordre quelconque et des valeurs 2-D, ce n'est pas l'état (m, l, acc) "
                             "de la softmax en ligne : quand le maximum change, l ET acc sont multipliés par e^(m − m')")
    report_20(not wrong_c20, "(3) online_softmax_fixed : des scores cachés dans un ordre quelconque, des valeurs 1-D et 2-D",
              "(3) online_softmax_fixed : " + " ; ".join(list(dict.fromkeys(wrong_c20))[:2]))
    parts_20.append(3)

if len(set(parts_20)) == 3:
    verdict("MB3.20", all(results_20), "les trois fonctions corrigées passent tous les cas.", "relis les lignes ❌ ci-dessus.")'''

NOTE_20 = (r"(1) `rotate_e3_then_e1` applique d'abord la rotation autour de $\mathbf{e}_1$ (la matrice de droite agit la "
           r"première) ; correction : `R23(beta) @ R12(alpha) @ x`. a) $(1{,}732051 ;\ -1 ;\ 1)$, puis "
           r"$(2{,}232051 ;\ 0{,}133975 ;\ 0)$. (2) La moyenne des angles ignore que 0° et 360° sont la même direction ; "
           r"correction : `np.degrees(np.arctan2(np.sin(a).mean(), np.cos(a).mean())) % 360` pour `a` en radians. b) "
           r"2,5°, puis 182,5°. (3) L'accumulateur se remet à l'échelle comme $l$ : `acc = acc * factor + weights @ "
           r"block_values`. c) $\approx 2{,}393046$, puis $\approx 3{,}056764$.")

MB3_20 = Ex(
    "MB3.20", "🐛", 1, 25, "Chasse à l'erreur : deux rotations de l'espace composées dans le mauvais ordre, une direction "
    "moyenne prise comme la moyenne des angles, une softmax en ligne qui remet l à l'échelle mais pas l'accumulateur",
    "reconnaître trois erreurs classiques sur l'ordre de deux rotations, la moyenne de directions et la remise à "
    "l'échelle de la softmax en ligne, qui passent une vérification mal choisie, puis les corriger.",
    "fiche §3, §4 et §8 ; Ex MB3.2, MB3.3 et MB3.7", tracks="C, E", given=GIVEN_20, note=NOTE_20,
    body=r"""Un collègue a écrit trois fonctions, chacune accompagnée d'une vérification qui passe (cellule fournie) :
1. `rotate_e3_then_e1(x, alpha, beta)` doit tourner $\mathbf{x}$ d'abord de $\alpha$ autour de $\mathbf{e}_3$, puis de $\beta$ autour de $\mathbf{e}_1$ ; elle rend `R12(alpha) @ R23(beta) @ x`, où `R12` et `R23` sont ces deux rotations. Il l'a vérifiée avec $\alpha = \beta = \pi$.
2. `mean_direction_bad(angles)` doit rendre la direction moyenne de directions données en degrés, dans $[0, 360[$ ; elle rend `np.mean(angles) % 360`. Il l'a vérifiée sur les relevés 40°, 60° et 80°.
3. `online_softmax_bad(scores, values, block_size)` doit rendre l'état de la softmax en ligne ; quand le maximum change, elle remet $l$ à l'échelle, mais pas l'accumulateur. Il l'a vérifiée en comparant $a/l$ à la moyenne pondérée calculée en une fois, pour des scores rangés en ordre décroissant.

À faire : trouve et corrige chaque erreur ; les fonctions corrigées s'appellent `rotate_e3_then_e1_fixed`, `mean_direction_fixed` et `online_softmax_fixed`, avec les mêmes arguments (sans `mymath`). Puis réponds :
- a) pour $\mathbf{x} = (2, 0, 1)$, $\alpha = \frac\pi6$ et $\beta = \frac\pi2$ : le résultat de la fonction corrigée, puis de la fonction fautive (une liste de 6 nombres) ;
- b) la direction moyenne des relevés 340°, 10°, 25° et 355°, par la fonction corrigée, puis par la fonction fautive (une liste de 2 nombres) ;
- c) pour les scores $(0{,}4 ;\ 2 ;\ 1{,}1 ;\ 3{,}2 ;\ -0{,}5 ;\ 2{,}7)$, les valeurs $(5, 1, 4, 2, 6, 3)$ et des blocs de 2 : $a/l$ par la fonction corrigée, puis par la fonction fautive (une liste de 2 nombres).

Dans ta copie : pour chacune des trois erreurs, pourquoi la vérification du collègue ne la voyait pas. La vérification essaie tes corrections sur des cas cachés : d'autres angles et d'autres vecteurs, des directions de part et d'autre de 0° et autour de 180°, des scores dans un ordre quelconque et des valeurs 2-D.""",
    todo='''def rotate_e3_then_e1_fixed(x, alpha, beta):
    """x turned first by alpha about e_3, then by beta about e_1."""
    raise NotImplementedError("rotate_e3_then_e1_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def mean_direction_fixed(angles):
    """The mean direction of directions given in degrees, in [0, 360)."""
    raise NotImplementedError("mean_direction_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def online_softmax_fixed(scores, values, block_size):
    """The state (m, l, acc) of the online softmax of the scores and the values read by blocks of block_size."""
    raise NotImplementedError("online_softmax_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB3_20a = answer_MB3_20b = answer_MB3_20c = ...
with wbm.attempt("MB3.20"):          # your three functions: ⏳ while they are not written
    answer_MB3_20a = ...  # a) a list of 6 numbers, as computed: rotate_e3_then_e1_fixed, then the WRONG rotate_e3_then_e1
    answer_MB3_20b = ...  # b) a list of 2 numbers, as computed: mean_direction_fixed, then the WRONG mean_direction_bad
    answer_MB3_20c = ...  # c) a list of 2 numbers, as computed: a / l by online_softmax_fixed, then by the WRONG online_softmax_bad''',
    check=answers_check("MB3.20", "abc") + "\n\n" + CHECK_20,
    solution='''def rotate_e3_then_e1_fixed(x, alpha, beta):
    """x turned first by alpha about e_3, then by beta about e_1."""
    return R23(beta) @ R12(alpha) @ np.asarray(x, dtype=float)          # the matrix on the right acts first


def mean_direction_fixed(angles):
    """The mean direction of directions given in degrees, in [0, 360)."""
    a = np.radians(np.asarray(angles, dtype=float))
    return float(np.degrees(np.arctan2(np.sin(a).mean(), np.cos(a).mean()))) % 360      # the mean of the vectors


def online_softmax_fixed(scores, values, block_size):
    """The state (m, l, acc) of the online softmax of the scores and the values read by blocks of block_size."""
    s, v = np.asarray(scores, dtype=float), np.asarray(values, dtype=float)
    m, l, acc = -math.inf, 0.0, 0.0
    for start in range(0, len(s), block_size):
        block, block_values = s[start:start + block_size], v[start:start + block_size]
        m_new = max(m, float(block.max()))
        factor = math.exp(m - m_new)
        weights = np.exp(block - m_new)
        l = l * factor + float(weights.sum())
        acc = acc * factor + weights @ block_values                     # acc rescaled like l
        m = m_new
    return m, l, acc


x_20 = np.array([2.0, 0.0, 1.0])
answer_MB3_20a = (rotate_e3_then_e1_fixed(x_20, np.pi / 6, np.pi / 2).tolist()
                  + rotate_e3_then_e1(x_20, np.pi / 6, np.pi / 2).tolist())
answer_MB3_20b = [mean_direction_fixed([340, 10, 25, 355]), mean_direction_bad([340, 10, 25, 355])]
scores_c_20, values_c_20 = [0.4, 2.0, 1.1, 3.2, -0.5, 2.7], [5.0, 1.0, 4.0, 2.0, 6.0, 3.0]
answer_MB3_20c = [(lambda m, l, acc: float(acc / l))(*online_softmax_fixed(scores_c_20, values_c_20, 2)),
                  (lambda m, l, acc: float(acc / l))(*online_softmax_bad(scores_c_20, values_c_20, 2))]
print("a)", np.round(answer_MB3_20a, 6).tolist(), " b)", np.round(answer_MB3_20b, 6).tolist(),
      " c)", np.round(answer_MB3_20c, 6).tolist())''',
    record='''from scipy.spatial.transform import Rotation as Rotation_20r
from scipy.special import softmax as softmax_20r


def turned_20r(x, alpha, beta, first="z"):
    """The oracle: x turned by alpha about e_3, then by beta about e_1 (scipy, extrinsic rotations); first="x" is the
    colleague's order."""
    angles = [alpha, beta] if first == "z" else [beta, alpha]
    return Rotation_20r.from_euler("zx" if first == "z" else "xz", angles).apply(np.asarray(x, dtype=float)).tolist()


def direction_20r(angles):
    a = np.radians(angles)
    return math.degrees(math.atan2(float(np.mean(np.sin(a))), float(np.mean(np.cos(a))))) % 360


right_a_20r, bad_a_20r = turned_20r([2.0, 0, 1], math.pi / 6, math.pi / 2), turned_20r([2.0, 0, 1], math.pi / 6,
                                                                                     math.pi / 2, first="x")
wbm.record("MB3.20a", right_a_20r + bad_a_20r, decimals=6,
           mistakes={"rotate_e3_then_e1_fixed applique encore d'abord la rotation autour de e₁ : dans un produit de "
                     "matrices appliqué à x, c'est la matrice de droite qui agit la première": bad_a_20r + bad_a_20r,
                     "les trois derniers nombres sont ceux de la version FAUSSE, rotate_e3_then_e1": right_a_20r + right_a_20r,
                     "la version corrigée d'abord, puis la version fautive": bad_a_20r + right_a_20r})
readings_20r = [340, 10, 25, 355]
right_b_20r, bad_b_20r = direction_20r(readings_20r), float(np.mean(readings_20r)) % 360
wbm.record("MB3.20b", [right_b_20r, bad_b_20r], decimals=6,
           mistakes={"mean_direction_fixed rend encore la moyenne des angles : moyenne les vecteurs (cos θ, sin θ)":
                         [bad_b_20r, bad_b_20r],
                     "le second nombre est celui de la version FAUSSE, mean_direction_bad": [right_b_20r, right_b_20r],
                     "la direction se donne en degrés": [math.radians(right_b_20r), bad_b_20r]})
s_20r, v_20r = np.array([0.4, 2.0, 1.1, 3.2, -0.5, 2.7]), np.array([5.0, 1, 4, 2, 6, 3])
right_c_20r = float(softmax_20r(s_20r) @ v_20r)
m_20r, l_20r, acc_20r = -math.inf, 0.0, 0.0                              # the colleague's error, written again
for start_20r in range(0, 6, 2):
    new_20r = max(m_20r, float(s_20r[start_20r:start_20r + 2].max()))
    w_20r = np.exp(s_20r[start_20r:start_20r + 2] - new_20r)
    l_20r, acc_20r, m_20r = l_20r * math.exp(m_20r - new_20r) + w_20r.sum(), acc_20r + w_20r @ v_20r[start_20r:start_20r + 2], new_20r
bad_c_20r = float(acc_20r / l_20r)
wbm.record("MB3.20c", [right_c_20r, bad_c_20r], decimals=6,
           mistakes={"online_softmax_fixed ne remet toujours pas l'accumulateur à l'échelle quand le maximum change":
                         [bad_c_20r, bad_c_20r],
                     "le second nombre est celui de la version FAUSSE, online_softmax_bad": [right_c_20r, right_c_20r]})
CASES_20r = __CASES_C20__                                                   # the hidden cases of the check
wbm.record(CASES_20r["ids"][0], [turned_20r(x, a, b) for x, a, b in CASES_20r["rotations"]], decimals=6)
wbm.record(CASES_20r["ids"][1], [direction_20r(angles) for angles in CASES_20r["directions"]], decimals=6)''',
    after=[
        ("solution", answers_check("MB3.20", "abc") + "\n\n" + CHECK_20),
        ("md", "**Après la vérification**, dans ta copie : pour chaque erreur, pourquoi la vérification du collègue ne la "
               "voyait-elle pas, et quelle vérification l'aurait vue ?"),
    ],
)

# ---------------------------------------------------------------------------
# MB3.21 · a property test of the online softmax and of the merge
# ---------------------------------------------------------------------------
GIVEN_21 = '''def differ_21(state1, state2, rtol=1e-9):
    """True when the two states (m, l, acc) differ: their m are not both -inf and differ by more than rtol·max(1, |m|),
    their l differ by more than rtol·max(1, l), or their accumulators are not
    np.allclose(rtol=rtol, atol=rtol * max(1, abs(acc).max())) (m, l and acc of state1 for the tolerances)."""
    m1, l1, a1 = state1
    m2, l2, a2 = state2
    m1, l1, m2, l2 = float(m1), float(l1), float(m2), float(l2)
    if not (m1 == -math.inf and m2 == -math.inf) and not abs(m1 - m2) <= rtol * max(1.0, abs(m1)):
        return True
    if not abs(l1 - l2) <= rtol * max(1.0, abs(l1)):
        return True
    if a1 is None or a2 is None:
        return (a1 is None) != (a2 is None)
    a1, a2 = np.atleast_1d(np.asarray(a1, dtype=float)), np.atleast_1d(np.asarray(a2, dtype=float))
    return a1.shape != a2.shape or not np.allclose(a1, a2, rtol=rtol, atol=rtol * max(1.0, float(np.abs(a1).max())))


def rescale_l_only(scores, values=None, block_size=1, history=False):
    """WRONG: the online softmax of 🐛 MB3.20, which rescales l but not the accumulator."""
    s, v = np.asarray(scores, dtype=float), np.asarray(values, dtype=float)
    m, l, acc = -math.inf, 0.0, np.zeros(v.shape[1:])
    for start in range(0, len(s), block_size):
        block, block_values = s[start:start + block_size], v[start:start + block_size]
        if np.all(np.isneginf(block)):
            continue
        m_new = max(m, float(block.max()))
        weights = np.exp(block - m_new)
        l = l * math.exp(m - m_new) + float(weights.sum())
        acc = acc + weights @ block_values
        m = m_new
    return m, l, acc


def centered(scores, values=None, block_size=1, history=False):
    """WRONG: an online softmax that first subtracts from the scores the mean of the finite scores."""
    s = np.asarray(scores, dtype=float)
    finite = np.isfinite(s)
    return ref_pos.online_softmax(s - (float(s[finite].mean()) if finite.any() else 0.0), values, block_size=block_size)


def merge_no_rescale(state1, state2):
    """WRONG: a merge that adds the l and the accumulators without rescaling them."""
    return max(state1[0], state2[0]), state1[1] + state2[1], np.asarray(state1[2], dtype=float) + np.asarray(state2[2], dtype=float)


def merge_mean(state1, state2):
    """WRONG: a merge that takes the mean of the two states rescaled, instead of their sum."""
    m = max(state1[0], state2[0])
    f1 = math.exp(state1[0] - m) if state1[0] > -math.inf else 0.0
    f2 = math.exp(state2[0] - m) if state2[0] > -math.inf else 0.0
    return (m, (state1[1] * f1 + state2[1] * f2) / 2,
            (np.asarray(state1[2], dtype=float) * f1 + np.asarray(state2[2], dtype=float) * f2) / 2)


# The loop of the property test (provided): the draws, in a fixed order, and the counters
def softmax_property_test_21(n_trials, rng, func=None, merge=None, rtol=1e-9, checks=None):
    """n_trials random cases, drawn in this order: n = int(rng.integers(3, 13)), scores = rng.normal(0, 3, n), then, if
    rng.random() < 0.3, the scores where rng.random(n) < 0.25 set to -inf and the score of index int(rng.integers(n))
    given the value float(rng.normal(0, 3)); then values = rng.normal(0, 1, (n, 2)), block_size =
    int(rng.integers(1, n + 1)), perm = rng.permutation(n), shift = float(rng.normal(0, 20)) and the cuts
    sorted(rng.choice(np.arange(1, n), 2, replace=False)). func defaults to mymath.positional.online_softmax, merge to
    mymath.positional.merge_softmax_states, checks to your failed_checks_21, all looked up at the call; each name
    returned by checks adds 1 to its counter. Returns the counters "blocks", "permutation", "shift", "associative"."""
    f = mymath.positional.online_softmax if func is None else func
    mg = mymath.positional.merge_softmax_states if merge is None else merge
    chk = failed_checks_21 if checks is None else checks
    counts = {"blocks": 0, "permutation": 0, "shift": 0, "associative": 0}
    for _ in range(n_trials):
        n = int(rng.integers(3, 13))
        scores = rng.normal(0, 3, n)
        if rng.random() < 0.3:
            scores[rng.random(n) < 0.25] = -np.inf
            scores[int(rng.integers(n))] = float(rng.normal(0, 3))
        values = rng.normal(0, 1, (n, 2))
        block_size = int(rng.integers(1, n + 1))
        perm = rng.permutation(n)
        shift = float(rng.normal(0, 20))
        i, j = (int(c) for c in sorted(rng.choice(np.arange(1, n), 2, replace=False)))
        names = chk(scores, values, block_size, perm, shift, (i, j), f, mg, rtol)
        if not isinstance(names, (set, frozenset, list, tuple)):     # None: shown by wbm.attempt as one ❌ line
            raise TypeError(f"failed_checks_21 doit rendre un ensemble de noms (set() si tout passe), reçu un objet de "
                            f"type {type(names).__name__!r} : as-tu oublié le return ?")
        for name in names:
            if name not in counts:
                raise ValueError(f"les contrôles rendent {name!r} : les noms sont 'blocks', 'permutation', 'shift' et "
                                 "'associative'")
            counts[name] += 1
    return counts'''

SOLUTION_21 = '''def failed_checks_21(scores, values, block_size, perm, shift, cuts, func, merge, rtol=1e-9):
    """The set of the names of the checks that fail, among "blocks", "permutation", "shift" and "associative" (set() when
    all pass); func and merge are the functions tested."""
    try:
        ref = func(scores, values, block_size=1)
        failed = set()
        if differ_21(func(scores, values, block_size=block_size), ref, rtol):
            failed.add("blocks")
        if differ_21(func(scores[perm], values[perm], block_size=1), ref, rtol):
            failed.add("permutation")
        m, l, acc = ref
        if differ_21(func(scores + shift, values, block_size=1), (m + shift, l, acc), rtol):
            failed.add("shift")
        i, j = cuts
        A, B, C = (func(scores[a:b], values[a:b], block_size=1) for a, b in ((0, i), (i, j), (j, len(scores))))
        if differ_21(merge(merge(A, B), C), merge(A, merge(B, C)), rtol):
            failed.add("associative")
        return failed
    except Exception:  # noqa: BLE001 - an exception of the functions tested fails the four checks
        return {"blocks", "permutation", "shift", "associative"}'''

CHECK_21 = '''OS_C21, MERGE_C21 = ref_pos.online_softmax, ref_pos.merge_softmax_states   # captured: never a function replaced later


def col2_c21(scores, values=None, block_size=1, history=False):
    """WRONG for values of two columns or more: the columns after the first are never rescaled."""
    s, v = np.asarray(scores, dtype=float), np.asarray(values, dtype=float)
    m, l, acc = -math.inf, 0.0, np.zeros(v.shape[1:])
    for start in range(0, len(s), block_size):
        block = s[start:start + block_size]
        if np.all(np.isneginf(block)):
            continue
        m_new = max(m, float(block.max()))
        f, w = math.exp(m - m_new), np.exp(block - m_new)
        l = l * f + float(w.sum())
        acc = acc * np.where(np.arange(acc.size) == 0, f, 1.0) + w @ v[start:start + block_size]
        m = m_new
    return m, l, acc


class AllMaskedError_c21(ValueError):
    """The error of minf_raises_c21."""


def minf_raises_c21(scores, values=None, block_size=1, history=False):
    """WRONG: an error when every score is -inf (the empty state is not returned)."""
    if np.all(np.isneginf(np.asarray(scores, dtype=float))):
        raise AllMaskedError_c21("aucun score fini")
    return OS_C21(scores, values, block_size=block_size)


def scaled_m_c21(scores, values=None, block_size=1, history=False):
    """WRONG: m returned multiplied by 1.001 (l and acc right)."""
    m, l, acc = OS_C21(scores, values, block_size=block_size)
    return m * 1.001, l, acc


def drop_tail_c21(scores, values=None, block_size=1, history=False):
    """WRONG: the last block is forgotten when it is shorter than block_size."""
    s = np.asarray(scores, dtype=float)
    keep = len(s) - len(s) % block_size or len(s)
    return OS_C21(s[:keep], None if values is None else np.asarray(values)[:keep], block_size=block_size)


def merge_left_c21(state1, state2):
    """WRONG: only the first state is rescaled to the common maximum."""
    m = max(state1[0], state2[0])
    if m == -math.inf:
        return state1
    f1 = math.exp(state1[0] - m)
    return m, state1[1] * f1 + state2[1], np.asarray(state1[2], dtype=float) * f1 + np.asarray(state2[2], dtype=float)


def merge_first_c21(state1, state2):
    """WRONG, but associative: the first state that is not empty, the other one ignored."""
    return state1 if state1[0] > -math.inf else state2


BROKEN_C21 = {"col2_c21": ("func", ("blocks", "permutation")), "minf_raises_c21": ("func", ("blocks", "permutation", "shift", "associative")),
              "scaled_m_c21": ("func", ("shift",)), "drop_tail_c21": ("func", ("blocks",)),
              "merge_left_c21": ("merge", ("associative",)), "merge_first_c21": ("merge", ())}   # role, properties broken
HIDDEN_C21 = __HIDDEN_C21__   # two hidden starts, and the sub-IDs of the counters expected for each version

with checked("MB3.21"):
    results_21 = []
    report_21 = reporter(results_21, stop=False)
    N_C21 = 40
    PROPERTIES_C21 = {"blocks": "l'état lu par blocs de block_size comparé à ref",
                      "permutation": "l'état des scores et des valeurs permutés par perm comparé à ref",
                      "shift": "l'état de scores + shift comparé à (m + shift, l, acc)",
                      "associative": "merge(merge(A, B), C) comparé à merge(A, merge(B, C))"}

    def run_c21(label, seed, **kwargs):
        """The loop of the notebook with your failed_checks_21, on a hidden start: its counters."""
        try:
            return softmax_property_test_21(N_C21, np.random.default_rng(seed), checks=failed_checks_21, **kwargs)
        except (NotImplementedError, MymathMissingError):
            raise
        except Exception as exc:  # noqa: BLE001 - the learner's error
            hint = (" ; failed_checks_21 doit rendre un ensemble de noms (set() si tout passe) : as-tu oublié le return ?"
                    if isinstance(exc, TypeError) and "NoneType" in str(exc) and "return" not in str(exc) else
                    " ; c'est la fonction testée qui lève : une exception de func ou de merge doit faire échouer les quatre "
                    "contrôles (appelle-les dans un try)" if isinstance(exc, AllMaskedError_c21) else "")
            print(f"❌ Ex MB3.21 : failed_checks_21 ({label}) lève {type(exc).__name__} : {str(exc)[:200]}{hint}")
            raise StopCheck from None

    def compare_c21(label, got, version, ids):
        """One ✅ when the four counters are those expected; else one ❌ per counter, naming the property."""
        wrong = []
        for key in ("blocks", "permutation", "shift", "associative"):
            if version is None or key not in BROKEN_C21[version][1]:            # 0 by construction
                if got[key] != 0:
                    wrong.append((key, f"vaut {got[key]}, attendu 0 : "
                                       + ("avec des fonctions justes, aucun contrôle ne compte : ton contrôle compte trop "
                                          "(ce qu'il compare, et à quoi)" if version is None else
                                          "cette version ne fausse pas cette propriété : ton contrôle compte trop (ce "
                                          "qu'il compare, et à quoi)")))
            elif not passes(ids[key], got[key]):
                wrong.append((key, ("vaut 0 : tes contrôles ne vérifient pas " + PROPERTIES_C21[key]
                                    + ", avec les fonctions reçues (func et merge, pas celles de mymath)") if got[key] == 0
                                   else (f"vaut {got[key]}, ce n'est pas le compte attendu : relis ce que ce contrôle "
                                         "compare, et avec quels blocs")))
        if not wrong:
            report_21(True, f"{label} : les quatre compteurs comme attendu", "")
        for key, why in wrong:
            report_21(False, "", f"{label} : le compteur {key!r} {why}")

    for start_c21, (seed_c21, ids_c21) in enumerate(HIDDEN_C21, start=1):
        compare_c21(f"les fonctions justes, départ caché {start_c21}",
                    run_c21("les fonctions justes", seed_c21, func=OS_C21, merge=MERGE_C21), None, {})
        for number_c21, (name_c21, (role_c21, _)) in enumerate(BROKEN_C21.items(), start=1):
            label_c21 = f"une version fausse cachée n° {number_c21}, départ caché {start_c21}"
            functions_c21 = {"func": OS_C21, "merge": MERGE_C21, role_c21: globals()[name_c21]}
            compare_c21(label_c21, run_c21(label_c21, seed_c21, **functions_c21), name_c21, ids_c21[name_c21])
    learner_c21 = (mymath.positional.online_softmax, mymath.positional.merge_softmax_states)   # put back even on failure
    try:
        mymath.positional.online_softmax, mymath.positional.merge_softmax_states = col2_c21, MERGE_C21
        got_c21 = run_c21("func=None", HIDDEN_C21[0][0])
    finally:
        mymath.positional.online_softmax, mymath.positional.merge_softmax_states = learner_c21
    compare_c21("la version fausse n° 1 mise un instant à la place de mymath.positional.online_softmax, sans func", got_c21,
                "col2_c21", HIDDEN_C21[0][1]["col2_c21"])
    verdict("MB3.21", all(results_21), "tes contrôles comptent juste sur les fonctions justes et sur les versions fausses "
            "cachées.", "relis les lignes ❌ ci-dessus.")'''

NOTE_21 = (r"`failed_checks_21` : un `try` autour des appels, `ref = func(scores, values, block_size=1)`, puis les quatre "
           r"contrôles par `differ_21`. a) Vrai. b) `rescale_l_only` : (126, 191, 0, 0) ; `centered` : (0, 0, 200, 0) ; "
           r"`merge_no_rescale` : (0, 0, 0, 0) ; `merge_mean` : (0, 0, 0, 199). c) `merge_no_rescale` passe tout : "
           r"additionner sans remettre à l'échelle est associatif, mais faux, et ce sont les tests de "
           r"`tests/test_mb3_positional.py` qui l'attrapent. La vérification lance ton test avec les fonctions justes et "
           r"six versions fausses cachées, dont une qui lève une erreur sur des scores tous égaux à $-\infty$, une qui se "
           r"trompe seulement sur les valeurs 2-D, et une fusion fausse mais associative.")

MB3_21 = Ex(
    "MB3.21", "🛠️", 1, 25, "Un test de propriété : la softmax en ligne ne dépend ni de la taille des blocs, ni d'une même "
    "permutation des scores et des valeurs, ni d'une constante ajoutée aux scores, et la fusion de trois états est "
    "associative",
    "écrire les contrôles d'un test de propriété de la softmax en ligne et de la fusion, sur des cas tirés au hasard, et "
    "voir ce qu'il attrape et ce qu'il ne peut pas attraper.", "fiche §8 ; Ex MB3.15 et MB3.16", tracks="C",
    given=GIVEN_21, note=NOTE_21,
    body=r"""La cellule fournie donne la boucle du test, `softmax_property_test_21(n_trials, rng, func=None, merge=None, rtol=1e-9, checks=None)` : quand `func` vaut `None`, elle prend `mymath.positional.online_softmax` **au moment de l'appel**, quand `merge` vaut `None`, `mymath.positional.merge_softmax_states`, et, quand `checks` vaut `None`, ta fonction `failed_checks_21`. Pour chacun des `n_trials` essais, dans cet ordre, elle tire `n = int(rng.integers(3, 13))`, `scores = rng.normal(0, 3, n)`, puis, si `rng.random() < 0.3`, met à $-\infty$ les scores où `rng.random(n) < 0.25` et redonne au score d'indice `int(rng.integers(n))` la valeur `float(rng.normal(0, 3))` ; puis `values = rng.normal(0, 1, (n, 2))`, `block_size = int(rng.integers(1, n + 1))`, `perm = rng.permutation(n)`, `shift = float(rng.normal(0, 20))` et deux coupures `i < j` tirées par `sorted(rng.choice(np.arange(1, n), 2, replace=False))` ; elle appelle `checks(scores, values, block_size, perm, shift, (i, j), f, m, rtol)`, où `f` et `m` sont les fonctions testées, et ajoute 1 au compteur de chaque nom rendu ; elle rend le dictionnaire des quatre compteurs `"blocks"`, `"permutation"`, `"shift"` et `"associative"`.

Écris les contrôles, `failed_checks_21(scores, values, block_size, perm, shift, cuts, func, merge, rtol=1e-9)`, qui rend l'**ensemble** des noms des contrôles qui échouent (`set()` si tout passe), avec `ref = func(scores, values, block_size=1)` :
- `"blocks"` échoue si l'état lu par blocs de `block_size` diffère de `ref` ;
- `"permutation"`, si l'état de `scores[perm]` et `values[perm]`, lu par blocs de 1, diffère de `ref` ;
- `"shift"`, si l'état de `scores + shift`, lu par blocs de 1, diffère de $(m + \text{shift}, l, a)$, où $(m, l, a)$ = `ref` ;
- `"associative"`, si, avec les états des trois morceaux `scores[:i]`, `scores[i:j]` et `scores[j:]` (et de leurs valeurs), lus par `func` avec des blocs de 1, `merge(merge(A, B), C)` diffère de `merge(A, merge(B, C))`.

Pour dire si deux états « diffèrent », sers-toi de la fonction fournie `differ_21(state1, state2, rtol)` : elle rend `True` si leurs $m$ ne sont pas tous deux $-\infty$ et s'écartent de plus de $\texttt{rtol}\cdot\max(1, \lvert m\rvert)$, si leurs $l$ s'écartent de plus de $\texttt{rtol}\cdot\max(1, l)$, ou si leurs accumulateurs ne sont pas égaux par `np.allclose(rtol=rtol, atol=rtol * max(1, abs(acc).max()))`. Une exception levée par `func` ou `merge` fait échouer les quatre contrôles. La cellule fournie donne aussi quatre versions fausses : `rescale_l_only` (la softmax en ligne du 🐛 MB3.20), `centered` (une softmax en ligne qui retranche d'abord aux scores la moyenne des scores finis), `merge_no_rescale` (une fusion qui additionne les $l$ et les accumulateurs sans les remettre à l'échelle) et `merge_mean` (une fusion qui fait la moyenne des deux états remis à l'échelle au lieu de leur somme). Puis :
- a) avec `rng = np.random.default_rng(7321)` et 200 essais, avec tes fonctions `online_softmax` et `merge_softmax_states` et tes contrôles : vrai ou faux, les quatre compteurs sont nuls ;
- b) avec le même départ (un nouveau `default_rng(7321)` chaque fois, 200 essais) et chacune des quatre versions fausses, dans l'ordre `rescale_l_only`, `centered` (pour `func`), `merge_no_rescale`, `merge_mean` (pour `merge`) : les quatre compteurs, dans l'ordre `"blocks"`, `"permutation"`, `"shift"`, `"associative"` (une liste de 4 listes de 4 entiers) ;
- c) dans ta copie : lesquelles passent un contrôle, ou tous, et pourquoi c'est normal ; qu'est-ce qui, dans le dépôt, vérifie ce qu'elles ont de faux ?

La vérification lance aussi ton test sur deux départs cachés de 40 essais, avec les fonctions justes (compteurs nuls) et avec six versions fausses cachées, qui faussent chacune une ou plusieurs des propriétés, ou aucune : l'une d'elles lève une erreur sur des scores tous égaux à $-\infty$, une autre se trompe seulement sur les valeurs 2-D ; elle remplace aussi un instant `mymath.positional.online_softmax` par l'une d'elles, pour l'appel sans `func`. Ce qu'il faut retenir : chaque contrôle attrape certaines erreurs et en laisse passer d'autres ; un test se juge aux erreurs qu'il attrape, et à celles qu'il ne peut pas attraper.""",
    todo='''def failed_checks_21(scores, values, block_size, perm, shift, cuts, func, merge, rtol=1e-9):
    """The set of the names of the checks that fail, among "blocks", "permutation", "shift" and "associative" (set() when
    all pass); func and merge are the functions tested."""
    raise NotImplementedError("failed_checks_21 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB3_21a = answer_MB3_21b = ...
with wbm.attempt("MB3.21"):          # your checks and your library: ⏳ while they are not written
    answer_MB3_21a = ...  # a) True or False: the four counters are 0 (default_rng(7321), 200 trials, your functions, your checks)
    answer_MB3_21b = ...  # b) a list of 4 lists of 4 integers: the counters for rescale_l_only, centered, merge_no_rescale, merge_mean''',
    check=answers_check("MB3.21", "ab") + "\n\n" + CHECK_21,
    solution=SOLUTION_21 + '''


KEYS_21 = ("blocks", "permutation", "shift", "associative")
with np.errstate(over="ignore", invalid="ignore"):
    mine_21 = softmax_property_test_21(200, np.random.default_rng(7321))
    wrong_21 = {name: softmax_property_test_21(200, np.random.default_rng(7321), **{role: function})
                for name, role, function in (("rescale_l_only", "func", rescale_l_only), ("centered", "func", centered),
                                             ("merge_no_rescale", "merge", merge_no_rescale),
                                             ("merge_mean", "merge", merge_mean))}
answer_MB3_21a = all(mine_21[key] == 0 for key in KEYS_21)
answer_MB3_21b = [[counts[key] for key in KEYS_21] for counts in wrong_21.values()]
for name_21, counts_21 in {"tes fonctions": mine_21, **wrong_21}.items():
    print(f"{name_21:17s}", counts_21)
print("a)", answer_MB3_21a, " b)", answer_MB3_21b)''',
    record='''def counters_21r(seed, func, merge, n_trials=200, variant="right"):
    """The loop and the checks of the statement written again (the oracle), with classic variants of the checks:
    "no shift" (ref compared without adding shift to m), "against ref" (merge(merge(A, B), C) compared with ref),
    "one try each" (an exception fails only the check where it happens)."""
    def close(s1, s2):
        (m1, l1, a1), (m2, l2, a2) = s1, s2
        if not (m1 == -math.inf and m2 == -math.inf) and not abs(m1 - m2) <= 1e-9 * max(1.0, abs(m1)):
            return False
        a1, a2 = np.atleast_1d(np.asarray(a1, dtype=float)), np.atleast_1d(np.asarray(a2, dtype=float))
        return (abs(l1 - l2) <= 1e-9 * max(1.0, abs(l1)) and a1.shape == a2.shape
                and bool(np.allclose(a1, a2, rtol=1e-9, atol=1e-9 * max(1.0, float(np.abs(a1).max())))))

    rng, counts = np.random.default_rng(seed), [0, 0, 0, 0]
    for _ in range(n_trials):
        n = int(rng.integers(3, 13))
        s = rng.normal(0, 3, n)
        if rng.random() < 0.3:
            s[rng.random(n) < 0.25] = -np.inf
            s[int(rng.integers(n))] = float(rng.normal(0, 3))
        v = rng.normal(0, 1, (n, 2))
        size = int(rng.integers(1, n + 1))
        perm = rng.permutation(n)
        shift = float(rng.normal(0, 20))
        i, j = (int(c) for c in sorted(rng.choice(np.arange(1, n), 2, replace=False)))
        tests = [lambda: not close(func(s, v, block_size=size), func(s, v, block_size=1)),
                 lambda: not close(func(s[perm], v[perm], block_size=1), func(s, v, block_size=1)),
                 lambda: not close(func(s + shift, v, block_size=1),
                                   (lambda m, l, a: (m + (0.0 if variant == "no shift" else shift), l, a))(
                                       *func(s, v, block_size=1))),
                 lambda: not close(merge(merge(*(func(s[a:b], v[a:b], block_size=1) for a, b in ((0, i), (i, j)))),
                                         func(s[j:], v[j:], block_size=1)),
                                   func(s, v, block_size=1) if variant == "against ref" else
                                   merge(func(s[:i], v[:i], block_size=1),
                                         merge(*(func(s[a:b], v[a:b], block_size=1) for a, b in ((i, j), (j, n))))))]
        if variant == "one try each":
            outcome = []
            for test in tests:
                try:
                    outcome.append(test())
                except Exception:  # noqa: BLE001
                    outcome.append(True)
        else:
            try:
                outcome = [test() for test in tests]
            except Exception:  # noqa: BLE001 - an exception fails the four checks
                outcome = [True] * 4
        counts = [c + bool(o) for c, o in zip(counts, outcome)]
    return counts


os_21r, merge_21r = mymath.positional.online_softmax, mymath.positional.merge_softmax_states   # the reference here
versions_21r = [(rescale_l_only, merge_21r), (centered, merge_21r), (os_21r, merge_no_rescale), (os_21r, merge_mean)]
with np.errstate(over="ignore", invalid="ignore"):
    right_21r = [counters_21r(7321, f, m) for f, m in versions_21r]
    wbm.record("MB3.21a", all(c == 0 for c in counters_21r(7321, os_21r, merge_21r)),
               mistakes={"avec des fonctions justes, aucun contrôle ne doit compter : relis ce que compare chacun, et à "
                         "quoi (le contrôle « shift » ajoute shift à m)": False})
    mistakes_21r, seen_21r = {}, [right_21r]
    for message_21r, variant_21r in (("le contrôle « shift » compare à (m + shift, l, acc) : ajouter une constante aux "
                                      "scores déplace m, et ne change ni l ni acc", "no shift"),
                                     ("le contrôle « associative » compare deux groupements, merge(merge(A, B), C) et "
                                      "merge(A, merge(B, C)), pas l'un d'eux à ref", "against ref"),
                                     ("une exception levée fait échouer les quatre contrôles, pas seulement celui où elle "
                                      "arrive", "one try each")):
        counts_21r = [counters_21r(7321, f, m, variant=variant_21r) for f, m in versions_21r]
        if counts_21r not in seen_21r:
            mistakes_21r[message_21r] = counts_21r
            seen_21r.append(counts_21r)
    if right_21r[::-1] not in seen_21r:
        mistakes_21r["l'ordre des versions : rescale_l_only, centered, merge_no_rescale, merge_mean"] = right_21r[::-1]
    wbm.record("MB3.21b", right_21r, mistakes=mistakes_21r)'''
    + '''
for seed_21r, ids_21r in __HIDDEN_C21__:                    # the counters of the hidden versions, on the hidden starts
    for version_21r, keys_21r in ids_21r.items():
        for key_21r, sub_id_21r in keys_21r.items():
            wbm.record(sub_id_21r, __COUNTERS_C21__[sub_id_21r])''',
    after=[
        ("solution", answers_check("MB3.21", "ab") + "\n\n" + CHECK_21),
    ],
)

PART_C = Part("C", "Déboguer, tester",
              "Fiche §3, §4 et §8. Trois erreurs classiques à corriger ; un test de propriété de la softmax en ligne et de "
              "la fusion.", exercises=[MB3_20, MB3_21])
