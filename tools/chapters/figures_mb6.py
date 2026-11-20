#!/usr/bin/env python
"""Draw the figures of chapter MB6 (used by Claude).

    python tools/chapters/figures_mb6.py

Writes small PNG files into chapitres/mb6_shapley_equite/figures/:
- §1: the six orders of arrival of a jazz trio (piano, double bass, drums) in a bar, with the marginal contribution
  of each musician (v(∅) = 20, v = 50, 30, 35 alone, 75, 90, 50 in pairs, 108 for the three: the hall is full);
  the weights of the coalitions for n = 5 (1/5, 1/20, 1/30, 1/20, 1/5), each size carrying 1/5 in all;
- §3: the fuel used by a ferry, f = 100 + 0.5 x₁² + 20 x₂ (wind x₁ ~ N(8, 3²), swell x₂ ~ N(1.5, 0.5²),
  correlation 0.8): the marginal mean (partial dependence) and the conditional mean of the swell; the ICE curves
  cos(x₁ − u) of a solar panel's orientation x₁ ∈ [−45°, 45°] for three positions of the sun (u = −45°, 0°, 45°)
  and their mean ((1 + √2)/3) cos x₁;
- §4: the gradient of the volume f = x₁²x₂ of a box with a square base, its level lines and three paths from
  (3, 1) to (4, 2) (all give 23); the field (x₁x₂, x₂²), which is not a gradient, along three paths from (0, 1) to
  (2, 2) (13/3, 17/3, 19/3);
- §4: the two shares of the variation of the volume (along the segment 32/3 and 37/3; the staircases 7 and 16, 14
  and 9; their mean 10.5 and 12.5) and a capped expense scale min(0.3 d + 5 n, 60) along two segments;
- §5: a profile of three depths (4, 7, 5 m) upscaled to nine values with the centres or the corners aligned;
- §6: the ranks given by two climbing guidebooks to eight routes (one tie), and a noisy increasing relation with its
  Pearson and Spearman correlations;
- §8: the ROC points of a forecast that takes few values, the chords between them, and the point reached by drawing
  between the thresholds of (0.02, 0.71) and (0.32, 0.95) to get a detection rate of 0.89.
The numbers are those of the fiche; none comes from workbookIA B1 to B7, nor from the exercises of MB6. The figures
that draw random numbers use the seeds 7891 (§3) and 7895 (§6), among the seeds 7891 to 7899 kept for MB6.
"""

from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from scipy.stats import pearsonr, rankdata, spearmanr  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "mb6_shapley_equite" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

# §1: the jazz trio in a bar (tickets sold), the hall holds 108
TRIO = {"": 20, "P": 50, "C": 30, "B": 35, "PC": 75, "PB": 90, "CB": 50, "PCB": 108}
NAMES = {"P": "piano", "C": "contrebasse", "B": "batterie"}
# §3: the ferry and the solar panel
WIND, SWELL, RHO = (8.0, 3.0), (1.5, 0.5), 0.8
SUN = (-45.0, 0.0, 45.0)
# §4: the box and the non-gradient field
BOX_R, BOX_X = (3.0, 1.0), (4.0, 2.0)
FIELD_A, FIELD_B = (0.0, 1.0), (2.0, 2.0)
SCALE = dict(per_km=0.3, per_night=5.0, cap=60.0, x=(160.0, 4.0), r2=(80.0, 2.0))
# §5: a profile of three depths
PROFILE = np.array([4.0, 7.0, 5.0])
# §6: two climbing guidebooks
GRADES = ["5a", "5b", "5c", "6a", "6a+", "6b", "6b+", "6c", "6c+", "7a", "7a+"]
TOPO1 = {"A": "5c", "B": "6a", "C": "6b+", "D": "6a+", "E": "7a", "F": "6b", "G": "6c", "H": "5b"}
TOPO2 = {"A": "6a", "B": "5c", "C": "6b", "D": "6b", "E": "6c+", "F": "6a+", "G": "7a", "H": "5b"}
# §8: the ROC points of a forecast with few values
ROC = [(0.0, 0.0), (0.02, 0.71), (0.32, 0.95), (0.65, 0.99), (1.0, 1.0)]
TARGET_TPR = 0.89


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


