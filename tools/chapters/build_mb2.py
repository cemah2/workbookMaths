#!/usr/bin/env python
"""Build the two notebooks of chapter MB2 from a single source (used by Claude).

    python tools/chapters/build_mb2.py
    python tools/run_all_notebooks.py chapitres/mb2_cooccurrences/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/mb2_cooccurrences/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ MB2.1 to MB2.7 and 🔗 MB2.11), each answer computed in the notebook from the data of
its statement (exact fractions and integer arithmetic where the calculation is exact; math and NumPy otherwise), each
wrong value computed by the error its message names; parts A to D are the notebook exercises (MB2.13 to MB2.19), exactly
as 02_exercices.md describes them. Wrong-answer messages state a rule, never a number of the answer, the last step that
gives it, nor another sub-question.

Data. The notebook exercises take the data of the paper exercises (a data cell of part A: the birds of MB2.2, the shops of
MB2.4, the animals of MB2.7), the settings of their own statements and their own random draws. Seeds 7101 to 7149 only
(the tests use 7000 to 7090, the figures of the fiche 7091 to 7099): 7115 (🔮 MB2.15) and 7118 (🛠️ MB2.18) in the
statements; 7119 (the counts of 🏆 MB2.19, drawn at build time: only the counts are written); 7131 to 7133 (the hidden
calls of MB2.15), 7141 and 7142 (the hidden starts of MB2.18), 7143 to 7149 (the hidden tables of MB2.19, chosen and
calibrated at build time) in the check cells or here. The other hidden cases are drawn without a seed at each run (the
scale factors of 🐛 MB2.17, the new sales, the renumbering of the rows and columns of the hidden tables of MB2.19), or
written in their cell (the hidden table of 🎨 MB2.16, the hidden cases of MB2.17), computed at build time by private
functions of this script: none is the answer of a question. The check cells never hold the code that solves an exercise
nor a value that gives an answer without a calculation: the expected values are recorded by the solutions as hidden
sub-IDs and compared with ``wbm.check(..., computed=True)`` (the hidden calls of MB2.15 and MB2.16, the counters of the
hidden wrong versions of MB2.18, the five pairs of the table of MB2.19), given by properties (the PMI of a table of
counts does not change when the counts are multiplied by a same number; a removed direction leaves rows orthogonal to it
and removes a multiple of it), or computed at check time by the reference for hidden cases only (the five pairs of the
hidden tables of MB2.19, from their joint law). They use their own data, never the test cases of
tests/test_mb2_cooccurrence.py, the examples of the docstrings of the stub cooccurrence, the examples of the fiche, nor the
numbers of workbookIA B2 and B1 (the notes of MB2 in the syllabus and their list « Évités »).
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

CHAPTER = "MB2"
FOLDER = "chapitres/mb2_cooccurrences"

BOOL = "True or False"


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("MB2.1", "Des entiers en base 2 et en base 16 : conversions, une couleur #RRGGBB, les bits pour 5 000 codes, "
                   "et un mot de 16 bits découpé en deux champs", [
        ("a", "a text of 8 binary digits, between quotes", "to_base(214, 2)",
         '''mistakes={"les restes des divisions successives s'écrivent du dernier obtenu au premier":
                         to_base(214, 2)[::-1],
                     "on convertit le nombre 214 en entier, pas chacun de ses chiffres décimaux":
                         "".join(to_base(int(digit), 2).rjust(4, "0") for digit in "214"),
                     "écris seulement les chiffres, sans le préfixe 0b de Python": "0b" + to_base(214, 2)}'''),
        ("b", "a text of 2 hexadecimal digits, between quotes", "to_base(214, 16)",
         '''mistakes={"le quotient de la division par 16 donne le chiffre de gauche, le reste celui de droite":
                         to_base(214, 16)[::-1],
                     "au-delà de 9, un chiffre hexadécimal s'écrit avec une lettre : 10 s'écrit A, 15 s'écrit F":
                         "".join(str(int(digit, 16)) for digit in to_base(214, 16)),
                     "écris seulement les chiffres, sans le préfixe 0x de Python": "0x" + to_base(214, 16)}'''),
        ("c", "an integer", "from_base(BYTE_1, 2)",
         '''decimals=0,
           mistakes={"le chiffre de gauche est celui de poids fort, 2⁷ = 128": from_base(BYTE_1[::-1], 2),
                     "les deux groupes de 4 bits sont deux chiffres de base 16 : celui de gauche pèse 16 fois plus":
                         int(str(from_base(BYTE_1[:4], 2)) + str(from_base(BYTE_1[4:], 2)))}'''),
        ("d", "a list of 3 integers: red, green, blue", "[from_base(COLOR_1[k:k + 2], 16) for k in (0, 2, 4)]",
         '''decimals=0,
           mistakes={"dans une paire de chiffres hexadécimaux, celui de gauche est le chiffre de poids fort":
                         [from_base(COLOR_1[k:k + 2][::-1], 16) for k in (0, 2, 4)],
                     "dans une paire, le chiffre de gauche compte les seizaines, pas les dizaines":
                         [10 * from_base(COLOR_1[k], 16) + from_base(COLOR_1[k + 1], 16) for k in (0, 2, 4)]}'''),
        ("e", "an integer", "next(k for k in itertools.count(0) if 2 ** k >= TINTS_1)",
         '''decimals=0,
           mistakes={"avec k bits, on écrit 2^k codes distincts, et il en faut au moins 5 000": math.floor(math.log2(TINTS_1)),
                     "on compte des chiffres binaires, pas des chiffres décimaux": len(str(TINTS_1))}'''),
        ("f", "a list of 2 integers: the machine, then the counter", "[WORD_1 // 2 ** 12, WORD_1 % 2 ** 12]",
         '''decimals=0,
           mistakes={"le champ de 4 bits est un seul chiffre hexadécimal, le premier": [WORD_1 // 2 ** 8, WORD_1 % 2 ** 8],
                     "le champ bas ne garde que les 12 derniers bits du mot": [WORD_1 // 2 ** 12, WORD_1]}'''),
        ("g", "a text of 4 hexadecimal digits, between quotes", "to_base(MACHINE_1 * 2 ** 12 + COUNTER_1, 16)",
         '''mistakes={"le champ bas occupe 12 bits, donc 3 chiffres hexadécimaux, complétés par des zéros à gauche":
                         to_base(MACHINE_1, 16) + to_base(COUNTER_1, 16),
                     "le champ bas se convertit en base 16 avant d'être écrit": to_base(MACHINE_1, 16) + str(COUNTER_1),
                     "la question demande l'écriture du mot en base 16": str(MACHINE_1 * 2 ** 12 + COUNTER_1),
                     "écris seulement les chiffres, sans le préfixe 0x de Python":
                         "0x" + to_base(MACHINE_1 * 2 ** 12 + COUNTER_1, 16)}'''),
    ]),

    Paper("MB2.2", "Cent oiseaux, trois milieux, quatre espèces : la PMI des cases, le lift d'une règle, la PPMI, "
                   "l'espèce vue une seule fois, et l'information mutuelle comme moyenne", [
        ("a", "a number", "float((F_2[0][1] / ROWS_2[0]) / COLS_2[1])",
         '''decimals=6,
           mistakes={"le lift compare P(pic | forêt) à P(pic), pas à P(forêt)": float((F_2[0][1] / ROWS_2[0]) / ROWS_2[0]),
                     "P(pic | forêt) divise le nombre de pics de la forêt par le nombre d'oiseaux de la forêt":
                         float(F_2[0][1] / COLS_2[1])}'''),
        ("b", "a number (3 decimals)", "PMI_2[0][1]",
         '''decimals=3,
           mistakes={"la PMI se calcule avec le logarithme népérien, en nats": PMI_2[0][1] / math.log(2),
                     "la PMI se calcule avec le logarithme népérien ln, pas log₁₀": PMI_2[0][1] / math.log(10)}'''),
        ("c", "a number (3 decimals)", "PMI_2[2][2]",
         '''decimals=3,
           mistakes={"la PMI se calcule avec le logarithme népérien, en nats": PMI_2[2][2] / math.log(2),
                     "la PMI divise p(x, y) par le produit des deux marges, pas par celle de la ligne seule":
                         math.log(F_2[2][2] / ROWS_2[2])}'''),
        ("d", "an integer", "sum(v == -math.inf for row in PMI_2 for v in row)",
         '''decimals=0,
           mistakes={"une case vide, de probabilité 0, a une PMI de −∞ : elle compte": 0,
                     "seules les cases vides ont une PMI de −∞ ; une PMI négative reste finie":
                         sum(v < 0 for row in PMI_2 for v in row)}'''),
        ("e", "a number (3 decimals)", "PMI_2[1][0]",
         '''decimals=3,
           mistakes={"la PMI se calcule avec le logarithme népérien, en nats": PMI_2[1][0] / math.log(2),
                     "la PMI se calcule avec des probabilités : divise d'abord chaque compte par le total, 100":
                         math.log(COUNTS_2[1][0] / (sum(COUNTS_2[1]) * sum(row[0] for row in COUNTS_2)))}'''),
        ("f", "an integer", "sum(v > 0 for row in PMI_2 for v in row)",
         '''decimals=0,
           mistakes={"une case de PMI négative a une PPMI nulle": sum(v != 0 and v > -math.inf for row in PMI_2 for v in row),
                     "la PPMI garde les PMI positives et met les autres à 0":
                         sum(-math.inf < v < 0 for row in PMI_2 for v in row)}'''),
        ("g", "a number (4 decimals), in nats", "mean_pmi_2(lambda v: v)",
         '''decimals=4,
           mistakes={"l'information mutuelle se compte ici en nats, avec ln": mean_pmi_2(lambda v: v) / math.log(2),
                     "l'information mutuelle est la moyenne des PMI, pas celle des PPMI": mean_pmi_2(lambda v: max(v, 0.0)),
                     "la moyenne pondère chaque PMI par la probabilité p(x, y) de sa case":
                         float(np.mean([v for row in PMI_2 for v in row if v > -math.inf]))}'''),
    ]),

    Paper("MB2.3", "Lisser la marge des espèces de la même table (α = 1/3) : la loi lissée, le décalage de la PMI de "
                   "chaque colonne, et le classement des espèces d'un milieu avant et après", [
        ("a", "a list of 4 numbers, species 0 to 3", "floats(SMOOTH_3)",
         '''decimals=6,
           mistakes={"α = 1/3 : on prend les racines cubiques des comptes, pas leurs cubes":
                         floats(smoothed_3(lambda n: n ** 3)),
                     "la loi lissée se renormalise : sa somme vaut 1": floats([cube_root(n) for n in SPECIES_3]),
                     "on lisse la marge des colonnes (les espèces), pas celle des milieux":
                         floats(smoothed_3(lambda n: n ** (1 / 3), [sum(row) for row in COUNTS_2]))}'''),
        ("b", "a list of 4 numbers (4 decimals), species 0 to 3", "SHIFT_3",
         '''decimals=4,
           mistakes={"le décalage est −ln(p_α(y)/p(y)) : une colonne qui gagne de la probabilité perd de la PMI":
                         [-v for v in SHIFT_3],
                     "le décalage est un logarithme de rapport, pas la différence p_α(y) − p(y)":
                         [-float(p - q) for p, q in zip(SMOOTH_3, COLS_2)]}'''),
        ("c", "a number (3 decimals)", "PMI_2[1][0] + SHIFT_3[0]",
         '''decimals=3,
           mistakes={"la PMI lissée ajoute à la PMI le décalage de sa colonne, avec son signe": PMI_2[1][0] - SHIFT_3[0],
                     "la PMI lissée se calcule avec ln, en nats": (PMI_2[1][0] + SHIFT_3[0]) / math.log(2)}'''),
        ("d", "a list of 3 numbers (3 decimals): woodpecker, blackbird, sparrow", "[PMI_2[0][j] + SHIFT_3[j] for j in (1, 2, 3)]",
         '''decimals=3,
           mistakes={"le lissage décale la PMI de chaque colonne : pars des PMI de MB2.2 et ajoute le décalage de b)":
                         [PMI_2[0][j] for j in (1, 2, 3)],
                     "le décalage s'ajoute avec son signe, −ln(p_α(y)/p(y))": [PMI_2[0][j] - SHIFT_3[j] for j in (1, 2, 3)]}'''),
        ("e", "a list of species numbers, by decreasing smoothed PMI", "forest_order_3([PMI_2[0][j] + SHIFT_3[j] for j in range(4)])",
         '''decimals=0,
           mistakes={"dans une ligne, le lissage décale chaque colonne d'une constante différente : l'ordre peut changer":
                         forest_order_3(PMI_2[0]),
                     "la huppe n'est pas observée en forêt : la liste ne contient que les espèces observées":
                         forest_order_3([PMI_2[0][j] + SHIFT_3[j] for j in range(4)]) + [0]}'''),
        ("f", BOOL, "all(column_order_3(PMI_2, j) == column_order_3(SMOOTHED_PMI_3, j) for j in range(4))",
         '''mistakes={"dans une colonne, toutes les cases sont décalées de la même constante": False}'''),
    ]),

    Paper("MB2.4", "Quatre magasins, trois produits, une table de rang 2 de SVD donnée : les facteurs U S^β et V S^{1−β} "
                   "pour β = 0, ½ et 1, leur produit, et le cosinus de deux magasins", [
        ("a", "a list of 2 numbers", "[float(S_4[k] * U_4[2, k] * V_4[1, k]) for k in range(2)]",
         '''decimals=6,
           mistakes={"la case (3, 2) est à la ligne 3 (le magasin) et à la colonne 2 (le produit)":
                         [float(S_4[k] * U_4[1, k] * V_4[2, k]) for k in range(2)],
                     "chaque terme est multiplié par sa valeur singulière s_k": [float(U_4[2, k] * V_4[1, k]) for k in range(2)]}'''),
        ("b", "a 4 × 2 matrix, as the list of its rows", "floats(factor_4(1)[0])",
         '''decimals=6,
           mistakes={"S multiplie la colonne k de U par s_k : la première par 135, la seconde par 45":
                         floats(U_4 * S_4[::-1]),
                     "pour β = 1, chaque colonne est multipliée par s_k entière, pas par sa racine":
                         floats(U_4 * np.sqrt(S_4))}'''),
        ("c", "a 3 × 2 matrix, as the list of its rows", "floats(factor_4(0)[1])",
         '''decimals=6,
           mistakes={"pour β = 0, le second facteur prend S₂^{1−β} = S₂ entière": floats(V_4),
                     "le second facteur a une ligne par produit : la forme (3, 2)": floats(factor_4(0)[1].T)}'''),
        ("d", "a list of 3 numbers: β = 0, ½, 1", "[cos(factor_4(b)[0][0], factor_4(b)[0][3]) for b in (0, 0.5, 1)]",
         '''decimals=6,
           mistakes={"la liste suit l'ordre β = 0, ½, 1": [cos(factor_4(b)[0][0], factor_4(b)[0][3]) for b in (1, 0.5, 0)],
                     "β = ½ multiplie chaque colonne par √s_k, pas par s_k/2":
                         [cos(halved_4(b)[0], halved_4(b)[3]) for b in (0, 0.5, 1)]}'''),
        ("e", "a list of 3 numbers (4 decimals): β = 0, ½, 1", "[cos(factor_4(b)[0][0], factor_4(b)[0][1]) for b in (0, 0.5, 1)]",
         '''decimals=4,
           mistakes={"la liste suit l'ordre β = 0, ½, 1": [cos(factor_4(b)[0][0], factor_4(b)[0][1]) for b in (1, 0.5, 0)],
                     "β = ½ multiplie chaque colonne par √s_k, pas par s_k/2":
                         [cos(halved_4(b)[0], halved_4(b)[1]) for b in (0, 0.5, 1)]}'''),
        ("f", BOOL, "all(np.allclose(factor_4(b)[0] @ factor_4(b)[1].T, M_4) for b in np.linspace(0, 1, 11))",
         '''mistakes={"(U S^β)(V S^{1−β})ᵀ = U S^β S^{1−β} Vᵀ, et les puissances de S s'ajoutent": False}'''),
    ]),

    Paper("MB2.5", "Une bannière affichée 3 200 fois et cliquée 50 fois : le logit de vraisemblance maximale, puis un "
                   "non-clic gardé sur 9, le décalage de ln 9 et sa correction", [
        ("a", 'an irreducible fraction, between quotes, like "5/8"', "F(CLICKS_5, SHOWN_5)",
         '''kind="fraction", simplified=True,
           mistakes={"le taux de clic divise les clics par les affichages, pas par les non-clics":
                         F(CLICKS_5, SHOWN_5 - CLICKS_5),
                     "le taux de clic divise les clics par les affichages, pas l'inverse": F(SHOWN_5, CLICKS_5)}'''),
        ("b", "a number (3 decimals)", "math.log(CLICKS_5 / (SHOWN_5 - CLICKS_5))",
         '''decimals=3,
           mistakes={"le logit est le logarithme de la cote (les succès sur les échecs), pas celui du taux":
                         math.log(CLICKS_5 / SHOWN_5),
                     "le logit se calcule avec ln": math.log2(CLICKS_5 / (SHOWN_5 - CLICKS_5))}'''),
        ("c", "a number (3 decimals)", "math.log(CLICKS_5 / KEPT_5)",
         '''decimals=3,
           mistakes={"on garde un non-clic sur 9 et tous les clics : seuls les non-clics sont divisés par 9":
                         math.log(CLICKS_5 / (SHOWN_5 / KEEP_5 - CLICKS_5)),
                     "garder un non-clic sur 9 divise le nombre de non-clics par 9":
                         math.log(CLICKS_5 / ((SHOWN_5 - CLICKS_5) * KEEP_5))}'''),
        ("d", "a number (3 decimals)", "math.log(CLICKS_5 / KEPT_5) - math.log(CLICKS_5 / (SHOWN_5 - CLICKS_5))",
         '''decimals=3,
           mistakes={"l'écart est le logarithme du rapport des taux de sélection, pas le rapport lui-même": float(KEEP_5),
                     "l'écart se mesure en nats, avec ln": math.log2(KEEP_5)}'''),
        ("e", 'an irreducible fraction, between quotes', "F(CLICKS_5, CLICKS_5 + KEPT_5)",
         '''kind="fraction", simplified=True,
           mistakes={"la probabilité est σ du logit, a/(a + b) : la cote a/b n'est pas une probabilité": F(CLICKS_5, KEPT_5),
                     "sans correction, le modèle lit le taux de l'échantillon, pas celui de la population":
                         F(CLICKS_5, SHOWN_5)}'''),
        ("f", 'an irreducible fraction, between quotes', "from_odds_5(odds_5(READ_5) / KEEP_5)",
         '''kind="fraction", simplified=True,
           mistakes={"on corrige le logit (ou la cote), pas la probabilité directement": READ_5 / KEEP_5,
                     "on retranche ln 9 au logit, on ne l'ajoute pas": from_odds_5(odds_5(READ_5) * KEEP_5)}'''),
    ]),

    Paper("MB2.6", "Yaourt et fromage blanc, nature et sucrés : mesurer le parallélogramme d'une analogie (défaut, "
                   "rapport ε, borne du cosinus), et dire si d peut l'emporter sur c", [
        ("a", "a list of 3 numbers", "floats(Q_6)",
         '''decimals=6,
           mistakes={"q part de c et ajoute le décalage b − a, du nature au sucré": floats(A_6 - B_6 + C_6),
                     "q = b − a + c : on ajoute c, on ne le retranche pas": floats(B_6 + A_6 - C_6)}'''),
        ("b", "a number", "norm((B_6 - A_6) - (D_6 - C_6))",
         '''decimals=6,
           mistakes={"le décalage du fromage blanc va du nature au sucré : d − c": norm((B_6 - A_6) - (C_6 - D_6)),
                     "le défaut est la norme de la différence des décalages, pas la différence de leurs normes":
                         norm(B_6 - A_6) - norm(D_6 - C_6)}'''),
        ("c", "a list of 2 numbers (3 decimals): ε, then the bound", "[EPS_6, math.sqrt(1 - EPS_6 ** 2)]",
         '''decimals=3,
           mistakes={"ε rapporte ‖b − a‖ à la norme de c, pas à celle de q":
                         [norm(B_6 - A_6) / norm(Q_6), math.sqrt(1 - (norm(B_6 - A_6) / norm(Q_6)) ** 2)],
                     "la borne est √(1 − ε²), une racine": [EPS_6, 1 - EPS_6 ** 2]}'''),
        ("d", "a number (3 decimals)", "cos(Q_6, C_6)",
         '''decimals=3,
           mistakes={"le cosinus divise le produit scalaire par le produit des deux normes": float(Q_6 @ C_6 / (C_6 @ C_6)),
                     "la question demande le cosinus de q et c, le point de la question": cos(Q_6, D_6)}'''),
        ("e", "a number (3 decimals)", "math.sqrt(1 - DELTA_6 ** 2 / float(D_6 @ D_6))",
         '''decimals=3,
           mistakes={"appliquée à d, la borne rapporte δ à la norme de d, pas à celle de c":
                         math.sqrt(1 - DELTA_6 ** 2 / float(C_6 @ C_6)),
                     "la borne est √(1 − δ²/‖d‖²), une racine": 1 - DELTA_6 ** 2 / float(D_6 @ D_6)}'''),
        ("f", BOOL, "cos(Q_6, D_6) > cos(Q_6, C_6)",
         '''mistakes={"la borne garantie pour d dépasse le cosinus de c : compare les deux nombres": False}'''),
        ("g", "a number (4 decimals)", "cos(B_6 - A_6, D_6 - C_6)",
         '''decimals=4,
           mistakes={"on compare les deux décalages, b − a et d − c, pas leurs extrémités b et d": cos(B_6, D_6),
                     "les deux décalages vont du nature au sucré : d − c, pas c − d": cos(B_6 - A_6, C_6 - D_6)}'''),
        ("h", "a list of 3 numbers (4 decimals): ε, the bound, then cos(q, cream)", "cream_6(norm(CREAM_6))",
         '''decimals=4,
           mistakes={"ε rapporte ‖b − a‖ à la norme de la crème, pas à celle de q": cream_6(norm(B_6 - A_6 + CREAM_6)),
                     "la borne est √(1 − ε²), une racine": cream_6(norm(CREAM_6), root=False)}'''),
    ]),

    Paper("MB2.7", "Des mesures d'animaux en logarithme : la direction de taille estimée sur deux différences, la retirer "
                   "de trois animaux, et les distances qui restent", [
        ("a", "a 2 × 2 matrix, as the list of its rows", "floats(D_7 @ D_7.T)",
         '''decimals=6,
           mistakes={"la matrice de Gram des deux différences (les lignes) est de forme (2, 2)": floats(D_7.T @ D_7),
                     "G_ij est le produit scalaire des différences i et j, pas le carré de leur distance":
                         floats(((D_7[:, None, :] - D_7[None, :, :]) ** 2).sum(axis=-1))}'''),
        ("b", "a number", "float(np.linalg.eigvalsh(D_7 @ D_7.T).max())",
         '''decimals=6,
           mistakes={"le premier axe est celui de la plus grande valeur propre": float(np.linalg.eigvalsh(D_7 @ D_7.T).min()),
                     "les valeurs propres de G ne sont pas ses coefficients diagonaux": float((D_7 @ D_7.T)[0, 0])}'''),
        ("c", "a list of 3 numbers (3 decimals)", "floats(U_7)",
         '''decimals=3,
           mistakes={"l'axe est unitaire : divise par sa norme": floats(D_7.T @ TOP_7 * math.sqrt(2)),
                     "l'axe vit dans l'espace des mesures, de dimension 3 : c'est Dᵀ fois le vecteur propre de G":
                         floats(TOP_7)}'''),
        ("d", "a 3 × 3 matrix, as the list of its rows", "floats(X_7 - np.outer(X_7 @ U_7, U_7))",
         '''decimals=6,
           mistakes={"sans diviser par u·u, la direction n'est retirée que si u est unitaire":
                         floats(X_7 - np.outer(X_7 @ ONES_7, ONES_7)),
                     "on garde x moins sa projection sur u, pas la projection": floats(np.outer(X_7 @ U_7, U_7))}'''),
        ("e", "a list of 2 numbers (4 decimals): before, then after", "[norm(X_7[0] - X_7[2]), norm(R_7[0] - R_7[2])]",
         '''decimals=4,
           mistakes={"la question demande des distances, pas leurs carrés":
                         [float((X_7[0] - X_7[2]) @ (X_7[0] - X_7[2])), float((R_7[0] - R_7[2]) @ (R_7[0] - R_7[2]))],
                     "la liste donne la distance avant le retrait, puis après":
                         [norm(R_7[0] - R_7[2]), norm(X_7[0] - X_7[2])]}'''),
        ("f", "a number", "float(((X_7[0] - X_7[2]) @ U_7) ** 2)",
         '''decimals=6,
           mistakes={"c'est le carré du produit scalaire, ((x₁ − x₃)·u)²": float((X_7[0] - X_7[2]) @ U_7),
                     "u est unitaire : (1, 1, 1) doit d'abord être divisé par sa norme":
                         float(((X_7[0] - X_7[2]) @ ONES_7) ** 2)}'''),
    ]),

    Paper("MB2.11", "Pont : résumer des séries de relevés de longueurs différentes par une moyenne masquée, montrer que le "
                    "remplissage ne change rien, et compter les comparaisons par paires", [
        ("a", "a list of 2 numbers: temperature, humidity", "floats(masked_mean_11(H_11, MASK_11)[0])",
         '''decimals=6,
           mistakes={"la moyenne masquée divise par la somme du masque (les vrais relevés), pas par la longueur complétée":
                         floats(H_11[0].mean(axis=0)),
                     "la moyenne se fait grandeur par grandeur, sur les relevés : un vecteur de 2 nombres":
                         floats(H_11[0][MASK_11[0] == 1].mean(axis=1))}'''),
        ("b", "a list of 2 numbers: temperature, humidity", "floats(masked_mean_11(H_11, MASK_11)[1])",
         '''decimals=6,
           mistakes={"la moyenne masquée divise par la somme du masque (les vrais relevés), pas par la longueur complétée":
                         floats(H_11[1].mean(axis=0)),
                     "on divise la somme par le nombre de relevés de la station, pas par le nombre de stations":
                         floats(H_11[1].sum(axis=0) / len(H_11))}'''),
        ("c", BOOL, "bool(np.allclose(masked_mean_11(*padded_11(6)), masked_mean_11(H_11, MASK_11)))",
         '''mistakes={"un relevé de masque 0 ne compte ni dans la somme ni dans le nombre de relevés": False}'''),
        ("d", "an integer", "math.comb(STATIONS_11, 2)",
         '''decimals=0,
           mistakes={"une paire de stations ne se compare qu'une fois, et pas une station avec elle-même":
                         STATIONS_11 * STATIONS_11,
                     "(A, B) et (B, A) sont la même paire": STATIONS_11 * (STATIONS_11 - 1)}'''),
        ("e", "a number", "float(F(math.comb(STATIONS_11, 2), STATIONS_11))",
         '''decimals=6,
           mistakes={"(A, B) et (B, A) sont la même comparaison": float(STATIONS_11 - 1),
                     "une station ne se compare pas avec elle-même": STATIONS_11 / 2}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed from the statements (exact fractions and integers where the calculation is exact)
import itertools
import math
from fractions import Fraction as F

import numpy as np


def floats(values):
    """A number, a vector or a matrix (fractions, NumPy) as a float or nested lists of floats (-0.0 written 0.0)."""
    return (np.round(np.asarray(values, dtype=float), 12) + 0.0).tolist()


def norm(v):
    return float(np.linalg.norm(np.asarray(v, dtype=float)))


def cos(a, b):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


# MB2.1: bases 2 and 16, by successive divisions (Euclidean division, R0)
DIGITS = "0123456789ABCDEF"


def to_base(n, base):
    """The digits of the integer n >= 1 in the base, the most significant first."""
    digits = ""
    while n:
        n, r = divmod(n, base)
        digits = DIGITS[r] + digits
    return digits


def from_base(text, base):
    """The integer written by the digits of text in the base."""
    value = 0
    for digit in text:
        value = value * base + DIGITS.index(digit.upper())
    return value


BYTE_1, COLOR_1, TINTS_1 = "11001011", "4A7C59", 5000
WORD_1 = from_base("6B4D", 16)
MACHINE_1, COUNTER_1 = 9, 200


# MB2.2: 100 birds, rows forêt, prairie, village; columns huppe, pic, merle, moineau
COUNTS_2 = [[0, 6, 14, 20], [1, 2, 10, 22], [0, 0, 3, 22]]
F_2 = [[F(c, 100) for c in row] for row in COUNTS_2]                     # the joint law, exactly
ROWS_2 = [sum(row) for row in F_2]
COLS_2 = [sum(row[j] for row in F_2) for j in range(4)]
PMI_2 = [[math.log(F_2[i][j] / (ROWS_2[i] * COLS_2[j])) if F_2[i][j] else -math.inf for j in range(4)]
         for i in range(3)]


def mean_pmi_2(transform):
    """Σ p(x, y) transform(PMI(x, y)) over the cells of probability > 0."""
    return float(sum(float(F_2[i][j]) * transform(PMI_2[i][j]) for i in range(3) for j in range(4) if F_2[i][j]))


# MB2.3: the species margin smoothed with alpha = 1/3 (exact cube roots of 1, 8, 27, 64)
SPECIES_3 = [sum(row[j] for row in COUNTS_2) for j in range(4)]


def cube_root(n):
    """The cube root of a perfect cube, exactly."""
    return next(k for k in range(n + 1) if k ** 3 == n)


def smoothed_3(power, counts=SPECIES_3):
    """power(n(y)) renormalized (exact fractions for integer powers)."""
    values = [F(power(n)) for n in counts]
    return [v / sum(values) for v in values]


SMOOTH_3 = smoothed_3(cube_root)
SHIFT_3 = [-math.log(p / q) for p, q in zip(SMOOTH_3, COLS_2)]           # the shift of each column
SMOOTHED_PMI_3 = [[v + SHIFT_3[j] for j, v in enumerate(row)] for row in PMI_2]


def forest_order_3(row):
    """The species observed in the forest (finite values), by decreasing value."""
    return sorted((j for j in range(4) if row[j] > -math.inf), key=lambda j: -row[j])


def column_order_3(table, j):
    """The habitats by decreasing value in column j (-inf last, the smaller index first)."""
    return sorted(range(3), key=lambda i: (-table[i][j], i))


# MB2.4: four shops, three products; the given compact SVD of rank 2
M_4 = np.array([[50.0, 8, 26], [5, 44, 8], [88, 40, 49], [34, 40, 22]])
U_4 = np.array([[2.0, -2], [1, 4], [4, -1], [2, 2]]) / 5
V_4 = np.array([[7.0, -4], [4, 8], [4, -1]]) / 9
S_4 = np.array([135.0, 45.0])
assert np.allclose(U_4 @ np.diag(S_4) @ V_4.T, M_4)


def factor_4(beta):
    """(A_beta, B_beta) = (U S^beta, V S^(1 - beta))."""
    return U_4 * S_4 ** beta, V_4 * S_4 ** (1 - beta)


def halved_4(beta):
    """The classic error: S^beta read as beta S (S/2 for beta = 1/2; S^0 = I kept)."""
    return U_4 * (beta * S_4 if beta else np.ones(2))


# MB2.5: a banner shown 3 200 times, clicked 50 times; one non-click in 9 kept
SHOWN_5, CLICKS_5, KEEP_5 = 3200, 50, 9
KEPT_5 = F(SHOWN_5 - CLICKS_5, KEEP_5)                                  # the non-clicks kept
READ_5 = F(2, 10)                                                       # the probability read for another banner


def odds_5(p):
    return p / (1 - p)


def from_odds_5(o):
    return o / (1 + o)


# MB2.6: (protein, carbohydrate, fat) per 100 g
A_6, B_6 = np.array([4.0, 5, 3]), np.array([4.0, 10, 3])                # yoghurt, plain and sweet
C_6, D_6 = np.array([8.0, 4, 3]), np.array([7.0, 9, 3])                 # fromage blanc, plain and sweet
CREAM_6 = np.array([2.0, 3, 30])
Q_6 = B_6 - A_6 + C_6
EPS_6 = norm(B_6 - A_6) / norm(C_6)
DELTA_6 = norm((B_6 - A_6) - (D_6 - C_6))


def cream_6(reference_norm, root=True):
    """[eps, bound, cos(q, cream)] with eps = ||b - a|| / reference_norm, for the query b - a + cream."""
    eps = norm(B_6 - A_6) / reference_norm
    return [eps, math.sqrt(1 - eps ** 2) if root else 1 - eps ** 2, cos(B_6 - A_6 + CREAM_6, CREAM_6)]


# MB2.7: log2 lengths (body, tail, ear) of three animals; two differences
D_7 = np.array([[2.0, 4, 3], [4, 2, 3]])
X_7 = np.array([[2.0, 3, 4], [3.5, 4.5, 5.5], [5, 3, 4]])
ONES_7 = np.ones(3)
_w7, _V7 = np.linalg.eigh(D_7 @ D_7.T)
TOP_7 = _V7[:, -1] * np.sign(_V7[0, -1])                               # the eigenvector of the largest eigenvalue
U_7 = D_7.T @ TOP_7
U_7 = U_7 / np.linalg.norm(U_7)
U_7 = U_7 * np.sign(U_7[0])                                             # unit, first coordinate positive
R_7 = X_7 - np.outer(X_7 @ U_7, U_7)


# MB2.11: three weather stations, (temperature °C, humidity %), padded with (0, 0) to 4 readings
SERIES_11 = [[(12, 80), (15, 71), (18, 62)], [(9, 88), (11, 84)], [(20, 55), (22, 49), (19, 58), (23, 46)]]
STATIONS_11 = 300


def padded_11(length):
    """The array H of shape (3, length, 2) and its mask of shape (3, length)."""
    H, mask = np.zeros((3, length, 2)), np.zeros((3, length))
    for i, series in enumerate(SERIES_11):
        H[i, :len(series)] = series
        mask[i, :len(series)] = 1
    return H, mask


H_11, MASK_11 = padded_11(4)


def masked_mean_11(H, mask):
    """Σ m_t h_t / Σ m_t for each station."""
    return (H * mask[..., None]).sum(axis=1) / mask.sum(axis=1)[:, None]'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ MB2.1 à MB2.7 ; 🔗 MB2.11)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question "
               "(« a number » sans décimales : la valeur exacte, ces calculs tombent juste) ;\n"
               "- une fraction irréductible entre guillemets, `\"5/8\"` ;\n"
               "- un nombre écrit en base 2 ou en base 16 comme un texte entre guillemets, avec ses seuls chiffres, "
               "`\"1011\"` ou `\"3F\"` (sans `0b` ni `0x`) ;\n"
               "- une liste `[0.2, -1]`, dans l'ordre que dit la question ; des espèces comme la liste de leurs "
               "numéros ; une matrice comme la liste de ses **lignes**, `[[1, 0], [-2, 3]]` ;\n"
               "- `True` ou `False` pour un vrai ou faux.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")


def paper_part(kind: str) -> list:
    """The cells of Part 0."""
    return paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO)


# ---------------------------------------------------------------------------
# Notebook exercises: your library (MB2.13, MB2.14)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to D)
import math
import re
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import null_space

from wbm.errors import MymathMissingError
from wbm.nbtools import StopCheck, checked, drawn, filled, fr, own_code, run_pytest_group, verdict

TEST_MB2 = "tests/test_mb2_cooccurrence.py"         # the tests of mymath/cooccurrence.py
REF = wbm.load_mymath("ref", alias="mymath_ref")  # the reference: the wrong versions and the checks rely on it
ref_cooc, ref_svd = REF.cooccurrence, REF.svd_pca
REF_COOC = {f"ref_cooc.{name}": getattr(ref_cooc, name)          # a check stops if your code calls one of them
            for name in ("pmi", "case_control_logit", "remove_direction")}


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
    return bool(wbm.check(ex_id, value, computed=True, quiet=True).passed)


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
               for x, y in zip(np.atleast_1d(xs), np.atleast_1d(ys)))'''

DATA = '''# The data of the paper exercises (02_exercices.md)
BIRDS = np.array([[0.0, 6, 14, 20], [1, 2, 10, 22], [0, 0, 3, 22]])  # MB2.2: 100 birds (counts); rows forêt, prairie, village
P = BIRDS / 100                                                      # their joint law; columns 0 huppe, 1 pic, 2 merle, 3 moineau
SHOPS = np.array([[50.0, 8, 26], [5, 44, 8], [88, 40, 49], [34, 40, 22]])   # MB2.4: shops 1 to 4 (rows), three products
BANNER = {"shown": 3200, "clicks": 50, "keep_negative": 1 / 9}       # MB2.5: one non-click in 9 kept
ANIMALS = np.array([[2.0, 3, 4], [3.5, 4.5, 5.5], [5, 3, 4]])        # MB2.7: log2 of (body, tail, ear), animals 1 to 3'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="MB2")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M28). Ouvre ta copie `mon_travail/mymath/cooccurrence.py`, lis la "
         "docstring du module (ses conventions, et ce qui est permis) puis celle de la fonction, remplace chaque "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Dans le notebook, appelle tes fonctions par "
         "`mymath.cooccurrence.<nom>` (par exemple `mymath.cooccurrence.pmi(P)`), ou donne-leur un nom court "
         "(`pmi = mymath.cooccurrence.pmi`) dans une cellule exécutée après le rechargement. "
         "⚠️ Le squelette n'importe rien : ajoute en tête du fichier `import numpy as np` (et `import math` si tu t'en "
         "sers). NumPy et le module `math` sont permis, mais aucune fonction de SciPy (`scipy.special.logit`, "
         "`scipy.special.xlogy`) ni de scikit-learn (`mutual_info_score`) : les tests comparent tes résultats aux "
         "leurs, et un test lit ton module. Les logarithmes sont népériens ; une loi jointe est donnée par ses "
         "**probabilités**, jamais par des comptes ; ne modifie jamais les tableaux reçus. Hors de `mymath`, le "
         "notebook peut se servir de tout NumPy et de SciPy, et de tes fonctions de M06 (`mymath.info`), de M12d "
         "(`mymath.svd_pca`) et de M28 (`mymath.sampling`).")

REMINDER = ("> Même mode d'emploi qu'en MB2.13 : écris les fonctions dans ta copie `mon_travail/mymath/cooccurrence.py`, "
            "**enregistre**, puis exécute les cellules ci-dessous ; la première recharge ta librairie.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of cooccurrence.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("todo", f'run_pytest_group(TEST_MB2, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_MB2, "{keyword}", impl="ref")')]


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


HINT_13A = '''lambda v: ("la table a une ligne par milieu et une colonne par espèce : la forme (3, 4) de P"
           if np.shape(v) == (4, 3) else None)'''

NOTE_13 = (r"`table = np.array(joint, dtype=float)` (une copie), les contrôles (booléens avant la conversion, 2-D, non "
           r"vide, finis, $\ge 0$, somme 1 à $10^{-9}$ près), `p_x = table.sum(axis=1)`, `p_y = table.sum(axis=0)`, "
           r"`result = np.full(table.shape, -np.inf)`, puis, sur `rows, columns = np.nonzero(table > 0)`, "
           r"`np.log(table[rows, columns]) - np.log(p_x[rows]) - np.log(p_y[columns])`. a) La table de MB2.2 : "
           r"$0{,}629$ pour (forêt, pic), $-0{,}811$ pour (village, merle), $1{,}050$ pour (prairie, huppe), et $-\infty$ "
           r"sur les trois cases vides. b) $I \approx 0{,}0759$ nat, et vrai. c) Vrai. d) 5 : la ligne vide et la colonne "
           r"vide ont 5 cases en tout.")

MB2_13 = Ex(
    "MB2.13", "🔨", 1, 25, "La table des PMI d'une loi jointe, −∞ sur les cases vides · `pmi`",
    "programmer la table des PMI d'une loi jointe, avec −∞ sur les cases vides, puis la comparer à ta copie, retrouver "
    "l'information mutuelle de M06 comme sa moyenne, et voir ce que deviennent une ligne et une colonne vides.",
    "fiche §2 ; M03, M06 ; Ex MB2.2", tracks="C, E", mymath="cooccurrence.py", note=NOTE_13,
    body=HOWTO + r"""

