#!/usr/bin/env python
"""Build the two notebooks of chapter R0 from a single source (used by Claude).

    python tools/chapters/build_r0.py
    python tools/run_all_notebooks.py chapitres/r0_prise_en_main/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/r0_prise_en_main/03_notebook.ipynb

Part 0 checks the ✏️ paper exercise R0.1; parts A and B are the notebook exercises R0.3 to R0.9.
Wrong-answer messages state a rule, never a number of the answer (independent check of 2026-11-06).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, check_unique_keys, code,  # noqa: E402
                         guarded, md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "R0"
FOLDER = "chapitres/r0_prise_en_main"

# ---------------------------------------------------------------------------
# Part 0: the paper exercise R0.1 (02_exercices.md)
# ---------------------------------------------------------------------------
PAPER = [
    Paper("R0.1", "Calculer avec Python : priorités, division entière et reste", [
        ("a", "5 + 2 * 3 ** 2", "5 + 2 * 3 ** 2",
         'mistakes={"il n\'y a pas de parenthèses : la multiplication passe avant l\'addition": 63, '
         '"la puissance passe avant la multiplication": 41}'),
        ("b", "(5 + 2) * 3 ** 2", "(5 + 2) * 3 ** 2",
         'mistakes={"les parenthèses passent en premier": 23, '
         '"après les parenthèses, la puissance passe avant la multiplication": 441}'),
        ("c", "-4 ** 2", "-4 ** 2",
         'mistakes={"** passe avant le signe moins placé devant un nombre": 16}'),
        ("d", "(-4) ** 2", "(-4) ** 2",
         'mistakes={"avec les parenthèses, c\'est le nombre négatif tout entier qui est élevé au carré": -16}'),
        ("e", "29 // 6", "29 // 6", 'mistakes={"// donne le quotient entier, pas le reste": 5}'),
        ("f", "29 % 6", "29 % 6", 'mistakes={"% donne le reste, pas le quotient": 4}'),
        ("g", "-29 // 6", "-29 // 6",
         'mistakes={"// arrondit vers le bas (vers moins l\'infini), pas vers zéro": -4}'),
        ("h", "-29 % 6", "-29 % 6",
         'mistakes={"le reste est toujours entre 0 et 5 : quel quotient le permet ?": -5, '
         '"-29 n\'est pas un multiple de 6 : le reste n\'est pas nul": 0}'),
        ("i", "4 ** 3 ** 0", "4 ** 3 ** 0",
         'mistakes={"les puissances se calculent de droite à gauche": 1, '
         '"n\'oublie pas l\'exposant ** 0 : c\'est lui qui se calcule en premier": 64}'),
        ("j", "12 / 8 * 2, as a float", "12 / 8 * 2",
         'decimals=1, mistakes={"/ et * ont la même priorité : on calcule de gauche à droite": 0.75}'),
    ]),
]

PAPER_CONTEXT = "# Part 0 needs no data: the answers are the values Python prints for each expression."

PAPER_INTRO = ("## Partie 0 · Vérifier ton exercice papier (✏️ R0.1)\n\n"
               "Fais d'abord l'exercice R0.1 de `02_exercices.md` **sur papier**, dans ta copie de "
               "`06_mes_reponses.md`. Reporte ensuite chaque réponse ici : **la valeur** que tu as trouvée "
               "(par exemple `42`), pas l'expression Python, sinon tu ne vérifies rien. Les réponses pas encore "
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
           mistakes={"au même dénominateur, on multiplie le numérateur ET le dénominateur de chaque fraction": "2/3",
                     "on ne soustrait pas les numérateurs et les dénominateurs entre eux": "-1"})
wbm.record("R0.3b", "(x + 3)**2 - 1", kind="expr", variables=("x",),
           mistakes={"le carré porte sur toute la somme : des parenthèses autour de cette somme": "x + 3**2 - 1",
                     "le « moins 1 » vient après le carré, hors des parenthèses": "(x + 3 - 1)**2"})
wbm.record("R0.3c", "]-2 ; 5]", kind="interval",
           mistakes={"« strictement » exclut la borne, « ou égaux » l'inclut : vérifie chaque crochet": "[-2 ; 5[",
                     "« strictement supérieurs » : cette borne-là est exclue": "[-2 ; 5]"})
wbm.record("R0.3d", "]-oo ; 0]", kind="interval",
           mistakes={"« ou nuls » : 0 est inclus, donc crochet fermé de ce côté": "]-oo ; 0[",
                     "« négatifs » : ce sont les nombres inférieurs à 0, pas supérieurs": "[0 ; +oo["})
wbm.record("R0.3e", math.pi, decimals=3,
           mistakes={"arrondir n'est pas tronquer : regarde la décimale qui suit la troisième": 3.141})''',
)

TEN_TENTHS = "0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1"

R0_4_EXPERIMENT = f'''total = {TEN_TENTHS}
print("0.5 + 0.25 == 0.75 :", 0.5 + 0.25 == 0.75)
print("dix fois 0.1        =", total)
print("total == 1.0        :", total == 1.0)
print("écart 1.0 - total   =", 1.0 - total)
print("math.isclose        :", math.isclose(total, 1.0))
print("avec des Fraction   :", sum([Fraction(1, 10)] * 10))'''

R0_4 = Ex(
    "R0.4", "🔮", 1, 10, "Prédire : 0,5 + 0,25 et dix fois 0,1, exacts ou arrondis ?",
    "prévoir quand un calcul en flottants est exact et quand il est arrondi, et savoir comparer deux flottants.",
    "fiche §2, « Les flottants »", tracks="C, E",
    hypothesis=True,
    body=f"""La fiche (§2) explique pourquoi `0.1 + 0.2 == 0.3` vaut `False`. **Avant d'exécuter quoi que ce soit**, prédis :
