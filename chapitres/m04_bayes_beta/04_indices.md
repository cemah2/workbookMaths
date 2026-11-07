# M04 · Bayes, vraisemblance et loi Beta — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M04.Q1 — Les quatre termes de la formule de Bayes

<details><summary>Indice 1</summary>

Relis « La formule et ses quatre termes » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Écris chaque phrase avec la notation : « des fichiers malveillants, l'antivirus alerte sur 98 % » est une probabilité **sachant** malveillant.

</details>
<details><summary>Indice 3</summary>

5 : calcule $\frac{P(O \mid H)\,P(H)}{P(O)}$ et compare au quatrième chiffre. 6 : le dénominateur de la formule dépend-il de l'hypothèse ?

</details>

### M04.Q2 — Mettre à jour deux fois

<details><summary>Indice 1</summary>

Relis « Observation après observation » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Pour la deuxième observation, l'a priori est l'a posteriori de la première.

</details>
<details><summary>Indice 3</summary>

5 : chaque observation multiplie le rapport $\frac{P(H_1 \mid \ldots)}{P(H_2 \mid \ldots)}$ par le rapport des vraisemblances. 6 : $P(H_1 \mid \ldots) = \frac{r}{r + 1}$ si le rapport vaut $r$.

</details>

### M04.Q3 — La vraisemblance, une fonction du paramètre

<details><summary>Indice 1</summary>

Relis « La vraisemblance, une fonction du paramètre » (fiche §3).

</details>
<details><summary>Indice 2</summary>

La vraisemblance d'une suite : un facteur $\theta$ par succès, un facteur $1 - \theta$ par échec.

</details>
<details><summary>Indice 3</summary>

3 : calcule l'intégrale avec la fonction Beta (fiche §4). 6 : quelle est la monotonie de $(1 - \theta)^6$ ?

</details>

### M04.Q4 — La loi Beta : forme et paramètres

<details><summary>Indice 1</summary>

Relis « Moyenne, variance, mode » et « Les formes de la loi Beta » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Moyenne $\frac{a}{a + b}$, variance $\frac{ab}{(a + b)^2(a + b + 1)}$, $\Gamma(n) = (n - 1)!$.

</details>
<details><summary>Indice 3</summary>

3 : compare les variances, ou le nombre de pseudo-observations $a + b$. 6 : calcule la densité de $\mathrm{Beta}(2, 2)$ en $\frac{1}{2}$.

</details>

### M04.Q5 — Conjuguée, Laplace, MAP

<details><summary>Indice 1</summary>

Relis « La conjugaison » (fiche §5) et « Trois estimations d'un paramètre » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Succès sur $a$, échecs sur $b$. Mode $\frac{a - 1}{a + b - 2}$, moyenne $\frac{a}{a + b}$.

</details>
<details><summary>Indice 3</summary>

5 : écris l'a posteriori de $\mathrm{Beta}(1, 1)$ après $k$ succès sur $n$, puis son mode.

</details>

### M04.Q6 — Logarithmes et underflow

<details><summary>Indice 1</summary>

Relis « Quand le produit devient 0 » et « Revenir aux probabilités : log-sum-exp » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\ln(x^n) = n\ln x$. Le plus petit `float64` positif vaut environ $5 \times 10^{-324}$.

</details>
<details><summary>Indice 3</summary>

5 : mets $e^{-500}$ en facteur : $e^{-500}(1 + 1)$.

</details>

### M04.Q7 — Fréquentiste ou bayésien ?

<details><summary>Indice 1</summary>

Relis « Deux façons de lire une probabilité » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Une probabilité **sur un paramètre** est bayésienne ; une fréquence sur des expériences répétées est fréquentiste.

</details>
<details><summary>Indice 3</summary>

6 : relis la description de l'échantillonnage de Thompson : que tire-t-on à chaque affichage ?

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M04.R1 — Probabilités conditionnelles (M03)

<details><summary>Indice 1</summary>

Fais le tableau 2 × 2 (système, achat) avec ses totaux.

</details>
<details><summary>Indice 2</summary>

