#!/usr/bin/env python
"""Draw the figures of chapter M25a (used by Claude).

    python tools/chapters/figures_m25a.py

Writes small PNG files into chapitres/m25a_gaussienne/figures/: the error of a GPS receiver, N(μ, Σ) with
μ = (2, −4) and Σ = [[16, 4], [4, 10]] (Cholesky factor L = [[4, 0], [1, 3]], eigenvalues 18 and 8), drawn as
μ + Lε, with its 80 % and 98 % ellipses, two points at the same Euclidean distance, and the same draws whitened;
the mass of a Mahalanobis ellipse, 1 − e^(−c²/2), against the 1-D mass, and the density of the norm of a draw of
N(0, I_d) for d = 2, 5, 26; the delays of a bus at three stops (μ = (2, 3, 5), Σ = [[1, 1, 1], [1, 2, 2], [1, 2, 4]]):
the joint law of the 2nd and 3rd delays, the slice x₂ = 5 and the conditional law N(7, 2) against the marginal
N(5, 4); the Bayesian regression of the stretch of a spring, y = θ F + w, prior N(2, 1), σ² = 0,25, after 0, 1, 3
and 12 measurements; the KL divergence between N(6, 4) and N(8, 9) in both directions, and an exponential law
against N(1, 1); the slerp of the camera of §8 (u = (1, 1, 0)/√2, v = (0, 1, 1)/√2, Ω = 60°) on the unit
sphere against the straight line, and the norm and the angle of the point for Ω = 60° and 120°.
The numbers are those of the fiche; none comes from workbookIA 25, B5 or its checkpoint VI (no encoder, no latent
code, no prior N(0, I) of a VAE, no 25xx seed). Randomness: the draws of the first figure (seed 5901) and the nine
extra measurements of the spring (seed 5902).
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
from scipy import special, stats  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m25a_gaussienne" / "figures"
C = wbplot.CATEGORICAL
DPI = 110
BOX = dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85)   # label on a cloud of points

GPS_MU = np.array([2.0, -4.0])                     # §1–§3: the error of a GPS receiver, in metres
GPS_COV = np.array([[16.0, 4.0], [4.0, 10.0]])     # Cholesky [[4, 0], [1, 3]], eigenvalues 18 and 8
LEVELS = [(0.80, 2 * math.log(5)), (0.98, 2 * math.log(50))]    # mass and c² of the two ellipses
BUS_MU = np.array([2.0, 3.0, 5.0])                 # §4: delays (min) of a bus at three stops
BUS_COV = np.array([[1.0, 1.0, 1.0], [1.0, 2.0, 2.0], [1.0, 2.0, 4.0]])
BUS_SEEN = 5.0                                     # §4: delay read at the second stop
SPRING_F = np.array([1.0, 2.0, 3.0])               # §5: masses (kg)
SPRING_Y = np.array([2.1, 3.9, 6.2])               # §5: stretches (cm)
SPRING_PRIOR = (2.0, 1.0)                          # §5: θ ~ N(2, 1) cm/kg
SPRING_NOISE = 0.25                                # §5: σ² (cm²)
KL_P = (6.0, 4.0)                                  # §7: p = N(6, 4)
KL_Q = (8.0, 9.0)                                  # §7: q = N(8, 9)
CAMERA_U = np.array([1.0, 1.0, 0.0]) / math.sqrt(2)  # §8: the camera turns from u to v (Ω = 60°)
CAMERA_V = np.array([0.0, 1.0, 1.0]) / math.sqrt(2)
SLERP_OMEGAS = (60.0, 120.0)                       # §8: angles of the norm and angle panels, in degrees


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and ax.axison:
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def ellipse(mu, cov, c2, n=300):
    """Points of the Mahalanobis ellipse (x − μ)ᵀ Σ⁻¹ (x − μ) = c² (as columns of a (2, n) array)."""
    s = np.linspace(0, 2 * np.pi, n)
    L = np.linalg.cholesky(cov)
    return mu[:, None] + math.sqrt(c2) * L @ np.vstack([np.cos(s), np.sin(s)])


# --------------------------------------------------------------------------------------------------------- §1–§3
def gps_ellipses() -> None:
    """§1–§3: draws μ + Lε, the 80 % and 98 % ellipses, the axes, two points; the same draws whitened."""
    rng = np.random.default_rng(5901)
    L = np.linalg.cholesky(GPS_COV)
    eps = rng.standard_normal((1500, 2))
    X = GPS_MU + eps @ L.T
    A = GPS_MU + np.array([4.0, 2.0])
    B = GPS_MU + np.array([2.0, -4.0])
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 5.6))
    ax = axes[0]
    ax.scatter(X[:, 0], X[:, 1], s=4, color=C[0], alpha=0.35, label="1 500 tirages μ + Lε")
    for (mass, c2), col in zip(LEVELS, (C[1], C[6])):
        e = ellipse(GPS_MU, GPS_COV, c2)
        ax.plot(e[0], e[1], color=col, lw=2, label=f"ellipse à {int(round(100 * mass))} % (c² = {french_number(round(c2, 2))})")
    q1 = np.array([2.0, 1.0]) / math.sqrt(5)
    q2 = np.array([1.0, -2.0]) / math.sqrt(5)
    c80 = math.sqrt(LEVELS[0][1])
    for q, lam, name in ((q1, 18.0, "c₈₀√18 le long de q₁"), (q2, 8.0, "c₈₀√8 le long de q₂")):
        tip = GPS_MU + c80 * math.sqrt(lam) * q
        ax.annotate("", tip, GPS_MU, arrowprops=dict(arrowstyle="->", color="0.15", lw=1.4))
        ax.annotate(name, tip, textcoords="offset points", xytext=(8, -14 if q is q2 else 4), fontsize=9.5,
                    bbox=BOX)
    circle = np.linspace(0, 2 * np.pi, 200)
    ax.plot(GPS_MU[0] + math.sqrt(20) * np.cos(circle), GPS_MU[1] + math.sqrt(20) * np.sin(circle), ":",
            color="0.35", lw=1.2, label="cercle de rayon √20 autour de μ")
    for P, name, d2, off in ((A, r"$\mathbf{x}_A$", "10/9", (-78, 30)), (B, r"$\mathbf{x}_B$", "5/2", (22, -6))):
        ax.plot(*P, "o", color=C[7], ms=7, zorder=4)
        ax.annotate(f"{name} : Δ² = {d2}", P, textcoords="offset points", xytext=off, fontsize=10, bbox=BOX,
                    arrowprops=dict(arrowstyle="-", color="0.25", lw=0.9))
    ax.plot(*GPS_MU, "k+", ms=12, mew=2)
    ax.annotate("μ", GPS_MU, textcoords="offset points", xytext=(-14, 6), fontsize=11)
    ax.set(xlim=(-14, 18), ylim=(-17, 9), aspect="equal", xlabel="erreur vers l'est x₁ (m)",
           ylabel="erreur vers le nord x₂ (m)", title="N(μ, Σ) : tirages, ellipses de niveau et axes propres")
    ax.legend(fontsize=8.6, loc="lower right")
    ax.grid(alpha=0.25)

    ax = axes[1]
    ax.scatter(eps[:, 0], eps[:, 1], s=4, color=C[0], alpha=0.35, label="les mêmes tirages ε = L⁻¹(x − μ)")
    for (mass, c2), col in zip(LEVELS, (C[1], C[6])):
        ax.plot(math.sqrt(c2) * np.cos(circle), math.sqrt(c2) * np.sin(circle), color=col, lw=2,
                label=f"cercle de rayon c = {math.sqrt(c2):.2f} ({int(round(100 * mass))} %)".replace(".", ","))
    for P, name in ((A, r"L⁻¹($\mathbf{x}_A$ − μ)"), (B, r"L⁻¹($\mathbf{x}_B$ − μ)")):
        w = np.linalg.solve(L, P - GPS_MU)
        ax.plot(*w, "o", color=C[7], ms=7, zorder=4)
        ax.annotate(f"{name}, de norme {french_number(round(float(np.linalg.norm(w)), 3))}", w,
                    textcoords="offset points", xytext=(7, 4), fontsize=9.5)
    ax.plot(0, 0, "k+", ms=12, mew=2)
    ax.set(xlim=(-4.2, 4.2), ylim=(-4.2, 4.2), aspect="equal", xlabel="ε₁", ylabel="ε₂",
           title="blanchis par L⁻¹ : la loi N(0, I), des cercles")
    ax.legend(fontsize=8.6, loc="lower right")
    ax.grid(alpha=0.25)
    fig.suptitle("L'erreur d'un récepteur GPS : μ = (2, −4), Σ de lignes (16, 4) et (4, 10), L de lignes (4, 0) et (1, 3)",
                 fontsize=11.5, y=1.0)
    save(fig, "ellipses_cholesky.png")


def ellipse_mass() -> None:
    """§3: 1 − e^(−c²/2) against P(|Z| ≤ c), and the density of ‖ε‖ for d = 2, 5, 26."""
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.6))
    ax = axes[0]
    c = np.linspace(0, 4, 400)
    ax.plot(c, 2 * stats.norm.cdf(c) - 1, color=C[0], lw=2, label="d = 1 : P(|Z| ≤ c), Z ~ N(0, 1)")
    ax.plot(c, 1 - np.exp(-c ** 2 / 2), color=C[1], lw=2, label="d = 2 : P(Δ ≤ c) = 1 − e^(−c²/2)")
    ax.plot([1.5, 1.5], [0, 2 * stats.norm.cdf(1.5) - 1], ":", color="0.4")
    for val, col in ((2 * stats.norm.cdf(1.5) - 1, C[0]), (1 - math.exp(-1.125), C[1])):
        ax.plot(1.5, val, "o", color=col, ms=7)
        ax.annotate(french_number(round(val, 3)), (1.5, val), textcoords="offset points", xytext=(-38, 4), fontsize=10,
                    color=col)
    for mass, c2 in LEVELS:
        cc = math.sqrt(c2)
        ax.plot(cc, mass, "s", color=C[6], ms=6)
        ax.annotate(f"{int(round(100 * mass))} % : c ≈ {french_number(round(cc, 3))}", (cc, mass),
                    textcoords="offset points", xytext=(6, -14), fontsize=9.5, color=C[6])
    ax.set(xlabel="niveau c (distance de Mahalanobis)", ylabel="masse de l'intervalle ou de l'ellipse", ylim=(0, 1.05), xlim=(0, 4),
           title="à niveau égal, l'ellipse du plan contient moins que l'intervalle")
    ax.legend(fontsize=9, loc="lower right")
    ax.grid(alpha=0.25)

    ax = axes[1]
    r = np.linspace(0, 8, 600)
    for d, col in ((2, C[1]), (5, C[2]), (26, C[6])):
        const = 1 / (2 ** (d / 2 - 1) * special.gamma(d / 2))
        f = const * r ** (d - 1) * np.exp(-r ** 2 / 2)
        ax.plot(r, f, color=col, lw=2, label=f"d = {d} : mode √{d - 1} = {french_number(round(math.sqrt(d - 1), 2))}")
        ax.axvline(math.sqrt(d - 1), color=col, ls=":", lw=1.2)
    ax.set(xlabel="r = ‖ε‖", ylabel="densité de la norme", xlim=(0, 8), ylim=(0, 0.82),
           title="la norme d'un tirage de N(0, I_d) : densité ∝ r^(d−1) e^(−r²/2)")
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(alpha=0.25)
    save(fig, "masse_ellipse.png")


# --------------------------------------------------------------------------------------------------------- §4
def conditioning() -> None:
    """§4: the joint law of (x₂, x₃), the slice x₂ = 5, the conditional law N(7, 2) against the marginal N(5, 4)."""
    mu = BUS_MU[1:]
    cov = BUS_COV[1:, 1:]
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 5.0), gridspec_kw={"width_ratios": [1.05, 1]})
    ax = axes[0]
    g2, g3 = np.meshgrid(np.linspace(-2, 9, 300), np.linspace(-3, 14, 300))
    dens = stats.multivariate_normal(mu, cov).pdf(np.dstack([g2, g3]))
    peak = stats.multivariate_normal(mu, cov).pdf(mu)
    levels = sorted(peak * np.exp(-np.array([0.5, 1.0, 1.5, 2.0, 2.5]) ** 2 / 2))
    ax.contour(g2, g3, dens, levels=levels, cmap=wbplot.sequential_cmap(), linewidths=1.3)
    xs = np.linspace(-2, 9, 10)
    ax.plot(xs, mu[1] + cov[1, 0] / cov[0, 0] * (xs - mu[0]), "--", color=C[1], lw=1.6,
            label="moyenne conditionnelle 5 + (x₂ − 3)")
    ax.axvline(BUS_SEEN, color=C[7], lw=2, label="la coupe x₂ = 5")
    cm = mu[1] + cov[1, 0] / cov[0, 0] * (BUS_SEEN - mu[0])
    ax.plot(BUS_SEEN, cm, "o", color=C[7], ms=7, zorder=4)
    ax.annotate("7", (BUS_SEEN, cm), textcoords="offset points", xytext=(8, -4), fontsize=10)
    ax.plot(*mu, "k+", ms=12, mew=2)
    ax.set(xlabel="retard au 2ᵉ arrêt x₂ (min)", ylabel="retard au 3ᵉ arrêt x₃ (min)", xlim=(-2, 9), ylim=(-3, 14),
           title="loi jointe de (x₂, x₃) : lignes de niveau")
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(alpha=0.25)

    ax = axes[1]
    t = np.linspace(-4, 15, 500)
    ax.plot(t, stats.norm(5, 2).pdf(t), color=C[0], lw=2, label="loi marginale de x₃ : N(5, 4)")
    ax.plot(t, stats.norm(7, math.sqrt(2)).pdf(t), color=C[7], lw=2, label="loi conditionnelle sachant x₂ = 5 : N(7, 2)")
    ax.fill_between(t, stats.norm(7, math.sqrt(2)).pdf(t), color=C[7], alpha=0.12)
    ax.set(xlabel="retard au 3ᵉ arrêt x₃ (min)", ylabel="densité", xlim=(-4, 15), ylim=(0, 0.32),
           title="la coupe, renormalisée : décalée et plus étroite")
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(alpha=0.25)
    fig.suptitle("Les retards d'un bus à trois arrêts : lire le 2ᵉ retard renseigne sur le 3ᵉ", fontsize=11.5, y=1.01)
    save(fig, "conditionnement.png")


# --------------------------------------------------------------------------------------------------------- §5
def bayes_regression() -> None:
    """§5: the predictive band (± 2 sd) of y = θ F + w after 0, 1, 3 and 12 measurements."""
    rng = np.random.default_rng(5902)
    extra_F = rng.uniform(0.5, 4.5, 9)
    extra_y = 2.05 * extra_F + math.sqrt(SPRING_NOISE) * rng.standard_normal(9)
    F_all = np.concatenate([SPRING_F, extra_F])
    y_all = np.concatenate([SPRING_Y, extra_y])
    m0, s0 = SPRING_PRIOR
    grid = np.linspace(0, 5, 200)
    fig, axes = plt.subplots(1, 4, figsize=(15.0, 4.3), sharey=True)
    for ax, n in zip(axes, (0, 1, 3, 12)):
        F, y = F_all[:n], y_all[:n]
        SN = 1 / (1 / s0 + F @ F / SPRING_NOISE)
        mN = SN * (m0 / s0 + F @ y / SPRING_NOISE)
        mean = mN * grid
        sd_f = np.sqrt(grid ** 2 * SN)
        sd_y = np.sqrt(grid ** 2 * SN + SPRING_NOISE)
        ax.fill_between(grid, mean - 2 * sd_y, mean + 2 * sd_y, color=C[0], alpha=0.18,
                        label="prédictive : moyenne ± 2 écarts-types")
        ax.fill_between(grid, mean - 2 * sd_f, mean + 2 * sd_f, color=C[0], alpha=0.35,
                        label="droite θF : ± 2 écarts-types")
        ax.plot(grid, mean, color=C[0], lw=2)
        if n:
            ax.plot(F, y, "o", color=C[1], ms=6, zorder=4, label="mesures")
        title = "a priori : θ ~ N(2, 1)" if n == 0 else f"après {n} mesure{'s' if n > 1 else ''}"
        ax.set(title=f"{title}\n$m_N$ = {french_number(round(mN, 3))}, $S_N$ = {french_number(round(SN, 4))}",
               xlabel="masse F (kg)", xlim=(0, 5), ylim=(-5, 22))
        ax.grid(alpha=0.25)
    axes[0].set_ylabel("allongement y (cm)")
    handles, labels = axes[-1].get_legend_handles_labels()
    fig.legend(handles, labels, fontsize=9.5, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.1))
    fig.suptitle("Régression linéaire bayésienne d'un ressort, y = θF + w, σ² = 0,25 : la bande se resserre quand "
                 "les mesures s'accumulent, et s'élargit avec F", fontsize=11.5, y=1.04)
    save(fig, "regression_bayesienne.png")


# --------------------------------------------------------------------------------------------------------- §7
def kl_both_ways() -> None:
    """§7: p = N(6, 4), q = N(8, 9), the two integrands and their areas; an exponential law against N(1, 1)."""
    p = stats.norm(KL_P[0], math.sqrt(KL_P[1]))
    q = stats.norm(KL_Q[0], math.sqrt(KL_Q[1]))
    t = np.linspace(-6, 20, 800)
    fig, axes = plt.subplots(1, 3, figsize=(15.0, 4.4))
    ax = axes[0]
    ax.plot(t, p.pdf(t), color=C[0], lw=2, label="p = N(6, 4)")
    ax.plot(t, q.pdf(t), color=C[1], lw=2, label="q = N(8, 9)")
    ax.set(xlabel="x", ylabel="densité", title="deux lois normales\n(moyennes et variances différentes)", xlim=(-4, 20))
    ax.legend(fontsize=9)
    ax.grid(alpha=0.25)

    ax = axes[1]
    f_pq = p.pdf(t) * (p.logpdf(t) - q.logpdf(t))
    f_qp = q.pdf(t) * (q.logpdf(t) - p.logpdf(t))
    k_pq = math.log(1.5) + 8 / 18 - 0.5
    k_qp = math.log(2 / 3) + 13 / 8 - 0.5
    ax.plot(t, f_pq, color=C[0], lw=2, label=f"p ln(p/q) : aire KL(p ‖ q) ≈ {k_pq:.3f}".replace(".", ","))
    ax.fill_between(t, f_pq, color=C[0], alpha=0.15)
    ax.plot(t, f_qp, color=C[1], lw=2, label=f"q ln(q/p) : aire KL(q ‖ p) ≈ {k_qp:.3f}".replace(".", ","))
    ax.fill_between(t, f_qp, color=C[1], alpha=0.15)
    ax.axhline(0, color="0.4", lw=0.8)
    ax.set(xlabel="x", title="ce qu'on intègre, dans les deux sens\n(les aires sont en nats)", xlim=(-4, 20))
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(alpha=0.25)

    ax = axes[2]
    t2 = np.linspace(-3, 6, 600)
    expo = np.where(t2 >= 0, np.exp(-np.clip(t2, 0, None)), 0.0)
    nrm = stats.norm(1, 1).pdf(t2)
    ax.plot(t2, expo, color=C[2], lw=2, label="loi exponentielle de paramètre 1")
    ax.plot(t2, nrm, color=C[6], lw=2, label="N(1, 1)")
    neg = t2 < 0
    ax.fill_between(t2[neg], nrm[neg], color=C[7], alpha=0.25,
                    label="masse de N(1, 1) là où l'exponentielle est nulle")
    ax.set(xlabel="x", title="supports différents : KL(N(1, 1) ‖ exp.) = +∞,\nmais KL(exp. ‖ N(1, 1)) ≈ 0,419", xlim=(-3, 6), ylim=(0, 1.08))
    ax.legend(fontsize=8.6, loc="upper right")
    ax.grid(alpha=0.25)
    save(fig, "kl_deux_sens.png")


# --------------------------------------------------------------------------------------------------------- §8
def slerp_figure() -> None:
    """§8: the camera of the fiche on the unit sphere (t = 0, ¼, ½, ¾, 1); norm and angle for Ω = 60° and 120°."""
    u, v = CAMERA_U, CAMERA_V
    Om = math.acos(float(u @ v))                                       # 60°
    ts = np.arange(5) / 4
    sl = np.array([(math.sin((1 - t) * Om) * u + math.sin(t * Om) * v) / math.sin(Om) for t in ts])
    li = np.array([(1 - t) * u + t * v for t in ts])
    arc = np.array([(math.sin((1 - t) * Om) * u + math.sin(t * Om) * v) / math.sin(Om)
                    for t in np.linspace(0, 1, 100)])
    fig = plt.figure(figsize=(15.5, 5.0))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.3, 1, 1])
    ax = fig.add_subplot(gs[0], projection="3d")
    a, b = np.meshgrid(np.linspace(0, 2 * np.pi, 37), np.linspace(0, np.pi, 19))
    ax.plot_wireframe(np.cos(a) * np.sin(b), np.sin(a) * np.sin(b), np.cos(b), color="0.82", lw=0.5)
    for P in sl:
        ax.plot([0, P[0]], [0, P[1]], [0, P[2]], color=C[0], lw=0.7, alpha=0.6)
    ax.plot(*arc.T, color=C[0], lw=1.8)
    ax.plot(*sl.T, "o", color=C[0], ms=7, label="slerp, t = 0, ¼, ½, ¾, 1 : sur l'arc")
    ax.plot(*np.vstack([u, v]).T, color=C[1], lw=1.2)
    ax.plot(*li.T, "s", color=C[1], ms=6, label="(1 − t) u + t v : sur la corde")
    for P, name in ((u, "u"), (v, "v")):
        ax.text(*(1.12 * P), name, fontsize=13)
    ax.plot([0], [0], [0], "k+", ms=9)
    ax.view_init(elev=math.degrees(math.asin(1 / math.sqrt(3))) - 8, azim=-45)   # almost along u × v
    ax.set_box_aspect((1, 1, 1), zoom=1.3)
    ax.set(xlim=(-1, 1), ylim=(-1, 1), zlim=(-1, 1))
    ax.set_axis_off()
    ax.set_title("la caméra du §8 : Ω = 60°, sur la sphère unité", fontsize=11)
    ax.legend(fontsize=9, loc="lower center", bbox_to_anchor=(0.5, -0.06))

    tt = np.linspace(0, 1, 200)
    ax_n = fig.add_subplot(gs[1])
    ax_a = fig.add_subplot(gs[2])
    ax_n.plot(tt, np.ones_like(tt), color=C[0], lw=2, label="slerp : 1")
    for deg, ls in zip(SLERP_OMEGAS, ("-", "--")):
        om = math.radians(deg)
        norm = np.sqrt((1 - tt) ** 2 + tt ** 2 + 2 * tt * (1 - tt) * math.cos(om))
        mid = french_number(round(math.cos(om / 2), 3))
        ax_n.plot(tt, norm, color=C[1], lw=2, ls=ls, label=f"ligne droite, Ω = {deg:g}° : {mid} au milieu")
        uu = np.array([1.0, 0.0])
        vv = np.array([math.cos(om), math.sin(om)])
        lin = (1 - tt)[:, None] * uu + tt[:, None] * vv
        ang = np.degrees(np.arctan2(lin[:, 1], lin[:, 0]))
        ax_a.plot(tt, deg * tt, color=C[0], lw=2, ls=ls, label=f"slerp, Ω = {deg:g}° : tΩ")
        ax_a.plot(tt, ang, color=C[1], lw=2, ls=ls, label=f"ligne droite, Ω = {deg:g}°")
    ax_n.set(xlabel="t", ylabel="norme", ylim=(0, 1.1), title="la norme du point")
    ax_n.legend(fontsize=9, loc="lower center")
    ax_n.grid(alpha=0.25)
    ax_a.set(xlabel="t", ylabel="angle avec u (degrés)", ylim=(0, 125),
             title="l'angle parcouru : la ligne droite est lente aux bouts")
    ax_a.legend(fontsize=8.6, loc="upper left")
    ax_a.grid(alpha=0.25)
    save(fig, "slerp.png")


def main() -> int:
    print(f"Figures M25a → {OUT.relative_to(ROOT)}")
    gps_ellipses()
    ellipse_mass()
    conditioning()
    bayes_regression()
    kl_both_ways()
    slerp_figure()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
