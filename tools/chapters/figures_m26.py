#!/usr/bin/env python
"""Draw the figures of chapter M26 (used by Claude).

    python tools/chapters/figures_m26.py

Writes small PNG files into chapitres/m26_markov_bellman/figures/:
- the transition graph of a shop's shelf (0, 1 or 2 items on Saturday evening; weekly demand 0, 1, 2 with
  probabilities 0.3, 0.5, 0.2; two items ordered when the shelf is empty, delivered a week later);
- a two-state machine (breakdown 0.12, repair 0.28: λ₂ = 0.6, π = (0.7, 0.3)) that forgets its start, next to the
  periodic chain 0 → 1 → 2 → 0, which never does;
- a web of four pages (links 1→2, 1→3, 2→3, 3→1, 4→1, 4→3) and its PageRank with d = 0.85;
- a shop website (home, product page, cart; purchase and exit absorbing) with its absorption probabilities h and
  mean numbers of pages t;
- the Bellman iterates of the shop (r = (−5, 7, 9), γ = 0.85), synchronous and in place, with the a priori and
  a posteriori bounds;
- optimal stopping with independent offers (uniform on [0, 1 000] €, storage cost 20 €, γ = 0.96): the value
  max(x, C*) and the continuation equation C = −20 + 0.96 E[max(X, C)], iterated from 0;
- the maximization bias: two settings of the same true accuracy 72 %, measured on 400 examples each, against the
  double estimator; and the density of max(Z₁, Z₂), of mean 1/√π.
The numbers are those of the fiche; none comes from workbookIA 26, B8 or its checkpoint VI (no agent, game, Q table,
no 26xx seed). Seed 6191.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy import stats  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m26_markov_bellman" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

# §1, §4–§6: the shelf
P_SHOP = np.array([[0.0, 0.0, 1.0], [0.7, 0.3, 0.0], [0.2, 0.5, 0.3]])
R_SHOP = np.array([-5.0, 7.0, 9.0])
GAMMA_SHOP = 0.85
# §2: the machine (running 0, broken 1)
BREAK, REPAIR = 0.12, 0.28
# §2: the web of four pages (0-based indices of pages 1 to 4)
LINKS = [(0, 1), (0, 2), (1, 2), (2, 0), (3, 0), (3, 2)]
DAMPING = 0.85
# §3: the website (transient: home, product, cart)
Q_SITE = np.array([[0.0, 0.6, 0.0], [0.3, 0.0, 0.4], [0.0, 0.2, 0.0]])
B_BUY = np.array([0.0, 0.0, 0.7])
B_EXIT = np.array([0.4, 0.3, 0.1])
# §7: optimal stopping (thousands of euros)
STORE_COST, GAMMA_SELL = 0.02, 0.96
# §8: maximization bias
TRUE_ACC, N_VAL, N_EXPERIMENTS = 0.72, 400, 20_000


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def fr(value: float, digits: int) -> str:
    return f"{value:.{digits}f}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and ax.axison:
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


# ----------------------------------------------------------------------------------------------- graph helpers
def node(ax, xy, label, r=0.36, fc="white", ec="0.15", fontsize=13, lw=1.6):
    ax.add_patch(Circle(xy, r, fc=fc, ec=ec, lw=lw, zorder=3))
    ax.text(*xy, label, ha="center", va="center", fontsize=fontsize, zorder=4)


def edge(ax, a, b, label=None, r=0.36, rad=0.0, color="0.15", label_offset=(0.0, 0.0), fontsize=11, lw=1.5,
         label_pos=0.5, r_end=None):
    """Arrow from the border of the circle at a to the border of the circle at b, optionally curved."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    u = (b - a) / np.linalg.norm(b - a)
    start, end = a + r * u, b - (r if r_end is None else r_end) * u
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=15, lw=lw, color=color,
                                 connectionstyle=f"arc3,rad={rad}", zorder=2))
    if label is not None:
        mid = start + label_pos * (end - start)
        normal = np.array([u[1], -u[0]])
        pos = mid + normal * rad * np.linalg.norm(end - start) * 0.5 + np.asarray(label_offset)
        ax.text(*pos, label, ha="center", va="center", fontsize=fontsize, zorder=5,
                bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.9))


