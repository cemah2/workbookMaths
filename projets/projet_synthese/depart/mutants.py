"""Deliberate mistakes for PS.7: do your tests catch them?

    python -m pytest -q test_algo.py --mutant=<name>    # algo.<name> replaced by mutants.<name>

TODO PS.7: copy here one function of algo.py, under the same name, and introduce ONE plausible mistake, one that
could really happen while coding (a forgotten factor, a transposition, an index shifted by one, a sum instead of a
mean, a sign). With ``--mutant=<name>``, conftest.py replaces ``algo.<name>`` by this copy for the whole run,
including the calls made by the other functions of algo.py: at least one test must fail, and its name tells which
test protects you from this mistake. Show this run in §7 of the article (the cell « mutation »).

A mutant may use the other functions of your module, unchanged: ``algo.<other>(...)``.
"""

from __future__ import annotations

import numpy as np  # noqa: F401

import algo  # noqa: F401  (your module: its other functions, unchanged)

# def example_function(x):
#     """Mutant of algo.example_function: <the mistake, in one line>."""
#     ...   # the copy of algo.example_function, with one mistake
