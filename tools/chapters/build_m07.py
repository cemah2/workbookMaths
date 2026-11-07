#!/usr/bin/env python
"""Build the two notebooks of chapter M07 from a single source (used by Claude).

    python tools/chapters/build_m07.py
    python tools/run_all_notebooks.py chapitres/m07_vecteurs_rn/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m07_vecteurs_rn/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M07.1 to M07.13, 🔗 M07.19); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it. The vectors and
points are new: none is a test case of tests/test_m07_vectors.py, an example of the fiche, or an example of
workbookIA 0B and 7 (no x = (3, 4), no a = (3, 1) and b = (1, 2), no penguins, no eggs, no centroids (1, 1) and
(3, 5) with x = (6, 0), no a = (1, 2) and b = (3, 4), no a = (3, −1, 2) and b = (1, 2, 0), no k-means on the points
(1, 1), (2, 1), (1, 3), (5, 4), (6, 5), (7, 4) nor on 0, 2, 3, 9, 11, 12, no k-means++ on 0, 1, 5, 9, no silhouette of
{0, 1, 2} and {6, 7}, no μ0 = (1, 2) and μ1 = (5, 4), no density n / bᵈ, no ball in a cube, no hyper-orange, no
nearest-neighbour distance study), nor of R9 (no u = (3, −1), v = (−2, 4), w = (−6, 2), no projection of (1, 3) on
(4, 2), no line 2x − y − 3 = 0).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M07"
FOLDER = "chapitres/m07_vecteurs_rn"

F = 'kind="fraction", simplified=True'
ROOT_L2 = "la norme L2 est la racine de la somme des carrés : n'oublie pas la racine"
SQUARED = "la question demande le carré de la norme : sans racine"
UNIT_L2 = "divise par la norme L2 (la racine de la somme des carrés), pas par la norme L1"
SCORE = "le score w · x + b n'est pas une distance : divise-le par ‖w‖"
DEGREES = "la question demande des degrés : arccos donne des radians, à convertir (× 180/π)"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M07.1", "Combinaisons linéaires et vecteurs one-hot dans ℝ⁴", [
        ("a", "a list of 4 integers", "[4, -1, -1, 6]",
         '''mistakes={"additionne coordonnée par coordonnée : la question demande u + v, pas u − v": [-2, -3, 1, 2]}'''),
        ("b", "a list of 4 integers", "[-7, -7, 3, 2]",
         '''mistakes={"3v se retranche : 2u − 3v, coordonnée par coordonnée": [11, -1, -3, 14]}'''),
        ("c", "a list of 4 integers", "[-2, -1, 6, 1]",
         '''mistakes={"w s'ajoute : u − v + w": [-2, -5, -4, 3]}'''),
        ("d", "the list [a, b]", "[2, 1]",
         '''mistakes={"a multiplie u et b multiplie v : l'ordre est [a, b]": [1, 2]}'''),
        ("e", "a list of 4 integers", "[0, 0, 1, 0]",
         '''mistakes={"l'ordre des modes est (vélo, bus, métro, marche) : le métro est le troisième": [0, 0, 0, 1], '''
         '''"le métro est le troisième mode de la liste (vélo, bus, métro, marche)": [0, 1, 0, 0]}'''),
        ("f", "a list of 4 integers", "[4, 3, 0, 3]"),
        ("g", "a list of 4 numbers", "[0.4, 0.3, 0, 0.3]",
         '''decimals=2, mistakes={"divise chaque coordonnée par le nombre de trajets": [4, 3, 0, 3]}'''),
    ]),

    Paper("M07.2", "Produits scalaires, ‖u + v‖² et l'identité du parallélogramme", [
        ("a", "an integer", "3",
         '''mistakes={"attention aux signes : (−2) × 1 est négatif": 7}'''),
        ("b", "an integer", "9", f'''mistakes={{"{SQUARED}": 3}}'''),
        ("c", "an integer", "12", ""),
        ("d", "an integer", "27",
         '''mistakes={"le double produit 2 u · v manque : ‖u + v‖² = ‖u‖² + 2 u · v + ‖v‖²": 21, '''
         '''"le produit croisé compte deux fois : 2 u · v, pas u · v": 24}'''),
        ("e", "an irreducible fraction", '"-1/4"',
         f'''{F}, mistakes={{"(u + t v) · v = u · v + t v · v : isole t, avec son signe": "1/4", '''
         '''"la condition porte sur v : c'est v · v qui apparaît, pas u · u": "-1/3"}'''),
        ("f", "an integer", "8",
         '''mistakes={"la différence ‖a + b‖² − ‖a − b‖² vaut 4 a · b : divise par 4": 32, '''
         '''"divise par 4, pas par 2": 16, "la somme donne 2‖a‖² + 2‖b‖² ; pour a · b, fais la différence": 34}'''),
        ("g", "True or False", "False"),
    ]),

    Paper("M07.3", "Normes L1, L2, L∞ et distances entre trois profils", [
        ("a", "a list of 3 numbers", "[5, 3, 2]",
         f'''mistakes={{"{ROOT_L2}": [5, 9, 2], "l'ordre demandé est [L1, L2, L∞]": [2, 3, 5]}}'''),
        ("b", "a list of 3 numbers", "[4, 2, 1]", f'''mistakes={{"{ROOT_L2}": [4, 4, 1]}}'''),
        ("c", "a number (3 decimals)", "7 ** 0.5", f'''decimals=3, mistakes={{"{ROOT_L2}": 7}}'''),
        ("d", '"Q" or "R"', '"Q"'),
        ("e", '"Q" or "R"', '"R"'),
        ("f", "a list (4 decimals)", "[1 / 3, -2 / 3, 2 / 3, 0]",
         f'''decimals=4, mistakes={{"{UNIT_L2}": [0.2, -0.4, 0.4, 0]}}'''),
        ("g", "a number (3 decimals)", "2 + 7 ** 0.5",
         '''decimals=3, mistakes={"c'est le membre de gauche, d₂(P, Q) ; la question demande d₂(P, R) + d₂(R, Q)": 3}'''),
    ]),

    Paper("M07.4", "Similarité cosinus entre des profils d'écoute musicale", [
        ("a", "an integer", "6", f'''mistakes={{"{ROOT_L2}": 36}}'''),
        ("b", "an irreducible fraction", '"8/15"', F),
        ("c", "a number (2 decimals)", "math.degrees(math.acos(8 / 15))", "decimals=2"),
        ("d", "a number (4 decimals)", "29 ** 0.5", f'''decimals=4, mistakes={{"{ROOT_L2}": 29}}'''),
        ("e", "a number", "1"),
        ("f", "a number", "6", f'''mistakes={{"{ROOT_L2}": 36, "un cosinus de 1 dit que les directions sont les mêmes, pas les longueurs : calcule E − A": 0}}'''),
        ("g", '"C" or "E"', '"C"'),
        ("h", '"C" or "E"', '"E"'),
    ]),

    Paper("M07.5", "Projeter sur une droite : composante parallèle et composante orthogonale", [
        ("a", "an integer", "18"),
        ("b", "a number", "2",
         '''mistakes={"divise par u · u = ‖u‖², pas par ‖u‖": 6}'''),
        ("c", "a list of 4 numbers", "[4, 0, 2, 4]",
         '''mistakes={"le coefficient divise x · u par u · u = ‖u‖², pas par ‖u‖": [12, 0, 6, 12], '''
         '''"multiplie u par le coefficient (x · u)/(u · u), pas par x · u": [36, 0, 18, 36]}'''),
        ("d", "a list of 4 numbers", "[1, -1, 0, -1]",
         '''mistakes={"le reste est r = x − p, pas p − x": [-1, 1, 0, 1]}'''),
        ("e", "a number", "0"),
        ("f", "a number", "39", ""),
        ("g", "a list of 4 numbers", "[4, 0, 2, 4]",
         '''mistakes={"la projection ne dépend que de la droite : la longueur du vecteur directeur ne compte pas": '''
         '''[-12, 0, -6, -12], "la projection ne dépend que de la droite : le sens du vecteur directeur ne compte '''
         '''pas": [-4, 0, -2, -4]}'''),
        ("h", "a number", "6",
         '''mistakes={"la composante divise x · u par ‖u‖, pas par ‖u‖² : c'est une longueur": 2}'''),
    ]),

    Paper("M07.6", "Un plan de ℝ³ : vecteur normal, côté, distance signée", [
        ("a", "a list of 3 integers", "[2, -1, 2]",
         '''mistakes={"le vecteur normal est fait des coefficients de x, y et z, avec leurs signes": [2, 1, 2]}'''),
        ("b", "True or False", "True"),
        ("c", "1, -1 or 0", "1", '''choices=[1, -1, 0]'''),
        ("d", "a number", "1", f'''mistakes={{"{SCORE}": 3}}'''),
        ("e", "an irreducible fraction", '"-5/3"',
         f'''{F}, mistakes={{"la distance signée garde le signe de w · x + b, négatif ici": "5/3", '''
         f'''"{SCORE}": "-5"}}'''),
        ("f", "a number", "3",
         f'''mistakes={{"une distance est positive : prends la valeur absolue": -3, "{SCORE}": {{9, -9}}}}'''),
        ("g", "a list (4 decimals)", "[7 / 3, 1 / 3, 1 / 3]",
         '''decimals=4, mistakes={"le score de B est positif : B recule le long de w, on retire (score/‖w‖²) w": '''
         '''[11 / 3, -1 / 3, 5 / 3], "divise le score par ‖w‖² = w · w, pas par ‖w‖": [1, 1, -1], '''
         '''"divise le score par ‖w‖² avant de multiplier w": [-3, 3, -5]}'''),
        ("h", "an integer", "-8",
         '''mistakes={"le plan passe par B quand 2x − y + 2z + b′ = 0 en B : b′ = −(2x − y + 2z)": 8}'''),
    ]),

    Paper("M07.7", "Un score linéaire w · x + b : calculer, décider, lire le vecteur normal", [
        ("a", "a number", "-0.5",
         '''decimals=3, mistakes={"le biais s'ajoute au produit scalaire : z = w · x + b": 1.5}'''),
        ("b", "a number", "2.5",
         '''decimals=3, mistakes={"le biais s'ajoute au produit scalaire : z = w · x + b": 4.5}'''),
        ("c", "1 or 0", "0", '''choices=[1, 0]'''),
        ("d", "a number", "0"),
        ("e", "a number", "1",
         '''mistakes={"multiplie le poids des vibrations par la variation, 0,5": 2}'''),
        ("f", "a list (3 decimals)", "[1.5 / 6.5 ** 0.5, 2 / 6.5 ** 0.5, -0.5 / 6.5 ** 0.5]",
         '''decimals=3, mistakes={"divise w par sa norme : la question demande un vecteur unitaire": [1.5, 2, -0.5]}'''),
        ("g", "a number (4 decimals)", "2.5 / 6.5 ** 0.5",
         f'''decimals=4, mistakes={{"{SCORE}": 2.5, "‖w‖ est la racine de la somme des carrés des poids": 2.5 / 6.5}}'''),
    ]),

    Paper("M07.8", "Centroïde, inertie et formule de König-Huygens", [
        ("a", "a list of 2 numbers", "[2, 1]"),
        ("b", "a number", "20", ""),
        ("c", "a number", "45"),
        ("d", "a number", "60",
         '''mistakes={"le terme de König-Huygens est m ‖x̄ − c‖² : multiplie par le nombre de points": 28}'''),
        ("e", "a number", "4",
         '''mistakes={"divise par le nombre de points, 5": 5}'''),
        ("f", "a list of 2 numbers", "[3, 2]"),
        ("g", "a number", "80",
         '''mistakes={"les cinq anciens points ne sont plus centrés sur le nouveau barycentre : ajoute 5 ‖x̄ − x̄′‖²": 70, '''
         '''"le sixième point compte aussi : ajoute le carré de sa distance au nouveau barycentre": 30}'''),
    ]),

    Paper("M07.9", "Où placer un dépôt : le barycentre pondéré des livraisons", [
        ("a", "an integer", "6"),
        ("b", "a list (4 decimals)", "[5 / 3, 4 / 3]",
         '''decimals=4, mistakes={"pondère chaque magasin par son nombre de livraisons": [8 / 3, 4 / 3]}'''),
        ("c", "an irreducible fraction", '"146/3"', F),
        ("d", "an irreducible fraction", '"164/3"',
         f'''{F}, mistakes={{"le terme de König-Huygens se multiplie par la somme des poids": "149/3"}}'''),
        ("e", "True or False", "False"),
    ]),

    Paper("M07.10", "La silhouette d'un point, à la main, en dimension 2", [
        ("a", "a number (4 decimals)", "(2 + 5 ** 0.5) / 2",
         '''decimals=4, mistakes={"a(i) ne compte pas le point lui-même : moyenne sur les autres points": '''
         '''(2 + 5 ** 0.5) / 3}'''),
        ("b", "a number (4 decimals)", "(37 ** 0.5 + 58 ** 0.5) / 2", "decimals=4"),
        ("c", "a number (3 decimals)", "S10_A",
         '''decimals=3, mistakes={"divise par le plus grand des deux nombres, max(a, b)": (B10_A - A10_A) / A10_A, '''
         '''"c'est b − a sur max(a, b), pas a − b": -S10_A}'''),
        ("d", "a number (3 decimals)", "S10_D", "decimals=3"),
        ("e", "a number (3 decimals)", "S10_B",
         '''decimals=3, mistakes={"B est maintenant plus loin des points de son cluster que de ceux de l'autre : le '''
         '''signe de b − a le dit": -S10_B}'''),
        ("f", "a number", "0"),
    ]),

    Paper("M07.11", "k-means++ : des probabilités de tirage proportionnelles à D²", [
        ("a", "a list of 5 integers", "[0, 1, 9, 20, 50]",
         '''mistakes={"k-means++ utilise les carrés des distances, sans racine": [0, 1, 3, 20 ** 0.5, 50 ** 0.5]}'''),
        ("b", "an irreducible fraction", '"5/8"',
         f'''{F}, mistakes={{"le tirage n'est pas uniforme : la probabilité est proportionnelle à D²": "1/4"}}'''),
        ("c", "an irreducible fraction", '"1/80"', F),
        ("d", "a list of 5 integers", "[0, 1, 9, 10, 0]",
         '''mistakes={"D est la distance au centre choisi le plus proche : compare chaque point aux deux centres": '''
         '''[0, 1, 9, 20, 0]}'''),
        ("e", "an irreducible fraction", '"1/2"',
         f'''{F}, mistakes={{"D est la distance au centre le plus proche, P1 ou P5": "2/9"}}'''),
        ("f", "an irreducible fraction", '"1/4"',
         f'''{F}, mistakes={{"P1 est déjà choisi : il reste quatre points": "1/5"}}'''),
    ]),

    Paper("M07.12", "La diagonale du cube unité et son angle avec les axes, quand d grandit", [
        ("a", "a number", "2", f'''mistakes={{"{ROOT_L2}": 4}}'''),
        ("b", "a number (4 decimals)", "50 ** 0.5", f'''decimals=4, mistakes={{"{ROOT_L2}": 50}}'''),
        ("c", "a number", "60", '''mistakes={"cos θ = 1/√d : en dimension 4, 1/2": 45}'''),
        ("d", "a number (2 decimals)", "math.degrees(math.acos(0.1))", "decimals=2"),
        ("e", "an integer", "34",
         '''mistakes={"en dimension 33, l'angle reste juste sous 80° : vérifie l'entier suivant": 33}'''),
        ("f", "an irreducible fraction", '"4/5"',
         f'''{F}, mistakes={{"le dernier produit vaut 1 × (−1) = −1 : le produit scalaire vaut (d − 1) − 1": "9/10", "compter −1 comme +1 rendrait les deux vecteurs égaux : le dernier produit vaut 1 × (−1)": "1"}}'''),
    ]),

    Paper("M07.13", "La distance au carré moyenne de deux points tirés dans le cube [0, 1]ᵈ", [
        ("a", "an irreducible fraction", '"1/3"',
         f'''{F}, mistakes={{"E[U²] n'est pas E[U]² : intègre x² sur [0, 1]": "1/4"}}'''),
        ("b", "an irreducible fraction", '"1/4"', F),
        ("c", "an irreducible fraction", '"1/6"',
         f'''{F}, mistakes={{"1/12 est la variance de U ; développe (U − V)² : E[U²] − 2 E[UV] + E[V²]": "1/12", "le double produit −2 E[UV] manque : (U − V)² = U² − 2UV + V²": "2/3", '''
         '''"c'est E[U − V]² ; la question demande E[(U − V)²]": "0"}'''),
        ("d", "a number", "2"),
        ("e", "a number", "10"),
        ("f", "a number (3 decimals)", "1 / 6 ** 0.5", "decimals=3"),
    ]),

    Paper("M07.19", "Pont : changer l'unité d'une feature change le plus proche voisin", [
        ("a", "a number (2 decimals)", "(10 ** 2 + 0.7 ** 2) ** 0.5", "decimals=2"),
        ("b", "a number (2 decimals)", "(30 ** 2 + 0.05 ** 2) ** 0.5", "decimals=2"),
        ("c", '"A" or "B"', '"A"'),
        ("d", '"A" or "B"', '"B"'),
        ("e", "a list of 2 numbers (3 decimals)", "[(0.5 ** 2 + 2.8 ** 2) ** 0.5, (1.5 ** 2 + 0.2 ** 2) ** 0.5]",
         '''decimals=3, mistakes={"divise chaque écart par l'écart-type de sa feature avant de l'élever au carré": '''
         '''[(10 ** 2 / 20 + 0.7 ** 2 / 0.25) ** 0.5, (30 ** 2 / 20 + 0.05 ** 2 / 0.25) ** 0.5]}'''),
        ("f", '"A" or "B"', '"B"'),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math

import numpy as np

P10 = np.array([(0, 0), (2, 0), (1, 2), (6, 1), (7, 3)], dtype=float)      # M07.10: A, B, C, D, F


def silhouette_10(labels, i):
    """s(i), a(i), b(i) for the points P10 with the given cluster labels."""
    labels = np.array(labels)
    d = np.sqrt(((P10 - P10[i]) ** 2).sum(axis=1))
    same = labels == labels[i]
    same[i] = False
    a = d[same].mean()
    b = min(d[labels == k].mean() for k in set(labels.tolist()) if k != labels[i])
    return (b - a) / max(a, b), a, b


S10_A, A10_A, B10_A = silhouette_10([1, 1, 1, 2, 2], 0)
S10_D = silhouette_10([1, 1, 1, 2, 2], 3)[0]
S10_B = silhouette_10([1, 2, 1, 2, 2], 1)[0]'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M07.1 à M07.13, 🔗 M07.19)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"7/9\"` ;\n"
               "- une liste `[-1.5, 2.5, 0]` (un vecteur, un point, une liste de valeurs), `True` / `False`, ou une "
               "lettre entre guillemets, `\"K\"`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M07.24 to M07.28)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance as spd

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

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M07")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/vectors.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "Un vecteur est une liste ou un tableau NumPy à une dimension ; un ensemble de points, un tableau à deux "
         "dimensions, un point par ligne. NumPy suffit (sommes, `np.abs`, `np.sqrt`) ; `np.linalg.norm` et "
         "`scipy.spatial` sont interdits : les tests comparent tes résultats aux leurs, et un test vérifie que tu ne "
         "t'en sers pas. Les nombres renvoyés sont des `float` de Python, les vecteurs des tableaux NumPy.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of vectors.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_vectors_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m07_vectors.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m07_vectors.py", "{keyword}", impl="ref")')]


ZERO_DIVISION = "un vecteur nul n'a pas de direction : lève une ValueError avant de diviser par sa norme"

M07_24 = Ex(
    "M07.24", "🔨", 1, 20, "Normes Lp et similarité cosinus · `norm_p, cosine_similarity`",
    "programmer les normes $L^p$, L∞ comprise, et la similarité cosinus, en refusant les cas où elles n'ont pas de "
    "sens.", "fiche §3 et §4", tracks="C, E", mymath="vectors.py",
    body=HOWTO + """

