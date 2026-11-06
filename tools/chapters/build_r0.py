#!/usr/bin/env python
"""Build the two notebooks of chapter R0 from a single source (used by Claude).

    python tools/chapters/build_r0.py
    python tools/run_all_notebooks.py chapitres/r0_prise_en_main/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/r0_prise_en_main/03_notebook.ipynb

Part 0 checks the ✏️ paper exercise R0.1; parts A and B are the notebook exercises R0.3 to R0.9.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, bug_letters_mistakes, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "R0"
FOLDER = "chapitres/r0_prise_en_main"

# ---------------------------------------------------------------------------
# Part 0: the paper exercise R0.1 (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("R0.1", "Calculer avec Python : priorités, division entière et reste", [
        ("a", "5 + 2 * 3 ** 2", "5 + 2 * 3 ** 2",
         'mistakes={"** passe avant *, et * avant + : 3 ** 2 d\'abord": 441, "** passe avant * : 2 * 3 ** 2 = 2 × 9": 41}'),
        ("b", "(5 + 2) * 3 ** 2", "(5 + 2) * 3 ** 2",
         'mistakes={"les parenthèses d\'abord, puis ** avant * : 7 × 9": 441}'),
        ("c", "-4 ** 2", "-4 ** 2",
         'mistakes={"** passe avant le signe moins : -4 ** 2 se lit -(4 ** 2)": 16}'),
        ("d", "(-4) ** 2", "(-4) ** 2",
         'mistakes={"avec les parenthèses, c\'est (-4) qui est élevé au carré : moins par moins donne plus": -16}'),
        ("e", "29 // 6", "29 // 6", 'mistakes={"// donne le quotient entier, pas le reste": 5}'),
        ("f", "29 % 6", "29 % 6", 'mistakes={"% donne le reste, pas le quotient : 29 = 6 × 4 + 5": 4}'),
        ("g", "-29 // 6", "-29 // 6",
         'mistakes={"// arrondit vers le bas (vers moins l\'infini), pas vers zéro : -4,83… devient -5": -4}'),
        ("h", "-29 % 6", "-29 % 6",
         'mistakes={"le reste est toujours entre 0 et 5 : écris -29 = 6 × (-5) + r": -5}'),
        ("i", "4 ** 3 ** 0", "4 ** 3 ** 0",
         'mistakes={"les puissances se calculent de droite à gauche : 3 ** 0 d\'abord": 1}'),
        ("j", "10 / 4 * 2, as a float", "10 / 4 * 2",
         'decimals=1, mistakes={"/ et * se calculent de gauche à droite : (10 / 4) × 2": 1.25}'),
    ]),
]

PAPER_CONTEXT = "# Part 0 needs no data: the answers are the values Python prints for each expression."

PAPER_INTRO = ("## Partie 0 · Vérifier ton exercice papier (✏️ R0.1)\n\n"
               "Fais d'abord l'exercice R0.1 de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée "
               "(par exemple `23`), pas l'expression Python, sinon tu ne vérifies rien. Les réponses pas encore "
               "remplies affichent ⏳.")

# ---------------------------------------------------------------------------
# Part A: type, check, compute (R0.3 to R0.6)
# ---------------------------------------------------------------------------
PART_A_GIVEN = '''# Tools of the notebook (parts A and B)
import math
from fractions import Fraction

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.Symbol("x")'''

R0_3 = Ex(
    "R0.3", "📦", 1, 10, "Taper une fraction exacte, une expression et un intervalle",
    "taper chaque sorte de réponse comme `wbm.check` l'attend.",
    "fiche §3", tracks="C, E",
    body="""Calcule ou traduis chaque réponse **sur papier**, puis tape-la sous la bonne forme (fiche §3, tableau « Comment taper chaque sorte de réponse »).

