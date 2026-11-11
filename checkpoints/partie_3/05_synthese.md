# CP3 · Synthèse de la partie III (M12a à M14)

> La synthèse se fait **avant** l'examen blanc, un autre jour si possible. Commence par l'exercice CP3.11 : construire **ta** carte mentale et **ta** fiche d'une page. Ensuite seulement, compare-les avec les versions de référence des sections 1 à 3, puis lis les sections 4 et 5 : ce que tu as oublié, c'est ce qu'il faut revoir.

**Les sept chapitres en une phrase chacun**
1. **M12a · Espaces vectoriels et applications linéaires** : sous-espaces, bases, dimension et coordonnées ; une application linéaire est une matrice, avec son rang, son noyau et son image ; changer de base, inverser une application affine.
2. **M12b · Orthogonalité et projections** : produits scalaires, bases orthonormées, complément orthogonal, projection (le point le plus proche), les moindres carrés vus comme une projection, Gram-Schmidt et QR.
3. **M12c · Valeurs propres et matrices symétriques** : déterminant et trace, valeurs et vecteurs propres, diagonalisation, méthode de la puissance, théorème spectral, matrices définies positives et Cholesky, covariance et blanchiment.
4. **M12d · SVD et analyse en composantes principales** : toute matrice tourne, étire, puis tourne ; rang faible, pseudo-inverse, conditionnement ; l'ACP centre, projette et reconstruit ; t-SNE et UMAP en aperçu.
5. **M13a · Vraisemblance et régression logistique** : le maximum de vraisemblance, la log-loss, la sigmoïde et la softplus, la régression logistique, Naïve Bayes, les impuretés des arbres.
6. **M13b · Optimisation sous contraintes et SVM** : Lagrange, KKT, dualité, problèmes convexes, puis la SVM : marges dure et souple, hinge loss, dual, vecteurs de support, noyaux.
7. **M14 · Les maths des ensembles** : la queue binomiale et ses bornes, la variance d'une moyenne pondérée, la limite $(1 + x/n)^n \to e^x$, les poids exponentiels de Hedge, le gradient d'une loss par rapport aux prédictions.

## CP3.11 — Ta carte mentale et ta fiche d'une page 🗣️ ★ ⏱️ 60 min

**Objectif :** organiser toute la partie III dans ta tête, avant l'examen, et repérer ce qui manque.

