#!/usr/bin/env python
"""Draw the figures of chapter M02c (used by Claude).

    python tools/chapters/figures_m02c.py

Writes small PNG files into chapitres/m02c_echantillons_estimation/figures/: the nine training durations of the sheet
with their box and their outlier, the law of large numbers on a Monte Carlo estimate with Chebyshev's bound, the
central limit theorem on a very skewed discrete law, the two variance estimators on samples of 5 normal values,
50 confidence intervals and the ones that miss, the bootstrap distribution of a median, the signs of the products of
deviations behind a covariance, the effect of imputing by the mean, and the volume of the cube near its border in high
dimension. Every figure is computed and uses the workbook style (wbm.plot colours, French decimal commas). The data
are those of the sheet's own examples: none comes from workbookIA 2 (its request times, its series 2, 4, 4, 4, 5, 5, 7,
9, its commuters, its six scatter plots, its MNIST distances) or from an exercise of M02c.
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
from scipy import stats  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m02c_echantillons_estimation" / "figures"
C = wbplot.CATEGORICAL
DPI = 110
DURATIONS = np.array([14, 11, 13, 16, 12, 15, 13, 38, 12])


def french(value: float, digits: int = 2) -> str:
    return f"{value:.{digits}f}".replace(".", ",")


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        if getattr(ax, "keep_labels", False):
            continue
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear":
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def grid(ax) -> None:
    ax.grid(True, alpha=0.25)


def fig_box() -> None:
    """The nine durations: points, mean and median, box from Q1 to Q3, Tukey's fences and the outlier 38."""
    q1, med, q3 = np.percentile(DURATIONS, [25, 50, 75])
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    fig, ax = plt.subplots(figsize=(8, 2.8))
    ax.add_patch(plt.Rectangle((q1, -0.25), q3 - q1, 0.5, fill=True, alpha=0.25, color=C[0]))
    ax.plot([med, med], [-0.25, 0.25], color=C[0], linewidth=2.5, label=f"médiane {french_number(med)}")
    inside = DURATIONS[(DURATIONS >= low) & (DURATIONS <= high)]
    ax.plot([inside.min(), q1], [0, 0], color=C[0])
    ax.plot([q3, inside.max()], [0, 0], color=C[0])
    for v in (low, high):
        ax.axvline(v, color="gray", linestyle=":", linewidth=1.2)
    ax.text(high + 0.3, 0.33, f"Q3 + 1,5 × EI = {french_number(high)}", fontsize=9, color="gray")
    values, counts = np.unique(DURATIONS, return_counts=True)
    for v, c in zip(values, counts):
        ys = 0.45 + 0.12 * np.arange(c)
        ax.plot([v] * c, ys, "o", color=C[1] if v > high else "black", markersize=6)
    ax.axvline(DURATIONS.mean(), color=C[1], linewidth=1.8, label=f"moyenne {french_number(DURATIONS.mean())}")
    ax.annotate("valeur aberrante", xy=(38, 0.45), xytext=(30, 0.85), fontsize=9,
                arrowprops=dict(arrowstyle="->", color=C[1]))
    ax.set(xlim=(8, 41), ylim=(-0.45, 1.1), xlabel="durée d'entraînement (minutes)",
           title="Neuf durées : la boîte va de Q1 à Q3, la moyenne est tirée par 38")
    ax.set_yticks([])
    ax.legend(loc="upper left", fontsize=9)
    grid(ax)
    save(fig, "boite.png")


def fig_large_numbers() -> None:
    """Monte Carlo: the share of points under y = x² (true value 1/3), with ±2 standard errors, and Chebyshev."""
    rng = np.random.default_rng(1)
    u = rng.random((10_000, 2))
    hits = (u[:, 1] < u[:, 0] ** 2).astype(float)
    n = np.arange(1, len(hits) + 1)
    running = np.cumsum(hits) / n
    sigma = math.sqrt(2 / 9)
    fig, ax = plt.subplots(figsize=(7.5, 3.3))
    ax.plot(n, running, color=C[0], linewidth=1.3, label="proportion des points sous la courbe")
    ax.axhline(1 / 3, color="black", linewidth=1, label="valeur exacte 1/3")
    ax.fill_between(n, 1 / 3 - 2 * sigma / np.sqrt(n), 1 / 3 + 2 * sigma / np.sqrt(n), color=C[0], alpha=0.15,
                    label="±2 erreurs types, 2σ/√n")
    ax.set(xscale="log", ylim=(0, 0.75), xlabel="nombre de points n (échelle log)",
           title="Loi des grands nombres : la moyenne se stabilise, l'écart diminue comme 1/√n")
    ax.legend(fontsize=9, loc="upper right")
    grid(ax)
    save(fig, "grands_nombres.png")


