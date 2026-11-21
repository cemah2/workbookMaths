"""Cells of the worked example of the synthesis project: projets/projet_synthese/exemple/exemple.ipynb.

    python tools/chapters/build_ps.py --only exemple
    python tools/run_all_notebooks.py projets/projet_synthese/exemple/exemple.ipynb --inplace   # outputs kept

The example is a complete notebook-article on an algorithm that is neither in the list of the brief nor in
workbookIA: Poisson regression fitted by Newton's method (iteratively reweighted least squares). It follows the
sections of the kit's model (tools/chapters/ps_depart.py), one per step of the grid, with the same check cells
(« cas limite », « vérification de l'exemple », « Contrôle du module », tests and « mutation », « expérience »,
duration). Its setup cell is ``setup_cell("solution")``: it runs on the reference of mymath. Its module, tests,
conftest and mutants live next to it (poisson_newton.py, test_poisson_newton.py, conftest.py, mutants.py); its
figures are written into figures/ next to the notebook that runs (the folder where it is executed, if it holds the
notebook and the module). Seeds 9000 to 9099; no data nor number of an exercise of workbookIA or of this repository.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nbbuild import code, md, setup_cell  # noqa: E402

TITLE = r"""
# La régression de Poisson ajustée par la méthode de Newton : dérivation, implémentation, vérification

> **L'exemple rédigé du projet de synthèse.** Un article complet sur un algorithme qui n'est ni dans la liste du cahier des charges ni dans workbookIA. Il sert d'étalon pour chaque étape (PS.2 à PS.9 et PS.E1) : ton article lui emprunte la méthode, jamais le contenu, et son algorithme n'est pas accepté comme projet. Ouvre-le une fois ton cadrage écrit une première fois : le [`README.md`](README.md) de ce dossier dit quoi y regarder (et, si tu as choisi la régression logistique, ce qu'il ne faut pas y lire avant d'avoir rédigé tes §3 et §4). Ses sections ont les numéros du modèle du kit, son cadrage est dans [`cadrage.md`](cadrage.md), et sa grille remplie, [`grille.md`](grille.md), renvoie à chaque cellule qui sert de preuve. Il tourne sur la **référence** de `mymath` ; ton projet, lui, appelle **tes** fonctions.

**Auteur** : l'exemple de workbookMaths · **Algorithme** : régression de Poisson, ajustée par la méthode de Newton (moindres carrés repondérés) ; hors liste, hors workbookIA

## Résumé

