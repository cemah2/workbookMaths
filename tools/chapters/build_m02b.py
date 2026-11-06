#!/usr/bin/env python
"""Build the two notebooks of chapter M02b from a single source (used by Claude).

    python tools/chapters/build_m02b.py
    python tools/run_all_notebooks.py chapitres/m02b_variables_aleatoires/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m02b_variables_aleatoires/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M02b.1 to M02b.10, 🔗 M02b.14); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer nor the calculation that gives it. An irreducible
fraction is answered by text (kind="fraction", simplified=True), an expression in p, x or y by text or SymPy
(kind="expr"), an interval by text (kind="interval"). The values read in the table of Φ (fiche §3) are rounded so that
the table and the exact values give the same answer.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M02b"
FOLDER = "chapitres/m02b_variables_aleatoires"

F = 'kind="fraction", simplified=True'
EP = 'kind="expr", variables=("p",)'
EX = 'kind="expr", variables=("x",)'
EY = 'kind="expr", variables=("y",)'

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M02b.1", "Loi de Bernoulli et loi binomiale", [
        ("a", "a number (4 decimals)", "0.8 ** 5",
         'decimals=4, mistakes={"0,8 est la probabilité de réussir un lancer : cinq réussites, c\'est 0,8 à la '
         'puissance 5": 0.2 ** 5, "les cinq lancers réussissent tous : les probabilités se multiplient, elles ne '
         's\'additionnent pas": 4.0}'),
        ("b", "a number (4 decimals)", "math.comb(5, 3) * 0.8 ** 3 * 0.2 ** 2",
         'decimals=4, mistakes={"n\'oublie pas C(5, 3) : le nombre de façons de placer les 3 réussites parmi les 5 '
         'lancers": 0.8 ** 3 * 0.2 ** 2, "p^k (1 − p)^(n − k) : la probabilité de réussite porte l\'exposant k, le '
         'nombre de réussites": math.comb(5, 3) * 0.8 ** 2 * 0.2 ** 3}'),
        ("c", "a number (4 decimals)", "math.comb(5, 4) * 0.8 ** 4 * 0.2 + 0.8 ** 5",
         'decimals=4, mistakes={"X ≥ 4 : X = 4 ou X = 5, additionne les deux probabilités": '
         '{math.comb(5, 4) * 0.8 ** 4 * 0.2, 0.8 ** 5}, "c\'est P(X ≤ 3) ; X ≥ 4 est l\'événement contraire": '
         '1 - math.comb(5, 4) * 0.8 ** 4 * 0.2 - 0.8 ** 5}'),
        ("d", "an integer", "4",
         'mistakes={"compare P(X = 4) et P(X = 5) : la valeur la plus probable n\'est pas forcément n": 5}'),
        ("e", "a number (1 decimal)", "5 * 0.8",
         'decimals=1, mistakes={"E[X] = n p pour la loi binomiale B(n, p) : n essais, chacun réussi en moyenne p '
         'fois": 0.8, "c\'est l\'espérance du nombre d\'échecs ; E[X] = n p, avec p la probabilité de réussite": 1.0}'),
        ("f", "a number (2 decimals)", "5 * 0.8 * 0.2",
         'decimals=2, mistakes={"c\'est l\'espérance ; la variance de B(n, p) vaut n p (1 − p)": 4.0, '
         '"c\'est la variance d\'un seul lancer ; pour 5 lancers indépendants, les variances s\'additionnent": 0.16, '
         '"c\'est l\'écart-type ; la variance est son carré": 0.894}'),
        ("g", "a number (4 decimals)", "1 - 0.8 ** 5",
         'decimals=4, mistakes={"c\'est P(aucun échec) ; « au moins un échec » est l\'événement contraire": 0.8 ** 5, '
         '"« au moins un échec » est le contraire de « cinq réussites », pas de « cinq échecs »": 1 - 0.2 ** 5}'),
        ("h", "an integer", "11",
         'mistakes={"1 − 0,8ⁿ ≥ 0,9 équivaut à 0,8ⁿ ≤ 0,1 : avec ce n, 0,8ⁿ dépasse encore 0,1": 10, '
         '"le plus petit n qui convient : vérifie aussi l\'entier juste en dessous": 12}'),
    ]),

    Paper("M02b.2", "Loi géométrique : probabilités, et l'espérance par une série", [
        ("a", "a number (3 decimals)", "0.6 ** 2 * 0.4",
         'decimals=3, mistakes={"X = 3 : deux échecs (probabilité 0,6 chacun), puis une réussite (0,4)": '
         '{0.4 ** 2 * 0.6, 0.4 ** 3}}'),
        ("b", "a number (3 decimals)", "0.6 ** 3",
         'decimals=3, mistakes={"X > 3 : les trois premières tentatives échouent, chacune avec la probabilité 0,6, et '
         'rien n\'est imposé à la quatrième": {0.4 ** 3, 0.6 ** 4}, "c\'est P(X ≤ 3) ; P(X > 3) est l\'événement '
         'contraire": 1 - 0.6 ** 3}'),
        ("c", "a number (2 decimals)", "1 - 0.6 ** 2",
         'decimals=2, mistakes={"X ≤ 2 : réussite à la première tentative ou à la deuxième, additionne les deux cas": '
         '{0.4, 0.24}}'),
        ("d", "a number (2 decimals)", "1 / (1 - 0.6) ** 2",
         'decimals=2, mistakes={"S − qS est la série géométrique Σ q^(k−1), de somme 1/(1 − q) ; S s\'obtient en '
         'divisant encore par 1 − q": 1 / (1 - 0.6), "S = 1/(1 − q)², sans facteur q au numérateur": '
         '0.6 / (1 - 0.6) ** 2}'),
        ("e", "a number (1 decimal)", "0.4 / (1 - 0.6) ** 2",
         'decimals=1, mistakes={"E[X] = Σ k p q^(k−1) = p × S : n\'oublie pas le facteur p": 1 / (1 - 0.6) ** 2, '
         '"c\'est q/p, le nombre moyen d\'échecs ; X compte aussi la tentative réussie": 0.6 / 0.4, '
         '"E[X] = p × S, avec la somme S de d)": 1 / 0.6}'),
        ("f", "a number (1 decimal)", "0.6 / 0.4",
         'decimals=1, mistakes={"les tentatives échouées sont X − 1 : toutes sauf la dernière": 0.4 / (1 - 0.6) ** 2}'),
        ("g", "an integer", "2",
         'mistakes={"P(X ≤ 1) = 0,4 n\'atteint pas 0,5 : la médiane est plus loin": 1, '
         '"le plus petit k : P(X ≤ 2) atteint déjà 0,5": 3}'),
        ("h", "an expression in p, as text", '"1/p"',
         EP + ', mistakes={"c\'est le nombre moyen d\'échecs ; X compte aussi la tentative réussie": "(1 - p)/p", '
         '"1 − q = p : p × 1/(1 − q)² se simplifie en divisant par p": "1/(1 - p)", '
         '"n\'oublie pas le facteur p devant la somme S": "1/p**2"}'),
    ]),

    Paper("M02b.3", "Loi de Poisson : probabilités, espérance, et la somme de deux variables de Poisson "
                    "indépendantes", [
        ("a", "a number (4 decimals)", "math.exp(-1.5)",
         'decimals=4, mistakes={"c\'est P(X ≥ 1) ; P(X = 0) = e^(−λ) λ⁰/0! = e^(−λ)": 1 - math.exp(-1.5)}'),
        ("b", "a number (4 decimals)", "math.exp(-1.5) * 1.5 ** 2 / 2",
         'decimals=4, mistakes={"λᵏ/k! avec k = 2 : n\'oublie pas de diviser par 2! = 2": math.exp(-1.5) * 1.5 ** 2, '
         '"λᵏ/k! avec k = 2 : λ au carré, divisé par 2": math.exp(-1.5) * 1.5}'),
        ("c", "a number (4 decimals)", "1 - math.exp(-1.5) * (1 + 1.5)",
         'decimals=4, mistakes={"X ≥ 2 exclut X = 0 et X = 1 : retire les deux probabilités": 1 - math.exp(-1.5), '
         '"c\'est P(X ≤ 1) ; X ≥ 2 est l\'événement contraire": math.exp(-1.5) * 2.5}'),
        ("d", "a number (1 decimal)", "5 * 1.5",
         'decimals=1, mistakes={"sur 5 jours, la linéarité de l\'espérance additionne l\'espérance de chaque jour": '
         '1.5}'),
        ("e", "a number (4 decimals)", "math.exp(-1.5) * math.exp(-2.5)",
         'decimals=4, mistakes={"S = 0 demande X = 0 et Y = 0 : pour des variables indépendantes, les probabilités se '
         'multiplient": math.exp(-1.5) + math.exp(-2.5)}'),
        ("f", "a number (4 decimals)", "math.exp(-4) * (2.5 + 1.5)",
         'decimals=4, mistakes={"S = 1 : (X, Y) vaut (0, 1) ou (1, 0) ; additionne les deux cas": '
         '{math.exp(-4) * 2.5, math.exp(-4) * 1.5}, "(X, Y) = (1, 1) donne S = 2, pas S = 1": math.exp(-4) * 3.75}'),
        ("g", "a number (4 decimals)", "math.exp(-4) * (2.5 ** 2 / 2 + 1.5 * 2.5 + 1.5 ** 2 / 2)",
         'decimals=4, mistakes={"S = 2 : trois couples, (0, 2), (1, 1) et (2, 0) ; n\'oublie pas (1, 1)": '
         'math.exp(-4) * (2.5 ** 2 / 2 + 1.5 ** 2 / 2)}'),
        ("h", "a number (1 decimal)", "4.0",
         'decimals=1, mistakes={"e^(−1,5) e^(−2,5) = e^(−λ) : λ est la somme des deux paramètres": 3.75}'),
    ]),

    Paper("M02b.4", "Lois uniforme et exponentielle : probabilités et espérance", [
        ("a", "an irreducible fraction, as text", "Fraction(1, 15)",
         F + ', mistakes={"la densité vaut 1/(b − a) sur [a ; b] : l\'inverse de la longueur de l\'intervalle": '
         '"15", "b − a est la longueur de l\'intervalle : 25 − 10": "1/25"}'),
        ("b", "an irreducible fraction, as text", "Fraction(1, 3)",
         F + ', mistakes={"P(D ≤ 15) = (15 − 10)/(25 − 10) : D commence à 10, pas à 0": "3/5"}'),
        ("c", "an irreducible fraction, as text", "Fraction(8, 15)",
         F + ', mistakes={"la longueur de [12 ; 20] divisée par celle de [10 ; 25]": "8/25"}'),
        ("d", "a number (1 decimal)", "17.5",
         'decimals=1, mistakes={"l\'espérance d\'une loi uniforme est le milieu de l\'intervalle, (a + b)/2": '
         '{7.5, 12.5}}'),
        ("e", "a number (3 decimals)", "15 / math.sqrt(12)",
         'decimals=3, mistakes={"c\'est la variance (b − a)²/12 ; l\'écart-type est sa racine": 15 ** 2 / 12, '
         '"σ = (b − a)/√12, avec b − a = 15, la longueur de l\'intervalle": 25 / math.sqrt(12), '
         '"(b − a)²/12, puis la racine : (b − a)/√12, pas (b − a)/12": 15 / 12}'),
        ("f", "a number (4 decimals)", "math.exp(-2)",
         'decimals=4, mistakes={"c\'est P(T ≤ 5) ; P(T > t) = e^(−λt)": 1 - math.exp(-2)}'),
        ("g", "a number (1 decimal)", "1 / 0.4",
         'decimals=1, mistakes={"E[T] = 1/λ, l\'inverse du paramètre": 0.4}'),
        ("h", "a number (4 decimals)", "math.exp(-1)",
         'decimals=4, mistakes={"P(T > t) = e^(−λt) avec t = E[T] = 1/λ ; la loi exponentielle n\'est pas '
         'symétrique": 0.5, "c\'est P(T ≤ E[T]) ; P(T > t) = e^(−λt)": 1 - math.exp(-1)}'),
    ]),

    Paper("M02b.5", "Loi normale : standardiser et lire la fonction Φ", [
        ("a", "a number (1 decimal)", "(36 - 30) / 4",
         'decimals=1, mistakes={"z = (x − μ)/σ : divise par l\'écart-type, pas par la variance (N(30, 4²) a pour '
         'variance 16)": 6 / 16}'),
        ("b", "a number (4 decimals)", "0.9332",
         'decimals=4, mistakes={"P(X ≤ 36) = Φ(z), l\'aire à gauche de z": 1 - 0.9332}'),
        ("c", "a number (4 decimals)", "1 - 0.8413",
         'decimals=4, mistakes={"z = −1 : Φ(−1) = 1 − Φ(1), l\'aire à gauche d\'un z négatif est petite": 0.8413, '
         '"Φ(−z) = 1 − Φ(z), pas −Φ(z) : une probabilité n\'est jamais négative": -0.8413}'),
        ("d", "a number (4 decimals)", "0.9332 - (1 - 0.8413)",
         'decimals=4, mistakes={"P(26 ≤ X ≤ 36) = Φ(1,5) − Φ(−1), avec Φ(−1) = 1 − Φ(1)": 0.9332 - 0.8413}'),
        ("e", "a number (4 decimals)", "1 - 0.9772",
         'decimals=4, mistakes={"c\'est P(X ≤ 38) ; P(X > 38) = 1 − Φ(z)": 0.9772}'),
        ("f", "a number (2 decimals)", "30 + 4 * 2.33",
         'decimals=2, mistakes={"t = μ + z σ, avec l\'écart-type σ = 4": 30 + 16 * 2.33, '
         '"c\'est z, lu dans la table ; ramène-le à une durée : t = μ + z σ": 2.33}'),
        ("g", "a number (3 decimals)", "2 * 0.8944 - 1",
         'decimals=3, mistakes={"|X − 30| ≤ 5 va de 25 à 35, des deux côtés de μ : Φ(1,25) − Φ(−1,25) = '
         '2Φ(1,25) − 1": 0.8944}'),
        ("h", "a number (4 decimals)", "1 - 0.9332",
         'decimals=4, mistakes={"N(31, 2²) a pour écart-type 2 : z = (34 − 31)/2": 1 - 0.7734, '
         '"c\'est P(Y ≤ 34) ; P(Y > 34) = 1 − Φ(z)": 0.9332}'),
    ]),

    Paper("M02b.6", "Espérance et variance d'une variable continue (théorème de transfert)", [
        ("a", "an irreducible fraction, as text", "Fraction(3, 4)",
         F + ', mistakes={"c\'est la densité en 1/2 ; la probabilité est l\'aire sous la densité de 0 à 1/2": "1", '
         '"c\'est P(X > 1/2) ; P(X ≤ 1/2) est l\'aire de 0 à 1/2": "1/4"}'),
        ("b", "an irreducible fraction, as text", "Fraction(1, 3)",
         F + ', mistakes={"X n\'est pas uniforme : la densité, plus haute près de 0, tire l\'espérance vers 0 ; '
         'calcule ∫ x f(x) dx": "1/2", "E[X] = ∫ x f(x) dx, pas ∫ f(x) dx": "1"}'),
        ("c", "an irreducible fraction, as text", "Fraction(1, 6)",
         F + ', mistakes={"E[X²] = ∫ x² f(x) dx, la moyenne des carrés, pas le carré de la moyenne": "1/9"}'),
        ("d", "an irreducible fraction, as text", "Fraction(1, 18)",
         F + ', mistakes={"V(X) = E[X²] − E[X]² : retire le carré de l\'espérance": "1/6"}'),
        ("e", "an irreducible fraction, as text", "Fraction(11, 3)",
         F + ', mistakes={"E[5X + 2] = 5 E[X] + 2 : n\'oublie pas le + 2": "5/3"}'),
        ("f", "an irreducible fraction, as text", "Fraction(25, 18)",
         F + ', mistakes={"V(aX + b) = a² V(X) : le facteur compte au carré": "5/18", '
         '"la constante b ne change pas la dispersion : V(aX + b) = a² V(X)": "61/18"}'),
        ("g", "a number (4 decimals)", "2 * math.e - 4",
         'decimals=4, mistakes={"par parties, une primitive de (1 − x)eˣ est (2 − x)eˣ ; n\'oublie pas le facteur 2 '
         'de la densité": math.e - 2, "c\'est e^(E[X]) ; le théorème de transfert calcule ∫ eˣ f(x) dx": '
         'math.exp(1 / 3)}'),
        ("h", "True or False", "True",
         'mistakes={"compare g) à e^(1/3), calculé avec la valeur de b)": False}'),
    ]),

    Paper("M02b.7", "Un couple de variables discrètes : loi jointe, marginales, indépendance", [
        ("a", "a number (2 decimals)", "0.8",
         'decimals=2, mistakes={"P(Y ≥ 1) = 1 − P(Y = 0), et P(Y = 0) somme la colonne Y = 0 sur les deux valeurs '
         'de X": {0.85, 0.95}}'),
        ("b", "a list (2 decimals)", "[0.2, 0.4, 0.4]",
         'decimals=2, mistakes={"c\'est une ligne du tableau ; la marginale de Y somme chaque colonne sur les deux '
         'valeurs de X": [0.15, 0.25, 0.1], "c\'est l\'autre ligne du tableau ; additionne les deux lignes, '
         'colonne par colonne": [0.05, 0.15, 0.3]}'),
        ("c", "a number (2 decimals)", "0 * 0.2 + 1 * 0.4 + 2 * 0.4",
         'decimals=2, mistakes={"E[Y] = Σ y P(Y = y), pondérée par la loi marginale de b), pas la moyenne simple des '
         'valeurs": 1.0}'),
        ("d", "a number (2 decimals)", "1 * (1 * 0.25 + 2 * 0.10) + 2 * (1 * 0.15 + 2 * 0.30)",
         'decimals=2, mistakes={"c\'est E[X] E[Y] ; E[XY] somme xy P(X = x, Y = y) sur les six cases du tableau": '
         '1.8}'),
        ("e", "a number (2 decimals)", "(1 * 0.5 + 2 * 0.5) * 1.2",
         'decimals=2, mistakes={"c\'est E[XY] ; ici, le produit des deux espérances": 1.95}'),
        ("f", "True or False", "False",
         'mistakes={"compare P(X = 1, Y = 0) au produit P(X = 1) P(Y = 0) : une seule case suffit à conclure": '
         'True}'),
        ("g", "a number (2 decimals)", "0.7 * 0.3",
         'decimals=2, mistakes={"X′ et Y′ sont indépendantes : P(X′ = 2, Y′ = 1) = P(X′ = 2) × P(Y′ = 1)": '
         '{0.09, 0.14, 1.0}}'),
        ("h", "True or False", "True",
         'mistakes={"complète la dernière case (la somme vaut 1), puis compare chaque case au produit des '
         'marginales": False}'),
    ]),

    Paper("M02b.8", "Linéarité et variance d'une somme : sommes et moyennes de variables", [
        ("a", "an integer", "4 + 6 + 10", ''),
        ("b", "an integer", "1 ** 2 + 2 ** 2 + 2 ** 2",
         'mistakes={"additionne les variances σ², pas les écarts-types": 5, '
         '"la somme des variances, pas le carré de la somme des écarts-types": 25}'),
        ("c", "an integer", "3",
         'mistakes={"σ(S) = √V(S) : additionne d\'abord les variances, puis prends la racine": 5, '
         '"c\'est la variance ; l\'écart-type est sa racine": 9}'),
        ("d", "an integer", "10 - 6", 'mistakes={"T₃ − T₂ : l\'espérance de T₂ se retranche": 16}'),
        ("e", "a number (3 decimals)", "math.sqrt(2 ** 2 + 2 ** 2)",
         'decimals=3, mistakes={"V(T₃ − T₂) = V(T₃) + V(T₂) : les variances s\'additionnent aussi pour une '
         'différence": 0.0, "σ = √(V(T₃) + V(T₂)), pas σ(T₃) + σ(T₂)": 4.0, "c\'est la variance ; l\'écart-type est '
         'sa racine": 8.0}'),
        ("f", "a number (3 decimals)", "math.sqrt(50)",
         'decimals=3, mistakes={"50 durées indépendantes : la variance est multipliée par 50, donc l\'écart-type par '
         '√50": 50.0}'),
        ("g", "a number (4 decimals)", "1 / math.sqrt(50)",
         'decimals=4, mistakes={"σ(moyenne) = σ/√n, pas σ/n": 0.02, "la moyenne divise la somme par 50 : son '
         'écart-type est celui de f) divisé par 50": math.sqrt(50)}'),
        ("h", "an integer", "4",
         'mistakes={"T₁ + T₁ = 2T₁ : V(2T₁) = 4 V(T₁) ; une variable n\'est pas indépendante d\'elle-même": 2}'),
    ]),

    Paper("M02b.9", "Une intégrale double sur un rectangle, et une densité jointe", [
        ("a", "an irreducible fraction, as text", "Fraction(9, 2)",
         F + ', mistakes={"le produit des deux intégrales simples : ∫ de 0 à 1 de x dx, fois ∫ de 0 à 3 de y² dy": '
         '"9", "une primitive de y² est y³/3 : ∫ de 0 à 3 de y² dy vaut 3³/3": "27/2"}'),
        ("b", "a number (4 decimals)", "(math.e - 1) ** 2",
         'decimals=4, mistakes={"e^(x + y) = eˣ eʸ : le produit de deux intégrales simples, chacune égale à e − 1": '
         'math.e - 1}'),
        ("c", "an irreducible fraction, as text", "Fraction(7, 12)",
         F + ', mistakes={"après l\'intégrale en x, qui vaut 1/3 + y/2, il reste à intégrer en y de 0 à 1": "5/6"}'),
        ("d", "an irreducible fraction, as text", "Fraction(2, 9)",
         F + ', mistakes={"c × (l\'intégrale de a)) = 1 : c est l\'inverse de cette intégrale": "9/2"}'),
        ("e", "an expression in x, as text", '"2*x"',
         EX + ', mistakes={"f_X(x) = ∫ de 0 à 3 de c x y² dy, avec la constante c de d)": "x", '
         '"intègre la variable y seulement : x reste dans le résultat": "2"}'),
        ("f", "an expression in y, as text", '"y**2/9"',
         EY + ', mistakes={"f_Y(y) = ∫ de 0 à 1 de c x y² dx, et ∫ de 0 à 1 de x dx = 1/2": "2*y**2/9", '
         '"intègre la variable x seulement : y reste dans le résultat": "1/3"}'),
        ("g", "True or False", "True",
         'mistakes={"compare f(x, y) au produit f_X(x) f_Y(y) de e) et f)": False}'),
        ("h", "an irreducible fraction, as text", "Fraction(1, 108)",
         F + ', mistakes={"une probabilité de densité produit : ∫ de 0 à 1/2 de f_X, fois ∫ de 0 à 1 de f_Y": "1/27", '
         '"il manque le second facteur, ∫ de 0 à 1 de f_Y(y) dy": "1/4"}'),
    ]),

    Paper("M02b.10", "Changement de variable : la loi de aX + b, et celle de X²", [
        ("a", "an interval, as text", '"[-1 ; 5]"',
         'kind="interval", mistakes={"c\'est l\'intervalle des valeurs de X ; Y = 3X − 1 va de 3 × 0 − 1 à '
         '3 × 2 − 1": "[0 ; 2]"}'),
        ("b", "an irreducible fraction, as text", "Fraction(1, 6)",
         F + ', mistakes={"f_Y(y) = f_X((y + 1)/3) / 3 : la densité de X divisée par 3": "1/2", '
         '"divise par 3, ne multiplie pas : l\'aire doit rester 1": "3/2"}'),
        ("c", "an irreducible fraction, as text", "Fraction(1, 2)",
         F + ', mistakes={"Y commence à −1 : P(Y ≤ 2) = (2 − (−1)) × la densité de b)": "1/3"}'),
        ("d", "a number (4 decimals)", "1 / (6 * math.sqrt(2 * math.pi))",
         'decimals=4, mistakes={"Y = 2X + 5 a pour écart-type 2 × 3 : sa densité est deux fois plus basse que celle '
         'de X": 1 / (3 * math.sqrt(2 * math.pi)), "l\'écart-type de Y vaut 2 × 3, pas 2 × 3²": '
         '1 / (18 * math.sqrt(2 * math.pi))}'),
        ("e", "an irreducible fraction, as text", "Fraction(2, 3)",
         F + ', mistakes={"X² ≤ 4 équivaut à X ≤ 2 (X est positif), puis P(X ≤ 2) pour X uniforme sur [0 ; 3]": '
         '"4/9"}'),
        ("f", "an expression in y, as text", '"sqrt(y)/3"',
         EY + ', mistakes={"F_Y(y) = P(X ≤ √y) : remplace t par √y dans P(X ≤ t) = t/3": "y/9", '
         '"c\'est une densité ; la fonction de répartition est F_Y(y) = P(Y ≤ y)": "1/(6*sqrt(y))"}'),
        ("g", "an expression in y, as text", '"1/(6*sqrt(y))"',
         EY + ', mistakes={"dérive √y/3 : la dérivée de √y vaut 1/(2√y)": "1/(3*sqrt(y))", '
         '"c\'est F_Y ; la densité est sa dérivée": "sqrt(y)/3"}'),
        ("h", "an integer", "3",
         'mistakes={"E[X²] = ∫ de 0 à 3 de x² × (1/3) dx : n\'oublie pas la densité 1/3": 9, '
         '"c\'est E[X]² ; E[X²] est la moyenne des carrés": 2}'),
    ]),

    Paper("M02b.14", "Combien d'erreurs d'annotation dans un dataset ? Binomiale et Poisson", [
        ("a", "an integer", "4", 'mistakes={"E[X] = n p : 2 000 × 0,002": 8}'),
        ("b", "a number (3 decimals)", "math.sqrt(2000 * 0.002 * 0.998)",
         'decimals=3, mistakes={"c\'est la variance ; l\'écart-type est sa racine": 2000 * 0.002 * 0.998, '
         '"c\'est l\'écart-type de la loi de Poisson ; avec la binomiale, σ = √(n p (1 − p))": 2.0}'),
        ("c", "a number (4 decimals)", "0.998 ** 2000",
         'decimals=4, mistakes={"c\'est l\'approximation de Poisson ; la binomiale donne (1 − p)ⁿ": math.exp(-4)}'),
        ("d", "a number (4 decimals)", "math.exp(-4)",
         'decimals=4, mistakes={"c\'est la valeur exacte de la binomiale ; l\'approximation de Poisson donne e^(−λ), '
         'avec λ = n p": 0.998 ** 2000}'),
        ("e", "a number (4 decimals)", "13 * math.exp(-4)",
         'decimals=4, mistakes={"P(X ≤ 2) additionne k = 0, 1 et 2 : n\'oublie pas k = 0": 12 * math.exp(-4), '
         '"λᵏ/k! avec k = 2 : 4²/2, pas 4²": 21 * math.exp(-4), '
         '"c\'est P(X = 2) seule ; X ≤ 2 additionne k = 0, 1 et 2": 8 * math.exp(-4)}'),
        ("f", "a number (4 decimals)", "1 - math.exp(-1)",
         'decimals=4, mistakes={"c\'est P(Y = 0) ; P(Y ≥ 1) est l\'événement contraire": math.exp(-1), '
         '"Y porte sur 500 images : son paramètre est 500 × 0,002, pas celui de X": 1 - math.exp(-4)}'),
        ("g", "an integer", "1152",
         'mistakes={"c\'est le résultat exact avec la binomiale, 0,998ⁿ ≤ 0,1 ; la question demande l\'approximation '
         'e^(−0,002 n) ≤ 0,1": 1151}'),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements (Φ: the values of the table, fiche §3)
import math
from fractions import Fraction'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M02b.1 à M02b.10, 🔗 M02b.14)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `-1.25`, arrondi comme le demande la question ;\n"
               "- une fraction irréductible entre guillemets, `\"5/9\"` ;\n"
               "- une expression entre guillemets, dans la variable indiquée ($p$, $x$ ou $y$), avec `**` pour les "
               "puissances, `sqrt` et des parenthèses autour d'un dénominateur, `\"3/(2*p)\"`, `\"sqrt(y)/5\"` ;\n"
               "- une liste `[0.25, 0.75]`, un intervalle `\"[-2 ; 7]\"`, ou `True` / `False`.\n\n"
               "Pour la loi normale, utilise la table de $\\Phi$ de la fiche (§3) : les réponses attendues sont "
               "arrondies de sorte que la table et un calcul exact donnent la même valeur. Les réponses pas encore "
               "remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M02b.18 to M02b.21)
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

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M02b")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M02a). Ouvre ta copie `mon_travail/mymath/distributions.py`, lis la "
         "docstring de la fonction en entier, remplace la ligne `raise NotImplementedError(...)` par ton code, "
         "**enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "`math.comb`, `math.factorial`, `math.exp`, `math.erf` et NumPy sont permis (importe-les en haut du fichier). "
         "Mais pas `scipy.stats` : les tests comparent tes résultats à lui, et un test vérifie que tu ne t'en sers "
         "pas. Chaque probabilité ou densité est un `float` de Python (`float(...)` convertit un nombre de NumPy).")

WRONG_ERROR = "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)"
OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ZeroDivisionError"]


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of distributions.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m02b_distributions.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m02b_distributions.py", "{keyword}", impl="ref")')]


PY_FLOAT = ('mistakes={{"la docstring demande un float de Python : float(...) convertit un nombre de NumPy": '
            '{{"float64", "int"}}}}')

M02B_18 = Ex(
    "M02b.18", "🔨", 1, 20, "Lois binomiale et de Poisson · `binomial_pmf`, `poisson_pmf`",
    "programmer les probabilités des lois binomiale et de Poisson, avec leurs cas limites et leurs cas d'erreur.",
    "fiche §2 ; R8 (coefficients binomiaux)", tracks="C, E", mymath="distributions.py",
    body=HOWTO + """

