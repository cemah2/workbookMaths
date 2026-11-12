#!/usr/bin/env python
"""Build the two notebooks of chapter M17 from a single source (used by Claude).

    python tools/chapters/build_m17.py
    python tools/run_all_notebooks.py chapitres/m17_jacobienne/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m17_jacobienne/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M17.1 to M17.7 and M17.11); parts A to C are the notebook exercises (M17.14 to
M17.23). Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it.
The data are new: synthetic (seeds 5030 to 5049 only, never 16xx nor 17xx) or written in the statements; none is a
test case of tests/test_m17_jacobian.py, an example of the fiche or of a docstring of jacobian.py, nor the data of a
paper exercise. Nothing of workbookIA 17 is used (none of the data that the notes of M17 in the syllabus list to avoid):
the Earth as a sphere, arctan on a grid, products of neighbours, spherical coordinates, a composite of two polynomial
maps, the 60-fold iteration of c x (1 − x) and its fixed points, a warp of the plane, three small polynomial maps, the
inversion of matrices.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, check_unique_keys, guarded,  # noqa: E402,F401
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M17"
FOLDER = "chapitres/m17_jacobienne"

MATRIX = "a matrix (list of rows)"
ROW_RULE = "une ligne par SORTIE et une colonne par entrée"


# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M17.1", "La jacobienne des coordonnées polaires, son déterminant, et l'approximation linéaire près d'un "
                   "point", [
        ("a", "a list of 2 numbers (4 decimals)", "flat(F_1)",
         '''decimals=4, mistakes={"les angles sont en radians : ta calculatrice est-elle réglée en degrés ?": DEGREES_1,
                     "θ = π/6 radian : ne remplace pas π/6 par 30 dans un cosinus qui attend des radians": THIRTY_1}'''),
        ("b", "a matrix (list of rows, 4 decimals)", "rows(J_1)",
         f'''decimals=4, mistakes={{"{ROW_RULE} : la ligne 1 est le gradient de r cos θ": rows(J_1.T),
                     "dérive r sin θ par rapport à θ : le facteur r reste": rows(J_NO_R_1)}}'''),
        ("c", "a number", "int(sympy.simplify(J_1.det()))",
         '''mistakes={"le facteur r de la deuxième colonne reste dans le déterminant": 1,
                     "det = ad − bc : attention au signe du produit des coefficients hors de la diagonale": -4}'''),
        ("d", "a list of 2 numbers (4 decimals)", "flat(LINEAR_1)",
         '''decimals=4, mistakes={"J h, avec h = (0,1 ; 0,05) en colonne : la jacobienne, pas sa transposée":
                         flat(F_1 + J_1.T * H_1),
                     "l'approximation linéaire est f(a) + J h : n'oublie pas f(a)": flat(J_1 * H_1)}'''),
        ("e", "a list of 2 numbers (4 decimals)", "flat(EXACT_1)", "decimals=4"),
        ("f", "a number (4 decimals)", "float((LINEAR_1 - EXACT_1).norm())", "decimals=4"),
        ("g", "a number (4 decimals)", "float(abs(sympy.simplify(J_1.det())) * R(1, 100) * R(2, 100))",
         '''decimals=4, mistakes={"les aires sont multipliées par |det J| : l'aire du petit rectangle ne suffit pas":
                         float(R(1, 100) * R(2, 100))}'''),
    ]),

    Paper("M17.2", "Une fonction appliquée coordonnée par coordonnée : la jacobienne diagonale, et son produit par un "
                   "vecteur", [
        ("a", "a list of 4 numbers", "flat(DG_2)",
         '''decimals=4, mistakes={"la diagonale porte les DÉRIVÉES g′(xᵢ), pas les valeurs g(xᵢ)": flat(G_VALUES_2)}'''),
        ("b", "a list of 4 numbers", "flat([d * v for d, v in zip(DG_2, V_2)])",
         '''decimals=4, mistakes={"J v est un vecteur, une coordonnée par sortie : le produit case par case g′(x) ⊙ v, pas '''
         '''un produit scalaire": [float(sum(d * v for d, v in zip(DG_2, V_2)))]}'''),
        ("c", "an integer", "sum(1 for i in range(4) for j in range(4) if i != j or DG_2[i] == 0)",
         '''mistakes={"compte aussi les zéros de la diagonale : calcule chaque g′(xᵢ)": 12}'''),
        ("d", "an integer", "1000 ** 2 - 1000",
         '''mistakes={"hors de la diagonale : n² coefficients en tout, moins les n de la diagonale": 1000 ** 2,
                     "hors de la diagonale : les deux triangles, au-dessus ET au-dessous": (1000 ** 2 - 1000) // 2}'''),
        ("e", "a list of 2 integers", "[2, 2 * 1000]",
         '''mistakes={"pour la diagonale, toutes les coordonnées bougent ensemble : une seule paire d'évaluations":
                         [2 * 1000, 2 * 1000],
                     "des différences CENTRÉES : deux évaluations par colonne, en x + h e_j et en x − h e_j": [2, 1000],
                     "l'ordre demandé : la diagonale d'abord, puis la jacobienne entière": [2 * 1000, 2]}'''),
        ("f", "a list of 4 numbers (3 decimals)", "flat(DXG_2)",
         '''decimals=3, mistakes={"t g(t) est un produit : sa dérivée a deux termes, g(t) + t g′(t)":
                         flat([x * d for x, d in zip(X_2, DG_2)]),
                     "règle du produit : (t g(t))′ = g(t) + t g′(t), le second terme compte aussi": flat(G_VALUES_2)}'''),
    ]),

    Paper("M17.3", "Dériver une composée de trois applications par le produit de leurs jacobiennes", [
        ("a", "a list of 3 numbers", "flat(Y1_3)"),
        ("b", MATRIX, "rows(J1_3)",
         f'''mistakes={{"{ROW_RULE} : f₁ a 3 sorties et 2 entrées, sa jacobienne 3 lignes et 2 colonnes": '''
         '''rows(J1_3.T)}'''),
        ("c", MATRIX, "rows(J2_3)",
         f'''mistakes={{"{ROW_RULE} : f₂ a 2 sorties et 3 entrées, sa jacobienne 2 lignes et 3 colonnes": '''
         '''rows(J2_3.T),
                     "∂(uv)/∂u = v et ∂(uv)/∂v = u": rows(J2_SWAP_3),
                     "J_f₂ s'évalue en f₁(1, 2) : w = x − y, attention au signe": rows(J2_SIGN_3)}'''),
        ("d", "a matrix (one row: [[a, b]])", "rows(J3_3)",
         '''mistakes={"J_f₃ s'évalue au point où l'on applique f₃, f₂(f₁(1, 2)), pas en les deux premières coordonnées '''
         '''de f₁(1, 2)": rows(J3_EARLY_3),
                     "J_f₃ s'évalue au point où l'on applique f₃, f₂(f₁(1, 2)), pas au point de départ (1, 2)":
                         rows(J3_AT_X_3)}'''),
        ("e", "a list of 2 numbers", "flat(J3_3 * J2_3 * J1_3)",
         '''mistakes={"J_f₃ s'évalue en f₂(f₁(1, 2)) : revois d)": flat(J3_EARLY_3 * J2_3 * J1_3),
                     "J_f₃ s'évalue en f₂(f₁(1, 2)), pas en (1, 2) : revois d)": flat(J3_AT_X_3 * J2_3 * J1_3)}'''),
        ("f", "a list of 2 integers", "COST_3",
         '''mistakes={"l'ordre demandé : (J_f₃ J_f₂) J_f₁ d'abord, puis J_f₃ (J_f₂ J_f₁)": COST_3[::-1]}'''),
    ]),

    Paper("M17.4", "La normalisation x/‖x‖ : sa jacobienne (I − uuᵀ)/‖x‖, et la direction qu'elle écrase", [
        ("a", "a list of 4 numbers", "flat([NORM_4, *U_4])",
         '''decimals=4, mistakes={"‖x‖ est la RACINE de la somme des carrés": flat([NORM_4 ** 2, *(X_4 / NORM_4 ** 2)])}'''),
        ("b", MATRIX, "rows(JN_4)",
         '''decimals=4, mistakes={"divise la projection I − uuᵀ par ‖x‖": rows(P_4),
                     "uuᵀ est une matrice (une colonne fois une ligne), pas le nombre uᵀu = 1": rows(sympy.zeros(3, 3))}'''),
        ("c", "a list of 3 numbers", "flat(JN_4 * X_4)",
         '''decimals=4, mistakes={"J x n'est pas u : calcule (x − (u · x) u) / ‖x‖": flat(U_4)}'''),
        ("d", "a list of 3 numbers", "flat((V_4 - U_4.dot(V_4) * U_4) / NORM_4)",
         '''decimals=4, mistakes={"divise par ‖x‖ = 5": flat(V_4 - U_4.dot(V_4) * U_4)}'''),
        ("e", "an integer", "JN_4.rank()",
         '''mistakes={"J envoie x lui-même sur 0 (revois c) : une direction est écrasée": 3}'''),
        ("f", "a list of 3 numbers", "flat(sorted(JN_4.eigenvals(multiple=True)))",
         '''decimals=4, mistakes={"ce sont les valeurs propres de la projection I − uuᵀ : divise-les par ‖x‖":
                         flat(sorted(P_4.eigenvals(multiple=True)))}'''),
    ]),

    Paper("M17.5", "Le gradient d'une fonction scalaire d'une composée, dans les deux conventions : J_fᵀ ∇L", [
        ("a", "a list of 3 numbers", "flat(Y_5)"),
        ("b", "a list of 3 numbers", "flat(GL_5)",
         '''mistakes={"∇L s'évalue au point intermédiaire y = f(x) : y₁ = x₁ − x₂": flat(GL_AT_X_5)}'''),
        ("c", MATRIX, "rows(JF_5)",
         f'''mistakes={{"{ROW_RULE} : f a 3 sorties et 2 entrées, sa jacobienne 3 lignes et 2 colonnes": '''
         '''rows(JF_5.T)}'''),
        ("d", "a list of 2 numbers", "flat(GL_5 * JF_5)",
         '''mistakes={"∇L s'évalue au point intermédiaire y = f(x) : revois b)": flat(GL_AT_X_5 * JF_5)}'''),
        ("e", "a list of 2 integers", "list(JF_5.T.shape)",
         '''mistakes={"J_f a la forme (3, 2) : sa transposée échange lignes et colonnes": list(JF_5.shape)}'''),
        ("f", "a number", "float((GL_5 * JF_5 * sympy.Matrix([1, 1]))[0])",
         '''decimals=4, mistakes={"la question demande la dérivée de t ↦ (L∘f)(x + t(1, 1)), sans normaliser la '''
         '''direction": float((GL_5 * JF_5 * sympy.Matrix([1, 1]))[0] / sympy.sqrt(2))}'''),
    ]),

    Paper("M17.6", "Dérivées à gauche et à droite d'une fonction définie par morceaux, et la dérivée d'une composée de "
                   "sept copies d'une fonction lisse", [
        ("a", "a number", "int(bill_6(320))",
         '''mistakes={"au-delà de 300 kWh, c'est le troisième morceau qui s'applique : la remise, à 0,1 € le kWh":
                         int(15 + SLOPES_6[1] * (320 - 100)),
                     "au-delà de 300 kWh, le kWh coûte 0,1 €, pas le prix de la première tranche":
                         int(65 + SLOPES_6[0] * (320 - 300)),
                     "chaque tranche a son prix : 65 € pour les 300 premiers kWh, puis le prix de la troisième tranche":
                         int(SLOPES_6[2] * 320)}'''),
        ("b", "a list of 2 numbers", "flat(SLOPES_6[:2])",
         '''decimals=4, mistakes={"à gauche de 100, la pente du morceau de gauche ; à droite, celle du morceau de '''
         '''droite": flat(SLOPES_6[1::-1])}'''),
        ("c", "a list of 2 numbers", "flat(SLOPES_6[1:])",
         '''decimals=4, mistakes={"à gauche de 300, la pente du morceau de gauche ; à droite, celle de la remise":
                         flat(SLOPES_6[:0:-1])}'''),
        ("d", "a list of 2 numbers", "flat([-SLOPES_6[1], SLOPES_6[1]])",
         '''decimals=4, mistakes={"à gauche du point où c(x) = 40, c(x) − 40 est négatif : |c(x) − 40| = 40 − c(x)":
                         flat([SLOPES_6[1], SLOPES_6[1]])}'''),
        ("e", "an irreducible fraction, as text", "str(XS_6[7])",
         '''kind="fraction", simplified=True,
           mistakes={"x₇ : sept applications de g à partir de x₀ = 1, et il en manque une": str(XS_6[6]),
                     "x₇ : sept applications de g à partir de x₀ = 1, et il y en a une de trop": str(XS_6[8])}'''),
        ("f", "an irreducible fraction, as text", "str(DER_6)",
         '''kind="fraction", simplified=True,
           mistakes={"g′(x) = −1/(1 + x)² est négative : compte les signes des sept facteurs": str(-DER_6),
                     "chaque g′ s'évalue en son point de la trajectoire, x₀, x₁, …, x₆, pas toujours en x₀ = 1":
                         str(Fraction(-1, 4) ** 7),
                     "g′(x) = −1/(1 + x)² : n'oublie pas le carré": str(DER_NO_SQUARE_6)}'''),
        ("g", "a number (3 decimals)", "float((3 - sympy.sqrt(5)) / 2)",
         '''decimals=3, mistakes={"c'est x* = 1/(1 + x*) : |g′(x*)| = 1/(1 + x*)² en est le carré":
                         float((sympy.sqrt(5) - 1) / 2)}'''),
    ]),

    Paper("M17.7", "Une loi de Boltzmann à quatre niveaux d'énergie : rapports de populations, énergie moyenne, et la "
                   "température où le niveau fondamental garde la moitié", [
        ("a", "a number (4 decimals)", "float(P1_7[1] / P1_7[0])",
         '''decimals=4, mistakes={"p₁/p₀ = e^(−(E₁ − E₀)/T) : le niveau le plus haut est le MOINS peuplé":
                         float(sympy.E)}'''),
        ("b", "a number (4 decimals)", "float(P1_7[0])",
         '''decimals=4, mistakes={"normalise : divise le poids e⁰ = 1 par Z, la somme des quatre poids": 1.0}'''),
        ("c", "a number (4 decimals)", "float(MEAN_7)",
         '''decimals=4, mistakes={"c'est la moyenne SIMPLE des niveaux : pondère chaque énergie par sa population à '''
         '''T = 1": float(R(sum(E_7), len(E_7)))}'''),
        ("d", "a list of 2 numbers", "flat([0, R(sum(E_7), len(E_7))])",
         '''decimals=6, mistakes={"l'ordre demandé : T → 0 d'abord, puis T → ∞": flat([R(sum(E_7), len(E_7)), 0]),
                     "quand T → ∞, la loi devient uniforme : l'énergie moyenne tend vers la MOYENNE des niveaux, "
                     "(0 + 1 + 2 + 4)/4": flat([0, 2])}'''),
        ("e", "a number (4 decimals)", "float(T_HALF_7)",
         '''decimals=4, mistakes={"la moitié de TOUTE la population : p₁ = 1/Z = 1/2, donc Z = 2, avec les trois '''
         '''niveaux excités": float(1 / sympy.log(2))}'''),
        ("f", "a number (4 decimals)", "float(4 / sympy.log(10))",
         '''decimals=4, mistakes={"e^(−E/T) : l'énergie est DIVISÉE par la température": float(sympy.log(10) / 4),
                     "e^(−4/T) = 1/10 se résout avec le logarithme népérien, ln 10": 4.0}'''),
    ]),

    Paper("M17.11", "Le recuit simulé : une loi de Boltzmann sur cinq configurations, dont on baisse la température", [
        ("a", "a number (4 decimals)", "float(tours_11(4)[1])",
         '''decimals=4, mistakes={"normalise : divise le poids de B par la somme des cinq poids": 1.0}'''),
        ("b", "a number (2 decimals)", "float(tours_11(1)[1])",
         '''decimals=2, mistakes={"normalise : divise le poids de B par la somme des cinq poids": 1.0}'''),
        ("c", "a number (2 decimals)", "float(sum(l * p for l, p in zip(LENGTHS_11, tours_11(1))))",
         '''decimals=2, mistakes={"pondère chaque longueur par sa probabilité à T = 1 : la moyenne simple des cinq '''
         '''longueurs ne dépend pas de T": float(R(sum(LENGTHS_11), len(LENGTHS_11))),
                     "tu as calculé avec les écarts à 38 km : ajoute 38 à la moyenne des écarts":
                         float(sum((l - 38) * p for l, p in zip(LENGTHS_11, tours_11(1))))}'''),
        ("d", "a number (4 decimals)", "float(tours_11(1)[1] + tours_11(1)[3])",
         '''decimals=4, mistakes={"B ou D : additionne les deux probabilités": float(tours_11(1)[1]),
                     "B ou D : la probabilité de B compte aussi": float(tours_11(1)[3])}'''),
        ("e", "a number (4 decimals)", "float(sympy.exp(-2))",
         '''decimals=4, mistakes={"e^(−Δ/T) : l'écart Δ est DIVISÉ par la température": float(sympy.exp(-R(1, 2))),
                     "la température compte : e^(−Δ/T) avec T = 0,5": float(sympy.exp(-1))}'''),
        ("f", "a number", "1.0",
         '''decimals=4, mistakes={"un passage vers une tournée plus COURTE est toujours accepté": float(sympy.exp(2)),
                     "la formule e^(−Δ/T) ne vaut que pour une tournée plus LONGUE ; une tournée plus courte est "
                     "toujours acceptée": float(sympy.exp(-2))}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly (SymPy, fractions) from the statements
import math
from fractions import Fraction

import sympy

R = sympy.Rational


def rows(M):
    """A SymPy matrix as the list of its rows (Python ints, floats for the other numbers)."""
    return [[int(v) if v.is_Integer else float(v) for v in M.row(i)] for i in range(M.rows)]


def flat(values):
    """SymPy numbers (a row, a column, a list) as a flat list (Python ints, floats for the other numbers)."""
    return [int(v) if sympy.sympify(v).is_Integer else float(v) for v in values]


R_1, T_1 = sympy.Integer(4), sympy.pi / 6                                                        # M17.1
F_1 = sympy.Matrix([R_1 * sympy.cos(T_1), R_1 * sympy.sin(T_1)])
J_1 = sympy.Matrix([[sympy.cos(T_1), -R_1 * sympy.sin(T_1)], [sympy.sin(T_1), R_1 * sympy.cos(T_1)]])
J_NO_R_1 = sympy.Matrix([[sympy.cos(T_1), -sympy.sin(T_1)], [sympy.sin(T_1), sympy.cos(T_1)]])
H_1 = sympy.Matrix([R(1, 10), R(1, 20)])                       # the move (dr, dθ) of d) and e)
LINEAR_1 = F_1 + J_1 * H_1
EXACT_1 = sympy.Matrix([R(41, 10) * sympy.cos(T_1 + R(1, 20)), R(41, 10) * sympy.sin(T_1 + R(1, 20))])
DEGREES_1 = [4 * math.cos(math.radians(math.pi / 6)), 4 * math.sin(math.radians(math.pi / 6))]   # a calculator in °
THIRTY_1 = [4 * math.cos(30), 4 * math.sin(30)]                # 30 read as radians
t_ = sympy.Symbol("t")                                                                           # M17.2
G_2 = sympy.log(1 + t_ ** 2)
X_2, V_2 = [1, -2, 0, 3], [2, 1, -5, R(1, 2)]
DG_2 = [sympy.diff(G_2, t_).subs(t_, x) for x in X_2]          # g′(t) = 2t / (1 + t²)
G_VALUES_2 = [G_2.subs(t_, x) for x in X_2]
DXG_2 = [sympy.diff(t_ * G_2, t_).subs(t_, x) for x in X_2]    # (t g(t))′ = g(t) + t g′(t)
x_, y_, u_, v_, w_, a_, b_ = sympy.symbols("x y u v w a b")                                       # M17.3
F1_3 = sympy.Matrix([x_ + y_, x_ * y_, x_ - y_])
F2_3 = sympy.Matrix([u_ * v_, v_ + w_ ** 2])
F3_3 = sympy.Matrix([a_ ** 2 - 3 * b_])
P_3 = {x_: 1, y_: 2}
Y1_3 = F1_3.subs(P_3)                                          # f1(1, 2)
Q_3 = dict(zip((u_, v_, w_), Y1_3))
Y2_3 = F2_3.subs(Q_3)                                          # f2(f1(1, 2))
J1_3 = F1_3.jacobian([x_, y_]).subs(P_3)
J2_3 = F2_3.jacobian([u_, v_, w_]).subs(Q_3)
J2_SWAP_3 = sympy.Matrix([[u_, v_, 0], [0, 1, 2 * w_]]).subs(Q_3)   # the two partial derivatives of uv swapped
J2_SIGN_3 = F2_3.jacobian([u_, v_, w_]).subs({u_: Y1_3[0], v_: Y1_3[1], w_: -Y1_3[2]})
J3_JAC_3 = F3_3.jacobian([a_, b_])
J3_3 = J3_JAC_3.subs(dict(zip((a_, b_), Y2_3)))
J3_EARLY_3 = J3_JAC_3.subs({a_: Y1_3[0], b_: Y1_3[1]})       # at the first two coordinates of f1(1, 2)
J3_AT_X_3 = J3_JAC_3.subs({a_: 1, b_: 2})                    # at the starting point
COST_3 = [J3_3.rows * J3_3.cols * J2_3.cols + J3_3.rows * J2_3.cols * J1_3.cols,     # (J3 J2) J1
          J2_3.rows * J2_3.cols * J1_3.cols + J3_3.rows * J3_3.cols * J1_3.cols]     # J3 (J2 J1)
X_4, V_4 = sympy.Matrix([3, 0, 4]), sympy.Matrix([0, 2, 1])                                      # M17.4
NORM_4 = X_4.norm()
U_4 = X_4 / NORM_4
P_4 = sympy.eye(3) - U_4 * U_4.T                               # the orthogonal projection on the plane orthogonal to u
JN_4 = P_4 / NORM_4
x1_, x2_, y1_, y2_, y3_ = sympy.symbols("x1 x2 y1 y2 y3")                                        # M17.5
F_5 = sympy.Matrix([x1_ - x2_, x1_ * x2_, x2_ ** 2])
L_5 = y1_ ** 2 + 3 * y2_ - y3_
P_5 = {x1_: 2, x2_: -1}
Y_5 = F_5.subs(P_5)
GRAD_L_5 = sympy.Matrix([[sympy.diff(L_5, y) for y in (y1_, y2_, y3_)]])     # a row, as in MML
GL_5 = GRAD_L_5.subs(dict(zip((y1_, y2_, y3_), Y_5)))
GL_AT_X_5 = GRAD_L_5.subs({y1_: 2, y2_: Y_5[1], y3_: Y_5[2]})             # y1 read as x1 = 2
JF_5 = F_5.jacobian([x1_, x2_]).subs(P_5)
SLOPES_6 = (Fraction(15, 100), Fraction(25, 100), Fraction(1, 10))                               # M17.6


def bill_6(x):
    """c(x), the bill in € for x kWh, in exact fractions."""
    x = Fraction(x)
    if x <= 100:
        return SLOPES_6[0] * x
    if x <= 300:
        return 15 + SLOPES_6[1] * (x - 100)
    return 65 + SLOPES_6[2] * (x - 300)


XS_6 = [Fraction(1)]                                           # x_0 = 1, then x_{k+1} = 1 / (1 + x_k), up to x_8
for _ in range(8):
    XS_6.append(1 / (1 + XS_6[-1]))
DER_6 = math.prod(Fraction(-1) / (1 + XS_6[k]) ** 2 for k in range(7))      # the product of g′(x_k), k = 0 … 6
DER_NO_SQUARE_6 = math.prod(Fraction(-1) / (1 + XS_6[k]) for k in range(7))
E_7 = (0, 1, 2, 4)                                                                               # M17.7


def populations_7(T):
    """The Boltzmann populations of the levels E_7 at the temperature T (exact SymPy numbers)."""
    weights = [sympy.exp(-sympy.Integer(E) / T) for E in E_7]
    return [w / sum(weights) for w in weights]


P1_7 = populations_7(sympy.Integer(1))
MEAN_7 = sum(E * p for E, p in zip(E_7, P1_7))
T_SYMBOL_7 = sympy.Symbol("T", positive=True)
T_HALF_7 = sympy.nsolve(sum(sympy.exp(-sympy.Integer(E) / T_SYMBOL_7) for E in E_7[1:]) - 1, T_SYMBOL_7, 1.8,
                        prec=30)                               # p_0 = 1/2 ⇔ e^(−1/T) + e^(−2/T) + e^(−4/T) = 1
LENGTHS_11 = (41, 38, 45, 39, 40)                                                                # M17.11: A to E


def tours_11(T):
    """The Boltzmann probabilities of the five tours at the temperature T (exact SymPy numbers)."""
    weights = [sympy.exp(-(sympy.Integer(length) - 38) / sympy.sympify(T)) for length in LENGTHS_11]
    return [w / sum(weights) for w in weights]'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M17.1 à M17.7, M17.11)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une liste `[0.2, -1]` ;\n"
               "- une matrice comme la liste de ses **lignes** : `[[1, 0], [-2, 3]]` ; un nombre décimal s'y écrit "
               "avec un point, `[[0.5, 1], [0, 2]]`, ou comme un calcul, `[[1/2, 1], [0, 2]]` ;\n"
               "- une fraction irréductible entre guillemets, `\"3/7\"`, quand la question le dit.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M17.14 to M17.16)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import inspect
import math
import time
import warnings

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import sympy

from wbm.nbtools import StopCheck, checked, drawn, fr, run_pytest_group, verdict

TEST_M17 = "tests/test_m17_jacobian.py"          # the tests of mymath/jacobian.py'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M17")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/jacobian.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "NumPy est permis, mais ni SymPy ni `scipy.differentiate` (les tests comparent tes résultats aux leurs, et un "
         "test vérifie que ton module ne les importe pas). Ne modifie jamais le `x` reçu : travaille sur une copie en "
         "flottants, `np.array(x, dtype=float)` (une liste d'entiers doit être acceptée). Une valeur de `f` qui est un "
         "nombre compte comme un tableau de longueur 1 (`np.atleast_1d`). Les matrices et les vecteurs se rendent en "
         "tableaux NumPy de flottants.")


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of jacobian.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group(TEST_M17, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_M17, "{keyword}", impl="ref")')]


GIVEN_14 = '''EARTH_RADIUS_14 = 6371.0                       # km: the Earth taken as a sphere
LYON_14 = np.radians([45.76, 4.84])            # Lyon: (latitude φ, longitude λ), converted into radians


def sphere_14(p):
    """S(φ, λ): the point of latitude p[0] and longitude p[1] (radians) of the sphere, in km."""
    phi, lam = p
    return EARTH_RADIUS_14 * np.array([np.cos(phi) * np.cos(lam), np.cos(phi) * np.sin(lam), np.sin(phi)])'''

M17_14 = Ex(
    "M17.14", "🔨", 2, 20, "La jacobienne par différences centrées, colonne par colonne · `numerical_jacobian`",
    "programmer la jacobienne d'une application de $\\mathbb{R}^n$ dans $\\mathbb{R}^m$ par différences centrées, et "
    "lire ses colonnes sur une carte de la Terre.", "fiche §1 ; M05a", tracks="C, E", mymath="jacobian.py",
    given=GIVEN_14,
    body=HOWTO + r"""

