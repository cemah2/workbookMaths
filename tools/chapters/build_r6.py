#!/usr/bin/env python
"""Build the two notebooks of chapter R6 from a single source (used by Claude).

    python tools/chapters/build_r6.py
    python tools/run_all_notebooks.py chapitres/r6_exp_log/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/r6_exp_log/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ R6.1 to R6.8, 🔗 R6.11 and R6.12); parts A to C are the notebook exercises.
Wrong-answer messages state a rule, never a number of the answer. An exponent or a value is answered by a number, an
exponent in x by an expression between quotes, a solution set by an interval, several solutions by a list.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, guarded,  # noqa: E402
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "R6"
FOLDER = "chapitres/r6_exp_log"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("R6.1", "Simplifier avec les propriétés de exp", [
        ("a", "a number", "2.5",
         'decimals=2, mistakes={"multiplier des puissances de e, c\'est additionner les exposants, pas les multiplier": '
         '-6, "l\'exposant −1,5 est négatif : on l\'ajoute avec son signe": 5.5}'),
        ("b", "a number", "1.0",
         'decimals=2, mistakes={"une puissance de puissance multiplie les exposants, elle ne les additionne pas": 2, '
         '"diviser des puissances de e, c\'est soustraire les exposants, pas les diviser": 7 / 6}'),
        ("c", "an expression in x, as text", '"2 - 2*x"',
         'kind="expr", variables=("x",), mistakes={"multiplier des puissances, c\'est additionner les exposants": '
         '"3*x*(2 - 5*x)", "l\'exposant 2 − 5x garde son signe moins : additionne-le tel quel": "8*x + 2", '
         '"tous les termes des deux exposants s\'additionnent, le nombre seul compris": "-2*x"}'),
        ("d", "an expression in x, as text", '"2*x + 3"',
         'kind="expr", variables=("x",), mistakes={"multiplier des puissances de 2, c\'est additionner les exposants": '
         '"x*(x + 3)"}'),
        ("e", "an integer", "8.0",
         'decimals=2, mistakes={"16^(3/4) n\'est pas 16 × 3/4 : un exposant fractionnaire est une racine, puis une '
         'puissance": 12, "le dénominateur 4 de l\'exposant demande la racine quatrième, pas la racine carrée": 64, '
         '"le dénominateur de l\'exposant donne la racine, le numérateur la puissance : pas l\'inverse": 16 ** (4 / 3)}'),
        ("f", "a fraction, as text", "Fraction(1, 5)",
         'kind="fraction", mistakes={"un exposant négatif donne l\'inverse, pas un nombre négatif": "-5", '
         '"le signe moins de l\'exposant demande l\'inverse du résultat": "5", '
         '"un exposant négatif donne un nombre positif : l\'inverse": "-1/5"}'),
        ("g", "an expression in x, as text", '"2*x + 2"',
         'kind="expr", variables=("x",), mistakes={"diviser, c\'est soustraire les exposants, pas les additionner": '
         '"4*x - 2", "on soustrait tout l\'exposant x − 2 : mets-le entre parenthèses": "2*x - 2"}'),
        ("h", "an integer", "1", 'mistakes={"la question demande la valeur du nombre, pas son exposant": 0}'),
    ]),
    Paper("R6.2", "Simplifier avec les propriétés de ln", [
        ("a", "an integer", "2.0",
         'decimals=2, mistakes={"on soustrait les deux logarithmes, on ne les divise pas": 1.5, '
         '"3 ln(e²) est 3 fois ln(e²), pas 3 + ln(e²)": 1}'),
        ("b", "an integer", "5",
         'mistakes={"ln a − ln b = ln(a / b), pas ln(a − b)": 53, '
         '"soustraire des logarithmes, c\'est diviser, pas multiplier": 720, '
         '"les deux logarithmes sont soustraits : on divise par l\'un et par l\'autre": 45}'),
        ("c", "an integer", "36",
         'mistakes={"2 ln 3 = ln(3²), puis ln a + ln b = ln(a × b)": {10, 13}, "2 ln 3 = ln(3²), pas ln(2 × 3)": 24}'),
        ("d", "a fraction, as text", "Fraction(-5, 2)",
         'kind="fraction", mistakes={"ln(a / b) = ln a − ln b, pas ln a ÷ ln b": "1/6", '
         '"diviser des puissances de e, c\'est soustraire les exposants, pas les additionner": "7/2", '
         '"celui du numérateur moins celui du dénominateur : vérifie le signe": "5/2"}'),
        ("e", "an integer", "20", 'mistakes={"e^(ln 4 + ln 5) = e^(ln 4) × e^(ln 5) : un produit": 9}'),
        ("f", "an integer", "2.0",
         'decimals=2, mistakes={"e^(u − v) = e^u / e^v : un quotient, pas une différence": 4, '
         '"3 ln 2 = ln(2³), pas ln(3 × 2)": 1.5, "e^(u − v) est un quotient, pas un produit": 32}'),
        ("g", "an expression in a and b (not ln), as text", '"a + 2*b"',
         'kind="expr", variables=("a", "b"), mistakes={"2a + b vaut ln 12 : vérifie ta décomposition de 18 en facteurs '
         'premiers": "2*a + b", "ln(xy) = ln x + ln y, pas ln x × ln y": "a*b**2", '
         '"écris ta réponse avec les lettres a et b, pas avec ln": "log(2) + 2*log(3)"}'),
        ("h", "an expression in a and b (not ln), as text", '"b - 2*a"',
         'kind="expr", variables=("a", "b"), mistakes={"b − a vaut ln(3/2) : vérifie la décomposition du dénominateur": '
         '"b - a", "le logarithme d\'un quotient est celui du numérateur moins celui du dénominateur": "2*a - b", '
         '"écris ta réponse avec les lettres a et b, pas avec ln": "log(3) - 2*log(2)"}'),
    ]),
    Paper("R6.3", "Équations et inéquations avec exp et ln", [
        ("a", "a number (2 decimals)", "round(math.log(5), 2)",
         'decimals=2, mistakes={"isole d\'abord eˣ : retire 1, puis divise par 4, et seulement ensuite prends ln": '
         'round(math.log(20) / 4, 2), "isole eˣ en entier : il reste à diviser par 4": round(math.log(20), 2), '
         '"eˣ = c ⟺ x = ln c : le logarithme népérien, pas le décimal": round(math.log10(5), 2)}'),
        ("b", "a number (2 decimals)", "round((1 - math.log(6)) / 2, 2)",
         'decimals=2, mistakes={"1 − 2x = ln 6 : il reste à diviser par −2 les deux membres": round(1 - math.log(6), 2), '
         '"1 − 2x = ln 6 : retire 1 aux deux membres, puis divise par −2": round((1 + math.log(6)) / 2, 2)}'),
        ("c", "a number (2 decimals)", "round(math.exp(2.5), 2)",
         'decimals=2, mistakes={"ln x = c ⟺ x = e^c : on défait ln avec exp": round(math.log(2.5), 2), '
         '"x = e^c est une puissance de e, pas un produit": round(2.5 * math.e, 2), '
         '"isole ln x : retire 1, puis divise par 2": round(math.exp(3.5), 2), '
         '"divise par 2 avant d\'appliquer exp : 2 ln x + 1 = 6 donne d\'abord ln x": round(math.exp(5) / 2, 2)}'),
        ("d", "an integer", "3",
         'mistakes={"pour cette valeur, x − 1 est négatif : ln(x − 1) n\'y est pas défini": -3, '
         '"tu as trouvé x², pas x": 9, "ln a + ln b = ln(ab), pas ln(a + b)": 4}'),
        ("e", "an integer", "next(n for n in range(100) if 5 * 1.04**n > 8)",
         'fractional="un nombre de périodes entier : le premier entier qui convient, pas un arrondi", '
         'mistakes={"calcule 5 × 1,04ⁿ pour ce n : il ne dépasse pas encore 8": 11}'),
        ("f", "an integer", "next(n for n in range(100) if 0.85**n < 0.05)",
         'fractional="un nombre de périodes entier : le premier entier qui convient, pas un arrondi", '
         'mistakes={"ln 0,85 < 0 : diviser par lui change le sens de l\'inégalité ; vérifie 0,85ⁿ pour ce n": 18}'),
        ("g", "an interval, as text", '"]1 ; 2]"',
         'kind="interval", mistakes={"ln n\'est défini que pour x − 1 > 0": "]-oo ; 2]", '
         '"en x = 1, ln(x − 1) = ln 0 n\'existe pas : la borne est exclue": "[1 ; 2]", '
         '"ln(x − 1) ≤ 0 inclut l\'égalité ln(x − 1) = 0": "]1 ; 2[", '
         '"ln(x − 1) ≤ 0 ⟺ 0 < x − 1 ≤ 1 : on ajoute 1": "]0 ; 1]"}'),
        ("h", "a list in increasing order (4 decimals)", "[math.log(2), math.log(3)]",
         'decimals=4, mistakes={"X = eˣ : il reste à revenir à x, avec x = ln X": [2, 3], '
         '"X² − 5X + 6 = 0 a deux solutions positives : deux valeurs de x": [math.log(2)]}'),
    ]),
    Paper("R6.4", "Changer de base : log₂, log₁₀, ln", [
        ("a", "an integer", "9",
         'mistakes={"log₂ 512 est l\'exposant y tel que 2^y = 512, pas un quotient": 256, '
         '"vérifie : 2 puissance ta réponse doit redonner 512": 8}'),
        ("b", "an integer", "2.0",
         'decimals=3, mistakes={"une somme de logarithmes est le logarithme du produit, pas de la somme": '
         'round(math.log10(29), 3), "tu as trouvé le produit : il reste à en prendre le log₁₀": 100, '
         '"log a + log b est le logarithme du produit ab, pas le produit log a × log b": '
         'round(math.log10(25) * math.log10(4), 3)}'),
        ("c", "an integer", "3", 'mistakes={"log₆ 216 est l\'exposant y tel que 6^y = 216, pas un quotient": 36}'),
        ("d", "an integer", "-7", 'mistakes={"un nombre entre 0 et 1 a un logarithme négatif": 7}'),
        ("e", "a number (3 decimals)", "round(math.log(30) / math.log(5), 3)",
         'decimals=3, mistakes={"le logarithme de x divisé par celui de la base, pas l\'inverse": '
         'round(math.log(5) / math.log(30), 3), "divise par ln 5 : le logarithme décimal de 30 n\'est pas son '
         'logarithme en base 5": round(math.log10(30), 3), "log₅ 30 est un exposant, pas le quotient 30 / 5": 6}'),
        ("f", "a number (3 decimals)", "round(math.log2(7), 3)",
         'decimals=3, mistakes={"le logarithme de x divisé par celui de la base, pas l\'inverse": '
         'round(math.log(2) / math.log(7), 3), "le logarithme en base 2, pas en base 10": round(math.log10(7), 3)}'),
        ("g", "an integer", "len(str(2**100))",
         'mistakes={"le nombre de chiffres est la partie entière du logarithme décimal, plus 1": 30, '
         '"passe par le logarithme décimal de 2^100 (fiche §4)": 100}'),
        ("h", "a fraction, as text", "Fraction(3, 2)",
         'kind="fraction", mistakes={"le logarithme de x divisé par celui de la base, pas l\'inverse": "2/3", '
         '"log₄ 8 est un exposant y tel que 4^y = 8, pas un quotient": "2"}'),
    ]),
    Paper("R6.5", "Compter en bits et en nats : combien de questions oui ou non ?", [
        ("a", "an integer", "math.ceil(math.log2(300))",
         'mistakes={"k questions distinguent au plus 2^k nombres : il faut 2^k ≥ 300": 8, '
         '"chaque question coupe les possibilités restantes en deux": {150, 299, 300}}'),
        ("b", "a number (2 decimals)", "round(math.log2(300), 2)",
         'decimals=2, mistakes={"log₂ 300 = ln 300 / ln 2 : pas le logarithme décimal": round(math.log10(300), 2), '
         '"log₂ 300 = ln 300 / ln 2 : divise par ln 2": round(math.log(300), 2)}'),
        ("c", "a number (2 decimals)", "round(3 * math.log2(26), 2)",
         'decimals=2, mistakes={"3 lettres parmi 26 : 26 × 26 × 26 codes possibles, pas 26 × 3": '
         'round(math.log2(78), 2), "en bits : log₂, pas ln": round(3 * math.log(26), 2), '
         '"l\'information est le logarithme du nombre de codes, pas ce nombre": 26**3}'),
        ("d", "an integer", "math.ceil(50 / math.log2(26))",
         'fractional="un nombre de lettres entier : le premier entier qui convient, pas un arrondi", '
         'mistakes={"avec ce nombre de lettres, l\'information reste sous 50 bits : il faut l\'atteindre": 10}'),
        ("e", "a number (2 decimals)", "round(math.log2(52), 2)",
         'decimals=2, mistakes={"en bits : log₂ 52, pas ln 52": round(math.log(52), 2), '
         '"l\'information est log₂ 52, pas le nombre de cartes": 52}'),
        ("f", "a number (2 decimals)", "round(math.log2(52 / 12), 2)",
         'decimals=2, mistakes={"l\'information est −log₂ p, avec p la probabilité de l\'événement, pas log₂ du nombre '
         'de figures": round(math.log2(12), 2), "en bits : log₂, pas ln": round(math.log(52 / 12), 2)}'),
        ("g", "a number (4 decimals)", "round(math.exp(-3), 4)",
         'decimals=4, mistakes={"les nats utilisent ln, pas log₂": round(2**-3, 4), '
         '"il faut défaire un ln, pas un log₁₀": 0.001, "une probabilité est entre 0 et 1 : attention au signe moins '
         'de −ln p": round(math.exp(3), 4)}'),
        ("h", "a number (2 decimals)", "round(10 * math.log(2), 2)",
         'decimals=2, mistakes={"1 bit vaut moins d\'un nat : 10 bits font moins de 10 nats": round(10 / math.log(2), 2)}'),
    ]),
    Paper("R6.6", "Temps de doublement et demi-vie", [
        ("a", "a number (2 decimals)", "round(math.log(2) / math.log(1.03), 2)",
         'decimals=2, mistakes={"c\'est l\'estimation de la règle de 70 ; la question demande la valeur exacte (fiche '
         '§3)": round(70 / 3, 2), "(1,03)ⁿ = 2 : le logarithme de 1,03, pas de 0,03": '
         'round(math.log(2) / math.log(0.03), 2), "le même logarithme au numérateur et au dénominateur (ln, ou log₁₀, '
         'mais pas les deux)": round(math.log10(2) / math.log(1.03), 2)}'),
        ("b", "a number (2 decimals)", "round(70 / 3, 2)",
         'decimals=2, mistakes={"la règle de 70 : 70 divisé par le taux en pourcentage": '
         'round(math.log(2) / math.log(1.03), 2)}'),
        ("c", "a number (2 decimals)", "round(math.log(0.5) / math.log(0.9), 2)",
         'decimals=2, mistakes={"une baisse de 10 % multiplie par 0,9 chaque année, pas une hausse par 1,1": '
         'round(math.log(2) / math.log(1.1), 2), "les baisses se composent : on ne retire pas 10 % de la masse de '
         'départ chaque année": 5}'),
        ("d", "a number (4 decimals)", "round(2 ** (1 / 5), 4)",
         'decimals=4, mistakes={"en une heure, la population est multipliée par m ; en 5 heures, par m⁵, qui vaut 2": '
         '{1.4, 0.4}}'),
        ("e", "a number (2 decimals)", "round(2 ** (12 / 5), 2)",
         'decimals=2, mistakes={"12 heures ne font pas un nombre entier de périodes de 5 heures : le facteur est 2 '
         'puissance le nombre de périodes, pas 2 fois ce nombre": 4.8}'),
        ("f", "a number (2 decimals)", "round(math.log(2) / 0.04, 2)",
         'decimals=2, mistakes={"croissance continue : le temps de doublement n\'a pas la même formule qu\'avec un '
         'taux par période (fiche §3)": round(math.log(2) / math.log(1.04), 2)}'),
        ("g", "a fraction, as text", "Fraction(1, 16)",
         'kind="fraction", mistakes={"compte les demi-vies dans 24 heures : chacune divise la dose par 2": "1/4", '
         '"24 heures ÷ 6 heures : recompte les demi-vies": "1/8"}'),
    ]),
    Paper("R6.7", "La cote et le logit : d'une probabilité à un score, et retour", [
        ("a", "a number", "19.0",
         'decimals=2, mistakes={"la cote est p / (1 − p), pas (1 − p) / p": round(1 / 19, 2)}'),
        ("b", "a number (3 decimals)", "round(math.log(19), 3)",
         'decimals=3, mistakes={"le logit est le logarithme de la cote de a), pas de son inverse": '
         '-round(math.log(19), 3), "le logit utilise ln, pas log₁₀": round(math.log10(19), 3), '
         '"le logit est le logarithme de la cote, pas de p": round(math.log(0.95), 3)}'),
        ("c", "a number", "0.3",
         'decimals=2, mistakes={"3/7 est la cote ; la probabilité est le p tel que p / (1 − p) = 3/7": round(3 / 7, 2)}'),
        ("d", "a number (3 decimals)", "round(math.log(3 / 7), 3)",
         'decimals=3, mistakes={"le logit est le logarithme de la cote, pas de p": round(math.log(0.3), 3), '
         '"le logit utilise ln, pas log₁₀": round(math.log10(3 / 7), 3)}'),
        ("e", "a number (3 decimals)", "round(1 / (1 + math.exp(-1.2)), 3)",
         'decimals=3, mistakes={"σ(x) = 1 / (1 + e^(−x)) : l\'exponentielle a l\'exposant −x": '
         'round(1 / (1 + math.exp(1.2)), 3)}'),
        ("f", "a number", "-1.2",
         'decimals=2, mistakes={"1 − p a la cote inverse de celle de p : que devient son logarithme ?": 1.2, '
         '"c\'est la probabilité du contraire ; on demande son logit": round(1 / (1 + math.exp(1.2)), 2)}'),
        ("g", "a number (2 decimals)", "round(math.exp(3), 2)",
         'decimals=2, mistakes={"le logit est un ln, pas un log₁₀ : on le défait avec exp": 1000, '
         '"on demande la cote, pas la probabilité": round(1 / (1 + math.exp(-3)), 2), '
         '"le logit est le logarithme de la cote : la cote s\'obtient en défaisant ce logarithme": '
         'round(math.log(3), 2)}'),
        ("h", "a number", "0.6",
         'decimals=2, mistakes={"ajouter ln 6 au logit multiplie la cote par 6, pas la probabilité": 1.2, '
         '"1,5 est la nouvelle cote : reviens à la probabilité": 1.5}'),
    ]),
    Paper("R6.8", "Placer des valeurs sur une échelle logarithmique", [
        ("a", "a number (1 decimal)", "10.0",
         'decimals=1, mistakes={"c\'est le nombre de décades : convertis-le en centimètres": 2, '
         '"la position est proportionnelle au logarithme de la valeur, pas à la valeur": 100 * 20 / 10000}'),
        ("b", "a number (1 decimal)", "round(5 * math.log10(2000), 1)",
         'decimals=1, mistakes={"multiplie le nombre de décades par 5 cm": round(math.log10(2000), 1), '
         '"log₁₀, pas ln": round(5 * math.log(2000), 1), '
         '"la position est proportionnelle au logarithme de la valeur, pas à la valeur": 2000 * 20 / 10000}'),
        ("c", "a number (1 decimal)", "round(5 * math.log10(5), 1)",
         'decimals=1, mistakes={"multiplie le nombre de décades par 5 cm": round(math.log10(5), 1), '
         '"5 n\'est pas au milieu de la décade : l\'axe est logarithmique": 2.5}'),
        ("d", "a number (2 decimals)", "round(10**1.5, 2)",
         'decimals=2, mistakes={"1,5 est le nombre de décades : la valeur est 10 puissance ce nombre": 1.5, '
         '"convertis d\'abord les centimètres en décades (5 cm par décade)": round(10**7.5, 2)}'),
        ("e", "a number (2 decimals)", "round(10**0.6, 2)",
         'decimals=2, mistakes={"0,6 est le nombre de décades : le rapport est 10 puissance ce nombre": 0.6, '
         '"convertis d\'abord les centimètres en décades (5 cm par décade)": {1000, 3}}'),
    ]),
    Paper("R6.11", "Des produits de probabilités aux sommes de logarithmes", [
        ("a", "a number (4 decimals)", "round(math.prod(P11), 4)",
         'decimals=4, mistakes={"une vraisemblance est un produit de probabilités, pas une somme": round(sum(P11), 4)}'),
        ("b", "a number (4 decimals)", "round(sum(math.log(p) for p in P11), 4)",
         'decimals=4, mistakes={"le logarithme népérien, pas le décimal": round(sum(math.log10(p) for p in P11), 4), '
         '"le logarithme d\'une probabilité est négatif": -round(sum(math.log(p) for p in P11), 4)}'),
        ("c", "a number (4 decimals)", "round(sum(math.log(p) for p in P11) / 5, 4)",
         'decimals=4, mistakes={"une moyenne : divise la somme par le nombre d\'expériences": '
         'round(sum(math.log(p) for p in P11), 4)}'),
        ("d", "a number (4 decimals)", "round(0.7**5, 4)",
         'decimals=4, mistakes={"la vraisemblance est le produit des cinq probabilités, pas leur somme": 3.5}'),
        ("e", "1 or 2", "2",
         'choices=[1, 2], mistakes={"compare les deux vraisemblances (ou leurs logarithmes) : la plus grande gagne": 1}'),
        ("f", "a number (1 decimal)", "round(LOG_B, 1)",
         'decimals=1, mistakes={"la log-vraisemblance utilise ln, pas log₁₀": '
         'round(600 * math.log10(0.5) + 400 * math.log10(0.3), 1), '
         '"chaque groupe compte autant de fois qu\'il a de résultats : 600 fois un logarithme, 400 fois l\'autre": '
         'round(1000 * math.log(0.5 * 0.3), 1), "c\'est la log-vraisemblance du modèle A, pas celle de B": '
         'round(LOG_A, 1)}'),
        ("g", "a number (1 decimal)", "round(LOG_B - LOG_A, 1)",
         'decimals=1, mistakes={"l\'écart des log-vraisemblances népériennes, pas des log₁₀": '
         'round((LOG_B - LOG_A) / math.log(10), 1)}'),
        ("h", "a number (2 decimals)", "round((LOG_B - LOG_A) / math.log(10), 2)",
         'decimals=2, mistakes={"le log₁₀ du rapport : divise l\'écart des ln par ln 10": round(LOG_B - LOG_A, 2), '
         '"divise par ln 10, ne multiplie pas": round((LOG_B - LOG_A) * math.log(10), 2)}'),
    ]),
    Paper("R6.12", "Des logarithmes au travail : TF-IDF et PSNR", [
        ("a", "a number", "0.0", 'decimals=2, mistakes={"idf = ln(N / df) : calcule N / df, puis son logarithme": 1}'),
        ("b", "a number (3 decimals)", "round(math.log(100), 3)",
         'decimals=3, mistakes={"l\'idf utilise ln, pas log₁₀": 2, "idf = ln(N / df), pas N / df": 100}'),
        ("c", "a number (3 decimals)", "round(math.log(10), 3)",
         'decimals=3, mistakes={"l\'idf utilise ln, pas log₁₀": 1, "idf = ln(N / df), pas N / df": 10}'),
        ("d", "a list (3 decimals)", "[round(2 * math.log(100), 3), round(5 * math.log(10), 3)]",
         'decimals=3, mistakes={"le mot de b) apparaît 2 fois, celui de c) 5 fois : tf × idf pour chacun": '
         '[round(5 * math.log(100), 3), round(2 * math.log(10), 3)], '
         '"un poids tf-idf est tf × idf, pas l\'idf seul": [round(math.log(100), 3), round(math.log(10), 3)], '
         '"calcule avec les valeurs non arrondies de b) et c), pas avec leurs arrondis": '
         '[round(2 * round(math.log(100), 3), 3), round(5 * round(math.log(10), 3), 3)]}'),
        ("e", "a number", "30.0",
         'decimals=2, mistakes={"le PSNR est 10 × log₁₀ du rapport : n\'oublie pas le facteur 10": 3, '
         '"le PSNR est le logarithme du rapport, pas le rapport lui-même": 1000}'),
        ("f", "a number (2 decimals)", "round(10 * math.log10(5), 2)",
         'decimals=2, mistakes={"le PSNR a un facteur 10 devant le logarithme": round(math.log10(5), 2), '
         '"diviser la MSE par 5 multiplie le rapport par 5 : le PSNR augmente": -round(10 * math.log10(5), 2)}'),
        ("g", "a number (4 decimals)", "255**2 / 10**4",
         'decimals=4, mistakes={"défais le log₁₀ : le rapport 255² / MSE vaut 10 puissance (PSNR / 10)": '
         '255**2 / 10**3, "le PSNR a un facteur 10 devant le logarithme, pas 20": 255**2 / 10**2, '
         '"la MSE est au dénominateur du rapport : MSE = 255² / rapport": 10**4 / 255**2}'),
    ]),
]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math
from fractions import Fraction

P11 = [0.9, 0.6, 0.3, 0.8, 0.5]                              # R6.11 a to e
LOG_A = 1000 * math.log(0.4)                                 # R6.11 f to h: the log-likelihoods of A and B
LOG_B = 600 * math.log(0.5) + 400 * math.log(0.3)'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ R6.1 à R6.8, 🔗 R6.11 et R6.12)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un nombre avec un point décimal, `-1.5`, arrondi comme le demande la question ;\n"
               "- une fraction exacte entre guillemets, `\"5/7\"` ;\n"
               "- une expression entre guillemets, `\"3*x - 1\"` (`*` pour multiplier, `**` pour la puissance) ;\n"
               "- un intervalle entre guillemets, `\"[-2 ; 4[\"` (`-oo` et `+oo` pour l'infini) ;\n"
               "- une liste de nombres entre crochets ; vrai ou faux par `True` ou `False` ; un numéro de réponse "
               "proposée par un entier.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (R6.14 to R6.16)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math
import warnings

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

LOAD_LEARNER = 'mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="R6")  # reload your saved file'
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme dans les chapitres précédents). Ouvre ta copie "
         "`mon_travail/mymath/explog.py`, lis la docstring de la fonction en entier, remplace la ligne "
         "`raise NotImplementedError(...)` par ton code, **enregistre** le fichier, puis exécute les cellules "
         "ci-dessous : la première recharge ta librairie. Tu n'as droit qu'à `math.exp` et `math.log` (le logarithme "
         "népérien, avec un seul argument) : un test le vérifie. Les autres tests comparent tes résultats à "
         "`math.log2`, `math.log10`, NumPy et SciPy.")

WRONG_ERROR = "lève précisément une ValueError, le type d'erreur que demande la docstring : raise ValueError(...)"
OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "TypeError", "ZeroDivisionError"]


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of explog.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_r6_explog.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_r6_explog.py", "{keyword}", impl="ref")')]


R6_14 = Ex(
    "R6.14", "🔨", 1, 15, "Un logarithme dans n'importe quelle base · `log_base`",
    "programmer le logarithme en base quelconque avec le seul logarithme népérien, et refuser les entrées interdites.",
    "fiche §3 et §4", tracks="C, E", mymath="explog.py",
    body=HOWTO + """

