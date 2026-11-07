#!/usr/bin/env python
"""Build the two notebooks of chapter M03 from a single source (used by Claude).

    python tools/chapters/build_m03.py
    python tools/run_all_notebooks.py chapitres/m03_probabilites_conditionnelles/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m03_probabilites_conditionnelles/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M03.1 to M03.11, 🔗 M03.14 and M03.15); parts A to C are the notebook
exercises. Wrong-answer messages state a rule, never a number of the answer nor the calculation that gives it. The
data of the notebook are new (a 2 × 3 table of app usage, scores of an imaginary model, dice drawn once with a seeded
generator): none is a test case of tests/test_m03_conditional.py, an answer of the paper exercises, or an example of
workbookIA 3.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M03"
FOLDER = "chapitres/m03_probabilites_conditionnelles"

F = 'kind="fraction", simplified=True'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M03.1", "Un tableau de contingence : jointes, marginales, conditionnelles", [
        ("a", "a number (2 decimals)", "120 / 400",
         'decimals=2, mistakes={"« avec photo » : la première colonne du tableau": 280 / 400}'),
        ("b", "a number (2 decimals)", "220 / 400",
         'decimals=2, mistakes={"« 4 ou 5 étoiles » : la dernière ligne du tableau": {80 / 400, 100 / 400}}'),
        ("c", "a number (3 decimals)", "70 / 400",
         'decimals=3, mistakes={"une probabilité jointe divise la case par le total du tableau, pas par le total '
         'd\'une ligne ou d\'une colonne": {70 / 120, 70 / 220}}'),
        ("d", "a number (3 decimals)", "70 / 120",
         'decimals=3, mistakes={"« sachant avec photo » : on ne garde que les avis avec photo, donc on divise par le '
         'total de leur colonne": 70 / 220, "une probabilité conditionnelle divise par la probabilité de l\'événement '
         '« sachant », pas par le total du tableau": 70 / 400}'),
        ("e", "a number (3 decimals)", "70 / 220",
         'decimals=3, mistakes={"« sachant 4 ou 5 étoiles » : on ne garde que ces avis, donc on divise par le total '
         'de leur ligne": 70 / 120, "une probabilité conditionnelle divise par la probabilité de l\'événement '
         '« sachant », pas par le total du tableau": 70 / 400}'),
        ("f", "a number (3 decimals)", "30 / 80",
         'decimals=3, mistakes={"« sachant 1 ou 2 étoiles » : on ne garde que ces avis, donc on divise par le total '
         'de leur ligne": 30 / 120, "une probabilité conditionnelle divise par la probabilité de l\'événement '
         '« sachant », pas par le total du tableau": 30 / 400}'),
        ("g", "a list of 3 numbers (3 decimals)", "[30 / 120, 20 / 120, 70 / 120]",
         'decimals=3, mistakes={"une loi conditionnelle a une somme de 1 : divise la colonne « avec photo » par son '
         'total, pas par le total du tableau": [30 / 400, 20 / 400, 70 / 400], "chaque case de la colonne se divise '
         'par le total de la colonne, pas par celui de sa ligne": [30 / 80, 20 / 100, 70 / 220]}'),
        ("h", "a number (3 decimals)", "(80 + 120 - 30) / 400",
         'decimals=3, mistakes={"les avis à la fois 1 ou 2 étoiles et avec photo ont été comptés deux fois": '
         '200 / 400, "« ou » contient aussi les avis qui ont les deux": 30 / 400}'),
    ]),

    Paper("M03.2", "L'indépendance, vérifiée dans un tableau", [
        ("a", "a number (2 decimals)", "80 / 1000", 'decimals=2'),
        ("b", "a number (2 decimals)", "32 / 400",
         'decimals=2, mistakes={"« sachant version B » : on ne garde que les visiteurs de la version B, donc on divise '
         'par le total de leur ligne": 32 / 80, "une probabilité conditionnelle divise par la probabilité de '
         'l\'événement « sachant », pas par le total du tableau": 32 / 1000}'),
        ("c", "True or False", "True",
         'mistakes={"compare la probabilité de clic dans chaque version à la probabilité de clic globale": False}'),
        ("d", "a number (2 decimals)", "90 / 500", 'decimals=2'),
        ("e", "a number (3 decimals)", "200 / 500 * 90 / 500",
         'decimals=3, mistakes={"« matin » : la première ligne du tableau 2": 300 / 500 * 90 / 500}'),
        ("f", "a number (2 decimals)", "30 / 500",
         'decimals=2, mistakes={"une probabilité jointe divise la case par le total du tableau": {30 / 200, 30 / 90}}'),
        ("g", "True or False", "False", 'mistakes={"compare f) à e) : la case et le produit des marges": True}'),
        ("h", "an integer", "54",
         'mistakes={"c\'est l\'effectif observé ; l\'effectif attendu se calcule avec les seuls totaux": 60}'),
    ]),

    Paper("M03.3", "Probabilités totales avec trois cas", [
        ("a", "a number (4 decimals)", "0.45 * 0.01 + 0.35 * 0.02 + 0.2 * 0.04",
         'decimals=4, mistakes={"les taux se pondèrent par la part du trafic de chaque serveur, pas par 1/3": '
         '(0.01 + 0.02 + 0.04) / 3, "additionner les taux oublie les parts du trafic : chaque taux est une '
         'probabilité sachant le serveur": 0.07}'),
        ("b", "a number (3 decimals)", "0.2 * 0.04",
         'decimals=3, mistakes={"c\'est P(E | S₃) ; la probabilité de l\'intersection utilise la règle du produit": '
         '0.04}'),
        ("c", "a number (4 decimals)", "1 - (0.45 * 0.01 + 0.35 * 0.02 + 0.2 * 0.04)",
         'decimals=4, mistakes={"l\'événement contraire de E, sur toutes les requêtes": 0.93}'),
        ("d", "an integer", "195",
         'mistakes={"une moyenne sur toutes les requêtes, avec les parts du trafic": 233, '
         '"les requêtes en erreur, pas celles qui réussissent": 9805}'),
        ("e", "a number (2 decimals)", "0.008 / 0.0195",
         'decimals=2, mistakes={"P(S₃ | E) n\'est pas P(E | S₃) : parmi les requêtes en erreur, quelle part vient de '
         'S₃ ?": 0.04, "la part de S₃ dans le trafic n\'est pas sa part parmi les requêtes en erreur": 0.2}'),
        ("f", "a number (4 decimals)", "0.45 * 0.01 + 0.35 * 0.02 + 0.2 * 0.02", 'decimals=4'),
        ("g", "a number (4 decimals)", "0.45 * 0.01 + 0.45 * 0.02 + 0.1 * 0.04",
         'decimals=4, mistakes={"la moitié seulement du trafic de S₃ change de serveur": 0.45 * 0.01 + 0.55 * 0.02}'),
        ("h", "an integer", "45",
         'mistakes={"S₁ ne traite qu\'une partie des 10 000 requêtes": 100}'),
    ]),

    Paper("M03.4", "Une matrice de confusion lue comme des probabilités", [
        ("a", "a number (2 decimals)", "80 / 2000",
         'decimals=2, mistakes={"la prévalence compte les pièces vraiment défectueuses, pas les pièces signalées": '
         '160 / 2000}'),
        ("b", "a number (2 decimals)", "64 / 80",
         'decimals=2, mistakes={"le recall conditionne par la vérité : parmi les pièces vraiment défectueuses": '
         '64 / 160}'),
        ("c", "a number (2 decimals)", "1824 / 1920",
         'decimals=2, mistakes={"c\'est le taux de faux positifs ; la spécificité est son complément": 96 / 1920, '
         '"la spécificité conditionne par la vérité : parmi les pièces vraiment saines": 1824 / 1840}'),
        ("d", "a number (2 decimals)", "64 / 160",
         'decimals=2, mistakes={"la precision conditionne par la prédiction : parmi les pièces signalées": 64 / 80}'),
        ("e", "a number (3 decimals)", "(64 + 1824) / 2000",
         'decimals=3, mistakes={"l\'accuracy compte les bonnes réponses des deux sortes : les vrais positifs et les '
         'vrais négatifs": {64 / 2000, 1824 / 2000}}'),
        ("f", "a number (4 decimals)", "1824 / 1840",
         'decimals=4, mistakes={"la valeur prédictive négative conditionne par la prédiction : parmi les pièces non '
         'signalées": 1824 / 1920}'),
        ("g", "a number (2 decimals)", "160 / 2000",
         'decimals=2, mistakes={"les pièces signalées, pas les pièces défectueuses": 80 / 2000}'),
        ("h", "a number (4 decimals)", "2 * 64 / (2 * 64 + 96 + 16)",
         'decimals=4, mistakes={"le F1 est la moyenne harmonique de la precision et du recall, pas leur moyenne '
         'arithmétique": 0.6}'),
    ]),

    Paper("M03.5", "F-beta : quel β pour quel coût d'erreur ?", [
        ("a", "a number (4 decimals)", "2 * 0.6 * 0.9 / (0.6 + 0.9)",
         'decimals=4, mistakes={"le F1 est la moyenne harmonique, pas la moyenne arithmétique": 0.75}'),
        ("b", "a number (4 decimals)", "5 * 0.6 * 0.9 / (4 * 0.6 + 0.9)",
         'decimals=4, mistakes={"relis la formule de F_β : β y apparaît au carré": 3 * 0.6 * 0.9 / (2 * 0.6 + 0.9), '
         '"au dénominateur de la formule avec P et R, β² multiplie la precision": 5 * 0.6 * 0.9 / (0.6 + 4 * 0.9)}'),
        ("c", "a number (4 decimals)", "1.25 * 0.6 * 0.9 / (0.25 * 0.6 + 0.9)",
         'decimals=4, mistakes={"relis la formule de F_β : β y apparaît au carré": 1.5 * 0.6 * 0.9 / (0.5 * 0.6 + 0.9)}'),
        ("d", "an integer", "3",
         'mistakes={"relis la formule avec les comptages : comment β intervient-il devant FN ?": 9}'),
        ("e", "a number (2 decimals)", "4 / 5",
         'decimals=2, mistakes={"c\'est le poids de la precision ; celui du recall est l\'autre": 1 / 5}'),
        ("f", "a number (2 decimals)", "0.9",
         'decimals=2, mistakes={"quand β grandit, tout le poids va au recall, pas à la precision": 0.6, '
         '"F_β reste entre la precision et le recall": 1.0}'),
        ("g", "a number (4 decimals)", "5 * 0.9 * 0.6 / (4 * 0.9 + 0.6)",
         'decimals=4, mistakes={"recalcule avec la precision et le recall du modèle B": 5 * 0.6 * 0.9 / (4 * 0.6 + 0.9)}'),
        ("h", "a letter, as text", '"A"', 'mistakes={"compare les F_β des deux modèles pour un β plus grand que 1": "B"}'),
    ]),

    Paper("M03.6", "Balanced accuracy et MCC sur un problème déséquilibré", [
        ("a", "a number (2 decimals)", "950 / 1000", 'decimals=2'),
        ("b", "a number (2 decimals)", "(0 + 1) / 2",
         'decimals=2, mistakes={"la balanced accuracy fait la moyenne des recalls des deux classes, pas la proportion '
         'de bonnes réponses": 0.95}'),
        ("c", "a number (2 decimals)", "(35 + 865) / 1000",
         'decimals=2, mistakes={"le modèle B signale 120 clients : les 85 signalés à tort sont des erreurs": 0.985}'),
        ("d", "a number (2 decimals)", "35 / 50",
         'decimals=2, mistakes={"le recall conditionne par la vérité : parmi les 50 clients qui ont résilié": 35 / 120}'),
        ("e", "a number (4 decimals)", "865 / 950",
         'decimals=4, mistakes={"la spécificité conditionne par la vérité : parmi les 950 clients restés": 865 / 880}'),
        ("f", "a number (4 decimals)", "(35 / 50 + 865 / 950) / 2",
         'decimals=4, mistakes={"la moyenne du recall de chaque classe : le recall des positifs et la spécificité": '
         '(35 / 50 + 0.9) / 2}'),
        ("g", "a number (3 decimals)", "(35 * 865 - 85 * 15) / math.sqrt(120 * 50 * 950 * 880)",
         'decimals=3, mistakes={"au numérateur, TP × TN moins FP × FN": (35 * 865 + 85 * 15) / math.sqrt(120 * 50 * 950 '
         '* 880)}'),
        ("h", "a number (4 decimals)", "35 / 120",
         'decimals=4, mistakes={"la precision conditionne par la prédiction : parmi les 120 clients signalés": 35 / 50}'),
    ]),

    Paper("M03.7", "Changer de population : recalculer la precision quand la prévalence change", [
        ("a", "a number (4 decimals)", "0.9 * 0.2 / (0.9 * 0.2 + 0.02 * 0.8)",
         'decimals=4, mistakes={"la precision n\'est ni le recall ni la spécificité": {0.9, 0.98}}'),
        ("b", "a number (4 decimals)", "0.9 * 0.02 / (0.9 * 0.02 + 0.02 * 0.98)",
         'decimals=4, mistakes={"recalcule avec la prévalence de la production": 0.9 * 0.2 / (0.9 * 0.2 + 0.02 * 0.8), '
         '"la precision n\'est ni le recall ni la spécificité": {0.9, 0.98}}'),
        ("c", "an integer", "180",
         'mistakes={"le recall s\'applique aux seuls comptes piratés": 9000}'),
        ("d", "an integer", "196",
         'mistakes={"les faux positifs viennent des seuls comptes non piratés": 200}'),
        ("e", "a number (3 decimals)", "9604 / 9624", 'decimals=3'),
        ("f", "a number (4 decimals)", "(180 + 9604) / 10_000",
         'decimals=4, mistakes={"l\'accuracy compte les vrais positifs et les vrais négatifs": 9604 / 10_000}'),
        ("g", "a number (4 decimals)", "0.016 / 0.196", 'decimals=4'),
        ("h", "a number (4 decimals)", "1 - 45 / 9800",
         'decimals=4, mistakes={"c\'est le taux de faux positifs ; la spécificité est son complément": 45 / 9800}'),
    ]),

    Paper("M03.8", "Une courbe ROC à la main, et son aire par les trapèzes", [
        ("a", "an integer", "11",
         'mistakes={"compte un point par score, et le point de départ (0, 0) avant tout seuil": {9, 10}}'),
        ("b", "a list [FPR, recall] (2 decimals)", "[1 / 5, 3 / 5]",
         'decimals=2, mistakes={"l\'ordre est [FPR, recall] : l\'abscisse d\'abord": [3 / 5, 1 / 5]}'),
        ("c", "a list [FPR, recall] (2 decimals)", "[2 / 5, 4 / 5]",
         'decimals=2, mistakes={"l\'ordre est [FPR, recall] : l\'abscisse d\'abord": [4 / 5, 2 / 5]}'),
        ("d", "a number (2 decimals)", "20 / 25", 'decimals=2'),
        ("e", "a number (2 decimals)", "2 / 5", 'decimals=2'),
        ("f", "a number (2 decimals)", "3 / 5", 'decimals=2'),
        ("g", "a number (4 decimals)", "20 / 30",
         'decimals=4, mistakes={"le nouveau négatif a un score plus élevé que des positifs : l\'AUC ne peut pas '
         'rester la même": 0.8}'),
        ("h", "a number (2 decimals)", "22 / 25", 'decimals=2'),
    ]),

    Paper("M03.9", "L'AUC comme proportion de paires bien classées", [
        ("a", "an integer", "12", 'mistakes={"une paire associe un positif et un négatif : 4 × 3 paires": 7}'),
        ("b", "an integer", "2", ''),
        ("c", "an integer", "8", ''),
        ("d", "a number (2 decimals)", "9 / 12",
         'decimals=2, mistakes={"relis la fiche : combien compte une paire ex æquo ?": {8 / 12, 10 / 12}}'),
        ("e", "a number (2 decimals)", "3 / 12", 'decimals=2'),
        ("f", "a number (4 decimals)", "11 / 15", 'decimals=4'),
        ("g", "a number (4 decimals)", "2 / 12", 'decimals=4'),
    ]),

    Paper("M03.10", "Courbe precision-recall et average precision à la main", [
        ("a", "a list [precision, recall] (4 decimals)", "[2 / 3, 2 / 3]", 'decimals=4'),
        ("b", "a list [precision, recall] (4 decimals)", "[3 / 5, 1.0]",
         'decimals=4, mistakes={"l\'ordre est [precision, recall]": [1.0, 3 / 5]}'),
        ("c", "an irreducible fraction, as text", "Fraction(3, 7)", F),
        ("d", "a number (4 decimals)", "34 / 45",
         'decimals=4, mistakes={"l\'average precision utilise des rectangles (chaque gain de recall fois la precision '
         'atteinte), pas des trapèzes": 1 / 3 + (1 / 3) * (0.5 + 2 / 3) / 2 + (1 / 3) * (0.5 + 0.6) / 2, '
         '"seuls les seuils où le recall augmente comptent": (1 + 0.5 + 2 / 3 + 0.5 + 0.6 + 0.5 + 3 / 7) / 7}'),
        ("e", "an irreducible fraction, as text", "Fraction(34, 45)", F),
        ("f", "a number (2 decimals)", "0.75", 'decimals=2'),
        ("g", "a number (2 decimals)", "0.5", 'decimals=2, mistakes={"c\'est le F1 ; la question demande le seuil qui le donne": 0.75}'),
        ("h", "a number (4 decimals)", "(1 + 1 + 3 / 4) / 3", 'decimals=4'),
    ]),

    Paper("M03.11", "Score de Brier et calibration de huit prévisions", [
        ("a", "a number (3 decimals)", "1.0 / 8",
         'decimals=3, mistakes={"le score de Brier fait la moyenne des carrés des écarts, pas des écarts": 2.4 / 8}'),
        ("b", "a number (3 decimals)", "0.25", 'decimals=3'),
        ("c", "a number (3 decimals)", "3 / 8 * 5 / 8", 'decimals=3'),
        ("d", "a number (2 decimals)", "0.75", 'decimals=2'),
        ("e", "a number (2 decimals)", "0.75", 'decimals=2'),
        ("f", "a number (2 decimals)", "0.25", 'decimals=2'),
        ("g", "a number (2 decimals)", "0.0", 'decimals=2'),
        ("h", "a number (2 decimals)", "0.49",
         'decimals=2, mistakes={"une contribution est un carré : (p_i − y_i)²": 0.7}'),
    ]),

    Paper("M03.14", "Un seuil sur un score : trois seuils, trois matrices de confusion", [
        ("a", "an integer", "4", 'mistakes={"au seuil 0,5, un score égal ou supérieur à 0,5 est déclaré positif": 3}'),
        ("b", "an integer", "1", ''),
        ("c", "an irreducible fraction, as text", "Fraction(2, 3)",
         F + ', mistakes={"la precision divise par le nombre de colis signalés, pas par celui des colis mal '
         'adressés": "2/5"}'),
        ("d", "a number (2 decimals)", "0.4",
         'decimals=2, mistakes={"le recall divise par le nombre de colis vraiment mal adressés": 2 / 3}'),
        ("e", "a list [precision, recall] (3 decimals)", "[5 / 8, 1.0]",
         'decimals=3, mistakes={"l\'ordre est [precision, recall]": [1.0, 5 / 8]}'),
        ("f", "a number (1 decimal)", "0.5", 'decimals=1'),
        ("g", "an integer", "4",
         'mistakes={"chaque sorte d\'erreur se multiplie par son propre coût": 2}'),
        ("h", "a number (1 decimal)", "0.3",
         'decimals=1, mistakes={"compare les coûts totaux des trois seuils (pas leurs F1), chaque sorte d\'erreur avec son '
         'propre coût": 0.5}'),
    ]),

    Paper("M03.15", "Équité : les taux de faux positifs de deux groupes", [
        ("a", "a number (2 decimals)", "28 / 140",
         'decimals=2, mistakes={"le taux de faux positifs conditionne par la vérité : parmi les comptes qui ne sont '
         'pas des robots": 28 / 76}'),
        ("b", "a number (2 decimals)", "18 / 180",
         'decimals=2, mistakes={"le taux de faux positifs conditionne par la vérité : parmi les comptes qui ne sont '
         'pas des robots": 18 / 34}'),
        ("c", "a number (2 decimals)", "16 / 20", 'decimals=2'),
        ("d", "a number (4 decimals)", "48 / 76",
         'decimals=4, mistakes={"la precision conditionne par la prédiction : parmi les comptes signalés": 48 / 60}'),
        ("e", "a number (4 decimals)", "16 / 34",
         'decimals=4, mistakes={"la precision conditionne par la prédiction : parmi les comptes signalés": 16 / 20}'),
        ("f", "a number (2 decimals)", "76 / 200",
         'decimals=2, mistakes={"les comptes signalés, vrais positifs et faux positifs ensemble": 60 / 200}'),
        ("g", "True or False", "False",
         'mistakes={"compare les deux taux, recall et taux de faux positifs, groupe par groupe": True}'),
        ("h", "a number (4 decimals)", "(20 / 180) * (28 / 48) * 0.8", 'decimals=4'),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math
from fractions import Fraction'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M03.1 à M03.11, 🔗 M03.14 et M03.15)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"7/9\"` ;\n"
               "- une liste `[-1.5, 2.5]`, `True` / `False`, ou une lettre entre guillemets, `\"B\"`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M03.19 to M03.22)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import average_precision_score, balanced_accuracy_score, roc_auc_score, roc_curve

from wbm.nbtools import checked, drawn, run_pytest_group, verdict


def raised(function, *args):
    """The name of the exception that function(*args) raises, or "aucune" if it returns.

    NotImplementedError (a TODO not done yet) goes through, for wbm.attempt to show ⏳; so do the errors of a code
    that cannot run (a missing import, a misspelt name such as ValueErorr), for the check to name them."""
    try:
        function(*args)
    except (NotImplementedError, NameError, AttributeError, ImportError):
        raise
    except Exception as exc:  # noqa: BLE001 - any other error is the answer
        return type(exc).__name__
    return "aucune"'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M03")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M02c). Ouvre ta copie `mon_travail/mymath/conditional.py`, lis la "
         "docstring de la fonction en entier, remplace la ligne `raise NotImplementedError(...)` par ton code, "
         "**enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "NumPy est permis (importe-le en haut du fichier), scikit-learn non : les tests comparent tes résultats à "
         "lui, et un test vérifie que tu ne t'en sers pas. Une loi jointe est un tableau à deux dimensions : la "
         "ligne `i` est la valeur $x_i$ de $X$, la colonne `j` la valeur $y_j$ de $Y$. Les tableaux renvoyés sont des "
         "arrays NumPy de `float`, les nombres des `float` ou des `bool` de Python.")

WRONG_ERROR = "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)"
OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ZeroDivisionError"]


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of conditional.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m03_conditional.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m03_conditional.py", "{keyword}", impl="ref")')]


TABLE_19 = "TABLE_19 = [[45, 30, 25], [15, 45, 40]]   # rows: free trial, paid plan; columns: never, sometimes, often"

M03_19 = Ex(
    "M03.19", "🔨", 1, 20, "Jointe, marginales et conditionnelles à partir d'un tableau de comptages · "
    "`joint_from_counts, marginal, conditional`",
    "programmer le passage d'un tableau de comptages à la loi jointe, ses marginales et ses lois conditionnelles, "
    "avec leurs cas d'erreur.", "fiche §1 et §2", tracks="C, E", mymath="conditional.py",
    body=HOWTO + """