Écris `numerical_jacobian(f, x, h=1e-5)` (fiche §1), en suivant sa docstring : `ValueError` si `x` n'est pas un tableau 1-D non vide, si `h` n'est pas un nombre $> 0$, ou si les valeurs de `f` ne sont pas des tableaux 1-D, toutes de la même longueur ; sinon la matrice $(m, n)$ dont la colonne $j$ est
$$\frac{\mathbf{f}(\mathbf{x} + h\,\mathbf{e}_j) - \mathbf{f}(\mathbf{x} - h\,\mathbf{e}_j)}{2h},$$
où $\mathbf{e}_j$ est le $j$-ième vecteur de la base canonique. La colonne $j$ est la vitesse de $\mathbf{f}(\mathbf{x})$ quand seule $x_j$ varie (fiche §1) ; la ligne $i$ est le gradient de la sortie $f_i$. La matrice entière coûte $2n$ évaluations de $\mathbf{f}$.

**L'usage.** On prend la Terre pour une sphère de rayon $R = 6\,371$ km. Le point de latitude $\varphi$ et de longitude $\lambda$ (en radians) est
$$\mathbf{S}(\varphi, \lambda) = R\,(\cos\varphi\cos\lambda,\ \cos\varphi\sin\lambda,\ \sin\varphi),$$
une application de $\mathbb{R}^2$ dans $\mathbb{R}^3$ (cellule fournie : `sphere_14`, et Lyon, $\varphi = 45{,}76°$ et $\lambda = 4{,}84°$, convertis en radians dans `LYON_14`). La colonne 1 de $\mathbf{J}_{\mathbf{S}}$ dit comment le point bouge (en km par radian) quand la latitude bouge, la colonne 2 quand la longitude bouge. Avec ta fonction, calcule la jacobienne $(3, 2)$ de $\mathbf{S}$ à Lyon, puis :
- a) la longueur, en km, d'un degré de longitude à cette latitude : la norme de la colonne 2, fois $\frac{\pi}{180}$ (2 décimales) ;
- b) la longueur, en km, d'un degré de latitude (2 décimales).

Dans ta copie : écris $\mathbf{J}_{\mathbf{S}}(\varphi, \lambda)$ à la main, et montre que la colonne 1 a la norme $R$ et la colonne 2 la norme $R\cos\varphi$. Pourquoi a) vaut-elle $R\cos\varphi\,\frac{\pi}{180}$ (sur quel cercle le point se déplace-t-il quand seule la longitude bouge, et quel est son rayon) ? Que vaudrait a) à l'équateur, et au pôle ? Combien d'évaluations de $\mathbf{S}$ ta fonction a-t-elle faites ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("numerical_jacobian or module_uses") + [
        ("md", "**L'usage** : la jacobienne de la sphère à Lyon, et ses deux colonnes."),
        ("todo", '''answer_M17_14a = answer_M17_14b = ...
with wbm.attempt("M17.14"):          # if you call numerical_jacobian here: ⏳ while it is not written
    jacobian_14 = ...     # the (3, 2) Jacobian of sphere_14 at LYON_14, by mymath.jacobian.numerical_jacobian
    answer_M17_14a = ...  # a) a number (2 decimals): the length of one degree of longitude, in km
    answer_M17_14b = ...  # b) a number (2 decimals): the length of one degree of latitude, in km'''),
        ("check", '''wbm.check("M17.14a", answer_M17_14a, computed=True)
wbm.check("M17.14b", answer_M17_14b, computed=True)'''),
        ("solution", '''numerical_jacobian = mymath.jacobian.numerical_jacobian
jacobian_14 = numerical_jacobian(sphere_14, LYON_14)
answer_M17_14a = float(np.linalg.norm(jacobian_14[:, 1]) * math.pi / 180)    # column 2: the longitude moves
answer_M17_14b = float(np.linalg.norm(jacobian_14[:, 0]) * math.pi / 180)    # column 1: the latitude moves
print("J =", np.round(jacobian_14, 2).tolist())
print("a)", round(answer_M17_14a, 2), "km ; b)", round(answer_M17_14b, 2), "km")
print("R cos φ π/180 =", round(EARTH_RADIUS_14 * math.cos(LYON_14[0]) * math.pi / 180, 4), "; R π/180 =",
      round(EARTH_RADIUS_14 * math.pi / 180, 4), "; à l'équateur, a) vaudrait aussi", round(EARTH_RADIUS_14 * math.pi / 180, 2))'''),
        ("record", '''latitude_14r = math.radians(45.76)
wbm.record("M17.14a", 6371 * math.cos(latitude_14r) * math.pi / 180, decimals=2,
           mistakes={"la longitude est la 2ᵉ entrée de S : sa colonne est la 2ᵉ de la jacobienne (une colonne par "
                     "entrée)": 6371 * math.pi / 180,
                     "la norme d'une colonne est en km par RADIAN : un degré vaut π/180 radian":
                         6371 * math.cos(latitude_14r)})
wbm.record("M17.14b", 6371 * math.pi / 180, decimals=2,
           mistakes={"la latitude est la 1ʳᵉ entrée de S : sa colonne est la 1ʳᵉ de la jacobienne (une colonne par "
                     "entrée)": 6371 * math.cos(latitude_14r) * math.pi / 180,
                     "la norme d'une colonne est en km par RADIAN : un degré vaut π/180 radian": 6371.0})'''),
    ],
    note=r"$\mathbf{J}_{\mathbf{S}} = R\begin{pmatrix} -\sin\varphi\cos\lambda & -\cos\varphi\sin\lambda \\ "
         r"-\sin\varphi\sin\lambda & \cos\varphi\cos\lambda \\ \cos\varphi & 0 \end{pmatrix}$ : la colonne 1 a la "
         r"norme $R$, la colonne 2 la norme $R\cos\varphi$. Quand seule la longitude bouge, le point parcourt le "
         r"parallèle, un cercle de rayon $R\cos\varphi$ ; quand seule la latitude bouge, le méridien, de rayon $R$. "
         r"a) $6\,371 \times \cos(45{,}76°) \times \frac{\pi}{180} \approx 77{,}58$ km ; b) $6\,371 \times "
         r"\frac{\pi}{180} \approx 111{,}19$ km (la valeur tombe tout près d'une limite d'arrondi : 111,19 et 111,20 "
         r"sont acceptés). À l'équateur, a) vaudrait aussi 111,19 km ; au pôle, 0 : tous les méridiens s'y rejoignent. "
         r"La fonction a fait $2n = 4$ évaluations de $\mathbf{S}$.",
)

