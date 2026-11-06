#!/usr/bin/env python
"""Draw the figure of the placement test POS (used by Claude).

    python tools/chapters/figures_pos.py

Writes positionnement/figures/pos_5_graphique.png: the graph read in exercise POS.5 (a piecewise linear function
through integer points, so that every reading is exact).
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import FuncFormatter, MultipleLocator  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "positionnement" / "figures"
DPI = 110
POINTS = [(-3, -1), (-1, 3), (2, -3), (4, 1)]     # the graph of g in POS.5


def french_number(value: float, _pos=None) -> str:
    return f"{value:g}".replace(".", ",").replace("-", "−")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    xs, ys = zip(*POINTS)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(xs, ys, color=wbplot.CATEGORICAL[0], lw=2, label="courbe de g")
    ax.plot([xs[0], xs[-1]], [ys[0], ys[-1]], "o", color=wbplot.CATEGORICAL[0], ms=5)
    ax.axhline(0, color=wbplot.TEXT_MUTED, lw=0.9)
    ax.axvline(0, color=wbplot.TEXT_MUTED, lw=0.9)
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    for axis in (ax.xaxis, ax.yaxis):
        axis.set_major_formatter(FuncFormatter(french_number))
    ax.grid(True, color=wbplot.GRID)
    ax.set_xlim(-3.5, 4.5)
    ax.set_ylim(-3.5, 3.5)
    ax.set_xlabel("x")
    ax.set_ylabel("g(x)")
    ax.set_title("La fonction g, définie sur [−3 ; 4]")
    ax.legend(loc="upper right")
    fig.savefig(OUT / "pos_5_graphique.png", dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("  positionnement/figures/pos_5_graphique.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