Écris, dans cet ordre (fiche §1 et §2) :
- `joint_from_counts(counts)` : chaque comptage divisé par le total ; une `ValueError` si le tableau n'a pas deux dimensions, a un comptage négatif, ou ne contient que des zéros ;
- `marginal(joint, axis)` : la convention de `np.sum(joint, axis=axis)`, donc `axis=0` donne la loi de $Y$ (une probabilité par **colonne**) et `axis=1` celle de $X$ (une par **ligne**) ; une `ValueError` si `joint` n'est pas une loi jointe valide (des cases positives de somme 1, à $10^{-9}$ près) ou si `axis` ne vaut ni 0 ni 1 ;
- `conditional(joint, given_row=None, given_column=None)` : la loi de $Y$ sachant $X = x_i$ (la ligne `i` divisée par sa somme), ou celle de $X$ sachant $Y = y_j$ ; une `ValueError` si l'on donne les deux indices ou aucun, si l'indice sort du tableau, ou si l'événement de la condition a une probabilité nulle. Un indice est dans le tableau s'il va de 0 au nombre de lignes (ou de colonnes) moins 1.

Une fonction auxiliaire `_check_joint(joint)`, qui convertit et vérifie une loi jointe, évite d'écrire trois fois les mêmes vérifications.

La vérification utilise `TABLE_19`, les 200 utilisateurs d'une application de cuisine, selon leur formule (essai gratuit ou abonnement payant, en lignes) et leur usage du minuteur intégré (jamais, parfois, souvent, en colonnes). Elle calcule :
- a) la loi jointe, `joint_from_counts(TABLE_19)` (3 décimales) ;
- b) sa marginale avec `axis=0` (3 décimales) ;
- c) sa marginale avec `axis=1` (3 décimales) ;
- d) la loi de l'usage sachant « essai gratuit », `given_row=0` (3 décimales) ;
- e) la loi de la formule sachant « souvent », `given_column=2` (3 décimales) ;
- f) le nom de l'erreur levée par `joint_from_counts([[1, -2], [3, 4]])` ;
- g) le nom de l'erreur levée par `conditional(joint, 0, 1)`, avec les deux indices ;
- h) le nom de l'erreur levée par `marginal([[0.5, 0.6], [0.1, 0.2]], 0)`.