GIVEN_15 = '''X_15 = np.linspace(-3.0, 3.0, 300)       # 300 points evenly spaced from -3 to 3


class Counted:
    """A map that counts its calls: Counted(g)(p) is g(p), and .calls is the number of calls made so far."""

    def __init__(self, g):
        self.g, self.calls = g, 0

    def __call__(self, p):
        self.calls += 1
        return self.g(p)'''

M17_15 = Ex(
    "M17.15", "🔨", 1, 15, "Une jacobienne diagonale avec une seule paire d'évaluations · `diagonal_jacobian`",
    "programmer la jacobienne diagonale d'une fonction appliquée coordonnée par coordonnée avec deux évaluations, et "
    "comparer son coût à celui de la jacobienne entière.", "fiche §2 ; Ex M17.14", tracks="C, E", mymath="jacobian.py",
    given=GIVEN_15,
    body=r"""Écris `diagonal_jacobian(f, x, h=1e-5)` (fiche §2), en suivant sa docstring : `ValueError` si `x` n'est pas un tableau 1-D non vide, si `h` n'est pas un nombre $> 0$, ou si $\mathbf{f}(\mathbf{x})$ n'a pas la longueur de $\mathbf{x}$ ; sinon la matrice diagonale $(n, n)$ de la jacobienne d'une fonction appliquée coordonnée par coordonnée. Puisque la sortie $i$ ne dépend que de $x_i$, on **bouge toutes les coordonnées à la fois** : la coordonnée $i$ de $\frac{\mathbf{f}(\mathbf{x} + h\mathbf{1}) - \mathbf{f}(\mathbf{x} - h\mathbf{1})}{2h}$ est la dérivée $g'(x_i)$, et `np.diag` en fait la matrice. Deux évaluations de $\mathbf{f}$ en tout. La fonction ne vérifie pas que $\mathbf{f}$ est appliquée coordonnée par coordonnée : sur une autre application, elle rend une diagonale fausse (un test le vérifie).

**L'usage.** $g = \arctan$, appliquée aux 300 points `X_15`, régulièrement espacés de $-3$ à $3$. La cellule fournie donne aussi `Counted` : `Counted(np.arctan)` se comporte comme `np.arctan` et compte ses appels dans son attribut `calls` (crée un nouveau compteur pour chaque appel de tes fonctions). Avec tes fonctions, calcule :
- a) le nombre d'évaluations de $\mathbf{f}$ faites par `diagonal_jacobian`, puis par `numerical_jacobian`, sur `X_15` (une liste de 2 entiers) ;
- b) la trace de la jacobienne de $\arctan$ en `X_15` (4 décimales) ;
- c) vrai ou faux : la plus grande différence, en valeur absolue, entre la diagonale de `numerical_jacobian` et celle de `diagonal_jacobian` est sous $10^{-8}$.

Dans ta copie : pourquoi la trace vaut-elle $\sum_i\frac{1}{1 + x_i^2}$ ? Les 300 points sont espacés d'environ $\frac{6}{300}$ : compare b) à la valeur approchée $\frac{300}{6}\int_{-3}^{3}\frac{\mathrm{d}t}{1 + t^2}$. Pourquoi les deux diagonales de c) sont-elles si proches (quels nombres chaque fonction calcule-t-elle pour la coordonnée $i$) ? Combien de coefficients a la matrice de `numerical_jacobian`, et combien sont non nuls ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("diagonal_jacobian") + [
        ("md", "**L'usage** : la diagonale de la jacobienne de arctan, et ce qu'elle coûte."),
        ("todo", '''answer_M17_15a = answer_M17_15b = answer_M17_15c = ...
with wbm.attempt("M17.15"):          # if you call your functions here: ⏳ while they are not written
    answer_M17_15a = ...  # a) a list of 2 integers: the evaluations of f by diagonal_jacobian, then by numerical_jacobian
    answer_M17_15b = ...  # b) a number (4 decimals): the trace of the Jacobian of arctan at X_15
    answer_M17_15c = ...  # c) True or False'''),
        ("check", '''for letter, answer in zip("abc", [answer_M17_15a, answer_M17_15b, answer_M17_15c]):
    wbm.check(f"M17.15{letter}", answer, computed=True)'''),
        ("solution", '''diagonal_jacobian = mymath.jacobian.diagonal_jacobian
numerical_jacobian = mymath.jacobian.numerical_jacobian
counted_diagonal_15, counted_full_15 = Counted(np.arctan), Counted(np.arctan)
diagonal_15 = diagonal_jacobian(counted_diagonal_15, X_15)
full_15 = numerical_jacobian(counted_full_15, X_15)
answer_M17_15a = [counted_diagonal_15.calls, counted_full_15.calls]
answer_M17_15b = float(np.trace(diagonal_15))
answer_M17_15c = bool(np.max(np.abs(np.diag(full_15) - np.diag(diagonal_15))) < 1e-8)
print("a)", answer_M17_15a, " b)", round(answer_M17_15b, 4), " c)", answer_M17_15c,
      f"(plus grand écart : {np.max(np.abs(np.diag(full_15) - np.diag(diagonal_15))):.1e})")
print("approximation par l'intégrale, 50 × 2 arctan 3 ≈", round(100 * math.atan(3), 4))
print("coefficients de la jacobienne entière :", full_15.size, "; non nuls :", int(np.count_nonzero(full_15)))'''),
        ("record", '''from fractions import Fraction

points_15r = [Fraction(-3) + Fraction(6 * i, 299) for i in range(300)]
wbm.record("M17.15a", [2, 2 * 300],
           mistakes={"diagonal_jacobian bouge toutes les coordonnées à la fois : une seule paire d'évaluations en tout":
                         [2 * 300, 2 * 300],
                     "numerical_jacobian évalue f DEUX fois par colonne (en x + h e_j et en x − h e_j)": [2, 300],
                     "numerical_jacobian fait une évaluation de trop (f(x) seul ?) : deux par colonne suffisent, et la "
                     "longueur m se lit sur la première différence": [2, 2 * 300 + 1],
                     "diagonal_jacobian fait une évaluation de trop (f(x) seul ?) : f(x + h) et f(x − h) suffisent":
                         [3, 2 * 300],
                     "tes deux fonctions font chacune une évaluation de trop (f(x) seul ?) : les différences centrées "
                     "n'en ont pas besoin": [3, 2 * 300 + 1]})
wbm.record("M17.15b", float(sum(1 / (1 + t * t) for t in points_15r)), decimals=4,     # Σ 1 / (1 + x_i²), exactly
           mistakes={"la trace somme la diagonale, les DÉRIVÉES arctan′(xᵢ), pas les valeurs arctan(xᵢ)": 0.0,
                     "c'est la valeur approchée par l'intégrale : b) demande la trace elle-même, calculée avec ta "
                     "fonction": 100 * math.atan(3)})
wbm.record("M17.15c", True,
           mistakes={"compare les deux DIAGONALES (np.diag de chaque matrice), en valeur absolue : pour la coordonnée "
                     "i, les deux fonctions calculent la même différence centrée": False})'''),
    ],
    note=r"a) Deux évaluations pour la diagonale, $2n = 600$ pour la jacobienne entière, dont $300^2 = 90\,000$ "
         r"coefficients n'en ont que 300 non nuls. b) $\sum_i\frac{1}{1 + x_i^2} \approx 124{,}5880$, proche de "
         r"$\frac{300}{6}\int_{-3}^{3}\frac{\mathrm{d}t}{1 + t^2} = 100\arctan 3 \approx 124{,}90$ (l'écart vient de "
         r"l'espacement exact, $\frac{6}{299}$, et des bords). c) Vrai, et l'écart est même nul : pour la coordonnée "
         r"$i$, les deux fonctions calculent $\frac{\arctan(x_i + h) - \arctan(x_i - h)}{2h}$, les mêmes nombres "
         r"flottants ; seules changent les autres coordonnées, que la sortie $i$ ne voit pas.",
)

GIVEN_16 = '''N_16 = 2000
X_16 = np.linspace(-1.0, 1.0, N_16)
V_16 = np.cos(np.linspace(0.0, 2 * np.pi, N_16))


def neighbours_16(p):
    """f(p)_i = p_i p_{i+1}, the indices taken modulo n: the last coordinate is multiplied by the first one."""
    return p * np.roll(p, -1)'''

M17_16 = Ex(
    "M17.16", "🔨", 1, 15, "Un produit jacobienne-vecteur sans former la jacobienne · `jacobian_vector_product`",
    "programmer un produit jacobienne-vecteur avec deux évaluations, sans former la jacobienne, et mesurer ce qu'il "
    "économise.", "fiche §5 ; Ex M17.14", tracks="C", mymath="jacobian.py", given=GIVEN_16,
    body=r"""Écris `jacobian_vector_product(f, x, v, h=1e-5)` (fiche §5), en suivant sa docstring : `ValueError` si `x` ou `v` n'est pas un tableau 1-D, s'ils sont vides ou de longueurs différentes, ou si `h` n'est pas un nombre $> 0$ ; sinon les $m$ coordonnées de
$$\mathbf{J}_{\mathbf{f}}(\mathbf{x})\,\mathbf{v} \approx \frac{\mathbf{f}(\mathbf{x} + h\mathbf{v}) - \mathbf{f}(\mathbf{x} - h\mathbf{v})}{2h},$$
la dérivée de toutes les sorties quand on part de $\mathbf{x}$ dans la direction $\mathbf{v}$ : deux évaluations de $\mathbf{f}$, quel que soit $n$, sans former la matrice.

**L'usage.** $\mathbf{f}(\mathbf{x})_i = x_ix_{i+1}$, les indices pris modulo $n$ (la dernière coordonnée est multipliée par la première) : `neighbours_16`, sur $n = 2\,000$ coordonnées, au point `X_16` (2 000 points régulièrement espacés de $-1$ à $1$) et dans la direction `V_16` ($\cos$ de 2 000 points régulièrement espacés de $0$ à $2\pi$). Avec tes fonctions, et `Counted` (M17.15), calcule :
- a) la norme euclidienne de $\mathbf{J}\mathbf{v}$ (2 décimales) ;
- b) le nombre d'évaluations de $\mathbf{f}$ faites par `jacobian_vector_product`, puis par `numerical_jacobian` (pour former $\mathbf{J}$, avant le produit `J @ v`) : une liste de 2 entiers.

Pour b), ta `numerical_jacobian` forme une matrice de 4 millions de coefficients : une fraction de seconde si tu remplis une matrice préparée par `np.zeros`, ou si tu empiles les colonnes une seule fois à la fin. Si elle prend plus de quelques secondes, compte ses évaluations sur les 200 premières coordonnées, et déduis b) de ce que coûte une colonne.

Dans ta copie : écris $(\mathbf{J}\mathbf{v})_i = v_ix_{i+1} + x_iv_{i+1}$ (quelles cases de la ligne $i$ de $\mathbf{J}$ sont non nulles ?), et compte les multiplications de cette formule, contre $n^2$ pour `J @ v` avec la matrice formée. Combien de coefficients de $\mathbf{J}$ sont non nuls ? Pourquoi la formule des différences donne-t-elle ici $\mathbf{J}\mathbf{v}$ exactement, aux arrondis près (de quel degré est chaque sortie) ?""",
    todo=LOAD_LEARNER,
    solution=LOAD_REF,
    after=tests_cells("jacobian_vector_product") + [
        ("md", "**L'usage** : un produit jacobienne-vecteur sur 2 000 coordonnées, avec et sans la matrice."),
        ("todo", '''answer_M17_16a = answer_M17_16b = ...
with wbm.attempt("M17.16"):          # if you call your functions here: ⏳ while they are not written
    answer_M17_16a = ...  # a) a number (2 decimals): the norm of J v
    answer_M17_16b = ...  # b) a list of 2 integers: the evaluations of f by jacobian_vector_product, then by
                          #    numerical_jacobian'''),
        ("check", '''wbm.check("M17.16a", answer_M17_16a, computed=True)
wbm.check("M17.16b", answer_M17_16b, computed=True)'''),
        ("solution", '''jacobian_vector_product = mymath.jacobian.jacobian_vector_product
numerical_jacobian = mymath.jacobian.numerical_jacobian
counted_product_16, counted_full_16 = Counted(neighbours_16), Counted(neighbours_16)
start_16 = time.perf_counter()
product_16 = jacobian_vector_product(counted_product_16, X_16, V_16)
middle_16 = time.perf_counter()
full_16 = numerical_jacobian(counted_full_16, X_16)
end_16 = time.perf_counter()
answer_M17_16a = float(np.linalg.norm(product_16))
answer_M17_16b = [counted_product_16.calls, counted_full_16.calls]
by_hand_16 = V_16 * np.roll(X_16, -1) + X_16 * np.roll(V_16, -1)           # (J v)_i = v_i x_{i+1} + x_i v_{i+1}
print("a)", round(answer_M17_16a, 2), " b)", answer_M17_16b)
print(f"durées : {1000 * (middle_16 - start_16):.2f} ms pour J v, {1000 * (end_16 - middle_16):.0f} ms pour former J")
print("écart avec la formule :", f"{np.max(np.abs(product_16 - by_hand_16)):.1e}", "; avec J @ v :",
      f"{np.max(np.abs(full_16 @ V_16 - by_hand_16)):.1e}")
print("coefficients non nuls de J :", int(np.count_nonzero(np.abs(full_16) > 1e-9)), "sur", full_16.size)'''),
        ("record", '''x_16r = np.linspace(-1.0, 1.0, 2000)
v_16r = np.cos(np.linspace(0.0, 2 * np.pi, 2000))
first_16r, second_16r = v_16r * np.roll(x_16r, -1), x_16r * np.roll(v_16r, -1)     # the two terms of (J v)_i
wbm.record("M17.16a", float(np.linalg.norm(first_16r + second_16r)), decimals=2,
           mistakes={"la sortie i dépend de x_i ET de x_{i+1} : (J v)_i a deux termes":
                         float(np.linalg.norm(first_16r)),
                     "une différence centrée se divise par 2h, l'écart entre x + h v et x − h v":
                         float(2 * np.linalg.norm(first_16r + second_16r)),
                     "J v est la dérivée des sorties dans la direction v, pas les sorties elles-mêmes":
                         float(np.linalg.norm(x_16r * np.roll(x_16r, -1)))})
wbm.record("M17.16b", [2, 2 * 2000],
           mistakes={"jacobian_vector_product bouge x dans la seule direction v : deux évaluations en tout":
                         [2 * 2000, 2 * 2000],
                     "numerical_jacobian évalue f DEUX fois par colonne (en x + h e_j et en x − h e_j)": [2, 2000],
                     "numerical_jacobian fait une évaluation de trop (f(x) seul ?) : deux par colonne suffisent":
                         [2, 2 * 2000 + 1],
                     "jacobian_vector_product fait une évaluation de trop (f(x) seul ?) : f(x + h v) et f(x − h v) "
                     "suffisent": [3, 2 * 2000],
                     "tes deux fonctions font chacune une évaluation de trop (f(x) seul ?) : les différences centrées "
                     "n'en ont pas besoin": [3, 2 * 2000 + 1]})'''),
    ],
    note=r"La ligne $i$ de $\mathbf{J}$ n'a que deux cases non nulles, $\frac{\partial f_i}{\partial x_i} = x_{i+1}$ "
         r"et $\frac{\partial f_i}{\partial x_{i+1}} = x_i$ : $(\mathbf{J}\mathbf{v})_i = v_ix_{i+1} + x_iv_{i+1}$, "
         r"$2n = 4\,000$ multiplications, contre $n^2 = 4$ millions pour `J @ v` avec la matrice formée, dont 4 000 "
         r"coefficients seulement sont non nuls. a) $\lVert\mathbf{J}\mathbf{v}\rVert \approx 39{,}18$. b) Deux "
         r"évaluations contre $2n = 4\,000$. Chaque sortie est de degré 2 : dans "
         r"$\mathbf{f}(\mathbf{x} + h\mathbf{v}) - \mathbf{f}(\mathbf{x} - h\mathbf{v})$, les termes en $h^2$ "
         r"s'annulent, et la différence centrée donne $\mathbf{J}\mathbf{v}$ exactement, aux arrondis près. Ici "
         r"$\lVert\mathbf{v}\rVert \approx 32$, loin de la norme 1 que conseille la docstring : sans conséquence pour "
         r"une application de degré 2, mais à surveiller en général.",
)

PART_A = Part("A", "Ta librairie : la jacobienne numérique, sa diagonale, et un produit jacobienne-vecteur",
              "Fiche §1, §2 et §5. Les trois fonctions de `mymath/jacobian.py`, leurs tests, et un usage de chacune.",
              given=TOOLS, exercises=[M17_14, M17_15, M17_16])

# ---------------------------------------------------------------------------
# Notebook exercises: tools, a prediction, an experiment and a figure (M17.17 to M17.20)
# ---------------------------------------------------------------------------
GIVEN_B = '''ref_jacobian = wbm.load_mymath("ref", alias="mymath_ref").jacobian   # the reference: the jacobians of the checks'''

GIVEN_17 = '''from scipy.differentiate import jacobian as scipy_jacobian

r, theta, phi = sympy.symbols("r theta phi")          # the symbols of a): keep these names
POINT_17 = np.array([2.0, math.pi / 3, math.pi / 4])   # the point (r, θ, φ) of b) to d)


def spherical_17(p):
    """(r, θ, φ) ↦ (r sin θ cos φ, r sin θ sin φ, r cos θ): p is one point, of shape (3,), or an array (3, k, ...) of
    points in columns, as scipy.differentiate.jacobian passes them."""
    return np.array([p[0] * np.sin(p[1]) * np.cos(p[2]), p[0] * np.sin(p[1]) * np.sin(p[2]), p[0] * np.cos(p[1])])'''

M17_17 = Ex(
    "M17.17", "📦", 1, 15, "`sympy.Matrix.jacobian` et `scipy.differentiate.jacobian` contre ta jacobienne numérique",
    "calculer une jacobienne exacte avec SymPy et une jacobienne numérique soignée avec SciPy, et les comparer à ta "
    "`numerical_jacobian`.", "fiche §1 et §3 ; Ex M17.14", tracks="C, E", given=GIVEN_17,
    body=r"""Deux bibliothèques calculent des jacobiennes :
