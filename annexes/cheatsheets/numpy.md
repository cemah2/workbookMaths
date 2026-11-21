# Cheatsheet NumPy pour les maths

Les bases de NumPy (tableaux, formes, broadcasting) sont dans le chapitre 0A de workbookIA et son `annexes/cheatsheets/numpy.md`. Ici, ce qui sert aux maths : vecteurs, matrices, algèbre linéaire, convolutions, récurrences, lois gaussiennes, mélanges, chaînes de Markov, distances entre lois, matrices de Gram et motifs sur une grille, bases 2 et 16, tables creuses, rotations de l'espace, horloges et softmax en ligne, rangs et classements, équations différentielles et décibels, coalitions, rangs moyens et grilles agrandies, lois données par leur taux et log-sum-exp pondéré, calcul numérique.

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
| un produit à plusieurs indices | `np.einsum("ij,jk->ik", A, B)` (le produit matriciel écrit avec ses indices) ; une lettre absente du résultat est sommée ; `"sij,sjk->sik"` multiplie des matrices empilées ; `optimize=True` et `np.linalg.multi_dot` choisissent l'ordre des produits (M20) ; `np.linalg.multi_dot([C, F, x])` calcule $\mathbf{C}\mathbf{F}\mathbf{x}$ sans former $\mathbf{C}\mathbf{F}$ quand c'est moins coûteux (MB4) |
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
| le rang | `np.linalg.matrix_rank(A)` | le nombre de valeurs singulières au-dessus d'un seuil d'environ $10^{-16}\,s_{\max}\max(m, n)$ : un rang **numérique** (M12a, M12d) ; avec un seuil absolu, `np.linalg.matrix_rank(A, tol=t)` compte les valeurs singulières au-dessus de `t` : on donne le seuil avec le rang (MB4) |
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

## Programmes linéaires et distances entre lois (M27)

Des échantillons `x` et `y` à une dimension ; des lois discrètes `p` et `q` sur les mêmes classes, des tableaux de probabilités.

| Je veux… | Code |
|---|---|
| résoudre un programme linéaire | `from scipy.optimize import linprog` ; `res = linprog(c, A_ub=A, b_ub=b, A_eq=Ae, b_eq=be, bounds=…)` **minimise** `c @ x` sous `A @ x <= b` et `Ae @ x == be` ; pour maximiser, passer `-c` et lire `-res.fun` ; une contrainte $\ge$ se multiplie par $-1$ ; par défaut `bounds=(0, None)` : toutes les variables sont positives ou nulles (une variable libre : `bounds=(None, None)`, ou une liste d'un couple par variable) ; maximiser $3x + 2y$ sous $x + y \le 4$ et $x + 3y \le 6$ : `res = linprog([-3, -2], A_ub=[[1, 1], [1, 3]], b_ub=[4, 6])`, puis `res.x` → `[4., 0.]` et `-res.fun` → `12.0` ; contrôler `res.status == 0` (2 : aucun point admissible, 3 : problème non borné) |
| la fonction quantile d'une loi normale | `from scipy.stats import norm` ; `norm.ppf(u, mu, sigma)` $= \mu + \sigma\,\Phi^{-1}(u)$, le troisième argument étant l'**écart-type** ; `norm.ppf(0.975)` → `1.959963984540054` ; `norm.ppf(0)` et `norm.ppf(1)` valent `-inf` et `inf` ; `norm.cdf(norm.ppf(u))` redonne `u` |
| la statistique de Kolmogorov-Smirnov de deux échantillons | `from scipy.stats import ks_2samp` ; `res = ks_2samp(x, y)` (tailles quelconques) : `res.statistic` est $\sup_t\lvert F_n(t) - G_m(t)\rvert$, `res.statistic_location` la valeur où cet écart est atteint ; `res.pvalue` est la p-valeur du test « même loi » (M08), prévu pour des lois continues ; `ks_2samp([1, 2, 3], [4, 5, 6]).statistic` → `1.0` |
| les termes d'une divergence KL discrète | `from scipy.special import rel_entr` ; `rel_entr(p, q)` rend les $p_k\ln\frac{p_k}{q_k}$, en nats : `0` là où $p_k = 0$, `inf` là où $p_k > 0 = q_k$ ; leur somme `rel_entr(p, q).sum()` est $\mathrm{KL}(p \,\Vert\, q)$, comme `scipy.stats.entropy(p, q)` (qui normalise d'abord `p` et `q`) ; `np.sum(p * np.log(p / q))` rend `nan` dès que $p_k = 0$ ; `rel_entr([0.5, 0.5, 0], [0.25, 0.5, 0.25]).sum()` → $\frac12\ln 2 \approx 0{,}3466$ |

