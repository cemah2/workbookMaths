"""The placement test (positionnement/): its writing examples never give an answer away (session 4)."""

import ast
import json
import re
from pathlib import Path

import pytest

import wbm

ROOT = Path(__file__).resolve().parents[2]
FOLDER = ROOT / "positionnement"
ANSWERS = json.loads((ROOT / "src" / "wbm" / "answers.json").read_text(encoding="utf-8"))
POS_IDS = sorted(k for k in ANSWERS.get("answers", ANSWERS) if str(k).startswith("POS."))


def examples() -> list[tuple[str, object]]:
    """The values shown as writing examples in the README, the sujet and the learner notebook."""
    found = []
    sources = {"README.md": (FOLDER / "README.md").read_text(encoding="utf-8"),
               "01_sujet.md": (FOLDER / "01_sujet.md").read_text(encoding="utf-8")}
    notebook = json.loads((FOLDER / "02_notebook.ipynb").read_text(encoding="utf-8"))
    sources["02_notebook.ipynb"] = "\n".join("".join(c["source"]) for c in notebook["cells"] if c["cell_type"] == "markdown")
    for name, text in sources.items():
        for token in re.findall(r"`([^`\n]+)`", text):
            try:
                value = ast.literal_eval(token)
            except (ValueError, SyntaxError):
                continue
            if isinstance(value, bool) or value is Ellipsis:
                continue
            found.append((f"{name}: {token}", value))
    return found


def test_the_pos_answers_are_recorded():
    assert len(POS_IDS) >= 55


@pytest.mark.parametrize("where, value", examples())
def test_no_writing_example_is_an_answer_of_the_test(where, value):
    right = [ex for ex in POS_IDS if wbm.check(ex, value, quiet=True).passed]
    assert not right, f"{where} is the answer of {right}: choose an example that answers no question"
