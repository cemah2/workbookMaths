"""The worked example of the synthesis project (projets/projet_synthese/exemple, BIBLE §18).

Its tests pass on the reference of mymath and catch its two mutations (in a subprocess, with --impl=ref, as the
notebook runs them); its notebook is executed, without an error output and without the phrases that replace a
calculation (GRILLE.md, PS.3), with paired $ and a \\tag on each cited equation (PS.9); its module imports only NumPy,
math and mymath; its tests import their oracles and never mymath; its conftest.py is the kit's one; its cadrage fits
on one page; its grille.md is GRILLE.md filled (same rows, criteria, points and checks).
"""

from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "projets" / "projet_synthese"
EXAMPLE = PROJECT / "exemple"
TEST_FILE = EXAMPLE / "test_poisson_newton.py"
NOTEBOOK = EXAMPLE / "exemple.ipynb"
FILES = ["README.md", "cadrage.md", "grille.md", "poisson_newton.py", "test_poisson_newton.py", "conftest.py",
         "mutants.py", "exemple.ipynb", "figures/convergence.png", "figures/sans_maximum.png"]


def _pytest(*args: str) -> subprocess.CompletedProcess:
    """The example's tests in a subprocess, from the repository, on the reference of mymath."""
    env = {**os.environ, "WBM_ROOT": str(ROOT), "PYTHONDONTWRITEBYTECODE": "1", "COLUMNS": "200"}
    command = [sys.executable, "-m", "pytest", str(TEST_FILE.relative_to(ROOT)), "-q", "-p", "no:cacheprovider",
               "--impl=ref", *args]
    return subprocess.run(command, cwd=ROOT, capture_output=True, text=True, env=env, timeout=600)


def _imported_modules(path: Path) -> set[str]:
    """The top-level names of every module imported by a file (at any depth of its code)."""
    names = set()
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0:
            names.add((node.module or "").split(".")[0])
    return names


def test_example_files_exist():
    missing = [name for name in FILES if not (EXAMPLE / name).exists()]
    assert not missing, f"expected the files of the example, missing: {missing}"


def test_example_tests_pass_on_the_reference_and_skip_nothing():
    proc = _pytest("-rfs")
    summary = proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else proc.stderr[-500:]
    assert proc.returncode == 0, f"expected every test of the example to pass with --impl=ref, got: {summary}"
    assert "skipped" not in summary, f"expected no skipped test in the example, got: {summary}"


def test_example_mutations_are_caught():
    for mutant in ("newton_direction", "hessian"):
        proc = _pytest(f"--mutant={mutant}", "--tb=no")
        summary = proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else proc.stderr[-500:]
        assert proc.returncode == 1 and " failed" in summary, (
            f"expected the mutation {mutant} of mutants.py to make tests fail, got: {summary}")


def test_example_notebook_is_executed_without_errors():
    nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    code_cells = [cell for cell in nb["cells"] if cell["cell_type"] == "code"]
    not_run = [i for i, cell in enumerate(code_cells) if cell.get("execution_count") is None]
    assert not not_run, f"expected an executed notebook (outputs kept), code cells not run: {not_run}"
    for i, cell in enumerate(code_cells):
        for output in cell.get("outputs", []):
            assert output.get("output_type") != "error", f"expected no error output, got one in code cell {i}"
            text = "".join(output.get("text", []))
            assert "Traceback (most recent call last)" not in text, f"expected no traceback, got one in code cell {i}"
    setup = "".join(code_cells[0]["source"])
    assert 'wbm.load_mymath("ref")' in setup, "expected the solution setup cell (the reference of mymath)"


def test_example_notebook_has_no_phrase_that_replaces_a_calculation():
    """GRILLE.md, PS.3: « on voit », « facile de voir », « après calcul », « évident », « clairement » (grep -i)."""
    text = NOTEBOOK.read_text(encoding="utf-8")
    found = re.findall(r"(?i)on voit|facile de voir|après calcul|évident|clairement", text)
    assert not found, f"expected none of the phrases of PS.3 in the example, found: {found}"


def test_example_module_imports_only_numpy_math_and_mymath():
    allowed = {"numpy", "math", "mymath", "__future__"}
    extra = _imported_modules(EXAMPLE / "poisson_newton.py") - allowed
    assert not extra, f"expected poisson_newton.py to import NumPy, math and mymath only, got also: {sorted(extra)}"
    extra = _imported_modules(EXAMPLE / "mutants.py") - allowed - {"poisson_newton"}
    assert not extra, f"expected mutants.py to import NumPy, mymath and the module only, got also: {sorted(extra)}"


