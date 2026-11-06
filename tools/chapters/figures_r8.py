#!/usr/bin/env python
"""Draw the figures of chapter R8 (used by Claude).

    python tools/chapters/figures_r8.py

Writes small PNG files into chapitres/r8_probabilites/figures/: the wheel of 8 sectors with two events, a weighted
tree (rain, then a late bus), the law of the sum of two 4-sided dice, two laws with the same expectation and
different spreads, and running frequencies of 30 series on the wheel (law of large numbers). Every figure is computed and uses
the workbook style (wbm.plot colours, French decimal commas). The examples are those of the sheet: none comes from
workbookIA 0B, 2 or 3, from the placement test or from an exercise of R8.
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

OUT = ROOT / "chapitres" / "r8_probabilites" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and axis.get_visible():
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def fig_events() -> None:
    """§1: the wheel {1, ..., 8}, A = even numbers, B = at most 3; each sector coloured by the events it belongs to."""
    A, B = {2, 4, 6, 8}, {1, 2, 3}
    colours = {"A seulement": C[0], "B seulement": C[1], "A ∩ B (A et B)": C[2], "ni A ni B": "#d9d9d9"}

    def label(n: int) -> str:
        if n in A and n in B:
            return "A ∩ B (A et B)"
        if n in A:
            return "A seulement"
        if n in B:
            return "B seulement"
        return "ni A ni B"

    numbers = list(range(1, 9))
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    wedges, _ = ax.pie([1] * 8, colors=[colours[label(n)] for n in numbers], startangle=90, counterclock=False,
                       wedgeprops={"edgecolor": "white", "linewidth": 2})
    for wedge, n in zip(wedges, numbers):
        angle = np.deg2rad((wedge.theta1 + wedge.theta2) / 2)
        ax.text(0.68 * np.cos(angle), 0.68 * np.sin(angle), str(n), ha="center", va="center", fontsize=14,
                fontweight="bold", color="black")
    handles = [plt.Rectangle((0, 0), 1, 1, color=colour) for colour in colours.values()]
    ax.legend(handles, list(colours), loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=9)
    ax.set_title("A = « pair », B = « au plus 3 » : A ∪ B = {1, 2, 3, 4, 6, 8}", fontsize=10)
    ax.axis("equal")
    save(fig, "evenements.png")


def fig_tree() -> None:
    """§4: rain A (0,3), then a late bus B (0,4 if it rains, 0,1 otherwise), with the probability of each path."""
    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    ax.axis("off")
    root = (0.0, 0.5)
    rain, dry = "pluie $A$", r"pas de pluie $\bar{A}$"
    late, on_time = "retard $B$", r"à l'heure $\bar{B}$"
    first = {rain: (0.38, 0.8), dry: (0.38, 0.2)}
    second = {
        (rain, late): (1.0, 0.95, 0.4, "0,3 × 0,4 = 0,12"),
        (rain, on_time): (1.0, 0.65, 0.6, "0,3 × 0,6 = 0,18"),
        (dry, late): (1.0, 0.35, 0.1, "0,7 × 0,1 = 0,07"),
        (dry, on_time): (1.0, 0.05, 0.9, "0,7 × 0,9 = 0,63"),
    }

    def edge(start, end, text, colour="black"):
        ax.plot([start[0], end[0]], [start[1], end[1]], color=colour, linewidth=1.5)
        mx, my = start[0] + 0.55 * (end[0] - start[0]), start[1] + 0.55 * (end[1] - start[1])
        ax.text(mx, my + 0.03, text, ha="center", va="bottom", fontsize=10, color=colour,
                bbox={"boxstyle": "round,pad=0.15", "facecolor": "white", "edgecolor": "none"})

    ax.plot(*root, "o", color="black", markersize=6)
    for name, point in first.items():
        edge(root, point, "0,3" if name == rain else "0,7")
        ax.text(point[0] + 0.01, point[1], name, ha="left", va="center", fontsize=10,
                bbox={"boxstyle": "round,pad=0.25", "facecolor": "#f0f0f0", "edgecolor": "0.6"})
    for (parent, name), (x, y, p, path) in second.items():
        start = (first[parent][0] + (0.17 if parent == rain else 0.28), first[parent][1])
        is_late = name == late
        edge(start, (x, y), french_number(p), colour=C[1] if is_late else "black")
        ax.text(x + 0.01, y, name, ha="left", va="center", fontsize=10, color=C[1] if is_late else "black")
        ax.text(1.32, y, path, ha="left", va="center", fontsize=9, color=C[1] if is_late else "0.3")
    ax.text(1.32, 1.05, "probabilité du chemin", ha="left", fontsize=9, style="italic")
    ax.text(0.0, -0.08, "P(B) = 0,12 + 0,07 = 0,19 (les deux chemins en orange)", fontsize=10, color=C[1])
    ax.set_xlim(-0.05, 1.75)
    ax.set_ylim(-0.12, 1.08)
    save(fig, "arbre.png")


SUM_VALUES = np.arange(2, 9)
SUM_PROBS = np.array([1, 2, 3, 4, 3, 2, 1]) / 16


def fig_sum_law() -> None:
    """§6: the law of S, the sum of two 4-sided dice, as a bar chart, with its expectation 5."""
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    ax.bar(SUM_VALUES, SUM_PROBS, width=0.15, color=C[0])
    for x, p in zip(SUM_VALUES, SUM_PROBS):
        ax.text(x, p + 0.008, f"{int(round(p * 16))}/16", ha="center", fontsize=9)
    ax.axvline(5, color=C[1], linestyle="--", linewidth=1.5, label="espérance E[S] = 5")
    ax.set_xticks(SUM_VALUES)
    ax.set_xlabel("valeur x de la somme S")
    ax.set_ylabel("P(S = x)")
    ax.set_ylim(0, 0.31)
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(loc="upper right", fontsize=9)
    ax.set_title("Loi de la somme de deux dés à 4 faces (16 couples équiprobables)", fontsize=10)
    save(fig, "loi_somme.png")


def fig_spread() -> None:
    """§7: two laws with expectation 5: S (σ ≈ 1,58) and T, which is 1, 5 or 9 with probabilities 1/4, 1/2, 1/4."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.4), sharey=True)
    laws = [(SUM_VALUES, SUM_PROBS, "S : somme de deux dés à 4 faces", np.sqrt(2.5)),
            (np.array([1, 5, 9]), np.array([0.25, 0.5, 0.25]), "T : 1, 5 ou 9, avec 1/4, 1/2, 1/4", np.sqrt(8))]
    for ax, (values, probs, title, sigma), colour in zip(axes, laws, (C[0], C[2])):
        ax.bar(values, probs, width=0.15, color=colour)
        ax.axvline(5, color=C[1], linestyle="--", linewidth=1.5, label="espérance 5")
        ax.axvspan(5 - sigma, 5 + sigma, color=C[1], alpha=0.12,
                   label=f"espérance ± écart-type ({french_number(round(sigma, 2))})")
        ax.set_xticks(range(1, 10))
        ax.set_xlim(0.5, 9.5)
        ax.set_title(title, fontsize=10)
        ax.set_xlabel("valeur")
        ax.grid(True, axis="y", alpha=0.3)
        ax.legend(loc="upper left", fontsize=8)
    axes[0].set_ylabel("probabilité")
    axes[0].set_ylim(0, 0.65)
    fig.suptitle("Même espérance, dispersions différentes : V(S) = 2,5 et V(T) = 8", fontsize=10)
    fig.tight_layout()
    save(fig, "dispersion.png")


