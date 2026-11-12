#!/usr/bin/env python
"""Draw the figures of chapter M21 (used by Claude).

    python tools/chapters/figures_m21.py

Writes small PNG files into chapitres/m21_convolution/figures/: the sliding sum of the libraries and the convolution
(flipped kernel) of x = (2, 5, −1, 3, 0, 4) by w = (3, 1, −2); the Toeplitz matrix of the full convolution by
w = (3, −1, 2) for n = 6, next to the circulant matrix of the same kernel; translation equivariance of the stencil
(1, −2, 1) on a pulse, with a step of 1 and of 2; the windows of a sliding sum on 11 cells for four settings of step,
dilation and padding; the stamps of a transposed convolution, y = (2, −1, 3), w = (1, 3, 3, 1), step 3, and its
overlaps for (k, s) = (4, 3) and (6, 3); the receptive field of a stack of three sliding sums, (k, s, d) = (4, 2, 1),
(3, 2, 1), (3, 1, 2). The numbers are those of the fiche; none comes from workbookIA 21 (no image, no network, no
layer, no 21xx seed). No randomness.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.colors import TwoSlopeNorm  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m21_convolution" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

X_SIG = [2, 5, -1, 3, 0, 4]          # §2: the signal
W_SIG = [3, 1, -2]                   # §2: the kernel
W_TOE = [3, -1, 2]                   # §3: the kernel of the Toeplitz matrix
PULSE = [0, 0, 3, 1, 0, 0, 0, 0]     # §4: a pulse
STENCIL = [1, -2, 1]                 # §4: the second difference stencil (symmetric)
STACK = [(4, 2, 1), (3, 2, 1), (3, 1, 2)]   # §7: (k, s, d) of each stage


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def signed(v: float) -> str:
    return french_number(v)


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and ax.axison:
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def cell(ax, x0, y0, text, fc="white", ec="0.3", alpha=1.0, fontsize=11, ls="-", color="black", width=1.0):
    ax.add_patch(Rectangle((x0, y0), width, 0.8, fc=fc, ec=ec, alpha=alpha, ls=ls, lw=1.0))
    ax.text(x0 + width / 2, y0 + 0.4, text, ha="center", va="center", fontsize=fontsize, color=color)


def corr_valid(w, x, s=1, d=1):
    w, x = np.asarray(w, float), np.asarray(x, float)
    k = len(w)
    out, i = [], 0
    while s * i + d * (k - 1) <= len(x) - 1:
        out.append(float(sum(w[u] * x[s * i + d * u] for u in range(k))))
        i += 1
    return np.array(out)


# --------------------------------------------------------------------------------------------------------- §2
def sliding() -> None:
    """§2: the library sliding sum at i = 1 (kernel as is) and the convolution at m = 3 (kernel flipped)."""
    x, w = X_SIG, W_SIG
    corr = corr_valid(w, x)
    conv = np.convolve(x, w, "valid")
    fig, axes = plt.subplots(2, 1, figsize=(10.0, 6.4))
    panels = [
        (axes[0], w, 1, corr, "corrélation croisée (bibliothèques) : w ⋆ x, noyau tel quel",
         "w = (3, 1, −2)", "(w ⋆ x)₁ = 3·5 + 1·(−1) + (−2)·3 = 8", C[0]),
        (axes[1], w[::-1], 1, conv, "convolution (mathématiciens, np.convolve) : x * w, noyau retourné",
         "w̃ = (−2, 1, 3)", "(x * w)₃ = (−2)·5 + 1·(−1) + 3·3 = −2", C[1]),
    ]
    for ax, kern, start, out, title, kname, formula, color in panels:
        ax.set_axis_off()
        ax.set(xlim=(-2.6, 7.2), ylim=(-0.4, 3.9))
        ax.text(-2.5, 3.5, title, fontsize=11.5, color=color, fontweight="bold")
        ax.text(-2.5, 2.5, "signal x", fontsize=10, va="center")
        for i, v in enumerate(x):
            hl = start <= i < start + 3
            cell(ax, i, 2.1, signed(v), fc=color if hl else "white", alpha=0.25 if hl else 1.0)
            ax.text(i + 0.5, 3.0, f"{i}", ha="center", fontsize=8.5, color="0.4")
        ax.text(-2.5, 1.4, kname, fontsize=10, va="center")
        for u, v in enumerate(kern):
            cell(ax, start + u, 1.0, signed(v), fc=color, alpha=0.45)
        ax.text(-2.5, 0.3, "sortie valide", fontsize=10, va="center")
        for i, v in enumerate(out):
            hl = i == start
            cell(ax, i + 1, -0.1, french_number(round(v)), fc=color if hl else "white", alpha=0.45 if hl else 1.0)
        ax.text(6.2, 1.4, formula, fontsize=10, va="center", ha="left", color=color)
        ax.annotate("", xy=(start + 1 + 0.5, 0.72), xytext=(start + 1.5, 1.0),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4))
    fig.suptitle("Glisser, multiplier, sommer : la même fenêtre, le noyau lu dans un sens ou dans l'autre",
                 fontsize=11.5, y=0.99)
    save(fig, "glisser_retourner.png")


# --------------------------------------------------------------------------------------------------------- §3, §4
def toeplitz_circulant() -> None:
    """§3-§4: the full Toeplitz matrix of x ↦ x * w for n = 6, and the circulant matrix of the same kernel."""
    w = np.array(W_TOE, float)
    n, k = 6, len(w)
    T = np.zeros((n + k - 1, n))
    for j in range(n):
        T[j:j + k, j] = w
    h = np.concatenate([w, np.zeros(n - k)])
    Cm = np.array([[h[(i - j) % n] for j in range(n)] for i in range(n)])
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.6), gridspec_kw={"width_ratios": [1, 1]})
    norm = TwoSlopeNorm(vmin=-3.2, vcenter=0.0, vmax=3.2)
    cmap = wbplot.diverging_cmap()
    for ax, M, title in ((axes[0], T, "Toeplitz : x ↦ x * w en mode plein\nforme (8, 6), 18 coefficients non nuls"),
                         (axes[1], Cm, "circulante : x ↦ x ⊛ h, h = (3, −1, 2, 0, 0, 0)\n"
                                       "forme (6, 6) : ce qui sortait en bas revient en haut")):
        ax.imshow(M, cmap=cmap, norm=norm)
        for (i, j), v in np.ndenumerate(M):
            ax.text(j, i, french_number(v), ha="center", va="center", fontsize=10,
                    color="white" if abs(v) >= 2.5 else ("black" if v != 0 else "0.75"))
        ax.set_xticks(range(M.shape[1]))
        ax.set_yticks(range(M.shape[0]))
        ax.set(xlabel="colonne j", ylabel="ligne i")
        ax.set_title(title, fontsize=10.5)
    # the rows kept by the valid mode
    axes[0].add_patch(Rectangle((-0.5, 1.5), n, 4, fill=False, ec=C[3], lw=2.4, ls="--"))
    axes[0].text(n - 0.4, 3.5, "lignes 2 à 5 :\nmode valide", color=C[3], fontsize=9.5, va="center")
    for i in range(n):
        for j in range(n):
            if (i - j) % n in (1, 2) and i < j:
                axes[1].add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, ec=C[3], lw=2.0))
    fig.suptitle("Chaque diagonale est constante : le coefficient (i, j) ne dépend que de i − j "
                 "(modulo n pour la circulante)", fontsize=11, y=1.0)
    fig.subplots_adjust(wspace=0.45)
    save(fig, "toeplitz_circulante.png")


def equivariance() -> None:
    """§4: shift the pulse, filter it: the output shifts too (step 1); with a step of 2, only even shifts do."""
    x = np.array(PULSE, float)
    x2 = np.roll(x, 2)
    x1 = np.roll(x, 1)
    fig, axes = plt.subplots(1, 3, figsize=(14.0, 4.1))
    idx = np.arange(len(x))
    axes[0].stem(idx - 0.08, x, linefmt=C[0], markerfmt="o", basefmt=" ", label="x")
    axes[0].stem(idx + 0.08, x2, linefmt=C[1], markerfmt="s", basefmt=" ", label="x décalé de 2")
    axes[0].set(title="deux signaux : x et x décalé de 2 cases", xlabel="indice")
    y, y2 = corr_valid(STENCIL, x), corr_valid(STENCIL, x2)
    j = np.arange(len(y))
    axes[1].stem(j - 0.08, y, linefmt=C[0], markerfmt="o", basefmt=" ", label="pochoir appliqué à x")
    axes[1].stem(j + 0.08, y2, linefmt=C[1], markerfmt="s", basefmt=" ", label="pochoir appliqué à x décalé")
    axes[1].set(title="pas 1 : la sortie est décalée de 2 aussi\n(1, −2, 1) ⋆ x, mode valide", xlabel="indice")
    for (s_, sig, lab, col, mk, off) in ((0, x, "x", C[0], "o", -0.15), (1, x1, "x décalé de 1", C[2], "^", 0.0),
                                         (2, x2, "x décalé de 2", C[1], "s", 0.15)):
        out = corr_valid(STENCIL, sig, s=2)
        jj = np.arange(len(out))
        axes[2].stem(jj + off, out, linefmt=col, markerfmt=mk, basefmt=" ", label=f"{lab} : {tuple(int(v) for v in out)}"
                     .replace("-", "−"))
    axes[2].set(title="pas 2 : décaler de 2 décale la sortie de 1 ;\ndécaler de 1 donne une autre sortie",
                xlabel="indice de sortie")
    axes[0].set(ylim=(-0.3, 4.4), xticks=range(len(x)))
    axes[1].set(ylim=(-6.0, 5.6), xticks=range(len(y)))
    axes[2].set(ylim=(-6.0, 5.6), xticks=range(3))
    for ax in axes:
        ax.axhline(0, color="0.6", lw=0.8)
        ax.grid(alpha=0.25)
        ax.legend(fontsize=8.5, loc="upper right")
    save(fig, "equivariance.png")


# --------------------------------------------------------------------------------------------------------- §5
def windows() -> None:
    """§5: the windows of a sliding sum of width k = 3 on n = 11 cells, for four (s, d, p)."""
    n, k = 11, 3
    settings = [(1, 1, 0), (2, 1, 0), (1, 2, 0), (2, 1, 1)]
    fig, axes = plt.subplots(len(settings), 1, figsize=(11.0, 7.4))
    for ax, (s, d, p) in zip(axes, settings):
        ax.set_axis_off()
        ax.set(xlim=(-4.8, n + 3.2), ylim=(-1.3, 1.25))
        total = n + 2 * p
        count = (total - d * (k - 1) - 1) // s + 1
        for c in range(total):
            pad = c < p or c >= p + n
            cell(ax, c - p, 0.0, "0" if pad else f"{c - p}", fc="0.92" if pad else "white", ls="--" if pad else "-",
                 fontsize=9, color="0.5" if pad else "black")
        colors = [C[0], C[1], C[2]]
        for i in range(min(count, 3)):
            cells = [s * i + d * u - p for u in range(k)]
            col = colors[i]
            y = -0.35 - 0.3 * i
            ax.plot([cells[0] + 0.5, cells[-1] + 0.5], [y, y], color=col, lw=1.2)
            for c in cells:
                ax.plot(c + 0.5, y, "o", color=col, ms=6)
                ax.add_patch(Rectangle((c, 0.0), 1, 0.8, fc=col, alpha=0.22, ec="none"))
            ax.text(cells[-1] + 0.8, y, f"fenêtre {i}", fontsize=8, color=col, va="center")
        label = f"s = {s}, d = {d}, p = {p}"
        ax.text(-4.7, 0.4, label, fontsize=10.5, va="center")
        ax.text(n + 0.6 + p, 0.4, f"{count} positions", fontsize=10.5, va="center", fontweight="bold")
    fig.suptitle("Une fenêtre de k = 3 poids sur n = 11 cases : ⌊(n + 2p − d(k − 1) − 1)/s⌋ + 1 positions "
                 "(les trois premières sont dessinées)", fontsize=11, y=0.99)
    save(fig, "pas_dilatation_padding.png")


def transposed() -> None:
    """§5: the stamps of a transposed convolution and the overlaps, for (k, s) = (4, 3) and (6, 3)."""
    y = np.array([2.0, -1.0, 3.0])
    w = np.array([1.0, 3.0, 3.0, 1.0])
    s = 3
    m, k = len(y), len(w)
    length = (m - 1) * s + k
    fig, axes = plt.subplots(3, 1, figsize=(10.5, 8.6), gridspec_kw={"height_ratios": [1.5, 0.75, 0.75]})
    ax = axes[0]
    total = np.zeros(length)
    for i, v in enumerate(y):
        stamp = np.zeros(length)
        stamp[s * i:s * i + k] = v * w
        total += stamp
        ax.bar(np.arange(length) + (i - 1) * 0.22, stamp, width=0.22, color=C[i],
               label=f"y{'₀₁₂'[i]} = {french_number(v)} : tampon {french_number(v)} × w posé en {s * i}")
    ax.plot(np.arange(length), total, "kD", ms=6, label="somme : (2, 6, 6, 1, −3, −3, 2, 9, 9, 3)")
    ax.axhline(0, color="0.6", lw=0.8)
    ax.set_xticks(range(length))
    ax.set(xlabel="indice de sortie", title="convolution transposée : y = (2, −1, 3), w = (1, 3, 3, 1), pas 3 "
           "→ (3 − 1) × 3 + 4 = 10 valeurs")
    ax.set_ylim(-4.2, 15.5)
    ax.legend(fontsize=8.5, loc="upper left", ncol=2)
    ax.grid(alpha=0.25)
    for ax, kk in ((axes[1], 4), (axes[2], 6)):
        ln = (m - 1) * s + kk
        cover = np.zeros(ln, int)
        for i in range(m):
            cover[s * i:s * i + kk] += 1
        ax.set_axis_off()
        ax.set(xlim=(-3.4, 13.4), ylim=(-0.4, 1.3))
        for c, v in enumerate(cover):
            cell(ax, c, 0.0, str(v), fc=C[0], alpha=0.12 + 0.28 * (v - 1), fontsize=10)
        verdict = "s ne divise pas k : 1 ou 2 tampons selon la case (en 2D, un damier)" if kk % s else \
            "s divise k : 2 tampons sur chaque case intérieure"
        ax.text(-3.3, 0.4, f"k = {kk}, s = {s}", fontsize=10.5, va="center")
        ax.text(-0.0, 1.05, f"nombre de tampons qui couvrent chaque case ; {verdict}", fontsize=9.5)
    save(fig, "convolution_transposee.png")


# --------------------------------------------------------------------------------------------------------- §7
def receptive_field() -> None:
    """§7: the cells of x that output z[0] of a stack of three sliding sums depends on. Each cell of a stage is
    drawn above the middle of its own receptive field, as wide as the step it advances by."""
    n = 36
    lengths, jumps, fields = [n], [1], [1]
    for k, s, d in STACK:
        lengths.append((lengths[-1] - d * (k - 1) - 1) // s + 1)
        fields.append(fields[-1] + d * (k - 1) * jumps[-1])
        jumps.append(jumps[-1] * s)

    def field(j):
        """The cells read, stage by stage, by output j of the last stage (index 0: the cells of x)."""
        sets = [{j}]
        for k, s, d in reversed(STACK):
            sets.append({s * i + d * u for i in sets[-1] for u in range(k)})
        return sets[::-1]

    f0, f1 = field(0), field(1)
    width = 0.34
    rows_y = [0, 1.6, 3.2, 4.8]
    names = ["x (36 cases)", "étage 1 : k = 4, s = 2", "étage 2 : k = 3, s = 2", "étage 3 : k = 3, s = 1, d = 2"]

    def centre(r, i):
        return (jumps[r] * i + (fields[r] - 1) / 2 + 0.5) * width

    fig, ax = plt.subplots(figsize=(13.0, 5.2))
    ax.set_axis_off()
    for r, (ln, yy) in enumerate(zip(lengths, rows_y)):
        box = width * min(jumps[r], 4) * 0.9 if r else width * 0.9
        for c in range(ln):
            used0 = c in f0[r]
            used1 = c in f1[r] and not used0
            fc = C[1] if used0 else (C[0] if used1 else "white")
            ax.add_patch(Rectangle((centre(r, c) - box / 2, yy), box, 0.6, fc=fc,
                                   alpha=0.55 if (used0 or used1) else 1, ec="0.4", lw=0.6))
        ax.text(-0.25, yy + 0.3, names[r], ha="right", va="center", fontsize=9.5)
    for r, (k, s, d) in enumerate(STACK):
        for i in f0[r + 1]:
            for u in range(k):
                src = s * i + d * u
                ax.plot([centre(r + 1, i), centre(r, src)], [rows_y[r + 1], rows_y[r] + 0.6],
                        color=C[1], lw=0.7, alpha=0.7)
    lo, hi = min(f0[0]), max(f0[0])
    ax.annotate("", xy=(lo * width, -0.35), xytext=((hi + 1) * width, -0.35),
                arrowprops=dict(arrowstyle="<->", color=C[1], lw=1.5))
    ax.text((lo + hi + 1) * width / 2, -0.75, "champ récepteur de z₀ : 24 cases (0 à 23)", ha="center",
            color=C[1], fontsize=10)
    ax.text(n * width + 0.3, 0.3, "en bleu : les cases lues\npar z₁ et pas par z₀\n(z₁ lit les cases 4 à 27 :\n"
            "le pas total vaut S = 4)", color=C[0], fontsize=9, va="center")
    ax.set(xlim=(-4.2, n * width + 3.4), ylim=(-1.1, 5.6))
    ax.set_title("Une pile de trois sommes glissantes : le champ récepteur passe de 1 à 4, 8 puis 24 cases",
                 fontsize=11)
    save(fig, "champ_recepteur.png")


def main() -> int:
    print(f"Figures M21 → {OUT.relative_to(ROOT)}")
    sliding()
    toeplitz_circulant()
    equivariance()
    windows()
    transposed()
    receptive_field()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