Un comptage (des piqûres de moustique en une soirée, des pannes en une semaine) se modélise par une loi de Poisson dont le logarithme de la moyenne est une somme pondérée des features. L'article dérive, de la log-vraisemblance jusqu'aux formules que le code calcule, son gradient $\mathbf{X}^\top(\mathbf{y} - \boldsymbol{\mu})$, sa hessienne $-\mathbf{X}^\top\mathbf{W}\mathbf{X}$ et le pas de Newton, réécrit en moindres carrés pondérés. Il démontre que la log-vraisemblance est strictement concave quand les colonnes de $\mathbf{X}$ sont libres (le maximum, s'il existe, est unique) et que les moyennes ajustées ont la somme des comptages, puis il caractérise les données pour lesquelles le maximum n'existe pas. Un exemple de cinq soirées est calculé à la main, en fractions. Le module `poisson_newton.py`, qui appelle cinq fonctions de `mymath`, est vérifié contre scikit-learn et SciPy par une centaine de tests, et deux mutations sont attrapées. L'expérience montre la convergence quadratique de Newton contre la convergence linéaire d'une montée de gradient, de facteur prédit $1 - 1/\kappa$, puis la fuite des itérés quand le maximum n'existe pas.
"""

PROJECT_MD = r"""
### Le dossier de l'exemple

Cette cellule trouve le dossier de l'exemple (celui où le notebook s'exécute, s'il contient le notebook et le module, sinon `projets/projet_synthese/exemple` du dépôt) et importe son module, `poisson_newton.py`, qui utilise la librairie `mymath` chargée par la cellule de setup (ici, la référence). Elle ne demande rien.
"""

PROJECT_CODE = r'''
# The folder of the example, its module, and the tools of the check cells
import ast
import math
import re
import sys
import time
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from wbm.nbtools import run_pytest_group

T0 = time.perf_counter()
HERE = Path.cwd().resolve()           # the folder where the notebook runs (a copy of the example, or the repository's)
PROJECT = (HERE if (HERE / "exemple.ipynb").exists() and (HERE / "poisson_newton.py").exists()
           else (ROOT / "projets" / "projet_synthese" / "exemple").resolve())
FIGURES = PROJECT / "figures"         # the figures are written next to the notebook that runs
TEST_FILE = PROJECT / "test_poisson_newton.py"
if str(PROJECT) not in sys.path:
    sys.path.insert(0, str(PROJECT))
import poisson_newton as pn   # noqa: E402  (it imports mymath, registered by the setup cell)

shown_folder = PROJECT.relative_to(ROOT) if PROJECT.is_relative_to(ROOT) else PROJECT
print(f"📁 Dossier de l'exemple : {shown_folder} ; mymath : implémentation « {mymath.__wb_impl__} »")
'''

INTRO = r"""
## 1. Introduction et plan

Beaucoup de cibles sont des **comptages** : des appels par heure, des pannes par semaine, des piqûres par soirée. Une régression linéaire sur ces nombres peut prédire un comptage négatif et suppose une variance constante. La **régression de Poisson** suppose au contraire que chaque comptage suit une loi de Poisson (M02b §2) dont la moyenne est l'exponentielle d'une somme pondérée des features : la moyenne reste positive, et la variance, égale à la moyenne (M02b §4), grandit avec elle. C'est un **modèle linéaire généralisé** (*generalized linear model*, Nelder et Wedderburn, 1972), le cousin, pour les comptages, des modèles linéaires de workbookIA ; workbookIA ne le traite pas, et aucun algorithme de la liste du cahier des charges n'en dépend.

Ses poids s'estiment par maximum de vraisemblance (M13a §1). Il n'y a pas de formule fermée : on résout l'équation « gradient nul » par la méthode de Newton (M05a §4), qui se réécrit comme une suite de moindres carrés pondérés (M09b §3, M12b §7) dont les poids changent à chaque itération (*iteratively reweighted least squares*). L'article dérive tout cela, parce que la dérivation dit ce que le code seul ne dit pas : pourquoi le pas est bien défini (la hessienne est définie négative), pourquoi le point trouvé est le bon (il n'y a qu'un maximum), pourquoi il est atteint en quelques itérations (la convergence est quadratique), et quand il ne peut pas l'être (des comptages nuls mal placés).

**Plan.** §2 pose le problème : notations, hypothèses (H1) à (H4), conventions. §3 dérive la log-vraisemblance, son gradient, sa hessienne, le pas de Newton et sa forme en moindres carrés pondérés, les erreurs types, le modèle sans feature et la montée de gradient qui servira de comparaison. §4 démontre deux propriétés (la concavité stricte et l'unicité ; la somme des moyennes ajustées) et caractérise l'existence du maximum, le cas où une hypothèse tombe. §5 calcule un exemple à la main. §6 présente le module, §7 ses tests et une mutation, §8 l'expérience. §9 conclut et dit les limites ; les références et la présentation suivent.
"""

PROBLEM = r"""
## 2. Le problème

**En une phrase.** Un exemple est un couple $(\mathbf{x}_i, y_i)$ : un vecteur de $p$ nombres, dont le premier vaut 1, et un comptage $y_i \in \lbrace 0, 1, 2, \ldots \rbrace$ ; les paramètres sont $p$ poids $\mathbf{w}$ ; l'algorithme calcule les poids qui rendent les comptages observés les plus probables, quand $y_i$ est tiré d'une loi de Poisson de moyenne $\mu_i = e^{\mathbf{x}_i^\top\mathbf{w}}$.

**En une formule.**
$$\hat{\mathbf{w}} = \arg\max_{\mathbf{w} \in \mathbb{R}^p}\ \ell(\mathbf{w}), \qquad \ell(\mathbf{w}) = \sum_{i=1}^n \ln P(Y_i = y_i), \qquad Y_i \sim \mathcal{P}(\mu_i), \tag{2.1}$$
$$\mathbf{z} = \mathbf{X}\mathbf{w}, \qquad \boldsymbol{\mu} = \exp(\mathbf{z}) \ \text{(coordonnée par coordonnée)}, \qquad \mu_i = e^{z_i} = e^{\mathbf{x}_i^\top\mathbf{w}}. \tag{2.2}$$

**Les notations.**

| Symbole | Sens | Forme | Domaine |
|---|---|---|---|
| $n$, $p$ | nombre d'exemples ; nombre de colonnes de $\mathbf{X}$ (la colonne de 1 comprise) | scalaires | entiers, $1 \le p \le n$ |
| $\mathbf{X}$ | les données, une ligne par exemple | $(n, p)$ | $\mathbb{R}^{n \times p}$, première colonne $\mathbf{1}$ (H3) |
| $\mathbf{x}_i$ | la ligne $i$ de $\mathbf{X}$, écrite en colonne | $(p,)$ | $\mathbb{R}^p$ |
| $\mathbf{y}$ | les comptages observés | $(n,)$ | $\lbrace 0, 1, 2, \ldots \rbrace^n$ |
| $Y_i$, $\mathcal{P}(\mu_i)$ | le comptage aléatoire de l'exemple $i$, dont $y_i$ est la valeur observée ; la loi de Poisson de moyenne $\mu_i$ (M02b §2) | scalaire | $\lbrace 0, 1, 2, \ldots \rbrace$ |
| $\mathbf{w}$ | les poids ; $w_1$ est l'ordonnée à l'origine | $(p,)$ | $\mathbb{R}^p$ |
| $\mathbf{z} = \mathbf{X}\mathbf{w}$ | les sommes pondérées | $(n,)$ | $\mathbb{R}^n$ |
| $\boldsymbol{\mu} = \exp(\mathbf{z})$ | les moyennes du modèle | $(n,)$ | $]0, +\infty[^n$ |
| $\mathbf{W} = \operatorname{diag}(\boldsymbol{\mu})$, $\mathbf{W}^{1/2} = \operatorname{diag}(\sqrt{\mu_1}, \ldots, \sqrt{\mu_n})$ | la matrice diagonale des poids d'une itération, et sa racine (§3.5) | $(n, n)$ | diagonales $> 0$ |
| $\ell(\mathbf{w})$ | la log-vraisemblance | scalaire | $]-\infty, 0[$ |
| $\nabla\ell(\mathbf{w})$ | le gradient, de la forme de $\mathbf{w}$ | $(p,)$ | $\mathbb{R}^p$ |
| $\nabla^2\ell(\mathbf{w})$ | la hessienne | $(p, p)$ | symétrique |
| $\boldsymbol{\delta}$ | la direction de Newton | $(p,)$ | $\mathbb{R}^p$ |
| $\mathbf{A} = \mathbf{X}^\top\mathbf{W}\mathbf{X}$ | moins la hessienne au point considéré ($\mathbf{X}^\top\hat{\mathbf{W}}\mathbf{X}$, au maximum, en §3.8) | $(p, p)$ | symétrique définie positive sous (H1) et (H2) |
| $\mathbf{w}_k$, $\boldsymbol{\delta}_k$, $\boldsymbol{\mu}_k$ | l'itéré $k$ (`w0` du module pour $k = 0$, par défaut $\mathbf{0}$), sa direction de Newton ($\boldsymbol{\delta}_0$ en $\mathbf{w}_0 = \mathbf{0}$, (3.8)) et ses moyennes | $(p,)$, $(p,)$, $(n,)$ | $\mathbb{R}^p$, $\mathbb{R}^p$, $]0, +\infty[^n$ |
| $t_k$ | la fraction du pas de Newton prise à l'itération $k$ | scalaire | $\lbrace 1, \frac12, \frac14, \ldots \rbrace$ |
| `tol`, `max_iter`, `max_halvings` | les réglages de `fit` : l'arrêt quand $\max_j\lvert\delta_j\rvert \le$ `tol` $\cdot\,(1 + \max_j\lvert w_j\rvert)$ (§3.4), le nombre de pas au plus, de divisions par deux au plus | scalaires | `tol` $> 0$ (défaut $10^{-10}$) ; entiers $\ge 1$ et $\ge 0$ (défauts 100 et 30) |
| $\operatorname{se}(\hat{w}_j)$ | l'erreur type du poids $j$, (3.9) (`standard_errors` rend les $p$ à la fois) | scalaire ; $(p,)$ | $> 0$ |
| $\bar{y}$, $w_k$, $w^\star$ | le modèle sans feature (§3.7) : la moyenne des comptages, l'itéré $k$ (un nombre) et le maximum $\ln\bar{y}$ | scalaires | $\bar{y} \ge 0$ ; $\mathbb{R}$ |
| $\tilde{\mathbf{r}} = \mathbf{W}^{-1}(\mathbf{y} - \boldsymbol{\mu})$ | les résidus de travail | $(n,)$ | $\mathbb{R}^n$ |
| $\tilde{\mathbf{z}} = \mathbf{z} + \tilde{\mathbf{r}}$ | la réponse de travail (*working response*) | $(n,)$ | $\mathbb{R}^n$ |
| $\hat{\mathbf{w}}$, $\hat{\boldsymbol{\mu}}$, $\hat{\mathbf{W}}$ | les mêmes objets au maximum | | |
| $\eta$, `n_steps` | le learning rate de la montée de gradient (§3.8) ; son nombre de pas (`gradient_ascent` rend les $\mathbf{w}_k$, une ligne chacun : un tableau de forme `(n_steps + 1, p)`) | scalaires | $> 0$ ; entier $\ge 0$ |
| $\eta_c$, $\rho(\eta)$ | le learning rate critique ; le facteur par lequel la montée linéarisée multiplie l'erreur à chaque pas (3.12) | scalaires | $> 0$ ; $\ge 0$ |
| $\lambda_i$, $\lambda_{\min}$, $\lambda_{\max}$, $\kappa$ | les valeurs propres de $\mathbf{A} = \mathbf{X}^\top\hat{\mathbf{W}}\mathbf{X}$, les extrêmes, et le conditionnement $\lambda_{\max}/\lambda_{\min}$ | scalaires | $> 0$ ; $\kappa \ge 1$ |
| $\mathbf{1}$, $\mathbf{e}_j$ | le vecteur de 1 ; le $j$-ième vecteur de la base canonique | $(n,)$ ; $(p,)$ | |

**Les hypothèses**, citées par leur numéro en §3 et §4.
- **(H1) Le modèle.** Sachant les $\mathbf{x}_i$, les $Y_i$ sont indépendantes, $Y_i \sim \mathcal{P}(\mu_i)$ avec $\ln\mu_i = \mathbf{x}_i^\top\mathbf{w}$ (le lien logarithme, dit *canonique*) ; les $y_i$ observés sont des entiers $\ge 0$.
- **(H2) Le rang.** Les $p$ colonnes de $\mathbf{X}$ sont linéairement indépendantes (M12a §2) : $\mathbf{X}$ est de rang $p$ (M12a §4), donc $n \ge p$.
- **(H3) L'ordonnée à l'origine.** La première colonne de $\mathbf{X}$ est $\mathbf{1}$.
- **(H4) L'existence.** $\ell$ atteint son maximum. Le théorème 3 (§4) dit exactement quand ; « tous les $y_i > 0$ » suffit.

**Les conventions.**
- Vecteurs **colonnes** dans les formules (un tableau de forme `(n,)` dans le code) ; $\mathbf{x}_i$ est la ligne $i$ de $\mathbf{X}$ écrite en colonne, donc $z_i = \mathbf{x}_i^\top\mathbf{w}$.
- Gradient **de la forme de la variable** (M17 §4, M18 §6) : $\nabla\ell(\mathbf{w})$ est une colonne de $p$ coordonnées, comme $\mathbf{w}$, et la règle de la chaîne s'écrit avec la jacobienne transposée. MML range ce gradient en ligne (convention jacobienne) : ses formules sont les transposées des nôtres.
- **Somme** sur les exemples, pas de moyenne : $\ell$ est la log-vraisemblance de l'échantillon. scikit-learn minimise une moyenne (la moitié de la déviance moyenne) : même maximum, gradient divisé par $n$ (§7).
- $\exp$, $\ln$ et les autres fonctions d'une variable s'appliquent coordonnée par coordonnée à un vecteur ; $\ln$ est le logarithme népérien (`np.log`).

**Les notations du dépôt** ($n$ exemples, $p$ features, $\mathbf{X}$ de forme $(n, p)$, gras pour les vecteurs et les matrices, $\ln$, somme pondérée $\mathbf{z}$, learning rate $\eta$) sont gardées. Deux écarts avec la littérature sur ces modèles, signalés ici : elle note $\boldsymbol{\eta}$ la somme pondérée (ici $\mathbf{z}$, puisque $\eta$ est le learning rate) ; et $\mathbf{W}$ y est la matrice diagonale des poids d'une itération, pas une matrice de poids d'une couche comme dans workbookIA.
"""

DERIVATION_1 = r"""
## 3. La dérivation

Chaque étape est suivie de sa *justification* (le résultat utilisé, avec son chapitre et sa section) et des *formes* de ses objets. Les formules que le code calcule sont rassemblées à la fin de la section, avec la fonction qui calcule chacune.

### 3.1 La log-vraisemblance

Pour un comptage, la loi de Poisson donne $P(Y_i = y_i) = e^{-\mu_i}\,\dfrac{\mu_i^{y_i}}{y_i!}$, avec $\mu_i > 0$ (M02b §2). Le logarithme d'un produit est la somme des logarithmes, et $\ln e^a = a$ (R6 §3) :
$$\ln P(Y_i = y_i) = -\mu_i + y_i\ln\mu_i - \ln(y_i!).$$
Par (H1), les $Y_i$ sont indépendantes : la probabilité de l'échantillon est le produit des $P(Y_i = y_i)$ (M02b §5), et son logarithme la somme des logarithmes (R6 §3). Avec (2.2), $\ln\mu_i = z_i$ et $\mu_i = e^{z_i}$ :
$$\ell(\mathbf{w}) = \sum_{i=1}^n \big[\,y_iz_i - e^{z_i} - \ln(y_i!)\,\big], \qquad \mathbf{z} = \mathbf{X}\mathbf{w}. \tag{3.1}$$
*Formes* : $\mathbf{X}\mathbf{w}$ est $(n, p) \times (p,) \to (n,)$ ; chaque terme de la somme est un nombre, $\ell$ est un scalaire.

*Points délicats.* (a) Un comptage nul : $y_i\ln\mu_i = 0$, puisque $\mu_i > 0$ ; la formule ne prend jamais $\ln y_i$ (ni $\ln 0$), et $0! = 1$. (b) Le terme $-\ln(y_i!)$ ne dépend pas de $\mathbf{w}$ : il ne change ni le maximum ni les dérivées ; le code le garde pour que $\ell$ soit le logarithme d'une probabilité, donc $\ell < 0$ (chaque $P(Y_i = y_i) < 1$), et pour la comparer à SciPy (§7). (c) $e^{z_i}$ dépasse le plus grand flottant pour $z_i > 709$ environ (M05a §8) : le code rend alors $\ell = -\infty$, et le garde-fou de (3.5) refuse ce pas.

### 3.2 Le gradient

$\ell$ est la composée $\ell = L \circ \mathbf{f}$ de $\mathbf{f}(\mathbf{w}) = \mathbf{X}\mathbf{w}$, de $\mathbb{R}^p$ dans $\mathbb{R}^n$, et de $L(\mathbf{z}) = \sum_i \big[y_iz_i - e^{z_i} - \ln(y_i!)\big]$, de $\mathbb{R}^n$ dans $\mathbb{R}$.

1. **La jacobienne de $\mathbf{f}$.** $\mathbf{f}$ est linéaire : sa jacobienne est $\mathbf{X}$, de forme $(n, p)$, en tout point (M17 §1).
2. **Le gradient de $L$.** $z_i$ n'apparaît que dans le terme $i$ ; la dérivée de $y_iz_i$ est $y_i$, celle de $e^{z_i}$ est $e^{z_i}$ (R7 §5), et une somme se dérive terme à terme (R7 §6) : $\dfrac{\partial L}{\partial z_i} = y_i - e^{z_i} = y_i - \mu_i$, donc $\nabla_{\mathbf{z}}L = \mathbf{y} - \boldsymbol{\mu}$, de forme $(n,)$.
3. **La règle de la chaîne**, dans la convention de §2 (M17 §3 et §4) : $\nabla\ell(\mathbf{w}) = \mathbf{J}_{\mathbf{f}}(\mathbf{w})^\top\,\nabla_{\mathbf{z}}L\big(\mathbf{f}(\mathbf{w})\big)$, soit
$$\nabla\ell(\mathbf{w}) = \mathbf{X}^\top(\mathbf{y} - \boldsymbol{\mu}). \tag{3.2}$$

*Formes* : $\mathbf{X}^\top$ est $(p, n)$ et $\mathbf{y} - \boldsymbol{\mu}$ est $(n,)$ : le produit est $(p,)$, la forme de $\mathbf{w}$.

*Contrôle par la différentielle* (M18 §6 et §7). $\mathrm{d}\ell = \sum_i (y_i - \mu_i)\,\mathrm{d}z_i = (\mathbf{y} - \boldsymbol{\mu})^\top\mathrm{d}\mathbf{z}$ et $\mathrm{d}\mathbf{z} = \mathbf{X}\,\mathrm{d}\mathbf{w}$, donc $\mathrm{d}\ell = \operatorname{tr}\big(\mathbf{M}\,\mathrm{d}\mathbf{w}\big)$ avec $\mathbf{M} = (\mathbf{y} - \boldsymbol{\mu})^\top\mathbf{X}$, de forme $(1, p)$ (un nombre est sa propre trace) ; on lit $\nabla\ell = \mathbf{M}^\top = \mathbf{X}^\top(\mathbf{y} - \boldsymbol{\mu})$, la même formule. Coordonnée par coordonnée : $\dfrac{\partial\ell}{\partial w_j} = \sum_i (y_i - \mu_i)\,X_{ij}$. MML écrirait la ligne $(\mathbf{y} - \boldsymbol{\mu})^\top\mathbf{X}$ : les mêmes nombres.

### 3.3 La hessienne

La hessienne est la jacobienne du gradient (M19 §1). Dans (3.2), $\mathbf{X}^\top\mathbf{y}$ ne dépend pas de $\mathbf{w}$ ; reste $\mathbf{g}(\mathbf{w}) = -\mathbf{X}^\top\boldsymbol{\mu}(\mathbf{w})$, avec $\boldsymbol{\mu}(\mathbf{w}) = \exp(\mathbf{X}\mathbf{w})$.

1. $\exp$, appliquée coordonnée par coordonnée, a pour jacobienne $\operatorname{diag}(e^{z_1}, \ldots, e^{z_n}) = \mathbf{W}$ (M17 §2) ; composée avec $\mathbf{w} \mapsto \mathbf{X}\mathbf{w}$, de jacobienne $\mathbf{X}$, elle donne $\mathbf{J}_{\boldsymbol{\mu}}(\mathbf{w}) = \mathbf{W}\mathbf{X}$ (M17 §3), de forme $(n, n) \times (n, p) \to (n, p)$.
2. $\mathbf{m} \mapsto -\mathbf{X}^\top\mathbf{m}$ est linéaire, de jacobienne $-\mathbf{X}^\top$ (M17 §1) ; la règle de la chaîne (M17 §3) donne $\mathbf{J}_{\mathbf{g}}(\mathbf{w}) = -\mathbf{X}^\top\mathbf{W}\mathbf{X}$ :
$$\nabla^2\ell(\mathbf{w}) = -\mathbf{X}^\top\mathbf{W}\mathbf{X} = -\sum_{i=1}^n \mu_i\,\mathbf{x}_i\mathbf{x}_i^\top, \qquad \mathbf{W} = \operatorname{diag}(\boldsymbol{\mu}). \tag{3.3}$$

*Formes* : $(p, n) \times (n, n) \times (n, p) \to (p, p)$ ; chaque $\mathbf{x}_i\mathbf{x}_i^\top$ est $(p, 1) \times (1, p) \to (p, p)$. Coordonnée par coordonnée, $\dfrac{\partial^2\ell}{\partial w_j\,\partial w_k} = -\sum_i \mu_iX_{ij}X_{ik}$, symétrique en $j$ et $k$, comme le veut le théorème de Schwarz (M19 §1). Deux remarques : la hessienne **ne dépend pas de $\mathbf{y}$** (§3.6 s'en sert) ; et le code ne forme jamais $\mathbf{W}$, de taille $n \times n$ : `-(X.T * mu) @ X` multiplie la colonne $i$ de $\mathbf{X}^\top$ par $\mu_i$ (le produit de Hadamard et sa diffusion, M09a §3).

### 3.4 Le pas de Newton

Près de $\mathbf{w}$, le développement de Taylor d'ordre 2 (M19 §1) remplace $\ell$ par une fonction quadratique du déplacement $\mathbf{h}$ :
$$\ell(\mathbf{w} + \mathbf{h}) \approx q(\mathbf{h}) = \ell(\mathbf{w}) + \nabla\ell(\mathbf{w})^\top\mathbf{h} + \tfrac12\,\mathbf{h}^\top\nabla^2\ell(\mathbf{w})\,\mathbf{h}.$$
Sous (H1) et (H2), $\mathbf{A} = -\nabla^2\ell(\mathbf{w}) = \mathbf{X}^\top\mathbf{W}\mathbf{X}$ est symétrique définie positive (le lemme de §4). Donc $-q(\mathbf{h}) = \frac12\mathbf{h}^\top\mathbf{A}\mathbf{h} - \mathbf{b}^\top\mathbf{h} - \ell(\mathbf{w})$, avec $\mathbf{b} = \nabla\ell(\mathbf{w})$, est la quadratique de M12c §7 (« Le minimum d'une quadratique ») : son unique minimum, c'est-à-dire l'unique maximum de $q$, est la solution de $\mathbf{A}\mathbf{h} = \mathbf{b}$. La **méthode de Newton** va jusqu'à ce maximum :
$$\boldsymbol{\delta} = (\mathbf{X}^\top\mathbf{W}\mathbf{X})^{-1}\,\mathbf{X}^\top(\mathbf{y} - \boldsymbol{\mu}) = -\big(\nabla^2\ell(\mathbf{w})\big)^{-1}\,\nabla\ell(\mathbf{w}). \tag{3.4}$$
*Formes* : $(p, p) \times (p,) \to (p,)$. En dimension 1, $w + \delta = w - \ell'(w)/\ell''(w)$ : la méthode de Newton de M05a §4 appliquée à l'équation $\ell'(w) = 0$ (l'encadré 🔗 de M05a §4). *Point délicat* : (3.4) demande que $\mathbf{X}^\top\mathbf{W}\mathbf{X}$ soit inversible ; c'est (H2), par le lemme de §4 ; sans (H2), le pas n'est pas défini, et le maximum, s'il existe, n'est pas unique (le cas limite de §4).

**L'itération et son garde-fou.** En partant de $\mathbf{w}_0 = \mathbf{0}$,
$$\mathbf{w}_{k+1} = \mathbf{w}_k + t_k\,\boldsymbol{\delta}_k, \qquad t_k = \text{le premier nombre de } 1, \tfrac12, \tfrac14, \ldots \text{ tel que } \ell(\mathbf{w}_k + t_k\boldsymbol{\delta}_k) \ge \ell(\mathbf{w}_k) \tag{3.5}$$
(le code tolère une baisse de $10^{-12}(1 + \lvert\ell(\mathbf{w}_k)\rvert)$, l'arrondi). Newton pur prend toujours $t_k = 1$ ; loin du maximum, le pas plein peut faire **baisser** $\ell$ (M05a §4, un départ trop loin ; §5 en donne un exemple). La division par deux s'arrête toujours : avec $\varphi(t) = \ell(\mathbf{w}_k + t\boldsymbol{\delta}_k)$, la règle de la chaîne (M19 §1) donne $\varphi'(0) = \mathbf{b}^\top\boldsymbol{\delta}_k = \mathbf{b}^\top\mathbf{A}^{-1}\mathbf{b} = \mathbf{c}^\top\mathbf{A}\mathbf{c}$ avec $\mathbf{c} = \mathbf{A}^{-1}\mathbf{b}$, qui est $> 0$ dès que $\mathbf{b} \ne \mathbf{0}$ ($\mathbf{A}$ définie positive, M12c §7) ; une dérivée positive en 0 donne $\varphi(t) > \varphi(0)$ pour $t > 0$ assez petit (le taux d'accroissement tend vers $\varphi'(0)$, R7 §3). Près du maximum, le pas plein est accepté : par Taylor d'ordre 2 (M19 §1, avec un reste en $\lVert\boldsymbol{\delta}\rVert^3$), $\ell(\mathbf{w} + \boldsymbol{\delta}) - \ell(\mathbf{w}) = \mathbf{b}^\top\boldsymbol{\delta} - \frac12\boldsymbol{\delta}^\top\mathbf{A}\boldsymbol{\delta} + O(\lVert\boldsymbol{\delta}\rVert^3) = \frac12\,\mathbf{b}^\top\mathbf{A}^{-1}\mathbf{b} + O(\lVert\boldsymbol{\delta}\rVert^3)$, et $\frac12\,\mathbf{b}^\top\mathbf{A}^{-1}\mathbf{b} = \frac12\,\boldsymbol{\delta}^\top\mathbf{A}\boldsymbol{\delta} \ge \frac{\lambda_{\min}(\mathbf{A})}{2}\lVert\boldsymbol{\delta}\rVert^2$ l'emporte quand $\boldsymbol{\delta}$ est petit : la méthode redevient Newton pur. Le code s'arrête quand $\max_j\lvert\delta_j\rvert \le 10^{-10}\,(1 + \max_j\lvert w_j\rvert)$, après avoir fait ce dernier pas.

### 3.5 Les moindres carrés pondérés

(3.4) s'écrit $\mathbf{X}^\top\mathbf{W}\mathbf{X}\,\boldsymbol{\delta} = \mathbf{X}^\top(\mathbf{y} - \boldsymbol{\mu})$. Comme $\mu_i > 0$, $\mathbf{W}$ est inversible et $\mathbf{y} - \boldsymbol{\mu} = \mathbf{W}\tilde{\mathbf{r}}$, avec les **résidus de travail** $\tilde{r}_i = (y_i - \mu_i)/\mu_i$ (aucune division par 0 : c'est un avantage du lien logarithme). Avec $\mathbf{W}^{1/2} = \operatorname{diag}(\sqrt{\mu_1}, \ldots, \sqrt{\mu_n})$, diagonale donc symétrique, la transposée d'un produit (M09a §4) donne $\mathbf{X}^\top\mathbf{W}\mathbf{X} = (\mathbf{W}^{1/2}\mathbf{X})^\top(\mathbf{W}^{1/2}\mathbf{X})$ et $\mathbf{X}^\top\mathbf{W}\tilde{\mathbf{r}} = (\mathbf{W}^{1/2}\mathbf{X})^\top(\mathbf{W}^{1/2}\tilde{\mathbf{r}})$ : (3.4) est le système des **équations normales** (M09b §3) des moindres carrés de $\mathbf{W}^{1/2}\tilde{\mathbf{r}}$ sur $\mathbf{W}^{1/2}\mathbf{X}$. Les colonnes de $\mathbf{W}^{1/2}\mathbf{X}$ sont libres (par (H2), puisque $\mathbf{W}^{1/2}$ est inversible), donc ce problème a une unique solution (M09b §3) :
$$\boldsymbol{\delta} = \arg\min_{\mathbf{d} \in \mathbb{R}^p}\ \sum_{i=1}^n \mu_i\,\big(\tilde{r}_i - \mathbf{x}_i^\top\mathbf{d}\big)^2 = \arg\min_{\mathbf{d}}\ \big\lVert \mathbf{W}^{1/2}\tilde{\mathbf{r}} - \mathbf{W}^{1/2}\mathbf{X}\,\mathbf{d} \big\rVert^2, \qquad \big(\mathbf{W}^{1/2}\tilde{\mathbf{r}}\big)_i = \frac{y_i - \mu_i}{\sqrt{\mu_i}}. \tag{3.6}$$
Ce sont des moindres carrés **pondérés** par les $\mu_i$ (le produit scalaire pondéré de M12b §1). Le code les résout par la décomposition QR de $\mathbf{W}^{1/2}\mathbf{X}$ (M12b §7 ; `orthogonal.least_squares_qr` de `mymath`), sans former $\mathbf{X}^\top\mathbf{W}\mathbf{X}$, dont le conditionnement est le carré de celui de $\mathbf{W}^{1/2}\mathbf{X}$ (M12d §4). *Formes* : $\mathbf{W}^{1/2}\mathbf{X}$ est $(n, p)$ (la ligne $i$ de $\mathbf{X}$ multipliée par $\sqrt{\mu_i}$), $\mathbf{W}^{1/2}\tilde{\mathbf{r}}$ est $(n,)$, $\boldsymbol{\delta}$ est $(p,)$.

**La forme « moindres carrés repondérés ».** En posant $\mathbf{d} = \mathbf{v} - \mathbf{w}$ dans (3.6), $\tilde{r}_i - \mathbf{x}_i^\top(\mathbf{v} - \mathbf{w}) = \tilde{z}_i - \mathbf{x}_i^\top\mathbf{v}$, avec la **réponse de travail** $\tilde{\mathbf{z}} = \mathbf{X}\mathbf{w} + \tilde{\mathbf{r}}$ :
$$\mathbf{w} + \boldsymbol{\delta} = \arg\min_{\mathbf{v} \in \mathbb{R}^p}\ \sum_{i=1}^n \mu_i\,\big(\tilde{z}_i - \mathbf{x}_i^\top\mathbf{v}\big)^2, \qquad \tilde{\mathbf{z}} = \mathbf{X}\mathbf{w} + \mathbf{W}^{-1}(\mathbf{y} - \boldsymbol{\mu}). \tag{3.7}$$
Chaque pas de Newton est donc une régression des moindres carrés pondérés, dont la réponse et les poids sont recalculés à chaque itération : d'où le nom de la méthode. $\tilde{z}_i$ est la linéarisation de $\ln y_i$ autour de $\mu_i$, $\ln y \approx \ln\mu + (y - \mu)/\mu$ (Taylor d'ordre 1, M05a §3), qui a un sens même pour $y_i = 0$, contrairement à $\ln y_i$. Le code calcule (3.6), pas (3.7) : les deux donnent le même $\mathbf{w}_{k+1}$ en arithmétique exacte, mais (3.6) évite d'ajouter puis de retrancher $\mathbf{X}\mathbf{w}$.

**Le premier pas.** En $\mathbf{w}_0 = \mathbf{0}$ : $\mathbf{z} = \mathbf{0}$, $\boldsymbol{\mu} = \mathbf{1}$, $\mathbf{W} = \mathbf{I}$ et $\tilde{\mathbf{r}} = \mathbf{y} - \mathbf{1}$. (3.6) devient les moindres carrés ordinaires de $\mathbf{y} - \mathbf{1}$ sur $\mathbf{X}$ (M09b §3) :
$$\boldsymbol{\delta}_0 = (\mathbf{X}^\top\mathbf{X})^{-1}\,\mathbf{X}^\top(\mathbf{y} - \mathbf{1}), \tag{3.8}$$
un vecteur de nombres **rationnels** quand $\mathbf{X}$ et $\mathbf{y}$ sont entiers : c'est l'exemple à la main de §5.

### 3.6 L'information de Fisher et les erreurs types

La hessienne (3.3) ne dépend pas des comptages : son espérance sous le modèle est elle-même. L'information de Fisher de MB8 §1, $-\mathbb{E}\big[\partial_\theta^2\ln p_\theta(X)\big]$, dans sa version matricielle pour un paramètre vectoriel et pour tout l'échantillon (admise ici), vaut donc $\mathcal{I}(\mathbf{w}) = -\mathbb{E}\big[\nabla^2\ell(\mathbf{w})\big] = \mathbf{X}^\top\mathbf{W}\mathbf{X}$ : l'information observée (la courbure de $\ell$) et l'information de Fisher coïncident. Au maximum, l'erreur type de chaque poids (M02c §7) s'estime par la racine de la diagonale de l'inverse (résultat asymptotique, pour $n$ grand, admis : l'encadré 💻 de MB8 §1) :
$$\operatorname{se}(\hat{w}_j) = \sqrt{\big[(\mathbf{X}^\top\hat{\mathbf{W}}\mathbf{X})^{-1}\big]_{jj}}. \tag{3.9}$$
Le code factorise $\mathbf{X}^\top\hat{\mathbf{W}}\mathbf{X} = \mathbf{L}\mathbf{L}^\top$ (Cholesky, M12c §7 ; `eigen.cholesky`) : $(\mathbf{L}\mathbf{L}^\top)^{-1} = \mathbf{L}^{-\top}\mathbf{L}^{-1}$, dont le terme diagonal $j$ est $\sum_i (\mathbf{L}^{-1})_{ij}^2$, le carré de la norme de la colonne $j$ de $\mathbf{L}^{-1}$. *Formes* : $\mathbf{L}$ et $\mathbf{L}^{-1}$ sont $(p, p)$, triangulaires inférieures ; $\operatorname{se}$ est $(p,)$.

### 3.7 Le modèle sans feature

Avec $\mathbf{X} = \mathbf{1}$ ($p = 1$), et $S = \sum_iy_i$, $c = \sum_i\ln(y_i!)$ : (3.1) devient $\ell(w) = Sw - ne^w - c$, (3.2) $\ell'(w) = S - ne^w$, (3.3) $\ell''(w) = -ne^w < 0$. Si $S > 0$, $\ell'$ s'annule en un seul point, $w^\star = \ln\bar{y}$ avec $\bar{y} = S/n$ (R6 §3), le maximum (M05a §2, $\ell$ étant strictement concave). Le pas (3.4) vaut $(S - ne^w)/(ne^w)$ :
$$w_{k+1} = w_k + \bar{y}\,e^{-w_k} - 1, \qquad w_k \to w^\star = \ln\bar{y}. \tag{3.10}$$

- **Le premier pas va au-delà du maximum quand $\bar{y} > 1$.** Depuis $w_0 = 0$, $w_1 = \bar{y} - 1$. Or $\ln a \le a - 1$ pour tout $a > 0$ : $\ln$ est concave ($(\ln)''(a) = -1/a^2 < 0$), donc au-dessous de sa tangente en 1, la droite $a \mapsto a - 1$ (M05a §1). Ainsi $w_1 \ge w^\star$, et si $\bar{y} > 1$, $w_0 = 0 < w^\star \le w_1$ : le premier pas saute par-dessus le maximum.
- **Ensuite, la suite descend vers $w^\star$.** Avec $u_k = w_k - w^\star$, (3.10) s'écrit $u_{k+1} = \psi(u_k)$, $\psi(u) = u + e^{-u} - 1$. La fonction $g(u) = e^{-u} - (1 - u)$ est strictement convexe ($g'' = e^{-u} > 0$) et $g'(0) = 0$ : 0 est son unique minimum (M05a §2), où $g(0) = 0$, donc $\psi(u) = g(u) > 0$ pour $u \ne 0$. Et pour $u > 0$, $e^{-u} < 1$ (R6 §1), donc $\psi(u) < u$. Si $\bar{y} \ne 1$, $u_1 > 0$, puis $0 < u_{k+1} < u_k$. Et $u_k \to 0$ : pour $u > 0$, Taylor avec reste (M05a §3) donne $e^{-u} \le 1 - u + \frac{u^2}{2}$, donc $\psi(u) \le \frac{u^2}{2}$, et $\psi(u) \le \frac{u}{2}$ si $u \le 1$ ; si $u > 1$, $\psi(u) < u - 1 + e^{-1}$. L'écart perd donc au moins $1 - e^{-1} \approx 0{,}63$ à chaque pas tant qu'il dépasse 1, puis il est au moins divisé par 2 à chaque pas : $w_k \to w^\star$.
- **L'erreur est élevée au carré.** Taylor en 0 (M05a §3) : $e^{-u} = 1 - u + \frac{u^2}{2} + O(u^3)$, donc $\psi(u) = \frac{u^2}{2} + O(u^3)$ et $u_{k+1} \approx \frac12\,u_k^2$, la convergence quadratique de M05a §4 (avec $f(w) = \bar{y} - e^w$, $\frac{f''(w^\star)}{2f'(w^\star)} = \frac{-\bar{y}}{-2\bar{y}} = \frac12$).

