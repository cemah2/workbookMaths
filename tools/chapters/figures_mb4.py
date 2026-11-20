#!/usr/bin/env python
"""Draw the figures of chapter MB4 (used by Claude).

    python tools/chapters/figures_mb4.py

Writes small PNG files into chapitres/mb4_rang_faible/figures/:
- §1: the alloy table of the fiche (copper, zinc and tin in four alloys, two of them blends of the first two) as the
  product C F of its pivot columns by the rows of its reduced form, and as the sum of two outer products;
- §2: the energy of six singular values (10, 6, 3, 0.4, 0.3, 0.2), its cumulative share and the stable rank; the
  singular values of a simulated 120 × 40 table of rank 5 plus noise, against the noise level σ(√m + √n);
- §3: three weights of a clue present in n records out of N = 800 (the surprise, the corrected log odds ratio without
  relevance information, the variant that stays positive), with the clinic's two clues (n = 51 and n = 640);
- §4: the saturation x ↦ x(k₁ + 1)/(x + k₁) from k₁ → 0 to k₁ → ∞; the normalization 1 − b + bℓ for four values
  of b; the saturation k₁ = 3 for a record half as long, as long and three times as long as the mean (b = 1/2);
- §5: the place of four photos in the fusion of four judges' rankings as c grows (A then B first, switch at
  c = (1 + √57)/2); the region where j-th in two lists beats first in one (j < c + 2);
- §6: the law of the rank R of the first relevant object among 12 (q = 1, 2, 4); the rectangles that frame H_n;
  E[1/R] = H_n/n against n, between ln(n + 1)/n and (1 + ln n)/n.
The numbers are those of the fiche; none comes from workbookIA B1 to B4, nor from the exercises of MB4. Only the
simulated table of §2 draws random numbers (seed 7491, among the seeds 7491 to 7499 kept for the figures of MB4).
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
from matplotlib.patches import Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "mb4_rang_faible" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

# §1: kg of copper, zinc and tin in 100 kg of brass, bronze and two blends (1/2–1/2 and 3/4–1/4)
ALLOYS = np.array([[60.0, 80.0, 70.0, 65.0], [40.0, 0.0, 20.0, 30.0], [0.0, 20.0, 10.0, 5.0]])
METALS = ["cuivre", "zinc", "étain"]
NAMES = ["laiton", "bronze", "alliage 3", "alliage 4"]
# §2: six singular values of a 40 × 6 table of measurements; a simulated table for the gap
SV = np.array([10.0, 6.0, 3.0, 0.4, 0.3, 0.2])
SIM_M, SIM_N, SIM_R, SIM_SIGMA, SIM_SEED = 120, 40, 5, 0.1, 7491
# §3: a veterinary clinic, 800 records; limping in 51 of them, tiredness in 640
N_REC, N_LIMP, N_TIRED = 800, 51, 640
# §5: four judges rank four photos (best first)
RANKINGS = ["ABCD", "ABCD", "CBAD", "DBCA"]


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


def rref(A: np.ndarray, tol: float = 1e-10):
    """Reduced row echelon form and pivot columns (partial pivoting), as in M09a."""
    R = np.array(A, dtype=float)
    m, n = R.shape
    pivots, row = [], 0
    for col in range(n):
        if row == m:
            break
        p = row + int(np.argmax(np.abs(R[row:, col])))
        if abs(R[p, col]) <= tol:
            continue
        R[[row, p]] = R[[p, row]]
        R[row] /= R[row, col]
        for i in range(m):
            if i != row:
                R[i] -= R[i, col] * R[row]
        pivots.append(col)
        row += 1
    R[np.abs(R) <= tol] = 0.0
    return R, pivots


def frac_text(v: float) -> str:
    f = Fraction(v).limit_denominator(16)
    if f.denominator == 1:
        return f"{f.numerator}"
    return f"{f.numerator}/{f.denominator}".replace("-", "−")


def heat(ax, A, title, rows=None, cols=None, vmax=80.0, fracs=False, cmap=None):
    ax.imshow(A, cmap=cmap or wbplot.sequential_cmap(), vmin=0, vmax=vmax, aspect="equal")
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            v = A[i, j]
            txt = frac_text(v) if fracs else f"{v:g}"
            ax.text(j, i, txt, ha="center", va="center", fontsize=10,
                    color="white" if v > 0.6 * vmax else "black")
    ax.set_xticks(range(A.shape[1]), cols if cols is not None else [str(k + 1) for k in range(A.shape[1])],
                  fontsize=8.5)
    ax.set_yticks(range(A.shape[0]), rows if rows is not None else [str(k + 1) for k in range(A.shape[0])],
                  fontsize=8.5)
    ax.keep_ticks = True
    ax.grid(False)
    ax.set_title(title, fontsize=10.5)


# --------------------------------------------------------------------------------------------------------- §1
def factorization() -> None:
    """§1: M = C F with the pivot columns and the reduced rows; M = c1 f1ᵀ + c2 f2ᵀ."""
    R, piv = rref(ALLOYS)
    assert piv == [0, 1]
    Cm, Fm = ALLOYS[:, piv], R[:2]
    assert np.allclose(Cm @ Fm, ALLOYS)
    L1, L2 = np.outer(Cm[:, 0], Fm[0]), np.outer(Cm[:, 1], Fm[1])
    assert np.allclose(L1 + L2, ALLOYS)
    fig = plt.figure(figsize=(13.2, 6.6))
    gs = fig.add_gridspec(2, 5, width_ratios=[2.2, 0.35, 4.2, 0.35, 4.2], height_ratios=[1, 1], wspace=0.25,
                          hspace=0.55)
    heat(fig.add_subplot(gs[0, 0]), Cm, "C : les colonnes pivots", METALS, NAMES[:2])
    ax = fig.add_subplot(gs[0, 1])
    ax.axis("off")
    ax.text(0.5, 0.5, "×", fontsize=22, ha="center", va="center")
    heat(fig.add_subplot(gs[0, 2]), Fm, "F : les recettes (lignes non nulles de la forme réduite)",
         ["laiton", "bronze"], NAMES, vmax=1.6, fracs=True)
    ax = fig.add_subplot(gs[0, 3])
    ax.axis("off")
    ax.text(0.5, 0.5, "=", fontsize=22, ha="center", va="center")
    heat(fig.add_subplot(gs[0, 4]), ALLOYS, "M : kg de métal pour 100 kg d'alliage", METALS, NAMES)
    ax = fig.add_subplot(gs[1, 0:2])
    ax.axis("off")
    ax.text(0.75, 0.5, "M  =", fontsize=20, ha="center", va="center")
    heat(fig.add_subplot(gs[1, 2]), L1, r"$\mathbf{c}_1\mathbf{f}_1^\top$ : la part du laiton (rang 1)", METALS,
         NAMES)
    ax = fig.add_subplot(gs[1, 3])
    ax.axis("off")
    ax.text(0.5, 0.5, "+", fontsize=22, ha="center", va="center")
    heat(fig.add_subplot(gs[1, 4]), L2, r"$\mathbf{c}_2\mathbf{f}_2^\top$ : la part du bronze (rang 1)", METALS, NAMES)
    fig.suptitle("Un tableau de rang 2 : un produit C F, et une somme de deux produits extérieurs",
                 fontsize=12.5, fontweight="bold")
    save(fig, "factorisation.png")
    print(f"    pivots {piv}; F = {np.round(Fm, 4).tolist()}")


# --------------------------------------------------------------------------------------------------------- §2
def energy() -> None:
    """§2: energy shares of six singular values, stable rank; a simulated noisy table and the noise level."""
    s2 = SV ** 2
    E = s2.sum()
    cum = np.cumsum(s2) / E
    srank = E / s2[0]
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.9))
    ax = axes[0]
    ks = np.arange(1, len(SV) + 1)
    ax.bar(ks, s2 / E, color=C[0], width=0.6, label="part de l'énergie de $s_i^2$")
    ax.plot(ks, cum, "o-", color=C[1], lw=1.8, label="part cumulée des $r$ premières")
    for t, lab in ((0.90, "90 %"), (0.99, "99 %")):
        ax.axhline(t, color="0.55", lw=0.9, ls=":")
        ax.text(6.45, t, lab, fontsize=9, va="center", color="0.35")
    for k in (2, 3):
        ax.annotate(f"{fr(100 * cum[k - 1], 1)} %", (k, cum[k - 1]), textcoords="offset points", xytext=(-14, -18),
                    fontsize=9, color=C[1])
    ax.axvline(srank, color=C[2], lw=1.6, ls="--")
    stable = r"$\Vert\mathbf{M}\Vert_F^2/\Vert\mathbf{M}\Vert_2^2$"
    ax.text(srank + 0.08, 0.42, "rang stable\n" + stable + f" ≈ {fr(srank, 2)}",
            fontsize=9.5, color=C[2])
    ax.set(xlabel="rang r", ylabel=r"part de $\Vert\mathbf{M}\Vert_F^2$", xticks=ks, ylim=(0, 1.08), xlim=(0.4, 6.9),
           title="s = (10 ; 6 ; 3 ; 0,4 ; 0,3 ; 0,2) : l'énergie gardée par rang")
    ax.legend(fontsize=9, loc="center right")
    ax = axes[1]
    rng = np.random.default_rng(SIM_SEED)
    signal = rng.standard_normal((SIM_M, SIM_R)) @ np.diag([1.6, 1.2, 0.9, 0.7, 0.5]) @ \
        rng.standard_normal((SIM_R, SIM_N)) / math.sqrt(SIM_N)
    noisy = signal + SIM_SIGMA * rng.standard_normal((SIM_M, SIM_N))
    sv = np.linalg.svd(noisy, compute_uv=False)
    level = SIM_SIGMA * (math.sqrt(SIM_M) + math.sqrt(SIM_N))
    k = np.arange(1, len(sv) + 1)
    ax.semilogy(k[:SIM_R], sv[:SIM_R], "o", color=C[0], ms=7, label="les 5 premières")
    ax.semilogy(k[SIM_R:], sv[SIM_R:], "o", color="0.55", ms=4, label="les autres")
    ax.axhline(level, color=C[1], lw=1.6, ls="--",
               label=f"niveau du bruit σ(√m + √n) ≈ {fr(level, 2)}")
    ax.annotate(f"écart : s₅/s₆ ≈ {fr(sv[4] / sv[5], 1)}", (5.5, math.sqrt(sv[4] * sv[5])),
                textcoords="offset points",
                xytext=(14, 0), fontsize=9.5, va="center")
    ax.set(xlabel="i", ylabel="valeur singulière $s_i$ (échelle logarithmique)", xlim=(0, SIM_N + 1),
           title=f"Un tableau {SIM_M} × {SIM_N} de rang {SIM_R}, plus un bruit d'écart-type {fr(SIM_SIGMA, 1)}")
    ax.legend(fontsize=9, loc="upper right")
    fig.tight_layout(w_pad=3)
    save(fig, "energie.png")
    rank_tol = int(np.sum(sv > level))
    print(f"    energy {E:.2f}, cumulative {np.round(100 * cum, 2).tolist()}, stable rank {srank:.4f}")
    print(f"    simulated: s5 {sv[4]:.3f}, s6 {sv[5]:.3f}, s1 {sv[0]:.2f}, level {level:.4f}, kept {rank_tol}, "
          f"stable rank {np.sum(sv ** 2) / sv[0] ** 2:.3f}")


# --------------------------------------------------------------------------------------------------------- §3
def rarity() -> None:
    """§3: surprise, corrected log odds without relevance information, and the positive variant, for N = 800."""
    N = N_REC
    n = np.arange(1, N + 1)
    surprise = np.log(N / n)
    rsj = np.log((N - n + 0.5) / (n + 0.5))
    variant = np.log((N + 1) / (n + 0.5))
    fig, ax = plt.subplots(figsize=(8.6, 4.9))
    ax.axvspan(N / 2, N, color="0.94", zorder=0)
    ax.text(0.75 * N, 3.6, "n > N/2 : le poids sans information\nde pertinence est négatif", ha="center", fontsize=9,
            color="0.35")
    ax.plot(n, surprise, color=C[0], lw=1.8, label="surprise −ln(n/N)")
    ax.plot(n, rsj, color=C[1], lw=2.0, label="ln((N − n + ½)/(n + ½)) : sans information de pertinence")
    ax.plot(n, variant, color=C[2], lw=1.6, ls="--",
            label="ln((N + 1)/(n + ½)) : toujours positive, presque la surprise")
    ax.axhline(0, color="0.5", lw=0.9)
    ax.plot([N / 2], [0], "o", color=C[1], ms=6)
    ax.annotate("n = N/2 = 400 : 0", (N / 2, 0), textcoords="offset points", xytext=(-40, -18), fontsize=9)
    for nn, lab in ((N_LIMP, "boiterie\n(n = 51)"), (N_TIRED, "fatigue\n(n = 640)")):
        y = math.log((N - nn + 0.5) / (nn + 0.5))
        ax.plot([nn], [y], "s", color="black", ms=6, zorder=4)
        ax.annotate(f"{lab} : {fr(y, 2)}", (nn, y), textcoords="offset points", xytext=(8, 6 if y > 0 else -30),
                    fontsize=9)
    ax.set(xlabel="n, le nombre de dossiers qui contiennent l'indice (N = 800)", ylabel="poids (nats)",
           xlim=(0, N), ylim=(-4.2, 6.2), title="Trois poids d'un indice, du plus rare au plus commun")
    ax.legend(fontsize=9, loc="upper right")
    fig.tight_layout()
    save(fig, "rarete.png")
    print(f"    limping: {math.log((N - N_LIMP + .5) / (N_LIMP + .5)):.4f}; "
          f"tiredness: {math.log((N - N_TIRED + .5) / (N_TIRED + .5)):.4f}")


# --------------------------------------------------------------------------------------------------------- §4
def saturation() -> None:
    """§4: saturation curves, normalization lines, and the k1 = 3 curve for three lengths (b = 1/2)."""
    x = np.linspace(0, 12, 601)
    fig, axes = plt.subplots(1, 3, figsize=(15.0, 4.8), gridspec_kw={"width_ratios": [1.25, 1, 1.15]})
    ax = axes[0]
    ax.plot(x, np.where(x > 0, 1.0, 0.0), color="0.45", lw=1.4, ls=":", label="k₁ → 0 : la seule présence")
    for k1, col in ((1, C[0]), (2, C[1]), (3, C[2])):
        ax.plot(x, x * (k1 + 1) / (x + k1), color=col, lw=2, label=f"k₁ = {k1} : plafond {k1 + 1}")
        ax.axhline(k1 + 1, color=col, lw=0.8, ls="--", alpha=0.7)
    ax.plot(x, x, color="0.45", lw=1.4, ls="-.", label="k₁ → ∞ : le compte brut x")
    ax.plot([1], [1], "o", color="black", ms=6, zorder=5)
    ax.annotate("(1, 1) pour tout k₁", (1, 1), textcoords="offset points", xytext=(10, -14), fontsize=9)
    ax.plot([3], [2], "s", color=C[2], ms=6, zorder=5)
    ax.annotate("k₁ = 3 : la moitié du plafond\nen x = k₁ = 3", (3, 2), xytext=(6.2, 1.05), fontsize=8.5,
                color=C[2],
                arrowprops=dict(arrowstyle="->", color=C[2], lw=1))
    ax.set(xlabel="x, le nombre de mentions", ylabel="s(x) = x(k₁ + 1)/(x + k₁)", xlim=(0, 12), ylim=(0, 5.2),
           title="La saturation : croissante, concave, plafonnée")
    ax.legend(fontsize=8.5, loc="upper left", frameon=True, framealpha=0.95, edgecolor="none")
    ax = axes[1]
    ell = np.linspace(0, 3.2, 100)
    for b, col in ((0, "0.45"), (0.25, C[0]), (0.5, C[1]), (1, C[2])):
        lab = {0: "b = 0 : aucune normalisation", 0.25: "b = 1/4", 0.5: "b = 1/2", 1: "b = 1 : ν = ℓ"}[b]
        ax.plot(ell, 1 - b + b * ell, color=col, lw=2, label=lab)
    ax.plot([1], [1], "o", color="black", ms=6, zorder=5)
    ax.annotate("ℓ = 1 : ν = 1 pour tout b", (1, 1), textcoords="offset points", xytext=(10, -16), fontsize=9)
    ax.set(xlabel="ℓ, la longueur rapportée à la moyenne", ylabel="ν = 1 − b + bℓ", xlim=(0, 3.2),
           ylim=(0, 3.3),
           title="La normalisation : affine en ℓ et en b")
    ax.legend(fontsize=8.5, loc="upper left")
    ax = axes[2]
    lengths = ((0.5, C[0], "ℓ = 1/2 : ν = 3/4"), (1.0, "black", "ℓ = 1 : ν = 1"), (3.0, C[1], "ℓ = 3 : ν = 2"))
    for ell_v, col, lab in lengths:
        nu = 1 - 0.5 + 0.5 * ell_v
        ax.plot(x, x * 4 / (x + 3 * nu), color=col, lw=2, label=lab)
    ax.axhline(4, color="0.5", lw=0.8, ls="--")
    ax.text(11.8, 3.82, "plafond 4", ha="right", fontsize=9, color="0.35")
    ax.plot([1, 1, 1], [4 / (1 + 2.25), 1, 4 / 7], "o", color="0.3", ms=5)
    ax.annotate("une mention : 16/13, 1, 4/7", (1, 4 / 7), textcoords="offset points", xytext=(10, -14), fontsize=8.5)
    ax.set(xlabel="x, le nombre de mentions", ylabel="s(x/ν) = x(k₁ + 1)/(x + k₁ν)", xlim=(0, 12), ylim=(0, 4.4),
           title="k₁ = 3, b = 1/2 : un dossier long, un court")
    ax.legend(fontsize=8.5, loc="lower right")
    fig.tight_layout(w_pad=2.2)
    save(fig, "saturation.png")
    print(f"    k1 = 3: s(1, 3, 7, 21) = {[round(v * 4 / (v + 3), 4) for v in (1, 3, 7, 21)]}")


# --------------------------------------------------------------------------------------------------------- §5
def fusion() -> None:
    """§5: the place of each photo in the fusion as c grows; the region j < c + 2."""
    cands = "ABCD"
    ranks = {c: [rk.index(c) + 1 for rk in RANKINGS] for c in cands}
    cs = np.exp(np.linspace(math.log(0.5), math.log(300), 800))
    places = {c: [] for c in cands}
    for cv in cs:
        sc = {c: sum(1 / (cv + j) for j in ranks[c]) for c in cands}
        order = sorted(cands, key=lambda c: (-sc[c], c))
        for c in cands:
            places[c].append(order.index(c) + 1)
    cstar = (1 + math.sqrt(57)) / 2
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.9), gridspec_kw={"width_ratios": [1.25, 1]})
    ax = axes[0]
    styles = {"A": (C[0], "-"), "B": (C[1], "-"), "C": (C[2], "--"), "D": ("0.45", ":")}
    for c in cands:
        col, ls = styles[c]
        lab = f"photo {c} : rangs {tuple(ranks[c])}, somme {sum(ranks[c])}"
        ax.plot(cs, places[c], color=col, ls=ls, lw=2.4, drawstyle="steps-post", label=lab)
    ax.axvline(cstar, color="0.4", lw=1, ls=":")
    ax.text(cstar * 1.07, 1.45, "c = (1 + √57)/2 ≈ 4,27", fontsize=9, color="0.3")
    ax.set_xscale("log")
    ax.set(xlabel="la constante c (échelle logarithmique)", ylabel="place dans la fusion", ylim=(4.5, 0.5),
           yticks=[1, 2, 3, 4], title="Somme des 1/(c + rang) : A d'abord, puis l'ordre de Borda")
    ax.xaxis.set_major_formatter(FuncFormatter(french_number))
    ax.legend(fontsize=8.5, loc="center right", bbox_to_anchor=(1.0, 0.5))
    ax = axes[1]
    cg = np.linspace(0.5, 10, 400)
    ax.fill_between(cg, 1.5, cg + 2, color=C[0], alpha=0.18, label="deux fois j-ième l'emporte")
    ax.plot(cg, cg + 2, color=C[0], lw=2, label="j = c + 2 : égalité")
    for cv in range(1, 11):
        for j in range(2, 14):
            win = 2 / (cv + j) > 1 / (cv + 1)
            tie = 2 * (cv + 1) == cv + j
            ax.plot(cv, j, "o" if win else ("D" if tie else "x"), color=C[0] if win else ("black" if tie else C[1]),
                    ms=4.5 if not tie else 5.5)
    ax.set(xlabel="la constante c", ylabel="rang j dans les deux listes", xlim=(0.5, 10.3), ylim=(1.5, 13.5),
           title="Deux fois j-ième contre une fois premier")
    ax.plot([], [], "x", color=C[1], label="une fois premier l'emporte")
    ax.legend(fontsize=8.5, loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=2)
    fig.tight_layout(w_pad=2.5)
    save(fig, "fusion.png")
    print(f"    ranks {ranks}; switch at c = {cstar:.4f}")


# --------------------------------------------------------------------------------------------------------- §6
def first_relevant() -> None:
    """§6: law of R for n = 12; rectangles around H_n; E[1/R] = H_n/n and its bounds."""
    n = 12
    fig, axes = plt.subplots(1, 3, figsize=(15.0, 4.7), gridspec_kw={"width_ratios": [1.1, 1, 1.1]})
    ax = axes[0]
    width = 0.27
    for k, (q, col) in enumerate(((1, C[0]), (2, C[1]), (4, C[2]))):
        js = np.arange(1, n - q + 2)
        p = np.array([math.comb(n - j, q - 1) / math.comb(n, q) for j in js])
        assert abs(p.sum() - 1) < 1e-12
        mean_inv = float(np.sum(p / js))
        ax.bar(js + (k - 1) * width, p, width=width, color=col,
               label=f"q = {q} : E[1/R] ≈ {fr(mean_inv, 2)}")
    ax.set(xlabel="j", ylabel="P(R = j)", xticks=range(1, n + 1), xlim=(0.4, n + 0.6))
    ax.set_title(f"La loi de R parmi n = {n} objets, ordre au hasard", fontsize=11)
    ax.legend(fontsize=9, loc="upper right")
    ax = axes[1]
    m = 7
    xs = np.linspace(0.6, m + 1.4, 400)
    ax.plot(xs, 1 / xs, color="black", lw=1.8, label="1/x")
    for j in range(1, m + 1):
        ax.add_patch(Rectangle((j, 0), 1, 1 / j, fc=C[0], ec=C[0], alpha=0.22, lw=1))
    for j in range(1, m):
        ax.add_patch(Rectangle((j, 0), 1, 1 / (j + 1), fc="none", ec=C[1], lw=1.6))
    ax.plot([], [], "s", color=C[0], alpha=0.4,
            label=r"aires $1, \frac{1}{2}, \ldots, \frac{1}{7}$ sur $[1, 8]$ : $H_7 \geq \ln 8$")
    ax.plot([], [], "s", mfc="none", color=C[1],
            label=r"aires $\frac{1}{2}, \ldots, \frac{1}{7}$ sur $[1, 7]$ : $H_7 - 1 \leq \ln 7$")
    hm = sum(1 / j for j in range(1, m + 1))
    ax.set(xlabel="x", ylabel="hauteur", xlim=(0.6, m + 1.4), ylim=(0, 1.15))
    ax.set_title(r"$\ln 8 \leq H_7 \leq 1 + \ln 7$ : " + f"{fr(math.log(m + 1), 3)} ≤ {fr(hm, 3)} ≤ "
                 f"{fr(1 + math.log(m), 3)}", fontsize=11)
    ax.legend(fontsize=9, loc="upper right")
    ax = axes[2]
    ns = np.arange(2, 501)
    Hn = np.cumsum(1 / np.arange(1, 501))[1:]
    ax.loglog(ns, Hn / ns, color=C[0], lw=2.2, label="E[1/R] = H_n/n (un seul pertinent)")
    ax.loglog(ns, np.log(ns + 1) / ns, color=C[1], lw=1.2, ls="--", label="ln(n + 1)/n")
    ax.loglog(ns, (1 + np.log(ns)) / ns, color=C[2], lw=1.2, ls="--", label="(1 + ln n)/n")
    for nn, txt in ((7, "n = 7 : 363/980"), (50, "n = 50 : ≈ 0,090")):
        v = sum(1 / j for j in range(1, nn + 1)) / nn
        ax.plot([nn], [v], "o", color="black", ms=5)
        ax.annotate(txt, (nn, v), textcoords="offset points", xytext=(8, 4), fontsize=9)
    ax.set(xlabel="n (échelle logarithmique)", ylabel="E[1/R] (échelle logarithmique)")
    ax.set_title("La ligne de base d'un ordre au hasard", fontsize=11)
    ax.legend(fontsize=8.5, loc="lower left")
    fig.tight_layout(w_pad=2.2)
    save(fig, "premier_pertinent.png")
    print(f"    H_7 = {hm:.4f}, ln 8 = {math.log(8):.4f}, 1 + ln 7 = {1 + math.log(7):.4f}")


def main() -> int:
    print(f"Figures MB4 → {OUT.relative_to(ROOT)}")
    wbplot.set_style()
    factorization()
    energy()
    rarity()
    saturation()
    fusion()
    first_relevant()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
