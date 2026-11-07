#!/usr/bin/env python
"""Build the two notebooks of chapter M08 from a single source (used by Claude).

    python tools/chapters/build_m08.py
    python tools/run_all_notebooks.py chapitres/m08_tests/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m08_tests/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M08.1 to M08.9, 🔗 M08.13); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it. The data are new:
none is a test case of tests/test_m08_testing.py, an example of the fiche or of a docstring of testing.py, or an example
of workbookIA 8 (no penguins, no accuracy of 0.92 on 250 examples, no scores of two models on five folds, no maximum of
K validation scores, no disagreements of two models on one test set, no McNemar, no paired bootstrap of two models, no
feature selection before the cross-validation, no « 91,2 % contre 90,5 % »), nor of M02c (no accuracy of 0.92 on 500
examples, no Student quantile 2.262 for n = 10).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M08"
FOLDER = "chapitres/m08_tests"

F = 'kind="fraction", simplified=True'
LN = "le BIC utilise le logarithme népérien, ln"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M08.1", "Un test binomial à la main : un algorithme de compression est-il plus rapide sur douze fichiers ?", [
        ("a", "an irreducible fraction", '"33/2048"',
         f'''{F}, mistakes={{"compte aussi les façons de choisir les fichiers gagnés parmi les 12 : le coefficient '''
         '''binomial": "1/4096"}'''),
        ("b", "an irreducible fraction", '"79/4096"',
         f'''{F}, mistakes={{"la p-valeur compte toutes les issues au moins aussi extrêmes que l'observation, '''
         '''l'observation comprise": "13/4096", "la p-valeur additionne toutes les issues au moins aussi extrêmes, pas '''
         '''seulement celle qui a été observée": "33/2048"}'''),
        ("c", "an irreducible fraction", '"79/2048"',
         f'''{F}, mistakes={{"en bilatéral, compte aussi les issues aussi extrêmes de l'autre côté": "79/4096"}}'''),
        ("d", "True or False", "True",
         '''mistakes={"compare la p-valeur bilatérale au seuil : on rejette quand elle est au plus égale à 0,05": '''
         '''False}'''),
        ("e", "True or False", "False",
         '''mistakes={"compare la p-valeur bilatérale au seuil de 1 %": True}'''),
        ("f", "an integer", "10",
         '''mistakes={"pour ce nombre de fichiers, P(K ≥ k) dépasse encore 0,05 : recalcule-la": 9, '''
         '''"calcule aussi P(K ≥ k) pour un k plus petit : elle est peut-être déjà sous 0,05": 11}'''),
        ("g", "a number (3 decimals)", "1 - NormalDist().cdf(4 / math.sqrt(3))",
         '''decimals=3, mistakes={"la question demande la p-valeur unilatérale, 1 − Φ(z)": '''
         '''2 * (1 - NormalDist().cdf(4 / math.sqrt(3))), "la p-valeur est 1 − Φ(z), pas Φ(z)": '''
         '''NormalDist().cdf(4 / math.sqrt(3))}'''),
    ]),

    Paper("M08.2", "Un test par permutation exhaustif : deux groupes de trois mesures, vingt répartitions", [
        ("a", "an integer", "math.comb(6, 3)",
         '''mistakes={"l'ordre des temps dans un groupe ne compte pas : choisis les 3 temps du groupe A parmi les 6": '''
         '''{120, 720}, "le groupe A et le groupe B ne jouent pas le même rôle : ne divise pas par 2": 10}'''),
        ("b", "a number", "-5",
         '''mistakes={"t = x̄_A − x̄_B, dans cet ordre : le groupe A d'abord": 5}'''),
        ("c", "an irreducible fraction", '"1/20"',
         f'''{F}, mistakes={{"la répartition observée compte parmi les 20 : elle est au moins aussi extrême '''
         '''qu'elle-même": "0"}'''),
        ("d", "an irreducible fraction", '"1/10"',
         f'''{F}, mistakes={{"en bilatéral, compte aussi les répartitions extrêmes de l'autre côté, où t est grand et '''
         '''positif": "1/20"}'''),
        ("e", "True or False", "False",
         '''mistakes={"cherche la plus petite p-valeur bilatérale possible avec deux groupes de trois : peut-elle '''
         '''descendre sous 0,05 ?": True}'''),
        ("f", "an integer", "math.comb(8, 4)",
         '''mistakes={"le groupe A est choisi, le groupe B est le reste : ne divise pas par 2": 35, '''
         '''"l'ordre des valeurs dans un groupe ne compte pas : un coefficient binomial": 1680}'''),
        ("g", "a number", "1 / 1000",
         '''decimals=4, mistakes={"la p-valeur d'un test par permutation tiré au hasard n'est jamais nulle : la '''
         '''répartition observée compte comme un tirage": 0}'''),
    ]),

    Paper("M08.3", "Erreur de type I, erreur de type II et puissance d'un test binomial", [
        ("a", "an irreducible fraction", '"235/8192"',
         f'''{F}, mistakes={{"le risque de type I est P(K ≥ 11) sous H0 : l'issue K = 11 fait rejeter": "53/8192", '''
         '''"c'est le risque de la règle K ≥ 10 : la question porte sur K ≥ 11": "1471/16384"}'''),
        ("b", "a number (3 decimals)", "binom_tail(11, 14, 0.8)",
         '''decimals=3, mistakes={"la puissance se calcule sous l'alternative p = 0,8, pas sous H0": 235 / 8192, '''
         '''"la puissance est la probabilité de rejeter, P(K ≥ 11), pas son complément": 1 - binom_tail(11, 14, 0.8)}'''),
        ("c", "a number (3 decimals)", "1 - binom_tail(11, 14, 0.8)",
         '''decimals=3, mistakes={"β est le risque de ne pas rejeter quand p = 0,8 : le complément de la puissance": '''
         '''binom_tail(11, 14, 0.8)}'''),
        ("d", "an irreducible fraction", '"1471/16384"',
         f'''{F}, mistakes={{"le risque de type I additionne P(K = j) pour toutes les issues qui font rejeter, de 10 '''
         '''à 14": "1001/16384"}'''),
        ("e", "a number (3 decimals)", "binom_tail(10, 14, 0.8)",
         '''decimals=3, mistakes={"la puissance se calcule sous l'alternative p = 0,8, pas sous H0": 1471 / 16384}'''),
        ("f", "an integer", "11",
         '''mistakes={"le risque de type I de cette règle dépasse 0,05": 10, '''
         '''"une règle qui rejette plus souvent a peut-être déjà un risque de type I sous 0,05 : essaie-la": 12}'''),
    ]),

    Paper("M08.4", "Combien d'observations pour une puissance de 80 % ? (approximation normale)", [
        ("a", "a number (3 decimals)", "Z95",
         '''decimals=3, mistakes={"un test unilatéral au seuil α utilise z_{1−α} ; z_{1−α/2} sert au test bilatéral": '''
         '''NormalDist().inv_cdf(0.975)}'''),
        ("b", "a number (3 decimals)", "Z80",
         '''decimals=3, mistakes={"pour une puissance de 80 %, z_{1−β} est le quantile d'ordre 0,80 : il est positif": '''
         '''-Z80}'''),
        ("c", "an integer", "math.ceil(((Z95 + Z80) * 8 / 2) ** 2)",
         '''mistakes={"arrondis à l'entier supérieur : avec moins de mesures, la puissance n'atteint pas 80 %": 98, '''
         '''"le nombre de mesures est le carré de (z_{1−α} + z_{1−β}) σ/δ": 10, '''
         '''"le test est unilatéral : z_{1−α}, pas z_{1−α/2}": 126}'''),
        ("d", "an integer", "math.ceil(((NormalDist().inv_cdf(0.975) + Z80) * 8 / 2) ** 2)",
         '''mistakes={"un test bilatéral au seuil α utilise z_{1−α/2}": 99, '''
         '''"arrondis à l'entier supérieur : avec moins de mesures, la puissance n'atteint pas 80 %": 125}'''),
        ("e", "an integer", "math.ceil(((Z95 + Z80) * 8) ** 2)",
         '''mistakes={"le nombre de mesures varie comme 1/δ², pas comme 1/δ": 198, '''
         '''"arrondis à l'entier supérieur : avec moins de mesures, la puissance n'atteint pas 80 %": 395}'''),
        ("f", "a number (2 decimals)", "NormalDist().cdf(2 * math.sqrt(36) / 8 - Z95)",
         '''decimals=2, mistakes={"la puissance est Φ(δ√n/σ − z_{1−α}) : n'oublie pas √n": NormalDist().cdf(2 / 8 - Z95), '''
         '''"la puissance est Φ(…), pas 1 − Φ(…)": 1 - NormalDist().cdf(2 * math.sqrt(36) / 8 - Z95)}'''),
    ]),

    Paper("M08.5", "L'intervalle d'une proportion : Wald contre Wilson, avec peu de succès", [
        ("a", "a number", "3 / 50", "decimals=2"),
        ("b", "a number (4 decimals)", "0.06 - WALD_5",
         '''decimals=4, mistakes={"la demi-largeur de Wald est z √(p̂(1 − p̂)/n) : n'oublie pas la racine": '''
         '''0.06 - 1.96 * 0.06 * 0.94 / 50, "la borne basse retranche la demi-largeur à p̂": 0.06 + WALD_5}'''),
        ("c", "a list of 2 numbers (4 decimals)", "[0, 0.06 + WALD_5]",
         '''decimals=4, mistakes={"une proportion ne peut pas être négative : ramène la borne basse dans [0, 1]": '''
         '''[0.06 - WALD_5, 0.06 + WALD_5]}'''),
        ("d", "a list of 2 numbers (4 decimals)", "wilson(3, 50)",
         '''decimals=4, mistakes={"c'est l'intervalle de Wald : l'intervalle de Wilson a la formule de la fiche, §5": '''
         '''[0, 0.06 + WALD_5]}'''),
        ("e", "a number (4 decimals)", "sum(wilson(3, 50)) / 2",
         '''decimals=4, mistakes={"le centre de l'intervalle de Wilson n'est pas p̂ : il est tiré vers 1/2": 0.06}'''),
        ("f", "a number (4 decimals)", "wilson(0, 60)[1]",
         '''decimals=4, mistakes={"avec 0 erreur, l'intervalle de Wald se réduit à [0, 0] : la question demande celui '''
         '''de Wilson": 0}'''),
    ]),

    Paper("M08.6", "L'intervalle de Student d'une différence appariée : un serveur avant et après une mise à jour", [
        ("a", "a number", "D6.mean()", "decimals=2"),
        ("b", "a number (4 decimals)", "D6.std(ddof=1)",
         '''decimals=4, mistakes={"ddof = 1 : divise la somme des carrés des écarts par n − 1 = 5": D6.std(), '''
         '''"l'écart-type est la racine de la variance": D6.var(ddof=1)}'''),
        ("c", "a number (3 decimals)", "SE6",
         '''decimals=3, mistakes={"l'erreur type divise l'écart-type par √n, pas par n": D6.std(ddof=1) / 6}'''),
        ("d", "a number (3 decimals)", "T6",
         '''decimals=3, mistakes={"le nombre de degrés de liberté est n − 1, avec n = 6 paires": '''
         '''student.ppf(0.975, 6), "avec six paires, le quantile de la loi de Student remplace celui de la loi '''
         '''normale": 1.96, "un intervalle à 95 % laisse 2,5 % de chaque côté : le quantile d'ordre 0,975": '''
         '''student.ppf(0.95, 5)}'''),
        ("e", "a list of 2 numbers (2 decimals)", "[D6.mean() - T6 * SE6, D6.mean() + T6 * SE6]",
         '''decimals=2, mistakes={"avec six paires, le quantile de Student à 5 degrés de liberté remplace 1,96": '''
         '''[D6.mean() - 1.96 * SE6, D6.mean() + 1.96 * SE6]}'''),
        ("f", "a number (2 decimals)", "math.sqrt(A6.var(ddof=1) / 6 + B6.var(ddof=1) / 6)", "decimals=2"),
        ("g", "True or False", "False",
         '''mistakes={"regarde le signe des deux bornes de l'intervalle": True}'''),
    ]),

    Paper("M08.7", "Vingt tests au seuil de 5 % : les faux positifs attendus, puis Bonferroni", [
        ("a", "a number", "20 * 0.05",
         '''decimals=2, mistakes={"chacun des 20 tests a une probabilité 0,05 de donner un faux positif : additionne": '''
         '''0.05}'''),
        ("b", "a number (4 decimals)", "1 - 0.95 ** 20",
         '''decimals=4, mistakes={"c'est la probabilité d'aucun faux positif : la question demande son complément": '''
         '''0.95 ** 20, "20 × 0,05 compte plusieurs fois les cas à plusieurs faux positifs : passe par la probabilité '''
         '''d'aucun faux positif": 1.0}'''),
        ("c", "a number", "0.05 / 20",
         '''decimals=4, mistakes={"Bonferroni divise le seuil par le nombre de tests, il ne le multiplie pas": 1.0}'''),
        ("d", "a number (4 decimals)", "1 - (1 - 0.05 / 20) ** 20", "decimals=4"),
        ("e", "a list of 3 numbers", "[0.001 * 20, 0.004 * 20, 0.03 * 20]",
         '''decimals=4, mistakes={"la p-valeur ajustée de Bonferroni multiplie p par m, elle ne la divise pas": '''
         '''[0.001 / 20, 0.004 / 20, 0.03 / 20], "m est le nombre de tests faits, pas le nombre de p-valeurs citées": '''
         '''[0.003, 0.012, 0.09]}'''),
        ("f", "an integer", "1",
         '''mistakes={"compare chaque p-valeur ajustée au risque de la famille, 0,05": {2, 3}}'''),
    ]),

    Paper("M08.8", "L'AIC et le BIC de deux modèles, à partir de leurs log-vraisemblances", [
        ("a", "a number", "2 * 3 - 2 * (-412.6)",
         '''decimals=1, mistakes={"AIC = 2k − 2 ln L : quand ln L est négatif, −2 ln L est positif": 2 * 3 - 825.2}'''),
        ("b", "a number", "2 * 7 - 2 * (-405.1)",
         '''decimals=1, mistakes={"AIC = 2k − 2 ln L : quand ln L est négatif, −2 ln L est positif": 2 * 7 - 810.2}'''),
        ("c", "a number (1 decimal)", "3 * math.log(200) + 825.2",
         f'''decimals=1, mistakes={{"{LN}": 3 * math.log10(200) + 825.2}}'''),
        ("d", "a number (1 decimal)", "7 * math.log(200) + 810.2",
         f'''decimals=1, mistakes={{"{LN}": 7 * math.log10(200) + 810.2}}'''),
        ("e", "1 or 2", "2", '''choices=[1, 2]'''),
        ("f", "1 or 2", "1", '''choices=[1, 2]'''),
        ("g", "a number (3 decimals)", "2 * math.log(200)",
         f'''decimals=3, mistakes={{"le gain de log-vraisemblance compte double dans le BIC, qui contient −2 ln L": '''
         f'''4 * math.log(200), "{LN}": 2 * math.log10(200)}}'''),
    ]),

    Paper("M08.9", "Un facteur de Bayes entre deux taux de clics", [
        ("a", "a number (3 decimals)", "L_A9", "decimals=3"),
        ("b", "a number (3 decimals)", "L_B9", "decimals=3"),
        ("c", "a number (2 decimals)", "L_B9 / L_A9",
         '''decimals=2, mistakes={"BF_BA met l'évidence de M_B au numérateur": L_A9 / L_B9}'''),
        ("d", "a number (2 decimals)", "(BF9 / 3) / (1 + BF9 / 3)",
         '''decimals=2, mistakes={"tiens compte de la cote a priori : la cote a posteriori est le facteur de Bayes fois '''
         '''la cote a priori": BF9 / (1 + BF9), "une cote n'est pas une probabilité : P = cote / (1 + cote)": BF9 / 3}'''),
        ("e", "an irreducible fraction", '"1/41"',
         f'''{F}, mistakes={{"recompte les nombres de clics possibles, de la plus petite valeur à la plus grande": '''
         '''"1/40"}'''),
        ("f", "a number (1 decimal)", "L_A9 * 41",
         '''decimals=1, mistakes={"BF_AC met l'évidence de M_A au numérateur": 1 / (41 * L_A9)}'''),
    ]),

    Paper("M08.13", "Pont : l'importance d'une feature par permutation, sur un petit tableau", [
        ("a", "a number", "1"),
        ("b", "an irreducible fraction", '"1/3"', F),
        ("c", "an irreducible fraction", '"2/3"',
         f'''{F}, mistakes={{"l'importance est l'accuracy de départ moins l'accuracy après le mélange": "-2/3"}}'''),
        ("d", "an irreducible fraction", '"2/3"', F),
        ("e", "an irreducible fraction", '"1/3"',
         f'''{F}, mistakes={{"l'importance est l'accuracy de départ moins l'accuracy après le mélange": "-1/3"}}'''),
        ("f", "a number", "0"),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math
from statistics import NormalDist

import numpy as np
from scipy.stats import t as student


def binom_tail(c, n, p):
    """P(K ≥ c) for K of law B(n, p)."""
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(c, n + 1))


def wilson(k, n, z=1.96):
    """Wilson's interval [low, high] after k successes in n trials."""
    p_hat, denominator = k / n, 1 + z * z / n
    center = (p_hat + z * z / (2 * n)) / denominator
    half = z * math.sqrt(p_hat * (1 - p_hat) / n + z * z / (4 * n * n)) / denominator
    return [center - half, center + half]