Le code de ce cas, `intercept_only`, appelle `approx.newton` de `mymath` sur $f(w) = \bar{y} - e^w$, de dérivée $-e^w$.

### 3.8 La montée de gradient, pour comparer

La montée de gradient (M05b §8) remplace la courbure par un learning rate fixe $\eta > 0$ :
$$\mathbf{w}_{k+1} = \mathbf{w}_k + \eta\,\mathbf{X}^\top(\mathbf{y} - \boldsymbol{\mu}_k). \tag{3.11}$$
Près du maximum, avec $\mathbf{e}_k = \mathbf{w}_k - \hat{\mathbf{w}}$ et $\mathbf{A} = \mathbf{X}^\top\hat{\mathbf{W}}\mathbf{X}$ : la jacobienne du gradient est la hessienne (M19 §1), donc l'approximation linéaire du gradient (M17 §1) donne $\nabla\ell(\mathbf{w}_k) \approx \nabla\ell(\hat{\mathbf{w}}) - \mathbf{A}\mathbf{e}_k = -\mathbf{A}\mathbf{e}_k$, et $\mathbf{e}_{k+1} \approx (\mathbf{I} - \eta\mathbf{A})\,\mathbf{e}_k$ : l'itération de Richardson de M19 §4 sur $\mathbf{A}$, symétrique définie positive (le lemme de §4). Pour cette itération linéarisée, M19 §4 et §5 donnent (l'écart entre l'itération et sa linéarisation, d'ordre $\lVert\mathbf{e}_k\rVert^2$, est admis négligeable près du maximum) :
$$\eta_c = \frac{2}{\lambda_{\max}(\mathbf{A})}, \qquad \rho(\eta) = \max_i\,\lvert 1 - \eta\lambda_i\rvert, \qquad \rho\Big(\frac{1}{\lambda_{\max}}\Big) = 1 - \frac{1}{\kappa}, \qquad \kappa = \frac{\lambda_{\max}}{\lambda_{\min}} = \kappa\big(\hat{\mathbf{W}}^{1/2}\mathbf{X}\big)^2. \tag{3.12}$$
L'erreur est multipliée par environ $\rho$ à chaque pas : une convergence **linéaire**, une droite de pente $\log_{10}\rho$ sur un graphique à l'échelle logarithmique, à comparer à la convergence quadratique de Newton. La dernière égalité vient de $\mathbf{A} = \mathbf{B}^\top\mathbf{B}$ avec $\mathbf{B} = \hat{\mathbf{W}}^{1/2}\mathbf{X}$ (§3.5) et de $\kappa(\mathbf{B}^\top\mathbf{B}) = \kappa(\mathbf{B})^2$ (M12d §4). Le code de $\eta_c$, `critical_learning_rate`, appelle `iterative.critical_step_size` de `mymath`.

### Les formules finales et le code

| Formule | Ce qu'elle calcule | Fonction de `poisson_newton.py` (sa docstring cite le numéro) | Fonction de `mymath` appelée |
|---|---|---|---|
| (2.2) | $\boldsymbol{\mu} = \exp(\mathbf{X}\mathbf{w})$ | `mean` | — |
| (3.1) | $\ell(\mathbf{w})$ | `log_likelihood` | — |
| (3.2) | $\nabla\ell(\mathbf{w})$ | `gradient` | — |
| (3.3) | $\nabla^2\ell(\mathbf{w})$ | `hessian` | — |
| (3.4), calculée par (3.6) ; (3.8) en $\mathbf{w} = \mathbf{0}$ | $\boldsymbol{\delta}$ | `newton_direction` | `orthogonal.least_squares_qr` |
| (3.5) | l'itération et son garde-fou | `fit` | `svd_pca.condition_number` (H2, et des poids qui s'effondrent) |
| (3.9) | les erreurs types | `standard_errors` | `eigen.cholesky` |
| (3.10) | le modèle sans feature | `intercept_only` | `approx.newton` |
| (3.11) | la montée de gradient | `gradient_ascent` | — |
| (3.12) | le learning rate critique $\eta_c$ | `critical_learning_rate` | `iterative.critical_step_size` |

(3.7) est une autre écriture de (3.6), que le code ne calcule pas telle quelle ; `check_data` vérifie (H1) (des comptages entiers $\ge 0$) et (H2) (`svd_pca.condition_number`).
"""

PROPERTIES = r"""
## 4. Deux propriétés et un cas limite

Les démonstrations suivent R4 §8 : l'énoncé, les objets introduits, chaque « donc » appuyé sur ce qu'il cite, une conclusion et ∎.

**Lemme.** Sous (H1) et (H2), pour tout $\mathbf{w}$, la matrice $\mathbf{X}^\top\mathbf{W}\mathbf{X}$ est symétrique définie positive.

*Démonstration.* Elle est symétrique : $(\mathbf{X}^\top\mathbf{W}\mathbf{X})^\top = \mathbf{X}^\top\mathbf{W}^\top\mathbf{X} = \mathbf{X}^\top\mathbf{W}\mathbf{X}$ (M09a §4 ; $\mathbf{W}$ est diagonale). Pour $\mathbf{v} \in \mathbb{R}^p$, posons $\mathbf{u} = \mathbf{X}\mathbf{v}$, de forme $(n,)$ :
$$\mathbf{v}^\top\mathbf{X}^\top\mathbf{W}\mathbf{X}\,\mathbf{v} = \mathbf{u}^\top\mathbf{W}\mathbf{u} = \sum_{i=1}^n \mu_i\,u_i^2 \ \ge\ 0. \tag{4.1}$$
Une somme de termes positifs ou nuls n'est nulle que si chaque terme l'est. Par (H1), $\mu_i = e^{z_i} > 0$ (R6 §1), donc (4.1) est nulle seulement si $u_i = 0$ pour tout $i$, c'est-à-dire $\mathbf{X}\mathbf{v} = \mathbf{0}$, $\mathbf{v} \in \ker\mathbf{X}$. Par (H2), les colonnes de $\mathbf{X}$ sont libres, donc $\ker\mathbf{X} = \lbrace \mathbf{0} \rbrace$ (un vecteur du noyau est une relation entre les colonnes, M12a §2 et §6). Ainsi (4.1) est $> 0$ pour $\mathbf{v} \ne \mathbf{0}$ : la matrice est définie positive (M12c §7). ∎

