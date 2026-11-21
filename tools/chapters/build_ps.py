"""Build the two notebooks of the synthesis project (PS) from their sources.

    python tools/chapters/build_ps.py                 # both notebooks
    python tools/chapters/build_ps.py --only depart   # the starter notebook of the kit
    python tools/chapters/build_ps.py --only exemple  # the worked example
    python tools/run_all_notebooks.py projets/projet_synthese/exemple/exemple.ipynb --inplace
    python tools/run_all_notebooks.py projets/projet_synthese/depart/synthese.ipynb   # "Run all" with nothing written

The cells come from two modules, one per notebook:

* ``tools/chapters/ps_depart.py``: ``cells()`` -> the starter notebook ``depart/synthese.ipynb``, copied for the learner
  by ``start_chapter.py PS`` (setup cell ``setup_cell("exercise", chapter="PS")``; "Run all" with nothing written ends
  with ⏳, never with an error);
* ``tools/chapters/ps_exemple.py``: ``cells()`` -> the worked example ``exemple/exemple.ipynb`` (setup cell
  ``setup_cell("solution")``, executed with its outputs kept; never copied for the learner).
"""

from __future__ import annotations

import argparse
import importlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from nbbuild import write_notebook  # noqa: E402

PROJECT = "projets/projet_synthese"
TARGETS = {"depart": ("ps_depart", f"{PROJECT}/depart/synthese.ipynb"),
           "exemple": ("ps_exemple", f"{PROJECT}/exemple/exemple.ipynb")}


def build(which: str) -> Path:
    module_name, path = TARGETS[which]
    module = importlib.import_module(module_name)
    return write_notebook(path, module.cells())


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--only", choices=sorted(TARGETS), help="build one notebook only")
    args = parser.parse_args(argv)
    for which in [args.only] if args.only else sorted(TARGETS):
        print(f"✅ {build(which).relative_to(HERE.parents[1])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
