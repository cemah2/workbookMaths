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
