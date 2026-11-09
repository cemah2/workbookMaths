#!/usr/bin/env python
"""Draw the figures of chapter M12d (used by Claude).

    python tools/chapters/figures_m12d.py

Writes small PNG files into chapitres/m12d_svd_acp/figures/: the unit circle through Vᵀ, S and U, a synthetic image
and its low-rank approximations, two linear systems (well and badly conditioned), a cloud of ℝ³ with its principal
axes and its scores, the cumulative explained variance and the reconstruction error of a synthetic dataset, and the
neighbourhood probabilities of t-SNE. The matrices are those of the fiche: A = [[6, 4], [1, −6]] (§1 to §3),
M = [[10, 7], [7, 5]] (§4) and C = [[11, 6, 0], [6, 6, 0], [0, 0, 8]] (§5 to §7). None comes from workbookIA 12 (no
standardized 2-D cloud projected on an axis, no digits, no « 10 features, 3 directions and noise »).
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

OUT = ROOT / "chapitres" / "m12d_svd_acp" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

A = np.array([[6.0, 4.0], [1.0, -6.0]])                       # s = 8 and 5
V = np.array([[2.0, 3.0], [3.0, -2.0]]) / np.sqrt(13)          # columns v₁ = (2, 3)/√13, v₂ = (3, −2)/√13
U = np.array([[3.0, 2.0], [-2.0, 3.0]]) / np.sqrt(13)          # columns u₁ = (3, −2)/√13, u₂ = (2, 3)/√13
S = np.diag([8.0, 5.0])
M = np.array([[10.0, 7.0], [7.0, 5.0]])                       # κ ≈ 223
COV = np.array([[11.0, 6.0, 0.0], [6.0, 6.0, 0.0], [0.0, 0.0, 8.0]])   # variances 15, 8 and 2
THETA = np.linspace(0, 2 * np.pi, 361)
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


def svd_geometry() -> None:
    """The unit circle, then Vᵀ (a reflection here), S (the stretch) and U (a rotation): the ellipse A·circle."""
    assert np.allclose(U @ S @ V.T, A)
    colors = plt.cm.twilight(np.linspace(0, 1, len(THETA)))
    stages = [(np.eye(2), "Le cercle unité, avec v₁ et v₂"),
              (V.T, "Après Vᵀ : v₁ → e₁, v₂ → e₂\n(det V = −1 : une symétrie)"),
              (S @ V.T, "Après S = diag(8, 5) :\nétirement le long des axes"),
              (A, "Après U (une rotation) :\nl'ellipse A · cercle, demi-axes 8 u₁ et 5 u₂")]
    fig, axes = plt.subplots(1, 4, figsize=(17, 4.6))
    for i, (ax, (T, title)) in enumerate(zip(axes, stages)):
        points = CIRCLE @ T.T
        ax.scatter(points[:, 0], points[:, 1], c=colors, s=6)
        lim = 1.6 if i < 2 else 9
        axes_frame(ax, (-lim, lim))
        first, second = T @ V[:, 0], T @ V[:, 1]
        o = 0.06 * lim
        arrow(ax, (0, 0), first, C[1], ["v₁", "e₁", "8 e₁", "8 u₁"][i], (o, o))
        arrow(ax, (0, 0), second, C[2], ["v₂", "e₂", "5 e₂", "5 u₂"][i], (o, -3 * o))
        ax.set_title(title, fontsize=10)
    save(fig, "svd_geometrie.png")


def synthetic_image(h=120, w=160) -> np.ndarray:
    """A grey-level picture made of smooth shapes, slanted stripes and a texture (values in [0, 1]): no file, no licence."""
    y, x = np.mgrid[0:h, 0:w] / np.array([h, w])[:, None, None]
    rng = np.random.default_rng(1262)
    image = 0.3 + 0.25 * x + 0.1 * y
    image += 0.4 * (((x - 0.28) / 0.17) ** 2 + ((y - 0.45) / 0.24) ** 2 < 1)                     # a disc
    u, v = (x - 0.72) * 0.8 + (y - 0.68) * 0.6, -(x - 0.72) * 0.6 + (y - 0.68) * 0.8
    image -= 0.35 * ((np.abs(u) < 0.11) & (np.abs(v) < 0.09))                                        # a slanted square
    image += 0.12 * np.sin(40 * (x + 0.6 * y)) * (y < 0.35) * (x > 0.45)                             # slanted stripes
    for cx, cy, r in rng.uniform([0, 0, 0.01], [1, 1, 0.04], size=(25, 3)):                          # small spots
        image += 0.12 * np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * r ** 2))
    image += 0.03 * rng.normal(size=image.shape)                                                     # grain
    return np.clip(image, 0, 1)


def low_rank() -> None:
    """A synthetic image and its approximations of rank 1, 5 and 20, with the singular values and the energy."""
    image = synthetic_image()
    mean = image.mean()                                   # the SVD of the CENTERED image: the mean grey level is
    U_, s, Vt = np.linalg.svd(image - mean, full_matrices=False)       # put back for display only
    energy = np.cumsum(s ** 2) / np.sum(s ** 2)
    m, n = image.shape
    fig = plt.figure(figsize=(15, 7.6))
    grid = fig.add_gridspec(2, 4, height_ratios=[1.15, 1])
    for i, k in enumerate([None, 1, 5, 20]):
        ax = fig.add_subplot(grid[0, i])
        if k is None:
            ax.imshow(image, cmap="gray", vmin=0, vmax=1)
            ax.set_title(f"L'image : {m} × {n} = {m * n} nombres", fontsize=10)
        else:
            approx = (U_[:, :k] * s[:k]) @ Vt[:k] + mean
            ax.imshow(approx, cmap="gray", vmin=0, vmax=1)
            ax.set_title(f"Rang {k} : {k * (m + n + 1)} nombres ({k * (m + n + 1) / (m * n):.0%}),\n"
                         f"{energy[k - 1]:.1%} de l'énergie".replace(".", ","), fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
    ax = fig.add_subplot(grid[1, :2])
    ax.semilogy(np.arange(1, len(s) + 1), s, "o", ms=3, color=C[0])
    ax.set(xlabel="i", ylabel="valeur singulière sᵢ (échelle log)",
           title="Les valeurs singulières de l'image centrée décroissent vite")
    ax = fig.add_subplot(grid[1, 2:])
    ax.plot(np.arange(1, 41), energy[:40], "o-", ms=3, color=C[1])
    ax.set(xlabel="rang k", ylabel="énergie gardée", ylim=(0.4, 1.005),
           title="Part de l'énergie gardée, (s₁² + ⋯ + s_k²) / Σ sᵢ² (image centrée)")
    fig.tight_layout()
    save(fig, "rang_faible.png")


def conditioning() -> None:
    """Two systems A x = b: the solutions for 400 right-hand sides b within 0.1 of b₀."""
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.4))
    cases = [(A, np.array([1.0, 1.0]), "A = [[6, 4], [1, −6]] : κ = 8/5 = 1,6\ndroites presque perpendiculaires",
              (-1.5, 3.5), (-2.2, 4.2)),
             (M, np.array([1.0, 1.0]), "M = [[10, 7], [7, 5]] : κ ≈ 223\ndroites presque parallèles",
              (-1.5, 3.5), (-2.2, 4.2))]
    for ax, (T, x0, title, xlim, ylim) in zip(axes, cases):
        b0 = T @ x0
        rng = np.random.default_rng(1263)
        angles, radii = rng.uniform(0, 2 * np.pi, 400), 0.1 * np.sqrt(rng.uniform(0, 1, 400))
        db = np.column_stack([radii * np.cos(angles), radii * np.sin(angles)])          # ‖δb‖ ≤ 0.1
        solutions = np.linalg.solve(T, (b0 + db).T).T
        xs = np.linspace(*xlim, 50)
        for row, bi, color in zip(T, b0, (C[1], C[2])):
            ax.plot(xs, (bi - row[0] * xs) / row[1], color=color, lw=1.2)
        ax.scatter(solutions[:, 0], solutions[:, 1], s=7, color=C[0], zorder=3, label="solutions pour ‖b − b₀‖ ≤ 0,1")
        b_text = ", ".join(f"{v:g}".replace("-", "−") for v in b0)
        ax.plot(*x0, "o", color="black", ms=5, zorder=4, label=f"x₀ = (1, 1), solution pour b₀ = ({b_text})")
        ax.set(xlim=xlim, ylim=ylim, aspect="equal", title=title)
        ax.legend(loc="lower left", fontsize=9)
    save(fig, "conditionnement.png")


def principal_axes() -> None:
    """A cloud of ℝ³ of covariance C, its three principal axes (± 2√λ), and its scores on the first two axes."""
    rng = np.random.default_rng(1260)
    X = rng.multivariate_normal(np.zeros(3), COV, size=400)
    X = X - X.mean(axis=0)
    values, Q = np.linalg.eigh(np.cov(X, rowvar=False))          # the axes of THIS cloud: its scores are uncorrelated
    values, Q = values[::-1], Q[:, ::-1]
    Q = Q * np.where(Q[np.argmax(np.abs(Q), axis=0), range(3)] < 0, -1, 1)
    fig = plt.figure(figsize=(13, 5.6))
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], s=4, color="0.55", alpha=0.5)
    for j, color in enumerate((C[1], C[2], C[3])):
        end = 2 * np.sqrt(values[j]) * Q[:, j]
        ax.plot([-end[0], end[0]], [-end[1], end[1]], [-end[2], end[2]], color=color, lw=3,
                label=f"u{'₁₂₃'[j]}, variance {values[j]:.1f}".replace(".", ","))
    ax.set(xlabel="x₁", ylabel="x₂", zlabel="x₃", title="Un nuage de 400 points tiré avec la covariance C,\net ses axes principaux (± 2√λ)")
    ax.legend(loc="upper left", fontsize=9)
    ax.view_init(elev=22, azim=-60)
    ax = fig.add_subplot(1, 2, 2)
    T = X @ Q[:, :2]
    ax.scatter(T[:, 0], T[:, 1], s=6, color="0.45", alpha=0.6)
    ax.set(xlabel="score sur u₁", ylabel="score sur u₂", aspect="equal",
           title=f"Les scores sur u₁ et u₂ : variances {T[:, 0].var(ddof=1):.1f} et {T[:, 1].var(ddof=1):.1f}\n"
                 f"(les valeurs propres), corrélation {abs(np.corrcoef(T.T)[0, 1]):.2f}".replace(".", ","))
    ax.axhline(0, color="0.7", lw=0.8)
    ax.axvline(0, color="0.7", lw=0.8)
    save(fig, "axes_principaux.png")


def explained_variance() -> None:
    """Eight features with a decreasing spectrum: the cumulative share kept, and the mean reconstruction error."""
    rng = np.random.default_rng(1261)
    spectrum = np.array([20.0, 9.0, 5.0, 2.5, 1.2, 0.6, 0.4, 0.3])
    Q = np.linalg.qr(rng.normal(size=(8, 8)))[0]
    X = rng.normal(size=(500, 8)) * np.sqrt(spectrum) @ Q.T + rng.normal(size=8) * 3
    Xc = X - X.mean(axis=0)
    values, vectors = np.linalg.eigh(np.cov(X, rowvar=False))
    values, vectors = values[::-1], vectors[:, ::-1]
    share = np.cumsum(values) / values.sum()
    ks = np.arange(0, 9)
    errors = [np.mean(np.sum((Xc - Xc @ vectors[:, :k] @ vectors[:, :k].T) ** 2, axis=1)) for k in ks]
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.8))
    ax = axes[0]
    ax.plot(np.arange(1, 9), share, "o-", color=C[0])
    for level, color, label in ((0.9, C[1], "90 %"), (0.95, C[2], "95 %")):
        k = int(np.argmax(share >= level)) + 1
        ax.axhline(level, color=color, ls="--", lw=1)
        ax.plot(k, share[k - 1], "o", ms=12, mfc="none", mec=color, mew=2)
        ax.text(5.6, level - 0.035, f"seuil de {label} : k = {k}", color=color, va="center")
    ax.set(xlabel="nombre k de composantes", ylabel="part cumulée de la variance", ylim=(0.4, 1.02), xlim=(0.5, 8.5),
           title="Part de variance expliquée cumulée")
    ax = axes[1]
    n = len(X)
    formula = [values[k:].sum() * (n - 1) / n for k in ks]
    ax.plot(ks, errors, "o", ms=8, color=C[0], label="mesurée : moyenne des ‖x − x̂‖²")
    ax.plot(ks, formula, "-", color=C[3], label="somme des variances oubliées × (n − 1)/n")
    ax.set(xlabel="nombre k de composantes", ylabel="erreur de reconstruction moyenne",
           title="L'erreur de reconstruction : ce qu'on n'a pas gardé")
    ax.legend()
    save(fig, "variance_expliquee.png")


def neighbourhoods() -> None:
    """t-SNE: the probabilities p(j | i) for two widths σ, and the Gaussian and Student kernels."""
    d = np.array([0.4, 0.7, 1.0, 1.3, 1.9, 2.6, 3.4])
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.6))
    ax = axes[0]
    width = 0.11
    for shift, sigma, color in ((-width / 2, 0.5, C[0]), (width / 2, 1.5, C[1])):
        w = np.exp(-d ** 2 / (2 * sigma ** 2))
        p = w / w.sum()
        perplexity = 2 ** (-np.sum(p * np.log2(p)))
        ax.bar(d + shift, p, width, color=color, label=f"σ = {sigma} : perplexité {perplexity:.1f}".replace(".", ","))
    ax.set(xlabel="distance du voisin j au point i (sept voisins)", ylabel="p(j | i)",
           title="Les probabilités de voisinage d'un point,\npour deux largeurs σ")
    ax.legend()
    ax = axes[1]
    r = np.linspace(0, 5, 300)
    ax.plot(r, np.exp(-r ** 2 / 2), color=C[0], label="gaussienne exp(−r²/2) (espace d'origine)")
    ax.plot(r, 1 / (1 + r ** 2), color=C[3], label="Student 1/(1 + r²) (la carte)")
    ax.set(xlabel="distance r", ylabel="poids (non normalisé)",
           title="Une queue plus lourde dans la carte :\nles points lointains peuvent s'écarter davantage")
    ax.legend()
    save(fig, "tsne_voisinages.png")


def main() -> int:
    print(f"figures of M12d -> {OUT.relative_to(ROOT)}")
    svd_geometry()
    low_rank()
    conditioning()
    principal_axes()
    explained_variance()
    neighbourhoods()
    return 0


if __name__ == "__main__":
    sys.exit(main())
