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
