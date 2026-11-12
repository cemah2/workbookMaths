#!/usr/bin/env python
"""Draw the figures of chapter M19 (used by Claude).

    python tools/chapters/figures_m19.py

Writes small PNG files into chapitres/m19_hessienne_convergence/figures/: the level lines of x³ − 6x² + y² with its
two critical points (a saddle and a minimum) and the eigendirections of the Hessian there; Richardson's iterates for
the system of two springs, A = [[5, −2], [−2, 2]], b = (2, 1), on the level lines of ½ xᵀAx − bᵀx, for three steps;
the convergence factor ρ(ω) = max(|1 − ω|, |1 − 6ω|) of the same system; the stability triangle of the recurrences
u_{k+2} = p u_{k+1} − q u_k in the plane (p, q), with the parabola q = p²/4; the projections of (12, −5) on a ball and
on a box. The numbers are those of the fiche; none comes from workbookIA 19 (no loss, no valley, no learning rate, no
19xx seed). No randomness.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m19_hessienne_convergence" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

SPRINGS_A = np.array([[5.0, -2.0], [-2.0, 2.0]])   # §4: the stiffness matrix of the two springs (eigenvalues 1, 6)
SPRINGS_B = np.array([2.0, 1.0])                    # §4: the two forces; the solution is (1, 1.5)
START = np.array([-1.0, 2.0])                       # a start with a large component on the stiff direction
STEPS = [(0.25, "ω = 0,25 (ρ = 0,75)"), (2 / 7, "ω = 2/7, le meilleur pas (ρ = 5/7)"),
         (0.32, "ω = 0,32, près du pas critique 1/3 (ρ = 0,92)")]
PROJECTED = np.array([12.0, -5.0])                  # §8: the vector projected on the ball and on the box
RADIUS, HALF_SIDE = 2.6, 2.0


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and ax.axison:
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def arrow(ax, start, vector, color, label=None, where=None):
    start = np.asarray(start, dtype=float)
    ax.add_patch(FancyArrowPatch(start, start + vector, arrowstyle="-|>", mutation_scale=14, color=color, lw=1.8,
                                 zorder=4))
    if label:
        ax.text(*where, label, color=color, fontsize=9, zorder=5)


def critical_points() -> None:
    """§2: the level lines of x³ − 6x² + y² (the slice z = 0 of the example), a saddle at (0, 0), a minimum at (4, 0)."""
    xs, ys = np.meshgrid(np.linspace(-2.2, 6.2, 400), np.linspace(-4.5, 4.5, 400))
    values = xs ** 3 - 6 * xs ** 2 + ys ** 2
    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    levels = np.concatenate([np.arange(-34, 0, 4), np.arange(0, 30, 4)])
    contours = ax.contour(xs, ys, values, levels=levels, cmap="Greys", linewidths=0.8)
    ax.clabel(contours, levels[::2], fontsize=7, fmt=lambda v: french_number(v))
    ax.contour(xs, ys, values, levels=[0], colors=[C[0]], linewidths=1.6)
    ax.plot([0], [0], "o", color=C[1], ms=8, zorder=5)
    ax.plot([4], [0], "o", color=C[2], ms=8, zorder=5)
    box = dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85)
    ax.text(0.15, -2.1, "selle (0, 0)", color=C[1], fontsize=10, bbox=box)
    ax.text(4.15, -2.1, "minimum (4, 0)", color=C[2], fontsize=10, bbox=box)
    for start, label in (((0, 0), None), ((4, 0), None)):
        arrow(ax, start, (1.3, 0), C[3])
        arrow(ax, start, (-1.3, 0), C[3])
        arrow(ax, start, (0, 1.3), C[4])
        arrow(ax, start, (0, -1.3), C[4])
    ax.text(-2.1, 0.3, "courbure −12\n(f descend)", color=C[3], fontsize=9, bbox=box)
    ax.text(2.45, 0.3, "courbure 12", color=C[3], fontsize=9, bbox=box)
    ax.text(0.15, 1.45, "courbure 2", color=C[4], fontsize=9, bbox=box)
    ax.text(4.15, 1.45, "courbure 2", color=C[4], fontsize=9, bbox=box)
    ax.set(xlabel="x", ylabel="y", xlim=(-2.2, 6.2), ylim=(-4.5, 4.5))
    ax.set_aspect("equal")
    ax.set_title("Les lignes de niveau de x³ − 6x² + y² et les directions propres de la hessienne\n"
                 "aux deux points critiques (la ligne de niveau 0 en couleur passe par la selle)", fontsize=10)
    save(fig, "points_critiques.png")


def richardson(omega, start, n):
    path = [start.copy()]
    x = start.copy()
    for _ in range(n):
        x = x + omega * (SPRINGS_B - SPRINGS_A @ x)
        path.append(x.copy())
    return np.array(path)


def richardson_springs() -> None:
    """§4: Richardson's iterates on the level lines of ½ xᵀAx − bᵀx, for three steps."""
    solution = np.linalg.solve(SPRINGS_A, SPRINGS_B)
    xs, ys = np.meshgrid(np.linspace(-1.6, 2.6, 300), np.linspace(-0.4, 3.0, 300))
    points = np.stack([xs, ys], axis=-1)
    energy = 0.5 * np.einsum("...i,ij,...j->...", points, SPRINGS_A, points) - points @ SPRINGS_B
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.4), sharey=True)
    for ax, (omega, title) in zip(axes, STEPS):
        bottom = -0.5 * SPRINGS_B @ solution          # the minimum of ½ xᵀAx − bᵀx
        ax.contour(xs, ys, energy, levels=bottom + 0.06 * np.arange(1, 13) ** 2, colors="0.6", linewidths=0.7,
                   linestyles="solid")
        path = richardson(omega, START, 12)
        ax.plot(path[:, 0], path[:, 1], "-o", color=C[0], ms=3.5, lw=1.2)
        ax.plot(*START, "s", color=C[1], ms=7, label="départ (−1 ; 2)")
        ax.plot(*solution, "*", color=C[2], ms=13, label="solution (1 ; 1,5)")
        ax.set_title(title + "\n12 pas", fontsize=9.5)
        ax.set_xlabel("$x_1$")
        ax.set_aspect("equal")
        ax.grid(alpha=0.25)
    axes[0].set_ylabel("$x_2$")
    axes[0].legend(fontsize=8, loc="upper right")
    fig.suptitle("Richardson pour les deux ressorts, A = [[5, −2], [−2, 2]], b = (2 ; 1), sur les lignes de niveau de "
                 "½ xᵀAx − bᵀx (valeurs propres 1 et 6, pas critique 1/3)", fontsize=10.5)
    save(fig, "richardson_ressorts.png")


