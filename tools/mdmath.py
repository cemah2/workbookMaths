#!/usr/bin/env python
"""Math in Markdown that GitHub displays as Colab and Jupyter do (BIBLE §6, §24, session 79).

    python tools/mdmath.py --check            # every tracked .md file (exit 1 if a formula would be broken)
    python tools/mdmath.py --check FILE...    # some files
    python tools/mdmath.py --fix FILE...      # rewrite them (the formulas only; the prose is never touched)

Why. GitHub reads a ``$…$`` or ``$$…$$`` formula of a Markdown file as ordinary Markdown text first: it applies the
backslash escapes of Markdown (``\\{`` becomes ``{``, ``\\,`` becomes ``,``, ``\\\\`` becomes ``\\``) and the
emphasis delimiters (an ``_`` or a ``*`` of a formula can pair with another one and turn into italics), and only then
gives the formula to MathJax. Colab, Jupyter and VS Code take the formula out before reading the Markdown, so they show
it as written. Hence, on GitHub: ``\\{i\\}`` showed « i », ``2\\,000`` showed « 2,000 », a matrix written with ``\\\\``
was not even read as a formula, and a few formulas were cut by italics (checked on the rendered page of a fiche,
session 79).

The rule, which holds in both worlds: inside a formula,

* no backslash before an ASCII punctuation mark, but the letter command that means the same thing: ``\\lbrace`` and
  ``\\rbrace`` for ``\\{`` and ``\\}``, ``\\thinspace``, ``\\mkern4mu``, ``\\mkern5mu`` and ``\\negthinspace`` for
  ``\\,``, ``\\:``, ``\\;`` and ``\\!`` (MathJax 3 has no ``\\medspace`` nor ``\\thickspace``), ``\\Vert`` for ``\\|``, ``\\cr`` for the ``\\\\`` that ends a row;
  ``\\$`` (that GitHub documents) and ``\\`` followed by a space stay;
* no ``*`` (``\\ast``, the same glyph ∗), no ``<`` before a letter (``\\lt``);
* no ``_`` that the emphasis rules of CommonMark would pair with another delimiter of the same paragraph: such an
  ``_`` gets a space before it (``\\sum _{i}``), which TeX ignores and which keeps it from closing an emphasis;
* no ``$`` right after ``@``: GitHub leaves « recall@$k$ » as text, so write ``recall@k`` (``--fix`` takes a formula of
  letters and digits out of its ``$``; it leaves any other formula after ``@`` for a person to rewrite).

``\\%`` and ``\\#`` have no letter command: a percent sign goes after the formula (``$95$ %``) and ``\\#\\{…\\}``
becomes ``\\operatorname{card}\\lbrace…\\rbrace`` (``annexes/symboles.md``); ``--fix`` does the first when ``\\%`` ends the
formula, and leaves the others for a person to rewrite (``--check`` names them).
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PUNCT = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
ESCAPES = {"{": r"\lbrace", "}": r"\rbrace", ",": r"\thinspace", ":": r"\mkern4mu ", ">": r"\mkern4mu ",
           ";": r"\mkern5mu ", "!": r"\negthinspace", "|": r"\Vert", "\\": r"\cr"}
KEPT = {"$", " "}     # \$ is documented by GitHub; "\ " (a control space) is not a Markdown escape


# ---------------------------------------------------------------------------------------------------- finding formulas
@dataclass
class Span:
    start: int          # index of the first $ in the text
    end: int            # index just after the last $
    display: bool

    def tex(self, text: str) -> str:
        k = 2 if self.display else 1
        return text[self.start + k:self.end - k]


def _code_mask(text: str) -> list[bool]:
    """True for the characters inside a fenced code block or a code span (never read as math)."""
    mask = [False] * len(text)
    for m in re.finditer(r"^( {0,3})(```+|~~~+)[^\n]*\n.*?^\1\2[ \t]*$", text, re.S | re.M):
        for i in range(m.start(), m.end()):
            mask[i] = True
    i = 0
    while i < len(text):
        if text[i] == "`" and not mask[i] and (i == 0 or text[i - 1] != "\\"):
            j = i
            while j < len(text) and text[j] == "`":
                j += 1
            ticks = text[i:j]
            close = text.find(ticks, j)
            while close != -1 and (close + len(ticks) < len(text) and text[close + len(ticks)] == "`"):
                close = text.find(ticks, close + len(ticks) + 1)
            if close != -1 and "\n\n" not in text[j:close]:
                for k in range(i, close + len(ticks)):
                    mask[k] = True
                i = close + len(ticks)
                continue
            i = j
            continue
        i += 1
    return mask


def math_spans(text: str) -> list[Span]:
    """The formulas of a Markdown text: $$…$$ (may span lines) and $…$ (one line), outside code, \\$ excluded."""
    mask = _code_mask(text)
    spans: list[Span] = []
    i, n = 0, len(text)
    while i < n:
        if mask[i] or text[i] != "$" or (i > 0 and text[i - 1] == "\\"):
            i += 1
            continue
        if (i + 1 < n and text[i + 1] == "`" and mask[i + 1]) or (i > 0 and text[i - 1] == "`" and mask[i - 1]):
            i += 1          # the $ of GitHub's $`…`$: the formula is a code span, never read as $-math
            continue
        if text.startswith("$$", i):
            j = i + 2
            while j < n and not (text.startswith("$$", j) and text[j - 1] != "\\") and not mask[j]:
                j += 1
            if j < n and text.startswith("$$", j):
                spans.append(Span(i, j + 2, True))
                i = j + 2
                continue
            i += 2
            continue
        j = i + 1
        while j < n and text[j] != "\n" and not mask[j] and not (text[j] == "$" and text[j - 1] != "\\"):
            j += 1
        if j < n and text[j] == "$" and j > i + 1:
            spans.append(Span(i, j + 1, False))
            i = j + 1
            continue
        i += 1
    return spans


# ---------------------------------------------------------------------------------------------------- escapes, *, <
def fix_tex(tex: str) -> str:
    """The formula with letter commands instead of Markdown-sensitive escapes, \\ast for *, \\lt before a letter."""
    out, i, n = [], 0, len(tex)
    while i < n:
        c = tex[i]
        if c == "\\" and i + 1 < n:
            d = tex[i + 1]
            if d.isalpha():
                j = i + 1
                while j < n and tex[j].isalpha():
                    j += 1
                out.append(tex[i:j])
                i = j
                continue
            if d in ESCAPES:
                cmd = ESCAPES[d]
                nxt = tex[i + 2] if i + 2 < n else ""
                out.append(cmd + (" " if nxt.isalpha() and not cmd.endswith(" ") else ""))
                i += 2
                continue
            if d == "#" and tex.startswith("\\#\\{", i):
                out.append(r"\operatorname{card}")
                i += 2
                continue
            out.append(tex[i:i + 2])
            i += 2
            continue
        if c == "*":
            nxt = tex[i + 1] if i + 1 < n else ""
            out.append(r"\ast" + (" " if nxt.isalpha() else ""))
            i += 1
            continue
        if c == "<" and i + 1 < n and (tex[i + 1].isalpha() or tex[i + 1] in "/!?"):
            out.append(r"\lt ")
            i += 1
            continue
        out.append(c)
        i += 1
    return "".join(out)


def escape_problems(tex: str) -> list[str]:
    """What GitHub would change in this formula (empty when it is safe)."""
    problems, i, n = [], 0, len(tex)
    while i < n:
        c = tex[i]
        if c == "\\" and i + 1 < n:
            d = tex[i + 1]
            if d.isalpha():
                i += 2
                while i < n and tex[i].isalpha():
                    i += 1
                continue
            if d in PUNCT and d not in KEPT:
                problems.append("\\" + d)
            i += 2
            continue
        if c == "*":
            problems.append("*")
        elif c == "<" and i + 1 < n and (tex[i + 1].isalpha() or tex[i + 1] in "/!?"):
            problems.append("<" + tex[i + 1])
        i += 1
    return problems


# ---------------------------------------------------------------------------------------------------- emphasis
def _blocks(text: str):
    """Yield (start, end) of the inline units of a Markdown text: paragraph-like blocks, and each cell of a table row.

    An approximation of CommonMark's blocks, enough for emphasis: a delimiter pairs only inside one unit."""
    mask = _code_mask(text)
    pos = 0
    lines = text.split("\n")
    block_start = None
    offsets = []
    for line in lines:
        offsets.append(pos)
        pos += len(line) + 1
    in_fence = False
    for k, line in enumerate(lines):
        start = offsets[k]
        stripped = re.sub(r"^(\s*>)+\s?", "", line)
        if line and mask[start] and line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
        if in_fence or (line and all(mask[start:start + len(line)])):
            if block_start is not None:
                yield block_start, start - 1
                block_start = None
            continue
        is_table = stripped.strip().startswith("|") and stripped.strip().endswith("|")
        is_heading = re.match(r"\s{0,3}#{1,6}\s", stripped) is not None
        is_item = re.match(r"\s*([-+*]|\d+[.)])\s", stripped) is not None
        if not stripped.strip() or is_table or is_heading or is_item:
            if block_start is not None:
                yield block_start, start - 1
                block_start = None
            if is_table:
                cell = start + (len(line) - len(line.lstrip()))
                for m in re.finditer(r"(?<!\\)\|", line):
                    a = start + m.start()
                    if a > cell:
                        yield cell, a
                    cell = a + 1
            elif is_heading:
                yield start, start + len(line)
            elif is_item:
                block_start = start
            continue
        if block_start is None:
            block_start = start
    if block_start is not None:
        yield block_start, len(text)