Écris `pmi(joint)` (fiche §2), en suivant sa docstring : contrôle la table (2-D, non vide, des nombres finis $\ge 0$, pas des booléens, de somme 1 à $10^{-9}$ près) ; calcule les marges $p(x)$ (sommes des lignes) et $p(y)$ (sommes des colonnes), en colonne et en ligne pour qu'elles se diffusent (M20) ; pars d'une table remplie de `-np.inf`, et calcule le logarithme du rapport sur les seules cases de probabilité non nulle, sans avertissement de NumPy ; rends un tableau de flottants de la forme de la table.

**L'usage.** La cellule de données de la partie A donne la table des oiseaux de MB2.2 (`BIRDS`, les comptes) et sa loi jointe `P = BIRDS / 100`. Avec ta fonction :
- a) la table des PMI de `P` (un tableau de forme $(3, 4)$, tel que rendu, $-\infty$ compris), à comparer à ta copie de MB2.2 ;
- b) la moyenne $\sum p(x, y)\operatorname{PMI}(x, y)$ sur les cases non vides, puis vrai ou faux : elle est égale, à $10^{-12}$ près, à `mymath.info.mutual_information(P, base=math.e)` (M06 compte en bits par défaut) (une liste de 2 : le nombre, puis le booléen) ;
- c) vrai ou faux : `pmi(P.T)` est égale à la transposée de `pmi(P)`, à $10^{-12}$ près, avec $-\infty$ aux mêmes places ;
- d) pour la loi $\mathbf{Q} = \begin{pmatrix} 0{,}25 & 0 & 0{,}15 \\ 0 & 0 & 0 \\ 0{,}2 & 0 & 0{,}4 \end{pmatrix}$ (`Q_13`), qui a une ligne et une colonne vides : le nombre de cases de PMI $-\infty$ (un entier).

