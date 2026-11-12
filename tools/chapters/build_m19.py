#!/usr/bin/env python
"""Build the two notebooks of chapter M19 from a single source (used by Claude).

    python tools/chapters/build_m19.py
    python tools/run_all_notebooks.py chapitres/m19_hessienne_convergence/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m19_hessienne_convergence/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M19.1 to M19.9, 🔗 M19.14 and M19.15); parts A to C are the notebook exercises
(M19.19 to M19.28). Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it.
The data are new: written in the statements, or synthetic with the seeds 5231 to 5239 only (never 19xx); none is a test
case of tests/test_m19_iterative.py nor the data of a paper exercise. Examples of the fiche come back on purpose: the
two springs (§4) in M19.20, read on the iterates from 0 at the fiche's step ω = 0.32 (just below the critical step:
the limit factor 0.92 of λmax, after a start dominated by λmin) and at the best step 2/7 (42 iterations); the stiff
and the soft spring (§5), whose critical step is computed before and after the diagonal scaling; the complex
recurrence u_{k+2} = 0.8 u_{k+1} − 0.64 u_k (§6) in M19.21, compared with 0.8^k cos(kπ/3); the bar of §3 (made finer:
50 inner points, ends at 10 °C and 70 °C) in M19.22 and M19.24; and the three recurrences of §6 in the colleague's
check of M19.26. Nothing of workbookIA 19 is used (the notes of M19 in the syllabus): no optimiser, no learning rate,
no schedule, no momentum (the leapfrog scheme of M19.28 is a recurrence of mechanics, never a method of optimisation;
nothing on hΩ = 0), no parabola, valley, Rosenbrock function nor saddle of its list, none of its formulas, numbers or
seeds; no step ω with ωλmax = 1.8, no step 0.1 nor 0.125. The prediction of M19.23 is about a 4 × 4 matrix and a
formula: which of four steps, given as numbers, does not converge (a letter), and ⌈6 ln 10 / (−ln ρ(ω))⌉ for the three
others (integers), never ranges of steps on a valley; M19.23 and M19.25 take 0.4 ω_c, not 1/λmax, and no question
is about a stiff component that vanishes in one step (18.3 d, ∂ 19.7.2 of workbookIA). M19.27 updates the residual by its own
recurrence r_{k+1} = (I − ωA) r_k and bounds it by ρ^k ‖b‖, without the lesson « test before or after the step » of
workbookIA 5.18. The inertia of M19.26 (n_neg, n_zero, n_pos, a relative tolerance) is not the four-outcome rule of
classify_critical_point (workbookIA 5). The count of evaluations of f in numerical_hessian is never asked: the tests
allow 2n² + n, the fiche says 2n² + 1 at best.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, check_unique_keys, guarded,  # noqa: E402,F401
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M19"
FOLDER = "chapitres/m19_hessienne_convergence"

MATRIX = "a matrix (list of rows)"
LETTER = '"A", "B", "C" or "D"'


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M19.1", "La hessienne d'une fonction de trois variables, et son développement de Taylor d'ordre 2", [
        ("a", "a list of 3 numbers", "flat(GRAD_1)",
         '''mistakes={"∂(e^(x − y))/∂y = −e^(x − y) : la dérivée par rapport à y amène un signe moins":
                         flat(GRAD_1 + sympy.Matrix([0, 2, 0]))}'''),
        ("b", MATRIX, "rows(HESS_1)",
         '''mistakes={"∂²(e^(x − y))/∂x∂y = −e^(x − y) : la dérivée par rapport à y amène un signe moins":
                         rows(HESS_1 + sympy.Matrix([[0, 2, 0], [2, 0, 0], [0, 0, 0]]))}'''),
        ("c", "a number", "float(TAYLOR1_1)",
         '''decimals=6, mistakes={"Taylor d'ordre 1 part de f(p) : f(p) + ∇f(p)ᵀh": float(TAYLOR1_1 - F_1.subs(P_1))}'''),
        ("d", "a number", "float(TAYLOR2_1)",
         '''decimals=6, mistakes={"le terme d'ordre 2 est ½ hᵀHh : n'oublie pas le ½": float(2 * TAYLOR2_1 - TAYLOR1_1)}'''),
        ("e", "a number (3 decimals)", "float(TRUE_1)",
         '''decimals=3, mistakes={"la vraie valeur de f, pas une approximation de Taylor : calcule f(1,1 ; 0,8 ; 2,1)":
                         float(TAYLOR2_1)}'''),
        ("f", "a number", "int(CURVATURE_1)",
         '''mistakes={"u est unitaire, u = (2, −1, 2)/3 : la courbure est uᵀHu, le facteur 1/9 compris":
                         int(9 * CURVATURE_1)}'''),
        ("g", "a number", "int(HESS_1[:2, :2].det())",
         '''mistakes={"le déterminant d'un bloc 2 × 2 est ad − bc, avec ici b = c = −4":
                         int(HESS_1[0, 0] * HESS_1[1, 1] + HESS_1[0, 1] ** 2)}'''),
        ("h", "True or False", "bool(np.all(np.linalg.eigvalsh(np.array(HESS_1, dtype=float)) > 0))",
         '''mistakes={"un mineur principal négatif suffit à exclure « définie positive » (critère de Sylvester, "
                     "M12c §7) : une diagonale positive ne suffit pas": True}'''),
    ]),

    Paper("M19.2", "Classer les points critiques d'une fonction de trois variables", [
        ("a", "an integer", "len(CRIT_2)",
         '''mistakes={"x et y peuvent aussi être tous deux négatifs : (x + y)² = 9 donne deux valeurs de x + y":
                         len(CRIT_2) // 2}'''),
        ("b", "a list of 4 lists of 3 numbers, by increasing x", "CRIT_2",
         '''mistakes={"rangés par x CROISSANT : le plus petit x d'abord": CRIT_2[::-1]}'''),
        ("c", "a list of 3 numbers, in increasing order", "EIGEN_2[(2, 1, 1)]",
         '''mistakes={"en ordre croissant": EIGEN_2[(2, 1, 1)][::-1]}'''),
        ("d", "a list of 3 numbers, in increasing order", "EIGEN_2[(-2, -1, 1)]",
         '''mistakes={"en ordre croissant : la plus négative d'abord": EIGEN_2[(-2, -1, 1)][::-1]}'''),
        ("e", "a list of 4 integers", "[sum(v < 0 for v in EIGEN_2[tuple(p)]) for p in CRIT_2]",
         '''mistakes={"compte les valeurs propres NÉGATIVES": [sum(v > 0 for v in EIGEN_2[tuple(p)]) for p in CRIT_2]}'''),
        ("f", "a number", "int(F_2.subs(dict(zip(V_1, (2, 1, 1)))))",
         '''mistakes={"le minimum local est le point critique dont les trois valeurs propres sont POSITIVES":
                         {int(F_2.subs(dict(zip(V_1, p)))) for p in CRIT_2 if p != [2, 1, 1]}}'''),
        ("g", "True or False", "all(v < 0 for v in EIGEN_2[(-2, -1, 1)])",
         '''mistakes={"la valeur propre de la direction z est la même en tout point, et positive : f y monte": True}'''),
    ]),

    Paper("M19.3", "Une itération linéaire 2 × 2 : point fixe, erreur, et convergence par les valeurs propres", [
        ("a", "a list of 2 numbers", "flat(STAR_3)", "decimals=6"),
        ("b", "a list of 2 lists of 2 numbers: [x1, x2]", "[flat(iterate_3(ZERO_3, 1)), flat(iterate_3(ZERO_3, 2))]",
         "decimals=6"),
        ("c", "a list of 2 numbers", "flat(EIGEN_3)",
         '''decimals=6, mistakes={"l'ordre demandé : la valeur propre de q₁ d'abord, puis celle de q₂":
                         flat(EIGEN_3[::-1])}'''),
        ("d", "a list of 2 numbers: [a, b]", "flat(BASIS_3.solve(X0_3 - STAR_3))",
         '''decimals=6, mistakes={"décompose l'ÉCART x₀ − x*, pas x₀ lui-même": flat(BASIS_3.solve(X0_3))}'''),
        ("e", "a list of 2 numbers", "flat(iterate_3(X0_3, 3))",
         '''decimals=6, mistakes={"xₖ = x* + Mᵏ(x₀ − x*) : M³x₀ seul oublie le point fixe": flat(M_3 ** 3 * X0_3),
                     "x₃ = x* + e₃ : ajoute le point fixe à l'écart": flat(iterate_3(X0_3, 3) - STAR_3)}'''),
        ("f", "an integer", "STEPS_3",
         '''fractional="le plus petit entier qui convient : arrondis vers le HAUT, math.ceil",
           mistakes={"il faut ρᵏ ≤ 10⁻³ : arrondis k vers le haut, jamais vers le bas": STEPS_3 - 1}'''),
        ("g", "True or False", "G_3",
         '''mistakes={"regarde l'écart de départ x₀ − x* : de quel vecteur propre de M est-il un multiple ?": not G_3}'''),
    ]),

    Paper("M19.4", "Résoudre un système 2 × 2 par l'itération de Richardson : trois pas à la main, et le pas critique", [
        ("a", "a list of 2 numbers", "flat(STAR_4)", "decimals=6"),
        ("b", "a list of 3 lists of 2 numbers (6 decimals): [x1, x2, x3]", "[flat(x) for x in RICH_4]",
         '''decimals=6, mistakes={"recalcule le résidu b − Axₖ à chaque pas, avec le nouvel itéré":
                         [flat(k * OMEGA_4 * B_4) for k in (1, 2, 3)]}'''),
        ("c", "a list of 2 numbers (6 decimals)", "flat(B_4 - A_4 * RICH_4[2])",
         '''decimals=6, mistakes={"le résidu est b − Ax₃, pas Ax₃": flat(A_4 * RICH_4[2])}'''),
        ("d", "a list of 2 numbers, in decreasing order", "EIGEN_4",
         '''mistakes={"en ordre décroissant": EIGEN_4[::-1]}'''),
        ("e", "a list of 2 numbers", "[float(1 - OMEGA_4 * v) for v in EIGEN_4]",
         '''decimals=6, mistakes={"dans le même ordre que d) : d'abord celle qui vient de la plus grande valeur propre de A":
                         [float(1 - OMEGA_4 * v) for v in EIGEN_4[::-1]]}'''),
        ("f", "a number", "float(R(2, max(EIGEN_4)))",
         '''decimals=6, mistakes={"le pas critique se règle sur la PLUS GRANDE valeur propre": float(R(2, min(EIGEN_4))),
                     "le pas critique est 2/λmax : n'oublie pas le 2": float(R(1, max(EIGEN_4)))}'''),
        ("g", "a number", "float(G_4)",
         '''decimals=6, mistakes={"la valeur propre de plus grand MODULE, pas de plus petit": float(SMALL_4),
                     "la valeur propre elle-même, avec son signe, pas son module": float(abs(G_4))}'''),
        ("h", "True or False", "H_4",
         '''mistakes={"regarde l'écart (1, −1) : de quelle valeur propre de A est-il un vecteur propre, et que vaut "
                     "1 − 0,3λ pour elle ?": not H_4}'''),
    ]),

    Paper("M19.5", "Le meilleur pas de Richardson (énoncé), et le nombre d'itérations pour gagner six décimales", [
        ("a", "a list of 3 numbers, in increasing order", "EIGEN_5",
         '''mistakes={"en ordre croissant": EIGEN_5[::-1]}'''),
        ("b", "an irreducible fraction, as text", "str(2 / LMAX_5)",
         '''kind="fraction", simplified=True,
           mistakes={"le pas critique se règle sur la PLUS GRANDE valeur propre": str(2 / LMIN_5)}'''),
        ("c", "an irreducible fraction, as text", "str(BEST_5)",
         '''kind="fraction", simplified=True,
           mistakes={"le meilleur pas ne dépend que des deux valeurs propres EXTRÊMES": str(2 / (EIGEN_5[1] + LMAX_5))}'''),
        ("d", "an irreducible fraction, as text", "str(RHO_5)",
         '''kind="fraction", simplified=True,
           mistakes={"κ = λmax/λmin est un quotient, pas une différence":
                         str((LMAX_5 - LMIN_5 - 1) / (LMAX_5 - LMIN_5 + 1))}'''),
        ("e", "an integer", "steps_to_gain(RHO_5)",
         '''fractional="le plus petit entier qui convient : arrondis vers le HAUT, math.ceil",
           mistakes={"ρᵏ ≤ 10⁻⁶ : arrondis k vers le haut, jamais vers le bas": steps_to_gain(RHO_5) - 1}'''),
        ("f", "an irreducible fraction, as text", "str(PRUDENT_5)",
         '''kind="fraction", simplified=True,
           mistakes={"le facteur est le plus grand des |1 − ωλᵢ| : regarde aussi la plus petite valeur propre":
                         str(abs(1 - EIGEN_5[1] / LMAX_5))}'''),
        ("g", "an integer", "steps_to_gain(PRUDENT_5)",
         '''fractional="le plus petit entier qui convient : arrondis vers le HAUT, math.ceil",
           mistakes={"ρᵏ ≤ 10⁻⁶ : arrondis k vers le haut, jamais vers le bas": steps_to_gain(PRUDENT_5) - 1}'''),
        ("h", "an integer", "steps_to_gain(R(110 - 1, 110 + 1))",
         '''fractional="le plus petit entier qui convient : arrondis vers le HAUT, math.ceil",
           mistakes={"ρᵏ ≤ 10⁻⁶ : arrondis k vers le haut, jamais vers le bas": steps_to_gain(R(110 - 1, 110 + 1)) - 1}'''),
    ]),

    Paper("M19.6", "Une récurrence d'ordre 2 à racines réelles : terme général et convergence", [
        ("a", "a list of 2 numbers, in decreasing order", "flat(ROOTS_6)",
         '''decimals=6, mistakes={"en ordre décroissant": flat(ROOTS_6[::-1])}'''),
        ("b", "a list of 2 numbers: [alpha, beta]", "flat(COEFS_6)",
         '''decimals=6, mistakes={"α va avec la plus grande racine r₁": flat(COEFS_6[::-1])}'''),
        ("c", "a list of 2 numbers: [u2, u3]", "flat(U_6[2:4])",
         '''decimals=6, mistakes={"la récurrence RETRANCHE q uₖ : uₖ₊₂ = 0,7uₖ₊₁ − 0,1uₖ": flat(PLUS_6[2:4])}'''),
        ("d", "a number (6 decimals)", "float(U_6[10])",
         '''decimals=6, mistakes={"uₖ = α r₁ᵏ + β r₂ᵏ : n'oublie pas les coefficients α et β":
                         float(ROOTS_6[0] ** 10 + ROOTS_6[1] ** 10)}'''),
        ("e", "a list of 2 numbers, in decreasing order", "flat(ROOTS_V_6)",
         '''decimals=6, mistakes={"en ordre décroissant": flat(ROOTS_V_6[::-1])}'''),
        ("f", "a number", "float(V1_6)",
         '''decimals=6, mistakes={"vₖ tend vers 0 quand le coefficient de la racine de module > 1 est NUL : c'est "
                     "l'autre terme qui doit rester": float(2 * max(ROOTS_V_6))}'''),
        ("g", "True or False", "bool(abs(Q_6) < 1 and abs(P_6) < 1 + Q_6)"),
    ]),

    Paper("M19.7", "Une récurrence d'ordre 2 à racines complexes : module et oscillation amortie", [
        ("a", "a number", "float(DELTA_7)",
         '''decimals=6, mistakes={"Δ = p² − 4q : n'oublie pas le facteur 4": float(P_7 ** 2 - Q_7)}'''),
        ("b", "a list of 2 numbers: [real part, positive imaginary part]", "[float(RE_7), float(IM_7)]",
         '''decimals=6, mistakes={"les racines sont p/2 ± i√(−Δ)/2 : divise aussi la partie imaginaire par 2":
                         [float(RE_7), float(2 * IM_7)]}'''),
        ("c", "a number", "float(MODULUS_7)",
         '''decimals=6, mistakes={"le module est √(a² + b²) = √q, pas la partie réelle": float(RE_7),
                     "le module est √q : q est le CARRÉ du module, le produit des deux racines conjuguées": float(Q_7)}'''),
        ("d", "a number (4 decimals)", "float(THETA_7)",
         '''decimals=4, mistakes={"un angle en radians, pas en degrés": math.degrees(float(THETA_7))}'''),
        ("e", "a list of 4 numbers (6 decimals): [u2, u3, u4, u5]", "flat(U_7[2:6])",
         '''decimals=6, mistakes={"la récurrence RETRANCHE q uₖ : uₖ₊₂ = p uₖ₊₁ − q uₖ": flat(PLUS_7[2:6])}'''),
        ("f", "a list of 2 numbers: [A, B]", "flat(AB_7)", "decimals=6"),
        ("g", "an integer", "STEPS_7",
         '''fractional="le plus petit entier qui convient : arrondis vers le HAUT, math.ceil",
           mistakes={"0,65ᵏ < 10⁻³ : arrondis k vers le haut, jamais vers le bas": STEPS_7 - 1}'''),
        ("h", "a number (2 decimals)", "float(2 * sympy.pi / THETA_7)",
         '''decimals=2, mistakes={"une période complète est un tour, un angle de 2π, pas π": float(sympy.pi / THETA_7)}'''),
    ]),

    Paper("M19.8", "Une pente estimée sur B points tirés au hasard : espérance et variance de l'estimation", [
        ("a", "a number", "float(FPRIME_8)",
         '''decimals=6, mistakes={"F′(2) est la MOYENNE des quatre dérivées gₖ(2)": float(4 * FPRIME_8)}'''),
        ("b", "a list of 4 numbers", "flat(G_8)",
         '''mistakes={"gₖ(a) = 2Iₖ(aIₖ − Uₖ) : multiplie chaque résidu aIₖ − Uₖ par 2Iₖ": flat(RESIDUALS_8)}'''),
        ("c", "a number", "float(SIGMA2_8)",
         '''decimals=6, mistakes={"σ² divise par N = 4, la dispersion des quatre gradients, pas par N − 1":
                         {float(SIGMA2_8 * 4 / 3), 19.67, 19.6667},
                     "σ² est la moyenne des carrés des ÉCARTS à F′(2), pas des carrés des gₖ":
                         float(sum(g * g for g in G_8) / 4)}'''),
        ("d", "a number", "float(SIGMA2_8 / 2)",
         '''decimals=6, mistakes={"la variance d'une moyenne de B tirages indépendants est σ²/B, pas σ²/B²":
                         {float(SIGMA2_8 / 4), 3.69}}'''),
        ("e", "a number (4 decimals)", "math.sqrt(SIGMA2_8 / 2)",
         '''decimals=4, mistakes={"l'erreur type est la RACINE de la variance": float(SIGMA2_8 / 2),
                     "l'erreur type est σ/√B : divise σ par √B, pas par B": {math.sqrt(SIGMA2_8) / 2, 1.92}}'''),
        ("f", "an integer", "B_MIN_8",
         '''mistakes={"l'erreur type est σ/√B : élève au carré l'inégalité σ/√B ≤ 0,5": math.ceil(math.sqrt(SIGMA2_8) / 0.5)}'''),
        ("g", "a number (4 decimals)", "float(SIGMA2_8 / 2 * R(4 - 2, 4 - 1))",
         '''decimals=4, mistakes={"le facteur de population finie est (N − B)/(N − 1), pas son inverse":
                         float(SIGMA2_8 / 2 * R(4 - 1, 4 - 2)),
                     "sans remise, la variance de la moyenne est multipliée par (N − B)/(N − 1)": float(SIGMA2_8 / 2),
                     "le facteur de population finie est (N − B)/(N − 1), pas (N − B)/N":
                         float(SIGMA2_8 / 2 * R(4 - 2, 4))}'''),
        ("h", "an irreducible fraction, as text", "str(POSITIVE_8)",
         '''kind="fraction", simplified=True,
           mistakes={"tirages AVEC remise : les 16 couples ordonnés sont équiprobables, pas les 10 paires": str(PAIRS_8),
                     "STRICTEMENT positive : une moyenne nulle ne compte pas": str(NONNEGATIVE_8)}'''),
        ("i", "an irreducible fraction, as text", "str(A_STAR_8)",
         '''kind="fraction", simplified=True,
           mistakes={"a* annule F′ : a* = Σ IₖUₖ / Σ Iₖ², pas Σ Uₖ / Σ Iₖ": str(R(sum(U_8), sum(I_8)))}'''),
    ]),

    Paper("M19.9", "Projeter un même vecteur sur une boule et sur un pavé : deux points, deux directions", [
        ("a", "a number", "int(NORM_9)"),
        ("b", "a list of 3 numbers", "flat(BALL_9)",
         '''decimals=6, mistakes={"couper chaque coordonnée à ±r projette sur le PAVÉ [−r, r]³, pas sur la boule":
                         flat(X_9.applyfunc(lambda v: max(min(v, R(28, 10)), -R(28, 10))))}'''),
        ("c", "a list of 3 numbers", "flat(BOX_9)",
         '''mistakes={"sur un pavé, chaque coordonnée est coupée séparément, sans facteur commun":
                         flat(X_9 * R(2, 6))}'''),
        ("d", "a list of 2 numbers (4 decimals)", "[float((X_9 - BALL_9).norm()), float((X_9 - BOX_9).norm())]",
         '''decimals=4, mistakes={"la distance de x à sa projection est ‖x − P(x)‖, pas ‖x‖":
                         [float(NORM_9), float((X_9 - BOX_9).norm())]}'''),
        ("e", "a number (4 decimals)", "float(X_9.dot(BOX_9) / (NORM_9 * BOX_9.norm()))",
         '''decimals=4, mistakes={"le cosinus vaut 1 pour la boule ; sur le pavé, chaque coordonnée est coupée "
                                 "séparément": 1}'''),
        ("f", "True or False", "F_9",
         '''mistakes={"compare les deux vecteurs : l'un est-il un multiple POSITIF de l'autre ?": not F_9}'''),
    ]),

    Paper("M19.14", "Pont : un pas de Richardson est un pas de descente sur ½ xᵀA x − bᵀx (énoncé, sans calcul)", [
        ("a", LETTER, '"B"',
         '''mistakes={"le gradient de ½xᵀAx est Ax, celui de bᵀx est b : b − Ax en est l'opposé": "A",
                     "le ½ de ½xᵀAx compense le 2 de la dérivée de xᵀAx": "C"}'''),
        ("b", LETTER, '"C"',
         '''mistakes={"la hessienne de ½xᵀAx est A : le ½ compense le 2 de la dérivée seconde": {"B", "D"}}'''),
        ("c", LETTER, '"A"',
         '''mistakes={"le résidu b − Ax est l'OPPOSÉ du gradient : un pas de Richardson descend": "B"}'''),
        ("d", LETTER, '"A"'),
        ("e", LETTER, '"B"',
         '''mistakes={"c'est la plus GRANDE valeur propre qui limite le pas": "C",
                     "c'est le meilleur pas, pas celui au-dessus duquel la descente diverge": "D"}'''),
        ("f", LETTER, '"B"',
         '''mistakes={"∇f = Ax − b : le résidu b − Ax en est l'opposé": "A"}'''),
        ("g", "True or False", "True",
         '''mistakes={"A symétrique définie positive : f est strictement convexe, et son unique point critique, où "
                     "∇f = 0, est la solution": False}'''),
    ]),

    Paper("M19.15", "Pont : le préconditionnement diagonal, une idée commune à plusieurs méthodes de workbookIA 19", [
        ("a", "a list of 2 numbers (3 decimals), in decreasing order", "flat(EIGEN_15)",
         '''decimals=3, mistakes={"en ordre décroissant": flat(EIGEN_15[::-1])}'''),
        ("b", "a number (1 decimal)", "float(KAPPA_15)", "decimals=1"),
        ("c", MATRIX, "rows(TILDE_15)",
         '''decimals=6, mistakes={"ãᵢⱼ = aᵢⱼ/√(aᵢᵢaⱼⱼ) : divise par la racine des DEUX coefficients diagonaux":
                         rows(sympy.diag(*[1 / A_15[i, i] for i in range(2)]) * A_15),
                     "ãᵢⱼ = aᵢⱼ/√(aᵢᵢaⱼⱼ) : la RACINE du produit des deux coefficients diagonaux":
                         rows(sympy.Matrix(2, 2, lambda i, j: 1 if i == j else A_15[i, j] / (A_15[i, i] * A_15[j, j])))}'''),
        ("d", "a number", "int(KAPPA_TILDE_15)"),
        ("e", "a list of 2 integers", "STEPS_15",
         '''mistakes={"l'ordre demandé : A d'abord, puis Ã": STEPS_15[::-1],
                     "le nombre d'itérations s'arrondit vers le HAUT ; vérifie aussi que ρ* a gardé 6 chiffres "
                     "significatifs": [STEPS_15[0] - 1, STEPS_15[1]]}'''),
        ("f", "a list of 2 numbers", "flat(SQRT_D_15 * X_15)",
         '''decimals=6, mistakes={"y = D^(1/2)x : multiplie chaque coordonnée par √aᵢᵢ, ne la divise pas":
                         flat(SQRT_D_15.inv() * X_15)}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly (SymPy, fractions) from the statements
import math
from fractions import Fraction
from itertools import product

import numpy as np
import sympy

R = sympy.Rational


def rows(M):
    """A SymPy matrix as the list of its rows (Python ints, floats for the other numbers)."""
    return [[int(v) if v.is_Integer else float(v) for v in M.row(i)] for i in range(M.rows)]


def flat(values):
    """SymPy numbers (a row, a column, a list) as a flat list (Python ints, floats for the other numbers)."""
    return [int(v) if sympy.sympify(v).is_Integer else float(v) for v in values]


def steps_to_gain(rho, d=6):
    """The smallest k with rho^k ≤ 10^(−d), for an exact 0 < rho < 1 (computed with 50 digits)."""
    k = sympy.N(d * sympy.log(10) / -sympy.log(rho), 50)
    assert abs(k - sympy.floor(k)) > 1e-30                   # never an integer: the rounding up is safe
    return int(sympy.ceiling(k))


x_, y_, z_ = sympy.symbols("x y z")                                                              # M19.1
V_1 = (x_, y_, z_)
F_1 = x_ ** 2 * z_ + y_ * z_ ** 2 - 3 * x_ * y_ + sympy.exp(x_ - y_)
P_1 = {x_: 1, y_: 1, z_: 2}
GRAD_1 = sympy.Matrix([sympy.diff(F_1, v) for v in V_1]).subs(P_1)
HESS_1 = sympy.hessian(F_1, V_1).subs(P_1)
H_1 = sympy.Matrix([R(1, 10), R(-2, 10), R(1, 10)])                  # (1.1, 0.8, 2.1) − p
TAYLOR1_1 = F_1.subs(P_1) + (GRAD_1.T * H_1)[0]
TAYLOR2_1 = TAYLOR1_1 + (H_1.T * HESS_1 * H_1)[0] / 2
TRUE_1 = F_1.subs({x_: R(11, 10), y_: R(8, 10), z_: R(21, 10)})
U_1 = sympy.Matrix([2, -1, 2]) / 3
CURVATURE_1 = (U_1.T * HESS_1 * U_1)[0]
F_2 = x_ ** 3 + 3 * x_ * y_ ** 2 - 15 * x_ - 12 * y_ + z_ ** 2 - 2 * z_                           # M19.2
CRIT_2 = sorted([int(s[v]) for v in V_1] for s in sympy.solve([sympy.diff(F_2, v) for v in V_1], V_1, dict=True)
                if all(s[v].is_real for v in V_1))
HESS_2 = sympy.hessian(F_2, V_1)
EIGEN_2 = {tuple(p): sorted(int(v) for v, m in HESS_2.subs(dict(zip(V_1, p))).eigenvals().items() for _ in range(m))
           for p in CRIT_2}
M_3 = sympy.Matrix([[R(5, 10), R(2, 10)], [R(2, 10), R(2, 10)]])                                 # M19.3
C_3 = sympy.Matrix([R(16, 10), R(8, 10)])
STAR_3 = (sympy.eye(2) - M_3).solve(C_3)
ZERO_3, X0_3 = sympy.zeros(2, 1), sympy.Matrix([4, 7])
BASIS_3 = sympy.Matrix([[2, 1], [1, -2]])                          # the columns q1 = (2, 1) and q2 = (1, −2)


def iterate_3(x0, k):
    """x_k of x ← M x + c from x0, exactly."""
    x = x0
    for _ in range(k):
        x = M_3 * x + C_3
    return x


EIGEN_3 = [(M_3 * BASIS_3[:, j])[0] / BASIS_3[0, j] for j in range(2)]
assert all(M_3 * BASIS_3[:, j] == EIGEN_3[j] * BASIS_3[:, j] for j in range(2))
STEPS_3 = steps_to_gain(max(abs(v) for v in EIGEN_3), 3)
E0_G_3 = sympy.Matrix([5, 0]) - STAR_3
G_3 = bool(M_3 * E0_G_3 == EIGEN_3[1] * E0_G_3)                  # the start error is an eigenvector of 0.1
A_4, B_4 = sympy.Matrix([[5, 3], [3, 5]]), sympy.Matrix([2, 6])                                   # M19.4
STAR_4, OMEGA_4 = A_4.solve(B_4), R(8, 100)
RICH_4, x_4 = [], sympy.zeros(2, 1)
for _ in range(3):
    x_4 = x_4 + OMEGA_4 * (B_4 - A_4 * x_4)
    RICH_4.append(x_4)
EIGEN_4 = sorted((int(v) for v in A_4.eigenvals()), reverse=True)
G_4 = max((1 - R(3, 10) * v for v in EIGEN_4), key=abs)
SMALL_4 = min((1 - R(3, 10) * v for v in EIGEN_4), key=abs)
E0_H_4 = sympy.Matrix([1, -1])
H_4 = bool(A_4 * E0_H_4 == 2 * E0_H_4 and abs(1 - R(3, 10) * 2) < 1)   # an eigenvector of 2: the factor 0.4
A_5 = sympy.Matrix([[7, 6, 0], [6, 7, 0], [0, 0, 7]])                                              # M19.5
EIGEN_5 = sorted(int(v) for v, m in A_5.eigenvals().items() for _ in range(m))
LMIN_5, LMAX_5 = sympy.Integer(EIGEN_5[0]), sympy.Integer(EIGEN_5[-1])
BEST_5 = 2 / (LMIN_5 + LMAX_5)
RHO_5 = (LMAX_5 / LMIN_5 - 1) / (LMAX_5 / LMIN_5 + 1)
assert RHO_5 == max(abs(1 - BEST_5 * v) for v in EIGEN_5)
PRUDENT_5 = max(abs(1 - v / LMAX_5) for v in EIGEN_5)
r_ = sympy.Symbol("r")                                                                             # M19.6
P_6, Q_6 = R(7, 10), R(1, 10)
ROOTS_6 = sorted(sympy.solve(r_ ** 2 - P_6 * r_ + Q_6, r_), reverse=True)
alpha_, beta_ = sympy.symbols("alpha beta")
COEFS_6 = [v for v in sympy.solve([alpha_ + beta_ - 3, alpha_ * ROOTS_6[0] + beta_ * ROOTS_6[1] - R(12, 10)],
                                  [alpha_, beta_], dict=True)[0].values()]
U_6, PLUS_6 = [R(3), R(12, 10)], [R(3), R(12, 10)]
for _ in range(9):
    U_6.append(P_6 * U_6[-1] - Q_6 * U_6[-2])
    PLUS_6.append(P_6 * PLUS_6[-1] + Q_6 * PLUS_6[-2])              # the sign of q forgotten
assert U_6[10] == 2 * R(1, 2) ** 10 + R(1, 5) ** 10
ROOTS_V_6 = sorted(sympy.solve(r_ ** 2 - R(3, 2) * r_ - 1, r_), reverse=True)
V1_6 = 2 * min(ROOTS_V_6)                       # v_k = 2 (−0.5)^k: the coefficient of 2^k is zero
P_7, Q_7 = R(5, 10), R(4225, 10000)                                                                  # M19.7
DELTA_7 = P_7 ** 2 - 4 * Q_7
RE_7, IM_7 = P_7 / 2, sympy.sqrt(-DELTA_7) / 2
MODULUS_7 = sympy.sqrt(RE_7 ** 2 + IM_7 ** 2)
assert MODULUS_7 == sympy.sqrt(Q_7)
THETA_7 = sympy.acos(P_7 / (2 * MODULUS_7))
U_7, PLUS_7 = [R(1), R(25, 100)], [R(1), R(25, 100)]
for _ in range(4):
    U_7.append(P_7 * U_7[-1] - Q_7 * U_7[-2])
    PLUS_7.append(P_7 * PLUS_7[-1] + Q_7 * PLUS_7[-2])
A_cos_, B_sin_ = sympy.symbols("A B")
AB_7 = list(sympy.solve([A_cos_ - U_7[0], MODULUS_7 * (A_cos_ * sympy.cos(THETA_7) + B_sin_ * sympy.sin(THETA_7))
                         - U_7[1]], [A_cos_, B_sin_], dict=True)[0].values())
STEPS_7 = next(k for k in range(1, 100) if MODULUS_7 ** k < R(1, 1000))
I_8, U_8, A0_8 = [1, 2, 2, 3], [2, 3, 5, 7], 2                                                     # M19.8
RESIDUALS_8 = [A0_8 * i - u for i, u in zip(I_8, U_8)]
G_8 = [2 * i * res for i, res in zip(I_8, RESIDUALS_8)]
FPRIME_8 = R(sum(G_8), 4)
SIGMA2_8 = sum((g - FPRIME_8) ** 2 for g in G_8) / 4
B_MIN_8 = next(b for b in range(1, 1000) if SIGMA2_8 / b <= R(1, 4))      # σ/√B ≤ 0.5
COUPLES_8 = [R(g + h, 2) for g, h in product(G_8, repeat=2)]                  # 16 ordered draws with replacement
POSITIVE_8 = R(sum(bool(m > 0) for m in COUPLES_8), 16)
NONNEGATIVE_8 = R(sum(bool(m >= 0) for m in COUPLES_8), 16)
PAIRS_8 = R(sum(bool(R(G_8[i] + G_8[j], 2) > 0) for i in range(4) for j in range(i, 4)), 10)
A_STAR_8 = R(sum(i * u for i, u in zip(I_8, U_8)), sum(i * i for i in I_8))
X_9 = sympy.Matrix([6, -3, 2])                                                                      # M19.9
NORM_9 = X_9.norm()
BALL_9 = X_9 * min(1, R(28, 10) / NORM_9)
BOX_9 = X_9.applyfunc(lambda v: max(min(v, 2), -2))
Y_9 = sympy.Matrix([4, -4, 4])
P_Y_9 = Y_9.applyfunc(lambda v: max(min(v, 2), -2))
F_9 = bool(sympy.Matrix.hstack(Y_9, P_Y_9).rank() == 1 and P_Y_9.dot(Y_9) > 0)
A_15 = sympy.Matrix([[16, 1], [1, R(1, 4)]])                                                       # M19.15
EIGEN_15 = sorted(A_15.eigenvals(), key=lambda v: float(v), reverse=True)
KAPPA_15 = EIGEN_15[0] / EIGEN_15[1]
SQRT_D_15 = sympy.diag(*[sympy.sqrt(A_15[i, i]) for i in range(2)])
TILDE_15 = SQRT_D_15.inv() * A_15 * SQRT_D_15.inv()
TILDE_EIGEN_15 = sorted(TILDE_15.eigenvals(), key=lambda v: float(v))
KAPPA_TILDE_15 = TILDE_EIGEN_15[-1] / TILDE_EIGEN_15[0]
STEPS_15 = [steps_to_gain((KAPPA_15 - 1) / (KAPPA_15 + 1)), steps_to_gain((KAPPA_TILDE_15 - 1) / (KAPPA_TILDE_15 + 1))]
X_15 = sympy.Matrix([R(1, 2), 2])'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M19.1 à M19.9, 🔗 M19.14 et M19.15)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question (une "
               "valeur exacte se tape aussi comme un calcul, `1/8`) ;\n"
               "- une liste `[0.2, -1]`, ou une liste de listes ;\n"
               "- une matrice comme la liste de ses **lignes** : `[[1, 0], [-2, 3]]` ; un nombre décimal s'y écrit "
               "avec un point, `[[0.25, 1], [0, 2]]` ;\n"
               "- une fraction irréductible entre guillemets, `\"3/7\"`, quand la question le dit ;\n"
               "- une lettre entre guillemets pour un choix, `\"D\"` ; `True` ou `False` pour un vrai ou faux.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M19.19 to M19.21)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math
import warnings

import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse
import scipy.sparse.linalg
import sympy
from matplotlib.contour import ContourSet

from wbm.nbtools import StopCheck, checked, drawn, filled, run_pytest_group, verdict

TEST_M19 = "tests/test_m19_iterative.py"          # the tests of mymath/iterative.py'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M19")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/iterative.py`, lis la "
         "docstring du module puis celle de la fonction, remplace chaque `raise NotImplementedError(...)` par ton code, "
         "**enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. ⚠️ Le "
         "squelette n'importe rien : ajoute `import numpy as np` en tête du fichier (et `import numbers` si tu t'en sers "
         "pour reconnaître un entier). `np.linalg.eigvalsh` est permis dans `critical_step_size` seulement ; ni "
         "`np.linalg.solve`, ni `np.linalg.inv`, ni `scipy.optimize`, ni `scipy.sparse.linalg` : les tests comparent tes "
         "résultats aux leurs, et un test lit ton module. Les nombres se rendent en `float` de Python, les vecteurs et "
         "les matrices en tableaux NumPy de flottants ; ne modifie jamais les tableaux reçus.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of iterative.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group(TEST_M19, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_M19, "{keyword}", impl="ref")')]


GIVEN_19 = '''x_19, y_19 = sympy.symbols("x y")
G_EXPR_19 = x_19 ** 2 / (1 + y_19 ** 2) + sympy.cos(x_19 * y_19)      # g, for SymPy


def g_19(v):
    """g(x, y) = x² / (1 + y²) + cos(x y), for v = (x, y) (NumPy)."""
    x, y = v
    return x ** 2 / (1 + y ** 2) + np.cos(x * y)


def s_19(v):
    """s(x, y, z) = cosh x + cos y + x z + z², for v = (x, y, z): the origin is a critical point."""
    x, y, z = v
    return np.cosh(x) + np.cos(y) + x * z + z ** 2


P_19 = np.array([1.2, -0.5])                     # the point of a) and e)
STEPS_19 = [10.0 ** -k for k in range(2, 9)]     # h = 1e-2, 1e-3, ..., 1e-8'''

M19_19 = Ex(
    "M19.19", "🔨", 2, 35, "La hessienne par différences centrées · `numerical_hessian`",
    "programmer la hessienne d'une fonction de $n$ variables par différences centrées, choisir son pas, et classer un "
    "point critique de $\\mathbb{R}^3$ par les signes de ses valeurs propres.",
    "fiche §1 et §2 ; M05a (le pas des différences finies)", tracks="C, E", mymath="iterative.py", given=GIVEN_19,
    body=HOWTO + r"""