def _is_ws(c: str) -> bool:
    return c == "" or c.isspace()


def _is_punct(c: str) -> bool:
    import unicodedata
    return c != "" and (c in PUNCT or unicodedata.category(c).startswith("P"))


def emphasis_pairs(text: str, start: int, end: int, mask: list[bool]) -> list[tuple[int, int]]:
    """CommonMark's emphasis on text[start:end] (code spans and escapes skipped): the matched (opener, closer) indices."""
    runs = []   # [char, index of first char, length, can_open, can_close, original length]
    i = start
    while i < end:
        c = text[i]
        if mask[i]:
            i += 1
            continue
        if c == "\\" and i + 1 < end and text[i + 1] in PUNCT:
            i += 2
            continue
        if c in "*_":
            j = i
            while j < end and text[j] == c and not mask[j]:
                j += 1
            before = text[i - 1] if i > start else ""
            after = text[j] if j < end else ""
            left = not _is_ws(after) and (not _is_punct(after) or _is_ws(before) or _is_punct(before))
            right = not _is_ws(before) and (not _is_punct(before) or _is_ws(after) or _is_punct(after))
            if c == "*":
                can_open, can_close = left, right
            else:
                can_open = left and (not right or _is_punct(before))
                can_close = right and (not left or _is_punct(after))
            runs.append([c, i, j - i, can_open, can_close, j - i])
            i = j
            continue
        i += 1
    pairs = []
    openers_bottom = {}
    k = 0
    while k < len(runs):
        c, idx, length, can_open, can_close, orig = runs[k]
        if can_close and length > 0:
            found = None
            for o in range(k - 1, -1, -1):
                oc, oidx, olen, oopen, oclose, oorig = runs[o]
                if oc != c or olen == 0 or not oopen:
                    continue
                if (oclose or can_open) and (oorig + orig) % 3 == 0 and not (oorig % 3 == 0 and orig % 3 == 0):
                    continue
                found = o
                break
            if found is not None:
                use = 2 if runs[found][2] >= 2 and length >= 2 else 1
                pairs.append((runs[found][1] + runs[found][2] - use, idx))
                runs[found][2] -= use
                runs[k][2] -= use
                runs[k][1] += use
                for o in range(found + 1, k):
                    runs[o][2] = 0
                continue
        k += 1
    return pairs


