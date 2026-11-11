# M14 · Les maths des ensembles — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M14.Q1 — La queue d'une loi binomiale et ses bornes : vrai ou faux

<details><summary>Indice 1</summary>

Relis le §1 de la fiche : « Au moins $k$ sur $n$ » et « Majorer la queue : trois bornes ».

</details>
<details><summary>Indice 2</summary>

« Au moins $k$ » est le contraire de « au plus $k - 1$ ». Regarde de quoi dépend chaque borne.

</details>
<details><summary>Indice 3</summary>

3 : l'inégalité de Pinsker. 4 : que vaut la proportion de succès en moyenne ? 5 : $e^{-2n\,\mathrm{KL}}$, c'est quoi par rapport à $e^{-n\,\mathrm{KL}}$ ? 6 : calcule les deux (R1).

</details>

### M14.Q2 — Corrélation et variance d'une moyenne

<details><summary>Indice 1</summary>

Relis « La formule » (fiche §2).

</details>
<details><summary>Indice 2</summary>

$\mathbb{V}(X + Y) = \mathbb{V}(X) + \mathbb{V}(Y) + 2\operatorname{Cov}(X, Y)$ ; les poids sortent **au carré** d'une variance.

</details>
<details><summary>Indice 3</summary>

5 : écris la moyenne comme $\frac{2X_1 + X_2}{3}$. 6 : relis « Une borne générale » (fiche §2).

</details>

### M14.Q3 — Des limites remarquables

<details><summary>Indice 1</summary>

Relis le §3 de la fiche.

</details>
<details><summary>Indice 2</summary>

Écris chaque suite sous la forme $\exp\big(\text{exposant} \times \ln(1 + \text{petit})\big)$, puis $\ln(1 + u) \approx u$.

</details>
<details><summary>Indice 3</summary>

3 : $\left(1 + \frac1n\right)^{2n} = \left(\left(1 + \frac1n\right)^n\right)^2$. 4 : l'exposant vaut environ $\frac{5}{n}$. 6 : l'erreur relative vaut environ $-\frac{x^2}{2n}$.

</details>

### M14.Q4 — Des poids exponentiels

<details><summary>Indice 1</summary>

Relis « Les poids exponentiels » et « Le calcul en pratique » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$e^{-L\ln 5} = 5^{-L}$. Un facteur commun à tous les poids disparaît à la normalisation.

</details>
<details><summary>Indice 3</summary>

3 : regarde $e^{-\eta(L_k - \min_j L_j)}$ quand $\eta \to 0$ et quand $\eta \to +\infty$. 6 : ta loss d'un tour est une moyenne des losses des experts.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M14.R1 — La log-loss et la divergence KL (M13a, M06)

<details><summary>Indice 1</summary>

Relis la définition de $\mathrm{KL}(a \Vert p)$ (fiche §1), et M13a §2 pour la log-loss.

</details>
<details><summary>Indice 2</summary>

Logarithme népérien : le résultat est en nats.

</details>
<details><summary>Indice 3</summary>

3 : $-\big(0{,}1\ln 0{,}25 + 0{,}9\ln 0{,}75\big)$. 4 : $H(0{,}1) = -\big(0{,}1\ln 0{,}1 + 0{,}9\ln 0{,}9\big)$, et compare la différence à la question 2.

</details>

### M14.R2 — La variance d'une somme et la matrice de covariance (M02c)

<details><summary>Indice 1</summary>

Relis M02c (variance d'une somme, matrice de covariance).

</details>
<details><summary>Indice 2</summary>

La covariance est bilinéaire et symétrique.

</details>
<details><summary>Indice 3</summary>

3 : $\operatorname{Cov}(X + Y, X - Y) = \mathbb{V}(X) - \operatorname{Cov}(X, Y) + \operatorname{Cov}(Y, X) - \mathbb{V}(Y)$. 4 : $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ est la variance de quoi ?

</details>

### M14.R3 — Taylor et ln(1 + u) (M05a)

<details><summary>Indice 1</summary>

Relis M05a (le développement de $\ln(1 + u)$).

</details>
<details><summary>Indice 2</summary>

$u = -0{,}03$.

</details>
<details><summary>Indice 3</summary>

2 : pour $u < 0$, regarde le signe de chacun des termes suivants, $\frac{u^3}{3}$, $-\frac{u^4}{4}$…

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M14.1 — La fiabilité d'un système « k parmi n » : au moins k composants qui marchent

<details><summary>Indice 1</summary>

Relis l'exemple « $k$ parmi $n$ » et « Majorer la queue : trois bornes » (fiche §1).

</details>
<details><summary>Indice 2</summary>

a) trois termes, $j = 7$, 8 et 9. $F = 9 - X$ compte les pannes : de quelle loi ? Les bornes portent sur $P(F \ge 9a)$ : que valent $a$ et $p$ ?