Ce qu'il faut observer : une ligne vide et une colonne vide ne font ni erreur ni avertissement ; transposer la loi transpose la table ; l'information mutuelle est la moyenne des PMI, et ne dépend que de l'unité du logarithme.""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `pmi` (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu).")]
    + tests_cells("test_pmi_ or test_module_uses_") + [
        ("md", "**L'usage** : la table des oiseaux, sa moyenne, sa transposée, et une loi qui a une ligne et une colonne "
               "vides."),
        ("todo", '''Q_13 = np.array([[0.25, 0.0, 0.15], [0.0, 0.0, 0.0], [0.2, 0.0, 0.4]])
answer_MB2_13a = answer_MB2_13b = answer_MB2_13c = answer_MB2_13d = ...
with wbm.attempt("MB2.13"):          # if you call pmi here: ⏳ while it is not written
    answer_MB2_13a = ...  # a) a (3, 4) array, as returned: pmi(P), -inf included
    answer_MB2_13b = ...  # b) a list of 2: the mean of the PMI under P over the cells of probability > 0 (as computed), then True or False: it equals mymath.info.mutual_information(P, base=math.e) to 1e-12
    answer_MB2_13c = ...  # c) True or False: pmi(P.T) equals the transpose of pmi(P) to 1e-12, with -inf at the same places
    answer_MB2_13d = ...  # d) an integer: the number of cells of pmi(Q_13) equal to -inf'''),
        ("check", answers_check("MB2.13", "abcd", {"a": HINT_13A})),
        ("solution", '''Q_13 = np.array([[0.25, 0.0, 0.15], [0.0, 0.0, 0.0], [0.2, 0.0, 0.4]])
pmi = mymath.cooccurrence.pmi
with warnings.catch_warnings():
    warnings.simplefilter("error")                           # pmi must not warn, even with empty cells
    T_13, TQ_13 = pmi(P), pmi(Q_13)
nonzero_13 = P > 0
mean_13 = float(np.sum(P[nonzero_13] * T_13[nonzero_13]))
answer_MB2_13a = T_13
answer_MB2_13b = [mean_13, abs(mean_13 - mymath.info.mutual_information(P, base=math.e)) <= 1e-12]
TT_13 = pmi(P.T)
answer_MB2_13c = bool(np.array_equal(np.isneginf(TT_13), np.isneginf(T_13.T))
                      and np.allclose(TT_13, T_13.T, rtol=0, atol=1e-12))
answer_MB2_13d = int(np.isneginf(TQ_13).sum())
print("a)", np.round(answer_MB2_13a, 4).tolist())
print("b)", answer_MB2_13b, " c)", answer_MB2_13c, " d)", answer_MB2_13d)
print("   l'information mutuelle de M06 en bits, par défaut :", round(mymath.info.mutual_information(P), 6))

''' + answers_check("MB2.13", "abcd", {"a": HINT_13A})),
        ("record", '''def pmi_13r(J):
    """The oracle: ln p(x, y) - ln p(x) - ln p(y), cell by cell with math.log, -inf on the cells of probability 0."""
    J = np.asarray(J, dtype=float)
    px, py = J.sum(axis=1), J.sum(axis=0)
    return np.array([[math.log(J[i, j]) - math.log(px[i]) - math.log(py[j]) if J[i, j] > 0 else -math.inf
                      for j in range(J.shape[1])] for i in range(J.shape[0])])


P_13r = np.array([[0.0, 6, 14, 20], [1, 2, 10, 22], [0, 0, 3, 22]]) / 100
T_13r = pmi_13r(P_13r)
conditional_13r = np.where(P_13r > 0, T_13r + np.log(P_13r.sum(axis=0)), -np.inf)       # ln p(y | x)
wbm.record("MB2.13a", T_13r.tolist(), decimals=6,
           mistakes={"la PMI est en nats : le logarithme népérien, np.log": (T_13r / math.log(2)).tolist(),
                     "la PMI divise p(x, y) par p(x) ET par p(y) : ln P(y | x) − ln p(y)": conditional_13r.tolist(),
                     "une case de probabilité 0 a une PMI de −∞, pas 0": np.where(np.isinf(T_13r), 0.0, T_13r).tolist()})
finite_13r = P_13r > 0
I_13r = float(sum(P_13r[i, j] * T_13r[i, j] for i in range(3) for j in range(4) if finite_13r[i, j]))
wbm.record("MB2.13b", [I_13r, True], decimals=6,
           mistakes={"mutual_information de M06 compte en bits par défaut : compare avec base=math.e": [I_13r, False],
                     "la moyenne pondère chaque PMI par la probabilité p(x, y) de sa case, sur les cases non vides":
                         [float(T_13r[finite_13r].mean()), False]})
wbm.record("MB2.13c", True,
           mistakes={"transposer la loi échange les rôles de X et Y, donc ceux de p(x) et p(y) : compare pmi(P.T) à "
                     "pmi(P).T avec np.allclose, qui tient deux −∞ pour égaux": False})
Q_13r = np.array([[0.25, 0.0, 0.15], [0.0, 0.0, 0.0], [0.2, 0.0, 0.4]])
wbm.record("MB2.13d", int(np.isneginf(pmi_13r(Q_13r)).sum()),
           mistakes={"la case commune à la ligne vide et à la colonne vide ne compte qu'une fois":
                         int((Q_13r == 0).any(axis=1).sum() * Q_13r.shape[1] + (Q_13r == 0).all(axis=0).sum() * Q_13r.shape[0]),
                     "une case de probabilité 0 a une PMI de −∞, même dans une ligne ou une colonne vide": 0,
                     "la colonne vide compte aussi : chacune de ses cases a une PMI de −∞":
                         int((Q_13r == 0).all(axis=1).sum() * Q_13r.shape[1])})'''),
    ],
)

