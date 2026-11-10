#!/usr/bin/env python
"""Build the two notebooks of chapter M13a from a single source (used by Claude).

    python tools/chapters/build_m13a.py
    python tools/run_all_notebooks.py chapitres/m13a_vraisemblance_logistique/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m13a_vraisemblance_logistique/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M13a.1 to M13a.12, 🔗 M13a.18); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer nor the last step that gives it. The data are new:
synthetic (seeds 4122 to 4132, never 1301 to 1336, the seeds of workbookIA 13) or written in the statements; none is a
test case of tests/test_m13a_likelihood.py, an example of the fiche (no 8 visitors, no counts (11, 6, 3, 0), no
durations 31, 24, 38, 29, 33, no w = (1.2, −0.8)) or of a docstring of likelihood.py, nor an example of workbookIA 13
(no penguins, no letters nor words, no clouds centred at 0 and 1.5, no scores ±1 000, ±700, ±40 or −745, no « start
of a gradient descent » at ln 2, no maxima log₂ 3 and 2/3 asked for).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M13a"
FOLDER = "chapitres/m13a_vraisemblance_logistique"

F = 'kind="fraction", simplified=True'
FRAC = "an irreducible fraction, as text"
LN10 = "les logarithmes du chapitre sont népériens : ln, pas log₁₀"
LN2 = "les logarithmes de la log-loss sont népériens : ln, pas log₂"
BITS = "la question demande des bits : log₂ x = ln x / ln 2, pas ln"
NEG = "une log-vraisemblance d'une loi discrète est négative ou nulle : chaque ln p est négatif"
MEAN = "la log-loss est une MOYENNE sur les exemples : divise la somme par leur nombre"
EXPONENT = "σ(z) = 1/(1 + e^(−z)) : attention au signe de l'exposant"
PRIORS = "n'oublie pas les proportions des classes, P(Y = 1) = 0,4 et P(Y = 0) = 0,6"
WEIGHTS = "pondère chaque ligne par sa probabilité P(X = x)"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M13a.1", "Le maximum de vraisemblance d'une loi de Bernoulli et d'une loi catégorielle", [
        ("a", FRAC, "P_1", F + ''', mistakes={"la proportion des pièces DÉFECTUEUSES, de label 1": R(13, 20)}'''),
        ("b", "a number (4 decimals)", "float(ELL_1)",
         f'''decimals=4, mistakes={{"{LN10}": float(ELL_1 / L10), "{NEG}": float(-ELL_1)}}'''),
        ("c", "a number (4 decimals)", "float(20 * ln(R(1, 2)))",
         f'''decimals=4, mistakes={{"{LN10}": float(20 * ln(R(1, 2)) / L10), "{NEG}": float(-20 * ln(R(1, 2)))}}'''),
        ("d", "a number (4 decimals)", "float(ELL_1 / 20)",
         f'''decimals=4, mistakes={{"la log-vraisemblance MOYENNE par pièce : divise la somme par 20": float(ELL_1), '''
         f'''"{LN10}": float(ELL_1 / 20 / L10), "{NEG}": float(-ELL_1 / 20)}}'''),
        ("e", "a list of 4 fractions, written as calculations (2/9) or with 6 decimals", "floats(R(c, 20) for c in C_1)",
         '''decimals=6, mistakes={"divise chaque comptage par N = 20, le nombre de clients": [5, 9, 0, 6]}'''),
        ("f", "a list of 4 numbers (4 decimals)", "floats(smooth_1(1, 24))",
         '''decimals=4, mistakes={"ajoute aussi Kα au dénominateur : les probabilités lissées doivent sommer à 1": '''
         '''floats(smooth_1(1, 20)), "le dénominateur est N + Kα : α s'ajoute à CHACUN des K = 4 comptages": '''
         '''floats(smooth_1(1, 21))}'''),
        ("g", "a list of 4 numbers (4 decimals)", "floats(smooth_1(R(1, 4), 21))",
         '''decimals=4, mistakes={"ajoute aussi Kα au dénominateur : les probabilités lissées doivent sommer à 1": '''
         '''floats(smooth_1(R(1, 4), 20)), "le dénominateur est N + Kα : α s'ajoute à CHACUN des K = 4 comptages": '''
         '''floats(smooth_1(R(1, 4), R(81, 4)))}'''),
        ("h", "a number (4 decimals)", "float(CAT_1)",
         f'''decimals=4, mistakes={{"{LN2.replace("de la log-loss", "d'une log-vraisemblance")}": float(CAT_1 / ln(2)), '''
         f'''"{LN10}": float(CAT_1 / L10), "avec les estimations du maximum de vraisemblance de e), pas les lissées": '''
         f'''float(sum(c * ln(q) for c, q in zip(C_1, smooth_1(1, 24))))}}'''),
    ]),

    Paper("M13a.2", "Le maximum de vraisemblance d'une loi normale : μ̂ et σ̂²", [
        ("a", "a number", "int(MU_2)"),
        ("b", "a number", "int(S_2)", '''mistakes={"S est la somme des CARRÉS des écarts à μ̂": 48}'''),
        ("c", "a number (4 decimals)", "float(V_2)",
         '''decimals=4, mistakes={"le maximum de vraisemblance divise S par n = 6, pas par n − 1": float(U_2)}'''),
        ("d", "a number (4 decimals)", "float(U_2)",
         '''decimals=4, mistakes={"l'estimation sans biais divise S par n − 1 = 5": float(V_2)}'''),
        ("e", "a number (4 decimals)", "float(sq(V_2))",
         '''decimals=4, mistakes={"σ̂ est la racine du σ̂² du maximum de vraisemblance, en n": float(sq(U_2)), '''
         '''"σ̂ est la RACINE de σ̂²": float(V_2)}'''),
        ("f", "a number (4 decimals)", "float(ell_2(V_2))",
         '''decimals=4, mistakes={"ℓ = −(n/2) ln(2πv) − S/(2v) : n'oublie pas le second terme": '''
         '''float(-3 * ln(2 * sympy.pi * V_2))}'''),
        ("g", "a number (4 decimals)", "float(ell_2(U_2))",
         '''decimals=4, mistakes={"c'est ℓ au maximum, la valeur de f) : g) se calcule en v = d)": float(ell_2(V_2)), '''
         '''"le terme S/(2v) ne vaut n/2 qu'au maximum : en v = d), calcule-le": float(-3 * (ln(2 * sympy.pi * U_2) + 1))}'''),
        ("h", FRAC, "R(5, 6)",
         F + ''', mistakes={"le maximum de vraisemblance SOUS-estime σ² en moyenne : le rapport est sous 1": R(6, 5), '''
         '''"le maximum de vraisemblance de la variance est biaisé : le rapport n'est pas 1": 1}'''),
    ]),

    Paper("M13a.3", "La log-loss de quatre prédictions, puis la même en cross-entropy", [
        ("a", "a list of 4 numbers (4 decimals)", "floats(TERMS_3)",
         '''decimals=4, mistakes={"pour un label 0, le terme est −ln(1 − p̂) : la probabilité du label OBSERVÉ": '''
         '''floats(-ln(q) for q in P_3), "un terme de log-loss est −ln q, positif": floats(-t for t in TERMS_3)}'''),
        ("b", "a number (4 decimals)", "float(LL_3)",
         f'''decimals=4, mistakes={{"{MEAN}": float(4 * LL_3), '''
         '''"pour un label 0, le terme est −ln(1 − p̂)": float(sum(-ln(q) for q in P_3) / 4)}'''),
        ("c", "a number (3 decimals)", "float(LL_3 / ln(2))",
         '''decimals=3, mistakes={"pour passer des nats aux bits, DIVISE par ln 2 : 1 bit vaut ln 2 nat": float(LL_3 * ln(2))}'''),
        ("d", "a number (4 decimals)", "float(-4 * LL_3)",
         f'''decimals=4, mistakes={{"{NEG}": float(4 * LL_3), '''
         '''"la log-vraisemblance est une SOMME : ne divise pas par 4": float(-LL_3)}'''),
        ("e", FRAC, "R(3, 4)", F + ''', mistakes={"l'accuracy est la part des BONNES décisions": R(1, 4)}'''),
        ("f", "a number (4 decimals)", "float(ln(2))",
         f'''decimals=4, mistakes={{"le terme de chaque exemple est −ln 0,5, pas 0,5": 0.5, "{LN2}": 1.0}}'''),
        ("g", "a number (4 decimals)", "float(-ln(R(3, 10)))",
         '''decimals=4, mistakes={"le terme est −ln de la probabilité de la classe OBSERVÉE, pas de la plus probable": '''
         '''float(-ln(R(1, 2))), "la classe observée est la troisième, la dernière de la liste": float(-ln(R(1, 5)))}'''),
        ("h", "a number (4 decimals)", "float(H_3)",
         f'''decimals=4, mistakes={{"{MEAN}": float(4 * H_3), '''
         '''"le deuxième label est 1 : son terme est −ln 0,9": float((-ln(R(8, 10)) - ln(R(1, 10)) - ln(R(65, 100)) '''
         '''- ln(R(95, 100))) / 4)}'''),
    ]),

    Paper("M13a.4", "Ce que coûte une prédiction sûre et fausse : la log-loss quand p tend vers 0", [
        ("a", "a number (4 decimals)", "float(A_4)",
         f'''decimals=4, mistakes={{"le terme est −ln 0,98, pas 1 − 0,98": 0.02, "{MEAN}": float(1000 * A_4)}}'''),
        ("b", "a number (4 decimals)", "float(loss_4(R(1, 10 ** 4)))",
         f'''decimals=4, mistakes={{"{MEAN}": float(1000 * loss_4(R(1, 10 ** 4)))}}'''),
        ("c", "a number (4 decimals)", "float(loss_4(R(1, 10 ** 12)))",
         f'''decimals=4, mistakes={{"{MEAN}": float(1000 * loss_4(R(1, 10 ** 12)))}}'''),
        ("d", "a number (2 decimals)", "float(BASE_4)",
         '''decimals=2, mistakes={"la question demande la valeur de −ln q, pas celle de q": float(sympy.exp(-BASE_4)), '''
         '''"les 999 autres RÉUNIS : la somme de leurs termes": float(A_4)}'''),
        ("e", "a number (4 decimals)", "float(loss_4(R(1, 10 ** 15)))",
         f'''decimals=4, mistakes={{"{MEAN}": float(1000 * loss_4(R(1, 10 ** 15))), '''
         '''"la bibliothèque remplace q = 0 par 10⁻¹⁵ : la log-loss reste finie": math.inf}'''),
        ("f", "a number (4 decimals)", "float(-sympy.log(R(1, 10 ** 4), 2))",
         f'''decimals=4, mistakes={{"{BITS}": float(-ln(R(1, 10 ** 4)))}}'''),
        ("g", "True or False", "False",
         '''mistakes={"−ln q tend vers +∞ quand q tend vers 0 : un seul exemple suffit": True}'''),
    ]),

    Paper("M13a.5", "La sigmoïde : valeurs, logit, cote et symétrie σ(−z) = 1 − σ(z)", [
        ("a", "a number (4 decimals)", "float(sig(R(4, 5)))", f'''decimals=4, mistakes={{"{EXPONENT}": float(sig(-R(4, 5)))}}'''),
        ("b", "a number (4 decimals)", "float(sig(-R(5, 2)))", f'''decimals=4, mistakes={{"{EXPONENT}": float(sig(R(5, 2)))}}'''),
        ("c", "a number", "1",
         '''fractional="additionne les valeurs exactes, pas les arrondis de a) et b) : la symétrie σ(−z) = 1 − σ(z) donne '''
         '''la somme exacte."'''),
        ("d", "a number (4 decimals)", "float(ln(R(3, 17)))",
         f'''decimals=4, mistakes={{"le logit est ln(p/(1 − p)), dans cet ordre": float(ln(R(17, 3))), '''
         f'''"{LN10}": float(ln(R(3, 17)) / L10), "le logit est le ln de la COTE p/(1 − p), pas de p": float(ln(R(3, 20)))}}'''),
        ("e", FRAC, "R(3, 17)",
         F + ''', mistakes={"la cote est p/(1 − p), dans cet ordre": R(17, 3), "la cote divise p par 1 − p": R(3, 20)}'''),
        ("f", "a number (4 decimals)", "float(ln(19))",
         f'''decimals=4, mistakes={{"σ(z) = 0,95 > 1/2, donc z > 0 : z = ln(p/(1 − p))": float(-ln(19)), '''
         f'''"{LN10}": float(ln(19) / L10)}}'''),
        ("g", FRAC, "R(5, 7)", F + ''', mistakes={"p = cote/(1 + cote)": R(2, 7)}'''),
        ("h", FRAC, "R(6, 23)",
         F + ''', mistakes={"ajouter ln 2 au score multiplie la COTE par 2, pas la probabilité": R(3, 10), '''
         '''"c'est la cote doublée : reconvertis-la en probabilité, p = cote/(1 + cote)": R(6, 17)}'''),
    ]),

    Paper("M13a.6", "La softplus : valeurs, asymptotes et comportement pour |z| grand", [
        ("a", "a number (4 decimals)", "float(soft(R(5, 2)))", f'''decimals=4, mistakes={{"{LN10}": float(soft(R(5, 2)) / L10)}}'''),
        ("b", "a number (4 decimals)", "float(soft(-R(5, 2)))",
         f'''decimals=4, mistakes={{"{LN10}": float(soft(-R(5, 2)) / L10)}}'''),
        ("c", "a number", "R(5, 2)", '''kind="fraction", mistakes={"a) moins b), dans cet ordre": R(-5, 2)}'''),
        ("d", "a number (6 decimals)", "float(soft(6) - 6)",
         f'''decimals=6, mistakes={{"s(6) n'est pas exactement 6 : s(z) − z = ln(1 + e^(−z)), petit mais pas nul": 0.0, '''
         f'''"{LN10}": float((soft(6) - 6) / L10)}}'''),
        ("e", "a number (4 decimals)", "float(soft(-R(17, 5)))",
         '''decimals=4, mistakes={"z = −3,4 est négatif : max(z, 0) = 0 et |z| = 3,4": float(soft(R(17, 5)))}'''),
        ("f", "a number (4 decimals)", "float(soft(R(7, 10)))",
         '''decimals=4, mistakes={"−ln(1 − σ(z)) = s(z), pas s(−z) = −ln σ(z)": float(soft(-R(7, 10)))}'''),
        ("g", "True or False", "True", '''mistakes={"s(z) > 0 et s(z) > z, pour tout z": False}'''),
        ("h", "a number (4 decimals)", "float(ln(2))", f'''decimals=4, mistakes={{"{LN2.replace("de la log-loss", "de la softplus")}": 1.0}}'''),
    ]),

    Paper("M13a.7", "Un modèle logistique à deux features : probabilités, cote et frontière de décision", [
        ("a", "a number (4 decimals)", "float(z_7(1, 1))",
         '''decimals=4, mistakes={"z = w·x + b : n'oublie pas le biais": 1.8, "le biais b = −3,2 est négatif": 5.0}'''),
        ("b", "a number (4 decimals)", "float(sig(z_7(1, 1)))", f'''decimals=4, mistakes={{"{EXPONENT}": float(sig(-z_7(1, 1)))}}'''),
        ("c", "a number (4 decimals)", "float(sympy.exp(z_7(2, 2)))",
         '''decimals=4, mistakes={"la cote est e^z ; σ(z) est la probabilité": float(sig(z_7(2, 2))), '''
         '''"le score est la LOG-cote : la cote est e^z": float(z_7(2, 2))}'''),
        ("d", "a number (4 decimals)", "float(sympy.exp(W_7[1]))",
         '''decimals=4, mistakes={"w₂ agit sur la log-cote : la cote est multipliée par e^(w₂)": 1.1, '''
         '''"le poids de x₂ est w₂ = 1,1": float(sympy.exp(W_7[0]))}'''),
        ("e", "a number (4 decimals)", "float(-(B_7 + 2 * W_7[0]) / W_7[1])",
         '''decimals=4, mistakes={"w·x + b = 0 donne x₂ = (−b − w₁x₁)/w₂ : attention au signe de b": '''
         '''float((B_7 - 2 * W_7[0]) / W_7[1]), "isole x₂ : divise par w₂, son poids": float(-(B_7 + 2 * W_7[0]) / W_7[0])}'''),
        ("f", "a number (4 decimals)", "float((ln(R(17, 3)) - B_7 - 2 * W_7[0]) / W_7[1])",
         '''decimals=4, mistakes={"la ligne P = 0,85 est z = logit(0,85), pas z = 0,85": '''
         '''float((R(85, 100) - B_7 - 2 * W_7[0]) / W_7[1]), "logit(0,85) = ln(0,85/0,15) est positif": '''
         '''float((ln(R(3, 17)) - B_7 - 2 * W_7[0]) / W_7[1])}'''),
        ("g", "a number (4 decimals)", "float(z_7(2, 2) / NORM_7)",
         '''decimals=4, mistakes={"le score est la distance multipliée par ‖w‖ : divise-le par ‖w‖": float(z_7(2, 2)), '''
         '''"‖w‖ = √(w₁² + w₂²), avec la racine": float(z_7(2, 2) / NORM_7 ** 2)}'''),
        ("h", "a number (4 decimals)", "float(sig(B_7))",
         '''decimals=4, mistakes={"la question demande la probabilité σ(b), pas le score b": -3.2, '''
         '''"le score en (0, 0) est b = −3,2, négatif": float(sig(-B_7))}'''),
    ]),

    Paper("M13a.8", "L'hypothèse naïve à la main : une loi jointe factorisée, comparée à la vraie", [
        ("a", FRAC, "J1_8[(1, 0)] + J1_8[(1, 1)]",
         F + ''', mistakes={"P(x₁ = 1 | Y = 1) additionne les cases (1, 0) et (1, 1)": R(9, 20)}'''),
        ("b", FRAC, "N1_8[(0, 1)]",
         F + ''', mistakes={"c'est la vraie probabilité : Naïve Bayes la remplace par le produit des deux marginales": R(1, 4)}'''),
        ("c", FRAC, "post_8(J1_8, J0_8, (0, 1))",
         F + f''', mistakes={{"{PRIORS}": R(5, 7), '''
         '''"c'est P((0, 1) | Y = 1) ; la question demande P(Y = 1 | (0, 1)), par la formule de Bayes": R(1, 4)}'''),
        ("d", "a number (4 decimals)", "float(post_8(N1_8, N0_8, (0, 1)))",
         f'''decimals=4, mistakes={{"{PRIORS}": float(post_8(N1_8, N0_8, (0, 1), R(1, 2)))}}'''),
        ("e", "a number (4 decimals)", "float(post_8(J1_8, J0_8, (1, 1)))",
         f'''decimals=4, mistakes={{"{PRIORS}": float(post_8(J1_8, J0_8, (1, 1), R(1, 2)))}}'''),
        ("f", "a number (4 decimals)", "float(post_8(N1_8, N0_8, (1, 1)))",
         f'''decimals=4, mistakes={{"{PRIORS}": float(post_8(N1_8, N0_8, (1, 1), R(1, 2)))}}'''),
        ("g", "an integer", "DIFF_8",
         '''mistakes={"compare la classe la plus probable case par case : certaines décisions changent": 0, '''
         '''"compare case par case : certaines décisions ne changent pas": 4}'''),
        ("h", "a list of 2 integers", "[2 * (2 ** 10 - 1) + 1, 2 * 10 + 1]",
         '''mistakes={"une loi sur 2¹⁰ cases n'a que 2¹⁰ − 1 probabilités libres, puisque leur somme vaut 1": [2 * 2 ** 10, 21], '''
         '''"avec Naïve Bayes aussi, la proportion des classes compte : une probabilité de plus": [2 * 2 ** 10 - 1, 20], '''
         '''"avec les lois jointes complètes aussi, la proportion des classes compte : une probabilité de plus": '''
         '''[2 * 2 ** 10 - 2, 21], '''
         '''"la proportion des classes compte dans les deux cas : une probabilité de plus": [2 * 2 ** 10 - 2, 20]}'''),
    ]),

    Paper("M13a.9", "Deux classes gaussiennes de même variance : l'a posteriori est une sigmoïde d'un score affine", [
        ("a", "a number", "int(W_9)",
         '''mistakes={"w = (μ₁ − μ₀)/σ² : divise par la VARIANCE σ² = 4": 2, "w = (μ₁ − μ₀)/σ², dans cet ordre": -1}'''),
        ("b", "a number (4 decimals)", "float(B_9)",
         '''decimals=4, mistakes={"n'oublie pas le terme ln(π₁/π₀)": -1.0, "(μ₀² − μ₁²)/(2σ²), dans cet ordre": '''
         '''float(1 + LOG_9), "ln(π₁/π₀) : la proportion de la classe 1 au numérateur": float(-1 - LOG_9), '''
         '''"le dénominateur est 2σ² = 8": float(-2 + LOG_9)}'''),
        ("c", "a number (4 decimals)", "float(-B_9 / W_9)",
         '''decimals=4, mistakes={"le milieu des moyennes n'est la frontière que pour des classes équiprobables : '''
         '''n'oublie pas ln(π₁/π₀)": 1.0, "x* = −b/w : attention au signe": float(B_9 / W_9)}'''),
        ("d", "a number (4 decimals)", "float(sig(W_9 + B_9))",
         '''decimals=4, mistakes={"le milieu des moyennes n'est pas la frontière quand les classes ne sont pas '''
         '''équiprobables": 0.5}'''),
        ("e", "a number (3 decimals)", "float(sig(3 * W_9 + B_9))",
         '''decimals=3, mistakes={"n'oublie pas le terme ln(π₁/π₀) dans le biais": float(sig(3 * W_9 - 1))}'''),
        ("f", "a number", "1",
         '''fractional="avec des classes équiprobables, ln(π₁/π₀) = 0 : refais c) sans ce terme."'''),
        ("g", "a number (4 decimals)", "float(sympy.exp(W_9))",
         '''decimals=4, mistakes={"w agit sur la log-cote : la cote est multipliée par e^w": 1.0}'''),
        ("h", "a number (4 decimals)", "float(R(1, 8) - R(1, 18))",
         '''decimals=4, mistakes={"la log-cote est ln p(x | 1) − ln p(x | 0), dans cet ordre": float(R(1, 18) - R(1, 8)), '''
         '''"l'exposant d'une densité normale est −(x − μ)²/(2σ²), avec le 2": float(R(1, 4) - R(1, 9))}'''),
    ]),

    Paper("M13a.10", "L'entropie et l'indice de Gini de quelques distributions", [
        ("a", "a number (4 decimals)", "float(gini(D1_10))",
         '''decimals=4, mistakes={"l'indice de Gini est 1 − Σ p_k², pas le taux d'erreur 1 − max p_k": 0.05, '''
         '''"l'indice de Gini est 1 MOINS la somme des carrés": 0.905}'''),
        ("b", "a number (4 decimals)", "float(bits(D1_10))", f'''decimals=4, mistakes={{"{BITS}": float(bits(D1_10) * ln(2))}}'''),
        ("c", "a number (4 decimals)", "float(gini(D2_10))",
         '''decimals=4, mistakes={"l'indice de Gini est 1 − Σ p_k², pas le taux d'erreur 1 − max p_k": 0.6, '''
         '''"l'indice de Gini est 1 MOINS la somme des carrés": 0.36}'''),
        ("d", "a number (4 decimals)", "float(bits(D2_10))", f'''decimals=4, mistakes={{"{BITS}": float(bits(D2_10) * ln(2))}}'''),
        ("e", FRAC, "sympy.nsimplify(bits(D3_10))",
         F + ''', mistakes={"deux issues ont la probabilité 1/8 : chacune a son terme": R(11, 8)}'''),
        ("f", FRAC, "gini(D3_10)",
         F + ''', mistakes={"l'indice de Gini est 1 MOINS la somme des carrés": R(11, 32), '''
         '''"deux issues ont la probabilité 1/8 : chacune a son carré": R(43, 64)}'''),
        ("g", "a number (4 decimals)", "float(sympy.log(6, 2))",
         f'''decimals=4, mistakes={{"{BITS}": float(ln(6)), "l'entropie maximale est log₂ K, pas K": 6.0}}'''),
        ("h", FRAC, "R(5, 6)", F + ''', mistakes={"le maximum de l'indice de Gini est 1 − 1/K, pas 1/K": R(1, 6)}'''),
    ]),

    Paper("M13a.11", "L'information mutuelle d'un tableau de contingence, et la baisse d'entropie qu'elle mesure", [
        ("a", FRAC, "PY_11[0]", F + ''', mistakes={"« à l'heure » est la première colonne": R(7, 20)}'''),
        ("b", "a number (4 decimals)", "float(bits(PY_11))", f'''decimals=4, mistakes={{"{BITS}": float(bits(PY_11) * ln(2))}}'''),
        ("c", "a number (4 decimals)", "float(bits(ROWS_11[1]))",
         f'''decimals=4, mistakes={{"la loi de Y sachant X = vélo : divise la ligne par son total, 30": '''
         f'''float(bits([R(26, 100), R(4, 100)])), "{BITS}": float(bits(ROWS_11[1]) * ln(2))}}'''),
        ("d", "a number (4 decimals)", "float(HYX_11)",
         f'''decimals=4, mistakes={{"{WEIGHTS}": float(sum(bits(r) for r in ROWS_11) / 3), '''
         '''"H(Y | X) est une MOYENNE pondérée des entropies des lignes, pas leur somme": float(sum(bits(r) for r in ROWS_11))}'''),
        ("e", "a number (4 decimals)", "float(bits(PY_11) - HYX_11)",
         f'''decimals=4, mistakes={{"c'est H(Y | X) ; I(X ; Y) = H(Y) − H(Y | X)": float(HYX_11), '''
         f'''"{BITS}": float((bits(PY_11) - HYX_11) * ln(2))}}'''),
        ("f", "a number (4 decimals)", "float(bits(PX_11))",
         f'''decimals=4, mistakes={{"{BITS}": float(bits(PX_11) * ln(2)), '''
         '''"la loi de X se lit sur la colonne « total » : elle n'est pas uniforme": float(sympy.log(3, 2))}'''),
        ("g", "a number (4 decimals)", "float(gini(PY_11) - GYX_11)",
         f'''decimals=4, mistakes={{"{WEIGHTS}": float(gini(PY_11) - sum(gini(r) for r in ROWS_11) / 3)}}'''),
        ("h", "a number", "0",
         '''fractional="si chaque ligne avait les proportions de la colonne « total », connaître X ne changerait rien à '''
         '''la loi de Y."'''),
    ]),

    Paper("M13a.12", "La variance d'un groupe coupé en deux : variance intra plus variance inter", [
        ("a", "a number (4 decimals)", "float(mean_12(ALL_12))",
         '''decimals=4, mistakes={"la moyenne des sept cibles, pas le milieu des deux moyennes de groupes": 13.0}'''),
        ("b", "a number (4 decimals)", "float(var_12(ALL_12))",
         '''decimals=4, mistakes={"l'énoncé calcule les variances avec 1/n, n = 7": float(var_12(ALL_12) * R(7, 6))}'''),
        ("c", "a list of 2 numbers", "[int(mean_12(A_12)), int(mean_12(B_12))]",
         '''mistakes={"m_A d'abord, puis m_B": [int(mean_12(B_12)), int(mean_12(A_12))]}'''),
        ("d", "a list of 2 numbers (4 decimals)", "floats([var_12(A_12), var_12(B_12)])",
         '''decimals=4, mistakes={"l'énoncé calcule les variances avec 1/n : 1/3 pour A, 1/4 pour B": '''
         '''floats([var_12(A_12) * R(3, 2), var_12(B_12) * R(4, 3)])}'''),
        ("e", "a number (4 decimals)", "float(INTRA_12)",
         '''decimals=4, mistakes={"pondère chaque variance par la taille de son groupe, n_A/n et n_B/n": '''
         '''float((var_12(A_12) + var_12(B_12)) / 2)}'''),
        ("f", "a number (4 decimals)", "float(INTER_12)",
         '''decimals=4, mistakes={"pondère chaque écart par la taille de son groupe, n_A/n et n_B/n": '''
         '''float(((mean_12(A_12) - mean_12(ALL_12)) ** 2 + (mean_12(B_12) - mean_12(ALL_12)) ** 2) / 2)}'''),
        ("g", "True or False", "bool(sympy.simplify(INTRA_12 + INTER_12 - var_12(ALL_12)) == 0)",
         '''mistakes={"la décomposition est exacte quand toutes les variances sont en 1/n : refais e) + f)": False}'''),
        ("h", "a number (4 decimals)", "float(var_12(ALL_12) * R(7, 6))",
         '''decimals=4, mistakes={"la question demande la division par n − 1 = 6": float(var_12(ALL_12))}'''),
    ]),

    Paper("M13a.18", "Pont : une sonde linéaire, un modèle logistique en NumPy sur un batch de représentations figées, "
                     "jusqu'à la log-loss", [
        ("a", "a list of 6 numbers (4 decimals)", "floats(Z_18)",
         '''decimals=4, mistakes={"z = Hw + b : n'oublie pas le biais": floats(H_18 * W_18)}'''),
        ("b", "a list of 6 numbers (4 decimals)", "floats(sig(z) for z in Z_18)",
         f'''decimals=4, mistakes={{"{EXPONENT}": floats(sig(-z) for z in Z_18), '''
         '''"z = Hw + b : n'oublie pas le biais": floats(sig(z) for z in H_18 * W_18)}'''),
        ("c", "a number (4 decimals)", "float(LOSS_18)",
         f'''decimals=4, mistakes={{"{MEAN}": float(6 * LOSS_18), '''
         '''"le terme de chaque exemple est s(z) − yz : n'oublie pas −yz": float(sum(soft(z) for z in Z_18) / 6)}'''),
        ("d", FRAC, "R(5, 6)", F + ''', mistakes={"l'accuracy est la part des BONNES décisions": R(1, 6)}'''),
        ("e", "a number (4 decimals)", "float(CONST_18)",
         f'''decimals=4, mistakes={{"le meilleur modèle constant répond la proportion des labels 1, pas 0,5": float(ln(2)), '''
         f'''"{LN2}": float(CONST_18 / ln(2))}}'''),
        ("f", "a number (4 decimals)", "float(CONST_18 - LOSS_18)",
         '''decimals=4, mistakes={"e) − c), dans cet ordre : ce que la sonde GAGNE": float(LOSS_18 - CONST_18), '''
         '''"compare à la log-loss du meilleur modèle constant, celle de e)": float(ln(2) - LOSS_18)}'''),
        ("g", "an integer", "int(bool(Z_NEW_18 > 0))",
         '''mistakes={"le label 1 seulement si le score est positif : calcule le score de (1, 1, 0)": 1}'''),
        ("h", "an integer", "768 + 1", '''mistakes={"n'oublie pas le biais": 768}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly (SymPy) from the statements
import math

import sympy

R, ln, sq = sympy.Rational, sympy.log, sympy.sqrt
L10 = sympy.log(10)                       # log₁₀ x = ln x / ln 10 (a classic mistake)


def floats(values):
    """SymPy numbers as a list of Python floats."""
    return [float(v) for v in values]


def bits(p):
    """The entropy of the law p in bits, with 0 log₂ 0 = 0."""
    return -sum(q * sympy.log(q, 2) for q in p if q != 0)


def gini(p):
    """The Gini index 1 − Σ p_k² of the law p."""
    return 1 - sum(q ** 2 for q in p)


def sig(z):
    """The sigmoid 1 / (1 + e^(−z))."""
    return 1 / (1 + sympy.exp(-z))


def soft(z):
    """The softplus ln(1 + e^z)."""
    return sympy.log(1 + sympy.exp(z))


P_1, C_1 = R(7, 20), [5, 9, 0, 6]                                                           # M13a.1
ELL_1 = 7 * ln(P_1) + 13 * ln(1 - P_1)
CAT_1 = sum(c * ln(R(c, 20)) for c in C_1 if c)


def smooth_1(alpha, denominator):
    """(n_k + alpha) / denominator for the four counts."""
    return [(c + alpha) / R(denominator) for c in C_1]


X_2 = [245, 262, 251, 270, 248, 260]                                                       # M13a.2
MU_2 = R(sum(X_2), 6)
S_2 = sum((x - MU_2) ** 2 for x in X_2)
V_2, U_2 = S_2 / 6, S_2 / 5
assert sum(abs(x - MU_2) for x in X_2) == 48


def ell_2(v):
    """The normal log-likelihood at (μ̂, v)."""
    return -3 * ln(2 * sympy.pi * v) - S_2 / (2 * v)


Y_3, P_3 = [1, 1, 0, 0], [R(8, 10), R(45, 100), R(35, 100), R(5, 100)]                    # M13a.3
TERMS_3 = [-ln(q) if y else -ln(1 - q) for y, q in zip(Y_3, P_3)]
LL_3 = sum(TERMS_3) / 4
H_3 = (-ln(R(8, 10)) - ln(R(9, 10)) - ln(R(65, 100)) - ln(R(95, 100))) / 4
A_4 = -ln(R(98, 100))                                                                       # M13a.4
BASE_4 = 999 * A_4


def loss_4(q):
    """The log-loss of the 1 000 examples when the last one got the probability q."""
    return (BASE_4 - ln(q)) / 1000


W_7, B_7 = (R(7, 10), R(11, 10)), R(-16, 5)                                                 # M13a.7
NORM_7 = sq(W_7[0] ** 2 + W_7[1] ** 2)


def z_7(x1, x2):
    """The score w·x + b."""
    return W_7[0] * x1 + W_7[1] * x2 + B_7


J1_8 = {(0, 0): R(5, 100), (0, 1): R(25, 100), (1, 0): R(25, 100), (1, 1): R(45, 100)}      # M13a.8
J0_8 = {(0, 0): R(52, 100), (0, 1): R(10, 100), (1, 0): R(10, 100), (1, 1): R(28, 100)}


def naive_8(J):
    """The product of the two marginals of the joint law J."""
    a, b = J[(1, 0)] + J[(1, 1)], J[(0, 1)] + J[(1, 1)]
    return {(x1, x2): (a if x1 else 1 - a) * (b if x2 else 1 - b) for x1, x2 in J}


def post_8(J1, J0, cell, prior=R(2, 5)):
    """P(Y = 1 | cell) from the laws J1 and J0 of the two classes."""
    return prior * J1[cell] / (prior * J1[cell] + (1 - prior) * J0[cell])


N1_8, N0_8 = naive_8(J1_8), naive_8(J0_8)
DIFF_8 = sum((post_8(J1_8, J0_8, c) > R(1, 2)) != (post_8(N1_8, N0_8, c) > R(1, 2)) for c in J1_8)
W_9 = R(3 - (-1), 4)                                                                        # M13a.9
LOG_9 = ln(R(35, 65))
B_9 = R((-1) ** 2 - 3 ** 2, 2 * 4) + LOG_9
D1_10, D2_10 = [R(95, 100), R(5, 100)], [R(2, 5), R(2, 5), R(1, 5)]                         # M13a.10
D3_10 = [R(1, 2), R(1, 4), R(1, 8), R(1, 8)]
T_11 = [[22, 18], [26, 4], [17, 13]]                                                        # M13a.11
PY_11 = [R(sum(row[j] for row in T_11), 100) for j in range(2)]
PX_11 = [R(sum(row), 100) for row in T_11]
ROWS_11 = [[R(v, sum(row)) for v in row] for row in T_11]
HYX_11 = sum(px * bits(row) for px, row in zip(PX_11, ROWS_11))
GYX_11 = sum(px * gini(row) for px, row in zip(PX_11, ROWS_11))
A_12, B_12 = [6, 10, 8], [15, 19, 17, 21]                                                   # M13a.12
ALL_12 = A_12 + B_12


def mean_12(v):
    return R(sum(v), len(v))


def var_12(v):
    """The variance with 1/n."""
    return sum((t - mean_12(v)) ** 2 for t in v) / len(v)


INTRA_12 = R(3, 7) * var_12(A_12) + R(4, 7) * var_12(B_12)
INTER_12 = R(3, 7) * (mean_12(A_12) - mean_12(ALL_12)) ** 2 + R(4, 7) * (mean_12(B_12) - mean_12(ALL_12)) ** 2
H_18 = sympy.Matrix([[2, 0, R(1, 2)], [0, 1, 0], [1, 1, R(1, 2)], [0, 2, 1], [1, 0, 1], [0, 1, R(1, 2)]])   # M13a.18
W_18, B_18, Y_18 = sympy.Matrix([R(2, 5), R(-9, 10), R(8, 5)]), R(-1, 5), [1, 0, 0, 0, 1, 0]
Z_18 = H_18 * W_18 + B_18 * sympy.ones(6, 1)
LOSS_18 = sum(soft(z) - y * z for z, y in zip(Z_18, Y_18)) / 6
CONST_18 = -(R(1, 3) * ln(R(1, 3)) + R(2, 3) * ln(R(2, 3)))
Z_NEW_18 = (sympy.Matrix([[1, 1, 0]]) * W_18)[0] + B_18'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M13a.1 à M13a.12, 🔗 M13a.18)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"5/9\"` ;\n"
               "- une liste `[0.15, -2]` ; dans une liste, une fraction s'écrit comme un calcul, sans guillemets : "
               "`[2/9, 7/9]` ;\n"
               "- `True` / `False`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M13a.22 to M13a.24) and the libraries (M13a.25)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math
import warnings

import matplotlib.pyplot as plt
import numpy as np
import sympy

from wbm.nbtools import checked, drawn, filled, run_pytest_group, verdict


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

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M13a")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/likelihood.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "NumPy et le module `math` sont permis ; SciPy et scikit-learn sont interdits (les tests comparent tes "
         "résultats aux leurs, et un test vérifie que tu ne t'en sers pas). Ne modifie jamais les tableaux reçus : "
         "travaille sur une copie, `np.array(y, dtype=float)`. Les nombres se rendent en `float` de Python, les "
         "vecteurs en tableaux NumPy de flottants. Les logarithmes sont népériens, et aucun calcul ne doit produire "
         "`nan` ni d'avertissement (`RuntimeWarning`) : un $\\ln 0$ se traite à part.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError", "FloatingPointError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def value_error(message: str) -> str:
    return (f'''mistakes={{"{message}": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}}''')


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of likelihood.py selected by ``keyword`` (learner's code, or the reference)."""
    keyword = f"{keyword} or test_likelihood_uses_"
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m13a_likelihood.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m13a_likelihood.py", "{keyword}", impl="ref")')]