« sachant iOS » : on divise par le nombre d'utilisateurs iOS ; « sachant achat » : par le nombre d'acheteurs.

</details>
<details><summary>Indice 3</summary>

5 : compare $P(\text{achat} \mid \text{iOS})$ à $P(\text{achat})$.

</details>

### M04.R2 — Intégrales et densités (M02a)

<details><summary>Indice 1</summary>

Une primitive de $x^n$ est $\frac{x^{n + 1}}{n + 1}$.

</details>
<details><summary>Indice 2</summary>

Une densité sur $[0, 1]$ a une intégrale de 1 ; son espérance est $\int_0^1 x\,f(x)\,dx$.

</details>
<details><summary>Indice 3</summary>

5 : une primitive de $(1 - x)^4$ est $-\frac{(1 - x)^5}{5}$.

</details>

### M04.R3 — Loi binomiale (M02b)

<details><summary>Indice 1</summary>

Relis la loi binomiale de M02b : $P(X = k) = \binom{n}{k}p^k(1 - p)^{n - k}$.

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[X] = np$, $\mathbb{V}(X) = np(1 - p)$.

</details>
<details><summary>Indice 3</summary>

5 : le coefficient dépend-il de $p$ ? Que fait une constante positive au maximum d'une fonction ?

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M04.1 — Bayes avec deux hypothèses : un capteur de fuite d'eau

<details><summary>Indice 1</summary>

Fais le tableau du §1 : hypothèse, a priori, vraisemblance de « sonne », produit, puis l'évidence.

</details>
<details><summary>Indice 2</summary>

L'évidence additionne les deux façons de sonner : avec une fuite (bonne détection) et sans fuite (fausse alerte). Pour c), la vraisemblance de « ne sonne pas » est $1 - $ celle de « sonne ».

</details>
<details><summary>Indice 3</summary>

f) : avec deux capteurs, la vraisemblance de chaque hypothèse est un produit de deux probabilités (ou reprends b) comme nouvel a priori). g) : écris $\frac{0{,}0095}{0{,}0095 + 0{,}99\,x} \ge 0{,}5$ et résous en $x$.

</details>

### Ex M04.2 — Trois hypothèses et un tableau de mise à jour

<details><summary>Indice 1</summary>

Relis l'exemple du QCM (fiche §2) : un tableau par observation, l'a posteriori de l'un devient l'a priori du suivant.

</details>
<details><summary>Indice 2</summary>

Pour une semaine N, la vraisemblance de chaque type est sa probabilité de **ne pas** venir : $1 - 0{,}9$, $1 - 0{,}4$, $1 - 0{,}05$.

</details>
<details><summary>Indice 3</summary>

e) : le produit des trois évidences, ou la somme sur les types de a priori × trois vraisemblances. h) : après $m$ semaines N, compare les poids $0{,}0243 \times 0{,}1^m$, $0{,}048 \times 0{,}6^m$ et $0{,}000475 \times 0{,}95^m$.

</details>

### Ex M04.3 — La vraisemblance d'un taux de clic

<details><summary>Indice 1</summary>

Relis l'imprimante de la fiche (§3) : même forme de vraisemblance.

</details>
<details><summary>Indice 2</summary>

Un rapport de vraisemblances se simplifie : $\frac{L(0{,}15)}{L(0{,}10)} = \big(\frac{0{,}15}{0{,}10}\big)^3\big(\frac{0{,}85}{0{,}90}\big)^{17}$.

</details>
<details><summary>Indice 3</summary>

d) : la loi binomiale multiplie $L$ par le nombre de places des 3 clics. g) : sur deux jours, la vraisemblance est le produit des deux : additionne les clics et les affichages.

</details>

### Ex M04.4 — Maximiser une vraisemblance : dériver son logarithme

<details><summary>Indice 1</summary>

Relis la loi exponentielle de la fiche (§3).

</details>
<details><summary>Indice 2</summary>

$\ell(\lambda) = 5\ln\lambda - 8\lambda$ ; dérive deux fois. Pour Poisson, $\ell(\mu) = -5\mu + (\sum_i x_i)\ln\mu - \sum_i \ln(x_i!)$.