NOTE_14 = (r"`case_control_logit` : `_rate` pour les deux taux, des tableaux de flottants (booléens refusés avant), "
           r"`np.broadcast_arrays`, le refus d'une case 0/0, puis trois masques ; `float(...)` pour une forme `()`. "
           r"`remove_direction` : `coefficients = (X @ u) / (u @ u)`, puis `X - np.multiply.outer(coefficients, u)`. "
           r"a) $-\ln 63 \approx -4{,}143$, comme MB2.5 b). b) $(-\ln 63 ;\ -\ln 30 ;\ -\infty)$. c) $-\ln 128 \approx "
           r"-4{,}852$, puis $\frac{1}{129} \approx 0{,}0078$. d) $(-1, 0, 1)$, $(-1, 0, 1)$, $(1, -1, 0)$, et vrai. e) 3.")

MB2_14 = Ex(
    "MB2.14", "🔨", 2, 25, "Deux briques : le logit d'une population estimé sur un échantillon cas-témoins, et retirer une "
    "direction des lignes d'une matrice · `case_control_logit`, `remove_direction`",
    "programmer la correction d'un logit estimé sur un échantillon cas-témoins et le retrait d'une direction, puis s'en "
    "servir sur la bannière de MB2.5, une étude cas-témoins et les animaux de MB2.7.",
    "fiche §5 et §7 ; M04, M07, M12b, M13a ; Ex MB2.5 et MB2.7", tracks="C, E",
    mymath="cooccurrence.py", note=NOTE_14,
    body=REMINDER + r"""

Écris `case_control_logit(n_positive, n_negative, keep_positive=1.0, keep_negative=1.0)` et `remove_direction(X, u)` (fiche §5 et §7), en suivant leurs docstrings. `case_control_logit` : contrôle les deux taux (dans $]0, 1]$, ni `nan` ni booléen), puis les nombres d'exemples (finis, $\ge 0$, pas des booléens, refusés avant la conversion en flottants) ; diffuse-les (`np.broadcast_arrays`) ; traite les trois cas case par case (les deux nombres positifs : le logarithme du rapport, moins celui des taux ; seul $n_1 > 0$ : $+\infty$ ; seul $n_0 > 0$ : $-\infty$), et refuse une case où les deux sont nuls ; rends un `float` quand la forme diffusée est `()`. `remove_direction` : contrôle $\mathbf{X}$ (1-D ou 2-D, non vide, des nombres finis) et $\mathbf{u}$ (1-D, de la longueur des lignes, non nul) ; calcule les coefficients $\mathbf{x}\cdot\mathbf{u}/\mathbf{u}\cdot\mathbf{u}$ de toutes les lignes en un produit matrice-vecteur, puis retire coefficient fois $\mathbf{u}$ à chaque ligne (un produit extérieur, ou la diffusion).

**L'usage.** La cellule de données de la partie A donne la bannière de MB2.5 (`BANNER`) et les animaux de MB2.7 (`ANIMALS`, une ligne par animal). Avec tes fonctions :
- a) la bannière de MB2.5 : `case_control_logit(50, 350, keep_negative=1/9)` (un nombre), à comparer à ta réponse b) de MB2.5 ;
- b) trois bannières d'un même échantillon, de 50, 12 et 0 clics, et de 350, 40 et 25 non-clics gardés, avec le même taux $\frac19$ : les trois logits de la population, en un appel (un tableau de 3 nombres, tel que rendu) ;
- c) une étude cas-témoins garde chaque positif avec la probabilité 0,8 et chaque négatif avec la probabilité 0,025, et compte 30 positifs et 120 négatifs : le logit de la population, puis la probabilité d'un positif dans la population (une liste de 2 nombres) ;
- d) les trois animaux de MB2.7 sans la direction $(1, 1, 1)$, à comparer à ta réponse d) de MB2.7, puis vrai ou faux : la direction $(-2, -2, -2)$ donne le même résultat (à $10^{-12}$ près) (une liste de 10 : les 9 coordonnées, ligne par ligne, puis le booléen) ;
- e) $\lVert\mathbf{x}_1 - \mathbf{x}_3\rVert^2 - \lVert\mathbf{r}_1 - \mathbf{r}_3\rVert^2$, où $\mathbf{r}_i$ est l'animal $i$ après le retrait (un nombre).

Ce qu'il faut observer : une bannière sans clic a un logit de $-\infty$, qui reste $-\infty$ après la correction ; un sous-échantillonnage fort des négatifs se corrige par une simple soustraction ; retirer une direction ne dépend ni de la longueur de $\mathbf{u}$ ni de son sens.""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=[("md", "**Les tests** de `case_control_logit`, puis de `remove_direction` (lis d'abord la ligne qui suit chaque "
                  "❌ : elle dit ce qui était attendu).")]
    + tests_cells("test_case_control_logit_") + tests_cells("test_remove_direction_") + [
        ("md", "**L'usage** : la bannière, trois bannières en un appel, une étude cas-témoins, puis les animaux."),
        ("todo", '''answer_MB2_14a = answer_MB2_14b = answer_MB2_14c = answer_MB2_14d = answer_MB2_14e = ...
with wbm.attempt("MB2.14"):          # if you call your functions here: ⏳ while they are not written
    answer_MB2_14a = ...  # a) a number, as computed: case_control_logit(50, 350, keep_negative=1 / 9)
    answer_MB2_14b = ...  # b) an array of 3 numbers, as returned by ONE call: the three banners (-inf included)
    answer_MB2_14c = ...  # c) a list of 2 numbers, as computed: the logit of the population, then the probability of a positive in the population
    answer_MB2_14d = ...  # d) a list of 10: the 9 coordinates of remove_direction(ANIMALS, (1, 1, 1)), row by row (.ravel()), then True or False: the direction (-2, -2, -2) gives the same result to 1e-12
    answer_MB2_14e = ...  # e) a number, as computed: ‖x1 − x3‖² − ‖r1 − r3‖²'''),
        ("check", answers_check("MB2.14", "abcde")),
        ("solution", '''case_control_logit = mymath.cooccurrence.case_control_logit
remove_direction = mymath.cooccurrence.remove_direction
answer_MB2_14a = case_control_logit(BANNER["clicks"], (BANNER["shown"] - BANNER["clicks"]) * BANNER["keep_negative"],
                                    keep_negative=BANNER["keep_negative"])
answer_MB2_14b = case_control_logit([50, 12, 0], [350, 40, 25], keep_negative=1 / 9)
logit_14 = case_control_logit(30, 120, keep_positive=0.8, keep_negative=0.025)
answer_MB2_14c = [logit_14, 1 / (1 + math.exp(-logit_14))]
R_14 = remove_direction(ANIMALS, np.ones(3))
answer_MB2_14d = R_14.ravel().tolist() + [bool(np.allclose(remove_direction(ANIMALS, [-2.0, -2.0, -2.0]), R_14,
                                                           rtol=0, atol=1e-12))]
answer_MB2_14e = float(np.sum((ANIMALS[0] - ANIMALS[2]) ** 2) - np.sum((R_14[0] - R_14[2]) ** 2))
print("a)", answer_MB2_14a, " b)", answer_MB2_14b, " c)", answer_MB2_14c)
print("d)", np.round(answer_MB2_14d[:9], 6).tolist(), answer_MB2_14d[9], " e)", answer_MB2_14e)

''' + answers_check("MB2.14", "abcde")),
        ("record", '''def logit_14r(n1, n0, s1=1.0, s0=1.0):
    """The oracle: ln(n1/n0) - ln(s1/s0) with math.log; +inf or -inf when a class is absent."""
    if n0 == 0:
        return math.inf
    if n1 == 0:
        return -math.inf
    return math.log(n1 / n0) - math.log(s1 / s0)


a_14r = logit_14r(50, 350, 1.0, 1 / 9)
wbm.record("MB2.14a", a_14r, decimals=6,
           mistakes={"le logit de la population retranche ln(s₁/s₀) au logit de l'échantillon : ici s₁ = 1 et s₀ = 1/9":
                         logit_14r(50, 350),
                     "keep_negative est le taux s₀ des négatifs : on retranche ln(s₁/s₀), on ne l'ajoute pas":
                         logit_14r(50, 350) + math.log(9)})
banners_14r = [(50, 350), (12, 40), (0, 25)]
wbm.record("MB2.14b", [logit_14r(a, b, 1.0, 1 / 9) for a, b in banners_14r], decimals=6,
           mistakes={"le logit de la population retranche ln(s₁/s₀) au logit de l'échantillon":
                         [logit_14r(a, b) for a, b in banners_14r],
                     "keep_negative est le taux s₀ des négatifs : on retranche ln(s₁/s₀), on ne l'ajoute pas":
                         [logit_14r(a, b, 1 / 9, 1.0) for a, b in banners_14r]})
c_14r = logit_14r(30, 120, 0.8, 0.025)
wbm.record("MB2.14c", [c_14r, 1 / (1 + math.exp(-c_14r))], decimals=6,
           mistakes={"la probabilité est σ(logit) = cote/(1 + cote), pas la cote e^logit": [c_14r, math.exp(c_14r)],
                     "keep_positive = 0,8 est le taux des positifs, keep_negative = 0,025 celui des négatifs":
                         [logit_14r(30, 120, 0.025, 0.8), 1 / (1 + math.exp(-logit_14r(30, 120, 0.025, 0.8)))],
                     "le logit de la population retranche ln(s₁/s₀) au logit de l'échantillon":
                         [logit_14r(30, 120), 1 / (1 + math.exp(-logit_14r(30, 120)))]})
X_14r = np.array([[2.0, 3, 4], [3.5, 4.5, 5.5], [5, 3, 4]])
means_14r = X_14r.mean(axis=1, keepdims=True)
R_14r = X_14r - means_14r                                              # removing (1, 1, 1) centers each animal (M20)
undivided_14r = X_14r - 3 * means_14r                                   # x - (x·u) u without dividing by u·u = 3
wbm.record("MB2.14d", R_14r.ravel().tolist() + [True], decimals=6,
           mistakes={"sans diviser par u·u, ta fonction ne retire la direction que si u est unitaire (relance ses tests)":
                         undivided_14r.ravel().tolist() + [False],
                     "on garde x moins sa projection sur u, pas la projection elle-même (relance les tests)":
                         np.repeat(means_14r, 3, axis=1).ravel().tolist() + [True]})
gap_14r = float(np.sum((X_14r[0] - X_14r[2]) ** 2) - np.sum((R_14r[0] - R_14r[2]) ** 2))
wbm.record("MB2.14e", gap_14r, decimals=6,
           mistakes={"e) compare les carrés des distances, pas les distances":
                         float(np.linalg.norm(X_14r[0] - X_14r[2]) - np.linalg.norm(R_14r[0] - R_14r[2])),
                     "sans diviser par u·u, ta fonction ne retire la direction que si u est unitaire (relance ses tests)":
                         float(np.sum((X_14r[0] - X_14r[2]) ** 2) - np.sum((undivided_14r[0] - undivided_14r[2]) ** 2))})'''),
    ],
)

PART_A = Part("A", "Ta librairie : la table des PMI ; le logit d'une population et le retrait d'une direction",
              "Fiche §2, §5 et §7. Les trois fonctions de `mymath/cooccurrence.py`, leurs tests, et un usage de chacune "
              "sur les données des exercices papier. La cellule de données ci-dessous recopie les données des exercices "
              "papier.",
              given=TOOLS + "\n\n\n" + DATA, exercises=[MB2_13, MB2_14])

# ---------------------------------------------------------------------------
# Notebook exercises: predict, draw (MB2.15, MB2.16)
# ---------------------------------------------------------------------------
GIVEN_15 = '''CELLS_15 = [(1, 0), (1, 1), (2, 3)]     # (prairie, huppe), (prairie, pic), (village, moineau): (row, column) of P
T_ALPHA_15 = 3                           # the smoothing of MB2.3: alpha = 1/3, a temperature T = 3'''

CHECK_15 = '''HIDDEN_C15 = __HIDDEN_C15__   # hidden calls: (law, seed, n_rep, n_obs) and the sub-IDs of their two arrays in answers.json

with checked("MB2.15"):
    results_15 = []
    report_15 = reporter(results_15, stop=False)
    law_15 = P                                            # the law of the notebook, put back after the hidden calls
    try:
        for law_c15, seed_c15, n_rep_c15, n_obs_c15, ids_c15 in HIDDEN_C15:
            P = np.array(law_c15)                         # your function reads P at the call
            got_c15 = pmi_samples_15(np.random.default_rng(seed_c15), n_rep_c15, n_obs_c15)
            P = law_15
            label_c15 = (f"un appel caché ({n_rep_c15} échantillons de {n_obs_c15} oiseaux, "
                         f"{'la loi des oiseaux' if np.allclose(law_c15, law_15) else 'une autre loi'})")
            if not isinstance(got_c15, (tuple, list)) or len(got_c15) != 2:
                report_15(False, "", f"{label_c15} : pmi_samples_15 doit rendre deux tableaux (sans, puis avec lissage), "
                                     f"reçu {shown(got_c15)}")
                continue
            plain_c15, smooth_c15 = (as_floats(a) for a in got_c15)
            if any(a is None or a.shape != (n_rep_c15, 3) for a in (plain_c15, smooth_c15)):
                report_15(False, "", f"{label_c15} : chaque tableau a la forme (n_rep, 3) = ({n_rep_c15}, 3), une ligne "
                                     "par échantillon et une colonne par case de CELLS_15")
                continue
            ok_plain, ok_smooth = passes(ids_c15[0], plain_c15.tolist()), passes(ids_c15[1], smooth_c15.tolist())
            if not ok_plain and not np.allclose(law_c15, law_15):
                again_c15 = pmi_samples_15(np.random.default_rng(seed_c15), n_rep_c15, n_obs_c15)
                if isinstance(again_c15, (tuple, list)) and matches(again_c15[0], plain_c15):
                    why_c15 = "ta fonction rend la même chose pour deux lois différentes : lis P au moment de l'appel"
                else:
                    why_c15 = "les PMI estimées sans lissage ne sont pas celles de l'énoncé"
            elif not ok_plain:
                why_c15 = ("les PMI estimées sans lissage : un échantillon par rng.multinomial(n_obs, P.ravel()), remis à "
                           "la forme (3, 4), puis pmi(comptes / n_obs), lues aux cases de CELLS_15, dans cet ordre")
            elif not ok_smooth:
                why_c15 = ("les PMI lissées : ln p̂(x, y) − ln p̂(x) − ln p̂_α(y), avec p̂_α la marge des espèces DE "
                           "L'ÉCHANTILLON tempérée à T = 3 (mymath.sampling.temper), −∞ sur une case vide")
            else:
                why_c15 = ""
            report_15(not why_c15, f"pmi_samples_15 : {label_c15}, comme attendu", f"pmi_samples_15, {label_c15} : {why_c15}")
    finally:
        P = law_15
    verdict("MB2.15", all(results_15) and len(results_15) == len(HIDDEN_C15),
            "ta fonction suit l'énoncé sur des appels cachés aussi.", "relis les lignes ❌ ci-dessus.")'''

NOTE_15 = (r"Prédictions attendues : a) $0{,}99^{400} \approx 0{,}018$ ; b) (B) ; c) (C). La huppe n'est vue qu'en prairie : "
           r"quand elle est vue, sa case a le compte de sa colonne, ils se simplifient, et l'estimation vaut "
           r"$\ln\frac{400}{n_{\text{prairie}}}$, très stable ; le lissage casse cette simplification. Le lissage déplace "
           r"la cible des cases rares (la vraie $\operatorname{PMI}_\alpha$), mais ne réduit pas la dispersion d'une case : "
           r"seuls plus d'observations, ou des pseudo-comptes (M04), le font.")

MB2_15 = Ex(
    "MB2.15", "🔮", 2, 20, "Prédire puis mesurer la dispersion de la PMI estimée sur 400 observations, pour une case rare "
    "et une case fréquente, avec et sans lissage",
    "prévoir ce que le nombre d'observations d'une case fait à sa PMI estimée, et ce que le lissage y change, puis le "
    "mesurer.", "fiche §2 et §3 ; M02c, M28 ; Ex MB2.2 et MB2.3", tracks="C", hypothesis=True, given=GIVEN_15,
    note=NOTE_15,
    body=r"""La loi des oiseaux de MB2.2 (`P`) est celle d'une région. Un observateur n'y voit que 400 oiseaux, tirés au hasard selon cette loi, et estime les PMI par `pmi(comptes / 400)`, puis, avec le lissage de MB2.3, par $\ln\frac{\hat p(x, y)}{\hat p(x)\,\hat p_\alpha(y)}$, où $\hat p_\alpha$ est la marge des espèces de l'échantillon tempérée à $T = 3$ (`mymath.sampling.temper`, M28). On suit trois cases (`CELLS_15`) : (prairie, huppe), dont l'espèce est rare et n'est vue qu'en prairie ; (prairie, pic), une case rare d'une espèce présente ailleurs ; (village, moineau), une case fréquente. **Avant d'exécuter quoi que ce soit**, prédis :
- a) la probabilité qu'un échantillon de 400 oiseaux ne contienne aucune huppe, ce qui rend $-\infty$ la PMI estimée de (prairie, huppe) (un nombre, 3 décimales, que tu calcules à la main) ;
- b) celle des trois cases dont la PMI estimée (finie) est la plus dispersée : (A) (prairie, huppe) ; (B) (prairie, pic) ; (C) (village, moineau) (une lettre) ;
- c) avec le lissage, l'écart-type de la PMI estimée de (prairie, huppe) : (A) diminue nettement ; (B) reste à peu près le même ; (C) augmente nettement (une lettre).