Écris `log_base(x, base)` dans `mon_travail/mymath/explog.py` : le logarithme de `x` en base `base`, avec la formule de changement de base (fiche §4) et `math.log`. Une `ValueError` si `x <= 0`, si `base <= 0` ou si `base == 1` : vérifie-le **avant** de calculer.

La vérification calcule :
- a) $\\log_{5} 15\\,625$ et $\\log_{2} 0{,}001\\,953\\,125$ ;
- b) $\\log_{0{,}5} 6$ ;
- c) le nom de l'erreur levée pour $x = 0$ (avec `raised`, de la cellule des outils), puis d) pour la base 1.

Puis, dans ta copie : pourquoi la base 1 est-elle interdite ? Que donnerait la formule ?""",
    todo=LOAD_LEARNER,
    check='''with checked("R6.14a"):
    wbm.check("R6.14a", [mymath.explog.log_base(15625, 5), mymath.explog.log_base(0.001953125, 2)], computed=True)
with checked("R6.14b"):
    wbm.check("R6.14b", mymath.explog.log_base(6, 0.5), computed=True)
with checked("R6.14c"):
    wbm.check("R6.14c", raised(mymath.explog.log_base, 0, 10), computed=True)
with checked("R6.14d"):
    wbm.check("R6.14d", raised(mymath.explog.log_base, 5, 1), computed=True)''',
    solution=LOAD_REF + '''
log_base = mymath.explog.log_base
print("a)", [log_base(15625, 5), log_base(0.001953125, 2)], " b)", log_base(6, 0.5))
print("c)", raised(log_base, 0, 10), " d)", raised(log_base, 5, 1))''',
    record=f'''wbm.record("R6.14a", [6.0, -9.0], decimals=6,
           mistakes={{"log_base(x, base) = ln x / ln base, pas ln base / ln x": [1 / 6, -1 / 9]}})
wbm.record("R6.14b", math.log(6) / math.log(0.5), decimals=4,
           mistakes={{"log_base(x, base) = ln x / ln base, pas ln base / ln x": math.log(0.5) / math.log(6)}})
wbm.record("R6.14c", "ValueError",
           mistakes={{"x = 0 : lève une ValueError (raise) avant de calculer": "aucune",
                     "{WRONG_ERROR}": {errors_source()}}})
wbm.record("R6.14d", "ValueError",
           mistakes={{"base = 1 : ln 1 = 0, la formule diviserait par zéro ; teste base == 1 et lève une ValueError":
                         {{"ZeroDivisionError", "aucune"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})''',
    after=tests_cells("test_log_base_ or test_explog_uses"),
    note="Toutes les bases se ramènent à $\\ln$ : $\\log_b x = \\frac{\\ln x}{\\ln b}$. Avec la base 1, $\\ln 1 = 0$ et "
         "la formule divise par zéro : aucune puissance de 1 ne vaut autre chose que 1. Une base entre 0 et 1 est "
         "permise, et son logarithme change de signe : $\\log_{0{,}5} 6 = -\\log_2 6$.",
)

R6_15 = Ex(
    "R6.15", "🔨", 2, 20, "Sigmoïde et tanh à partir de exp · `sigmoid`, `tanh`",
    "programmer la sigmoïde et la tangente hyperbolique avec la seule exponentielle, et vérifier leurs propriétés.",
    "fiche §7 ; R6.10", tracks="C, E", mymath="explog.py",
    body="""Dans `mon_travail/mymath/explog.py` :