- a) `0.5 + 0.25 == 0.75` vaut-il `True` ou `False` ?
- b) on additionne dix fois 0,1 : `{TEN_TENTHS}`. Le résultat `== 1.0` vaut-il `True` ou `False` ?

Écris tes deux prédictions dans la cellule (des booléens, `True` ou `False`), vérifie-les, puis lance l'expérience.""",
    todo='''prediction_R0_4a = ...  # a) True or False, written BEFORE running the experiment below
prediction_R0_4b = ...  # b) True or False''',
    check='''wbm.check("R0.4a", prediction_R0_4a)
wbm.check("R0.4b", prediction_R0_4b)''',
    record=f'''wbm.record("R0.4a", 0.5 + 0.25 == 0.75, prediction=True,
           mistakes={{"lance l'expérience, puis cherche ce que 0,5, 0,25 et 0,75 ont de particulier en binaire": False}})
wbm.record("R0.4b", ({TEN_TENTHS}) == 1.0, prediction=True,
           mistakes={{"lance l'expérience et compare avec 0.1 + 0.2 : chaque 0.1 est déjà arrondi": True}})''',
    after=[
        ("md", "**L'expérience.** Elle ne s'exécute qu'une fois tes deux prédictions écrites."),
        ("todo", guarded(R0_4_EXPERIMENT, ["prediction_R0_4a", "prediction_R0_4b"],
                         "⏳ Écris d'abord tes deux prédictions (True ou False), puis exécute à nouveau.")),
        ("solution", R0_4_EXPERIMENT),
        ("md", """**Après l'expérience**, lis les lignes affichées et réponds :
- c) l'écart s'affiche en notation scientifique, sous la forme `<m>e<k>`, qui veut dire $m \\times 10^{k}$. Quel est l'entier $k$ ?
- d) avec `Fraction`, la somme de dix fois $\\frac{1}{10}$ vaut-elle exactement 1 ? (`True` ou `False`)"""),
        ("todo", '''answer_R0_4c = ...  # c) an integer
answer_R0_4d = ...  # d) True or False'''),
        ("check", '''wbm.check("R0.4c", answer_R0_4c)
wbm.check("R0.4d", answer_R0_4d)'''),
        ("record", f'''wbm.record("R0.4c", math.floor(math.log10(1.0 - ({TEN_TENTHS}))),
           mistakes={{"un nombre minuscule a un exposant négatif : e-k veut dire « fois 10 puissance -k »": 16,
                     "donne seulement l'exposant k (ce qui suit le e, avec son signe), pas l'écart lui-même": 1.1e-16}})
wbm.record("R0.4d", sum([Fraction(1, 10)] * 10) == 1,
           mistakes={{"Fraction calcule exactement : regarde la dernière ligne affichée": False}})'''),
    ],
    note="0,5, 0,25 et 0,75 sont des sommes de puissances de 2 ($\\frac{1}{2}$, $\\frac{1}{4}$, $\\frac{3}{4}$) : ils "
         "s'écrivent exactement en binaire, sans arrondi. 0,1 non : chaque addition ajoute un peu d'erreur. Les deux "
         "remèdes : comparer avec une tolérance (`math.isclose`), ou calculer exactement avec `Fraction`.",
)

