#!/usr/bin/env python
"""Draw the figures of chapter MB3 (used by Claude).

    python tools/chapters/figures_mb3.py

Writes small PNG files into chapitres/mb3_rotations_attention/figures/:
- §1: the unit vectors of angles a and b (cos a = 35/37, cos b = 28/53) and the cosine of their difference, and the
  product of two cosines written as half the sum of two cosines (beats of cos 7t and cos 6t);
- §2: a flag turned by R_a then R_b, by R_b then R_a, and by R_{a+b}; a rotation and a reflection of the same flag;
- §3: the matrices of a Givens rotation of ℝ⁵ (plane (2, 5), cos θ = 35/37), of a block-diagonal rotation, and of Pᵀ R₁₂ P = R₂₃ in ℝ³; two
  quarter turns of space applied to e₁ in both orders;
- §4: the twelve months on a circle (December and January close, June opposite), four breakdowns and their mean
  vector; the dot product of two encodings of a clock with two hands as a function of the gap;
- §5: Nadaraya-Watson on the autonomy of an electric bike against the outside temperature (five points), for three
  bandwidths, and the weights of the five points at 7 °C as functions of h;
- §6: a law on four car parks, masked before the softmax or zeroed after it; the cells of a triangular mask (7 days);
- §7: the weights of four scores (3, 2, 2, 0) multiplied by c, and 1 − p_max, 1 − Σp² against the bound 3e^{−c};
- §8: the state (m, l, a) of seven reviews read by pages of three (one flagged review, score −∞; scores
  (2, 0, 1, 1, −∞, 2, 3), ratings (7, 4, 8, 9, 2, 6, 5));
- §9: the memory of an n × n matrix of float64 against blocks of 500 rows, in log-log scales.
The numbers are those of the fiche; none comes from workbookIA B1, B2 or B3, nor from the exercises of MB3. No figure
draws random numbers: the seeds 7291 to 7299 kept for the figures of MB3 are not used.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Arc, FancyArrowPatch, Polygon, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "mb3_rotations_attention" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

# §1 and §2: two points of the unit circle with rational coordinates
COS_A, SIN_A = 35 / 37, 12 / 37
COS_B, SIN_B = 28 / 53, 45 / 53
ANG_A, ANG_B = math.atan2(12, 35), math.atan2(45, 28)
FLAG = np.array([[1.0, 0.0], [2.2, 0.0], [2.2, 0.35], [1.7, 0.35], [1.7, 0.7], [1.0, 0.7]])   # an asymmetric flag
# §4: months, four breakdowns (October, November, January, February), a clock with two hands
BREAKDOWNS = [10, 11, 1, 2]
# §5: autonomy of an electric bike (km) against the outside temperature (°C)
X_BIKE = np.array([-6.0, -1.0, 4.0, 13.0, 25.0])
Y_BIKE = np.array([28.0, 40.0, 49.0, 57.0, 61.0])
X_QUERY, H_TEXT = 7.0, 3.0
# §6: exponentials of the scores of four car parks
PARK = np.array([6.0, 3.0, 2.0, 1.0])
# §7: four scores, gap Δ = 1 between the largest and the next
S4 = np.array([3.0, 2.0, 2.0, 0.0])
# §8: seven reviews (reliability score, rating out of 10), read by blocks of three
S_ON = [2.0, 0.0, 1.0, 1.0, -math.inf, 2.0, 3.0]
V_ON = [7.0, 4.0, 8.0, 9.0, 2.0, 6.0, 5.0]
# §9: n clients, blocks of B rows, float64
N_EX, B_EX = 30_000, 500


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
            keep = getattr(ax, "keep_ticks", False)
            if axis.get_scale() == "linear" and ax.axison and not keep:
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def rot(theta: float) -> np.ndarray:
    return np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])


def givens(n: int, i: int, j: int, theta: float) -> np.ndarray:
    """MML (3.80)–(3.81), coordinates numbered from 1 as in the fiche."""
    G = np.eye(n)
    G[i - 1, i - 1] = G[j - 1, j - 1] = math.cos(theta)
    G[i - 1, j - 1], G[j - 1, i - 1] = -math.sin(theta), math.sin(theta)
    return G


def softmax(s: np.ndarray) -> np.ndarray:
    s = np.asarray(s, dtype=float)
    w = np.exp(s - s.max())
    return w / w.sum()


def arrow(ax, start, end, color, lw=2.0, ms=14, **kw):
    ax.add_patch(FancyArrowPatch(tuple(start), tuple(end), arrowstyle="-|>", mutation_scale=ms, lw=lw, color=color,
                                 **kw))


def unit_circle(ax, color="0.6"):
    t = np.linspace(0, 2 * math.pi, 400)
    ax.plot(np.cos(t), np.sin(t), color=color, lw=1)
    ax.axhline(0, color="0.75", lw=0.8)
    ax.axvline(0, color="0.75", lw=0.8)


# --------------------------------------------------------------------------------------------------------- §1
def addition() -> None:
    """§1: the dot product of two unit vectors is the cosine of their angle; a product of cosines as a half sum."""
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 4.9), gridspec_kw={"width_ratios": [1, 1.35]})
    ax = axes[0]
    unit_circle(ax)
    ua, ub = np.array([COS_A, SIN_A]), np.array([COS_B, SIN_B])
    arrow(ax, (0, 0), ua, C[0])
    arrow(ax, (0, 0), ub, C[1])
    ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=0, theta2=math.degrees(ANG_A), color=C[0], lw=1.4))
    ax.add_patch(Arc((0, 0), 0.78, 0.78, theta1=math.degrees(ANG_A), theta2=math.degrees(ANG_B), color="0.25", lw=1.4))
    ax.text(0.3, 0.035, "a", color=C[0], fontsize=12)
    ax.text(0.27, 0.36, "b − a", color="0.25", fontsize=11)
    ax.annotate(r"$\mathbf{u}_a = (35/37,\ 12/37)$", ua, textcoords="offset points", xytext=(6, -16), fontsize=10,
                color=C[0])
    ax.annotate(r"$\mathbf{u}_b = (28/53,\ 45/53)$", ub, textcoords="offset points", xytext=(6, 4), fontsize=10,
                color=C[1])
    ax.plot([COS_A, COS_A], [0, SIN_A], color=C[0], ls=":", lw=1)
    ax.plot([COS_B, COS_B], [0, SIN_B], color=C[1], ls=":", lw=1)
    ax.text(-1.15, -1.32, r"$\mathbf{u}_a\cdot\mathbf{u}_b = \cos a\cos b + \sin a\sin b = 1520/1961 = \cos(b - a)$",
            fontsize=10)
    ax.set(xlim=(-1.2, 1.35), ylim=(-1.4, 1.2), aspect="equal", xlabel="cosinus", ylabel="sinus",
           title="Deux points du cercle unité")
    ax = axes[1]
    t = np.linspace(0, 2 * math.pi, 2000)
    ax.plot(t, np.cos(7 * t) * np.cos(6 * t), color=C[0], lw=1.2, label=r"$\cos 7t\,\cos 6t$")
    ax.plot(t, 0.5 * np.cos(t), color=C[1], lw=1.6, ls="--", label=r"$\frac{1}{2}\cos t$ (la différence)")
    ax.plot(t, 0.5 * np.cos(t) + 0.5, color="0.55", lw=1, ls=":")
    ax.plot(t, 0.5 * np.cos(t) - 0.5, color="0.55", lw=1, ls=":", label=r"$\frac{1}{2}\cos t \pm \frac{1}{2}$ (enveloppe)")
    ax.set(xlabel="t (radians)", ylabel="valeur", xlim=(0, 2 * math.pi), ylim=(-1.15, 1.25),
           title=r"$\cos 7t\cos 6t = \frac{1}{2}[\cos t + \cos 13t]$ : une onde lente et une rapide")
    ax.legend(fontsize=9, loc="upper right", ncol=1)
    fig.tight_layout(w_pad=3)
    save(fig, "addition.png")
    print(f"    a = {math.degrees(ANG_A):.2f}°, b = {math.degrees(ANG_B):.2f}°, b − a = {math.degrees(ANG_B - ANG_A):.2f}°, "
          f"u_a·u_b = {COS_A * COS_B + SIN_A * SIN_B:.4f} = 1520/1961 = {1520 / 1961:.4f}")


# --------------------------------------------------------------------------------------------------------- §2
def plane_rotations() -> None:
    """§2: R_a R_b = R_b R_a = R_{a+b} on a flag; a rotation keeps the orientation, a reflection reverses it."""
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.6))
    ax = axes[0]
    unit_circle(ax, color="0.85")
    ra, rb = rot(ANG_A), rot(ANG_B)
    shapes = [(FLAG, "0.55", "drapeau de départ"), (FLAG @ ra.T, C[0], r"$\mathbf{R}_a$"),
              (FLAG @ rb.T, C[2], r"$\mathbf{R}_b$"), (FLAG @ (rb @ ra).T, C[1], r"$\mathbf{R}_b\mathbf{R}_a$"),
              (FLAG @ (ra @ rb).T, "black", r"$\mathbf{R}_a\mathbf{R}_b = \mathbf{R}_{a+b}$")]
    assert np.allclose(ra @ rb, rb @ ra) and np.allclose(ra @ rb, rot(ANG_A + ANG_B))
    for k, (shape, col, lab) in enumerate(shapes):
        ls = "--" if k == 3 else "-"
        ax.add_patch(Polygon(shape, closed=True, fill=k == 0, fc="0.9", ec=col, lw=2.6 if k == 3 else 1.6, ls=ls,
                             label=lab, zorder=3 + (k == 4)))
    for theta, r, col in ((ANG_A, 1.15, C[0]), (ANG_A + ANG_B, 2.45, "black")):
        ax.add_patch(Arc((0, 0), 2 * r, 2 * r, theta1=0, theta2=math.degrees(theta), color=col, lw=1, ls=":"))
    ax.set(xlim=(-1.4, 2.6), ylim=(-0.5, 2.7), aspect="equal", xlabel="x", ylabel="y",
           title="Deux rotations s'enchaînent en une seule, dans n'importe quel ordre")
    ax.legend(fontsize=9, loc="upper left")
    ax = axes[1]
    S = np.array([[COS_A, SIN_A], [SIN_A, -COS_A]])
    half = ANG_A / 2
    flag2 = FLAG + np.array([0.0, 1.0])
    ax.add_patch(Polygon(flag2, closed=True, fc="0.9", ec="0.55", lw=1.6, label="drapeau de départ"))
    ax.add_patch(Polygon(flag2 @ rot(1.9).T, closed=True, fill=False, ec=C[0], lw=1.8,
                         label="une rotation (dét. 1) : même sens de lecture"))
    ax.add_patch(Polygon(flag2 @ S.T, closed=True, fill=False, ec=C[1], lw=1.8, ls="--",
                         label="la symétrie de matrice ((35, 12), (12, −35))/37 (dét. −1)"))
    tt = np.linspace(-2.6, 2.6, 2)
    ax.plot(tt * math.cos(half), tt * math.sin(half), color=C[1], lw=1, ls=":")
    ax.text(-2.4, -2.4 * math.tan(half) - 0.32, f"axe de la symétrie, à a/2 ≈ {fr(math.degrees(half), 2)}°",
            fontsize=9, color=C[1])
    ax.axhline(0, color="0.75", lw=0.8)
    ax.axvline(0, color="0.75", lw=0.8)
    ax.set(xlim=(-2.5, 2.6), ylim=(-2.0, 2.9), aspect="equal", xlabel="x", ylabel="y",
           title="Rotation ou symétrie : le signe du déterminant")
    ax.legend(fontsize=8.5, loc="upper left")
    fig.tight_layout(w_pad=2.5)
    save(fig, "rotation_plan.png")
    print(f"    a + b = {math.degrees(ANG_A + ANG_B):.2f}°; reflection axis {math.degrees(half):.2f}°")


# --------------------------------------------------------------------------------------------------------- §3
def givens_matrices() -> None:
    """§3: a Givens rotation of ℝ⁵, a block-diagonal rotation of ℝ⁵, and Pᵀ R₁₂ P = R₂₃ in ℝ³."""
    th = ANG_A
    G = givens(5, 2, 5, th)
    Bd = givens(5, 1, 2, 0.6) @ givens(5, 3, 4, 1.3)
    P = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=float)
    conj = P.T @ givens(3, 1, 2, th) @ P
    assert np.allclose(conj, givens(3, 2, 3, th))
    mats = [(G, r"$\mathbf{R}_{25}(\theta)$ dans $\mathbb{R}^5$ : un seul plan tourne"),
            (Bd, r"$\mathbf{R}_{12}(\alpha)\,\mathbf{R}_{34}(\beta)$ : deux blocs $2\times2$ et un 1"),
            (conj, r"$\mathbf{P}^\top\mathbf{R}_{12}(\theta)\,\mathbf{P} = \mathbf{R}_{23}(\theta)$ dans $\mathbb{R}^3$")]
    fig, axes = plt.subplots(1, 3, figsize=(14.2, 4.7), gridspec_kw={"width_ratios": [5, 5, 3.4]})
    for ax, (M, title) in zip(axes, mats):
        n = M.shape[0]
        ax.imshow(M, cmap=wbplot.diverging_cmap(), vmin=-1, vmax=1)
        for i in range(n):
            for j in range(n):
                v = M[i, j]
                if abs(v) < 1e-12:
                    txt = "0"
                elif abs(v - 1) < 1e-12:
                    txt = "1"
                else:
                    txt = fr(v, 2)
                ax.text(j, i, txt, ha="center", va="center", fontsize=9.5,
                        color="white" if abs(v) > 0.75 and txt not in ("0", "1") else "black")
        ax.set_xticks(range(n), [str(k + 1) for k in range(n)])
        ax.set_yticks(range(n), [str(k + 1) for k in range(n)])
        ax.keep_ticks = True
        ax.grid(False)
        ax.set_title(title, fontsize=10.5)
    fig.tight_layout(w_pad=2)
    save(fig, "givens.png")
    print(f"    θ = a: cos {math.cos(th):.4f}, sin {math.sin(th):.4f}; block angles 0.6 and 1.3 rad")


def rotation_order() -> None:
    """§3: two quarter turns of space applied to e₁ in both orders end at e₃ or at e₂."""
    R12, R23 = givens(3, 1, 2, math.pi / 2), givens(3, 2, 3, math.pi / 2)
    e1 = np.array([1.0, 0, 0])
    paths = [(r"d'abord $\mathbf{R}_{12}$, puis $\mathbf{R}_{23}$ : $\mathbf{e}_1 \to \mathbf{e}_2 \to \mathbf{e}_3$",
              [e1, R12 @ e1, R23 @ R12 @ e1], (R12, R23)),
             (r"d'abord $\mathbf{R}_{23}$, puis $\mathbf{R}_{12}$ : $\mathbf{e}_1 \to \mathbf{e}_1 \to \mathbf{e}_2$",
              [e1, R23 @ e1, R12 @ R23 @ e1], (R23, R12))]
    fig = plt.figure(figsize=(12.0, 5.2))
    for k, (title, pts, (first, second)) in enumerate(paths):
        ax = fig.add_subplot(1, 2, k + 1, projection="3d")
        for v, lab in zip(np.eye(3), (r"$\mathbf{e}_1$", r"$\mathbf{e}_2$", r"$\mathbf{e}_3$")):
            ax.plot([0, 1.25 * v[0]], [0, 1.25 * v[1]], [0, 1.25 * v[2]], color="0.6", lw=1)
            ax.text(*(1.35 * v), lab, fontsize=12)
        for step, (p0, p1, col) in enumerate(((pts[0], pts[1], C[0]), (pts[1], pts[2], C[1]))):
            M = first if step == 0 else second
            if np.allclose(p0, p1):
                ax.scatter(*p0, color=col, s=60)
                continue
            ts = np.linspace(0, 1, 30)
            arc = np.array([np.cos(t * math.pi / 2) * p0 + np.sin(t * math.pi / 2) * (M @ p0) for t in ts])
            ax.plot(arc[:, 0], arc[:, 1], arc[:, 2], color=col, lw=2.4)
        ax.quiver(0, 0, 0, *pts[-1], color="black", lw=2.2, arrow_length_ratio=0.12)
        ax.set(xlim=(0, 1.3), ylim=(0, 1.3), zlim=(0, 1.3), xticks=[], yticks=[], zticks=[])
        ax.view_init(elev=22, azim=35)
        ax.set_title(title, fontsize=10.5)
    fig.suptitle("Deux quarts de tour de l'espace qui ne commutent pas", fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    save(fig, "ordre_rotations.png")
    print(f"    R23 R12 e1 = {np.round(R23 @ R12 @ e1, 6).tolist()}, R12 R23 e1 = {np.round(R12 @ R23 @ e1, 6).tolist()}")


# --------------------------------------------------------------------------------------------------------- §4
def clocks() -> None:
    """§4: the months on a circle and the mean of four breakdowns; the dot product of a two-hand clock encoding."""
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.2), gridspec_kw={"width_ratios": [1, 1.45]})
    ax = axes[0]
    unit_circle(ax, color="0.7")
    w = 2 * math.pi / 12
    names = ["déc.", "janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov."]
    for m in range(12):
        p = np.array([math.cos(w * m), math.sin(w * m)])
        hit = (m % 12) in [b % 12 for b in BREAKDOWNS]
        ax.plot(*p, "o", color=C[1] if hit else "0.45", ms=8 if hit else 5, zorder=3)
        ax.annotate(names[m], p, textcoords="offset points", xytext=(14 * p[0] - 8, 12 * p[1] - 4), fontsize=9)
    dec, jan, jun = (np.array([math.cos(w * m), math.sin(w * m)]) for m in (0, 1, 6))
    ax.plot([dec[0], jan[0]], [dec[1], jan[1]], color=C[0], lw=2)
    ax.plot([dec[0], jun[0]], [dec[1], jun[1]], color=C[2], lw=1.2, ls="--")
    ax.text(0.62, 0.2, "0,52", color=C[0], fontsize=9.5)
    ax.text(-0.35, 0.06, "2", color=C[2], fontsize=9.5)
    mean = np.mean([[math.cos(w * b), math.sin(w * b)] for b in BREAKDOWNS], axis=0)
    arrow(ax, (0, 0), mean, "black", lw=2.2)
    ax.annotate("moyenne des 4 pannes\n(longueur ≈ 0,683)", mean, textcoords="offset points", xytext=(-40, -38),
                fontsize=9)
    ax.set(xlim=(-1.45, 1.45), ylim=(-1.4, 1.4), aspect="equal", xticks=[], yticks=[],
           title="Les mois sur un cercle (ω = 2π/12)")
    ax = axes[1]
    gap = np.linspace(0, 24 * 60, 2000)
    wm, wh = 2 * math.pi / 60, 2 * math.pi / 720
    ax.plot(gap / 60, np.cos(wm * gap) + np.cos(wh * gap), color=C[0], lw=1.3, label="deux aiguilles : cos ω₁δ + cos ω₂δ")
    ax.plot(gap / 60, np.cos(wh * gap), color=C[1], lw=2, ls="--", label="aiguille des heures seule : cos ω₂δ")
    hours = np.arange(0, 25)
    ax.plot(hours, 1 + np.cos(wh * hours * 60), "o", color=C[2], ms=4,
            label="écarts d'un nombre entier d'heures : 1 + cos ω₂δ")
    ax.axhline(0, color="0.7", lw=0.8)
    ax.set(xlabel="écart δ (heures)", ylabel="produit scalaire des deux encodages", xlim=(0, 24), ylim=(-2.15, 2.4),
           xticks=range(0, 25, 3), title="Une horloge à deux aiguilles : le produit scalaire ne dépend que de l'écart")
    ax.legend(fontsize=8.5, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2)
    fig.tight_layout(w_pad=2.5)
    save(fig, "horloges.png")
    print(f"    mean of the breakdowns {np.round(mean, 4).tolist()}, ‖dec − jan‖ = {np.linalg.norm(dec - jan):.4f}")


# --------------------------------------------------------------------------------------------------------- §5
def kernel() -> None:
    """§5: Nadaraya-Watson for three bandwidths, and the weights of the five points at 7 °C as functions of h."""
    xs = np.linspace(-10, 30, 801)

    def nw(x, h):
        return softmax(-(x - X_BIKE) ** 2 / (2 * h * h)) @ Y_BIKE

    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.8))
    ax = axes[0]
    nearest = Y_BIKE[np.argmin(np.abs(xs[:, None] - X_BIKE[None]), axis=1)]
    ax.plot(xs, nearest, color="0.6", lw=1, ls=":", label="h → 0 : le plus proche voisin")
    ax.axhline(Y_BIKE.mean(), color="0.6", lw=1, ls="--", label="h → ∞ : la moyenne (47 km)")
    for h, col in ((1.0, C[2]), (3.0, C[0]), (10.0, C[1])):
        ax.plot(xs, [nw(x, h) for x in xs], color=col, lw=1.8, label=f"h = {h:g} °C")
    ax.plot(X_BIKE, Y_BIKE, "o", color="black", ms=7, zorder=4, label="les cinq trajets")
    ax.plot(X_QUERY, nw(X_QUERY, H_TEXT), "s", color=C[0], ms=8, zorder=5)
    ax.annotate(f"ŷ(7) ≈ {fr(nw(X_QUERY, H_TEXT), 2)} km", (X_QUERY, nw(X_QUERY, H_TEXT)), textcoords="offset points",
                xytext=(-38, 14), fontsize=9.5, color=C[0])
    ax.set(xlabel="température extérieure (°C)", ylabel="autonomie (km)", xlim=(-10, 30), ylim=(24, 66),
           title="Nadaraya-Watson pour trois largeurs de bande")
    ax.legend(fontsize=8.5, loc="lower right")
    ax = axes[1]
    hs = np.logspace(-0.3, 2, 300)
    W = np.array([softmax(-(X_QUERY - X_BIKE) ** 2 / (2 * h * h)) for h in hs])
    for k in range(5):
        ax.semilogx(hs, W[:, k], color=C[k % len(C)], lw=1.8, label=f"trajet à {fr(X_BIKE[k], 0)} °C")
    ax.axhline(0.2, color="0.6", lw=0.8, ls="--")
    ax.text(60, 0.23, "1/5", fontsize=9.5, color="0.4")
    ax.axvline(H_TEXT, color="0.5", lw=0.8, ls=":")
    ax.set(xlabel="largeur de bande h (°C, échelle logarithmique)", ylabel="poids à 7 °C", ylim=(-0.03, 1.03),
           title="Les poids à 7 °C : du plus proche voisin à la moyenne")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _p: french_number(v)))
    ax.legend(fontsize=8.5, loc="center right")
    fig.tight_layout(w_pad=2.5)
    save(fig, "noyau.png")
    print(f"    ŷ(7) for h = 1, 3, 10: {[round(nw(X_QUERY, h), 4) for h in (1.0, 3.0, 10.0)]}")


# --------------------------------------------------------------------------------------------------------- §6
def masks() -> None:
    """§6: a law on four car parks, masked before the softmax or zeroed after it; a triangular mask of 7 days."""
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 4.6), gridspec_kw={"width_ratios": [1.3, 1]})
    ax = axes[0]
    p = PARK / PARK.sum()
    masked = np.where(np.arange(4) == 1, 0, PARK)
    masked = masked / masked.sum()
    zeroed = np.where(np.arange(4) == 1, 0, p)
    labels = ["P1", "P2 (complet)", "P3", "P4"]
    xk = np.arange(4)
    for off, vals, col, lab in ((-0.27, p, "0.6", "la loi des quatre parkings"),
                                (0, masked, C[0], "score −∞ avant la softmax (somme 1)"),
                                (0.27, zeroed, C[1], f"poids mis à 0 après (somme {fr(zeroed.sum(), 2)})")):
        ax.bar(xk + off, vals, width=0.26, color=col, label=lab)
    for k, txt in enumerate(["1/2", "1/4", "1/6", "1/12"]):
        ax.text(k - 0.27, p[k] + 0.012, txt, ha="center", fontsize=8.5)
    for k, txt in enumerate(["2/3", "0", "2/9", "1/9"]):
        ax.text(k, masked[k] + 0.012, txt, ha="center", fontsize=8.5, color=C[0])
    ax.set_xticks(xk, labels)
    ax.keep_ticks = True
    ax.set(ylabel="probabilité", ylim=(0, 0.78), title="Masquer avant la softmax : une loi conditionnelle")
    ax.legend(fontsize=8.5, loc="upper right")
    ax = axes[1]
    T = 7
    grid = np.tril(np.ones((T, T)))
    ax.imshow(grid, cmap=matplotlib.colors.ListedColormap(["#f0efec", C[0]]), vmin=0, vmax=1)
    for i in range(T):
        for j in range(T):
            ax.text(j, i, "" if grid[i, j] else "−∞", ha="center", va="center", fontsize=8, color="0.45")
    days = ["lun.", "mar.", "mer.", "jeu.", "ven.", "sam.", "dim."]
    ax.set_xticks(range(T), days, fontsize=8.5)
    ax.set_yticks(range(T), days, fontsize=8.5)
    ax.keep_ticks = True
    ax.grid(False)
    ax.set(xlabel="jour u regardé", ylabel="jour t qui calcule",
           title=f"Ne regarder que le passé : {int(grid.sum())} cases sur {T * T}")
    fig.tight_layout(w_pad=2.5)
    save(fig, "masques.png")
    print(f"    p {np.round(p, 4).tolist()}, masked {np.round(masked, 4).tolist()}, zeroed sum {zeroed.sum():.4f}")


# --------------------------------------------------------------------------------------------------------- §7
def saturation() -> None:
    """§7: the weights of c·(3, 2, 2, 0) against c, and the distance to the one-hot against the bound 3e^{−c}."""
    cs = np.linspace(0, 8, 401)
    P = np.array([softmax(c * S4) for c in cs])
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 4.6))
    ax = axes[0]
    ax.plot(cs, P[:, 0], color=C[0], lw=2, label="score 3 (le plus grand)")
    ax.plot(cs, P[:, 1], color=C[1], lw=2, label="chacun des deux scores 2")
    ax.plot(cs, P[:, 3], color=C[2], lw=2, label="score 0")
    ax.axhline(0.25, color="0.6", lw=0.8, ls="--")
    ax.text(7.0, 0.27, "1/4 en c = 0", fontsize=9, color="0.4")
    ax.set(xlabel="facteur c", ylabel="poids", ylim=(-0.02, 1.02), title="Multiplier les scores (3, 2, 2, 0) par c")
    ax.legend(fontsize=9, loc="center right")
    ax = axes[1]
    one_minus = 1 - P.max(axis=1)
    sens = 1 - np.sum(P ** 2, axis=1)
    bound = 3 * np.exp(-cs)
    assert np.all(one_minus <= bound + 1e-15) and np.all(sens <= 2 * one_minus + 1e-15)
    ax.semilogy(cs, sens, color=C[1], lw=2, label="sensibilité 1 − Σ pᵢ²")
    ax.semilogy(cs, one_minus, color=C[0], lw=2, label="1 − p_max")
    ax.semilogy(cs, bound, color="black", lw=1.4, ls="--", label="borne de 1 − p_max : (K − 1) e^(−cΔ) = 3 e^(−c)")
    ax.semilogy(cs, 2 * bound, color="0.45", lw=1.2, ls=":", label="borne de la sensibilité : 6 e^(−c)")
    ax.set(xlabel="facteur c", ylabel="échelle logarithmique", ylim=(1e-4, 5),
           title="Saturation : des droites de pente −Δ en échelle logarithmique")
    ax.legend(fontsize=9, loc="upper right")
    fig.tight_layout(w_pad=2.5)
    save(fig, "saturation.png")
    for c in (2, 4, 6):
        p = softmax(c * S4)
        print(f"    c = {c}: p_max {p.max():.4f}, 1 − p_max {1 - p.max():.4f}, 1 − Σp² {1 - (p ** 2).sum():.4f}, "
              f"bound {3 * math.exp(-c):.4f}")


# --------------------------------------------------------------------------------------------------------- §8
def online_states() -> list[tuple[float, float, float]]:
    state = (-math.inf, 0.0, 0.0)
    out = []
    for start in range(0, len(S_ON), 3):
        ss, vv = S_ON[start:start + 3], V_ON[start:start + 3]
        fin = [k for k, s in enumerate(ss) if s != -math.inf]
        if fin:
            m_new = max(state[0], max(ss[k] for k in fin))
            f = 0.0 if state[0] == -math.inf else math.exp(state[0] - m_new)
            state = (m_new, state[1] * f + sum(math.exp(ss[k] - m_new) for k in fin),
                     state[2] * f + sum(math.exp(ss[k] - m_new) * vv[k] for k in fin))
        out.append(state)
    return out


def online() -> None:
    """§8: the scores read by blocks of three and the running maximum m; l and a/l after each block."""
    states = online_states()
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.6), gridspec_kw={"width_ratios": [1.25, 1]})
    ax = axes[0]
    for k, s in enumerate(S_ON):
        blk = k // 3
        if s == -math.inf:
            ax.add_patch(Rectangle((k + 1 - 0.35, -0.5), 0.7, 0.5, fc="0.9", ec="0.5", hatch="//"))
            ax.text(k + 1, -0.8, "−∞", ha="center", fontsize=10)
            continue
        ax.bar(k + 1, s, width=0.7, color=C[blk], alpha=0.85)
        if s == 0:
            ax.plot([k + 1 - 0.35, k + 1 + 0.35], [0, 0], color=C[blk], lw=4)
        ax.text(k + 1, s + 0.08, f"note {V_ON[k]:g}", ha="center", fontsize=8.5)
    for b, (m, _l, _a) in enumerate(states):
        ax.plot([3 * b + 0.5, 3 * b + 3.5], [m, m], color="black", lw=2)
        ax.text(3 * b + 0.6, m + 0.32, f"m = {m:g}", fontsize=9.5)
        if b:
            ax.axvline(3 * b + 0.5, color="0.6", lw=0.8, ls=":")
    ax.set_xticks(range(1, 8), [f"avis {k}" for k in range(1, 8)], fontsize=8.5)
    ax.keep_ticks = True
    ax.set(ylabel="score de fiabilité", ylim=(-1.2, 4.0), xlim=(0.4, 7.6),
           title="Sept avis lus par pages de trois : le plus grand score lu")
    ax = axes[1]
    blocks = np.arange(1, len(states) + 1)
    ls_ = [s[1] for s in states]
    means = [s[2] / s[1] for s in states]
    ax.plot(blocks, ls_, "o-", color=C[0], lw=2, label="l après la page")
    for b, val in zip(blocks, ls_):
        ax.annotate(fr(val, 4), (b, val), textcoords="offset points", xytext=(6, 4), fontsize=9, color=C[0])
    ax2 = ax.twinx()
    ax2.plot(blocks, means, "s--", color=C[1], lw=1.6, label="a/l (note moyenne pondérée)")
    for b, val in zip(blocks, means):
        ax2.annotate(fr(val, 4), (b, val), textcoords="offset points", xytext=(6, -14), fontsize=9, color=C[1])
    ax2.axhline(means[-1], color=C[1], lw=0.8, ls=":")
    ax2.set_ylabel("a/l", color=C[1])
    ax2.set_ylim(5.0, 7.6)
    ax2.yaxis.set_major_formatter(FuncFormatter(french_number))
    ax2.grid(False)
    ax.set(xlabel="page", ylabel="l", xticks=[1, 2, 3], ylim=(0.8, 3.4),
           title="L'état après chaque page : l remis à l'échelle à la page 3")
    lines = ax.get_legend_handles_labels()
    lines2 = ax2.get_legend_handles_labels()
    ax.legend(lines[0] + lines2[0], lines[1] + lines2[1], fontsize=9, loc="upper left")
    fig.tight_layout(w_pad=2.5)
    save(fig, "softmax_en_ligne.png")
    print("    states " + "; ".join(f"(m {m:g}, l {l_:.4f}, a {a:.4f}, a/l {a / l_:.4f})" for m, l_, a in states))


# --------------------------------------------------------------------------------------------------------- §9
def memory() -> None:
    """§9: n² float64 against n·B float64 (B = 500), in log-log scales: slopes 2 and 1."""
    ns = np.logspace(3, 6, 200)
    full = ns ** 2 * 8
    blocks = ns * B_EX * 8
    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    ax.loglog(ns, full, color=C[0], lw=2, label="la matrice n × n entière : 8n² octets (pente 2)")
    ax.loglog(ns, blocks, color=C[1], lw=2, label=f"un bloc de {B_EX} lignes : 8·{B_EX}·n octets (pente 1)")
    for n, col in ((N_EX, "black"), (2 * N_EX, "0.4")):
        ax.loglog([n], [n * n * 8], "o", color=col, ms=6)
        ax.loglog([n], [n * B_EX * 8], "o", color=col, ms=6)
    ax.annotate("n = 30 000 : 7,2 Go", (N_EX, N_EX ** 2 * 8), textcoords="offset points", xytext=(-120, 6), fontsize=9)
    ax.annotate("n = 60 000 : 28,8 Go (× 4)", (2 * N_EX, (2 * N_EX) ** 2 * 8), textcoords="offset points",
                xytext=(-150, 8), fontsize=9)
    ax.annotate("120 Mo, puis 240 Mo (× 2)", (N_EX, N_EX * B_EX * 8), textcoords="offset points", xytext=(4, -18),
                fontsize=9)
    for val, lab in ((1e9, "1 Go"), (1e12, "1 To")):
        ax.axhline(val, color="0.7", lw=0.8, ls=":")
        ax.text(1.1e3, val * 1.3, lab, fontsize=8.5, color="0.4")
    ax.set(xlabel="nombre n de clients (échelle logarithmique)", ylabel="mémoire (octets, échelle logarithmique)",
           title="La mémoire des distances entre n clients")
    ax.legend(fontsize=9, loc="upper left")
    fig.tight_layout()
    save(fig, "memoire.png")
    print(f"    n = {N_EX}: {N_EX ** 2 * 8:.3g} and {N_EX * B_EX * 8:.3g} octets")


def main() -> int:
    print(f"Figures MB3 → {OUT.relative_to(ROOT)}")
    wbplot.set_style()
    addition()
    plane_rotations()
    givens_matrices()
    rotation_order()
    clocks()
    kernel()
    masks()
    saturation()
    online()
    memory()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