Z95, Z80 = NormalDist().inv_cdf(0.95), NormalDist().inv_cdf(0.80)            # M08.4
WALD_5 = 1.96 * math.sqrt(0.06 * 0.94 / 50)                                  # M08.5: the half-width of Wald
A6 = np.array([52, 47, 61, 55, 49, 58], dtype=float)                         # M08.6: before, after
B6 = np.array([48, 46, 55, 54, 45, 53], dtype=float)
D6 = A6 - B6
SE6, T6 = D6.std(ddof=1) / math.sqrt(6), student.ppf(0.975, 5)
L_A9 = math.comb(40, 6) * 0.1 ** 6 * 0.9 ** 34                               # M08.9: the evidences
L_B9 = math.comb(40, 6) * 0.2 ** 6 * 0.8 ** 34
BF9 = L_B9 / L_A9'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M08.1 à M08.9, 🔗 M08.13)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"7/9\"` ;\n"
               "- une liste `[-1.5, 2.5]` (deux bornes, une liste de valeurs), ou `True` / `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M08.16 to M08.20)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import itertools
import math
from statistics import NormalDist

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from wbm.nbtools import checked, drawn, run_pytest_group


def raised(function, *args, **kwargs):
    """The name of the exception that function(*args, **kwargs) raises, or "aucune" if it returns.

    NotImplementedError (a TODO not done yet) goes through, for wbm.attempt to show ⏳; so do the errors of a code
    that cannot run (a missing import, a misspelt name such as ValueErorr), for the check to name them."""
    try:
        function(*args, **kwargs)
    except (NotImplementedError, NameError, AttributeError, ImportError):
        raise
    except Exception as exc:  # noqa: BLE001 - any other error is the answer
        return type(exc).__name__
    return "aucune"'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M08")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/testing.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "NumPy et `math` suffisent, avec deux quantiles permis : `statistics.NormalDist().inv_cdf` (loi normale) et "
         "`scipy.stats.t.ppf` (loi de Student). Les autres outils de `scipy.stats` (`binomtest`, `permutation_test`, "
         "`ttest_rel`…) sont interdits dans `testing.py` : les tests comparent tes résultats aux leurs, et un test "
         "vérifie que tu ne t'en sers pas. Les nombres renvoyés sont des `float` de Python.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of testing.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_testing_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m08_testing.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m08_testing.py", "{keyword}", impl="ref")')]


PYTHON_FLOAT = "la docstring demande un float de Python : float(...) convertit un nombre de NumPy"

M08_16 = Ex(
    "M08.16", "🔨", 1, 15, "Le test binomial exact · `binomial_test`",
    "programmer la p-valeur exacte d'un test binomial, unilatérale ou bilatérale, et refuser les entrées qui n'ont pas "
    "de sens.", "fiche §2", tracks="C, E", mymath="testing.py",
    body=HOWTO + r"""

Écris `binomial_test(k, n, p=0.5, alternative="two-sided")` (fiche §2) : la p-valeur exacte du test de $H_0$ : « la probabilité de succès vaut $p$ », après $k$ succès en $n$ essais. Avec $K$ de loi $\mathcal{B}(n, p)$ :
- `"greater"` : $P(K \ge k)$ ; `"less"` : $P(K \le k)$ ;
- `"two-sided"` : la somme des $P(K = j)$ sur toutes les issues $j$ au plus aussi probables que l'observation, $P(K = j) \le P(K = k)$ (à un facteur $1 + 10^{-7}$ près, pour les arrondis), plafonnée à 1 ;
- une `ValueError` si $k$, $n$ ou $p$ sort de son domaine, ou si `alternative` est inconnue.

Pour les coefficients binomiaux, `math.comb(n, j)`.

La vérification calcule :
- a) `binomial_test(13, 16, alternative="greater")` (4 décimales) ;
- b) `binomial_test(13, 16)` (4 décimales) ;
- c) `binomial_test(1, 18, p=0.3, alternative="less")` (4 décimales) ;
- d) `binomial_test(9, 15, p=0.3)` (4 décimales) ;
- e) le nom de l'erreur levée par `binomial_test(4, 3)` ;
- f) le nom du type de `binomial_test(13, 16)`, en texte.

Dans ta copie : calcule a) à la main, en fraction. Pourquoi b) est-il exactement le double de a), et d) **pas** le double de $P(K \ge 9)$ ? Quelles issues $j$ la p-valeur d) additionne-t-elle ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M08.16a"):
    wbm.check("M08.16a", mymath.testing.binomial_test(13, 16, alternative="greater"), computed=True)
with checked("M08.16b"):
    wbm.check("M08.16b", mymath.testing.binomial_test(13, 16), computed=True)
with checked("M08.16c"):
    wbm.check("M08.16c", mymath.testing.binomial_test(1, 18, p=0.3, alternative="less"), computed=True)
with checked("M08.16d"):
    wbm.check("M08.16d", mymath.testing.binomial_test(9, 15, p=0.3), computed=True)
with checked("M08.16e"):
    wbm.check("M08.16e", raised(mymath.testing.binomial_test, 4, 3), computed=True)
with checked("M08.16f"):
    wbm.check("M08.16f", type(mymath.testing.binomial_test(13, 16)).__name__, computed=True)''',
    solution=LOAD_REF + '''
binomial_test = mymath.testing.binomial_test
print("a)", binomial_test(13, 16, alternative="greater"), " b)", binomial_test(13, 16),
      " c)", binomial_test(1, 18, p=0.3, alternative="less"), " d)", binomial_test(9, 15, p=0.3))
print("e)", raised(binomial_test, 4, 3), " f)", type(binomial_test(13, 16)).__name__)
pmf_9 = [math.comb(15, j) * 0.3 ** j * 0.7 ** (15 - j) for j in range(16)]
print("d) outcomes at most as likely as k = 9:", [j for j in range(16) if pmf_9[j] <= pmf_9[9] * (1 + 1e-7)])''',
    record=f'''wbm.record("M08.16a", 697 / 65536, decimals=4,
           mistakes={{"P(K ≥ k) compte aussi l'issue observée K = k": 137 / 65536}})
wbm.record("M08.16b", 697 / 32768, decimals=4,
           mistakes={{"en bilatéral, ajoute les issues de l'autre côté qui sont au plus aussi probables que "
                      "l'observation": 697 / 65536}})
wbm.record("M08.16c", 0.7 ** 18 + 18 * 0.3 * 0.7 ** 17, decimals=4,
           mistakes={{"P(K ≤ k) compte aussi l'issue observée K = k": 0.7 ** 18}})
wbm.record("M08.16d", sum(math.comb(15, j) * 0.3 ** j * 0.7 ** (15 - j) for j in [0] + list(range(9, 16))),
           decimals=4,
           mistakes={{"le test bilatéral ne double pas la p-valeur unilatérale : il additionne les issues au plus "
                      "aussi probables que l'observation, des deux côtés":
                         2 * sum(math.comb(15, j) * 0.3 ** j * 0.7 ** (15 - j) for j in range(9, 16)),
                     "ajoute aussi les issues de l'autre côté qui sont au plus aussi probables que l'observation":
                         sum(math.comb(15, j) * 0.3 ** j * 0.7 ** (15 - j) for j in range(9, 16))}})
wbm.record("M08.16e", "ValueError",
           mistakes={{"k ne peut pas dépasser n : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M08.16f", "float",
           mistakes={{"{PYTHON_FLOAT}": "float64"}})''',
    after=tests_cells("test_binomial_test_"),
    note=r"a) $P(K \ge 13) = \frac{560 + 120 + 16 + 1}{2^{16}} = \frac{697}{65\,536} \approx 0{,}0106$. b) Pour $p = "
         r"\frac{1}{2}$, la loi est symétrique : les issues au plus aussi probables que 13 sont $0, 1, 2, 3$ et $13$ à "
         r"$16$, et la p-valeur bilatérale est le double de l'unilatérale, $\approx 0{,}0213$. c) $P(K \le 1) = 0{,}7^{18} "
         r"+ 18 \times 0{,}3 \times 0{,}7^{17} \approx 0{,}0142$. d) Pour $p = 0{,}3$, la loi n'est pas symétrique : "
         r"$P(K = 9) \approx 0{,}0116$, et seule l'issue $j = 0$ ($\approx 0{,}0047$) est au plus aussi probable de "
         r"l'autre côté ; la p-valeur additionne $j = 0$ et $j = 9$ à $15$, $\approx 0{,}0200$, alors que doubler "
         r"$P(K \ge 9) \approx 0{,}0152$ donnerait $0{,}0305$.",
)

X_17, Y_17 = "[8.1, 9.4, 7.7, 9.0]", "[6.9, 7.2, 8.0, 6.5, 7.4]"
U_17 = "[14.2, 15.0, 13.9, 14.8, 15.3, 14.6, 15.1, 14.4]"
V_17 = "[12.1, 12.9, 12.5, 13.0, 12.3, 12.8, 12.6, 12.2]"

M08_17 = Ex(
    "M08.17", "🔨", 2, 25, "Le test par permutation à deux échantillons · `permutation_test`",
    "programmer un test par permutation reproductible, qui suit une procédure fixée, et voir qu'il ne renvoie jamais "
    "une p-valeur nulle.", "fiche §3", tracks="C, E", mymath="testing.py",
    body=r"""Écris `permutation_test(x, y, n_permutations=9999, alternative="two-sided", seed=0)` (fiche §3), en suivant **exactement** la procédure de sa docstring :
- la statistique $t = \bar{x} - \bar{y}$, et les valeurs réunies, `x` d'abord, puis `y` ;
- `n_permutations` fois : `perm = rng.permutation(pooled)`, avec **un seul** générateur `rng = np.random.default_rng(seed)` créé avant la boucle, puis $t_{\text{perm}}$ = la moyenne de `perm[:len(x)]` moins celle de `perm[len(x):]` ;
- $C$, le nombre de tirages au moins aussi extrêmes que $t$, à $10^{-9}$ près pour les arrondis (`"greater"` : $t_{\text{perm}} \ge t - 10^{-9}$ ; `"less"` : $t_{\text{perm}} \le t + 10^{-9}$ ; `"two-sided"` : $|t_{\text{perm}}| \ge |t| - 10^{-9}$) ;
- la p-valeur $\frac{C + 1}{B + 1}$, avec $B$ = `n_permutations` ;
- une `ValueError` si un échantillon est vide, si `n_permutations` est plus petit que 1 ou si `alternative` est inconnue.

Suivre la procédure à la lettre (le même générateur, utilisé dans le même ordre) donne exactement les p-valeurs de la référence : c'est ce que vérifient les tests.

Un ancien outil a demandé $x = (8{,}1 ;\ 9{,}4 ;\ 7{,}7 ;\ 9{,}0)$ minutes pour quatre tâches, et un nouvel outil $y = (6{,}9 ;\ 7{,}2 ;\ 8{,}0 ;\ 6{,}5 ;\ 7{,}4)$ minutes pour cinq autres. La vérification calcule :
- a) `permutation_test(x, y, n_permutations=1999, alternative="greater", seed=3)` (4 décimales) ;
- b) la même chose avec `alternative="two-sided"` (4 décimales) ;
- c) `permutation_test(u, v, n_permutations=499, alternative="greater", seed=1)` pour deux groupes de huit mesures bien séparées, $u = (14{,}2 ;\ 15{,}0 ;\ 13{,}9 ;\ 14{,}8 ;\ 15{,}3 ;\ 14{,}6 ;\ 15{,}1 ;\ 14{,}4)$ et $v = (12{,}1 ;\ 12{,}9 ;\ 12{,}5 ;\ 13{,}0 ;\ 12{,}3 ;\ 12{,}8 ;\ 12{,}6 ;\ 12{,}2)$ (4 décimales) ;
- d) le nom de l'erreur levée par `permutation_test([], [4, 5])` ;
- e) le nom du type de la p-valeur de a), en texte.

