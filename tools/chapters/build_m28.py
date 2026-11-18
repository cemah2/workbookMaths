#!/usr/bin/env python
"""Build the two notebooks of chapter M28 from a single source (used by Claude).

    python tools/chapters/build_m28.py
    python tools/run_all_notebooks.py chapitres/m28_gram_echantillonnage/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m28_gram_echantillonnage/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M28.1 to M28.7 and 🔗 M28.11), each answer computed in the notebook from the data of
its statement (exact fractions where the calculation is exact; math, NumPy and SciPy otherwise), each wrong value computed
by the error its message names; parts A to D are the notebook exercises (M28.13 to M28.19), exactly as 02_exercices.md
describes them. Wrong-answer messages state a rule, never a number of the answer, the last step that gives it, nor another
sub-question.

Data. The notebook exercises take the data of the paper exercises (a data cell of part A: the beacons of M28.1, the
rhombus of M28.2, the forecast of M28.6), the settings of their own statements and their own random draws. Seeds 6601 to
6649 only (the tests use 6500 to 6590, the figures of the fiche 6591 to 6599): 6618 (🛠️ M28.18) and 6619 (the region of
🏆 M28.19) in the statements; 6627 (the hidden clouds of 🐛 M28.17), and 6642, 6644, 6649 (the three hidden regions of
M28.19, renumbered, turned and moved at each run) in the check cells. The other hidden cases are drawn without a seed at
each run (the starts of the property test of M28.18, the transformations of M28.19), or written in their cell (the hidden
start of 🔮 M28.15, the hidden motifs of 🎨 M28.16, the hidden cases of M28.17), computed at build time by private
functions of this script: none is the answer of a question. The check cells never hold the code that solves an exercise
nor a value that gives an answer without a calculation: the expected values are computed by the reference implementation
at check time (``ref_sampling``), compared with ``wbm.check(..., computed=True)``, given by properties (distances, the
optimality conditions on a box, the counters of a wrong version built to break one property at every trial), or written
for hidden cases only. They use their own data, never the test cases of tests/test_m28_sampling.py, the examples of the
docstrings of the stub sampling, the examples of the fiche, nor the numbers of workbookIA 28, B4 and its checkpoint VI (the
notes of M28 in the syllabus and their list « Évités »).
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import math
import pprint
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (ROOT, STARS, Ex, Paper, Part, badge, check_unique_keys, guarded,  # noqa: E402,F401
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M28"
FOLDER = "chapitres/m28_gram_echantillonnage"

BOOL = "True or False"


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M28.1", "Quatre points du plan : leur matrice de Gram 4 × 4, leur matrice des moments d'ordre 2, et les "
                   "distances lues dans la Gram", [
        ("a", "a 4 × 4 matrix, as the list of its rows (m²)", "floats(X_1 @ X_1.T)",
         '''decimals=6,
           mistakes={"G = XXᵀ contient les produits scalaires des lignes de X (les points) ; XᵀX est la matrice des "
                     "colonnes": floats(X_1.T @ X_1),
                     "G_ij est le produit scalaire des points i et j, pas le carré de leur distance": floats(sq_dists(X_1))}'''),
        ("b", "a 2 × 2 matrix, as the list of its rows (m²)", "floats(X_1.T @ X_1 / len(X_1))",
         '''decimals=6,
           mistakes={"on divise par le nombre d'échantillons (les points), pas par le nombre de coordonnées":
                         floats(X_1.T @ X_1 / X_1.shape[1]),
                     "sans division par le nombre d'échantillons, la somme des produits n'est pas une moyenne":
                         floats(X_1.T @ X_1),
                     "les points sont en lignes : la matrice des moments de leurs coordonnées a la forme (2, 2)":
                         floats(X_1 @ X_1.T / len(X_1))}'''),
        ("c", "a list of 2 numbers, in decreasing order", "nonzero_desc(X_1 @ X_1.T)",
         '''decimals=6,
           mistakes={"les valeurs propres demandées sont celles de G, pas celles de la matrice des moments":
                         nonzero_desc(X_1.T @ X_1 / len(X_1)),
                     "par ordre décroissant": nonzero_desc(X_1 @ X_1.T)[::-1]}'''),
        ("d", "a list of 3 numbers (m²)", "from_point_0(lambda gii, gjj, gij: gii + gjj - 2 * gij)",
         '''decimals=6,
           mistakes={"le terme croisé de ‖xᵢ − xⱼ‖² apparaît deux fois dans le développement":
                         from_point_0(lambda gii, gjj, gij: gii + gjj - gij),
                     "dans ‖xᵢ − xⱼ‖², le terme croisé se retranche": from_point_0(lambda gii, gjj, gij: gii + gjj + 2 * gij),
                     "la question demande les carrés des distances, pas les distances":
                         [math.sqrt(v) for v in from_point_0(lambda gii, gjj, gij: gii + gjj - 2 * gij)]}'''),
        ("e", "a number (1 decimal), in degrees", "math.degrees(math.acos(G_1[0][1] / math.sqrt(G_1[0][0] * G_1[1][1])))",
         '''decimals=1,
           mistakes={"l'angle est demandé en degrés": math.acos(G_1[0][1] / math.sqrt(G_1[0][0] * G_1[1][1])),
                     "le cosinus divise G₁₂ par le produit des deux normes, pas par leur somme":
                         math.degrees(math.acos(G_1[0][1] / (G_1[0][0] + G_1[1][1]))),
                     "l'angle entre deux vecteurs se lit dans leur produit scalaire, pas dans le carré de leur distance":
                         math.degrees(math.acos((G_1[0][0] + G_1[1][1] - 2 * G_1[0][1]) / math.sqrt(G_1[0][0] * G_1[1][1])))}'''),
    ]),

    Paper("M28.2", "Quatre villes aux sommets d'un losange : le double centrage des carrés des distances, puis une carte "
                   "à une isométrie près", [
        ("a", "a number (km²)", "float(D2_2.mean())",
         '''decimals=6,
           mistakes={"s est la moyenne des n² coefficients de D⁽²⁾, diagonale comprise": float(D2_2.sum() / (4 * 3)),
                     "le double centrage porte sur les carrés des distances, pas sur les distances": float(D_2.mean())}'''),
        ("b", "a 4 × 4 matrix, as the list of its rows (km²)", "floats(double_centering(D2_2))",
         '''decimals=6,
           mistakes={"le double centrage se fait sur les carrés des distances": floats(double_centering(D_2)),
                     "G = −½ J D⁽²⁾ J : sans le facteur −½, sa diagonale serait négative":
                         floats(-2 * double_centering(D2_2))}'''),
        ("c", "a list of 4 numbers, in decreasing order", "eigen_desc(double_centering(D2_2))",
         '''decimals=6,
           mistakes={"les valeurs propres d'une matrice symétrique ne sont pas ses coefficients diagonaux":
                         sorted(np.diag(double_centering(D2_2)).tolist(), reverse=True),
                     "par ordre décroissant": eigen_desc(double_centering(D2_2))[::-1]}'''),
        ("d", "a 4 × 2 matrix, as the list of its rows (km)", "floats(spectral_map(double_centering(D2_2)))",
         '''decimals=6,
           mistakes={"la colonne k est √λ_k fois le vecteur propre unitaire : pense à la racine":
                         floats(spectral_map(double_centering(D2_2), root=False)),
                     "les colonnes viennent par valeur propre décroissante":
                         floats(spectral_map(double_centering(D2_2))[:, ::-1]),
                     "dans chaque colonne, la première coordonnée non nulle est positive":
                         floats(-spectral_map(double_centering(D2_2)))}'''),
        ("e", BOOL, "bool(min(eigen_desc(double_centering(D2_2E))) >= -1e-9)",
         '''mistakes={"respecter l'inégalité triangulaire ne suffit pas pour être des distances euclidiennes": True}'''),
    ]),

    Paper("M28.3", "Régler quatre émetteurs entre 0 et 1 : le maximum d'une réponse linéaire sur la boule et sur le pavé, "
                   "d'une énergie quadratique sur la sphère, et deux pas de montée projetée", [
        ("a", "a number", "float(np.linalg.norm(W_3))",
         '''decimals=6,
           mistakes={"le maximum est ‖w‖, une racine : pas ‖w‖²": float(W_3 @ W_3),
                     "sur la boule, toutes les coordonnées comptent, celles de poids négatif aussi":
                         float(np.linalg.norm(np.clip(W_3, 0, None)))}'''),
        ("b", "a list of 4 numbers", "floats(BEST_3)",
         '''decimals=6,
           mistakes={"le maximum sur le pavé n'est pas la projection du maximum sur la boule":
                         floats(np.clip(W_3 / np.linalg.norm(W_3), 0, 1)),
                     "une coordonnée de poids négatif fait baisser la réponse": [1.0, 1.0, 1.0, 1.0]}'''),
        ("c", "an integer", "first_step_3(lambda x, previous: np.array_equal(x, BEST_3))",
         '''mistakes={"après un pas, toutes les coordonnées ne sont pas encore à leur borne":
                         first_step_3(lambda x, previous: bool(np.any(x == BEST_3))),
                     "un pas projeté qui dépasse une borne s'arrête sur elle : il ne faut pas attendre un pas de plus":
                         first_step_3(lambda x, previous: np.array_equal(x, previous))}'''),
        ("d", "a number", "float(np.max(GAP_3 / np.abs(W_3)))",
         '''decimals=6,
           mistakes={"avec un pas trop court, au moins une coordonnée reste loin de sa borne":
                         float(np.min(GAP_3 / np.abs(W_3))),
                     "la distance de xᵢ à sa borne se divise par |wᵢ| pour donner le pas": float(np.max(GAP_3 * np.abs(W_3)))}'''),
        ("e", "a number", "float(np.linalg.eigvalsh(A_3).max())",
         '''decimals=6,
           mistakes={"le maximum sur la sphère est une valeur propre, pas un coefficient diagonal": float(np.diag(A_3).max()),
                     "le maximum sur la sphère est une seule valeur propre, pas leur somme":
                         float(np.linalg.eigvalsh(A_3).sum())}'''),
        ("f", "a number", "max(float(v @ A_3 @ v) for v in VERTICES_3)",
         '''decimals=6,
           mistakes={"le sommet (1, 1, 1, 1) n'est pas forcément le meilleur": float(np.ones(4) @ A_3 @ np.ones(4)),
                     "λ_max‖x‖² majore xᵀAx, mais cette borne n'est pas atteinte sur le pavé":
                         float(np.linalg.eigvalsh(A_3).max() * 4)}'''),
    ]),

    Paper("M28.4", "Les températures le long d'une barre : la variation totale xᵀLx, son gradient 2Lx, un pas de lissage, "
                   "et une marche étalée sur n pas, au carré ou en valeur absolue", [
        ("a", "a number (°C²)", "float(X_4 @ L_4 @ X_4)",
         '''decimals=6,
           mistakes={"la variation totale additionne des carrés, pas des valeurs absolues": float(np.abs(np.diff(X_4)).sum()),
                     "la barre a deux bouts libres : la case 4 n'est pas voisine de la case 0":
                         float(X_4 @ RING_4 @ X_4)}'''),
        ("b", "a list of 5 numbers", "floats(2 * L_4 @ X_4)",
         '''decimals=6,
           mistakes={"le gradient de xᵀLx est 2Lx, pas Lx": floats(L_4 @ X_4),
                     "aux deux bouts, une case n'a qu'une voisine": floats(2 * RING_4 @ X_4)}'''),
        ("c", "a list of 5 numbers (°C)", "floats(X_4 - ETA_4 * 2 * L_4 @ X_4)",
         '''decimals=6,
           mistakes={"on descend : on retire le pas": floats(X_4 + ETA_4 * 2 * L_4 @ X_4),
                     "le pas est η fois le gradient 2Lx": floats(X_4 - ETA_4 * L_4 @ X_4)}'''),
        ("d", "a number (2 decimals) (°C²)", "tv_4(X_4 - ETA_4 * 2 * L_4 @ X_4)",
         '''decimals=2,
           mistakes={"la variation totale additionne des carrés, pas des valeurs absolues":
                         float(np.abs(np.diff(X_4 - ETA_4 * 2 * L_4 @ X_4)).sum()),
                     "le pas est η fois le gradient 2Lx": tv_4(X_4 - ETA_4 * L_4 @ X_4)}'''),
        ("e", "a number (4 decimals)", "1 / max(4 * math.sin(k * math.pi / (2 * 5)) ** 2 for k in range(5))",
         '''decimals=4,
           mistakes={"le pas critique de M19 se calcule avec la hessienne de VT, qui n'est pas L":
                         2 / max(4 * math.sin(k * math.pi / (2 * 5)) ** 2 for k in range(5)),
                     "la borne λ_max ≤ 4 donne un pas sûr, pas le pas critique": 1 / 4}'''),
        ("f", "a list of 2 numbers: squared, then absolute value", "[H_4 ** 2 / N_4, abs(H_4)]",
         '''decimals=6,
           mistakes={"chacune des n différences vaut h/n": [N_4 * H_4 ** 2, abs(H_4)],
                     "la liste donne d'abord la variation totale au carré, puis en valeur absolue": [abs(H_4), H_4 ** 2 / N_4]}'''),
        ("g", "an integer", "next(n for n in itertools.count(1) if H_4 ** 2 / n < 1)",
         '''mistakes={"moins de 1 : une inégalité stricte": next(n for n in itertools.count(1) if H_4 ** 2 / n <= 1),
                     "au carré, chaque différence compte par son carré": next(n for n in itertools.count(1) if abs(H_4) / n < 1)}'''),
    ]),

    Paper("M28.5", "Des étoffes rayées : période, fréquence, fréquence de Nyquist, repliement, variation totale rapportée à "
                   "l'énergie 4 sin²(ω/2), et gain d'une moyenne mobile", [
        ("a", "a list of 2 numbers (3 decimals)", "[ring_ratio(MOTIF_A_5), ring_ratio(MOTIF_B_5)]",
         '''decimals=3,
           mistakes={"4 sin²(ω/2) attend ω = 2πf, en radians par case, pas f en cycles par case":
                         [4 * math.sin(f / 2) ** 2 for f in (1 / 6, 1 / 12)],
                     "c'est le carré du sinus de la moitié de ω": [4 * math.sin(2 * math.pi * f) ** 2 for f in (1 / 6, 1 / 12)]}'''),
        ("b", "a list of 2 numbers (4 decimals)", "[ring_gain_rows(MOTIF_A_5), ring_gain_rows(MOTIF_B_5)]",
         '''decimals=4,
           mistakes={"la moyenne mobile pèse 1/3 sur chacune des trois cases, pas 1/2 sur deux":
                         [(1 + math.cos(2 * math.pi * f)) / 2 for f in (1 / 6, 1 / 12)],
                     "cos ω attend ω en radians par case": [(1 + 2 * math.cos(f)) / 3 for f in (1 / 6, 1 / 12)]}'''),
        ("c", "a number (2 decimals), in cells", "1 / math.hypot(*FREQ_C_5)",
         '''decimals=2,
           mistakes={"en dimension 2, la période n'est pas la somme des périodes le long des axes":
                         1 / FREQ_C_5[0] + 1 / FREQ_C_5[1],
                     "la période ne s'obtient pas à partir de la somme f₁ + f₂": 1 / (FREQ_C_5[0] + FREQ_C_5[1])}'''),
        ("d", "a number (3 decimals)", "ring_ratio(MOTIF_C_5)",
         '''decimals=3,
           mistakes={"la formule de dimension 1, appliquée à la fréquence prise dans la direction des rayures, ne donne "
                     "pas la variation totale d'une grille": 4 * math.sin(math.pi * math.hypot(*FREQ_C_5)) ** 2,
                     "le motif C varie aussi le long des colonnes": ring_ratio(np.cos(2 * np.pi * FREQ_C_5[1] * JJ_5))}'''),
        ("e", "a number (3 decimals)", "ring_blur(MOTIF_C_5)",
         '''decimals=3,
           mistakes={"le gain du flou 3 × 3 n'est pas la moyenne des gains des deux directions":
                         (gain_1d(FREQ_C_5[0]) + gain_1d(FREQ_C_5[1])) / 2,
                     "le flou 3 × 3 agit aussi le long des colonnes": gain_1d(FREQ_C_5[1])}'''),
        ("f", "a number, in cells", "1 / min(F_5 % 1, 1 - F_5 % 1)",
         '''decimals=6,
           mistakes={"un motif relevé une fois par case n'a jamais une période de moins de 2 cases : replie d'abord la "
                     "fréquence": 1 / F_5,
                     "la question demande une période, en cases, pas une fréquence": min(F_5 % 1, 1 - F_5 % 1)}'''),
    ]),

    Paper("M28.6", "La prévision d'un météorologue en six catégories : la refroidir, garder les trois plus probables, "
                   "garder le plus petit ensemble de masse donnée, et le coût de chaque troncature", [
        ("a", "a list of 6 numbers (3 decimals)", "floats(tempered_6(F(1, 3)))",
         '''decimals=3,
           mistakes={"à T = 1/3, on élève à la puissance 1/T, pas à la puissance T": floats(tempered_float_6(3.0)),
                     "multiplier toutes les probabilités par un même nombre ne change rien après la renormalisation : on "
                     "élève à une puissance": floats(P_6),
                     "les probabilités tempérées se renormalisent pour que leur somme vaille 1":
                         floats([p ** 3 for p in P_6])}'''),
        ("b", "a list of 6 numbers (4 decimals)", "floats(truncated_6(P_6, TOP3_6))",
         '''decimals=4,
           mistakes={"la loi conditionnelle divise par la masse P(S) des issues gardées":
                         floats([p if i in TOP3_6 else 0 for i, p in enumerate(P_6)]),
                     "le top-3 tronque la loi de départ p, pas la loi refroidie":
                         floats(truncated_6(tempered_6(F(1, 3)), TOP3_6))}'''),
        ("c", "a list of 2 numbers (4 decimals): KL, then the half L1 norm", "costs_6(TOP3_6)",
         '''decimals=4,
           mistakes={"la divergence KL se compte en nats, avec ln": costs_6(TOP3_6, log=math.log2),
                     "la distance en variation totale est la moitié de la norme L1":
                         [costs_6(TOP3_6)[0], 2 * costs_6(TOP3_6)[1]],
                     "1 − P(S) est la distance en variation totale, pas la divergence KL": [costs_6(TOP3_6)[1]] * 2}'''),
        ("d", "a list of integers, by decreasing probability", "top_p_6(M_6)",
         '''mistakes={"la liste se range par probabilité décroissante, pas par numéro de catégorie": sorted(top_p_6(M_6)),
                     "les issues se prennent par probabilité décroissante, pas dans l'ordre des catégories":
                         top_p_6(M_6, ordered=False)}'''),
        ("e", "a list of 2 numbers (4 decimals): KL, then the half L1 norm", "costs_6(top_p_6(M_6))",
         '''decimals=4,
           mistakes={"la divergence KL se compte en nats, avec ln": costs_6(top_p_6(M_6), log=math.log2),
                     "le coût se calcule avec la masse de l'ensemble gardé, pas avec le seuil m":
                         [-math.log(float(M_6)), float(1 - M_6)]}'''),
        ("f", 'an interval, as a text in French notation with decimal points, like "]2.5 ; 4]"', "three_outcomes_6()",
         '''kind="interval",
           mistakes={"au seuil m = P₂ (la masse des deux plus probables), deux issues suffisent déjà":
                         three_outcomes_6(left="["),
                     "au seuil m = P₃ (la masse des trois plus probables), trois issues atteignent m":
                         three_outcomes_6(right="["),
                     "l'intervalle demandé est celui des seuils où l'on garde trois issues, pas deux": three_outcomes_6(k=2)}'''),
    ]),

    Paper("M28.7", "Les décimales de a/n et l'itération x ↦ x² + c modulo n : prépériode et période à la main, et la borne "
                   "du principe des tiroirs", [
        ("a", "a list of 2 integers [mu, lambda]", "list(rho(lambda r: 10 * r % 26, 5)[:2])",
         '''mistakes={"la période est la longueur du cycle, sans la queue": [rho(lambda r: 10 * r % 26, 5)[0],
                                                                            rho(lambda r: 10 * r % 26, 5)[2]],
                     "la liste donne la prépériode, puis la période": list(rho(lambda r: 10 * r % 26, 5)[1::-1])}'''),
        ("b", "a list of 2 integers [mu, lambda]", "list(rho(lambda x: (x * x + 2) % 17, 0)[:2])",
         '''mistakes={"la période est la longueur du cycle, sans la queue": [rho(lambda x: (x * x + 2) % 17, 0)[0],
                                                                            rho(lambda x: (x * x + 2) % 17, 0)[2]],
                     "la liste donne la prépériode, puis la période": list(rho(lambda x: (x * x + 2) % 17, 0)[1::-1])}'''),
        ("c", BOOL, "all(rho(lambda r, n=n: 10 * r % n, a)[1] <= n - 1 for n in range(2, 80) for a in range(1, n))",
         '''mistakes={"compte les restes possibles quand le développement ne s'arrête pas": False}'''),
    ]),

    Paper("M28.11", "Pont : diviser des scores par T avant la softmax, ou élever les probabilités à la puissance 1/T, la "
                    "même loi ; et le même top-k", [
        ("a", "a list of 5 numbers (4 decimals)", "floats(softmax(Z_11))",
         '''decimals=4,
           mistakes={"la softmax passe les scores à l'exponentielle avant de normaliser": floats(Z_11 / Z_11.sum()),
                     "la softmax normalise : la somme des probabilités vaut 1": floats(np.exp(Z_11))}'''),
        ("b", "a list of 5 numbers (4 decimals)", "floats(softmax(Z_11 / 3))",
         '''decimals=4,
           mistakes={"la température divise les scores : z/T, pas zT": floats(softmax(3 * Z_11)),
                     "on divise les scores par T avant la softmax, pas les probabilités après": floats(softmax(Z_11) / 3)}'''),
        ("c", "a list of 5 numbers (4 decimals)", "floats(top_k_11(power_11(softmax(Z_11), 3), 3))",
         '''decimals=4,
           mistakes={"tronque la loi à T = 3, pas la loi de départ": floats(top_k_11(softmax(Z_11), 3)),
                     "la loi tronquée se renormalise sur les trois espèces gardées":
                         floats(top_k_11(power_11(softmax(Z_11), 3), 3, renormalize=False))}'''),
        ("d", BOOL, "all(set(np.argsort(-softmax(Z_11 / T), kind='stable')[:3]) == set(np.argsort(-Z_11, kind='stable')[:3]) "
                    "for T in (0.05, 0.3, 1.0, 3.0, 25.0))",
         '''mistakes={"compare l'ordre des espèces aux deux températures": False}'''),
        ("e", BOOL, "bool(np.allclose(top_k_11(power_11(softmax(Z_11), 3), 3), power_11(top_k_11(softmax(Z_11), 3), 3)))",
         '''mistakes={"écris les deux lois pour une espèce gardée, et compare leurs dénominateurs": False}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (exact fractions where the calculation is exact)
import itertools
import math
from fractions import Fraction as F

import numpy as np
from scipy import linalg


def floats(values):
    """A number, a vector or a matrix (fractions, NumPy) as a float or nested lists of floats (-0.0 written 0.0)."""
    return (np.round(np.asarray(values, dtype=float), 12) + 0.0).tolist()


def sq_dists(Z):
    """The matrix of the squared distances between the rows of Z."""
    Z = np.asarray(Z, dtype=float)
    return ((Z[:, None, :] - Z[None, :, :]) ** 2).sum(axis=-1)


def eigen_desc(S):
    """The eigenvalues of a symmetric matrix, in decreasing order (scipy.linalg.eigh), rounded to 1e-9."""
    return floats(np.round(linalg.eigh(np.asarray(S, dtype=float), eigvals_only=True)[::-1], 9))


def nonzero_desc(S):
    """The eigenvalues of a symmetric matrix larger than 1e-9, in decreasing order."""
    return [v for v in eigen_desc(S) if v > 1e-9]


# M28.1: the four beacons, in rows (m)
X_1 = np.array([[3, 1], [1, 3], [-2, 0], [0, -2]], dtype=float)
G_1 = (X_1 @ X_1.T).tolist()


def from_point_0(rule):
    """rule(G_ii, G_jj, G_ij) for i = 1 and j = 2, 3, 4 (the first point against the three others)."""
    return [float(rule(G_1[0][0], G_1[j][j], G_1[0][j])) for j in (1, 2, 3)]


# M28.2: the rhombus A, B, C, D (km): AB = BC = CD = DA = 29, AC = 40, BD = 42; e) AC = 50
D_2 = np.array([[0, 29, 40, 29], [29, 0, 29, 42], [40, 29, 0, 29], [29, 42, 29, 0]], dtype=float)
D2_2 = D_2 ** 2
D2_2E = D2_2.copy()
D2_2E[0, 2] = D2_2E[2, 0] = 50.0 ** 2


def double_centering(M):
    """−½ J M J with the centering matrix J = I − 11ᵀ/n."""
    n = len(M)
    J = np.eye(n) - np.ones((n, n)) / n
    return -0.5 * J @ np.asarray(M, dtype=float) @ J


def spectral_map(G, root=True):
    """The map of the statement: column k = √λ_k q_k (root=False: λ_k q_k), the eigenvalues > 1e-9 by decreasing value
    (scipy.linalg.eigh), and in each column the first coordinate of absolute value > 1e-8 made positive."""
    w, V = linalg.eigh(np.asarray(G, dtype=float))
    w, V = w[::-1], V[:, ::-1]
    keep = w > 1e-9
    X = V[:, keep] * (np.sqrt(w[keep]) if root else w[keep])
    for k in range(X.shape[1]):
        first = np.flatnonzero(np.abs(X[:, k]) > 1e-8)[0]
        if X[first, k] < 0:
            X[:, k] = -X[:, k]
    return np.round(X, 9) + 0.0


# M28.3: four emitters in [0, 1]
W_3 = np.array([2.0, -1.0, 2.0, 4.0])
A_3 = np.array([[5, -1, 0, 0], [-1, 5, 0, 0], [0, 0, 6, -2], [0, 0, -2, 3]], dtype=float)
X0_3 = np.array([0.3, 0.3, 0.6, 0.92])
ETA_3 = 0.2
BEST_3 = (W_3 > 0).astype(float)                       # the vertex of the box that maximizes wᵀx
GAP_3 = np.abs(BEST_3 - X0_3)                          # the distance of each coordinate to its bound
VERTICES_3 = [np.array(v, dtype=float) for v in itertools.product([0, 1], repeat=4)]


def first_step_3(stop):
    """The first t >= 1 such that stop(x_t, x_(t−1)), for the projected ascent clip(x + η w, 0, 1) from x0."""
    previous, x = X0_3, np.clip(X0_3 + ETA_3 * W_3, 0, 1)
    for t in itertools.count(1):
        if stop(x, previous):
            return t
        previous, x = x, np.clip(x + ETA_3 * W_3, 0, 1)


# M28.4: a bar with free ends (°C)
X_4 = np.array([8.0, 6.0, 7.0, 3.0, 1.0])
L_4 = np.diag([1.0, 2, 2, 2, 1]) - np.eye(5, k=1) - np.eye(5, k=-1)           # the laplacian of a path
RING_4 = 2 * np.eye(5) - np.roll(np.eye(5), 1, axis=1) - np.roll(np.eye(5), -1, axis=1)   # the laplacian of a ring
ETA_4, H_4, N_4 = 0.15, 6.0, 4


def tv_4(x):
    """The total variation of a signal: the sum of the squares of the differences between neighbours."""
    return float(np.sum(np.diff(np.asarray(x, dtype=float)) ** 2))


# M28.5: three motifs on a 36 × 36 grid closed in both directions
II_5, JJ_5 = np.meshgrid(np.arange(36), np.arange(36), indexing="ij")
MOTIF_A_5, MOTIF_B_5 = np.cos(2 * np.pi * JJ_5 / 6), np.cos(2 * np.pi * JJ_5 / 12)
FREQ_C_5 = (1 / 12, 1 / 6)
MOTIF_C_5 = np.cos(2 * np.pi * (FREQ_C_5[0] * II_5 + FREQ_C_5[1] * JJ_5))
F_5 = 11 / 12


def ring_ratio(x):
    """VT(x) / ‖x‖² on the closed grid, VT = xᵀLx with the laplacian of the torus (np.roll)."""
    Lx = 4 * x - np.roll(x, 1, 0) - np.roll(x, -1, 0) - np.roll(x, 1, 1) - np.roll(x, -1, 1)
    return float((x * Lx).sum() / (x * x).sum())


def ring_gain_rows(x):
    """The gain of the moving average of three cells along the rows, on the closed grid."""
    y = (np.roll(x, 1, 1) + x + np.roll(x, -1, 1)) / 3
    return float((y * x).sum() / (x * x).sum())


def ring_blur(x):
    """The gain of the 3 × 3 blur on the closed grid."""
    y = sum(np.roll(np.roll(x, a, 0), b, 1) for a in (-1, 0, 1) for b in (-1, 0, 1)) / 9
    return float((y * x).sum() / (x * x).sum())


def gain_1d(f):
    """The gain (1 + 2 cos ω)/3 of the moving average of three cells, ω = 2πf."""
    return (1 + 2 * math.cos(2 * math.pi * f)) / 3


# M28.6: the forecast, categories 0 to 5
P_6 = [F(4, 100), F(19, 100), F(33, 100), F(26, 100), F(10, 100), F(8, 100)]
M_6 = F(87, 100)


def tempered_6(T):
    """p^(1/T) renormalized, exactly (T = 1/q with q an integer)."""
    powers = [p ** int(1 / T) for p in P_6]
    return [v / sum(powers) for v in powers]


def tempered_float_6(T):
    """p^(1/T) renormalized, in floats."""
    powers = [float(p) ** (1 / T) for p in P_6]
    return [v / sum(powers) for v in powers]


ORDER_6 = sorted(range(6), key=lambda i: (-P_6[i], i))   # by decreasing probability, the smaller index first
TOP3_6 = ORDER_6[:3]


def truncated_6(law, kept):
    """The conditional law on the set kept."""
    mass = sum(law[i] for i in kept)
    return [law[i] / mass if i in kept else F(0) for i in range(len(law))]


def costs_6(kept, log=math.log):
    """KL(p_S ‖ p) by its sum, and ½‖p_S − p‖₁, for the truncation of P_6 to kept."""
    pS = truncated_6(P_6, kept)
    kl = sum(float(q) * log(float(q / p)) for q, p in zip(pS, P_6) if q > 0)
    return [kl, float(sum(abs(q - p) for q, p in zip(pS, P_6)) / 2)]


def top_p_6(m, ordered=True):
    """The outcomes taken one by one (by decreasing probability, or in the order of the categories) until their mass
    reaches m."""
    order = ORDER_6 if ordered else list(range(6))
    kept = []
    for i in order:
        kept.append(i)
        if sum(P_6[k] for k in kept) >= m:
            return kept


def three_outcomes_6(k=3, left="]", right="]"):
    """The interval of the thresholds m for which the top-p keeps exactly k outcomes: ]P_(k−1) ; P_k]."""
    masses = [sum(P_6[i] for i in ORDER_6[:j]) for j in range(7)]
    return f"{left}{float(masses[k - 1]):g} ; {float(masses[k]):g}{right}"


# M28.7
def rho(f, x0):
    """(mu, lambda, j): the preperiod, the period and the index of the first repetition of u_(t+1) = f(u_t)."""
    seen, x, t = {}, x0, 0
    while x not in seen:
        seen[x] = t
        x, t = f(x), t + 1
    return seen[x], t - seen[x], t


# M28.11: the scores of the classifier of tree species
Z_11 = np.array([1.1, 2.4, 0.1, 2.1, -0.5])


def softmax(z):
    e = np.exp(np.asarray(z, dtype=float) - np.max(z))
    return e / e.sum()


def power_11(p, T):
    """p^(1/T) renormalized, on the outcomes of positive probability."""
    p = np.asarray(p, dtype=float)
    q = np.where(p > 0, p, 0.0) ** (1 / T)
    return q / q.sum()


def top_k_11(p, k, renormalize=True):
    """The conditional law on the k most probable outcomes (renormalize=False: only the others set to 0)."""
    p = np.asarray(p, dtype=float)
    kept = np.argsort(-p, kind="stable")[:k]
    q = np.zeros_like(p)
    q[kept] = p[kept]
    return q / q.sum() if renormalize else q'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M28.1 à M28.7 ; 🔗 M28.11)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question "
               "(« a number » sans décimales : la valeur exacte, ces calculs tombent juste) ;\n"
               "- une liste `[0.2, -1]`, dans l'ordre que dit la question ; un ensemble d'issues comme la liste de leurs "
               "numéros, `[4, 0, 2]` ; une matrice comme la liste de ses **lignes**, `[[1, 0], [-2, 3]]` ;\n"
               "- un intervalle entre guillemets, en notation française, avec des points décimaux, `\"]2.5 ; 4]\"` ;\n"
               "- `True` ou `False` pour un vrai ou faux.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")


def paper_part(kind: str) -> list:
    """The cells of Part 0."""
    return paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO)


# ---------------------------------------------------------------------------
# Notebook exercises: your library (M28.13, M28.14)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to D)
import math
import numbers
import re
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np

from wbm.errors import MymathMissingError
from wbm.nbtools import StopCheck, checked, drawn, filled, fr, own_code, pair, run_pytest_group, verdict

TEST_M28 = "tests/test_m28_sampling.py"            # the tests of mymath/sampling.py
REF = wbm.load_mymath("ref", alias="mymath_ref")  # the reference: the checks compute their expected values with it
ref_sampling = REF.sampling
REF_SAMPLING = {f"ref_sampling.{name}": getattr(ref_sampling, name)    # a check stops if your code calls one of them
                for name in ("points_from_gram", "temper", "smallest_mass_set")}


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


def check_rounding(ex_id, label, value, limit):
    """A number that must be a rounding error (0 <= value < limit): ✅, ⏳ or ❌."""
    if not filled(value):
        print(f"⏳ Ex {ex_id} : {label} : pas encore fait.")
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        print(f"❌ Ex {ex_id} : {label} : attendu un nombre, reçu {value!r}.")
        return False
    ok = 0 <= number < limit
    print(f"✅ Ex {ex_id} : {label} : {number:.1e}, une erreur d'arrondi." if ok else
          f"❌ Ex {ex_id} : {label} : attendu un écart de l'ordre des arrondis (positif, moins de {limit:.0e}), reçu "
          f"{number!r}.")
    return ok


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
    return arr is not None and arr.shape == want.shape and bool(np.allclose(arr, want, rtol=rtol, atol=atol))


def sq_dists_of(Z):
    """The squared distances between the rows of Z (to compare two maps: they ignore an isometry)."""
    Z = np.asarray(Z, dtype=float)
    return ((Z[:, None, :] - Z[None, :, :]) ** 2).sum(axis=-1)


_NUMBER = re.compile(r"[-−]?\\d+(?:[.,]\\d+)?(?:[eE][-−+]?\\d+)?")


def numbers_in(text):
    """The numbers written in a text (a decimal point or comma, a minus sign − or -, an exponent e-07)."""
    found = []
    for token in _NUMBER.findall(text or ""):
        try:
            found.append(float(token.replace("−", "-").replace(",", ".")))
        except ValueError:
            pass
    return found


def gives(text, values, rel=0.01, abs_tol=0.006):
    """True when the text writes one of the values (to 1 % or to 0.006)."""
    return any(math.isclose(x, v, rel_tol=rel, abs_tol=abs_tol) for x in numbers_in(text) for v in values)


def line_points(line):
    """The (x, y) points of a line of matplotlib, as two float arrays."""
    return np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)


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
    """True when every point (xs[k], ys[k]) is drawn in ax (a line with markers, or a scatter)."""
    points = np.array(drawn_points(ax, marker_only) or [(np.nan, np.nan)], dtype=float)
    return all(np.any(np.isclose(points[:, 0], x, rtol=rtol, atol=atol) & np.isclose(points[:, 1], y, rtol=rtol, atol=atol))
               for x, y in zip(np.atleast_1d(xs), np.atleast_1d(ys)))


def follows(ax, f, lo, hi, rtol=1e-6):
    """True when one line of ax has at least ten points with y = f(x), its x covering [lo, hi]."""
    for line in ax.lines:
        x, y = line_points(line)
        if (x.size >= 10 and np.all(np.isfinite(x)) and x.min() <= lo + 1e-9 * max(1.0, abs(lo))
                and x.max() >= hi - 1e-9 * max(1.0, abs(hi)) and np.allclose(y, f(x), rtol=rtol, atol=0)):
            return True
    return False'''

DATA = '''# The data of the paper exercises (02_exercices.md)
X_BEACONS = np.array([[3.0, 1.0], [1.0, 3.0], [-2.0, 0.0], [0.0, -2.0]])     # M28.1: the four beacons (m), in rows
D_RHOMBUS = np.array([[0.0, 29, 40, 29], [29, 0, 29, 42], [40, 29, 0, 29], [29, 42, 29, 0]])   # M28.2: A, B, C, D (km)
P_FORECAST = np.array([0.04, 0.19, 0.33, 0.26, 0.10, 0.08])                  # M28.6: the forecast, categories 0 to 5'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M28")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M27). Ouvre ta copie `mon_travail/mymath/sampling.py`, lis la docstring "
         "du module (ses conventions, et ce qui est permis) puis celle de la fonction, remplace chaque "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Dans le notebook, appelle tes fonctions par "
         "`mymath.sampling.<nom>` (par exemple `mymath.sampling.points_from_gram(G)`), ou donne-leur un nom court "
         "(`points_from_gram = mymath.sampling.points_from_gram`) dans une cellule exécutée après le rechargement. "
         "⚠️ Le squelette n'importe rien : ajoute en tête du fichier `import numpy as np` (et `import math`, "
         "`import numbers` si tu t'en sers). NumPy est permis, mais de `np.linalg` seulement `eigh` (dans "
         "`points_from_gram`), et aucune fonction de SciPy ni de scikit-learn (`scipy.special.softmax` donnerait "
         "`temper`) : les tests comparent tes résultats à ceux de SciPy, et un test lit ton module. Une loi est donnée "
         "par ses **probabilités**, jamais par des scores ; rien n'est tiré au hasard ; ne modifie jamais les tableaux "
         "reçus. Hors de `mymath`, le notebook peut se servir de tout NumPy et de SciPy.")

REMINDER = ("> Même mode d'emploi qu'en M28.13 : écris les fonctions dans ta copie `mon_travail/mymath/sampling.py`, "
            "**enregistre**, puis exécute les cellules ci-dessous ; la première recharge ta librairie.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of sampling.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group(TEST_M28, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_M28, "{keyword}", impl="ref")')]


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


CHECK_13 = '''with checked("M28.13"):                       # b): Y and R, compared with what the reference gives now
    results_13 = []
    report_13 = reporter(results_13, stop=False)
    G_c13 = X_BEACONS @ X_BEACONS.T
    want_Y_c13 = ref_sampling.points_from_gram(G_c13)        # computed by the reference at check time (no value written here)
    if not filled(Y_M28_13b):
        print("⏳ Ex M28.13b : la carte Y, pas encore faite.")
    else:
        Y_c13 = as_floats(Y_M28_13b)
        if Y_c13 is None or Y_c13.shape != want_Y_c13.shape:
            why_c13 = (f"Y a une ligne par balise et une colonne par valeur propre non nulle : attendu la forme "
                       f"{want_Y_c13.shape}, reçu {None if Y_c13 is None else Y_c13.shape}")
        elif matches(Y_c13, want_Y_c13, atol=1e-9):
            why_c13 = ""
        elif matches(Y_c13[:, ::-1], want_Y_c13, atol=1e-9):
            why_c13 = "les colonnes viennent par valeur propre décroissante (np.linalg.eigh les range dans l'ordre croissant)"
        elif matches(np.abs(Y_c13), np.abs(want_Y_c13), atol=1e-9):
            why_c13 = ("au signe près d'une colonne : dans chaque colonne, la première coordonnée de valeur absolue > 1e-8 "
                       "est positive (relance les tests de points_from_gram)")
        elif np.allclose(sq_dists_of(Y_c13), sq_dists_of(X_BEACONS), atol=1e-9):
            why_c13 = "Y a les bonnes distances, mais pas la carte que donne la construction de la docstring"
        else:
            why_c13 = "Y Yᵀ doit redonner G = X Xᵀ (relance les tests de points_from_gram)"
        report_13(not why_c13, "Ex M28.13b : la carte Y est celle de la construction de la docstring",
                  f"Ex M28.13b : la carte Y : {why_c13}")
    check_rounding("M28.13b", "le plus grand écart |Y Yᵀ − G|", gap_M28_13b, 1e-12)
    if not filled(R_M28_13b):
        print("⏳ Ex M28.13b : la matrice R, pas encore faite.")
    else:
        want_R_c13 = want_Y_c13.T @ X_BEACONS @ np.linalg.inv(X_BEACONS.T @ X_BEACONS)   # the formula of the statement
        R_c13 = as_floats(R_M28_13b)
        if matches(R_c13, want_R_c13, atol=1e-9):
            why_c13 = ""
        elif matches(R_c13, want_R_c13.T, atol=1e-9):
            why_c13 = "y_i = R x_i pour les points en lignes s'écrit Y = X Rᵀ : R = Yᵀ X (Xᵀ X)⁻¹, pas sa transposée"
        else:
            why_c13 = "R = Yᵀ X (Xᵀ X)⁻¹, de forme (2, 2), avec ta carte Y"
        report_13(not why_c13, "Ex M28.13b : R envoie chaque balise sur sa ligne de Y", f"Ex M28.13b : R : {why_c13}")
    check_answer("M28.13b", answer_M28_13b)'''

NOTE_13 = (r"`G = np.array(G, dtype=float)`, les contrôles, `s`, la symétrie, `np.linalg.eigh` puis l'ordre retourné, le "
           r"refus d'une valeur propre sous $-s$, la mise à 0, `V[:, :k] * np.sqrt(w[:k])`, le signe colonne par "
           r"colonne. a) $\begin{pmatrix} 0 & 20 \\ 21 & 0 \\ 0 & -20 \\ -21 & 0 \end{pmatrix}$, comme M28.2 d). b) "
           r"$\mathbf{Y} = \sqrt2\begin{pmatrix} 2 & 1 \\ 2 & -1 \\ -1 & -1 \\ -1 & 1 \end{pmatrix}$, un écart de "
           r"l'ordre de $10^{-15}$, $\mathbf{R} = \frac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ : "
           r"$\det\mathbf{R} = -1$, orthogonale, une symétrie. c) Une `ValueError` ; la plus petite valeur propre vaut "
           r"$-225$. d) $(0, 21, 0, -21)$ et 800, la valeur propre laissée de côté.")

M28_13 = Ex(
    "M28.13", "🔨", 2, 25, "Une configuration de points de matrice de Gram donnée, par le théorème spectral · "
    "`points_from_gram`",
    "programmer la construction de positions à partir d'une matrice de Gram, puis retrouver une carte à partir de "
    "distances, voir l'isométrie qui la sépare des vraies positions, et ce que deviennent des distances impossibles et "
    "une colonne de moins.", "fiche §2 ; M12c, M12d ; Ex M28.1 et M28.2", tracks="C", mymath="sampling.py", note=NOTE_13,
    body=HOWTO + r"""