Dans `mymath/distances.py`, la docstring du module dit ce qui est permis : NumPy et le module `math`, rien de `np.linalg` et aucune SciPy (`scipy.optimize.linprog` résout un jeu) : les tests comparent tes résultats à `linprog`, à `np.linalg.matrix_power` et à une intégrale de l'écart des fonctions quantiles. Les formules des valeurs d'un jeu, des stratégies d'indifférence, des itérés de la descente-montée et de $W_2$ entre deux gaussiennes sont dans la fiche (§1, §2, §4 et §8) et dans le formulaire ; les coder est le travail des 🔨 M27.19 à M27.22.

## Matrices de Gram, motifs sur une grille et entropie (M28)

Des points rangés en lignes dans `X` et `Y`, de forme $(n, d)$ ; une grille de `H` lignes et `W` colonnes ; une loi `p`, un tableau de probabilités.

| Je veux… | Code |
|---|---|
| les carrés des distances lus dans une matrice de Gram | `g = np.diag(G)` ; `D2 = g[:, None] + g[None, :] - 2 * G` ($\lVert\mathbf{x}_i - \mathbf{x}_j\rVert^2 = G_{ii} + G_{jj} - 2G_{ij}$) ; à partir des points, `scipy.spatial.distance.cdist(X, X, "sqeuclidean")` (plus bas, « Calcul numérique ») ; les arrondis peuvent laisser de petites valeurs négatives : `np.sqrt(np.maximum(D2, 0))` |
| comparer deux configurations à une isométrie près | jamais leurs coordonnées : `np.allclose(cdist(X, X), cdist(Y, Y))` (mêmes distances), `np.allclose(X @ X.T, Y @ Y.T)` (même matrice de Gram, à origine fixée) ; pour les superposer, `from scipy.linalg import orthogonal_procrustes` ; `Xc, Yc = X - X.mean(axis=0), Y - Y.mean(axis=0)` ; `R, _ = orthogonal_procrustes(Xc, Yc)` : la matrice orthogonale (rotation, ou symétrie) qui rend `Xc @ R` le plus proche possible de `Yc` au sens des moindres carrés |
| la moyenne quadratique d'un vecteur, les trois pas normalisés | `np.sqrt(np.mean(g ** 2))`, c'est `np.linalg.norm(g) / np.sqrt(g.size)` ; `g / np.linalg.norm(g)`, `g / np.sqrt(np.mean(g ** 2))` et `np.sign(g)` (`np.sign(0.0)` vaut `0.0`) |
| un motif périodique sur une grille | `i, j = np.meshgrid(np.arange(H), np.arange(W), indexing="ij")`, ou `i, j = np.indices((H, W))` ; `Z = np.cos(2 * np.pi * (f1 * i + f2 * j) + phi)`, de forme `(H, W)`, où `Z[i, j]` est la case de la ligne `i` et de la colonne `j` ; **sans `indexing="ij"`, `meshgrid` rend des tableaux de forme `(W, H)`** ; le damier : `(-1.0) ** (i + j)` ; pour le voir, `ax.imshow(Z, cmap="gray")` |
| l'entropie d'une loi, en nats | `scipy.stats.entropy(p)` : le logarithme népérien par défaut (`base=2` pour des bits), une probabilité nulle compte pour 0, et `p` est renormalisée si sa somme n'est pas 1 ; `-np.sum(p * np.log(p))` rend `nan` dès qu'un $p_i$ est nul ; `scipy.special.entr(p).sum()` additionne les termes $-p_i\ln p_i$ |

Dans `mymath/sampling.py`, la docstring du module dit ce qui est permis : NumPy, et de `np.linalg` seulement `eigh` (dans `points_from_gram`) ; aucune SciPy (`scipy.special.softmax` et `scipy.special.logsumexp` donneraient `temper`) ni scikit-learn : les tests comparent tes résultats à SciPy. Les fonctions prennent des probabilités, jamais des scores, et ne tirent rien au hasard. Les formules des positions de matrice de Gram donnée, de la loi tempérée et du plus petit ensemble de masse donnée sont dans la fiche (§2 et §5) et dans le formulaire ; les coder est le travail des 🔨 M28.13 et M28.14.

## Bases 2 et 16, tables creuses et paires (MB2)

