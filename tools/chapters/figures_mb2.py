#!/usr/bin/env python
"""Draw the figures of chapter MB2 (used by Claude).

    python tools/chapters/figures_mb2.py

Writes small PNG files into chapitres/mb2_cooccurrences/figures/:
- the PMI table of a pump watched by an acoustic sensor for 98 hours (regime × signal, counts
  [[0, 2, 47], [0, 8, 26], [1, 6, 8]]), and each non-empty cell against the bound −ln max(p(x), p(y));
- the smoothed column margin p_α(y) ∝ n(y)^α of the same table for α from 1 to 0, and the smoothed PMI of the row
  « rapide », whose order changes (α = 1/4 marked: the fourth roots of 1, 16 and 81);
- the rows of U₂S₂^β of a rank-2 table of visits (three feeders × three species, [[8, 9, 10], [4, 8, 12], [0, 7, 14]],
  s₁ = 4√42, s₂ = √42) for β = 0, 1/2 and 1;
- the parallelogram of an analogy in the plane, and the lemma ‖q − x‖ ≤ ε‖x‖ ⇒ cos(q, x) ≥ √(1 − ε²) (ε = 0.4);
- the first axis of three differences of (ln L, ln m) of trout, (1, 3)/√10, and three trout projected on its
  complement.
The numbers are those of the fiche; none comes from workbookIA B1 or B2 (no word, token, text, corpus nor word
vector). No figure draws random numbers: the seeds 7091 to 7099 kept for the figures of MB2 are not used.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "mb2_cooccurrences" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

# §2 and §3: a pump, 98 hours, regime (rows) × signal of the sensor (columns)
REGIMES = ["lent", "normal", "rapide"]
SIGNALS = ["arrêt", "alerte", "RAS"]
COUNTS = np.array([[0, 2, 47], [0, 8, 26], [1, 6, 8]], dtype=float)
ALPHA = 0.25
# §4: three feeders × three species, a table of rank 2
FEEDERS = ["A", "B", "C"]
BOX = 0.85                                                  # height / width of each panel
M_FEED = np.array([[8, 9, 10], [4, 8, 12], [0, 7, 14]], dtype=float)
# §6: a parallelogram in the plane, and the lemma with ε = 0.4
PA, PB, PC, PD = np.array([1.0, 2.6]), np.array([2.2, 3.4]), np.array([4.2, 0.8]), np.array([5.55, 1.35])
X_LEMMA, EPS = np.array([4.0, 1.5]), 0.4
# §7: three differences of (ln L, ln m), and three trout
DIFFS = np.array([[0.08, 0.14], [0.10, 0.30], [0.02, 0.16]])
TROUT = np.array([[3.0, 4.5], [3.2, 5.1], [3.1, 5.1]])


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


def pmi_table(joint: np.ndarray, col_margin: np.ndarray | None = None) -> np.ndarray:
    px = joint.sum(axis=1, keepdims=True)
    py = joint.sum(axis=0, keepdims=True) if col_margin is None else col_margin[None, :]
    out = np.full(joint.shape, -np.inf)
    pos = joint > 0
    out[pos] = np.log(joint[pos] / (px * py)[pos])
    return out


def smoothed_margin(counts_y: np.ndarray, alpha: float) -> np.ndarray:
    w = counts_y ** alpha
    return w / w.sum()


# --------------------------------------------------------------------------------------------------------- §2
def pmi_bound() -> None:
    """§2: the PMI table of the pump, and every non-empty cell under the bound −ln max(p(x), p(y))."""
    P = COUNTS / COUNTS.sum()
    px, py = P.sum(1), P.sum(0)
    pmi = pmi_table(P)
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.6), gridspec_kw={"width_ratios": [1, 1.25]})
    ax = axes[0]
    shown = np.where(np.isfinite(pmi), pmi, np.nan)
    im = ax.imshow(shown, cmap=wbplot.diverging_cmap(), vmin=-2, vmax=2)
    for i in range(3):
        for j in range(3):
            if np.isfinite(pmi[i, j]):
                ax.text(j, i, fr(pmi[i, j], 3), ha="center", va="center", fontsize=11,
                        color="white" if abs(pmi[i, j]) > 1.2 else "black", fontweight="bold")
            else:
                ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fc="0.85", ec="0.5", hatch="//", lw=0))
                ax.text(j, i, "−∞", ha="center", va="center", fontsize=12)
    ax.set_xticks(range(3), SIGNALS)
    ax.set_yticks(range(3), REGIMES)
    ax.keep_ticks = True
    ax.grid(False)
    ax.set(xlabel="signal du capteur", ylabel="régime de la pompe", title="PMI (nats) des 98 heures")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    ax = axes[1]
    grid = np.logspace(math.log10(0.05), 0, 300)
    ax.semilogx(grid, -np.log(grid), color="0.35", lw=1.6, label="borne −ln p")
    markers = {0: "s", 1: "o", 2: "^"}
    offsets = {(2, 0): (8, -3), (2, 1): (8, -3), (1, 1): (-90, -3), (0, 1): (8, -3), (0, 2): (-62, 8),
               (1, 2): (-76, -4), (2, 2): (-74, -12)}
    for j, sig in enumerate(SIGNALS):
        first = True
        for i, reg in enumerate(REGIMES):
            if not np.isfinite(pmi[i, j]):
                continue
            m = max(px[i], py[j])
            ax.plot(m, pmi[i, j], markers[j], color=C[j], ms=8, label=sig if first else None, zorder=3)
            first = False
            ax.annotate(f"{reg}, {sig}", (m, pmi[i, j]), textcoords="offset points", fontsize=8.5,
                        xytext=offsets[(i, j)])
    bound_ras = -math.log(py[2])
    ax.axhline(bound_ras, color=C[2], ls=":", lw=1.2)
    ax.text(0.05, bound_ras - 0.2, f"borne de la colonne RAS : {fr(bound_ras, 3)}", fontsize=9, color=C[2])
    ax.axhline(0, color="0.6", lw=0.8)
    ax.set(xlabel="max(p(x), p(y)) (échelle logarithmique)", ylabel="PMI (nats)",
           title="Chaque case sous la borne −ln max(p(x), p(y))", ylim=(-1.7, 3.2), xlim=(0.045, 1.25))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _p: french_number(v)))
    ax.legend(fontsize=9, loc="upper right")
    fig.tight_layout(w_pad=2.5)
    save(fig, "pmi_borne.png")
    print(f"    PMI {np.round(pmi, 4).tolist()}; RAS bound {bound_ras:.4f}")


# --------------------------------------------------------------------------------------------------------- §3
def smoothing() -> None:
    """§3: the smoothed margin of the columns and the smoothed PMI of the row « rapide », for α from 1 to 0."""
    P = COUNTS / COUNTS.sum()
    ny = COUNTS.sum(0)
    alphas = np.linspace(1, 0, 401)
    margins = np.array([smoothed_margin(ny, a) for a in alphas])
    rows = np.array([pmi_table(P, smoothed_margin(ny, a))[2] for a in alphas])
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.4))
    for ax in axes:
        ax.axvline(ALPHA, color="0.45", ls=":", lw=1.2)
        ax.set_xlim(1, 0)
    ax = axes[0]
    for j, sig in enumerate(SIGNALS):
        ax.plot(alphas, margins[:, j], color=C[j], label=sig)
        v = smoothed_margin(ny, ALPHA)[j]
        ax.plot(ALPHA, v, "o", color=C[j])
        ax.annotate(["1/6", "1/3", "1/2"][j], (ALPHA, v), textcoords="offset points", xytext=(6, 4), fontsize=9.5)
        ax.annotate(["1/98", "16/98", "81/98"][j], (1, margins[0, j]), textcoords="offset points",
                    xytext=(4, -12 if j else 4), fontsize=9)
    ax.set(xlabel="exposant α (lissage de plus en plus fort vers la droite)", ylabel=r"$p_\alpha(y)$",
           title="La marge lissée des signaux", ylim=(0, 0.9))
    ax.legend(fontsize=9.5)
    ax = axes[1]
    for j, sig in enumerate(SIGNALS):
        ax.plot(alphas, rows[:, j], color=C[j], label=sig)
        v = pmi_table(P, smoothed_margin(ny, ALPHA))[2, j]
        ax.plot(ALPHA, v, "o", color=C[j])
        ax.annotate(fr(v, 3), (ALPHA, v), textcoords="offset points", xytext=(6, -12 if j == 2 else 4), fontsize=9.5)
    ax.annotate(fr(rows[0, 0], 3), (1, rows[0, 0]), textcoords="offset points", xytext=(4, -4), fontsize=9)
    ax.axhline(0, color="0.6", lw=0.8)
    ax.set(xlabel="exposant α", ylabel="PMI lissée (nats)", title="La ligne « rapide » : l'ordre change")
    ax.legend(fontsize=9.5)
    fig.tight_layout(w_pad=3)
    save(fig, "lissage.png")
    cross_alert = alphas[np.argmax(rows[:, 0] < rows[:, 1])]
    cross_ras = alphas[np.argmax(rows[:, 0] < rows[:, 2])]
    print(f"    p_1/4 {np.round(smoothed_margin(ny, ALPHA), 4).tolist()}; the stop passes the alert at α ≈ "
          f"{cross_alert:.3f} and RAS at α ≈ {cross_ras:.3f}")


# --------------------------------------------------------------------------------------------------------- §4
def factors_beta() -> None:
    """§4: the rows of U₂S₂^β of the feeders for β = 0, 1/2 and 1: the product is the same, the angles are not."""
    U, s, Vt = np.linalg.svd(M_FEED)
    sign = np.sign(Vt[np.arange(2), np.argmax(np.abs(Vt[:2]), axis=1)])   # mymath's sign convention
    U, s = U[:, :2] * sign, s[:2]
    fig, axes = plt.subplots(1, 3, figsize=(13.6, 4.9))
    for ax, beta, lab in zip(axes, (0.0, 0.5, 1.0), ("β = 0", "β = 1/2", "β = 1")):
        W = U * s ** beta
        Vb = Vt[:2].T * sign * s ** (1 - beta)
        assert np.allclose(W @ Vb.T, M_FEED)
        cos_ac = W[0] @ W[2] / np.linalg.norm(W[0]) / np.linalg.norm(W[2])
        xmax, ymax = np.abs(W[:, 0]).max(), np.abs(W[:, 1]).max()
        width = max(1.45 * xmax, 2.7 * ymax / BOX)                    # the same box in the three panels
        height = BOX * width
        for i, name in enumerate(FEEDERS):
            ax.add_patch(FancyArrowPatch((0, 0), tuple(W[i]), arrowstyle="-|>", mutation_scale=14, lw=2,
                                         color=C[i]))
            ax.annotate(name, tuple(W[i]), textcoords="offset points", xytext=(6, 2), fontsize=12, fontweight="bold",
                        color=C[i])
        ax.axhline(0, color="0.6", lw=0.8)
        ax.axvline(0, color="0.6", lw=0.8)
        ax.set(xlim=(-0.1 * width, 0.9 * width), ylim=(-height / 2, height / 2), aspect="equal", xlabel="coordonnée 1",
               ylabel="coordonnée 2", title=f"{lab} : cos(A, C) ≈ {fr(cos_ac, 3)}")
        print(f"    beta = {beta}: rows {np.round(W, 4).tolist()}, cos(A, C) = {cos_ac:.4f}")
    fig.suptitle(r"Les lignes de $\mathbf{U}_2\mathbf{S}_2^{\beta}$ des trois mangeoires", fontsize=12.5, fontweight="bold")
    fig.tight_layout(w_pad=2)
    save(fig, "facteurs_beta.png")
    print(f"    singular values {np.round(s, 4).tolist()} (4√42 = {4 * math.sqrt(42):.4f}, √42 = {math.sqrt(42):.4f})")


# --------------------------------------------------------------------------------------------------------- §6
def analogy() -> None:
    """§6: the parallelogram of an analogy, and the cone of half-angle arcsin ε seen from the origin."""
    fig, axes = plt.subplots(1, 2, figsize=(12.4, 4.8))
    ax = axes[0]
    q = PB - PA + PC
    for start, end, col in ((PA, PB, C[0]), (PC, q, C[0])):
        ax.add_patch(FancyArrowPatch(tuple(start), tuple(end), arrowstyle="-|>", mutation_scale=14, lw=2, color=col))
    ax.plot([PA[0], PC[0]], [PA[1], PC[1]], ls="--", color="0.6", lw=1)
    ax.plot([PB[0], q[0]], [PB[1], q[1]], ls="--", color="0.6", lw=1)
    for p, name, off in ((PA, "a", (-14, 4)), (PB, "b", (-4, 8)), (PC, "c", (-6, -16)), (q, "q = b − a + c", (8, 4)),
                         (PD, "d", (8, -10))):
        ax.plot(*p, "o", color=C[1] if name == "d" else "black", ms=6, zorder=3)
        ax.annotate(name, tuple(p), textcoords="offset points", xytext=off, fontsize=11)
    ax.annotate("défaut δ = ‖q − d‖", tuple((q + PD) / 2), textcoords="offset points", xytext=(10, -26), fontsize=9.5,
                color=C[1])
    ax.text(1.35, 3.25, "b − a", color=C[0], fontsize=10)
    ax.text(4.55, 1.45, "b − a", color=C[0], fontsize=10)
    ax.set(xlim=(0, 7), ylim=(0, 4.2), aspect="equal", xlabel="coordonnée 1", ylabel="coordonnée 2",
           title="Le parallélogramme d'une analogie")
    ax = axes[1]
    x = X_LEMMA
    r = EPS * np.linalg.norm(x)
    half = math.asin(EPS)
    theta = math.atan2(x[1], x[0])
    ax.add_patch(Circle(tuple(x), r, fc=C[0], alpha=0.15, ec=C[0], lw=1.5))
    ax.add_patch(FancyArrowPatch((0, 0), tuple(x), arrowstyle="-|>", mutation_scale=14, lw=2, color="black"))
    ax.annotate("x", tuple(x), textcoords="offset points", xytext=(4, -14), fontsize=12)
    length = np.linalg.norm(x) * math.cos(half)
    for sgn in (1, -1):
        t = theta + sgn * half
        ax.plot([0, 1.25 * length * math.cos(t)], [0, 1.25 * length * math.sin(t)], color=C[2], lw=1.4, ls="--")
    angles = np.linspace(0, 2 * math.pi, 9)[:-1]
    for k, a in enumerate(angles):
        qq = x + 0.8 * r * np.array([math.cos(a), math.sin(a)])
        ax.plot(*qq, "o", color=C[1], ms=4.5)
        cos_q = qq @ x / np.linalg.norm(qq) / np.linalg.norm(x)
        assert cos_q >= math.sqrt(1 - EPS ** 2) - 1e-12
    ax.annotate("rayon ε‖x‖", tuple(x + np.array([0, r])), textcoords="offset points", xytext=(4, 4), fontsize=9.5)
    arc = np.linspace(theta, theta + half, 40)
    ax.plot(1.2 * np.cos(arc), 1.2 * np.sin(arc), color=C[2], lw=1.2)
    ax.text(1.35 * math.cos(theta + half / 2), 1.35 * math.sin(theta + half / 2),
            f"arcsin ε ≈ {fr(math.degrees(half), 1)}°", fontsize=9.5, color=C[2])
    ax.set(xlim=(-0.3, 6.5), ylim=(-0.6, 4.2), aspect="equal", xlabel="coordonnée 1", ylabel="coordonnée 2",
           title=f"Si ‖q − x‖ ≤ ε‖x‖ : cos(q, x) ≥ √(1 − ε²) ≈ {fr(math.sqrt(1 - EPS ** 2), 3)}")
    fig.tight_layout(w_pad=3)
    save(fig, "analogie.png")
    print(f"    q = {q.tolist()}, d = {PD.tolist()}, defect {np.linalg.norm(q - PD):.3f}; eps = {EPS}: "
          f"arcsin {math.degrees(half):.2f}°, bound {math.sqrt(1 - EPS ** 2):.4f}")


# --------------------------------------------------------------------------------------------------------- §7
def direction() -> None:
    """§7: the first axis of three differences, the trout and the lines along u, and what remains after removing u."""
    G = DIFFS.T @ DIFFS
    lam, vecs = np.linalg.eigh(G)
    u = vecs[:, -1] * np.sign(vecs[1, -1])
    assert np.allclose(u, np.array([1, 3]) / math.sqrt(10))
    w = np.array([3.0, -1.0]) / math.sqrt(10)
    fig, axes = plt.subplots(1, 3, figsize=(14.2, 4.9), gridspec_kw={"width_ratios": [1, 1, 1.15]})
    ax = axes[0]
    t = np.linspace(-0.01, 0.115, 2)
    ax.plot(t, 3 * t, color="0.55", ls="--", lw=1.2, label="premier axe : u = (1, 3)/√10", zorder=1)
    for k, d in enumerate(DIFFS):
        ax.add_patch(FancyArrowPatch((0, 0), tuple(d), arrowstyle="-|>", mutation_scale=12, lw=1.8, color=C[k],
                                     zorder=2))
        ax.annotate(f"d{chr(0x2081 + k)}", tuple(d), textcoords="offset points", xytext=(5, -4), fontsize=11)
    ax.set(xlim=(-0.02, 0.24), ylim=(-0.02, 0.36), aspect="equal", xlabel="différence de ln L",
           ylabel="différence de ln m", title=f"Premier axe : λ₁ = {fr(lam[-1], 3)}, λ₂ = {fr(lam[0], 3)}")
    ax.legend(fontsize=9, loc="lower right")
    ax = axes[1]
    for k, x in enumerate(TROUT):
        if k == 1:
            continue
        tt = np.linspace(-0.12, 0.25, 2)
        ax.plot(x[0] + tt, x[1] + 3 * tt, color="0.6", lw=1.1, ls="--", zorder=1)
    for k, x in enumerate(TROUT):
        ax.plot(*x, "o", color=C[k], ms=8, zorder=3)
        ax.annotate(f"truite {k + 1}", tuple(x), textcoords="offset points",
                    xytext=[(8, -4), (8, -14), (-58, 6)][k], fontsize=10)
    ax.add_patch(FancyArrowPatch((2.95, 4.75), (2.95 + 0.06, 4.75 + 0.18), arrowstyle="-|>", mutation_scale=12,
                                 lw=1.6, color="black"))
    ax.text(2.92, 4.95, "u", fontsize=12)
    ax.set(xlim=(2.85, 3.35), ylim=(4.3, 5.4), aspect="equal", xlabel="ln L (L en cm)", ylabel="ln m (m en g)",
           title="Les truites et les droites de direction u")
    ax = axes[2]
    R = TROUT - np.outer(TROUT @ u, u)
    tt = np.linspace(0.0, 1.55, 2)
    ax.plot(3 * tt, -tt, color="0.35", lw=1.4, label="le complément R(3, −1)")
    for k, r in enumerate(R):
        ax.plot(*r, "s" if k != 1 else "o", color=C[k], ms=9 if k == 0 else 6, zorder=3 + k)
    ax.annotate("truites 1 et 2 : (1,35 ; −0,45)", tuple(R[0]), textcoords="offset points", xytext=(10, 4),
                fontsize=9.5)
    ax.annotate("truite 3 : (1,26 ; −0,42)", tuple(R[2]), textcoords="offset points", xytext=(-150, -16),
                fontsize=9.5)
    ax.axhline(0, color="0.6", lw=0.8)
    ax.axvline(0, color="0.6", lw=0.8)
    ax.set(xlim=(-0.1, 2.4), ylim=(-0.75, 0.25), aspect="equal", xlabel="coordonnée 1", ylabel="coordonnée 2",
           title="Ce qui reste après le retrait de u")
    ax.legend(fontsize=9, loc="upper right")
    fig.tight_layout(w_pad=2.5)
    save(fig, "direction.png")
    print(f"    DᵀD {np.round(G, 4).tolist()}, eigenvalues {np.round(lam, 4).tolist()}; rests {np.round(R, 4).tolist()}; "
          f"x·w {np.round(TROUT @ w, 4).tolist()}")


def main() -> int:
    print(f"Figures MB2 → {OUT.relative_to(ROOT)}")
    wbplot.set_style()
    pmi_bound()
    smoothing()
    factors_beta()
    analogy()
    direction()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
