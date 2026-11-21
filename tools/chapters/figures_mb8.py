#!/usr/bin/env python
"""Draw the figures of chapter MB8 (used by Claude).

    python tools/chapters/figures_mb8.py

Writes small PNG files into chapitres/mb8_gradient_politique/figures/:
- §1: an archer shoots 4 arrows, each hits the centre with the probability θ = 0.8 (a binomial law B(4, θ)): the
  law, the score s_θ(x) = (x − 4θ)/(θ(1 − θ)) of each outcome, and the log-likelihoods θ ↦ ln p_θ(x), whose mean
  under θ₀ = 0.8 has a horizontal tangent at θ₀ (E[s] = 0) and the curvature −I(θ₀) = −25;
- §2: shooting stars, a Poisson law of mean θ: P(X ≥ 3) as a function of θ and its tangent at θ = 2 (slope
  2e⁻² ≈ 0.2707); for X ~ N(1, 1) and f(x) = x², 20 000 one-draw estimates of d/dμ E[f(X)] = 2 along the path
  (2X, standard deviation 2) and by the score (X²(X − 1), standard deviation √30);
- §3: the variance of (f − b)s as a function of the baseline b for the shooting stars (f = 1{X ≥ 3}, θ = 2), with
  b = 0, b = E[f] and b* = E[f s²]/E[s²]; a control variate: e^U against U for 300 uniform draws;
- §4: the weights (1 − γ)γᵗ of the discounted occupancy law for γ = 0.6 and 0.7; the occupancy laws of a two-level
  dam (high, low) under a softmax policy (γ = 0.6); the error of the centred finite differences against the exact
  gradient, as a function of the step h;
- §5: the weights (1 − λ)λ^{k−1} of the k-step returns in a λ-return, for λ = 0.6 and 0.7; the bias γᵏ(Pᵏe)(s) of
  the k-step returns on the chain of the dam when the estimated values are wrong by e = (1, 0);
- §6: the target p = Exp(1), the proposals q = Exp(1/2) and q = Exp(3) (rates) and their weights p/q; the effective
  sample size per draw, θ(2 − θ) for a proposal of rate θ < 2, and its value measured on 2 000 draws;
- §7: the Bradley-Terry probability σ(β_i − β_j) and the Elo expected result 1/(1 + 10^(−ΔR/400)), the same curve
  on two scales; Zermelo's sweeps on a table-tennis league of four players (each pair plays 4 matches);
- §8: a florist's Gibbs law π* ∝ π_ref e^{r/β} over four flowers as a function of β, and its value β ln Z between
  E_ref[r] = 2.05 and max r = 4.
The numbers are those of the fiche; none comes from workbookIA B1 to B8, nor from the exercises of MB8. The figures
that draw random numbers use the seeds 8091 (§2), 8092 (§3) and 8093 (§6), among the seeds 8091 to 8099 kept for MB8.
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
from scipy.stats import binom, poisson  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "mb8_gradient_politique" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

# §1: the archer, B(5, θ)
ARROWS, THETA0 = 4, 0.8
# §2, §3: shooting stars, Poisson of mean θ, f = 1{X ≥ 3}
STARS_THETA, STARS_K = 2.0, 3
# §4, §5: the dam (states H = high, B = low; actions T = turbine, R = hold back)
DAM_P = np.array([[[0.35, 0.65], [0.1, 0.9]],    # T
                  [[0.85, 0.15], [0.45, 0.55]]])   # R
DAM_R = np.array([[7.0, 2.0],                   # r[T, H], r[T, B]
                  [-1.0, 0.0]])                 # r[R, H], r[R, B]
DAM_LOGITS = np.array([[math.log(2.0), -math.log(2.0)],    # in H: π(T | H) = 0.8
                       [0.0, math.log(1.5)]])   # in B: π(T | B) = 0.4
DAM_GAMMA = 0.6
DAM_ERROR = np.array([1.0, 0.0])
# §7: table tennis, wins[i, j] = number of wins of i against j
LEAGUE = np.array([[0, 3, 2, 4], [1, 0, 3, 2], [2, 1, 0, 3], [0, 2, 1, 0]], dtype=float)
PLAYERS = ["A", "B", "C", "D"]
# §8: the florist
FLOWERS = ["roses", "tulipes", "pivoines", "lys"]
PI_REF = np.array([0.4, 0.35, 0.15, 0.1])
PROFIT = np.array([2.0, 1.0, 4.0, 3.0])


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def fr(value: float, digits: int) -> str:
    return f"{value:.{digits}f}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            keep = getattr(ax, "keep_ticks", False)
            if axis.get_scale() == "linear" and ax.axison and not keep:
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def dam_values(logits: np.ndarray):
    """Policy, induced chain, M = (I − γP_π)⁻¹, values, action values and advantages of the dam."""
    z = logits - logits.max(axis=1, keepdims=True)
    pi = np.exp(z) / np.exp(z).sum(axis=1, keepdims=True)
    p_pi = np.einsum("sa,ast->st", pi, DAM_P)
    r_pi = np.einsum("sa,as->s", pi, DAM_R)
    m = np.linalg.inv(np.eye(2) - DAM_GAMMA * p_pi)
    v = m @ r_pi
    q = DAM_R.T + DAM_GAMMA * np.einsum("ast,t->sa", DAM_P, v)
    return pi, p_pi, r_pi, m, v, q, q - v[:, None]


# --------------------------------------------------------------------------------------------------------- §1
def score_fisher() -> None:
    xs = np.arange(ARROWS + 1)
    p = binom.pmf(xs, ARROWS, THETA0)
    s = (xs - ARROWS * THETA0) / (THETA0 * (1 - THETA0))
    fisher = float(np.sum(p * s**2))
    fig, axes = plt.subplots(1, 2, figsize=(13.8, 4.7), gridspec_kw=dict(width_ratios=[1, 1.15]))
    ax = axes[0]
    ax.bar(xs, p, color=C[0], width=0.62, label="p(x), loi B(4 ; 0,8)")
    for x, px, sx in zip(xs, p, s):
        ax.text(x, px + 0.012, f"s = {french_number(sx)}", ha="center", fontsize=9, color=C[1])
    ax.set_xticks(xs, [str(x) for x in xs])
    ax.keep_ticks = True
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set(xlabel="nombre x de flèches au cœur (sur 4)", ylabel="probabilité", ylim=(0, 0.47))
    ax.set_title("Le score de chaque issue : ses valeurs pondérées par p(x)\n"
                 f"ont une somme nulle, et Σ p(x) s(x)² = I(0,8) = {french_number(round(fisher, 10))}", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="upper left")
    ax = axes[1]
    th = np.linspace(0.55, 0.97, 300)
    for x, col in zip((2, 3, 4), (C[2], C[3], C[4])):
        ll = binom.logpmf(x, ARROWS, th)
        ax.plot(th, ll, color=col, lw=1.4, label=f"ln p_θ({x})")
        l0 = binom.logpmf(x, ARROWS, THETA0)
        sx = (x - ARROWS * THETA0) / (THETA0 * (1 - THETA0))
        tt = np.linspace(THETA0 - 0.06, THETA0 + 0.06, 2)
        ax.plot(tt, l0 + sx * (tt - THETA0), color=col, lw=1.6, ls="--")
    mean_ll = np.array([np.sum(p * binom.logpmf(xs, ARROWS, t)) for t in th])
    ax.plot(th, mean_ll, color="black", lw=2.6, label="moyenne sous θ₀ = 0,8 : Σ p₀(x) ln p_θ(x)")
    top = float(np.sum(p * binom.logpmf(xs, ARROWS, THETA0)))
    ax.plot(th, top - 0.5 * fisher * (th - THETA0) ** 2, color="black", lw=1, ls=":",
            label="parabole de courbure −I(θ₀)")
    ax.axvline(THETA0, color="0.5", lw=0.8)
    ax.set(xlabel="paramètre θ", ylabel="log-vraisemblance", ylim=(-3.3, 0.2))
    ax.set_title("Pentes en θ₀ (tirets) : les scores −7,5, −1,25 et 5 ;\n"
                 "leur moyenne a une tangente horizontale en θ₀", fontsize=10.5)
    ax.legend(fontsize=8.2, loc="lower center")
    fig.tight_layout(w_pad=2.5)
    save(fig, "score_fisher.png")
    print(f"    I(0.8) = {fisher:.4f}, E[s] = {np.sum(p * s):.2e}")


# --------------------------------------------------------------------------------------------------------- §2
def score_path() -> None:
    rng = np.random.default_rng(8091)
    fig, axes = plt.subplots(1, 2, figsize=(13.6, 4.6))
    ax = axes[0]
    th = np.linspace(0.3, 5.0, 300)
    prob = poisson.sf(STARS_K - 1, th)
    deriv = math.exp(-STARS_THETA) * STARS_THETA**2 / 2
    p0 = float(poisson.sf(STARS_K - 1, STARS_THETA))
    ax.plot(th, prob, color=C[0], lw=2.2, label="P(X ≥ 3), X de loi de Poisson de moyenne θ")
    tt = np.linspace(1.0, 3.0, 2)
    ax.plot(tt, p0 + deriv * (tt - STARS_THETA), color=C[1], lw=1.6, ls="--",
            label=f"tangente en θ = 2, de pente 2e⁻² ≈ {fr(deriv, 4)}")
    ax.plot([STARS_THETA], [p0], "o", color=C[1])
    ax.set(xlabel="nombre moyen θ d'étoiles filantes par quart d'heure", ylabel="probabilité d'en voir au moins 3",
           ylim=(0, 1.0))
    ax.set_title("Une indicatrice, une loi discrète : la dérivée vaut 2e⁻²,\n"
                 "la dérivée tirage par tirage vaut 0", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="upper left")
    ax = axes[1]
    x = rng.normal(1.0, 1.0, size=20_000)
    path = 2 * x
    score = x**2 * (x - 1.0)
    bins = np.linspace(-12, 16, 113)
    ax.hist(score, bins=bins, color=C[1], alpha=0.55, density=True,
            label=f"score x²(x − 1) : moyenne {fr(score.mean(), 2)}, écart-type {fr(score.std(), 2)}")
    ax.hist(path, bins=bins, color=C[0], alpha=0.65, density=True,
            label=f"chemin 2x : moyenne {fr(path.mean(), 2)}, écart-type {fr(path.std(), 2)}")
    ax.axvline(2.0, color="black", lw=1.2, ls=":")
    ax.set(xlabel="estimation à un tirage de d/dμ E[X²] = 2μ, en μ = 1", ylabel="densité", xlim=(-12, 16),
           ylim=(0, 0.42))
    ax.annotate("pic du score près de 0\n(coupé)", (0.0, 0.42), textcoords="offset points", xytext=(-115, -30),
                fontsize=8.5, color=C[1], arrowprops=dict(arrowstyle="->", color=C[1]))
    ax.set_title("X de loi N(1, 1), f(x) = x² : même espérance 2,\nvariances 4 (chemin) et 30 (score)",
                 fontsize=10.5)
    ax.legend(fontsize=8.3, loc="upper right")
    fig.tight_layout(w_pad=2.5)
    save(fig, "score_chemin.png")
    print(f"    path {path.mean():.4f} ± {path.std():.4f}; score {score.mean():.4f} ± {score.std():.4f}")


# --------------------------------------------------------------------------------------------------------- §3
def baseline_variance() -> None:
    rng = np.random.default_rng(8092)
    xs = np.arange(0, 80)
    p = poisson.pmf(xs, STARS_THETA)
    f = (xs >= STARS_K).astype(float)
    s = xs / STARS_THETA - 1
    d = float(np.sum(p * f * s))
    b_star = float(np.sum(p * f * s**2) / np.sum(p * s**2))
    ef = float(np.sum(p * f))
    var = lambda b: float(np.sum(p * (f - b) ** 2 * s**2) - d**2)  # noqa: E731
    fig, axes = plt.subplots(1, 2, figsize=(13.6, 4.6))
    ax = axes[0]
    bb = np.linspace(-0.4, 1.4, 300)
    ax.plot(bb, [var(b) for b in bb], color=C[0], lw=2.2, label="variance de (f − b)s à un tirage")
    for b, name, col in ((0.0, "b = 0", C[3]), (ef, f"b = E[f] ≈ {fr(ef, 3)}", C[2]),
                         (b_star, f"b* = E[fs²]/E[s²] ≈ {fr(b_star, 3)}", C[1])):
        ax.plot([b], [var(b)], "o", color=col, ms=8, label=f"{name} : {fr(var(b), 4)}")
    ax.set(xlabel="baseline b", ylabel="variance", ylim=(0, 0.42))
    ax.set_title("Étoiles filantes, f = 1{X ≥ 3}, θ = 2 : un trinôme en b,\n"
                 "minimal en b*, qui n'est pas E[f]", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="upper center")
    ax = axes[1]
    u = rng.uniform(size=300)
    cov = 1 - (math.e - 1) / 2
    c_star = cov / (1 / 12)
    ax.scatter(u, np.exp(u), s=9, color=C[0], alpha=0.7, label="300 tirages (U, e^U)")
    uu = np.linspace(0, 1, 2)
    ax.plot(uu, (math.e - 1) + c_star * (uu - 0.5), color=C[1], lw=1.8,
            label=f"e − 1 + c*(u − ½), c* ≈ {fr(c_star, 3)}")
    ax.set(xlabel="u", ylabel="e^u")
    ax.set_title("Une variable de contrôle : h = U, de moyenne ½ connue,\n"
                 "explique presque toute la variation de e^U (ρ² ≈ 0,984)", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="upper left")
    fig.tight_layout(w_pad=2.5)
    save(fig, "baseline_variance.png")
    print(f"    b* = {b_star:.4f}, E[f] = {ef:.4f}; var {var(0):.4f}, {var(ef):.4f}, {var(b_star):.4f}")


# --------------------------------------------------------------------------------------------------------- §4
def occupancy() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.5), gridspec_kw=dict(width_ratios=[1.1, 0.8, 1.0]))
    pi, p_pi, r_pi, m, v, q, a = dam_values(DAM_LOGITS)
    ax = axes[0]
    t = np.arange(0, 11)
    rows = np.array([(1 - DAM_GAMMA) * DAM_GAMMA**tt * np.linalg.matrix_power(p_pi, tt)[0] for tt in t])
    ax.bar(t, rows[:, 0], width=0.62, color=C[2], label="part de H")
    ax.bar(t, rows[:, 1], width=0.62, bottom=rows[:, 0], color=C[3], label="part de B")
    ax.plot(t, (1 - DAM_GAMMA) * DAM_GAMMA**t, "k_", ms=14, mew=1.5, label="poids (1 − γ)γᵗ du pas t")
    ax.set_xticks(t, [str(i) for i in t])
    ax.keep_ticks = True
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set(xlabel="pas t", ylabel="(1 − γ)γᵗ P(S_t = s | S₀ = H)")
    ax.set_title("Depuis H : le poids de chaque pas, partagé selon\nla loi de S_t ; leur somme sur t est ν_H",
                 fontsize=10.5)
    ax.legend(fontsize=8.5)
    ax = axes[1]
    nu = (1 - DAM_GAMMA) * m
    for k, (name, col) in enumerate((("départ s₀ = H", C[0]), ("départ s₀ = B", C[1]))):
        ax.bar(np.arange(2) + (k - 0.5) * 0.36, nu[k], width=0.36, color=col, label=name)
        for j in range(2):
            ax.text(j + (k - 0.5) * 0.36, nu[k, j] + 0.015, fr(nu[k, j], 3), ha="center", fontsize=8.5)
    ax.set_xticks([0, 1], ["H (haut)", "B (bas)"])
    ax.keep_ticks = True
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set(ylabel="ν_s₀(s), pour s₀ = H ou B", ylim=(0, 0.92))
    ax.set_title("Le barrage (γ = 0,6) : lois d'occupation", fontsize=10.5)
    ax.legend(fontsize=9, loc="upper center")
    ax = axes[2]
    grad = np.einsum("xs,sa,sa->xsa", m, pi, a)
    hs = np.logspace(-12, -0.3, 60)
    errs = []
    for h in hs:
        zp, zm = DAM_LOGITS.copy(), DAM_LOGITS.copy()
        zp[0, 0] += h
        zm[0, 0] -= h
        fd = (dam_values(zp)[4][0] - dam_values(zm)[4][0]) / (2 * h)
        errs.append(abs(fd - grad[0, 0, 0]))
    ax.loglog(hs, np.maximum(errs, 1e-17), color=C[0], lw=1.6, marker="o", ms=3)
    ax.set(xlabel="pas h", ylabel="|différence finie − formule|")
    ax.set_title("∂V(H)/∂z(H, T) : différences finies centrées\n"
                 f"contre la formule ({fr(grad[0, 0, 0], 4)})", fontsize=10.5)
    fig.tight_layout(w_pad=2.2)
    save(fig, "occupation.png")
    print(f"    nu = {nu.round(4).tolist()}, grad[H] = {grad[0].round(4).tolist()}, best h = {hs[int(np.argmin(errs))]:.1e}")


# --------------------------------------------------------------------------------------------------------- §5
def k_step_returns() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13.4, 4.5))
    ax = axes[0]
    k = np.arange(1, 13)
    for j, (lam, col) in enumerate(((0.6, C[0]), (0.7, C[1]))):
        w = (1 - lam) * lam ** (k - 1)
        ax.bar(k + (j - 0.5) * 0.36, w, width=0.36, color=col,
               label=f"λ = {french_number(lam)} : 1 − λ, puis ×λ à chaque pas")
    ax.set_xticks(k, [str(i) for i in k])
    ax.keep_ticks = True
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set(xlabel="nombre de pas k", ylabel="poids (1 − λ)λ^(k−1) de G^(k)")
    ax.set_title("Le λ-retour : une moyenne des retours à k pas,\nde poids géométriques de somme 1", fontsize=10.5)
    ax.legend(fontsize=8.5)
    ax = axes[1]
    pi, p_pi, *_ = dam_values(DAM_LOGITS)
    ks = np.arange(0, 11)
    bias = np.array([DAM_GAMMA**kk * np.linalg.matrix_power(p_pi, kk) @ DAM_ERROR for kk in ks])
    ax.plot(ks, bias[:, 0], "o-", color=C[2], lw=1.6, label="depuis H")
    ax.plot(ks, bias[:, 1], "s-", color=C[3], lw=1.6, label="depuis B")
    ax.plot(ks, DAM_GAMMA**ks, color="0.4", lw=1, ls="--", label="borne γᵏ ‖e‖∞")
    ax.set(xlabel="nombre de pas k", ylabel="biais γᵏ(Pᵏe)(s)", ylim=(-0.03, 1.08))
    ax.set_xticks(ks, [str(i) for i in ks])
    ax.keep_ticks = True
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set_title("Barrage : valeurs estimées trop hautes de 1 en H ;\nle biais du retour à k pas", fontsize=10.5)
    ax.legend(fontsize=9)
    fig.tight_layout(w_pad=2.5)
    save(fig, "retours_k_pas.png")
    print(f"    bias k=1: {bias[1].round(4)}, k=2: {bias[2].round(4)}")


# --------------------------------------------------------------------------------------------------------- §6
def importance() -> None:
    rng = np.random.default_rng(8093)
    fig, axes = plt.subplots(1, 2, figsize=(13.6, 4.6))
    ax = axes[0]
    x = np.linspace(0, 4, 400)
    p = np.exp(-x)
    ax.plot(x, p, color="black", lw=2.4, label="cible p : taux 1")
    for rate, col in ((0.5, C[0]), (3.0, C[1])):
        q = rate * np.exp(-rate * x)
        ax.plot(x, q, color=col, lw=1.6, label=f"proposition q : taux {french_number(rate)}")
        ax.plot(x, p / q, color=col, lw=1.6, ls="--", label=f"poids p/q (taux {french_number(rate)})")
    ax.set(xlabel="x", ylabel="densité, ou poids", ylim=(0, 3.2), xlim=(0, 4))
    ax.set_title("Une proposition à queue plus lourde : des poids bornés par 2 ;\n"
                 "à queue plus légère : des poids qui explosent", fontsize=10.5)
    ax.legend(fontsize=8.2, loc="upper right")
    ax = axes[1]
    rates = np.linspace(0.1, 3.0, 59)
    theory = np.where(rates < 2, rates * (2 - rates), 0.0)
    ax.plot(rates, theory, color="black", lw=2.0, label="θ(2 − θ) pour θ < 2, 0 au-delà (n → ∞)")
    n = 2000
    measured = []
    for rate in rates:
        xx = rng.exponential(1 / rate, size=n)
        lw = -xx - (math.log(rate) - rate * xx)
        w = np.exp(lw - lw.max())
        measured.append(w.sum() ** 2 / np.sum(w**2) / n)
    ax.plot(rates, measured, "o", color=C[0], ms=4, label="mesurée sur 2 000 tirages de q")
    ax.axvline(2.0, color="0.5", lw=0.8, ls=":")
    ax.set(xlabel="taux θ de la proposition q (cible : taux 1)", ylabel="taille effective / n", ylim=(0, 1.08))
    ax.set_title("Taille effective par tirage : n au mieux (q = p),\n"
                 "variance des poids infinie dès θ ≥ 2", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="upper right")
    fig.tight_layout(w_pad=2.5)
    save(fig, "importance.png")


# --------------------------------------------------------------------------------------------------------- §7
def bradley_terry() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13.6, 4.6))
    ax = axes[0]
    d = np.linspace(-4, 4, 300)
    ax.plot(d, 1 / (1 + np.exp(-d)), color=C[0], lw=2.4, label="σ(β_i − β_j)")
    ax.axhline(0.5, color="0.6", lw=0.8)
    ax.axvline(0, color="0.6", lw=0.8)
    d0 = 140 * math.log(10) / 400
    e0 = 1 / (1 + 10 ** (-140 / 400))
    ax.plot([d0], [e0], "o", color=C[1], ms=7)
    ax.annotate(f"écart de 140 points Elo : Δβ ≈ {fr(d0, 3)}, {fr(e0, 4)}", (d0, e0), textcoords="offset points",
                xytext=(12, -24), fontsize=9, color=C[1])
    ax.set(xlabel="écart de forces β_i − β_j", ylabel="P(i bat j)", ylim=(-0.02, 1.02))
    sec = ax.secondary_xaxis("top", functions=(lambda b: b * 400 / math.log(10), lambda r: r * math.log(10) / 400))
    sec.set_xlabel("écart de cotes Elo R_i − R_j (points)")
    sec.xaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set_title("Bradley-Terry et Elo : la même courbe, deux échelles", fontsize=10.5, pad=34)
    ax.legend(fontsize=9, loc="upper left")
    ax = axes[1]
    n_games = LEAGUE + LEAGUE.T
    wins = LEAGUE.sum(axis=1)
    p = np.ones(4)
    history = [np.log(p)]
    for _ in range(40):
        new = np.array([wins[i] / sum(n_games[i, j] / (p[i] + p[j]) for j in range(4) if j != i) for i in range(4)])
        new /= np.exp(np.log(new).mean())
        p = new
        history.append(np.log(p))
    history = np.array(history)
    for i, (col, style) in enumerate(((C[0], "o-"), (C[1], "s--"), (C[2], "o:"), (C[3], "o-"))):
        extra = " ; B et C confondues" if i == 2 else ""
        ax.plot(range(len(history)), history[:, i], style, ms=3.5 if i != 1 else 5, lw=1.4, color=col,
                mfc="none" if i == 1 else col, label=f"{PLAYERS[i]} ({int(wins[i])} victoires sur 12{extra})")
    ax.set(xlabel="balayage de l'algorithme de Zermelo", ylabel="force β (centrée)", xlim=(-0.5, 25))
    ax.set_title("Une ligue de tennis de table : les forces après chaque balayage\n"
                 f"tendent vers ({fr(history[-1, 0], 4)} ; 0 ; 0 ; {fr(history[-1, 3], 4)})", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="upper right", bbox_to_anchor=(1.0, 0.82))
    fig.tight_layout(w_pad=2.5)
    save(fig, "bradley_terry_elo.png")
    print(f"    strengths {history[-1].round(4)}")


# --------------------------------------------------------------------------------------------------------- §8
def gibbs() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13.6, 4.6))
    betas = np.logspace(-1.3, 1.7, 300)
    laws = np.array([PI_REF * np.exp(PROFIT / b) / np.sum(PI_REF * np.exp(PROFIT / b)) for b in betas])
    ax = axes[0]
    for i, col in enumerate((C[0], C[1], C[2], C[3])):
        ax.semilogx(betas, laws[:, i], color=col, lw=2, label=f"{FLOWERS[i]} (r = {french_number(PROFIT[i])})")
        ax.plot([betas[-1] * 1.25], [PI_REF[i]], "<", color=col, ms=6, clip_on=False)
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set(xlabel="β (échelle logarithmique)", ylabel="π*(x)", ylim=(-0.02, 1.02))
    ax.set_title("La loi de Gibbs π* ∝ π_ref·e^(r/β) : tout sur les pivoines quand β → 0,\n"
                 "la loi de l'an dernier π_ref (triangles) quand β → ∞", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="center right")
    ax = axes[1]
    value = np.array([b * math.log(np.sum(PI_REF * np.exp(PROFIT / b))) for b in betas])
    mean_r = laws @ PROFIT
    ax.semilogx(betas, value, color="black", lw=2.4, label="valeur β ln Z")
    ax.semilogx(betas, mean_r, color=C[1], lw=1.6, ls="--", label="bénéfice moyen E_π*[r]")
    ax.axhline(PROFIT.max(), color="0.5", lw=0.8, ls=":")
    ax.axhline(PI_REF @ PROFIT, color="0.5", lw=0.8, ls=":")
    ax.text(betas[0], PROFIT.max() + 0.05, "max r = 4", fontsize=9, color="0.3")
    ax.text(betas[0], PI_REF @ PROFIT - 0.17, "E_ref[r] = 2,05", fontsize=9, color="0.3")
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set(xlabel="β (échelle logarithmique)", ylabel="€ par botte", ylim=(1.75, 4.25))
    ax.set_title("La valeur β ln Z = E_π*[r] − β KL(π* ‖ π_ref),\n"
                 "entre E_ref[r] et max r", fontsize=10.5)
    ax.legend(fontsize=9, loc="center right")
    fig.tight_layout(w_pad=2.5)
    save(fig, "gibbs.png")


def main() -> int:
    print(f"Figures MB8 → {OUT.relative_to(ROOT)}")
    wbplot.set_style()
    score_fisher()
    score_path()
    baseline_variance()
    occupancy()
    k_step_returns()
    importance()
    bradley_terry()
    gibbs()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
