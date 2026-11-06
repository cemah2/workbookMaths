#!/usr/bin/env python
"""Build the two notebooks of chapter R3 from a single source (used by Claude).

    python tools/chapters/build_r3.py
    python tools/run_all_notebooks.py chapitres/r3_fonctions/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/r3_fonctions/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ R3.1 and R3.3 to R3.12, 📈 R3.2, 🔗 R3.15); parts A to C are the notebook
exercises. Wrong-answer messages state a rule, never a number of the answer. A developed polynomial is answered by its
list of coefficients, an affine function by [m, c], a canonical form by [a, alpha, beta].
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys,  # noqa: E402
                         code, guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "R3"
FOLDER = "chapitres/r3_fonctions"

EXACT = "donne la valeur exacte, une fraction tapée comme un calcul, pas une valeur arrondie"
MC = '"l\'ordre demandé est [m, c] : la pente, puis l\'ordonnée à l\'origine"'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("R3.1", "Images, antécédents et ensemble de définition", [
        ("a", "a number", "3 * (-2) ** 2 - (-2) - 4",
         'mistakes={"le carré d\'un nombre négatif est positif : garde les parenthèses autour de −2": -14, '
         '"−x avec x = −2 donne +2": 6}'),
        ("b", "a fraction, as text", "(2 * Fraction(1, 2) + 1) / (Fraction(1, 2) - 3)",
         'kind="fraction", mistakes={"le dénominateur 1/2 − 3 est négatif": "4/5"}'),
        ("c", "a list", "[-3, 3]",
         'ordered=False, mistakes={"un carré égal à un nombre positif : deux solutions opposées": [3], '
         '"un antécédent se cherche en résolvant h(x) = 10, pas en calculant h(10)": [101]}'),
        ("d", "a list (empty if there is none)", "[]",
         'ordered=False, mistakes={"un carré n\'est jamais négatif : regarde ce que donne h(x) = −3": [-2, 2]}'),
        ("e", "a number", "3.0",
         'decimals=2, mistakes={"un antécédent se cherche en résolvant k(x) = 7, pas en calculant k(7)": 23.0, '
         '"pour isoler 4x, ajoute 5 aux deux membres": 0.5}'),
        ("f", "a union of intervals, as text", '"]-oo ; 4[ U ]4 ; +oo["',
         'kind="interval", mistakes={"x − 4 s\'annule pour la valeur qui le rend nul, avec son signe": '
         '"]-oo ; -4[ U ]-4 ; +oo[", "on n\'exclut qu\'une seule valeur : celle qui annule le dénominateur": '
         '"]4 ; +oo["}'),
        ("g", "an interval, as text", '"]-oo ; 3]"',
         'kind="interval", mistakes={"6 − 2x ≥ 0 : en divisant par −2, le sens change": "[3 ; +oo[", '
         '"la racine carrée de 0 existe : la borne est incluse": "]-oo ; 3["}'),
        ("h", "a union of intervals, as text", '"[-2 ; 1[ U ]1 ; +oo["',
         'kind="interval", mistakes={"il faut les deux conditions : la racine et le dénominateur": "[-2 ; +oo[", '
         '"la racine carrée de 0 existe : la borne de gauche est incluse": "]-2 ; 1[ U ]1 ; +oo["}'),
    ]),
    Paper("R3.2", "Lire des valeurs, des solutions et des variations sur un graphique", [
        ("a", "a number", "4", ""),
        ("b", "a number", "0", ""),
        ("c", "a list", "[-3, -1, 4]",
         'ordered=False, mistakes={"trace toute la droite y = 2 : elle coupe la courbe trois fois": [-1, 4], '
         '"des antécédents sont des abscisses, lues sur l\'axe horizontal": [2]}'),
        ("d", "a list", "[-4, 0, 3]",
         'ordered=False, mistakes={"regarde aussi les extrémités de la courbe et ses points anguleux": [0], '
         '"l\'extrémité gauche de la courbe est aussi sur l\'axe horizontal": [0, 3]}'),
        ("e", "a number", "4",
         'mistakes={"le maximum est une valeur de f, lue sur l\'axe vertical, pas une abscisse": 5}'),
        ("f", "a list", "[-2, 5]",
         'ordered=False, mistakes={"le maximum est atteint deux fois : regarde aussi les extrémités": [-2], '
         '"ce sont des valeurs de x, lues sur l\'axe horizontal": [4]}'),
        ("g", "an interval, as text", '"[1 ; 5]"',
         'kind="interval", mistakes={"croissante : la courbe monte quand on va de gauche à droite": "[-2 ; 1]", '
         '"la courbe monte sans s\'arrêter sur deux segments de suite : ils forment un seul intervalle": "[3 ; 5]", '
         '"un intervalle de variation se donne avec ses bornes, fermé": "]1 ; 5["}'),
        ("h", "a union of intervals, as text", '"[-3 ; -1] U [4 ; 5]"',
         'kind="interval", mistakes={"f(x) ≥ 2 garde aussi les points sur la droite y = 2 : bornes incluses": '
         '"]-3 ; -1[ U ]4 ; 5[", "≥ 2 : là où la courbe est au-dessus de la droite y = 2, pas en dessous": '
         '"]-1 ; 4["}'),
    ]),
    Paper("R3.3", "La fonction affine qui passe par deux points", [
        ("a", "the list [m, c]", "[2.0, -3.0]",
         f'decimals=3, mistakes={{"la pente est Δy/Δx, pas Δx/Δy": [0.5, 0.0], {MC}: [-3.0, 2.0]}}'),
        ("b", "the list [m, c]", "[-2.0, 1.0]",
         f'decimals=3, mistakes={{"c = y − m·x : avec une pente négative, attention aux signes": [-2.0, -3.0], '
         f'{MC}: [1.0, -2.0]}}'),
        ("c", "the list [m, c]", "[0.4, 4.0]",
         'decimals=3, mistakes={"la pente est Δy/Δx : la variation de y divisée par celle de x": [2.5, 4.0]}'),
        ("d", "a number", "Fraction(1, 2)",
         'kind="fraction", mistakes={"la racine annule la fonction : isole x avec son signe": "-1/2", '
         '"la racine est l\'abscisse où la droite coupe l\'axe horizontal, pas l\'ordonnée à l\'origine": 1}'),
        ("e", "a number", "45", 'mistakes={"f est affine, pas proportionnelle : f(50) n\'est pas 5 × f(10)": 125}'),
        ("f", "True or False", "2 * 4 - 3 == 5",
         'mistakes={"calcule m × 4 + c avec les m et c de a, puis compare à 5": False}'),
        ("g", "the list [m, c]", "[1.2, 5.0]",
         f'decimals=3, mistakes={{{MC}: [5.0, 1.2]}}'),
    ]),
    Paper("R3.4", "Ramener des données entre 0 et 1 avec une fonction affine (min-max)", [
        ("a", "the list [m, c]", "[0.01, -0.2]",
         f'decimals=4, mistakes={{{MC}: [-0.2, 0.01]}}'),
        ("b", "a number", "Fraction(65 - 20, 100)",
         'kind="fraction", mistakes={"retire le minimum avant de diviser par l\'étendue": "13/24"}'),
        ("c", "the list [m, c]", "[100.0, 20.0]",
         f'decimals=3, mistakes={{"la réciproque défait N : multiplie par l\'étendue, puis ajoute le minimum": '
         f'[100.0, -20.0], {MC}: [20.0, 100.0]}}'),
        ("d", "a number (m²)", "100", 'mistakes={"multiplie par l\'étendue, puis ajoute le minimum": 80}'),
        ("e", "the list [m, c]", "[0.1, -2.0]",
         'decimals=3, mistakes={"10 × N multiplie les deux coefficients par 10": [0.1, -0.2]}'),
    ]),
    Paper("R3.5", "Variations et signe des fonctions de référence", [
        ("a", "an interval, as text", '"]-oo ; 0]"',
         'kind="interval", mistakes={"le carré décroît à gauche de 0 et croît à droite": "[0 ; +oo[", '
         '"un intervalle de variation se donne avec ses bornes, fermé du côté de 0": "]-oo ; 0["}'),
        ("b", "an interval, as text", '"]-3 ; 3["',
         'kind="interval", mistakes={"x² < 9 garde aussi des négatifs : essaie x = −2": "]-oo ; 3[", '
         '"l\'inégalité est stricte : les bornes sont exclues": "[-3 ; 3]"}'),
        ("c", "an interval, as text", '"]0 ; 0.5["',
         'kind="interval", mistakes={"1/x est négatif pour x < 0 : seuls des x positifs conviennent": '
         '"]-oo ; 0.5[", "l\'inverse est décroissant sur ]0 ; +∞[ : il retourne l\'ordre": "]0.5 ; +oo["}'),
        ("d", "an interval, as text", '"[0 ; 9]"',
         'kind="interval", mistakes={"√x n\'est définie que pour x ≥ 0": "]-oo ; 9]", '
         '"√x ≤ 3 : élève au carré, ne prends pas une racine de plus": "[0 ; 3]"}'),
        ("e", "a union of intervals, as text", '"]-oo ; -2] U [2 ; +oo["',
         'kind="interval", mistakes={"|x| ≥ 2 : les points à distance au moins 2 de 0, donc à l\'extérieur": '
         '"[-2 ; 2]", "l\'inégalité est large : les bornes sont incluses": "]-oo ; -2[ U ]2 ; +oo["}'),
        ("f", "an interval, as text", '"[0 ; 4]"',
         'kind="interval", mistakes={"quand x parcourt l\'intervalle, x passe par 0 : trace la courbe": "[1 ; 4]"}'),
        ("g", "True or False", "1 / -0.3 > 1 / -0.2",
         'mistakes={"calcule les deux nombres, ou sers-toi du sens de variation de l\'inverse sur les '
         'négatifs": False}'),
    ]),
    Paper("R3.6", "Forme canonique et sommet d'une parabole", [
        ("a", "the list [a, alpha, beta]", "[1, -3, -7]",
         'mistakes={"(x − α)² : α est l\'opposé du nombre dans la parenthèse": [1, 3, -7], '
         '"le carré ajouté pour compléter doit être retiré": [1, -3, 2]}'),
        ("b", "the list [a, alpha, beta]", "[2, 3, -5]",
         'mistakes={"a est en facteur : le carré retiré est multiplié par a": [2, 3, 4], '
         '"(x − α)² : α est l\'opposé du nombre dans la parenthèse": [2, -3, -5]}'),
        ("c", "the list [a, alpha, beta]", "[-1, 2, 5]",
         'mistakes={"avec a = −1, mets −1 en facteur et suis les signes": [-1, 2, -3], '
         '"a est le coefficient de x², avec son signe": [1, 2, 5]}'),
        ("d", "the list [alpha, beta]", "[-1, -5]",
         'mistakes={"α = −b/(2a) : attention au signe": [1, 7], '
         '"le carré d\'un nombre négatif est positif": [-1, -11]}'),
        ("e", "the list [a, b, c]", "[2, 8, 11]",
         'mistakes={"développe le carré, puis multiplie tout le carré développé par a": [2, 4, 7], '
         '"un sommet d\'abscisse négative donne (x + …)² dans la forme canonique": [2, -8, 11]}'),
        ("f", "a number", "2", 'mistakes={"(3 − 1)² est un carré : calcule-le avant de résoudre": 4}'),
    ]),
    Paper("R3.7", "Racines par le discriminant et factorisation", [
        ("a", "a number", "(-5) ** 2 - 4 * 3 * (-2)",
         'mistakes={"b² avec b négatif : un carré est positif": -1, "−4ac avec c négatif : moins par moins donne '
         'plus": 1}'),
        ("b", "a list", "[-1 / 3, 2]",
         'ordered=False, decimals=8, mistakes={"−b avec b négatif donne un nombre positif": [-2, 1 / 3]}'),
        ("c", "the list [a, x1, x2]", "[3, -1 / 3, 2]",
         'decimals=8, mistakes={"n\'oublie pas le coefficient a devant le produit": [1, -1 / 3, 2], '
         '"x₁ < x₂ : la plus petite racine d\'abord": [3, 2, -1 / 3]}'),
        ("d", "a list", "[3]",
         'ordered=False, mistakes={"(x − 3)² s\'annule quand x − 3 = 0 : résous avec le bon signe": [-3]}'),
        ("e", "a list (empty if there is none)", "[]",
         'ordered=False, mistakes={"un discriminant négatif : pas de racine réelle": [-0.25]}'),
        ("f", "a list", "[-2, 4]",
         'ordered=False, mistakes={"avec a négatif, 2a est négatif : les signes changent": [2, -4]}'),
        ("g", "an interval, as text", '"]-1/3 ; 2["',
         'kind="interval", mistakes={"a > 0 : le polynôme est négatif entre les racines, pas à l\'extérieur": '
         '"]-oo ; -1/3[ U ]2 ; +oo[", "l\'inégalité est stricte : les racines sont exclues": "[-1/3 ; 2]"}'),
    ]),
    Paper("R3.8", "Trouver le maximum d'une aire ou d'un bénéfice", [
        ("a", "a number (m²)", "10 * (40 - 2 * 10)",
         'mistakes={"le grillage fait trois côtés : deux de longueur x et un de longueur 40 − 2x": 400, '
         '"le mur fait le quatrième côté : seuls trois côtés sont en grillage": 100, '
         '"on demande l\'aire maximale, pas la valeur de x qui la donne": 10}'),
        ("b", "a number (m)", "10", 'mistakes={"on demande la valeur de x, pas l\'aire": 200}'),
        ("c", "a list", "[5, 15]",
         'ordered=False, mistakes={"l\'équation du second degré a deux solutions, de part et d\'autre du sommet": '
         '[5], "il y a deux solutions : cherche l\'autre": [15]}'),
        ("d", "a number (€)", "25", 'mistakes={"on demande le prix, pas la recette": 2500}'),
        ("e", "a number (€)", "25 * (200 - 4 * 25)", 'mistakes={"on demande la recette, pas le prix": 25}'),
    ]),
    Paper("R3.9", "Composer deux fonctions dans les deux ordres", [
        ("a", "a number", "(2 * 2**2 + 1) - 4", 'mistakes={"(f∘g)(2) : g d\'abord, puis f": 9}'),
        ("b", "a number", "2 * (2 - 4) ** 2 + 1", 'mistakes={"(g∘f)(2) : f d\'abord, puis g": 5}'),
        ("c", "a list of coefficients", "[2, 0, -3]",
         'mistakes={"(f∘g)(x) = f(g(x)) : on remplace x par g(x) dans f": [2, -16, 33]}'),
        ("d", "a list of coefficients", "[2, -16, 33]",
         'mistakes={"(g∘f)(x) = g(f(x)) : on remplace x par f(x) dans g": [2, 0, -3], '
         '"(x − 4)² a un double produit": [2, 0, 33], "multiplie tout le carré développé par 2": [2, -8, 17], '
         '"le terme constant du carré développé est lui aussi multiplié par 2": [2, -16, 17]}'),
        ("e", "a list of coefficients", "[1, -8]",
         'mistakes={"f∘f applique f deux fois, ce n\'est pas f(x) × f(x)": [1, -8, 16]}'),
        ("f", "the list [m, c]", "[-5, 4]", f"mistakes={{{MC}: [4, -5], \"v(x) = 4 − 5x : la pente est le coefficient de x, avec son signe\": [5, 4]}}"),
        ("g", "a list", "[9 / 4]",
         'ordered=False, decimals=6'),
        ("h", "a list of coefficients", "[-3, 13]", 'mistakes={"p∘q = p(q(x)) : q d\'abord, puis p": [-3, 7]}'),
    ]),
    Paper("R3.10", "Trouver une réciproque et son ensemble de définition", [
        ("a", "the list [m, c]", "[0.25, 0.75]",
         f'decimals=4, mistakes={{"pour isoler x, ajoute 3 puis divise par 4": [0.25, -0.75], {MC}: [0.75, 0.25]}}'),
        ("b", "a number", "3.0",
         'decimals=4, mistakes={"f⁻¹(9) est l\'antécédent de 9 par f, pas f(9)": 33.0, '
         '"f⁻¹ n\'est pas 1/f : f⁻¹(9) est le nombre x tel que f(x) = 9": 1 / 33}'),
        ("c", "a number", "1 + Fraction(2, 4)",
         'kind="fraction", mistakes={"g⁻¹(4) est le nombre x tel que g(x) = 4, pas g(4)": "2/3"}'),
        ("d", "a union of intervals, as text", '"]-oo ; 0[ U ]0 ; +oo["',
         'kind="interval", mistakes={"g⁻¹ est définie sur l\'ensemble des valeurs prises par g, pas sur celui de g": '
         '"]-oo ; 1[ U ]1 ; +oo["}'),
        ("e", "an interval, as text", '"[3 ; +oo["',
         'kind="interval", mistakes={"h⁻¹ est définie sur l\'ensemble des valeurs prises par h": "[0 ; +oo["}'),
        ("f", "a number", "2", 'mistakes={"h⁻¹(7) est l\'antécédent positif de 7 par h, pas h(7)": 52}'),
        ("g", "True or False", "False",
         'mistakes={"un nombre positif a deux antécédents par le carré : on ne saurait pas lequel rendre": True}'),
    ]),
    Paper("R3.11", "Fonctions par morceaux et argmax", [
        ("a", "a number", "Fraction(0)", 'kind="fraction", mistakes={"max(0, x) remplace les négatifs par 0": "-5/2"}'),
        ("b", "a number", "3", 'mistakes={"r(−3) = max(0, −3), qui n\'est pas négatif": 0}'),
        ("c", "an interval, as text", '"]-oo ; 0]"',
         'kind="interval", mistakes={"r(0) = max(0, 0) : la borne 0 est incluse": "]-oo ; 0["}'),
        ("d", "a number", "1",
         'mistakes={"la convention de l\'énoncé fixe la valeur en 0": 0, "−0,1 est négatif : regarde la marche à '
         'gauche de 0": 2}'),
        ("e", "an expression in x, as text", '"Abs(x)"',
         'kind="expr", variables=("x",), mistakes={"pour x négatif, r(x) vaut 0 et r(−x) vaut −x": "x", '
         '"un des deux termes est toujours nul, mais pas les deux": "0"}'),
        ("f", "a number", "-(3 - 2) ** 2 + 3",
         'mistakes={"le sommet n\'est pas dans l\'intervalle : regarde les variations de q sur [3 ; 6]": 3}'),
        ("g", "a number", "3",
         'mistakes={"q est décroissante sur l\'intervalle : son maximum est à une borne, et le sommet n\'y est pas": 2}'),
        ("h", "an integer", "2",
         'mistakes={"NumPy compte les positions à partir de 0": 3, "NumPy prend la première position du maximum": 4, '
         '"on demande la position du maximum, pas sa valeur": 9}'),
    ]),
    Paper("R3.12", "Évaluer un polynôme par le schéma de Horner", [
        ("a", "a number", "((2 * 2 - 3) * 2 + 4) * 2 - 5", ""),
        ("b", "the list of the running values, in order", "[2, 1, 6, 7]",
         'mistakes={"multiplie la valeur courante par x avant d\'ajouter le coefficient suivant": [2, -1, 3, -2]}'),
        ("c", "a number", "-5", 'mistakes={"n\'oublie pas le coefficient nul du terme en x³": -7}'),
        ("d", "an integer", "4",
         'mistakes={"Horner ne calcule aucune puissance : une multiplication par étape": 10}'),
    ]),
    Paper("R3.15", "Une fonction de coût donnée par une formule : une parabole et son sommet", [
        ("a", "a number", "Fraction(2, 100) * 10**2 - Fraction(12, 10) * 10 + 25", 'kind="fraction"'),
        ("b", "a number", "30", 'mistakes={"on demande le nombre d\'epochs, pas l\'erreur minimale": 7}'),
        ("c", "a number", "Fraction(2, 100) * 30**2 - Fraction(12, 10) * 30 + 25",
         'kind="fraction", mistakes={"on demande l\'erreur minimale, pas le nombre d\'epochs": 30}'),
        ("d", "an interval, as text", '"[0 ; 30]"',
         'kind="interval", mistakes={"l\'erreur diminue avant le sommet, pas après": "[30 ; +oo[", '
         '"un intervalle de variation se donne avec ses bornes, fermé du côté du sommet": "[0 ; 30["}'),
        ("e", "an interval, as text", '"[20 ; 40]"',
         'kind="interval", mistakes={"a > 0 : E(t) − 9 est négatif entre ses racines": "]-oo ; 20] U [40 ; +oo[", '
         '"« ne dépasse pas » : les bornes sont incluses": "]20 ; 40[", '
         '"a > 0 : E(t) − 9 est négatif entre ses racines, pas à l\'extérieur": "[0 ; 20] U [40 ; +oo[", '
         '"E(t) ≤ 9 est vrai entre les racines : à l\'extérieur, l\'erreur dépasse 9": "[0 ; 20[ U ]40 ; +oo["}'),
    ]),
]

PAPER_CONTEXT = "# Part 0: the answers are computed exactly from the statements\nfrom fractions import Fraction"

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ R3.1 à R3.12, 📈 R3.2, 🔗 R3.15)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un nombre avec un point décimal, `-1.5` ; une fraction exacte entre guillemets, `\"5/7\"` ;\n"
               "- une liste de coefficients, du plus haut degré au terme constant, zéros compris : `[2, 0, -5]` "
               "pour $2x^2 - 5$ ;\n"
               "- une liste de valeurs (solutions, antécédents, racines) dans l'ordre que tu veux, la liste vide s'il "
               "n'y en a aucune ; une fraction s'y écrit comme un calcul : `[-2/7, 6]` ;\n"
               "- un intervalle entre guillemets, `\"]-1 ; 4]\"` ou `\"[0 ; +oo[\"`, une réunion avec un U ;\n"
               "- une fonction affine par la liste `[m, c]`, une forme canonique par `[a, alpha, beta]` ;\n"
               "- vrai ou faux par `True` ou `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Part A: reference functions and clean figures (R3.21, R3.26)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np

from wbm.nbtools import checked, drawn, run_pytest_group


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

R3_21_CHECK = '''with checked("R3.21 vérifications"):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    try:
        created = drawn(plot_reference, axes)
    finally:
        plt.close(fig)                                 # only the checks below are shown here
    problems = []
    if created:
        problems.append("un dessin dans les axes reçus (axes[0].plot, axes[1].plot), sans créer de figure")
    else:
        if len(axes[0].lines) < 3:
            problems.append("les trois courbes x, x² et √x dans axes[0]")
        if len(axes[1].lines) < 2:
            problems.append("les courbes de 1/x et de x dans axes[1]")
        if any(ax.get_legend() is None for ax in axes):
            problems.append("une légende dans chaque graphique (label=, puis ax.legend())")
        for line in axes[1].lines:                     # 1/x drawn in one piece: a vertical line that does not exist
            xs = np.asarray(line.get_xdata(), dtype=float)
            ys = np.asarray(line.get_ydata(), dtype=float)
            ok = np.isfinite(xs) & np.isfinite(ys) & (xs != 0)
            if ok.sum() > 2 and np.allclose(xs[ok] * ys[ok], 1) and xs[ok].min() < 0 < xs[ok].max():
                problems.append("1/x en deux morceaux, un de chaque côté de 0, et non d'un seul trait")
                break
    if problems:
        print("❌ Ex R3.21 : il manque " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex R3.21 : deux graphiques avec leurs courbes et leurs légendes, et 1/x en deux morceaux.")'''

R3_21 = Ex(
    "R3.21", "📦", 1, 15, "Tracer et lire les fonctions de référence",
    "tracer des fonctions avec NumPy et matplotlib, lire leurs positions relatives, puis les justifier par le calcul.",
    "fiche §2 et §4 ; R0 (matplotlib)", tracks="C, E",
    body="""Avec NumPy, une fonction s'applique à tout un tableau d'un coup : `xs = np.linspace(0, 3, 300)` fabrique 300 abscisses régulières, et `np.sqrt(xs)`, `xs**2`, `np.abs(xs)` ou `1 / xs` calculent les images de toutes ces abscisses.

