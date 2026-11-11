# Cheatsheet NumPy pour les maths

Les bases de NumPy (tableaux, formes, broadcasting) sont dans le chapitre 0A de workbookIA et son `annexes/cheatsheets/numpy.md`. Ici, ce qui sert aux maths : vecteurs, matrices, algèbre linéaire, calcul numérique.

```python
import numpy as np
rng = np.random.default_rng(42)          # toujours un générateur avec une graine
```

## Vecteurs et matrices

| Je veux… | Code |
|---|---|
| un vecteur, une matrice | `v = np.array([1.0, 2.0])`, `A = np.array([[1, 2], [3, 4]])` |
| la forme | `A.shape` → `(2, 2)` |
| la transposée | `A.T` |
| le produit matriciel | `A @ B` (jamais `A * B`, qui multiplie terme à terme) |
| le produit scalaire | `u @ v` ou `np.dot(u, v)` |
| la norme L2, L1, L∞ | `np.linalg.norm(v)`, `np.linalg.norm(v, 1)`, `np.linalg.norm(v, np.inf)` |
| l'identité, des zéros | `np.eye(3)`, `np.zeros((2, 3))` |
| une matrice diagonale | `np.diag([1, 2, 3])` |
| un produit à plusieurs indices | `np.einsum("ij,jk->ik", A, B)` (le produit matriciel écrit avec ses indices) |

## Algèbre linéaire (`np.linalg`)

| Je veux… | Code | Remarque |
|---|---|---|
| résoudre $\mathbf{A}\mathbf{x} = \mathbf{b}$ | `np.linalg.solve(A, b)` | toujours préférable à `inv(A) @ b` |
| l'inverse | `np.linalg.inv(A)` | |
| le déterminant | `np.linalg.det(A)` | valeur approchée : `1e-16` signifie « zéro » ; un déterminant petit ne veut pas dire « presque singulière » (M12c) |
| le rang | `np.linalg.matrix_rank(A)` | le nombre de valeurs singulières au-dessus d'un seuil d'environ $10^{-16}\,s_{\max}\max(m, n)$ : un rang **numérique** (M12d) |
| valeurs et vecteurs propres | `np.linalg.eig(A)` ; pour une matrice symétrique : `np.linalg.eigh(A)` | les vecteurs propres sont les **colonnes** du résultat ; `eigh` rend des valeurs réelles par ordre **croissant** et des vecteurs orthonormés, `eig` peut rendre des complexes (une rotation) |
| la SVD | `U, s, Vt = np.linalg.svd(A, full_matrices=False)` ; les valeurs seules : `np.linalg.svd(A, compute_uv=False)` | `A ≈ (U * s) @ Vt` ; `s` décroissant ; les $\mathbf{v}_i$ sont les **lignes** de `Vt` ; signes arbitraires (changer une ligne de `Vt` et la colonne de `U` ensemble) ; $\min(m, n)$ valeurs, nulles comprises |
| l'approximation de rang $k$ | `(U[:, :k] * s[:k]) @ Vt[:k]` | la meilleure de rang $k$ (Eckart-Young) |
| la pseudo-inverse | `np.linalg.pinv(A)` | $\mathbf{A}^+$, de forme $(n, m)$ ; un seuil relatif (`rcond`) traite les petites valeurs singulières comme nulles |
| le conditionnement | `np.linalg.cond(A)` | $s_{\max}/s_{\min}$ ; très grand (ou `inf`) pour une matrice presque singulière |
| les moindres carrés | `np.linalg.lstsq(X, y, rcond=None)[0]` | par la SVD : la solution de plus petite norme si les colonnes sont liées |
| une ACP | `from sklearn.decomposition import PCA` ; `pca = PCA(n_components=k).fit(X)` | centre, puis SVD (ou, si $n \gg p$, diagonalise la covariance ; `svd_solver="full"` impose la SVD) ; axes en **lignes** de `pca.components_`, variances `explained_variance_` (en $n - 1$), parts `explained_variance_ratio_`, scores `pca.transform(X)`, reconstruction `pca.inverse_transform(Z)` |
| Cholesky | `np.linalg.cholesky(A)` | $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$, `LinAlgError` si $\mathbf{A}$ n'est pas définie positive ; ne vérifie **pas** la symétrie (elle ne lit que le triangle inférieur) |
| la racine carrée d'une matrice | `scipy.linalg.sqrtm(A)` ; symétrique positive : `Q * np.sqrt(values) @ Q.T` avec `values, Q = np.linalg.eigh(A)` | jamais `np.sqrt(A)`, qui prend la racine des éléments |
| comparer deux résultats approchés | `np.allclose(a, b)` | jamais `==` entre flottants |

