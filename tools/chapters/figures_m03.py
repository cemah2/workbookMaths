#!/usr/bin/env python
"""Draw the figures of chapter M03 (used by Claude).

    python tools/chapters/figures_m03.py

Writes small PNG files into chapitres/m03_probabilites_conditionnelles/figures/: conditioning on a row of a contingency
table, Simpson's paradox, a confusion matrix read by rows and by columns, the precision of one model when the
prevalence changes, the expected cost of a decision threshold, the ROC curve as a staircase over the grid of pairs
next to the precision-recall curve and its average precision, a reliability diagram, and the false positive rates
forced by equal precision in two groups. Every figure is computed from the sheet's own examples (subscriptions by
device, two support teams, a disk failure model, eight scores, a churn model): none comes from workbookIA 3
(darts, ice cream, the 99 % test, the spam filter, the six scores of its ROC example, weather forecasts).
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

OUT = ROOT / "chapitres" / "m03_probabilites_conditionnelles" / "figures"
C = wbplot.CATEGORICAL
DPI = 110


def french(value: float, digits: int = 2) -> str:
    return f"{value:.{digits}f}".replace(".", ",")


def french_number(value: float, _pos=None) -> str:
    """Tick label with a French decimal comma and a true minus sign: 0,5 and −2."""
    return f"{value:g}".replace(".", ",").replace("-", "−")


def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ax in fig.axes:
        if getattr(ax, "keep_labels", False):
            continue
        for axis in (ax.xaxis, ax.yaxis):
            if axis.get_scale() == "linear" and not getattr(axis, "keep_labels", False):
                axis.set_major_formatter(FuncFormatter(french_number))
    fig.savefig(OUT / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  {name}")


def grid(ax) -> None:
    ax.grid(True, alpha=0.25)


def fig_conditioning() -> None:
    """P(plan | device) for each device next to P(plan): conditioning keeps one row and rescales it to 1."""
    counts = np.array([[180, 90, 30], [70, 80, 50]])
    plans = ["gratuit", "standard", "premium"]
    rows = [("mobile", counts[0] / counts[0].sum()), ("ordinateur", counts[1] / counts[1].sum()),
            ("tous", counts.sum(axis=0) / counts.sum())]
    fig, ax = plt.subplots(figsize=(7.5, 2.8))
    for k, (label, probs) in enumerate(rows):
        left = 0.0
        for j, p in enumerate(probs):
            ax.barh(k, p, left=left, color=C[j], alpha=0.85, edgecolor="white")
            ax.text(left + p / 2, k, french(p), ha="center", va="center", color="white", fontsize=9)
            left += p
    ax.set_yticks(range(3), labels=["sachant mobile", "sachant ordinateur", "sans condition"])
    ax.yaxis.keep_labels = True
    ax.invert_yaxis()
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=C[j], label=plan) for j, plan in enumerate(plans)], ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.18), fontsize=9, frameon=False)
    ax.set(xlim=(0, 1), title="La loi de l'abonnement, sachant l'appareil (chaque ligne a une somme de 1)")
    save(fig, "conditionnement.png")


def fig_simpson() -> None:
    """Two support teams: A is better on easy and on hard tickets, B is better overall."""
    labels = ["faciles", "difficiles", "tous"]
    team_a = [90 / 100, 30 / 100, 120 / 200]
    team_b = [170 / 200, 5 / 20, 175 / 220]
    x = np.arange(3)
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    ax.bar(x - 0.18, team_a, width=0.36, color=C[0], label="équipe A (100 faciles, 100 difficiles)")
    ax.bar(x + 0.18, team_b, width=0.36, color=C[1], label="équipe B (200 faciles, 20 difficiles)")
    for xi, a, b in zip(x, team_a, team_b):
        ax.text(xi - 0.18, a + 0.02, french(a), ha="center", fontsize=9)
        ax.text(xi + 0.18, b + 0.02, french(b), ha="center", fontsize=9)
    ax.set_xticks(x, labels=labels)
    ax.xaxis.keep_labels = True
    ax.set(ylim=(0, 1.05), ylabel="taux de résolution", title="Paradoxe de Simpson : A gagne dans chaque groupe, B au total")
    ax.legend(fontsize=8, loc="upper right")
    grid(ax)
    save(fig, "simpson.png")


def fig_confusion() -> None:
    """The confusion matrix of the disk failure model; recall reads along a row, precision down a column."""
    matrix = np.array([[90, 30], [40, 840]])
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.imshow(np.log1p(matrix), cmap="Blues")
    names = [["TP = 90", "FN = 30"], ["FP = 40", "TN = 840"]]
    for i in range(2):
        for j in range(2):
            ax.text(j, i, names[i][j], ha="center", va="center", fontsize=12,
                    color="white" if matrix[i, j] > 60 else "black")
    ax.add_patch(plt.Rectangle((-0.47, -0.47), 1.94, 0.94, fill=False, edgecolor=C[1], linewidth=2.5))
    ax.add_patch(plt.Rectangle((-0.42, -0.42), 0.84, 1.84, fill=False, edgecolor=C[2], linewidth=2.5, linestyle="--"))
    ax.text(1.6, 0, "recall = 90 / 120\n(une ligne)", color=C[1], va="center", fontsize=9, clip_on=False)
    ax.text(1.6, 1, "precision = 90 / 130\n(une colonne, pointillés)", color=C[2], va="center", fontsize=9,
            clip_on=False)
    ax.set_xticks([0, 1], labels=["panne prédite", "pas de panne prédite"])
    ax.set_yticks([0, 1], labels=["vraie panne", "disque sain"])
    ax.xaxis.keep_labels = ax.yaxis.keep_labels = True
    ax.set_title("1 000 disques : la vérité en lignes, la prédiction en colonnes", fontsize=10)
    for spine in ax.spines.values():
        spine.set_visible(False)
    save(fig, "confusion.png")


def fig_prevalence() -> None:
    """Precision of the disk failure model (recall 0,75, specificity 21/22) as a function of the prevalence."""
    recall, specificity = 0.75, 21 / 22
    prevalence = np.linspace(0.002, 0.6, 400)
    precision = recall * prevalence / (recall * prevalence + (1 - specificity) * (1 - prevalence))
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    ax.plot(prevalence, precision, color=C[0], linewidth=2)
    for pi, label in [(0.12, "parc ancien : 12 %"), (0.03, "parc récent : 3 %")]:
        value = recall * pi / (recall * pi + (1 - specificity) * (1 - pi))
        ax.plot(pi, value, "o", color=C[1])
        ax.annotate(f"{label}\nprecision {french(value)}", xy=(pi, value), xytext=(pi + 0.06, value - 0.22),
                    fontsize=9, arrowprops=dict(arrowstyle="->", color="gray"))
    ax.set(xlabel="prévalence P(panne)", ylabel="precision", ylim=(0, 1),
           title="Même modèle (recall 0,75, spécificité 0,955), autre prévalence")
    grid(ax)
    save(fig, "prevalence.png")


def fig_cost() -> None:
    """Expected cost per disk as a function of the threshold, for calibrated scores and a false negative 5 times
    as costly as a false positive: the minimum is at 1/6."""
    rng = np.random.default_rng(3)
    p = rng.beta(0.6, 3.0, 20_000)                     # calibrated probabilities of a failure
    y = rng.random(20_000) < p                         # outcomes drawn with those probabilities
    thresholds = np.linspace(0.01, 0.9, 179)
    cost = [(np.sum((p >= t) & ~y) * 1 + np.sum((p < t) & y) * 5) / len(p) for t in thresholds]
    best = thresholds[int(np.argmin(cost))]
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    ax.plot(thresholds, cost, color=C[0], linewidth=2)
    ax.axvline(1 / 6, color=C[1], linestyle="--", label="seuil théorique 1/6")
    ax.plot(best, min(cost), "o", color="black", label=f"minimum simulé : {french(best)}")
    ax.set(xlabel="seuil de décision t", ylabel="coût moyen par disque",
           title="Coût d'un faux négatif = 5, d'un faux positif = 1")
    ax.legend(fontsize=9)
    grid(ax)
    save(fig, "cout_seuil.png")


def fig_roc_pairs() -> None:
    """The ROC curve of the eight scores as a staircase over the 4 × 4 grid of pairs, and the precision-recall curve
    with the rectangles of the average precision."""
    pos = [0.95, 0.8, 0.6, 0.35]
    neg = [0.7, 0.5, 0.3, 0.1]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.3))
    for i, sp in enumerate(sorted(pos, reverse=True)):            # rows: positives from the top score
        for j, sn in enumerate(sorted(neg, reverse=True)):        # columns: negatives from the top score
            good = sp > sn
            ax1.add_patch(plt.Rectangle((j / 4, i / 4), 0.25, 0.25, facecolor=C[0] if good else "white",
                                        alpha=0.25 if good else 1, edgecolor="lightgray"))
    order = sorted([(s, 1) for s in pos] + [(s, 0) for s in neg], reverse=True)
    fpr, tpr = [0.0], [0.0]
    for _, label in order:
        fpr.append(fpr[-1] + (0 if label else 0.25))
        tpr.append(tpr[-1] + (0.25 if label else 0))
    ax1.plot(fpr, tpr, color=C[1], linewidth=2.5, marker="o", markersize=4)
    ax1.plot([0, 1], [0, 1], color="gray", linestyle=":")
    ax1.text(0.55, 0.15, "AUC = 13 cases sur 16\n= 0,8125", fontsize=10)
    ax1.set(xlim=(0, 1), ylim=(0, 1), aspect="equal", xlabel="taux de faux positifs (FPR)",
            ylabel="taux de vrais positifs (recall)", title="ROC : une marche par exemple, une case par paire")
    recall, precision, ap_parts = [], [], []
    tp = fp = 0
    for score, label in order:
        tp += label
        fp += 1 - label
        recall.append(tp / 4)
        precision.append(tp / (tp + fp))
    previous = 0.0
    for r, p in zip(recall, precision):
        if r > previous:
            ax2.add_patch(plt.Rectangle((previous, 0), r - previous, p, facecolor=C[2], alpha=0.25, edgecolor=C[2]))
            previous = r
    ax2.plot(recall, precision, color=C[0], marker="o", linewidth=2)
    ax2.axhline(0.5, color="gray", linestyle=":", label="hasard : la prévalence 0,5")
    ax2.text(0.05, 0.12, "AP = somme des rectangles\n≈ 0,854", fontsize=10)
    ax2.set(xlim=(0, 1.02), ylim=(0, 1.05), xlabel="recall", ylabel="precision",
            title="Precision-recall et average precision")
    ax2.legend(fontsize=9, loc="lower right")
    grid(ax2)
    save(fig, "roc_paires.png")


def fig_calibration() -> None:
    """Reliability diagram of a calibrated model and of an overconfident one (simulated), 10 bins."""
    rng = np.random.default_rng(7)
    true_p = rng.beta(2, 2, 6_000)
    y = rng.random(6_000) < true_p
    over = 1 / (1 + np.exp(-3 * np.log(true_p / (1 - true_p))))     # the same ranking, pushed towards 0 and 1
    bins = np.linspace(0, 1, 11)
    fig, ax = plt.subplots(figsize=(5, 4.6))
    ax.plot([0, 1], [0, 1], color="gray", linestyle=":", label="calibration parfaite")
    for probs, colour, label in [(true_p, C[0], "modèle calibré"), (over, C[1], "modèle trop sûr de lui")]:
        idx = np.clip(np.digitize(probs, bins) - 1, 0, 9)
        xs = [probs[idx == k].mean() for k in range(10) if np.any(idx == k)]
        ys = [y[idx == k].mean() for k in range(10) if np.any(idx == k)]
        brier = np.mean((probs - y) ** 2)
        ax.plot(xs, ys, marker="o", color=colour, label=f"{label} (Brier {french(brier, 3)})")
    ax.set(xlim=(0, 1), ylim=(0, 1), aspect="equal", xlabel="probabilité annoncée (moyenne de l'intervalle)",
           ylabel="fréquence observée", title="Diagramme de fiabilité, 10 intervalles")
    ax.legend(fontsize=8, loc="upper left")
    grid(ax)
    save(fig, "calibration.png")


def fig_fairness() -> None:
    """The false positive rate forced by a precision of 0,6 and a recall of 0,8, as a function of the prevalence."""
    prevalence = np.linspace(0.02, 0.5, 300)
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    for ppv, colour in [(0.6, C[0]), (0.8, C[2])]:
        fpr = prevalence / (1 - prevalence) * (1 - ppv) / ppv * 0.8
        ax.plot(prevalence, fpr, color=colour, linewidth=2, label=f"precision {french(ppv, 1)}, recall 0,8")
    for pi in (0.1, 0.3):
        value = pi / (1 - pi) * (0.4 / 0.6) * 0.8
        ax.plot(pi, value, "o", color=C[1])
        ax.annotate(f"prévalence {french(pi, 1)} :\nFPR {french(value, 3)}", xy=(pi, value), xytext=(pi + 0.04, value + 0.08),
                    fontsize=9, arrowprops=dict(arrowstyle="->", color="gray"))
    ax.set(xlabel="prévalence du groupe", ylabel="taux de faux positifs imposé", ylim=(0, 0.75),
           title="Même precision et même recall : le FPR dépend de la prévalence")
    ax.legend(fontsize=9, loc="upper left")
    grid(ax)
    save(fig, "equite.png")


def main() -> int:
    print(f"Figures de M03 dans {OUT.relative_to(ROOT)} :")
    fig_conditioning()
    fig_simpson()
    fig_confusion()
    fig_prevalence()
    fig_cost()
    fig_roc_pairs()
    fig_calibration()
    fig_fairness()
    return 0


if __name__ == "__main__":
    sys.exit(main())
