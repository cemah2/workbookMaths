"""A writing example shown to the learner (`"11/20"`, `[3.5, -2]`) must never be the answer of a question of its chapter.

The literals between backticks of 02_exercices.md and of the introduction of Part 0 of the exercise notebook (where the
answer forms are shown) are evaluated (``ast.literal_eval``) and checked against every recorded answer of the chapter
(session 5, independent check of R1). The statements of the notebook exercises are not scanned: a number they quote
(``72.0``, the harmonic mean of the course) may coincide with the answer of another exercise without showing a form.
"""

import ast
import json
import re
from pathlib import Path

import pytest

import wbm

ROOT = Path(__file__).resolve().parents[2]
ANSWERS = json.loads((ROOT / "src" / "wbm" / "answers.json").read_text(encoding="utf-8"))["answers"]


def chapter_cases():
    cases = []
    for folder in sorted((ROOT / "chapitres").glob("*_*")):
        chapter = folder.name.split("_")[0].upper()
        ids = sorted(k for k in ANSWERS if k.startswith(chapter + "."))
        if not ids:
            continue
        texts = []
        if (folder / "02_exercices.md").exists():
            texts.append(("02_exercices.md", (folder / "02_exercices.md").read_text(encoding="utf-8")))
        if (folder / "03_notebook.ipynb").exists():
            nb = json.loads((folder / "03_notebook.ipynb").read_text(encoding="utf-8"))
            texts.append(("03_notebook.ipynb", "\n".join("".join(c["source"]) for c in nb["cells"]
                                                         if c["cell_type"] == "markdown"
                                                         and "".join(c["source"]).startswith("## Partie 0"))))
        for name, text in texts:
            for token in sorted(set(re.findall(r"`([^`\n]+)`", text))):
                try:
                    value = ast.literal_eval(token)
                except (ValueError, SyntaxError, MemoryError, RecursionError):
                    continue
                if isinstance(value, (bool, dict)) or value is Ellipsis or value is None:
                    continue
                if isinstance(value, str) and value.strip() in {"+oo", "-oo", "oo"}:   # the notation of an infinite
                    continue                                                       # limit (R7), not an example value
                cases.append(pytest.param(ids, value, id=f"{folder.name}/{name}:{token}"))
    return cases


@pytest.mark.parametrize("ids, value", chapter_cases())
def test_a_writing_example_is_not_an_answer(ids, value):
    right = [ex for ex in ids if wbm.check(ex, value, quiet=True).passed]
    assert not right, f"expected the example {value!r} to answer no question of its chapter, but it answers {right}"
