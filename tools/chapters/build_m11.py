#!/usr/bin/env python
"""Build the two notebooks of chapter M11 from a single source (used by Claude).

    python tools/chapters/build_m11.py
    python tools/run_all_notebooks.py chapitres/m11_logique_concentration/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m11_logique_concentration/03_notebook.ipynb

Part 0 checks the paper exercises (✏️ M11.1 to M11.10, 🔗 M11.14); parts A to C are the notebook exercises. Wrong-answer
messages state a rule, never a number of the answer nor the last step that gives it. The data are new: none is a test
case of tests/test_m11_concentration.py, an example of the fiche or of a docstring of concentration.py, or an example of
workbookIA 0B and 11 (no syllogism, no lighthouse, no ripe apples, no spam proportion 48/400, no reinforcement or
punishment, no hand-played bandit with arms (0.3, 0.5, 0.8) or (0.2, 0.5, 0.7), no ε = 0.1 with K = 4, no UCB with
c = 2 and t = 25, no rewards 4, 2, 6, no Beta(7, 5), no Thompson posteriors 6/4, 1/1, 18/22, no agent, no bandit loop).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M11"
FOLDER = "chapitres/m11_logique_concentration"

# ---------------------------------------------------------------------------
# Part 0: the paper exercises (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("M11.1", "Tables de vérité : modus ponens, modus tollens et l'affirmation du conséquent", [
        ("a", "a list of 4 booleans", "[True, False, True, True]",
         '''mistakes={"P ⇒ Q n'est fausse que dans un cas, P vraie et Q fausse : quand P est fausse, l'implication est '''
         '''vraie": [True, False, False, False], "P ⇒ Q est vraie quand P est fausse et Q vraie (ligne FV)": '''
         '''[True, False, False, True]}'''),
        ("b", "a list of line numbers", "[1, 3]",
         '''mistakes={"la seconde prémisse demande Q vraie : la ligne FF ne compte pas": [1, 3, 4], '''
         '''"à la ligne FV, P ⇒ Q est vraie (P fausse) et Q est vraie : les deux prémisses le sont": [1]}'''),
        ("c", "True or False", "False",
         '''mistakes={"une ligne rend les deux prémisses vraies et la conclusion P fausse : c'est un contre-exemple": '''
         '''True}'''),
        ("d", "a list of line numbers", "[2]",
         '''mistakes={"à la ligne FF, non P est vraie et Q fausse : non P ⇒ Q y est fausse": [2, 4], '''
         '''"la seconde prémisse, non Q, demande Q fausse": [1, 2]}'''),
        ("e", "True or False", "True",
         '''mistakes={"regarde la conclusion P dans la seule ligne où les deux prémisses sont vraies": False}'''),
        ("f", "an integer", "4",
         '''mistakes={"compte les lignes où P ⇒ Q et Q ⇒ R sont vraies toutes les deux, sur les 8": {3, 5, 6}}'''),
        ("g", "True or False", "True",
         '''mistakes={"dans chaque ligne où les deux prémisses sont vraies, vérifie la conclusion P ⇒ R": False}'''),
        ("h", "a line number", "2",
         '''mistakes={"ici l'implication va de Q vers P : la ligne 3 serait le contre-exemple de « P ⇒ Q ; non P ; donc non Q »": 3, "cherche la ligne où Q ⇒ P et non Q sont vraies, et la conclusion non P fausse": {1, 4}}'''),
        ("i", "True or False", "True",
         '''mistakes={"avec P vraie et R fausse, la première prémisse n'est vraie que si P et Q est faux, donc si Q est '''
         '''fausse": False}'''),
    ]),

    Paper("M11.2", "Nier des phrases quantifiées sur des modèles et des features", [
        ("a", "True or False", "False",
         '''mistakes={"un « pour tout » tombe dès qu'une case du tableau est sous 0,80": True}'''),
        ("b", "letters, as text", '"BD"',
         '''mistakes={"regarde aussi la colonne du dataset 1": "B", "regarde aussi la colonne du dataset 3": "D", '''
         '''"seules les cases sous 0,80 mettent S₁ en défaut": {"ABD", "BCD", "BDE", "ABCDE"}}'''),
        ("c", "True or False", "False",
         '''mistakes={"le meilleur modèle n'est pas le même sur les trois datasets": True}'''),
        ("d", "True or False", "True",
         '''mistakes={"dans S₃, le modèle peut changer d'un dataset à l'autre : cherche une case ≥ 0,90 par colonne": '''
         '''False}'''),
        ("e", "True or False", "False",
         '''mistakes={"dans S₄, le même modèle doit atteindre 0,90 sur les trois datasets à la fois": True}'''),
        ("f", "True or False", "True",
         '''mistakes={"un seul témoin suffit pour un « il existe » : cherche une ligne entière ≥ 0,85": False}'''),
        ("g", "a letter, as text", '"E"',
         '''mistakes={"A a 0,84 sur le dataset 2, sous 0,85": "A", "C a 0,81 sur le dataset 2": "C", '''
         '''"B et D ont une case sous 0,80": {"B", "D"}}'''),
        ("h", "True or False", "False",
         '''mistakes={"chaque colonne contient une case sous 0,84 : aucun dataset ne convient": True}'''),
    ]),

    Paper("M11.3", "Des phrases traduites en inclusions d'ensembles, et un contre-exemple", [
        ("a", "a list of 2 integers", "[5, 10]",
         '''mistakes={"les multiples de 6 jusqu'à 30 : 6, 12, 18, 24 et 30": [4, 10], '''
         '''"les multiples de 3 jusqu'à 30 : de 3 à 30, de 3 en 3": [5, 9]}'''),
        ("b", "True or False", "True",
         '''mistakes={"un multiple de 6 s'écrit 6k = 3 × (2k)": False}'''),
        ("c", "an integer", "3",
         '''mistakes={"cherche le plus petit multiple de 3 qui n'est pas multiple de 6": {6, 9}}'''),
        ("d", "an integer", "5",
         '''mistakes={"B \\\\ A est l'ensemble des multiples de 3 qui ne sont pas multiples de 6, les impairs": {4, 10}}'''),
        ("e", "a list of integers", "[3]",
         '''mistakes={"3 est premier et multiple de 3": [], "seul 3 est à la fois premier et multiple de 3": [2, 3]}'''),
        ("f", "True or False", "True",
         '''mistakes={"un multiple de 6 est divisible par 2 et par 3 : il n'est jamais premier": False}'''),
        ("g", "an integer", "5",
         '''mistakes={"retire des multiples de 4 ceux qui sont aussi multiples de 6 (multiples de 12)": 7, '''
         '''"compte les contre-exemples (multiples de 4 non multiples de 6), pas les exemples": 2}'''),
        ("h", "an integer", "10",
         '''mistakes={"|A ∪ Q| = |A| + |Q| − |A ∩ Q| : 12 et 24 sont dans les deux": 12}'''),
    ]),

    Paper("M11.4", "Une induction trompeuse par oubli du taux de base, recalculée avec Bayes", [
        ("a", "a number (4 decimals)", "0.03 * 0.92 + 0.97 * 0.06",
         '''decimals=4, mistakes={"ajoute les capteurs bons signalés à tort, 0,97 × 0,06": 0.0276, '''
         '''"les capteurs bons sont 97 % des capteurs, pas 100 %": 0.0876}'''),
        ("b", "a number (4 decimals)", "0.03 * 0.92 / (0.03 * 0.92 + 0.97 * 0.06)",
         '''decimals=4, mistakes={"c'est P(signalé | défectueux) ; la question demande P(défectueux | signalé)": 0.92, '''
         '''"divise par la probabilité d'être signalé": 0.0276}'''),
        ("c", "a number", "582.0",
         '''decimals=1, mistakes={"les capteurs bons sont 97 % des 10 000": 600.0, '''
         '''"c'est le nombre de capteurs défectueux signalés ; la question porte sur les bons": 276.0}'''),
        ("d", "a number (4 decimals)", "0.03 * 0.08 / (1 - (0.03 * 0.92 + 0.97 * 0.06))",
         '''decimals=4, mistakes={"divise par la probabilité de ne pas être signalé, 1 − P(signalé)": 0.0024}'''),
        ("e", "a number (4 decimals)",
         "(lambda q: q * 0.92 / (q * 0.92 + (1 - q) * 0.06))(0.03 * 0.92 / (0.03 * 0.92 + 0.97 * 0.06))",
         '''decimals=4, mistakes={"refais Bayes avec le nouveau taux de base, la réponse de b) : pas 0,92 × 0,92": '''
         '''0.8464}'''),
        ("f", "a number (4 decimals)", "0.06 / (0.92 + 0.06)",
         '''decimals=4, mistakes={"résous 0,92 π = 0,06 (1 − π) : le π est des deux côtés": 0.06 / 0.92, "la réponse est une proportion entre 0 et 1, comme 0,03, pas un pourcentage": 100 * 0.06 / 0.98}'''),
        ("g", "a number (1 decimal)", "50 * 0.03 * 0.92 / (0.03 * 0.92 + 0.97 * 0.06)",
         '''decimals=1, mistakes={"50 × 0,92 reprend la conclusion du technicien : utilise P(défectueux | signalé)": '''
         '''46.0}'''),
    ]),

    Paper("M11.5", "Markov : la queue d'une durée positive", [
        ("a", "a number", "0.25",
         '''decimals=2, mistakes={"Markov : l'espérance divisée par le seuil, pas l'inverse": 4.0}'''),
        ("b", "a number", "1.0",
         '''decimals=2, mistakes={"une borne de probabilité ne dépasse pas 1 : la formule donne plus, on garde 1": 1.5}'''),
        ("c", "a number", "30.0",
         '''decimals=1, mistakes={"E[T] / a ≤ 0,05 donne a ≥ E[T] / 0,05": 0.075}'''),
        ("d", "a number (4 decimals)", "math.exp(-6 / 1.5)",
         '''decimals=4, mistakes={"pour une exponentielle de moyenne 1,5, le paramètre vaut 1/1,5 : P(T ≥ a) = '''
         '''e^(−a/1,5)": math.exp(-9.0), "c'est P(T < 6) ; la question demande P(T ≥ 6)": 1 - math.exp(-4.0)}'''),
        ("e", "a number (1 decimal)", "0.25 / math.exp(-4)",
         '''decimals=1, mistakes={"divise la borne par la vraie valeur, pas l'inverse": math.exp(-4) / 0.25}'''),
        ("f", "a number", "0.75",
         '''decimals=2, mistakes={"6 p = 1,5 donne la probabilité de la valeur 6 ; la valeur 0 prend le reste": 0.25}'''),
        ("g", "a number", "0.375",
         '''decimals=3, mistakes={"« au moins égales à 2 » : la durée 2,0 compte": 0.25}'''),
        ("h", "a number", "0.125",
         '''decimals=3, mistakes={"Markov appliquée à T² : E[T²] divisé par 6², pas par 6": 0.75}'''),
    ]),

    Paper("M11.6", "Tchebychev : combien d'observations pour une moyenne à ± 0,1 ?", [
        ("a", "a number", "1.0",
         '''decimals=2, mistakes={"la variance d'une variable dans [a, b] est au plus (b − a)² / 4": {4.0, 2.0, 0.5}}'''),
        ("b", "an integer", "2000",
         '''mistakes={"n ≥ σ² / (δ t²), avec t² = 0,1² = 0,01": {200, 20000}}'''),
        ("c", "an integer", "180",
         '''mistakes={"la formule utilise la variance σ² = 0,3², pas l'écart-type": 600}'''),
        ("d", "a number", "0.2",
         '''decimals=2, mistakes={"σ² / (n t²) avec le nouvel écart t = 0,05": 0.05}'''),
        ("e", "a number (4 decimals)", "1 / 9",
         '''decimals=4, mistakes={"t = 3σ/√n donne σ² / (n t²) = 1 / 3², pas 1/3": 1 / 3}'''),
        ("f", "a number", "0.25",
         '''decimals=2, mistakes={"p(1 − p) est le plus grand en p = 1/2": {1.0, 0.5}}'''),
        ("g", "an integer", "250",
         '''mistakes={"le risque est de 10 % ici : δ = 0,1": 500, "c'est la taille que donne Hoeffding ; la question demande celle de Tchebychev, σ² / (δ t²)": 150}'''),
        ("h", "an integer", "9",
         '''mistakes={"la borne σ² / (n t²) est inversement proportionnelle à n": 3}'''),
    ]),

    Paper("M11.7", "Hoeffding : rayon de confiance et taille d'échantillon d'une proportion", [
        ("a", "a number (4 decimals)", "math.sqrt(math.log(2 / 0.05) / (2 * 1000))",
         '''decimals=4, mistakes={"le rayon bilatéral utilise ln(2/δ) = ln 40": math.sqrt(math.log(20) / 2000), '''
         '''"n'oublie pas la racine carrée": math.log(40) / 2000, '''
         '''"ln(2/δ) se divise par 2n, pas par n": math.sqrt(math.log(40) / 1000)}'''),
        ("b", "a list of 2 numbers (4 decimals)",
         "[0.137 - math.sqrt(math.log(40) / 2000), 0.137 + math.sqrt(math.log(40) / 2000)]",
         '''decimals=4, mistakes={"le rayon bilatéral utilise ln(2/δ) = ln 40": '''
         '''[0.137 - math.sqrt(math.log(20) / 2000), 0.137 + math.sqrt(math.log(20) / 2000)]}'''),
        ("c", "an integer", "2050",
         '''mistakes={"n doit être au moins ln(2/δ) / (2 r²) : arrondis au-dessus": 2049, '''
         '''"le rayon bilatéral utilise ln(2/δ), pas ln(1/δ)": 1665}'''),
        ("d", "an integer", "2944",
         '''mistakes={"n doit être au moins ln(2/δ) / (2 r²) : arrondis au-dessus": 2943}'''),
        ("e", "a number (4 decimals)", "2 * math.exp(-2 * 1000 * 0.05 ** 2)",
         '''decimals=4, mistakes={"la borne bilatérale a un facteur 2": math.exp(-5.0)}'''),
        ("f", "a number", "0.1",
         '''decimals=2, mistakes={"la variance d'une réponse 0 ou 1 est au plus 1/4": 0.4}'''),
        ("g", "a number (4 decimals)", "math.sqrt(math.log(40) / 8000)",
         '''decimals=4, mistakes={"le rayon décroît comme 1/√n : quatre fois plus de requêtes le divisent par 2": '''
         '''math.sqrt(math.log(40) / 2000) / 4}'''),
        ("h", "a number (4 decimals)", "math.sqrt(math.log(1 / 0.05) / 2000)",
         '''decimals=4, mistakes={"le rayon unilatéral utilise ln(1/δ)": math.sqrt(math.log(40) / 2000)}'''),
    ]),

    Paper("M11.8", "Trois bornes pour une même question : Markov, Tchebychev, Hoeffding, et l'approximation normale", [
        ("a", "a number (4 decimals)", "20 / 30",
         '''decimals=4, mistakes={"Markov sur S ≥ 0 : E[S] = 100 × 0,2, divisé par le seuil": 0.2 / 30}'''),
        ("b", "a number", "0.16",
         '''decimals=2, mistakes={"V(S) = n p (1 − p)": 0.2, "divise la variance par 10², pas par 10": 1.0}'''),
        ("c", "a number (4 decimals)", "math.exp(-2 * 100 * 0.1 ** 2)",
         '''decimals=4, mistakes={"la borne unilatérale n'a pas le facteur 2": 2 * math.exp(-2.0)}'''),
        ("d", "a number (4 decimals)", "normal_sf(2.5)",
         '''decimals=4, mistakes={"z = (30 − 20) / 4, et la question demande la queue à droite": 1 - normal_sf(2.5), '''
         '''"l'écart-type de S est √16 = 4, pas 16": normal_sf(10 / 16)}'''),
        ("e", "a number (4 decimals)", "binomial_tail(100, 0.2, 30)",
         '''decimals=4, mistakes={"S ≥ 30 inclut S = 30": binomial_tail(100, 0.2, 31)}'''),
        ("f", "a letter, as text", '"c"',
         '''mistakes={"compare chacune des trois bornes à la valeur exacte de e)": {"a", "b"}}'''),
        ("g", "a number (4 decimals)", "math.exp(-2 * 100 * 0.05 ** 2)",
         '''decimals=4, mistakes={"S ≥ 25 correspond à un écart t = 0,05 pour X̄ ; la borne unilatérale n'a pas le '''
         '''facteur 2": 1.0}'''),
        ("h", "an integer", "231",
         '''mistakes={"exp(−2 n × 0,1²) ≤ 0,01 donne n ≥ ln(100) / 0,02 : arrondis au-dessus": 230}'''),
    ]),

    Paper("M11.9", "D'où vient le bonus d'UCB : Hoeffding avec un risque qui décroît avec t", [
        ("a", "a number (4 decimals)", "math.sqrt(math.log(1 / 0.01) / (2 * 50))",
         '''decimals=4, mistakes={"le rayon unilatéral utilise ln(1/δ), pas ln(2/δ)": math.sqrt(math.log(200) / 100), '''
         '''"divise par 2N = 100": math.sqrt(math.log(100) / 50)}'''),
        ("b", "a number (4 decimals)", "math.sqrt(2 * math.log(1000) / 50)",
         '''decimals=4, mistakes={"ln(1/δ_t) = 4 ln t, à diviser par 2N": math.sqrt(4 * math.log(1000) / 50), '''
         '''"ln, le logarithme népérien, pas log₁₀": math.sqrt(2 * 3 / 50)}'''),
        ("c", "a number (4 decimals)", "0.62 + math.sqrt(2 * math.log(1000) / 50)",
         '''decimals=4, mistakes={"la borne supérieure est la moyenne observée plus le bonus": 0.62 - math.sqrt(2 * math.log(1000) / 50)}'''),
        ("d", "a number (4 decimals)", "0.45 + math.sqrt(2 * math.log(1000) / 8)",
         '''decimals=4, mistakes={"le bonus de l'option 2 utilise N = 8": 0.45 + math.sqrt(2 * math.log(1000) / 50)}'''),
        ("e", "an integer", "2",
         '''mistakes={"UCB choisit la plus grande borne supérieure, pas la plus grande moyenne observée": 1}'''),
        ("f", "an integer", "1843",
         '''mistakes={"√(2 ln t / N) < 0,1 donne N > 200 ln t : le plus petit entier strictement au-dessus": 1842}'''),
        ("g", "a number (4 decimals)", "math.pi ** 4 / 90 - 1",
         '''decimals=4, mistakes={"la somme commence à t = 2 : retire le terme t = 1": math.pi ** 4 / 90}'''),
        ("h", "a number (4 decimals)", "math.sqrt(math.log(1000) / 50)",
         '''decimals=4, mistakes={"ln(1/δ_t) = 2 ln t pour δ_t = t⁻², à diviser par 2N": math.sqrt(2 * math.log(1000) / 50)}'''),
    ]),

    Paper("M11.10", "ε-greedy : la loi du bras joué et le regret attendu par pas", [
        ("a", "a number", "0.88",
         '''decimals=2, mistakes={"le choix glouton reçoit 1 − ε, plus sa part ε/K du tirage au hasard": 0.85}'''),
        ("b", "a number", "0.03",
         '''decimals=2, mistakes={"l'option 3 n'est choisie que par le tirage au hasard, qui la prend une fois sur K": '''
         '''0.15}'''),
        ("c", "a number", "0.079",
         '''decimals=3, mistakes={"ajoute les options choisies par le tirage au hasard, chacune avec ε / K": 0.0616, '''
         '''"le choix glouton est l'option 1, d'écart 0,07 : ce n'est pas la meilleure": 0.0195}'''),
        ("d", "a number (4 decimals)", "0.01 * 5 / 0.65",
         '''decimals=4, mistakes={"le regret d'un pas vaut (ε / K) Σ Δ_k, avec K = 5": 0.01 / 0.65}'''),
        ("e", "a number", "195.0",
         '''decimals=1, mistakes={"le regret d'un pas, (ε / K) Σ Δ_k = 0,0195, se répète à chaque pas": {19.5, 1950.0}}'''),
        ("f", "a number (4 decimals)", "0.13 * 9.787606036044382",
         '''decimals=4, mistakes={"le regret du pas t vaut (1/t) × Σ Δ_k / K : n'oublie pas le K": '''
         '''0.65 * 9.787606036044382}'''),
        ("g", "a number", "300.0",
         '''decimals=1, mistakes={"l'option 2 n'est choisie que par le tirage au hasard, avec ε / K par pas": 1500.0}'''),
    ]),

    Paper("M11.14", "Pont : combien d'exemples de test pour connaître une accuracy à ± 2 points, garanti par Hoeffding ?", [
        ("a", "an integer", "4612",
         '''mistakes={"n doit être au moins ln(2/δ) / (2 r²) : arrondis au-dessus": 4611, '''
         '''"le rayon bilatéral utilise ln(2/δ) = ln 40": 3745}'''),
        ("b", "a number (4 decimals)", "math.sqrt(math.log(40) / 4000)",
         '''decimals=4, mistakes={"divise ln(2/δ) par 2n = 4 000": math.sqrt(math.log(40) / 2000), '''
         '''"n'oublie pas la racine carrée": math.log(40) / 4000}'''),
        ("c", "True or False", "True",
         '''mistakes={"les deux intervalles ont le même rayon ; l'écart des deux accuracies est plus petit que 2 rayons": '''
         '''False}'''),
        ("d", "a number (4 decimals)", "math.sqrt(math.log(2 / (0.05 / 20)) / 4000)",
         '''decimals=4, mistakes={"choisir le meilleur de 20 demande δ / 20 pour chacun (borne de l'union)": '''
         '''math.sqrt(math.log(40) / 4000), "δ / 20 entre dans le logarithme, pas devant la racine": '''
         '''math.sqrt(20 * math.log(40) / 4000)}'''),
        ("e", "a number (4 decimals)", "1.96 * math.sqrt(0.874 * 0.126 / 2000)",
         '''decimals=4, mistakes={"l'erreur type est √(p̂(1 − p̂) / n), avant le facteur 1,96": math.sqrt(0.874 * 0.126 / 2000)}'''),
        ("f", "an integer", "18445",
         '''mistakes={"n doit être au moins ln(2/δ) / (2 r²) : arrondis au-dessus": 18444}'''),
    ]),
]

for _paper in PAPER:                      # a sub-question without wbm.record options gets an empty string
    _paper.subs = [tuple(sub) + ("",) * (4 - len(sub)) for sub in _paper.subs]

PAPER_CONTEXT = '''# Part 0: the answers are computed exactly from the statements
import math


def normal_sf(z):
    """P(Z >= z) for a standard normal Z."""
    return 0.5 * math.erfc(z / math.sqrt(2))


def binomial_tail(n, p, k):
    """P(S >= k) for S of law B(n, p), summed exactly term by term."""
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))'''

PAPER_INTRO = ("## Partie 0 · Vérifier tes exercices papier (✏️ M11.1 à M11.10, 🔗 M11.14)\n\n"
               "Fais d'abord les exercices de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée, sous la "
               "forme indiquée en commentaire, jamais le calcul qui y mène :\n"
               "- un entier, ou un nombre avec un point décimal, `0.62`, arrondi comme le demande la question ;\n"
               "- `True` / `False` ; une liste `[False, True, True, False]` pour une colonne de table de vérité, `[2, 4]` "
               "pour des numéros de lignes, `[0.09, 0.18]` pour les deux bornes d'un intervalle ;\n"
               "- des lettres entre guillemets, `\"AC\"`.\n\n"
               "Les réponses pas encore remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Notebook exercises: your library (M11.17 to M11.19)
# ---------------------------------------------------------------------------
TOOLS = '''# Tools of the notebook (parts A to C)
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate, stats

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

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M11")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'

HOWTO = ("> **Mode d'emploi `mymath`** (comme en M03). Ouvre ta copie `mon_travail/mymath/concentration.py`, lis la "
         "docstring du module puis celle de la fonction, remplace la ligne `raise NotImplementedError(...)` par ton "
         "code, **enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie. "
         "NumPy et `math` sont permis. Une borne est une probabilité : quand la formule dépasse 1, la fonction rend 1. "
         "Chaque nombre rendu est un `float` de Python.")

OTHER_ERRORS = ["AssertionError", "Exception", "IndexError", "KeyError", "OverflowError", "RecursionError",
                "TypeError", "ValueError", "RuntimeError", "ZeroDivisionError"]


def wrong_error(name: str) -> str:
    return f"lève précisément une {name}, le type d'erreur que demande la docstring : raise {name}(...)"


def errors_source(*excluded: str) -> str:
    """The set of the other exception names, as source code in a fixed order (the notebooks stay identical)."""
    return "{" + ", ".join(f'"{name}"' for name in OTHER_ERRORS if name not in excluded) + "}"


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of concentration.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group("tests/test_m11_concentration.py", "{keyword}")'),
            ("solution", f'run_pytest_group("tests/test_m11_concentration.py", "{keyword}", impl="ref")')]


FLOAT = "la docstring demande un float de Python : float(...)"

M11_17 = Ex(
    "M11.17", "🔨", 1, 15, "Les bornes de Markov et de Tchebychev · `markov_bound, chebyshev_bound`",
    "programmer les bornes de Markov et de Tchebychev, avec leurs contrôles d'entrée et le plafond à 1.",
    "fiche §4 et §5", tracks="C, E", mymath="concentration.py",
    body=HOWTO + r"""