Y22 = "(np.random.default_rng(4122).random(50) < 0.35).astype(int)"
E_22 = "[0, 1, 1, 0], [0.0, 0.5, 1.0, 0.2]"
F_22 = "[0, 1, 1, 0], [0.3, 0.8, 0.0, 0.1]"

M13A_22 = Ex(
    "M13a.22", "🔨", 1, 15, "La log-vraisemblance et le maximum de vraisemblance d'une loi de Bernoulli · "
    "`bernoulli_log_likelihood, bernoulli_mle`",
    "programmer la log-vraisemblance de labels de Bernoulli, avec ses deux cas limites (un terme $0 \\ln 0$, un label "
    "impossible), et son maximum.", "fiche §1", tracks="C, E", mymath="likelihood.py",
    given=f'''Y_22 = {Y22}   # 50 synthetic labels, 0 or 1''',
    body=HOWTO + r"""

Écris, en suivant les docstrings (fiche §1) :
- `bernoulli_log_likelihood(y, p)` : $\sum_i \big[y_i\ln p_i + (1 - y_i)\ln(1 - p_i)\big]$, avec une seule probabilité `p` pour tous les labels ou une par label. Les contrôles d'abord (`ValueError` si `y` est vide ou contient autre chose que des 0 et des 1, si `p` n'a pas la bonne longueur ou sort de $[0, 1]$). Puis, pour chaque label, le $\ln$ de la probabilité **du label observé** seulement : $p_i$ pour un 1, $1 - p_i$ pour un 0. Ainsi un terme $0 \ln 0$ ne se calcule jamais (il compte pour 0), et un label de probabilité 0 rend `-math.inf`, sans avertissement ;
- `bernoulli_mle(y)` : la proportion de 1, avec les mêmes contrôles sur `y`.

La vérification calcule, avec les 50 labels `Y_22` de la cellule fournie :
- a) `bernoulli_log_likelihood(Y_22, 0.2)` (6 décimales) ;
- b) `bernoulli_mle(Y_22)` (6 décimales) ;
- c) la log-vraisemblance en ce maximum, `bernoulli_log_likelihood(Y_22, bernoulli_mle(Y_22))` (6 décimales) ;
- d) vrai ou faux : c) est au moins égale (à $10^{-12}$ près) à `bernoulli_log_likelihood(Y_22, q)` pour les 99 valeurs `q` de `np.linspace(0.01, 0.99, 99)` ;
- e) `bernoulli_log_likelihood(""" + E_22 + r""")` (6 décimales) : deux des labels sont certains ;
- f) `bernoulli_log_likelihood(""" + F_22 + r""")` : un label observé avait reçu la probabilité 0 ;
- g) le nom de l'erreur levée par `bernoulli_log_likelihood([0, 1, 2, 1], 0.5)`.

Dans ta copie : retrouve b) et c) à la main, à partir du nombre de 1 de `Y_22` (`Y_22.sum()`). Combien de fois la vraisemblance $L(\hat{p})$ est-elle plus grande que $L(0{,}2)$ ? Pourquoi la formule $y\ln p + (1 - y)\ln(1 - p)$, écrite telle quelle avec NumPy, donne-t-elle `nan` pour e), et que vaut chacun des quatre termes en vérité ? Que dit la valeur de f) sur le modèle qui a donné ces probabilités ?""",
    todo=LOAD_LEARNER,
    check=f'''with checked("M13a.22a"):
    wbm.check("M13a.22a", mymath.likelihood.bernoulli_log_likelihood(Y_22, 0.2), computed=True)
with checked("M13a.22b"):
    wbm.check("M13a.22b", mymath.likelihood.bernoulli_mle(Y_22), computed=True)
with checked("M13a.22c"):
    wbm.check("M13a.22c", mymath.likelihood.bernoulli_log_likelihood(Y_22, mymath.likelihood.bernoulli_mle(Y_22)),
              computed=True)
with checked("M13a.22d"):
    best_22 = mymath.likelihood.bernoulli_log_likelihood(Y_22, mymath.likelihood.bernoulli_mle(Y_22))
    wbm.check("M13a.22d", all(best_22 >= mymath.likelihood.bernoulli_log_likelihood(Y_22, float(q)) - 1e-12
                              for q in np.linspace(0.01, 0.99, 99)), computed=True)
with checked("M13a.22e"):
    wbm.check("M13a.22e", mymath.likelihood.bernoulli_log_likelihood({E_22}), computed=True)
with checked("M13a.22f"):
    wbm.check("M13a.22f", mymath.likelihood.bernoulli_log_likelihood({F_22}), computed=True)
with checked("M13a.22g"):
    wbm.check("M13a.22g", raised(mymath.likelihood.bernoulli_log_likelihood, [0, 1, 2, 1], 0.5), computed=True)''',
    solution=LOAD_REF + f'''
bernoulli_log_likelihood, bernoulli_mle = mymath.likelihood.bernoulli_log_likelihood, mymath.likelihood.bernoulli_mle
p_hat_22 = bernoulli_mle(Y_22)
best_22 = bernoulli_log_likelihood(Y_22, p_hat_22)
print("nombre de 1 :", int(Y_22.sum()), " a)", round(bernoulli_log_likelihood(Y_22, 0.2), 6), " b)", p_hat_22,
      " c)", round(best_22, 6))
print("d)", all(best_22 >= bernoulli_log_likelihood(Y_22, float(q)) - 1e-12 for q in np.linspace(0.01, 0.99, 99)),
      " e)", round(bernoulli_log_likelihood({E_22}), 6), " f)", bernoulli_log_likelihood({F_22}),
      " g)", raised(bernoulli_log_likelihood, [0, 1, 2, 1], 0.5))
print("L(p̂) / L(0,2) =", round(math.exp(best_22 - bernoulli_log_likelihood(Y_22, 0.2)), 2))''',
    record=f'''from scipy import stats

labels_22 = {Y22}
k_22 = int(labels_22.sum())


def loglik_22(q):
    return float(np.sum(stats.bernoulli.logpmf(labels_22, q)))


wbm.record("M13a.22a", loglik_22(0.2), decimals=6,
           mistakes={{"la log-vraisemblance est une SOMME sur les 50 labels, pas une moyenne": loglik_22(0.2) / 50,
                     "chaque label compte avec la probabilité de SA valeur : ln p pour un 1, ln(1 − p) pour un 0":
                         50 * math.log(0.2),
                     "p est la probabilité du label 1 : ln p va avec les 1, ln(1 − p) avec les 0":
                         k_22 * math.log(0.8) + (50 - k_22) * math.log(0.2)}})
wbm.record("M13a.22b", k_22 / 50, decimals=6,
           mistakes={{"la proportion des labels 1, pas des 0": 1 - k_22 / 50,
                     "le nombre de 1 divisé par n, le nombre de labels": float(k_22)}})
wbm.record("M13a.22c", loglik_22(k_22 / 50), decimals=6,
           mistakes={{"la log-vraisemblance est une SOMME sur les 50 labels, pas une moyenne": loglik_22(k_22 / 50) / 50}})
wbm.record("M13a.22d", True,
           mistakes={{"le maximum de vraisemblance est la proportion de 1 : relis bernoulli_mle et "
                      "bernoulli_log_likelihood (leurs tests disent ce qui ne va pas)": False}})
wbm.record("M13a.22e", math.log(0.5) + math.log(0.8), decimals=6,
           mistakes={{"un terme 0 · ln 0 compte pour 0 : ne prends le ln que de la probabilité du label OBSERVÉ":
                         -math.inf}})
wbm.record("M13a.22f", -math.inf, decimals=6,
           mistakes={{"ne remplace pas une probabilité 0 par un petit nombre : la docstring demande -math.inf":
                         math.log(0.7) + math.log(0.8) + math.log(1e-15) + math.log(0.9)}})
wbm.record("M13a.22g", "ValueError",
           {value_error("un label 2 n'est pas un label de Bernoulli : la docstring demande une ValueError")})''',
    after=tests_cells("test_bernoulli_log_likelihood or test_bernoulli_mle"),
    note=r"`Y_22` a 17 labels 1 sur 50 : $\hat{p} = 0{,}34$, $\ell(\hat{p}) = 17\ln 0{,}34 + 33\ln 0{,}66 \approx "
         r"-32{,}0518$, contre $\ell(0{,}2) = 17\ln 0{,}2 + 33\ln 0{,}8 \approx -34{,}7242$ : la vraisemblance est "
         r"$e^{2{,}672} \approx 14{,}5$ fois plus grande en $\hat{p}$. e) Les deux labels certains ont la probabilité 1 "
         r"(le label 0 de probabilité $1 - 0 = 1$, le label 1 de probabilité 1) : leurs termes valent $\ln 1 = 0$, et "
         r"il reste $\ln 0{,}5 + \ln 0{,}8 \approx -0{,}9163$. Écrite telle quelle, la formule calcule $0 \times \ln 0 = "
         r"0 \times (-\infty)$, que NumPy rend `nan`. f) Le troisième label, un 1, avait reçu la probabilité 0 : le "
         r"modèle déclarait impossible ce qui s'est produit, et la vraisemblance est nulle ($\ell = -\infty$).",
)

