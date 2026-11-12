#!/usr/bin/env python
"""Build the two notebooks of chapter M13b from a single source (used by Claude).

    python tools/chapters/build_m13b.py
    python tools/run_all_notebooks.py chapitres/m13b_lagrange_svm/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m13b_lagrange_svm/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M13b.1 to M13b.13, 🔗 M13b.20); parts A to C are the notebook exercises
(M13b.25 to M13b.34). Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it.
The data are new: synthetic (seeds 4225 to 4234 only, never 13xx nor 15xx) or written in the statements; none is a test
case of tests/test_m13b_svm.py, an example of the fiche or of a docstring of svm.py, nor the data of a paper exercise.
Nothing of workbookIA 13 is used: no blobs centred at (0, 0) and (2.5, 2.0), no circles, rings, moons, spirals nor
exclusive or, no MNIST nor penguins, none of the values C = 0.01, 0.1, 1, 100, 1 000, 10⁶ nor their grids, no RBF at
distance 1 with γ = 0.1, 1 or 10, none of its points ((1, 2), (3, 1), (2, 0), (1, 1), (2, 2), (2, −1), (3, 3), (4, 0),
(4, 1), (0, 1), (5, 4), (4, 5), (2, 3)), no direction w ∝ (1, 1), no homogeneous kernel (x · z)².
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M13b"
FOLDER = "chapitres/m13b_lagrange_svm"

F = 'kind="fraction", simplified=True'
FRAC = "an irreducible fraction, as text"
FRACS = "written as calculations or with 6 decimals"
SUM = "C multiplie la SOMME des hinges dans J, pas leur moyenne"
HALF = "½‖w‖² : n'oublie pas le ½"
BIAS = "t = y(w · x + b) : n'oublie pas le biais"
SQUARED = "le noyau RBF élève la distance au CARRÉ : e^(−γ‖x − z‖²)"
STRICT = "ne compte que les marges STRICTEMENT sous 1 : un exemple exactement sur un bord n'entre pas"


def convexity_mistakes() -> str:
    """The ``mistakes`` dict (as source code) of M13b.7 a: one message for each answer that misses one convex problem,
    adds one non-convex problem, or both; three shared messages for the other sets of letters."""
    import itertools

    answer, others = "ADFH", "BCEG"
    missing = {"A": "(A) est convexe : x + y ≥ 1 s'écrit 1 − x − y ≤ 0, une contrainte affine",
               "D": "(D) est convexe : eˣ + y² est convexe, et x − y = 2 est une égalité affine",
               "F": "(F) est convexe : −ln est convexe sur ]0, +∞[, et ses contraintes sont affines",
               "H": "(H) est convexe : max(0, 1 − x) est un maximum de fonctions affines, et une somme de fonctions "
                    "convexes est convexe"}
    extra = {"B": "(B) n'est pas convexe : x² + y² ≥ 1 décrit l'extérieur d'un disque",
             "C": "(C) n'est pas convexe : on y MAXIMISE une fonction convexe",
             "E": "(E) n'est pas convexe : l'égalité x² + y² = 4 n'est pas affine",
             "G": "(G) n'est pas convexe : la hessienne de x² − y² n'est pas semi-définie positive"}
    entries = {}
    for m in answer:
        entries[missing[m]] = "".join(sorted(set(answer) - {m}))
    for e in others:
        entries[extra[e]] = "".join(sorted(set(answer) | {e}))
    for m in answer:
        for e in others:
            entries[f"{extra[e]} ; et {missing[m]}"] = "".join(sorted((set(answer) - {m}) | {e}))
    known = set(entries.values()) | {answer}
    groups: dict[str, list[str]] = {}
    letters = sorted(answer + others)
    for size in range(1, len(letters) + 1):
        for chosen in itertools.combinations(letters, size):
            text = "".join(chosen)
            if text in known:
                continue
            lost, added = set(answer) - set(chosen), set(chosen) - set(answer)
            key = ("plusieurs problèmes convexes manquent : examine l'objectif, chaque inégalité et chaque égalité"
                   if not added else
                   "plusieurs problèmes que tu cites ne sont pas convexes : examine l'objectif, chaque inégalité et "
                   "chaque égalité" if not lost else
                   "il manque des problèmes convexes, et certains que tu cites ne le sont pas : examine l'objectif, "
                   "chaque inégalité et chaque égalité de chacun")
            groups.setdefault(key, []).append(text)
    parts = [f"{json.dumps(k, ensure_ascii=False)}: {json.dumps(v)}" for k, v in entries.items()]
    parts += [f"{json.dumps(k, ensure_ascii=False)}: {{{', '.join(json.dumps(v) for v in values)}}}"
              for k, values in groups.items()]
    return "mistakes={" + ",\n                     ".join(parts) + "}"


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M13b.1", "Lagrange à la main : un produit maximal sous une contrainte linéaire", [
        ("a", "a list of 3 numbers", "POINT_1",
         '''mistakes={"le coefficient 4 rend z « cher » : c'est la plus petite des trois valeurs": [2, 4, 8], '''
         '''"la stationnarité donne yz = λ, xz = 2λ et xy = 4λ : divise ces équations deux à deux": '''
         '''[24 / 7, 24 / 7, 24 / 7]}'''),
        ("b", "a number", "int(PSTAR_1.subs(c_, 24))"),
        ("c", "a number", "int(LAM_1)",
         '''mistakes={"avec ℒ = xyz − λ(x + 2y + 4z − 24), la stationnarité en x donne yz − λ = 0 : regarde le signe de '''
         '''yz": -8}'''),
        ("d", "a number", "int(PSTAR_1.subs(c_, 24) + LAM_1)",
         '''mistakes={"augmenter le second membre (c passe de 24 à 25) fait MONTER le maximum : P* + λ × 1": 56}'''),
        ("e", FRAC, "PSTAR_1.subs(c_, 25)",
         F + ''', mistakes={"e) demande la VRAIE valeur, au maximum pour c = 25, pas l'estimation de d)": 72}'''),
        ("f", "a number", "int(sympy.diff(PSTAR_1, c_).subs(c_, 24))",
         '''mistakes={"f) demande la DÉRIVÉE de P*(c) en c = 24, pas la valeur P*(24)": 64}'''),
        ("g", "a number", "12 * 2 * 2",
         '''mistakes={"le PRODUIT xyz au point (12, 2, 2), pas la valeur de x + 2y + 4z": 24}'''),
    ]),

    Paper("M13b.2", "La distance d'un point à un plan, retrouvée par Lagrange", [
        ("a", FRAC, "LAM_2",
         F + ''', mistakes={"le gradient de ‖x − x₀‖² est 2(x − x₀) : n'oublie pas le 2": R(1, 3), '''
         '''"avec ℒ = ‖x − x₀‖² + λ(n · x − 10), λ a le signe de n · x₀ − 10": R(-2, 3)}'''),
        ("b", f"a list of 3 fractions, {FRACS}", "floats(PROJ_2)",
         '''decimals=6, mistakes={"on revient VERS le plan : x = x₀ − (λ/2) n": floats(X0_2 + LAM_2 / 2 * N_2), '''
         '''"la stationnarité 2(x − x₀) + λn = 0 donne x = x₀ − (λ/2) n : n'oublie pas le 2": '''
         '''floats(X0_2 - LAM_2 * N_2)}'''),
        ("c", "a number", "int(((PROJ_2 - X0_2).T * (PROJ_2 - X0_2))[0])",
         '''mistakes={"c) demande le minimum de ‖x − x₀‖², le CARRÉ de la distance": 3}'''),
        ("d", "a number", "int(sq(((PROJ_2 - X0_2).T * (PROJ_2 - X0_2))[0]))",
         '''mistakes={"divise n · x₀ − 10 par ‖n‖, la norme de n": 27, "la distance est la RACINE du minimum de c)": 9}'''),
        ("e", "a number", "int((N_2.T * X0_2)[0])",
         '''mistakes={"e) demande n · x₀ seul, sans retrancher le second membre": 27}'''),
        ("f", "a number", "int(N_2.norm())", '''mistakes={"‖n‖ est la RACINE de 4² + 4² + 7²": 81}'''),
    ]),

    Paper("M13b.3", "Un problème quadratique sous deux contraintes linéaires : le système de Lagrange", [
        ("a", "an integer", "block_3(A_3).rows",
         '''mistakes={"une ligne par inconnue ET une par multiplicateur : n + m": {2, 3}}'''),
        ("b", f"a list of 3 fractions, {FRACS}", "floats(X_3)",
         '''decimals=6, mistakes={"x* respecte les DEUX contraintes, x₁ + x₂ + x₃ = 3 et x₁ − x₃ = 1": floats(X1_3), '''
         '''"le minimum libre −Q⁻¹c ne respecte pas les contraintes : résous le système par blocs": floats(FREE_3)}'''),
        ("c", f"a list of 2 fractions, {FRACS}", "floats(L_3)",
         '''decimals=6, mistakes={"avec ℒ = f + λᵀ(Ax − b), la stationnarité est Qx + c + Aᵀλ = 0 : attention au '''
         '''signe": floats(-L_3)}'''),
        ("d", FRAC, "obj_3(X_3)", F + f''', mistakes={{"f = ½ xᵀQx + cᵀx : n'oublie pas le ½": obj_3(X_3, 1)}}'''),
        ("e", "an integer", "int(block_3(A_3).det())"),
        ("f", "a list of 3 numbers", "[int(v) for v in X1_3]",
         '''mistakes={"f) ne garde que la PREMIÈRE contrainte, x₁ + x₂ + x₃ = 3": floats(X_3)}'''),
        ("g", "a number", "int(obj_3(X1_3))", '''mistakes={"f = ½ xᵀQx + cᵀx : n'oublie pas le ½": int(obj_3(X1_3, 1))}'''),
        ("h", FRAC, "obj_3(FREE_3)",
         F + ''', mistakes={"le minimum libre, en x = −Q⁻¹c, vaut −½ cᵀQ⁻¹c : un nombre négatif": -obj_3(FREE_3), '''
         '''"le minimum libre vaut −½ cᵀQ⁻¹c : n'oublie pas le ½": 2 * obj_3(FREE_3)}'''),
    ]),

    Paper("M13b.4", "Relire l'ACP par Lagrange : maximiser uᵀCu sous ‖u‖ = 1", [
        ("a", "an integer", "int(EIG_4[0])",
         '''mistakes={"le maximum de uᵀCu sous ‖u‖ = 1 est la PLUS GRANDE valeur propre": {1, 6}}'''),
        ("b", "a list of 3 numbers (4 decimals)", "floats(U1_4)",
         '''decimals=4, mistakes={"un axe est UNITAIRE : divise le vecteur propre par sa norme": [-1, 3, -2], '''
         '''"divise par la norme, puis applique la convention : la coordonnée de plus grande valeur absolue est '''
         '''positive": [1, -3, 2], '''
         '''"la convention de M12d : la coordonnée de plus grande valeur absolue est positive": floats(-U1_4)}'''),
        ("c", "a number", "int((U1_4.T * C_4 * U1_4)[0])",
         '''mistakes={"u₁ est unitaire : calcule uᵀCu avec le vecteur normalisé de b)": 182}'''),
        ("d", "a number", "0"),
        ("e", "an integer", "int(EIG_4[1])", '''mistakes={"la DEUXIÈME plus grande valeur propre": 1}'''),
        ("f", FRAC, "EIG_4[0] / C_4.trace()",
         F + ''', mistakes={"divise par la somme de TOUTES les valeurs propres, la trace de C": R(13, 19)}'''),
        ("g", FRAC, "(EIG_4[0] + EIG_4[1]) / C_4.trace()",
         F + ''', mistakes={"les DEUX plus grandes valeurs propres, divisées par la trace": R(7, 10)}'''),
        ("h", "a number", "int(C_4[0, 0])"),
    ]),

    Paper("M13b.5", "Une contrainte d'inégalité : active ou non, les conditions KKT à la main", [
        ("a", "True or False", "bool(2 * FREE_5[xs] + FREE_5[ys] <= 3)",
         '''mistakes={"calcule le minimum libre (∇f = 0), puis teste la contrainte 2x + y ≤ 3": True}'''),
        ("b", FRAC, "MU_5",
         F + ''', mistakes={"avec g = 2x + y − c ≤ 0 et ℒ = f + μg, la stationnarité est ∇f + μ∇g = 0 : au minimum, '''
         '''un multiplicateur d'inégalité est positif ou nul": -MU_5}'''),
        ("c", f"a list of 2 fractions, {FRACS}", "floats(P_5)",
         '''decimals=6, mistakes={"le minimum libre n'est pas admissible pour c = 3 : la contrainte est active": '''
         '''floats([FREE_5[xs], FREE_5[ys]])}'''),
        ("d", "a number", "int(F_5.subs(SOL_5))",
         '''mistakes={"pour c = 3, le minimum libre n'est pas admissible : calcule f au point de c)": '''
         '''int(F_5.subs(FREE_5))}'''),
        ("e", "a number", "int(F_5.subs(FREE_5))",
         '''mistakes={"pour c = 8, le minimum libre est admissible : la contrainte est inactive, et f* est la valeur '''
         '''de f au minimum libre": int(F_5.subs(SOL_5))}'''),
        ("f", FRAC, "-MU_5",
         F + ''', mistakes={"df*/dc = −μ : desserrer une contrainte active fait BAISSER le minimum": MU_5}'''),
        ("g", FRAC, "GE_5[mu]",
         F + ''', mistakes={"écris ℒ = f + μ(3 − 2x − y) : ∇g = (−2, −1), et la stationnarité ∇f + μ∇g = 0 donne '''
         '''le signe de μ": -GE_5[mu]}'''),
    ]),

    Paper("M13b.6", "La fonction duale d'un petit problème quadratique, et la dualité faible", [
        ("a", 'an expression in mu (between quotes, "mu**3" for μ³)', "str(D_6)",
         '''kind="expr", variables=("mu",), mistakes={"D(μ) est ℒ au point qui le minimise en (x, y), avec tous ses '''
         '''termes, −μx − μy compris": str(sympy.expand(D_6 + 3 * mu ** 2 / 4)), '''
         '''"le terme 6μ de ℒ ne dépend pas de (x, y) : il reste dans D(μ)": str(sympy.expand(D_6 - 6 * mu))}'''),
        ("b", "a number", "int(D_6.subs(mu, 4))"),
        ("c", "a number", "int(MU_6)"),
        ("d", "a number", "int(D_6.subs(mu, MU_6))"),
        ("e", "a list of 2 numbers", "[int(ARG_6[xs].subs(mu, MU_6)), int(ARG_6[ys].subs(mu, MU_6))]",
         '''mistakes={"x* d'abord, puis y*": [int(ARG_6[ys].subs(mu, MU_6)), int(ARG_6[xs].subs(mu, MU_6))]}'''),
        ("f", "a number", "int((xs ** 2 + 2 * ys ** 2).subs({xs: ARG_6[xs].subs(mu, MU_6), ys: ARG_6[ys].subs(mu, MU_6)}))"),
        ("g", "a number", "int(D_6.subs(mu, 12))",
         '''mistakes={"calcule D(12) avec la formule de a) : la dualité faible dit seulement D(μ) ≤ f*": '''
         '''int(D_6.subs(mu, MU_6))}'''),
    ]),

    Paper("M13b.7", "Reconnaître un problème convexe : fonctions, contraintes, ensembles", [
        ("a", "letters, as text", '"ADFH"', convexity_mistakes()),
    ]),

    Paper("M13b.8", "Une SVM à marge dure sur trois points, résolue par les conditions KKT", [
        ("a", "a list of 2 numbers", "floats(W_8)",
         '''decimals=6, mistakes={"w pointe vers la classe +1 : vérifie y₁(w · x₁ + b) = 1": floats(-W_8)}'''),
        ("b", "a number", "float(B_8)",
         '''decimals=6, mistakes={"vérifie y₃(w · x₃ + b) = 1, avec le label y₃ = −1": float(-B_8)}'''),
        ("c", "a list of 3 numbers", "floats(ALPHA_8)",
         '''decimals=6, mistakes={"les αᵢ d'une SVM sont positifs : w = Σ αᵢ yᵢ xᵢ porte déjà le label": '''
         '''floats([ALPHA_8[0], ALPHA_8[1], -ALPHA_8[2]])}'''),
        ("d", "a number", "float(HALF_8)", f'''decimals=6, mistakes={{"{HALF}": float(2 * HALF_8)}}'''),
        ("e", "a number (4 decimals)", "float(1 / sq(2 * HALF_8))",
         '''decimals=4, mistakes={"la marge est ρ = 1/‖w‖ ; la bande, deux fois plus large": float(2 / sq(2 * HALF_8)), '''
         '''"la marge est 1/‖w‖, pas ‖w‖": float(sq(2 * HALF_8)), '''
         '''"ρ = 1/‖w‖, avec la racine : ‖w‖ = √(w₁² + w₂²)": float(1 / (2 * HALF_8))}'''),
        ("f", "a number", "float((W_8.T * sympy.Matrix([0, 8]))[0] + B_8)",
         f'''decimals=6, mistakes={{"{BIAS}": float((W_8.T * sympy.Matrix([0, 8]))[0])}}'''),
        ("g", "an integer", "sum(1 for a in ALPHA_8 if a > 0)",
         '''mistakes={"g) compte les vecteurs de support de la SVM des trois exemples : le quatrième de f) n'en fait '''
         '''pas partie": 4}'''),
        ("h", "a number", "float(sum(ALPHA_8) - HALF_8)",
         '''decimals=6, mistakes={"le dual retranche ½‖w‖² à Σ αᵢ": float(sum(ALPHA_8))}'''),
    ]),

    Paper("M13b.9", "La hinge loss et l'objectif régularisé de quelques points", [
        ("a", "a list of 6 numbers", "floats(T_9)",
         f'''decimals=6, mistakes={{"{BIAS}": floats(yy * (s - B_9) for s, (_, yy) in zip(S_9, PTS_9)), '''
         '''"la marge fonctionnelle multiplie le score par le label y": floats(S_9)}'''),
        ("b", "a list of 6 numbers", "floats(H_9)",
         '''decimals=6, mistakes={"max(0, 1 − t) n'est jamais négatif": floats(1 - t for t in T_9)}'''),
        ("c", "a number (4 decimals)", "float(sum(H_9) / 6)",
         '''decimals=4, mistakes={"la hinge MOYENNE : divise la somme par 6": float(sum(H_9))}'''),
        ("d", "a number", "float(HALF_9)", f'''decimals=6, mistakes={{"{HALF}": float(2 * HALF_9)}}'''),
        ("e", "a number", "float(HALF_9 + C_9 * sum(H_9))",
         f'''decimals=6, mistakes={{"{SUM}": float(HALF_9 + C_9 * sum(H_9) / 6), '''
         '''"J = ½‖w‖² + C Σ max(0, 1 − tᵢ) : n'oublie pas C": float(HALF_9 + sum(H_9)), '''
         f'''"{HALF}": float(2 * HALF_9 + C_9 * sum(H_9)), "{SUM} (et garde toutes les décimales)": 1.7583, '''
         '''"J commence par ½‖w‖² : n'oublie pas ce terme": float(C_9 * sum(H_9))}'''),
        ("f", FRAC, "R(1, 6 * C_9)",
         F + ''', mistakes={"λ = 1/(nC) : divise aussi par C": R(1, 6), "λ = 1/(nC) : divise aussi par n": R(1, 2), '''
         '''"λ = 1/(nC), pas nC": 12}'''),
        ("g", "an integer", "sum(1 for t in T_9 if t < 1)",
         '''mistakes={"« strictement » sous 1 : une marge égale à 1 ne compte pas": 3}'''),
        ("h", "an integer", "sum(1 for t in T_9 if t < 0)",
         '''mistakes={"mal classé veut dire t < 0 ; un exemple de marge 0 < t < 1 est bien classé": 2}'''),
    ]),

    Paper("M13b.10", "Un pas de sous-gradient sur l'objectif d'une SVM linéaire", [
        ("a", "a list of 4 numbers", "floats(margins_10(W_10, B_10))",
         f'''decimals=6, mistakes={{"{BIAS}": floats(margins_10(W_10, 0))}}'''),
        ("b", "a number (4 decimals)", "float(j_10(W_10, B_10))",
         f'''decimals=4, mistakes={{"{SUM}": float(j_10(W_10, B_10, C_10 / 4)), '''
         '''"J = ½‖w‖² + C Σ max(0, 1 − tᵢ) : n'oublie pas C": float(j_10(W_10, B_10, 1))}'''),
        ("c", "a list of 2 numbers", "floats(GW_10)",
         f'''decimals=6, mistakes={{"{STRICT}": floats(GW2_10), '''
         '''"g_w commence par w, le gradient de ½‖w‖²": floats(GW_10 - W_10)}'''),
        ("d", "a number", "float(GB_10)", f'''decimals=6, mistakes={{"{STRICT}": float(GB2_10)}}'''),
        ("e", "a list of 2 numbers", "floats(WNEW_10)",
         '''decimals=6, mistakes={"on descend : w − η g_w, pas w + η g_w": floats(W_10 + ETA_10 * GW_10)}'''),
        ("f", "a number (4 decimals)", "float(j_10(WNEW_10, BNEW_10))",
         '''decimals=4, mistakes={"on descend : (w, b) − η (g_w, g_b)": float(j_10(W_10 + ETA_10 * GW_10, '''
         '''B_10 + ETA_10 * GB_10))}'''),
        ("g", "a list of 2 numbers", "floats(GW2_10)",
         '''decimals=6, mistakes={"g) compte AUSSI l'exemple de marge exactement 1": floats(GW_10)}'''),
    ]),

    Paper("M13b.11", "Le dual d'une SVM : lire les vecteurs de support et retrouver w", [
        ("a", "a number", "float(sum(a * yy for _, yy, a in PTS_11))",
         '''decimals=6, mistakes={"Σ αᵢ yᵢ, avec les labels": float(sum(a for _, _, a in PTS_11))}'''),
        ("b", "a list of 2 numbers", "floats(W_11)",
         '''decimals=6, mistakes={"w = Σ αᵢ yᵢ xᵢ : le label yᵢ compte": '''
         '''floats(sum((a * sympy.Matrix(p) for p, _, a in PTS_11), sympy.zeros(2, 1)))}'''),
        ("c", "a number", "float(B_11)",
         '''decimals=6, mistakes={"b se lit sur un vecteur de support LIBRE (0 < αᵢ < C), le seul exactement sur un '''
         '''bord": {float(1 - (W_11.T * sympy.Matrix([3, 7]))[0]), float(-1 - (W_11.T * sympy.Matrix([5, 8]))[0])}}'''),
        ("d", "a list of integers", "[i + 1 for i, (_, _, a) in enumerate(PTS_11) if a > 0]",
         '''mistakes={"les vecteurs de support sont TOUS les exemples où αᵢ > 0, les bornés (αᵢ = C) compris": [1, 6], '''
         '''"les vecteurs de support sont tous les exemples où αᵢ > 0, les libres (0 < αᵢ < C) compris": [2, 4], '''
         '''"numérote les exemples à partir de 1, comme le tableau (pas à partir de 0)": [0, 1, 3, 5]}'''),
        ("e", "a list of 6 numbers", "floats(T_11)",
         '''decimals=6, mistakes={"la marge fonctionnelle multiplie le score par le label y": floats(S_11)}'''),
        ("f", "a number", "float(HALF_11 + HINGE_11)",
         f'''decimals=6, mistakes={{"{SUM}": float(HALF_11 + HINGE_11 / 6), "{HALF}": float(2 * HALF_11 + HINGE_11)}}'''),
        ("g", "a number", "float(sum(a for _, _, a in PTS_11) - HALF_11)",
         '''decimals=6, mistakes={"le dual retranche ½‖w‖² à Σ αᵢ": float(sum(a for _, _, a in PTS_11)), '''
         '''"le dual retranche ½‖w‖², avec le ½": float(sum(a for _, _, a in PTS_11) - 2 * HALF_11)}'''),
    ]),

    Paper("M13b.12", "Le noyau (1 + x · z)² en dimension 2 : sa fonction φ à six coordonnées", [
        ("a", "a list of 6 numbers (2 decimals)", "floats(phi_12(X_12))",
         '''decimals=2, mistakes={"les √2 de φ ne sont pas décoratifs : ils font sortir les doubles produits": '''
         '''floats(phi_12(X_12, root=1, cross=1))}'''),
        ("b", "a list of 6 numbers (2 decimals)", "floats(phi_12(Z_12))",
         '''decimals=2, mistakes={"les √2 de φ ne sont pas décoratifs : ils font sortir les doubles produits": '''
         '''floats(phi_12(Z_12, root=1, cross=1))}'''),
        ("c", "an integer", "int(k_12(X_12, Z_12))",
         '''mistakes={"k = (1 + x · z)² : n'oublie pas le 1": int((X_12.T * Z_12)[0] ** 2)}'''),
        ("d", "a list of 6 numbers (2 decimals)", "floats(phi_12(X_12, const=3))",
         '''decimals=2, mistakes={"pour (c + x · z)², les termes de degré 1 ont le coefficient √(2c), ici √6": '''
         '''floats(phi_12(X_12, const=3, root=sq(2))), '''
         '''"la première coordonnée de φ est c = 3 : c × c donne le terme constant c² du développement": '''
         '''floats(phi_12(X_12, const=3, first=1))}'''),
        ("e", "an integer", "math.comb(9 + 2, 2)",
         '''mistakes={"la constante 1 du développement est aussi une coordonnée de φ": math.comb(11, 2) - 1, '''
         '''"(1 + x · z)² contient les monômes de degré 0, 1 ET 2": math.comb(10, 2), '''
         '''"xᵢxⱼ et xⱼxᵢ sont le même monôme : compte chaque paire une fois": 1 + 9 + 9 ** 2}'''),
        ("f", "an integer", "math.comb(9 + 3, 3)",
         '''mistakes={"la constante 1 du développement est aussi une coordonnée de φ": math.comb(12, 3) - 1, '''
         '''"(1 + x · z)³ contient les monômes de degré 0 à 3, pas seulement ceux de degré 3": math.comb(11, 3), '''
         '''"un monôme ne dépend pas de l'ordre de ses facteurs : compte chacun une fois": 1 + 9 + 9 ** 2 + 9 ** 3}'''),
    ]),

    Paper("M13b.13", "La matrice de Gram d'un noyau RBF sur trois points, et l'effet de γ", [
        ("a", "a list of 3 numbers", "[int(D2_13[0][1]), int(D2_13[0][2]), int(D2_13[1][2])]",
         '''mistakes={"les CARRÉS des distances, sans racine": floats(sq(d) for d in (D2_13[0][1], D2_13[0][2], '''
         '''D2_13[1][2]))}'''),
        ("b", "a number (4 decimals)", "float(K_13[0, 1])",
         f'''decimals=4, mistakes={{"{SQUARED}": float(gram_13(R(1, 5), squared=False)[0, 1]), '''
         '''"e^(−γ d²) : γ MULTIPLIE le carré de la distance": float(sympy.exp(-D2_13[0][1] / R(1, 5))), '''
         '''"e^(−γ d²), avec le signe moins": float(1 / K_13[0, 1])}'''),
        ("c", "a 3 x 3 matrix, as a list of rows (4 decimals)", "[floats(K_13.row(i)) for i in range(3)]",
         f'''decimals=4, mistakes={{"{SQUARED}": [floats(gram_13(R(1, 5), squared=False).row(i)) for i in range(3)]}}'''),
        ("d", "a number (4 decimals)", "float(K_13.det())",
         f'''decimals=4, mistakes={{"{SQUARED}": float(gram_13(R(1, 5), squared=False).det())}}'''),
        ("e", "a number (4 decimals)", "float(sq(2 - 2 * K_13[0, 1]))",
         '''decimals=4, mistakes={"la distance est la RACINE de k(x₁, x₁) − 2k(x₁, x₂) + k(x₂, x₂)": '''
         '''float(2 - 2 * K_13[0, 1]), "la distance dans l'espace des features, pas dans le plan": 3.0}'''),
        ("f", "a number", "int(-2 * D2_13[0][1])", f'''mistakes={{"{SQUARED}": int(-2 * sq(D2_13[0][1]))}}'''),
        ("g", "an integer", "1",
         '''mistakes={"quand γ → 0, chaque valeur du noyau tend vers e⁰ : compare les lignes de la matrice limite": 3, '''
         '''"quand γ → 0, la matrice tend vers la matrice pleine de 1, pas vers la matrice nulle": 0}'''),
        ("h", "an integer", "3",
         '''mistakes={"quand γ → +∞, la diagonale reste k(xᵢ, xᵢ) = 1 : la matrice limite n'est pas nulle": 0}'''),
    ]),

    Paper("M13b.20", "Pont : la décision d'une SVM à noyau, une somme pondérée sur les vecteurs de support", [
        ("a", "a number", "float(sum(a * yy for _, yy, a in SV_20))",
         '''decimals=6, mistakes={"Σ αᵢ yᵢ, avec les labels": float(sum(a for _, _, a in SV_20))}'''),
        ("b", "a number (4 decimals)", "float(s_20((R(1, 2), R(1, 2))))",
         '''decimals=4, mistakes={"s(x) = Σ αᵢ yᵢ k(xᵢ, x) + b : n'oublie pas le biais": '''
         '''float(s_20((R(1, 2), R(1, 2)), bias=0)), '''
         f'''"{SQUARED}": float(s_20((R(1, 2), R(1, 2)), squared=False)), '''
         '''"chaque terme est multiplié par le label yᵢ": float(s_20((R(1, 2), R(1, 2)), labels=False))}'''),
        ("c", "an integer (-1 or 1)", "1 if s_20((R(1, 2), R(1, 2))) > 0 else -1",
         '''mistakes={"la classe prédite est −1 ou +1 : le signe de s": 0}'''),
        ("d", "a number (4 decimals)", "float(s_20((2, 4)))",
         '''decimals=4, mistakes={"s(x) = Σ αᵢ yᵢ k(xᵢ, x) + b : n'oublie pas le biais": float(s_20((2, 4), bias=0)), '''
         f'''"{SQUARED}": float(s_20((2, 4), squared=False))}}'''),
        ("e", "a number", "float(B_20)",
         '''decimals=6, mistakes={"loin de tous les vecteurs de support, chaque k(xᵢ, x) tend vers 0, mais le biais '''
         '''reste": 0.0}'''),
        ("f", "an integer", "len(SV_20)"),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly (SymPy) from the statements
import math

import sympy

R, sq = sympy.Rational, sympy.sqrt
mu = sympy.symbols("mu")
xs, ys = sympy.symbols("xs ys", real=True)


def floats(values):
    """SymPy numbers as a list of Python floats."""
    return [float(v) for v in values]


x_, y_, z_, l_, c_ = sympy.symbols("x y z l c", positive=True)                              # M13b.1
SOL_1 = sympy.solve([y_ * z_ - l_, x_ * z_ - 2 * l_, x_ * y_ - 4 * l_, x_ + 2 * y_ + 4 * z_ - c_],
                    [x_, y_, z_, l_], dict=True)[0]      # the stationarity of xyz − λ(x + 2y + 4z − c), and the constraint
PSTAR_1 = sympy.simplify((x_ * y_ * z_).subs(SOL_1))     # P*(c)
POINT_1 = [int(SOL_1[v].subs(c_, 24)) for v in (x_, y_, z_)]
LAM_1 = SOL_1[l_].subs(c_, 24)
N_2, X0_2 = sympy.Matrix([4, -4, 7]), sympy.Matrix([5, 1, 3])                              # M13b.2
P_2 = sympy.Matrix(sympy.symbols("p1:4"))
SOL_2 = sympy.solve(list(2 * (P_2 - X0_2) + mu * N_2) + [(N_2.T * P_2)[0] - 10], list(P_2) + [mu], dict=True)[0]
LAM_2, PROJ_2 = SOL_2[mu], P_2.subs(SOL_2)
Q_3 = sympy.Matrix([[4, 1, 0], [1, 2, 0], [0, 0, 2]])                                       # M13b.3
C_3, A_3, B_3 = sympy.Matrix([-2, 0, 1]), sympy.Matrix([[1, 1, 1], [1, 0, -1]]), sympy.Matrix([3, 1])


def block_3(A):
    """The block matrix [[Q, Aᵀ], [A, 0]] of the constraints A x = b."""
    return sympy.BlockMatrix([[Q_3, A.T], [A, sympy.zeros(A.rows, A.rows)]]).as_explicit()


def solve_3(A, b):
    """(x, λ) of min ½ xᵀQx + cᵀx under A x = b."""
    s = block_3(A).LUsolve(sympy.Matrix.vstack(-C_3, b))
    return s[:3, 0], s[3:, 0]


def obj_3(x, half=R(1, 2)):
    """half · xᵀQx + cᵀx (half = 1/2 for f)."""
    return half * (x.T * Q_3 * x)[0] + (C_3.T * x)[0]


X_3, L_3 = solve_3(A_3, B_3)
X1_3 = solve_3(A_3[0:1, :], B_3[0:1, :])[0]
FREE_3 = -Q_3.inv() * C_3
C_4 = sympy.Matrix([[2, -3, 1], [-3, 10, -3], [1, -3, 8]])                                  # M13b.4
EIG_4 = sorted(C_4.eigenvals(), reverse=True)
V_4 = (C_4 - EIG_4[0] * sympy.eye(3)).nullspace()[0]
U1_4 = V_4 / V_4.norm()
U1_4 = U1_4 * sympy.sign(U1_4[max(range(3), key=lambda i: abs(U1_4[i]))])   # largest coordinate in absolute value > 0
F_5 = xs ** 2 + 2 * ys ** 2 - 4 * xs - 8 * ys                                               # M13b.5
FREE_5 = sympy.solve([sympy.diff(F_5, xs), sympy.diff(F_5, ys)], [xs, ys], dict=True)[0]
SOL_5 = sympy.solve([sympy.diff(F_5, xs) + 2 * mu, sympy.diff(F_5, ys) + mu, 2 * xs + ys - 3], [xs, ys, mu], dict=True)[0]
MU_5, P_5 = SOL_5[mu], [SOL_5[xs], SOL_5[ys]]
GE_5 = sympy.solve([sympy.diff(F_5, xs) - 2 * mu, sympy.diff(F_5, ys) - mu, 3 - 2 * xs - ys], [xs, ys, mu], dict=True)[0]
L_6 = xs ** 2 + 2 * ys ** 2 + mu * (6 - xs - ys)                                             # M13b.6
ARG_6 = sympy.solve([sympy.diff(L_6, xs), sympy.diff(L_6, ys)], [xs, ys], dict=True)[0]
D_6 = sympy.expand(L_6.subs(ARG_6))
MU_6 = sympy.solve(sympy.diff(D_6, mu), mu)[0]
a1, a2, a3, w1, w2, bb = sympy.symbols("a1 a2 a3 w1 w2 bb")                                 # M13b.8
PTS_8 = [((3, 5), 1), ((7, 7), 1), ((7, 2), -1)]
WS_8 = sympy.Matrix([w1, w2])
SOL_8 = sympy.solve(list(WS_8 - sum((a * yy * sympy.Matrix(p) for a, (p, yy) in zip((a1, a2, a3), PTS_8)),
                                    sympy.zeros(2, 1)))
                    + [a1 + a2 - a3] + [yy * ((WS_8.T * sympy.Matrix(p))[0] + bb) - 1 for p, yy in PTS_8],
                    [a1, a2, a3, w1, w2, bb], dict=True)[0]
W_8, B_8 = sympy.Matrix([SOL_8[w1], SOL_8[w2]]), SOL_8[bb]
ALPHA_8 = [SOL_8[a1], SOL_8[a2], SOL_8[a3]]
HALF_8 = (W_8.T * W_8)[0] / 2
W_9, B_9, C_9 = sympy.Matrix([1, R(-1, 2)]), R(1, 2), 2                                     # M13b.9
PTS_9 = [((3, 0), 1), ((1, 0), 1), ((0, R(3, 5)), 1), ((-1, 1), -1), ((2, R(9, 5)), -1), ((-2, R(2, 5)), -1)]
S_9 = [(W_9.T * sympy.Matrix(p))[0] + B_9 for p, _ in PTS_9]
T_9 = [yy * s for s, (_, yy) in zip(S_9, PTS_9)]
H_9 = [sympy.Max(0, 1 - t) for t in T_9]
HALF_9 = (W_9.T * W_9)[0] / 2
W_10, B_10, C_10, ETA_10 = sympy.Matrix([R(1, 2), 1]), -1, R(1, 2), R(1, 5)                 # M13b.10
PTS_10 = [((3, R(1, 2)), 1), ((0, 3), -1), ((1, -1), -1), ((-1, 2), 1)]


def margins_10(w, b):
    """The functional margins y (w · x + b) of the four examples."""
    return [yy * ((w.T * sympy.Matrix(p))[0] + b) for p, yy in PTS_10]


def j_10(w, b, C=C_10):
    """½‖w‖² + C Σ max(0, 1 − t)."""
    return (w.T * w)[0] / 2 + C * sum(sympy.Max(0, 1 - t) for t in margins_10(w, b))


def sub_10(w, b, kink=False):
    """(g_w, g_b), counting the margins < 1 (≤ 1 with kink)."""
    chosen = [(p, yy) for (p, yy), t in zip(PTS_10, margins_10(w, b)) if (t <= 1 if kink else t < 1)]
    g_w = w - C_10 * sum((yy * sympy.Matrix(p) for p, yy in chosen), sympy.zeros(2, 1))
    return g_w, -C_10 * sum(yy for _, yy in chosen)


GW_10, GB_10 = sub_10(W_10, B_10)
GW2_10, GB2_10 = sub_10(W_10, B_10, kink=True)
WNEW_10, BNEW_10 = W_10 - ETA_10 * GW_10, B_10 - ETA_10 * GB_10
PTS_11 = [((5, 6), 1, R(9, 10)), ((3, 7), 1, 1), ((7, 4), 1, 0), ((5, 8), -1, 1), ((1, 5), -1, 0),     # M13b.11
          ((2, 5), -1, R(9, 10))]
W_11 = sum((a * yy * sympy.Matrix(p) for p, yy, a in PTS_11), sympy.zeros(2, 1))
B_11 = 1 - (W_11.T * sympy.Matrix([5, 6]))[0]            # read on the free support vector x₁, of label +1
S_11 = [(W_11.T * sympy.Matrix(p))[0] + B_11 for p, _, _ in PTS_11]
T_11 = [yy * s for s, (_, yy, _) in zip(S_11, PTS_11)]
HALF_11 = (W_11.T * W_11)[0] / 2
HINGE_11 = sum(sympy.Max(0, 1 - t) for t in T_11)
X_12, Z_12 = sympy.Matrix([4, -3]), sympy.Matrix([3, -5])                                   # M13b.12


def phi_12(v, const=1, root=None, first=None, cross=sq(2)):
    """φ(v) of (const + x · z)²: (const, √(2 const) v₁, √(2 const) v₂, v₁², √2 v₁v₂, v₂²); the variants replace the
    coefficient of the degree-1 terms by root, the first coordinate by first, and the √2 of x₁x₂ by cross."""
    root = sq(2 * const) if root is None else root
    first = const if first is None else first
    return sympy.Matrix([first, root * v[0], root * v[1], v[0] ** 2, cross * v[0] * v[1], v[1] ** 2])


def k_12(u, v, const=1):
    """(const + u · v)²."""
    return (const + (u.T * v)[0]) ** 2


assert sympy.simplify((phi_12(X_12).T * phi_12(Z_12))[0] - k_12(X_12, Z_12)) == 0
assert sympy.simplify((phi_12(X_12, 3).T * phi_12(Z_12, 3))[0] - k_12(X_12, Z_12, 3)) == 0


PTS_13 = [sympy.Matrix([0, 0]), sympy.Matrix([3, 0]), sympy.Matrix([0, -2])]                # M13b.13
D2_13 = [[((u - v).T * (u - v))[0] for v in PTS_13] for u in PTS_13]


def gram_13(gamma, squared=True):
    """The RBF Gram matrix e^(−γ d²) of the three points (e^(−γ d) when not squared)."""
    return sympy.Matrix(3, 3, lambda i, j: sympy.exp(-gamma * (D2_13[i][j] if squared else sq(D2_13[i][j]))))


K_13 = gram_13(R(1, 5))
SV_20 = [((-1, 1), 1, R(4, 5)), ((2, -1), -1, R(1, 2)), ((1, 3), -1, R(3, 10))]               # M13b.20
G_20, B_20 = R(3, 10), R(-1, 10)


def s_20(p, bias=B_20, labels=True, squared=True):
    """The decision Σ αᵢ yᵢ e^(−γ‖xᵢ − p‖²) + b (variants: without labels, without the square)."""
    total = bias
    for q, yy, a in SV_20:
        d2 = ((sympy.Matrix(q) - sympy.Matrix(p)).T * (sympy.Matrix(q) - sympy.Matrix(p)))[0]
        total += a * (yy if labels else 1) * sympy.exp(-G_20 * (d2 if squared else sq(d2)))
    return total'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M13b.1 à M13b.13, 🔗 M13b.20)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"5/9\"` ;\n"
               "- une liste `[0.15, -2]` ; dans une liste, une fraction s'écrit comme un calcul, sans guillemets : "
               "`[2/9, 7/9]` ; une matrice, comme une liste de lignes : `[[1, 0.5], [0.5, 1]]` ;\n"
               "- une expression entre guillemets, écrite comme en Python : `\"mu**2 - 7*mu\"` pour $\\mu^2 - 7\\mu$ ;\n"
               "- des lettres collées entre guillemets, `\"BD\"`, ou `True` / `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M13b.25 to M13b.27) and the libraries (M13b.28)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import inspect
import io
import math
import re
import time
import tokenize
import warnings

import matplotlib.pyplot as plt
import numpy as np

from wbm.nbtools import checked, drawn, fr, run_pytest_group, verdict


def raised(function, *args, **kwargs):
    """The name of the exception that function(*args, **kwargs) raises, or "aucune" if it returns.

    NotImplementedError (a TODO not done yet) goes through, for wbm.attempt to show ⏳; so do the errors of a code
    that cannot run (a missing import, a misspelt name such as ValueErorr), for the check to name them."""
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            function(*args, **kwargs)
    except (NotImplementedError, NameError, AttributeError, ImportError):
        raise
    except Exception as exc:  # noqa: BLE001 - any other error is the answer
        return type(exc).__name__
    return "aucune"'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M13b")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/svm.py`, lis la docstring "
         "du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton code, "
         "**enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. NumPy "
         "est permis (`@`, `.T`, `np.linalg.norm` et `np.linalg.solve` compris) ; `scipy.optimize`, `scipy.spatial`, "
         "`scipy.linalg` et scikit-learn sont interdits (les tests comparent tes résultats aux leurs, et un test "
         "vérifie que tu ne t'en sers pas). Ne modifie jamais les tableaux reçus : travaille sur une copie, "
         "`np.array(X, dtype=float)`. Les nombres se rendent en `float` de Python, les vecteurs et les matrices en "
         "tableaux NumPy de flottants ; les labels d'une SVM valent −1 ou +1, un exemple par ligne.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError", "FloatingPointError",
                "LinAlgError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def value_error(message: str) -> str:
    return (f'''mistakes={{"{message}": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}}''')


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of svm.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_svm_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m13b_svm.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m13b_svm.py", "{keyword}", impl="ref")')]


GIVEN_25 = '''Q_25 = np.array([[6.0, 1.0, 0.0, -1.0],
                 [1.0, 4.0, 1.0, 0.0],
                 [0.0, 1.0, 5.0, 2.0],
                 [-1.0, 0.0, 2.0, 3.0]])         # symmetric positive definite
C_25 = np.array([-2.0, 3.0, -1.0, 4.0])
A_25 = np.array([[1.0, -2.0, 1.0, 3.0],
                 [2.0, 0.0, -1.0, 1.0]])         # two independent constraints A x = b
B_25 = np.array([5.0, -3.0])
TWICE_25 = [[1.0, -2.0, 1.0, 3.0], [1.0, -2.0, 1.0, 3.0]]   # the same constraint written twice'''

QP_25 = "mymath.svm.lagrange_equality_qp(Q_25, C_25, A_25, B_25)"

M13B_25 = Ex(
    "M13b.25", "🔨", 1, 20, "Un problème quadratique sous contraintes d'égalité, par le système de Lagrange · "
    "`lagrange_equality_qp`",
    "programmer la résolution d'un problème quadratique sous contraintes d'égalité par un seul système linéaire par "
    "blocs, et vérifier que sa solution est bien le minimum.", "fiche §2", tracks="C, E", mymath="svm.py",
    given=GIVEN_25,
    body=HOWTO + r"""

