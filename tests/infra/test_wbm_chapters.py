"""The chapter ids, the study order and the common order with workbookIA (BIBLE §8-9)."""

import re
from pathlib import Path

import pytest

from wbm import chapters

ROOT = Path(__file__).resolve().parents[2]


def test_49_chapters_in_the_order_of_the_bible():
    """The ids and the order of wbm.chapters are those of the tables of BIBLE §8."""
    bible = (ROOT / "docs" / "BIBLE.md").read_text(encoding="utf-8")
    plan = bible.split("## 8.")[1].split("## 9.")[0]
    in_bible = re.findall(r"^\|(?: [^|]* \|)? (POS|PS|CP\d|R\d|M\d\d[a-d]?|MB\d) \|", plan, re.M)
    in_bible = list(dict.fromkeys(in_bible))     # a CP row repeats its id in two columns
    assert list(chapters.CHAPTER_ORDER) == in_bible
    assert len([c for c in chapters.CHAPTER_ORDER if c[0] in "RM"]) == 49


def test_titles_and_parts_cover_every_chapter():
    assert set(chapters.TITLES) == set(chapters.PARTS) == set(chapters.CHAPTER_ORDER)
    assert set(chapters.PARTS.values()) <= set(chapters.PART_TITLES)


@pytest.mark.parametrize("cid, ia", [("R4", "0B"), ("CP0", "0B"), ("M02a", "2"), ("M12c", "12"), ("M25b", "25"),
                                     ("MB3", "B3"), ("CP2", None), ("PS", None), ("POS", None)])
def test_ia_chapter_of(cid, ia):
    assert chapters.ia_chapter_of(cid) == ia


def test_every_math_chapter_prepares_an_existing_workbookia_chapter():
    for cid in chapters.CHAPTER_ORDER:
        ia = chapters.ia_chapter_of(cid)
        assert ia is None or ia in chapters.IA_CHAPTERS, cid


@pytest.mark.parametrize("ia", ["1", "15", "23", "24", "29", "B1", "B7"])
def test_workbookia_chapters_without_maths(ia):
    assert chapters.chapters_before_ia(ia) == []


def test_common_order_alternates_the_two_workbooks():
    order = chapters.common_order()
    maths = [cid for book, cid in order if book == "maths"]
    assert maths == list(chapters.CHAPTER_ORDER), "every math chapter once, in study order"
    ia = [cid for book, cid in order if book == "IA" and not cid.startswith("CP")]
    assert ia == [*chapters.IA_CHAPTERS, "PF"], "every workbookIA chapter once, in its own order"
    position = {item: index for index, item in enumerate(order)}
    for cid in chapters.CHAPTER_ORDER:                # a math chapter comes just before the chapter it prepares
        target = chapters.ia_chapter_of(cid)
        if target and target != "0B":
            assert position[("maths", cid)] < position[("IA", target)], cid
    for n in range(1, 7):                             # a mock exam just before workbookIA's checkpoint
        assert position[("IA", f"CP{n}")] == position[("maths", f"CP{n}")] + 1


@pytest.mark.parametrize("raw", ["M15", "R10", "MB7", "M02e", "x"])
def test_unknown_ids(raw):
    with pytest.raises(ValueError):
        chapters.canonical_id(raw)
