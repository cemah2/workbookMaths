"""Build 00_setup/demo.ipynb and 00_setup/demo_solutions.ipynb from one source.

    python tools/chapters/build_demo.py
    python tools/run_all_notebooks.py 00_setup/demo_solutions.ipynb --inplace
    python tools/build_answers.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nbbuild import badge, code, md, setup_cell, write_notebook  # noqa: E402

INTRO = """# 00 · Démo : vérifier que tout fonctionne

{badge}

Ce notebook vérifie ton installation, sur Colab comme sur ton ordinateur. Lance **Exécuter tout** (*Run all*) : il doit aller jusqu'au bout sans erreur.

| Étape | Ce que tu vérifies |
|---|---|
| 1. Setup | Python, les bibliothèques, la graine aléatoire |
| 2. `wbm.check` | la vérification de tes réponses : un nombre, une fraction, une expression, un intervalle |
| 3. SymPy | le calcul symbolique, qui vérifie tes calculs à la main |
| 4. Un graphique | une fonction et sa tangente avec matplotlib |
| 5. `mymath` | ta propre librairie, construite chapitre après chapitre |
"""

SETUP_MD = """## 1. Setup

Chaque notebook du workbook commence par **la même cellule**. Sur Colab, elle monte ton Google Drive, récupère la dernière version du dépôt (`git pull`) ou le clone la première fois, puis appelle `wbm.setup()`. En local, elle retrouve simplement le dossier du dépôt."""

CHECK_MD = """## 2. Vérifier une réponse sans voir la solution