Dans ta copie : refais a), d) et e) à la main sur le tableau. Lequel des deux, b) ou c), est la loi de la formule ?""",
    given=TABLE_19,
    todo=LOAD_LEARNER,
    check='''with checked("M03.19a"):
    wbm.check("M03.19a", mymath.conditional.joint_from_counts(TABLE_19), computed=True)
joint_19 = np.array(TABLE_19) / np.sum(TABLE_19)     # the right joint law, so that b) to h) do not depend on a)
with checked("M03.19b"):
    wbm.check("M03.19b", mymath.conditional.marginal(joint_19, 0), computed=True)
with checked("M03.19c"):
    wbm.check("M03.19c", mymath.conditional.marginal(joint_19, 1), computed=True)
with checked("M03.19d"):
    wbm.check("M03.19d", mymath.conditional.conditional(joint_19, given_row=0), computed=True)
with checked("M03.19e"):
    wbm.check("M03.19e", mymath.conditional.conditional(joint_19, given_column=2), computed=True)
with checked("M03.19f"):
    wbm.check("M03.19f", raised(mymath.conditional.joint_from_counts, [[1, -2], [3, 4]]), computed=True)
with checked("M03.19g"):
    wbm.check("M03.19g", raised(mymath.conditional.conditional, joint_19, 0, 1), computed=True)
with checked("M03.19h"):
    wbm.check("M03.19h", raised(mymath.conditional.marginal, [[0.5, 0.6], [0.1, 0.2]], 0), computed=True)''',
    solution=LOAD_REF + '''
cond = mymath.conditional
joint_19 = cond.joint_from_counts(TABLE_19)
print("a)", joint_19.round(3).tolist())
print("b)", cond.marginal(joint_19, 0), " c)", cond.marginal(joint_19, 1))
print("d)", cond.conditional(joint_19, given_row=0), " e)", cond.conditional(joint_19, given_column=2).round(4))
print("f)", raised(cond.joint_from_counts, [[1, -2], [3, 4]]), " g)", raised(cond.conditional, joint_19, 0, 1),
      " h)", raised(cond.marginal, [[0.5, 0.6], [0.1, 0.2]], 0))''',
    record=f'''wbm.record("M03.19a", [[0.225, 0.15, 0.125], [0.075, 0.225, 0.2]], decimals=3,
           mistakes={{"chaque comptage se divise par le total du tableau, pas par celui de sa ligne":
                         [[0.45, 0.3, 0.25], [0.15, 0.45, 0.4]],
                     "chaque comptage se divise par le total du tableau, pas par celui de sa colonne":
                         [[0.75, 0.4, 25 / 65], [0.25, 0.6, 40 / 65]]}})
wbm.record("M03.19b", [0.3, 0.375, 0.325], decimals=3,
           mistakes={{"axis=0 donne la loi de Y : une probabilité par colonne (la convention de np.sum)": [0.5, 0.5]}})
wbm.record("M03.19c", [0.5, 0.5], decimals=3,
           mistakes={{"axis=1 donne la loi de X : une probabilité par ligne (la convention de np.sum)":
                         [0.3, 0.375, 0.325]}})
wbm.record("M03.19d", [0.45, 0.3, 0.25], decimals=3,
           mistakes={{"une loi conditionnelle a une somme de 1 : divise la ligne par sa somme, P(X = x_i)":
                         [0.225, 0.15, 0.125],
                     "given_row=i conditionne par X = x_i : la ligne i du tableau, pas sa colonne i": [0.75, 0.25]}})
wbm.record("M03.19e", [25 / 65, 40 / 65], decimals=3,
           mistakes={{"une loi conditionnelle a une somme de 1 : divise la colonne par sa somme, P(Y = y_j)":
                         [0.125, 0.2]}})
wbm.record("M03.19f", "ValueError",
           mistakes={{"un comptage négatif est impossible : lève une ValueError": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M03.19g", "ValueError",
           mistakes={{"la docstring demande exactement un des deux indices : avec les deux, lève une ValueError":
                         "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M03.19h", "ValueError",
           mistakes={{"une loi jointe a une somme de 1 : vérifie-la avant de calculer la marginale": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})''',
    after=tests_cells("test_joint_from_counts_ or test_marginal_ or test_conditional_"),
    note="a) $\\frac{45}{200} = 0{,}225$, etc. b) La loi de l'usage du minuteur (une probabilité par colonne) : "
         "$\\frac{60}{200}$, $\\frac{75}{200}$, $\\frac{65}{200}$. c) La loi de la formule : 100 utilisateurs de chaque "
         "sorte. d) La ligne « essai gratuit » divisée par son total, 100. e) La colonne « souvent » divisée par son "
         "total, 65 : $\\frac{25}{65} \\approx 0{,}385$ et $\\frac{40}{65} \\approx 0{,}615$. Parmi les utilisateurs qui se "
         "servent souvent du minuteur, près de deux sur trois sont abonnés, alors que les abonnés ne sont que la "
         "moitié des utilisateurs : les deux variables sont dépendantes (M03.20).",
)

M03_20 = Ex(
    "M03.20", "🔨", 1, 15, "Tester l'indépendance avec une tolérance · `are_independent`",
    "décider si deux variables sont indépendantes en comparant chaque case de leur loi jointe au produit de ses "
    "marginales, avec une tolérance.", "fiche §2 ; Ex M03.19", tracks="C", mymath="conditional.py",
    body="""Écris `are_independent(joint, tol=1e-9)` (fiche §2) : `True` si **chaque** case de la loi jointe diffère du produit de ses deux marginales d'au plus `tol`, `False` sinon. `np.outer(a, b)` construit d'un coup le tableau de tous les produits `a[i] * b[j]`. Le résultat est un `bool` de Python (`bool(...)` convertit un booléen de NumPy) ; une loi jointe invalide lève une `ValueError`. Ta fonction peut appeler `marginal`.

La vérification calcule :
- a) `are_independent` pour la loi jointe de `TABLE_19` ;
- b) pour la loi `np.outer([0.3, 0.7], [0.2, 0.5, 0.3])`, construite indépendante par le calcul en flottants ;
- c) pour la loi `TABLE_20`, issue d'un échantillon de 1 000 personnes, avec la tolérance par défaut ;
- d) pour `TABLE_20` avec `tol=0.005` ;
- e) pour la loi `[[0.1, 0.2, 0.2], [0.1, 0.1, 0.3]]` ;
- f) `isinstance(résultat, bool)` : le résultat est-il un `bool` de Python ? (Le nom du type ne suffit pas : depuis NumPy 2, celui d'un booléen de NumPy s'écrit aussi `bool`.)
- g) le nom de l'erreur levée pour `[[0.5, 0.5], [0.5, 0.5]]` ;
- h) `are_independent` pour `TABLE_20H`, dont chaque case s'écarte de $2 \\times 10^{-6}$ du produit de ses marges, avec la tolérance par défaut.

