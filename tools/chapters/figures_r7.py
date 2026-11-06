#!/usr/bin/env python
"""Draw the figures of chapter R7 (used by Claude).

    python tools/chapters/figures_r7.py

Writes small PNG files into chapitres/r7_limites_derivation/figures/: a rational function and its two asymptotes,
the bisection on x³ + x − 1, secants that turn into the tangent, a zoom on a curve and its tangent, and a function
with its derivative (variations and extremums). Every figure is computed and uses the workbook style (wbm.plot
colours, French decimal commas). The functions are those of the sheet's own examples: none comes from workbookIA 0B
or 5, from the placement test or from an exercise of R7.
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

OUT = ROOT / "chapitres" / "r7_limites_derivation" / "figures"
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


def axes_cross(ax) -> None:
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.axvline(0, color="gray", linewidth=0.8)
    ax.grid(True, alpha=0.3)


def fig_asymptotes() -> None:
    """§1: f(x) = (2x + 1)/(x − 3), with its vertical asymptote x = 3 and horizontal asymptote y = 2."""
    f = lambda x: (2 * x + 1) / (x - 3)  # noqa: E731
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    for lo, hi in ((-12, 2.9), (3.1, 16)):
        x = np.linspace(lo, hi, 400)
        ax.plot(x, f(x), color=C[0], linewidth=2, label="y = (2x + 1)/(x − 3)" if lo < 0 else None)
    ax.axvline(3, color=C[1], linestyle="--", linewidth=1.5, label="asymptote verticale x = 3")
    ax.axhline(2, color=C[2], linestyle="--", linewidth=1.5, label="asymptote horizontale y = 2")
    axes_cross(ax)
    ax.set_xlim(-12, 16)
    ax.set_ylim(-10, 14)
    ax.set_xlabel("x")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_title("Deux asymptotes : une limite infinie en 3, une limite finie en ±∞", fontsize=10)
    save(fig, "asymptotes.png")


def fig_bisection() -> None:
    """§2: four nested intervals of the bisection on x³ + x − 1, starting from [0 ; 1]."""
    f = lambda x: x**3 + x - 1  # noqa: E731
    x = np.linspace(-0.1, 1.1, 300)
    fig, ax = plt.subplots(figsize=(6.4, 4))
    ax.plot(x, f(x), color=C[0], linewidth=2, label="y = x³ + x − 1")
    axes_cross(ax)
    a, b = 0.0, 1.0
    for step in range(4):
        level = -1.25 - 0.2 * step
        ax.plot([a, b], [level, level], color=C[1], linewidth=3, solid_capstyle="butt")
        ax.text(b + 0.02, level, f"étape {step + 1}", va="center", fontsize=8)
        m = (a + b) / 2
        if f(m) < 0:
            a = m
        else:
            b = m
    root = 0.6823278
    ax.plot([root], [0], "o", color="black", markersize=5)
    ax.annotate("zéro ≈ 0,6823", (root, 0), textcoords="offset points", xytext=(-80, 12), fontsize=9)
    ax.set_xlim(-0.1, 1.25)
    ax.set_ylim(-2.0, 1.3)
    ax.set_xlabel("x")
    ax.legend(loc="upper left", fontsize=8)
    ax.set_title("Dichotomie : l'intervalle est coupé en deux à chaque étape", fontsize=10)
    save(fig, "dichotomie.png")


def fig_secants() -> None:
    """§3: secants of f(x) = x² − 2x between 3 and 3 + h (h = 1, 0,5, 0,2) and the tangent at 3 (slope 4)."""
    f = lambda x: x**2 - 2 * x  # noqa: E731
    x = np.linspace(1.5, 4.3, 300)
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.plot(x, f(x), color=C[0], linewidth=2, label="y = x² − 2x")
    for h, colour in ((1, C[1]), (0.5, C[2]), (0.2, C[3])):
        slope = (f(3 + h) - f(3)) / h
        ax.plot(x, f(3) + slope * (x - 3), color=colour, linewidth=1.2,
                label=f"sécante, h = {french_number(h)} : pente {french_number(round(slope, 2))}")
        ax.plot([3 + h], [f(3 + h)], "o", color=colour, markersize=4)
    ax.plot(x, 4 * x - 9, color="black", linewidth=1.8, linestyle="--", label="tangente : pente 4")
    ax.plot([3], [3], "o", color="black", markersize=5)
    ax.set_xlim(1.5, 4.3)
    ax.set_ylim(-2, 11)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel("x")
    ax.legend(loc="upper left", fontsize=8)
    ax.set_title("Les sécantes issues de (3 ; 3) pivotent vers la tangente", fontsize=10)
    save(fig, "secantes.png")


def fig_zoom() -> None:
    """§4: f(x) = x² − 2x and its tangent y = 4x − 9 at 3, on three windows of widths 2, 0,2 and 0,02."""
    f = lambda x: x**2 - 2 * x  # noqa: E731
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.4))
    for ax, width in zip(axes, (1, 0.1, 0.01)):
        x = np.linspace(3 - width, 3 + width, 200)
        ax.plot(x, f(x), color=C[0], linewidth=2, label="y = x² − 2x")
        ax.plot(x, 4 * x - 9, color="black", linewidth=1.2, linestyle="--", label="tangente")
        ax.plot([3], [3], "o", color="black", markersize=4)
        ax.set_title(f"x entre {french_number(round(3 - width, 3))} et {french_number(round(3 + width, 3))}",
                     fontsize=9)
        ax.grid(True, alpha=0.3)
    axes[0].legend(fontsize=8, loc="upper left")
    fig.suptitle("Trois fenêtres de plus en plus étroites autour de (3 ; 3) : la courbe finit par se confondre avec "
                 "sa tangente", fontsize=10)
    fig.tight_layout()
    save(fig, "zoom.png")


def fig_variations() -> None:
    """§8: f(x) = x³ − 6x² + 9x + 1 above, f′(x) = 3(x − 1)(x − 3) below: f′ vanishes and changes sign at 1 and 3."""
    x = np.linspace(-0.5, 4.5, 400)
    f = x**3 - 6 * x**2 + 9 * x + 1
    df = 3 * x**2 - 12 * x + 9
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(6.4, 5.4), sharex=True)
    top.plot(x, f, color=C[0], linewidth=2, label="f(x) = x³ − 6x² + 9x + 1")
    top.plot([1, 3], [5, 1], "o", color="black", markersize=5)
    top.annotate("maximum local (1 ; 5)", (1, 5), textcoords="offset points", xytext=(6, 6), fontsize=8)
    top.annotate("minimum local (3 ; 1)", (3, 1), textcoords="offset points", xytext=(6, -14), fontsize=8)
    bottom.plot(x, df, color=C[1], linewidth=2, label="f′(x) = 3(x − 1)(x − 3)")
    bottom.fill_between(x, df, 0, where=df > 0, color=C[2], alpha=0.15)
    bottom.fill_between(x, df, 0, where=df < 0, color=C[1], alpha=0.15)
    bottom.plot([1, 3], [0, 0], "o", color="black", markersize=5)
    for ax in (top, bottom):
        axes_cross(ax)
        ax.legend(loc="upper left", fontsize=8)
    bottom.set_xlabel("x")
    top.set_ylim(-3, 9)
    bottom.set_ylim(-5, 12)
    fig.suptitle("Chaque changement de signe de f′ (en bas) marque un extremum local de f (en haut)", fontsize=10)
    fig.tight_layout()
    save(fig, "variations_extremums.png")


def main() -> int:
    print(f"Figures of R7 -> {OUT.relative_to(ROOT)}")
    fig_asymptotes()
    fig_bisection()
    fig_secants()
    fig_zoom()
    fig_variations()
    return 0


if __name__ == "__main__":
    sys.exit(main())
