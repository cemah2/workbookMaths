"""A writing example shown to the learner (`"11/20"`, `[3.5, -2]`) must never be the answer of a question of its chapter.

The literals between backticks of 02_exercices.md and of the introduction of Part 0 of the exercise notebook (where the
answer forms are shown) are evaluated (``ast.literal_eval``) and checked against every recorded answer of the chapter
(session 5, independent check of R1). The statements of the notebook exercises are not scanned: a number they quote
(``72.0``, the harmonic mean of the course) may coincide with the answer of another exercise without showing a form.

The comments and the strings (docstrings, messages) of the code cells of the exercise and exam notebooks are scanned too
(audit of part VI, session 70: « a float such as 1/6 », « L = [[4, 0], [3, 2]] » and « -ln(0,79) » gave answers of
M26, M27 and CP6 from a context or tools cell, out of reach of the backticks). There, only the forms of an example are
taken: a fraction p/q, a list of numbers (outermost brackets), a logarithm, an exponential or a square root of a number.
A plain number of a comment is mostly data (a level 0.05, a quantile 1.645), and is not taken.
"""

import ast
import io
import json
import math
import re
import tokenize
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


# The comments and strings of the code cells (session 70). A value quoted from a statement (a datum, not a writing
# example) that happens to answer another question is listed here, with the reason, after review.
QUOTED_DATA = {
    ("m03_probabilites_conditionnelles", "1/6"): "a clue of the statement of M03.28 (« P(appli | abandon) = 1/6 »)",
    ("m11_logique_concentration", "1/2"): "the parameter of the Bernoulli(1/2) of M11 in a docstring",
    ("m16_couches_affines", "1/4"): "the question of M16.20 c) in its TODO comment (« P(Z ≤ 1/4) »)",
    ("m28_gram_echantillonnage", "[0, 1]"): "the box [0, 1]² of M28.15 (an interval, not a list)",
    ("r3_fonctions", "[−3, 3]"): "a plotting interval of the docstring of R3 (« on [−3, 3] »)",
}
# Writing examples of the chapters before part VI that answer a question: reported by the audit of part VI (session 70)
# and left to the coordinator. Remove the line once the example is replaced.
PENDING = {}

_FRACTION = re.compile(r"(?<![\w.,/√)])[-−]?\d+/\d+(?![\w./])")
_CALC = re.compile(r"(?<![\w.])([-−]?)(ln|log|exp|sqrt|√)\s*(?:\(\s*(\d+(?:[.,]\d+)?(?:/\d+)?)\s*\)"
                   r"|(\d+(?:[.,]\d+)?)(?![\w.,(]))(?:/(\d+)(?![\w.,/]))?")      # « √2/2 » is √2 divided by 2
_FUNCTIONS = {"ln": math.log, "log": math.log, "exp": math.exp, "sqrt": math.sqrt, "√": math.sqrt}


def _comments_and_strings(source):
    """The comments and the string literals of a code cell (docstrings, messages, the literal parts of f-strings)."""
    kinds = {tokenize.COMMENT, tokenize.STRING, getattr(tokenize, "FSTRING_MIDDLE", tokenize.STRING)}
    try:
        return [tok.string for tok in tokenize.generate_tokens(io.StringIO(source).readline) if tok.type in kinds]
    except (tokenize.TokenError, SyntaxError):
        return re.findall(r"#[^\n]*", source)


def _bracket_groups(text):
    """The outermost [...] groups of a text (the opening « ] » of a French interval ]a ; b[ is skipped)."""
    depth, start = 0, 0
    for i, ch in enumerate(text):
        if ch == "[":
            start = i if depth == 0 else start
            depth += 1
        elif ch == "]" and depth:
            depth -= 1
            if depth == 0:
                yield text[start:i + 1]


def _numbers(value):
    """The numbers of a (nested) list of numbers, None for anything else."""
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return [value]
    if isinstance(value, list):
        out = []
        for item in value:
            numbers = _numbers(item)
            if numbers is None:
                return None
            out += numbers
        return out
    return None


def example_values(text):
    """{token: values to check} for the example forms of a comment or a string: a fraction p/q (as typed, and its
    value), a list of at least two numbers, ln, log, exp, sqrt or √ of a number, perhaps divided by an integer
    (decimal comma read as a point)."""
    found = {}
    for m in _FRACTION.finditer(text):
        token = m.group(0).replace("−", "-")
        p, q = (int(x) for x in token.lstrip("-").split("/"))
        if p and q > 1:                                            # « 0/1 predictions », « 5/1 » are not fractions
            found[m.group(0)] = [token, int(token.split("/")[0]) / q]
    for m in _CALC.finditer(text):
        sign, function, inside, bare, divisor = m.groups()
        arg = (inside or bare).replace(",", ".")
        x = float(arg.split("/")[0]) / float(arg.split("/")[1]) if "/" in arg else float(arg)
        try:
            value = _FUNCTIONS[function](x) / int(divisor or 1)
        except (ValueError, OverflowError, ZeroDivisionError):
            continue
        found[m.group(0)] = [-value if sign else value]
    for group in _bracket_groups(text):
        try:
            value = ast.literal_eval(group.replace("−", "-"))
        except (ValueError, SyntaxError, TypeError, MemoryError, RecursionError):
            continue
        numbers = _numbers(value)
        if numbers is not None and len(numbers) >= 2:
            found[group] = [value]
    return found


