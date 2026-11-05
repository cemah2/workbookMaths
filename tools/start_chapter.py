#!/usr/bin/env python
"""Copy a chapter's exercise notebook and mymath stubs into mon_travail/.

    python tools/start_chapter.py R3        # a catch-up chapter (studied during workbookIA 0A)
    python tools/start_chapter.py M12c      # one math chapter
    python tools/start_chapter.py 12        # ALL the math chapters to study before workbookIA ch. 12 (M12a-M12d)
    python tools/start_chapter.py CP1       # the mock exam of part I (just before workbookIA's checkpoint I)
    python tools/start_chapter.py POS       # the placement test (before R0)
    python tools/start_chapter.py PS        # the final synthesis project (its starter kit)
    python tools/start_chapter.py --init    # create mon_travail/mymath (base files) and mon_travail/suivi
    python tools/start_chapter.py M12c --dry-run

What is copied (NEVER overwriting an existing file):
  chapitres/<chapter>/03_notebook.ipynb   -> mon_travail/<chapter>/03_notebook.ipynb
  chapitres/<chapter>/06_mes_reponses.md  -> mon_travail/<chapter>/06_mes_reponses.md
  mymath stubs listed in templates/mymath_stubs/MANIFEST.json
      (the "base" files + the chapter's files) -> mon_travail/mymath/
  for a mock exam CPn:
  checkpoints/partie_n/02_examen_notebook.ipynb and 04_mes_reponses.md
                                          -> mon_travail/checkpoints/partie_n/
  for the placement test POS:
  positionnement/02_notebook.ipynb and 04_mes_reponses.md -> mon_travail/positionnement/
  for the synthesis project PS:
  projets/projet_synthese/depart/*        -> mon_travail/projet_synthese/ (its starter kit)
  your tracking files (models in suivi/)  -> mon_travail/suivi/
      tableau_de_bord.md, auto_evaluation.md, journal.md: copied once; later,
      sections published by Claude (<!-- wbm:section ID --> ... <!-- wbm:end ID -->)
      are APPENDED to your copy if missing. Your ticks and notes are never touched;
      a section of the dashboard that changed in the model since your copy is reported.

A chapter still being generated contains a file EN_COURS.md: its notebook is not
copied yet (a half-written copy would never be completed, since your files are
never overwritten); run the same command again when the chapter is finished, or
pass --force.

The mymath modules of EARLIER chapters are not copied: if you skipped one, the
notebooks and the tests take it from the reference (solutions/mymath_ref), and
this script lists them. Run start_chapter for that chapter to write it yourself.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))  # wbm without `pip install -e .`
CHAPTERS = ROOT / "chapitres"
STUBS = ROOT / "templates" / "mymath_stubs"
WORK = ROOT / "mon_travail"
CHAPTER_FILES = ("03_notebook.ipynb", "06_mes_reponses.md")
CHECKPOINT_FILES = ("02_examen_notebook.ipynb", "04_mes_reponses.md")   # the learner's copies of a checkpoint
PROJECT_STARTER = "depart"   # sub-folder of a project copied for the learner (a solution never is)
IN_PROGRESS = "EN_COURS.md"   # marker of a chapter that is still being generated
TRACKERS = ("tableau_de_bord.md", "auto_evaluation.md", "journal.md")
SECTION = re.compile(r"<!-- wbm:section (\S+) -->.*?<!-- wbm:end \1 -->\n?", re.S)


from wbm.chapters import TITLES, canonical_ia, chapters_before_ia, checkpoint_number  # noqa: E402
from wbm.chapters import canonical_id as _canonical_math_id  # noqa: E402
from wbm.chapters import dir_prefix  # noqa: E402,F401  (used by the tests and the other tools)

PLACEMENT = "positionnement"
PLACEMENT_FILES = ("02_notebook.ipynb", "04_mes_reponses.md")
SYNTHESIS = "projet_synthese"   # projets/projet_synthese/depart -> mon_travail/projet_synthese


def canonical_id(raw: str) -> str:
    """'r3' -> 'R3', 'm12C' -> 'M12c', 'cp1' -> 'CP1', 'pos' -> 'POS' (a math chapter id)."""
    return _canonical_math_id(raw)


class NoMathsChapter(ValueError):
    """A workbookIA chapter that has no math chapter before it (1, 15, 23, 24, 29, B1, B7, and 0A)."""


def resolve(raw: str) -> list[str]:
    """The math chapters a command names: one id ('M12c'), or a workbookIA chapter ('12' -> M12a-M12d).

    ValueError with a helpful message for an unknown id or a workbookIA chapter without new maths.
    """
    try:
        return [canonical_id(raw)]
    except ValueError as math_error:
        try:
            ia = canonical_ia(raw)
        except ValueError:
            raise math_error from None
        chapters = chapters_before_ia(ia)
        if not chapters:
            if ia == "0A":
                raise NoMathsChapter("workbookIA 0A (Python) se fait en même temps que la remise à niveau R0 à R9 : "
                                     "python tools/start_chapter.py R0") from None
            raise NoMathsChapter(f"Le chapitre {ia} de workbookIA n'a pas de chapitre de maths : passe directement "
                                 "à workbookIA") from None
        return chapters


# What a project notebook writes in its own folder: never part of a starter kit
OUTPUT_DIRS = {"__pycache__", ".ipynb_checkpoints", ".pytest_cache", "figures", ".git"}


def starter_files(project: Path) -> list[Path]:
    """The files of a project's starter kit (``depart/``), without caches nor notebook outputs."""
    starter = project / PROJECT_STARTER
    if not starter.is_dir():
        return []
    return sorted(p for p in starter.rglob("*") if p.is_file()
                  and not OUTPUT_DIRS & set(p.relative_to(starter).parts)
                  and not any(part.endswith(".egg-info") for part in p.relative_to(starter).parts))


