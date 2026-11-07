#!/usr/bin/env python
"""Draw the figures of chapter M04 (used by Claude).

    python tools/chapters/figures_m04.py

Writes small PNG files into chapitres/m04_bayes_beta/figures/: Bayes' rule as areas, a three-hypothesis update
answer after answer, a likelihood and its logarithm, the shapes of the Beta law, a conjugate update (prior, likelihood,
posterior), a credible interval with the mode, the mean and the maximum likelihood, the posterior that narrows as data
accumulate, and two posteriors for Thompson sampling. Every figure is computed from the sheet's own examples (a wind
turbine sensor, a multiple-choice quiz, a 3D printer, two article titles): none comes from workbookIA 4 (coins, the
space probe, the smoke detector, the medical test).
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

OUT = ROOT / "chapitres" / "m04_bayes_beta" / "figures"
C = wbplot.CATEGORICAL
SEED_THOMPSON = 9                                  # a draw where B wins: θA ≈ 0,057, θB ≈ 0,105
DPI = 110


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
            if axis.get_scale() == "linear" and not getattr(axis, "keep_labels", False):
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def grid(ax) -> None:
    ax.grid(True, alpha=0.25)


def fig_areas() -> None:
    """Bayes' rule as areas: width = prior, height = likelihood of the alert; the posterior is a ratio of areas."""
    prior_worn, like_worn, like_ok = 0.02, 0.9, 0.05
    width_worn = 0.12                                  # drawn wider than 0.02 to stay visible (the axis is broken)
    fig, ax = plt.subplots(figsize=(7.2, 3.3))
    ax.add_patch(plt.Rectangle((0, 0), width_worn, 1, facecolor="white", edgecolor="gray"))
    ax.add_patch(plt.Rectangle((width_worn, 0), 1 - width_worn, 1, facecolor="white", edgecolor="gray"))
    ax.add_patch(plt.Rectangle((0, 0), width_worn, like_worn, facecolor=C[1], alpha=0.8))
    ax.add_patch(plt.Rectangle((width_worn, 0), 1 - width_worn, like_ok, facecolor=C[0], alpha=0.8))
    ax.text(width_worn / 2, 1.04, "usé\nP = 0,02", ha="center", va="bottom", fontsize=9)
    ax.text(width_worn + (1 - width_worn) / 2, 1.04, "sain\nP = 0,98", ha="center", va="bottom", fontsize=9)
    ax.text(width_worn / 2, like_worn / 2, "alerte\n0,9", ha="center", va="center", color="white", fontsize=9)
    ax.annotate("alerte : 0,05", xy=(0.55, like_ok), xytext=(0.55, 0.3), ha="center", fontsize=9,
                arrowprops=dict(arrowstyle="->", color="gray"))
    ax.text(0.98, 0.62, "aire orange : 0,02 × 0,9 = 0,018\naire bleue : 0,98 × 0,05 = 0,049\n"
            "P(usé | alerte) = 0,018 / 0,067 ≈ 0,27", ha="right", va="center", fontsize=9,
            bbox=dict(facecolor="white", edgecolor="lightgray"))
    ax.set(xlim=(0, 1), ylim=(0, 1.25), xticks=[], ylabel="P(alerte | état)",
           title="La règle de Bayes en aires (la bande « usé » est élargie pour rester visible)")
    ax.set_yticks([0, 0.5, 1])
    save(fig, "bayes_aires.png")