def _code_notebooks():
    """(folder, chapter, answer IDs of the chapter, {token: values}) for each exercise and exam notebook."""
    notebooks = [(folder.name, folder.name.split("_")[0].upper(), folder / "03_notebook.ipynb")
                 for folder in sorted((ROOT / "chapitres").glob("*_*"))]
    notebooks += [(folder.name, "CP" + folder.name.split("_")[1], folder / "02_examen_notebook.ipynb")
                  for folder in sorted((ROOT / "checkpoints").glob("partie_*"))]
    out = []
    for folder, chapter, path in notebooks:
        ids = sorted(k for k in ANSWERS if k.startswith(chapter + "."))
        if not ids or not path.exists():
            continue
        found = {}
        for cell in json.loads(path.read_text(encoding="utf-8"))["cells"]:
            if cell["cell_type"] == "code":
                for text in _comments_and_strings("".join(cell["source"])):
                    found.update(example_values(text))
        out.append((folder, path, ids, found))
    return out


def code_cases():
    cases = []
    for folder, path, ids, found in _code_notebooks():
        for token, values in sorted(found.items()):
            if (folder, token) in QUOTED_DATA or (folder, token) in PENDING:
                continue
            cases.append(pytest.param(ids, values, id=f"{folder}/{path.name}#code:{token}"))
    return cases


@pytest.mark.parametrize("ids, values", code_cases())
def test_a_value_of_a_comment_or_string_of_a_code_cell_is_not_an_answer(ids, values):
    right = sorted({ex for ex in ids for value in values if wbm.check(ex, value, quiet=True).passed})
    assert not right, (f"expected the example {values[0]!r} of a comment or string of a code cell to answer no "
                       f"question of its chapter, but it answers {right} (a datum of a statement goes in QUOTED_DATA)")


def test_the_code_scan_sees_the_leaks_of_session_70():
    assert example_values("# a float such as 1/6 is only close to it") == {"1/6": ["1/6", 1 / 6]}
    assert example_values('"""… (« L = [[4, 0], [3, 2]] »), as a line"""') == {"[[4, 0], [3, 2]]": [[[4, 0], [3, 2]]]}
    found = example_values("# -ln(0,79) : a decimal comma is read as a point")
    assert list(found) == ["-ln(0,79)"] and math.isclose(found["-ln(0,79)"][0], -math.log(0.79))
    assert example_values("# c) on the 0/1 predictions, ln(1 + x) ≈ x, ]0, 1[ and [a, b]") == {}
    assert example_values("# √2/2") == {"√2/2": [math.sqrt(2) / 2]}
    assert _comments_and_strings('x = f"a {y} such as 5/13"  # see [3, 5]\n') == ['a ', ' such as 5/13', '# see [3, 5]']


def test_each_listed_value_is_still_found_and_still_answers():
    """A line of QUOTED_DATA or PENDING whose value is gone (the example replaced) is removed."""
    listed = set(QUOTED_DATA) | set(PENDING)
    stale = set(listed)
    for folder, path, ids, found in _code_notebooks():
        for token, values in found.items():
            if (folder, token) in listed and any(wbm.check(ex, v, quiet=True).passed for ex in ids for v in values):
                stale.discard((folder, token))
    assert not stale, f"expected each listed value to be found and to answer a question, but not: {sorted(stale)}"


def message_examples():
    """The values quoted as writing examples in the messages of `wbm` (`comme "8/11"`, `` `[-1.25, 1]` ``): they are
    shown in every chapter, so they must answer no question at all, nor its opposite (session 14, R9 learner C1:
    "sqrt(3)/2" was the answer of R9.7d up to the sign)."""
    examples = set()
    for name in ("checker.py", "mathcheck.py"):
        source = (ROOT / "src" / "wbm" / name).read_text(encoding="utf-8")
        examples |= set(re.findall(r'(?:comme|ou|\() \\"([^"\\]+)\\"', source))
        examples |= {token for token in re.findall(r"sans guillemets : `([^`]+)`", source)}
    return sorted(examples)


@pytest.mark.parametrize("example", message_examples())
def test_a_message_example_is_no_answer(example):
    if example == "vide":                                  # the empty set, a notation rather than an example
        return
    if example.startswith(("[2 ;", "]-oo", "[0 ; 1] U")):
        values = [example]                                 # an interval written as text
    else:
        try:
            values = [ast.literal_eval(example)]
        except (ValueError, SyntaxError):
            values = [example]
    for value in list(values):
        if isinstance(value, str) and not value.startswith(("[", "]")):
            values.append("-(" + value + ")")
        elif isinstance(value, list):
            values.append([-x for x in value])
    right = [(ex, v) for ex in sorted(ANSWERS) for v in values if wbm.check(ex, v, quiet=True).passed]
    assert not right, f"expected the message example {example!r} to answer no question, but {right}"