R0_5 = Ex(
    "R0.5", "📦", 1, 15, "Vérifier un développement avec SymPy (expand, simplify)",
    "utiliser SymPy pour vérifier un calcul fait à la main, sans le faire à sa place.",
    "fiche §4", tracks="C, E",
    body="""Un camarade a développé quatre expressions à la main :

| Ligne | Départ | Son résultat |
|---|---|---|
| 1 | $(x + 3)(x - 7)$ | $x^2 - 4x - 21$ |
| 2 | $(3x - 2)^2$ | $9x^2 - 4$ |
| 3 | $(x - 1)^3$ | $x^3 - 3x^2 + 3x - 1$ |
| 4 | $(x + 2)(x^2 - 2x + 4)$ | $x^3 - 8$ |

- a) Avec `sp.expand`, trouve **les lignes justes** (la méthode de la fiche : la différence se développe-t-elle en 0 ?). Réponds par la liste de leurs numéros, par exemple `[1, 2]`.
- b) Développe correctement la ligne 2 avec SymPy : quel est le **coefficient de $x$** (le nombre devant $x$) ?
- c) Avec `sp.simplify`, simplifie $\\dfrac{x^2 - 4}{x + 2}$. Le résultat s'écrit $ax + b$ : donne la liste `[a, b]`.

Pour b) et c), on demande des nombres : une expression recopiée de l'énoncé passerait la vérification sans rien prouver. `x` est déjà une lettre SymPy (cellule des outils, partie A).""",
    todo='''# Your checks with sp.expand and sp.simplify (as many lines as you want), then the three answers.
# Example of a check: sp.expand((x + 3)*(x - 7) - (x**2 - 4*x - 21))

answer_R0_5a = ...  # a) the list of the right lines, e.g. [1, 2]
answer_R0_5b = ...  # b) a number
answer_R0_5c = ...  # c) the list [a, b]''',
    check='''for letter, answer in zip("abc", [answer_R0_5a, answer_R0_5b, answer_R0_5c]):
    wbm.check(f"R0.5{letter}", answer)''',
    solution='''claims = {1: ((x + 3)*(x - 7), x**2 - 4*x - 21),
          2: ((3*x - 2)**2, 9*x**2 - 4),
          3: ((x - 1)**3, x**3 - 3*x**2 + 3*x - 1),
          4: ((x + 2)*(x**2 - 2*x + 4), x**3 - 8)}
for line, (start, result) in claims.items():
    difference = sp.expand(start - result)
    print("ligne", line, ":", "juste" if difference == 0 else f"fausse (il reste {difference})")
right = sp.expand((3*x - 2)**2)
print("ligne 2, bon développement :", right, "; coefficient de x :", right.coeff(x, 1))
print("simplification             :", sp.simplify((x**2 - 4) / (x + 2)))''',
    record='''wbm.record("R0.5a", [1, 3], ordered=False,
           mistakes={"la ligne 2 est fausse : le carré d'une différence a trois termes": [1, 2, 3],
                     "la ligne 4 est fausse : développe-la avec SymPy et regarde ce qui reste": [1, 3, 4],
                     "la ligne 3 est juste : la différence se développe en 0": [1],
                     "la ligne 1 est juste : la différence se développe en 0": [3]})
wbm.record("R0.5b", int(sp.expand((3*x - 2)**2).coeff(x, 1)),
           mistakes={"le double produit a le signe du produit de ses deux termes": 12,
                     "il y a bien un terme en x : le double produit": 0,
                     "le double produit vaut 2 × (premier terme) × (second terme)": -6})
wbm.record("R0.5c", [1, -2],
           mistakes={"factorise x² - 4, puis regarde quel facteur reste après la simplification": [1, 2]})''',
    note="`sp.expand(depart - resultat) == 0` prouve l'égalité ; remplacer x par un nombre ne fait que la tester.",
)

