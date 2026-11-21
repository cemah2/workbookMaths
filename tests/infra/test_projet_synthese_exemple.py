"""The worked example of the synthesis project (projets/projet_synthese/exemple, BIBLE §18).

Its tests pass on the reference of mymath and catch its two mutations (in a subprocess, with --impl=ref, as the
notebook runs them); its notebook is executed, without an error output and without the phrases that replace a
calculation (GRILLE.md, PS.3); its module imports only NumPy, math and mymath; its tests import their oracles and
never mymath; its conftest.py is the kit's one; its cadrage fits on one page.
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
