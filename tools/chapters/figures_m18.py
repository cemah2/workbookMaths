#!/usr/bin/env python
"""Draw the figures of chapter M18 (used by Claude).

    python tools/chapters/figures_m18.py

Writes small PNG files into chapitres/m18_retropropagation/figures/: the computation graph of the height of a
projectile, y = v t sin θ − 5 t², with the values of the forward pass, the local derivatives on the edges and the
adjoints of the reverse pass; the parallelogram spanned by the columns of a 2 × 2 matrix and the gradient of its
determinant with respect to each column (the other column turned a quarter turn); a check of the gradient of
ln det X along a direction, where the transposed gradient is caught by a direction that is not symmetric and missed by
a symmetric one. The numbers are those of the fiche; none comes from workbookIA 18 (no network, no loss, no delta, no
18xx seed). No randomness.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m18_retropropagation" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

V, THETA, T = 20.0, math.pi / 6, 0.5              # §1 to §4: the point of the projectile
DET_X = np.array([[3.0, 1.0], [2.0, 4.0]])        # §6: the matrix whose determinant is differentiated
LOGDET_X = np.array([[2.0, 1.0], [0.5, 3.0]])     # §8: the point of the check of ln det X
H_RANDOM = np.array([[1.0, -1.0], [1.0, 0.5]])    # §8: a direction that is not symmetric
H_SYMMETRIC = np.array([[1.0, 0.5], [0.5, -1.0]])  # §8: a symmetric direction


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def fr(value: float, digits: int = 3) -> str:
    """A number rounded to `digits` decimals, written the French way."""
    return f"{round(value, digits):g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and ax.axison:
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def projectile_graph() -> None:
    """§1 to §4: the computation graph of y = v t sin θ − 5 t², forward values, local derivatives, adjoints."""
    u1, u2, u4 = math.sin(THETA), V * T, T ** 2
    u3, u5 = u2 * u1, 5 * u4
    y = u3 - u5
    adj = {"y": 1.0, "u3": 1.0, "u5": -1.0}
    adj["u4"] = adj["u5"] * 5
    adj["u2"] = adj["u3"] * u1
    adj["u1"] = adj["u3"] * u2
    adj["t"] = adj["u2"] * V + adj["u4"] * 2 * T
    adj["v"] = adj["u2"] * T
    adj["theta"] = adj["u1"] * math.cos(THETA)
    nodes = {
        "theta": ((0.0, 2.6), "θ", "π/6", adj["theta"], "ū = 5√3"),
        "v": ((0.0, 1.3), "v", fr(V), adj["v"], None),
        "t": ((0.0, 0.0), "t", fr(T), adj["t"], None),
        "u1": ((2.9, 2.6), "u₁ = sin θ", fr(u1), adj["u1"], None),
        "u2": ((2.9, 1.3), "u₂ = v · t", fr(u2), adj["u2"], None),
        "u4": ((2.9, 0.0), "u₄ = t²", fr(u4), adj["u4"], None),
        "u3": ((5.8, 1.95), "u₃ = u₂ · u₁", fr(u3), adj["u3"], None),
        "u5": ((5.8, 0.0), "u₅ = 5 u₄", fr(u5), adj["u5"], None),
        "y": ((8.4, 1.0), "y = u₃ − u₅", fr(y), adj["y"], None),
    }
    edges = {("theta", "u1"): "cos θ ≈ 0,866", ("v", "u2"): "t = 0,5", ("t", "u2"): "v = 20",
             ("t", "u4"): "2t = 1", ("u1", "u3"): "u₂ = 10", ("u2", "u3"): "u₁ = 0,5", ("u4", "u5"): "5",
             ("u3", "y"): "1", ("u5", "y"): "−1"}
    fig, ax = plt.subplots(figsize=(12.5, 5.4))
    width, height = 1.3, 0.62
    for (a, b), label in edges.items():
        start, end = np.array(nodes[a][0]), np.array(nodes[b][0])
        arrow = FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=15, color=C[0], lw=1.5,
                                shrinkA=40, shrinkB=40)
        ax.add_patch(arrow)
        mid = start + 0.5 * (end - start)
        ax.text(*mid, label, fontsize=9, ha="center", va="center", color=C[0],
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))
    for key, ((x, yy), name, value, adjoint, shown) in nodes.items():
        box = FancyBboxPatch((x - width / 2, yy - height / 2), width, height, boxstyle="round,pad=0.04",
                             fc="white", ec="0.25", lw=1.3, zorder=3)
        ax.add_patch(box)
        ax.text(x, yy + 0.12, name, ha="center", va="center", fontsize=10, zorder=4)
        ax.text(x, yy - 0.15, f"= {value}", ha="center", va="center", fontsize=10, color=C[1], zorder=4)
        ax.text(x, yy - 0.5, shown or f"ū = {fr(adjoint)}", ha="center", va="center", fontsize=10, color=C[2],
                fontweight="bold", zorder=4)
    ax.text(-0.7, -1.1, "valeur (passe avant)", color=C[1], fontsize=10, ha="left")
    ax.text(2.2, -1.1, "dérivée locale ∂w/∂u (sur l'arête u → w)", color=C[0], fontsize=10, ha="left")
    ax.text(6.4, -1.1, "adjoint ū = ∂y/∂u (passe arrière)", color=C[2], fontsize=10, ha="left", fontweight="bold")
    ax.set(xlim=(-0.9, 9.3), ylim=(-1.3, 3.1))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Le graphe de calcul de y = v t sin θ − 5 t² en (v, θ, t) = (20 ; π/6 ; 0,5)", fontsize=11)
    save(fig, "graphe_projectile.png")


def determinant_gradient() -> None:
    """§6: the parallelogram of the columns of X and the gradient of det X with respect to each column."""
    c1, c2 = DET_X[:, 0], DET_X[:, 1]
    grad = np.array([[DET_X[1, 1], -DET_X[1, 0]], [-DET_X[0, 1], DET_X[0, 0]]])   # the cofactor matrix
    g1, g2 = grad[:, 0], grad[:, 1]
    fig, ax = plt.subplots(figsize=(6.4, 5.6))
    ax.add_patch(Polygon([(0, 0), c1, c1 + c2, c2], closed=True, fc=C[0], alpha=0.15, ec=C[0], lw=1.2))
    for vec, start, color, label, where in (
            (c1, (0, 0), C[0], "c₁ = (3 ; 2)", (1.7, 0.45)),
            (c2, (0, 0), C[0], "c₂ = (1 ; 4)", (-1.55, 2.2)),
            (0.5 * g1, c1, C[1], "½ ∂det/∂c₁ = ½ (4 ; −1)", (3.35, 2.3)),
            (0.5 * g2, c2, C[2], "½ ∂det/∂c₂ = ½ (−2 ; 3)", (-2.2, 5.85))):
        start = np.array(start, dtype=float)
        ax.add_patch(FancyArrowPatch(start, start + vec, arrowstyle="-|>", mutation_scale=16, color=color, lw=2))
        ax.text(*where, label, color=color, fontsize=10)
    ax.text(1.6, 2.9, "aire = det X = 10", fontsize=10, ha="center")
    ax.plot([0, c2[0]], [0, c2[1]], color=C[0], lw=0)
    ax.set(xlim=(-2.5, 6.2), ylim=(-1.2, 7.4), xlabel="première coordonnée", ylabel="seconde coordonnée")
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    ax.set_title("X = [[3, 1], [2, 4]] : le gradient de det X par rapport à une colonne\n"
                 "est l'autre colonne tournée d'un quart de tour (perpendiculaire à elle)", fontsize=10)
    save(fig, "gradient_determinant.png")


def direction_check() -> None:
    """§8: ln det(X + s H) and two tangents at 0, for a direction H that is not symmetric and for a symmetric one."""
    G = np.linalg.inv(LOGDET_X).T          # the gradient of ln det X
    wrong = G.T                            # a transposed gradient
    s = np.linspace(-0.6, 0.6, 241)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), sharey=False)
    for ax, H, title in ((axes[0], H_RANDOM, "H = [[1, −1], [1, 0,5]], pas symétrique : le gradient transposé est démasqué"),
                         (axes[1], H_SYMMETRIC, "H = [[1, 0,5], [0,5, −1]], symétrique : il passe inaperçu")):
        phi = np.array([np.log(np.linalg.det(LOGDET_X + si * H)) for si in s])
        base = math.log(np.linalg.det(LOGDET_X))
        good, bad = float(np.sum(G * H)), float(np.sum(wrong * H))
        ax.plot(s, phi, color=C[0], lw=2.2, label="φ(s) = ln det(X + s H)")
        ax.plot(s, base + good * s, color=C[2], lw=1.6, ls="--", label=f"pente tr(Gᵀ H) ≈ {fr(good)} (G juste)")
        ax.plot(s, base + bad * s, color=C[1], lw=1.6, ls=":", label=f"pente avec Gᵀ à la place de G ≈ {fr(bad)}")
        ax.axvline(0, color="0.6", lw=0.8)
        ax.set(xlabel="s", ylabel="φ(s)")
        ax.set_title(title, fontsize=9)
        ax.legend(fontsize=8.5, loc="lower right")
        ax.grid(alpha=0.3)
    fig.suptitle("Vérifier le gradient G = X⁻ᵀ de ln det X en X = [[2, 1], [0,5, 3]] le long d'une direction H",
                 fontsize=11)
    save(fig, "verification_direction.png")


def main() -> int:
    print(f"Figures M18 → {OUT.relative_to(ROOT)}")
    projectile_graph()
    determinant_gradient()
    direction_check()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
