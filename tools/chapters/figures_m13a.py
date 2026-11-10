#!/usr/bin/env python
"""Draw the figures of chapter M13a (used by Claude).

    python tools/chapters/figures_m13a.py

Writes small PNG files into chapitres/m13a_vraisemblance_logistique/figures/: the Bernoulli log-likelihood of a
proportion 5/8 for 8 and for 80 labels, the Gaussian log-likelihood of five travel times, the sigmoid and the softplus
with their asymptotes, the log-loss of a score against the error rate, the probability lines of a logistic model with
two features, the posterior of two Gaussian classes of the same variance, and a split of six targets into a
within-group and a between-group variance. The numbers are those of the fiche; none comes from workbookIA 13 (no
log-loss against p̂, no σ′, no impurity of a binary law, no penguins, no letters).
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

OUT = ROOT / "chapitres" / "m13a_vraisemblance_logistique" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

TIMES = np.array([31.0, 24.0, 38.0, 29.0, 33.0])               # §1: μ̂ = 31, σ̂² = 21,2 (26,5 with n − 1)
W, B = np.array([1.2, -0.8]), -0.4                              # §4: the logistic model
MU0, MU1, VAR, PI1 = 1.0, 4.0, 2.25, 0.36                       # §5: two Gaussian classes
TARGETS = np.array([3.0, 5.0, 4.0, 10.0, 12.0, 8.0])            # §7: split into (3, 5, 4) and (10, 12, 8)


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


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def softplus(z):
    return np.maximum(z, 0.0) + np.log1p(np.exp(-np.abs(z)))


def likelihoods() -> None:
    """Left: ℓ(p) − ℓ(p̂) for 5 ones out of 8 and 50 out of 80. Right: the Gaussian log-likelihood of the five times."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    p = np.linspace(0.02, 0.98, 400)
    for n, color in ((8, C[0]), (80, C[1])):
        k = 5 * n // 8
        ell = k * np.log(p) + (n - k) * np.log1p(-p)
        top = k * np.log(k / n) + (n - k) * np.log1p(-k / n)
        axes[0].plot(p, ell - top, color=color, lw=2, label=f"{k} sur {n}")
    axes[0].axvline(0.625, color="0.4", ls="--", lw=1)
    axes[0].text(0.635, -9.3, "p̂ = 0,625", color="0.3")
    axes[0].set(ylim=(-10, 0.5), xlabel="p", ylabel="ℓ(p) − ℓ(p̂)",
                title="Log-vraisemblance de Bernoulli :\nmême maximum, pic plus étroit avec plus de données")
    axes[0].legend(loc="lower left")

    mu = np.linspace(25, 37, 300)
    var = np.linspace(6, 70, 300)
    M, S2 = np.meshgrid(mu, var)
    n = TIMES.size
    ss = ((TIMES[:, None, None] - M) ** 2).sum(axis=0)
    ell = -n / 2 * np.log(2 * np.pi * S2) - ss / (2 * S2)
    best = -n / 2 * np.log(2 * np.pi * 21.2) - 106 / (2 * 21.2)
    levels = best - np.array([8, 4, 2, 1, 0.5])
    cs = axes[1].contour(M, S2, ell, levels=levels, colors=[C[2]], linewidths=1.2)
    axes[1].clabel(cs, fmt=lambda v: french_number(round(v - best, 1)), fontsize=8)
    axes[1].plot([31], [21.2], "o", color=C[0], ms=8, label="(μ̂, σ̂²) = (31 ; 21,2)")
    axes[1].plot([31], [26.5], "s", color=C[3], ms=7, label="avec n − 1 : (31 ; 26,5)")
    axes[1].set(xlabel="μ (minutes)", ylabel="σ² (minutes²)",
                title="Log-vraisemblance gaussienne de cinq durées\n(écart au maximum)")
    axes[1].legend(loc="upper right", fontsize=9)
    save(fig, "vraisemblances.png")


def sigmoid_softplus() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    z = np.linspace(-6, 6, 400)
    axes[0].plot(z, sigmoid(z), color=C[0], lw=2.2, label="σ(z)")
    axes[0].axhline(0.5, color="0.6", lw=0.8, ls="--")
    axes[0].axhline(0, color="0.6", lw=0.8)
    axes[0].axhline(1, color="0.6", lw=0.8)
    axes[0].axvline(0, color="0.6", lw=0.8)
    for zz in (0.3, -2.2):
        axes[0].plot([zz], [sigmoid(zz)], "o", color=C[1])
        axes[0].text(zz + 0.25, sigmoid(zz) - 0.06, f"σ({french_number(zz)}) ≈ {sigmoid(zz):.3g}".replace(".", ","),
                     color=C[1], fontsize=9)
    axes[0].set(xlabel="score z", ylabel="probabilité", title="La sigmoïde, de ℝ dans ]0, 1[")
    axes[0].legend(loc="upper left")

    axes[1].plot(z, softplus(z), color=C[0], lw=2.2, label="s(z) = ln(1 + eᶻ)")
    axes[1].plot(z, softplus(-z), color=C[2], lw=1.8, label="s(−z) = −ln σ(z)")
    axes[1].plot(z, np.maximum(z, 0), color="0.4", lw=1, ls="--", label="max(z, 0)")
    axes[1].plot([0], [np.log(2)], "o", color=C[1])
    axes[1].text(0.2, np.log(2) + 0.25, "ln 2", color=C[1])
    axes[1].set(ylim=(-0.3, 6.3), xlabel="z", title="La softplus et ses deux asymptotes")
    axes[1].legend(loc="upper center", fontsize=9)
    save(fig, "sigmoide_softplus.png")


