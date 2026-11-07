# M02c · Échantillons et estimation — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M02c.Q1 — Résumer une série : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Position : moyenne et médiane » et « Dispersion : variance et écart-type » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Teste chaque affirmation sur une toute petite série, comme $1, 2, 3, 10$.

</details>
<details><summary>Indice 3</summary>

1 : la médiane de $1, 2, 3, 10$. 2 et 3 : la transformation affine du §1. 6 : où sont $Q_1$ et $Q_3$ par rapport au minimum et au maximum ?

</details>

### M02c.Q2 — z-scores et valeurs aberrantes

<details><summary>Indice 1</summary>

Relis le §2 en entier.

</details>
<details><summary>Indice 2</summary>

Le z-score compte des écarts-types. Les barrières de Tukey sont à $1{,}5\,\text{EI}$ des quartiles.

</details>
<details><summary>Indice 3</summary>

4 : la borne admise au §2, $\lvert z \rvert \le \sqrt{n - 1}$. 5 : l'effet de masque.

</details>

### M02c.Q3 — i.i.d. ou pas ?

<details><summary>Indice 1</summary>

Relis « Le modèle : un échantillon » et les deux sous-sections sur les tirages (fiche §3).

</details>
<details><summary>Indice 2</summary>

Pose deux questions : connaître une valeur renseigne-t-il sur une autre (indépendance) ? Chaque valeur vient-elle de la même loi ?

</details>
<details><summary>Indice 3</summary>

4 : calcule le facteur $\frac{N - n}{N - 1}$. 6 : la fin du §3 et son ⚠️.

</details>

### M02c.Q4 — Grands nombres et TCL : ce qu'ils disent, ce qu'ils ne disent pas

<details><summary>Indice 1</summary>

Relis les ⚠️ des §4 et §5.

</details>
<details><summary>Indice 2</summary>

L'écart-type de la moyenne vaut $\frac{\sigma}{\sqrt{n}}$. Le théorème central limite porte sur la moyenne, pas sur les tirages.

</details>
<details><summary>Indice 3</summary>

2 : $\sqrt{\frac{10\,000}{100}}$. 5 : Bienaymé-Tchebychev avec $\varepsilon = 2\sigma$. 6 : l'hypothèse indispensable du §4.

</details>

### M02c.Q5 — Biais, variance et ddof

<details><summary>Indice 1</summary>

Relis le §6, en particulier la décomposition de l'erreur quadratique et « Sans biais ne veut pas dire meilleur ».

</details>
<details><summary>Indice 2</summary>

$\text{EQM} = \text{biais}^2 + \text{variance}$ ; $s^2 = \frac{n}{n - 1}s_n^2$.

</details>
<details><summary>Indice 3</summary>

1 : « en moyenne sur tous les échantillons ». 4 : $\frac{n}{n - 1}$ avec $n = 4$.

</details>

### M02c.Q6 — Lire un intervalle de confiance

<details><summary>Indice 1</summary>

Relis « Comment le lire » (fiche §7).

</details>
<details><summary>Indice 2</summary>

L'intervalle est $\bar{x} \pm 1{,}96\,\text{SE}$ : son centre est la moyenne, sa demi-largeur $1{,}96$ erreurs types.

</details>
<details><summary>Indice 3</summary>

4 : demi-largeur $\frac{13{,}5 - 12{,}1}{2} = 0{,}7$. 5 : la largeur varie en $\frac{1}{\sqrt{n}}$.

</details>

### M02c.Q7 — Covariance et corrélation : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Les règles de calcul » et « La corrélation » (fiche §8).

</details>
<details><summary>Indice 2</summary>

La force d'une relation linéaire se lit sur $\lvert r \rvert$. Une variance d'une différence ajoute les variances.

</details>
<details><summary>Indice 3</summary>

5 : quelle troisième grandeur fait grandir les pieds et progresser en lecture ? 6 : la diagonale, puis les cases au-dessus de la diagonale.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M02c.R1 — Espérance et variance d'une somme (M02b)