Écris `lagrange_equality_qp(Q, c, A, b)` (fiche §2), en suivant sa docstring : les contrôles de forme d'abord (`ValueError` si `Q` n'est pas $n \times n$ pour un `c` de longueur $n$, si `A` n'a pas $n$ colonnes et une ligne par second membre de `b`) ; puis la matrice par blocs $\begin{pmatrix} \mathbf{Q} & \mathbf{A}^\top \\ \mathbf{A} & \mathbf{0} \end{pmatrix}$ (`np.block`), le second membre $(-\mathbf{c}, \mathbf{b})$ (`np.concatenate`), `np.linalg.solve`, et le découpage de la solution en $(\mathbf{x}, \boldsymbol{\lambda})$. Si le système est singulier, `np.linalg.solve` lève une `numpy.linalg.LinAlgError` : attrape-la et lève une `ValueError` à la place.

La vérification calcule, avec le problème de la cellule fournie (4 variables, 2 contraintes) :
- a) le point $\mathbf{x}$ rendu par `lagrange_equality_qp(Q_25, C_25, A_25, B_25)` (une liste, 6 décimales) ;
- b) les multiplicateurs $\boldsymbol{\lambda}$ (une liste, 6 décimales) ;
- c) vrai ou faux : $\mathbf{Q}\mathbf{x} + \mathbf{c} + \mathbf{A}^\top\boldsymbol{\lambda} = \mathbf{0}$, chaque coordonnée à $10^{-10}$ près ;
- d) vrai ou faux : $\mathbf{x}$ est admissible ($\mathbf{A}\mathbf{x} = \mathbf{b}$ à $10^{-10}$ près) et aucun des 1 000 points admissibles tirés au hasard (graine 4225) n'a une valeur de $f$ plus petite ;
- e) le nom de l'erreur levée quand la même contrainte est écrite deux fois, `lagrange_equality_qp(Q_25, C_25, TWICE_25, [5, 5])`.