</details>
<details><summary>Indice 3</summary>

$a = \frac{1}{3}$ et $p = 0{,}1$ ; $\mathrm{KL}\left(\frac{1}{3} \Vert 0{,}1\right) = \frac{1}{3}\ln\frac{10}{3} + \frac{2}{3}\ln\frac{20}{27}$ ; Markov : $\frac{\mathbb{E}[F]}{3}$. h) `binom.sf(9, 12, 0.9)` pour vérifier.

</details>

### Ex M14.2 — La variance de la moyenne de trois mesures corrélées, par la matrice de covariance

<details><summary>Indice 1</summary>

Relis l'exemple des trois capteurs et « Les meilleurs poids » (fiche §2).

</details>
<details><summary>Indice 2</summary>

a) $\frac{1}{9}$ fois la somme des neuf cases. d) Résous $\boldsymbol{\Sigma}\mathbf{v} = \mathbf{1}$, puis divise $\mathbf{v}$ par la somme de ses coordonnées.

</details>
<details><summary>Indice 3</summary>

Essaie $\mathbf{v}$ proportionnel à $(6, 3, 10)$ : calcule $\boldsymbol{\Sigma}\,(6, 3, 10)^\top$.

</details>

### Ex M14.3 — (1 + x/n)ⁿ pour quelques n, et des intérêts composés en continu

<details><summary>Indice 1</summary>

Relis « La vitesse » et « Des intérêts composés en continu » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\left(1 + \frac{0{,}065}{m}\right)^{6m} = \left(1 + \frac{x}{N}\right)^N$ : que valent $x$ et $N$ ?

</details>
<details><summary>Indice 3</summary>

$x = 0{,}39$ et $N = 6m$ : $N = 6$, 24, 312. f) $-\frac{0{,}39^2}{48}$. h) $\frac{9}{2n} < 0{,}008$.

</details>

### Ex M14.4 — Les poids exponentiels de cinq experts après trois tours

<details><summary>Indice 1</summary>

Relis « Les poids exponentiels » et l'exemple (fiche §4).

</details>
<details><summary>Indice 2</summary>

Avant chaque tour : les losses cumulées des tours **précédents**, puis $3^{-L}$, puis la normalisation.

</details>
<details><summary>Indice 3</summary>

Avant le tour 3, les losses cumulées valent $(1, 1, 2, 0, 1)$ : multiplie $3^{-L}$ par 9 pour avoir des entiers. d) $\frac{3}{5} + \frac{4}{9} + \frac{12}{19}$.

</details>

### Ex M14.5 — Le gradient de la loss exponentielle e^(−yF) et de la loss de Huber par rapport aux prédictions, et les poids exponentiels qu'il fait apparaître

<details><summary>Indice 1</summary>

Relis le §5 de la fiche (ses deux exemples).

</details>
<details><summary>Indice 2</summary>

La coordonnée $i$ du gradient est $-y_i\,e^{-y_iF_i}$ ; pour Huber, $-\operatorname{clip}(y_i - F_i, -\delta, \delta)$.

</details>
<details><summary>Indice 3</summary>

Les losses : $e^{-2}$, $e^{0{,}5}$, $e^{-1{,}5}$, $e^{0{,}3}$, $e^0$. Les résidus : $(0{,}5 ;\ -1{,}1 ;\ -0{,}3 ;\ 2{,}7)$ ; au-delà de $\delta$, la loss vaut $\delta\left(\lvert r \rvert - \frac{\delta}{2}\right)$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M14.6 — (1 + x/n)ⁿ → eˣ, par le logarithme et ln(1 + u) ≈ u

