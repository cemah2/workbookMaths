#!/usr/bin/env python
"""Draw the figures of chapter M17 (used by Claude).

    python tools/chapters/figures_m17.py

Writes small PNG files into chapitres/m17_jacobienne/figures/: a small rectangle of the (r, θ) plane, its image by the
polar map (a curved quadrilateral) and by the linear approximation f(a) + J (p − a) (a parallelogram); a piecewise
linear tax with its left and right slopes, arctan and its derivative that vanishes far from 0, and the derivative of
the L-fold composition of cos, which shrinks like |cos′(x*)|^L; the populations of three energy levels (0; 0,5; 2) and
the mean energy as functions of the temperature. The numbers are those of the fiche; none comes from workbookIA 17 (no
activation, no softmax, no score, no 17xx seed).
"""

from __future__ import annotations

import math
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

OUT = ROOT / "chapitres" / "m17_jacobienne" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

POINT = (2.0, math.pi / 4)                       # §1: the point (r, θ) of the figure
DR, DTHETA = 0.4, 0.35                           # §1: the sides of the small rectangle
LEVELS = np.array([0.0, 0.5, 2.0])               # §7: three energy levels


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


def polar(r, t):
    return np.array([r * np.cos(t), r * np.sin(t)])


def linear_approximation() -> None:
    """§1: a small rectangle of the (r, θ) plane, its image by the polar map and by the linear approximation."""
    r0, t0 = POINT
    J = np.array([[math.cos(t0), -r0 * math.sin(t0)], [math.sin(t0), r0 * math.cos(t0)]])
    s = np.linspace(0, 1, 60)
    border = np.concatenate([np.column_stack([s * DR, 0 * s]), np.column_stack([DR + 0 * s, s * DTHETA]),
                             np.column_stack([(1 - s) * DR, DTHETA + 0 * s]), np.column_stack([0 * s, (1 - s) * DTHETA])])
    curved = polar(r0 + border[:, 0], t0 + border[:, 1]).T
    straight = polar(r0, t0) + border @ J.T
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    axes[0].fill(r0 + border[:, 0], t0 + border[:, 1], color=C[0], alpha=0.35)
    axes[0].plot(r0, t0, "o", color="0.2")
    axes[0].set(xlabel="r", ylabel="θ (radians)", xlim=(1.7, 2.6), ylim=(0.6, 1.3),
                title="Un petit rectangle du plan (r, θ)\nautour de a = (2, π/4)")
    axes[0].grid(alpha=0.3)
    axes[1].fill(*curved.T, color=C[0], alpha=0.35, label="son image par f(r, θ) = (r cos θ, r sin θ)")
    axes[1].plot(*straight.T, color=C[1], lw=2, ls="--", label="son image par f(a) + J (p − a), un parallélogramme")
    axes[1].plot(*polar(r0, t0), "o", color="0.2")
    for column, name in ((J[:, 0] * DR, "J (0,4 ; 0)"), (J[:, 1] * DTHETA, "J (0 ; 0,35)")):
        axes[1].annotate("", xy=polar(r0, t0) + column, xytext=polar(r0, t0),
                         arrowprops=dict(arrowstyle="->", color=C[2], lw=2))
        axes[1].text(*(polar(r0, t0) + 1.08 * column), name, color=C[2], fontsize=9)
    axes[1].set(xlabel="x", ylabel="y", aspect="equal", xlim=(0.6, 2.4), ylim=(1.0, 2.6),
                title="Son image : la jacobienne donne le parallélogramme\nqui approche le quadrilatère courbe")
    axes[1].grid(alpha=0.3)
    axes[1].legend(fontsize=8, loc="lower left")
    save(fig, "approximation_lineaire.png")


def tax(t):
    """§6: 0 up to 10, 20 % between 10 and 30, 40 % beyond (in k€)."""
    t = np.asarray(t, dtype=float)
    return np.where(t <= 10, 0.0, np.where(t <= 30, 0.2 * (t - 10), 4 + 0.4 * (t - 30)))