Puis, une fois tes prédictions écrites et vérifiées, écris `pmi_samples_15(rng, n_rep, n_obs=400)`, qui tire `n_rep` échantillons, chacun par `rng.multinomial(n_obs, P.ravel())` remis à la forme $(3, 4)$, et rend deux tableaux de forme `(n_rep, 3)` : les PMI estimées des trois cases, dans l'ordre de `CELLS_15`, sans puis avec lissage ($-\infty$ compris) ; `pmi_samples_15` lit `P` au moment de l'appel ; la vérification l'essaie sur des appels cachés, dont un sur une autre loi. Avec `rng = np.random.default_rng(7115)` et 1 000 échantillons, relève :
- d) la proportion des échantillons où la PMI estimée de (prairie, huppe) vaut $-\infty$ (un nombre ; 3 décimales dans ta copie) ;
- e) l'écart-type (`ddof=1`) des valeurs finies de chaque case, sans puis avec lissage, une ligne par case (un tableau de forme $(3, 2)$ ; 3 décimales dans ta copie) ;
- f) les vraies valeurs, $\operatorname{PMI}$ et $\operatorname{PMI}_\alpha$ de la loi `P` de la région, une ligne par case (un tableau de forme $(3, 2)$ ; 3 décimales dans ta copie) ;
- g) vrai ou faux : pour les deux cases rares, la moyenne des estimations lissées finies est plus proche de la vraie $\operatorname{PMI}_\alpha$ que de la vraie PMI.