Écris `binomial_pmf(k, n, p)` puis `poisson_pmf(k, lam)` (fiche §2). Une valeur de $k$ impossible (négative, ou plus grande que $n$ pour la binomiale) a la probabilité `0.0` : ce n'est pas une erreur. Des paramètres impossibles ($n < 0$, $p$ hors de $[0 ; 1]$, $\\lambda < 0$) lèvent une `ValueError`.

La vérification calcule :
- a) `binomial_pmf(3, 10, 0.3)` (6 décimales) ;
- b) la somme des `binomial_pmf(k, 12, 0.35)` pour $k$ de 0 à 12 (6 décimales) ;
- c) `binomial_pmf(11, 10, 0.3)` ;
- d) le nom de l'erreur levée par `binomial_pmf(2, 5, 1.5)` (avec `raised`, de la cellule des outils) ;
- e) `poisson_pmf(4, 2.5)` (6 décimales) ;
- f) `poisson_pmf(0, 0)` ;
- g) le type de `poisson_pmf(1, 3)`, en texte (`"float"` pour un flottant) ;
- h) la somme des `k * poisson_pmf(k, 6.5)` pour $k$ de 0 à 100 (4 décimales).

Puis, dans ta copie : quelle propriété de la loi binomiale b) vérifie-t-il ? Pourquoi h) redonne-t-il le paramètre, et pourquoi s'arrêter à $k = 100$ suffit-il ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M02b.18a"):
    wbm.check("M02b.18a", mymath.distributions.binomial_pmf(3, 10, 0.3), computed=True)
