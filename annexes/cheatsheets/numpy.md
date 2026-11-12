# Cheatsheet NumPy pour les maths

Les bases de NumPy (tableaux, formes, broadcasting) sont dans le chapitre 0A de workbookIA et son `annexes/cheatsheets/numpy.md`. Ici, ce qui sert aux maths : vecteurs, matrices, algèbre linéaire, convolutions, calcul numérique.

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
| un produit à plusieurs indices | `np.einsum("ij,jk->ik", A, B)` (le produit matriciel écrit avec ses indices) ; une lettre absente du résultat est sommée ; `"sij,sjk->sik"` multiplie des matrices empilées ; `optimize=True` et `np.linalg.multi_dot` choisissent l'ordre des produits (M20) |
| la position d'un élément dans la file (ordre C), et l'inverse | `np.ravel_multi_index((2, 3, 5), (4, 7, 24))` → `413` ; `np.unravel_index(413, (4, 7, 24))` → `(2, 3, 5)` (M20) |
| réordonner les axes d'un tableau | `x.transpose(2, 0, 1)`, `np.moveaxis(x, -1, 0)` ; jamais `reshape`, qui garde l'ordre de la file (M20) |
| réduire en gardant les axes, puis diffuser | `m = x.mean(axis=(1, 2), keepdims=True)` ; `x - m` ; la variance : `((x - m) ** 2).sum(axis=(1, 2), keepdims=True) / (N - ddof)` (M20) |
| une application affine sur des points rangés en lignes | `X @ W + b` : `W` de forme (entrées, sorties), `b` ajouté à chaque ligne par broadcasting (diffusion, M16) |
| des coordonnées homogènes | `np.hstack([X, np.ones((len(X), 1))])` ; la matrice homogène : `np.vstack([np.hstack([W, np.zeros((n, 1))]), np.hstack([b, [1.0]])])` (M16) |
| une puissance de matrice | `np.linalg.matrix_power(A, k)` ; pour toutes les puissances, multiplier pas à pas : `P = P @ A` (M16) |
| des degrés dans un graphe | `A.sum(axis=1)` (sortants, lignes), `A.sum(axis=0)` (entrants, colonnes) (M16) |
| tester qu'une matrice est nilpotente (sans flottants) | `B = (A != 0).astype(int)`, puis $n - 1$ fois `B = ((B @ P) > 0).astype(int)` avec `P` le motif de départ : il ne reste que des zéros si et seulement si le graphe est sans cycle (M16) |
| la partie triangulaire stricte | `np.triu(A, k=1)`, `np.tril(A, k=-1)` ; `np.allclose(A, np.triu(A, k=1))` teste « strictement triangulaire supérieure » |
| une jacobienne par différences centrées (M17) | pour chaque `j` : `e = np.zeros(n); e[j] = h`, colonne `(f(x + e) - f(x - e)) / (2 * h)`, puis `np.column_stack(colonnes)` (une colonne par entrée) |
| une matrice diagonale à partir d'un vecteur, et l'inverse | `np.diag(v)` (vecteur → matrice), `np.diag(M)` (matrice → sa diagonale) |
| une jacobienne avec SciPy | `scipy.differentiate.jacobian(f, x).df` : `f` reçoit des tableaux de points, une colonne par point (M17) |
| un produit de Kronecker | `np.kron(A, B)` : la matrice par blocs $a_{ij}\mathbf{B}$ (M17.23) |
| parcourir toutes les cases d'un tableau | `for idx in np.ndindex(X.shape):` donne `(0, 0)`, `(0, 1)`… ; `E = np.zeros(X.shape); E[idx] = 1.0` est le déplacement d'une seule case (M18) |
| la somme des produits terme à terme, $\operatorname{tr}(\mathbf{G}^\top\mathbf{H})$ | `np.sum(G * H)` ; et $\operatorname{tr}(\mathbf{A}\mathbf{B})$ sans former le produit : `np.sum(A * B.T)` (M18) |
| vérifier un gradient matriciel le long d'une direction | `H = rng.normal(size=X.shape)` ; `(f(X + h * H) - f(X - h * H)) / (2 * h)` avec `h = 1e-5`, à comparer à `np.sum(G * H)` (M18) |
| la comatrice d'une matrice inversible | `np.linalg.det(X) * np.linalg.inv(X).T` ; le gradient de $\ln\lvert\det\mathbf{X}\rvert$ : `np.linalg.inv(X).T`, et `np.linalg.slogdet(X)` pour $\ln\lvert\det\mathbf{X}\rvert$ sans débordement (M18) |