Écris `points_from_gram(G, dim=None, tol=1e-9)` (fiche §2), en suivant sa docstring : contrôle `G` (une matrice carrée non vide de nombres finis, symétrique au seuil $s = \texttt{tol}\cdot\max(1, \max\lvert G_{ij}\rvert)$ près), `dim` (un entier entre 1 et $n$, pas un booléen) et `tol` ($\ge 0$) ; diagonalise par `np.linalg.eigh`, qui range les valeurs propres par ordre **croissant** (retourne l'ordre) ; refuse une valeur propre sous $-s$ (une `ValueError` : $\mathbf{G}$ n'est pas une matrice de Gram) ; compte comme nulles celles de $[-s, s]$ ; garde `dim` colonnes, par défaut autant que de valeurs propres $> s$ (au moins une) ; multiplie chaque vecteur propre unitaire par la racine de sa valeur propre ; puis rends positive, dans chaque colonne, la première coordonnée de valeur absolue $> 10^{-8}$ ; rends un tableau de flottants de forme $(n, \texttt{dim})$.

**L'usage.** La cellule de données de la partie A donne les balises de M28.1 (`X_BEACONS`, en lignes) et les distances du losange de M28.2 (`D_RHOMBUS`, dans l'ordre A, B, C, D). Avec ta fonction :
- a) le losange : forme $\mathbf{G} = -\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$ à partir des **carrés** des distances, puis la carte (une matrice $4 \times 2$, telle que rendue), à comparer à ta réponse d) de M28.2 ;
- b) les balises : la carte $\mathbf{Y}$ rendue pour $\mathbf{G} = \mathbf{X}\mathbf{X}^\top$ (`Y_M28_13b`), le plus grand écart $\max\lvert\mathbf{Y}\mathbf{Y}^\top - \mathbf{G}\rvert$ (`gap_M28_13b`), la matrice $\mathbf{R} = \mathbf{Y}^\top\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}$, de forme $(2, 2)$, telle que $\mathbf{y}_i = \mathbf{R}\mathbf{x}_i$ pour les quatre balises (`R_M28_13b`), puis son déterminant et vrai ou faux : $\mathbf{R}$ est orthogonale ($\mathbf{R}\mathbf{R}^\top = \mathbf{I}$ à $10^{-9}$ près) (une liste de 2 : le nombre, puis le booléen) ;
- c) le losange avec $\mathrm{AC} = 50$ km (M28.2 e)) : vrai ou faux, ta fonction lève une `ValueError`, puis la plus petite valeur propre de $-\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$, par `np.linalg.eigvalsh` (hors de `mymath`) (une liste de 2 : le booléen, puis le nombre) ;
- d) le losange avec `dim=1` : les quatre coordonnées de la carte à une colonne (`.ravel()`), puis $\lVert\mathbf{G} - \mathbf{X}\mathbf{X}^\top\rVert_F$ (une liste de 5 nombres).

