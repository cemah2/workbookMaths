"""The synthesis project (projets/projet_synthese/, session 77): its specification, its grid and its starter kit.

* the files are present; the grid sums to 20, step by step as in the README and in the syllabus (fin.py);
* the learner's copy of the grid (depart/grille.md) has exactly the criteria and points of GRILLE.md;
* the README follows the contract of fin.py (titles, types, stars, durations, points), and every function of mymath,
  chapter and section it cites exists;
* the starter notebook is the one built from tools/chapters/ps_depart.py, with the standard setup cell, its
  sections, and every call to the learner's code inside ``wbm.attempt``;
* the tests of the kit run without error and are all skipped (⏳) while nothing is written; ``--mutant`` replaces a
  function of algo.py by its copy in mutants.py.
"""

from __future__ import annotations

import ast
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "projets" / "projet_synthese"
KIT = PROJECT / "depart"
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools" / "chapters"))

STEPS = ["PS.1", "PS.2", "PS.3", "PS.4", "PS.5", "PS.6", "PS.7", "PS.8", "PS.9", "PS.E1"]
OWN_FILES = ["README.md", "GRILLE.md", "04_indices.md", "depart/README.md", "depart/cadrage.md", "depart/grille.md",
             "depart/algo.py", "depart/test_algo.py", "depart/conftest.py", "depart/mutants.py",
             "depart/synthese.ipynb"]
CHAPTER_ID = r"(?:R\d|M\d\d[a-d]?|MB\d)"
# functions of mymath that take one number, or one example (one vector, one sequence) at a time: on a batch they need
# a Python loop, so a row of the list of algorithms needs three bricks besides them (README, « Des fonctions qui
# prennent un nombre »)
ONE_EXAMPLE_AT_A_TIME = {"explog.sigmoid", "explog.tanh", "approx.logsumexp", "sequences.exponential_moving_average",
                         "vectors.norm_p", "vectors.cosine_similarity", "orthogonal.project", "positional.online_softmax",
                         "positional.merge_softmax_states", "gaussian.condition_gaussian"}


def _number(text: str) -> Fraction:
    return Fraction(text.strip().replace(",", ".").replace("−", "-"))