**Propriété 1 (concavité stricte et unicité).** Sous (H1) et (H2) : (i) la hessienne $\nabla^2\ell(\mathbf{w})$ est définie négative en tout point ; (ii) un point critique de $\ell$ est son unique maximum global ; (iii) $\ell$ a au plus un maximum.

*Démonstration.* (i) Par (3.3) et le lemme, $-\nabla^2\ell(\mathbf{w})$ est définie positive, donc $\nabla^2\ell(\mathbf{w})$ est définie négative (M12c §7).
(ii) Soit $\hat{\mathbf{w}}$ tel que $\nabla\ell(\hat{\mathbf{w}}) = \mathbf{0}$, et $\mathbf{v} \ne \hat{\mathbf{w}}$. Sur la droite qui les joint, posons $\varphi(t) = \ell\big(\hat{\mathbf{w}} + t(\mathbf{v} - \hat{\mathbf{w}})\big)$ pour $t \in \mathbb{R}$. La règle de la chaîne (M19 §1) donne $\varphi'(t) = \nabla\ell(\cdot)^\top(\mathbf{v} - \hat{\mathbf{w}})$ et $\varphi''(t) = (\mathbf{v} - \hat{\mathbf{w}})^\top\,\nabla^2\ell(\cdot)\,(\mathbf{v} - \hat{\mathbf{w}})$, au point $\hat{\mathbf{w}} + t(\mathbf{v} - \hat{\mathbf{w}})$. Par (i), et parce que $\mathbf{v} - \hat{\mathbf{w}} \ne \mathbf{0}$, $\varphi''(t) < 0$ pour tout $t$ : $-\varphi$ est strictement convexe, et $\varphi'(0) = \nabla\ell(\hat{\mathbf{w}})^\top(\mathbf{v} - \hat{\mathbf{w}}) = 0$. Par M05a §2 (un point critique d'une fonction strictement convexe est son unique minimum, appliqué à $-\varphi$), 0 est l'unique maximum de $\varphi$ : $\ell(\mathbf{v}) = \varphi(1) < \varphi(0) = \ell(\hat{\mathbf{w}})$. Comme $\mathbf{v}$ est quelconque, $\hat{\mathbf{w}}$ est l'unique maximum global.
(iii) $\ell$ est dérivable sur tout $\mathbb{R}^p$ : un maximum est un point intérieur, donc un point critique (M05b §7 ; R7 §8, coordonnée par coordonnée) ; par (ii), il n'y en a qu'un. ∎

*Où servent les hypothèses.* (H1) donne $\mu_i > 0$ dans (4.1) ; (H2) donne $\ker\mathbf{X} = \lbrace \mathbf{0} \rbrace$. Sans (H2), pour $\mathbf{v} \in \ker\mathbf{X}$ non nul, $\mathbf{X}(\mathbf{w} + s\mathbf{v}) = \mathbf{X}\mathbf{w}$, donc $\ell(\mathbf{w} + s\mathbf{v}) = \ell(\mathbf{w})$ pour tout $s$ : $\varphi'' = 0$ dans cette direction, et un maximum, s'il existe, est atteint sur toute une droite (la cellule « cas limite » le montre).

*Ce qu'elle garantit en pratique.* Le pas de Newton (3.4) est toujours défini et c'est une direction de montée, donc le garde-fou de (3.5) s'arrête ; le point où le gradient s'annule est **le** maximum de vraisemblance, sans maximum local où se perdre. Trois méthodes différentes (la nôtre, scikit-learn, SciPy) doivent trouver le même point, et la nôtre aussi depuis plusieurs départs.

*Vérifiée numériquement par* `test_hessian_is_negative_definite`, `test_fit_finds_the_same_maximum_from_random_starts`, et l'accord avec deux oracles, `test_fit_matches_sklearn` et `test_fit_matches_scipy_minimize` (§7).

**Propriété 2 (les moyennes ajustées ont la somme des comptages).** Sous (H1), (H3) et (H4) : au maximum $\hat{\mathbf{w}}$, $\mathbf{X}^\top(\mathbf{y} - \hat{\boldsymbol{\mu}}) = \mathbf{0}$ ; en particulier
$$\sum_{i=1}^n \hat{\mu}_i = \sum_{i=1}^n y_i, \tag{4.2}$$
et, pour une feature qui vaut 0 ou 1 (un groupe), la somme des moyennes ajustées du groupe est le nombre d'événements observés dans le groupe.

*Démonstration.* Par (H4), $\hat{\mathbf{w}}$ existe ; c'est un point critique (propriété 1, (iii), dont l'argument n'utilise pas (H2)) : $\nabla\ell(\hat{\mathbf{w}}) = \mathbf{0}$, et (3.2), qui repose sur (H1), donne $\mathbf{X}^\top(\mathbf{y} - \hat{\boldsymbol{\mu}}) = \mathbf{0}$. Sa coordonnée $j$ s'écrit $\sum_i X_{ij}\,(y_i - \hat{\mu}_i) = 0$. Par (H3), la colonne 1 est $\mathbf{1}$ : $\sum_i (y_i - \hat{\mu}_i) = 0$, c'est (4.2). Pour une feature $j$ qui vaut 0 ou 1, $X_{ij} = 1$ exactement dans le groupe, et la coordonnée $j$ dit $\sum_{i \in \text{groupe}}\hat{\mu}_i = \sum_{i \in \text{groupe}}y_i$. ∎

*Où servent les hypothèses.* (H4) : sans maximum, pas de $\hat{\mathbf{w}}$ (le théorème 3, ci-dessous). (H3) : sans colonne de 1, rien n'impose (4.2) ; sur l'exemple de §5 privé de sa colonne de 1, $\sum_i\hat{\mu}_i \approx 9{,}63$ pour $\sum_iy_i = 11$ (cellule « cas limite »). (H1) donne la formule (3.2).

*Ce qu'elle garantit en pratique.* Le modèle reproduit le nombre total d'événements, et celui de chaque groupe d'une feature 0/1 : il est calibré en moyenne, sans réglage. C'est aussi un test d'une implémentation qui ne demande aucun oracle.

*Vérifiée numériquement par* `test_fitted_means_sum_to_the_counts` (§7) et par l'exemple de §5.

**Théorème 3 (quand le maximum existe).** Sous (H1) et (H2), $\ell$ atteint son maximum si et seulement s'il n'existe **aucune** direction $\mathbf{d} \ne \mathbf{0}$ telle que
$$\mathbf{X}\mathbf{d} \le \mathbf{0} \ \text{(coordonnée par coordonnée)} \qquad \text{et} \qquad (\mathbf{X}\mathbf{d})_i = 0 \ \text{pour tout } i \text{ tel que } y_i > 0. \tag{4.3}$$
Trois conséquences. (a) Si tous les $y_i > 0$, le maximum existe : (4.3) imposerait $\mathbf{X}\mathbf{d} = \mathbf{0}$, donc $\mathbf{d} = \mathbf{0}$ par (H2). (b) Si tous les $y_i$ sont nuls et (H3), il n'existe pas : $\mathbf{d} = -\mathbf{e}_1$ donne $\mathbf{X}\mathbf{d} = -\mathbf{1}$. (c) Si une feature $j$ qui vaut 0 ou 1 n'a que des comptages nuls dans le groupe où elle vaut 1, il n'existe pas : $\mathbf{d} = -\mathbf{e}_j$ donne $(\mathbf{X}\mathbf{d})_i = -1$ dans ce groupe, 0 ailleurs. Si c'est le groupe où elle vaut 0, il faut (H3) : $\mathbf{d} = \mathbf{e}_j - \mathbf{e}_1$ donne $(\mathbf{X}\mathbf{d})_i = -1$ dans ce groupe, 0 ailleurs ; sans colonne de 1, le maximum peut exister ($\mathbf{X} = (0, 0, 1, 1)^\top$, $\mathbf{y} = (0, 0, 3, 4)$ : $\hat{w} = \ln\frac72$).

*Démonstration du « seulement si » : le cas où (H4) tombe.* Supposons qu'une direction $\mathbf{d} \ne \mathbf{0}$ vérifie (4.3), et soit $\mathbf{w}$ quelconque, $\mathbf{z} = \mathbf{X}\mathbf{w}$. Dans (3.1), séparons les exemples selon le signe de $(\mathbf{X}\mathbf{d})_i$ ; quand $(\mathbf{X}\mathbf{d})_i < 0$, (4.3) impose $y_i = 0$, donc le terme $i$ vaut $-e^{z_i + s(\mathbf{X}\mathbf{d})_i}$ (avec $\ln 0! = 0$) :
$$\ell(\mathbf{w} + s\mathbf{d}) = \sum_{i\,:\,(\mathbf{X}\mathbf{d})_i = 0}\big[y_iz_i - e^{z_i} - \ln(y_i!)\big] \;-\; \sum_{i\,:\,(\mathbf{X}\mathbf{d})_i < 0} e^{z_i + s(\mathbf{X}\mathbf{d})_i}.$$
La première somme ne dépend pas de $s$. Par (H2), $\mathbf{X}\mathbf{d} \ne \mathbf{0}$ : la seconde n'est pas vide, et chacun de ses termes est strictement croissant en $s$ ($\exp$ est strictement croissante, R6 §1, et $(\mathbf{X}\mathbf{d})_i < 0$). Donc $\ell(\mathbf{w} + \mathbf{d}) > \ell(\mathbf{w})$ : aucun $\mathbf{w}$ n'est un maximum. ∎ Le long de $\mathbf{d}$, $\ell$ croît vers une limite finie sans l'atteindre, $\lVert\mathbf{w}\rVert \to \infty$, et les moyennes $\mu_i$ des exemples où $(\mathbf{X}\mathbf{d})_i < 0$ tendent vers 0 : le modèle voudrait des moyennes nulles, que $e^{z_i}$ n'atteint jamais.

<details><summary>Démonstration du « si » (plus longue, hors du chemin principal de l'article)</summary>

Supposons qu'aucune direction ne vérifie (4.3). Chaque terme de (3.1), $f_i(t) = y_it - e^t - \ln(y_i!)$, est majoré par un nombre $M_i$ : si $y_i > 0$, $f_i$ est maximale en $t = \ln y_i$ (M05a §2) ; si $y_i = 0$, $f_i = -e^t < 0$. Et $f_i(t) \to -\infty$ quand $t \to +\infty$ ($e^t$ l'emporte sur $y_it$, R6 §5) ; si $y_i > 0$, aussi quand $t \to -\infty$ ($y_it \to -\infty$ et $-e^t < 0$).

Sur la sphère unité $\lbrace \mathbf{u} : \lVert\mathbf{u}\rVert = 1 \rbrace$, posons $m(\mathbf{u}) = \max\big(\max_i\,(\mathbf{X}\mathbf{u})_i,\ \max_{i : y_i > 0}\,-(\mathbf{X}\mathbf{u})_i\big)$ (le second maximum est omis s'il n'y a aucun $y_i > 0$). Si $m(\mathbf{u}) \le 0$, alors $\mathbf{X}\mathbf{u} \le \mathbf{0}$, et $(\mathbf{X}\mathbf{u})_i \ge 0$, donc $(\mathbf{X}\mathbf{u})_i = 0$, pour $y_i > 0$ : $\mathbf{u}$ vérifierait (4.3). Donc $m > 0$ sur la sphère. $m$ est continue (un maximum de fonctions linéaires) et la sphère est fermée et bornée : $m$ y atteint son minimum $c > 0$ (admis : une fonction continue sur un fermé borné atteint ses extrema, M05a §2 en dimension 1, M05b §7).

Soit $\mathbf{w} \ne \mathbf{0}$, $r = \lVert\mathbf{w}\rVert$ et $\mathbf{u} = \mathbf{w}/r$. Comme $m(\mathbf{u}) \ge c$, il existe un $i$ tel que, ou bien $z_i = r\,(\mathbf{X}\mathbf{u})_i \ge cr$, ou bien $y_i > 0$ et $z_i \le -cr$. Dans les deux cas, $f_i(z_i) \le F(cr)$, où $F(s) = \max_i\max\big(\sup_{t \ge s}f_i(t),\ \sup_{t \le -s}f_i(t)\ \text{si } y_i > 0\big)$ tend vers $-\infty$ quand $s \to +\infty$. Donc $\ell(\mathbf{w}) \le \sum_{k \ne i}M_k + f_i(z_i) \le C + F(c\lVert\mathbf{w}\rVert)$, avec $C = \sum_kM_k - \min_kM_k$ : $\ell(\mathbf{w}) \to -\infty$ quand $\lVert\mathbf{w}\rVert \to \infty$.

L'ensemble $S = \lbrace \mathbf{w} : \ell(\mathbf{w}) \ge \ell(\mathbf{0}) \rbrace$ est donc borné ; il est fermé ($\ell$ est continue) et contient $\mathbf{0}$. $\ell$ y atteint un maximum (le même résultat admis), qui est un maximum sur tout $\mathbb{R}^p$, puisque $\ell < \ell(\mathbf{0})$ hors de $S$. ∎ L'existence et l'unicité pour ces modèles sont étudiées par Haberman (1974) et Wedderburn (1976) ; cette démonstration est rédigée ici sans les suivre.

</details>

**Le cas où une hypothèse tombe.** La cellule « cas limite » montre les trois hypothèses qui tombent, sur des nombres :
- **(H4)** : six soirées sans moustiquaire (feature 0 : 2, 0, 3, 1, 4 et 1 piqûres) et six avec (feature 1 : aucune piqûre). $\mathbf{d} = (0, -1)$ vérifie (4.3) : $(\mathbf{X}\mathbf{d})_i = -1$ avec moustiquaire, où $y_i = 0$, et 0 sans. Par le théorème 3 (c), il n'y a pas de maximum : $\ell$ croît strictement le long de $\mathbf{d}$, vers une limite finie qu'elle n'atteint pas, et `fit` lève `NoMaximumError`. Le modèle dit que la moustiquaire multiplie la moyenne par $e^{w_2}$ ; les données poussent ce facteur vers 0, que $e^{w_2}$ n'atteint pour aucun $w_2$ fini. L'expérience de §8 suit les itérés de Newton.
- **(H2)** : l'exemple de §5 avec une troisième colonne égale à deux fois la feature : `check_data` refuse ces données, et $\ell$ est constante le long du noyau, donc un maximum, s'il existe, n'est pas unique (propriété 1).
- **(H3)** : l'exemple de §5 sans sa colonne de 1 : le maximum existe, mais (4.2) n'est plus vraie.
"""

LIMIT_CODE = r'''
def limit_case():
    """The three hypotheses that fail (§4): no maximum (H4), dependent columns (H2), no column of ones (H3)."""
    # (H4) the mosquito net: six evenings without (2, 0, 3, 1, 4, 1 bites), six with (no bite)
    X_net = np.column_stack([np.ones(12), [0] * 6 + [1] * 6])
    y_net = np.array([2, 0, 3, 1, 4, 1] + [0] * 6, dtype=float)
    d = np.array([0.0, -1.0])
    print("(H4) X d =", (X_net @ d).astype(int).tolist(), "; comptages =", y_net.astype(int).tolist())
    start = np.array([math.log(11 / 6), 0.0])          # the best intercept for the evenings without a net
    for s in [0, 1, 2, 5, 10, 20]:
        print(f"     l(w + {s:2d} d) = {pn.log_likelihood(start + s * d, X_net, y_net):.9f}")
    steps = None
    try:
        pn.fit(X_net, y_net)
    except pn.NoMaximumError as exc:
        steps, last = len(exc.history) - 1, exc.history[-1]
        print(f"     fit lève NoMaximumError après {steps} pas, en w = {np.round(last, 4).tolist()} :")
        print("     " + str(exc).split(". Look")[0] + ".")
    # (H2) a third column equal to twice the feature of §5
    X_hand = np.column_stack([np.ones(5), [-2.0, -1.0, 0.0, 2.0, 4.0]])
    y_hand = np.array([0.0, 0.0, 3.0, 4.0, 4.0])
    X_dep = np.column_stack([X_hand, 2 * X_hand[:, 1]])
    try:
        pn.check_data(X_dep, y_hand)
    except ValueError as exc:
        print(f"(H2) check_data refuse : {exc}")
    w_hat = pn.fit(X_hand, y_hand).w
    v = np.array([0.0, 2.0, -1.0])                      # X_dep v = 0
    values = [pn.log_likelihood(np.append(w_hat, 0.0) + s * v, X_dep, y_hand) for s in (0, 1, 10)]
    print("     X v =", (X_dep @ v).tolist(), "; l le long de v (s = 0, 1, 10) :", np.round(values, 9).tolist())
    # (H3) the example of §5 without its column of ones
    w_no_one = pn.fit(X_hand[:, 1:], y_hand).w
    total = pn.mean(w_no_one, X_hand[:, 1:]).sum()
    print(f"(H3) sans colonne de 1 : w = {np.round(w_no_one, 6).tolist()}, somme des moyennes ajustées "
          f"{total:.2f} pour {y_hand.sum():.0f} piqûres")
    return {"H4: steps before NoMaximumError": steps, "H3: sum of the fitted means": round(float(total), 2)}
'''

LIMIT_CHECK = r'''
# Cell « cas limite » (PS.4)
print(limit_case())
'''

HAND = r"""
## 5. Un exemple à la main

**Les données.** Cinq soirées d'été, avec $x$ l'écart de la température du soir à la normale de saison (en °C) et $y$ le nombre de piqûres de moustique relevées :

| soirée $i$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $x_i$ (°C) | $-2$ | $-1$ | $0$ | $2$ | $4$ |
| $y_i$ | 0 | 0 | 3 | 4 | 4 |

$\mathbf{X}$ a deux colonnes, $\mathbf{1}$ et $\mathbf{x}$ : $n = 5$, $p = 2$, et $\mathbf{w} = (w_1, w_2)$, ordonnée à l'origine et pente.

**Le contrôle de vraisemblance, annoncé avant le calcul.** (a) Les comptages croissent avec $x$ : la pente $\hat{w}_2$ doit être positive. (b) Sans la feature, (3.10) donne $\ln\bar{y} = \ln\frac{11}{5} \approx 0{,}788$ ; les données vont de 0 à 4 piqûres sur 6 °C, donc $e^{6\hat{w}_2}$, le rapport des moyennes ajustées extrêmes, doit être de l'ordre de 10, soit $\hat{w}_2$ de l'ordre de $\frac16\ln 10 \approx 0{,}4$. (c) Par la propriété 2, $\sum_i\hat{\mu}_i = 11$. (d) $\det(\mathbf{X}^\top\mathbf{X})$ est un entier : (3.8) donne des fractions de dénominateur un diviseur de ce déterminant.

**Le premier pas, en fractions.** En $\mathbf{w}_0 = \mathbf{0}$ : $\mathbf{z} = \mathbf{0}$, $\boldsymbol{\mu} = \mathbf{1}$, et, par (3.1),
$$\ell(\mathbf{0}) = \sum_i (0 - 1) - \sum_i\ln(y_i!) = -5 - (\ln 6 + 2\ln 24) \approx -13{,}147867$$
($0! = 1$, $3! = 6$, $4! = 24$). Avec $\mathbf{y} - \mathbf{1} = (-1, -1, 2, 3, 3)$, (3.2) donne
$$\nabla\ell(\mathbf{0}) = \mathbf{X}^\top(\mathbf{y} - \mathbf{1}) = \begin{pmatrix} -1 - 1 + 2 + 3 + 3 \\ (-2)(-1) + (-1)(-1) + 0 \cdot 2 + 2 \cdot 3 + 4 \cdot 3 \end{pmatrix} = \begin{pmatrix} 6 \\ 21 \end{pmatrix},$$
et (3.3), avec $\mathbf{W} = \mathbf{I}$, $\sum_ix_i = 3$ et $\sum_ix_i^2 = 4 + 1 + 0 + 4 + 16 = 25$ :
$$\nabla^2\ell(\mathbf{0}) = -\mathbf{X}^\top\mathbf{X} = -\begin{pmatrix} 5 & 3 \\ 3 & 25 \end{pmatrix}, \qquad \det(\mathbf{X}^\top\mathbf{X}) = 125 - 9 = 116.$$
Par (3.8), avec l'inverse d'une matrice $2 \times 2$ (M09a §7) :
$$\boldsymbol{\delta}_0 = \frac{1}{116}\begin{pmatrix} 25 & -3 \\ -3 & 5 \end{pmatrix}\begin{pmatrix} 6 \\ 21 \end{pmatrix} = \frac{1}{116}\begin{pmatrix} 150 - 63 \\ -18 + 105 \end{pmatrix} = \frac{1}{116}\begin{pmatrix} 87 \\ 87 \end{pmatrix} = \begin{pmatrix} 3/4 \\ 3/4 \end{pmatrix}.$$
*Contrôle* : remis dans le système $\mathbf{X}^\top\mathbf{X}\,\boldsymbol{\delta}_0 = \mathbf{X}^\top(\mathbf{y} - \mathbf{1})$ dont (3.8) est la solution, $\mathbf{X}^\top\mathbf{X}\,\boldsymbol{\delta}_0 = \big(5 \cdot \frac34 + 3 \cdot \frac34,\ 3 \cdot \frac34 + 25 \cdot \frac34\big) = (6, 21) = \mathbf{X}^\top(\mathbf{y} - \mathbf{1})$. Le dénominateur 4 divise bien $116 = 4 \times 29$ (contrôle (d)). L'égalité des deux coordonnées est une coïncidence de ces données.

**Le pas plein est refusé.** En $\boldsymbol{\delta}_0 = (\frac34, \frac34)$, $\mathbf{z} = \frac34 + \frac34\,\mathbf{x} = (-\frac34, 0, \frac34, \frac94, \frac{15}{4})$, exactement ; les moyennes $e^{z_i} \approx (0{,}4724 ;\ 1 ;\ 2{,}1170 ;\ 9{,}4877 ;\ 42{,}5211)$ ne sont plus rationnelles, sauf $e^0 = 1$ (4 décimales gardées), de somme $\approx 55{,}5982$ pour 11 piqûres observées. Avec $\sum_iy_iz_i = 0 + 0 + \frac94 + 9 + 15 = \frac{105}{4}$, (3.1) donne $\ell(\boldsymbol{\delta}_0) \approx 26{,}25 - 55{,}5982 - 8{,}1479 \approx -37{,}496$, **plus bas** que $\ell(\mathbf{0})$ : le pas plein va trop loin (la pente $\frac34$ est une pente de comptages, pas de logarithmes). Le garde-fou de (3.5) essaie $t_0 = \frac12$ : $\mathbf{w}_1 = (\frac38, \frac38)$, $\mathbf{z} = (-\frac38, 0, \frac38, \frac98, \frac{15}{8})$, $\sum_ie^{z_i} \approx 12{,}7433$, $\sum_iy_iz_i = \frac{105}{8}$, et $\ell(\mathbf{w}_1) \approx 13{,}125 - 12{,}7433 - 8{,}1479 \approx -7{,}766$ : il monte, le demi-pas est pris.

**La suite, par le code** (les moyennes ne sont plus rationnelles) : la cellule ci-dessous donne les itérés. Dès $\mathbf{w}_1$, les pas sont pleins ; `fit` s'arrête après 6 pas, quand $\max_j\lvert\delta_j\rvert$ ne dépasse plus $10^{-10}(1 + \max_j\lvert w_j\rvert)$, le critère de §3.4, en $\hat{\mathbf{w}} \approx (0{,}317805 ;\ 0{,}335278)$.

**Le résultat, et les contrôles annoncés.** (a) $\hat{w}_2 \approx 0{,}335 > 0$. (b) $e^{6\hat{w}_2} \approx 7{,}5$, de l'ordre de 10, et $\hat{w}_2$ est proche de l'ordre de grandeur annoncé, 0,4. (c) $\hat{\boldsymbol{\mu}} \approx (0{,}7028 ;\ 0{,}9827 ;\ 1{,}3741 ;\ 2{,}6868 ;\ 5{,}2536)$, de somme 11, à l'arrondi près. Chaque degré multiplie le nombre moyen de piqûres par $e^{\hat{w}_2} \approx 1{,}40$. Les erreurs types (3.9) valent environ $0{,}44$ et $0{,}15$ : avec cinq soirées, l'approximation asymptotique est grossière, et la pente n'est qu'à 2,3 erreurs types de 0.

**Le modèle sans feature**, sur les mêmes comptages : $\bar{y} = \frac{11}{5} > 1$, donc (3.10) donne $w_1 = \bar{y} - 1 = \frac65 = 1{,}2$, au-delà du maximum $w^\star = \ln\frac{11}{5} \approx 0{,}788457$ ; puis les écarts $u_k = w_k - w^\star$ décroissent et sont à peu près élevés au carré à chaque pas, $u_{k+1}/u_k^2 \to \frac12$ (cellule suivante).
"""

HAND_CODE = r'''
# What was found by hand (§5), and the tolerance of the comparison
X_HAND = np.column_stack([np.ones(5), [-2.0, -1.0, 0.0, 2.0, 4.0]])
Y_HAND = np.array([0.0, 0.0, 3.0, 4.0, 4.0])
HAND_RESULT = {"delta_0": [Fraction(3, 4), Fraction(3, 4)],           # Eq. (3.8), by hand
               "w_1 (t_0 = 1/2)": [Fraction(3, 8), Fraction(3, 8)],
               "l(0)": -5 - (math.log(6) + 2 * math.log(24)),
               "w* without feature": math.log(Fraction(11, 5))}
# Tolerance 1e-12: the module works in float64; a QR on X (condition number 2.4) and a few sums of five terms of
# size at most 25 lose at most a few units of 1e-15. 1e-12 leaves room, and still catches any wrong fraction.
TOLERANCE = 1e-12


def hand_example():
    """The same quantities, computed by the module on the data of §5."""
    result = pn.fit(X_HAND, Y_HAND)
    return {"delta_0": pn.newton_direction(np.zeros(2), X_HAND, Y_HAND),
            "w_1 (t_0 = 1/2)": result.history[1],
            "l(0)": pn.log_likelihood(np.zeros(2), X_HAND, Y_HAND),
            "w* without feature": pn.intercept_only(Y_HAND)}
'''

HAND_CHECK = r'''
# Cell « vérification de l'exemple » (PS.5): the hand result against the module
def shown(value):
    """A value of HAND_RESULT as it is written by hand: fractions as p/q, floats with 9 digits."""
    if isinstance(value, list):
        return "(" + ", ".join(str(v) for v in value) + ")"
    return f"{value:.9f}"


computed = hand_example()
gaps = {key: float(np.max(np.abs(np.array(computed[key], dtype=float) - np.array(value, dtype=float))))
        for key, value in HAND_RESULT.items()}
for key, gap in gaps.items():
    print(f"  {key:20s} à la main {shown(HAND_RESULT[key]):14s} module {np.round(computed[key], 12)!s:28s} "
          f"écart {gap:.1e}")
largest = max(gaps.values())
print(f"{'✅' if largest <= TOLERANCE else '❌'} écart le plus grand entre le calcul à la main et le module : "
      f"{largest:.1e} (tolérance {TOLERANCE:g})")
# The exact first step, again, with fractions only (Gauss on the 2 x 2 normal equations of Eq. (3.8))
a, b, c = 5, 3, 25                                  # X^T X
g1, g2 = Fraction(6), Fraction(21)                  # X^T (y - 1)
det = a * c - b * b
print("δ₀ en fractions :", ((c * g1 - b * g2) / det, (a * g2 - b * g1) / det))
'''

HAND_TABLE = r'''
# The iterates of fit on the example (Eq. (3.5)), the fitted means, and the model without feature (Eq. (3.10))
result = pn.fit(X_HAND, Y_HAND)
print(" k   w_k                          l(w_k)        t_k")
for k, (w, value) in enumerate(zip(result.history, result.log_likelihoods)):
    t = f"{result.step_sizes[k]:g}" if k < len(result.step_sizes) else ""
    print(f"{k:2d}   {np.array2string(w, precision=6, floatmode='fixed'):27s}  {value:12.6f}  {t}")
mu_hat = pn.mean(result.w, X_HAND)
print("moyennes ajustées :", np.round(mu_hat, 4).tolist(), "; somme :", round(mu_hat.sum(), 12), "(11 piqûres)")
print("e^(6 w2) =", round(math.exp(6 * result.w[1]), 2), "; e^(w2) =", round(math.exp(result.w[1]), 4),
      "; erreurs types (3.9) :", np.round(pn.standard_errors(result.w, X_HAND), 4).tolist())
w_star, w, gaps = math.log(11 / 5), 0.0, []
for _ in range(7):                                  # Eq. (3.10) from w0 = 0
    gaps.append(w - w_star)
    w = w + (11 / 5) * math.exp(-w) - 1
print("modèle sans feature, u_k = w_k − ln(11/5) :", [f"{u:.3e}" for u in gaps])
print("u_(k+1) / u_k² :", [round(gaps[k + 1] / gaps[k] ** 2, 4) for k in range(1, 5)])
'''

IMPLEMENTATION = r"""
## 6. L'implémentation

Le module [`poisson_newton.py`](poisson_newton.py) suit la table des formules finales de §3 : une fonction publique par formule, dont la docstring (en anglais, au format NumPy) dit ce qu'elle calcule, son équation, ses paramètres avec leurs formes, ce qu'elle rend et les erreurs qu'elle lève. Il n'importe que NumPy, `math` et `mymath`.

- **Les fonctions de `mymath`**, chacune utile au calcul : `orthogonal.least_squares_qr` résout les moindres carrés pondérés (3.6) de chaque pas ; `svd_pca.condition_number` vérifie (H2) dans `check_data`, puis, à chaque itération de `fit`, que les poids $\sqrt{\mu_i}$ ne s'effondrent pas (le symptôme du théorème 3 ; quand tous les comptages sont nuls, les poids s'effondrent ensemble et le conditionnement ne bouge pas, celui de $\mathbf{X}$ tout du long : c'est alors le second diagnostic, après `max_iter` pas, qui lève `NoMaximumError`) ; `eigen.cholesky` factorise $\mathbf{X}^\top\hat{\mathbf{W}}\mathbf{X}$ pour les erreurs types (3.9) ; `approx.newton` résout (3.10) ; `iterative.critical_step_size` donne $\eta_c$ (3.12).
- **Les erreurs** : `check_data` lève `ValueError` pour des comptages négatifs, non entiers ou non finis, des formes incompatibles, des colonnes liées, et `log_likelihood` pour des comptages invalides. `fit` lève `NoMaximumError` (une sous-classe de `RuntimeError`, qui garde les itérés) quand il voit le symptôme d'un maximum qui n'existe pas : le conditionnement de $\mathbf{W}^{1/2}\mathbf{X}$ dépasse $10^6$ alors que la moyenne ajustée d'un comptage nul est passée sous $10^{-8}$, ou, après `max_iter` pas sans convergence, une telle moyenne. Sinon, il lève `RuntimeError` : pas de convergence en `max_iter` pas, ou un conditionnement qui dépasse $10^6$ sans moyenne d'un comptage nul près de 0 (une feature à centrer).
- **Le coût** d'une itération de `fit` : former $\mathbf{W}^{1/2}\mathbf{X}$ coûte $O(np)$, la QR $O(np^2)$ (M12b §7), le conditionnement $O(np^2 + p^3)$ (la SVD de `mymath` passe par $\mathbf{B}^\top\mathbf{B}$, M12d §4), la log-vraisemblance du garde-fou $O(np)$ par essai : en tout $O(np^2)$ par itération, pour une dizaine d'itérations au plus ici. Un pas de montée de gradient (3.11) coûte $O(np)$, mais il en faut de l'ordre de $\kappa$ fois plus (§8).
- **Sans boucle sur les exemples** : les sommes de (3.1) à (3.3) sont des produits de NumPy, et $\ln(y_i!)$ se lit dans une somme cumulée de logarithmes ($\ln 1 + \cdots + \ln m$), calculée une fois pour toutes les valeurs de $\mathbf{y}$. Les seules boucles Python sont celles des itérations et des divisions du pas par deux.

La cellule « Contrôle du module » lit `poisson_newton.py` sans l'exécuter : ses fonctions publiques et leurs docstrings (**API** ; une fonction qui ne cite aucune équation, comme `check_data`, reçoit une note ℹ️, normale pour une vérification des données), les fonctions de `mymath` qu'il appelle (**mymath** ; dans ton projet, elles doivent être marquées « à toi »), et ses imports (**imports**).
"""

CONTROL_CODE = r'''
# Cell « Contrôle du module » (PS.6): reads poisson_newton.py without running it
FORBIDDEN = {"sklearn", "torch", "scipy", "sympy", "tensorflow", "jax", "statsmodels"}   # the oracles of PS.7
tree = ast.parse((PROJECT / "poisson_newton.py").read_text(encoding="utf-8"))
print("API :")
for node in tree.body:
    if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and not node.name.startswith("_"):
        doc = ast.get_docstring(node) or ""
        needed = ("Parameters", "Returns", "Raises") if isinstance(node, ast.FunctionDef) else ("Attributes",)   # the kit
        missing = [part for part in needed if part not in doc]
        equation = bool(re.search(r"\((?:2|3|4)\.\d+\)", doc))
        mark = "✅" if doc and not missing else "⚠️"
        note = "" if doc and not missing else f" (docstring {'absente' if not doc else 'sans ' + ', '.join(missing)})"
        note += ("" if equation or isinstance(node, ast.ClassDef) else
                 " ℹ️ aucune équation citée : normal seulement pour une fonction qui ne calcule pas une formule de §3 "
                 "(vérification des données)")
        print(f"  {mark} {node.name} : {doc.splitlines()[0] if doc else '—'}{note}")
print("mymath :")
modules = {alias.name for node in ast.walk(tree) if isinstance(node, ast.ImportFrom) and node.module == "mymath"
           for alias in node.names}
calls = sorted({(node.value.id, node.attr) for node in ast.walk(tree)
                if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id in modules})
for module, function in calls:
    mine = (ROOT / "mon_travail" / "mymath" / f"{module}.py").exists() and mymath.__wb_impl__ == "learner"
    print(f"  {'✅ à toi    ' if mine else 'ℹ️ référence'} mymath.{module}.{function}")
print(f"  {len(calls)} fonctions de mymath appelées ; l'exemple tourne sur la référence (setup de solution), "
      "ton projet appelle les tiennes")
print("imports :")
for node in ast.walk(tree):
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module or "."]
        for name in [n for n in names if n != "__future__"]:
            top = name.split(".")[0]
            allowed = top in {"numpy", "mymath"} or top in sys.stdlib_module_names
            print(f"  {'❌' if top in FORBIDDEN else '✅' if allowed else '⚠️'} {name}")
'''

DEMO_CODE = r'''
# The module at work: a fit, its standard errors, and the errors it raises on invalid data
print(pn.fit(X_HAND, Y_HAND))
for label, y_bad in [("un comptage négatif", [0, 0, -2, 4, 4]), ("un comptage non entier", [0, 0, 2.5, 4, 4]),
                     ("une mauvaise longueur", [0, 0, 3])]:
    try:
        pn.fit(X_HAND, y_bad)
    except ValueError as exc:
        print(f"{label:24s} → ValueError : {exc}")
'''

MYMATH_TESTS = r'''
# The tests of the five functions of mymath that the module calls (in your project: with your code, impl="learner")
for test_file, keyword in [("tests/test_m12b_orthogonal.py", "least_squares_qr"),
                           ("tests/test_m12d_svd_pca.py", "condition_number"),
                           ("tests/test_m12c_eigen.py", "cholesky"),
                           ("tests/test_m05a_approx.py", "newton"),
                           ("tests/test_m19_iterative.py", "critical_step_size")]:
    print(f"— {keyword} : {test_file}")
    run_pytest_group(test_file, keyword, impl="ref")
'''

VERIFICATION = r"""
## 7. La vérification

Les tests sont dans [`test_poisson_newton.py`](test_poisson_newton.py) ; [`conftest.py`](conftest.py) est celui du kit, recopié (il charge `mymath` selon `--impl` et applique `--mutant`). Les oracles ne dépendent ni du module ni de `mymath`, et aucune formule de §3 n'est recopiée dans les tests :

| Ce qui est vérifié | Oracle | Cas | Tolérance, et pourquoi |
|---|---|---|---|
| `fit` (3.5) | scikit-learn `PoissonRegressor(alpha=0, fit_intercept=False, solver="newton-cholesky", tol=1e-9)`, la colonne de 1 dans $\mathbf{X}$ | 3 tailles × 3 graines, et l'exemple de §5 | $10^{-7}$ relatif + $10^{-8}$ : scikit-learn s'arrête quand le gradient de son objectif moyen passe sous $10^{-9}$, d'où une erreur sur $\mathbf{w}$ inférieure à $10^{-9}$ ici |
| `fit` (3.5) | `scipy.optimize.minimize` (BFGS, son propre gradient par différences à 3 points) sur $-\ell$ écrite avec `scipy.stats.poisson.logpmf` | 3 × 3 | $5 \cdot 10^{-6}$ : l'arrêt de BFGS, `gtol` $= 10^{-6}\,n$, divisé par $\lambda_{\min}$ |
| `log_likelihood` (3.1) | la somme de `scipy.stats.poisson.logpmf` | 3 × 3 | $10^{-11}(1 + \lvert\ell\rvert)$ : l'arrondi d'une somme de $n$ termes |
| `gradient` (3.2) | différences centrées de l'oracle de $\ell$, $h = 10^{-5}$ (M05a §5 et §7) | 3 × 3 | $10^{-6}$ + $10^{-7}$ relatif : l'erreur $h^2\lvert\ell'''\rvert/6 + \varepsilon\lvert\ell\rvert/h$ reste sous $10^{-6}$ pour $\lvert\ell\rvert \le 10^3$ et $\lvert\ell'''\rvert \le 3 \cdot 10^3$ |
| `hessian` (3.3) | différences secondes centrées, $h = 10^{-4}$ (M19 §1 : $h \approx \varepsilon^{1/4}$) | 3 × 3 | $10^{-4} + 10^{-6}\max\lvert H_{jk}\rvert$ |
| `newton_direction` (3.4), (3.6) | la solution de $\mathbf{H}\boldsymbol{\delta} = -\nabla\ell$, $\mathbf{H}$ et $\nabla\ell$ par différences, `numpy.linalg.solve` | 3 × 3 | $10^{-6}(1 + \max\lvert\delta_j\rvert)$ |
| `standard_errors` (3.9), `critical_learning_rate` (3.12), `gradient_ascent` (3.11) | `numpy.linalg.inv` et `eigvalsh` de la hessienne par différences ; scikit-learn | 3 graines ; 1 pour `gradient_ascent` | $10^{-5}$ et $10^{-6}$ relatifs ; $10^{-8}$ après 3 000 pas |
| propriété 1 | les valeurs propres de la hessienne (`eigvalsh`) ; trois départs tirés au hasard | 3 graines | $\lambda_{\max} < 0$ ; $10^{-9}$ |
| propriété 2, et le gradient nul au maximum | (4.2) ; différences centrées de l'oracle de $\ell$ | 3 × 3 | $10^{-9}$ relatif ; $10^{-6}$ |
| une invariance | décaler une feature de $c$ ne change que l'ordonnée à l'origine, de $-c\,\hat{w}_j$ | 2 décalages | $10^{-9}$ |
| l'exemple de §5 | `fractions.Fraction`, `math.factorial` et `math.log` | | $10^{-12}$ |
| les erreurs | (H1) et (H2) : `ValueError` de `check_data`, et de `log_likelihood` pour des comptages invalides ; le théorème 3 : `NoMaximumError` au pas 28 sur les soirées à moustiquaire, et sans comptage non nul ; (c) quand le groupe sans comptage est celui où la feature vaut 0 : `NoMaximumError` avec la colonne de 1, le maximum $\ln\frac72$ (`math.log`) sans elle ; une feature non centrée, comptages tous $\ge 1$ : `RuntimeError`, pas `NoMaximumError`, et la feature centrée donne le point de scikit-learn | | |

Les données tirées au hasard ont $\mathbf{X} = [\mathbf{1}, \text{features} \sim \mathcal{N}(0, 1)]$ et des comptages tirés du modèle (graines 9010 à 9012 pour les tailles $(n, p) = (20, 2)$, $(100, 3)$ et $(500, 5)$, 9020 à 9026 pour les autres tests). La première ligne de chaque message d'échec dit ce qui était attendu.
"""

TESTS_CODE = r'''
# The tests of the example (PS.7), on the reference of mymath
tests = run_pytest_group(TEST_FILE, impl="ref", root=PROJECT)
'''

MUTATION_MD = r"""
**La mutation.** [`mutants.py`](mutants.py) contient deux copies fautives, chacune avec **une** erreur plausible : les poids $\mu_i$ oubliés, une fois dans `newton_direction` (les moindres carrés de $\mathbf{y} - \boldsymbol{\mu}$ sur $\mathbf{X}$ sans pondération, c'est-à-dire le pas de la hessienne $-\mathbf{X}^\top\mathbf{X}$), une fois dans `hessian`. La cellule « mutation » relance les tests avec la première à la place de l'original (`python -m pytest test_poisson_newton.py --impl=ref --mutant=newton_direction`), puis avec la seconde.
"""

MUTATION_CODE = r'''
# Cell « mutation » (PS.7): the tests against two deliberate mistakes
for MUTANT in ["newton_direction", "hessian"]:
    print(f"— --mutant={MUTANT}")
    mutated = run_pytest_group(TEST_FILE, impl="ref", root=PROJECT, args=[f"--mutant={MUTANT}"], max_shown=6)
    print(f"{'✅' if mutated.failed else '❌'} la mutation {MUTANT} est attrapée : {mutated.failed} test(s) en échec\n")
'''

MUTATION_COMMENT = r"""
**Qui attrape quoi.** Sans les poids dans `newton_direction`, les points fixes de l'itération restent les zéros du gradient, donc un résultat final juste reste possible ; mais l'itération n'est plus celle de Newton : elle converge lentement, et `fit` ne converge plus en 100 pas (les tests contre scikit-learn et SciPy, la propriété 2, l'invariance échouent sur `RuntimeError`), et la direction diffère de $-\mathbf{H}^{-1}\nabla\ell$ (`test_newton_direction_matches_finite_differences`). Les valeurs de l'exemple à la main ne la voient **pas** : en $\mathbf{w} = \mathbf{0}$, tous les poids valent 1, et la mutation ne change ni $\boldsymbol{\delta}_0$ ni $\mathbf{w}_1$ (`test_hand_example_first_direction_is_least_squares_of_y_minus_1` passe, et `test_hand_example_full_step_is_refused_and_half_step_taken` n'échoue que parce que `fit` ne converge plus en 100 pas) : un exemple calculé en un seul point ne suffit pas. Sans les poids dans `hessian`, `fit` reste juste (il n'appelle pas `hessian`) : seuls la comparaison aux différences secondes et les deux fonctions qui utilisent la hessienne (`standard_errors`, `critical_learning_rate`) l'attrapent. D'où l'intérêt de tester chaque dérivée à part, et pas seulement le résultat final.
"""

EXPERIMENT = r"""
## 8. L'expérience

### 8.1 Newton contre une montée de gradient

**La question.** À quelle vitesse les itérés approchent-ils le maximum, avec la méthode de Newton (3.5) et avec la montée de gradient (3.11) de learning rate $\eta = 1/\lambda_{\max}$, la moitié du learning rate critique (3.12) ?

**Le protocole.** Trois datasets synthétiques (graines 9001, 9002 et 9003) de $n = 200$ soirées et deux features très corrélées ($x_2 = 0{,}95\,x_1 + \sqrt{1 - 0{,}95^2}\,\varepsilon$, avec $x_1$, $\varepsilon \sim \mathcal{N}(0, 1)$), pour que $\kappa$ soit grand ; comptages tirés du modèle avec $\mathbf{w} = (0{,}7 ;\ 0{,}45 ;\ -0{,}25)$. Les deux méthodes partent de $\mathbf{0}$ ; $\hat{\mathbf{w}}$ est le point final de `fit` (exact à l'arrondi). On trace $\lVert\mathbf{w}_k - \hat{\mathbf{w}}\rVert$ en fonction de $k$, à l'échelle logarithmique.

**La prédiction**, écrite le 21 novembre 2026, avant d'exécuter (`PREDICTION`, ci-dessous) : elle repose sur la convergence quadratique de Newton (M05a §4 en dimension 1, §3.7 ; énoncée sans démonstration en dimension $p$ : près d'un maximum où la hessienne est inversible, $\lVert\mathbf{e}_{k+1}\rVert \le C\,\lVert\mathbf{e}_k\rVert^2$) et sur (3.12), qui utilise le lemme de §4 ($\lambda_{\min} > 0$). La pente prédite pour la montée de gradient est calculée par la cellule à partir de la hessienne au maximum, **avant** de lancer la montée.
"""

EXPERIMENT_CODE = r'''
PREDICTION = ("Newton : une fois l'erreur sous 0,1 environ, chaque pas l'élève à peu près au carré (le rapport "
              "e_(k+1) / e_k² reste borné) ; le nombre de chiffres justes double, et l'erreur passe sous 1e-12 en au "
              "plus 7 pas depuis 0. Montée de gradient avec η = 1/λmax : convergence linéaire, une droite de pente "
              "log10(1 − 1/κ) sur la figure (3.12), κ étant le conditionnement de X^T Ŵ X ; il faut donc environ "
              "10 / (−log10(1 − 1/κ)) pas pour gagner 10 chiffres.")
SEEDS_EXPERIMENT = [9001, 9002, 9003]
FIGURE_NAME = "convergence.png"


def experiment_data(seed, n=200, rho=0.95):
    """Synthetic counts: X = [1, x1, x2] with corr(x1, x2) = rho, counts drawn with w = (0.7, 0.45, -0.25)."""
    rng = np.random.default_rng(seed)
    x1, noise = rng.normal(size=(2, n))
    X = np.column_stack([np.ones(n), x1, rho * x1 + math.sqrt(1 - rho ** 2) * noise])
    y = rng.poisson(np.exp(X @ np.array([0.7, 0.45, -0.25]))).astype(float)
    return X, y


def run_experiment(seed, max_steps=3000):
    """Newton's errors, the gradient ascent's errors, and the predicted factor 1 - 1/kappa (before the ascent)."""
    X, y = experiment_data(seed)
    newton = pn.fit(X, y)
    w_hat = newton.w
    newton_errors = np.array([np.linalg.norm(w - w_hat) for w in newton.history])
    A = -pn.hessian(w_hat, X)
    eigenvalues = np.linalg.eigvalsh(A)                              # an independent check of (3.12)
    kappa = eigenvalues[-1] / eigenvalues[0]
    kappa_svd = mymath.svd_pca.condition_number(np.sqrt(pn.mean(w_hat, X))[:, None] * X) ** 2   # M12d §4
    eta = pn.critical_learning_rate(w_hat, X) / 2                   # 1 / lambda_max
    predicted = math.log10(1 - 1 / kappa)                           # the prediction, before running the ascent
    ascent = pn.gradient_ascent(X, y, eta, max_steps)
    ascent_errors = np.linalg.norm(ascent - w_hat, axis=1)
    window = (ascent_errors < 1e-2) & (ascent_errors > 1e-9)        # the linear regime, above rounding
    steps = np.arange(max_steps + 1)
    measured = np.polyfit(steps[window], np.log10(ascent_errors[window]), 1)[0]
    return {"seed": seed, "newton": newton_errors, "ascent": ascent_errors, "kappa": kappa, "kappa_svd": kappa_svd,
            "eta": eta, "predicted": predicted, "measured": measured,
            "steps_1e-10": int(np.argmax(ascent_errors < 1e-10)), "newton_steps": newton.n_iter}


print("PREDICTION :", PREDICTION)
results = [run_experiment(seed) for seed in SEEDS_EXPERIMENT]
print("\ngraine   κ (valeurs propres)  κ (SVD de mymath)  pente prédite  pente mesurée  pas pour 1e-10 : montée, "
      "Newton")
for r in results:
    print(f"{r['seed']}   {r['kappa']:18.2f}  {r['kappa_svd']:17.2f}  {r['predicted']:13.5f}  {r['measured']:13.5f}"
          f"  {r['steps_1e-10']:14d}   {r['newton_steps']}")
first = results[0]["newton"]
print("\nNewton, graine 9001 : erreurs", [f"{e:.1e}" for e in first],
      "\n  e_(k+1) / e_k² :", [round(float(first[k + 1] / first[k] ** 2), 2) for k in range(len(first) - 1)
                                 if 1e-8 < first[k] < 0.1 and first[k + 1] > 0])
'''

EXPERIMENT_FIGURE = r'''
# Cell « expérience » (PS.8): the figure, checked and saved in figures/
fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
for r, marker in zip(results, ["o", "s", "^"]):
    keep = r["newton"] > 0
    left.semilogy(np.flatnonzero(keep), r["newton"][keep], marker=marker, lw=1.2, ms=5,
                  label=f"Newton (graine {r['seed']})")
left.set_xlabel("itération k (sans unité)")
left.set_ylabel(r"erreur $\|w_k - \hat{w}\|$ (sans unité, échelle log)")
left.set_title("Newton : quadratique (7 pas au plus)")
left.legend(fontsize=8)
for r, shade in zip(results, ["#1f77b4", "#ff7f0e", "#2ca02c"]):
    errors = r["ascent"]
    right.semilogy(np.flatnonzero(errors > 0), errors[errors > 0], color=shade, lw=1.4,
                   label=f"montée, η = 1/λmax (graine {r['seed']})")
    k0 = 300
    right.semilogy([k0, k0 + 700], [errors[k0], errors[k0] * 10 ** (700 * r["predicted"])], "k--", lw=1)
right.plot([], [], "k--", lw=1, label=r"pentes prédites $\log_{10}(1 - 1/\kappa)$")
right.set_xlabel("itération k (sans unité)")
right.set_title("Montée de gradient : linéaire, de pente prédite")
right.legend(fontsize=8)
right.set_ylim(1e-17, 3)
for ax in (left, right):
    for what, present in [("de nom pour l'axe des abscisses", ax.get_xlabel()),
                          ("de nom pour l'axe des ordonnées", left.get_ylabel()),
                          ("de titre", ax.get_title()), ("de légende", ax.get_legend())]:
        if not present:
            print(f"⚠️ la figure n'a pas {what}")
fig.tight_layout()
FIGURES.mkdir(exist_ok=True)
fig.savefig(FIGURES / FIGURE_NAME, dpi=120, bbox_inches="tight")
print(f"🖼️ enregistrée dans figures/{FIGURE_NAME} (les deux panneaux partagent l'axe des ordonnées)")
plt.show()
'''

EXPERIMENT_CONCLUSION = r"""
**Ce que montre la figure.** À gauche, les erreurs de Newton : sur la graine 9001, $9{,}2 \cdot 10^{-3}$, puis $6{,}6 \cdot 10^{-5}$, puis $3{,}7 \cdot 10^{-9}$, puis $8{,}7 \cdot 10^{-17}$, l'arrondi : le nombre de chiffres justes double à chaque pas, et le rapport $e_{k+1}/e_k^2$ reste borné (0,77 puis 0,84). Les trois graines finissent en 7, 7 et 6 pas. À droite, la montée de gradient suit une droite, jusqu'au plancher de l'arrondi, vers $10^{-16}$. Le tableau donne $\kappa \approx 37{,}7$, $48{,}9$ et $41{,}1$, la même valeur par les valeurs propres de $\mathbf{X}^\top\hat{\mathbf{W}}\mathbf{X}$ et par la SVD de $\hat{\mathbf{W}}^{1/2}\mathbf{X}$ de `mymath` (M12d §4) ; la pente mesurée sur la partie linéaire ($10^{-9} < e_k < 10^{-2}$) coïncide avec la pente prédite $\log_{10}(1 - 1/\kappa)$ aux cinq décimales affichées ($-0{,}01167$, $-0{,}00897$, $-0{,}01070$), et il faut 796, 1 099 et 922 pas pour passer sous $10^{-10}$.

**Conclusion.** La prédiction tient pour les deux méthodes et pour les trois graines. La montée de gradient a besoin d'un nombre de pas proportionnel à $\kappa$ (M19 §5) : la graine au $\kappa$ le plus grand demande le plus de pas. Newton, qui divise par la courbure, n'en dépend pas, au prix d'une QR en $O(np^2)$ par pas au lieu d'un produit en $O(np)$. La pente prédite vaut pour l'itération linéarisée : au début, quand l'erreur est proche de 1, la montée s'en écarte un peu, ce qui est attendu, puisque la hessienne n'y est pas celle du maximum.

### 8.2 Quand le maximum n'existe pas

**La question.** Que font les itérés de Newton sur les soirées à moustiquaire de §4, où (4.3) a une solution, $\mathbf{d} = (0, -1)$ ?

**La prédiction**, écrite le 21 novembre 2026, avant d'exécuter (`PREDICTION_NO_MAXIMUM`, ci-dessous). Elle vient d'un changement de coordonnées. Avec $a = w_1$ et $s = w_1 + w_2$ (les logarithmes des moyennes sans et avec moustiquaire), (3.1) se sépare : $\ell = (11a - 6e^a) + (0 \cdot s - 6e^s) - \text{const}$, puisque les six soirées sans moustiquaire ont 11 piqûres et les six autres aucune. La méthode de Newton ne dépend pas d'un changement de coordonnées linéaire $\mathbf{w} = \mathbf{T}\mathbf{v}$ ($\mathbf{T}$ inversible) : par la règle de la chaîne (M17 §3), le gradient en $\mathbf{v}$ est $\mathbf{T}^\top\nabla\ell$ et la hessienne $\mathbf{T}^\top\nabla^2\ell\,\mathbf{T}$, donc la direction en $\mathbf{v}$ est $-(\mathbf{T}^\top\nabla^2\ell\,\mathbf{T})^{-1}\mathbf{T}^\top\nabla\ell = \mathbf{T}^{-1}\boldsymbol{\delta}$, l'image de la même direction, et le garde-fou compare les mêmes valeurs de $\ell$. Dans les coordonnées $(a, s)$, la hessienne est diagonale, et chaque coordonnée suit sa propre méthode de Newton : $a$ celle de (3.10), avec $\bar{y} = \frac{11}{6}$, vers $\ln\frac{11}{6} \approx 0{,}606$ ; $s$ celle de la fonction $-6e^s$, dont le pas vaut $-\frac{-6e^s}{-6e^s} = -1$. D'où :
$$s_{k+1} = s_k - 1, \qquad s_k = -k \ \text{exactement} ; \qquad \lVert\mathbf{w}_k\rVert \approx k ; \qquad \sup\ell - \ell(\mathbf{w}_k) \approx 6\,e^{-k}. \tag{8.1}$$
Et `fit` s'arrête quand le conditionnement de $\mathbf{W}^{1/2}\mathbf{X}$ dépasse $10^6$, le seuil de `svd_pca.condition_number` : $\lambda_{\min}/\lambda_{\max}$ de $\mathbf{X}^\top\mathbf{W}\mathbf{X}$ vaut environ $6e^{-k}/11$, qui passe sous $10^{-12}$ pour $k \ge \ln\big(6 \cdot 10^{12}/11\big) \approx 27{,}03$, donc au pas 28.
"""

NO_MAXIMUM_CODE = r'''
PREDICTION_NO_MAXIMUM = ("s_k = w1 + w2 = −k exactement (pas plein à chaque itération), w1 → ln(11/6) ≈ 0,606, "
                         "‖w_k‖ ≈ k, sup l − l(w_k) ≈ 6 e^(−k), et NoMaximumError levée au pas 28.")
X_NET = np.column_stack([np.ones(12), [0] * 6 + [1] * 6])
Y_NET = np.array([2, 0, 3, 1, 4, 1] + [0] * 6, dtype=float)
SUP = 11 * math.log(11 / 6) - 11 - float(np.sum([math.lgamma(v + 1) for v in Y_NET]))   # l at a = ln(11/6), s = -inf
print("PREDICTION :", PREDICTION_NO_MAXIMUM)
run = gap_to_sup = None
try:
    pn.fit(X_NET, Y_NET)
    print("❌ fit a convergé : la prédiction est fausse")
except pn.NoMaximumError as exc:
    run = np.array(exc.history)
    gap_to_sup = SUP - np.array(exc.log_likelihoods)
print(f"NoMaximumError après {len(run) - 1} pas")
print("s_k = w1 + w2 :", np.round(run.sum(axis=1)[:8], 12).tolist(), "…", round(float(run[-1].sum()), 12))
print("w1 :", np.round(run[:6, 0], 6).tolist(), "; ln(11/6) =", round(math.log(11 / 6), 6))
print("‖w_k‖ − k aux pas 10, 20, 28 :", [round(float(np.linalg.norm(run[k]) - k), 4) for k in (10, 20, 28)])
print("(sup l − l(w_k)) / (6 e^(−k)) aux pas 2, 3, 4, 10 :",
      [round(float(gap_to_sup[k] / (6 * math.exp(-k))), 6) for k in (2, 3, 4, 10)])
'''

NO_MAXIMUM_FIGURE = r'''
# The run without maximum: the figure, checked and saved in figures/
fig, (left, right) = plt.subplots(1, 2, figsize=(9, 3.6))
k = np.arange(len(run))
left.plot(k, np.linalg.norm(run, axis=1), "o-", ms=3, color="#d62728", label=r"$\|w_k\|$ (Newton)")
left.plot(k, k, "k--", lw=1, label=r"prédiction (8.1) : $\|w_k\| \approx k$")
left.set_xlabel("itération k (sans unité)")
left.set_ylabel(r"$\|w_k\|$ (sans unité)")
left.set_title("Les itérés s'en vont à l'infini")
left.legend(fontsize=8)
right.semilogy(k[1:], gap_to_sup[1:], "o-", ms=3, color="#d62728", label=r"$\sup\ell - \ell(w_k)$")
right.semilogy(k[1:], 6 * np.exp(-k[1:]), "k--", lw=1, label=r"prédiction (8.1) : $6\,e^{-k}$")
right.set_xlabel("itération k (sans unité)")
right.set_ylabel(r"écart au sup de $\ell$ (nats, échelle log)")
right.set_title(r"$\ell$ monte vers son sup sans l'atteindre")
right.legend(fontsize=8)
for ax in (left, right):
    for what, present in [("de nom pour l'axe des abscisses", ax.get_xlabel()), ("de nom pour l'axe des ordonnées",
                          ax.get_ylabel()), ("de titre", ax.get_title()), ("de légende", ax.get_legend())]:
        if not present:
            print(f"⚠️ la figure n'a pas {what}")
fig.tight_layout()
fig.savefig(FIGURES / "sans_maximum.png", dpi=120, bbox_inches="tight")
print("🖼️ enregistrée dans figures/sans_maximum.png")
plt.show()
'''

NO_MAXIMUM_CONCLUSION = r"""
**Ce que montre la figure, et la conclusion.** La prédiction (8.1) tient exactement : $s_k = -k$ à l'arrondi près, $w_1$ atteint $\ln\frac{11}{6} \approx 0{,}606136$ en quatre pas, $\lVert\mathbf{w}_k\rVert - k$ se stabilise vers $0{,}61$ (la contribution de $w_1$), et l'écart au sup de $\ell$ suit $6e^{-k}$ (rapport 1 à $10^{-6}$ près dès le pas 4 ; au début, s'y ajoute l'écart de $w_1$ à sa limite). `fit` lève `NoMaximumError` au pas 28, comme prévu, avec un message qui dit quoi chercher. Sans le contrôle du conditionnement, la méthode ferait des pas de longueur 1 jusqu'à `max_iter` = 100, où le second diagnostic (une moyenne d'un comptage nul sous $10^{-8}$) lèverait `NoMaximumError` : le gradient tend vers 0, mais le pas garde la longueur 1, et le critère d'arrêt sur le pas ne se déclenche jamais. Le théorème 3 dit d'où vient la fuite : des six soirées à moustiquaire sans aucune piqûre, et non de la méthode de Newton.
"""

CONCLUSION = r"""
## 9. Conclusion et limites