def emphasis_problems(text: str) -> list[tuple[int, int]]:
    """The emphasis pairs of a Markdown text with at least one delimiter inside a formula."""
    spans = math_spans(text)
    inside = [False] * len(text)
    for s in spans:
        for i in range(s.start, s.end):
            inside[i] = True
    mask = _code_mask(text)
    bad = []
    for a, b in _blocks(text):
        for o, cl in emphasis_pairs(text, a, b, mask):
            if inside[o] or inside[cl]:
                bad.append((o, cl))
    return bad


# ---------------------------------------------------------------------------------------------------- whole files
def _needs_github_syntax(tex: str) -> bool:
    """A matrix or another environment: GitHub never displayed one as $-math (no rendered formula had ``&``,
    ``\\begin`` or ``\\cr``, session 79), even a column vector without ``&``."""
    return "&" in tex or "\\begin{" in tex or "\\cr" in tex


def _github_syntax(text: str) -> str:
    """Three cases that GitHub refuses as $-math whatever the escapes (checked on rendered pages, session 79).

    * A formula with ``&``, ``\\begin{`` or ``\\cr`` (a matrix, a column vector, cases) is never read as math: it goes into GitHub's own syntax, a ```` ```math ```` block
      for a display formula alone on its lines, ``$`…`$`` otherwise (Colab, Jupyter and VS Code then show its TeX as
      code: the price of a readable matrix on GitHub).
    * A formula with a space right inside one of its ``$`` (« $2 + 3 = $ 5 ») is not read: the space goes outside.
    * A formula that ends with ``)`` right before a ``)`` (« (vecteur propre $(1, 6)$) ») is not read either: it gets
      an empty group at its end, ``$(1, 6){}$)``, which TeX ignores.
    """
    out, last = [], 0
    for s in math_spans(text):
        tex = s.tex(text)
        if not _needs_github_syntax(tex):
            if not s.display and tex.strip() and tex != tex.strip():     # « $2 + 3 = $ 5 »: the spaces go outside
                prev, nxt = text[s.start - 1:s.start], text[s.end:s.end + 1]
                lead = "" if prev == "" or prev.isspace() or prev in "([«'’" else " "
                trail = "" if nxt == "" or nxt.isspace() or nxt in ".,;:!?)]»" else " "
                lead = lead if tex[:1].isspace() else ""
                trail = trail if tex[-1:].isspace() else ""
                out.append(text[last:s.start] + lead + "$" + tex.strip() + "$" + trail)
                last = s.end
                tex = tex.strip()
                if tex.endswith(")") and text[s.end:s.end + 1] == ")" and not trail:
                    out[-1] = out[-1][:-1] + "{}$"
                continue
            if tex.rstrip().endswith(")") and text[s.end:s.end + 1] == ")":
                out.append(text[last:s.end - 1] + "{}$")
                last = s.end
            continue
        if "`" in tex:
            continue
        line_start = text.rfind("\n", 0, s.start) + 1
        prefix = text[line_start:s.start]
        line_end = text.find("\n", s.end)
        line_end = len(text) if line_end == -1 else line_end
        if s.display and re.fullmatch(r"[ \t]*(?:>[ \t]?)*", prefix) and not text[s.end:line_end].strip():
            body = [re.sub(r"^[ \t]*(?:>[ \t]?)*", "", line).rstrip() if k else line.rstrip()
                    for k, line in enumerate(tex.strip("\n").split("\n"))]
            block = [prefix + "```math"] + [prefix + line.strip() for line in body if line.strip()] + [prefix + "```"]
            out.append(text[last:line_start] + "\n".join(block))
            last = line_end
            continue
        flat = " ".join(line.strip() for line in tex.split("\n"))
        out.append(text[last:s.start] + "$`" + (r"\displaystyle " if s.display else "") + flat + "`$")
        last = s.end
    out.append(text[last:])
    return "".join(out)