def factor_curve() -> None:
    """§5: ρ(ω) = max(|1 − ω|, |1 − 6ω|) for the two springs."""
    omegas = np.linspace(0, 0.4, 801)
    small, large = np.abs(1 - omegas), np.abs(1 - 6 * omegas)
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    ax.plot(omegas, small, color=C[0], lw=1.4, ls="--", label="|1 − ω λmin|, λmin = 1")
    ax.plot(omegas, large, color=C[1], lw=1.4, ls="--", label="|1 − ω λmax|, λmax = 6")
    ax.plot(omegas, np.maximum(small, large), color=C[2], lw=2.6, label="ρ(ω), le plus grand des deux")
    ax.axhline(1, color="0.4", lw=0.9)
    ax.axvline(1 / 3, color=C[1], lw=1, ls=":")
    ax.plot([2 / 7], [5 / 7], "o", color=C[2], ms=8, zorder=5)
    ax.annotate("ω* = 2/7, ρ* = 5/7", (2 / 7, 5 / 7), (0.13, 0.42), fontsize=9, color=C[2],
                arrowprops=dict(arrowstyle="->", color=C[2]))
    ax.text(0.328, 1.27, "pas critique 1/3 :\nau-delà, ρ > 1", fontsize=9, color=C[1], ha="right")
    ax.set(xlabel="le pas ω", ylabel="facteur par pas", xlim=(0, 0.4), ylim=(0, 1.5))
    ax.legend(fontsize=8.5, loc="lower left")
    ax.grid(alpha=0.25)
    ax.set_title("Le facteur de convergence de Richardson pour les deux ressorts", fontsize=10.5)
    save(fig, "facteur_richardson.png")