Complète `plot_reference(axes)`, qui dessine **dans les deux axes qu'on lui donne**, côte à côte : la cellule de vérification les crée (`plt.subplots(1, 2)`), et tu dessines avec `axes[0].plot(...)` et `axes[1].plot(...)`, sans créer de figure.
- Dans `axes[0]`, sur $[0 \\;;\\; 3]$ : les courbes de $x$, de $x^2$ et de $\\sqrt{x}$, avec une légende.
- Dans `axes[1]`, sur $[-3 \\;;\\; 3]$ : les courbes de $\\frac{1}{x}$ et de $x$. Attention : $\\frac{1}{x}$ n'est pas définie en 0 ; trace-la en **deux morceaux**, sur $[-3 \\;;\\; -0{,}1]$ et sur $[0{,}1 \\;;\\; 3]$, sinon matplotlib relie les deux branches par un trait vertical qui n'existe pas.

Puis, en lisant tes figures **et** en le justifiant par le calcul dans ta copie :
- a) l'intervalle de $]0 \\;;\\; +\\infty[$ sur lequel $\\sqrt{x} > x$ ;
- b) l'ensemble des réels $x$ (pas seulement ceux de la figure) tels que $x^2 > x$ ;
- c) les abscisses des points communs aux courbes de $\\frac{1}{x}$ et de $x$.""",
    todo='''def plot_reference(axes):
    """axes[0]: x, x² and √x on [0, 3]. axes[1]: 1/x (in two pieces) and x on [−3, 3]. Legends, titles, axis labels."""
    raise NotImplementedError("trace les deux graphiques dans axes[0] et axes[1]")


answer_R3_21a = ...  # a) an interval, as text
answer_R3_21b = ...  # b) an interval or a union, as text
answer_R3_21c = ...  # c) a list''',
    check='''with checked("R3.21 figure"):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    try:
        created = drawn(plot_reference, axes)
    except BaseException:
        plt.close(fig)                                 # no empty figure while plot_reference is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex R3.21 : ta fonction ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans les axes "
              "qu'elle reçoit, avec axes[0].plot(...) et axes[1].plot(...).")
    else:
        plt.show()
for letter, answer in zip("abc", [answer_R3_21a, answer_R3_21b, answer_R3_21c]):
    wbm.check(f"R3.21{letter}", answer)''',
    solution='''def plot_reference(axes):
    """axes[0]: x, x² and √x on [0, 3]. axes[1]: 1/x (in two pieces) and x on [−3, 3]. Legends, titles, axis labels."""
    xs = np.linspace(0, 3, 300)
    axes[0].plot(xs, xs, label="x")
    axes[0].plot(xs, xs**2, label="x²")
    axes[0].plot(xs, np.sqrt(xs), label="√x")
    axes[0].set_title("x, x² et √x sur [0 ; 3]")
    left, right = np.linspace(-3, -0.1, 200), np.linspace(0.1, 3, 200)
    axes[1].plot(left, 1 / left, color="C3", label="1/x")
    axes[1].plot(right, 1 / right, color="C3")
    xs2 = np.linspace(-3, 3, 200)
    axes[1].plot(xs2, xs2, color="C0", label="x")
    axes[1].set_ylim(-4, 4)
    axes[1].set_title("1/x et x sur [−3 ; 3]")
    for ax in axes:
        ax.axhline(0, color="gray", linewidth=0.6)
        ax.axvline(0, color="gray", linewidth=0.6)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True, alpha=0.3)
        ax.legend()


fig, axes = plt.subplots(1, 2, figsize=(10, 4))
plot_reference(axes)
plt.show()
answer_R3_21a, answer_R3_21b, answer_R3_21c = "]0 ; 1[", "]-oo ; 0[ U ]1 ; +oo[", [-1, 1]''',
    record='''wbm.record("R3.21a", "]0 ; 1[", kind="interval",
           mistakes={"pour x > 1, la droite y = x passe au-dessus de la racine carrée": "]1 ; +oo[",
                     "en 1, √x et x sont égaux : la borne est exclue": "]0 ; 1]"})
wbm.record("R3.21b", "]-oo ; 0[ U ]1 ; +oo[", kind="interval",
           mistakes={"x² > x vaut aussi pour les négatifs : x² est positif, x est négatif": "]1 ; +oo[",
                     "x² − x = x(x − 1) : positif à l'extérieur des racines, pas entre elles": "]0 ; 1["})
wbm.record("R3.21c", [-1, 1], ordered=False,
           mistakes={"1/x = x revient à x² = 1 : deux solutions, opposées": [1]})''',
    after=[("md", "**Vérifications automatiques** (la figure elle-même se juge à l'œil)."), ("code", R3_21_CHECK)],
    note="Pour b), $x^2 > x \\iff x^2 - x > 0 \\iff x(x - 1) > 0$ : un produit de deux facteurs, positif quand ils ont "
         "le même signe, donc pour $x < 0$ ou $x > 1$. La figure de gauche ne montre que $[0 \\;;\\; 3]$ : elle ne "
         "pouvait pas révéler les négatifs. Une lecture graphique suggère ; le calcul conclut.",
)

R3_26_CHECK = '''with checked("R3.26 vérifications"):
    fig, ax = plt.subplots(figsize=(6.5, 4))
    try:
        created = drawn(plot_cost, ax)
    finally:
        plt.close(fig)                                 # only the checks below are shown here
    problems = []
    if created:
        problems.append("un dessin dans l'axe ax reçu (ax.plot, ax.axhline…), sans créer de figure ni appeler plt.plot")
    elif not ax.get_title():
        problems.append("un titre (`ax.set_title`)")
    if not created and (not ax.get_xlabel() or not ax.get_ylabel()):
        problems.append("les deux axes nommés (`ax.set_xlabel`, `ax.set_ylabel`)")
    if not created and ax.get_legend() is None:
        problems.append("une légende (`label=` dans chaque `plot`, puis `ax.legend()`)")
    if not created and len(ax.lines) + len(ax.collections) < 3:          # ax.scatter or ax.hlines count too
        problems.append("la courbe, la droite du budget et le point du minimum (trois tracés au moins)")
    if problems:
        print("❌ Ex R3.26 : il manque " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex R3.26 : titre, axes nommés, légende et trois tracés ; compare ta figure à celle de "
              "05_solutions.ipynb.")'''

R3_26 = Ex(
    "R3.26", "🛠️", 1, 15, "Un graphique propre : titre, axes, légende",
    "produire une figure qu'on peut montrer : titre, axes nommés avec leur unité, légende, point remarquable annoté.",
    "fiche §2, l'encadré « Un graphique propre » ; R0 (matplotlib)", tracks="C",
    body="""Une usine estime son coût de production par $C(q) = 0{,}5\\,q^2 - 20\\,q + 300$, en milliers d'euros, pour $q$ (en tonnes) entre 0 et 40. Son budget est de 150 milliers d'euros.