| | Réponse demandée | Forme |
|---|---|---|
| a | $\\dfrac{3}{4} - \\dfrac{1}{6}$ | une fraction **irréductible**, entre guillemets |
| b | le carré de la somme de $x$ et de 3, moins 1 | une expression en $x$, entre guillemets |
| c | les réels strictement supérieurs à $-2$ et inférieurs ou égaux à 5 | un intervalle |
| d | les réels négatifs ou nuls | un intervalle |
| e | le nombre $\\pi$ arrondi à 3 décimales | un nombre (tape le nombre, pas `math.pi`) |""",
    todo='''answer_R0_3a = ...  # a) a fraction as text, e.g. "2/9"
answer_R0_3b = ...  # b) an expression in x, as text
answer_R0_3c = ...  # c) an interval, as text, e.g. "[0 ; 1["
answer_R0_3d = ...  # d) an interval, as text
answer_R0_3e = ...  # e) a number with 3 decimals''',
    check='''for letter, answer in zip("abcde", [answer_R0_3a, answer_R0_3b, answer_R0_3c, answer_R0_3d, answer_R0_3e]):
    wbm.check(f"R0.3{letter}", answer)''',
    record='''wbm.record("R0.3a", Fraction(3, 4) - Fraction(1, 6), kind="fraction", simplified=True,
           mistakes={"1/6 = 2/12 : le numérateur aussi est multiplié par 2": "2/3",
                     "on ne soustrait pas les numérateurs et les dénominateurs entre eux": "-1"})
wbm.record("R0.3b", "(x + 3)**2 - 1", kind="expr", variables=("x",),
           mistakes={"le carré porte sur toute la somme x + 3 : des parenthèses autour de x + 3": "x + 3**2 - 1",
                     "le « moins 1 » vient après le carré, hors des parenthèses": "(x + 3 - 1)**2"})
wbm.record("R0.3c", "]-2 ; 5]", kind="interval",
           mistakes={"« strictement supérieurs » : -2 est exclu, et « inférieurs ou égaux » : 5 est inclus": "[-2 ; 5[",
                     "-2 est exclu (« strictement »), crochet ouvert de ce côté-là": "[-2 ; 5]"})
wbm.record("R0.3d", "]-oo ; 0]", kind="interval",
           mistakes={"« ou nuls » : 0 est inclus, donc crochet fermé en 0": "]-oo ; 0[",
                     "« négatifs » : ce sont les nombres inférieurs à 0, pas supérieurs": "[0 ; +oo["})
wbm.record("R0.3e", math.pi, decimals=3,
           mistakes={"arrondir n'est pas tronquer : π = 3,14159…, la 4e décimale (5) fait monter la 3e": 3.141})''',
)

R0_4 = Ex(
    "R0.4", "🔮", 1, 10, "Prédire : 0,1 + 0,2 vaut-il 0,3 pour Python ?",
    "constater qu'un calcul en flottants est arrondi, et savoir comparer deux flottants.",
    "fiche §2 (lis « Les flottants » **après** l'exercice si tu ne l'as pas encore lue)", tracks="C, E",
    hypothesis=True,
    body="""**Avant d'exécuter quoi que ce soit**, prédis : pour Python, l'expression `0.1 + 0.2 == 0.3` vaut-elle `True` ou `False` ? Écris ta prédiction dans la cellule (un booléen, `True` ou `False`), vérifie-la, puis lance l'expérience.""",
    todo='''prediction_R0_4 = ...  # True or False, written BEFORE running the experiment below''',
    check='''wbm.check("R0.4a", prediction_R0_4)''',
    record='''wbm.record("R0.4a", 0.1 + 0.2 == 0.3, prediction=True)''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois ta prédiction écrite."),
        ("todo", guarded('''print("0.1 + 0.2         =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3  :", 0.1 + 0.2 == 0.3)
print("écart             =", 0.1 + 0.2 - 0.3)
print("math.isclose      :", math.isclose(0.1 + 0.2, 0.3))
print("avec des Fraction :", Fraction(1, 10) + Fraction(2, 10))''', ["prediction_R0_4"],
                          "⏳ Écris d'abord ta prédiction (prediction_R0_4 = True ou False), puis exécute à nouveau.")),
        ("solution", '''print("0.1 + 0.2         =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3  :", 0.1 + 0.2 == 0.3)
print("écart             =", 0.1 + 0.2 - 0.3)
print("math.isclose      :", math.isclose(0.1 + 0.2, 0.3))
print("avec des Fraction :", Fraction(1, 10) + Fraction(2, 10))'''),
        ("md", """**Après l'expérience**, lis les lignes affichées et réponds :
- b) l'écart s'affiche en notation scientifique, sous la forme `m e k`. Quel est l'entier $k$, c'est-à-dire la puissance de 10 de l'écart ?
- c) quelle est la valeur **exacte** de $\\frac{1}{10} + \\frac{2}{10}$ calculée avec `Fraction` ? Tape-la comme une fraction entre guillemets."""),
        ("todo", '''answer_R0_4b = ...  # b) an integer