</details>
<details><summary>Indice 3</summary>

c) : résous $\frac{5}{\lambda} - 8 = 0$. g) : résous $-5 + \frac{\sum_i x_i}{\mu} = 0$.

</details>

### Ex M04.5 — La loi Beta : normalisation, moyenne, mode, variance

<details><summary>Indice 1</summary>

Relis les formules de la loi Beta (fiche §4) et l'exemple $\mathrm{Beta}(3, 6)$.

</details>
<details><summary>Indice 2</summary>

$B(2, 5) = \frac{\Gamma(2)\Gamma(5)}{\Gamma(7)}$ avec $\Gamma(n) = (n - 1)!$. La densité est $\frac{1}{B(2, 5)}\theta(1 - \theta)^4$.

</details>
<details><summary>Indice 3</summary>

f) : avec $u = 1 - \theta$, $\int_0^{0{,}5} \theta(1 - \theta)^4\,d\theta = \int_{0{,}5}^1 (1 - u)u^4\,du$. g) : reconnais $\theta^2(1 - \theta)$ comme la forme de $\mathrm{Beta}(3, 2)$.

</details>

### Ex M04.6 — Conjugaison : de Beta(a, b) à Beta(a + k, b + n − k)

<details><summary>Indice 1</summary>

Relis la règle de conjugaison et « Des pseudo-observations » (fiche §5).

</details>
<details><summary>Indice 2</summary>

$\theta$ est le taux de retour : les retours sont les « succès », les ventes gardées les « échecs ».

</details>
<details><summary>Indice 3</summary>

c) : le poids des données vaut $\frac{n}{a + b + n}$, avec les paramètres de l'a priori. h) : résous $\frac{n}{30 + n} \ge 0{,}9$.

</details>

### Ex M04.7 — Lissage de Laplace : la prédictive avec Beta(1, 1)

<details><summary>Indice 1</summary>

Relis « Le lissage de Laplace » et « La loi prédictive » (fiche §5).

</details>
<details><summary>Indice 2</summary>

La probabilité du succès suivant est la moyenne a posteriori : $\frac{k + 1}{n + 2}$ ; pour $K$ catégories, $\frac{n_j + 1}{n + K}$.

</details>
<details><summary>Indice 3</summary>

e) : multiplie la probabilité du premier achat par celle du second **après mise à jour**. f) : passe par le contraire, « aucun achat ».

</details>

### Ex M04.8 — MAP, maximum de vraisemblance et moyenne a posteriori

<details><summary>Indice 1</summary>

Relis « Trois estimations d'un paramètre » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Écris d'abord l'a posteriori (ses deux paramètres), puis son mode et sa moyenne.

</details>
<details><summary>Indice 3</summary>

h) : l'a posteriori est $\mathrm{Beta}(5 + n, 5)$ ; écris le MAP en fonction de $n$ et résous l'inégalité stricte.

</details>

### Ex M04.9 — Un intervalle de crédibilité d'une loi Beta

<details><summary>Indice 1</summary>

Relis « L'intervalle de crédibilité » (fiche §6) et les quantiles de M02a §7.

</details>
<details><summary>Indice 2</summary>

Une borne $x$ de quantile $q$ résout $F(x) = q$ ; la borne basse a $q = 0{,}025$, la borne haute $q = 0{,}975$.

</details>
<details><summary>Indice 3</summary>

Pour $\mathrm{Beta}(1, 9)$ : $1 - (1 - x)^9 = q \iff x = 1 - (1 - q)^{1/9}$. Pour $\mathrm{Beta}(3, 1)$ : $x^3 = q$.

</details>

### Ex M04.10 — Log-probabilités : additionner au lieu de multiplier, normaliser par log-sum-exp

<details><summary>Indice 1</summary>

Relis « Quand le produit devient 0 » et « Revenir aux probabilités : log-sum-exp » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\log_{10} x = \frac{\ln x}{\ln 10}$. Pour d), mets $e^{-1000}$ en facteur.