La vérification de l'expérience ne s'exécute qu'une fois tes trois prédictions écrites. Ce qu'il faut observer (après l'expérience) : ce qui rend une estimation dispersée (le nombre d'oiseaux de la case), ce qui sauve (prairie, huppe) quand la huppe est vue (et ce qu'il en coûte quand elle ne l'est pas), ce que fait le lissage à la cible et ce qu'il ne fait pas à la dispersion.""",
    todo='''prediction_MB2_15a = ...  # a) a number (3 decimals), computed by hand BEFORE the experiment: the probability that 400 birds hold no hoopoe
prediction_MB2_15b = ...  # b) "A", "B" or "C": the cell whose estimated PMI (finite) is the most dispersed
prediction_MB2_15c = ...  # c) "A", "B" or "C": with the smoothing, the standard deviation of the estimated PMI of (prairie, huppe)''',
    check='''for letter, prediction in zip("abc", [prediction_MB2_15a, prediction_MB2_15b, prediction_MB2_15c]):
    wbm.check(f"MB2.15{letter}", prediction)''',
    record='''def samples_15r(law, seed, n_rep, n_obs=400, cells=((1, 0), (1, 1), (2, 3))):
    """The oracle: the draws of the statement, each PMI computed cell by cell with math.log; the smoothed margin of the
    species is n(y)^(1/3) renormalized (the tempered law at T = 3)."""
    rng, law = np.random.default_rng(seed), np.asarray(law, dtype=float)
    plain, smooth = [], []
    for _ in range(n_rep):
        counts = rng.multinomial(n_obs, law.ravel()).reshape(law.shape)
        rows, cols = counts.sum(axis=1), counts.sum(axis=0)
        roots = [c ** (1 / 3) for c in cols]
        alpha = [r / sum(roots) for r in roots]
        plain.append([math.log(counts[i, j] * n_obs / (rows[i] * cols[j])) if counts[i, j] else -math.inf
                      for i, j in cells])
        smooth.append([math.log(counts[i, j] / (rows[i] * alpha[j])) if counts[i, j] else -math.inf for i, j in cells])
    return np.array(plain), np.array(smooth)


def spread_15r(values):
    finite = values[np.isfinite(values)]
    return float(np.std(finite, ddof=1))


P_15r = np.array([[0.0, 6, 14, 20], [1, 2, 10, 22], [0, 0, 3, 22]]) / 100
plain_15r, smooth_15r = samples_15r(P_15r, 7115, 1000)
spreads_15r = [[spread_15r(plain_15r[:, k]), spread_15r(smooth_15r[:, k])] for k in range(3)]
no_hoopoe_15r = (1 - P_15r[:, 0].sum()) ** 400
wbm.record("MB2.15a", no_hoopoe_15r, decimals=3,
           mistakes={"aucun oiseau n'est une huppe : chacun des 400 tirages indépendants l'évite avec la probabilité "
                     "0,99": 1 - no_hoopoe_15r,
                     "400 × 0,01 est le nombre moyen de huppes, pas une probabilité": 400 * P_15r[:, 0].sum(),
                     "chaque oiseau évite la huppe avec la probabilité 1 − 0,01, pas 0,01": P_15r[:, 0].sum() ** 400})
most_15r = "ABC"[int(np.argmax([row[0] for row in spreads_15r]))]
wbm.record("MB2.15b", most_15r, prediction=True,
           mistakes={"quand la huppe est vue, elle ne l'est qu'en prairie : compare le compte de sa case à celui de sa "
                     "colonne, et ce qu'il reste dans le rapport": "A",
                     "une case fréquente a beaucoup d'oiseaux : sa proportion estimée varie peu": "C"})
ratio_15r = spreads_15r[0][1] / spreads_15r[0][0]
wbm.record("MB2.15c", "C" if ratio_15r > 1.5 else "A" if ratio_15r < 1 / 1.5 else "B", prediction=True,
           mistakes={"le lissage change la marge de la colonne, pas le nombre d'oiseaux de la case : il ne peut pas "
                     "réduire la dispersion d'une estimation": "A",
                     "avec le lissage, la marge lissée de la huppe ne varie plus comme le compte de sa case : écris "
                     "l'estimation en fonction du nombre de huppes vues": "B"})''',
    after=[
        ("md", "**L'expérience.** Écris-la une fois tes trois prédictions vérifiées ; sa vérification ne s'exécute qu'à cette "
               "condition."),
        ("todo", '''def pmi_samples_15(rng, n_rep, n_obs=400):
    """n_rep samples of n_obs birds, each drawn by rng.multinomial(n_obs, P.ravel()) (P read at the call) and reshaped to
    (3, 4): two arrays of shape (n_rep, 3), the estimated PMI of the cells CELLS_15 without, then with the smoothing of
    the species margin of the sample (mymath.sampling.temper at T = 3), -inf included."""
    raise NotImplementedError("pmi_samples_15 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB2_15d = answer_MB2_15e = answer_MB2_15f = answer_MB2_15g = ...
with wbm.attempt("MB2.15"):          # your function: ⏳ while it is not written
    answer_MB2_15d = ...  # d) a number, as computed: the proportion of samples where the estimated PMI of (prairie, huppe) is -inf (rng = np.random.default_rng(7115), 1 000 samples)
    answer_MB2_15e = ...  # e) a (3, 2) array, as computed: the standard deviations (ddof=1) of the finite values of each cell, without then with the smoothing
    answer_MB2_15f = ...  # f) a (3, 2) array: the true PMI, then the true PMI_alpha, of the law P, one row per cell
    answer_MB2_15g = ...  # g) True or False: for the two rare cells, the mean of the finite smoothed estimates is closer to the true PMI_alpha than to the true PMI'''),
        ("check", guarded(answers_check("MB2.15", "defg") + "\n\n" + CHECK_15,
                          [f"prediction_MB2_15{letter}" for letter in "abc"],
                          "⏳ Écris d'abord tes trois prédictions, puis exécute à nouveau.")),
        ("solution", '''def pmi_samples_15(rng, n_rep, n_obs=400):
    """n_rep samples of n_obs birds, each drawn by rng.multinomial(n_obs, P.ravel()) (P read at the call) and reshaped to
    (3, 4): two arrays of shape (n_rep, 3), the estimated PMI of the cells CELLS_15 without, then with the smoothing of
    the species margin of the sample (mymath.sampling.temper at T = 3), -inf included."""
    rows, cols = (list(index) for index in zip(*CELLS_15))
    plain, smooth = np.empty((n_rep, 3)), np.empty((n_rep, 3))
    for r in range(n_rep):
        joint = rng.multinomial(n_obs, P.ravel()).reshape(P.shape) / n_obs
        plain[r] = mymath.cooccurrence.pmi(joint)[rows, cols]
        p_x, p_alpha = joint.sum(axis=1), mymath.sampling.temper(joint.sum(axis=0), T_ALPHA_15)
        with np.errstate(divide="ignore", invalid="ignore"):
            smoothed = np.log(joint) - np.log(p_x)[:, None] - np.log(p_alpha)[None, :]
        smoothed[joint == 0] = -np.inf
        smooth[r] = smoothed[rows, cols]
    return plain, smooth


plain_15, smooth_15 = pmi_samples_15(np.random.default_rng(7115), 1000)
answer_MB2_15d = float(np.mean(np.isneginf(plain_15[:, 0])))
answer_MB2_15e = [[float(np.std(values[np.isfinite(values)], ddof=1)) for values in (plain_15[:, k], smooth_15[:, k])]
                  for k in range(3)]
true_15 = mymath.cooccurrence.pmi(P)
with np.errstate(divide="ignore"):
    true_alpha_15 = np.log(P) - np.log(P.sum(axis=1))[:, None] - np.log(mymath.sampling.temper(P.sum(axis=0), T_ALPHA_15))
answer_MB2_15f = [[float(true_15[cell]), float(true_alpha_15[cell])] for cell in CELLS_15]
means_15 = [float(np.mean(smooth_15[:, k][np.isfinite(smooth_15[:, k])])) for k in (0, 1)]
answer_MB2_15g = all(abs(m - answer_MB2_15f[k][1]) < abs(m - answer_MB2_15f[k][0]) for k, m in enumerate(means_15))
print("d)", answer_MB2_15d, " e)", np.round(answer_MB2_15e, 4).tolist())
print("f)", np.round(answer_MB2_15f, 4).tolist(), " g)", answer_MB2_15g, " (moyennes lissées :", np.round(means_15, 3).tolist(), ")")
print("   moyennes des estimations finies sans lissage :",
      [round(float(np.mean(plain_15[:, k][np.isfinite(plain_15[:, k])])), 3) for k in range(3)])

''' + answers_check("MB2.15", "defg") + "\n\n" + CHECK_15),
        ("record", '''wbm.record("MB2.15d", float(np.mean(np.isneginf(plain_15r[:, 0]))), decimals=6,
           mistakes={"d) est une proportion des 1 000 échantillons, pas un nombre d'échantillons":
                         float(np.sum(np.isneginf(plain_15r[:, 0]))),
                     "d) compte les échantillons où la PMI estimée VAUT −∞, ceux où aucune huppe n'est vue":
                         float(np.mean(np.isfinite(plain_15r[:, 0])))})
wbm.record("MB2.15e", spreads_15r, decimals=6,
           mistakes={"l'écart-type est celui de l'échantillon des estimations, avec ddof=1":
                         [[float(np.std(v[np.isfinite(v)])) for v in (plain_15r[:, k], smooth_15r[:, k])] for k in range(3)],
                     "une ligne par case : sans lissage, puis avec": [row[::-1] for row in spreads_15r]})
with np.errstate(divide="ignore"):
    roots_15r = P_15r.sum(axis=0) ** (1 / 3)
    true_15r = np.log(P_15r) - np.log(np.outer(P_15r.sum(axis=1), P_15r.sum(axis=0)))
    alpha_15r = np.log(P_15r) - np.log(np.outer(P_15r.sum(axis=1), roots_15r / roots_15r.sum()))
    cubes_15r = P_15r.sum(axis=0) ** 3
    wrong_alpha_15r = np.log(P_15r) - np.log(np.outer(P_15r.sum(axis=1), cubes_15r / cubes_15r.sum()))
cells_15r = ((1, 0), (1, 1), (2, 3))
wbm.record("MB2.15f", [[float(true_15r[c]), float(alpha_15r[c])] for c in cells_15r], decimals=6,
           mistakes={"la température T = 3 élève les probabilités à la puissance 1/T = 1/3":
                         [[float(true_15r[c]), float(wrong_alpha_15r[c])] for c in cells_15r],
                     "une ligne par case : la PMI, puis la PMI lissée": [[float(alpha_15r[c]), float(true_15r[c])] for c in cells_15r]})
means_15r = [float(np.mean(smooth_15r[:, k][np.isfinite(smooth_15r[:, k])])) for k in (0, 1)]
wbm.record("MB2.15g", all(abs(m - alpha_15r[c]) < abs(m - true_15r[c]) for m, c in zip(means_15r, cells_15r)),
           mistakes={"compare la moyenne des estimations lissées finies de chaque case rare à ses deux vraies valeurs, f)":
                         False})
for law_15r, seed_15r, n_rep_15r, n_obs_15r, ids_15r in __HIDDEN_C15__:      # the hidden calls of the check
    for sub_id_15r, values_15r in zip(ids_15r, samples_15r(law_15r, seed_15r, n_rep_15r, n_obs_15r)):
        wbm.record(sub_id_15r, values_15r.tolist(), decimals=6)'''),
        ("md", "**Après l'expérience**, dans ta copie : pourquoi (prairie, huppe) est-elle si peu dispersée tant que la "
               "huppe est vue ? Pourquoi le lissage la rend-il dispersée ? Que faudrait-il pour réduire la dispersion de "
               "(prairie, pic) ?"),
    ],
)