Complète `plot_cost(ax)`, qui dessine **dans l'axe `ax` qu'on lui donne** :
- la courbe de $C$ sur $[0 \\;;\\; 40]$ ;
- la droite horizontale du budget (`ax.axhline`) ;
- le point du minimum de $C$ (calcule-le d'abord à la main : §5), marqué d'un rond et annoté (`ax.annotate`) ;
- un titre, les axes nommés **avec leurs unités**, une légende, une grille.

La première cellule de vérification affiche ta figure ; la seconde regarde automatiquement qu'il ne manque rien d'essentiel. Compare ensuite ta figure à celle de `05_solutions.ipynb` : plusieurs mises en forme sont justes. Dans ta copie, lis sur ta figure les productions qui respectent le budget.""",
    todo='''def plot_cost(ax):
    """Draw C(q) = 0.5 q² − 20 q + 300 on [0, 40], the budget line y = 150 and the marked minimum, in ax."""
    raise NotImplementedError("dessine la courbe, le budget et le minimum dans ax")''',
    check='''with checked("R3.26"):
    fig, ax = plt.subplots(figsize=(6.5, 4))
    try:
        created = drawn(plot_cost, ax)
    except BaseException:
        plt.close(fig)                                 # no empty figure while plot_cost is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex R3.26 : ta fonction ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans l'axe ax "
              "qu'elle reçoit (ax.plot, ax.axhline, ax.set_title…).")
    else:
        plt.show()''',
    solution='''def plot_cost(ax):
    """Draw C(q) = 0.5 q² − 20 q + 300 on [0, 40], the budget line y = 150 and the marked minimum, in ax."""
    qs = np.linspace(0, 40, 200)
    ax.plot(qs, 0.5 * qs**2 - 20 * qs + 300, label="coût C(q)")
    ax.axhline(150, color="C3", linestyle="--", label="budget : 150 k€")
    ax.plot(20, 100, "o", color="black", label="minimum")
    ax.annotate("minimum : 100 k€\\npour 20 t", (20, 100), xytext=(23, 160), arrowprops={"arrowstyle": "->"})
    ax.set_title("Coût de production en fonction de la quantité")
    ax.set_xlabel("quantité produite q (tonnes)")
    ax.set_ylabel("coût C(q) (milliers d'euros)")
    ax.grid(True, alpha=0.3)
    ax.legend()


fig, ax = plt.subplots(figsize=(6.5, 4))
plot_cost(ax)
plt.show()''',
    after=[("md", "**Vérifications automatiques** : ce qu'une figure à montrer doit contenir."),
           ("code", R3_26_CHECK)],
    note="Le minimum est au sommet : $\\alpha = -\\frac{-20}{2 \\times 0{,}5} = 20$ tonnes, et $C(20) = 200 - 400 + 300 "
         "= 100$ milliers d'euros. Le budget est respecté quand la courbe est sous la droite : $C(q) \\le 150 \\iff "
         "q^2 - 40q + 300 \\le 0$, entre les racines 10 et 30, soit de 10 à 30 tonnes.",
)

PART_A = Part("A", "Fonctions de référence et graphiques",
              "Fiche §2 et §4. Tracer des fonctions avec NumPy, lire leurs positions relatives, et faire une figure "
              "qu'on peut montrer.", given=TOOLS, exercises=[R3_21, R3_26])

# ---------------------------------------------------------------------------
# Part B: affine functions and quadratics (R3.18, R3.19, R3.22, R3.24)
# ---------------------------------------------------------------------------
LOAD_LEARNER = 'mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="R3")  # reload your saved file'
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en R2). Ouvre ta copie `mon_travail/mymath/functions.py`, lis la docstring "
         "de la fonction en entier, remplace la ligne `raise NotImplementedError(...)` par ton code, **enregistre** le "
         "fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. Les tests comparent tes "
         "résultats à NumPy et à SymPy : écris le calcul toi-même, sans les appeler.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of functions.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_r3_functions.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_r3_functions.py", "{keyword}", impl="ref")')]


R3_18 = Ex(
    "R3.18", "🔨", 1, 25, "La fonction affine qui passe par deux points · `affine_from_points`",
    "programmer le calcul de la pente et de l'ordonnée à l'origine, et refuser une droite verticale.",
    "fiche §3 ; workbookIA 0A §100.6.2 (`raise`)", tracks="C, E", mymath="functions.py",
    body=HOWTO + """

Écris `affine_from_points(p, q)` : `p` et `q` sont deux points `(x, y)`. Dépaquette-les (`(x1, y1), (x2, y2) = p, q`), lève une `ValueError` si leurs abscisses sont égales (une droite verticale n'est pas la courbe d'une fonction), puis calcule la pente et l'ordonnée à l'origine (fiche §3) ; rends le tuple `(m, c)`, deux flottants.

La vérification calcule `affine_from_points((-1, 4), (3, -4))`, puis le nom de l'erreur levée pour deux points de même abscisse (avec `raised`, de la cellule des outils).""",
    todo=LOAD_LEARNER,
    check='''with checked("R3.18a"):
    wbm.check("R3.18a", list(mymath.functions.affine_from_points((-1, 4), (3, -4))), computed=True)
with checked("R3.18b"):
    wbm.check("R3.18b", raised(mymath.functions.affine_from_points, (2, 1), (2, 5)), computed=True)''',
    solution=LOAD_REF + '''
print("affine_from_points((-1, 4), (3, -4)) =", mymath.functions.affine_from_points((-1, 4), (3, -4)))
print("même abscisse :", raised(mymath.functions.affine_from_points, (2, 1), (2, 5)))''',
    record='''wbm.record("R3.18a", [-2.0, 2.0], decimals=4,
           mistakes={"la pente est (y₂ − y₁)/(x₂ − x₁) : même ordre en haut et en bas": [2.0, 6.0],
                     "c = y₁ − m·x₁ : attention au signe de x₁": [-2.0, 6.0],
                     "rends le couple dans l'ordre (m, c)": [2.0, -2.0]})
wbm.record("R3.18b", "ValueError",
           mistakes={"teste x1 == x2 avant de diviser, et lève une ValueError": "ZeroDivisionError",
                     "deux points de même abscisse : la fonction doit lever une ValueError (raise), pas rendre un "
                     "résultat": "aucune",
                     "lève précisément une ValueError, le type d'erreur que demande la docstring : "
                     "raise ValueError(\\"...\\")": {"Exception", "TypeError", "AssertionError"}})''',
    after=tests_cells("test_affine_from_points_"),
)