Dans ta copie : écris le système par blocs de ce problème (sa taille ?). Que vaut $f(\mathbf{x})$, et pourquoi d) suffit-il à te convaincre que c'est un minimum, alors que la condition de Lagrange n'est que nécessaire (fiche §5) ? Pourquoi deux contraintes identiques rendent-elles la matrice par blocs singulière (regarde ses deux dernières lignes) ? Que dit le signe de chaque multiplicateur quand on augmente d'une unité le second membre de sa contrainte ?""",
    todo=LOAD_LEARNER,
    check=f'''with checked("M13b.25a"):
    wbm.check("M13b.25a", np.asarray({QP_25}[0]).tolist(), computed=True)
with checked("M13b.25b"):
    wbm.check("M13b.25b", np.asarray({QP_25}[1]).tolist(), computed=True)
with checked("M13b.25c"):
    x_25, lam_25 = {QP_25}
    wbm.check("M13b.25c", bool(np.max(np.abs(Q_25 @ x_25 + C_25 + A_25.T @ lam_25)) <= 1e-10), computed=True)
with checked("M13b.25d"):
    x_25 = np.asarray({QP_25}[0], dtype=float)
    base_25 = A_25.T @ np.linalg.solve(A_25 @ A_25.T, B_25)                    # one feasible point
    along_25 = np.eye(4) - A_25.T @ np.linalg.solve(A_25 @ A_25.T, A_25)      # the projection on A v = 0
    tries_25 = base_25 + np.random.default_rng(4225).normal(0.0, 1.0, size=(1000, 4)) @ along_25
    f_tries_25 = 0.5 * np.sum((tries_25 @ Q_25) * tries_25, axis=1) + tries_25 @ C_25
    wbm.check("M13b.25d", bool(np.max(np.abs(A_25 @ x_25 - B_25)) <= 1e-10
                               and np.all(f_tries_25 >= 0.5 * x_25 @ Q_25 @ x_25 + C_25 @ x_25 - 1e-12)), computed=True)
with checked("M13b.25e"):
    wbm.check("M13b.25e", raised(mymath.svm.lagrange_equality_qp, Q_25, C_25, TWICE_25, [5, 5]), computed=True)''',
    solution=LOAD_REF + f'''
lagrange_equality_qp = mymath.svm.lagrange_equality_qp
x_25, lam_25 = lagrange_equality_qp(Q_25, C_25, A_25, B_25)
print("a)", np.round(x_25, 6).tolist(), " b)", np.round(lam_25, 6).tolist())
print("c) résidu de la stationnarité :", float(np.max(np.abs(Q_25 @ x_25 + C_25 + A_25.T @ lam_25))),
      " ; A x − b :", float(np.max(np.abs(A_25 @ x_25 - B_25))))
base_25 = A_25.T @ np.linalg.solve(A_25 @ A_25.T, B_25)
along_25 = np.eye(4) - A_25.T @ np.linalg.solve(A_25 @ A_25.T, A_25)
tries_25 = base_25 + np.random.default_rng(4225).normal(0.0, 1.0, size=(1000, 4)) @ along_25
f_tries_25 = 0.5 * np.sum((tries_25 @ Q_25) * tries_25, axis=1) + tries_25 @ C_25
f_25 = 0.5 * x_25 @ Q_25 @ x_25 + C_25 @ x_25
print("d) f(x) =", round(float(f_25), 6), " ; le meilleur des 1 000 points :", round(float(f_tries_25.min()), 6),
      " ; e)", raised(lagrange_equality_qp, Q_25, C_25, TWICE_25, [5, 5]))
print("taille du système par blocs :", np.block([[Q_25, A_25.T], [A_25, np.zeros((2, 2))]]).shape)''',
    record='''from scipy.linalg import null_space

q_25r = np.array([[6.0, 1.0, 0.0, -1.0], [1.0, 4.0, 1.0, 0.0], [0.0, 1.0, 5.0, 2.0], [-1.0, 0.0, 2.0, 3.0]])
c_25r, a_25r, b_25r = np.array([-2.0, 3.0, -1.0, 4.0]), np.array([[1.0, -2.0, 1.0, 3.0], [2.0, 0.0, -1.0, 1.0]]), \\
    np.array([5.0, -3.0])
start_25r = np.linalg.lstsq(a_25r, b_25r, rcond=None)[0]      # the minimum by elimination: x = x0 + N z
basis_25r = null_space(a_25r)
x_25r = start_25r + basis_25r @ np.linalg.solve(basis_25r.T @ q_25r @ basis_25r,
                                                -basis_25r.T @ (q_25r @ start_25r + c_25r))
lam_25r = np.linalg.lstsq(a_25r.T, -(q_25r @ x_25r + c_25r), rcond=None)[0]
wrong_25r = np.linalg.solve(np.block([[q_25r, a_25r.T], [a_25r, np.zeros((2, 2))]]), np.concatenate([c_25r, b_25r]))
RHS_25 = "le second membre du système est (−c, b) : Qx + c + Aᵀλ = 0 s'écrit Qx + Aᵀλ = −c"
wbm.record("M13b.25a", x_25r.tolist(), decimals=6, mistakes={RHS_25: wrong_25r[:4].tolist()})
wbm.record("M13b.25b", lam_25r.tolist(), decimals=6,
           mistakes={"avec le lagrangien ½xᵀQx + cᵀx + λᵀ(Ax − b), le bloc en haut à droite est +Aᵀ : attention au "
                     "signe de λ": (-lam_25r).tolist(), RHS_25: wrong_25r[4:].tolist()})
wbm.record("M13b.25c", True,
           mistakes={"relis lagrange_equality_qp : ses tests disent ce qui ne va pas": False})
wbm.record("M13b.25d", True,
           mistakes={"ton x doit respecter A x = b et faire au moins aussi bien que tout point admissible : relis "
                     "lagrange_equality_qp (ses tests disent ce qui ne va pas)": False})
wbm.record("M13b.25e", "ValueError",
           ''' + value_error("deux contraintes identiques rendent le système singulier : attrape la LinAlgError de "
                             "np.linalg.solve et lève une ValueError") + ''')''',
    after=tests_cells("test_lagrange"),
    note=r"$\mathbf{x} \approx (0{,}129353 ;\ -2{,}756219 ;\ 2{,}283582 ;\ -0{,}975124)$, $\boldsymbol{\lambda} \approx "
         r"(-2{,}805970 ;\ 2{,}905473)$ et $f(\mathbf{x}) \approx 4{,}0174$ : un système $6 \times 6$ (4 inconnues, 2 "
         r"multiplicateurs). Le problème est convexe ($\mathbf{Q}$ définie positive, contraintes affines) : le point "
         r"de Lagrange est le minimum, et les 1 000 points admissibles tirés au hasard le confirment (le meilleur fait "
         r"$\approx 4{,}1101$). Avec la même contrainte écrite deux fois, les deux dernières lignes de la matrice par "
         r"blocs sont égales : elle est singulière, et les multiplicateurs ne sont plus uniques (seule leur somme est "
         r"fixée). Augmenter d'une unité le second membre de la contrainte $j$ change le minimum d'environ $-\lambda_j$ : $+2{,}8$ pour la "
         r"première, $-2{,}9$ pour la seconde (fiche §1).",
)

GIVEN_26 = '''X_26 = np.array([[2.0, 1.5], [3.0, -1.0], [0.5, 2.5], [-1.0, -0.5],
                 [1.5, 3.0], [-2.0, 1.0], [0.0, -2.0], [2.5, 0.5]])   # 8 examples (multiples of 0.5: exact in floats)
Y_26 = np.array([1, 1, 1, -1, -1, -1, 1, -1])                          # their labels
W_26, B_26, C_26 = np.array([0.75, -0.5]), 0.25, 0.5                   # a separator (w, b) and the weight C
LABEL_0_26 = [1, 1, 1, 0, -1, -1, 1, -1]                               # a label 0 by mistake'''

SUB_26 = "mymath.svm.svm_subgradient(W_26, B_26, X_26, Y_26, C=C_26)"