**Ce que l'article établit.** De la log-vraisemblance (3.1), la règle de la chaîne donne le gradient (3.2) et la hessienne (3.3) ; le pas de Newton (3.4) est un problème de moindres carrés pondérés (3.6), résolu par QR, et le premier pas depuis $\mathbf{0}$ est rationnel (3.8), ce que l'exemple de §5 vérifie en fractions. Sous (H1) et (H2), la hessienne est définie négative (le lemme, la propriété 1) : le maximum, s'il existe, est unique, et le pas est une direction de montée, ce qui justifie le garde-fou (3.5). Avec une colonne de 1, les moyennes ajustées ont la somme des comptages (propriété 2). Le maximum existe si et seulement si (4.3) n'a pas de solution (théorème 3) ; sinon, les itérés s'en vont à l'infini selon (8.1), comme §8.2 le montre. Le module est vérifié contre deux bibliothèques et des différences finies, et deux mutations sont attrapées (§7) ; Newton converge en 6 ou 7 pas, la montée de gradient en un nombre de pas proportionnel à $\kappa$, avec le facteur $1 - 1/\kappa$ prédit, aux cinq décimales affichées (§8.1).

**Les limites.**
- **Ce qui est admis** : la convergence quadratique de Newton en dimension $p$ (démontrée ici en dimension 1 seulement, §3.7) ; l'écart entre la montée de gradient et sa linéarisation (3.12) ; la version matricielle de l'information de Fisher et le caractère asymptotique des erreurs types (3.9), grossier pour cinq soirées ; le théorème des bornes atteintes dans la démonstration du théorème 3.
- **Ce que le modèle suppose** : une variance égale à la moyenne (H1). Des comptages plus dispersés (des soirées très différentes à température égale) donnent des erreurs types trop petites ; il faudrait un autre modèle (une loi binomiale négative, par exemple) ou une correction, que l'article ne traite pas. Pas de terme d'exposition (des soirées de durées différentes), pas de pénalité.
- **Ce que le code ne fait pas** : il refuse un $\mathbf{X}$ de conditionnement supérieur à $10^6$ environ (le seuil de `svd_pca.condition_number`), même si la QR s'en sortirait encore ; il s'arrête dès que le conditionnement de $\mathbf{W}^{1/2}\mathbf{X}$ dépasse $10^6$, ce qui peut arriver, maximum existant, quand le rapport des moyennes ajustées extrêmes dépasse environ $10^{12}/\kappa(\mathbf{X})^2$ (une feature non centrée, par exemple) : `fit` lève alors `RuntimeError`, et centrer les features suffit ; il peut prendre pour une absence de maximum un maximum dont une moyenne ajustée d'un comptage nul descend sous $10^{-8}$ ; $e^{z_i}$ déborde au-delà de $z_i \approx 709$ ; la table des $\ln(y_i!)$ prend une mémoire proportionnelle au plus grand comptage.
- **Ce que les oracles ne vérifient pas** : scikit-learn et SciPy disent que le point final est le bon, pas que le chemin est celui de Newton (c'est le rôle du test de la direction, que la première mutation montre) ; aucun test ne mesure la vitesse de convergence, que seule l'expérience montre ; les tests ne couvrent que des $n \le 500$ et $p \le 5$.
- **Avec plus de temps** : démontrer la convergence quadratique en dimension $p$ ; chercher une direction de (4.3) avant d'itérer (un problème d'optimisation linéaire), pour annoncer l'absence de maximum dès le départ au lieu d'attendre le pas 28 ; comparer au coût réel de la QR quand $p$ grandit.
"""

REFERENCES = r"""
## Références

