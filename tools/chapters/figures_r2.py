#!/usr/bin/env python
"""Draw the figures of the course sheet of chapter R2 (used by Claude).

    python tools/chapters/figures_r2.py

Writes small PNG files into chapitres/r2_calcul_litteral/figures/. Every figure is computed and uses the workbook
style (wbm.plot colours, French decimal commas). The numbers are those of the sheet's own examples: none comes from
an exercise of R2, of the placement test or of workbookIA 0A/0B.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "r2_calcul_litteral" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and axis.get_major_formatter().__class__.__name__ != "StrCategoryFormatter":
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def number_line(ax, low: float, high: float, y: float = 0.0) -> None:
    ax.plot([low - 0.3, high + 0.3], [y, y], color="black", linewidth=1)
    for k in range(math.ceil(low), math.floor(high) + 1):
        ax.plot([k, k], [y - 0.06, y + 0.06], color="black", linewidth=1)
        ax.text(k, y - 0.22, french_number(k), ha="center", va="top", fontsize=8)


def bracket(ax, x: float, y: float, closed: bool, left: bool, colour) -> None:
    """A bracket [ or ] drawn at x: turned towards the interval when closed, away from it when open."""
    facing_right = left == closed
    d = 0.12 if facing_right else -0.12
    ax.plot([x + d, x, x, x + d], [y - 0.13, y - 0.13, y + 0.13, y + 0.13], color=colour, linewidth=2)


def segment(ax, low, high, y, left_closed, right_closed, colour, label) -> None:
    ax.plot([low, high], [y, y], color=colour, linewidth=5, alpha=0.75, solid_capstyle="butt")
    if math.isfinite(low):
        bracket(ax, low, y, left_closed, True, colour)
    if math.isfinite(high):
        bracket(ax, high, y, right_closed, False, colour)
    ax.text(-3.4, y, label, ha="right", va="center", fontsize=9, color=colour)


def fig_intervals() -> None:
    """§5: A = [−1 ; 4], B = [2 ; 6], their intersection and their union."""
    fig, ax = plt.subplots(figsize=(7.4, 2.9))
    rows = [("A = [−1 ; 4]", -1, 4, True, True, C[0]), ("B = [2 ; 6]", 2, 6, True, True, C[1]),
            ("A ∩ B = [2 ; 4]", 2, 4, True, True, C[2]), ("A ∪ B = [−1 ; 6]", -1, 6, True, True, C[3])]
    for i, (label, low, high, lc, rc, colour) in enumerate(rows):
        y = 3 - i
        ax.plot([-3, 8], [y, y], color="lightgray", linewidth=0.8)
        segment(ax, low, high, y, lc, rc, colour, label)
    number_line(ax, -3, 8, y=-0.6)
    ax.set_xlim(-6.8, 8.5)
    ax.set_ylim(-1.2, 3.5)
    ax.axis("off")
    ax.set_title("Intersection : dans les deux à la fois ; réunion : dans l'un ou dans l'autre", fontsize=10)
    save(fig, "intervalles.png")


def fig_absolute_value() -> None:
    """§6: |x + 2| = 5 has two solutions, |x − 3| < 1,5 is an interval around 3."""
    fig, axes = plt.subplots(2, 1, figsize=(7.4, 3.0))
    ax = axes[0]
    number_line(ax, -8, 4)
    ax.plot([-2], [0], "o", color=C[3], markersize=7)
    ax.text(-2, 0.3, "−2", ha="center", fontsize=9, color=C[3])
    for x in (-7, 3):
        ax.plot([x], [0], "o", color=C[0], markersize=8)
        ax.annotate("", xy=(x, 0.18), xytext=(-2, 0.18), arrowprops={"arrowstyle": "->", "color": C[0]})
    ax.text(-4.5, 0.42, "distance 5", ha="center", fontsize=9, color=C[0])
    ax.text(0.5, 0.42, "distance 5", ha="center", fontsize=9, color=C[0])
    ax.set_title("|x + 2| = 5 : les points à distance 5 de −2, soit −7 et 3", fontsize=10)
    ax.set_xlim(-8.6, 4.6)
    ax.set_ylim(-0.6, 0.8)
    ax.axis("off")
    ax = axes[1]
    number_line(ax, -1, 7)
    ax.plot([1.5, 4.5], [0, 0], color=C[2], linewidth=5, alpha=0.75)
    bracket(ax, 1.5, 0, False, True, C[2])
    bracket(ax, 4.5, 0, False, False, C[2])
    ax.plot([3], [0], "o", color=C[3], markersize=7)
    ax.text(3, 0.3, "3", ha="center", fontsize=9, color=C[3])
    ax.set_title("|x − 3| < 1,5 : les points à moins de 1,5 de 3, soit ]1,5 ; 4,5[", fontsize=10)
    ax.set_xlim(-1.6, 7.6)
    ax.set_ylim(-0.6, 0.8)
    ax.axis("off")
    fig.tight_layout()
    save(fig, "valeur_absolue.png")


def fig_systems() -> None:
    """§7: one solution, no solution, infinitely many solutions."""
    xs = np.linspace(-2, 5, 50)
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.3), sharey=True)
    cases = [("une seule solution : (2 ; −1)", [(3, 2, 4, "3x + 2y = 4"), (1, -4, 6, "x − 4y = 6")], (2, -1)),
             ("aucune solution (parallèles)", [(1, -3, 3, "x − 3y = 3"), (1, -3, -3, "x − 3y = −3")], None),
             ("une infinité (même droite)", [(1, -3, 3, "x − 3y = 3"), (2, -6, 6, "2x − 6y = 6")], None)]
    for ax, (title, lines, point) in zip(axes, cases):
        for k, (a, b, c, label) in enumerate(lines):
            style = "--" if k == 1 else "-"
            ax.plot(xs, (c - a * xs) / b, style, color=C[k], linewidth=2.2 if k == 0 else 1.8, label=label)
        if point:
            ax.plot(*point, "o", color="black", markersize=7, zorder=3)
        ax.axhline(0, color="gray", linewidth=0.6)
        ax.axvline(0, color="gray", linewidth=0.6)
        ax.set_xlim(-2, 5)
        ax.set_ylim(-4, 4)
        ax.set_title(title, fontsize=10)
        ax.legend(fontsize=8, loc="upper right")
        ax.grid(True, alpha=0.3)
        ax.set_xlabel("x")
    axes[0].set_ylabel("y")
    fig.tight_layout()
    save(fig, "systemes_droites.png")


def fig_square_identity() -> None:
    """§3: (a + b)² = a² + 2ab + b², read on a square of side a + b."""
    a, b = 3.0, 1.6
    fig, ax = plt.subplots(figsize=(3.8, 3.8))
    parts = [((0, 0), a, a, C[0], "a²"), ((a, 0), b, a, C[1], "ab"), ((0, a), a, b, C[1], "ab"),
             ((a, a), b, b, C[2], "b²")]
    for (x, y), w, h, colour, label in parts:
        ax.add_patch(Rectangle((x, y), w, h, facecolor=colour, alpha=0.35, edgecolor="black"))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=13)
    ax.text(a / 2, -0.35, "a", ha="center", fontsize=12)
    ax.text(a + b / 2, -0.35, "b", ha="center", fontsize=12)
    ax.text(-0.35, a / 2, "a", va="center", fontsize=12)
    ax.text(-0.35, a + b / 2, "b", va="center", fontsize=12)
    ax.set_xlim(-0.7, a + b + 0.2)
    ax.set_ylim(-0.7, a + b + 0.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(a + b)² = a² + 2ab + b²", fontsize=11)
    save(fig, "carre_somme.png")


def main() -> int:
    print(f"Figures of R2 -> {OUT.relative_to(ROOT)}")
    fig_intervals()
    fig_absolute_value()
    fig_systems()
    fig_square_identity()
    return 0


if __name__ == "__main__":
    sys.exit(main())
