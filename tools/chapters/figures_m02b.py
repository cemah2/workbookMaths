#!/usr/bin/env python
"""Draw the figures of chapter M02b (used by Claude).

    python tools/chapters/figures_m02b.py

Writes small PNG files into chapitres/m02b_variables_aleatoires/figures/: two cumulative distribution functions (a die
and the uniform law on [0, 1]), three discrete laws (binomial B(6 ; 0,2), geometric of parameter 1/6, Poisson of
parameter 3), the binomial B(100 ; 0,03) next to the Poisson law of parameter 3, three continuous laws (the uniform
law on [0, 12], the exponential law of parameter 3, the normal law N(505, 5²)), four normal densities and Φ as an area,
the mean and the median of an exponential law, a joint law with its margins, the density of a sum of two independent
normal durations, a double integral as a volume and the polar area element, the law of Z², and sampling by inversion.
Every figure is computed and uses the workbook style (wbm.plot colours, French decimal commas). The laws are those of
the sheet's own examples: none comes from workbookIA 2 (its normal laws, its wheel, its animals), from R8 or from an
exercise of M02b.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Wedge  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy import stats  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m02b_variables_aleatoires" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


def french(value: float, digits: int = 4) -> str:
    """A number with a French decimal comma: 0,3935."""
    return f"{value:.{digits}f}".replace(".", ",")


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        if getattr(ax, "keep_labels", False):
            continue
        for axis in (ax.xaxis, ax.yaxis, *([ax.zaxis] if ax.name == "3d" else [])):
            if axis.get_scale() == "linear":
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def grid(ax) -> None:
    ax.grid(True, alpha=0.25)


def fig_cdf() -> None:
    """The CDF of a fair die (a staircase) and of the uniform law on [0, 1] (a ramp)."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.3))
    ax = axes[0]
    for k in range(0, 7):
        ax.hlines(k / 6, k, k + 1 if k < 6 else 7.5, color=C[0], linewidth=2)
        if 1 <= k <= 6:
            ax.plot(k, k / 6, "o", color=C[0], markersize=5)                      # the value at k is reached
            ax.plot(k, (k - 1) / 6, "o", color="white", markeredgecolor=C[0], markersize=5)
    ax.hlines(0, -1, 0, color=C[0], linewidth=2)
    ax.set(xlim=(-0.8, 7.5), ylim=(-0.05, 1.08), xlabel="x", ylabel="F(x) = P(X ≤ x)",
           title="Un dé équilibré : une fonction en escalier")
    ax.set_yticks([0, 1 / 6, 2 / 6, 3 / 6, 4 / 6, 5 / 6, 1])
    ax.set_yticklabels(["0", "1/6", "2/6", "3/6", "4/6", "5/6", "1"])
    ax.keep_labels = True                     # fractions on the y-axis: no French decimal formatter here
    grid(ax)
    ax = axes[1]
    xs = np.linspace(-0.5, 1.5, 300)
    ax.plot(xs, np.clip(xs, 0, 1), color=C[1], linewidth=2)
    ax.set(xlim=(-0.5, 1.5), ylim=(-0.05, 1.08), xlabel="x", ylabel="F(x) = P(X ≤ x)",
           title="La loi uniforme sur [0 ; 1] : une rampe continue")
    grid(ax)
    save(fig, "repartition.png")


def fig_discrete() -> None:
    """B(6 ; 0,2), the geometric law of parameter 1/6 and the Poisson law of parameter 3."""
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.3))
    ks = np.arange(0, 7)
    axes[0].bar(ks, stats.binom(6, 0.2).pmf(ks), color=C[0], width=0.6)
    axes[0].set(title="Binomiale B(6 ; 0,2)", xlabel="k", ylabel="P(X = k)")
    ks = np.arange(1, 21)
    axes[1].bar(ks, stats.geom(1 / 6).pmf(ks), color=C[1], width=0.6)
    axes[1].set(title="Géométrique, p = 1/6 (jusqu'au premier 6)", xlabel="k")
    ks = np.arange(0, 11)
    axes[2].bar(ks, stats.poisson(3).pmf(ks), color=C[2], width=0.6)
    axes[2].set(title="Poisson de paramètre 3", xlabel="k")
    for ax in axes:
        grid(ax)
    save(fig, "lois_discretes.png")


def fig_poisson_binomial() -> None:
    """B(100 ; 0,03) and the Poisson law of parameter 3, side by side: almost the same bars."""
    ks = np.arange(0, 11)
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.bar(ks - 0.2, stats.binom(100, 0.03).pmf(ks), width=0.4, color=C[0], label="binomiale B(100 ; 0,03)")
    ax.bar(ks + 0.2, stats.poisson(3).pmf(ks), width=0.4, color=C[2], label="Poisson de paramètre 3")
    ax.set(xlabel="k", ylabel="P(X = k)", title="Beaucoup d'essais, un succès rare : la loi de Poisson")
    ax.set_xticks(ks)
    ax.legend()
    grid(ax)
    save(fig, "poisson_binomiale.png")