Dans ta copie : la p-valeur exacte de a), calculée sur les 126 répartitions, vaut $\frac{2}{126}$ (M08.20 la retrouve). De combien a) s'en écarte-t-il ? Est-ce compatible avec l'erreur type d'une proportion estimée sur 1 999 tirages ? Pourquoi c) ne peut-il pas descendre sous $\frac{1}{500}$, et que faudrait-il pour une p-valeur plus petite ?""",
    todo=LOAD_LEARNER,
    check=f'''X_17, Y_17 = {X_17}, {Y_17}
U_17 = {U_17}
V_17 = {V_17}
with checked("M08.17a"):
    wbm.check("M08.17a", mymath.testing.permutation_test(X_17, Y_17, n_permutations=1999, alternative="greater",
                                                         seed=3), computed=True)
with checked("M08.17b"):
    wbm.check("M08.17b", mymath.testing.permutation_test(X_17, Y_17, n_permutations=1999, alternative="two-sided",
                                                         seed=3), computed=True)
with checked("M08.17c"):
    wbm.check("M08.17c", mymath.testing.permutation_test(U_17, V_17, n_permutations=499, alternative="greater",
                                                         seed=1), computed=True)
with checked("M08.17d"):
    wbm.check("M08.17d", raised(mymath.testing.permutation_test, [], [4, 5]), computed=True)
with checked("M08.17e"):
    wbm.check("M08.17e", type(mymath.testing.permutation_test(X_17, Y_17, n_permutations=1999, alternative="greater",
                                                              seed=3)).__name__, computed=True)''',
    solution=LOAD_REF + f'''
permutation_test = mymath.testing.permutation_test
X_17, Y_17 = {X_17}, {Y_17}
U_17 = {U_17}
V_17 = {V_17}
p_a = permutation_test(X_17, Y_17, n_permutations=1999, alternative="greater", seed=3)
print("a)", p_a, " b)", permutation_test(X_17, Y_17, n_permutations=1999, alternative="two-sided", seed=3),
      " c)", permutation_test(U_17, V_17, n_permutations=499, alternative="greater", seed=1))
print("d)", raised(permutation_test, [], [4, 5]), " e)", type(p_a).__name__)
print("exact one-sided p-value 2/126 =", 2 / 126, "· standard error of the estimate:",
      math.sqrt((2 / 126) * (1 - 2 / 126) / 1999))''',
    record=f'''wbm.record("M08.17a", 38 / 2000, decimals=4,
           mistakes={{"la p-valeur est (C + 1)/(B + 1) : la répartition observée compte comme un tirage": 37 / 1999}})
wbm.record("M08.17b", 52 / 2000, decimals=4,
           mistakes={{"la p-valeur est (C + 1)/(B + 1) : la répartition observée compte comme un tirage": 51 / 1999}})
wbm.record("M08.17c", 1 / 500, decimals=4,
           mistakes={{"la p-valeur d'un test par permutation tiré au hasard n'est jamais nulle : (C + 1)/(B + 1)": 0.0}})
wbm.record("M08.17d", "ValueError",
           mistakes={{"un échantillon vide n'a pas de moyenne : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M08.17e", "float",
           mistakes={{"{PYTHON_FLOAT}": "float64"}})''',
    after=tests_cells("test_permutation_test_"),
    note=r"a) $C = 37$ tirages sur 1 999 sont au moins aussi extrêmes : $\frac{38}{2000} = 0{,}019$, pour une valeur "
         r"exacte de $\frac{2}{126} \approx 0{,}0159$. L'écart, 0,003, vaut un peu plus d'une erreur type "
         r"($\sqrt{0{,}0159 \times 0{,}984 / 1999} \approx 0{,}0028$) : rien d'anormal. b) $\frac{52}{2000} = 0{,}026$, "
         r"pour une valeur exacte de $\frac{3}{126} \approx 0{,}0238$. c) Aucun des 499 tirages n'atteint l'écart "
         r"observé ($C = 0$) : la p-valeur vaut $\frac{1}{500}$, la plus petite possible avec 499 permutations. Pour "
         r"descendre plus bas, il faut plus de permutations ; la p-valeur exacte, $\frac{1}{12\,870}$, demanderait de "
         r"parcourir les $\binom{16}{8} = 12\,870$ répartitions.",
)

A_18, B_18 = "[12.4, 11.8, 13.1, 12.9, 12.2]", "[11.9, 11.6, 12.2, 12.5, 12.0]"