- `sigmoid(x)` : $\\sigma(x) = \\frac{1}{1 + e^{-x}}$, avec `math.exp` ;
- `tanh(x)` : $\\tanh x = \\frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$, avec `math.exp` (ou avec ta sigmoïde : fiche §7). `math.tanh` est interdite.

Les tests restent dans $\\lvert x \\rvert \\le 30$ (la docstring) : pas besoin de précautions pour des $x$ énormes, que workbookIA prendra au chapitre 17.

La vérification calcule :
- a) $\\sigma(0)$, $\\sigma(0{,}7)$ et $\\sigma(-0{,}7)$ ;
- b) si $\\sigma(-30) > 0$ et si $\\sigma(30) < 1$ (une liste de deux booléens) ;
- c) $\\tanh 0$, $\\tanh 0{,}75$ et $\\tanh(-2)$ ;
- d) si $\\tanh x = 2\\,\\sigma(2x) - 1$ à $10^{-12}$ près pour 101 valeurs de $x$ entre −5 et 5 ;
- e) $\\tanh 30$ et $\\tanh(-30)$.""",
    todo=LOAD_LEARNER,
    check='''with checked("R6.15a"):
    sigmoid = mymath.explog.sigmoid
    wbm.check("R6.15a", [sigmoid(0), sigmoid(0.7), sigmoid(-0.7)], computed=True)
with checked("R6.15b"):
    sigmoid = mymath.explog.sigmoid
    wbm.check("R6.15b", [bool(sigmoid(-30) > 0), bool(sigmoid(30) < 1)], computed=True)
with checked("R6.15c"):
    tanh = mymath.explog.tanh
    wbm.check("R6.15c", [tanh(0), tanh(0.75), tanh(-2)], computed=True)
with checked("R6.15d"):
    sigmoid, tanh = mymath.explog.sigmoid, mymath.explog.tanh
    wbm.check("R6.15d", all(abs(tanh(x) - (2 * sigmoid(2 * x) - 1)) < 1e-12 for x in np.linspace(-5, 5, 101)),
              computed=True)
with checked("R6.15e"):
    tanh = mymath.explog.tanh
    wbm.check("R6.15e", [tanh(30), tanh(-30)], computed=True)''',
    solution=LOAD_REF + '''
sigmoid, tanh = mymath.explog.sigmoid, mymath.explog.tanh
print("a)", [sigmoid(0), sigmoid(0.7), sigmoid(-0.7)], " b)", [sigmoid(-30) > 0, sigmoid(30) < 1])
print("c)", [tanh(0), tanh(0.75), tanh(-2)], " e)", [tanh(30), tanh(-30)])
print("d)", all(abs(tanh(x) - (2 * sigmoid(2 * x) - 1)) < 1e-12 for x in np.linspace(-5, 5, 101)))''',
    record='''wbm.record("R6.15a", [0.5, 1 / (1 + math.exp(-0.7)), 1 / (1 + math.exp(0.7))], decimals=4,
           mistakes={"σ(x) = 1 / (1 + e^(−x)) : l'exponentielle a l'exposant −x": [0.5, 1 / (1 + math.exp(0.7)),
                                                                              1 / (1 + math.exp(-0.7))]})
wbm.record("R6.15b", [True, True],
           mistakes={"σ(x) reste strictement entre 0 et 1 : 1 / (1 + e^(−x)), sans arrondi de ta part":
                         [False, True]})
wbm.record("R6.15c", [0.0, math.tanh(0.75), math.tanh(-2)], decimals=5,
           mistakes={"tanh x = 2σ(2x) − 1 : la sigmoïde de 2x, pas de x": [0.0, 2 / (1 + math.exp(-0.75)) - 1,
                                                                        2 / (1 + math.exp(2)) - 1],
                     "tanh est impaire : tanh(−2) est négatif": [0.0, math.tanh(0.75), -math.tanh(-2)]})
wbm.record("R6.15d", True,
           mistakes={"ta tanh ne coïncide pas avec 2σ(2x) − 1 : écrite avec ta sigmoïde, relis son argument (2x, pas x) ; "
                     "écrite avec exp, vérifie chaque exponentielle de la formule": False})
wbm.record("R6.15e", [1.0, -1.0], decimals=6,
           mistakes={"le signe de ta tanh est inversé : vérifie l'ordre de la soustraction du numérateur": [-1.0, 1.0]})''',
    after=tests_cells("test_sigmoid_ or test_tanh_ or test_explog_uses"),
    note="Avec la sigmoïde déjà écrite, `tanh` tient en une ligne : `2 * sigmoid(2 * x) - 1`. La formule "
         "$\\frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$ marche aussi pour $\\lvert x \\rvert \\le 30$ ; pour $x = 1\\,000$, "
         "elle calculerait $e^{1000}$, trop grand pour un flottant : c'est le problème que workbookIA règle au "
         "chapitre 17.",
)

R6_16 = Ex(
    "R6.16", "🔨", 1, 15, "Temps de doublement · `doubling_time`",
    "programmer le temps de doublement d'une croissance à taux constant, et le comparer à la règle de 70.",
    "fiche §1 et §3 ; R6.6", tracks="C", mymath="explog.py",
    body="""Écris `doubling_time(rate)` : le nombre **réel** $n$ de périodes tel que $(1 + \\text{rate})^n = 2$ (fiche §3), sans l'arrondir. Une `ValueError` si `rate <= 0` (une grandeur qui ne grandit pas ne double jamais).

