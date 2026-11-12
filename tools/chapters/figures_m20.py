#!/usr/bin/env python
"""Draw the figures of chapter M20 (used by Claude).

    python tools/chapters/figures_m20.py

Writes small PNG files into chapitres/m20_tenseurs_normalisation/figures/: the C order of a (2, 3, 3) array and its
reshape into (3, 6); synthetic hourly temperatures of 4 stations over 7 days, of shape (4, 7, 24), and two of their
reductions; the centering of x = (3, 1) in the plane as an orthogonal projection on the line {v₁ + v₂ = 0}; the exact
laws, over the 32 possible samples, of the Horvitz-Thompson and naive estimators of the forest of the fiche
(y = (120, 40, 300, 90, 60), π = (0.3, 0.1, 0.9, 0.15, 0.3)); Euler's trajectories of the rotation x' = Jx over half a
turn in L = 6, 12 and 48 steps. The numbers are those of the fiche; none comes from workbookIA 20 (no network, no
layer, no mini-batch, no 20xx seed). The temperatures use the seed 5301.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from wbm import plot as wbplot  # noqa: E402

OUT = ROOT / "chapitres" / "m20_tenseurs_normalisation" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

FOREST_Y = np.array([120.0, 40.0, 300.0, 90.0, 60.0])     # §5: the trees of the 5 plots (total 610)
FOREST_PI = np.array([0.3, 0.1, 0.9, 0.15, 0.3])           # §5: their inclusion probabilities
STATIONS = ["station 0", "station 1", "station 2", "station 3"]


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


def temperatures() -> np.ndarray:
    """Synthetic hourly temperatures, shape (4 stations, 7 days, 24 hours): a mild station, a cold one, a warm one, a
    mountain one; a daily cycle (coldest near 4 h, warmest near 15 h), a cooler spell in the middle of the week and a
    little noise."""
    rng = np.random.default_rng(5301)
    base = np.array([12.0, 9.0, 15.0, 5.0])[:, None, None]
    swing = np.array([4.0, 3.0, 5.0, 6.0])[:, None, None]
    day = np.array([1.5, 1.0, -1.0, -2.5, -2.0, 0.0, 1.0])[None, :, None]
    hour = np.arange(24)[None, None, :]
    cycle = -np.cos(2 * np.pi * (hour - 3.5) / 24)
    return base + day + swing * cycle + rng.normal(0.0, 0.6, size=(4, 7, 24))


def c_order() -> None:
    """§1: the positions of a (2, 3, 3) array in C order, the file, and the reshape into (3, 6)."""
    shades = [C[0], C[1]]
    fig = plt.figure(figsize=(10.5, 5.2))
    top = fig.add_axes([0.02, 0.48, 0.96, 0.48])
    top.set_axis_off()
    top.set(xlim=(-0.5, 9.0), ylim=(-0.4, 3.8))
    for i0 in range(2):
        x0 = 0.6 + 4.2 * i0
        top.text(x0 + 1.5, 3.45, f"T[{i0}]  (i₀ = {i0})", ha="center", fontsize=11, color=shades[i0])
        for i1 in range(3):
            for i2 in range(3):
                p = (i0 * 3 + i1) * 3 + i2
                top.add_patch(Rectangle((x0 + i2, 2 - i1), 1, 1, fc=shades[i0], alpha=0.18 + 0.05 * i1, ec="0.3"))
                top.text(x0 + i2 + 0.5, 2.5 - i1, str(p), ha="center", va="center", fontsize=12)
        for i1 in range(3):
            top.text(x0 - 0.15, 2.5 - i1, f"i₁ = {i1}", ha="right", va="center", fontsize=8, color="0.35")
        for i2 in range(3):
            top.text(x0 + i2 + 0.5, -0.2, f"i₂ = {i2}", ha="center", fontsize=8, color="0.35")
    fig.suptitle("Forme (2, 3, 3) : la case (i₀, i₁, i₂) est à la position (3 i₀ + i₁) × 3 + i₂", fontsize=11,
                 y=1.02)
    bottom = fig.add_axes([0.02, 0.02, 0.96, 0.42])
    bottom.set_axis_off()
    bottom.set(xlim=(-0.5, 19.0), ylim=(-4.6, 1.6))
    bottom.text(-0.3, 1.25, "la file en mémoire (ordre C : le dernier indice varie le plus vite)", fontsize=10)
    for p in range(18):
        i0 = p // 9
        bottom.add_patch(Rectangle((p, 0), 1, 0.9, fc=shades[i0], alpha=0.3, ec="0.3"))
        bottom.text(p + 0.5, 0.45, str(p), ha="center", va="center", fontsize=10)
    bottom.text(-0.3, -0.75, "remodelée en (3, 6) : la même file, relue ligne par ligne", fontsize=10)
    for p in range(18):
        r, c = divmod(p, 6)
        bottom.add_patch(Rectangle((c + 0.0, -2.0 - r * 0.9), 1, 0.9, fc=shades[p // 9], alpha=0.3, ec="0.3"))
        bottom.text(c + 0.5, -1.55 - r * 0.9, str(p), ha="center", va="center", fontsize=10)
    bottom.text(7.0, -2.9, "aucun nombre ne bouge dans la file :\nseule la forme change (une transposition, elle, "
                "changerait l'ordre)", fontsize=9.5, va="center")
    save(fig, "ordre_c.png")


def reductions() -> None:
    """§2: station 0 as an image, the mean along the days (one hourly profile per station), the mean along the
    hours (one daily mean per station)."""
    T = temperatures()
    fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.0), gridspec_kw={"width_ratios": [1.25, 1, 1]})
    im = axes[0].imshow(T[0], aspect="auto", cmap="coolwarm", origin="upper")
    axes[0].set(xlabel="heure (axe 2)", ylabel="jour (axe 1)", title="T[0] : la station 0, forme (7, 24)")
    fig.colorbar(im, ax=axes[0], label="°C", fraction=0.05)
    fig.subplots_adjust(wspace=0.38)
    hours = np.arange(24)
    for s in range(4):
        axes[1].plot(hours, T.mean(axis=1)[s], marker=".", color=C[s], label=STATIONS[s])
    axes[1].set(xlabel="heure", ylabel="°C", title="T.mean(axis=1) : forme (4, 24)\nun profil horaire par station")
    axes[1].legend(fontsize=8, ncol=2)
    days = np.arange(7)
    for s in range(4):
        axes[2].plot(days, T.mean(axis=2)[s], marker="o", color=C[s], label=STATIONS[s])
    axes[2].set(xlabel="jour", ylabel="°C", title="T.mean(axis=2) : forme (4, 7)\nune moyenne par station et par jour")
    for ax in axes[1:]:
        ax.grid(alpha=0.25)
    save(fig, "reductions.png")


def centering() -> None:
    """§4: in the plane, x = (3, 1) = x̄1 + Cx; every x + b1 has the same centered vector Cx."""
    x = np.array([3.0, 1.0])
    mean_part = np.full(2, x.mean())
    centered = x - mean_part
    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    t = np.linspace(-1.5, 4.6, 2)
    ax.plot(t, t, color=C[0], lw=1.6)
    ax.text(4.0, 4.25, "droite engendrée par 1 = (1, 1)", color=C[0], fontsize=9.5, ha="right")
    ax.plot(t, -t, color=C[1], lw=1.6)
    ax.text(-1.4, 1.65, "H = {v₁ + v₂ = 0}", color=C[1], fontsize=9.5)
    ax.plot(x[0] + (t - 1.5), x[1] + (t - 1.5), color="0.55", lw=1, ls="--")
    ax.text(4.3, 2.05, "x + b1 :\nmême Cx", color="0.4", fontsize=9, ha="center")
    for start, vec, color, label, where in (((0, 0), x, C[2], "x = (3, 1)", (3.05, 0.75)),
                                            ((0, 0), mean_part, C[0], "x̄1 = (2, 2)", (1.0, 2.15)),
                                            ((0, 0), centered, C[1], "Cx = (1, −1)", (1.05, -1.05)),
                                            (mean_part, centered, C[1], None, None)):
        ax.add_patch(FancyArrowPatch(start, np.asarray(start) + vec, arrowstyle="-|>", mutation_scale=14,
                                     color=color, lw=1.9, zorder=4, ls="-" if label else ":"))
        if label:
            ax.text(*where, label, color=color, fontsize=10)
    s = 0.22
    corner = mean_part
    u, v = np.array([1, 1]) / np.sqrt(2), np.array([1, -1]) / np.sqrt(2)
    ax.plot(*np.array([corner - s * u, corner - s * u + s * v, corner + s * v]).T, color="0.3", lw=1)
    ax.set(xlim=(-1.6, 4.8), ylim=(-1.9, 4.5), xlabel="v₁", ylabel="v₂")
    ax.set_aspect("equal")
    ax.axhline(0, color="0.85", lw=0.8, zorder=0)
    ax.axvline(0, color="0.85", lw=0.8, zorder=0)
    ax.set_title("Centrer x, c'est le projeter orthogonalement sur H :\nx = x̄1 + Cx, deux vecteurs orthogonaux",
                 fontsize=10.5)
    save(fig, "centrage.png")


def horvitz_thompson() -> None:
    """§5: the exact laws of the two estimators over the 32 samples of the forest."""
    rows = []
    for inc in itertools.product([False, True], repeat=5):
        inc = np.array(inc)
        prob = float(np.prod(np.where(inc, FOREST_PI, 1 - FOREST_PI)))
        ht = float(np.sum(FOREST_Y[inc] / FOREST_PI[inc]))
        naive = float(5 * FOREST_Y[inc].mean()) if inc.any() else 0.0
        rows.append((prob, ht, naive))
    probs = np.array([r[0] for r in rows])
    total = FOREST_Y.sum()
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 4.2), sharey=True)
    for ax, k, name, color in ((axes[0], 1, "Horvitz-Thompson : Σ y_i / π_i", C[0]),
                               (axes[1], 2, "naïf : N × moyenne de l'échantillon", C[3])):
        values = np.array([r[k] for r in rows])
        support = {}
        for v, p in zip(np.round(values, 6), probs):
            support[v] = support.get(v, 0.0) + p
        xs = np.array(sorted(support))
        ps = np.array([support[v] for v in xs])
        ax.vlines(xs, 0, ps, color=color, lw=3)
        mean = float(np.sum(xs * ps))
        ax.axvline(total, color="0.2", ls="--", lw=1.4, label=f"vrai total : {french_number(total)}")
        ax.axvline(mean, color=color, ls=":", lw=2, label=f"moyenne de l'estimateur : {mean:.0f}")
        ax.set(xlabel="estimation du nombre d'arbres", title=name)
        ax.legend(fontsize=9)
        ax.grid(alpha=0.25)
    axes[0].set_ylabel("probabilité")
    fig.suptitle("Les 32 échantillons possibles de la forêt, pondérés par leur probabilité", fontsize=11)
    save(fig, "horvitz_thompson.png")


def euler_rotation() -> None:
    """§6: the rotation x' = Jx over half a turn (T = π), exact circle and Euler in L = 6, 12, 48 steps."""
    J = np.array([[0.0, -1.0], [1.0, 0.0]])
    T = np.pi
    fig, ax = plt.subplots(figsize=(6.6, 5.2))
    angles = np.linspace(0, T, 200)
    ax.plot(np.cos(angles), np.sin(angles), color="0.2", lw=2, label="trajectoire exacte (rayon 1)")
    for L, color in ((6, C[3]), (12, C[1]), (48, C[0])):
        h = T / L
        x = np.array([1.0, 0.0])
        path = [x]
        for _ in range(L):
            x = x + h * (J @ x)
            path.append(x)
        path = np.array(path)
        radius = (1 + h ** 2) ** (L / 2)
        ax.plot(*path.T, marker="o", ms=3.5, color=color,
                label=f"Euler, L = {L} pas : rayon final {french_number(round(radius, 3))}")
    ax.plot([1], [0], "ks", ms=6)
    ax.text(1.04, -0.12, "départ (1, 0)", fontsize=9)
    ax.set_aspect("equal")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8.5, loc="lower left")
    ax.set(xlabel="x₁", ylabel="x₂", xlim=(-2.15, 1.55), ylim=(-0.75, 1.75))
    ax.set_title("x' = Jx (une rotation) sur un demi-tour, T = π :\n"
                 "à horizon fixé, Euler s'écarte de moins en moins du cercle quand L grandit", fontsize=10)
    save(fig, "euler_rotation.png")


def main() -> int:
    print(f"Figures M20 → {OUT.relative_to(ROOT)}")
    c_order()
    reductions()
    centering()
    horvitz_thompson()
    euler_rotation()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
