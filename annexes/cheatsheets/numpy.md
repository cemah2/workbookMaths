# Cheatsheet NumPy pour les maths

Les bases de NumPy (tableaux, formes, broadcasting) sont dans le chapitre 0A de workbookIA et son `annexes/cheatsheets/numpy.md`. Ici, ce qui sert aux maths : vecteurs, matrices, algèbre linéaire, convolutions, récurrences, lois gaussiennes, mélanges, chaînes de Markov, calcul numérique.

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
| valeurs et vecteurs propres | `np.linalg.eig(A)` ; pour une matrice symétrique : `np.linalg.eigh(A)` ; les valeurs seules, en ordre croissant : `np.linalg.eigvalsh(A)` (elle ne lit qu'un triangle : la matrice doit être exactement symétrique, M19) ; les valeurs seules d'une matrice quelconque : `np.linalg.eigvals(A)` (M22) | les vecteurs propres sont les **colonnes** du résultat ; `eigh` rend des valeurs réelles par ordre **croissant** et des vecteurs orthonormés, `eig` peut rendre des complexes (une rotation) |
| la SVD | `U, s, Vt = np.linalg.svd(A, full_matrices=False)` ; les valeurs seules : `np.linalg.svd(A, compute_uv=False)`, ou `np.linalg.svdvals(A)` (NumPy ≥ 2.0) | `A ≈ (U * s) @ Vt` ; `s` décroissant ; les $\mathbf{v}_i$ sont les **lignes** de `Vt` ; signes arbitraires (changer une ligne de `Vt` et la colonne de `U` ensemble) ; $\min(m, n)$ valeurs, nulles comprises |
| l'approximation de rang $k$ | `(U[:, :k] * s[:k]) @ Vt[:k]` | la meilleure de rang $k$ (Eckart-Young) |
| la pseudo-inverse | `np.linalg.pinv(A)` | $\mathbf{A}^+$, de forme $(n, m)$ ; un seuil relatif (`rcond`) traite les petites valeurs singulières comme nulles |
| le conditionnement | `np.linalg.cond(A)` ; dans une norme induite : `np.linalg.cond(A, 1)`, `np.linalg.cond(A, np.inf)` (M22) | $s_{\max}/s_{\min}$ ; très grand (ou `inf`) pour une matrice presque singulière ; avec `1` ou `np.inf`, $\lVert\mathbf{A}\rVert\,\lVert\mathbf{A}^{-1}\rVert$ dans cette norme |
| les moindres carrés | `np.linalg.lstsq(X, y, rcond=None)[0]` | par la SVD : la solution de plus petite norme si les colonnes sont liées |
| une ACP | `from sklearn.decomposition import PCA` ; `pca = PCA(n_components=k).fit(X)` | centre, puis SVD (ou, si $n \gg p$, diagonalise la covariance ; `svd_solver="full"` impose la SVD) ; axes en **lignes** de `pca.components_`, variances `explained_variance_` (en $n - 1$), parts `explained_variance_ratio_`, scores `pca.transform(X)`, reconstruction `pca.inverse_transform(Z)` |
| la décomposition QR | `Q, R = np.linalg.qr(A)` | forme réduite par défaut ; les signes des colonnes de `Q` (et des lignes de `R`) peuvent différer de ceux de Gram-Schmidt (M12b) |
| Cholesky | `np.linalg.cholesky(A)` ; le facteur supérieur $\mathbf{L}^\top$ : `np.linalg.cholesky(A, upper=True)` (M25a) | $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$, `LinAlgError` si $\mathbf{A}$ n'est pas définie positive ; ne vérifie **pas** la symétrie (elle ne lit que le triangle inférieur) ; `scipy.linalg.cholesky(A)`, elle, rend par défaut le facteur **supérieur** (M25a) |
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

## Récurrences, puissances et normes de matrices (M22)

| Je veux… | Code |
|---|---|
| un nombre complexe | `z = 3 - 4j` (Python écrit `j` pour $i$) ; `z.real`, `z.imag`, `np.conj(z)` ; le module `np.abs(z)` ; l'argument `np.angle(z)`, en radians, entre $-\pi$ et $\pi$ (`np.angle(z, deg=True)` en degrés) |
| $e^{i\theta}$, la forme exponentielle | `np.exp(1j * theta)`, `r * np.exp(1j * theta)` ; dans l'autre sens, `r, theta = np.abs(z), np.angle(z)` ; le point `(x, y)` du plan est le complexe `x + 1j * y` |
| les valeurs propres complexes, le rayon spectral | `lam = np.linalg.eigvals(A)` : des complexes (`0.6+0.8j`…) dès qu'une valeur propre n'est pas réelle, dans un ordre quelconque ; `np.abs(lam)`, `np.angle(lam)` ; le rayon spectral `np.abs(lam).max()`, jamais `lam.max()`, qui compare les parties réelles |
| une rotation, une matrice normale | `R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])` ; `r * R` multiplie par `r * np.exp(1j * th)` ; tester qu'une matrice est normale : `np.allclose(A.T @ A, A @ A.T)` |
| les états d'une récurrence avec entrée | `X = np.zeros((T + 1, n))` ; `X[0] = x0` ; `for t in range(T): X[t + 1] = A @ X[t] + B @ U[t]` : `U` de forme $(T, m)$, une entrée par ligne, et un état par ligne de `X` ; un produit par pas, sans calculer $\mathbf{A}^t$ |
| la même chose avec SciPy | `_, Y, X = scipy.signal.dlsim((A, B, C, D, 1), U, x0=x0)` : les états $\mathbf{x}_0, \ldots, \mathbf{x}_{T-1}$ en lignes de `X`, les sorties $\mathbf{C}\mathbf{x}_t + \mathbf{D}\mathbf{u}_t$ en lignes de `Y` (ici `D = np.zeros((1, m))`) |
| la réponse impulsionnelle, et la sortie comme convolution | `h = np.zeros(K)` ; `v = b.copy()` ; `for k in range(K): h[k] = c @ v; v = A @ v` (`b` et `c` à une dimension) ; pour $\mathbf{x}_0 = \mathbf{0}$, `np.convolve(h, u)[t]` vaut $y_{t+1}$, tant que $t < K$ |
| un filtre récursif d'une seule variable | `scipy.signal.lfilter([0, b], [1, -a], u)` calcule $x_{t+1} = a\,x_t + b\,u_t$ depuis $x_0 = 0$, et rend $x_0, \ldots, x_{T-1}$ |
| les puissances d'une matrice | `np.linalg.matrix_power(A, t)` (`t = 0` donne l'identité) ; toutes, pas à pas : `P = np.eye(n)`, puis `P = A @ P` ; la formule de Gelfand : `np.linalg.norm(np.linalg.matrix_power(A, t), 2) ** (1 / t)`, pour `t` grand, s'approche de $\rho(\mathbf{A})$ |
| les normes induites, la norme de Frobenius | `np.linalg.norm(A, 1)` (colonnes), `np.linalg.norm(A, np.inf)` (lignes), `np.linalg.norm(A, 2)` ($s_{\max}$, aussi `np.linalg.svdvals(A)[0]`), `np.linalg.norm(A, "fro")` ; **sans `ord`, `np.linalg.norm(A)` est la norme de Frobenius** ; NumPy ≥ 2.0 : `np.linalg.matrix_norm(A, ord=2)` (Frobenius par défaut, lui aussi) |
| un produit de matrices, ses normes et leur majoration | `P = np.eye(n)` ; pour chaque `Ak` dans l'ordre des pas : `P = Ak @ P` (le dernier à gauche), puis `np.linalg.norm(P, 2)` ; la majoration : `np.cumprod([np.linalg.norm(Ak, 2) for Ak in As])` |
| des facteurs : ce qui reste, sans débordement | `np.cumprod(a)` (ce qui reste après chaque pas) ; des facteurs vectoriels, un pas par ligne : `np.cumprod(F, axis=0)` ; un long produit : `np.exp(np.cumsum(np.log(a)))`, son taux par pas `np.log(a).mean()` ; pour des matrices, renormaliser à chaque pas : `x = Ak @ x`, `s += np.log(np.linalg.norm(x))`, `x = x / np.linalg.norm(x)` |
| la jacobienne d'une composée itérée, une sensibilité | `J = np.eye(n)` ; `for t in range(T): J = jac(x) @ J; x = f(x)` (chaque jacobienne au point où $f$ est appliquée, avant de mettre `x` à jour) ; la sensibilité : `s = np.zeros(n)`, puis `s = dfdx(x, beta) @ s + dfdbeta(x, beta); x = f(x, beta)` à chaque pas |
| la norme globale d'un vecteur fait de blocs, le ramener sous un seuil | `g = np.sqrt(sum(np.sum(w ** 2) for w in blocks))`, ou `np.linalg.norm(np.concatenate([w.ravel() for w in blocks]))` ; `factor = min(1.0, c / g)` ; `[w * factor for w in blocks]` |

