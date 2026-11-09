#!/usr/bin/env python
"""Rebuild the light datasets versioned in ``data/`` from their official sources (BIBLE §10).

    python tools/build_datasets.py --check                 # checks the versioned files (no network)
    python tools/build_datasets.py tasse                   # downloads the scikit-image wheel from PyPI, rebuilds
    python tools/build_datasets.py tasse --wheel FILE.whl  # same, from a wheel already downloaded

Each dataset has its card in ``data/cards/``. The files are never copied from workbookIA.

``tasse`` (``data/images/tasse_cafe.png``): the photograph ``coffee.png`` shipped with scikit-image 0.25.2
(CC0, Rachel Michetti, Pikolo Espresso Bar), converted to grey levels with the ITU-R BT.601 weights in integer
arithmetic, ``L = (19595 R + 38470 G + 7471 B + 32768) >> 16`` (the formula of Pillow's ``convert("L")``), then
saved as an 8-bit PNG of 400 x 600 pixels. The wheel is downloaded into ``data/downloads/`` (not versioned) and
only read as a zip archive: nothing from it is imported or run.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import subprocess
import sys
import zipfile
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = ROOT / "data" / "downloads"

TASSE = {
    "package": "scikit-image==0.25.2",
    "member": "skimage/data/coffee.png",
    "source_sha256": "cc02f8ca188b167c775a7101b5d767d1e71792cf762c33d6fa15a4599b5a8de7",   # the RGB PNG in the wheel
    "out": ROOT / "data" / "images" / "tasse_cafe.png",
    "shape": (400, 600),
    "pixels_sha256": "3e8857c7e771b09cbf5d2e6e60d921830a1b1f097fe066f05d238ba19f87bf61",   # the uint8 grey levels
}


def grey_levels(rgb: np.ndarray) -> np.ndarray:
    """ITU-R BT.601 luma in integer arithmetic (as Pillow's ``convert("L")``): uint8 array of shape (m, n)."""
    r, g, b = (rgb[..., i].astype(np.int64) for i in range(3))
    return ((19595 * r + 38470 * g + 7471 * b + 32768) >> 16).astype(np.uint8)


def pixels_sha256(path: Path) -> tuple[str, tuple[int, ...]]:
    from PIL import Image

    with Image.open(path) as im:
        if im.mode != "L":
            raise SystemExit(f"{path}: mode {im.mode}, expected L (8-bit grey levels)")
        a = np.asarray(im, dtype=np.uint8)
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest(), a.shape


def _download_wheel() -> Path:
    DOWNLOADS.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, "-m", "pip", "download", TASSE["package"], "--no-deps", "--only-binary=:all:",
           "-d", str(DOWNLOADS), "-q"]
    subprocess.run(cmd, check=True)
    wheels = sorted(DOWNLOADS.glob("scikit_image-0.25.2-*.whl"))
    if not wheels:
        raise SystemExit("no scikit-image 0.25.2 wheel downloaded")
    return wheels[0]


def build_tasse(wheel: Path | None) -> None:
    from PIL import Image

    wheel = wheel or _download_wheel()
    with zipfile.ZipFile(wheel) as z:
        data = z.read(TASSE["member"])
    digest = hashlib.sha256(data).hexdigest()
    if digest != TASSE["source_sha256"]:
        raise SystemExit(f"{TASSE['member']}: SHA-256 {digest}, expected {TASSE['source_sha256']}")
    with Image.open(io.BytesIO(data)) as im:
        rgb = np.asarray(im.convert("RGB"), dtype=np.uint8)
    grey = grey_levels(rgb)
    out = TASSE["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(grey, mode="L").save(out, optimize=True)
    check_tasse()
    print(f"written {out.relative_to(ROOT)} ({out.stat().st_size} bytes)")


def check_tasse() -> bool:
    out = TASSE["out"]
    if not out.exists():
        print(f"missing: {out.relative_to(ROOT)}")
        return False
    digest, shape = pixels_sha256(out)
    ok = digest == TASSE["pixels_sha256"] and tuple(shape) == TASSE["shape"]
    print(f"{'ok' if ok else 'DIFFERENT'}: {out.relative_to(ROOT)} {shape}")
    return ok


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("dataset", nargs="?", choices=["tasse"], help="dataset to rebuild")
    parser.add_argument("--wheel", type=Path, help="scikit-image 0.25.2 wheel already downloaded")
    parser.add_argument("--check", action="store_true", help="only check the versioned files")
    args = parser.parse_args(argv)
    if args.check or not args.dataset:
        return 0 if check_tasse() else 1
    build_tasse(args.wheel)
    return 0


if __name__ == "__main__":
    sys.exit(main())