def fig_updates() -> None:
    """Three hypotheses on a student (well, a little, not prepared), updated answer after answer: R, R, F."""
    names = ["bien révisé", "un peu", "pas révisé"]
    prior = np.array([0.5, 0.3, 0.2])
    right = np.array([0.9, 0.6, 0.25])
    stages = [("a priori", prior)]
    for answer in "JJF":
        like = right if answer == "J" else 1 - right
        prior = prior * like / np.sum(prior * like)
        stages.append((f"après {'juste' if answer == 'J' else 'faux'}", prior))
    fig, axes = plt.subplots(1, 4, figsize=(11, 2.9), sharey=True)
    for k, (ax, (label, probs)) in enumerate(zip(axes, stages)):
        ax.bar(range(3), probs, color=[C[0], C[1], C[2]], alpha=0.85)
        for j, p in enumerate(probs):
            ax.text(j, p + 0.02, french(p), ha="center", fontsize=8)
        ax.set_xticks(range(3), labels=names, fontsize=8, rotation=20)
        ax.xaxis.keep_labels = True
        ax.set(title=label if k == 0 else f"{k} : {label}", ylim=(0, 1))
        grid(ax)
    axes[0].set_ylabel("probabilité")
    fig.suptitle("Trois hypothèses, mises à jour réponse après réponse (juste, juste, faux)", y=1.04)
    save(fig, "mise_a_jour.png")


def fig_likelihood() -> None:
    """Likelihood of 2 failures in 12 prints, and its logarithm: both are maximal at 1/6."""
    theta = np.linspace(0.001, 0.7, 600)
    like = theta ** 2 * (1 - theta) ** 10
    loglike = 2 * np.log(theta) + 10 * np.log(1 - theta)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.2))
    ax1.plot(theta, like * 1e3, color=C[0], linewidth=2)
    ax1.axvline(1 / 6, color=C[1], linestyle="--", label="maximum en θ = 1/6")
    ax1.set(xlabel="θ (taux d'échec)", ylabel="L(θ) × 1 000", title="Vraisemblance : θ² (1 − θ)¹⁰")
    ax1.legend(fontsize=9)
    grid(ax1)
    ax2.plot(theta, loglike, color=C[2], linewidth=2)
    ax2.axvline(1 / 6, color=C[1], linestyle="--")
    ax2.set(xlabel="θ (taux d'échec)", ylabel="ℓ(θ) = ln L(θ)", ylim=(-15, -4),
            title="Log-vraisemblance : 2 ln θ + 10 ln(1 − θ)")
    grid(ax2)
    save(fig, "vraisemblance.png")


def fig_beta_shapes() -> None:
    """Shapes of Beta(a, b): U, uniform, bell, skewed, decreasing, concentrated."""
    x = np.linspace(0.0005, 0.9995, 800)
    cases = [((0.5, 0.5), "Beta(0,5 ; 0,5)"), ((1, 1), "Beta(1, 1) uniforme"), ((2, 2), "Beta(2, 2)"),
             ((3, 6), "Beta(3, 6)"), ((1, 4), "Beta(1, 4)"), ((20, 40), "Beta(20, 40)")]
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    for k, ((a, b), label) in enumerate(cases):
        ax.plot(x, stats.beta(a, b).pdf(x), color=C[k % len(C)], linewidth=2, label=label)
    ax.set(xlim=(0, 1), ylim=(0, 7.3), xlabel="θ", ylabel="densité", title="Quelques lois Beta")
    ax.legend(fontsize=8, ncol=2)
    grid(ax)
    save(fig, "lois_beta.png")


def fig_conjugate() -> None:
    """Prior Beta(2, 8), likelihood of 2 failures in 12 (normalized), posterior Beta(4, 18)."""
    x = np.linspace(0.0005, 0.9995, 800)
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    ax.plot(x, stats.beta(2, 8).pdf(x), color=C[0], linewidth=2, label="a priori Beta(2, 8)")
    ax.plot(x, stats.beta(3, 11).pdf(x), color=C[2], linewidth=2, linestyle="--",
            label="vraisemblance θ²(1 − θ)¹⁰, normalisée")
    ax.plot(x, stats.beta(4, 18).pdf(x), color=C[1], linewidth=2.5, label="a posteriori Beta(4, 18)")
    ax.set(xlim=(0, 0.8), xlabel="θ (taux d'échec)", ylabel="densité",
           title="Conjugaison : Beta(2, 8), puis 2 échecs sur 12, donne Beta(4, 18)")
    ax.legend(fontsize=9)
    grid(ax)
    save(fig, "conjugaison.png")