R3_19 = Ex(
    "R3.19", "🔨", 2, 40, "Racines et sommet d'un polynôme du second degré · `quadratic_roots`, `quadratic_vertex`",
    "programmer les trois cas du discriminant et la forme canonique.",
    "fiche §5 ; R3.18", tracks="C, E", mymath="functions.py",
    body="""Dans `mon_travail/mymath/functions.py` :
- a) `quadratic_roots(a, b, c)` : une `ValueError` si `a == 0` ; sinon le discriminant décide (fiche §5) : deux racines (`math.sqrt`, rendues dans l'ordre croissant, même quand `a` est négatif), une racine double, ou la liste vide. Compare le discriminant à 0 avec `==` : les tests de la racine double utilisent des entiers. Le squelette n'importe pas `math` : ajoute `import math` en haut du fichier.
- b) `quadratic_vertex(a, b, c)` : une `ValueError` si `a == 0` ; sinon le tuple `(alpha, beta)` de la forme canonique.

La vérification calcule `quadratic_roots(-2, 7, -3)`, regarde si `quadratic_roots(1, 2, 3)` vaut bien `[]`, puis calcule `quadratic_vertex(-1, 6, -5)`.""",
    todo=LOAD_LEARNER,
    check='''with checked("R3.19a"):
    wbm.check("R3.19a", mymath.functions.quadratic_roots(-2, 7, -3), computed=True)
with checked("R3.19b"):
    wbm.check("R3.19b", mymath.functions.quadratic_roots(1, 2, 3) == [], computed=True)
with checked("R3.19c"):
    wbm.check("R3.19c", list(mymath.functions.quadratic_vertex(-1, 6, -5)), computed=True)''',
    solution=LOAD_REF + '''
print("quadratic_roots(-2, 7, -3)  =", mymath.functions.quadratic_roots(-2, 7, -3))
print("quadratic_roots(1, 2, 3)    =", mymath.functions.quadratic_roots(1, 2, 3))
print("quadratic_vertex(-1, 6, -5) =", mymath.functions.quadratic_vertex(-1, 6, -5))''',
    record='''wbm.record("R3.19a", [0.5, 3.0], decimals=4,
           mistakes={"le dénominateur est 2a, pas 2": [-6.0, -1.0],
                     "rends les racines dans l'ordre croissant : avec a négatif, (−b − √Δ)/(2a) est la plus grande":
                         [3.0, 0.5],
                     "priorités : -b + math.sqrt(d) / 2 * a ne divise que la racine, puis multiplie par a ; "
                     "écris (-b + math.sqrt(d)) / (2 * a)": [-12.0, -2.0],
                     "priorités : -b + math.sqrt(d) / 2 * a ne divise que la racine ; écris (-b + math.sqrt(d)) / "
                     "(2 * a), et rends les racines dans l'ordre croissant": [-2.0, -12.0],
                     "priorités : / 2 * a divise par 2 puis multiplie par a ; écris / (2 * a)": [2.0, 12.0],
                     "priorités : / 2 * a divise par 2 puis multiplie par a ; écris / (2 * a), et rends les racines "
                     "dans l'ordre croissant": [12.0, 2.0]})
wbm.record("R3.19b", True,
           mistakes={"un discriminant négatif : pas de racine réelle, la fonction doit rendre la liste vide": False})
wbm.record("R3.19c", [3.0, 4.0], decimals=4,
           mistakes={"α = −b/(2a) : avec a négatif, attention au signe": [-3.0, -32.0],
                     "β = c − b²/(4a) : attention au signe": [3.0, -14.0]})''',
    after=tests_cells("test_quadratic_roots_ or test_quadratic_vertex_"),
    note="Le tri compte quand `a` est négatif : $\\frac{-b - \\sqrt{\\Delta}}{2a}$ est alors la **plus grande** "
         "racine (on divise par un négatif). `sorted([...])` règle la question sans réfléchir au signe.",
)