def fig_continuous() -> None:
    """U[0 ; 12] with P(W > 8), the exponential law of parameter 3 with P(T > 1), N(505, 5²) with P(X < 500)."""
    fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.3))
    ax = axes[0]
    xs = np.linspace(-2, 14, 600)
    ys = np.where((xs >= 0) & (xs <= 12), 1 / 12, 0)
    ax.plot(xs, ys, color="black", linewidth=1.6)
    ax.fill_between(xs, ys, where=xs >= 8, color=C[0], alpha=0.35, label="P(W > 8) = 1/3")
    ax.set(title="Uniforme sur [0 ; 12]", xlabel="w (minutes)", ylim=(0, 0.12))
    ax.legend(loc="upper left", fontsize=9)
    ax = axes[1]
    ts = np.linspace(0, 2, 400)
    ax.plot(ts, 3 * np.exp(-3 * ts), color="black", linewidth=1.6)
    ax.fill_between(ts, 3 * np.exp(-3 * ts), where=ts >= 1, color=C[1], alpha=0.5,
                    label=f"P(T > 1) = e⁻³ ≈ {french(math.exp(-3))}")
    ax.set(title="Exponentielle, λ = 3", xlabel="t (heures)", ylim=(0, 3.2))
    ax.legend(fontsize=9)
    ax = axes[2]
    xs = np.linspace(485, 525, 500)
    pdf = stats.norm(505, 5).pdf(xs)
    ax.plot(xs, pdf, color="black", linewidth=1.6)
    ax.fill_between(xs, pdf, where=xs <= 500, color=C[2], alpha=0.4,
                    label=f"P(X < 500) = Φ(−1) ≈ {french(stats.norm.cdf(-1))}")
    ax.axvline(505, color="gray", linestyle=":", linewidth=1)
    ax.set(title="Normale N(505, 5²)", xlabel="x (grammes)", ylim=(0, 0.095))
    ax.legend(loc="upper left", fontsize=9)
    for ax in axes:
        grid(ax)
    save(fig, "lois_continues.png")


