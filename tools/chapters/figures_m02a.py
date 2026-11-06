#!/usr/bin/env python
"""Draw the figures of chapter M02a (used by Claude).

    python tools/chapters/figures_m02a.py

Writes small PNG files into chapitres/m02a_integrales_densites/figures/: the three Riemann sums of x² on [0, 2], a
signed area, the area function and its derivative, two tails (1/x² and 1/x), trapezoids and Simpson's parabolas on
1/x, the errors of the methods against n, a density with the probability of an interval and a density above 1, two
cumulative distribution functions with their quantiles, the area under a ROC curve, and the mean value of a function.
Every figure is computed and uses the workbook style (wbm.plot colours, French decimal commas). The functions are those
of the sheet's own examples: none comes from workbookIA 2, 3 or B6, from the placement test or from an exercise of M02a.
"""

from __future__ import annotations

import math
import sys
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

OUT = ROOT / "chapitres" / "m02a_integrales_densites" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


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


def axes_through_origin(ax) -> None:
    ax.axhline(0, color="gray", linewidth=0.9)
    ax.grid(True, alpha=0.25)


def fig_riemann() -> None:
    """x² on [0, 2], 4 rectangles: left (1,75), right (3,75), midpoint (2,625); the exact area is 8/3."""
    f = lambda x: x ** 2   # noqa: E731
    xs = np.linspace(0, 2, 200)
    h = 0.5
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.4), sharey=True)
    for ax, (rule, shift, colour) in zip(axes, [("à gauche", 0.0, C[0]), ("à droite", 1.0, C[1]),
                                                 ("au milieu", 0.5, C[2])]):
        total = 0.0
        for i in range(4):
            height = f(i * h + shift * h)
            total += h * height
            ax.add_patch(Rectangle((i * h, 0), h, height, facecolor=colour, alpha=0.35, edgecolor=colour))
            ax.plot([i * h + shift * h], [height], "o", color=colour, markersize=4)
        ax.plot(xs, f(xs), color="black", linewidth=1.6)
        axes_through_origin(ax)
        ax.set_xlim(-0.1, 2.1)
        ax.set_ylim(0, 4.3)
        ax.set_title(f"rectangles {rule} : {total:g}".replace(".", ","))
        ax.set_xlabel("x")
    axes[0].set_ylabel("y = x²")
    fig.suptitle("Trois sommes de Riemann de x² sur [0 ; 2] (n = 4) ; l'aire exacte vaut 8/3 ≈ 2,667", y=1.03)
    save(fig, "riemann.png")


def fig_signed_area() -> None:
    """sin on [0, 2π]: the positive arch counts +2, the negative one −2, the integral is 0."""
    xs = np.linspace(0, 2 * np.pi, 400)
    ys = np.sin(xs)
    fig, ax = plt.subplots(figsize=(7, 2.8))
    ax.fill_between(xs, ys, where=ys >= 0, color=C[0], alpha=0.35, label="compte +2")
    ax.fill_between(xs, ys, where=ys < 0, color=C[3], alpha=0.35, label="compte −2")
    ax.plot(xs, ys, color="black", linewidth=1.5)
    axes_through_origin(ax)
    ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
    ax.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])
    ax.set_title("Aire algébrique : ∫ sin x dx sur [0 ; 2π] vaut 2 − 2 = 0")
    ax.legend(loc="upper right")
    fig.axes[0].yaxis.set_major_formatter(FuncFormatter(french_number))
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "aire_signee.png", dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("  aire_signee.png")


