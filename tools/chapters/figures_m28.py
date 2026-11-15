#!/usr/bin/env python
"""Draw the figures of chapter M28 (used by Claude).

    python tools/chapters/figures_m28.py

Writes small PNG files into chapitres/m28_gram_echantillonnage/figures/:
- a map recovered from distances: seven sensors in a field (seed 6591), the positions given by the eigenvectors of
  the double-centered matrix of squared distances (a rotation of the true map, possibly with a reflection), and its
  eigenvalues (two positive, the others zero);
- what projected ascent finds: the squared distance to c = (4, 6) in a square hangar [0, 10]² (each start ends at
  the vertex of its quadrant, every vertex is a local maximum), and the renormalized ascent on xᵀAx over the unit circle,
  A = [[5, 2], [2, 8]], step η = 1/4 (the power method on I + 2ηA, towards (1, 2)/√5);
- a noisy step (seed 6592) smoothed by the squared total variation, (I + τL)x = y, and by the total variation in
  absolute value (Rudin, Osher and Fatemi), which keeps the edge;
- striped patterns cos(2π(f₁i + f₂j)) on a circular 40 × 40 grid and the ratio total variation / energy,
  4 sin²(πf₁) + 4 sin²(πf₂), over the frequency square [0, 1/2]²;
- the gain (1 + 2 cos ω)/3 of a moving average of three cases, and a signal of periods 24 and 3 whose period-3 part
  it erases;
- the tempered laws of a car diagnosis p = (0.05, 0.37, 0.12, 0.27, 0.19) at T = 1/4, 1, 4 and ∞, and the entropy
  against T;
- the smallest set of mass at least 0.7 of the same law at T = 1/4, 1 and 4 (1, 3 and 4 outcomes);
- the rho of the iteration "sum of the squares of the digits" from 15 (preperiod 3, period 8), with two other tails.
The numbers are those of the fiche; none comes from workbookIA 28, B4 or its checkpoint VI (no network, image of a
dataset, activation, word or logit, no 28xx seed).
"""

from __future__ import annotations

import math
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

OUT = ROOT / "chapitres" / "m28_gram_echantillonnage" / "figures"
C = wbplot.CATEGORICAL
DPI = 110

# §2: seven sensors in a field of 100 m × 60 m
SEED_SENSORS, N_SENSORS = 6591, 7
# §3: squared distance to c on the unit square; renormalized ascent on xᵀAx
C_DRONE, SIDE = np.array([4.0, 6.0]), 10.0
STARTS = [(5.5, 5.0), (3.0, 8.0), (6.0, 7.5), (2.5, 4.5)]
ETA_BOX, STEPS_BOX = 0.12, 25
A_QUAD, ETA_SPHERE, X0_SPHERE, STEPS_SPHERE = np.array([[5.0, 2.0], [2.0, 8.0]]), 0.25, np.array([1.0, 0.0]), 7
# §4: a noisy step; striped patterns; a moving average
SEED_NOISE, N_SIGNAL, SIGMA, TAU_SQ, LAM_ABS = 6592, 80, 0.12, 6.0, 0.3
PATTERNS = [(0.0, 1 / 8), (0.0, 1 / 5), (0.15, 0.2), (0.5, 0.5)]
GRID, CROP = 40, 16
# §5: a car that does not start: a mechanic's diagnosis (causes 0 to 4)
CAUSES = ["démarreur", "batterie", "carburant", "allumage", "électronique"]
P_DIAG = np.array([0.05, 0.37, 0.12, 0.27, 0.19])
MASS = 0.7


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def fr(value: float, digits: int) -> str:
    return f"{value:.{digits}f}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            keep = getattr(ax, "keep_ticks", False)                        # category labels stay as they are
            keep = keep or (axis is ax.xaxis and getattr(ax, "keep_ticks_x", False))
            if axis.get_scale() == "linear" and ax.axison and not keep:
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


# --------------------------------------------------------------------------------------------------------- §2
def double_centered(D2: np.ndarray) -> np.ndarray:
    n = len(D2)
    J = np.eye(n) - np.ones((n, n)) / n
    return -0.5 * J @ D2 @ J


