"""Light datasets versioned in ``data/`` (BIBLE §10), each with its card in ``data/cards/``.

>>> import wbm
>>> A = wbm.datasets.load_image("tasse")   # a 400 x 600 photograph in grey levels 0..255 (float64)

The files are rebuilt from their official sources by ``tools/build_datasets.py`` (never copied from workbookIA).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from wbm.core import repo_root

IMAGES = {
    # name: (file in data/images/, shape, card in data/cards/)
    "tasse": ("tasse_cafe.png", (400, 600), "tasse_cafe.md"),
}


def image_path(name: str) -> Path:
    """Path of a versioned image (``KeyError`` with the known names otherwise)."""
    if name not in IMAGES:
        raise KeyError(f"unknown image {name!r}; known images: {', '.join(sorted(IMAGES))}")
    return repo_root() / "data" / "images" / IMAGES[name][0]


def load_image(name: str = "tasse") -> np.ndarray:
    """A versioned grey-level image as a 2-D float64 array (rows = pixel rows), values 0..255 (a fresh copy)."""
    from PIL import Image   # Pillow comes with matplotlib

    path = image_path(name)
    with Image.open(path) as im:
        if im.mode != "L":
            raise ValueError(f"{path.name}: mode {im.mode}, expected L (8-bit grey levels)")
        a = np.asarray(im, dtype=np.float64).copy()
    expected = IMAGES[name][1]
    if a.shape != expected:
        raise ValueError(f"{path.name}: shape {a.shape}, expected {expected}")
    return a