Écris `numerical_hessian(f, x, h=1e-4)` (fiche §1), en suivant sa docstring : la hessienne $(n, n)$ de $f : \mathbb{R}^n \to \mathbb{R}$ en $\mathbf{x}$, par la dérivée seconde centrée sur la diagonale et par la formule à quatre points hors de la diagonale, toutes deux avec le pas `h` ; le résultat est **exactement** symétrique ; `ValueError` si `x` n'est pas un tableau 1-D non vide, ou si $h \le 0$ ; `x` n'est pas modifié.

**L'usage.** La cellule fournie donne $g(x, y) = \frac{x^2}{1 + y^2} + \cos(xy)$ (`g_19` pour NumPy, `G_EXPR_19` pour SymPy), le point $\mathbf{p} = (1{,}2 ;\ -0{,}5)$ (`P_19`), la fonction $s(x, y, z) = \cosh x + \cos y + xz + z^2$ (`s_19`), dont l'origine est un point critique, et les sept pas $h = 10^{-2}, 10^{-3}, \ldots, 10^{-8}$ (`STEPS_19`). Avec ta fonction, calcule :
- a) la hessienne numérique de $g$ en $\mathbf{p}$ (une matrice, 4 décimales) ;
- b) les valeurs propres de la hessienne numérique de $s$ en $\mathbf{0}$, en ordre croissant (`np.linalg.eigvalsh` ; une liste de 3 nombres, 4 décimales) ;
- c) l'indice de ce point critique, le nombre de ses valeurs propres négatives (un entier) ;
- d) sa nature : (A) minimum local ; (B) maximum local ; (C) point selle ; (D) le test ne conclut pas (une lettre entre guillemets) ;
- e) la hessienne exacte de $g$ en $\mathbf{p}$ par SymPy (`sympy.hessian`, puis `.subs` et `np.array(..., dtype=float)`), puis, pour chacun des sept pas de `STEPS_19`, le plus grand écart $\max_{ij}\lvert H^{\text{num}}_{ij} - H_{ij}\rvert$ : l'entier $k$ du meilleur pas $h = 10^{-k}$.

