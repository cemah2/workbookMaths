"""Tests of wbm.datasets and tools/build_datasets.py: the versioned files, their cards, the loader."""

import hashlib
import sys
from pathlib import Path

import numpy as np
import pytest

import wbm
from wbm import datasets

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

import build_datasets  # noqa: E402


def test_tasse_loads_as_grey_levels():
    A = wbm.datasets.load_image("tasse")
    assert A.shape == (400, 600) and A.dtype == np.float64
    assert A.min() >= 0 and A.max() <= 255 and np.all(A == np.round(A))
    assert 90 < A.mean() < 120          # a dark photograph (mean grey level about 104)
    A[0, 0] = -1                        # a fresh copy each time
    assert wbm.datasets.load_image("tasse")[0, 0] >= 0


def test_tasse_pixels_match_the_build_tool():
    digest, shape = build_datasets.pixels_sha256(datasets.image_path("tasse"))
    assert digest == build_datasets.TASSE["pixels_sha256"] and tuple(shape) == build_datasets.TASSE["shape"]


def test_grey_levels_formula():
    rgb = np.array([[[255, 255, 255], [0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [10, 200, 30]]],
                   dtype=np.uint8)
    expected = [255, 0, 76, 150, 29, 0]
    expected[5] = (19595 * 10 + 38470 * 200 + 7471 * 30 + 32768) >> 16
    assert build_datasets.grey_levels(rgb).tolist() == [expected]


def test_every_image_has_a_card():
    readme = (ROOT / "data" / "cards" / "README.md").read_text(encoding="utf-8")
    for name, (filename, _shape, card) in datasets.IMAGES.items():
        assert (ROOT / "data" / "images" / filename).exists(), filename
        text = (ROOT / "data" / "cards" / card).read_text(encoding="utf-8")
        assert "CC0" in text and "tools/build_datasets.py" in text, card
        assert card in readme, f"{card} is not listed in data/cards/README.md"


def test_unknown_image():
    with pytest.raises(KeyError, match="tasse"):
        datasets.load_image("lena")


def test_versioned_png_is_small():
    for filename, _shape, _card in datasets.IMAGES.values():
        assert (ROOT / "data" / "images" / filename).stat().st_size < 300_000


def test_source_hash_is_recorded():
    assert len(build_datasets.TASSE["source_sha256"]) == 64
    assert hashlib.sha256(b"").hexdigest() != build_datasets.TASSE["source_sha256"]