Écris, en suivant les docstrings :
- `markov_bound(mean, a)` : $\min\big(1, \frac{\mathbb{E}[X]}{a}\big)$, la borne de Markov sur $P(X \ge a)$ pour une variable positive ; une `ValueError` si `mean < 0` ou `a <= 0` ;
- `chebyshev_bound(variance, t)` : $\min\big(1, \frac{\mathbb{V}(X)}{t^2}\big)$, la borne de Tchebychev sur $P(\lvert X - \mathbb{E}[X] \rvert \ge t)$ ; une `ValueError` si `variance < 0` ou `t <= 0`.

La vérification calcule :
- a) `markov_bound(2.5, 10)` ; b) `markov_bound(4, 3)` ;
- c) `chebyshev_bound(0.36, 1.2)` ; d) `chebyshev_bound(0, 2)` ;
- e) le nom de l'erreur levée par `markov_bound(-1.0, 2.0)` ; f) le nom de l'erreur levée par `chebyshev_bound(1.0, 0.0)` ;
- g) le nom du type de `markov_bound(1, 4)`, en texte.

Dans ta copie : pourquoi b) vaut-il 1, et que rendrait la formule sans le `min` ? Que dit d) d'une variable de variance nulle ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M11.17a"):
    wbm.check("M11.17a", mymath.concentration.markov_bound(2.5, 10), computed=True)