Écris (fiche §3 et §4) :
- `norm_p(x, p=2)` : $\\big(\\sum_i |x_i|^p\\big)^{1/p}$, et $\\max_i |x_i|$ pour `p = float("inf")` ; une `ValueError` si `x` est vide ou si $p < 1$ (la formule n'est alors pas une norme) ;
- `cosine_similarity(u, v)` : $\\frac{\\mathbf{u} \\cdot \\mathbf{v}}{\\lVert \\mathbf{u} \\rVert\\,\\lVert \\mathbf{v} \\rVert}$, ramené dans $[-1, 1]$ par `np.clip` (un arrondi peut donner 1,0000000000000002) ; une `ValueError` si les longueurs diffèrent ou si un vecteur est nul.

La vérification calcule, pour $\\mathbf{x} = (1, -2, 2, -4)$ :
- a) `norm_p(x, 1)` ;
- b) `norm_p(x)` ;
- c) `norm_p(x, float("inf"))` ;
- d) `norm_p(x, 3)` (3 décimales) ;
- e) le nom de l'erreur levée par `norm_p([1, 2], 0.5)` ;

puis :
- f) `cosine_similarity([1, 2, 0, -1], [2, 1, 1, 0])` (4 décimales) ;
- g) le nom de l'erreur levée par `cosine_similarity([0, 0, 0], [1, 2, 3])` ;
- h) le nom du type de `norm_p(np.array([1.5, 2.0]), 3)`, en texte.

Dans ta copie : calcule a) à d) et f) à la main. Pourquoi la norme diminue-t-elle de a) à c) quand $p$ augmente ? Et pourquoi faut-il `np.clip` (essaie `cosine_similarity` d'un vecteur avec lui-même, sans lui) ?""",
    todo=LOAD_LEARNER,
    check='''X_24 = [1, -2, 2, -4]
with checked("M07.24a"):
    wbm.check("M07.24a", mymath.vectors.norm_p(X_24, 1), computed=True)
with checked("M07.24b"):
    wbm.check("M07.24b", mymath.vectors.norm_p(X_24), computed=True)
with checked("M07.24c"):
    wbm.check("M07.24c", mymath.vectors.norm_p(X_24, float("inf")), computed=True)
with checked("M07.24d"):
    wbm.check("M07.24d", mymath.vectors.norm_p(X_24, 3), computed=True)
with checked("M07.24e"):
    wbm.check("M07.24e", raised(mymath.vectors.norm_p, [1, 2], 0.5), computed=True)
with checked("M07.24f"):
    wbm.check("M07.24f", mymath.vectors.cosine_similarity([1, 2, 0, -1], [2, 1, 1, 0]), computed=True)
with checked("M07.24g"):
    wbm.check("M07.24g", raised(mymath.vectors.cosine_similarity, [0, 0, 0], [1, 2, 3]), computed=True)
with checked("M07.24h"):
    wbm.check("M07.24h", type(mymath.vectors.norm_p(np.array([1.5, 2.0]), 3)).__name__, computed=True)''',
    solution=LOAD_REF + '''
norm_p, cosine = mymath.vectors.norm_p, mymath.vectors.cosine_similarity
X_24 = [1, -2, 2, -4]
print("a)", norm_p(X_24, 1), " b)", norm_p(X_24), " c)", norm_p(X_24, float("inf")), " d)", norm_p(X_24, 3))
print("e)", raised(norm_p, [1, 2], 0.5), " f)", cosine([1, 2, 0, -1], [2, 1, 1, 0]),
      " g)", raised(cosine, [0, 0, 0], [1, 2, 3]), " h)", type(norm_p(np.array([1.5, 2.0]), 3)).__name__)''',
    record=f'''wbm.record("M07.24a", 9.0, decimals=6,
           mistakes={{"la norme L1 additionne les valeurs absolues : les signes ne comptent pas": -3.0}})
wbm.record("M07.24b", 5.0, decimals=6,
           mistakes={{"{ROOT_L2}": 25.0}})
wbm.record("M07.24c", 4.0, decimals=6,
           mistakes={{"la norme L∞ est le plus grand des |x_i|, pas le plus grand des x_i": 2.0}})
wbm.record("M07.24d", 81 ** (1 / 3), decimals=3,
           mistakes={{"prends les valeurs absolues avant la puissance p : avec des signes, une puissance impaire "
                      "change tout": abs(1 - 8 + 8 - 64) ** (1 / 3), "la puissance finale est 1/p": 81.0}})
wbm.record("M07.24e", "ValueError",
           mistakes={{"p < 1 ne définit pas une norme : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M07.24f", 4 / 6, decimals=4,
           mistakes={{"divise le produit scalaire par le produit des deux normes": 4.0,
                     "divise par le produit des deux normes, pas par le carré d'une seule": 4 / 36}})
wbm.record("M07.24g", "ValueError",
           mistakes={{"{ZERO_DIVISION}": {{"aucune", "ZeroDivisionError"}},
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "ZeroDivisionError")}}})
wbm.record("M07.24h", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy": "float64"}})''',
    after=tests_cells("test_norm_p_ or test_cosine_similarity_"),
    note="a) $1 + 2 + 2 + 4 = 9$. b) $\\sqrt{1 + 4 + 4 + 16} = 5$. c) $\\max |x_i| = 4$. d) $(1 + 8 + 8 + 64)^{1/3} = "
         "81^{1/3} \\approx 4{,}3267$. La norme diminue quand $p$ augmente : la plus grande coordonnée pèse de plus en "
         "plus, jusqu'à rester seule (L∞). f) $\\frac{2 + 2 + 0 + 0}{\\sqrt{6}\\sqrt{6}} = \\frac{4}{6} \\approx 0{,}6667$. "
         "Sans `np.clip`, le cosinus d'un vecteur avec lui-même peut valoir 1,0000000000000002 à cause des arrondis, et "
         "`math.acos` lève alors une erreur.",
)