La vérification calcule :
- a) les temps de doublement à +7 % et à +25 % par période ;
- b) le nom de l'erreur levée pour un taux nul ;
- c) les temps de doublement à +1 %, +10 % et +50 %.

Puis, dans ta copie : compare les réponses de c) à la règle de 70 ($\\frac{70}{\\text{taux en \\%}}$). Pour quels taux la règle est-elle bonne, et pourquoi (fiche §3) ?""",
    todo=LOAD_LEARNER,
    check='''with checked("R6.16a"):
    wbm.check("R6.16a", [mymath.explog.doubling_time(0.07), mymath.explog.doubling_time(0.25)], computed=True)
with checked("R6.16b"):
    wbm.check("R6.16b", raised(mymath.explog.doubling_time, 0), computed=True)
with checked("R6.16c"):
    wbm.check("R6.16c", [mymath.explog.doubling_time(r) for r in (0.01, 0.1, 0.5)], computed=True)''',
    solution=LOAD_REF + '''
doubling_time = mymath.explog.doubling_time
print("a)", [doubling_time(0.07), doubling_time(0.25)], " b)", raised(doubling_time, 0))
for r in (0.01, 0.1, 0.5):
    print(f"c) +{r:.0%} : {doubling_time(r):.2f} périodes, règle de 70 : {70 / (100 * r):.2f}")''',
    record=f'''wbm.record("R6.16a", [math.log(2) / math.log(1.07), math.log(2) / math.log(1.25)], decimals=4,
           mistakes={{"(1 + r)ⁿ = 2 : le logarithme de 1 + r, pas de r": [math.log(2) / 0.07, math.log(2) / 0.25],
                     "le nombre réel de périodes, sans l'arrondir": [11, 4]}})
wbm.record("R6.16b", "ValueError",
           mistakes={{"rate = 0 : ln 1 = 0, on diviserait par zéro ; teste rate <= 0 et lève une ValueError":
                         {{"ZeroDivisionError", "aucune"}},
                     "{WRONG_ERROR}": {errors_source("ZeroDivisionError")}}})
wbm.record("R6.16c", [math.log(2) / math.log(1 + r) for r in (0.01, 0.1, 0.5)], decimals=4,
           mistakes={{"(1 + r)ⁿ = 2 : le logarithme de 1 + r, pas de r": [math.log(2) / r for r in (0.01, 0.1, 0.5)]}})''',
    after=tests_cells("test_doubling_time_ or test_explog_uses"),
    note="La règle de 70 remplace $\\ln(1 + r)$ par $r$ et $\\ln 2 \\approx 0{,}693$ par 0,70 : très bonne à 1 % "
         "(70 contre 69,66), correcte à 10 % (7 contre 7,27), fausse à 50 % (1,4 contre 1,71), car $\\ln(1 + r) "
         "\\approx r$ n'est vrai que pour un petit $r$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: NumPy, prediction, experiments (R6.17 to R6.20)
# ---------------------------------------------------------------------------
R6_17 = Ex(
    "R6.17", "📦", 1, 15, "Sur tout un tableau : `np.exp`, `np.log2` et `scipy.special.expit`",
    "appliquer exp, les logarithmes et la sigmoïde à tout un tableau d'un coup, et fabriquer une grille logarithmique.",
    "fiche §4, §6 et §7 ; workbookIA 0A §100.8.3 (calcul vectorisé)", tracks="C",
    body="""NumPy applique une fonction à chaque élément d'un tableau, sans boucle (0A §100.8.3) : `np.exp`, `np.log` (le logarithme népérien), `np.log2`, `np.log10`, `np.floor` (la partie entière, vers le bas) ; `scipy.special.expit` est la sigmoïde de SciPy. Et `np.logspace(a, b, n)` fabrique $n$ valeurs de $10^a$ à $10^b$, également espacées **sur une échelle logarithmique** (fiche §6). Calcule, chacun **en une ligne** :