def trio_value(S) -> float:
    return TRIO["".join(p for p in "PCB" if p in S)]


# --------------------------------------------------------------------------------------------------------- §1
def orders_and_weights() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14.5, 4.6), gridspec_kw=dict(width_ratios=[1.35, 1]))
    ax = axes[0]
    colors = {"P": C[0], "C": C[1], "B": C[2]}
    orders = list(itertools.permutations("PCB"))
    phi = {p: 0.0 for p in "PCB"}
    for row, order in enumerate(orders):
        y = len(orders) - 1 - row
        left = TRIO[""]
        before: set[str] = set()
        for p in order:
            gain = trio_value(before | {p}) - trio_value(before)
            phi[p] += gain / len(orders)
            ax.barh(y, gain, left=left, color=colors[p], edgecolor="white", height=0.62)
            ax.text(left + gain / 2, y, f"{p} +{gain}", ha="center", va="center", fontsize=9, color="white",
                    fontweight="bold")
            left += gain
            before.add(p)
    ax.set_yticks(range(len(orders)), ["".join(o) for o in reversed(orders)])
    ax.keep_ticks = True
    ax.xaxis.set_major_formatter(FuncFormatter(french_number))
    ax.axvline(TRIO[""], color="0.3", lw=1, ls=":")
    ax.axvline(TRIO["PCB"], color="0.3", lw=1, ls=":")
    ax.text(TRIO[""] + 1, -0.85, "v(∅) = 20", fontsize=8.5, color="0.3")
    ax.text(TRIO["PCB"] - 1, -0.85, "v(N) = 108", fontsize=8.5, color="0.3", ha="right")
    ax.set(xlabel="entrées vendues, à mesure que les musiciens arrivent", ylabel="ordre d'arrivée",
           xlim=(15, 112), ylim=(-1.2, 5.6))
    ax.set_title("Six ordres : chaque ligne partage 108 − 20 = 88 entrées\n"
                 f"moyennes : piano {fr(phi['P'], 0)}, contrebasse {fr(phi['C'], 0)}, batterie {fr(phi['B'], 0)}",
                 fontsize=10.5)
    ax = axes[1]
    n = 5
    w = [Fraction(math.factorial(s) * math.factorial(n - 1 - s), math.factorial(n)) for s in range(n)]
    for s in range(n):
        k = math.comb(n - 1, s)
        for j in range(k):
            ax.bar(s, float(w[s]), bottom=j * float(w[s]), width=0.62, color=C[s % len(C)], edgecolor="white")
        ax.text(s, 0.2 + 0.006, f"{k} × {w[s].numerator}/{w[s].denominator}", ha="center", fontsize=9)
    ax.axhline(0.2, color="0.3", lw=1, ls="--")
    ax.set_xticks(range(n), [str(s) for s in range(n)])
    ax.keep_ticks = True
    ax.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax.set(xlabel="taille s de la coalition déjà arrivée (n = 5)", ylabel="part des 5! = 120 ordres", ylim=(0, 0.235))
    ax.set_title("Poids w(s) = s!(n − 1 − s)!/n! : chaque taille porte 1/5", fontsize=10.5)
    fig.tight_layout(w_pad=2.5)
    save(fig, "ordres_poids.png")
    print(f"    phi = {phi}; weights n = 5: {[str(x) for x in w]}")