M13B_26 = Ex(
    "M13b.26", "🔨", 2, 25, "La hinge loss et un sous-gradient de l'objectif d'une SVM linéaire · "
    "`hinge_loss, svm_subgradient`",
    "programmer la hinge loss et un sous-gradient de l'objectif d'une SVM à marge souple, avec la bonne convention "
    "au coude, et voir qu'un pas de sous-gradient peut faire monter l'objectif.", "fiche §7", tracks="C, E",
    mymath="svm.py", given=GIVEN_26,
    body=r"""Écris, en suivant les docstrings (fiche §7) :
- `hinge_loss(scores, y)` : `ValueError` si les scores sont vides ou pas 1-D, ou si `y` n'a pas un label −1 ou +1 par score ; sinon la **moyenne** des $\max(0, 1 - y_is_i)$ (`np.maximum`) ;
- `svm_subgradient(w, b, X, y, C=1.0)` : `ValueError` si les formes ne vont pas ensemble, si un label n'est ni −1 ni +1, ou si $C \le 0$ ; sinon le triplet $(J, \mathbf{g}_{\mathbf{w}}, g_b)$, avec $J = \frac{1}{2}\lVert\mathbf{w}\rVert^2 + C\sum_i \max(0, 1 - t_i)$ (une **somme** de hinges) et le sous-gradient de la fiche, qui ne compte que les exemples de marge fonctionnelle $t_i = y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ **strictement** inférieure à 1 : $\mathbf{g}_{\mathbf{w}} = \mathbf{w} - C\sum_{t_i < 1} y_i\mathbf{x}_i$ et $g_b = -C\sum_{t_i < 1} y_i$.

Les huit exemples de la cellule fournie ont des coordonnées multiples de 0,5 : avec $(\mathbf{w}, b)$ donné, le premier a une marge fonctionnelle **exactement** 1, en flottants aussi. La vérification calcule :
- a) `hinge_loss(X_26 @ W_26 + B_26, Y_26)` (6 décimales) ;
- b) $J$, le premier élément de `svm_subgradient(W_26, B_26, X_26, Y_26, C=C_26)` (6 décimales) ;
- c) $\mathbf{g}_{\mathbf{w}}$ (une liste, 6 décimales) ;
- d) $g_b$ (6 décimales) ;
- e) vrai ou faux : l'inégalité du sous-gradient, $J(\mathbf{v}, d) \ge J(\mathbf{w}, b) + \mathbf{g}_{\mathbf{w}} \cdot (\mathbf{v} - \mathbf{w}) + g_b\,(d - b)$, tient (à $10^{-12}$ près) pour 500 points $(\mathbf{v}, d)$ tirés au hasard (graine 4226) ;
- f) $J$ après un pas de taille $\eta = 0{,}5$, $(\mathbf{w}, b) \leftarrow (\mathbf{w}, b) - 0{,}5\,(\mathbf{g}_{\mathbf{w}}, g_b)$ (4 décimales) ;
- g) le nom de l'erreur levée par `svm_subgradient(W_26, B_26, X_26, LABEL_0_26, C=C_26)`.

Dans ta copie : calcule à la main les huit marges fonctionnelles, et range les exemples selon leur marge fonctionnelle ($t_i > 1$, $0 \le t_i \le 1$, $t_i < 0$). Retrouve a), b) et c). Que deviendrait $\mathbf{g}_{\mathbf{w}}$ si l'on comptait aussi le premier exemple, et pourquoi est-ce aussi un sous-gradient ? Compare f) à b) : que dit la fiche de ce phénomène, et le pas $\eta = 0{,}1$ ferait-il de même ?""",
    todo=LOAD_LEARNER,
    check=f'''with checked("M13b.26a"):
    wbm.check("M13b.26a", mymath.svm.hinge_loss(X_26 @ W_26 + B_26, Y_26), computed=True)
with checked("M13b.26b"):
    wbm.check("M13b.26b", {SUB_26}[0], computed=True)
with checked("M13b.26c"):
    wbm.check("M13b.26c", np.asarray({SUB_26}[1]).tolist(), computed=True)
with checked("M13b.26d"):
    wbm.check("M13b.26d", {SUB_26}[2], computed=True)
with checked("M13b.26e"):
    j_26, gw_26, gb_26 = {SUB_26}
    rng_26 = np.random.default_rng(4226)
    v_26, d_26 = W_26 + rng_26.normal(0.0, 1.5, size=(500, 2)), B_26 + rng_26.normal(0.0, 1.5, size=500)
    wbm.check("M13b.26e", all(mymath.svm.svm_subgradient(v, float(d), X_26, Y_26, C=C_26)[0]
                              >= j_26 + float(np.dot(gw_26, v - W_26)) + gb_26 * (d - B_26) - 1e-12
                              for v, d in zip(v_26, d_26)), computed=True)
with checked("M13b.26f"):
    j_26, gw_26, gb_26 = {SUB_26}
    wbm.check("M13b.26f", mymath.svm.svm_subgradient(W_26 - 0.5 * np.asarray(gw_26), B_26 - 0.5 * gb_26, X_26, Y_26,
                                                     C=C_26)[0], computed=True)
with checked("M13b.26g"):
    wbm.check("M13b.26g", raised(mymath.svm.svm_subgradient, W_26, B_26, X_26, LABEL_0_26, C=C_26), computed=True)''',
    solution=LOAD_REF + f'''
hinge_loss, svm_subgradient = mymath.svm.hinge_loss, mymath.svm.svm_subgradient
print("marges fonctionnelles :", (Y_26 * (X_26 @ W_26 + B_26)).tolist())
j_26, gw_26, gb_26 = svm_subgradient(W_26, B_26, X_26, Y_26, C=C_26)
print("a)", hinge_loss(X_26 @ W_26 + B_26, Y_26), " b)", j_26, " c)", gw_26.tolist(), " d)", gb_26)
rng_26 = np.random.default_rng(4226)
v_26, d_26 = W_26 + rng_26.normal(0.0, 1.5, size=(500, 2)), B_26 + rng_26.normal(0.0, 1.5, size=500)
print("e)", all(svm_subgradient(v, float(d), X_26, Y_26, C=C_26)[0] >= j_26 + float(gw_26 @ (v - W_26)) + gb_26 * (d - B_26)
                - 1e-12 for v, d in zip(v_26, d_26)))
for eta in (0.5, 0.1):
    print(f"J après un pas {{eta}} :", svm_subgradient(W_26 - eta * gw_26, B_26 - eta * gb_26, X_26, Y_26, C=C_26)[0])
print("g)", raised(svm_subgradient, W_26, B_26, X_26, LABEL_0_26, C=C_26))''',
    record='''from sklearn.metrics import hinge_loss as sk_hinge_loss

x_26r = np.array([[2.0, 1.5], [3.0, -1.0], [0.5, 2.5], [-1.0, -0.5], [1.5, 3.0], [-2.0, 1.0], [0.0, -2.0], [2.5, 0.5]])
y_26r, w_26r, b_26r, c_26r = np.array([1, 1, 1, -1, -1, -1, 1, -1]), np.array([0.75, -0.5]), 0.25, 0.5


def parts_26r(w, b, kink=False):
    """J, g_w and g_b computed example by example (kink=True also counts a margin equal to 1)."""
    margins = [float(yy * (x @ w + b)) for x, yy in zip(x_26r, y_26r)]
    chosen = [i for i, t in enumerate(margins) if (t <= 1 if kink else t < 1)]
    j = 0.5 * float(w @ w) + c_26r * sum(max(0.0, 1.0 - t) for t in margins)
    g_w = w - c_26r * sum((y_26r[i] * x_26r[i] for i in chosen), np.zeros(2))
    return j, g_w, -c_26r * float(sum(y_26r[i] for i in chosen))


j_26r, gw_26r, gb_26r = parts_26r(w_26r, b_26r)
hinges_26r = np.maximum(0.0, 1.0 - y_26r * (x_26r @ w_26r + b_26r))
wbm.record("M13b.26a", float(sk_hinge_loss(y_26r, x_26r @ w_26r + b_26r)), decimals=6,
           mistakes={"hinge_loss rend la MOYENNE des hinges, pas leur somme": float(hinges_26r.sum()),
                     "la hinge d'un exemple est max(0, 1 − y s), avec le label y":
                         float(np.mean(np.maximum(0.0, 1.0 - (x_26r @ w_26r + b_26r))))})
wbm.record("M13b.26b", j_26r, decimals=6,
           mistakes={"''' + SUM + '''": 0.5 * float(w_26r @ w_26r) + c_26r * float(hinges_26r.mean()),
                     "''' + HALF + '''": float(w_26r @ w_26r) + c_26r * float(hinges_26r.sum()),
                     "J = ½‖w‖² + C Σ max(0, 1 − tᵢ) : n'oublie pas C": 0.5 * float(w_26r @ w_26r) + float(hinges_26r.sum())})
below_26r = y_26r * (x_26r @ w_26r + b_26r) < 1
wbm.record("M13b.26c", gw_26r.tolist(), decimals=6,
           mistakes={"''' + STRICT + '''": parts_26r(w_26r, b_26r, kink=True)[1].tolist(),
                     "g_w commence par w, le gradient de ½‖w‖²": (gw_26r - w_26r).tolist(),
                     "g_w = w − C Σ yᵢ xᵢ, avec le label yᵢ": (w_26r - c_26r * x_26r[below_26r].sum(axis=0)).tolist()})
wbm.record("M13b.26d", gb_26r, decimals=6,
           mistakes={"''' + STRICT + '''": parts_26r(w_26r, b_26r, kink=True)[2],
                     "g_b = −C Σ yᵢ : attention au signe": -gb_26r})
wbm.record("M13b.26e", True,
           mistakes={"relis svm_subgradient : ses tests disent ce qui ne va pas": False})
wbm.record("M13b.26f", parts_26r(w_26r - 0.5 * gw_26r, b_26r - 0.5 * gb_26r)[0], decimals=4,
           mistakes={"le pas va dans la direction OPPOSÉE au sous-gradient : (w, b) − η (g_w, g_b)":
                         parts_26r(w_26r + 0.5 * gw_26r, b_26r + 0.5 * gb_26r)[0],
                     "le pas change aussi b : b − η g_b": parts_26r(w_26r - 0.5 * gw_26r, b_26r)[0]})
wbm.record("M13b.26g", "ValueError",
           ''' + value_error("un label 0 n'est pas un label de SVM : la docstring demande une ValueError") + ''')''',
    after=tests_cells("test_hinge or test_subgradient"),
    note=r"Les marges fonctionnelles valent $1$ ; $3$ ; $-0{,}625$ ; $0{,}25$ ; $0{,}125$ ; $1{,}75$ ; $1{,}25$ ; "
         r"$-1{,}875$ : deux exemples de l'autre côté de la frontière (le 3ᵉ et le 8ᵉ, $t < 0$), deux entre le bord de "
         r"leur classe et la frontière (le 4ᵉ et le 5ᵉ), le premier exactement sur son bord, les trois autres au-delà. Hinges : $1{,}625 + 0{,}75 + 0{,}875 + "
         r"2{,}875 = 6{,}125$, moyenne $0{,}765625$ ; $J = \frac{1}{2}(0{,}5625 + 0{,}25) + 0{,}5 \times 6{,}125 = "
         r"3{,}46875$. Les quatre exemples de marge strictement sous 1 donnent $\sum y_i\mathbf{x}_i = (-2{,}5 ;\ "
         r"-0{,}5)$, d'où $\mathbf{g}_{\mathbf{w}} = (2 ;\ -0{,}25)$ et $g_b = 1$. Compter aussi le premier exemple "
         r"donnerait $(1 ;\ -1)$ et $0{,}5$ : un autre sous-gradient, valide lui aussi (au coude, toute pente de la "
         r"hinge entre −1 et 0 convient). f) Le pas 0,5 fait passer $J$ de 3,46875 à 4,5078 : un pas de "
         r"sous-gradient ne garantit pas la baisse (fiche §7). Avec $\eta = 0{,}1$, $J$ baisse (3,2141) : la dérivée "
         r"de $J$ dans la direction $-\mathbf{g}$ est négative ici, et un petit pas suffit.",
)

GIVEN_27 = '''X_27 = np.array([[0.5, -1.0], [1.5, 0.0], [-0.5, 1.0]])    # 3 points x_i
Z_27 = np.array([[1.0, 0.5], [-1.5, -0.5]])               # 2 points z_j
rng_27 = np.random.default_rng(4227)
G_27 = rng_27.normal(0.0, 1.0, size=(30, 3))               # 30 points, for a Gram matrix
F_27 = 3000.0 + rng_27.normal(0.0, 1.0, size=(40, 3))     # 40 points far from the origin, close to one another'''

M13B_27 = Ex(
    "M13b.27", "🔨", 1, 20, "Les noyaux RBF et polynomial · `rbf_kernel, polynomial_kernel`",
    "programmer les matrices des noyaux RBF et polynomial en un seul produit matriciel, sans erreur d'arrondi qui "
    "dépasse 1.", "fiche §8", tracks="C, E", mymath="svm.py", given=GIVEN_27,
    body=r"""Écris, en suivant les docstrings (fiche §8) :
- `rbf_kernel(X, Z, gamma)` : `ValueError` si `X` ou `Z` n'est pas 2-D, si leurs nombres de colonnes diffèrent, ou si $\gamma \le 0$ ; sinon la matrice $\mathbf{K}_{ij} = e^{-\gamma\lVert\mathbf{x}_i - \mathbf{z}_j\rVert^2}$, ligne $i$ pour $\mathbf{x}_i$, colonne $j$ pour $\mathbf{z}_j$. Calcule tous les carrés de distances d'un coup en développant $\lVert\mathbf{x} - \mathbf{z}\rVert^2 = \lVert\mathbf{x}\rVert^2 - 2\,\mathbf{x} \cdot \mathbf{z} + \lVert\mathbf{z}\rVert^2$ (un produit `X @ Z.T` et deux sommes de carrés), puis remplace par 0 les petites valeurs négatives que l'arrondi peut produire (`np.maximum`) ;
- `polynomial_kernel(X, Z, degree=2, coef0=1.0)` : les mêmes contrôles de forme, `ValueError` si `degree` n'est pas un entier $\ge 1$ ou si `coef0` est négatif ; sinon $\mathbf{K}_{ij} = (\mathbf{x}_i \cdot \mathbf{z}_j + c)^d$.

La vérification calcule, avec les points de la cellule fournie :
- a) `rbf_kernel(X_27, Z_27, 0.4)` (une matrice $3 \times 2$, comme une liste de lignes, 6 décimales) ;
- b) `polynomial_kernel(X_27, Z_27, degree=3, coef0=0.5)` (6 décimales) ;
- c) vrai ou faux : la matrice de Gram `rbf_kernel(G_27, G_27, 0.7)` des 30 points est symétrique (à $10^{-12}$ près) et ses valeurs propres sont toutes $\ge -10^{-10}$ ;
- d) vrai ou faux : toutes les valeurs de `rbf_kernel(F_27, F_27, 0.5)` sont $\le 1$, pour 40 points de coordonnées voisines de 3 000 ;
- e) le nom de l'erreur levée par `rbf_kernel(X_27, Z_27, 0.0)`.

Dans ta copie : retrouve à la main une valeur de a) (les carrés des distances d'abord) et une de b). Pourquoi la matrice de c) n'est-elle pas **exactement** symétrique en flottants, alors qu'elle l'est en théorie ? Pour d), si tu as calculé par développement, que vaudrait la diagonale sans `np.maximum`, et pourquoi le développement du carré perd-il des chiffres quand les points sont loin de l'origine (compare $\lVert\mathbf{x}\rVert^2 \approx 2{,}7 \times 10^7$ à l'écart cherché) ? Pourquoi $\gamma = 0$ est-il refusé ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M13b.27a"):
    wbm.check("M13b.27a", np.asarray(mymath.svm.rbf_kernel(X_27, Z_27, 0.4)).tolist(), computed=True)
with checked("M13b.27b"):
    wbm.check("M13b.27b", np.asarray(mymath.svm.polynomial_kernel(X_27, Z_27, degree=3, coef0=0.5)).tolist(),
              computed=True)
with checked("M13b.27c"):
    k_27 = np.asarray(mymath.svm.rbf_kernel(G_27, G_27, 0.7), dtype=float)
    wbm.check("M13b.27c", bool(k_27.shape == (30, 30) and np.allclose(k_27, k_27.T, rtol=0, atol=1e-12)
                               and np.linalg.eigvalsh((k_27 + k_27.T) / 2).min() >= -1e-10), computed=True)
with checked("M13b.27d"):
    wbm.check("M13b.27d", bool(np.max(mymath.svm.rbf_kernel(F_27, F_27, 0.5)) <= 1.0), computed=True)
with checked("M13b.27e"):
    wbm.check("M13b.27e", raised(mymath.svm.rbf_kernel, X_27, Z_27, 0.0), computed=True)''',
    solution=LOAD_REF + '''
rbf_kernel, polynomial_kernel = mymath.svm.rbf_kernel, mymath.svm.polynomial_kernel
print("carrés des distances :", (((X_27[:, None, :] - Z_27[None, :, :]) ** 2).sum(axis=2)).tolist())
print("a)", np.round(rbf_kernel(X_27, Z_27, 0.4), 6).tolist())
print("b)", np.round(polynomial_kernel(X_27, Z_27, degree=3, coef0=0.5), 6).tolist())
k_27 = rbf_kernel(G_27, G_27, 0.7)
print("c) symétrique exactement ?", bool(np.array_equal(k_27, k_27.T)), " ; à 1e-12 près ?",
      bool(np.allclose(k_27, k_27.T, rtol=0, atol=1e-12)), " ; plus petite valeur propre :",
      round(float(np.linalg.eigvalsh((k_27 + k_27.T) / 2).min()), 6))
squared_27 = np.sum(F_27 ** 2, axis=1)[:, None] - 2 * F_27 @ F_27.T + np.sum(F_27 ** 2, axis=1)[None, :]
print("d) max :", float(rbf_kernel(F_27, F_27, 0.5).max()), " ; sans np.maximum :", float(np.exp(-0.5 * squared_27).max()),
      " ; diagonale la plus négative :", float(np.diag(squared_27).min()))
print("e)", raised(rbf_kernel, X_27, Z_27, 0.0))''',
    record='''from scipy.spatial.distance import cdist

x_27r, z_27r = np.array([[0.5, -1.0], [1.5, 0.0], [-0.5, 1.0]]), np.array([[1.0, 0.5], [-1.5, -0.5]])
d2_27r = cdist(x_27r, z_27r, "sqeuclidean")
wbm.record("M13b.27a", np.exp(-0.4 * d2_27r).tolist(), decimals=6,
           mistakes={"''' + SQUARED + '''": np.exp(-0.4 * np.sqrt(d2_27r)).tolist(),
                     "e^(−γ d²) : γ MULTIPLIE le carré de la distance": np.exp(-d2_27r / 0.4).tolist(),
                     "ligne i pour xᵢ, colonne j pour zⱼ : une matrice (3, 2)": np.exp(-0.4 * d2_27r).T.tolist()})
dots_27r = np.array([[sum(a * b for a, b in zip(x, z)) for z in z_27r] for x in x_27r])
wbm.record("M13b.27b", ((dots_27r + 0.5) ** 3).tolist(), decimals=6,
           mistakes={"(x · z + coef0)^degree : n'oublie pas coef0": (dots_27r ** 3).tolist(),
                     "degree=3 : le cube de x · z + coef0": ((dots_27r + 0.5) ** 2).tolist()})
wbm.record("M13b.27c", True,
           mistakes={"relis rbf_kernel : ses tests disent ce qui ne va pas (une matrice de Gram de noyau est "
                     "symétrique et semi-définie positive)": False})
wbm.record("M13b.27d", True,
           mistakes={"l'arrondi du développement ‖x‖² − 2 x · z + ‖z‖² donne de petits carrés négatifs : remplace-les "
                     "par 0 (np.maximum) avant l'exponentielle": False})
wbm.record("M13b.27e", "ValueError",
           ''' + value_error("le noyau RBF demande γ > 0 : la docstring demande une ValueError pour γ = 0") + ''')''',
    after=tests_cells("test_rbf or test_polynomial"),
    note=r"Les carrés des distances valent $2{,}5$ et $4{,}25$ ; $0{,}5$ et $9{,}25$ ; $2{,}5$ et $3{,}25$ : a) "
         r"$e^{-1} \approx 0{,}367879$, $e^{-1{,}7} \approx 0{,}182684$, puis $e^{-0{,}2}$, $e^{-3{,}7}$, $e^{-1}$, "
         r"$e^{-1{,}3}$. b) Les produits scalaires $0$ et $-0{,}25$ ; $1{,}5$ et $-2{,}25$ ; $0$ et $0{,}25$ donnent "
         r"$0{,}125$ ; $0{,}015625$ ; $8$ ; $-5{,}359375$ ; $0{,}125$ ; $0{,}421875$ : un noyau polynomial peut être "
         r"négatif. c) $\lVert\mathbf{x}_i\rVert^2 - 2\,\mathbf{x}_i \cdot \mathbf{x}_j + \lVert\mathbf{x}_j\rVert^2$ "
         r"et la même somme dans l'autre ordre ne s'arrondissent pas toujours de la même façon : symétrique à $10^{-16}$ "
         r"près, pas exactement ; plus petite valeur propre $\approx 0{,}023 > 0$. d) Pour des points voisins de "
         r"3 000, $\lVert\mathbf{x}\rVert^2 \approx 2{,}7 \times 10^7$ ; l'arrondi, de l'ordre de $10^{-8}$ ici, "
         r"donne des carrés de distances diagonaux de $-1{,}5 \times 10^{-8}$ : sans `np.maximum`, $e^{+0{,}75 \times "
         r"10^{-8}} > 1$, une « similarité » plus grande que celle d'un point avec lui-même. e) Avec $\gamma = 0$, toutes "
         r"les valeurs vaudraient 1 : le noyau ne distinguerait plus aucun point.",
)

GIVEN_28 = '''from scipy.optimize import minimize
from sklearn.metrics import hinge_loss
from sklearn.metrics.pairwise import polynomial_kernel, rbf_kernel

rng_28 = np.random.default_rng(4228)
X_28 = np.round(rng_28.normal(0.0, 1.0, size=(5, 3)), 2)     # 5 points
Z_28 = np.round(rng_28.normal(0.0, 1.0, size=(4, 3)), 2)     # 4 other points
P_28 = np.round(rng_28.normal(0.0, 1.0, size=(3, 4)), 2)     # 3 points with p = 4 features
R_28 = np.round(rng_28.normal(0.0, 1.0, size=(2, 4)), 2)     # 2 other points with 4 features
Y_28 = np.where(rng_28.random(12) < 0.5, -1, 1)              # 12 labels
S_28 = np.round(rng_28.normal(0.3, 1.5, size=12), 2)         # their scores'''

M13B_28 = Ex(
    "M13b.28", "📦", 1, 15, "`scipy.optimize.minimize` sous contraintes et les noyaux de scikit-learn contre tes "
    "fonctions",
    "résoudre un problème sous contraintes avec `scipy.optimize.minimize`, utiliser les noyaux et la hinge loss de "
    "scikit-learn, lire leurs paramètres par défaut, et comparer avec ta librairie.",
    "fiche §2 et §8 ; Ex M13b.25 à M13b.27", tracks="C, E", given=GIVEN_28,
    body=r"""En pratique, ces calculs sont tout faits :
- `minimize(fun, x0, jac=grad, method="SLSQP", constraints=[{"type": "eq", "fun": h, "jac": dh}], tol=1e-12)` (SciPy) part de `x0` et cherche le minimum de `fun` sous la contrainte $h(\mathbf{x}) = \mathbf{0}$ (`h` rend un vecteur, une coordonnée par contrainte ; `grad` et `dh` rendent le gradient de `fun` et la jacobienne de `h`, la matrice dont les lignes sont les gradients des coordonnées de `h` ; M17 l'étudiera) ; elle rend un objet `res` : `res.x` est le point trouvé, `res.fun` la valeur de `fun` en ce point, `res.nit` le nombre d'itérations ;
- `rbf_kernel(X, Z, gamma=g)` (scikit-learn) rend la matrice des $e^{-g\lVert\mathbf{x}_i - \mathbf{z}_j\rVert^2}$ ; sans `gamma`, elle prend $g = 1/p$, avec $p$ le nombre de features ;
- `polynomial_kernel(X, Z, degree=d, gamma=g, coef0=r)` rend la matrice des $(g\,\mathbf{x}_i \cdot \mathbf{z}_j + r)^d$ ; sans paramètres, $d = 3$, $g = 1/p$ et $r = 1$ ;
- `hinge_loss(y, s)` rend la hinge **moyenne** des scores `s` pour les labels `y` : les labels **d'abord**, à l'inverse de ta fonction.

Calcule :
- a) `res.fun` pour le problème de M13b.25 (`Q_25`, `C_25`, `A_25`, `B_25`), avec `fun` $= \frac{1}{2}\mathbf{x}^\top\mathbf{Q}\mathbf{x} + \mathbf{c}^\top\mathbf{x}$, son gradient, la contrainte $\mathbf{A}\mathbf{x} - \mathbf{b} = \mathbf{0}$ et sa jacobienne $\mathbf{A}$, depuis `x0 = np.zeros(4)`, avec `tol=1e-12` (6 décimales) ;
- b) vrai ou faux : `res.x` et le $\mathbf{x}$ de ta fonction `lagrange_equality_qp` sont égaux à $10^{-6}$ près (`np.allclose(..., rtol=0, atol=1e-6)`) ;
- c) vrai ou faux : `rbf_kernel(X_28, Z_28, gamma=0.3)` de scikit-learn et ta fonction `rbf_kernel(X_28, Z_28, 0.3)` sont égales à $10^{-12}$ près ;
- d) vrai ou faux : `polynomial_kernel(X_28, Z_28, degree=3, gamma=1.0, coef0=0.5)` et ta fonction `polynomial_kernel(X_28, Z_28, degree=3, coef0=0.5)` sont égales à $10^{-12}$ près (relativement : `np.allclose(..., rtol=1e-12, atol=1e-12)`) ;
- e) la valeur `[0, 0]` de `polynomial_kernel(P_28, R_28)` de scikit-learn, **sans aucun paramètre** (6 décimales). Ne devine pas : **exécute-la** ;
- f) `hinge_loss(Y_28, S_28)` de scikit-learn (6 décimales) ;
- g) vrai ou faux : ta fonction `hinge_loss(S_28, Y_28)` est égale à f), à $10^{-12}$ près ;
- h) le nom de l'erreur levée par `hinge_loss(S_28, Y_28)` de scikit-learn, les arguments dans l'ordre de ta fonction (exécute-la dans un `try` / `except Exception as exc`, puis `type(exc).__name__`).