R0_6 = Ex(
    "R0.6", "🐛", 1, 10, "Chasse à l'erreur : `x^2` et `2x` en Python",
    "repérer les écritures de formules que Python lit autrement que les maths.",
    "fiche §2 et §4", tracks="C, E",
    body="""Chaque ligne veut calculer la formule écrite en commentaire, pour un nombre `x` déjà défini. **Sans rien exécuter**, trouve les lignes fausses : soit elles provoquent une erreur, soit elles calculent autre chose que la formule.

```python
y1 = 3*x**2 - 5*x      # ligne 1 :  3x² − 5x
y2 = x^3               # ligne 2 :  x³
y3 = 1/4*x             # ligne 3 :  1/(4x)
y4 = (x - 1)**2        # ligne 4 :  (x − 1)²
y5 = -x**2             # ligne 5 :  −x²
y6 = 5x + 1            # ligne 6 :  5x + 1
y7 = x**(1/2)          # ligne 7 :  √x
```

- a) Donne la liste des numéros des lignes fausses, par exemple `[1, 2]`.
- b) Écris la fonction `y3` corrigée, qui calcule vraiment $\\dfrac{1}{4x}$ ; la vérification calcule `y3(2)`.""",
    todo='''answer_R0_6a = ...  # a) the list of the faulty lines, e.g. [1, 2]


def y3(x):
    """Line 3, corrected: return 1/(4x)."""
    raise NotImplementedError("écris la formule corrigée")''',
    check='''wbm.check("R0.6a", answer_R0_6a)
with wbm.attempt("R0.6b"):
    wbm.check("R0.6b", y3(2), computed=True)''',
    solution='''def y3(x):
    """Line 3, corrected: return 1/(4x)."""
    return 1 / (4 * x)


print("y3(2) =", y3(2))
print("ce que calculait la ligne 3 pour x = 2 :", 1/4*2)''',
    record='''wbm.record("R0.6a", [2, 3, 6], ordered=False,
           mistakes={"il manque une ligne fausse : en Python, ^ n'est pas la puissance": [3, 6],
                     "il manque une ligne fausse : regarde comment Python lit une division suivie d'un produit": [2, 6],
                     "il manque une ligne fausse : la multiplication ne se sous-entend pas en Python": [2, 3],
                     "la ligne 5 est juste : -x**2 vaut -(x²), comme la formule": [2, 3, 5, 6],
                     "la ligne 7 est juste : la puissance 1/2 est la racine carrée": [2, 3, 6, 7],
                     "la ligne 1 est juste : relis-la lentement": [1, 2, 3, 6],
                     "la ligne 4 est juste : les parenthèses portent sur x - 1": [2, 3, 4, 6]})
wbm.record("R0.6b", 1 / (4 * 2), decimals=4,
           mistakes={"sans parenthèses, Python divise d'abord, puis multiplie : protège le dénominateur": 0.5})''',
    note="La ligne 5 est juste : `-x**2` vaut $-(x^2)$, exactement comme la formule $-x^2$. La ligne 7 aussi : "
         "`x**(1/2)` est la racine carrée (pour x ≥ 0).",
)

PART_A = Part("A", "Taper, vérifier, calculer",
              "Fiche §2 à §4. Tu tapes des réponses de toutes les sortes, tu prévois les arrondis des flottants, "
              "et tu vérifies des calculs avec SymPy.",
              given=PART_A_GIVEN, exercises=[R0_3, R0_4, R0_5, R0_6])

