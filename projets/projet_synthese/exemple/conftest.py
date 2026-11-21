"""pytest configuration of the worked example (projets/projet_synthese/exemple): the kit's conftest.py, copied.

    python -m pytest -q test_poisson_newton.py --impl=ref                            # the example runs on the reference
    python -m pytest -q test_poisson_newton.py --impl=ref --mutant=newton_direction  # PS.7: the mutation of mutants.py

Run them from this folder, or from the workbook folder
(python -m pytest -q projets/projet_synthese/exemple/test_poisson_newton.py --impl=ref).
From a copy placed elsewhere, give the workbook folder in WBM_ROOT.

The only differences with depart/conftest.py: this docstring, and MODULE_NAME (the module of the example is
poisson_newton.py). What this file provides to test_poisson_newton.py:

* the fixture ``algo``: the module poisson_newton.py, imported once (with the mutations of ``--mutant`` applied);
  its tests are skipped with ⏳ while the library mymath selected by ``--impl`` does not exist;
* the fixture ``mymath``: the library selected by ``--impl`` (learner: mon_travail/mymath, a module you do not
  have comes from the reference and is listed at the end; ref: solutions/mymath_ref; stubs: the empty skeletons);
* a test that stops on ``NotImplementedError`` is skipped with ⏳.
"""

from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
MODULE_NAME = "poisson_newton"   # the module of the example: poisson_newton.py
MUTANTS_NAME = "mutants"    # the deliberate mistakes of PS.7: mutants.py


def _find_root() -> Path | None:
    """The workbookMaths folder: WBM_ROOT, else the first parent folder that contains src/wbm."""
    env = os.environ.get("WBM_ROOT")
    if env and (Path(env) / "src" / "wbm").is_dir():
        return Path(env).resolve()
    for folder in (HERE, *HERE.parents):
        if (folder / "src" / "wbm").is_dir():
            return folder
    return None


ROOT = _find_root()
if ROOT is not None and str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))     # `import wbm` without `pip install -e .`
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))             # `import algo` and `import mutants` from this folder

_STATE: dict = {"impl": None, "mymath": None, "error": None, "mutants": []}


def pytest_addoption(parser):
    group = parser.getgroup("mymath", "workbook: implementation of mymath under test")
    try:
        group.addoption("--impl", choices=["learner", "ref", "stubs"],
                        default=os.environ.get("WBM_IMPL", "learner"),
                        help="learner = mon_travail/mymath (default), ref = solutions/mymath_ref, "
                             "stubs = templates/mymath_stubs")
    except ValueError:      # already added by another conftest.py of the workbook (one pytest run on two folders)
        pass
    project = parser.getgroup("synthese", "synthesis project")
    try:
        project.addoption("--mutant", default="",
                          help="PS.7: comma-separated names of functions of algo.py replaced by those of mutants.py")
    except ValueError:
        pass


def pytest_configure(config):
    impl = config.getoption("--impl")
    _STATE["impl"] = impl
    _STATE["mutants"] = [name.strip() for name in config.getoption("--mutant").split(",") if name.strip()]
    if ROOT is None:
        _STATE["error"] = ("dépôt workbookMaths introuvable : lance pytest depuis son dossier, ou donne son chemin "
                           "dans la variable WBM_ROOT")
        return
    from wbm.impl import load_mymath

    try:
        if impl == "learner":    # yours; a module you do not have comes from the reference
            _STATE["mymath"] = load_mymath("learner", root=ROOT, fallback="ref", chapter="PS", notify=False)
        else:
            _STATE["mymath"] = load_mymath(impl, root=ROOT)
    except ImportError as exc:  # includes MymathNotFoundError: mon_travail/mymath does not exist yet
        _STATE["error"] = (str(exc) if impl != "learner" or "n'existe pas encore" not in str(exc) else
                           "ta librairie n'existe pas encore dans mon_travail/mymath/ (le projet appelle les fonctions "
                           "que tu as écrites dans les chapitres ; python tools/start_chapter.py --init crée le dossier)")
    os.environ["WBM_IMPL"] = impl