- **workbookMaths** (les sections citées, et ce qui y est pris) : R4 §8 (rédiger une démonstration) ; R6 §1, §3 et §5 (exponentielle, logarithme, croissances comparées) ; R7 §3, §5, §6 et §8 (taux d'accroissement, dérivées usuelles et règles, extremums) ; M02b §2, §4 et §5 (la loi de Poisson, sa moyenne et sa variance, l'indépendance) ; M02c §7 (l'erreur type) ; M05a §1 à §5, §7 et §8 (convexité en une variable, extrema, Taylor, la méthode de Newton et sa convergence quadratique, différences finies et choix du pas, overflow) ; M05b §7 et §8 (points critiques, montée de gradient) ; M09a §3, §4 et §7 (Hadamard, transposée, inverse) ; M09b §3 (équations normales) ; M12a §2, §4 et §6 (indépendance, rang, noyau) ; M12b §1 et §7 (produit scalaire pondéré, moindres carrés par QR) ; M12c §7 (matrices définies positives, quadratiques, Cholesky) ; M12d §4 (conditionnement) ; M13a §1 (maximum de vraisemblance) ; M17 §1 à §4 (jacobiennes, règle de la chaîne, convention du gradient) ; M18 §6 et §7 (gradient lu dans la différentielle) ; M19 §1, §4 et §5 (hessienne et Taylor d'ordre 2, Richardson et pas critique, conditionnement et vitesse) ; MB8 §1 (information de Fisher).
- **MML** : M. P. Deisenroth, A. A. Faisal et C. S. Ong, *Mathematics for Machine Learning*, Cambridge University Press, 2020 : §5.2 et §5.3 (dérivées partielles, règle de la chaîne, jacobiennes), §5.5 (identités pour les gradients), §5.7 et §5.8 (hessienne, Taylor à plusieurs variables), §3.8 (projections orthogonales), §4.3 (Cholesky), §7.1 (descente de gradient et conditionnement), §7.3 (optimisation convexe), §8.3.1 (maximum de vraisemblance).
- J. A. Nelder et R. W. M. Wedderburn, « Generalized Linear Models », *Journal of the Royal Statistical Society, Series A*, 135(3), 1972 : les modèles linéaires généralisés et leur ajustement par moindres carrés repondérés.
- R. W. M. Wedderburn, « On the existence and uniqueness of the maximum likelihood estimates for certain generalized linear models », *Biometrika*, 63(1), 1976 : une condition suffisante d'existence, et l'unicité, pour une large classe de ces modèles.
- S. J. Haberman, *The Analysis of Frequency Data*, University of Chicago Press, 1974 (Statistical Research Monographs, 4) : une condition nécessaire et suffisante d'existence du maximum pour les modèles log-linéaires de Poisson (attribuée ainsi par S. E. Fienberg et A. Rinaldo, « Maximum likelihood estimation in log-linear models », *The Annals of Statistics*, 40(2), 2012), dont le théorème 3 est une autre forme (démontrée ici indépendamment).
- **Les oracles** : scikit-learn 1.6.1, `sklearn.linear_model.PoissonRegressor` (solveur `"newton-cholesky"`) ; SciPy 1.16.3, `scipy.optimize.minimize` (méthode `"BFGS"`) et `scipy.stats.poisson` (documentations officielles de ces versions).
- **workbookIA** : aucun chapitre, par construction (l'exemple est hors de workbookIA).
- **Rédaction** : Claude (Anthropic), l'assistant qui génère workbookMaths ; vérifications : les tests de §7 et la grille remplie ([`grille.md`](grille.md)).
"""

PRESENTATION = r"""
## Annexe · La présentation

**Le plan de l'exposé de cinq minutes** (support : ce notebook, ses deux figures et la table des formules finales de §3).

| Partie | Durée prévue | Ce que je montre |
|---|---|---|
| 1. Le problème | 0 min 45 s | des comptages, la loi de Poisson et (2.1) ; pourquoi pas les moindres carrés sur $\mathbf{y}$ |
| 2. La dérivation | 1 min 30 s | (3.1) → (3.2) par la règle de la chaîne, (3.3), puis (3.4) réécrit en (3.6) : un pas de Newton est une régression pondérée |
| 3. Ce qui est garanti | 1 min | le lemme et la propriété 1 (un seul maximum), la propriété 2, le théorème 3 et les soirées à moustiquaire |
| 4. La vérification | 45 s | les oracles, les différences finies, la mutation que les valeurs de l'exemple à la main ne voient pas |
| 5. L'expérience et les limites | 1 min | la figure de §8.1 (quadratique contre linéaire, la pente prédite), (8.1), et deux limites |

**La durée.** Le texte de l'exposé, ci-dessous, est lu par la cellule suivante, qui estime sa durée à 130 mots par minute. C'est une **estimation**, pas une répétition chronométrée : l'auteur de cet exemple n'a pas de voix. Pour ton projet, chronomètre une vraie répétition et écris sa durée ici.

**Cinq questions d'entretien et mes réponses.**

1. *Pourquoi cet objectif, et pas les moindres carrés sur $\mathbf{y}$ ?* — Parce que les données sont des comptages : (H1) dit d'où ils viennent, et (2.1) est la vraisemblance de ce modèle (M13a §1). Les moindres carrés sur $\mathbf{y}$ supposent une variance constante et peuvent prédire un comptage négatif ; les moindres carrés sur $\ln y$ sont impossibles dès qu'un $y_i$ est nul. La réponse de travail (3.7) est justement la linéarisation de $\ln y$, qui garde un sens pour $y_i = 0$.
2. *Le problème est-il convexe ? Que garantit la réponse ?* — $-\ell$ est strictement convexe sous (H2) (propriété 1) : il y a au plus un maximum, tout point où le gradient s'annule est ce maximum, et toute méthode qui converge trouve le même (les deux oracles de §7 l'illustrent). Cela ne garantit ni que le maximum existe (théorème 3), ni que Newton pur converge depuis n'importe où : en §5, le pas plein fait baisser $\ell$ de $-13{,}15$ à $-37{,}50$ (ici, Newton pur finit par converger, en 8 pas au lieu de 6, mais sans monotonie), d'où le garde-fou (3.5).
3. *L'algorithme converge-t-il, à quelle vitesse, et qu'est-ce qui règle cette vitesse ?* — Près du maximum, l'erreur de Newton est à peu près élevée au carré à chaque pas : 6 ou 7 pas en §8.1, quel que soit $\kappa$. La montée de gradient multiplie l'erreur par $1 - 1/\kappa$ (3.12) : pour $\kappa \approx 37{,}7$ (graine 9001), 796 pas pour 10 chiffres. Je n'ai démontré la convergence quadratique qu'en dimension 1 (§3.7) ; en dimension $p$, je l'ai admise et vérifiée sur la figure.
4. *Comment sais-tu que ton implémentation est juste ? Que laisseraient passer tes tests ?* — Deux oracles pour le point final, des différences finies pour chaque dérivée, deux propriétés et une invariance (§7). La mutation des poids oubliés dans la direction de Newton montre qu'un test du seul point final, ou de l'exemple en $\mathbf{w} = \mathbf{0}$, ne suffit pas. Ils laisseraient passer une erreur qui ne touche que la vitesse sans changer ni la direction ni le point final, par exemple un garde-fou qui divise le pas par 4 au lieu de 2 ; je le verrais en comptant les itérations, comme en §8.
5. *Que se passe-t-il si un groupe n'a que des comptages nuls ?* — Le maximum n'existe pas (théorème 3, (c)) : l'effet du groupe part vers $-\infty$, d'un pas exactement à chaque itération (8.1), et `fit` s'arrête au pas 28 avec `NoMaximumError`, dont le message dit quoi chercher. Ce que je ferais : retirer la feature, ou regrouper ce groupe avec un groupe où il y a eu des piqûres, et dire à part que les six soirées à moustiquaire n'en ont eu aucune. Le théorème 3 dit que le maximum existe alors : avec une colonne de 1 et une feature 0/1 dont chaque groupe a au moins un comptage non nul, (4.3) impose $d_1 = 0$, puis $d_1 + d_2 = 0$. Je n'ai pas mesuré ce que ce regroupement change aux autres poids ; je le vérifierais en relançant `fit` sur les deux versions des données et en comparant les ajustements.
"""

SPEECH_CODE = r'''
# The text of the five-minute talk, and its estimated duration (130 words per minute, not a timed rehearsal)
SPEECH = """
Je compte des événements : des piqûres de moustique par soirée, selon l'écart de température à la normale. Une
régression linéaire prédirait parfois des comptages négatifs, et elle suppose une variance constante. Je suppose
plutôt que chaque comptage suit une loi de Poisson, dont la moyenne est l'exponentielle d'une somme pondérée des
features : la moyenne reste positive, et la variance grandit avec elle. J'estime les poids par maximum de
vraisemblance, et il n'y a pas de formule fermée : il faut une méthode itérative.

