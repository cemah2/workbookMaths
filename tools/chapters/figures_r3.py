#!/usr/bin/env python
"""Draw the figures of chapter R3 (used by Claude).

    python tools/chapters/figures_r3.py

Writes small PNG files into chapitres/r3_fonctions/figures/: the figures of the course sheet, and the graph read in
exercise R3.2 (a broken line through integer points, so that every reading is exact). Every figure is computed and
uses the workbook style (wbm.plot colours, French decimal commas). The numbers are those of the sheet's own examples:
none comes from workbookIA 0B, from the placement test or from another exercise of R3.
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

OUT = ROOT / "chapitres" / "r3_fonctions" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

EXERCISE_POINTS = [(-4, 1), (-2, 3), (1, -3), (3, -1), (5, 3)]   # the graph of f in R3.2


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


def axes_cross(ax) -> None:
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.axvline(0, color="gray", linewidth=0.8)
    ax.grid(True, alpha=0.3)


def fig_reading() -> None:
    """§2: f(x) = (x³ − 6x² + 9x)/2 − 1; the image of 4, the antecedents of 0."""
    xs = np.linspace(-0.5, 4.5, 300)
    f = (xs**3 - 6 * xs**2 + 9 * xs) / 2 - 1
    fig, ax = plt.subplots(figsize=(6.2, 4.0))
    ax.plot(xs, f, color=C[0], linewidth=2.2, label="courbe de f")
    ax.plot([4, 4], [0, 1], ":", color=C[1], linewidth=1.6)
    ax.plot([0, 4], [1, 1], ":", color=C[1], linewidth=1.6)
    ax.plot([4], [1], "o", color=C[1], markersize=7)
    ax.annotate("f(4) = 1 : on monte de 4 jusqu'à la courbe,\npuis on lit l'ordonnée", (4, 1), xytext=(1.55, 2.25),
                fontsize=8.5, color=C[1], arrowprops={"arrowstyle": "->", "color": C[1]})
    roots = np.sort(np.roots([0.5, -3, 4.5, -1]).real)
    ax.plot(roots, [0, 0, 0], "s", color=C[2], markersize=6)
    ax.annotate("les antécédents de 0 : là où la courbe\ncoupe la droite y = 0 (trois points)", (roots[1], 0),
                xytext=(1.2, -2.4), fontsize=8.5, color=C[2], arrowprops={"arrowstyle": "->", "color": C[2]})
    axes_cross(ax)
    ax.set_xlim(-0.6, 4.6)
    ax.set_ylim(-3, 3)
    ax.set_xlabel("x")
    ax.set_ylabel("y = f(x)")
    ax.set_title("Lire une image et des antécédents sur une courbe", fontsize=10)
    save(fig, "lecture_graphique.png")


def fig_affine() -> None:
    """§3: f(x) = −0,5x + 3 (through (−2 ; 4) and (2 ; 2)) and g(x) = 1,5x − 1, with their slope triangles."""
    xs = np.linspace(-3, 4, 50)
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    ax.plot(xs, -0.5 * xs + 3, color=C[0], linewidth=2.2, label="f(x) = −0,5x + 3 : pente −0,5")
    ax.plot(xs, 1.5 * xs - 1, color=C[1], linewidth=2.2, label="g(x) = 1,5x − 1 : pente 1,5")
    ax.plot([-2, 2], [4, 2], "o", color=C[0], markersize=6)
    ax.plot([-2, 2, 2], [4, 4, 2], "--", color=C[0], linewidth=1.2)
    ax.text(0, 4.25, "+4 en x", ha="center", fontsize=8.5, color=C[0])
    ax.text(2.15, 3, "−2 en y", fontsize=8.5, color=C[0])
    ax.plot([1, 2, 2], [0.5, 0.5, 2], "--", color=C[1], linewidth=1.2)
    ax.text(1.5, 0.05, "+1", ha="center", fontsize=8.5, color=C[1])
    ax.text(2.1, 1.1, "+1,5", fontsize=8.5, color=C[1])
    ax.plot([0, 0], [3, -1], "D", color="black", markersize=5)
    ax.annotate("ordonnées à l'origine :\nf(0) = 3 et g(0) = −1", (0, -1), xytext=(-2.9, -3.4), fontsize=8.5,
                arrowprops={"arrowstyle": "->", "color": "black"})
    axes_cross(ax)
    ax.set_xlim(-3, 4)
    ax.set_ylim(-4, 5.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(fontsize=8.5, loc="lower right")
    ax.set_title("La pente : de combien y change quand x augmente de 1", fontsize=10)
    save(fig, "affine.png")


def fig_reference() -> None:
    """§4: the four reference functions."""
    fig, axes = plt.subplots(1, 4, figsize=(12, 3.2))
    xs = np.linspace(-3, 3, 400)
    axes[0].plot(xs, xs**2, color=C[0], linewidth=2.2)
    axes[0].set_title("carré : x²", fontsize=10)
    axes[0].set_ylim(-1, 9)
    left, right = np.linspace(-3, -0.15, 200), np.linspace(0.15, 3, 200)
    axes[1].plot(left, 1 / left, color=C[1], linewidth=2.2)
    axes[1].plot(right, 1 / right, color=C[1], linewidth=2.2)
    axes[1].set_title("inverse : 1/x (x ≠ 0)", fontsize=10)
    axes[1].set_ylim(-6, 6)
    pos = np.linspace(0, 9, 400)
    axes[2].plot(pos, np.sqrt(pos), color=C[2], linewidth=2.2)
    axes[2].set_title("racine carrée : √x (x ≥ 0)", fontsize=10)
    axes[2].set_xlim(-1, 9)
    axes[2].set_ylim(-0.5, 3.5)
    axes[3].plot(xs, np.abs(xs), color=C[3], linewidth=2.2)
    axes[3].set_title("valeur absolue : |x|", fontsize=10)
    axes[3].set_ylim(-1, 3.5)
    for ax in axes:
        axes_cross(ax)
        ax.set_xlabel("x")
    fig.tight_layout()
    save(fig, "fonctions_reference.png")


def fig_piecewise() -> None:
    """§4: max(0, x), the step and |x|, three functions defined piece by piece."""
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.0))
    xs = np.linspace(-3, 3, 400)
    axes[0].plot(xs, np.maximum(0, xs), color=C[0], linewidth=2.2)
    axes[0].set_title("max(0, x) : 0 à gauche, x à droite", fontsize=9.5)
    axes[1].plot([-3, 0], [0, 0], color=C[1], linewidth=2.2)
    axes[1].plot([0, 3], [1, 1], color=C[1], linewidth=2.2)
    axes[1].plot([0], [1], "o", color=C[1], markersize=6)
    axes[1].plot([0], [0], "o", color=C[1], markersize=6, markerfacecolor="white")
    axes[1].set_title("la marche : 0 si x < 0, 1 si x ≥ 0", fontsize=9.5)
    axes[2].plot(xs, np.abs(xs), color=C[3], linewidth=2.2)
    axes[2].set_title("|x| : −x à gauche, x à droite", fontsize=9.5)
    for ax in axes:
        axes_cross(ax)
        ax.set_ylim(-0.6, 3.2)
        ax.set_xlabel("x")
    fig.tight_layout()
    save(fig, "par_morceaux.png")


def fig_parabolas() -> None:
    """§5: three parabolas with a positive, zero and negative discriminant, and their vertices."""
    xs = np.linspace(-4.5, 3.5, 400)
    cases = [((2, 4, -6), "2x² + 4x − 6 : Δ = 64 > 0, deux racines", C[0]),
             ((1, 4, 4), "x² + 4x + 4 : Δ = 0, une racine double", C[1]),
             ((1, -2, 3), "x² − 2x + 3 : Δ = −8 < 0, aucune racine", C[2])]
    fig, ax = plt.subplots(figsize=(6.6, 4.4))
    for (a, b, c), label, colour in cases:
        ax.plot(xs, a * xs**2 + b * xs + c, color=colour, linewidth=2.2, label=label)
        alpha = -b / (2 * a)
        ax.plot([alpha], [a * alpha**2 + b * alpha + c], "o", color=colour, markersize=7)
        delta = b * b - 4 * a * c
        if delta >= 0:
            roots = sorted({(-b - np.sqrt(delta)) / (2 * a), (-b + np.sqrt(delta)) / (2 * a)})
            ax.plot(roots, [0] * len(roots), "s", color=colour, markersize=6)
    ax.annotate("sommet (−1 ; −8)", (-1, -8), xytext=(0.2, -7.5), fontsize=8.5, color=C[0],
                arrowprops={"arrowstyle": "->", "color": C[0]})
    axes_cross(ax)
    ax.set_xlim(-4.5, 3.5)
    ax.set_ylim(-9, 10)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(fontsize=8, loc="upper center")
    ax.set_title("Le signe du discriminant : combien de fois la parabole coupe l'axe", fontsize=10)
    save(fig, "paraboles.png")


def fig_inverse() -> None:
    """§8: x ↦ x² on [0 ; +∞[ and its reciprocal √x, symmetric about the line y = x."""
    xs = np.linspace(0, 2.6, 200)
    ys = np.linspace(0, 6.8, 300)
    fig, ax = plt.subplots(figsize=(4.8, 4.6))
    ax.plot(xs, xs**2, color=C[0], linewidth=2.2, label="f(x) = x², x ≥ 0")
    ax.plot(ys, np.sqrt(ys), color=C[1], linewidth=2.2, label="sa réciproque : √x")
    ax.plot([0, 6.8], [0, 6.8], "--", color="gray", linewidth=1.2, label="la droite y = x")
    ax.plot([2, 4], [4, 2], "o:", color="black", markersize=6, linewidth=1)
    ax.annotate("(2 ; 4) et (4 ; 2) : symétriques\npar rapport à y = x", (4, 2), xytext=(2.4, 0.35), fontsize=8.5)
    axes_cross(ax)
    ax.set_xlim(-0.3, 6.8)
    ax.set_ylim(-0.3, 6.8)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(fontsize=8.5, loc="upper left")
    ax.set_title("Une fonction et sa réciproque", fontsize=10)
    save(fig, "reciproque.png")


def fig_exercise_graph() -> None:
    """R3.2: the graph of f on [−4 ; 5], a broken line through integer points."""
    xs, ys = zip(*EXERCISE_POINTS)
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    ax.plot(xs, ys, color=C[0], linewidth=2.4)
    ax.plot([xs[0], xs[-1]], [ys[0], ys[-1]], "o", color=C[0], markersize=6)
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.grid(True, alpha=0.5)
    ax.set_xlim(-5, 6)
    ax.set_ylim(-4, 4)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("La courbe de f, définie sur [−4 ; 5] (quadrillage d'unité 1)", fontsize=10)
    save(fig, "r3_2_graphique.png")


def main() -> int:
    print(f"Figures of R3 -> {OUT.relative_to(ROOT)}")
    fig_reading()
    fig_affine()
    fig_reference()
    fig_piecewise()
    fig_parabolas()
    fig_inverse()
    fig_exercise_graph()
    return 0


if __name__ == "__main__":
    sys.exit(main())