Dans `mymath/recurrence.py`, la docstring du module dit ce qui est permis : de `np.linalg`, seulement `eigvalsh` (dans `operator_norm`) et `norm` (dans `product_norms`), et pas de SciPy.

## Lois gaussiennes (M25a)

Une covariance `S` de forme $(d, d)$, une moyenne `mu` de forme $(d,)$, des points rangés en lignes dans `X`, de forme $(n, d)$.

| Je veux… | Code |
|---|---|
| le facteur de Cholesky d'une covariance | `L = np.linalg.cholesky(S)` (triangulaire inférieure, $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^\top$) ; `np.allclose(L @ L.T, S)` ; attention, `scipy.linalg.cholesky(S)` rend par défaut le facteur **supérieur** $\mathbf{L}^\top$ (`lower=True` pour $\mathbf{L}$) |
| résoudre $\mathbf{L}\mathbf{y} = \mathbf{x} - \boldsymbol{\mu}$ (une descente) | `from scipy.linalg import solve_triangular` (de SciPy : NumPy n'en a pas) ; `y = solve_triangular(L, x - mu, lower=True)` ; **sans `lower=True`, elle lit le triangle supérieur**, sans message ; plusieurs points : `solve_triangular(L, (X - mu).T, lower=True)`, une colonne par point ; `np.linalg.solve(L, x - mu)` donne le même résultat, sans profiter de la forme triangulaire |
| $\ln\det\boldsymbol{\Sigma}$ sans former le déterminant | `2 * np.log(np.diag(L)).sum()` ; ou `sign, logdet = np.linalg.slogdet(S)` (un couple : le signe, 1 pour une covariance définie positive, puis $\ln\lvert\det\rvert$) |
| la densité, la log-densité, l'entropie de $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ | `from scipy.stats import multivariate_normal` ; `mvn = multivariate_normal(mean=mu, cov=S)` ; `mvn.logpdf(X)` (une valeur par ligne de `X`), `mvn.pdf(x)`, `mvn.entropy()` (en nats) ; en grande dimension, `mvn.logpdf(x)`, jamais `np.log(mvn.pdf(x))` (qui rend `-inf`) ; en dimension 1, `scipy.stats.norm(m, s)` attend l'**écart-type** |
| tirer $n$ vecteurs de $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, un par ligne | `E = rng.standard_normal((n, d))` ($n$ tirages de $\mathcal{N}(\mathbf{0}, \mathbf{I})$) ; `X = mu + E @ L.T` (jamais `E @ L`) ; contrôle : `X.mean(axis=0)` et `np.cov(X, rowvar=False)` sont proches de `mu` et de `S` |
| la même chose en un appel | `rng.multivariate_normal(mu, S, size=n)` : par défaut `method="svd"` ; avec `method="cholesky"` (la plus rapide) et la même graine, exactement les tirages `mu + rng.standard_normal((n, d)) @ L.T` ; ou `multivariate_normal(mu, S).rvs(size=n, random_state=rng)` |
| le niveau de l'ellipsoïde de masse $1 - \beta$, la masse d'un niveau | `from scipy.stats import chi2` ; `c2 = chi2(d).ppf(1 - beta)` (le niveau $c^2$) ; `chi2(d).cdf(c**2)` (la masse de $\Delta \le c$) ; en dimension 2, `-2 * np.log(beta)` et `1 - np.exp(-c**2 / 2)` ; en dimension 1, `2 * scipy.stats.norm.cdf(c) - 1` |
| les axes d'une ellipse de niveau | `lam, Q = np.linalg.eigh(S)` (valeurs propres **croissantes**) : demi-axes `c * np.sqrt(lam)`, le long des colonnes de `Q` ; le grand axe est la dernière colonne, `Q[:, -1]` |
| la loi de la norme d'un tirage de $\mathcal{N}(\mathbf{0}, \mathbf{I}_d)$ | `scipy.stats.chi(d)` : `.pdf(r)`, `.mean()` ; `chi(2)` est la loi de Rayleigh (`scipy.stats.rayleigh`), `chi(3)` celle de Maxwell (`scipy.stats.maxwell`) ; sur des tirages : `np.linalg.norm(E, axis=1)` |
| des blocs | `a, b = [0, 2], [1]` ; `S_aa, S_ab, S_bb = S[np.ix_(a, a)], S[np.ix_(a, b)], S[np.ix_(b, b)]` ; un produit par $\boldsymbol{\Sigma}_{bb}^{-1}$ se fait par `np.linalg.solve(S_bb, …)`, jamais par `np.linalg.inv(S)` (les formules sont dans la fiche, §4 ; les coder est le 🔨 M25a.22) |
| une régression linéaire bayésienne | scikit-learn, qui choisit en plus $\sigma^2$ et $\tau^2$ : `reg = BayesianRidge(fit_intercept=False).fit(Phi, y)` (de `sklearn.linear_model`), `reg.coef_` ($\mathbf{m}_N$), `reg.sigma_` ($\mathbf{S}_N$), `reg.predict(Phi_new, return_std=True)` ; $\sigma^2$ = `1 / reg.alpha_`, $\tau^2$ = `1 / reg.lambda_` ; le calcul à la main est le 🔨 M25a.23 |
| $\hat{\boldsymbol{\mu}}$ et $\hat{\boldsymbol{\Sigma}}$ du maximum de vraisemblance | `xbar = X.mean(axis=0)` ; `np.cov(X, rowvar=False, bias=True)` (ou `ddof=0`), c'est-à-dire `(X - xbar).T @ (X - xbar) / len(X)` ; **sans `bias=True`, division par $n - 1$** ; $n$ petit devant $d$ : `sklearn.covariance.LedoitWolf().fit(X).covariance_` |
| une divergence KL entre deux lois continues | SciPy n'en a pas ; en dimension 1, `scipy.integrate.quad(lambda t: p.pdf(t) * (p.logpdf(t) - q.logpdf(t)), lo, hi)[0]`, sur le support de `p` ; en dimension 2, `scipy.integrate.dblquad(f, x0, x1, y0, y1)[0]`, avec **`f(y, x)`**, la variable intérieure d'abord ; par des tirages `Xp` de $p$ : `np.mean(p.logpdf(Xp) - q.logpdf(Xp))` ; `scipy.stats.entropy(pk, qk)` est la KL **discrète** de M06 |
| une entropie différentielle | `multivariate_normal(mu, S).entropy()`, `scipy.stats.norm(m, s).entropy()`, en nats ; c'est $\frac12[d\ln(2\pi e) + \ln\det\boldsymbol{\Sigma}]$ |

Dans `mymath/gaussian.py`, la docstring du module dit ce qui est permis : de `np.linalg`, seulement `cholesky` et `solve` (et `LinAlgError`) ; ni `multivariate_normal` (ni celle de NumPy, ni la méthode d'un `Generator`, qui, avec `method="cholesky"`, rendrait les tirages de `sample_mvn` à ta place), ni SciPy : les tests comparent tes résultats aux leurs. La fiche fait le slerp sur papier : ni `mymath` ni le notebook n'en ont de fonction.

## Mélanges, ACP probabiliste et angles principaux (M25b)

Des données `X` de forme $(n, d)$, une par ligne (des mesures en dimension 1 forment une colonne : `x.reshape(-1, 1)`) ; un tableau `a` de forme $(n, K)$, une ligne par donnée.

| Je veux… | Code |
|---|---|
| le log-sum-exp de chaque ligne de `a` | `from scipy.special import logsumexp` ; `logsumexp(a, axis=1)`, de forme $(n,)$ ; avec `keepdims=True`, de forme $(n, 1)$, qui se diffuse sur les colonnes ; **sans `axis`, un seul nombre pour tout le tableau** ; la formule factorisée par le maximum est celle de M05a ; jamais `np.log(np.exp(a).sum(axis=1))`, qui rend `-inf` dès que les `a` sont très négatifs |
| ajuster un mélange de gaussiennes | `from sklearn.mixture import GaussianMixture` ; `gm = GaussianMixture(n_components=K, n_init=5, random_state=0).fit(X)` (`X` à deux dimensions : un tableau 1-D est refusé) ; `gm.weights_` $(K,)$, `gm.means_` $(K, d)$, `gm.covariances_` $(K, d, d)$ ; `reg_covar` (par défaut `1e-6`) est ajouté à la diagonale de chaque covariance ; `n_init` relance l'EM depuis plusieurs initialisations (par défaut une seule, tirée d'un k-means) et garde la meilleure ; l'ordre des composantes est arbitraire : trier, par exemple `np.argsort(gm.means_[:, 0])`, avant de comparer deux ajustements |
| les responsabilités et les log-densités du mélange ajusté | `gm.predict_proba(X)` : les $r_{ik}$, de forme $(n, K)$, chaque ligne de somme 1 (la documentation dit « density » : ce sont bien les probabilités a posteriori) ; `gm.predict(X)` : le numéro de la plus grande, une affectation dure ; `gm.score_samples(X)` : les $\ln p(\mathbf{x}_i)$, de forme $(n,)$ ; `gm.score(X)` : leur **moyenne**, en nats par donnée ; `gm.lower_bound_` : la même moyenne, calculée au dernier pas E, avant le dernier pas M (un peu sous `gm.score(X)`) |
| les valeurs propres dans l'ordre de l'ACP probabiliste | `S = np.cov(X, rowvar=False, bias=True)` (la covariance du maximum de vraisemblance, en $n$) ; `lam, U = np.linalg.eigh(S)` : valeurs **croissantes**, vecteurs propres en colonnes ; `lam, U = lam[::-1], U[:, ::-1]` pour $\lambda_1 \ge \cdots \ge \lambda_d$ |
| l'ACP probabiliste avec scikit-learn | les formules de Tipping et Bishop sont dans la fiche (§6), et le 📦 M25b.24 les code ; `pca = PCA(n_components=k).fit(X)` (de `sklearn.decomposition`), `pca.noise_variance_`, `pca.get_covariance()`, `pca.score_samples(X)` (les $\ln p(\mathbf{x}_i)$ du modèle), mais **en $n - 1$** : `noise_variance_` vaut $\frac{n}{n - 1}\hat\sigma^2$, et `get_covariance()` vaut $\frac{n}{n - 1}$ fois la covariance $\hat{\mathbf{W}}\hat{\mathbf{W}}^\top + \hat\sigma^2\mathbf{I}$ du modèle |
| les angles principaux | `scipy.linalg.subspace_angles(A, B)` : les angles principaux entre les sous-espaces engendrés par les colonnes de `A` et de `B`, qu'il orthonormalise lui-même (📦 M25b.24) ; leurs cosinus par la définition de la fiche : `QA = np.linalg.qr(A)[0]`, `QB = np.linalg.qr(B)[0]` (des bases orthonormées, si les colonnes sont indépendantes), puis `np.linalg.svd(QA.T @ QB, compute_uv=False)` |
| la densité, la fonction de répartition de $\mathcal{N}(\mu, \sigma^2)$ | `from scipy.stats import norm` ; `norm.pdf(c, mu, sigma)`, c'est $\mathcal{N}(c \mid \mu, \sigma^2)$ (le troisième argument est l'**écart-type**) ; `norm.logpdf(c, mu, sigma)` ; `norm.cdf(c, mu, sigma)`, $P(X \le c)$ ; `norm.sf(c, mu, sigma)`, $P(X > c)$, précise même minuscule (`1 - norm.cdf(10)` rend 0, `norm.sf(10)` environ $7{,}6 \times 10^{-24}$) ; une loi figée : `law = norm(mu, sigma)`, puis `law.pdf(c)`, `law.cdf(c)` |
| une information mutuelle continue, estimée sur des tirages | `from sklearn.feature_selection import mutual_info_regression` ; `mutual_info_regression(X, y)` : une valeur par colonne de `X`, en nats, estimée par les plus proches voisins (une estimation, avec son erreur, ramenée à 0 si elle sort négative) |