GIVEN_16 = '''SHOPS_16 = ["épicerie A", "épicerie B", "épicerie C", "quincaillerie A", "quincaillerie B", "quincaillerie C",
            "bazar A", "bazar B", "bazar C", "bazar D"]
PRODUCTS_16 = ["pain", "fruits", "fromage", "vis", "peinture"]
M_16 = np.array([[41.0, 29, 26, 2, 3], [33, 25, 19, 6, 4], [52, 41, 31, 4, 2],          # weekly sales (tens of items):
                 [4, 1, 0, 36, 27], [6, 3, 2, 49, 41], [0, 2, 1, 23, 21],              # one row per shop of SHOPS_16,
                 [26, 19, 15, 23, 18], [37, 29, 22, 14, 11], [11, 8, 7, 33, 24],       # one column per product
                 [22, 15, 14, 19, 13]])'''

CHECK_16 = '''HIDDEN_C16 = __HIDDEN_C16__   # a hidden table, its names, three other betas, and the sub-IDs of the arrays expected


def factors_why_c16(axes, M, betas, names, arrays, sub_id):
    """What is wrong in a call of draw_factors_16 (French phrases): the arrays returned, then the three panels."""
    if not isinstance(arrays, (list, tuple)) or len(arrays) != len(betas):
        return [f"draw_factors_16 doit rendre la liste des {len(betas)} tableaux tracés, reçu {shown(arrays)}"]
    arrays = [as_floats(a) for a in arrays]
    shape = (len(M), 2)
    if any(a is None or a.shape != shape for a in arrays):
        return [f"chaque tableau tracé a une ligne par ligne de M et deux colonnes : la forme {shape}"]
    problems = []
    if not passes(sub_id, [a.tolist() for a in arrays]):
        flipped = any(passes(sub_id, [(a * signs).tolist() for a in arrays]) for signs in ([-1, 1], [1, -1], [-1, -1]))
        problems.append("au signe près d'une colonne : prends la SVD de mymath.svd_pca.svd, qui suit la convention de "
                        "signe de M12d" if flipped else
                        "les tableaux tracés ne sont pas U₂S₂^β pour les β reçus (dans l'ordre de betas), à partir de la "
                        "SVD de la table reçue")
    for k, (ax, beta, a) in enumerate(zip(axes, betas, arrays)):
        missing = []
        if not points_at(ax, a[:, 0], a[:, 1]):
            missing.append("un point par ligne, à ses deux coordonnées (ax.scatter, ou ax.plot avec un marqueur)")
        if not set(names) <= {text.get_text().strip() for text in ax.texts}:
            missing.append("le nom de chaque ligne près de son point (ax.annotate ou ax.text)")
        if ax.get_aspect() not in (1.0, "equal"):
            missing.append('la même échelle sur les deux axes (ax.set_aspect("equal"))')
        if not ax.get_xlabel() or not ax.get_ylabel():
            missing.append("des noms d'axes")
        if not gives(ax.get_title(), [float(np.linalg.norm(a[:, 0]) / np.linalg.norm(a[:, 1]))]):
            missing.append("en titre, le rapport des longueurs des deux colonnes (un nombre)")
        if missing:
            problems.append(f"panneau {k + 1} (β = {fr(beta, 2)}) : il manque " + " ; ".join(missing))
    return problems


with checked("MB2.16"):
    results_16 = []
    report_16 = reporter(results_16, stop=False)
    fig_16, axes_16 = plt.subplots(1, 3, figsize=(16, 5.2))
    try:
        result_16 = []
        opened_16 = drawn(lambda: result_16.append(draw_factors_16(axes_16, M_16, (0, 0.5, 1), SHOPS_16)))
        problems_16 = factors_why_c16(axes_16, M_16, (0, 0.5, 1), SHOPS_16, result_16[0], "MB2.16g")
        report_16(not problems_16, "draw_factors_16 (β = 0, ½ et 1) : les trois tableaux, les points, les noms, l'échelle, "
                  "les noms d'axes et les titres", "draw_factors_16 : " + " ; ".join(problems_16))
        fig_c16, axes_c16 = plt.subplots(1, 4)             # the 4th axes is the current one: plt.scatter would draw there
        try:
            hidden_c16 = []
            opened_16 += drawn(lambda: hidden_c16.append(draw_factors_16(axes_c16[:3], np.array(HIDDEN_C16["table"]),
                                                                          HIDDEN_C16["betas"], HIDDEN_C16["names"])))
            problems_c16 = factors_why_c16(axes_c16[:3], HIDDEN_C16["table"], HIDDEN_C16["betas"], HIDDEN_C16["names"],
                                           hidden_c16[0], HIDDEN_C16["ids"][0])
            elsewhere_16 = bool(axes_c16[3].lines or axes_c16[3].collections or axes_c16[3].texts or axes_c16[3].get_title())
        finally:
            plt.close(fig_c16)
        report_16(not problems_c16, "un appel caché de draw_factors_16 (une autre table, d'autres β) est juste aussi",
                  "un appel caché de draw_factors_16 (une autre table, d'autres β) : " + " ; ".join(problems_c16))
        rows_c16 = factor_rows_16(np.array(HIDDEN_C16["table"]), HIDDEN_C16["beta"], k=3)
        ok_c16 = as_floats(rows_c16) is not None and np.shape(rows_c16) == (len(HIDDEN_C16["table"]), 3) and passes(
            HIDDEN_C16["ids"][1], as_floats(rows_c16).tolist())
        report_16(ok_c16, "factor_rows_16 sur la table cachée, avec k = 3 et un autre β, comme attendu",
                  f"factor_rows_16 sur la table cachée, avec k = 3 : attendu U₃S₃^β, de forme "
                  f"({len(HIDDEN_C16['table'])}, 3), reçu {shown(rows_c16)[:80]} (k est le nombre de colonnes gardées)")
        report_16(not opened_16 and not elsewhere_16, "tes fonctions dessinent dans les axes reçus",
                  "tes fonctions doivent dessiner dans les axes reçus (ax.scatter, ax.set_title…), sans ouvrir de figure ni "
                  "dessiner dans l'axe courant (plt.scatter, plt.title…)")
    except BaseException:
        plt.close(fig_16)
        raise
    fig_16.tight_layout()
    plt.show()
    verdict("MB2.16", all(results_16), "tes facteurs et tes trois panneaux sont justes.", "relis les lignes ❌ ci-dessus.")'''

NOTE_16 = (r"`factor_rows_16` : `U, s, Vt = mymath.svd_pca.svd(M)`, puis `U[:, :k] * s[:k] ** beta`. a) "
           r"$(192{,}37 ;\ 61{,}97 ;\ 6{,}10)$ : la table est presque de rang 2. b) $(-0{,}261 ;\ -0{,}058 ;\ 0{,}133)$. "
           r"c) $(0{,}808 ;\ 0{,}916 ;\ 0{,}969)$. d) $(1 ;\ 1{,}762 ;\ 3{,}104)$, soit $(s_1/s_2)^\beta$. e) Vrai. f) Faux : "
           r"la troisième valeur singulière, petite mais non nulle, écarte un peu les cosinus de $\mathbf{M}$ de ceux de "
           r"$\mathbf{M}_2$.")