def gram_map() -> None:
    """§2: positions recovered from distances, up to an isometry, and the eigenvalues that say the dimension."""
    rng = np.random.default_rng(SEED_SENSORS)
    P = np.column_stack([rng.uniform(0, 100, N_SENSORS), rng.uniform(0, 60, N_SENSORS)])
    D2 = ((P[:, None, :] - P[None, :, :]) ** 2).sum(-1)
    G = double_centered(D2)
    lam, Q = np.linalg.eigh(G)
    lam, Q = lam[::-1], Q[:, ::-1]
    X = Q[:, :2] * np.sqrt(lam[:2])
    for k in range(2):                                            # the sign convention of points_from_gram
        first = X[np.abs(X[:, k]) > 1e-8, k][0]
        X[:, k] *= np.sign(first)
    Pc = P - P.mean(0)
    U, _, Vt = np.linalg.svd(X.T @ Pc)                          # only to report what the isometry is
    R = U @ Vt
    angle = math.degrees(math.atan2(R[1, 0], R[0, 0]))
    D2_back = ((X[:, None, :] - X[None, :, :]) ** 2).sum(-1)
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3), gridspec_kw={"width_ratios": [1.35, 1.1, 0.9]})
    ax = axes[0]
    ax.scatter(P[:, 0], P[:, 1], s=55, color=C[0], zorder=3)
    for i, (x, y) in enumerate(P):
        ax.annotate(str(i + 1), (x, y), textcoords="offset points", xytext=(6, 5), fontsize=10)
    ax.add_patch(Rectangle((0, 0), 100, 60, fill=False, ec="0.5", lw=1, ls="--"))
    ax.set(xlim=(-5, 105), ylim=(-5, 65), aspect="equal", xlabel="est (m)", ylabel="nord (m)",
           title="Les capteurs sur le terrain")
    ax = axes[1]
    ax.scatter(X[:, 0], X[:, 1], s=55, color=C[1], zorder=3)
    for i, (x, y) in enumerate(X):
        ax.annotate(str(i + 1), (x, y), textcoords="offset points", xytext=(6, 5), fontsize=10)
    ax.axhline(0, color="0.6", lw=0.8)
    ax.axvline(0, color="0.6", lw=0.8)
    ax.set(aspect="equal", xlabel="colonne 1 : √λ₁ q₁ (m)", ylabel="colonne 2 : √λ₂ q₂ (m)",
           title="Retrouvés à partir des seules distances")
    ax = axes[2]
    ax.bar(range(1, N_SENSORS + 1), lam, color=[C[1]] * 2 + ["0.6"] * (N_SENSORS - 2))
    for k, v in enumerate(lam[:2]):
        ax.text(k + 1, v, f"{v:,.0f}".replace(",", " "), ha="center", va="bottom", fontsize=9)
    ax.set(xlabel="rang k", ylabel="λₖ (m²)", title="Valeurs propres de −½ J D⁽²⁾ J")
    ax.set_xticks(range(1, N_SENSORS + 1))
    fig.tight_layout(w_pad=2.5)
    save(fig, "gram_carte.png")
    print(f"    positions {np.round(P, 1).tolist()}")
    print(f"    eigenvalues {np.round(lam, 2).tolist()}; det R = {np.linalg.det(R):+.0f}, angle {angle:.1f}°; "
          f"max distance error {np.abs(D2_back - D2).max():.2e}")


# --------------------------------------------------------------------------------------------------------- §3
def box_path(start) -> np.ndarray:
    x = np.array(start, dtype=float)
    path = [x.copy()]
    for _ in range(STEPS_BOX):
        x = np.clip(x + ETA_BOX * 2 * (x - C_DRONE), 0.0, SIDE)
        path.append(x.copy())
    return np.array(path)


def sphere_path() -> np.ndarray:
    x = X0_SPHERE / np.linalg.norm(X0_SPHERE)
    path = [x]
    for _ in range(STEPS_SPHERE):
        y = x + ETA_SPHERE * 2 * A_QUAD @ x
        x = y / np.linalg.norm(y)
        path.append(x)
    return np.array(path)