COUNTS_23 = "[9, 15, 0, 11, 7, 24]"
X23 = "np.random.default_rng(4123).normal(12.0, 3.0, size=40)"

M13A_23 = Ex(
    "M13a.23", "🔨", 1, 20, "Maximum de vraisemblance catégoriel, avec lissage, et gaussien · "
    "`categorical_mle, gaussian_mle`",
    "programmer le maximum de vraisemblance d'une loi catégorielle, avec lissage, et celui d'une loi normale.",
    "fiche §1 et §5", tracks="C, E", mymath="likelihood.py",
    given=f'''COUNTS_23 = {COUNTS_23}      # 66 throws of a loaded die: how many times each face 1 to 6 came up
X_23 = {X23}   # 40 synthetic measures''',
    body=r"""Écris, en suivant les docstrings :
- `categorical_mle(counts, alpha=0.0)` (fiche §1) : `ValueError` si les comptages sont vides, pas 1-D, ou ont une valeur négative, si `alpha` est négatif, ou si tous les comptages sont nuls avec `alpha = 0` ; sinon $\frac{n_k + \alpha}{N + K\alpha}$ (le maximum de vraisemblance $\frac{n_k}{N}$ pour $\alpha = 0$) ;
- `gaussian_mle(x)` (fiche §1) : `ValueError` si l'échantillon est vide ou pas 1-D ; sinon le couple $(\hat{\mu}, \hat{\sigma}^2)$, avec la variance **en $n$**, calculée sur les écarts $x_i - \hat{\mu}$.

La vérification calcule, avec les comptages `COUNTS_23` des six faces d'un dé truqué et l'échantillon `X_23` :
- a) `categorical_mle(COUNTS_23)` (une liste, 6 décimales) ;
- b) `categorical_mle(COUNTS_23, alpha=1)` (6 décimales) ;
- c) `categorical_mle(COUNTS_23, alpha=0.5)` (6 décimales) ;
- d) `gaussian_mle(X_23)`, sous la forme d'une liste $[\hat{\mu}, \hat{\sigma}^2]$ (6 décimales) ;
- e) le rapport `gaussian_mle(X_23)[1] / np.var(X_23, ddof=1)` (6 décimales) ;
- f) le nom de l'erreur levée par `categorical_mle([0, 0, 0, 0, 0, 0])`.

Dans ta copie : retrouve à la main les estimations de la face 3 en a), b) et c). Pourquoi celle de la face 4 est-elle la même dans les trois cas ? Vers quelle loi le lissage tire-t-il les estimations quand $\alpha$ grandit ? Retrouve e) sans rien calculer sur `X_23`. Quelle log-vraisemblance aurait un 67ᵉ lancer tombé sur la face 3, selon a) et selon b) ?""",
    todo=LOAD_LEARNER,
    check=f'''with checked("M13a.23a"):
    wbm.check("M13a.23a", np.asarray(mymath.likelihood.categorical_mle(COUNTS_23)).tolist(), computed=True)
with checked("M13a.23b"):
    wbm.check("M13a.23b", np.asarray(mymath.likelihood.categorical_mle(COUNTS_23, alpha=1)).tolist(), computed=True)
with checked("M13a.23c"):
    wbm.check("M13a.23c", np.asarray(mymath.likelihood.categorical_mle(COUNTS_23, alpha=0.5)).tolist(), computed=True)
with checked("M13a.23d"):
    wbm.check("M13a.23d", list(mymath.likelihood.gaussian_mle(X_23)), computed=True)
with checked("M13a.23e"):
    wbm.check("M13a.23e", mymath.likelihood.gaussian_mle(X_23)[1] / np.var(X_23, ddof=1), computed=True)
with checked("M13a.23f"):
    wbm.check("M13a.23f", raised(mymath.likelihood.categorical_mle, [0, 0, 0, 0, 0, 0]), computed=True)''',
    solution=LOAD_REF + '''
categorical_mle, gaussian_mle = mymath.likelihood.categorical_mle, mymath.likelihood.gaussian_mle
print("a)", np.round(categorical_mle(COUNTS_23), 6).tolist())
print("b)", np.round(categorical_mle(COUNTS_23, alpha=1), 6).tolist())
print("c)", np.round(categorical_mle(COUNTS_23, alpha=0.5), 6).tolist())
print("d)", np.round(gaussian_mle(X_23), 6).tolist(), " e)", round(gaussian_mle(X_23)[1] / np.var(X_23, ddof=1), 6),
      " f)", raised(categorical_mle, [0, 0, 0, 0, 0, 0]))''',
    record=f'''from scipy import stats

counts_23 = np.array({COUNTS_23}, dtype=float)
x_23 = {X23}
wbm.record("M13a.23a", (counts_23 / 66).tolist(), decimals=6,
           mistakes={{"divise chaque comptage par N = 66, le nombre de lancers": counts_23.tolist()}})
wbm.record("M13a.23b", ((counts_23 + 1) / 72).tolist(), decimals=6,
           mistakes={{"ajoute aussi Kα au dénominateur : les probabilités lissées doivent sommer à 1": ((counts_23 + 1) / 66).tolist(),
                     "le dénominateur est N + Kα : α s'ajoute à CHACUN des K = 6 comptages": ((counts_23 + 1) / 67).tolist()}})
wbm.record("M13a.23c", ((counts_23 + 0.5) / 69).tolist(), decimals=6,
           mistakes={{"ajoute aussi Kα au dénominateur : les probabilités lissées doivent sommer à 1": ((counts_23 + 0.5) / 66).tolist(),
                     "le dénominateur est N + Kα : α s'ajoute à CHACUN des K = 6 comptages": ((counts_23 + 0.5) / 66.5).tolist()}})
mean_23, scale_23 = stats.norm.fit(x_23)
wbm.record("M13a.23d", [float(mean_23), float(scale_23 ** 2)], decimals=6,
           mistakes={{"le maximum de vraisemblance divise par n, pas par n − 1": [float(mean_23), float(np.var(x_23, ddof=1))],
                     "la VARIANCE σ̂², pas l'écart-type": [float(mean_23), float(scale_23)]}})
wbm.record("M13a.23e", 39 / 40, decimals=6,
           mistakes={{"gaussian_mle divise par n, np.var(..., ddof=1) par n − 1 : leurs résultats diffèrent": 1.0,
                     "le rapport gaussian_mle / np.var(ddof=1), dans cet ordre": 40 / 39}})
wbm.record("M13a.23f", "ValueError",
           {value_error("des comptages tous nuls avec α = 0 donnent 0/0 : la docstring demande une ValueError")})''',
    after=tests_cells("test_categorical_mle or test_gaussian_mle"),
    note=r"Face 3 : $\frac{0}{66} = 0$, $\frac{0 + 1}{72} \approx 0{,}0139$ et $\frac{0{,}5}{69} \approx 0{,}0072$ ; la "
         r"face 4, sortie $11 = \frac{66}{6}$ fois, garde $\frac{1}{6}$ : le lissage tire chaque estimation vers la loi "
         r"uniforme $\frac{1}{K}$, d'autant plus fort que $\alpha$ est grand, et ne bouge pas celle qui y est déjà. Un "
         r"67ᵉ lancer sur la face 3 aurait la log-vraisemblance $\ln 0 = -\infty$ selon a), $\ln\frac{1}{72} \approx "
         r"-4{,}28$ selon b). e) Le maximum de vraisemblance divise par $n = 40$, `ddof=1` par $n - 1 = 39$ : le "
         r"rapport vaut $\frac{39}{40} = 0{,}975$, quel que soit l'échantillon ($\hat{\mu} \approx 11{,}2226$, "
         r"$\hat{\sigma}^2 \approx 10{,}6642$).",
)