## Calcul numérique

| Je veux… | Code |
|---|---|
| des points régulièrement espacés | `np.linspace(0, 1, 101)` (101 points, bornes comprises) |
| une somme, un produit | `np.sum(x)`, `np.prod(x)` ; sommes cumulées : `np.cumsum(x)` |
| exp, log, racine | `np.exp`, `np.log` (népérien), `np.log2`, `np.sqrt` |
| log-sum-exp stable | `scipy.special.logsumexp(x)` |
| softplus stable, $\ln(1 + e^z)$ | `np.logaddexp(0, z)`, ou `np.maximum(z, 0) + np.log1p(np.exp(-np.abs(z)))` |
| sigmoïde, $\ln\sigma(z)$ sans débordement | `scipy.special.expit(z)`, `scipy.special.log_expit(z)` |
| $x\ln y$ avec $0 \ln 0 = 0$ | `scipy.special.xlogy(x, y)` |
| la log-loss | `sklearn.metrics.log_loss(y, p)` (en nats, probabilités écrêtées près de 0 et de 1) |
| un maximum de vraisemblance | `scipy.stats.norm.fit(x)` rend $(\hat{\mu}, \hat{\sigma})$ (l'écart-type, en $\frac{1}{n}$) ; `np.var(x)` divise par $n$ |
| une intégrale numérique | `scipy.integrate.quad(f, 0, 1)` ; sur des points : `np.trapezoid(y, x)` |
| un zéro de fonction | `scipy.optimize.brentq(f, a, b)` |
| un minimum | `scipy.optimize.minimize(f, x0)` |
| un minimum sous contraintes | `scipy.optimize.minimize(f, x0, constraints=[{"type": "ineq", "fun": h}])` (SLSQP) : `"ineq"` veut dire $h(\mathbf{x}) \ge 0$, l'inverse de la convention $g \le 0$ de M13b ; `"eq"` pour $h(\mathbf{x}) = 0$ |
| le système de Lagrange par blocs | `np.block([[Q, A.T], [A, np.zeros((m, m))]])`, puis `np.linalg.solve` avec le second membre `np.concatenate([-c, b])` |
| une SVM | `sklearn.svm.SVC(kernel="linear", C=1.0)` ; `.coef_`, `.intercept_`, `.support_` (indices des vecteurs de support), `.dual_coef_` (les $\alpha_iy_i$) ; `kernel="rbf", gamma=…` |
| des matrices de noyau | `sklearn.metrics.pairwise.rbf_kernel(X, Z, gamma=g)` ; `polynomial_kernel(X, Z, degree=d, gamma=1, coef0=c)` calcule $(\gamma\,\mathbf{x} \cdot \mathbf{z} + c)^d$ |
| des distances au carré deux à deux | `scipy.spatial.distance.cdist(X, Z, "sqeuclidean")` |
| la hinge loss moyenne | `sklearn.metrics.hinge_loss(y, scores)` (labels $\pm 1$) |
| tirer au hasard | `rng.normal(mu, sigma, size=n)`, `rng.uniform(a, b, size=n)`, `rng.integers(1, 7, size=n)` (dé) |

> ⚠️ **Piège classique — les flottants** — `0.1 + 0.2 == 0.3` vaut `False` : un ordinateur ne représente pas exactement 0,1. Compare avec `np.isclose` ; pour un calcul exact, `fractions.Fraction` ou SymPy (R1, M05a).