def ascent() -> None:
    """§3: projected ascent of a convex function ends at a vertex; renormalized ascent is the power method."""
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.0))
    ax = axes[0]
    g = np.linspace(0, SIDE, 201)
    XX, YY = np.meshgrid(g, g)
    F = (XX - C_DRONE[0]) ** 2 + (YY - C_DRONE[1]) ** 2
    cs = ax.contourf(XX, YY, F, levels=14, cmap=wbplot.sequential_cmap(), alpha=0.85)
    ax.axvline(C_DRONE[0], color="0.35", lw=0.9, ls=":")
    ax.axhline(C_DRONE[1], color="0.35", lw=0.9, ls=":")
    ax.plot(*C_DRONE, "x", color="black", ms=9, mew=2)
    ax.annotate("c", C_DRONE, textcoords="offset points", xytext=(6, 4), fontsize=11)
    for k, s in enumerate(STARTS):
        path = box_path(s)
        ax.plot(path[:, 0], path[:, 1], "-o", color=C[2 + k % 4], ms=3, lw=1.4)
        ax.plot(*s, "s", color=C[2 + k % 4], ms=6)
    for vx in (0, SIDE):
        for vy in (0, SIDE):
            val = (vx - C_DRONE[0]) ** 2 + (vy - C_DRONE[1]) ** 2
            ax.annotate(f"{val:g} m²", (vx, vy), textcoords="offset points", fontsize=10.5, fontweight="bold",
                        xytext=(-44 if vx else 6, 6 if vy == 0 else -16),
                        bbox={"boxstyle": "round,pad=0.15", "fc": "white", "ec": "none", "alpha": 0.85})
    ax.set(xlim=(-0.2, SIDE + 0.2), ylim=(-0.2, SIDE + 0.2), aspect="equal", xlabel="x₁ (m)", ylabel="x₂ (m)",
           title="‖x − c‖² dans le hangar : chaque montée finit à un sommet")
    ax.grid(False)
    fig.colorbar(cs, ax=ax, fraction=0.046, pad=0.04)
    ax = axes[1]
    t = np.linspace(0, 2 * math.pi, 400)
    ax.plot(np.cos(t), np.sin(t), color="0.6", lw=1)
    lam, Q = np.linalg.eigh(A_QUAD)
    for v, lab, col in ((Q[:, 1], "λ = 9 : (1, 2)/√5", C[1]), (Q[:, 0], "λ = 4 : (2, −1)/√5", "0.5")):
        ax.plot([-1.25 * v[0], 1.25 * v[0]], [-1.25 * v[1], 1.25 * v[1]], ls="--", lw=1.2, color=col, label=lab)
    path = sphere_path()
    ax.plot(path[:, 0], path[:, 1], "o", color=C[0], ms=6, zorder=4)
    for k, (x, y) in enumerate(path[:5]):
        ax.annotate(f"x{chr(0x2080 + k)}", (x, y), textcoords="offset points", xytext=(8, -4), fontsize=10)
    ax.set(xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), aspect="equal", xlabel="x₁", ylabel="x₂",
           title="Montée renormalisée sur xᵀAx : la méthode de la puissance")
    ax.legend(loc="upper left", fontsize=9)
    fig.tight_layout(w_pad=3)
    save(fig, "montee.png")
    ends = [tuple(box_path(s)[-1]) for s in STARTS]
    print(f"    box ends {ends}; sphere iterates {np.round(path, 4).tolist()}")


# --------------------------------------------------------------------------------------------------------- §4
def path_laplacian(n: int) -> np.ndarray:
    L = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    L[0, 0] = L[-1, -1] = 1
    return L


