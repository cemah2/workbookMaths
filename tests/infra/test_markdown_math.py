"""The formulas of the Markdown files display on GitHub as in Colab and Jupyter (tools/mdmath.py, BIBLE §6 and §24).

GitHub applies the Markdown escapes and emphasis to a ``$…$`` formula before MathJax sees it: ``\\{i\\}`` showed « i »,
``2\\,000`` showed « 2,000 », a matrix written with ``\\\\`` was not read as a formula, and an ``_`` of a formula could
pair with another one into italics (session 79, on the rendered page of a fiche).
"""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import mdmath  # noqa: E402


def test_every_tracked_markdown_formula_is_safe_on_github():
    found = []
    for path in mdmath.tracked_markdown(ROOT):
        for line in mdmath.problems(path.read_text(encoding="utf-8")):
            found.append(f"{path.relative_to(ROOT)}: {line}")
    assert not found, (f"expected no formula that GitHub would change, found {len(found)} "
                       "(python tools/mdmath.py --fix <file>): " + " | ".join(found[:8]))


@pytest.mark.parametrize("tex, safe", [
    (r"\{i\}", r"\lbrace i\rbrace"),
    (r"2\,000", r"2\thinspace000"),
    (r"a\;b", r"a\mkern5mu b"),
    (r"\|x\|", r"\Vert x\Vert"),
    (r"\begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix}", r"\begin{pmatrix}1 & 2 \cr 3 & 4\end{pmatrix}"),
    (r"f^* = a * b", r"f^\ast = a \ast b"),
    (r"\sum_{k<t}", r"\sum_{k\lt t}"),
    (r"\#\{i : x_i > 0\}", r"\operatorname{card}\lbrace i : x_i > 0\rbrace"),
    (r"\$5 \text{ et } \ 3", r"\$5 \text{ et } \ 3"),
])
def test_fix_tex_uses_letter_commands(tex, safe):
    assert mdmath.fix_tex(tex) == safe, f"expected {safe!r}, got {mdmath.fix_tex(tex)!r}"
    assert not mdmath.escape_problems(mdmath.fix_tex(tex))


def test_an_underscore_pair_across_two_formulas_is_seen_and_fixed():
    text = (r"Pour des points $\mathbf{x}_1, \ldots, \mathbf{x}_m$, la courbe du point $i$ est "
            r"$v \mapsto f(v, \mathbf{x}_{i,-j})$." "\n")
    assert mdmath.emphasis_problems(text), "expected the _ after } and the _ before { to pair into italics"
    fixed = mdmath.fix_text(text)
    assert not mdmath.problems(fixed), mdmath.problems(fixed)
    assert fixed.replace(" _", "_") == text, "expected only spaces before underscores of the formulas"


def test_prose_code_and_kept_escapes_are_never_touched():
    text = "Du code `x_1 * y_2 \\{` et du texte *en italique* avec 5 \\$ ; une formule $a_i b_j$.\n"
    assert mdmath.fix_text(text) == text
    assert mdmath.problems(text) == []


def test_a_percent_sign_that_ends_a_formula_goes_after_it():
    assert mdmath.fix_text(r"soit $95\,\%$ des cas") == "soit $95$ % des cas"


def test_table_cells_are_separate_units():
    text = "| a | $x_{1}$ | $y_{2}$ |\n|---|---|---|\n"
    assert mdmath.emphasis_problems(text) == []
