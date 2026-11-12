#!/usr/bin/env python
"""Draw the figures of chapter M16 (used by Claude).

    python tools/chapters/figures_m16.py

Writes small PNG files into chapitres/m16_couches_affines/figures/: a figure of the plane and its images by a shear
followed by a translation, then by a homothety followed by a translation, composed in homogeneous coordinates; two
directed graphs (four villages with a cycle, and a water network without cycle, with its fractions) and their
adjacency matrices; the second moment of a quantity multiplied by a random gain at each stage (γ = 1,2, 1 and 0,85),
in log scale, and the variance of a chain of noisy amplifiers that settles at s²/(1 − g²). The numbers are those of the
fiche; none comes from workbookIA 16 (no layer, no network, no 16xx seed, no gain 1,25, 0,8, 1,5 or 0,5).
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Polygon  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m16_couches_affines" / "figures"
C = wbplot.CATEGORICAL
DPI = 110
SEED = 4901

H1 = np.array([[1.0, 0.0, 0.0], [2.0, 1.0, 0.0], [0.0, 1.0, 1.0]])     # §2: shear (x, y) ↦ (x + 2y, y), then + (0, 1)
H2 = np.array([[3.0, 0.0, 0.0], [0.0, 3.0, 0.0], [-1.0, 0.0, 1.0]])    # §2: homothety of ratio 3, then + (−1, 0)
GAMMAS = (1.2, 1.0, 0.85)                                              # §7: E[G²] of the random gains
STAGES = 25
G_NOISY, S2_NOISY = 0.7, 1.0                                           # §7: Z_{k+1} = 0,7 Z_k + N_k, V(N_k) = 1


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


def homogeneous() -> None:
    """§2: an L-shaped figure, its image by f1 (H1), then by f2 ∘ f1 (H1 @ H2)."""
    shape = np.array([[0, 0], [1, 0], [1, 1], [0.5, 1.6], [0, 1]], dtype=float)          # a small house
    rows = np.hstack([shape, np.ones((len(shape), 1))])
    images = [(shape, "la figure", C[0]), ((rows @ H1)[:, :2], "image par f₁", C[1]),
              ((rows @ H1 @ H2)[:, :2], "image par f₂ ∘ f₁ : [x, 1] H₁ H₂", C[2])]
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    for points, label, color in images:
        ax.add_patch(Polygon(points, closed=True, facecolor=color, alpha=0.35, edgecolor=color, lw=2, label=label))
        ax.plot(*points[0], "o", color=color, ms=5)
    ax.plot([1, 3, 8], [1, 2, 6], "o:", color="0.3", lw=1, ms=4)
    ax.annotate("(1, 1) ↦ (3, 2) ↦ (8, 6)", xy=(8, 6), xytext=(6.6, 2.2), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="0.3"))
    ax.set(xlim=(-1.5, 10.5), ylim=(-0.5, 8.5), aspect="equal", xlabel="x", ylabel="y",
           title="Composer deux applications affines : multiplier leurs matrices homogènes")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9, loc="upper left")
    save(fig, "coordonnees_homogenes.png")


def _draw_graph(ax, positions, edges, labels, weights=None, color=C[0]):
    for (i, j) in edges:
        start, end = np.array(positions[i]), np.array(positions[j])
        arrow = FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=16, color=color, lw=1.6,
                                shrinkA=17, shrinkB=17, connectionstyle="arc3,rad=0.12")
        ax.add_patch(arrow)
        if weights is not None:
            mid = (start + end) / 2 + 0.11 * np.array([-(end - start)[1], (end - start)[0]])
            ax.text(*mid, french_number(weights[(i, j)]), fontsize=9, ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))
    for k, (x, y) in positions.items():
        ax.plot(x, y, "o", ms=26, color="white", markeredgecolor="0.25", markeredgewidth=1.5, zorder=3)
        ax.text(x, y, labels[k], ha="center", va="center", fontsize=10, zorder=4)
    ax.set_aspect("equal")
    ax.axis("off")


def graphs() -> None:
    """§3 and §4: four villages with a cycle; a water network without cycle, with the fractions on its edges."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
    villages = {0: (0, 1), 1: (1.5, 2), 2: (1.5, 0), 3: (3, 1)}
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 0)]
    _draw_graph(axes[0], villages, edges, {0: "V₁", 1: "V₂", 2: "V₃", 3: "V₄"})
    axes[0].set_title("Quatre villages : six lignes de navette à sens unique\n(un cycle V₁ → V₂ → V₄ → V₁)",
                      fontsize=10)
    axes[0].set(xlim=(-0.5, 3.5), ylim=(-0.5, 2.5))
    water = {0: (0, 1), 1: (1.5, 2), 2: (1.5, 0), 3: (3, 1)}
    flows = {(0, 1): 0.6, (0, 2): 0.4, (1, 2): 0.5, (1, 3): 0.5, (2, 3): 0.8}
    _draw_graph(axes[1], water, list(flows), {0: "S", 1: "a", 2: "b", 3: "R"}, weights=flows, color=C[1])
    axes[1].set_title("Un réseau d'eau sans cycle : la part de l'eau qui passe\nde la source S au réservoir R vaut 0,86",
                      fontsize=10)
    axes[1].set(xlim=(-0.5, 3.5), ylim=(-0.5, 2.5))
    save(fig, "graphes.png")


def stages() -> None:
    """§7: E[Z_k²] when a random gain of second moment γ multiplies Z at each stage; a chain of noisy amplifiers."""
    rng = np.random.default_rng(SEED)
    k = np.arange(STAGES + 1)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.0))
    for gamma, color in zip(GAMMAS, C):
        axes[0].plot(k, gamma ** k, color=color, lw=2, label=f"γ = {french_number(gamma)} : γᵏ")
        signs = rng.choice([-1.0, 1.0], size=(20000, STAGES))
        spread = 1 + 0.3 * rng.uniform(-1, 1, size=(20000, STAGES))            # E[spread] = 1
        gains = signs * np.sqrt(gamma * spread)                                  # E[G²] = γ, independent gains
        z = np.cumprod(np.hstack([np.ones((20000, 1)), gains]), axis=1)         # Z_0 = 1
        axes[0].plot(k[::3], np.mean(z ** 2, axis=0)[::3], "o", color=color, ms=4)
    axes[0].set_yscale("log")
    axes[0].set(xlabel="étage k", ylabel="E[Zₖ²] (échelle log)",
                title="Un gain aléatoire par étage : E[Zₖ²] = γᵏ\n(courbes : la formule ; points : 20 000 simulations)")
    axes[0].legend(fontsize=9)
    v = [0.0]
    for _ in range(STAGES):
        v.append(G_NOISY ** 2 * v[-1] + S2_NOISY)
    limit = S2_NOISY / (1 - G_NOISY ** 2)
    axes[1].plot(k, v, "o-", color=C[0], ms=4, lw=1.5, label="vₖ₊₁ = 0,49 vₖ + 1, v₀ = 0")
    axes[1].axhline(limit, color=C[1], ls="--", lw=1.5, label=f"limite s²/(1 − g²) ≈ {french_number(round(limit, 3))}")
    axes[1].set(xlabel="étage k", ylabel="variance du bruit", ylim=(0, 2.3),
                title="Des amplificateurs bruités de gain 0,7 :\nla variance se stabilise")
    axes[1].legend(fontsize=9, loc="lower right")
    save(fig, "variances_etages.png")


def main() -> int:
    print(f"Figures of M16 into {OUT.relative_to(ROOT)}:")
    homogeneous()
    graphs()
    stages()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