def loop(ax, xy, label, direction=(0.0, 1.0), r=0.36, fontsize=11):
    """A self-loop drawn on the side ``direction`` of the node."""
    xy = np.asarray(xy, float)
    d = np.asarray(direction, float) / np.linalg.norm(direction)
    lr = 0.3
    centre = xy + d * (r + 0.55 * lr)
    back = math.atan2(-d[1], -d[0])                    # the direction of the node, seen from the centre
    angles = back + np.radians(np.linspace(55, 320, 60))
    pts = centre + lr * np.c_[np.cos(angles), np.sin(angles)]
    ax.plot(pts[:-1, 0], pts[:-1, 1], color="0.15", lw=1.5, zorder=2, solid_capstyle="round")
    ax.annotate("", xy=pts[-1], xytext=pts[-4], zorder=2,
                arrowprops=dict(arrowstyle="-|>", mutation_scale=13, lw=1.5, color="0.15", shrinkA=0, shrinkB=0))
    ax.text(*(xy + d * (r + 2 * lr + 0.28)), label, ha="center", va="center", fontsize=fontsize,
            bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.9))


# --------------------------------------------------------------------------------------------------------- §1
def shop_graph() -> None:
    """§1: the transition graph of the shelf."""
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    pos = {0: (0.0, 0.0), 1: (3.0, 0.0), 2: (1.5, 2.4)}
    names = {0: "0", 1: "1", 2: "2"}
    for s, xy in pos.items():
        node(ax, xy, names[s], r=0.42, fontsize=15)
    edge(ax, pos[0], pos[2], "1", r=0.42, rad=-0.25)
    edge(ax, pos[2], pos[0], "0,2", r=0.42, rad=-0.25)
    edge(ax, pos[2], pos[1], "0,5", r=0.42, rad=-0.2)
    edge(ax, pos[1], pos[0], "0,7", r=0.42, rad=0.0, label_offset=(0.0, -0.22))
    loop(ax, pos[1], "0,3", direction=(1.0, -0.3), r=0.42)
    loop(ax, pos[2], "0,3", direction=(0.0, 1.0), r=0.42)
    ax.text(0.0, -0.75, "étagère vide\n(livraison commandée)", ha="center", va="top", fontsize=9.5, color="0.3")
    ax.text(3.0, -0.75, "un article", ha="center", va="top", fontsize=9.5, color="0.3")
    ax.text(2.25, 2.9, "étagère pleine", ha="left", va="center", fontsize=9.5, color="0.3")
    ax.set_xlim(-1.4, 4.6)
    ax.set_ylim(-1.5, 3.95)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("La boutique : articles restants le samedi soir", fontsize=12)
    save(fig, "graphe_stock.png")


