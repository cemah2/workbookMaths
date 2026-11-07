#!/usr/bin/env python
"""Draw the figures of chapter M05b (used by Claude).

    python tools/chapters/figures_m05b.py

Writes small PNG files into chapitres/m05b_gradient/figures/: a surface with two hills and its map of level lines,
the two slices that give the partial derivatives of x³y + 2y², the gradient arrows of a dome across its level lines,
a tangent plane, the critical points of x³ + y³ − 3xy, a few gradient-descent steps, and the map of exercise M05b.16.
None comes from workbookIA 5 (no Rosenbrock, no x² − y², no xy, no x² + xy + 2y², no x³ − 3x − y³ + 3y).
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

OUT = ROOT / "chapitres" / "m05b_gradient" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        if ax.name == "3d":
            continue
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear":
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def two_hills(x, y):
    return 3 * np.exp(-((x - 1) ** 2 + y ** 2) / 2) + 2 * np.exp(-((x + 1.5) ** 2 + (y - 1) ** 2))


def surface_and_levels() -> None:
    """Left: the surface z = f(x, y) of two hills. Right: the same function as a map of level lines."""
    fig = plt.figure(figsize=(11, 4.2))
    x = np.linspace(-4, 4, 121)
    y = np.linspace(-3, 3.5, 121)
    X, Y = np.meshgrid(x, y)
    Z = two_hills(X, Y)
    ax3 = fig.add_subplot(1, 2, 1, projection="3d")
    ax3.plot_surface(X, Y, Z, cmap="viridis", linewidth=0, alpha=0.9)
    ax3.contour(X, Y, Z, levels=np.arange(0.25, 3.2, 0.5), offset=0, cmap="viridis", linewidths=0.8)
    ax3.set(xlabel="x", ylabel="y", zlabel="z", title="La surface z = f(x, y)")
    ax3.view_init(elev=32, azim=-60)
    ax = fig.add_subplot(1, 2, 2)
    levels = np.arange(0.25, 3.2, 0.25)
    cs = ax.contour(X, Y, Z, levels=levels, cmap="viridis", linewidths=1.2)
    ax.clabel(cs, levels[1::2], fmt=lambda v: french_number(round(v, 2)), fontsize=7)
    ax.plot([1, -1.5], [0, 1], "k^", markersize=6)
    ax.set(xlabel="x", ylabel="y", aspect="equal", title="Ses lignes de niveau f(x, y) = c")
    ax.grid(alpha=0.25)
    save(fig, "surface_niveaux.png")


def slices() -> None:
    """The partial derivatives of f(x, y) = x³y + 2y² at (1, 2): the slopes of the two slices through the point."""
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 3.6))
    x = np.linspace(-0.2, 2, 200)
    left.plot(x, 2 * x ** 3 + 8, color=C[0], linewidth=2, label="x ↦ f(x, 2) = 2x³ + 8")
    left.plot(x, 10 + 6 * (x - 1), "--", color=C[1], label="tangente, pente ∂f/∂x(1, 2) = 6")
    left.plot(1, 10, "o", color=C[1])
    left.set(xlabel="x (y fixé à 2)", ylim=(4, 26), title="On fixe y = 2 et l'on dérive en x")
    left.legend(fontsize=8, loc="upper left")
    left.grid(alpha=0.3)
    y = np.linspace(0.5, 3.2, 200)
    right.plot(y, y + 2 * y ** 2, color=C[0], linewidth=2, label="y ↦ f(1, y) = y + 2y²")
    right.plot(y, 10 + 9 * (y - 2), "--", color=C[2], label="tangente, pente ∂f/∂y(1, 2) = 9")
    right.plot(2, 10, "o", color=C[2])
    right.set(xlabel="y (x fixé à 1)", ylim=(0, 24), title="On fixe x = 1 et l'on dérive en y")
    right.legend(fontsize=8, loc="upper left")
    right.grid(alpha=0.3)
    save(fig, "tranches.png")


def gradient_and_levels() -> None:
    """The dome T(x, y) = 100 − x² − 2y²: gradient arrows across the level lines, and the point (3, 1)."""
    fig, ax = plt.subplots(figsize=(7.2, 5.2))
    x = np.linspace(-4.5, 4.5, 200)
    y = np.linspace(-3.2, 3.2, 200)
    X, Y = np.meshgrid(x, y)
    T = 100 - X ** 2 - 2 * Y ** 2
    levels = np.arange(76, 100, 4)
    cs = ax.contour(X, Y, T, levels=levels, cmap="viridis", linewidths=1.2)
    ax.clabel(cs, fmt=lambda v: french_number(round(v)), fontsize=8)
    gx, gy = np.meshgrid(np.arange(-4, 4.1, 1.0), np.arange(-3, 3.1, 1.0))
    ax.quiver(gx, gy, -2 * gx, -4 * gy, color="gray", angles="xy", scale_units="xy", scale=12, width=0.004)
    ax.plot(3, 1, "o", color=C[3], markersize=7)
    ax.quiver([3], [1], [-6], [-4], color=C[3], angles="xy", scale_units="xy", scale=6, width=0.008,
              label="∇T(3, 1) = (−6, −4)")
    tangent = np.array([4, -6]) / np.sqrt(52)
    ax.plot([3 - 1.2 * tangent[0], 3 + 1.2 * tangent[0]], [1 - 1.2 * tangent[1], 1 + 1.2 * tangent[1]], ":",
            color=C[3], linewidth=2, label="la ligne de niveau en (3, 1) : direction (4, −6)")
    ax.set(xlabel="x", ylabel="y", aspect="equal", xlim=(-4.5, 4.5), ylim=(-3.2, 3.2),
           title="Le gradient monte le plus vite, à angle droit des lignes de niveau")
    ax.title.set_fontsize(10)
    ax.legend(fontsize=8, loc="lower left")
    save(fig, "gradient_niveaux.png")


def tangent_plane() -> None:
    """The bowl z = 2x² + y² and its tangent plane at (0.5, 1): z = 1.5 + 2(x − 0.5) + 2(y − 1)."""
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(projection="3d")
    x = np.linspace(-0.8, 1.8, 50)
    y = np.linspace(-0.6, 2.6, 50)
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, 2 * X ** 2 + Y ** 2, cmap="viridis", alpha=0.45, linewidth=0)
    xp = np.linspace(-0.2, 1.2, 10)
    yp = np.linspace(0.2, 1.8, 10)
    XP, YP = np.meshgrid(xp, yp)
    ax.plot_surface(XP, YP, 1.5 + 2 * (XP - 0.5) + 2 * (YP - 1), color=C[1], alpha=0.85, linewidth=0)
    ax.scatter([0.5], [1], [1.5], color="black", s=40, depthshade=False)
    ax.set(xlabel="x", ylabel="y", zlabel="z", title="La surface z = 2x² + y² et son plan tangent en (0,5 ; 1)")
    ax.view_init(elev=6, azim=-62)
    save(fig, "plan_tangent.png")


def critical_points() -> None:
    """x³ + y³ − 3xy: a saddle at (0, 0) and a local minimum at (1, 1)."""
    fig, ax = plt.subplots(figsize=(6.4, 5.2))
    x = np.linspace(-1.5, 2, 300)
    X, Y = np.meshgrid(x, x)
    F = X ** 3 + Y ** 3 - 3 * X * Y
    levels = [-0.9, -0.6, -0.3, 0, 0.5, 1, 2, 4]
    cs = ax.contour(X, Y, F, levels=levels, cmap="viridis", linewidths=1.2)
    ax.clabel(cs, fmt=lambda v: french_number(round(v, 1)), fontsize=7)
    ax.plot(0, 0, "X", color=C[3], markersize=10, label="(0, 0) : point selle")
    ax.plot(1, 1, "o", color=C[2], markersize=8, label="(1, 1) : minimum local, f = −1")
    ax.set(xlabel="x", ylabel="y", aspect="equal", title="Les points critiques de f(x, y) = x³ + y³ − 3xy")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.25)
    save(fig, "points_critiques.png")


def descent() -> None:
    """Steps x ← x − 0,1 ∇f(x) on f(x, y) = (x − 3)² + 2(y + 1)², from (0, 0)."""
    fig, ax = plt.subplots(figsize=(6.8, 4.6))
    x = np.linspace(-0.5, 4.5, 200)
    y = np.linspace(-2.5, 0.8, 200)
    X, Y = np.meshgrid(x, y)
    F = (X - 3) ** 2 + 2 * (Y + 1) ** 2
    cs = ax.contour(X, Y, F, levels=[0.25, 1, 2, 4, 6.48, 11], cmap="viridis", linewidths=1.1)
    ax.clabel(cs, fmt=lambda v: french_number(round(v, 2)), fontsize=7)
    point = np.array([0.0, 0.0])
    path = [point.copy()]
    for _ in range(8):
        point = point - 0.1 * np.array([2 * (point[0] - 3), 4 * (point[1] + 1)])
        path.append(point.copy())
    path = np.array(path)
    ax.plot(path[:, 0], path[:, 1], "o-", color=C[3], markersize=4, label="les pas, η = 0,1")
    ax.plot(3, -1, "*", color="black", markersize=12, label="le minimum (3, −1)")
    ax.set(xlabel="x", ylabel="y", aspect="equal", title="Descendre : chaque pas va contre le gradient")
    ax.legend(fontsize=8, loc="lower left")
    ax.grid(alpha=0.25)
    save(fig, "descente.png")


def exercise_16_map() -> None:
    """The map of exercise M05b.16: integer level lines of an unnamed function, five marked points."""
    fig, ax = plt.subplots(figsize=(6.4, 5.4))
    x = np.linspace(-0.5, 3.2, 300)
    y = np.linspace(-2.2, 3.2, 300)
    X, Y = np.meshgrid(x, y)
    F = X ** 2 + 2 * Y
    levels = np.arange(-4, 13, 1)
    cs = ax.contour(X, Y, F, levels=levels, colors="tab:blue", linewidths=1, linestyles="solid")
    spots = [(0.0, c / 2) for c in range(-4, 7)] + [(float(np.sqrt(c - 6)), 3.0) for c in range(7, 13)]
    ax.clabel(cs, fmt=lambda v: french_number(round(v)), fontsize=8, inline_spacing=2, manual=spots)
    points = {"A": (1, 1), "B": (2, 1), "C": (1, 2), "P": (0.5, -1), "Q": (2.5, -1)}
    for name, (px, py) in points.items():
        ax.plot(px, py, "o", color=C[3], markersize=6)
        ax.annotate(name, (px, py), xytext=(5, 5), textcoords="offset points", fontsize=10, color=C[3],
                    fontweight="bold")
    ax.set(xlabel="x", ylabel="y", xlim=(-0.5, 3.2), ylim=(-2.2, 3.2), aspect="equal",
           xticks=np.arange(0, 3.5, 0.5), yticks=np.arange(-2, 3.5, 0.5),
           title="Les lignes de niveau de f (valeurs entières)")
    ax.grid(alpha=0.4)
    save(fig, "m05b_16_carte.png")


def main() -> int:
    print(f"Figures of M05b → {OUT}")
    surface_and_levels()
    slices()
    gradient_and_levels()
    tangent_plane()
    critical_points()
    descent()
    exercise_16_map()
    return 0


if __name__ == "__main__":
    sys.exit(main())