M08_18 = Ex(
    "M08.18", "🔨", 1, 20, "Les intervalles de Wilson et de Student · `proportion_ci, paired_difference_ci`",
    "programmer les intervalles de Wald et de Wilson d'une proportion, et l'intervalle de Student d'une différence "
    "appariée.", "fiche §5", tracks="C, E", mymath="testing.py",
    body=r"""Écris (fiche §5) :
- `proportion_ci(k, n, level=0.95, method="wilson")` : l'intervalle `(low, high)` d'une proportion après $k$ succès en $n$ essais, par la méthode de Wilson ou de Wald (`method="wald"`), avec $z$ le quantile d'ordre $\frac{1 + \text{level}}{2}$ de la loi normale ; les bornes sont ramenées dans $[0, 1]$ ; une `ValueError` si $k$, $n$ ou `level` sort de son domaine, ou si `method` est inconnue ;
- `paired_difference_ci(a, b, level=0.95)` : l'intervalle de Student $\bar{d} \pm t\,\frac{s_d}{\sqrt{n}}$ de la moyenne des différences $d_i = a_i - b_i$, avec $s_d$ l'écart-type des différences ($\mathrm{ddof} = 1$) et $t$ le quantile d'ordre $\frac{1 + \text{level}}{2}$ de la loi de Student à $n - 1$ degrés de liberté (`scipy.stats.t.ppf(q, n - 1)`) ; une `ValueError` si les longueurs diffèrent, s'il y a moins de deux paires ou si `level` sort de $]0, 1[$.

Les deux fonctions renvoient un `tuple` de deux `float`.

La vérification calcule (des listes de 2 nombres, 4 décimales) :
- a) `proportion_ci(4, 30)` ;
- b) `proportion_ci(4, 30, method="wald")` ;
- c) `proportion_ci(30, 30)` ;
- d) `proportion_ci(4, 30, level=0.9)` ;
- e) `paired_difference_ci(a, b)` pour les temps de compilation (en secondes) de cinq projets avant, $a = (12{,}4 ;\ 11{,}8 ;\ 13{,}1 ;\ 12{,}9 ;\ 12{,}2)$, et après une mise à jour du compilateur, $b = (11{,}9 ;\ 11{,}6 ;\ 12{,}2 ;\ 12{,}5 ;\ 12{,}0)$ ;

puis :
- f) le nom de l'erreur levée par `paired_difference_ci([4, 5], [1, 2, 3])` ;
- g) le nom du type de `proportion_ci(4, 30)`, en texte.

Dans ta copie : pourquoi l'intervalle de Wilson c) ne contient-il pas seulement la valeur 1 ? Pourquoi d) est-il plus étroit que a) ? La mise à jour du compilateur a-t-elle un effet, d'après e) ?""",
    todo=LOAD_LEARNER,
    check=f'''A_18, B_18 = {A_18}, {B_18}
with checked("M08.18a"):
    wbm.check("M08.18a", list(mymath.testing.proportion_ci(4, 30)), computed=True)
with checked("M08.18b"):
    wbm.check("M08.18b", list(mymath.testing.proportion_ci(4, 30, method="wald")), computed=True)
with checked("M08.18c"):
    wbm.check("M08.18c", list(mymath.testing.proportion_ci(30, 30)), computed=True)
with checked("M08.18d"):
    wbm.check("M08.18d", list(mymath.testing.proportion_ci(4, 30, level=0.9)), computed=True)
with checked("M08.18e"):
    wbm.check("M08.18e", list(mymath.testing.paired_difference_ci(A_18, B_18)), computed=True)
with checked("M08.18f"):
    wbm.check("M08.18f", raised(mymath.testing.paired_difference_ci, [4, 5], [1, 2, 3]), computed=True)
with checked("M08.18g"):
    wbm.check("M08.18g", type(mymath.testing.proportion_ci(4, 30)).__name__, computed=True)''',
    solution=LOAD_REF + f'''
proportion_ci, paired_ci = mymath.testing.proportion_ci, mymath.testing.paired_difference_ci
A_18, B_18 = {A_18}, {B_18}
print("a)", proportion_ci(4, 30), " b)", proportion_ci(4, 30, method="wald"))
print("c)", proportion_ci(30, 30), " d)", proportion_ci(4, 30, level=0.9))
print("e)", paired_ci(A_18, B_18), " f)", raised(paired_ci, [4, 5], [1, 2, 3]),
      " g)", type(proportion_ci(4, 30)).__name__)''',
    record=f'''def wilson_18(k, n, z):
    p_hat, denominator = k / n, 1 + z * z / n
    center = (p_hat + z * z / (2 * n)) / denominator
    half = z * math.sqrt(p_hat * (1 - p_hat) / n + z * z / (4 * n * n)) / denominator
    return [max(0.0, center - half), min(1.0, center + half)]


def wald_18(k, n, z):
    half = z * math.sqrt(k / n * (1 - k / n) / n)
    return [max(0.0, k / n - half), min(1.0, k / n + half)]


Z_95, Z_90 = NormalDist().inv_cdf(0.975), NormalDist().inv_cdf(0.95)
d_18 = np.array({A_18}) - np.array({B_18})
SE_18 = d_18.std(ddof=1) / math.sqrt(5)
wbm.record("M08.18a", wilson_18(4, 30, Z_95), decimals=4,
           mistakes={{"la méthode par défaut est celle de Wilson : relis la docstring": wald_18(4, 30, Z_95),
                     "z est le quantile d'ordre (1 + level)/2, pas d'ordre level": wilson_18(4, 30, Z_90)}})
wbm.record("M08.18b", wald_18(4, 30, Z_95), decimals=4,
           mistakes={{"z est le quantile d'ordre (1 + level)/2, pas d'ordre level": wald_18(4, 30, Z_90)}})
wbm.record("M08.18c", wilson_18(30, 30, Z_95), decimals=4,
           mistakes={{"avec method=\\"wilson\\" (par défaut), l'intervalle ne se réduit pas à un point":
                         [1.0, 1.0]}})
wbm.record("M08.18d", wilson_18(4, 30, NormalDist().inv_cdf(0.95)), decimals=4,
           mistakes={{"z est le quantile d'ordre (1 + level)/2, pas d'ordre level":
                         wilson_18(4, 30, NormalDist().inv_cdf(0.9))}})
wbm.record("M08.18e", [d_18.mean() - stats.t.ppf(0.975, 4) * SE_18, d_18.mean() + stats.t.ppf(0.975, 4) * SE_18],
           decimals=4,
           mistakes={{"avec cinq paires, le quantile de Student à n − 1 = 4 degrés de liberté remplace celui de la loi "
                      "normale": [d_18.mean() - Z_95 * SE_18, d_18.mean() + Z_95 * SE_18],
                     "le nombre de degrés de liberté est n − 1": [d_18.mean() - stats.t.ppf(0.975, 5) * SE_18,
                                                                 d_18.mean() + stats.t.ppf(0.975, 5) * SE_18],
                     "l'écart-type des différences se calcule avec ddof = 1":
                         [d_18.mean() - stats.t.ppf(0.975, 4) * d_18.std() / math.sqrt(5),
                          d_18.mean() + stats.t.ppf(0.975, 4) * d_18.std() / math.sqrt(5)]}})
wbm.record("M08.18f", "ValueError",
           mistakes={{"des mesures appariées ont la même longueur : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M08.18g", "tuple",
           mistakes={{"la docstring demande un tuple (low, high)": {{"list", "ndarray"}}}})''',
    after=tests_cells("test_proportion_ci_ or test_paired_difference_ci_"),
    note=r"a) $\hat{p} = \frac{4}{30} \approx 0{,}133$ ; l'intervalle de Wilson, $[0{,}0531 ;\ 0{,}2968]$, est décalé vers "
         r"$\frac{1}{2}$ par rapport à celui de Wald, $[0{,}0117 ;\ 0{,}2550]$. c) Avec 30 succès sur 30, Wald donnerait "
         r"$[1, 1]$, un intervalle sans largeur ; Wilson donne $[0{,}8865 ;\ 1]$ : 30 succès n'excluent pas une "
         r"probabilité de 0,9. d) À 90 %, $z \approx 1{,}645$ au lieu de 1,96 : l'intervalle est plus étroit, au prix "
         r"d'un risque plus grand de manquer la vraie valeur. e) Les différences valent 0,5 ; 0,2 ; 0,9 ; 0,4 ; 0,2, de "
         r"moyenne 0,44 s, et l'intervalle $[0{,}0823 ;\ 0{,}7977]$ ne contient pas 0 : la mise à jour accélère la "
         r"compilation, de quelques dixièmes de seconde.",
)

M08_19 = Ex(
    "M08.19", "🔨", 1, 10, "Bonferroni, l'AIC et le BIC · `bonferroni, aic_bic`",
    "programmer les p-valeurs ajustées de Bonferroni et les deux critères d'information.", "fiche §6 et §7",
    tracks="C", mymath="testing.py",
    body=r"""Écris (fiche §6 et §7) :
- `bonferroni(p_values)` : les p-valeurs ajustées $\min(1, m\,p_i)$, avec $m$ le nombre de tests, en tableau NumPy, dans le même ordre ; une `ValueError` si la liste est vide ou si une valeur sort de $[0, 1]$ ;
- `aic_bic(log_likelihood, k, n)` : le couple $(2k - 2\ln L,\ k\ln n - 2\ln L)$, avec le logarithme népérien ; une `ValueError` si $k < 1$ ou $n < 1$.

La vérification calcule :
- a) `bonferroni([0.002, 0.03, 0.2, 0.011])` (une liste, 4 décimales) ;
- b) `bonferroni([0.5, 0.7])` (une liste) ;
- c) `aic_bic(-57.3, 4, 120)` (une liste, 4 décimales) ;
- d) le nom de l'erreur levée par `bonferroni([0.05, 1.2, 0.3])` ;
- e) le nom du type de `bonferroni([0.2])`, en texte.

Dans ta copie : au risque de la famille de 5 %, quels tests de a) rejettent leur hypothèse nulle ? Pourquoi plafonner à 1 en b) ? Dans c), lequel des deux critères pénalise le plus les 4 paramètres, et à partir de quel $n$ est-ce toujours le cas ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M08.19a"):
    wbm.check("M08.19a", np.asarray(mymath.testing.bonferroni([0.002, 0.03, 0.2, 0.011])).tolist(), computed=True)
with checked("M08.19b"):
    wbm.check("M08.19b", np.asarray(mymath.testing.bonferroni([0.5, 0.7])).tolist(), computed=True)
with checked("M08.19c"):
    wbm.check("M08.19c", list(mymath.testing.aic_bic(-57.3, 4, 120)), computed=True)
with checked("M08.19d"):
    wbm.check("M08.19d", raised(mymath.testing.bonferroni, [0.05, 1.2, 0.3]), computed=True)
with checked("M08.19e"):
    wbm.check("M08.19e", type(mymath.testing.bonferroni([0.2])).__name__, computed=True)''',
    solution=LOAD_REF + '''
bonferroni, aic_bic = mymath.testing.bonferroni, mymath.testing.aic_bic
print("a)", bonferroni([0.002, 0.03, 0.2, 0.011]), " b)", bonferroni([0.5, 0.7]), " c)", aic_bic(-57.3, 4, 120))
print("d)", raised(bonferroni, [0.05, 1.2, 0.3]), " e)", type(bonferroni([0.2])).__name__)''',
    record=f'''wbm.record("M08.19a", [0.008, 0.12, 0.8, 0.044], decimals=4,
           mistakes={{"la p-valeur ajustée multiplie p par m, elle ne la divise pas": [0.0005, 0.0075, 0.05, 0.00275]}})
wbm.record("M08.19b", [1.0, 1.0], decimals=4,
           mistakes={{"une p-valeur ajustée reste une probabilité : plafonne-la à 1": [1.0, 1.4]}})
wbm.record("M08.19c", [122.6, 4 * math.log(120) + 114.6], decimals=4,
           mistakes={{"le BIC utilise le logarithme népérien, math.log": [122.6, 4 * math.log10(120) + 114.6],
                     "−2 ln L est positif quand ln L est négatif": [8 - 114.6, 4 * math.log(120) - 114.6],
                     "l'ordre demandé est (AIC, BIC)": [4 * math.log(120) + 114.6, 122.6]}})
wbm.record("M08.19d", "ValueError",
           mistakes={{"une p-valeur est entre 0 et 1 : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M08.19e", "ndarray",
           mistakes={{"la docstring demande un tableau NumPy : np.array(...)": {{"list", "tuple"}}}})''',
    after=tests_cells("test_bonferroni_ or test_aic_bic_"),
    note=r"a) $m = 4$ : $(0{,}008 ;\ 0{,}12 ;\ 0{,}8 ;\ 0{,}044)$ ; au risque de la famille de 5 %, le premier et le "
         r"quatrième test rejettent leur hypothèse nulle. b) $m\,p_i$ peut dépasser 1, qui n'est pas une probabilité : "
         r"on plafonne. c) AIC $= 8 + 114{,}6 = 122{,}6$ et BIC $= 4\ln 120 + 114{,}6 \approx 133{,}75$ : le BIC pénalise "
         r"chaque paramètre de $\ln 120 \approx 4{,}79$, l'AIC de 2 ; $\ln n > 2$ dès que $n \ge 8$.",
)

X_20, Y_20 = X_17, Y_17

M08_20 = Ex(
    "M08.20", "📦", 1, 15, "`scipy.stats.binomtest`, `permutation_test` et `ttest_rel` contre tes fonctions",
    "faire les mêmes tests avec `scipy.stats`, lire ce que renvoie chaque fonction, et comparer avec ta librairie.",
    "fiche §2, §3 et §5 ; Ex M08.16 à M08.18", tracks="C",
    body=r"""En pratique, on ne réécrit pas ces tests : `scipy.stats` (importé sous le nom `stats`) les fournit.
- `stats.binomtest(k, n, p=0.5, alternative="two-sided")` renvoie un résultat dont `.pvalue` est la p-valeur, et `.proportion_ci(confidence_level=0.95, method="wilson")` l'intervalle d'une proportion (attributs `.low` et `.high`) ;
- `stats.permutation_test((x, y), statistic, permutation_type="independent", alternative="greater", n_resamples=np.inf)` fait le test par permutation ; avec `n_resamples=np.inf`, il parcourt **toutes** les répartitions, et sa p-valeur est exacte ; la fonction `statistic(x, y, axis)` doit accepter un argument `axis` (par exemple `np.mean(x, axis=axis) - np.mean(y, axis=axis)`) ;
- `stats.ttest_rel(a, b)` fait le test de Student apparié : `.pvalue` est sa p-valeur bilatérale, et `.confidence_interval(0.95)` l'intervalle de M08.18.

Calcule avec ces fonctions :
- a) la p-valeur de `stats.binomtest(7, 30, p=0.1)` (4 décimales) ;
- b) l'intervalle de Wilson à 95 % de ce même résultat, `[low, high]` (4 décimales) ;
- c) la p-valeur exacte unilatérale du test par permutation de M08.17 a), pour les durées $x$ et $y$ (4 décimales) ;
- d) la p-valeur du test de Student apparié pour les temps de compilation $a$ et $b$ de M08.18 e) (4 décimales) ;
- e) vrai ou faux : pour chaque $k$ de 0 à 30, ta fonction `binomial_test(k, 30, 0.1)` donne la même p-valeur que `stats.binomtest(k, 30, 0.1)`, à $10^{-9}$ près (calcule-le avec une boucle) ;
- f) vrai ou faux : `stats.ttest_rel(a, b).confidence_interval(0.95)` et ta fonction `paired_difference_ci(a, b)` donnent le même intervalle, à $10^{-9}$ près.