def find_chapter_dir(chapter_id: str, chapters: Path = CHAPTERS) -> Path | None:
    prefix = dir_prefix(chapter_id)
    if not chapters.exists():
        return None
    matches = sorted(p for p in chapters.iterdir()
                     if p.is_dir() and (p.name == prefix or p.name.startswith(prefix + "_")))
    return matches[0] if matches else None


def load_manifest(stubs: Path = STUBS) -> dict:
    path = stubs / "MANIFEST.json"
    if not path.exists():
        return {"base": [], "chapters": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def stub_files_for(chapter_id: str | None, manifest: dict, stubs: Path = STUBS) -> list[str]:
    """Base files + the chapter's files + the __init__.py of their sub-packages."""
    files = list(manifest.get("base", []))
    if chapter_id is not None:
        files += manifest.get("chapters", {}).get(chapter_id, [])
    extra = []
    for rel in files:
        parent = Path(rel).parent
        while str(parent) not in ("", "."):
            init = (parent / "__init__.py").as_posix()
            if (stubs / init).exists() and init not in files and init not in extra:
                extra.append(init)
            parent = parent.parent
    ordered = []
    for rel in extra + files:  # parents' __init__.py first
        if rel not in ordered:
            ordered.append(rel)
    return ordered


def missing_earlier_modules(chapter_id: str, manifest: dict, work_mymath: Path) -> dict[str, list[str]]:
    """Modules of the chapters before ``chapter_id`` that the learner does not have."""
    from wbm.impl import CHAPTER_ORDER

    if chapter_id not in CHAPTER_ORDER:
        return {}
    rank = CHAPTER_ORDER.index(chapter_id)
    missing = {}
    for cid, files in manifest.get("chapters", {}).items():
        if cid in CHAPTER_ORDER and CHAPTER_ORDER.index(cid) < rank:
            absent = [f for f in files if not f.endswith("__init__.py")
                      and not (work_mymath / f).exists()]
            if absent:
                missing[cid] = absent
    return missing


def copy_no_overwrite(src: Path, dst: Path, dry_run: bool) -> str:
    """Copy src to dst unless dst exists. Returns 'copied', 'kept' or 'missing'."""
    if not src.exists():
        return "missing"
    if dst.exists():
        return "kept"
    if dry_run:
        return "copied"
    data = src.read_bytes()  # read first: a read error leaves nothing behind
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        with dst.open("xb") as handle:  # "x": fails if the file appeared meanwhile
            handle.write(data)
    except FileExistsError:
        return "kept"
    except BaseException:  # disk full, Ctrl+C...: never leave a truncated file
        dst.unlink(missing_ok=True)
        raise
    return "copied"


def sync_trackers(model_dir: Path, work_dir: Path, dry_run: bool) -> list[tuple[str, str]]:
    """Copy the tracking files once, then append the sections missing from the learner's copy."""
    results = []
    for name in TRACKERS:
        model, mine = model_dir / name, work_dir / name
        if not model.exists():
            continue
        if mine.exists():
            status = "kept"
        elif dry_run:
            status = "copied"
        else:  # first copy, without the "model kept by Claude" banner
            lines = model.read_text(encoding="utf-8").splitlines(keepends=True)
            kept = [line for line in lines if not line.startswith("> **Modèle")]
            mine.parent.mkdir(parents=True, exist_ok=True)
            try:
                with mine.open("x", encoding="utf-8", newline="\n") as handle:
                    handle.write("".join(kept).replace("\n\n\n", "\n\n"))
                status = "copied"
            except FileExistsError:
                status = "kept"
        changed = []
        if status == "kept":
            text = mine.read_text(encoding="utf-8")
            missing = [m.group(0) for m in SECTION.finditer(model.read_text(encoding="utf-8"))
                       if f"<!-- wbm:section {m.group(1)} -->" not in text]
            if missing:
                status = "appended"
                if not dry_run:
                    with mine.open("a", encoding="utf-8", newline="\n") as handle:
                        handle.write(("" if text.endswith("\n") else "\n") + "\n" + "\n".join(missing))
            if name == "tableau_de_bord.md":
                changed = changed_sections(model.read_text(encoding="utf-8"), text)
        results.append((f"mon_travail/suivi/{name}", status))
        if changed:
            results.append((f"mon_travail/suivi/{name} : section(s) {', '.join(changed)}", "changed"))
    return results


def changed_sections(model_text: str, mine_text: str) -> list[str]:
    """Sections of the learner's dashboard where a line of the model is missing (a title, ★ or duration changed).

    Ticks are ignored, and so is what the learner wrote after a line; the copy is never modified.
    """
    def untick(line: str) -> str:
        return re.sub(r"^- \[[xX]\]", "- [ ]", line.rstrip())

    mine = {m.group(1): [untick(line) for line in m.group(0).splitlines()] for m in SECTION.finditer(mine_text)}
    changed = []
    for m in SECTION.finditer(model_text):
        lines = mine.get(m.group(1))
        if lines is not None and any(not any(line.startswith(expected) for line in lines)
                                     for expected in map(untick, m.group(0).splitlines()) if expected):
            changed.append(m.group(1))
    return changed


def chapter_test_files(chapter_id: str, root: Path = ROOT) -> list[str]:
    """The test files of the chapter's mymath modules, e.g. ["tests/test_m12c_eigen.py"] (none for R0)."""
    files = [f"tests/{path.name}" for path in sorted((root / "tests").glob(f"test_{chapter_id.lower()}_*.py"))]
    if chapter_id == "R0" and (root / "tests" / "test_example_mymath.py").exists():
        files.append("tests/test_example_mymath.py")          # _example.mean, written in R0
    return files


ICONS = {"copied": "✅ copié  ", "kept": "🔒 conservé", "missing": "⚠️ absent ",
         "appended": "➕ complété", "later": "⏳ plus tard", "changed": "ℹ️ à revoir"}


def _copy_chapter(chapter_id: str, root: Path, work: Path, dry_run: bool, force: bool, out) -> tuple[list, str | None]:
    """Copy the learner's files of one math chapter, an exam, the placement test or the synthesis project.

    Returns (results, kind) where kind is "chapter", "exam", "placement", "synthesis", or None if absent.
    """
    results: list[tuple[str, str]] = []
    part = checkpoint_number(chapter_id)
    if chapter_id == "PS":
        project = root / "projets" / SYNTHESIS
        if not starter_files(project):
            out(f"❌ Le projet de synthèse n'existe pas encore dans projets/{SYNTHESIS}/ (`git pull` ?).")
            return results, None
        for src in starter_files(project):
            dst = f"{SYNTHESIS}/{src.relative_to(project / PROJECT_STARTER).as_posix()}"
            results.append((f"mon_travail/{dst}", copy_no_overwrite(src, work / dst, dry_run)))
        return results, "synthesis"
    if chapter_id == "POS" or part is not None:
        folder = root / PLACEMENT if chapter_id == "POS" else root / "checkpoints" / f"partie_{part}"
        names = PLACEMENT_FILES if chapter_id == "POS" else CHECKPOINT_FILES
        if not (folder / names[0]).exists():
            what = "Le test de positionnement" if chapter_id == "POS" else f"L'examen blanc {chapter_id}"
            out(f"❌ {what} n'existe pas encore dans {folder.relative_to(root).as_posix()}/ (`git pull` ?).")
            return results, None
        rel_dir = folder.relative_to(root).as_posix()
        for name in names:
            dst = f"{rel_dir}/{name}"
            results.append((f"mon_travail/{dst}", copy_no_overwrite(folder / name, work / dst, dry_run)))
        return results, "placement" if chapter_id == "POS" else "exam"
    chapter_dir = find_chapter_dir(chapter_id, root / "chapitres")
    if chapter_dir is None:
        chapters = root / "chapitres"
        available = sorted(p.name for p in chapters.iterdir() if p.is_dir()) if chapters.exists() else []
        out(f"❌ Le chapitre {chapter_id} ({TITLES.get(chapter_id, '?')}) n'existe pas encore dans chapitres/.")
        out("   Chapitres disponibles : " + (", ".join(available) or "aucun pour l'instant"))
        out("   Astuce : `git pull` pour récupérer les derniers chapitres.")
        return results, None
    in_progress = (chapter_dir / IN_PROGRESS).exists() and not force
    for name in CHAPTER_FILES:
        if in_progress and name.endswith(".ipynb"):
            results.append((f"mon_travail/{chapter_dir.name}/{name}", "later"))
            continue
        status = copy_no_overwrite(chapter_dir / name, work / chapter_dir.name / name, dry_run)
        results.append((f"mon_travail/{chapter_dir.name}/{name}", status))
    return results, "chapter"


def start_chapter(chapter: str | None, *, root: Path = ROOT, dry_run: bool = False,
                  out=print, force: bool = False) -> int:
    """Start one math chapter, all the math chapters before a workbookIA chapter, an exam, POS or PS."""
    stubs = root / "templates" / "mymath_stubs"
    work = root / "mon_travail"
    manifest = load_manifest(stubs)
    chapter_ids = resolve(chapter) if chapter is not None else []
    if len(chapter_ids) > 1:
        out(f"Avant le chapitre {canonical_ia(chapter)} de workbookIA : {', '.join(chapter_ids)}.")
    status_code = 0
    for chapter_id in chapter_ids or [None]:
        status_code = max(status_code, _start_one(chapter_id, root=root, work=work, stubs=stubs, manifest=manifest,
                                                  dry_run=dry_run, out=out, force=force))
    return status_code


def _start_one(chapter_id: str | None, *, root: Path, work: Path, stubs: Path, manifest: dict, dry_run: bool,
               out, force: bool) -> int:
    results: list[tuple[str, str]] = []
    kind = None
    if chapter_id is not None:
        results, kind = _copy_chapter(chapter_id, root, work, dry_run, force, out)
        if kind is None:
            return 1
    for rel in stub_files_for(chapter_id, manifest, stubs) if kind != "synthesis" else []:
        status = copy_no_overwrite(stubs / rel, work / "mymath" / rel, dry_run)
        results.append((f"mon_travail/mymath/{rel}", status))
    results += sync_trackers(root / "suivi", work / "suivi", dry_run)

    title = {"exam": f"Examen blanc {chapter_id}", "placement": "Test de positionnement",
             "synthesis": "Projet de synthèse", "chapter": f"Chapitre {chapter_id} · {TITLES.get(chapter_id, '')}",
             None: "Initialisation de mymath et du suivi"}[kind]
    out(f"{title}{' (simulation, rien n’est écrit)' if dry_run else ''} :")
    for path, status in results:
        out(f"  {ICONS[status]} {path}")
    if any(status == "kept" for _, status in results):
        out("  🔒 = fichier déjà présent : ton travail n'a pas été touché.")
    if any(status == "later" for _, status in results):
        out(f"  ⏳ = le chapitre est encore en cours de génération (voir {IN_PROGRESS} dans son dossier) : "
            "le notebook sera copié quand il sera complet ; relance alors la même commande.")
        out("     En attendant, lis la fiche et fais les exercices papier. Pour copier quand même : --force.")
    if any(status == "appended" for _, status in results):
        out("  ➕ = nouvelles sections ajoutées à la fin de ton fichier (le reste est intact).")
    if any(status == "changed" for _, status in results):
        out("  ℹ️ = ces sections ont changé dans le modèle suivi/tableau_de_bord.md depuis ta copie (titres, ★ ou "
            "durées) : compare et recopie ce qui t'intéresse ; ta copie n'est jamais modifiée.")
    if kind is None:
        out("👉 Teste toute ta librairie : python -m pytest tests/ -q -m mymath")
        return 0
    missing = {} if kind == "synthesis" else missing_earlier_modules(chapter_id, manifest, work / "mymath")
    if missing:
        listing = " · ".join(f"{cid} : {', '.join(files)}" for cid, files in missing.items())
        out(f"ℹ️ Modules de chapitres précédents absents de ta librairie ({listing}).")
        out("   Les notebooks et les tests prendront la version de référence à leur place ;")
        out(f"   pour les écrire toi-même : python tools/start_chapter.py {next(iter(missing))} "
            "(et de même pour les autres).")
    if kind == "synthesis":
        out(f"👉 Le cahier des charges : projets/{SYNTHESIS}/README.md ; ton travail : mon_travail/{SYNTHESIS}/")
        return 0
    if kind in ("exam", "placement"):
        folder = PLACEMENT if kind == "placement" else f"checkpoints/partie_{checkpoint_number(chapter_id)}"
        out(f"👉 Lis {folder}/README.md, puis travaille dans mon_travail/{folder}/ (le notebook et ta copie)")
        return 0
    folder = find_chapter_dir(chapter_id, root / "chapitres").name
    if any(status == "later" for _, status in results):
        out(f"👉 Lis chapitres/{folder}/01_fiche.md et écris tes réponses dans mon_travail/{folder}/06_mes_reponses.md")
    else:
        out(f"👉 Commence par chapitres/{folder}/01_fiche.md (« Ordre conseillé »), puis ta copie "
            f"mon_travail/{folder}/03_notebook.ipynb")
    tests = chapter_test_files(chapter_id, root)
    if tests:
        out(f"👉 Teste ton code du chapitre : python -m pytest {' '.join(tests)} -q")
    else:
        out("👉 Teste toute ta librairie : python -m pytest tests/ -q -m mymath")
    return 0


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):  # emoji on Windows consoles and pipes
        sys.stdout.reconfigure(errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("chapter", nargs="?", help="R3, M12c, 12 (a workbookIA chapter), CP1, POS, PS...")
    parser.add_argument("--init", action="store_true",
                        help="create mon_travail/mymath (base files) and your tracking files in mon_travail/suivi")
    parser.add_argument("--dry-run", action="store_true", help="show what would be copied")
    parser.add_argument("--force", action="store_true", help="start a chapter even if it is still being generated")
    args = parser.parse_args(argv)
    if not args.chapter and not args.init:
        parser.error("indique un chapitre (ex. R3, M12c, ou 12 pour tous les chapitres de maths avant le ch. 12 "
                     "de workbookIA) ou --init")
    try:
        return start_chapter(None if args.init and not args.chapter else args.chapter, dry_run=args.dry_run,
                             force=args.force)
    except NoMathsChapter as exc:
        print(f"ℹ️ {exc}.")
        return 2
    except ValueError as exc:
        print(f"❌ {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