Dans ta copie : pour la loi de e), compare la première case au produit de ses marges, puis les autres. Pour `TABLE_20`, de combien chaque case s'écarte-t-elle du produit ? Sur des données réelles, pourquoi ne trouve-t-on jamais une indépendance exacte, et que faudrait-il pour décider (fiche §2) ?""",
    given=("TABLE_20 = np.array([[61, 139], [239, 561]]) / 1000   # a sample of 1 000 people: a joint law estimated from counts\n"
           "TABLE_20H = np.outer([0.5, 0.5], [0.5, 0.5]) + np.array([[2e-6, -2e-6], [-2e-6, 2e-6]])   # gaps of 2e-6"),
    todo=LOAD_LEARNER,
    check='''joint_19 = np.array(TABLE_19) / np.sum(TABLE_19)
with checked("M03.20a"):
    wbm.check("M03.20a", mymath.conditional.are_independent(joint_19), computed=True)
with checked("M03.20b"):
    wbm.check("M03.20b", mymath.conditional.are_independent(np.outer([0.3, 0.7], [0.2, 0.5, 0.3])), computed=True)
with checked("M03.20c"):
    wbm.check("M03.20c", mymath.conditional.are_independent(TABLE_20), computed=True)
with checked("M03.20d"):
    wbm.check("M03.20d", mymath.conditional.are_independent(TABLE_20, 0.005), computed=True)
with checked("M03.20e"):
    wbm.check("M03.20e", mymath.conditional.are_independent([[0.1, 0.2, 0.2], [0.1, 0.1, 0.3]]), computed=True)
with checked("M03.20f"):
    wbm.check("M03.20f", isinstance(mymath.conditional.are_independent(joint_19), bool), computed=True)
with checked("M03.20g"):
    wbm.check("M03.20g", raised(mymath.conditional.are_independent, [[0.5, 0.5], [0.5, 0.5]]), computed=True)
with checked("M03.20h"):
    wbm.check("M03.20h", mymath.conditional.are_independent(TABLE_20H), computed=True)''',
    solution=LOAD_REF + '''
indep = mymath.conditional.are_independent
joint_19 = np.array(TABLE_19) / np.sum(TABLE_19)
outer = np.outer([0.3, 0.7], [0.2, 0.5, 0.3])
products = np.outer(TABLE_20.sum(axis=1), TABLE_20.sum(axis=0))
print("a)", indep(joint_19), " b)", indep(outer), " c)", indep(TABLE_20), " d)", indep(TABLE_20, 0.005),
      " e)", indep([[0.1, 0.2, 0.2], [0.1, 0.1, 0.3]]), " f)", isinstance(indep(joint_19), bool),
      " g)", raised(indep, [[0.5, 0.5], [0.5, 0.5]]), " h)", indep(TABLE_20H))
print("TABLE_20 minus the products of its marginals:", (TABLE_20 - products).round(4).tolist())
print("outer: largest gap to the products, in floats:",
      np.abs(outer - np.outer(outer.sum(axis=1), outer.sum(axis=0))).max())''',
    record=f'''wbm.record("M03.20a", False,
           mistakes={{"compare chaque case de la loi jointe au produit de ses deux marginales": True}})
wbm.record("M03.20b", True,
           mistakes={{"des produits calculés en flottants ne sont pas exactement égaux : compare l'écart à tol, pas "
                      "avec ==": False}})
wbm.record("M03.20c", False)
wbm.record("M03.20d", True,
           mistakes={{"tol est l'écart permis dans chaque case : |case − produit des marges| ≤ tol": False}})
wbm.record("M03.20e", False,
           mistakes={{"la première case vaut bien le produit de ses marges ; vérifie toutes les cases": True}})
wbm.record("M03.20f", True,
           mistakes={{"la docstring demande un bool de Python : bool(...) convertit un booléen de NumPy": False}})
wbm.record("M03.20g", "ValueError",
           mistakes={{"une somme de 2 n'est pas une loi jointe : lève une ValueError": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M03.20h", False,
           mistakes={{"np.allclose et np.isclose ajoutent une tolérance relative (rtol=1e-5) : compare "
                      "np.abs(table - produits) <= tol, ou passe rtol=0": True}})''',
    after=tests_cells("test_are_independent_"),
    note="b) Les sommes en flottants donnent des marges comme 0,30000000000000004 : un test `==` dirait « dépendantes » "
         "pour une loi construite indépendante, d'où la tolérance. c) et d) Chaque case de `TABLE_20` s'écarte de "
         "0,001 du produit de ses marges (0,2 et 0,8 en lignes, 0,3 et 0,7 en colonnes) : dépendantes à $10^{-9}$ "
         "près, « indépendantes » à 0,005 près. Avec 1 000 personnes, un tel écart est bien plus petit que l'aléa de "
         "l'échantillon ; le choix de la tolérance est une décision, qu'un test statistique (le $\\chi^2$, M08) rend "
         "rigoureuse. e) La première case vaut $0{,}5 \\times 0{,}2 = 0{,}1$, mais la deuxième vaut 0,2 au lieu de "
         "$0{,}5 \\times 0{,}3 = 0{,}15$ : une seule case ne suffit pas à conclure.",
)

M03_21_GIVEN = '''rng_21 = np.random.default_rng(21)
POS_21 = rng_21.normal(1.0, 1.0, 2000)     # scores of 2 000 positive examples
NEG_21 = rng_21.normal(0.0, 1.0, 3000)     # scores of 3 000 negative examples'''

M03_21 = Ex(
    "M03.21", "🔨", 2, 20, "L'AUC en comptant les paires · `auc_by_pairs`",
    "programmer l'AUC comme la proportion des paires (positif, négatif) bien classées, ex æquo compris, et la "
    "comparer à scikit-learn.", "fiche §7", tracks="C, E", mymath="conditional.py",
    body="""Écris `auc_by_pairs(scores_pos, scores_neg)` (fiche §7) : chaque paire (positif, négatif) compte 1 si le positif a le score le plus élevé, $\\frac{1}{2}$ en cas d'égalité, 0 sinon, et l'on divise le total par le nombre de paires. Une liste vide lève une `ValueError` ; le résultat est un `float` de Python. Deux boucles `for` imbriquées conviennent ; le **broadcasting** de NumPy fait mieux : `pos[:, None] - neg[None, :]` est le tableau de toutes les différences, une ligne par positif et une colonne par négatif.

La vérification calcule (4 décimales) :
- a) `auc_by_pairs([0.8, 0.6, 0.55], [0.7, 0.3])` ;
- b) `auc_by_pairs([0.5, 0.5, 0.9], [0.5, 0.1])`, avec des ex æquo ;
- c) `auc_by_pairs([3, 4], [1, 2])` ;
- d) `auc_by_pairs([1, 2], [3, 4])` ;
- e) le nom de l'erreur levée par `auc_by_pairs([], [0.2])` ;
- f) le nom du type du résultat, en texte ;
- g) l'AUC des 2 000 positifs et 3 000 négatifs de la cellule fournie (6 millions de paires).

Dans ta copie : refais a) et b) à la main, en écrivant le tableau des paires. Combien de temps prend g) avec ta méthode ? La valeur théorique de g) est $P(S_+ > S_-)$ pour $S_+ \\sim \\mathcal{N}(1, 1)$ et $S_- \\sim \\mathcal{N}(0, 1)$ indépendantes : avec M02b et M02c, montre qu'elle vaut $\\Phi\\big(\\frac{1}{\\sqrt{2}}\\big) \\approx 0{,}760$.""",
    given=M03_21_GIVEN,
    todo=LOAD_LEARNER,
    check='''with checked("M03.21a"):
    wbm.check("M03.21a", mymath.conditional.auc_by_pairs([0.8, 0.6, 0.55], [0.7, 0.3]), computed=True)
with checked("M03.21b"):
    wbm.check("M03.21b", mymath.conditional.auc_by_pairs([0.5, 0.5, 0.9], [0.5, 0.1]), computed=True)
with checked("M03.21c"):
    wbm.check("M03.21c", mymath.conditional.auc_by_pairs([3, 4], [1, 2]), computed=True)
with checked("M03.21d"):
    wbm.check("M03.21d", mymath.conditional.auc_by_pairs([1, 2], [3, 4]), computed=True)
with checked("M03.21e"):
    wbm.check("M03.21e", raised(mymath.conditional.auc_by_pairs, [], [0.2]), computed=True)
with checked("M03.21f"):
    wbm.check("M03.21f", type(mymath.conditional.auc_by_pairs([0.8], [0.3])).__name__, computed=True)
with checked("M03.21g"):
    wbm.check("M03.21g", mymath.conditional.auc_by_pairs(POS_21, NEG_21), computed=True)''',
    solution=LOAD_REF + '''
import time

auc = mymath.conditional.auc_by_pairs
start = time.perf_counter()
big = auc(POS_21, NEG_21)
seconds = time.perf_counter() - start
print("a)", auc([0.8, 0.6, 0.55], [0.7, 0.3]), " b)", auc([0.5, 0.5, 0.9], [0.5, 0.1]), " c)", auc([3, 4], [1, 2]),
      " d)", auc([1, 2], [3, 4]), " e)", raised(auc, [], [0.2]), " f)", type(auc([0.8], [0.3])).__name__)
print(f"g) {big:.6f} in {seconds:.3f} s · scikit-learn:",
      roc_auc_score(np.r_[np.ones(2000), np.zeros(3000)], np.r_[POS_21, NEG_21]))''',
    record=f'''wbm.record("M03.21a", 4 / 6, decimals=4,
           mistakes={{"une paire compte quand le positif a le score le plus élevé, pas le négatif": 2 / 6}})
wbm.record("M03.21b", 5 / 6, decimals=4,
           mistakes={{"relis la docstring : combien compte une paire ex æquo ?": {{4 / 6, 1.0}}}})
wbm.record("M03.21c", 1.0, decimals=4)
wbm.record("M03.21d", 0.0, decimals=4)
wbm.record("M03.21e", "ValueError",
           mistakes={{"une liste vide : aucune paire, lève une ValueError": {{"aucune", "ZeroDivisionError"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("M03.21f", "float",
           mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy":
                         {{"float64", "int", "ndarray"}}}})
wbm.record("M03.21g", 0.7748283333, decimals=4,
           mistakes={{"une paire compte quand le positif a le score le plus élevé, pas le négatif": 0.2251716667}})''',
    after=tests_cells("test_auc_by_pairs_"),
    note="a) Les paires bien classées : (0,8 ; 0,7), (0,8 ; 0,3), (0,6 ; 0,3), (0,55 ; 0,3) : 4 sur 6. b) Les deux "
         "positifs à 0,5 font chacun un ex æquo avec le négatif à 0,5 ($\\frac{1}{2}$) et battent 0,1 (1) ; 0,9 bat "
         "les deux négatifs : $\\frac{1{,}5 + 1{,}5 + 2}{6} = \\frac{5}{6}$. g) 0,775 ; le broadcasting traite les "
         "6 millions de paires en quelques centièmes de seconde, deux boucles Python en environ une demi-seconde. La "
         "différence $D = S_+ - S_-$ suit $\\mathcal{N}(1, 2)$ (M02b, M02c), donc $P(D > 0) = \\Phi\\big(\\frac{1}{\\sqrt{2}}"
         "\\big) \\approx 0{,}760$ : l'écart à 0,775 est l'aléa de l'échantillon.",
)

M03_22_GIVEN = '''Y_22 = np.array([1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1])                                # 6 positives, 6 negatives
S_22 = np.array([0.8, 0.8, 0.9, 0.4, 0.4, 0.5, 0.2, 0.6, 0.1, 0.15, 0.4, 0.8])     # scores rounded to 0.1 or 0.05'''