</details>
<details><summary>Indice 3</summary>

f) : ajoute $\ln(\text{a priori})$ à chaque log-vraisemblance, soustrais le maximum, prends les exponentielles, divise par leur somme.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M04.11 — La conjugaison Beta-binomiale, démontrée

<details><summary>Indice 1</summary>

Relis « La conjugaison » (fiche §5) : c'est la démonstration, sur un exemple.

</details>
<details><summary>Indice 2</summary>

Regroupe les puissances de $\theta$ et de $1 - \theta$ dans le produit ; tout le reste est une constante.

</details>
<details><summary>Indice 3</summary>

4 : la constante trouvée en 3 et celle de 2 sont égales : isole $P(K = k)$. 6 : remplace $k$ par $np$ et garde les termes dominants. 7 : même démarche, avec $\lambda$ et $e^{-\lambda}$.

</details>

### Ex M04.12 — Le maximum de vraisemblance d'une loi de Bernoulli est la fréquence

<details><summary>Indice 1</summary>

Relis l'imprimante (fiche §3) : c'est le cas $k = 2$, $n = 12$.

</details>
<details><summary>Indice 2</summary>

Mets $\ell'(\theta)$ sous un même dénominateur, $\theta(1 - \theta)$, et étudie le signe du numérateur.

</details>
<details><summary>Indice 3</summary>

3 : pour $k = 0$, n'écris pas $\ln 0$ : étudie directement $(1 - \theta)^n$. 4 : linéarité de l'espérance, et variance d'une somme de variables indépendantes. 6 : l'a posteriori, puis son mode (fiche §6).

</details>

### Ex M04.13 — Le mode de la loi Beta

<details><summary>Indice 1</summary>

Relis « Les formes de la loi Beta » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$g'(\theta) = \frac{(a - 1) - (a + b - 2)\theta}{\theta(1 - \theta)}$ : le signe est celui d'une fonction affine de $\theta$.

</details>
<details><summary>Indice 3</summary>

2 : chasse les dénominateurs (positifs) et simplifie. 5 : le numérateur de $g'$ vaut $a - 1 < 0$ en 0 et croît. 7 : traite $k = 0$ par la question 3.

</details>

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M04.14 — Un test A/B : deux taux de conversion et P(θB > θA) par simulation

<details><summary>Indice 1</summary>

Relis « L'échantillonnage de Thompson » (fiche §8) et « La conjugaison » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Moyenne $\frac{a}{a + b}$ et écart-type $\sqrt{\frac{ab}{(a + b)^2(a + b + 1)}}$ pour chaque a posteriori.

</details>
<details><summary>Indice 3</summary>

e) : $\theta_B - \theta_A$ approchée par une loi normale de moyenne la différence des moyennes et de **variance** la somme des variances ; puis $\Phi\big(\frac{\text{moyenne}}{\text{écart-type}}\big)$.

</details>

### Ex M04.15 — MML §6.3 (relire le théorème de Bayes) et §6.6 : conjugaison et famille exponentielle (lecture guidée)

<details><summary>Indice 1</summary>

Lis d'abord la fin de §6.3, puis §6.6 avec la fiche (§5 et §7) ouverte à côté.

</details>
<details><summary>Indice 2</summary>

Cherche les mots *prior*, *likelihood*, *posterior*, *evidence*, puis *conjugate*, *sufficient statistic*, *exponential family*.

</details>
<details><summary>Indice 3</summary>

6 : pour Bernoulli, écris $\mu^x(1 - \mu)^{1 - x} = \exp\big(x\ln\frac{\mu}{1 - \mu} + \ln(1 - \mu)\big)$ et identifie les morceaux.

</details>

### Ex M04.16 — MML §8.3 : maximum de vraisemblance et MAP (lecture guidée)

<details><summary>Indice 1</summary>

Lis §8.3 avec la fiche (§3 et §6) ouverte à côté.

</details>
<details><summary>Indice 2</summary>

Le livre minimise moins la log-vraisemblance ; le MAP ajoute moins le logarithme de l'a priori.

