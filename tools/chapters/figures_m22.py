#!/usr/bin/env python
"""Draw the figures of chapter M22 (used by Claude).

    python tools/chapters/figures_m22.py

Writes small PNG files into chapitres/m22_recurrences/figures/: the impulse response of the two-year course,
A = [[0.2, 0], [0.6, 0.1]], B = (1, 0), C = (0, 0.8), and the graduates of 100, 120 then 80 enrolments as a sum of
shifted copies of it; the trajectories of x ↦ cA x for A = [[1, -1], [0.8, 0.2]] (eigenvalues 0.6 ± 0.8i) and
c = 0.96, 1, 1.03; the transient growth of A = [[0.75, 6], [0, 0.6]] against 0.75ᵗ, and the two large terms that
cancel; the unit balls of the norms 1, 2 and ∞, their images by A = [[2, 1], [-2, 4]] and the balls of radius
‖A‖; what remains of three pollutants (factors 0.97, 0.92, 0.6) and the growth rate (1/t) ln(a₁ ⋯ aₜ) of six
random products of factors 2.5 or 0.3;
the trajectory of z ↦ z² − 0.24 from 0.2 + 0.4i and the norms of the products of its Jacobians. The numbers are
those of the fiche; none comes from workbookIA 22, 23 or 24 (no network, no cell, no gradient, no 22xx seed). The
only randomness is the coin of the random products (seed 5701).
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, Polygon  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m22_recurrences" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

COURSE_A = np.array([[0.2, 0.0], [0.6, 0.1]])     # §1: the two-year course
COURSE_B = np.array([1.0, 0.0])
COURSE_C = np.array([0.0, 0.8])
ENROLMENTS = [100.0, 120.0, 80.0]                  # §1: u_0, u_1, u_2
SPIRAL_A = np.array([[1.0, -1.0], [0.8, 0.2]])     # §2: eigenvalues 0.6 ± 0.8i, det 1
SPIRAL_V = np.array([[1.0, 0.0], [0.4, 0.8]])      # §2: A = V R_θ V⁻¹
TRANSIENT_A = np.array([[0.75, 6.0], [0.0, 0.6]])  # §3: ρ = 0.75, non normal
NORM_A = np.array([[2.0, 1.0], [-2.0, 4.0]])       # §4: ‖A‖₁ = 5, ‖A‖₂ = 2√5, ‖A‖∞ = 6
LAKE_EPS = [0.03, 0.08, 0.4]                       # §5: monthly elimination rates
GOOD, BAD = 2.5, 0.3                               # §5: random yearly factors
SHIFT = -0.24                                      # §6: z ↦ z² + SHIFT
Z0 = 0.2 + 0.4j
SEED = 5701


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and ax.axison:
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


# --------------------------------------------------------------------------------------------------------- §1
def impulse_response() -> None:
    """§1: h_k = C A^k B, and the graduates as the sum of the shifted copies u_k h (a convolution)."""
    K = 7
    h = np.array([COURSE_C @ np.linalg.matrix_power(COURSE_A, k) @ COURSE_B for k in range(K)])
    fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.2), gridspec_kw={"width_ratios": [1, 1.3]})
    ax = axes[0]
    ax.stem(np.arange(K), h, linefmt=C[0], markerfmt="o", basefmt=" ")
    for k in range(4):
        ax.annotate(french_number(round(h[k], 4)), (k, h[k]), textcoords="offset points", xytext=(8, 4),
                    fontsize=9.5)
    ax.set(title="réponse impulsionnelle h_k = C Aᵏ B", xlabel="k : la sortie k + 1 ans après une inscription",
           ylabel="diplômés par inscrit", xticks=range(K), ylim=(-0.03, 0.56))
    ax.grid(alpha=0.25)

    ax = axes[1]
    T = 8
    years = np.arange(1, T)
    bottom = np.zeros(len(years))
    for i, u in enumerate(ENROLMENTS):
        part = np.array([u * h[t - 1 - i] if 0 <= t - 1 - i < K else 0.0 for t in years])
        ax.bar(years, part, bottom=bottom, color=C[i], alpha=0.8,
               label=f"promotion inscrite en {i} : {french_number(u)} × h décalée de {i}")
        bottom += part
    for t, total in zip(years, bottom):
        if total > 0:
            ax.text(t, total + 1.2, french_number(round(total, 2)), ha="center", fontsize=9.5)
    ax.set(title="diplômés de l'année t : la convolution h * u, décalée d'un an", xlabel="année t",
           ylabel="diplômés", xticks=years, ylim=(0, 104))
    ax.legend(fontsize=8.8, loc="upper right")
    ax.grid(alpha=0.25, axis="y")
    fig.suptitle("Un cursus en deux ans : chaque promotion apporte sa copie de la réponse impulsionnelle",
                 fontsize=11.5, y=1.02)
    save(fig, "reponse_impulsionnelle.png")


# --------------------------------------------------------------------------------------------------------- §2
def spirals() -> None:
    """§2: x ↦ cA x from (1, 0), for c = 0.96, 1, 1.03; for c = 1, also the circle of R_θ and its image by V."""
    settings = [(0.96, 70, "0,96 A : |λ| = 0,96, la spirale rentre"),
                (1.0, 40, "A : |λ| = 1, une ellipse"),
                (1.03, 40, "1,03 A : |λ| = 1,03, la spirale sort")]
    fig, axes = plt.subplots(1, 3, figsize=(14.0, 4.9))
    for ax, (c, steps, title) in zip(axes, settings):
        x = np.array([1.0, 0.0])
        pts = [x]
        for _ in range(steps):
            x = c * SPIRAL_A @ x
            pts.append(x)
        pts = np.array(pts)
        ax.plot(pts[:, 0], pts[:, 1], "-", color=C[0], lw=0.8, alpha=0.35 if c == 1.0 else 0.6)
        ax.scatter(pts[:, 0], pts[:, 1], s=14, c=np.arange(len(pts)), cmap=wbplot.sequential_cmap(), zorder=3)
        for t in range(4):
            ax.annotate(f"x{'₀₁₂₃'[t]}", pts[t], textcoords="offset points", xytext=(6, 4), fontsize=9.5)
        if c == 1.0:
            s = np.linspace(0, 2 * np.pi, 200)
            y0 = np.linalg.solve(SPIRAL_V, np.array([1.0, 0.0]))
            ellipse = SPIRAL_V @ (np.linalg.norm(y0) * np.vstack([np.cos(s), np.sin(s)]))
            ax.plot(ellipse[0], ellipse[1], ":", color=C[1], lw=1.5, label="image par V d'un cercle")
            ax.plot(np.linalg.norm(y0) * np.cos(s), np.linalg.norm(y0) * np.sin(s), "--", color="0.6", lw=1.0,
                    label="le cercle de R_θ, avant V")
            ax.legend(fontsize=8.5, loc="lower left")
        ax.plot(0, 0, "k+", ms=9)
        lim = 1.6 if c != 1.03 else 3.6
        ax.set(xlim=(-lim, lim), ylim=(-lim, lim), aspect="equal", title=title, xlabel="x₁", ylabel="x₂")
        ax.grid(alpha=0.25)
    fig.suptitle("A de lignes (1, −1) et (0,8 ; 0,2), de valeurs propres 0,6 ± 0,8i : un multiple de A tourne "
                 "d'environ 53° par pas, dans un repère oblique", fontsize=11, y=1.0)
    save(fig, "spirales.png")


# --------------------------------------------------------------------------------------------------------- §3
def transient() -> None:
    """§3: ‖Aᵗ‖₂ against ρᵗ for the non-normal triangular matrix, and the two terms that cancel."""
    T = 40
    ts = np.arange(0, T + 1)
    norms = [np.linalg.norm(np.linalg.matrix_power(TRANSIENT_A, t), 2) for t in ts]
    rho = 0.75 ** ts
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.6))
    ax = axes[0]
    ax.semilogy(ts, norms, "o-", color=C[1], ms=4, label="‖Aᵗ‖₂, A non normale")
    ax.semilogy(ts, rho, "s-", color=C[0], ms=3, label="ρ(A)ᵗ = 0,75ᵗ = ‖diag(0,75 ; 0,6)ᵗ‖₂")
    ax.axhline(1.0, color="0.4", lw=1.0, ls="--")
    ax.annotate("8,25 en t = 3", (3, norms[3]), textcoords="offset points", xytext=(12, -4), fontsize=9.5,
                color=C[1])
    ax.annotate("sous 1 à partir de t = 13", (13, norms[13]), textcoords="offset points", xytext=(8, 10),
                fontsize=9.5, color=C[1])
    ax.set(title="la norme monte, puis décroît au rythme de ρ = 0,75", xlabel="t", ylabel="échelle logarithmique")
    ax.legend(fontsize=9, loc="lower left")
    ax.grid(alpha=0.25, which="both")

    ax = axes[1]
    ts2 = np.arange(0, 21)
    big1 = 40 * 0.75 ** ts2
    big2 = 40 * 0.6 ** ts2
    ax.plot(ts2, big1, "-", color=C[0], label="40 × 0,75ᵗ : 1ʳᵉ coordonnée de 40 × 0,75ᵗ e₁")
    ax.plot(ts2, big2, "-", color=C[2], label="40 × 0,6ᵗ : opposée de la 1ʳᵉ coordonnée de 0,6ᵗ v₂")
    ax.plot(ts2, big1 - big2, "o-", color=C[1], ms=4, label="leur différence : 1ʳᵉ coordonnée de Aᵗe₂")
    ax.set(title="e₂ = v₂ + 40 e₁ : deux grands termes qui se compensent d'abord", xlabel="t", ylim=(0, 42),
           xticks=range(0, 21, 5))
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(alpha=0.25)
    fig.suptitle("Croissance transitoire : A de lignes (0,75 ; 6) et (0 ; 0,6), de rayon spectral 0,75",
                 fontsize=11.5, y=1.01)
    save(fig, "croissance_transitoire.png")


# --------------------------------------------------------------------------------------------------------- §4
def balls() -> None:
    """§4: the unit balls of the norms 1, 2, ∞, their images by A, and the balls of radius ‖A‖."""
    A = NORM_A
    s = np.linspace(0, 2 * np.pi, 400)
    circle = np.vstack([np.cos(s), np.sin(s)])
    diamond = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]], float).T
    square = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]], float).T
    panels = [
        ("norme 1 : ‖A‖₁ = 5 (la 2ᵉ colonne)", diamond, 5.0, [np.array([1.0, 4.0]), np.array([-1.0, -4.0])],
         "polygon"),
        ("norme 2 : ‖A‖₂ = 2√5 ≈ 4,47", circle, 2 * np.sqrt(5),
         [A @ np.array([1.0, -2.0]) / np.sqrt(5), A @ np.array([-1.0, 2.0]) / np.sqrt(5)],
         "curve"),
        ("norme ∞ : ‖A‖∞ = 6 (la 2ᵉ ligne)", square, 6.0, [np.array([-1.0, 6.0]), np.array([1.0, -6.0])],
         "polygon"),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(14.0, 5.0))
    for ax, (title, ball, radius, touch, kind) in zip(axes, panels):
        image = A @ ball
        if kind == "polygon":
            ax.add_patch(Polygon(ball.T, closed=True, fill=False, ec="0.4", ls="--", lw=1.2,
                                 label="boule unité"))
            ax.add_patch(Polygon(image.T, closed=True, fc=C[0], alpha=0.3, ec=C[0], lw=1.5,
                                 label="son image par A"))
            ax.add_patch(Polygon((radius * ball).T, closed=True, fill=False, ec=C[1], lw=1.8,
                                 label=f"boule de rayon {french_number(round(radius, 2))}"))
        else:
            ax.plot(ball[0], ball[1], "--", color="0.4", lw=1.2, label="boule unité")
            ax.fill(image[0], image[1], color=C[0], alpha=0.3)
            ax.plot(image[0], image[1], color=C[0], lw=1.5, label="son image par A")
            ax.plot(radius * ball[0], radius * ball[1], color=C[1], lw=1.8,
                    label=f"cercle de rayon {french_number(round(radius, 2))}")
        for p in touch:
            ax.plot(*p, "o", color=C[3], ms=8, zorder=4)
            ax.annotate(f"({french_number(round(p[0], 2))} ; {french_number(round(p[1], 2))})", p,
                        textcoords="offset points", xytext=(8, -4), fontsize=9.5)
        ax.plot(0, 0, "k+", ms=8)
        ax.set(xlim=(-6.8, 6.8), ylim=(-6.8, 6.8), aspect="equal", title=title)
        ax.legend(fontsize=8.3, loc="upper center", bbox_to_anchor=(0.5, -0.07), ncol=2)
        ax.grid(alpha=0.25)
    fig.suptitle("A de lignes (2, 1) et (−2, 4) : la norme induite est le rayon de la plus petite boule, "
                 "de la même norme, qui contient l'image de la boule unité", fontsize=11, y=1.0)
    save(fig, "boules_images.png")


# --------------------------------------------------------------------------------------------------------- §5
def factors() -> None:
    """§5: what remains of three pollutants, and six random products of factors 2.5 or 0.3 (seed 5701)."""
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.7))
    ax = axes[0]
    ts = np.arange(0, 37)
    for i, eps in enumerate(LAKE_EPS):
        ax.semilogy(ts, (1 - eps) ** ts, "-", color=C[i], lw=2,
                    label=f"ε = {french_number(eps)} : {french_number(1 - eps)}ᵗ")
        ax.semilogy(ts, np.exp(-eps * ts), ":", color=C[i], lw=1.6)
        half = np.log(2) / -np.log(1 - eps)
        ax.plot(half, 0.5, "o", color=C[i], ms=6)
    ax.axhline(0.5, color="0.5", lw=0.8, ls="--")
    ax.plot([], [], ":", color="0.3", lw=1.6, label="pointillés : e^(−tε)")
    ax.plot([], [], "o", color="0.3", ms=6, label="demi-vies : 1,36 ; 8,3 et 22,8 mois")
    ax.set(title="ce qui reste de trois polluants, en échelle logarithmique", xlabel="mois t", ylim=(1e-6, 1.5))
    ax.legend(fontsize=9, loc="lower left")
    ax.grid(alpha=0.25, which="both")

    ax = axes[1]
    rng = np.random.default_rng(SEED)
    T = 400
    ts = np.arange(1, T + 1)
    for j in range(6):
        a = np.where(rng.random(T) < 0.5, GOOD, BAD)
        ax.plot(ts, np.cumsum(np.log(a)) / ts, "-", color=C[j % 8], lw=1.0, alpha=0.85)
    ax.axhline(0.5 * np.log(GOOD * BAD), color="k", ls="--", lw=2,
               label="𝔼[ln a] = ½ ln 0,75 ≈ −0,144 : la population s'éteint")
    ax.axhline(np.log((GOOD + BAD) / 2), color=C[7], lw=2, label="ln 𝔼[a] = ln 1,4 ≈ 0,336 : la moyenne grandit")
    ax.axhline(0.0, color="0.5", lw=0.8)
    ax.set_xscale("log")
    ax.set(title="facteurs 2,5 ou 0,3 à pile ou face : (1/t) ln(a₁ ⋯ aₜ), six trajectoires",
           xlabel="années t (échelle logarithmique)", ylim=(-1.3, 1.0))
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(alpha=0.25, which="both")
    save(fig, "facteurs_produits.png")


# --------------------------------------------------------------------------------------------------------- §6
def jacobian_products() -> None:
    """§6: the trajectory of z ↦ z² − 0.24 and the norm of the product of its Jacobians (multiplication by 2z)."""
    T = 12
    zs = [Z0]
    for _ in range(T):
        zs.append(zs[-1] ** 2 + SHIFT)
    zs = np.array(zs)
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 5.0), gridspec_kw={"width_ratios": [1, 1.1]})
    ax = axes[0]
    ax.add_patch(Circle((0, 0), 0.46, fc=C[0], alpha=0.08, ec=C[0], lw=1.2,
                       label="disque |z| ≤ 0,46 (contraction)"))
    ax.plot(zs.real, zs.imag, "-", color=C[1], lw=1.0, alpha=0.6)
    ax.scatter(zs.real, zs.imag, s=22, color=C[1], zorder=3, label="z₀, z₁, z₂, …")
    for t in range(4):
        ax.annotate(f"z{'₀₁₂₃'[t]}", (zs[t].real, zs[t].imag), textcoords="offset points", xytext=(6, 5),
                    fontsize=9.5)
    ax.plot(-0.2, 0, "*", color=C[2], ms=14, zorder=4, label="point fixe attractif −0,2")
    ax.plot(1.2, 0, "X", color=C[7], ms=10, zorder=4, label="point fixe répulsif 1,2")
    ax.set(xlim=(-0.6, 1.35), ylim=(-0.55, 0.55), aspect="equal", title="la trajectoire de z ↦ z² − 0,24",
           xlabel="partie réelle x", ylabel="partie imaginaire y")
    ax.legend(fontsize=8.5, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2)
    ax.grid(alpha=0.25)

    ax = axes[1]
    norms, bounds, P, b = [1.0], [1.0], np.eye(2), 1.0
    for t in range(T):
        z = zs[t]
        J = 2 * np.array([[z.real, -z.imag], [z.imag, z.real]])
        P = J @ P
        b *= np.linalg.norm(J, 2)
        norms.append(np.linalg.norm(P, 2))
        bounds.append(b)
    ts = np.arange(T + 1)
    ax.semilogy(ts, norms, "o-", color=C[1], ms=5, label="‖Jₜ₋₁ ⋯ J₀‖₂ = ‖∂xₜ/∂x₀‖₂")
    ax.semilogy(ts, bounds, "x", color=C[0], ms=9, label="‖Jₜ₋₁‖₂ ⋯ ‖J₀‖₂ (ici, la même chose)")
    ax.semilogy(ts, 0.92 ** ts, "--", color="0.4", label="0,92ᵗ (le facteur de contraction du disque)")
    ax.semilogy(ts, 0.4 ** ts, ":", color=C[2], label="0,4ᵗ (le rayon spectral au point fixe)")
    ax.set(title="la jacobienne de x₀ ↦ xₜ, un produit de jacobiennes", xlabel="t", ylim=(1e-6, 2))
    ax.legend(fontsize=8.8, loc="lower left")
    ax.grid(alpha=0.25, which="both")
    save(fig, "trajectoire_jacobiennes.png")


def main() -> int:
    print(f"Figures M22 → {OUT.relative_to(ROOT)}")
    impulse_response()
    spirals()
    transient()
    balls()
    factors()
    jacobian_products()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