def tv_abs_denoise(y: np.ndarray, lam: float, iters: int = 20000) -> np.ndarray:
    """min ½‖x − y‖² + lam Σ|x_{j+1} − x_j|, by projected gradient on the dual (|z_j| ≤ lam), x = y − Dᵀz."""
    n = len(y)
    D = np.diff(np.eye(n), axis=0)
    z = np.zeros(n - 1)
    for _ in range(iters):
        x = y - D.T @ z
        z = np.clip(z + 0.25 * D @ x, -lam, lam)
    return y - D.T @ z


def step_smoothing() -> None:
    """§4: the square spreads the step (it prefers ramps), the absolute value keeps it."""
    rng = np.random.default_rng(SEED_NOISE)
    j = np.arange(N_SIGNAL)
    clean = (j >= N_SIGNAL // 2).astype(float)
    y = clean + SIGMA * rng.standard_normal(N_SIGNAL)
    x_sq = np.linalg.solve(np.eye(N_SIGNAL) + TAU_SQ * path_laplacian(N_SIGNAL), y)
    x_abs = tv_abs_denoise(y, LAM_ABS)
    fig, ax = plt.subplots(figsize=(9.6, 4.4))
    ax.plot(j, y, "o", color="0.6", ms=3.2, label="mesures bruitées")
    ax.plot(j, clean, color="black", lw=1, ls="--", label="la marche sans bruit")
    ax.plot(j, x_sq, color=C[0], lw=2.2, label=f"variation totale au carré : (I + τL)x = y, τ = {TAU_SQ:g}")
    ax.plot(j, x_abs, color=C[1], lw=2.2, label="variation totale en valeur absolue")
    ax.set(xlabel="case j", ylabel="valeur", title="Lisser une marche : le carré l'étale, la valeur absolue la garde")
    ax.legend(fontsize=9, loc="upper left")
    save(fig, "marche_lissee.png")
    print(f"    squared: x[38..41] = {np.round(x_sq[38:42], 3).tolist()}; absolute: {np.round(x_abs[38:42], 3).tolist()}")


def stripes() -> None:
    """§4: periodic patterns are eigenvectors of the circular Laplacian: TV / energy = 4 sin²(πf₁) + 4 sin²(πf₂)."""
    i, jj = np.meshgrid(np.arange(GRID), np.arange(GRID), indexing="ij")
    fig = plt.figure(figsize=(12.0, 5.6))
    ratios = []
    for k, (f1, f2) in enumerate(PATTERNS):
        x = np.cos(2 * math.pi * (f1 * i + f2 * jj))
        tv = ((np.roll(x, -1, 0) - x) ** 2).sum() + ((np.roll(x, -1, 1) - x) ** 2).sum()   # circular grid
        ratio = tv / (x ** 2).sum()
        ratios.append(ratio)
        row, col = divmod(k, 2)
        ax = fig.add_axes([0.02 + 0.235 * col, 0.53 - 0.47 * row, 0.2, 0.36])
        ax.imshow(x[:CROP, :CROP], cmap="gray", vmin=-1, vmax=1, interpolation="nearest")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(False)
        ax.set_title(f"f = ({french_number(round(f1, 4))} ; {french_number(round(f2, 4))}) : "
                     f"VT / énergie = {fr(ratio, 3)}", fontsize=9.5)
    ax = fig.add_axes([0.55, 0.1, 0.36, 0.8])
    f = np.linspace(0, 0.5, 201)
    F1, F2 = np.meshgrid(f, f, indexing="ij")
    R = 4 * np.sin(math.pi * F1) ** 2 + 4 * np.sin(math.pi * F2) ** 2
    cs = ax.contourf(F2, F1, R, levels=16, cmap=wbplot.sequential_cmap())
    ax.contour(F2, F1, R, levels=[1, 2, 4, 6], colors="white", linewidths=0.7)
    for (f1, f2), r in zip(PATTERNS, ratios):
        ax.plot(f2, f1, "o", color=wbplot.BAD, ms=7, mec="white")
        ax.annotate(fr(r, 2), (f2, f1), textcoords="offset points", xytext=(-26 if f2 > 0.4 else 7, 6),
                    fontsize=9.5, color="black",
                    bbox={"boxstyle": "round,pad=0.15", "fc": "white", "ec": "none", "alpha": 0.8})
    ax.set(xlabel="f₂ (cycles par case, le long des colonnes j)", ylabel="f₁ (le long des lignes i)",
           title="4 sin²(πf₁) + 4 sin²(πf₂)", aspect="equal")
    ax.grid(False)
    fig.colorbar(cs, ax=ax, fraction=0.046, pad=0.04)
    fig.text(0.245, 0.96, f"Quatre motifs ({CROP} × {CROP} cases d'une grille circulaire de {GRID} × {GRID})",
             ha="center", fontsize=11, fontweight="bold")
    save(fig, "motifs_raies.png")
    print(f"    ratios {np.round(ratios, 4).tolist()}")


def moving_average() -> None:
    """§4: the gain of the moving average of three cases, and a period-3 component erased."""
    f = np.linspace(0, 0.5, 301)
    gain = (1 + 2 * np.cos(2 * math.pi * f)) / 3
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.3), gridspec_kw={"width_ratios": [1, 1.25]})
    ax = axes[0]
    ax.plot(f, gain, color=C[0], lw=2.2)
    ax.axhline(0, color="0.4", lw=0.8)
    for ff, lab, off in ((1 / 8, "période 8 : (1 + √2)/3 ≈ 0,805", (8, 6)), (1 / 3, "période 3 : 0", (8, 8)),
                         (0.5, "f = ½ : −1/3", (-92, 22))):
        g = (1 + 2 * math.cos(2 * math.pi * ff)) / 3
        ax.plot(ff, g, "o", color=wbplot.BAD, ms=6)
        ax.annotate(lab, (ff, g), textcoords="offset points", xytext=off, fontsize=9.5)
    ax.set(xlabel="fréquence f (cycles par case)", ylabel="gain (1 + 2 cos ω)/3",
           title="Gain d'une moyenne mobile de trois cases", xlim=(0, 0.5), ylim=(-0.45, 1.08))
    ax = axes[1]
    n = 48
    j = np.arange(n)
    slow, fast = np.cos(2 * math.pi * j / 24), 0.5 * np.cos(2 * math.pi * j / 3)
    x = slow + fast
    y = (np.roll(x, 1) + x + np.roll(x, -1)) / 3                # circular: the signal closes on itself
    g24 = (1 + 2 * math.cos(2 * math.pi / 24)) / 3
    ax.plot(j, x, "-o", color="0.55", ms=3, lw=1, label="signal : périodes 24 et 3")
    ax.plot(j, y, "-", color=C[0], lw=2.2, label="moyenne mobile de trois cases")
    ax.plot(j, g24 * slow, ":", color="black", lw=1.4, label=f"{fr(g24, 3)} × la composante de période 24")
    ax.set(xlabel="case j (signal refermé en anneau, 48 cases)", ylabel="valeur",
           title="La période 3 disparaît, la période 24 passe", ylim=(-1.75, 2.75))
    ax.legend(fontsize=9, loc="upper center", ncol=1)
    fig.tight_layout(w_pad=3)
    save(fig, "gain_moyenne.png")
    print(f"    gain at 1/24 = {g24:.4f}; max |y - g24 slow| = {np.abs(y - g24 * slow).max():.2e}")