Un entier Python `n` ; un mot de bits `w` ; une table de comptes `M`, creuse ; `n` éléments à comparer deux à deux.

| Je veux… | Code |
|---|---|
| écrire un entier en base 2 ou en base 16, le relire | `bin(n)` et `hex(n)` rendent des chaînes avec les préfixes `'0b'` et `'0x'` (`hex` écrit en minuscules) ; sans préfixe : `format(n, "b")`, `format(n, "X")` (majuscules) ; sur une largeur fixe, complétée par des zéros à gauche : `f"{n:08b}"` (8 bits), `f"{n:02X}"` (un octet) ; `int(s, 2)` et `int(s, 16)` relisent une chaîne, avec ou sans préfixe ; pour NumPy : `np.binary_repr(n, width=8)`, `np.base_repr(n, base=16)` |
| les bits d'un entier, les bits qui numérotent $N$ valeurs | `n.bit_length()` : les $\lfloor\log_2 n\rfloor + 1$ bits de l'entier $n \ge 1$ ; `(N - 1).bit_length()` : les $\lceil\log_2N\rceil$ bits qui numérotent $N \ge 2$ valeurs, en entiers exacts (`math.ceil(math.log2(N))` passe par un flottant, et se trompe d'un bit pour $N = 2^{53} + 1$) ; jamais `len(bin(n))`, qui compte le préfixe |
| découper un mot de bits en champs, l'assembler | le champ de `l` bits qui commence au bit `i` : `(w >> i) & ((1 << l) - 1)`, c'est `(w // 2**i) % 2**l` ; placer `a` devant un champ `b` de `l` bits : `(a << l) + b` (ou `a * 2**l + b`) ; les mêmes opérateurs agissent case par case sur un tableau d'entiers (`dtype=np.uint8`, `np.uint16`) ; les 8 bits de chaque octet d'un tableau : `np.unpackbits(np.asarray(octets, dtype=np.uint8))`, le bit de poids fort d'abord |
| une grande table creuse, ses $k$ plus grandes valeurs singulières | `from scipy.sparse import csr_matrix` ; `S = csr_matrix(M)` ; `S.nnz` compte les cases non nulles, et `S.data.nbytes + S.indices.nbytes + S.indptr.nbytes` mesure la mémoire ; `from scipy.sparse.linalg import svds` ; `U, s, Vt = svds(S, k=k)`, avec `k < min(S.shape)` : l'ordre des valeurs singulières n'est pas garanti (croissant avec le solveur par défaut), donc `order = np.argsort(s)[::-1]`, puis `U[:, order]`, `s[order]` et `Vt[order]` ; `S - S.mean(axis=0)` rend une matrice **pleine** (une `numpy.matrix`) : le centrage détruit le creux |
| un logit, une sigmoïde | `scipy.special.logit(p)` $= \ln\frac{p}{1 - p}$ et `scipy.special.expit(z)` $= \sigma(z)$, réciproques l'une de l'autre, terme à terme sur un tableau |
| compter les paires, les parcourir | `math.comb(n, 2)` $= \binom{n}{2}$ ; `itertools.combinations(range(n), 2)` énumère les paires $(i, j)$, $i < j$ ; `i, j = np.triu_indices(n, k=1)`, puis `G[i, j]` : les $\binom{n}{2}$ coefficients au-dessus de la diagonale d'une matrice $n \times n$, chaque paire une fois |

Dans `mymath/cooccurrence.py`, la docstring du module dit ce qui est permis : NumPy et le module `math`, mais aucune SciPy (`scipy.special.logit`, `scipy.special.xlogy`, `scipy.optimize`) ni scikit-learn (`mutual_info_score`, `LogisticRegression`) : les tests comparent tes résultats aux leurs. Une loi jointe s'y donne en probabilités, jamais en comptes, et les logarithmes sont népériens. Les formules de la PMI, du logit d'une population estimé sur un échantillon cas-témoins et du retrait d'une direction sont dans la fiche (§2, §5 et §7) et dans le formulaire ; les coder est le travail des 🔨 MB2.13 et MB2.14.

## Rotations, horloges et softmax en ligne (MB3)

Des angles en radians ; des points `X` en lignes, de forme $(n, d)$ ; des scores `s` qui peuvent valoir `-np.inf`.

| Je veux… | Code |
|---|---|
| l'angle d'un point $(x, y)$ | `np.arctan2(y, x)`, en radians dans $[-\pi, \pi]$ : l'ordonnée d'abord ; `np.angle(x + 1j * y)` rend le même angle ; `% (2 * np.pi)` le ramène dans $[0, 2\pi[$, `np.degrees` le passe en degrés ; `np.arctan(y / x)` se trompe de quadrant quand $x < 0$ |
| une matrice diagonale par blocs | `scipy.linalg.block_diag(A, B, C)` : les blocs le long de la diagonale, des zéros ailleurs |
| des rotations de l'espace avec SciPy | `from scipy.spatial.transform import Rotation` ; `r = Rotation.from_rotvec(theta * axis)`, avec un axe unitaire et un angle en radians, positif quand on regarde l'axe depuis sa pointe vers l'origine ; `r.as_matrix()`, `r.apply(x)`, `r.inv()` |
| des scores masqués | `-np.inf` : `np.exp(-np.inf)` vaut `0.0`, et `scipy.special.softmax` donne un poids nul à un tel score ; si tous les scores valent `-np.inf`, elle rend des `nan` (un $0/0$, avec un `RuntimeWarning`), et `scipy.special.logsumexp` rend `-inf` |
| la mémoire d'un tableau, des distances par blocs de lignes | `A.nbytes` : 8 octets par nombre en `float64`, 4 en `float32` ; un bloc de `B` lignes de la matrice des distances : `scipy.spatial.distance.cdist(X[debut:debut + B], X)`, de forme `(B, n)` ; `sklearn.metrics.pairwise_distances_chunked(X, working_memory=m)` rend les blocs de lignes l'un après l'autre, chacun d'environ `m` Mio au plus |
| une moyenne exponentielle normalisée | `pd.Series(y).ewm(alpha=1 - lam, adjust=True).mean()` : au jour $t$, les poids $\lambda^{t - u}$ des jours $u \le t$, divisés par leur somme ; avec `adjust=False`, la récurrence $\hat y_t = \lambda\,\hat y_{t-1} + (1 - \lambda)\,y_t$ (R5) |

Dans `mymath/positional.py`, la docstring du module dit ce qui est permis : NumPy et le module `math`, mais aucune SciPy (`scipy.special.softmax`, `scipy.special.logsumexp`, `scipy.spatial.transform.Rotation`) ni `np.logaddexp` : les tests comparent tes résultats aux leurs, et aux matrices de MML (3.76)–(3.81). Les indices des coordonnées partent de 0, et une fonction ne modifie jamais les tableaux qu'elle reçoit. Les formules de la rotation de Givens, de la mise à jour par un bloc et de la fusion de deux états sont dans la fiche (§3 et §8) et dans le formulaire ; les coder est le travail des 🔨 MB3.14, MB3.15 et MB3.16.

## Rangs, classements et rapports de cotes (MB4)

Une matrice `M` de forme $(m, n)$ ; les notes `t` d'un juge ; un tableau $2 \times 2$ de comptes `table`.

| Je veux… | Code |
|---|---|
| une QR qui révèle le rang | `Q, R, P = scipy.linalg.qr(M, pivoting=True, mode="economic")` : `M[:, P]` vaut `Q @ R`, et les valeurs absolues de la diagonale de `R` décroissent ; celles qui dépassent une tolérance donnent un rang numérique, et `P` dit dans quel ordre les colonnes ont été prises (MB4 §1) |
| les rangs de notes | `scipy.stats.rankdata(t)` donne le rang 1 à la **plus petite** note ; pour un juge dont la meilleure note est la plus haute : `scipy.stats.rankdata(-t)` ; deux notes égales reçoivent la moyenne des rangs en jeu (`method="average"`, par défaut ; `method="min"` leur donne le plus petit) ; chaque ligne d'un tableau : `axis=1` |
| un rapport des cotes | `from scipy.stats.contingency import odds_ratio` ; `odds_ratio(table, kind="sample").statistic` vaut `table[0, 0] * table[1, 1] / (table[0, 1] * table[1, 0])` ; le réglage par défaut, `kind="conditional"`, donne une autre estimation ; `table` doit contenir des entiers (`ValueError` pour des flottants) : avec la correction ½, on calcule le rapport à la main |
| un taux de succès@$k$ | `sklearn.metrics.top_k_accuracy_score(y_true, scores, k=k)` : la part des lignes de `scores` (une par question, une colonne par candidat) dont le candidat juste, `y_true`, est parmi les `k` plus grands scores ; à scores égaux, le candidat d'indice le plus grand passe d'abord |

Dans `mymath/ranks.py`, la docstring du module dit ce qui est permis : NumPy (`@` compris), mais rien de `np.linalg` (ni `matrix_rank`, ni `svd`, ni `qr`…), ni SciPy (`scipy.linalg`, `scipy.stats.rankdata`), ni SymPy : les tests comparent tes résultats aux leurs ; dans `borda_scores`, ni `np.argsort` ni `np.lexsort` ; `random_ranking_mrr` calcule en `fractions.Fraction`, avec `math.comb`, sans énumérer les $n!$ ordres. Les candidats sont numérotés à partir de 0, un rang commence à 1, et une fonction ne modifie jamais les tableaux qu'elle reçoit. La factorisation CR, les points de Borda et la loi du premier pertinent sont dans la fiche (§1, §5 et §6) et dans le formulaire ; les coder est le travail des 🔨 MB4.8 et MB4.9.

## Équations différentielles, décibels et débruitage (MB5)

Un champ `f(t, x)`, le temps d'abord ; des instants `t0` et `t1` (`t1 < t0` pour remonter le temps) ; un rapport de variances `snr`.

| Je veux… | Code |
|---|---|
| suivre une équation différentielle avec SciPy | `sol = scipy.integrate.solve_ivp(f, (t0, t1), [x0], rtol=1e-10, atol=1e-10)` : `f(t, y)` reçoit un tableau 1-D `y`, même pour une seule inconnue ; `sol.y` a la forme `(n, nombre d'instants)`, d'où `sol.y[0, -1]` pour la valeur finale d'une équation à une inconnue, et `sol.t` les instants ; `t_eval=[…]` choisit les instants rendus, `sol.nfev` compte les évaluations du champ ; par défaut, une méthode de Runge-Kutta à pas adaptatif (`method="RK45"`), aux tolérances lâches (`rtol=1e-3`, `atol=1e-6`) : serre-les pour en faire une référence ; `t1 < t0` est permis |
| l'ancienne interface, `odeint` | `scipy.integrate.odeint(func, x0, t)` attend `func(y, t)`, **l'état d'abord**, l'inverse de `solve_ivp`, sauf avec `tfirst=True` ; elle rend un tableau de forme `(len(t), n)` ; la documentation conseille `solve_ivp` pour du code nouveau |
| passer un champ écrit « le point d'abord » | `lambda s, x: v(x, s)` : `euler_ode`, `midpoint_ode` et `solve_ivp` appellent toujours `f(t, x)`, le temps d'abord ; un champ écrit `v(x, s)`, comme celui de workbookIA B5, se passe ainsi |
| un rapport de variances en décibels, et retour | `10 * np.log10(snr)` ; un rapport d'écarts-types (d'amplitudes) donne le même nombre de décibels par `20 * np.log10(a / b)` ; dans l'autre sens, `10 ** (db / 10)` ; `scipy.special.logit` et `expit` passent de la part $\gamma$ à $\ln\operatorname{SNR}$ et retour (MB2) |
| une intégrale sur toute la droite | `scipy.integrate.quad(f, -np.inf, np.inf)` rend la valeur et une estimation de l'erreur ; une densité étroite loin de 0 peut lui échapper : `quad(lambda x: norm.pdf(x, 50, 0.01), -np.inf, np.inf)` rend `(0.0, 0.0)` ; intègre alors sur un intervalle borné qui contient la masse |
| un arbre de régression qui prédit une moyenne, ou une médiane | `from sklearn.tree import DecisionTreeRegressor` ; `criterion="squared_error"` (par défaut) : chaque feuille prédit la moyenne de ses cibles ; `criterion="absolute_error"` : leur médiane |

Dans `mymath/gaussian_paths.py`, la docstring du module dit ce qui est permis : NumPy et le module `math`, et aucune SciPy (`solve_ivp`, `odeint`, `quad`, `scipy.stats.norm`, `logsumexp`, `softmax`) : les tests comparent tes résultats aux leurs et à des simulations ; les imports relatifs de tes propres modules sont permis (`from .approx import logsumexp`, M05a). Un champ s'écrit `f(t, x)`, le temps d'abord, et une fonction ne modifie jamais les tableaux qu'elle reçoit. Les moments d'une récurrence, le débruiteur d'un mélange et les deux méthodes sont dans la fiche ; les coder est le travail des 🔨 MB5.16 à MB5.18.

## Coalitions, corrélation de rangs et grilles agrandies (MB6)

Des joueurs `0, …, n - 1` ; deux échantillons appariés `x` et `y` ; un profil `a` de `h` valeurs à agrandir en `H`.

| Je veux… | Code |
|---|---|
| parcourir les coalitions, les ordres | `[frozenset(c) for k in range(n + 1) for c in itertools.combinations(range(n), k)]` donne les $2^n$ coalitions, taille par taille, du `frozenset()` vide au grand groupe ; `itertools.permutations(range(n))` donne les $n!$ ordres d'arrivée, des tuples, à réserver aux petits jeux ; une table de valeurs indexée par des `frozenset` se passe comme jeu sous la forme `lambda S: t[S]` |
| une corrélation de rangs de Spearman | `scipy.stats.spearmanr(x, y).statistic` ; avec des ex aequo, c'est la corrélation de Pearson des rangs moyens de `scipy.stats.rankdata` ; pour un échantillon constant, un `ConstantInputWarning` et `nan` |
| agrandir un profil par interpolation linéaire | `scipy.ndimage.zoom(a, H / h, order=1)` aligne les coins (`grid_mode=False`, par défaut : le premier et le dernier centre restent en place) ; `scipy.ndimage.zoom(a, H / h, order=1, grid_mode=True, mode="nearest")` aligne les centres (les bords coïncident) ; `order=3`, le réglage par défaut, interpole par des polynômes de degré 3, pas linéairement ; sur un tableau à deux dimensions, l'interpolation est bilinéaire |

Dans `mymath/attribution.py`, la docstring du module dit ce qui est permis : NumPy et les modules `math`, `fractions` et `itertools`, mais ni SciPy (`spearmanr`, `rankdata`, `pearsonr`, `scipy.integrate`), ni `np.corrcoef`, ni `np.cov`, ni le module `statistics`, ni pandas : les tests comparent tes résultats aux leurs ; les imports relatifs de tes propres modules sont permis (`from .integrate import simpson`, M02a). Un jeu est une fonction qui reçoit un `frozenset`, et une fonction ne modifie jamais les tableaux qu'elle reçoit. Les poids des coalitions, les dividendes, la règle de Simpson et les rangs moyens sont dans la fiche (§1, §2, §4 et §6) ; les coder est le travail des 🔨 MB6.13 à MB6.16.

## Lois données par leur taux, log-sum-exp pondéré (MB8)

Un paramètre `theta` de loi ; des gains `r` et une loi de référence `pi_ref` de même longueur ; un `beta > 0`.

| Je veux… | Code |
|---|---|
| tirer une loi exponentielle de taux $\theta$ | `rng.exponential(scale=1/theta, size=n)` : NumPy prend l'**échelle**, la moyenne $\frac1\theta$, et non le taux (`rng.exponential(theta)` tirerait la loi de moyenne $\theta$) ; de même `scipy.stats.expon(scale=1/theta)` ; la densité en `x` : `theta * np.exp(-theta * x)` |
| tirer une loi de Poisson, une binomiale, une normale | `rng.poisson(theta, size=n)` (de moyenne `theta`), `rng.binomial(m, theta, size=n)` (`m` essais de probabilité `theta`), `rng.normal(mu, sigma, size=n)` (le second argument est l'**écart-type**) |
| $\beta\ln\sum_x\pi_{\mathrm{ref}}(x)\,e^{r(x)/\beta}$, sans débordement | `beta * scipy.special.logsumexp(r / beta, b=pi_ref)` : l'argument `b` multiplie chaque exponentielle ; une issue où `pi_ref` vaut 0 ne compte pas, même si son `r` est très grand |

Dans `mymath/policy_gradient.py`, la docstring du module dit ce qui est permis : NumPy et le module `math`, de `np.linalg` seulement `solve` et `matrix_rank` (dans `policy_gradient_exact`), et ni SciPy ni scikit-learn (`scipy.optimize`, `scipy.special`, `sklearn.linear_model`) : les tests comparent tes résultats à des sommes exactes, à des différences finies de valeurs calculées par `np.linalg.solve`, à `scipy.optimize.minimize` et à scikit-learn ; l'import relatif de ta fonction de M26 est permis (`from .markov import bellman_linear_solve`). Rien n'y tire au hasard : les fonctions reçoivent des valeurs calculées à partir de tirages faits ailleurs, et ne modifient jamais les tableaux qu'elles reçoivent. L'estimateur score, le gradient de la valeur, les poids d'importance et l'algorithme de Zermelo sont dans la fiche (§2, §3, §4, §6 et §7) ; les coder est le travail des 🔨 MB8.13 à MB8.16.

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