<details><summary>Indice 1</summary>

Relis « L'idée » et « La vitesse » (fiche §3), et CP1.10 B pour $e^v \ge 1 + v$.

</details>
<details><summary>Indice 2</summary>

1 et 2 : une différence nulle en $u = 0$ ; étudie le signe de sa dérivée sur l'intervalle. 3 : $\lvert u \rvert < \frac{1}{2}$, puis multiplie par $n$.

</details>
<details><summary>Indice 3</summary>

1 : la dérivée vaut $\frac{u^2}{1 + u}$. 2 : $\frac{u(1 + 2u)}{1 + u}$. 4 : $\frac{(1 + x/n)^n}{e^x} = \exp\left(n\ln\left(1 + \frac{x}{n}\right) - x\right)$. 5 : $\ln(1 + u) \le u$ avec $u = -\frac{v}{1 + v}$ donne $\ln(1 + v) \ge \frac{v}{1 + v}$.

</details>

### Ex M14.7 — Une moyenne pondérée de variables de variance σ² a une variance au plus σ²

<details><summary>Indice 1</summary>

Relis « Une borne générale » (fiche §2), et ∂ M07.14 pour Cauchy-Schwarz.

</details>
<details><summary>Indice 2</summary>

1 : relis la preuve de M07.14 en remplaçant le produit scalaire par la covariance ; où sert l'hypothèse « vecteur non nul » ? 3 : développe la variance en double somme.

</details>
<details><summary>Indice 3</summary>

3 : $w_iw_j \ge 0$ permet de majorer chaque terme : $\sum_{i,j}w_iw_j\sigma_i\sigma_j = \big(\sum_i w_i\sigma_i\big)^2$. 5 : deux variables indépendantes et les poids $(2, -1)$.

</details>

### Ex M14.8 — La borne de Chernoff d'une queue binomiale : le meilleur λ donne exp(−n KL(a ‖ p))

<details><summary>Indice 1</summary>

Relis « D'où vient la borne de Chernoff » (fiche §1), et M11 pour Markov.

</details>
<details><summary>Indice 2</summary>

1 : relis CP2.9 B ; seule l'espérance de $e^{\lambda X_i}$ change. 2 : annule $g'$, puis regarde le signe de $g''$. 3 : calcule d'abord $1 - p + pe^{\lambda^*}$.

</details>
<details><summary>Indice 3</summary>

3 : $1 - p + pe^{\lambda^*} = \frac{1 - p}{1 - a}$, puis $\ln\frac{a(1 - p)}{p(1 - a)} = \ln\frac{a}{p} + \ln\frac{1 - p}{1 - a}$. 5 : $f''(a) = \frac{1}{a(1 - a)} - 4$, et $a(1 - a) \le \frac{1}{4}$.

</details>

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M14.9 — Pont : ajouter des modèles très corrélés ne sert presque à rien, un plancher de variance sur deux groupes de modèles

<details><summary>Indice 1</summary>

Relis « Moyenner des prédictions corrélées : un plancher » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Écris la moyenne comme une partie commune plus la moyenne des parts propres ; les deux sont indépendantes.

</details>
<details><summary>Indice 3</summary>

a) $\frac{0{,}7 + 0{,}9 + 2 \times 0{,}3}{4} + \frac{2{,}5}{2m}$. c) divise b) par a). e) Avec une proportion $\alpha$ de modèles A, le plancher vaut $\mathbb{V}\big(\alpha Z_A + (1 - \alpha)Z_B\big)$ ; dérive en $\alpha$. h) Poids $\frac{100}{110}$ et $\frac{10}{110}$, plus $\frac{2{,}5}{110}$.

</details>

### Ex M14.10 — Expliquer pourquoi une moyenne réduit la variance, et quand elle ne la réduit plus

<details><summary>Indice 1</summary>

Relis le §2 de la fiche, sa figure et son modèle à part commune.

</details>
<details><summary>Indice 2</summary>

Sépare l'erreur d'un thermomètre en deux parts : celle qui lui est propre, celle qu'il partage avec les autres.

</details>
<details><summary>Indice 3</summary>