- **SymPy**, exactement : pour une colonne `M = sympy.Matrix([...])` d'expressions, `M.jacobian([r, theta, phi])` rend la jacobienne, une ligne par expression et une colonne par variable (la convention de la fiche) ; `sympy.simplify(...)` simplifie une expression, et `J.subs({r: 2, theta: sympy.pi / 3, phi: sympy.pi / 4})` évalue la matrice en un point (puis `np.array(..., dtype=float)`).
- **SciPy**, numériquement mais avec soin : `scipy.differentiate.jacobian(f, x)` (SciPy 1.15 et après ; importée sous le nom `scipy_jacobian` dans la cellule fournie) rend un objet dont l'attribut `df` est la jacobienne $(m, n)$, `error` une estimation de l'erreur de chaque coefficient, et `nfev` le nombre d'évaluations de $\mathbf{f}$ faites pour chaque coefficient. ⚠️ Pour aller vite, SciPy appelle $\mathbf{f}$ sur **beaucoup de points à la fois** : $\mathbf{f}$ reçoit un tableau de forme $(n, k, \ldots)$, **une colonne par point**, et doit rendre un tableau de forme $(m, k, \ldots)$. Une fonction écrite avec `p[0]`, `p[1]`, `p[2]` et les fonctions de NumPy (`np.sin`, jamais `math.sin`) le fait d'elle-même : c'est le cas de `spherical_17` (cellule fournie), qui sert aussi à ta `numerical_jacobian`.

Les **coordonnées sphériques** : $(r, \theta, \varphi) \mapsto (r\sin\theta\cos\varphi,\ r\sin\theta\sin\varphi,\ r\cos\theta)$, où $\theta$ est l'angle avec l'axe vertical et $\varphi$ l'angle autour de cet axe. Calcule :
- a) avec SymPy et les symboles `r`, `theta`, `phi` de la cellule fournie : le déterminant de la jacobienne, simplifié (une expression SymPy, ou son texte) ;
- b) vrai ou faux : au point $(2 ;\ \frac{\pi}{3} ;\ \frac{\pi}{4})$ (`POINT_17`), la plus grande différence, en valeur absolue, entre ta `numerical_jacobian` et la jacobienne de SymPy évaluée en ce point est sous $10^{-8}$ ;
- c) vrai ou faux : la même chose entre ta `numerical_jacobian` et le `df` de `scipy_jacobian` ;
- d) vrai ou faux : pour **chaque** coefficient, `scipy_jacobian` a fait plus de 6 évaluations de la fonction (son `nfev`), alors que ta `numerical_jacobian` en fait 6 en tout.

Dans ta copie : écris la jacobienne, et retrouve le déterminant à la main (développe selon la 3ᵉ ligne). Que dit $\lvert\det\mathbf{J}\rvert$ du volume de l'image d'une petite boîte $[r, r + \delta r] \times [\theta, \theta + \delta\theta] \times [\varphi, \varphi + \delta\varphi]$ (fiche §1) ? Pourquoi s'annule-t-il sur l'axe vertical, et en $r = 0$ ? Compare l'erreur estimée par SciPy (`error`) à l'écart entre ta jacobienne et celle de SymPy : que gagne SciPy avec ses évaluations en plus ?""",
    todo='''answer_M17_17a = answer_M17_17b = answer_M17_17c = answer_M17_17d = ...
answer_M17_17a = ...  # a) a SymPy expression of r, theta, phi (or its text): the simplified determinant
with wbm.attempt("M17.17"):          # numerical_jacobian: ⏳ while it is not written
    answer_M17_17b = ...  # b) True or False
    answer_M17_17c = ...  # c) True or False
    answer_M17_17d = ...  # d) True or False''',
    check='''wbm.check("M17.17a", answer_M17_17a)
for letter, answer in zip("bcd", [answer_M17_17b, answer_M17_17c, answer_M17_17d]):
    wbm.check(f"M17.17{letter}", answer, computed=True)''',
    solution='''column_17 = sympy.Matrix([r * sympy.sin(theta) * sympy.cos(phi), r * sympy.sin(theta) * sympy.sin(phi),
                          r * sympy.cos(theta)])
jacobian_sym_17 = column_17.jacobian([r, theta, phi])
answer_M17_17a = sympy.simplify(jacobian_sym_17.det())
exact_17 = np.array(jacobian_sym_17.subs({r: 2, theta: sympy.pi / 3, phi: sympy.pi / 4}).evalf(), dtype=float)
mine_17 = mymath.jacobian.numerical_jacobian(spherical_17, POINT_17)
result_17 = scipy_jacobian(spherical_17, POINT_17)
answer_M17_17b = bool(np.max(np.abs(mine_17 - exact_17)) < 1e-8)
answer_M17_17c = bool(np.max(np.abs(mine_17 - result_17.df)) < 1e-8)
answer_M17_17d = bool(np.all(result_17.nfev > 6))
print("J =", jacobian_sym_17)
print("a)", answer_M17_17a, " b)", answer_M17_17b, " c)", answer_M17_17c, " d)", answer_M17_17d)
print(f"écarts à SymPy : numerical_jacobian {np.max(np.abs(mine_17 - exact_17)):.1e}, "
      f"scipy {np.max(np.abs(result_17.df - exact_17)):.1e} ; erreur estimée par scipy {np.max(result_17.error):.1e}")
print("nfev de scipy :", result_17.nfev.tolist())''',
    record='''wbm.record("M17.17a", "r**2*sin(theta)", kind="expr", variables=("r", "theta", "phi"),
           mistakes={"développe le déterminant jusqu'au bout : deux colonnes de la jacobienne ont le facteur r":
                         "r*sin(theta)",
                     "attention au signe d'un des termes du développement": "-r**2*sin(theta)"})
wbm.record("M17.17b", True,
           mistakes={"évalue la jacobienne de SymPy au même point que la tienne, puis compare les deux matrices "
                     "coefficient par coefficient, en valeur absolue": False})
wbm.record("M17.17c", True,
           mistakes={"compare ta jacobienne à l'attribut df du résultat de scipy_jacobian, coefficient par coefficient, "
                     "en valeur absolue": False})
wbm.record("M17.17d", True,
           mistakes={"regarde le plus petit coefficient de nfev, le tableau des évaluations faites pour chaque "
                     "coefficient": False})''',
    note=r"$\mathbf{J} = \begin{pmatrix} \sin\theta\cos\varphi & r\cos\theta\cos\varphi & -r\sin\theta\sin\varphi "
         r"\\ \sin\theta\sin\varphi & r\cos\theta\sin\varphi & r\sin\theta\cos\varphi \\ \cos\theta & -r\sin\theta & "
         r"0 \end{pmatrix}$, de déterminant $r^2\sin\theta$ : une petite boîte de côtés $\delta r$, $\delta\theta$, "
         r"$\delta\varphi$ a pour image un petit volume d'environ $r^2\sin\theta\,\delta r\,\delta\theta\,\delta\varphi$. "
         r"Il s'annule sur l'axe vertical ($\sin\theta = 0$ : $\varphi$ n'y bouge plus le point) et en $r = 0$ (tous "
         r"les angles donnent l'origine). b) et c) Vrai : ta jacobienne est juste à quelques $10^{-11}$, SciPy à "
         r"quelques $10^{-13}$. d) Vrai : SciPy fait au moins 11 évaluations par coefficient (une extrapolation de "
         r"Richardson d'ordre 8, avec des pas qui diminuent jusqu'à la tolérance), réparties sur une dizaine d'appels "
         r"de la fonction sur des tableaux de points ; son estimation d'erreur, `error`, dit jusqu'où le croire. Le "
         r"coefficient $(3, 3)$, nul, n'atteint pas la tolérance relative : SciPy le signale dans `success`.",
)

GIVEN_18 = '''def f_18(x):
    """f(x) = (x1 x2, x3², x4 + x1), of R^4 into R^3."""
    return np.array([x[0] * x[1], x[2] ** 2, x[3] + x[0]])


def g_18(y):
    """g(y) = (y1 + y2, y3²), of R^3 into R^2."""
    return np.array([y[0] + y[1], y[2] ** 2])


def composite_18(x):
    """g ∘ f, of R^4 into R^2."""
    return g_18(f_18(x))'''

EXPERIMENT_18 = '''rng_18 = np.random.default_rng(5031)
zero_18 = None
for x_18 in rng_18.normal(size=(3, 4)):              # three points of R^4 drawn at random
    jacobian_18 = ref_jacobian.numerical_jacobian(composite_18, x_18)
    print(f"en x = {np.round(x_18, 3).tolist()} : forme {jacobian_18.shape}, J =", np.round(jacobian_18, 3).tolist())
    zero_18 = (np.abs(jacobian_18) < 1e-9) if zero_18 is None else zero_18 & (np.abs(jacobian_18) < 1e-9)
print("cases nulles aux trois points (True) :", zero_18.tolist(), "; il y en a", int(zero_18.sum()))'''

M17_18 = Ex(
    "M17.18", "🔮", 1, 10, "Prédire la forme et les zéros de la jacobienne d'une composée, puis vérifier",
    "prévoir la forme et les coefficients nuls de la jacobienne d'une composée à partir de celles de ses facteurs, puis "
    "le vérifier en trois points.", "fiche §3", tracks="C, E", hypothesis=True, given=GIVEN_18,
    body=r"""Deux applications : $\mathbf{f}(\mathbf{x}) = (x_1x_2,\ x_3^2,\ x_4 + x_1)$, de $\mathbb{R}^4$ dans $\mathbb{R}^3$, et $\mathbf{g}(\mathbf{y}) = (y_1 + y_2,\ y_3^2)$, de $\mathbb{R}^3$ dans $\mathbb{R}^2$ (cellule fournie : `f_18`, `g_18` et `composite_18` $= \mathbf{g} \circ \mathbf{f}$). Raisonne sur les formes, et sur les cases toujours nulles de $\mathbf{J}_{\mathbf{f}}$ et de $\mathbf{J}_{\mathbf{g}}$ : par la règle de la chaîne (fiche §3), le coefficient $(i, j)$ de $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}$ est une somme sur les chemins $x_j \to y_k \to$ sortie $i$. Pour chaque question, choisis le numéro de la bonne réponse :
- a) la forme de $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}$ : (1) $(4, 2)$ ; (2) $(2, 4)$ ; (3) $(3, 3)$ ;
- b) le nombre de coefficients de $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}$ qui sont nuls en **tout** point $\mathbf{x}$ : (1) 0 ; (2) 5 ; (3) 3 ;
- c) la sortie 2 de $\mathbf{g} \circ \mathbf{f}$ dépend-elle de $x_3$ ? (1) oui ; (2) non.

**Avant d'exécuter quoi que ce soit**, écris tes trois prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience : la jacobienne numérique de $\mathbf{g} \circ \mathbf{f}$ (celle de la référence) en trois points tirés au hasard (graine 5031), et les cases nulles aux trois points.""",
    todo='''prediction_M17_18a = ...  # a) 1, 2 or 3, written BEFORE running the experiment below
prediction_M17_18b = ...  # b) 1, 2 or 3
prediction_M17_18c = ...  # c) 1 or 2''',
    check='''for letter, prediction in zip("abc", [prediction_M17_18a, prediction_M17_18b, prediction_M17_18c]):
    wbm.check(f"M17.18{letter}", prediction)''',
    record='''wbm.record("M17.18a", 2, prediction=True, choices=[1, 2, 3])
wbm.record("M17.18b", 3, prediction=True, choices=[1, 2, 3])
wbm.record("M17.18c", 2, prediction=True, choices=[1, 2])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes trois prédictions écrites."),
        ("todo", guarded(EXPERIMENT_18, [f"prediction_M17_18{letter}" for letter in "abc"],
                         "⏳ Écris d'abord tes trois prédictions, puis exécute à nouveau.")),
        ("solution", EXPERIMENT_18),
        ("md", "**Après l'expérience**, dans ta copie : écris $\\mathbf{J}_{\\mathbf{f}}(\\mathbf{x})$, de forme "
               "$(3, 4)$, et $\\mathbf{J}_{\\mathbf{g}}(\\mathbf{y})$, de forme $(2, 3)$, puis leur produit, avec "
               "$\\mathbf{y} = \\mathbf{f}(\\mathbf{x})$. Pour chaque case toujours nulle du produit, dis quel chemin "
               "$x_j \\to y_k \\to$ sortie $i$ manque. Une case du produit peut-elle être nulle en tout point alors que "
               "les termes de sa somme ne le sont pas ? La case $(1, 3)$ est nulle en certains points seulement : "
               "lesquels, et pourquoi ne compte-t-elle pas dans b) ?"),
    ],
    note=r"$\mathbf{J}_{\mathbf{f}} = \begin{pmatrix} x_2 & x_1 & 0 & 0 \\ 0 & 0 & 2x_3 & 0 \\ 1 & 0 & 0 & 1 "
         r"\end{pmatrix}$ et $\mathbf{J}_{\mathbf{g}} = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 2y_3 \end{pmatrix}$, d'où "
         r"$\mathbf{J}_{\mathbf{g} \circ \mathbf{f}} = \begin{pmatrix} x_2 & x_1 & 2x_3 & 0 \\ 2(x_4 + x_1) & 0 & 0 & "
         r"2(x_4 + x_1) \end{pmatrix}$ : a) la forme $(2, 4)$ (choix 2), une ligne par sortie de $\mathbf{g}$, une "
         r"colonne par entrée de $\mathbf{f}$ ; b) trois cases nulles en tout point (choix 3) : la sortie 1 ne voit "
         r"pas $x_4$ (le seul chemin passe par $y_3$, que la sortie 1 ignore), la sortie 2 ne voit ni $x_2$ ni $x_3$ "
         r"(elle ne passe que par $y_3 = x_4 + x_1$) ; c) non (choix 2). Ici, chaque case nulle vient d'un chemin "
         r"absent ; en général, une somme de termes non nuls peut aussi s'annuler partout par compensation. La case "
         r"$(1, 3)$, $2x_3$, ne s'annule qu'en $x_3 = 0$.",
)

GIVEN_19 = '''X0_19, N_STEPS_19 = 0.3, 60
C_VALUES_19 = (1.4, 2.6, 2.8, 4.0)           # the values of c of the figure
STARTS_19 = np.sin(np.pi / 2 * np.linspace(0.0, 1.0, 10002)[1:-1]) ** 2    # the 10 000 starts of c), in ]0, 1[,
                                             # spread as the points of a long trajectory of φ_4 (closer near 0 and 1)


def parabola_19(c):
    """The map φ_c(x) = c x (1 − x) and its derivative φ_c′(x) = c (1 − 2x), for numbers or arrays."""
    return (lambda x: c * x * (1 - x)), (lambda x: c * (1 - 2 * x))'''

FIGURE_19 = '''fig, ax = plt.subplots(figsize=(7.5, 4.2))
try:
    steps_19 = np.arange(N_STEPS_19 + 1)
    for c_19, colour_19 in zip(C_VALUES_19, ("C0", "C1", "C2", "C3")):
        xs_19, ds_19 = (np.asarray(a, dtype=float) for a in iterate_with_derivative(*parabola_19(c_19), X0_19,
                                                                                     N_STEPS_19))
        shown_19 = f"{c_19:g}".replace(".", ",")
        ax.semilogy(steps_19, np.abs(ds_19), "-", color=colour_19, lw=1.6, label=f"c = {shown_19}")
        if c_19 < 3:                                     # the slope ln|φ_c′(x*)| = ln|2 − c|, through the last point
            ax.semilogy(steps_19, abs(ds_19[-1]) * abs(2 - c_19) ** (steps_19 - N_STEPS_19), ":", color=colour_19,
                        lw=1.2)
    ax.set_xlabel("itération k")
    ax.set_ylabel("|D_k| = |dx_k / dx_0| (échelle log)")
    ax.set_title("pointillés : la pente ln|2 − c| du point fixe", fontsize=9)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