EXTREME_24 = "[800.0, -800.0, 800.0, -800.0], [0, 1, 1, 0]"
CERTAIN_24 = "[800.0, -800.0], [1, 0]"
GIVEN_24 = '''rng_24 = np.random.default_rng(4124)
Z_24 = rng_24.normal(0.5, 2.0, size=30)                             # 30 moderate scores
Y_24 = (rng_24.random(30) < 1 / (1 + np.exp(-Z_24))).astype(int)   # their labels, drawn with the probabilities σ(z)'''

M13A_24 = Ex(
    "M13a.24", "🔨", 2, 20, "La log-loss à partir des scores, sans débordement · `logistic_loss`",
    "programmer la log-loss d'un modèle logistique directement à partir des scores, juste et sans débordement pour "
    "des scores immenses.", "fiche §2 et §3", tracks="C, E", mymath="likelihood.py", given=GIVEN_24,
    body=r"""Écris `logistic_loss(z, y)` (fiche §3), en suivant la docstring : `ValueError` si les longueurs diffèrent, si `y` est vide ou contient autre chose que des 0 et des 1 ; puis la moyenne des $s(z_i) - y_i z_i$, avec la softplus calculée **sans débordement** : $s(z) = \max(z, 0) + \ln(1 + e^{-\lvert z \rvert})$ (`np.maximum`, `np.log1p`). L'exponentielle ne reçoit ainsi jamais un nombre positif.

La vérification calcule :
- a) `logistic_loss(Z_24, Y_24)` pour les 30 scores modérés de la cellule fournie (6 décimales) : elle est comparée à `sklearn.metrics.log_loss(Y_24, σ(Z_24))` ;
- b) `logistic_loss(""" + EXTREME_24 + r""")` (6 décimales) ;
- c) vrai ou faux : le calcul de b) ne produit aucun avertissement (`RuntimeWarning`) ;
- d) `logistic_loss(""" + CERTAIN_24 + r""")` (6 décimales) : deux prédictions sûres et justes ;
- e) le nom de l'erreur levée par `logistic_loss([0.3, -0.7, 1.9], [1, 0])`.

Dans ta copie : retrouve b) à la main, terme par terme, avec l'écriture stable. Pourquoi `np.log(1 + np.exp(z))` rend-il `inf` (avec un avertissement) pour $z = 800$, et pourquoi la formule « avec $\hat{p} = \sigma(z)$ » perd-elle tout bien avant ($\sigma(45)$ vaut exactement 1 en flottants) ? Que donnerait la formule naïve pour d) ? Compare a) à $\ln 2$, la log-loss d'un modèle qui répond toujours 0,5.""",
    todo=LOAD_LEARNER,
    check=f'''with checked("M13a.24a"):
    wbm.check("M13a.24a", mymath.likelihood.logistic_loss(Z_24, Y_24), computed=True)
with checked("M13a.24b"):
    wbm.check("M13a.24b", mymath.likelihood.logistic_loss({EXTREME_24}), computed=True)
with checked("M13a.24c"):
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)       # a warning becomes an error, caught just below
        try:
            mymath.likelihood.logistic_loss({EXTREME_24})
            quiet_24 = True
        except RuntimeWarning:
            quiet_24 = False
    wbm.check("M13a.24c", quiet_24, computed=True)
with checked("M13a.24d"):
    wbm.check("M13a.24d", mymath.likelihood.logistic_loss({CERTAIN_24}), computed=True)
with checked("M13a.24e"):
    wbm.check("M13a.24e", raised(mymath.likelihood.logistic_loss, [0.3, -0.7, 1.9], [1, 0]), computed=True)''',
    solution=LOAD_REF + f'''
logistic_loss = mymath.likelihood.logistic_loss
with warnings.catch_warnings():
    warnings.simplefilter("error", RuntimeWarning)
    extreme_24 = logistic_loss({EXTREME_24})          # no RuntimeWarning: c) is True
print("a)", round(logistic_loss(Z_24, Y_24), 6), " b)", extreme_24, " d)", logistic_loss({CERTAIN_24}),
      " e)", raised(logistic_loss, [0.3, -0.7, 1.9], [1, 0]))
print("ln 2 =", round(math.log(2), 6), " ; accuracy au seuil 0 :", round(float(np.mean((Z_24 > 0) == Y_24)), 4))''',
    record=f'''from scipy import special
from sklearn.metrics import log_loss

rng_24r = np.random.default_rng(4124)
z_24r = rng_24r.normal(0.5, 2.0, size=30)
y_24r = (rng_24r.random(30) < special.expit(z_24r)).astype(int)
loss_24r = float(log_loss(y_24r, special.expit(z_24r), labels=[0, 1]))
wbm.record("M13a.24a", loss_24r, decimals=6,
           mistakes={{"{MEAN}": loss_24r * 30,
                     "chaque terme est s(z) − yz, avec le signe moins": float(np.mean(np.logaddexp(0, z_24r) + y_24r * z_24r)),
                     "chaque terme est s(z) − yz : le label y compte": float(np.mean(np.logaddexp(0, z_24r)))}})
wbm.record("M13a.24b", 400.0, decimals=6,
           mistakes={{"{MEAN}": 1600.0,
                     "e^800 déborde en flottants : écris la softplus max(z, 0) + ln(1 + e^(−|z|))": math.inf}})
wbm.record("M13a.24c", True,
           mistakes={{"np.exp d'un grand nombre positif déborde avec un avertissement : n'exponentie que −|z|": False}})
wbm.record("M13a.24d", 0.0, decimals=6,
           mistakes={{"e^800 déborde en flottants (inf − 800 reste inf) : écris la softplus max(z, 0) + ln(1 + e^(−|z|))":
                         math.inf}})
wbm.record("M13a.24e", "ValueError",
           {value_error("3 scores pour 2 labels : la docstring demande une ValueError")})''',
    after=tests_cells("test_logistic_loss"),
    note=r"b) Avec $t = z$ pour un label 0 et $t = -z$ pour un label 1, chaque terme vaut $s(t)$ : $s(800) = 800$ "
         r"(deux fois, deux prédictions sûres et fausses) et $s(-800) = \ln(1 + e^{-800}) = 0$ en flottants (deux fois) : "
         r"moyenne 400. La formule naïve calcule $e^{800}$, qui dépasse le plus grand flottant ($\approx 1{,}8 \times "
         r"10^{308}$, soit $e^{709{,}8}$) : `inf`. Par les probabilités, c'est pire : $\sigma(45) = 1 - 3 \times "
         r"10^{-20}$ s'arrondit à 1, et $\ln(1 - \hat{p}) = \ln 0$. d) Deux prédictions sûres et justes : 0 exactement, "
         r"là où la formule naïve donne `inf`. a) $\approx 0{,}3717$, bien sous $\ln 2 \approx 0{,}6931$ : les scores "
         r"portent de l'information sur les labels (ils ont servi à les tirer).",
)

