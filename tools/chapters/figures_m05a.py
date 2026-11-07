#!/usr/bin/env python
"""Draw the figures of chapter M05a (used by Claude).

    python tools/chapters/figures_m05a.py

Writes small PNG files into chapitres/m05a_derivees_taylor/figures/: convexity (√(1 + x²) with a chord above and a
tangent below, and the inflection points of ln(1 + x²)), the extrema of x² e^(−x) on a closed interval, the Taylor polynomials of cos at 0,
Newton's method on e^x − 3, the representable numbers of a toy floating-point format, and log-sum-exp as a smooth
maximum. None comes from workbookIA 5 (x³ − 3x, x⁴ − 2x², the secants of exp, the error curve against the step h).
"""

from __future__ import annotations

import math
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

OUT = ROOT / "chapitres" / "m05a_derivees_taylor" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and not getattr(axis, "keep_labels", False):
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def convexity() -> None:
    """Left: √(1 + x²) is convex (a chord above, a tangent below). Right: ln(1 + x²) and its two inflection points."""
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 3.8))
    x = np.linspace(-3, 3, 400)
    left.plot(x, np.sqrt(1 + x ** 2), color=C[0], linewidth=2, label="f(x) = √(1 + x²)")
    left.plot(x, np.abs(x), color="gray", linewidth=1, linestyle=(0, (1, 2)), label="|x|")
    a, b = -2.0, 1.0
    fa, fb = math.sqrt(1 + a * a), math.sqrt(1 + b * b)
    left.plot([a, b], [fa, fb], "--", color=C[1], label="une corde (au-dessus)")
    left.plot([a, b], [fa, fb], "o", color=C[1])
    x0 = 1.5
    f0, s0 = math.sqrt(1 + x0 * x0), x0 / math.sqrt(1 + x0 * x0)
    left.plot(x, f0 + s0 * (x - x0), ":", color=C[2], linewidth=2, label="une tangente (au-dessous)")
    left.set(xlim=(-3, 3), ylim=(-0.5, 3.6), xlabel="x", title="Convexe : f'' > 0 partout")
    left.legend(fontsize=8, loc="upper center")
    left.grid(alpha=0.3)

    g = np.log1p(x ** 2)
    right.plot(x, g, color=C[0], linewidth=2, label="g(x) = ln(1 + x²)")
    inside = np.abs(x) <= 1
    right.fill_between(x, 0, g, where=inside, color=C[0], alpha=0.12, label="convexe sur [−1, 1]")
    right.plot([-1, 1], [math.log(2)] * 2, "o", color=C[3], label="points d'inflexion (g'' = 0)")
    right.set(xlim=(-3, 3), ylim=(-0.1, 2.5), xlabel="x", title="ln(1 + x²) : convexe sur [−1, 1] seulement")
    right.legend(fontsize=8, loc="upper center")
    right.grid(alpha=0.3)
    save(fig, "convexite.png")


def extrema() -> None:
    """x² e^(−x) on [−1, 4]: a local minimum that is global, a local maximum that is not, the global maximum at an end."""
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    x = np.linspace(-1, 4, 400)
    ax.plot(x, x ** 2 * np.exp(-x), color=C[0], linewidth=2, label="f(x) = x² e⁻ˣ")
    points = [(-1, math.e, "maximum global (au bord)", C[3]), (0, 0, "minimum local et global", C[2]),
              (2, 4 * math.exp(-2), "maximum local, pas global", C[1]), (4, 16 * math.exp(-4), "bord droit", "gray")]
    for px, py, label, color in points:
        ax.plot(px, py, "o", color=color, markersize=7, label=label)
    ax.axvline(-1, color="gray", linewidth=0.8, linestyle=":")
    ax.axvline(4, color="gray", linewidth=0.8, linestyle=":")
    ax.set(xlabel="x", title="Sur [−1 ; 4] : comparer les points critiques et les bords")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    save(fig, "extrema.png")