def _fin() -> dict:
    spec = importlib.util.spec_from_file_location("fin", ROOT / "docs" / "syllabus" / "data" / "fin.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.CHAPTERS[0]


def _syllabus_points() -> dict[str, Fraction]:
    """The points of each step, as written in the notes of fin.py (« Points : PS.1 1, PS.2 1,5, … ; »)."""
    notes = _fin()["notes"]
    listing = re.search(r"Points : (.+?) ;", notes).group(1)
    return {m.group(1): _number(m.group(2)) for m in re.finditer(r"(PS\.\w+) (\d+(?:,\d+)?)", listing)}


def _grid_sections(text: str) -> dict[str, list[tuple[str, Fraction]]]:
    """{section title: [(criterion, points), …]} for each table of a grid (steps and penalties)."""
    sections, current = {}, None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.startswith("| [") else None
        if current and cells:
            assert len(cells) == 5, f"{current}: a row of the grid has {len(cells)} columns instead of 5: {line[:80]}"
            sections.setdefault(current, []).append((cells[1], _number(cells[2])))
    return sections


def _step_of(title: str) -> str | None:
    match = re.match(r"(PS\.\w+) — ", title)
    return match.group(1) if match else None


def test_the_files_of_the_project_are_present():
    missing = [name for name in OWN_FILES if not (PROJECT / name).is_file()]
    assert not missing, f"expected the files of the synthesis project, missing: {missing}"


def test_the_grid_sums_to_20_with_the_points_of_the_syllabus_and_of_the_readme():
    expected = _syllabus_points()
    assert list(expected) == STEPS and sum(expected.values()) == 20, f"expected 20 points over {STEPS}, got {expected}"
    sections = _grid_sections((PROJECT / "GRILLE.md").read_text(encoding="utf-8"))
    by_step = {}
    for title, rows in sections.items():
        step = _step_of(title)
        if step is None:
            continue
        announced = _number(re.search(r"\((\d+(?:,\d+)?) points?\)", title).group(1))
        total = sum(points for _, points in rows)
        assert total == announced, f"{step}: expected criteria summing to {announced} (its title), got {total}"
        by_step[step] = total
    assert by_step == expected, f"expected the points of fin.py per step {expected}, got {by_step} in GRILLE.md"
    penalties = sections.get("Les pénalités", [])
    assert sorted(points for _, points in penalties) == [-3, -2], f"expected the penalties −3 and −2, got {penalties}"
    readme = (PROJECT / "README.md").read_text(encoding="utf-8")
    table = {m.group(1): _number(m.group(2)) for m in re.finditer(r"^\| (PS\.\w+) [^|]+\| (\d+(?:,\d+)?) \|$",
                                                                  readme, re.M)}
    assert table == expected, f"expected the README's grid table to give {expected}, got {table}"
    for step, points in expected.items():
        text = f"**Points :** {str(float(points)).removesuffix('.0').replace('.', ',')}"
        assert text in readme.split(f"### {step} — ", 1)[1].split("\n### ", 1)[0], f"{step}: expected « {text} »"


def test_the_learners_copy_of_the_grid_has_the_same_criteria_and_points():
    reference = _grid_sections((PROJECT / "GRILLE.md").read_text(encoding="utf-8"))
    copy = _grid_sections((KIT / "grille.md").read_text(encoding="utf-8"))
    assert copy == reference, ("expected depart/grille.md to have exactly the criteria and points of GRILLE.md "
                               "(regenerate it from GRILLE.md); differing sections: "
                               + ", ".join(t for t in set(reference) | set(copy) if reference.get(t) != copy.get(t)))
    assert "Pour le correcteur" not in (KIT / "grille.md").read_text(encoding="utf-8")


def test_the_readme_follows_the_contract_of_the_syllabus():
    readme = (PROJECT / "README.md").read_text(encoding="utf-8")
    for ex_id, kind, stars, minutes, title, *_ in _fin()["exercises"]:
        header = f"### {ex_id} — {title} {kind} {'★' * stars} ⏱️ {minutes} min"
        assert header in readme, f"expected the header « {header} » in the README"
        body = readme.split(header, 1)[1].split("\n### ", 1)[0]
        for part in ("**Objectif :**", "**Chapitres mobilisés**", "**Livrable**", "**Critères de réussite**",
                     "**Erreurs à éviter**"):
            assert part in body, f"{ex_id}: expected « {part} » in its section of the README"
    for anchor in ("contexte", "algorithmes", "regles", "jalons", "demarrer", "kit", "etapes", "grille", "correction",
                   "entretien", "exemple", "hors-champ"):
        assert f'<a id="{anchor}"></a>' in readme, f"expected the section anchor « {anchor} » in the README"
    assert "```text" in readme.split('<a id="correction">', 1)[1], "expected the correction prompt, ready to copy"


def test_the_durations_of_the_readme_add_up_to_those_of_the_syllabus():
    fin = _fin()
    readme = (PROJECT / "README.md").read_text(encoding="utf-8")
    reading = fin["reading_minutes"]
    total = sum(ex[3] for ex in fin["exercises"]) + reading
    hours = str(fin["hours"]).replace(".", ",")
    assert f"| **Durée** | {hours} h, dont {reading} min de lecture" in readme, \
        f"expected the header table to give {hours} h, with {reading} min of reading (fin.py)"
    milestones = readme.split('<a id="jalons"></a>', 1)[1].split('<a id="demarrer"></a>', 1)[0]
    cells = re.findall(r"^\| \d \|.*\| (\d+) h(?: (\d+))? \|$", milestones, re.M)
    minutes = sum(60 * int(h) + int(m or 0) for h, m in cells)
    assert len(cells) == 4 and minutes == total, (f"expected four weeks of milestones adding up to {total} min (the steps "
                                                  f"and the reading of fin.py), got {minutes} min over {len(cells)} rows")


def test_the_list_of_algorithms_cites_existing_chapters_and_mymath_functions():
    from wbm.chapters import CHAPTER_ORDER

    readme = (PROJECT / "README.md").read_text(encoding="utf-8")
    listing = readme.split('<a id="algorithmes">', 1)[1].split('<a id="regles">', 1)[0]
    rows = [line for line in listing.splitlines() if re.match(r"^\| \d+ \|", line)]
    assert len(rows) == 15, f"expected 15 algorithms in the list, got {len(rows)}"
    stubs = ROOT / "templates" / "mymath_stubs"
    public = {}
    for path in stubs.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        public[path.stem] = {n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))
                             and not n.name.startswith("_")}
    problems = []
    for row in rows:
        cells = [c.strip() for c in row.strip("|").split("|")]
        problems += [f"row {cells[0]}: unknown chapter {cid}" for cid in re.split(r",\s*", cells[3])
                     if cid not in CHAPTER_ORDER]
        functions = re.findall(r"`(\w+)\.(\w+)`", cells[4])
        if len(functions) < 3:
            problems.append(f"row {cells[0]}: expected at least three functions of mymath, got {len(functions)}")
        arrays = [f"{m}.{f}" for m, f in functions if f"{m}.{f}" not in ONE_EXAMPLE_AT_A_TIME]
        if len(arrays) < 3:
            problems.append(f"row {cells[0]}: expected at least three bricks that take an array (not one number or one "
                            f"example at a time), got {arrays}")
    for module, function in re.findall(r"`(\w+)\.(\w+)`", readme):
        if module in public and function not in public[module]:
            problems.append(f"mymath.{module} has no public function {function}")
    assert not problems, "expected existing chapters and mymath functions: " + "; ".join(problems)