# --------------------------------------------------------------------------------------------------------- §3
def marginal_conditional() -> None:
    rng = np.random.default_rng(7891)
    (m1, s1), (m2, s2) = WIND, SWELL
    cov = [[s1**2, RHO * s1 * s2], [RHO * s1 * s2, s2**2]]
    pts = rng.multivariate_normal([m1, m2], cov, size=400)
    f = lambda a, b: 100 + 0.5 * a**2 + 20 * b  # noqa: E731
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 4.6))
    ax = axes[0]
    ax.scatter(pts[:, 1], f(pts[:, 0], pts[:, 1]), s=8, color="0.7", alpha=0.6, label="400 traversées simulées")
    v = np.linspace(0.0, 3.0, 200)
    pd_ = 100 + 0.5 * (m1**2 + s1**2) + 20 * v
    mc = m1 + RHO * s1 / s2 * (v - m2)
    cond = 100 + 0.5 * (mc**2 + s1**2 * (1 - RHO**2)) + 20 * v
    ax.plot(v, pd_, color=C[0], lw=2.2, label="moyenne marginale 136,5 + 20v")
    ax.plot(v, cond, color=C[1], lw=2.2, label="moyenne conditionnelle E[f(X) | X₂ = v]")
    for vv in (0.5, 2.5):
        ax.plot([vv, vv], [100 + 0.5 * 73 + 20 * vv,
                           100 + 0.5 * ((m1 + RHO * s1 / s2 * (vv - m2)) ** 2 + 3.24) + 20 * vv], "k:", lw=1)
    ax.annotate("v = 2,5 : 186,5 contre 233,54", (2.5, 233.54), textcoords="offset points", xytext=(-150, 6),
                fontsize=9, arrowprops=dict(arrowstyle="->", color="0.3"))
    ax.set(xlabel="houle v (m)", ylabel="gazole (L/h)", ylim=(80, 320))
    ax.set_title("Ferry : fixer la houle, avec ou sans le vent qui l'accompagne (ρ = 0,8)", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="upper left")
    ax = axes[1]
    x1 = np.linspace(-45, 45, 181)
    for u, col in zip(SUN, (C[2], C[3], C[4])):
        ax.plot(x1, np.cos(np.radians(x1 - u)), color=col, lw=1.6, label=f"courbe ICE, soleil à {french_number(u)}°")
        ax.plot([u], [1.0], "o", color=col, ms=5)
    mean_coef = (1 + math.sqrt(2)) / 3
    ax.plot(x1, mean_coef * np.cos(np.radians(x1)), color="black", lw=2.6,
            label="leur moyenne ((1 + √2)/3) cos x₁")
    ax.set(xlabel="orientation x₁ du panneau (degrés)", ylabel="puissance relative cos(x₁ − u)", ylim=(-0.05, 1.12))
    ax.set_xticks([-45, -30, -15, 0, 15, 30, 45])
    ax.set_title("Panneau solaire : des courbes ICE décalées, une moyenne qui les écrase", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="lower center")
    fig.tight_layout(w_pad=2.5)
    save(fig, "marginale_ice.png")


# --------------------------------------------------------------------------------------------------------- §4
def fields() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.2))
    ax = axes[0]
    xs, ys = np.meshgrid(np.linspace(2.6, 4.4, 200), np.linspace(0.6, 2.4, 200))
    cs = ax.contour(xs, ys, xs**2 * ys, levels=[6, 9, 12, 16, 20, 25, 32, 40], colors="0.6", linewidths=0.9)
    ax.clabel(cs, fmt=lambda z: french_number(z), fontsize=8)
    qx, qy = np.meshgrid(np.linspace(2.7, 4.3, 7), np.linspace(0.7, 2.3, 7))
    gx, gy = 2 * qx * qy, qx**2
    norm_ = np.hypot(gx, gy)
    ax.quiver(qx, qy, gx / norm_, gy / norm_, color=C[6], alpha=0.5, scale=22, width=0.004)
    (r1, r2), (x1, x2) = BOX_R, BOX_X
    ax.plot([r1, x1], [r2, x2], color=C[0], lw=2.4, label="segment")
    ax.plot([r1, x1, x1], [r2, r2, x2], color=C[1], lw=2.2, ls="--", label="côté d'abord")
    ax.plot([r1, r1, x1], [r2, x2, x2], color=C[2], lw=2.2, ls="-.", label="hauteur d'abord")
    ax.plot([r1], [r2], "ko", ms=6)
    ax.plot([x1], [x2], "ks", ms=6)
    ax.text(r1 - 0.05, r2 - 0.12, "r = (3, 1) : 9 L", ha="right", fontsize=9)
    ax.text(x1 + 0.05, x2 + 0.07, "x = (4, 2) : 32 L", fontsize=9)
    ax.set(xlabel="côté x₁ (dm)", ylabel="hauteur x₂ (dm)", aspect="equal", xlim=(2.6, 4.4), ylim=(0.6, 2.4))
    ax.set_title("∇f, f = x₁²x₂ : chaque chemin donne 32 − 9 = 23", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="lower right", framealpha=0.95)
    ax = axes[1]
    qx, qy = np.meshgrid(np.linspace(-0.2, 2.2, 9), np.linspace(0.7, 2.3, 7))
    fx, fy = qx * qy, qy**2
    norm_ = np.hypot(fx, fy)
    ax.quiver(qx, qy, fx / norm_, fy / norm_, color=C[6], alpha=0.5, scale=22, width=0.004)
    (a1, a2), (b1, b2) = FIELD_A, FIELD_B
    ax.plot([a1, b1], [a2, b2], color=C[0], lw=2.4, label="segment : 17/3")
    ax.plot([a1, b1, b1], [a2, a2, b2], color=C[1], lw=2.2, ls="--", label="x₁ d'abord : 13/3")
    ax.plot([a1, a1, b1], [a2, b2, b2], color=C[2], lw=2.2, ls="-.", label="x₂ d'abord : 19/3")
    ax.plot([a1], [a2], "ko", ms=6)
    ax.plot([b1], [b2], "ks", ms=6)
    ax.set(xlabel="x₁", ylabel="x₂", aspect="equal", xlim=(-0.3, 2.3), ylim=(0.6, 2.4))
    ax.set_title("F = (x₁x₂, x₂²), dérivées croisées x₁ et 0 :\ntrois chemins, trois valeurs", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="upper left")
    fig.tight_layout(w_pad=2.5)
    save(fig, "champs.png")