# --------------------------------------------------------------------------------------------------------- §2
def forgetting() -> None:
    """§2: the two-state machine forgets its start (λ₂ = 0.6); the periodic 3-cycle never does."""
    lam = 1 - BREAK - REPAIR
    pi0 = REPAIR / (BREAK + REPAIR)
    n = np.arange(0, 16)
    from_run = pi0 + (1 - pi0) * lam ** n
    from_broken = pi0 - pi0 * lam ** n
    P = np.array([[1 - BREAK, BREAK], [REPAIR, 1 - REPAIR]])
    mu = np.array([1.0, 0.0])
    check = []
    for _ in n:
        check.append(mu[0])
        mu = mu @ P
    assert np.allclose(check, from_run)

    fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.4), gridspec_kw={"width_ratios": [1.35, 1]})
    ax = axes[0]
    nn = np.linspace(0, 15, 300)
    ax.plot(nn, pi0 + (1 - pi0) * lam ** nn, ls=":", color=C[0], lw=1.3)
    ax.plot(nn, pi0 - pi0 * lam ** nn, ls=":", color=C[1], lw=1.3)
    ax.plot(n, from_run, "o-", color=C[0], lw=1.8, ms=5, label="départ : en marche")
    ax.plot(n, from_broken, "s-", color=C[1], lw=1.8, ms=5, label="départ : en panne")
    ax.axhline(pi0, color="0.3", lw=1.2, ls="--", label="loi stationnaire : 0,7")
    ax.set(xlabel="jour n", ylabel="P(Sₙ = en marche)", ylim=(-0.03, 1.03),
           title="La machine oublie son départ : écart × 0,6 chaque jour")
    ax.legend(fontsize=9.5, loc="center right")
    ax.grid(alpha=0.25)

    ax = axes[1]
    cyc = np.array([1.0 if k % 3 == 0 else 0.0 for k in n])
    ax.plot(n, cyc, "-", color=C[2], lw=0.9, alpha=0.5)
    ax.plot(n, cyc, "o", color=C[2], ms=6, label="départ : état 0")
    ax.axhline(1 / 3, color="0.3", lw=1.2, ls="--", label="loi stationnaire : 1/3")
    ax.set(xlabel="pas n", ylabel="P(Sₙ = 0)", ylim=(-0.05, 1.08), xticks=np.arange(0, 16, 3),
           title="La chaîne 0 → 1 → 2 → 0 ne converge pas")
    ax.legend(fontsize=9.5, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2)
    ax.grid(alpha=0.25)
    save(fig, "oubli_depart.png")


def pagerank_values() -> np.ndarray:
    m = 4
    L = np.zeros((m, m))
    for i, j in LINKS:
        L[i, j] = 1.0
    L /= L.sum(axis=1, keepdims=True)
    G = DAMPING * L + (1 - DAMPING) / m
    A = G.T - np.eye(m)
    A[-1] = 1.0
    return np.linalg.solve(A, np.r_[np.zeros(m - 1), 1.0])