</details>
<details><summary>Indice 3</summary>

5 : l'a posteriori est $\mathrm{Beta}(4, 18)$ ; moins son logarithme vaut $-3\ln\theta - 17\ln(1 - \theta)$ plus une constante.

</details>

### Ex M04.17 — Expliquer la conjugaison avec des pseudo-observations

<details><summary>Indice 1</summary>

Relis « Des pseudo-observations » (fiche §5).

</details>
<details><summary>Indice 2</summary>

$\frac{\text{clics} + 2}{\text{affichages} + 10}$ est la moyenne a posteriori de quelle loi Beta, partie de quel a priori ?

</details>
<details><summary>Indice 3</summary>

Trois idées : ce que valent 2 et 10, ce qui se passe quand les vrais affichages sont nombreux, le cas où l'on a très peu de données.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M04.E1 — Qu'est-ce que le lissage de Laplace, et pourquoi l'utiliser ?

<details><summary>Indice 1</summary>

Relis « Le lissage de Laplace » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Pense au classifieur naïf de Bayes : un produit de probabilités, dont une seule peut valoir 0.

</details>
<details><summary>Indice 3</summary>

Plan : la formule (deux issues, $K$ catégories) ; le problème des comptages nuls ; l'a priori uniforme ; une variante ($\alpha$) ou une limite.

</details>

<a id="notebook"></a>

## Notebook

### Ex M04.18 — Densité et moments de la loi Beta (avec `math.lgamma`) · `beta_pdf, beta_moments`

<details><summary>Indice 1</summary>

Relis la docstring de `beta_pdf` en entier : elle dit les valeurs aux bords.

</details>
<details><summary>Indice 2</summary>

À l'intérieur de $]0, 1[$, calcule le logarithme de la densité avec `math.log`, `math.log1p(-x)` et `math.lgamma`, puis `math.exp` à la fin.

</details>
<details><summary>Indice 3</summary>

Aux bords, regarde l'exposant du facteur qui vaut 0 : $a - 1$ en $x = 0$, $b - 1$ en $x = 1$ ; positif, nul ou négatif, trois cas.

</details>

### Ex M04.19 — Mise à jour conjuguée et loi prédictive des prochains essais · `conjugate_beta_update, posterior_predictive`

<details><summary>Indice 1</summary>

Relis « La loi prédictive » (fiche §5).

</details>
<details><summary>Indice 2</summary>

$\ln\binom{n}{k} = \ln\Gamma(n + 1) - \ln\Gamma(k + 1) - \ln\Gamma(n - k + 1)$.

</details>
<details><summary>Indice 3</summary>

Teste `k < 0 or k > n` **avant** d'appeler `math.lgamma`, qui refuse 0 et les entiers négatifs.

</details>

### Ex M04.20 — Le MAP d'une loi Beta, cas limites compris · `map_estimate_beta`

<details><summary>Indice 1</summary>

Fais l'exercice ∂ M04.13, ou esquisse les densités de $\mathrm{Beta}(0{,}6 ;\ 3)$, $\mathrm{Beta}(3 ;\ 0{,}8)$ et $\mathrm{Beta}(0{,}8 ;\ 0{,}6)$.

</details>
<details><summary>Indice 2</summary>

Traite d'abord le cas $a > 1$ et $b > 1$, puis les deux cas sans mode unique, puis les densités monotones.

</details>
<details><summary>Indice 3</summary>

Décroissante si `a <= 1 < b` ou `a < 1 == b` ; croissante dans les cas symétriques ; renvoie `0.0` ou `1.0`.

</details>

### Ex M04.21 — La fonction Beta avec `scipy.special` : `beta`, `betaln` et l'underflow

<details><summary>Indice 1</summary>

Lis `help(special.betaln)`.

</details>
<details><summary>Indice 2</summary>

Un rapport de deux nombres minuscules se calcule par la différence de leurs logarithmes.

</details>
<details><summary>Indice 3</summary>

e) : `math.exp(special.betaln(602, 900) - special.betaln(600, 900))`.

</details>

