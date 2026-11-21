"""Cells of the starter notebook of the synthesis project: projets/projet_synthese/depart/synthese.ipynb.

    python tools/chapters/build_ps.py --only depart
    python tools/run_all_notebooks.py projets/projet_synthese/depart/synthese.ipynb   # "Run all" with nothing written

The notebook is the model of the learner's article (PS.2 to PS.9 and PS.E1): one section per step, each saying what
to write and which step it serves; ``start_chapter.py PS`` copies it into mon_travail/projet_synthese/. Every cell
that calls the learner's code runs inside ``with wbm.attempt("PS.n"):``, so "Run all" with nothing written ends with
⏳ lines, never with an error, even when mon_travail/mymath does not exist. The project folder is the current folder
when it holds the article and algo.py (Jupyter on a computer, or a copy placed elsewhere), else
ROOT/mon_travail/projet_synthese (Colab, whose current folder is /content), else the kit itself (depart/).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nbbuild import code, md, setup_cell  # noqa: E402

TITLE = r"""
# 📝 Le titre de ton article

> **Le modèle de ton notebook-article** (projet de synthèse). Remplace chaque bloc 📝 par ton texte et garde les numéros de sections : la grille (`grille.md`) s'y réfère. Le cahier des charges est dans `projets/projet_synthese/README.md`, les indices dans `projets/projet_synthese/04_indices.md`, un exemple rédigé dans `projets/projet_synthese/exemple/` (à lire après ta première version de `cadrage.md`).
>
> Ce notebook s'exécute de bout en bout dès le départ : chaque cellule qui appelle ton code affiche ⏳ tant que ce code n'est pas écrit. Ton travail tient dans ton dossier `mon_travail/projet_synthese/` : `cadrage.md` (PS.1), ce notebook (PS.2 à PS.9 et PS.E1), `algo.py` (PS.6), `test_algo.py` et `mutants.py` (PS.7), et ta copie de la grille, `grille.md`.

**Auteur** : 📝 · **Date** : 📝 · **Algorithme** : 📝 (workbookIA, ch. 📝)

## Résumé

📝 **PS.9** · Cinq lignes : l'algorithme et ce qu'il calcule, ce que l'article dérive, les deux propriétés démontrées, comment l'implémentation est vérifiée, et ce que montre l'expérience.
"""

PROJECT_MD = r"""
### Le dossier du projet

Cette cellule trouve ton dossier et prépare `load_algo()`, qui relit ton module `algo.py` après chaque modification. Elle ne demande rien.
"""

PROJECT_CODE = r'''
# The project folder: the current folder when it holds the article and algo.py (Jupyter on your computer, or a copy),
# else mon_travail/projet_synthese (Colab, whose current folder is /content), else the kit (projets/.../depart).
import ast
import importlib
import json
import re
import sys
import time
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from wbm.nbtools import filled, run_pytest_group

T0 = time.perf_counter()
MODULE_NAME = "algo"
KIT = (ROOT / "projets" / "projet_synthese" / "depart").resolve()
CANDIDATES = [Path.cwd().resolve(), (ROOT / "mon_travail" / "projet_synthese").resolve(), KIT]
PROJECT = next((folder for folder in CANDIDATES
                if (folder / "synthese.ipynb").exists() and (folder / f"{MODULE_NAME}.py").exists()), None)
if PROJECT is None:
    raise FileNotFoundError("dossier du projet introuvable : garde les noms synthese.ipynb et algo.py, "
                            "dans mon_travail/projet_synthese/")
FIGURES = PROJECT / "figures"
if str(PROJECT) not in sys.path:
    sys.path.insert(0, str(PROJECT))
print(f"📁 Dossier du projet : {PROJECT}")
if PROJECT == KIT:
    print("ℹ️ C'est le modèle du kit : ton travail se fait dans ta copie, mon_travail/projet_synthese/ "
          "(python tools/start_chapter.py PS la crée).")


def load_algo():
    """Your module algo.py, read again from its file (call it after each change of algo.py)."""
    if MODULE_NAME in sys.modules:
        return importlib.reload(sys.modules[MODULE_NAME])
    return importlib.import_module(MODULE_NAME)
'''

INTRO = r"""
## 1. Introduction et plan