- a) $\\log_{2}$ de chaque nombre de `values_a` ;
- b) le nombre de chiffres de chaque entier de `values_b` (fiche §4) ;
- c) la sigmoïde de chaque nombre de `values_c` ;
- d) cinq valeurs de $10^{-4}$ à $10^{0}$, également espacées sur une échelle logarithmique.""",
    todo='''from scipy.special import expit

values_a = np.array([0.25, 2, 2048])
values_b = np.array([7, 4321, 1000000])
values_c = np.array([-2.5, 0, 2.5])

answer_R6_17a = ...  # a) an array of 3 numbers
answer_R6_17b = ...  # b) an array of 3 numbers of digits
answer_R6_17c = ...  # c) an array of 3 numbers
answer_R6_17d = ...  # d) an array of 5 numbers''',
    check='''for letter, answer in zip("abcd", [answer_R6_17a, answer_R6_17b, answer_R6_17c, answer_R6_17d]):
    wbm.check(f"R6.17{letter}", answer)''',
    solution='''from scipy.special import expit

values_a = np.array([0.25, 2, 2048])
values_b = np.array([7, 4321, 1000000])
values_c = np.array([-2.5, 0, 2.5])

answer_R6_17a = np.log2(values_a)
answer_R6_17b = np.floor(np.log10(values_b)) + 1
answer_R6_17c = expit(values_c)
answer_R6_17d = np.logspace(-4, 0, 5)
print(answer_R6_17a, answer_R6_17b, answer_R6_17c.round(4), answer_R6_17d, sep="\\n")''',
    record='''wbm.record("R6.17a", [-2.0, 1.0, 11.0], decimals=6,
           mistakes={"log₂ : np.log2, pas np.log (le logarithme népérien)": [math.log(0.25), math.log(2), math.log(2048)]})
wbm.record("R6.17b", [1.0, 4.0, 7.0], decimals=6,
           mistakes={"un entier de d chiffres a un log₁₀ entre d − 1 et d : la partie entière, plus 1": [0.0, 3.0, 6.0],
                     "le nombre de chiffres est un entier : la partie entière de log₁₀, plus 1":
                         [math.log10(7), math.log10(4321), 6.0]})
wbm.record("R6.17c", [1 / (1 + math.exp(2.5)), 0.5, 1 / (1 + math.exp(-2.5))], decimals=4)
wbm.record("R6.17d", [1e-4, 1e-3, 1e-2, 1e-1, 1.0], decimals=6,
           mistakes={"np.logspace(a, b, n) : des exposants également espacés, de 10^a à 10^b":
                         [1e-4, 0.250075, 0.50005, 0.750025, 1.0]})''',
    note="`np.floor(np.log10(n)) + 1` compte les chiffres sans transformer le nombre en texte. Et la grille de d) est "
         "celle qu'on essaie quand on ignore jusqu'à l'ordre de grandeur d'un réglage : $10^{-4}, 10^{-3}, \\dots, 1$.",
)

R6_18_EXPERIMENT = '''def outcome(compute):
    """What compute() gives: its value, the name of the error it raises, and the warnings it emits."""
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            value = compute()
        except Exception as exc:  # noqa: BLE001 - the error is part of the answer
            value = f"erreur {type(exc).__name__} : {exc}"
    alerts = "; ".join(f"{type(w.message).__name__} : {w.message}" for w in caught)
    return value, alerts or "aucune alerte"


for label, compute in [("a) math.exp(800)", lambda: math.exp(800)),
                       ("b) np.exp(800.0)", lambda: np.exp(800.0)),
                       ("c) math.exp(-800)", lambda: math.exp(-800)),
                       ("d) np.exp(-800.0)", lambda: np.exp(-800.0))]:
    value, alerts = outcome(compute)
    print(f"{label:20} -> {value}   [{alerts}]")'''

R6_18 = Ex(
    "R6.18", "🔮", 2, 15, "Prédire : exp(800) et exp(−800), avec math et avec NumPy",
    "prévoir ce que font Python et NumPy d'un nombre trop grand ou trop petit pour un flottant.",
    "fiche §5", tracks="C, E", hypothesis=True,
    body="""$e^{800}$ dépasse de loin le plus grand `float64` (≈ $1{,}8 \\times 10^{308}$, fiche §5), et $e^{-800}$ est bien plus petit que le plus petit flottant positif. Que font alors Python et NumPy ? **Avant d'exécuter quoi que ce soit**, prédis, pour chaque calcul, le numéro de ce qu'il donne :
- a) `math.exp(800)` : 1 un nombre fini immense ; 2 la valeur spéciale `inf` (l'infini des flottants) ; 3 une erreur qui arrête le calcul ;
- b) `np.exp(800.0)` : 1, 2 ou 3, comme en a) ;
- c) `math.exp(-800)` : 1 un tout petit nombre positif ; 2 exactement `0.0` ; 3 une erreur qui arrête le calcul ;
- d) `np.exp(-800.0)` : 1 un tout petit nombre positif ; 2 exactement `0.0`, avec une alerte ; 3 exactement `0.0`, sans aucune alerte.