def _unwrap_after_at(text: str) -> str:
    """« recall@$k$ » becomes « recall@k »: GitHub does not read a $ right after @ (rendered pages, session 79).

    Only a formula of letters and digits goes out of its $ (it reads the same as text); any other is left to
    ``problems``."""
    out, last = [], 0
    for s in math_spans(text):
        if (not s.display and s.start > 0 and text[s.start - 1] == "@"
                and re.fullmatch(r"[A-Za-z0-9]+", s.tex(text))):
            out.append(text[last:s.start] + s.tex(text))
            last = s.end
    out.append(text[last:])
    return "".join(out)


def fix_text(text: str) -> str:
    """The text with every formula made safe for GitHub (the prose is never touched)."""
    text = re.sub(r"(?:\\,|\\ |\\;|~)?\\%\$(?!\$)", "$ %", text)          # a percent sign that ends a formula
    text = _unwrap_after_at(text)                                         # recall@$k$ -> recall@k
    for _ in range(3):
        spans = math_spans(text)
        pieces, last = [], 0
        for s in spans:
            k = 2 if s.display else 1
            pieces.append(text[last:s.start + k])
            pieces.append(fix_tex(s.tex(text)))
            pieces.append(text[s.end - k:s.end])
            last = s.end
        pieces.append(text[last:])
        new = "".join(pieces)
        if new == text:
            break
        text = new
    for _ in range(50):         # each round adds a space before the underscores of a formula that close an emphasis
        bad = emphasis_problems(text)
        if not bad:
            break
        spans = math_spans(text)
        inside = [False] * len(text)
        for s in spans:
            for i in range(s.start, s.end):
                inside[i] = True
        targets = set()
        for o, cl in bad:
            for p in (cl, o):
                if inside[p] and text[p] == "_":
                    targets.add(p)
        if not targets:
            break
        for p in sorted(targets, reverse=True):
            text = text[:p] + " " + text[p:]
    return _github_syntax(text)