📝 **PS.9** · Dis en un paragraphe ce que fait l'algorithme, où il sert dans workbookIA, ce que l'article va dériver et pourquoi cela vaut la peine (ce que la dérivation explique et que le code seul ne dit pas). Puis le plan : une ligne par section, de §2 à §9.
"""

PROBLEM = r"""
## 2. Le problème

📝 **PS.2** (1,5 point) · Pose le problème avant tout calcul.

- **En une phrase, puis en une formule** : ce qu'est un exemple, ce que sont les paramètres, ce que l'algorithme calcule ou minimise.
- **Le tableau des notations** : chaque symbole de l'article, son sens, sa forme et son domaine. Garde les notations du dépôt ($n$ exemples, $p$ features, $\mathbf{X}$ de forme $(n, p)$, gras pour les vecteurs et les matrices, $\ln$), ou signale l'écart.

| Symbole | Sens | Forme | Domaine |
|---|---|---|---|
| 📝 | | | |

- **Les hypothèses**, numérotées pour être citées plus loin : (H1) 📝 ; (H2) 📝 …
- **Les conventions** : vecteurs lignes ou colonnes ; gradient en ligne (convention jacobienne, M17 §4) ou de la forme de la variable ; somme ou moyenne sur les exemples.
"""

DERIVATION = r"""
## 3. La dérivation

📝 **PS.3** (4 points) · Va de l'objectif de §2 jusqu'aux formules exactes que ton code calcule. Une étape par ligne, et pour chacune :

- l'équation, numérotée : `$$ … \tag{3.1} $$` ;
- *Justification* : le résultat utilisé, avec son chapitre et sa section dans ce dépôt (« M17 §3 ») ou dans MML (« MML §5.5 ») ;
- *Formes* : la forme de chaque objet, et la vérification de chaque produit.

Termine par l'encadré des formules finales : chacune avec son numéro et le nom de la fonction de `algo.py` qui la calcule (sa docstring cite le même numéro). Les points délicats (division par zéro, logarithme de 0, point où une fonction n'est pas dérivable, matrice non inversible) sont dits et réglés au moment où ils apparaissent.

**Étape 1.** 📝

$$ 📝 \tag{3.1} $$

*Justification* : 📝 · *Formes* : 📝
"""

SYMPY_CODE = r'''
# Optional (PS.3): check one step of your derivation with SymPy, in a small dimension (R0 §4, R7 §5).
# A check, not a proof: the derivation of §3 stays the one written above.
# import sympy as sp
'''

PROPERTIES = r"""
## 4. Deux propriétés et un cas limite

📝 **PS.4** (2,5 points) · Deux propriétés de l'algorithme (convexité, unicité, invariance, espérance, borne, coût…), pas d'un outil seul, chacune rédigée comme en R4 §8 : hypothèses, étapes justifiées, conclusion.

**Propriété 1.** *Énoncé* : sous (H…), 📝 · *Démonstration* : 📝 · *Ce qu'elle garantit en pratique* : 📝 · *Vérifiée numériquement par* : 📝 (un test de `test_algo.py` ou l'expérience de §8)

**Propriété 2.** 📝

**Le cas où une hypothèse tombe.** Nomme l'hypothèse, puis montre ce qui casse sans elle : un contre-exemple chiffré ou une petite expérience, calculé par la cellule « cas limite » ci-dessous.
"""

LIMIT_TODO = r'''
def limit_case():
    """TODO PS.4: the case where a hypothesis fails (a numerical counterexample, or a small experiment).

    Print what breaks (a conclusion that becomes false, an iteration that diverges, several solutions) and return
    the numbers that show it. It may use your module: algo = load_algo().
    """
    raise NotImplementedError("PS.4 : le cas limite n'est pas encore écrit")
'''

LIMIT_CHECK = r'''
# Cell « cas limite » (PS.4)
with wbm.attempt("PS.4"):
    print(limit_case())
'''

HAND = r"""
## 5. Un exemple à la main

📝 **PS.5** (1,5 point) · Un exemple en petite dimension (2 ou 3, quelques exemples), calculé sur papier avec les formules de §3, en fractions exactes quand c'est possible.

