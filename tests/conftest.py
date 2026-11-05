"""Shared pytest configuration.

Choose which implementation of mymath the tests run against:

    pytest                      # your code: mon_travail/mymath (default)
    pytest --impl=ref           # the reference: solutions/mymath_ref
    pytest --impl=stubs         # the empty skeletons (all mymath tests must fail)

Tests of mymath modules use the ``mymath_module`` fixture (one module, skipped if
you have not created it yet: one summary line lists those modules); the ``mymath``
fixture (the whole package) is for the infrastructure tests only.
``pytest tests/ -m mymath`` runs the tests of the library only (``tests/infra/``
tests the tooling of the workbook).
With your code (``--impl=learner``), a module you do not have yet is taken from
the reference when another module needs it (e.g. your ``ensemble.py`` imports
``tree.py``), but only your own modules are tested.
A function that still raises ``NotImplementedError`` is reported as a short
"⏳ pas encore implémenté" failure instead of a long traceback, and a module that cannot
be imported (a ``SyntaxError``...) stops the session with one line that names its file
and line.
The one-line summaries of ``pytest -rf`` (what the notebooks print) always carry a
reason: the ⏳ message for a function not written yet, and, for the NumPy assertions
whose message starts with an empty line, their first lines and the expected and
obtained values.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

# The repository (WBM_ROOT when the tests of the mechanism copy this file elsewhere)
ROOT = Path(os.environ.get("WBM_ROOT") or Path(__file__).resolve().parents[1])
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))  # `import wbm` works without `pip install -e .`

_STATE: dict = {"impl": None, "path": None, "module": None, "error": None}
_MISSING: dict[str, str] = {}   # mymath modules the learner has not created yet -> their chapter


def _chapter_of(name: str) -> str:
    """The chapter whose ``start_chapter.py`` copies the module ``name`` (MANIFEST.json), or ``<chapitre>``."""
    from wbm.impl import _manifest

    rel = name.replace(".", "/")
    for cid, files in _manifest(ROOT).get("chapters", {}).items():
        if f"{rel}.py" in files or f"{rel}/__init__.py" in files:
            return cid
    return "<chapitre>"


def _skip_missing(full: str, name: str):
    chapter = _MISSING.setdefault(full, _chapter_of(name))
    pytest.skip(f"{full} ({chapter}) n'existe pas encore : lance python tools/start_chapter.py {chapter}")


def pytest_addoption(parser):
    group = parser.getgroup("mymath", "workbook: implementation of mymath under test")
    group.addoption(
        "--impl",
        choices=["learner", "ref", "stubs"],
        default=os.environ.get("WBM_IMPL", "learner"),
        help="learner = mon_travail/mymath (default), ref = solutions/mymath_ref, "
        "stubs = templates/mymath_stubs",
    )
    group.addoption(
        "--run-network",
        action="store_true",
        default=False,
        help="also run the tests that download data (public datasets)",
    )
    group.addoption(
        "--learner-dir",
        default=None,
        help="use another directory as the learner's package (tests of the mechanism)",
    )


def pytest_configure(config):
    from wbm.impl import load_mymath, mymath_path

    impl = config.getoption("--impl")
    learner_dir = config.getoption("--learner-dir")
    path = Path(learner_dir) if (impl == "learner" and learner_dir) else mymath_path(impl, ROOT)
    _STATE.update(impl=impl, path=path)
    try:
        _STATE["module"] = load_mymath(
            impl, path=path if learner_dir else None, root=ROOT,
            fallback="ref" if impl == "learner" else None, notify=False,
        )
    except ImportError as exc:  # includes MymathNotFoundError
        _STATE["error"] = str(exc)
    os.environ["WBM_IMPL"] = impl


def pytest_report_header(config):
    status = "OK" if _STATE["module"] is not None else f"absent ({_STATE['error']})"
    return f"mymath : implémentation « {_STATE['impl']} » -> {_STATE['path']} [{status}]"


@pytest.fixture(scope="session")
def mymath():
    """The mymath package selected with --impl (skips if it does not exist).

    For the tests of the infrastructure only. Tests of mymath modules use
    ``mymath_module``: in learner mode, a module missing from the learner's library
    is served by the reference (fallback), so accessing it through this fixture would
    test the reference instead of the learner (guarded by tests/infra/test_syllabus.py).
    """
    if _STATE["module"] is None:
        pytest.skip(f"mymath introuvable : {_STATE['error']}")
    return _STATE["module"]


def _session_package():
    """Put the package selected with --impl back in ``sys.modules`` if a test loaded another implementation.

    The tests of the mechanism call ``wbm.load_mymath("ref")`` or ``("stubs")``, which replaces
    ``sys.modules["mymath"]`` (and removes the learner's fallback finder). A test of a mymath module that runs
    afterwards would otherwise import that other implementation, not the one selected (``pytest tests/`` would
    then test the reference instead of the learner's code).
    """
    module = _STATE["module"]
    if module is not None and sys.modules.get("mymath") is not module:
        from wbm.impl import _forget

        _forget("mymath")                        # the other implementation and its submodules
        sys.modules["mymath"] = module
        finder = getattr(module, "__wb_fallback__", None)
        if finder is not None:                    # learner mode: modules of earlier chapters from the reference
            sys.meta_path.insert(0, finder)
    return module


@pytest.fixture(scope="session")
def mymath_module(mymath):
    """Import one mymath module by name: ``metrics = mymath_module("metrics")``.

    Skips the test (instead of failing) when the module has not been copied yet. Always imports from the
    implementation selected with --impl, even after a test of the mechanism loaded another one.
    """
    import importlib

    def _import(name: str):
        _session_package()
        full = f"mymath.{name}"
        if _STATE["impl"] == "learner":  # test only the modules the learner has
            rel = Path(*name.split("."))
            base = Path(_STATE["path"])
            present = (base / rel).with_suffix(".py").exists() or (
                base / rel / "__init__.py").exists()
            if not present:
                _skip_missing(full, name)
        try:
            return importlib.import_module(full)
        except ModuleNotFoundError as exc:
            if exc.name and (full == exc.name or full.startswith(exc.name + ".")):
                _skip_missing(full, name)
            pytest.exit(_import_failure(exc), returncode=1)
        except Exception as exc:  # noqa: BLE001 - a SyntaxError (or any error) while the module is imported
            pytest.exit(_import_failure(exc), returncode=1)

    return _import


def _import_failure(exc: BaseException) -> str:
    """One line for a mymath module that cannot be imported (instead of one long traceback per test).

    For a SyntaxError, the file and line come from the exception; otherwise from the deepest frame of the
    traceback inside the package under test (or inside the workbook).
    """
    import traceback

    if isinstance(exc, SyntaxError):
        filename, line, reason = exc.filename, exc.lineno, exc.msg
    else:
        frames = traceback.extract_tb(exc.__traceback__)
        package = str(Path(_STATE["path"] or ROOT).resolve())
        inside = [f for f in frames if str(Path(f.filename).resolve()).startswith(package)] or frames[-1:]
        filename = inside[-1].filename if inside else None
        line = inside[-1].lineno if inside else None
        reason = str(exc)
    where = "un module de mymath"
    if filename:
        path = Path(filename).resolve()
        try:
            where = str(path.relative_to(ROOT.resolve()))
        except ValueError:
            where = str(path)
    at = f" ligne {line}" if line else ""
    return (f"❌ {where} ne s'importe pas : {type(exc).__name__}{at} : {reason}. "
            "Corrige ce fichier, puis relance pytest.")


def pytest_terminal_summary(terminalreporter):
    """One line for the modules not created yet, instead of one SKIPPED line per test."""
    if _STATE["module"] is None and terminalreporter.stats.get("skipped"):
        error = _STATE["error"] or ""
        why = ("ta librairie n'existe pas encore (mon_travail/mymath/) : python tools/start_chapter.py --init la crée"
               if "n'existe pas" in error else f"ta librairie ne se charge pas ({error})")
        terminalreporter.write_line(f"ℹ️ Tests de mymath ignorés : {why}.")
        return
    if not _MISSING:
        return
    shown = ", ".join(f"{full} ({chapter})" for full, chapter in list(_MISSING.items())[:4])
    more = f" et {len(_MISSING) - 4} autre(s)" if len(_MISSING) > 4 else ""
    terminalreporter.write_line(
        f"ℹ️ Tests ignorés : {len(_MISSING)} module(s) de mymath pas encore créé(s), {shown}{more} ; "
        "python tools/start_chapter.py <chapitre> copie le squelette du chapitre.")


def pytest_collection_modifyitems(config, items):
    run_network = config.getoption("--run-network")
    skip_network = pytest.mark.skip(reason="télécharge des données : relance avec --run-network")
    for item in items:
        if "network" in item.keywords and not run_network:
            item.add_marker(skip_network)
        if {"mymath", "mymath_module"} & set(getattr(item, "fixturenames", ())):
            item.add_marker(pytest.mark.mymath)


class _PendingRepr:
    """A one-line failure report that `pytest -rf` and `--tb=line` also show (a plain string has no crash line)."""

    def __init__(self, text: str):
        self.text = text
        self.reprcrash = self

    @property
    def message(self) -> str:
        return self.text

    def toterminal(self, tw) -> None:
        tw.line(self.text)

    def __str__(self) -> str:
        return self.text


def _numpy_summary(text: str) -> str | None:
    """One line out of a NumPy assertion message, whose first line is empty (`-rf` would show nothing)."""
    if not text.startswith("\n"):
        return None
    labels = ("ACTUAL:", "DESIRED:", "x:", "y:")
    skip = ("Mismatched elements", "Max absolute", "Max relative")
    head, arrays, current = [], {}, None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        label = next((lab for lab in labels if line.startswith(lab)), None)
        if label:
            current = label
            arrays[label] = line[len(label):].strip()
        elif current:
            arrays[current] += " " + line          # continuation of a multi-line array
        elif not line.startswith(skip):
            head.append(line)
    parts = head[:2]
    got = arrays.get("ACTUAL:") or arrays.get("x:")
    expected = arrays.get("DESIRED:") or arrays.get("y:")
    if expected and got:
        parts.append(f"expected {' '.join(expected.split())}, got {' '.join(got.split())}")
    return " | ".join(parts) or None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or call.excinfo is None:
        return
    if call.excinfo.errisinstance(NotImplementedError):
        message = str(call.excinfo.value) or "fonction pas encore écrite"
        report.longrepr = _PendingRepr(f"⏳ pas encore implémenté : {message}")
    elif call.excinfo.errisinstance(AssertionError):
        summary = _numpy_summary(str(call.excinfo.value))
        crash = getattr(report.longrepr, "reprcrash", None)
        if summary and crash is not None:
            crash.message = f"AssertionError: {summary}"