M13A_25 = Ex(
    "M13a.25", "📦", 1, 15, "`scipy.stats`, `scipy.special` et `sklearn.metrics.log_loss` contre tes fonctions",
    "utiliser `scipy.stats.bernoulli`, `scipy.stats.norm.fit`, `scipy.special.xlogy`, `scipy.special.log_expit` et "
    "`sklearn.metrics.log_loss`, lire ce qu'elles rendent, et comparer avec ta librairie.",
    "fiche §1 à §3 ; Ex M13a.22 à M13a.24", tracks="C, E",
    given='''from scipy import special, stats
from sklearn.metrics import log_loss

rng_25 = np.random.default_rng(4125)
Y_25 = (rng_25.random(40) < 0.6).astype(int)                 # 40 labels
P_25 = np.round(rng_25.uniform(0.05, 0.95, size=40), 2)     # the probabilities of label 1 given by a model
Z_25 = rng_25.normal(0.0, 4.0, size=40)                     # the scores of another model, for the same labels
X_25 = rng_25.normal(-4.0, 1.5, size=25)                    # a sample of real values
COUNTS_25 = np.array([14, 0, 7, 3, 6])                      # the counts of five categories''',
    body=r"""En pratique, ces calculs sont tout faits :
- `stats.bernoulli.logpmf(y, p)` rend le tableau des $\ln P(Y = y_i)$, un par label (`p` peut être un tableau) ;
- `stats.norm.fit(x)` rend le couple $(\hat{\mu}, \hat{\sigma})$ du maximum de vraisemblance d'une loi normale : l'**écart-type**, pas la variance ;
- `special.xlogy(a, b)` calcule $a\ln b$, avec la convention $0 \ln 0 = 0$, sans avertissement ;
- `special.log_expit(z)` calcule $\ln\sigma(z)$ sans débordement ;
- `log_loss(y, p)` (scikit-learn) rend la log-loss moyenne, en nats, à partir des **probabilités**, qu'elle écrête loin de 0 et de 1.

Avec les données de la cellule fournie, calcule :
- a) `stats.bernoulli.logpmf(Y_25, P_25).sum()` (6 décimales) ;
- b) vrai ou faux : ta fonction `bernoulli_log_likelihood(Y_25, P_25)` est égale à a), à $10^{-10}$ près relativement ;
- c) les deux nombres rendus par `stats.norm.fit(X_25)` (une liste, 6 décimales) ;
- d) vrai ou faux : ta fonction `gaussian_mle(X_25)` rend la même moyenne que c) et, pour variance, le **carré** du second nombre de c), à $10^{-10}$ près relativement ;
- e) la log-vraisemblance catégorielle des comptages `COUNTS_25` en leur maximum, `special.xlogy(COUNTS_25, COUNTS_25 / COUNTS_25.sum()).sum()` (6 décimales) ;
- f) vrai ou faux : ta fonction `logistic_loss(Z_25, Y_25)` est égale à la moyenne de `-special.log_expit(np.where(Y_25 == 1, Z_25, -Z_25))`, à $10^{-12}$ près relativement ;
- g) `log_loss([1], [0.0], labels=[0, 1])` : la log-loss d'un seul exemple, de label 1, auquel le modèle a donné la probabilité 0 (4 décimales). Ne devine pas : **exécute-la** ;
- h) l'entier $k$ tel que $e^{-g} = 2^{-k}$ : la probabilité que `log_loss` a utilisée à la place de 0.

Dans ta copie : pourquoi le second nombre de c) n'est-il pas une variance, et que rendrait `np.std(X_25, ddof=1)` ? Que donne `np.sum(COUNTS_25 * np.log(COUNTS_25 / COUNTS_25.sum()))`, et pourquoi ? Que vaut `np.finfo(float).eps`, et quel lien avec h) ? En M13a.4 e), une bibliothèque écrêtait à $10^{-15}$ : pourquoi deux bibliothèques peuvent-elles rendre des log-loss différentes pour les mêmes prédictions ? Pourquoi `special.log_expit(z)` plutôt que `np.log(special.expit(z))` ?""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M13a")
answer_M13a_25a = ...  # a) a number (6 decimals)
answer_M13a_25c = ...  # c) a list of 2 numbers (6 decimals)
answer_M13a_25e = ...  # e) a number (6 decimals)
answer_M13a_25g = ...  # g) a number (4 decimals)
answer_M13a_25h = ...  # h) an integer
answer_M13a_25b = answer_M13a_25d = answer_M13a_25f = ...
# Each block stands alone: compute inside it what it needs, so that "Run all" goes on when a function is not written.
with wbm.attempt("M13a.25b"):        # your bernoulli_log_likelihood is called here: ⏳ while it is not written
    answer_M13a_25b = ...  # b) True or False
with wbm.attempt("M13a.25d"):        # your gaussian_mle
    answer_M13a_25d = ...  # d) True or False
with wbm.attempt("M13a.25f"):        # your logistic_loss
    answer_M13a_25f = ...  # f) True or False''',
    check='''for letter, answer in zip("abcdefgh", [answer_M13a_25a, answer_M13a_25b, answer_M13a_25c, answer_M13a_25d,
                                        answer_M13a_25e, answer_M13a_25f, answer_M13a_25g, answer_M13a_25h]):
    wbm.check(f"M13a.25{letter}", answer)''',
    solution='''ref_25 = wbm.load_mymath("ref", alias="mymath_ref").likelihood
answer_M13a_25a = round(float(stats.bernoulli.logpmf(Y_25, P_25).sum()), 6)
answer_M13a_25b = math.isclose(ref_25.bernoulli_log_likelihood(Y_25, P_25), float(stats.bernoulli.logpmf(Y_25, P_25).sum()),
                               rel_tol=1e-10)
loc_25, scale_25 = stats.norm.fit(X_25)
answer_M13a_25c = [round(float(loc_25), 6), round(float(scale_25), 6)]
mean_25, variance_25 = ref_25.gaussian_mle(X_25)
answer_M13a_25d = math.isclose(mean_25, loc_25, rel_tol=1e-10) and math.isclose(variance_25, scale_25 ** 2, rel_tol=1e-10)
answer_M13a_25e = round(float(special.xlogy(COUNTS_25, COUNTS_25 / COUNTS_25.sum()).sum()), 6)
answer_M13a_25f = math.isclose(ref_25.logistic_loss(Z_25, Y_25),
                               float(np.mean(-special.log_expit(np.where(Y_25 == 1, Z_25, -Z_25)))), rel_tol=1e-12)
answer_M13a_25g = round(float(log_loss([1], [0.0], labels=[0, 1])), 4)
answer_M13a_25h = round(float(log_loss([1], [0.0], labels=[0, 1])) / math.log(2))
print(answer_M13a_25a, answer_M13a_25b, answer_M13a_25c, answer_M13a_25d, answer_M13a_25e, answer_M13a_25f,
      answer_M13a_25g, answer_M13a_25h)
print("np.std(X_25, ddof=1) :", round(float(np.std(X_25, ddof=1)), 6), " ; eps :", np.finfo(float).eps,
      " ; 2**-52 :", 2.0 ** -52)
with warnings.catch_warnings():
    warnings.simplefilter("ignore", RuntimeWarning)
    print("sans xlogy :", np.sum(COUNTS_25 * np.log(COUNTS_25 / COUNTS_25.sum())))''',
    record='''from scipy import special, stats
from sklearn.metrics import log_loss

rng_25r = np.random.default_rng(4125)
y_25r = (rng_25r.random(40) < 0.6).astype(int)
p_25r = np.round(rng_25r.uniform(0.05, 0.95, size=40), 2)
z_25r = rng_25r.normal(0.0, 4.0, size=40)
x_25r = rng_25r.normal(-4.0, 1.5, size=25)
c_25r = np.array([14, 0, 7, 3, 6])
a_25r = float(stats.bernoulli.logpmf(y_25r, p_25r).sum())
wbm.record("M13a.25a", a_25r, decimals=6,
           mistakes={"logpmf rend un terme par label : la log-vraisemblance est leur SOMME": a_25r / 40})
wbm.record("M13a.25b", True,
           mistakes={"relis ta fonction bernoulli_log_likelihood (M13a.22) : ses tests disent ce qui ne va pas": False})
loc_25r, scale_25r = (float(v) for v in stats.norm.fit(x_25r))
wbm.record("M13a.25c", [loc_25r, scale_25r], decimals=6,
           mistakes={"norm.fit rend (loc, scale) : scale est l'ÉCART-TYPE, pas la variance": [loc_25r, scale_25r ** 2],
                     "norm.fit rend l'estimation du maximum de vraisemblance, en n": [loc_25r, float(np.std(x_25r, ddof=1))]})
wbm.record("M13a.25d", True,
           mistakes={"compare ta variance au CARRÉ de scale ; sinon, relis ta fonction gaussian_mle (M13a.23)": False})
e_25r = float(special.xlogy(c_25r, c_25r / c_25r.sum()).sum())
wbm.record("M13a.25e", e_25r, decimals=6,
           mistakes={"xlogy rend un terme par catégorie : la log-vraisemblance est leur SOMME": e_25r / 5})
wbm.record("M13a.25f", True,
           mistakes={"relis ta fonction logistic_loss (M13a.24) : ses tests disent ce qui ne va pas": False})
g_25r = float(log_loss([1], [0.0], labels=[0, 1]))
wbm.record("M13a.25g", g_25r, decimals=4,
           mistakes={"scikit-learn 1.6.1 n'écrête pas à 10⁻¹⁵ : exécute la ligne": float(-np.log(1e-15)),
                     "log_loss écrête les probabilités : son résultat est fini, exécute la ligne": math.inf})
wbm.record("M13a.25h", round(g_25r / math.log(2)),
           mistakes={"k = g / ln 2, avec la valeur de g que rend scikit-learn 1.6.1": 50})''',
    note=r"c) `norm.fit` rend $(\hat{\mu}, \hat{\sigma}) \approx (-3{,}686470 ;\ 1{,}107414)$ : un écart-type en $n$ ; "
         r"le carré, $\approx 1{,}2264$, est la variance de `gaussian_mle`. e) Sans `xlogy`, la catégorie de comptage 0 "
         r"donne $0 \times \ln 0$ : `nan` (et un avertissement), qui contamine toute la somme. g) scikit-learn 1.6.1 "
         r"remplace 0 par l'epsilon machine `np.finfo(float).eps` $= 2^{-52} \approx 2{,}2 \times 10^{-16}$ (le plus "
         r"petit $\varepsilon$ tel que $1 + \varepsilon \ne 1$) : $-\ln 2^{-52} = 52\ln 2 \approx 36{,}0437$, d'où "
         r"$k = 52$. Une bibliothèque qui écrête à $10^{-15}$ donne $34{,}5388$ : la valeur d'une log-loss qui contient "
         r"une probabilité 0 dépend d'une convention, et elle est surtout le signe d'un modèle trop sûr de lui. "
         r"`np.log(special.expit(z))` calcule $\ln$ d'un $\sigma(z)$ déjà arrondi, nul pour $z = -800$ ($\ln 0$) : `log_expit` "
         r"passe par la softplus, comme ta fonction.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M13a.26 to M13a.28)
# ---------------------------------------------------------------------------
M13A_26_GIVEN = '''Y_26 = np.zeros(1000, dtype=int)
Y_26[np.random.default_rng(4126).permutation(1000)[:150]] = 1   # 1 000 synthetic labels, exactly 150 of them 1
ONES_26 = np.ones(1000, dtype=int)                              # 1 000 labels, all 1'''

M13A_26_EXPERIMENT = '''def constant_log_loss(labels, q):
    """The log-loss (in nats) of the model that gives the same probability q of label 1 to every example."""
    labels = np.asarray(labels, dtype=float)
    return float(-np.mean(labels * np.log(q) + (1 - labels) * np.log(1 - q)))


print(f"a) toujours 0,5 sur Y_26 : {constant_log_loss(Y_26, 0.5):.4f}".replace(".", ","))
print(f"b) toujours 0,15 sur Y_26 : {constant_log_loss(Y_26, 0.15):.4f}".replace(".", ","))
print(f"c) toujours 0,5 sur des labels tous à 1 : {constant_log_loss(ONES_26, 0.5):.4f}".replace(".", ","))
print("d) " + " ; ".join(f"toujours {q} : {constant_log_loss(Y_26, q):.4f}" for q in (0.05, 0.15, 0.35, 0.5)).replace(".", ","))
qs = np.linspace(0.01, 0.99, 197)
fig, ax = plt.subplots(figsize=(6.5, 3.4))
ax.plot(qs, [constant_log_loss(Y_26, q) for q in qs], label="labels Y_26 (15 % de 1)")
ax.plot(qs, [constant_log_loss(ONES_26, q) for q in qs], label="labels tous à 1")
ax.axvline(0.15, color="0.6", lw=0.8, ls="--")
ax.set_xlabel("probabilité q annoncée à chaque exemple")
ax.set_ylabel("log-loss (nats)")
ax.set_ylim(0, 3)
ax.legend()
plt.show()'''

M13A_26 = Ex(
    "M13a.26", "🔮", 1, 10, "Prédire la log-loss d'un modèle qui répond toujours 0,5, puis toujours la fréquence des 1",
    "prévoir la log-loss de modèles qui ne regardent pas les features, et lequel d'entre eux est le meilleur, puis le "
    "vérifier.", "fiche §2", tracks="C, E", hypothesis=True, given=M13A_26_GIVEN,
    body=r"""La cellule fournie fabrique 1 000 labels synthétiques `Y_26`, dont exactement 150 valent 1 (une fréquence de 0,15), et 1 000 labels `ONES_26`, tous à 1. Un modèle **constant** donne la même probabilité $q$ du label 1 à tous les exemples, sans regarder leurs features. Pour chaque question, choisis le numéro de la bonne réponse :
- a) la log-loss (en nats) du modèle qui répond toujours $q = 0{,}5$, sur `Y_26` : (1) environ 0,22 ; (2) environ 0,42 ; (3) environ 0,69 ; (4) environ 1,90 ;
- b) la log-loss du modèle qui répond toujours $q = 0{,}15$, sur `Y_26` : mêmes choix ;
- c) la log-loss du modèle qui répond toujours $q = 0{,}5$, sur `ONES_26` : (1) 0 ; (2) environ 0,35 ; (3) environ 0,69 ; (4) $+\infty$ ;
- d) parmi les modèles constants $q = 0{,}05$, $0{,}15$, $0{,}35$ et $0{,}5$, celui qui a la plus petite log-loss sur `Y_26` : (1) 0,05 ; (2) 0,15 ; (3) 0,35 ; (4) 0,5.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_M13a_26a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M13a_26b = ...  # b) 1, 2, 3 or 4
prediction_M13a_26c = ...  # c) 1, 2, 3 or 4
prediction_M13a_26d = ...  # d) 1, 2, 3 or 4''',
    check='''for letter, prediction in zip("abcd", [prediction_M13a_26a, prediction_M13a_26b, prediction_M13a_26c,
                                      prediction_M13a_26d]):
    wbm.check(f"M13a.26{letter}", prediction)''',
    record='''wbm.record("M13a.26a", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M13a.26b", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M13a.26c", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M13a.26d", 2, prediction=True, choices=[1, 2, 3, 4])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(M13A_26_EXPERIMENT, [f"prediction_M13a_26{letter}" for letter in "abcd"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", M13A_26_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : pourquoi a) et c) sont-elles égales, et pourquoi la log-loss "
               "du modèle 0,5 ne dépend-elle pas des labels ? Que vaut b) en termes d'entropie (fiche §2) ? Pourquoi "
               "aucun modèle constant ne fait-il mieux que b) sur `Y_26`, et que doit donc battre un modèle qui regarde "
               "les features ? Sur les labels tous à 1, pourquoi la courbe n'a-t-elle pas de minimum dans $]0, 1[$ ?"),
    ],
    note=r"a) et c) : chaque exemple coûte $-\ln 0{,}5 = \ln 2 \approx 0{,}693$, quel que soit son label : la log-loss "
         r"du modèle 0,5 ne dépend pas des labels. b) $-0{,}15\ln 0{,}15 - 0{,}85\ln 0{,}85 \approx 0{,}4227$ : c'est "
         r"l'entropie, en nats, de la fréquence 0,15. d) La log-loss d'un modèle constant est $-\frac{1}{n}$ fois la "
         r"log-vraisemblance de Bernoulli des labels en $q$ : elle est la plus petite au maximum de vraisemblance, la "
         r"fréquence des 1 (fiche §1 et §2) ; 0,05 et 0,35 donnent $\approx 0{,}4930$ et $0{,}5236$. Un modèle qui regarde "
         r"les features doit faire mieux que 0,4227, pas seulement mieux que $\ln 2$. Sur des labels tous à 1, la "
         r"log-loss $-\ln q$ décroît jusqu'à $q = 1$ : le maximum de vraisemblance $\hat{p} = 1$ est au bord.",
)

M13A_27_GIVEN = '''P_27 = 0.3                    # the true parameter of the Bernoulli law
SIZES_27 = (25, 100, 400)     # the sizes n of the samples
N_SAMPLES_27 = 2000           # the number of samples for each n'''

M13A_27_FIGURE = '''table_fig_27 = spread_table()
fig, axes = plt.subplots(1, 3, figsize=(13, 3.2))
try:
    grid_27 = np.linspace(0.0, 0.65, 300)
    for ax, n in zip(axes, SIZES_27):
        sd = math.sqrt(P_27 * (1 - P_27) / n)
        ax.hist(table_fig_27[n], bins=np.arange(-0.5, n + 1.5, max(1, n // 100)) / n, density=True, alpha=0.6,
                label="les 2 000 p̂")
        ax.plot(grid_27, np.exp(-(grid_27 - P_27) ** 2 / (2 * sd ** 2)) / (sd * math.sqrt(2 * math.pi)), color="C3",
                label="N(p, p(1 − p)/n)")
        ax.axvline(P_27, color="0.3", lw=0.8, ls="--")
        ax.set_xlim(0.0, 0.65)
        ax.set_title(f"n = {n}")
        ax.set_xlabel("p̂")
    axes[0].legend(fontsize=8)
except BaseException:
    plt.close(fig)
    raise
plt.show()'''

