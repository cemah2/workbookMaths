#!/usr/bin/env python
"""Build the two notebooks of the placement test POS from a single source (used by Claude).

    python tools/chapters/build_pos.py
    python tools/run_all_notebooks.py positionnement/03_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py positionnement/02_notebook.ipynb

02_notebook.ipynb: the learner reports the answers written on paper (01_sujet.md); every check is stored, and the
last cell turns them into the grid of 05_grille.md (2/2 -> skip, 1/2 -> skim, 0/2 -> study the whole chapter).
03_solutions.ipynb: the recorded answers (cells tagged "answer"), then the same checks with the right answers.
Wrong-answer messages state a rule, never a number of the answer.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import Paper, badge, check_unique_keys, code, md, setup_cell, write_notebook  # noqa: E402

FOLDER = "positionnement"

# (chapter, title, [Paper]) in the order of 01_sujet.md; each sub: (letter, hint, answer expression, record options)
SECTIONS = [
    ("R1", "Nombres et calcul", [
        Paper("POS.1", "Calculer avec des priorités et des fractions", [
            ("a", "a number", "7 - 3 * (2 - 5)",
             'mistakes={"la multiplication passe avant la soustraction": -12, "moins par moins donne plus": -2}'),
            ("b", "an irreducible fraction, as text", "Fraction(2, 3) + Fraction(5, 4)",
             'kind="fraction", simplified=True, '
             'mistakes={"on n\'additionne pas les numérateurs et les dénominateurs entre eux": "1"}'),
            ("c", "an irreducible fraction, as text", "Fraction(3, 5) / Fraction(9, 10)",
             'kind="fraction", simplified=True, '
             'mistakes={"diviser par une fraction, c\'est multiplier par son inverse": "27/50"}'),
            ("d", "an irreducible fraction, as text", "(1 - Fraction(1, 4)) / 2",
             'kind="fraction", simplified=True, '
             'mistakes={"diviser par 2 rend le nombre plus petit : c\'est le dénominateur qui double": "3/2"}'),
        ]),
        Paper("POS.2", "Puissances, racines et notation scientifique", [
            ("a", "a number", "3 ** (6 - 2 - 3)",
             'mistakes={"un exposant négatif compte en moins : additionne les exposants avec leur signe": 243}'),
            ("b", "an integer", "6", 'mistakes={"écris 72 comme un carré parfait multiplié par 2": 36}'),
            ("c", "a number", "round(6e5 / 3e-2)",
             'mistakes={"diviser par 10 puissance -2, c\'est multiplier par 10 puissance 2": 2000}'),
            ("d", "a decimal", "2.5e-3",
             'decimals=5, mistakes={"10 puissance -3 est un millième : la virgule recule de 3 rangs, pas de 4": 0.00025, '
             '"10 puissance -3 est un millième : la virgule recule de 3 rangs, pas de 2": 0.025}'),
        ]),
    ]),
    ("R2", "Calcul littéral et équations", [
        Paper("POS.3", "Développer, factoriser, résoudre une équation et une inéquation", [
            ("a", "the list [a, b, c]", "[2, 5, -12]",
             'mistakes={"le terme constant est le produit des deux nombres, avec son signe": [2, 5, 12], '
             '"réduis les termes en x avec leurs signes": [2, 11, -12], '
             '"développe chaque terme de la première parenthèse par chaque terme de la seconde": [2, 0, -12], '
             '"l\'ordre demandé est [a, b, c], du terme en x² au terme constant": [-12, 5, 2]}'),
            ("b", "a number", "5",
             'mistakes={"(x - a)² = x² - 2ax + a² : identifie le double produit": 10, '
             '"le signe de a se lit dans le double produit": -5}'),
            ("c", "a number", "5", ""),
            ("d", "an interval, as text", '"]-oo ; 2]"',
             'kind="interval", mistakes={"diviser par un nombre négatif retourne l\'inégalité": "[2 ; +oo[", '
             '"l\'inégalité est large : la borne est solution": "]-oo ; 2["}'),
        ]),
        Paper("POS.4", "Un système de deux équations à deux inconnues", [
            ("a", "the list [x, y]", "[3, 2]", 'mistakes={"l\'ordre demandé est [x, y]": [2, 3]}'),
            ("b", "1, 2 or 3", "1",
             'choices=[1, 2, 3], mistakes={"divise la seconde équation par 2 et compare-la à la première": 2, '
             '"les deux équations se ressemblent, mais leurs membres de droite sont-ils compatibles ?": 3}'),
        ]),
    ]),
    ("R3", "Fonctions", [
        Paper("POS.5", "Lire un graphique de fonction", [
            ("a", "a number", "1", ""),
            ("b", "a number", "3", 'mistakes={"regarde aussi les extrémités de la courbe": 2}'),
            ("c", "an interval, as text", '"[-1 ; 2]"',
             'kind="interval", mistakes={"décroissante : la courbe descend quand x augmente": "[2 ; 4]", '
             '"le plus grand intervalle contient ses bornes : crochets fermés": "]-1 ; 2["}'),
            ("d", "a number", "3",
             'mistakes={"le maximum est une valeur de g(x), pas l\'abscisse où elle est atteinte": -1}'),
        ]),
        Paper("POS.6", "Racines et sommet d'un polynôme du second degré", [
            ("a", "a number", "2 ** 2 - 4 * 2 * (-12)",
             'mistakes={"c est négatif : le terme -4ac est donc positif": -92}'),
            ("b", "a list of numbers", "[-3, 2]",
             'ordered=False, mistakes={"vérifie chaque racine en la remplaçant dans p(x)": [3, -2], '
             '"le dénominateur de la formule des racines est 2a": [4, -6]}'),
            ("c", "a fraction or a decimal", '"-1/2"',
             'kind="fraction", mistakes={"l\'abscisse du sommet vaut -b/(2a), avec le signe moins": "1/2"}'),
            ("d", "a fraction or a decimal", '"-25/2"',
             'kind="fraction", mistakes={"n\'oublie pas le coefficient devant x² en calculant p": "-25/4"}'),
        ]),
    ]),
    ("R4", "Logique, ensembles, Σ et Π", [
        Paper("POS.7", "Sommes avec Σ, somme double et produit avec Π", [
            ("a", "a number", "sum(2 * k + 1 for k in range(1, 6))",
             'mistakes={"le +1 s\'ajoute à chacun des termes": 31}'),
            ("b", "a number", "sum(10 ** i for i in range(4))",
             'mistakes={"i commence à 0 : le premier terme compte aussi": 1110}'),
            ("c", "a number", "sum(i * j for i in range(1, 3) for j in range(1, 4))", ""),
            ("d", "a number", "2 * 4 * 6",
             'mistakes={"Π multiplie les termes, Σ les additionne": 12}'),
        ]),
        Paper("POS.8", "La négation d'une phrase avec « pour tout »", [
            ("a", "1, 2, 3 or 4", "2",
             'choices=[1, 2, 3, 4], mistakes={"la négation de « pour tout » est « il existe »": 1, '
             '"« il existe » est juste, mais la conclusion aussi doit être niée": 3, '
             '"« aucun » nie trop : il suffit d\'un seul exemple pour contredire « pour tout »": 4}'),
            ("b", "True or False", "False",
             'mistakes={"un seul contre-exemple suffit à rendre la phrase fausse : cherche-le": True}'),
        ]),
    ]),
    ("R5", "Suites", [
        Paper("POS.9", "Terme et somme d'une suite géométrique", [
            ("a", "a number", "3 * 2 ** 5",
             'mistakes={"u_n = u_0 × q^n : compte bien l\'exposant": 192, "u_5 est le 6e terme, car on part de u_0": 48}'),
            ("b", "a number", "3 * (2 ** 6 - 1)", 'mistakes={"compte les termes de u_0 à u_5 : il y en a un de plus que 5": 93}'),
            ("c", "a fraction, as text", "Fraction(1, 1) / (1 - Fraction(1, 3))",
             'kind="fraction", mistakes={"la somme infinie vaut 1 / (1 - q), avec un signe moins": "3/4"}'),
        ]),
        Paper("POS.10", "Une suite définie par récurrence : premiers termes et limite", [
            ("a", "the list [v1, v2, v3]", "[4, 5, 5.5]",
             'decimals=1, mistakes={"chaque terme se calcule à partir du précédent : moitié, puis plus 3": [7, 17, 37], '
             '"on demande v1, v2 et v3 : v0 n\'en fait pas partie": [2, 4, 5]}'),
            ("b", "a number", "6", 'mistakes={"la limite vérifie la même relation que les termes de la suite": 3}'),
        ]),
    ]),
    ("R6", "Exponentielle et logarithmes", [
        Paper("POS.11", "Propriétés de l'exponentielle et du logarithme", [
            ("a", "a number", "1", 'mistakes={"e puissance 0 vaut 1, pas 0": 0}'),
            ("b", "an integer", "7", 'mistakes={"ln a - ln b = ln(a / b), pas ln(a - b)": 18}'),
            ("c", "a fraction or a decimal", '"1/2"',
             'kind="fraction", mistakes={"la racine carrée est la puissance 1/2 : écris √e comme une puissance de e": "2"}'),
            ("d", "a number", "6", 'mistakes={"log₂ 64 est l\'exposant de 2 qui donne 64": 32}'),
        ]),
        Paper("POS.12", "Résoudre des équations avec exp et ln", [
            ("a", "an exact expression with ln, as text", '"ln(7)"',
             'kind="expr", variables=("x",), '
             'mistakes={"on défait l\'exponentielle avec le logarithme népérien, pas avec l\'exponentielle": "exp(7)"}'),
            ("b", "an exact expression with exp, as text", '"exp(-1)"',
             'kind="expr", variables=("x",), '
             'mistakes={"applique exp aux deux membres, sans perdre le signe du second membre": "exp(1)", '
             '"une exponentielle est toujours positive": "-exp(1)"}'),
            ("c", "a number", "2.0",
             'decimals=2, mistakes={"e puissance y vaut 1 seulement quand y vaut 0, pas quand y vaut 1": round(7 / 3, 2)}'),
        ]),
    ]),
    ("R7", "Limites et dérivation", [
        Paper("POS.13", "Dériver trois fonctions, dont une composée", [
            ("a", "an expression in x, as text", '"10*x**4 - 6*x"',
             'kind="expr", variables=("x",), mistakes={"la dérivée d\'une constante est nulle": "10*x**4 - 6*x + 1", '
             '"(x^n)\' = n x^(n-1) : l\'exposant baisse de 1": "10*x**5 - 6*x**2"}'),
            ("b", "an expression in x, as text", '"x*exp(x)"',
             'kind="expr", variables=("x",), '
             'mistakes={"un produit se dérive par (uv)\' = u\'v + uv\'": "exp(x)"}'),
            ("c", "an expression in x, as text", '"-6*(5 - 2*x)**2"',
             'kind="expr", variables=("x",), '
             'mistakes={"n\'oublie pas la dérivée de l\'intérieur (règle de la chaîne)": "3*(5 - 2*x)**2", '
             '"la dérivée de l\'intérieur, 5 - 2x, est négative": "6*(5 - 2*x)**2"}'),
        ]),
        Paper("POS.14", "Tangente, variations et une limite", [
            ("a", "the list [m, p]", "[15, -28]",
             'mistakes={"p n\'est pas f(2) : écris y = f\'(2)(x - 2) + f(2), puis développe": [15, 2]}'),
            ("b", "an interval, as text", '"[-3 ; 1]"',
             'kind="interval", mistakes={"le plus grand intervalle contient les bornes où f\' s\'annule : '
             'crochets fermés": "]-3 ; 1["}'),
            ("c", "a number", "27", 'mistakes={"le maximum local est une valeur de f(x), pas une abscisse": -3}'),
            ("d", "a number", "3",
             'mistakes={"en +∞, seuls les termes de plus haut degré comptent, en haut comme en bas": 0}'),
        ]),
    ]),
    ("R8", "Probabilités de base", [
        Paper("POS.15", "Une probabilité avec un arbre", [
            ("a", "an irreducible fraction, as text", "Fraction(3, 5) * Fraction(2, 4)",
             'kind="fraction", simplified=True, '
             'mistakes={"sans remise, le second tirage se fait avec une boule de moins": "9/25"}'),
            ("b", "an irreducible fraction, as text", "2 * Fraction(3, 5) * Fraction(2, 4)",
             'kind="fraction", simplified=True, '
             'mistakes={"une de chaque couleur : rouge puis bleue, ou bleue puis rouge": "3/10"}'),
        ]),
        Paper("POS.16", "L'espérance et la variance d'une variable aléatoire", [
            ("a", "a decimal", "0.3",
             'decimals=2, mistakes={"l\'espérance pondère chaque valeur par sa probabilité": round(-1 / 3, 2), '
             '"attention au signe de la valeur négative": 0.7}'),
            ("b", "a decimal", "0.81",
             'decimals=2, mistakes={"V = E[X²] - E[X]² : soustrais le carré de l\'espérance": 0.9, '
             '"c\'est le carré de l\'espérance qu\'on soustrait": 0.6}'),
        ]),
    ]),
    ("R9", "Géométrie du plan, vecteurs et trigonométrie", [
        Paper("POS.17", "Distance et produit scalaire dans le plan", [
            ("a", "a number", "13",
             'decimals=0, mistakes={"la distance est la racine de la somme des carrés des écarts": 17, '
             '"n\'oublie pas la racine carrée": 169, "attention au signe : soustraire une ordonnée négative revient à ajouter": 11}'),
            ("b", "a number", "3 * 4 + (-2) * 1", 'mistakes={"attention au signe du produit des secondes coordonnées": 14}'),
            ("c", "True or False", "3 * 2 + (-2) * 3 == 0",
             'mistakes={"deux vecteurs sont orthogonaux quand leur produit scalaire est nul : calcule-le": False}'),
        ]),
        Paper("POS.18", "Cosinus d'un angle et radians", [
            ("a", "a fraction, as text", "Fraction(150, 180)",
             'kind="fraction", mistakes={"180 degrés correspondent à π radians": "6/5"}'),
            ("b", "a fraction, as text", '"1/2"', 'kind="fraction"'),
            ("c", "a number in degrees", "60",
             'mistakes={"les vecteurs ne sont pas orthogonaux : calcule le cosinus de leur angle": 90, '
             '"cos θ = u·v / (‖u‖ ‖v‖) : l\'angle est celui dont le cosinus vaut ce quotient": 30}'),
        ]),
    ]),
]

HELPERS = '''# Tools of the placement test: they store each check, then turn the results into your grid.
from fractions import Fraction

FINISHED = False   # put True when you have reported ALL your answers (a question left at ... then counts as missed)
RESULTS = {}       # filled by the check cells below: exercise -> [(right?, status)] for its questions

GRID = {"R1": ("Nombres et calcul", ["POS.1", "POS.2"]),
        "R2": ("Calcul littéral et équations", ["POS.3", "POS.4"]),
        "R3": ("Fonctions", ["POS.5", "POS.6"]),
        "R4": ("Logique, ensembles, Σ et Π", ["POS.7", "POS.8"]),
        "R5": ("Suites", ["POS.9", "POS.10"]),
        "R6": ("Exponentielle et logarithmes", ["POS.11", "POS.12"]),
        "R7": ("Limites et dérivation", ["POS.13", "POS.14"]),
        "R8": ("Probabilités de base", ["POS.15", "POS.16"]),
        "R9": ("Géométrie du plan, vecteurs et trigonométrie", ["POS.17", "POS.18"])}
ADVICE = {2: "tu peux sauter", 1: "à survoler", 0: "à faire en entier"}


def is_form_problem(result):
    \"\"\"A message about the way the answer is written (quotes, comma, fraction typed as a decimal), not its value.\"\"\"
    return result.status == "type" or (result.status == "near" and "valeur approchée" in result.message)


def check_all(ex_id, letters, answers):
    \"\"\"Check every question of a placement exercise and return (right?, status) for each.

    Until FINISHED is True, a wrong value only shows ❌: its message could guide a correction, and the test
    measures what you knew on paper. A problem of form (quotes, decimal point...) is always explained.
    \"\"\"
    results = []
    for letter, answer in zip(letters, answers):
        result = wbm.check(f"{ex_id}{letter}", answer, quiet=True)
        if result.status == "pending":
            line = "— laissée vide : comptée fausse" if FINISHED else "⏳ vide (laisse `...` si tu n'as pas su la faire)"
        elif result.passed:
            line = "✅"
        elif is_form_problem(result):
            line = f"⚠️ la forme, pas la valeur : {result.message} Corrige l'écriture, garde ta valeur."
        elif FINISHED:
            line = f"❌ {result.message}"
        else:
            line = "❌ (le message s'affichera quand FINISHED = True)"
        print(f"{ex_id}{letter} {line}")
        results.append((bool(result.passed), result.status))
    return results


def show_grid(results, finished):
    \"\"\"Print the verdict of each chapter: an exercise counts when ALL its questions are right.\"\"\"
    for cid, (title, exercises) in GRID.items():
        checks = [results.get(ex, [(False, "pending")]) for ex in exercises]
        if not finished and any(status == "pending" for c in checks for _, status in c):
            verdict = "⏳ pas encore rempli (ou mets FINISHED = True dans la cellule des outils)"
        else:
            score = sum(all(right for right, _ in c) for c in checks)
            verdict = f"{score}/2 → {ADVICE[score]}"
        print(f"{cid} · {title:<46} {verdict}")
    print("\\nCe que veut dire chaque verdict, et ce qu'il faut faire quand même : positionnement/05_grille.md")'''


FRENCH = {"1, 2 or 3": "le numéro 1, 2 ou 3", "1, 2, 3 or 4": "le numéro 1, 2, 3 ou 4", "True or False": "`True` ou `False`",
          "a decimal": "un décimal, avec un point", "a fraction or a decimal": "une fraction (entre guillemets) ou un décimal",
          "a fraction, as text": "une fraction, entre guillemets", "a list of numbers": "une liste de nombres",
          "a number in degrees": "un nombre (en degrés, sans le signe °)", "a number": "un nombre",
          "an exact expression with exp, as text": "une expression exacte avec `exp`, entre guillemets",
          "an exact expression with ln, as text": "une expression exacte avec `ln`, entre guillemets",
          "an expression in x, as text": "une expression en x, entre guillemets", "an integer": "un entier",
          "an interval, as text": "un intervalle, entre guillemets",
          "an irreducible fraction, as text": "une fraction irréductible, entre guillemets",
          "the list [a, b, c]": "la liste `[a, b, c]`", "the list [m, p]": "la liste `[m, p]`",
          "the list [v1, v2, v3]": "la liste `[v1, v2, v3]`", "the list [x, y]": "la liste `[x, y]`"}


def french_forms(paper: Paper) -> str:
    return " · ".join(f"{letter}) {FRENCH[hint]}" for letter, hint, _, _ in paper.subs)


def record_lines(paper: Paper) -> str:
    lines = []
    for letter, _, expr, options in paper.subs:
        args = f", {options}" if options else ""
        lines.append(f'wbm.record("{paper.id}{letter}", {expr}{args})')
    return "\n".join(lines)


def answer_value(expr: str) -> str:
    """The value the learner would type, as Python source, for the solutions notebook."""
    return expr


def check_cell(paper: Paper, kind: str) -> str:
    stem = f"answer_{paper.id.replace('.', '_')}"
    letters = "".join(letter for letter, *_ in paper.subs)
    names = ", ".join(f"{stem}{letter}" for letter in letters)
    if kind == "exercise":
        lines = [f"{stem}{letter} = ...  # {letter}) {hint}" for letter, hint, _, _ in paper.subs]
    else:
        lines = [f"{stem}{letter} = {answer_value(expr)}" for letter, _, expr, _ in paper.subs]
    lines += ["", f'RESULTS["{paper.id}"] = check_all("{paper.id}", "{letters}", [{names}])']
    return "\n".join(lines)


def header_cells(kind: str) -> list:
    rel = f"{FOLDER}/{'02_notebook' if kind == 'exercise' else '03_solutions'}.ipynb"
    if kind == "exercise":
        title = "# Test de positionnement — notebook de vérification"
        how = ("Fais d'abord le test **sur papier** (`01_sujet.md`, environ 2 heures, sans fiche ni calculatrice). "
               "Reporte ensuite ici **les valeurs** que tu as trouvées, exercice par exercice, sous la forme rappelée "
               "au-dessus de chaque cellule. Une question que tu n'as pas su faire : laisse `...`.\n\n"
               "Chaque cellule vérifie tes réponses avec `wbm.check` et affiche ✅ ou ❌, sans le message d'erreur tant "
               "que `FINISHED` vaut `False` : le test mesure ce que tu savais sur papier. Seul un problème de **forme** "
               "est expliqué tout de suite (⚠️ : guillemets, virgule, fraction tapée en décimal) : corrige l'écriture, "
               "jamais la valeur. Une erreur rouge (`SyntaxError`, `NameError`) vient aussi de la forme : il manque "
               "sans doute des guillemets.\n\n"
               "Quand tout est reporté, mets `FINISHED = True` dans la cellule des outils, puis « Tout exécuter » : les "
               "messages s'affichent, et la dernière cellule donne ta grille, chapitre par chapitre.\n\n"
               "> Travaille dans **ta copie** (`mon_travail/positionnement/02_notebook.ipynb`, créée par "
               "`python tools/start_chapter.py POS`) ; la version du dépôt, `positionnement/02_notebook.ipynb`, est "
               "mise à jour par Claude. Sur Colab, le badge ouvre la version du dépôt, qui n'est pas enregistrée : "
               "crée puis ouvre ta copie comme l'explique `00_setup/COLAB.md` §2.")
    else:
        title = "# Test de positionnement — solutions (notebook exécuté)"
        how = ("Les réponses enregistrées (cellules marquées `answer`, lues par `tools/build_answers.py`), puis les "
               "mêmes vérifications que le notebook de l'apprenant, remplies avec les bonnes réponses. Les démarches "
               "sont dans `03_corrige.md`.")
    return [md(f"{title}\n\n{badge(rel)}\n\n{how}")]


def build(kind: str) -> list:
    cells = header_cells(kind)
    cells.append(setup_cell(kind, chapter="POS") if kind == "exercise" else setup_cell(kind))
    cells.append(md("## Les outils\n\nExécute cette cellule (« Tout exécuter » le fait pour toi). Mets `FINISHED = True` "
                    "quand tu as reporté toutes tes réponses."))
    helpers = HELPERS if kind == "exercise" else HELPERS.replace("FINISHED = False", "FINISHED = True")
    cells.append(code(helpers))
    for cid, title, papers in SECTIONS:
        cells.append(md(f"## {cid} · {title}"))
        for paper in papers:
            cells.append(md(f"**{paper.id} — {paper.title}** · {french_forms(paper)}"))
            if kind == "solution":
                cells.append(code(record_lines(paper), tags=["answer"]))
            cells.append(code(check_cell(paper, kind)))
    cells.append(md("## Ta grille\n\nUn exercice compte quand **toutes** ses questions sont justes. Deux exercices par "
                    "chapitre : 2/2 → tu peux sauter, 1/2 → à survoler, 0/2 → à faire en entier. Le détail, et ce qu'il "
                    "faut faire quand même, est dans `05_grille.md`."))
    cells.append(code("show_grid(RESULTS, FINISHED)"))
    cells.append(md("## Et maintenant\n\nRecopie ta grille dans ta copie de `04_mes_reponses.md` et dans "
                    "`mon_travail/suivi/journal.md`. Lis `03_corrige.md` pour les questions ratées : chacune renvoie "
                    "à la section du chapitre qui l'enseigne. Puis passe à R1 : même « sauté », un chapitre garde "
                    "quelques exercices à faire (`05_grille.md`)."))
    return cells


def main() -> int:
    for _, _, papers in SECTIONS:
        for paper in papers:
            check_unique_keys(record_lines(paper), paper.id)
    write_notebook(f"{FOLDER}/02_notebook.ipynb", build("exercise"))
    write_notebook(f"{FOLDER}/03_solutions.ipynb", build("solution"))
    n_ex = sum(len(papers) for _, _, papers in SECTIONS)
    n_checks = sum(len(p.subs) for _, _, papers in SECTIONS for p in papers)
    print(f"✅ {FOLDER}/02_notebook.ipynb and 03_solutions.ipynb written ({n_ex} exercises, {n_checks} checks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