def pagerank() -> None:
    """§2: the web of four pages, node sizes increasing with the PageRank."""
    pr = pagerank_values()
    pos = {0: (0.0, 0.0), 1: (2.6, 1.3), 2: (2.6, -1.3), 3: (-2.4, -1.3)}
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    radii = {k: 0.22 + 1.05 * math.sqrt(pr[k]) for k in pos}
    for i, j in LINKS:
        a, b = np.asarray(pos[i], float), np.asarray(pos[j], float)
        u = (b - a) / np.linalg.norm(b - a)
        rad = 0.18 if (j, i) in LINKS else 0.0
        ax.add_patch(FancyArrowPatch(a + radii[i] * u, b - radii[j] * u, arrowstyle="-|>", mutation_scale=15,
                                     lw=1.5, color="0.2", connectionstyle=f"arc3,rad={rad}", zorder=2))
    for k, xy in pos.items():
        ax.add_patch(Circle(xy, radii[k], fc=C[0], ec="0.15", alpha=0.35 + 0.6 * pr[k] / pr.max(), lw=1.4,
                            zorder=3))
        ax.text(xy[0], xy[1], f"page {k + 1}", ha="center", va="center", fontsize=11, zorder=4)
        ax.text(xy[0], xy[1] - radii[k] - 0.22, fr(pr[k], 4 if k == 3 else 3), ha="center", va="top",
                fontsize=10.5, zorder=4)
    ax.set_xlim(-3.4, 3.8)
    ax.set_ylim(-2.6, 2.3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("PageRank d'un web de quatre pages (d = 0,85)", fontsize=12)
    save(fig, "pagerank.png")


# --------------------------------------------------------------------------------------------------------- §3
def site() -> None:
    """§3: the shop website, absorbing purchase and exit, with h and t."""
    N = np.linalg.inv(np.eye(3) - Q_SITE)
    h = N @ B_BUY
    t = N @ np.ones(3)
    pos = {"A": (0.0, 0.0), "F": (3.0, 0.0), "K": (6.0, 0.0), "achat": (8.6, 1.4), "départ": (4.5, -2.6)}
    fig, ax = plt.subplots(figsize=(10.5, 4.8))
    r = 0.55
    labels = {"A": "accueil", "F": "fiche\nproduit", "K": "panier"}
    for k in ("A", "F", "K"):
        node(ax, pos[k], labels[k], r=r, fontsize=10.5)
    for k, col in (("achat", C[2]), ("départ", C[1])):
        x, y = pos[k]
        ax.add_patch(FancyBboxPatch((x - 0.75, y - 0.38), 1.5, 0.76, boxstyle="round,pad=0.05", fc=col, alpha=0.25,
                                    ec="0.15", lw=1.6, zorder=3))
        ax.text(x, y, k, ha="center", va="center", fontsize=11, zorder=4)
    edge(ax, pos["A"], pos["F"], "0,6", r=r, rad=-0.25)
    edge(ax, pos["F"], pos["A"], "0,3", r=r, rad=-0.25)
    edge(ax, pos["F"], pos["K"], "0,4", r=r, rad=-0.25)
    edge(ax, pos["K"], pos["F"], "0,2", r=r, rad=-0.25)
    edge(ax, pos["K"], pos["achat"], "0,7", r=r, rad=0.0, r_end=0.85)
    edge(ax, pos["A"], pos["départ"], "0,4", r=r, rad=0.15, label_pos=0.45, r_end=0.85)
    edge(ax, pos["F"], pos["départ"], "0,3", r=r, rad=0.0, label_pos=0.45, r_end=0.5)
    edge(ax, pos["K"], pos["départ"], "0,1", r=r, rad=-0.15, label_pos=0.45, r_end=0.5)
    for i, k in enumerate(("A", "F", "K")):
        x, y = pos[k]
        ax.text(x, y + 1.05, f"h ≈ {fr(h[i], 3)}\nt ≈ {fr(t[i], 2)}", ha="center", va="bottom", fontsize=10,
                color="0.15", bbox=dict(boxstyle="round,pad=0.25", fc="#f3f2ee", ec="0.7"))
    ax.set_xlim(-1.2, 9.8)
    ax.set_ylim(-3.4, 2.9)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Un site marchand : probabilité d'achat h et nombre moyen de pages t", fontsize=12)
    save(fig, "site_absorption.png")


# --------------------------------------------------------------------------------------------------------- §6
def bellman_iterates() -> None:
    """§6: synchronous and in-place iterates of the shop's Bellman operator, errors and bounds."""
    g = GAMMA_SHOP
    V = np.linalg.solve(np.eye(3) - g * P_SHOP, R_SHOP)
    K = 60
    sync = [np.zeros(3)]
    for _ in range(K):
        sync.append(R_SHOP + g * P_SHOP @ sync[-1])
    sync = np.array(sync)
    gs = [np.zeros(3)]
    W = np.zeros(3)
    for _ in range(K):
        for i in range(3):
            W[i] = R_SHOP[i] + g * P_SHOP[i] @ W
        gs.append(W.copy())
    gs = np.array(gs)
    err_s = np.abs(sync - V).max(axis=1)
    err_g = np.abs(gs - V).max(axis=1)
    k = np.arange(K + 1)
    k_s = int(np.argmax(err_s <= 0.01))
    k_g = int(np.argmax(err_g <= 0.01))

    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.6))
    ax = axes[0]
    for i in range(3):
        ax.plot(k[:31], sync[:31, i], "-", color=C[i], lw=1.8, label=f"V({i}), synchrone")
        ax.plot(k[:31], gs[:31, i], "--", color=C[i], lw=1.4, label=f"V({i}), en place")
        ax.axhline(V[i], color=C[i], lw=0.8, ls=":")
        ax.text(30.4, V[i], fr(V[i], 2), va="center", fontsize=9.5, color=C[i])
    ax.set(xlabel="itération k", ylabel="valeur (€)", xlim=(0, 33), title="Les itérés depuis V₀ = 0 (γ = 0,85)")
    ax.legend(fontsize=8.5, ncol=2, loc="lower right")
    ax.grid(alpha=0.25)

    ax = axes[1]
    ax.semilogy(k, err_s, "o-", ms=3, color=C[0], lw=1.6, label="erreur, synchrone")
    ax.semilogy(k, err_g, "s-", ms=3, color=C[1], lw=1.6, label="erreur, en place")
    ax.semilogy(k, err_s[0] * g ** k, ":", color="0.2", lw=1.6, label="borne a priori 33,48 × 0,85ᵏ")
    post = np.r_[np.nan, g / (1 - g) * np.abs(np.diff(sync, axis=0)).max(axis=1)]
    ax.semilogy(k, post, "--", color=C[3], lw=1.3, label="borne a posteriori (synchrone)")
    ax.axhline(0.01, color="0.45", lw=1, ls="-.")
    ax.annotate(f"0,01 : k = {k_s}", (k_s, 0.01), textcoords="offset points", xytext=(4, 8), fontsize=9.5,
                color=C[0])
    ax.annotate(f"k = {k_g}", (k_g, 0.01), textcoords="offset points", xytext=(-14, -15), fontsize=9.5,
                color=C[1])
    ax.set(xlabel="itération k", ylabel="‖Vₖ − V‖∞ (échelle log)", xlim=(0, K), ylim=(1e-4, 300),
           title="L'erreur et ses bornes")
    ax.legend(fontsize=8.8, loc="upper right")
    ax.grid(alpha=0.25, which="both")
    save(fig, "iteres_bellman.png")