Dans ta copie : vérifie que $\mathbf{0}$ est un point critique de $s$, écris sa hessienne exacte et retrouve b) (un bloc $2 \times 2$, et un $-1$). Dans quelle direction $s$ descend-elle depuis $\mathbf{0}$ ? D'où viennent les grandes erreurs aux deux bouts de e) ? Pourquoi le meilleur pas d'une dérivée seconde est-il plus grand que celui d'une dérivée première (M05a) ? Combien de fois ta fonction évalue-t-elle $f$ pour $n = 3$, et combien d'évaluations faut-il au mieux (fiche §1) ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("numerical_hessian or module_uses") + [
        ("md", "**L'usage** : la hessienne d'une fonction en un point, un point critique de $\\mathbb{R}^3$, et le choix "
               "du pas."),
        ("todo", '''answer_M19_19a = answer_M19_19b = answer_M19_19c = answer_M19_19d = answer_M19_19e = ...
with wbm.attempt("M19.19"):          # if you call numerical_hessian here: ⏳ while it is not written
    answer_M19_19a = ...  # a) a matrix (4 decimals): the numerical Hessian of g_19 at P_19
    answer_M19_19b = ...  # b) a list of 3 numbers (4 decimals), increasing: the eigenvalues of the Hessian of s_19 at 0
    answer_M19_19c = ...  # c) an integer: the index of this critical point (its negative eigenvalues)
    answer_M19_19d = ...  # d) "A", "B", "C" or "D": its nature
    answer_M19_19e = ...  # e) an integer k: the best step h = 10^(-k) among STEPS_19, for g_19 at P_19'''),
        ("check", '''for letter, answer in zip("ab", [answer_M19_19a, answer_M19_19b]):
    wbm.check(f"M19.19{letter}", answer, computed=True)
for letter, answer in zip("cde", [answer_M19_19c, answer_M19_19d, answer_M19_19e]):
    wbm.check(f"M19.19{letter}", answer)'''),
        ("solution", '''numerical_hessian = mymath.iterative.numerical_hessian
answer_M19_19a = numerical_hessian(g_19, P_19).tolist()
values_19 = np.linalg.eigvalsh(numerical_hessian(s_19, np.zeros(3)))
answer_M19_19b = values_19.tolist()
answer_M19_19c = int(np.sum(values_19 < 0))
answer_M19_19d = "C"                                       # one negative eigenvalue, two positive: a saddle
exact_19 = np.array(sympy.hessian(G_EXPR_19, (x_19, y_19)).subs({x_19: P_19[0], y_19: P_19[1]}), dtype=float)
errors_19 = [float(np.max(np.abs(numerical_hessian(g_19, P_19, h=h) - exact_19))) for h in STEPS_19]
answer_M19_19e = int(np.argmin(errors_19)) + 2             # STEPS_19[0] is 10^-2
print("a)", np.round(answer_M19_19a, 4).tolist(), "; exacte :", np.round(exact_19, 4).tolist())
print("b)", np.round(values_19, 4).tolist(), "; (3 ± √5)/2 =", round((3 - 5 ** 0.5) / 2, 4), round((3 + 5 ** 0.5) / 2, 4))
print("c)", answer_M19_19c, " d)", answer_M19_19d)
print("e) écarts :", {f"1e-{k}": f"{e:.1e}" for k, e in zip(range(2, 9), errors_19)}, "-> k =", answer_M19_19e)'''),
        ("record", '''x_19r, y_19r = sympy.symbols("x y")
g_19r = x_19r ** 2 / (1 + y_19r ** 2) + sympy.cos(x_19r * y_19r)
point_19r = {x_19r: sympy.Rational(6, 5), y_19r: sympy.Rational(-1, 2)}
exact_19r = np.array(sympy.hessian(g_19r, (x_19r, y_19r)).subs(point_19r).evalf(30), dtype=float)
no_four_19r = exact_19r * np.array([[1.0, 4.0], [4.0, 1.0]])          # the cross entries without the 4 of 4h²
wbm.record("M19.19a", exact_19r.tolist(), decimals=4,
           mistakes={"la formule à quatre points divise par 4h² : relis-la dans la docstring": no_four_19r.tolist()})
values_19r = [-1.0, (3 - math.sqrt(5)) / 2, (3 + math.sqrt(5)) / 2]   # the Hessian of s at 0: [[1, 0, 1], [0, -1, 0], [1, 0, 2]]
wbm.record("M19.19b", values_19r, decimals=4,
           mistakes={"en ordre croissant : np.linalg.eigvalsh les rend déjà dans cet ordre": values_19r[::-1]})
wbm.record("M19.19c", sum(v < 0 for v in values_19r),
           mistakes={"l'indice compte les valeurs propres NÉGATIVES": sum(v > 0 for v in values_19r)})
wbm.record("M19.19d", "C",
           mistakes={"des valeurs propres des deux signes : relis le test du second ordre (fiche §2)": {"A", "B"},
                     "aucune valeur propre n'est nulle, même à la précision des différences finies : le test conclut":
                         "D"})
g_num_19r = sympy.lambdify([(x_19r, y_19r)], g_19r, "numpy")


def centered_19r(f, p, h):
    """The Hessian of f at p by the two centered formulas of the fiche (§1), written again here."""
    p = np.asarray(p, dtype=float)
    E, H = h * np.eye(len(p)), np.empty((len(p), len(p)))
    for i in range(len(p)):
        for j in range(len(p)):
            H[i, j] = ((f(p + E[i]) - 2 * f(p) + f(p - E[i])) / h ** 2 if i == j else
                       (f(p + E[i] + E[j]) - f(p + E[i] - E[j]) - f(p - E[i] + E[j]) + f(p - E[i] - E[j]))
                       / (4 * h ** 2))
    return H


errors_19r = [np.max(np.abs(centered_19r(g_num_19r, [1.2, -0.5], 10.0 ** -k) - exact_19r)) for k in range(2, 9)]
best_19r = int(np.argmin(errors_19r)) + 2
assert best_19r == 4 and min(errors_19r[1], errors_19r[3]) > 20 * errors_19r[2]   # 1e-4 wins by a factor 20 at least
wbm.record("M19.19e", best_19r,
           mistakes={"10⁻⁵ est le meilleur pas d'une dérivée PREMIÈRE centrée (M05a) ; une dérivée seconde divise par "
                     "h², et les arrondis grandissent plus vite": 5,
                     "le plus petit pas n'est pas le meilleur : les arrondis, divisés par h², grandissent quand h "
                     "diminue": 8,
                     "np.argmin rend une position dans la liste, et STEPS_19 commence à 10⁻²": best_19r - 2})'''),
    ],
    note=r"a) $\nabla^2 g(\mathbf{p}) \approx \begin{pmatrix} 1{,}3937 & 2{,}5958 \\ 2{,}5958 & -1{,}5571 \end{pmatrix}$, à "
         r"$3 \cdot 10^{-8}$ près de la hessienne exacte. b) La hessienne de $s$ en $\mathbf{0}$ est "
         r"$\begin{pmatrix} 1 & 0 & 1 \\ 0 & -1 & 0 \\ 1 & 0 & 2 \end{pmatrix}$ : la valeur propre $-1$ (direction "
         r"$y$) et celles du bloc $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, $\frac{3 \pm \sqrt5}{2} \approx 0{,}3820$ "
         r"et $2{,}6180$. c) Indice 1 : d) un point selle, où $s$ descend le long de l'axe des $y$ ($\cos y \le 1$). "
         r"e) L'écart vaut environ $2 \cdot 10^{-4}$ pour $h = 10^{-2}$, $2 \cdot 10^{-6}$ pour $10^{-3}$, $3 \cdot 10^{-8}$ "
         r"pour $10^{-4}$, puis remonte : $3 \cdot 10^{-6}$ pour $10^{-5}$, et de l'ordre de 1 pour $10^{-8}$. La "
         r"troncature est en $h^2$, les arrondis en $\varepsilon/h^2$ : l'équilibre est vers $\varepsilon^{1/4} \approx "
         r"10^{-4}$, plus grand que le $\varepsilon^{1/3} \approx 10^{-5}$ d'une dérivée première centrée (M05a). La "
         r"référence évalue $f$ $2n^2 + 1 = 19$ fois pour $n = 3$ (le centre une seule fois).",
)

GIVEN_20 = '''K_20 = np.array([[100.0, -4.0],
                 [-4.0, 4.0]])                  # the stiff and the soft spring of the fiche (§5)
A_20 = np.array([[5.0, -2.0],
                 [-2.0, 2.0]])                  # the two springs of the fiche (§4)
B_20 = np.array([2.0, 1.0])
X_STAR_20 = np.array([1.0, 1.5])               # the solution of A_20 x = B_20'''

M19_20 = Ex(
    "M19.20", "🔨", 2, 30, "Le pas critique d'une matrice symétrique définie positive, et les itérés de Richardson · "
    "`critical_step_size, richardson_iterates`",
    "programmer le pas critique $2/\\lambda_{\\max}$ et l'itération de Richardson, puis lire sur les itérés le facteur "
    "de convergence et le nombre d'itérations.", "fiche §4 et §5", tracks="C, E", mymath="iterative.py",
    given=GIVEN_20,
    body=r"""Écris `critical_step_size(A)` et `richardson_iterates(A, b, omega, x0=None, n_steps=10)` (fiche §4), en suivant leurs docstrings :
- `critical_step_size(A)` rend le pas critique $\frac{2}{\lambda_{\max}}$ d'une matrice symétrique définie positive, en `float` ; `ValueError` si `A` n'est pas carrée, pas symétrique (à la tolérance de la docstring du module), ou pas définie positive ;
- `richardson_iterates(A, b, omega, x0=None, n_steps=10)` rend le tableau $(N + 1, n)$ des itérés $\mathbf{x}_0, \ldots, \mathbf{x}_N$ de $\mathbf{x}_{k+1} = \mathbf{x}_k + \omega(\mathbf{b} - \mathbf{A}\mathbf{x}_k)$, un par ligne (la ligne 0 est `x0`, le vecteur nul par défaut) ; elle ne vérifie pas la convergence : avec un pas trop grand, elle rend les itérés qui explosent ; `ValueError` pour des formes qui ne vont pas ensemble ou un nombre de pas qui n'est pas un entier $\ge 0$.

**L'usage : les ressorts de la fiche.** La cellule fournie donne la matrice $\mathbf{K}$ du ressort raide et du ressort souple (§5, `K_20`), et le système des deux ressorts (§4) : $\mathbf{A}$, $\mathbf{b}$ et sa solution $\mathbf{x}^\star = (1 ;\ 1{,}5)$ (`A_20`, `B_20`, `X_STAR_20`). Avec tes fonctions, calcule :
- a) le pas critique de $\mathbf{K}$ (6 décimales) ;
- b) le pas critique de $\tilde{\mathbf{K}} = \mathbf{D}^{-1/2}\mathbf{K}\mathbf{D}^{-1/2}$, $\mathbf{D}$ la diagonale de $\mathbf{K}$ (un nombre) ;
- c) pour les deux ressorts, avec $\omega = 0{,}32$ (le pas de la fiche, juste sous le pas critique), depuis $\mathbf{0}$ : le rapport $\lVert\mathbf{e}_{61}\rVert/\lVert\mathbf{e}_{60}\rVert$ des normes de deux écarts successifs, $\mathbf{e}_k = \mathbf{x}_k - \mathbf{x}^\star$ (4 décimales) ;
- d) pour les deux ressorts, au meilleur pas $\omega^\star = \frac27$, depuis $\mathbf{0}$ : le plus petit $k$ tel que $\lVert\mathbf{e}_k\rVert \le 10^{-6}\lVert\mathbf{e}_0\rVert$ (un entier).

Dans ta copie : combien de fois la mise à l'échelle agrandit-elle le pas critique, et pourquoi ? Compare c) à $\rho(0{,}32) = \max(\lvert 1 - 0{,}32\lambda_{\min}\rvert, \lvert 1 - 0{,}32\lambda_{\max}\rvert)$ : laquelle des deux valeurs propres décide ? Calcule aussi $\lVert\mathbf{e}_3\rVert/\lVert\mathbf{e}_2\rVert$ : de quel facteur est-il proche, et pourquoi ce n'est pas le même (compare les deux composantes de $\mathbf{e}_0 = -\mathbf{x}^\star$ sur les vecteurs propres $(1, 2)$ et $(2, -1)$) ? Compare d) à la fiche (§5). Avec $\omega^\star$, pourquoi le rapport $\lVert\mathbf{e}_{k+1}\rVert/\lVert\mathbf{e}_k\rVert$ est-il le même à chaque pas, quel que soit le départ ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("critical_step_size or richardson_iterates") + [
        ("md", "**L'usage** : les pas critiques de la fiche, puis le facteur de convergence et le nombre d'itérations, "
               "lus sur les itérés."),
        ("todo", '''answer_M19_20a = answer_M19_20b = answer_M19_20c = answer_M19_20d = ...
with wbm.attempt("M19.20"):          # if you call your functions here: ⏳ while they are not written
    answer_M19_20a = ...  # a) a number (6 decimals): the critical step of K_20
    answer_M19_20b = ...  # b) a number: the critical step of K̃ = D^(-1/2) K_20 D^(-1/2)
    answer_M19_20c = ...  # c) a number (4 decimals): ‖e_61‖ / ‖e_60‖ for A_20, B_20, ω = 0.32, from 0
    answer_M19_20d = ...  # d) an integer: the smallest k with ‖e_k‖ ≤ 1e-6 ‖e_0‖ at ω* = 2/7, from 0'''),
        ("check", '''for letter, answer in zip("abcd", [answer_M19_20a, answer_M19_20b, answer_M19_20c, answer_M19_20d]):
    wbm.check(f"M19.20{letter}", answer, computed=True)'''),
        ("solution", '''critical_step_size = mymath.iterative.critical_step_size
richardson_iterates = mymath.iterative.richardson_iterates
scale_20 = 1 / np.sqrt(np.diag(K_20))
K_tilde_20 = K_20 * np.outer(scale_20, scale_20)           # k_ij / √(k_ii k_jj)
answer_M19_20a = critical_step_size(K_20)
answer_M19_20b = critical_step_size(K_tilde_20)
errors_20 = np.linalg.norm(richardson_iterates(A_20, B_20, 0.32, n_steps=70) - X_STAR_20, axis=1)
answer_M19_20c = float(errors_20[61] / errors_20[60])
best_20 = np.linalg.norm(richardson_iterates(A_20, B_20, 2 / 7, n_steps=60) - X_STAR_20, axis=1)
answer_M19_20d = int(np.flatnonzero(best_20 <= 1e-6 * best_20[0])[0])
print("a)", round(answer_M19_20a, 6), " b)", round(answer_M19_20b, 6), "; K̃ =", K_tilde_20.tolist(),
      "; rapport :", round(answer_M19_20b / answer_M19_20a, 1))
print("c)", round(answer_M19_20c, 4), "; ‖e_3‖/‖e_2‖ =", round(float(errors_20[3] / errors_20[2]), 4))
print("d)", answer_M19_20d, "; ‖e_k+1‖/‖e_k‖ au meilleur pas :", np.round(best_20[1:6] / best_20[:5], 6).tolist())'''),
        ("record", '''k_20r = np.array([[100.0, -4.0], [-4.0, 4.0]])
lambdas_20r = np.linalg.eigvalsh(k_20r)
wbm.record("M19.20a", 2 / lambdas_20r[-1], decimals=6,
           mistakes={"le pas critique se règle sur la PLUS GRANDE valeur propre": 2 / lambdas_20r[0],
                     "la diagonale de K n'est pas son spectre : calcule ses valeurs propres": 2 / k_20r[0, 0]})
tilde_20r = k_20r / np.sqrt(np.outer(np.diag(k_20r), np.diag(k_20r)))
wbm.record("M19.20b", 2 / np.linalg.eigvalsh(tilde_20r)[-1], decimals=6,
           mistakes={"le pas critique se règle sur la PLUS GRANDE valeur propre de K̃":
                         2 / np.linalg.eigvalsh(tilde_20r)[0]})
a_20r, star_20r = np.array([[5.0, -2.0], [-2.0, 2.0]]), np.array([1.0, 1.5])
m_20r = np.eye(2) - 0.32 * a_20r                                     # e_k = (I − ωA)^k e_0, e_0 = −x*
norms_20r = [np.linalg.norm(np.linalg.matrix_power(m_20r, k) @ -star_20r) for k in range(62)]
wbm.record("M19.20c", norms_20r[61] / norms_20r[60], decimals=4,
           mistakes={"ρ(ω) est le PLUS GRAND des |1 − ωλᵢ| : la composante la plus lente finit par l'emporter":
                         min(abs(1 - 0.32 * lambdas) for lambdas in np.linalg.eigvalsh(a_20r)),
                     "le rapport demandé est celui du 60ᵉ pas, quand la composante la plus lente l'emporte, pas celui "
                     "des premiers pas": {norms_20r[k + 1] / norms_20r[k] for k in range(4)}})
rho_20r = (6 - 1) / (6 + 1)                                          # ω* = 2/7: every component × 5/7 in modulus
wbm.record("M19.20d", math.ceil(6 * math.log(10) / -math.log(rho_20r)))'''),
    ],
    note=r"a) $\lambda_{\max}(\mathbf{K}) = 52 + \sqrt{2\,320} \approx 100{,}166$, d'où $\omega_c \approx 0{,}019967$, "
         r"un peu moins que $\frac{2}{100}$. b) $\tilde{\mathbf{K}} = \begin{pmatrix} 1 & -0{,}2 \\ -0{,}2 & 1 "
         r"\end{pmatrix}$ a pour valeurs propres $0{,}8$ et $1{,}2$ : $\omega_c = \frac{2}{1{,}2} = \frac53$, "
         r"environ 83 fois plus grand, car la mise à l'échelle ramène la plus grande courbure de 100 à 1,2. c) $\rho(0{,}32) = "
         r"\max(0{,}68 ;\ 0{,}92) = 0{,}92$ : c'est la valeur propre 6, de facteur $-0{,}92$, qui décide, et le rapport "
         r"vaut $0{,}9200$ au 60ᵉ pas. Au début, il est proche de l'autre facteur : $\frac{\lVert\mathbf{e}_3\rVert}"
         r"{\lVert\mathbf{e}_2\rVert} \approx 0{,}694$, car $\mathbf{e}_0 = -\mathbf{x}^\star$ a une composante huit fois "
         r"plus grande sur $(1, 2)$, de facteur $0{,}68$, que sur $(2, -1)$ ; elle diminue plus vite, et la composante "
         r"raide, qui change de signe à chaque pas, l'emporte dès le 7ᵉ pas ; le rapport dépasse $0{,}91$ au 12ᵉ. d) 42, comme dans la fiche : avec "
         r"$\omega^\star$, les deux composantes sont multipliées par $\frac57$ et $-\frac57$, et la norme de l'écart "
         r"exactement par $\frac57$ à chaque pas, depuis tout départ.",
)

M19_21 = Ex(
    "M19.21", "🔨", 1, 15, "Une récurrence linéaire d'ordre d · `linear_recurrence`",
    "programmer une récurrence linéaire d'ordre quelconque, retrouver la forme $\\lvert r\\rvert^k\\cos k\\theta$ "
    "d'une récurrence à racines complexes, et suivre une récurrence d'ordre 3 vers sa limite.", "fiche §6 ; R5",
    tracks="C",
    mymath="iterative.py",
    body=r"""Écris `linear_recurrence(coefficients, initial, n_terms)` (fiche §6), en suivant sa docstring : les `n_terms` premiers termes de $u_{k+d} = c_1u_{k+d-1} + \cdots + c_du_k$, où `coefficients` $= [c_1, \ldots, c_d]$ ($c_1$ multiplie le terme le plus **récent**) et `initial` $= [u_0, \ldots, u_{d-1}]$, en tableau NumPy de flottants ; une récurrence $u_{k+2} = p\,u_{k+1} - q\,u_k$ s'écrit donc `coefficients = [p, -q]`. Avec moins de `n_terms` que $d$, ce sont les premières valeurs de départ ; `ValueError` si `coefficients` est vide, si `initial` n'a pas $d$ valeurs, ou si `n_terms` n'est pas un entier $\ge 0$ ; le résultat est un **nouveau** tableau.

**L'usage.** Avec ta fonction :
- a) l'exemple de la fiche (§6), $u_{k+2} = 0{,}8\,u_{k+1} - 0{,}64\,u_k$ depuis $u_0 = 1$, $u_1 = 0{,}4$ : $u_9$ (6 décimales) ;
- b) vrai ou faux : pour $0 \le k \le 39$, ses termes s'écartent de $0{,}8^k\cos\frac{k\pi}{3}$ de moins de $10^{-12}$ ;
- c) la récurrence d'ordre 3 $u_{k+3} = 0{,}5\,u_{k+2} + 0{,}3\,u_{k+1} + 0{,}2\,u_k$, depuis $u_0 = 0$, $u_1 = 10$, $u_2 = 4$ : $u_{11}$ (6 décimales).

