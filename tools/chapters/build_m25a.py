#!/usr/bin/env python
"""Build the two notebooks of chapter M25a from a single source (used by Claude).

    python tools/chapters/build_m25a.py
    python tools/run_all_notebooks.py chapitres/m25a_gaussienne/05_solutions.ipynb --inplace
    python tools/build_answers.py
    python tools/run_all_notebooks.py chapitres/m25a_gaussienne/03_notebook.ipynb

(draft: the exercises are written once 02_exercices.md is available)
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chapter_kit import (STARS, Ex, Paper, Part, badge, check_unique_keys, guarded,  # noqa: E402,F401
                         md, paper_cells, part_cells, setup_cell, write_notebook)

CHAPTER = "M25a"
FOLDER = "chapitres/m25a_gaussienne"

BOOL = "True or False"

TOOLS = '''# Tools of the notebook (parts A to D)
import math
import numbers
import re
import warnings

import matplotlib.pyplot as plt
import numpy as np

from wbm.errors import MymathMissingError
from wbm.nbtools import StopCheck, checked, drawn, filled, fr, run_pytest_group, same, verdict

TEST_M25A = "tests/test_m25a_gaussian.py"            # the tests of mymath/gaussian.py


def shown(value, digits=4):
    """A short text for a result of the learner's code (the check messages): numbers rounded, as lists."""
    if value is None:
        return "None"
    try:
        if isinstance(value, tuple):
            return "(" + ", ".join(str(np.round(np.asarray(v, dtype=float), digits).tolist()) for v in value) + ")"
        return str(np.round(np.asarray(value, dtype=float), digits).tolist())
    except (TypeError, ValueError):
        return repr(value)[:120]


def reporter(results, stop=True):
    """A function report(ok, success, failure) that prints one ✅ or ❌ line, keeps the verdict in results, and (stop)
    ends the check at the first ❌ (StopCheck, caught by checked)."""
    def report(ok, success, failure):
        results.append(bool(ok))
        print(("✅ " + success) if ok else ("❌ " + failure))
        if not ok and stop:
            raise StopCheck
    return report'''

LOAD_LEARNER = ('mymath = wbm.load_mymath("learner", missing_ok=True, fallback="ref", chapter="M25a")  '
                '# reload your saved file')
LOAD_REF = 'mymath = wbm.load_mymath("ref")'


def tests_cells(keyword: str) -> list:
    """The cells that run the tests of gaussian.py selected by ``keyword`` (learner's code, or the reference)."""
    return [("md", "**Les tests** (lis d'abord la ligne qui suit chaque ❌ : elle dit ce qui était attendu)."),
            ("todo", f'run_pytest_group(TEST_M25A, "{keyword}")'),
            ("solution", f'run_pytest_group(TEST_M25A, "{keyword}", impl="ref")')]


def main() -> int:
    return 0


if __name__ == "__main__":
    sys.exit(main())