R3_22_CHECK = '''with checked("R3.22 vérifications"):
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
    try:
        created = drawn(plot_families, axes)
    finally:
        plt.close(fig)
    problems = []
    if created:
        problems.append("un dessin dans les axes reçus (axes[0].plot…), sans créer de figure")
    elif any(len(ax.lines) < 3 for ax in axes):
        problems.append("au moins trois paraboles dans chacun des trois graphiques")
    if not created and not all(ax.get_title() for ax in axes):
        problems.append("un titre par graphique, qui dit quel paramètre varie")
    if problems:
        print("❌ Ex R3.22 : il manque " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex R3.22 : trois familles de paraboles, chacune avec son titre ; à toi de conclure dans ta copie.")'''

R3_22 = Ex(
    "R3.22", "🎨", 2, 20, "Faire varier a, b et c : déformer une parabole",
    "voir ce que chaque paramètre fait à une parabole, et pourquoi la forme canonique le dit d'un coup d'œil.",
    "fiche §5", tracks="C, E",
    body="""Complète `plot_families(axes)`, qui reçoit trois axes côte à côte et trace, sur $[-4 \\;;\\; 4]$ :
1. dans `axes[0]`, la famille $y = a\\,x^2$ pour $a \\in \\{-2, -0{,}5, 0{,}5, 1, 2\\}$ ;
2. dans `axes[1]`, la famille $y = x^2 + c$ pour $c \\in \\{-3, 0, 2\\}$ ;
3. dans `axes[2]`, la famille $y = (x - h)^2$ pour $h \\in \\{-2, 0, 3\\}$.

Une légende dans chaque graphique (la valeur du paramètre), un titre, la même fenêtre verticale $[-6 \\;;\\; 8]$ partout pour comparer.

Puis réponds dans ta copie : que fait $a$ (son signe, sa taille) ? que fait $c$ ? que fait $h$ ? En déduire, sans calcul, à quoi ressemble la courbe de $y = 2(x - 3)^2 - 1$ par rapport à celle de $y = x^2$. Et le coefficient $b$ de $ax^2 + bx + c$ : pourquoi est-il plus difficile à « lire » que $a$, $\\alpha$ et $\\beta$ ?""",
    todo='''def plot_families(axes):
    """Three families of parabolas: y = a x², y = x² + c, y = (x − h)², one per axis, with legends and titles."""
    raise NotImplementedError("trace les trois familles")''',
    check='''with checked("R3.22"):
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
    try:
        created = drawn(plot_families, axes)
    except BaseException:
        plt.close(fig)
        raise
    if created:
        plt.close(fig)
        print("❌ Ex R3.22 : ta fonction ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans les trois "
              "axes qu'elle reçoit (axes[0].plot, axes[1].plot, axes[2].plot).")
    else:
        plt.show()''',
    solution='''def plot_families(axes):
    """Three families of parabolas: y = a x², y = x² + c, y = (x − h)², one per axis, with legends and titles."""
    xs = np.linspace(-4, 4, 300)
    for a in (-2, -0.5, 0.5, 1, 2):
        axes[0].plot(xs, a * xs**2, label=f"a = {a}")
    for c in (-3, 0, 2):
        axes[1].plot(xs, xs**2 + c, label=f"c = {c}")
    for h in (-2, 0, 3):
        axes[2].plot(xs, (xs - h) ** 2, label=f"h = {h}")
    titles = ["y = a·x² : a ouvre, ferme, retourne", "y = x² + c : c monte ou descend",
              "y = (x − h)² : h décale à gauche ou à droite"]
    for ax, title in zip(axes, titles):
        ax.set_ylim(-6, 8)
        ax.axhline(0, color="gray", linewidth=0.6)
        ax.axvline(0, color="gray", linewidth=0.6)
        ax.set_title(title, fontsize=10)
        ax.set_xlabel("x")
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=8)


fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
plot_families(axes)
plt.show()''',
    after=[("md", "**Vérifications automatiques** (la figure elle-même se juge à l'œil)."), ("code", R3_22_CHECK)],
    note="$a$ règle l'ouverture (plus $|a|$ est grand, plus la parabole est fermée) et le sens ($a < 0$ la retourne) ; "
         "$c$ la translate verticalement ; $h$ la translate horizontalement, vers la droite quand $h > 0$ (le signe "
         "moins de $(x - h)$ trompe souvent). Donc $2(x - 3)^2 - 1$ est la parabole $y = x^2$ resserrée d'un facteur 2, "
         "puis décalée de 3 vers la droite et de 1 vers le bas : sommet $(3 \\;;\\; -1)$. Le coefficient $b$, lui, "
         "déplace le sommet en biais : il change à la fois $\\alpha$ et $\\beta$.",
)