def shares() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 4.6))
    ax = axes[0]
    rows = [("segment", 32 / 3, 37 / 3), ("côté d'abord", 7, 16), ("hauteur d'abord", 14, 9),
            ("moyenne des deux\n(Shapley)", 10.5, 12.5)]
    for i, (name, a, b) in enumerate(rows):
        ax.barh(i, a, color=C[0], edgecolor="white", height=0.6)
        ax.barh(i, b, left=a, color=C[1], edgecolor="white", height=0.6)
        ax.text(a / 2, i, fr(a, 2).rstrip("0").rstrip(","), ha="center", va="center", color="white",
                fontweight="bold", fontsize=9.5)
        ax.text(a + b / 2, i, fr(b, 2).rstrip("0").rstrip(","), ha="center", va="center", color="white",
                fontweight="bold", fontsize=9.5)
    ax.set_yticks(range(len(rows)), [r[0] for r in rows])
    ax.keep_ticks = True
    ax.xaxis.set_major_formatter(FuncFormatter(french_number))
    ax.invert_yaxis()
    handles = [Patch(color=C[0], label="part du côté"), Patch(color=C[1], label="part de la hauteur")]
    ax.set(xlabel="litres (la variation vaut 23)", xlim=(0, 23.8), ylim=(3.5, -0.9))
    ax.set_title("Boîte de (3, 1) à (4, 2) : deux partages de 23", fontsize=10.5)
    ax.legend(handles=handles, fontsize=8.5, loc="upper center", ncol=2)
    ax = axes[1]
    sc = SCALE
    t = np.linspace(0, 1, 401)
    for (r_d, r_n), col, ls in (((0.0, 0.0), C[0], "-"), (sc["r2"], C[1], "--")):
        d = r_d + t * (sc["x"][0] - r_d)
        nn = r_n + t * (sc["x"][1] - r_n)
        g = np.minimum(sc["per_km"] * d + sc["per_night"] * nn, sc["cap"])
        ax.plot(t, g, color=col, lw=2.2, ls=ls, label=f"depuis r = ({french_number(r_d)} km, {french_number(r_n)} nuits)")
        tstar = (sc["cap"] - sc["per_km"] * r_d - sc["per_night"] * r_n) / (
            sc["per_km"] * (sc["x"][0] - r_d) + sc["per_night"] * (sc["x"][1] - r_n))
        ax.axvline(tstar, color=col, lw=0.9, ls=":")
        ax.text(tstar, 8 if ls == "-" else 15, f" plafond atteint\n en t = {fr(tstar, 3)}", fontsize=8.5, color=col)
    ax.axhline(sc["cap"], color="0.3", lw=1, ls=":")
    ax.text(0.36, 2, "parts le long du segment :\ndepuis 0 : 42,35 € (km) et 17,65 € (nuits)\n"
            "depuis (80, 2) : 18,35 € et 7,65 €", fontsize=8.5, color="0.2",
            bbox=dict(boxstyle="round", fc="white", ec="0.8"))
    ax.set(xlabel="t, le long du segment de r à x = (160 km, 4 nuits)", ylabel="remboursement (€)", ylim=(0, 66))
    ax.set_title("Barème plafonné : dérivée nulle en x, parts non nulles", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="center right")
    fig.tight_layout(w_pad=2.5)
    save(fig, "partages.png")