def test_the_kit_table_of_the_readme_lists_exactly_the_files_of_the_kit():
    import start_chapter

    readme = (PROJECT / "README.md").read_text(encoding="utf-8")
    table = readme.split('<a id="kit"></a>', 1)[1].split('<a id="etapes"></a>', 1)[0]
    listed = set(re.findall(r"^\| `([^`]+)` \|", table, re.M))
    files = {path.relative_to(KIT).as_posix() for path in start_chapter.starter_files(PROJECT)}
    assert listed == files, f"expected the kit table to list exactly the files of depart/ {sorted(files)}, got {sorted(listed)}"


def test_the_hints_give_three_levels_for_each_step():
    text = (PROJECT / "04_indices.md").read_text(encoding="utf-8")
    sections = re.split(r"^### ", text, flags=re.M)[1:]
    steps = [section.split(" — ", 1)[0] for section in sections]
    assert steps == STEPS, f"expected one section of hints per step {STEPS}, got {steps}"
    for step, section in zip(steps, sections):
        levels = re.findall(r"<summary>Indice (\d)</summary>", section)
        assert levels == ["1", "2", "3"], f"{step}: expected the hints 1, 2 and 3, got {levels}"


def _fiche_sections(chapter: str) -> set[int]:
    from wbm.chapters import dir_prefix

    folder = next((p for p in (ROOT / "chapitres").iterdir()
                   if p.is_dir() and p.name.startswith(dir_prefix(chapter) + "_")), None)
    if folder is None:
        return set()
    text = (folder / "01_fiche.md").read_text(encoding="utf-8")
    return {int(n) for n in re.findall(r"^## §(\d+) ", text, re.M)}


def test_the_cited_sections_and_exercises_exist():
    sources = ["README.md", "GRILLE.md", "04_indices.md", "depart/README.md", "depart/cadrage.md"]
    texts = {name: (PROJECT / name).read_text(encoding="utf-8") for name in sources}
    notebook = json.loads((KIT / "synthese.ipynb").read_text(encoding="utf-8"))
    texts["depart/synthese.ipynb"] = "\n".join("".join(c["source"]) for c in notebook["cells"])
    syllabus = "\n".join(p.read_text(encoding="utf-8") for p in (ROOT / "docs" / "syllabus" / "data").glob("partie_*.py"))
    reference = re.compile(rf"\b({CHAPTER_ID}) §(\d+)((?:(?:,| et| à) §\d+)*)")
    problems = []
    for name, text in texts.items():
        for match in reference.finditer(text):
            chapter = match.group(1)
            numbers = [int(match.group(2))] + [int(n) for n in re.findall(r"§(\d+)", match.group(3))]
            known = _fiche_sections(chapter)
            problems += [f"{name}: {chapter} §{n}" for n in numbers if n not in known]
        for ex_id in re.findall(rf"🛠️ ({CHAPTER_ID}\.\d+)", text):
            if f'("{ex_id}",' not in syllabus:
                problems.append(f"{name}: no exercise {ex_id} in the syllabus")
    assert not problems, "expected sections and exercises that exist: " + ", ".join(sorted(set(problems)))


def test_the_project_files_state_no_result_of_a_frontier():
    """BIBLE §8: the derivations of the listed algorithms (frontieres of fin.py) are the learner's; a few tell-tale
    results must never appear in the specification, the grid, the hints or the kit."""
    telltales = ["p − y", "p - y", "XᵀΔ", "ΔWᵀ", "Σxy / (Σx² + λ)", "sign(z)", "max(|z|", "2/a", "1 − β^t",
                 "1 - beta**t", "√d_k", "sqrt(d_k)", "ᾱ_t", "alpha_bar"]
    found = []
    for name in OWN_FILES:
        text = (PROJECT / name).read_text(encoding="utf-8")
        found += [f"{name}: « {t} »" for t in telltales if t in text]
    assert not found, "expected no result of a frontier exercise in the project files: " + ", ".join(found)


def _notebook():
    return json.loads((KIT / "synthese.ipynb").read_text(encoding="utf-8"))


def test_the_starter_notebook_is_built_from_its_source_with_the_standard_setup_cell():
    import nbbuild
    import ps_depart

    expected = [cell.source for cell in ps_depart.cells()]
    got = ["".join(cell["source"]) for cell in _notebook()["cells"]]
    assert got == expected, ("expected depart/synthese.ipynb to be the notebook built from tools/chapters/ps_depart.py: "
                             "python tools/chapters/build_ps.py --only depart")
    setup = [c for c in _notebook()["cells"] if "setup" in c.get("metadata", {}).get("tags", [])]
    assert len(setup) == 1 and "".join(setup[0]["source"]) == nbbuild.setup_cell("exercise", chapter="PS").source, \
        'expected one setup cell, setup_cell("exercise", chapter="PS")'
    assert not any(c.get("outputs") for c in _notebook()["cells"] if c["cell_type"] == "code"), \
        "expected the starter notebook without outputs (the learner runs it)"