Dans ta copie : combien d'itérations SLSQP a-t-elle faites (`res.nit`), et pourquoi ta fonction n'en a-t-elle besoin d'aucune ? Retrouve e) à la main à partir de `P_28[0] @ R_28[0]` : quels sont les trois paramètres par défaut, et quelle valeur aurait donnée ta fonction avec ses propres défauts ? Que penses-tu d'un message d'erreur comme celui de h) quand on inverse deux arguments ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M13b")
answer_M13b_28a = ...  # a) a number (6 decimals)
answer_M13b_28e = ...  # e) a number (6 decimals)
answer_M13b_28f = ...  # f) a number (6 decimals)
answer_M13b_28h = ...  # h) the name of an exception, as text
answer_M13b_28b = answer_M13b_28c = answer_M13b_28d = answer_M13b_28g = ...
# Each block stands alone: compute inside it what it needs, so that "Run all" goes on when a function is not written.
with wbm.attempt("M13b.28b"):        # your lagrange_equality_qp is called here: ⏳ while it is not written
    answer_M13b_28b = ...  # b) True or False
with wbm.attempt("M13b.28c"):        # your rbf_kernel
    answer_M13b_28c = ...  # c) True or False
with wbm.attempt("M13b.28d"):        # your polynomial_kernel
    answer_M13b_28d = ...  # d) True or False
with wbm.attempt("M13b.28g"):        # your hinge_loss
    answer_M13b_28g = ...  # g) True or False''',
    check='''for letter, answer in zip("abcdefgh", [answer_M13b_28a, answer_M13b_28b, answer_M13b_28c, answer_M13b_28d,
                                        answer_M13b_28e, answer_M13b_28f, answer_M13b_28g, answer_M13b_28h]):
    wbm.check(f"M13b.28{letter}", answer)''',
    solution='''ref_28 = wbm.load_mymath("ref", alias="mymath_ref").svm
res_28 = minimize(lambda x: 0.5 * x @ Q_25 @ x + C_25 @ x, np.zeros(4), jac=lambda x: Q_25 @ x + C_25, method="SLSQP",
                  constraints=[{"type": "eq", "fun": lambda x: A_25 @ x - B_25, "jac": lambda x: A_25}], tol=1e-12)
answer_M13b_28a = round(float(res_28.fun), 6)
answer_M13b_28b = bool(np.allclose(res_28.x, ref_28.lagrange_equality_qp(Q_25, C_25, A_25, B_25)[0], rtol=0, atol=1e-6))
answer_M13b_28c = bool(np.allclose(rbf_kernel(X_28, Z_28, gamma=0.3), ref_28.rbf_kernel(X_28, Z_28, 0.3), rtol=0,
                                   atol=1e-12))
answer_M13b_28d = bool(np.allclose(polynomial_kernel(X_28, Z_28, degree=3, gamma=1.0, coef0=0.5),
                                   ref_28.polynomial_kernel(X_28, Z_28, degree=3, coef0=0.5), rtol=1e-12, atol=1e-12))
answer_M13b_28e = round(float(polynomial_kernel(P_28, R_28)[0, 0]), 6)
answer_M13b_28f = round(float(hinge_loss(Y_28, S_28)), 6)
answer_M13b_28g = math.isclose(ref_28.hinge_loss(S_28, Y_28), float(hinge_loss(Y_28, S_28)), rel_tol=1e-12)
try:
    hinge_loss(S_28, Y_28)
    answer_M13b_28h = "aucune"
except Exception as exc:  # noqa: BLE001 - the name of the error is the answer
    answer_M13b_28h = type(exc).__name__
    message_28 = str(exc)
print(answer_M13b_28a, answer_M13b_28b, answer_M13b_28c, answer_M13b_28d, answer_M13b_28e, answer_M13b_28f,
      answer_M13b_28g, answer_M13b_28h)
dot_28 = float(P_28[0] @ R_28[0])
print("res.nit :", res_28.nit, " ; P_28[0] · R_28[0] =", round(dot_28, 4), " ; (x · z/4 + 1)³ =",
      round((dot_28 / 4 + 1) ** 3, 6), " ; tes défauts, (x · z + 1)² :", round((dot_28 + 1) ** 2, 6))
print("le message de h) :", message_28[:160])''',
    record='''from scipy.optimize import minimize as minimize_r
from sklearn.metrics import hinge_loss as hinge_r
from sklearn.metrics.pairwise import polynomial_kernel as poly_r

q_28r = np.array([[6.0, 1.0, 0.0, -1.0], [1.0, 4.0, 1.0, 0.0], [0.0, 1.0, 5.0, 2.0], [-1.0, 0.0, 2.0, 3.0]])
c_28r, a_28r, b_28r = np.array([-2.0, 3.0, -1.0, 4.0]), np.array([[1.0, -2.0, 1.0, 3.0], [2.0, 0.0, -1.0, 1.0]]), \\
    np.array([5.0, -3.0])


def solve_28r(weight):
    """min weight · xᵀQx + cᵀx under A x = b, with SLSQP."""
    return minimize_r(lambda x: weight * x @ q_28r @ x + c_28r @ x, np.zeros(4),
                      jac=lambda x: 2 * weight * q_28r @ x + c_28r, method="SLSQP",
                      constraints=[{"type": "eq", "fun": lambda x: a_28r @ x - b_28r, "jac": lambda x: a_28r}], tol=1e-12)


wbm.record("M13b.28a", float(solve_28r(0.5).fun), decimals=6,
           mistakes={"fun = ½ xᵀQx + cᵀx, avec le ½ : sans lui, SLSQP minimise une autre fonction":
                         float(solve_28r(1.0).fun)})
wbm.record("M13b.28b", True,
           mistakes={"compare res.x et ton x à 1e−6 près ; si l'écart est grand, passe tol=1e-12 à minimize, ou relis "
                     "lagrange_equality_qp (M13b.25)": False})
wbm.record("M13b.28c", True,
           mistakes={"passe gamma=0.3 à scikit-learn (sans lui, gamma = 1/p), ou relis ta fonction rbf_kernel (M13b.27)":
                         False})
wbm.record("M13b.28d", True,
           mistakes={"passe gamma=1.0 à scikit-learn (sans lui, gamma = 1/p), ou relis ta fonction polynomial_kernel "
                     "(M13b.27)": False})
rng_28r = np.random.default_rng(4228)
for shape in ((5, 3), (4, 3)):
    rng_28r.normal(0.0, 1.0, size=shape)
p_28r, r_28r = (np.round(rng_28r.normal(0.0, 1.0, size=shape), 2) for shape in ((3, 4), (2, 4)))
y_28r = np.where(rng_28r.random(12) < 0.5, -1, 1)
s_28r = np.round(rng_28r.normal(0.3, 1.5, size=12), 2)
dot_28r = float(p_28r[0] @ r_28r[0])
wbm.record("M13b.28e", float(poly_r(p_28r, r_28r)[0, 0]), decimals=6,
           mistakes={"sans paramètre, gamma vaut 1/p, pas 1 : exécute la ligne": (dot_28r + 1) ** 3,
                     "le degré par défaut de scikit-learn est 3 : exécute la ligne": (dot_28r / 4 + 1) ** 2,
                     "ce sont les défauts de ta fonction (degré 2, sans gamma) : exécute celle de scikit-learn":
                         (dot_28r + 1) ** 2})
wbm.record("M13b.28f", float(hinge_r(y_28r, s_28r)), decimals=6,
           mistakes={"hinge_loss rend la MOYENNE des hinges, pas leur somme": float(hinge_r(y_28r, s_28r)) * 12})
wbm.record("M13b.28g", True,
           mistakes={"scikit-learn prend les labels EN PREMIER, hinge_loss(Y_28, S_28) ; ta fonction, les scores : "
                     "sinon, relis ta fonction hinge_loss (M13b.26)": False})
wbm.record("M13b.28h", "ValueError",
           mistakes={"exécute la ligne dans un try / except : scikit-learn refuse des « labels » qui sont des scores":
                         "aucune",
                     "le nom exact de l'erreur, tel que Python l'affiche : type(exc).__name__": ''' +
           errors_source("ValueError") + '''})''',
    note=r"a) $\approx 4{,}017413$, la valeur de $f$ en M13b.25 : SLSQP la retrouve en 8 itérations (le nombre dépend "
         r"des versions), à $10^{-7}$ près sur $\mathbf{x}$ ; ta fonction résout un seul système linéaire, exact aux "
         r"arrondis près, parce que le problème est quadratique et les contraintes affines. SLSQP sert quand ce n'est "
         r"pas le cas (des contraintes non linéaires, des inégalités). e) `polynomial_kernel` sans paramètres calcule "
         r"$(\frac{1}{4}\mathbf{x} \cdot \mathbf{z} + 1)^3$ pour $p = 4$ features : $\mathbf{x} \cdot \mathbf{z} "
         r"\approx 1{,}0749$ donne $\approx 2{,}042220$, quand $(\mathbf{x} \cdot \mathbf{z} + 1)^3 \approx 8{,}93$ "
         r"et tes défauts $(\mathbf{x} \cdot \mathbf{z} + 1)^2 \approx 4{,}31$ : comparer deux bibliothèques demande "
         r"de passer tous les paramètres. h) Avec les scores en premier, scikit-learn prend les 12 scores pour des "
         r"labels de 12 classes, et lève une `ValueError` qui parle de forme et de classes, pas d'ordre des "
         r"arguments : un message qui ne dit pas la vraie cause, à reconnaître.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M13b.29 to M13b.31)
# ---------------------------------------------------------------------------
GIVEN_29 = '''Q_29 = np.array([[3.0, -1.0], [-1.0, 4.0]])     # f(x) = ½ xᵀ Q_29 x + LIN_29 · x = 1.5x² − xy + 2y² − 3x − 2y
LIN_29 = np.array([-3.0, -2.0])
A_29, RHS_29 = np.array([2.0, -1.0]), 5.0       # the constraint a · x = c: 2x − y = 5'''

EXPERIMENT_29 = '''ref_29 = wbm.load_mymath("ref", alias="mymath_ref").svm


def solve_29(Q, lin, a, c):
    """(f*, λ) of min ½ xᵀQx + lin · x under a · x = c, with the reference lagrange_equality_qp."""
    x, lam = ref_29.lagrange_equality_qp(Q, lin, [a], [c])
    return float(0.5 * x @ Q @ x + lin @ x), float(lam[0])


f0_29, lam0_29 = solve_29(Q_29, LIN_29, A_29, RHS_29)
f1_29 = solve_29(Q_29, LIN_29, A_29, RHS_29 + 0.1)[0]
print(f"a) et b) f*(5) = {f0_29:.4f}, f*(5,1) = {f1_29:.4f} : le minimum change de {f1_29 - f0_29:+.4f}, "
      f"et −λ × 0,1 = {-lam0_29 * 0.1:+.4f}".replace(".", ","))
print(f"c) λ pour f : {lam0_29:.4f} ; pour 2f : {solve_29(2 * Q_29, 2 * LIN_29, A_29, RHS_29)[1]:.4f}".replace(".", ","))
print(f"d) λ pour 4x − 2y = 10 : {solve_29(Q_29, LIN_29, 2 * A_29, 2 * RHS_29)[1]:.4f}".replace(".", ","))
cs_29 = np.linspace(3.0, 7.0, 81)
fig, ax = plt.subplots(figsize=(6.5, 3.6))
ax.plot(cs_29, [solve_29(Q_29, LIN_29, A_29, c)[0] for c in cs_29], label="f*(c), le minimum sous 2x − y = c")
ax.plot(cs_29, f0_29 - lam0_29 * (cs_29 - RHS_29), ls="--", label="la tangente en c = 5, de pente −λ")
ax.plot([RHS_29], [f0_29], "o", color="C3")
ax.set_xlabel("second membre c")
ax.set_ylabel("minimum f*(c)")
ax.legend()
plt.show()'''