def stability_triangle() -> None:
    """§6: the triangle |q| < 1, |p| < 1 + q, cut by the parabola q = p²/4."""
    fig, ax = plt.subplots(figsize=(7.2, 5.2))
    ax.add_patch(Polygon([(-2, 1), (2, 1), (0, -1)], closed=True, fc=C[0], alpha=0.12, ec=C[0], lw=1.6))
    ps = np.linspace(-2, 2, 400)
    ax.plot(ps, ps ** 2 / 4, color=C[1], lw=1.6, label="q = p²/4 (racine double)")
    upper = np.linspace(-2, 2, 400)
    ax.fill_between(upper, upper ** 2 / 4, 1, color=C[1], alpha=0.10)
    ax.text(0, 0.72, "racines complexes de module √q :\noscillation amortie", ha="center", fontsize=9, color=C[1])
    ax.text(0, -0.35, "racines réelles\nde module < 1", ha="center", fontsize=9, color=C[0])
    for (p, q), label, color, dx in (((1, 0.21), "u₍ₖ₊₂₎ = u₍ₖ₊₁₎ − 0,21 uₖ", C[2], 0.08),
                                     ((0.8, 0.64), "u₍ₖ₊₂₎ = 0,8 u₍ₖ₊₁₎ − 0,64 uₖ", C[2], 0.08),
                                     ((1.5, -1), "u₍ₖ₊₂₎ = 1,5 u₍ₖ₊₁₎ + uₖ : hors du triangle", C[3], 0.08)):
        ax.plot([p], [q], "o", color=color, ms=7, zorder=5)
        ax.text(p + dx, q + 0.04, label, fontsize=8.5, color=color)
    for vertex in ((-2, 1), (2, 1), (0, -1)):
        ax.plot(*vertex, "k.", ms=6)
    ax.text(-2.05, 1.06, "(−2 ; 1)", fontsize=8.5, ha="center")
    ax.text(2.05, 1.06, "(2 ; 1)", fontsize=8.5, ha="center")
    ax.text(0.1, -1.12, "(0 ; −1)", fontsize=8.5)
    ax.axhline(0, color="0.6", lw=0.7)
    ax.axvline(0, color="0.6", lw=0.7)
    ax.set(xlabel="p", ylabel="q", xlim=(-2.6, 3.6), ylim=(-1.3, 1.35))
    ax.legend(fontsize=8.5, loc="lower right")
    ax.set_title("u₍ₖ₊₂₎ = p u₍ₖ₊₁₎ − q uₖ tend vers 0 depuis tout départ\n"
                 "si et seulement si |q| < 1 et |p| < 1 + q (l'intérieur du triangle)", fontsize=10)
    save(fig, "triangle_stabilite.png")


def projections() -> None:
    """§8: (12, −5) projected on the ball of radius 2,6 and on the box [−2, 2]²."""
    ball = PROJECTED * min(1.0, RADIUS / np.linalg.norm(PROJECTED))
    box = np.clip(PROJECTED, -HALF_SIDE, HALF_SIDE)
    fig, ax = plt.subplots(figsize=(8.4, 4.6))
    ax.add_patch(Circle((0, 0), RADIUS, fc=C[0], alpha=0.12, ec=C[0], lw=1.6))
    ax.add_patch(Rectangle((-HALF_SIDE, -HALF_SIDE), 2 * HALF_SIDE, 2 * HALF_SIDE, fc=C[1], alpha=0.10, ec=C[1],
                           lw=1.6))
    arrow(ax, (0, 0), PROJECTED, "0.35")
    ax.text(PROJECTED[0] - 1.2, PROJECTED[1] - 0.8, "x = (12 ; −5)", fontsize=10)
    for point, color, text, offset in ((ball, C[0], "sur la boule de rayon 2,6 :\n(2,4 ; −1), même direction",
                                        (0.4, 0.55)),
                                       (box, C[1], "sur le pavé [−2, 2]² :\n(2 ; −2), direction changée", (-5.2, -1.4))):
        ax.plot([PROJECTED[0], point[0]], [PROJECTED[1], point[1]], ls=":", color=color, lw=1.3)
        ax.plot(*point, "o", color=color, ms=7, zorder=5)
        ax.text(point[0] + offset[0], point[1] + offset[1], text, fontsize=9, color=color)
    ax.plot([0, 2.6 * 2], [0, -2.6 * 2], color=C[1], lw=0.8, ls="--")
    ax.set(xlim=(-3.4, 13.5), ylim=(-6.2, 3.4), xlabel="première coordonnée", ylabel="seconde coordonnée")
    ax.set_aspect("equal")
    ax.grid(alpha=0.25)
    ax.set_title("Projeter (12 ; −5) : la boule garde la direction, le pavé coupe chaque coordonnée", fontsize=10.5)
    save(fig, "projections.png")


def main() -> int:
    print(f"Figures M19 → {OUT.relative_to(ROOT)}")
    critical_points()
    richardson_springs()
    factor_curve()
    stability_triangle()
    projections()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
