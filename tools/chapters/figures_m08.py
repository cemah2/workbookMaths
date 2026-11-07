#!/usr/bin/env python
"""Draw the figures of chapter M08 (used by Claude).

    python tools/chapters/figures_m08.py

Writes small PNG files into chapitres/m08_tests/figures/: the null law B(15, 1/2) of the fiche's example with its
one-sided p-value, the 126 differences of means of the fiche's permutation example, the power curve of the test
"K ≥ 12 out of 15", the exact coverage of the Wald and Wilson intervals for n = 20, and the family-wise error rate of
m independent tests with and without Bonferroni. None comes from workbookIA 8 (no penguins, no two models compared on
their disagreements, no maximum of K validation scores, no folds).
"""

from __future__ import annotations

import itertools
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402
from statistics import NormalDist  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m08_tests" / "figures"
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


def pmf(j: int, n: int, p: float) -> float:
    return math.comb(n, j) * p ** j * (1 - p) ** (n - j)


def null_law() -> None:
    """B(15, 1/2): the bars from 12 to 15 make the one-sided p-value 9/512."""
    n = 15
    ks = np.arange(n + 1)
    probs = np.array([pmf(k, n, 0.5) for k in ks])
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    colors = [C[3] if k >= 12 else C[0] for k in ks]
    ax.bar(ks, probs, color=colors, width=0.8)
    ax.axvline(11.5, color="gray", ls="--", lw=1)
    ax.text(12.0, 0.17, "P(K ≥ 12) = 9/512\n≈ 0,0176", color=C[3], fontsize=10)
    ax.set(xlabel="k, le nombre de votes pour la nouvelle version", ylabel="P(K = k) sous H0",
           title="La loi nulle B(15 ; 1/2) et la p-valeur unilatérale", xticks=ks[::1])
    save(fig, "loi_nulle.png")


def permutation() -> None:
    """The 126 differences of means of the fiche's example (5 plants with fertilizer, 4 without)."""
    fert, ctrl = [14.2, 15.1, 13.8, 16.0, 15.4], [13.1, 12.6, 14.0, 13.5]
    pooled = fert + ctrl
    observed = np.mean(fert) - np.mean(ctrl)
    diffs = []
    for idx in itertools.combinations(range(9), 5):
        a = [pooled[i] for i in idx]
        b = [pooled[i] for i in range(9) if i not in idx]
        diffs.append(np.mean(a) - np.mean(b))
    diffs = np.array(diffs)
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    bins = np.linspace(-1.9, 1.9, 39)
    ax.hist(diffs[diffs < observed - 1e-9], bins=bins, color=C[0], label="les autres répartitions")
    ax.hist(diffs[diffs >= observed - 1e-9], bins=bins, color=C[3], label="au moins aussi extrêmes (2 sur 126)")
    ax.axvline(observed, color="black", lw=1.5)
    ax.text(observed - 0.05, 5.6, "écart observé\n1,6 cm", fontsize=9, ha="right")
    ax.set(xlabel="écart des moyennes (engrais − témoin), en cm", ylabel="nombre de répartitions",
           title="La loi nulle obtenue en rebattant les groupes (126 répartitions)")
    ax.legend(fontsize=8, loc="upper left")
    save(fig, "permutation.png")


def power() -> None:
    """Power of the rule K ≥ 12 out of 15, as a function of the true p."""
    ps = np.linspace(0.3, 1.0, 141)
    power_values = [sum(pmf(j, 15, p) for j in range(12, 16)) for p in ps]
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    ax.plot(ps, power_values, color=C[0], lw=2)
    for p, label in [(0.5, "p = 1/2 : α ≈ 0,018"), (0.7, "p = 0,7 : 0,297"), (0.8, "p = 0,8 : 0,648")]:
        value = sum(pmf(j, 15, p) for j in range(12, 16))
        ax.plot(p, value, "o", color=C[3])
        ax.annotate(label, (p, value), textcoords="offset points", xytext=(-95 if p > 0.6 else 8, 8), fontsize=9)
    ax.set(xlabel="la vraie probabilité p de préférer la nouvelle version", ylabel="P(rejeter H0)",
           title="La puissance du test « K ≥ 12 sur 15 »", ylim=(0, 1.02))
    save(fig, "puissance.png")


def coverage(n: int, p: float, method: str, z: float) -> float:
    """Exact probability that the interval of the method contains p, for K ~ B(n, p)."""
    total = 0.0
    for k in range(n + 1):
        ph = k / n
        if method == "wald":
            half = z * math.sqrt(ph * (1 - ph) / n)
            low, high = ph - half, ph + half
        else:
            den = 1 + z * z / n
            center = (ph + z * z / (2 * n)) / den
            half = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
            low, high = center - half, center + half
        if low <= p <= high:
            total += pmf(k, n, p)
    return total


def wald_wilson() -> None:
    """Exact coverage of the 95 % Wald and Wilson intervals for n = 20."""
    z = NormalDist().inv_cdf(0.975)
    ps = np.linspace(0.005, 0.995, 397)
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    ax.plot(ps, [coverage(20, p, "wald", z) for p in ps], color=C[3], lw=1.2, label="Wald")
    ax.plot(ps, [coverage(20, p, "wilson", z) for p in ps], color=C[0], lw=1.2, label="Wilson")
    ax.axhline(0.95, color="gray", ls="--", lw=1)
    ax.set(xlabel="la vraie proportion p", ylabel="couverture réelle", ylim=(0.3, 1.0),
           title="Couverture des intervalles « à 95 % », n = 20")
    ax.legend(fontsize=9, loc="lower center")
    save(fig, "wald_wilson.png")


def multiple_comparisons() -> None:
    """Probability of at least one false positive among m independent tests at 5 %, with and without Bonferroni."""
    m = np.arange(1, 61)
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    ax.plot(m, 1 - 0.95 ** m, color=C[3], lw=2, label="chaque test au seuil 0,05")
    ax.plot(m, 1 - (1 - 0.05 / m) ** m, color=C[0], lw=2, label="Bonferroni : chaque test au seuil 0,05/m")
    ax.axhline(0.05, color="gray", ls="--", lw=1)
    ax.set(xlabel="nombre m de tests (toutes les hypothèses nulles vraies)", ylabel="P(au moins un faux positif)",
           title="Comparaisons multiples", ylim=(0, 1))
    ax.legend(fontsize=9, loc="center right")
    save(fig, "comparaisons_multiples.png")


def main() -> int:
    print(f"Figures of M08 in {OUT.relative_to(ROOT)}:")
    null_law()
    permutation()
    power()
    wald_wilson()
    multiple_comparisons()
    return 0


if __name__ == "__main__":
    sys.exit(main())