Dans ta copie : c) est-il loin de la p-valeur de M08.17 a), estimée avec 1 999 permutations ? Que dit la p-valeur d), et est-elle cohérente avec l'intervalle de M08.18 e) (0 est-il dedans) ?""",
    todo='''answer_M08_20a = ...  # a) a number (4 decimals)
answer_M08_20b = ...  # b) a list [low, high] (4 decimals)
answer_M08_20c = ...  # c) a number (4 decimals)
answer_M08_20d = ...  # d) a number (4 decimals)
answer_M08_20e = ...  # e) True or False, computed with a loop
answer_M08_20f = ...  # f) True or False''',
    check='''for letter, answer in zip("abcdef", [answer_M08_20a, answer_M08_20b, answer_M08_20c, answer_M08_20d,
                                     answer_M08_20e, answer_M08_20f]):
    wbm.check(f"M08.20{letter}", answer)''',
    solution=f'''ref_20 = wbm.load_mymath("ref")
X_20, Y_20 = np.array({X_20}), np.array({Y_20})
A_20, B_20 = np.array({A_18}), np.array({B_18})
result_20 = stats.binomtest(7, 30, p=0.1)
answer_M08_20a = float(result_20.pvalue)
interval_20 = result_20.proportion_ci(confidence_level=0.95, method="wilson")
answer_M08_20b = [float(interval_20.low), float(interval_20.high)]


def difference_of_means(x, y, axis):
    return np.mean(x, axis=axis) - np.mean(y, axis=axis)


answer_M08_20c = float(stats.permutation_test((X_20, Y_20), difference_of_means, permutation_type="independent",
                                              alternative="greater", n_resamples=np.inf).pvalue)
answer_M08_20d = float(stats.ttest_rel(A_20, B_20).pvalue)
answer_M08_20e = all(abs(ref_20.testing.binomial_test(k, 30, 0.1) - stats.binomtest(k, 30, 0.1).pvalue) <= 1e-9
                     for k in range(31))
ci_20 = stats.ttest_rel(A_20, B_20).confidence_interval(0.95)
answer_M08_20f = bool(np.allclose([ci_20.low, ci_20.high], ref_20.testing.paired_difference_ci(A_20, B_20),
                                  rtol=0, atol=1e-9))
print(answer_M08_20a, answer_M08_20b, answer_M08_20c, answer_M08_20d, answer_M08_20e, answer_M08_20f)''',
    record='''wbm.record("M08.20a", stats.binomtest(7, 30, p=0.1).pvalue, decimals=4)
interval_record_20 = stats.binomtest(7, 30, p=0.1).proportion_ci(confidence_level=0.95, method="wilson")
wbm.record("M08.20b", [interval_record_20.low, interval_record_20.high], decimals=4,
           mistakes={"la question demande la méthode de Wilson : method=\\"wilson\\"":
                         [stats.binomtest(7, 30, p=0.1).proportion_ci(method="exact").low,
                          stats.binomtest(7, 30, p=0.1).proportion_ci(method="exact").high]})
wbm.record("M08.20c", 2 / 126, decimals=4,
           mistakes={"la question demande la p-valeur unilatérale : alternative=\\"greater\\"": 3 / 126})
wbm.record("M08.20d", stats.ttest_rel(np.array([12.4, 11.8, 13.1, 12.9, 12.2]),
                                      np.array([11.9, 11.6, 12.2, 12.5, 12.0])).pvalue, decimals=4,
           mistakes={"les mesures sont appariées : ttest_rel, pas ttest_ind":
                         stats.ttest_ind(np.array([12.4, 11.8, 13.1, 12.9, 12.2]),
                                         np.array([11.9, 11.6, 12.2, 12.5, 12.0])).pvalue})
wbm.record("M08.20e", True,
           mistakes={"relis ta fonction binomial_test (M08.16) : ses tests disent ce qui ne va pas": False})
wbm.record("M08.20f", True,
           mistakes={"relis ta fonction paired_difference_ci (M08.18) : ses tests disent ce qui ne va pas": False})''',
    note=r"a) $\approx 0{,}0258$ : 7 succès sur 30 sont rares si la probabilité vaut 0,1. b) $[0{,}1179 ;\ 0{,}4093]$, "
         r"le même intervalle que ta fonction `proportion_ci(7, 30)`. c) La p-valeur exacte vaut $\frac{2}{126} "
         r"\approx 0{,}0159$ ; M08.17 a) l'estimait à 0,019 avec 1 999 permutations. d) $\approx 0{,}0269$ : sous 0,05, "
         r"en accord avec l'intervalle à 95 % de M08.18 e), qui ne contient pas 0 (un intervalle de Student à 95 % "
         r"exclut 0 exactement quand la p-valeur bilatérale du test de Student est sous 0,05). e) et f) Ta librairie "
         r"et SciPy coïncident : SciPy définit la p-valeur bilatérale du test binomial comme la fiche (§2).",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M08.21 to M08.23)
# ---------------------------------------------------------------------------
M08_21_EXPERIMENT = '''rng_21 = np.random.default_rng(821)
n_21 = 20
z_h0 = rng_21.normal(0, 1, size=(1000, n_21)).mean(axis=1) * math.sqrt(n_21)        # H0 true: mean 0, σ = 1
p_h0 = 2 * stats.norm.sf(np.abs(z_h0))
z_h1 = rng_21.normal(0.5, 1, size=(1000, n_21)).mean(axis=1) * math.sqrt(n_21)      # H1 true: mean 0.5
p_h1 = 2 * stats.norm.sf(np.abs(z_h1))
p_by_k = np.array([stats.binomtest(k, 10).pvalue for k in range(11)])                # the 11 possible p-values
p_binomial = p_by_k[rng_21.binomial(10, 0.5, size=1000)]                            # H0 true: p = 1/2
exact_b = float(np.sum(stats.binom.pmf(np.flatnonzero(p_by_k <= 0.05), 10, 0.5)))
print(f"a) z-test, H0 true: share of p-values ≤ 0.05 = {np.mean(p_h0 <= 0.05):.3f}")
print(f"b) binomial test (n = 10), H0 true: share = {np.mean(p_binomial <= 0.05):.3f} (exact: {exact_b:.4f})")
print(f"c) z-test, H1 true (effect 0.5): share = {np.mean(p_h1 <= 0.05):.3f}")
fig, axes = plt.subplots(1, 2, figsize=(9, 3.2), sharey=True)
axes[0].hist(p_h0, bins=20, range=(0, 1), color="C0")
axes[0].set(title="H0 vraie", xlabel="p-valeur", ylabel="nombre de tests")
axes[1].hist(p_h1, bins=20, range=(0, 1), color="C3")
axes[1].set(title="H1 vraie (effet 0,5)", xlabel="p-valeur")
plt.show()'''

M08_21 = Ex(
    "M08.21", "🔮", 1, 10, "Prédire : sous H0, quelle part de 1 000 p-valeurs tombe sous 0,05 ?",
    "prévoir la loi des p-valeurs sous $H_0$ et sous $H_1$, pour un test continu et un test discret, puis la mesurer.",
    "fiche §1 et §4", tracks="C, E", hypothesis=True,
    body=r"""On répète 1 000 fois une expérience, et l'on calcule chaque fois la p-valeur d'un test. Choisis, pour chaque question :
- a) test $z$ bilatéral sur 20 mesures de loi $\mathcal{N}(\mu, 1)$, de $H_0 : \mu = 0$, quand $H_0$ est **vraie** : la part des p-valeurs au plus égales à 0,05 est (1) presque nulle ; (2) environ 0,05 ; (3) environ 0,5 ; (4) impossible à prévoir sans connaître les données ;
- b) test binomial exact bilatéral de $H_0 : p = \frac{1}{2}$ sur 10 essais, quand $H_0$ est **vraie** : la part des p-valeurs au plus égales à 0,05 est (1) environ 0,05 ; (2) nettement plus petite que 0,05 ; (3) nettement plus grande que 0,05 ;
- c) le test de a) quand $H_1$ est vraie, avec $\mu = 0{,}5$ : la part des p-valeurs au plus égales à 0,05 est (1) environ 0,05 ; (2) plus petite que 0,05 ; (3) nettement plus grande que 0,05 ;
- d) l'histogramme des 1 000 p-valeurs de a) est (1) à peu près plat ; (2) concentré près de 0 ; (3) en cloche autour de 0,5.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M08_21a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M08_21b = ...  # b) 1, 2 or 3
prediction_M08_21c = ...  # c) 1, 2 or 3
prediction_M08_21d = ...  # d) 1, 2 or 3''',
    check='''for letter, prediction in zip("abcd", [prediction_M08_21a, prediction_M08_21b, prediction_M08_21c,
                                      prediction_M08_21d]):
    wbm.check(f"M08.21{letter}", prediction)''',
    record='''wbm.record("M08.21a", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M08.21b", 2, prediction=True, choices=[1, 2, 3])
wbm.record("M08.21c", 3, prediction=True, choices=[1, 2, 3])
wbm.record("M08.21d", 1, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(M08_21_EXPERIMENT, ["prediction_M08_21a", "prediction_M08_21b", "prediction_M08_21c",
                                              "prediction_M08_21d"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", M08_21_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : relie a) et d) à la démonstration de M08.10. Pourquoi le test "
               "binomial sur 10 essais rejette-t-il moins souvent que 5 % sous $H_0$ (liste les issues qui font "
               "rejeter) ? Que mesure la part de c), et comment la faire grandir ?"),
    ],
    note=r"a) et d) Sous $H_0$, la p-valeur d'un test à statistique continue suit la loi uniforme sur $[0, 1]$ (M08.10) : "
         r"environ 5 % des p-valeurs tombent sous 0,05, et l'histogramme est plat, aux fluctuations près. b) Avec 10 "
         r"essais, seules les issues 0, 1, 9 et 10 donnent une p-valeur au plus égale à 0,05 : $P = \frac{2 \times "
         r"(1 + 10)}{1024} \approx 0{,}021$. Un test discret est **conservateur** : son risque de type I réel est plus "
         r"petit que le seuil. c) Sous $H_1$, la part des p-valeurs sous 0,05 est la **puissance** du test, environ "
         r"$\Phi(0{,}5\sqrt{20} - 1{,}96) \approx 0{,}61$ ; l'histogramme s'entasse près de 0. Elle grandit avec "
         r"l'effet et avec le nombre de mesures.",
)

M08_22_CHECK = '''with checked("M08.22a"):
    wbm.check("M08.22a", power(0, 10), computed=True)
with checked("M08.22b"):
    wbm.check("M08.22b", power(1.0, 10), computed=True)
with checked("M08.22c"):
    wbm.check("M08.22c", power(0.5, 20), computed=True)
with checked("M08.22d"):
    wbm.check("M08.22d", next((n for n in (5, 10, 20) if power(1.0, n) >= 0.8), None), computed=True)'''

M08_22_GRID = '''print("effect · measured power for n = 5, 10, 20 · power of the z-test, Φ(δ√(n/2) − 1.645)")
for effect in (0, 0.5, 1.0):
    measured = [power(effect, n) for n in (5, 10, 20)]
    theory = [NormalDist().cdf(effect * math.sqrt(n / 2) - NormalDist().inv_cdf(0.95)) for n in (5, 10, 20)]
    print(f"{effect:3.1f} · " + "  ".join(f"{m:.2f}" for m in measured) + " · "
          + "  ".join(f"{t:.2f}" for t in theory))'''

M08_22 = Ex(
    "M08.22", "🔬", 2, 25, "La puissance d'un test par permutation, selon l'effet et la taille des groupes",
    "mesurer par simulation la puissance d'un test par permutation, et la comparer à celle d'un test $z$.",
    "fiche §3 et §4 ; Ex M08.17", tracks="C",
    body=r"""La **puissance** d'un test est la probabilité qu'il rejette $H_0$ quand l'effet existe. Pour un test par permutation, elle n'a pas de formule : on la **mesure** par simulation. Écris `power(effect, n, n_sims=100, n_permutations=199, seed=0)`, qui suit exactement cette procédure :
1. `rng = np.random.default_rng(seed)`, un seul générateur ;
2. pour `sim` de 0 à `n_sims − 1` : `x = rng.normal(effect, 1, n)` puis `y = rng.normal(0, 1, n)` (dans cet ordre), puis `p = mymath.testing.permutation_test(x, y, n_permutations, alternative="greater", seed=sim)` ;
3. renvoie la proportion des `n_sims` p-valeurs au plus égales à 0,05, en `float`.

La vérification calcule (avec ta fonction `permutation_test` : écris d'abord M08.17) :
- a) `power(0, 10)` (2 décimales) ;
- b) `power(1.0, 10)` (2 décimales) ;
- c) `power(0.5, 20)` (2 décimales) ;
- d) parmi $n = 5$, 10 et 20, le plus petit nombre de mesures par groupe pour lequel `power(1.0, n)` atteint 0,8.