def test_the_starter_notebook_has_the_sections_of_the_grid_and_guards_the_learners_code():
    cells = _notebook()["cells"]
    markdown = "\n".join("".join(c["source"]) for c in cells if c["cell_type"] == "markdown")
    headings = ["## Résumé", "## 1. Introduction et plan", "## 2. Le problème", "## 3. La dérivation",
                "## 4. Deux propriétés et un cas limite", "## 5. Un exemple à la main", "## 6. L'implémentation",
                "## 7. La vérification", "## 8. L'expérience", "## 9. Conclusion et limites", "## Références",
                "## Annexe · La présentation"]
    positions = [markdown.find(h) for h in headings]
    assert -1 not in positions and positions == sorted(positions), \
        f"expected the sections in this order: {[h for h, p in zip(headings, positions) if p == -1] or headings}"
    calls = ("limit_case()", "hand_example()", "run_experiment()", "plot_experiment(", "run_pytest_group(")
    unguarded = []
    for i, cell in enumerate(cells):
        source = "".join(cell["source"])
        if cell["cell_type"] != "code" or "def " in source:
            continue
        if any(call in source for call in calls) and 'with wbm.attempt("PS.' not in source:
            unguarded.append(i)
    assert not unguarded, f"expected the calls to the learner's code inside wbm.attempt, cells {unguarded}"
    words = re.compile(r"on voit|facile de voir|après calcul|évident|clairement", re.I)
    assert not words.search("\n".join("".join(c["source"]) for c in cells)), \
        "expected none of the words that the grid looks for (PS.3) in the model of the article"


def _pytest(args, cwd, env_extra=None):
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "WBM_ROOT": str(ROOT), "COLUMNS": "200",
           **(env_extra or {})}
    env.pop("WBM_IMPL", None)
    return subprocess.run([sys.executable, "-m", "pytest", "-q", "-rs", "-p", "no:cacheprovider", *args], cwd=cwd,
                          capture_output=True, text=True, env=env, timeout=120)


@pytest.mark.parametrize("impl", ["ref", "stubs", "learner"])
def test_the_tests_of_the_kit_run_and_are_all_skipped(impl):
    result = _pytest(["projets/projet_synthese/depart/test_algo.py", f"--impl={impl}"], cwd=ROOT)
    summary = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else result.stderr[-500:]
    assert result.returncode == 0 and re.search(r"\d+ skipped", summary) and not re.search(
        r"passed|failed|error", summary), f"expected every test of the kit skipped (⏳), got: {summary}"
    reasons = [line for line in result.stdout.splitlines() if line.startswith("SKIPPED")]
    assert reasons and all("⏳" in line for line in reasons), f"expected ⏳ in every skip reason: {reasons[:3]}"


def test_the_mutant_option_swaps_a_function_and_a_missing_mutant_stops_the_run(tmp_path):
    for name in ("conftest.py", "algo.py"):
        shutil.copy(KIT / name, tmp_path / name)
    (tmp_path / "mutants.py").write_text("import numpy as np\n\n\ndef example_function(x):\n"
                                         "    return np.zeros(len(x))\n", encoding="utf-8")
    (tmp_path / "test_algo.py").write_text(
        "import numpy as np\n\n\ndef test_shape(algo):\n"
        "    assert algo.example_function(np.ones((3, 2))).shape == (3,), 'expected shape (3,)'\n", encoding="utf-8")
    plain = _pytest(["test_algo.py", "--impl=ref"], cwd=tmp_path)
    assert "1 skipped" in plain.stdout and "⏳ pas encore écrit" in plain.stdout, \
        f"expected the test skipped while example_function raises NotImplementedError: {plain.stdout[-300:]}"
    mutated = _pytest(["test_algo.py", "--impl=ref", "--mutant=example_function"], cwd=tmp_path)
    assert "1 passed" in mutated.stdout and "Mutation : algo.example_function" in mutated.stdout, \
        f"expected the mutant used instead of algo.example_function: {mutated.stdout[-300:]}"
    missing = _pytest(["test_algo.py", "--impl=ref", "--mutant=gradient"], cwd=tmp_path)
    assert missing.returncode != 0 and "mutants.py n'a pas de fonction gradient()" in missing.stdout, \
        f"expected the run stopped for a mutant that does not exist: {missing.stdout[-300:]}"
