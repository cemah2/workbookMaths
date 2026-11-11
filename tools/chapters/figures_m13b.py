#!/usr/bin/env python
"""Draw the figures of chapter M13b (used by Claude).

    python tools/chapters/figures_m13b.py

Writes small PNG files into chapitres/m13b_lagrange_svm/figures/: the level lines of x² + 3y² and the constraint
x + y = 8, tangent at the point of Lagrange; an inequality constraint, active then inactive; a hard-margin SVM with its
band and its two support vectors; the 0-1 loss, the hinge loss and the log-loss as functions of the margin y s; the
objective of an SVM along a subgradient descent (not monotone); the RBF Gram matrix of six points for three values of
γ. The numbers are those of the fiche; none comes from workbookIA 13 (no six points of 13.4, no (x · z)², no RBF at
distance 1 for γ = 0,1, 1, 10, no ellipses tangent to a disc, no circles, no seed 13xx).
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m13b_lagrange_svm" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

POS = np.array([[6.0, 1.0], [7.0, 3.0], [8.0, 0.0]])          # §6: the positive examples
NEG = np.array([[3.0, 2.0], [1.0, 4.0], [0.0, 2.0]])          # §6: the negative examples
W_SVM, B_SVM = np.array([0.6, -0.2]), -2.4                    # §6: the hard-margin solution
GRAM_X = np.array([0.0, 0.5, 1.2, 2.0, 3.5, 4.0])             # §8: six points on a line
GAMMAS = (0.05, 1.0, 20.0)                                    # §8: three widths


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear":
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def lagrange_point() -> None:
    """§1: min x² + 3y² under x + y = 8: the level line f = 48 touches the constraint at (6, 2)."""
    xs, ys = np.linspace(-2, 11, 400), np.linspace(-4.5, 6, 400)
    X, Y = np.meshgrid(xs, ys)
    F = X ** 2 + 3 * Y ** 2
    fig, ax = plt.subplots(figsize=(6.2, 4.6))
    cs = ax.contour(X, Y, F, levels=[12, 27, 48, 75, 108], colors=["0.6"], linewidths=1)
    ax.clabel(cs, fmt=lambda v: f"f = {v:g}", fontsize=8)
    ax.contour(X, Y, F, levels=[48], colors=[C[0]], linewidths=2.2)
    ax.plot(xs, 8 - xs, color=C[1], lw=2, label="contrainte x + y = 8")
    ax.plot([6], [2], "ko", zorder=5)
    ax.annotate("(6, 2) : f = 48", (6, 2), xytext=(7.7, 4.6), fontsize=10, arrowprops={"arrowstyle": "-", "color": "0.3"})
    # both arrows are shortened (∇f is 12 times ∇g): only their common direction matters
    ax.annotate("", xy=(6 + 1.4, 2 + 1.4), xytext=(6, 2), arrowprops={"arrowstyle": "->", "color": C[0], "lw": 1.8})
    ax.text(7.55, 3.3, "∇f = (12, 12)", color=C[0], fontsize=10)
    ax.annotate("", xy=(6 + 0.8, 2 + 0.8), xytext=(6, 2), arrowprops={"arrowstyle": "->", "color": C[1], "lw": 1.8})
    ax.text(7.0, 2.2, "∇g = (1, 1)", color=C[1], fontsize=10)
    ax.set(xlim=(-2, 11), ylim=(-4.5, 6), xlabel="x", ylabel="y", aspect="equal",
           title="La ligne de niveau f = 48 touche la contrainte en (6, 2)")
    ax.legend(loc="lower left", fontsize=9)
    save(fig, "lagrange_lignes_niveau.png")


def kkt_cases() -> None:
    """§3: min ‖x − (6, 5)‖² under x + 3y ≤ c: active for c = 11 (solution (5, 2), μ = 2), inactive for c = 25."""
    xs = np.linspace(-1, 11, 300)
    X, Y = np.meshgrid(xs, np.linspace(-2, 9, 300))
    F = (X - 6) ** 2 + (Y - 5) ** 2
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
    for ax, c, sol, title in ((axes[0], 11, (5, 2), "x + 3y ≤ 11 : contrainte active, μ = 2"),
                              (axes[1], 25, (6, 5), "x + 3y ≤ 25 : contrainte inactive, μ = 0")):
        ax.contourf(X, Y, (X + 3 * Y <= c).astype(float), levels=[0.5, 1.5], colors=[C[1]], alpha=0.15)
        ax.contour(X, Y, F, levels=[1, 4, 10, 20, 35], colors=["0.6"], linewidths=1)
        ax.plot(xs, (c - xs) / 3, color=C[1], lw=2)
        ax.plot([6], [5], "x", color="0.2", ms=9, mew=2)
        ax.text(6.2, 5.3, "minimum libre (6, 5)", fontsize=9)
        ax.plot(*sol, "o", color=C[0], ms=8, zorder=5)
        if c == 11:
            # same scale for both arrows: ∇g = (1, 3) and ∇f = (−2, −6), drawn at half length
            ax.annotate("", xy=(5 + 0.5, 2 + 1.5), xytext=(5, 2), arrowprops={"arrowstyle": "->", "color": C[1]})
            ax.text(5.65, 3.2, "∇g = (1, 3)", color=C[1])
            ax.annotate("", xy=(5 - 1.0, 2 - 3.0), xytext=(5, 2), arrowprops={"arrowstyle": "->", "color": C[0]})
            ax.text(0.2, -1.4, "∇f = (−2, −6) = −2 ∇g", color=C[0])
        ax.set(xlim=(-1, 11), ylim=(-2, 9), aspect="equal", xlabel="x", ylabel="y", title=title)
    save(fig, "kkt_active_inactive.png")


def hard_margin() -> None:
    """§6: the hard-margin SVM of six points: w = (0,6 ; −0,2), b = −2,4, support vectors (6, 1) and (3, 2)."""
    fig, ax = plt.subplots(figsize=(6.2, 5.0))
    xs = np.linspace(-1, 9.5, 200)
    for level, style, label in ((0, "-", "frontière w · x + b = 0"), (1, "--", "bords w · x + b = ±1"),
                                (-1, "--", None)):
        ax.plot(xs, (W_SVM[0] * xs + B_SVM - level) / -W_SVM[1], style, color="0.25", lw=1.8 if level == 0 else 1,
                label=label)
    ax.fill_between(xs, (W_SVM[0] * xs + B_SVM - 1) / -W_SVM[1], (W_SVM[0] * xs + B_SVM + 1) / -W_SVM[1],
                    color="0.85", zorder=0)
    ax.scatter(*POS.T, s=60, color=C[0], label="label +1", zorder=3)
    ax.scatter(*NEG.T, s=60, color=C[1], marker="s", label="label −1", zorder=3)
    for p in ((6, 1), (3, 2)):
        ax.scatter(*p, s=260, facecolors="none", edgecolors="k", lw=1.5, zorder=4)
    ax.set(xlim=(-1, 9.5), ylim=(-1.5, 6), aspect="equal", xlabel="x₁", ylabel="x₂",
           title="Marge dure : ρ = 1/‖w‖ ≈ 1,58, bande de largeur 2ρ")
    ax.legend(loc="upper right", fontsize=8, framealpha=0.95)
    save(fig, "svm_marge_dure.png")


def losses() -> None:
    """§7: three losses of a margin t = y s: 0-1, hinge, log-loss in bits."""
    t = np.linspace(-2.5, 3, 500)
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    ax.plot(t, (t <= 0).astype(float), color="0.3", lw=2, label="loss 0-1 (erreur)")
    ax.plot(t, np.maximum(0, 1 - t), color=C[0], lw=2.2, label="hinge max(0, 1 − t)")
    ax.plot(t, np.log1p(np.exp(-t)) / np.log(2), color=C[1], lw=2, label="log-loss en bits log₂(1 + e⁻ᵗ)")
    ax.axvline(1, color="0.7", lw=0.8, ls=":")
    ax.text(1.05, 2.6, "t = 1", color="0.4", fontsize=9)
    ax.set(xlabel="marge fonctionnelle t = y (w · x + b)", ylabel="loss", ylim=(-0.1, 3.4),
           title="La hinge majore l'erreur et s'annule dès t ≥ 1")
    ax.legend(fontsize=9)
    save(fig, "pertes_hinge.png")


def subgradient_run() -> None:
    """§7: J − J* along a subgradient descent with steps 0,02/√t on 120 synthetic points: J is not monotone."""
    sys.path.insert(0, str(ROOT / "solutions"))
    from mymath_ref import svm  # noqa: E402
    from sklearn.svm import SVC  # noqa: E402

    rng = np.random.default_rng(4201)
    n = 120
    y = np.where(rng.random(n) < 0.5, 1, -1)
    X = np.where(y[:, None] == 1, [1.5, -0.5], [-1.0, 0.5]) + rng.normal(0, 1.1, (n, 2))
    C_ = 0.5
    best_model = SVC(kernel="linear", C=C_, tol=1e-12).fit(X, y)       # the same J, minimized by a QP solver
    J_star = svm.svm_subgradient(best_model.coef_[0], float(best_model.intercept_[0]), X, y, C_)[0]
    w, b = np.zeros(2), 0.0
    gaps = []
    for t in range(1, 201):
        J, g_w, g_b = svm.svm_subgradient(w, b, X, y, C_)
        gaps.append(J - J_star)
        w, b = w - 0.02 / np.sqrt(t) * g_w, b - 0.02 / np.sqrt(t) * g_b
    gaps = np.maximum(np.array(gaps), 1e-6)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.semilogy(range(1, 201), gaps, color=C[0], lw=1, label="J(w_t, b_t) − J*")
    ax.semilogy(range(1, 201), np.minimum.accumulate(gaps), color=C[1], lw=2, label="meilleur écart vu jusque-là")
    ax.set(xlabel="itération t", ylabel="écart à l'optimum (échelle log)",
           title="Descente de sous-gradient, pas 0,02/√t : J ne baisse pas à chaque pas")
    ax.legend(fontsize=9)
    save(fig, "sous_gradient.png")


def rbf_gram() -> None:
    """§8: the RBF Gram matrix of six points of a line, for γ = 0,05, 1 and 20."""
    D2 = (GRAM_X[:, None] - GRAM_X[None, :]) ** 2
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.7))
    for ax, gamma in zip(axes, GAMMAS):
        K = np.exp(-gamma * D2)
        im = ax.imshow(K, vmin=0, vmax=1, cmap="viridis")
        for i in range(6):
            for j in range(6):
                ax.text(j, i, f"{K[i, j]:.2f}".replace(".", ","), ha="center", va="center", fontsize=7,
                        color="white" if K[i, j] < 0.55 else "black")
        ax.set_xticks(range(6), [french_number(v) for v in GRAM_X], fontsize=8)
        ax.set_yticks(range(6), [french_number(v) for v in GRAM_X], fontsize=8)
        ax.set_title(f"γ = {french_number(gamma)}")
    fig.colorbar(im, ax=axes, shrink=0.8)
    fig.suptitle("La matrice de Gram RBF de six points : presque des 1 pour γ petit, presque l'identité pour γ grand",
                 fontsize=10)
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "gram_rbf.png", dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("  gram_rbf.png")


def main() -> int:
    print(f"figures of M13b -> {OUT.relative_to(ROOT)}")
    lagrange_point()
    kkt_cases()
    hard_margin()
    losses()
    subgradient_run()
    rbf_gram()
    return 0


if __name__ == "__main__":
    sys.exit(main())