La log-vraisemblance est une somme, sur les exemples, de y fois z, moins l'exponentielle de z, moins le logarithme
de y factorielle. La règle de la chaîne donne le gradient : X transposée fois y moins mu, un vecteur de la forme
des poids. La dérivée de l'exponentielle donne la hessienne : moins X transposée, diagonale de mu, X. J'ai vérifié
chaque forme, et je relis le gradient dans la différentielle. Le pas de Newton résout le système de la hessienne ;
et ce système, ce sont les équations normales d'une régression des moindres carrés pondérée par les moyennes. Chaque
pas de Newton est donc une régression pondérée, dont les poids changent à chaque itération ; je la résous par une
décomposition QR, avec ma librairie, sans jamais former X transposée W X, dont le conditionnement serait élevé au
carré. Depuis zéro, le premier pas est la régression ordinaire de y moins un : sur mes cinq soirées, je l'ai
calculé à la main, en fractions, trois quarts pour chacun des deux poids, et le code retrouve les mêmes nombres.
Mais ce pas plein fait baisser la log-vraisemblance, de moins treize virgule un à moins trente-sept virgule cinq :
je divise alors le pas par deux, et il remonte.

Ce qui est garanti. Si les colonnes de X sont libres, la hessienne est définie négative : il y a au plus un
maximum, tout point où le gradient s'annule est ce maximum, et la direction de Newton monte toujours, donc diviser
le pas par deux finit par marcher. Avec une colonne de un, les moyennes ajustées ont exactement la somme des
comptages : le modèle est calibré en moyenne. Et le maximum n'existe que s'il n'y a pas de direction qui baisse les
moyennes des seuls comptages nuls, sans toucher aux autres. Avec six soirées à moustiquaire sans aucune piqûre,
l'effet de la moustiquaire part à moins l'infini : le modèle voudrait une moyenne nulle, qu'une exponentielle
n'atteint jamais.

