#!/usr/bin/env python
"""Draw the figures of chapter R9 (used by Claude).

    python tools/chapters/figures_r9.py

Writes small PNG files into chapitres/r9_geometrie_vecteurs/figures/: a point, a distance and a midpoint in a frame,
the sum of two vectors (tip to tail and parallelogram), the unit "circles" of the norms L1, L2 and L∞, a line with a
direction vector and a normal vector, the projection of a vector on another, the unit circle with cos and sin, the
curves of cos and sin, the angle between two vectors, and a vector of space. Every figure is computed and uses the
workbook style (wbm.plot colours, French decimal commas). The vectors are those of the sheet's own examples: none
comes from workbookIA 0B, from the placement test or from an exercise of R9.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Arc, Polygon  # noqa: E402
from matplotlib.ticker import FuncFormatter, MultipleLocator  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "r9_geometrie_vecteurs" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str, formatter: bool = True) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if formatter:
        for ax in fig.axes:
            for axis in (ax.xaxis, ax.yaxis):
                if axis.get_scale() == "linear":
                    axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def frame(ax, xlim, ylim, step=1) -> None:
    """Orthonormal axes through the origin, a light grid, the same unit on both axes."""
    ax.axhline(0, color="gray", linewidth=0.9)
    ax.axvline(0, color="gray", linewidth=0.9)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.xaxis.set_major_locator(MultipleLocator(step))
    ax.yaxis.set_major_locator(MultipleLocator(step))
    ax.grid(True, alpha=0.3)


def arrow(ax, start, vec, colour, label=None, offset=(0.15, 0.15), width=0.04, style="-", size=12):
    ax.annotate("", xy=(start[0] + vec[0], start[1] + vec[1]), xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": colour, "lw": 2, "linestyle": style,
                            "shrinkA": 0, "shrinkB": 0, "mutation_scale": 16})
    if label:
        mx, my = start[0] + vec[0] / 2 + offset[0], start[1] + vec[1] / 2 + offset[1]
        ax.text(mx, my, label, color=colour, fontsize=size, fontweight="bold" if size >= 12 else "normal")


def fig_frame() -> None:
    """§1: A(−2, 1), B(6, 16): the right triangle of sides 8 and 15, the distance 17 and the midpoint M(2 ; 8,5)."""
    A, B = np.array([-2, 1]), np.array([6, 16])
    M = (A + B) / 2
    fig, ax = plt.subplots(figsize=(5.2, 7.2))
    frame(ax, (-4, 9), (-1, 18), step=2)
    ax.plot([A[0], B[0], B[0], A[0]], [A[1], A[1], B[1], A[1]], color=C[2], linewidth=1.2, linestyle="--")
    ax.plot([A[0], B[0]], [A[1], B[1]], color=C[0], linewidth=2.2)
    for P, name, dx, dy in ((A, "A(−2 ; 1)", 0.3, -1.0), (B, "B(6 ; 16)", 0.3, 0.4), (M, "M(2 ; 8,5)", 0.4, 0.4)):
        ax.plot(*P, "o", color="black", markersize=6)
        ax.text(P[0] + dx, P[1] + dy, name, ha="left", fontsize=11)
    ax.text(3.6, A[1] + 0.3, "xB − xA = 8", ha="center", color=C[2], fontsize=10)
    ax.text(B[0] + 0.3, (A[1] + B[1]) / 2, "yB − yA = 15", ha="left", color=C[2], fontsize=10)
    ax.text(0.9, 10.6, "AB = √(8² + 15²) = 17", color=C[0], fontsize=11, rotation=60)
    ax.set_title("Distance et milieu dans un repère orthonormé", fontsize=10)
    save(fig, "repere.png")


def fig_vectors() -> None:
    """§2: u = (3, −1) and v = (−2, 4); u + v by tip to tail and by the parallelogram; 2u and −v."""
    u, v = np.array([3, -1]), np.array([-2, 4])
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8))
    ax = axes[0]
    frame(ax, (-2.5, 4.5), (-1.5, 4.5))
    arrow(ax, (0, 0), u, C[0], "u", offset=(0.1, -0.5))
    arrow(ax, u, v, C[1], "v", offset=(0.25, 0))
    arrow(ax, (0, 0), u + v, C[2], "u + v", offset=(-0.9, 0.4))
    arrow(ax, (0, 0), v, C[1], None, style="--")
    arrow(ax, v, u, C[0], None, style="--")
    ax.set_title("u + v : les flèches bout à bout (et le parallélogramme)", fontsize=10)
    ax = axes[1]
    frame(ax, (-2.5, 6.5), (-4.5, 4.5))
    arrow(ax, (0, 0), 2 * u, C[0], "2u", offset=(0.1, 0.15))
    arrow(ax, (0, 0), u, C[3], "u", offset=(-0.1, 0.3))
    arrow(ax, (0, 0), v, C[1], "v", offset=(-0.6, 0))
    arrow(ax, (0, 0), -v, C[1], "−v", offset=(0.25, 0))
    ax.set_title("Multiplier par un nombre : 2u (même sens), −v (sens contraire)", fontsize=10)
    fig.tight_layout()
    save(fig, "vecteurs.png")


def fig_norms() -> None:
    """§3: the points at distance 1 from the origin for the norms L1 (a diamond), L2 (a circle) and L∞ (a square)."""
    fig, ax = plt.subplots(figsize=(5.2, 5.2))
    frame(ax, (-1.6, 1.6), (-1.6, 1.6), step=0.5)
    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(t), np.sin(t), color=C[0], linewidth=2, label="‖u‖₂ = 1 : un cercle")
    ax.plot([1, 0, -1, 0, 1], [0, 1, 0, -1, 0], color=C[1], linewidth=2, label="‖u‖₁ = 1 : un losange")
    ax.plot([1, -1, -1, 1, 1], [1, 1, -1, -1, 1], color=C[2], linewidth=2, label="‖u‖∞ = 1 : un carré")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.32), fontsize=9, ncol=1)
    ax.set_title("Les vecteurs de longueur 1 pour trois normes", fontsize=10)
    save(fig, "normes.png")


def fig_line() -> None:
    """§4: the line y = 2x − 3 through A(1, −1) and B(4, 5), a direction vector (1, 2) and a normal vector (2, −1)."""
    fig, ax = plt.subplots(figsize=(6.4, 6))
    frame(ax, (-2, 6), (-5, 7))
    xs = np.linspace(-2, 6, 2)
    ax.plot(xs, 2 * xs - 3, color=C[0], linewidth=2, label="y = 2x − 3, soit 2x − y − 3 = 0")
    gx, gy = np.meshgrid(np.linspace(-2, 6, 120), np.linspace(-5, 7, 120))
    ax.contourf(gx, gy, 2 * gx - gy - 3, levels=[-100, 0, 100], colors=[C[1], C[2]], alpha=0.10)
    for P, name in (((1, -1), "A(1 ; −1)"), ((4, 5), "B(4 ; 5)")):
        ax.plot(*P, "o", color="black", markersize=6)
        ax.text(P[0] + 0.25, P[1] - 0.2, name, fontsize=11)
    arrow(ax, (2, 1), (1, 2), C[3], "(1 ; 2) directeur", offset=(-3.3, 0.6), size=10)
    arrow(ax, (2, 1), (2, -1), C[1], "(2 ; −1) normal", offset=(-0.3, -0.9), size=10)
    ax.text(-1.6, 5.5, "2x − y − 3 < 0", color=C[1], fontsize=10)
    ax.text(2.4, -4.3, "2x − y − 3 > 0", color=C[2], fontsize=10)
    ax.legend(loc="upper left", fontsize=9, bbox_to_anchor=(0.0, -0.08))
    ax.set_title("Une droite, un vecteur directeur, un vecteur normal", fontsize=10)
    save(fig, "droite.png")


def fig_projection() -> None:
    """§5: v = (1, 3) projected on the direction of u = (4, 2): p = (2, 1), and v − p = (−1, 2) is orthogonal to u."""
    u, v = np.array([4, 2]), np.array([1, 3])
    p = (u @ v) / (u @ u) * u
    fig, ax = plt.subplots(figsize=(6, 4.6))
    frame(ax, (-1.5, 5), (-0.8, 3.8))
    arrow(ax, (0, 0), u, C[0], "u", offset=(0.1, -0.5))
    arrow(ax, (0, 0), v, C[1], "v", offset=(-0.5, 0.1))
    arrow(ax, (0, 0), p, C[2], "p", offset=(0.0, 0.25))
    arrow(ax, p, v - p, C[3], "v − p", offset=(0.15, 0))
    s = 0.25 * u / np.linalg.norm(u)
    n = 0.25 * (v - p) / np.linalg.norm(v - p)
    ax.add_patch(Polygon([p - s, p - s + n, p + n - s + s, p], closed=False, fill=False, edgecolor="black"))
    ax.set_title("L'ombre de v sur la direction de u : p = (u·v / ‖u‖²) u", fontsize=10)
    save(fig, "projection.png")


def fig_circle() -> None:
    """§6: the unit circle, the point of angle 7π/6, its cosine (abscissa) and sine (ordinate), and π/6, π/4, π/3."""
    theta = 7 * np.pi / 6
    fig, ax = plt.subplots(figsize=(6, 6))
    frame(ax, (-1.35, 1.35), (-1.35, 1.35), step=0.5)
    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(t), np.sin(t), color="black", linewidth=1.2)
    x, y = np.cos(theta), np.sin(theta)
    ax.plot([0, x], [0, y], color=C[0], linewidth=2)
    ax.plot([x, x], [0, y], color=C[2], linestyle="--")
    ax.plot([0, x], [y, y], color=C[1], linestyle="--")
    ax.plot(x, y, "o", color=C[0], markersize=7)
    ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=0, theta2=210, color=C[0], linewidth=1.5))
    ax.text(0.05, 0.3, "7π/6", color=C[0], fontsize=11)
    ax.text(x, 0.07, "cos = −√3/2", color=C[2], ha="center", fontsize=10)
    ax.text(0.05, y - 0.12, "sin = −1/2", color=C[1], fontsize=10)
    for angle, name in ((np.pi / 6, "π/6"), (np.pi / 4, "π/4"), (np.pi / 3, "π/3"), (np.pi / 2, "π/2"),
                        (np.pi, "π"), (3 * np.pi / 2, "3π/2"), (0, "0")):
        px, py = np.cos(angle), np.sin(angle)
        ax.plot(px, py, "o", color="gray", markersize=4)
        ax.text(1.13 * px, 1.13 * py, name, ha="center", va="center", fontsize=9, color="0.3")
    ax.set_title("Le cercle trigonométrique : cos θ est l'abscisse, sin θ l'ordonnée", fontsize=10)
    save(fig, "cercle.png")


def fig_curves() -> None:
    """§6: cos and sin on [−2π, 2π], with the period 2π and the bounds −1 and 1."""
    t = np.linspace(-2 * np.pi, 2 * np.pi, 800)
    fig, ax = plt.subplots(figsize=(8.4, 3.6))
    ax.plot(t, np.cos(t), color=C[2], linewidth=2, label="cos")
    ax.plot(t, np.sin(t), color=C[1], linewidth=2, label="sin")
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.axvline(0, color="gray", linewidth=0.8)
    ticks = np.arange(-2, 2.5, 0.5) * np.pi
    names = ["−2π", "−3π/2", "−π", "−π/2", "0", "π/2", "π", "3π/2", "2π"]
    ax.set_xticks(ticks, names)
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.annotate("", xy=(2 * np.pi, 1.25), xytext=(0, 1.25), arrowprops={"arrowstyle": "<->", "color": "0.3"})
    ax.text(np.pi, 1.32, "une période : 2π", ha="center", fontsize=9, color="0.3")
    ax.set_ylim(-1.3, 1.55)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower left", fontsize=9)
    ax.set_title("Les courbes de cosinus et de sinus", fontsize=10)
    for axis in (ax.yaxis,):
        axis.set_major_formatter(FuncFormatter(french_number))
    save(fig, "courbes_trig.png", formatter=False)


def fig_angle() -> None:
    """§7: u = (3, −1) and v = (−2, 4): u·v = −10, cos θ = −√2/2, θ = 3π/4 (135°)."""
    u, v = np.array([3, -1]), np.array([-2, 4])
    fig, ax = plt.subplots(figsize=(5.4, 5.2))
    frame(ax, (-2.5, 3.5), (-1.5, 4.5))
    arrow(ax, (0, 0), u, C[0], "u", offset=(0.1, -0.45))
    arrow(ax, (0, 0), v, C[1], "v", offset=(-0.6, 0))
    start = np.degrees(np.arctan2(u[1], u[0]))
    end = np.degrees(np.arctan2(v[1], v[0]))
    ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=start, theta2=end, color=C[2], linewidth=2))
    ax.text(0.45, 0.55, "θ = 135°", color=C[2], fontsize=11)
    ax.set_title("cos θ = u·v / (‖u‖ ‖v‖) = −10 / (√10 √20) = −√2/2", fontsize=10)
    save(fig, "angle.png")


def fig_space() -> None:
    """§8: u = (2, 3, 6) in space, the box of its coordinates, and its length √(4 + 9 + 36) = 7."""
    fig = plt.figure(figsize=(5.6, 5.4))
    ax = fig.add_subplot(projection="3d")
    x, y, z = 2, 3, 6
    ax.quiver(0, 0, 0, x, y, z, color=C[0], linewidth=2, arrow_length_ratio=0.08)
    for a, b in (((0, 0, 0), (x, 0, 0)), ((x, 0, 0), (x, y, 0)), ((0, 0, 0), (0, y, 0)), ((0, y, 0), (x, y, 0)),
                 ((x, y, 0), (x, y, z)), ((0, 0, 0), (x, y, 0))):
        ax.plot(*zip(a, b), color="gray", linestyle="--", linewidth=1)
    ax.text(x, y, z + 0.3, "u = (2 ; 3 ; 6)", color=C[0], fontsize=11)
    ax.text(x / 2 + 0.2, y / 2, 0, "√(2² + 3²)", color="0.3", fontsize=9)
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    ax.set_zlim(0, 7)
    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.set_zticks(range(8))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("‖u‖ = √(2² + 3² + 6²) = 7 : Pythagore deux fois", fontsize=10)
    save(fig, "espace.png", formatter=False)


def main() -> int:
    print(f"Figures of R9 -> {OUT.relative_to(ROOT)}")
    fig_frame()
    fig_vectors()
    fig_norms()
    fig_line()
    fig_projection()
    fig_circle()
    fig_curves()
    fig_angle()
    fig_space()
    return 0


if __name__ == "__main__":
    sys.exit(main())