# --------------------------------------------------------------------------------------------------------- §5
def interpolation() -> None:
    h, H = len(PROFILE), 9
    centers = np.array([(u + 0.5) * h / H - 0.5 for u in range(H)])
    corners = np.array([u * (h - 1) / (H - 1) for u in range(H)])
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 4.3))
    ax = axes[0]
    for k in range(h + 1):
        ax.axvline(k - 0.5, color="0.75", lw=1)
    ax.plot(range(h), [1.0] * h, "ks", ms=8)
    ax.text(-0.45, 1.13, "centres des 3 cases d'origine", fontsize=8.5)
    ax.plot(centers, [0.55] * H, "o", color=C[0], ms=7)
    ax.plot(corners, [0.15] * H, "^", color=C[1], ms=7)
    for u in range(H):
        ax.text(centers[u], 0.67, str(u), ha="center", fontsize=8, color=C[0])
        ax.text(corners[u], 0.27, str(u), ha="center", fontsize=8, color=C[1])
    ax.text(2.55, 0.55, "centres alignés\n(u + ½)·3/9 − ½", va="center", fontsize=8.5, color=C[0])
    ax.text(2.55, 0.15, "coins alignés\nu·2/8", va="center", fontsize=8.5, color=C[1])
    ax.annotate("", (centers[0], 0.42), (corners[0], 0.42), arrowprops=dict(arrowstyle="<->", color="0.3"))
    ax.text(-0.17, 0.36, "1/3", fontsize=8.5, ha="center")
    ax.set(xlim=(-0.6, 3.4), ylim=(0, 1.3), xlabel="coordonnée dans la grille d'origine (en pas)")
    ax.set_yticks([])
    ax.set_title("Où tombent les 9 cases d'arrivée u = 0, …, 8", fontsize=10.5)
    ax = axes[1]
    clamp = lambda c: np.clip(c, 0, h - 1)  # noqa: E731
    u = np.arange(H)
    vc = np.interp(clamp(centers), np.arange(h), PROFILE)
    vk = np.interp(corners, np.arange(h), PROFILE)
    ax.plot(u, vc, "o-", color=C[0], ms=7, lw=1.2, label="centres alignés (coordonnées bornées à [0, 2])")
    ax.plot(u, vk, "^--", color=C[1], ms=7, lw=1.2, label="coins alignés")
    for k in range(H):
        if abs(vc[k] - vk[k]) > 1e-9:
            ax.annotate("", (k, vk[k]), (k, vc[k]), arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
    ax.set_xticks(u)
    ax.set(xlabel="case d'arrivée u", ylabel="profondeur (m)", ylim=(3.5, 7.5))
    ax.set_title("Le profil (4, 7, 5) agrandi en 9 valeurs", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="lower center")
    fig.tight_layout(w_pad=2.5)
    save(fig, "interpolation.png")
    print(f"    centers {np.round(centers, 3)}; corners {np.round(corners, 3)}")


# --------------------------------------------------------------------------------------------------------- §6
def ranks() -> None:
    rng = np.random.default_rng(7895)
    routes = list(TOPO1)
    r1 = rankdata([GRADES.index(TOPO1[k]) for k in routes])
    r2 = rankdata([GRADES.index(TOPO2[k]) for k in routes])
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.8))
    ax = axes[0]
    ax.plot([0.5, 8.5], [0.5, 8.5], color="0.6", lw=1, ls="--")
    ax.plot(r1, r2, "o", color=C[0], ms=8)
    for k, a, b in zip(routes, r1, r2):
        ax.text(a + 0.15, b - 0.32, f"{k} ({TOPO1[k]} ; {TOPO2[k]})", fontsize=8)
    rho = spearmanr(r1, r2).statistic
    ax.set(xlabel="rang dans le topo 1", ylabel="rang dans le topo 2", xlim=(0.5, 9.3), ylim=(0.5, 8.6),
           aspect="equal")
    ax.set_xticks(range(1, 9))
    ax.set_title(f"Huit voies, deux topos : ρ_S ≈ {fr(rho, 3)}\nC et D ex aequo dans le topo 2 (rang 5,5)", fontsize=10.5)
    ax = axes[1]
    x = rng.uniform(0, 3, 40)
    y = np.exp(1.3 * x) * np.exp(0.35 * rng.standard_normal(40))
    pr, sr = pearsonr(x, y).statistic, spearmanr(x, y).statistic
    ax.plot(x, y, "o", color=C[1], ms=6, alpha=0.8)
    ax.set(xlabel="x", ylabel="y")
    ax.set_title(f"Une relation croissante mais pas affine :\nPearson ≈ {fr(pr, 2)}, Spearman ≈ {fr(sr, 2)}",
                 fontsize=10.5)
    inset = ax.inset_axes([0.08, 0.5, 0.36, 0.42])
    inset.plot(rankdata(x), rankdata(y), "o", color=C[1], ms=3)
    inset.set_title("les mêmes points en rangs", fontsize=8)
    inset.tick_params(labelsize=7)
    fig.tight_layout(w_pad=2.5)
    save(fig, "spearman.png")
    print(f"    rho_S topos = {rho:.4f}; random relation Pearson {pr:.3f}, Spearman {sr:.3f}")


