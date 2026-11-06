#!/usr/bin/env python
"""The syllabus of workbookMaths: data, checks and generated documents (BIBLE §8, §13).

    python tools/syllabus.py check     # consistency of the data (errors stop, warnings are listed)
    python tools/syllabus.py build     # check, then write docs/SYLLABUS.md, docs/PARCOURS.md,
                                       # docs/syllabus/COUVERTURE_IA.md, the dashboard model and the README table
    python tools/syllabus.py stats     # totals per part

Source of truth: ``docs/syllabus/data/partie_*.py`` and ``fin.py`` (one list ``CHAPTERS`` per file, in study order),
and ``docs/syllabus/data/ia_coverage.py`` (which math chapter teaches each mathematical notion of workbookIA). The ids,
titles and order come from ``src/wbm/chapters.py``; the notions of workbookIA from the frozen copy
``docs/syllabus/workbookia_notions.json`` (workbookIA is never read here).

A chapter is either **detailed** (``"exercises"`` present: objectives, sections, every exercise) or **planned**
(notions, prerequisites, MML sections, planned mymath functions): the exercises of a part are detailed in a syllabus
session just before the part is generated (BIBLE §24, 2026-11-06).

Exercise tuple: ``(id, type, stars, minutes, title, covers, flags)`` where ``covers`` lists section ids
(``"§2 §3"``) and ``flags`` is a space-separated string of tokens:

* ``E``: in the essential track (every exercise is in the complete track);
* ``c:wbm`` | ``c:pytest`` | ``c:manuel``: how it is checked (default from the type);
* ``f:02`` | ``f:03``: where it lives (default from the type: paper types in 02_exercices, the others in the notebook);
* ``p:R1.3,R1.4``: exercises it needs (prerequisites);
* ``m:gcd,lcm``: the mymath functions it writes (🔨).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from wbm import chapters as wch  # noqa: E402

DATA = ROOT / "docs" / "syllabus" / "data"
SNAPSHOT = ROOT / "docs" / "syllabus" / "workbookia_notions.json"
STUBS = ROOT / "templates" / "mymath_stubs"
DATA_FILES = ["partie_0.py", "partie_1.py", "partie_2.py", "partie_3.py", "partie_4.py", "partie_5.py",
              "partie_6.py", "partie_7.py", "fin.py"]

TYPES = ["🧠", "🔁", "✏️", "∂", "🔗", "📖", "🔨", "📦", "🔬", "🔮", "🐛", "📈", "🎨", "🧮", "🗣️", "⚖️", "🏆",
         "💼", "🛠️"]
TYPE_NAMES = {"🧠": "quiz", "🔁": "rappel", "✏️": "calcul à la main", "∂": "démonstration", "🔗": "pont vers workbookIA",
              "📖": "lecture de MML", "🔨": "from scratch (mymath)", "📦": "avec une bibliothèque",
              "🔬": "expérience", "🔮": "prédire", "🐛": "chasse à l'erreur", "📈": "lire un graphique",
              "🎨": "visualiser", "🧮": "Fermi", "🗣️": "Feynman", "⚖️": "esprit critique", "🏆": "défi",
              "💼": "entretien", "🛠️": "compétence pro"}
PAPER_TYPES = {"🧠", "🔁", "✏️", "∂", "🔗", "📖", "🧮", "🗣️", "⚖️", "💼"}
DEFAULT_CHECK = {"✏️": "wbm", "🔗": "wbm", "🔨": "pytest", "📦": "wbm", "🔬": "wbm", "🔮": "wbm", "🐛": "wbm",
                 "📈": "wbm", "🎨": "manuel", "🧮": "manuel", "🏆": "wbm"}
CHECKS = {"wbm", "pytest", "manuel"}
FLASHCARD_MINUTES = 2
TRACKS = {"complet": "Parcours complet", "essentiel": "Parcours essentiel"}


class SyllabusError(Exception):
    pass


# ---------------------------------------------------------------------------- loading
def _import(path: Path):
    spec = importlib.util.spec_from_file_location(f"syllabus_data_{path.stem}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_exercise(raw: tuple, chapter_id: str) -> dict:
    """An exercise tuple -> dict (see the module docstring)."""
    if len(raw) != 7:
        raise SyllabusError(f"{chapter_id}: exercise {raw[:1]} must have 7 fields, has {len(raw)}")
    ex_id, kind, stars, minutes, title, covers, flags = raw
    ex = {"id": ex_id, "type": kind, "stars": stars, "minutes": minutes, "title": title,
          "covers": covers.split(), "tracks": ["complet"], "check": DEFAULT_CHECK.get(kind, "manuel"),
          "file": "02" if kind in PAPER_TYPES else "03", "prereq": [], "mymath": []}
    for token in flags.split():
        if token == "E":
            ex["tracks"].append("essentiel")
        elif token.startswith("c:"):
            ex["check"] = token[2:]
        elif token.startswith("f:"):
            ex["file"] = token[2:]
        elif token.startswith("p:"):
            ex["prereq"] = [p for p in token[2:].split(",") if p]
        elif token.startswith("m:"):
            ex["mymath"] = [m for m in token[2:].split(",") if m]
        else:
            raise SyllabusError(f"{ex_id}: unknown flag {token!r}")
    return ex


def load() -> dict[str, dict]:
    """Every chapter of the data files, in study order: {id: chapter dict} (exercises parsed)."""
    chapters: dict[str, dict] = {}
    for name in DATA_FILES:
        path = DATA / name
        if not path.exists():
            continue
        for raw in _import(path).CHAPTERS:
            ch = dict(raw)
            cid = ch["id"]
            if cid in chapters:
                raise SyllabusError(f"chapter {cid} defined twice")
            ch["title"] = wch.TITLES.get(cid, "?")
            ch["part"] = wch.PARTS.get(cid, "?")
            ch["prepares"] = wch.ia_chapter_of(cid)
            ch["detailed"] = "exercises" in ch
            ch["exercises"] = [parse_exercise(e, cid) for e in ch.get("exercises", [])]
            chapters[cid] = ch
    return chapters


def load_coverage() -> dict[str, dict[str, str]]:
    return _import(DATA / "ia_coverage.py").COVERAGE


def load_snapshot() -> dict:
    return json.loads(SNAPSHOT.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------- times
def chapter_minutes(ch: dict, track: str = "complet") -> int | None:
    """Study time of a detailed chapter in a track (reading + exercises + flashcards), None for a planned one."""
    if not ch["detailed"]:
        return None
    exercises = sum(e["minutes"] for e in ch["exercises"] if track in e["tracks"])
    return ch.get("reading_minutes", 0) + exercises + ch.get("flashcards", 0) * FLASHCARD_MINUTES


def hours_label(minutes: int | None) -> str:
    if minutes is None:
        return "?"
    hours = minutes / 60
    return f"{hours:.1f} h".replace(".", ",")


# ---------------------------------------------------------------------------- checks
ID_PATTERN = re.compile(r"^(?P<ch>POS|PS|CP\d|R\d|M\d\d[a-d]?|MB\d)\.(?P<kind>Q|R|E)?(?P<n>\d+)$")


def check(chapters: dict | None = None, coverage: dict | None = None, snapshot: dict | None = None
          ) -> tuple[list[str], list[str]]:
    """(errors, warnings) of the syllabus."""
    chapters = load() if chapters is None else chapters
    coverage = load_coverage() if coverage is None else coverage
    snapshot = load_snapshot() if snapshot is None else snapshot
    errors: list[str] = []
    warnings: list[str] = []
    order = list(wch.CHAPTER_ORDER)
    if list(chapters) != order:
        missing = [c for c in order if c not in chapters]
        extra = [c for c in chapters if c not in order]
        if missing or extra:
            errors.append(f"chapters missing {missing} or unknown {extra} (wbm.chapters is the reference)")
        else:
            errors.append("chapters are not in the study order of wbm.chapters")
    all_ids: dict[str, str] = {}
    for cid, ch in chapters.items():
        if cid not in order:
            continue
        rank = order.index(cid)
        expected_dir = special_dir(cid)
        if expected_dir is not None:
            if ch.get("dir") != expected_dir:
                errors.append(f"{cid}: dir must be {expected_dir!r} (got {ch.get('dir')!r})")
        elif not ch.get("dir", "").startswith(cid.lower() + "_"):
            errors.append(f"{cid}: dir must start with {cid.lower()}_ (got {ch.get('dir')!r})")
        for key in ("summary", "teaches", "hours", "generation_sessions"):
            if not ch.get(key):
                errors.append(f"{cid}: missing {key!r}")
        if ch.get("mymath") and not ch["detailed"]:
            if not ch["mymath"].get("module", "").endswith(".py") or not ch["mymath"].get("functions"):
                errors.append(f"{cid}: mymath needs a module (.py) and planned functions")
        for before in ch.get("after", []):
            if before not in order or order.index(before) >= rank:
                errors.append(f"{cid}: 'after' names {before}, which is not an earlier chapter")
        for notion, source in ch.get("requires", []):
            if source.startswith("IA:"):
                continue
            if source not in order or order.index(source) >= rank:
                errors.append(f"{cid}: requires « {notion} » from {source}, which is not an earlier chapter")
        if not ch["detailed"]:
            continue
        for key in ("objectives", "sections", "reading_minutes", "flashcards"):
            if key not in ch or (key in ("objectives", "sections") and not ch[key]):
                errors.append(f"{cid}: a detailed chapter needs {key!r}")
        sections = {s for s, _ in ch.get("sections", [])}
        counters = {"Q": 0, "R": 0, "E": 0, "": 0}
        for ex in ch["exercises"]:
            m = ID_PATTERN.match(ex["id"])
            if not m or m.group("ch") != cid:
                errors.append(f"{cid}: bad exercise id {ex['id']!r}")
                continue
            kind_letter = m.group("kind") or ""
            counters[kind_letter] += 1
            if int(m.group("n")) != counters[kind_letter]:
                errors.append(f"{ex['id']}: ids of the same kind must be consecutive (expected "
                              f"{cid}.{kind_letter}{counters[kind_letter]})")
            expected_letter = {"🧠": "Q", "🔁": "R", "💼": "E"}.get(ex["type"], "")
            if kind_letter != expected_letter:
                errors.append(f"{ex['id']}: a {ex['type']} uses the letter {expected_letter or '(none)'}")
            if ex["id"] in all_ids:
                errors.append(f"{ex['id']}: duplicate id")
            all_ids[ex["id"]] = cid
            if ex["type"] not in TYPES:
                errors.append(f"{ex['id']}: unknown type {ex['type']!r}")
            if ex["stars"] not in (1, 2, 3, 4):
                errors.append(f"{ex['id']}: stars must be 1 to 4")
            if not isinstance(ex["minutes"], int) or ex["minutes"] <= 0:
                errors.append(f"{ex['id']}: minutes must be a positive integer")
            if ex["check"] not in CHECKS:
                errors.append(f"{ex['id']}: unknown check {ex['check']!r}")
            if ex["file"] not in ("02", "03"):
                errors.append(f"{ex['id']}: file must be 02 or 03")
            if ex["type"] == "🔨" and not ex["mymath"]:
                errors.append(f"{ex['id']}: a 🔨 names the mymath functions it writes (m:...)")
            unknown = [s for s in ex["covers"] if s not in sections]
            if unknown or not ex["covers"]:
                errors.append(f"{ex['id']}: covers unknown sections {unknown or '(none)'}")
        for ex in ch["exercises"]:
            for p in ex["prereq"]:
                if p not in all_ids:
                    errors.append(f"{ex['id']}: prerequisite {p} is not an earlier exercise")
                elif "essentiel" in ex["tracks"]:
                    prereq = next(e for c in chapters.values() for e in c["exercises"] if e["id"] == p)
                    if "essentiel" not in prereq["tracks"]:
                        warnings.append(f"{ex['id']} (essentiel) needs {p}, which is not in the essential track: "
                                        "its solution must be read")
        covered = {s for ex in ch["exercises"] for s in ex["covers"]}
        for s in sorted(sections - covered):
            errors.append(f"{cid}: section {s} is covered by no exercise")
        warnings += composition_warnings(cid, ch)
        errors += mymath_errors(cid, ch)
    errors += coverage_errors(coverage, snapshot)
    return errors, warnings


def special_dir(cid: str) -> str | None:
    """The fixed folder of POS, CPn and PS (None for an ordinary chapter, which lives in chapitres/<id>_<name>)."""
    if cid == "POS":
        return "positionnement"
    if cid == "PS":
        return "projets/projet_synthese"
    if cid.startswith("CP"):
        return f"checkpoints/partie_{wch.checkpoint_number(cid)}"
    return None


def folder(ch: dict) -> str:
    """The chapter's folder relative to the repository root."""
    return special_dir(ch["id"]) or f"chapitres/{ch['dir']}"


