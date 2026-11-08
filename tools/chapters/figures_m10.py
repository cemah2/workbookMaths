#!/usr/bin/env python
"""Draw the figures of chapter M10 (used by Claude).

    python tools/chapters/figures_m10.py

Writes small PNG files into chapitres/m10_separabilite_convexite/figures/: convex and non-convex sets, the convex hulls
of the two clouds of the fiche, two separators with their margins, the bias trick in 3-D, a linear growth against a
growth in √k, and four activations applied to the same score over the plane. None comes from workbookIA 10 (no logic
gate, no neuron, no perceptron, no learning curve, no activation plotted against z with its derivative, no ball of
radius R with a margin γ).
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, Polygon, Wedge  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "solutions"))

from mymath_ref.convex import convex_hull_2d  # noqa: E402
from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m10_separabilite_convexite" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

A = np.array([[4, 3], [8, 3], [8, 7], [5, 7], [6, 3], [6, 5]], dtype=float)   # label +1
B = np.array([[-1, 0], [3, 0], [0, 4], [1, 2], [1, 0]], dtype=float)          # label -1


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        axes = (ax.xaxis, ax.yaxis, *([ax.zaxis] if ax.name == "3d" else []))
        for axis in axes:
            if axis.get_scale() == "linear":
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def clouds(ax, hulls=True):
    """The two clouds of the fiche, and their convex hulls."""
    for P, color, marker, label in ((A, C[0], "o", "A (+1)"), (B, C[1], "X", "B (−1)")):
        if hulls:
            H = convex_hull_2d(P)
            ax.add_patch(Polygon(H, closed=True, facecolor=color, alpha=0.15, edgecolor="none"))
            ring = np.vstack([H, H[:1]])
            ax.plot(ring[:, 0], ring[:, 1], color=color, linewidth=1.8)
        ax.scatter(P[:, 0], P[:, 1], s=55, color=color, marker=marker, zorder=3, label=label)
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)


def convex_sets():
    fig, axes = plt.subplots(1, 4, figsize=(12, 3.2))
    titles = ["un disque : convexe", "un polygone convexe", "un croissant : non convexe", "deux disques : non convexe"]
    for ax, title in zip(axes, titles):
        ax.set_xlim(-2.2, 2.2), ax.set_ylim(-2.2, 2.2), ax.set_aspect("equal"), ax.axis("off")
        ax.set_title(title, fontsize=10)
    axes[0].add_patch(Circle((0, 0), 1.6, color=C[0], alpha=0.3))
    axes[0].plot([-1.0, 0.9], [-0.9, 1.1], color="k", marker="o", markersize=4)
    axes[1].add_patch(Polygon([[-1.6, -1.2], [1.4, -1.5], [1.8, 0.6], [0.2, 1.7], [-1.5, 0.8]], color=C[0], alpha=0.3))
    axes[1].plot([-1.2, 1.3], [0.5, -1.0], color="k", marker="o", markersize=4)
    axes[2].add_patch(Wedge((0, 0), 1.8, 50, 310, width=0.8, color=C[1], alpha=0.3))
    axes[2].plot([0.6, 0.6], [1.45, -1.45], color="k", marker="o", markersize=4)
    axes[2].plot([0.6, 0.6], [0.9, -0.9], color=C[3], linewidth=3)
    axes[3].add_patch(Circle((-1.1, 0), 0.8, color=C[1], alpha=0.3))
    axes[3].add_patch(Circle((1.1, 0.3), 0.8, color=C[1], alpha=0.3))
    axes[3].plot([-1.1, 1.1], [0.0, 0.3], color="k", marker="o", markersize=4)
    axes[3].plot([-0.3, 0.3], [0.11, 0.19], color=C[3], linewidth=3)
    fig.text(0.5, -0.02, "En noir, un segment entre deux points de l'ensemble ; en orange, la partie qui en sort.",
             ha="center", fontsize=9)
    save(fig, "convexes.png")


def hulls():
    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    clouds(ax)
    ax.annotate("(6, 3) : au milieu d'un côté", (6, 3), (5.2, 1.0), fontsize=8, arrowprops={"arrowstyle": "->"})
    ax.annotate("(6, 5) : à l'intérieur", (6, 5), (6.3, 8.2), fontsize=8, arrowprops={"arrowstyle": "->"})
    ax.set_xlim(-2, 9.5), ax.set_ylim(-1.5, 9)
    ax.legend(loc="upper left", fontsize=8)
    ax.set_title("conv(A), un quadrilatère ; conv(B), un triangle", fontsize=10)
    save(fig, "enveloppes.png")


def margins():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    xs = np.linspace(-2, 9.5, 2)
    for ax, (w, b, gamma, title) in zip(axes, [((1, 1), -6, 1 / np.sqrt(2), "x₁ + x₂ = 6 : marge ≈ 0,71"),
                                             ((4, 3), -18.5, 1.3, "4x₁ + 3x₂ = 18,5 : marge 1,3, la plus grande")]):
        clouds(ax)
        w = np.array(w, dtype=float)
        norm = np.linalg.norm(w)
        for shift, style in ((0, "-"), (gamma * norm, "--"), (-gamma * norm, "--")):
            ax.plot(xs, (-b + shift - w[0] * xs) / w[1], color="k", linestyle=style, linewidth=1.4 if shift == 0 else 1)
        ax.set_xlim(-2, 9.5), ax.set_ylim(-1.5, 9)
        ax.set_title(title, fontsize=10)
    axes[1].plot([4, 1.92], [3, 1.44], color=C[3], linewidth=2.2, label="le plus court segment entre les enveloppes")
    axes[1].legend(loc="upper left", fontsize=8)
    axes[0].legend(loc="upper left", fontsize=8)
    save(fig, "marges.png")


def bias_trick():
    fig = plt.figure(figsize=(6.4, 5.2))
    ax = fig.add_subplot(projection="3d")
    for P, color, marker in ((A, C[0], "o"), (B, C[1], "X")):
        ax.scatter(np.ones(len(P)), P[:, 0], P[:, 1], color=color, marker=marker, s=40, depthshade=False)
    # the plane -6 x0 + x1 + x2 = 0, through the origin, and its trace at x0 = 1
    u, v = np.meshgrid(np.linspace(0, 1.25, 8), np.linspace(-1, 9, 8))
    ax.plot_surface(u, v, 6 * u - v, alpha=0.25, color=C[2])
    t = np.linspace(-1, 7, 2)
    ax.plot(np.ones(2), t, 6 - t, color="k", linewidth=2, label="la droite x₁ + x₂ = 6, au niveau x₀ = 1")
    yy, zz = np.meshgrid(np.linspace(-1.5, 9, 2), np.linspace(-1, 8, 2))
    ax.plot_surface(np.ones_like(yy), yy, zz, alpha=0.08, color="grey")
    ax.scatter([0], [0], [0], color="k", s=30)
    ax.text(0, 0, -1.4, "origine", fontsize=8)
    ax.set_xlabel("x₀ (toujours 1)"), ax.set_ylabel("x₁"), ax.set_zlabel("x₂")
    ax.set_zlim(-1, 8)
    ax.view_init(elev=18, azim=-62)
    ax.legend(loc="upper left", fontsize=8)
    ax.set_title("le plan −6x₀ + x₁ + x₂ = 0 passe par l'origine", fontsize=10)
    save(fig, "astuce_biais.png")


def growths():
    fig, ax = plt.subplots(figsize=(6, 3.8))
    k = np.linspace(0, 12, 300)
    ax.plot(k, 0.5 * k, color=C[0], linewidth=2, label="au moins 0,5 k (progression)")
    ax.plot(k, np.sqrt(4 + k), color=C[1], linewidth=2, label="au plus √(4 + k) (norme)")
    cross = 2 + np.sqrt(20)
    ax.axvline(cross, color="grey", linestyle=":")
    ax.annotate("croisement : k ≈ 6,5", (cross, 0.5 * cross), (7.5, 1.4), fontsize=8,
                arrowprops={"arrowstyle": "->"})
    ax.set_xlabel("nombre de pas k")
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(alpha=0.3)
    save(fig, "croissances.png")


def activations():
    w, b = np.array([4.0, 3.0]) / 6.5, -18.5 / 6.5
    g1, g2 = np.meshgrid(np.linspace(-2, 9.5, 300), np.linspace(-1.5, 9, 300))
    z = w[0] * g1 + w[1] * g2 + b
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.6), sharey=True)
    outputs = [("seuil H(z)", (z > 0).astype(float), (0, 1)),
               ("sigmoïde σ(z)", 1 / (1 + np.exp(-z)), (0, 1)),
               ("tanh(z)", np.tanh(z), (-1, 1)),
               ("ReLU(z)", np.maximum(0, z), (0, 5))]
    for ax, (title, out, (lo, hi)) in zip(axes, outputs):
        image = ax.imshow(out, origin="lower", extent=(-2, 9.5, -1.5, 9), cmap="viridis", vmin=lo, vmax=hi,
                          aspect="equal")
        ax.contour(g1, g2, z, levels=[-1, 0, 1], colors=["w", "w", "w"], linestyles=["--", "-", "--"],
                   linewidths=1)
        ax.scatter(A[:, 0], A[:, 1], s=14, color="w", marker="o")
        ax.scatter(B[:, 0], B[:, 1], s=14, color="w", marker="X")
        ax.set_title(title, fontsize=10)
        fig.colorbar(image, ax=ax, fraction=0.046, pad=0.03)
    fig.text(0.5, -0.03, "Le même score z = (4x₁ + 3x₂ − 18,5)/6,5 ; en blanc, les droites z = −1, z = 0 et z = 1.",
             ha="center", fontsize=9)
    save(fig, "activations.png")


def main() -> int:
    print(f"Figures of M10 → {OUT.relative_to(ROOT)}")
    convex_sets()
    hulls()
    margins()
    bias_trick()
    growths()
    activations()
    return 0


if __name__ == "__main__":
    sys.exit(main())
