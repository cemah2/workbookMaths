#!/usr/bin/env python
"""Build the two notebooks of chapter M25b from a single source (used by Claude).

    python tools/chapters/build_m25b.py
    python tools/run_all_notebooks.py chapitres/m25b_variables_latentes/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m25b_variables_latentes/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M25b.1, 2, 3, 6, 9, 10, 12, 13, 14 and 🔗 M25b.23), each answer computed in the
notebook from the data of its statement (exact fractions for M25b.2 and M25b.14, NumPy for the rest, the logarithms of
the densities by the formula of the fiche), each wrong value computed by the error its message names; parts A to D are
the notebook exercises (M25b.20 to M25b.30), exactly as 02_exercices.md describes them. Wrong-answer messages state a
rule, never a number of the answer, the last step that gives it, nor another sub-question.

Data. The notebook exercises take the data of 02_exercices.md: the four resistors of M25b.3 (46.0, 48.0, 49.4 and
52.1 Ω, π = (0.45, 0.55), μ = (47, 51), variances (1, 2.5)), a stray resistor of 120 Ω, and the rod of 98.2 mm of
M25b.1 with its three machines (M25b.20); the hard responsibilities [[1, 0], [1, 0], [0, 1], [0, 1]] and
[[1, 0], [0, 1], [0, 1], [0, 1]], reg = 0.01 (M25b.21); the three pieces of M25b.23 (9.2, 11.6 and 13.4 g,
π = (0.75, 0.25), N(10, 1) and N(14, 2.25), the table R) (M25b.22); the planes and the lines of M25b.10, the model of
M25b.9 (w = (2, 1, 2), μ = (12, 11, 13), σ² = 3) with 500 candidates drawn with the seed 6054 and the candidate
(15, 12, 15) (M25b.24); the mixture (0.48, 0.52), N(50.57, 2.36), a component centred on 46.0 Ω of standard deviation
1e-1, 1e-3 and 1e-6, reg = 0.01 (M25b.25); 300 fish lengths of three cohorts (0.5, 0.3, 0.2), N(12, 1.5²), N(20, 2²),
N(28, 2.5²), drawn with the seeds 6056 (the cohorts) and 6057 to 6059 (the lengths), ten initializations drawn with the
seed 6060 (M25b.26); the travel times of M25b.13, 0.7 N(22, 4) + 0.3 N(40, 6.25), the means 10 to 55 by 0.25, the grid
−30 to 100 of 260 001 points (M25b.27); the resistors with the colleague's check of 200 tables drawn with the seed 6066
(M25b.28); 40 random mixtures (dimension 1 to 5, 2 to 4 components, 200 data) drawn with the seed 6061 (M25b.29); three
regimes of a probe, 600 training and 400 test measures drawn with the seeds 6062 and 6070 (and seed + 1 + k for the
regime k), the fit seed 6080 (M25b.30).
Seeds 6051 to 6089 only (the tests use 5950 to 6016, the figures of the fiche 6041 to 6046): those of the statements
(6054, 6056 to 6062, 6063 to 6065, 6066, 6070 to 6073, 6080), and, for the hidden cases of the check cells, 6068 (the
corrected functions of M25b.28), 6069 and 6081 (the mixtures and the draws of the property test of M25b.29), 6075 to
6078 (another mixture of three regimes, M25b.30); the 🔨 are checked by their tests. The check cells use their own data
(random mixtures in dimension 1 to 5, points far from every component, another bimodal mixture 0.6 N(18, 4) +
0.4 N(37, 6.25) for M25b.27, another mixture of three regimes for M25b.30), never the test cases of
tests/test_m25b_latent.py nor the examples of the docstrings of the stubs latent, gaussian and approx (no measurements
(0.5, 2, 3.5, 6) with the weights (0.4, 0.6), the means 1 and 5 and the variances 1 and 2, no point 1000, no points
(0, 0), (1, 0), (0, 2), (4, 4), (5, 3), no reg = 0.1 on them), nor the examples of the fiche (no station π = (1/4, 3/4),
N(11, 4), N(3, 9), x = 8 or 250 °C, no mornings 2, 5, 8, 12, 13 °C, no boiler, no plots w = (3, 2), σ² = 2, no
eigenvalues 27, 18, 3, 1, no line (1, 4, 0), no bulb, no binary code (0.7, 0.3)), nor those of M25a.

Nothing of workbookIA 25 is used (the notes of M25b in the syllabus and their list « Évités »): no encoder, decoder,
network, image nor VAE; no KL against N(0, 1), N(0, I) or N(0, τ²), no log-variance, no σ ⊙ ε, no β; no angle between a
fitted W and the subspace of the PCA, no subspace_angles_deg_23 nor its checks (the plane z = 0 tilted by 30°); none of
the numbers of its exercises. The bug (1) of M25b.28 computes the responsibilities with the densities (0/0 far away),
(2) divides the variances of the M step by n, (3) forgets the entropy of q in the ELBO: three functions in dimension 1
(x, weights, means, sds), never a network. The property test of M25b.29 counts its failures and is run on the M step of
the reference, on the wrong M step of the statement (the means divided by n) and on hidden wrong ones (covariances twice
too large, reg = 0.1). The check of M25b.30 compares the fit to the exact model, then fits another mixture.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, check_unique_keys, guarded,  # noqa: E402,F401
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M25b"
FOLDER = "chapitres/m25b_variables_latentes"

SHAPE = 'a shape: a tuple (7, 2) or a text "(7, 2)"'
FRACTION = 'an irreducible fraction, as text "p/q"'
EXACT = 'an exact value, as text, with sqrt, pi, ln, exp and fractions'
BOOL = "True or False"


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M25b.1", "Trois machines, des tiges de longueurs gaussiennes : tirage ancestral, vraisemblance marginale et "
          "posterior de la machine", [
              ("a", "a list of 2 numbers: the number of the machine, then the length (mm)",
               "[MACHINE_1, float(MU_1[MACHINE_1 - 1] + SD_1[MACHINE_1 - 1] * EPS_1)]",
               '''decimals=1,
           mistakes={"la machine se lit sur les probabilités cumulées 0,5 ; 0,8 ; 1, dans l'ordre des machines":
                         [1, float(MU_1[0] + SD_1[0] * EPS_1)],
                     "une longueur tirée vaut μ_z + σ_z ε : ε est négatif ici":
                         [MACHINE_1, float(MU_1[MACHINE_1 - 1] - SD_1[MACHINE_1 - 1] * EPS_1)]}'''),
              ("b", "a number (4 decimals)", "P_1",
               '''decimals=4,
           mistakes={"la vraisemblance marginale pondère chaque densité par la proportion de sa machine":
                         float(DENS_1.sum()),
                     "p(x) est la somme des trois termes π_k N(x | μ_k, σ_k²), pas le plus grand": float(JOINT_1.max()),
                     "la densité de N(μ, σ²) divise par σ√(2π), avec l'écart-type de chaque machine":
                         float(np.sum(PI_1 * np.exp(-(X_1 - MU_1) ** 2 / (2 * SD_1 ** 2)) / math.sqrt(2 * math.pi)))}'''),
              ("c", "a list of 3 numbers (3 decimals)", "POST_1.tolist()",
               '''decimals=3,
           mistakes={"le posterior multiplie chaque densité par la proportion de sa machine avant de normaliser":
                         EQUAL_1.tolist(),
                     "un posterior est une loi : ses trois probabilités ont pour somme 1": JOINT_1.tolist(),
                     "une densité gaussienne contient (x − μ)²/(2σ²), avec le carré de l'écart-type":
                         normalized(PI_1 * np.exp(-(X_1 - MU_1) ** 2 / (2 * SD_1)) / (SD_1 * math.sqrt(2 * math.pi)))}'''),
              ("d", "an integer", "int(np.argmax(POST_1)) + 1",
               '''mistakes={"la machine la plus probable est celle de plus grande probabilité a posteriori, pas celle de la "
                     "moyenne la plus proche": int(np.argmin(np.abs(X_1 - MU_1))) + 1}'''),
              ("e", BOOL, "bool(np.argmin(np.abs(X_1 - MU_1)) == np.argmax(POST_1))",
               '''mistakes={"compare les probabilités a posteriori, pas les distances aux moyennes": True}'''),
              ("f", "a number (4 decimals)", "float(EQUAL_1[2])",
               '''decimals=4,
           mistakes={"avec des proportions égales, le posterior ne dépend plus que des densités": float(POST_1[2]),
                     "un posterior est une probabilité : les trois valeurs doivent avoir pour somme 1": float(DENS_1[2])}'''),
          ]),

    Paper("M25b.2", "Deux variétés de grains de café : moyenne et covariance du mélange, part entre variétés, "
          "corrélation du sac", [
              ("a", "a list of 2 numbers", "floats(MEAN_2)",
               '''decimals=4,
           mistakes={"la moyenne d'un mélange pondère chaque moyenne par la proportion de sa variété":
                         floats([(M_2[0][i] + M_2[1][i]) / 2 for i in range(2)])}'''),
              ("b", "a 2 × 2 matrix", "floats(WITHIN_2)",
               '''decimals=4,
           mistakes={"la covariance moyenne dans les variétés pondère chaque Σ_k par π_k":
                         floats([[(S_2[0][i][j] + S_2[1][i][j]) / 2 for j in range(2)] for i in range(2)])}'''),
              ("c", "a 2 × 2 matrix", "floats(BETWEEN_2)",
               '''decimals=4,
           mistakes={"chaque terme de la variance entre groupes est pondéré par π_k, pas par π_k²":
                         floats(between_2([p ** 2 for p in P_2])),
                     "la variance entre groupes mesure les écarts des moyennes à la moyenne du mélange, pondérés":
                         floats([[(M_2[0][i] - M_2[1][i]) * (M_2[0][j] - M_2[1][j]) for j in range(2)] for i in range(2)])}'''),
              ("d", "a 2 × 2 matrix", "floats(TOTAL_2)",
               '''decimals=4,
           mistakes={"la covariance d'un mélange ne se réduit pas à la moyenne des covariances des composantes (fiche §2)":
                         floats(WITHIN_2),
                     "Σ π_k(Σ_k + μ_k μ_kᵀ) est un moment d'ordre 2 autour de 0, pas une covariance": floats(SECOND_2)}'''),
              ("e", FRACTION, "str(BETWEEN_2[0][0] / TOTAL_2[0][0])",
               '''kind="fraction", simplified=True,
           mistakes={"la part se rapporte à la variance totale de la longueur": str(BETWEEN_2[0][0] / WITHIN_2[0][0]),
                     "la part demandée est celle de la variance entre les variétés": str(WITHIN_2[0][0] / TOTAL_2[0][0])}'''),
              ("f", "a number (4 decimals)", "float(TOTAL_2[0][1]) / math.sqrt(float(TOTAL_2[0][0] * TOTAL_2[1][1]))",
               '''decimals=4,
           mistakes={"une corrélation divise la covariance par le produit des deux écarts-types":
                         float(TOTAL_2[0][1] / (TOTAL_2[0][0] * TOTAL_2[1][1])),
                     "la corrélation du sac se lit sur la covariance du mélange, pas sur celles des variétés": 0.0}'''),
              ("g", BOOL, "bool(S_2[0][0][1] == 0 and S_2[1][0][1] == 0 and TOTAL_2[0][1] != 0)",
               '''mistakes={"compare les coefficients hors diagonale de Σ₁, de Σ₂ et de la covariance du mélange": False}'''),
          ]),

    Paper("M25b.3", "Deux séries de résistances : une itération de l'EM en log, et la log-vraisemblance qui monte", [
        ("a", "a list of 4 numbers (4 decimals)", "R_3[:, 0].tolist()",
         '''decimals=4,
           mistakes={"a_ik contient ln π_k : la proportion compte dans la responsabilité": NO_WEIGHTS_3[:, 0].tolist(),
                     "N(x | μ, σ²) se calcule avec la variance σ² de chaque série, pas avec l'écart-type σ":
                         WITH_SD_3[:, 0].tolist(),
                     "donne la responsabilité de la série 1 (moyenne 47 Ω), pas celle de la série 2": R_3[:, 1].tolist()}'''),
        ("b", "a list of 2 numbers (4 decimals)", "W1_3.tolist()",
         '''decimals=4,
           mistakes={"un poids est une proportion : les deux poids ont pour somme 1": N_3.tolist()}'''),
        ("c", "a list of 2 numbers (3 decimals)", "M1_3.tolist()",
         '''decimals=3,
           mistakes={"la moyenne pondérée divise par N_k, pas par n": (R_3 * X_3[:, None]).sum(axis=0) / len(X_3)}'''),
        ("d", "a list of 2 numbers (3 decimals)", "V1_3.tolist()",
         '''decimals=3,
           mistakes={"la variance du pas M se calcule avec la nouvelle moyenne": weighted_ss_3(MU_3) / N_3,
                     "le pas M divise par N_k (maximum de vraisemblance), pas par N_k − 1": weighted_ss_3(M1_3) / (N_3 - 1),
                     "la variance pondérée divise par N_k, pas par n": weighted_ss_3(M1_3) / len(X_3)}'''),
        ("e", "a number (4 decimals)", "LL0_3",
         '''decimals=4,
           mistakes={"le logarithme d'une somme n'est pas la somme des logarithmes": float(A_3.sum()),
                     "la log-vraisemblance garde toute la somme sur les composantes (log-sum-exp), pas le plus grand "
                     "terme": float(A_3.max(axis=1).sum())}'''),
        ("f", "a number (4 decimals)", "LL1_3",
         '''decimals=4,
           mistakes={"après le pas M, tous les paramètres changent, y compris les poids":
                         float(row_lse(np.log(PI_3) + log_normal(X_3[:, None], M1_3, V1_3)).sum())}'''),
        ("g", BOOL, "bool(LL1_3 > LL0_3)",
         '''mistakes={"compare tes deux log-vraisemblances, e) et f)": False}'''),
    ]),

    Paper("M25b.6", "Une sonde de qualité de l'eau : ln p(x), l'ELBO pour trois lois q et l'écart égal à la KL", [
        ("a", "a number (4 decimals)", "LP_6",
         '''decimals=4,
           mistakes={"p(x) somme les deux termes π_k N(x | μ_k, σ_k²), pas le plus grand": float(A_6.max()),
                     "p(x) pondère chaque densité par la probabilité a priori de l'état":
                         float(np.log(np.exp(log_normal(X_6, MU_6, VAR_6)).sum())),
                     "le second paramètre de N(1 ; 0,25) est la variance σ², pas l'écart-type σ":
                         float(lse(np.log(PRIOR_6) + log_normal(X_6, MU_6, np.sqrt(VAR_6))))}'''),
        ("b", "a number (3 decimals)", "float(POST_6[1])",
         '''decimals=3,
           mistakes={"le posterior multiplie la densité par la probabilité a priori de l'état":
                         float(normalized(np.exp(log_normal(X_6, MU_6, VAR_6)))[1]),
                     "la question demande la probabilité de l'état pollué (z = 2)": float(POST_6[0])}'''),
        ("c", "a number (4 decimals)", "elbo_6([0.5, 0.5])",
         '''decimals=4,
           mistakes={"l'ELBO retranche E_q[ln q] : n'oublie pas ce terme": float(np.sum(0.5 * A_6)),
                     "l'ELBO retranche E_q[ln q], elle ne l'ajoute pas": float(np.sum(0.5 * (A_6 + np.log(0.5))))}'''),
        ("d", "a number (4 decimals)", "elbo_6([0.6, 0.4])",
         '''decimals=4,
           mistakes={"l'ELBO retranche E_q[ln q] : n'oublie pas ce terme": float(np.sum(np.array([0.6, 0.4]) * A_6)),
                     "q(z = 1) = 0,6 multiplie le terme de l'état conforme": elbo_6([0.4, 0.6])}'''),
        ("e", "a number (4 decimals)", "elbo_6(POST_6)",
         '''decimals=4,
           mistakes={"au posterior aussi, l'ELBO retranche E_q[ln q]": float(np.sum(POST_6 * A_6))}'''),
        ("f", "a number (4 decimals)", "kl_6([0.5, 0.5], POST_6)",
         '''decimals=4,
           mistakes={"l'écart est KL(q ‖ p(z | x)), q en premier": kl_6(POST_6, [0.5, 0.5]),
                     "l'écart compare q au posterior, pas au prior": kl_6([0.5, 0.5], PRIOR_6)}'''),
        ("g", BOOL, "bool(abs(elbo_6([0.5, 0.5]) + kl_6([0.5, 0.5], POST_6) - LP_6) < 1e-12)",
         '''mistakes={"vérifie avec tes valeurs non arrondies": False}'''),
    ]),

    Paper("M25b.9", "Trois épreuves d'un concours, une aptitude cachée : l'ACP probabiliste à un facteur", [
        ("a", "a 3 × 3 matrix", "floats(C_9)",
         '''decimals=4,
           mistakes={"le bruit ε ajoute sa covariance à celle de wz": floats(np.outer(W_9, W_9)),
                     "le bruit est indépendant d'une épreuve à l'autre : sa covariance est σ²I":
                         floats(np.outer(W_9, W_9) + S2_9)}'''),
        ("b", "a number", "float(M_9)",
         '''decimals=4, mistakes={"M contient aussi le bruit σ²": float(W_9 @ W_9)}'''),
        ("c", "a list of 3 numbers (4 decimals)", "floats(W_9 / M_9)",
         '''decimals=4,
           mistakes={"l'a priori tire z vers 0 : la règle n'est pas la projection orthogonale de M12d":
                         floats(W_9 / (W_9 @ W_9))}'''),
        ("d", "a list of 2 numbers (4 decimals)", "[float(W_9 @ (XA_9 - MU_9) / M_9), S2_9 / M_9]",
         '''decimals=4,
           mistakes={"la règle affine s'applique à x − μ, pas aux notes brutes": [float(W_9 @ XA_9 / M_9), S2_9 / M_9],
                     "la variance a posteriori contient le bruit σ²": [float(W_9 @ (XA_9 - MU_9) / M_9), 1 / M_9],
                     "l'a priori tire z vers 0 : la moyenne a posteriori est plus petite que la coordonnée de la "
                     "projection orthogonale": [float(W_9 @ (XA_9 - MU_9) / (W_9 @ W_9)), S2_9 / M_9]}'''),
        ("e", BOOL, "True",
         '''mistakes={"regarde de quoi dépend la covariance a posteriori": False}'''),
        ("f", "a number", "float(LAMBDA_9[1:].mean())",
         '''decimals=4,
           mistakes={"σ̂² est la moyenne des valeurs propres écartées seulement": float(LAMBDA_9.mean()),
                     "σ̂² est la moyenne des d − k valeurs propres écartées, pas la plus petite": float(LAMBDA_9[-1])}'''),
        ("g", "a number", "float(LAMBDA_9[0] - LAMBDA_9[1:].mean())",
         '''decimals=4,
           mistakes={"dans la direction gardée, une part de la variance revient au bruit": float(LAMBDA_9[0])}'''),
        ("h", "a list of 2 numbers", "floats(np.maximum(LAMBDA_9[:2] - KNOWN_9, 0))",
         '''decimals=4,
           mistakes={"un carré de norme n'est jamais négatif": floats(LAMBDA_9[:2] - KNOWN_9),
                     "le bruit connu prend sa part de chaque valeur propre": floats(LAMBDA_9[:2])}'''),
        ("i", BOOL, "bool(LAMBDA_9[1] <= KNOWN_9)",
         '''mistakes={"compare λ₂ et le bruit connu σ²": False}'''),
    ]),

    Paper("M25b.10", "Les angles principaux entre deux plans de ℝ⁴ et entre deux droites de ℝ³", [
        ("a", "a 4 × 2 matrix (4 decimals)", "floats(QA_10)",
         '''decimals=4,
           mistakes={"Gram-Schmidt retire de a₂ sa projection sur q₁ avant de normaliser":
                         floats(np.column_stack([A1_10 / np.linalg.norm(A1_10), A2_10 / np.linalg.norm(A2_10)]))}'''),
        ("b", "a 4 × 2 matrix (4 decimals)", "floats(QB_10)",
         '''decimals=4,
           mistakes={"les colonnes de Q_B forment une base orthonormée : vérifie leur produit scalaire": floats(NORMED_B_10)}'''),
        ("c", "a 2 × 2 matrix (4 decimals)", "floats(M_10)",
         '''decimals=4,
           mistakes={"l'ordre compte : la ligne i de Q_Aᵀ Q_B correspond à la colonne i de Q_A": floats(M_10.T)}'''),
        ("d", "a list of 2 numbers (4 decimals)", "floats(SV_10)",
         '''decimals=4,
           mistakes={"les valeurs singulières de M sont des longueurs, pas leurs carrés": floats(SV_10 ** 2)}'''),
        ("e", "a list of 2 numbers (2 decimals)", "floats(np.degrees(np.arccos(SV_10)))",
         '''decimals=2,
           mistakes={"la question demande des degrés": floats(np.arccos(SV_10)),
                     "les angles se rangent du plus petit au plus grand, φ₁ ≤ φ₂": floats(np.degrees(np.arccos(SV_10))[::-1])}'''),
        ("f", "a number (2 decimals)", "math.degrees(math.acos(abs(COS_LINES_10)))",
         '''decimals=2,
           mistakes={"un angle principal est dans [0°, 90°] : une droite n'a pas de sens de parcours":
                         math.degrees(math.acos(COS_LINES_10)),
                     "la question demande des degrés": math.acos(abs(COS_LINES_10))}'''),
        ("g", BOOL, "bool(np.allclose(np.linalg.svd(QA_10.T @ NORMED_B_10, compute_uv=False), SV_10))",
         '''mistakes={"des vecteurs seulement normés ne forment une base orthonormée que s'ils sont orthogonaux": True}'''),
    ]),

    Paper("M25b.12", "Le coût d'un stock face à une demande gaussienne : E[(D − c)⁺] et ses dérivées par le chemin", [
        ("a", "a number (2 decimals)", "SD_12 * PHI_DENS_12 - (C_12 - MU_12) * (1 - PHI_CDF_12)",
         '''decimals=2,
           mistakes={"sur {D > c}, D − c = σ(ε − z) : vérifie le signe du terme en z":
                         SD_12 * PHI_DENS_12 + (C_12 - MU_12) * (1 - PHI_CDF_12),
                     "(D − c)⁺ = max(D − c, 0) : la partie où D < c compte pour 0, pas pour D − c": MU_12 - C_12,
                     "le changement de variable d = μ + σε fait sortir l'écart-type σ, pas la variance":
                         SD_12 ** 2 * PHI_DENS_12 - (C_12 - MU_12) * (1 - PHI_CDF_12)}'''),
        ("b", "a number (4 decimals)", "1 - PHI_CDF_12",
         '''decimals=4,
           mistakes={"la demande non servie ne bouge avec μ que si la demande dépasse le stock : c'est la queue de "
                     "droite": PHI_CDF_12}'''),
        ("c", "a number (4 decimals)", "PHI_DENS_12",
         '''decimals=4,
           mistakes={"en σ, le chemin μ + σε se dérive en ε : l'estimateur n'est pas celui de la dérivée en μ":
                         1 - PHI_CDF_12,
                     "N(c | μ, σ²) contient déjà le facteur 1/σ : vérifie ce que tu multiplies par σ": PHI_DENS_12 / SD_12}'''),
        ("d", "a list of 2 numbers", "pathwise_12(1.2)",
         '''decimals=1,
           mistakes={"compare la demande μ + σε au stock c pour ce tirage": [0.0, 0.0],
                     "l'estimateur de la dérivée en σ multiplie l'indicatrice par ε": [1.0, 1.0]}'''),
        ("e", "a list of 2 numbers", "pathwise_12(0.1)",
         '''decimals=1,
           mistakes={"compare la demande μ + σε au stock c pour ce tirage": [1.0, 0.1]}'''),
        ("f", "a number (4 decimals)", "(1 - PHI_CDF_12) * PHI_CDF_12",
         '''decimals=4,
           mistakes={"une variance retranche le carré de l'espérance": 1 - PHI_CDF_12,
                     "(E[ĝ])² n'est qu'une partie de la variance : il manque E[ĝ²]": (1 - PHI_CDF_12) ** 2}'''),
        ("g", "a number (4 decimals)", "-(1 - PHI_CDF_12)",
         '''decimals=4,
           mistakes={"un stock plus grand fait baisser la demande non servie": 1 - PHI_CDF_12}'''),
    ]),

    Paper("M25b.13", "Une seule gaussienne pour les temps de trajet par deux itinéraires : les deux sens de la KL", [
        ("a", "a list of 2 numbers", "[MEAN_13, VAR_13]",
         '''decimals=4,
           mistakes={"la variance d'un mélange ne se réduit pas à la moyenne des variances des composantes":
                         [MEAN_13, float(W_13 @ V_13)],
                     "la moyenne du mélange pondère par les proportions des itinéraires": [float(M_13.mean()), VAR_13]}'''),
        ("b", "a number (2 decimals)", "Q_STAR_AT_13 / P_AT_13",
         '''decimals=2, mistakes={"le rapport demandé met q⋆ au numérateur": P_AT_13 / Q_STAR_AT_13}'''),
        ("c", EXACT, 'f"ln({1 / Fraction(7, 10)})"',
         '''kind="exact",
           mistakes={"une KL est positive ou nulle": f"ln({Fraction(7, 10)})",
                     "q₁ est la gaussienne de la rocade, q₂ celle du centre-ville : vérifie l'itinéraire":
                         f"ln({1 / Fraction(3, 10)})"}'''),
        ("d", EXACT, 'f"ln({1 / Fraction(3, 10)})"',
         '''kind="exact", mistakes={"une KL est positive ou nulle": f"ln({Fraction(3, 10)})"}'''),
        ("e", "an integer", "1 + int(np.argmin([math.log(1 / 0.7), math.log(1 / 0.3)]))",
         '''mistakes={"le minimum global est le plus bas des minima locaux": 2}'''),
        ("f", "a number (4 decimals)", "expected_log_normal_13(22.0, 4.0)",
         '''decimals=4,
           mistakes={"E_p[(X − 22)²] = variance de p + (moyenne de p − 22)²": -0.5 * math.log(2 * math.pi * 4.0) - VAR_13 / 8,
                     "−ln q₁(x) contient ½ ln(2π · 4), avec la variance de q₁":
                         -0.5 * math.log(2 * math.pi * 2.0) - (VAR_13 + (MEAN_13 - 22.0) ** 2) / 8}'''),
        ("g", "a number (4 decimals)", "expected_log_normal_13(MEAN_13, VAR_13)",
         '''decimals=4,
           mistakes={"−ln q⋆(x) contient aussi (x − m)²/(2s²), dont l'espérance sous p n'est pas nulle":
                         -0.5 * math.log(2 * math.pi * VAR_13)}'''),
        ("h", BOOL, "bool(expected_log_normal_13(MEAN_13, VAR_13) - expected_log_normal_13(22.0, 4.0) > 10)",
         '''mistakes={"KL(p ‖ q) = −h(p) − E_p[ln q], et h(p) ne dépend pas de q": False}'''),
    ]),

    Paper("M25b.14", "Un code stochastique d'une source à trois symboles : posterior agrégé, information mutuelle, code "
          "effondré", [
              ("a", "a list of 2 numbers (4 decimals)", "floats(QZ_14)",
               '''decimals=4,
           mistakes={"le posterior agrégé pondère chaque ligne q(z | x) par p(x)":
                         floats([sum(Q_14[i][k] for i in range(3)) / 3 for k in range(2)])}'''),
              ("b", "a list of 3 numbers (4 decimals)", "KLS_14",
               '''decimals=4,
           mistakes={"la KL au prior met q(· | x) en premier : KL(q(· | x) ‖ p(z))":
                         [kl_14(PZ_14, Q_14[i]) for i in range(3)]}'''),
              ("c", "a number (4 decimals)", "AVERAGE_14",
               '''decimals=4, mistakes={"la moyenne sur les symboles est pondérée par p(x)": sum(KLS_14) / 3}'''),
              ("d", "a number (4 decimals)", "INFO_14",
               '''decimals=4,
           mistakes={"l'information mutuelle compare q(z | x) à la marge q(z), pas au prior": AVERAGE_14,
                     "I(X ; Z) pondère chaque terme par la probabilité jointe p(x) q(z | x)":
                         sum(kl_14(Q_14[i], QZ_14) for i in range(3))}'''),
              ("e", "a number (4 decimals)", "kl_14(QZ_14, PZ_14)",
               '''decimals=4,
           mistakes={"la KL du posterior agrégé au prior met q(z) en premier": kl_14(PZ_14, QZ_14)}'''),
              ("f", BOOL, "bool(abs(AVERAGE_14 - INFO_14 - kl_14(QZ_14, PZ_14)) < 1e-12)",
               '''mistakes={"vérifie c) = d) + e) avec tes valeurs non arrondies": False}'''),
              ("g", "a list of 2 numbers", "[0, 0]",
               '''mistakes={"si q(z | x) ne dépend pas de x, le code ne transmet aucune information sur la source":
                         [0, INFO_14]}'''),
              ("h", BOOL, "True",
               '''mistakes={"relis la propriété du posterior agrégé (fiche §8)": False}'''),
          ]),

    Paper("M25b.23", "Pont : l'ELBO de mesures rangées en lignes, « reconstruction moins KL au prior », en nats par "
          "mesure", [
              ("a", SHAPE, "shape_of(LOG_DENS_23)",
               '''mistakes={"dans les bibliothèques, les mesures sont les lignes": shape_of(LOG_DENS_23.T)}'''),
              ("b", "a number (4 decimals)", "terms_23(R_23)[0] / N_23",
               '''decimals=4,
           mistakes={"en nats par mesure : divise la somme par n": terms_23(R_23)[0],
                     "la reconstruction est une moyenne sous q_i (les lignes de R), pas sous le prior":
                         float(np.sum(PI_23 * LOG_DENS_23)) / N_23}'''),
              ("c", "a number (4 decimals)", "terms_23(R_23)[1] / N_23",
               '''decimals=4,
           mistakes={"en nats par mesure : divise la somme par n": terms_23(R_23)[1],
                     "la KL au prior met q_i en premier : KL(q_i ‖ π)": float(np.sum(PI_23 * np.log(PI_23 / R_23))) / N_23}'''),
              ("d", "a number (4 decimals)", "(terms_23(R_23)[0] - terms_23(R_23)[1]) / N_23",
               '''decimals=4,
           mistakes={"l'ELBO retranche la KL au prior": (terms_23(R_23)[0] + terms_23(R_23)[1]) / N_23,
                     "par mesure : divise par n (le nombre de lignes) seulement":
                         (terms_23(R_23)[0] - terms_23(R_23)[1]) / (2 * N_23)}'''),
              ("e", "a list of 3 numbers (3 decimals)", "POST_23[:, 0].tolist()",
               '''decimals=3,
           mistakes={"la responsabilité contient le poids π_k": normalized_rows(np.exp(LOG_DENS_23))[:, 0].tolist()}'''),
              ("f", "a list of 2 numbers (4 decimals)", "[terms_23(POST_23)[0] / N_23, terms_23(POST_23)[1] / N_23]",
               '''decimals=4, mistakes={"en nats par mesure : divise par n": list(terms_23(POST_23))}'''),
              ("g", "a number (4 decimals)", "(terms_23(POST_23)[0] - terms_23(POST_23)[1]) / N_23",
               '''decimals=4,
           mistakes={"en nats par mesure : divise par n": terms_23(POST_23)[0] - terms_23(POST_23)[1]}'''),
              ("h", BOOL, "bool(terms_23(POST_23)[0] > terms_23(R_23)[0] and terms_23(POST_23)[1] > terms_23(R_23)[1])",
               '''mistakes={"compare f) à b) et à c), terme par terme": False}'''),
          ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (exact fractions for M25b.2 and M25b.14, NumPy for the rest)
import math
from fractions import Fraction

import numpy as np


def floats(values):
    """A vector or a matrix of exact values (fractions, floats) as nested lists of floats."""
    return np.asarray(values, dtype=float).tolist()


def shape_of(shape):
    """A shape (a tuple, or that of an array) written as NumPy prints it: "(3, 4)"."""
    shape = np.shape(shape) if hasattr(shape, "shape") else shape
    return str(tuple(int(n) for n in shape))


def normalized(values):
    """Values divided by their sum, as a list of floats."""
    values = np.asarray(values, dtype=float)
    return (values / values.sum()).tolist()


def normalized_rows(table):
    """Each row of a table divided by its sum."""
    table = np.asarray(table, dtype=float)
    return table / table.sum(axis=1, keepdims=True)


def log_normal(x, mean, var):
    """ln N(x | mean, var) in dimension 1, with the VARIANCE var (the formula of the fiche)."""
    return -0.5 * np.log(2 * np.pi * var) - (x - mean) ** 2 / (2 * var)


def lse(a):
    """The stable log-sum-exp of a vector (M05a): the maximum factored out."""
    a = np.asarray(a, dtype=float)
    m = a.max()
    return float(m + np.log(np.sum(np.exp(a - m))))


def row_lse(a):
    """The stable log-sum-exp of each row of an (n, K) table."""
    m = a.max(axis=1, keepdims=True)
    return (m + np.log(np.exp(a - m).sum(axis=1, keepdims=True)))[:, 0]


PI_1, MU_1, SD_1 = np.array([0.5, 0.3, 0.2]), np.array([100.0, 102.0, 97.0]), np.array([1.0, 1.0, 2.0])   # M25b.1
X_1, U_1, EPS_1 = 98.2, 0.62, -1.3
MACHINE_1 = 1 + int(U_1 >= 0.5) + int(U_1 >= 0.8)            # 1 if u < 0.5, 2 if 0.5 <= u < 0.8, 3 otherwise
DENS_1 = np.exp(-(X_1 - MU_1) ** 2 / (2 * SD_1 ** 2)) / (SD_1 * math.sqrt(2 * math.pi))
JOINT_1 = PI_1 * DENS_1
P_1 = float(JOINT_1.sum())
POST_1 = JOINT_1 / P_1
EQUAL_1 = DENS_1 / DENS_1.sum()                               # equal proportions: the densities alone
P_2 = [Fraction(3, 5), Fraction(2, 5)]                        # M25b.2
M_2 = [[Fraction(10), Fraction(7)], [Fraction(12), Fraction(8)]]
S_2 = [[[Fraction(1), Fraction(0)], [Fraction(0), Fraction(2, 5)]],
       [[Fraction(3, 2), Fraction(0)], [Fraction(0), Fraction(3, 10)]]]
MEAN_2 = [sum(P_2[k] * M_2[k][i] for k in range(2)) for i in range(2)]
WITHIN_2 = [[sum(P_2[k] * S_2[k][i][j] for k in range(2)) for j in range(2)] for i in range(2)]


def between_2(weights):
    """Σ_k weights_k (μ_k − μ)(μ_k − μ)ᵀ, exact."""
    return [[sum(weights[k] * (M_2[k][i] - MEAN_2[i]) * (M_2[k][j] - MEAN_2[j]) for k in range(2)) for j in range(2)]
            for i in range(2)]


BETWEEN_2 = between_2(P_2)
TOTAL_2 = [[WITHIN_2[i][j] + BETWEEN_2[i][j] for j in range(2)] for i in range(2)]
SECOND_2 = [[sum(P_2[k] * (S_2[k][i][j] + M_2[k][i] * M_2[k][j]) for k in range(2)) for j in range(2)] for i in range(2)]
assert all(SECOND_2[i][j] - MEAN_2[i] * MEAN_2[j] == TOTAL_2[i][j] for i in range(2) for j in range(2))
X_3 = np.array([46.0, 48.0, 49.4, 52.1])                      # M25b.3
PI_3, MU_3, VAR_3 = np.array([0.45, 0.55]), np.array([47.0, 51.0]), np.array([1.0, 2.5])
A_3 = np.log(PI_3) + log_normal(X_3[:, None], MU_3, VAR_3)    # a_ik, an (4, 2) table
LSE_3 = row_lse(A_3)
R_3 = np.exp(A_3 - LSE_3[:, None])
NO_WEIGHTS_3 = np.exp(log_normal(X_3[:, None], MU_3, VAR_3) - row_lse(log_normal(X_3[:, None], MU_3, VAR_3))[:, None])
WITH_SD_3 = np.exp((np.log(PI_3) + log_normal(X_3[:, None], MU_3, np.sqrt(VAR_3)))
                   - row_lse(np.log(PI_3) + log_normal(X_3[:, None], MU_3, np.sqrt(VAR_3)))[:, None])
N_3 = R_3.sum(axis=0)
W1_3 = N_3 / len(X_3)
M1_3 = (R_3 * X_3[:, None]).sum(axis=0) / N_3


def weighted_ss_3(means):
    """Σ_i r_ik (x_i − m_k)² for each component."""
    return (R_3 * (X_3[:, None] - means) ** 2).sum(axis=0)


V1_3 = weighted_ss_3(M1_3) / N_3
LL0_3 = float(LSE_3.sum())
LL1_3 = float(row_lse(np.log(W1_3) + log_normal(X_3[:, None], M1_3, V1_3)).sum())
PRIOR_6, MU_6, VAR_6, X_6 = np.array([0.9, 0.1]), np.array([1.0, 3.0]), np.array([0.25, 1.0]), 2.0   # M25b.6
A_6 = np.log(PRIOR_6) + log_normal(X_6, MU_6, VAR_6)
LP_6 = lse(A_6)
POST_6 = np.exp(A_6 - LP_6)


def elbo_6(q):
    """Σ_z q(z) (ln p(x, z) − ln q(z))."""
    q = np.asarray(q, dtype=float)
    return float(np.sum(q * (A_6 - np.log(q))))


def kl_6(p, q):
    """KL(p ‖ q) of two laws on the two states, in nats."""
    p, q = np.asarray(p, dtype=float), np.asarray(q, dtype=float)
    return float(np.sum(p * np.log(p / q)))


W_9, S2_9, MU_9 = np.array([2.0, 1.0, 2.0]), 3.0, np.array([12.0, 11.0, 13.0])   # M25b.9
C_9 = np.outer(W_9, W_9) + S2_9 * np.eye(3)
M_9 = float(W_9 @ W_9 + S2_9)
XA_9 = np.array([15.0, 12.0, 15.0])
LAMBDA_9, KNOWN_9 = np.array([14.0, 4.5, 2.5]), 5.0
A1_10, A2_10 = np.array([1.0, 2.0, 0.0, 0.0]), np.array([2.0, 1.0, 0.0, 0.0])   # M25b.10
B1_10, B2_10 = np.array([12.0, 0.0, 5.0, 0.0]), np.array([12.0, 7.0, 5.0, 24.0])


def gram_schmidt_10(v1, v2):
    """The orthonormal basis (q1, q2) of Gram-Schmidt, as the two columns of a matrix."""
    q1 = v1 / np.linalg.norm(v1)
    u = v2 - (v2 @ q1) * q1
    return np.column_stack([q1, u / np.linalg.norm(u)])


QA_10, QB_10 = gram_schmidt_10(A1_10, A2_10), gram_schmidt_10(B1_10, B2_10)
NORMED_B_10 = np.column_stack([B1_10 / np.linalg.norm(B1_10), B2_10 / np.linalg.norm(B2_10)])
M_10 = QA_10.T @ QB_10
SV_10 = np.sort(np.sqrt(np.linalg.eigvalsh(M_10.T @ M_10)))[::-1]       # the singular values, by MᵀM
U_10, V_10 = np.array([1.0, 4.0, 8.0]), np.array([-4.0, -8.0, 1.0])
COS_LINES_10 = float(U_10 @ V_10 / (np.linalg.norm(U_10) * np.linalg.norm(V_10)))
MU_12, SD_12, C_12 = 240.0, 40.0, 252.0                      # M25b.12
Z_12 = (C_12 - MU_12) / SD_12
PHI_DENS_12 = math.exp(-Z_12 ** 2 / 2) / math.sqrt(2 * math.pi)
PHI_CDF_12 = 0.5 * (1 + math.erf(Z_12 / math.sqrt(2)))


def pathwise_12(eps):
    """The one-draw estimates of the derivatives in μ and in σ: 1{D > c} and 1{D > c} ε, with D = μ + σε."""
    above = float(MU_12 + SD_12 * eps > C_12)
    return [above, above * eps]


W_13, M_13, V_13 = np.array([0.7, 0.3]), np.array([22.0, 40.0]), np.array([4.0, 6.25])   # M25b.13
MEAN_13 = float(W_13 @ M_13)
VAR_13 = float(W_13 @ V_13 + W_13 @ (M_13 - MEAN_13) ** 2)
P_AT_13 = float(W_13 @ np.exp(log_normal(MEAN_13, M_13, V_13)))
Q_STAR_AT_13 = 1 / math.sqrt(2 * math.pi * VAR_13)


def expected_log_normal_13(m, s2):
    """E_p[ln N(X | m, s2)] = −½ ln(2π s2) − (V_p + (E_p X − m)²) / (2 s2)."""
    return -0.5 * math.log(2 * math.pi * s2) - (VAR_13 + (MEAN_13 - m) ** 2) / (2 * s2)


PX_14 = [Fraction(1, 2), Fraction(3, 10), Fraction(1, 5)]   # M25b.14
Q_14 = [[Fraction(17, 20), Fraction(3, 20)], [Fraction(7, 20), Fraction(13, 20)], [Fraction(3, 20), Fraction(17, 20)]]
PZ_14 = [Fraction(4, 5), Fraction(1, 5)]
QZ_14 = [sum(PX_14[i] * Q_14[i][k] for i in range(3)) for k in range(2)]


def kl_14(p, q):
    """KL(p ‖ q) of two laws on z, in nats."""
    return sum(float(p[k]) * math.log(p[k] / q[k]) for k in range(2))


KLS_14 = [kl_14(Q_14[i], PZ_14) for i in range(3)]
AVERAGE_14 = sum(float(PX_14[i]) * KLS_14[i] for i in range(3))
INFO_14 = sum(float(PX_14[i] * Q_14[i][k]) * math.log(Q_14[i][k] / QZ_14[k]) for i in range(3) for k in range(2))
PI_23, MU_23, VAR_23 = np.array([0.75, 0.25]), np.array([10.0, 14.0]), np.array([1.0, 2.25])   # M25b.23
X_23 = np.array([[9.2], [11.6], [13.4]])
R_23 = np.array([[0.85, 0.15], [0.5, 0.5], [0.3, 0.7]])
N_23 = len(X_23)
LOG_DENS_23 = log_normal(X_23, MU_23, VAR_23)                 # ln N(x_i | μ_k, σ_k²), one row per measurement
POST_23 = normalized_rows(PI_23 * np.exp(LOG_DENS_23))


def terms_23(R):
    """(reconstruction, KL to the prior), summed over the measurements: Σ r ln N and Σ_i KL(q_i ‖ π)."""
    return float(np.sum(R * LOG_DENS_23)), float(np.sum(R * np.log(R / PI_23)))'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M25b.1, M25b.2, M25b.3, M25b.6, M25b.9, M25b.10, "
               "M25b.12, M25b.13, M25b.14 ; 🔗 M25b.23)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md` (le 🔗 M25b.23 après le 🔨 M25b.22). Reporte ensuite chaque réponse ici : "
               "**la valeur** que tu as trouvée, sous la forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une liste `[0.2, -1]` ; une matrice comme la liste de ses **lignes**, `[[1, 0], [-2, 3]]` ;\n"
               "- une fraction irréductible entre guillemets, `\"3/7\"`, quand la question le dit ;\n"
               "- une valeur exacte entre guillemets, écrite avec des entiers, des fractions, `sqrt`, `pi`, `ln` et "
               "`exp`, comme `\"ln(5/2)\"` ;\n"
               "- une **forme** comme un tuple, `(7, 2)`, ou comme un texte, `\"(7, 2)\"` ;\n"
               "- `True` ou `False` pour un vrai ou faux.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")