def composition_warnings(cid: str, ch: dict) -> list[str]:
    """BIBLE §13 composition, for a detailed chapter (CPn, POS and PS have their own rules)."""
    if cid in ("POS", "PS") or cid.startswith("CP") or "COMPOSITION" in ch.get("notes", ""):
        return []
    counts = {t: 0 for t in TYPES}
    for ex in ch["exercises"]:
        counts[ex["type"]] += 1
    short = ch["hours"] <= 8
    factor = 0.5 if short else 1.0
    part = ch["part"]
    rules = [("🧠", 6), ("✏️∂", 10), ("🔨📦", 4), ("🔬🔮", 2), ("🐛", 1), ("🎨", 1), ("🗣️", 1), ("🛠️", 1)]
    if part != "0":
        rules += [("💼", 1), ("🏆", 1)]
    if ch.get("mml"):
        rules.append(("📖", 1))
    warnings = []
    for group, minimum in rules:
        have = sum(counts[t] for t in TYPES if t in group)
        if have < max(1, int(minimum * factor)):
            warnings.append(f"{cid}: composition {group} = {have} (expected ≥ {max(1, int(minimum * factor))}); "
                            "justify with COMPOSITION in notes")
    recall = counts["🔁"]
    earlier = wch.CHAPTER_ORDER.index(cid) - 1          # POS is first
    if recall < min(3, max(0, earlier)):
        warnings.append(f"{cid}: {recall} 🔁 (expected {min(3, earlier)})")
    if not 15 <= ch.get("flashcards", 0) <= 30 and not short:
        warnings.append(f"{cid}: {ch.get('flashcards')} flashcards (expected 15 to 30)")
    return warnings


