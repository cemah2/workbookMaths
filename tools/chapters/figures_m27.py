#!/usr/bin/env python
"""Draw the figures of chapter M27 (used by Claude).

    python tools/chapters/figures_m27.py

Writes small PNG files into chapitres/m27_jeux_distances/figures/:
- two payoff matrices: a 3 × 3 handball game (goals scored in ten attacks, saddle point 4, a dominated attack) and
  a 2 × 2 volleyball game (points won by the attack, in %, maximin 45 < minimax 60, no saddle point);
- the mixed strategies of the volleyball game: the guaranteed payoffs of the attack (p* = 0.3) and of the block
  (q* = 0.6), value 54;
- gradient descent-ascent on the mixed strategies of the volleyball game (step 0.4 on probabilities, the bilinear
  game κ(p − p*)(q − q*) with κ = −0.5): simultaneous steps spiral out, alternating steps stay on an ellipse;
- Jensen-Shannon against the shift θ, for two point masses and for N(0, 1) against N(θ, 1), next to W₁ = θ;
- Monge's earth on a road (piles at km 0, 2, 3 with masses 0.5, 0.3, 0.2; holes at km 1, 4 with 0.6, 0.4): the
  optimal plan and the independent one;
- the same laws: the area between the distribution functions and between the quantile functions (W₁ = 1.2);
- covariance ellipses of the two Fréchet examples (diag(3, 2) against [[5, 1], [1, 5]]; a commuting pair with
  eigenvalues 25, 1 and 9, 16 along the diagonals, means (0, 0) and (3, 3));
- the PSI of a drift of orders (items per order, January q = (0.42, 0.33, 0.16, 0.09), June p = (0.37, 0.32,
  0.19, 0.12)) and its approximation Σ(p − q)²/q along the path q + t (p − q), t from 0 to 8 (June: t = 1).
The numbers are those of the fiche; none comes from workbookIA 27, B7 or its checkpoint VI (no network, image,
generator, learning rate, no 27xx seed). Everything is deterministic: the seeds 6391 to 6399 reserved for these
figures are not needed.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Ellipse, FancyArrowPatch, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy import integrate, stats  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m27_jeux_distances" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

# §1: handball (rows: attacks, columns: defences; goals in ten attacks)
G_HAND = np.array([[5, 3, 7], [4, 2, 1], [6, 4, 5]], dtype=float)
# §1, §2, §4: volleyball (rows: attack left/right, columns: block left/right; % of points won by the attack)
G_VOLLEY = np.array([[40, 75], [60, 45]], dtype=float)
# §4: descent-ascent on the volleyball probabilities
ETA_GAME, N_STEPS, START = 0.4, 60, (0.38, 0.6)
# §7, §8: Monge's earth (déblais and remblais)
X_PILES, A_PILES = np.array([0.0, 2.0, 3.0]), np.array([0.5, 0.3, 0.2])
Y_HOLES, B_HOLES = np.array([1.0, 4.0]), np.array([0.6, 0.4])
PLAN_STAR = np.array([[0.5, 0.0], [0.1, 0.2], [0.0, 0.2]])
LABEL_POS = {(0, 0): (0.5, 0.3), (1, 0): (1.5, -0.42), (1, 1): (2.75, 0.43), (2, 1): (3.5, 0.3)}
# §9: Fréchet
S1_NC, S2_NC = np.diag([3.0, 2.0]), np.array([[5.0, 1.0], [1.0, 5.0]])
S1_C, S2_C = np.array([[13.0, 12.0], [12.0, 13.0]]), np.array([[12.5, -3.5], [-3.5, 12.5]])
MU1_C, MU2_C = np.array([0.0, 0.0]), np.array([3.0, 3.0])
# §10: items per order
Q_JAN = np.array([0.42, 0.33, 0.16, 0.09])
P_JUN = np.array([0.37, 0.32, 0.19, 0.12])


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def fr(value: float, digits: int) -> str:
    return f"{value:.{digits}f}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            keep = getattr(ax, "keep_ticks", False)                        # category labels stay as they are
            if axis.get_scale() == "linear" and ax.axison and not keep:
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


# --------------------------------------------------------------------------------------------------------- §1
def draw_matrix(ax, G, rows, cols, title, saddle=None, struck=(), fmt="{:g}"):
    m, n = G.shape
    ax.imshow(G, cmap=wbplot.sequential_cmap(), vmin=G.min() - 0.3 * np.ptp(G), vmax=G.max() + 0.1 * np.ptp(G))
    for i in range(m):
        for j in range(n):
            ax.text(j, i, fmt.format(G[i, j]), ha="center", va="center", fontsize=13,
                    color="0.55" if i in struck else "black")
    for i in struck:
        ax.plot([-0.45, n - 0.55], [i, i], color=wbplot.BAD, lw=2)
    if saddle is not None:
        ax.add_patch(Rectangle((saddle[1] - 0.45, saddle[0] - 0.45), 0.9, 0.9, fill=False, ec=wbplot.GOOD, lw=3))
    row_min, col_max = G.min(axis=1), G.max(axis=0)
    for i in range(m):
        ax.text(n - 0.35, i, fmt.format(row_min[i]), ha="left", va="center", fontsize=11, color=C[0])
    for j in range(n):
        ax.text(j, m - 0.35, fmt.format(col_max[j]), ha="center", va="top", fontsize=11, color=C[1])
    ax.text(n - 0.35, -0.55, "min de\nla ligne", ha="left", va="bottom", fontsize=9, color=C[0])
    ax.text(-0.6, m - 0.35, "max de la\ncolonne", ha="right", va="top", fontsize=9, color=C[1])
    ax.set_xticks(range(n), cols, fontsize=9.5)
    ax.set_yticks(range(m), rows, fontsize=9.5)
    ax.xaxis.tick_top()
    ax.set_xlim(-0.5, n + 0.3)
    ax.set_ylim(m + 0.25, -0.5)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.grid(False)
    ax.tick_params(length=0)
    ax.keep_ticks = True
    ax.set_title(title, fontsize=11, pad=40)


def matrices() -> None:
    """§1: a game with a saddle point (and a dominated row), a game without one."""
    fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.6), gridspec_kw={"width_ratios": [3.2, 2.4]})
    draw_matrix(axes[0], G_HAND, ["attaque 1", "attaque 2", "attaque 3"], ["défense 1", "défense 2", "défense 3"],
                "Handball : maximin = minimax = 4, point selle (3, 2)", saddle=(2, 1), struck=(1,))
    draw_matrix(axes[1], G_VOLLEY, ["attaque\nà gauche", "attaque\nà droite"], ["contre\nà gauche", "contre\nà droite"],
                "Volley (%) : maximin 45 < minimax 60")
    fig.tight_layout(w_pad=4)
    save(fig, "matrices_gains.png")


# --------------------------------------------------------------------------------------------------------- §2
def mixed() -> None:
    """§2: what each player of the volleyball game can guarantee with a mixed strategy."""
    (a, b), (c, d) = G_VOLLEY
    D = a - b - c + d
    p_star, q_star, v = (d - c) / D, (d - b) / D, (a * d - b * c) / D
    t = np.linspace(0, 1, 201)
    fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.4))
    ax = axes[0]
    vs_left, vs_right = a * t + c * (1 - t), b * t + d * (1 - t)
    ax.plot(t, vs_left, color=C[0], lw=1.6, label="contre à gauche : 60 − 20p")
    ax.plot(t, vs_right, color=C[1], lw=1.6, label="contre à droite : 45 + 30p")
    ax.plot(t, np.minimum(vs_left, vs_right), color="black", lw=3.2, alpha=0.6, label="garanti : le minimum")
    ax.plot([p_star], [v], "o", color="black", ms=7)
    ax.annotate(f"p* = {fr(p_star, 1)}, valeur {v:g}", (p_star, v), textcoords="offset points", xytext=(10, -22),
                fontsize=10)
    ax.set(xlabel="p : probabilité d'attaquer à gauche", ylabel="points gagnés par l'attaque (%)",
           title="L'attaque choisit p", ylim=(35, 80))
    ax2 = axes[1]
    pays_left, pays_right = a * t + b * (1 - t), c * t + d * (1 - t)
    ax2.plot(t, pays_left, color=C[2], lw=1.6, label="attaque à gauche : 75 − 35q")
    ax2.plot(t, pays_right, color=C[3], lw=1.6, label="attaque à droite : 45 + 15q")
    ax2.plot(t, np.maximum(pays_left, pays_right), color="black", lw=3.2, alpha=0.6, label="concédé au pire : le maximum")
    ax2.plot([q_star], [v], "o", color="black", ms=7)
    ax2.annotate(f"q* = {fr(q_star, 1)}, valeur {v:g}", (q_star, v), textcoords="offset points", xytext=(-40, 14),
                 fontsize=10)
    ax2.set(xlabel="q : probabilité de contrer à gauche", ylabel="points concédés par le contre (%)",
            title="Le contre choisit q", ylim=(35, 80))
    for axx in axes:
        axx.axhline(45, color="0.4", ls=":", lw=1)
        axx.axhline(60, color="0.4", ls="--", lw=1)
        axx.text(1.0, 45.6, "maximin 45", ha="right", fontsize=8.5, color="0.3")
        axx.text(1.0, 60.6, "minimax 60", ha="right", fontsize=8.5, color="0.3")
        axx.legend(fontsize=8.8, loc="upper center")
        axx.grid(alpha=0.25)
        axx.set_xlim(0, 1)
    fig.tight_layout()
    save(fig, "gain_mixte.png")


# --------------------------------------------------------------------------------------------------------- §4
def gda_volley(alternating: bool) -> np.ndarray:
    """Descent-ascent on E(p, q) = v + κ (p − p*)(q − q*) (κ = D here), probabilities, the block (q) moving first."""
    (a, b), (c, d) = G_VOLLEY / 100
    D = a - b - c + d
    p_star, q_star = (d - c) / D, (d - b) / D
    p, q = START
    path = [(p, q)]
    for _ in range(N_STEPS):
        q_new = q - ETA_GAME * D * (p - p_star)            # the block minimizes E
        p_new = p + ETA_GAME * D * ((q_new if alternating else q) - q_star)   # the attack maximizes E
        p, q = p_new, q_new
        path.append((p, q))
    return np.array(path)


def descent_ascent() -> None:
    """§4: simultaneous steps spiral out of the equilibrium, alternating steps stay on an ellipse."""
    p_star, q_star = 0.3, 0.6
    sim, alt = gda_volley(False), gda_volley(True)
    r0 = math.hypot(START[0] - p_star, START[1] - q_star)
    r_end = math.hypot(sim[-1, 0] - p_star, sim[-1, 1] - q_star)
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.0))
    for ax, path, title, col in ((axes[0], sim, f"Simultanée : une spirale (distance × {fr(r_end / r0, 1)} "
                                  f"en {N_STEPS} pas)", C[0]),
                                 (axes[1], alt, f"Alternée : une ellipse ({N_STEPS} pas)", C[1])):
        ax.plot(path[:, 0], path[:, 1], "-", color=col, lw=1.1, alpha=0.8)
        ax.plot(path[:, 0], path[:, 1], "o", color=col, ms=2.6)
        ax.plot(*START, "s", color="black", ms=7, label="départ")
        ax.plot(p_star, q_star, "*", color=wbplot.BAD, ms=14, label="équilibre (0,3 ; 0,6)")
        ax.set(xlabel="p : attaque à gauche", ylabel="q : contre à gauche", title=title, xlim=(0, 0.65),
               ylim=(0.25, 0.95), aspect="equal")
        ax.legend(fontsize=9, loc="lower right")
        ax.grid(alpha=0.25)
    fig.tight_layout()
    save(fig, "descente_montee.png")
    print(f"    start distance {r0:.4f}, simultaneous end {r_end:.4f} (× {r_end / r0:.3f}), "
          f"alternating max distance {np.hypot(alt[:, 0] - p_star, alt[:, 1] - q_star).max():.4f}")


# --------------------------------------------------------------------------------------------------------- §6
def js_gauss(theta: float) -> float:
    """JS(N(0, 1), N(θ, 1)) in nats, by numerical integration."""
    if theta == 0:
        return 0.0

    def integrand(x):
        p, q = stats.norm.pdf(x), stats.norm.pdf(x, theta)
        m = 0.5 * (p + q)
        out = 0.0
        if p > 0:
            out += 0.5 * p * math.log(p / m)
        if q > 0:
            out += 0.5 * q * math.log(q / m)
        return out

    return integrate.quad(integrand, -12, theta + 12, limit=200)[0]


def js_plateau() -> None:
    """§6: JS saturates at ln 2 when the supports separate; W₁ keeps growing."""
    th = np.linspace(0, 6, 241)
    js_g = np.array([js_gauss(t) for t in th])
    fig, ax = plt.subplots(figsize=(8.6, 4.6))
    h_d, = ax.plot(th[1:], np.full(len(th) - 1, math.log(2)), color=C[0], lw=2, label="JS(δ₀, δθ)")
    ax.plot([0], [0], "o", color=C[0], ms=7, zorder=6, clip_on=False)
    ax.plot([0], [math.log(2)], "o", mfc="white", mec=C[0], ms=6)
    h_g, = ax.plot(th, js_g, color=C[1], lw=2, label="JS(N(0, 1), N(θ, 1))")
    ax.axhline(math.log(2), color="0.35", lw=1, ls=":")
    ax.text(0.15, math.log(2) + 0.02, "ln 2 ≈ 0,693", fontsize=9.5, color="0.3")
    ax.set(xlabel="décalage θ", ylabel="Jensen-Shannon (nats)", ylim=(-0.03, 0.85), xlim=(-0.1, 6))
    ax2 = ax.twinx()
    h_w, = ax2.plot(th, th, color=C[2], lw=1.6, ls="--", label="W₁ = θ (les deux familles)")
    ax2.set_ylabel("W₁", color=C[2])
    ax2.set_ylim(-0.03 * 6 / 0.85, 6)
    ax2.grid(False)
    ax2.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.legend([h_d, h_g, h_w], [h.get_label() for h in (h_d, h_g, h_w)], fontsize=9.5, loc="center right")
    ax.grid(alpha=0.25)
    ax.set_title("JS plafonne et s'aplatit ; W₁ garde une pente de 1")
    save(fig, "js_plafond.png")
    print(f"    JS gauss: θ=1 {js_gauss(1):.4f}, θ=2 {js_gauss(2):.4f}, θ=4 {js_gauss(4):.4f}, θ=6 {js_gauss(6):.4f}")


# --------------------------------------------------------------------------------------------------------- §7
def plan() -> None:
    """§7: the earth of the road, the optimal plan as arrows, and the two plans as matrices."""
    cost = np.abs(X_PILES[:, None] - Y_HOLES[None, :])
    indep = np.outer(A_PILES, B_HOLES)
    fig = plt.figure(figsize=(12.5, 4.2))
    ax = fig.add_axes([0.03, 0.1, 0.52, 0.8])
    ax.axhline(0, color="0.3", lw=1.2)
    for x, a in zip(X_PILES, A_PILES):
        ax.add_patch(Rectangle((x - 0.18, 0.15), 0.36, a * 2.2, color=C[0], alpha=0.85))
        ax.text(x, 0.2 + a * 2.2, fr(a, 1), ha="center", va="bottom", fontsize=10.5, color=C[0])
    for y, b in zip(Y_HOLES, B_HOLES):
        ax.add_patch(Rectangle((y - 0.18, -0.15 - b * 2.2), 0.36, b * 2.2, color=C[1], alpha=0.85))
        ax.text(y, -0.2 - b * 2.2, fr(b, 1), ha="center", va="top", fontsize=10.5, color=C[1])
    for i, x in enumerate(X_PILES):
        for j, y in enumerate(Y_HOLES):
            w = PLAN_STAR[i, j]
            if w > 0:
                ax.add_patch(FancyArrowPatch((x, 0.1), (y, -0.1), arrowstyle="-|>", mutation_scale=14,
                                             lw=1 + 12 * w, color="0.2", alpha=0.7,
                                             connectionstyle="arc3,rad=-0.25"))
                lx, ly = LABEL_POS[(i, j)]
                ax.text(lx, ly, fr(w, 1), ha="center", fontsize=10, fontweight="bold")
    ax.text(-0.45, 0.9, "tas", color=C[0], fontsize=10)
    ax.text(-0.45, -1.1, "trous", color=C[1], fontsize=10)
    ax.set(xlim=(-0.6, 4.6), ylim=(-1.6, 1.6), xlabel="kilomètre")
    ax.set_yticks([])
    ax.set_title("Le plan optimal Γ* (aucune flèche ne croise une autre)", fontsize=11)
    for k, (P, name) in enumerate(((indep, "indépendant"), (PLAN_STAR, "Γ*"))):
        axm = fig.add_axes([0.60 + 0.205 * k, 0.12, 0.17, 0.72])
        axm.imshow(P, cmap=wbplot.sequential_cmap(), vmin=0, vmax=0.55)
        for i in range(3):
            for j in range(2):
                axm.text(j, i, fr(P[i, j], 2).rstrip("0").rstrip(",") if P[i, j] else "0", ha="center",
                         va="center", fontsize=11)
        axm.grid(False)
        axm.tick_params(length=0)
        axm.keep_ticks = True
        axm.set_xticks([0, 1], ["km 1", "km 4"])
        axm.set_yticks([0, 1, 2], ["km 0", "km 2", "km 3"])
        axm.set_title(f"{name} : coût {fr((P * cost).sum(), 2).rstrip('0').rstrip(',')}", fontsize=10.5)
    save(fig, "plan_transport.png")


# --------------------------------------------------------------------------------------------------------- §8
def cdf(points, masses, x):
    return np.array([masses[points <= v].sum() for v in np.atleast_1d(x)])


def quantile(points, masses, u):
    cum = np.cumsum(masses)
    return np.array([points[np.searchsorted(cum, v - 1e-12)] for v in np.atleast_1d(u)])


def cdf_quantiles() -> None:
    """§8: W₁ as the area between the distribution functions, and between the quantile functions."""
    x = np.linspace(-0.5, 4.5, 2001)
    F, G = cdf(X_PILES, A_PILES, x), cdf(Y_HOLES, B_HOLES, x)
    area = np.trapezoid(np.abs(F - G), x)
    u = np.linspace(1e-4, 1, 2001)
    Fi, Gi = quantile(X_PILES, A_PILES, u), quantile(Y_HOLES, B_HOLES, u)
    area_q = np.trapezoid(np.abs(Fi - Gi), u)
    fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.3))
    ax = axes[0]
    ax.step(x, F, where="post", color=C[0], lw=2, label="F (les tas)")
    ax.step(x, G, where="post", color=C[1], lw=2, label="G (les trous)")
    ax.fill_between(x, F, G, step="post", color="0.6", alpha=0.35, hatch="//", label=f"aire = {fr(area, 2)} = W₁")
    for xm, h in ((0.5, 0.5), (1.5, 0.1), (2.5, 0.2), (3.5, 0.4)):
        ax.text(xm, 1.04, fr(h, 1), ha="center", fontsize=9.5, color="0.25")
    ax.set(xlabel="kilomètre x", ylabel="fonction de répartition", ylim=(-0.03, 1.12),
           title="Entre F et G : 0,5 + 0,1 + 0,2 + 0,4 = 1,2")
    ax.legend(fontsize=9.2, loc="lower right")
    ax.grid(alpha=0.25)
    ax = axes[1]
    ax.step(u, Fi, where="pre", color=C[0], lw=2, label="F⁻¹ (les tas)")
    ax.step(u, Gi, where="pre", color=C[1], lw=2, label="G⁻¹ (les trous)")
    ax.fill_between(u, Fi, Gi, step="pre", color="0.6", alpha=0.35, hatch="\\\\", label=f"aire = {fr(area_q, 2)} = W₁")
    for b in (0.5, 0.6, 0.8):
        ax.axvline(b, color="0.5", lw=0.8, ls=":")
    ax.set(xlabel="u", ylabel="quantile (km)", xlim=(0, 1), ylim=(-0.2, 4.3),
           title="Entre F⁻¹ et G⁻¹ : la même aire")
    ax.legend(fontsize=9.2, loc="upper left")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    save(fig, "repartition_quantiles.png")
    print(f"    areas {area:.4f} {area_q:.4f}")


# --------------------------------------------------------------------------------------------------------- §9
def sqrtm_sym(S):
    w, V = np.linalg.eigh(S)
    return V @ np.diag(np.sqrt(np.clip(w, 0, None))) @ V.T


def frechet2(m1, S1, m2, S2):
    r1 = sqrtm_sym(S1)
    return float(np.sum((m1 - m2) ** 2) + np.trace(S1 + S2 - 2 * sqrtm_sym(r1 @ S2 @ r1)))


def ellipse(ax, mu, S, color, label, k=2.0):
    w, V = np.linalg.eigh(S)
    angle = math.degrees(math.atan2(V[1, 1], V[0, 1]))
    ax.add_patch(Ellipse(mu, 2 * k * math.sqrt(w[1]), 2 * k * math.sqrt(w[0]), angle=angle, fill=False, ec=color,
                         lw=2.2, label=label))
    ax.plot(*mu, "o", color=color, ms=5)


def frechet() -> None:
    """§9: the two Fréchet examples, as covariance ellipses (2 standard deviations)."""
    d_nc = frechet2(np.zeros(2), S1_NC, np.zeros(2), S2_NC)
    d_c = frechet2(MU1_C, S1_C, MU2_C, S2_C)
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.2))
    ax = axes[0]
    ellipse(ax, (0, 0), S1_NC, C[0], "Σ₁ = diag(3, 2)")
    ellipse(ax, (0, 0), S2_NC, C[1], "Σ₂ = [[5, 1], [1, 5]]")
    ax.set(xlim=(-6, 6), ylim=(-5, 5), aspect="equal",
           title=f"Ne commutent pas : W₂² = 5 + 10 − 2 × 7 = {d_nc:.0f}")
    ax = axes[1]
    ellipse(ax, MU1_C, S1_C, C[0], "écarts-types 5 et 1")
    ellipse(ax, MU2_C, S2_C, C[1], "écarts-types 3 et 4")
    for s in (-1, 1):
        ax.plot([-12, 12], [-12 * s, 12 * s], color="0.6", lw=0.8, ls=":")
    ax.set(xlim=(-11, 14), ylim=(-11, 14), aspect="equal", title=f"Mêmes axes : W₂² = 18 + 13 = {d_c:.0f}")
    for axx in axes:
        axx.legend(fontsize=9.5, loc="lower right")
        axx.grid(alpha=0.25)
        axx.axhline(0, color="0.75", lw=0.8)
        axx.axvline(0, color="0.75", lw=0.8)
    fig.tight_layout()
    save(fig, "frechet_ellipses.png")
    print(f"    Fréchet non commuting {d_nc:.4f}, commuting {d_c:.4f}")


# -------------------------------------------------------------------------------------------------------- §10
def psi(p, q):
    return float(np.sum((p - q) * np.log(p / q)))


def psi_curve() -> None:
    """§10: the PSI and its small-shift approximation along a growing drift p(t) = q + t (p_June − q), t from 0 to 8."""
    ts = np.linspace(0, 8, 321)
    psis, approx = [], []
    for t in ts:
        p = Q_JAN + t * (P_JUN - Q_JAN)
        psis.append(psi(p, Q_JAN))
        approx.append(float(np.sum((p - Q_JAN) ** 2 / Q_JAN)))
    psis, approx = np.array(psis), np.array(approx)
    cross = ts[1:][np.diff(np.sign(approx - psis))[0:] != 0]
    fig, ax = plt.subplots(figsize=(8.4, 4.5))
    ax.plot(ts, psis, color=C[0], lw=2.2, label="PSI = KL(p ‖ q) + KL(q ‖ p)")
    ax.plot(ts, approx, color=C[1], lw=1.8, ls="--", label="approximation Σ(pₖ − qₖ)²/qₖ")
    ax.plot([1.0], [psi(P_JUN, Q_JAN)], "o", color="black", ms=6, zorder=5)
    ax.annotate("juin (t = 1) : 0,0204 et 0,0219", (1.0, psi(P_JUN, Q_JAN)), textcoords="offset points",
                xytext=(10, 62), fontsize=9.5, arrowprops={"arrowstyle": "-", "color": "0.4"},
                bbox={"boxstyle": "round,pad=0.2", "fc": "white", "ec": "none"})
    ax.set(xlabel="t (juin vaut t = 1)", ylabel="nats",
           title="Le PSI et son approximation, le long d'une dérive qui grandit", xlim=(0, 8))
    ax.legend(fontsize=9.5, loc="upper left")
    ax.grid(alpha=0.25)
    save(fig, "psi_approximation.png")
    p_end = Q_JAN + 8 * (P_JUN - Q_JAN)
    print(f"    end of path p = {np.round(p_end, 3)}, PSI {psis[-1]:.4f}, approx {approx[-1]:.4f}; "
          f"curves cross near t = {cross[1:] if len(cross) > 1 else cross}")


def main() -> int:
    print(f"Figures M27 → {OUT.relative_to(ROOT)}")
    wbplot.set_style()
    matrices()
    mixed()
    descent_ascent()
    js_plateau()
    plan()
    cdf_quantiles()
    frechet()
    psi_curve()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