La vérification. Je compare le résultat à scikit-learn, sans pénalité et avec la colonne de un dans X, et à
SciPy ; chaque dérivée à des différences finies centrées, avec un pas choisi entre la troncature et l'arrondi ; et
je teste les deux propriétés, sur trois tailles et trois graines. Une erreur introduite exprès, les poids oubliés
dans le pas de Newton, est attrapée par une cinquantaine de tests ; mais pas par les valeurs de l'exemple à la main,
où tous les poids valent un. Un exemple calculé en un seul point ne suffit donc pas.

L'expérience. J'ai écrit ma prédiction avant de lancer le calcul. Newton double le nombre de chiffres justes à
chaque pas : six ou sept pas suffisent. Une montée de gradient, avec un learning rate égal à un sur la plus grande
valeur propre, multiplie l'erreur par un moins un sur kappa à chaque pas, et la pente mesurée est celle que je
prédisais, à cinq décimales : huit cents à onze cents pas. Sans maximum, les itérés s'en vont d'exactement un pas
par itération, comme prévu, et mon code s'arrête au vingt-huitième pas avec un message qui dit quoi chercher.

Les limites. La variance est supposée égale à la moyenne ; des comptages plus dispersés demanderaient un autre
modèle. Et deux résultats sont admis, la convergence quadratique en dimension quelconque et les erreurs types
asymptotiques : l'article le dit à l'endroit où il s'en sert.
"""
words = len(SPEECH.split())
print(f"{words} mots, soit environ {words / 130:.1f} minutes à 130 mots par minute (une estimation, pas une "
      "répétition chronométrée)")
'''

DURATION = r'''
# The duration of "Run all" (PS.9: less than 5 minutes on CPU, no cell over one minute)
elapsed = time.perf_counter() - T0
print(f"⏱️ « Run all » : {elapsed:.0f} s depuis la cellule du dossier de l'exemple "
      + ("✅" if elapsed < 300 else "⚠️ (plus de 5 minutes)"))
'''


def cells() -> list:
    return [
        md(TITLE),
        setup_cell("solution"),
        md(PROJECT_MD), code(PROJECT_CODE),
        md(INTRO),
        md(PROBLEM),
        md(DERIVATION_1),
        md(PROPERTIES), code(LIMIT_CODE), code(LIMIT_CHECK),
        md(HAND), code(HAND_CODE), code(HAND_CHECK), code(HAND_TABLE),
        md(IMPLEMENTATION), code(CONTROL_CODE), code(DEMO_CODE), code(MYMATH_TESTS),
        md(VERIFICATION), code(TESTS_CODE), md(MUTATION_MD), code(MUTATION_CODE), md(MUTATION_COMMENT),
        md(EXPERIMENT), code(EXPERIMENT_CODE), code(EXPERIMENT_FIGURE), md(EXPERIMENT_CONCLUSION),
        code(NO_MAXIMUM_CODE), code(NO_MAXIMUM_FIGURE), md(NO_MAXIMUM_CONCLUSION),
        md(CONCLUSION),
        md(REFERENCES),
        md(PRESENTATION), code(SPEECH_CODE),
        code(DURATION),
    ]
