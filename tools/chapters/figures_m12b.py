#!/usr/bin/env python
"""Draw the figures of chapter M12b (used by Claude).

    python tools/chapters/figures_m12b.py

Writes small PNG files into chapitres/m12b_orthogonalite/figures/: the unit "circle" of the inner product of the fiche
(an ellipse) next to the usual one, one Gram-Schmidt step in the plane, the projection of v = (2, 1, 6) on the plane
of the fiche, least squares seen on the scatter plot and as a projection, and the best affine approximation of x² on
[0 ; 1]. None comes from workbookIA 12 or 25 (no cloud of points projected on an axis, no principal component, no
covariance matrix).
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m12b_orthogonalite" / "figures"
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


def arrow(ax, start, vector, color, label, offset=(0.1, 0.1), lw=2.2, ls="-"):
    ax.annotate("", xy=(start[0] + vector[0], start[1] + vector[1]), xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": lw, "mutation_scale": 14, "ls": ls})
    if label:
        mid = (start[0] + vector[0] / 2 + offset[0], start[1] + vector[1] / 2 + offset[1])
        ax.text(*mid, label, color=color, fontsize=11)


def axes_frame(ax, lim):
    ax.axhline(0, color="0.6", lw=0.8)
    ax.axvline(0, color="0.6", lw=0.8)
    ax.set(xlim=(-lim, lim), ylim=(-lim, lim), aspect="equal")


def inner_products() -> None:
    """Left: the usual unit circle, e1 ⊥ e2. Right: {x : xᵀMx = 1} for M = [[1, 2], [2, 5]], with e1 and (−2, 1)."""
    M = np.array([[1.0, 2.0], [2.0, 5.0]])
    theta = np.linspace(0, 2 * np.pi, 400)
    circle = np.column_stack([np.cos(theta), np.sin(theta)])
    L = np.linalg.cholesky(M)                      # xᵀMx = ‖Lᵀx‖² = 1  ⟺  x = (Lᵀ)⁻¹ u, ‖u‖ = 1
    ellipse = np.linalg.solve(L.T, circle.T).T
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.9))
    ax = axes[0]
    axes_frame(ax, 2.6)
    ax.plot(circle[:, 0], circle[:, 1], color=C[0], lw=2)
    arrow(ax, (0, 0), (1, 0), C[1], "e₁", (0.0, -0.3))
    arrow(ax, (0, 0), (0, 1), C[2], "e₂", (-0.35, 0.0))
    ax.set_title("Produit scalaire usuel : ‖x‖ = 1 est un cercle")
    ax = axes[1]
    axes_frame(ax, 2.6)
    ax.plot(ellipse[:, 0], ellipse[:, 1], color=C[0], lw=2)
    arrow(ax, (0, 0), (1, 0), C[1], "e₁", (0.0, -0.3))
    arrow(ax, (0, 0), (-2, 1), C[3], "(−2, 1)", (-0.6, 0.25))
    arrow(ax, (0, 0), (0, 1), C[2], "e₂", (0.1, 0.1), lw=1.5, ls="--")
    ax.text(-2.45, -2.3, "e₁ et (−2, 1) : orthonormés pour ⟨·,·⟩_M\ne₂ : de norme √5, pas orthogonal à e₁",
            fontsize=9, color="0.25")
    ax.set_title("⟨x, y⟩_M = xᵀMy : ‖x‖_M = 1 est une ellipse")
    save(fig, "produit_scalaire.png")


def gram_schmidt_step() -> None:
    """One step of Gram-Schmidt in the plane: a2 minus its projection on q1 gives v2, then q2 = v2 / ‖v2‖."""
    a1, a2 = np.array([4.0, 1.0]), np.array([1.0, 3.0])
    q1 = a1 / np.linalg.norm(a1)
    proj = (a2 @ q1) * q1
    v2 = a2 - proj
    q2 = v2 / np.linalg.norm(v2)
    fig, ax = plt.subplots(figsize=(6.4, 5.0))
    ax.axhline(0, color="0.75", lw=0.8)
    ax.axvline(0, color="0.75", lw=0.8)
    t = np.linspace(-0.6, 1.3, 2)
    ax.plot(t * a1[0], t * a1[1], color=C[0], lw=0.8, alpha=0.5)
    arrow(ax, (0, 0), a1, C[0], "a₁", (0.2, -0.45))
    arrow(ax, (0, 0), a2, C[1], "", lw=2.2)
    ax.text(a2[0] + 0.1, a2[1] + 0.05, "a₂", color=C[1], fontsize=11)
    arrow(ax, (0, 0), proj, C[4], "", lw=2)
    ax.text(proj[0] - 0.1, proj[1] - 0.5, "(a₂ · q₁) q₁", color=C[4], fontsize=10)
    ax.plot([a2[0], proj[0]], [a2[1], proj[1]], color="0.4", lw=1, ls=":")
    arrow(ax, (0, 0), v2, C[3], "", lw=2.2)
    ax.text(v2[0] - 1.55, v2[1] + 0.2, "v₂ = a₂ − (a₂ · q₁) q₁", color=C[3], fontsize=10)
    arrow(ax, (0, 0), q1, "black", "q₁", (0.05, -0.4), lw=2.6)
    arrow(ax, (0, 0), q2, "black", "q₂", (-0.45, -0.05), lw=2.6)
    side = 0.22                                    # the right angle between proj and v2, at proj
    corner = [proj + side * (-q1), proj + side * (-q1) + side * q2, proj + side * q2]
    ax.plot([c[0] for c in corner], [c[1] for c in corner], color="0.4", lw=0.9)
    ax.set(xlim=(-2.5, 4.6), ylim=(-0.9, 3.4), aspect="equal")
    ax.set_title("Gram-Schmidt : retirer de a₂ sa projection sur q₁, puis normer")
    save(fig, "gram_schmidt.png")


def plane_patch(ax, q1, q2, half=4.0, color=C[0]):
    corners = [s * q1 + t * q2 for s, t in ((-half, -half), (half, -half), (half, half), (-half, half))]
    ax.add_collection3d(Poly3DCollection([corners], alpha=0.18, facecolor=color, edgecolor=color))


def arrow3(ax, start, end, color, lw=2.2, ls="-"):
    ax.quiver(*start, *(np.asarray(end) - np.asarray(start)), color=color, lw=lw, arrow_length_ratio=0.08,
              linestyle=ls)


def projection_plane() -> None:
    """The projection of v = (2, 1, 6) on U = Vect((2, 2, 1), (2, −2, 3)): p = (4, 0, 4), v − p = (−2, 1, 2)."""
    q1, q2 = np.array([2.0, 2.0, 1.0]) / 3, np.array([1.0, -2.0, 2.0]) / 3
    v, p = np.array([2.0, 1.0, 6.0]), np.array([4.0, 0.0, 4.0])
    fig = plt.figure(figsize=(6.6, 5.6))
    ax = fig.add_subplot(projection="3d")
    plane_patch(ax, q1, q2, half=5.0)
    arrow3(ax, (0, 0, 0), v, C[1])
    arrow3(ax, (0, 0, 0), p, C[4])
    ax.plot(*np.column_stack([v, p]), color=C[3], lw=2, ls="--")
    for point, text, color in ((v, "v = (2, 1, 6)", C[1]), (p, "p = (4, 0, 4)", C[4])):
        ax.text(*(point + np.array([0.2, 0.2, 0.25])), text, color=color, fontsize=10)
    ax.text(*((v + p) / 2 + np.array([-0.2, 0.3, 0.0])), "v − p ⊥ U\n‖v − p‖ = 3", color=C[3], fontsize=9)
    ax.text(*(-3.5 * q1 + 3.0 * q2), "U", color=C[0], fontsize=13)
    ax.set(xlabel="x", ylabel="y", zlabel="z", xlim=(-2, 6), ylim=(-4, 4), zlim=(-2, 7))
    ax.view_init(elev=18, azim=-62)
    ax.set_title("Le projeté p est le point de U le plus proche de v")
    save(fig, "projection_plan.png")


def least_squares() -> None:
    """Left: the data of the fiche, the fitted line 1,2 + 1,2x and the residuals. Right: ŷ = projection of y on Im X."""
    x, y = np.array([0.0, 1.0, 2.0, 3.0]), np.array([2.0, 1.0, 4.0, 5.0])
    w0, w1 = 1.2, 1.2
    fig = plt.figure(figsize=(11, 4.8))
    ax = fig.add_subplot(1, 2, 1)
    grid = np.linspace(-0.4, 3.4, 2)
    ax.plot(grid, w0 + w1 * grid, color=C[0], lw=2, label="droite ajustée : 1,2 + 1,2 x")
    for xi, yi in zip(x, y):
        ax.plot([xi, xi], [yi, w0 + w1 * xi], color=C[3], lw=1.6)
    ax.plot(x, y, "o", color=C[1], ms=7, label="données (xᵢ, yᵢ)")
    ax.plot(x, w0 + w1 * x, "s", color=C[0], ms=5, label="prédictions ŷᵢ")
    ax.plot([], [], color=C[3], lw=1.6, label="résidus yᵢ − ŷᵢ")
    ax.set(xlabel="x", ylabel="y", xlim=(-0.5, 3.5), ylim=(0, 6))
    ax.legend(loc="upper left", fontsize=9)
    ax.set_title("Vu dans le plan des données : 4 points")
    ax = fig.add_subplot(1, 2, 2, projection="3d")
    e1, e2 = np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0])
    plane_patch(ax, e1, e2, half=3.2)
    yv, yh = np.array([1.6, 1.2, 2.4]), np.array([1.6, 1.2, 0.0])
    arrow3(ax, (0, 0, 0), yv, C[1])
    arrow3(ax, (0, 0, 0), yh, C[0])
    ax.plot(*np.column_stack([yv, yh]), color=C[3], lw=2, ls="--")
    ax.text(*(yv + np.array([0.1, 0.1, 0.15])), "y", color=C[1], fontsize=12)
    ax.text(*(yh + np.array([0.15, 0.1, -0.35])), "ŷ = Xw*", color=C[0], fontsize=11)
    ax.text(*(np.array([1.75, 1.3, 1.2])), "y − ŷ ⊥ Im X", color=C[3], fontsize=10)
    ax.text(-2.8, -2.6, 0.0, "Im X", color=C[0], fontsize=12)
    ax.set(xlim=(-3, 3), ylim=(-3, 3), zlim=(0, 3), xticks=[], yticks=[], zticks=[])
    ax.view_init(elev=20, azim=-58)
    ax.set_title("Vu dans ℝⁿ (schéma) : ŷ est le projeté de y")
    save(fig, "moindres_carres.png")


def functions() -> None:
    """On [0 ; 1], x² and its projection on Vect(1, x) for ⟨f, g⟩ = ∫ f g: the line x − 1/6."""
    t = np.linspace(0, 1, 300)
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
    ax = axes[0]
    ax.plot(t, np.ones_like(t), color=C[0], lw=2, label="1")
    ax.plot(t, t, color=C[1], lw=2, ls="--", label="x")
    ax.plot(t, t - 0.5, color=C[2], lw=2, label="x − 1/2")
    ax.axhline(0, color="0.6", lw=0.8)
    ax.set(xlabel="x", xlim=(0, 1), ylim=(-0.7, 1.2))
    ax.legend(loc="lower right", fontsize=9)
    ax.set_title("⟨1, x⟩ = 1/2, mais ⟨1, x − 1/2⟩ = 0")
    ax = axes[1]
    ax.plot(t, t ** 2, color=C[1], lw=2.2, label="x²")
    ax.plot(t, t - 1 / 6, color=C[0], lw=2.2, label="son projeté sur Vect(1, x) : x − 1/6")
    ax.fill_between(t, t ** 2, t - 1 / 6, color=C[3], alpha=0.2, label="l'écart, d'intégrale du carré minimale")
    ax.axhline(0, color="0.6", lw=0.8)
    ax.set(xlabel="x", xlim=(0, 1), ylim=(-0.25, 1.05))
    ax.legend(loc="upper left", fontsize=9)
    ax.set_title("La meilleure droite pour x² au sens de ∫₀¹ (f − g)²")
    save(fig, "fonctions.png")


def main() -> int:
    print(f"figures of M12b -> {OUT.relative_to(ROOT)}")
    inner_products()
    gram_schmidt_step()
    projection_plane()
    least_squares()
    functions()
    return 0


if __name__ == "__main__":
    sys.exit(main())