Dans ta copie : pourquoi $u_9$ vaut-il $-0{,}8^9$ ? Pour c), les coefficients ont pour somme 1 : chaque terme est une moyenne pondérée des trois précédents. Vérifie que $1$ est racine de $r^3 - 0{,}5r^2 - 0{,}3r - 0{,}2$, factorise, et montre que les deux autres racines sont complexes, de module $\sqrt{0{,}2}$. Montre que $u_{k+2} + 0{,}5\,u_{k+1} + 0{,}2\,u_k$ ne change pas d'un rang au suivant, et déduis-en la limite exacte $\ell$ de $u_k$. De combien $u_{11}$ s'en écarte-t-il, et de combien l'écart est-il multiplié, à peu près, à chaque rang ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("linear_recurrence") + [
        ("md", "**L'usage** : une oscillation amortie de la fiche, puis une récurrence d'ordre 3."),
        ("todo", '''answer_M19_21a = answer_M19_21b = answer_M19_21c = ...
with wbm.attempt("M19.21"):          # if you call linear_recurrence here: ⏳ while it is not written
    answer_M19_21a = ...  # a) a number (6 decimals): u_9 of u_{k+2} = 0.8 u_{k+1} − 0.64 u_k from (1, 0.4)
    answer_M19_21b = ...  # b) True or False: |u_k − 0.8^k cos(kπ/3)| < 1e-12 for 0 ≤ k ≤ 39
    answer_M19_21c = ...  # c) a number (6 decimals): u_11 of the order-3 recurrence from (0, 10, 4)'''),
        ("check", '''for letter, answer in zip("abc", [answer_M19_21a, answer_M19_21b, answer_M19_21c]):
    wbm.check(f"M19.21{letter}", answer, computed=True)'''),
        ("solution", '''linear_recurrence = mymath.iterative.linear_recurrence
terms_21 = linear_recurrence([0.8, -0.64], [1.0, 0.4], 40)
k_21 = np.arange(40)
gap_21 = float(np.max(np.abs(terms_21 - 0.8 ** k_21 * np.cos(k_21 * np.pi / 3))))
answer_M19_21a = float(terms_21[9])
answer_M19_21b = bool(gap_21 < 1e-12)
order3_21 = linear_recurrence([0.5, 0.3, 0.2], [0.0, 10.0, 4.0], 41)
answer_M19_21c = float(order3_21[11])
print("a)", answer_M19_21a, "; −0.8⁹ =", -0.8 ** 9, " b)", answer_M19_21b, f"(plus grand écart {gap_21:.1e})")
print("c)", answer_M19_21c, "; premiers termes :", np.round(order3_21[:8], 4).tolist())
print("u_{k+2} + 0.5 u_{k+1} + 0.2 u_k :", np.round(order3_21[2:7] + 0.5 * order3_21[1:6] + 0.2 * order3_21[0:5], 12).tolist())
print("écarts à 90/17 :", [f"{abs(u - 90 / 17):.1e}" for u in order3_21[9:14]], "; u_40 − 90/17 =",
      f"{order3_21[40] - 90 / 17:.1e}")'''),
        ("record", '''from fractions import Fraction


def exact_21r(coefficients, initial, k):
    """u_k of a linear recurrence, exactly (fractions)."""
    terms = [Fraction(v) for v in initial]
    while len(terms) <= k:
        terms.append(sum(c * terms[-1 - i] for i, c in enumerate(coefficients)))
    return terms[k]


u9_21r = exact_21r([Fraction(4, 5), Fraction(-16, 25)], [1, Fraction(2, 5)], 9)
assert u9_21r == -Fraction(4, 5) ** 9
wbm.record("M19.21a", float(u9_21r), decimals=6,
           mistakes={"coefficients = [p, −q] : u_{k+2} = p u_{k+1} − q u_k, le signe de q compte":
                         float(exact_21r([Fraction(4, 5), Fraction(16, 25)], [1, Fraction(2, 5)], 9))})
wbm.record("M19.21b", True,
           mistakes={"compare tes termes à 0,8ᵏ cos(kπ/3), en radians (np.cos), en valeur absolue": False})
weights_21r = [Fraction(1, 2), Fraction(3, 10), Fraction(1, 5)]
u11_21r = exact_21r(weights_21r, [0, 10, 4], 11)
neighbours_21r = {round(float(exact_21r(weights_21r, [0, 10, 4], k)), 6) for k in (10, 12)}
assert round(float(u11_21r), 6) not in neighbours_21r and abs(u11_21r * 10 ** 6 % 1 - Fraction(1, 2)) > Fraction(1, 10)
wbm.record("M19.21c", float(u11_21r), decimals=6,
           mistakes={"c₁ multiplie le terme le plus RÉCENT : coefficients = [0.5, 0.3, 0.2]":
                         float(exact_21r(weights_21r[::-1], [0, 10, 4], 11)),
                     "initial = [u₀, u₁, u₂], dans cet ordre : u₀ = 0 d'abord": float(exact_21r(weights_21r, [4, 10, 0], 11)),
                     "u₁₁ est le terme d'indice 11 : il faut n_terms = 12 termes, puis [11]": neighbours_21r})'''),
    ],
    note=r"a) $u_k = 0{,}8^k\cos\frac{k\pi}{3}$ et $\cos 3\pi = -1$ : $u_9 = -0{,}8^9 = -0{,}134218$. b) Vrai : l'écart "
         r"reste de l'ordre de $10^{-16}$, l'arrondi de chaque produit. c) $r^3 - 0{,}5r^2 - 0{,}3r - 0{,}2 = (r - 1)"
         r"(r^2 + 0{,}5r + 0{,}2)$ : la racine 1, et deux racines complexes $-0{,}25 \pm 0{,}37i$ environ, de module "
         r"$\sqrt{0{,}2} \approx 0{,}447$, qui s'éteignent. La quantité $u_{k+2} + 0{,}5\,u_{k+1} + 0{,}2\,u_k$ vaut 9 à "
         r"chaque rang ; à la limite $\ell(1 + 0{,}5 + 0{,}2) = 9$, d'où $\ell = \frac{90}{17} \approx 5{,}294118$. "
         r"$u_{11} \approx 5{,}292669$ s'en écarte encore de $1{,}4 \cdot 10^{-3}$ ; l'écart est multiplié par "
         r"$\sqrt{0{,}2} \approx 0{,}45$ par rang en moyenne, en oscillant : $u_{40}$ est à $10^{-13}$ près.",
)

PART_A = Part("A", "Ta librairie : la hessienne numérique, le pas critique, les itérés de Richardson et les récurrences",
              "Fiche §1, §2, §4, §5 et §6. Les quatre fonctions de `mymath/iterative.py`, leurs tests, et un usage de "
              "chacune.", given=TOOLS, exercises=[M19_19, M19_20, M19_21])

# ---------------------------------------------------------------------------
# Notebook exercises: compare, predict, measure (M19.22 to M19.24)
# ---------------------------------------------------------------------------
GIVEN_22 = '''N_22 = 50                                        # the inner points of the bar
T_ENDS_22 = (10.0, 70.0)                         # the temperatures of its two ends, in °C'''

M19_22 = Ex(
    "M19.22", "📦", 1, 15, "`scipy.sparse.linalg.cg` : le gradient conjugué contre Richardson",
    "résoudre un système creux avec le gradient conjugué de SciPy, compter ses itérations, et les comparer à celles "
    "de Richardson au meilleur pas.", "fiche §3 et §5 ; Ex M19.20", tracks="C", given=GIVEN_22,
    body=r"""Le **gradient conjugué** (fiche §5, 💻) résout un système symétrique défini positif en choisissant, à chaque pas, la meilleure combinaison des directions déjà explorées : en arithmétique exacte, il trouve la solution en au plus $n$ itérations, et son nombre d'itérations croît comme $\sqrt\kappa$ au lieu de $\kappa$. SciPy l'implémente dans `scipy.sparse.linalg.cg`, qui accepte une matrice **creuse** (*sparse*), dont SciPy ne stocke que les coefficients non nuls.

**Une barre qui tiédit, plus finement.** Une barre a $n = 50$ points intérieurs régulièrement espacés, et ses bouts sont maintenus à 10 °C et 70 °C (`N_22`, `T_ENDS_22`). À l'équilibre, chaque température est la moyenne de ses deux voisines (fiche §3) : $-T_{i-1} + 2T_i - T_{i+1} = 0$, les températures des bouts passant au second membre. C'est $\mathbf{A}\mathbf{T} = \mathbf{b}$, avec $\mathbf{A}$ tridiagonale (2 sur la diagonale, $-1$ juste au-dessus et juste au-dessous) et $\mathbf{b} = (10, 0, \ldots, 0, 70)$. Les valeurs propres de $\mathbf{A}$ sont $\lambda_k = 2 - 2\cos\frac{k\pi}{n + 1}$, $k = 1, \ldots, n$.
- Construis `A_22` avec `scipy.sparse.diags([-np.ones(n - 1), 2 * np.ones(n), -np.ones(n - 1)], [-1, 0, 1], format="csr")`, et `B_22` ;
- lance `scipy.sparse.linalg.cg(A_22, B_22, rtol=1e-8, callback=...)` depuis $\mathbf{0}$ (le départ par défaut) : `rtol` est le résidu relatif visé, $\lVert\mathbf{b} - \mathbf{A}\mathbf{T}\rVert/\lVert\mathbf{b}\rVert \le 10^{-8}$ (l'ancien nom `tol` a disparu de SciPy), et le `callback` est une fonction que `cg` appelle une fois par itération, avec l'itéré courant : qu'elle ajoute 1 à un compteur ;
- puis lance Richardson au meilleur pas $\omega^\star = \frac{2}{\lambda_{\min} + \lambda_{\max}}$ avec ta `richardson_iterates`, 10 000 pas depuis $\mathbf{0}$ (elle attend un tableau NumPy : passe-lui `A_22.toarray()`), et cherche le premier itéré dont le résidu relatif est $\le 10^{-8}$.

Réponds :
- a) le nombre d'itérations du gradient conjugué (un entier) ;
- b) le nombre d'itérations de Richardson au meilleur pas (un entier) ;
- c) le conditionnement $\kappa$ de `A_22`, par la formule de ses valeurs propres (1 décimale).

Dans ta copie : que vaut le meilleur pas ici, et pourquoi Richardson est-elle alors la méthode de Jacobi de la fiche (§5) ? Compare a) à $n$ et à $\sqrt\kappa$, b) à $1{,}15\,\kappa\,d$ avec $d = 8$. Combien de coefficients la matrice creuse stocke-t-elle (`A_22.nnz`), contre $n^2$ pour un tableau plein ? Vérifie que la solution de `cg` est le profil linéaire entre 10 °C et 70 °C.""",
    todo='''A_22 = ...            # the sparse (50, 50) matrix tridiag(−1, 2, −1), by scipy.sparse.diags
B_22 = ...            # the right-hand side: 10 first, 70 last, 0 elsewhere
answer_M19_22a = ...  # a) an integer: the iterations of scipy.sparse.linalg.cg down to a relative residual of 1e-8
answer_M19_22c = ...  # c) a number (1 decimal): the condition number of A_22, from the formula of its eigenvalues
answer_M19_22b = ...
with wbm.attempt("M19.22"):          # richardson_iterates: ⏳ while it is not written
    answer_M19_22b = ...  # b) an integer: the iterations of Richardson at the best step, down to 1e-8''',
    check='''wbm.check("M19.22a", answer_M19_22a)
wbm.check("M19.22b", answer_M19_22b, computed=True)
wbm.check("M19.22c", answer_M19_22c)''',
    solution='''n_22 = N_22
A_22 = scipy.sparse.diags([-np.ones(n_22 - 1), 2 * np.ones(n_22), -np.ones(n_22 - 1)], [-1, 0, 1], format="csr")
B_22 = np.zeros(n_22)
B_22[0], B_22[-1] = T_ENDS_22
calls_22 = []
T_22, info_22 = scipy.sparse.linalg.cg(A_22, B_22, rtol=1e-8, callback=lambda xk: calls_22.append(1))
answer_M19_22a = len(calls_22)
lambdas_22 = 2 - 2 * np.cos(np.arange(1, n_22 + 1) * np.pi / (n_22 + 1))
answer_M19_22c = float(lambdas_22.max() / lambdas_22.min())
omega_22 = 2 / (lambdas_22.min() + lambdas_22.max())
iterates_22 = mymath.iterative.richardson_iterates(A_22.toarray(), B_22, omega_22, n_steps=10_000)
relative_22 = np.linalg.norm(B_22 - (A_22 @ iterates_22.T).T, axis=1) / np.linalg.norm(B_22)
answer_M19_22b = int(np.flatnonzero(relative_22 <= 1e-8)[0])
profile_22 = T_ENDS_22[0] + (T_ENDS_22[1] - T_ENDS_22[0]) * np.arange(1, n_22 + 1) / (n_22 + 1)
print("a)", answer_M19_22a, "itérations, info =", info_22, "; écart au profil linéaire :",
      f"{np.max(np.abs(T_22 - profile_22)):.1e}", "; √κ ≈", round(answer_M19_22c ** 0.5, 1))
print("b)", answer_M19_22b, "itérations avec ω* =", omega_22, "; 1,15 κ d ≈", round(1.15 * answer_M19_22c * 8))
print("c) κ =", round(answer_M19_22c, 1), "; coefficients stockés :", A_22.nnz, "contre", n_22 ** 2)''',
    record='''n_22r = 50
a_22r = 2 * np.eye(n_22r) - np.eye(n_22r, k=1) - np.eye(n_22r, k=-1)
b_22r = np.zeros(n_22r)
b_22r[0], b_22r[-1] = 10.0, 70.0
calls_22r = []
scipy.sparse.linalg.cg(scipy.sparse.csr_matrix(a_22r), b_22r, rtol=1e-8, callback=lambda xk: calls_22r.append(1))
wbm.record("M19.22a", len(calls_22r))
x_22r, k_22r = np.zeros(n_22r), 0                     # Richardson at ω* = 2/(λmin + λmax) = 1/2, step by step
while np.linalg.norm(b_22r - a_22r @ x_22r) > 1e-8 * np.linalg.norm(b_22r):
    x_22r = x_22r + 0.5 * (b_22r - a_22r @ x_22r)
    k_22r += 1
wbm.record("M19.22b", k_22r)
lambdas_22r = 2 - 2 * np.cos(np.arange(1, n_22r + 1) * np.pi / (n_22r + 1))
wrong_22r = 4 / (2 - 2 * np.cos(np.pi / n_22r))       # λ_k with n instead of n + 1
wbm.record("M19.22c", lambdas_22r.max() / lambdas_22r.min(), decimals=1,
           mistakes={"λₖ = 2 − 2cos(kπ/(n + 1)) : le dénominateur est n + 1 = 51, et κ = λmax/λmin": wrong_22r})''',
    note=r"a) 50 itérations, soit $n$ : sur ce système, le gradient conjugué n'a besoin d'aucun arrondi favorable, il "
         r"trouve la solution, le profil linéaire de 10 °C à 70 °C, à $10^{-13}$ près, en exactement $n$ pas (et "
         r"$\sqrt\kappa \approx 32$ n'est qu'un ordre de grandeur). b) 7 565 itérations de Richardson au meilleur pas, "
         r"$\omega^\star = \frac12$ : les valeurs propres extrêmes ont pour somme $4$, et Richardson de pas $\frac12$ sur "
         r"une diagonale constante 2 est la méthode de Jacobi. $1{,}15\,\kappa\,d \approx 9\,700$ est le compte du pire "
         r"départ ; celui-ci a de petites composantes sur les deux directions extrêmes, et s'en tire un peu mieux. c) "
         r"$\kappa = \cot^2\frac{\pi}{102} \approx 1\,053{,}5$. La matrice creuse stocke 148 coefficients, contre 2 500.",
)

GIVEN_23 = '''rng_23 = np.random.default_rng(5232)
Q_23, _ = np.linalg.qr(rng_23.normal(size=(4, 4)))            # an orthonormal basis of eigenvectors (the columns)
A_23 = Q_23 @ np.diag([2.0, 5.0, 11.0, 24.0]) @ Q_23.T         # symmetric, of eigenvalues 2, 5, 11 and 24
A_23 = (A_23 + A_23.T) / 2
X_STAR_23 = rng_23.normal(size=4)                              # the solution
B_23 = A_23 @ X_STAR_23
X0_23 = X_STAR_23 + Q_23 @ np.ones(4)                          # the start: the same component on each eigenvector
OMEGAS_23 = {"A": 1 / 30, "B": 1 / 13, "C": 0.0875, "D": 0.0825}   # the four steps'''

EXPERIMENT_23 = '''with checked("M19.23"):
    print("pas    ω         ρ(ω)     ⌈6 ln 10 / (−ln ρ)⌉   itérations comptées (1 500 pas au plus)")
    fig_23, ax_23 = plt.subplots(figsize=(7.5, 4.2))
    try:
        for name_23, omega_23 in OMEGAS_23.items():
            iterates_23 = mymath.iterative.richardson_iterates(A_23, B_23, omega_23, x0=X0_23, n_steps=1500)
            gains_23 = np.linalg.norm(iterates_23 - X_STAR_23, axis=1) / np.linalg.norm(X0_23 - X_STAR_23)
            reached_23 = np.flatnonzero(gains_23 <= 1e-6)
            rho_23 = max(abs(1 - omega_23 * 2), abs(1 - omega_23 * 24))
            formula_23 = f"{math.ceil(6 * math.log(10) / -math.log(rho_23)):8d}" if rho_23 < 1 else "     ∞  "
            shown_23 = (f"{reached_23[0]}" if reached_23.size else
                        f"aucune : l'écart a été multiplié par {gains_23[-1]:.1e}")
            print(f"({name_23})    {omega_23:.5f}   {rho_23:.4f}   {formula_23}              {shown_23}")
            ax_23.semilogy(np.minimum(gains_23, 1e8), label=f"({name_23}) ω = {omega_23:.4f} : ρ = {rho_23:.3f}")
        ax_23.axhline(1e-6, color="0.5", ls="--", lw=1)
        ax_23.set_xlabel("itération k")
        ax_23.set_ylabel("‖e_k‖ / ‖e_0‖ (échelle log)")
        ax_23.set_ylim(1e-9, 1e8)
        ax_23.legend(fontsize=8)
        ax_23.grid(True, which="both", alpha=0.3)
    except BaseException:
        plt.close(fig_23)
        raise
    plt.show()'''

