#!/usr/bin/env python
"""Build the two notebooks of chapter M02c from a single source (used by Claude).

    python tools/chapters/build_m02c.py
    python tools/run_all_notebooks.py chapitres/m02c_echantillons_estimation/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m02c_echantillons_estimation/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M02c.1 to M02c.10, 🔗 M02c.13 and M02c.14); parts A to C are the notebook
exercises. Wrong-answer messages state a rule, never a number of the answer nor the calculation that gives it. The
quantiles of a series follow the convention of the sheet (NumPy's linear method), the values of Φ the table of M02b.
The simulations of parts A and B are deterministic: either the learner's function replays a seeded generator in the
order fixed by its docstring, or the samples are drawn once in a given cell and the learner computes on them.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M02c"
FOLDER = "chapitres/m02c_echantillons_estimation"

F = 'kind="fraction", simplified=True'
SMALLEST = 'fractional="le plus petit entier qui convient : l\'arrondi supérieur, pas l\'arrondi le plus proche."'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M02c.1", "Les statistiques d'une petite série : moyenne, médiane, quartiles, variance", [
        ("a", "a number (2 decimals)", "360 / 8",
         'decimals=2, mistakes={"c\'est la médiane ; la moyenne est la somme des valeurs divisée par leur nombre": 43.5, '
         '"divise la somme par le nombre de valeurs, 8": 360 / 7}'),
        ("b", "a number (2 decimals)", "(42 + 45) / 2",
         'decimals=2, mistakes={"la médiane se lit sur la série triée": 42.5, '
         '"avec 8 valeurs, la médiane est la moyenne des deux valeurs du milieu": {42.0, 45.0}}'),
        ("c", "an integer", "328",
         'mistakes={"les carrés des écarts, pas les écarts : la somme des écarts vaut toujours 0": 0, '
         '"c\'est la somme des carrés des valeurs ; il faut celle des carrés des écarts à la moyenne": 16528}'),
        ("d", "a number (2 decimals)", "328 / 8",
         'decimals=2, mistakes={"c\'est la variance divisée par n − 1 ; ici, on divise par n": 328 / 7, '
         '"c\'est un écart-type ; la variance est son carré": 41 ** 0.5}'),
        ("e", "a number (3 decimals)", "328 / 7",
         'decimals=3, mistakes={"c\'est la variance divisée par n ; ici, on divise par n − 1": 41.0}'),
        ("f", "a number (2 decimals)", "39 + 0.75 * (40 - 39)",
         'decimals=2, mistakes={"la convention de la fiche : position p(n − 1) dans la série triée numérotée à partir '
         'de 0, puis interpolation linéaire entre les deux voisines": {39.0, 39.25, 39.5, 40.0}}'),
        ("g", "a number (2 decimals)", "47 + 0.25 * (51 - 47)",
         'decimals=2, mistakes={"la convention de la fiche : position p(n − 1) dans la série triée numérotée à partir '
         'de 0, puis interpolation linéaire entre les deux voisines": {47.0, 49.0, 50.0, 51.0}}'),
        ("h", "a number (2 decimals)", "48 - 39.75",
         'decimals=2, mistakes={"l\'écart interquartile est Q3 − Q1, pas l\'étendue": 20.0}'),
    ]),

    Paper("M02c.2", "z-scores, écart interquartile et valeurs aberrantes", [
        ("a", "a number (1 decimal)", "157 / 10",
         'decimals=1, mistakes={"c\'est la médiane ; la moyenne est la somme divisée par n": 14.0}'),
        ("b", "a number (3 decimals)", "(272.1 / 10) ** 0.5",
         'decimals=3, mistakes={"l\'énoncé demande s_n, qui divise par n": (272.1 / 9) ** 0.5, '
         '"c\'est la variance ; l\'écart-type est sa racine": 27.21}'),
        ("c", "a number (2 decimals)", "(31 - 15.7) / (272.1 / 10) ** 0.5",
         'decimals=2, mistakes={"z = (x − x̄)/s : divise par l\'écart-type, pas par la variance": 15.3 / 27.21, '
         '"l\'énoncé demande s_n, qui divise par n": (31 - 15.7) / (272.1 / 9) ** 0.5}'),
        ("d", "True or False", "False", 'mistakes={"compare |z| de c) à 3": True}'),
        ("e", "a number (2 decimals)", "13 + 0.25 * (14 - 13)",
         'decimals=2, mistakes={"la convention de la fiche : position p(n − 1) dans la série triée numérotée à partir '
         'de 0, puis interpolation linéaire": {13.0, 13.5, 14.0}}'),
        ("f", "a number (3 decimals)", "15 + 1.5 * (15 - 13.25)",
         'decimals=3, mistakes={"c\'est la barrière basse ; la barrière haute part de Q3": 13.25 - 1.5 * 1.75, '
         '"le facteur 1,5 multiplie l\'écart interquartile": 15 + 1.75}'),
        ("g", "True or False", "True", 'mistakes={"compare 31 à la barrière de f)": False}'),
        ("h", "a number (1 decimal)", "(31 - 14) / (12 / 9) ** 0.5",
         'decimals=1, mistakes={"avec la moyenne et l\'écart-type des 9 autres valeurs, sans 31": '
         '(31 - 15.7) / (272.1 / 10) ** 0.5, "l\'énoncé demande s_n, qui divise par le nombre de valeurs, ici 9": '
         '(31 - 14) / (12 / 8) ** 0.5}'),
    ]),

    Paper("M02c.3", "Imputer par la moyenne ou la médiane : ce qui change", [
        ("a", "a number (2 decimals)", "60 / 6",
         'decimals=2, mistakes={"la moyenne des 6 réponses : divise par 6": 60 / 8}'),
        ("b", "a number (2 decimals)", "(7 + 9) / 2",
         'decimals=2, mistakes={"avec 6 valeurs, la médiane est la moyenne des deux valeurs du milieu": {7.0, 9.0}}'),
        ("c", "a number (2 decimals)", "258 / 6",
         'decimals=2, mistakes={"l\'énoncé divise par le nombre de valeurs, n, pas par n − 1": 258 / 5}'),
        ("d", "a number (2 decimals)", "80 / 8",
         'decimals=2, mistakes={"une valeur manquante n\'est pas un zéro : on la remplace par la moyenne": 60 / 8}'),
        ("e", "a number (2 decimals)", "258 / 8",
         'decimals=2, mistakes={"les deux valeurs imputées comptent : il y a maintenant 8 valeurs": 43.0}'),
        ("f", "a number (3 decimals)", "(6 / 8) ** 0.5",
         'decimals=3, mistakes={"le rapport des écarts-types, pas celui des variances": 6 / 8}'),
        ("g", "a number (2 decimals)", "76 / 8",
         'decimals=2, mistakes={"on ajoute deux valeurs égales à la médiane, pas à la moyenne": 10.0}'),
        ("h", "a number (2 decimals)", "8.0", 'decimals=2'),
    ]),

    Paper("M02c.4", "Avec ou sans remise : la variance de la moyenne", [
        ("a", "an integer", "8",
         'mistakes={"c\'est la variance d\'une population : divise par N = 5": 10}'),
        ("b", "an integer", "4",
         'mistakes={"V(X̄) = σ²/n : la moyenne de n tirages varie moins qu\'un tirage": 8, '
         '"σ²/n, pas σ²/n² : la somme a pour variance n σ²": 2}'),
        ("c", "an integer", "10",
         'mistakes={"sans tenir compte de l\'ordre : chaque paire est comptée une fois": 20, '
         '"sans remise, une boule ne sort pas deux fois": 15}'),
        ("d", "an integer", "6", ''),
        ("e", "an integer", "3",
         'mistakes={"c\'est la variance avec remise ; sans remise, les tirages sont dépendants": 4}'),
        ("f", "an integer", "-2",
         'mistakes={"sans remise, un grand numéro tiré en laisse moins de grands : la covariance est négative": 2}'),
        ("g", "an irreducible fraction, as text", "Fraction(3, 4)",
         F + ', mistakes={"sans remise divisé par avec remise, dans cet ordre": "4/3"}'),
        ("h", "a number (4 decimals)", "(10_000 - 100) / (10_000 - 1)",
         'decimals=4, mistakes={"le dénominateur est N − 1, pas N": (10_000 - 100) / 10_000}'),
    ]),

    Paper("M02c.5", "Combien d'observations pour une moyenne précise à 1 % ?", [
        ("a", "a number (2 decimals)", "2 / 16 ** 0.5",
         'decimals=2, mistakes={"l\'écart-type de la moyenne divise σ par √n, pas par n": 2 / 16}'),
        ("b", "a number (2 decimals)", "1.96 * 2 / 16 ** 0.5",
         'decimals=2, mistakes={"c\'est l\'écart-type de X̄ ; à 95 %, la demi-largeur le multiplie par le quantile '
         'de la loi normale": 0.5}'),
        ("c", "an integer", "62",
         SMALLEST + ', mistakes={"avec ce n, la demi-largeur dépasse encore 0,5 W": 61}'),
        ("d", "a number (3 decimals)", "4 / (62 * 0.5 ** 2)",
         'decimals=3, mistakes={"Bienaymé-Tchebychev utilise la variance σ², pas l\'écart-type": 2 / (62 * 0.25)}'),
        ("e", "an integer", "320", SMALLEST),
        ("f", "an integer", "4",
         'mistakes={"la demi-largeur varie en 1/√n, pas en 1/n": 2}'),
        ("g", "a number (2 decimals)", "2 / 400 ** 0.5",
         'decimals=2, mistakes={"l\'écart-type de la moyenne divise σ par √n, pas par n": 2 / 400}'),
        ("h", "an integer", "246",
         SMALLEST + ', mistakes={"avec ce n, la demi-largeur dépasse encore 0,5 W": 245, '
         '"recalcule avec σ = 4 W": 62}'),
    ]),

    Paper("M02c.6", "Le théorème central limite à la main : une somme de 100 variables", [
        ("a", "a number (2 decimals)", "-1 * 0.5 + 0 * 0.3 + 4 * 0.2",
         'decimals=2, mistakes={"pondère chaque valeur par sa probabilité": 1.0}'),
        ("b", "a number (2 decimals)", "(1 * 0.5 + 16 * 0.2) - 0.3 ** 2",
         'decimals=2, mistakes={"V(X) = E[X²] − E[X]² : retire le carré de l\'espérance": 3.7, '
         '"c\'est l\'écart-type ; la variance est son carré": 1.9}'),
        ("c", "a number (1 decimal)", "100 * 0.3",
         'decimals=1, mistakes={"S additionne 100 jours : la linéarité de l\'espérance": 0.3}'),
        ("d", "a number (1 decimal)", "(100 * 3.61) ** 0.5",
         'decimals=1, mistakes={"les variances s\'additionnent, pas les écarts-types": 190.0, '
         '"c\'est la variance de S ; l\'écart-type est sa racine": 361.0}'),
        ("e", "a number (4 decimals)", "1 - 0.8413",
         'decimals=4, mistakes={"c\'est P(S ≤ 49) ; P(S > 49) est l\'événement contraire": 0.8413}'),
        ("f", "a number (3 decimals)", "2 * 0.8413 - 1",
         'decimals=3, mistakes={"l\'événement a deux côtés de l\'espérance : retire la queue de gauche aussi": 0.8413}'),
        ("g", "a number (2 decimals)", "1.9 / 10",
         'decimals=2, mistakes={"c\'est σ(S) ; le gain moyen divise S par 100": 19.0, '
         '"l\'écart-type d\'une moyenne divise σ par √n, pas par n": 1.9 / 100}'),
        ("h", "an integer", "155",
         SMALLEST + ', mistakes={"avec ce n, la probabilité reste un peu sous 0,975": 154}'),
    ]),

    Paper("M02c.7", "Biais, variance et erreur quadratique de trois estimateurs", [
        ("a", "a number (2 decimals)", "3 * 6 / 4 - 6",
         'decimals=2, mistakes={"le biais est E[T₃] − μ, dans cet ordre": 1.5, '
         '"le biais est E[T₃] − μ, pas E[T₃]": 4.5}'),
        ("b", "an integer", "3",
         'mistakes={"V(T₂) n\'est pas σ² : la moyenne de trois variables indépendantes varie moins": 9, '
         '"V(X₁ + X₂ + X₃) = 3σ², puis V(aY) = a² V(Y)": 1}'),
        ("c", "an irreducible fraction, as text", "Fraction(27, 16)",
         F + ', mistakes={"la somme contient trois variables de variance σ²": "9/16", '
         '"diviser par 4 divise la variance par 4²": "27/4"}'),
        ("d", "a number (4 decimals)", "1.5 ** 2 + 27 / 16",
         'decimals=4, mistakes={"EQM = biais² + variance : le biais compte au carré": 27 / 16 + 1.5, '
         '"EQM = biais² + variance : les deux s\'additionnent": 27 / 16 - 1.5 ** 2}'),
        ("e", "an integer (1, 2 or 3)", "2",
         'mistakes={"compare l\'EQM de T₃ (d) à celle de T₂, qui est sans biais": 3}'),
        ("f", "a number (4 decimals)", "0.5 ** 2 + 27 / 16",
         'decimals=4, mistakes={"recalcule le biais de T₃ avec μ = 2": 1.5 ** 2 + 27 / 16}'),
        ("g", "an integer (1, 2 or 3)", "3",
         'mistakes={"recalcule l\'EQM de T₃ avec μ = 2, puis compare-la à celle de T₂": 2}'),
        ("h", "a number (3 decimals)", "21 ** 0.5",
         'decimals=3, mistakes={"c\'est m² ; la question demande m": 21.0}'),
    ]),

    Paper("M02c.8", "Erreur type et intervalle de confiance d'une moyenne", [
        ("a", "a number (2 decimals)", "14 / 49 ** 0.5",
         'decimals=2, mistakes={"l\'erreur type divise s par √n, pas par n": 14 / 49}'),
        ("b", "a list [low, high] (2 decimals)", "[120.5 - 1.96 * 2, 120.5 + 1.96 * 2]",
         'decimals=2, mistakes={"l\'intervalle utilise l\'erreur type de a), pas l\'écart-type des données": '
         '[120.5 - 1.96 * 14, 120.5 + 1.96 * 14], "à 95 %, la demi-largeur multiplie l\'erreur type par le quantile '
         'de la loi normale": [118.5, 122.5]}'),
        ("c", "a number (2 decimals)", "2 * 1.96 * 2",
         'decimals=2, mistakes={"c\'est la demi-largeur ; la largeur va de la borne basse à la borne haute": 3.92}'),
        ("d", "a number (2 decimals)", "1.645 * 2",
         'decimals=2, mistakes={"à 90 %, le quantile n\'est pas celui de 95 %": 3.92}'),
        ("e", "an integer", "189",
         SMALLEST + ', mistakes={"avec ce n, la demi-largeur dépasse encore 2 ms": 188}'),
        ("f", "a number (3 decimals)", "(0.9 * 0.1 / 400) ** 0.5",
         'decimals=3, mistakes={"l\'erreur type est la racine de p̂(1 − p̂)/n": 0.9 * 0.1 / 400}'),
        ("g", "a number (4 decimals)", "1.96 * (0.9 * 0.1 / 400) ** 0.5",
         'decimals=4, mistakes={"c\'est l\'erreur type ; la demi-largeur à 95 % la multiplie par le quantile": 0.015}'),
        ("h", "True or False", "False", 'mistakes={"compare 0,02 à la demi-largeur de g)": True}'),
    ]),

    Paper("M02c.9", "La variance d'une somme et la covariance : V(X + Y), V(X − Y)", [
        ("a", "a number (2 decimals)", "3 / (4 ** 0.5 * 9 ** 0.5)",
         'decimals=2, mistakes={"ρ divise la covariance par le produit des écarts-types, pas des variances": 3 / 36}'),
        ("b", "an integer", "4 + 9 + 2 * 3",
         'mistakes={"n\'oublie pas le terme de covariance": 13, "le terme de covariance compte deux fois": 16}'),
        ("c", "an integer", "4 + 9 - 2 * 3",
         'mistakes={"V(Y) s\'ajoute aussi pour une différence : une variance n\'est jamais retranchée": {1, -11, -5}, '
         '"pour une différence, le terme de covariance change de signe": 19}'),
        ("d", "an integer", "4 * 4 + 9 - 2 * 2 * 3",
         'mistakes={"V(2X) = 4 V(X) : le facteur compte au carré": 5, '
         '"le terme de covariance porte le produit des deux coefficients, ici négatif": 37}'),
        ("e", "an integer", "2 * 3",
         'mistakes={"Cov(aX, Y) = a Cov(X, Y) : le facteur compte": 3, "le facteur compte une fois, pas au carré": 12}'),
        ("f", "a number (2 decimals)", "16 / 4",
         'decimals=2, mistakes={"la moyenne des produits des écarts : divise leur somme par n = 4": 16.0, '
         '"l\'énoncé divise par n = 4, pas par n − 1": 16 / 3}'),
        ("g", "a number (3 decimals)", "4 / (2.5 * 7.5) ** 0.5",
         'decimals=3, mistakes={"r divise la covariance par le produit des écarts-types, pas des variances": '
         '4 / (2.5 * 7.5)}'),
        ("h", "a number (2 decimals)", "2.5 + 7.5 + 2 * 4",
         'decimals=2, mistakes={"n\'oublie pas le terme de covariance": 10.0}'),
    ]),

    Paper("M02c.10", "La matrice de covariance de trois variables : la lire et la vérifier", [
        ("a", "an integer", "9",
         'mistakes={"la diagonale contient les variances, pas les écarts-types": 3}'),
        ("b", "an integer", "-1", ''),
        ("c", "an irreducible fraction, as text", "Fraction(1, 3)",
         F + ', mistakes={"la corrélation divise par le produit des écarts-types, racines des variances": "1/18"}'),
        ("d", "True or False", "True", 'mistakes={"lis la case de la ligne 2, colonne 3": False}'),
        ("e", "an integer", "16",
         'mistakes={"les covariances comptent, et chacune deux fois (Σᵢⱼ et Σⱼᵢ)": {14, 15}}'),
        ("f", "an integer", "7",
         'mistakes={"le terme −2 Cov(X₁, X₃) change de signe quand la covariance est négative": 3, '
         '"une différence ajoute aussi la variance de X₃": 5}'),
        ("g", "a letter, as text", '"B"',
         'mistakes={"vérifie pour chaque tableau la symétrie, puis que la corrélation reste entre −1 et 1": '
         '{"A", "C"}}'),
        ("h", "an integer", "9",
         'mistakes={"n\'oublie pas les termes hors de la diagonale (i ≠ j)": 17}'),
    ]),

    Paper("M02c.13", "Le 99e percentile d'une latence : l'estimer et dire son incertitude", [
        ("a", "a number (2 decimals)", "0.99 * 999",
         'decimals=2, mistakes={"la convention de la fiche : h = p(n − 1), avec n − 1 = 999": 990.0}'),
        ("b", "a number (2 decimals)", "179 + 0.01 * (182 - 179)",
         'decimals=2, mistakes={"interpole entre les deux valeurs qui encadrent la position h": {179.0, 182.0}}'),
        ("c", "a number (3 decimals)", "290 + 0.001 * (412 - 290)",
         'decimals=3, mistakes={"interpole entre les deux valeurs qui encadrent la position h": {290.0, 412.0}}'),
        ("d", "an integer", "10",
         'mistakes={"compte les mesures au-dessus du quantile, pas en dessous": 990}'),
        ("e", "a number (3 decimals)", "(1000 * 0.01 * 0.99) ** 0.5",
         'decimals=3, mistakes={"c\'est la variance ; l\'écart-type est sa racine": 9.9, '
         '"la binomiale a pour variance n p (1 − p)": 10 ** 0.5}'),
        ("f", "a number (2 decimals)", "-40 * math.log(0.01)",
         'decimals=2, mistakes={"la loi exponentielle d\'espérance 40 a pour paramètre λ = 1/40": '
         '-math.log(0.01) / 40, "au-dessus de q_0,99, il reste 1 % des valeurs, pas 99 %": -40 * math.log(0.99)}'),
        ("g", "an integer", "10_000",
         'mistakes={"au-dessus de q_0,999, il y a 0,1 % des mesures, pas 1 %": 1000}'),
    ]),

    Paper("M02c.14", "Standardiser des features avec les statistiques du seul train", [
        ("a", "a number (2 decimals)", "70 / 5", 'decimals=2'),
        ("b", "a number (3 decimals)", "8 ** 0.5",
         'decimals=3, mistakes={"l\'énoncé demande s_n, qui divise par n": 10 ** 0.5, '
         '"c\'est la variance ; l\'écart-type est sa racine": 8.0}'),
        ("c", "a number (3 decimals)", "(20 - 14) / 8 ** 0.5",
         'decimals=3, mistakes={"standardise avec la moyenne et l\'écart-type du jeu d\'entraînement": '
         '(20 - 103 / 7) / 3.238795442501324}'),
        ("d", "a number (3 decimals)", "(13 - 14) / 8 ** 0.5",
         'decimals=3, mistakes={"13 est sous la moyenne du train : son z-score est négatif": 1 / 8 ** 0.5}'),
        ("e", "a number (3 decimals)", "103 / 7",
         'decimals=3, mistakes={"la moyenne des 7 valeurs, train et test réunis": 14.0}'),
        ("f", "a number (3 decimals)", "(20 - 103 / 7) / 3.238795442501324",
         'decimals=3, mistakes={"cette fois, la moyenne et l\'écart-type des 7 valeurs": (20 - 14) / 8 ** 0.5}'),
        ("g", "a number (2 decimals)", "0.0", 'decimals=2'),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements (Φ: the values of the table of M02b, §3)
import math
from fractions import Fraction'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M02c.1 à M02c.10, 🔗 M02c.13 et M02c.14)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"5/9\"` ;\n"
               "- une liste `[116.5, 124.5]`, `True` / `False`, ou une lettre entre guillemets, `\"B\"`.\n\n"
               "Pour la loi normale, utilise la table de $\\Phi$ de M02b (§3) : les réponses attendues sont arrondies de "
               "sorte que la table et un calcul exact donnent la même valeur. Les quantiles d'une série suivent la "
               "convention de la fiche (§1). Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M02c.18 to M02c.21)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from wbm.nbtools import checked, drawn, run_pytest_group, verdict


def raised(function, *args):
    """The name of the exception that function(*args) raises, or "aucune" if it returns.

    NotImplementedError (a TODO not done yet) goes through, for wbm.attempt to show ⏳."""
    try:
        function(*args)
    except NotImplementedError:
        raise
    except Exception as exc:  # noqa: BLE001 - any other error is the answer
        return type(exc).__name__
    return "aucune"'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M02c")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M02b). Ouvre ta copie `mon_travail/mymath/estimation.py`, lis la "
         "docstring de la fonction en entier, remplace la ligne `raise NotImplementedError(...)` par ton code, "
         "**enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "NumPy est permis (importe-le en haut du fichier), `scipy.stats` non : les tests comparent tes résultats à "
         "lui, et un test vérifie que tu ne t'en sers pas. Le hasard vient toujours d'**un seul** générateur "
         "`np.random.default_rng(seed)`, créé une fois au début de la fonction, et utilisé dans l'ordre que dit la "
         "docstring : c'est ce qui rend tes résultats identiques à ceux de la référence. Chaque nombre renvoyé est un "
         "`float` de Python (`float(...)` convertit un nombre de NumPy).")

WRONG_ERROR = "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)"
OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ZeroDivisionError"]


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of estimation.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m02c_estimation.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m02c_estimation.py", "{keyword}", impl="ref")')]


PY_FLOAT = ('mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy": '
            '{{"float64", "int", "ndarray"}}}}')

M02C_18 = Ex(
    "M02c.18", "🔨", 1, 20, "La distribution des moyennes d'échantillons · `sample_means`",
    "simuler beaucoup d'échantillons, calculer leurs moyennes, et vérifier la loi des grands nombres et le théorème "
    "central limite sur ces moyennes.", "fiche §3 à §5", tracks="C, E", mymath="estimation.py",
    body=HOWTO + """