R3_24_PLOT = '''with checked("R3.24 figure"):
    bs, cs = np.meshgrid(range(-5, 6), range(-5, 6))
    deltas = bs**2 - 4 * cs
    grid = np.linspace(-5, 5, 200)
    frontier = boundary(grid)                     # before the figure: no half-drawn figure if boundary is not written
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    for mask, colour, label in [(deltas > 0, "C0", "Δ > 0 : deux racines"), (deltas == 0, "C3", "Δ = 0 : une racine"),
                                (deltas < 0, "C2", "Δ < 0 : aucune racine")]:
        ax.scatter(bs[mask], cs[mask], color=colour, label=label, s=30)
    ax.plot(grid, frontier, color="black", linewidth=1.2, label="ta frontière")
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 6.5)
    ax.set_xlabel("b")
    ax.set_ylabel("c")
    ax.set_title("Nombre de racines de x² + bx + c")
    ax.legend(fontsize=8, loc="upper left", bbox_to_anchor=(1.01, 1))
    plt.show()'''

R3_24 = Ex(
    "R3.24", "🔬", 2, 20, "Combien de racines ? Le signe du discriminant sur une grille de paramètres",
    "voir sur une grille de paramètres quand un second degré a deux, une ou aucune racine, et trouver la frontière.",
    "fiche §5 ; R3.19", tracks="C",
    body="""On étudie tous les polynômes $x^2 + bx + c$ avec $b$ et $c$ **entiers** de $-5$ à $5$ : 121 polynômes.

- a) Écris `count_roots()` : la liste `[n2, n1, n0]`, où `n2` est le nombre de ces polynômes qui ont deux racines, `n1` le nombre qui en ont une, et `n0` le nombre qui n'en ont aucune. Deux boucles `for` imbriquées et le discriminant suffisent (ou ta fonction `quadratic_roots` de R3.19).
- b) Sur la figure de l'expérience, les points « une racine » sont sur une courbe qui sépare les deux autres familles. Écris `boundary(b)`, qui donne le $c$ de cette frontière en fonction de $b$ (il s'agit de résoudre $\\Delta = 0$ en $c$), puis donne son expression en `b`, entre guillemets.

L'expérience colore les 121 points selon le signe de $\\Delta$ et trace ta frontière par-dessus.""",
    todo='''def count_roots():
    """[n2, n1, n0]: how many x² + bx + c (b, c integers from −5 to 5) have two, one or no real root."""
    raise NotImplementedError("compte avec deux boucles et le discriminant")


def boundary(b):
    """The c for which x² + bx + c has exactly one root (works on a NumPy array of b)."""
    raise NotImplementedError("résous Δ = 0 en c")


answer_R3_24b = ...  # b) the expression of the boundary c in terms of b, as text, e.g. "3*b - 1"''',
    check='''with checked("R3.24a"):
    wbm.check("R3.24a", count_roots(), computed=True)
wbm.check("R3.24b", answer_R3_24b)''',
    solution='''def count_roots():
    """[n2, n1, n0]: how many x² + bx + c (b, c integers from −5 to 5) have two, one or no real root."""
    counts = [0, 0, 0]
    for b in range(-5, 6):
        for c in range(-5, 6):
            delta = b * b - 4 * c
            counts[0 if delta > 0 else 1 if delta == 0 else 2] += 1
    return counts


def boundary(b):
    """The c for which x² + bx + c has exactly one root (works on a NumPy array of b)."""
    return b**2 / 4


print("deux, une, aucune racine :", count_roots())
answer_R3_24b = "b**2/4"''',
    record='''wbm.record("R3.24a", [85, 5, 31],
           mistakes={"l'ordre demandé est [deux racines, une racine, aucune racine]": [31, 5, 85],
                     "b et c vont de −5 à 5 inclus : range(-5, 6) dans les deux boucles": [73, 5, 22],
                     "b va de −5 à 5 inclus : range(-5, 6) aussi pour b": [74, 5, 31],
                     "c va de −5 à 5 inclus : range(-5, 6) aussi pour c": [83, 5, 22]})
wbm.record("R3.24b", "b**2/4", kind="expr", variables=("b",),
           mistakes={"Δ = b² − 4c = 0 : isole c, en divisant par 4": "b**2",
                     "Δ = b² − 4ac avec a = 1 : il y a un facteur 4": "b**2/2"})''',
    after=[("md", "**L'expérience** : les 121 polynômes, colorés selon le signe du discriminant, et ta frontière."),
           ("code", R3_24_PLOT)],
    note="Les polynômes à une racine sont ceux où $c = \\frac{b^2}{4}$ est entier : $b$ pair, soit 5 points. "
         "Au-dessous de la parabole $c = \\frac{b^2}{4}$ (pour $c$ petit), $\\Delta > 0$ : deux racines ; au-dessus, "
         "aucune. Tirer $b$ et $c$ au hasard donne bien plus souvent deux racines : 85 fois sur 121 ici.",
)