M07_25 = Ex(
    "M07.25", "🔨", 1, 15, "La projection sur une droite · `project_onto_line`",
    "programmer la projection orthogonale sur une droite dirigée par un vecteur quelconque, et vérifier que le reste "
    "est orthogonal.", "fiche §4 ; Ex M07.24", tracks="C, E", mymath="vectors.py",
    body="""Écris `project_onto_line(x, u)` (fiche §4) : $\\frac{\\mathbf{x} \\cdot \\mathbf{u}}{\\mathbf{u} \\cdot \\mathbf{u}}\\,\\mathbf{u}$, en tableau NumPy ; une `ValueError` si les longueurs diffèrent ou si $\\mathbf{u}$ est nul. Le vecteur $\\mathbf{u}$ n'a pas besoin d'être unitaire.

La vérification calcule :
- a) `project_onto_line([3, -1, 2], [1, 1, 1])` (une liste, 4 décimales) ;
- b) le produit scalaire du reste $\\mathbf{x} - \\mathbf{p}$ de a) avec $\\mathbf{u} = (1, 1, 1)$ (4 décimales) ;
- c) `project_onto_line([2, 5], [0, -3])` (une liste) ;
- d) `project_onto_line([4, 1, 0, -2], [2, 0, 0, 0])` (une liste) ;
- e) le nom de l'erreur levée par `project_onto_line([1, 2], [0, 0])` ;
- f) le nom du type de `project_onto_line([1, 2], [1, 1])`, en texte.

Dans ta copie : calcule a), c) et d) à la main. Que fait la projection sur un axe (regarde c) et d)) ? Pourquoi le signe de $\\mathbf{u} = (0, -3)$ ne change-t-il rien en c) ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M07.25a"):
    wbm.check("M07.25a", np.asarray(mymath.vectors.project_onto_line([3, -1, 2], [1, 1, 1])).tolist(),
              computed=True)
with checked("M07.25b"):
    p_25 = np.asarray(mymath.vectors.project_onto_line([3, -1, 2], [1, 1, 1]), dtype=float)
    wbm.check("M07.25b", float((np.array([3, -1, 2]) - p_25) @ np.array([1, 1, 1])), computed=True)
with checked("M07.25c"):
    wbm.check("M07.25c", np.asarray(mymath.vectors.project_onto_line([2, 5], [0, -3])).tolist(), computed=True)
with checked("M07.25d"):
    wbm.check("M07.25d", np.asarray(mymath.vectors.project_onto_line([4, 1, 0, -2], [2, 0, 0, 0])).tolist(),
              computed=True)
with checked("M07.25e"):
    wbm.check("M07.25e", raised(mymath.vectors.project_onto_line, [1, 2], [0, 0]), computed=True)
with checked("M07.25f"):
    wbm.check("M07.25f", type(mymath.vectors.project_onto_line([1, 2], [1, 1])).__name__, computed=True)''',
    solution=LOAD_REF + '''
proj = mymath.vectors.project_onto_line
p_25 = proj([3, -1, 2], [1, 1, 1])
print("a)", p_25, " b)", (np.array([3, -1, 2]) - p_25) @ np.array([1, 1, 1]), " c)", proj([2, 5], [0, -3]),
      " d)", proj([4, 1, 0, -2], [2, 0, 0, 0]))
print("e)", raised(proj, [1, 2], [0, 0]), " f)", type(proj([1, 2], [1, 1])).__name__)''',
    record=f'''wbm.record("M07.25a", [4 / 3, 4 / 3, 4 / 3], decimals=4,
           mistakes={{"divise par u · u = ‖u‖², pas par ‖u‖": [4 / 3 ** 0.5] * 3,
                     "divise x · u par u · u avant de multiplier u": [4.0, 4.0, 4.0]}})
wbm.record("M07.25b", 0.0, decimals=4)
wbm.record("M07.25c", [0.0, 5.0], decimals=6,
           mistakes={{"divise par u · u = 9 : le coefficient est (x · u)/(u · u)": [0.0, 45.0],
                     "divise par u · u = ‖u‖², pas par ‖u‖": [0.0, 15.0]}})
wbm.record("M07.25d", [4.0, 0.0, 0.0, 0.0], decimals=6,
           mistakes={{"divise par u · u = ‖u‖², pas par ‖u‖": [8.0, 0.0, 0.0, 0.0]}})
wbm.record("M07.25e", "ValueError",
           mistakes={{"un vecteur u nul ne donne aucune droite : lève une ValueError avant de diviser":
                         {{"aucune", "ZeroDivisionError"}},
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "ZeroDivisionError")}}})
wbm.record("M07.25f", "ndarray",
           mistakes={{"la docstring demande un tableau NumPy : np.array(...)": {{"list", "tuple"}}}})''',
    after=tests_cells("test_project_onto_line_"),
    note="a) $\\mathbf{x} \\cdot \\mathbf{u} = 3 - 1 + 2 = 4$ et $\\mathbf{u} \\cdot \\mathbf{u} = 3$ : $\\mathbf{p} = "
         "\\frac{4}{3}(1, 1, 1)$. b) Le reste $\\big(\\frac{5}{3}, -\\frac{7}{3}, \\frac{2}{3}\\big)$ est orthogonal à "
         "$\\mathbf{u}$ : $\\frac{5 - 7 + 2}{3} = 0$. c) $\\frac{-15}{9}(0, -3) = (0, 5)$ : projeter sur un axe garde la "
         "coordonnée de cet axe et annule les autres, quel que soit le sens du vecteur directeur. d) De même, $(4, 0, 0, 0)$.",
)

POINTS_26 = "[[1, 4], [3, 0], [-1, 2], [5, 6]]"

M07_26 = Ex(
    "M07.26", "🔨", 1, 20, "Barycentre et somme des carrés des distances · `centroid, sum_sq_distances_to`",
    "programmer le barycentre, pondéré ou non, et l'inertie d'un nuage autour d'un point, et vérifier la formule de "
    "König-Huygens.", "fiche §6", tracks="C, E", mymath="vectors.py",
    body=f"""Écris (fiche §6) :
- `centroid(points, weights=None)` : la moyenne des lignes de `points`, ou $\\frac{{\\sum_i \\omega_i \\mathbf{{x}}_i}}{{\\sum_i \\omega_i}}$ avec des poids ; une `ValueError` si `points` est vide, ou si les poids n'ont pas la bonne longueur, ont une valeur négative ou une somme nulle ;
- `sum_sq_distances_to(points, c)` : $\\sum_i \\lVert \\mathbf{{x}}_i - \\mathbf{{c}} \\rVert^2$, en `float` ; une `ValueError` si `c` n'a pas une coordonnée par colonne.

La vérification calcule, pour les quatre points `{POINTS_26}` :
- a) `centroid(points)` (une liste) ;
- b) `centroid(points, weights=[1, 1, 2, 0])` (une liste) ;
- c) `sum_sq_distances_to(points, centroid(points))` ;
- d) `sum_sq_distances_to(points, [0, 0])` ;
- e) le nom de l'erreur levée par `centroid(points, weights=[1, -1, 1, 1])` ;
- f) le nom du type de `sum_sq_distances_to(points, [0, 0])`, en texte.

Dans ta copie : calcule a) à d) à la main, et vérifie d) avec la formule de König-Huygens. Pourquoi le dernier point ne compte-t-il pas en b) ?""",
    todo=LOAD_LEARNER,
    check=f'''POINTS_26 = {POINTS_26}
with checked("M07.26a"):
    wbm.check("M07.26a", np.asarray(mymath.vectors.centroid(POINTS_26)).tolist(), computed=True)
with checked("M07.26b"):
    wbm.check("M07.26b", np.asarray(mymath.vectors.centroid(POINTS_26, weights=[1, 1, 2, 0])).tolist(),
              computed=True)
with checked("M07.26c"):
    wbm.check("M07.26c", mymath.vectors.sum_sq_distances_to(POINTS_26, mymath.vectors.centroid(POINTS_26)),
              computed=True)
with checked("M07.26d"):
    wbm.check("M07.26d", mymath.vectors.sum_sq_distances_to(POINTS_26, [0, 0]), computed=True)
with checked("M07.26e"):
    wbm.check("M07.26e", raised(mymath.vectors.centroid, POINTS_26, weights=[1, -1, 1, 1]), computed=True)
with checked("M07.26f"):
    wbm.check("M07.26f", type(mymath.vectors.sum_sq_distances_to(POINTS_26, [0, 0])).__name__, computed=True)''',
    solution=LOAD_REF + f'''
centroid, inertia = mymath.vectors.centroid, mymath.vectors.sum_sq_distances_to
POINTS_26 = {POINTS_26}
print("a)", centroid(POINTS_26), " b)", centroid(POINTS_26, weights=[1, 1, 2, 0]),
      " c)", inertia(POINTS_26, centroid(POINTS_26)), " d)", inertia(POINTS_26, [0, 0]))
print("e)", raised(centroid, POINTS_26, weights=[1, -1, 1, 1]), " f)", type(inertia(POINTS_26, [0, 0])).__name__)''',
    record=f'''wbm.record("M07.26a", [2.0, 3.0], decimals=6)
wbm.record("M07.26b", [0.5, 2.0], decimals=6,
           mistakes={{"multiplie chaque point par son poids avant d'additionner": [2.0, 3.0]}})
wbm.record("M07.26c", 40.0, decimals=6,
           mistakes={{"additionne les carrés des distances, sans racine": float(sum(np.sqrt([2, 10, 10, 18])))}})
wbm.record("M07.26d", 92.0, decimals=6)
wbm.record("M07.26e", "ValueError",
           mistakes={{"un poids négatif est refusé : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M07.26f", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy": "float64"}})''',
    after=tests_cells("test_centroid_ or test_sum_sq_distances_to_"),
    note="a) $\\big(\\frac{1 + 3 - 1 + 5}{4}, \\frac{4 + 0 + 2 + 6}{4}\\big) = (2, 3)$. b) $\\frac{(1, 4) + (3, 0) + 2(-1, 2) "
         "+ 0 \\times (5, 6)}{4} = (0{,}5 ;\\ 2)$ : un poids nul retire le point. c) $2 + 10 + 10 + 18 = 40$. d) $17 + 9 + "
         "5 + 61 = 92$, et König-Huygens donne $40 + 4 \\times \\lVert (2, 3) \\rVert^2 = 40 + 52 = 92$.",
)

W_27, B_27, X_27 = "[1, -2, 2]", "1", "[[1, 1, 1], [0, 0, 0], [-3, 0, 0], [2, 3, 0]]"

M07_27 = Ex(
    "M07.27", "🔨", 1, 20, "Côté d'un hyperplan et distance à un hyperplan · "
    "`side_of_hyperplane, distance_to_hyperplane`",
    "programmer le côté d'un hyperplan et la distance, signée ou non, pour un point ou pour toutes les lignes d'un "
    "tableau.", "fiche §5 ; Ex M07.24", tracks="C, E", mymath="vectors.py",
    body=f"""Écris (fiche §5) :