# --------------------------------------------------------------------------------------------------------- §5
def temper(p: np.ndarray, T: float) -> np.ndarray:
    if T == 0:
        q = (p == p.max()).astype(float)
    elif math.isinf(T):
        q = (p > 0).astype(float)
    else:
        q = np.where(p > 0, np.exp((np.log(np.where(p > 0, p, 1)) - math.log(p.max())) / T), 0.0)
    return q / q.sum()


def entropy(q: np.ndarray) -> float:
    q = q[q > 0]
    return float(-(q * np.log(q)).sum())


def temperature() -> None:
    """§5: tempered laws of the diagnosis, and the entropy that increases with T."""
    temps = [(0.25, "T = 1/4"), (1.0, "T = 1"), (4.0, "T = 4"), (math.inf, "T = ∞")]
    fig, axes = plt.subplots(1, 2, figsize=(12.4, 4.4), gridspec_kw={"width_ratios": [1.25, 1]})
    ax = axes[0]
    width = 0.2
    for k, (T, lab) in enumerate(temps):
        q = temper(P_DIAG, T)
        ax.bar(np.arange(5) + (k - 1.5) * width, q, width, color=C[k], label=lab)
    ax.set_xticks(range(5), [f"{i} : {c}" for i, c in enumerate(CAUSES)])
    ax.keep_ticks_x = True
    ax.set(ylabel="probabilité", title="La loi du diagnostic à quatre températures", ylim=(0, 0.82))
    ax.legend(fontsize=9.5)
    ax = axes[1]
    Ts = np.logspace(-1.6, 2, 300)
    H = [entropy(temper(P_DIAG, T)) for T in Ts]
    ax.semilogx(Ts, H, color=C[0], lw=2.2)
    ax.axhline(math.log(5), color="0.4", ls=":", lw=1.2)
    ax.text(0.03, math.log(5) + 0.03, "ln 5 ≈ 1,609 (uniforme sur les 5 causes)", fontsize=9, color="0.3")
    for T, lab in temps[:3]:
        h = entropy(temper(P_DIAG, T))
        ax.plot(T, h, "o", color=wbplot.BAD, ms=6)
        ax.annotate(f"{lab} : {fr(h, 3)}", (T, h), textcoords="offset points", xytext=(8, -14), fontsize=9.5)
    ax.set(xlabel="température T (échelle logarithmique)", ylabel="entropie (nats)",
           title="L'entropie croît avec T", ylim=(0, 1.75))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _p: french_number(v)))
    fig.tight_layout(w_pad=3)
    save(fig, "temperature.png")
    for T, lab in temps:
        q = temper(P_DIAG, T)
        print(f"    {lab}: {np.round(q, 4).tolist()} H = {entropy(q):.4f}")