except BaseException:
    plt.close(fig)
    raise
plt.show()'''

M17_19 = Ex(
    "M17.19", "🔬", 2, 20, "Une longue composition : une dérivée qui s'éteint ou explose selon la pente au point fixe",
    "suivre la dérivée d'une longue itération par la règle de la chaîne, et relier sa vitesse d'extinction ou "
    "d'explosion à la pente au point fixe.", "fiche §6 ; R5", tracks="C", given=GIVEN_19,
    body=r"""On itère $\varphi_c(x) = cx(1 - x)$ sur $[0 ; 1]$ à partir de $x_0 = 0{,}3$ : $x_{k+1} = \varphi_c(x_k)$, donc $x_k$ est la composée de $k$ copies de $\varphi_c$, appliquée à $x_0$. Par la règle de la chaîne (fiche §6), sa dérivée par rapport au départ est le produit des dérivées le long de la trajectoire :
$$D_k = \frac{\mathrm{d}x_k}{\mathrm{d}x_0} = \prod_{j < k}\varphi_c'(x_j), \qquad D_0 = 1, \qquad D_{k+1} = \varphi_c'(x_k)\,D_k.$$
Écris `iterate_with_derivative(phi, dphi, x0, n_steps)`, qui rend deux tableaux de longueur `n_steps + 1` : les $x_k$ et les $D_k$, de $k = 0$ à `n_steps` (la cellule fournie donne $\varphi_c$ et $\varphi_c'$ par `parabola_19(c)`).

Pour $1 < c < 3$, la trajectoire converge vers le point fixe $x^* = 1 - \frac{1}{c}$, où la pente vaut $\varphi_c'(x^*) = 2 - c$ : les derniers facteurs du produit valent presque $2 - c$, et $D_k$ s'éteint comme $\lvert 2 - c\rvert^k$. Pour $c = 4$, le point fixe $x^* = 0{,}75$ est **repoussant** (pente $-2$) : la trajectoire ne s'en approche pas, elle erre dans $[0 ; 1]$, et $D_k$ grandit en moyenne comme $2^k$, alors que les $x_k$ restent dans $[0 ; 1]$. Calcule, avec $L = 60$ itérations :
- a) pour $c = 2{,}6$, la pente $\varphi_c'(x^*)$ au point fixe (un nombre) ;
- b) pour $c = 2{,}6$, $\lvert D_{60}\rvert^{1/60}$ (3 décimales) ;
- c) pour $c = 4$, le taux moyen de croissance $\frac{1}{60}\ln\lvert D_{60}\rvert$, en **moyenne sur les 10 000 départs** `STARTS_19` (2 décimales) ;
- d) vrai ou faux : pour $c = 4$, les trajectoires parties de $0{,}3$ et de $0{,}3 + 10^{-10}$ sont à plus de $0{,}01$ l'une de l'autre après 40 itérations.

Pourquoi une moyenne en c) : pour $c = 4$, les erreurs d'arrondi des flottants sont, elles aussi, multipliées par 2 à chaque pas en moyenne ; après une cinquantaine d'itérations, la trajectoire calculée n'est plus celle qu'on calculerait exactement, et le taux d'un seul départ dépend de ces détails (d'une écriture de $\varphi_c$ à une autre, par exemple). La moyenne sur beaucoup de départs, elle, n'en dépend presque plus. Les 10 000 départs de `STARTS_19` (cellule fournie) sont plus serrés près de 0 et de 1 : ils sont répartis comme les points d'une très longue trajectoire de $\varphi_4$, ce qui rend la moyenne indépendante des premiers pas. Ta fonction peut prendre un `x0` qui est un tableau de départs, si tu l'écris avec des opérations de NumPy ; sinon, fais une boucle sur les départs (moins d'une seconde).

Une cellule trace ensuite, avec ta fonction, $\lvert D_k\rvert$ en échelle logarithmique pour $c = 1{,}4$ ; $2{,}6$ ; $2{,}8$ et $4$, avec, en pointillés, des droites de pente $\ln\lvert 2 - c\rvert$ pour $c < 3$.""",
    todo='''def iterate_with_derivative(phi, dphi, x0, n_steps):
    """The arrays (x_0, ..., x_n) and (D_0, ..., D_n), n = n_steps: x_{k+1} = phi(x_k), D_0 = 1 and
    D_{k+1} = dphi(x_k) D_k, the derivative dx_k/dx_0 by the chain rule."""
    raise NotImplementedError("iterate_with_derivative n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M17_19a = answer_M17_19b = answer_M17_19c = answer_M17_19d = ...
answer_M17_19a = ...  # a) a number: the slope φ_c′(x*) at the fixed point, c = 2.6
with wbm.attempt("M17.19"):          # if you call iterate_with_derivative here: ⏳ while it is not written
    answer_M17_19b = ...  # b) a number (3 decimals): |D_60|^(1/60), c = 2.6
    answer_M17_19c = ...  # c) a number (2 decimals): the mean over STARTS_19 of ln|D_60| / 60, c = 4
    answer_M17_19d = ...  # d) True or False''',
    check='''wbm.check("M17.19a", answer_M17_19a)
for letter, answer in zip("bcd", [answer_M17_19b, answer_M17_19c, answer_M17_19d]):
    wbm.check(f"M17.19{letter}", answer, computed=True)

with checked("M17.19 figure"):
''' + "\n".join("    " + line if line else "" for line in FIGURE_19.splitlines()),
    solution='''def iterate_with_derivative(phi, dphi, x0, n_steps):
    """The arrays (x_0, ..., x_n) and (D_0, ..., D_n), n = n_steps: x_{k+1} = phi(x_k), D_0 = 1 and
    D_{k+1} = dphi(x_k) D_k, the derivative dx_k/dx_0 by the chain rule."""
    xs, ds = [x0], [np.ones_like(x0, dtype=float)]           # x0 may be a number or an array of starts
    for _ in range(n_steps):
        ds.append(dphi(xs[-1]) * ds[-1])                     # the derivative at the point BEFORE the step
        xs.append(phi(xs[-1]))
    return np.array(xs, dtype=float), np.array(ds, dtype=float)


phi_25, dphi_25 = parabola_19(2.6)
phi_4, dphi_4 = parabola_19(4.0)
answer_M17_19a = round(dphi_25(1 - 1 / 2.6), 12)                # φ′(x*) = 2 − c
xs_25, ds_25 = iterate_with_derivative(phi_25, dphi_25, X0_19, N_STEPS_19)
answer_M17_19b = float(abs(ds_25[-1]) ** (1 / N_STEPS_19))
xs_4, ds_4 = iterate_with_derivative(phi_4, dphi_4, STARTS_19, N_STEPS_19)      # 10 000 starts at once
rates_19 = np.log(np.abs(ds_4[-1])) / N_STEPS_19
answer_M17_19c = float(np.mean(rates_19))
near_19, _ = iterate_with_derivative(phi_4, dphi_4, X0_19 + 1e-10, N_STEPS_19)
far_19, _ = iterate_with_derivative(phi_4, dphi_4, X0_19, N_STEPS_19)
answer_M17_19d = bool(abs(near_19[40] - far_19[40]) > 0.01)
uniform_19 = iterate_with_derivative(phi_4, dphi_4, np.linspace(0.01, 0.99, 10000), N_STEPS_19)[1][-1]
print("a)", answer_M17_19a, " b)", round(answer_M17_19b, 3), " c)", round(answer_M17_19c, 2),
      f"({answer_M17_19c:.4f} ; ln 2 = {math.log(2):.4f} ; écart-type des 10 000 taux : {np.std(rates_19):.3f} ; "
      f"avec 10 000 départs uniformes : {np.mean(np.log(np.abs(uniform_19))) / N_STEPS_19:.4f})",
      " d)", answer_M17_19d)
print("c = 2,6 : les premiers facteurs φ′(x_k) :", np.round(dphi_25(xs_25[:6]), 3).tolist(), "; x_60 =", xs_25[-1])
print("c = 4 : écart entre les deux trajectoires aux itérations 10, 20, 30, 40 :",
      [f"{abs(near_19[k] - far_19[k]):.1e}" for k in (10, 20, 30, 40)])

''' + FIGURE_19,
    record='''def run_19r(c, x0, n):
    """x_n and D_n for φ_c(x) = c x (1 − x), from x0 (a number or an array of starts)."""
    x, d = np.asarray(x0, dtype=float), np.ones_like(np.asarray(x0, dtype=float))
    for _ in range(n):
        x, d = c * x * (1 - x), c * (1 - 2 * x) * d
    return x, d


wbm.record("M17.19a", 2 - 2.6, decimals=4,
           mistakes={"a) demande la PENTE φ_c′(x*), pas le point fixe x* lui-même": 1 - 1 / 2.6,
                     "φ_c(x) = cx − cx² : sa dérivée est c − 2cx": 2.6 * (1 - (1 - 1 / 2.6))})
_, d_25r = run_19r(2.6, 0.3, 60)
wbm.record("M17.19b", float(abs(d_25r) ** (1 / 60)), decimals=3,
           mistakes={"b) demande |D_60|^(1/60), pas son logarithme divisé par 60": float(np.log(abs(d_25r)) / 60)})
_, d_4r = run_19r(4.0, np.sin(np.pi / 2 * np.linspace(0.0, 1.0, 10002)[1:-1]) ** 2, 60)
wbm.record("M17.19c", float(np.mean(np.log(np.abs(d_4r)) / 60)), decimals=2,
           mistakes={"le taux se calcule avec le logarithme népérien, ln": float(np.mean(np.log10(np.abs(d_4r)) / 60)),
                     "c) demande le taux (1/60) ln|D_60|, pas |D_60|^(1/60)": float(np.mean(np.abs(d_4r) ** (1 / 60)))})
wbm.record("M17.19d", bool(abs(run_19r(4.0, 0.3, 40)[0] - run_19r(4.0, 0.3 + 1e-10, 40)[0]) > 0.01),
           mistakes={"compare les deux trajectoires après 40 itérations, |x_40 − x′_40|, à 0,01 : l'écart de départ "
                     "est multiplié par |D_k| à chaque pas, en première approximation": False})''',
    after=[
        ("md", "**Dans ta copie** : pour $c = 2{,}6$, écris les premiers facteurs $\\varphi_c'(x_0)$, "
               "$\\varphi_c'(x_1)$, … : pourquoi b) est-elle un peu plus petite que $\\lvert 2 - c\\rvert$ ? Pour "
               "$c = 2{,}8$, pourquoi la courbe met-elle plus longtemps à rejoindre sa droite, et pourquoi "
               "décroît-elle si lentement ? Pour $c = 1{,}4$ et $c = 2{,}6$, les pentes sont les mêmes : qu'est-ce qui "
               "distingue les deux trajectoires (regarde le signe des $D_k$) ? Pour $c = 4$, comment l'écart de d) "
               "grandit-il entre les itérations 10 et 40, et que dit-il de la prévision de $x_{60}$ à partir d'un "
               "$x_0$ connu à $10^{-10}$ près ?"),
    ],
    note=r"a) $\varphi_c'(x) = c(1 - 2x)$ et $x^* = 1 - \frac{1}{c}$ donnent $\varphi_c'(x^*) = c - 2c + 2 = 2 - c = "
         r"-0{,}6$. b) $\lvert D_{60}\rvert^{1/60} \approx 0{,}597$, un peu sous $0{,}6$ : le deuxième facteur, "
         r"$\varphi_c'(x_1)$ avec $x_1 = 0{,}546$, ne vaut que $-0{,}239$, et les premiers facteurs, loin du point fixe, "
         r"pèsent sur la moyenne géométrique. Les $D_k$ changent de signe à chaque pas (pente négative) : la trajectoire "
         r"tourne autour de $x^*$ ; pour $c = 1{,}4$, pente $+0{,}6$, elle s'en approche d'un seul côté. Pour "
         r"$c = 2{,}8$, $\lvert 2 - c\rvert = 0{,}8$ : la convergence est plus lente, et $D_k$ ne perd qu'un facteur "
         r"$0{,}8$ par pas. c) La moyenne des 10 000 taux vaut $\approx 0{,}693$, $\ln 2$ à quelques $10^{-4}$ près : "
         r"$D_k$ double en moyenne à chaque pas. Les départs suivent la loi des points d'une longue trajectoire de "
         r"$\varphi_4$ (la loi de l'arc sinus, de densité $\frac{1}{\pi\sqrt{x(1 - x)}}$) ; avec des départs "
         r"uniformes, la moyenne serait un peu plus petite, $\approx 0{,}686$, car les premiers pas n'ont pas encore "
         r"cette loi, et un seul départ donnerait un taux qui dépend des arrondis. d) Vrai : l'écart de $10^{-10}$ est multiplié par environ $2^k$ "
         r"($\approx 10^{12}$ après 40 pas) tant qu'il reste petit, puis il sature à la taille de $[0 ; 1]$ ; après "
         r"une quarantaine de pas, connaître $x_0$ à $10^{-10}$ près ne dit plus rien de $x_k$.",
)

GIVEN_20 = '''A_20 = np.array([1.0, 0.5])            # the centre a of the square
N_LINES_20 = 5                          # n lines in each direction


def warp_20(p):
    """F(x, y) = (x + 0.4 sin y, y + 0.4 sin x), for one point (2,) or an array (2, k) of k points in columns."""
    return np.array([p[0] + 0.4 * np.sin(p[1]), p[1] + 0.4 * np.sin(p[0])])


J_20 = ref_jacobian.numerical_jacobian(warp_20, A_20)     # the Jacobian of F at a (the reference's numerical_jacobian)


def preimages_20(points, linear):
    """The points of the plane (one per row) sent onto `points` by F (linear=False), or by p ↦ F(a) + J (p − a)."""
    points = np.asarray(points, dtype=float)
    if linear:
        return A_20 + np.linalg.solve(J_20, (points - warp_20(A_20)).T).T
    p = points.copy()
    for _ in range(80):                    # p = P − 0.4 (sin y, sin x): a contraction of ratio 0.4
        p = points - 0.4 * np.sin(p[:, ::-1])
    return p


def grid_images_20(ax, half_width, n_lines):
    """{(kind, direction, k): colour} for the curves of ax that are the image of a line of the grid: kind "F" or
    "linear", direction "h" (y = a_y + t_k) or "v" (x = a_x + t_k), t_k = np.linspace(-w, w, n)[k]. A curve counts
    when it has at least 20 points, all coming from that line, and covering the whole line."""
    ts = np.linspace(-half_width, half_width, n_lines)
    tolerance = 1e-6 * max(1.0, half_width)
    found = {}
    for line in ax.lines:
        points = np.column_stack([np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)])
        if len(points) < 20 or not np.all(np.isfinite(points)):
            continue
        for kind in ("F", "linear"):
            q = preimages_20(points, kind == "linear") - A_20        # the preimages, from the centre
            for direction, fixed, free in (("h", 1, 0), ("v", 0, 1)):
                k = int(np.argmin(np.abs(ts - q[0, fixed])))
                on_line = bool(np.all(np.abs(q[:, fixed] - ts[k]) < tolerance))
                covers = bool(q[:, free].min() < -0.98 * half_width and q[:, free].max() > 0.98 * half_width
                              and np.all(np.abs(q[:, free]) <= half_width + tolerance))
                if on_line and covers:
                    found[(kind, direction, k)] = mcolors.to_hex(line.get_color())
    return found'''

CHECK_20 = '''with checked("M17.20"):
    results_20 = []

    def report_20(ok, success, failure):
        results_20.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.0))
    try:
        for ax, width_20 in zip(axes, (0.2, 1.5)):
            shown_20 = f"demi-côté {fr(width_20, 1)}"
            opened_20 = drawn(draw_grid_images, ax, warp_20, A_20.copy(), J_20.copy(), width_20, N_LINES_20)
            report_20(not opened_20, f"{shown_20} : draw_grid_images dessine dans l'axe reçu",
                      f"{shown_20} : draw_grid_images doit dessiner dans l'axe reçu, sans ouvrir de figure (ni "
                      f"plt.figure ni plt.subplots)")
            found_20 = grid_images_20(ax, width_20, N_LINES_20)
            for kind_20, name_20 in (("F", "par F"), ("linear", "par l'approximation linéaire")):
                missing_20 = sum((kind_20, d, k) not in found_20 for d in "hv" for k in range(N_LINES_20))
                report_20(not missing_20, f"{shown_20} : les {2 * N_LINES_20} lignes de la grille ont leur image {name_20}",
                          f"{shown_20} : il manque l'image {name_20} de {missing_20} ligne(s) de la grille sur "
                          f"{2 * N_LINES_20} (une courbe ax.plot par ligne, d'au moins 20 points, qui couvre toute la "
                          f"ligne, du bord du carré à l'autre bord)")
            colours_20 = [{c for (kind, _, _), c in found_20.items() if kind == k} for k in ("F", "linear")]
            if colours_20[0] and colours_20[1]:          # (the missing images are reported above)
                report_20(len(colours_20[0]) == 1 and len(colours_20[1]) == 1 and colours_20[0] != colours_20[1],
                          f"{shown_20} : une couleur par application",
                          f"{shown_20} : une couleur pour toutes les images par F, une autre pour toutes celles de "
                          f"l'approximation linéaire")
            entries_20 = len(ax.get_legend().get_texts()) if ax.get_legend() is not None else 0
            report_20(entries_20 >= 2, f"{shown_20} : une légende",
                      f"{shown_20} : ajoute une légende à deux entrées (label=... sur une courbe de chaque sorte, puis "
                      f"ax.legend()) : j'en compte {entries_20}")
            ax.set_title(shown_20, fontsize=9)
    except BaseException:
        plt.close(fig)
        raise
    plt.show()
    verdict("M17.20", all(results_20), "les images de la grille par F et par l'approximation linéaire sont tracées, "
                                       "pour les deux carrés, en deux couleurs, avec une légende.",
            "relis les lignes ❌ ci-dessus.")'''