def fig_clt() -> None:
    """A very skewed discrete law (0 with probability 0,9, 10 with probability 0,1), then its means for n = 5, 30, 200."""
    rng = np.random.default_rng(2)
    mu, sigma = 1.0, 3.0
    fig, axes = plt.subplots(1, 4, figsize=(13, 3))
    axes[0].vlines([0, 10], 0, [0.9, 0.1], color=C[0], linewidth=4)
    axes[0].plot([0, 10], [0.9, 0.1], "o", color=C[0])
    axes[0].set(title="n = 1 : la loi elle-même", xlabel="valeur d'un tirage", ylabel="probabilité", xlim=(-2, 12),
                ylim=(0, 1))
    grid(axes[0])
    for ax, n in zip(axes[1:], [5, 30, 200]):
        means = (rng.random((40_000, n)) < 0.1).mean(axis=1) * 10
        values, counts = np.unique(means, return_counts=True)
        width = 10 / n
        ax.bar(values, counts / len(means) / width, width=width * 0.9, color=C[0], alpha=0.6)
        xs = np.linspace(mu - 4 * sigma / math.sqrt(n), mu + 4 * sigma / math.sqrt(n), 300)
        ax.plot(xs, stats.norm(mu, sigma / math.sqrt(n)).pdf(xs), color="black", linewidth=1.5)
        ax.set(title=f"n = {n}", xlabel="moyenne de n tirages")
        grid(ax)
    axes[1].set_ylabel("densité (histogramme)")
    fig.suptitle("Théorème central limite : les moyennes d'une loi très asymétrique deviennent normales", y=1.03)
    save(fig, "tcl.png")


def fig_estimators() -> None:
    """S² divided by n and by n − 1, on 20 000 samples of 5 values of N(0, 2²): the first is biased, its spread smaller."""
    rng = np.random.default_rng(3)
    samples = rng.normal(0, 2, (20_000, 5))
    v0, v1 = samples.var(axis=1), samples.var(axis=1, ddof=1)
    bins = np.linspace(0, 20, 61)
    fig, ax = plt.subplots(figsize=(7.5, 3.3))
    ax.hist(v0, bins=bins, density=True, alpha=0.45, color=C[0], label="divisé par n")
    ax.hist(v1, bins=bins, density=True, alpha=0.45, color=C[1], label="divisé par n − 1")
    ax.axvline(4, color="black", linewidth=1.5, label="vraie variance σ² = 4")
    ax.axvline(v0.mean(), color=C[0], linestyle="--", linewidth=1.5, label=f"moyenne : {french(v0.mean())}")
    ax.axvline(v1.mean(), color=C[1], linestyle="--", linewidth=1.5, label=f"moyenne : {french(v1.mean())}")
    ax.set(xlabel="variance estimée sur 5 valeurs", title="Deux estimateurs de σ² : l'un biaisé, l'autre non")
    ax.legend(fontsize=9)
    grid(ax)
    save(fig, "estimateurs.png")


def fig_intervals() -> None:
    """50 intervals mean ± 1,96 σ/√n from 50 samples of 25 values of N(100, 15²): the ones that miss the mean in red."""
    rng = np.random.default_rng(5)
    mu, sigma, n = 100, 15, 25
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    missed = 0
    for k in range(50):
        sample = rng.normal(mu, sigma, n)
        half = 1.96 * sigma / math.sqrt(n)
        low, high = sample.mean() - half, sample.mean() + half
        ok = low <= mu <= high
        missed += not ok
        ax.plot([k, k], [low, high], color=C[0] if ok else C[1], linewidth=2 if not ok else 1.3)
        ax.plot(k, sample.mean(), "o", color=C[0] if ok else C[1], markersize=3)
    ax.axhline(mu, color="black", linewidth=1)
    ax.set(xlabel="échantillon n°", ylabel="intervalle à 95 %",
           title=f"50 échantillons, 50 intervalles : {missed} ne contiennent pas la vraie moyenne")
    grid(ax)
    save(fig, "intervalles.png")