def test_example_tests_use_independent_oracles_and_never_mymath():
    imported = _imported_modules(TEST_FILE)
    assert {"sklearn", "scipy"} <= imported, f"expected scikit-learn and SciPy as oracles, imported: {sorted(imported)}"
    assert "mymath" not in imported and "poisson_newton" not in imported, (
        "expected the tests to reach the module through the fixture algo, and never to import mymath")
    tree = ast.parse(TEST_FILE.read_text(encoding="utf-8"))
    names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    names |= {node.arg for node in ast.walk(tree) if isinstance(node, ast.arg)}
    assert "mymath" not in names, "expected no use of mymath (not even its fixture) in the tests of the example"


def test_example_conftest_is_the_kit_one():
    """Same contract as depart/conftest.py: only the docstring and MODULE_NAME differ."""
    def body(path: Path) -> str:
        source = path.read_text(encoding="utf-8")
        docstring = ast.get_docstring(ast.parse(source), clean=False)
        source = source.replace(f'"""{docstring}"""', "", 1)
        return re.sub(r'^MODULE_NAME = .*$', "MODULE_NAME = ...", source, count=1, flags=re.MULTILINE)

    kit = PROJECT / "depart" / "conftest.py"
    assert body(EXAMPLE / "conftest.py") == body(kit), (
        "expected exemple/conftest.py to be depart/conftest.py with another docstring and MODULE_NAME: copy the kit's "
        "file again")


def test_example_cadrage_fits_on_one_page():
    words = len((EXAMPLE / "cadrage.md").read_text(encoding="utf-8").split())
    assert words <= 600, f"expected a cadrage of 600 words at most (GRILLE.md, PS.1), got {words}"


def _table_rows(text: str) -> dict[str, list[list[str]]]:
    """The rows of the tables of a grid, by section (« PS.1 » … « PS.E1 », « pénalités »), cut on unescaped pipes."""
    rows, section = {}, None
    for line in text.splitlines():
        match = re.match(r"## (PS\.\w+|Les pénalités)", line)
        if match:
            section = match.group(1)
        elif line.startswith("## "):
            section = None
        elif section and line.startswith("| ") and not line.startswith("| Fait |"):
            rows.setdefault(section, []).append([cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip()[1:-1])])
    return rows


def test_example_grid_has_the_criteria_points_and_checks_of_the_grid():
    """exemple/grille.md is GRILLE.md filled: same rows, same « Critère », « Pts » and « Comment le vérifier »
    (five cells per row: an unescaped | would cut a cell), each row ticked, not applied or « sans objet »."""
    grid, filled = _table_rows((PROJECT / "GRILLE.md").read_text(encoding="utf-8")), _table_rows(
        (EXAMPLE / "grille.md").read_text(encoding="utf-8"))
    assert list(filled) == list(grid), f"expected the sections of GRILLE.md {list(grid)}, got {list(filled)}"
    for section, rows in grid.items():
        assert len(filled[section]) == len(rows), (
            f"expected {len(rows)} rows in {section} of exemple/grille.md, got {len(filled[section])}")
        for k, (row, mine) in enumerate(zip(rows, filled[section]), start=1):
            assert len(mine) == 5, f"expected 5 cells in row {k} of {section} of exemple/grille.md, got {len(mine)}"
            assert mine[1:4] == row[1:4], (
                f"expected row {k} of {section} to copy GRILLE.md (Critère, Pts, Comment le vérifier), got {mine[1:4]}")
            assert mine[0] in ("[x]", "[ ]", "sans objet") and mine[4], (
                f"expected row {k} of {section} to be ticked, or not applied, or « sans objet », with a proof")


def test_example_markdown_latex_is_clean():
    """GRILLE.md, PS.9: $ and $$ paired in each Markdown cell, no \\newcommand nor \\begin{align}, and a \\tag on
    each equation cited by its number."""
    nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    cells = ["".join(cell["source"]) for cell in nb["cells"] if cell["cell_type"] == "markdown"]
    for i, text in enumerate(cells):
        text = re.sub(r"`[^`]*`", "", text)
        displays = text.count("$$")
        inline = text.replace("$$", "").count("$")
        assert displays % 2 == 0 and inline % 2 == 0, (
            f"expected paired $ and $$ in Markdown cell {i}, got {displays} $$ and {inline} $")
    text = "\n".join(cells)
    assert "\\newcommand" not in text and "\\begin{align" not in text, "expected MathJax only (no \\newcommand, align)"
    tags = re.findall(r"\\tag\{(\d+\.\d+)\}", text)
    assert len(tags) == len(set(tags)), f"expected each \\tag once, got {sorted(tags)}"
    cited = set(re.findall(r"\((\d\.\d{1,2})\)", re.sub(r"\\tag\{[\d.]+\}", "", text)))
    untagged = sorted(cited - set(tags))
    assert not untagged, f"expected a \\tag on each cited equation, missing for: {untagged}"