Un exemple concret de part partagée : le même étalonnage d'usine, le même emplacement. Puis : des appareils différents, des erreurs de sens opposés, des poids.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M14.E1 — « Comment combiner les avis de plusieurs experts quand on ne sait pas lequel est le meilleur ? »

<details><summary>Indice 1</summary>

Relis le §4 de la fiche.

</details>
<details><summary>Indice 2</summary>

Le cadre, l'échec de « suivre le meneur », les poids $e^{-\eta L}$, le regret.

</details>
<details><summary>Indice 3</summary>

La borne $\sqrt{T\ln K/2}$, $\eta_t = \sqrt{8\ln K/t}$ sans horizon, la différence avec un bandit (M11), un usage, et Freund et Schapire (1997) en une phrase.

</details>

<a id="notebook"></a>

## Notebook

### Ex M14.11 — La borne de Chernoff et la variance d'une moyenne pondérée · `chernoff_bound, variance_of_average`

<details><summary>Indice 1</summary>

Relis « Majorer la queue : trois bornes » (fiche §1) et « La formule » (fiche §2), puis les deux docstrings.

</details>
<details><summary>Indice 2</summary>

`chernoff_bound` : les contrôles d'abord ($n$ entier, pas un booléen ; $p$ et $a$ dans $[0, 1]$), puis les cas $a \le p$ (1.0) et $p = 0$ (0.0), puis la KL, en n'ajoutant le terme $(1 - a)\ln\frac{1 - a}{1 - p}$ que si $a < 1$. `variance_of_average` : une matrice carrée et symétrique (à un arrondi près), des poids positifs de somme 1, `1 / M` par défaut.

</details>
<details><summary>Indice 3</summary>

La KL : `a * math.log(a / p) + (1 - a) * math.log((1 - a) / (1 - p))`, puis `math.exp(-n * kl)`. La variance : `float(w @ c @ w)`. Pour la symétrie, `np.allclose(c, c.T)` avec une tolérance relative à la taille des coefficients.

</details>

### Ex M14.12 — Les poids de l'algorithme Hedge · `hedge_weights`

<details><summary>Indice 1</summary>

Relis « Les poids exponentiels » et « Le calcul en pratique » (fiche §4), puis la docstring.

</details>
<details><summary>Indice 2</summary>

Les losses cumulées avant chaque tour : une ligne de zéros, puis `np.cumsum(losses, axis=0)` ; cela fait $T + 1$ lignes. Retranche le minimum de chaque ligne (`keepdims=True`) avant l'exponentielle.

</details>
<details><summary>Indice 3</summary>

`w = np.exp(-eta * shifted)` puis `w / w.sum(axis=1, keepdims=True)`. d) La loss de l'algorithme utilise les lignes 0 à $T - 1$ (les poids **avant** chaque tour) : `np.sum(W[:-1] * losses)`.

</details>

### Ex M14.13 — Simuler la moyenne de deux groupes de modèles corrélés, et retrouver aᵀΣa et son plancher

<details><summary>Indice 1</summary>

Relis « Moyenner des prédictions corrélées : un plancher » (fiche §2) et ta solution de 🔗 M14.9.

</details>
<details><summary>Indice 2</summary>

Une seule paire $(Z_A, Z_B)$ par tirage : `rng.multivariate_normal(np.zeros(2), COV_Z_13, size=n_draws)`, un tableau `n_draws × 2`, puis `rng.normal(0, np.sqrt(2.2), size=(n_draws, 2 * m))` pour les parts propres (le second argument de `rng.normal` est un écart-type, pas une variance).

</details>
<details><summary>Indice 3</summary>

Erreurs du groupe A : `Z[:, [0]] + E[:, :m]` ; du groupe B : `Z[:, [1]] + E[:, m:]`. La matrice $2m \times 2m$ : un bloc rempli de $0{,}6$, un de $1{,}4$, deux de $0{,}5$ (`np.block` avec `np.full`), plus $2{,}2$ sur la diagonale (`np.eye`). b) $\frac{0{,}6 + 1{,}4 + 2 \times 0{,}5}{4}$.

</details>

### Ex M14.14 — Les poids exponentiels au fil des tours : quel expert domine, selon le learning rate

