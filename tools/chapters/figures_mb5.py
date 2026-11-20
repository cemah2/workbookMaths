#!/usr/bin/env python
"""Draw the figures of chapter MB5 (used by Claude).

    python tools/chapters/figures_mb5.py

Writes small PNG files into chapitres/mb5_diffusion/figures/:
- §1: the heading error of a sailing boat under autopilot, an AR(1) with a = 0.7 and b = 1 (trajectories from 6° and
  from −4°, their mean and band; the variance from v₀ = 0 and v₀ = 5 towards 1/0.51, and the random walk a = 1); the
  survival of a four-leg race (risks 0.09, 0.03, 0.11, 0.13) between its two exponential bounds;
- §2: the bridge of a mechanical watch (variance 4 s² a day when worn, 1 s² a day from Saturday noon to Monday noon,
  x₀ = 0, x₇ = 11 s); three couplings of the same marginals N(0, 4t) (random walk, one draw, a fresh draw each day);
- §3: the share γ of the signal variance against the SNR in decibels, measurements of a bright (a = 5) and a faint
  (a = 0.5) source with a receiver b = 2, and the factor 1/√SNR as a curve;
- §4: the prices of twelve flats in three districts with the district means; the MSE and the MAE of a constant for
  a building permit answered in 18 or 42 days (probabilities 0.75 and 0.25);
- §5: spruce heights 0.6 N(8, 4) + 0.4 N(15, 1) measured by a drone with b = 2, the score of the noisy law, the
  optimal denoiser for three noise levels; the denoiser of the cloud 2, 5, 9 (weights 0.2, 0.5, 0.3) as b shrinks;
- §6: the chain of a box that fades (erasing probabilities 0.3 and 0.5) and the decomposition of its ELBO for x = 1;
- §7: guided laws p_c^(1+w) p_u^(−w) for the sea temperature (N(22, 4) in August, N(16, 16) over the year) and for a
  condition five times more spread than the whole; their precision λ(w);
- §8: a loaf cooling as x' = −0.05(x − 22) from 95 °C, Euler and midpoint against the exact solution, and their error
  at t = 20 against the number of evaluations of the field (log-log);
- §9: straight paths between data N(3, 0.45²) and noises, the trajectories of the mean field for these data, and for
  data on the two points −1.5 and 2.5.
The numbers are those of the fiche; none comes from workbookIA B1 to B5, nor from the exercises of MB5. The
figures that draw random numbers use the seeds 7691 (§1), 7692 and 7693 (§2), 7694 (§3), 7695 (§5) and 7696 (§9),
among the seeds 7691 to 7699 kept for the figures of MB5.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy.integrate import solve_ivp  # noqa: E402
from scipy.special import logsumexp  # noqa: E402
from scipy.stats import norm  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "mb5_diffusion" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

# §1: the autopilot (a = 0.7, b = 1) and the four-leg race
AR_A, AR_B = 0.7, 1.0
RACE_RISKS = [0.09, 0.03, 0.11, 0.13]
# §2: the watch (weekdays 4 s², weekend 1 s²), checked at +11 s after seven days; the couplings (4 s² a day)
WATCH_VAR = [4.0, 4.0, 4.0, 4.0, 4.0, 1.0, 1.0]
WATCH_END = 11.0
COUPLING_VAR = 4.0
# §3: a receiver b = 2, a bright source a = 5 and a faint one a = 0.5
RECEIVER_B, BRIGHT_A, FAINT_A = 2.0, 5.0, 0.5
# §4: twelve flats (k€) and a building permit
FLATS = {"Gare": [180, 200, 205, 215], "Centre": [290, 310, 330], "Port": [240, 250, 260, 270, 280]}
PERMIT_DAYS = ([18.0, 42.0], [0.75, 0.25])
# §5: the spruce heights and the drone; the cloud
SPRUCE_HEIGHTS = (np.array([0.6, 0.4]), np.array([8.0, 15.0]), np.array([4.0, 1.0]))
DRONE_B = 2.0
CLOUD = (np.array([0.2, 0.5, 0.3]), np.array([2.0, 5.0, 9.0]))
# §6: the fading box
RHO = (0.3, 0.5)
# §7: the sea temperature
SEA_C, SEA_U = (22.0, 4.0), (16.0, 16.0)
# §8: the loaf
LOAF = dict(x0=95.0, room=22.0, rate=0.05, t1=20.0)
# §9: Gaussian data and two points
FLOW_M, FLOW_TAU = 3.0, 0.45
TWO_POINTS = np.array([-1.5, 2.5])


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


def recursion_moments(a, b2, m0, v0):
    """Means and variances of x_t = a_t x_{t-1} + b_t ε_t, step by step."""
    m, v = [m0], [v0]
    for ak, bk2 in zip(a, b2):
        m.append(ak * m[-1])
        v.append(ak * ak * v[-1] + bk2)
    return np.array(m), np.array(v)


def posterior_mean(y, a, b, weights, means, variances):
    """E[x | y] for y = a x + b n and x a 1-D Gaussian mixture (point masses allowed), by log-sum-exp."""
    y = np.asarray(y, dtype=float)[..., None]
    pv = a * a * variances + b * b
    logw = np.log(weights) + norm.logpdf(y, a * means, np.sqrt(pv))
    r = np.exp(logw - logsumexp(logw, axis=-1, keepdims=True))
    ek = means + a * variances * (y - a * means) / pv
    return (r * ek).sum(axis=-1)


# --------------------------------------------------------------------------------------------------------- §1
def recurrence() -> None:
    rng = np.random.default_rng(7691)
    T = 20
    t = np.arange(T + 1)
    vinf = AR_B**2 / (1 - AR_A**2)
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.6))
    ax = axes[0]
    for start, col in ((6.0, C[0]), (-4.0, C[1])):
        for _ in range(6):
            x = [start]
            for _k in range(T):
                x.append(AR_A * x[-1] + AR_B * rng.standard_normal())
            ax.plot(t, x, color=col, lw=0.8, alpha=0.55)
        m, v = recursion_moments([AR_A] * T, [AR_B**2] * T, start, 0.0)
        ax.plot(t, m, color=col, lw=2.2, label=f"moyenne depuis {french_number(start)}°")
        ax.fill_between(t, m - 2 * np.sqrt(v), m + 2 * np.sqrt(v), color=col, alpha=0.12)
    for sgn in (-1, 1):
        ax.axhline(sgn * 2 * math.sqrt(vinf), color="black", lw=1, ls="--")
    ax.text(T, 2 * math.sqrt(vinf) + 0.25, "±2 × 1,40° (stationnaire)", ha="right", fontsize=8.5)
    ax.set(xlabel="minute t", ylabel="écart de cap x_t (degrés)")
    ax.set_title("AR(1), a = 0,7 et b = 1 : l'oubli du départ", fontsize=11)
    ax.legend(fontsize=8.5, loc="upper right")
    ax = axes[1]
    for v0, col in ((0.0, C[0]), (5.0, C[1])):
        _, v = recursion_moments([AR_A] * T, [AR_B**2] * T, 0.0, v0)
        ax.plot(t, v, "o-", color=col, ms=3.5, lw=1.4, label=f"a = 0,7, v₀ = {french_number(v0)}")
    ax.plot(t, t * AR_B**2, color=C[2], lw=1.6, ls="-.", label="a = 1 (marche aléatoire)")
    ax.axhline(vinf, color="black", lw=1, ls="--")
    ax.text(T, vinf + 0.15, "1/0,51 ≈ 1,96", ha="right", fontsize=8.5)
    ax.set(xlabel="minute t", ylabel="variance v_t", ylim=(0, 6))
    ax.set_title(r"La variance : $v_t = a^2 v_{t-1} + b^2$", fontsize=11)
    ax.legend(fontsize=8.5, loc="upper left")
    ax = axes[2]
    h = np.array(RACE_RISKS)
    k = np.arange(len(h) + 1)
    S = np.concatenate([[1.0], np.cumprod(1 - h)])
    H = np.concatenate([[0.0], np.cumsum(h)])
    H2 = np.concatenate([[0.0], np.cumsum(h * h)])
    ax.plot(k, np.exp(-H), "^--", color=C[1], ms=6, lw=1.2, label="e^(−H) (au-dessus)")
    ax.plot(k, S, "o-", color=C[0], ms=6, lw=2, label="survie Π(1 − h_k)")
    ax.plot(k, np.exp(-H - H2), "v--", color=C[2], ms=6, lw=1.2, label="e^(−H − Σh²) (au-dessous)")
    ax.annotate(f"S ≈ {fr(S[-1], 4)}", (4, S[-1]), textcoords="offset points", xytext=(-75, 28), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="0.3"))
    ax.set(xlabel="étape k", ylabel="probabilité de finir les k premières étapes")
    ax.set_xticks(k)
    ax.set_title("Une course en quatre étapes", fontsize=11)
    ax.legend(fontsize=8.5, loc="lower left")
    fig.tight_layout(w_pad=2.0)
    save(fig, "recurrence.png")
    print(f"    v_inf = {vinf:.4f}; S = {S[-1]:.4f}, bounds {math.exp(-H[-1] - H2[-1]):.4f}, {math.exp(-H[-1]):.4f}")


# --------------------------------------------------------------------------------------------------------- §2
def bridge() -> None:
    rng = np.random.default_rng(7692)
    V = np.concatenate([[0.0], np.cumsum(WATCH_VAR)])
    VT = V[-1]
    days = np.arange(len(V))
    mean = WATCH_END * V / VT
    sd = np.sqrt(V * (VT - V) / VT)
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    ax.fill_between(days, mean - 2 * sd, mean + 2 * sd, color=C[0], alpha=0.15, label="± 2 écarts-types")
    for _ in range(5):
        walk = np.concatenate([[0.0], np.cumsum(np.sqrt(WATCH_VAR) * rng.standard_normal(len(WATCH_VAR)))])
        path = walk - V / VT * (walk[-1] - WATCH_END)        # a walk conditioned on x_7 = 11 (same law as the bridge)
        ax.plot(days, path, "o-", color=C[0], lw=0.8, ms=3, alpha=0.6)
    ax.plot(days, mean, "o-", color=C[0], lw=2.4, ms=6, label="moyenne : 11 × V_s/22")
    ax.plot(days, WATCH_END * days / days[-1], ":", color=C[1], lw=1.8, label="selon le temps : 11 × s/7")
    ax.annotate("jeudi : N(6 ; 5,45)", (3, mean[3]), textcoords="offset points", xytext=(10, -34), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="0.3"))
    ax.axvspan(5, 7, color="0.85", alpha=0.5, lw=0)
    ax.text(6, -3.2, "week-end\n(1 s² par jour)", ha="center", fontsize=8.5, color="0.3")
    ax.set_xticks(days, ["lun.", "mar.", "mer.", "jeu.", "ven.", "sam.", "dim.", "lun."])
    ax.keep_ticks = True
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set(xlabel="jour (midi)", ylabel="avance de la montre x_s (s)", ylim=(-4.5, 16))
    ax.set_title("Le pont de la montre : x₀ = 0 et x₇ = 11 s", fontsize=11)
    ax.legend(fontsize=8.5, loc="upper left")
    save(fig, "pont.png")
    print(f"    day 3: mean {mean[3]:.3f}, var {sd[3] ** 2:.4f}; day 5: mean {mean[5]:.3f}, var {sd[5] ** 2:.4f}")


def couplings() -> None:
    rng = np.random.default_rng(7693)
    T = 9
    t = np.arange(T + 1)
    band = 2 * np.sqrt(COUPLING_VAR * t)
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.4), sharey=True)
    titles = ["A : un bruit frais ajouté chaque jour\ncorr(x_s, x_t) = √(s/t)",
              "B : un seul tirage U\ncorr(x_s, x_t) = 1",
              "C : un tirage frais chaque jour\ncorr(x_s, x_t) = 0"]
    for j, ax in enumerate(axes):
        ax.fill_between(t, -band, band, color="0.85", alpha=0.6, lw=0)
        for i in range(6):
            if j == 0:
                x = np.concatenate([[0.0], np.cumsum(math.sqrt(COUPLING_VAR) * rng.standard_normal(T))])
            elif j == 1:
                x = math.sqrt(COUPLING_VAR) * np.sqrt(t) * rng.standard_normal()
            else:
                x = math.sqrt(COUPLING_VAR) * np.sqrt(t) * rng.standard_normal(T + 1)
            style = dict(lw=1.2) if j < 2 else dict(ls="none")
            ax.plot(t, x, marker="o", ms=3, color=C[i % len(C)], **style)
        ax.set_title(titles[j], fontsize=10.5)
        ax.set_xlabel("jour t")
    axes[0].set_ylabel("dérive x_t (s) ; bande ± 2√(4t)")
    fig.suptitle("Trois couplages des mêmes lois marginales N(0, 4t)", fontsize=12, fontweight="bold")
    fig.tight_layout(w_pad=1.5)
    save(fig, "couplages.png")


# --------------------------------------------------------------------------------------------------------- §3
def snr() -> None:
    rng = np.random.default_rng(7694)
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.5))
    ax = axes[0]
    db = np.linspace(-25, 30, 400)
    ax.plot(db, 1 / (1 + 10 ** (-db / 10)), color=C[0], lw=2)
    for a, name, col in ((BRIGHT_A, "brillante", C[1]), (FAINT_A, "faible", C[2])):
        s = a * a / RECEIVER_B**2
        g = s / (1 + s)
        ax.plot([10 * math.log10(s)], [g], "o", color=col, ms=7)
        ax.annotate(f"source {name} : {fr(10 * math.log10(s), 2)} dB, γ ≈ {fr(g, 3)}", (10 * math.log10(s), g),
                    textcoords="offset points", xytext=(8, -14 if a > 1 else 8), fontsize=8.5)
    ax.set(xlabel="SNR en décibels (10 log₁₀ SNR)", ylabel="part γ de la variance du signal")
    ax.set_title("γ = SNR/(1 + SNR) : ln SNR = logit γ", fontsize=11)
    ax = axes[1]
    x = rng.standard_normal(300)
    n = rng.standard_normal(300)
    for a, name, col in ((BRIGHT_A, "brillante (a = 5)", C[1]), (FAINT_A, "faible (a = 0,5)", C[2])):
        ax.scatter(x, a * x + RECEIVER_B * n, s=9, color=col, alpha=0.55, label=f"source {name}")
    ax.set(xlabel="signal x", ylabel="mesure y = a x + 2 n")
    ax.set_title("300 mesures simulées, b = 2", fontsize=11)
    ax.legend(fontsize=8.5, loc="upper left")
    ax = axes[2]
    ax.semilogy(db, 10 ** (-db / 20), color=C[0], lw=2)
    ax.axhline(1, color="0.5", lw=0.8, ls=":")
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set(xlabel="SNR en décibels", ylabel="1/√SNR (échelle logarithmique)")
    ax.set_title("L'erreur sur x = l'erreur sur n × 1/√SNR", fontsize=11)
    fig.tight_layout(w_pad=2.0)
    save(fig, "snr.png")


# --------------------------------------------------------------------------------------------------------- §4
def conditional_expectation() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.5))
    ax = axes[0]
    allp = sum(FLATS.values(), [])
    for i, (name, prices) in enumerate(FLATS.items()):
        ax.plot([i] * len(prices), prices, "o", color=C[i], ms=7, alpha=0.8)
        ax.hlines(np.mean(prices), i - 0.3, i + 0.3, color=C[i], lw=2.5)
        ax.text(i + 0.33, np.mean(prices), fr(np.mean(prices), 0), va="center", fontsize=9)
    ax.axhline(np.mean(allp), color="black", lw=1, ls="--")
    ax.text(-0.55, np.mean(allp) + 4, "moyenne générale 252,5", ha="left", fontsize=8.5)
    ax.set_xticks(range(3), list(FLATS))
    ax.keep_ticks = True
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set(xlim=(-0.6, 2.8), ylabel="prix (k€)")
    within = sum(sum((y - np.mean(v)) ** 2 for y in v) for v in FLATS.values()) / len(allp)
    ax.set_title(f"MSE des moyennes de quartier ≈ {fr(within, 1)}, d'une constante ≈ {fr(np.var(allp), 1)}",
                 fontsize=10.5)
    ax = axes[1]
    vals, probs = PERMIT_DAYS
    c = np.linspace(10, 50, 401)
    mse = sum(p * (v - c) ** 2 for v, p in zip(vals, probs))
    mae = sum(p * np.abs(v - c) for v, p in zip(vals, probs))
    ax.plot(c, mse, color=C[0], lw=2, label="MSE E[(Y − c)²]")
    ax2 = ax.twinx()
    ax2.plot(c, mae, color=C[1], lw=2, label="MAE E|Y − c|")
    ax.plot([24], [108], "o", color=C[0], ms=7)
    ax.annotate("moyenne 24 : MSE 108", (24, 108), textcoords="data", xytext=(26, 480), fontsize=9,
                color=C[0], arrowprops=dict(arrowstyle="->", color=C[0]))
    ax2.plot([18], [6], "s", color=C[1], ms=7)
    ax2.annotate("médiane 18 : MAE 6", (18, 6), textcoords="offset points", xytext=(-40, 60), fontsize=9,
                 color=C[1], arrowprops=dict(arrowstyle="->", color=C[1]))
    ax.set(xlabel="prédiction constante c (jours)", ylabel="MSE")
    ax2.set_ylabel("MAE")
    ax2.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set_title("Un permis de construire : 18 jours (0,75) ou 42 jours (0,25)", fontsize=10.5)
    lines = ax.get_lines()[:1] + ax2.get_lines()[:1]
    ax2.legend(lines, [ln.get_label() for ln in lines], fontsize=8.5, loc="upper center")
    fig.tight_layout(w_pad=2.5)
    save(fig, "esperance_conditionnelle.png")
    print(f"    flats: within {within:.4f}, total {np.var(allp):.4f}")


# --------------------------------------------------------------------------------------------------------- §5
def denoiser() -> None:
    rng = np.random.default_rng(7695)
    w, mu, var = SPRUCE_HEIGHTS
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.6))
    ax = axes[0]
    xs = np.linspace(0, 22, 600)
    px = sum(wk * norm.pdf(xs, m, math.sqrt(v)) for wk, m, v in zip(w, mu, var))
    py = sum(wk * norm.pdf(xs, m, math.sqrt(v + DRONE_B**2)) for wk, m, v in zip(w, mu, var))
    k = rng.choice(2, size=4000, p=w)
    y = mu[k] + np.sqrt(var[k]) * rng.standard_normal(4000) + DRONE_B * rng.standard_normal(4000)
    ax.hist(y, bins=60, range=(0, 22), density=True, color="0.85", label="4 000 hauteurs relevées (simulées)")
    ax.plot(xs, px, color=C[0], lw=2, label="hauteurs vraies p_X")
    ax.plot(xs, py, color=C[1], lw=2, label="hauteurs relevées p_Y (b = 2)")
    ax.set(xlabel="hauteur (m)", ylabel="densité", ylim=(0, 0.25))
    ax2 = ax.twinx()
    dpy = sum(wk * norm.pdf(xs, m, math.sqrt(v + DRONE_B**2)) * (-(xs - m) / (v + DRONE_B**2))
              for wk, m, v in zip(w, mu, var))
    score = dpy / py
    ax2.plot(xs, score, color=C[2], lw=1.5, ls="--", label="score s_Y")
    ax2.axhline(0, color=C[2], lw=0.7, ls=":")
    zeros = xs[:-1][np.sign(score[:-1]) != np.sign(score[1:])]
    ax2.plot(zeros, np.zeros_like(zeros), "o", color=C[2], ms=6)
    ax2.set_ylabel("score s_Y(y)")
    ax2.set_ylim(-1.6, 2.4)
    ax2.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set_title("Le mélange des hauteurs et le score de p_Y", fontsize=11)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, fontsize=7.5, loc="upper center", ncol=2)
    ax = axes[1]
    ys = np.linspace(0, 22, 600)
    for b, col in ((3.0, C[0]), (DRONE_B, C[1]), (0.5, C[2])):
        ax.plot(ys, posterior_mean(ys, 1.0, b, w, mu, var), color=col, lw=2, label=f"b = {french_number(b)}")
    ax.plot(ys, ys, color="0.6", lw=0.8, ls=":", label="y (aucune correction)")
    ax.plot([12], [posterior_mean(12.0, 1.0, DRONE_B, w, mu, var)], "o", color="black", ms=5)
    ax.annotate("y = 12 : ≈ 12,12", (12, 12.12), textcoords="offset points", xytext=(10, -22), fontsize=9)
    ax.set(xlabel="hauteur relevée y (m)", ylabel="E[x | y]")
    ax.set_title("Le débruiteur optimal du mélange", fontsize=11)
    ax.legend(fontsize=8.5, loc="upper left")
    ax = axes[2]
    cw, cp = CLOUD
    ys = np.linspace(0, 11, 800)
    for b, col in ((1.5, C[0]), (0.7, C[1]), (0.2, C[2])):
        ax.plot(ys, posterior_mean(ys, 1.0, b, cw, cp, np.zeros(3)), color=col, lw=2, label=f"b = {french_number(b)}")
    for p_, wt in zip(cp, cw):
        ax.axhline(p_, color="0.7", lw=0.8, ls=":")
        ax.text(11, p_ + 0.15, f"point {french_number(p_)} (poids {french_number(wt)})", ha="right", fontsize=8)
    ax.plot([3.5, 7.0], [2.9 / 0.7, 6.5], "ko", ms=5)
    ax.annotate("≈ 4,14", (3.5, 2.9 / 0.7), textcoords="offset points", xytext=(-38, 6), fontsize=9)
    ax.annotate("6,5", (7.0, 6.5), textcoords="offset points", xytext=(6, -14), fontsize=9)
    ax.set(xlabel="mesure y (a = 1)", ylabel="E[x | y]")
    ax.set_title("Un nuage de trois points : il les recopie", fontsize=11)
    ax.legend(fontsize=8.5, loc="upper left")
    fig.tight_layout(w_pad=2.0)
    save(fig, "debruiteur.png")
    print(f"    score zeros of p_Y near {', '.join(f'{z:.2f}' for z in zeros)}")


# --------------------------------------------------------------------------------------------------------- §6
def elbo_chain() -> None:
    r1, r2 = RHO
    rec = r1 * math.log(0.5)
    q2 = {"1": (1 - r1) * (1 - r2), "?": 1 - (1 - r1) * (1 - r2)}
    kl_final = q2["1"] * math.log(q2["1"] / 0.2) + q2["?"] * math.log(q2["?"] / 0.6)
    back = (1 - r1) * r2 / q2["?"]
    kl_step = q2["?"] * (back * math.log(back / 0.15) + (1 - back) * math.log((1 - back) / 0.7))
    elbo = rec - kl_final - kl_step
    lnp = math.log(0.2 + 0.6 * (0.15 + 0.7 * 0.5))
    fig = plt.figure(figsize=(11.5, 7.2))
    ax = fig.add_axes([0.03, 0.56, 0.94, 0.4])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    nodes = {"x": 1.2, "z₁": 5.0, "z₂": 8.8}
    for name, xc in nodes.items():
        ax.add_patch(FancyBboxPatch((xc - 0.55, 1.55), 1.1, 0.9, boxstyle="round,pad=0.05", fc="#eef3fb",
                                    ec=C[0], lw=1.5))
        ax.text(xc, 2.0, name, ha="center", va="center", fontsize=15)
    for (a, b), txt in (((1.2, 5.0), "q : effacée avec 0,3"), ((5.0, 8.8), "q : effacée avec 0,5")):
        ax.add_patch(FancyArrowPatch((a + 0.65, 2.25), (b - 0.65, 2.25), arrowstyle="-|>", mutation_scale=18,
                                     color=C[0], lw=1.8))
        ax.text((a + b) / 2, 2.55, txt, ha="center", fontsize=10, color=C[0])
    for (a, b), txt in (((8.8, 5.0), "p : lisible reste lisible ;\n? → 0, 1 (0,15 chacun) ou ? (0,7)"),
                        ((5.0, 1.2), "p : recopie, ou pile ou face si ?")):
        ax.add_patch(FancyArrowPatch((a - 0.65, 1.75), (b + 0.65, 1.75), arrowstyle="-|>", mutation_scale=18,
                                     color=C[1], lw=1.8))
        ax.text((a + b) / 2, 0.85, txt, ha="center", fontsize=9.5, color=C[1])
    ax.text(8.8, 3.2, "p(z₂) : 0 (0,2), 1 (0,2), ? (0,6)", ha="center", fontsize=9.5, color=C[1])
    ax.text(5.0, 3.6, "processus aller q (au-dessus), modèle retour p (au-dessous)", ha="center", fontsize=11,
            fontweight="bold")
    ax = fig.add_axes([0.12, 0.08, 0.83, 0.4])
    labels = ["reconstruction\nE_q[ln p(x | z₁)]", "− KL finale", "− KL du pas retour", "ELBO", "ln p(x)"]
    vals = [rec, -kl_final, -kl_step, elbo, lnp]
    cols = [C[0], C[1], C[2], "0.35", "black"]
    left = 0.0
    for i, (lab, val, col) in enumerate(zip(labels, vals, cols)):
        if i < 3:
            ax.barh(i, val, left=left, color=col, alpha=0.85)
            ax.text(left + val - 0.01, i, fr(val, 4), va="center", ha="right", fontsize=9.5)
            left += val
        else:
            ax.barh(i, val, color=col, alpha=0.75)
            ax.text(val - 0.01, i, fr(val, 4), va="center", ha="right", fontsize=9.5)
    ax.axvline(lnp, color="black", lw=1, ls="--")
    ax.set_yticks(range(5), labels)
    ax.keep_ticks = True
    ax.xaxis.set_major_formatter(FuncFormatter(french_number))
    ax.invert_yaxis()
    ax.set(xlabel="nats", xlim=(-0.95, 0.05))
    ax.set_title(f"x = 1 : l'ELBO ({fr(elbo, 4)}) reste sous ln p(x) = ln 0,5 ({fr(lnp, 4)})", fontsize=11)
    save(fig, "chaine_elbo.png")
    print(f"    rec {rec:.4f}, kl_final {kl_final:.4f}, kl_step {kl_step:.4f}, elbo {elbo:.4f}, ln p {lnp:.4f}")


# --------------------------------------------------------------------------------------------------------- §7
def guided(mu_c, v_c, mu_u, v_u, w):
    lam = (1 + w) / v_c - w / v_u
    return ((1 + w) * mu_c / v_c - w * mu_u / v_u) / lam, 1 / lam


def guidance() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.5))
    ax = axes[0]
    xs = np.linspace(0, 32, 600)
    (mc, vc), (mu_, vu) = SEA_C, SEA_U
    ax.plot(xs, norm.pdf(xs, mu_, math.sqrt(vu)), color="0.5", lw=1.8, ls="--", label="p_u : l'année, N(16, 16)")
    ax.plot(xs, norm.pdf(xs, mc, math.sqrt(vc)), color=C[0], lw=2.2, label="p_c : août, N(22, 4)")
    for w, col in ((0.75, C[1]), (1.5, C[2]), (2.5, C[3])):
        m, v = guided(mc, vc, mu_, vu, w)
        ax.plot(xs, norm.pdf(xs, m, math.sqrt(v)), color=col, lw=1.6,
                label=f"w = {french_number(w)} : N({fr(m, 2)} ; {fr(v, 2)})")
    ax.set(xlabel="température de l'eau (°C)", ylabel="densité")
    ax.set_title("σ_c < σ_u : plus étroite, poussée loin de μ_u", fontsize=11)
    ax.legend(fontsize=8, loc="upper left")
    ax = axes[1]
    xs = np.linspace(-15, 35, 800)
    mu_c2, v_c2, mu_u2, v_u2 = 1.0, 5.0, 0.0, 1.0
    ax.plot(xs, norm.pdf(xs, mu_u2, 1.0), color="0.5", lw=1.8, ls="--", label="p_u = N(0, 1)")
    ax.plot(xs, norm.pdf(xs, mu_c2, math.sqrt(v_c2)), color=C[0], lw=2.2, label="p_c = N(1, 5)")
    for w, col in ((0.07, C[1]), (0.17, C[2]), (0.22, C[3])):
        m, v = guided(mu_c2, v_c2, mu_u2, v_u2, w)
        ax.plot(xs, norm.pdf(xs, m, math.sqrt(v)), color=col, lw=1.6,
                label=f"w = {french_number(w)} : variance {fr(v + 1e-9, 2)}")
    ax.set(xlabel="x", ylabel="densité")
    ax.set_title("σ_c² = 5σ_u² : plus de densité pour w ≥ 1/4", fontsize=11)
    ax.legend(fontsize=8, loc="upper right")
    ax = axes[2]
    ws = np.linspace(0, 1.2, 300)
    ax.plot(ws, (1 + ws) / vc - ws / vu, color=C[0], lw=2, label="eau de mer : 0,25 + 0,1875 w")
    ax.plot(ws, ((1 + ws) / v_c2 - ws / v_u2), color=C[1], lw=2, label="σ_c² = 5σ_u² (σ_u = 1) : (1 − 4w)/5")
    ax.axhline(0, color="black", lw=0.8)
    ax.plot([0.25], [0], "o", color=C[1], ms=7)
    ax.annotate("w* = 1/4", (0.25, 0), textcoords="offset points", xytext=(8, 10), fontsize=9)
    ax.set(xlabel="w", ylabel="précision λ(w)")
    ax.set_title("La précision de la loi guidée", fontsize=11)
    ax.legend(fontsize=8.5, loc="lower left")
    fig.tight_layout(w_pad=2.0)
    save(fig, "guidance.png")


# --------------------------------------------------------------------------------------------------------- §8
def euler(f, x0, t0, t1, n):
    h = (t1 - t0) / n
    xs, x = [x0], x0
    for k in range(n):
        x = x + h * f(t0 + k * h, x)
        xs.append(x)
    return np.array(xs)


def midpoint(f, x0, t0, t1, n):
    h = (t1 - t0) / n
    xs, x = [x0], x0
    for k in range(n):
        t = t0 + k * h
        x = x + h * f(t + h / 2, x + h / 2 * f(t, x))
        xs.append(x)
    return np.array(xs)


def euler_midpoint() -> None:
    x0, room, rate, t1 = LOAF["x0"], LOAF["room"], LOAF["rate"], LOAF["t1"]

    def f(_t, x):
        return -rate * (x - room)

    def exact(t):
        return room + (x0 - room) * np.exp(-rate * t)

    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.6))
    ax = axes[0]
    ts = np.linspace(0, t1, 300)
    ax.plot(ts, exact(ts), color="black", lw=2, label="solution exacte")
    for n, col, style in ((2, C[1], "o--"), (4, C[2], "s--")):
        ax.plot(np.linspace(0, t1, n + 1), euler(f, x0, 0, t1, n), style, color=col, lw=1.4, ms=6,
                label=f"Euler, {n} pas")
    ax.plot(np.linspace(0, t1, 3), midpoint(f, x0, 0, t1, 2), "D-", color=C[0], lw=1.4, ms=6,
            label="point milieu, 2 pas")
    ax.set(xlabel="t (minutes)", ylabel="température du pain (°C)")
    ax.set_title("x′ = −0,05 (x − 22), depuis 95 °C", fontsize=11)
    ax.legend(fontsize=8.5)
    ax = axes[1]
    ns = 2 ** np.arange(0, 9)
    err_e = [abs(euler(f, x0, 0, t1, n)[-1] - exact(t1)) for n in ns]
    err_m = [abs(midpoint(f, x0, 0, t1, n)[-1] - exact(t1)) for n in ns[:-1]]
    ax.loglog(ns, err_e, "o-", color=C[1], label="Euler (1 évaluation par pas)")
    ax.loglog(2 * ns[:-1], err_m, "D-", color=C[0], label="point milieu (2 évaluations par pas)")
    ax.loglog(ns, 30 / ns, ":", color=C[1], lw=1)
    ax.loglog(ns, 30 / ns**2, ":", color=C[0], lw=1)
    ax.text(40, 30 / 40 * 1.3, "pente −1", color=C[1], fontsize=9)
    ax.text(25, 30 / 25**2 * 0.45, "pente −2", color=C[0], fontsize=9)
    ax.xaxis.set_major_formatter(FuncFormatter(french_number))
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set(xlabel="évaluations du champ (échelle logarithmique)", ylabel="erreur en t = 20 (°C)")
    ax.set_title("À nombre d'évaluations égal", fontsize=11)
    ax.legend(fontsize=8.5, loc="lower left")
    fig.tight_layout(w_pad=2.5)
    save(fig, "euler_point_milieu.png")
    print(f"    exact {exact(t1):.4f}; Euler 2, 4: {euler(f, x0, 0, t1, 2)[-1]:.4f}, {euler(f, x0, 0, t1, 4)[-1]:.4f}; "
          f"midpoint 2, 4: {midpoint(f, x0, 0, t1, 2)[-1]:.4f}, {midpoint(f, x0, 0, t1, 4)[-1]:.4f}")


# --------------------------------------------------------------------------------------------------------- §9
def flow_matching() -> None:
    rng = np.random.default_rng(7696)
    m, tau = FLOW_M, FLOW_TAU
    s = np.linspace(0, 1, 200)
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.7), sharey=True)
    ax = axes[0]
    x0 = m + tau * rng.standard_normal(25)
    eps = rng.standard_normal(25)
    for a_, e_ in zip(x0, eps):
        ax.plot(s, (1 - s) * a_ + s * e_, color=C[0], lw=0.9, alpha=0.7)
    ax.set_title("Chemins droits x_s = (1 − s) x₀ + s ε", fontsize=11)
    ax.set_xlabel("s (0 : la donnée, 1 : le bruit)")
    ax.set_ylabel("x")
    ax = axes[1]
    sig = np.sqrt((1 - s) ** 2 * tau**2 + s**2)
    for z in norm.ppf(np.linspace(0.04, 0.96, 15)):
        ax.plot(s, (1 - s) * m + sig * z, color=C[1], lw=1.2)
    ax.plot(s, (1 - s) * m, color="black", lw=1, ls="--", label="z = 0 : droite")
    ax.set_title("Champ moyen, données N(3 ; 0,45²)", fontsize=11)
    ax.set_xlabel("s, suivi de 1 vers 0")
    ax.legend(fontsize=8.5, loc="upper right")
    ax = axes[2]
    w2 = np.array([0.5, 0.5])

    def field(si, x):
        if si <= 0:
            return np.zeros_like(x)
        e0 = posterior_mean(x, 1 - si, si, w2, TWO_POINTS, np.zeros(2))
        return (x - e0) / si

    starts = norm.ppf(np.linspace(0.04, 0.96, 14))        # an even number: no start on the watershed x = 0
    sol = solve_ivp(field, (1.0, 1e-3), starts, rtol=1e-8, atol=1e-10, dense_output=True)
    ss = np.linspace(1.0, 1e-3, 400)
    xs = sol.sol(ss)
    for row in xs:
        ax.plot(ss, row, color=C[2], lw=1.2)
    for p_ in TWO_POINTS:
        ax.plot([0], [p_], "ko", ms=6)
    ax.set_title("Champ moyen, données en −1,5 et 2,5", fontsize=11)
    ax.set_xlabel("s, suivi de 1 vers 0")
    for ax in axes:
        ax.set_xlim(-0.03, 1.03)
    fig.tight_layout(w_pad=1.5)
    save(fig, "flow_matching.png")
    print(f"    two points: ends {np.round(xs[:, -1], 3)}")


def main() -> int:
    print(f"Figures MB5 → {OUT.relative_to(ROOT)}")
    wbplot.set_style()
    recurrence()
    bridge()
    couplings()
    snr()
    conditional_expectation()
    denoiser()
    elbo_chain()
    guidance()
    euler_midpoint()
    flow_matching()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