M19_23 = Ex(
    "M19.23", "🔮", 1, 10, "Prédire le nombre d'itérations de Richardson selon ω, puis vérifier",
    "prévoir, par le facteur $\\rho(\\omega)$, quel pas fait diverger Richardson et combien d'itérations demandent les "
    "autres, puis le compter.", "fiche §3 à §5 ; Ex M19.20", tracks="C, E", hypothesis=True, given=GIVEN_23,
    body=r"""La cellule fournie construit une matrice symétrique $4 \times 4$, `A_23`, de valeurs propres $2$, $5$, $11$ et $24$, un second membre `B_23` de solution `X_STAR_23`, et un départ `X0_23` dont l'écart a la même composante sur les quatre vecteurs propres. On lance Richardson avec quatre pas (`OMEGAS_23`) : (A) $\omega = \frac{1}{30}$ ; (B) $\omega = \frac{1}{13}$ ; (C) $\omega = 0{,}0875$ ; (D) $\omega = 0{,}0825$.

Prédis, **avant d'exécuter quoi que ce soit** :
- a) lequel des quatre pas ne converge pas (une lettre entre guillemets) ;
- b), c) et d) pour les pas (A), (B) et (D) : le nombre d'itérations qui gagne 6 décimales, $\lVert\mathbf{e}_k\rVert \le 10^{-6}\,\lVert\mathbf{e}_0\rVert$, tel que le donne la formule $\left\lceil\frac{6\ln 10}{-\ln\rho(\omega)}\right\rceil$ (fiche §3), avec $\rho(\omega) = \max(\lvert 1 - 2\omega\rvert, \lvert 1 - 24\omega\rvert)$ (fiche §4) : trois entiers.

L'expérience lance ta `richardson_iterates` (1 500 pas au plus), compte les itérations depuis `X0_23`, et trace $\lVert\mathbf{e}_k\rVert/\lVert\mathbf{e}_0\rVert$.

Écris tes quatre prédictions, vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M19_23a = ...  # a) "A", "B", "C" or "D": the step that does not converge, written BEFORE the experiment
prediction_M19_23b = ...  # b) an integer: the iterations given by the formula for (A)
prediction_M19_23c = ...  # c) an integer: the iterations given by the formula for (B)
prediction_M19_23d = ...  # d) an integer: the iterations given by the formula for (D)''',
    check='''for letter, prediction in zip("abcd", [prediction_M19_23a, prediction_M19_23b, prediction_M19_23c,
                                         prediction_M19_23d]):
    wbm.check(f"M19.23{letter}", prediction)''',
    record='''def formula_23r(omega, pick=max):
    """The smallest k with ρ^k ≤ 1e-6, ρ the larger (pick=max) of |1 − 2ω| and |1 − 24ω| (None when ρ ≥ 1)."""
    rho = pick(abs(1 - 2 * omega), abs(1 - 24 * omega))
    return math.ceil(6 * math.log(10) / -math.log(rho)) if rho < 1 else None


steps_23r = {"A": 1 / 30, "B": 1 / 13, "C": 0.0875, "D": 0.0825}
diverging_23r = [name for name, omega in steps_23r.items() if formula_23r(omega) is None]
assert diverging_23r == ["C"]
wbm.record("M19.23a", diverging_23r[0], prediction=True,
           mistakes={"compare chaque pas au pas critique 2/λmax : un pas un peu en dessous converge encore, "
                     "lentement": "D",
                     "compare chaque pas au pas critique 2/λmax : un petit pas converge toujours": {"A", "B"}})
for letter_23r, name_23r in zip("bcd", "ABD"):
    right_23r = formula_23r(steps_23r[name_23r])
    wrong_23r = {"le plus petit k tel que ρᵏ ≤ 10⁻⁶ : arrondis vers le HAUT, jamais vers le bas": right_23r - 1}
    if formula_23r(steps_23r[name_23r], pick=min) != right_23r:
        wrong_23r["ρ(ω) est le PLUS GRAND des deux modules |1 − 2ω| et |1 − 24ω|"] = formula_23r(steps_23r[name_23r],
                                                                                             pick=min)
    wbm.record(f"M19.23{letter_23r}", right_23r, prediction=True, mistakes=wrong_23r,
               fractional="le plus petit entier qui convient : arrondis vers le HAUT, math.ceil")''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(EXPERIMENT_23, [f"prediction_M19_23{letter}" for letter in "abcd"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", EXPERIMENT_23),
        ("md", "**Après l'expérience**, dans ta copie : calcule le pas critique et le meilleur pas de `A_23`, et place "
               "les quatre pas par rapport à eux. Pour chacun des trois pas qui convergent, laquelle des deux valeurs "
               "propres extrêmes décide de $\\rho(\\omega)$ ? Pourquoi les comptes de l'expérience sont-ils un peu en "
               "dessous de la formule (compare $\\lVert\\mathbf{e}_0\\rVert$ à sa composante sur le vecteur propre le "
               "plus lent) ? Calcule le rapport des nombres d'itérations de (D) et de (B), alors que $\\omega_D > "
               "\\omega_B$."),
    ],
    note=r"Le pas critique vaut $\frac{2}{24} = \frac{1}{12} \approx 0{,}0833$ : a) (C), $\omega = 0{,}0875$, est au-dessus, "
         r"$1 - 24\omega = -1{,}1$, et la composante de $\lambda_{\max}$ grandit en changeant de signe ; elle est "
         r"multipliée par $6 \cdot 10^{61}$ en 1 500 pas. b) (A), $\omega = \frac{1}{30}$ : $\rho = \max(\frac{14}{15} ;\ "
         r"0{,}2) = \frac{14}{15}$, c'est $\lambda_{\min}$ qui décide ; $\frac{6\ln 10}{\ln(15/14)} \approx 200{,}2$, soit "
         r"201 itérations ; l'expérience en compte 191. c) (B), le meilleur pas $\frac{2}{2 + 24} = \frac{1}{13}$ : "
         r"$\rho = \frac{11}{13} = \frac{\kappa - 1}{\kappa + 1}$ avec $\kappa = 12$, 83 itérations ; 81 comptées. d) (D), "
         r"$\omega = 0{,}0825$, juste sous le pas critique : $\rho = \lvert 1 - 1{,}98\rvert = 0{,}98$, c'est "
         r"$\lambda_{\max}$ qui décide ; 684 itérations, 650 comptées. Les comptes sont un peu en dessous de la formule, "
         r"car l'écart de départ n'a que la moitié de sa norme sur le vecteur propre le plus lent. (D) demande "
         r"$\frac{684}{83} \approx 8{,}2$ fois plus d'itérations que (B), bien que son pas soit plus grand.",
)

GIVEN_24 = '''N_24 = [2, 3, 5, 8, 13, 20, 32, 50]               # the inner points of eight bars, finer and finer


def bar_24(n):
    """The matrix tridiag(−1, 2, −1) of a bar with n inner points (a NumPy array), and its right-hand side, the ends
    being at 10 °C and 70 °C."""
    A = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    b = np.zeros(n)
    b[0], b[-1] = 10.0, 70.0
    return A, b'''

FIGURE_24 = '''fig, ax = plt.subplots(figsize=(7.0, 4.4))
try:
    kappas_f24 = np.asarray(kappas_24, dtype=float)
    for counts_f24, label_f24, color_f24 in ((richardson_24, "Richardson au meilleur pas", "C0"),
                                             (cg_24, "gradient conjugué", "C3")):
        counts_f24 = np.asarray(counts_f24, dtype=float)
        slope_f24, intercept_f24 = np.polyfit(np.log(kappas_f24), np.log(counts_f24), 1)
        ax.loglog(kappas_f24, counts_f24, "o", color=color_f24, label=f"{label_f24} : pente {slope_f24:.2f}")
        ax.loglog(kappas_f24, np.exp(intercept_f24) * kappas_f24 ** slope_f24, "-", color=color_f24, alpha=0.6)
    ax.set_xlabel("conditionnement κ (échelle log)")
    ax.set_ylabel("itérations jusqu'au résidu relatif 1e-6 (échelle log)")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=8)
except BaseException:
    plt.close(fig)
    raise
plt.show()'''

M19_24 = Ex(
    "M19.24", "🔬", 2, 20, "Le nombre d'itérations contre le conditionnement : une droite en échelle logarithmique",
    "mesurer comment le nombre d'itérations de Richardson et du gradient conjugué croît avec le conditionnement, et "
    "lire l'exposant sur une droite en échelles logarithmiques.", "fiche §5 ; Ex M19.20 et M19.22", tracks="C",
    given=GIVEN_24,
    body=r"""Les barres de M19.22, de plus en plus fines : pour chaque nombre $n$ de points intérieurs de `N_24` (de 2 à 50), `bar_24(n)` rend la matrice tridiagonale et le second membre (bouts à 10 °C et 70 °C ; cellule fournie). Plus la barre est fine, plus le système est mal conditionné. Pour chaque barre :
- son conditionnement $\kappa$, par la formule des valeurs propres de M19.22 ;
- le nombre d'itérations de Richardson au meilleur pas, depuis $\mathbf{0}$, jusqu'au premier itéré dont le résidu relatif $\lVert\mathbf{b} - \mathbf{A}\mathbf{x}_k\rVert/\lVert\mathbf{b}\rVert$ est $\le 10^{-6}$ (ta `richardson_iterates` ; 6 000 pas suffisent) ;
- le nombre d'itérations de `scipy.sparse.linalg.cg`, avec `rtol=1e-6` (il accepte aussi un tableau plein) et un `callback` qui compte.

Range-les dans `kappas_24`, `richardson_24` et `cg_24`, dans l'ordre de `N_24`. La cellule de vérification trace les deux comptes en fonction de $\kappa$, les deux axes en échelle logarithmique, avec les droites ajustées par `np.polyfit` sur $(\ln\kappa, \ln\text{compte})$ : une droite de pente $s$ veut dire un compte proportionnel à $\kappa^s$.

Réponds :
- a) le nombre d'itérations de Richardson pour la barre la plus fine, $n = 50$ (un entier) ;
- b) la pente de la droite de Richardson, arrondie au demi le plus proche (0,5 ; 1 ; 1,5 ou 2) ;
- c) la même pente pour le gradient conjugué, arrondie au demi le plus proche.

Dans ta copie : que vaut le meilleur pas pour toutes ces barres, et pourquoi ? Compare a) à $1{,}15\,\kappa\,d$ avec $d = 6$. Pourquoi le gradient conjugué fait-il ici exactement $n$ itérations, et comment $\kappa$ grandit-il avec $n$ (pour $n$ grand, $1 - \cos x \approx \frac{x^2}{2}$) ? Pour une barre de 1 000 points, combien d'itérations prévois-tu pour chaque méthode ?""",
    todo='''kappas_24 = ...       # the 8 condition numbers of the bars of N_24, from the formula of their eigenvalues
cg_24 = ...           # the 8 iteration counts of scipy.sparse.linalg.cg, down to a relative residual of 1e-6
richardson_24 = ...
answer_M19_24a = answer_M19_24b = answer_M19_24c = ...
with wbm.attempt("M19.24"):          # richardson_iterates: ⏳ while it is not written
    richardson_24 = ...   # the 8 iteration counts of Richardson at the best step, down to a relative residual of 1e-6
    answer_M19_24a = ...  # a) an integer: Richardson's count for the finest bar, n = 50
    answer_M19_24b = ...  # b) 0.5, 1, 1.5 or 2: the slope of Richardson's line, rounded to the nearest half
    answer_M19_24c = ...  # c) 0.5, 1, 1.5 or 2: the slope of the conjugate gradient's line''',
    check='''with checked("M19.24 figure"):
    if filled(kappas_24, richardson_24, cg_24):
''' + "\n".join("        " + line if line else "" for line in FIGURE_24.splitlines()) + '''
    else:
        print("⏳ Ex M19.24 : la figure attend tes trois listes, kappas_24, richardson_24 et cg_24.")
wbm.check("M19.24a", answer_M19_24a, computed=True)
for letter, answer in zip("bc", [answer_M19_24b, answer_M19_24c]):
    wbm.check(f"M19.24{letter}", answer)''',
    solution='''kappas_24, richardson_24, cg_24 = [], [], []
for n_24 in N_24:
    A_b24, b_b24 = bar_24(n_24)
    lambdas_24 = 2 - 2 * np.cos(np.arange(1, n_24 + 1) * np.pi / (n_24 + 1))
    kappas_24.append(float(lambdas_24.max() / lambdas_24.min()))
    omega_24 = 2 / (lambdas_24.min() + lambdas_24.max())
    iterates_24 = mymath.iterative.richardson_iterates(A_b24, b_b24, omega_24, n_steps=6000)
    relative_24 = np.linalg.norm(b_b24 - iterates_24 @ A_b24.T, axis=1) / np.linalg.norm(b_b24)
    richardson_24.append(int(np.flatnonzero(relative_24 <= 1e-6)[0]))
    calls_24 = []
    scipy.sparse.linalg.cg(A_b24, b_b24, rtol=1e-6, callback=lambda xk: calls_24.append(1))
    cg_24.append(len(calls_24))
slope_r24 = np.polyfit(np.log(kappas_24), np.log(richardson_24), 1)[0]
slope_c24 = np.polyfit(np.log(kappas_24), np.log(cg_24), 1)[0]
answer_M19_24a = richardson_24[-1]
answer_M19_24b = round(2 * slope_r24) / 2
answer_M19_24c = round(2 * slope_c24) / 2
print("κ :", np.round(kappas_24, 1).tolist())
print("Richardson :", richardson_24, "; 1,15 κ d :", [round(1.15 * k * 6) for k in kappas_24])
print("gradient conjugué :", cg_24)
print("pentes :", round(slope_r24, 3), round(slope_c24, 3), "->", answer_M19_24b, answer_M19_24c)

''' + FIGURE_24,
    record='''counts_24r, kappas_24r, cg_24r = [], [], []
for n_24r in [2, 3, 5, 8, 13, 20, 32, 50]:
    a_24r = 2 * np.eye(n_24r) - np.eye(n_24r, k=1) - np.eye(n_24r, k=-1)
    b_24r = np.zeros(n_24r)
    b_24r[0], b_24r[-1] = 10.0, 70.0
    lambdas_24r = 2 - 2 * np.cos(np.arange(1, n_24r + 1) * np.pi / (n_24r + 1))
    kappas_24r.append(lambdas_24r.max() / lambdas_24r.min())
    x_24r, k_24r = np.zeros(n_24r), 0                 # Richardson at ω* = 1/2, step by step
    while np.linalg.norm(b_24r - a_24r @ x_24r) > 1e-6 * np.linalg.norm(b_24r):
        x_24r = x_24r + 0.5 * (b_24r - a_24r @ x_24r)
        k_24r += 1
    counts_24r.append(k_24r)
    calls_24r = []
    scipy.sparse.linalg.cg(a_24r, b_24r, rtol=1e-6, callback=lambda xk: calls_24r.append(1))
    cg_24r.append(len(calls_24r))
slopes_24r = [np.polyfit(np.log(kappas_24r), np.log(c), 1)[0] for c in (counts_24r, cg_24r)]
assert abs(slopes_24r[0] - 1) < 0.15 and abs(slopes_24r[1] - 0.5) < 0.1   # far from the next halves
wbm.record("M19.24a", counts_24r[-1])
wbm.record("M19.24b", round(2 * slopes_24r[0]) / 2, decimals=2, choices=[0.5, 1, 1.5, 2],
           mistakes={"Richardson demande de l'ordre de κ itérations (≈ 1,15 κ d) : relis la pente de sa droite":
                         {0.5, 1.5, 2}})
wbm.record("M19.24c", round(2 * slopes_24r[1]) / 2, decimals=2, choices=[0.5, 1, 1.5, 2],
           mistakes={"le gradient conjugué grandit bien plus lentement que Richardson : relis la pente de sa droite":
                         {1, 1.5, 2}})''',
    after=[
        ("md", "**Après la figure**, dans ta copie : réponds aux questions de l'énoncé. Pour quelle taille de barre le "
               "gradient conjugué fait-il cent fois moins d'itérations que Richardson ?"),
    ],
    note=r"$\kappa$ va de 3 ($n = 2$) à $1\,053{,}5$ ($n = 50$). a) 5 139 itérations de Richardson pour $n = 50$, contre "
         r"$1{,}15\,\kappa\,d \approx 7\,270$ pour le pire départ. b) La pente de Richardson vaut environ $0{,}94$ : 1, un "
         r"compte proportionnel à $\kappa$ ; elle est un peu sous 1 parce que, pour les petites barres, "
         r"$-\ln\frac{\kappa - 1}{\kappa + 1}$ dépasse $\frac{2}{\kappa}$. c) Le gradient conjugué fait exactement $n$ "
         r"itérations (2, 3, 5… 50) ; comme $\kappa \approx \frac{4(n + 1)^2}{\pi^2}$ pour $n$ grand, $n$ grandit comme "
         r"$\sqrt\kappa$ : pente $0{,}55$, soit $\frac12$. Le meilleur pas vaut $\frac12$ pour toutes les barres "
         r"($\lambda_{\min} + \lambda_{\max} = 4$). Pour 1 000 points, $\kappa \approx 4 \times 10^5$ : environ "
         r"$3 \times 10^6$ itérations de Richardson, 1 000 du gradient conjugué.",
)

PART_B = Part("B", "Comparer, prédire, mesurer",
              "Fiche §3 à §5. Le gradient conjugué de SciPy contre Richardson sur une barre ; le nombre d'itérations de "
              "Richardson selon le pas, prédit puis compté ; et sa croissance avec le conditionnement.",
              exercises=[M19_22, M19_23, M19_24])

# ---------------------------------------------------------------------------
# Notebook exercises: draw, debug, build, challenge (M19.25 to M19.28)
# ---------------------------------------------------------------------------
GIVEN_C = ('ref_iterative = wbm.load_mymath("ref", alias="mymath_ref").iterative   # the reference: the check of '
           'M19.25')

GIVEN_25 = '''A_25 = np.array([[10.0, 6.0],
                 [6.0, 5.0]])                   # symmetric positive definite, eigenvalues 14 and 1
X_STAR_25 = np.array([1.0, -1.0])               # the solution
B_25 = A_25 @ X_STAR_25
X0_25 = np.array([-2.0, 1.0])                   # the start
N_25 = 25                                       # the number of steps
OMEGA_C_25 = 2 / 14                             # the critical step
OMEGAS_25 = [0.4 * OMEGA_C_25, 2 / (1 + 14), 0.95 * OMEGA_C_25]   # 0.4 of it, the best step, just below it'''

CHECK_25 = '''with checked("M19.25"):
    results_25 = []

    def report_25(ok, success, failure):
        results_25.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))

    fig_25, axes_25 = plt.subplots(1, 3, figsize=(14.0, 4.6))
    try:
        opened_25, contour_25, path_25, star_25, aspect_25 = [], [], [], [], []
        for ax_25, omega_25 in zip(axes_25, OMEGAS_25):
            opened_25 += drawn(draw_richardson, ax_25, A_25, B_25, omega_25, X0_25, N_25)
            want_25 = ref_iterative.richardson_iterates(A_25, B_25, omega_25, x0=X0_25, n_steps=N_25)
            contour_25.append(any(isinstance(item, ContourSet) for item in ax_25.collections))
            path_25.append(any(np.shape(line.get_xydata()) == want_25.shape
                               and np.allclose(line.get_xydata(), want_25, rtol=1e-9, atol=1e-9)
                               for line in ax_25.lines))
            points_25 = [np.asarray(line.get_xydata(), dtype=float).reshape(-1, 2) for line in ax_25.lines]
            points_25 += [np.asarray(item.get_offsets(), dtype=float).reshape(-1, 2) for item in ax_25.collections
                          if not isinstance(item, ContourSet)]
            star_25.append(any(len(p) and np.min(np.linalg.norm(p - X_STAR_25, axis=1)) < 1e-6 for p in points_25))
            aspect_25.append(ax_25.get_aspect() in ("equal", 1.0))
        report_25(not opened_25, "draw_richardson dessine dans l'axe reçu",
                  "draw_richardson doit dessiner dans l'axe reçu, sans ouvrir de figure (ni plt.figure ni plt.subplots)")
        report_25(all(contour_25), "les lignes de niveau sont tracées (ax.contour)",
                  f"pas de lignes de niveau (ax.contour) dans {contour_25.count(False)} des trois axes")
        report_25(all(path_25), f"les {N_25 + 1} itérés x₀, …, x_N sont reliés par une ligne, dans l'ordre",
                  "aucune ligne ne passe par les itérés x₀, …, x_N, tous et dans l'ordre, pour "
                  f"{path_25.count(False)} des trois pas : ax.plot(xs[:, 0], xs[:, 1], \\"o-\\"), avec xs le tableau "
                  "de richardson_iterates (x0, n_steps)")
        report_25(all(star_25), "la solution x* est marquée",
                  "marque la solution x* d'un point (ax.plot(x_star[0], x_star[1], \\"k*\\")), dans chaque axe")
        report_25(all(aspect_25), "les deux axes ont la même échelle : les ellipses ne sont pas déformées",
                  "donne la même échelle aux deux axes : ax.set_aspect(\\"equal\\")")
    except BaseException:
        plt.close(fig_25)
        raise
    plt.show()
    verdict("M19.25", all(results_25), "les lignes de niveau, les itérés et la solution sont dessinés pour les trois "
                                       "pas.", "relis les lignes ❌ ci-dessus.")'''