M17_20 = Ex(
    "M17.20", "🎨", 1, 20, "Une grille du plan déformée par une application non linéaire, et par son approximation "
    "linéaire",
    "voir l'approximation linéaire d'une application du plan : l'image d'une grille par l'application et par "
    "$\\mathbf{p} \\mapsto \\mathbf{F}(\\mathbf{a}) + \\mathbf{J}(\\mathbf{p} - \\mathbf{a})$, sur un petit et sur un "
    "grand carré.", "fiche §1", tracks="C, E", given=GIVEN_20,
    body=r"""La cellule fournie donne $\mathbf{F}(x, y) = (x + 0{,}4\sin y,\ y + 0{,}4\sin x)$ (`warp_20`, qui prend un point, ou un tableau de forme $(2, k)$ de $k$ points rangés en colonnes), le point $\mathbf{a} = (1 ;\ 0{,}5)$ (`A_20`), et la jacobienne $\mathbf{J}$ de $\mathbf{F}$ en $\mathbf{a}$ (`J_20`, calculée par la `numerical_jacobian` de la référence). Écris `draw_grid_images(ax, F, a, J, half_width, n_lines)`, qui dessine dans l'axe `ax` (sans en ouvrir d'autre) :
- les $n$ lignes horizontales $y = a_y + t$ et les $n$ lignes verticales $x = a_x + t$, pour $t$ dans `np.linspace(-half_width, half_width, n_lines)`, chacune limitée au carré de demi-côté `half_width` centré en $\mathbf{a}$ ;
- l'image de chaque ligne par $\mathbf{F}$, dans une couleur, et par l'approximation linéaire $\mathbf{p} \mapsto \mathbf{F}(\mathbf{a}) + \mathbf{J}(\mathbf{p} - \mathbf{a})$, dans une autre : **une courbe** `ax.plot` par ligne et par application, d'au moins 20 points répartis sur toute la ligne ;
- une légende à deux entrées (un `label` sur une seule courbe de chaque sorte), et des axes de même échelle (`ax.set_aspect("equal")`).

Ne trace pas la grille de départ elle-même, seulement ses deux images. Pour les points d'une ligne rangés en colonnes dans un tableau `P` de forme $(2, k)$, `F(P)` donne leurs images, et `F(a)[:, None] + J @ (P - a[:, None])` celles de l'approximation linéaire.

La cellule de vérification appelle ta fonction deux fois, avec $n = 5$ lignes : sur un petit carré (`half_width = 0.2`) et sur un grand (`half_width = 1.5`). Elle vérifie que chaque courbe tracée est bien l'image d'une ligne de la grille (en remontant de chacun de ses points à son antécédent), qu'il ne manque aucune image, les couleurs et la légende, puis affiche ta figure.""",
    todo='''def draw_grid_images(ax, F, a, J, half_width, n_lines):
    """In ax (and no other axes): the images, by F and by the linear approximation p ↦ F(a) + J (p − a), of the
    n_lines horizontal and n_lines vertical lines of the square of half side half_width centred at a; one ax.plot
    curve per line and per map (at least 20 points), one colour per map, a legend."""
    raise NotImplementedError("draw_grid_images n'est pas encore écrite (04_indices.md si tu bloques)")''',
    check=CHECK_20,
    solution='''def draw_grid_images(ax, F, a, J, half_width, n_lines):
    """In ax (and no other axes): the images, by F and by the linear approximation p ↦ F(a) + J (p − a), of the
    n_lines horizontal and n_lines vertical lines of the square of half side half_width centred at a; one ax.plot
    curve per line and per map (at least 20 points), one colour per map, a legend."""
    a, J = np.asarray(a, dtype=float), np.asarray(J, dtype=float)
    s = np.linspace(-half_width, half_width, 60)              # 60 points along each line
    centre = np.asarray(F(a), dtype=float)
    first = True
    for t in np.linspace(-half_width, half_width, n_lines):
        for line in (np.vstack([a[0] + s, np.full_like(s, a[1] + t)]),       # horizontal: y = a_y + t
                     np.vstack([np.full_like(s, a[0] + t), a[1] + s])):       # vertical: x = a_x + t
            exact = np.asarray(F(line), dtype=float)
            linear = centre[:, None] + J @ (line - a[:, None])
            ax.plot(exact[0], exact[1], color="C0", lw=1.4, label="image par F" if first else None)
            ax.plot(linear[0], linear[1], color="C3", lw=1.0, ls="--",
                    label="image par F(a) + J (p − a)" if first else None)
            first = False
    ax.plot([centre[0]], [centre[1]], "ko", ms=4)            # F(a), where both images touch
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)


corners_20 = A_20 + 1.5 * np.array([[1.0, 1.0], [-1.0, 1.0], [-1.0, -1.0], [1.0, -1.0]])
gaps_20 = [np.linalg.norm(warp_20(p) - (warp_20(A_20) + J_20 @ (p - A_20))) for p in corners_20]
print("J =", np.round(J_20, 4).tolist(), "; det J =", round(float(np.linalg.det(J_20)), 4))
print("écart entre F et son approximation aux coins du grand carré :", np.round(gaps_20, 3).tolist())
small_20 = [np.linalg.norm(warp_20(p) - (warp_20(A_20) + J_20 @ (p - A_20)))
            for p in A_20 + 0.2 * np.array([[1.0, 1.0], [-1.0, 1.0], [-1.0, -1.0], [1.0, -1.0]])]
print("… et aux coins du petit carré :", np.round(small_20, 4).tolist())


''' + CHECK_20,
    after=[
        ("md", "**Regarde ta figure**, puis, dans ta copie : sur le petit carré, les deux grilles sont presque "
               "confondues ; sur le grand, elles s'écartent. Comment l'écart entre les deux images d'un coin "
               "évolue-t-il quand le demi-côté est multiplié par 7,5 (fiche §1 : de quel ordre est l'erreur de "
               "l'approximation linéaire) ? Pourquoi les images par l'approximation linéaire restent-elles des droites "
               "parallèles, et celles par $\\mathbf{F}$ se courbent-elles ? Écris $\\mathbf{J}$ à la main ; que vaut "
               "son déterminant, et que dit-il de l'aire de l'image d'un petit carré autour de $\\mathbf{a}$ ? Les "
               "deux colonnes de $\\mathbf{J}$ : où les vois-tu sur la figure ?"),
    ],
    note=r"$\mathbf{J} = \begin{pmatrix} 1 & 0{,}4\cos a_y \\ 0{,}4\cos a_x & 1 \end{pmatrix} \approx \begin{pmatrix} "
         r"1 & 0{,}351 \\ 0{,}216 & 1 \end{pmatrix}$, de déterminant $\approx 0{,}924$ : près de $\mathbf{a}$, "
         r"$\mathbf{F}$ réduit les aires d'environ 8 %. L'approximation linéaire envoie la grille sur une grille de "
         r"parallélogrammes, construits sur les deux colonnes de $\mathbf{J}$ (les images des pas horizontaux et "
         r"verticaux) ; $\mathbf{F}$ courbe les lignes. L'erreur de l'approximation est d'ordre 2 : multiplier le "
         r"demi-côté par 7,5 multiplie l'écart aux coins par un facteur de l'ordre de $7{,}5^2 \approx 56$ (de 28 à 67 "
         r"selon le coin : si loin de $\mathbf{a}$, les termes d'ordre 3 comptent aussi).",
)

PART_B = Part("B", "Des outils, une prédiction, une expérience et une figure",
              "Fiche §1, §3 et §6. SymPy et SciPy contre ta jacobienne numérique ; la forme et les zéros de la "
              "jacobienne d'une composée, prédits puis vérifiés ; la dérivée d'une longue itération ; une grille "
              "déformée par une application du plan et par son approximation linéaire. Les vérifications calculent "
              "leurs jacobiennes de contrôle avec la `numerical_jacobian` de la référence (`ref_jacobian`), pour ne "
              "pas dépendre de la tienne.",
              given=GIVEN_B, exercises=[M17_17, M17_18, M17_19, M17_20])

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M17.21 to M17.23)
# ---------------------------------------------------------------------------
GIVEN_21 = '''def f_21(p):
    """f(x, y) = (x², x + y)."""
    return np.array([p[0] ** 2, p[0] + p[1]])


def g_21(q):
    """g(u, v) = (u v, u − v)."""
    return np.array([q[0] * q[1], q[0] - q[1]])


def jac_g_21(q):
    """The Jacobian of g at q, exact (checked): one row per output."""
    return np.array([[q[1], q[0]],
                     [1.0, -1.0]])


def jac_f_numeric_21(p):
    """The Jacobian of f at p, by the reference's numerical_jacobian."""
    return ref_jacobian.numerical_jacobian(f_21, p)


X_21 = np.array([1.0, 2.0])


# The colleague's three functions
def jacobian_by_hand(p):
    """The Jacobian of f(x, y) = (x², x + y) at p = (x, y), written by hand."""
    x, y = p
    return np.array([[2 * x, 1.0],
                     [0.0, 1.0]])


def chain(Jf, Jg):
    """The Jacobian of g ∘ f at x, from the Jacobian Jf of f at x and the Jacobian Jg of g at f(x)."""
    return Jf @ Jg


def composite_jacobian(f, jac_f, jac_g, x):
    """The Jacobian of g ∘ f at x, from f and from the functions jac_f and jac_g that give the Jacobians of f and g."""
    x = np.asarray(x, dtype=float)
    return jac_g(x) @ jac_f(x)'''

CHECK_21 = '''with checked("M17.21"):
    results_21 = []

    def report_21(ok, success, failure):
        results_21.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))

    def outcome_21(call):
        """(the value of call(), "") or (None, the error it raises); NotImplementedError goes through: ⏳."""
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", RuntimeWarning)
                return call(), ""
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001 - reported below
            return None, f"{type(exc).__name__} : {str(exc)[:120]}"

    def same_21(got, want):
        try:
            return got is not None and np.shape(got) == np.shape(want) and bool(np.allclose(np.asarray(got, dtype=float),
                                                                                           want))
        except (TypeError, ValueError):
            return False

    def shown_21(got, error):
        if error:
            return f"ta fonction lève {error}"
        try:
            return "reçu None" if got is None else f"reçu {np.round(np.asarray(got, dtype=float), 3).tolist()}"
        except (TypeError, ValueError):
            return f"reçu {got!r}"[:120]

    rng_21 = np.random.default_rng(5036)
    wrong_points_21 = []                                         # (A) the Jacobian of f at four other points
    for p_21 in rng_21.integers(-4, 5, size=(4, 2)).astype(float):
        want_21 = np.array([[2 * p_21[0], 0.0], [1.0, 1.0]])
        got_21, error_21 = outcome_21(lambda: jacobian_by_hand_fixed(p_21.copy()))
        if not same_21(got_21, want_21):
            wrong_points_21.append(f"en {p_21.tolist()} : attendu {want_21.tolist()}, {shown_21(got_21, error_21)}")
    report_21(not wrong_points_21, "jacobian_by_hand_fixed : la jacobienne de f en quatre autres points",
              "jacobian_by_hand_fixed, " + " ; ".join(wrong_points_21[:2]))
    for n_21, p_21, m_21 in ((2, 3, 4), (2, 2, 2), (3, 1, 2)):  # (B) f of R^n into R^p, g of R^p into R^m
        jf_21 = rng_21.integers(-3, 4, size=(p_21, n_21)).astype(float)
        jg_21 = rng_21.integers(-3, 4, size=(m_21, p_21)).astype(float)
        got_21, error_21 = outcome_21(lambda: chain_fixed(jf_21.copy(), jg_21.copy()))
        report_21(same_21(got_21, jg_21 @ jf_21), f"chain_fixed : f de R^{n_21} dans R^{p_21}, g de R^{p_21} dans R^{m_21}",
                  f"chain_fixed, f de R^{n_21} dans R^{p_21} et g de R^{p_21} dans R^{m_21} : attendu la jacobienne de "
                  f"g ∘ f, de forme ({m_21}, {n_21}) ; {shown_21(got_21, error_21)}")
    cases_21 = [                                                 # (C) label, f, jac_f, jac_g, x
        ("f de R² dans R³, g de R³ dans R²",
         lambda p: np.array([p[0] * p[1], np.sin(p[0]), p[1] ** 2]),
         lambda p: np.array([[p[1], p[0]], [np.cos(p[0]), 0.0], [0.0, 2 * p[1]]]),
         lambda q: np.array([[1.0, q[2], q[1]], [-2 * q[0], 0.0, 1.0]]),            # g(q) = (q1 + q2 q3, q3 − q1²)
         np.array([0.7, -1.3])),
        ("f et g de R² dans R²",
         lambda p: np.array([p[0] + p[1] ** 2, p[0] * p[1]]),
         lambda p: np.array([[1.0, 2 * p[1]], [p[1], p[0]]]),
         lambda q: np.array([[np.cos(q[0]), 0.0], [q[1], q[0]]]),                   # g(q) = (sin q1, q1 q2)
         np.array([0.5, -1.2])),
        ("f de R³ dans R², g de R² dans R",
         lambda p: np.array([p[0] * p[2], p[1] - p[2]]),
         lambda p: np.array([[p[2], 0.0, p[0]], [0.0, 1.0, -1.0]]),
         lambda q: np.array([[2 * q[0] * q[1], q[0] ** 2]]),                       # g(q) = q1² q2
         np.array([1.5, -0.5, 2.0])),
    ]
    for label_21, f_c21, jac_f_c21, jac_g_c21, x_c21 in cases_21:
        want_21 = jac_g_c21(f_c21(x_c21)) @ jac_f_c21(x_c21)
        got_21, error_21 = outcome_21(lambda: composite_jacobian_fixed(f_c21, jac_f_c21, jac_g_c21, x_c21.copy()))
        report_21(same_21(got_21, want_21), f"composite_jacobian_fixed : {label_21}",
                  f"composite_jacobian_fixed, {label_21} : attendu {np.round(want_21, 3).tolist()} ; "
                  f"{shown_21(got_21, error_21)}")
    verdict("M17.21", all(results_21), "les trois fonctions corrigées passent tous les cas.",
            "relis les lignes ❌ ci-dessus.")'''