- **Les données**, écrites en entier : 📝
- **Le contrôle de vraisemblance**, annoncé avant le calcul (un ordre de grandeur, un signe, un cas dont le résultat est connu d'avance) : 📝
- **Le calcul**, étape par étape, chaque étape avec le numéro de sa formule de §3 : 📝
- **Le résultat** : 📝

Puis reporte ce résultat dans `HAND_RESULT` : la cellule de vérification le compare à ce que calcule ton module.
"""

HAND_TODO = r'''
# TODO PS.5: what you found by hand, and the tolerance of the comparison
HAND_RESULT = ...   # a number, a list or an array; Fraction(…) for exact values (from fractions import Fraction)
TOLERANCE = ...     # 0 to require equality (exact fractions), else a float justified in §5


def hand_example():
    """TODO PS.5: the same quantity, computed by your module (``algo``) on the data of the example."""
    raise NotImplementedError("PS.5 : l'exemple n'est pas encore calculé par ton module")
'''

HAND_CHECK = r'''
# Cell « vérification de l'exemple » (PS.5): your hand result against your module
with wbm.attempt("PS.5"):
    if not filled(HAND_RESULT, TOLERANCE):
        raise NotImplementedError("PS.5 : écris d'abord HAND_RESULT et TOLERANCE")
    algo = load_algo()
    computed = hand_example()
    expected_values = np.asarray(HAND_RESULT, dtype=object)
    computed_values = np.asarray(computed, dtype=object)
    if expected_values.shape != computed_values.shape:
        print(f"❌ formes différentes : à la main {expected_values.shape}, par ton module {computed_values.shape}")
    else:
        exact = all(isinstance(v, (int, Fraction)) for v in np.ravel(computed_values))
        if TOLERANCE == 0 and exact:   # fractions on both sides: exact equality
            gaps = [abs(Fraction(a) - Fraction(b)) for a, b in zip(np.ravel(expected_values), np.ravel(computed_values))]
            largest = max(gaps, default=Fraction(0))
        else:
            largest = float(np.max(np.abs(expected_values.astype(float) - computed_values.astype(float)), initial=0.0))
        verdict = "✅" if largest <= TOLERANCE else "❌"
        print(f"{verdict} écart le plus grand entre ton calcul à la main et ton module : {largest} "
              f"(tolérance {TOLERANCE})")
'''

IMPLEMENTATION = r"""
## 6. L'implémentation

📝 **PS.6** (3 points) · Présente `algo.py` : ses fonctions publiques, la formule de §3 que chacune calcule, les fonctions de `mymath` qu'il appelle et ce qu'elles font dans le calcul, et le coût d'un appel (en fonction de $n$ et $p$, M18 §5 si c'est une rétropropagation).