def smallest_mass(q: np.ndarray, mass: float) -> np.ndarray:
    order = np.argsort(-q, kind="stable")
    cum = np.cumsum(q[order])
    k = int(np.searchsorted(cum, mass - 1e-9)) + 1
    return order[:k]


def top_p() -> None:
    """§5: the smallest set of mass ≥ 0.7 shrinks when the law is cooled, grows when it is heated."""
    fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.3), sharey=True)
    for ax, (T, lab) in zip(axes, ((0.25, "T = 1/4"), (1.0, "T = 1"), (4.0, "T = 4"))):
        q = temper(P_DIAG, T)
        order = np.argsort(-q, kind="stable")
        kept = set(smallest_mass(q, MASS).tolist())
        cols = [C[0] if i in kept else "0.75" for i in order]
        ax.bar(range(5), q[order], color=cols)
        cum = np.cumsum(q[order])
        ax.step(np.arange(5), cum, where="mid", color="black", lw=1.4, label="probabilité cumulée")
        ax.plot(np.arange(5), cum, "o", color="black", ms=3.5)
        ax.axhline(MASS, color=wbplot.BAD, ls="--", lw=1.2, label="m = 0,7")
        ax.set_xticks(range(5), [f"{i}\n{CAUSES[i]}" for i in order], fontsize=9)
        ax.keep_ticks_x = True
        ax.set(title=f"{lab} : {len(kept)} cause{'s' if len(kept) > 1 else ''} gardée{'s' if len(kept) > 1 else ''}",
               ylim=(0, 1.05))
        for k, v in enumerate(cum):
            ax.text(k, v + 0.025, fr(v, 3) if T != 1.0 else fr(v, 2), ha="center", fontsize=8.5)
    axes[0].set_ylabel("probabilité (causes triées)")
    axes[0].legend(fontsize=9, loc="center right")
    fig.tight_layout(w_pad=1.5)
    save(fig, "top_p.png")
    for T in (0.25, 1.0, 4.0, math.inf):
        q = temper(P_DIAG, T)
        print(f"    T = {T}: kept {smallest_mass(q, MASS).tolist()}, cumulative {np.round(np.cumsum(np.sort(q)[::-1]), 4).tolist()}")