def pytest_report_header(config):
    status = "OK" if _STATE["mymath"] is not None else f"absente ({_STATE['error']})"
    return f"mymath : implémentation « {_STATE['impl']} » [{status}]"


@pytest.fixture(scope="session")
def mymath():
    """The mymath package selected with --impl (the tests that need it are skipped with ⏳ while it is missing)."""
    if _STATE["mymath"] is None:
        pytest.skip(f"⏳ mymath absente : {_STATE['error']}")
    return _STATE["mymath"]


def _apply_mutants(module) -> None:
    """Replace module.<name> by mutants.<name> for each name given to --mutant (PS.7)."""
    if not _STATE["mutants"]:
        return
    try:
        mutants = importlib.import_module(MUTANTS_NAME)
    except ModuleNotFoundError:
        pytest.exit(f"❌ --mutant : pas de fichier {MUTANTS_NAME}.py à côté de {MODULE_NAME}.py", returncode=4)
    for name in _STATE["mutants"]:
        if not callable(getattr(mutants, name, None)):
            pytest.exit(f"❌ --mutant={name} : {MUTANTS_NAME}.py n'a pas de fonction {name}()", returncode=4)
        if not hasattr(module, name):
            pytest.exit(f"❌ --mutant={name} : {MODULE_NAME}.py n'a pas de fonction {name}() à remplacer", returncode=4)
        setattr(module, name, getattr(mutants, name))


@pytest.fixture(scope="session")
def algo(mymath):
    """Your module algo.py, imported once, with the mutations of --mutant applied."""
    try:
        module = importlib.import_module(MODULE_NAME)
    except ModuleNotFoundError as exc:
        if (exc.name or "").startswith("mymath"):
            pytest.skip(f"⏳ {MODULE_NAME}.py utilise {exc.name}, absent de ta librairie : lance "
                        "python tools/start_chapter.py <chapitre> pour ce module")
        raise
    _apply_mutants(module)
    return module


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """A test stopped by NotImplementedError (a function not written yet) is skipped with ⏳, not failed."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and call.excinfo is not None and call.excinfo.errisinstance(NotImplementedError):
        message = str(call.excinfo.value) or "fonction pas encore écrite"
        message = message.replace(" is not implemented yet", " n'est pas encore écrite")
        line = (item.location[1] or 0) + 1
        report.outcome = "skipped"
        report.longrepr = (str(item.path), line, f"⏳ pas encore écrit : {message}")


def pytest_terminal_summary(terminalreporter):
    """One ℹ️ line for what the summary does not say: tests waiting, mutation applied, modules of the reference."""
    skipped = terminalreporter.stats.get("skipped", [])
    pending = [report for report in skipped if "⏳" in str(report.longrepr)]
    if _STATE["mymath"] is None and skipped:
        terminalreporter.write_line(f"ℹ️ Tests sautés : mymath absente ({_STATE['error']}).")
    elif pending:
        terminalreporter.write_line(f"ℹ️ {len(pending)} test(s) en attente ⏳ (squelettes à écrire ou fonctions pas "
                                    "encore écrites) : le projet est fini quand plus rien n'est sauté.")
    if _STATE["mutants"]:
        swapped = ", ".join(f"{MODULE_NAME}.{name} ← {MUTANTS_NAME}.{name}" for name in _STATE["mutants"])
        terminalreporter.write_line(f"ℹ️ Mutation : {swapped} ; au moins un test doit échouer.")
    finder = getattr(_STATE["mymath"], "__wb_fallback__", None)
    used = sorted(set(getattr(finder, "used", []) or []))
    if used:
        terminalreporter.write_line("ℹ️ Pris dans la référence (absents de ta librairie) : " + ", ".join(used) + ".")
