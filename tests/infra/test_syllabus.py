"""Tests of tools/syllabus.py and of the syllabus data (BIBLE §8, §13)."""

import ast
import copy
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "src"))

import syllabus  # noqa: E402
from wbm import chapters as wch  # noqa: E402

STUBS = ROOT / "templates" / "mymath_stubs"


@pytest.fixture(scope="module")
def data():
    return syllabus.load(), syllabus.load_coverage(), syllabus.load_snapshot()


# ---------------------------------------------------------------- the real data
def test_syllabus_has_no_error_and_no_warning(data):
    chapters, coverage, snapshot = data
    errors, warnings = syllabus.check(chapters, coverage, snapshot)
    assert errors == []
    assert warnings == []


def test_every_chapter_in_study_order(data):
    chapters, _, _ = data
    assert list(chapters) == list(wch.CHAPTER_ORDER)


def test_generated_documents_are_up_to_date(data):
    """`python tools/syllabus.py build` was run after the last change of the data."""
    chapters, coverage, snapshot = data
    _, warnings = syllabus.check(chapters, coverage, snapshot)
    stale = [str(path.relative_to(ROOT)) for path, text in syllabus.render(chapters, warnings, coverage,
                                                                          snapshot).items()
             if not path.exists() or path.read_text(encoding="utf-8") != text]
    assert stale == [], f"run `python tools/syllabus.py build` (stale: {stale})"


DETAILED_PARTS = {"0", "I"}  # a part is detailed in its syllabus session (BIBLE §24): add it here then


def test_detailed_parts_are_detailed_and_later_parts_planned(data):
    chapters, _, _ = data
    for cid, ch in chapters.items():
        assert ch["detailed"] == (ch["part"] in DETAILED_PARTS), cid


def test_every_ia_notion_with_maths_is_covered(data):
    """Each workbookIA chapter with maths has a coverage entry; chapters without maths are known."""
    _, coverage, snapshot = data
    no_maths = {"1", "15", "23", "24", "29", "B1", "B7"}
    for ia in snapshot["chapters"]:
        if ia in ("0A",) or ia in no_maths:
            continue
        assert ia in coverage, f"workbookIA {ia} has no coverage entry"


def test_coverage_report_lists_every_entry(data):
    _, coverage, snapshot = data
    text = syllabus.build_coverage(coverage, snapshot)
    for ia, notions in coverage.items():
        for notion in notions:
            assert notion in text, (ia, notion)