MB2_16 = Ex(
    "MB2.16", "🎨", 1, 25, "Des magasins dans le plan des deux facteurs U₂S₂^β, pour β = 0, ½ et 1 : ce qui s'étire, et les "
    "angles qui changent",
    "dessiner les lignes d'une table dans le plan de U₂S₂^β pour trois β, et voir ce que la répartition des valeurs "
    "singulières change à la forme du nuage et aux angles.", "fiche §4 ; M07, M12d ; Ex MB2.4", tracks="C",
    given=GIVEN_16, note=NOTE_16,
    body=r"""Le notebook fournit `M_16`, les ventes hebdomadaires (en dizaines d'articles) de cinq produits (pain, fruits, fromage, vis, peinture) dans dix magasins : trois épiceries, trois quincailleries et quatre bazars, et `SHOPS_16`, leurs noms.

Écris `factor_rows_16(M, beta, k=2)`, qui rend $\mathbf{U}_k\mathbf{S}_k^\beta$ par ta fonction `mymath.svd_pca.svd` (M12d, avec sa convention de signe), puis `draw_factors_16(axes, M, betas, names)`, qui reçoit une ligne de trois axes et, pour chaque $\beta$ de `betas` (un axe chacun), place les lignes de $\mathbf{U}_2\mathbf{S}_2^\beta$ dans le plan de ses deux colonnes : un point et le nom de chaque ligne (`names`), une même échelle sur les deux axes (`ax.set_aspect("equal")`), des noms d'axes, et en titre $\beta$ et le rapport des longueurs (normes) de la première et de la seconde colonne ; elle rend la liste des trois tableaux tracés. Les deux fonctions dessinent dans les axes reçus, sans ouvrir de figure.

La vérification appelle `draw_factors_16` avec $\beta = 0$, $\frac12$ et 1, affiche la figure, compare tes tableaux aux réponses, et essaie tes fonctions sur une autre table, d'autres $\beta$ et $k = 3$ (des appels cachés). Relève :
- a) les trois plus grandes valeurs singulières de `M_16` (une liste de 3 nombres ; 2 décimales dans ta copie) ;
- b) le cosinus de l'épicerie A et de la quincaillerie A entre les lignes de $\mathbf{U}_2\mathbf{S}_2^\beta$, pour $\beta = 0$, $\frac12$ et 1 (une liste de 3 nombres ; 3 décimales dans ta copie) ;
- c) le même pour les bazars A et B ;
- d) le rapport des longueurs des deux colonnes de $\mathbf{U}_2\mathbf{S}_2^\beta$, pour les trois $\beta$ (une liste de 3 nombres ; 3 décimales dans ta copie) ;
- e) vrai ou faux : les cosinus entre les lignes de $\mathbf{U}_2\mathbf{S}_2$ sont ceux des lignes de $\mathbf{M}_2$, l'approximation de rang 2 (`mymath.svd_pca.low_rank_approximation`), à $10^{-9}$ près ;
- f) vrai ou faux : ce sont ceux des lignes de `M_16` elle-même, à $10^{-9}$ près.

Ce qu'il faut observer : quand $\beta$ monte, le nuage s'étire le long du premier axe, celui du profil moyen ; les magasins semblent alors plus proches les uns des autres ; $\beta = 1$ garde les angles de la table approchée, pas ceux de la table.""",
    todo='''def factor_rows_16(M, beta, k=2):
    """U_k S_k^beta for the compact SVD of M by mymath.svd_pca.svd (M12d, its sign convention): an array of shape
    (number of rows of M, k)."""
    raise NotImplementedError("factor_rows_16 n'est pas encore écrite (04_indices.md si tu bloques)")


def draw_factors_16(axes, M, betas, names):
    """axes: a row of 3 axes. For each beta of betas (one axes each): the rows of factor_rows_16(M, beta) as points in the
    plane of its two columns, the name of each row (names) next to its point, the same scale on both axes
    (ax.set_aspect("equal")), axis labels, and a title giving beta and the ratio of the lengths (norms) of the first and
    the second column. Returns the list of the 3 arrays drawn. Opens no figure."""
    raise NotImplementedError("draw_factors_16 n'est pas encore écrite (04_indices.md si tu bloques)")


answer_MB2_16a = answer_MB2_16b = answer_MB2_16c = answer_MB2_16d = answer_MB2_16e = answer_MB2_16f = ...
with wbm.attempt("MB2.16"):          # your functions: ⏳ while they are not written
    answer_MB2_16a = ...  # a) a list of 3 numbers, as computed: the three largest singular values of M_16
    answer_MB2_16b = ...  # b) a list of 3 numbers, as computed: cos(épicerie A, quincaillerie A) between the rows of U2 S2^beta, for beta = 0, 0.5, 1
    answer_MB2_16c = ...  # c) a list of 3 numbers, as computed: the same for bazar A and bazar B
    answer_MB2_16d = ...  # d) a list of 3 numbers, as computed: the ratio of the lengths of the two columns of U2 S2^beta, for beta = 0, 0.5, 1
    answer_MB2_16e = ...  # e) True or False: the cosines between the rows of U2 S2 are those of the rows of M2, to 1e-9
    answer_MB2_16f = ...  # f) True or False: they are those of the rows of M_16 itself, to 1e-9''',
    check=answers_check("MB2.16", "abcdef") + "\n\n" + CHECK_16,
    solution='''def factor_rows_16(M, beta, k=2):
    """U_k S_k^beta for the compact SVD of M by mymath.svd_pca.svd (M12d, its sign convention): an array of shape
    (number of rows of M, k)."""
    U, s, Vt = mymath.svd_pca.svd(M)
    return U[:, :k] * s[:k] ** beta


def draw_factors_16(axes, M, betas, names):
    """axes: a row of 3 axes. For each beta of betas (one axes each): the rows of factor_rows_16(M, beta) as points in the
    plane of its two columns, the name of each row (names) next to its point, the same scale on both axes
    (ax.set_aspect("equal")), axis labels, and a title giving beta and the ratio of the lengths (norms) of the first and
    the second column. Returns the list of the 3 arrays drawn. Opens no figure."""
    drawn_arrays = []
    for ax, beta in zip(axes, betas):
        A = factor_rows_16(M, beta)
        ax.scatter(A[:, 0], A[:, 1], s=18, color="tab:blue")
        for name, (x, y) in zip(names, A):
            ax.annotate(name, (x, y), textcoords="offset points", xytext=(4, 3), fontsize=7)
        ax.axhline(0, color="0.8", lw=0.8)
        ax.axvline(0, color="0.8", lw=0.8)
        ax.set_aspect("equal")
        ax.set_xlabel("première colonne de U₂S₂^β")
        ax.set_ylabel("seconde colonne")
        ratio = np.linalg.norm(A[:, 0]) / np.linalg.norm(A[:, 1])
        ax.set_title(f"β = {beta:g} ; rapport des longueurs {ratio:.3f}".replace(".", ","), fontsize=10)
        drawn_arrays.append(A)
    return drawn_arrays


def cosine_16(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


def all_cosines_16(Z):
    return np.array([cosine_16(Z[i], Z[j]) for i in range(len(Z)) for j in range(i + 1, len(Z))])


answer_MB2_16a = mymath.svd_pca.svd(M_16)[1][:3].tolist()
answer_MB2_16b = [cosine_16(*factor_rows_16(M_16, beta)[[0, 3]]) for beta in (0, 0.5, 1)]
answer_MB2_16c = [cosine_16(*factor_rows_16(M_16, beta)[[6, 7]]) for beta in (0, 0.5, 1)]
answer_MB2_16d = [float(np.linalg.norm(A[:, 0]) / np.linalg.norm(A[:, 1]))
                  for A in (factor_rows_16(M_16, beta) for beta in (0, 0.5, 1))]
cos_A_16 = all_cosines_16(factor_rows_16(M_16, 1))
answer_MB2_16e = bool(np.allclose(cos_A_16, all_cosines_16(mymath.svd_pca.low_rank_approximation(M_16, 2)), rtol=0, atol=1e-9))
answer_MB2_16f = bool(np.allclose(cos_A_16, all_cosines_16(M_16), rtol=0, atol=1e-9))
print("a)", np.round(answer_MB2_16a, 4).tolist(), " b)", np.round(answer_MB2_16b, 4).tolist(),
      " c)", np.round(answer_MB2_16c, 4).tolist())
print("d)", np.round(answer_MB2_16d, 4).tolist(), " e)", answer_MB2_16e, " f)", answer_MB2_16f,
      " (plus grand écart :", round(float(np.abs(cos_A_16 - all_cosines_16(M_16)).max()), 4), ")")

''' + answers_check("MB2.16", "abcdef") + "\n\n" + CHECK_16,
    record='''from scipy import linalg as linalg_16r


def factors_16r(M, beta, k=2):
    """The oracle: scipy.linalg.svd, the sign convention of M12d (the entry of largest absolute value of each right
    singular vector made positive), then U_k S_k^beta."""
    U, s, Vt = linalg_16r.svd(np.asarray(M, dtype=float), full_matrices=False)
    for j in range(len(s)):
        if Vt[j, np.argmax(np.abs(Vt[j]))] < 0:
            U[:, j], Vt[j] = -U[:, j], -Vt[j]
    return U[:, :k] * s[:k] ** beta


def cos_16r(a, b):
    return float(np.dot(a, b) / math.sqrt(np.dot(a, a) * np.dot(b, b)))


M_16r = np.array([[41.0, 29, 26, 2, 3], [33, 25, 19, 6, 4], [52, 41, 31, 4, 2], [4, 1, 0, 36, 27], [6, 3, 2, 49, 41],
                  [0, 2, 1, 23, 21], [26, 19, 15, 23, 18], [37, 29, 22, 14, 11], [11, 8, 7, 33, 24], [22, 15, 14, 19, 13]])
s_16r = linalg_16r.svdvals(M_16r)
wbm.record("MB2.16a", s_16r[:3].tolist(), decimals=6,
           mistakes={"les valeurs singulières sont les racines des valeurs propres de MᵀM, pas ces valeurs propres":
                         (s_16r[:3] ** 2).tolist(),
                     "les trois plus grandes, par ordre décroissant": s_16r[::-1][:3].tolist()})
betas_16r = (0, 0.5, 1)
for letter_16r, (i_16r, j_16r) in (("b", (0, 3)), ("c", (6, 7))):
    values_16r = [cos_16r(factors_16r(M_16r, b)[i_16r], factors_16r(M_16r, b)[j_16r]) for b in betas_16r]
    wbm.record(f"MB2.16{letter_16r}", values_16r, decimals=6,
               mistakes={"la liste suit l'ordre β = 0, ½, 1": values_16r[::-1],
                         "β = ½ multiplie chaque colonne par √s_k, pas par s_k/2":
                             [values_16r[0], values_16r[2], values_16r[2]],
                         "le cosinus se mesure entre les lignes de U₂S₂^β, pas entre celles de M_16":
                             [cos_16r(M_16r[i_16r], M_16r[j_16r])] * 3})
ratios_16r = [float(np.linalg.norm(factors_16r(M_16r, b)[:, 0]) / np.linalg.norm(factors_16r(M_16r, b)[:, 1]))
              for b in betas_16r]
wbm.record("MB2.16d", ratios_16r, decimals=6,
           mistakes={"le rapport de la première colonne à la seconde, ‖col₁‖/‖col₂‖": [1 / r for r in ratios_16r],
                     "la longueur d'une colonne est sa norme, pas la somme de ses coordonnées":
                         [float(np.sum(factors_16r(M_16r, b)[:, 0]) / np.sum(factors_16r(M_16r, b)[:, 1]))
                          for b in betas_16r]})


def pair_cosines_16r(Z):
    return np.array([cos_16r(Z[i], Z[j]) for i in range(len(Z)) for j in range(i + 1, len(Z))])


U_16r, S_16r, Vt_16r = linalg_16r.svd(M_16r, full_matrices=False)
M2_16r = (U_16r[:, :2] * S_16r[:2]) @ Vt_16r[:2]
wbm.record("MB2.16e", bool(np.allclose(pair_cosines_16r(factors_16r(M_16r, 1)), pair_cosines_16r(M2_16r), rtol=0, atol=1e-9)),
           mistakes={"(U₂S₂)(U₂S₂)ᵀ = M₂M₂ᵀ : compare les cosinus de toutes les paires de lignes": False})
wbm.record("MB2.16f", bool(np.allclose(pair_cosines_16r(factors_16r(M_16r, 1)), pair_cosines_16r(M_16r), rtol=0, atol=1e-9)),
           mistakes={"M_16 n'est pas exactement de rang 2 : compare ses cosinus à ceux de U₂S₂, paire par paire": True})
wbm.record("MB2.16g", [factors_16r(M_16r, b).tolist() for b in betas_16r], decimals=6)        # the arrays drawn
HIDDEN_16r = __HIDDEN_C16__                                                                 # the hidden calls of the check
wbm.record(HIDDEN_16r["ids"][0], [factors_16r(HIDDEN_16r["table"], b).tolist() for b in HIDDEN_16r["betas"]], decimals=6)
wbm.record(HIDDEN_16r["ids"][1], factors_16r(HIDDEN_16r["table"], HIDDEN_16r["beta"], k=3).tolist(), decimals=6)''',
    after=[
        ("md", "**Après la figure**, dans ta copie : quels magasins se rapprochent quand $\\beta$ monte, et pourquoi ? Quel "
               "$\\beta$ choisirais-tu pour comparer les magasins par le cosinus, et pour comparer les produits ?"),
    ],
)

PART_B = Part("B", "Prédire, dessiner",
              "Fiche §2, §3 et §4. La dispersion d'une PMI estimée, prédite puis mesurée ; des magasins dans le plan des "
              "deux facteurs d'une SVD tronquée.",
              exercises=[MB2_15, MB2_16])