M13B_29 = Ex(
    "M13b.29", "🔮", 1, 10, "Prédire : comment change le minimum quand on relâche la contrainte, et ce que dit λ",
    "prévoir, à partir du multiplicateur de Lagrange, comment le minimum réagit quand on déplace la contrainte, et "
    "comment le multiplicateur change quand on réécrit le problème, puis le vérifier.", "fiche §1 et §4",
    tracks="C, E", hypothesis=True, given=GIVEN_29,
    body=r"""On minimise $f(x, y) = 1{,}5x^2 - xy + 2y^2 - 3x - 2y$ sous la contrainte $2x - y = c$, avec le lagrangien $f + \lambda(2x - y - c)$ (la cellule fournie l'écrit sous la forme $\frac{1}{2}\mathbf{x}^\top\mathbf{Q}\mathbf{x} + \mathbf{q} \cdot \mathbf{x}$, contrainte $\mathbf{a} \cdot \mathbf{x} = c$). Pour $c = 5$, la solution est $(x, y) = (2{,}8 ;\ 0{,}6)$, avec le multiplicateur $\lambda = -2{,}4$. Pour chaque question, choisis le numéro de la bonne réponse :
- a) quand $c$ passe de 5 à 5,1, le minimum $f^*$ : (1) monte ; (2) baisse ; (3) ne change pas ; (4) on ne peut pas le savoir sans tout recalculer ;
- b) de combien, environ : (1) 0,024 ; (2) 0,24 ; (3) 2,4 ; (4) 24 ;
- c) si l'on multiplie $f$ par 2 (même contrainte), le multiplicateur : (1) ne change pas ; (2) est multiplié par 2 ; (3) est divisé par 2 ; (4) change de signe ;
- d) si l'on écrit la même contrainte $4x - 2y = 10$ (même $f$), le multiplicateur : mêmes choix qu'en c).

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience : elle résout le problème avec `lagrange_equality_qp` de la référence pour plusieurs valeurs de $c$, trace $f^*(c)$ et sa tangente en $c = 5$.""",
    todo='''prediction_M13b_29a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M13b_29b = ...  # b) 1, 2, 3 or 4
prediction_M13b_29c = ...  # c) 1, 2, 3 or 4
prediction_M13b_29d = ...  # d) 1, 2, 3 or 4''',
    check='''for letter, prediction in zip("abcd", [prediction_M13b_29a, prediction_M13b_29b, prediction_M13b_29c,
                                      prediction_M13b_29d]):
    wbm.check(f"M13b.29{letter}", prediction)''',
    record='''wbm.record("M13b.29a", 1, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M13b.29b", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M13b.29c", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M13b.29d", 3, prediction=True, choices=[1, 2, 3, 4])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(EXPERIMENT_29, [f"prediction_M13b_29{letter}" for letter in "abcd"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", EXPERIMENT_29),
        ("md", "**Après l'expérience**, dans ta copie : pourquoi l'écart mesuré en b) n'est-il pas exactement "
               "$-\\lambda \\times 0{,}1$ (regarde la courbure de $f^*(c)$) ? Écris la stationnarité pour $2f$ et pour "
               "la contrainte multipliée par 2, et retrouve c) et d) sans calcul. Que dit un multiplicateur nul ? "
               "Pourquoi le signe de $\\lambda$ dépend-il de la convention $f + \\lambda g$ ou $f - \\lambda g$, et "
               "pas la variation de $f^*$ ?"),
    ],
    note=r"a) et b) La sensibilité $\frac{df^*}{dc} = -\lambda = 2{,}4$ (fiche §1) : le minimum monte d'environ $2{,}4 "
         r"\times 0{,}1 = 0{,}24$ ; on mesure $0{,}2437$, parce que $f^*(c) = \frac{11}{30}c^2 - \frac{19}{15}c - "
         r"\frac{49}{30}$ est une parabole, au-dessus de sa tangente. c) La stationnarité $2\nabla f + \lambda'\nabla g = "
         r"\mathbf{0}$ et $\nabla f + \lambda\nabla g = \mathbf{0}$ donnent $\lambda' = 2\lambda = -4{,}8$ : un prix "
         r"s'exprime dans l'unité de l'objectif. d) $\nabla f + \lambda'(2\nabla g) = \mathbf{0}$ donne $\lambda' = "
         r"\lambda/2 = -1{,}2$ : une unité de la contrainte $4x - 2y = 10$ vaut une demi-unité de $2x - y = 5$. Le "
         r"multiplicateur est un prix : il dépend de l'unité de l'objectif et de celle de la contrainte, pas du point "
         r"solution, qui ne change dans aucun des deux cas.",
)

GIVEN_30 = '''from sklearn.svm import SVC

rng_30 = np.random.default_rng(4230)
Y_30 = np.where(rng_30.random(150) < 0.5, -1, 1)                                     # 150 labels ±1
X_30 = rng_30.normal(0.0, 1.0, size=(150, 3)) + np.outer(Y_30, [0.9, -0.7, 0.5])    # two classes that overlap a bit
C_30, STEPS_30 = 0.5, 300
SCHEDULES_30 = {"constant 0,01": lambda t: 0.01,                                     # the step η_t at iteration t
                "constant 0,001": lambda t: 0.001,
                "décroissant 0,01/√t": lambda t: 0.01 / math.sqrt(t)}
ref_30 = wbm.load_mymath("ref", alias="mymath_ref").svm
svc_30 = SVC(kernel="linear", C=C_30, tol=1e-10).fit(X_30, Y_30)
J_STAR_30 = ref_30.svm_subgradient(svc_30.coef_[0], float(svc_30.intercept_[0]), X_30, Y_30, C_30)[0]   # min of J'''

FIGURE_30 = '''fig, ax = plt.subplots(figsize=(7.5, 3.8))
try:
    for (name, eta), color in zip(SCHEDULES_30.items(), ("C0", "C1", "C2")):
        gaps = np.asarray(run_subgradient(X_30, Y_30, C_30, STEPS_30, eta), dtype=float) - J_STAR_30
        steps = np.arange(1, len(gaps) + 1)
        ax.semilogy(steps, np.maximum(gaps, 1e-9), color=color, lw=0.7, alpha=0.6, label=f"pas {name} : J − J*")
        ax.semilogy(steps, np.maximum(np.minimum.accumulate(gaps), 1e-9), color=color, lw=2, ls="--",
                    label=f"pas {name} : meilleur écart vu")
    ax.set_xlabel("itération t")
    ax.set_ylabel("J(w_t, b_t) − J*")
    ax.legend(fontsize=7, ncol=2)
except BaseException:
    plt.close(fig)
    raise
plt.show()'''

M13B_30 = Ex(
    "M13b.30", "🔬", 2, 20, "La descente de sous-gradient sur la hinge loss : pas constant contre pas décroissant",
    "mesurer comment le choix du pas règle la descente de sous-gradient sur l'objectif d'une SVM linéaire : "
    "oscillations d'un pas constant, lenteur d'un petit pas, convergence d'un pas décroissant.", "fiche §7",
    tracks="C", given=GIVEN_30,
    body=r"""150 exemples synthétiques en dimension 3, de deux classes qui se chevauchent un peu (cellule fournie), et l'objectif $J(\mathbf{w}, b)$ d'une SVM à marge souple avec $C = 0{,}5$. La cellule fournie calcule aussi son minimum $J^*$, avec la SVM de scikit-learn (`SVC(kernel="linear", C=0.5, tol=1e-10)`, un solveur du dual) et la fonction `svm_subgradient` de la référence, `ref_30`. Écris :
- `run_subgradient(X, y, C, steps, eta)` : la descente de sous-gradient qui part de $\mathbf{w} = \mathbf{0}$, $b = 0$ et, pour $t = 1, \ldots,$ `steps`, calcule `(J, g_w, g_b) = svm_subgradient(w, b, X, y, C)` (celle de la référence, `ref_30.svm_subgradient`, ou la tienne), range $J$ dans une liste, puis fait le pas $(\mathbf{w}, b) \leftarrow (\mathbf{w}, b) - \eta_t\,(\mathbf{g}_{\mathbf{w}}, g_b)$, avec $\eta_t$ = `eta(t)`. Elle rend la liste des `steps` valeurs de $J$, la première étant $J(\mathbf{0}, 0)$.

Lance-la pour les trois réglages du dictionnaire `SCHEDULES_30` (un pas constant 0,01, un pas constant 0,001, un pas décroissant $\eta_t = 0{,}01/\sqrt{t}$), avec 300 itérations, puis calcule :
- a) les trois meilleurs écarts $\min_t J_t - J^*$, dans l'ordre de `SCHEDULES_30` (une liste, 6 décimales) ;
- b) vrai ou faux : le pas décroissant finit avec un meilleur écart plus petit que celui des deux pas constants ;
- c) le nombre d'itérations où $J$ **remonte** ($J_{t+1} > J_t$) avec le pas constant 0,01 (un entier).

Une cellule trace ensuite $J_t - J^*$ en échelle logarithmique pour les trois réglages, avec le meilleur écart vu.

Dans ta copie : pourquoi le pas constant 0,01 ne descend-il plus sous un certain niveau, et pourquoi $J$ remonte-t-il si souvent (la fiche §7 dit pourquoi ce n'est pas une méthode de descente) ? Pourquoi le pas constant 0,001 est-il si lent au début ? Que garde le pas décroissant de chacun des deux ? Pourquoi garde-t-on le **meilleur** point vu, et pas le dernier ?""",
    todo='''def run_subgradient(X, y, C, steps, eta):
    """The list of the `steps` values J(w_t, b_t) of the subgradient descent that starts at w = 0, b = 0 and, for
    t = 1, ..., steps, computes (J, g_w, g_b) = svm_subgradient(w, b, X, y, C) (ref_30.svm_subgradient, or your
    own), stores J, then steps (w, b) <- (w, b) - eta(t) * (g_w, g_b)."""
    raise NotImplementedError("w = 0 et b = 0, puis à chaque t : svm_subgradient, range J, fais le pas η_t = eta(t)")


answer_M13b_30a = answer_M13b_30b = answer_M13b_30c = ...
with wbm.attempt("M13b.30a"):        # your run_subgradient is called here: ⏳ while it is not written
    runs_30 = {name: run_subgradient(X_30, Y_30, C_30, STEPS_30, eta) for name, eta in SCHEDULES_30.items()}
    answer_M13b_30a = ...  # a) a list of 3 numbers (6 decimals), in the order of SCHEDULES_30
    answer_M13b_30b = ...  # b) True or False
    answer_M13b_30c = ...  # c) an integer''',
    check='''for letter, answer in zip("abc", [answer_M13b_30a, answer_M13b_30b, answer_M13b_30c]):
    wbm.check(f"M13b.30{letter}", answer)

with checked("M13b.30 figure"):
''' + "\n".join("    " + line for line in FIGURE_30.splitlines()),
    solution='''def run_subgradient(X, y, C, steps, eta):
    """The list of the `steps` values J(w_t, b_t) of the subgradient descent that starts at w = 0, b = 0 and, for
    t = 1, ..., steps, computes (J, g_w, g_b) = svm_subgradient(w, b, X, y, C) (ref_30.svm_subgradient, or your
    own), stores J, then steps (w, b) <- (w, b) - eta(t) * (g_w, g_b)."""
    w, b, values = np.zeros(np.shape(X)[1]), 0.0, []
    for t in range(1, steps + 1):
        J, g_w, g_b = ref_30.svm_subgradient(w, b, X, y, C)
        values.append(J)
        w, b = w - eta(t) * g_w, b - eta(t) * g_b
    return values


runs_30 = {name: np.array(run_subgradient(X_30, Y_30, C_30, STEPS_30, eta)) for name, eta in SCHEDULES_30.items()}
gaps_30 = [float(run.min() - J_STAR_30) for run in runs_30.values()]
answer_M13b_30a = [round(g, 6) for g in gaps_30]
answer_M13b_30b = gaps_30[2] < min(gaps_30[:2])
answer_M13b_30c = int(np.sum(np.diff(runs_30["constant 0,01"]) > 0))
print("J* =", round(J_STAR_30, 6), " ; a)", answer_M13b_30a, " b)", answer_M13b_30b, " c)", answer_M13b_30c)
for name, run in runs_30.items():
    best = np.minimum.accumulate(run) - J_STAR_30
    print(f"{name:>20} : meilleur écart après 10, 50, 100, 300 itérations :",
          [f"{best[t - 1]:.1e}" for t in (10, 50, 100, 300)], " ; dernier écart :", f"{run[-1] - J_STAR_30:.1e}",
          " ; remontées :", int(np.sum(np.diff(run) > 0)))
''' + FIGURE_30,
    record='''from sklearn.svm import SVC as SVC_r

rng_30r = np.random.default_rng(4230)
y_30r = np.where(rng_30r.random(150) < 0.5, -1, 1)
x_30r = rng_30r.normal(0.0, 1.0, size=(150, 3)) + np.outer(y_30r, [0.9, -0.7, 0.5])


def j_30r(w, b):
    """J(w, b), computed directly."""
    return 0.5 * float(w @ w) + 0.5 * float(np.sum(np.maximum(0.0, 1.0 - y_30r * (x_30r @ w + b))))


def descent_30r(eta):
    """The 300 values J(w_t, b_t) of the descent, computed without svm_subgradient."""
    w, b, values = np.zeros(3), 0.0, []
    for t in range(1, 301):
        below = y_30r * (x_30r @ w + b) < 1
        values.append(j_30r(w, b))
        g_w, g_b = w - 0.5 * (y_30r[below] @ x_30r[below]), -0.5 * float(np.sum(y_30r[below]))
        w, b = w - eta(t) * g_w, b - eta(t) * g_b
    return np.array(values)


svc_30r = SVC_r(kernel="linear", C=0.5, tol=1e-10).fit(x_30r, y_30r)
star_30r = j_30r(svc_30r.coef_[0], float(svc_30r.intercept_[0]))
runs_30r = [descent_30r(eta) for eta in (lambda t: 0.01, lambda t: 0.001, lambda t: 0.01 / math.sqrt(t))]
best_30r = [float(run.min() - star_30r) for run in runs_30r]
wbm.record("M13b.30a", best_30r, decimals=6,
           mistakes={"le MEILLEUR écart, min_t J_t − J*, pas le dernier": [float(run[-1] - star_30r) for run in runs_30r],
                     "l'écart à J* : retranche J_STAR_30": [float(run.min()) for run in runs_30r]})
wbm.record("M13b.30b", best_30r[2] < min(best_30r[:2]),
           mistakes={"compare le meilleur écart du pas décroissant au plus petit des deux autres": False})
ups_30r = int(np.sum(np.diff(runs_30r[0]) > 0))
wbm.record("M13b.30c", ups_30r,
           mistakes={"compte les t où J remonte, J_(t+1) > J_t, pas ceux où il baisse": len(runs_30r[0]) - 1 - ups_30r})''',
    note=r"Meilleurs écarts après 300 itérations : $\approx 7{,}3 \times 10^{-4}$ (pas 0,01), $1{,}3 \times 10^{-4}$ "
         r"(pas 0,001) et $8{,}2 \times 10^{-5}$ (pas décroissant), pour $J^* \approx 21{,}68$. Le pas 0,01 descend "
         r"vite, puis oscille : son meilleur écart reste à $7{,}3 \times 10^{-4}$ dès la 200ᵉ itération, son dernier "
         r"écart vaut $\approx 0{,}033$, et $J$ remonte 129 fois sur 299 pas. Le pas 0,001 oscille moins, mais "
         r"démarre lentement (écart $\approx 1$ après 50 itérations). Le pas $0{,}01/\sqrt{t}$ fait les grands pas du "
         r"premier au début et des pas de plus en plus fins ensuite : il atteint $8{,}2 \times 10^{-5}$ dès la 200ᵉ "
         r"itération. Un pas de sous-gradient ne garantit pas la baisse (fiche §7) : on garde le meilleur point vu. "
         r"Sur un autre dataset, l'ordre des deux pas constants peut changer ; la théorie ne garantit la convergence "
         r"qu'au pas décroissant.",
)

GIVEN_31 = '''def f_31(x, y):
    """The objective (x − 3)² + 2(y + 1)²: its level lines are ellipses centred at (3, −1)."""
    return (x - 3) ** 2 + 2 * (y + 1) ** 2


def grad_f_31(x, y):
    """The gradient of f_31 at (x, y)."""
    return np.array([2 * (x - 3), 4 * (y + 1)], dtype=float)


def g_31(x, y):
    """The constraint g = 0: the parabola y = x²/2 − 2."""
    return x ** 2 / 2 - 2 - y


def grad_g_31(x, y):
    """The gradient of g_31 at (x, y)."""
    return np.array([x, -1.0], dtype=float)'''

CHECK_31 = '''with checked("M13b.31"):
    results_31 = []

    def report_31(ok, success, failure):
        results_31.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))

    fig, ax = plt.subplots(figsize=(6.5, 6.0))
    try:
        returned_31 = []
        opened_31 = drawn(lambda axis: returned_31.append(draw_lagrange(axis)), ax)
    except BaseException:
        plt.close(fig)
        raise
    report_31(not opened_31 and bool(ax.lines or ax.collections), "draw_lagrange dessine dans l'axe reçu",
              "draw_lagrange doit dessiner dans l'axe reçu, sans ouvrir de figure (ni plt.figure ni plt.subplots)")
    try:
        x_31, y_31 = (float(v) for v in returned_31[0])
        point_ok_31 = math.isfinite(x_31) and math.isfinite(y_31)
    except (TypeError, ValueError, IndexError):
        point_ok_31 = False
    if not point_ok_31:
        report_31(False, "", "draw_lagrange doit rendre le point trouvé, un couple de deux nombres (x, y)")
    else:
        gap_31 = abs(g_31(x_31, y_31))
        report_31(gap_31 <= 1e-3, f"le point ({fr(x_31, 4)} ; {fr(y_31, 4)}) est sur la contrainte",
                  f"le point ({fr(x_31, 4)} ; {fr(y_31, 4)}) n'est pas sur la parabole : |g| = {fr(gap_31, 4)} > 0,001")
        gf_31, gg_31 = grad_f_31(x_31, y_31), grad_g_31(x_31, y_31)
        sine_31 = abs(gf_31[0] * gg_31[1] - gf_31[1] * gg_31[0]) / (np.linalg.norm(gf_31) * np.linalg.norm(gg_31) or 1.0)
        report_31(sine_31 < 1e-2, f"∇f et ∇g sont colinéaires en ce point (sinus de leur angle : {sine_31:.1e})".replace(".", ","),
                  f"∇f et ∇g ne sont pas colinéaires en ce point : le sinus de leur angle vaut {fr(sine_31, 4)}, plus "
                  "que 0,01 ; cherche le minimum de f sur la courbe plus finement")
    plt.show()
    verdict("M13b.31", all(results_31), "le point de Lagrange est juste, et la figure est dans l'axe reçu.",
            "relis les lignes ❌ ci-dessus.")'''

M13B_31 = Ex(
    "M13b.31", "🎨", 1, 20, "Lignes de niveau et contrainte : voir le point de Lagrange",
    "trouver numériquement le minimum d'une fonction sur une courbe, et voir qu'en ce point la ligne de niveau touche "
    "la courbe et que les deux gradients sont colinéaires.", "fiche §1", tracks="C, E", given=GIVEN_31,
    body=r"""On minimise $f(x, y) = (x - 3)^2 + 2(y + 1)^2$, dont les lignes de niveau sont des ellipses centrées en $(3, -1)$, sous la contrainte $g(x, y) = \frac{x^2}{2} - 2 - y = 0$ : le point doit rester sur la parabole $y = \frac{x^2}{2} - 2$. La cellule fournie donne $f$, $g$ et leurs gradients. Écris `draw_lagrange(ax)`, qui, dans l'axe reçu (sans en ouvrir d'autre) :
- trouve le point de Lagrange **par ta propre méthode numérique** : par exemple, paramètre la parabole par $x$ (le point $(x, \frac{x^2}{2} - 2)$), calcule $f$ sur une grille fine de valeurs de $x$ (`np.linspace`, des dizaines de milliers de points) et garde la plus petite ;
- trace quelques lignes de niveau de $f$ (`ax.contour` sur une grille `np.meshgrid`), dont celle qui passe par ce point, la parabole, et le point ;
- dessine en ce point les deux gradients $\nabla f$ et $\nabla g$, ramenés à la même longueur (`ax.annotate` avec une flèche, ou `ax.quiver`) ;
- met `ax.set_aspect("equal")`, une légende et un titre ;
- **rend** le point trouvé, le couple `(x, y)`.

La cellule de vérification appelle ta fonction, contrôle que le point est sur la parabole (à $10^{-3}$ près) et que les deux gradients y sont colinéaires (le sinus de leur angle sous 0,01), puis affiche ta figure.

Dans ta copie : écris le système de Lagrange de ce problème, élimine $y$ et $\lambda$, et montre que $x$ vérifie $x^3 - x - 3 = 0$. Pourquoi cette équation n'a-t-elle qu'une racine réelle (regarde les variations de $x^3 - x - 3$), et que vaut $\lambda$ ? Sur ta figure, la ligne de niveau du point traverse-t-elle la parabole, ou la touche-t-elle ? Que se passerait-il en un point de la parabole où les gradients ne sont pas colinéaires ?""",
    todo='''def draw_lagrange(ax):
    """In the axes received (and no other): the level lines of f_31, the parabola g_31 = 0, the Lagrange point found
    numerically (the minimum of f_31 on the parabola), and the two gradients at that point. Return the point (x, y)."""
    raise NotImplementedError("une grille fine sur la parabole, le minimum de f, puis ax.contour, ax.plot, ax.annotate")''',
    check=CHECK_31,
    solution='''def draw_lagrange(ax):
    """In the axes received (and no other): the level lines of f_31, the parabola g_31 = 0, the Lagrange point found
    numerically (the minimum of f_31 on the parabola), and the two gradients at that point. Return the point (x, y)."""
    xs = np.linspace(-4.0, 4.0, 160001)               # the parabola, parametrized by x: a step of 5e-5
    best = int(np.argmin(f_31(xs, xs ** 2 / 2 - 2)))
    x_star = float(xs[best])
    y_star = x_star ** 2 / 2 - 2
    gx, gy = np.meshgrid(np.linspace(-3.0, 6.0, 300), np.linspace(-4.0, 5.0, 300))
    levels = sorted({0.5, 1.0, round(f_31(x_star, y_star), 4), 4.0, 8.0, 14.0, 22.0})
    ax.contour(gx, gy, f_31(gx, gy), levels=levels, cmap="viridis", linewidths=1)
    curve = np.linspace(-3.0, 3.6, 200)
    ax.plot(curve, curve ** 2 / 2 - 2, color="black", lw=1.5, label="contrainte y = x²/2 − 2")
    ax.plot(x_star, y_star, "o", color="C3", label="point de Lagrange")
    for grad, color, name in ((grad_f_31(x_star, y_star), "C3", "∇f"), (grad_g_31(x_star, y_star), "C0", "∇g")):
        u = grad / np.linalg.norm(grad)
        ax.annotate("", xy=(x_star + u[0], y_star + u[1]), xytext=(x_star, y_star),
                    arrowprops=dict(arrowstyle="->", color=color, lw=2))
        ax.text(x_star + 1.15 * u[0], y_star + 1.15 * u[1], name, color=color)
    ax.set_xlim(-3.0, 6.0)
    ax.set_ylim(-4.0, 5.0)
    ax.set_aspect("equal")
    ax.legend(loc="upper left", fontsize=8)
    ax.set_title("min (x − 3)² + 2(y + 1)² sur la parabole")
    return x_star, y_star


x_31, y_31 = draw_lagrange(plt.figure().add_subplot())
plt.close()
lam_31 = -grad_f_31(x_31, y_31)[0] / grad_g_31(x_31, y_31)[0]
print(f"point ({x_31:.4f} ; {y_31:.4f}), λ = {lam_31:.4f}, x³ − x − 3 = {x_31 ** 3 - x_31 - 3:.1e}".replace(".", ","))


''' + CHECK_31,
    note=r"La stationnarité $2(x - 3) + \lambda x = 0$, $4(y + 1) - \lambda = 0$, avec $y = \frac{x^2}{2} - 2$, donne "
         r"$\lambda = 4(y + 1) = 2x^2 - 4$ puis $2x - 6 + 2x^3 - 4x = 0$, soit $x^3 - x - 3 = 0$. Sa dérivée $3x^2 - 1$ "
         r"s'annule en $\pm\frac{1}{\sqrt{3}}$, où la fonction vaut $\approx -3{,}4$ et $\approx -2{,}6$, deux valeurs "
         r"négatives : une seule racine réelle, $x^* \approx 1{,}6717$, donc $y^* \approx -0{,}6027$ et $\lambda "
         r"\approx 1{,}589$. Sur la figure, l'ellipse $f = f^* \approx 2{,}08$ touche la parabole sans la traverser, et "
         r"les deux gradients sont portés par la même droite, de sens opposés ($\nabla f = -\lambda\nabla g$). En un "
         r"point où ils ne sont pas colinéaires, $\nabla f$ a une composante le long de la courbe : en glissant sur la "
         r"parabole dans le sens opposé, $f$ baisse, et le point n'est pas le minimum.",
)

PART_A = Part("A", "Ta librairie : Lagrange, hinge loss, sous-gradient et noyaux ; SciPy et scikit-learn",
              "Fiche §2, §7 et §8. Les cinq fonctions de `mymath/svm.py`, puis `scipy.optimize.minimize` et les "
              "noyaux et la hinge loss de scikit-learn.",
              given=TOOLS, exercises=[M13B_25, M13B_26, M13B_27, M13B_28])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §1, §4 et §7. Le prix d'une contrainte, le pas d'une descente de sous-gradient, et le point de "
              "Lagrange sur une figure.",
              exercises=[M13B_29, M13B_30, M13B_31])

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M13b.32 to M13b.34)
# ---------------------------------------------------------------------------
GIVEN_32 = '''X_32 = np.array([[1.5, -0.5], [0.0, 2.5], [-1.0, 1.0], [2.5, 1.5], [-2.0, -1.5], [0.5, 3.0]])   # 6 examples
Y_32 = np.array([1, -1, -1, 1, -1, 1])                                                    # their labels
Z_32 = np.array([[1.0, 0.5], [-0.5, 2.0], [3.0, -1.5], [0.0, -2.5]])                      # 4 new points
W_32, B_32, C_32, GAMMA_32 = np.array([1.2, -0.5]), 0.1, 2.0, 0.5
# A candidate for min (p₁ − 3)² + (p₂ − 0.5)² under g(p) = 2p₁ + p₂ − 7 ≤ 0: the point P_32 of the line g = 0, and
# the μ that makes the stationarity ∇f + μ∇g = 0 hold there
P_32 = np.array([3.2, 0.6])
GRAD_F_32, GRAD_G_32 = 2 * (P_32 - np.array([3.0, 0.5])), np.array([2.0, 1.0])
G_P_32 = float(P_32 @ GRAD_G_32 - 7)                                                     # g(P_32)
MU_32 = float(-(GRAD_F_32 @ GRAD_G_32) / (GRAD_G_32 @ GRAD_G_32))
STATIONARY_32 = bool(np.allclose(GRAD_F_32 + MU_32 * GRAD_G_32, 0.0))'''