# --------------------------------------------------------------------------------------------------------- §7
def stopping() -> None:
    """§7: optimal stopping with independent uniform offers; the threshold and the iterated equation."""
    c, g = -STORE_COST, GAMMA_SELL
    phi = lambda C_: c + g * (1 + C_ ** 2) / 2          # valid for 0 ≤ C ≤ 1   # noqa: E731
    a = g / 2
    c_star = (1 - math.sqrt(1 - 4 * a * (a + c))) / (2 * a)
    fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.6))
    ax = axes[0]
    x = np.linspace(0, 1, 400)
    ax.plot(1000 * x, 1000 * np.maximum(x, c_star), color=C[0], lw=2.2, label="V(x) = max(x, C*)")
    ax.plot(1000 * x, 1000 * x, ":", color="0.4", lw=1.2, label="accepter : x")
    ax.axhline(1000 * c_star, color=C[1], lw=1.2, ls="--", label=f"refuser : C* ≈ {fr(1000 * c_star, 2)} €")
    ax.axvline(1000 * c_star, color="0.5", lw=1, ls=":")
    ax.fill_between(1000 * x, 0, 1000, where=x < c_star, color=C[1], alpha=0.07)
    ax.fill_between(1000 * x, 0, 1000, where=x >= c_star, color=C[2], alpha=0.07)
    ax.text(330, 120, "on refuse", ha="center", fontsize=11, color=C[1])
    ax.text(845, 120, "on accepte", ha="center", fontsize=11, color=C[2])
    ax.set(xlabel="offre x (€)", ylabel="valeur (€)", xlim=(0, 1000), ylim=(0, 1000),
           title="Une règle à seuil")
    ax.legend(fontsize=9.5, loc="upper left")
    ax.grid(alpha=0.25)

    ax = axes[1]
    cc = np.linspace(0, 1, 400)
    ax.plot(1000 * cc, 1000 * phi(cc), color=C[0], lw=2.2, label="φ(C) = −20 + 0,96 E[max(X, C)]")
    ax.plot(1000 * cc, 1000 * cc, color="0.4", lw=1.2, ls=":", label="diagonale")
    it = [0.0]
    for _ in range(12):
        it.append(phi(it[-1]))
    xs, ys = [1000 * it[0]], [0.0]
    for k in range(len(it) - 1):
        xs += [1000 * it[k], 1000 * it[k + 1]]
        ys += [1000 * it[k + 1], 1000 * it[k + 1]]
    ax.plot(xs, ys, color=C[1], lw=1.1, label="itérés depuis C₀ = 0")
    ax.plot([1000 * c_star], [1000 * c_star], "o", color=C[3], ms=7, zorder=5)
    ax.annotate(f"C* ≈ {fr(1000 * c_star, 2)} €", (1000 * c_star, 1000 * c_star), textcoords="offset points",
                xytext=(10, -18), fontsize=10)
    ax.set(xlabel="C (€)", ylabel="φ(C) (€)", xlim=(0, 1000), ylim=(0, 1000),
           title="La valeur de continuation, point fixe d'une contraction")
    ax.legend(fontsize=9.2, loc="upper left")
    ax.grid(alpha=0.25)
    save(fig, "seuil_arret.png")


