#!/usr/bin/env python
"""Draw the figures of chapter M12c (used by Claude).

    python tools/chapters/figures_m12c.py

Writes small PNG files into chapitres/m12c_valeurs_propres/figures/: the unit square and its image by matrices of
determinant −4 and 0, the vectors that a matrix only stretches, the power iteration and its speed, the image of the
unit circle by a symmetric matrix, the level curves of three quadratic forms, and a cloud whitened in two ways. The
matrices are those of the fiche: A = [[1, 2], [3, 2]] (§1, §3 to §5), S = [[2, 3], [3, 10]] (§6, §7) and
Σ = [[4, 6], [6, 13]] (§8). None comes from workbookIA 12 (no projection of a cloud on an axis, no principal component,
no correlation matrix [[1, r], [r, 1]]).
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Polygon  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m12c_valeurs_propres" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

A = np.array([[1.0, 2.0], [3.0, 2.0]])          # eigenvalues 4 and −1, eigenvectors (2, 3) and (1, −1)
S = np.array([[2.0, 3.0], [3.0, 10.0]])         # eigenvalues 11 and 1, eigenvectors (1, 3) and (3, −1)
SIGMA = np.array([[4.0, 6.0], [6.0, 13.0]])     # eigenvalues 16 and 1, eigenvectors (1, 2) and (2, −1)
THETA = np.linspace(0, 2 * np.pi, 400)
CIRCLE = np.column_stack([np.cos(THETA), np.sin(THETA)])


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


def arrow(ax, start, vector, color, label="", offset=(0.1, 0.1), lw=2.2, ls="-"):
    ax.annotate("", xy=(start[0] + vector[0], start[1] + vector[1]), xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": lw, "mutation_scale": 14, "ls": ls})
    if label:
        ax.text(start[0] + vector[0] + offset[0], start[1] + vector[1] + offset[1], label, color=color, fontsize=11)


def axes_frame(ax, xlim, ylim=None):
    ylim = ylim or xlim
    ax.axhline(0, color="0.6", lw=0.8)
    ax.axvline(0, color="0.6", lw=0.8)
    ax.set(xlim=xlim, ylim=ylim, aspect="equal")


def determinant() -> None:
    """The unit square, its image by A (det −4: area 4, orientation reversed), and by a singular matrix (det 0)."""
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)
    fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.6))
    ax = axes[0]
    axes_frame(ax, (-0.6, 1.8))
    ax.add_patch(Polygon(square, closed=True, color=C[0], alpha=0.25))
    arrow(ax, (0, 0), (1, 0), C[1], "e₁", (-0.1, -0.25))
    arrow(ax, (0, 0), (0, 1), C[2], "e₂", (-0.3, -0.1))
    ax.set_title("Le carré unité : aire 1\n(de e₁ vers e₂ : sens direct)")
    ax = axes[1]
    image = square @ A.T
    axes_frame(ax, (-1, 5.5), (-1, 6))
    ax.add_patch(Polygon(image, closed=True, color=C[0], alpha=0.25))
    arrow(ax, (0, 0), A[:, 0], C[1], "A e₁ = (1, 3)", (-1.6, 0.15))
    arrow(ax, (0, 0), A[:, 1], C[2], "A e₂ = (2, 2)", (0.15, -0.35))
    ax.set_title("Son image par A = [[1, 2], [3, 2]] : aire 4,\nde A e₁ vers A e₂ : sens indirect, det A = −4")
    ax = axes[2]
    singular = np.array([[3.0, 6.0], [1.0, 2.0]])
    image = square @ singular.T
    axes_frame(ax, (-1, 10), (-1, 4))
    ax.plot(image[[0, 2], 0], image[[0, 2], 1], color=C[0], lw=5, alpha=0.4, solid_capstyle="butt")
    arrow(ax, (0, 0), singular[:, 0], C[1], "(3, 1)", (-0.6, 0.3))
    arrow(ax, (0, 0), singular[:, 1], C[2], "(6, 2)", (-0.4, 0.35), lw=1.6, ls="--")
    ax.set_title("Par [[3, 6], [1, 2]] : colonnes colinéaires,\nle carré s'aplatit sur un segment : det = 0")
    save(fig, "determinant.png")


def eigenvectors() -> None:
    """Left: x on the unit circle and A x. Right: the two eigen-directions, only stretched (by 4 and by −1)."""
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.4))
    ax = axes[0]
    axes_frame(ax, (-4.2, 4.2))
    ax.plot(CIRCLE[:, 0], CIRCLE[:, 1], color="0.5", lw=1.2)
    image = CIRCLE @ A.T
    ax.plot(image[:, 0], image[:, 1], color=C[0], lw=1.6)
    for t in np.linspace(0, 2 * np.pi, 13)[:-1]:
        x = np.array([np.cos(t), np.sin(t)])
        ax.plot(*x, "o", color="0.4", ms=3.5)
        ax.annotate("", xy=A @ x, xytext=x, arrowprops={"arrowstyle": "-|>", "color": C[3], "lw": 0.9, "alpha": 0.7})
    ax.set_title("Chaque point x du cercle unité est envoyé sur A x :\nen général, A x n'est pas sur la droite de x")
    ax = axes[1]
    axes_frame(ax, (-4.2, 4.2))
    v1, v2 = np.array([2.0, 3.0]) / np.sqrt(13), np.array([1.0, -1.0]) / np.sqrt(2)
    for v, color in ((v1, C[1]), (v2, C[2])):
        ax.plot([-6 * v[0], 6 * v[0]], [-6 * v[1], 6 * v[1]], color=color, lw=0.8, ls=":")
    arrow(ax, (0, 0), 4 * v1, C[1], "A v₁ = 4 v₁", (0.1, 0.0), lw=1.4)
    arrow(ax, (0, 0), v1, C[1], "v₁", (0.15, -0.3), lw=3)
    arrow(ax, (0, 0), v2, C[2], "v₂", (0.1, 0.05), lw=3)
    arrow(ax, (0, 0), -v2, C[2], "A v₂ = −v₂", (-1.9, 0.15), lw=1.4, ls="--")
    ax.set_title("Les vecteurs propres restent sur leur droite :\nv₁ ∝ (2, 3) est étiré par 4, v₂ ∝ (1, −1) retourné (−1)")
    save(fig, "vecteurs_propres.png")


def power_iteration() -> None:
    """Left: the iterates of the power method on A from (1, 0). Right: the distance to v₁, against k, for |λ₂/λ₁| =
    1/4 (A) and 0.9 (a diagonal matrix), on a logarithmic scale."""
    v1 = np.array([2.0, 3.0]) / np.sqrt(13)
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.9))
    ax = axes[0]
    axes_frame(ax, (-0.3, 1.2))
    ax.plot(CIRCLE[:, 0], CIRCLE[:, 1], color="0.6", lw=1)
    x = np.array([1.0, 0.0])
    for k in range(5):
        ax.annotate("", xy=x, xytext=(0, 0),
                    arrowprops={"arrowstyle": "-|>", "color": C[0], "lw": 1.6, "alpha": 0.35 + 0.15 * k})
        if k < 3:
            ax.text(x[0] + (0.05 if k != 1 else -0.12), x[1] + (0.03 if k != 2 else -0.08), f"x{'₀₁₂'[k]}",
                    color=C[0], fontsize=11)
        y = A @ x
        x = y / np.linalg.norm(y)
        x = -x if x[np.argmax(np.abs(x))] < 0 else x
    ax.plot([0, 1.15 * v1[0]], [0, 1.15 * v1[1]], color=C[1], lw=1.2, ls="--", label="la direction de v₁ ∝ (2, 3)")
    ax.legend(loc="lower left", fontsize=9)
    ax.set_title("x ← A x / ‖A x‖, depuis x₀ = (1, 0) :\nles itérés se rapprochent de la direction de v₁")
    ax = axes[1]
    ks = np.arange(0, 41)
    for M, start, ratio, color, label in (
            (A, np.array([1.0, 0.0]), 0.25, C[0], "A : |λ₂ / λ₁| = 1/4"),
            (np.diag([1.0, 0.9]), np.array([1.0, 1.0]) / np.sqrt(2), 0.9, C[2], "diag(1 ; 0,9) : |λ₂ / λ₁| = 0,9")):
        target = v1 if M is A else np.array([1.0, 0.0])
        x, errors = start.copy(), []
        for _ in ks:
            errors.append(np.linalg.norm(x - target))
            y = M @ x
            x = y / np.linalg.norm(y)
            x = -x if x[np.argmax(np.abs(x))] < 0 else x
        ax.semilogy(ks, np.maximum(errors, 1e-17), "o-", ms=3, color=color, label=label)
        ax.semilogy(ks, errors[0] * ratio ** ks, ls=":", color=color, lw=1)
    ax.set(xlabel="itération k", ylabel="‖xₖ − v₁‖ (échelle logarithmique)", ylim=(1e-16, 3))
    ax.legend(fontsize=9, loc="lower left")
    ax.set_title("L'écart à v₁ est multiplié par environ |λ₂ / λ₁| à chaque pas\n(en pointillés : la droite de pente |λ₂ / λ₁|ᵏ)")
    save(fig, "puissance.png")


def spectral() -> None:
    """The unit circle and its image by S: an ellipse whose axes are the orthonormal eigenvectors of S."""
    q1, q2 = np.array([1.0, 3.0]) / np.sqrt(10), np.array([3.0, -1.0]) / np.sqrt(10)
    fig, ax = plt.subplots(figsize=(6.4, 6.4))
    axes_frame(ax, (-6.5, 6.5), (-11.5, 11.5))
    ax.plot(CIRCLE[:, 0], CIRCLE[:, 1], color="0.5", lw=1.2, label="le cercle unité")
    image = CIRCLE @ S.T
    ax.plot(image[:, 0], image[:, 1], color=C[0], lw=2, label="son image par S")
    arrow(ax, (0, 0), 11 * q1, C[1], "S q₁ = 11 q₁", (0.2, -0.6), lw=1.6)
    arrow(ax, (0, 0), q1, C[1], "q₁", (0.2, -0.3), lw=3)
    arrow(ax, (0, 0), q2, C[2], "q₂ = S q₂", (0.1, -0.9), lw=3)
    ax.legend(loc="lower right", fontsize=9)
    ax.set_title("S = [[2, 3], [3, 10]] étire le cercle en une ellipse :\n"
                 "axes le long de q₁ ∝ (1, 3) et q₂ ∝ (3, −1), orthogonaux,\ndemi-axes 11 et 1, les valeurs propres")
    save(fig, "spectral.png")


def quadratic_forms() -> None:
    """Level curves of xᵀMx for a positive definite, a positive semi-definite and an indefinite M."""
    grid = np.linspace(-2.2, 2.2, 301)
    X, Y = np.meshgrid(grid, grid)
    cases = [(S, "définie positive : S = [[2, 3], [3, 10]]\nλ = 11 et 1 : des ellipses", [0.5, 1, 2, 4, 8]),
             (np.array([[1.0, -2.0], [-2.0, 4.0]]), "semi-définie positive : (x − 2y)²\nλ = 5 et 0 : des droites",
              [0.5, 1, 2, 4, 8]),
             (np.array([[1.0, 0.0], [0.0, -2.0]]), "indéfinie : x² − 2y²\nλ = 1 et −2 : des hyperboles",
              [-4, -2, -1, -0.5, 0.5, 1, 2, 4])]
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.7))
    for ax, (M, title, levels) in zip(axes, cases):
        Q = M[0, 0] * X ** 2 + 2 * M[0, 1] * X * Y + M[1, 1] * Y ** 2
        cs = ax.contour(X, Y, Q, levels=levels, cmap="viridis")
        ax.clabel(cs, fmt=lambda v: french_number(v), fontsize=8)
        axes_frame(ax, (-2.2, 2.2))
        ax.set_title(title)
    save(fig, "formes_quadratiques.png")


def whitening() -> None:
    """A cloud of covariance Σ, then whitened by Σ^(-1/2) (ZCA) and by L⁻¹ (Cholesky): three points are followed."""
    rng = np.random.default_rng(1208)
    L = np.linalg.cholesky(SIGMA)
    X = rng.normal(size=(400, 2)) @ L.T
    values, Q = np.linalg.eigh(SIGMA)
    W_zca = Q @ np.diag(1 / np.sqrt(values)) @ Q.T
    W_chol = np.linalg.inv(L)
    marked = np.array([[3.0, 7.0], [-2.0, -1.0], [1.0, -2.0]])
    ellipse = CIRCLE @ L.T * 2                              # {x : xᵀ Σ⁻¹ x = 4}
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.9))
    panels = [(np.eye(2), "Le nuage, de covariance Σ = [[4, 6], [6, 13]]\net l'ellipse xᵀΣ⁻¹x = 4", (-8, 8), (-12, 12)),
              (W_zca, "Blanchi par W = Σ^(−1/2) (ZCA) :\ncovariance I, par des étirements seulement", (-4.5, 4.5),
               (-4.5, 4.5)),
              (W_chol, "Blanchi par W = L⁻¹ (Cholesky) :\ncovariance I aussi, suivie d'une rotation", (-4.5, 4.5),
               (-4.5, 4.5))]
    for ax, (W, title, xlim, ylim) in zip(axes, panels):
        Z = X @ W.T
        ax.scatter(Z[:, 0], Z[:, 1], s=6, color="0.55", alpha=0.6)
        ax.plot(*(ellipse @ W.T).T, color=C[0], lw=1.8)
        for point, color in zip(marked, (C[1], C[2], C[3])):
            ax.plot(*(W @ point), "o", color=color, ms=8, mec="black")
        axes_frame(ax, xlim, ylim)
        ax.set_title(title, fontsize=10)
    save(fig, "blanchiment.png")


def main() -> int:
    print(f"figures of M12c -> {OUT.relative_to(ROOT)}")
    determinant()
    eigenvectors()
    power_iteration()
    spectral()
    quadratic_forms()
    whitening()
    return 0


if __name__ == "__main__":
    sys.exit(main())