- `side_of_hyperplane(x, w, b)` : le signe de $\\mathbf{{w}} \\cdot \\mathbf{{x}} + b$ (1, −1 ou 0), en `int` de Python pour un point (`x` à une dimension), en tableau d'entiers pour plusieurs points (une ligne par point) ;
- `distance_to_hyperplane(x, w, b, signed=False)` : $\\frac{{|\\mathbf{{w}} \\cdot \\mathbf{{x}} + b|}}{{\\lVert \\mathbf{{w}} \\rVert}}$, sans la valeur absolue si `signed=True` ; un `float` pour un point, un tableau pour plusieurs ;
- dans les deux cas, une `ValueError` si $\\mathbf{{w}}$ est nul ou si sa longueur ne correspond pas aux points.

Pour un tableau `X` (un point par ligne), `np.sum(X * w, axis=1)` donne tous les produits scalaires d'un coup (le broadcasting de 0A), et `np.sum(x * w, axis=-1)` marche pour un point comme pour un tableau.

La vérification prend l'hyperplan $x_1 - 2x_2 + 2x_3 + 1 = 0$ (`w = {W_27}`, `b = {B_27}`) et les points `X = {X_27}`, et calcule :
- a) `side_of_hyperplane(X, w, b)` (une liste) ;
- b) `distance_to_hyperplane(X, w, b)` (une liste, 4 décimales) ;
- c) `distance_to_hyperplane(X, w, b, signed=True)` (une liste, 4 décimales) ;
- d) le nom du type de `side_of_hyperplane([1, 1, 1], w, b)`, en texte ;
- e) `distance_to_hyperplane([1, 1, 1], w, b)` (4 décimales) ;
- f) le nom de l'erreur levée par `distance_to_hyperplane([1, 2], [0, 0], 1)`.

Dans ta copie : calcule a) et b) à la main. À quelle distance de l'origine passe l'hyperplan, et de quel côté est l'origine ?""",
    todo=LOAD_LEARNER,
    check=f'''W_27, B_27, X_27 = {W_27}, {B_27}, {X_27}
with checked("M07.27a"):
    wbm.check("M07.27a", np.asarray(mymath.vectors.side_of_hyperplane(X_27, W_27, B_27)).tolist(), computed=True)
with checked("M07.27b"):
    wbm.check("M07.27b", np.asarray(mymath.vectors.distance_to_hyperplane(X_27, W_27, B_27)).tolist(), computed=True)
with checked("M07.27c"):
    wbm.check("M07.27c", np.asarray(mymath.vectors.distance_to_hyperplane(X_27, W_27, B_27, signed=True)).tolist(),
              computed=True)
with checked("M07.27d"):
    wbm.check("M07.27d", type(mymath.vectors.side_of_hyperplane([1, 1, 1], W_27, B_27)).__name__, computed=True)
with checked("M07.27e"):
    wbm.check("M07.27e", mymath.vectors.distance_to_hyperplane([1, 1, 1], W_27, B_27), computed=True)
with checked("M07.27f"):
    wbm.check("M07.27f", raised(mymath.vectors.distance_to_hyperplane, [1, 2], [0, 0], 1), computed=True)''',
    solution=LOAD_REF + f'''
side, dist = mymath.vectors.side_of_hyperplane, mymath.vectors.distance_to_hyperplane
W_27, B_27, X_27 = {W_27}, {B_27}, {X_27}
print("a)", side(X_27, W_27, B_27), " b)", dist(X_27, W_27, B_27), " c)", dist(X_27, W_27, B_27, signed=True))
print("d)", type(side([1, 1, 1], W_27, B_27)).__name__, " e)", dist([1, 1, 1], W_27, B_27),
      " f)", raised(dist, [1, 2], [0, 0], 1))''',
    record=f'''wbm.record("M07.27a", [1, 1, -1, -1])
wbm.record("M07.27b", [2 / 3, 1 / 3, 2 / 3, 1.0], decimals=4,
           mistakes={{"{SCORE}": [2.0, 1.0, 2.0, 3.0], "la question demande des distances, positives : |w · x + b| / ‖w‖":
                         [2 / 3, 1 / 3, -2 / 3, -1.0],
                     "‖w‖ est la racine de 1 + 4 + 4 : divise par ‖w‖, pas par ‖w‖²": [2 / 9, 1 / 9, 2 / 9, 1 / 3]}})
wbm.record("M07.27c", [2 / 3, 1 / 3, -2 / 3, -1.0], decimals=4,
           mistakes={{"avec signed=True, garde le signe de w · x + b": [2 / 3, 1 / 3, 2 / 3, 1.0]}})
wbm.record("M07.27d", "int",
           mistakes={{"la docstring demande un int de Python pour un point : int(...)": {{"int64", "float", "float64"}},
                     "pour un seul point, la docstring demande un nombre, pas un tableau": "ndarray"}})
wbm.record("M07.27e", 2 / 3, decimals=4, mistakes={{"{SCORE}": 2.0}})
wbm.record("M07.27f", "ValueError",
           mistakes={{"un vecteur normal nul ne définit aucun hyperplan : lève une ValueError": {{"aucune",
                                                                                               "ZeroDivisionError"}},
                     "{wrong_error("ValueError")}": {errors_source("ValueError", "ZeroDivisionError")}}})''',
    after=tests_cells("test_side_of_hyperplane_ or test_distance_to_hyperplane_"),
    note="Les scores $\\mathbf{w} \\cdot \\mathbf{x} + b$ valent $1 - 2 + 2 + 1 = 2$, $1$, $-3 + 1 = -2$ et $2 - 6 + 0 + 1 = "
         "-3$ ; $\\lVert \\mathbf{w} \\rVert = \\sqrt{1 + 4 + 4} = 3$. a) $(1, 1, -1, -1)$. b) $\\big(\\frac{2}{3}, \\frac{1}{3}, "
         "\\frac{2}{3}, 1\\big)$. c) les mêmes avec le signe du score. L'origine donne le score $b = 1 > 0$ : elle est du "
         "côté positif, à la distance $\\frac{1}{3}$.",
)

