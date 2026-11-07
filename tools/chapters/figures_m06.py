#!/usr/bin/env python
"""Draw the figures of chapter M06 (used by Claude).

    python tools/chapters/figures_m06.py

Writes small PNG files into chapitres/m06_information/figures/: three laws on five outcomes with their entropies,
the information diagram of two variables, Jensen's inequality for a concave and a convex function, the tree of a
prefix code with the Kraft shares of its words, and two clouds of points (a linear link, and a link that the
correlation misses). None comes from workbookIA 6 (no coin, no die, no letters, no weather, no Morse, no Huffman
tree, no curve of the surprise −log₂ p or of the entropy of a coin).
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m06_information" / "figures"
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


def entropy_bits(p) -> float:
    p = np.asarray(p, dtype=float)
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) + 0.0


def three_laws() -> None:
    """Three laws on five outcomes: uniform, uneven, certain, and their entropies in bits."""
    laws = [("uniforme", [0.2] * 5), ("inégale", [0.5, 0.2, 0.15, 0.1, 0.05]), ("certaine", [0, 0, 1, 0, 0])]
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.2), sharey=True)
    for ax, (name, p), color in zip(axes, laws, C):
        ax.bar(range(1, 6), p, color=color, width=0.6)
        ax.set(title=f"Loi {name} : H = {french_number(round(entropy_bits(p), 3))} bit(s)", xticks=range(1, 6),
               xlabel="issue", ylim=(0, 1.05))
        ax.grid(axis="y", alpha=0.3)
    axes[0].set_ylabel("probabilité")
    save(fig, "trois_lois.png")


def information_diagram() -> None:
    """Two overlapping discs: H(X) and H(Y); their common part is I(X ; Y), the rest H(X | Y) and H(Y | X)."""
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.add_patch(Circle((-0.75, 0), 1.35, color=C[0], alpha=0.35))
    ax.add_patch(Circle((0.75, 0), 1.35, color=C[1], alpha=0.35))
    ax.text(-1.35, 0, "H(X | Y)", ha="center", va="center", fontsize=12)
    ax.text(0, 0, "I(X ; Y)", ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(1.35, 0, "H(Y | X)", ha="center", va="center", fontsize=12)
    ax.text(-0.75, 1.55, "H(X)", ha="center", fontsize=12, color=C[0], fontweight="bold")
    ax.text(0.75, 1.55, "H(Y)", ha="center", fontsize=12, color=C[1], fontweight="bold")
    ax.annotate("", xy=(-2.1, -1.65), xytext=(2.1, -1.65), arrowprops=dict(arrowstyle="<->", color="0.3"))
    ax.text(0, -1.95, "H(X, Y) : toute la surface couverte", ha="center", fontsize=11, color="0.25")
    ax.set(xlim=(-2.6, 2.6), ylim=(-2.25, 2.0), aspect="equal")
    ax.axis("off")
    save(fig, "diagramme_information.png")


def jensen() -> None:
    """Jensen: for a concave f (√x), f(E[X]) ≥ E[f(X)]; for a convex f (x²), the opposite."""
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 3.9))
    xs = np.linspace(0, 10, 300)
    left.plot(xs, np.sqrt(xs), color=C[0], label="f(x) = √x (concave)")
    left.plot([1, 9], [1, 3], "o--", color="0.4", label="la corde entre (1, 1) et (9, 3)")
    left.plot(5, 2, "s", color=C[3], markersize=8, label="E[f(X)] = 2")
    left.plot(5, np.sqrt(5), "^", color=C[2], markersize=9, label="f(E[X]) = √5 ≈ 2,24")
    left.vlines(5, 0, np.sqrt(5), color="0.7", linestyles=":")
    left.set(xlabel="x", title="X vaut 1 ou 9 (une chance sur deux)", ylim=(0, 3.5))
    left.legend(fontsize=8, loc="lower right")
    left.grid(alpha=0.3)
    xs = np.linspace(-2, 4, 300)
    right.plot(xs, xs ** 2, color=C[1], label="f(x) = x² (convexe)")
    right.plot([-1, 3], [1, 9], "o--", color="0.4", label="la corde entre (−1, 1) et (3, 9)")
    right.plot(1, 5, "s", color=C[3], markersize=8, label="E[f(X)] = 5")
    right.plot(1, 1, "^", color=C[2], markersize=9, label="f(E[X]) = 1")
    right.vlines(1, 0, 5, color="0.7", linestyles=":")
    right.set(xlabel="x", title="X vaut −1 ou 3 (une chance sur deux)", ylim=(0, 16))
    right.legend(fontsize=8, loc="upper left")
    right.grid(alpha=0.3)
    save(fig, "jensen.png")


def code_tree() -> None:
    """The tree of the prefix code {00, 01, 10, 110, 111}: each word is a leaf, and owns 2^(−length) of the line."""
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(8, 5.6), gridspec_kw={"height_ratios": [3, 1]})
    nodes = {"": (0.0, 3.0), "0": (-2.0, 2.0), "1": (2.0, 2.0), "00": (-3.0, 1.0), "01": (-1.0, 1.0),
             "10": (1.0, 1.0), "11": (3.0, 1.0), "110": (2.4, 0.0), "111": (3.6, 0.0)}
    leaves = ["00", "01", "10", "110", "111"]
    for name, (x, y) in nodes.items():
        if name:
            px, py = nodes[name[:-1]]
            top.plot([px, x], [py, y], color="0.5", zorder=1)
            top.text((px + x) / 2 + (0.15 if name[-1] == "1" else -0.15), (py + y) / 2 + 0.08, name[-1],
                     ha="center", color="0.3", fontsize=10)
        leaf = name in leaves
        top.scatter([x], [y], s=520 if leaf else 140, color=C[0] if leaf else "0.75", zorder=2)
        if leaf:
            top.text(x, y, name, ha="center", va="center", color="white", fontsize=9, fontweight="bold", zorder=3)
    top.text(0, 3.32, "racine", ha="center", fontsize=9, color="0.3")
    top.set(xlim=(-3.8, 4.3), ylim=(-0.5, 3.6))
    top.axis("off")
    start = 0.0
    for k, word in enumerate(leaves):
        share = 2.0 ** (-len(word))
        bottom.barh(0, share, left=start, color=C[k % len(C)], edgecolor="white")
        bottom.text(start + share / 2, 0, f"{word}\n2^−{len(word)}", ha="center", va="center", fontsize=8,
                    color="white")
        start += share
    bottom.set(xlim=(0, 1), yticks=[], xlabel="les parts 2^(−longueur) des mots : leur somme, la somme de Kraft, vaut 1")
    save(fig, "arbre_code.png")


def mi_and_correlation() -> None:
    """A linear link (correlation near 1) and a link Y ≈ X² (correlation near 0): both are strong dependences."""
    rng = np.random.default_rng(6)
    x = rng.uniform(-2, 2, 400)
    y_lin = 1.5 * x + rng.normal(0, 0.4, x.size)
    y_sq = x ** 2 + rng.normal(0, 0.25, x.size)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 3.8))
    for ax, y, title, color in [(left, y_lin, "Y ≈ 1,5 X", C[0]), (right, y_sq, "Y ≈ X²", C[1])]:
        r = np.corrcoef(x, y)[0, 1]
        ax.scatter(x, y, s=8, alpha=0.6, color=color)
        ax.set(xlabel="X", ylabel="Y", title=f"{title} : corrélation {french_number(round(r, 2))}")
        ax.grid(alpha=0.3)
    save(fig, "information_correlation.png")


def main() -> int:
    print(f"Figures of M06 → {OUT}")
    three_laws()
    information_diagram()
    jensen()
    code_tree()
    mi_and_correlation()
    return 0


if __name__ == "__main__":
    sys.exit(main())