M13A_27 = Ex(
    "M13a.27", "🔬", 2, 20, "La variabilité du maximum de vraisemblance d'une loi de Bernoulli d'un échantillon à "
    "l'autre",
    "mesurer de combien l'estimation $\\hat{p}$ varie d'un échantillon à l'autre, comparer à la formule "
    "$\\sqrt{p(1 - p)/n}$, et voir l'effet de la taille de l'échantillon.", "fiche §1 ; M02c", tracks="C",
    given=M13A_27_GIVEN,
    body=r"""Une loi de Bernoulli de paramètre $p = 0{,}3$ (connu ici, puisque c'est toi qui tires les données). Pour chaque taille $n$ de `SIZES_27`, tire 2 000 échantillons de $n$ labels, calcule le maximum de vraisemblance $\hat{p}$ de chacun (la proportion de 1), et regarde comment ces 2 000 valeurs se dispersent. Écris :
- `phat_samples(rng, n)` : les 2 000 valeurs de $\hat{p}$ pour des échantillons de taille $n$, en tirant les labels par `rng.random((N_SAMPLES_27, n)) < P_27` (un échantillon par ligne), puis en prenant la moyenne de chaque ligne ;
- `spread_table(seed=4127)` : le dictionnaire `{n: les 2 000 valeurs de p̂}` pour $n$ = 25, 100 et 400, **dans cet ordre**, avec **un seul** générateur `np.random.default_rng(seed)`, créé une fois (c'est ce qui rend tes nombres égaux à ceux de la vérification).

Puis calcule :
- a) les écarts-types des 2 000 valeurs de $\hat{p}$ pour $n$ = 25, 100 et 400, avec `np.std(..., ddof=1)` (une liste, 5 décimales) ;
- b) leurs valeurs théoriques $\sqrt{p(1 - p)/n}$ (une liste, 5 décimales) ;
- c) vrai ou faux : chaque écart-type mesuré est à moins de 5 % de sa valeur théorique ;
- d) les deux rapports des écarts-types mesurés, $n = 25$ sur $n = 100$ puis $n = 100$ sur $n = 400$ (une liste, 2 décimales) ;
- e) l'entier par lequel l'écart-type théorique est divisé quand $n$ est multiplié par 4.

Une cellule trace ensuite les trois histogrammes, avec la densité de la loi normale $\mathcal{N}\big(p, \frac{p(1 - p)}{n}\big)$.

Dans ta copie : d'où vient $\sqrt{p(1 - p)/n}$ (M02c : la variance d'une moyenne de $n$ variables indépendantes) ? Combien de labels faudrait-il pour que l'écart-type de $\hat{p}$ tombe sous 0,01 ? Pourquoi les histogrammes ressemblent-ils à des cloches de plus en plus étroites, et quel lien avec la figure de la fiche §1 (une log-vraisemblance plus creuse quand $n$ grandit) ? Que dire d'une proportion estimée sur 25 exemples à « 0,32 » ?""",
    todo='''def phat_samples(rng, n):
    """The N_SAMPLES_27 maximum likelihood estimates p̂ of samples of n labels of a Bernoulli law of parameter P_27:
    the labels drawn as rng.random((N_SAMPLES_27, n)) < P_27 (one sample per row), then the mean of each row."""
    raise NotImplementedError("rng.random((N_SAMPLES_27, n)) < P_27, puis la moyenne de chaque ligne")


def spread_table(seed=4127):
    """{n: the array of the N_SAMPLES_27 values of p̂} for n in SIZES_27, in this order, with ONE generator
    np.random.default_rng(seed), created once."""
    raise NotImplementedError("un seul générateur, puis phat_samples(rng, n) pour n = 25, 100 et 400, dans cet ordre")


answer_M13a_27a = answer_M13a_27c = answer_M13a_27d = ...
with wbm.attempt("M13a.27a"):        # your spread_table is called here: ⏳ while it is not written
    table_27 = spread_table()
    answer_M13a_27a = ...  # a) a list of 3 numbers (5 decimals)
    answer_M13a_27c = ...  # c) True or False
    answer_M13a_27d = ...  # d) a list of 2 numbers (2 decimals)
answer_M13a_27b = ...  # b) a list of 3 numbers (5 decimals)
answer_M13a_27e = ...  # e) an integer''',
    check='''for letter, answer in zip("abcde", [answer_M13a_27a, answer_M13a_27b, answer_M13a_27c, answer_M13a_27d,
                                     answer_M13a_27e]):
    wbm.check(f"M13a.27{letter}", answer)

with checked("M13a.27 figure"):
''' + "\n".join("    " + line for line in M13A_27_FIGURE.splitlines()),
    solution='''def phat_samples(rng, n):
    """The N_SAMPLES_27 maximum likelihood estimates p̂ of samples of n labels of a Bernoulli law of parameter P_27:
    the labels drawn as rng.random((N_SAMPLES_27, n)) < P_27 (one sample per row), then the mean of each row."""
    labels = rng.random((N_SAMPLES_27, n)) < P_27
    return labels.mean(axis=1)


def spread_table(seed=4127):
    """{n: the array of the N_SAMPLES_27 values of p̂} for n in SIZES_27, in this order, with ONE generator
    np.random.default_rng(seed), created once."""
    rng = np.random.default_rng(seed)
    return {n: phat_samples(rng, n) for n in SIZES_27}


table_27 = spread_table()
measured_27 = [float(np.std(table_27[n], ddof=1)) for n in SIZES_27]
theory_27 = [math.sqrt(P_27 * (1 - P_27) / n) for n in SIZES_27]
answer_M13a_27a = [round(s, 5) for s in measured_27]
answer_M13a_27b = [round(s, 5) for s in theory_27]
answer_M13a_27c = all(abs(m - t) / t < 0.05 for m, t in zip(measured_27, theory_27))
answer_M13a_27d = [round(measured_27[0] / measured_27[1], 2), round(measured_27[1] / measured_27[2], 2)]
answer_M13a_27e = 2
print(answer_M13a_27a, answer_M13a_27b, answer_M13a_27c, answer_M13a_27d, answer_M13a_27e)
print("moyennes des p̂ :", [round(float(np.mean(table_27[n])), 4) for n in SIZES_27],
      " ; n pour un écart-type de 0,01 :", math.ceil(P_27 * (1 - P_27) / 0.01 ** 2))
''' + M13A_27_FIGURE,
    record='''rng_27r = np.random.default_rng(4127)
samples_27r = [(rng_27r.random((2000, n)) < 0.3).mean(axis=1) for n in (25, 100, 400)]
std_27r = [float(np.std(s, ddof=1)) for s in samples_27r]
wbm.record("M13a.27a", std_27r, decimals=5,
           mistakes={"l'écart-type, pas la variance : np.std, ou la racine de np.var": [s ** 2 for s in std_27r],
                     "l'énoncé demande l'écart-type d'échantillon, ddof=1": [float(np.std(s)) for s in samples_27r]})
wbm.record("M13a.27b", [math.sqrt(0.21 / n) for n in (25, 100, 400)], decimals=5,
           mistakes={"l'écart-type théorique est la RACINE de p(1 − p)/n": [0.21 / n for n in (25, 100, 400)]})
wbm.record("M13a.27c", True,
           mistakes={"compare chaque écart-type mesuré à SA valeur théorique : |mesuré − théorique| / théorique": False})
wbm.record("M13a.27d", [std_27r[0] / std_27r[1], std_27r[1] / std_27r[2]], decimals=2,
           mistakes={"le plus petit n d'abord : l'écart-type pour n divisé par celui pour 4n":
                         [std_27r[1] / std_27r[0], std_27r[2] / std_27r[1]]})
wbm.record("M13a.27e", 2,
           mistakes={"l'écart-type varie comme 1/√n : multiplier n par 4 le divise par √4": 4})''',
    note=r"Mesurés : $\approx 0{,}0927$, $0{,}0461$ et $0{,}0237$, pour $\sqrt{0{,}21/n} \approx 0{,}0917$, $0{,}0458$ et "
         r"$0{,}0229$ (écarts relatifs de 1 %, 0,5 % et 3,6 %, du même ordre que l'incertitude d'un écart-type estimé "
         r"sur 2 000 valeurs, environ $1/\sqrt{2 \times 2\,000} \approx 1{,}6\,\%$). $\hat{p}$ est la moyenne de $n$ "
         r"variables de Bernoulli indépendantes, de variance $p(1 - p)$ : sa variance est $\frac{p(1 - p)}{n}$ (M02c), "
         r"et son écart-type est divisé par $\sqrt{4} = 2$ quand $n$ est multiplié par 4 (rapports mesurés 2,01 et 1,94). "
         r"Pour un écart-type sous 0,01, il faut $n \ge 0{,}21/10^{-4} = 2\,100$ labels. Sur 25 exemples, « 0,32 » a "
         r"une incertitude de l'ordre de $\pm 0{,}09$ : le deuxième chiffre ne veut rien dire.",
)

M13A_28_GIVEN = '''def simplex_grid(n=60):
    """The laws (p1, p2, p3) whose coordinates are multiples of 1/n, one law per row."""
    i, j = np.meshgrid(np.arange(n + 1), np.arange(n + 1), indexing="ij")
    keep = i + j <= n
    return np.column_stack([i[keep], j[keep], n - i[keep] - j[keep]]) / n


def to_plane(P):
    """The points of the plane of the laws P (one per row): the laws (1, 0, 0), (0, 1, 0) and (0, 0, 1) go to the
    vertices (0, 0), (1, 0) and (1/2, √3/2) of an equilateral triangle."""
    P = np.asarray(P, dtype=float)
    return P[:, 1] + P[:, 2] / 2, P[:, 2] * math.sqrt(3) / 2'''

M13A_28_CHECK = '''with checked("M13a.28"):
    from scipy.stats import entropy as scipy_entropy

    LAWS_28 = np.array([[0.6, 0.3, 0.1], [0.0, 0.75, 0.25], [1.0, 0.0, 0.0], [0.2, 0.2, 0.6], [0.45, 0.1, 0.45]])
    GRID_28 = simplex_grid()
    results_28 = []

    def report_28(ok, success, failure):
        results_28.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))

    with warnings.catch_warnings(record=True) as caught_h:
        warnings.simplefilter("always")
        h_laws, h_grid = np.asarray(entropy_bits(LAWS_28), dtype=float), np.asarray(entropy_bits(GRID_28), dtype=float)
    with warnings.catch_warnings(record=True) as caught_g:
        warnings.simplefilter("always")
        g_laws, g_grid = np.asarray(gini(LAWS_28), dtype=float), np.asarray(gini(GRID_28), dtype=float)
    h_ok_28 = bool(h_laws.shape == (5,) and np.allclose(h_laws, scipy_entropy(LAWS_28.T, base=2), rtol=0, atol=1e-12)
                   and h_grid.shape == (len(GRID_28),) and not caught_h)
    g_ok_28 = bool(g_laws.shape == (5,) and np.allclose(g_laws, 1 - np.sum(LAWS_28 ** 2, axis=1), rtol=0, atol=1e-12)
                   and g_grid.shape == (len(GRID_28),) and not caught_g)
    report_28(h_ok_28, "entropy_bits : une entropie par loi, en bits, 0 log₂ 0 compris, sans avertissement",
              "entropy_bits : une entropie par LIGNE, en bits (log₂), où un terme 0 log₂ 0 compte pour 0 sans calculer "
              "log₂ 0 (np.where ou un masque), sans avertissement")
    report_28(g_ok_28, "gini : un indice de Gini par loi", "gini : 1 − la somme des carrés, une valeur par LIGNE")
    right_28 = [(f, values) for f, values, ok in ((entropy_bits, h_grid, h_ok_28), (gini, g_grid, g_ok_28)) if ok]
    if len(right_28) < 2:                            # the properties below are checked on right values only
        results_28.append(False)
        print("ℹ️ la symétrie, le maximum et la concavité se vérifient une fois les valeurs des deux impuretés justes")
    if right_28:
        swaps_28 = [[1, 2, 0], [1, 0, 2]]            # a rotation and a reflection of the triangle
        report_28(all(np.allclose(np.asarray(f(GRID_28[:, s]), dtype=float), values, rtol=0, atol=1e-12)
                      for f, values in right_28 for s in swaps_28),
                  "les impuretés ne dépendent pas de l'ordre des issues : leurs lignes de niveau ont les symétries du "
                  "triangle",
                  "une impureté change quand on permute les issues : elle doit traiter les trois de la même façon")
        center_28 = np.full(3, 1 / 3)
        report_28(all(np.allclose(GRID_28[np.argmax(values)], center_28) for _, values in right_28),
                  "le maximum est au centre du triangle, la loi uniforme",
                  "le maximum de tes impuretés n'est pas au centre du triangle : relis tes formules")
        pairs_28 = np.random.default_rng(4128).dirichlet(np.ones(3), size=(200, 2))
        middle_28 = pairs_28.mean(axis=1)
        report_28(all(np.all(np.asarray(f(middle_28), dtype=float)
                             >= (np.asarray(f(pairs_28[:, 0]), dtype=float) + np.asarray(f(pairs_28[:, 1]), dtype=float)) / 2
                             - 1e-12) for f, _ in right_28),
                  "concaves : l'impureté d'un mélange de deux lois est au moins la moyenne de leurs impuretés",
                  "une de tes impuretés n'est pas concave sur 200 couples de lois : relis tes formules")
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
    try:
        opened_28 = drawn(draw_impurities, axes)
    except BaseException:
        plt.close(fig)
        raise
    report_28(not opened_28 and all(ax.collections or ax.lines for ax in axes),
              "draw_impurities dessine dans les deux axes reçus",
              "draw_impurities doit dessiner dans les deux axes reçus, sans ouvrir de figure (ni plt.figure ni "
              "plt.subplots)")
    plt.show()
    verdict("M13a.28", all(results_28), "les impuretés et leur figure sont justes.",
            "relis les lignes ❌ ci-dessus.")'''