def problems(text: str) -> list[str]:
    """What GitHub would break in the formulas of this text: one line per problem."""
    out = []
    lines_at = [0]
    for m in re.finditer("\n", text):
        lines_at.append(m.end())

    def line_of(i):
        import bisect
        return bisect.bisect_right(lines_at, i)

    for s in math_spans(text):
        tex = s.tex(text)
        found = escape_problems(tex)
        if _needs_github_syntax(tex):
            found.append("an environment or & (a matrix: GitHub reads it only as ```math or $`…`$)")
        if tex.rstrip().endswith(")") and text[s.end:s.end + 1] == ")":
            found.append(")$) (end the formula with {})")
        if not s.display and tex.strip() and tex != tex.strip():
            found.append("a space right inside a $ (GitHub then does not read the formula)")
        if s.start > 0 and text[s.start - 1] == "@":
            found.append("a $ right after @ (GitHub does not read it: write recall@k)")
        if found:
            out.append(f"line {line_of(s.start)}: {' '.join(sorted(set(found)))} in ${tex[:60]}$")
    for o, cl in emphasis_problems(text):
        out.append(f"line {line_of(o)}: {text[o]} at columns {o - lines_at[line_of(o) - 1] + 1} and line {line_of(cl)} "
                   "would become italics")
    return out


def tracked_markdown(root: Path = ROOT) -> list[Path]:
    """The Markdown files of the repository (git ls-files), never mon_travail/."""
    out = subprocess.run(["git", "-C", str(root), "ls-files", "*.md"], capture_output=True, text=True, check=True)
    return [root / p for p in out.stdout.split() if not p.startswith("mon_travail/")]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--fix", action="store_true")
    parser.add_argument("files", nargs="*", type=Path)
    args = parser.parse_args(argv)
    files = args.files or tracked_markdown()
    status = 0
    for path in files:
        if "mon_travail" in path.parts:
            print(f"⛔ {path}: mon_travail/ is the learner's space")
            status = 1
            continue
        text = path.read_text(encoding="utf-8")
        if args.fix:
            new = fix_text(text)
            if new != text:
                path.write_text(new, encoding="utf-8")
                print(f"fixed {path}")
        left = problems(path.read_text(encoding="utf-8") if args.fix else text)
        for line in left:
            print(f"{path}: {line}")
        status = status or bool(left)
    return 1 if status else 0


if __name__ == "__main__":
    raise SystemExit(main())