def taylor_cos() -> None:
    """cos and its Taylor polynomials of orders 2, 4 and 6 at 0: they hug the curve further and further."""
    fig, ax = plt.subplots(figsize=(6.8, 3.9))
    x = np.linspace(-4.5, 4.5, 500)
    ax.plot(x, np.cos(x), color="black", linewidth=2.5, label="cos x")
    for n, color in zip((2, 4, 6), (C[0], C[1], C[2])):
        poly = sum((-1) ** k * x ** (2 * k) / math.factorial(2 * k) for k in range(n // 2 + 1))
        ax.plot(x, poly, color=color, linewidth=1.6, label=f"P{n}, ordre {n}")
    ax.set(xlim=(-4.5, 4.5), ylim=(-2, 2), xlabel="x", title="Les polynômes de Taylor de cos en 0")
    ax.legend(fontsize=8, loc="lower center", ncol=4)
    ax.grid(alpha=0.3)
    save(fig, "taylor_cos.png")


def newton_ln3() -> None:
    """Newton's method on f(x) = e^x − 3 from x0 = 2: each tangent cuts the axis at the next value."""
    fig, ax = plt.subplots(figsize=(6.8, 4))
    x = np.linspace(0.8, 2.15, 300)
    ax.plot(x, np.exp(x) - 3, color=C[0], linewidth=2, label="f(x) = eˣ − 3")
    ax.axhline(0, color="black", linewidth=0.8)
    xk = 2.0
    for k in range(3):
        fx, slope = math.exp(xk) - 3, math.exp(xk)
        x_next = xk - fx / slope
        ax.plot([xk, xk], [0, fx], ":", color="gray", linewidth=1)
        ax.plot([xk, x_next], [fx, 0], "--", color=C[1], linewidth=1.4, label="tangentes" if k == 0 else None)
        ax.plot(xk, fx, "o", color=C[1], markersize=5)
        ax.annotate(f"x{k}", (xk, 0), xytext=(xk, -0.55), ha="center", fontsize=9)
        xk = x_next
    ax.plot(math.log(3), 0, "*", color=C[3], markersize=12, label="la racine ln 3")
    ax.set(xlim=(0.8, 2.15), ylim=(-1, 4.6), xlabel="x", title="Newton : suivre la tangente jusqu'à l'axe")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)
    save(fig, "newton.png")


def toy_floats() -> None:
    """The positive numbers of a toy format with 3 bits after the point: the gap doubles at each power of 2."""
    fig, ax = plt.subplots(figsize=(9, 1.9))
    values = sorted({(1 + m / 8) * 2.0 ** e for e in range(-1, 3) for m in range(8)})
    ax.plot(values, [0] * len(values), "|", color=C[0], markersize=22, markeredgewidth=2)
    for p in (0.5, 1, 2, 4):
        ax.annotate(french_number(p), (p, 0), xytext=(p, -0.9), ha="center", fontsize=9, color=C[3])
        ax.plot(p, 0, "|", color=C[3], markersize=28, markeredgewidth=2.5)
    ax.set(xlim=(0, 8.2), ylim=(-1.4, 1), yticks=[], xlabel="les nombres positifs d'un format jouet : un 1, puis 3 bits après la virgule, fois une puissance de 2",
           title="Entre deux puissances de 2, 8 nombres également espacés ; l'écart double à chaque puissance")
    ax.title.set_fontsize(10)
    save(fig, "flottants.png")


def lse_max() -> None:
    """log-sum-exp of (t, 0) and of (t, 0, 0) against max: a smooth maximum, between max and max + ln n."""
    fig, ax = plt.subplots(figsize=(6.8, 3.9))
    t = np.linspace(-5, 5, 400)
    ax.plot(t, np.maximum(t, 0), color="black", linewidth=2, label="max(t, 0)")
    ax.plot(t, np.logaddexp(t, 0), color=C[0], linewidth=2, label="LSE(t, 0) = ln(eᵗ + 1)")
    ax.plot(t, np.logaddexp(np.logaddexp(t, 0), 0), color=C[1], linewidth=2, label="LSE(t, 0, 0)")
    ax.plot(t, np.maximum(t, 0) + math.log(2), ":", color=C[0], label="max + ln 2")
    ax.plot(t, np.maximum(t, 0) + math.log(3), ":", color=C[1], label="max + ln 3")
    ax.set(xlabel="t", title="log-sum-exp : un maximum « adouci », jamais à plus de ln n au-dessus")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)
    save(fig, "lse.png")


def main() -> int:
    print(f"Figures of M05a → {OUT}")
    convexity()
    extrema()
    taylor_cos()
    newton_ln3()
    toy_floats()
    lse_max()
    return 0


if __name__ == "__main__":
    sys.exit(main())
