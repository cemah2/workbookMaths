#!/usr/bin/env python
"""Draw the figures of chapter M25b (used by Claude).

    python tools/chapters/figures_m25b.py

Writes small PNG files into chapitres/m25b_variables_latentes/figures/: four directed graphs (a chain, a fork, a
collider, and the mixture model with its plate); the morning temperatures of a weather station, a mixture
(1/4) N(11, 4) + (3/4) N(3, 9) (overcast or clear night), with 4 000 ancestral draws and the responsibilities, which
cross near 8.3 °C and again near 26.5 °C; the EM of the same model on five mornings (2, 5, 8, 12, 13 °C) with only
the mean μ₁ free, started at 7 °C: the log-likelihood, the bound μ₁ ↦ ELBO(q_t, μ₁) of the first three iterations and
the gap, a sum of KL divergences; probabilistic PCA of the yields of two plots (w = (3, 2), σ² = 2, C = [[11, 6],
[6, 6]], M = 15), a season x − μ = (3, 3), its orthogonal projection and its posterior reconstruction, and the
posterior of z for three seasons; the principal angle between the line spanned by (1, 4, 0) and the plane spanned by
(1, 0, 0) and (0, 1, 1) (≈ 43.3°); the pathwise derivative of E[min(θξ, 3)], ξ ~ Exp(1), at θ = 2 (≈ 0.442), with
eight draws and 20 000 one-draw estimates.
The numbers are those of the fiche; none comes from workbookIA 25, B5 or its checkpoint VI (no encoder, no image, no
prior N(0, I) of a VAE, no 25xx seed). Seeds 6041, 6042, 6044 and 6046.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy import special, stats  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m25b_variables_latentes" / "figures"
C = wbplot.CATEGORICAL
DPI = 110
SUB = "₀₁₂₃"                            # subscripts for the iterations of the EM figure

PI = np.array([0.25, 0.75])            # §1–§5: overcast (z = 1) or clear (z = 2) night
MU = np.array([11.0, 3.0])             # morning temperatures (°C)
VAR = np.array([4.0, 9.0])
READING = 8.0                          # §2–§3: the reading of the example
MORNINGS = np.array([2.0, 5.0, 8.0, 12.0, 13.0])   # §4–§5: five mornings
MU1_START = 7.0                        # §5: start of the one-parameter EM of the figure
PPCA_W = np.array([3.0, 2.0])          # §6: two plots, one latent factor
PPCA_S2 = 2.0
PPCA_X = np.array([3.0, 3.0])          # §6: a season, x − μ
LINE_A = np.array([1.0, 4.0, 0.0])     # §6: principal angle between a line and a plane of R³
PLANE_B = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 1.0]])
VIEW = (18, -35)                          # §6: elevation and azimuth of the 3-D figure
LAMP_T = 3.0                           # §7: replacement after T years
LAMP_THETA = 2.0                       # §7: mean lifetime (years)


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def fr(value: float, digits: int) -> str:
    return f"{value:.{digits}f}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        if getattr(ax, "name", "") == "3d":
            continue
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and ax.axison:
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def log_joint(x, mu=MU, var=VAR, pi=PI):
    """a[i, k] = ln π_k + ln N(x_i | μ_k, σ_k²), for 1-D data."""
    x = np.atleast_1d(np.asarray(x, dtype=float))
    return np.log(pi) + stats.norm(mu, np.sqrt(var)).logpdf(x[:, None])


# --------------------------------------------------------------------------------------------------------- §1
def node(ax, xy, label, observed=False, r=0.42):
    ax.add_patch(Circle(xy, r, fc="0.82" if observed else "white", ec="0.15", lw=1.6, zorder=3))
    ax.text(*xy, label, ha="center", va="center", fontsize=14, zorder=4)


def arrow(ax, a, b, r=0.42, r_start=None):
    a, b = np.asarray(a, float), np.asarray(b, float)
    u = (b - a) / np.linalg.norm(b - a)
    r0 = r if r_start is None else r_start
    ax.add_patch(FancyArrowPatch(a + r0 * u, b - r * u, arrowstyle="-|>", mutation_scale=16, lw=1.5,
                                 color="0.15", zorder=2))


def directed_graphs() -> None:
    """§1: chain, fork, collider (observed middle node), and the mixture model with its plate."""
    fig, axes = plt.subplots(1, 4, figsize=(15.0, 3.9))
    specs = [
        ("chaîne a → c → b", {"a": (0, 0), "c": (1.6, 0), "b": (3.2, 0)}, [("a", "c"), ("c", "b")],
         "sachant c : a et b indépendants"),
        ("fourche a ← c → b", {"c": (1.6, 1.1), "a": (0.4, -0.4), "b": (2.8, -0.4)}, [("c", "a"), ("c", "b")],
         "sachant c : a et b indépendants"),
        ("collision a → c ← b", {"a": (0.4, 1.1), "b": (2.8, 1.1), "c": (1.6, -0.4)}, [("a", "c"), ("b", "c")],
         "a et b indépendants,\nmais dépendants sachant c"),
    ]
    for ax, (title, pos, edges, note) in zip(axes[:3], specs):
        for name, xy in pos.items():
            node(ax, xy, name, observed=(name == "c"))
        for s, t in edges:
            arrow(ax, pos[s], pos[t])
        ax.text(1.6, -1.6, note, ha="center", va="center", fontsize=10.5)
        ax.set_title(title, fontsize=12)
    ax = axes[3]
    ax.add_patch(FancyBboxPatch((0.7, -1.15), 1.8, 2.8, boxstyle="round,pad=0.05", fc="none", ec="0.35", lw=1.2))
    ax.text(2.45, -1.1, "i = 1, …, n", ha="right", va="bottom", fontsize=9.5)
    node(ax, (1.6, 1.0), "zᵢ")
    node(ax, (1.6, -0.25), "xᵢ", observed=True)
    arrow(ax, (1.6, 1.0), (1.6, -0.25))
    for xy, label in (((-0.2, 1.0), "π"), ((3.4, -0.25), "μₖ, Σₖ")):
        ax.plot(*xy, "o", color="0.15", ms=5)
        ax.text(xy[0], xy[1] + 0.32, label, ha="center", fontsize=11.5)
    arrow(ax, (-0.2, 1.0), (1.6, 1.0), r_start=0.0)
    arrow(ax, (3.4, -0.25), (1.6, -0.25), r_start=0.0)
    ax.text(1.6, -1.6, "le modèle de mélange (xᵢ observé)", ha="center", va="center", fontsize=10.5)
    ax.set_title("mélange : zᵢ → xᵢ", fontsize=12)
    for ax in axes:
        ax.set_xlim(-0.8, 4.0)
        ax.set_ylim(-1.95, 1.8)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.suptitle("Quatre graphes orientés (les nœuds grisés sont observés)", fontsize=12.5, y=1.02)
    save(fig, "graphes_orientes.png")


# --------------------------------------------------------------------------------------------------------- §2–§3
def mixture_responsibilities() -> None:
    """§2–§3: the station mixture, ancestral draws, the reading 8 °C, and the responsibilities r₁, r₂."""
    rng = np.random.default_rng(6041)
    z = rng.choice(2, size=4000, p=PI)
    draws = MU[z] + np.sqrt(VAR[z]) * rng.standard_normal(4000)
    t = np.linspace(-8, 34, 900)
    comp = PI * stats.norm(MU, np.sqrt(VAR)).pdf(t[:, None])
    fig, axes = plt.subplots(2, 1, figsize=(10.5, 7.2), sharex=True, gridspec_kw={"height_ratios": [1.25, 1]})
    ax = axes[0]
    ax.hist(draws, bins=70, density=True, color="0.85", ec="0.7", lw=0.4, label="4 000 tirages ancestraux")
    ax.plot(t, comp[:, 0], color=C[1], lw=2, label="(1/4) N(11, 4) : nuit couverte")
    ax.plot(t, comp[:, 1], color=C[0], lw=2, label="(3/4) N(3, 9) : nuit dégagée")
    ax.plot(t, comp.sum(axis=1), color="0.1", lw=2.2, ls="--", label="densité du mélange")
    ax.axvline(READING, color=C[7], lw=1.4, ls=":")
    ax.annotate("x = 8 °C", (READING, 0.09), textcoords="offset points", xytext=(6, 0), fontsize=10, color=C[7])
    ax.set(ylabel="densité", ylim=(0, 0.115), title="Températures à 6 h : un mélange de deux régimes")
    ax.legend(fontsize=9.2, loc="upper right")
    ax.grid(alpha=0.25)

    ax = axes[1]
    a = log_joint(t)
    r = np.exp(a - special.logsumexp(a, axis=1, keepdims=True))
    ax.plot(t, r[:, 0], color=C[1], lw=2, label="r₁(x) : nuit couverte")
    ax.plot(t, r[:, 1], color=C[0], lw=2, label="r₂(x) : nuit dégagée")
    r8 = float(np.exp(log_joint(READING)[0, 0] - special.logsumexp(log_joint(READING))))
    ax.plot(READING, r8, "o", color=C[7], ms=7, zorder=4)
    ax.annotate(f"r₁(8) ≈ {fr(r8, 3)}", (READING, r8), textcoords="offset points", xytext=(10, -16), fontsize=10)
    # the two crossings: log-odds −ln 2 − (x − 11)²/8 + (x − 3)²/18 = 0, i.e. −5x² + 174x − 1053 − 72 ln 2 = 0
    roots = np.sort(np.roots([-5.0, 174.0, -1053.0 - 72 * math.log(2)]).real)
    for x0 in roots:
        ax.axvline(x0, color="0.5", lw=1, ls=":")
        ax.annotate(f"{fr(x0, 1)} °C", (x0, 0.5), textcoords="offset points", xytext=(5, 6), fontsize=9.5, color="0.3")
    ax.set(xlabel="température x (°C)", ylabel="responsabilité", ylim=(-0.03, 1.03), xlim=(-8, 34),
           title="Les responsabilités se croisent deux fois : loin à droite, la composante large reprend le dessus")
    ax.legend(fontsize=9.2, loc="center", bbox_to_anchor=(0.66, 0.5))
    ax.grid(alpha=0.25)
    save(fig, "melange_responsabilites.png")


# --------------------------------------------------------------------------------------------------------- §4–§5
def em_bound() -> None:
    """§5: ℓ(μ₁) and the bounds ELBO(q_t, μ₁) of three EM iterations, with μ₂, σ², π fixed; the gap."""
    def loglik(m1):
        return np.array([special.logsumexp(log_joint(MORNINGS, mu=np.array([m, MU[1]])), axis=1).sum()
                         for m in np.atleast_1d(m1)])

    def resp(m1):
        a = log_joint(MORNINGS, mu=np.array([m1, MU[1]]))
        return np.exp(a - special.logsumexp(a, axis=1, keepdims=True))

    def elbo(R, m1):
        out = []
        for m in np.atleast_1d(m1):
            a = log_joint(MORNINGS, mu=np.array([m, MU[1]]))
            out.append(float(np.sum(np.where(R > 0, R * (a - np.log(np.where(R > 0, R, 1.0))), 0.0))))
        return np.array(out)

    grid = np.linspace(4.0, 16.0, 500)
    ll = loglik(grid)
    mus = [MU1_START]
    for _ in range(3):
        R = resp(mus[-1])
        mus.append(float((R[:, 0] * MORNINGS).sum() / R[:, 0].sum()))
    fig, axes = plt.subplots(1, 2, figsize=(14.0, 5.0), gridspec_kw={"width_ratios": [1.35, 1]})
    ax = axes[0]
    ax.plot(grid, ll, color="0.1", lw=2.4, label="log-vraisemblance ℓ(μ₁)")
    cols = [C[1], C[0], C[2]]
    for t in range(3):
        R = resp(mus[t])
        ax.plot(grid, elbo(R, grid), color=cols[t], lw=1.6, ls="--",
                label=f"borne ELBO(q{SUB[t]}, μ₁), touchant ℓ en μ₁ = {fr(mus[t], 2)}")
        ax.plot(mus[t], loglik(mus[t])[0], "o", color=cols[t], ms=7, zorder=4)
        ax.annotate("", (mus[t + 1], elbo(R, mus[t + 1])[0]), (mus[t], loglik(mus[t])[0]),
                    arrowprops=dict(arrowstyle="->", color=cols[t], lw=1.3))
    ax.plot(mus[3], loglik(mus[3])[0], "o", color="0.1", ms=6, zorder=4)
    ax.set(xlabel="moyenne μ₁ de la composante « couvert » (°C)", ylabel="nats", ylim=(ll.max() - 9, ll.max() + 0.8),
           xlim=(4, 16), title="L'EM monte la borne, puis la recolle : ℓ ne baisse jamais")
    ax.legend(fontsize=9, loc="lower right")
    ax.grid(alpha=0.25)

    ax = axes[1]
    for t in range(3):
        R = resp(mus[t])
        ax.plot(grid, ll - elbo(R, grid), color=cols[t], lw=2, label=f"t = {t} : nul en μ₁ = {fr(mus[t], 2)}")
        ax.plot(mus[t], 0, "o", color=cols[t], ms=6)
    ax.set(xlabel="μ₁ (°C)", ylabel="ℓ(μ₁) − ELBO(qₜ, μ₁) (nats)", xlim=(4, 16), ylim=(-0.2, 6),
           title="l'écart : la somme des KL(qₜ,ᵢ ‖ p(z | xᵢ, μ₁))")
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(alpha=0.25)
    fig.suptitle("Cinq matins (2, 5, 8, 12, 13 °C), le modèle de la station, seul μ₁ libre, parti de 7 °C",
                 fontsize=11.5, y=1.02)
    save(fig, "borne_em.png")


# --------------------------------------------------------------------------------------------------------- §6
def ppca() -> None:
    """§6: draws of the model, the line μ + ℝw, the marginal ellipse, a season, its projection and reconstruction."""
    rng = np.random.default_rng(6042)
    w, s2 = PPCA_W, PPCA_S2
    Cm = np.outer(w, w) + s2 * np.eye(2)
    M = float(w @ w + s2)
    Z = rng.standard_normal(400)
    X = Z[:, None] * w + math.sqrt(s2) * rng.standard_normal((400, 2))
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.4), gridspec_kw={"width_ratios": [1.1, 1]})
    ax = axes[0]
    ax.scatter(X[:, 0], X[:, 1], s=6, color=C[0], alpha=0.35, label="400 saisons tirées du modèle")
    tt = np.linspace(-4, 4, 10)
    ax.plot(tt * w[0], tt * w[1], color="0.25", lw=1.3, label="la droite μ + ℝw")
    s = np.linspace(0, 2 * np.pi, 300)
    L = np.linalg.cholesky(Cm)
    e = 2.0 * L @ np.vstack([np.cos(s), np.sin(s)])
    ax.plot(e[0], e[1], color=C[1], lw=1.8, label="ellipse de C (distance de Mahalanobis 2)")
    proj = (w @ PPCA_X) / (w @ w) * w
    rec = w * (w @ PPCA_X) / M
    ax.plot(*PPCA_X, "o", color=C[7], ms=8, zorder=5, label="une saison : x − μ = (3, 3)")
    ax.plot(*proj, "s", color="0.1", ms=7, zorder=5, label="projection orthogonale (45/13 ; 30/13)")
    ax.plot(*rec, "D", color=C[2], ms=7, zorder=5, label="reconstruction μ + w E[z | x] = (3, 2)")
    ax.plot([PPCA_X[0], proj[0]], [PPCA_X[1], proj[1]], ":", color="0.3", lw=1)
    ax.plot(0, 0, "k+", ms=12, mew=2)
    ax.annotate("μ", (0, 0), textcoords="offset points", xytext=(-14, 4), fontsize=11)
    ax.set(xlim=(-10, 10), ylim=(-8, 8), aspect="equal", xlabel="parcelle 1 (écart à la moyenne)",
           ylabel="parcelle 2 (écart à la moyenne)", title="ACP probabiliste : w = (3, 2), σ² = 2")
    ax.legend(fontsize=8.6, loc="lower right")
    ax.grid(alpha=0.25)

    ax = axes[1]
    zz = np.linspace(-3.2, 3.2, 600)
    ax.plot(zz, stats.norm.pdf(zz), color="0.55", lw=1.5, ls="--", label="a priori N(0, 1)")
    for x, col in ((np.array([3.0, 3.0]), C[7]), (np.array([-3.0, -1.0]), C[0]), (np.array([0.0, 4.0]), C[2])):
        m = float(w @ x) / M
        frac = Fraction(int(w @ x), int(M))
        ax.plot(zz, stats.norm(m, math.sqrt(s2 / M)).pdf(zz), color=col, lw=2,
                label=f"x − μ = ({x[0]:g}, {x[1]:g}) : N({frac} ; 2/15)".replace("-", "−"))
    ax.set(xlabel="z (qualité de la saison)", ylabel="densité", xlim=(-3.2, 3.2),
           title="le posterior de z : même largeur pour toute saison")
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(alpha=0.25)
    save(fig, "acp_probabiliste.png")


def principal_angle() -> None:
    """§6: the line spanned by (1, 4, 0), the plane spanned by (1, 0, 0) and (0, 1, 1), the projection, the angle."""
    QB = np.linalg.qr(PLANE_B.T)[0]
    u = LINE_A / np.linalg.norm(LINE_A)
    p = QB @ (QB.T @ u)
    phi = math.degrees(math.acos(np.linalg.norm(p)))
    fig = plt.figure(figsize=(7.6, 6.4))
    ax = fig.add_subplot(projection="3d")
    a, b = np.meshgrid(np.linspace(-1.2, 1.2, 9), np.linspace(-1.2, 1.2, 9))
    pts = a[..., None] * PLANE_B[0] + b[..., None] * PLANE_B[1] / math.sqrt(2)
    ax.plot_surface(pts[..., 0], pts[..., 1], pts[..., 2], color=C[0], alpha=0.18, edgecolor=C[0], lw=0.3)
    ax.plot(*np.vstack([-1.3 * u, 1.3 * u]).T, color=C[1], lw=2.4, label="droite A, dirigée par (1, 4, 0)")
    ax.plot(*np.vstack([0 * p, 1.3 * p / np.linalg.norm(p)]).T, color="0.15", lw=1.8, ls="--",
            label="sa projection orthogonale sur B")
    tip = 1.25 * u
    foot = QB @ (QB.T @ tip)
    ax.plot(*np.vstack([tip, foot]).T, ":", color="0.2", lw=1.6)
    ax.plot(*tip, "o", color=C[1], ms=5)
    ax.plot(*foot, "o", color="0.15", ms=5)
    arc = np.array([math.cos(t) * p / np.linalg.norm(p) + math.sin(t) * (u - p) / np.linalg.norm(u - p)
                    for t in np.linspace(0, math.radians(phi), 30)]) * 0.55
    ax.plot(*arc.T, color=C[7], lw=2)
    ax.text(*(0.75 * u + 0.15 * p / np.linalg.norm(p) - np.array([0.0, 0.0, 0.32])), f"φ₁ ≈ {fr(phi, 1)}°",
            fontsize=12, color=C[7])
    for v, name in ((PLANE_B[0], "(1, 0, 0)"), (PLANE_B[1] / math.sqrt(2), "(0, 1, 1)/√2")):
        ax.quiver(0, 0, 0, *v, color=C[0], lw=1.6, arrow_length_ratio=0.12)
        ax.text(*(1.08 * v), name, fontsize=10, color=C[0])
    ax.plot([0], [0], [0], "k+", ms=8)
    ax.set(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2), zlim=(-1.2, 1.2), xlabel="x₁", ylabel="x₂", zlabel="x₃",
           xticks=[-1, 0, 1], yticks=[-1, 0, 1], zticks=[-1, 0, 1])
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_major_formatter(FuncFormatter(french_number))
    ax.view_init(elev=VIEW[0], azim=VIEW[1])
    ax.set_box_aspect((1, 1, 1))
    ax.set_title("Plan B engendré par (1, 0, 0) et (0, 1, 1) : un seul angle principal avec la droite A",
                 fontsize=11)
    ax.legend(fontsize=9.5, loc="upper left")
    save(fig, "angles_principaux.png")


# --------------------------------------------------------------------------------------------------------- §7
def pathwise() -> None:
    """§7: θ ↦ min(θξ_j, T) for eight draws, their mean, J(θ) and its tangent at θ = 2; one-draw estimates."""
    rng = np.random.default_rng(6046)
    xi = rng.exponential(1.0, size=8)
    th = np.linspace(0.2, 6.0, 400)
    J = th * (1 - np.exp(-LAMP_T / th))
    u = LAMP_T / LAMP_THETA
    dJ = 1 - math.exp(-u) * (1 + u)
    J0 = LAMP_THETA * (1 - math.exp(-u))
    fig, axes = plt.subplots(1, 2, figsize=(14.0, 5.0))
    ax = axes[0]
    for j, x in enumerate(xi):
        ax.plot(th, np.minimum(th * x, LAMP_T), color=C[0], lw=1, alpha=0.55,
                label="min(θξⱼ, 3) pour huit tirages ξⱼ" if j == 0 else None)
    ax.plot(th, np.minimum(th[:, None] * xi, LAMP_T).mean(axis=1), color=C[0], lw=2.2,
            label="leur moyenne (huit tirages)")
    ax.plot(th, J, color="0.1", lw=2.4, label="J(θ) = θ(1 − e^(−3/θ)), exacte")
    tl = np.linspace(0.8, 3.6, 10)
    ax.plot(tl, J0 + dJ * (tl - LAMP_THETA), color=C[7], lw=2, ls="--",
            label=f"tangente en θ = 2, de pente J′(2) ≈ {fr(dJ, 3)}")
    ax.plot(LAMP_THETA, J0, "o", color=C[7], ms=7, zorder=4)
    ax.set(xlabel="durée de vie moyenne θ (années)", ylabel="durée d'usage (années)", xlim=(0.2, 6), ylim=(0, 3.2),
           title="La durée d'usage min(θξ, 3) : un coin par tirage, une espérance lisse")
    ax.legend(fontsize=9, loc="lower right")
    ax.grid(alpha=0.25)

    ax = axes[1]
    rng2 = np.random.default_rng(6044)
    g = rng2.exponential(1.0, size=20000)
    est = np.where(g < u, g, 0.0)
    zero = float(np.mean(est == 0))
    ax.hist(est[est > 0], bins=45, range=(0, u), density=False, color=C[0], alpha=0.75,
            label="estimations ξ 1{ξ < 1,5} non nulles")
    ax.bar([0.0], [np.sum(est == 0)], width=0.06, color=C[1], label=f"estimations nulles ({fr(100 * zero, 0)} % ; e^(−1,5) en théorie)")
    ax.axvline(est.mean(), color=C[7], lw=2, ls="--", label=f"moyenne {fr(est.mean(), 3)} (J′(2) ≈ {fr(dJ, 3)})")
    ax.set(xlabel="estimation à un tirage de J′(2)", ylabel="nombre (sur 20 000)",
           title=f"Sans biais, mais dispersée : écart-type ≈ {fr(est.std(), 2)}")
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(alpha=0.25)
    save(fig, "chemin_derivee.png")


def main() -> int:
    print(f"Figures M25b → {OUT.relative_to(ROOT)}")
    directed_graphs()
    mixture_responsibilities()
    em_bound()
    ppca()
    principal_angle()
    pathwise()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