def stub_functions(module: str) -> list[str] | None:
    """Public function names of a stub module, or None if the stub does not exist."""
    import ast

    path = STUBS / module
    if not path.exists():
        return None
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return [n.name for n in tree.body if isinstance(n, ast.FunctionDef) and not n.name.startswith("_")]


def mymath_errors(cid: str, ch: dict) -> list[str]:
    """A detailed chapter's mymath module: frozen stub, listed in MANIFEST.json, every function written by a 🔨."""
    spec = ch.get("mymath")
    if not spec:
        return []
    errors = []
    module, functions = spec["module"], spec["functions"]
    found = stub_functions(module)
    if found is None:
        return [f"{cid}: stub {module} missing in templates/mymath_stubs"]
    if found != functions:
        errors.append(f"{cid}: functions of {module} {found} differ from the syllabus {functions}")
    manifest = json.loads((STUBS / "MANIFEST.json").read_text(encoding="utf-8"))
    if module not in manifest.get("chapters", {}).get(cid, []) and module not in manifest.get("base", []):
        errors.append(f"{cid}: {module} is not listed for {cid} in MANIFEST.json")
    written = {f for ex in ch["exercises"] for f in ex["mymath"]}
    for f in functions:
        if f not in written:
            errors.append(f"{cid}: no 🔨 writes {module}:{f}")
    for f in sorted(written - set(functions)):
        errors.append(f"{cid}: a 🔨 writes {f}, which is not in {module}")
    return errors