Écris `sample_means(draw, n, repeats, seed=0)` : un générateur `rng = np.random.default_rng(seed)`, puis `repeats` appels `draw(rng, n)`, **l'un après l'autre**, et la moyenne de chaque échantillon, dans un array NumPy de forme `(repeats,)`. `draw` peut renvoyer une liste ou un array. $n < 1$ ou `repeats` $< 1$ lèvent une `ValueError`.

Dans la vérification, `expo` tire $n$ valeurs de la loi exponentielle d'espérance 2 (`rng.exponential(2.0, n)`, d'écart-type 2 aussi), et `die` $n$ lancers d'un dé à 6 faces. La vérification calcule :
- a) la liste des 3 moyennes de `sample_means(die, 4, 3, seed=5)` (2 décimales) ;
- b) la longueur de `sample_means(expo, 10, 500)` (un entier) ;
- c) la moyenne des 20 000 moyennes de `sample_means(expo, 5, 20_000)` (2 décimales) ;
- d) leur écart-type (`np.std` ; 2 décimales) ;
- e) l'écart-type des 20 000 moyennes de 20 valeurs, divisé par celui de d) (2 décimales) ;
- f) le nom de l'erreur levée par `sample_means(expo, 3, 0)` ;
- g) le nom du type du résultat, en texte (`type(...).__name__`) ;
- h) la proportion des 20 000 moyennes de 30 valeurs qui tombent dans $2 \\pm 1{,}96\\,\\frac{2}{\\sqrt{30}}$ (2 décimales).