# ---------------------------------------------------------------------------
# Part B: plot and program (R0.7, R0.9)
# ---------------------------------------------------------------------------
R0_7 = Ex(
    "R0.7", "🎨", 1, 10, "Tracer une fonction avec matplotlib",
    "tracer proprement la courbe d'une fonction et y lire des valeurs.",
    "fiche §6", tracks="C",
    body="""Complète la fonction `plot_f` pour qu'elle trace la courbe de $f(x) = x^2 + 2x - 8$ sur l'intervalle $[-5 ; 3]$, en suivant la recette de la fiche (§6) : 200 points, un titre, le nom des deux axes, un quadrillage, une légende, et l'axe horizontal $y = 0$ en trait fin (`ax.axhline(0, linewidth=0.8)`).

Puis **lis sur ta courbe**, et écris dans ta copie de `06_mes_reponses.md` : les abscisses des points où la courbe coupe l'axe horizontal, et les coordonnées de son point le plus bas. Compare ensuite ta figure et tes lectures à celles de `05_solutions.md`.""",
    todo='''def plot_f():
    """Draw f(x) = x**2 + 2*x - 8 on [-5, 3]: title, axis labels, grid, legend and the line y = 0."""
    raise NotImplementedError("suis la recette de la fiche, §6")''',
    check='''with wbm.attempt("R0.7"):
    plot_f()''',
    solution='''def plot_f():
    """Draw f(x) = x**2 + 2*x - 8 on [-5, 3]: title, axis labels, grid, legend and the line y = 0."""
    xs = np.linspace(-5, 3, 200)
    ys = xs**2 + 2*xs - 8
    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.plot(xs, ys, label="f(x) = x² + 2x − 8")
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

R0_9_MY_TESTS_CHECK = '''with wbm.attempt("R0.9 tests"):
    import inspect
    try:
        n_asserts = inspect.getsource(my_tests).count("assert ")
    except (OSError, TypeError):  # the source of the function cannot be read: trust the learner
        n_asserts = 2
    my_tests()
    if n_asserts >= 2:
        print("✅ Ex R0.9 : tes assert passent.")
    else:
        print(f"❌ Ex R0.9 : my_tests contient {n_asserts} ligne(s) assert ; il en faut deux (question c).")'''

R0_9 = Ex(
    "R0.9", "🔨", 1, 25, "Ta première fonction : la moyenne (`mean`)",
    "écrire une fonction de `mymath` d'après son contrat, la tester et écrire ses propres tests.",
    "fiche §7 ; workbookIA 0A §100.3.1 (listes, `len`, `sum`) et §100.5.1 (définir une fonction)",
    tracks="C, E", mymath="_example.py",
    body=R0_9_HOWTO + """

- a) Écris `mean(values)` dans `mon_travail/mymath/_example.py` : la somme des valeurs divisée par leur nombre, sous forme de flottant ; une `ValueError` si la suite est vide. Fiche §7, et son piège : teste le vide avec `len(values) == 0`.
- b) Lance les tests de `mean` : la cellule sous « Les tests de `mean` » les exécute ; ils comparent ta fonction à `np.mean`.
- c) Écris **tes propres tests** dans `my_tests` : deux lignes `assert`, l'une sur une liste de deux nombres dont tu connais la moyenne de tête, l'autre sur une liste d'un seul nombre. Dans le notebook, ta fonction s'appelle `mymath._example.mean(...)` (le nom du module, puis celui de la fonction), et non `mean(...)` tout court.

Si tu as déjà fait l'exercice 0A.26 de workbookIA, tu reconnais le mécanisme : ici, c'est ta librairie de maths.""",
    todo='''mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="R0")  # reload your saved file''',
    check='''with wbm.attempt("R0.9"):
    wbm.check("R0.9", mymath._example.mean([2, 4, 9]), computed=True)''',
    solution='''mymath = wbm.load_mymath("ref")
print("mean([2, 4, 9]) =", mymath._example.mean([2, 4, 9]))''',
    record='''wbm.record("R0.9", 5.0, decimals=4,
           mistakes={"divise par le nombre de valeurs, pas par 2": 7.5,
                     "on veut la moyenne, pas la somme : divise par le nombre de valeurs": 15})''',
    after=[
        ("md", "**Les tests de `mean`** (fiche §7 : lis d'abord la ligne qui suit chaque ❌, elle dit ce qui était attendu)."),
        ("todo", '''from wbm.nbtools import run_pytest_group

run_pytest_group("tests/test_example_mymath.py", "test_mean")'''),
        ("solution", '''from wbm.nbtools import run_pytest_group

run_pytest_group("tests/test_example_mymath.py", "test_mean", impl="ref")'''),
        ("md", "**Tes propres tests.** Deux lignes `assert` dans `my_tests` (question c)."),
        ("todo", '''def my_tests():
    """Two asserts of your own on mymath._example.mean (question c)."""
    raise NotImplementedError("écris deux lignes assert")'''),
        ("check", R0_9_MY_TESTS_CHECK),
        ("solution", '''def my_tests():
    """Two asserts of your own on mymath._example.mean (question c)."""
    assert mymath._example.mean([10, 20]) == 15.0
    assert mymath._example.mean([7]) == 7.0'''),
        ("solution", R0_9_MY_TESTS_CHECK),
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
            f"| 0 | R0.1 | {PAPER[0].title} (vérification) | ✏️ | ★ | 10 |"]
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
               "- Prévoir les arrondis des flottants et vérifier un calcul avec SymPy.\n"
               "- Tracer une courbe propre et écrire ta première fonction de `mymath`.\n\n"
               "**Rappel express.** La puissance s'écrit `**` ; la multiplication s'écrit toujours (`2*x`) ; "
               "`//` et `%` donnent le quotient et le reste ; une fraction, une expression et un intervalle se tapent "
               "entre guillemets (`\"5/8\"`, `\"(x + 1)**2\"`, `\"[0 ; 1[\"`).")]


def footer_cells(kind: str) -> list:
    return [md("## ✅ Bilan\n\n"
               "**Auto-évaluation** (note-toi de 0 à 3 dans `mon_travail/suivi/auto_evaluation.md`) :\n"
               "1. Sais-tu prévoir ce que Python calcule pour `-3 ** 2`, `23 // 4` ou `2 ** 3 ** 2`, et pourquoi "
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