with checked("M11.17b"):
    wbm.check("M11.17b", mymath.concentration.markov_bound(4, 3), computed=True)
with checked("M11.17c"):
    wbm.check("M11.17c", mymath.concentration.chebyshev_bound(0.36, 1.2), computed=True)
with checked("M11.17d"):
    wbm.check("M11.17d", mymath.concentration.chebyshev_bound(0, 2), computed=True)
with checked("M11.17e"):
    wbm.check("M11.17e", raised(mymath.concentration.markov_bound, -1.0, 2.0), computed=True)
with checked("M11.17f"):
    wbm.check("M11.17f", raised(mymath.concentration.chebyshev_bound, 1.0, 0.0), computed=True)
with checked("M11.17g"):
    wbm.check("M11.17g", type(mymath.concentration.markov_bound(1, 4)).__name__, computed=True)''',
    solution=LOAD_REF + '''
markov_bound, chebyshev_bound = mymath.concentration.markov_bound, mymath.concentration.chebyshev_bound
print("a)", markov_bound(2.5, 10), " b)", markov_bound(4, 3), " c)", chebyshev_bound(0.36, 1.2),
      " d)", chebyshev_bound(0, 2))
print("e)", raised(markov_bound, -1.0, 2.0), " f)", raised(chebyshev_bound, 1.0, 0.0),
      " g)", type(markov_bound(1, 4)).__name__)''',
    record=f'''wbm.record("M11.17a", 0.25, decimals=4,
           mistakes={{"Markov : l'espérance divisée par le seuil, pas l'inverse": 4.0}})
wbm.record("M11.17b", 1.0, decimals=4,
           mistakes={{"une borne de probabilité ne dépasse pas 1 : rends min(1, mean / a)": 4 / 3}})
wbm.record("M11.17c", 0.25, decimals=4,
           mistakes={{"Tchebychev divise par t², pas par t": 0.3}})
wbm.record("M11.17d", 0.0, decimals=4,
           mistakes={{"une variance nulle donne une borne nulle : min(1, 0 / t²) = 0": 1.0}})