Dans ta copie : compare c), d), e) et h) à ce que prévoient les §3 et §5 de la fiche ($\\mu$, $\\frac{\\sigma}{\\sqrt{n}}$, $\\sqrt{\\frac{5}{20}}$, 0,95).""",
    todo=LOAD_LEARNER,
    check='''expo = lambda rng, n: rng.exponential(2.0, n)      # mean 2, standard deviation 2
die = lambda rng, n: rng.integers(1, 7, n)          # n throws of a six-sided die
with checked("M02c.18a"):
    wbm.check("M02c.18a", list(mymath.estimation.sample_means(die, 4, 3, seed=5)), computed=True)
with checked("M02c.18b"):
    wbm.check("M02c.18b", len(mymath.estimation.sample_means(expo, 10, 500)), computed=True)
with checked("M02c.18c"):
    wbm.check("M02c.18c", np.mean(mymath.estimation.sample_means(expo, 5, 20_000)), computed=True)
with checked("M02c.18d"):
    wbm.check("M02c.18d", np.std(mymath.estimation.sample_means(expo, 5, 20_000)), computed=True)
with checked("M02c.18e"):
    ratio = np.std(mymath.estimation.sample_means(expo, 20, 20_000)) / np.std(
        mymath.estimation.sample_means(expo, 5, 20_000))
    wbm.check("M02c.18e", ratio, computed=True)
with checked("M02c.18f"):
    wbm.check("M02c.18f", raised(mymath.estimation.sample_means, expo, 3, 0), computed=True)
with checked("M02c.18g"):
    wbm.check("M02c.18g", type(mymath.estimation.sample_means(expo, 3, 4)).__name__, computed=True)
with checked("M02c.18h"):
    means_30 = np.asarray(mymath.estimation.sample_means(expo, 30, 20_000))
    wbm.check("M02c.18h", np.mean(np.abs(means_30 - 2) <= 1.96 * 2 / math.sqrt(30)), computed=True)''',
    solution=LOAD_REF + '''
sample_means = mymath.estimation.sample_means
expo = lambda rng, n: rng.exponential(2.0, n)      # mean 2, standard deviation 2
die = lambda rng, n: rng.integers(1, 7, n)          # n throws of a six-sided die
m5, m20, m30 = (sample_means(expo, n, 20_000) for n in (5, 20, 30))
print("a)", list(sample_means(die, 4, 3, seed=5)), " b)", len(sample_means(expo, 10, 500)),
      " c)", m5.mean(), " d)", m5.std(), "theory:", 2 / math.sqrt(5))
print("e)", m20.std() / m5.std(), "theory:", math.sqrt(5 / 20), " f)", raised(sample_means, expo, 3, 0),
      " g)", type(sample_means(expo, 3, 4)).__name__,
      " h)", np.mean(np.abs(m30 - 2) <= 1.96 * 2 / math.sqrt(30)))''',
    record=f'''wbm.record("M02c.18a", [4.0, 3.25, 3.0], decimals=2,
           mistakes={{"un seul générateur pour tous les échantillons : np.random.default_rng(seed) une fois, avant la "
                      "boucle": [4.0, 4.0, 4.0],
                     "le générateur reçoit la graine passée en argument (seed)": [4.0, 1.25, 4.25]}})
wbm.record("M02c.18b", 500)
wbm.record("M02c.18c", 1.994470280, decimals=2,
           mistakes={{"la moyenne de chaque échantillon, pas sa somme : divise par n": 9.972351398}})
wbm.record("M02c.18d", 0.899125827, decimals=2,
           mistakes={{"la moyenne de chaque échantillon, pas sa somme : divise par n": 4.495629133}})
wbm.record("M02c.18e", 0.500957231, decimals=2)
wbm.record("M02c.18f", "ValueError",
           mistakes={{"repeats = 0 : aucun échantillon, lève une ValueError": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M02c.18g", "ndarray",
           mistakes={{"la docstring demande un array NumPy : np.array(...) ou np.asarray(...)": {{"list", "tuple"}}}})
wbm.record("M02c.18h", 0.9489, decimals=2)''',
    after=tests_cells("test_sample_means_ or test_estimation_uses"),
    note="c) 1,99 pour $\\mu = 2$ ; d) 0,90 pour $\\frac{2}{\\sqrt{5}} \\approx 0{,}894$ ; e) 0,50 pour "
         "$\\sqrt{\\frac{5}{20}} = \\frac{1}{2}$ : quatre fois plus de valeurs divisent l'écart-type par 2. h) 0,949 "
         "pour 0,95 : avec 30 valeurs d'une loi pourtant très asymétrique, la loi normale prédit déjà bien la "
         "proportion. La boucle `for` sur les échantillons est permise ici : 20 000 appels prennent moins d'une "
         "seconde.",
)

M02C_19 = Ex(
    "M02c.19", "🔨", 2, 25, "Biais et erreur quadratique d'un estimateur, par simulation · "
    "`estimator_bias, estimator_mse`",
    "mesurer par simulation le biais et l'erreur quadratique d'un estimateur, et retrouver ceux des deux variances "
    "de l'échantillon.", "fiche §6", tracks="C", mymath="estimation.py",
    body="""Écris `estimator_bias(estimator, draw_sample, true_value, repeats, seed=0)` et `estimator_mse(...)` (fiche §6) : un générateur `np.random.default_rng(seed)`, `repeats` échantillons `draw_sample(rng)` tirés l'un après l'autre, l'estimation `estimator(sample)` de chacun, puis la moyenne des estimations moins `true_value` (le biais), ou la moyenne des carrés des erreurs (l'erreur quadratique). Avec la même graine, les deux fonctions voient les mêmes échantillons : une fonction auxiliaire commune, `_estimates(...)`, évite d'écrire deux fois la simulation. `repeats` $< 1$ lève une `ValueError`.

Dans la vérification, `normal_5` tire 5 valeurs de $\\mathcal{N}(0, 2^2)$ (donc $\\sigma^2 = 4$), `var_0` est la variance divisée par $n$ et `var_1` la variance divisée par $n - 1$ ; `uniform_5` tire 5 valeurs uniformes sur $[0 ; 10]$. Avec `repeats = 20_000` et la graine par défaut, la vérification calcule :
- a) le biais de `var_0` (2 décimales) ;
- b) le biais de `var_1` (2 décimales) ;
- c) l'erreur quadratique de `var_0` (1 décimale) ;
- d) l'erreur quadratique de `var_1` (1 décimale) ;
- e) l'erreur quadratique de `var_0` moins le carré de son biais (1 décimale) ;
- f) le nom de l'erreur levée par `estimator_bias(var_0, normal_5, 4.0, 0)` ;
- g) le nom du type de `estimator_mse(var_0, normal_5, 4.0, 10)`, en texte ;
- h) le biais du maximum de `uniform_5` comme estimateur de la borne 10 (2 décimales).

Dans ta copie : compare a), b), c) et d) aux valeurs de la fiche ($-\\frac{\\sigma^2}{n}$, 0, 5,76 et 8). Que mesure e) ? Lequel des deux estimateurs préfères-tu, et selon quel critère ? h) a été calculé à la main dans la fiche : retrouves-tu la même valeur ?""",
    todo=LOAD_LEARNER,
    check='''normal_5 = lambda rng: rng.normal(0, 2, 5)        # 5 values of N(0, 2²): sigma² = 4
var_0 = lambda sample: np.var(sample)               # divided by n
var_1 = lambda sample: np.var(sample, ddof=1)       # divided by n − 1
uniform_5 = lambda rng: rng.uniform(0, 10, 5)
with checked("M02c.19a"):
    wbm.check("M02c.19a", mymath.estimation.estimator_bias(var_0, normal_5, 4.0, 20_000), computed=True)
with checked("M02c.19b"):
    wbm.check("M02c.19b", mymath.estimation.estimator_bias(var_1, normal_5, 4.0, 20_000), computed=True)
with checked("M02c.19c"):
    wbm.check("M02c.19c", mymath.estimation.estimator_mse(var_0, normal_5, 4.0, 20_000), computed=True)
with checked("M02c.19d"):
    wbm.check("M02c.19d", mymath.estimation.estimator_mse(var_1, normal_5, 4.0, 20_000), computed=True)
with checked("M02c.19e"):
    spread = (mymath.estimation.estimator_mse(var_0, normal_5, 4.0, 20_000)
              - mymath.estimation.estimator_bias(var_0, normal_5, 4.0, 20_000) ** 2)
    wbm.check("M02c.19e", spread, computed=True)
with checked("M02c.19f"):
    wbm.check("M02c.19f", raised(mymath.estimation.estimator_bias, var_0, normal_5, 4.0, 0), computed=True)
with checked("M02c.19g"):
    wbm.check("M02c.19g", type(mymath.estimation.estimator_mse(var_0, normal_5, 4.0, 10)).__name__, computed=True)
with checked("M02c.19h"):
    wbm.check("M02c.19h", mymath.estimation.estimator_bias(max, uniform_5, 10.0, 20_000), computed=True)''',
    solution=LOAD_REF + '''
bias, mse = mymath.estimation.estimator_bias, mymath.estimation.estimator_mse
normal_5 = lambda rng: rng.normal(0, 2, 5)        # 5 values of N(0, 2²): sigma² = 4
var_0 = lambda sample: np.var(sample)               # divided by n
var_1 = lambda sample: np.var(sample, ddof=1)       # divided by n − 1
uniform_5 = lambda rng: rng.uniform(0, 10, 5)
b0, b1 = bias(var_0, normal_5, 4.0, 20_000), bias(var_1, normal_5, 4.0, 20_000)
e0, e1 = mse(var_0, normal_5, 4.0, 20_000), mse(var_1, normal_5, 4.0, 20_000)
print("a)", b0, " b)", b1, " c)", e0, " d)", e1, " e)", e0 - b0 ** 2, "theory: -0.8, 0, 5.76, 8, 5.12")
print("f)", raised(bias, var_0, normal_5, 4.0, 0), " g)", type(mse(var_0, normal_5, 4.0, 10)).__name__,
      " h)", bias(max, uniform_5, 10.0, 20_000), "theory:", 5 * 10 / 6 - 10)''',
    record=f'''wbm.record("M02c.19a", -0.795448004, decimals=2,
           mistakes={{"le biais est la moyenne des estimations moins la vraie valeur": 3.204551996,
                     "un seul générateur pour toute la simulation, créé avant la boucle : chaque échantillon doit être "
                     "nouveau": -3.413534227}})
wbm.record("M02c.19b", 0.005689996, decimals=2)
wbm.record("M02c.19c", 5.814982605, decimals=1,
           mistakes={{"l'erreur quadratique compare chaque estimation à la vraie valeur, pas à la moyenne des estimations":
                         5.182245078,
                     "la moyenne des carrés des erreurs, pas le carré de l'erreur moyenne": 0.632737526}})
wbm.record("M02c.19d", 8.097290311, decimals=1)
wbm.record("M02c.19e", 5.182245078, decimals=1)
wbm.record("M02c.19f", "ValueError",
           mistakes={{"repeats = 0 : aucun échantillon, lève une ValueError": {{"aucune", "ZeroDivisionError"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("M02c.19g", "float", {PY_FLOAT.format()})
wbm.record("M02c.19h", -1.676040063, decimals=2,
           mistakes={{"le biais est la moyenne des estimations moins la vraie valeur": 8.323959937}})''',
    after=tests_cells("test_estimator_bias_ or test_estimator_mse_"),
    note="a) $-0{,}80$ pour $-\\frac{\\sigma^2}{n} = -\\frac{4}{5}$ ; b) 0,01 pour 0 ; c) 5,8 pour 5,76 ; d) 8,1 pour "
         "8. e) est la **variance** de l'estimateur ($\\text{EQM} = \\text{biais}^2 + \\text{variance}$), environ "
         "5,12 en théorie : $S_n^2$ est biaisé, mais moins dispersé que $S^2$ (variance 8), si bien que son erreur "
         "quadratique est plus petite. Sur le critère de l'EQM, `var_0` gagne ; sur le biais, `var_1`. h) "
         "$-1{,}68$ pour $\\frac{5}{6} \\times 10 - 10 \\approx -1{,}67$ (fiche §6). L'écart à la théorie est l'aléa "
         "de 20 000 échantillons : la simulation estime un biais à quelques centièmes près.",
)

M02C_20 = Ex(
    "M02c.20", "🔨", 1, 20, "Erreur type et intervalle de confiance · `standard_error, confidence_interval_mean`",
    "programmer l'erreur type d'une moyenne et son intervalle de confiance, avec leurs cas d'erreur.",
    "fiche §7", tracks="C, E", mymath="estimation.py",
    body="""Écris `standard_error(sample, ddof=1)` puis `confidence_interval_mean(sample, z=1.96)` (fiche §7) : l'écart-type $s$ divise la somme des carrés des écarts par $n - \\text{ddof}$, l'erreur type vaut $\\frac{s}{\\sqrt{n}}$, et l'intervalle est le **tuple** `(moyenne - z * erreur_type, moyenne + z * erreur_type)`. `standard_error` lève une `ValueError` si l'échantillon a `ddof` valeurs ou moins ; `confidence_interval_mean`, s'il a moins de deux valeurs ou si $z \\le 0$.