PART_B = Part("B", "Fonctions affines et second degré",
              "Fiche §3 et §5. Tes premières fonctions de `mymath/functions.py`, une famille de paraboles à déformer, "
              "et une grille de discriminants.", exercises=[R3_18, R3_19, R3_22, R3_24])

# ---------------------------------------------------------------------------
# Part C: composition, reciprocal, polynomials (R3.20, R3.23, R3.25, R3.17)
# ---------------------------------------------------------------------------
R3_20 = Ex(
    "R3.20", "🔨", 1, 25, "Composer deux fonctions · `compose`",
    "programmer une fonction qui fabrique une fonction (une fermeture), dans le bon ordre.",
    "fiche §7 ; workbookIA 0A §100.5.3 (fonctions comme valeurs) et §100.5.4 (fermetures)", tracks="C, E",
    mymath="functions.py",
    body="""Écris `compose(f, g)` dans `mon_travail/mymath/functions.py` : elle **renvoie une nouvelle fonction**, qui à `x` associe `f(g(x))`. Définis cette fonction à l'intérieur de `compose` (une fermeture, comme `then_add` dans la fiche §7), puis renvoie-la **sans l'appeler**.

La vérification fabrique $x \\mapsto (x - 1)^2$ et $x \\mapsto x^2 - 1$ avec `compose`, et les calcule en 4.""",
    todo=LOAD_LEARNER,
    check='''with checked("R3.20"):
    square_after = mymath.functions.compose(lambda t: t**2, lambda t: t - 1)
    minus_after = mymath.functions.compose(lambda t: t - 1, lambda t: t**2)
    wbm.check("R3.20", [square_after(4), minus_after(4)], computed=True)''',
    solution=LOAD_REF + '''
square_after = mymath.functions.compose(lambda t: t**2, lambda t: t - 1)
minus_after = mymath.functions.compose(lambda t: t - 1, lambda t: t**2)
print("(x − 1)² en 4 :", square_after(4), " ;  x² − 1 en 4 :", minus_after(4))''',
    record='''wbm.record("R3.20", [9, 15],
           mistakes={"compose(f, g) applique g d'abord, puis f": [15, 9]})''',
    after=tests_cells("test_compose_"),
    note="`return composite` (sans parenthèses) renvoie la fonction elle-même ; `return composite(x)` n'aurait pas de "
         "sens ici, puisque `compose` ne reçoit pas de `x`. C'est exactement ce que fait une couche suivie d'une "
         "activation dans un réseau : une composée, construite une fois, appelée sur chaque donnée.",
)

R3_23_EXPERIMENT = '''f = abs
g = lambda t: t - 3
print("(f∘g)(1) =", f(g(1)), " ; (g∘f)(1) =", g(f(1)))
print("(f∘g)(−2) =", f(g(-2)), " ; (g∘f)(−2) =", g(f(-2)))
xs = np.linspace(-5, 7, 400)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(xs, np.abs(xs - 3), label="(f∘g)(x) = |x − 3|", linewidth=2.2)
ax.plot(xs, np.abs(xs) - 3, "--", label="(g∘f)(x) = |x| − 3", linewidth=2.2)
ax.axhline(0, color="gray", linewidth=0.6)
ax.axvline(0, color="gray", linewidth=0.6)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Deux ordres, deux fonctions")
ax.grid(True, alpha=0.3)
ax.legend()
plt.show()'''

