#!/usr/bin/env python
"""Draw the figures of chapter M09b (used by Claude).

    python tools/chapters/figures_m09b.py

Writes small PNG files into chapitres/m09b_moindres_carres/figures/: least squares as the orthogonal projection of y
onto the plane of the columns of X, the three losses r²/2, |r| and Huber, and the penalties w² and |w| with their
slopes. None comes from workbookIA 9 (no L1 and L2 balls with ellipses, no penalized weight against z, no coefficient
path, no fits of increasing degree, no double descent curve).
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

OUT = ROOT / "chapitres" / "m09b_moindres_carres" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


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


def projection() -> None:
    """y, its projection ŷ on the plane spanned by two columns (here the floor z = 0), and the vertical residual."""
    a1, a2 = np.array([2.0, 0.0, 0.0]), np.array([0.6, 2.0, 0.0])
    y = np.array([1.6, 1.4, 1.8])
    y_hat = np.array([1.6, 1.4, 0.0])
    fig = plt.figure(figsize=(6.6, 5.6))
    ax = fig.add_subplot(projection="3d")
    s, t = np.meshgrid(np.linspace(-0.2, 1.2, 2), np.linspace(-0.2, 1.1, 2))
    plane = s[..., None] * a1 + t[..., None] * a2
    ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], color=C[0], alpha=0.15, edgecolor="none")

    def vec(start, end, color, label, shift, lw=2.2, ls="-"):
        ax.quiver(*start, *(np.asarray(end) - np.asarray(start)), color=color, lw=lw, linestyle=ls,
                  arrow_length_ratio=0.08)
        ax.text(*(np.asarray(end) + np.asarray(shift)), label, color=color, fontsize=11)

    origin = np.zeros(3)
    vec(origin, a1, C[0], "colonne 1", (-0.9, -0.3, 0.0), lw=1.6)
    vec(origin, a2, C[0], "colonne 2", (-0.35, 0.1, 0.05), lw=1.6)
    vec(origin, y, "black", "y", (0.05, 0.05, 0.08))
    vec(origin, y_hat, C[1], "ŷ = Hy", (0.08, 0.05, -0.25))
    vec(y_hat, y, C[3], "r = y − ŷ", (0.08, 0.0, -0.9), ls="--")
    # a small right-angle mark at the foot of the perpendicular
    d = 0.18
    u = -y_hat / np.linalg.norm(y_hat)
    corner = [y_hat + d * u, y_hat + d * u + np.array([0, 0, d]), y_hat + np.array([0, 0, d])]
    ax.plot(*np.array(corner).T, color="gray", lw=1)
    ax.text(1.3, 2.1, 0.0, "plan des colonnes de X", color=C[0], fontsize=9)
    ax.set(xlim=(-0.2, 2.4), ylim=(-0.4, 2.2), zlim=(0, 2), xticks=[], yticks=[], zticks=[])
    ax.view_init(elev=18, azim=-62)
    ax.set_title("Les moindres carrés : ŷ est la projection orthogonale de y\nsur le plan des colonnes de X",
                 fontsize=11)
    save(fig, "projection.png")


def huber() -> None:
    """r²/2, |r| and the Huber loss with δ = 1, which glue at |r| = δ."""
    r = np.linspace(-3, 3, 601)
    delta = 1.0
    hub = np.where(np.abs(r) <= delta, 0.5 * r ** 2, delta * (np.abs(r) - 0.5 * delta))
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.plot(r, 0.5 * r ** 2, color=C[0], lw=2, label="r²/2 (moindres carrés)")
    ax.plot(r, np.abs(r), color=C[2], lw=2, label="|r| (valeur absolue)")
    ax.plot(r, hub, color=C[3], lw=3, ls="--", label="Huber, δ = 1")
    for side in (-delta, delta):
        ax.axvline(side, color="gray", lw=0.8, ls=":")
        ax.plot(side, 0.5, "o", color=C[3], ms=6)
    ax.annotate("en |r| = δ : même valeur\net même pente", xy=(1, 0.5), xytext=(1.3, 0.12), fontsize=9, color="gray",
                arrowprops={"arrowstyle": "->", "color": "gray"})
    ax.set(xlim=(-3, 3), ylim=(0, 4.5), xlabel="résidu r", ylabel="loss",
           title="Huber : quadratique sous δ, linéaire au-dessus")
    ax.axhline(0, color="gray", lw=0.6)
    ax.legend(fontsize=9, loc="upper center")
    ax.grid(alpha=0.3)
    save(fig, "huber.png")


def penalties() -> None:
    """(a) the penalties w² and |w|; (b) their slopes 2w and the sign of w, which jumps at 0."""
    w = np.linspace(-1.5, 1.5, 301)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 3.9))
    ax1.plot(w, w ** 2, color=C[0], lw=2.2, label="w² (L2)")
    ax1.plot(w, np.abs(w), color=C[3], lw=2.2, label="|w| (L1)")
    ax1.set(xlim=(-1.5, 1.5), ylim=(-0.1, 2.3), xlabel="w", title="(a) les deux pénalités")
    ax1.legend(fontsize=9, loc="upper center")
    ax2.plot(w, 2 * w, color=C[0], lw=2.2, label="pente de w² : 2w")
    neg, pos = w[w < 0], w[w > 0]
    ax2.plot(neg, -np.ones_like(neg), color=C[3], lw=2.2, label="pente de |w| : −1 ou 1")
    ax2.plot(pos, np.ones_like(pos), color=C[3], lw=2.2)
    ax2.plot([0, 0], [-1, 1], "o", color=C[3], mfc="white", ms=7)
    ax2.annotate("en 0, la pente de w²\nest nulle ; celle de |w|\nne tend pas vers 0", xy=(0, 0), xytext=(0.2, -2.9),
                 fontsize=9, color="gray", arrowprops={"arrowstyle": "->", "color": "gray"})
    ax2.set(xlim=(-1.5, 1.5), ylim=(-3.1, 3.1), xlabel="w", title="(b) leurs pentes")
    ax2.legend(fontsize=9, loc="upper left")
    for ax in (ax1, ax2):
        ax.axhline(0, color="gray", lw=0.6)
        ax.axvline(0, color="gray", lw=0.6)
        ax.grid(alpha=0.3)
    save(fig, "penalites.png")


def main() -> int:
    print(f"Figures of M09b in {OUT.relative_to(ROOT)}:")
    projection()
    huber()
    penalties()
    return 0


if __name__ == "__main__":
    sys.exit(main())