# --------------------------------------------------------------------------------------------------------- §8
def roc_chord() -> None:
    fig, ax = plt.subplots(figsize=(6.6, 5.2))
    fx, ty = zip(*ROC)
    ax.plot(fx, ty, color="0.6", lw=1, ls="--", label="cordes entre seuils voisins")
    ax.plot(fx[1:-1], ty[1:-1], "o", color=C[0], ms=8, label="les seuils de la prévision")
    (fa, ta), (fb, tb) = ROC[1], ROC[2]
    q = (tb - TARGET_TPR) / (tb - ta)
    fq = q * fa + (1 - q) * fb
    ax.plot([fa, fb], [ta, tb], color=C[1], lw=2.4)
    ax.plot([fq], [TARGET_TPR], "*", color=C[1], ms=15, label=f"tirage : A avec 0,25, B avec 0,75")
    ax.annotate(f"A = (0,02 ; 0,71)", (fa, ta), textcoords="offset points", xytext=(10, -14), fontsize=9)
    ax.annotate(f"B = (0,32 ; 0,95)", (fb, tb), textcoords="offset points", xytext=(6, 8), fontsize=9)
    ax.annotate(f"({fr(fq, 3)} ; {fr(TARGET_TPR, 2)})", (fq, TARGET_TPR), textcoords="offset points",
                xytext=(14, -22), fontsize=9, color=C[1])
    ax.plot([0, 1], [0, 1], color="0.8", lw=0.8)
    ax.set(xlabel="taux de fausses alertes (FPR)", ylabel="taux de détection (TPR)", xlim=(-0.02, 1.02),
           ylim=(-0.02, 1.04), aspect="equal")
    ax.set_title("Tirer au sort entre deux seuils :\nun point de la corde", fontsize=10.5)
    ax.legend(fontsize=8.5, loc="lower right")
    save(fig, "roc_corde.png")
    print(f"    q = {q:.4f}, FPR = {fq:.4f}")


def main() -> int:
    print(f"Figures MB6 → {OUT.relative_to(ROOT)}")
    wbplot.set_style()
    orders_and_weights()
    marginal_conditional()
    fields()
    shares()
    interpolation()
    ranks()
    roc_chord()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