## Algèbre linéaire (`np.linalg`)

| Je veux… | Code | Remarque |
|---|---|---|
| résoudre $\mathbf{A}\mathbf{x} = \mathbf{b}$ | `np.linalg.solve(A, b)` | toujours préférable à `inv(A) @ b` |
| l'inverse | `np.linalg.inv(A)` | |
| le déterminant | `np.linalg.det(A)` | valeur approchée : `1e-16` signifie « zéro » ; un déterminant petit ne veut pas dire « presque singulière » (M12c) |
| le rang | `np.linalg.matrix_rank(A)` | le nombre de valeurs singulières au-dessus d'un seuil d'environ $10^{-16}\,s_{\max}\max(m, n)$ : un rang **numérique** (M12a, M12d) |
| valeurs et vecteurs propres | `np.linalg.eig(A)` ; pour une matrice symétrique : `np.linalg.eigh(A)` ; les valeurs seules, en ordre croissant : `np.linalg.eigvalsh(A)` (elle ne lit qu'un triangle : la matrice doit être exactement symétrique, M19) | les vecteurs propres sont les **colonnes** du résultat ; `eigh` rend des valeurs réelles par ordre **croissant** et des vecteurs orthonormés, `eig` peut rendre des complexes (une rotation) |
| la SVD | `U, s, Vt = np.linalg.svd(A, full_matrices=False)` ; les valeurs seules : `np.linalg.svd(A, compute_uv=False)` | `A ≈ (U * s) @ Vt` ; `s` décroissant ; les $\mathbf{v}_i$ sont les **lignes** de `Vt` ; signes arbitraires (changer une ligne de `Vt` et la colonne de `U` ensemble) ; $\min(m, n)$ valeurs, nulles comprises |
| l'approximation de rang $k$ | `(U[:, :k] * s[:k]) @ Vt[:k]` | la meilleure de rang $k$ (Eckart-Young) |
| la pseudo-inverse | `np.linalg.pinv(A)` | $\mathbf{A}^+$, de forme $(n, m)$ ; un seuil relatif (`rcond`) traite les petites valeurs singulières comme nulles |
| le conditionnement | `np.linalg.cond(A)` | $s_{\max}/s_{\min}$ ; très grand (ou `inf`) pour une matrice presque singulière |
| les moindres carrés | `np.linalg.lstsq(X, y, rcond=None)[0]` | par la SVD : la solution de plus petite norme si les colonnes sont liées |
| une ACP | `from sklearn.decomposition import PCA` ; `pca = PCA(n_components=k).fit(X)` | centre, puis SVD (ou, si $n \gg p$, diagonalise la covariance ; `svd_solver="full"` impose la SVD) ; axes en **lignes** de `pca.components_`, variances `explained_variance_` (en $n - 1$), parts `explained_variance_ratio_`, scores `pca.transform(X)`, reconstruction `pca.inverse_transform(Z)` |
| la décomposition QR | `Q, R = np.linalg.qr(A)` | forme réduite par défaut ; les signes des colonnes de `Q` (et des lignes de `R`) peuvent différer de ceux de Gram-Schmidt (M12b) |
| Cholesky | `np.linalg.cholesky(A)` | $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$, `LinAlgError` si $\mathbf{A}$ n'est pas définie positive ; ne vérifie **pas** la symétrie (elle ne lit que le triangle inférieur) |
| la racine carrée d'une matrice | `scipy.linalg.sqrtm(A)` ; symétrique positive : `Q * np.sqrt(values) @ Q.T` avec `values, Q = np.linalg.eigh(A)` | jamais `np.sqrt(A)`, qui prend la racine des éléments |
| comparer deux résultats approchés | `np.allclose(a, b)` | jamais `==` entre flottants |

## Convolutions et signaux (M21)

| Je veux… | Code |
|---|---|
| la convolution de deux suites (un produit de polynômes, la loi d'une somme) | `np.convolve(a, b)` : mode plein, $n + k - 1$ valeurs ; `np.convolve(a, b, "valid")`, `np.convolve(a, b, "same")` ; le noyau est **retourné** |
| la corrélation croisée, sans retournement (celle des bibliothèques) | `np.correlate(x, w, "valid")`, le signal d'abord (`np.correlate(w, x, "valid")` rend le résultat à l'envers) ; c'est `np.convolve(x, w[::-1], "valid")` |
| retourner un noyau | `w[::-1]` ou `np.flip(w)` ; en 2D, `np.flip(K)` retourne les deux axes, comme `K[::-1, ::-1]` ; le retourné circulaire $\check{\mathbf{h}}$ : `np.roll(h[::-1], 1)` |
| décaler un signal périodique | `np.roll(x, 1)` calcule $\mathbf{P}\mathbf{x}$ (la dernière valeur revient en tête) ; `np.roll(x, t)` décale de $t$ cases |
| compléter par des zéros, sous-échantillonner, insérer des zéros | `np.pad(x, p)` ($p$ zéros de chaque côté) ; `x[::s]` ; `z = np.zeros((m - 1) * s + 1)` puis `z[::s] = y` |
| la matrice des fenêtres | `F = np.lib.stride_tricks.sliding_window_view(x, k)`, de forme $(n - k + 1, k)$ : `F @ w` est la corrélation valide, `F[::s] @ w` la même avec un pas $s$ ; pour une grille $(C, H, W)$ : `sliding_window_view(X, (kh, kw), axis=(1, 2))`, de forme $(C, H_{\text{out}}, W_{\text{out}}, k_h, k_w)$, puis `np.einsum("ocuv,cijuv->oij", W, F)` |
| la matrice d'une convolution | `scipy.linalg.convolution_matrix(w, n)` : la matrice de Toeplitz $(n + k - 1, n)$ de `x` ↦ `np.convolve(x, w)` (`mode="valid"` et `mode="same"` aussi) ; `scipy.linalg.toeplitz(c, r)` (première colonne, première ligne) ; `scipy.linalg.circulant(h)` (première colonne `h`) |
| filtrer une grille | `scipy.signal.correlate2d(X, K, mode="valid")`, sans retournement ; `scipy.signal.convolve2d` retourne les deux axes |
| une longue convolution | `scipy.signal.fftconvolve(a, b)` : le résultat de `np.convolve(a, b)`, par la FFT, plus rapide pour de longs noyaux |
| un produit extérieur, un noyau séparable | `np.outer(u, v)`, ou `u[:, None] * v[None, :]` ; `K` est de rang 1 si `np.linalg.svd(K, compute_uv=False)[1]` est négligeable devant la première valeur |
| le pire cas d'une perturbation bornée | boule L∞ : `eps * np.sign(g)`, qui donne `eps * np.linalg.norm(g, 1)` ; boule L2 : `eps * g / np.linalg.norm(g)`, qui donne `eps * np.linalg.norm(g)` |

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
| une queue binomiale | `scipy.stats.binom.sf(k - 1, n, p)` pour $P(X \ge k)$ (`sf(m)` rend $P(X > m)$) |
| une divergence KL entre deux lois de Bernoulli, en nats | `scipy.special.rel_entr(a, p) + scipy.special.rel_entr(1 - a, 1 - p)` |
| projeter sur un pavé, sur une boule | `np.clip(x, lo, hi)` (chaque coordonnée) ; `x * min(1.0, r / np.linalg.norm(x))` (même direction) (M19) |
| une matrice creuse tridiagonale | `scipy.sparse.diags([-1, 2, -1], [-1, 0, 1], shape=(n, n), format="csr")` ; `A @ x` reste un produit matrice-vecteur (M19) |
| l'exponentielle d'une matrice | `scipy.linalg.expm(T * J)` ; c'est la limite de `np.linalg.matrix_power(np.eye(n) + T / L * J, L)` (M20) |
| le gradient conjugué | `x, info = scipy.sparse.linalg.cg(A, b, rtol=1e-8, callback=f)` : `info == 0` si la tolérance relative est atteinte ; `f(xk)` est appelée à chaque itération (pour les compter) ; `M=` un préconditionneur (M19) |
| la variance d'une moyenne pondérée | `w @ S @ w`, avec `S` la matrice de covariance ; sur des tirages en lignes : `np.cov(X, rowvar=False)` |
| des poids exponentiels stables | `scipy.special.softmax(-eta * L, axis=1)`, ou `np.exp(-eta * (L - L.min(axis=1, keepdims=True)))` puis diviser par la somme de chaque ligne |
| tirer au hasard | `rng.normal(mu, sigma, size=n)`, `rng.uniform(a, b, size=n)`, `rng.integers(1, 7, size=n)` (dé) |

> ⚠️ **Piège classique — les flottants** — `0.1 + 0.2 == 0.3` vaut `False` : un ordinateur ne représente pas exactement 0,1. Compare avec `np.isclose` ; pour un calcul exact, `fractions.Fraction` ou SymPy (R1, M05a).