Ce qu'il faut observer : la carte ne retrouve les vraies positions qu'à une isométrie près, ici une symétrie ($\det\mathbf{R} = -1$) ; des distances impossibles donnent une valeur propre négative, que la fonction refuse ; une colonne de moins, c'est la meilleure matrice de Gram de rang 1 (Eckart-Young), à une distance égale à la valeur propre laissée de côté.""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_points_from_gram_ or test_module_uses_") + [
        ("md", "**L'usage** : le losange, les balises, des distances impossibles, et une colonne de moins."),
        ("todo", '''answer_M28_13a = answer_M28_13b = answer_M28_13c = answer_M28_13d = ...
Y_M28_13b = gap_M28_13b = R_M28_13b = ...
with wbm.attempt("M28.13"):          # if you call points_from_gram here: ⏳ while it is not written
    answer_M28_13a = ...  # a) a (4, 2) array, as returned: the map of the rhombus, from G = -1/2 J D² J
    Y_M28_13b = ...       # b) the (4, 2) array returned for G = X Xᵀ (the beacons)
    gap_M28_13b = ...     # b) a number, as computed: the largest |Y Yᵀ − G|
    R_M28_13b = ...       # b) the (2, 2) array R = Yᵀ X (Xᵀ X)⁻¹
    answer_M28_13b = ...  # b) a list of 2: det R (as computed), then True or False: R Rᵀ = I (to 1e-9)
    answer_M28_13c = ...  # c) a list of 2: True or False: your function raises a ValueError for AC = 50 km, then the smallest eigenvalue of -1/2 J D² J (np.linalg.eigvalsh)
    answer_M28_13d = ...  # d) a list of 5 numbers, as computed: the 4 coordinates of the map with dim=1, then ‖G − X Xᵀ‖_F'''),
        ("check", "check_answer(\"M28.13a\", answer_M28_13a)\n\n" + CHECK_13 + "\n\n" + answers_check("M28.13", "cd")),
        ("solution", '''points_from_gram = mymath.sampling.points_from_gram
J_13 = np.eye(4) - np.ones((4, 4)) / 4
G_rhombus_13 = -0.5 * J_13 @ D_RHOMBUS ** 2 @ J_13
answer_M28_13a = points_from_gram(G_rhombus_13)
G_beacons_13 = X_BEACONS @ X_BEACONS.T
Y_M28_13b = points_from_gram(G_beacons_13)
gap_M28_13b = float(np.abs(Y_M28_13b @ Y_M28_13b.T - G_beacons_13).max())
R_M28_13b = Y_M28_13b.T @ X_BEACONS @ np.linalg.inv(X_BEACONS.T @ X_BEACONS)
answer_M28_13b = [float(np.linalg.det(R_M28_13b)), bool(np.allclose(R_M28_13b @ R_M28_13b.T, np.eye(2), rtol=0, atol=1e-9))]
D2_wrong_13 = D_RHOMBUS ** 2
D2_wrong_13[0, 2] = D2_wrong_13[2, 0] = 50.0 ** 2
G_wrong_13 = -0.5 * J_13 @ D2_wrong_13 @ J_13
try:
    points_from_gram(G_wrong_13)
    raised_13 = False
except ValueError as error_13:
    raised_13 = True
    print("c) ValueError :", error_13)
answer_M28_13c = [raised_13, float(np.linalg.eigvalsh(G_wrong_13).min())]
X1_13 = points_from_gram(G_rhombus_13, dim=1)
answer_M28_13d = X1_13.ravel().tolist() + [float(np.linalg.norm(G_rhombus_13 - X1_13 @ X1_13.T))]
print("a)", np.round(answer_M28_13a, 6).tolist())
print("b) Y =", np.round(Y_M28_13b, 6).tolist(), "; écart", gap_M28_13b, "; R =", np.round(R_M28_13b, 6).tolist(), ";",
      answer_M28_13b)
print("c)", answer_M28_13c, " d)", np.round(answer_M28_13d, 6).tolist())

''' + CHECK_13),
        ("record", '''from scipy import linalg as linalg_13r


def map_13r(G, dim=None):
    """The oracle: scipy.linalg.eigh, the eigenvalues by decreasing value, column k = √λ_k q_k, the sign convention."""
    w, V = linalg_13r.eigh(np.asarray(G, dtype=float))
    w, V = w[::-1], V[:, ::-1]
    s = 1e-9 * max(1.0, float(np.abs(G).max()))
    w = np.where(w > s, w, 0.0)
    k = max(1, int(np.count_nonzero(w))) if dim is None else dim
    X = V[:, :k] * np.sqrt(w[:k])
    for j in range(k):
        first = np.flatnonzero(np.abs(X[:, j]) > 1e-8)
        if first.size and X[first[0], j] < 0:
            X[:, j] = -X[:, j]
    return X + 0.0


D_13r = np.array([[0.0, 29, 40, 29], [29, 0, 29, 42], [40, 29, 0, 29], [29, 42, 29, 0]])
J_13r = np.eye(4) - 0.25
G_13r = -0.5 * J_13r @ D_13r ** 2 @ J_13r
map_rhombus_13r = map_13r(G_13r)
wbm.record("M28.13a", map_rhombus_13r.tolist(), decimals=6,
           mistakes={"G se forme à partir des carrés des distances, et les colonnes viennent par valeur propre décroissante":
                         map_rhombus_13r[:, ::-1].tolist(),
                     "dans chaque colonne, la première coordonnée de valeur absolue > 1e-8 est positive":
                         (-map_rhombus_13r).tolist(),
                     "G = −½ J D⁽²⁾ J : le facteur ½ compte (sans lui, chaque coordonnée est multipliée par √2)":
                         (math.sqrt(2) * map_rhombus_13r).tolist()})
X_13r = np.array([[3.0, 1.0], [1.0, 3.0], [-2.0, 0.0], [0.0, -2.0]])
Y_13r = map_13r(X_13r @ X_13r.T)
R_13r = Y_13r.T @ X_13r @ np.linalg.inv(X_13r.T @ X_13r)
wbm.record("M28.13b", [float(np.linalg.det(R_13r)), True], decimals=6,
           mistakes={"R Rᵀ = I : une matrice orthogonale conserve les produits scalaires, et Y Yᵀ = X Xᵀ":
                         [float(np.linalg.det(R_13r)), False],
                     "le déterminant de R se calcule sur R = Yᵀ X (Xᵀ X)⁻¹, avec la carte rendue par ta fonction":
                         [-float(np.linalg.det(R_13r)), True]})
D2e_13r = D_13r ** 2
D2e_13r[0, 2] = D2e_13r[2, 0] = 2500.0
lowest_13r = float(linalg_13r.eigh(-0.5 * J_13r @ D2e_13r @ J_13r, eigvals_only=True)[0])
wbm.record("M28.13c", [True, lowest_13r], decimals=6,
           mistakes={"une valeur propre sous −s veut dire que G n'est pas une matrice de Gram : ta fonction doit lever une "
                     "ValueError (relance ses tests)": [False, lowest_13r],
                     "la plus petite valeur propre se calcule sur −½ J D⁽²⁾ J, avec les carrés des distances":
                         [True, float(linalg_13r.eigh(-0.5 * J_13r @ np.sqrt(D2e_13r) @ J_13r, eigvals_only=True)[0])]})
X1_13r = map_13r(G_13r, dim=1)
wbm.record("M28.13d", X1_13r.ravel().tolist() + [float(np.linalg.norm(G_13r - X1_13r @ X1_13r.T))], decimals=6,
           mistakes={"avec dim=1, on garde la colonne de la plus grande valeur propre":
                         map_13r(G_13r)[:, 1].tolist() + [float(np.linalg.norm(G_13r - np.outer(map_13r(G_13r)[:, 1], map_13r(G_13r)[:, 1])))],
                     "‖·‖_F est la racine de la somme des carrés des coefficients, pas cette somme":
                         X1_13r.ravel().tolist() + [float(np.linalg.norm(G_13r - X1_13r @ X1_13r.T)) ** 2]})'''),
    ],
)