### Ex M04.22 — Prédire : le MAP avec Beta(1, 1) après trois échecs

<details><summary>Indice 1</summary>

Écris l'a posteriori, puis sa densité.

</details>
<details><summary>Indice 2</summary>

$\mathrm{Beta}(1, 4)$ a la densité $4(1 - \theta)^3$ : où est son maximum ?

</details>
<details><summary>Indice 3</summary>

d) : après un premier succès, la loi n'est plus la même. e) : $F(x) = 1 - (1 - x)^4$.

</details>

### Ex M04.23 — Le posterior se resserre : la largeur de l'intervalle en 1/√n

<details><summary>Indice 1</summary>

Relis « L'intervalle de crédibilité » (fiche §6).

</details>
<details><summary>Indice 2</summary>

L'a posteriori est $\mathrm{Beta}(a + k,\ b + n - k)$ ; `stats.beta(..., ...).ppf([0.025, 0.975])` donne ses deux bornes.

</details>
<details><summary>Indice 3</summary>

Renvoie `float(haute - basse)`.

</details>

### Ex M04.24 — Prior, vraisemblance et posterior sur une même figure

<details><summary>Indice 1</summary>

Relis la figure de « La conjugaison » (fiche §5).

</details>
<details><summary>Indice 2</summary>

La vraisemblance normalisée est la densité de $\mathrm{Beta}(k + 1,\ n - k + 1)$ : trois densités Beta, donc.

</details>
<details><summary>Indice 3</summary>

`theta = np.linspace(0, 1, 501)`, puis `ax.plot(theta, stats.beta(a, b).pdf(theta), label="a priori")`, et de même pour les deux autres ; `ax.legend()`, `ax.set_xlabel("θ")`.

</details>

### Ex M04.25 — Chasse à l'erreur : évidence oubliée, mise à jour à l'envers, mode et moyenne

<details><summary>Indice 1</summary>

Relis les ⚠️ des §1, §5 et §6, et le tableau des pièges classiques.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, écris ce que le calcul donne vraiment, et compare au commentaire.

</details>
<details><summary>Indice 3</summary>

Pour $\theta$, une pièce défectueuse est un succès. Un a posteriori se divise par l'évidence. Le mode n'est pas la moyenne. Une prédiction utilise l'a posteriori.

</details>

### Ex M04.26 — Un calcul stable : comparer des vraisemblances en logarithmes (`math.lgamma`)

<details><summary>Indice 1</summary>

Relis « Quand le produit devient 0 » (fiche §7) et ta fonction `posterior_predictive`.

</details>
<details><summary>Indice 2</summary>

Traite les cas particuliers d'abord : $p$ hors de $[0, 1]$, puis $k$ hors de $0..n$, puis $p = 0$ et $p = 1$.

</details>
<details><summary>Indice 3</summary>

Pour $p = 0$ : la probabilité vaut 1 si $k = 0$ (logarithme 0.0), et 0 sinon (`-math.inf`).

</details>

### Ex M04.27 — Défi : traduire l'avis d'un expert en une loi Beta (moyenne, écart-type, intervalle)

<details><summary>Indice 1</summary>

a) : avec $m = \frac{a}{a + b}$ et $s = a + b$, la variance vaut $\frac{m(1 - m)}{s + 1}$.

</details>
<details><summary>Indice 2</summary>

b) : deux inconnues, deux équations : le quantile 0,05 vaut 0,10, le quantile 0,95 vaut 0,32.

</details>
<details><summary>Indice 3</summary>

Écris `gaps(x)`, qui renvoie `[quantile_0.05 - 0.10, quantile_0.95 - 0.32]` pour la loi Beta de paramètres `x` (avec `stats.beta(a, b).ppf([0.05, 0.95])`), puis `optimize.fsolve(gaps, [5.0, 15.0])` : il part du point $(5, 15)$. Si le solveur essaie des paramètres négatifs, prends comme inconnues $\ln a$ et $\ln b$ (`a, b = np.exp(x)` dans `gaps`), et pars alors de `np.log([5.0, 15.0])`.

</details>