wbm.record("M11.17e", "ValueError",
           mistakes={{"une espérance négative est impossible pour X ≥ 0 : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M11.17f", "ValueError",
           mistakes={{"t = 0 n'a pas de sens (division par zéro) : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M11.17g", "float", mistakes={{"{FLOAT}": {{"float64", "int", "Fraction"}}}})''',
    after=tests_cells("markov_bound or chebyshev_bound"),
    note=r"b) La formule donne $\frac{4}{3} > 1$ : un nombre qui ne peut pas être une probabilité. La borne reste vraie "
         r"(toute probabilité est au plus $\frac{4}{3}$), mais elle n'apprend rien ; on rend 1. d) Une variable de "
         r"variance nulle est presque sûrement égale à sa moyenne : $P(\lvert X - \mu \rvert \ge 2) = 0$, et la borne "
         r"aussi.",
)

M11_18 = Ex(
    "M11.18", "🔨", 1, 15, "La borne et le rayon de Hoeffding · `hoeffding_bound, hoeffding_radius`",
    "programmer la borne de Hoeffding et le rayon de confiance qu'on en tire, pour des variables dans un intervalle "
    "quelconque.", "fiche §6", tracks="C, E", mymath="concentration.py",
    body=r"""Écris, en suivant les docstrings :
- `hoeffding_bound(n, t, a=0.0, b=1.0)` : $\min\big(1, 2\exp(-\frac{2nt^2}{(b - a)^2})\big)$, la borne bilatérale de Hoeffding sur $P(\lvert \bar{X} - \mu \rvert \ge t)$ ; une `ValueError` si `n < 1`, `t <= 0` ou `a >= b` ;
- `hoeffding_radius(n, delta, a=0.0, b=1.0)` : $(b - a)\sqrt{\frac{\ln(2/\delta)}{2n}}$, l'écart pour lequel la borne vaut $\delta$ ; une `ValueError` si `n < 1`, si `delta` n'est pas dans $]0, 1[$ ou si `a >= b`.

La vérification calcule (4 décimales) :
- a) `hoeffding_bound(250, 0.08)` ; b) `hoeffding_bound(250, 0.08, a=0.0, b=2.0)` ;
- c) `hoeffding_radius(500, 0.1)` ; d) `hoeffding_radius(500, 0.1, a=-1.0, b=1.0)` ;
- e) `hoeffding_bound(500, hoeffding_radius(500, 0.1))` ;
- f) le nom de l'erreur levée par `hoeffding_radius(100, 1.0)` ; g) celui de l'erreur levée par `hoeffding_bound(0, 0.1)`.

Dans ta copie : pourquoi e) redonne-t-il exactement le risque de c) ? Pourquoi b) est-il bien plus grand que a), et d) le double de c) ?""",
    todo=LOAD_LEARNER,
    check='''with checked("M11.18a"):
    wbm.check("M11.18a", mymath.concentration.hoeffding_bound(250, 0.08), computed=True)
with checked("M11.18b"):
    wbm.check("M11.18b", mymath.concentration.hoeffding_bound(250, 0.08, a=0.0, b=2.0), computed=True)
with checked("M11.18c"):
    wbm.check("M11.18c", mymath.concentration.hoeffding_radius(500, 0.1), computed=True)
with checked("M11.18d"):
    wbm.check("M11.18d", mymath.concentration.hoeffding_radius(500, 0.1, a=-1.0, b=1.0), computed=True)
with checked("M11.18e"):
    wbm.check("M11.18e", mymath.concentration.hoeffding_bound(500, mymath.concentration.hoeffding_radius(500, 0.1)),
              computed=True)
with checked("M11.18f"):
    wbm.check("M11.18f", raised(mymath.concentration.hoeffding_radius, 100, 1.0), computed=True)
with checked("M11.18g"):
    wbm.check("M11.18g", raised(mymath.concentration.hoeffding_bound, 0, 0.1), computed=True)''',
    solution=LOAD_REF + '''
hoeffding_bound, hoeffding_radius = mymath.concentration.hoeffding_bound, mymath.concentration.hoeffding_radius
print("a)", round(hoeffding_bound(250, 0.08), 4), " b)", round(hoeffding_bound(250, 0.08, a=0.0, b=2.0), 4))
print("c)", round(hoeffding_radius(500, 0.1), 4), " d)", round(hoeffding_radius(500, 0.1, a=-1.0, b=1.0), 4),
      " e)", round(hoeffding_bound(500, hoeffding_radius(500, 0.1)), 4))
print("f)", raised(hoeffding_radius, 100, 1.0), " g)", raised(hoeffding_bound, 0, 0.1))''',
    record=f'''wbm.record("M11.18a", 2 * math.exp(-3.2), decimals=4,
           mistakes={{"la borne bilatérale a un facteur 2": math.exp(-3.2)}})
wbm.record("M11.18b", 2 * math.exp(-0.8), decimals=4,
           mistakes={{"la largeur b − a = 2 entre au carré au dénominateur": 2 * math.exp(-1.6),
                     "le résultat dépend de a et b : utilise-les dans la formule": 2 * math.exp(-3.2)}})
wbm.record("M11.18c", math.sqrt(math.log(20) / 1000), decimals=4,
           mistakes={{"le rayon bilatéral utilise ln(2/δ), pas ln(1/δ)": math.sqrt(math.log(10) / 1000),
                     "n'oublie pas la racine carrée": math.log(20) / 1000}})
wbm.record("M11.18d", 2 * math.sqrt(math.log(20) / 1000), decimals=4,
           mistakes={{"le rayon est multiplié par b − a, pas par (b − a)²": 4 * math.sqrt(math.log(20) / 1000),
                     "le résultat dépend de a et b : multiplie par b − a": math.sqrt(math.log(20) / 1000)}})
wbm.record("M11.18e", 0.1, decimals=4,
           mistakes={{"le rayon est l'écart pour lequel la borne vaut δ : vérifie ln(2/δ) et la racine": 0.05}})
wbm.record("M11.18f", "ValueError",
           mistakes={{"δ = 1 n'est pas un risque dans ]0, 1[ : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M11.18g", "ValueError",
           mistakes={{"une moyenne de 0 variable n'a pas de sens : la docstring demande une ValueError pour n < 1": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})''',
    after=tests_cells("hoeffding"),
    note=r"e) Le rayon est **défini** comme l'écart $r$ pour lequel $2e^{-2nr^2/(b - a)^2} = \delta$ : remettre $r$ "
         r"dans la borne redonne $\delta$ (aux arrondis près). b) La borne ne dépend que de $\frac{t}{b - a}$ : un "
         r"écart 0,08 pour des variables dans $[0, 2]$ vaut un écart 0,04 dans $[0, 1]$, d'où l'exposant "
         r"$-2 \times 250 \times 0{,}04^2 = -0{,}8$. d) Le rayon est proportionnel à $b - a = 2$.",
)

M11_19 = Ex(
    "M11.19", "🔨", 1, 10, "La queue empirique d'un échantillon · `empirical_tail`",
    "estimer une probabilité de queue par la proportion d'un échantillon, et vérifier que cette proportion respecte "
    "Markov.", "fiche §4", tracks="C", mymath="concentration.py",
    body=r"""Écris `empirical_tail(samples, threshold)` : la proportion des valeurs de l'échantillon **au moins égales** au seuil, une estimation de $P(X \ge \text{seuil})$ ; une `ValueError` si l'échantillon est vide.

Avec `sample_19 = np.random.default_rng(19).exponential(2.0, size=20_000)` (vingt mille tirages d'une loi exponentielle de moyenne 2), la vérification calcule :
- a) `empirical_tail([3, 8, 1, 8, 5, 2], 5)` ; b) `empirical_tail([3, 8, 1, 8, 5, 2], 8)` (4 décimales) ;
- c) `empirical_tail(sample_19, 6.0)` (4 décimales) ;
- d) le nom de l'erreur levée par `empirical_tail([], 1.0)` ;
- e) vrai ou faux : pour chaque seuil $a$ de `[0.5, 1, 2, 4, 8, 16]`, `empirical_tail(sample_19, a) <= sample_19.mean() / a`.

Dans ta copie : comparer c) à la valeur exacte $e^{-3} \approx 0{,}0498$ ; d'où vient l'écart ? Pourquoi e) est-il vrai pour **tout** échantillon de valeurs positives, et pas seulement en moyenne ?""",
    given='''sample_19 = np.random.default_rng(19).exponential(2.0, size=20_000)   # an exponential law of mean 2''',
    todo=LOAD_LEARNER,
    check='''with checked("M11.19a"):
    wbm.check("M11.19a", mymath.concentration.empirical_tail([3, 8, 1, 8, 5, 2], 5), computed=True)
with checked("M11.19b"):
    wbm.check("M11.19b", mymath.concentration.empirical_tail([3, 8, 1, 8, 5, 2], 8), computed=True)
with checked("M11.19c"):
    wbm.check("M11.19c", mymath.concentration.empirical_tail(sample_19, 6.0), computed=True)
with checked("M11.19d"):
    wbm.check("M11.19d", raised(mymath.concentration.empirical_tail, [], 1.0), computed=True)
with checked("M11.19e"):
    wbm.check("M11.19e", all(mymath.concentration.empirical_tail(sample_19, a) <= sample_19.mean() / a
                             for a in [0.5, 1, 2, 4, 8, 16]), computed=True)''',
    solution=LOAD_REF + '''
empirical_tail = mymath.concentration.empirical_tail
print("a)", empirical_tail([3, 8, 1, 8, 5, 2], 5), " b)", round(empirical_tail([3, 8, 1, 8, 5, 2], 8), 4),
      " c)", round(empirical_tail(sample_19, 6.0), 4), " d)", raised(empirical_tail, [], 1.0))
print("e)", all(empirical_tail(sample_19, a) <= sample_19.mean() / a for a in [0.5, 1, 2, 4, 8, 16]))''',
    record=f'''wbm.record("M11.19a", 0.5, decimals=4,
           mistakes={{"« au moins égales » : la valeur 5 elle-même compte (>=, pas >)": 1 / 3}})
wbm.record("M11.19b", 1 / 3, decimals=4,
           mistakes={{"« au moins égales » : les deux valeurs 8 comptent (>=, pas >)": 0.0,
                     "une proportion : divise le nombre de valeurs par la taille de l'échantillon": 2.0}})
wbm.record("M11.19c", 0.05145, decimals=4,
           mistakes={{"la proportion des valeurs au moins égales au seuil, pas des valeurs en dessous": 0.94855}})
wbm.record("M11.19d", "ValueError",
           mistakes={{"un échantillon vide n'a pas de proportion : la docstring demande une ValueError": "aucune",
                     "{wrong_error("ValueError")}": {errors_source("ValueError")}}})
wbm.record("M11.19e", True,
           mistakes={{"Markov vaut pour la loi de l'échantillon : vérifie que ta fonction compte les valeurs >= seuil, en "
                      "proportion": False}})''',
    after=tests_cells("empirical_tail"),
    note=r"c) L'écart à $e^{-3}$ vient du hasard du tirage : l'erreur type d'une proportion voisine de 0,05 sur "
         r"20 000 tirages est $\sqrt{0{,}05 \times 0{,}95 / 20\,000} \approx 0{,}0015$. e) La loi qui donne le poids "
         r"$\frac{1}{n}$ à chaque valeur est une loi de variable positive, d'espérance la moyenne de l'échantillon : "
         r"Markov s'y applique exactement, sans aucun hasard.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a library, a prediction, two experiments (M11.20 to M11.23)
# ---------------------------------------------------------------------------
M11_20 = Ex(
    "M11.20", "📦", 1, 15, "Les vraies queues d'une loi exponentielle et d'une binomiale (`scipy.stats`) contre les bornes",
    "calculer des probabilités de queue exactes avec scipy.stats, et les comparer aux bornes de ta librairie.",
    "fiche §4 à §6", tracks="C",
    body=r"""Avec `scipy.stats` (importé sous le nom `stats`) et tes fonctions de `mymath` :
- $T$ suit une loi exponentielle de moyenne 3 (`stats.expon(scale=3)`) : a) $P(T \ge 15)$, avec la méthode `.sf` (*survival function*, $P(T > x)$, égale ici à $P(T \ge x)$) ; b) combien de fois la borne de Markov dépasse cette valeur (2 décimales) ; c) le plus petit seuil $a$ tel que $P(T \ge a) \le 0{,}01$, avec la méthode `.isf` ;
- $S$ suit une loi binomiale $\mathcal{B}(60 ;\ 0{,}25)$ (`stats.binom(60, 0.25)`) et $\bar{X} = \frac{S}{60}$ : d) $P(\lvert \bar{X} - 0{,}25 \rvert \ge 0{,}1)$, c'est-à-dire $P(S \le 9) + P(S \ge 21)$, avec `.cdf` et `.sf` ; e) la borne de Tchebychev de cette probabilité ($\mathbb{V}(\bar{X}) = \frac{0{,}25 \times 0{,}75}{60}$) ; f) la borne de Hoeffding.

Les réponses a) et c) à f) sont à 4 décimales. Attention : pour une loi discrète, `.sf(k)` vaut $P(S > k)$, donc $P(S \ge 21)$ s'écrit `.sf(20)`.

Dans ta copie : laquelle des deux bornes de e) et f) est la meilleure ici, et pourquoi Hoeffding perd-elle avec $n = 60$ ?""",
    todo='''answer_M11_20a = ...  # a) P(T >= 15) with stats.expon(scale=3).sf
answer_M11_20b = ...  # b) Markov's bound divided by a)
answer_M11_20c = ...  # c) the smallest a with P(T >= a) <= 0.01, with .isf
answer_M11_20d = ...  # d) P(S <= 9) + P(S >= 21) for S of law B(60, 0.25)
answer_M11_20e = ...  # e) Chebyshev's bound (mymath.concentration.chebyshev_bound)
answer_M11_20f = ...  # f) Hoeffding's bound (mymath.concentration.hoeffding_bound)''',
    check='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M11")
for letter, answer in zip("abcdef", [answer_M11_20a, answer_M11_20b, answer_M11_20c, answer_M11_20d, answer_M11_20e,
                                     answer_M11_20f]):
    wbm.check(f"M11.20{letter}", answer, computed=True)''',
    solution=LOAD_REF + '''
T_20, S_20 = stats.expon(scale=3), stats.binom(60, 0.25)
answer_M11_20a = float(T_20.sf(15))
answer_M11_20b = mymath.concentration.markov_bound(3, 15) / answer_M11_20a
answer_M11_20c = float(T_20.isf(0.01))
answer_M11_20d = float(S_20.cdf(9) + S_20.sf(20))
answer_M11_20e = mymath.concentration.chebyshev_bound(0.25 * 0.75 / 60, 0.1)
answer_M11_20f = mymath.concentration.hoeffding_bound(60, 0.1)
print([round(v, 4) for v in (answer_M11_20a, answer_M11_20b, answer_M11_20c, answer_M11_20d, answer_M11_20e,
                             answer_M11_20f)])''',
    record='''wbm.record("M11.20a", math.exp(-5), decimals=4,
           mistakes={"sf donne P(T > x), la queue à droite ; cdf donne la partie gauche": 1 - math.exp(-5),
                     "scale est la moyenne 3 : stats.expon(scale=3), pas stats.expon(3)": math.exp(-4)})
wbm.record("M11.20b", 0.2 / math.exp(-5), decimals=2,
           mistakes={"divise la borne de Markov, E[T] / 15 = 0,2, par la vraie valeur": math.exp(-5) / 0.2})
wbm.record("M11.20c", 3 * math.log(100), decimals=4,
           mistakes={"isf(0.01) donne le seuil dont la queue à droite vaut 0,01 ; ppf(0.01) donne celui de gauche":
                         -3 * math.log(0.99)})
wbm.record("M11.20d", 0.09931141968069937, decimals=4,
           mistakes={"pour une loi discrète, sf(20) = P(S >= 21) ; sf(21) oublie S = 21": 0.0749683515073285,
                     "compte les deux côtés : P(S <= 9) et P(S >= 21)": {0.05414393818821915,
                                                                          0.045167481492480246}})
wbm.record("M11.20e", 0.3125, decimals=4,
           mistakes={"la variance de la moyenne est p(1 − p) / n, et t = 0,1": 0.1875 / 0.1})
wbm.record("M11.20f", 2 * math.exp(-1.2), decimals=4,
           mistakes={"la borne bilatérale a un facteur 2": math.exp(-1.2)})''',
    note=r"e) Tchebychev (0,31) bat Hoeffding (0,60) : avec $n = 60$ et $t = 0{,}1$, l'exposant $2nt^2 = 1{,}2$ est "
         r"petit, et Hoeffding ignore la variance (0,1875, sous le maximum 0,25 qu'elle suppose). Pour $n$ grand, "
         r"l'exponentielle finit par gagner (M11.21, M11.24). La vraie valeur, 0,099, est trois fois sous la "
         r"meilleure borne.",
)

M11_21_EXPERIMENT = '''print(f"{'cas':4} {'Markov':>10} {'Tchebychev':>12} {'Hoeffding':>11}   la plus serrée")
for letter, (p, t) in zip("abcd", CASES_21):
    bounds = bounds_21(100, p, t)
    best = ["Markov", "Tchebychev", "Hoeffding"][int(np.argmin(bounds))]
    print(f"{letter})   {bounds[0]:10.4g} {bounds[1]:12.4g} {bounds[2]:11.4g}   {best}")'''

M11_21 = Ex(
    "M11.21", "🔮", 1, 10, "Prédire : laquelle des trois bornes est la plus serrée pour n = 100 ?",
    "prévoir quelle borne gagne selon la moyenne et l'écart, puis le vérifier.", "fiche §4 à §6", tracks="C, E",
    hypothesis=True,
    given='''reference_21 = wbm.load_mymath("ref")     # the experiment uses the reference of concentration.py
CASES_21 = [(0.5, 0.1), (0.02, 0.05), (0.01, 0.5), (0.001, 0.004)]   # (p, t) for the cases a) to d)


def bounds_21(n, p, t):
    """The three bounds on P(X̄ >= p + t) for the mean of n Bernoulli(p): Markov, Chebyshev, one-sided Hoeffding."""
    return [reference_21.concentration.markov_bound(p, p + t),
            reference_21.concentration.chebyshev_bound(p * (1 - p) / n, t),
            min(1.0, math.exp(-2 * n * t ** 2))]''',
    body=r"""$\bar{X}$ est la moyenne de $n = 100$ variables de Bernoulli de paramètre $p$, indépendantes. On cherche une borne de $P(\bar{X} \ge p + t)$ ; trois sont valables :
- **Markov** ($\bar{X} \ge 0$) : $\frac{p}{p + t}$ ;
- **Tchebychev** : $\frac{p(1 - p)}{n t^2}$ (elle borne même $P(\lvert \bar{X} - p \rvert \ge t)$) ;
- **Hoeffding**, unilatérale : $e^{-2nt^2}$.

Pour chaque cas, choisis le numéro de la borne la plus petite (la plus serrée) : (1) Markov ; (2) Tchebychev ; (3) Hoeffding.
- a) $p = 0{,}5$, $t = 0{,}1$ ;
- b) $p = 0{,}02$, $t = 0{,}05$ ;
- c) $p = 0{,}01$, $t = 0{,}5$ ;
- d) $p = 0{,}001$, $t = 0{,}004$.

**Avant d'exécuter quoi que ce soit**, écris tes quatre prédictions (le **numéro du choix**), vérifie-les, puis lance le calcul des trois bornes.""",
    todo='''prediction_M11_21a = ...  # a) 1, 2 or 3, written BEFORE running the computation below
prediction_M11_21b = ...  # b) 1, 2 or 3
prediction_M11_21c = ...  # c) 1, 2 or 3
prediction_M11_21d = ...  # d) 1, 2 or 3''',
    check='''for letter, prediction in zip("abcd", [prediction_M11_21a, prediction_M11_21b, prediction_M11_21c,
                                         prediction_M11_21d]):
    wbm.check(f"M11.21{letter}", prediction)''',
    record='''wbm.record("M11.21a", 3, prediction=True, choices=[1, 2, 3])
wbm.record("M11.21b", 2, prediction=True, choices=[1, 2, 3])
wbm.record("M11.21c", 3, prediction=True, choices=[1, 2, 3])
wbm.record("M11.21d", 1, prediction=True, choices=[1, 2, 3])''',
    after=[
        ("md", "**Le calcul.** Il ne s'exécute qu'une fois tes quatre prédictions écrites."),
        ("todo", guarded(M11_21_EXPERIMENT, [f"prediction_M11_21{letter}" for letter in "abcd"],
                         "⏳ Écris d'abord tes quatre prédictions, puis exécute à nouveau.")),
        ("solution", M11_21_EXPERIMENT),
        ("md", "**Après le calcul**, dans ta copie : pour chaque cas, dis ce que chaque borne utilise (la moyenne "
               "seule, la variance, ou l'intervalle $[0, 1]$) et pourquoi c'est celle-là qui gagne. Quand $p$ est "
               "proche de 0, pourquoi Hoeffding est-elle mauvaise pour un petit écart ? Laquelle choisirais-tu sans "
               "rien savoir de $p$ ?"),
    ],
    note=r"a) $p = 0{,}5$ : la variance est maximale, $nt^2 = 1$ ; Hoeffding ($e^{-2} \approx 0{,}14$) bat Tchebychev "
         r"(0,25) et Markov (0,83). b) $p = 0{,}02$ : la variance $0{,}0196$ est minuscule, Tchebychev donne 0,078 ; "
         r"Hoeffding, qui l'ignore, donne $e^{-0{,}5} \approx 0{,}61$. c) Un grand écart : l'exponentielle "
         r"$e^{-50}$ écrase tout. d) Un écart minuscule : Hoeffding ($\approx 0{,}997$) et Tchebychev (0,62) ne "
         r"disent presque rien, et Markov, qui sait seulement que la moyenne vaut 0,001, donne 0,2. Aucune borne "
         r"ne gagne partout : chacune utilise une information différente.",
)

NS_22 = "[32, 64, 128, 256, 512, 1024]"

M11_22 = Ex(
    "M11.22", "🔬", 2, 20, "La fréquence des écarts |x̄ − p| ≥ t comparée à la borne de Hoeffding, quand n grandit",
    "simuler la fréquence des grands écarts d'une moyenne, la comparer à la probabilité exacte et à la borne de "
    "Hoeffding, et voir la décroissance exponentielle.", "fiche §6", tracks="C",
    body=rf"""On simule des moyennes $\bar{{X}}$ de $n$ variables de Bernoulli de paramètre $p = 0{{,}}25$, et on compte la fréquence des écarts $\lvert \bar{{X}} - p \rvert \ge t$, avec $t = 0{{,}}0625 = \frac{{1}}{{16}}$ (des nombres exacts en binaire : aucune comparaison de flottants ne tombe à côté).

1. Écris `deviation_frequency(n, p, t, reps, rng)` : elle tire `k = rng.binomial(n, p, size=reps)` (le nombre de succès de `reps` échantillons de taille $n$, en un seul appel), puis rend la proportion des échantillons pour lesquels $\lvert \frac{{k}}{{n}} - p \rvert \ge t$, en `float`.
2. La cellule suivante l'appelle pour $n$ dans `{NS_22}`, dans cet ordre, avec `reps = 4000` et **un seul** générateur `rng = np.random.default_rng(22)` créé avant la boucle ; elle calcule aussi la probabilité exacte (avec `stats.binom`) et la borne de Hoeffding (avec ta fonction).

La vérification calcule :
- a) la fréquence simulée pour $n = 256$ (4 décimales) ;
- b) vrai ou faux : pour chaque $n$, la fréquence simulée est au plus la borne de Hoeffding ;
- c) le plus petit $n$ de la liste pour lequel la borne de Hoeffding est sous 0,05 ;
- d) la probabilité exacte pour $n = 256$ (4 décimales) ;
- e) pour $n = 512$, combien de fois la borne dépasse la probabilité exacte (1 décimale).

Dans ta copie : trace (ou imagine) les trois suites en échelle log : laquelle décroît comme une droite, et pourquoi ? D'où vient l'écart entre a) et d) ? Pourquoi la borne devient-elle de plus en plus lâche en valeur relative (e)) ?""",
    todo='''def deviation_frequency(n, p, t, reps, rng):
    """The share of reps simulated means of n Bernoulli(p) at distance at least t from p (one call to rng.binomial)."""
    raise NotImplementedError("rng.binomial(n, p, size=reps), puis la proportion des |k/n − p| >= t")''',
    check=f'''with checked("M11.22"):
    mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M11")
    rng_22, p_22, t_22 = np.random.default_rng(22), 0.25, 0.0625
    rows_22 = []
    for n in {NS_22}:
        k_exact = np.arange(n + 1)
        exact = float(stats.binom.pmf(k_exact, n, p_22)[np.abs(k_exact / n - p_22) >= t_22].sum())
        rows_22.append((n, deviation_frequency(n, p_22, t_22, 4000, rng_22), exact,
                        mymath.concentration.hoeffding_bound(n, t_22)))
    for n, freq, exact, bound in rows_22:
        print(f"n = {{n:5d}}  fréquence {{freq:.4f}}  exacte {{exact:.6f}}  Hoeffding {{bound:.6f}}")
    by_n = {{n: (freq, exact, bound) for n, freq, exact, bound in rows_22}}
    wbm.check("M11.22a", by_n[256][0], computed=True)
    wbm.check("M11.22b", all(freq <= bound for _, freq, _, bound in rows_22), computed=True)
    wbm.check("M11.22c", min(n for n, _, _, bound in rows_22 if bound < 0.05), computed=True)
    wbm.check("M11.22d", by_n[256][1], computed=True)
    wbm.check("M11.22e", by_n[512][2] / by_n[512][1], computed=True)''',
    solution=LOAD_REF + f'''


def deviation_frequency(n, p, t, reps, rng):
    """The share of reps simulated means of n Bernoulli(p) at distance at least t from p (one call to rng.binomial)."""
    k = rng.binomial(n, p, size=reps)
    return float(np.mean(np.abs(k / n - p) >= t))


rng_22, p_22, t_22 = np.random.default_rng(22), 0.25, 0.0625
for n in {NS_22}:
    k_exact = np.arange(n + 1)
    exact = float(stats.binom.pmf(k_exact, n, p_22)[np.abs(k_exact / n - p_22) >= t_22].sum())
    print(f"n = {{n:5d}}  fréquence {{deviation_frequency(n, p_22, t_22, 4000, rng_22):.4f}}  exacte {{exact:.6f}}  "
          f"Hoeffding {{mymath.concentration.hoeffding_bound(n, t_22):.6f}}")''',
    record='''wbm.record("M11.22a", 0.021, decimals=4,
           mistakes={"un seul générateur, créé avant la boucle, et un appel rng.binomial(n, p, size=reps) par n, dans "
                     "l'ordre de la liste : sinon les tirages diffèrent": {0.0205, 0.02475}})
wbm.record("M11.22b", True,
           mistakes={"la borne de Hoeffding est une borne : compare chaque fréquence à hoeffding_bound(n, t)": False})
wbm.record("M11.22c", 512,
           mistakes={"la borne bilatérale 2 exp(−2 n t²), plafonnée à 1, passe sous 0,05 plus tard que la fréquence":
                         {128, 256, 1024}})
wbm.record("M11.22d", 0.02500559710298505, decimals=4,
           mistakes={"compte les k avec |k/n − p| >= t des deux côtés de p": {0.014083366906127836,
                                                                            0.010922230196857211}})
wbm.record("M11.22e", 0.03663127777746836 / 0.001302439566538581, decimals=1,
           mistakes={"divise la borne par la probabilité exacte, pas l'inverse": 0.001302439566538581 /
                     0.03663127777746836})''',
    note=r"En échelle log, la borne $2e^{-n/128}$ est une droite en $n$ ; la probabilité exacte décroît aussi "
         r"exponentiellement, mais plus vite (son exposant dépend de la variance $p(1 - p) = 0{,}1875$, sous le "
         r"$\frac{1}{4}$ que Hoeffding suppose), d'où un rapport qui grandit : 11 à $n = 256$, 28 à $n = 512$, 135 à "
         r"$n = 1\,024$. La fréquence simulée colle à la probabilité exacte, à l'erreur type près "
         r"($\sqrt{0{,}025 \times 0{,}975 / 4\,000} \approx 0{,}0025$).",
)

M11_23 = Ex(
    "M11.23", "🔬", 2, 15, "La probabilité qu'un tirage d'une loi Beta dépasse celui d'une autre, par simulation",
    "estimer par simulation, puis calculer par une intégrale, la probabilité que l'échantillonnage de Thompson choisisse "
    "une option plutôt qu'une autre.", "fiche §7 ; M04 (loi Beta a posteriori)", tracks="C",
    body=r"""Deux options ont, après quelques essais et avec un a priori uniforme, les lois a posteriori $\theta_1 \sim \mathrm{Beta}(a_1, b_1)$ et $\theta_2 \sim \mathrm{Beta}(a_2, b_2)$, indépendantes. L'échantillonnage de Thompson choisit l'option 2 avec la probabilité $P(\theta_2 > \theta_1)$.

1. Écris `prob_draw_greater(a1, b1, a2, b2, size, rng)` : elle tire `x1 = rng.beta(a1, b1, size)`, **puis** `x2 = rng.beta(a2, b2, size)`, et rend la proportion des indices où `x2 > x1`, en `float`.
2. Écris `exact_greater(a1, b1, a2, b2)` : $P(\theta_2 > \theta_1) = \int_0^1 f_2(x)\,F_1(x)\,dx$, où $f_2$ est la densité de $\theta_2$ et $F_1$ la fonction de répartition de $\theta_1$ (`stats.beta(a, b).pdf`, `.cdf`, et `integrate.quad`, qui rend un couple : la valeur, puis une estimation de l'erreur).

La vérification calcule :
- a) `prob_draw_greater(1, 1, 2, 1, 200_000, np.random.default_rng(231))` (4 décimales) ;
- b) la valeur exacte de a), calculée **à la main** (fiche §7 ; 4 décimales) ;
- c) l'option 1 a eu 12 succès et 8 échecs, l'option 2 3 succès et 2 échecs : `prob_draw_greater(13, 9, 4, 3, 200_000, np.random.default_rng(232))` (4 décimales) ;
- d) `exact_greater(13, 9, 4, 3)` (4 décimales) ;
- e) l'option 2 a maintenant 30 succès et 28 échecs (l'option 1 n'a pas changé) : `exact_greater(13, 9, 31, 29)` (4 décimales).

Dans ta copie : les moyennes a posteriori de c) valent 0,59 et 0,57 ; pourquoi Thompson choisit-il quand même l'option 2 presque une fois sur deux ? Que s'est-il passé entre d) et e) ?""",
    todo='''def prob_draw_greater(a1, b1, a2, b2, size, rng):
    """The share of the size pairs of draws (x1 from Beta(a1, b1) first, then x2 from Beta(a2, b2)) with x2 > x1."""
    raise NotImplementedError("x1 = rng.beta(a1, b1, size), puis x2 = rng.beta(a2, b2, size), puis la proportion")


def exact_greater(a1, b1, a2, b2):
    """P(theta2 > theta1) for independent theta1 ~ Beta(a1, b1) and theta2 ~ Beta(a2, b2), by numerical integration."""
    raise NotImplementedError("integrate.quad sur [0, 1] de la densité de theta2 fois la répartition de theta1")


answer_M11_23b = ...  # b) the exact value of a), computed by hand (4 decimals)''',
    check='''with checked("M11.23a"):
    wbm.check("M11.23a", prob_draw_greater(1, 1, 2, 1, 200_000, np.random.default_rng(231)), computed=True)
wbm.check("M11.23b", answer_M11_23b)
with checked("M11.23c"):
    wbm.check("M11.23c", prob_draw_greater(13, 9, 4, 3, 200_000, np.random.default_rng(232)), computed=True)
with checked("M11.23d"):
    wbm.check("M11.23d", exact_greater(13, 9, 4, 3), computed=True)
with checked("M11.23e"):
    wbm.check("M11.23e", exact_greater(13, 9, 31, 29), computed=True)''',
    solution='''def prob_draw_greater(a1, b1, a2, b2, size, rng):
    """The share of the size pairs of draws (x1 from Beta(a1, b1) first, then x2 from Beta(a2, b2)) with x2 > x1."""
    x1 = rng.beta(a1, b1, size)
    x2 = rng.beta(a2, b2, size)
    return float(np.mean(x2 > x1))


def exact_greater(a1, b1, a2, b2):
    """P(theta2 > theta1) for independent theta1 ~ Beta(a1, b1) and theta2 ~ Beta(a2, b2), by numerical integration."""
    value, _ = integrate.quad(lambda x: stats.beta(a2, b2).pdf(x) * stats.beta(a1, b1).cdf(x), 0, 1)
    return float(value)


answer_M11_23b = 2 / 3
print("a)", round(prob_draw_greater(1, 1, 2, 1, 200_000, np.random.default_rng(231)), 4), " b)", round(2 / 3, 4))
print("c)", round(prob_draw_greater(13, 9, 4, 3, 200_000, np.random.default_rng(232)), 4),
      " d)", round(exact_greater(13, 9, 4, 3), 4), " e)", round(exact_greater(13, 9, 31, 29), 4))''',
    record='''wbm.record("M11.23a", 0.667175, decimals=4,
           mistakes={"tire x1 d'abord, puis x2, avec le même générateur : sinon les tirages diffèrent": 0.665985,
                     "la proportion des x2 > x1, pas des x1 > x2": 0.332825})
wbm.record("M11.23b", 2 / 3, decimals=4,
           mistakes={"P(θ₁ < θ₂) = E[θ₂] pour θ₁ uniforme : la moyenne de Beta(2, 1) est 2/3": {0.5, 1 / 3}})
wbm.record("M11.23c", 0.46982, decimals=4,
           mistakes={"tire x1 d'abord, puis x2, avec le même générateur : sinon les tirages diffèrent": 0.471545,
                     "la proportion des x2 > x1, pas des x1 > x2": 0.53018})
wbm.record("M11.23d", 0.47246376811594176, decimals=4,
           mistakes={"intègre la densité de θ₂ fois la répartition de θ₁ (et non l'inverse)": 1 - 0.47246376811594176})
wbm.record("M11.23e", 0.26929213601079727, decimals=4,
           mistakes={"intègre la densité de θ₂ fois la répartition de θ₁ (et non l'inverse)": 1 - 0.26929213601079727})''',
    note=r"c) La loi $\mathrm{Beta}(4, 3)$, tirée de 5 essais seulement, est très étalée : ses tirages dépassent "
         r"souvent ceux de $\mathrm{Beta}(13, 9)$, plus resserrée, même si les moyennes sont proches. e) Avec 58 "
         r"essais, la loi de l'option 2 se resserre autour de 0,52 : la probabilité tombe à 0,27, et Thompson la choisit "
         r"de moins en moins. Les paramètres sont entiers : la valeur exacte de d) est même un rationnel, "
         r"$\frac{163}{345}$.",
)

# ---------------------------------------------------------------------------
# Notebook exercises: a figure, a bug hunt, a test, a challenge (M11.24 to M11.27)
# ---------------------------------------------------------------------------
M11_24_CHECK = '''with checked("M11.24 vérifications"):
    problems = []
    n_t, p_t = 80, 0.35
    ts_t = np.linspace(0.021, 0.401, 25)               # n (p + t) is never an integer here
    expected = {
        "la vraie queue P(X̄ >= p + t) (stats.binom)": [float(stats.binom.sf(math.ceil(n_t * (p_t + t) - 1e-9) - 1,
                                                                            n_t, p_t)) for t in ts_t],
        "la borne de Markov p / (p + t)": [min(1.0, p_t / (p_t + t)) for t in ts_t],
        "la borne de Tchebychev p(1 − p) / (n t²), plafonnée à 1": [min(1.0, p_t * (1 - p_t) / (n_t * t ** 2))
                                                                    for t in ts_t],
        "la borne de Hoeffding exp(−2 n t²)": [math.exp(-2 * n_t * t ** 2) for t in ts_t],
    }
    fig_t, ax_t = plt.subplots()
    try:
        created = drawn(draw_24, ax_t, n_t, p_t, ts_t)
    finally:
        plt.close(fig_t)
    if created:
        problems.append("draw_24 ouvre sa propre figure : dessine dans l'axe reçu")
    else:
        curves = [np.asarray(line.get_ydata(), dtype=float) for line in ax_t.get_lines()]
        for what, values in expected.items():
            if not any(len(c) == len(values) and np.allclose(c, values, rtol=1e-6, atol=1e-12) for c in curves):
                problems.append(f"il manque {what}, tracée en fonction de t (une ligne ax.plot sur les ts reçus)")
        if ax_t.get_yscale() != "log":
            problems.append("l'axe des probabilités doit être en échelle log : ax.set_yscale(\\"log\\")")
        if not ax_t.get_legend():
            problems.append("ajoute une légende (ax.legend()) : quatre courbes sans nom ne se lisent pas")
    if problems:
        print("❌ Ex M11.24 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M11.24 : la vraie queue et les trois bornes sont à leur place, en échelle log, avec une légende.")'''

M11_24 = Ex(
    "M11.24", "🎨", 1, 15, "Les bornes de Markov, de Tchebychev et de Hoeffding contre la vraie queue, en échelle log",
    "voir sur une figure à quel point chaque borne est large, et comment elles se croisent quand l'écart grandit.",
    "fiche §4 à §6 ; Ex M11.21", tracks="C",
    body=r"""Écris `draw_24(ax, n, p, ts)`, qui trace dans l'axe `ax`, en fonction de $t$ (le tableau `ts`), pour la moyenne $\bar{X}$ de $n$ variables de Bernoulli de paramètre $p$ :
- la **vraie queue** $P(\bar{X} \ge p + t) = P(S \ge n(p + t))$, avec $S \sim \mathcal{B}(n, p)$ : `stats.binom.sf(k - 1, n, p)` où `k = math.ceil(n * (p + t) - 1e-9)` est le plus petit entier au moins égal à $n(p + t)$ ;
- la borne de **Markov** $\frac{p}{p + t}$, la borne de **Tchebychev** $\min\big(1, \frac{p(1 - p)}{n t^2}\big)$ et la borne de **Hoeffding** unilatérale $e^{-2nt^2}$ ;

chacune par `ax.plot(ts, valeurs, label=...)`, avec l'axe des probabilités en échelle log (`ax.set_yscale("log")`) et une légende. La cellule de la figure s'en sert pour $n = 50$ et $p = 0{,}3$ ; une cellule de vérification l'essaie sur d'autres valeurs, dans des axes neufs.

Dans ta copie : pour quels écarts $t$ chaque borne est-elle la meilleure ? Laquelle a la même forme que la vraie queue en échelle log, et pourquoi ?""",
    todo='''def draw_24(ax, n, p, ts):
    """In ax, against t (the array ts): the true tail P(mean >= p + t) for the mean of n Bernoulli(p), and the bounds
    of Markov, Chebyshev and (one-sided) Hoeffding; log scale for the probabilities, and a legend."""
    raise NotImplementedError("quatre ax.plot(ts, ...), ax.set_yscale(\\"log\\"), ax.legend()")''',
    check='''with checked("M11.24 figure"):
    fig, ax = plt.subplots(figsize=(6.5, 4))
    try:
        created = drawn(draw_24, ax, 50, 0.3, np.linspace(0.011, 0.491, 49))
    except BaseException:
        plt.close(fig)
        raise
    if created:
        plt.close(fig)
        print("❌ Ex M11.24 : draw_24 ouvre sa propre figure : dessine dans l'axe reçu.")
    else:
        ax.set_xlabel("écart t")
        plt.show()''',
    solution='''def draw_24(ax, n, p, ts):
    """In ax, against t (the array ts): the true tail P(mean >= p + t) for the mean of n Bernoulli(p), and the bounds
    of Markov, Chebyshev and (one-sided) Hoeffding; log scale for the probabilities, and a legend."""
    ts = np.asarray(ts, dtype=float)
    true_tail = [float(stats.binom.sf(math.ceil(n * (p + t) - 1e-9) - 1, n, p)) for t in ts]
    ax.plot(ts, true_tail, color="black", linewidth=2, label="vraie queue")
    ax.plot(ts, p / (p + ts), label="Markov")
    ax.plot(ts, np.minimum(1.0, p * (1 - p) / (n * ts ** 2)), label="Tchebychev")
    ax.plot(ts, np.exp(-2 * n * ts ** 2), label="Hoeffding")
    ax.set_yscale("log")
    ax.set_ylabel("P(moyenne >= p + t)")
    ax.legend()


fig, ax = plt.subplots(figsize=(6.5, 4))
draw_24(ax, 50, 0.3, np.linspace(0.011, 0.491, 49))
ax.set_xlabel("écart t")
plt.show()''',
    after=[("md", "**Vérifications automatiques** (sur d'autres valeurs, dans des axes neufs)."),
           ("code", M11_24_CHECK)],
    note=r"Pour $n = 50$ et $p = 0{,}3$ : Hoeffding est la meilleure des trois bornes presque partout ; seuls les très "
         r"petits écarts ($t < 0{,}033$ environ) laissent Markov devant, et Tchebychev n'est ici jamais la meilleure "
         r"(elle l'emporte quand la variance est petite, M11.21 b). La vraie queue et la borne de Hoeffding ont toutes deux, en échelle "
         r"log, la forme d'une parabole en $t$ (un exposant en $t^2$) ; Markov et Tchebychev, des courbes en "
         r"$\frac{1}{t}$ et $\frac{1}{t^2}$, décroissent trop lentement.",
)

M11_25_MISTAKES = bug_letters_mistakes(
    "BEF", "ACD",
    {"B": "Markov demande une variable positive : les variations quotidiennes peuvent-elles être négatives ?",
     "E": "les variations sont dans [−5, 5], pas dans [0, 1] : que devient (b − a)² ?",
     "F": "un rayon de Hoeffding est une racine carrée : regarde ce que calcule la ligne"},
    name_correct=False)

M11_25 = Ex(
    "M11.25", "🐛", 1, 15, "Chasse à l'erreur : Markov pour une variable négative, Hoeffding sans bornes, un rayon "
    "sans racine", "repérer dans du code trois erreurs classiques sur les inégalités de concentration, et calculer ce "
    "qu'elles coûtent.", "fiche §4 à §6", tracks="C",
    body=r"""Un collègue a écrit le code ci-dessous pour les variations quotidiennes $x_i$ d'un indicateur, dont on sait qu'elles sont toujours comprises entre $-5$ et $5$ (elles peuvent être négatives). Trois lignes ne calculent pas ce que dit leur commentaire. **Sans exécuter de code**, trouve-les.

```python
def report_25(x, threshold, t, delta):
    '''Bounds for n daily changes x, each known to lie in [-5, 5], independent.'''
    n = len(x)
    mean = float(np.mean(x))                                   # (A) the sample mean
    markov = min(1.0, mean / threshold)                        # (B) a bound on P(X >= threshold) for one change X
    variance = float(np.var(x))                                # (C) the sample variance, an estimate of V(X)
    chebyshev = min(1.0, variance / (n * t ** 2))              # (D) a bound on P(|mean - mu| >= t), V(X) estimated
    hoeffding = min(1.0, 2 * math.exp(-2 * n * t ** 2))        # (E) a bound on P(|mean - mu| >= t)
    radius = 10 * math.log(2 / delta) / (2 * n)                # (F) the Hoeffding radius at risk delta
    return markov, chebyshev, hoeffding, radius
```

Questions :
- a) les lettres des lignes fausses, dans l'ordre alphabétique (un texte) ;
- b) la vraie borne de Hoeffding sur $P(\lvert \bar{X} - \mu \rvert \ge 0{,}5)$ pour $n = 400$ variations (4 décimales) ;
- c) le vrai rayon de Hoeffding pour $n = 400$ et $\delta = 0{,}05$ (4 décimales) ;
- d) ce que rend la ligne (F) **telle quelle** pour $n = 400$ et $\delta = 0{,}05$ (4 décimales).

Dans ta copie : corrige les trois lignes. Que vaudrait `markov` pour des variations de moyenne $-0{,}2$, et pourquoi ce nombre n'est-il une borne de rien ? Le rayon faux de d) est-il trop grand ou trop petit, et qu'est-ce que cela fait croire ?""",
    todo='''answer_M11_25a = ...  # a) letters, as text
answer_M11_25b = ...  # b) a number (4 decimals)
answer_M11_25c = ...  # c) a number (4 decimals)
answer_M11_25d = ...  # d) a number (4 decimals)''',
    check='''wbm.check("M11.25a", answer_M11_25a)
wbm.check("M11.25b", answer_M11_25b)
wbm.check("M11.25c", answer_M11_25c)
wbm.check("M11.25d", answer_M11_25d)''',
    solution='''n_25, t_25, delta_25, width_25 = 400, 0.5, 0.05, 10.0          # the changes lie in [-5, 5]: b - a = 10
answer_M11_25a = "BEF"
answer_M11_25b = min(1.0, 2 * math.exp(-2 * n_25 * t_25 ** 2 / width_25 ** 2))   # (E) corrected: (b - a)² = 100
answer_M11_25c = width_25 * math.sqrt(math.log(2 / delta_25) / (2 * n_25))       # (F) corrected: the square root
answer_M11_25d = 10 * math.log(2 / delta_25) / (2 * n_25)                        # (F) as written
print(answer_M11_25a, round(answer_M11_25b, 4), round(answer_M11_25c, 4), round(answer_M11_25d, 4))''',
    record=f'''wbm.record("M11.25a", "BEF",
           mistakes={M11_25_MISTAKES})
wbm.record("M11.25b", 2 * math.exp(-2.0), decimals=4,
           mistakes={{"les variations sont dans [−5, 5] : divise l'exposant par (b − a)² = 100": 2 * math.exp(-200.0)}})
wbm.record("M11.25c", 10 * math.sqrt(math.log(40) / 800), decimals=4,
           mistakes={{"le rayon est multiplié par b − a = 10": math.sqrt(math.log(40) / 800),
                     "ln(2/δ) = ln 40, à diviser par 2n = 800, puis la racine": 10 * math.sqrt(math.log(20) / 800)}})
wbm.record("M11.25d", 10 * math.log(40) / 800, decimals=4,
           mistakes={{"la question demande ce que rend la ligne telle quelle, sans racine": 10 * math.sqrt(math.log(40) / 800)}})''',
    note=r"(B) Markov suppose $X \ge 0$ : pour des variations de moyenne $-0{,}2$, la ligne rend un nombre négatif, "
         r"qui n'est la borne d'aucune probabilité. Il faudrait l'appliquer à $X + 5 \ge 0$ : "
         r"$P(X \ge s) = P(X + 5 \ge s + 5) \le \frac{\mathbb{E}[X] + 5}{s + 5}$. (E) Pour des variables dans "
         r"$[-5, 5]$, l'exposant est divisé par $(b - a)^2 = 100$ : la ligne fausse donne $2e^{-200}$, une confiance "
         r"absurde. (F) Sans racine, le rayon vaut 0,046 au lieu de 0,68 : quinze fois trop petit, il fait croire à une "
         r"précision qu'on n'a pas. (D) est juste à une estimation près : elle remplace $\mathbb{V}(X)$ par la variance "
         r"de l'échantillon, ce que dit son commentaire.",
)

M11_26_CHECK = '''with checked("M11.26 vérifications"):
    test_markov_bound_on_ten_laws()                     # your test runs here first: ⏳ while it is not written
    reference_26 = wbm.load_mymath("ref")
    results = {
        "la vraie borne de Markov": (reference_26.concentration.markov_bound, True),
        "une borne deux fois trop petite": (markov_bound_half, False),
        "la queue d'une loi exponentielle prise pour la borne": (markov_bound_exp, False),
    }
    problems = []
    for what, (function, should_pass) in results.items():
        run = wbm.run_pytest(test_markov_bound_on_ten_laws, subject=function, name="markov_bound",
                             preamble="from scipy import stats", quiet=True)
        if "NameError" in run.output:
            problems.append("ton test utilise un nom défini hors de lui (NameError) : pytest l'exécute seul ; seuls "
                            "math, np, pytest, stats et markov_bound lui sont fournis")
            break
        if should_pass and not run.ok:
            problems.append(f"ton test échoue sur {what} : il refuse une fonction juste (lis print(run.output))")
        if not should_pass and run.failed == 0:
            problems.append(f"ton test passe sur {what} : il ne la voit pas ; ajoute une loi où Markov est presque "
                            f"atteinte (une loi à deux valeurs, comme une Bernoulli) ou une loi à queue lourde")
    if problems:
        print("❌ Ex M11.26 : à revoir : " + " ; ".join(problems) + ".")
    else:
        print("✅ Ex M11.26 : ton test accepte la vraie borne et attrape les deux fausses.")'''

M11_26 = Ex(
    "M11.26", "🛠️", 1, 15, "Un test paramétré qui vérifie l'inégalité de Markov sur dix lois",
    "écrire un test de propriété qui vérifie une borne sur plusieurs lois, et choisir des lois qui attrapent les "
    "fausses bornes.", "fiche §4 ; Ex M11.17", tracks="C",
    body=r"""Une borne se teste par sa **propriété** : elle doit rester au-dessus de la vraie probabilité, pour toute loi qui vérifie ses hypothèses. Écris `test_markov_bound_on_ten_laws()`, **sans argument**, qui vérifie, pour **dix lois positives** de `scipy.stats` (continues ou discrètes, gelées avec leurs paramètres, comme `stats.expon(scale=2)` ou `stats.bernoulli(0.3)`) et pour plusieurs seuils $a > 0$ chacune, que `markov_bound(law.mean(), a) >= P(X >= a)`, avec une petite tolérance (`1e-12`) et un message d'`assert` qui dit la loi et le seuil.

Attention : pour une loi discrète, `law.sf(a)` vaut $P(X > a)$ ; pour un seuil entier, $P(X \ge a)$ s'écrit `law.sf(a - 1)`, ou bien choisis des seuils non entiers (pour une loi à valeurs entières, $P(X \ge 2{,}5) = P(X > 2{,}5)$).

pytest exécute ta fonction de test **seule**, sans les autres cellules : seuls `math`, `np`, `pytest`, `stats` (`from scipy import stats`) et `markov_bound` lui sont fournis. La vérification la lance trois fois : sur la vraie borne de Markov, où elle doit **passer** ; puis sur `markov_bound_half` et `markov_bound_exp` (fournies), deux fausses bornes, où elle doit **échouer**.

Dans ta copie : quelle loi de ta liste attrape `markov_bound_half` ? Pourquoi une liste de lois « ordinaires » (exponentielle, uniforme, Poisson) peut-elle laisser passer une borne deux fois trop petite ?""",
    given='''markov_bound = wbm.load_mymath("ref").concentration.markov_bound   # the true bound, to run your test here


def markov_bound_half(mean, a):
    """A wrong Markov bound: two times too small."""
    return min(1.0, mean / (2 * a))


def markov_bound_exp(mean, a):
    """A wrong Markov bound: the tail of an exponential law of the same mean, exp(-a / mean)."""
    return math.exp(-a / mean) if mean > 0 else 0.0''',
    todo='''def test_markov_bound_on_ten_laws():
    """markov_bound(law.mean(), a) >= P(X >= a) for ten non-negative laws of scipy.stats and several thresholds."""
    raise NotImplementedError("dix lois positives, plusieurs seuils, un assert avec un message par cas")''',
    check=M11_26_CHECK,
    solution='''def test_markov_bound_on_ten_laws():
    """markov_bound(law.mean(), a) >= P(X >= a) for ten non-negative laws of scipy.stats and several thresholds."""
    laws = {
        "Bernoulli(0.3)": stats.bernoulli(0.3), "Bernoulli(0.9)": stats.bernoulli(0.9),
        "exponential, mean 2": stats.expon(scale=2), "uniform on [0, 4]": stats.uniform(0, 4),
        "Poisson 1.5": stats.poisson(1.5), "binomial (12, 0.4)": stats.binom(12, 0.4),
        "gamma (0.3, 5)": stats.gamma(0.3, scale=5), "lognormal (s = 1.5)": stats.lognorm(1.5),
        "Pareto (b = 1.2)": stats.pareto(1.2), "geometric (0.2)": stats.geom(0.2),
    }
    for name, law in laws.items():
        for a in (0.5, 0.999, 1.5, 3.7, 10.5, 40.5):
            tail = float(law.sf(a))      # thresholds that are not integers: sf(a) = P(X > a) = P(X >= a)
            bound = markov_bound(float(law.mean()), a)
            assert bound >= tail - 1e-12, f"{name}, a = {a}: bound {bound} below P(X >= a) = {tail}"
''' + "\n\n" + M11_26_CHECK,
    note=r"La loi de Bernoulli(0,9) au seuil 0,999 donne $P(X \ge 0{,}999) = 0{,}9$ et la borne $\frac{0{,}9}{0{,}999} "
         r"\approx 0{,}901$ : Markov y est presque atteinte (une loi à deux valeurs, 0 et presque le seuil), et la borne "
         r"deux fois trop petite tombe à 0,45, sous la vraie valeur. Les lois « ordinaires » ont des queues bien plus "
         r"légères que $\frac{\mathbb{E}[X]}{a}$ : même divisée par 2, une borne fausse reste au-dessus d'elles. La "
         r"loi de Pareto, à queue lourde, attrape `markov_bound_exp` : sa queue décroît comme une puissance de $a$, "
         r"plus lentement que l'exponentielle. Un bon test de propriété contient des **cas extrêmes**.",
)

M11_27_CHECK = '''with checked("M11.27"):
    n_27 = smallest_n_27()                   # ⏳ while smallest_n_27 is not written
    wbm.check("M11.27", int(n_27), computed=True)'''

M11_27 = Ex(
    "M11.27", "🏆", 3, 25, "Défi : la plus petite taille d'échantillon qui garantit une moyenne à ± 0,05 avec 99 %, "
    "vérifiée sur une loi défavorable", "calculer exactement la taille d'échantillon nécessaire pour une loi "
    "défavorable, et la comparer à la garantie de Hoeffding.", "fiche §5 et §6 ; Ex M11.22", tracks="C",
    body=r"""Pour des variables à valeurs dans $[0, 1]$, Hoeffding garantit $P(\lvert \bar{X} - \mu \rvert \ge 0{,}05) \le 0{,}01$ dès que $n \ge \frac{\ln 200}{2 \times 0{,}05^2} \approx 1\,059{,}7$, donc pour $n \ge 1\,060$, **quelle que soit** la loi. Est-ce beaucoup trop ? Regardons une loi défavorable : la loi de Bernoulli de paramètre $\frac{1}{2}$, celle dont la variance est la plus grande.

**Le défi.** Écris `smallest_n_27()`, qui rend le plus petit entier $n_0$ tel que, pour **tout** $n$ de $n_0$ à 3 000, la probabilité **exacte** $P\big(\lvert \bar{X} - \frac{1}{2} \rvert \ge 0{,}05\big)$ soit au plus 0,01, où $\bar{X}$ est la moyenne de $n$ variables de Bernoulli$(\frac{1}{2})$ indépendantes. Objectif : la valeur exacte. Deux pièges t'attendent : la probabilité n'est pas une fonction décroissante de $n$ (le nombre de valeurs possibles de $\bar{X}$ change avec $n$), et l'égalité $\lvert \frac{k}{n} - \frac{1}{2} \rvert = 0{,}05$ tombe souvent pile, là où les flottants arrondissent.

Ensuite, dans ta copie : compare ton $n_0$ à la garantie de Hoeffding (1 060) et à l'approximation normale ($n \approx (2{,}576 \times 0{,}5 / 0{,}05)^2 \approx 664$). Pourquoi Hoeffding demande-t-il plus ? Pour ton $n_0$, vérifie que la loi de Bernoulli de paramètre $p$ donne une probabilité plus petite pour $p$ = 0,3 ou 0,1 : pourquoi parle-t-on de loi « défavorable » ?""",
    todo='''def smallest_n_27():
    """The smallest n0 such that P(|mean - 1/2| >= 0.05) <= 0.01 for every n from n0 to 3000, for the mean of n
    independent Bernoulli(1/2) (exact binomial probabilities)."""
    raise NotImplementedError("pour chaque n, la probabilité exacte (stats.binom) ; puis le plus petit n0 qui marche "
                              "jusqu'à 3 000")''',
    check=M11_27_CHECK,
    solution='''def smallest_n_27():
    """The smallest n0 such that P(|mean - 1/2| >= 0.05) <= 0.01 for every n from n0 to 3000, for the mean of n
    independent Bernoulli(1/2) (exact binomial probabilities)."""
    probs = {}
    for n in range(1, 3001):
        k = np.arange(n + 1)
        far = 10 * np.abs(2 * k - n) >= n           # |k/n - 1/2| >= 0.05, written with integers only
        probs[n] = float(stats.binom.pmf(k, n, 0.5)[far].sum())
    n0 = 3000
    while n0 > 1 and probs[n0 - 1] <= 0.01:         # go down while the property still holds
        n0 -= 1
    return n0


n_27 = smallest_n_27()
print("n0 =", n_27, "; Hoeffding :", math.ceil(math.log(200) / (2 * 0.05 ** 2)))
for p in (0.5, 0.3, 0.1):
    k = np.arange(n_27 + 1)
    far = np.abs(k - n_27 * p) >= 0.05 * n_27 - 1e-9
    print(f"p = {p} : P(|mean - p| >= 0.05) = {stats.binom.pmf(k, n_27, p)[far].sum():.5f}")
''' + "\n" + M11_27_CHECK,
    record='''wbm.record("M11.27", 681,
           mistakes={"c'est la première taille où la probabilité passe sous 1 % ; elle remonte au-dessus pour des n plus "
                     "grands : vérifie tous les n jusqu'à 3 000": 651,
                     "l'égalité |k/n − 1/2| = 0,05 tombe sur des flottants arrondis : compare des entiers, "
                     "10 |2k − n| >= n": 679,
                     "c'est la garantie de Hoeffding, valable pour toute loi ; le défi demande la valeur exacte pour la "
                     "loi de Bernoulli(1/2)": {1059, 1060},
                     "c'est l'approximation normale ; le défi demande la probabilité exacte": {663, 664}})''',
    note=r"$n_0 = 681$. La probabilité exacte passe une première fois sous 1 % à $n = 651$, puis remonte au-dessus "
         r"pour plusieurs $n$ (665, 667, 669, 678 et 680 : ceux où un $k$ tombe pile sur la frontière) ; la "
         r"comparaison en flottants rate une partie de ces frontières et donne 679. Hoeffding (1 060) demande plus de "
         r"1,5 fois plus d'exemples : elle doit valoir pour toutes les lois de $[0, 1]$ et pour tout $n$, avec une "
         r"marge de sécurité. Pour $p = 0{,}3$ ou $0{,}1$, la variance $p(1 - p)$ est plus petite, et la probabilité "
         r"d'un écart de 0,05 aussi : Bernoulli($\frac{1}{2}$) est la loi la plus dispersée de $[0, 1]$ parmi celles "
         r"de moyenne $\frac{1}{2}$, d'où « défavorable ».",
)

PART_A = Part("A", "Ta librairie : les bornes de Markov, de Tchebychev et de Hoeffding",
              "Fiche §4 à §6. Les cinq fonctions de `mymath/concentration.py`.",
              given=TOOLS, exercises=[M11_17, M11_18, M11_19])

PART_B = Part("B", "Les vraies queues, une prédiction et deux simulations",
              "Fiche §4 à §7. `scipy.stats` contre les bornes, la borne qui gagne, la décroissance exponentielle, et la "
              "probabilité que Thompson choisisse une option.",
              exercises=[M11_20, M11_21, M11_22, M11_23])

PART_C = Part("C", "Une figure, des erreurs classiques, un test et un défi",
              "Fiche §4 à §6. Les trois bornes sur une figure, trois erreurs à trouver, un test de propriété, puis la "
              "taille d'échantillon exacte d'une loi défavorable.",
              exercises=[M11_24, M11_25, M11_26, M11_27])

PARTS = [PART_A, PART_B, PART_C]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | M11.1 à M11.10, M11.14 | Les exercices papier (vérification) | ✏️ 🔗 | | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | "
                        f"{ex.minutes} |")
    if kind == "exercise":
        title = "# M11 · Logique, induction et inégalités de concentration — notebook d'exercices"
        how = ("La partie 0 vérifie tes exercices papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/m11_logique_concentration/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py M11`) ; la version du dépôt est mise à jour par Claude. Sur Colab, le "
               "badge ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme "
               "l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# M11 · Logique, induction et inégalités de concentration — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier tes calculs papier (partie 0) : tables de vérité, quantificateurs, ensembles, taux de base, "
               "Markov, Tchebychev, Hoeffding, bonus d'UCB, ε-greedy.\n"
               "- Écrire les cinq fonctions de `mymath/concentration.py` et les tester.\n"
               "- Calculer de vraies queues avec `scipy.stats`, prédire quelle borne gagne, simuler des écarts et des "
               "tirages de Thompson, dessiner les bornes, chasser trois erreurs, écrire un test, relever un défi.\n\n"
               r"**Rappel express.** Valide : aucune ligne « prémisses vraies, conclusion fausse » ; Markov "
               r"$P(X \ge a) \le \frac{\mathbb{E}[X]}{a}$ ($X \ge 0$) ; Tchebychev $P(\lvert X - \mu \rvert \ge t) \le "
               r"\frac{\sigma^2}{t^2}$, et $\frac{\sigma^2}{nt^2}$ pour une moyenne ; Hoeffding $P(\lvert \bar{X} - \mu "
               r"\rvert \ge t) \le 2e^{-2nt^2/(b - a)^2}$ ; rayon $(b - a)\sqrt{\ln(2/\delta)/(2n)}$ ; regret "
               r"$\sum_k \Delta_k\,\mathbb{E}[N_k(T)]$ ; bonus d'UCB1 $\sqrt{2\ln t / N}$.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu décider par une table de vérité si un argument est valide, et nier une phrase quantifiée ?\n"
               "2. Sais-tu traduire une phrase en inclusion d'ensembles, et trouver un contre-exemple ?\n"
               "3. Sais-tu repérer et chiffrer un piège d'induction (taux de base, échantillon biaisé) ?\n"
               "4. Sais-tu démontrer Markov et Tchebychev, et en tirer une taille d'échantillon ?\n"
               "5. Sais-tu calculer un rayon de Hoeffding, et dire ce que l'inégalité suppose ?\n"
               "6. Sais-tu expliquer d'où vient le bonus d'UCB, et pourquoi ε-greedy à ε fixé a un regret linéaire ?\n\n"
               "**La suite** : le chapitre 11 de workbookIA (apprentissage et raisonnement, puis un agent qui apprend "
               "par essais et récompenses), puis CP2, l'examen blanc de la partie II.")]


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