M17_21 = Ex(
    "M17.21", "🐛", 1, 15, "Chasse à l'erreur : une jacobienne transposée, un produit dans le mauvais ordre, une "
    "jacobienne évaluée au mauvais point",
    "reconnaître trois erreurs classiques de la règle de la chaîne qui ne lèvent aucune erreur Python (une jacobienne "
    "transposée, un produit dans le mauvais ordre, un mauvais point d'évaluation), mesurer leurs effets, puis les "
    "corriger.", "fiche §1, §3 et §4", tracks="C, E", given=GIVEN_21,
    body=r"""Un collègue a écrit trois fonctions (cellule fournie) ; leurs docstrings disent ce qu'elles doivent faire, et chacune a l'erreur que nomme le titre :
- `jacobian_by_hand(p)` doit rendre la jacobienne de $\mathbf{f}(x, y) = (x^2,\ x + y)$ au point $\mathbf{p}$ ;
- `chain(Jf, Jg)` doit rendre la jacobienne de $\mathbf{g} \circ \mathbf{f}$ en $\mathbf{x}$, à partir de la jacobienne `Jf` de $\mathbf{f}$ en $\mathbf{x}$ et de la jacobienne `Jg` de $\mathbf{g}$ en $\mathbf{f}(\mathbf{x})$ ;
- `composite_jacobian(f, jac_f, jac_g, x)` doit rendre la jacobienne de $\mathbf{g} \circ \mathbf{f}$ en $\mathbf{x}$, à partir de $\mathbf{f}$ et des fonctions `jac_f` et `jac_g` qui donnent les jacobiennes de $\mathbf{f}$ et de $\mathbf{g}$ en un point ; son erreur : `jac_g` est évaluée au point de départ $\mathbf{x}$ au lieu du point intermédiaire $\mathbf{f}(\mathbf{x})$.

La cellule donne aussi $\mathbf{f}$ (`f_21`), $\mathbf{g}(u, v) = (uv,\ u - v)$ (`g_21`), la jacobienne exacte de $\mathbf{g}$ (`jac_g_21`), une jacobienne numérique de $\mathbf{f}$ (`jac_f_numeric_21`, par la référence) et le point $\mathbf{x} = (1, 2)$ (`X_21`). Aucune des trois fonctions ne lève d'erreur sur ces données. Calcule à la main, puis vérifie en appelant les fonctions du collègue :
- a) ce que rend `chain(jac_f_numeric_21(X_21), jac_g_21(f_21(X_21)))` (une matrice, ses coefficients arrondis à l'entier) ;
- b) ce que rend `composite_jacobian(f_21, jac_f_numeric_21, jac_g_21, X_21)` (une matrice, arrondie à l'entier) ;
- c) la bonne jacobienne de $\mathbf{g} \circ \mathbf{f}$ en $(1, 2)$ (une matrice).

Corrige ensuite les trois fonctions : écris `jacobian_by_hand_fixed`, `chain_fixed` et `composite_jacobian_fixed`, avec les mêmes arguments et les mêmes docstrings. La vérification les essaie sur des cas que tu ne vois pas : d'autres points, d'autres applications, d'autres dimensions.""",
    todo='''answer_M17_21a = ...  # a) a matrix (list of rows)
answer_M17_21b = ...  # b) a matrix
answer_M17_21c = ...  # c) a matrix''',
    check='''for letter, answer in zip("abc", [answer_M17_21a, answer_M17_21b, answer_M17_21c]):
    wbm.check(f"M17.21{letter}", answer)''',
    solution='''jf_21 = jac_f_numeric_21(X_21)                     # J_f(1, 2)
jg_21 = jac_g_21(f_21(X_21))                       # J_g at the intermediate point f(1, 2) = (1, 3)
answer_M17_21a = np.round(chain(jf_21, jg_21)).tolist()
answer_M17_21b = np.round(composite_jacobian(f_21, jac_f_numeric_21, jac_g_21, X_21)).tolist()
answer_M17_21c = np.round(jg_21 @ jf_21).tolist()
print("J_f =", np.round(jf_21, 6).tolist(), "; jacobian_by_hand =", jacobian_by_hand(X_21).tolist())
print("a)", answer_M17_21a, " b)", answer_M17_21b, " c)", answer_M17_21c)
print("J_g au point de départ (1, 2) au lieu du point intermédiaire :", jac_g_21(X_21).tolist())''',
    record='''jf_21r = np.array([[2.0, 0.0], [1.0, 1.0]])           # J_f(1, 2)
jg_21r = np.array([[3.0, 1.0], [1.0, -1.0]])          # J_g(f(1, 2)) = J_g(1, 3)
jg_x_21r = np.array([[2.0, 1.0], [1.0, -1.0]])        # J_g(1, 2): the wrong point
wbm.record("M17.21a", (jf_21r @ jg_21r).tolist(),
           mistakes={"a) demande ce que RENVOIE chain, la fonction du collègue : refais son produit, dans son ordre":
                         (jg_21r @ jf_21r).tolist()})
wbm.record("M17.21b", (jg_x_21r @ jf_21r).tolist(),
           mistakes={"b) demande ce que RENVOIE composite_jacobian : refais son calcul, avec J_g évaluée là où elle "
                     "l'évalue": (jg_21r @ jf_21r).tolist()})
wbm.record("M17.21c", (jg_21r @ jf_21r).tolist(),
           mistakes={"la dernière application, g, a sa jacobienne à GAUCHE : J_g J_f": (jf_21r @ jg_21r).tolist(),
                     "J_g s'évalue au point intermédiaire f(1, 2), pas en (1, 2)": (jg_x_21r @ jf_21r).tolist(),
                     "la jacobienne de f a une ligne par sortie : la ligne 1 est le gradient de x²":
                         (jg_21r @ jf_21r.T).tolist()})''',
    after=[
        ("md", "**Corrige maintenant les trois fonctions.** La cellule qui suit la tienne les vérifie sur des cas que "
               "tu ne vois pas."),
        ("todo", '''def jacobian_by_hand_fixed(p):
    """The Jacobian of f(x, y) = (x², x + y) at p = (x, y), written by hand."""
    raise NotImplementedError("jacobian_by_hand_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def chain_fixed(Jf, Jg):
    """The Jacobian of g ∘ f at x, from the Jacobian Jf of f at x and the Jacobian Jg of g at f(x)."""
    raise NotImplementedError("chain_fixed n'est pas encore écrite (04_indices.md si tu bloques)")


def composite_jacobian_fixed(f, jac_f, jac_g, x):
    """The Jacobian of g ∘ f at x, from f and from the functions jac_f and jac_g that give the Jacobians of f and g."""
    raise NotImplementedError("composite_jacobian_fixed n'est pas encore écrite (04_indices.md si tu bloques)")'''),
        ("check", CHECK_21),
        ("solution", '''def jacobian_by_hand_fixed(p):
    """The Jacobian of f(x, y) = (x², x + y) at p = (x, y), written by hand."""
    x, y = p
    return np.array([[2 * x, 0.0],                     # row 1: the gradient of x²
                     [1.0, 1.0]])                      # row 2: the gradient of x + y


def chain_fixed(Jf, Jg):
    """The Jacobian of g ∘ f at x, from the Jacobian Jf of f at x and the Jacobian Jg of g at f(x)."""
    return np.asarray(Jg, dtype=float) @ np.asarray(Jf, dtype=float)     # the last map applied on the left


def composite_jacobian_fixed(f, jac_f, jac_g, x):
    """The Jacobian of g ∘ f at x, from f and from the functions jac_f and jac_g that give the Jacobians of f and g."""
    x = np.asarray(x, dtype=float)
    return np.asarray(jac_g(f(x)), dtype=float) @ np.asarray(jac_f(x), dtype=float)   # J_g at the point f(x)


''' + CHECK_21),
        ("md", "**Après la vérification**, dans ta copie : pour chaque fonction du collègue, que calcule-t-elle "
               "exactement, et quelle règle de la fiche viole-t-elle (une ligne par sortie ; la dernière application "
               "à gauche ; la jacobienne de $\\mathbf{g}$ au point intermédiaire) ? En quels points `jacobian_by_hand` "
               "donnerait-elle quand même la bonne matrice ? Pour quelles applications `composite_jacobian` aurait-"
               "elle raison (pense à une $\\mathbf{g}$ dont la jacobienne ne dépend pas du point) ?"),
    ],
    note=r"$\mathbf{J}_{\mathbf{f}}(1, 2) = \begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}$, $\mathbf{f}(1, 2) = (1, 3)$ "
         r"et $\mathbf{J}_{\mathbf{g}}(1, 3) = \begin{pmatrix} 3 & 1 \\ 1 & -1 \end{pmatrix}$. a) `chain` rend "
         r"$\mathbf{J}_{\mathbf{f}}\mathbf{J}_{\mathbf{g}} = \begin{pmatrix} 6 & 2 \\ 4 & 0 \end{pmatrix}$, le produit "
         r"dans l'ordre où l'on applique les fonctions. b) `composite_jacobian` évalue $\mathbf{J}_{\mathbf{g}}$ en "
         r"$(1, 2)$ : $\begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix} = "
         r"\begin{pmatrix} 5 & 1 \\ 1 & -1 \end{pmatrix}$. c) $\mathbf{J}_{\mathbf{g}}(1, 3)\,\mathbf{J}_{\mathbf{f}}(1, "
         r"2) = \begin{pmatrix} 7 & 1 \\ 1 & -1 \end{pmatrix}$ ; vérification directe : $\mathbf{g}(\mathbf{f}(x, y)) "
         r"= (x^3 + x^2y,\ x^2 - x - y)$, de jacobienne $\begin{pmatrix} 3x^2 + 2xy & x^2 \\ 2x - 1 & -1 "
         r"\end{pmatrix}$ en $(1, 2)$. `jacobian_by_hand` range une ligne par **entrée** : elle n'aurait raison que "
         r"si la jacobienne était symétrique, ce qui n'arrive jamais ici (ses cases hors de la diagonale valent 0 et "
         r"1). `composite_jacobian` aurait raison si $\mathbf{J}_{\mathbf{g}}$ était la même partout, c'est-à-dire "
         r"pour $\mathbf{g}$ affine, ou par chance si $\mathbf{f}(\mathbf{x})$ et $\mathbf{x}$ donnaient la même "
         r"jacobienne de $\mathbf{g}$.",
)

GIVEN_22 = '''def jacobian_transposed(f, x, h=1e-5):
    """A wrong Jacobian: the transpose of the right one, one row per INPUT."""
    return ref_jacobian.numerical_jacobian(f, x, h).T


def jacobian_forward(f, x, h=1e-2):
    """A wrong Jacobian: forward differences (f(x + h e_j) − f(x)) / h with h = 1e-2, wrong by about h."""
    x = np.array(x, dtype=float)
    f0 = np.atleast_1d(np.asarray(f(x.copy()), dtype=float))
    columns = []
    for j in range(len(x)):
        step = np.zeros_like(x)
        step[j] = h
        columns.append((np.atleast_1d(np.asarray(f(x + step), dtype=float)) - f0) / h)
    return np.column_stack(columns)


WRONG_22 = {"jacobian_transposed (la transposée)": jacobian_transposed,
            "jacobian_forward (des différences avant, h = 10⁻²)": jacobian_forward}'''

CHECK_22 = '''with checked("M17.22"):
    if len(inspect.signature(test_chain_rule).parameters) != 1:
        raise TypeError("ton test prend un seul argument, la jacobienne à tester : def test_chain_rule(jacobian)")
    results_22, shapes_22 = [], []

    def report_22(ok, success, failure):
        results_22.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))

    def recorded_22(f, x, h=1e-5):
        """The reference numerical_jacobian, which records the shape of each Jacobian it returns."""
        jacobian = ref_jacobian.numerical_jacobian(f, x, h)
        shapes_22.append(tuple(jacobian.shape))
        return jacobian

    try:
        test_chain_rule(recorded_22)                   # your test on a right Jacobian: ⏳ while it is not written
        why_22 = ""
    except AssertionError as exc:
        why_22 = str(exc)[:200] or "un assert sans message"
    report_22(not why_22, "ton test passe sur la bonne jacobienne numérique",
              f"ton test échoue sur la jacobienne numérique de la référence : il refuse une implémentation juste "
              f"({why_22})")
    counts_22 = {shape: shapes_22.count(shape) for shape in ((2, 3), (2, 4), (4, 3))}
    report_22(min(counts_22.values()) >= 3,
              f"ton test calcule les jacobiennes de g ∘ f, de g et de f en {min(counts_22.values())} points",
              "ton test doit calculer, en au moins 3 points et avec la fonction reçue, les trois jacobiennes : celle "
              "de g ∘ f (forme (2, 3)), celle de g en f(x) (forme (2, 4)) et celle de f (forme (4, 3)) ; j'en compte "
              + ", ".join(f"{n} de forme {s}" for s, n in counts_22.items()))
    hints_22 = {"jacobian_transposed": "vérifie d'abord, par un assert, la forme de chaque jacobienne : (4, 3) pour f, "
                                       "(2, 4) pour g, (2, 3) pour g ∘ f",
                "jacobian_forward": "compare J_{g∘f} à J_g J_f avec une tolérance de l'ordre de 10⁻⁶ "
                                    "(np.allclose(..., rtol=1e-6, atol=1e-6)) : des différences avant avec h = 10⁻² se "
                                    "trompent d'environ 10⁻²"}
    for label_22, wrong_22 in WRONG_22.items():
        try:
            test_chain_rule(wrong_22)
            report_22(False, "", f"ton test passe sur {label_22} : il ne la voit pas ; {hints_22[wrong_22.__name__]}")
        except AssertionError:
            report_22(True, f"ton test échoue sur {label_22}", "")
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001 - a crash is not a failed assert
            report_22(False, "", f"ton test plante sur {label_22} ({type(exc).__name__} : {str(exc)[:100]}) au lieu "
                                 f"d'échouer sur un assert : {hints_22[wrong_22.__name__]}")
    verdict("M17.22", all(results_22), "ton test accepte la bonne jacobienne, calcule les trois jacobiennes en "
                                       "plusieurs points et attrape les deux fausses.", "relis les lignes ❌ ci-dessus.")'''

M17_22 = Ex(
    "M17.22", "🛠️", 1, 15, "Un test de propriété : J_{g∘f} = J_g J_f sur des applications tirées au hasard",
    "écrire un test de propriété de la règle de la chaîne, qui ne connaît aucune jacobienne exacte, et s'assurer qu'il "
    "attrape des implémentations fausses.", "fiche §3 ; Ex M17.14", tracks="C", given=GIVEN_22,
    body=r"""Écris `test_chain_rule(jacobian)`, une fonction de test dans le style de pytest (des `assert` avec un message qui dit le cas), qui reçoit une fonction `jacobian(f, x)` de même contrat que `numerical_jacobian` (une matrice $(m, n)$, une ligne par sortie) et vérifie la règle de la chaîne du §3 :
- avec un générateur de graine 5035 (`np.random.default_rng(5035)`, créé dans le test), tire une matrice $\mathbf{A}$ de forme $(4, 3)$ et une matrice $\mathbf{B}$ de forme $(2, 4)$, de coefficients de loi normale, et définis $\mathbf{f}(\mathbf{x}) = \sin(\mathbf{A}\mathbf{x})$, de $\mathbb{R}^3$ dans $\mathbb{R}^4$, et $\mathbf{g}(\mathbf{y}) = (\mathbf{B}\mathbf{y}) \odot (\mathbf{B}\mathbf{y})$, de $\mathbb{R}^4$ dans $\mathbb{R}^2$ ;
- en **au moins 3 points** $\mathbf{x}$ tirés au hasard, calcule avec `jacobian` les trois jacobiennes $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{x})$, $\mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))$ et $\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ ;
- vérifie d'abord leurs formes, $(2, 3)$, $(2, 4)$ et $(4, 3)$, puis que $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{x})$ et $\mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))\,\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ coïncident à une tolérance de l'ordre de $10^{-6}$ (`np.allclose(..., rtol=1e-6, atol=1e-6)`).

C'est un test de **propriété** : il ne compare à aucune formule exacte de jacobienne, seulement trois jacobiennes calculées par la fonction testée.

La vérification appelle ton test sur la `numerical_jacobian` de la référence, où il doit **passer**, et compte les jacobiennes qu'il calcule ; puis sur deux implémentations fausses de la cellule fournie, où il doit **échouer** (par un `assert`, pas par une autre erreur) : `jacobian_transposed`, qui rend la transposée, et `jacobian_forward`, des différences avant avec $h = 10^{-2}$.

Dans ta copie : quel `assert` attrape chacune des deux fausses jacobiennes ? Pourquoi un test de la règle de la chaîne peut-il attraper `jacobian_forward`, alors qu'il ne connaît aucune jacobienne exacte (les erreurs de $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}$ et de $\mathbf{J}_{\mathbf{g}}\mathbf{J}_{\mathbf{f}}$ se compensent-elles) ? Une jacobienne fausse pourrait-elle passer ce test ? Pense à une fonction qui multiplie toute jacobienne par 2, ou qui rend toujours la matrice nulle de la bonne forme.""",
    todo='''def test_chain_rule(jacobian):
    """J_{g∘f}(x) = J_g(f(x)) J_f(x), shapes first, for f(x) = sin(A x) of R^3 into R^4 and g(y) = (B y) ⊙ (B y) of R^4
    into R^2 (A and B drawn with the seed 5035), at a few points: three Jacobians computed by `jacobian`."""
    raise NotImplementedError("test_chain_rule n'est pas encore écrit (04_indices.md si tu bloques)")''',
    check=CHECK_22,
    solution='''def test_chain_rule(jacobian):
    """J_{g∘f}(x) = J_g(f(x)) J_f(x), shapes first, for f(x) = sin(A x) of R^3 into R^4 and g(y) = (B y) ⊙ (B y) of R^4
    into R^2 (A and B drawn with the seed 5035), at a few points: three Jacobians computed by `jacobian`."""
    rng = np.random.default_rng(5035)
    A, B = rng.normal(size=(4, 3)), rng.normal(size=(2, 4))

    def f(x):
        return np.sin(A @ x)

    def g(y):
        return (B @ y) * (B @ y)

    for point in range(5):
        x = rng.normal(size=3)
        J_gf = np.asarray(jacobian(lambda p: g(f(p)), x))
        J_g = np.asarray(jacobian(g, f(x)))
        J_f = np.asarray(jacobian(f, x))
        assert J_f.shape == (4, 3), f"point {point}: J_f has the shape {J_f.shape}, not (4, 3)"
        assert J_g.shape == (2, 4), f"point {point}: J_g has the shape {J_g.shape}, not (2, 4)"
        assert J_gf.shape == (2, 3), f"point {point}: J_(g∘f) has the shape {J_gf.shape}, not (2, 3)"
        gap = float(np.max(np.abs(J_gf - J_g @ J_f)))
        assert np.allclose(J_gf, J_g @ J_f, rtol=1e-6, atol=1e-6), (
            f"point {point}, x = {np.round(x, 3).tolist()}: J_(g∘f) and J_g J_f differ by up to {gap:.2e}")


for label_22s, wrong_22s in WRONG_22.items():               # which assert catches each wrong Jacobian
    try:
        test_chain_rule(wrong_22s)
        print(label_22s, ": pas attrapée")
    except AssertionError as exc:
        print(label_22s, ":", exc)


''' + CHECK_22,
    note=r"`jacobian_transposed` est attrapée dès le premier `assert` de forme ($\mathbf{J}_{\mathbf{f}}$ a la "
         r"forme $(3, 4)$) ; sans lui, `J_g @ J_f` lèverait une erreur de forme au lieu d'échouer proprement. "
         r"`jacobian_forward` passe les formes, mais ses erreurs, d'ordre $h = 10^{-2}$, ne sont pas les mêmes des "
         r"deux côtés : $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}$ et $\mathbf{J}_{\mathbf{g}}\mathbf{J}_{\mathbf{f}}$ "
         r"diffèrent de quelques $10^{-2}$, bien au-delà de $10^{-6}$ ; avec des différences centrées, l'écart tombe à "
         r"quelques $10^{-10}$. Un test de propriété ne voit pas tout : une fonction qui rendrait toujours $2\mathbf{J}$ "
         r"échouerait (le produit donne $4\mathbf{J}_{\mathbf{g}}\mathbf{J}_{\mathbf{f}}$, pas $2\,\mathbf{J}_{\mathbf{g} "
         r"\circ \mathbf{f}}$), mais une fonction qui rend toujours la matrice nulle de la bonne forme passerait : "
         r"d'où l'intérêt de tester aussi contre des valeurs connues (les tests de `jacobian.py` le font).",
)