Une dernière cellule affiche la grille complète (effets 0 ; 0,5 ; 1 et $n$ = 5, 10, 20), à côté de la puissance du test $z$ unilatéral qui connaît $\sigma = 1$, $\Phi\big(\delta\sqrt{n/2} - z_{0{,}95}\big)$ : la différence de deux moyennes de $n$ mesures a l'écart-type $\sqrt{2/n}$.

Dans ta copie : que mesure a) ? Pourquoi ne vaut-il pas exactement 0,05 (pense à l'erreur type d'une proportion estimée sur 100 simulations) ? Comment la puissance évolue-t-elle avec l'effet, et avec $n$ ? Le test par permutation, qui ne suppose rien sur la loi des mesures, fait-il beaucoup moins bien que le test $z$ ?""",
    todo='''def power(effect, n, n_sims=100, n_permutations=199, seed=0):
    """The share of n_sims simulated permutation tests (alternative="greater") whose p-value is at most 0.05."""
    raise NotImplementedError("un générateur, une boucle de n_sims simulations, puis la proportion des p ≤ 0,05")''',
    check=M08_22_CHECK,
    solution='''def power(effect, n, n_sims=100, n_permutations=199, seed=0):
    """The share of n_sims simulated permutation tests (alternative="greater") whose p-value is at most 0.05."""
    rng = np.random.default_rng(seed)
    rejected = 0
    for sim in range(n_sims):
        x = rng.normal(effect, 1, n)
        y = rng.normal(0, 1, n)
        p = mymath.testing.permutation_test(x, y, n_permutations, alternative="greater", seed=sim)
        rejected += p <= 0.05
    return float(rejected / n_sims)


print("a)", power(0, 10), " b)", power(1.0, 10), " c)", power(0.5, 20))''',
    record='''wbm.record("M08.22a", power(0, 10), decimals=2)
wbm.record("M08.22b", power(1.0, 10), decimals=2,
           mistakes={"la puissance est la part des p-valeurs au plus égales à 0,05, pas au-dessus":
                         1 - power(1.0, 10)})
wbm.record("M08.22c", power(0.5, 20), decimals=2)
wbm.record("M08.22d", 20, choices=[5, 10, 20])''',
    after=[("md", "**La grille complète** (cette cellule utilise ta fonction)."),
           ("todo", 'with checked("M08.22 grille"):\n' + "\n".join("    " + line
                                                                   for line in M08_22_GRID.splitlines())),
           ("solution", M08_22_GRID)],
    note=r"a) Sans effet, la puissance mesurée est le **risque de type I** : environ 0,05. Sur 100 simulations, son "
         r"erreur type vaut $\sqrt{0{,}05 \times 0{,}95 / 100} \approx 0{,}022$ : 0,05 ou 0,08 sont aussi normaux "
         r"l'un que l'autre. b) et c) La puissance grandit avec l'effet et avec $n$ : environ 0,7 pour un effet de 1 avec "
         r"10 mesures par groupe, près de 0,95 avec 20. d) Il faut 20 mesures par groupe pour dépasser 0,8 avec un effet "
         r"de 1. La grille suit de près la puissance du test $z$, qui connaît pourtant $\sigma$ : le test par permutation "
         r"perd peu, et il ne suppose rien sur la loi des mesures.",
)

X_23, Y_23 = "[31, 27, 34, 29, 33]", "[26, 28, 25, 30, 24]"
X2_23, Y2_23 = "[4.2, 5.1, 3.8, 4.9]", "[3.9, 4.4, 3.1, 4.0, 3.6, 3.3]"

M08_23_CHECK = f'''with checked("M08.23 vérifications"):
    import matplotlib.colors as mcolors
    problems = []
    X2_23, Y2_23 = {X2_23}, {Y2_23}
    pooled_t = X2_23 + Y2_23
    observed_t = np.mean(X2_23) - np.mean(Y2_23)
    splits_t = [np.mean([pooled_t[i] for i in idx]) - np.mean([pooled_t[i] for i in range(10) if i not in idx])
                for idx in itertools.combinations(range(10), 4)]
    exact_t = sum(t >= observed_t - 1e-9 for t in splits_t) / len(splits_t)
    fig_t, ax_t = plt.subplots()
    returned_t = []
    try:
        created = drawn(lambda: returned_t.append(draw_null_distribution(ax_t, X2_23, Y2_23)))
    except BaseException:
        plt.close(fig_t)
        raise
    lines_t = [line for line in ax_t.get_lines()
               if len(set(np.round(np.asarray(line.get_xdata(), dtype=float), 9))) == 1]
    colors_t = {{mcolors.to_hex(patch.get_facecolor()) for patch in ax_t.patches
                if getattr(patch, "get_height", lambda: 0)() > 0}}
    plt.close(fig_t)
    if created:
        problems.append("draw_null_distribution ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans "
                        "l'axe reçu")
    elif not returned_t or returned_t[0] is None:
        problems.append("draw_null_distribution ne renvoie rien : il manque return (la p-valeur exacte)")
    elif not isinstance(returned_t[0], (int, float)) or abs(float(returned_t[0]) - exact_t) > 1e-9:
        problems.append(f"la p-valeur renvoyée, {{returned_t[0]}}, n'est pas la part des {{len(splits_t)}} "
                        "répartitions au moins aussi extrêmes que l'observation (t_perm ≥ t − 1e-9)")
    elif not any(abs(float(np.asarray(line.get_xdata(), dtype=float)[0]) - observed_t) < 1e-6 for line in lines_t):
        problems.append("aucune ligne verticale à l'écart observé : ax.axvline(t)")
    elif len(colors_t) < 2:
        problems.append("les répartitions au moins aussi extrêmes doivent avoir une autre couleur que les autres")
    if problems:
        print("❌ Ex M08.23 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M08.23 : la loi exacte, la ligne de l'écart observé et la p-valeur sont justes, sur un autre "
              "dataset.")'''