def fig_area_function() -> None:
    """f(t) = 1 + t/2 on [0, 3] and its area function A(x) = x + x²/4: the slope of A at x is f(x)."""
    f = lambda t: 1 + t / 2   # noqa: E731
    A = lambda x: x + x ** 2 / 4   # noqa: E731
    ts = np.linspace(0, 3, 200)
    x0, h = 1.5, 0.4
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.6))
    ax1.plot(ts, f(ts), color="black", linewidth=1.6)
    mask = ts <= x0
    ax1.fill_between(ts[mask], f(ts[mask]), color=C[0], alpha=0.35, label="A(x), l'aire de 0 à x")
    band = (ts >= x0) & (ts <= x0 + h)
    ax1.fill_between(ts[band], f(ts[band]), color=C[1], alpha=0.5, label="A(x + h) − A(x) ≈ f(x) h")
    axes_through_origin(ax1)
    ax1.set_xlim(0, 3)
    ax1.set_ylim(0, 2.8)
    ax1.set_xticks([0, x0, x0 + h, 3])
    ax1.set_xticklabels(["0", "x", "x + h", "3"])
    ax1.set_title("f(t) = 1 + t/2 et l'aire sous sa courbe")
    ax1.legend(loc="upper left", fontsize=9)
    ax2.plot(ts, A(ts), color=C[0], linewidth=1.8, label="A(x) = x + x²/4")
    slope = f(x0)
    xt = np.linspace(x0 - 0.9, x0 + 0.9, 10)
    ax2.plot(xt, A(x0) + slope * (xt - x0), "--", color=C[1], label=f"tangente en x = 1,5 : pente f(1,5) = {slope:g}"
             .replace(".", ","))
    ax2.plot([x0], [A(x0)], "o", color=C[1])
    axes_through_origin(ax2)
    ax2.set_xlim(0, 3)
    ax2.set_title("La fonction aire : A′(x) = f(x)")
    ax2.legend(loc="upper left", fontsize=9)
    save(fig, "fonction_aire.png")


def fig_tails() -> None:
    """1/x² (area 1 from 1 to +∞) against 1/x (area ln b, unbounded)."""
    xs = np.linspace(1, 10, 300)
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.plot(xs, 1 / xs, color=C[3], linewidth=1.6, label="1/x : aire de 1 à b = ln b → +∞")
    ax.plot(xs, 1 / xs ** 2, color=C[0], linewidth=1.6, label="1/x² : aire de 1 à b = 1 − 1/b → 1")
    ax.fill_between(xs, 1 / xs ** 2, color=C[0], alpha=0.3)
    axes_through_origin(ax)
    ax.set_xlim(0.8, 10)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("x")
    ax.set_title("Deux queues : l'une a une aire finie, l'autre non")
    ax.legend(loc="upper right")
    save(fig, "queues.png")


def fig_methods() -> None:
    """1/x on [1, 2], n = 2: two trapezoids against Simpson's parabola through the three points."""
    f = lambda x: 1 / x   # noqa: E731
    xs = np.linspace(0.95, 2.05, 300)
    pts = np.array([1.0, 1.5, 2.0])
    coeffs = np.polyfit(pts, f(pts), 2)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.4), sharey=True)
    for ax in (ax1, ax2):
        ax.plot(xs, f(xs), color="black", linewidth=1.6, label="y = 1/x")
        ax.plot(pts, f(pts), "o", color=C[1])
        axes_through_origin(ax)
        ax.set_xlim(0.9, 2.1)
        ax.set_ylim(0, 1.1)
        ax.set_xlabel("x")
    ax1.fill_between(pts, f(pts), color=C[0], alpha=0.35, label="2 trapèzes : 0,708")
    ax1.plot(pts, f(pts), color=C[0], linewidth=1.2)
    ax1.set_title("Trapèzes : des segments")
    ax1.legend(loc="upper right")
    xp = np.linspace(1, 2, 200)
    ax2.fill_between(xp, np.polyval(coeffs, xp), color=C[2], alpha=0.35, label="Simpson : 0,6944")
    ax2.plot(xp, np.polyval(coeffs, xp), "--", color=C[2], linewidth=1.2)
    ax2.set_title("Simpson : une parabole par trois points")
    ax2.legend(loc="upper right")
    fig.suptitle("∫ 1/x dx sur [1 ; 2] = ln 2 ≈ 0,6931, avec n = 2", y=1.03)
    save(fig, "methodes.png")


