#!/usr/bin/env python
"""Draw the figures of chapter M14 (used by Claude).

    python tools/chapters/figures_m14.py

Writes small PNG files into chapitres/m14_ensembles/figures/: the exact tail of a binomial law against the Hoeffding
and Chernoff bounds, as n grows (log scale); the variance of the average of M correlated predictions, which levels off
at the average covariance; (1 + x/n)ⁿ against eˣ for x = 2 and x = −3; the weights of four experts under Hedge for two
learning rates; the exponential and Huber losses and their derivatives with respect to the prediction. The numbers are
those of the fiche; none comes from workbookIA 14 (no voters, no bootstrap, no x = −1, no equicorrelated models, no
seed 14xx).
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
from scipy.special import rel_entr, softmax  # noqa: E402
from scipy.stats import binom  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m14_ensembles" / "figures"
C = wbplot.CATEGORICAL
DPI = 110
SEED = 4301

P_TAIL, A_TAIL = 0.3, 0.5                       # §1: P(X ≥ n a) for X ~ B(n, 0,3), a = 0,5
X_LIMIT = (2.0, -3.0)                           # §3: two values of x
ETAS = (0.1, 0.8)                               # §4: two learning rates
DELTA = 1.0                                     # §5: the threshold of the Huber loss


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


def binomial_tail() -> None:
    """§1: the exact tail, the Hoeffding bound and the Chernoff bound, for p = 0,3 and a = 0,5."""
    ns = np.arange(4, 151, 2)
    kl = float(rel_entr(A_TAIL, P_TAIL) + rel_entr(1 - A_TAIL, 1 - P_TAIL))
    exact = [binom.sf(math.ceil(n * A_TAIL) - 1, n, P_TAIL) for n in ns]
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.plot(ns, np.exp(-2 * ns * (A_TAIL - P_TAIL) ** 2), color=C[1], lw=2, label="Hoeffding : exp(−2n(a − p)²)")
    ax.plot(ns, np.exp(-ns * kl), color=C[0], lw=2, label="Chernoff : exp(−n KL(a ‖ p))")
    ax.plot(ns, exact, "o", color="0.25", ms=3, label="queue exacte P(X ≥ n/2)")
    ax.set_yscale("log")
    ax.set(xlabel="n", ylabel="probabilité (échelle log)",
           title="X de loi B(n ; 0,3) : la queue P(X ≥ 0,5 n) et ses deux bornes")
    ax.legend(fontsize=9)
    save(fig, "queue_binomiale.png")


def variance_of_mean() -> None:
    """§2: M predictions X_i = a_i Z + E_i (a common part, an own part): V(mean) levels off at the mean covariance."""
    rng = np.random.default_rng(SEED)
    loads = rng.uniform(0.4, 1.0, size=200)          # how much each prediction follows the common part Z
    own = rng.uniform(1.0, 3.0, size=200)            # the variance of its own part E_i
    ms = np.arange(1, 201)
    values, floors = [], []
    for m in ms:
        a, s = loads[:m], own[:m]
        cov = np.outer(a, a) + np.diag(s)
        values.append(cov.sum() / m ** 2)
        floors.append(a.mean() ** 2 if m > 1 else np.nan)
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    ax.plot(ms, values, color=C[0], lw=2, label="V(moyenne des M prédictions)")
    ax.plot(ms, floors, "--", color=C[1], lw=1.5, label="(moyenne des aᵢ)² : la part commune")
    ax.plot(ms, np.array([own[:m].mean() for m in ms]) / ms, ":", color="0.4", lw=1.5,
            label="ce qu'on aurait sans la part commune")
    ax.set_xscale("log")
    ax.set(xlabel="nombre M de prédictions moyennées (échelle log)", ylabel="variance",
           title="Moyenner réduit la part propre, pas la part commune")
    ax.legend(fontsize=9)
    save(fig, "variance_moyenne.png")


def exp_limit() -> None:
    """§3: (1 + x/n)ⁿ against eˣ, for x = 2 and x = −3."""
    ns = np.unique(np.round(np.logspace(0, 3.3, 60)).astype(int))
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 3.8))
    names = {2.0: ("(1 + 2/n)ⁿ", "e²"), -3.0: ("(1 − 3/n)ⁿ", "e⁻³")}
    for ax, x in zip(axes, X_LIMIT):
        keep = ns[1 + x / ns > 0]
        ax.plot(keep, (1 + x / keep) ** keep, "o-", color=C[0], ms=3, lw=1.2, label=names[x][0])
        ax.axhline(math.exp(x), color=C[1], lw=1.5, ls="--",
                   label=f"{names[x][1]} ≈ {math.exp(x):.4f}".replace(".", ","))
        ax.set_xscale("log")
        ax.set(xlabel="n (échelle log)", title=f"x = {french_number(x)}")
        ax.legend(fontsize=9)
    save(fig, "limite_exponentielle.png")


def hedge_weights() -> None:
    """§4: the weights of four experts under Hedge, for a small and a large learning rate."""
    rng = np.random.default_rng(SEED + 5)
    T, means = 100, np.array([0.5, 0.35, 0.6, 0.45])
    losses = (rng.uniform(size=(T, 4)) < means).astype(float)
    cumulative = np.vstack([np.zeros(4), np.cumsum(losses, axis=0)])
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 3.8), sharey=True)
    for ax, eta in zip(axes, ETAS):
        weights = softmax(-eta * cumulative, axis=1)
        ax.stackplot(np.arange(T + 1), weights.T, colors=C[:4], alpha=0.85,
                     labels=[f"expert {k + 1} (perd {french_number(m)} en moyenne)" for k, m in enumerate(means)])
        ax.set(xlabel="tour t", title=f"η = {french_number(eta)}", xlim=(0, T), ylim=(0, 1))
    axes[0].set_ylabel("poids")
    axes[1].legend(fontsize=8, loc="lower right")
    fig.suptitle("Hedge, losses 0 ou 1 tirées au hasard : un petit η répartit les poids longtemps, un grand η se "
                 "concentre vite sur l'expert en tête", fontsize=10)
    save(fig, "hedge_poids.png")


def losses_and_gradients() -> None:
    """§5: the exponential loss e^(−yF) and the Huber loss, with their derivatives with respect to F."""
    t = np.linspace(-2, 3, 400)
    r = np.linspace(-3, 3, 400)
    huber = np.where(np.abs(r) <= DELTA, r ** 2 / 2, DELTA * (np.abs(r) - DELTA / 2))
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 3.8))
    axes[0].plot(t, np.exp(-t), color=C[0], lw=2, label="loss e^(−yF)")
    axes[0].plot(t, -np.exp(-t), color=C[1], lw=2, ls="--", label="dérivée en F, pour y = +1 : −e^(−F)")
    axes[0].axhline(0, color="0.6", lw=0.8)
    axes[0].set(xlabel="marge yF", ylim=(-4, 7), title="Loss exponentielle (y = +1)")
    axes[0].legend(fontsize=9)
    axes[1].plot(r, huber, color=C[0], lw=2, label="Huber (δ = 1) du résidu y − F")
    axes[1].plot(r, -np.clip(r, -DELTA, DELTA), color=C[1], lw=2, ls="--", label="dérivée en F : −clip(y − F, −δ, δ)")
    axes[1].axhline(0, color="0.6", lw=0.8)
    axes[1].set(xlabel="résidu y − F", title="Loss de Huber")
    axes[1].legend(fontsize=9)
    save(fig, "losses_gradients.png")


def main() -> int:
    print(f"Figures of M14 into {OUT.relative_to(ROOT)}:")
    binomial_tail()
    variance_of_mean()
    exp_limit()
    hedge_weights()
    losses_and_gradients()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