answer_R0_4c = ...  # c) a fraction as text'''),
        ("check", '''wbm.check("R0.4b", answer_R0_4b)
wbm.check("R0.4c", answer_R0_4c)'''),
        ("record", '''wbm.record("R0.4b", math.floor(math.log10(0.1 + 0.2 - 0.3)),
           mistakes={"e-17 veut dire « fois 10 puissance -17 » : l'exposant est négatif": 17})
wbm.record("R0.4c", Fraction(1, 10) + Fraction(2, 10), kind="fraction",
           mistakes={"avec Fraction, le calcul est exact : 1/10 + 2/10 n'a pas d'erreur d'arrondi": "3/11"})'''),
    ],
    note="Retiens les deux remèdes : comparer avec une tolérance (`math.isclose`), ou calculer exactement avec `Fraction` "
         "quand les nombres sont des fractions.",
)

R0_5 = Ex(
    "R0.5", "📦", 1, 15, "Vérifier un développement avec SymPy (expand, simplify)",
    "utiliser SymPy pour vérifier un calcul fait à la main, sans le faire à sa place.",
    "fiche §4", tracks="C, E",
    body="""Un camarade a développé quatre expressions à la main :

| | Départ | Son résultat |
|---|---|---|
| a | $(x + 3)(x - 7)$ | $x^2 - 4x - 21$ |
| b | $(3x - 2)^2$ | $9x^2 - 4$ |
| c | $(x - 1)^3$ | $x^3 - 3x^2 + 3x - 1$ |
| d | $(x + 2)(x^2 - 2x + 4)$ | $x^3 - 8$ |

1. Avec `sp.expand`, trouve **lesquels sont justes** (la méthode de la fiche : la différence se développe-t-elle en 0 ?). Réponds par les lettres des résultats justes, dans l'ordre alphabétique, par exemple `"ab"`.
2. Donne le bon développement de b), sous forme d'expression.
3. Avec `sp.simplify`, simplifie $\\dfrac{x^2 - 4}{x + 2}$ et tape la forme simplifiée.

`x` est déjà une lettre SymPy (cellule des outils, partie A).""",
    todo='''# Your checks with sp.expand and sp.simplify (as many lines as you want), then the three answers.
# Example of a check: sp.expand((x + 3)*(x - 7) - (x**2 - 4*x - 21))

answer_R0_5a = ...  # 1) the letters of the right results, in alphabetical order, as text
answer_R0_5b = ...  # 2) the right expansion of (3x - 2)^2, as text
answer_R0_5c = ...  # 3) the simplified form of (x^2 - 4)/(x + 2), as text''',
    check='''for letter, answer in zip("abc", [answer_R0_5a, answer_R0_5b, answer_R0_5c]):
    wbm.check(f"R0.5{letter}", answer)''',
    solution='''claims = {"a": ((x + 3)*(x - 7), x**2 - 4*x - 21),
          "b": ((3*x - 2)**2, 9*x**2 - 4),
          "c": ((x - 1)**3, x**3 - 3*x**2 + 3*x - 1),
          "d": ((x + 2)*(x**2 - 2*x + 4), x**3 - 8)}
for letter, (start, result) in claims.items():
    difference = sp.expand(start - result)
    print(letter, "juste" if difference == 0 else f"faux (il reste {difference})")
print("b) bon développement :", sp.expand((3*x - 2)**2))
print("simplification       :", sp.simplify((x**2 - 4) / (x + 2)))''',
    record='''wbm.record("R0.5a", "ac",
           mistakes={"b) est faux : le carré d'une différence a un « double produit », -12x": "abc",
                     "d) est faux : développe-le, le dernier terme vaut 2 × 4 = +8": "acd",
                     "c) est juste : sp.expand((x - 1)**3) redonne exactement son résultat": "a",
                     "a) est juste : la différence se développe en 0": "c"})
wbm.record("R0.5b", sp.expand((3*x - 2)**2), kind="expr", variables=("x",),
           mistakes={"le double produit vaut 2 × 3x × 2 = 12x": "9*x**2 - 6*x + 4",
                     "le dernier terme est (-2)² = +4": "9*x**2 - 12*x - 4"})
wbm.record("R0.5c", sp.simplify((x**2 - 4) / (x + 2)), kind="expr", variables=("x",),
           mistakes={"x² - 4 = (x - 2)(x + 2) : quand on simplifie par x + 2, il reste x - 2": "x + 2"})''',
    note="`sp.expand(depart - resultat) == 0` prouve l'égalité ; remplacer x par un nombre ne fait que la tester.",
)