<details><summary>Indice 1</summary>

Relis M02b §6 (linéarité, variance d'une somme).

</details>
<details><summary>Indice 2</summary>

Pour des variables indépendantes, les variances s'additionnent, même pour une différence. Un facteur compte au carré.

</details>
<details><summary>Indice 3</summary>

4 : $\mathbb{V}(\bar{X}) = \frac{\sigma^2}{n}$.

</details>

### M02c.R2 — Loi normale et fonction Φ (M02b)

<details><summary>Indice 1</summary>

Relis la table de $\Phi$ et « Standardiser » (M02b §3).

</details>
<details><summary>Indice 2</summary>

$P(-z \le Z \le z) = 2\Phi(z) - 1$ ; $P(Z > z) = 1 - \Phi(z)$.

</details>
<details><summary>Indice 3</summary>

3 : $z = \frac{89 - 80}{6}$. 4 : cherche $\Phi(z) = 0{,}95$ dans la table.

</details>

### M02c.R3 — Racines et puissances (R1)

<details><summary>Indice 1</summary>

Relis les racines carrées de R1.

</details>
<details><summary>Indice 2</summary>

$\sqrt{ab} = \sqrt{a}\sqrt{b}$ et $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$.

</details>
<details><summary>Indice 3</summary>

1 : $0{,}0144 = \frac{144}{10\,000}$. 5 : isole $\sqrt{n}$, puis élève au carré.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M02c.1 — Les statistiques d'une petite série : moyenne, médiane, quartiles, variance

<details><summary>Indice 1</summary>

Relis le §1, dans l'ordre : moyenne, médiane, variance, quantiles.

</details>
<details><summary>Indice 2</summary>

Commence par **trier** la série et numéroter les valeurs de 0 à 7. Pour la variance, écris le tableau des écarts à la moyenne et de leurs carrés.

</details>
<details><summary>Indice 3</summary>

f : position $0{,}25 \times 7 = 1{,}75$, donc entre les valeurs n° 1 et n° 2, aux trois quarts du chemin. g : position $0{,}75 \times 7 = 5{,}25$.

</details>

### Ex M02c.2 — z-scores, écart interquartile et valeurs aberrantes

<details><summary>Indice 1</summary>

Relis le §2, et l'exemple des neuf durées.

</details>
<details><summary>Indice 2</summary>

b : le tableau des écarts à 15,7 et de leurs carrés, puis la division par 10. e et f : trie la série (10 valeurs, positions 0 à 9).

</details>
<details><summary>Indice 3</summary>

f : $Q_3$ est à la position 6,75, entre deux valeurs égales. h : la moyenne des 9 autres vaut 14 ; leurs écarts sont petits.

</details>

### Ex M02c.3 — Imputer par la moyenne ou la médiane : ce qui change

<details><summary>Indice 1</summary>

Relis « Valeurs manquantes » (fiche §9).

</details>
<details><summary>Indice 2</summary>

Une valeur imputée par la moyenne a un écart nul à la moyenne : elle ne change pas la somme des carrés des écarts, seulement le nombre par lequel on divise.

</details>
<details><summary>Indice 3</summary>

e : la somme des carrés de c), divisée par 8. f : $\sqrt{\frac{m}{n}}$. h : trie les 8 valeurs, les deux 8 compris.

</details>

### Ex M02c.4 — Avec ou sans remise : la variance de la moyenne

<details><summary>Indice 1</summary>

Relis « Avec remise » et « Sans remise » (fiche §3), et l'encadré des tirages sans remise.

</details>
<details><summary>Indice 2</summary>

La population a $N = 5$ valeurs ; sa variance divise par $N$. Sans remise : $\mathbb{V}(\bar{X}) = \frac{\sigma^2}{n}\cdot\frac{N - n}{N - 1}$ et $\operatorname{Cov}(X_1, X_2) = -\frac{\sigma^2}{N - 1}$.