def coverage_errors(coverage: dict, snapshot: dict) -> list[str]:
    """Every mathematical notion of workbookIA is taught by a math chapter studied BEFORE its chapter."""
    errors = []
    position = {item: i for i, item in enumerate(wch.common_order())}
    for ia, notions in coverage.items():
        if ia not in snapshot["chapters"]:
            errors.append(f"coverage: unknown workbookIA chapter {ia}")
            continue
        taught = snapshot["chapters"][ia]["teaches"]
        for notion, where in notions.items():
            if notion not in taught:
                errors.append(f"coverage {ia}: « {notion} » is not a notion of workbookIA {ia}")
            self_taught = where.startswith("0B:")
            if self_taught and ia != "0B":
                errors.append(f"coverage {ia}: « {notion} » : the prefix 0B: is for workbookIA 0B only")
            for cid in where.removeprefix("0B:").split(","):
                cid = cid.strip()
                if cid not in wch.CHAPTER_ORDER:
                    errors.append(f"coverage {ia}: « {notion} » -> unknown chapter {cid}")
                elif (not self_taught and ("IA", ia) in position
                      and position[("maths", cid)] > position[("IA", ia)]):
                    errors.append(f"coverage {ia}: « {notion} » is taught by {cid}, after workbookIA {ia}")
    return errors