1. **De mémoire, sans rien ouvrir (20 min).** Sur une grande feuille, écris les sept chapitres, puis, autour de chacun, les objets mathématiques, les notions et les formules qui te viennent : range-les par objets (sous-espaces, projections, valeurs propres…), pas par étapes d'un projet. Relie les notions qui se servent l'une de l'autre (« les valeurs singulières viennent de $\mathbf{A}^\top\mathbf{A}$, une matrice symétrique : le théorème spectral s'applique »), et écris sur chaque flèche **pourquoi**.
2. **Avec les fiches (25 min).** Ouvre les fiches des chapitres (sections « L'essentiel en 10 lignes ») et l'annexe `annexes/formulaire.md`. Complète ta carte d'une autre couleur : tout ce que tu ajoutes maintenant est à revoir.
3. **Ta fiche d'une page (15 min).** Sur une seule page, écris les 20 à 25 formules ou règles que tu veux avoir en tête le jour de l'examen, et les cinq pièges qui te concernent le plus (dans tes copies et dans `annexes/erreurs_frequentes.md`).
4. **Compare** avec les sections 1 à 3 ci-dessous, puis garde ta carte et ta fiche dans `mon_travail/checkpoints/partie_3/` (une photo suffit).

**Grille de relecture.** Une bonne synthèse : (1) contient les sept chapitres ; (2) a au moins sept flèches justifiées entre chapitres ; (3) donne chaque formule avec ses conditions ($\mathbf{A}$ symétrique pour le théorème spectral et Rayleigh, des colonnes libres pour Gram-Schmidt, $a > p$ pour Chernoff, des variables indépendantes dans $[0 ; 1]$ pour Hoeffding, des losses dans $[0 ; 1]$ pour le regret de Hedge, un problème convexe pour que KKT suffise) ; (4) a des pièges tirés de tes propres erreurs ; (5) tient sur une page pour la fiche.

## 1. Carte mentale

```text
ALGÈBRE LINÉAIRE
M12a  sous-espaces → bases, dimension, coordonnées
      └─ applications linéaires x ↦ Ax (colonne j = f(eⱼ), composer = multiplier)
         ├─ rang, noyau, image : dim ker A + rg A = n
         ├─ changement de base S⁻¹AS
         └─ applications affines Ax + b et leur réciproque
M12b  produit scalaire → orthogonalité, bases orthonormées, QᵀQ = I
      ├─ complément orthogonal (Im A)⊥ = ker Aᵀ
      ├─ projection = point le plus proche → moindres carrés
      └─ Gram-Schmidt → QR → Rw = Qᵀy
M12c  déterminant, trace → valeurs propres : det(A − λI) = 0 → diagonalisation
      └─ A symétrique : théorème spectral QΛQᵀ, quotient de Rayleigh
         └─ définie positive ⇔ λᵢ > 0 ⇔ Cholesky LLᵀ → covariance, blanchiment
M12d  SVD A = USVᵀ (par AᵀA, symétrique)
      ├─ rang faible (Eckart-Young), pseudo-inverse, conditionnement
      └─ ACP : centrer, axes propres de C, scores, variance expliquée, reconstruction

PROBABILITÉS ET OPTIMISATION
M13a  vraisemblance → maximum de vraisemblance
      ├─ log-loss = −ℓ/n → sigmoïde, softplus → régression logistique (convexe)
      └─ impuretés : entropie, Gini → gain d'information
M13b  Lagrange → KKT → dualité ; problème convexe : KKT suffisantes
      └─ SVM : marge dure → marge souple, hinge → dual, vecteurs de support → noyaux
M14   queue binomiale → Markov, Hoeffding, Chernoff (KL)
      ├─ variance d'une moyenne pondérée wᵀΣw
      └─ (1 + x/n)ⁿ → eˣ → poids exponentiels, Hedge et son regret
```

**Les flèches entre chapitres**, chacune avec sa raison :
- **M12a → M12b** : $(\operatorname{Im}\mathbf{A})^\perp = \ker\mathbf{A}^\top$ : un complément orthogonal est un noyau.
- **M12a → M12c** : $\lambda$ est valeur propre quand $\mathbf{A} - \lambda\mathbf{I}$ a un noyau non nul ; diagonaliser, c'est changer de base.
- **M12b → M12c** : une matrice symétrique a une base **orthonormée** de vecteurs propres ; une matrice symétrique définie positive définit un produit scalaire.
- **M12c → M12d** : $\mathbf{A}^\top\mathbf{A}$ est symétrique semi-définie positive, de valeurs propres $s_i^2$ ; la variance le long de $\mathbf{u}$ est un quotient de Rayleigh de $\mathbf{C}$.
- **M12b → M12d** : les scores sont des projections sur des axes orthonormés, la reconstruction en est une aussi.
- **M12d → M13b** : l'ACP relue par Lagrange donne $\mathbf{C}\mathbf{u} = \lambda\mathbf{u}$ (MML §10.2).
- **M12c → M13b** : une hessienne semi-définie positive partout donne une fonction convexe ; une matrice de Gram de noyau est semi-définie positive.
- **M13a → M13b** : la log-loss et la hinge sont deux majorants convexes de l'erreur ; Lagrange retrouve $\hat{p}_k = n_k/N$.
- **M12c → M14** : $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ est la règle $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top$ avec une seule ligne.
- **M13b → M14** : les meilleurs poids d'une moyenne, sous $\sum_i w_i = 1$, sortent d'un lagrangien.

Redessine-la de mémoire, puis compare : chaque flèche doit pouvoir se justifier par un exemple (« le blanchiment par l'ACP, $\boldsymbol{\Lambda}^{-1/2}\mathbf{Q}^\top$, divise chaque score par son écart-type : M12c rejoint M12d »).

## 2. Fiche d'une page : les formules clés

| Chapitre | Formules et règles |
|---|---|
| M12a | sous-espace : $\mathbf{0} \in U$, $\lambda\mathbf{x} + \mu\mathbf{y} \in U$ ; « $f$ puis $g$ » $= \mathbf{B}\mathbf{A}$ ; $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \min(\operatorname{rg}\mathbf{A}, \operatorname{rg}\mathbf{B})$ ; **théorème du rang** $\dim\ker\mathbf{A} + \operatorname{rg}\mathbf{A} = n$ (colonnes) ; solutions de $\mathbf{A}\mathbf{x} = \mathbf{b}$ : $\mathbf{x}_p + \ker\mathbf{A}$ ; nouvelle base : $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ ; $\varphi^{-1}(\mathbf{y}) = \mathbf{A}^{-1}(\mathbf{y} - \mathbf{b})$ |
| M12b | base orthonormée : $c_i = \langle \mathbf{v}, \mathbf{q}_i \rangle$ ; **projection** : $\mathbf{v} - \mathbf{p} \perp U$, $\mathbf{p} = \mathbf{Q}\mathbf{Q}^\top\mathbf{v}$, ou $\mathbf{A}^\top\mathbf{A}\,\mathbf{c} = \mathbf{A}^\top\mathbf{v}$ et $\mathbf{p} = \mathbf{A}\mathbf{c}$ ; **Gram-Schmidt** $\mathbf{v}_k = \mathbf{a}_k - \sum_{j<k} \langle \mathbf{a}_k, \mathbf{q}_j \rangle\,\mathbf{q}_j$, $\mathbf{q}_k = \mathbf{v}_k/\lVert \mathbf{v}_k \rVert$ ; **QR** : $r_{jk} = \langle \mathbf{q}_j, \mathbf{a}_k \rangle$, $r_{kk} = \lVert \mathbf{v}_k \rVert$ ; moindres carrés : $\mathbf{R}\mathbf{w}^* = \mathbf{Q}^\top\mathbf{y}$, en remontant |
| M12c | $\det(c\mathbf{A}) = c^n\det\mathbf{A}$ ; $2 \times 2$ : $\lambda^2 - (\operatorname{tr}\mathbf{A})\lambda + \det\mathbf{A} = 0$ ; $\sum\lambda_i = \operatorname{tr}\mathbf{A}$, $\prod\lambda_i = \det\mathbf{A}$ ; **spectral** ($\mathbf{A}$ symétrique) $\mathbf{A} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$ ; **Rayleigh** $\lambda_{\min} \le \frac{\mathbf{x}^\top\mathbf{A}\mathbf{x}}{\mathbf{x}^\top\mathbf{x}} \le \lambda_{\max}$ ; définie positive $\iff$ tous les $\lambda_i > 0$ $\iff$ mineurs principaux $> 0$ $\iff$ **Cholesky** $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$, $l_{jj} = \sqrt{a_{jj} - \sum_{k<j} l_{jk}^2}$, $l_{ij} = \big(a_{ij} - \sum_{k<j} l_{ik}l_{jk}\big)/l_{jj}$ ; $\operatorname{Cov}(\mathbf{A}\mathbf{x} + \mathbf{b}) = \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top$ |
| M12d | **SVD** $\mathbf{A} = \sum_i s_i\mathbf{u}_i\mathbf{v}_i^\top$, $s_i = \sqrt{\lambda_i(\mathbf{A}^\top\mathbf{A})}$, $\mathbf{u}_i = \mathbf{A}\mathbf{v}_i/s_i$ ; **Eckart-Young** $\lVert \mathbf{A} - \mathbf{A}_k \rVert_F^2 = \sum_{i > k} s_i^2$ ; **conditionnement** $\kappa = s_{\max}/s_{\min}$, $\kappa(\mathbf{A}^\top\mathbf{A}) = \kappa(\mathbf{A})^2$ ; **ACP** $\mathbf{C} = \frac{1}{n - 1}\mathbf{X}_c^\top\mathbf{X}_c$, variance le long de $\mathbf{u}$ unitaire : $\mathbf{u}^\top\mathbf{C}\mathbf{u}$ ; scores $\mathbf{X}_c\mathbf{W}_k$ ; $\lambda_j = s_j^2/(n - 1)$ ; part expliquée $\lambda_j/\sum_l \lambda_l$ ; erreur moyenne $\frac{n - 1}{n}\sum_{j > k}\lambda_j$ |
| M13a | **maximum de vraisemblance** de $\ell = \sum_i \ln p(x_i \mid \boldsymbol{\theta})$ : $\hat{p}_k = \frac{n_k}{N}$, $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}\sum_i (x_i - \hat{\mu})^2$ ; **log-loss** $-\frac{1}{n}\sum_i \big[y_i\ln\hat{p}_i + (1 - y_i)\ln(1 - \hat{p}_i)\big]$, en nats ; **softplus** $s(z) = \ln(1 + e^z) = \max(z, 0) + \ln(1 + e^{-\lvert z \rvert})$, terme d'un exemple $s(z) - yz$ ; $P(Y = 1 \mid \mathbf{x}) = \sigma(\mathbf{w} \cdot \mathbf{x} + b)$ ; **entropie** $-\sum_k p_k\log_2 p_k \le \log_2 K$ ; **Gini** $1 - \sum_k p_k^2 \le 1 - \frac{1}{K}$ ; **gain** $H(Y) - H(Y \mid X)$ |
| M13b | **Lagrange** ($\mathcal{L} = f + \lambda g$) : $\nabla f + \lambda\nabla g = \mathbf{0}$, $g = 0$ ; **KKT** ($g_i \le 0$) : stationnarité, faisabilité, $\mu_i \ge 0$, $\mu_i\,g_i(\mathbf{x}^*) = 0$ ; **dual** $D = \inf_{\mathbf{x}}\mathcal{L} \le f(\mathbf{x})$ pour $\mathbf{x}$ admissible ; **SVM** $\min \frac{1}{2}\lVert \mathbf{w} \rVert^2$ sous $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ ; **hinge** $J = \frac{1}{2}\lVert \mathbf{w} \rVert^2 + C\sum_i \max\big(0,\ 1 - y_i(\mathbf{w} \cdot \mathbf{x}_i + b)\big)$ ; dual de la SVM : $\mathbf{w} = \sum_i \alpha_iy_i\mathbf{x}_i$, $\sum_i \alpha_iy_i = 0$, $0 \le \alpha_i \le C$ ; RBF $e^{-\gamma\lVert \mathbf{x} - \mathbf{z} \rVert^2}$ |
| M14 | $P(X \ge k) = \sum_{j \ge k}\binom{n}{j}p^j(1 - p)^{n - j}$ ; si $a > p$, $P(X \ge na)$ est au plus $e^{-2n(a - p)^2}$ (**Hoeffding**) et $e^{-n\,\mathrm{KL}(a \Vert p)}$ (**Chernoff**), $\mathrm{KL}(a \Vert p) = a\ln\frac{a}{p} + (1 - a)\ln\frac{1 - a}{1 - p}$ ; $\mathbb{V}\big(\sum_i w_iX_i\big) = \mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ ; $\left(1 + \frac{x}{n}\right)^n \to e^x$, erreur relative $\approx -\frac{x^2}{2n}$ ; **Hedge** $w_t[k] \propto e^{-\eta L_t[k]}$, $L_t[k] = \sum_{s < t}\ell_s[k]$ ; regret $R_T \le \frac{\ln K}{\eta} + \frac{\eta T}{8}$ |

## 3. Les pièges de la partie

Dix erreurs fréquentes de la partie III, avec leur correction (le détail, chapitre par chapitre, est dans `annexes/erreurs_frequentes.md`) :

| Piège | Faux | Juste |
|---|---|---|
| base de l'image (M12a) | les colonnes à pivot de la forme réduite | les colonnes **de $\mathbf{A}$** aux indices des pivots : réduire change l'espace des colonnes |
| système triangulaire (M12b) | résoudre $\mathbf{R}\mathbf{w} = \mathbf{Q}^\top\mathbf{y}$ à partir de la première ligne | $\mathbf{R}$ est triangulaire supérieure : partir de la dernière ligne, qui n'a qu'une inconnue |
| déterminant d'un multiple (M12c) | $\mathbf{A}$ de taille $2 \times 2$, $\det\mathbf{A} = 2$, donc $\det(3\mathbf{A}) = 6$ | $\det(c\mathbf{A}) = c^n\det\mathbf{A}$ : $3^2 \times 2 = 18$ |
| standardiser ou blanchir (M12c) | diviser chaque feature par son écart-type donne la covariance $\mathbf{I}$ | les variances valent 1, les corrélations restent ; blanchir : $\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top = \mathbf{I}$ |
| valeurs singulières (M12d) | les valeurs propres de $\mathbf{A}^\top\mathbf{A}$, ou celles de $\mathbf{A}$ | leurs **racines** : $s_i = \sqrt{\lambda_i(\mathbf{A}^\top\mathbf{A})}$ |
| ACP sans centrer (M12d) | diagonaliser $\frac{1}{n - 1}\mathbf{X}^\top\mathbf{X}$ sur les données brutes | retirer la moyenne d'abord, sinon le premier axe pointe vers la moyenne |
| variance (M13a) | maximum de vraisemblance : $\hat{\sigma}^2 = \frac{1}{n - 1}\sum_i (x_i - \hat{\mu})^2$ | diviser par $n$ ; $n - 1$ donne l'estimation sans biais |
| marge (M13b) | « la marge vaut $\lVert \mathbf{w} \rVert$ », ou la largeur de la bande | $\rho = 1/\lVert \mathbf{w} \rVert$ en forme canonique ; la bande fait $2\rho$ |
| « au moins $k$ » (M14) | $P(X \ge k)$ = `binom.sf(k, n, p)` | `binom.sf(k - 1, n, p)`, car `sf(m)` rend $P(X > m)$ |
| sens de la KL (M14) | $\mathrm{KL}(p \Vert a)$ dans la borne de Chernoff, ou la borne avec $a < p$ | $\mathrm{KL}(a \Vert p)$, la proportion de l'événement d'abord ; pour $a \le p$, seule la borne 1 |

## 4. Ce qui sert dans workbookIA

Le checkpoint III de workbookIA se fait juste après cet examen blanc. Ce qui t'y attend, et dans les chapitres 12 à 15, sans en dévoiler les exercices :
- **ch. 12 (préparation des données)** : les mises à l'échelle sont affines, et `inverse_transform` est leur réciproque ; le rang et le noyau repèrent les colonnes redondantes (M12a) ; centrer, c'est projeter (M12b) ; la covariance, ses deux conventions et le blanchiment (M12c) ; l'ACP par la SVD des données centrées, la variance expliquée, la reconstruction, t-SNE et UMAP (M12d). Les axes de plus grande variance, que le chapitre admet, ont deux démonstrations : Rayleigh (M12c) et Lagrange (M13b).
- **ch. 13 (classifieurs)** : la régression logistique et sa log-loss, Naïve Bayes, les arbres et leurs impuretés (M13a) ; les SVM linéaires et à noyau RBF, $C$ et $\gamma$, les vecteurs de support et la bande (M13b).
- **ch. 14 (ensembles)** : la queue binomiale compte la probabilité qu'une majorité de votants se trompe ; $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ dit ce que coûte la corrélation entre arbres ; la limite $(1 + x/n)^n$ revient dans les tirages avec remise ; les poids exponentiels et le gradient par rapport aux prédictions préparent AdaBoost et le gradient boosting (M14).
- **ch. 15 (scikit-learn)** : `inverse_transform` encore (M12a), et le nombre de composantes d'une ACP, réglé en validation avec le modèle qui suit (M12d).

Ensuite, la partie IV de ce dépôt commence par M16 (couches affines et variance à l'initialisation), avant workbookIA 16.

## 5. Vocabulaire à maîtriser à l'oral

Dis chaque mot à voix haute, en français puis en anglais, puis la phrase de la dernière colonne, et invente ton propre exemple.

| Français | Anglais | À dire à voix haute |
|---|---|---|
| sous-espace, base, dimension | subspace, basis, dimension | « Le plan $x + y + z = 0$ a pour base $(1, -1, 0)$ et $(0, 1, -1)$ : dimension 2. » |
| noyau, image, théorème du rang | kernel, image, rank-nullity theorem | « Le noyau vit au départ ; sa dimension plus le rang donne le nombre de colonnes. » |
| projection orthogonale, complément orthogonal | orthogonal projection, orthogonal complement | « Le projeté est le point le plus proche ; le résidu est dans $U^\perp$. » |
| Gram-Schmidt, décomposition QR | Gram-Schmidt process, QR decomposition | « Retirer les projections sur les vecteurs précédents, puis normer : c'est $\mathbf{A} = \mathbf{Q}\mathbf{R}$. » |
| valeur propre, vecteur propre, théorème spectral | eigenvalue, eigenvector, spectral theorem | « Une matrice symétrique a une base orthonormée de directions qu'elle ne fait qu'étirer. » |
| définie positive, Cholesky | positive definite, Cholesky decomposition | « Symétrique et définie positive, c'est exactement s'écrire $\mathbf{L}\mathbf{L}^\top$. » |
| valeur singulière, rang faible, conditionnement | singular value, low-rank approximation, condition number | « Garder les $k$ plus grandes valeurs singulières donne la meilleure approximation de rang $k$. » |
| ACP, variance expliquée | principal component analysis, explained variance ratio | « La part d'un axe est sa valeur propre sur la somme de toutes. » |
| vraisemblance, log-loss | likelihood, log-loss | « Minimiser la log-loss, c'est maximiser la vraisemblance des labels. » |
| entropie, indice de Gini, gain d'information | entropy, Gini impurity, information gain | « Le gain est la baisse d'entropie, sous-groupes pondérés par leurs tailles. » |
| multiplicateur de Lagrange, KKT, complémentarité | Lagrange multiplier, KKT conditions, complementary slackness | « Une inégalité non atteinte a un multiplicateur nul : elle ne pousse pas. » |
| hinge loss, vecteur de support, noyau | hinge loss, support vector, kernel | « $\mathbf{w}$ ne dépend que des exemples où $\alpha_i > 0$, les vecteurs de support. » |
| borne de Chernoff, poids exponentiels, regret | Chernoff bound, exponential weights, regret | « Hedge donne à chaque expert un poids proportionnel à $e^{-\eta L}$ : une grande loss, un petit poids. » |

## Mode d'emploi (≈ 75 minutes)

1. CP3.11 d'abord (60 min) : ta carte et ta fiche, de mémoire puis avec les fiches.
2. Compare avec les sections 1 à 3 (10 min) : note ce qui te manquait.
3. Lis les sections 4 et 5 (5 min), en disant le vocabulaire à voix haute.
4. L'examen blanc, un autre jour : `01_examen_sujet.md`, en conditions réelles.

Ces 15 minutes de comparaison et de lecture sont la « lecture » du bilan ; avec CP3.11, la synthèse prend environ 75 minutes.
