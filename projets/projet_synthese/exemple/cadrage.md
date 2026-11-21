# Cadrage · La régression de Poisson ajustée par la méthode de Newton

> **PS.1** de l'exemple : une page, 600 mots au plus.

**Auteur** : l'exemple de workbookMaths · **Date** : novembre 2026

## L'algorithme

- **Lequel** : la régression de Poisson, ajustée par la méthode de Newton (moindres carrés repondérés). Hors liste et hors workbookIA, exprès. Il convient : sa dérivation (gradient, hessienne, réécriture du pas, existence du maximum) tient sur plusieurs pages, et scikit-learn en donne un oracle indépendant.
- **Ce qu'il calcule** : les poids qui maximisent la vraisemblance de comptages, chacun tiré d'une loi de Poisson de moyenne $e^{\mathbf{x}_i^\top\mathbf{w}}$.
- **Ses entrées** : $\mathbf{X}$, de forme $(n, p)$, colonne de 1 comprise ; $\mathbf{y}$, de forme $(n,)$, des entiers $\ge 0$.
- **Ses sorties** : $\hat{\mathbf{w}}$, de forme $(p,)$ ; les itérés, de forme $(p,)$ chacun ; les erreurs types, de forme $(p,)$.

## Les maths dont la dérivation a besoin

| Notion | Où elle s'enseigne dans ce dépôt | Dans MML |
|---|---|---|
| loi de Poisson, indépendance | M02b §2 et §5 | — |
| maximum de vraisemblance | M13a §1 | §8.3.1 |
| dérivées usuelles, règle de la chaîne | R7 §5 à §7 ; M17 §1 à §4 | §5.2, §5.3 |
| gradient de la forme de la variable, différentielle | M18 §6 et §7 | §5.5 |
| hessienne, Taylor d'ordre 2 | M19 §1 | §5.7, §5.8 |
| méthode de Newton, convergence quadratique | M05a §4 | — |
| matrices définies positives, Cholesky | M12c §7 | §4.3 |
| équations normales, moindres carrés par QR | M09b §3 ; M12b §7 | §3.8 |
| conditionnement | M12d §4 | — |
| pas critique et vitesse d'une itération | M19 §4 et §5 | §7.1 |
| information de Fisher | MB8 §1 | — |

## L'oracle

- **La bibliothèque et la fonction** : scikit-learn, `sklearn.linear_model.PoissonRegressor` ; en second, SciPy, `scipy.optimize.minimize` (BFGS) sur $-\ell$ écrite avec `scipy.stats.poisson.logpmf`.
- **Les réglages qui la rendent comparable** : `alpha=0` (la pénalité par défaut, `alpha=1`, déplacerait le maximum) ; `fit_intercept=False`, avec la colonne de 1 dans $\mathbf{X}$ (les mêmes paramètres) ; `solver="newton-cholesky"` et `tol=1e-9`. Il minimise la moitié de la déviance moyenne : même maximum que $\ell$, gradient divisé par $n$.
- **Ce qu'elle ne vérifie pas** : le chemin (mes itérés sont-ils ceux de Newton ?), la vitesse, les dérivées.

## Le plan de l'article

| Section | Ce que j'y mets |
|---|---|
| §2 Le problème | notations ; (H1) le modèle, (H2) le rang, (H3) la colonne de 1, (H4) l'existence ; gradient de la forme de $\mathbf{w}$ |
| §3 La dérivation | de $\ell$ au gradient, à la hessienne, au pas de Newton, puis aux moindres carrés pondérés que le code résout |
| §4 Les propriétés | propriété 1 : concavité stricte sous (H2), donc unicité ; propriété 2 : $\sum_i\hat{\mu}_i = \sum_iy_i$ ; cas limite pressenti : (H4) tombe, un groupe aux comptages tous nuls |
| §5 L'exemple à la main | cinq soirées, une feature : le premier pas depuis $\mathbf{0}$, en fractions |
| §6 et §7 | `orthogonal.least_squares_qr`, `eigen.cholesky`, `approx.newton`, `svd_pca.condition_number`, `iterative.critical_step_size` ; mutation prévue : les poids oubliés |
| §8 L'expérience | Newton contre une montée de gradient (pente prédite $\log_{10}(1 - 1/\kappa)$, trois graines) ; les itérés sans maximum |

## Mes jalons

Semaine 1 : cadrage, §2, début de §3. Semaine 2 : §3 à §5. Semaine 3 : module, tests, mutation. Semaine 4 : expérience, rédaction, présentation.