def loss_and_error() -> None:
    """For a label 1: the log-loss of the score, in bits, lies above the error 1[z ≤ 0]."""
    fig, ax = plt.subplots(figsize=(6.2, 4.0))
    z = np.linspace(-4, 4, 801)
    ax.plot(z, softplus(-z) / np.log(2), color=C[0], lw=2.2, label="log-loss en bits : log₂(1 + e⁻ᶻ)")
    ax.step(z, (z <= 0).astype(float), where="post", color=C[3], lw=2, label="erreur : 1 si z ≤ 0")
    ax.plot([0], [1], "o", color=C[1])
    ax.set(ylim=(-0.2, 5.0), xlabel="score z d'un exemple de label 1", ylabel="coût",
           title="Une borne supérieure lisse et convexe de l'erreur")
    ax.legend(loc="upper right", fontsize=9)
    save(fig, "logloss_erreur.png")


def logistic_plane() -> None:
    fig, ax = plt.subplots(figsize=(6.4, 5.2))
    x1 = np.linspace(-1, 4, 300)
    x2 = np.linspace(-1, 4, 300)
    X1, X2 = np.meshgrid(x1, x2)
    P = sigmoid(W[0] * X1 + W[1] * X2 + B)
    im = ax.contourf(X1, X2, P, levels=np.linspace(0, 1, 11), cmap="RdBu_r", alpha=0.55)
    cs = ax.contour(X1, X2, P, levels=[0.3, 0.5, 0.7], colors=["0.25"], linewidths=[1, 2, 1],
                    linestyles=["--", "-", "--"])
    ax.clabel(cs, fmt=lambda v: f"P = {french_number(v)}", fontsize=9)
    for pt in ((2.0, 0.5), (0.5, 1.0), (1.0, 2.0)):
        prob = sigmoid(W @ np.array(pt) + B)
        ax.plot(*pt, "ko")
        ax.text(pt[0] + 0.08, pt[1] + 0.1, f"{prob:.2f}".replace(".", ","), fontsize=10)
    ax.annotate("", xy=(0.5 + W[0] * 0.8, 0.25 + W[1] * 0.8), xytext=(0.5, 0.25),
                arrowprops={"arrowstyle": "-|>", "color": C[1], "lw": 2})
    ax.text(1.35, -0.55, "w", color=C[1], fontsize=12)
    fig.colorbar(im, ax=ax, label="P(Y = 1 | x) = σ(w · x + b)")
    ax.set(aspect="equal", xlabel="x₁", ylabel="x₂",
           title="w = (1,2 ; −0,8), b = −0,4 : des droites de niveau parallèles")
    save(fig, "logistique_plan.png")


def gaussian_classes() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.0))
    x = np.linspace(-4, 9, 500)
    dens = lambda m: np.exp(-(x - m) ** 2 / (2 * VAR)) / np.sqrt(2 * np.pi * VAR)
    axes[0].plot(x, (1 - PI1) * dens(MU0), color=C[0], lw=2, label="0,64 × N(1 ; 1,5²)  (classe 0)")
    axes[0].plot(x, PI1 * dens(MU1), color=C[3], lw=2, label="0,36 × N(4 ; 1,5²)  (classe 1)")
    w = (MU1 - MU0) / VAR
    b = (MU0 ** 2 - MU1 ** 2) / (2 * VAR) + np.log(PI1 / (1 - PI1))
    xstar = -b / w
    for ax in axes:
        ax.axvline(xstar, color="0.4", ls="--", lw=1)
    axes[0].text(xstar + 0.15, 0.115, f"x* ≈ {xstar:.2f}".replace(".", ","), color="0.3")
    axes[0].set(xlabel="x", ylabel="π_k p(x | k)", title="Deux classes gaussiennes de même variance")
    axes[0].legend(loc="upper right", fontsize=9)
    axes[1].plot(x, sigmoid(w * x + b), color=C[1], lw=2.2)
    axes[1].axhline(0.5, color="0.6", lw=0.8)
    axes[1].set(xlabel="x", ylabel="P(classe 1 | x)",
                title=f"L'a posteriori : σ({french_number(round(w, 3))} x − {french_number(round(-b, 3))})")
    save(fig, "bayes_gaussien.png")


def within_between() -> None:
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    idx = np.arange(1, 7)
    m = TARGETS.mean()
    groups = ((idx[:3], TARGETS[:3], C[0]), (idx[3:], TARGETS[3:], C[3]))
    ax.axhline(m, color="0.3", lw=1.2, ls="--")
    ax.text(5.3, m - 0.55, "moyenne 7", color="0.3", fontsize=9)
    for i, y, color in groups:
        mg = y.mean()
        ax.hlines(mg, i[0] - 0.3, i[-1] + 0.3, color=color, lw=2)
        for ii, yy in zip(i, y):
            ax.vlines(ii, mg, yy, color=color, lw=1.2, ls=":")
        ax.plot(i, y, "o", color=color, ms=8)
        ax.annotate("", xy=(i[1], mg), xytext=(i[1], m), arrowprops={"arrowstyle": "<->", "color": "0.45", "lw": 1})
    ax.text(1.35, 5.4, "inter : la moyenne\ndu groupe s'écarte de 7", fontsize=8.5, color="0.35")
    ax.set(xticks=idx, xlabel="exemple", ylabel="cible y", ylim=(1.5, 13.5),
           title="Variance totale 10,67 = intra 1,67 + inter 9")
    save(fig, "variance_intra_inter.png")


def main() -> int:
    print(f"figures of M13a -> {OUT.relative_to(ROOT)}")
    likelihoods()
    sigmoid_softplus()
    loss_and_error()
    logistic_plane()
    gaussian_classes()
    within_between()
    return 0


if __name__ == "__main__":
    sys.exit(main())