# ---------------------------------------------------------------------------- documents
def _exercise_row(ex: dict) -> str:
    tracks = "C, E" if "essentiel" in ex["tracks"] else "C"
    prereq = ", ".join(ex["prereq"]) or "—"
    extra = f" · `{', '.join(ex['mymath'])}`" if ex["mymath"] else ""
    return (f"| {ex['id']} | {ex['type']} | {ex['title']}{extra} | {'★' * ex['stars']} | {ex['minutes']} | "
            f"{' '.join(ex['covers'])} | {tracks} | {ex['check']} | {prereq} |")


def build_syllabus(chapters: dict, warnings: list[str]) -> str:
    out = ["# SYLLABUS — workbookMaths", "",
           "*Généré par `python tools/syllabus.py build` à partir de `docs/syllabus/data/` : ne pas modifier à la "
           "main.*", "",
           "Le contrat du workbook : pour chaque chapitre, ses notions, ses prérequis, les sections de MML, le "
           "chapitre de workbookIA qu'il prépare et le module `mymath` ; pour une partie **détaillée**, chaque "
           "exercice. Les exercices d'une partie sont détaillés dans une session de syllabus juste avant sa "
           "génération (BIBLE §24, 2026-11-06), pour profiter des retours d'étude des parties précédentes.", "",
           "## Conventions", "",
           "- **ID** : `R1.4` (exercice), `R1.Q2` (quiz), `R1.R1` (rappel), `M12c.E1` (entretien) ; stables une fois "
           "publiés.",
           "- **★** : ★ application directe (5–15 min) · ★★ standard (15–30 min) · ★★★ approfondi (30–90 min) · "
           "★★★★ défi.",
           "- **Parcours** : C = complet (tout) ; E = essentiel (ce dont workbookIA a besoin).",
           "- **Vérification** : `wbm` (`wbm.check` dans le notebook, partie 0 pour les calculs papier), `pytest` "
           "(tests de `mymath`), `manuel` (solutions et grille de relecture).",
           "- **Types** : " + " · ".join(f"{t} {n}" for t, n in TYPE_NAMES.items()) + ".", "",
           "## Vue d'ensemble", "",
           "| Chapitre | Titre | Prépare (workbookIA) | MML | Durée | Détail | Sessions |", "|---|---|---|---|---|---|---|"]
    for cid, ch in chapters.items():
        minutes = chapter_minutes(ch)
        duration = hours_label(minutes) if minutes else f"≈ {ch['hours']} h (estimé)"
        prepares = ch["prepares"] or "—"
        out.append(f"| [{cid}](#{cid.lower()}) | {ch['title']} | {prepares} | {', '.join(ch.get('mml', [])) or '—'} | "
                   f"{duration} | {'✅ exercices' if ch['detailed'] else 'plan'} | {ch['generation_sessions']} |")
    out += ["", totals_table(chapters), ""]
    if warnings:
        out += ["## Points de vigilance (avertissements de `syllabus.py check`)", ""]
        out += [f"- {w}" for w in warnings] + [""]
    for cid, ch in chapters.items():
        out += chapter_section(cid, ch)
    return "\n".join(out) + "\n"