M03_22 = Ex(
    "M03.22", "📦", 1, 15, "`sklearn.metrics.roc_auc_score` contre le comptage des paires, ex æquo compris",
    "calculer avec scikit-learn l'AUC, la courbe ROC et l'average precision de scores arrondis, et relier une AUC "
    "calculée sur des prédictions 0/1 à la balanced accuracy.", "fiche §5 et §7", tracks="C",
    body="""Les fonctions de `sklearn.metrics` prennent toujours **les labels vrais d'abord**, puis les scores : `roc_auc_score(y_true, y_score)`, `roc_curve(y_true, y_score)` (qui renvoie `fpr, tpr, thresholds`), `average_precision_score(y_true, y_score)`, `balanced_accuracy_score(y_true, y_pred)`. Lis `help(roc_curve)` avant de commencer.

La cellule fournie définit `Y_22` et `S_22` : 12 exemples, dont plusieurs scores égaux. Calcule :
- a) l'AUC, `roc_auc_score` (4 décimales) ;
- b) l'AUC des scores opposés, `-S_22` (4 décimales) ;
- c) l'AUC des **prédictions** 0/1 au seuil 0,5, `(S_22 >= 0.5).astype(int)`, données à la place des scores (4 décimales) ;
- d) la balanced accuracy de ces mêmes prédictions (4 décimales) ;
- e) le nombre de seuils renvoyés par `roc_curve(Y_22, S_22)` (un entier) ;
- f) l'average precision (4 décimales).

Dans ta copie : retrouve a) en comptant les paires (ta fonction `auc_by_pairs` le fait aussi). Pourquoi c) et d) sont-ils égaux ? (Trace la courbe ROC d'un classifieur qui ne donne que 0 ou 1 : combien a-t-elle de points ?) Que vaut le premier seuil de e), et à quel point de la courbe correspond-il ?""",
    given=M03_22_GIVEN,
    todo='''answer_M03_22a = ...  # a) roc_auc_score(...)
answer_M03_22b = ...  # b) with -S_22
answer_M03_22c = ...  # c) on the 0/1 predictions at the threshold 0.5
answer_M03_22d = ...  # d) balanced_accuracy_score(...)
answer_M03_22e = ...  # e) an integer
answer_M03_22f = ...  # f) average_precision_score(...)''',
    check='''for letter, answer in zip("abcdef", [answer_M03_22a, answer_M03_22b, answer_M03_22c, answer_M03_22d,
                                     answer_M03_22e, answer_M03_22f]):
    wbm.check(f"M03.22{letter}", answer)''',
    solution='''predictions_22 = (S_22 >= 0.5).astype(int)
answer_M03_22a = roc_auc_score(Y_22, S_22)                       # the true labels first, then the scores
answer_M03_22b = roc_auc_score(Y_22, -S_22)
answer_M03_22c = roc_auc_score(Y_22, predictions_22)             # a single threshold: (TPR + 1 − FPR) / 2
answer_M03_22d = balanced_accuracy_score(Y_22, predictions_22)
fpr_22, tpr_22, thresholds_22 = roc_curve(Y_22, S_22)
answer_M03_22e = len(thresholds_22)
answer_M03_22f = average_precision_score(Y_22, S_22)
print([round(float(v), 4) for v in [answer_M03_22a, answer_M03_22b, answer_M03_22c, answer_M03_22d, answer_M03_22e,
                                     answer_M03_22f]])
print("thresholds:", thresholds_22, "· pairs:", mymath.conditional.auc_by_pairs(S_22[Y_22 == 1], S_22[Y_22 == 0]))''',
    record='''wbm.record("M03.22a", 0.7222222222, decimals=4,
           mistakes={"les labels d'abord, les scores ensuite ; et des scores, pas les prédictions 0/1":
                         {0.2777777778, 0.6666666667}})
wbm.record("M03.22b", 0.2777777778, decimals=4)
wbm.record("M03.22c", 0.6666666667, decimals=4,
           mistakes={"c) donne à roc_auc_score les prédictions 0/1 au seuil 0,5, pas les scores": 0.7222222222})
wbm.record("M03.22d", 0.6666666667, decimals=4)
wbm.record("M03.22e", 9,
           mistakes={"compte len(thresholds) renvoyé par roc_curve, et regarde son premier seuil": 8,
                     "roc_curve renvoie un seuil par score distinct (plus un premier seuil), pas un par exemple": 12})
wbm.record("M03.22f", 0.7335016835, decimals=4,
           mistakes={"c'est la prévalence, l'average precision d'un classement au hasard": 0.5,
                     "l'average precision se calcule sur les scores, pas sur les prédictions 0/1": 0.6111111111})''',
    note="a) En comptant les paires : $\\frac{26}{36} \\approx 0{,}7222$ (4 paires ex æquo comptent pour moitié). "
         "b) $1 - 0{,}7222$ : inverser les scores échange paires bien et mal classées. c) Avec des prédictions 0/1, "
         "la courbe ROC n'a que trois points, $(0, 0)$, $(\\text{FPR}, \\text{TPR})$ et $(1, 1)$, et l'aire sous ces "
         "deux segments vaut $\\frac{\\text{TPR} + 1 - \\text{FPR}}{2}$, la moyenne du recall et de la spécificité : "
         "la balanced accuracy d). Ici TPR $= \\frac{4}{6}$ et FPR $= \\frac{2}{6}$. e) 8 scores distincts, plus un "
         "premier seuil infini (aucune prédiction positive) : le point $(0, 0)$. Une AUC calculée sur des "
         "prédictions plutôt que sur des scores perd toute l'information de classement.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M03.23 to M03.25)
# ---------------------------------------------------------------------------
M03_23_EXPERIMENT = '''rng_23 = np.random.default_rng(23)
y_23 = rng_23.random(400) < 0.3                                          # 400 examples, about 30 % positive
s_23 = np.where(y_23, rng_23.beta(5, 3, 400), rng_23.beta(2, 5, 400))    # scores between 0 and 1
ranks_23 = np.argsort(np.argsort(s_23)) + 1                              # 1 for the smallest score, 400 for the largest
for name, scores in [("s", s_23), ("10 s", 10 * s_23), ("s²", s_23 ** 2), ("1 − s", 1 - s_23), ("rang", ranks_23)]:
    print(f"{name:>6} : AUC {roc_auc_score(y_23, scores):.4f}")
for name, scores in [("s", s_23), ("s²", s_23 ** 2)]:
    print(f"{name:>6} : score de Brier {np.mean((scores - y_23) ** 2):.4f}")'''

M03_23 = Ex(
    "M03.23", "🔮", 1, 10, "Prédire : l'AUC après une transformation croissante des scores",
    "prévoir l'effet d'une transformation des scores sur l'AUC et sur le score de Brier, puis le vérifier.",
    "fiche §7 et §8", tracks="C, E", hypothesis=True,
    body="""Un modèle donne à 400 exemples un score $s$ entre 0 et 1. On remplace ces scores par une transformation, et l'on recalcule l'AUC et le score de Brier. Choisis, pour chaque question :
- a) l'AUC des scores $10\\,s$ : (1) la même ; (2) multipliée par 10 ; (3) elle change, dans un sens imprévisible ; (4) elle vaut 1 ;
- b) l'AUC des scores $s^2$ : (1) la même ; (2) élevée au carré ; (3) plus petite ; (4) plus grande ;
- c) l'AUC des scores $1 - s$ : (1) la même ; (2) $1 - \\text{AUC}$ ; (3) 0,5 ; (4) 0 ;
- d) l'AUC quand chaque score est remplacé par son **rang** (1 pour le plus petit, 400 pour le plus grand) : (1) la même ; (2) elle change ; (3) elle vaut 0,5 ; (4) elle dépend du nombre d'exemples ;
- e) le score de Brier des scores $s^2$, comparé à celui des scores $s$ : (1) le même ; (2) différent.

**Avant d'exécuter quoi que ce soit**, écris tes cinq prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M03_23a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M03_23b = ...  # b) 1, 2, 3 or 4
prediction_M03_23c = ...  # c) 1, 2, 3 or 4
prediction_M03_23d = ...  # d) 1, 2, 3 or 4
prediction_M03_23e = ...  # e) 1 or 2''',
    check='''for letter, prediction in zip("abcde", [prediction_M03_23a, prediction_M03_23b, prediction_M03_23c,
                                       prediction_M03_23d, prediction_M03_23e]):
    wbm.check(f"M03.23{letter}", prediction)''',
    record='''wbm.record("M03.23a", 1, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M03.23b", 1, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M03.23c", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M03.23d", 1, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M03.23e", 2, prediction=True, choices=[1, 2])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes cinq prédictions écrites."),
        ("todo", guarded(M03_23_EXPERIMENT, ["prediction_M03_23a", "prediction_M03_23b", "prediction_M03_23c",
                                              "prediction_M03_23d", "prediction_M03_23e"],
                         "⏳ Écris d'abord tes cinq prédictions, puis exécute à nouveau.")),
        ("solution", M03_23_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : explique chaque résultat avec la lecture de l'AUC comme "
               "proportion de paires (fiche §7). Pourquoi le score de Brier, lui, change-t-il ? Que dit cette "
               "expérience de ce que mesure l'AUC, et de ce qu'elle ne mesure pas ?"),
    ],
    note="a), b), d) L'AUC compte les paires dont le positif a le score le plus élevé : une fonction strictement "
         "croissante ($10\\,s$, $s^2$ pour des scores positifs, le rang) garde l'ordre de chaque paire, donc l'AUC "
         "(0,9424 ici). c) $1 - s$ inverse l'ordre de chaque paire : les paires bien classées deviennent mal classées, "
         "et l'AUC devient $1 - 0{,}9424 = 0{,}0576$. e) Le score de Brier compare chaque score à 0 ou 1 : il dépend des "
         "**valeurs**, pas seulement de l'ordre (0,1165 puis 0,1143 ici). L'AUC mesure le classement, pas la "
         "calibration (fiche §8) ; deux modèles de même AUC peuvent donner des probabilités très différentes.",
)

M03_24_GIVEN = '''DICE_24 = np.random.default_rng(2075).integers(1, 7, (100_000, 2))   # 100 000 throws of two dice, one per row'''

M03_24 = Ex(
    "M03.24", "🔬", 2, 20, "Simuler pour estimer une probabilité conditionnelle",
    "estimer des probabilités conditionnelles par la fréquence dans des tirages simulés, et les comparer aux valeurs "
    "exactes.", "fiche §2 ; R8", tracks="C",
    body="""Pour estimer $P(A \\mid B)$ par simulation, on ne garde que les tirages où $B$ s'est produit, et l'on y compte la proportion de ceux où $A$ s'est produit aussi : c'est la définition du §2, appliquée aux fréquences. La cellule fournie lance 100 000 fois deux dés à six faces (`DICE_24`, une ligne par lancer, une colonne par dé).

Écris `conditional_frequency(event, given)`, qui reçoit deux tableaux de booléens de même longueur (un par tirage) et renvoie la fréquence de `event` parmi les tirages où `given` est vrai, en `float`. Si `given` n'est jamais vrai, la fréquence n'a pas de sens : lève une `ValueError`. Avec NumPy, `event[given]` garde les seules valeurs de `event` où `given` est vrai.

La vérification appelle ta fonction et calcule (3 décimales) :
- a) la fréquence de « la somme vaut au moins 10 » sachant « au moins un 6 » ;
- b) la fréquence de « au moins un 6 » sachant « la somme vaut au moins 10 » ;
- c) la fréquence de « le premier dé donne 6 » sachant « la somme vaut au moins 10 » ;
- d) la fréquence de « le premier dé est pair » sachant « la somme est paire » ;
- e) la fréquence de « le premier dé est pair », sans condition (`given` toujours vrai) ;
- f) le nom de l'erreur levée par `conditional_frequency(somme >= 10, somme > 12)` ;
- g) le produit a) × (fréquence de « au moins un 6 »), comparé à la fréquence de l'intersection (la règle du produit).