M07_28 = Ex(
    "M07.28", "📦", 1, 10, "`np.linalg.norm` (ord = 1, 2, inf) et `scipy.spatial.distance` contre tes fonctions",
    "calculer des normes et des distances avec NumPy et SciPy, lire ce que renvoie chaque fonction, et comparer avec "
    "ta librairie.", "fiche §3 et §4 ; Ex M07.24", tracks="C",
    body="""En pratique, on ne réécrit pas les normes : NumPy et SciPy les fournissent.
- `np.linalg.norm(x, ord=p)` donne la norme $L^p$ d'un vecteur (`ord=1`, `ord=2`, `ord=np.inf`) ;
- `scipy.spatial.distance` (importé sous le nom `spd`) donne les distances entre deux points : `spd.euclidean(a, b)`, `spd.cityblock(a, b)` (L1, la distance de Manhattan), `spd.chebyshev(a, b)` (L∞), et `spd.cosine(a, b)`, qui renvoie une **distance cosinus**, $1 - \\cos\\theta$.

Avec $\\mathbf{a} = (2, -1, 1, 3)$ et $\\mathbf{b} = (-1, 1, 4, 1)$, calcule avec ces fonctions :
- a) `spd.cityblock(a, b)` ;
- b) `spd.chebyshev(a, b)` ;
- c) `spd.euclidean(a, b)` (4 décimales) ;
- d) `spd.cosine(a, b)` (4 décimales) ;
- e) `np.linalg.norm(a, ord=np.inf)` ;
- f) vrai ou faux : pour 20 vecteurs tirés au hasard et $p \\in \\{1, 2, 3, \\infty\\}$, ta fonction `norm_p` donne la même valeur que `np.linalg.norm` à $10^{-12}$ près (calcule-le avec une boucle et `np.isclose`).

Dans ta copie : quelle similarité cosinus correspond à d) ? Pourquoi SciPy préfère-t-il une distance, $1 - \\cos\\theta$, plutôt qu'une similarité ?""",
    todo='''answer_M07_28a = ...  # a) a number
answer_M07_28b = ...  # b) a number
answer_M07_28c = ...  # c) a number (4 decimals)
answer_M07_28d = ...  # d) a number (4 decimals)
answer_M07_28e = ...  # e) a number
answer_M07_28f = ...  # f) True or False, computed with a loop over random vectors''',
    check='''for letter, answer in zip("abcdef", [answer_M07_28a, answer_M07_28b, answer_M07_28c, answer_M07_28d,
                                     answer_M07_28e, answer_M07_28f]):
    wbm.check(f"M07.28{letter}", answer)''',
    solution='''ref_28 = wbm.load_mymath("ref")
a_28, b_28 = np.array([2, -1, 1, 3]), np.array([-1, 1, 4, 1])
answer_M07_28a = float(spd.cityblock(a_28, b_28))
answer_M07_28b = float(spd.chebyshev(a_28, b_28))
answer_M07_28c = float(spd.euclidean(a_28, b_28))
answer_M07_28d = float(spd.cosine(a_28, b_28))
answer_M07_28e = float(np.linalg.norm(a_28, ord=np.inf))
rng_28 = np.random.default_rng(28)
answer_M07_28f = all(np.isclose(ref_28.vectors.norm_p(x, p), np.linalg.norm(x, ord=p), rtol=1e-12, atol=1e-12)
                     for x in rng_28.normal(size=(20, 6)) for p in (1, 2, 3, np.inf))
print(answer_M07_28a, answer_M07_28b, answer_M07_28c, answer_M07_28d, answer_M07_28e, answer_M07_28f)''',
    record='''wbm.record("M07.28a", 10)
wbm.record("M07.28b", 3)
wbm.record("M07.28c", 26 ** 0.5, decimals=4)
wbm.record("M07.28d", 1 - 4 / 285 ** 0.5, decimals=4,
           mistakes={"spd.cosine renvoie une distance, 1 − cos θ : c'est la similarité cosinus": 4 / 285 ** 0.5})
wbm.record("M07.28e", 3)
wbm.record("M07.28f", True)''',
    note="a) $3 + 2 + 3 + 2 = 10$. b) $\\max(3, 2, 3, 2) = 3$. c) $\\sqrt{9 + 4 + 9 + 4} = \\sqrt{26} \\approx 5{,}0990$. "
         "d) $\\mathbf{a} \\cdot \\mathbf{b} = -2 - 1 + 4 + 3 = 4$, $\\cos\\theta = \\frac{4}{\\sqrt{15}\\sqrt{19}} \\approx "
         "0{,}2369$, d'où la distance cosinus $\\approx 0{,}7631$. Une distance vaut 0 pour deux points identiques et "
         "grandit quand ils s'éloignent : c'est ce qu'attendent les fonctions de SciPy qui cherchent des plus proches "
         "voisins ou regroupent des points.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, two experiments, a figure (M07.29 to M07.32)
# ---------------------------------------------------------------------------
M07_29_EXPERIMENT = '''rng_29 = np.random.default_rng(729)
for d in (2, 10, 1000):
    X, Y = rng_29.normal(size=(2000, d)), rng_29.normal(size=(2000, d))
    cosines = np.sum(X * Y, axis=1) / (np.sqrt(np.sum(X ** 2, axis=1)) * np.sqrt(np.sum(Y ** 2, axis=1)))
    angles = np.degrees(np.arccos(np.clip(cosines, -1, 1)))
    print(f"d = {d:4d} · mean angle {angles.mean():6.2f}° · standard deviation {angles.std():6.2f}° · "
          f"share between 85° and 95°: {np.mean((angles > 85) & (angles < 95)):.3f}")
fig, ax = plt.subplots(figsize=(6, 3.2))
for d in (2, 10, 1000):
    X, Y = rng_29.normal(size=(2000, d)), rng_29.normal(size=(2000, d))
    cosines = np.sum(X * Y, axis=1) / (np.sqrt(np.sum(X ** 2, axis=1)) * np.sqrt(np.sum(Y ** 2, axis=1)))
    ax.hist(np.degrees(np.arccos(np.clip(cosines, -1, 1))), bins=np.linspace(0, 180, 73), histtype="step",
            density=True, lw=1.8, label=f"d = {d}")
ax.set(xlabel="angle (degrés)", ylabel="densité", title="Angle de deux vecteurs gaussiens")
ax.legend()
plt.show()'''

M07_29 = Ex(
    "M07.29", "🔮", 1, 10, "Prédire : l'angle de deux vecteurs tirés au hasard en dimension 1 000",
    "prévoir la loi de l'angle entre deux vecteurs aléatoires selon la dimension, puis la mesurer.",
    "fiche §4 et §7", tracks="C, E", hypothesis=True,
    body="""On tire deux vecteurs de $\\mathbb{R}^d$ dont les coordonnées sont des variables indépendantes de loi $\\mathcal{N}(0, 1)$, et l'on calcule l'angle qu'ils font. On recommence 2 000 fois. Choisis, pour chaque question :
- a) en dimension 1 000, l'angle est le plus souvent : (1) proche de 0° ; (2) proche de 45° ; (3) proche de 90° ; (4) n'importe où entre 0° et 180°, sans préférence ;
- b) en dimension 1 000, la part des tirages dont l'angle est entre 85° et 95° : (1) moins de 10 % ; (2) environ la moitié ; (3) plus de 99 % ;
- c) quand la dimension passe de 10 à 1 000, l'écart-type des angles : (1) grandit ; (2) diminue ; (3) reste le même ;
- d) en dimension 2, l'angle est : (1) réparti uniformément entre 0° et 180° ; (2) concentré près de 90° ; (3) concentré près de 0° et de 180°.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M07_29a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M07_29b = ...  # b) 1, 2 or 3
prediction_M07_29c = ...  # c) 1, 2 or 3
prediction_M07_29d = ...  # d) 1, 2 or 3''',
    check='''for letter, prediction in zip("abcd", [prediction_M07_29a, prediction_M07_29b, prediction_M07_29c,
                                      prediction_M07_29d]):
    wbm.check(f"M07.29{letter}", prediction)''',
    record='''wbm.record("M07.29a", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M07.29b", 3, prediction=True, choices=[1, 2, 3])
wbm.record("M07.29c", 2, prediction=True, choices=[1, 2, 3])
wbm.record("M07.29d", 1, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(M07_29_EXPERIMENT, ["prediction_M07_29a", "prediction_M07_29b", "prediction_M07_29c",
                                              "prediction_M07_29d"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", M07_29_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : relie l'écart-type mesuré en dimension 1 000 au calcul de la "
               "fiche (§7 : le cosinus est de l'ordre de $\\frac{1}{\\sqrt{d}}$, et près de 90°, un petit cosinus "
               "$c$ correspond à un écart d'environ $c$ radians). Pourquoi la dimension 2 se comporte-t-elle si "
               "différemment ? Qu'en conclus-tu pour des *embeddings* de dimension 768 qui n'auraient aucune "
               "structure ?"),
    ],
    note="a) et b) En dimension 1 000, l'angle est presque toujours à moins de 5° de 90° : l'écart-type du cosinus vaut "
         "environ $\\frac{1}{\\sqrt{1000}} \\approx 0{,}032$, soit environ 1,8° pour l'angle, et 85° à 95° couvre près de "
         "trois écarts-types de chaque côté (plus de 99 %). c) L'écart-type diminue comme $\\frac{1}{\\sqrt{d}}$. d) En "
         "dimension 2, un vecteur gaussien a une direction uniforme sur le cercle : l'angle entre deux tirages est "
         "réparti uniformément entre 0° et 180°.",
)

M07_30_GIVEN = '''rng_30 = np.random.default_rng(737)
DIMS_30 = [1, 10, 100, 1000]
SAMPLES_30 = {d: rng_30.normal(size=(2000, d)) for d in DIMS_30}      # 2,000 Gaussian vectors in each dimension'''

M07_30_CHECK = '''with checked("M07.30a"):
    wbm.check("M07.30a", norm_summary(SAMPLES_30[1000])[0], computed=True)
with checked("M07.30b"):
    wbm.check("M07.30b", norm_summary(SAMPLES_30[1000])[1], computed=True)
with checked("M07.30c"):
    wbm.check("M07.30c", norm_summary(SAMPLES_30[1])[1], computed=True)
with checked("M07.30d"):
    spreads_30 = [norm_summary(SAMPLES_30[d])[1] / math.sqrt(d) for d in DIMS_30]
    wbm.check("M07.30d", float(np.polyfit(np.log(DIMS_30), np.log(spreads_30), 1)[0]), computed=True)'''

M07_30 = Ex(
    "M07.30", "🔬", 2, 20, "La norme d'un vecteur gaussien se concentre autour de √d",
    "mesurer comment la norme d'un vecteur gaussien se rapproche de $\\sqrt{d}$, et comment sa dispersion relative "
    "diminue avec la dimension.", "fiche §7 ; M02b (loi normale) ; M02c (écart-type)", tracks="C",
    body="""La fiche (§7) annonce que la norme d'un vecteur $\\mathbf{X}$ de $\\mathbb{R}^d$ à coordonnées gaussiennes indépendantes vaut environ $\\sqrt{d}$, avec une dispersion qui ne grandit pas. Vérifie-le sur les échantillons fixés de la cellule ci-dessous : 2 000 vecteurs dans chaque dimension 1, 10, 100 et 1 000.

Écris `norm_summary(X)`, qui reçoit un tableau de vecteurs (un par ligne, de dimension $d$) et renvoie le couple `(moyenne des normes divisée par √d, écart-type des normes)`, deux `float` (l'écart-type avec `np.std`, `ddof = 0`). Pas de boucle : les normes de toutes les lignes s'obtiennent d'un coup (`axis=1`).

La vérification calcule :
- a) la moyenne des normes divisée par $\\sqrt{1000}$, en dimension 1 000 (2 décimales) ;
- b) l'écart-type des normes en dimension 1 000 (2 décimales) ;
- c) l'écart-type des normes en dimension 1 (2 décimales) ;
- d) la pente de la droite qui ajuste $\\ln\\big(\\frac{\\text{écart-type}}{\\sqrt{d}}\\big)$ en fonction de $\\ln d$, pour les quatre dimensions (`np.polyfit`, 1 décimale).

Dans ta copie : que dit d) de la dispersion **relative** de la norme ? Compare c) à $\\sqrt{1 - \\frac{2}{\\pi}} \\approx 0{,}603$, l'écart-type exact de $|Z|$ pour $Z$ de loi $\\mathcal{N}(0, 1)$. Vers quelle valeur l'écart-type de b) semble-t-il tendre ?""",
    given=M07_30_GIVEN,
    todo='''def norm_summary(X):
    """(mean of the norms of the rows of X divided by √d, standard deviation of the norms), two Python floats."""
    raise NotImplementedError("les normes de toutes les lignes avec axis=1, puis np.mean et np.std")''',
    check=M07_30_CHECK,
    solution='''def norm_summary(X):
    """(mean of the norms of the rows of X divided by √d, standard deviation of the norms), two Python floats."""
    X = np.asarray(X, dtype=float)
    norms = np.sqrt(np.sum(X ** 2, axis=1))
    return float(norms.mean() / math.sqrt(X.shape[1])), float(norms.std())


for d in DIMS_30:
    mean_ratio, spread = norm_summary(SAMPLES_30[d])
    print(f"d = {d:4d} · mean norm / √d = {mean_ratio:.4f} · standard deviation of the norm = {spread:.4f}")
spreads_30 = [norm_summary(SAMPLES_30[d])[1] / math.sqrt(d) for d in DIMS_30]
print("slope:", np.polyfit(np.log(DIMS_30), np.log(spreads_30), 1)[0])''',
    record='''values_30 = {d: norm_summary(SAMPLES_30[d]) for d in DIMS_30}
wbm.record("M07.30a", values_30[1000][0], decimals=2,
           mistakes={"divise la moyenne des normes par √d": values_30[1000][0] * math.sqrt(1000)})
wbm.record("M07.30b", values_30[1000][1], decimals=2,
           mistakes={"la question demande l'écart-type des normes, sans diviser par √d": values_30[1000][1] / 1000 ** 0.5})
wbm.record("M07.30c", values_30[1][1], decimals=2)
wbm.record("M07.30d", float(np.polyfit(np.log(DIMS_30), np.log([values_30[d][1] / math.sqrt(d) for d in DIMS_30]),
                                      1)[0]), decimals=1)''',
    note="a) La moyenne des normes divisée par $\\sqrt{d}$ vaut presque 1 en dimension 1 000. b) L'écart-type de la "
         "norme reste proche de $\\frac{1}{\\sqrt{2}} \\approx 0{,}71$, quelle que soit la dimension (dès $d \\approx "
         "10$) ; c) en dimension 1, la norme est $|Z|$, d'écart-type 0,60. d) La dispersion relative, l'écart-type "
         "divisé par $\\sqrt{d}$, décroît comme $d^{-1/2}$ (pente $-0{,}5$) : en grande dimension, presque tous les "
         "vecteurs ont la même norme, à quelques pour mille près.",
)

POINTS_31 = "[[1, 2], [2, 3], [3, 1], [2, 2], [4, 3], [3, 4], [1, 1], [5, 2], [2, 5]]"
OUTLIERS_31 = "[[40, 2], [38, 1]]"

M07_31 = Ex(
    "M07.31", "🔬", 2, 20, "Médiane ou moyenne : le centre qui minimise les distances L1 ou leurs carrés, face à des "
    "points aberrants",
    "comparer le point qui minimise la somme des distances L1 (la médiane, coordonnée par coordonnée) à celui qui "
    "minimise la somme des carrés des distances (le barycentre), et leur résistance aux points aberrants.",
    "fiche §3 et §6 ; Ex M07.26", tracks="C",
    body=f"""Le barycentre minimise $\\sum_i \\lVert \\mathbf{{x}}_i - \\mathbf{{c}} \\rVert_2^2$ (fiche §6). Et la somme des distances L1, $\\sum_i \\lVert \\mathbf{{x}}_i - \\mathbf{{c}} \\rVert_1$ ? Elle se découpe coordonnée par coordonnée : $\\sum_i \\lVert \\mathbf{{x}}_i - \\mathbf{{c}} \\rVert_1 = \\sum_j \\sum_i |x_{{ij}} - c_j|$, et chaque somme $\\sum_i |x_{{ij}} - c_j|$ est la plus petite quand $c_j$ est une **médiane** des $x_{{ij}}$ (pour un nombre impair de valeurs, la valeur du milieu). Le point qui minimise la somme des distances L1 est donc la médiane, coordonnée par coordonnée.

Écris `l1_center(points)`, qui renvoie ce point en tableau NumPy (`np.median` avec le bon `axis`), et `l1_cost(points, c)`, qui renvoie $\\sum_i \\lVert \\mathbf{{x}}_i - \\mathbf{{c}} \\rVert_1$ en `float`.

Les neuf points `{POINTS_31}` décrivent les positions d'un petit troupeau ; deux points aberrants `{OUTLIERS_31}` y sont ajoutés (une erreur de saisie). La vérification calcule, avec ta fonction `mymath.vectors.centroid` pour le barycentre (écris d'abord M07.26) :
- a) `l1_center` des neuf points (une liste) ;
- b) leur barycentre (une liste, 4 décimales) ;
- c) `l1_center` des onze points (une liste) ;
- d) le barycentre des onze points (une liste, 4 décimales) ;
- e) la distance euclidienne dont le barycentre s'est déplacé entre b) et d) (4 décimales) ;
- f) la distance euclidienne dont la médiane s'est déplacée entre a) et c) ;
- g) le rapport `l1_cost(onze points, barycentre) / l1_cost(onze points, médiane)` (4 décimales).