def compositions() -> None:
    """§6: a piecewise linear function, arctan and its derivative, the derivative of cos ∘ … ∘ cos."""
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 3.9))
    t = np.linspace(0, 45, 451)
    axes[0].plot(t, tax(t), color=C[0], lw=2)
    for corner, left, right in ((10, 0.0, 0.2), (30, 0.2, 0.4)):
        axes[0].plot(corner, tax(corner), "o", color=C[1])
        axes[0].text(corner + 0.8, float(tax(corner)) - 0.9,
                     f"pente {french_number(left)} à gauche,\n{french_number(right)} à droite", fontsize=8)
    axes[0].set(xlabel="revenu (k€)", ylabel="impôt (k€)", title="Une fonction affine par morceaux :\n"
                "deux pentes en chaque point anguleux")
    axes[0].grid(alpha=0.3)
    z = np.linspace(-8, 8, 401)
    axes[1].plot(z, np.arctan(z), color=C[0], lw=2, label="arctan t")
    axes[1].plot(z, 1 / (1 + z ** 2), color=C[1], lw=2, label="arctan′ t = 1 / (1 + t²)")
    axes[1].set(xlabel="t", title="Saturation : loin de 0, la courbe s'aplatit\net sa dérivée tend vers 0")
    axes[1].legend(fontsize=8, loc="upper left")
    axes[1].grid(alpha=0.3)
    x, derivative, values = 1.0, 1.0, []
    for _ in range(30):
        derivative *= -math.sin(x)                 # chain rule: (cos ∘ h)′ = cos′(h) h′
        x = math.cos(x)
        values.append(abs(derivative))
    star = 0.7390851332151607
    L = np.arange(1, 31)
    axes[2].semilogy(L, values, "o", color=C[0], ms=4, label="|dx_L/dx₀|, de x₀ = 1")
    axes[2].semilogy(L, values[0] * abs(math.sin(star)) ** (L - 1), color=C[1], lw=1.5,
                     label="pente |cos′(x*)|^L ≈ 0,674^L")
    axes[2].set(xlabel="nombre L de compositions", ylabel="échelle log",
                title="La dérivée de cos ∘ cos ∘ ⋯ ∘ cos (L fois) :\nun produit de L facteurs, qui s'éteint")
    axes[2].legend(fontsize=8)
    axes[2].grid(alpha=0.3, which="both")
    save(fig, "morceaux_et_compositions.png")


def boltzmann() -> None:
    """§7: populations of three energy levels and mean energy, as functions of the temperature."""
    T = np.logspace(-1.5, 2, 300)
    weights = np.exp(-LEVELS[None, :] / T[:, None])
    p = weights / weights.sum(axis=1, keepdims=True)
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))
    for k, color in zip(range(3), C):
        axes[0].semilogx(T, p[:, k], color=color, lw=2, label=f"niveau E = {french_number(LEVELS[k])}")
    axes[0].axhline(1 / 3, color="0.5", ls=":", lw=1)
    axes[0].set(xlabel="température T (échelle log)", ylabel="population pᵢ",
                title="Populations : tout sur le niveau le plus bas quand T → 0,\nuniformes (1/3) quand T → ∞")
    axes[0].legend(fontsize=8)
    axes[0].grid(alpha=0.3)
    axes[1].semilogx(T, p @ LEVELS, color=C[0], lw=2, label="énergie moyenne Σ pᵢ Eᵢ")
    axes[1].axhline(LEVELS.mean(), color=C[1], ls="--", lw=1.5, label="moyenne des niveaux, 5/6")
    axes[1].set(xlabel="température T (échelle log)", ylabel="énergie moyenne",
                title="L'énergie moyenne croît avec T,\nde l'énergie la plus basse à la moyenne des niveaux")
    axes[1].legend(fontsize=8, loc="upper left")
    axes[1].grid(alpha=0.3)
    save(fig, "boltzmann.png")


def main() -> int:
    print(f"Figures of M17 into {OUT.relative_to(ROOT)}:")
    linear_approximation()
    compositions()
    boltzmann()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