with checked("M02b.18b"):
    wbm.check("M02b.18b", sum(mymath.distributions.binomial_pmf(k, 12, 0.35) for k in range(13)), computed=True)
with checked("M02b.18c"):
    wbm.check("M02b.18c", mymath.distributions.binomial_pmf(11, 10, 0.3), computed=True)
with checked("M02b.18d"):
    wbm.check("M02b.18d", raised(mymath.distributions.binomial_pmf, 2, 5, 1.5), computed=True)
with checked("M02b.18e"):
    wbm.check("M02b.18e", mymath.distributions.poisson_pmf(4, 2.5), computed=True)
with checked("M02b.18f"):
    wbm.check("M02b.18f", mymath.distributions.poisson_pmf(0, 0), computed=True)
with checked("M02b.18g"):
    wbm.check("M02b.18g", type(mymath.distributions.poisson_pmf(1, 3)).__name__, computed=True)
with checked("M02b.18h"):
    wbm.check("M02b.18h", sum(k * mymath.distributions.poisson_pmf(k, 6.5) for k in range(101)), computed=True)''',
    solution=LOAD_REF + '''
binomial_pmf, poisson_pmf = mymath.distributions.binomial_pmf, mymath.distributions.poisson_pmf
print("a)", binomial_pmf(3, 10, 0.3), " b)", sum(binomial_pmf(k, 12, 0.35) for k in range(13)),
      " c)", binomial_pmf(11, 10, 0.3), " d)", raised(binomial_pmf, 2, 5, 1.5))
print("e)", poisson_pmf(4, 2.5), " f)", poisson_pmf(0, 0), " g)", type(poisson_pmf(1, 3)).__name__,
      " h)", sum(k * poisson_pmf(k, 6.5) for k in range(101)))''',
    record=f'''wbm.record("M02b.18a", 0.266827932, decimals=6,
           mistakes={{"C(n, k) p^k (1 − p)^(n − k) : la probabilité p porte l'exposant k, le nombre de succès":
                         0.009001692, "n'oublie pas le coefficient C(n, k), le nombre de suites à k succès": 0.002223566}})