M13A_28 = Ex(
    "M13a.28", "🎨", 1, 20, "L'entropie et l'indice de Gini sur les lois à trois issues : lignes de niveau et "
    "maximum au centre",
    "dessiner l'entropie et l'indice de Gini sur le triangle des lois à trois issues, et voir où et comment ils sont "
    "maximaux.", "fiche §6", tracks="C, E", given=M13A_28_GIVEN,
    body=r"""Une loi à trois issues $(p_1, p_2, p_3)$, positive et de somme 1, est un point d'un triangle : chaque sommet est une loi certaine, le milieu d'un côté une loi qui partage sa masse entre deux issues, le centre la loi uniforme. La cellule fournie donne `simplex_grid()`, une grille de lois (une par ligne, de coordonnées multiples de $\frac{1}{60}$), et `to_plane(P)`, qui place chaque loi dans le triangle. Écris :
- `entropy_bits(P)` : l'entropie en bits de chaque loi (une par ligne), $-\sum_k p_k\log_2 p_k$, où un terme $0 \log_2 0$ compte pour 0 **sans** calculer $\log_2 0$ (aucun avertissement) ;
- `gini(P)` : l'indice de Gini $1 - \sum_k p_k^2$ de chaque loi ;
- `draw_impurities(axes)` : dans les deux axes reçus (sans en ouvrir d'autres), le triangle et les lignes de niveau de l'entropie (à gauche) et de l'indice de Gini (à droite) sur `simplex_grid()`, avec `ax.tricontourf` ou `ax.tricontour` sur les points de `to_plane`, et une marque à la loi où chacun est le plus grand. Mets `ax.set_aspect("equal")` et un titre par axe.

La cellule de vérification contrôle tes valeurs sur cinq lois (comparées à `scipy.stats.entropy`), la symétrie des deux impuretés quand on permute les issues, la position de leur maximum, leur concavité sur 200 couples de lois, puis trace ta figure.

Dans ta copie : où est le maximum de chaque impureté, et pour quelle loi ? Pourquoi les lignes de niveau de Gini sont-elles des cercles centrés au centre du triangle (développe $\lVert \mathbf{p} - \mathbf{u} \rVert^2$, avec $\mathbf{u}$ la loi uniforme) ? Celles de l'entropie en sont-elles ? Sur un côté du triangle, une issue a la probabilité 0 : quelle fonction d'une seule variable retrouves-tu ? Près d'un sommet, quelle impureté monte le plus vite, et pourquoi (regarde la pente de $-p\log_2 p$ en 0) ?""",
    todo='''def entropy_bits(P):
    """The entropies in bits of the laws P (one per row), where a term 0 log₂ 0 counts as 0: an array."""
    raise NotImplementedError("−Σ p log₂ p sur chaque ligne, sans jamais calculer log₂ 0")


def gini(P):
    """The Gini indices 1 − Σ p_k² of the laws P (one per row): an array."""
    raise NotImplementedError("1 − la somme des carrés de chaque ligne")


def draw_impurities(axes):
    """In the two axes received (and no other): the triangle of the laws with three outcomes, the level lines of the
    entropy (left) and of the Gini index (right) on simplex_grid(), and a marker at the law where each is largest."""
    raise NotImplementedError("to_plane(simplex_grid()), ax.tricontourf, puis ax.plot pour le triangle et le maximum")''',
    check=M13A_28_CHECK,
    solution='''def entropy_bits(P):
    """The entropies in bits of the laws P (one per row), where a term 0 log₂ 0 counts as 0: an array."""
    P = np.asarray(P, dtype=float)
    logs = np.log2(np.where(P > 0, P, 1.0))          # log₂ 1 = 0 where p = 0: the term 0 log₂ 0 counts as 0
    return -np.sum(P * logs, axis=1)


def gini(P):
    """The Gini indices 1 − Σ p_k² of the laws P (one per row): an array."""
    P = np.asarray(P, dtype=float)
    return 1 - np.sum(P ** 2, axis=1)


def draw_impurities(axes):
    """In the two axes received (and no other): the triangle of the laws with three outcomes, the level lines of the
    entropy (left) and of the Gini index (right) on simplex_grid(), and a marker at the law where each is largest."""
    grid = simplex_grid()
    xs, ys = to_plane(grid)
    cx, cy = to_plane(np.eye(3))
    for ax, values, title in zip(axes, (entropy_bits(grid), gini(grid)), ("entropie (bits)", "indice de Gini")):
        ax.tricontourf(xs, ys, values, levels=12, cmap="viridis")
        ax.tricontour(xs, ys, values, levels=12, colors="white", linewidths=0.6)
        ax.plot(np.append(cx, cx[0]), np.append(cy, cy[0]), color="black", lw=1)
        best = int(np.argmax(values))
        ax.plot(xs[best], ys[best], marker="*", color="red", markersize=14)
        for x, y, label in zip(cx, cy, ("(1, 0, 0)", "(0, 1, 0)", "(0, 0, 1)")):
            ax.annotate(label, (x, y), textcoords="offset points", xytext=(0, -14 if y == 0 else 6), ha="center")
        ax.set_xlim(-0.12, 1.12)
        ax.set_ylim(-0.1, 1.0)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title)


''' + M13A_28_CHECK,
    note=r"Les deux impuretés sont maximales au centre, la loi uniforme $(\frac{1}{3}, \frac{1}{3}, \frac{1}{3})$, et "
         r"nulles aux sommets. Avec $\mathbf{u}$ la loi uniforme, $\lVert \mathbf{p} - \mathbf{u} \rVert^2 = \sum_k "
         r"p_k^2 - \frac{2}{3}\sum_k p_k + \frac{1}{3} = \sum_k p_k^2 - \frac{1}{3}$ : l'indice de Gini ne dépend que de "
         r"la distance au centre, ses lignes de niveau sont des cercles (coupés par les côtés). Celles de l'entropie "
         r"n'en sont pas : elles s'arrondissent près du centre et s'aplatissent le long des côtés. Sur un côté, on "
         r"retrouve l'entropie et le Gini d'une loi à deux issues. Près d'un sommet, l'entropie monte bien plus vite : "
         r"la pente de $-p\log_2 p$ est infinie en $p = 0$, celle de $p(1 - p)$ vaut 1 ; c'est pourquoi l'entropie "
         r"« voit » mieux les classes rares.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M13a.29 to M13a.31)
# ---------------------------------------------------------------------------
M13A_29_GIVEN = '''Y_29 = np.array([1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0])                                  # 12 labels
P_29 = np.array([0.9, 0.0, 0.25, 1.0, 0.7, 0.4, 0.05, 0.55, 0.0, 0.3, 0.85, 0.15])           # a model's P(Y = 1), rounded
Z_29 = np.array([2.1, -800.0, -1.3, 800.0, 0.8, -0.2, -3.1, 0.3, -5.0, -0.9, 1.7, -2.4])    # another model's scores
X_29 = np.round(np.random.default_rng(4129).normal(5.0, 2.0, size=12), 2)                   # 12 measures'''

M13A_29_MISTAKES = bug_letters_mistakes(
    "ABCG", "DEF",
    {"A": "regarde ce que vaut chaque terme quand une probabilité vaut exactement 0 ou 1",
     "B": "regarde ce que calcule NumPy pour chaque valeur de z, les plus négatives surtout",
     "C": "regarde ce que devient e^z en flottants pour les plus grandes valeurs de z",
     "G": "regarde les conventions de NumPy, et la formule du maximum de vraisemblance d'une variance"},
    name_correct=False)

M13A_29 = Ex(
    "M13a.29", "🐛", 1, 15, "Chasse à l'erreur : un ln 0, une sigmoïde qui déborde, une variance de maximum de "
    "vraisemblance divisée par n − 1",
    "repérer dans un code de résumé d'un modèle les erreurs classiques de la vraisemblance et des scores, puis "
    "calculer les bonnes valeurs.", "fiche §1 à §3", tracks="C", given=M13A_29_GIVEN,
    body=r"""Un collègue résume les sorties de deux modèles et un échantillon (la cellule fournie) : les probabilités `P_29` (arrondies : certaines valent exactement 0 ou 1), les scores `Z_29` (dont deux immenses) et des mesures `X_29`. Sept lignes portent une lettre et un commentaire qui dit ce qu'elles doivent calculer. Quatre lignes ne font pas ce que dit leur commentaire. **Sans exécuter son code**, trouve-les.

```python
y, p, z, x = Y_29, P_29, Z_29, X_29
ll = np.sum(y * np.log(p) + (1 - y) * np.log(1 - p))       # (A) the log-likelihood of the labels y under p
prob = 1 / (1 + np.exp(-z))                                 # (B) σ(z), without any warning, even for z = −800
loss = np.mean(np.log(1 + np.exp(z)) - y * z)               # (C) the mean logistic loss of the scores z
p_hat = np.mean(y)                                          # (D) the maximum likelihood estimate of P(Y = 1)
base = -(p_hat * np.log(p_hat) + (1 - p_hat) * np.log(1 - p_hat))   # (E) the log-loss of the constant model p̂
mu = np.mean(x)                                             # (F) the maximum likelihood estimate of μ
var = np.var(x, ddof=1)                                     # (G) the maximum likelihood estimate of σ²
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) la bonne valeur de `ll` (4 décimales) ;
- c) la bonne valeur de `loss` (4 décimales) ;
- d) la bonne valeur de `var` (4 décimales).

Pour b) à d), écris le code corrigé dans la cellule (c'est permis : seule la recherche des lignes fausses se fait sans exécuter).

Dans ta copie : pour chaque ligne fausse, que se passe-t-il exactement (une valeur, `nan`, `inf`, un avertissement), et comment la corriger ? Laquelle donne une valeur juste mais avec un avertissement ? Laquelle donne un nombre faux sans aucun signal ? Pourquoi la ligne (E), qui ressemble à (A), est-elle juste ici ?""",
    todo='''answer_M13a_29a = ...  # a) letters, as text
answer_M13a_29b = ...  # b) a number (4 decimals)
answer_M13a_29c = ...  # c) a number (4 decimals)
answer_M13a_29d = ...  # d) a number (4 decimals)''',
    check='''for letter, answer in zip("abcd", [answer_M13a_29a, answer_M13a_29b, answer_M13a_29c, answer_M13a_29d]):
    wbm.check(f"M13a.29{letter}", answer)''',
    solution='''answer_M13a_29a = "ABCG"
y_29, p_29, z_29, x_29 = Y_29, P_29, Z_29, X_29
ll_29 = float(np.sum(np.log(np.where(y_29 == 1, p_29, 1 - p_29))))   # (A) the probability of the OBSERVED label only
e_29 = np.exp(-np.abs(z_29))                                         # (B) at most 1: no overflow
prob_29 = np.where(z_29 >= 0, 1 / (1 + e_29), e_29 / (1 + e_29))
loss_29 = float(np.mean(np.maximum(z_29, 0) + np.log1p(e_29) - y_29 * z_29))   # (C) the stable softplus
var_29 = float(np.var(x_29))                                         # (G) the maximum likelihood divides by n
answer_M13a_29b, answer_M13a_29c, answer_M13a_29d = round(ll_29, 4), round(loss_29, 4), round(var_29, 4)
print(answer_M13a_29a, answer_M13a_29b, answer_M13a_29c, answer_M13a_29d)
with warnings.catch_warnings(record=True) as caught_29:               # what the colleague's lines give
    warnings.simplefilter("always")
    wrong_29 = (np.sum(y_29 * np.log(p_29) + (1 - y_29) * np.log(1 - p_29)), (1 / (1 + np.exp(-z_29)))[1],
                np.mean(np.log(1 + np.exp(z_29)) - y_29 * z_29), np.var(x_29, ddof=1))
print("lignes du collègue : (A)", wrong_29[0], " (B) σ(−800) =", wrong_29[1], " (C)", wrong_29[2],
      " (G)", round(float(wrong_29[3]), 4))
print("avertissements :", sorted({str(w.message) for w in caught_29}))''',
    record=f'''wbm.record("M13a.29a", "ABCG",
           mistakes={M13A_29_MISTAKES})
Y_29r = np.array([1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0])
P_29r = np.array([0.9, 0.0, 0.25, 1.0, 0.7, 0.4, 0.05, 0.55, 0.0, 0.3, 0.85, 0.15])
Z_29r = np.array([2.1, -800.0, -1.3, 800.0, 0.8, -0.2, -3.1, 0.3, -5.0, -0.9, 1.7, -2.4])
X_29r = np.round(np.random.default_rng(4129).normal(5.0, 2.0, size=12), 2)
ll_29r = float(np.sum(np.log(np.where(Y_29r == 1, P_29r, 1 - P_29r))))
loss_29r = float(np.mean(np.logaddexp(0, Z_29r) - Y_29r * Z_29r))
wbm.record("M13a.29b", ll_29r, decimals=4,
           mistakes={{"(A) calcule une log-vraisemblance : une SOMME sur les labels, pas une moyenne": ll_29r / 12}})
wbm.record("M13a.29c", loss_29r, decimals=4,
           mistakes={{"e^800 déborde : écris la softplus max(z, 0) + ln(1 + e^(−|z|))": math.inf,
                     "{MEAN}": loss_29r * 12}})
wbm.record("M13a.29d", float(np.var(X_29r)), decimals=4,
           mistakes={{"le maximum de vraisemblance d'une variance divise par n, pas par n − 1": float(np.var(X_29r, ddof=1))}})''',
    note=r"(A) Quand $p_i = 0$ pour un label 0, ou $p_i = 1$ pour un label 1, la formule calcule $0 \times \ln 0 = 0 "
         r"\times (-\infty)$ : `nan`, qui contamine la somme (et deux avertissements) ; il faut ne prendre le $\ln$ que de "
         r"la probabilité du label observé (`np.where`), ou `scipy.special.xlogy`. (B) Pour $z = -800$, $e^{800}$ déborde "
         r"en `inf`, et $1/(1 + \infty) = 0$ : la valeur est juste, mais avec un avertissement d'overflow ; pour "
         r"$z < 0$, on écrit $\frac{e^{z}}{1 + e^{z}}$. (C) Pour $z = 800$, `np.log(1 + np.exp(z))` vaut `inf`, et la "
         r"log-loss aussi, alors que le modèle a raison (score 800, label 1) : la softplus stable donne 0,2106. (G) "
         r"`ddof=1` divise par $n - 1$ : un nombre plausible, faux sans aucun signal, le piège le plus dangereux. (E) "
         r"est juste parce que $\hat{p} = \frac{5}{12}$ n'est ni 0 ni 1 : un $\hat{p}$ calculé sur des labels "
         r"n'atteint 0 ou 1 que si tous les labels sont égaux.",
)

M13A_30_GIVEN = '''p = sympy.symbols("p", positive=True)
lam = sympy.symbols("lambda", positive=True)
GEOM_30 = [3, 1, 4, 2, 5]        # observations of a geometric law: P(X = k) = (1 − p)^(k − 1) p, k = 1, 2, ...
POIS_30 = [2, 0, 3, 1, 4, 2]     # observations of a Poisson law: P(X = k) = e^(−λ) λ^k / k!, k = 0, 1, ...'''

M13A_30_CHECK = '''with checked("M13a.30"):
    def at_30(expr, symbol, point):
        """The value of the SymPy expression expr at symbol = point, as a float (None if not a real number)."""
        try:
            value = complex(sympy.sympify(expr).subs(symbol, point).evalf())
        except (TypeError, ValueError, AttributeError, sympy.SympifyError):
            return None
        return value.real if abs(value.imag) < 1e-12 else None

    def same_30(expr, reference, symbol, points, constant=False):
        """True when expr equals reference at the points (up to an additive constant if constant)."""
        gaps = []
        for point in points:
            a, b = at_30(expr, symbol, point), at_30(reference, symbol, point)
            if a is None or b is None:
                return False
            gaps.append((a - b, max(1.0, abs(b))))
        shift = gaps[0][0] if constant else 0.0
        return all(abs(gap - shift) <= 1e-9 * size for gap, size in gaps)

    def number_30(expr, expected):
        """True when expr is one number equal to expected; else False, or the reason as a text."""
        if isinstance(expr, (list, tuple, set, dict)):
            return "sympy.solve rend une LISTE de solutions : prends-en l'élément, sympy.solve(...)[0]"
        try:
            free = sympy.sympify(expr).free_symbols
            if free:
                return (f"c'est encore une expression de {', '.join(sorted(map(str, free)))} : remplace la variable "
                        f"par la solution, avec .subs(...)")
            return abs(float(sympy.sympify(expr)) - expected) <= 1e-9 * max(1.0, abs(expected))
        except (TypeError, ValueError, AttributeError, sympy.SympifyError):
            return False

    ref_geom_30 = sum((k - 1) * sympy.log(1 - p) + sympy.log(p) for k in GEOM_30)
    ref_pois_30 = sum(x * sympy.log(lam) - lam for x in POIS_30)
    items_30 = [
        ("ell_geom", lambda: ell_geom, lambda e: same_30(e, ref_geom_30, p, [0.2, 0.45, 0.8]),
         "ℓ(p), la log-vraisemblance géométrique : une somme de ln((1 − p)^(kᵢ − 1) p) sur les cinq observations"),
        ("dell_geom", lambda: dell_geom, lambda e: same_30(e, sympy.diff(ref_geom_30, p), p, [0.2, 0.45, 0.8]),
         "ℓ′(p) : sympy.diff(ell_geom, p)"),
        ("p_hat", lambda: p_hat, lambda e: number_30(e, 1 / sum(GEOM_30) * len(GEOM_30)),
         "p̂ : la solution de ℓ′(p) = 0 (sympy.solve), dans ]0, 1["),
        ("d2_geom", lambda: d2_geom,
         lambda e: number_30(e, float(sympy.diff(ref_geom_30, p, 2).subs(p, sympy.Rational(len(GEOM_30), sum(GEOM_30))))),
         "ℓ″(p̂) : la dérivée seconde de ℓ, puis .subs(p, p_hat)"),
        ("ell_pois", lambda: ell_pois, lambda e: same_30(e, ref_pois_30, lam, [0.7, 2.0, 3.5], constant=True),
         "ℓ(λ), la log-vraisemblance de Poisson : une somme de ln(e^(−λ) λ^(xᵢ) / xᵢ!)"),
        ("lam_hat", lambda: lam_hat, lambda e: number_30(e, sum(POIS_30) / len(POIS_30)),
         "λ̂ : la solution de ℓ′(λ) = 0"),
        ("d2_pois", lambda: d2_pois, lambda e: number_30(e, -sum(POIS_30) / (sum(POIS_30) / len(POIS_30)) ** 2),
         "ℓ″(λ̂) : la dérivée seconde de ℓ en λ̂"),
    ]
    done_30, right_30 = 0, 0
    for name, get, test, what in items_30:
        value = get()
        if not filled(value):
            print(f"⏳ {name} : pas encore écrit")
            continue
        done_30 += 1
        result = test(value)
        ok = result is True
        right_30 += ok
        print(f"✅ {name}" if ok else f"❌ {name} : {result if isinstance(result, str) else what}")
    if done_30 < len(items_30):
        print(f"⏳ Ex M13a.30 : {done_30} objets sur {len(items_30)} écrits, dont {right_30} justes.")
    else:
        verdict("M13a.30", right_30 == len(items_30),
                "SymPy confirme les deux maxima de vraisemblance, et le signe de la dérivée seconde dit que ce sont "
                "des maxima.", f"{len(items_30) - right_30} objet(s) faux : relis les lignes ❌ ci-dessus.")'''

M13A_30 = Ex(
    "M13a.30", "🛠️", 1, 15, "Vérifier avec SymPy le maximum de vraisemblance d'une loi géométrique et d'une loi de "
    "Poisson",
    "faire calculer par SymPy une log-vraisemblance, sa dérivée, son point critique et le signe de sa dérivée "
    "seconde, pour vérifier un maximum de vraisemblance fait à la main.", "fiche §1 ; M05a", tracks="C",
    given=M13A_30_GIVEN,
    body=r"""Vérifier un calcul à la main avec un logiciel de calcul formel, c'est un geste de métier. La cellule fournie définit les symboles `p` et `lam` (positifs) et deux échantillons :
- `GEOM_30`, cinq observations d'une loi **géométrique** (le rang du premier succès, $P(X = k) = (1 - p)^{k - 1}p$ pour $k \ge 1$) ;
- `POIS_30`, six observations d'une loi de **Poisson** ($P(X = k) = e^{-\lambda}\frac{\lambda^k}{k!}$ pour $k \ge 0$).

Fais d'abord le calcul à la main, dans ta copie : écris $\ell(p)$, dérive, résous $\ell'(p) = 0$ (tu dois trouver $\hat{p} = 1/\bar{x}$), et le signe de $\ell''$ ; de même pour $\lambda$ (tu dois trouver $\hat{\lambda} = \bar{x}$). Puis fais-le faire par SymPy, en définissant :
- `ell_geom` : $\ell(p)$ pour `GEOM_30`, une expression SymPy (une somme de `sympy.log(...)` sur les observations) ;
- `dell_geom` : sa dérivée, par `sympy.diff` ;
- `p_hat` : la solution de $\ell'(p) = 0$, par `sympy.solve` (un nombre SymPy, pas la liste que rend `solve`) ;
- `d2_geom` : $\ell''(\hat{p})$, la dérivée seconde en $\hat{p}$ (`sympy.diff(..., p, 2)`, puis `.subs(p, p_hat)`) ;
- `ell_pois`, `lam_hat` et `d2_pois` : la même chose pour `POIS_30` et $\lambda$ (les termes constants $-\ln x_i!$ peuvent être omis : ils ne changent ni la dérivée ni le maximum).

La cellule de vérification compare chacun de tes objets à un calcul indépendant (en quelques points pour les expressions) et dit ✅ ou ❌.

Dans ta copie : pourquoi le signe de $\ell''(\hat{p})$ suffit-il à conclure à un maximum ici (regarde le signe de $\ell''(p)$ sur tout $]0, 1[$) ? `sympy.solve` a-t-il trouvé d'autres solutions, et pourquoi pas ? Écris $\hat{p}$ et $\hat{\lambda}$ en fonction de $\bar{x}$ : lequel des deux est une moyenne, lequel l'inverse d'une moyenne, et pourquoi est-ce naturel (l'espérance d'une loi géométrique est $\frac{1}{p}$) ?""",
    todo='''ell_geom = ...    # ℓ(p) for GEOM_30: a SymPy expression in p
dell_geom = ...   # ℓ′(p), with sympy.diff
p_hat = ...       # the solution of ℓ′(p) = 0, with sympy.solve: one SymPy number, not a list
d2_geom = ...     # ℓ″(p̂): a SymPy number
ell_pois = ...    # ℓ(λ) for POIS_30, a SymPy expression in lam (the constants −ln(xᵢ!) may be left out)
lam_hat = ...     # the solution of ℓ′(λ) = 0
d2_pois = ...     # ℓ″(λ̂)''',
    check=M13A_30_CHECK,
    solution='''ell_geom = sum(sympy.log((1 - p) ** (k - 1) * p) for k in GEOM_30)
dell_geom = sympy.diff(ell_geom, p)
p_hat = sympy.solve(sympy.Eq(dell_geom, 0), p)[0]
d2_geom = sympy.simplify(sympy.diff(ell_geom, p, 2).subs(p, p_hat))
ell_pois = sum(sympy.log(sympy.exp(-lam) * lam ** x / sympy.factorial(x)) for x in POIS_30)
lam_hat = sympy.solve(sympy.diff(ell_pois, lam), lam)[0]
d2_pois = sympy.simplify(sympy.diff(ell_pois, lam, 2).subs(lam, lam_hat))
print("ℓ′(p) =", sympy.simplify(dell_geom), " ; solutions :", sympy.solve(dell_geom, p), " ; ℓ″(p̂) =", d2_geom)
print("ℓ″(p) =", sympy.simplify(sympy.diff(ell_geom, p, 2)))
print("ℓ′(λ) =", sympy.simplify(sympy.diff(ell_pois, lam)), " ; λ̂ =", lam_hat, " ; ℓ″(λ̂) =", d2_pois)


''' + M13A_30_CHECK,
    note=r"Géométrique : $\ell(p) = \sum_i \big[(k_i - 1)\ln(1 - p) + \ln p\big] = 10\ln(1 - p) + 5\ln p$, $\ell'(p) = "
         r"\frac{5}{p} - \frac{10}{1 - p}$, nul en $\hat{p} = \frac{5}{15} = \frac{1}{3} = \frac{1}{\bar{x}}$ "
         r"($\bar{x} = 3$) ; $\ell''(p) = -\frac{5}{p^2} - \frac{10}{(1 - p)^2} < 0$ sur tout $]0, 1[$ : $\ell$ est "
         r"concave, le point critique est l'unique maximum, et $\ell''(\hat{p}) = -45 - 22{,}5 = -\frac{135}{2}$. "
         r"Poisson : $\ell(\lambda) = 12\ln\lambda - 6\lambda - \sum_i \ln x_i!$, $\ell'(\lambda) = \frac{12}{\lambda} - "
         r"6$, nul en $\hat{\lambda} = 2 = \bar{x}$, et $\ell''(\hat{\lambda}) = -\frac{12}{4} = -3$. `solve` ne trouve "
         r"qu'une solution : l'équation se ramène à une équation du premier degré. Le maximum de vraisemblance égale "
         r"l'espérance du modèle à la moyenne observée : $\frac{1}{p} = \bar{x}$ pour la géométrique, $\lambda = \bar{x}$ "
         r"pour Poisson.",
)

M13A_31_GIVEN = '''def normal_pdf(x, mu, sigma):
    """The density of N(mu, sigma²) at x."""
    return np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))


def mixture_sample(seed, weight, n=400):
    """n points of the mixture weight · N(2.5, 1) + (1 − weight) · N(0, 1)."""
    rng = np.random.default_rng(seed)
    from_f1 = rng.random(n) < weight
    return np.where(from_f1, rng.normal(2.5, 1.0, n), rng.normal(0.0, 1.0, n))


def make_loglik(x):
    """(ell, dell): the log-likelihood ℓ(π) of the mixture π f₁ + (1 − π) f₀ (f₁ = N(2.5, 1), f₀ = N(0, 1)) for the
    sample x, and its derivative ℓ′(π). Both take one number π of [0, 1]."""
    x = np.asarray(x, dtype=float)
    f0, f1 = normal_pdf(x, 0.0, 1.0), normal_pdf(x, 2.5, 1.0)

    def ell(pi):
        return float(np.sum(np.log(pi * f1 + (1 - pi) * f0)))

    def dell(pi):
        return float(np.sum((f1 - f0) / (pi * f1 + (1 - pi) * f0)))

    return ell, dell


X_31 = mixture_sample(4131, 0.35)                # 400 points; you know f₀ and f₁, not the proportion π
ell_31, dell_31 = make_loglik(X_31)
MAX_CALLS_31 = 200'''

M13A_31_CHECK = '''with checked("M13a.31 défi"):
    import inspect
    import re

    from scipy.optimize import brentq                # the reference maximum (forbidden in find_weight)

    problems_31, ok_31, ran_31 = [], False, False
    try:
        source_31 = inspect.getsource(find_weight)
    except (OSError, TypeError):
        source_31 = ""
    banned_31 = sorted(set(re.findall(r"\\b(scipy|optimize|minimize|minimize_scalar|brentq|fsolve|polyfit|sklearn|"
                                      r"X_31|ell_31|dell_31|make_loglik|normal_pdf|mixture_sample)\\b", source_31)))
    if banned_31:
        ran_31 = True
        problems_31.append(f"find_weight utilise {', '.join(banned_31)}, interdit dans ce défi")
    samples_31 = [("l'échantillon X_31", X_31), ("un autre échantillon, d'une autre proportion", mixture_sample(4132, 0.6))]
    for name_t, x_t in ([] if banned_31 else samples_31):
        ell_t, dell_t = make_loglik(x_t)
        if dell_t(0.0) <= 0:
            best_t = 0.0
        elif dell_t(1.0) >= 0:
            best_t = 1.0
        else:
            best_t = brentq(dell_t, 0.0, 1.0, xtol=1e-15, rtol=1e-15)
        calls_t = [0]

        def counted(function, calls=calls_t):
            def wrapper(pi):
                if np.ndim(pi) != 0:
                    raise TypeError("ell et dell prennent un seul nombre π, pas un tableau")
                calls[0] += 1
                return function(float(pi))
            return wrapper

        try:
            pi_t = find_weight(counted(ell_t), counted(dell_t))
        except NotImplementedError:
            raise
        except Exception as exc:  # noqa: BLE001
            ran_31 = True
            problems_31.append(f"find_weight lève {type(exc).__name__} ({exc})")
            break
        ran_31 = True
        try:
            pi_t = float(pi_t)
        except (TypeError, ValueError):
            problems_31.append(f"find_weight doit rendre un nombre, pas {type(pi_t).__name__}")
            break
        gap_t = abs(pi_t - best_t)
        print(f"{name_t} : {calls_t[0]} évaluations de ell et dell, écart au maximum {gap_t:.1e}".replace(".", ","))
        if calls_t[0] > MAX_CALLS_31:
            problems_31.append(f"{name_t} : {calls_t[0]} évaluations, au-dessus du budget de {MAX_CALLS_31}")
        if not gap_t <= 1e-6:
            problems_31.append(f"{name_t} : ton π̂ est à {gap_t:.1e} du maximum, plus que 1e−6".replace(".", ","))
        if problems_31:
            break
    if problems_31:
        print("❌ Ex M13a.31 : " + " ; ".join(problems_31) + ".")
    elif ran_31:
        ok_31 = True
        print("✅ Ex M13a.31 : défi réussi : le maximum à 1e−6 près, en au plus 200 évaluations, sur les deux échantillons.")'''

M13A_31 = Ex(
    "M13a.31", "🏆", 3, 25, "Défi : la proportion d'un mélange de deux lois connues par maximum de vraisemblance, à "
    "1e−6 près du maximum (dichotomie ou Newton)",
    "trouver numériquement un maximum de vraisemblance qui n'a pas de formule, avec une méthode qui garantit sa "
    "précision et un budget d'évaluations.", "fiche §1 ; M05a ; M10", tracks="C", given=M13A_31_GIVEN,
    body=r"""Des mesures viennent de deux sources mélangées, de densités **connues** $f_0 = \mathcal{N}(0, 1)$ et $f_1 = \mathcal{N}(2{,}5 ;\ 1)$, dans une proportion $\pi$ **inconnue** : chaque mesure suit la densité $\pi f_1(x) + (1 - \pi) f_0(x)$. Les 400 mesures `X_31` (cellule fournie) donnent la log-vraisemblance et sa dérivée

$$\ell(\pi) = \sum_{i=1}^{400} \ln\big(\pi f_1(x_i) + (1 - \pi) f_0(x_i)\big), \qquad \ell'(\pi) = \sum_{i=1}^{400} \frac{f_1(x_i) - f_0(x_i)}{\pi f_1(x_i) + (1 - \pi) f_0(x_i)},$$

calculées par `ell_31` et `dell_31`. Annuler $\ell'$ ne donne pas de formule : il faut chercher le maximum numériquement. Bonne nouvelle, $\ell$ est **concave** sur $[0, 1]$ (calcule $\ell''$ : une somme de carrés changée de signe), donc $\ell'$ décroît, et un point où elle s'annule est le maximum.

**L'objectif** : écrire `find_weight(ell, dell)`, qui reçoit deux fonctions d'un seul nombre $\pi$ (comme `ell_31` et `dell_31`) et rend le $\hat{\pi} \in [0, 1]$ qui maximise `ell`, à $10^{-6}$ près du vrai maximum, en appelant `ell` et `dell` **au plus 200 fois** en tout. La vérification compte les appels, et essaie ta fonction sur `X_31` puis sur un autre échantillon, d'une autre proportion : ta fonction ne doit utiliser que les deux fonctions reçues (ni `X_31`, ni `ell_31`, ni `make_loglik`). Une recherche sur une grille ne suffit pas : $10^{-6}$ près demanderait un million de points. `scipy.optimize` (`minimize`, `brentq`, `fsolve`…), `np.polyfit` et scikit-learn sont interdits. Pense à la **dichotomie** sur $\ell'$ (M05a) ou à la méthode de **Newton** (une dérivée seconde approchée par les valeurs de `dell`), et au cas où le maximum serait au bord, en 0 ou en 1.

Une dernière cellule enregistre si l'objectif est atteint.

Dans ta copie : combien d'évaluations ta méthode a-t-elle utilisées, et combien en faudrait-il, au minimum, pour une précision de $10^{-12}$ ? Pourquoi la concavité garantit-elle que ta méthode ne s'arrête pas sur un faux maximum ? Ton $\hat{\pi}$ est-il égal à la proportion de points venus de $f_1$, et pourquoi pas exactement ?""",
    todo='''def find_weight(ell, dell):
    """The π in [0, 1] that maximizes ell (a concave function), to 1e-6, with at most MAX_CALLS_31 calls of ell and
    dell together; dell is the derivative of ell. Both take one number π."""
    raise NotImplementedError("dichotomie sur le signe de dell, ou méthode de Newton, en au plus 200 appels")''',
    check=M13A_31_CHECK + '''
with checked("M13a.31"):
    if not ran_31:                               # ⏳ while find_weight is not written
        raise NotImplementedError("find_weight n'est pas encore écrite")
    wbm.check("M13a.31", bool(ok_31), computed=True)''',
    solution='''def find_weight(ell, dell):
    """The π in [0, 1] that maximizes ell (a concave function), to 1e-6, with at most MAX_CALLS_31 calls of ell and
    dell together; dell is the derivative of ell. Both take one number π."""
    lo, hi = 0.0, 1.0
    if dell(lo) <= 0:                            # ℓ decreases on [0, 1]: the maximum is at 0
        return lo
    if dell(hi) >= 0:                            # ℓ increases on [0, 1]: the maximum is at 1
        return hi
    while hi - lo > 1e-9:                        # dell decreases: keep the sign change inside [lo, hi]
        mid = (lo + hi) / 2
        if dell(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


pi_hat_31 = find_weight(ell_31, dell_31)
print(f"π̂ = {pi_hat_31:.6f}, ℓ(π̂) = {ell_31(pi_hat_31):.4f}".replace(".", ","))
pis_31 = np.linspace(0.0, 1.0, 201)
fig, ax = plt.subplots(figsize=(6.5, 3.2))
ax.plot(pis_31, [ell_31(q) for q in pis_31])
ax.axvline(pi_hat_31, color="C3", lw=0.8, ls="--", label="π̂")
ax.set_xlabel("π")
ax.set_ylabel("ℓ(π)")
ax.legend()
plt.show()''',
    after=[("solution", M13A_31_CHECK)],
    record='''wbm.record("M13a.31", True,
           mistakes={"l'objectif n'est pas atteint : la cellule du défi dit pourquoi": False})''',
    note=r"$\ell''(\pi) = -\sum_i \Big(\frac{f_1(x_i) - f_0(x_i)}{\pi f_1(x_i) + (1 - \pi) f_0(x_i)}\Big)^2 \le 0$ : "
         r"$\ell$ est concave, $\ell'$ décroît, et l'unique zéro de $\ell'$ est le maximum. Ici $\ell'(0) > 0 > \ell'(1)$ "
         r"et la dichotomie garde un changement de signe dans un intervalle qu'elle coupe en deux à chaque appel : "
         r"$\lceil \log_2 10^{6} \rceil = 20$ appels suffisent pour $10^{-6}$ (40 pour $10^{-12}$), plus les deux des "
         r"bords. Newton converge encore plus vite (quelques itérations, l'erreur étant élevée au carré à chaque pas), "
         r"mais demande une garde : un pas qui sort de $[0, 1]$ se replie sur la dichotomie. On trouve $\hat{\pi} "
         r"\approx 0{,}335527$ pour `X_31` (et $\approx 0{,}602316$ pour le second échantillon) : proche de la proportion "
         r"des points venus de $f_1$, sans lui être égal, puisque les deux densités se chevauchent et qu'un point ne dit "
         r"pas d'où il vient. L'algorithme EM (M25b) cherche le même maximum quand $f_0$ et $f_1$ sont aussi inconnues.",
)

PART_A = Part("A", "Ta librairie : log-vraisemblance, maximum de vraisemblance et log-loss ; SciPy et scikit-learn",
              "Fiche §1 à §3. Les cinq fonctions de `mymath/likelihood.py`, puis les mêmes calculs avec `scipy.stats`, "
              "`scipy.special` et `sklearn.metrics`.",
              given=TOOLS, exercises=[M13A_22, M13A_23, M13A_24, M13A_25])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §1, §2 et §6. La log-loss des modèles constants, la variabilité de $\\hat{p}$ d'un échantillon à "
              "l'autre, et les deux impuretés sur le triangle des lois à trois issues.",
              exercises=[M13A_26, M13A_27, M13A_28])