def _sums(f, a, b, n):
    h = (b - a) / n
    left = h * sum(f(a + i * h) for i in range(n))
    mid = h * sum(f(a + (i + 0.5) * h) for i in range(n))
    trap = h * ((f(a) + f(b)) / 2 + sum(f(a + i * h) for i in range(1, n)))
    simp = h / 3 * (f(a) + f(b) + sum((4 if i % 2 else 2) * f(a + i * h) for i in range(1, n)))
    return left, mid, trap, simp


def fig_errors() -> None:
    """Errors on ∫_1^2 dx/x against n, in log-log scale: slopes −1, −2, −2 and −4."""
    ns = np.array([2, 4, 8, 16, 32, 64])
    exact = math.log(2)
    errs = np.array([[abs(v - exact) for v in _sums(lambda x: 1 / x, 1, 2, int(n))] for n in ns])
    fig, ax = plt.subplots(figsize=(6.5, 4))
    labels = ["rectangles à gauche", "rectangles au milieu", "trapèzes", "Simpson"]
    for k, (label, marker) in enumerate(zip(labels, "osd^")):
        ax.loglog(ns, errs[:, k], marker=marker, color=C[k], label=label)
    ax.set_xticks(ns)
    ax.set_xticklabels([str(n) for n in ns])
    ax.minorticks_off()
    ax.set_xlabel("nombre d'intervalles n (échelle logarithmique)")
    ax.set_ylabel("erreur (échelle logarithmique)")
    ax.set_title("Erreur sur ∫ 1/x dx (de 1 à 2) quand n double")
    ax.grid(True, which="both", alpha=0.25)
    ax.legend()
    save(fig, "erreurs.png")


def fig_density() -> None:
    """f(x) = 3/4 (1 − x²) on [−1, 1], with P(0 ≤ X ≤ 1/2) = 11/32; and the density 4 on [2 ; 2,25]."""
    xs = np.linspace(-1.3, 1.3, 400)
    f = np.where(np.abs(xs) <= 1, 0.75 * (1 - xs ** 2), 0)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.4), gridspec_kw={"width_ratios": [1.3, 1]})
    ax1.plot(xs, f, color="black", linewidth=1.6)
    band = (xs >= 0) & (xs <= 0.5)
    ax1.fill_between(xs[band], f[band], color=C[0], alpha=0.45, label="P(0 ≤ X ≤ 1/2) = 11/32 ≈ 0,344")
    axes_through_origin(ax1)
    ax1.set_ylim(0, 0.95)
    ax1.set_title("f(x) = 3/4 (1 − x²) sur [−1 ; 1] : aire totale 1")
    ax1.legend(loc="upper right", fontsize=9)
    xs2 = np.linspace(1.8, 2.45, 400)
    g = np.where((xs2 >= 2) & (xs2 <= 2.25), 4.0, 0.0)
    ax2.plot(xs2, g, color="black", linewidth=1.6)
    ax2.fill_between(xs2, g, color=C[2], alpha=0.35, label="aire : 0,25 × 4 = 1")
    ax2.axhline(1, color=C[3], linestyle=":", linewidth=1.2, label="hauteur 1")
    axes_through_origin(ax2)
    ax2.set_ylim(0, 5.4)
    ax2.set_title("Une densité qui vaut 4 : rien d'anormal")
    ax2.legend(loc="upper right", fontsize=9)
    save(fig, "densite.png")