Dans ta copie : pourquoi la médiane résiste-t-elle aux points aberrants, et pas le barycentre ? Lequel des deux décrit le mieux le troupeau ? Que confirme g) ?""",
    todo='''def l1_center(points):
    """The coordinate-wise median of the rows of points: the point that minimises the sum of the L1 distances."""
    raise NotImplementedError("np.median, colonne par colonne")


def l1_cost(points, c):
    """The sum of the L1 distances from the rows of points to c, as a Python float."""
    raise NotImplementedError("les valeurs absolues des écarts, puis la somme")''',
    check=f'''POINTS_31, OUTLIERS_31 = np.array({POINTS_31}), np.array({OUTLIERS_31})
ALL_31 = np.vstack([POINTS_31, OUTLIERS_31])
with checked("M07.31a"):
    wbm.check("M07.31a", np.asarray(l1_center(POINTS_31), dtype=float).tolist(), computed=True)
with checked("M07.31b"):
    wbm.check("M07.31b", np.asarray(mymath.vectors.centroid(POINTS_31)).tolist(), computed=True)
with checked("M07.31c"):
    wbm.check("M07.31c", np.asarray(l1_center(ALL_31), dtype=float).tolist(), computed=True)
with checked("M07.31d"):
    wbm.check("M07.31d", np.asarray(mymath.vectors.centroid(ALL_31)).tolist(), computed=True)
with checked("M07.31e"):
    moved_mean = np.asarray(mymath.vectors.centroid(ALL_31)) - np.asarray(mymath.vectors.centroid(POINTS_31))
    wbm.check("M07.31e", float(np.sqrt(np.sum(moved_mean ** 2))), computed=True)
with checked("M07.31f"):
    moved_median = np.asarray(l1_center(ALL_31), dtype=float) - np.asarray(l1_center(POINTS_31), dtype=float)
    wbm.check("M07.31f", float(np.sqrt(np.sum(moved_median ** 2))), computed=True)
with checked("M07.31g"):
    wbm.check("M07.31g", l1_cost(ALL_31, mymath.vectors.centroid(ALL_31)) / l1_cost(ALL_31, l1_center(ALL_31)),
              computed=True)''',
    solution=f'''def l1_center(points):
    """The coordinate-wise median of the rows of points: the point that minimises the sum of the L1 distances."""
    return np.median(np.asarray(points, dtype=float), axis=0)


def l1_cost(points, c):
    """The sum of the L1 distances from the rows of points to c, as a Python float."""
    return float(np.sum(np.abs(np.asarray(points, dtype=float) - np.asarray(c, dtype=float))))


ref_31 = wbm.load_mymath("ref")
POINTS_31, OUTLIERS_31 = np.array({POINTS_31}), np.array({OUTLIERS_31})
ALL_31 = np.vstack([POINTS_31, OUTLIERS_31])
for name, pts in [("9 points", POINTS_31), ("11 points", ALL_31)]:
    print(name, "· median:", l1_center(pts), "· centroid:", ref_31.vectors.centroid(pts).round(4))
print("L1 cost ratio:", l1_cost(ALL_31, ref_31.vectors.centroid(ALL_31)) / l1_cost(ALL_31, l1_center(ALL_31)))''',
    record='''wbm.record("M07.31a", [2.0, 2.0], decimals=6)
wbm.record("M07.31b", [23 / 9, 23 / 9], decimals=4)
wbm.record("M07.31c", [3.0, 2.0], decimals=6,
           mistakes={"np.median doit travailler colonne par colonne : axis=0": [3.0, 3.0]})
wbm.record("M07.31d", [101 / 11, 26 / 11], decimals=4)
wbm.record("M07.31e", float(np.hypot(101 / 11 - 23 / 9, 26 / 11 - 23 / 9)), decimals=4)
wbm.record("M07.31f", 1.0, decimals=6)
wbm.record("M07.31g", float(np.sum(np.abs(ALL_31 - [101 / 11, 26 / 11])) / np.sum(np.abs(ALL_31 - [3, 2]))),
           decimals=4)''',
    note="Sans les points aberrants, la médiane $(2, 2)$ et le barycentre $\\big(\\frac{23}{9}, \\frac{23}{9}\\big) "
         "\\approx (2{,}56 ;\\ 2{,}56)$ sont proches. Avec eux, le barycentre part en $\\big(\\frac{101}{11}, "
         "\\frac{26}{11}\\big) \\approx (9{,}18 ;\\ 2{,}36)$, loin de tout le troupeau : il s'est déplacé d'environ 6,63. "
         "La médiane passe seulement à $(3, 2)$ : deux valeurs extrêmes décalent le rang du milieu d'une ou deux places, "
         "quelle que soit leur grandeur. Les carrés donnent un poids énorme aux grands écarts ; les valeurs absolues, "
         "non. g) confirme que la médiane minimise bien la somme des distances L1 : le barycentre fait nettement pire.",
)

M07_32_CHECK = '''with checked("M07.32 vérifications"):
    import matplotlib.lines as mlines
    problems = []
    for p_t in (1, 1.5, 2, 3, float("inf")):
        fig_t, ax_t = plt.subplots()
        try:
            created = drawn(draw_unit_circle, ax_t, p_t)
        except NotImplementedError:
            plt.close(fig_t)
            raise
        lines_t = [line for line in ax_t.get_lines() if len(line.get_xdata()) > 1]
        plt.close(fig_t)
        if created:
            problems.append("draw_unit_circle ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans l'axe "
                            "reçu")
            break
        if not lines_t:
            problems.append(f"pour p = {p_t}, aucune courbe n'est tracée : ax.plot(xs, ys)")
            break
        xy = np.concatenate([np.column_stack([line.get_xdata(), line.get_ydata()]) for line in lines_t])
        xy = xy[np.isfinite(xy).all(axis=1)]
        norms_t = (np.max(np.abs(xy), axis=1) if math.isinf(p_t)
                   else np.sum(np.abs(xy) ** p_t, axis=1) ** (1 / p_t))
        angles_t = np.arctan2(xy[:, 1], xy[:, 0])
        if len(xy) < 100:
            problems.append(f"pour p = {p_t}, la courbe a {len(xy)} points : prends-en au moins 100 pour qu'elle soit "
                            "lisse")
            break
        if not np.allclose(norms_t, 1, atol=1e-6):
            problems.append(f"pour p = {p_t}, des points tracés n'ont pas une norme L{p_t} égale à 1 (de "
                            f"{norms_t.min():.3f} à {norms_t.max():.3f}) : divise chaque direction par sa norme")
            break
        if np.histogram(angles_t, bins=8, range=(-np.pi, np.pi))[0].min() == 0:
            problems.append(f"pour p = {p_t}, la courbe ne fait pas tout le tour de l'origine : prends des directions "
                            "sur tout le cercle, de 0 à 2π")
            break
    if problems:
        print("❌ Ex M07.32 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M07.32 : draw_unit_circle trace des courbes fermées dont tous les points ont la norme 1, pour "
              "cinq valeurs de p.")'''

M07_32 = Ex(
    "M07.32", "🎨", 1, 20, "Les boules unités L1, L2, L∞ et Lp dans le plan",
    "tracer les vecteurs de norme 1 pour plusieurs normes $L^p$, en normalisant des directions, et voir les boules "
    "s'emboîter.", "fiche §3 ; R0 (matplotlib)", tracks="C",
    body="""Écris `draw_unit_circle(ax, p, **style)`, qui trace dans l'axe `ax` la courbe des vecteurs du plan de norme $L^p$ égale à 1. Une méthode simple : prends 400 directions $\\mathbf{d}_k = (\\cos t_k, \\sin t_k)$ régulièrement réparties de 0 à $2\\pi$, divise chacune par sa norme $L^p$ (ta fonction `norm_p`, ou la formule, avec `float("inf")` pour L∞), et relie les points obtenus par `ax.plot(xs, ys, **style)`. Les arguments `**style` (couleur, épaisseur, légende) passent tels quels à `ax.plot`.

Puis trace sur la même figure les courbes de $p = 1$, $1{,}5$, $2$, $4$ et $\\infty$, avec une légende, la même échelle sur les deux axes (`ax.set_aspect("equal")`) et les axes de coordonnées. Ajoute, en pointillés, la courbe de $p = \\frac{1}{2}$ : pour elle, `norm_p` lève une erreur, utilise la formule.