def fig_fluctuations() -> None:
    """§8: running frequency of « even or at most 3 » on the wheel, for 30 series; the fan narrows around 3/4."""
    fig, ax = plt.subplots(figsize=(7, 3.8))
    n, series = 10_000, 30
    k = np.arange(1, n + 1)
    rng = np.random.default_rng(31)
    spins = rng.integers(1, 9, size=(series, n))
    hits = (spins % 2 == 0) | (spins <= 3)
    running = np.cumsum(hits, axis=1) / k
    for row in running:
        ax.plot(k, row, color=C[0], linewidth=0.7, alpha=0.45)
    ax.plot(k, 0.75 + 1.3 / np.sqrt(k), color=C[1], linewidth=1.2, linestyle=":", label="3/4 ± 1,3/√n (une enveloppe en 1/√n)")
    ax.plot(k, 0.75 - 1.3 / np.sqrt(k), color=C[1], linewidth=1.2, linestyle=":")
    ax.axhline(0.75, color="black", linestyle="--", linewidth=1.2, label="probabilité 3/4")
    ax.set_xscale("log")
    ax.set_xlabel("nombre de tours n (échelle logarithmique)")
    ax.set_ylabel("fréquence de « pair ou au plus 3 »")
    ax.set_xlim(10, n)
    ax.set_ylim(0.4, 1.02)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower right", fontsize=8)
    ax.set_title("30 séries de tours : les fréquences se resserrent autour de la probabilité", fontsize=10)
    save(fig, "fluctuations.png")


def main() -> int:
    print(f"Figures of R8 -> {OUT.relative_to(ROOT)}")
    fig_events()
    fig_tree()
    fig_sum_law()
    fig_spread()
    fig_fluctuations()
    return 0


if __name__ == "__main__":
    sys.exit(main())