MISTAKES_32 = bug_letters_mistakes(
    "BCFG", "ADE",
    {"B": "regarde comment C pèse les hinges dans l'objectif J",
     "C": "compare la largeur de la bande et la marge ρ",
     "F": "regarde la forme et la symétrie de la matrice que la ligne calcule",
     "G": "relis les quatre conditions KKT : sont-elles toutes testées ?"},
    name_correct=False)

M13B_32 = Ex(
    "M13b.32", "🐛", 1, 15, "Chasse à l'erreur : le signe d'un multiplicateur, une largeur de bande 1/‖w‖ au lieu de "
    "2/‖w‖, une matrice de Gram non symétrique",
    "repérer dans un résumé de SVM les erreurs classiques des multiplicateurs, de la marge et des noyaux, puis "
    "calculer les bonnes valeurs.", "fiche §3, §6 et §8", tracks="C", given=GIVEN_32,
    body=r"""Un collègue résume une SVM linéaire et une vérification de conditions KKT (la cellule fournie) : six exemples `X_32` et leurs labels, quatre autres points `Z_32`, un séparateur $(\mathbf{w}, b)$, le poids $C$ et un paramètre $\gamma$ ; puis un candidat `P_32` pour un petit problème à une contrainte d'inégalité, avec le multiplicateur `MU_32` qui y rend la stationnarité vraie. Sept lignes portent une lettre et un commentaire qui dit ce qu'elles doivent calculer. Quatre lignes ne font pas ce que dit leur commentaire. **Sans exécuter son code**, trouve-les.

```python
X, y, w, b = X_32, Y_32, W_32, B_32
margins = y * (X @ w + b)                                            # (A) the functional margins t_i
J = 0.5 * w @ w + C_32 * np.mean(np.maximum(0, 1 - margins))         # (B) the soft-margin objective J(w, b)
band = 1 / np.linalg.norm(w)                                         # (C) the width of the band
rho = 1 / np.linalg.norm(w)                                          # (D) the margin ρ, from the boundary to a border
K = np.exp(-GAMMA_32 * np.sum((X[:, None, :] - X[None, :, :]) ** 2, axis=2))   # (E) the RBF Gram matrix of X
G = X @ Z_32.T                                                       # (F) the linear Gram matrix of X, x_i · x_j
kkt = STATIONARY_32 and G_P_32 <= 1e-12 and abs(MU_32 * G_P_32) <= 1e-12   # (G) (P_32, MU_32) is a KKT point
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) la bonne valeur de `J` (4 décimales) ;
- c) la bonne valeur de `band` (4 décimales) ;
- d) la somme de tous les coefficients de la bonne matrice `G` (4 décimales) ;
- e) la bonne valeur de `kkt` (`True` ou `False`).

Pour b) à e), écris le code corrigé dans la cellule (c'est permis : seule la recherche des lignes fausses se fait sans exécuter).""",
    todo='''answer_M13b_32a = ...  # a) letters, as text
answer_M13b_32b = ...  # b) a number (4 decimals)
answer_M13b_32c = ...  # c) a number (4 decimals)
answer_M13b_32d = ...  # d) a number (4 decimals)
answer_M13b_32e = ...  # e) True or False''',
    check='''for letter, answer in zip("abcde", [answer_M13b_32a, answer_M13b_32b, answer_M13b_32c, answer_M13b_32d,
                                     answer_M13b_32e]):
    wbm.check(f"M13b.32{letter}", answer)''',
    after=[("md", "**Après la vérification**, dans ta copie : pour chaque ligne fausse, que calcule-t-elle exactement, "
                  "et comment la corriger ? Laquelle donne une matrice de la mauvaise forme, et laquelle un nombre "
                  "plausible sans aucun signal ? Pourquoi les lignes (C) et (D), presque identiques, ne sont-elles "
                  "pas toutes les deux fausses ? Pour (G), que dit le signe de `MU_32` sur la contrainte, et quel est "
                  "le vrai minimum de ce petit problème ?")],
    solution='''answer_M13b_32a = "BCFG"
margins_32 = Y_32 * (X_32 @ W_32 + B_32)                                    # (A) right
J_32 = 0.5 * W_32 @ W_32 + C_32 * np.sum(np.maximum(0, 1 - margins_32))    # (B) C times the SUM of the hinges
band_32 = 2 / np.linalg.norm(W_32)                                          # (C) the band is 2ρ wide
G_32 = X_32 @ X_32.T                                                        # (F) n × n, symmetric
kkt_32 = STATIONARY_32 and G_P_32 <= 1e-12 and abs(MU_32 * G_P_32) <= 1e-12 and MU_32 >= 0   # (G) the sign of μ too
answer_M13b_32b, answer_M13b_32c = round(float(J_32), 4), round(float(band_32), 4)
answer_M13b_32d, answer_M13b_32e = round(float(G_32.sum()), 4), bool(kkt_32)
print(answer_M13b_32a, answer_M13b_32b, answer_M13b_32c, answer_M13b_32d, answer_M13b_32e)
print("lignes du collègue : (B)", round(float(0.5 * W_32 @ W_32 + C_32 * np.mean(np.maximum(0, 1 - margins_32))), 4),
      " (C)", round(float(1 / np.linalg.norm(W_32)), 4), " (F) forme", (X_32 @ Z_32.T).shape,
      " (G)", STATIONARY_32 and G_P_32 <= 1e-12 and abs(MU_32 * G_P_32) <= 1e-12, " ; MU_32 =", round(MU_32, 4))
print("marges :", np.round(margins_32, 2).tolist(), " ; g au minimum libre (3 ; 0,5) :", float(np.array([3.0, 0.5]) @ GRAD_G_32 - 7))''',
    record=f'''wbm.record("M13b.32a", "BCFG",
           mistakes={MISTAKES_32})
x_32r, y_32r = np.array([[1.5, -0.5], [0.0, 2.5], [-1.0, 1.0], [2.5, 1.5], [-2.0, -1.5], [0.5, 3.0]]), \\
    np.array([1, -1, -1, 1, -1, 1])
z_32r, w_32r, b_32r, c_32r = np.array([[1.0, 0.5], [-0.5, 2.0], [3.0, -1.5], [0.0, -2.5]]), np.array([1.2, -0.5]), 0.1, 2.0
hinges_32r = np.maximum(0.0, 1.0 - y_32r * (x_32r @ w_32r + b_32r))
norm_32r = float(np.hypot(*w_32r))
wbm.record("M13b.32b", 0.5 * float(w_32r @ w_32r) + c_32r * float(hinges_32r.sum()), decimals=4,
           mistakes={{"{SUM}": 0.5 * float(w_32r @ w_32r) + c_32r * float(hinges_32r.mean())}})
wbm.record("M13b.32c", 2 / norm_32r, decimals=4,
           mistakes={{"la bande s'étend des deux côtés de la frontière : sa largeur est 2ρ = 2/‖w‖": 1 / norm_32r,
                     "la largeur de la bande est 2/‖w‖, avec la norme de w": 2 / float(w_32r @ w_32r)}})
wbm.record("M13b.32d", float(sum(float(xi @ xj) for xi in x_32r for xj in x_32r)), decimals=4,
           mistakes={{"la matrice de Gram des exemples est X Xᵀ, de taille n × n : la somme de ses coefficients":
                         float((x_32r @ z_32r.T).sum())}})
wbm.record("M13b.32e", False,
           mistakes={{"un multiplicateur d'inégalité doit être positif ou nul : regarde le signe de MU_32": True}})''',
    note=r"(B) $C$ multiplie la **somme** des hinges : la moyenne divise le terme d'attache aux données par $n = 6$ "
         r"(le collègue trouve $\approx 1{,}4450$ au lieu de $4{,}4450$), un nombre plausible sans aucun signal. (C) "
         r"La bande a une largeur $2\rho = 2/\lVert\mathbf{w}\rVert = 2/1{,}3 \approx 1{,}5385$ ; (D), presque la "
         r"même ligne, calcule la marge $\rho$ : elle est juste. (F) `X @ Z_32.T` est la matrice $6 \times 4$ des "
         r"produits scalaires des exemples avec d'autres points ; la matrice de Gram des exemples est $\mathbf{X}"
         r"\mathbf{X}^\top$, $6 \times 6$ et symétrique, dont la somme des coefficients vaut $\lVert\sum_i "
         r"\mathbf{x}_i\rVert^2 = 1{,}5^2 + 6^2 = 38{,}25$. (E) élève bien les distances au carré : elle est juste. (G) "
         r"oublie la condition de signe : `MU_32` $= -0{,}2 < 0$ dit que la contrainte supposée active ne devrait pas "
         r"l'être. Le minimum libre $(3 ;\ 0{,}5)$ vérifie $g = -0{,}5 < 0$ : c'est la solution, avec $\mu = 0$ (fiche §3).",
)

GIVEN_33 = '''def grad_f_33(x):
    """The gradient of f(x) = (x₁ − 1)² + 3(x₂ − 4)²."""
    return np.array([2 * (x[0] - 1), 6 * (x[1] - 4)], dtype=float)


CONSTRAINTS_33 = [                                                       # (g_i, its gradient): g_i(x) ≤ 0
    (lambda x: -x[0] + 3 * x[1] - 3, lambda x: np.array([-1.0, 3.0])),   # g₁(x) = −x₁ + 3x₂ − 3
    (lambda x: x[0] - x[1] - 5, lambda x: np.array([1.0, -1.0])),        # g₂(x) = x₁ − x₂ − 5
]'''

CHECK_33 = '''with checked("M13b.33"):
    KEYS_33 = ("feasibility", "stationarity", "sign", "complementarity")
    CASES_33 = [("un point KKT", [3.0, 2.0], [4.0, 0.0]),
                ("le minimum libre, hors de l'ensemble admissible", [1.0, 4.0], [0.0, 0.0]),
                ("un multiplicateur négatif", [7.0, 2.0], [0.0, -12.0]),
                ("une complémentarité violée", [3.5, 1.5], [5.0, 0.0]),
                ("un gradient du lagrangien non nul", [3.0, 2.0], [2.0, 0.0])]

    def expected_33(x, mu):
        """The four conditions at (x, μ), computed directly."""
        x, mu = np.asarray(x, dtype=float), np.asarray(mu, dtype=float)
        g = np.array([g_i(x) for g_i, _ in CONSTRAINTS_33], dtype=float)
        rest = grad_f_33(x) + sum(m * dg(x) for m, (_, dg) in zip(mu, CONSTRAINTS_33))
        return {"feasibility": bool(np.all(g <= 1e-8)), "stationarity": bool(np.max(np.abs(rest)) <= 1e-8),
                "sign": bool(np.all(mu >= -1e-8)), "complementarity": bool(np.all(np.abs(mu * g) <= 1e-8))}

    right_33 = 0
    for name_33, x_33, mu_33 in CASES_33:
        want_33 = expected_33(x_33, mu_33)
        got_33 = check_kkt(grad_f_33, CONSTRAINTS_33, np.array(x_33), np.array(mu_33))
        if not isinstance(got_33, dict) or set(got_33) != set(KEYS_33):
            print(f"❌ {name_33} : check_kkt doit rendre un dictionnaire de clés {', '.join(KEYS_33)}, "
                  f"reçu {str(got_33)[:120]}")
            continue
        if not all(isinstance(got_33[k], (bool, np.bool_)) for k in KEYS_33):
            print(f"❌ {name_33} : chaque valeur du dictionnaire doit être True ou False")
            continue
        wrong_33 = [k for k in KEYS_33 if bool(got_33[k]) != want_33[k]]
        shown_33 = ", ".join(f"{k} {want_33[k]}" for k in KEYS_33)
        if wrong_33:
            print(f"❌ {name_33} (x = {x_33}, μ = {mu_33}) : " + " ; ".join(
                f"{k} attendu {want_33[k]}, reçu {bool(got_33[k])}" for k in wrong_33))
        else:
            right_33 += 1
            print(f"✅ {name_33} : {shown_33}")
    verdict("M13b.33", right_33 == len(CASES_33),
            "check_kkt reconnaît le point KKT et les quatre façons d'en manquer un.",
            f"{len(CASES_33) - right_33} cas faux sur {len(CASES_33)} : relis les lignes ❌ ci-dessus.")'''