def totals_table(chapters: dict) -> str:
    rows = ["## Totaux par partie", "",
            "| Partie | Chapitres | Exercices détaillés | Durée (complet) | Durée (essentiel) |", "|---|---|---|---|---|"]
    by_part: dict[str, list] = {}
    for ch in chapters.values():
        by_part.setdefault(ch["part"], []).append(ch)
    for part, chs in by_part.items():
        detailed = [c for c in chs if c["detailed"]]
        n_ex = sum(len(c["exercises"]) for c in detailed)
        if len(detailed) == len(chs):
            full = hours_label(sum(chapter_minutes(c) for c in chs))
            ess = hours_label(sum(chapter_minutes(c, "essentiel") for c in chs))
        else:
            full = f"≈ {sum(c['hours'] for c in chs)} h (estimé)"
            ess = "à détailler"
        label = wch.PART_TITLES.get(part, part)
        rows.append(f"| {part} · {label} | {len(chs)} | {n_ex or '—'} | {full} | {ess} |")
    return "\n".join(rows)


def chapter_section(cid: str, ch: dict) -> list[str]:
    ia = ch["prepares"]
    ia_label = f"workbookIA {ia}" if ia else "—"
    out = [f"<a id=\"{cid.lower()}\"></a>", f"## {cid} · {ch['title']}", "",
           f"**Partie** {ch['part']} · **prépare** {ia_label} · **dossier** `{folder(ch)}/` · "
           f"**MML** {', '.join(ch.get('mml', [])) or '—'} · **sessions de génération** {ch['generation_sessions']}", "",
           ch["summary"], ""]
    if ch["detailed"]:
        out.append(f"**Temps** : {hours_label(chapter_minutes(ch))} en parcours complet, "
                   f"{hours_label(chapter_minutes(ch, 'essentiel'))} en parcours essentiel (lecture "
                   f"{ch['reading_minutes']} min, {ch['flashcards']} flashcards).")
        out.append("")
        out += ["**Objectifs**", ""] + [f"- {o}" for o in ch["objectives"]] + [""]
        out += ["**Sections de la fiche**", ""] + [f"- {s} {t}" for s, t in ch["sections"]] + [""]
    else:
        out.append(f"**Durée estimée** : ≈ {ch['hours']} h. Exercices détaillés avant la génération de la partie.")
        out.append("")
    out += ["**Notions enseignées** : " + " · ".join(ch["teaches"]), ""]
    if ch.get("requires"):
        out.append("**Prérequis** : " + " · ".join(f"{n} ({s})" for n, s in ch["requires"]))
        out.append("")
    if ch.get("after"):
        out.append("**Après** : " + ", ".join(ch["after"]))
        out.append("")
    spec = ch.get("mymath")
    if spec:
        status = "signatures figées" if ch["detailed"] else "fonctions prévues"
        out.append(f"**mymath** : `{spec['module']}` ({status}) : " + ", ".join(f"`{f}`" for f in spec["functions"]))
        out.append("")
    if ch["detailed"]:
        out += ["| ID | Type | Titre | ★ | ⏱️ min | Sections | Parcours | Vérif. | Prérequis |",
                "|---|---|---|---|---|---|---|---|---|"]
        out += [_exercise_row(ex) for ex in ch["exercises"]]
        out.append("")
        if ch.get("notes"):
            out += [f"*Notes* : {ch['notes']}", ""]
    return out


def build_parcours(chapters: dict) -> str:
    out = ["# PARCOURS — workbookMaths", "",
           "*Généré par `python tools/syllabus.py build` : ne pas modifier à la main.*", "",
           "Deux parcours (BIBLE §12) : **complet** (tout, par défaut) et **essentiel** (ce dont workbookIA a besoin). "
           "Seules les parties détaillées sont listées ; les autres le seront avant leur génération.", ""]
    for track, label in TRACKS.items():
        out += [f"<a id=\"{track}\"></a>", f"## {label}", "",
                "| Chapitre | Exercices | Durée |", "|---|---|---|"]
        total = 0
        for cid, ch in chapters.items():
            if not ch["detailed"]:
                continue
            ids = [e["id"] for e in ch["exercises"] if track in e["tracks"]]
            minutes = chapter_minutes(ch, track)
            total += minutes
            out.append(f"| {cid} | {', '.join(ids)} | {hours_label(minutes)} |")
        out += ["", f"**Total des parties détaillées** : {hours_label(total)}.", ""]
    return "\n".join(out) + "\n"