Dans ta copie : calcule les valeurs exactes de a) à e) en comptant les 36 issues équiprobables (a) vaut $\\frac{5}{11}$). Pourquoi a) et b) sont-ils si différents ? Que montrent d) et e) ? L'écart entre une fréquence et sa valeur exacte est-il raisonnable, compte tenu de l'erreur type d'une proportion (M02c §7) et du **nombre** de tirages où la condition est vraie ?""",
    given=M03_24_GIVEN,
    todo='''def conditional_frequency(event, given):
    """The frequency of event among the draws where given is True (two arrays of booleans, one value per draw)."""
    raise NotImplementedError("ne garde que les tirages où given est vrai, puis la proportion de event parmi eux")''',
    check='''total_24 = DICE_24.sum(axis=1)
six_24 = (DICE_24 == 6).any(axis=1)              # at least one 6
with checked("M03.24a"):
    wbm.check("M03.24a", conditional_frequency(total_24 >= 10, six_24), computed=True)
with checked("M03.24b"):
    wbm.check("M03.24b", conditional_frequency(six_24, total_24 >= 10), computed=True)
with checked("M03.24c"):
    wbm.check("M03.24c", conditional_frequency(DICE_24[:, 0] == 6, total_24 >= 10), computed=True)
with checked("M03.24d"):
    wbm.check("M03.24d", conditional_frequency(DICE_24[:, 0] % 2 == 0, total_24 % 2 == 0), computed=True)
with checked("M03.24e"):
    wbm.check("M03.24e", conditional_frequency(DICE_24[:, 0] % 2 == 0, np.ones(len(DICE_24), dtype=bool)),
              computed=True)
with checked("M03.24f"):
    wbm.check("M03.24f", raised(conditional_frequency, total_24 >= 10, total_24 > 12), computed=True)
with checked("M03.24g"):
    wbm.check("M03.24g", conditional_frequency(total_24 >= 10, six_24) * float(np.mean(six_24)), computed=True)''',
    solution='''def conditional_frequency(event, given):
    """The frequency of event among the draws where given is True (two arrays of booleans, one value per draw)."""
    event, given = np.asarray(event, dtype=bool), np.asarray(given, dtype=bool)
    if not given.any():
        raise ValueError("the condition is never true: the conditional frequency is not defined")
    return float(np.mean(event[given]))


total_24 = DICE_24.sum(axis=1)
six_24 = (DICE_24 == 6).any(axis=1)
values = [conditional_frequency(total_24 >= 10, six_24), conditional_frequency(six_24, total_24 >= 10),
          conditional_frequency(DICE_24[:, 0] == 6, total_24 >= 10),
          conditional_frequency(DICE_24[:, 0] % 2 == 0, total_24 % 2 == 0),
          conditional_frequency(DICE_24[:, 0] % 2 == 0, np.ones(len(DICE_24), dtype=bool))]
print("a) to e):", [round(v, 4) for v in values], "· exact:", [round(v, 4) for v in [5 / 11, 5 / 6, 1 / 2, 1 / 2, 1 / 2]])
print("f)", raised(conditional_frequency, total_24 >= 10, total_24 > 12),
      " g)", values[0] * float(np.mean(six_24)), "· intersection:", float(np.mean((total_24 >= 10) & six_24)),
      "· exact 5/36:", 5 / 36)
print("draws where the condition holds: at least one 6:", int(six_24.sum()), "· sum ≥ 10:", int((total_24 >= 10).sum()))''',
    record=f'''wbm.record("M03.24a", 0.4585487143, decimals=3,
           mistakes={{"divise par le nombre de tirages où la condition est vraie, pas par le nombre total de tirages":
                         0.14016,
                     "c'est l'autre probabilité conditionnelle : l'événement d'abord, la condition ensuite":
                         0.8344844010}})
wbm.record("M03.24b", 0.8344844010, decimals=3,
           mistakes={{"divise par le nombre de tirages où la condition est vraie, pas par le nombre total de tirages":
                         0.14016,
                     "c'est l'autre probabilité conditionnelle : l'événement d'abord, la condition ensuite":
                         0.4585487143}})
wbm.record("M03.24c", 0.5027982853, decimals=3,
           mistakes={{"divise par le nombre de tirages où la condition est vraie, pas par le nombre total de tirages":
                         0.08445}})
wbm.record("M03.24d", 0.5011389522, decimals=3,
           mistakes={{"divise par le nombre de tirages où la condition est vraie, pas par le nombre total de tirages":
                         0.2508}})
wbm.record("M03.24e", 0.50073, decimals=3)
wbm.record("M03.24f", "ValueError",
           mistakes={{"la condition n'est jamais vraie : lève une ValueError plutôt que de renvoyer nan":
                         {{"aucune", "ZeroDivisionError"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("M03.24g", 0.14016, decimals=3,
           mistakes={{"conditional_frequency divise par le nombre de tirages où la condition est vraie, pas par le "
                      "nombre total de tirages": 0.0428413056}})''',
    note="Valeurs exactes, sur les 36 issues : « au moins un 6 » en compte 11, dont 5 de somme au moins 10 ((4, 6), "
         "(5, 6), (6, 6), (6, 5), (6, 4)), d'où a) $\\frac{5}{11} \\approx 0{,}455$ ; « somme au moins 10 » en compte 6, "
         "dont 5 avec un 6, d'où b) $\\frac{5}{6} \\approx 0{,}833$ ; c) $\\frac{3}{6} = 0{,}5$. a) et b) ont le même "
         "numérateur ($\\frac{5}{36}$, g) mais des conditions de probabilités $\\frac{11}{36}$ et $\\frac{6}{36}$. "
         "d) et e) valent tous deux $\\frac{1}{2}$ : « premier dé pair » et « somme paire » sont indépendants, alors "
         "que la parité du premier dé intervient dans celle de la somme. Les écarts (0,004 pour a, 0,003 pour c) sont "
         "normaux : c) ne repose que sur environ 16 800 tirages, et l'erreur type d'une proportion de 0,5 sur "
         "16 800 tirages vaut environ 0,004 ; a), sur environ 30 600 tirages, a une erreur type de 0,003.",
)

M03_25_GIVEN = '''POS_25 = [0.93, 0.88, 0.71, 0.71, 0.64, 0.52, 0.47, 0.38]     # 8 positive examples
NEG_25 = [0.82, 0.71, 0.55, 0.40, 0.35, 0.21]                   # 6 negative examples (one tie with two positives)'''

M03_25_CHECK = '''with checked("M03.25 vérifications"):
    problems = []
    pos_t, neg_t = [0.9, 0.6, 0.6, 0.3, 0.1], [0.6, 0.4, 0.3, 0.2]       # another example, with ties
    y_t = np.r_[np.ones(len(pos_t)), np.zeros(len(neg_t))]
    fpr_t, tpr_t, _ = roc_curve(y_t, np.r_[pos_t, neg_t], drop_intermediate=False)
    expected = [(float(f), float(t)) for f, t in zip(fpr_t, tpr_t)]
    result = list(roc_points(pos_t, neg_t))
    if (len(result) == 2 and all(np.ndim(part) == 1 and len(part) == len(expected) for part in result)):
        problems.append("roc_points renvoie deux listes (fpr, tpr), comme roc_curve : la docstring demande une liste de "
                        "couples (fpr, tpr), par exemple list(zip(fpr, tpr))")
    else:
        points = [tuple(float(v) for v in point) for point in result]
        if len(points) == len(pos_t) + len(neg_t) + 1:
            problems.append("roc_points : un point par score distinct, pas un par exemple ; des ex æquo passent le "
                            "seuil ensemble et font avancer les deux coordonnées d'un coup")
        elif len(points) != len(expected) or any(abs(a - c) > 1e-9 or abs(b - d) > 1e-9
                                                 for (a, b), (c, d) in zip(points, expected)):
            problems.append("roc_points : un point (0, 0), puis un point par score distinct, du plus grand au plus "
                            "petit, chacun (FPR, recall) avec la règle « score ≥ seuil »")
    fig, ax = plt.subplots(figsize=(4, 4))
    try:
        created = drawn(draw_roc, ax, pos_t, neg_t)
    finally:
        plt.close(fig)                                     # only the checks below are shown here
    if created:
        problems.append("draw_roc ouvre sa propre figure : dessine dans l'axe reçu")
    else:
        lines = [line for line in ax.get_lines() if len(line.get_xdata()) >= 3]
        diagonals = [line for line in ax.get_lines()
                     if np.allclose(np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float))
                     and min(line.get_xdata()) <= 0 and max(line.get_xdata()) >= 1]
        curve = None
        for line in lines:
            xy = list(zip(np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)))
            if all(any(abs(x - a) < 1e-9 and abs(y - b) < 1e-9 for x, y in xy) for a, b in expected):
                curve = line
        if curve is None:
            problems.append("la courbe ROC doit passer par tous ses points (FPR, recall) : trace roc_points avec ax.plot")
        else:
            if curve.get_drawstyle() != "default":
                problems.append("relie les points par des segments (ax.plot) : un ex æquo donne un segment oblique, "
                                "que ax.step dessinerait en marche")
            if curve.get_linestyle() in ("None", "none", "", " "):
                problems.append("relie les points par des segments : ax.plot(fpr, tpr), pas des points seuls (le format « o »)")
            xs, ys = np.asarray(curve.get_xdata(), dtype=float), np.asarray(curve.get_ydata(), dtype=float)
            area = float(np.sum((xs[1:] - xs[:-1]) * (ys[1:] + ys[:-1]) / 2))
            if abs(area - roc_auc_score(y_t, np.r_[pos_t, neg_t])) > 1e-9:
                problems.append("l'aire sous la courbe tracée doit être l'AUC : relie dans l'ordre, de (0, 0) à (1, 1), "
                                "les seuls points de roc_points (un par score distinct)")
        if not diagonals:
            problems.append("il manque la diagonale du hasard, de (0, 0) à (1, 1)")
        if not ax.get_xlabel() or not ax.get_ylabel():
            problems.append("nomme les deux axes (taux de faux positifs, recall)")
        if "AUC" not in ax.get_title():
            problems.append("le titre doit donner l'AUC")
    if problems:
        print("❌ Ex M03.25 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M03.25 : une courbe ROC juste, ex æquo compris, avec la diagonale, les axes nommés et l'AUC.")'''