Écris tes quatre prédictions, vérifie-les, puis lance l'expérience : elle affiche chaque résultat, ou l'erreur levée, et les alertes émises.""",
    todo='''prediction_R6_18a = ...  # a) 1, 2 or 3, written BEFORE running the experiment below
prediction_R6_18b = ...  # b) 1, 2 or 3
prediction_R6_18c = ...  # c) 1, 2 or 3
prediction_R6_18d = ...  # d) 1, 2 or 3''',
    check='''for letter, prediction in zip("abcd", [prediction_R6_18a, prediction_R6_18b, prediction_R6_18c,
                                          prediction_R6_18d]):
    wbm.check(f"R6.18{letter}", prediction)''',
    record='''wbm.record("R6.18a", 3, prediction=True, choices=[1, 2, 3])
wbm.record("R6.18b", 2, prediction=True, choices=[1, 2, 3])
wbm.record("R6.18c", 2, prediction=True, choices=[1, 2, 3])
wbm.record("R6.18d", 3, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(R6_18_EXPERIMENT, ["prediction_R6_18a", "prediction_R6_18b", "prediction_R6_18c",
                                            "prediction_R6_18d"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", R6_18_EXPERIMENT),
        ("md", "**Après l'expérience**, dans ta copie : laquelle des quatre sorties est la plus dangereuse au milieu "
               "d'un long calcul, et pourquoi ? Que deviendrait le `0.0` de c) si le calcul en prenait ensuite le "
               "logarithme avec `math.log` (fiche §3) ?"),
    ],
    note="`math.exp(800)` lève `OverflowError` ; `np.exp(800.0)` renvoie `inf` avec une alerte (`RuntimeWarning`), "
         "et le calcul continue. Dans l'autre sens, `math.exp(-800)` et `np.exp(-800.0)` renvoient exactement `0.0`, "
         "sans erreur ni alerte : un nombre trop petit est arrondi à 0 en silence. C'est le plus dangereux : ce 0 "
         "n'en est pas un, et il fera plus loin un $\\ln 0$ (`ValueError` avec `math.log`) ou une division par 0.",
)

R6_19_GIVEN = '''n = np.arange(2, 1001)                                  # the integers 2, 3, …, 1000
t = np.arange(2, 101)                                   # values of ln x, from 2 to 100'''

R6_19_PLOT = '''with checked("R6.19 figure"):
    if gap is ... or race is ...:
        print("⏳ Écris d'abord gap et race.")
    else:
        fig, axes = plt.subplots(1, 2, figsize=(12, 3.8))
        axes[0].plot(n, np.asarray(gap) / math.log(10), color="C0")
        axes[0].axhline(0, color="gray", linewidth=0.8)
        axes[0].set_xlabel("n")
        axes[0].set_title("log₁₀(2ⁿ / n¹⁰) : négatif, puis positif pour toujours")
        axes[1].plot(t, race, color="C1")
        axes[1].axhline(0, color="gray", linewidth=0.8)
        axes[1].set_xlabel("t = ln x")
        axes[1].set_title("ln(x^0,1) − ln(ln x) = 0,1 t − ln t")
        for ax in axes:
            ax.grid(True, alpha=0.3)
        fig.tight_layout()
        plt.show()'''

R6_19 = Ex(
    "R6.19", "🔬", 2, 20, "Croissances comparées : x¹⁰, 2ˣ et ln x de plus en plus loin",
    "comparer des fonctions trop grandes pour un flottant en comparant leurs logarithmes, et voir où une croissance "
    "en dépasse une autre.",
    "fiche §3 et §5 ; R6.18", tracks="C",
    body="""$2^{1000}$ et $1000^{10}$ sont des nombres énormes, mais on peut les comparer **par leurs logarithmes**, qui restent petits (fiche §5) : $\\ln(2^{n}) = n \\ln 2$ et $\\ln(n^{10}) = 10 \\ln n$.

1. Calcule `gap`, le tableau des $\\ln \\frac{2^{n}}{n^{10}} = n \\ln 2 - 10 \\ln n$ pour chaque entier $n$ de `n` (de 2 à 1 000), en une ligne de NumPy. Puis :
   - a) combien d'entiers $n$ de 2 à 1 000 vérifient $2^{n} \\le n^{10}$ ?
   - b) le plus petit entier $n$ à partir duquel $2^{n} > n^{10}$ pour tous les entiers suivants jusqu'à 1 000 ;
   - c) de combien d'ordres de grandeur $2^{1000}$ dépasse-t-il $1000^{10}$ ? (le $\\log_{10}$ du rapport, 2 décimales)
2. Compare maintenant $x^{0{,}1}$ et $\\ln x$, avec $t = \\ln x$ : $\\ln(x^{0{,}1}) = 0{,}1\\,t$ et $\\ln(\\ln x) = \\ln t$. Calcule `race`, le tableau des $0{,}1\\,t - \\ln t$ pour chaque $t$ de `t` (de 2 à 100). Puis :
   - d) le plus petit entier $t$ à partir duquel $x^{0{,}1} > \\ln x$, c'est-à-dire $0{,}1\\,t > \\ln t$ ;
   - e) le plus petit entier $k$ tel que $\\ln k > 15$ (pense à $e^{15}$).

Dans ta copie : à partir de quel ordre de grandeur de $x$ la puissance $x^{0{,}1}$ dépasse-t-elle enfin $\\ln x$ ? Qu'en conclus-tu sur « finit par » ?""",
    given=R6_19_GIVEN,
    todo='''gap = ...            # 1. an array: n ln 2 − 10 ln n, for each n of n
race = ...           # 2. an array: 0.1 t − ln t, for each t of t
answer_R6_19a = ...  # a) an integer
answer_R6_19b = ...  # b) an integer
answer_R6_19c = ...  # c) a number (2 decimals)
answer_R6_19d = ...  # d) an integer
answer_R6_19e = ...  # e) an integer''',
    check='''for letter, answer in zip("abcde", [answer_R6_19a, answer_R6_19b, answer_R6_19c, answer_R6_19d,
                                       answer_R6_19e]):
    wbm.check(f"R6.19{letter}", answer)''',
    solution='''gap = n * math.log(2) - 10 * np.log(n)
race = 0.1 * t - np.log(t)
answer_R6_19a = int((gap <= 0).sum())
answer_R6_19b = int(n[np.nonzero(gap <= 0)[0][-1] + 1])
answer_R6_19c = round(float(gap[-1] / math.log(10)), 2)
answer_R6_19d = int(t[np.nonzero(race <= 0)[0][-1] + 1])
answer_R6_19e = math.floor(math.exp(15)) + 1
print(answer_R6_19a, answer_R6_19b, answer_R6_19c, answer_R6_19d, answer_R6_19e)''',
    record='''wbm.record("R6.19a", 57,
           mistakes={"compte tous les entiers de 2 à 1 000 où gap est négatif ou nul, n = 2 compris": {56, 58},
                     "compte les n où 2ⁿ est le plus petit, pas ceux où il est le plus grand": 942})
wbm.record("R6.19b", 59,
           mistakes={"c'est le dernier n où 2ⁿ ≤ n¹⁰ ; on demande le premier à partir duquel 2ⁿ reste devant": 58,
                     "c'est une position dans le tableau n (ou le compte de a), pas une valeur de n : lis n à cette "
                     "position": 57,
                     "le plus petit n à partir duquel 2ⁿ reste devant, pas le premier n où il passe devant : regarde "
                     "les petites valeurs de n": 2})
wbm.record("R6.19c", 1000 * math.log10(2) - 30, decimals=2,
           mistakes={"le log₁₀ du rapport : divise l'écart des ln par ln 10": 1000 * math.log(2) - 10 * math.log(1000)})
wbm.record("R6.19d", 36,
           mistakes={"le premier t à partir duquel 0,1 t > ln t pour tous les t suivants : regarde le signe de race "
                     "juste avant et juste après ta réponse": {35, 37},
                     "c'est une position dans le tableau t, pas une valeur de t : lis t à cette position": 34,
                     "le premier t à partir duquel 0,1 t reste devant ; pour les petits t, ln t est devant": 2})
wbm.record("R6.19e", math.floor(math.exp(15)) + 1,
           mistakes={"ln k > 15 ⟺ k > e^15 : le premier entier strictement plus grand": math.floor(math.exp(15)),
                     "ln k > 15 ⟺ k > e^15, pas 10^15": 10**15 + 1})''',
    after=[("md", "**La figure** : les deux écarts, en fonction de $n$ et de $t$."), ("code", R6_19_PLOT)],
    note="$2^{n}$ passe devant $n^{10}$ pour de bon à $n = 59$, puis l'écart explose : à $n = 1\\,000$, $2^{n}$ est "
         "$10^{271}$ fois plus grand. $x^{0{,}1}$ ne dépasse $\\ln x$ qu'à partir de $\\ln x = 36$, soit "
         "$x = e^{36} \\approx 4 \\times 10^{15}$ : « finit par » peut vouloir dire « très loin ».",
)

