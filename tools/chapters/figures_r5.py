#!/usr/bin/env python
"""Draw the figures of chapter R5 (used by Claude).

    python tools/chapters/figures_r5.py

Writes small PNG files into chapitres/r5_suites/figures/: an arithmetic and a geometric sequence, four geometric
sequences by their ratio, the limit of a sequence with its band of width ε, and a noisy series smoothed by a moving
average and an exponential moving average. Every figure is computed and uses the workbook style (wbm.plot colours,
French decimal commas). The numbers are those of the sheet's own examples: none comes from workbookIA 0B, from the
placement test or from an exercise of R5.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter, MaxNLocator  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "r5_suites" / "figures"
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


def fig_arith_geom() -> None:
    """§2 and §3: u(n) = 3 + 5n (points on a line) and v(n) = 2 × 1,5ⁿ (points on a curve that bends up)."""
    n = np.arange(0, 9)
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
    axes[0].plot(n, 3 + 5 * n, "o", color=C[0], markersize=7)
    axes[0].plot(n, 3 + 5 * n, "--", color=C[0], linewidth=0.8, alpha=0.6)
    axes[0].set_title("arithmétique : uₙ = 3 + 5n\n(+5 à chaque pas : des points alignés)", fontsize=10)
    axes[1].plot(n, 2 * 1.5**n, "o", color=C[1], markersize=7)
    axes[1].set_title("géométrique : vₙ = 2 × 1,5ⁿ\n(× 1,5 à chaque pas : la croissance s'accélère)", fontsize=10)
    for ax in axes:
        ax.set_xlabel("n")
        ax.grid(True, alpha=0.3)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    fig.tight_layout()
    save(fig, "arithmetique_geometrique.png")


def fig_geometric_ratios() -> None:
    """§3 and §5: qⁿ for q = 0,6 ; −0,7 ; 1 ; 1,3."""
    n = np.arange(0, 13)
    fig, axes = plt.subplots(1, 4, figsize=(13, 3.0), sharex=True)
    for ax, q, comment, colour in zip(axes, (0.6, -0.7, 1.0, 1.3),
                                      ("tend vers 0", "oscille et tend vers 0", "constante", "tend vers +∞"),
                                      (C[0], C[2], C[3], C[1])):
        ax.axhline(0, color="gray", linewidth=0.8)
        ax.plot(n, q**n, "o", color=colour, markersize=4)           # points only: a sequence lives on the integers
        ax.set_title(f"q = {french_number(q)} : {comment}", fontsize=10)
        ax.set_xlabel("n")
        ax.grid(True, alpha=0.3)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    axes[0].set_ylabel("qⁿ")
    fig.tight_layout()
    save(fig, "geometriques.png")


def fig_limit() -> None:
    """§5: uₙ = 10 − 9 × 0,6ⁿ tends to 10; from N = 6 on, every term stays within ε = 0,5 of 10."""
    n = np.arange(0, 15)
    u = 10 - 9 * 0.6**n
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.axhspan(9.5, 10.5, color=C[2], alpha=0.18, label="la bande ]9,5 ; 10,5[ (ε = 0,5)")
    ax.axhline(10, color=C[2], linewidth=1.2)
    inside = np.abs(u - 10) < 0.5
    ax.plot(n[~inside], u[~inside], "o", color=C[1], markersize=6, label="termes hors de la bande")
    ax.plot(n[inside], u[inside], "o", color=C[0], markersize=6, label="termes dans la bande (n ≥ 6)")
    ax.axvline(5.5, color="black", linestyle=":", linewidth=1)
    ax.text(5.7, 3.0, "N = 6", fontsize=10)
    ax.set_xlabel("n")
    ax.set_ylabel("uₙ")
    ax.set_ylim(0, 11.5)
    ax.set_title("uₙ tend vers 10 : à partir d'un certain rang, tous les termes sont dans la bande", fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8.5, loc="lower right")
    save(fig, "limite.png")


def fig_smoothing() -> None:
    """§6: a noisy series, its moving average over 5 values and its exponential moving average (β = 0,8)."""
    rng = np.random.default_rng(5)
    t = np.arange(1, 61)
    trend = 20 + 6 * np.sin(t / 9)
    x = trend + rng.normal(0, 2.2, size=t.size)
    window = 5
    moving = np.convolve(x, np.ones(window) / window, mode="valid")
    ema, v = [], 0.0
    for value in x:
        v = 0.8 * v + 0.2 * value
        ema.append(v)
    fig, ax = plt.subplots(figsize=(8, 3.8))
    ax.plot(t, x, "o", color="gray", markersize=3, alpha=0.7, label="série bruitée")
    ax.plot(t[window - 1:], moving, color=C[0], linewidth=2, label="moyenne mobile sur 5 valeurs")
    ax.plot(t, ema, color=C[1], linewidth=2, label="moyenne exponentielle, β = 0,8 (v₀ = 0)")
    ax.set_xlabel("t")
    ax.set_ylim(0, 32)
    ax.set_title("Deux lissages : la moyenne exponentielle part de 0, puis rattrape la série", fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8.5, loc="lower right")
    save(fig, "lissage.png")


def main() -> int:
    print(f"Figures of R5 -> {OUT.relative_to(ROOT)}")
    fig_arith_geom()
    fig_geometric_ratios()
    fig_limit()
    fig_smoothing()
    return 0


if __name__ == "__main__":
    sys.exit(main())