M19_25 = Ex(
    "M19.25", "🎨", 1, 20, "Les itérés de Richardson sur les lignes de niveau d'une forme quadratique",
    "dessiner les itérés de Richardson sur les lignes de niveau de $\\frac12\\mathbf{x}^\\top\\mathbf{A}\\mathbf{x} - "
    "\\mathbf{b}^\\top\\mathbf{x}$, et voir l'effet du pas et du conditionnement.", "fiche §4 et §5 ; Ex M19.20",
    tracks="C, E", given=GIVEN_25,
    body=r"""Richardson est une descente sur $f(\mathbf{x}) = \frac12\mathbf{x}^\top\mathbf{A}\mathbf{x} - \mathbf{b}^\top\mathbf{x}$ (fiche §4) : on la voit sur les lignes de niveau de $f$, des ellipses centrées en $\mathbf{x}^\star$, allongées dans la direction propre de $\lambda_{\min}$ (fiche §5). La cellule fournie donne $\mathbf{A} = \begin{pmatrix} 10 & 6 \\ 6 & 5 \end{pmatrix}$, de valeurs propres 14 et 1 ($\kappa = 14$ ; vecteurs propres $(3, 2)$ et $(2, -3)$), la solution $\mathbf{x}^\star = (1 ;\ -1)$, $\mathbf{b} = \mathbf{A}\mathbf{x}^\star$, le départ $\mathbf{x}_0 = (-2 ;\ 1)$, $N = 25$ pas, et trois pas : $0{,}4\,\omega_c$, le meilleur pas et $0{,}95\,\omega_c$ (`OMEGAS_25`).

Écris `draw_richardson(ax, A, b, omega, x0, n_steps)`, qui dessine dans l'axe `ax` (sans en ouvrir d'autre) :
- les lignes de niveau de $f$ : `ax.contour(X, Y, F, levels=...)`, avec `X, Y = np.meshgrid(xs, ys)` sur une grille qui contient tous les itérés, et `F` la valeur de $f$ en chaque point de la grille (`F = 0.5 * (A[0, 0] * X**2 + 2 * A[0, 1] * X * Y + A[1, 1] * Y**2) - b[0] * X - b[1] * Y`) ;
- les itérés $\mathbf{x}_0, \ldots, \mathbf{x}_N$ que rend ta `richardson_iterates`, reliés dans l'ordre par **une seule** ligne avec des points : `ax.plot(xs[:, 0], xs[:, 1], "o-")` ;
- la solution $\mathbf{x}^\star$, marquée d'un point (`np.linalg.solve` est permis ici) ;
- la même échelle sur les deux axes (`ax.set_aspect("equal")`), et un titre qui donne $\omega$.

La vérification appelle ta fonction pour les trois pas, côte à côte, et regarde le dessin : les lignes de niveau, une ligne qui passe par les $N + 1$ itérés de la référence, dans l'ordre, la solution marquée, et les échelles égales.""",
    todo='''def draw_richardson(ax, A, b, omega, x0, n_steps):
    """In ax (and no other axes): the level lines of f(x) = ½ xᵀ A x − bᵀ x, the iterates x_0, ..., x_N of
    Richardson's method joined in order by one line with markers, the solution marked, equal scales, a title."""
    raise NotImplementedError("draw_richardson n'est pas encore écrite (04_indices.md si tu bloques)")''',
    check=CHECK_25,
    solution='''def draw_richardson(ax, A, b, omega, x0, n_steps):
    """In ax (and no other axes): the level lines of f(x) = ½ xᵀ A x − bᵀ x, the iterates x_0, ..., x_N of
    Richardson's method joined in order by one line with markers, the solution marked, equal scales, a title."""
    A, b = np.asarray(A, dtype=float), np.asarray(b, dtype=float)
    path = mymath.iterative.richardson_iterates(A, b, omega, x0=x0, n_steps=n_steps)
    x_star = np.linalg.solve(A, b)
    low, high = path.min(axis=0), path.max(axis=0)
    margin = 0.25 * max(high - low)
    X, Y = np.meshgrid(np.linspace(low[0] - margin, high[0] + margin, 200),
                       np.linspace(low[1] - margin, high[1] + margin, 200))
    F = 0.5 * (A[0, 0] * X ** 2 + 2 * A[0, 1] * X * Y + A[1, 1] * Y ** 2) - b[0] * X - b[1] * Y
    f_star = -0.5 * b @ x_star                                # the minimum of f
    ax.contour(X, Y, F, levels=f_star + np.geomspace(0.02, 1.2 * (F.max() - f_star), 12), colors="0.6",
               linewidths=0.8)
    ax.plot(path[:, 0], path[:, 1], "o-", color="C0", ms=3.5, lw=1)
    ax.plot(x_star[0], x_star[1], "k*", ms=11)
    ax.set_aspect("equal")
    rho = max(abs(1 - omega * lam) for lam in np.linalg.eigvalsh(A))
    ax.set_title(f"ω = {omega:.4f} : ρ(ω) = {rho:.3f}", fontsize=10)


''' + CHECK_25,
    after=[
        ("md", "**Regarde ta figure**, puis, dans ta copie : pour chaque pas, que vaut le facteur $1 - \\omega\\lambda$ "
               "dans la direction raide $(3, 2)$, et dans la direction plate $(2, -3)$ ? Avec $0{,}95\\,\\omega_c$, "
               "pourquoi les itérés passent-ils de part et d'autre de l'axe long à chaque pas ? Calcule, pour "
               "$0 < \\omega < \\omega_c$, le plus petit facteur possible $1 - \\omega\\lambda_{\\min}$ dans la "
               "direction de l'axe long : montre qu'il vaut $1 - \\frac{2}{\\kappa}$, et donne sa valeur ici. Que "
               "verrais-tu avec $1{,}05\\,\\omega_c$ ?"),
    ],
    note=r"Les facteurs $(1 - 14\omega ;\ 1 - \omega)$ valent $(0{,}2 ;\ \frac{33}{35} \approx 0{,}943)$ pour "
         r"$0{,}4\,\omega_c = \frac{2}{35}$, $(-\frac{13}{15} ;\ \frac{13}{15})$ pour $\omega^\star = \frac{2}{15}$, et "
         r"$(-0{,}9 ;\ 0{,}864)$ pour $0{,}95\,\omega_c$. Avec $0{,}4\,\omega_c$, la composante raide diminue vite, sans "
         r"changer de signe, et la composante plate lentement. Au meilleur pas, les deux composantes diminuent au même "
         r"rythme, la raide en changeant de signe. Juste sous le pas critique, la composante raide change de signe et ne "
         r"diminue que de 10 % par pas : les itérés passent de part et d'autre de l'axe long à chaque pas. Pour "
         r"$0 < \omega < \omega_c = \frac{2}{\lambda_{\max}}$, $1 - \omega\lambda_{\min} > 1 - "
         r"\frac{2\lambda_{\min}}{\lambda_{\max}} = 1 - \frac{2}{\kappa}$, ici $\frac67 \approx 0{,}857$ : aucun pas "
         r"permis ne fait mieux dans la direction plate, et c'est le conditionnement qui fixe cette borne. Avec "
         r"$1{,}05\,\omega_c$, $1 - 14\omega = -1{,}1$ : la composante raide grandit, l'itération diverge.",
)

GIVEN_26 = '''K_26 = np.array([[3.0, -2.0, 0.0],
                 [-2.0, 5.0, -3.0],
                 [0.0, -3.0, 9.0]])            # three masses, four springs of stiffness 1, 2, 3 and 6
F_26 = np.array([1.0, 0.0, 2.0])               # the forces on the masses


# The colleague's code
def critical_26(A):
    """The critical step 2 / λmax of a symmetric positive definite matrix A."""
    return 2.0 / np.linalg.eigvalsh(A)[0]


def hessian_26(f, x, h=1e-4):
    """The Hessian of f at x by centered differences: each entry on or above the diagonal is computed once."""
    x = np.asarray(x, dtype=float)
    n = len(x)
    E = h * np.eye(n)
    H = np.zeros((n, n))
    for i in range(n):
        H[i, i] = (f(x + E[i]) - 2 * f(x) + f(x - E[i])) / h ** 2
        for j in range(i + 1, n):
            H[i, j] = (f(x + E[i] + E[j]) - f(x + E[i] - E[j]) - f(x - E[i] + E[j]) + f(x - E[i] - E[j])) / (4 * h ** 2)
    return H


def inertia_26(H):
    """The inertia (n_neg, n_zero, n_pos) of a symmetric matrix H: its numbers of negative, zero and positive
    eigenvalues, an eigenvalue counting as zero when its modulus is at most 1e-8 times the largest modulus."""
    values = np.linalg.eigvalsh(H)
    zero = 1e-8 * np.max(np.abs(values))
    return int(np.sum(values < -zero)), int(np.sum(np.abs(values) <= zero)), int(np.sum(values > zero))


def converges_26(p, q):
    """True when every solution of u_{k+2} = p u_{k+1} − q u_k tends to 0: both roots of r² − p r + q have a modulus
    < 1."""
    delta = p * p - 4 * q
    if delta >= 0:                                     # two real roots
        roots = [(p + math.sqrt(delta)) / 2, (p - math.sqrt(delta)) / 2]
        return max(abs(r) for r in roots) < 1
    modulus = abs(p) / 2                               # complex roots p/2 ± i √(−Δ)/2
    return modulus < 1


def g_26(v):
    """g(x, y, z) = x² + y² + z² + 3 sin x sin y + y z, for v = (x, y, z): the origin is a critical point."""
    x, y, z = v
    return x ** 2 + y ** 2 + z ** 2 + 3 * np.sin(x) * np.sin(y) + y * z


# The colleague's checks: all pass
print("(1) critical_26(4 I) =", critical_26(4 * np.eye(3)))
print("(2) inertia_26 de la hessienne de cos x + y² + z² en 0 :",
      inertia_26(hessian_26(lambda v: np.cos(v[0]) + v[1] ** 2 + v[2] ** 2, np.zeros(3))), "(une selle)")
print("(3) converges_26 pour les trois récurrences de la fiche :",
      [converges_26(p, q) for p, q in ((1.0, 0.21), (0.8, 0.64), (1.5, -1.0))])
omega_26 = critical_26(K_26) / 2                 # « half the critical step, to be safe »
x_26 = np.zeros(3)
for k_26 in range(1, 31):
    x_26 = x_26 + omega_26 * (F_26 - K_26 @ x_26)
    if k_26 % 10 == 0:
        print(f"(1) Richardson sur K_26 x = F_26 avec ce pas, itération {k_26} : ‖x‖ = {np.linalg.norm(x_26):.3g}")'''

CHECK_26 = '''results_26, parts_26 = [], []


def report_26(ok, success, failure):
    results_26.append(bool(ok))
    print(("✅ " + success) if ok else ("❌ " + failure))


with checked("M19.26"):                                       # (1) critical_26_fixed
    rng_26 = np.random.default_rng(5236)
    wrong_26 = []
    for n_26 in (1, 2, 3, 5):
        Q_c26, _ = np.linalg.qr(rng_26.normal(size=(n_26, n_26)))
        values_c26 = np.sort(rng_26.uniform(0.3, 9.0, size=n_26))
        A_c26 = Q_c26 @ np.diag(values_c26) @ Q_c26.T
        A_c26 = (A_c26 + A_c26.T) / 2
        got_26 = critical_26_fixed(A_c26.copy())
        if got_26 is None or not math.isclose(float(got_26), 2 / values_c26[-1], rel_tol=1e-9):
            wrong_26.append(f"une matrice {n_26} × {n_26} de valeurs propres {np.round(values_c26, 2).tolist()} : "
                            f"attendu {2 / values_c26[-1]:.6g}, reçu {got_26!r}"[:200])
    report_26(not wrong_26, "(1) critical_26_fixed : le pas critique de quatre matrices",
              "(1) critical_26_fixed, " + " ; ".join(wrong_26[:2]))
    parts_26.append(1)

with checked("M19.26"):                                       # (2) hessian_26_fixed
    xyz_26 = sympy.symbols("x y z")
    cases_26 = [(sympy.sin(xyz_26[0] * xyz_26[1]) + xyz_26[0] * xyz_26[2] ** 2, 3),
                (sympy.log(2 + xyz_26[0] ** 2) + xyz_26[1] * xyz_26[2] ** 3, 3),
                (xyz_26[0] ** 3 * xyz_26[1] - sympy.cos(xyz_26[1]), 2),
                (xyz_26[0] ** 2 + xyz_26[1] ** 2 + xyz_26[2] ** 2 + 3 * sympy.sin(xyz_26[0]) * sympy.sin(xyz_26[1])
                 + xyz_26[1] * xyz_26[2], 3)]                 # g_26
    rng_26 = np.random.default_rng(5237)
    wrong_26 = []
    for expr_26, n_26 in cases_26:
        symbols_26 = xyz_26[:n_26]
        f_c26 = sympy.lambdify([symbols_26], expr_26, "numpy")
        point_26 = rng_26.uniform(-1.5, 1.5, size=n_26)
        exact_26 = np.array(sympy.hessian(expr_26, symbols_26).subs(dict(zip(symbols_26, point_26))), dtype=float)
        got_26 = hessian_26_fixed(f_c26, point_26.copy())
        shape_26 = np.shape(got_26) if got_26 is not None else None
        if shape_26 != (n_26, n_26):
            wrong_26.append(f"pour {expr_26} : attendu une matrice {n_26} × {n_26}, reçu {got_26!r}"[:160])
        elif not np.array_equal(np.asarray(got_26), np.asarray(got_26).T):
            wrong_26.append(f"pour {expr_26} : la matrice n'est pas exactement symétrique")
        elif not np.allclose(got_26, exact_26, rtol=1e-5, atol=1e-5):
            wrong_26.append(f"pour {expr_26} en {np.round(point_26, 3).tolist()} : attendu "
                            f"{np.round(exact_26, 4).tolist()}, reçu {np.round(got_26, 4).tolist()}"[:240])
    report_26(not wrong_26, "(2) hessian_26_fixed : quatre fonctions en des points tirés au hasard, symétrique",
              "(2) hessian_26_fixed, " + " ; ".join(wrong_26[:2]))
    exact_g26 = np.array(sympy.hessian(cases_26[-1][0], xyz_26).subs(dict.fromkeys(xyz_26, 0)), dtype=float)
    seen_26 = inertia_26(hessian_26_fixed(g_26, np.zeros(3)))
    report_26(seen_26 == inertia_26(exact_g26), "(2) avec hessian_26_fixed, inertia_26 lit en 0 la même inertie que sur "
                                               "la hessienne exacte de g_26",
              f"(2) avec hessian_26_fixed, inertia_26 rend {seen_26!r} pour g_26 en 0, autre chose qu'avec la hessienne "
              "exacte")
    parts_26.append(2)

with checked("M19.26"):                                       # (3) converges_26_fixed
    wrong_26, tried_26 = [], 0
    for p_26 in np.linspace(-2.5, 2.5, 21):
        for q_26 in np.linspace(-1.35, 1.65, 21):
            if min(abs(abs(q_26) - 1), abs(abs(p_26) - (1 + q_26))) < 1e-9:
                continue                                      # on the border of the triangle: not tried
            tried_26 += 1
            want_26 = bool(np.max(np.abs(np.roots([1.0, -p_26, q_26]))) < 1)
            got_26 = converges_26_fixed(float(p_26), float(q_26))
            if got_26 is None or bool(got_26) != want_26:
                wrong_26.append(f"(p, q) = ({p_26:.2f} ; {q_26:.2f}) : attendu {want_26}, reçu {got_26!r}")
    report_26(not wrong_26, f"(3) converges_26_fixed : juste sur une grille de {tried_26} couples (p, q)",
              f"(3) converges_26_fixed se trompe pour {len(wrong_26)} couple(s) sur {tried_26}, par exemple "
              + " ; ".join(wrong_26[:2]))
    parts_26.append(3)

if len(parts_26) == 3:
    verdict("M19.26", all(results_26), "les trois fonctions corrigées passent tous les cas.",
            "relis les lignes ❌ ci-dessus.")'''

