#!/usr/bin/env python
"""Draw the figures of chapter M09a (used by Claude).

    python tools/chapters/figures_m09a.py

Writes small PNG files into chapitres/m09a_matrices/figures/: the matrix-vector product of the fiche read as a
combination of the columns (2 a₁ + 1 a₂ + 1 a₃ = (4, 5)), the three cases of a system of two equations in two unknowns,
and the pattern of a reduced row echelon form. None comes from workbookIA 0B, 9 or 10 (no shape diagram of a product,
no tempo of a shop, no neuron weights named AD or BE).
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m09a_matrices" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear":
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def arrow(ax, start, vector, color, label, offset=(0.1, 0.1)):
    ax.annotate("", xy=(start[0] + vector[0], start[1] + vector[1]), xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2, "mutation_scale": 14})
    mid = (start[0] + vector[0] / 2 + offset[0], start[1] + vector[1] / 2 + offset[1])
    ax.text(*mid, label, color=color, fontsize=11)


def columns() -> None:
    """A x as a combination of the columns: 2 a1 + 1 a2 + 1 a3, head to tail, ends at (4, 5)."""
    a1, a2, a3 = np.array([1, 3]), np.array([-2, 0]), np.array([4, -1])
    fig, ax = plt.subplots(figsize=(5.8, 5.2))
    p0 = np.array([0, 0])
    p1 = p0 + 2 * a1
    p2 = p1 + a2
    p3 = p2 + a3
    arrow(ax, p0, 2 * a1, C[0], "2 a₁", (0.15, -0.2))
    arrow(ax, p1, a2, C[1], "1 a₂", (-0.2, 0.25))
    arrow(ax, p2, a3, C[2], "1 a₃", (0.1, 0.25))
    ax.annotate("", xy=p3, xytext=p0, arrowprops={"arrowstyle": "-|>", "color": "black", "lw": 2.5,
                                                   "mutation_scale": 16, "ls": "--"})
    ax.text(p3[0] + 0.15, p3[1] - 0.1, "Ax = (4, 5)", fontsize=11)
    for col, name, color, shift in [(a1, "a₁ = (1, 3)", C[0], (-1.75, 0.05)), (a2, "a₂ = (−2, 0)", C[1], (0.1, -0.45)),
                                    (a3, "a₃ = (4, −1)", C[2], (0.1, -0.45))]:
        ax.plot(*col, "o", color=color, ms=5)
        ax.text(col[0] + shift[0], col[1] + shift[1], name, color=color, fontsize=9)
    ax.axhline(0, color="gray", lw=0.6)
    ax.axvline(0, color="gray", lw=0.6)
    ax.set(xlim=(-2.8, 5.6), ylim=(-1.8, 7), aspect="equal",
           title="A x : la combinaison des colonnes de A, de coefficients (2, 1, 1)")
    ax.grid(alpha=0.3)
    save(fig, "combinaison_colonnes.png")


def three_cases() -> None:
    """x + y = 4 with x − y = 2 (one point), 2x + 2y = 6 (parallel), 3x + 3y = 12 (the same line)."""
    xs = np.linspace(-1, 5, 50)
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.6), sharey=True)
    cases = [("une solution", xs - 2, "x − y = 2", (3, 1)),
             ("aucune solution", 3 - xs, "2x + 2y = 6", None),
             ("une infinité", 4 - xs, "3x + 3y = 12", None)]
    for ax, (title, other, label, point) in zip(axes, cases):
        ax.plot(xs, 4 - xs, color=C[0], lw=3, label="x + y = 4")
        ax.plot(xs, other, color=C[3], lw=1.6, ls="--" if title == "une infinité" else "-", label=label)
        if point:
            ax.plot(*point, "o", color="black", ms=7)
            ax.text(point[0] + 0.2, point[1] - 0.6, "(3, 1)", fontsize=10)
        ax.set(title=title, xlim=(-1, 5), ylim=(-2, 5), xlabel="x")
        ax.axhline(0, color="gray", lw=0.6)
        ax.axvline(0, color="gray", lw=0.6)
        ax.legend(fontsize=8, loc="upper right")
        ax.grid(alpha=0.3)
    axes[0].set_ylabel("y")
    save(fig, "trois_cas.png")


def echelon() -> None:
    """The pattern of a reduced row echelon form: pivots 1, zeros above and below, free columns."""
    R = np.array([[1, "*", 0, 0, "*", "*"],
                  [0, 0, 1, 0, "*", "*"],
                  [0, 0, 0, 1, "*", "*"],
                  [0, 0, 0, 0, 0, 0]], dtype=object)
    pivots = {(0, 0), (1, 2), (2, 3)}
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            face = C[0] if (i, j) in pivots else ("#f2f2f2" if R[i, j] == 0 else "#ffe8b3")
            ax.add_patch(plt.Rectangle((j, -i), 1, -1, facecolor=face, edgecolor="white", lw=2))
            text = str(R[i, j])
            ax.text(j + 0.5, -i - 0.5, text, ha="center", va="center", fontsize=13,
                    color="white" if (i, j) in pivots else "black")
    ax.plot([0, 2, 2, 3, 3, 4, 4, 6], [-1, -1, -2, -2, -3, -3, -4, -4], color="black", lw=2)
    for j, name in enumerate(["base", "libre", "base", "base", "libre", "libre"]):
        ax.text(j + 0.5, 0.3, name, ha="center", fontsize=9, color=C[0] if name == "base" else "#b07d00")
    ax.set(xlim=(-0.2, 6.2), ylim=(-4.2, 0.8), aspect="equal",
           title="Forme échelonnée réduite : pivots égaux à 1, seuls dans leur colonne")
    ax.axis("off")
    save(fig, "echelonnee.png")


def main() -> int:
    print(f"Figures of M09a in {OUT.relative_to(ROOT)}:")
    columns()
    three_cases()
    echelon()
    return 0


if __name__ == "__main__":
    sys.exit(main())