GIVEN_23 = '''X0_23 = np.array([[2.0, 1.0],
                  [0.0, 1.0]])
H_23 = np.array([[0.0, 1.0],
                 [1.0, 0.0]])


def inversion_23(v):
    """X ↦ X⁻¹ as a map of R^(n²) into R^(n²): v is X flattened row by row (X.reshape(-1)), n = √len(v)."""
    n = math.isqrt(len(v))
    return np.linalg.inv(np.reshape(v, (n, n))).reshape(-1)'''

CHECK_23D = '''with checked("M17.23d"):
    rng_23 = np.random.default_rng(5040)
    gaps_23 = []
    for draw_23 in range(3):                           # three 3 × 3 matrices, moved by 3 I to be invertible
        X_23 = rng_23.normal(size=(3, 3)) + 3 * np.eye(3)
        want_23 = ref_jacobian.numerical_jacobian(inversion_23, X_23.reshape(-1))
        got_23 = inverse_jacobian(X_23.copy())
        if got_23 is None or np.shape(got_23) != (9, 9):
            print(f"❌ Ex M17.23 : pour une matrice 3 × 3, la jacobienne de l'inversion a la forme (9, 9) ; "
                  f"inverse_jacobian rend {'None' if got_23 is None else 'la forme ' + str(np.shape(got_23))}")
            raise StopCheck
        gaps_23.append(float(np.max(np.abs(np.asarray(got_23, dtype=float) - want_23))))
    print(f"plus grand écart avec la jacobienne numérique, sur les trois matrices : {max(gaps_23):.1e} "
          f"(objectif : moins de 1e-6)")
    wbm.check("M17.23d", bool(max(gaps_23) < 1e-6), computed=True)'''

M17_23 = Ex(
    "M17.23", "🏆", 3, 25, "Défi : la jacobienne de l'inversion X ↦ X⁻¹, vue comme une application de ℝ^{n²} dans "
    "ℝ^{n²}",
    "dériver l'inversion des matrices, la voir comme une application de $\\mathbb{R}^{n^2}$ dans "
    "$\\mathbb{R}^{n^2}$, et trouver une formule de sa jacobienne vérifiée numériquement.", "fiche §3 et §5 ; M12c",
    tracks="C", given=GIVEN_23,
    body=r"""L'inversion $X \mapsto X^{-1}$ des matrices $n \times n$ inversibles est une application de $\mathbb{R}^{n^2}$ dans $\mathbb{R}^{n^2}$, si l'on range les $n^2$ coefficients **ligne par ligne**, comme `X.reshape(-1)` (la convention de NumPy) : la coordonnée $ni + j$ est $X[i, j]$, les indices partant de 0, et de même pour $X^{-1}$. La cellule fournie l'écrit (`inversion_23`) et donne $X_0 = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$ (`X0_23`), de déterminant 2 et d'inverse $X_0^{-1} = \begin{pmatrix} 0{,}5 & -0{,}5 \\ 0 & 1 \end{pmatrix}$, et $H = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ (`H_23`). Trouve :
- a) la jacobienne $4 \times 4$ de l'inversion en $X_0$ (4 décimales) ;
- b) son déterminant (une fraction irréductible entre guillemets) ;
- c) la dérivée de l'inversion en $X_0$ dans la direction $H$, la limite de $\frac{(X_0 + tH)^{-1} - X_0^{-1}}{t}$ quand $t \to 0$ (une matrice $2 \times 2$) ;
- d) **l'objectif chiffré** : écris `inverse_jacobian(X)`, la jacobienne $(n^2, n^2)$ de l'inversion en une matrice inversible $X$ de taille $n \times n$, par une **formule** (ni différences finies ni `numerical_jacobian`). La vérification la compare à la jacobienne numérique de la référence sur trois matrices $3 \times 3$ tirées au hasard (graine 5040), décalées de $3\mathbf{I}$ pour être inversibles : le plus grand écart doit rester **sous $10^{-6}$**.

Pour a), ta `numerical_jacobian` et `inversion_23` suffisent. Pour c) et d), dérive l'égalité $X X^{-1} = \mathbf{I}$ : si $X$ bouge de $tH$, comment $X^{-1}$ doit-il bouger pour que le produit reste $\mathbf{I}$, au premier ordre en $t$ ? Puis passe d'une direction à la matrice : la colonne $nk + l$ de la jacobienne est la dérivée dans la direction $E_{kl}$, la matrice qui a un 1 en $(k, l)$ et des 0 ailleurs, aplatie comme les autres.

La cellule de vérification compare tes valeurs de a) à c), puis calcule l'écart de d) et enregistre si l'objectif est atteint.

Dans ta copie : écris ta formule de la dérivée dans une direction $H$, et vérifie c) avec elle. Pour $n = 1$, que dit-elle (la dérivée de $x \mapsto \frac{1}{x}$) ? Retrouve la première colonne de a) à partir d'elle, avec $H = E_{00}$ (le 1 en haut à gauche ; les indices partent de 0, comme dans NumPy). Comment b) s'exprime-t-il à partir de $\det X_0$ ? Pourquoi le déterminant d'une matrice $4 \times 4$ ne change-t-il pas quand on change le signe de tous ses coefficients ?""",
    todo='''def inverse_jacobian(X):
    """The (n², n²) Jacobian at X of X ↦ X⁻¹, the matrices flattened row by row (X.reshape(-1)), by a formula:
    neither finite differences nor numerical_jacobian."""
    raise NotImplementedError("inverse_jacobian n'est pas encore écrite (04_indices.md si tu bloques)")


answer_M17_23a = answer_M17_23b = answer_M17_23c = ...
with wbm.attempt("M17.23"):          # numerical_jacobian: ⏳ while it is not written
    answer_M17_23a = ...  # a) a matrix (4 decimals): the 4 × 4 Jacobian at X0_23
    answer_M17_23b = ...  # b) an irreducible fraction, as text: its determinant
    answer_M17_23c = ...  # c) a matrix: the derivative at X0_23 in the direction H_23''',
    check='''for letter, answer in zip("abc", [answer_M17_23a, answer_M17_23b, answer_M17_23c]):
    wbm.check(f"M17.23{letter}", answer)

''' + CHECK_23D,
    solution='''from fractions import Fraction


def inverse_jacobian(X):
    """The (n², n²) Jacobian at X of X ↦ X⁻¹, the matrices flattened row by row (X.reshape(-1)), by a formula:
    neither finite differences nor numerical_jacobian."""
    inverse = np.linalg.inv(np.asarray(X, dtype=float))
    return -np.kron(inverse, inverse.T)        # ∂(X⁻¹)[i, j] / ∂X[k, l] = −X⁻¹[i, k] X⁻¹[l, j]


jacobian_23 = mymath.jacobian.numerical_jacobian(inversion_23, X0_23.reshape(-1))
answer_M17_23a = np.round(jacobian_23, 4).tolist()
answer_M17_23b = str(Fraction(float(np.linalg.det(jacobian_23))).limit_denominator(1000))
inverse_23 = np.linalg.inv(X0_23)
answer_M17_23c = (-inverse_23 @ H_23 @ inverse_23).tolist()   # from X X⁻¹ = I: H X⁻¹ + X D = 0
print("a)", answer_M17_23a)
print("b)", answer_M17_23b, " c)", answer_M17_23c)
print("formule contre différences, en X0 :", f"{np.max(np.abs(inverse_jacobian(X0_23) - jacobian_23)):.1e}",
      "; J @ H aplatie :", np.round(jacobian_23 @ H_23.reshape(-1), 6).reshape(2, 2).tolist())''',
    record='''inverse_23r = np.array([[0.5, -0.5], [0.0, 1.0]])           # X0⁻¹
h_23r = np.array([[0.0, 1.0], [1.0, 0.0]])
jacobian_23r = -np.kron(inverse_23r, inverse_23r.T)
wbm.record("M17.23a", jacobian_23r.tolist(), decimals=4,
           mistakes={"lignes et colonnes échangées : la ligne 2i + j est le gradient de la sortie X⁻¹[i, j], la "
                     "colonne 2k + l la dérivée par rapport à X[k, l]": jacobian_23r.T.tolist(),
                     "l'aplatissement est ligne par ligne : la coordonnée 2i + j est X[i, j], pas X[j, i]":
                         (-np.kron(inverse_23r, inverse_23r)).tolist()})
wbm.record("M17.23b", "1/16", kind="fraction", simplified=True,
           mistakes={"(−1)⁴ = 1 : changer le signe des 16 coefficients d'une matrice 4 × 4 ne change pas son "
                     "déterminant": "-1/16",
                     "c'est l'inverse de la bonne valeur : près de X₀, l'inversion fait intervenir X₀⁻¹, pas X₀": "16",
                     "c'est le déterminant de X₀⁻¹ : b) demande celui de la jacobienne 4 × 4 de a)": "1/2"})
wbm.record("M17.23c", (-inverse_23r @ h_23r @ inverse_23r).tolist(), decimals=4,
           mistakes={"un produit de matrices ne commute pas : en dérivant X X⁻¹ = I, H reste ENTRE les deux facteurs":
                         (-inverse_23r @ inverse_23r @ h_23r).tolist(),
                     "un produit de matrices ne commute pas : H reste entre les deux facteurs, ni à gauche ni à droite":
                         (-h_23r @ inverse_23r @ inverse_23r).tolist()})
wbm.record("M17.23d", True,
           mistakes={"ta formule s'écarte de la jacobienne numérique : dérive X X⁻¹ = I dans la direction E_kl, puis "
                     "range les dérivées une ligne par coefficient de X⁻¹ et une colonne par coefficient de X": False})''',
    after=[("solution", CHECK_23D)],
    note=r"En dérivant $XX^{-1} = \mathbf{I}$ dans la direction $H$ : $HX^{-1} + X\,D = 0$, donc la dérivée de "
         r"l'inversion dans la direction $H$ est $D = -X^{-1}HX^{-1}$ (pour $n = 1$, $-\frac{h}{x^2}$, la dérivée de "
         r"$\frac{1}{x}$). Coefficient par coefficient, $\frac{\partial(X^{-1})_{ij}}{\partial X_{kl}} = "
         r"-(X^{-1})_{ik}(X^{-1})_{lj}$ : dans l'aplatissement par lignes, la jacobienne est $-(X^{-1} \otimes "
         r"X^{-\top})$ (`-np.kron(inv, inv.T)`). a) $\begin{pmatrix} -0{,}25 & 0 & 0{,}25 & 0 \\ 0{,}25 & -0{,}5 & "
         r"-0{,}25 & 0{,}5 \\ 0 & 0 & -0{,}5 & 0 \\ 0 & 0 & 0{,}5 & -1 \end{pmatrix}$. b) $\det(A \otimes B) = "
         r"\det(A)^n\det(B)^n$ pour $A$, $B$ de taille $n$, et le signe disparaît en dimension 4 : $\det\mathbf{J} = "
         r"\det(X_0^{-1})^4 = \frac{1}{16}$. c) $-X_0^{-1}HX_0^{-1} = \begin{pmatrix} 0{,}25 & -0{,}75 \\ -0{,}5 & "
         r"0{,}5 \end{pmatrix}$, aussi $\mathbf{J}$ fois $H$ aplatie. d) La formule et la jacobienne numérique "
         r"coïncident à quelques $10^{-12}$ près.",
)

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §1, §3, §4 et §5. Trois fonctions fausses à mesurer puis à corriger, un test de propriété de la "
              "règle de la chaîne, puis la jacobienne de l'inversion des matrices.",
              exercises=[M17_21, M17_22, M17_23])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M17.1 à M17.7, M17.11 | Les exercices papier (vérification) | ✏️ | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            rows.append(ex.table_row(part.key if i == 0 else ""))
    if kind == "exercise":
        title = "# M17 · Jacobienne et règle de la chaîne — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m17_jacobienne/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M17`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M17 · Jacobienne et règle de la chaîne — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : la jacobienne des coordonnées polaires et l'approximation "
               "linéaire, une jacobienne diagonale, une composée de trois applications, la normalisation "
               "$\\mathbf{x}/\\lVert\\mathbf{x}\\rVert$, un gradient dans les deux conventions, des dérivées à gauche "
               "et à droite et une composée de sept copies, deux lois de Boltzmann.\n"
               "- Écrire les trois fonctions de `mymath/jacobian.py` et les tester.\n"
               "- Comparer ta jacobienne à celles de SymPy et de SciPy, prédire la jacobienne d'une composée, suivre "
               "la dérivée d'une longue itération, voir une approximation linéaire, corriger des erreurs classiques, "
               "écrire un test de propriété, et relever un défi : la jacobienne de l'inversion des matrices.\n\n"
               r"**Rappel express.** Pour $\mathbf{f} : \mathbb{R}^n \to \mathbb{R}^m$, $\mathbf{J}_{\mathbf{f}}$ a la "
               r"forme $(m, n)$, $J_{ij} = \frac{\partial f_i}{\partial x_j}$ : une ligne par sortie, une colonne par "
               r"entrée. $\mathbf{f}(\mathbf{x} + \mathbf{h}) \approx \mathbf{f}(\mathbf{x}) + \mathbf{J}\mathbf{h}$, et "
               r"$\lvert\det\mathbf{J}\rvert$ multiplie les aires. Coordonnée par coordonnée : $\mathbf{J} = "
               r"\mathrm{diag}(g'(x_1), \ldots, g'(x_n))$, $\mathbf{J}\mathbf{v} = g'(\mathbf{x}) \odot \mathbf{v}$. "
               r"$\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{x}) = \mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))\,"
               r"\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ : la dernière à gauche, au point intermédiaire. "
               r"$\nabla_{\mathbf{x}}(L \circ \mathbf{f}) = \nabla_{\mathbf{y}}L\,\mathbf{J}_{\mathbf{f}}$ en ligne, "
               r"$\mathbf{J}_{\mathbf{f}}^\top\nabla_{\mathbf{y}}L$ de la forme de la variable. $\mathbf{J}\mathbf{v} "
               r"\approx \frac{\mathbf{f}(\mathbf{x} + h\mathbf{v}) - \mathbf{f}(\mathbf{x} - h\mathbf{v})}{2h}$ : deux "
               r"évaluations. Une itération : $\frac{\mathrm{d}x_L}{\mathrm{d}x_0} = \prod_k\varphi'(x_k)$. Boltzmann : "
               r"$p_i = \frac{e^{-E_i/T}}{\sum_je^{-E_j/T}}$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu calculer la jacobienne d'une application de $\\mathbb{R}^n$ dans $\\mathbb{R}^m$, une ligne "
               "par sortie, et t'en servir comme approximation linéaire ?\n"
               "2. Sais-tu reconnaître une jacobienne diagonale, et la calculer avec deux évaluations ?\n"
               "3. Sais-tu dériver une composée par le produit des jacobiennes, dans le bon ordre et au bon point ?\n"
               "4. Sais-tu passer du gradient en ligne au gradient de la forme de la variable, et calculer un produit "
               "jacobienne-vecteur sans former la matrice ?\n"
               "5. Sais-tu dériver une fonction définie par morceaux de chaque côté d'un coin, suivre la dérivée d'une "
               "longue itération, et calculer une loi de Boltzmann ?\n\n"
               "**La suite** : le chapitre 17 de workbookIA, qui se sert de ces outils, puis M18 (différentiation "
               "automatique et calcul matriciel), juste avant le chapitre 18 de workbookIA.")]


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
