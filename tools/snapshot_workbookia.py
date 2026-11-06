#!/usr/bin/env python
"""Freeze what workbookMaths needs to know about workbookIA (BIBLE §8, §23): read-only.

    python tools/snapshot_workbookia.py /path/to/workbookia          # writes docs/syllabus/workbookia_notions.json
    python tools/snapshot_workbookia.py /path/to/workbookia --check  # only says whether the copy is up to date

The clone of workbookIA is only **read** (its ``tools/syllabus.py`` ORDER, parsed as text, and its
``docs/syllabus/data/ch*.json``); nothing is ever written there. For each workbookIA chapter the copy keeps: title,
part, notions taught (``teaches``), exercises (id -> [type, title], for the sharing rule) and the names of the
``mylearn`` functions it asks to write; for 0A, its sections (the Python taught in parallel with part 0).
``tools/syllabus.py`` uses only this copy.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "syllabus" / "workbookia_notions.json"


def _order(ia: Path) -> list[str]:
    text = (ia / "tools" / "syllabus.py").read_text(encoding="utf-8")
    match = re.search(r"^ORDER\s*=\s*(\[.*?\])", text, flags=re.S | re.M)
    if not match:
        raise SystemExit("ORDER not found in workbookIA tools/syllabus.py")
    return [c for c in ast.literal_eval(match.group(1)) if not c.startswith("CP") and c != "PF"]


def _mylearn_names(chapter: dict) -> list[str]:
    names = []
    for module in chapter.get("mylearn") or []:
        for item in module.get("api", []):
            m = re.match(r"\s*(?:def|class)\s+(\w+)", item.get("signature", ""))
            if m:
                names.append(m.group(1))
    return names


def snapshot(ia: Path) -> dict:
    data = ia / "docs" / "syllabus" / "data"
    chapters = {}
    order = _order(ia)
    for cid in order:
        ch = json.loads((data / f"ch{cid.zfill(2) if cid.isdigit() else cid}.json").read_text(encoding="utf-8"))
        entry = {"title": ch["title"], "part": ch["part"], "teaches": ch["teaches"],
                 "exercises": {e["id"]: [e["type"], e["title"]] for e in ch["exercises"]},
                 "mylearn": _mylearn_names(ch)}
        if cid == "0A":
            entry["sections"] = [[s["ref"], s["title"]] for s in ch["sections"]]
        chapters[cid] = entry
    try:
        commit = subprocess.run(["git", "-C", str(ia), "rev-parse", "--short", "HEAD"], capture_output=True,
                                text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        commit = "?"
    meta = {"source": "cemah2/workbookIA, tools/syllabus.py (ORDER) et docs/syllabus/data/ch*.json, lus en lecture seule",
            "commit": commit, "date": date.today().isoformat(),
            "note": "Copie figée : workbookMaths ne lit jamais workbookIA à l'exécution. À rafraîchir avec "
                    "tools/snapshot_workbookia.py si workbookIA change (session de syllabus)."}
    return {"_meta": meta, "order": order, "chapters": chapters}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("workbookia", type=Path, help="a clone of cemah2/workbookIA (read only)")
    parser.add_argument("--check", action="store_true", help="compare with the frozen copy, write nothing")
    args = parser.parse_args(argv)
    new = snapshot(args.workbookia.resolve())
    if args.check:
        old = json.loads(OUT.read_text(encoding="utf-8"))
        same = {k: v for k, v in old.items() if k != "_meta"} == {k: v for k, v in new.items() if k != "_meta"}
        print("✅ copie à jour" if same else f"⚠️ workbookIA a changé depuis le commit {old['_meta']['commit']} : "
              "relancer sans --check, puis python tools/syllabus.py check")
        return 0 if same else 1
    OUT.write_text(json.dumps(new, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"✅ {OUT.relative_to(ROOT)} écrit (workbookIA {new['_meta']['commit']}, {len(new['chapters'])} chapitres).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