M19_26 = Ex(
    "M19.26", "🐛", 1, 25, "Chasse à l'erreur : un pas réglé sur λmin, une hessienne non symétrique, le module d'une "
    "racine complexe",
    "reconnaître trois erreurs classiques du chapitre qui ne lèvent aucune erreur Python et passent une vérification "
    "mal choisie, puis les corriger.", "fiche §1, §2, §4 et §6", tracks="C, E", given=GIVEN_26,
    body=r"""Un collègue a écrit trois morceaux de code (cellule fournie) ; chacun a l'erreur que nomme le titre, aucun ne lève d'erreur Python, et chacun a passé la vérification que le collègue a faite :
1. `critical_26(A)` doit rendre le pas critique $\frac{2}{\lambda_{\max}}$ d'une matrice symétrique définie positive. Il l'a vérifiée sur $4\mathbf{I}$ : 0,5, juste. Puis il a lancé Richardson sur le système des trois masses `K_26`, `F_26` avec la moitié de ce pas, « par prudence » : les itérés explosent.
2. `hessian_26(f, x, h)` calcule la hessienne par différences centrées, chaque case de la diagonale et au-dessus une seule fois ; `inertia_26(H)` rend l'**inertie** $(n_-, n_0, n_+)$ d'une matrice symétrique, ses nombres de valeurs propres négatives, nulles et positives (`np.linalg.eigvalsh`), une valeur propre comptant pour nulle quand son module est au plus $10^{-8}$ fois le plus grand. Il les a vérifiées sur $\cos x + y^2 + z^2$ en $\mathbf{0}$ : $(1, 0, 2)$, une selle, juste.
3. `converges_26(p, q)` doit dire si toutes les solutions de $u_{k+2} = p\,u_{k+1} - q\,u_k$ tendent vers 0. Il l'a vérifiée sur les trois récurrences de la fiche (§6), $(p, q) = (1 ;\ 0{,}21)$, $(0{,}8 ;\ 0{,}64)$ et $(1{,}5 ;\ -1)$ : juste.

À faire :
- a) avec le pas du collègue, $\omega$ = `critical_26(K_26) / 2` : le facteur $\rho(\omega) = \max_i\lvert 1 - \omega\lambda_i\rvert$ sur les valeurs propres de `K_26` (un nombre, 4 décimales) ;
- (1) écris `critical_26_fixed(A)` ;
- (2) écris `hessian_26_fixed(f, x, h=1e-4)` ; b) avec elle et `inertia_26`, la nature du point critique $\mathbf{0}$ de $g(x, y, z) = x^2 + y^2 + z^2 + 3\sin x\sin y + yz$ (`g_26`) : (A) minimum local ; (B) maximum local ; (C) point selle ; (D) le test ne conclut pas (une lettre entre guillemets) ;
- (3) écris `converges_26_fixed(p, q)` ; c) le module des racines de $r^2 - r + 1{,}2$, c'est-à-dire pour $(p, q) = (1 ;\ 1{,}2)$ (4 décimales).

La vérification essaie tes corrections sur des cas que tu ne vois pas : d'autres matrices, d'autres fonctions et d'autres points, une grille de couples $(p, q)$.""",
    todo='''answer_M19_26a = ...  # a) a number (4 decimals): ρ(ω) = max |1 − ω λ_i| over the eigenvalues of K_26, for the colleague's ω


def critical_26_fixed(A):
    """The critical step 2 / λmax of a symmetric positive definite matrix A."""
    raise NotImplementedError("critical_26_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def hessian_26_fixed(f, x, h=1e-4):
    """The Hessian of f at x by centered differences, exactly symmetric."""
    raise NotImplementedError("hessian_26_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def converges_26_fixed(p, q):
    """True when every solution of u_{k+2} = p u_{k+1} − q u_k tends to 0: both roots of r² − p r + q have a modulus
    < 1."""
    raise NotImplementedError("converges_26_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M19_26c = ...  # c) a number (4 decimals): the modulus of the roots of r² − r + 1.2
answer_M19_26b = ...
with wbm.attempt("M19.26"):          # hessian_26_fixed: ⏳ while it is not written
    answer_M19_26b = ...  # b) "A", "B", "C" or "D": the nature of the critical point 0 of g_26, by your Hessian''',
    check='''for letter, answer in zip("abc", [answer_M19_26a, answer_M19_26b, answer_M19_26c]):
    wbm.check(f"M19.26{letter}", answer)

''' + CHECK_26,
    solution='''lambdas_26 = np.linalg.eigvalsh(K_26)
answer_M19_26a = float(max(abs(1 - omega_26 * lambdas_26)))
print("valeurs propres de K_26 :", np.round(lambdas_26, 4).tolist(), "; ω du collègue :", round(omega_26, 4),
      "; pas critique :", round(2 / lambdas_26[-1], 4))


def critical_26_fixed(A):
    """The critical step 2 / λmax of a symmetric positive definite matrix A."""
    return float(2.0 / np.linalg.eigvalsh(A)[-1])           # eigvalsh: increasing order, λmax is the LAST one


def hessian_26_fixed(f, x, h=1e-4):
    """The Hessian of f at x by centered differences, exactly symmetric."""
    H = hessian_26(f, x, h)                                    # the diagonal and the upper triangle are right
    return np.triu(H) + np.triu(H, k=1).T                      # copy the upper triangle below


def converges_26_fixed(p, q):
    """True when every solution of u_{k+2} = p u_{k+1} − q u_k tends to 0: both roots of r² − p r + q have a modulus
    < 1."""
    delta = p * p - 4 * q
    if delta >= 0:
        roots = [(p + math.sqrt(delta)) / 2, (p - math.sqrt(delta)) / 2]
        return max(abs(r) for r in roots) < 1
    return math.sqrt(q) < 1                                    # conjugate roots: their product q is |r|²


def letter_26(inertia):
    """The nature of a critical point read on the inertia of its Hessian (fiche §2), as the letter of the statement."""
    n_neg, n_zero, n_pos = inertia
    if n_neg and n_pos:
        return "C"                                             # eigenvalues of both signs: a saddle
    if n_zero:
        return "D"                                             # a zero eigenvalue, the others of one sign
    return "A" if n_pos else "B"


answer_M19_26b = letter_26(inertia_26(hessian_26_fixed(g_26, np.zeros(3))))
answer_M19_26c = math.sqrt(1.2)
print("a)", round(answer_M19_26a, 4), " b)", answer_M19_26b, "; inertie :", inertia_26(hessian_26_fixed(g_26, np.zeros(3))), "; le collègue :",
      inertia_26(hessian_26(g_26, np.zeros(3))),
      "; valeurs propres :", np.round(np.linalg.eigvalsh(hessian_26_fixed(g_26, np.zeros(3))), 4).tolist())
print("c)", round(answer_M19_26c, 4), "; (p, q) = (1 ; 1,2) : le collègue dit", converges_26(1.0, 1.2),
      "; |u_k| pour k = 20, 40, 60 :", np.round(np.abs(mymath.iterative.linear_recurrence([1.0, -1.2], [1.0, 0.0], 61)
                                                      [[20, 40, 60]]), 2).tolist())


''' + CHECK_26,
    record='''k_26r = np.array([[3.0, -2.0, 0.0], [-2.0, 5.0, -3.0], [0.0, -3.0, 9.0]])
lambdas_26r = np.linalg.eigvalsh(k_26r)
omega_26r = (2 / lambdas_26r[0]) / 2                                 # the colleague's step: half of 2/λmin
wbm.record("M19.26a", max(abs(1 - omega_26r * lambdas_26r)), decimals=4,
           mistakes={"le collègue prend la MOITIÉ de ce que rend critical_26": max(abs(1 - 2 * omega_26r * lambdas_26r)),
                     "avec le pas du collègue, pas avec un pas juste : ρ(ω) pour ω = critical_26(K_26) / 2":
                         max(abs(1 - lambdas_26r / lambdas_26r[-1]))})
hessian_g_26r = np.array([[2.0, 3.0, 0.0], [3.0, 2.0, 1.0], [0.0, 1.0, 2.0]])   # the exact Hessian of g at 0
assert np.linalg.eigvalsh(hessian_g_26r)[0] < 0 < np.linalg.eigvalsh(hessian_g_26r)[-1]
wbm.record("M19.26b", "C",
           mistakes={"c'est ce que dit la hessienne du collègue : eigvalsh ne lit qu'un triangle de la matrice, et la "
                     "tienne doit être symétrique": "A",
                     "des valeurs propres des deux signes : relis le test du second ordre (fiche §2)": {"B", "D"}})
wbm.record("M19.26c", math.sqrt(1.2), decimals=4,
           mistakes={"le module de racines complexes conjuguées est √q, pas leur partie réelle |p|/2": 0.5,
                     "le module est √q : q est le produit des deux racines conjuguées, le carré de leur module": 1.2})''',
    after=[
        ("md", "**Après la vérification**, dans ta copie : sur $4\\mathbf{I}$, pourquoi la vérification du collègue ne "
               "pouvait-elle pas voir l'erreur (1) ? Que fait `np.linalg.eigvalsh` d'une matrice dont seul le triangle "
               "supérieur est rempli (lis la documentation de son argument `UPLO`), et pourquoi la fonction de test du "
               "collègue, $\\cos x + y^2 + z^2$, ne pouvait-elle pas voir l'erreur (2) ? Les trois récurrences de la "
               "fiche passent le test (3) : pour laquelle des trois $\\lvert p\\rvert/2$ et $\\sqrt q$ sont-ils tous "
               "deux $< 1$, et quelles autres récurrences auraient démasqué l'erreur ?"),
    ],
    note=r"a) $\mathbf{K}$ a pour valeurs propres $1{,}3687$ ; $4{,}9038$ et $10{,}7275$. `eigvalsh` les rend en ordre "
         r"croissant : `[0]` est $\lambda_{\min}$, et le pas du collègue vaut $\frac{1}{\lambda_{\min}} \approx 0{,}7306$, "
         r"près de quatre fois le pas critique $\frac{2}{\lambda_{\max}} \approx 0{,}1864$ ; $\rho = \frac{\lambda_{\max}}"
         r"{\lambda_{\min}} - 1 \approx 6{,}8379$. Sur $4\mathbf{I}$, toutes les valeurs propres sont égales : `[0]` et "
         r"`[-1]` donnent le même pas. b) La hessienne exacte de $g$ en $\mathbf{0}$ est $\begin{pmatrix} 2 & 3 & 0 \\ 3 "
         r"& 2 & 1 \\ 0 & 1 & 2 \end{pmatrix}$, de valeurs propres $2 - \sqrt{10}$, 2 et $2 + \sqrt{10}$ : une selle. "
         r"`eigvalsh` lit par défaut le triangle **inférieur** (`UPLO='L'`) ; celui du collègue est vide, `eigvalsh` voit "
         r"$\operatorname{diag}(2, 2, 2)$ et rend l'inertie $(0, 0, 3)$, celle d'un minimum. Sur $\cos x + y^2 + z^2$, la hessienne est diagonale : "
         r"aucun triangle ne manque. c) $\Delta = 1 - 4{,}8 < 0$ : les racines $0{,}5 \pm 0{,}975i$ ont pour module "
         r"$\sqrt{1{,}2} \approx 1{,}0954 > 1$, et la suite diverge en oscillant ; le collègue lit $\frac{\lvert p\rvert}"
         r"{2} = 0{,}5$. Pour $(0{,}8 ;\ 0{,}64)$, $0{,}4$ et $0{,}8$ sont tous deux $< 1$ : il faut $q > 1$ et "
         r"$\lvert p\rvert < 2$ pour démasquer l'erreur.",
)

GIVEN_27 = '''K_27 = np.array([[4.0, -1.0, 0.0, 0.0],
                 [-1.0, 3.0, -2.0, 0.0],
                 [0.0, -2.0, 3.0, -1.0],
                 [0.0, 0.0, -1.0, 4.0]])       # four masses, five springs of stiffness 3, 1, 2, 1, 3 between two walls
F_27 = np.array([1.0, 0.0, 0.0, 2.0])         # the forces on the masses'''

CHECK_27 = '''with checked("M19.27"):
    results_27 = []

    def report_27(ok, success, failure):
        results_27.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))

    def expected_27(A, b, omega, tol, max_iter):
        """The expected (x, n_iter, converged), by the rule of the statement (the residual by its own recurrence)."""
        x, r = np.zeros(len(b)), b.copy()
        for k in range(max_iter + 1):
            relative = np.linalg.norm(r) / np.linalg.norm(b)
            if relative <= tol:
                return x, k, True
            if not np.isfinite(relative) or relative > 1e10 or k == max_iter:
                return x, k, False
            product = A @ r
            x, r = x + omega * r, r - omega * product

    def run_27(A, b, omega, **options):
        """solve_richardson on copies of A and b, a RuntimeWarning turned into an error, the triple checked."""
        A_copy, b_copy = A.copy(), b.copy()
        with warnings.catch_warnings():
            warnings.simplefilter("error", RuntimeWarning)
            try:
                result = solve_richardson(A_copy, b_copy, omega, **options)
            except RuntimeWarning as warning:
                print(f"❌ Ex M19.27 : un RuntimeWarning ({warning}) : arrête la boucle dès que le résidu relatif "
                      "n'est plus fini ou dépasse 1e10, avant l'overflow")
                raise StopCheck from None
        if not (isinstance(result, tuple) and len(result) == 3):
            print(f"❌ Ex M19.27 : solve_richardson doit rendre le triplet (x, n_iter, converged), reçu {result!r}"[:200])
            raise StopCheck
        if not (np.array_equal(A_copy, A) and np.array_equal(b_copy, b)):
            print("❌ Ex M19.27 : solve_richardson a modifié A ou b : travaille sur des copies")
            raise StopCheck
        return np.asarray(result[0], dtype=float), result[1], result[2]

    def same_27(got, want):
        return (got[1] == want[1] and bool(got[2]) == want[2] and got[0].shape == want[0].shape
                and np.allclose(got[0], want[0], rtol=1e-9, atol=1e-12))

    def shown_27(triple):
        return f"(x, {triple[1]!r}, {triple[2]!r})"

    lambdas_27 = np.linalg.eigvalsh(K_27)
    good_27, bad_27 = 1 / lambdas_27[-1], 1.2 * 2 / lambdas_27[-1]
    cases_27 = [("un bon pas, 1/λmax", K_27, F_27, good_27, {}),
                ("tol = 1e-3", K_27, F_27, good_27, {"tol": 1e-3}),
                ("max_iter = 15", K_27, F_27, good_27, {"max_iter": 15}),
                ("un pas trop grand, 1,2 ω_c", K_27, F_27, bad_27, {})]
    rng_27 = np.random.default_rng(5238)
    for n_27 in (3, 6, 10):                                   # systems drawn at random, at their best step
        Q_27, _ = np.linalg.qr(rng_27.normal(size=(n_27, n_27)))
        values_27 = np.linspace(0.5, rng_27.uniform(4.0, 12.0), n_27)
        A_r27 = Q_27 @ np.diag(values_27) @ Q_27.T
        A_r27 = (A_r27 + A_r27.T) / 2
        cases_27.append((f"un système {n_27} × {n_27} tiré au hasard", A_r27, rng_27.normal(size=n_27),
                         2 / (values_27[0] + values_27[-1]), {}))
    for label_27, A_c27, b_c27, omega_c27, options_27 in cases_27:
        want_27 = expected_27(A_c27, b_c27, omega_c27, options_27.get("tol", 1e-8), options_27.get("max_iter", 10_000))
        got_27 = run_27(A_c27, b_c27, omega_c27, **options_27)
        report_27(same_27(got_27, want_27), f"{label_27} : {shown_27(want_27)}, avec le bon x",
                  f"{label_27} : attendu {shown_27(want_27)}, reçu {shown_27(got_27)}"
                  + ("" if got_27[1] != want_27[1] or got_27[2] != want_27[2] else " avec un autre x"))
    _, n_nan_27, converged_nan_27 = run_27(K_27, F_27, np.nan)
    report_27(not converged_nan_27 and n_nan_27 <= 1,
              f"omega = nan : arrêt après {n_nan_27} pas, converged = {converged_nan_27!r}",
              f"omega = nan : attendu un arrêt dès que le résidu n'est plus un nombre fini (au plus 1 pas) avec "
              f"converged = False, reçu {n_nan_27!r} pas et converged = {converged_nan_27!r}")
    x_27, n_27, converged_27 = run_27(K_27, F_27, good_27)
    gap_27 = np.linalg.norm(x_27 - np.linalg.solve(K_27, F_27)) / np.linalg.norm(np.linalg.solve(K_27, F_27))
    report_27(converged_27 and gap_27 < 1e-7, f"pour K_27 x = F_27, x s'écarte de np.linalg.solve de {gap_27:.1e} en "
                                              f"relatif, après {n_27} itérations",
              f"pour K_27 x = F_27, x s'écarte de np.linalg.solve de {gap_27:.1e} en relatif")
    verdict("M19.27", all(results_27), "le critère d'arrêt s'arrête au bon itéré dans tous les cas, sans warning.",
            "relis les lignes ❌ ci-dessus.")'''

M19_27 = Ex(
    "M19.27", "🛠️", 1, 15, "Un critère d'arrêt : le résidu relatif ‖b − A x‖/‖b‖ et un nombre maximal d'itérations",
    "écrire une itération de Richardson qui suit son résidu par sa propre récurrence, s'arrête d'elle-même au premier "
    "itéré assez précis, et sait dire qu'elle n'a pas convergé.", "fiche §3 et §4 (💻) ; Ex M19.20 ; M12d",
    tracks="C", given=GIVEN_27,
    body=r"""Une méthode itérative utilisable ne fait pas un nombre de pas fixé d'avance : elle s'arrête quand le **résidu relatif** $\frac{\lVert\mathbf{b} - \mathbf{A}\mathbf{x}_k\rVert}{\lVert\mathbf{b}\rVert}$ passe sous une tolérance, et abandonne après un nombre maximal d'itérations (fiche §4, 💻). Calculer $\mathbf{b} - \mathbf{A}\mathbf{x}_k$ à chaque itération en plus du pas coûterait deux produits par $\mathbf{A}$ ; le résidu $\mathbf{r}_k = \mathbf{b} - \mathbf{A}\mathbf{x}_k$ a sa **propre récurrence** : de $\mathbf{x}_{k+1} = \mathbf{x}_k + \omega\,\mathbf{r}_k$, on tire $\mathbf{r}_{k+1} = \mathbf{r}_k - \omega\mathbf{A}\mathbf{r}_k = (\mathbf{I} - \omega\mathbf{A})\,\mathbf{r}_k$, et $\mathbf{r}_0 = \mathbf{b}$ depuis $\mathbf{x}_0 = \mathbf{0}$. Un seul produit par $\mathbf{A}$ par itération suffit.

Écris `solve_richardson(A, b, omega, tol=1e-8, max_iter=10_000)`, qui part de $\mathbf{x}_0 = \mathbf{0}$, $\mathbf{r}_0 = \mathbf{b}$, et rend le triplet `(x, n_iter, converged)` ; pour $k = 0, 1, 2, \ldots$, elle regarde le résidu relatif $\frac{\lVert\mathbf{r}_k\rVert}{\lVert\mathbf{b}\rVert}$ :
- s'il est $\le$ `tol` : elle rend `(x_k, k, True)` ;
- sinon, s'il n'est plus un nombre fini, ou s'il dépasse $10^{10}$ (l'itération diverge : inutile d'attendre l'overflow), ou si $k$ = `max_iter` : elle rend `(x_k, k, False)` ;
- sinon : $\mathbf{p} = \mathbf{A}\mathbf{r}_k$ (le seul produit), $\mathbf{x}_{k+1} = \mathbf{x}_k + \omega\,\mathbf{r}_k$ et $\mathbf{r}_{k+1} = \mathbf{r}_k - \omega\,\mathbf{p}$.

`b` n'est pas nul ; `A` et `b` ne sont pas modifiés ; aucun `RuntimeWarning` (un overflow) ne doit apparaître ; un pas qui n'est pas un nombre (`np.nan`) doit lui aussi s'arrêter, sans boucle infinie, avec `converged` faux.

La cellule fournie donne le système de quatre masses entre deux murs, reliées par cinq ressorts, `K_27` $\mathbf{x}$ = `F_27`. La vérification lance ta fonction sur ce système avec un bon pas ($\frac{1}{\lambda_{\max}}$), avec `tol=1e-3`, avec `max_iter=15`, avec un pas trop grand ($1{,}2\,\omega_c$), avec `omega=np.nan`, puis sur trois systèmes tirés au hasard ; elle compare chaque triplet à celui de la règle ci-dessus, et la solution de `K_27` à `np.linalg.solve` (permis ici, pour vérifier).

Dans ta copie :
1. Démontre $\mathbf{r}_{k+1} = (\mathbf{I} - \omega\mathbf{A})\,\mathbf{r}_k$, puis, depuis $\mathbf{x}_0 = \mathbf{0}$ et pour $\mathbf{A}$ symétrique, $\lVert\mathbf{r}_k\rVert \le \rho(\omega)^k\,\lVert\mathbf{b}\rVert$ (§3 : $\mathbf{I} - \omega\mathbf{A}$ est symétrique, de valeurs propres $1 - \omega\lambda_i$). Pourquoi un résidu relatif au-dessus de 1, a fortiori de $10^{10}$, prouve-t-il que $\rho(\omega) > 1$ ?
2. Avec cette borne, combien d'itérations au plus faut-il pour `K_27` avec $\omega = \frac{1}{\lambda_{\max}}$ et `tol=1e-8` ? Compare au compte de ta fonction.
3. Montre que $\frac{\lVert\mathbf{x}_k - \mathbf{x}^\star\rVert}{\lVert\mathbf{x}^\star\rVert} \le \kappa\,\frac{\lVert\mathbf{r}_k\rVert}{\lVert\mathbf{b}\rVert}$ (avec $\mathbf{x}_k - \mathbf{x}^\star = -\mathbf{A}^{-1}\mathbf{r}_k$ et $\lVert\mathbf{b}\rVert \le \lambda_{\max}\lVert\mathbf{x}^\star\rVert$ ; M12d). Que vaut $\kappa$ pour `K_27`, et que garantit `tol=1e-8` sur l'erreur relative de $\mathbf{x}$ ? Que deviendrait cette garantie pour un système de conditionnement $10^6$ ?""",
    todo='''def solve_richardson(A, b, omega, tol=1e-8, max_iter=10_000):
    """Richardson's iteration from x_0 = 0 for A x = b, its residual r_k = b − A x_k updated by r_{k+1} = r_k − ω A r_k
    (one product by A per iteration), stopped at the first k whose relative residual ‖r_k‖ / ‖b‖ is ≤ tol (converged),
    or is not finite or above 1e10, or when k = max_iter (not converged). Returns (x_k, k, converged)."""
    raise NotImplementedError("solve_richardson n'est pas encore écrite (04_indices.md si tu bloques)")''',
    check=CHECK_27,
    solution='''def solve_richardson(A, b, omega, tol=1e-8, max_iter=10_000):
    """Richardson's iteration from x_0 = 0 for A x = b, its residual r_k = b − A x_k updated by r_{k+1} = r_k − ω A r_k
    (one product by A per iteration), stopped at the first k whose relative residual ‖r_k‖ / ‖b‖ is ≤ tol (converged),
    or is not finite or above 1e10, or when k = max_iter (not converged). Returns (x_k, k, converged)."""
    A, b = np.asarray(A, dtype=float), np.asarray(b, dtype=float)
    norm_b = np.linalg.norm(b)
    x, r, k = np.zeros(len(b)), b.copy(), 0
    while True:
        relative = np.linalg.norm(r) / norm_b
        if relative <= tol:
            return x, k, True
        if not np.isfinite(relative) or relative > 1e10 or k == max_iter:
            return x, k, False
        product = A @ r                                         # the only product by A of the iteration
        x = x + omega * r
        r = r - omega * product                                 # r_{k+1} = (I − ω A) r_k
        k += 1


lambdas_s27 = np.linalg.eigvalsh(K_27)
kappa_s27 = lambdas_s27[-1] / lambdas_s27[0]
for label_s27, omega_s27 in (("1/λmax", 1 / lambdas_s27[-1]), ("ω*", 2 / (lambdas_s27[0] + lambdas_s27[-1])),
                             ("1,2 ω_c", 2.4 / lambdas_s27[-1]), ("nan", np.nan)):
    x_s27, n_s27, converged_s27 = solve_richardson(K_27, F_27, omega_s27)
    print(f"ω = {label_s27} : {n_s27} itérations, converged = {converged_s27}, x = {np.round(x_s27, 6).tolist()}")
rho_s27 = 1 - 1 / kappa_s27                                     # ρ(1/λmax) = 1 − λmin/λmax
print("κ =", round(kappa_s27, 4), "; borne ρᵏ ≤ 1e-8 pour ω = 1/λmax :",
      math.ceil(8 * math.log(10) / -math.log(rho_s27)), "itérations au plus")
x_s27, _, _ = solve_richardson(K_27, F_27, 1 / lambdas_s27[-1])
x_star_s27 = np.linalg.solve(K_27, F_27)
print("erreur relative sur x :", f"{np.linalg.norm(x_s27 - x_star_s27) / np.linalg.norm(x_star_s27):.1e}",
      "; résidu relatif :", f"{np.linalg.norm(F_27 - K_27 @ x_s27) / np.linalg.norm(F_27):.1e}")


''' + CHECK_27,
    note=r"Les valeurs propres de `K_27` vont de $0{,}697$ à $5{,}618$ ($\kappa \approx 8{,}06$). Avec $\omega = "
         r"\frac{1}{\lambda_{\max}}$, $\rho = 1 - \frac{1}{\kappa} \approx 0{,}876$, et la borne $\rho^k \le 10^{-8}$ "
         r"demande au plus 140 itérations ; la fonction en fait 130 (43 avec `tol=1e-3`), car $\mathbf{b}$ n'est pas "
         r"tout entier sur le vecteur propre le plus lent ; au meilleur pas, 70. Avec $1{,}2\,\omega_c$, la composante "
         r"raide du résidu est multipliée par $-1{,}4$ à chaque pas : le résidu relatif dépasse $10^{10}$ après 74 "
         r"itérations, et la fonction s'arrête avant tout overflow. Avec `omega=np.nan`, le premier pas rend un résidu "
         r"`nan`, qui n'est pas fini : arrêt après 1 pas. 1. $\mathbf{r}_{k+1} = \mathbf{b} - \mathbf{A}\mathbf{x}_k - "
         r"\omega\mathbf{A}\mathbf{r}_k = (\mathbf{I} - \omega\mathbf{A})\,\mathbf{r}_k$ ; une matrice symétrique a pour "
         r"norme son rayon spectral (§3), d'où $\lVert\mathbf{r}_k\rVert \le \rho^k\lVert\mathbf{r}_0\rVert = "
         r"\rho^k\lVert\mathbf{b}\rVert$ : si $\rho < 1$, le résidu relatif ne dépasse jamais 1. 3. $\lVert\mathbf{x}_k - "
         r"\mathbf{x}^\star\rVert \le \frac{\lVert\mathbf{r}_k\rVert}{\lambda_{\min}}$ et $\lVert\mathbf{x}^\star\rVert \ge "
         r"\frac{\lVert\mathbf{b}\rVert}{\lambda_{\max}}$ donnent le facteur $\kappa$ : pour `K_27`, `tol=1e-8` garantit "
         r"une erreur relative d'au plus $8 \cdot 10^{-8}$ (on mesure $3 \cdot 10^{-8}$) ; avec $\kappa = 10^6$, le même "
         r"résidu ne garantirait que $10^{-2}$.",
)