def fig_bootstrap() -> None:
    """The bootstrap distribution of the median of 61 skewed values, and its percentile interval at 95 %."""
    rng = np.random.default_rng(8)
    sample = np.round(rng.lognormal(3, 0.6, 61), 1)
    boot = np.median(sample[rng.integers(0, 61, (5_000, 61))], axis=1)
    low, high = np.percentile(boot, [2.5, 97.5])
    fig, ax = plt.subplots(figsize=(7.5, 3.2))
    ax.hist(boot, bins=50, color=C[0], alpha=0.6, label="5 000 médianes de rééchantillons")
    ax.axvline(np.median(sample), color="black", linewidth=1.5,
               label=f"médiane de l'échantillon : {french(np.median(sample), 1)}")
    ax.axvspan(low, high, color=C[1], alpha=0.08)
    for v in (low, high):
        ax.axvline(v, color=C[1], linestyle="--", linewidth=1.5)
    ax.plot([], [], color=C[1], linestyle="--", label=f"intervalle à 95 % : [{french(low, 1)} ; {french(high, 1)}]")
    ax.set(xlabel="médiane", title="Bootstrap de la médiane de 61 valeurs asymétriques")
    ax.legend(fontsize=9, loc="upper right")
    grid(ax)
    save(fig, "bootstrap_mediane.png")


def fig_covariance() -> None:
    """The four points of the sheet, the centre (x̄, ȳ) and the sign of each product of deviations."""
    xs, ys = np.array([2, 4, 6, 8]), np.array([1, 5, 4, 8])
    mx, my = xs.mean(), ys.mean()
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    ax.axvline(mx, color="gray", linewidth=1)
    ax.axhline(my, color="gray", linewidth=1)
    for x, y in zip(xs, ys):
        product = (x - mx) * (y - my)
        colour = C[0] if product > 0 else C[1]
        ax.add_patch(plt.Rectangle((mx, my), x - mx, y - my, color=colour, alpha=0.25))
        ax.plot(x, y, "o", color=colour, markersize=8)
        ax.annotate(f"{french_number(product)}", xy=(x, y), xytext=(6, 6), textcoords="offset points", fontsize=10)
    ax.plot(mx, my, "s", color="black", markersize=7)
    ax.annotate("centre (x̄, ȳ) = (5 ; 4,5)", xy=(mx, my), xytext=(5.4, 1.2), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="gray"))
    ax.text(6.2, 7.6, "+ : produit positif", color=C[0], fontsize=9)
    ax.text(6.2, 7.1, "− : produit négatif", color=C[1], fontsize=9)
    ax.set(xlim=(0.5, 9.5), ylim=(0, 9), xlabel="x", ylabel="y",
           title="Covariance : la moyenne des aires signées\n(x − x̄)(y − ȳ) = 20 / 4 = 5")
    grid(ax)
    save(fig, "covariance.png")


def fig_imputation() -> None:
    """A sample of 40 values, 8 of them missing: imputing by the mean piles them up in the middle."""
    rng = np.random.default_rng(13)
    values = np.round(rng.normal(50, 10, 40), 0)
    missing = rng.choice(40, 8, replace=False)
    observed = np.delete(values, missing)
    imputed = np.concatenate([observed, np.full(8, observed.mean())])
    bins = np.arange(20, 82, 4)
    fig, axes = plt.subplots(1, 2, figsize=(10, 3), sharey=True)
    axes[0].hist(observed, bins=bins, color=C[0], alpha=0.7)
    axes[0].set(title=f"32 valeurs observées : écart-type {french(observed.std(), 1)}", xlabel="valeur")
    axes[1].hist(imputed, bins=bins, color=C[1], alpha=0.7)
    axes[1].set(title=f"+ 8 valeurs imputées par la moyenne : {french(imputed.std(), 1)}", xlabel="valeur")
    for ax in axes:
        grid(ax)
    save(fig, "imputation.png")


def fig_dimension() -> None:
    """In the cube [−1, 1]^d: the share of the volume inside the inscribed ball, and within 0,05 of the border."""
    ds = np.arange(1, 51)
    ball = np.array([math.pi ** (d / 2) / math.gamma(d / 2 + 1) / 2 ** d for d in ds])
    shell = 1 - 0.95 ** ds
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.3))
    axes[0].semilogy(ds, ball, marker=".", color=C[0])
    axes[0].set(xlabel="dimension d", ylabel="part du volume (log)", title="Dans la boule inscrite")
    axes[1].plot(ds, shell, marker=".", color=C[1])
    axes[1].set(xlabel="dimension d", ylim=(0, 1.02), title="À moins de 0,05 du bord")
    for ax in axes:
        grid(ax)
    fig.suptitle("Le cube [−1 ; 1]^d en grande dimension : presque tout le volume est près du bord", y=1.03)
    save(fig, "grande_dimension.png")


def main() -> int:
    print(f"Figures de M02c dans {OUT.relative_to(ROOT)} :")
    fig_box()
    fig_large_numbers()
    fig_clt()
    fig_estimators()
    fig_intervals()
    fig_bootstrap()
    fig_covariance()
    fig_imputation()
    fig_dimension()
    return 0


if __name__ == "__main__":
    sys.exit(main())