R3_23 = Ex(
    "R3.23", "🔮", 1, 10, "Prédire f∘g et g∘f pour « valeur absolue » et « moins 3 »",
    "prévoir le résultat d'une composée dans les deux ordres, puis le voir sur les courbes.",
    "fiche §7", tracks="C", hypothesis=True,
    body="""On pose $f(x) = |x|$ (« valeur absolue ») et $g(x) = x - 3$ (« moins 3 »). **Avant d'exécuter quoi que ce soit**, prédis :
- a) $(f \\circ g)(1)$ ;
- b) $(g \\circ f)(1)$ ;
- c) $(f \\circ g)(-2)$ ;
- d) $(g \\circ f)(-2)$.

Écris tes quatre prédictions, vérifie-les, puis lance l'expérience : elle calcule les quatre valeurs et trace les deux composées. Dans ta copie : pour quels $x$ les deux composées sont-elles égales ? Pourquoi ?""",
    todo='''prediction_R3_23a = ...  # a) a number, written BEFORE running the experiment below
prediction_R3_23b = ...  # b) a number
prediction_R3_23c = ...  # c) a number
prediction_R3_23d = ...  # d) a number''',
    check='''for letter, prediction in zip("abcd", [prediction_R3_23a, prediction_R3_23b, prediction_R3_23c,
                                       prediction_R3_23d]):
    wbm.check(f"R3.23{letter}", prediction)''',
    record='''wbm.record("R3.23a", abs(1 - 3), prediction=True,
           mistakes={"f∘g applique g d'abord (moins 3), puis la valeur absolue": -2})
wbm.record("R3.23b", abs(1) - 3, prediction=True,
           mistakes={"g∘f applique f d'abord (la valeur absolue), puis moins 3": 2})
wbm.record("R3.23c", abs(-2 - 3), prediction=True,
           mistakes={"f∘g : on retire 3 d'abord, puis on prend la valeur absolue du résultat": -1,
                     "−2 − 3 se calcule avec les signes avant de prendre la valeur absolue": 1})
wbm.record("R3.23d", abs(-2) - 3, prediction=True,
           mistakes={"g∘f : la valeur absolue d'abord, puis on retire 3": 5})''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(R3_23_EXPERIMENT, ["prediction_R3_23a", "prediction_R3_23b", "prediction_R3_23c",
                                            "prediction_R3_23d"],
                         "⏳ Écris d'abord tes quatre prédictions (des nombres), puis exécute à nouveau.")),
        ("solution", R3_23_EXPERIMENT),
    ],
    note="Les deux courbes coïncident pour $x \\ge 3$ : alors $x - 3 \\ge 0$ et $x \\ge 0$, donc $|x - 3| = x - 3$ et "
         "$|x| - 3 = x - 3$. Pour $x < 3$, $|x - 3|$ est positif (une distance) alors que $|x| - 3$ peut être négatif. "
         "Même deux fonctions très simples ne commutent pas.",
)

R3_25_MISSING = {"A": "une composée calculée dans le mauvais ordre",
                 "B": "une réciproque confondue avec l'inverse",
                 "C": "des racines qui ont pris le mauvais signe",
                 "F": "un discriminant qui a perdu un signe",
                 "G": "une formule des racines qui ne divise pas tout le numérateur"}

R3_25 = Ex(
    "R3.25", "🐛", 2, 20, "Chasse à l'erreur : composition, réciproque et racines",
    "repérer les erreurs classiques sur les composées, les réciproques et le second degré, et les corriger.",
    "fiche §5, §7 et §8, « Les pièges classiques »", tracks="C, E",
    body="""Un camarade a fait sept calculs. **Sans rien exécuter d'abord**, trouve ceux qui sont faux. On pose $f(x) = 5x - 1$ et $g(x) = x^2$.

| | Calcul |
|---|---|
| A | $(f \\circ g)(x) = (5x - 1)^2$ |
| B | $f^{-1}(x) = \\dfrac{1}{5x - 1}$ |
| C | les racines de $x^2 - 2x - 15$ sont $-5$ et $3$ |
| D | $3x^2 + 6x + 1 = 3(x + 1)^2 - 2$ |
| E | $x \\mapsto 3 - x$ est décroissante sur $\\mathbb{R}$ |
| F | le discriminant de $2x^2 - 3x - 4$ vaut $9 - 32 = -23$ |
| G | pour $4x^2 - 4x - 3$, $\\Delta = 64$, donc les racines sont $4 \\pm \\frac{8}{8}$, soit 3 et 5 |

- a) Les lettres des calculs faux, dans un texte.
- b) Le bon $(f \\circ g)(x)$ : une liste de coefficients.
- c) Les bonnes racines de $x^2 - 2x - 15$ : une liste.
- d) Le bon discriminant de $2x^2 - 3x - 4$.
- e) Les bonnes racines de $4x^2 - 4x - 3$ : une liste.""",
    todo='''answer_R3_25a = ...  # a) the letters of the wrong calculations, as text
answer_R3_25b = ...  # b) a list of coefficients
answer_R3_25c = ...  # c) a list
answer_R3_25d = ...  # d) a number
answer_R3_25e = ...  # e) a list''',
    check='''for letter, answer in zip("abcde", [answer_R3_25a, answer_R3_25b, answer_R3_25c, answer_R3_25d, answer_R3_25e]):
    wbm.check(f"R3.25{letter}", answer)''',
    solution='''import sympy as sp

x = sp.Symbol("x")
f = lambda t: 5 * t - 1
g = lambda t: t**2
print("A : f(g(x)) =", sp.expand(f(g(x))), " ; (5x − 1)² =", sp.expand((5 * x - 1) ** 2))
print("B : f⁻¹(f(2)) doit redonner 2 ; avec la formule proposée, on obtient", 1 / (5 * f(2) - 1), "-> faux")
print("C :", sp.solve(x**2 - 2 * x - 15, x))
print("D :", sp.expand(3 * (x + 1) ** 2 - 2))
print("F :", (-3) ** 2 - 4 * 2 * (-4))
print("G :", sp.solve(4 * x**2 - 4 * x - 3, x))''',
    record=f'''wbm.record("R3.25a", "ABCFG",
           mistakes={bug_letters_mistakes("ABCFG", "DE", R3_25_MISSING)})
wbm.record("R3.25b", [5, 0, -1],
           mistakes={{"f∘g applique g d'abord : on remplace x par x² dans f": [25, -10, 1]}})
wbm.record("R3.25c", [-3, 5], ordered=False,
           mistakes={{"les racines sont (−b ± √Δ)/(2a) : −b est positif ici": [-5, 3]}})
wbm.record("R3.25d", 41,
           mistakes={{"−4ac avec c négatif : moins par moins donne plus": -23}})
wbm.record("R3.25e", [-0.5, 1.5], ordered=False, decimals=4,
           mistakes={{"tout le numérateur −b ± √Δ est divisé par 2a, pas seulement √Δ": [3.0, 5.0]}})''',
    note="Les deux calculs justes ont leur piège apparent : D se vérifie en redéveloppant, $3(x^2 + 2x + 1) - 2 = "
         "3x^2 + 6x + 1$ ; E est une fonction affine de pente $-1$. Pour B, la réciproque de $f$ est "
         "$x \\mapsto \\frac{x + 1}{5}$ : elle défait « fois 5, moins 1 » en faisant « plus 1, divisé par 5 ».",
)

R3_17 = Ex(
    "R3.17", "🔨", 1, 25, "Évaluer un polynôme par Horner · `polyval`",
    "programmer le schéma de Horner, qui évalue un polynôme sans calculer aucune puissance.",
    "fiche §9 ; workbookIA 0A §100.4.2 (boucle `for`)", tracks="C", mymath="functions.py",
    body=HOWTO + """

Écris `polyval(coefficients, x)` : les coefficients vont du plus haut degré au terme constant (fiche §9). Pars de 0, puis, pour chaque coefficient, multiplie la valeur courante par `x` et ajoute le coefficient. Sans `**` : c'est tout l'intérêt du schéma. Avec des entiers, le résultat reste entier ; avec un tableau NumPy en `x`, les mêmes opérations marchent case par case.

La vérification calcule `polyval([1, -2, 0, 3], -2)` et `polyval([0.5, 1], 4)`.""",
    todo=LOAD_LEARNER,
    check='''with checked("R3.17a"):
    wbm.check("R3.17a", mymath.functions.polyval([1, -2, 0, 3], -2), computed=True)
with checked("R3.17b"):
    wbm.check("R3.17b", mymath.functions.polyval([0.5, 1], 4), computed=True)''',
    solution=LOAD_REF + '''
print("polyval([1, -2, 0, 3], -2) =", mymath.functions.polyval([1, -2, 0, 3], -2))
print("polyval([0.5, 1], 4)       =", mymath.functions.polyval([0.5, 1], 4))''',
    record='''wbm.record("R3.17a", -13,
           mistakes={"le premier coefficient va avec le plus haut degré : ne parcours pas la liste à l'envers": -19,
                     "la valeur courante part de 0, pas de 1": 3,
                     "à chaque étape, multiplie d'abord la valeur courante par x, puis ajoute le coefficient": 26})
wbm.record("R3.17b", 3.0, decimals=4,
           mistakes={"le premier coefficient va avec le plus haut degré": 4.5})''',
    after=tests_cells("test_polyval_"),
)

PART_C = Part("C", "Composition, réciproque et polynômes",
              "Fiche §7 à §9. Composer en Python, prédire deux composées, une chasse à l'erreur, et le schéma de "
              "Horner.", exercises=[R3_20, R3_23, R3_25, R3_17])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | R3.1 à R3.12, R3.15 | Les exercices papier (vérification) | ✏️ 📈 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# R3 · Fonctions — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/r3_fonctions/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py R3`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# R3 · Fonctions — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : images, antécédents, lecture graphique, droites, second "
               "degré, variations, composées, réciproques, Horner.\n"
               "- Écrire les cinq fonctions de `mymath/functions.py` et les tester.\n"
               "- Tracer des fonctions avec NumPy, déformer des paraboles, prédire des composées.\n\n"
               "**Rappel express.** Pente $m = \\frac{y_2 - y_1}{x_2 - x_1}$, $c = y_1 - m x_1$ ; "
               "$ax^2 + bx + c = a(x - \\alpha)^2 + \\beta$ avec $\\alpha = -\\frac{b}{2a}$ ; $\\Delta = b^2 - 4ac$ et "
               "racines $\\frac{-b \\pm \\sqrt{\\Delta}}{2a}$ ; $(f \\circ g)(x) = f(g(x))$, $g$ d'abord ; "
               "$f^{-1}(f(x)) = x$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Calcules-tu images et antécédents, lis-tu un graphique et trouves-tu un ensemble de définition ?\n"
               "2. Trouves-tu une droite par deux points, la forme canonique, les racines et le sommet d'un second "
               "degré, et un maximum sur un intervalle ?\n"
               "3. Composes-tu dans le bon ordre, trouves-tu une réciproque, et sais-tu écrire `compose` et `polyval` "
               "en Python ?\n\n"
               "**La suite** : R4, *Logique, ensembles, Σ et Π*. Dans workbookIA, continue le chapitre 0A au rythme de "
               "ton tableau de bord.")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter=CHAPTER) if kind == "exercise" else setup_cell(kind))
    cells += objectives_cell()
    cells += paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO)
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