</details>
<details><summary>Indice 3</summary>

c : $\binom{5}{2}$. Vérification de e : écris les 10 paires et la moyenne de chacune, puis la variance de ces 10 moyennes.

</details>

### Ex M02c.5 — Combien d'observations pour une moyenne précise à 1 % ?

<details><summary>Indice 1</summary>

Relis « Quelle taille d'échantillon ? » (fiche §7) et l'exemple de Monte-Carlo du §4.

</details>
<details><summary>Indice 2</summary>

Demi-largeur à 95 % : $1{,}96\,\frac{\sigma}{\sqrt{n}}$. Bienaymé-Tchebychev pour la moyenne : $P(\lvert \bar{X} - \mu \rvert \ge \varepsilon) \le \frac{\sigma^2}{n\varepsilon^2}$.

</details>
<details><summary>Indice 3</summary>

c : $1{,}96 \times \frac{2}{\sqrt{n}} \le 0{,}5$ donne $\sqrt{n} \ge 7{,}84$, puis arrondis au-dessus. e : $\frac{4}{0{,}25\,n} \le 0{,}05$.

</details>

### Ex M02c.6 — Le théorème central limite à la main : une somme de 100 variables

<details><summary>Indice 1</summary>

Relis l'exemple des 64 fichiers (fiche §5).

</details>
<details><summary>Indice 2</summary>

Calcule d'abord $\mathbb{E}[X]$ et $\mathbb{E}[X^2]$, puis $\mathbb{V}(X)$. La somme $S$ a pour espérance $100\,\mathbb{E}[X]$ et pour variance $100\,\mathbb{V}(X)$ ; standardise avec son écart-type.

</details>
<details><summary>Indice 3</summary>

e : $z = \frac{49 - 30}{19}$. h : $P(S_n > 0) \approx \Phi\big(\frac{0{,}3\,n}{1{,}9\sqrt{n}}\big)$ ; résous $\frac{0{,}3\sqrt{n}}{1{,}9} \ge 1{,}96$.

</details>

### Ex M02c.7 — Biais, variance et erreur quadratique de trois estimateurs

<details><summary>Indice 1</summary>

Relis « Estimer un paramètre » et la décomposition de l'erreur quadratique (fiche §6).

</details>
<details><summary>Indice 2</summary>

Par linéarité, $\mathbb{E}[T_3] = \frac{3\mu}{4}$ ; par M02b §6, $\mathbb{V}\big(\frac{X_1 + X_2 + X_3}{4}\big) = \frac{3\sigma^2}{16}$.

</details>
<details><summary>Indice 3</summary>

d : $\text{biais}^2 + \text{variance}$, avec le biais de a). h : écris $\text{EQM}(T_3) = \frac{\mu^2}{16} + \frac{27}{16}$ et compare-la à 3.

</details>

### Ex M02c.8 — Erreur type et intervalle de confiance d'une moyenne

<details><summary>Indice 1</summary>

Relis « L'erreur type », « L'intervalle de confiance » et « L'erreur type d'un score » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\text{SE} = \frac{s}{\sqrt{n}}$ ; intervalle $\bar{x} \pm z\,\text{SE}$, avec $z = 1{,}96$ à 95 % et $1{,}645$ à 90 %. Pour une accuracy : $\sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$.

</details>
<details><summary>Indice 3</summary>

e : $1{,}96 \times \frac{14}{\sqrt{n}} \le 2$. f : $\hat{p} = \frac{360}{400}$.

</details>

### Ex M02c.9 — La variance d'une somme et la covariance : V(X + Y), V(X − Y)

<details><summary>Indice 1</summary>

Relis « Les règles de calcul » et l'exemple des quatre points (fiche §8).

</details>
<details><summary>Indice 2</summary>

$\mathbb{V}(aX + bY) = a^2\mathbb{V}(X) + b^2\mathbb{V}(Y) + 2ab\operatorname{Cov}(X, Y)$ ; $\rho = \frac{\operatorname{Cov}}{\sigma_X\sigma_Y}$.