La cellule « Contrôle du module » lit `algo.py` sans l'exécuter : ses fonctions publiques et leurs docstrings (**API**), les fonctions de `mymath` qu'il appelle, marquées « à toi » si leur module est dans `mon_travail/mymath/`, « référence » sinon, et « copie de la référence » si ce module est la référence recopiée, aux commentaires et aux espaces près (**mymath**), et ses imports (**imports**). La cellule suivante lance, avec ton code, les tests de ces modules de `mymath`.
"""

CONTROL_CODE = r'''
# Cell « Contrôle du module » (PS.6): reads algo.py without running it
FORBIDDEN = {"sklearn", "torch", "scipy", "sympy", "tensorflow", "jax", "statsmodels"}   # the oracles of PS.7
manifest = json.loads((ROOT / "templates" / "mymath_stubs" / "MANIFEST.json").read_text(encoding="utf-8"))
OWNER = {Path(rel).stem: cid for cid, files in manifest["chapters"].items() for rel in files}
MYMATH_MODULES = {}   # module of mymath -> the test file of its chapter


def mymath_calls(tree):
    """The pairs (module, function) of mymath that a module calls: mymath.m.f, or m.f after a from-import."""
    aliases, calls = {}, set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "mymath":
            aliases.update({a.asname or a.name: a.name for a in node.names})
        elif isinstance(node, ast.ImportFrom) and (node.module or "").startswith("mymath."):
            calls.update((node.module.split(".")[1], a.name) for a in node.names)
        elif isinstance(node, ast.Import):   # import mymath.eigen as eig
            aliases.update({a.asname: a.name.split(".")[1] for a in node.names
                            if a.name.startswith("mymath.") and a.asname})
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Attribute):
            inner = node.value
            if isinstance(inner.value, ast.Name) and inner.value.id == "mymath":
                calls.add((inner.attr, node.attr))
        elif isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id in aliases:
            calls.add((aliases[node.value.id], node.attr))
    return sorted(calls)


try:
    tree = ast.parse((PROJECT / f"{MODULE_NAME}.py").read_text(encoding="utf-8"))
except SyntaxError as exc:
    tree = None
    print(f"❌ {MODULE_NAME}.py ne se lit pas (ligne {exc.lineno} : {exc.msg}) : corrige-le, puis réexécute.")
if tree is not None:
    print("API :")
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and not node.name.startswith("_"):
            doc = ast.get_docstring(node) or ""
            needed = ("Parameters", "Returns", "Raises") if isinstance(node, ast.FunctionDef) else ("Attributes",)
            missing = [part for part in needed if part not in doc]
            equation = bool(re.search(r"\((?:2|3|4)\.\d+\)", doc))
            mark = "⏳" if node.name == "example_function" else ("✅" if doc and not missing else "⚠️")
            note = (" (l'exemple du kit : remplace-la par tes fonctions)" if node.name == "example_function" else
                    "" if doc and not missing else f" (docstring {'absente' if not doc else 'sans ' + ', '.join(missing)})")
            note += ("" if equation or isinstance(node, ast.ClassDef) or node.name == "example_function" else
                     " ℹ️ aucune équation citée : normal seulement pour une fonction qui ne calcule pas une formule de §3 "
                     "(vérification des données)")
            print(f"  {mark} {node.name} : {doc.splitlines()[0] if doc else '—'}{note}")
    print("mymath :")
    calls = mymath_calls(tree)
    for module, function in calls:
        mine_path = ROOT / "mon_travail" / "mymath" / f"{module}.py"
        ref_path = ROOT / "solutions" / "mymath_ref" / f"{module}.py"
        mine = mine_path.exists()
        same_code = lambda a, b: ast.dump(ast.parse(a.read_text(encoding="utf-8"))) == ast.dump(ast.parse(b.read_text(encoding="utf-8")))  # noqa: E731,E501
        copied = mine and ref_path.exists() and same_code(mine_path, ref_path)
        chapter = OWNER.get(module, "?")
        MYMATH_MODULES[module] = f"tests/test_{chapter.lower()}_{module}.py"
        label = "⚠️ copie de la référence" if copied else ("✅ à toi    " if mine else "⚠️ référence")
        print(f"  {label} mymath.{module}.{function} ({chapter})")
    count = len(calls)
    print(f"  {count} fonction(s) de mymath appelée(s) ; au moins 3 sont attendues, écrites par toi"
          + (" ⏳" if count < 3 else ""))
    print("imports :")
    for node in ast.walk(tree):   # also the imports written inside a function
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module or "."]
            for name in [n for n in names if n != "__future__"]:
                top = name.split(".")[0]
                allowed = top in {"numpy", "mymath"} or top in sys.stdlib_module_names
                mark = "❌" if top in FORBIDDEN else ("✅" if allowed else "⚠️")
                note = (" (un oracle de PS.7 : pas dans le module)" if top in FORBIDDEN else "" if allowed else
                        " (ni NumPy, ni la bibliothèque standard, ni mymath : README, « Les règles », 3)")
                print(f"  {mark} {name}{note}")
'''

MYMATH_TESTS = r'''
# The tests of the mymath modules that algo.py calls, with your code (PS.6)
with wbm.attempt("PS.6"):
    if not MYMATH_MODULES:
        raise NotImplementedError("PS.6 : ton module n'appelle encore aucune fonction de mymath")
    for module, test_file in sorted(MYMATH_MODULES.items()):
        print(f"— mymath.{module} : {test_file}")
        run_pytest_group(test_file)
'''

VERIFICATION = r"""
## 7. La vérification