M08_23 = Ex(
    "M08.23", "🎨", 1, 15, "La loi de la statistique sous H0, et la p-valeur comme une aire",
    "tracer la loi exacte d'une statistique de permutation sous $H_0$, et y lire la p-valeur comme la part des "
    "répartitions au moins aussi extrêmes.", "fiche §1 et §3 ; R0 (matplotlib) ; R8 (combinaisons)", tracks="C",
    body=r"""Écris `draw_null_distribution(ax, x, y)`, qui, pour deux petits échantillons :
1. calcule l'écart observé $t = \bar{x} - \bar{y}$ et sa loi **exacte** sous $H_0$ : les valeurs de $t_{\text{perm}}$ pour **toutes** les répartitions des valeurs réunies (`x` puis `y`) en un groupe de `len(x)` valeurs et un groupe de `len(y)` valeurs (`itertools.combinations(range(len(pooled)), len(x))` donne les indices du premier groupe) ;
2. trace dans `ax` l'histogramme de ces valeurs, avec, d'une autre couleur, les répartitions au moins aussi extrêmes que l'observation ($t_{\text{perm}} \ge t - 10^{-9}$), et une ligne verticale à $t$ (`ax.axvline`) ;
3. renvoie la p-valeur exacte unilatérale : la part de ces répartitions au moins aussi extrêmes, en `float`.

La cellule de la figure s'en sert pour les durées (en minutes) d'un même trajet, fait cinq jours par un itinéraire, $x = (31, 27, 34, 29, 33)$, et cinq autres jours par un autre, $y = (26, 28, 25, 30, 24)$. Une cellule de vérification essaie ta fonction sur un autre dataset, dans un axe neuf (la figure elle-même se juge à l'œil).

Dans ta copie : combien y a-t-il de répartitions ? Que vaut la p-valeur, et à quelle partie de la figure correspond-elle ? Pourquoi la loi est-elle symétrique autour de 0 quand les deux groupes ont la même taille ?""",
    todo='''def draw_null_distribution(ax, x, y):
    """In ax, the histogram of mean(group 1) − mean(group 2) over every split of the pooled values, the splits at least
    as extreme as the observed difference in another color, and a vertical line at it; return the exact one-sided
    p-value (alternative "greater")."""
    raise NotImplementedError("itertools.combinations pour les répartitions, puis deux ax.hist et ax.axvline")''',
    check=f'''with checked("M08.23 figure"):
    fig, ax = plt.subplots(figsize=(7, 3.6))
    try:
        result_23 = []
        created = drawn(lambda: result_23.append(draw_null_distribution(ax, {X_23}, {Y_23})))
    except BaseException:
        plt.close(fig)                                     # no empty figure while the function is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M08.23 : draw_null_distribution ouvre sa propre figure : dessine dans l'axe reçu.")
    else:
        ax.set(xlabel="écart des moyennes (minutes)", ylabel="nombre de répartitions",
               title=f"Loi exacte sous H0 : p-valeur = {{result_23[0]}}")
        plt.show()''',
    solution=f'''def draw_null_distribution(ax, x, y):
    """In ax, the histogram of mean(group 1) − mean(group 2) over every split of the pooled values, the splits at least
    as extreme as the observed difference in another color, and a vertical line at it; return the exact one-sided
    p-value (alternative "greater")."""
    pooled = np.concatenate([np.asarray(x, dtype=float), np.asarray(y, dtype=float)])
    m = len(x)
    observed = pooled[:m].mean() - pooled[m:].mean()
    values = []
    for idx in itertools.combinations(range(len(pooled)), m):
        mask = np.zeros(len(pooled), dtype=bool)
        mask[list(idx)] = True
        values.append(pooled[mask].mean() - pooled[~mask].mean())
    values = np.array(values)
    extreme = values >= observed - 1e-9
    bins = np.linspace(values.min() - 0.1, values.max() + 0.1, 30)
    ax.hist(values[~extreme], bins=bins, color="C0", label="les autres répartitions")
    ax.hist(values[extreme], bins=bins, color="C3", label="au moins aussi extrêmes")
    ax.axvline(observed, color="black", lw=1.5)
    ax.legend(fontsize=8)
    return float(np.mean(extreme))


fig, ax = plt.subplots(figsize=(7, 3.6))
p_23 = draw_null_distribution(ax, {X_23}, {Y_23})
ax.set(xlabel="écart des moyennes (minutes)", ylabel="nombre de répartitions",
       title=f"Loi exacte sous H0 : p-valeur = {{p_23:.4f}}")
plt.show()''',
    after=[("md", "**Vérifications automatiques** (sur un autre dataset, dans un axe neuf)."),
           ("code", M08_23_CHECK)],
    note=r"Il y a $\binom{10}{5} = 252$ répartitions. L'écart observé vaut $30{,}8 - 26{,}6 = 4{,}2$ minutes, et 7 "
         r"répartitions sur 252 font au moins aussi bien : $p = \frac{7}{252} = \frac{1}{36} \approx 0{,}028$, la part "
         r"des barres rouges dans l'histogramme. Avec deux groupes de même taille, échanger les deux groupes change $t$ "
         r"en $-t$ : chaque valeur a sa symétrique, et la loi est symétrique autour de 0.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M08.24 to M08.26)
# ---------------------------------------------------------------------------
M08_24_MISTAKES = bug_letters_mistakes(
    "ACE", "BDF",
    {"A": "refais chaque calcul de p-valeur par permutation sur un petit exemple",
     "C": "refais chaque correction de Bonferroni sur un petit exemple",
     "E": "refais chaque p-valeur bilatérale sur un petit exemple"},
    name_correct=False)

M08_24 = Ex(
    "M08.24", "🐛", 1, 15, "Chasse à l'erreur : une p-valeur nulle, un test unilatéral choisi après coup, "
    "Bonferroni à l'envers",
    "repérer dans du code les erreurs classiques sur les p-valeurs, puis calculer les bonnes valeurs.",
    "fiche §2, §3, §5 et §6", tracks="C",
    body=r"""Un collègue a écrit six lignes, chacune avec un commentaire qui dit ce qu'elle doit calculer. Trois lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter de code**, trouve-les.

```python
B, C = 999, 0                                       # random permutations, and draws at least as extreme as observed
p_perm = C / B                                      # (A) the p-value of this permutation test
p_tail = sum(math.comb(18, j) for j in range(14, 19)) / 2 ** 18    # (B) P(K ≥ 14) for K of law B(18, 1/2)
p_values = [0.004, 0.02, 0.3]                       # the p-values of a family of three tests
adjusted = min(p_values) / len(p_values)            # (C) the Bonferroni-adjusted p-value of the smallest one
z_975 = NormalDist().inv_cdf(0.975)                 # (D) the quantile of a two-sided 95 % interval
p_two = 1 - NormalDist().cdf(abs(-1.8))             # (E) the two-sided p-value of z = −1.8 (H1 two-sided, set in advance)
half = z_975 * math.sqrt(0.3 * 0.7 / 50)            # (F) the half-width of Wald's 95 % interval, p̂ = 0.3, n = 50
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire (une liste de 6 nombres, 3 décimales).

Dans ta copie : pour chaque ligne fausse, quelle erreur a été faite, et comment la corriger ? Pourquoi l'erreur (E) revient-elle à choisir un test unilatéral **après** avoir vu le signe de $z$, et que vaut alors le vrai risque de type I d'une règle « rejeter si cette valeur est sous 0,05 » ?""",
    todo='''answer_M08_24a = ...  # a) letters, as text
answer_M08_24b = ...  # b) a list of 6 values (3 decimals)''',
    check='''wbm.check("M08.24a", answer_M08_24a)
wbm.check("M08.24b", answer_M08_24b)''',
    solution='''answer_M08_24a = "ACE"
B, C = 999, 0
p_perm = (C + 1) / (B + 1)                          # (A) never 0: the observed split counts as a draw
p_tail = sum(math.comb(18, j) for j in range(14, 19)) / 2 ** 18    # (B) correct
p_values = [0.004, 0.02, 0.3]
adjusted = min(1, min(p_values) * len(p_values))    # (C) multiply by m, do not divide
z_975 = NormalDist().inv_cdf(0.975)                 # (D) correct
p_two = 2 * (1 - NormalDist().cdf(abs(-1.8)))       # (E) count both tails
half = z_975 * math.sqrt(0.3 * 0.7 / 50)            # (F) correct
answer_M08_24b = [p_perm, p_tail, adjusted, z_975, p_two, half]
print(answer_M08_24a, [round(value, 4) for value in answer_M08_24b])''',
    record=f'''wbm.record("M08.24a", "ACE",
           mistakes={M08_24_MISTAKES})
VALUES_24 = [1 / 1000, 4048 / 2 ** 18, 0.012, NormalDist().inv_cdf(0.975), 2 * (1 - NormalDist().cdf(1.8)),
             NormalDist().inv_cdf(0.975) * math.sqrt(0.21 / 50)]
wbm.record("M08.24b", VALUES_24, decimals=3,
           mistakes={{"(A) : la p-valeur d'un test par permutation tiré au hasard n'est jamais nulle":
                         [0] + VALUES_24[1:],
                     "(C) : la p-valeur ajustée multiplie p par m":
                         VALUES_24[:2] + [0.004 / 3] + VALUES_24[3:],
                     "(E) : une p-valeur bilatérale compte les deux côtés":
                         VALUES_24[:4] + [1 - NormalDist().cdf(1.8)] + VALUES_24[5:]}})''',
    note=r"(A) Avec $C = 0$, la ligne annonce une p-valeur nulle ; la bonne est $\frac{C + 1}{B + 1} = 0{,}001$. (B) est "
         r"juste : $\frac{3060 + 816 + 153 + 18 + 1}{2^{18}} = \frac{4048}{262\,144} \approx 0{,}015$. (C) divise au "
         r"lieu de multiplier : la p-valeur ajustée vaut $\min(1, 3 \times 0{,}004) = 0{,}012$. (D) est juste, 1,960. (E) "
         r"ne compte qu'un côté : la p-valeur bilatérale vaut $2\big(1 - \Phi(1{,}8)\big) \approx 0{,}072$, pas 0,036. "
         r"Prendre toujours le côté où tombe $z$, c'est choisir le test unilatéral après coup : la règle « rejeter si "
         r"$1 - \Phi(|z|) \le 0{,}05$ » rejette quand $|z| \ge 1{,}645$, avec un risque de type I réel de 10 %, le double "
         r"du seuil annoncé. (F) est juste : $1{,}96\sqrt{0{,}21/50} \approx 0{,}127$.",
)

M08_25_GIVEN = '''def z_test_p_values(samples):
    """Two-sided p-values of the z-test of H0: mean = 0 (σ = 1 known), one per row of samples."""
    samples = np.asarray(samples, dtype=float)
    z = samples.mean(axis=1) * math.sqrt(samples.shape[1])
    return 2 * stats.norm.sf(np.abs(z))


def z_test_copy_1(samples):            # a copy with a bug
    samples = np.asarray(samples, dtype=float)
    z = samples.mean(axis=1) * math.sqrt(samples.shape[1])
    return stats.norm.sf(np.abs(z))


def z_test_copy_2(samples):            # a copy with another bug
    samples = np.asarray(samples, dtype=float)
    z = samples.mean(axis=1) / math.sqrt(samples.shape[1])
    return 2 * stats.norm.sf(np.abs(z))'''

M08_25_CHECK = '''with checked("M08.25 vérifications"):
    problems = []
    if K_SE is ...:
        raise NotImplementedError("choisis K_SE, le nombre d'erreurs types que ton test tolère")
    if isinstance(K_SE, bool) or not isinstance(K_SE, (int, float)):
        raise TypeError(f"K_SE doit être un nombre, pas {type(K_SE).__name__}")
    seen = []

    def spy(samples):                                   # records the first value of the samples it receives
        seen.append(float(np.asarray(samples)[0, 0]))
        return z_test_p_values(samples)

    def outcome(function, seed):
        """None if assert_calibrated passes, else the message of its AssertionError."""
        try:
            assert_calibrated(function, seed)
        except AssertionError as exc:
            return str(exc)
        return None

    outcome(spy, 7)
    if not seen or seen[0] != float(np.random.default_rng(7).normal(0, 1, size=(4000, 20))[0, 0]):
        problems.append("assert_calibrated doit tirer samples = np.random.default_rng(seed).normal(0, 1, size=(n_sims, "
                        "n)) avec la graine reçue : un test doit être reproductible")
    else:
        passed = sum(outcome(z_test_p_values, seed) is None for seed in range(30))
        messages_1 = [outcome(z_test_copy_1, seed) for seed in range(30)]
        messages_2 = [outcome(z_test_copy_2, seed) for seed in range(30)]
        caught_1 = sum(message is not None for message in messages_1)
        caught_2 = sum(message is not None for message in messages_2)
        print(f"K_SE = {K_SE} : la bonne fonction passe ton test {passed} fois sur 30 ; la copie 1 est attrapée "
              f"{caught_1} fois sur 30, la copie 2 {caught_2} fois sur 30")
        if passed < 30:
            problems.append("ton test échoue sur la bonne fonction pour certaines graines : la tolérance est trop "
                            "étroite (un test qui échoue sans bug est « instable », flaky)")
        if caught_1 < 30:
            problems.append("ton test laisse passer la copie 1 : la tolérance est trop large")
        if caught_2 < 30:
            problems.append("ton test laisse passer la copie 2 : un test peut aussi se tromper en rejetant trop "
                            "rarement ; regarde l'écart à alpha dans les deux sens")
        if not problems and any(not message.strip() for message in messages_1 + messages_2):
            problems.append("ajoute un message à ton assert (assert condition, message) : il dit ce qui était attendu "
                            "et ce qui a été obtenu")
        if not problems and not 3.5 <= K_SE <= 7:
            problems.append("ces 30 graines passent, mais ce K_SE serait instable ou trop large sur des milliers de "
                            "lancements : relis l'énoncé pour le choisir")
        if not problems:
            try:
                test_z_test_is_calibrated()
            except AssertionError as exc:
                problems.append(f"test_z_test_is_calibrated échoue sur la bonne fonction : {exc}")
    if problems:
        print("❌ Ex M08.25 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M08.25 : ton test accepte la bonne fonction et attrape les deux copies fausses, pour 30 graines.")'''

M08_25 = Ex(
    "M08.25", "🛠️", 1, 15, "Tester un test : un pytest qui vérifie l'uniformité des p-valeurs sous H0",
    "écrire le test automatique d'un test statistique : sous $H_0$, la part des p-valeurs sous le seuil doit être "
    "proche du seuil, à une tolérance comptée en erreurs types.", "fiche §1 et §4 ; Ex M08.21 ; M02c (Ex M02c.27)",
    tracks="C",
    body=r"""Comment vérifier qu'un test est **bien calibré**, c'est-à-dire que, sous $H_0$, il rejette au seuil de 5 % dans 5 % des cas ? Par simulation (M08.10 et M08.21) : on tire beaucoup d'échantillons sous $H_0$, on calcule leurs p-valeurs, et la part des p-valeurs au plus égales à 0,05 doit être proche de 0,05. Proche à combien près ? Comme en M02c.27 : à $k$ erreurs types près, avec l'erreur type d'une proportion, $\sqrt{\frac{\alpha(1 - \alpha)}{N}}$ pour $N$ simulations.

La cellule fournie définit `z_test_p_values(samples)`, les p-valeurs bilatérales du test $z$ de $H_0$ : « la moyenne vaut 0 » ($\sigma = 1$ connu), une par ligne de `samples`, et deux copies fausses. Écris :
- `K_SE` : le nombre d'erreurs types que ton test tolère. Un vrai projet lance ses tests des milliers de fois : la bonne fonction ne doit presque jamais échouer ; mais une copie qui rejette deux fois trop souvent, ou presque jamais, s'écarte de 0,05 d'une quinzaine d'erreurs types, et doit être attrapée à coup sûr ;
- `assert_calibrated(p_value_function, seed, n_sims=4000, n=20, alpha=0.05)` : tire `samples = np.random.default_rng(seed).normal(0, 1, size=(n_sims, n))` ($H_0$ vraie), calcule `p = p_value_function(samples)`, et **lève une `AssertionError`** (`assert condition, message`) si la part des p-valeurs au plus égales à `alpha` s'écarte de `alpha` de plus de `K_SE` erreurs types ; le message dit ce qui était attendu, puis ce qui a été obtenu ;
- `test_z_test_is_calibrated()` : le test au format pytest, sans argument, qui appelle `assert_calibrated` sur `z_test_p_values` avec une graine fixe. Dans un fichier `tests/test_….py`, pytest trouverait cette fonction et la lancerait tout seul.

La vérification lance `assert_calibrated` sur la bonne fonction et sur les deux copies fausses, pour 30 graines : la bonne doit passer **toutes** les fois, les fausses doivent échouer **toutes** les fois.

Dans ta copie : quel `K_SE` as-tu choisi, et pourquoi ? Quelle erreur chacune des deux copies fait-elle, et dans quel sens se trompe-t-elle ? Une troisième copie, qui renverrait `1 - p`, passerait ton test : pourquoi (que vaut la loi de $1 - P$ quand $P$ est uniforme sur $[0, 1]$) ? Que faudrait-il vérifier en plus pour l'attraper ?""",
    given=M08_25_GIVEN,
    todo='''K_SE = ...   # your choice: the number of standard errors your test tolerates


def assert_calibrated(p_value_function, seed, n_sims=4000, n=20, alpha=0.05):
    """Raise an AssertionError unless, under H0, the share of p-values <= alpha is within K_SE standard errors of alpha."""
    raise NotImplementedError("tire les échantillons sous H0, calcule la part des p ≤ alpha, puis assert ..., message")


def test_z_test_is_calibrated():
    """The pytest test: assert_calibrated on z_test_p_values, with a fixed seed."""
    raise NotImplementedError("un appel à assert_calibrated, avec une graine fixe")''',
    solution='''K_SE = 5      # 2 (1 − Φ(5)) ≈ 6e-7: never flaky in practice; a copy 10 standard errors away is always caught


def assert_calibrated(p_value_function, seed, n_sims=4000, n=20, alpha=0.05):
    """Raise an AssertionError unless, under H0, the share of p-values <= alpha is within K_SE standard errors of alpha."""
    samples = np.random.default_rng(seed).normal(0, 1, size=(n_sims, n))
    share = float(np.mean(np.asarray(p_value_function(samples)) <= alpha))
    standard_error = math.sqrt(alpha * (1 - alpha) / n_sims)
    assert abs(share - alpha) <= K_SE * standard_error, (
        f"expected a share of p-values <= {alpha} within {K_SE} standard errors ({K_SE * standard_error:.4f}) of "
        f"{alpha} under H0, got {share:.4f}")


def test_z_test_is_calibrated():
    """The pytest test: assert_calibrated on z_test_p_values, with a fixed seed."""
    assert_calibrated(z_test_p_values, seed=2025)


for name, function in [("z_test_p_values", z_test_p_values), ("copy 1", z_test_copy_1), ("copy 2", z_test_copy_2)]:
    share = np.mean(function(np.random.default_rng(0).normal(0, 1, size=(4000, 20))) <= 0.05)
    print(f"{name}: share of p-values <= 0.05 under H0 = {share:.4f}")''',
    after=[("code", M08_25_CHECK)],
    note=r"L'erreur type vaut $\sqrt{0{,}05 \times 0{,}95 / 4000} \approx 0{,}0034$. Un $K_{SE}$ entre 4 et 6 convient : "
         r"la bonne fonction échoue avec la probabilité $2\big(1 - \Phi(K_{SE})\big)$, $6 \times 10^{-5}$ pour 4 et "
         r"$6 \times 10^{-7}$ pour 5. La copie 1 oublie le facteur 2 : elle renvoie la p-valeur unilatérale du côté "
         r"observé, et rejette dans 10 % des cas (l'erreur (E) de M08.24) ; elle se trompe dans le sens dangereux, celui "
         r"des faux positifs. La copie 2 divise la moyenne par $\sqrt{n}$ au lieu de la multiplier : $z$ est 20 fois trop "
         r"petit, et le test ne rejette presque jamais ; il ne donne pas de faux positifs, mais il n'a plus de "
         r"puissance. Les deux s'écartent de 0,05 d'environ 14 erreurs types, dans un sens ou dans l'autre : il faut "
         r"comparer l'écart **en valeur absolue**. La copie `1 - p` passerait : si $P$ est uniforme, $1 - P$ l'est "
         r"aussi. Elle ne se trahit que sous $H_1$, où elle ne rejette presque jamais : un test complet vérifie aussi la "
         r"puissance sur un cas où l'effet existe.",
)

M08_26_GIVEN = '''def make_dataset(seed, n_true, n=200, p=50):
    """X (n × p), y and the sorted indices of the n_true features related to y (the other features are noise)."""
    rng = np.random.default_rng(seed)
    X = np.round(rng.normal(size=(n, p)), 3)
    true = np.sort(rng.choice(p, size=n_true, replace=False))
    coef = rng.uniform(0.95, 1.2, size=n_true) * rng.choice([-1, 1], size=n_true)
    y = X[:, true] @ coef + rng.normal(0, math.sqrt(6.25 - np.sum(coef ** 2)), size=n)
    return X, np.round(y, 3), true


X_26, y_26, _ = make_dataset(826, 3)          # three true features, whose indices stay hidden'''

M08_26_CASES = "[(826, 3), (21, 2), (22, 4), (23, 1), (24, 3)]"

M08_26_CHECK = f'''with checked("M08.26 défi"):
    import time
    problems, results_26, ok_26, slowest = [], [], False, 0.0
    for seed_t, n_true_t in {M08_26_CASES}:
        X_t, y_t, true_t = make_dataset(seed_t, n_true_t)
        start_t = time.perf_counter()
        try:
            chosen_t = select_features(X_t.copy(), y_t.copy())
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"select_features lève {{type(exc).__name__}} ({{exc}})")
            break
        slowest = max(slowest, time.perf_counter() - start_t)
        if chosen_t is None:
            problems.append("select_features ne renvoie rien : il manque return")
            break
        chosen_t = {{int(j) for j in np.asarray(chosen_t, dtype=int).ravel()}}
        results_26.append((len(set(true_t.tolist()) - chosen_t), len(chosen_t - set(true_t.tolist()))))
    if not problems:
        print("par dataset (vraies features manquées, faux positifs) :", results_26)
        if any(missed > 0 for missed, _ in results_26):
            problems.append("des vraies features manquent : ta règle est trop sévère")
        if any(false > 1 for _, false in results_26):
            problems.append("plus d'un faux positif sur un dataset : ta règle est trop permissive")
        if slowest > 10:
            problems.append(f"objectif atteint, mais en {{slowest:.1f}} s pour un dataset (objectif : 10 s)")
    if problems:
        print("❌ Ex M08.26 : " + " ; ".join(problems) + ".")
    else:
        ok_26 = True
        print("✅ Ex M08.26 : défi réussi : toutes les vraies features, et au plus un faux positif, sur les cinq datasets.")
with checked("M08.26"):
    select_features(X_26, y_26)                       # ⏳ while the function is not written
    wbm.check("M08.26", bool(ok_26), computed=True)'''

M08_26 = Ex(
    "M08.26", "🏆", 3, 25, "Défi : retrouver les trois vraies features parmi cinquante, avec au plus un faux positif",
    "choisir une règle de décision pour 50 tests à la fois, qui trouve les vraies features sans se laisser piéger par "
    "le bruit.", "fiche §6 ; Ex M08.7, M08.11 et M08.19", tracks="C",
    body=r"""Un dataset a 200 exemples et 50 features ; quelques-unes seulement sont liées à la cible $y$, les autres sont du bruit. Écris `select_features(X, y)`, qui renvoie la liste des indices des features que tu déclares liées à la cible.

**L'objectif** : sur `X_26, y_26`, qui a trois vraies features, et sur quatre autres datasets du même type, dont le nombre de vraies features (de 1 à 4) n'est pas donné à ta fonction, retrouver **toutes** les vraies features, avec **au plus un** faux positif par dataset, en moins de 10 secondes par dataset.

Une piste : un test par feature (la p-valeur de la corrélation de $x_j$ avec $y$, `stats.pearsonr(X[:, j], y).pvalue`), puis une règle de décision. Laquelle ? Ce chapitre a tout ce qu'il faut.

La vérification essaie ta fonction sur les cinq datasets ; une dernière cellule enregistre si l'objectif est atteint sur les cinq.

Dans ta copie : combien de features la règle « $p \le 0{,}05$ » déclare-t-elle liées sur `X_26`, et combien de faux positifs attendais-tu (M08.7) ? Pourquoi « garder les trois plus fortes corrélations » n'est-il pas une bonne règle ? Explique ta règle : que garantit-elle, et quel risque prend-elle ?""",
    given=M08_26_GIVEN,
    todo='''def select_features(X, y):
    """The list of the indices of the features of X that you declare related to y."""
    raise NotImplementedError("une p-valeur par feature, puis une règle de décision")''',
    check=M08_26_CHECK,
    solution=f'''def select_features(X, y, alpha=0.05):
    """The indices of the features whose correlation with y stays significant after Bonferroni's correction."""
    X, y = np.asarray(X, dtype=float), np.asarray(y, dtype=float)
    p_values = [stats.pearsonr(X[:, j], y).pvalue for j in range(X.shape[1])]
    adjusted = mymath.testing.bonferroni(p_values)
    return [int(j) for j in np.flatnonzero(adjusted <= alpha)]


def naive_rule(X, y):
    return [j for j in range(X.shape[1]) if stats.pearsonr(X[:, j], y).pvalue <= 0.05]


def top_three(X, y):
    correlations = np.abs([np.corrcoef(X[:, j], y)[0, 1] for j in range(X.shape[1])])
    return sorted(int(j) for j in np.argsort(correlations)[-3:])


for seed_t, n_true_t in {M08_26_CASES}:
    X_t, y_t, true_t = make_dataset(seed_t, n_true_t)
    print(f"true {{true_t.tolist()}} · Bonferroni {{select_features(X_t, y_t)}} · p ≤ 0.05 {{naive_rule(X_t, y_t)}}"
          f" · top three {{top_three(X_t, y_t)}}")''',
    after=[("solution", M08_26_CHECK.split('with checked("M08.26"):')[0].rstrip())],
    record='''wbm.record("M08.26", True,
           mistakes={"l'objectif n'est pas atteint sur les cinq datasets : la cellule du défi dit pourquoi":
                         False})''',
    note=r"La règle « $p \le 0{,}05$ » trouve les vraies features, mais aussi des faux positifs : sur 47 features de "
         r"bruit, on en attend $47 \times 0{,}05 \approx 2{,}4$ (sept sur l'un des datasets). Garder les trois plus fortes "
         r"corrélations suppose de connaître le nombre de vraies features : elle en manque une sur le dataset qui en a "
         r"quatre, et ajoute des faux positifs sur ceux qui en ont une ou deux. La correction de Bonferroni (rejeter "
         r"quand $50\,p_j \le 0{,}05$) garantit que la probabilité d'au moins un faux positif reste sous 5 %, quelle que "
         r"soit la dépendance entre les tests (M08.11) ; son risque est de manquer une vraie feature faible, ce qui "
         r"n'arrive pas ici : la plus faible a une corrélation d'environ 0,35, et son test a une p-valeur ajustée "
         r"bien plus petite que 0,05.",
)


PART_A = Part("A", "Ta librairie : test binomial, test par permutation, intervalles, Bonferroni, AIC et BIC ; SciPy",
              "Fiche §2 à §7. Les six fonctions de `mymath/testing.py`, puis les mêmes tests avec `scipy.stats`.",
              given=TOOLS, exercises=[M08_16, M08_17, M08_18, M08_19, M08_20])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §1, §3 et §4. La loi des p-valeurs sous $H_0$ et sous $H_1$, la puissance d'un test par "
              "permutation, la loi exacte d'une statistique.",
              exercises=[M08_21, M08_22, M08_23])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §1 à §6. Trois erreurs à trouver, le test automatique d'un test, puis une sélection de features "
              "parmi cinquante.",
              exercises=[M08_24, M08_25, M08_26])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M08.1 à M08.9, M08.13 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M08 · Tests statistiques — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m08_tests/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M08`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M08 · Tests statistiques — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : test binomial exact, test par permutation exhaustif, "
               "risques et puissance, taille d'échantillon, intervalles de Wald, de Wilson et de Student, comparaisons "
               "multiples, AIC et BIC, facteur de Bayes, importance par permutation.\n"
               "- Écrire les six fonctions de `mymath/testing.py` et les tester, puis comparer avec `scipy.stats`.\n"
               "- Prédire la loi des p-valeurs, mesurer une puissance, tracer une loi nulle exacte, chasser des "
               "erreurs, tester un test, choisir des features parmi cinquante.\n\n"
               r"**Rappel express.** p-valeur = $P_{H_0}(\text{statistique au moins aussi extrême que l'observation})$ ; "
               r"risque de type I $\alpha$ = $P_{H_0}(\text{rejeter})$, puissance $1 - \beta$ = $P_{H_1}(\text{rejeter})$ ; "
               r"$n = \Big(\frac{(z_{1-\alpha} + z_{1-\beta})\,\sigma}{\delta}\Big)^2$ ; permutation : "
               r"$\frac{C + 1}{B + 1}$ ; Wald $\hat{p} \pm z\sqrt{\hat{p}(1 - \hat{p})/n}$ ; Student apparié "
               r"$\bar{d} \pm t_{n-1}\,s_d/\sqrt{n}$ ; Bonferroni $\min(1, m\,p_i)$ ; AIC $= 2k - 2\ln L$, "
               r"BIC $= k\ln n - 2\ln L$ ; $\mathrm{BF}_{12} = \frac{p(\mathcal{D} \mid M_1)}{p(\mathcal{D} \mid M_2)}$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu poser $H_0$ et $H_1$, et dire ce qu'une p-valeur mesure et ce qu'elle ne mesure pas ?\n"
               "2. Sais-tu calculer la p-valeur exacte d'un test binomial et celle d'un petit test par permutation ?\n"
               "3. Sais-tu calculer un risque de type I, une puissance, et le nombre d'observations nécessaire ?\n"
               "4. Sais-tu calculer les intervalles de Wald, de Wilson et de Student apparié, et dire quand Wald "
               "échoue ?\n"
               "5. Sais-tu corriger des comparaisons multiples par Bonferroni, et comparer deux modèles par l'AIC, le "
               "BIC et un facteur de Bayes ?\n\n"
               "**La suite** : le chapitre 8 de workbookIA (entraînement et test : jeu de test, validation croisée, "
               "comparer deux modèles), puis M09a, les matrices et les systèmes linéaires.")]


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