</details>
<details><summary>Indice 3</summary>

e : les constantes ajoutées disparaissent. f : un tableau avec les écarts de $x$, ceux de $y$ et leurs produits. h : calcule les 4 sommes $x_i + y_i$, ou utilise la formule de la variance d'une somme.

</details>

### Ex M02c.10 — La matrice de covariance de trois variables : la lire et la vérifier

<details><summary>Indice 1</summary>

Relis « La matrice de covariance » (fiche §8).

</details>
<details><summary>Indice 2</summary>

La case $(i, j)$ contient $\operatorname{Cov}(X_i, X_j)$ ; la diagonale, les variances. $\mathbb{V}\big(\sum w_iX_i\big) = \sum_i\sum_j w_iw_j\Sigma_{ij}$.

</details>
<details><summary>Indice 3</summary>

e : tous les $w_i$ valent 1 : la somme de toutes les cases. g : pour chaque tableau, la symétrie, puis la corrélation de la case hors diagonale. h : la diagonale donne $w_i^2\Sigma_{ii}$, chaque paire $i \ne j$ apparaît deux fois.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M02c.11 — Pourquoi diviser par n − 1 : E[S²] = σ²

<details><summary>Indice 1</summary>

Relis la démonstration de l'identité du §1, puis « La variance de l'échantillon et le ddof » (fiche §6).

</details>
<details><summary>Indice 2</summary>

1 : écris $X_i - \mu = (X_i - \bar{X}) + (\bar{X} - \mu)$ et développe. 2 : la première espérance est une variance ; la seconde est $\mathbb{V}(\bar{X})$.

</details>
<details><summary>Indice 3</summary>

3 : prends l'espérance des deux membres de l'identité : $n\sigma^2 - n \times \frac{\sigma^2}{n}$. 6 : quelle formule de la question 2 demande l'indépendance ?

</details>

### Ex M02c.12 — La variance de la moyenne : V(X̄) = σ²/n, et l'erreur type

<details><summary>Indice 1</summary>

Relis la fin du §3 et « Les règles de calcul » (fiche §8).

</details>
<details><summary>Indice 2</summary>

2 : sors le facteur $\frac{1}{n}$ (au carré), puis utilise la variance d'une somme de variables indépendantes. 4 : la variance d'une somme est la somme de **toutes** les covariances $\operatorname{Cov}(X_i, X_j)$, $i = j$ compris.

</details>
<details><summary>Indice 3</summary>

4 : il y a $n$ termes $i = j$ (des variances) et $n(n - 1)$ termes $i \ne j$, chacun égal à $\rho\sigma^2$. 6 : remplace $\rho$ et mets $\frac{\sigma^2}{n}$ en facteur.

</details>

<a id="reflexion"></a>

## 🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication

### Ex M02c.13 — Le 99e percentile d'une latence : l'estimer et dire son incertitude

<details><summary>Indice 1</summary>

Relis « Quantiles d'une série » et « Percentiles d'une mesure : la latence » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Position $h = p(n - 1)$ avec $n - 1 = 999$ ; la valeur $x_{(989)}$ est la première de la liste. Le nombre de mesures au-dessus de $q_{0{,}99}$ suit une binomiale.

</details>
<details><summary>Indice 3</summary>

c : position $0{,}999 \times 999 = 998{,}001$. f : $P(T > q) = e^{-q/40} = 0{,}01$. g : $n \times 0{,}001 = 10$.

</details>

### Ex M02c.14 — Standardiser des features avec les statistiques du seul train

<details><summary>Indice 1</summary>

Relis « Standardiser une feature » et son ⚠️ (fiche §2).

</details>
<details><summary>Indice 2</summary>

Calcule la moyenne et l'écart-type ($s_n$) des 5 valeurs d'entraînement, puis $z = \frac{x - \bar{x}}{s_n}$ pour chaque valeur de test.

</details>
<details><summary>Indice 3</summary>