La vérification utilise l'échantillon `[12, 15, 11, 18, 14]` et calcule :
- a) son erreur type (4 décimales) ;
- b) son erreur type avec `ddof=0` (4 décimales) ;
- c) son intervalle à 95 %, en liste (4 décimales) ;
- d) son intervalle à 90 % ($z = 1{,}645$), en liste (4 décimales) ;
- e) le nom de l'erreur levée par `standard_error([5.0])` ;
- f) le nom de l'erreur levée par `confidence_interval_mean([1, 2, 3], -1)` ;
- g) le nom du type de l'intervalle, en texte ;
- h) la largeur de l'intervalle à 95 % de 400 valeurs tirées de $\\mathcal{N}(50, 10^2)$ (fournies ; 2 décimales).

Dans ta copie : refais a) et c) à la main. h) est proche de $2 \\times 1{,}96 \\times \\frac{10}{\\sqrt{400}}$ : pourquoi pas exactement ?""",
    todo=LOAD_LEARNER,
    check='''sample_20 = [12, 15, 11, 18, 14]
data_20 = np.random.default_rng(20).normal(50, 10, 400)   # 400 values of N(50, 10²)
with checked("M02c.20a"):
    wbm.check("M02c.20a", mymath.estimation.standard_error(sample_20), computed=True)
with checked("M02c.20b"):
    wbm.check("M02c.20b", mymath.estimation.standard_error(sample_20, ddof=0), computed=True)
with checked("M02c.20c"):
    wbm.check("M02c.20c", list(mymath.estimation.confidence_interval_mean(sample_20)), computed=True)
with checked("M02c.20d"):
    wbm.check("M02c.20d", list(mymath.estimation.confidence_interval_mean(sample_20, 1.645)), computed=True)
with checked("M02c.20e"):
    wbm.check("M02c.20e", raised(mymath.estimation.standard_error, [5.0]), computed=True)
with checked("M02c.20f"):
    wbm.check("M02c.20f", raised(mymath.estimation.confidence_interval_mean, [1, 2, 3], -1), computed=True)
with checked("M02c.20g"):
    wbm.check("M02c.20g", type(mymath.estimation.confidence_interval_mean(sample_20)).__name__, computed=True)
with checked("M02c.20h"):
    low, high = mymath.estimation.confidence_interval_mean(data_20)
    wbm.check("M02c.20h", high - low, computed=True)''',
    solution=LOAD_REF + '''
se, ci = mymath.estimation.standard_error, mymath.estimation.confidence_interval_mean
sample_20 = [12, 15, 11, 18, 14]
data_20 = np.random.default_rng(20).normal(50, 10, 400)   # 400 values of N(50, 10²)
low, high = ci(data_20)
print("a)", se(sample_20), " b)", se(sample_20, ddof=0), " c)", ci(sample_20), " d)", ci(sample_20, 1.645))
print("e)", raised(se, [5.0]), " f)", raised(ci, [1, 2, 3], -1), " g)", type(ci(sample_20)).__name__,
      " h)", high - low, "with sigma = 10:", 2 * 1.96 * 10 / math.sqrt(400))''',
    record=f'''wbm.record("M02c.20a", 1.224744871, decimals=4,
           mistakes={{"l'erreur type divise s par √n, pas par n": 0.547722558,
                     "c'est l'écart-type des données ; l'erreur type de la moyenne le divise par √n": 2.738612788,
                     "s est l'écart-type, la racine de la variance": 3.354101966,
                     "ddof=1 par défaut : la variance divise par n − 1": 1.095445115}})
wbm.record("M02c.20b", 1.095445115, decimals=4,
           mistakes={{"ddof=0 : la variance divise par n − 0 = n": 1.224744871}})
wbm.record("M02c.20c", [11.599500052, 16.400499948], decimals=4,
           mistakes={{"l'intervalle utilise l'erreur type, pas l'écart-type des données": [8.632318936, 19.367681064],
                     "l'erreur type de l'intervalle utilise ddof=1": [11.852927575, 16.147072425]}})
wbm.record("M02c.20d", [11.985294687, 16.014705313], decimals=4)
wbm.record("M02c.20e", "ValueError",
           mistakes={{"une seule valeur avec ddof=1 : n − ddof = 0, lève une ValueError": {{"aucune", "ZeroDivisionError"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("M02c.20f", "ValueError",
           mistakes={{"z ≤ 0 n'a pas de sens : lève une ValueError": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M02c.20g", "tuple",
           mistakes={{"la docstring demande un tuple (low, high)": {{"list", "ndarray"}}}})
wbm.record("M02c.20h", 2.069461867, decimals=2)''',
    after=tests_cells("test_standard_error_ or test_confidence_interval_mean_"),
    note="a) $\\bar{x} = 14$, somme des carrés des écarts 30, $s = \\sqrt{\\frac{30}{4}} \\approx 2{,}739$, erreur type "
         "$\\frac{2{,}739}{\\sqrt{5}} \\approx 1{,}2247$ ; c) $14 \\pm 1{,}96 \\times 1{,}2247$. h) vaut 2,07 et non "
         "1,96 : l'intervalle utilise l'écart-type **estimé** $s$ des 400 valeurs (environ 10,6 ici), pas le vrai "
         "$\\sigma = 10$. Un autre échantillon donnerait un autre $s$, donc une autre largeur.",
)

M02C_21 = Ex(
    "M02c.21", "📦", 1, 15, "NumPy et SciPy : `ddof`, `np.percentile`, `scipy.stats.sem`",
    "calculer avec NumPy et SciPy les statistiques d'une série, en choisissant le bon `ddof`, la bonne échelle et "
    "la bonne méthode de quantile.", "fiche §1, §2 et §7", tracks="C",
    body="""Les fonctions de NumPy et de SciPy calculent les statistiques du chapitre en une ligne, à condition de lire leurs paramètres : `np.std(x, ddof=...)`, `np.percentile(x, q, method=...)` (q **en pourcentage**, de 0 à 100), `np.quantile(x, q)` (q **entre 0 et 1**), `stats.sem(x, ddof=...)` (l'erreur type de la moyenne), `stats.iqr(x)` (l'écart interquartile). Lis `help(np.percentile)` et `help(stats.sem)` avant de commencer.

La cellule fournie définit `DATA_21`, les durées d'exécution (en ms) d'un test unitaire lancé 15 fois. Calcule :
- a) l'écart-type qui divise par $n - 1$ (3 décimales) ;
- b) l'erreur type de la moyenne, avec `stats.sem` (3 décimales) ;
- c) le percentile 90, avec la méthode par défaut (2 décimales) ;
- d) le percentile 90, avec `method="nearest"` (2 décimales) ;
- e) l'écart interquartile, avec `stats.iqr` (2 décimales) ;
- f) le nombre de valeurs signalées par la règle de Tukey (un entier) ;
- g) le quantile d'ordre 0,9, avec `np.quantile` (2 décimales) ;
- h) `stats.sem(DATA_21, ddof=0) / stats.sem(DATA_21)` (4 décimales).

Dans ta copie : retrouve c) avec la convention de la fiche (§1), et h) par une formule en $n$. Pourquoi c) et d) diffèrent-ils ?""",
    given="DATA_21 = np.array([23, 19, 31, 25, 22, 27, 24, 88, 21, 26, 30, 20, 24, 29, 23])   # 15 durations, in ms",
    todo='''answer_M02c_21a = ...  # a) np.std(...)
answer_M02c_21b = ...  # b) stats.sem(...)
answer_M02c_21c = ...  # c) np.percentile(...)
answer_M02c_21d = ...  # d) np.percentile(..., method="nearest")
answer_M02c_21e = ...  # e) stats.iqr(...)
answer_M02c_21f = ...  # f) an integer
answer_M02c_21g = ...  # g) np.quantile(...)
answer_M02c_21h = ...  # h) stats.sem(DATA_21, ddof=0) / stats.sem(DATA_21)''',
    check='''for letter, answer in zip("abcdefgh", [answer_M02c_21a, answer_M02c_21b, answer_M02c_21c, answer_M02c_21d,
                                        answer_M02c_21e, answer_M02c_21f, answer_M02c_21g, answer_M02c_21h]):
    wbm.check(f"M02c.21{letter}", answer)''',
    solution='''answer_M02c_21a = np.std(DATA_21, ddof=1)
answer_M02c_21b = stats.sem(DATA_21)                           # ddof=1 by default: np.std(DATA_21, ddof=1) / √15
answer_M02c_21c = np.percentile(DATA_21, 90)                   # q in percent: 90, not 0.9
answer_M02c_21d = np.percentile(DATA_21, 90, method="nearest")
answer_M02c_21e = stats.iqr(DATA_21)
q1, q3 = np.percentile(DATA_21, [25, 75])
outside = (DATA_21 < q1 - 1.5 * (q3 - q1)) | (DATA_21 > q3 + 1.5 * (q3 - q1))
answer_M02c_21f = int(np.sum(outside))
answer_M02c_21g = np.quantile(DATA_21, 0.9)                    # q between 0 and 1
answer_M02c_21h = stats.sem(DATA_21, ddof=0) / stats.sem(DATA_21)
print([round(float(v), 4) for v in [answer_M02c_21a, answer_M02c_21b, answer_M02c_21c, answer_M02c_21d,
                                     answer_M02c_21e, answer_M02c_21f, answer_M02c_21g, answer_M02c_21h]])
print("sorted:", np.sort(DATA_21), "· fences:", q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1))''',
    record='''wbm.record("M02c.21a", 16.755382930, decimals=3,
           mistakes={"ddof=1 : la somme des carrés des écarts divisée par n − 1": 16.187237771})
wbm.record("M02c.21b", 4.326221270, decimals=3,
           mistakes={"c'est l'écart-type ; l'erreur type le divise par √n": 16.755382930,
                     "stats.sem divise déjà par √n : ne le refais pas": 1.117025010,
                     "stats.sem a ddof=1 par défaut ; laisse-le": 4.179526821})
wbm.record("M02c.21c", 30.6, decimals=2,
           mistakes={"np.percentile attend un pourcentage entre 0 et 100": 19.126,
                     "la méthode par défaut (linéaire), sans l'argument method": 31.0})
wbm.record("M02c.21d", 31.0, decimals=2,
           mistakes={"method=\\"nearest\\" prend la valeur la plus proche de la position, sans interpoler": 30.6})
wbm.record("M02c.21e", 5.5, decimals=2,
           mistakes={"l'écart interquartile, pas l'étendue": 69.0})
wbm.record("M02c.21f", 1,
           mistakes={"compte les valeurs qui sortent des barrières Q1 − 1,5 × EI et Q3 + 1,5 × EI": 0})
wbm.record("M02c.21g", 30.6, decimals=2,
           mistakes={"np.quantile attend un ordre entre 0 et 1 ; c'est np.percentile qui attend un pourcentage": 19.126})
wbm.record("M02c.21h", 0.966091783, decimals=4,
           mistakes={"ddof=0 divisé par ddof=1, dans cet ordre": 1.035098339})''',
    note="c) Triées, les valeurs vont de 19 à 88 ; la position du percentile 90 est $0{,}9 \\times 14 = 12{,}6$, entre "
         "$x_{(12)} = 30$ et $x_{(13)} = 31$ : $30 + 0{,}6 \\times 1 = 30{,}6$. d) `nearest` prend la valeur de la "
         "position la plus proche, 13 : 31. h) $\\sqrt{\\frac{n - 1}{n}} = \\sqrt{\\frac{14}{15}} \\approx 0{,}9661$. La "
         "valeur 88 est la seule hors des barrières $[14{,}25 ; 36{,}25]$ ; elle gonfle l'écart-type (16,8 ms) bien "
         "plus que l'écart interquartile (5,5 ms).",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, two experiments, a figure (M02c.22 to M02c.25)
# ---------------------------------------------------------------------------
M02C_22_EXPERIMENT = '''rng_22 = np.random.default_rng(22)
fig, axes = plt.subplots(1, 4, figsize=(13, 2.8))
for ax, n in zip(axes, [1, 4, 16, 64]):
    means = rng_22.exponential(1.0, (100_000, n)).mean(axis=1)    # 100 000 means of n values, mean 1, std 1
    ax.hist(means, bins=80, density=True, alpha=0.6)
    ax.axvline(1, color="black", linewidth=1)
    ax.set_title(f"n = {n}")
    print(f"n = {n:2d} : moyenne {means.mean():.3f} · écart-type {means.std():.3f} · médiane {np.median(means):.3f}")
plt.show()'''

M02C_22 = Ex(
    "M02c.22", "🔮", 1, 10, "Prédire : l'histogramme des moyennes d'une loi exponentielle quand n grandit",
    "prévoir comment le centre, la largeur et la forme de la distribution des moyennes changent avec $n$, puis le "
    "vérifier par simulation.", "fiche §4 et §5", tracks="C, E", hypothesis=True,
    body="""On tire beaucoup d'échantillons de $n$ valeurs d'une loi exponentielle d'espérance 1 (et d'écart-type 1), et on trace l'histogramme de leurs moyennes, pour $n = 1, 4, 16, 64$. Choisis, pour chaque question :
