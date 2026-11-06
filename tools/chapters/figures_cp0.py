#!/usr/bin/env python
"""Draw the figure of the mock exam CP0 (used by Claude).

    python tools/chapters/figures_cp0.py

Writes checkpoints/partie_0/figures/droites.png: the three lines of CP0.3 on a grid, D1: 3x + y = 9,
D2: x - 2y = -4 and D3, whose equation the learner reads through two grid points, (0 ; -2) and (2 ; 2). The
intersection points are not marked: finding them is the question. The lines come from no exercise of R0 to R9, of
the placement test or of workbookIA.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter, MultipleLocator  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "checkpoints" / "partie_0" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def fig_lines() -> None:
    """CP0.3: three lines; D3 goes through the grid points (0 ; -2) and (2 ; 2)."""
    fig, ax = plt.subplots(figsize=(6.2, 7.2))
    xs = np.linspace(-2, 6, 2)
    ax.plot(xs, 9 - 3 * xs, color=C[0], linewidth=2)
    ax.plot(xs, (xs + 4) / 2, color=C[1], linewidth=2)
    ax.plot(xs, 2 * xs - 2, color=C[2], linewidth=2)
    ax.text(-1.0, 11.0, "D1", color=C[0], fontsize=13, fontweight="bold")
    ax.text(5.2, 5.3, "D2", color=C[1], fontsize=13, fontweight="bold")
    ax.text(3.3, 7.4, "D3", color=C[2], fontsize=13, fontweight="bold")
    ax.axhline(0, color="gray", linewidth=0.9)
    ax.axvline(0, color="gray", linewidth=0.9)
    ax.set_xlim(-2, 6)
    ax.set_ylim(-5, 12)
    ax.set_aspect("equal")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.grid(True, alpha=0.45)
    for axis in (ax.xaxis, ax.yaxis):
        axis.set_major_formatter(FuncFormatter(french_number))
    ax.set_title("Les droites D1, D2 et D3 (une unité par carreau)", fontsize=10)
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "droites.png", dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("  droites.png")


def main() -> int:
    print(f"Figures of CP0 -> {OUT.relative_to(ROOT)}")
    fig_lines()
    return 0


if __name__ == "__main__":
    sys.exit(main())