<details><summary>Indice 1</summary>

Relis le §4 de la fiche et sa figure des poids.

</details>
<details><summary>Indice 2</summary>

Calcule une fois `W = hedge_weights(losses, eta)` par axe : un tableau $81 \times 5$ ; une courbe par colonne, `ax.plot(np.arange(81), W[:, k], label=...)`, ou toutes ensemble avec `ax.stackplot(np.arange(81), W.T)`.

</details>
<details><summary>Indice 3</summary>

N'appelle ni `plt.figure` ni `plt.subplots` : dessine dans les `axes` reçus, avec `zip(axes, etas)`. Un titre comme `f"η = {eta}"`, puis `ax.legend()` et `ax.set(xlabel=..., ylabel=...)`.

</details>

### Ex M14.15 — Chasse à l'erreur : P(X ≥ k) calculée comme P(X > k), des covariances oubliées, des poids non renormalisés

<details><summary>Indice 1</summary>

Relis les pièges classiques de la fiche : $P(X \ge k)$, le sens de la divergence, les covariances oubliées, la normalisation.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, compare ce que calcule le code à ce que dit son commentaire : que rend `binom.sf(m, n, p)` ? dans quel ordre `kl_15` attend-il ses arguments ? que manque-t-il à `np.mean(np.diag(S_15))` ? une loi sur les experts somme-t-elle à 1 ?

</details>
<details><summary>Indice 3</summary>

Quatre lignes fausses. Les lignes qui ressemblent à une erreur sans en être une : une queue avec `k - 1` écrite autrement, `w @ S @ w`, et la soustraction du minimum, qui ne change pas les poids une fois normalisés.

</details>

### Ex M14.16 — Un test qui vérifie que la borne de Chernoff majore la queue exacte de `scipy.stats`, sur une grille de n, p et a

<details><summary>Indice 1</summary>

Relis « Majorer la queue : trois bornes » et « Chernoff contre Hoeffding » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Une grille par compréhension : `for n in (...) for p in (...) for a in (...)`, avec $a = 1$, des $p$ comme 0,01 et 0,99, des $n$ de 1 à quelques centaines. La queue exacte : `k = math.ceil(n * a - 1e-9)`, puis `binom.sf(k - 1, n, p)`.

</details>
<details><summary>Indice 3</summary>

Quatre `assert` par cas, chacun avec un message `f"n={n}, p={p}, a={a}"` : `0 <= b <= 1 + 1e-12` ; `b >= tail - 1e-12` ; si $a > p$, `b <= math.exp(-2 * n * (a - p) ** 2) + 1e-12` ; si $a > p$, `bound(2 * n, p, a) <= b + 1e-12`. Ce sont les cas extrêmes qui attrapent les fausses bornes : $a = 1$ (`bound_reversed`), $a = 0$ (`bound_fixed_lambda` dépasse 1), $a > p$ avec de petits $n$ (`bound_squared`), de grands $n$ ou un $p$ près de 0 (`bound_markov`, au-dessus de Hoeffding).

</details>

### Ex M14.17 — Défi : suivre le meilleur de dix experts avec Hedge sans connaître l'horizon, un regret sous la borne théorique sur 1 000 tours

<details><summary>Indice 1</summary>

Relis « Choisir η » et « Sans connaître T » (fiche §4), puis essaie les trois stratégies proposées et regarde où elles échouent.

</details>
<details><summary>Indice 2</summary>

Un $\eta$ constant fait un compromis pour **un** horizon : petit, il apprend trop lentement au début ; grand, il suit les à-coups ensuite. Il faut un $\eta$ qui dépend du tour : grand au début, de plus en plus petit.

</details>
<details><summary>Indice 3</summary>

Garde les losses cumulées $L$ et le numéro $t$ du tour qui vient (1 avant le premier tour) ; `weights()` rend `softmax` de $-\eta_t(L - \min L)$ avec $\eta_t = \sqrt{8\ln K/t}$, écrit avec `np.exp` ; `update` ajoute les losses à $L$ et incrémente $t$. Le η constant réglé pour $T = 1\,000$ paie $\frac{\ln K}{\eta} \approx 17$ dès le départ : trop pour la borne du tour 50.

</details>