def fig_cdf() -> None:
    """F of the density 3/4 (1 − x²) (median 0) and of the exponential density 0,5 e^(−0,5 x) (quartiles, median)."""
    xs = np.linspace(-1.5, 1.5, 400)
    F1 = np.clip(0.5 + 0.75 * (xs - xs ** 3 / 3), 0, 1)
    F1[xs < -1] = 0
    F1[xs > 1] = 1
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.4))
    ax1.plot(xs, F1, color=C[0], linewidth=1.8)
    ax1.plot([0.5, 0.5], [0, 27 / 32], ":", color="gray")
    ax1.plot([-1.5, 0.5], [27 / 32, 27 / 32], ":", color="gray")
    ax1.plot([0.5], [27 / 32], "o", color=C[1])
    ax1.annotate("F(1/2) = 27/32", (0.5, 27 / 32), textcoords="offset points", xytext=(-95, 6))
    axes_through_origin(ax1)
    ax1.set_ylim(-0.05, 1.08)
    ax1.set_title("F(x) = P(X ≤ x) pour la densité 3/4 (1 − x²)")
    ts = np.linspace(0, 9, 400)
    F2 = 1 - np.exp(-0.5 * ts)
    ax2.plot(ts, F2, color=C[2], linewidth=1.8)
    for p, name in [(0.25, "Q1"), (0.5, "médiane"), (0.9, "90ᵉ percentile")]:
        q = -math.log(1 - p) / 0.5
        ax2.plot([0, q], [p, p], ":", color="gray")
        ax2.plot([q, q], [0, p], ":", color="gray")
        ax2.plot([q], [p], "o", color=C[1])
        ax2.annotate(f"{name} ≈ {q:.2f}".replace(".", ","), (q, p), textcoords="offset points", xytext=(6, -14))
    axes_through_origin(ax2)
    ax2.set_ylim(-0.05, 1.08)
    ax2.set_xlabel("t (minutes)")
    ax2.set_title("F(t) = 1 − e^(−0,5 t) et trois quantiles")
    save(fig, "repartition.png")


def fig_roc() -> None:
    """An idealised ROC curve TPR = √FPR: area 2/3; the diagonal of a random classifier: area 1/2."""
    xs = np.linspace(0, 1, 300)
    fig, ax = plt.subplots(figsize=(4.6, 4.4))
    ax.fill_between(xs, np.sqrt(xs), color=C[0], alpha=0.3, label="AUC = ∫ √x dx = 2/3")
    ax.plot(xs, np.sqrt(xs), color=C[0], linewidth=1.8, label="ROC : TPR = √FPR")
    ax.plot([0, 1], [0, 1], "--", color="gray", label="hasard : AUC = 1/2")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.02)
    ax.set_aspect("equal")
    ax.set_xlabel("taux de faux positifs (FPR)")
    ax.set_ylabel("taux de vrais positifs (TPR)")
    ax.set_title("L'AUC est une aire")
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(True, alpha=0.25)
    save(fig, "roc_aire.png")


def fig_mean_value() -> None:
    """g(t) = e^(t/2) on [0, 2], its mean value e − 1 and the rectangle of the same area."""
    g = lambda t: np.exp(t / 2)   # noqa: E731
    ts = np.linspace(0, 2, 300)
    mean = math.e - 1
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.fill_between(ts, g(ts), color=C[0], alpha=0.3, label="aire sous la courbe : 2(e − 1)")
    ax.plot(ts, g(ts), color="black", linewidth=1.6, label="g(t) = e^(t/2)")
    ax.add_patch(Rectangle((0, 0), 2, mean, fill=False, edgecolor=C[1], linewidth=1.6, linestyle="--",
                           label=f"rectangle de hauteur e − 1 ≈ {mean:.3f}".replace(".", ",")))
    axes_through_origin(ax)
    ax.set_xlim(-0.1, 2.1)
    ax.set_ylim(0, 3)
    ax.set_title("Valeur moyenne : la hauteur du rectangle de même aire")
    ax.legend(loc="upper left", fontsize=9)
    save(fig, "valeur_moyenne.png")


def main() -> int:
    print(f"Figures de M02a dans {OUT.relative_to(ROOT)} :")
    fig_riemann()
    fig_signed_area()
    fig_area_function()
    fig_tails()
    fig_methods()
    fig_errors()
    fig_density()
    fig_cdf()
    fig_roc()
    fig_mean_value()
    return 0


if __name__ == "__main__":
    sys.exit(main())