# --------------------------------------------------------------------------------------------------------- §8
def max_bias() -> None:
    """§8: the best of two equal settings is optimistic; the double estimator is not; max(Z₁, Z₂)."""
    rng = np.random.default_rng(6191)
    first = rng.binomial(N_VAL, TRUE_ACC, size=(N_EXPERIMENTS, 2)) / N_VAL
    second = rng.binomial(N_VAL, TRUE_ACC, size=(N_EXPERIMENTS, 2)) / N_VAL
    best = first.max(axis=1)
    chosen = first.argmax(axis=1)          # ties: the first setting
    double = second[np.arange(N_EXPERIMENTS), chosen]
    s = math.sqrt(TRUE_ACC * (1 - TRUE_ACC) / N_VAL)
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.6))
    ax = axes[0]
    bins = np.arange(-9.125, 9.2, 0.5)
    ax.hist(100 * (best - TRUE_ACC), bins=bins, color=C[1], alpha=0.55,
            label=f"meilleur score mesuré (moyenne {fr(100 * (best.mean() - TRUE_ACC), 2)})")
    ax.hist(100 * (double - TRUE_ACC), bins=bins, color=C[0], alpha=0.45,
            label=f"estimateur double (moyenne {fr(100 * (double.mean() - TRUE_ACC), 2)})")
    ax.axvline(100 * s / math.sqrt(math.pi), color=C[1], lw=2, ls="--")
    ax.axvline(0, color=C[0], lw=2, ls="--")
    ax.set(xlabel="score annoncé − 72 (points)", ylabel=f"nombre (sur {N_EXPERIMENTS // 1000} 000 expériences)",
           title=f"Deux réglages à 72 % : +σ/√π ≈ +{fr(100 * s / math.sqrt(math.pi), 2)} point (σ ≈ {fr(100 * s, 3)})")
    ax.set_ylim(0, 1.32 * ax.get_ylim()[1])
    ax.legend(fontsize=9.2, loc="upper left")
    ax.grid(alpha=0.25)

    ax = axes[1]
    z = np.linspace(-4, 4, 500)
    dens_max = 2 * stats.norm.pdf(z) * stats.norm.cdf(z)
    ax.plot(z, stats.norm.pdf(z), color=C[0], lw=2, label="loi de Z₁ (moyenne 0)")
    ax.plot(z, dens_max, color=C[1], lw=2, label=f"loi de max(Z₁, Z₂) (moyenne 1/√π ≈ {fr(1 / math.sqrt(math.pi), 3)})")
    ax.axvline(0, color=C[0], lw=1.2, ls="--")
    ax.axvline(1 / math.sqrt(math.pi), color=C[1], lw=1.2, ls="--")
    ax.set(xlabel="z", ylabel="densité", title="Le maximum de deux gaussiennes centrées réduites")
    ax.legend(fontsize=9.2, loc="upper left")
    ax.grid(alpha=0.25)
    save(fig, "biais_maximum.png")


def main() -> int:
    print(f"Figures M26 → {OUT.relative_to(ROOT)}")
    shop_graph()
    forgetting()
    pagerank()
    site()
    bellman_iterates()
    stopping()
    max_bias()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