wbm.record("M02b.18b", 1.0, decimals=6)
wbm.record("M02b.18c", 0.0, decimals=6)
wbm.record("M02b.18d", "ValueError",
           mistakes={{"p hors de [0 ; 1] n'est pas une probabilité : lève une ValueError": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M02b.18e", 0.133601886, decimals=6,
           mistakes={{"e^(−λ) λᵏ / k! : n'oublie pas de diviser par k!": 3.206445259}})
wbm.record("M02b.18f", 1.0, decimals=6,
           mistakes={{"λ = 0 : aucun événement, X = 0 est sûr ; en Python, 0 ** 0 vaut 1": 0.0}})
wbm.record("M02b.18g", "float", {PY_FLOAT.format()})
wbm.record("M02b.18h", 6.5, decimals=4,
           mistakes={{"la somme de k P(X = k), pas de P(X = k)": 1.0}})''',
    after=tests_cells("test_binomial_pmf_ or test_poisson_pmf_ or test_distributions_uses"),
    note="b) vaut 1 : les probabilités d'une loi ont une somme de 1 (la formule du binôme). h) est l'espérance "
         "$\\sum_k k\\,P(X = k) = \\lambda$ (fiche §4) ; les termes au-delà de $k = 100$ sont inférieurs à $10^{-70}$ "
         "pour $\\lambda = 6{,}5$ : la queue d'une loi de Poisson décroît plus vite que toute suite géométrique.",
)

M02B_19 = Ex(
    "M02b.19", "🔨", 1, 20, "Densité et fonction de répartition de la loi normale (avec `math.erf`) · "
    "`normal_pdf`, `normal_cdf`",
    "programmer la densité et la fonction de répartition de la loi normale, et vérifier que l'une est la dérivée "
    "de l'autre.", "fiche §3 ; M02a.19 (erf)", tracks="C, E", mymath="distributions.py",
    body="""Écris `normal_pdf(x, mu=0.0, sigma=1.0)` et `normal_cdf(x, mu=0.0, sigma=1.0)` (fiche §3). `sigma` est l'**écart-type**. Pour $\\Phi$, la fonction d'erreur `math.erf` fait le travail : $\\Phi(z) = \\frac{1}{2}\\left(1 + \\operatorname{erf}\\frac{z}{\\sqrt{2}}\\right)$, après avoir standardisé. Les deux fonctions lèvent une `ValueError` si $\\sigma \\le 0$.

La vérification calcule :
- a) `normal_pdf(1)` (6 décimales) ;
- b) `normal_pdf(3, 3, 0.2)` (4 décimales) ;
- c) `normal_cdf(1.5)` (4 décimales), à comparer avec la table de la fiche ;
- d) `normal_cdf(4, 7, 2)` (4 décimales) ;
- e) `normal_cdf(2.5) - normal_cdf(0.5)` (4 décimales) ;
- f) le nom de l'erreur levée par `normal_pdf(0, 0, 0)` ;
- g) le type de `normal_cdf(0.3)`, en texte ;
- h) le taux d'accroissement `(normal_cdf(0.7 + 1e-5) - normal_cdf(0.7 - 1e-5)) / 2e-5` (5 décimales).

Dans ta copie : b) dépasse 1. Est-ce une erreur ? Compare h) avec `normal_pdf(0.7)` : quel théorème de M02a cela illustre-t-il ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M02b.19a"):
    wbm.check("M02b.19a", mymath.distributions.normal_pdf(1), computed=True)
with checked("M02b.19b"):
    wbm.check("M02b.19b", mymath.distributions.normal_pdf(3, 3, 0.2), computed=True)
with checked("M02b.19c"):
    wbm.check("M02b.19c", mymath.distributions.normal_cdf(1.5), computed=True)
with checked("M02b.19d"):
    wbm.check("M02b.19d", mymath.distributions.normal_cdf(4, 7, 2), computed=True)
with checked("M02b.19e"):
    wbm.check("M02b.19e", mymath.distributions.normal_cdf(2.5) - mymath.distributions.normal_cdf(0.5), computed=True)
with checked("M02b.19f"):
    wbm.check("M02b.19f", raised(mymath.distributions.normal_pdf, 0, 0, 0), computed=True)
with checked("M02b.19g"):
    wbm.check("M02b.19g", type(mymath.distributions.normal_cdf(0.3)).__name__, computed=True)
with checked("M02b.19h"):
    slope = (mymath.distributions.normal_cdf(0.7 + 1e-5) - mymath.distributions.normal_cdf(0.7 - 1e-5)) / 2e-5
    wbm.check("M02b.19h", slope, computed=True)''',
    solution=LOAD_REF + '''
normal_pdf, normal_cdf = mymath.distributions.normal_pdf, mymath.distributions.normal_cdf
print("a)", normal_pdf(1), " b)", normal_pdf(3, 3, 0.2), " c)", normal_cdf(1.5), " d)", normal_cdf(4, 7, 2))
print("e)", normal_cdf(2.5) - normal_cdf(0.5), " f)", raised(normal_pdf, 0, 0, 0), " g)", type(normal_cdf(0.3)).__name__)
print("h)", (normal_cdf(0.7 + 1e-5) - normal_cdf(0.7 - 1e-5)) / 2e-5, " density:", normal_pdf(0.7))''',
    record=f'''wbm.record("M02b.19a", 0.241970725, decimals=6,
           mistakes={{"φ(z) = e^(−z²/2) / √(2π) : le carré est divisé par 2 dans l'exponentielle": 0.146762663,
                     "n'oublie pas le facteur 1/√(2π) devant l'exponentielle": 0.606530660}})
wbm.record("M02b.19b", 1.994711402, decimals=4,
           mistakes={{"sigma est l'écart-type : le facteur vaut 1/(σ√(2π)), avec σ, pas σ²": 9.973557010,
                     "le facteur vaut 1/(σ√(2π)), avec σ lui-même, pas sa racine": 0.892062058}})
wbm.record("M02b.19c", 0.933192799, decimals=4,
           mistakes={{"Φ(z) = (1 + erf(z/√2)) / 2 : divise z par √2 dans erf": 0.983052573}})
wbm.record("M02b.19d", 0.066807201, decimals=4,
           mistakes={{"standardise par l'écart-type : z = (x − mu)/sigma": 0.226627352,
                     "Φ(z) = (1 + erf(z/√2)) / 2 : divise z par √2 dans erf": 0.016947427}})
wbm.record("M02b.19e", 0.302327873, decimals=4)
wbm.record("M02b.19f", "ValueError",
           mistakes={{"sigma = 0 : lève une ValueError avant de diviser par sigma": {{"aucune", "ZeroDivisionError"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("M02b.19g", "float", {PY_FLOAT.format()})
wbm.record("M02b.19h", 0.312253933, decimals=5)''',
    after=tests_cells("test_normal_pdf_ or test_normal_cdf_"),
    note="b) vaut environ 1,99 : une densité n'est pas une probabilité, et une cloche étroite ($\\sigma = 0{,}2$) est "
         "haute. h) approche $\\varphi(0{,}7) \\approx 0{,}312254$ : la fonction de répartition a pour dérivée la "
         "densité (M02a §7), et le taux d'accroissement symétrique est précis à $10^{-11}$ près ici.",
)

M02B_20_FIGURE = '''with checked("M02b.20 figure"):
    draws = mymath.distributions.inverse_transform_sample(lambda u: -math.log(1 - u) / 3, 20_000)
    grid_20 = np.linspace(0, 2, 200)
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.hist(draws, bins=np.linspace(0, 2, 51), density=True, alpha=0.5, label="20 000 tirages par inversion")
    ax.plot(grid_20, 3 * np.exp(-3 * grid_20), color="black", label="densité 3e^(−3t)")
    ax.set(xlabel="t", title="La loi exponentielle de paramètre 3, simulée")
    ax.legend()
    plt.show()'''

M02B_20 = Ex(
    "M02b.20", "🔨", 2, 20, "Simuler par inversion de la fonction de répartition · `inverse_transform_sample`",
    "programmer la simulation par inversion, et s'en servir pour une loi continue et pour une loi discrète.",
    "fiche §8 ; M02a §7 (quantiles)", tracks="C", mymath="distributions.py",
    body="""Écris `inverse_transform_sample(inverse_cdf, n, seed=0)` (fiche §8) : un générateur `np.random.default_rng(seed)`, puis $n$ nombres uniformes **dans l'ordre** (`rng.random(n)`), puis `inverse_cdf` appliquée à **chacun** (elle prend un seul nombre). Le résultat est un array NumPy de flottants, de forme `(n,)` ; $n < 1$ lève une `ValueError`.

La loi géométrique de paramètre $p$ se tire aussi par inversion, avec la fonction $u \\mapsto \\left\\lceil \\frac{\\ln(1 - u)}{\\ln(1 - p)} \\right\\rceil$ (`math.ceil` arrondit à l'entier supérieur).

La vérification calcule :
- a) le premier élément de `inverse_transform_sample(lambda u: 10 * u, 4)` (6 décimales) ;
- b) la moyenne de 100 000 tirages de la loi exponentielle de paramètre 3, obtenus avec $u \\mapsto -\\frac{\\ln(1 - u)}{3}$ (graine 0 ; 4 décimales) ;
- c) le nombre de ces 100 000 tirages qui dépassent 1 (un entier) ;
- d) le nom de l'erreur levée par `inverse_transform_sample(lambda u: u, 0)` ;
- e) la moyenne de 50 000 tirages de la loi géométrique de paramètre 0,2 (graine 0 ; 2 décimales) ;
- f) la proportion de ces 50 000 tirages égaux à 1 (3 décimales) ;
- g) le nom du type des éléments de `inverse_transform_sample(lambda u: int(6 * u) + 1, 3)`, en texte (`.dtype.name`) ;
- h) le premier élément de `inverse_transform_sample(lambda u: 10 * u, 5, seed=3)` (6 décimales).

Dans ta copie : compare b), c) et f) à leurs valeurs théoriques ($\\frac{1}{3}$, $100\\,000\\,e^{-3}$, 0,2). Démontre que, pour $U$ uniforme, $P\\left(\\left\\lceil \\frac{\\ln(1 - U)}{\\ln(1 - p)} \\right\\rceil > k\\right) = (1 - p)^k$ (indication : $\\lceil t \\rceil > k$ équivaut à $t > k$ pour un entier $k$, et $\\ln(1 - p) < 0$).""",
    todo=LOAD_LEARNER,
    check='''with checked("M02b.20a"):
    wbm.check("M02b.20a", mymath.distributions.inverse_transform_sample(lambda u: 10 * u, 4)[0], computed=True)
with checked("M02b.20b"):
    waits = mymath.distributions.inverse_transform_sample(lambda u: -math.log(1 - u) / 3, 100_000)
    wbm.check("M02b.20b", waits.mean(), computed=True)
with checked("M02b.20c"):
    waits = mymath.distributions.inverse_transform_sample(lambda u: -math.log(1 - u) / 3, 100_000)
    wbm.check("M02b.20c", int(np.sum(waits > 1)), computed=True)
with checked("M02b.20d"):
    wbm.check("M02b.20d", raised(mymath.distributions.inverse_transform_sample, lambda u: u, 0), computed=True)
with checked("M02b.20e"):
    ranks = mymath.distributions.inverse_transform_sample(
        lambda u: math.ceil(math.log(1 - u) / math.log(1 - 0.2)), 50_000)
    wbm.check("M02b.20e", ranks.mean(), computed=True)
with checked("M02b.20f"):
    ranks = mymath.distributions.inverse_transform_sample(
        lambda u: math.ceil(math.log(1 - u) / math.log(1 - 0.2)), 50_000)
    wbm.check("M02b.20f", np.mean(ranks == 1), computed=True)
with checked("M02b.20g"):
    wbm.check("M02b.20g", mymath.distributions.inverse_transform_sample(lambda u: int(6 * u) + 1, 3).dtype.name,
              computed=True)
with checked("M02b.20h"):
    wbm.check("M02b.20h", mymath.distributions.inverse_transform_sample(lambda u: 10 * u, 5, seed=3)[0], computed=True)''',
    solution=LOAD_REF + '''
sample = mymath.distributions.inverse_transform_sample
waits = sample(lambda u: -math.log(1 - u) / 3, 100_000)
ranks = sample(lambda u: math.ceil(math.log(1 - u) / math.log(1 - 0.2)), 50_000)
print("a)", sample(lambda u: 10 * u, 4)[0], " b)", waits.mean(), " c)", int(np.sum(waits > 1)),
      "theory:", 100_000 * math.exp(-3))
print("d)", raised(sample, lambda u: u, 0), " e)", ranks.mean(), " f)", np.mean(ranks == 1),
      " g)", sample(lambda u: int(6 * u) + 1, 3).dtype.name, " h)", sample(lambda u: 10 * u, 5, seed=3)[0])''',
    record=f'''wbm.record("M02b.20a", 6.369616873, decimals=6,
           mistakes={{"les uniformes de np.random.default_rng(seed).random(n), dans l'ordre, chacun passé à inverse_cdf":
                         {{2.697867138, 0.409735239, 0.165276355}}}})
wbm.record("M02b.20b", 0.332756630, decimals=4,
           mistakes={{"−ln(1 − u)/λ avec λ = 3 : divise par 3, ne multiplie pas": 2.994809673}})
wbm.record("M02b.20c", 4995)
wbm.record("M02b.20d", "ValueError",
           mistakes={{"n < 1 : aucun tirage, lève une ValueError": "aucune", "{WRONG_ERROR}": {errors_source()}}})
wbm.record("M02b.20e", 5.00136, decimals=2,
           mistakes={{"l'espérance de la loi géométrique vaut 1/p : relis la fonction d'inversion": 4.0}})
wbm.record("M02b.20f", 0.20028, decimals=3)
wbm.record("M02b.20g", "float64",
           mistakes={{"la docstring demande un array de flottants : np.array(values, dtype=float)": {{"int64", "object"}}}})
wbm.record("M02b.20h", 0.856491671, decimals=6,
           mistakes={{"seed=3 : le générateur np.random.default_rng(seed), avec la graine reçue": 6.369616873}})''',
    after=tests_cells("test_inverse_transform_sample_") + [
        ("md", "**La figure** : l'histogramme des tirages par inversion et la densité de la loi exponentielle."),
        ("code", M02B_20_FIGURE)],
    note="b) 0,3328 pour $\\frac{1}{3}$ ; c) 4 995 tirages au-delà de 1 pour $100\\,000\\,e^{-3} \\approx 4\\,979$ ; "
         "f) 0,200 : l'aléa de 100 000 ou 50 000 tirages est de l'ordre de quelques millièmes. Pour la loi "
         "géométrique : $\\ln(1 - p) < 0$, donc $\\frac{\\ln(1 - U)}{\\ln(1 - p)} > k$ équivaut à "
         "$\\ln(1 - U) < k\\ln(1 - p)$, soit $1 - U < (1 - p)^k$, de probabilité $(1 - p)^k$ car $1 - U$ est "
         "uniforme : c'est $P(X > k)$ de la fiche §2.",
)

M02B_21 = Ex(
    "M02b.21", "📦", 1, 15, "`scipy.stats` : pmf, pdf, cdf, ppf et rvs",
    "utiliser les lois de `scipy.stats` et leurs méthodes, en évitant les pièges de leurs paramètres `loc` et "
    "`scale`.", "fiche §2, §3 et §8", tracks="C, E",
    body="""Chaque loi de `scipy.stats` est un objet qu'on « fige » avec ses paramètres, puis qu'on interroge : `law = stats.binom(10, 0.3)`, puis `law.pmf(k)` (loi discrète), `law.pdf(x)` (densité), `law.cdf(x)` (fonction de répartition), `law.ppf(q)` (la fonction quantile, $F^{-1}$), `law.mean()`, `law.var()`, et `law.rvs(size=..., random_state=...)` pour tirer des valeurs. Les lois continues ont deux paramètres communs, `loc` (un décalage) et `scale` (un facteur d'échelle) : lis `help(stats.expon)` et `help(stats.uniform)` avant e) et h).

Calcule :
- a) $P(X = 3)$ pour $X \\sim \\mathcal{B}(20 ; 0{,}15)$ (4 décimales) ;
- b) $P(X \\le 2)$ pour $X \\sim \\mathcal{P}(4{,}5)$ (4 décimales) ;
- c) $P(X \\le 130)$ pour $X \\sim \\mathcal{N}(100, 15^2)$ (4 décimales) ;
- d) le percentile 90 de $\\mathcal{N}(100, 15^2)$ (2 décimales) ;
- e) l'espérance de la loi exponentielle de **paramètre** $\\lambda = 2$, avec `stats.expon` (1 décimale) ;
- f) le nombre $z$ tel que $\\Phi(z) = 0{,}975$ (4 décimales) ;
- g) la moyenne de 10 000 tirages de $\\mathcal{P}(4{,}5)$, avec `random_state=0` (4 décimales) ;
- h) la variance de la loi uniforme sur $[2 ; 8]$, avec `stats.uniform` (1 décimale).

Dans ta copie : quelle formule de la fiche donne e) et h) ? Que vaudrait d) avec la table de $\\Phi$ (indication : $\\Phi(1{,}2816) \\approx 0{,}9$) ?""",
    todo='''answer_M02b_21a = ...  # a) stats.binom(...).pmf(...)
answer_M02b_21b = ...  # b) stats.poisson(...).cdf(...)
answer_M02b_21c = ...  # c) stats.norm(...).cdf(...)
answer_M02b_21d = ...  # d) stats.norm(...).ppf(...)
answer_M02b_21e = ...  # e) stats.expon(...).mean()
answer_M02b_21f = ...  # f) stats.norm().ppf(...)
answer_M02b_21g = ...  # g) the mean of stats.poisson(...).rvs(size=10_000, random_state=0)
answer_M02b_21h = ...  # h) stats.uniform(...).var()''',
    check='''for letter, answer in zip("abcdefgh", [answer_M02b_21a, answer_M02b_21b, answer_M02b_21c, answer_M02b_21d,
                                        answer_M02b_21e, answer_M02b_21f, answer_M02b_21g, answer_M02b_21h]):
    wbm.check(f"M02b.21{letter}", answer)''',
    solution='''answer_M02b_21a = stats.binom(20, 0.15).pmf(3)
answer_M02b_21b = stats.poisson(4.5).cdf(2)
answer_M02b_21c = stats.norm(100, 15).cdf(130)
answer_M02b_21d = stats.norm(100, 15).ppf(0.9)
answer_M02b_21e = stats.expon(scale=1 / 2).mean()          # scale = 1/λ ; stats.expon(2) would shift the law by 2
answer_M02b_21f = stats.norm().ppf(0.975)
answer_M02b_21g = stats.poisson(4.5).rvs(size=10_000, random_state=0).mean()
answer_M02b_21h = stats.uniform(loc=2, scale=6).var()      # [loc ; loc + scale] = [2 ; 8]
print([round(float(v), 4) for v in [answer_M02b_21a, answer_M02b_21b, answer_M02b_21c, answer_M02b_21d,
                                     answer_M02b_21e, answer_M02b_21f, answer_M02b_21g, answer_M02b_21h]])
print("stats.expon(2).mean() =", stats.expon(2).mean(), "· stats.uniform(2, 8).var() =", stats.uniform(2, 8).var())''',
    record='''wbm.record("M02b.21a", 0.242828896, decimals=4,
           mistakes={"pmf(3) donne P(X = 3) ; cdf(3) donnerait P(X ≤ 3)": 0.647725174})
wbm.record("M02b.21b", 0.173578071, decimals=4,
           mistakes={"cdf(2) = P(X ≤ 2) ; pmf(2) donne seulement P(X = 2)": 0.112478590})
wbm.record("M02b.21c", 0.977249868, decimals=4,
           mistakes={"stats.norm(loc, scale) attend l'écart-type 15, pas la variance 225": 0.553035117})
wbm.record("M02b.21d", 119.223273483, decimals=2,
           mistakes={"le percentile 90 est ppf(0.9), une valeur de X ; cdf donne une probabilité": 1.0,
                     "stats.norm(loc, scale) attend l'écart-type 15, pas la variance 225": 388.349102})
wbm.record("M02b.21e", 0.5, decimals=1,
           mistakes={"stats.expon(2) fixe loc = 2, un décalage ; le paramètre λ se donne par scale = 1/λ": 3.0,
                     "scale = 1/λ, l'inverse du paramètre": 2.0})
wbm.record("M02b.21f", 1.959963985, decimals=4,
           mistakes={"ppf est la réciproque de cdf : ppf(0.975), pas cdf(0.975)": 0.835219870})
wbm.record("M02b.21g", 4.4493, decimals=4)
wbm.record("M02b.21h", 3.0, decimals=1,
           mistakes={"stats.uniform(loc, scale) couvre [loc ; loc + scale] : scale est la largeur de l'intervalle":
                         5.333333})''',
    note="e) $\\frac{1}{\\lambda} = 0{,}5$ et h) $\\frac{(8 - 2)^2}{12} = 3$ (le tableau de la fiche §4). Les deux "
         "pièges de `scipy.stats` : `stats.expon(2)` décale la loi de 2 (espérance 3) ; `stats.uniform(2, 8)` couvre "
         "$[2 ; 10]$ (variance $\\frac{64}{12}$). d) avec la table : $100 + 1{,}2816 \\times 15 \\approx 119{,}22$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a prediction, an experiment, a figure (M02b.22 to M02b.24)
# ---------------------------------------------------------------------------
M02B_22_EXPERIMENT = '''rng_22 = np.random.default_rng(0)
dice = rng_22.integers(1, 9, size=(100_000, 4))          # 100 000 rows of 4 eight-sided dice
one = dice[:, 0]
print(f"variance d'un dé                        : {one.var():.3f}")
print(f"variance de la moyenne des 4 dés         : {dice.mean(axis=1).var():.3f}")
print(f"écart-type d'un dé / celui de la moyenne : {one.std() / dice.mean(axis=1).std():.2f}")
print(f"variance de la somme des 4 dés           : {dice.sum(axis=1).var():.3f}")
print(f"variance de 4 fois un seul dé            : {(4 * one).var():.3f}")'''

M02B_22 = Ex(
    "M02b.22", "🔮", 1, 10, "Prédire : la variance de la moyenne de quatre dés",
    "prévoir l'effet d'une somme et d'une moyenne de variables indépendantes sur la variance et l'écart-type, puis "
    "le vérifier par simulation.", "fiche §6", tracks="C, E", hypothesis=True,
    body="""On lance quatre dés équilibrés à 8 faces (numérotées de 1 à 8), indépendants. Pour chaque question, choisis : (1) la même ; (2) multipliée (ou divisée) par 2 ; (3) multipliée (ou divisée) par 4 ; (4) multipliée (ou divisée) par 16.
- a) la variance de la **moyenne** des quatre dés, comparée à la variance d'un dé ;
- b) l'écart-type de cette moyenne, comparé à l'écart-type d'un dé ;
- c) la variance de la **somme** des quatre dés, comparée à la variance d'un dé ;
- d) la variance de **4 fois** le résultat d'un seul dé, comparée à la variance d'un dé.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**, de 1 à 4), vérifie-les, puis lance l'expérience : 100 000 lancers de quatre dés.""",
    todo='''prediction_M02b_22a = ...  # a) 1, 2, 3 or 4, written BEFORE running the experiment below
prediction_M02b_22b = ...  # b) 1, 2, 3 or 4
prediction_M02b_22c = ...  # c) 1, 2, 3 or 4
prediction_M02b_22d = ...  # d) 1, 2, 3 or 4''',
    check='''for letter, prediction in zip("abcd", [prediction_M02b_22a, prediction_M02b_22b, prediction_M02b_22c,
                                      prediction_M02b_22d]):
    wbm.check(f"M02b.22{letter}", prediction)''',
    record='''wbm.record("M02b.22a", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M02b.22b", 2, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M02b.22c", 3, prediction=True, choices=[1, 2, 3, 4])
wbm.record("M02b.22d", 4, prediction=True, choices=[1, 2, 3, 4])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(M02B_22_EXPERIMENT, ["prediction_M02b_22a", "prediction_M02b_22b", "prediction_M02b_22c",
                                               "prediction_M02b_22d"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", M02B_22_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : écris les quatre résultats avec les formules de la fiche §6 "
               "($\\mathbb{V}(X_1 + \\cdots + X_n)$, $\\mathbb{V}(aX)$, $\\mathbb{V}(\\bar{X})$). Pourquoi c) et d) "
               "diffèrent-ils, alors que la somme de quatre dés et 4 fois un dé ont la même espérance ?"),
    ],
    note="Un dé à 8 faces a pour variance $\\frac{8^2 - 1}{12} = 5{,}25$ (la loi uniforme sur $\\{1, \\ldots, n\\}$ a pour "
         "variance $\\frac{n^2 - 1}{12}$). a) La moyenne de 4 dés indépendants a pour variance $\\frac{5{,}25}{4} \\approx 1{,}31$ : "
         "divisée par 4 ; b) son écart-type est donc divisé par $\\sqrt{4} = 2$. c) La somme a pour variance "
         "$4 \\times 5{,}25$ : multipliée par 4 (les variances s'additionnent). d) $4X$ a pour variance $16 \\times 5{,}25$ : "
         "multipliée par 16. Quatre dés différents se "
         "compensent en partie ; un seul dé multiplié par 4 amplifie chaque écart, sans compensation.",
)

M02B_23_GIVEN = '''N_LIST = [5, 10, 30, 100, 1000]
LAM = 3'''

M02B_23 = Ex(
    "M02b.23", "🔬", 2, 20, "Binomiale et Poisson côte à côte quand n grandit",
    "mesurer l'écart entre la loi binomiale $\\mathcal{B}(n, \\frac{\\lambda}{n})$ et la loi de Poisson, et trouver "
    "à quelle vitesse il diminue.", "fiche §2 ; Ex M02b.13 (la limite)", tracks="C",
    body="""Pour chaque $n$ de `N_LIST`, on compare la loi binomiale $\\mathcal{B}\\big(n, \\frac{3}{n}\\big)$ et la loi de Poisson $\\mathcal{P}(3)$ (cellule fournie : `N_LIST`, `LAM` $= 3$). L'**écart** entre les deux est le plus grand des écarts entre leurs probabilités, $\\max_{0 \\le k \\le n} \\big\\lvert P(B = k) - P(N = k) \\big\\rvert$. Calcule-le avec `scipy.stats` (`stats.binom(n, p).pmf(ks)` et `stats.poisson(LAM).pmf(ks)` acceptent un array `ks = np.arange(n + 1)`), dans une liste `gaps`, dans l'ordre de `N_LIST`.

Puis :
- a) l'écart pour $n = 10$ (4 décimales) ;
- b) l'écart pour $n = 1\\,000$ (5 décimales) ;
- c) le rapport de l'écart pour $n = 100$ à l'écart pour $n = 1\\,000$ (1 décimale) ;
- d) le plus petit $n$ de `N_LIST` pour lequel l'écart est inférieur à 0,01 (un entier).

Trace ensuite les écarts en fonction de $n$, en échelles logarithmiques sur les deux axes (`ax.loglog`).

Dans ta copie : quelle pente lis-tu sur ta courbe ? Que dit c) de la vitesse de convergence ? D'après b), à partir de quel $n$ l'approximation de Poisson te semble-t-elle suffisante pour calculer une probabilité à 2 décimales ?""",
    given=M02B_23_GIVEN,
    todo='''gaps = ...           # the 5 gaps, in the order of N_LIST
gap_10 = ...         # a) a number
gap_1000 = ...       # b) a number
ratio_100_1000 = ... # c) a number
first_n = ...        # d) an integer of N_LIST''',
    check='''wbm.check("M02b.23a", gap_10)
wbm.check("M02b.23b", gap_1000)
wbm.check("M02b.23c", ratio_100_1000)
wbm.check("M02b.23d", first_n)''',
    solution='''def gap(n):
    ks = np.arange(n + 1)
    return float(np.max(np.abs(stats.binom(n, LAM / n).pmf(ks) - stats.poisson(LAM).pmf(ks))))


gaps = [gap(n) for n in N_LIST]
gap_10, gap_1000 = gaps[1], gaps[4]
ratio_100_1000 = gaps[3] / gaps[4]
first_n = next(n for n, g in zip(N_LIST, gaps) if g < 0.01)
print([f"{g:.2e}" for g in gaps], " c)", round(ratio_100_1000, 1), " d)", first_n)''',
    record='''wbm.record("M02b.23a", 0.042786124, decimals=4)
wbm.record("M02b.23b", 0.000336764, decimals=5)
wbm.record("M02b.23c", 10.192, decimals=1,
           mistakes={"l'écart pour n = 100 divisé par l'écart pour n = 1 000, dans cet ordre": 0.098})
wbm.record("M02b.23d", 100,
           mistakes={"compare chaque écart à 0,01 : pour n = 30, il est encore au-dessus": 30})''',
    after=[("md", "**Le tracé** des écarts en fonction de $n$, en échelles logarithmiques (`ax.loglog`)."),
           ("todo", "# the plot of gaps against N_LIST, log scales on both axes"),
           ("solution", '''fig, ax = plt.subplots(figsize=(6, 3.5))
ax.loglog(N_LIST, gaps, marker="o", label="écart binomiale − Poisson")
ax.loglog(N_LIST, [0.4 / n for n in N_LIST], "--", color="gray", label="0,4 / n (pente −1)")
ax.set(xlabel="n", ylabel="écart (échelle log)", title="L'écart diminue comme 1/n")
ax.legend()
ax.grid(True, which="both", alpha=0.3)
plt.show()''')],
    note="L'écart vaut environ 0,12 ; 0,043 ; 0,012 ; 0,0034 ; 0,00034 : il est divisé par 10 quand $n$ est multiplié "
         "par 10, une pente de $-1$ en échelles logarithmiques. L'écart diminue comme $\\frac{1}{n}$, c'est-à-dire "
         "comme $p$ : la loi de Poisson est une bonne approximation quand $p$ est petit, quel que soit $n$ (un "
         "théorème dit que l'écart est au plus de l'ordre de $p$). Pour 2 décimales, $n = 100$ ($p = 0{,}03$) suffit "
         "déjà largement.",
)

M02B_24_GIVEN = '''# The joint law of (the smaller, the larger) of two fair dice: rows = min (1 to 6), columns = max (1 to 6)
JOINT_24 = np.zeros((6, 6))
for a in range(1, 7):
    for b in range(1, 7):
        JOINT_24[min(a, b) - 1, max(a, b) - 1] += 1 / 36


def joint_axes():
    """A figure with three axes: the heat map, the margin of the rows above it, the margin of the columns on its
    right."""
    fig = plt.figure(figsize=(6.5, 5))
    grid = fig.add_gridspec(2, 2, width_ratios=(4, 1.3), height_ratios=(1.3, 4), wspace=0.08, hspace=0.08)
    ax = fig.add_subplot(grid[1, 0])
    return fig, ax, fig.add_subplot(grid[0, 0], sharex=ax), fig.add_subplot(grid[1, 1], sharey=ax)'''

M02B_24_CHECK = '''with checked("M02b.24 vérifications"):
    problems = []
    test_joint = np.array([[0.1, 0.2, 0.0], [0.05, 0.15, 0.5]])      # 2 rows, 3 columns: a law that is not square
    margins = marginals(test_joint)
    if margins is None:
        problems.append("marginals ne renvoie rien (None) : il manque un return")
    else:
        p_rows, p_cols = (np.asarray(m, dtype=float) for m in margins)
        if p_rows.shape != (2,) or not np.allclose(p_rows, [0.3, 0.7]):
            problems.append("marginals : la loi des lignes somme chaque ligne (sur les colonnes), axis=1")
        if p_cols.shape != (3,) or not np.allclose(p_cols, [0.15, 0.35, 0.5]):
            problems.append("marginals : la loi des colonnes somme chaque colonne (sur les lignes), axis=0")
    fig, ax, ax_top, ax_right = joint_axes()
    try:
        created = drawn(draw_joint, ax, ax_top, ax_right, test_joint)
    finally:
        plt.close(fig)                                   # only the checks below are shown here
    if created:
        problems.append("draw_joint ouvre sa propre figure : dessine dans les trois axes reçus")
    else:
        images = ax.get_images()
        if not images or np.asarray(images[0].get_array()).shape != (3, 2) or not np.allclose(
                np.asarray(images[0].get_array()), test_joint.T):
            problems.append("draw_joint : la carte de chaleur ax.imshow(joint.T, origin=\\"lower\\"), les valeurs de "
                            "la première variable (les lignes de joint) à l'horizontale")
        top = sorted(round(p.get_height(), 6) for p in ax_top.patches)
        if top != [0.3, 0.7]:
            problems.append("draw_joint : au-dessus, les barres de la loi des lignes (ax_top.bar)")
        right = sorted(round(p.get_width(), 6) for p in ax_right.patches)
        if right != [0.15, 0.35, 0.5]:
            problems.append("draw_joint : à droite, les barres horizontales de la loi des colonnes (ax_right.barh)")
    if problems:
        print("❌ Ex M02b.24 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M02b.24 : les marginales, la carte de chaleur et les deux barres des bords.")'''

M02B_24 = Ex(
    "M02b.24", "🎨", 1, 20, "Une loi jointe en carte de chaleur, ses marginales sur les bords",
    "représenter une loi jointe discrète par une carte de chaleur, avec ses deux lois marginales sur les bords, et "
    "mesurer l'écart à l'indépendance.", "fiche §5 ; R0 (matplotlib)", tracks="C",
    body="""On lance deux dés équilibrés ; $X$ est le plus petit des deux numéros, et $Y$ le plus grand (le même s'ils sont égaux). La cellule fournie construit leur loi jointe `JOINT_24` (un array 6 × 6 : la ligne $i$ correspond à $X = i + 1$, la colonne $j$ à $Y = j + 1$) et une fonction `joint_axes()` qui prépare une figure à trois axes.

Complète :
- `marginals(joint)`, qui renvoie le couple `(p_rows, p_cols)` des deux lois marginales : celle de la variable des lignes (somme de chaque ligne, `axis=1`) et celle de la variable des colonnes (`axis=0`) ;
- `draw_joint(ax, ax_top, ax_right, joint)`, qui dessine dans `ax` la carte de chaleur `ax.imshow(joint.T, origin="lower", cmap="Blues")` (la variable des lignes à l'horizontale), dans `ax_top` les barres de `p_rows` (`ax_top.bar`), et dans `ax_right` les barres horizontales de `p_cols` (`ax_right.barh`).

Puis calcule `max_gap_24`, le plus grand écart $\\big\\lvert P(X = x, Y = y) - P(X = x)\\,P(Y = y) \\big\\rvert$ sur les 36 cases (`np.outer` fabrique le tableau des produits ; 4 décimales).

Dans ta copie : pourquoi la moitié de la carte est-elle vide ? Pourquoi la diagonale est-elle plus claire que les cases au-dessus ? $X$ et $Y$ sont-elles indépendantes ? Quelle case le montre le plus nettement, sans aucun calcul ?""",
    given=M02B_24_GIVEN,
    todo='''def marginals(joint):
    """The two margins (p_rows, p_cols) of a discrete joint law given as a 2D array."""
    raise NotImplementedError("joint.sum(axis=1) pour les lignes, joint.sum(axis=0) pour les colonnes")


def draw_joint(ax, ax_top, ax_right, joint):
    """Draw the heat map of joint in ax, the margin of the rows above (ax_top), the margin of the columns on the
    right (ax_right)."""
    raise NotImplementedError("ax.imshow(joint.T, origin=\\"lower\\"), ax_top.bar, ax_right.barh")


max_gap_24 = ...   # the largest |P(X = x, Y = y) − P(X = x) P(Y = y)| (4 decimals)''',
    check='''with checked("M02b.24 figure"):
    fig, ax, ax_top, ax_right = joint_axes()
    try:
        created = drawn(draw_joint, ax, ax_top, ax_right, JOINT_24)
    except BaseException:
        plt.close(fig)                                     # no empty figure while the functions are not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M02b.24 : draw_joint ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans les axes "
              "reçus.")
    else:
        ax.set(xlabel="X : le plus petit numéro", ylabel="Y : le plus grand numéro")
        ax.set_xticks(range(6), labels=range(1, 7))
        ax.set_yticks(range(6), labels=range(1, 7))
        plt.show()
wbm.check("M02b.24", max_gap_24)''',
    solution='''def marginals(joint):
    """The two margins (p_rows, p_cols) of a discrete joint law given as a 2D array."""
    joint = np.asarray(joint, dtype=float)
    return joint.sum(axis=1), joint.sum(axis=0)


def draw_joint(ax, ax_top, ax_right, joint):
    """Draw the heat map of joint in ax, the margin of the rows above (ax_top), the margin of the columns on the
    right (ax_right)."""
    p_rows, p_cols = marginals(joint)
    ax.imshow(np.asarray(joint).T, origin="lower", cmap="Blues", aspect="auto")
    ax_top.bar(np.arange(len(p_rows)), p_rows, color="C0")
    ax_top.tick_params(labelbottom=False)
    ax_right.barh(np.arange(len(p_cols)), p_cols, color="C1")
    ax_right.tick_params(labelleft=False)


fig, ax, ax_top, ax_right = joint_axes()
draw_joint(ax, ax_top, ax_right, JOINT_24)
ax.set(xlabel="X : le plus petit numéro", ylabel="Y : le plus grand numéro")
ax.set_xticks(range(6), labels=range(1, 7))
ax.set_yticks(range(6), labels=range(1, 7))
plt.show()
p_min, p_max = marginals(JOINT_24)
max_gap_24 = float(np.max(np.abs(JOINT_24 - np.outer(p_min, p_max))))
print("P(X = x) × 36:", np.round(p_min * 36, 6), "· P(Y = y) × 36:", np.round(p_max * 36, 6), "· max gap:",
      round(max_gap_24, 4))''',
    record='''wbm.record("M02b.24", 0.037808642, decimals=4,
           mistakes={"le produit des marginales se calcule case par case : np.outer(p_rows, p_cols)": 0.0})''',
    after=[("md", "**Vérifications automatiques** (la figure elle-même se juge à l'œil)."), ("code", M02B_24_CHECK)],
    note="La moitié sous la diagonale est vide : le plus petit numéro ne dépasse jamais le plus grand. Une case de la "
         "diagonale vaut $\\frac{1}{36}$ (les deux dés égaux : un seul couple), une case au-dessus $\\frac{2}{36}$ "
         "(deux couples, $(a, b)$ et $(b, a)$). Les marginales valent $\\frac{13 - 2x}{36}$ et $\\frac{2y - 1}{36}$. "
         "Les variables sont dépendantes, et les cases vides le montrent sans calcul : $P(X = 6, Y = 1) = 0$, alors "
         "que $P(X = 6)\\,P(Y = 1) = \\frac{1}{36^2} > 0$. Le plus grand écart, 0,0378, est en $(1, 6)$ : "
         "$\\frac{2}{36} \\approx 0{,}056$ contre $\\left(\\frac{11}{36}\\right)^2 \\approx 0{,}093$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a bug hunt, a pro skill, a challenge (M02b.25 to M02b.27)
# ---------------------------------------------------------------------------
M02B_25_MISTAKES = bug_letters_mistakes(
    "ABD", "CE",
    {"A": "relis chaque phrase qui compare une densité à 1 : seule l'aire d'une densité doit valoir 1",
     "B": "relis chaque notation N(μ, ·) : le second paramètre est la variance, et l'on standardise par l'écart-type",
     "D": "relis chaque probabilité d'une valeur exacte pour une variable à densité"})

M02B_25 = Ex(
    "M02b.25", "🐛", 1, 15, "Chasse à l'erreur : une densité prise pour une probabilité, σ et σ²",
    "repérer trois confusions classiques sur les lois continues, puis calculer les bonnes valeurs.",
    "fiche §3, §4 et §6", tracks="C",
    body="""Voici cinq affirmations, chacune avec le raisonnement de son auteur. Trois sont fausses. **Sans exécuter de code**, trouve-les.

- **(A)** « $X \\sim \\mathcal{N}(0 ;\\ 0{,}1^2)$ a pour densité en 0 environ 3,99. C'est impossible, car une probabilité ne dépasse jamais 1 : la formule doit être fausse. »
- **(B)** « $X \\sim \\mathcal{N}(5, 4)$, donc $P(X \\le 7) = \\Phi\\left(\\frac{7 - 5}{4}\\right) = \\Phi(0{,}5) \\approx 0{,}6915$. »
- **(C)** « $X \\sim \\mathcal{U}([0 ; 4])$ a pour variance $\\frac{16}{12} = \\frac{4}{3}$, donc pour écart-type $\\approx 1{,}1547$. »
- **(D)** « $T \\sim \\mathcal{E}(2)$, donc $P(T = 1) = f(1) = 2e^{-2} \\approx 0{,}2707$. »
- **(E)** « $X$ et $Y$ sont indépendantes, d'écarts-types 3 et 4, donc $\\sigma(X + Y) = 5$. »

Questions :
- a) les lettres des affirmations fausses, dans l'ordre alphabétique (un texte) ;
- b) pour chacune des cinq, de (A) à (E), la bonne valeur de la grandeur dont parle son auteur : la densité en 0 pour (A), $P(X \\le 7)$ pour (B), l'écart-type pour (C), $P(T = 1)$ pour (D), $\\sigma(X + Y)$ pour (E) (une liste de 5 nombres, 4 décimales).

Dans ta copie : pour chaque affirmation fausse, quelle confusion a été faite ? Dans (A), la valeur 3,99 est-elle juste ?""",
    todo='''answer_M02b_25a = ...  # a) letters, as text
answer_M02b_25b = ...  # b) a list of 5 values (4 decimals)''',
    check='''wbm.check("M02b.25a", answer_M02b_25a)
wbm.check("M02b.25b", answer_M02b_25b)''',
    solution='''answer_M02b_25a = "ABD"
answer_M02b_25b = [stats.norm(0, 0.1).pdf(0), stats.norm(5, 2).cdf(7), math.sqrt(16 / 12), 0.0, math.sqrt(3 ** 2 + 4 ** 2)]
print(answer_M02b_25a, [round(float(v), 4) for v in answer_M02b_25b])''',
    record=f'''wbm.record("M02b.25a", "ABD",
           mistakes={M02B_25_MISTAKES})
wbm.record("M02b.25b", [3.989422804, 0.841344746, 1.154700538, 0.0, 5.0], decimals=4,
           mistakes={{"ce sont les valeurs des auteurs ; donne les bonnes valeurs des grandeurs dont ils parlent":
                         [0.0, 0.691462461, 1.154700538, 0.270670566, 5.0],
                     "(D) : une valeur exacte a une probabilité nulle pour une variable à densité":
                         [3.989422804, 0.841344746, 1.154700538, 0.270670566, 5.0],
                     "(B) : N(5, 4) a pour écart-type 2, et l'on standardise par l'écart-type":
                         [3.989422804, 0.691462461, 1.154700538, 0.0, 5.0],
                     "(A) : la valeur 3,99 de la densité est juste ; c'est le raisonnement qui est faux":
                         [0.0, 0.841344746, 1.154700538, 0.0, 5.0]}})''',
    note="(A) La valeur est juste ($\\frac{1}{0{,}1\\sqrt{2\\pi}} \\approx 3{,}9894$), le raisonnement faux : une "
         "densité n'est pas une probabilité, et seule son aire vaut 1. (B) $\\mathcal{N}(5, 4)$ a pour variance 4, donc "
         "pour écart-type 2 : $\\Phi\\big(\\frac{7 - 5}{2}\\big) = \\Phi(1) \\approx 0{,}8413$. (D) Pour une variable à "
         "densité, $P(T = 1) = 0$ ; $f(1)$ est une probabilité par unité de temps. (C) et (E) sont justes : "
         "$\\sqrt{9 + 16} = 5$.",
)

M02B_26_CHECK = '''with checked("M02b.26 vérifications"):
    import doctest

    problems = []
    doc = geometric_pmf.__doc__ or ""
    for word in ("Parameters", "Returns", "Raises", "Examples"):
        if word not in doc:
            problems.append(f"la docstring n'a pas de section « {word} » (le format NumPy des docstrings de mymath)")
    tests = doctest.DocTestFinder().find(geometric_pmf, "geometric_pmf", globs={"geometric_pmf": geometric_pmf})
    runner = doctest.DocTestRunner(optionflags=doctest.ELLIPSIS)
    for test in tests:
        runner.run(test, out=lambda text: None)
    attempted, failed = runner.tries, runner.failures
    if attempted < 3:
        problems.append(f"la docstring a {attempted} exemple(s) >>> : il en faut au moins 3 (une valeur ordinaire, "
                        "k = 0, et le cas d'erreur)")
    if failed:
        problems.append(f"{failed} exemple(s) de la docstring échoue(nt) : exécute "
                        "doctest.run_docstring_examples(geometric_pmf, globals()) pour les voir")
    if "ValueError" not in doc:
        problems.append("aucun exemple ne montre la ValueError (un exemple peut afficher Traceback ... ValueError)")
    cases = [(1, 0.25), (4, 0.25), (10, 0.6), (3, 1.0)]
    wrong = [(k, p) for k, p in cases if abs(geometric_pmf(k, p) - float(stats.geom(p).pmf(k))) > 1e-12]
    if wrong:
        problems.append(f"geometric_pmf se trompe, par exemple pour (k, p) = {wrong[0]} : (1 − p)^(k − 1) p")
    if geometric_pmf(0, 0.3) != 0.0 or geometric_pmf(-2, 0.3) != 0.0:
        problems.append("geometric_pmf(0, p) et geometric_pmf(-2, p) valent 0.0 : le premier succès a un rang au "
                        "moins égal à 1")
    if raised(geometric_pmf, 2, 0) != "ValueError" or raised(geometric_pmf, 2, 1.5) != "ValueError":
        problems.append("geometric_pmf lève une ValueError si p n'est pas dans ]0 ; 1]")
    if problems:
        print("❌ Ex M02b.26 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print(f"✅ Ex M02b.26 : une docstring complète, {attempted} exemples qui passent, et une fonction juste.")'''

M02B_26 = Ex(
    "M02b.26", "🛠️", 1, 15, "Documenter une loi : docstring et exemples testés (`doctest`)",
    "écrire une docstring au format NumPy dont les exemples sont exécutés comme des tests, réflexe professionnel "
    "pour une fonction de bibliothèque.", "fiche §2 ; les docstrings de `mymath`", tracks="C",
    body="""Les docstrings de `mymath` suivent le format NumPy (sections `Parameters`, `Returns`, `Raises`, `Examples`), et leurs exemples `>>>` sont des **tests** : le module `doctest` les exécute et compare le résultat affiché à celui qui est écrit. Une documentation testée ne ment pas.

Écris `geometric_pmf(k, p)`, la probabilité $P(X = k) = (1 - p)^{k-1}p$ de la loi géométrique (fiche §2), qui vaut `0.0` pour $k < 1$ et lève une `ValueError` si $p$ n'est pas dans $]0 ; 1]$, **avec sa docstring complète** : les quatre sections, et au moins trois exemples, dont une valeur ordinaire, le cas $k = 0$, et le cas d'erreur. Un exemple qui lève une erreur s'écrit ainsi :

```
>>> geometric_pmf(2, 1.5)
Traceback (most recent call last):
    ...
ValueError: p must be in ]0, 1]
```

(le message après `ValueError:` doit être exactement celui que lève ta fonction). Exécute ensuite tes exemples avec `doctest.run_docstring_examples(geometric_pmf, globals())` : rien ne s'affiche s'ils passent tous.

Dans ta copie : pourquoi un exemple de docstring qui n'est pas testé finit-il souvent par être faux ? Pourquoi écrire `round(..., 4)` dans un exemple qui affiche un flottant ?""",
    todo='''def geometric_pmf(k, p):
    """TODO: a one-line summary, then the sections Parameters, Returns, Raises and Examples (at least 3 examples)."""
    raise NotImplementedError("la formule (1 − p)^(k − 1) p, les cas k < 1 et p hors de ]0 ; 1], puis la docstring")''',
    solution='''def geometric_pmf(k, p):
    """Return ``P(X = k)`` for ``X`` following the geometric law of parameter ``p`` (rank of the first success).

    Parameters
    ----------
    k : int
        Any integer: the probability is 0.0 when ``k < 1``.
    p : float
        Probability of success of each trial, in ``]0, 1]``.

    Returns
    -------
    float
        ``(1 - p)**(k - 1) * p``.

    Raises
    ------
    ValueError
        If ``p`` is not in ``]0, 1]``.

    Examples
    --------
    >>> geometric_pmf(3, 0.5)
    0.125
    >>> geometric_pmf(0, 0.5)
    0.0
    >>> round(geometric_pmf(2, 0.1), 4)
    0.09
    >>> geometric_pmf(2, 1.5)
    Traceback (most recent call last):
        ...
    ValueError: p must be in ]0, 1]
    """
    if not 0 < p <= 1:
        raise ValueError("p must be in ]0, 1]")
    if k < 1:
        return 0.0
    return float((1 - p) ** (k - 1) * p)


import doctest

doctest.run_docstring_examples(geometric_pmf, globals())   # silent: every example passes''',
    after=[("code", M02B_26_CHECK)],
    note="Un exemple non testé dérive : on change la fonction, on oublie l'exemple, et la documentation ment. `doctest` "
         "compare des **textes** : un flottant affiché avec 17 chiffres (`0.09000000000000001`) ferait échouer "
         "l'exemple, d'où `round(..., 4)`, ou une valeur exacte en binaire comme 0,125. Les tests de `mymath` "
         "exécutent aussi les exemples des docstrings (le test « docstring example » de chaque fonction).",
)

M02B_27_GIVEN = '''class UniformOnly:
    """A generator that can only draw uniform numbers in [0, 1): random(size)."""

    def __init__(self, seed):
        self._rng = np.random.default_rng(seed)

    def random(self, size=None):
        return self._rng.random(size)


FORBIDDEN_27 = ("normal", "standard_normal", "scipy", "ppf", "erfinv", "NormalDist", "default_rng", "Generator")'''

M02B_27_CHECK = '''with checked("M02b.27"):
    import ast
    import inspect
    import time

    try:
        source = inspect.getsource(normal_draws)
    except (OSError, TypeError):
        source = ""
    names = {node.attr for node in ast.walk(ast.parse(source)) if isinstance(node, ast.Attribute)} | {
        node.id for node in ast.walk(ast.parse(source)) if isinstance(node, ast.Name)} if source else set()
    used = sorted(names & set(FORBIDDEN_27)) + sorted(word for word in ("scipy", "statistics") if word in source)
    start = time.perf_counter()
    big = np.asarray(normal_draws(UniformOnly(2026), 1_000_000), dtype=float)
    seconds = time.perf_counter() - start
    small = np.asarray(normal_draws(UniformOnly(7), 200_000), dtype=float)
    p_value = stats.kstest(small, "norm").pvalue if small.shape == (200_000,) else 0.0
    tail = float(np.mean(np.abs(big) > 4)) if big.shape == (1_000_000,) else 0.0
    print(f"forme : {big.shape} · test de Kolmogorov-Smirnov sur 200 000 valeurs : p = {p_value:.3f} · "
          f"part des |z| > 4 sur un million : {tail:.1e} (loi normale : 6,3e-05) · temps : {seconds:.2f} s")
    reasons = []
    if used:
        reasons.append(f"des outils interdits ({', '.join(sorted(set(used)))}) : seulement rng.random")
    if big.shape != (1_000_000,):
        reasons.append("un array de forme (n,)")
    if p_value <= 0.01:
        reasons.append("le test de Kolmogorov-Smirnov rejette la loi normale (p ≤ 0,01)")
    if not 3e-5 <= tail <= 1e-4:
        reasons.append("les queues ne sont pas celles d'une loi normale (valeurs au-delà de 4 écarts-types)")
    if seconds > 3:
        reasons.append("plus de 3 secondes pour un million de valeurs : vectorise avec NumPy")
    for reason in reasons:
        print(f"❌ {reason}")
    wbm.check("M02b.27", not reasons, computed=True)'''

M02B_27 = Ex(
    "M02b.27", "🏆", 3, 30, "Défi : tirer des valeurs normales avec seulement des tirages uniformes",
    "fabriquer des tirages de la loi normale centrée réduite à partir de nombres uniformes, assez fidèles pour passer "
    "un test statistique et reproduire les queues de la loi.", "fiche §7 et §8 ; Ex M02b.12 et M02b.20", tracks="C",
    body="""Écris `normal_draws(rng, n)`, qui renvoie un array de $n$ tirages de $\\mathcal{N}(0, 1)$ en n'utilisant **que** `rng.random(size)` : le générateur `UniformOnly` de la cellule fournie ne sait rien faire d'autre, et la vérification refuse `normal`, `scipy`, `ppf`, `erfinv`, `NormalDist` et un générateur à toi. **Objectifs**, vérifiés sur un million de valeurs :
1. le test de Kolmogorov-Smirnov (`stats.kstest`, qui compare la fonction de répartition des tirages à $\\Phi$) ne rejette pas la loi normale : $p > 0{,}01$ sur 200 000 valeurs ;
2. les **queues** sont justes : la part des valeurs au-delà de 4 en valeur absolue est entre $3 \\times 10^{-5}$ et $10^{-4}$ (la loi normale donne $2(1 - \\Phi(4)) \\approx 6{,}3 \\times 10^{-5}$) ;
3. moins de 3 secondes pour un million de valeurs.

Pistes, de la plus simple à la plus élégante (`04_indices.md` les détaille) :
- additionner 12 uniformes et retrancher 6 (le théorème central limite) : tente-la, et regarde quel objectif elle manque, et pourquoi ;
- inverser $\\Phi$ par dichotomie (M02a.18) : juste, mais lente, car `math.erf` ne traite qu'un nombre à la fois (essaie-la sur 1 000 valeurs) ;
- une transformation de **deux** uniformes en **deux** normales indépendantes, qui vient de l'intégrale de Gauss en coordonnées polaires (M02b.12, question 6 : la loi jointe de deux normales indépendantes ne dépend que de la distance au centre).

Dans ta copie : quelle méthode as-tu retenue, et pourquoi la somme de 12 uniformes échoue-t-elle sur les queues ? Pour la méthode polaire, quelle est la loi de $R^2 = X^2 + Y^2$ ?""",
    given=M02B_27_GIVEN,
    todo='''def normal_draws(rng, n):
    """Return n draws of N(0, 1) as an array of shape (n,), using only rng.random(size)."""
    raise NotImplementedError("seulement rng.random : une somme d'uniformes, une dichotomie, ou deux uniformes en polaire")''',
    check=M02B_27_CHECK,
    solution='''def normal_draws(rng, n):
    """Return n draws of N(0, 1) as an array of shape (n,), using only rng.random(size): the Box-Muller method."""
    m = (n + 1) // 2
    radius = np.sqrt(-2 * np.log(1 - rng.random(m)))     # R² = −2 ln(1 − U) follows the exponential law of mean 2
    angle = 2 * np.pi * rng.random(m)                     # the angle is uniform on [0, 2π[
    return np.concatenate([radius * np.cos(angle), radius * np.sin(angle)])[:n]


clt = UniformOnly(1).random((1_000_000, 12)).sum(axis=1) - 6       # the first idea: 12 uniforms, minus 6
print(f"12 uniforms: |z| > 4 for a share {np.mean(np.abs(clt) > 4):.1e}, max |z| = {np.abs(clt).max():.2f}")
draws = normal_draws(UniformOnly(2026), 1_000_000)
print(f"Box-Muller: mean {draws.mean():.4f}, std {draws.std():.4f}, |z| > 4 for a share {np.mean(np.abs(draws) > 4):.1e}")''',
    record='''wbm.record("M02b.27", True,
           mistakes={"un objectif au moins n'est pas atteint : relis les lignes ❌ et les pistes de 04_indices.md":
                         False})''',
    note="La somme de 12 uniformes a la bonne espérance et la bonne variance, et une forme de cloche presque parfaite au "
         "centre, mais elle ne dépasse jamais 6 et ses queues sont bien trop minces : 1 à 2 valeurs sur 100 000 "
         "au-delà de 4, au lieu de 6,3. La méthode de **Box-Muller** (1958) tire le carré de la distance au centre, "
         "$R^2 = -2\\ln(1 - U_1)$, de loi exponentielle d'espérance 2 (fiche §8), et l'angle $\\Theta = 2\\pi U_2$, "
         "uniforme, puis renvoie $R\\cos\\Theta$ et $R\\sin\\Theta$ : deux normales indépendantes, exactement, parce "
         "que la densité jointe $\\frac{1}{2\\pi}e^{-r^2/2}$ ne dépend que de $r$ (M02b.12, question 6). L'inversion "
         "de $\\Phi$ par dichotomie donne des tirages justes, mais un million d'appels à `math.erf` par étape de "
         "dichotomie dépasse largement les 3 secondes.",
)

PART_A = Part("A", "Ta librairie : lois binomiale, de Poisson et normale, simulation par inversion",
              "Fiche §2, §3 et §8. Les cinq fonctions de `mymath/distributions.py`, puis les mêmes lois avec "
              "`scipy.stats`.",
              given=TOOLS, exercises=[M02B_18, M02B_19, M02B_20, M02B_21])

PART_B = Part("B", "Une prédiction, une expérience et une figure",
              "Fiche §2, §5 et §6. La variance d'une moyenne, la vitesse de l'approximation de Poisson, une loi jointe "
              "en carte de chaleur.",
              exercises=[M02B_22, M02B_23, M02B_24])

PART_C = Part("C", "Erreurs classiques, documentation et défi",
              "Fiche §3, §6, §7 et §8. Trois confusions à trouver, une docstring testée, puis des normales fabriquées "
              "avec des uniformes.",
              exercises=[M02B_25, M02B_26, M02B_27])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M02b.1 à M02b.10, M02b.14 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M02b · Variables aléatoires et lois usuelles — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m02b_variables_aleatoires/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M02b`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M02b · Variables aléatoires et lois usuelles — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : lois binomiale, géométrique, de Poisson, uniforme, "
               "exponentielle et normale, espérances et variances, loi jointe et indépendance, variance d'une somme, "
               "intégrale double, changement de variable, erreurs d'annotation.\n"
               "- Écrire les cinq fonctions de `mymath/distributions.py` et les tester, puis utiliser `scipy.stats`.\n"
               "- Prédire la variance d'une moyenne, mesurer l'écart entre binomiale et Poisson, dessiner une loi "
               "jointe, chasser des confusions, documenter une loi, tirer des normales avec des uniformes.\n\n"
               "**Rappel express.** $\\mathcal{B}(n, p)$ : $\\binom{n}{k}p^k(1-p)^{n-k}$, $\\mathbb{E} = np$, "
               "$\\mathbb{V} = np(1-p)$ ; $\\mathcal{P}(\\lambda)$ : $e^{-\\lambda}\\frac{\\lambda^k}{k!}$, "
               "$\\mathbb{E} = \\mathbb{V} = \\lambda$ ; $\\mathcal{E}(\\lambda)$ : $P(T > t) = e^{-\\lambda t}$, "
               "$\\mathbb{E} = \\frac{1}{\\lambda}$ ; $\\mathcal{N}(\\mu, \\sigma^2)$ : "
               "$P(X \\le x) = \\Phi\\big(\\frac{x - \\mu}{\\sigma}\\big)$. $\\mathbb{V}(X + Y) = \\mathbb{V}(X) + "
               "\\mathbb{V}(Y)$ si $X$ et $Y$ sont indépendantes. Inversion : $F^{-1}(U)$ suit la loi de $F$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Reconnais-tu la loi d'une situation, et calcules-tu ses probabilités, son espérance et sa variance ?\n"
               "2. Lis-tu une loi jointe, ses marginales, et sais-tu décider de l'indépendance ?\n"
               "3. Sais-tu calculer la variance d'une somme ou d'une moyenne, et simuler une loi par inversion ?\n\n"
               "**La suite** : M02c, les échantillons et l'estimation (loi des grands nombres, théorème central "
               "limite, intervalles de confiance, covariance), puis le chapitre 2 de workbookIA.")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter=CHAPTER) if kind == "exercise" else setup_cell(kind))
    cells += objectives_cell()
    cells += paper_cells(kind, PAPER, PAPER_CONTEXT, PAPER_INTRO,
                         learner_context="from fractions import Fraction   # Fraction(5, 9) is accepted too, as \"5/9\"\n"
                                         "import sympy as sp\n"
                                         "p, x, y = sp.symbols(\"p x y\")      # an expression typed without quotes works too")
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