e et f : refais le calcul avec les 7 valeurs ; leur somme des carrés des écarts vaut environ 73,43. g : relis la transformation affine du §1.

</details>

### Ex M02c.15 — MML §6.4 : moyennes et covariances empiriques, en anglais

<details><summary>Indice 1</summary>

Lis le guide de lecture de la fiche, puis MML §6.4.1, §6.4.2 et §6.4.6, crayon en main.

</details>
<details><summary>Indice 2</summary>

Pour la question 3, écris la formule de la covariance empirique du livre avec $D = 1$ : le produit d'un écart par lui-même. Pour la question 4, cherche les mots *inner product*, *length* et *angle*.

</details>
<details><summary>Indice 3</summary>

5 : $\cos\theta = r$, puis $\theta = \arccos(0{,}894)$ (la touche $\cos^{-1}$ de la calculatrice, en degrés). 6 : $\cos 90° = 0$ et $\cos 180° = -1$.

</details>

### Ex M02c.16 — Le biais du survivant : des données qui ne montrent que ceux qui restent

<details><summary>Indice 1</summary>

Relis « Le biais d'échantillonnage » (fiche §9) et l'exemple des avions.

</details>
<details><summary>Indice 2</summary>

Qui manque dans les données, et pourquoi ? Sur quels clients le modèle prendra-t-il ses décisions ?

</details>
<details><summary>Indice 3</summary>

4 : un grand $n$ réduit l'erreur type, pas le biais (§6 et §9). 5 : pour connaître le remboursement de profils autrefois refusés, il faut bien leur accorder des prêts, ou trouver ces données ailleurs.

</details>

### Ex M02c.17 — Expliquer le théorème central limite avec un histogramme

<details><summary>Indice 1</summary>

Relis l'énoncé du théorème et son ⚠️ (fiche §5), et regarde la figure.

</details>
<details><summary>Indice 2</summary>

Distingue l'histogramme des **données** et l'histogramme des **moyennes** de beaucoup d'échantillons.

</details>
<details><summary>Indice 3</summary>

Trois phrases suffisent pour le cœur : ce qui reste fixe (le centre), ce qui rétrécit (la largeur, en $\frac{1}{\sqrt{n}}$), ce qui change de forme. Termine par le lien avec les intervalles de confiance.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M02c.E1 — L'erreur type décroît en 1/√n : qu'est-ce que cela change pour un jeu de test ?

<details><summary>Indice 1</summary>

Relis « L'erreur type d'un score » (fiche §7) et l'exemple de l'accuracy à 0,92.

</details>
<details><summary>Indice 2</summary>

$\sqrt{\frac{0{,}87 \times 0{,}13}{500}}$, puis compare l'écart de 2 points à cette incertitude.

</details>
<details><summary>Indice 3</summary>