M03_25 = Ex(
    "M03.25", "🎨", 1, 20, "La courbe ROC en escalier : une case par paire",
    "calculer les sommets d'une courbe ROC, ex æquo compris, et la tracer avec la diagonale du hasard et son AUC.",
    "fiche §7 ; R0 (matplotlib)", tracks="C",
    body="""Écris deux fonctions :
- `roc_points(scores_pos, scores_neg)` : la liste des sommets de la courbe ROC, des couples `(fpr, tpr)` : d'abord $(0, 0)$, puis un point pour chaque score **distinct**, du plus grand au plus petit, avec la règle « positif si score $\\ge$ seuil » ; le dernier point est $(1, 1)$. Un seuil qui fait passer à la fois des positifs et des négatifs (des ex æquo) fait avancer les deux coordonnées d'un coup ;
- `draw_roc(ax, scores_pos, scores_neg)` : dessine, dans l'axe `ax`, la courbe qui relie ces points par des segments (`ax.plot`), la diagonale du hasard en pointillés, les noms des deux axes, et un titre qui contient l'AUC (ta fonction `mymath.conditional.auc_by_pairs`, ou `roc_auc_score`).

Puis trace la courbe des scores `POS_25` et `NEG_25` de la cellule fournie. Si tu le veux, ajoute en fond la grille des $8 \\times 6$ paires (`ax.set_xticks(np.linspace(0, 1, 7))`, `ax.set_yticks(np.linspace(0, 1, 9))`, `ax.grid(True)`), comme la figure de la fiche.

Dans ta copie : compte les cases de la grille sous la courbe ; retrouves-tu l'AUC ? Où se trouve le segment en diagonale, et à quelles paires correspond-il ?""",
    given=M03_25_GIVEN,
    todo='''def roc_points(scores_pos, scores_neg):
    """The vertices (fpr, tpr) of the ROC curve: (0, 0), then one point per distinct score, from the largest to the
    smallest, with the rule "positive if score ≥ threshold"."""
    raise NotImplementedError("les scores distincts triés par ordre décroissant, puis deux proportions par seuil")


def draw_roc(ax, scores_pos, scores_neg):
    """In ax: the ROC curve (segments between the points), the dashed chance diagonal, axis names, the AUC in the
    title."""
    raise NotImplementedError("ax.plot des points de roc_points, ax.plot([0, 1], [0, 1], \\"--\\"), set_xlabel, set_title")''',
    check='''with checked("M03.25 figure"):
    fig, ax = plt.subplots(figsize=(4.5, 4.5))
    try:
        created = drawn(draw_roc, ax, POS_25, NEG_25)
    except BaseException:
        plt.close(fig)                                     # no empty figure while the function is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M03.25 : draw_roc ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans l'axe reçu.")
    else:
        plt.show()''',
    solution='''def roc_points(scores_pos, scores_neg):
    """The vertices (fpr, tpr) of the ROC curve: (0, 0), then one point per distinct score, from the largest to the
    smallest, with the rule "positive if score ≥ threshold"."""
    pos, neg = np.asarray(scores_pos, dtype=float), np.asarray(scores_neg, dtype=float)
    points = [(0.0, 0.0)]
    for threshold in np.unique(np.r_[pos, neg])[::-1]:          # distinct scores, from the largest
        points.append((float(np.mean(neg >= threshold)), float(np.mean(pos >= threshold))))
    return points


def draw_roc(ax, scores_pos, scores_neg):
    """In ax: the ROC curve (segments between the points), the dashed chance diagonal, axis names, the AUC in the
    title."""
    fpr, tpr = zip(*roc_points(scores_pos, scores_neg))
    ax.plot(fpr, tpr, marker="o", linewidth=2, label="courbe ROC")
    ax.plot([0, 1], [0, 1], "--", color="gray", label="hasard")
    ax.set_xticks(np.linspace(0, 1, len(scores_neg) + 1))
    ax.set_yticks(np.linspace(0, 1, len(scores_pos) + 1))
    ax.grid(True, alpha=0.4)
    ax.set(xlabel="taux de faux positifs", ylabel="recall",
           title=f"AUC = {mymath.conditional.auc_by_pairs(scores_pos, scores_neg):.4f}")
    ax.legend(loc="lower right", fontsize=8)


fig, ax = plt.subplots(figsize=(4.5, 4.5))
draw_roc(ax, POS_25, NEG_25)
plt.show()
print(roc_points(POS_25, NEG_25))''',
    after=[("md", "**Vérifications automatiques** (sur d'autres scores, avec des ex æquo ; la figure elle-même se juge "
                  "à l'œil)."),
           ("code", M03_25_CHECK)],
    note="Les scores triés : 0,93+, 0,88+, 0,82−, 0,71 (deux + et un −), 0,64+, 0,55−, 0,52+, 0,47+, 0,40−, 0,38+, "
         "0,35−, 0,21−. Au seuil 0,71, deux positifs et un négatif passent ensemble : la courbe va de "
         "$(\\frac{1}{6} ; \\frac{2}{8})$ à $(\\frac{2}{6} ; \\frac{4}{8})$ en diagonale, et ce segment traverse les "
         "$2 \\times 1$ cases des paires ex æquo, dont il laisse la moitié dessous. L'AUC vaut "
         "$\\frac{33}{48} = 0{,}6875$ : 32 paires bien classées et 2 ex æquo (comptés $\\frac{1}{2}$), sur 48.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M03.26 to M03.28)
# ---------------------------------------------------------------------------
M03_26_MISTAKES = bug_letters_mistakes(
    "ACDE", "BF",
    {"A": "vérifie qu'un taux global tient compte de la taille de chaque groupe",
     "C": "vérifie, pour chaque conditionnelle, quel événement est la condition",
     "D": "vérifie que chaque conditionnelle divise par la probabilité de sa condition",
     "E": "vérifie que chaque résultat est bien une probabilité, calculée sachant la bonne condition"},
    name_correct=False)

M03_26 = Ex(
    "M03.26", "🐛", 1, 15, "Chasse à l'erreur : conditionnelle inversée, marginale oubliée",
    "repérer dans du code les erreurs classiques du calcul de probabilités conditionnelles, puis calculer les bonnes "
    "valeurs.", "fiche §2 et §3", tracks="C",
    body="""Une plateforme de cours en ligne connaît le niveau de ses inscrits et la probabilité qu'ils terminent un cours selon leur niveau :

```python
p_level = {"débutant": 0.5, "intermédiaire": 0.3, "avancé": 0.2}       # P(niveau)
p_done = {"débutant": 0.2, "intermédiaire": 0.4, "avancé": 0.7}        # P(termine | niveau)
```

Un analyste a écrit six lignes, chacune avec un commentaire qui dit ce qu'elle veut calculer pour un inscrit tiré au hasard. Quatre lignes sont fausses. **Sans exécuter de code**, trouve-les.

```python
p_A = (0.2 + 0.4 + 0.7) / 3          # (A) P(termine)
p_B = 0.7 * 0.2                      # (B) P(avancé et termine)
p_C = 0.7                            # (C) P(avancé | termine)
p_D = 0.5 * 0.8                      # (D) P(débutant | ne termine pas)
p_E = 0.4 + 0.7                      # (E) P(termine | pas débutant)
p_F = 1 - 0.7                        # (F) P(ne termine pas | avancé)
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des six lignes, de (A) à (F), la bonne valeur de ce que dit son commentaire (une liste de 6 nombres, 3 décimales).

Dans ta copie : pour chaque ligne fausse, quelle confusion a été faite ? Une des lignes fausses donne une valeur impossible pour une probabilité : laquelle ?""",
    todo='''answer_M03_26a = ...  # a) letters, as text
answer_M03_26b = ...  # b) a list of 6 values (3 decimals)''',
    check='''wbm.check("M03.26a", answer_M03_26a)
wbm.check("M03.26b", answer_M03_26b)''',
    solution='''answer_M03_26a = "ACDE"
p_level = {"débutant": 0.5, "intermédiaire": 0.3, "avancé": 0.2}
p_done = {"débutant": 0.2, "intermédiaire": 0.4, "avancé": 0.7}
done = sum(p_level[k] * p_done[k] for k in p_level)                       # total probability
not_beginner = p_level["intermédiaire"] + p_level["avancé"]
answer_M03_26b = [done,                                                   # (A)
                  p_done["avancé"] * p_level["avancé"],                     # (B) product rule
                  p_done["avancé"] * p_level["avancé"] / done,              # (C) P(avancé ∩ termine) / P(termine)
                  (1 - p_done["débutant"]) * p_level["débutant"] / (1 - done),   # (D)
                  (p_done["intermédiaire"] * p_level["intermédiaire"] + p_done["avancé"] * p_level["avancé"])
                  / not_beginner,                                         # (E)
                  1 - p_done["avancé"]]                                   # (F)
print(answer_M03_26a, [round(v, 4) for v in answer_M03_26b])''',
    record=f'''wbm.record("M03.26a", "ACDE",
           mistakes={M03_26_MISTAKES})
wbm.record("M03.26b", [0.36, 0.14, 0.14 / 0.36, 0.4 / 0.64, 0.26 / 0.5, 0.3], decimals=3,
           mistakes={{"ce sont les valeurs des lignes ; donne les bonnes valeurs de ce que disent les commentaires":
                         [1.3 / 3, 0.14, 0.7, 0.4, 1.1, 0.3]}})''',
    note="(A) fait la moyenne simple des taux, sans les poids des niveaux : $P(\\text{termine}) = 0{,}2 \\times 0{,}5 + "
         "0{,}4 \\times 0{,}3 + 0{,}7 \\times 0{,}2 = 0{,}36$ (probabilités totales, la marginale oubliée). (C) "
         "inverse la conditionnelle : 0,7 est $P(\\text{termine} \\mid \\text{avancé})$ ; $P(\\text{avancé} \\mid "
         "\\text{termine}) = \\frac{0{,}14}{0{,}36} \\approx 0{,}389$. (D) calcule la probabilité **jointe** "
         "$P(\\text{débutant} \\cap \\text{ne termine pas}) = 0{,}4$ sans la diviser par $P(\\text{ne termine pas}) = "
         "0{,}64$ : 0,625. (E) additionne deux probabilités sachant des conditions différentes, et dépasse 1 : "
         "$\\frac{0{,}12 + 0{,}14}{0{,}5} = 0{,}52$. (B) est la règle du produit et (F) le complément sachant la même "
         "condition : justes.",
)

M03_27_CHECK = '''with checked("M03.27 vérifications"):
    problems = []
    cases = [("une loi 2 × 2 valide", [[0.1, 0.2], [0.3, 0.4]], True),
             ("une loi d'entiers valide", [[0, 1], [0, 0]], True),
             ("une somme de 1 à 1e-12 près", [[0.1, 0.2], [0.3, 0.4 + 1e-12]], True),
             ("un tableau à une dimension", [0.5, 0.5], False),
             ("une case négative (somme 1)", [[0.6, -0.1], [0.3, 0.2]], False),
             ("une somme de 1,2", [[0.3, 0.3], [0.3, 0.3]], False),
             ("une case NaN", [[float("nan"), 0.5], [0.25, 0.25]], False),
             ("un tableau vide", [[]], False)]
    messages = {}
    for name, table, valid in cases:
        try:
            result = check_joint(table)
        except NotImplementedError:
            raise
        except ValueError as exc:
            if valid:
                problems.append(f"{name} est refusée à tort ({exc})")
            else:
                messages[name] = str(exc)
                if not str(exc).strip():
                    problems.append(f"{name} : la ValueError doit avoir un message qui dit quelle règle est violée")
            continue
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{name} : lève {type(exc).__name__} ; la docstring demande une ValueError")
            continue
        if not valid:
            problems.append(f"{name} est acceptée à tort" + (" (abs(nan − 1) > 1e-9 est False : une comparaison avec "
                                                            "NaN est toujours fausse)" if "NaN" in name else ""))
        elif not (isinstance(result, np.ndarray) and result.dtype == float and result.ndim == 2):
            problems.append(f"{name} : renvoie un array NumPy de float à deux dimensions")
    rules = [messages.get(name) for name in ("un tableau à une dimension", "une case négative (somme 1)",
                                             "une somme de 1,2")]
    if all(rules) and len(set(rules)) < 3:
        problems.append("les trois règles (deux dimensions, cases positives, somme 1) doivent avoir trois messages "
                        "différents : un message doit dire ce qui ne va pas")
    if problems:
        print("❌ Ex M03.27 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M03.27 : les tableaux valides passent, les invalides lèvent une ValueError qui dit pourquoi.")'''

M03_27 = Ex(
    "M03.27", "🛠️", 1, 10, "Une fonction qui refuse un tableau invalide (`ValueError`)",
    "écrire une fonction de validation qui refuse les entrées invalides par une `ValueError` au message clair, sans "
    "laisser passer le cas piège des NaN.", "fiche §1 ; Ex M03.19", tracks="C",
    body="""Une fonction qui reçoit des données doit refuser ce qui n'a pas de sens, **tôt** et avec un message clair, plutôt que de renvoyer un résultat faux plus loin. En Python, l'erreur habituelle pour une valeur invalide est la `ValueError`.

Écris `check_joint(table, tol=1e-9)`, qui renvoie le tableau converti en array NumPy de `float` s'il est une loi jointe valide, et lève sinon une `ValueError` dont le message dit **quelle règle** est violée :
- le tableau doit avoir deux dimensions (et au moins une case) ;
- toutes ses cases doivent être positives ou nulles ;
- leur somme doit valoir 1, à `tol` près.

Attention au piège : une case `nan` (*not a number*, une valeur manquante dans un calcul) rend la somme `nan`, et **toute** comparaison avec `nan` est fausse : `abs(nan - 1) > tol` vaut `False`, comme `nan < 0`. `np.isfinite` repère les cases qui ne sont pas des nombres finis.

La vérification essaie huit tableaux, valides ou non.

Dans ta copie : dans quel ordre as-tu écrit les vérifications, et pourquoi l'ordre compte-t-il (que se passe-t-il si l'on additionne les cases d'un tableau vide) ? Ta fonction `_check_joint` de `mymath/conditional.py` résiste-t-elle aux NaN ?""",
    todo='''def check_joint(table, tol=1e-9):
    """Return table as a 2-D float array if it is a valid joint law; otherwise raise ValueError with a message that
    says which rule is broken (two dimensions, non-negative finite entries, sum 1 up to tol)."""
    raise NotImplementedError("np.asarray(table, dtype=float), puis une vérification par règle, chacune avec son message")''',
    solution='''def check_joint(table, tol=1e-9):
    """Return table as a 2-D float array if it is a valid joint law; otherwise raise ValueError with a message that
    says which rule is broken (two dimensions, non-negative finite entries, sum 1 up to tol)."""
    array = np.asarray(table, dtype=float)
    if array.ndim != 2 or array.size == 0:
        raise ValueError(f"a joint law is a non-empty 2-D table, got shape {array.shape}")
    if not np.all(np.isfinite(array)):
        raise ValueError("a joint law has finite entries (no nan, no inf)")
    if np.any(array < 0):
        raise ValueError("a joint law has non-negative entries")
    if abs(array.sum() - 1) > tol:
        raise ValueError(f"the entries of a joint law sum to 1, got {array.sum()}")
    return array


print(check_joint([[0.1, 0.2], [0.3, 0.4]]))''',
    after=[("code", M03_27_CHECK)],
    note="L'ordre compte : la forme d'abord (la somme d'un tableau vide vaut 0, et un tableau à une dimension n'a pas "
         "de lignes), puis les NaN (sinon `abs(nan - 1) > tol` est faux et le tableau passe), puis le signe, puis la "
         "somme. Une case `nan` n'est pas « positive ou nulle » : la référence de `conditional.py` refuse donc une loi "
         "qui en contient. Les tests de `mymath` ne vérifient pas ce cas ; essaie la tienne avec "
         "`marginal([[np.nan, 0.5], [0.25, 0.25]], 0)`, et corrige-la si elle renvoie un résultat.",
)

M03_28_CHECK = '''with checked("M03.28 indices"):
    if TABLE_28 is ...:
        raise NotImplementedError("remplis TABLE_28")
    table = np.asarray(TABLE_28, dtype=float)
    if table.shape != (2, 3):
        print("❌ TABLE_28 doit avoir 2 lignes (appli, site) et 3 colonnes (achat, abandon, rien).")
    else:
        rows, cols, n = table.sum(axis=1), table.sum(axis=0), table.sum()
        clues = [("600 visites", n == 600),
                 ("P(appli) = 0,4", math.isclose(rows[0] / n, 0.4)),
                 ("P(achat) = 0,5", math.isclose(cols[0] / n, 0.5)),
                 ("P(achat | appli) = 0,625", rows[0] > 0 and math.isclose(table[0, 0] / rows[0], 0.625)),
                 ("P(appli | abandon) = 1/6", cols[1] > 0 and math.isclose(table[0, 1] / cols[1], 1 / 6)),
                 ("P(rien | site) = 1/6", rows[1] > 0 and math.isclose(table[1, 2] / rows[1], 1 / 6))]
        print("  ".join(f"{'✓' if ok else '✗'} {name}" for name, ok in clues))
wbm.check("M03.28a", TABLE_28)
wbm.check("M03.28b", answer_M03_28b)'''

M03_28 = Ex(
    "M03.28", "🏆", 3, 25, "Défi : retrouver un tableau de contingence à partir de quelques probabilités",
    "reconstruire un tableau de contingence à partir de marges et de probabilités conditionnelles, par le calcul ou "
    "par une recherche.", "fiche §1 à §3", tracks="C",
    body="""Une boutique a perdu le tableau de ses 600 visites d'hier, classées selon le canal (appli ou site, en lignes) et le résultat (achat, panier abandonné, ou rien, en colonnes). Il lui reste ces informations, pour une visite tirée au hasard :
1. il y a eu 600 visites ;
2. $P(\\text{appli}) = 0{,}4$ ;
3. $P(\\text{achat}) = 0{,}5$ ;
4. $P(\\text{achat} \\mid \\text{appli}) = 0{,}625$ ;
5. $P(\\text{appli} \\mid \\text{abandon}) = \\frac{1}{6}$ ;
6. $P(\\text{rien} \\mid \\text{site}) = \\frac{1}{6}$.

Retrouve le tableau des **effectifs** : `TABLE_28`, une liste de 2 listes de 3 entiers, `[[appli-achat, appli-abandon, appli-rien], [site-achat, site-abandon, site-rien]]`. Deux chemins sont possibles :
- **à la main** : traduis chaque information en une équation sur les cases, et résous-les dans le bon ordre (une case après l'autre) ;
- **par le code** : cherche, parmi les tableaux d'entiers qui ont les bonnes marges, ceux qui vérifient toutes les informations (attention : les comparaisons de fractions se font avec `math.isclose` ou avec `fractions.Fraction`, pas avec `==` sur des flottants).

Puis calcule b) $P(\\text{appli} \\mid \\text{achat ou abandon})$, en fraction irréductible.

La vérification affiche, pour ton tableau, les informations qu'il respecte (✓) ou non (✗), puis vérifie tes réponses.

Dans ta copie : la solution est-elle unique ? Quelles informations suffiraient à la trouver si l'on retirait l'information 6 ? Le canal et le résultat sont-ils indépendants ?""",
    todo='''TABLE_28 = ...         # a) [[app-purchase, app-abandoned, app-nothing], [site-purchase, site-abandoned, site-nothing]]
answer_M03_28b = ...   # b) an irreducible fraction, as text''',
    check=M03_28_CHECK,
    solution='''# By hand, one cell at a time: the margins give 240 app visits (2) and 300 purchases (3); then (4) app-purchase =
# 0.625 × 240 = 150, so site-purchase = 150; (6) site-nothing = 360 / 6 = 60, so site-abandoned = 360 − 150 − 60 = 150;
# (5) app-abandoned = a with a / (a + 150) = 1/6, so 6a = a + 150 and a = 30; finally app-nothing = 240 − 150 − 30 = 60.
TABLE_28 = [[150, 30, 60], [150, 150, 60]]
# The same by a search over the tables with the right margins, with exact fractions (each clue prunes the search):
from fractions import Fraction as Fr

found = []
for a in range(241):                                     # app-purchase; site-purchase = 300 − a
    if Fr(a, 240) != Fr(5, 8):                           # clue 4
        continue
    for f in range(361 - (300 - a)):                     # site-nothing
        if Fr(f, 360) != Fr(1, 6):                       # clue 6
            continue
        e = 360 - (300 - a) - f                          # site-abandoned
        for b in range(241 - a):                         # app-abandoned; app-nothing = 240 − a − b
            if b + e > 0 and Fr(b, b + e) == Fr(1, 6):   # clue 5
                found.append([[a, b, 240 - a - b], [300 - a, e, f]])
print("tables found by the search:", found)
answer_M03_28b = str(Fr(150 + 30, 300 + 180))
print("b)", answer_M03_28b)''',
    record='''wbm.record("M03.28a", [[150, 30, 60], [150, 150, 60]])
wbm.record("M03.28b", "3/8", kind="fraction", simplified=True,
           mistakes={"« sachant achat ou abandon » : divise par le nombre de visites avec un achat ou un abandon":
                         "3/10"})''',
    note="L'ordre de résolution : les marges (240 visites sur l'appli, 300 achats), puis l'information 4 donne la case "
         "appli-achat ($0{,}625 \\times 240 = 150$), donc site-achat (150) ; l'information 6 donne site-rien "
         "($\\frac{360}{6} = 60$), donc site-abandon ($360 - 150 - 60 = 150$) ; enfin l'information 5, "
         "$\\frac{a}{a + 150} = \\frac{1}{6}$, donne appli-abandon $a = 30$, et appli-rien $= 60$. La solution est "
         "unique : chaque information fixe une case de plus. b) $\\frac{150 + 30}{300 + 180} = \\frac{3}{8}$. Le canal "
         "et le résultat sont dépendants : $P(\\text{achat} \\mid \\text{appli}) = 0{,}625$ mais "
         "$P(\\text{achat}) = 0{,}5$.",
)


PART_A = Part("A", "Ta librairie : loi jointe, marginales, conditionnelles, indépendance et AUC",
              "Fiche §1, §2 et §7. Les cinq fonctions de `mymath/conditional.py`, puis l'AUC et l'average precision "
              "avec scikit-learn.",
              given=TOOLS, exercises=[M03_19, M03_20, M03_21, M03_22])

PART_B = Part("B", "Une prédiction, une simulation et une figure",
              "Fiche §2, §7 et §8. Ce que l'AUC voit et ne voit pas, des probabilités conditionnelles estimées par "
              "simulation, la courbe ROC en escalier.",
              exercises=[M03_23, M03_24, M03_25])

PART_C = Part("C", "Erreurs classiques, validation et défi",
              "Fiche §1 à §3. Quatre erreurs de conditionnement à trouver, une fonction qui refuse les entrées "
              "invalides, puis un tableau à reconstruire.",
              exercises=[M03_26, M03_27, M03_28])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M03.1 à M03.11, M03.14, M03.15 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M03 · Probabilités conditionnelles — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m03_probabilites_conditionnelles/03_notebook.ipynb`, "
               "créée par `python tools/start_chapter.py M03`) ; la version du dépôt est mise à jour par Claude. Sur "
               "Colab, le badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M03 · Probabilités conditionnelles — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : tableaux de contingence, indépendance, probabilités totales, "
               "matrice de confusion, F-beta, balanced accuracy et MCC, prévalence, courbes ROC et precision-recall, "
               "AUC par les paires, score de Brier, seuils et taux par groupe.\n"
               "- Écrire les cinq fonctions de `mymath/conditional.py` et les tester, puis utiliser `sklearn.metrics`.\n"
               "- Prédire ce que voit l'AUC, estimer des conditionnelles par simulation, tracer une courbe ROC, chasser "
               "des erreurs de conditionnement, valider une entrée, reconstruire un tableau.\n\n"
               "**Rappel express.** $P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)}$ ; $P(A \\cap B) = P(A \\mid B)\\,P(B)$ ; "
               "indépendance : $P(A \\cap B) = P(A)\\,P(B)$ ; probabilités totales : $P(A) = \\sum_k P(A \\mid B_k)\\,"
               "P(B_k)$ ; recall $= P(\\hat{Y} = 1 \\mid Y = 1)$, precision $= P(Y = 1 \\mid \\hat{Y} = 1)$ ; "
               "$\\text{AUC} = P(S_+ > S_-) + \\frac{1}{2}P(S_+ = S_-)$ ; Brier $= \\frac{1}{n}\\sum (p_i - y_i)^2$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu lire dans un tableau des probabilités jointes, marginales et conditionnelles, décider de "
               "l'indépendance, et utiliser les probabilités totales ?\n"
               "2. Sais-tu écrire chaque mesure d'une matrice de confusion comme une probabilité conditionnelle, et "
               "dire comment elle change avec la prévalence et le seuil ?\n"
               "3. Sais-tu calculer une AUC par les paires, une average precision et un score de Brier, et dire ce que "
               "chacun mesure ?\n\n"
               "**La suite** : le chapitre 3 de workbookIA (probabilités et métriques de classification), puis M04, la "
               "règle de Bayes et la loi Beta.")]


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