def fig_normals() -> None:
    """Four normal densities (what μ and σ change), and Φ(1) as the area under φ to the left of 1."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.4))
    ax = axes[0]
    xs = np.linspace(-6, 6, 600)
    for (mu, sigma), colour in zip([(0, 1), (2.5, 1), (0, 0.6), (-1.5, 1.5)], C):
        label = f"N({french_number(mu)}, {french_number(sigma)}²)"
        ax.plot(xs, stats.norm(mu, sigma).pdf(xs), color=colour, linewidth=1.8, label=label)
    ax.set(title="μ déplace la cloche, σ l'élargit", xlabel="x")
    ax.legend(fontsize=9)
    grid(ax)
    ax = axes[1]
    zs = np.linspace(-4, 4, 600)
    phi = stats.norm.pdf(zs)
    ax.plot(zs, phi, color="black", linewidth=1.6, label="φ, la densité de N(0, 1)")
    ax.fill_between(zs, phi, where=zs <= 1, color=C[0], alpha=0.35,
                    label=f"Φ(1) = P(Z ≤ 1) ≈ {french(stats.norm.cdf(1))}")
    for z in (-1, 1):
        ax.plot([z], [stats.norm.pdf(z)], "o", color=C[1], markersize=5)
    ax.annotate("points d'inflexion\nen −1 et 1", xy=(-1, stats.norm.pdf(-1)), xytext=(-3.9, 0.33), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="gray"))
    ax.set(title="Φ(z) : l'aire sous φ à gauche de z", xlabel="z", ylim=(0, 0.56))
    ax.legend(loc="upper right", fontsize=9)
    grid(ax)
    save(fig, "normales.png")


def fig_mean_median() -> None:
    """The exponential law of parameter 3: its median ln 2 / 3 and its mean 1/3, the centre of gravity."""
    ts = np.linspace(0, 1.6, 400)
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    ax.plot(ts, 3 * np.exp(-3 * ts), color="black", linewidth=1.6, label="densité 3e⁻³ᵗ")
    median, mean = math.log(2) / 3, 1 / 3
    ax.fill_between(ts, 3 * np.exp(-3 * ts), where=ts <= median, color=C[0], alpha=0.3,
                    label="la moitié de l'aire, à gauche de la médiane")
    ax.axvline(median, color=C[0], linestyle="--", linewidth=1.5, label=f"médiane ln 2/3 ≈ {french(median, 3)}")
    ax.axvline(mean, color=C[1], linewidth=2, label=f"espérance 1/3 ≈ {french(mean, 3)}")
    ax.plot([mean], [0], marker="^", color=C[1], markersize=12, clip_on=False)
    ax.set(xlabel="t (heures)", title="Espérance et médiane d'une loi asymétrique", ylim=(0, 3.2))
    ax.legend(fontsize=9)
    grid(ax)
    save(fig, "esperance_mediane.png")


JOINT = np.array([[0.20, 0.10], [0.15, 0.25], [0.05, 0.25]])   # rows: X = 0, 1, 2 ; columns: Y = 0, 1


def fig_joint() -> None:
    """The joint law of (X, Y) of the sheet (§5), as a heat map, with its two margins on the edges."""
    fig = plt.figure(figsize=(6.2, 4.6))
    gs = fig.add_gridspec(2, 2, width_ratios=(4, 1.3), height_ratios=(1.3, 4), wspace=0.08, hspace=0.08)
    ax = fig.add_subplot(gs[1, 0])
    ax_top = fig.add_subplot(gs[0, 0], sharex=ax)
    ax_right = fig.add_subplot(gs[1, 1], sharey=ax)
    image = ax.imshow(JOINT.T, origin="lower", cmap="Blues", vmin=0, vmax=0.3, aspect="auto")
    for x in range(3):
        for y in range(2):
            ax.text(x, y, french(JOINT[x, y], 2), ha="center", va="center", fontsize=12,
                    color="white" if JOINT[x, y] > 0.18 else "black")
    ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["0 (pluie)", "1 (beau)"])
    ax.set(xlabel="X : glaces vendues (centaines)", ylabel="Y : météo")
    ax_top.bar([0, 1, 2], JOINT.sum(axis=1), color=C[0], width=0.6)
    for x, p in enumerate(JOINT.sum(axis=1)):
        ax_top.text(x, p + 0.02, french(p, 2), ha="center", fontsize=9)
    ax_top.set(ylim=(0, 0.6), title="Loi jointe et lois marginales")
    ax_top.tick_params(labelbottom=False)
    ax_right.barh([0, 1], JOINT.sum(axis=0), color=C[1], height=0.6)
    for y, p in enumerate(JOINT.sum(axis=0)):
        ax_right.text(p + 0.02, y, french(p, 2), va="center", fontsize=9)
    ax_right.set(xlim=(0, 0.9))
    ax_right.tick_params(labelleft=False)
    fig.colorbar(image, ax=[ax, ax_right], fraction=0.04, pad=0.02, label="P(X = x, Y = y)")
    save(fig, "loi_jointe.png")


def fig_sum() -> None:
    """Two independent normal durations, N(20, 3²) and N(35, 4²), and their sum N(55, 5²): σ = 5, not 7."""
    xs = np.linspace(5, 80, 600)
    fig, ax = plt.subplots(figsize=(7, 3.2))
    for (mu, sigma, label), colour in zip([(20, 3, "bus : N(20, 3²)"), (35, 4, "train : N(35, 4²)"),
                                          (55, 5, "total : N(55, 5²)")], C):
        ax.plot(xs, stats.norm(mu, sigma).pdf(xs), color=colour, linewidth=1.8, label=label)
    ax.plot(xs, stats.norm(55, 7).pdf(xs), color="gray", linestyle=":", linewidth=1.5,
            label="ce que donnerait σ = 3 + 4 = 7 (faux)")
    ax.set(xlabel="durée (minutes)", title="Variances qui s'additionnent : 3² + 4² = 5²")
    ax.legend(fontsize=9)
    grid(ax)
    save(fig, "somme.png")


def fig_double_integral() -> None:
    """The volume under z = x + y over [0, 1] × [0, 2] (its value is 3), and the polar area element r dr dθ."""
    fig = plt.figure(figsize=(11, 4.2))
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    xs, ys = np.meshgrid(np.linspace(0, 1, 21), np.linspace(0, 2, 41))
    ax.plot_surface(xs, ys, xs + ys, cmap="Blues", alpha=0.8, edgecolor="none")
    for x0, y0 in [(0, 0), (1, 0), (0, 2), (1, 2)]:
        ax.plot([x0, x0], [y0, y0], [0, x0 + y0], color="gray", linewidth=1)
    ax.plot([0, 1, 1, 0, 0], [0, 0, 2, 2, 0], [0, 0, 0, 0, 0], color="black", linewidth=1.2)
    ax.set(xlabel="x", ylabel="y", zlabel="z = x + y", title="Le volume sous z = x + y : 3")
    ax.view_init(elev=22, azim=-60)
    ax = fig.add_subplot(1, 2, 2)
    for r in np.arange(0.5, 3.01, 0.5):
        ax.add_patch(plt.Circle((0, 0), r, fill=False, color="lightgray", linewidth=0.8))
    for theta in np.linspace(0, 2 * np.pi, 13)[:-1]:
        ax.plot([0, 3 * np.cos(theta)], [0, 3 * np.sin(theta)], color="lightgray", linewidth=0.8)
    r0, dr, t0, dt = 2.0, 0.5, np.pi / 6, np.pi / 6
    ax.add_patch(Wedge((0, 0), r0 + dr, np.degrees(t0), np.degrees(t0 + dt), width=dr, color=C[0], alpha=0.6))
    ax.annotate("dr", xy=((r0 + dr / 2) * np.cos(t0) + 0.05, (r0 + dr / 2) * np.sin(t0) - 0.25), fontsize=11)
    ax.annotate("r dθ", xy=((r0 + dr) * np.cos(t0 + dt / 2) + 0.08, (r0 + dr) * np.sin(t0 + dt / 2)), fontsize=11)
    ax.annotate("θ", xy=(0.55, 0.12), fontsize=11)
    ax.set(xlim=(-3.2, 3.2), ylim=(-3.2, 3.2), aspect="equal", xlabel="x", ylabel="y",
           title="Un petit « rectangle » polaire : aire ≈ r dr dθ")
    save(fig, "integrale_double.png")


def fig_square_law() -> None:
    """Z² for Z ~ N(0, 1): a histogram of 100 000 draws and the density e^(−y/2) / √(2πy)."""
    rng = np.random.default_rng(3)
    ys = rng.standard_normal(100_000) ** 2
    grid_y = np.linspace(0.02, 6, 400)
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    ax.hist(ys, bins=np.linspace(0, 6, 61), density=True, color=C[0], alpha=0.45, label="100 000 tirages de Z²")
    ax.plot(grid_y, np.exp(-grid_y / 2) / np.sqrt(2 * np.pi * grid_y), color="black", linewidth=1.6,
            label="densité e^(−y/2) / √(2πy)")
    ax.set(xlabel="y", ylim=(0, 1.4), title="La loi de Z² : une densité qui explose en 0")
    ax.legend(fontsize=9)
    grid(ax)
    save(fig, "loi_du_carre.png")


def fig_inversion() -> None:
    """Sampling by inversion: u on the vertical axis, x = F⁻¹(u) on the horizontal axis; then 100 000 draws."""
    lam = 3
    ts = np.linspace(0, 1.6, 400)
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.4))
    ax = axes[0]
    ax.plot(ts, 1 - np.exp(-lam * ts), color="black", linewidth=1.6, label="F(t) = 1 − e⁻³ᵗ")
    for u, colour in [(0.5, C[0]), (0.9, C[1])]:
        x = -math.log(1 - u) / lam
        ax.annotate("", xy=(x, u), xytext=(0, u), arrowprops=dict(arrowstyle="->", color=colour, linewidth=1.5))
        ax.annotate("", xy=(x, 0), xytext=(x, u), arrowprops=dict(arrowstyle="->", color=colour, linewidth=1.5))
        ax.text(0.02, u + 0.03, f"u = {french(u, 1)}", color=colour, fontsize=9)
        ax.text(x + 0.02, 0.04, f"F⁻¹(u) ≈ {french(x, 3)}", color=colour, fontsize=9)
    ax.set(xlabel="t (heures)", ylabel="u", ylim=(0, 1.05), title="Inverser F : de u uniforme à une valeur de T")
    ax.legend(loc="center right", fontsize=9)
    grid(ax)
    ax = axes[1]
    u = np.random.default_rng(0).random(100_000)
    draws = -np.log(1 - u) / lam
    ax.hist(draws, bins=np.linspace(0, 1.6, 65), density=True, color=C[0], alpha=0.45,
            label="100 000 valeurs −ln(1 − u)/3")
    ax.plot(ts, lam * np.exp(-lam * ts), color="black", linewidth=1.6, label="densité 3e⁻³ᵗ")
    ax.set(xlabel="t (heures)", title="Les tirages suivent la loi exponentielle")
    ax.legend(fontsize=9)
    grid(ax)
    save(fig, "inversion.png")


def main() -> int:
    print(f"Figures de M02b dans {OUT.relative_to(ROOT)} :")
    fig_cdf()
    fig_discrete()
    fig_poisson_binomial()
    fig_continuous()
    fig_normals()
    fig_mean_median()
    fig_joint()
    fig_sum()
    fig_double_integral()
    fig_square_law()
    fig_inversion()
    return 0


if __name__ == "__main__":
    sys.exit(main())
