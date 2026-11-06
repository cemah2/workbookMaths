#!/usr/bin/env python
"""Draw the figures of the course sheet of chapter R0 (used by Claude).

    python tools/chapters/figures_r0.py

Writes small PNG files into chapitres/r0_prise_en_main/figures/. Every figure is computed and uses the workbook
style (wbm.plot colours, French decimal commas).
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

OUT = ROOT / "chapitres" / "r0_prise_en_main" / "figures"
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


def fig_first_plot() -> None:
    """The output of the plotting recipe of §6: g(x) = x³/4 − x on [−3, 3], with its title, labels and legend."""
    xs = np.linspace(-3, 3, 200)
    ys = xs ** 3 / 4 - xs
    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.plot(xs, ys, color=C[0], label="g(x) = x³/4 − x")
    ax.axhline(0, color=wbplot.TEXT_MUTED, lw=0.8)
    ax.axvline(0, color=wbplot.TEXT_MUTED, lw=0.8)
    ax.set_title("Un premier graphique")
    ax.set_xlabel("x")
    ax.set_ylabel("g(x)")
    ax.grid(True, color=wbplot.GRID)
    ax.legend()
    save(fig, "premier_graphique.png")


def fig_float_grid() -> None:
    """Why 0.1 + 0.2 != 0.3: the floats near 0.3 are a grid; 0.1 + 0.2 lands on the neighbour of the float 0.3."""
    import math
    base = 0.3
    spacing = math.ulp(base)
    grid = [base + k * spacing for k in range(-2, 4)]
    fig, ax = plt.subplots(figsize=(7, 1.9))
    ax.hlines(0, -2.6, 3.6, color=wbplot.TEXT_MUTED, lw=0.8)
    for k, value in zip(range(-2, 4), grid):
        ax.plot([k], [0], "o", color=C[0] if k not in (0, 1) else (C[1] if k == 0 else C[2]), ms=7)
    ax.annotate("le flottant le plus proche de 0,3\n(c'est lui que Python appelle 0.3)", xy=(0, 0), xytext=(-1.6, 0.62),
                arrowprops=dict(arrowstyle="->", color=wbplot.TEXT_MUTED), fontsize=9)
    ax.annotate("0.1 + 0.2 tombe ici :\n0.30000000000000004", xy=(1, 0), xytext=(1.5, 0.62),
                arrowprops=dict(arrowstyle="->", color=wbplot.TEXT_MUTED), fontsize=9)
    ax.text(0.5, -0.55, "écart entre deux flottants voisins près de 0,3 : environ 5,6 × 10⁻¹⁷", ha="center", fontsize=9,
            color=wbplot.TEXT_MUTED)
    ax.set_xlim(-2.8, 3.8)
    ax.set_ylim(-0.9, 1.25)
    ax.axis("off")
    ax.set_title("Les flottants forment une grille : la somme tombe sur le voisin", fontsize=10)
    save(fig, "grille_flottants.png")


def fig_r0_7_solution() -> None:
    """The figure expected in exercise R0.7 (05_solutions.md): f(x) = x² − 2x − 3 on [−2, 4], with its readings."""
    xs = np.linspace(-2, 4, 200)
    ys = xs ** 2 - 2 * xs - 3
    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.plot(xs, ys, color=C[0], label="f(x) = x² − 2x − 3")
    ax.axhline(0, color=wbplot.TEXT_MUTED, lw=0.8)
    ax.scatter([-1, 3], [0, 0], color=C[1], zorder=3, label="la courbe coupe l'axe : x = −1 et x = 3")
    ax.scatter([1], [-4], color=C[2], zorder=3, label="point le plus bas : (1 ; −4)")
    ax.set_title("La parabole de f")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True, color=wbplot.GRID)
    ax.legend(fontsize=8, loc="upper center")
    save(fig, "r0_7_parabole.png")


def main() -> int:
    print(f"Figures of R0 -> {OUT.relative_to(ROOT)}")
    fig_first_plot()
    fig_float_grid()
    fig_r0_7_solution()
    return 0


if __name__ == "__main__":
    sys.exit(main())