Une cellule de vérification essaie ta fonction pour cinq valeurs de $p$ (la figure elle-même se juge à l'œil).

Dans ta copie : comment les courbes s'emboîtent-elles, et quelle inégalité entre normes cela traduit-il ? Pourquoi la courbe de $p = \\frac{1}{2}$ montre-t-elle, d'un seul coup d'œil, que ce n'est pas une norme (pense au segment qui joint $(1, 0)$ à $(0, 1)$) ?""",
    todo='''def draw_unit_circle(ax, p, **style):
    """In ax, the curve of the vectors of the plane whose L^p norm equals 1 (p >= 1 or float("inf"); the formula
    also for 0 < p < 1), drawn with ax.plot(..., **style)."""
    raise NotImplementedError("400 directions (cos t, sin t), chacune divisée par sa norme L^p, puis ax.plot")''',
    check='''with checked("M07.32 figure"):
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    try:
        for p, style in [(1, {}), (1.5, {}), (2, {}), (4, {}), (float("inf"), {}), (0.5, {"ls": "--", "color": "gray"})]:
            created = drawn(lambda p=p, style=style: draw_unit_circle(ax, p, label=f"p = {p}", **style))
    except BaseException:
        plt.close(fig)                                     # no empty figure while the function is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M07.32 : draw_unit_circle ouvre sa propre figure : dessine dans l'axe reçu.")
    else:
        ax.axhline(0, color="black", lw=0.5)
        ax.axvline(0, color="black", lw=0.5)
        ax.set_aspect("equal")
        ax.legend(fontsize=8)
        plt.show()''',
    solution='''def draw_unit_circle(ax, p, **style):
    """In ax, the curve of the vectors of the plane whose L^p norm equals 1 (p >= 1 or float("inf"); the formula
    also for 0 < p < 1), drawn with ax.plot(..., **style)."""
    t = np.linspace(0, 2 * np.pi, 401)
    directions = np.column_stack([np.cos(t), np.sin(t)])
    if math.isinf(p):
        norms = np.max(np.abs(directions), axis=1)
    else:
        norms = np.sum(np.abs(directions) ** p, axis=1) ** (1 / p)
    points = directions / norms[:, None]
    ax.plot(points[:, 0], points[:, 1], **style)


fig, ax = plt.subplots(figsize=(5.5, 5.5))
for p, style in [(1, {}), (1.5, {}), (2, {}), (4, {}), (float("inf"), {}), (0.5, {"ls": "--", "color": "gray"})]:
    draw_unit_circle(ax, p, label=f"p = {p}", **style)
ax.axhline(0, color="black", lw=0.5)
ax.axvline(0, color="black", lw=0.5)
ax.set_aspect("equal")
ax.set(title="Les vecteurs de norme 1 pour plusieurs p")
ax.legend(fontsize=8)
plt.show()''',
    after=[("md", "**Vérifications automatiques** (sur cinq valeurs de $p$, chacune dans un axe neuf)."),
           ("code", M07_32_CHECK)],
    note="Les courbes s'emboîtent : celle de $p = 1$ (un losange) est à l'intérieur, celle de L∞ (un carré) à "
         "l'extérieur, et les autres passent de l'une à l'autre. Plus la norme est grande pour un même vecteur, plus "
         "sa boule unité est petite : $\\lVert \\mathbf{x} \\rVert_\\infty \\le \\lVert \\mathbf{x} \\rVert_2 \\le \\lVert "
         "\\mathbf{x} \\rVert_1$ se lit comme « le carré contient le cercle, qui contient le losange ». La courbe de $p = "
         "\\frac{1}{2}$ est creusée vers l'intérieur : le milieu $(\\frac{1}{2}, \\frac{1}{2})$ du segment qui joint deux "
         "de ses points, $(1, 0)$ et $(0, 1)$, est à l'extérieur. Pour une norme, la boule unité est toujours convexe "
         "(M10) : c'est l'inégalité triangulaire en image.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M07.33 to M07.35)
# ---------------------------------------------------------------------------
M07_33_MISTAKES = bug_letters_mistakes(
    "ACE", "BDF",
    {"A": "refais chaque calcul de distance sur un petit exemple",
     "C": "refais chaque calcul de cosinus sur un petit exemple",
     "E": "refais chaque calcul de composante sur un petit exemple"},
    name_correct=False)

M07_33 = Ex(
    "M07.33", "🐛", 1, 15, "Chasse à l'erreur : une distance sans racine, un cosinus mal normalisé, une projection sur "
    "un vecteur non unitaire",
    "repérer dans du code les erreurs classiques sur les distances, les cosinus et les composantes, puis calculer les "
    "bonnes valeurs.", "fiche §3 et §4", tracks="C",
    body="""Un collègue a écrit six lignes, chacune avec un commentaire qui dit ce qu'elle doit calculer, pour $\\mathbf{a} = (1, 3, -2)$ et $\\mathbf{b} = (4, -1, 2)$. Trois lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter de code**, trouve-les.

```python
a, b = np.array([1.0, 3.0, -2.0]), np.array([4.0, -1.0, 2.0])
dist = np.sum((a - b) ** 2)                         # (A) the Euclidean distance between a and b
dist_l1 = np.sum(np.abs(a - b))                     # (B) the L1 distance between a and b
cos = (a @ b) / np.sqrt(a @ a)                      # (C) the cosine similarity of a and b
norm_b = np.sqrt(b @ b)                             # (D) the Euclidean norm of b
comp = (b @ a) / (a @ a)                            # (E) the component of b along a (a signed length)
dist_inf = np.max(np.abs(a - b))                    # (F) the L∞ distance between a and b
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire (une liste de 6 nombres, 3 décimales).

Dans ta copie : pour chaque ligne fausse, quelle erreur a été faite, et comment la corriger ? La ligne (E) calcule autre chose qu'une composante : quoi, et à quoi sert ce nombre (fiche §4) ?""",
    todo='''answer_M07_33a = ...  # a) letters, as text
answer_M07_33b = ...  # b) a list of 6 values (3 decimals)''',
    check='''wbm.check("M07.33a", answer_M07_33a)
wbm.check("M07.33b", answer_M07_33b)''',
    solution='''answer_M07_33a = "ACE"
a, b = np.array([1.0, 3.0, -2.0]), np.array([4.0, -1.0, 2.0])
dist = np.sqrt(np.sum((a - b) ** 2))                # (A) the square root was missing: √41
dist_l1 = np.sum(np.abs(a - b))                     # (B) correct: 11
cos = (a @ b) / (np.sqrt(a @ a) * np.sqrt(b @ b))   # (C) divide by both norms: -3/√294
norm_b = np.sqrt(b @ b)                             # (D) correct: √21
comp = (b @ a) / np.sqrt(a @ a)                     # (E) divide by ‖a‖, not ‖a‖²: -3/√14
dist_inf = np.max(np.abs(a - b))                    # (F) correct: 4
answer_M07_33b = [float(v) for v in (dist, dist_l1, cos, norm_b, comp, dist_inf)]
print(answer_M07_33a, [round(value, 4) for value in answer_M07_33b])''',
    record=f'''wbm.record("M07.33a", "ACE",
           mistakes={M07_33_MISTAKES})
wbm.record("M07.33b", [41 ** 0.5, 11, -3 / 294 ** 0.5, 21 ** 0.5, -3 / 14 ** 0.5, 4], decimals=3,
           mistakes={{"(A) : la distance euclidienne est la racine de la somme des carrés":
                         [41, 11, -3 / 294 ** 0.5, 21 ** 0.5, -3 / 14 ** 0.5, 4],
                     "(C) : le cosinus divise par le produit des deux normes":
                         [41 ** 0.5, 11, -3 / 14 ** 0.5, 21 ** 0.5, -3 / 14 ** 0.5, 4],
                     "(E) : la composante divise par ‖a‖, pas par ‖a‖²":
                         [41 ** 0.5, 11, -3 / 294 ** 0.5, 21 ** 0.5, -3 / 14, 4]}})''',
    note="(A) oublie la racine : la somme des carrés vaut 41, la distance $\\sqrt{41} \\approx 6{,}403$. (C) ne divise que "
         "par $\\lVert \\mathbf{a} \\rVert$ : avec $\\mathbf{a} \\cdot \\mathbf{b} = 4 - 3 - 4 = -3$, le cosinus vaut "
         "$\\frac{-3}{\\sqrt{14}\\sqrt{21}} \\approx -0{,}175$. (E) divise par $\\lVert \\mathbf{a} \\rVert^2$ : c'est le "
         "**coefficient** $t$ de la projection, $\\mathbf{p} = t\\,\\mathbf{a}$ ; la composante (une longueur avec un signe) "
         "vaut $\\frac{-3}{\\sqrt{14}} \\approx -0{,}802$. (B), (D) et (F) sont justes : 11, $\\sqrt{21} \\approx 4{,}583$ et 4.",
)

M07_34_CHECK = '''with checked("M07.34 vérifications"):
    import ast
    import inspect
    import textwrap
    problems = []
    rng_t = np.random.default_rng(734)
    X_t = rng_t.normal(size=(7, 5))
    X_t[3] = 0.0                                                     # a zero row
    for p_t in (1, 2, float("inf")):
        expected = np.array([max(abs(v) for v in row) if math.isinf(p_t) else sum(abs(v) ** p_t for v in row) ** (1 / p_t)
                             for row in X_t])
        got = row_norms(X_t, p_t)
        if got is None:
            problems.append("row_norms ne renvoie rien : il manque return")
            break
        got = np.asarray(got)
        if got.shape != (7,):
            problems.append(f"row_norms renvoie la forme {got.shape} : une norme par ligne, de forme (7,)"
                            + (" ; somme sur axis=1, les colonnes" if got.shape == (5,) else ""))
            break
        if not np.allclose(got, expected, atol=1e-12):
            problems.append(f"pour p = {p_t}, row_norms ne donne pas la norme de chaque ligne")
            break
    if not problems:
        unit_t = normalize_rows(X_t)
        if unit_t is None:
            problems.append("normalize_rows ne renvoie rien : il manque return")
        else:
            unit_t = np.asarray(unit_t)
            if unit_t.shape != X_t.shape:
                problems.append(f"normalize_rows renvoie la forme {unit_t.shape}, pas {X_t.shape} : keepdims=True garde "
                                "une colonne pour le broadcasting")
            elif not np.all(np.isfinite(unit_t)):
                problems.append("normalize_rows produit des nan pour la ligne nulle : laisse-la à zéro (np.where)")
            elif not np.allclose(np.delete(np.sqrt(np.sum(unit_t ** 2, axis=1)), 3), 1, atol=1e-12):
                problems.append("les lignes non nulles de normalize_rows n'ont pas la norme 1")
            elif not np.allclose(unit_t[3], 0):
                problems.append("la ligne nulle doit rester nulle")
            elif not np.allclose(unit_t * np.sqrt(np.sum(X_t ** 2, axis=1, keepdims=True)), X_t, atol=1e-12):
                problems.append("normalize_rows doit garder la direction de chaque ligne")
    if not problems:
        for name_t, function_t in [("row_norms", row_norms), ("normalize_rows", normalize_rows)]:
            try:
                tree_t = ast.parse(textwrap.dedent(inspect.getsource(function_t)))
            except (OSError, TypeError, SyntaxError):
                continue
            if any(isinstance(node, (ast.For, ast.While, ast.comprehension)) for node in ast.walk(tree_t)):
                problems.append(f"{name_t} contient une boucle : l'exercice demande de calculer toutes les lignes d'un "
                                "coup (axis, keepdims)")
                break
    if problems:
        print("❌ Ex M07.34 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M07.34 : row_norms et normalize_rows sont justes, sans boucle, ligne nulle comprise.")'''

M07_34_TIME = '''import time
X_big = np.random.default_rng(34).normal(size=(20000, 64))
start = time.perf_counter()
loop = np.array([math.sqrt(sum(v * v for v in row)) for row in X_big])
loop_seconds = time.perf_counter() - start
start = time.perf_counter()
fast = np.asarray(row_norms(X_big, 2))
fast_seconds = time.perf_counter() - start
print(f"loop: {loop_seconds:.3f} s · row_norms: {fast_seconds:.4f} s · same values: {np.allclose(loop, fast)}")'''

M07_34 = Ex(
    "M07.34", "🛠️", 1, 15, "Les normes de toutes les lignes d'un tableau : axis, keepdims et broadcasting",
    "calculer les normes de toutes les lignes d'un tableau et normaliser chaque ligne d'un coup, sans boucle, avec "
    "`axis` et `keepdims`.", "fiche §1 et §3 ; 0A (broadcasting)", tracks="C",
    body="""Un dataset est un tableau `X` de forme `(n, p)`, un exemple par ligne. Calculer la norme de chaque exemple, ou le normaliser, se fait d'un coup avec NumPy :
- `np.sum(A, axis=1)` additionne chaque **ligne** (on « écrase » l'axe des colonnes) et rend un tableau de forme `(n,)` ;
- avec `keepdims=True`, le résultat garde la forme `(n, 1)` : une colonne, qui se divise ligne par ligne par le **broadcasting** (`X / colonne` divise chaque ligne par son nombre).

Écris, **sans boucle** :
- `row_norms(X, p=2)`, qui renvoie le tableau des normes $L^p$ des lignes de `X` (`p = float("inf")` pour L∞) ;
- `normalize_rows(X)`, qui renvoie le tableau de même forme dont chaque ligne est divisée par sa norme L2 ; une ligne nulle reste nulle (pas de division par zéro : `np.where`).

Une cellule de vérification compare tes fonctions à une boucle (ligne nulle comprise) et vérifie qu'elles n'en contiennent pas ; une autre compare les temps de calcul.

Dans ta copie : que donnerait `np.sum(X ** 2, axis=0)` ? Pourquoi `X / row_norms(X)` (sans `keepdims`) échoue-t-il, ou se trompe-t-il quand `X` est carré ? Combien de fois plus rapide est `row_norms` que la boucle ?""",
    todo='''def row_norms(X, p=2):
    """The L^p norms of the rows of X (p = float("inf") for L∞), without a Python loop."""
    raise NotImplementedError("np.abs, puis une somme (ou un maximum) sur axis=1")


def normalize_rows(X):
    """Each row of X divided by its L2 norm (a zero row stays zero), without a Python loop."""
    raise NotImplementedError("les normes avec keepdims=True, puis np.where pour la ligne nulle")''',
    solution='''def row_norms(X, p=2):
    """The L^p norms of the rows of X (p = float("inf") for L∞), without a Python loop."""
    A = np.abs(np.asarray(X, dtype=float))
    if math.isinf(p):
        return np.max(A, axis=1)
    return np.sum(A ** p, axis=1) ** (1 / p)


def normalize_rows(X):
    """Each row of X divided by its L2 norm (a zero row stays zero), without a Python loop."""
    X = np.asarray(X, dtype=float)
    norms = np.sqrt(np.sum(X ** 2, axis=1, keepdims=True))
    return np.where(norms > 0, X / np.where(norms > 0, norms, 1.0), 0.0)''',
    after=[("code", M07_34_CHECK),
           ("md", "**Le temps de calcul** (cette cellule utilise ta fonction)."),
           ("todo", 'with checked("M07.34 temps"):\n' + "\n".join("    " + line for line in M07_34_TIME.splitlines())),
           ("solution", M07_34_TIME)],
    note="`np.sum(X ** 2, axis=0)` additionne chaque **colonne** : un nombre par feature, pas par exemple. Sans "
         "`keepdims`, les normes ont la forme `(n,)`, que NumPy aligne sur la **dernière** dimension de `X` : une erreur "
         "de forme si $p \\ne n$, et, pire, une division des **colonnes** sans message d'erreur quand `X` est carré. La "
         "ligne nulle demande un `np.where` : $\\frac{0}{0}$ donnerait `nan`. Sur 20 000 lignes, la version vectorisée "
         "est en général une dizaine de fois plus rapide que la boucle, souvent davantage.",
)

M07_35_GIVEN = '''def make_cities(seed, angle):
    """60 towns in three groups of 26, 20 and 14, rotated by angle degrees (coordinates in km, rounded to 10 m)."""
    rng = np.random.default_rng(seed)
    centers, sizes = np.array([[0.0, 0.0], [10.0, 1.0], [4.0, 8.0]]), [26, 20, 14]
    towns = np.vstack([rng.normal(c, 1.2, size=(k, 2)) for c, k in zip(centers, sizes)])
    t = np.radians(angle)
    rotation = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    return np.round(towns @ rotation.T + [5.0, 3.0], 2)


def total_distance(points, c):
    """Σ ‖x_i − c‖: the sum of the (non-squared) Euclidean distances from the rows of points to c."""
    return float(np.sum(np.sqrt(np.sum((np.asarray(points, dtype=float) - np.asarray(c, dtype=float)) ** 2, axis=1))))


CITIES_35 = make_cities(735, 20)'''

M07_35_CHECK = '''with checked("M07.35 défi"):
    import time
    from scipy.optimize import minimize
    problems, worst_ratio, slowest = [], 0.0, 0.0
    for seed_t, angle_t in [(735, 20), (11, 75), (12, 140), (13, 200), (14, 290)]:
        towns_t = make_cities(seed_t, angle_t)
        best_t = minimize(lambda c: total_distance(towns_t, c), np.median(towns_t, axis=0), method="Nelder-Mead",
                          options={"xatol": 1e-10, "fatol": 1e-10, "maxiter": 20000}).fun
        start_t = time.perf_counter()
        try:
            got_t = geometric_median(towns_t)
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            problems.append(f"geometric_median lève {type(exc).__name__} ({exc})")
            break
        slowest = max(slowest, time.perf_counter() - start_t)
        if got_t is None or np.shape(got_t) != (2,) or not np.all(np.isfinite(np.asarray(got_t, dtype=float))):
            problems.append("geometric_median doit renvoyer un point du plan : deux nombres finis")
            break
        worst_ratio = max(worst_ratio, total_distance(towns_t, got_t) / best_t)
    if problems:
        print("❌ Ex M07.35 : " + problems[0] + ".")
    elif worst_ratio > 1.001:
        print(f"❌ Ex M07.35 : ton point fait jusqu'à {100 * (worst_ratio - 1):.3f} % de plus que le minimum (objectif : "
              "0,1 % au plus). Le barycentre ne minimise que la somme des carrés : regarde les indices.")
    elif slowest > 5:
        print(f"❌ Ex M07.35 : objectif atteint, mais en {slowest:.1f} s pour un ensemble de villes (objectif : 5 s).")
    else:
        print(f"✅ Ex M07.35 : défi réussi, à {100 * (worst_ratio - 1):.4f} % du minimum au pire, sur cinq ensembles de "
              "villes.")
with checked("M07.35"):
    wbm.check("M07.35", round(total_distance(CITIES_35, geometric_median(CITIES_35)), 1), computed=True)'''

M07_35 = Ex(
    "M07.35", "🏆", 3, 30, "Défi : le point qui minimise la somme des distances (non au carré) à 60 villes, à 0,1 % "
    "près",
    "trouver numériquement le point qui minimise la somme des distances euclidiennes à des points donnés (la médiane "
    "géométrique), et voir qu'il n'est ni le barycentre ni la médiane coordonnée par coordonnée.",
    "fiche §3 et §6 ; Ex M07.26 et M07.31", tracks="C",
    body="""Une entreprise veut construire un entrepôt qui dessert 60 villes, et minimiser la **somme des distances** (pas de leurs carrés) de l'entrepôt aux villes, $\\sum_i \\lVert \\mathbf{x}_i - \\mathbf{c} \\rVert$ (la fonction `total_distance` ci-dessous). Ce point s'appelle la **médiane géométrique**. Il n'a pas de formule : le barycentre minimise la somme des **carrés** (fiche §6), et la médiane coordonnée par coordonnée minimise la somme des distances **L1** (M07.31), mais aucun des deux ne convient ici.

Écris `geometric_median(points)`, qui renvoie le point `[x, y]` (deux nombres). **L'objectif** : une somme des distances à 0,1 % au plus du minimum, en moins de 5 secondes, sur les villes `CITIES_35` et sur quatre autres ensembles de villes. NumPy suffit ; `scipy.optimize` est interdit (c'est lui que la vérification utilise pour trouver le minimum).

La vérification essaie ta fonction sur cinq ensembles de villes, puis vérifie la somme des distances, arrondie à 0,1 km, pour `CITIES_35`.

Dans ta copie : de combien (en %) le barycentre et la médiane coordonnée par coordonnée manquent-ils l'objectif pour `CITIES_35` ? Explique l'idée de ta méthode. Le point trouvé est-il plus proche du groupe de 26 villes ou des deux autres, et pourquoi ?""",
    given=M07_35_GIVEN,
    todo='''def geometric_median(points):
    """The point [x, y] that minimises the sum of the Euclidean distances to the rows of points (within 0.1 %)."""
    raise NotImplementedError("pars du barycentre, puis améliore : un barycentre pondéré par l'inverse des distances")''',
    check=M07_35_CHECK,
    solution='''def geometric_median(points, iterations=500):
    """The point [x, y] that minimises the sum of the Euclidean distances to the rows of points (within 0.1 %).

    Weiszfeld's algorithm: start from the centroid, then replace c by the centroid of the points weighted by the
    inverse of their distances to c (a point far away pulls less than in the centroid)."""
    P = np.asarray(points, dtype=float)
    c = P.mean(axis=0)
    for _ in range(iterations):
        d = np.sqrt(np.sum((P - c) ** 2, axis=1))
        d = np.maximum(d, 1e-12)                       # c on a town: avoid a division by zero
        weights = 1 / d
        c = np.sum(weights[:, None] * P, axis=0) / np.sum(weights)
    return [float(c[0]), float(c[1])]


g_35 = geometric_median(CITIES_35)
best_35 = total_distance(CITIES_35, g_35)
print("geometric median:", np.round(g_35, 3), "· sum of distances:", round(best_35, 3))
print("centroid: +", round(100 * (total_distance(CITIES_35, CITIES_35.mean(axis=0)) / best_35 - 1), 2), "%",
      "· coordinate-wise median: +", round(100 * (total_distance(CITIES_35, np.median(CITIES_35, axis=0)) / best_35 - 1),
                                           2), "%")''',
    after=[("solution", M07_35_CHECK.split('with checked("M07.35"):')[0].rstrip())],
    record='''wbm.record("M07.35", round(total_distance(CITIES_35, geometric_median(CITIES_35)), 1), decimals=1,
           mistakes={"c'est la somme des distances au barycentre, qui ne minimise que la somme des carrés":
                         round(total_distance(CITIES_35, CITIES_35.mean(axis=0)), 1),
                     "c'est la somme des distances à la médiane coordonnée par coordonnée, qui minimise la somme des "
                     "distances L1": round(total_distance(CITIES_35, np.median(CITIES_35, axis=0)), 1)})''',
    note="Le barycentre manque l'objectif d'environ 0,6 %, et la médiane coordonnée par coordonnée de près de 2 %. "
         "L'algorithme de Weiszfeld (1937) part du barycentre, puis remplace $\\mathbf{c}$ par le barycentre des villes "
         "pondérées par $\\frac{1}{\\lVert \\mathbf{x}_i - \\mathbf{c} \\rVert}$ : une ville lointaine tire moins fort que "
         "dans le barycentre, où chaque ville tire proportionnellement à sa distance. Le point fixe annule le gradient "
         "de la somme des distances, $\\sum_i \\frac{\\mathbf{c} - \\mathbf{x}_i}{\\lVert \\mathbf{c} - \\mathbf{x}_i \\rVert}$, "
         "une somme de vecteurs unitaires. Le point trouvé est plus près du groupe de 26 villes que le barycentre (à "
         "environ 3,8 km de son centre, contre 4,9 km) : avec les distances non élevées au carré, chaque ville "
         "« vote » avec une force égale, et le groupe le plus nombreux l'emporte.",
)


PART_A = Part("A", "Ta librairie : normes, cosinus, projection, barycentre, hyperplans ; NumPy et SciPy",
              "Fiche §3 à §6. Les sept fonctions de `mymath/vectors.py`, puis les mêmes calculs avec NumPy et SciPy.",
              given=TOOLS, exercises=[M07_24, M07_25, M07_26, M07_27, M07_28])

PART_B = Part("B", "Une prédiction, deux expériences et une figure",
              "Fiche §3, §6 et §7. L'angle de deux vecteurs aléatoires, la norme d'un vecteur gaussien, la médiane face "
              "à la moyenne, les boules unités.",
              exercises=[M07_29, M07_30, M07_31, M07_32])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §1, §3, §4 et §6. Trois erreurs à trouver, les normes de toutes les lignes d'un tableau, puis la "
              "médiane géométrique de 60 villes.",
              exercises=[M07_33, M07_34, M07_35])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M07.1 à M07.13, M07.19 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M07 · Vecteurs et géométrie de ℝⁿ — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m07_vecteurs_rn/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M07`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M07 · Vecteurs et géométrie de ℝⁿ — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : combinaisons linéaires et one-hot, produits scalaires, "
               "normes et distances, cosinus, projection, hyperplans, score linéaire, barycentre et inertie, "
               "silhouette, k-means++, diagonale du cube, distance moyenne dans le cube, unités et plus proche voisin.\n"
               "- Écrire les sept fonctions de `mymath/vectors.py` et les tester, puis comparer avec NumPy et SciPy.\n"
               "- Prédire l'angle de deux vecteurs aléatoires, mesurer la concentration de la norme, comparer médiane "
               "et moyenne, tracer les boules unités, chasser des erreurs, vectoriser des normes, trouver une médiane "
               "géométrique.\n\n"
               "**Rappel express.** $\\mathbf{u} \\cdot \\mathbf{v} = \\sum u_i v_i$ ; $\\lVert \\mathbf{x} \\rVert_1 = \\sum "
               "|x_i|$, $\\lVert \\mathbf{x} \\rVert_2 = \\sqrt{\\sum x_i^2}$, $\\lVert \\mathbf{x} \\rVert_\\infty = \\max |x_i|$ ; "
               "$\\cos\\theta = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{\\lVert \\mathbf{u} \\rVert\\,\\lVert \\mathbf{v} \\rVert}$ ; "
               "projection $\\frac{\\mathbf{x} \\cdot \\mathbf{u}}{\\mathbf{u} \\cdot \\mathbf{u}}\\,\\mathbf{u}$ ; distance à "
               "l'hyperplan $\\frac{|\\mathbf{w} \\cdot \\mathbf{x} + b|}{\\lVert \\mathbf{w} \\rVert}$ ; $\\sum \\lVert "
               "\\mathbf{x}_i - \\mathbf{c} \\rVert^2 = \\sum \\lVert \\mathbf{x}_i - \\bar{\\mathbf{x}} \\rVert^2 + m\\,\\lVert "
               "\\bar{\\mathbf{x}} - \\mathbf{c} \\rVert^2$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu calculer un produit scalaire, les normes L1, L2 et L∞ et une distance en dimension $n$ ?\n"
               "2. Sais-tu calculer un cosinus et une projection, et démontrer l'inégalité de Cauchy-Schwarz ?\n"
               "3. Sais-tu dire de quel côté d'un hyperplan est un point, et calculer sa distance à l'hyperplan ?\n"
               "4. Sais-tu pourquoi le barycentre minimise l'inertie, et ce que font k-means, la silhouette et "
               "k-means++ ?\n"
               "5. Sais-tu ce qui change en grande dimension ?\n\n"
               "**La suite** : le chapitre 7 de workbookIA (classification, k-means, malédiction de la dimension), "
               "puis M08, les tests statistiques.")]


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