GIVEN_28 = '''OMEGA_28 = 5.0                                   # the angular frequency of the oscillator, in rad/s
V0_28 = 1.5                                      # the speed at t = 0, in m/s, from the equilibrium x = 0
H_28 = [round(0.04 * k, 2) for k in range(1, 16)]   # the time steps h = 0.04, 0.08, ..., 0.60 s'''

M19_28 = Ex(
    "M19.28", "🏆", 3, 30, "Défi : le schéma saute-mouton d'un oscillateur, x_{k+1} = (2 − h²Ω²) x_k − x_{k−1}, borné "
    "si et seulement si hΩ < 2",
    "lire la stabilité d'un schéma de la mécanique sur les racines d'une récurrence d'ordre 2, puis la vérifier par "
    "la simulation, jusqu'au cas limite.", "fiche §6 ; M05a ; Ex M19.21", tracks="C", given=GIVEN_28,
    body=r"""Une masse au bout d'un ressort oscille selon $\ddot x = -\Omega^2x$, de pulsation $\Omega$ (en rad/s). Le **schéma saute-mouton** (*leapfrog*), courant dans les simulations de mécanique, remplace la dérivée seconde par la différence centrée de M05a, avec un pas de temps $h$ : $\frac{x_{k+1} - 2x_k + x_{k-1}}{h^2} = -\Omega^2x_k$, soit
$$x_{k+1} = (2 - h^2\Omega^2)\,x_k - x_{k-1},$$
une récurrence d'ordre 2 (fiche §6) avec $p = 2 - h^2\Omega^2$ et $q = 1$. On lâche la masse de sa position d'équilibre avec la vitesse $v_0$ : $x_0 = 0$ et $x_1 = h\,v_0$. La cellule fournie donne $\Omega = 5$ rad/s (`OMEGA_28`), $v_0 = 1{,}5$ m/s (`V0_28`) et quinze pas de temps $h = 0{,}04 ;\ 0{,}08 ;\ \ldots ;\ 0{,}60$ s (`H_28`). L'oscillateur exact a l'amplitude $\frac{v_0}{\Omega} = 0{,}3$ m.

**L'objectif.**
- a) Par la théorie du §6 : les racines de $r^2 - p\,r + 1$ ont pour produit 1 ; elles sont complexes conjuguées, de module 1, quand $\lvert p\rvert < 2$, c'est-à-dire pour $0 < h\Omega < 2$, soit $0 < h < h_c$. Le pas critique $h_c$ (un nombre).
- b) Par la simulation, avec ta `linear_recurrence` : pour chaque $h$ de `H_28`, les 301 termes $x_0, \ldots, x_{300}$, et leur amplitude $\max_k\lvert x_k\rvert$. On dit la suite **bornée** quand cette amplitude ne dépasse pas 1 m. Le plus grand $h$ de `H_28` pour lequel elle l'est (un nombre).
- c) Pour un petit pas, $h = 0{,}03$ s : la période des oscillations du schéma, en pas, $\frac{2\pi}{\theta}$ avec $\cos\theta = 1 - \frac{h^2\Omega^2}{2}$ (2 décimales).
- d) En $h = h_c$ : $\lvert x_{1000}\rvert$, par la simulation (un nombre, 6 décimales).

Dans ta copie : pour $h\Omega > 2$, les racines sont réelles et de produit 1 : pourquoi l'une a-t-elle un module $> 1$ ? En $h\Omega = 2$, quelle est la racine double, et pourquoi $x_k = (\alpha + \beta k)(-1)^k$ grandit-il ici (que vaut $\beta$ pour ce départ) ? Compare c) à la période de l'oscillateur exact, $\frac{2\pi}{\Omega}$, comptée en pas, $\frac{2\pi}{h\Omega}$. Le schéma amortit-il l'oscillation, comme une récurrence de module $< 1$ ? Quel pas de `H_28` garderais-tu pour simuler cet oscillateur, et pourquoi pas le plus grand pas borné ?""",
    todo='''answer_M19_28a = ...  # a) a number: the critical time step h_c, by the theory of §6
answer_M19_28c = ...  # c) a number (2 decimals): the period 2π/θ, in steps, for h = 0.03
answer_M19_28b = answer_M19_28d = ...
with wbm.attempt("M19.28"):          # linear_recurrence: ⏳ while it is not written
    answer_M19_28b = ...  # b) a number: the largest h of H_28 whose 301 terms stay within 1 m
    answer_M19_28d = ...  # d) a number (6 decimals): |x_1000| for h = h_c''',
    check='''for letter, answer in zip("ac", [answer_M19_28a, answer_M19_28c]):
    wbm.check(f"M19.28{letter}", answer)
for letter, answer in zip("bd", [answer_M19_28b, answer_M19_28d]):
    wbm.check(f"M19.28{letter}", answer, computed=True)''',
    solution='''linear_recurrence = mymath.iterative.linear_recurrence


def leapfrog_28(h, n_terms):
    """x_0, ..., x_{n_terms − 1} of the leapfrog scheme of the oscillator, from x_0 = 0, x_1 = h v_0."""
    return linear_recurrence([2 - (h * OMEGA_28) ** 2, -1.0], [0.0, h * V0_28], n_terms)


amplitudes_28 = [float(np.max(np.abs(leapfrog_28(h, 301)))) for h in H_28]
answer_M19_28a = 2 / OMEGA_28
answer_M19_28b = max(h for h, a in zip(H_28, amplitudes_28) if a <= 1)
theta_28 = math.acos(1 - (0.03 * OMEGA_28) ** 2 / 2)
answer_M19_28c = 2 * math.pi / theta_28
answer_M19_28d = float(abs(leapfrog_28(answer_M19_28a, 1001)[1000]))
small_28 = leapfrog_28(0.03, 2001)
ups_28 = np.flatnonzero((small_28[:-1] < 0) & (small_28[1:] >= 0))      # the upward crossings of 0
print("amplitudes :", {h: f"{a:.3g}" for h, a in zip(H_28, amplitudes_28)})
print("a)", answer_M19_28a, " b)", answer_M19_28b, " c)", round(answer_M19_28c, 2), "; 2π/(hΩ) =",
      round(2 * math.pi / (0.03 * OMEGA_28), 2), "; mesurée sur 2 000 pas :", round(float(np.mean(np.diff(ups_28))), 2))
print("d)", round(answer_M19_28d, 1), "; |x_k| / k en h_c :", round(answer_M19_28d / 1000, 6))
fig_28, ax_28 = plt.subplots(figsize=(7.0, 4.0))
ax_28.semilogy([h * OMEGA_28 for h in H_28], amplitudes_28, "o-")
ax_28.axvline(2, color="C3", ls="--", label="hΩ = 2")
ax_28.axhline(1, color="0.5", ls=":", label="1 m")
ax_28.set_xlabel("hΩ")
ax_28.set_ylabel("max |x_k| sur 300 pas (m, échelle log)")
ax_28.legend(fontsize=8)
ax_28.grid(True, which="both", alpha=0.3)
plt.show()''',
    record='''omega_28r, v0_28r = 5.0, 1.5
h_c_28r = 2 / omega_28r
wbm.record("M19.28a", h_c_28r, decimals=6,
           mistakes={"|p| < 2 avec p = 2 − h²Ω² donne h²Ω² < 4 : prends la racine carrée": 4 / omega_28r ** 2,
                     "les racines restent complexes de module 1 tant que |2 − h²Ω²| < 2, pas |1 − h²Ω²| < 1":
                         math.sqrt(2) / omega_28r})


def amplitude_28r(h, n_terms=301):
    """max |x_k| of the leapfrog scheme, written again here (a plain loop)."""
    previous, current, largest = 0.0, h * v0_28r, h * v0_28r
    for _ in range(n_terms - 2):
        previous, current = current, (2 - (h * omega_28r) ** 2) * current - previous
        largest = max(largest, abs(current))
    return largest


grid_28r = [round(0.04 * k, 2) for k in range(1, 16)]
bounded_28r = max(h for h in grid_28r if amplitude_28r(h) <= 1)
assert bounded_28r < h_c_28r and amplitude_28r(h_c_28r) > 100
wbm.record("M19.28b", bounded_28r, decimals=6,
           mistakes={"en hΩ = 2, la racine double −1 fait grandir la suite comme k : elle n'est pas bornée": h_c_28r})
theta_28r = math.acos(1 - (0.03 * omega_28r) ** 2 / 2)
wbm.record("M19.28c", 2 * math.pi / theta_28r, decimals=2,
           mistakes={"la période du schéma est 2π/θ, avec cos θ = 1 − h²Ω²/2 : proche de 2π/(hΩ), sans lui être "
                     "égale": 2 * math.pi / (0.03 * omega_28r)})
x_28r = [0.0, h_c_28r * v0_28r]
while len(x_28r) <= 1000:
    x_28r.append(-2 * x_28r[-1] - x_28r[-2])                           # p = 2 − (h_c Ω)² = −2
wbm.record("M19.28d", abs(x_28r[1000]), decimals=6,
           mistakes={"x₁₀₀₀ est le terme d'indice 1 000 : il faut 1 001 termes": abs(x_28r[999])})''',
    after=[
        ("md", "**Dans ta copie**, réponds aux questions de l'énoncé, puis trace l'amplitude en fonction de $h\\Omega$, "
               "en échelle logarithmique : que se passe-t-il de part et d'autre de $h\\Omega = 2$ ?"),
    ],
    note=r"a) $h_c = \frac{2}{\Omega} = 0{,}4$ s. b) Jusqu'à $h = 0{,}36$ s ($h\Omega = 1{,}8$), l'amplitude reste "
         r"bornée : $\frac{h\,v_0}{\sin\theta}$, soit 0,30 m pour les petits pas et $0{,}69$ m pour $0{,}36$ s ; elle "
         r"grandit quand $h\Omega$ approche 2, car $\sin\theta \to 0$. En $h = 0{,}4$ s, la racine double $-1$ et le "
         r"départ $(0, h\,v_0)$ donnent $x_k = -h\,v_0\,k\,(-1)^k$ : une croissance linéaire, $\lvert x_{300}\rvert = 180$ "
         r"m ; au-delà, une racine réelle de module $> 1$ (produit 1) donne une croissance exponentielle, $10^{115}$ dès "
         r"$h = 0{,}44$ s. c) $\cos\theta = 1 - 0{,}01125$, $\theta \approx 0{,}150141$ : $\frac{2\pi}{\theta} \approx "
         r"41{,}85$ pas, un peu moins que $\frac{2\pi}{h\Omega} \approx 41{,}89$ ; la simulation le confirme. d) "
         r"$\lvert x_{1000}\rvert = 1\,000\,h_c\,v_0 = 600$ m. Les racines "
         r"étant de module exactement 1, le schéma n'amortit pas l'oscillation, comme l'oscillateur exact. Pour une "
         r"simulation fidèle, on garde un pas bien plus petit que $h_c$ (0,04 ou 0,08 s : l'amplitude reste à 1 % ou "
         r"2 % de 0,3 m), pas le plus grand pas borné.",
)

PART_C = Part("C", "Dessiner, déboguer, construire, défier",
              "Fiche §1, §2, §4 et §6. Les itérés de Richardson sur les lignes de niveau ; trois erreurs classiques du "
              "chapitre ; un critère d'arrêt ; un défi : la stabilité du schéma saute-mouton d'un oscillateur. La "
              "vérification de M19.25 s'appuie sur la référence (`ref_iterative`), pour ne pas dépendre de ton code.",
              given=GIVEN_C, exercises=[M19_25, M19_26, M19_27, M19_28])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M19.1 à M19.9, M19.14, M19.15 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            rows.append(ex.table_row(part.key if i == 0 else ""))
    if kind == "exercise":
        title = "# M19 · Hessienne, conditionnement et convergence — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m19_hessienne_convergence/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M19`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M19 · Hessienne, conditionnement et convergence — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : une hessienne et Taylor d'ordre 2, des points critiques en "
               "dimension 3, une itération linéaire, Richardson à la main, le meilleur pas et le nombre d'itérations, "
               "deux récurrences d'ordre 2, un gradient estimé sur un échantillon, deux projections, et deux ponts.\n"
               "- Écrire les quatre fonctions de `mymath/iterative.py` (`numerical_hessian`, `critical_step_size`, "
               "`richardson_iterates`, `linear_recurrence`) et les tester.\n"
               "- Comparer le gradient conjugué de SciPy à Richardson, prédire puis compter des itérations, mesurer leur "
               "croissance avec le conditionnement, dessiner des itérés sur des lignes de niveau, corriger trois "
               "erreurs classiques, écrire un critère d'arrêt, et relever un défi : la stabilité du schéma "
               "saute-mouton.\n\n"
               r"**Rappel express.** Hessienne $H_{ij} = \frac{\partial^2 f}{\partial x_i\partial x_j}$, symétrique ; "
               r"$f(\mathbf{x} + \mathbf{h}) \approx f(\mathbf{x}) + \nabla f^\top\mathbf{h} + \frac12\mathbf{h}^\top"
               r"\mathbf{H}\mathbf{h}$ ; par différences centrées, $h \approx 10^{-4}$. En un point critique : valeurs "
               r"propres toutes $> 0$, minimum ; toutes $< 0$, maximum ; des deux signes, selle. "
               r"$\mathbf{x}_{k+1} = \mathbf{M}\mathbf{x}_k + \mathbf{c}$, $\mathbf{M}$ symétrique : convergence depuis "
               r"tout départ si et seulement si $\rho = \max_i\lvert\lambda_i\rvert < 1$ ; $k \ge \frac{d\ln 10}"
               r"{-\ln\rho}$ pour gagner $d$ décimales. Richardson $\mathbf{x} \leftarrow \mathbf{x} + \omega(\mathbf{b} - "
               r"\mathbf{A}\mathbf{x})$ : $0 < \omega < \frac{2}{\lambda_{\max}}$, $\rho(\omega) = \max(\lvert 1 - "
               r"\omega\lambda_{\min}\rvert, \lvert 1 - \omega\lambda_{\max}\rvert)$, meilleur pas $\frac{2}{\lambda_"
               r"{\min} + \lambda_{\max}}$ de facteur $\frac{\kappa - 1}{\kappa + 1}$, environ $1{,}15\,\kappa\,d$ "
               r"itérations ; gradient conjugué : de l'ordre de $\sqrt\kappa$, au plus $n$. Récurrence $u_{k+2} = p\,"
               r"u_{k+1} - q\,u_k$ : racines de $r^2 - pr + q$, complexes de module $\sqrt q$ si $p^2 < 4q$ ; "
               r"$u_k \to 0$ depuis tout départ si et seulement si $\lvert q\rvert < 1$ et $\lvert p\rvert < 1 + q$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu calculer une hessienne, à la main et par différences centrées, avec un pas bien choisi ?\n"
               "2. Sais-tu classer un point critique de $\\mathbb{R}^n$ par les signes des valeurs propres de sa "
               "hessienne ?\n"
               "3. Sais-tu dire si une itération linéaire converge, et combien d'itérations elle demande ?\n"
               "4. Sais-tu choisir le pas de Richardson, prévoir l'effet du conditionnement, et arrêter l'itération au "
               "bon moment ?\n"
               "5. Sais-tu décider de la convergence d'une récurrence d'ordre 2 par le module de ses racines ?\n\n"
               "**La suite** : le chapitre 19 de workbookIA, qui règle et compare des méthodes de descente par la "
               "courbure, puis M20 (tenseurs, axes et estimateurs pondérés), juste avant le chapitre 20 de workbookIA.")]


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