R0_6_MISTAKES = bug_letters_mistakes(
    "bcf", "adeg",
    {"b": "en Python, ^ n'est pas la puissance", "c": "1/4*x se calcule (1/4) × x, pas 1/(4x)",
     "f": "la multiplication ne se sous-entend pas en Python"})

R0_6 = Ex(
    "R0.6", "🐛", 1, 10, "Chasse à l'erreur : `x^2` et `2x` en Python",
    "repérer les écritures de formules que Python lit autrement que les maths.",
    "fiche §2 et §4", tracks="C, E",
    body="""Chaque ligne veut calculer la formule écrite en commentaire, pour un nombre `x` déjà défini. **Sans rien exécuter**, trouve les lignes fausses : soit elles provoquent une erreur, soit elles calculent autre chose que la formule.

```python
y1 = 3*x**2 - 5*x      # (a)  3x² − 5x
y2 = x^3               # (b)  x³
y3 = 1/4*x             # (c)  1/(4x)
y4 = (x - 1)**2        # (d)  (x − 1)²
y5 = -x**2             # (e)  −x²
y6 = 5x + 1            # (f)  5x + 1
y7 = x**(1/2)          # (g)  √x
```

1. Donne les lettres des lignes fausses, dans l'ordre alphabétique (par exemple `"ab"`).
2. Écris la fonction `y3` corrigée, qui calcule vraiment $\\dfrac{1}{4x}$ ; la vérification calcule `y3(2)`.""",
    todo='''answer_R0_6a = ...  # 1) the letters of the faulty lines, in alphabetical order, as text


def y3(x):
    """Line (c), corrected: return 1/(4x)."""
    raise NotImplementedError("write the corrected formula")''',
    check='''wbm.check("R0.6a", answer_R0_6a)
with wbm.attempt("R0.6b"):
    wbm.check("R0.6b", y3(2), computed=True)''',
    solution='''def y3(x):
    """Line (c), corrected: return 1/(4x)."""
    return 1 / (4 * x)


print("y3(2) =", y3(2))
print("ce que calculait la ligne (c) pour x = 2 :", 1/4*2)''',
    record=f'''wbm.record("R0.6a", "bcf",
           mistakes={R0_6_MISTAKES})
wbm.record("R0.6b", 1 / (4 * 2), decimals=4,
           mistakes={{"1/4*x se lit (1/4) × x : il faut des parenthèses, 1/(4*x)": 0.5}})''',
    note="(e) est juste : `-x**2` vaut $-(x^2)$, exactement comme la formule $-x^2$. Et (g) est juste : "
         "`x**(1/2)` est la racine carrée (pour x ≥ 0).",
)

PART_A = Part("A", "Taper, vérifier, calculer",
              "Fiche §2 à §4. Tu tapes des réponses de toutes les sortes, tu constates les arrondis des flottants, "
              "et tu vérifies des calculs avec SymPy.",
              given=PART_A_GIVEN, exercises=[R0_3, R0_4, R0_5, R0_6])

# ---------------------------------------------------------------------------
# Part B: plot and program (R0.7, R0.9)
# ---------------------------------------------------------------------------
R0_7 = Ex(
    "R0.7", "🎨", 1, 10, "Tracer une fonction avec matplotlib",
    "tracer proprement la courbe d'une fonction et y lire des valeurs.",
    "fiche §6", tracks="C",
    body="""Complète la fonction `plot_f` pour qu'elle trace la courbe de $f(x) = x^2 - 2x - 3$ sur l'intervalle $[-2 ; 4]$, en suivant la recette de la fiche (§6) : 200 points, un titre, le nom des deux axes, un quadrillage, une légende, et l'axe horizontal $y = 0$ en trait fin (`ax.axhline(0, linewidth=0.8)`).

Puis **lis sur ta courbe**, et écris dans ta copie de `06_mes_reponses.md` : les abscisses des points où la courbe coupe l'axe horizontal, et les coordonnées de son point le plus bas. Compare ensuite ta figure et tes lectures à celles de `05_solutions.md`.""",
    todo='''def plot_f():
    """Draw f(x) = x**2 - 2*x - 3 on [-2, 4]: title, axis labels, grid, legend and the line y = 0."""
    raise NotImplementedError("follow the recipe of the course sheet, §6")''',
    check='''with wbm.attempt("R0.7"):
    plot_f()''',
    solution='''def plot_f():
    """Draw f(x) = x**2 - 2*x - 3 on [-2, 4]: title, axis labels, grid, legend and the line y = 0."""
    xs = np.linspace(-2, 4, 200)
    ys = xs**2 - 2*xs - 3
    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.plot(xs, ys, label="f(x) = x² − 2x − 3")
    ax.axhline(0, linewidth=0.8, color="gray")
    ax.set_title("La parabole de f")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()
    plt.show()


plot_f()''',
)