R6_20_CHECK = '''with checked("R6.20 vérifications"):
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
    try:
        created = drawn(plot_scales, axes, steps, counts)
    finally:
        plt.close(fig)                                     # only the checks below are shown here
    problems = []
    if created:
        problems.append("ta fonction ouvre sa propre figure : dessine dans les axes reçus (axes[0].plot, …)")
    else:
        for k, ax in enumerate(axes):
            ys = []
            for line in ax.lines:
                ys += list(np.asarray(line.get_ydata(), dtype=float))
            for collection in ax.collections:
                ys += list(np.asarray(collection.get_offsets(), dtype=float)[:, 1])
            if not ys:
                problems.append(f"rien n'est tracé dans axes[{k}] (dessine les données avec axes[{k}].plot(...), pas "
                                f"plt.plot)")
            elif not any(np.isclose(y, counts[-1]) for y in ys):
                problems.append(f"axes[{k}] ne montre pas les comptages eux-mêmes : trace counts tel quel (c'est "
                                f"l'axe qui devient logarithmique, pas les données)")
        if axes[0].get_yscale() != "linear":
            problems.append("axes[0] doit garder l'échelle linéaire")
        if axes[1].get_yscale() != "log":
            problems.append("l'axe vertical de axes[1] en échelle logarithmique (axes[1].set_yscale(\\"log\\"))")
        if not all(ax.get_title() for ax in axes):
            problems.append("un titre pour chaque graphique (ax.set_title)")
    if problems:
        print("❌ Ex R6.20 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex R6.20 : deux graphiques, l'un en échelle linéaire, l'autre en échelle logarithmique.")'''