Dans les chapitres, tu calcules d'abord **à la main**, sur papier, puis tu tapes ta réponse dans le notebook. `wbm.check("ID", ta_réponse)` te dit si elle est juste, **sans jamais afficher la bonne réponse** : seule une empreinte chiffrée de la solution est dans le dépôt. Quand c'est faux, le message essaie de dire où chercher (signe, facteur 2, fraction à l'envers…).

Quatre exemples, déjà remplis avec la bonne réponse. Exécute-les, puis **change une valeur** pour voir un message d'erreur.

**Démo 1 (un nombre).** Combien vaut $2^{10}$ ?"""

FRACTION_MD = """**Démo 2 (une fraction exacte).** Combien vaut $\\dfrac{1}{2} + \\dfrac{1}{3}$ ? Une fraction s'écrit comme un texte, entre guillemets : `"5/6"`. Essaie aussi `"10/12"`, `0.8333` et `"2/5"`."""

EXPR_MD = """**Démo 3 (une expression).** Quelle est la dérivée de $f(x) = x^3$ ? Une expression s'écrit comme en Python, entre guillemets : `"3*x**2"`. Les écritures `"3x^2"` et `"3*x²"` sont acceptées aussi. Essaie `"x**2"` ou `"-3*x**2"`."""

INTERVAL_MD = """**Démo 4 (un intervalle).** Pour quels réels $x$ a-t-on $x^2 \\le 4$ ? Un intervalle s'écrit en notation française `"[-2 ; 2]"` (ou anglaise `"[-2, 2]"`). Essaie `"]-2 ; 2["`."""

SYMPY_MD = """## 3. SymPy : vérifier un calcul à la main

SymPy fait du **calcul symbolique** : il manipule les expressions comme sur une feuille, sans approximation. Dans ce workbook, il sert à **vérifier** ce que tu as calculé à la main, jamais à le faire à ta place."""

SYMPY_CODE = """import sympy as sp

x = sp.Symbol("x")
f = x**2 * sp.exp(-x)
print("f(x)        =", f)
print("f'(x)       =", sp.factor(sp.diff(f, x)))
print("f'(x) = 0 si x ∈", sp.solve(sp.diff(f, x), x))
print("∫ f sur [0, +∞[ =", sp.integrate(f, (x, 0, sp.oo)))"""

PLOT_MD = """## 4. Un graphique : une fonction et sa tangente

La tangente à la courbe de $f$ au point d'abscisse $a$ a pour équation $y = f(a) + f'(a)(x - a)$ : c'est la meilleure approximation affine de $f$ près de $a$ (chapitre R7)."""

PLOT_CODE = """import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 * np.exp(-x)

def df(x):
    return (2 * x - x**2) * np.exp(-x)

a = 0.5
xs = np.linspace(-0.5, 5, 300)
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(xs, f(xs), label="f(x) = x² e^(-x)")
ax.plot(xs, f(a) + df(a) * (xs - a), linestyle="--", label=f"tangente en a = {a}")
ax.scatter([a], [f(a)], zorder=3)
ax.set_ylim(-0.3, 0.8)
ax.axhline(0, color="gray", linewidth=0.5)
ax.set_xlabel("x")
ax.legend()
plt.show()"""

MYMATH_MD = """## 5. `mymath`, ta librairie

Au fil des chapitres, tu écris ta propre librairie de maths dans `mon_travail/mymath/` : pivot de Gauss, méthode de Newton, valeurs propres, échantillonnage… Les tests la comparent à des bibliothèques de confiance (NumPy, SciPy, SymPy).

Pour la créer : `python tools/start_chapter.py --init` (sur Colab, voir `00_setup/COLAB.md`). Tant qu'elle n'existe pas, la cellule ci-dessous affiche ⏳ au lieu de planter."""

MYMATH_EXERCISE = """mymath = wbm.load_mymath("learner", missing_ok=True)
with wbm.attempt("démo mymath"):
    print("mymath._example.mean([1, 2, 3, 4]) =", mymath._example.mean([1, 2, 3, 4]))"""

MYMATH_SOLUTION = """mymath = wbm.load_mymath("ref")
print("mymath._example.mean([1, 2, 3, 4]) =", mymath._example.mean([1, 2, 3, 4]))"""

END_MD = """## C'est prêt

Si tout s'est exécuté jusqu'ici, ton environnement fonctionne. Suite : le chapitre R0 (`python tools/start_chapter.py R0`), puis le test de positionnement (`POS`), en parallèle du chapitre 0A de workbookIA (voir le README, « Ordre de travail commun »)."""


def build(kind: str) -> list:
    path = "00_setup/demo.ipynb" if kind == "exercise" else "00_setup/demo_solutions.ipynb"
    cells = [md(INTRO.format(badge=badge(path))), md(SETUP_MD), setup_cell("demo")]
    cells.append(md(CHECK_MD))
    answers = [
        ("DEMO.1", "answer_1 = 1024", "wbm.check(\"DEMO.1\", answer_1)",
         "wbm.record(\"DEMO.1\", 2**10, mistakes={\"tu as calculé 2 × 10, pas 2 puissance 10\": 20})"),
        ("DEMO.2", "answer_2 = \"5/6\"", "wbm.check(\"DEMO.2\", answer_2)",
         "from fractions import Fraction\n"
         "wbm.record(\"DEMO.2\", Fraction(1, 2) + Fraction(1, 3), kind=\"fraction\",\n"
         "           mistakes={\"on n'additionne pas les numérateurs et les dénominateurs entre eux\": \"2/5\"})"),
        ("DEMO.3", "answer_3 = \"3*x**2\"", "wbm.check(\"DEMO.3\", answer_3)",
         "wbm.record(\"DEMO.3\", \"3*x**2\", kind=\"expr\", variables=(\"x\",),\n"
         "           mistakes={\"l'exposant baisse de 1, et l'ancien exposant passe devant\": \"x**2\"})"),
        ("DEMO.4", "answer_4 = \"[-2 ; 2]\"", "wbm.check(\"DEMO.4\", answer_4)",
         "wbm.record(\"DEMO.4\", \"[-2 ; 2]\", kind=\"interval\",\n"
         "           mistakes={\"l'inégalité est large : -2 et 2 sont-ils solutions ?\": \"]-2 ; 2[\"})"),
    ]
    statements = {"DEMO.2": FRACTION_MD, "DEMO.3": EXPR_MD, "DEMO.4": INTERVAL_MD}
    for ex_id, value, check, record in answers:
        if ex_id in statements:
            cells.append(md(statements[ex_id]))
        if kind == "exercise":
            cells.append(code(value + "\n" + check))
        else:
            cells.append(code(record, tags=["answer"]))
            cells.append(code(value + "\n" + check))
    cells += [md(SYMPY_MD), code(SYMPY_CODE), md(PLOT_MD), code(PLOT_CODE), md(MYMATH_MD),
              code(MYMATH_EXERCISE if kind == "exercise" else MYMATH_SOLUTION), md(END_MD)]
    return cells


def main() -> None:
    write_notebook("00_setup/demo.ipynb", build("exercise"))
    write_notebook("00_setup/demo_solutions.ipynb", build("solution"))
    print("✅ 00_setup/demo.ipynb et 00_setup/demo_solutions.ipynb écrits")


if __name__ == "__main__":
    main()