Dans `mymath/latent.py`, la docstring du module dit ce qui est permis : NumPy, et de `np.linalg` seulement `cholesky` et `solve` ; ni `np.cov` ni `np.average` (les tests comparent ton pas M avec eux), aucune SciPy (ni `logsumexp`, ni `multivariate_normal`) et pas de scikit-learn (ni `GaussianMixture`) : les tests comparent tes résultats aux leurs. Le log-sum-exp s'importe de ton `approx.py` (M05a ; il prend une séquence à la fois) ou s'écrit par la formule factorisée ci-dessus ; `mvn_logpdf` s'importe de ton `gaussian.py` (M25a). Les formules des pas E et M, de la log-vraisemblance et de l'ELBO d'un mélange sont dans la fiche (§3 à §5) et dans le formulaire ; les coder est le travail des 🔨 M25b.20 à M25b.22.

## Chaînes de Markov (M26)

Une matrice de transition `P` de forme $(m, m)$ : une loi est une ligne (`mu @ P` avance d'un pas), une valeur par état une colonne (`P @ V` moyenne sur le pas suivant), comme dans `mymath/markov.py`.

| Je veux… | Code |
|---|---|
| vérifier qu'une matrice est stochastique, ou sous-stochastique | `np.all(P >= 0) and np.allclose(P.sum(axis=1), 1)` : ce sont les **lignes** (`axis=1`) qui ont pour somme 1 ; `np.isclose(P.sum(axis=1), 1)` dit, ligne par ligne, lesquelles ; sous-stochastique : `np.all(P.sum(axis=1) <= 1 + 1e-9)`, et `1 - P.sum(axis=1)` est la probabilité de finir après chaque état |
| une puissance de la matrice de transition | `np.linalg.matrix_power(P, n)` (M22) ; jamais `P ** n`, qui élève chaque coefficient (ses lignes n'ont plus pour somme 1) |
| les modules des valeurs propres, du plus grand au plus petit | `lam = np.linalg.eigvals(P)` (des complexes possibles, dans un ordre quelconque) ; `np.sort(np.abs(lam))[::-1]` : 1 d'abord pour une matrice stochastique, puis $\lvert\lambda_2\rvert$ ; pour une chaîne qui tourne sur trois états, trois modules égaux à 1 |
| les vecteurs propres d'une matrice quelconque | `vals, vecs = np.linalg.eig(A)` : `vecs[:, k]` (une **colonne**) va avec `vals[k]`, et `A @ vecs[:, k]` vaut `vals[k] * vecs[:, k]` (vecteurs propres **à droite**) ; l'ordre est quelconque, chaque vecteur a une norme 2 égale à 1 et un signe arbitraire, et tout devient complexe dès qu'une valeur propre l'est ; pour une loi stationnaire, c'est à `P.T` qu'on l'applique (M26 §2) |
| une base du noyau d'une matrice | `from scipy.linalg import null_space` ; `null_space(A)` : une base orthonormée du noyau, une colonne par vecteur (aucune colonne si le noyau est réduit à $\{\mathbf{0}\}$) ; chaque colonne a une norme 2 égale à 1, pas une somme 1, et un signe arbitraire ; `A @ null_space(A)` est proche de 0 |
| simuler un pas, une trajectoire | `rng.choice(m, p=P[s])` tire l'état qui suit `s` (la ligne doit avoir pour somme 1, à l'arrondi près, sinon `ValueError`) ; une trajectoire : `S = [s0]`, puis `for t in range(T): S.append(rng.choice(m, p=P[S[-1]]))` |
| compter les visites | `np.bincount(S, minlength=m)` : le nombre de visites à chaque état, les états jamais visités compris ; divisé par `len(S)`, la fréquence des visites, qui s'approche de $\boldsymbol{\pi}$ sur une longue trajectoire d'une chaîne irréductible (théorème ergodique) |
| une durée géométrique | `rng.geometric(p, size=n)` : le nombre d'essais jusqu'au premier succès, dans $\{1, 2, \ldots\}$, de moyenne $\frac1p$ ; un processus qui continue à chaque pas avec la probabilité `gamma` dure `rng.geometric(1 - gamma)` pas : le paramètre est la probabilité de **s'arrêter** |
| extraire des blocs (états transitoires, états absorbants) | `T, A = [0, 1, 2], [3, 4]` ; `Q = P[np.ix_(T, T)]`, `B = P[np.ix_(T, A)]` ; `P[T][:, T]` donne le même bloc ; jamais `P[T, T]`, qui rend la diagonale `[P[0, 0], P[1, 1], P[2, 2]]` |
| un maximum coordonnée par coordonnée, l'indice d'un maximum | `np.maximum(a, b)` compare `a` et `b` case par case et rend un tableau ; `np.max(a)` rend le plus grand coefficient de `a` (un nombre), `np.max(X, axis=1)` celui de chaque ligne ; `np.argmax(a)` rend l'indice du premier maximum |

Dans `mymath/markov.py`, la docstring du module dit ce qui est permis : NumPy, et de `np.linalg` seulement `solve` et `matrix_rank` (dans `stationary_distribution` et `bellman_linear_solve`) ; ni `matrix_power`, `eig`, `eigvals`, `inv`, ni SciPy : les tests comparent tes résultats aux leurs. Les formules de la loi à $n$ pas, de la loi stationnaire, du système de Bellman et de ses itérés sont dans la fiche (§1, §2, §5 et §6) et dans le formulaire ; les coder est le travail des 🔨 M26.16 à M26.19.

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