def fig_credible() -> None:
    """Beta(4, 18): 95 % equal-tailed credible interval, mode (MAP), mean, and the maximum likelihood 1/6."""
    law = stats.beta(4, 18)
    x = np.linspace(0, 0.7, 800)
    low, high = law.ppf([0.025, 0.975])
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    ax.plot(x, law.pdf(x), color=C[1], linewidth=2.5)
    inside = (x >= low) & (x <= high)
    ax.fill_between(x[inside], law.pdf(x[inside]), color=C[1], alpha=0.25, label=f"95 % : [{french(low, 3)} ; {french(high, 3)}]")
    for value, label, colour, style in [(3 / 20, "MAP (mode) 0,15", C[0], "-"), (1 / 6, "max. de vraisemblance 0,167", C[2], ":"),
                                        (4 / 22, "moyenne 0,182", "black", "--")]:
        ax.axvline(value, color=colour, linestyle=style, linewidth=1.5, label=label)
    ax.set(xlim=(0, 0.7), xlabel="θ (taux d'échec)", ylabel="densité",
           title="Résumer Beta(4, 18) : un intervalle de crédibilité et trois estimations")
    ax.legend(fontsize=8)
    grid(ax)
    save(fig, "credibilite.png")


def fig_narrowing() -> None:
    """Posterior from Beta(2, 8) after n prints with a failure rate of 1/6: the width shrinks like 1/√n."""
    x = np.linspace(0, 0.5, 1000)
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    for k, n in enumerate([12, 48, 192, 768]):
        failures = n // 6
        law = stats.beta(2 + failures, 8 + n - failures)
        low, high = law.interval(0.95)
        ax.plot(x, law.pdf(x), color=C[k], linewidth=2, label=f"n = {n} : largeur à 95 % {french(high - low, 3)}")
    ax.set(xlim=(0, 0.5), xlabel="θ (taux d'échec)", ylabel="densité",
           title="Quatre fois plus de données, un intervalle environ deux fois plus étroit")
    ax.legend(fontsize=8)
    grid(ax)
    save(fig, "resserrement.png")


def fig_thompson() -> None:
    """Two titles: Beta(19, 283) and Beta(10, 112); Thompson draws one value from each and shows the larger."""
    x = np.linspace(0, 0.2, 800)
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    ax.plot(x, stats.beta(19, 283).pdf(x), color=C[0], linewidth=2, label="titre A : 18 clics sur 300, Beta(19, 283)")
    ax.plot(x, stats.beta(10, 112).pdf(x), color=C[1], linewidth=2, label="titre B : 9 clics sur 120, Beta(10, 112)")
    rng = np.random.default_rng(SEED_THOMPSON)
    draw_a, draw_b = rng.beta(19, 283), rng.beta(10, 112)
    ax.plot([draw_a], [0.5], "v", color=C[0], markersize=10)
    ax.plot([draw_b], [0.5], "v", color=C[1], markersize=10)
    ax.text(0.112, 20, f"un tirage : θA = {french(draw_a, 3)}, θB = {french(draw_b, 3)}\n"
            f"on affiche le titre {'B' if draw_b > draw_a else 'A'}", fontsize=9,
            bbox=dict(facecolor="white", edgecolor="lightgray"))
    ax.set(xlim=(0, 0.2), xlabel="taux de clic θ", ylabel="densité",
           title="Échantillonnage de Thompson : tirer un taux par titre, afficher le plus grand")
    ax.legend(fontsize=8, loc="upper right")
    grid(ax)
    save(fig, "thompson.png")


def main() -> int:
    print(f"Figures de M04 dans {OUT.relative_to(ROOT)} :")
    fig_areas()
    fig_updates()
    fig_likelihood()
    fig_beta_shapes()
    fig_conjugate()
    fig_credible()
    fig_narrowing()
    fig_thompson()
    return 0


if __name__ == "__main__":
    sys.exit(main())
