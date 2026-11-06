#!/usr/bin/env python
"""Draw the figures of chapter R6 (used by Claude).

    python tools/chapters/figures_r6.py

Writes small PNG files into chapitres/r6_exp_log/figures/: exponential functions aˣ for three bases, exp and ln
(reciprocal functions), a power against an exponential (who wins, and when), the same exponential data on a linear
and on a logarithmic scale, and the sigmoid and tanh. Every figure is computed and uses the workbook style (wbm.plot
colours, French decimal commas). The numbers are those of the sheet's own examples: none comes from workbookIA 0B,
from the placement test or from an exercise of R6.
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

OUT = ROOT / "chapitres" / "r6_exp_log" / "figures"
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


def fig_powers() -> None:
    """§1: 3ˣ, 2ˣ and 0,4ˣ on [−3, 3]; all pass through (0, 1) and stay positive."""
    x = np.linspace(-3, 3, 400)
    fig, ax = plt.subplots(figsize=(6.4, 4))
    for base, colour in ((3, C[0]), (2, C[2]), (0.4, C[1])):
        ax.plot(x, base**x, color=colour, linewidth=2, label=f"{french_number(base)}ˣ")
    ax.plot([0], [1], "o", color="black", markersize=5)
    ax.annotate("(0 ; 1)", (0, 1), textcoords="offset points", xytext=(8, -14), fontsize=9)
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.axvline(0, color="gray", linewidth=0.8)
    ax.set_ylim(-0.5, 10)
    ax.set_xlabel("x")
    ax.set_title("Trois exponentielles : toujours positives, et égales à 1 en x = 0", fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.legend()
    save(fig, "exponentielles.png")


def fig_exp_ln() -> None:
    """§3: exp and ln, symmetric about the line y = x."""
    fig, ax = plt.subplots(figsize=(5.4, 5.4))
    x = np.linspace(-3, 2.3, 300)
    ax.plot(x, np.exp(x), color=C[0], linewidth=2, label="exp(x) = eˣ")
    t = np.linspace(0.02, 10, 400)
    ax.plot(t, np.log(t), color=C[1], linewidth=2, label="ln x")
    d = np.linspace(-3, 10, 2)
    ax.plot(d, d, "--", color="gray", linewidth=1, label="y = x")
    for (px, py) in ((0, 1), (1, 0)):
        ax.plot(px, py, "o", color="black", markersize=4)
    ax.annotate("(0 ; 1)", (0, 1), textcoords="offset points", xytext=(-42, 4), fontsize=9)
    ax.annotate("(1 ; 0)", (1, 0), textcoords="offset points", xytext=(6, -14), fontsize=9)
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.axvline(0, color="gray", linewidth=0.8)
    ax.set_xlim(-3, 10)
    ax.set_ylim(-3, 10)
    ax.set_aspect("equal")
    ax.set_title("exp et ln : deux courbes symétriques par rapport à y = x", fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower right", fontsize=9)
    save(fig, "exp_ln.png")


def fig_growth() -> None:
    """§5: x⁵ against 1,1ˣ: the power leads for a long time, the exponential wins after about x = 299."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
    x = np.linspace(0, 60, 300)
    axes[0].plot(x, x**5 / 1e6, color=C[0], linewidth=2, label="x⁵")
    axes[0].plot(x, 1.1**x / 1e6, color=C[1], linewidth=2, label="1,1ˣ")
    axes[0].set_title("De 0 à 60 : x⁵ écrase 1,1ˣ", fontsize=10)
    axes[0].set_ylabel("en millions")
    x = np.linspace(1, 400, 400)
    axes[1].plot(x, 5 * np.log10(x), color=C[0], linewidth=2, label="log₁₀(x⁵)")
    axes[1].plot(x, x * np.log10(1.1), color=C[1], linewidth=2, label="log₁₀(1,1ˣ)")
    axes[1].axvline(299, color="black", linestyle=":", linewidth=1)
    axes[1].text(305, 2, "x ≈ 299", fontsize=9)
    axes[1].set_title("De 1 à 400, en logarithmes : 1,1ˣ finit par gagner", fontsize=10)
    for ax in axes:
        ax.set_xlabel("x")
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=9)
    fig.tight_layout()
    save(fig, "croissances.png")


def fig_log_scale() -> None:
    """§6: y = 3 × 2ᵗ for t = 0 to 12, on a linear and on a logarithmic y axis."""
    t = np.arange(0, 13)
    y = 3 * 2.0**t
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
    for ax, scale in zip(axes, ("linear", "log")):
        ax.plot(t, y, "o", color=C[0], markersize=5)
        ax.set_yscale(scale)
        ax.set_xlabel("t")
        ax.grid(True, which="both" if scale == "log" else "major", alpha=0.3)
    axes[0].set_title("Échelle linéaire : on ne voit que la fin", fontsize=10)
    axes[1].set_title("Échelle logarithmique : une droite", fontsize=10)
    axes[0].set_ylabel("y = 3 × 2ᵗ")
    fig.tight_layout()
    save(fig, "echelle_log.png")


def fig_sigmoid_tanh() -> None:
    """§7: σ(x) in ]0, 1[ and tanh(x) in ]−1, 1[."""
    x = np.linspace(-6, 6, 400)
    sigma = 1 / (1 + np.exp(-x))
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(x, sigma, color=C[0], linewidth=2, label="σ(x) = 1 / (1 + e⁻ˣ)")
    ax.plot(x, np.tanh(x), color=C[1], linewidth=2, label="tanh(x)")
    for level in (-1, 0, 1):
        ax.axhline(level, color="gray", linewidth=0.8, linestyle="--" if level else "-")
    ax.axvline(0, color="gray", linewidth=0.8)
    ax.plot(0, 0.5, "o", color=C[0], markersize=5)
    ax.annotate("σ(0) = 0,5", (0, 0.5), textcoords="offset points", xytext=(8, -12), fontsize=9)
    ax.set_xlabel("x")
    ax.set_ylim(-1.2, 1.2)
    ax.set_title("La sigmoïde va de 0 à 1, tanh de −1 à 1", fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=9)
    save(fig, "sigmoide_tanh.png")


def main() -> int:
    print(f"Figures of R6 -> {OUT.relative_to(ROOT)}")
    fig_powers()
    fig_exp_ln()
    fig_growth()
    fig_log_scale()
    fig_sigmoid_tanh()
    return 0


if __name__ == "__main__":
    sys.exit(main())