NOTE_14 = (r"`temper` : la validation de la loi et de $T$, $T = 0$ (`p == p.max()`), $T = \infty$ (`p > 0`), puis "
           r"`logs = np.log(p[p > 0])`, `w = np.exp((logs - logs.max()) / T)` et la division par la somme. "
           r"`smallest_mass_set` : `order = np.argsort(-p, kind=\"stable\")`, `np.cumsum`, le premier cumul $\ge$ "
           r"`mass - 1e-9`. a) $(0{,}0010 ;\ 0{,}1107 ;\ 0{,}5801 ;\ 0{,}2837 ;\ 0{,}0161 ;\ 0{,}0083)$ et `[2, 3, 1, 4]`. "
           r"b) `[0.5, 0, 0.5, 0, 0]` et `[0.25, 0, 0.25, 0.25, 0.25]`. c) `[3, 4, 5, 6]`. d) 1,0303 ; 1,5927 ; 1,7642 "
           r"(et $\ln 6 \approx 1{,}7918$) ; vrai.")

M28_14 = Ex(
    "M28.14", "🔨", 2, 30, "Tempérer une loi donnée par ses probabilités, et le plus petit ensemble de masse donnée · "
    "`temper`, `smallest_mass_set`",
    "programmer la température sur des probabilités et le plus petit ensemble de masse donnée, puis voir ce que la "
    "température fait à l'ensemble d'un top-p et à l'entropie.", "fiche §5 ; M17 ; Ex M28.6", tracks="C, E",
    mymath="sampling.py", note=NOTE_14,
    body=REMINDER + r"""

Écris `temper(p, temperature)` et `smallest_mass_set(p, mass)` (fiche §5), en suivant leurs docstrings. `temper` : contrôle la loi (1-D, non vide, des nombres finis $\ge 0$ de somme 1 à $10^{-9}$ près) et la température ($\ge 0$, `np.inf` permis, ni `nan` ni booléen) ; traite d'abord $T = 0$ (la loi uniforme sur les issues les plus probables) et $T = \infty$ (la loi uniforme sur les issues de probabilité non nulle) ; sinon, calcule par les logarithmes des seuls $p_i > 0$, moins leur maximum, divisés par $T$, puis l'exponentielle et la division par la somme, et laisse les zéros à 0. `smallest_mass_set` : contrôle la loi et la masse ($0 < \texttt{mass} \le 1$) ; range les issues par probabilité décroissante avec un tri **stable** (`np.argsort(-p, kind="stable")` : à égalité, la plus petite issue d'abord) ; cumule jusqu'à ce que le total atteigne `mass` $- 10^{-9}$ ; rends les indices gardés, dans cet ordre, en tableau d'entiers.

**L'usage.** La cellule de données de la partie A donne la prévision de M28.6 (`P_FORECAST`). Avec tes fonctions :
- a) `temper(P_FORECAST, 1/3)`, puis `smallest_mass_set(P_FORECAST, 0.87)`, à comparer à tes réponses a) et d) de M28.6 (une liste de 10 nombres : les 6 probabilités, puis les 4 indices) ;
- b) pour $\mathbf{q} = (0{,}3 ;\ 0 ;\ 0{,}3 ;\ 0{,}25 ;\ 0{,}15)$ : `temper(q, 0)`, puis `temper(q, np.inf)` (une liste de 10 nombres) ;
- c) les tailles de l'ensemble du top-p de seuil 0,87 de la prévision tempérée, pour $T = \frac13$, 1, 3 et $\infty$, dans cet ordre (une liste de 4 entiers) ;
- d) les entropies, en nats, de la prévision tempérée à $T = \frac13$, 1 et 3 (calculées hors de `mymath`, sans compter les issues de probabilité nulle), puis vrai ou faux : elles croissent (une liste de 4 : les trois nombres, puis le booléen).

Ce qu'il faut observer : refroidir rétrécit l'ensemble du top-p, réchauffer l'agrandit ; à $T = \infty$, les zéros restent nuls ; l'entropie croît avec $T$ vers $\ln 6$.""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("test_temper_ or test_smallest_mass_set_") + [
        ("md", "**L'usage** : la prévision refroidie et son top-p, les deux limites, les tailles du top-p, et l'entropie."),
        ("todo", '''Q_14 = np.array([0.3, 0.0, 0.3, 0.25, 0.15])
answer_M28_14a = answer_M28_14b = answer_M28_14c = answer_M28_14d = ...
with wbm.attempt("M28.14"):          # if you call temper or smallest_mass_set here: ⏳ while they are not written
    answer_M28_14a = ...  # a) a list of 10 numbers: temper(P_FORECAST, 1/3) (6 probabilities), then smallest_mass_set(P_FORECAST, 0.87) (4 indices)
    answer_M28_14b = ...  # b) a list of 10 numbers: temper(Q_14, 0), then temper(Q_14, np.inf)
    answer_M28_14c = ...  # c) a list of 4 integers: the sizes of the top-p set of mass 0.87 of the tempered forecast, for T = 1/3, 1, 3, np.inf
    answer_M28_14d = ...  # d) a list of 4: the entropies (nats) of the tempered forecast at T = 1/3, 1, 3, then True or False: they grow'''),
        ("check", answers_check("M28.14", "abcd")),
        ("solution", '''Q_14 = np.array([0.3, 0.0, 0.3, 0.25, 0.15])
temper, smallest_mass_set = mymath.sampling.temper, mymath.sampling.smallest_mass_set
answer_M28_14a = temper(P_FORECAST, 1 / 3).tolist() + smallest_mass_set(P_FORECAST, 0.87).tolist()
answer_M28_14b = temper(Q_14, 0).tolist() + temper(Q_14, np.inf).tolist()
answer_M28_14c = [len(smallest_mass_set(temper(P_FORECAST, T), 0.87)) for T in (1 / 3, 1, 3, np.inf)]


def entropy_14(q):
    """The entropy in nats, without the outcomes of probability 0."""
    q = np.asarray(q, dtype=float)
    q = q[q > 0]
    return float(-np.sum(q * np.log(q)))


entropies_14 = [entropy_14(temper(P_FORECAST, T)) for T in (1 / 3, 1, 3)]
answer_M28_14d = entropies_14 + [bool(entropies_14[0] < entropies_14[1] < entropies_14[2])]
print("a)", np.round(answer_M28_14a, 6).tolist())
print("b)", answer_M28_14b, " c)", answer_M28_14c, " d)", np.round(entropies_14, 6).tolist(), answer_M28_14d[3])'''),
        ("record", '''from scipy import special as special_14r
from scipy import stats as stats_14r


def temper_14r(p, T):
    """The oracle: softmax(ln p / T) on the positive p_i (scipy.special.softmax), the limits T = 0 and T = inf."""
    p = np.asarray(p, dtype=float)
    q, positive = np.zeros_like(p), p > 0
    if T == 0:
        q[p == p.max()] = 1.0 / np.count_nonzero(p == p.max())
    elif np.isinf(T):
        q[positive] = 1.0 / np.count_nonzero(positive)
    else:
        q[positive] = special_14r.softmax(np.log(p[positive]) / T)
    return q


def smallest_14r(p, mass):
    """The oracle: a smallest set by exhaustive search (itertools), its outcomes by decreasing probability, ties by index."""
    for k in range(1, len(p) + 1):
        sets = [c for c in itertools.combinations(range(len(p)), k) if sum(p[i] for i in c) >= mass - 1e-9]
        if sets:
            best = max(sets, key=lambda c: (round(sum(p[i] for i in c), 12), [-i for i in c]))
            return sorted(best, key=lambda i: (-p[i], i))


import itertools
p_14r = np.array([0.04, 0.19, 0.33, 0.26, 0.10, 0.08])
q_14r = np.array([0.3, 0.0, 0.3, 0.25, 0.15])
cooled_14r = temper_14r(p_14r, 1 / 3)
wbm.record("M28.14a", cooled_14r.tolist() + smallest_14r(p_14r, 0.87), decimals=6,
           mistakes={"à T = 1/3, on élève les probabilités à la puissance 1/T = 3, pas 1/3":
                         temper_14r(p_14r, 3).tolist() + smallest_14r(p_14r, 0.87),
                     "smallest_mass_set rend les issues par probabilité décroissante, pas par numéro":
                         cooled_14r.tolist() + sorted(smallest_14r(p_14r, 0.87)),
                     "smallest_mass_set prend les issues par probabilité décroissante (np.argsort(-p, kind=\\"stable\\"))":
                         cooled_14r.tolist() + list(np.argsort(p_14r, kind="stable")[:4])})
wbm.record("M28.14b", temper_14r(q_14r, 0).tolist() + temper_14r(q_14r, np.inf).tolist(), decimals=6,
           mistakes={"à T = ∞, la loi est uniforme sur les issues de probabilité non nulle : un zéro reste nul":
                         temper_14r(q_14r, 0).tolist() + [0.2] * 5,
                     "à T = 0, deux issues ex aequo se partagent la probabilité":
                         [1.0, 0.0, 0.0, 0.0, 0.0] + temper_14r(q_14r, np.inf).tolist()})
sizes_14r = [len(smallest_14r(temper_14r(p_14r, T), 0.87)) for T in (1 / 3, 1, 3, np.inf)]
wbm.record("M28.14c", sizes_14r,
           mistakes={"dans l'ordre T = 1/3, 1, 3, ∞ : refroidir rétrécit l'ensemble": sizes_14r[::-1],
                     "à T = ∞, la loi est uniforme sur les six catégories : il en faut assez pour atteindre 0,87":
                         sizes_14r[:3] + [5]})
entropies_14r = [float(stats_14r.entropy(temper_14r(p_14r, T))) for T in (1 / 3, 1, 3)]
wbm.record("M28.14d", entropies_14r + [True], decimals=6,
           mistakes={"l'entropie se compte en nats, avec ln": [h / math.log(2) for h in entropies_14r] + [True],
                     "compare les trois entropies dans l'ordre des températures": entropies_14r + [False]})'''),
    ],
)

PART_A = Part("A", "Ta librairie : une carte à partir d'une matrice de Gram ; une loi tempérée et le plus petit ensemble "
              "de masse donnée",
              "Fiche §2 et §5. Les trois fonctions de `mymath/sampling.py`, leurs tests, et un usage de chacune sur les "
              "données des exercices papier. La cellule de données ci-dessous recopie les données des exercices papier.",
              given=TOOLS + "\n\n\n" + DATA, exercises=[M28_13, M28_14])