- a) quand $n$ passe de 4 à 16, l'écart-type des moyennes est : (1) le même ; (2) divisé par 2 ; (3) divisé par 4 ; (4) divisé par 16 ;
- b) quand $n$ grandit, le centre de l'histogramme (la moyenne des moyennes) : (1) reste en 1 ; (2) se rapproche de 0 ; (3) se rapproche de la médiane de la loi, $\\ln 2 \\approx 0{,}69$ ; (4) grandit ;
- c) pour $n = 1$, l'histogramme : (1) a la forme d'une cloche symétrique ; (2) part d'un maximum en 0 et décroît, avec une longue queue à droite ; (3) est plat ; (4) a une longue queue à gauche ;
- d) pour $n = 1$, la médiane des tirages, comparée à leur moyenne, est : (1) égale ; (2) plus petite ; (3) plus grande ; (4) impossible à prévoir.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**, de 1 à 4), vérifie-les, puis lance l'expérience : 100 000 échantillons pour chaque $n$.""",
    todo='''prediction_M02c_22a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M02c_22b = ...  # b) 1, 2, 3 or 4
prediction_M02c_22c = ...  # c) 1, 2, 3 or 4
prediction_M02c_22d = ...  # d) 1, 2, 3 or 4''',
    check='''for letter, prediction in zip("abcd", [prediction_M02c_22a, prediction_M02c_22b, prediction_M02c_22c,
                                      prediction_M02c_22d]):
    wbm.check(f"M02c.22{letter}", prediction)''',
    record='''wbm.record("M02c.22a", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M02c.22b", 1, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M02c.22c", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M02c.22d", 2, prediction=True, choices=[1, 2, 3, 4])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(M02C_22_EXPERIMENT, ["prediction_M02c_22a", "prediction_M02c_22b", "prediction_M02c_22c",
                                               "prediction_M02c_22d"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", M02C_22_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : explique chaque résultat avec la fiche ($\\mathbb{E}[\\bar{X}_n]$, "
               "$\\sigma(\\bar{X}_n)$, le théorème central limite). Pour $n = 64$, la cloche est-elle parfaitement "
               "symétrique ? Que deviennent la médiane et la moyenne des moyennes quand $n$ grandit ?"),
    ],
    note="a) L'écart-type des moyennes vaut $\\frac{\\sigma}{\\sqrt{n}}$ : 4 fois plus de valeurs le divisent par 2 "
         "(0,5 puis 0,25). b) $\\mathbb{E}[\\bar{X}_n] = \\mu = 1$ pour tout $n$ : le centre ne bouge pas, seule la "
         "largeur diminue. c) Pour $n = 1$, l'histogramme est celui de la loi elle-même, la densité $e^{-x}$ : un "
         "maximum en 0 et une longue queue à droite ; le théorème central limite ne dit rien pour $n = 1$. d) La "
         "médiane de la loi exponentielle vaut $\\ln 2 \\approx 0{,}69 < 1$ (M02a) : la longue queue tire la moyenne "
         "vers la droite. Quand $n$ grandit, la médiane des moyennes se rapproche de 1 (0,92 pour $n = 4$, 0,996 pour "
         "$n = 64$) : la distribution devient symétrique, mais garde une légère asymétrie pour $n = 64$.",
)

M02C_23_GIVEN = '''rng_23 = np.random.default_rng(23)
NORMAL_20 = rng_23.normal(10, 3, (10_000, 20))         # 10 000 samples of 20 values of N(10, 3²): true mean 10
EXPO_10 = rng_23.exponential(2.0, (10_000, 10))        # 10 000 samples of 10 values, exponential law: true mean 2
EXPO_100 = rng_23.exponential(2.0, (10_000, 100))      # 10 000 samples of 100 values of the same law'''

M02C_23 = Ex(
    "M02c.23", "🔬", 2, 20, "Couverture : 95 % des intervalles contiennent-ils la vraie moyenne ?",
    "mesurer par simulation la couverture de l'intervalle $\\bar{x} \\pm z\\,\\frac{s}{\\sqrt{n}}$, et voir quand "
    "elle s'éloigne de 95 %.", "fiche §5 et §7", tracks="C, E",
    body="""La **couverture** d'une méthode d'intervalle de confiance est la proportion des échantillons pour lesquels l'intervalle contient la vraie valeur (fiche §7). La cellule fournie tire, une fois pour toutes, trois paquets de 10 000 échantillons (une ligne par échantillon) : `NORMAL_20` (20 valeurs de $\\mathcal{N}(10, 3^2)$), `EXPO_10` et `EXPO_100` (10 et 100 valeurs d'une loi exponentielle d'espérance 2).

Écris `coverage(samples, true_mean, z=1.96)`, qui calcule pour **chaque ligne** l'intervalle $\\bar{x} \\pm z\\,\\frac{s}{\\sqrt{n}}$ (avec $s$ divisé par $n - 1$) et renvoie la proportion des lignes dont l'intervalle contient `true_mean`. Vectorise : `samples.mean(axis=1)` et `samples.std(axis=1, ddof=1)` traitent toutes les lignes d'un coup.

Puis calcule (3 décimales) :
- a) la couverture à 95 % pour `NORMAL_20` ;
- b) pour `EXPO_10` ;
- c) pour `EXPO_100` ;
- d) la couverture pour `NORMAL_20` avec $z = 1{,}645$ ;
- e) la couverture pour `NORMAL_20` avec le quantile de Student à 19 degrés de liberté, `stats.t.ppf(0.975, 19)`, à la place de 1,96.

Dans ta copie : l'aléa d'une proportion estimée sur 10 000 échantillons est d'environ $\\sqrt{\\frac{0{,}95 \\times 0{,}05}{10\\,000}} \\approx 0{,}002$. Lesquelles de ces couvertures sont nettement sous 0,95 ? Pourquoi b) est-elle la plus basse, et pourquoi c) remonte-t-elle ? Que corrige e) ?""",
    given=M02C_23_GIVEN,
    todo='''def coverage(samples, true_mean, z=1.96):
    """The share of the rows of samples whose interval mean ± z s/√n (s with ddof=1) contains true_mean."""
    raise NotImplementedError("samples.mean(axis=1), samples.std(axis=1, ddof=1), puis la proportion des lignes")


coverage_a = ...   # a) NORMAL_20
coverage_b = ...   # b) EXPO_10
coverage_c = ...   # c) EXPO_100
coverage_d = ...   # d) NORMAL_20 with z = 1.645
coverage_e = ...   # e) NORMAL_20 with z = stats.t.ppf(0.975, 19)''',
    check='''for letter, value in zip("abcde", [coverage_a, coverage_b, coverage_c, coverage_d, coverage_e]):
    wbm.check(f"M02c.23{letter}", value)''',
    solution='''def coverage(samples, true_mean, z=1.96):
    """The share of the rows of samples whose interval mean ± z s/√n (s with ddof=1) contains true_mean."""
    samples = np.asarray(samples, dtype=float)
    means = samples.mean(axis=1)
    half = z * samples.std(axis=1, ddof=1) / math.sqrt(samples.shape[1])
    return float(np.mean((means - half <= true_mean) & (true_mean <= means + half)))


coverage_a = coverage(NORMAL_20, 10)
coverage_b = coverage(EXPO_10, 2)
coverage_c = coverage(EXPO_100, 2)
coverage_d = coverage(NORMAL_20, 10, z=1.645)
coverage_e = coverage(NORMAL_20, 10, z=stats.t.ppf(0.975, 19))
print(coverage_a, coverage_b, coverage_c, coverage_d, coverage_e, "· Student quantile:", stats.t.ppf(0.975, 19))''',
    record='''wbm.record("M02c.23a", 0.9329, decimals=3,
           mistakes={"l'écart-type s divise par n − 1 (ddof=1)": 0.9246,
                     "l'intervalle utilise l'erreur type s/√n, pas l'écart-type s des données": 1.0})
wbm.record("M02c.23b", 0.87, decimals=3,
           mistakes={"l'écart-type s divise par n − 1 (ddof=1)": 0.856})
wbm.record("M02c.23c", 0.9406, decimals=3)
wbm.record("M02c.23d", 0.8772, decimals=3,
           mistakes={"l'écart-type s divise par n − 1 (ddof=1)": 0.868})
wbm.record("M02c.23e", 0.947, decimals=3,
           mistakes={"l'écart-type s divise par n − 1 (ddof=1)": 0.9417})''',
    note="a) 0,933 : même pour des données normales, 1,96 est un peu trop petit avec 20 valeurs, parce que $s$ varie "
         "d'un échantillon à l'autre. b) 0,870 : avec 10 valeurs d'une loi très asymétrique, la moyenne n'est pas "
         "encore normale, et $s$ est souvent trop petit quand $\\bar{x}$ l'est (les deux dépendent des rares grandes "
         "valeurs). c) 0,941 : avec 100 valeurs, le théorème central limite fait son effet. d) 0,877, proche des 90 % "
         "annoncés (même léger déficit qu'en a). e) 0,947 : le quantile de Student (2,093) corrige l'incertitude de "
         "$s$ pour des données normales ; il ne corrigerait pas l'asymétrie de b). Le défi M02c.28 cherche un intervalle "
         "exact pour ce cas.",
)

M02C_24_GIVEN = '''rng_24 = np.random.default_rng(24)
CUBES_24 = {d: rng_24.uniform(-1, 1, (100_000, d)) for d in (2, 3, 10, 20)}   # 100 000 points in [−1, 1]^d'''

