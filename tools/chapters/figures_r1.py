#!/usr/bin/env python
"""Draw the figures of the course sheet of chapter R1 (used by Claude).

    python tools/chapters/figures_r1.py

Writes small PNG files into chapitres/r1_nombres_calcul/figures/. Every figure is computed and uses the workbook
style (wbm.plot colours, French decimal commas). The numbers shown are those of the sheet's own examples: none comes
from an exercise of R1, of the placement test or of workbookIA 0A/0B.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Ellipse, Polygon  # noqa: E402
from matplotlib.category import StrCategoryFormatter  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "r1_nombres_calcul" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and not isinstance(axis.get_major_formatter(), StrCategoryFormatter):
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def number_line(ax, low: float, high: float) -> None:
    """A horizontal number line with integer ticks, no frame."""
    ax.axhline(0, color="black", linewidth=1)
    for k in range(math.ceil(low), math.floor(high) + 1):
        ax.plot([k, k], [-0.08, 0.08], color="black", linewidth=1)
        ax.text(k, -0.28, french_number(k), ha="center", va="top", fontsize=10)
    ax.annotate("", xy=(high + 0.3, 0), xytext=(high, 0), arrowprops={"arrowstyle": "->", "color": "black"})
    ax.set_xlim(low - 0.4, high + 0.5)
    ax.set_ylim(-1.0, 1.4)
    ax.axis("off")


def fig_number_line() -> None:
    """§1: a few numbers on the line, coloured by the smallest set that contains them."""
    # (value, label, set, colour, x of the label, height of the label)
    points = [(-3, "−3", "ℤ", C[1], -3, 0.45), (-0.75, "−0,75", "𝔻", C[2], -0.95, 0.85),
              (0, "0", "ℕ", C[0], -0.35, 0.45), (1 / 3, "1/3", "ℚ", C[3], 0.75, 0.85),
              (math.sqrt(2), "√2", "ℝ", C[4], 1.2, 0.45), (2, "2", "ℕ", C[0], 2.3, 0.85),
              (math.pi, "π", "ℝ", C[4], 3.35, 0.45)]
    fig, ax = plt.subplots(figsize=(7.5, 1.9))
    number_line(ax, -4, 4)
    for x, label, family, colour, text_x, height in points:
        ax.plot(x, 0, "o", color=colour, markersize=8, zorder=3)
        ax.annotate(f"{label}  ({family})", xy=(x, 0.05), xytext=(text_x, height), ha="center", fontsize=10,
                    arrowprops={"arrowstyle": "-", "color": colour, "linewidth": 0.8})
    ax.set_title("Quelques nombres sur la droite, avec le plus petit ensemble qui les contient", fontsize=10)
    save(fig, "droite_numerique.png")


def fig_nested_sets() -> None:
    """§1: ℕ ⊂ ℤ ⊂ 𝔻 ⊂ ℚ ⊂ ℝ, with examples in each ring."""
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    rings = [("ℝ", 6.8, 3.7, "√2   π   √5"), ("ℚ", 5.4, 2.9, "1/3   −5/7"), ("𝔻", 4.0, 2.1, "−0,75   2,05"),
             ("ℤ", 2.6, 1.35, "−3   −12"), ("ℕ", 1.5, 0.7, "0  2  17")]
    for i, (name, width, height, examples) in enumerate(rings):
        ax.add_patch(Ellipse((0, 0), width * 1.25, height * 1.1, facecolor=C[4 - i], alpha=0.18,
                             edgecolor=C[4 - i], linewidth=1.5))
        ax.text(-width * 0.62 + (0.15 if i < 4 else 0.05), 0, name, fontsize=15 if i < 4 else 12, va="center",
                color=C[4 - i], fontweight="bold")
        if i < 4:
            ax.text(0, height * 0.55 - 0.12, examples, fontsize=10, ha="center", va="top")
        else:
            ax.text(0.2, 0, examples, fontsize=9, ha="center", va="center")
    ax.set_xlim(-4.4, 4.4)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Chaque ensemble contient le précédent : ℕ ⊂ ℤ ⊂ 𝔻 ⊂ ℚ ⊂ ℝ", fontsize=10)
    save(fig, "ensembles_emboites.png")


def fig_floor_ceil() -> None:
    """§6: floor, ceiling and rounding of 2,4 and of −1,6 on the line."""
    fig, ax = plt.subplots(figsize=(7.5, 2.1))
    number_line(ax, -3, 4)
    for x, label, colour in [(2.4, "2,4", C[0]), (-1.6, "−1,6", C[1])]:
        low, high = math.floor(x), math.ceil(x)
        ax.plot(x, 0, "o", color=colour, markersize=8, zorder=3)
        ax.text(x, 0.25, label, ha="center", fontsize=10, color=colour)
        ax.annotate("", xy=(low, 0.62), xytext=(x, 0.62), arrowprops={"arrowstyle": "->", "color": colour})
        ax.annotate("", xy=(high, 0.62), xytext=(x, 0.62), arrowprops={"arrowstyle": "->", "color": colour,
                                                                          "linestyle": "--"})
        ax.text(low, 0.82, f"⌊{label}⌋ = {french_number(low)}", ha="center", fontsize=9, color=colour)
        ax.text(high, 1.1, f"⌈{label}⌉ = {french_number(high)}", ha="center", fontsize=9, color=colour)
    ax.set_title("Le plancher descend vers la gauche, le plafond monte vers la droite (même pour un négatif)",
                 fontsize=10)
    save(fig, "plancher_plafond.png")


def fig_successive_changes() -> None:
    """§7: +50 % then −50 % does not come back to the start."""
    values = [100, 150, 75]
    labels = ["départ", "après +50 %", "puis −50 %"]
    fig, ax = plt.subplots(figsize=(6.2, 3.2))
    bars = ax.bar(labels, values, color=[C[0], C[2], C[1]], width=0.55)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 3, f"{value}", ha="center", fontsize=10)
    ax.axhline(100, color="gray", linewidth=0.8, linestyle="--")
    ax.text(2.33, 103, "niveau de départ", fontsize=8, color="gray", ha="right")
    ax.annotate("× 1,5", xy=(0.36, 128), fontsize=10, color=C[2], fontweight="bold")
    ax.annotate("× 0,5", xy=(1.36, 122), fontsize=10, color=C[1], fontweight="bold")
    ax.set_ylim(0, 175)
    ax.set_ylabel("valeur")
    ax.set_title("Les coefficients se multiplient : 1,5 × 0,5 = 0,75, soit −25 %", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "evolutions_successives.png")


def fig_weighted_mean_lever() -> None:
    """§8: the weighted mean is the balance point of a lever: 8 (weight 1) and 14 (weight 2) balance at 12."""
    fig, ax = plt.subplots(figsize=(6.8, 2.6))
    ax.plot([6, 16], [0, 0], color="black", linewidth=3)
    for k in range(6, 17):
        ax.plot([k, k], [-0.07, 0.07], color="black", linewidth=0.8)
        if k != 12:   # the fulcrum stands on 12: its own label says so
            ax.text(k, -0.45, french_number(k), ha="center", fontsize=9)
    ax.add_patch(Polygon([[12, -0.05], [11.6, -0.7], [12.4, -0.7]], closed=True, color=C[3]))
    ax.text(12, -1.05, "point d'équilibre : 12", ha="center", fontsize=9, color=C[3])
    ax.add_patch(plt.Rectangle((7.7, 0.05), 0.6, 0.45, color=C[0]))
    ax.text(8, 0.65, "8 (poids 1)", ha="center", fontsize=9)
    for dy in (0.05, 0.5):
        ax.add_patch(plt.Rectangle((13.7, dy), 0.6, 0.43, color=C[1]))
    ax.text(14, 1.1, "14 (poids 2)", ha="center", fontsize=9)
    ax.set_xlim(5.5, 16.5)
    ax.set_ylim(-1.3, 1.5)
    ax.axis("off")
    ax.set_title("La moyenne pondérée est le point d'équilibre : (1 × 8 + 2 × 14) / 3 = 12", fontsize=10)
    save(fig, "moyenne_ponderee_levier.png")


def main() -> int:
    print(f"Figures of R1 -> {OUT.relative_to(ROOT)}")
    fig_number_line()
    fig_nested_sets()
    fig_floor_ceil()
    fig_successive_changes()
    fig_weighted_mean_lever()
    return 0


if __name__ == "__main__":
    sys.exit(main())