PART_C = Part("C", "Erreurs classiques, savoir-faire et défi",
              "Fiche §1 à §3. Quatre erreurs à trouver dans un résumé de modèle, deux maxima de vraisemblance vérifiés "
              "avec SymPy, puis un maximum de vraisemblance sans formule.",
              exercises=[M13A_29, M13A_30, M13A_31])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M13a.1 à M13a.12, M13a.18 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M13a · Vraisemblance et régression logistique — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m13a_vraisemblance_logistique/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M13a`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M13a · Vraisemblance et régression logistique — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : maximum de vraisemblance d'une loi de Bernoulli, "
               "catégorielle (avec lissage) et normale, log-loss et cross-entropy, sigmoïde, logit et cote, softplus, "
               "modèle logistique et sa frontière, hypothèse naïve, a posteriori gaussien, entropie et indice de Gini, "
               "information mutuelle, variance intra et inter, sonde linéaire.\n"
               "- Écrire les cinq fonctions de `mymath/likelihood.py` et les tester, puis comparer avec SciPy et "
               "scikit-learn.\n"
               "- Prédire la log-loss des modèles constants, mesurer la variabilité de $\\hat{p}$, dessiner les "
               "impuretés, chasser des erreurs de calcul en flottants, vérifier un maximum de vraisemblance avec "
               "SymPy, relever un défi de maximum de vraisemblance sans formule.\n\n"
               r"**Rappel express.** $\ell(\boldsymbol{\theta}) = \sum_i \ln p(x_i \mid \boldsymbol{\theta})$ ; "
               r"Bernoulli : $\hat{p}$ = la proportion de 1 ; catégorielle : $\hat{p}_k = \frac{n_k}{N}$, lissée "
               r"$\frac{n_k + \alpha}{N + K\alpha}$ ; normale : $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}"
               r"\sum_i (x_i - \hat{\mu})^2$ ; log-loss $= -\frac{1}{n}\ell = \frac{1}{n}\sum_i \big[s(z_i) - y_iz_i\big]$ ; "
               r"$\sigma(z) = \frac{1}{1 + e^{-z}}$, $s(z) = \ln(1 + e^z) = \max(z, 0) + \ln(1 + e^{-\lvert z \rvert})$, "
               r"$-\ln\sigma(z) = s(-z)$ ; cote $e^{z}$, logit $\ln\frac{p}{1 - p}$ ; frontière $\mathbf{w} \cdot "
               r"\mathbf{x} + b = 0$ ; $H = -\sum_k p_k\log_2 p_k$, $G = 1 - \sum_k p_k^2$, $I(X ; Y) = H(Y) - H(Y \mid X)$ ; "
               r"variance totale = intra + inter.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu écrire une log-vraisemblance et trouver son maximum pour une loi de Bernoulli, catégorielle "
               "et normale (et dire pourquoi la variance divise par $n$) ?\n"
               "2. Sais-tu passer de la log-vraisemblance des labels à la log-loss, et la calculer à partir des scores "
               "sans débordement ?\n"
               "3. Sais-tu lire un modèle logistique : probabilité, cote, logit, frontière ?\n"
               "4. Sais-tu calculer un a posteriori de Naïve Bayes et dire ce que change l'hypothèse naïve ?\n"
               "5. Sais-tu calculer une entropie, un indice de Gini, un gain d'information et une réduction de "
               "variance ?\n\n"
               "**La suite** : M13b, optimisation sous contraintes et SVM, puis le chapitre 13 de workbookIA "
               "(classifieurs).")]


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