Pour la taille : $n = \frac{p(1 - p)}{\text{SE}^2}$. Pour la comparaison : deux modèles évalués sur les mêmes exemples font souvent les mêmes erreurs (fiche §8, la variance d'une différence).

</details>

<a id="notebook"></a>

## Notebook

### Ex M02c.18 — La distribution des moyennes d'échantillons · `sample_means`

<details><summary>Indice 1</summary>

Relis la docstring : un seul générateur, puis `repeats` appels à `draw`, dans l'ordre.

</details>
<details><summary>Indice 2</summary>

`rng = np.random.default_rng(seed)` **avant** la boucle ; dans la boucle, `np.mean(draw(rng, n))`.

</details>
<details><summary>Indice 3</summary>

`np.array([float(np.mean(draw(rng, n))) for _ in range(repeats)], dtype=float)`, après avoir testé `n < 1 or repeats < 1`.

</details>

### Ex M02c.19 — Biais et erreur quadratique d'un estimateur, par simulation · `estimator_bias, estimator_mse`

<details><summary>Indice 1</summary>

Relis « Estimer par simulation » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Écris d'abord une fonction auxiliaire `_estimates(estimator, draw_sample, repeats, seed)` qui renvoie l'array des `repeats` estimations, avec un seul générateur.

</details>
<details><summary>Indice 3</summary>

Biais : `float(np.mean(estimates) - true_value)` ; erreur quadratique : `float(np.mean((estimates - true_value) ** 2))`.

</details>

### Ex M02c.20 — Erreur type et intervalle de confiance · `standard_error, confidence_interval_mean`

<details><summary>Indice 1</summary>

Relis « L'erreur type » et l'encadré de l'intervalle de confiance (fiche §7).

</details>
<details><summary>Indice 2</summary>

La somme des carrés des écarts divisée par $n - \text{ddof}$, la racine, puis la division par $\sqrt{n}$. L'intervalle réutilise `standard_error`.

</details>
<details><summary>Indice 3</summary>

Les cas d'erreur d'abord : `if n <= ddof: raise ValueError(...)` ; `if len(sample) < 2 or z <= 0: raise ValueError(...)`. Renvoie `(m - z * se, m + z * se)`, un tuple de floats.

</details>

### Ex M02c.21 — NumPy et SciPy : `ddof`, `np.percentile`, `scipy.stats.sem`

<details><summary>Indice 1</summary>

Lis `help(np.percentile)` et `help(stats.sem)` : regarde les valeurs par défaut de `ddof` et l'échelle de `q`.

</details>
<details><summary>Indice 2</summary>

`np.percentile` veut un pourcentage (90), `np.quantile` un ordre (0.9). `stats.sem` divise déjà par $\sqrt{n}$.

</details>
<details><summary>Indice 3</summary>

f : `q1, q3 = np.percentile(DATA_21, [25, 75])`, puis compte les valeurs hors de `[q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)]`. h : $\sqrt{\frac{n - 1}{n}}$.

</details>

### Ex M02c.22 — Prédire : l'histogramme des moyennes d'une loi exponentielle quand n grandit

<details><summary>Indice 1</summary>

Relis les §4 et §5 : $\mathbb{E}[\bar{X}_n]$ et $\sigma(\bar{X}_n)$.

</details>
<details><summary>Indice 2</summary>

L'écart-type de la moyenne varie en $\frac{1}{\sqrt{n}}$ ; son espérance ne dépend pas de $n$.

</details>
<details><summary>Indice 3</summary>

c : pour $n = 1$, l'histogramme est celui de la loi elle-même, de densité $e^{-x}$. d : la médiane de la loi exponentielle (M02a §7).

</details>

### Ex M02c.23 — Couverture : 95 % des intervalles contiennent-ils la vraie moyenne ?

<details><summary>Indice 1</summary>

Relis « Comment le lire » (fiche §7) : la couverture est une proportion d'échantillons.

</details>
<details><summary>Indice 2</summary>

Une ligne = un échantillon : `samples.mean(axis=1)` et `samples.std(axis=1, ddof=1)` donnent un array de moyennes et un array d'écarts-types.

</details>
<details><summary>Indice 3</summary>

`half = z * s / math.sqrt(n)` avec `n = samples.shape[1]`, puis `np.mean((means - half <= true_mean) & (true_mean <= means + half))`.

</details>

### Ex M02c.24 — Grande dimension : le cube dont le centre est vide

<details><summary>Indice 1</summary>

Relis « La grande dimension : premières surprises » (fiche §9).

</details>
<details><summary>Indice 2</summary>

Dans la boule : `np.sum(points ** 2, axis=1) <= 1`. Près du bord : `np.max(np.abs(points), axis=1) > 1 - eps`. La proportion : `np.mean` d'un array de booléens.

</details>
<details><summary>Indice 3</summary>

e : `math.pi ** (d / 2) / math.gamma(d / 2 + 1) / 2 ** d`. f : `int(np.sum(...))` au lieu de `np.mean`.

</details>

### Ex M02c.25 — Voir le théorème central limite : histogrammes et densité normale

<details><summary>Indice 1</summary>

Relis l'énoncé du théorème (fiche §5) : la loi approchée de la moyenne est $\mathcal{N}\big(\mu, \frac{\sigma^2}{n}\big)$.

</details>
<details><summary>Indice 2</summary>

Pour chaque `ax, n` de `zip(axes, ns)` : les moyennes avec `sample_means`, `ax.hist(..., density=True)`, puis la densité normale d'écart-type `sigma / math.sqrt(n)` sur une grille.

</details>
<details><summary>Indice 3</summary>

`grid = np.linspace(mu - 4 * w, mu + 4 * w, 300)` avec `w = sigma / math.sqrt(n)`, puis `ax.plot(grid, stats.norm(mu, w).pdf(grid))` et `ax.set_title(f"n = {n}")`.

</details>

### Ex M02c.26 — Chasse à l'erreur : un intervalle de confiance mal calculé

<details><summary>Indice 1</summary>

Relis l'⚠️ du §7 et le tableau des pièges classiques.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, vérifie trois choses : l'écart-type (pas la variance), la division par $\sqrt{n}$, et le quantile du niveau annoncé.

</details>
<details><summary>Indice 3</summary>

Les quantiles : 1,645 à 90 %, 1,96 à 95 %, 2,576 à 99 %. (E) : un intervalle de confiance de la moyenne utilise l'erreur type.

</details>

### Ex M02c.27 — Tester une fonction aléatoire : une tolérance en erreurs types

<details><summary>Indice 1</summary>

Relis la fin du §4 (la vitesse en $\frac{1}{\sqrt{n}}$), le théorème central limite (§5) et l'erreur type d'une proportion (fiche §7).

</details>
<details><summary>Indice 2</summary>

`estimate_pi` renvoie 4 fois une proportion $\hat{p}$ : son erreur type est 4 fois celle de $\hat{p}$, $\sqrt{\frac{p(1 - p)}{n}}$ avec $p = \frac{\pi}{4}$. Pour $k$, calcule $2(1 - \Phi(k))$ pour $k = 2, 3, 4, 5$ (`2 * stats.norm.sf(k)`), et compare $k$ au biais de 12 erreurs types de la copie fausse.

</details>
<details><summary>Indice 3</summary>

`abs(estimate(n, np.random.default_rng(seed)) - math.pi) <= TOLERANCE_K * pi_standard_error(n)`. Avec $k = 4$ ou 5, une fausse alarme arrive moins d'une fois sur dix mille tests, et la copie fausse, à 12 erreurs types, est toujours attrapée.

</details>

### Ex M02c.28 — Défi : un intervalle à 95 % avec dix valeurs d'une loi asymétrique

<details><summary>Indice 1</summary>

Commence par le bootstrap des percentiles (fiche §7) : regarde sa couverture. Puis relis la remarque clé de l'énoncé : si $X$ suit une loi exponentielle de moyenne $\mu$, $\frac{X}{\mu}$ suit la loi exponentielle de moyenne 1.

</details>
<details><summary>Indice 2</summary>

La loi de $\frac{\bar{X}}{\mu}$ est donc celle de la moyenne de 10 exponentielles de moyenne 1 : elle ne dépend pas de $\mu$. Simule-la une fois pour toutes, avec **au moins 100 000** moyennes de 10 tirages `rng.exponential(1.0, ...)` (avec quelques milliers seulement, l'aléa sur les percentiles suffit à faire sortir la couverture de la fenêtre), et lis ses percentiles 2,5 et 97,5.

</details>
<details><summary>Indice 3</summary>

Avec $q_{\text{bas}} \le \frac{\bar{X}}{\mu} \le q_{\text{haut}}$ (probabilité 0,95), isole $\mu$ : $\frac{\bar{X}}{q_{\text{haut}}} \le \mu \le \frac{\bar{X}}{q_{\text{bas}}}$. Calcule $q_{\text{bas}}$ et $q_{\text{haut}}$ **en dehors** de `interval_10`, une seule fois.

</details>