M13B_33 = Ex(
    "M13b.33", "🛠️", 1, 15, "Vérifier une solution KKT : faisabilité, stationnarité, complémentarité",
    "écrire une fonction qui vérifie les quatre conditions KKT d'une solution candidate, pour n'importe quel "
    "problème à contraintes d'inégalité.", "fiche §3", tracks="C", given=GIVEN_33,
    body=r"""Un solveur, un collègue ou toi-même proposez une solution $(\mathbf{x}, \boldsymbol{\mu})$ d'un problème $\min f(\mathbf{x})$ sous $g_i(\mathbf{x}) \le 0$ : avant de la croire, on la **vérifie** (le réflexe de la fiche). Écris `check_kkt(grad_f, constraints, x, mu, tol=1e-8)`, pour un problème quelconque : `grad_f` est une fonction qui rend $\nabla f(\mathbf{x})$, `constraints` une liste de couples `(g_i, grad_g_i)` de fonctions, `x` le point et `mu` les multiplicateurs, un par contrainte. Elle rend le dictionnaire des quatre conditions de la fiche §3, chacune `True` ou `False` :
- `"feasibility"` : chaque $g_i(\mathbf{x}) \le$ `tol` ;
- `"stationarity"` : chaque coordonnée de $\nabla f(\mathbf{x}) + \sum_i \mu_i\nabla g_i(\mathbf{x})$ est, en valeur absolue, au plus `tol` ;
- `"sign"` : chaque $\mu_i \ge -$`tol` ;
- `"complementarity"` : chaque $\lvert\mu_i\,g_i(\mathbf{x})\rvert \le$ `tol`.

La cellule fournie définit un problème : $f(\mathbf{x}) = (x_1 - 1)^2 + 3(x_2 - 4)^2$, sous $g_1(\mathbf{x}) = -x_1 + 3x_2 - 3 \le 0$ et $g_2(\mathbf{x}) = x_1 - x_2 - 5 \le 0$. La cellule de vérification essaie ta fonction sur cinq candidats : un point KKT, un point hors de l'ensemble admissible, un multiplicateur négatif, une complémentarité violée et un gradient du lagrangien non nul, et dit ✅ ou ❌ pour chacun.

Dans ta copie : vérifie à la main le premier candidat, $\mathbf{x} = (3, 2)$ et $\boldsymbol{\mu} = (4, 0)$. Pourquoi ce point est-il **le** minimum, et pas seulement un point KKT (fiche §5) ? Le troisième candidat, $(7, 2)$ avec $\boldsymbol{\mu} = (0, -12)$, vérifie trois conditions sur quatre : que dit son multiplicateur négatif ? Pourquoi faut-il une tolérance, et que se passerait-il avec `tol=0` pour un point calculé en flottants ?""",
    todo='''def check_kkt(grad_f, constraints, x, mu, tol=1e-8):
    """The four KKT conditions at (x, mu) for min f(x) under g_i(x) <= 0: a dict {"feasibility", "stationarity",
    "sign", "complementarity"} of booleans; constraints is a list of pairs (g_i, grad_g_i), one per multiplier."""
    raise NotImplementedError("les valeurs g_i(x), le résidu ∇f + Σ μ_i ∇g_i, puis les quatre tests à tol près")''',
    check=CHECK_33,
    solution='''def check_kkt(grad_f, constraints, x, mu, tol=1e-8):
    """The four KKT conditions at (x, mu) for min f(x) under g_i(x) <= 0: a dict {"feasibility", "stationarity",
    "sign", "complementarity"} of booleans; constraints is a list of pairs (g_i, grad_g_i), one per multiplier."""
    x, mu = np.asarray(x, dtype=float), np.asarray(mu, dtype=float)
    g = np.array([float(g_i(x)) for g_i, _ in constraints])
    rest = np.asarray(grad_f(x), dtype=float) + sum(m * np.asarray(dg(x), dtype=float)
                                                    for m, (_, dg) in zip(mu, constraints))
    return {"feasibility": bool(np.all(g <= tol)), "stationarity": bool(np.max(np.abs(rest)) <= tol),
            "sign": bool(np.all(mu >= -tol)), "complementarity": bool(np.all(np.abs(mu * g) <= tol))}


print("g(3, 2) =", [g_i(np.array([3.0, 2.0])) for g_i, _ in CONSTRAINTS_33], " ; ∇f(3, 2) =",
      grad_f_33(np.array([3.0, 2.0])).tolist())


''' + CHECK_33,
    note=r"En $(3, 2)$ : $g_1 = -3 + 6 - 3 = 0$ (active), $g_2 = -4 < 0$ (inactive, donc $\mu_2 = 0$) ; $\nabla f = "
         r"(4, -12)$ et $\mu_1\nabla g_1 = 4\,(-1, 3) = (-4, 12)$ : la stationnarité tient, $\mu_1 = 4 \ge 0$, et la "
         r"complémentarité aussi. Le problème est convexe ($f$ convexe, contraintes affines) : les conditions KKT y "
         r"suffisent, $(3, 2)$ est le minimum global (fiche §5). Le troisième candidat est le point de la droite "
         r"$g_2 = 0$ le plus favorable, où la stationnarité demande $\mu_2 = -12$ : le signe négatif dit que $f$ "
         r"baisserait en quittant cette droite vers l'intérieur, donc que $g_2$ ne devrait pas être active. En "
         r"flottants, $g_1(\mathbf{x})$ calculé au vrai point vaut souvent $\pm 10^{-16}$ au lieu de 0 : avec `tol=0`, "
         r"une solution juste serait déclarée non admissible ou non complémentaire.",
)

GIVEN_34 = '''def svm_dataset(seed, n, offset, shift, spread):
    """n examples of len(offset) features, far from the origin (around offset), of two classes ±1 that overlap."""
    rng = np.random.default_rng(seed)
    y = np.where(rng.random(n) < 0.5, -1, 1)
    X = np.asarray(offset) + rng.normal(0.0, 1.0, size=(n, len(offset))) * np.asarray(spread) + np.outer(y, shift)
    return X, y


X_34, Y_34 = svm_dataset(4234, 400, [12.0, -8.0, 6.0, 15.0, -10.0], [0.6, -0.4, 0.5, 0.3, -0.5],
                         [1.0, 1.5, 0.8, 1.2, 1.0])     # 400 examples, p = 5 features
C_34, MAX_CALLS_34, MAX_SECONDS_34 = 0.5, 20000, 30.0
ref_34 = wbm.load_mymath("ref", alias="mymath_ref").svm'''

CHECK_34 = '''with checked("M13b.34 défi"):
    from sklearn.svm import SVC                      # the reference objective J* (forbidden in train_linear_svm)

    problems_34, ok_34, ran_34 = [], False, False
    try:
        source_34 = inspect.getsource(train_linear_svm)
    except (OSError, TypeError):
        source_34 = ""
    try:                                             # the code only: comments and strings (docstrings) may name anything
        source_34 = " ".join(tok.string for tok in tokenize.generate_tokens(io.StringIO(source_34).readline)
                             if tok.type not in (tokenize.COMMENT, tokenize.STRING))
    except (tokenize.TokenError, SyntaxError):
        pass
    banned_34 = sorted(set(re.findall(r"\\b(scipy|optimize|minimize|sklearn|SVC|LinearSVC|SGDClassifier|mymath|"
                                      r"mymath_ref|ref_34|svm_subgradient|X_34|Y_34|svm_dataset)\\b", source_34)))
    if banned_34:
        ran_34 = True
        problems_34.append(f"train_linear_svm utilise {', '.join(banned_34)}, interdit dans ce défi")
    cases_34 = [("le dataset X_34 (n = 400, p = 5)", X_34, Y_34),
                ("un second dataset (n = 300, p = 3)",
                 *svm_dataset(4233, 300, [-10.0, 14.0, 9.0], [0.7, 0.5, -0.6], [1.0, 1.3, 0.9]))]
    for name_t, X_t, y_t in ([] if banned_34 else cases_34):
        svc_t = SVC(kernel="linear", C=C_34, tol=1e-10).fit(X_t, y_t)
        star_t = ref_34.svm_subgradient(svc_t.coef_[0], float(svc_t.intercept_[0]), X_t, y_t, C_34)[0]
        calls_t = [0]

        def counted(w, b, X, y, C=1.0, calls=calls_t):
            calls[0] += 1
            return ref_34.svm_subgradient(w, b, X, y, C)

        start_t = time.perf_counter()
        try:
            result_t = train_linear_svm(X_t.copy(), y_t.copy(), C_34, counted)
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            ran_34 = True
            problems_34.append(f"train_linear_svm lève {type(exc).__name__} ({exc})")
            break
        seconds_t = time.perf_counter() - start_t
        ran_34 = True
        try:
            w_t, b_t = result_t
            w_t, b_t = np.asarray(w_t, dtype=float).reshape(-1), float(b_t)
            j_t = ref_34.svm_subgradient(w_t, b_t, X_t, y_t, C_34)[0]
        except (TypeError, ValueError):
            problems_34.append("train_linear_svm doit rendre le couple (w, b) : w, un tableau de p nombres ; b, un "
                               "nombre")
            break
        ratio_t = j_t / star_t
        print(f"{name_t} : J = {j_t:.4f} pour J* = {star_t:.4f} (J/J* = {ratio_t:.5f}), {calls_t[0]} appels de "
              f"svm_subgradient, {seconds_t:.1f} s".replace(".", ","))
        if calls_t[0] > MAX_CALLS_34:
            problems_34.append(f"{name_t} : {calls_t[0]} appels, au-dessus du budget de {MAX_CALLS_34}")
        if seconds_t > MAX_SECONDS_34:
            problems_34.append(f"{name_t} : {seconds_t:.0f} s, au-dessus des {MAX_SECONDS_34:.0f} s permises")
        if not ratio_t <= 1.01:
            problems_34.append(f"{name_t} : ton objectif est {100 * (ratio_t - 1):.2f} % au-dessus de J*, plus que "
                               f"1 %".replace(".", ","))
        if problems_34:
            break
    if problems_34:
        print("❌ Ex M13b.34 : " + " ; ".join(problems_34) + ".")
    elif ran_34:
        ok_34 = True
        print("✅ Ex M13b.34 : défi réussi : un objectif à moins de 1 % de celui de scikit-learn, sur les deux datasets, "
              "dans le budget d'appels et de temps.")'''

M13B_34 = Ex(
    "M13b.34", "🏆", 3, 30, "Défi : une SVM linéaire entraînée par sous-gradient, un objectif à 1 % de celui de "
    "scikit-learn au même C",
    "entraîner une SVM linéaire par descente de sous-gradient jusqu'à un objectif chiffré, en choisissant le pas, le "
    "point gardé et un changement de variable qui rend la descente facile.", "fiche §7 ; Ex M13b.30", tracks="C",
    given=GIVEN_34,
    body=r"""Les 400 exemples `X_34` (cellule fournie) ont 5 features, de deux classes qui se chevauchent, et ils sont **loin de l'origine** (autour de $(12, -8, 6, 15, -10)$). Avec $C = 0{,}5$, la SVM de scikit-learn, `SVC(kernel="linear", C=0.5, tol=1e-10)`, atteint l'objectif $J^*$, le minimum de $J(\mathbf{w}, b) = \frac{1}{2}\lVert\mathbf{w}\rVert^2 + C\sum_i \max(0, 1 - y_i(\mathbf{w} \cdot \mathbf{x}_i + b))$.

**L'objectif** : écrire `train_linear_svm(X, y, C, subgradient)`, qui rend un couple $(\mathbf{w}, b)$ dont l'objectif $J$ est à **moins de 1 %** au-dessus de $J^*$, par descente de sous-gradient. La fonction reçue `subgradient(w, b, X, y, C)` est `svm_subgradient` (elle rend $(J, \mathbf{g}_{\mathbf{w}}, g_b)$) : ta fonction ne doit utiliser qu'elle, **au plus 20 000 fois** et en au plus 30 secondes. La vérification compte les appels, mesure le temps, et essaie ta fonction sur `X_34`, puis sur un second dataset de 300 exemples et 3 features, lui aussi loin de l'origine. scikit-learn, `scipy` (`scipy.optimize` compris), `mymath`, `svm_subgradient` appelée directement, `X_34` et `svm_dataset` sont interdits dans ta fonction.

Une descente naïve, à pas constant, échoue : essaie-la d'abord, pour voir, et cherche pourquoi (regarde $g_b$ et les coordonnées de $\mathbf{g}_{\mathbf{w}}$ quand $\lvert b \rvert$ doit être grand, une vingtaine ici). Les indices de `04_indices.md` donnent des pistes, à ouvrir une à une.

Une dernière cellule enregistre si l'objectif est atteint.

Dans ta copie : pourquoi les exemples loin de l'origine rendent-ils la descente si difficile ? Qu'as-tu changé pour réussir, et pourquoi ce changement ne modifie-t-il pas le problème (ni $J$, ni $\lVert\mathbf{w}\rVert$), alors qu'une **mise à l'échelle** des features le modifierait ? Combien d'appels ta méthode a-t-elle utilisés ?""",
    todo='''def train_linear_svm(X, y, C, subgradient):
    """(w, b) whose objective J is less than 1 % above its minimum, by subgradient descent, calling
    subgradient(w, b, X, y, C) -> (J, g_w, g_b) at most MAX_CALLS_34 times."""
    raise NotImplementedError("une descente de sous-gradient à 1 % de J*, au plus 20 000 appels (04_indices.md si tu bloques)")''',
    check=CHECK_34 + '''
with checked("M13b.34"):
    if not ran_34:                               # ⏳ while train_linear_svm is not written
        raise NotImplementedError("train_linear_svm n'est pas encore écrite")
    wbm.check("M13b.34", bool(ok_34), computed=True)''',
    solution='''from sklearn.svm import SVC


def train_linear_svm(X, y, C, subgradient):
    """(w, b) whose objective J is less than 1 % above its minimum, by subgradient descent, calling
    subgradient(w, b, X, y, C) -> (J, g_w, g_b) at most MAX_CALLS_34 times."""
    X = np.asarray(X, dtype=float)
    mean = X.mean(axis=0)                        # w · x + b = w · (x − m) + (b + w · m): J does not change
    centred = X - mean
    w, b = np.zeros(X.shape[1]), 0.0
    best = (math.inf, w, b)
    for t in range(1, 3001):
        J, g_w, g_b = subgradient(w, b, centred, y, C)
        if J < best[0]:                          # a subgradient step may raise J: keep the best point seen
            best = (J, w.copy(), b)
        eta = 0.01 / math.sqrt(t)
        w, b = w - eta * g_w, b - eta * g_b
    _, w, b = best
    return w, b - float(w @ mean)                # back to the bias of the original examples


def naive_34(X, y, C, eta=1e-4, steps=20000):
    """A constant step on the original examples, the last point: what fails."""
    w, b = np.zeros(X.shape[1]), 0.0
    for _ in range(steps):
        _, g_w, g_b = ref_34.svm_subgradient(w, b, X, y, C)
        w, b = w - eta * g_w, b - eta * g_b
    return w, b


svc_34 = SVC(kernel="linear", C=C_34, tol=1e-10).fit(X_34, Y_34)
star_34 = ref_34.svm_subgradient(svc_34.coef_[0], float(svc_34.intercept_[0]), X_34, Y_34, C_34)[0]
for eta in (1e-3, 1e-4):
    w_n, b_n = naive_34(X_34, Y_34, C_34, eta)
    print(f"pas constant {eta}, 20 000 pas : J/J* = {ref_34.svm_subgradient(w_n, b_n, X_34, Y_34, C_34)[0] / star_34:.3f}"
          .replace(".", ","))
w_34, b_34 = train_linear_svm(X_34, Y_34, C_34, ref_34.svm_subgradient)
print(f"exemples centrés, pas 0,01/√t, 3 000 pas : J/J* = "
      f"{ref_34.svm_subgradient(w_34, b_34, X_34, Y_34, C_34)[0] / star_34:.6f}, b = {b_34:.3f}".replace(".", ","))''',
    after=[("solution", CHECK_34)],
    record='''wbm.record("M13b.34", True,
           mistakes={"l'objectif n'est pas atteint : la cellule du défi dit pourquoi": False})''',
    note=r"Sur les exemples d'origine, le biais doit valoir environ $-23{,}5$, et chaque coordonnée de "
         r"$\mathbf{g}_{\mathbf{w}}$ est dominée par la moyenne des features, de l'ordre de 10 : un pas assez petit "
         r"pour ne pas faire exploser $\mathbf{w}$ fait bouger $b$ d'un rien, et le pas constant reste coincé "
         r"($J/J^* \approx 2{,}7$ avec $\eta = 10^{-4}$ après 20 000 pas, $\approx 17$ avec $10^{-3}$). Centrer les "
         r"exemples découple $b$ de $\mathbf{w}$ : $J$ ne change pas (même $\mathbf{w}$, même score pour chaque "
         r"exemple), et 3 000 pas $0{,}01/\sqrt{t}$, en gardant le meilleur point, donnent $J/J^* < 1{,}0001$ sur les "
         r"deux datasets, en moins d'une seconde. Diviser une feature par son écart-type, au contraire, change "
         r"$\lVert\mathbf{w}\rVert$ et donc le problème : on ne trouverait plus le même minimum. Les solveurs de "
         r"scikit-learn travaillent sur le dual (`SVC`) ou par coordonnées (`LinearSVC`), et la plupart des modèles "
         r"linéaires recommandent de centrer les features pour la même raison.",
)

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §3, §6, §7 et §8. Quatre erreurs à trouver dans un résumé de SVM, une fonction qui vérifie les "
              "conditions KKT, puis une SVM linéaire entraînée par sous-gradient jusqu'à un objectif chiffré.",
              exercises=[M13B_32, M13B_33, M13B_34])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M13b.1 à M13b.13, M13b.20 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            rows.append(ex.table_row(part.key if i == 0 else ""))
    if kind == "exercise":
        title = "# M13b · Optimisation sous contraintes et SVM — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m13b_lagrange_svm/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M13b`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M13b · Optimisation sous contraintes et SVM — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : Lagrange sous une et deux contraintes d'égalité, la "
               "distance à un plan, l'ACP relue par Lagrange, les conditions KKT, une fonction duale, la convexité, "
               "une SVM à marge dure, la hinge loss et le sous-gradient, le dual d'une SVM, les noyaux polynomial et "
               "RBF, la décision d'une SVM à noyau.\n"
               "- Écrire les cinq fonctions de `mymath/svm.py` et les tester, puis comparer avec SciPy et "
               "scikit-learn.\n"
               "- Prédire le prix d'une contrainte, comparer des pas de sous-gradient, voir le point de Lagrange, "
               "chasser des erreurs de SVM, vérifier une solution KKT, relever un défi d'entraînement.\n\n"
               r"**Rappel express.** Lagrange : $\nabla f + \lambda\nabla g = \mathbf{0}$ et $g = 0$, et $\frac{df^*}{dc} "
               r"= -\lambda$ pour $f + \lambda(g - c)$ ; problème quadratique : $\begin{pmatrix} \mathbf{Q} & "
               r"\mathbf{A}^\top \\ \mathbf{A} & \mathbf{0} \end{pmatrix}\begin{pmatrix} \mathbf{x} \\ "
               r"\boldsymbol{\lambda} \end{pmatrix} = \begin{pmatrix} -\mathbf{c} \\ \mathbf{b} \end{pmatrix}$ ; KKT "
               r"($g_i \le 0$) : stationnarité, faisabilité, $\mu_i \ge 0$, $\mu_i g_i = 0$ ; dual $D(\boldsymbol{\mu}) = "
               r"\min_{\mathbf{x}} \mathcal{L} \le f^*$ ; SVM : $\min \frac{1}{2}\lVert\mathbf{w}\rVert^2$ sous $y_i(\mathbf{w} "
               r"\cdot \mathbf{x}_i + b) \ge 1$, marge $\rho = 1/\lVert\mathbf{w}\rVert$, bande $2\rho$ ; $J = "
               r"\frac{1}{2}\lVert\mathbf{w}\rVert^2 + C\sum_i \max(0, 1 - t_i)$, $\mathbf{g}_{\mathbf{w}} = \mathbf{w} - "
               r"C\sum_{t_i < 1} y_i\mathbf{x}_i$, $g_b = -C\sum_{t_i < 1} y_i$ ; dual : $\mathbf{w} = \sum_i \alpha_i y_i "
               r"\mathbf{x}_i$, $0 \le \alpha_i \le C$ ; noyaux $(\mathbf{x} \cdot \mathbf{z} + c)^d$ et "
               r"$e^{-\gamma\lVert\mathbf{x} - \mathbf{z}\rVert^2}$, décision $s(\mathbf{x}) = \sum_i \alpha_i y_i\,"
               r"k(\mathbf{x}_i, \mathbf{x}) + b$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu résoudre un problème sous contraintes d'égalité par Lagrange, et lire un multiplicateur "
               "comme un prix ?\n"
               "2. Sais-tu écrire et vérifier les conditions KKT, et dire quelles contraintes sont actives ?\n"
               "3. Sais-tu reconnaître un problème convexe, et dire ce que cela garantit ?\n"
               "4. Sais-tu écrire le problème d'une SVM, calculer sa hinge loss et un sous-gradient, et choisir un "
               "pas de descente ?\n"
               "5. Sais-tu lire le dual d'une SVM et calculer avec les noyaux polynomial et RBF ?\n\n"
               "**La suite** : le chapitre 13 de workbookIA (classifieurs, dont les SVM linéaires et à noyau), puis "
               "M14, les maths des ensembles de modèles.")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter=CHAPTER) if kind == "exercise" else setup_cell(kind))
    cells += objectives_cell()
    cells += paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO,
                         learner_context="from fractions import Fraction   # Fraction(2, 9) is accepted too, as \"2/9\"")
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