def build_coverage(coverage: dict, snapshot: dict) -> str:
    out = ["# Couverture des notions de workbookIA", "",
           "*Généré par `python tools/syllabus.py build` : ne pas modifier à la main.*", "",
           f"Pour chaque chapitre de workbookIA, ses notions mathématiques et le chapitre de maths qui les enseigne "
           f"**avant** lui dans l'ordre de travail commun (`syllabus.py check` le vérifie). Les notions de workbookIA "
           f"sont lues dans une copie figée (`docs/syllabus/workbookia_notions.json`, commit "
           f"{snapshot['_meta']['commit']}). Les notions sans chapitre de maths sont jugées non mathématiques "
           f"(outils, pratique, vocabulaire du ML) : elles sont listées pour relecture.", ""]
    n_math = n_other = 0
    for ia in snapshot["order"]:
        info = snapshot["chapters"][ia]
        mapped = coverage.get(ia, {})
        others = [n for n in info["teaches"] if n not in mapped]
        n_math += len(mapped)
        n_other += len(others)
        out += [f"## workbookIA {ia} · {info['title']}", ""]
        if mapped:
            out += ["| Notion de workbookIA | Enseignée dans |", "|---|---|"]
            out += [f"| {n} | {_where_label(w)} |" for n, w in mapped.items()]
            out.append("")
        if others:
            out += ["Non mathématiques : " + " · ".join(others), ""]
    out.insert(6, f"**Bilan** : {n_math} notions mathématiques couvertes, {n_other} notions non mathématiques.\n")
    return "\n".join(out) + "\n"


def _where_label(where: str) -> str:
    if where.startswith("0B:"):
        return "workbookIA 0B lui-même (à partir de la remise à niveau), approfondi en " + where[3:].replace(",", ", ")
    return where.replace(",", ", ")


def readme_order_table() -> str:
    rows = ["| Dans workbookIA | Fais d'abord, dans workbookMaths |", "|---|---|"]

    def fmt(ids):
        return "<br>".join(f"**{c}** · {wch.TITLES[c]}" for c in ids)

    rows.append(f"| *(avant de commencer)* | {fmt(['POS'])} |")
    rows.append(f"| 0A · {wch.IA_TITLES['0A']} *(en parallèle de la remise à niveau)* | "
                f"{fmt([f'R{i}' for i in range(10)])} |")
    rows.append(f"| 0B · {wch.IA_TITLES['0B']} | {fmt(['CP0'])} |")
    checkpoints = {"6": 1, "11": 2, "15": 3, "20": 4, "24": 5, "29": 6}
    for ia in wch.IA_CHAPTERS[2:]:
        math = wch.chapters_before_ia(ia)
        rows.append(f"| {ia} · {wch.IA_TITLES[ia]} | {fmt(math) if math else '— (rien de nouveau)'} |")
        if ia in checkpoints:
            n = checkpoints[ia]
            rows.append(f"| CP{n} · checkpoint de la partie {wch.PARTS[f'CP{n}']} | {fmt([f'CP{n}'])} |")
    rows.append(f"| PF · projet final | {fmt(['PS'])} |")
    return "\n".join(rows)


def dashboard_order_section() -> str:
    lines = []
    for book, cid in wch.common_order():
        if book == "maths":
            lines.append(f"- [ ] 📐 **{cid}** · {wch.TITLES[cid]}")
        elif cid.startswith("CP"):
            lines.append(f"- [ ] 🤖 workbookIA **{cid}** · checkpoint (examen blanc, synthèse, mini-projet)")
        elif cid == "PF":
            lines.append("- [ ] 🤖 workbookIA **PF** · projet final")
        else:
            extra = " *(en parallèle de R0 à R9)*" if cid == "0A" else ""
            lines.append(f"- [ ] 🤖 workbookIA **{cid}** · {wch.IA_TITLES[cid]}{extra}")
    return "\n".join(lines)


def published(ch: dict, root: Path = ROOT) -> bool:
    """A detailed chapter whose folder exists and is not in progress (its dashboard section is published)."""
    if not ch["detailed"]:
        return False
    path = root / folder(ch)
    return (path.is_dir() and any(f.name != ".gitkeep" for f in path.iterdir())
            and not (path / "EN_COURS.md").exists())


