#!/usr/bin/env python
"""Draw the figures of chapter M11 (used by Claude).

    python tools/chapters/figures_m11.py

Writes small PNG files into chapitres/m11_logique_concentration/figures/: two Venn diagrams with two sets (an
inclusion, and a counterexample), the tail of an exponential law against the bounds of Markov and Chebyshev, the 95 %
radius of a mean against n (Chebyshev, Hoeffding, the normal approximation), the upper confidence bounds of three
options, and the expected regret of a fixed ε-greedy against the logarithmic bound of UCB1. None comes from workbookIA
11 (no syllogism with three circles, no Thompson posteriors of its fiche, no agent, no simulated learning curve).
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Ellipse  # noqa: E402
from matplotlib.ticker import FuncFormatter, ScalarFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m11_logique_concentration" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and isinstance(axis.get_major_formatter(), ScalarFormatter):
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def venn():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.4))
    for ax in axes:
        ax.add_patch(Ellipse((0, 0), 6.4, 4.2, facecolor=C[1], alpha=0.18, edgecolor=C[1], linewidth=2))
        ax.text(-2.6, 1.7, "B", fontsize=13, color=C[1], weight="bold")
        ax.set_xlim(-3.8, 3.8)
        ax.set_ylim(-2.6, 2.6)
        ax.set_aspect("equal")
        ax.axis("off")
    axes[0].add_patch(Ellipse((0.4, -0.1), 2.8, 2.0, facecolor=C[0], alpha=0.3, edgecolor=C[0], linewidth=2))
    axes[0].text(-0.3, 0.45, "A", fontsize=13, color=C[0], weight="bold")
    axes[0].set_title("(a) A ⊂ B : la région « A hors de B » est vide", fontsize=10)
    axes[1].add_patch(Ellipse((2.2, -0.2), 3.2, 2.0, facecolor=C[0], alpha=0.3, edgecolor=C[0], linewidth=2))
    axes[1].text(1.2, 0.4, "A", fontsize=13, color=C[0], weight="bold")
    axes[1].scatter([3.35], [-0.35], s=70, color=C[3], edgecolor="black", zorder=5)
    axes[1].annotate("un élément de A \\ B :\nun contre-exemple", (3.35, -0.35), (0.3, -2.25), fontsize=8,
                     ha="center", arrowprops={"arrowstyle": "->"})
    axes[1].set_title("(b) A ⊄ B : « tout élément de A est dans B » est faux", fontsize=10)
    save(fig, "venn.png")


def tails():
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    a = np.linspace(2.2, 20, 400)
    mean, var = 2.0, 4.0
    ax.semilogy(a, np.exp(-a / mean), color="black", linewidth=2.2, label="vraie queue P(X ≥ a) = e^(−a/2)")
    ax.semilogy(a, np.minimum(1, mean / a), color=C[0], linewidth=2, label="Markov : 2 / a")
    ax.semilogy(a, np.minimum(1, var / (a - mean) ** 2), color=C[1], linewidth=2,
                label="Tchebychev : 4 / (a − 2)²")
    ax.scatter([6], [math.exp(-3)], color="black", zorder=5)
    ax.annotate("a = 6 : 0,050 contre 0,33 (Markov)", (6, math.exp(-3)), (8.5, 0.15), fontsize=8,
                arrowprops={"arrowstyle": "->"})
    ax.set_xlabel("seuil a")
    ax.set_ylabel("probabilité (échelle log)")
    ax.set_title("Loi exponentielle de moyenne 2 (variance 4)", fontsize=10)
    ax.legend(loc="lower left", fontsize=8)
    ax.grid(alpha=0.3, which="both")
    save(fig, "queues.png")


def radii():
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    n = np.logspace(1, 4, 300)
    delta = 0.05
    ax.loglog(n, np.sqrt(0.25 / (delta * n)), color=C[0], linewidth=2, label="Tchebychev (variance ≤ 1/4)")
    ax.loglog(n, np.sqrt(math.log(2 / delta) / (2 * n)), color=C[1], linewidth=2, label="Hoeffding")
    ax.loglog(n, 1.96 * 0.5 / np.sqrt(n), color=C[2], linewidth=2, linestyle="--",
              label="approximation normale (TCL, p = 1/2)")
    ax.axhline(0.04, color="gray", linewidth=1, linestyle=":")
    ax.text(12, 0.043, "rayon 0,04", fontsize=8, color="gray")
    for value, color in ((601, C[2]), (1153, C[1]), (3125, C[0])):
        ax.scatter([value], [0.04], color=color, zorder=5)
    ax.annotate("601, 1 153 et 3 125 exemples", (1153, 0.04), (60, 0.012), fontsize=8,
                arrowprops={"arrowstyle": "->"})
    ax.set_xlabel("nombre de variables n (échelle log)")
    ax.set_ylabel("rayon à 95 % (échelle log)")
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(alpha=0.3, which="both")
    save(fig, "rayons.png")


def ucb():
    t, means, counts = 480, np.array([0.62, 0.55, 0.40]), np.array([400, 56, 24])
    bonus = np.sqrt(2 * math.log(t) / counts)
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    x = np.arange(3)
    for i in range(3):
        ax.plot([x[i], x[i]], [means[i], means[i] + bonus[i]], color=C[i], linewidth=3)
        ax.scatter([x[i]], [means[i]], color=C[i], s=60, zorder=5)
        ax.scatter([x[i]], [means[i] + bonus[i]], color=C[i], marker="v", s=70, zorder=5)
        ax.text(x[i] + 0.08, means[i] + bonus[i], f"{means[i] + bonus[i]:.2f}".replace(".", ","), fontsize=9,
                va="center")
        ax.text(x[i] + 0.08, means[i], f"μ̂ = {means[i]:.2f}".replace(".", ",") + f" (N = {counts[i]})", fontsize=8,
                va="center")
    ax.axhline(1.0, color="gray", linewidth=1, linestyle=":")
    ax.text(-0.45, 1.02, "récompenses dans [0 ; 1]", fontsize=8, color="gray")
    ax.set_xticks(x, ["option 1", "option 2", "option 3"])
    ax.set_xlim(-0.5, 2.9)
    ax.set_ylim(0.3, 1.3)
    ax.set_ylabel("moyenne observée et borne supérieure")
    ax.set_title("Au pas t = 480, bonus √(2 ln t / N) : UCB1 choisit l'option 3", fontsize=10)
    ax.grid(alpha=0.3, axis="y")
    save(fig, "ucb.png")


def regrets():
    gaps = np.array([0.2, 0.4])           # two suboptimal options among K = 3
    K, eps = 3, 0.1
    T = np.linspace(1, 100_000, 800)
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    ax.plot(T, eps / K * gaps.sum() * T, color=C[0], linewidth=2,
            label="ε-greedy, ε = 0,1 : au moins (ε/K) Σ Δₖ × T")
    ax.plot(T, sum(8 * np.log(T) / g for g in gaps), color=C[1], linewidth=2,
            label="UCB1 : environ Σ 8 ln T / Δₖ")
    ax.set_xlabel("nombre de pas T")
    ax.set_ylabel("regret attendu")
    ax.set_title("Trois options, écarts 0 ; 0,2 ; 0,4", fontsize=10)
    cross = 31_000
    ax.annotate("vers T ≈ 31 000, la droite passe au-dessus", (cross, 0.02 * cross), (45_000, 300), fontsize=8,
                arrowprops={"arrowstyle": "->"})
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(alpha=0.3)
    save(fig, "regrets.png")


def main() -> int:
    print(f"Figures of M11 → {OUT.relative_to(ROOT)}")
    venn()
    tails()
    radii()
    ucb()
    regrets()
    return 0


if __name__ == "__main__":
    sys.exit(main())
