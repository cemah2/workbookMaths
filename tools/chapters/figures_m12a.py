#!/usr/bin/env python
"""Draw the figures of chapter M12a (used by Claude).

    python tools/chapters/figures_m12a.py

Writes small PNG files into chapitres/m12a_espaces_vectoriels/figures/: the span of one vector and of two vectors
(a line, then the whole plane), the coordinates of v = (0, 6) in the basis b₁ = (1, 2), b₂ = (−1, 1) of the fiche,
the kernel and the image of a rank-1 map of the plane, and the unit square moved by the affine map of the fiche and
brought back by its inverse. None comes from workbookIA 12 or 17 (no cloud of points, no scaler, no network).
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Polygon  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m12a_espaces_vectoriels" / "figures"
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


def arrow(ax, start, vector, color, label, offset=(0.1, 0.1), lw=2.2):
    ax.annotate("", xy=(start[0] + vector[0], start[1] + vector[1]), xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": lw, "mutation_scale": 14})
    if label:
        mid = (start[0] + vector[0] / 2 + offset[0], start[1] + vector[1] / 2 + offset[1])
        ax.text(*mid, label, color=color, fontsize=11)


def axes_frame(ax, lim):
    ax.axhline(0, color="0.6", lw=0.8)
    ax.axvline(0, color="0.6", lw=0.8)
    ax.set(xlim=(-lim, lim), ylim=(-lim, lim), aspect="equal")


def span() -> None:
    """Left: the combinations of u = (3, 1) fill a line. Right: those of u and w = (1, 2) fill the plane."""
    u, w = np.array([3.0, 1.0]), np.array([1.0, 2.0])
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8))
    ax = axes[0]
    axes_frame(ax, 6)
    t = np.linspace(-3, 3, 2)
    ax.plot(t * u[0], t * u[1], color=C[0], lw=2, alpha=0.5)
    for k, name in ((-1, "−u"), (1.5, "1,5u")):
        ax.plot(k * u[0], k * u[1], "o", color=C[0], ms=5)
        ax.text(k * u[0] + 0.15, k * u[1] - 0.6, name, color=C[0], fontsize=10)
    arrow(ax, (0, 0), u, C[0], "u", (-0.3, 0.3))
    ax.set_title("Vect(u) : une droite par l'origine")
    ax = axes[1]
    axes_frame(ax, 6)
    for a in range(-4, 5):
        p, q = a * u - 4 * w, a * u + 4 * w
        ax.plot([p[0], q[0]], [p[1], q[1]], color=C[1], lw=0.7, alpha=0.5)
        p, q = -4 * u + a * w, 4 * u + a * w
        ax.plot([p[0], q[0]], [p[1], q[1]], color=C[0], lw=0.7, alpha=0.5)
    target = 1 * u + 1.5 * w
    arrow(ax, (0, 0), u, C[0], "u", (0.05, -0.55))
    arrow(ax, (0, 0), w, C[1], "w", (-0.55, 0.05))
    arrow(ax, u, 1.5 * w, C[1], "1,5 w", (0.15, -0.2), lw=1.5)
    ax.plot(*target, "o", color="black", ms=6)
    ax.text(target[0] - 1.2, target[1] + 0.35, "u + 1,5 w", fontsize=10)
    ax.set_title("Vect(u, w) : tout le plan")
    save(fig, "vect.png")


def coordinates() -> None:
    """The grid of the basis b1 = (1, 2), b2 = (−1, 1): v = (0, 6) = 2 b1 + 2 b2, coordinates (2, 2)."""
    b1, b2 = np.array([1.0, 2.0]), np.array([-1.0, 1.0])
    v = 2 * b1 + 2 * b2
    fig, ax = plt.subplots(figsize=(5.6, 5.6))
    axes_frame(ax, 7)
    for a in range(-5, 6):
        p, q = a * b1 - 6 * b2, a * b1 + 6 * b2
        ax.plot([p[0], q[0]], [p[1], q[1]], color="0.82", lw=0.8)
        p, q = -6 * b1 + a * b2, 6 * b1 + a * b2
        ax.plot([p[0], q[0]], [p[1], q[1]], color="0.82", lw=0.8)
    arrow(ax, (0, 0), 2 * b1, C[0], "2 b₁", (0.2, -0.3))
    arrow(ax, 2 * b1, 2 * b2, C[1], "2 b₂", (0.15, 0.1))
    arrow(ax, (0, 0), b1, C[0], "", lw=3)
    arrow(ax, (0, 0), b2, C[1], "", lw=3)
    ax.text(0.95, 0.45, "b₁", color=C[0], fontsize=11)
    ax.text(-1.25, 0.25, "b₂", color=C[1], fontsize=11)
    ax.annotate("", xy=v, xytext=(0, 0), arrowprops={"arrowstyle": "-|>", "color": "black", "lw": 2,
                                                     "mutation_scale": 16, "ls": "--"})
    ax.text(v[0] + 0.25, v[1] - 0.1, "v = (0, 6)", fontsize=11)
    ax.set_title("Dans la base (b₁, b₂), v a pour coordonnées (2, 2)")
    save(fig, "coordonnees.png")


def kernel_image() -> None:
    """The rank-1 map x ↦ M x, M = [[2, −1], [−2, 1]]: each line parallel to the kernel goes to one point of the image."""
    M = np.array([[2.0, -1.0], [-2.0, 1.0]])
    k = np.array([1.0, 2.0])              # M k = 0
    c = M[:, 0] / 2                        # the image is the line spanned by (1, −1)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.9))
    ax = axes[0]
    axes_frame(ax, 4)
    t = np.linspace(-1.9, 1.9, 2)
    ax.plot(t * k[0], t * k[1], color=C[3], lw=2.5, label="noyau : Vect((1, 2))")
    starts = [np.array([1.0, 0.0]), np.array([1.5, 0.0]), np.array([-1.0, 0.0])]
    for i, p in enumerate(starts):
        line = p + np.outer(np.linspace(-1.6, 1.6, 2), k)
        ax.plot(line[:, 0], line[:, 1], color=C[i], lw=1.5, ls="--")
        ax.plot(*p, "o", color=C[i], ms=6)
    ax.set_title("Départ : des droites parallèles au noyau")
    ax.legend(loc="lower right", fontsize=9)
    ax = axes[1]
    axes_frame(ax, 4)
    t = np.linspace(-3.5, 3.5, 2)
    ax.plot(t * c[0], t * c[1], color=C[4], lw=2.5, label="image : Vect((1, −1))")
    ax.plot(0, 0, "s", color=C[3], ms=8, label="image du noyau : 0")
    for i, (p, name) in enumerate(zip(starts, ["M(1, 0)", "M(1,5 ; 0)", "M(−1, 0)"])):
        q = M @ p
        ax.plot(*q, "o", color=C[i], ms=8)
        ax.text(q[0] + 0.2, q[1] + 0.15, name, color=C[i], fontsize=9)
    ax.set_title("Arrivée : chaque droite devient un point")
    ax.legend(loc="lower left", fontsize=9)
    save(fig, "noyau_image.png")


def affine() -> None:
    """The unit square and its image by φ(x) = A x + b, A = [[2, 1], [1, 1]], b = (1, −2); φ⁻¹ brings it back."""
    A, b = np.array([[2.0, 1.0], [1.0, 1.0]]), np.array([1.0, -2.0])
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)
    image = square @ A.T + b
    fig, ax = plt.subplots(figsize=(6.4, 5.2))
    ax.axhline(0, color="0.6", lw=0.8)
    ax.axvline(0, color="0.6", lw=0.8)
    ax.add_patch(Polygon(square, closed=True, facecolor=C[0], alpha=0.35, edgecolor=C[0], lw=1.5))
    ax.add_patch(Polygon(image, closed=True, facecolor=C[1], alpha=0.35, edgecolor=C[1], lw=1.5))
    for p, q in zip(square, image):
        ax.annotate("", xy=q, xytext=p, arrowprops={"arrowstyle": "-|>", "color": "0.45", "lw": 0.9,
                                                    "mutation_scale": 10, "connectionstyle": "arc3,rad=0.15"})
    ax.text(0.25, 0.45, "carré unité", color=C[0], fontsize=10)
    ax.text(3.2, -1.45, "φ(carré)", color=C[1], fontsize=10)
    ax.plot(*b, "o", color="black", ms=5)
    ax.text(b[0] - 0.95, b[1] - 0.15, "φ(0) = b", fontsize=10)
    ax.set(xlim=(-1, 5), ylim=(-2.8, 1.8), aspect="equal")
    ax.set_title("φ(x) = Ax + b : le carré est déplacé et déformé ; φ⁻¹ le ramène")
    save(fig, "affine.png")


def main() -> int:
    print(f"figures of M12a -> {OUT.relative_to(ROOT)}")
    span()
    coordinates()
    kernel_image()
    affine()
    return 0


if __name__ == "__main__":
    sys.exit(main())