M02C_24 = Ex(
    "M02c.24", "🔬", 2, 20, "Grande dimension : le cube dont le centre est vide",
    "mesurer par Monte-Carlo la part du cube occupée par la boule inscrite et par une fine couche près du bord, et "
    "voir où la simulation cesse d'être utile.", "fiche §4 et §9", tracks="C",
    body="""La cellule fournie tire 100 000 points uniformes dans le cube $[-1 ; 1]^d$ pour $d = 2, 3, 10, 20$ (le dictionnaire `CUBES_24`, une ligne par point). Écris :
- `ball_fraction(points)` : la proportion des points dans la boule de rayon 1 centrée en 0 ($x_1^2 + \\cdots + x_d^2 \\le 1$) ;
- `border_fraction(points, eps=0.05)` : la proportion des points à moins de `eps` du bord du cube, c'est-à-dire dont **au moins une** coordonnée dépasse $1 - \\varepsilon$ en valeur absolue ;
- `exact_ball_fraction(d)` : la valeur exacte, $\\frac{\\pi^{d/2}}{\\Gamma(d/2 + 1)\\,2^d}$ (la formule admise par la fiche ; `math.gamma` calcule $\\Gamma$).

Puis calcule :
- a) `ball_fraction` pour $d = 2$ (3 décimales) ;
- b) pour $d = 3$ (3 décimales) ;
- c) pour $d = 10$ (4 décimales) ;
- d) `border_fraction` pour $d = 20$ (3 décimales) ;
- e) `exact_ball_fraction(10)` (5 décimales) ;
- f) le **nombre** de points de `CUBES_24[20]` dans la boule (un entier).

Dans ta copie : compare a), b), d) aux valeurs exactes de la fiche ($\\frac{\\pi}{4}$, $\\frac{\\pi}{6}$, $1 - 0{,}95^{20}$). L'écart entre c) et e) est-il normal, compte tenu de l'erreur type d'une proportion ? Combien de points faudrait-il, en moyenne, pour en voir **un seul** dans la boule en dimension 20 (`exact_ball_fraction(20)`) ? Que dit f) des limites de Monte-Carlo pour un événement très rare ?""",
    given=M02C_24_GIVEN,
    todo='''def ball_fraction(points):
    """The share of the points (one per row) inside the ball of radius 1 centred at 0."""
    raise NotImplementedError("la somme des carrés des coordonnées de chaque ligne, comparée à 1")


def border_fraction(points, eps=0.05):
    """The share of the points with at least one coordinate beyond 1 − eps in absolute value."""
    raise NotImplementedError("le maximum des |coordonnées| de chaque ligne, comparé à 1 − eps")


def exact_ball_fraction(d):
    """The volume of the unit ball of dimension d divided by the volume 2^d of the cube [−1, 1]^d."""
    raise NotImplementedError("math.pi ** (d / 2) / math.gamma(d / 2 + 1) / 2 ** d")


answer_M02c_24a = ...  # a) d = 2
answer_M02c_24b = ...  # b) d = 3
answer_M02c_24c = ...  # c) d = 10
answer_M02c_24d = ...  # d) border_fraction for d = 20
answer_M02c_24e = ...  # e) exact_ball_fraction(10)
answer_M02c_24f = ...  # f) the number of points of CUBES_24[20] inside the ball''',
    check='''for letter, answer in zip("abcdef", [answer_M02c_24a, answer_M02c_24b, answer_M02c_24c, answer_M02c_24d,
                                      answer_M02c_24e, answer_M02c_24f]):
    wbm.check(f"M02c.24{letter}", answer)''',
    solution='''def ball_fraction(points):
    """The share of the points (one per row) inside the ball of radius 1 centred at 0."""
    return float(np.mean(np.sum(np.asarray(points) ** 2, axis=1) <= 1))


def border_fraction(points, eps=0.05):
    """The share of the points with at least one coordinate beyond 1 − eps in absolute value."""
    return float(np.mean(np.max(np.abs(np.asarray(points)), axis=1) > 1 - eps))


def exact_ball_fraction(d):
    """The volume of the unit ball of dimension d divided by the volume 2^d of the cube [−1, 1]^d."""
    return math.pi ** (d / 2) / math.gamma(d / 2 + 1) / 2 ** d


answer_M02c_24a = ball_fraction(CUBES_24[2])
answer_M02c_24b = ball_fraction(CUBES_24[3])
answer_M02c_24c = ball_fraction(CUBES_24[10])
answer_M02c_24d = border_fraction(CUBES_24[20])
answer_M02c_24e = exact_ball_fraction(10)
answer_M02c_24f = int(np.sum(np.sum(CUBES_24[20] ** 2, axis=1) <= 1))
print(answer_M02c_24a, math.pi / 4, "·", answer_M02c_24b, math.pi / 6, "·", answer_M02c_24c, answer_M02c_24e)
print(answer_M02c_24d, 1 - 0.95 ** 20, "·", answer_M02c_24f, "· d = 20:", exact_ball_fraction(20),
      "· points for one inside:", 1 / exact_ball_fraction(20))''',
    record='''wbm.record("M02c.24a", 0.78493, decimals=3,
           mistakes={"la boule de rayon 1 : la somme des carrés des coordonnées est au plus 1, pas 1/4": 0.19629})
wbm.record("M02c.24b", 0.52423, decimals=3)
wbm.record("M02c.24c", 0.0023, decimals=4)
wbm.record("M02c.24d", 0.63911, decimals=3,
           mistakes={"près du bord dès qu'**au moins une** coordonnée dépasse 1 − eps : le maximum des valeurs absolues, "
                     "pas le minimum": 0.0})
wbm.record("M02c.24e", 0.002490395, decimals=5,
           mistakes={"divise le volume de la boule par celui du cube, 2^d": 2.550164040})
wbm.record("M02c.24f", 0)''',
    note="a) 0,785 et b) 0,524, pour $\\frac{\\pi}{4} \\approx 0{,}7854$ et $\\frac{\\pi}{6} \\approx 0{,}5236$. c) 0,0023 "
         "pour 0,00249 : 230 points sur 100 000 au lieu de 249 attendus ; l'erreur type d'une proportion $p$ sur $N$ "
         "points vaut $\\sqrt{\\frac{p(1 - p)}{N}} \\approx 0{,}00016$, et l'écart (0,00019) en fait à peine plus d'une. "
         "d) 0,639 pour $1 - 0{,}95^{20} \\approx 0{,}6415$. f) Aucun point en dimension 20 : la boule occupe "
         "$2{,}5 \\times 10^{-8}$ du cube, il faudrait en moyenne 40 millions de points pour en voir un. Monte-Carlo "
         "estime bien une proportion de l'ordre de 0,1 à 0,9 ; pour un événement très rare, son erreur **relative** "
         "$\\frac{1}{\\sqrt{Np}}$ explose, et il faut d'autres méthodes (l'échantillonnage préférentiel, chapitre 28 "
         "de workbookIA).",
)

M02C_25_GIVEN = '''EXPO_DRAW = lambda rng, n: rng.exponential(1.0, n)     # the exponential law of mean 1 and standard deviation 1
NS_25 = [1, 2, 10, 50]'''

M02C_25_CHECK = '''with checked("M02c.25 vérifications"):
    problems = []
    uniform_draw = lambda rng, n: rng.random(n)            # another law: uniform on [0, 1], mean 0.5, std √(1/12)
    mu_t, sigma_t = 0.5, math.sqrt(1 / 12)
    fig, axes = plt.subplots(1, 2, figsize=(8, 3))
    try:
        created = drawn(draw_clt, axes, uniform_draw, mu_t, sigma_t, [1, 9], 4_000)
    finally:
        plt.close(fig)                                     # only the checks below are shown here
    if created:
        problems.append("draw_clt ouvre sa propre figure : dessine dans les axes reçus")
    else:
        for ax, n in zip(axes, [1, 9]):
            bars = [p for p in ax.patches if p.get_height() > 0]
            area = sum(p.get_width() * p.get_height() for p in bars)
            if not bars or abs(area - 1) > 0.02:
                problems.append(f"n = {n} : l'histogramme doit avoir une aire de 1 (density=True)")
                continue
            centre = sum((p.get_x() + p.get_width() / 2) * p.get_width() * p.get_height() for p in bars) / area
            if abs(centre - mu_t) > 0.05:
                problems.append(f"n = {n} : l'histogramme doit être celui des moyennes de n tirages, centré sur mu")
            spread = math.sqrt(sum((p.get_x() + p.get_width() / 2 - centre) ** 2 * p.get_width() * p.get_height()
                                   for p in bars) / area)
            if abs(spread / (sigma_t / math.sqrt(n)) - 1) > 0.15:
                problems.append(f"n = {n} : la largeur de l'histogramme doit être celle des moyennes de n tirages, "
                                "sigma / √n")
            lines = [line for line in ax.get_lines() if len(line.get_xdata()) > 20]
            if not lines:
                problems.append(f"n = {n} : il manque la courbe de la densité normale (ax.plot sur une grille)")
                continue
            xs, ys = (np.asarray(lines[0].get_xdata(), dtype=float), np.asarray(lines[0].get_ydata(), dtype=float))
            peak_x, peak_y = xs[np.argmax(ys)], ys.max()
            expected = 1 / (sigma_t / math.sqrt(n) * math.sqrt(2 * math.pi))
            if abs(peak_x - mu_t) > 0.02 * (1 + sigma_t):
                problems.append(f"n = {n} : le sommet de la densité normale doit être en mu (il est en {peak_x:.3f})")
            if abs(peak_y / expected - 1) > 0.02:
                problems.append(f"n = {n} : la densité normale doit avoir l'écart-type sigma / √n (sa hauteur au "
                                "sommet n'est pas la bonne)")
            if str(n) not in ax.get_title():
                problems.append(f"n = {n} : le titre de chaque axe doit indiquer n")
    if problems:
        print("❌ Ex M02c.25 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M02c.25 : des histogrammes de moyennes, d'aire 1, bien centrés, avec la bonne densité normale.")'''

