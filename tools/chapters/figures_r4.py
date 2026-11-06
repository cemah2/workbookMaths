#!/usr/bin/env python
"""Draw the figures of chapter R4 (used by Claude).

    python tools/chapters/figures_r4.py

Writes small PNG files into chapitres/r4_logique_ensembles/figures/: Venn diagrams of the set operations, the
staircase that adds 1 + 2 + … + 6, the table of a double sum, and the dominoes of a proof by induction. Every figure
is computed and uses the workbook style (wbm.plot colours). The numbers are those of the sheet's own examples: none
comes from workbookIA 0B, from the placement test or from an exercise of R4.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "r4_logique_ensembles" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

CENTRE_A, CENTRE_B, RADIUS = (-0.55, 0.0), (0.55, 0.0), 1.0


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def venn_panel(ax, region, title: str) -> None:
    """One Venn diagram in the universe E (a rectangle): the points where region(in_a, in_b) is true are shaded."""
    xs, ys = np.meshgrid(np.linspace(-2.2, 2.2, 500), np.linspace(-1.5, 1.5, 340))
    in_a = (xs - CENTRE_A[0]) ** 2 + (ys - CENTRE_A[1]) ** 2 <= RADIUS**2
    in_b = (xs - CENTRE_B[0]) ** 2 + (ys - CENTRE_B[1]) ** 2 <= RADIUS**2
    mask = region(in_a, in_b)
    ax.contourf(xs, ys, mask.astype(float), levels=[0.5, 1.5], colors=[C[0]], alpha=0.45)
    ax.add_patch(Rectangle((-2.2, -1.5), 4.4, 3.0, fill=False, linewidth=1.5, edgecolor="black"))
    for centre, name, dx in ((CENTRE_A, "A", -1.25), (CENTRE_B, "B", 1.25)):
        ax.add_patch(Circle(centre, RADIUS, fill=False, linewidth=1.8, edgecolor="black"))
        ax.text(centre[0] + dx * 0.55, 0.78, name, fontsize=12, ha="center", fontweight="bold")
    ax.text(-2.05, 1.22, "E", fontsize=11, fontstyle="italic")
    ax.set_title(title, fontsize=11)
    ax.set_xlim(-2.3, 2.3)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect("equal")
    ax.axis("off")


def fig_venn() -> None:
    """§4: union, intersection, difference, complement."""
    fig, axes = plt.subplots(1, 4, figsize=(13, 3.0))
    venn_panel(axes[0], lambda a, b: a | b, "A ∪ B : dans A ou dans B")
    venn_panel(axes[1], lambda a, b: a & b, "A ∩ B : dans A et dans B")
    venn_panel(axes[2], lambda a, b: a & ~b, "A \\ B : dans A, pas dans B")
    venn_panel(axes[3], lambda a, b: ~a, "Ā : dans E, pas dans A")
    fig.tight_layout()
    save(fig, "venn.png")


def fig_staircase() -> None:
    """§5: two staircases 1 + 2 + … + 6 make a 6 × 7 rectangle, so the sum is 6 × 7 / 2."""
    n = 6
    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    for k in range(1, n + 1):
        for row in range(k):
            ax.add_patch(Rectangle((k - 1, row), 1, 1, facecolor=C[0], edgecolor="white", linewidth=1.5))
        for row in range(k, n + 1):
            ax.add_patch(Rectangle((k - 1, row), 1, 1, facecolor=C[1], alpha=0.55, edgecolor="white",
                                   linewidth=1.5))
    for k in range(1, n + 1):
        ax.text(k - 0.5, -0.45, str(k), ha="center", fontsize=10, color=C[0])
    ax.text(n / 2, n + 1.35, "deux escaliers de 1 + 2 + … + 6 = un rectangle de 6 × 7 cases", ha="center",
            fontsize=10)
    ax.annotate("", (n + 0.35, 0), (n + 0.35, n + 1), arrowprops={"arrowstyle": "<->"})
    ax.text(n + 0.55, (n + 1) / 2, "7", fontsize=11, va="center")
    ax.annotate("", (0, -1.0), (n, -1.0), arrowprops={"arrowstyle": "<->"})
    ax.text(n / 2, -1.55, "6", fontsize=11, ha="center")
    ax.set_xlim(-0.5, n + 1.2)
    ax.set_ylim(-1.9, n + 1.8)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "escalier.png")


def fig_double_sum() -> None:
    """§5: the table of a(i, j) = i + j for i = 1..3 and j = 1, 2; rows first or columns first, the same total."""
    rows, cols, w = 3, 2, 1.8
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            y = rows - i
            ax.add_patch(Rectangle(((j - 1) * w, y), w, 1, facecolor=C[0], alpha=0.18, edgecolor="black"))
            ax.text((j - 0.5) * w, y + 0.5, f"{i} + {j} = {i + j}", ha="center", va="center", fontsize=10.5)
        ax.text(cols * w + 0.2, rows - i + 0.5, f"ligne i = {i} : {sum(i + j for j in range(1, cols + 1))}",
                va="center", fontsize=10.5, color=C[1])
    for j in range(1, cols + 1):
        ax.text((j - 0.5) * w, rows + 0.25, f"j = {j}", ha="center", fontsize=10.5)
        ax.text((j - 0.5) * w, -0.4, f"{sum(i + j for i in range(1, rows + 1))}", ha="center", fontsize=10.5,
                color=C[2])
    ax.text(-0.15, -0.4, "colonnes :", ha="right", fontsize=10.5, color=C[2])
    total = sum(i + j for i in range(1, rows + 1) for j in range(1, cols + 1))
    ax.text(w, -1.05, f"total : 5 + 7 + 9 = 9 + 12 = {total}", ha="center", fontsize=11, fontweight="bold")
    ax.set_xlim(-2.0, cols * w + 2.6)
    ax.set_ylim(-1.4, rows + 0.6)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "somme_double.png")


def fig_dominoes() -> None:
    """§7: the first domino falls (initialisation) and each one knocks the next over (heredity)."""
    fig, ax = plt.subplots(figsize=(8.5, 2.7))
    width, height, gap = 0.28, 1.6, 0.9
    tilt = float(np.degrees(np.arcsin((gap - width) / height)))   # a fallen domino leans on the next one
    for k in range(7):
        x = k * gap
        angle = -tilt if k < 2 else (-12 if k == 2 else 0)
        colour = C[1] if k < 3 else C[0]
        patch = Rectangle((x, 0), width, height, angle=angle, rotation_point=(x + width, 0), facecolor=colour,
                          edgecolor="black", alpha=0.85)
        ax.add_patch(patch)
        ax.text(x + width / 2, -0.35, f"P({k})" if k < 6 else "…", ha="center", fontsize=10)
    ax.add_patch(FancyArrowPatch((-0.7, 1.75), (0.05, 1.2), arrowstyle="->", mutation_scale=14, color="black"))
    ax.text(-0.95, 1.95, "initialisation : P(0) est vraie", fontsize=9.5)
    ax.add_patch(FancyArrowPatch((2.45, 1.95), (3.2, 1.75), arrowstyle="->", mutation_scale=14, color="black"))
    ax.text(2.35, 2.1, "hérédité : si P(n) tombe, P(n + 1) tombe", fontsize=9.5)
    ax.set_xlim(-1.1, 6.3)
    ax.set_ylim(-0.6, 2.5)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "dominos.png")


def main() -> int:
    print(f"Figures of R4 -> {OUT.relative_to(ROOT)}")
    fig_venn()
    fig_staircase()
    fig_double_sum()
    fig_dominoes()
    return 0


if __name__ == "__main__":
    sys.exit(main())