def dashboard_chapter_section(cid: str, ch: dict) -> str:
    total = hours_label(chapter_minutes(ch))
    lines = [f"<!-- wbm:section {cid} -->", f"## {cid} · {ch['title']} ⏱️ {total}", ""]
    for ex in ch["exercises"]:
        essential = "" if "essentiel" in ex["tracks"] else " (complet)"
        lines.append(f"- [ ] {ex['id']} {ex['type']} {ex['title']} {'★' * ex['stars']} {ex['minutes']} min{essential}")
    if ch.get("flashcards"):
        lines.append(f"- [ ] Flashcards du chapitre importées dans Anki ({ch['flashcards']} cartes)")
    lines.append(f"<!-- wbm:end {cid} -->")
    return "\n".join(lines)


def replace_block(text: str, start: str, end: str, body: str) -> str:
    i, j = text.index(start), text.index(end)
    return text[: i + len(start)] + "\n" + body + "\n" + text[j:]


def render(chapters: dict, warnings: list[str], coverage: dict, snapshot: dict, root: Path = ROOT
           ) -> dict[Path, str]:
    """Every generated file and its expected content: {path: text} (``build`` writes them, the tests compare)."""
    files = {root / "docs" / "SYLLABUS.md": build_syllabus(chapters, warnings),
             root / "docs" / "PARCOURS.md": build_parcours(chapters),
             root / "docs" / "syllabus" / "COUVERTURE_IA.md": build_coverage(coverage, snapshot)}
    readme = root / "README.md"
    files[readme] = replace_block(readme.read_text(encoding="utf-8"), "<!-- wbm:readme ordre -->",
                                  "<!-- wbm:end ordre -->", readme_order_table())
    board = root / "suivi" / "tableau_de_bord.md"
    text = board.read_text(encoding="utf-8")
    head = text[: text.index("<!-- wbm:section ordre -->")]
    sections = [head.rstrip("\n"), "", "<!-- wbm:section ordre -->", "## Ordre de travail commun (les deux workbooks)",
                "", "Une case par chapitre, dans l'ordre où les faire. Le détail de chaque chapitre de maths (ses "
                "exercices) s'ajoute plus bas quand il est publié.", "", dashboard_order_section(),
                "<!-- wbm:end ordre -->"]
    for cid, ch in chapters.items():
        if published(ch, root):
            sections += ["", dashboard_chapter_section(cid, ch)]
    files[board] = "\n".join(sections) + "\n"
    return files


def build(chapters: dict | None = None, out=print) -> int:
    chapters = load() if chapters is None else chapters
    coverage, snapshot = load_coverage(), load_snapshot()
    errors, warnings = check(chapters, coverage, snapshot)
    if errors:
        for e in errors:
            out(f"❌ {e}")
        out(f"{len(errors)} erreur(s) : rien n'est écrit.")
        return 1
    for path, text in render(chapters, warnings, coverage, snapshot).items():
        path.write_text(text, encoding="utf-8")
    for w in warnings:
        out(f"⚠️ {w}")
    out(f"✅ SYLLABUS.md, PARCOURS.md, COUVERTURE_IA.md, README et tableau de bord écrits "
        f"({len(warnings)} avertissement(s)).")
    return 0


def stats(chapters: dict | None = None, out=print) -> None:
    chapters = load() if chapters is None else chapters
    out(totals_table(chapters))
    n = sum(len(c["exercises"]) for c in chapters.values())
    by_type: dict[str, int] = {}
    for c in chapters.values():
        for e in c["exercises"]:
            by_type[e["type"]] = by_type.get(e["type"], 0) + 1
    out(f"\n{n} exercices détaillés : " + " · ".join(f"{t} {k}" for t, k in by_type.items()))


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["check", "build", "stats"])
    args = parser.parse_args(argv)
    if args.command == "check":
        errors, warnings = check()
        for e in errors:
            print(f"❌ {e}")
        for w in warnings:
            print(f"⚠️ {w}")
        print(f"{len(errors)} erreur(s), {len(warnings)} avertissement(s).")
        return 1 if errors else 0
    if args.command == "build":
        return build()
    stats()
    return 0


if __name__ == "__main__":
    sys.exit(main())