# ---------------------------------------------------------------- mymath stubs
def _stub_functions(path: Path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return [n for n in tree.body if isinstance(n, ast.FunctionDef) and not n.name.startswith("_")]


def test_manifest_lists_existing_files_only():
    manifest = json.loads((STUBS / "MANIFEST.json").read_text(encoding="utf-8"))
    listed = list(manifest["base"]) + [f for files in manifest["chapters"].values() for f in files]
    assert len(listed) == len(set(listed)), "a stub is listed twice"
    for name in listed:
        assert (STUBS / name).is_file(), name
    on_disk = {p.name for p in STUBS.glob("*.py")}
    assert on_disk == set(listed), f"stubs not in MANIFEST.json: {sorted(on_disk - set(listed))}"
    for cid in manifest["chapters"]:
        assert cid in wch.CHAPTER_ORDER, cid


def test_manifest_chapters_match_the_syllabus(data):
    chapters, _, _ = data
    manifest = json.loads((STUBS / "MANIFEST.json").read_text(encoding="utf-8"))
    for cid, files in manifest["chapters"].items():
        assert chapters[cid]["detailed"], f"{cid}: a stub is published before its chapter is detailed"
        assert chapters[cid]["mymath"]["module"] in files, cid


@pytest.mark.parametrize("path", sorted(STUBS.glob("*.py")), ids=lambda p: p.name)
def test_stub_functions_are_documented_skeletons(path):
    """Each public function: a NumPy-style docstring and a body that ends with raise NotImplementedError."""
    for fn in _stub_functions(path):
        doc = ast.get_docstring(fn)
        assert doc and "Returns" in doc and "Examples" in doc, f"{path.name}:{fn.name} docstring"
        last = fn.body[-1]
        assert isinstance(last, ast.Raise), f"{path.name}:{fn.name} must end with raise NotImplementedError"
        assert "NotImplementedError" in ast.unparse(last.exc), f"{path.name}:{fn.name}"
        assert len(fn.body) == 2, f"{path.name}:{fn.name} must contain only the docstring and the raise"


@pytest.mark.parametrize("path", sorted(STUBS.glob("*.py")), ids=lambda p: p.name)
def test_stub_functions_raise_not_implemented(path):
    if path.name == "__init__.py":
        pytest.skip("package file")
    spec = importlib.util.spec_from_file_location(f"stub_{path.stem}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for fn in _stub_functions(path):
        n_required = len([a for a in fn.args.args]) - len(fn.args.defaults)
        with pytest.raises(NotImplementedError):
            getattr(module, fn.name)(*([None] * n_required))


# ---------------------------------------------------------------- the checks catch mistakes
def _errors(chapters, coverage=None, snapshot=None):
    _, real_cov, real_snap = syllabus.load(), syllabus.load_coverage(), syllabus.load_snapshot()
    return syllabus.check(chapters, real_cov if coverage is None else coverage,
                          real_snap if snapshot is None else snapshot)[0]


def test_check_catches_a_later_prerequisite(data):
    chapters = copy.deepcopy(data[0])
    chapters["R1"]["after"] = ["R5"]
    assert any("R1: 'after' names R5" in e for e in _errors(chapters))


def test_check_catches_a_bad_exercise_id(data):
    chapters = copy.deepcopy(data[0])
    chapters["R1"]["exercises"][-1]["id"] = "R1.99"
    assert any("R1.99" in e for e in _errors(chapters))


def test_check_catches_an_uncovered_section(data):
    chapters = copy.deepcopy(data[0])
    chapters["R2"]["sections"].append(("§99", "Section fantôme"))
    assert any("§99" in e for e in _errors(chapters))


def test_check_catches_a_missing_mymath_function(data):
    chapters = copy.deepcopy(data[0])
    chapters["R3"]["mymath"]["functions"] = chapters["R3"]["mymath"]["functions"] + ["integrate"]
    errors = _errors(chapters)
    assert any("functions of functions.py" in e for e in errors)
    assert any("no 🔨 writes functions.py:integrate" in e for e in errors)


def test_check_catches_a_wrong_special_dir(data):
    chapters = copy.deepcopy(data[0])
    chapters["CP0"]["dir"] = "checkpoints/partie_9"
    assert any("CP0: dir must be 'checkpoints/partie_0'" in e for e in _errors(chapters))


def test_check_catches_a_notion_taught_too_late(data):
    chapters, coverage, snapshot = data
    coverage = copy.deepcopy(coverage)
    coverage["3"] = dict(coverage["3"])
    first = next(iter(coverage["3"]))
    coverage["3"][first] = "M12c"
    assert any(f"« {first} » is taught by M12c, after workbookIA 3" in e
               for e in _errors(copy.deepcopy(chapters), coverage, snapshot))


def test_check_catches_an_unknown_ia_notion(data):
    chapters, coverage, snapshot = data
    coverage = copy.deepcopy(coverage)
    coverage["3"] = dict(coverage["3"], **{"notion inventée": "M03"})
    assert any("notion inventée" in e for e in _errors(copy.deepcopy(chapters), coverage, snapshot))


# ---------------------------------------------------------------- helpers
def test_parse_exercise_flags():
    ex = syllabus.parse_exercise(("R1.21", "🔨", 2, 25, "PGCD", "§3 §4", "E m:gcd,simplify_fraction p:R1.5"), "R1")
    assert ex["tracks"] == ["complet", "essentiel"]
    assert ex["mymath"] == ["gcd", "simplify_fraction"]
    assert ex["prereq"] == ["R1.5"]
    assert ex["covers"] == ["§3", "§4"]
    assert ex["check"] == "pytest" and ex["file"] == "03"
    paper = syllabus.parse_exercise(("R1.1", "✏️", 1, 10, "Calcul", "§1", ""), "R1")
    assert paper["file"] == "02" and paper["check"] == "wbm" and paper["tracks"] == ["complet"]
    with pytest.raises(syllabus.SyllabusError):
        syllabus.parse_exercise(("R1.1", "✏️", 1, 10, "Calcul", "§1", "X"), "R1")


@pytest.mark.parametrize("cid, folder", [("POS", "positionnement"), ("CP0", "checkpoints/partie_0"),
                                         ("CP6", "checkpoints/partie_6"), ("PS", "projets/projet_synthese"),
                                         ("R7", "chapitres/r7_limites_derivation")])
def test_folder(data, cid, folder):
    assert syllabus.folder(data[0][cid]) == folder


def test_published_ignores_gitkeep(data, tmp_path):
    ch = data[0]["R1"]
    path = tmp_path / syllabus.folder(ch)
    path.mkdir(parents=True)
    (path / ".gitkeep").write_text("")
    assert not syllabus.published(ch, tmp_path)
    (path / "01_fiche.md").write_text("# R1")
    assert syllabus.published(ch, tmp_path)
    (path / "EN_COURS.md").write_text("")
    assert not syllabus.published(ch, tmp_path)


def test_hours_label():
    assert syllabus.hours_label(90) == "1,5 h"
    assert syllabus.hours_label(None) == "?"


# ---------------------------------------------------------------- sharing rule, 0A sync, mylearn (BIBLE §24)
def test_check_catches_an_unknown_frontier(data):
    chapters = copy.deepcopy(data[0])
    chapters["R5"]["frontieres"] = chapters["R5"]["frontieres"] + ["11.999"]
    assert any("R5: frontieres names 11.999" in e for e in _errors(chapters))


def test_check_catches_an_unknown_0a_section(data):
    chapters = copy.deepcopy(data[0])
    chapters["R1"]["python_0a"] = ["100.99"]
    assert any("R1: python_0a names §100.99" in e for e in _errors(chapters))


def test_detailed_chapters_declare_frontiers_and_0a_sync(data):
    chapters = copy.deepcopy(data[0])
    del chapters["R2"]["frontieres"]
    del chapters["R3"]["python_0a"]
    errors = _errors(chapters)
    assert any("R2: a detailed chapter needs 'frontieres'" in e for e in errors)
    assert any("R3: a detailed chapter needs 'python_0a'" in e for e in errors)


def test_check_catches_a_mymath_function_that_duplicates_mylearn(data):
    chapters = copy.deepcopy(data[0])
    chapters["M06"]["mymath"] = {"module": "info.py", "functions": ["entropy", "mutual_information"]}
    assert any("M06: mymath info.py duplicates the mylearn function(s) ['entropy']" in e for e in _errors(chapters))
    chapters["M06"]["mylearn_overlap"] = ["entropy"]
    assert not any(e.startswith("M06: mymath") for e in _errors(chapters))


def test_frontiers_include_every_proof_of_the_prepared_chapter(data):
    snapshot = data[2]
    ch = data[0]["M19"]
    proofs = [k for k, (kind, _) in snapshot["chapters"]["19"]["exercises"].items() if kind == "∂"]
    assert proofs and all(p in syllabus.frontier_ids(ch, snapshot) for p in proofs)


def test_part_0_does_not_solve_the_proofs_of_0b(data):
    """No part-0 exercise reuses the title of a 0B proof (the sharing rule, checked on titles)."""
    snapshot = data[2]
    proof_titles = {t.lower() for kind, t in snapshot["chapters"]["0B"]["exercises"].values() if kind == "∂"}
    for cid, ch in data[0].items():
        for ex in ch["exercises"]:
            assert ex["title"].lower() not in proof_titles, ex["id"]


def test_sync_with_0a_is_monotonic(data):
    order = [ref for ref, _ in syllabus.sections_0a(data[2])]
    upto = list(syllabus.sync_0a_upto(data[0]).values())
    assert [order.index(r) for r in upto] == sorted(order.index(r) for r in upto)


def test_snapshot_tool_reads_mylearn_names():
    import snapshot_workbookia
    chapter = {"mylearn": [{"api": [{"signature": "def entropy(p: ArrayLike) -> float"},
                                    {"signature": "class KMeans:"}, {"signature": "x = 1"}]}]}
    assert snapshot_workbookia._mylearn_names(chapter) == ["entropy", "KMeans"]
