#!/usr/bin/env python
"""Build the two notebooks of the mock exam CP0 from a single source (used by Claude).

    python tools/chapters/build_cp0.py
    python tools/run_all_notebooks.py checkpoints/partie_0/03_examen_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py checkpoints/partie_0/02_examen_notebook.ipynb

The exam of CP0 is on paper only (01_examen_sujet.md): the exam notebook is the check done AFTER the exam. The learner
reports the values written on the answer sheet; nothing is checked while EXAM_OVER is False, so that « Run all » goes
to the end. Wrong-answer messages state a rule, never the calculation that gives the answer. The solutions notebook
records the answers, computed from the numbers of the statements (cells tagged `answer`, read by build_answers.py).
Adapted from the checkpoint builders of workbookIA (part B of its exam notebooks); the questions are original.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import Paper, check_unique_keys, md  # noqa: E402
from nbbuild import badge, code, setup_cell, write_notebook  # noqa: E402

FOLDER = "checkpoints/partie_0"
EXAM = f"{FOLDER}/02_examen_notebook.ipynb"
SOLUTIONS = f"{FOLDER}/03_examen_solutions.ipynb"

F = 'kind="fraction", simplified=True'
FRACTION = "an irreducible fraction, as text"

PAPER_CONTEXT = r'''# Part B: the answers are computed from the numbers of the statements (01_examen_sujet.md)
import math
from fractions import Fraction

import sympy as sp

P_C, P_V = 0.7, 0.3                       # CP0.7: share of the parcels sent by van and by bike
LATE_C, LATE_V = 0.04, 0.08               # late rate of each way
P_R = P_C * LATE_C + P_V * LATE_V         # probability of a late parcel (total probability)
E_X = (1 - P_R) * 2 + P_R * (-10)         # gain: +2 for a parcel on time, -10 for a late one
V_X = (1 - P_R) * 2 ** 2 + P_R * (-10) ** 2 - E_X ** 2'''

PAPER = [
    Paper("CP0.1", "Fractions, puissances et notation scientifique", [
        ("a", FRACTION, "Fraction(7, 4) - Fraction(5, 6) / Fraction(4, 9)",
         F + ', mistakes={"la division passe avant la soustraction (les priorités)": "33/16", '
         '"diviser par une fraction, c\'est multiplier par son inverse": "149/108"}'),
        ("b", FRACTION, "Fraction(5) ** 4 * Fraction(25) ** -3 / Fraction(5) ** -1",
         F + ', mistakes={"écris tout avec des puissances de 5 : 25 est une puissance de 5": "25", '
         '"diviser par une puissance d\'exposant négatif, c\'est multiplier par la puissance opposée": "1/125"}'),
        ("c", "[a, n]", "[2.8, 4]",
         'decimals=1, mistakes={"en notation scientifique, 1 ≤ a < 10": [28, 3], '
         '"multiplier des puissances de 10, c\'est additionner leurs exposants": [2.8, -40]}'),
        ("d", "[a, n]", "[6, 3]",
         'decimals=1, mistakes={"diviser des puissances de 10, c\'est soustraire les exposants, avec leurs signes": '
         '[6, -11], "on soustrait l\'exposant du dénominateur à celui du numérateur, pas l\'inverse": [6, -3], '
         '"en notation scientifique, 1 ≤ a < 10": [0.6, 4]}'),
        ("e", "a number (a percentage, negative for a decrease)", "-10.0",
         'decimals=1, mistakes={"des évolutions successives ne s\'additionnent pas : multiplie leurs coefficients": -5, '
         '"c\'est le coefficient multiplicateur ; l\'énoncé demande l\'évolution en pourcentage": 0.9, '
         '"c\'est l\'évolution en proportion ; l\'énoncé la demande en pourcentage": -0.1}'),
    ]),
    Paper("CP0.2", "Développer, factoriser, résoudre", [
        ("a", 'an expression in x, expanded (between quotes, "x**2" for x²)', '"8*x**2 + 2*x - 5"',
         'kind="expr", variables=("x",), expanded=True, mistakes={"un signe moins devant une parenthèse change '
         'tous les signes qu\'elle contient": "8*x**2 - 2*x - 3", "(a − b)² = a² − 2ab + b²": "8*x**2 - 5"}'),
        ("b", "a list, in increasing order", "[0, 7]",
         'mistakes={"diviser les deux membres par x fait perdre une solution : factorise": [7]}'),
        ("c", FRACTION, "Fraction(-3, 8)",
         F + ', mistakes={"développe −3(2x − 1) en gardant les deux signes : (−3) × (−1) = +3": "-9/8"}'),
        ("d", 'an interval, as text (like "]2 ; +oo[")', '"]-oo ; -3["',
         'kind="interval", mistakes={"diviser par un nombre négatif change le sens de l\'inégalité": "]-3 ; +oo[", '
         '"une inégalité stricte n\'atteint pas sa borne : crochet ouvert": "]-oo ; -3]"}'),
        ("e", "an interval, as text", '"[-1 ; 7]"',
         'kind="interval", mistakes={"|x − 3| est la distance de x à 3 : les solutions sont autour de 3": "[-7 ; 1]", '
         '"avec ≤, les bornes sont atteintes : crochets fermés": "]-1 ; 7["}'),
    ]),
    Paper("CP0.3", "Un système 2 × 2 et sa lecture graphique", [
        ("a", "[x, y]", "[2, 3]",
         'mistakes={"vérifie ta solution dans les deux équations, dans l\'ordre [x, y]": [3, 2]}'),
        ("b", "a number", "3 * (-2) - 1 * 1",
         'mistakes={"le déterminant vaut ad − bc : on soustrait le second produit": -5}'),
        ("c", FRACTION, "Fraction(1, 2)",
         F + ', mistakes={"isole y, puis divise par son coefficient": "2", '
         '"isole y en gardant les signes : passe x de l\'autre côté": "-1/2"}'),
        ("d", "[m, p]", "[2, -2]",
         'mistakes={"la pente est l\'écart des ordonnées divisé par l\'écart des abscisses": [0.5, -2], '
         '"p est l\'ordonnée du point où la droite coupe l\'axe vertical": [2, 1]}'),
        ("e", "[x, y], 1 decimal", "[2.2, 2.4]",
         'decimals=1, mistakes={"c\'est le point commun à D1 et D2 ; prends l\'équation de D3 trouvée en d)": [2, 3]}'),
        ("f", "1, 2 or 3", "3",
         'choices=[1, 2, 3], mistakes={"compare les deux équations : l\'une est-elle un multiple de l\'autre ?": 1}'),
    ]),
    Paper("CP0.4", "Second degré : racines et sommet", [
        ("a", "a number", "(-6) ** 2 - 4 * (-1) * 7",
         'mistakes={"Δ = b² − 4ac, avec les signes de a et de c": 8}'),
        ("b", "a list, in increasing order", "[-7, 1]",
         'mistakes={"le dénominateur de la formule est 2a, avec le signe de a": [-1, 7]}'),
        ("c", "[x, y]", "[-3, 16]",
         'mistakes={"l\'abscisse du sommet est −b/(2a), avec les deux signes": [3, -20]}'),
        ("d", "an interval, as text", '"]-7 ; 1["',
         'kind="interval", mistakes={"a < 0 : la parabole est tournée vers le bas, f est positive entre ses racines": '
         '"]-oo ; -7[ U ]1 ; +oo[", "f(x) > 0 est strict : les racines sont exclues": "[-7 ; 1]"}'),
        ("e", "a number", "0",
         'mistakes={"compare 20 à la plus grande valeur que prend f (l\'ordonnée du sommet)": 2}'),
        ("f", "a number", "7",
         'mistakes={"le sommet n\'est pas dans [0 ; 2] : regarde le sens de variation de f sur cet intervalle": 16, '
         '"f est décroissante sur [0 ; 2] : sa plus grande valeur est au bord gauche": -9}'),
    ]),
    Paper("CP0.5", "Exponentielle et logarithme", [
        ("a", "a number", "0.0",
         'decimals=2, mistakes={"ln a − ln b = ln(a/b) et ln a + ln b = ln(ab), pas ln(a − b) ni ln(a + b)": '
         'math.log(12 - 3 + 1 / 4)}'),
        ("b", 'an exact value, as text (with ln)', "(sp.log(3) + 5) / 2",
         'kind="exact", mistakes={"isole 2x avant de diviser : ajoute 5 aux deux membres": "(log(3) - 5)/2", '
         '"divise tout le membre de droite par 2, pas seulement ln 3": "log(3)/2 + 5"}'),
        ("c", "a number (2 decimals)", "(math.e + 3) / 4",
         'decimals=2, mistakes={"ln(4x − 3) = 1 équivaut à 4x − 3 = e : la réciproque de ln est exp": 0.75, '
         '"isole x en gardant les signes : ajoute 3, puis divise par 4": (math.e - 3) / 4}'),
        ("d", "a number", "2.0",
         'decimals=2, mistakes={"log a + log b = log(ab), pas log(a + b)": math.log10(52)}'),
        ("e", FRACTION, "Fraction(4, 5)",
         F + ', mistakes={"la sigmoïde contient e^(−z), avec un signe moins : e^(−ln a) = 1/a": "1/5"}'),
    ]),
    Paper("CP0.6", "Dériver et étudier les variations", [
        ("a", "an expression in x (between quotes)", '"3*x**2 - 12"',
         'kind="expr", variables=("x",), mistakes={"la dérivée d\'une constante est nulle": "3*x**2 - 7"}'),
        ("b", "a list, in increasing order", "[-2, 2]",
         'mistakes={"un carré égal à 4 : deux solutions, opposées": [2]}'),
        ("c", "[maximum, minimum]", "[21, -11]",
         'mistakes={"l\'ordre demandé : le maximum local d\'abord": [-11, 21], '
         '"ce sont les abscisses ; la question demande les valeurs de f": [-2, 2]}'),
        ("d", "an interval, as text", '"[-2 ; 2]"',
         'kind="interval", mistakes={"f\' est un trinôme de coefficient positif : elle est négative entre ses '
         'racines": "]-oo ; -2] U [2 ; +oo[", "f\' ne s\'annule qu\'aux bornes : le plus grand intervalle les '
         'contient, crochets fermés": "]-2 ; 2["}'),
        ("e", "[m, p]", "[-9, 3]",
         'mistakes={"la tangente : y = f\'(a)(x − a) + f(a) ; développe pour lire p": [-9, -6]}'),
        ("f", "an expression in x (exp(-x) for e^(-x))", '"(2*x - x**2)*exp(-x)"',
         'kind="expr", variables=("x",), mistakes={"la dérivée d\'un produit est u\'v + uv\', pas u\'v\'": '
         '"-2*x*exp(-x)", "la dérivée de e^(−x) est −e^(−x) (règle de la chaîne)": "(2*x + x**2)*exp(-x)"}'),
        ("g", "an expression in x", '"-3/(x - 2)**2"',
         'kind="expr", variables=("x",), mistakes={"(u/v)\' = (u\'v − uv\')/v² : l\'ordre des termes compte": '
         '"3/(x - 2)**2", "la dérivée d\'un quotient n\'est pas le quotient des dérivées": "1"}'),
        ("h", "a number", "3",
         'mistakes={"utilise le tableau de variations : compare à 0 le maximum local, le minimum local et les limites '
         'en ±∞": 2, "f(x) = 0 peut avoir une solution sur chaque intervalle où f est monotone : regarde le signe de f '
         'aux deux extrema": 1}'),
    ]),
    Paper("CP0.7", "Un arbre de probabilités et une espérance", [
        ("a", "a number (3 decimals)", "P_R",
         'decimals=3, mistakes={"multiplie les probabilités le long de chaque branche, puis additionne": '
         'LATE_C + LATE_V, "pondère chaque taux de retard par la part des colis concernés": (LATE_C + LATE_V) / 2}'),
        ("b", "a number (3 decimals)", "P_V * LATE_V",
         'decimals=3, mistakes={"P(V ∩ R) = P(V) × P(R sachant V) : n\'oublie pas la première branche": LATE_V}'),
        ("c", "a number (4 decimals)", "1 - (1 - P_R) ** 2",
         'decimals=4, mistakes={"les probabilités ne s\'additionnent pas ici : passe par l\'événement contraire": '
         '2 * P_R, "c\'est la probabilité que les deux colis soient en retard": P_R ** 2}'),
        ("d", "a number (2 decimals)", "E_X",
         'decimals=2, mistakes={"pondère chaque gain par sa probabilité": (2 + (-10)) / 2}'),
        ("e", "a number (2 decimals)", "V_X",
         'decimals=2, mistakes={"V(X) = E[X²] − E[X]² : retranche le carré de l\'espérance": V_X + E_X ** 2, '
         '"V(X) = E[X²] − E[X]² : c\'est le CARRÉ de l\'espérance qu\'on retranche": V_X + E_X ** 2 - E_X}'),
        ("f", "a number (2 decimals)", "2 * E_X - 1",
         'decimals=2, mistakes={"E[aX + b] = a E[X] + b : n\'oublie pas la constante": 2 * E_X}'),
    ]),
    Paper("CP0.8", "Vecteurs, produit scalaire, angle", [
        ("a", "a list", "[3 - (-3), -3 - 1]",
         'mistakes={"les coordonnées d\'un vecteur : arrivée moins départ": [-6, 4]}'),
        ("b", "a number (2 decimals)", "math.sqrt(6 ** 2 + 4 ** 2)",
         'decimals=2, mistakes={"la distance est la racine carrée de la somme des carrés des écarts": 52, '
         '"élève les écarts au carré avant de les additionner": 10}'),
        ("c", "a number", "6 * 3 + (-4) * 2",
         'mistakes={"multiplie les coordonnées de même rang, avec leurs signes": 26}'),
        ("d", FRACTION, "Fraction(10, 26)",
         F + ', mistakes={"divise le produit scalaire par le produit des DEUX normes": "10/13"}'),
        ("e", "a number (1 decimal)", "math.degrees(math.acos(5 / 13))", 'decimals=1'),
    ]),
    Paper("CP0.10", "Corriger une copie : cinq erreurs (les lettres seulement)", [
        ("a", 'the letters, as text (like "ABCDE")', '"BCEFH"', ""),
    ]),
    Paper("CP0.11", "Une somme écrite avec Σ et une somme géométrique", [
        ("a", "a number", "sum(k ** 2 - 1 for k in range(1, 5))",
         'mistakes={"le − 1 est dans chaque terme : il compte autant de fois qu\'il y a de termes": 29}'),
        ("b", "a number", "5 * (2 ** 5 - 1) // (2 - 1)",
         'mistakes={"compte les termes : k va de 0 à 4": 75}'),
        ("c", "a number", "(12 - 4 + 1) * 3",
         'mistakes={"de k = 4 à k = 12 : compte les termes, bornes comprises": 24}'),
        ("d", FRACTION, "1 / (1 - Fraction(2, 5))",
         F + ', mistakes={"le premier terme (k = 0) vaut 1 : la somme vaut 1/(1 − q)": "2/3"}'),
        ("e", "a number", "math.prod(3 ** k for k in range(1, 4))",
         'mistakes={"Π multiplie les termes ; c\'est Σ qui les additionne": 3 + 9 + 27}'),
    ]),
    Paper("CP0.12", "Problème de synthèse : étudier une fonction de coût donnée par une formule", [
        ("a", "a number", "round(math.exp(0) - 2 * 0)", 'mistakes={"e⁰ = 1": 0}'),
        ("b", "an expression in w (exp(w) for e^w)", '"exp(w) - 2"',
         'kind="expr", variables=("w",), mistakes={"dérive aussi le terme −2w": "exp(w) - 2*w"}'),
        ("c", "an exact value, as text (with log or ln)", "sp.log(2)",
         'kind="exact", mistakes={"eʷ = 2 : on prend le logarithme népérien des deux membres": "2", '
         '"la réciproque de l\'exponentielle est le logarithme népérien": "exp(2)"}'),
        ("d", "a number (3 decimals)", "2 - 2 * math.log(2)",
         'decimals=3, mistakes={"e^(ln a) = a : remplace w par w* dans les deux termes": 1 - 2 * math.log(2)}'),
        ("e", "an interval, as text", '"]-oo ; log(2)]"',
         'kind="interval", mistakes={"L\' est négative avant w* : L décroît, puis croît": "[log(2) ; +oo[", '
         '"L\' ne s\'annule qu\'en w* : le plus grand intervalle le contient, crochet fermé": "]-oo ; log(2)["}'),
        ("f", 'a number, or "+oo"', "math.inf",
         'decimals=2, mistakes={"croissances comparées : eʷ l\'emporte sur 2w": -math.inf}'),
        ("g", "[m, p]", "[-1, 1]",
         'mistakes={"la tangente en 0 : y = L\'(0) w + L(0)": [-1, 0]}'),
        ("h", "True or False", "True",
         'mistakes={"compare à 0 la plus petite valeur de L, trouvée en d)": False}'),
    ]),
]

HELPERS = r'''EXAM_OVER = False   # set it to True once your exam is finished, then run the cells below

RESULTS = {}        # sub-ID -> result of wbm.check
_REMINDED = []      # the full reminder is printed once, then a short one


def exam_over():
    """True once the exam is finished; otherwise print a reminder (and the cell checks nothing)."""
    if not EXAM_OVER:
        print("⏸️ Rien n'est vérifié (EXAM_OVER vaut False)." if _REMINDED else
              "⏸️ Vérification après l'examen : passe EXAM_OVER à True dans cette cellule, puis exécute-la.")
        _REMINDED.append(True)
        return False
    if "wbm" not in globals():
        print("⚠️ Exécute d'abord la cellule de configuration, tout en haut du notebook.")
        return False
    return True'''

SUMMARY = r'''# Summary of the automatic checks
import re


def natural(sub_id):
    """CP0.2a before CP0.10a: the question number as a number, then the letter."""
    number, letter = re.match(r"CP0\.(\d+)(.*)", sub_id).groups()
    return int(number), letter


if exam_over():
    done = {k: r for k, r in RESULTS.items() if r.status != "pending"}
    right = sorted((k for k, r in done.items() if r), key=natural)
    wrong = sorted((k for k, r in done.items() if not r), key=natural)
    pending = sorted((k for k, r in RESULTS.items() if r.status == "pending"), key=natural)
    print(f"Réponses vérifiées : {len(right)} juste(s) sur {len(done)} ; pas remplies : {len(pending)}.")
    if wrong:
        print("À revoir avec le corrigé :", ", ".join(wrong))
    print("Note ensuite ta copie avec le barème de 03_examen_corrige.md : il donne aussi les points des démarches, "
          "des justifications et des questions rédigées, que cette vérification ne voit pas.")'''

INTRO = r'''## Après l'examen : vérification automatique

**Ne commence qu'une fois ta copie terminée**, examen rendu. Ce notebook vérifie les réponses que tu as écrites sur ta feuille, question par question : ✅ juste, ❌ faux (avec une piste), ⏳ pas rempli. Il ne note pas : les démarches, les justifications, le quiz CP0.Q1, la démonstration CP0.9 et les corrections de CP0.10 b) se corrigent avec `03_examen_corrige.md`, qui donne aussi le barème.

1. Passe `EXAM_OVER` à `True` dans la cellule ci-dessous, puis exécute-la.
2. Reporte chaque réponse de ta feuille : **la valeur** que tu as écrite, pas un nouveau calcul (sinon tu ne vérifies plus ta copie). Laisse `...` pour une question que tu n'as pas faite.
3. Les formes d'écriture : en Python, le séparateur décimal est un **point** (`2.5`) ; une fraction, une valeur exacte, une expression et un intervalle s'écrivent **entre guillemets** (`"-7/3"`, `"sqrt(5)/3"`, `"2*x**2 - 1"`, `"]-oo ; 0]"`) ; une liste entre crochets, sans guillemets (`[-1.5, 4]`) ; vrai ou faux par `True` ou `False`.'''


def paper_cell(kind: str, paper: Paper) -> list:
    """One question: the answers and a guarded wbm.check (exam), or the wbm.record cell (solutions)."""
    cells = [md(f"**{paper.id} — {paper.title}**")]
    stem = f"answer_{paper.id.replace('.', '_')}"
    if kind == "exercise":
        lines = [f"# {paper.id}: the values written on your answer sheet"]
        lines += [f"{stem}{letter} = ...  # {letter}) {hint}" for letter, hint, _, _ in paper.subs]
        names = ", ".join(f"{stem}{letter}" for letter, *_ in paper.subs)
        lines += ["", "if exam_over():",
                  f"    for letter, answer in zip(\"{paper.letters}\", [{names}]):",
                  f"        RESULTS[f\"{paper.id}{{letter}}\"] = wbm.check(f\"{paper.id}{{letter}}\", answer)"]
        cells.append(code("\n".join(lines)))
    else:
        lines = []
        for letter, _, expr, options in paper.subs:
            args = f", {options}" if options else ""
            lines.append(f'wbm.record("{paper.id}{letter}", {expr}{args})')
        source = "\n".join(lines)
        check_unique_keys(source, paper.id)
        cells.append(code(source, tags=["answer"]))
    return cells


def header_cells(kind: str) -> list:
    rel = EXAM if kind == "exercise" else SOLUTIONS
    if kind == "exercise":
        title = "# CP0 · Examen blanc de la remise à niveau — vérification de ta copie"
        how = ("L'examen se fait **sur papier** (`01_examen_sujet.md`, 122 minutes, fiches fermées). Ce notebook ne "
               "sert qu'**après** : il vérifie les réponses chiffrées de ta copie. Ses cellules ne vérifient rien tant "
               "que `EXAM_OVER` vaut `False`, et « Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est "
               "rempli (⏸️).\n\n"
               "> Travaille dans **ta copie** (`mon_travail/checkpoints/partie_0/02_examen_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py CP0`) : ce fichier-ci est mis à jour par Claude. Sur Colab, le badge "
               "ouvre la version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme l'explique "
               "`00_setup/COLAB.md` §2.")
    else:
        title = "# CP0 · Examen blanc de la remise à niveau — solutions (notebook exécuté)"
        how = ("L'enregistrement des réponses que vérifie le notebook de l'examen (cellules marquées `answer`, "
               "récoltées par `tools/build_answers.py`), calculées à partir des nombres du sujet ; les erreurs "
               "classiques reçoivent un message qui dit où chercher. Le corrigé détaillé et le barème sont dans "
               "`03_examen_corrige.md`.")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell("demo"))
    if kind == "exercise":
        cells.append(md(INTRO))
        cells.append(code(HELPERS))
        for paper in PAPER:
            cells += paper_cell(kind, paper)
        cells.append(md("## Bilan"))
        cells.append(code(SUMMARY))
        cells.append(md("**Ce que cette vérification ne voit pas** : les démarches et les justifications ; le quiz "
                        "CP0.Q1 ; la démonstration CP0.9 ; les corrections de CP0.10 b) (seules les lettres de a) sont "
                        "vérifiées). Tout cela se corrige avec `03_examen_corrige.md`. Remplis ensuite le tableau de "
                        "ta note, à la fin de ta copie, puis fais la remédiation du corrigé."))
    else:
        cells.append(md("## Les réponses vérifiées après l'examen"))
        cells.append(code(PAPER_CONTEXT))
        for paper in PAPER:
            cells += paper_cell(kind, paper)
    return cells


def main() -> int:
    write_notebook(EXAM, build("exercise"))
    write_notebook(SOLUTIONS, build("solution"))
    n_checks = sum(len(p.subs) for p in PAPER)
    print(f"✅ {EXAM} and {SOLUTIONS} written ({len(PAPER)} questions, {n_checks} checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