# --------------------------------------------------------------------------------------------------------- §6
def digits_squares(n: int) -> int:
    return sum(int(c) ** 2 for c in str(n))


def rho() -> None:
    """§6: the orbit of 15 under the sum of the squares of the digits: a tail of 3, a cycle of 8."""
    orbit = [15]
    while orbit.count(orbit[-1]) < 2:
        orbit.append(digits_squares(orbit[-1]))
    first = orbit.index(orbit[-1])
    tail, cycle = orbit[:first], orbit[first:-1]
    mu, lam = len(tail), len(cycle)
    fig, ax = plt.subplots(figsize=(9.2, 5.6))
    R0 = 1.0
    pos = {}
    for k, v in enumerate(cycle):                                # the cycle on a circle, 16 at the bottom
        a = -math.pi / 2 - 2 * math.pi * k / lam
        pos[v] = (R0 * math.cos(a), R0 * math.sin(a) + 0.2)
    entry = np.array(pos[cycle[0]])
    for k, v in enumerate(reversed(tail)):                        # the tail goes down from the cycle
        pos[v] = (entry[0] - 0.05 * (k + 1), entry[1] - 0.62 * (k + 1))
    others = [[3, 9, 81, 65, 61], [11, 2]]                        # two other tails (61 → 37, 2 → 4)
    for t_idx, chain in enumerate(others):
        target = digits_squares(chain[-1])
        tx, ty = pos[target]
        ang = math.atan2(ty - 0.2, tx)
        for k, v in enumerate(reversed(chain)):
            pos[v] = (tx + (0.55 * (k + 1)) * math.cos(ang), ty + (0.55 * (k + 1)) * math.sin(ang) - 0.12 * k * t_idx)

    def arrow(u, v, color, lw):
        ax.add_patch(FancyArrowPatch(pos[u], pos[v], arrowstyle="-|>", mutation_scale=13, lw=lw, color=color,
                                     shrinkA=13, shrinkB=13, connectionstyle="arc3,rad=0.12"))

    for chain in others:
        seq = chain + [digits_squares(chain[-1])]
        for u, v in zip(seq[:-1], seq[1:]):
            arrow(u, v, "0.7", 1.0)
    for u, v in zip(orbit[:-1], orbit[1:]):
        arrow(u, v, C[1] if u in tail else C[0], 1.6)
    for v, (x, y) in pos.items():
        on_orbit = v in orbit
        col = C[1] if v in tail else (C[0] if v in cycle else "0.6")
        ax.add_patch(plt.Circle((x, y), 0.15, color="white", ec=col, lw=2 if on_orbit else 1, zorder=3))
        ax.text(x, y, str(v), ha="center", va="center", fontsize=9.5 if on_orbit else 8.5, zorder=4,
                color="black" if on_orbit else "0.45", fontweight="bold" if v == 15 else None)
    ax.text(pos[15][0] + 0.2, pos[15][1], "départ u₀ = 15", va="center", fontsize=10)
    ax.text(entry[0] + 1.3, entry[1] + 0.5, f"cycle : période λ = {lam}", color=C[0], fontsize=11)
    ax.text(pos[26][0] + 0.2, pos[26][1], f"queue : prépériode μ = {mu}", color=C[1], fontsize=11, va="center")
    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    ax.set(xlim=(min(xs) - 0.4, max(xs) + 0.9), ylim=(min(ys) - 0.3, max(ys) + 0.3), aspect="equal")
    ax.axis("off")
    ax.set_title("u ↦ somme des carrés des chiffres de u : un ρ", fontsize=12)
    save(fig, "rho.png")
    print(f"    orbit {orbit}; mu = {mu}, lambda = {lam}")


def main() -> int:
    print(f"Figures M28 → {OUT.relative_to(ROOT)}")
    wbplot.set_style()
    gram_map()
    ascent()
    step_smoothing()
    stripes()
    moving_average()
    temperature()
    top_p()
    rho()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