M02C_25 = Ex(
    "M02c.25", "🎨", 1, 20, "Voir le théorème central limite : histogrammes et densité normale",
    "tracer les histogrammes des moyennes d'échantillons pour plusieurs tailles, avec la densité normale que prévoit "
    "le théorème central limite.", "fiche §5 ; R0 (matplotlib)", tracks="C",
    body="""Écris `draw_clt(axes, draw, mu, sigma, ns, repeats=20_000, seed=0)`, qui dessine, pour chaque taille $n$ de la liste `ns` et dans l'axe correspondant de `axes` :
- l'**histogramme** des `repeats` moyennes de $n$ tirages (ta fonction `mymath.estimation.sample_means(draw, n, repeats, seed)`, ou ton propre code), avec `density=True` pour qu'il ait une aire de 1, comme une densité ;
- la **densité normale** prévue par le théorème central limite, $\\mathcal{N}\\big(\\mu, \\frac{\\sigma^2}{n}\\big)$, tracée sur une grille de valeurs (`stats.norm(mu, sigma / math.sqrt(n)).pdf(grid)`, avec `grid` couvrant au moins $\\mu \\pm 4\\frac{\\sigma}{\\sqrt{n}}$) ;
- un titre qui indique $n$.

Puis trace-la pour la loi exponentielle d'espérance 1 (`EXPO_DRAW`, $\\mu = \\sigma = 1$) et `NS_25` $= [1, 2, 10, 50]$.

Dans ta copie : pour quel $n$ la densité normale te semble-t-elle décrire correctement l'histogramme ? Où l'écart se voit-il le plus pour $n = 10$ : au centre ou dans les queues ? Pourquoi la courbe de $n = 1$ est-elle si loin de l'histogramme ?""",
    given=M02C_25_GIVEN,
    todo='''def draw_clt(axes, draw, mu, sigma, ns, repeats=20_000, seed=0):
    """For each n of ns, in the matching axis: the histogram (density=True) of repeats means of n draws, the normal
    density N(mu, sigma²/n), and a title with n."""
    raise NotImplementedError("sample_means, ax.hist(..., density=True), ax.plot(grid, stats.norm(...).pdf(grid))")''',
    check='''with checked("M02c.25 figure"):
    fig, axes = plt.subplots(1, 4, figsize=(13, 3))
    try:
        created = drawn(draw_clt, axes, EXPO_DRAW, 1.0, 1.0, NS_25)
    except BaseException:
        plt.close(fig)                                     # no empty figure while the function is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M02c.25 : draw_clt ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans les axes "
              "reçus.")
    else:
        fig.suptitle("Moyennes de n tirages d'une loi exponentielle, et la densité normale prévue", y=1.05)
        plt.show()''',
    solution='''def draw_clt(axes, draw, mu, sigma, ns, repeats=20_000, seed=0):
    """For each n of ns, in the matching axis: the histogram (density=True) of repeats means of n draws, the normal
    density N(mu, sigma²/n), and a title with n."""
    for ax, n in zip(axes, ns):
        means = mymath.estimation.sample_means(draw, n, repeats, seed)
        ax.hist(means, bins=60, density=True, alpha=0.6)
        width = sigma / math.sqrt(n)
        grid = np.linspace(mu - 4 * width, mu + 4 * width, 300)
        ax.plot(grid, stats.norm(mu, width).pdf(grid), color="black", linewidth=1.5)
        ax.set_title(f"n = {n}")


fig, axes = plt.subplots(1, 4, figsize=(13, 3))
draw_clt(axes, EXPO_DRAW, 1.0, 1.0, NS_25)
fig.suptitle("Moyennes de n tirages d'une loi exponentielle, et la densité normale prévue", y=1.05)
plt.show()''',
    after=[("md", "**Vérifications automatiques** (sur une autre loi, uniforme ; la figure elle-même se juge à l'œil)."),
           ("code", M02C_25_CHECK)],
    note="Pour $n = 1$, l'histogramme est la densité $e^{-x}$ elle-même, et la cloche $\\mathcal{N}(1, 1)$ n'a rien à "
         "voir avec elle (elle donne même du poids aux valeurs négatives, impossibles). Pour $n = 2$ et $n = 10$, "
         "l'histogramme reste penché : son sommet est à gauche de 1, sa queue droite plus longue que la gauche. Pour "
         "$n = 50$, la cloche le décrit bien au centre ; l'écart restant est dans les queues (la queue droite reste un "
         "peu plus épaisse). Le théorème central limite est une approximation **au centre** d'abord.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M02c.26 to M02c.28)
# ---------------------------------------------------------------------------
M02C_26_MISTAKES = bug_letters_mistakes(
    "ABDE", "CF",
    {"A": "vérifie la puissance de n dans chaque erreur type",
     "B": "vérifie que chaque formule multiplie bien un écart-type, et pas une autre grandeur",
     "D": "vérifie que chaque quantile correspond au niveau annoncé",
     "E": "vérifie que chaque intervalle porte bien sur la moyenne, pas sur les valeurs elles-mêmes"})

M02C_26 = Ex(
    "M02c.26", "🐛", 1, 15, "Chasse à l'erreur : un intervalle de confiance mal calculé",
    "repérer les erreurs classiques d'une erreur type ou d'un intervalle de confiance dans du code, puis calculer "
    "les bonnes valeurs.", "fiche §7", tracks="C",
    body="""Une collègue a mesuré $n = 25$ fois la durée d'un traitement : moyenne `mean = 50`, écart-type `s = 10` (divisé par $n - 1$). Elle a aussi évalué un modèle : accuracy `acc = 0.8` sur `n_test = 400` exemples. Voici ses six lignes de code, chacune avec un commentaire qui dit ce qu'elle veut calculer. Quatre lignes sont fausses. **Sans exécuter de code**, trouve-les.

```python
half_A = 1.96 * s / n                                # (A) half-width of the 95 % interval of the mean
half_B = 1.96 * s ** 2 / math.sqrt(n)                # (B) half-width of the 95 % interval of the mean
half_C = 1.645 * s / math.sqrt(n)                    # (C) half-width of the 90 % interval of the mean
half_D = 1.96 * s / math.sqrt(n)                     # (D) half-width of the 99 % interval of the mean
low_E, high_E = mean - 1.96 * s, mean + 1.96 * s     # (E) the 95 % confidence interval of the mean
se_F = math.sqrt(acc * (1 - acc) / n_test)           # (F) standard error of the accuracy
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire : la demi-largeur demandée pour (A) à (E), l'erreur type pour (F) (une liste de 6 nombres, 3 décimales).

Dans ta copie : pour chaque ligne fausse, quelle confusion a été faite ? L'intervalle de (E) a-t-il quand même un sens ?""",
    todo='''answer_M02c_26a = ...  # a) letters, as text
answer_M02c_26b = ...  # b) a list of 6 values (3 decimals)''',
    check='''wbm.check("M02c.26a", answer_M02c_26a)
wbm.check("M02c.26b", answer_M02c_26b)''',
    solution='''answer_M02c_26a = "ABDE"
half_95 = stats.norm.ppf(0.975) * 10 / math.sqrt(25)
answer_M02c_26b = [half_95, half_95, stats.norm.ppf(0.95) * 10 / math.sqrt(25), stats.norm.ppf(0.995) * 10 / math.sqrt(25),
                   half_95, math.sqrt(0.8 * 0.2 / 400)]
print(answer_M02c_26a, [round(float(v), 3) for v in answer_M02c_26b])''',
    record=f'''wbm.record("M02c.26a", "ABDE",
           mistakes={M02C_26_MISTAKES})
wbm.record("M02c.26b", [3.919927969, 3.919927969, 3.289707254, 5.151658654, 3.919927969, 0.02], decimals=3,
           mistakes={{"ce sont les valeurs des lignes ; donne les bonnes valeurs de ce que disent les commentaires":
                         [0.784, 39.2, 3.29, 3.92, 19.6, 0.02],
                     "(D) : à 99 %, le quantile n'est pas 1,96": [3.919927969, 3.919927969, 3.289707254, 3.919927969,
                                                                  3.919927969, 0.02]}})''',
    note="(A) divise par $n$ au lieu de $\\sqrt{n}$ (0,784 au lieu de 3,92). (B) multiplie la **variance** $s^2$ au lieu "
         "de l'écart-type (39,2). (D) garde 1,96 pour un niveau de 99 % : il faut 2,576, d'où 5,152. (E) oublie le "
         "$\\sqrt{n}$ : $[30{,}4 ; 69{,}6]$ contient environ 95 % des **durées** (si elles sont à peu près normales), "
         "pas la moyenne avec 95 % de confiance ; c'est un autre objet, un intervalle de **prédiction** d'une "
         "valeur. (C) et (F) sont justes : 1,645 est le quantile de 90 %, et $\\sqrt{\\frac{0{,}8 \\times 0{,}2}{400}} = "
         "0{,}02$.",
)

M02C_27_GIVEN = '''def estimate_pi(n, rng):
    """Monte Carlo estimate of π: 4 × the share of n uniform points of [0, 1]² inside the quarter disc."""
    points = rng.random((n, 2))
    return 4 * float(np.mean(np.sum(points ** 2, axis=1) <= 1))


def estimate_pi_shrunk(n, rng):
    """A buggy copy: the quarter disc has a radius of 0.99 instead of 1 (an error of about 2 %)."""
    points = rng.random((n, 2))
    return 4 * float(np.mean(np.sum(points ** 2, axis=1) <= 0.99 ** 2))


def estimate_pi_slightly_off(n, rng):
    """A buggy copy whose error (+0.002) is smaller than one standard error for n = 100 000."""
    return estimate_pi(n, rng) + 0.002'''

M02C_27_CHECK = '''with checked("M02c.27 vérifications"):
    problems = []
    se = pi_standard_error(100_000)
    if not isinstance(se, (int, float)) or abs(se - 4 * math.sqrt(math.pi / 4 * (1 - math.pi / 4) / 100_000)) > 1e-6:
        problems.append("pi_standard_error(n) : 4 × √(p (1 − p) / n), avec p = π/4 la probabilité d'un point dans le "
                        "quart de disque")
    passed = [bool(pi_test(estimate_pi, seed)) for seed in range(100)]
    caught = [not pi_test(estimate_pi_shrunk, seed) for seed in range(100)]
    print(f"la bonne fonction passe ton test pour {sum(passed)} graines sur 100 ; la fonction fausse est attrapée "
          f"{sum(caught)} fois sur 100")
    if sum(passed) < 100:
        problems.append("ton test échoue sur la bonne fonction pour certaines graines : la tolérance est trop étroite "
                        "(un test qui échoue sans bug est un test « instable », flaky)")
    if sum(caught) < 100:
        problems.append("ton test laisse passer la fonction au rayon de 0,99 : la tolérance est trop large")
    if problems:
        print("❌ Ex M02c.27 : à revoir : " + " ; ".join(problems) + ".")
    else:
        slight = sum(not pi_test(estimate_pi_slightly_off, seed) for seed in range(100))
        print(f"✅ Ex M02c.27 : une tolérance juste. (La fonction décalée de +0,002 n'est attrapée que {slight} fois sur "
              "100 : un écart plus petit qu'une erreur type est invisible pour un seul tirage.)")'''

M02C_27 = Ex(
    "M02c.27", "🛠️", 1, 15, "Tester une fonction aléatoire : une tolérance en erreurs types",
    "écrire le test d'une fonction aléatoire avec une tolérance fixée en erreurs types, ni trop étroite (test "
    "instable) ni trop large (bugs invisibles).", "fiche §4 et §7 ; Ex M02c.18", tracks="C",
    body="""Comment tester une fonction dont le résultat est aléatoire ? Comparer à la valeur exacte avec `==` échoue toujours ; avec une tolérance prise au hasard (`abs(x - pi) < 0.1`), le test laisse passer des bugs, ou échoue sans bug (on dit qu'il est **instable**, *flaky*). La bonne tolérance se compte en **erreurs types** : une estimation juste tombe à moins de $4$ erreurs types de la vraie valeur, sauf avec une probabilité de l'ordre de $10^{-4}$ (fiche §5).

La cellule fournie définit `estimate_pi(n, rng)`, qui estime $\\pi$ par Monte-Carlo (4 fois la proportion de $n$ points uniformes du carré $[0 ; 1]^2$ tombés dans le quart de disque de rayon 1), et deux copies fausses. Écris :
- `pi_standard_error(n)` : l'erreur type de `estimate_pi` pour $n$ points, $4\\sqrt{\\frac{p(1 - p)}{n}}$ avec $p = \\frac{\\pi}{4}$ (pourquoi 4 ?) ;
- `pi_test(estimate, seed, n=100_000, k=4)` : renvoie `True` si `estimate(n, np.random.default_rng(seed))` est à moins de `k` erreurs types de $\\pi$, `False` sinon.

La vérification lance ton test sur la bonne fonction et sur la copie fausse au rayon de 0,99, pour 100 graines : il doit accepter la bonne fonction **toutes** les fois, et refuser la fausse **toutes** les fois.

Dans ta copie : que se passerait-il avec `k=1` ? Avec `k=50` ? Pourquoi la fonction décalée de $+0{,}002$ passe-t-elle presque toujours, et combien de points faudrait-il pour l'attraper ?""",
    given=M02C_27_GIVEN,
    todo='''def pi_standard_error(n):
    """The standard error of estimate_pi for n points."""
    raise NotImplementedError("4 × √(p (1 − p) / n) avec p = π/4")


def pi_test(estimate, seed, n=100_000, k=4):
    """True if estimate(n, rng) is within k standard errors of π, with rng = np.random.default_rng(seed)."""
    raise NotImplementedError("abs(estimate(...) - math.pi) <= k * pi_standard_error(n)")''',
    solution='''def pi_standard_error(n):
    """The standard error of estimate_pi for n points."""
    p = math.pi / 4                          # the probability that one point falls inside the quarter disc
    return 4 * math.sqrt(p * (1 - p) / n)    # estimate_pi multiplies a proportion by 4


def pi_test(estimate, seed, n=100_000, k=4):
    """True if estimate(n, rng) is within k standard errors of π, with rng = np.random.default_rng(seed)."""
    return abs(estimate(n, np.random.default_rng(seed)) - math.pi) <= k * pi_standard_error(n)


print("standard error for 100 000 points:", pi_standard_error(100_000),
      "· bias of the shrunk copy:", math.pi * (0.99 ** 2 - 1))''',
    after=[("code", M02C_27_CHECK)],
    note="L'erreur type vaut $4\\sqrt{\\frac{0{,}785 \\times 0{,}215}{100\\,000}} \\approx 0{,}0052$ (le 4 vient de ce "
         "que l'estimation est 4 fois une proportion, et $\\sigma(4Y) = 4\\sigma(Y)$). La copie au rayon de 0,99 a un "
         "biais de $\\pi(0{,}99^2 - 1) \\approx -0{,}063$, soit 12 erreurs types : toujours attrapée. Avec `k=1`, la "
         "bonne fonction échouerait environ une fois sur trois ($2(1 - \\Phi(1)) \\approx 0{,}32$) ; avec `k=50`, "
         "même la copie fausse passerait. Le décalage de 0,002 vaut 0,4 erreur type : pour l'attraper à "
         "4 erreurs types, il faudrait au moins $4\\,\\text{SE} < 0{,}002$, soit $n$ de l'ordre de 11 millions "
         "de points ($\\text{SE}$ en $\\frac{1}{\\sqrt{n}}$), et davantage pour l'attraper à coup sûr. Les tests de `mymath` qui portent sur des simulations, comme celui du "
         "biais de $S_n^2$, sont construits ainsi.",
)

M02C_28_GIVEN = '''rng_28 = np.random.default_rng(28)
SCALES_28 = np.repeat([0.5, 3.0, 40.0], 1500)                              # the true means μ, unknown to you
SAMPLES_28 = rng_28.exponential(1.0, (4500, 10)) * SCALES_28[:, None]      # 4 500 samples of 10 values'''

M02C_28_CHECK = '''with checked("M02c.28"):
    import time

    start = time.perf_counter()
    intervals = np.array([interval_10(sample.copy()) for sample in SAMPLES_28], dtype=float)
    seconds = time.perf_counter() - start
    reasons = []
    if intervals.shape != (4500, 2):
        reasons.append("interval_10 doit renvoyer deux nombres (low, high)")
    else:
        inside = (intervals[:, 0] <= SCALES_28) & (SCALES_28 <= intervals[:, 1])
        overall = float(np.mean(inside))
        per_scale = [float(np.mean(inside[SCALES_28 == mu])) for mu in (0.5, 3.0, 40.0)]
        width = float(np.mean((intervals[:, 1] - intervals[:, 0]) / SCALES_28))
        print(f"couverture : {overall:.4f} (par moyenne μ = 0,5 / 3 / 40 : "
              + " / ".join(f"{c:.3f}" for c in per_scale) + f") · largeur moyenne : {width:.3f} μ · temps : {seconds:.1f} s")
        if not 0.94 <= overall <= 0.96:
            reasons.append("la couverture n'est pas entre 0,94 et 0,96")
        elif not all(0.93 <= c <= 0.97 for c in per_scale):
            reasons.append("la couverture doit tenir pour chaque valeur de μ (entre 0,93 et 0,97) : ton intervalle ne "
                           "doit pas dépendre d'une échelle choisie d'avance")
        if not width <= 1.6:
            reasons.append("les intervalles sont trop larges (plus de 1,6 μ en moyenne)")
    if seconds > 20:
        reasons.append("plus de 20 secondes pour 4 500 intervalles : calcule une seule fois ce qui ne dépend pas de "
                       "l'échantillon")
    for reason in reasons:
        print(f"❌ {reason}")
    wbm.check("M02c.28", not reasons, computed=True)'''

M02C_28 = Ex(
    "M02c.28", "🏆", 3, 30, "Défi : un intervalle à 95 % avec dix valeurs d'une loi asymétrique",
    "construire un intervalle de confiance à 95 % pour la moyenne d'une loi exponentielle à partir de dix valeurs "
    "seulement, avec une couverture juste et une largeur raisonnable.", "fiche §5 à §7 ; Ex M02c.23", tracks="C",
    body="""Avec 10 valeurs d'une loi exponentielle, l'intervalle $\\bar{x} \\pm 1{,}96\\,\\frac{s}{\\sqrt{n}}$ ne couvre la vraie moyenne qu'environ 87 fois sur 100 (M02c.23), et le quantile de Student ne suffit pas. Écris `interval_10(sample)`, qui reçoit un array de **10 valeurs** tirées d'une loi exponentielle de moyenne $\\mu$ **inconnue**, et renvoie un intervalle `(low, high)` pour $\\mu$. **Objectifs**, mesurés sur les 4 500 échantillons de la cellule fournie (1 500 pour chacune des moyennes 0,5, 3 et 40, que ta fonction ne connaît pas) :
1. la couverture est entre 0,94 et 0,96, et entre 0,93 et 0,97 pour chaque moyenne ;
2. la largeur moyenne des intervalles est au plus $1{,}6\\,\\mu$ ;
3. moins de 20 secondes pour les 4 500 intervalles.

Tous les outils sont permis (NumPy, SciPy, une simulation). Pistes (`04_indices.md` les détaille) :
- le bootstrap des percentiles (fiche §7) : tente-le, et regarde quel objectif il manque ;
- une remarque clé : si $X$ suit une loi exponentielle de moyenne $\\mu$, alors $\\frac{X}{\\mu}$ suit la loi exponentielle de moyenne 1. Que peux-tu en dire de la loi de $\\frac{\\bar{X}}{\\mu}$ ? Dépend-elle de $\\mu$ ? Comment connaître ses quantiles, même sans formule ?

Dans ta copie : quelle méthode as-tu retenue ? Pourquoi ton intervalle n'est-il pas symétrique autour de $\\bar{x}$ ? Pourquoi le bootstrap des percentiles couvre-t-il mal avec 10 valeurs ?""",
    given=M02C_28_GIVEN,
    todo='''def interval_10(sample):
    """A 95 % confidence interval (low, high) for the mean of an exponential law, from 10 values."""
    raise NotImplementedError("le bootstrap, ou mieux : la loi de mean(sample) / μ ne dépend pas de μ")''',
    check=M02C_28_CHECK,
    solution='''# The law of mean(X) / μ is the same for every μ (it is the mean of 10 exponentials of mean 1): simulate it once,
# take its quantiles q_low and q_high, and invert q_low ≤ mean / μ ≤ q_high into mean / q_high ≤ μ ≤ mean / q_low.
PIVOT_MEANS = np.random.default_rng(2028).exponential(1.0, (200_000, 10)).mean(axis=1)
Q_LOW, Q_HIGH = np.percentile(PIVOT_MEANS, [2.5, 97.5])


def interval_10(sample):
    """A 95 % confidence interval (low, high) for the mean of an exponential law, from 10 values."""
    m = float(np.mean(sample))
    return m / Q_HIGH, m / Q_LOW


exact_low, exact_high = stats.gamma(10, scale=1 / 10).ppf([0.025, 0.975])   # the exact law of mean / μ
print(f"simulated quantiles of mean/μ: {Q_LOW:.4f}, {Q_HIGH:.4f} · exact (gamma law): {exact_low:.4f}, {exact_high:.4f}")


def bootstrap_percentile(sample, resamples=2000, rng=np.random.default_rng(0)):
    """The bootstrap percentile interval, for comparison."""
    means = np.asarray(sample)[rng.integers(0, len(sample), (resamples, len(sample)))].mean(axis=1)
    return tuple(np.percentile(means, [2.5, 97.5]))


boot = np.array([bootstrap_percentile(sample) for sample in SAMPLES_28])
print("bootstrap percentile coverage:", np.mean((boot[:, 0] <= SCALES_28) & (SCALES_28 <= boot[:, 1])))''',
    record='''wbm.record("M02c.28", True,
           mistakes={"un objectif au moins n'est pas atteint : relis les lignes ❌ et les pistes de 04_indices.md": False})''',
    note="Le bootstrap des percentiles couvre environ 86 fois sur 100 : avec 10 valeurs, la loi empirique n'a pas la "
         "longue queue de la vraie loi (aucune des 10 valeurs n'est très grande, le plus souvent), et ses intervalles "
         "sont trop étroits. La remarque clé : $\\frac{X_i}{\\mu}$ suit la loi exponentielle de moyenne 1, donc "
         "$\\frac{\\bar{X}}{\\mu}$ a **la même loi pour tous les $\\mu$** (on dit que c'est un **pivot**). On simule "
         "cette loi une fois, on lit ses quantiles $q_{0{,}025} \\approx 0{,}48$ et $q_{0{,}975} \\approx 1{,}71$, et "
         "$q_{0{,}025} \\le \\frac{\\bar{X}}{\\mu} \\le q_{0{,}975}$ s'inverse en "
         "$\\frac{\\bar{X}}{q_{0{,}975}} \\le \\mu \\le \\frac{\\bar{X}}{q_{0{,}025}}$, environ "
         "$[0{,}58\\,\\bar{x} ;\\ 2{,}09\\,\\bar{x}]$ : un intervalle **asymétrique**, plus long vers le haut, comme la "
         "loi. La loi de $\\frac{\\bar{X}}{\\mu}$ a d'ailleurs une formule (une loi gamma), qui donne les mêmes "
         "quantiles. Le bootstrap-t (fiche §7, idée voisine) couvre presque 95 %, mais avec des intervalles trop "
         "longs.",
)


PART_A = Part("A", "Ta librairie : moyennes d'échantillons, biais, erreur type et intervalle de confiance",
              "Fiche §3 à §7. Les cinq fonctions de `mymath/estimation.py`, puis les mêmes statistiques avec NumPy "
              "et SciPy.",
              given=TOOLS, exercises=[M02C_18, M02C_19, M02C_20, M02C_21])

PART_B = Part("B", "Une prédiction, deux expériences et une figure",
              "Fiche §4, §5, §7 et §9. Les moyennes d'une loi asymétrique, la couverture d'un intervalle, le volume en "
              "grande dimension, le théorème central limite en images.",
              exercises=[M02C_22, M02C_23, M02C_24, M02C_25])

PART_C = Part("C", "Erreurs classiques, tests et défi",
              "Fiche §4 à §7. Quatre erreurs d'intervalle à trouver, le test d'une fonction aléatoire, puis un "
              "intervalle exact pour dix valeurs.",
              exercises=[M02C_26, M02C_27, M02C_28])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M02c.1 à M02c.10, M02c.13, M02c.14 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M02c · Échantillons et estimation — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m02c_echantillons_estimation/03_notebook.ipynb`, créée "
               "par `python tools/start_chapter.py M02c`) ; la version du dépôt est mise à jour par Claude. Sur Colab, "
               "le badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M02c · Échantillons et estimation — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : statistiques descriptives, valeurs aberrantes, imputation, "
               "tirages sans remise, taille d'échantillon, théorème central limite, estimateurs, intervalles de "
               "confiance, covariance et matrice de covariance, percentile de latence, standardisation.\n"
               "- Écrire les cinq fonctions de `mymath/estimation.py` et les tester, puis utiliser NumPy et SciPy.\n"
               "- Prédire la distribution des moyennes, mesurer la couverture d'un intervalle et le volume en grande "
               "dimension, voir le théorème central limite, chasser des erreurs d'intervalle, tester une fonction "
               "aléatoire, construire un intervalle exact.\n\n"
               "**Rappel express.** $\\bar{x} = \\frac{1}{n}\\sum x_i$ ; $s^2 = \\frac{1}{n - 1}\\sum (x_i - \\bar{x})^2$ "
               "(`ddof=1`) ; $\\mathbb{E}[\\bar{X}] = \\mu$, $\\sigma(\\bar{X}) = \\frac{\\sigma}{\\sqrt{n}}$ ; pour $n$ "
               "grand, $\\bar{X} \\approx \\mathcal{N}\\big(\\mu, \\frac{\\sigma^2}{n}\\big)$ ; $\\text{EQM} = "
               "\\text{biais}^2 + \\text{variance}$ ; intervalle à 95 % : $\\bar{x} \\pm 1{,}96\\,\\frac{s}{\\sqrt{n}}$ ; "
               "$\\mathbb{V}(X + Y) = \\mathbb{V}(X) + \\mathbb{V}(Y) + 2\\operatorname{Cov}(X, Y)$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu résumer une série, repérer ses valeurs aberrantes, et dire ce qu'une imputation change ?\n"
               "2. Sais-tu utiliser la loi des grands nombres et le théorème central limite, et calculer le biais et "
               "l'erreur quadratique d'un estimateur ?\n"
               "3. Sais-tu calculer et interpréter une erreur type, un intervalle de confiance, une covariance et une "
               "corrélation ?\n\n"
               "**La suite** : le chapitre 2 de workbookIA (hasard et statistiques de base), puis M03, les probabilités "
               "conditionnelles.")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter=CHAPTER) if kind == "exercise" else setup_cell(kind))
    cells += objectives_cell()
    cells += paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO,
                         learner_context="from fractions import Fraction   # Fraction(3, 4) is accepted too, as \"3/4\"")
    for part in PARTS:
        cells += part_cells(part, kind)
    cells += footer_cells(kind)
    return cells


def main() -> int:
    for paper in PAPER:
        lines = [f'wbm.record("{paper.id}{letter}", {expr}{", " + options if options else ""})'
                 for letter, _, expr, options in paper.subs]
        check_unique_keys("\n".join(lines), paper.id)
    for ex in [e for part in PARTS for e in part.exercises]:
        for source in (ex.record, *(text for kind, text in ex.after if kind == "record")):
            if source:
                check_unique_keys(source, ex.id)
    write_notebook(f"{FOLDER}/03_notebook.ipynb", build("exercise"))
    write_notebook(f"{FOLDER}/05_solutions.ipynb", build("solution"))
    n_checks = sum(len(p.subs) for p in PAPER)
    n_ex = sum(len(part.exercises) for part in PARTS)
    print(f"✅ {FOLDER}/03_notebook.ipynb and 05_solutions.ipynb written ({len(PAPER)} paper exercises, "
          f"{n_checks} paper checks, {n_ex} notebook exercises)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