R6_20 = Ex(
    "R6.20", "🎨", 1, 15, "Les mêmes données en échelle linéaire et en échelle logarithmique",
    "tracer les mêmes données sur deux échelles, et lire une croissance exponentielle sur un graphique "
    "semi-logarithmique.",
    "fiche §6 ; R0 (matplotlib)", tracks="C, E",
    body="""Un comptage double à peu près tous les 1,5 pas : `counts` contient $12 \\times 1{,}6^{t}$ pour $t = 0$ à 15 (`steps`). Complète `plot_scales(axes, steps, counts)`, qui reçoit **deux axes** côte à côte :
- dans `axes[0]`, les points `(steps, counts)` en échelle ordinaire ;
- dans `axes[1]`, les mêmes points, avec l'axe vertical en échelle logarithmique (`axes[1].set_yscale("log")`, fiche §6) ;
- un titre pour chacun, et des points plutôt qu'une ligne (`"o"`).

La cellule de vérification crée les axes, puis la figure s'affiche. Puis, en lisant le graphique de droite **et** en le justifiant par le calcul :
- a) de combien de décades la droite monte-t-elle à chaque pas ? ($\\log_{10} 1{,}6$, 3 décimales)
- b) combien de pas faut-il pour monter d'une décade, c'est-à-dire multiplier le comptage par 10 ? (2 décimales)

Dans ta copie : sur lequel des deux graphiques vois-tu le mieux les premières valeurs ? Et si la croissance ralentissait à la fin, à quoi le verrais-tu sur le graphique de droite ?""",
    given='''steps = np.arange(0, 16)
counts = 12 * 1.6**steps''',
    todo='''def plot_scales(axes, steps, counts):
    """axes[0]: the points (steps, counts) on a linear scale; axes[1]: the same points with a log y axis. Titles."""
    raise NotImplementedError("trace les deux graphiques dans axes[0] et axes[1]")


answer_R6_20a = ...  # a) a number (3 decimals)
answer_R6_20b = ...  # b) a number (2 decimals)''',
    check='''with checked("R6.20 figure"):
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
    try:
        created = drawn(plot_scales, axes, steps, counts)
    except BaseException:
        plt.close(fig)                                     # no empty figure while plot_scales is not written yet
        raise
    if created:
        plt.close(fig)
        print("❌ Ex R6.20 : ta fonction ouvre sa propre figure (plt.figure ou plt.subplots) : dessine dans les axes "
              "qu'elle reçoit, avec axes[0].plot(...) et axes[1].plot(...).")
    else:
        fig.tight_layout()
        plt.show()
for letter, answer in zip("ab", [answer_R6_20a, answer_R6_20b]):
    wbm.check(f"R6.20{letter}", answer)''',
    solution='''def plot_scales(axes, steps, counts):
    """axes[0]: the points (steps, counts) on a linear scale; axes[1]: the same points with a log y axis. Titles."""
    for ax, scale, title in zip(axes, ("linear", "log"), ("Échelle linéaire", "Échelle logarithmique")):
        ax.plot(steps, counts, "o", markersize=4)
        ax.set_yscale(scale)
        ax.set_title(title)
        ax.set_xlabel("pas t")
        ax.grid(True, which="both" if scale == "log" else "major", alpha=0.3)


fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
plot_scales(axes, steps, counts)
fig.tight_layout()
plt.show()
answer_R6_20a = round(math.log10(1.6), 3)
answer_R6_20b = round(1 / math.log10(1.6), 2)''',
    record='''wbm.record("R6.20a", math.log10(1.6), decimals=3,
           mistakes={"sur un axe en base 10, la pente est log₁₀ 1,6, pas ln 1,6": math.log(1.6),
                     "la pente en décades par pas est log₁₀ du facteur 1,6, pas le facteur lui-même": 1.6})
wbm.record("R6.20b", 1 / math.log10(1.6), decimals=2,
           mistakes={"une décade divisée par la pente : 1 / log₁₀ 1,6": math.log10(1.6),
                     "1 / log₁₀ 1,6, pas 1 / ln 1,6": 1 / math.log(1.6)})''',
    after=[("md", "**Vérifications automatiques** (la figure elle-même se juge à l'œil)."), ("code", R6_20_CHECK)],
    note="Sur le graphique de droite, les points sont alignés : la pente vaut $\\log_{10} 1{,}6 \\approx 0{,}204$ "
         "décade par pas, soit une décade tous les 4,9 pas environ ($1{,}6^{4{,}9} \\approx 10$). Un ralentissement "
         "à la fin se verrait comme des points qui passent sous la droite.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: bugs, and the documentation (R6.21, R6.22)
# ---------------------------------------------------------------------------
R6_21_BUGGY = '''def total_log_prob(probabilities):
    """ln of the product of independent probabilities, computed as a sum of logarithms."""
    total = 1                                                     # (A)
    for p in probabilities:                                       # (B)
        total = total + math.log(p)                               # (C)
    return total                                                  # (D)


def log_of_sum(a, b):
    """ln(a + b), for a > 0 and b > 0."""
    return math.log(a) + math.log(b)                              # (E)


def grow(start, rate, t1, t2):
    """start × e^(rate × t1), then that value × e^(rate × t2): the value after t1 + t2 of continuous growth."""
    return start * (math.exp(rate * t1) + math.exp(rate * t2))    # (F)'''

R6_21_FIXED = '''def total_log_prob(probabilities):
    """ln of the product of independent probabilities, computed as a sum of logarithms."""
    total = 0                                                     # (A) corrected: a sum starts at 0
    for p in probabilities:                                       # (B)
        total = total + math.log(p)                               # (C)
    return total                                                  # (D)


def log_of_sum(a, b):
    """ln(a + b), for a > 0 and b > 0."""
    return math.log(a + b)                                        # (E) corrected: ln(a + b) does not split


def grow(start, rate, t1, t2):
    """start × e^(rate × t1), then that value × e^(rate × t2): the value after t1 + t2 of continuous growth."""
    return start * math.exp(rate * t1) * math.exp(rate * t2)      # (F) corrected: a product of exponentials'''

R6_21_MISTAKES = bug_letters_mistakes(
    "AEF", "BCD",
    {"A": "calcule total_log_prob([1.0]) à la main : ln 1 = 0, que doit rendre la fonction ?",
     "E": "essaie a = b = 1 : que vaut ln(1 + 1), et que rend la ligne ?",
     "F": "e^(u + v) est un produit d'exponentielles : relis la règle e^(u + v) = …"})

R6_21 = Ex(
    "R6.21", "🐛", 2, 15, "Chasse à l'erreur : ln(a + b), e^(a + b) et log(0)",
    "repérer les règles de exp et de ln mal appliquées dans du code, et ce que donne le logarithme de 0.",
    "fiche §2 et §3", tracks="C, E",
    body="""Trois petites fonctions utilisent exp et ln. Certaines lignes sont fausses. **Sans rien exécuter d'abord**, trouve-les.

```python
""" + R6_21_BUGGY + """
```

- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) même une fois corrigée, `total_log_prob([0.5, 0.0])` ne rend pas de nombre : quel est le nom de l'erreur levée ? (`math.log` de 0 ; fiche §3)

Puis corrige les trois fonctions dans la cellule ci-dessous (elle contient le code fautif) : la vérification calcule c), la liste `[total_log_prob([0.5, 0.4]), log_of_sum(2, 3), grow(100, 0.05, 4, 6)]`.

Dans ta copie : une probabilité nulle dans un produit le rend nul. Que devient sa log-probabilité, et pourquoi un modèle qui donne la probabilité 0 à ce qui arrive vraiment est-il infiniment mauvais ?""",
    todo='''answer_R6_21a = ...  # a) letters, as text
answer_R6_21b = ...  # b) the name of an error, as text


# correct the three functions below
''' + R6_21_BUGGY,
    check='''for letter, answer in zip("ab", [answer_R6_21a, answer_R6_21b]):
    wbm.check(f"R6.21{letter}", answer)
if answer_R6_21a is ...:
    print("⏳ Ex R6.21c : trouve d'abord les lignes fausses (a), puis corrige les trois fonctions.")
else:
    with checked("R6.21c"):
        wbm.check("R6.21c", [total_log_prob([0.5, 0.4]), log_of_sum(2, 3), grow(100, 0.05, 4, 6)], computed=True)''',
    solution='''answer_R6_21a = "AEF"
answer_R6_21b = raised(lambda: sum(math.log(p) for p in [0.5, 0.0]))

''' + R6_21_FIXED + '''


print(answer_R6_21a, answer_R6_21b, [total_log_prob([0.5, 0.4]), log_of_sum(2, 3), grow(100, 0.05, 4, 6)])''',
    record=f'''wbm.record("R6.21a", "AEF",
           mistakes={R6_21_MISTAKES})
wbm.record("R6.21b", "ValueError",
           mistakes={{"math.log(0) ne renvoie pas -inf (c'est NumPy qui le fait) : il lève une erreur ; lis son nom":
                         {{"aucune", "-inf", "nan"}},
                     "juste le nom de l'erreur, avant les deux-points": "ValueError: math domain error",
                     "le nom exact de l'erreur que lève math.log(0) : exécute-le pour le voir":
                         {{"ZeroDivisionError", "OverflowError", "MathError", "ArithmeticError"}}}})
wbm.record("R6.21c", [math.log(0.2), math.log(5), 100 * math.exp(0.5)], decimals=4,
           mistakes={{"total_log_prob : une somme de logarithmes part de 0": [1 + math.log(0.2), math.log(5),
                                                                             100 * math.exp(0.5)],
                     "log_of_sum : ln(a + b) se calcule tel quel, il ne se découpe pas": [math.log(0.2), math.log(6),
                                                                                          100 * math.exp(0.5)],
                     "grow : e^(u + v) = e^u × e^v, un produit": [math.log(0.2), math.log(5),
                                                                 100 * (math.exp(0.2) + math.exp(0.3))],
                     "aucune des trois fonctions n'est encore corrigée : corrige-les dans la cellule où tu as écrit a) "
                     "et b)": [1 + math.log(0.2), math.log(6), 100 * (math.exp(0.2) + math.exp(0.3))]}})''',
    note="(A) une somme part de 0, pas de 1 (c'est un produit qui part de 1). (E) $\\ln(a + b)$ ne se découpe pas : "
         "c'est $\\ln(ab)$ qui vaut $\\ln a + \\ln b$. (F) $e^{u + v} = e^{u} \\times e^{v}$, un produit. Et "
         "`math.log(0)` lève `ValueError` (*math domain error*) : la log-probabilité d'un événement impossible vaut "
         "$-\\infty$, et NumPy la renvoie telle quelle (`-inf`).",
)

R6_22_TODO = '''# 1. The documentation of np.log1p: its first lines, then its Notes (help(np.log1p) shows the full text)
doc = np.log1p.__doc__
print(doc[:doc.find("Parameters")].strip())
print("...")
print(doc[doc.find("Notes"):doc.find("Logarithm is a multivalued")].strip())

# 2. Your experiments: np.log(1 + 1e-12) against np.log1p(1e-12); np.log2(32.0) and np.log10(1e-5);
#    np.log(0.0) and np.log(-1.0) (inside `with np.errstate(all="ignore"):` to silence the alerts)
'''

R6_22_SOLUTION = R6_22_TODO + '''print("np.log(1 + 1e-12) =", np.log(1 + 1e-12), "  np.log1p(1e-12) =", np.log1p(1e-12))
print("np.log2(32.0) =", np.log2(32.0), "  np.log10(1e-5) =", np.log10(1e-5))
with np.errstate(all="ignore"):
    print("np.log(0.0) =", np.log(0.0), "  np.log(-1.0) =", np.log(-1.0))'''

R6_22 = Ex(
    "R6.22", "🛠️", 1, 15, "Lire la documentation de `numpy.log`, `log2`, `log10`, `log1p`",
    "lire la documentation d'une fonction de NumPy pour savoir ce qu'elle calcule, sur quelles entrées, et pourquoi "
    "une variante existe.",
    "fiche §3 et §4", tracks="C",
    body="""Une documentation dit ce qu'une fonction calcule, ce qu'elle rend pour les entrées interdites et à quoi servent ses variantes. Lis celle de `np.log1p` (la cellule en affiche le début et la note sur la précision ; `help(np.log1p)` ou la [page en ligne](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html) donnent tout), puis celles de `np.log`, `np.log2` et `np.log10`. Complète la cellule avec tes expériences.

Dans ta copie :
1. Que calcule `np.log1p(x)` ? Pour quels $x$ est-il plus précis que `np.log(1 + x)`, et pourquoi (pense à ce que devient `1 + 1e-12` en flottant, R1) ?
2. Que rendent `np.log(0.0)` et `np.log(-1.0)` ? Et `math.log` dans les mêmes cas (R6.21) ? Lequel des deux comportements préfères-tu pour détecter une erreur, et lequel pour calculer sur tout un tableau ?
3. Quelle fonction de NumPy calcule $\\log_{2}$, laquelle $\\log_{10}$, et laquelle $\\ln$ ? Et `np.log` accepte-t-il une base en second argument, comme `math.log` ?""",
    after=[("todo", R6_22_TODO), ("solution", R6_22_SOLUTION)],
    note="`np.log1p(x)` calcule $\\ln(1 + x)$ sans former `1 + x`, qui perd presque tous les chiffres de `x` quand "
         "`x` est minuscule : `np.log(1 + 1e-12)` est faux dès le cinquième chiffre, `np.log1p(1e-12)` est exact. "
         "`np.log(0.0)` rend `-inf` et `np.log(-1.0)` rend `nan`, avec une alerte : pratique sur un tableau, mais à "
         "surveiller. `np.log` n'a pas d'argument de base : c'est le second argument de `math.log` seul qui en a un.",
)


PART_A = Part("A", "Ta librairie : logarithmes, sigmoïde, tanh, doublement",
              "Fiche §1, §3, §4 et §7. Les quatre fonctions de `mymath/explog.py`.",
              given=TOOLS, exercises=[R6_14, R6_15, R6_16])

PART_B = Part("B", "NumPy, une prédiction et des expériences",
              "Fiche §3 à §7. Les mêmes fonctions sur tout un tableau, ce que font Python et NumPy d'un nombre trop "
              "grand ou trop petit, des croissances comparées par leurs logarithmes, puis deux échelles en image.",
              exercises=[R6_17, R6_18, R6_19, R6_20])

PART_C = Part("C", "Erreurs de règles et documentation",
              "Fiche §2 à §4. Trois règles mal appliquées à trouver, puis la documentation des logarithmes de NumPy.",
              exercises=[R6_21, R6_22])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | R6.1 à R6.8, R6.11, R6.12 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# R6 · Exponentielle et logarithmes — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/r6_exp_log/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py R6`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# R6 · Exponentielle et logarithmes — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : propriétés de exp et de ln, équations, changements de "
               "base, bits et nats, doublements, sigmoïde et logit, échelles logarithmiques, log-probabilités.\n"
               "- Écrire les quatre fonctions de `mymath/explog.py` et les tester.\n"
               "- Calculer sur des tableaux avec NumPy, comparer des croissances par leurs logarithmes, tracer une "
               "échelle logarithmique, chasser des règles mal appliquées et lire une documentation.\n\n"
               "**Rappel express.** $e^{a+b} = e^a e^b$, $(e^a)^b = e^{ab}$, $e^x > 0$. $\\ln$ est la réciproque de "
               "exp : $\\ln(e^y) = y$, $e^{\\ln x} = x$ pour $x > 0$. $\\ln(ab) = \\ln a + \\ln b$, "
               "$\\ln(a^k) = k \\ln a$ ; $\\ln(a + b)$ ne se simplifie pas. $\\log_b x = \\frac{\\ln x}{\\ln b}$. "
               "$\\sigma(x) = \\frac{1}{1 + e^{-x}}$, $\\sigma(-x) = 1 - \\sigma(x)$, "
               "$\\operatorname{logit}(p) = \\ln\\frac{p}{1 - p}$. `np.log` est $\\ln$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Simplifies-tu une expression avec exp et ln, et résous-tu $e^{x} = c$, $a^{n} > c$ en surveillant "
               "le domaine et le sens des inégalités ?\n"
               "2. Passes-tu d'une base de logarithme à une autre, et comptes-tu en bits et en nats ?\n"
               "3. Sais-tu comparer des croissances, lire une échelle logarithmique, et passer d'une probabilité à sa "
               "cote et à son logit ?\n\n"
               "**La suite** : R7, *Limites et dérivation*. Dans workbookIA, continue le chapitre 0A au rythme de ton "
               "tableau de bord.")]


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