R0_9_HOWTO = ("> **Mode d'emploi `mymath`.** Ouvre ta copie `mon_travail/mymath/_example.py` (créée par "
              "`python tools/start_chapter.py R0` ; sur Colab, `00_setup/COLAB.md`, « Modifier tes fichiers `.py` »). "
              "Lis la docstring de `mean` en entier, remplace la ligne `raise NotImplementedError(...)` par ton code, "
              "**enregistre** le fichier, puis exécute les cellules ci-dessous : la première recharge ta librairie.")

R0_9 = Ex(
    "R0.9", "🔨", 1, 25, "Ta première fonction : la moyenne (`mean`)",
    "écrire une fonction de `mymath` d'après son contrat, la tester et écrire ses propres tests.",
    "fiche §7 ; workbookIA 0A §100.5.1 (définir une fonction)", tracks="C, E", mymath="_example.py",
    body=R0_9_HOWTO + """

1. Écris `mean(values)` dans `mon_travail/mymath/_example.py` : la somme des valeurs divisée par leur nombre, sous forme de flottant ; une `ValueError` si la suite est vide. Fiche §7, et son piège : teste le vide avec `len(values) == 0`.
2. Lance les tests de `mean` (cellule « tests ») : ils comparent ta fonction à `np.mean`.
3. Écris **tes propres tests** dans `my_tests` : deux lignes `assert`, l'une sur une liste de deux nombres dont tu connais la moyenne de tête, l'autre sur une liste d'un seul nombre.

Si tu as déjà fait l'exercice 0A.26 de workbookIA, tu reconnais le mécanisme : ici, c'est ta librairie de maths.""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="R0")  # reload your saved file''',
    check='''with wbm.attempt("R0.9"):
    wbm.check("R0.9", mymath._example.mean([2, 4, 9]), computed=True)''',
    solution='''mymath = wbm.load_mymath("ref")
print("mean([2, 4, 9]) =", mymath._example.mean([2, 4, 9]))''',
    record='''wbm.record("R0.9", 5.0, decimals=4,
           mistakes={"divise par le nombre de valeurs (3), pas par 2": 7.5,
                     "on veut la moyenne, pas la somme : divise par le nombre de valeurs": 15})''',
    after=[
        ("md", "**Les tests de `mean`** (fiche §7 : lis d'abord la ligne qui suit chaque ❌, elle dit ce qui était attendu)."),
        ("todo", '''from wbm.nbtools import run_pytest_group

run_pytest_group("tests/test_example_mymath.py", "test_mean")'''),
        ("solution", '''from wbm.nbtools import run_pytest_group

run_pytest_group("tests/test_example_mymath.py", "test_mean", impl="ref")'''),
        ("md", "**Tes propres tests.** Deux lignes `assert` dans `my_tests` (question 3)."),
        ("todo", '''def my_tests():
    """Two asserts of your own on mymath._example.mean (question 3)."""
    raise NotImplementedError("write two assert lines")'''),
        ("check", '''with wbm.attempt("R0.9 tests"):
    my_tests()
    print("✅ Ex R0.9 : tes deux assert passent.")'''),
        ("solution", '''def my_tests():
    """Two asserts of your own on mymath._example.mean (question 3)."""
    assert mymath._example.mean([10, 20]) == 15.0
    assert mymath._example.mean([7]) == 7.0


my_tests()
print("✅ Ex R0.9 : les deux assert passent.")'''),
    ],
    note="Un `assert` qui passe n'affiche rien ; c'est quand il échoue qu'il parle (`AssertionError`).",
)

PART_B = Part("B", "Tracer et programmer",
              "Fiche §6 et §7. Une courbe propre, puis ta première fonction de `mymath` et ses tests.",
              exercises=[R0_7, R0_9])

PARTS = [PART_A, PART_B]


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'03_notebook' if kind == 'exercise' else '05_solutions'}.ipynb"
    rows = ["| Partie | ID | Titre | Type | ★ | ⏱️ |", "|---|---|---|---|---|---|",
            "| 0 | R0.1 | vérifier ton exercice papier ✏️ | ✏️ | ★ | |"]
    for part in PARTS:
        for i, ex in enumerate(part.exercises):
            title = ex.title.replace("|", "\\|")
            rows.append(f"| {part.key if i == 0 else ''} | {ex.id} | {title} | {ex.type} | {STARS[ex.stars]} | {ex.minutes} |")
    if kind == "exercise":
        title = "# R0 · Prise en main — notebook d'exercices"
        how = ("La partie 0 vérifie ton exercice papier. Chaque exercice de code : un énoncé, une cellule à compléter "
               "(les `...` et les `raise NotImplementedError`), puis une cellule de vérification (`wbm.check`). "
               "« Tout exécuter » (*Run all*) va jusqu'au bout même si rien n'est rempli : ce qui n'est pas fait "
               "affiche ⏳. Bloqué 15 minutes ? `04_indices.md`.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/r0_prise_en_main/03_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py R0`) : ce fichier-ci est mis à jour par Claude. Sur Colab, le badge "
               "ouvre cette version du dépôt, qui n'est pas enregistrée : crée puis ouvre ta copie comme l'explique "
               "`00_setup/COLAB.md` §2.")
    else:
        title = "# R0 · Prise en main — solutions (notebook exécuté)"
        how = ("Les réponses des exercices, exécutées. Les démarches détaillées (le *pourquoi*, les erreurs fréquentes, "
               "les variantes) sont dans `05_solutions.md`. Les cellules marquées `answer` enregistrent les réponses "
               "vérifiées par `wbm.check` (`tools/build_answers.py`).")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}\n\n" + "\n".join(rows))]


def objectives_cell() -> list:
    return [md("## Objectifs et rappel express\n\n"
               "- Vérifier ton calcul papier (partie 0), puis taper des réponses de toutes les sortes.\n"
               "- Constater les arrondis des flottants et vérifier un calcul avec SymPy.\n"
               "- Tracer une courbe propre et écrire ta première fonction de `mymath`.\n\n"
               "**Rappel express.** La puissance s'écrit `**` ; la multiplication s'écrit toujours (`2*x`) ; "
               "`//` et `%` donnent le quotient et le reste ; une fraction, une expression et un intervalle se tapent "
               "entre guillemets (`\"7/12\"`, `\"(x + 1)**2\"`, `\"]2 ; 5]\"`) ; on compare des flottants avec "
               "`math.isclose`.")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu prévoir ce que Python calcule pour `-3 ** 2`, `17 // 5` ou `2 ** 3 ** 2`, et pourquoi "
               "`0.1 + 0.2 == 0.3` est faux ?\n"
               "2. Sais-tu taper une fraction, une expression et un intervalle pour `wbm.check`, et vérifier un "
               "développement avec SymPy ?\n"
               "3. Sais-tu écrire une fonction de `mymath` d'après sa docstring, lancer ses tests et lire un échec ?\n\n"
               "**La suite** : le test de positionnement (`python tools/start_chapter.py POS`), puis R1. Dans "
               "workbookIA, continue le chapitre 0A (jusqu'à §100.6.2 avant R1).")]


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
    for ex in [e for part in PARTS for e in part.exercises]:
        for source in (ex.record, *(text for kind, text in ex.after if kind == "record")):
            if source:
                check_unique_keys(source, ex.id)
    write_notebook(f"{FOLDER}/03_notebook.ipynb", build("exercise"))
    write_notebook(f"{FOLDER}/05_solutions.ipynb", build("solution"))
    n_checks = sum(len(p.subs) for p in PAPER)
    n_ex = sum(len(part.exercises) for part in PARTS)
    print(f"✅ {FOLDER}/03_notebook.ipynb and 05_solutions.ipynb written ({len(PAPER)} paper exercise, "
          f"{n_checks} paper checks, {n_ex} notebook exercises)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
