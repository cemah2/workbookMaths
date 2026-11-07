#!/usr/bin/env python
"""Draw the figures of chapter M07 (used by Claude).

    python tools/chapters/figures_m07.py

Writes small PNG files into chapitres/m07_vecteurs_rn/figures/: the unit balls of L1, L2, L4 and L∞ (and the
non-convex "ball" of p = 1/2), the projection of x = (3, 1) on a line in the plane, a hyperplane of the plane with its
normal vector, half-planes and the distance of a point, a cloud with its centroid and the inertia map, and two panels
on high dimension (angle of the diagonal of the cube, norm of Gaussian vectors). None comes from workbookIA 7 (no
eggs, no penguins, no ball in a cube, no hyper-orange, no Voronoi cells of centroids, no k-means iteration).
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

OUT = ROOT / "chapitres" / "m07_vecteurs_rn" / "figures"
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


def unit_balls() -> None:
    """The unit circles ‖x‖_p = 1 for p = 1, 2, 4 and ∞, and the curve of p = 1/2 (not a norm)."""
    fig, ax = plt.subplots(figsize=(5.2, 5.2))
    t = np.linspace(0, 2 * np.pi, 801)
    for p, color, label in [(1, C[0], "L1 : losange"), (2, C[1], "L2 : cercle"), (4, C[2], "L4"),
                            (np.inf, C[3], "L∞ : carré")]:
        c, s = np.cos(t), np.sin(t)
        if np.isinf(p):
            r = 1 / np.maximum(np.abs(c), np.abs(s))
        else:
            r = 1 / (np.abs(c) ** p + np.abs(s) ** p) ** (1 / p)
        ax.plot(r * c, r * s, color=color, lw=2, label=label)
    c, s = np.cos(t), np.sin(t)
    r = 1 / (np.sqrt(np.abs(c)) + np.sqrt(np.abs(s))) ** 2
    ax.plot(r * c, r * s, color="gray", lw=1.5, ls="--", label="p = 1/2 : pas une norme")
    ax.axhline(0, color="black", lw=0.6)
    ax.axvline(0, color="black", lw=0.6)
    ax.set_aspect("equal")
    ax.set(xlim=(-1.25, 1.25), ylim=(-1.25, 1.25), xlabel="$x_1$", ylabel="$x_2$",
           title="Les vecteurs de norme 1")
    ax.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=3)
    save(fig, "boules_unites.png")


def projection() -> None:
    """x = (1, 3) projected on the line directed by u = (3, 1): p = 0.6 u = (1.8, 0.6), residual orthogonal to u."""
    x, u = np.array([1.0, 3.0]), np.array([3.0, 1.0])
    p = (x @ u) / (u @ u) * u
    fig, ax = plt.subplots(figsize=(5.4, 4.4))
    line = np.linspace(-0.6, 1.4, 2)[:, None] * u
    ax.plot(line[:, 0], line[:, 1], color="gray", lw=1, label="la droite dirigée par u")
    ax.annotate("", xy=u, xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=C[0], lw=2))
    ax.annotate("", xy=x, xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=C[1], lw=2))
    ax.annotate("", xy=p, xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=C[2], lw=2.5))
    ax.plot([x[0], p[0]], [x[1], p[1]], color=C[3], ls="--", lw=1.5)
    # right-angle mark at p
    e1 = u / np.linalg.norm(u) * 0.18
    e2 = (x - p) / np.linalg.norm(x - p) * 0.18
    corner = np.array([p + e1, p + e1 + e2, p + e2])
    ax.plot(corner[:, 0], corner[:, 1], color="black", lw=0.8)
    ax.text(*(u + [0.05, -0.25]), "u", color=C[0], fontsize=12)
    ax.text(*(x + [0.08, 0.0]), "x", color=C[1], fontsize=12)
    ax.text(*(p + [0.0, -0.4]), "p", color=C[2], fontsize=12)
    ax.text(*((x + p) / 2 + [0.1, 0.0]), "x − p", color=C[3], fontsize=11)
    ax.set_aspect("equal")
    ax.set(xlim=(-1, 4), ylim=(-0.8, 3.5), xlabel="$x_1$", ylabel="$x_2$", title="Projection sur une droite")
    ax.legend(fontsize=8, loc="upper right")
    save(fig, "projection.png")


def hyperplane() -> None:
    """The line 2x + y − 4 = 0, its normal vector w = (2, 1), the two half-planes, a point and its distance."""
    w, b = np.array([2.0, 1.0]), -4.0
    fig, ax = plt.subplots(figsize=(5.6, 4.8))
    X, Y = np.meshgrid(np.linspace(-1, 5, 300), np.linspace(-2, 5, 300))
    score = w[0] * X + w[1] * Y + b
    ax.contourf(X, Y, score > 0, levels=[-0.5, 0.5, 1.5], colors=[C[0], C[1]], alpha=0.15)
    xs = np.linspace(-1, 5, 2)
    ax.plot(xs, -(w[0] * xs + b) / w[1], color="black", lw=2, label="w · x + b = 0")
    foot = np.array([1.0, 2.0])                                  # a point of the line
    ax.annotate("", xy=foot + w * 0.6, xytext=foot, arrowprops=dict(arrowstyle="->", color=C[2], lw=2.5))
    ax.text(*(foot + w * 0.6 + [0.05, 0.1]), "w", color=C[2], fontsize=12)
    q = np.array([3.5, 3.0])
    proj = q - (w @ q + b) / (w @ w) * w
    ax.plot(*q, "o", color=C[3])
    ax.plot([q[0], proj[0]], [q[1], proj[1]], color=C[3], ls="--", lw=1.5)
    ax.text(q[0] + 0.1, q[1] + 0.1, "x", color=C[3], fontsize=12)
    ax.text((q[0] + proj[0]) / 2 + 0.1, (q[1] + proj[1]) / 2 - 0.35,
            "distance\n|w · x + b| / ‖w‖", color=C[3], fontsize=9)
    ax.text(-0.6, -1.6, "w · x + b < 0", color=C[0], fontsize=10)
    ax.text(3.6, 4.4, "w · x + b > 0", color=C[1], fontsize=10)
    ax.set_aspect("equal")
    ax.set(xlim=(-1, 5), ylim=(-2, 5), xlabel="$x_1$", ylabel="$x_2$", title="Un hyperplan du plan : une droite")
    ax.legend(fontsize=8, loc="lower right")
    save(fig, "hyperplan.png")


def centroid_and_inertia() -> None:
    """Left: seven points and their centroid. Right: the inertia Σ‖x_i − c‖² for each c, smallest at the centroid."""
    pts = np.array([[0.5, 1.0], [1.5, 3.5], [2.0, 2.0], [3.5, 3.0], [4.0, 0.5], [2.5, 0.0], [1.0, 2.5]])
    g = pts.mean(axis=0)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.3))
    for p in pts:
        ax1.plot([p[0], g[0]], [p[1], g[1]], color="gray", lw=0.8)
    ax1.plot(pts[:, 0], pts[:, 1], "o", color=C[0], label="les points")
    ax1.plot(*g, "*", color=C[3], ms=16, label="le barycentre")
    ax1.set_aspect("equal")
    ax1.set(xlim=(-0.5, 5), ylim=(-0.8, 4.3), xlabel="$x_1$", ylabel="$x_2$", title="Un nuage et son barycentre")
    ax1.legend(fontsize=8, loc="upper right")
    X, Y = np.meshgrid(np.linspace(-0.5, 5, 200), np.linspace(-0.8, 4.3, 200))
    inertia = sum((X - p[0]) ** 2 + (Y - p[1]) ** 2 for p in pts)
    cs = ax2.contour(X, Y, inertia, levels=10, cmap="viridis")
    ax2.clabel(cs, fontsize=7, fmt=lambda v: f"{v:.0f}")
    ax2.plot(pts[:, 0], pts[:, 1], "o", color=C[0], alpha=0.5)
    ax2.plot(*g, "*", color=C[3], ms=16)
    ax2.set_aspect("equal")
    ax2.set(xlim=(-0.5, 5), ylim=(-0.8, 4.3), xlabel="$c_1$", ylabel="$c_2$",
            title="L'inertie autour de c : la plus petite au barycentre")
    save(fig, "barycentre.png")


def high_dimension() -> None:
    """Left: angle between the diagonal of the cube and an axis. Right: ‖X‖ / √n for Gaussian vectors."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.0))
    n = np.arange(1, 201)
    ax1.plot(n, np.degrees(np.arccos(1 / np.sqrt(n))), color=C[0], lw=2)
    ax1.axhline(90, color="gray", ls="--", lw=1)
    ax1.set(xlabel="dimension n", ylabel="angle (degrés)", ylim=(0, 95),
            title="Angle entre la diagonale du cube et un axe")
    rng = np.random.default_rng(707)
    bins = np.linspace(0.0, 2.2, 89)
    for dim, color in [(2, C[0]), (20, C[1]), (200, C[2]), (2000, C[3])]:
        norms = np.linalg.norm(rng.normal(size=(4000, dim)), axis=1) / np.sqrt(dim)
        ax2.hist(norms, bins=bins, density=True, histtype="step", lw=1.8, color=color, label=f"n = {dim}")
    ax2.set(xlabel="‖X‖ / √n", ylabel="densité", title="Norme de vecteurs gaussiens, divisée par √n")
    ax2.legend(fontsize=8)
    save(fig, "grande_dimension.png")


def main() -> int:
    print(f"Figures of M07 in {OUT.relative_to(ROOT)}:")
    unit_balls()
    projection()
    hyperplane()
    centroid_and_inertia()
    high_dimension()
    return 0


if __name__ == "__main__":
    sys.exit(main())