📝 **PS.7** (3 points) · Décris tes tests (`test_algo.py`) : l'oracle et ses réglages (pourquoi il est indépendant de ton code), les cas tirés au hasard (tailles, graines), les dérivées contre des différences finies centrées (le pas et la tolérance, M05a §5 et §7), le test de propriété, et ce que chaque tolérance suppose.

La cellule suivante lance tes tests avec ton code. Tant qu'un squelette n'est pas écrit, il est sauté avec ⏳ ; le projet est fini quand tout passe et que rien n'est sauté.
"""

TESTS_CODE = r'''
# Your tests (PS.7)
with wbm.attempt("PS.7"):
    run_pytest_group(PROJECT / "test_algo.py", root=PROJECT)
'''

MUTATION_MD = r"""
**La mutation.** Copie dans `mutants.py` une fonction de `algo.py`, sous le même nom, avec **une** erreur plausible (un facteur oublié, une transposée, un indice décalé, une somme au lieu d'une moyenne, un signe). Écris son nom dans `MUTANT` : la cellule « mutation » relance tes tests avec cette copie à la place de l'original (`python -m pytest test_algo.py --mutant=<nom>`). Au moins un test doit échouer ; dis lequel, et pourquoi c'est lui qui l'attrape.
"""

MUTATION_TODO = r'''
MUTANT = ...   # TODO PS.7: the name of the function of mutants.py (the same name as in algo.py), as a string
'''

MUTATION_CHECK = r'''
# Cell « mutation » (PS.7): your tests against a deliberate mistake
with wbm.attempt("PS.7"):
    if not filled(MUTANT):
        raise NotImplementedError("PS.7 : écris une mutation dans mutants.py, puis son nom dans MUTANT")
    result = run_pytest_group(PROJECT / "test_algo.py", root=PROJECT, args=[f"--mutant={MUTANT}"])
    if result.failed:
        print(f"✅ la mutation {MUTANT} est attrapée : {result.failed} test(s) en échec, nommés ci-dessus")
    else:
        print(f"❌ aucun test n'échoue avec la mutation {MUTANT} (ou elle n'a pas pu s'appliquer : lis les lignes "
              "au-dessus) : quel test devrait la voir ?")
'''

EXPERIMENT = r"""
## 8. L'expérience

📝 **PS.8** (1,5 point) · Une expérience qui illustre une propriété de §4 ou un point de la dérivation (convergence, conditionnement, stabilité, effet d'un hyperparamètre).

- **La question** : 📝
- **Ma prédiction**, écrite le 📝, **avant** d'exécuter (une phrase, et un nombre, une pente ou un sens de variation quand c'est possible) : 📝 ; reporte-la dans `PREDICTION`.
- **Le protocole** (ce qui varie, ce qui est fixé, les graines) : 📝
- **Ce que montre la figure**, avec la valeur que tu y lis : 📝
- **Conclusion** : la prédiction tient-elle ? Sinon, qu'est-ce qui expliquerait l'écart ? 📝

La cellule de vérification trace ta figure, signale un axe sans nom, un titre ou une légende absents, et l'enregistre dans `figures/`.
"""

EXPERIMENT_TODO = r'''
PREDICTION = ...   # TODO PS.8: your prediction, written BEFORE running the experiment (a string)
FIGURE_NAME = "experience.png"


def run_experiment():
    """TODO PS.8: run the experiment (several seeds when it depends on chance); return what the figure needs."""
    raise NotImplementedError("PS.8 : l'expérience n'est pas encore écrite")


def plot_experiment(results, ax):
    """TODO PS.8: draw the figure on ``ax``: both axes named with their units, a legend, a title."""
    raise NotImplementedError("PS.8 : la figure n'est pas encore écrite")
'''

EXPERIMENT_CHECK = r'''
# Cell « expérience » (PS.8)
with wbm.attempt("PS.8"):
    if not filled(PREDICTION):
        raise NotImplementedError("PS.8 : écris d'abord ta prédiction dans PREDICTION, avant de lancer l'expérience")
    algo = load_algo()
    results = run_experiment()
    fig, ax = plt.subplots(figsize=(6.5, 4))
    try:
        plot_experiment(results, ax)
    except BaseException:
        plt.close(fig)   # no empty figure left behind
        raise
    for what, present in [("de nom pour l'axe des abscisses", ax.get_xlabel()),
                          ("de nom pour l'axe des ordonnées", ax.get_ylabel()),
                          ("de titre", ax.get_title()), ("de légende", ax.get_legend())]:
        if not present:
            print(f"⚠️ la figure n'a pas {what}")
    FIGURES.mkdir(exist_ok=True)
    fig.savefig(FIGURES / FIGURE_NAME, dpi=120, bbox_inches="tight")
    print(f"🖼️ enregistrée dans figures/{FIGURE_NAME}")
    plt.show()
'''

CONCLUSION = r"""
## 9. Conclusion et limites

📝 **PS.9** · Ce que l'article a établi (en reprenant les numéros des équations et des propriétés), ce que l'expérience a montré, puis les **limites** : ce que l'article ne démontre pas, les hypothèses qui ne tiennent pas toujours en pratique, ce que l'oracle ne vérifie pas, ce que tu ferais avec plus de temps.
"""

REFERENCES = r"""
## Références

📝 **PS.9** · Par sections, jamais par pages. Une ligne par source, et chaque passage inspiré d'une source la cite à l'endroit où il sert.

- workbookMaths, 📝 (« M18 §6 » : le chapitre, la section, ce que tu y prends) ;
- M. P. Deisenroth, A. A. Faisal et C. S. Ong, *Mathematics for Machine Learning*, Cambridge University Press, 2020, 📝 (« MML §5.5 ») ;
- workbookIA, ch. 📝 (le chapitre de l'algorithme) ;
- la documentation de l'oracle (bibliothèque, fonction, version) : 📝 ;
- l'aide reçue (une relecture, un forum, un assistant) : 📝.
"""

PRESENTATION = r"""
## Annexe · La présentation

📝 **PS.E1** (1 point) · Le plan de ton exposé de cinq minutes, sans diapositive obligatoire : ce notebook peut servir de support.

| Partie | Durée prévue | Ce que je montre (équation, propriété, figure) |
|---|---|---|
| 📝 | 📝 | 📝 |

**Répétition chronométrée** le 📝 : 📝 min 📝 s.

**Cinq questions d'entretien** (de la banque du README, ou les tiennes) et tes réponses, de quelques lignes chacune, qui renvoient à l'article. Faute de réponse sûre, écris ce qui trancherait (un test, une expérience, une section de MML).

1. *Question* : 📝 — *Réponse* : 📝
2. *Question* : 📝 — *Réponse* : 📝
3. *Question* : 📝 — *Réponse* : 📝
4. *Question* : 📝 — *Réponse* : 📝
5. *Question* : 📝 — *Réponse* : 📝
"""

DURATION = r'''
# The duration of "Run all" (PS.9: less than 5 minutes on CPU, no cell over one minute)
elapsed = time.perf_counter() - T0
print(f"⏱️ « Run all » : {elapsed:.0f} s depuis la cellule du dossier du projet "
      + ("✅" if elapsed < 300 else "⚠️ (plus de 5 minutes : allège l'expérience)"))
'''


def cells() -> list:
    return [
        md(TITLE),
        setup_cell("exercise", chapter="PS"),
        md(PROJECT_MD), code(PROJECT_CODE),
        md(INTRO),
        md(PROBLEM),
        md(DERIVATION), code(SYMPY_CODE),
        md(PROPERTIES), code(LIMIT_TODO), code(LIMIT_CHECK),
        md(HAND), code(HAND_TODO), code(HAND_CHECK),
        md(IMPLEMENTATION), code(CONTROL_CODE), code(MYMATH_TESTS),
        md(VERIFICATION), code(TESTS_CODE), md(MUTATION_MD), code(MUTATION_TODO), code(MUTATION_CHECK),
        md(EXPERIMENT), code(EXPERIMENT_TODO), code(EXPERIMENT_CHECK),
        md(CONCLUSION),
        md(REFERENCES),
        md(PRESENTATION),
        code(DURATION),
    ]
