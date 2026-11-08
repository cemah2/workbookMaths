# M08 · Tests statistiques — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M08.Q1 — Ce qu'une p-valeur est, et ce qu'elle n'est pas

<details><summary>Indice 1</summary>

Relis « La p-valeur » et « Ce qu'une p-valeur n'est pas » (fiche §1).

</details>
<details><summary>Indice 2</summary>

La p-valeur se calcule **en supposant** $H_0$ vraie : c'est une probabilité sur les données, pas sur l'hypothèse.

</details>
<details><summary>Indice 3</summary>

4 : pense à M08.10 (la loi de la p-valeur sous $H_0$). 5 : l'erreur type diminue comme $\frac{1}{\sqrt{n}}$. 6 : une p-valeur mélange la taille de l'effet et la quantité de données.

</details>

### M08.Q2 — Unilatéral ou bilatéral ?

<details><summary>Indice 1</summary>

Relis « Unilatéral ou bilatéral » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Le sens de $H_1$ se fixe **avant** de voir les données. Pour une loi symétrique, les deux côtés ont la même probabilité.

</details>
<details><summary>Indice 3</summary>

4 : relis l'exemple $p_0 = 0{,}1$ de la fiche. 5 : faire les deux tests unilatéraux et garder le meilleur, c'est rejeter dans les deux queues.

</details>

### M08.Q3 — Permuter quoi, et sous quelle hypothèse ?

<details><summary>Indice 1</summary>

Relis « L'idée : sous $H_0$, les groupes sont interchangeables », « Le test par tirage au hasard » et « Mesures appariées » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Sous $H_0$, le groupe d'une valeur ne dit rien d'elle : toutes les répartitions sont aussi probables. On en tire $B$, on compte $C$.

</details>
<details><summary>Indice 3</summary>

2 : choisir 3 valeurs parmi 7. 3 : $\frac{C + 1}{B + 1}$. 5 : on ne mélange pas les serveurs entre eux.

</details>

### M08.Q4 — Erreurs de type I et II, puissance : associer

<details><summary>Indice 1</summary>

Relis « Deux façons de se tromper » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Type I : rejeter $H_0$ alors qu'elle est vraie ; type II : ne pas la rejeter alors qu'elle est fausse ; puissance : $P(\text{rejeter} \mid H_1)$.

</details>
<details><summary>Indice 3</summary>

1 : l'hypothèse nulle d'une alarme est « pas de feu ». 6 : une règle plus sévère rejette moins souvent, sous $H_0$ comme sous $H_1$.

</details>

### M08.Q5 — Comparaisons multiples : vrai ou faux

<details><summary>Indice 1</summary>

Relis la fiche §6.

</details>
<details><summary>Indice 2</summary>

Chaque test vrai donne un faux positif avec la probabilité $\alpha$ ; Bonferroni divise le seuil par $m$, ou multiplie les p-valeurs par $m$.

</details>
<details><summary>Indice 3</summary>

2 : sur quelle inégalité repose la garantie (M08.11) ? 6 : combien de tests a-t-on faits, même si un seul est publié ?

</details>

### M08.Q6 — AIC, BIC, facteur de Bayes : qui pénalise quoi ?

<details><summary>Indice 1</summary>

Relis la fiche §7.

</details>
<details><summary>Indice 2</summary>

$\mathrm{AIC} = 2k - 2\ln L$, $\mathrm{BIC} = k\ln n - 2\ln L$ ; le plus petit gagne. Cote a posteriori $=$ facteur de Bayes $\times$ cote a priori.

</details>
<details><summary>Indice 3</summary>

2 : compare $\ln 1000$ à 2. 4 : une cote de 5 contre 1 correspond à une probabilité de $\frac{5}{6}$. 6 : l'évidence est une moyenne, et une probabilité totale vaut 1.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M08.R1 — La loi binomiale (M02b)

<details><summary>Indice 1</summary>

Relis M02b (loi binomiale).

</details>
<details><summary>Indice 2</summary>

$P(K = k) = \binom{n}{k}p^k(1 - p)^{n-k}$, $\mathbb{E}[K] = np$, $\mathbb{V}(K) = np(1 - p)$.

</details>
<details><summary>Indice 3</summary>

4 : passe par le complément, $1 - P(K = 0)$.

</details>

### M08.R2 — L'intervalle de confiance d'une moyenne (M02c)

<details><summary>Indice 1</summary>

Relis M02c (erreur type, intervalle de confiance).

</details>
<details><summary>Indice 2</summary>

Erreur type $\frac{s}{\sqrt{n}}$ ; demi-largeur $z \times$ erreur type, avec $z = 1{,}96$ à 95 % et $1{,}645$ à 90 %.

</details>
<details><summary>Indice 3</summary>

5 : résous $1{,}96 \times \frac{4{,}2}{\sqrt{n}} \le 0{,}5$, puis arrondis au-dessus.

</details>

### M08.R3 — Vraisemblance et log-vraisemblance (M04)

<details><summary>Indice 1</summary>

Relis M04 (vraisemblance, maximum de vraisemblance).

</details>
<details><summary>Indice 2</summary>

$L(p) = p^3(1 - p)^5$ ; le logarithme transforme le produit en somme ; dérive et annule.

</details>
<details><summary>Indice 3</summary>

3 : $\frac{3}{p} = \frac{5}{1 - p}$. 5 : $8\ln\frac{1}{2}$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M08.1 — Un test binomial à la main : un algorithme de compression est-il plus rapide sur douze fichiers ?

<details><summary>Indice 1</summary>

Relis « Un exemple » et « La p-valeur » (fiche §1), puis « Unilatéral ou bilatéral » et « Quand $n$ est grand » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Sous $H_0$, $K$ suit $\mathcal{B}(12, \frac{1}{2})$, et chaque issue a la probabilité $\frac{\binom{12}{k}}{4096}$.

</details>
<details><summary>Indice 3</summary>

b) $\binom{12}{10} + \binom{12}{11} + \binom{12}{12} = 66 + 12 + 1$. c) La loi est symétrique : les issues $K \le 2$ comptent autant. f) Calcule $P(K \ge 9)$ (il faut $\binom{12}{9} = 220$). g) $1 - \Phi(2{,}31)$.

</details>

### Ex M08.2 — Un test par permutation exhaustif : deux groupes de trois mesures, vingt répartitions

<details><summary>Indice 1</summary>

Relis « L'idée » et « Le test exact » (fiche §3).

</details>
<details><summary>Indice 2</summary>

La somme des six temps vaut 97 : $\bar{x}_B = \frac{97 - S_A}{3}$. La statistique ne dépend que de $S_A$.

</details>
<details><summary>Indice 3</summary>

Liste les 20 triplets par ordre de somme : la plus petite somme possible est celle des trois plus petits temps. d) Cherche aussi la plus grande somme. f) $\binom{8}{4}$. g) $\frac{C + 1}{B + 1}$.

</details>

### Ex M08.3 — Erreur de type I, erreur de type II et puissance d'un test binomial

<details><summary>Indice 1</summary>

Relis « Deux façons de se tromper » et son exemple (fiche §4).

</details>
<details><summary>Indice 2</summary>

Le risque de type I se calcule sous $p = \frac{1}{2}$, la puissance sous $p = 0{,}8$, avec la même règle « $K \ge c$ ».

</details>
<details><summary>Indice 3</summary>

a) $\binom{14}{11} = 364$, $\binom{14}{12} = 91$, $\binom{14}{13} = 14$. b) $\binom{14}{j}0{,}8^j\,0{,}2^{14-j}$ pour $j = 11$ à 14. d) $\binom{14}{10} = 1001$.

</details>

### Ex M08.4 — Combien d'observations pour une puissance de 80 % ? (approximation normale)

<details><summary>Indice 1</summary>

Relis « La taille d'échantillon » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$n \ge \Big(\frac{(z_{1-\alpha} + z_{1-\beta})\,\sigma}{\delta}\Big)^2$, et la puissance $\Phi\big(\frac{\delta\sqrt{n}}{\sigma} - z_{1-\alpha}\big)$.

</details>
<details><summary>Indice 3</summary>

c) $(2{,}487 \times 4)^2$, arrondi au-dessus. d) Remplace $z_{0{,}95}$ par $z_{0{,}975}$. f) $\frac{2 \times 6}{8} = 1{,}5$.

</details>

### Ex M08.5 — L'intervalle d'une proportion : Wald contre Wilson, avec peu de succès

<details><summary>Indice 1</summary>

Relis « Une proportion : Wald, et ses défauts » et « L'intervalle de Wilson » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Wald : $\hat{p} \pm z\sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$. Wilson : centre $\frac{\hat{p} + z^2/(2n)}{1 + z^2/n}$, demi-largeur $\frac{z}{1 + z^2/n}\sqrt{\frac{\hat{p}(1 - \hat{p})}{n} + \frac{z^2}{4n^2}}$.

</details>
<details><summary>Indice 3</summary>

$\frac{z^2}{n} = \frac{3{,}8416}{50} \approx 0{,}0768$. f) Avec $\hat{p} = 0$, le centre et la demi-largeur sont égaux.

</details>

### Ex M08.6 — L'intervalle de Student d'une différence appariée : un serveur avant et après une mise à jour

<details><summary>Indice 1</summary>

Relis « Une différence appariée : l'intervalle de Student » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Travaille sur les six différences $d_i$ : leur moyenne, leur écart-type ($\mathrm{ddof} = 1$), puis $\bar{d} \pm t_{5}\frac{s_d}{\sqrt{6}}$.

</details>
<details><summary>Indice 3</summary>

Les différences : 4, 1, 6, 1, 4, 5. d) La table de la fiche, ligne 5 degrés de liberté. f) Calcule la variance de chaque colonne, puis la racine de leur somme divisée par 6. h) $2^6$ combinaisons de signes : lesquelles donnent une moyenne au moins égale à 3,5 ?

</details>

### Ex M08.7 — Vingt tests au seuil de 5 % : les faux positifs attendus, puis Bonferroni

<details><summary>Indice 1</summary>

Relis « Le problème » et « La correction de Bonferroni » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Le nombre de faux positifs est une somme de 20 indicatrices ; « au moins un » se calcule par le complément de « aucun ».

</details>
<details><summary>Indice 3</summary>

b) $1 - 0{,}95^{20}$. d) $1 - 0{,}9975^{20}$. e) Multiplie chaque p-valeur par 20, le nombre de tests faits.

</details>

### Ex M08.8 — L'AIC et le BIC de deux modèles, à partir de leurs log-vraisemblances

<details><summary>Indice 1</summary>

Relis « AIC et BIC » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\mathrm{AIC} = 2k - 2\ln L$, $\mathrm{BIC} = k\ln n - 2\ln L$, avec $\ln$ népérien ; le plus petit gagne.

</details>
<details><summary>Indice 3</summary>

$-2\ln L_1 = 825{,}2$, $-2\ln L_2 = 810{,}2$, $\ln 200 \approx 5{,}298$. g) Écris $\mathrm{BIC}_2 < \mathrm{BIC}_1$ et isole $\ln L_2 - \ln L_1$.

</details>

### Ex M08.9 — Un facteur de Bayes entre deux taux de clics

<details><summary>Indice 1</summary>

Relis « Le facteur de Bayes » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Pour un modèle sans paramètre libre, l'évidence est la vraisemblance : $\binom{40}{6}p^6(1 - p)^{34}$. Pour $M_C$, raisonne comme pour la pièce de la fiche.

</details>
<details><summary>Indice 3</summary>

c) Le coefficient binomial se simplifie. d) Cote a posteriori $= \mathrm{BF} \times \frac{1}{3}$, puis $P = \frac{\text{cote}}{1 + \text{cote}}$. e) Combien de nombres de clics sont possibles ?

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M08.10 — Sous H0, une p-valeur continue suit la loi uniforme

<details><summary>Indice 1</summary>

Relis la fiche §1 et la fonction de répartition (M02b).

</details>
<details><summary>Indice 2</summary>

$P = 1 - F(T)$. Pour $F(T)$, utilise la bijection réciproque $F^{-1}$ : $F(T) \le v \iff T \le F^{-1}(v)$.

</details>
<details><summary>Indice 3</summary>

2 : $P(P \le u) = P\big(F(T) \ge 1 - u\big)$. 4 : $P(K \ge k)$ pour $k = 0, 1, 2, 3$ vaut $1, \frac{7}{8}, \frac{1}{2}, \frac{1}{8}$.

</details>

### Ex M08.11 — L'inégalité de Boole et la garantie de Bonferroni, sans hypothèse d'indépendance

<details><summary>Indice 1</summary>

Relis « La correction de Bonferroni » (fiche §6) et la récurrence (R4).

</details>
<details><summary>Indice 2</summary>

$A \cup B = A \cup (B \setminus A)$, une réunion disjointe. Pour la récurrence, regroupe les $m$ premiers événements.

</details>
<details><summary>Indice 3</summary>

3 : un événement par hypothèse nulle **vraie**, chacun de probabilité au plus $\frac{\alpha}{m}$. 5 : multiplie l'hypothèse de récurrence par $1 - x \ge 0$. 6 : distingue $m\,p_i \ge 1$ et $m\,p_i < 1$.

</details>

### Ex M08.12 — L'intervalle de Wilson, en inversant le test d'une proportion

<details><summary>Indice 1</summary>

Relis « Le lien entre tests et intervalles » et « L'intervalle de Wilson » (fiche §5), et le second degré (R3).

</details>
<details><summary>Indice 2</summary>

Élève au carré (les deux membres sont positifs), développe, et regroupe les termes en $p_0^2$, $p_0$ et le terme constant.

</details>
<details><summary>Indice 3</summary>

$a = 1 + \frac{z^2}{n}$, $b = -\big(2\hat{p} + \frac{z^2}{n}\big)$, $c = \hat{p}^2$ ; le discriminant se simplifie en $\frac{4z^2}{n}\big(\hat{p}(1 - \hat{p}) + \frac{z^2}{4n}\big)$. 4 : évalue le trinôme en 0 et en 1, et situe son sommet $-\frac{b}{2a}$ par rapport à 0 et à 1.

</details>

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M08.13 — Pont : l'importance d'une feature par permutation, sur un petit tableau

<details><summary>Indice 1</summary>

Relis « L'importance d'une feature par permutation » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Recopie le tableau avec la colonne décalée, recalcule $x_1 + x_2$ ligne par ligne, puis compare les prédictions à $y$.

</details>
<details><summary>Indice 3</summary>

$x_1$ décalé : 2, 7, 3, 5, 4, 6. $x_2$ décalé : 4, 2, 3, 1, 5, 3. L'importance est l'accuracy de départ **moins** celle d'après.

</details>

### Ex M08.14 — MML §8.6 : validation croisée imbriquée, sélection bayésienne de modèle et facteur de Bayes

<details><summary>Indice 1</summary>

Lis MML §8.6 en entier, avec la fiche §7 à côté.

</details>
<details><summary>Indice 2</summary>

Repère trois choses : le rôle des deux boucles (§8.6.1), la quantité qui compare les modèles (§8.6.2), la relation entre les cotes (§8.6.3).

</details>
<details><summary>Indice 3</summary>

4 : $4 \times \frac{1}{2}$, puis $\frac{\text{cote}}{1 + \text{cote}}$. 5 : qu'est-ce qui distingue $M_A$ de $M_C$ dans M08.9 ?

</details>

### Ex M08.15 — Expliquer une p-valeur sans dire « la probabilité que H0 soit vraie »

<details><summary>Indice 1</summary>

Relis « Ce qu'une p-valeur n'est pas » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Commence par la supposition (« si la page ne changeait rien… »), puis dis ce qu'on calcule sous cette supposition.

</details>
<details><summary>Indice 3</summary>

Termine par la taille du gain : une p-valeur ne la donne pas, un intervalle oui.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M08.E1 — « Votre test donne p = 0,03 : que concluez-vous, et que dites-vous à l'équipe produit ? »

<details><summary>Indice 1</summary>

Relis la fiche §1, §4 et §6.

</details>
<details><summary>Indice 2</summary>

Quatre temps : le sens de $p = 0{,}03$, la décision au seuil prévu, les vérifications, le message.

</details>
<details><summary>Indice 3</summary>

Les vérifications : un protocole fixé d'avance (pas d'arrêt dès que la p-valeur passe sous 0,05), la taille de l'effet et son intervalle.

</details>

<a id="notebook"></a>

## Notebook

### Ex M08.16 — Le test binomial exact · `binomial_test`

<details><summary>Indice 1</summary>

Relis la fiche §2, et la docstring du module `testing.py`.

</details>
<details><summary>Indice 2</summary>

Les vérifications d'abord ; puis la liste des $P(K = j)$ pour $j = 0$ à $n$ (`math.comb`), et trois cas selon `alternative`.

</details>
<details><summary>Indice 3</summary>

Bilatéral : `sum(q for q in probs if q <= probs[k] * (1 + 1e-7))`, puis `min(1.0, ...)` ; renvoie un `float`.

</details>

### Ex M08.17 — Le test par permutation à deux échantillons · `permutation_test`

<details><summary>Indice 1</summary>

Relis la fiche §3 et la docstring : la procédure y est décrite pas à pas.

</details>
<details><summary>Indice 2</summary>

Un seul générateur, créé avant la boucle ; à chaque tour, `rng.permutation(pooled)` sur les valeurs réunies, `x` d'abord.

</details>
<details><summary>Indice 3</summary>

Le compte avec la tolérance : `t_perm >= observed - 1e-9` (greater), `t_perm <= observed + 1e-9` (less), `abs(t_perm) >= abs(observed) - 1e-9` (bilatéral) ; puis `(count + 1) / (n_permutations + 1)`.

</details>

### Ex M08.18 — Les intervalles de Wilson et de Student · `proportion_ci, paired_difference_ci`

<details><summary>Indice 1</summary>

Relis la fiche §5.

</details>
<details><summary>Indice 2</summary>

$z$ est le quantile d'ordre $\frac{1 + \text{level}}{2}$ (`NormalDist().inv_cdf`) ; le quantile de Student, `scipy.stats.t.ppf(q, n - 1)`.

</details>
<details><summary>Indice 3</summary>

Ramène chaque borne dans $[0, 1]$ avec `min(1.0, max(0.0, ...))` ; pour les différences, `d.std(ddof=1)`.

</details>

### Ex M08.19 — Bonferroni, l'AIC et le BIC · `bonferroni, aic_bic`

<details><summary>Indice 1</summary>

Relis la fiche §6 et §7.

</details>
<details><summary>Indice 2</summary>

`np.minimum(1.0, p * p.size)` ; les deux critères en une ligne chacun, avec `math.log`.

</details>
<details><summary>Indice 3</summary>

Vérifie d'abord que la liste n'est pas vide et que `np.all((p >= 0) & (p <= 1))`.

</details>

### Ex M08.20 — `scipy.stats.binomtest`, `permutation_test` et `ttest_rel` contre tes fonctions

<details><summary>Indice 1</summary>

Relis l'énoncé : il donne le nom de chaque fonction et de chaque attribut.

</details>
<details><summary>Indice 2</summary>

`result.pvalue`, `result.proportion_ci(...).low` et `.high` ; une fonction `statistic(x, y, axis)` pour `permutation_test`.

</details>
<details><summary>Indice 3</summary>

e) `all(abs(mymath.testing.binomial_test(k, 30, 0.1) - stats.binomtest(k, 30, 0.1).pvalue) <= 1e-9 for k in range(31))`.

</details>

### Ex M08.21 — Prédire : sous H0, quelle part de 1 000 p-valeurs tombe sous 0,05 ?

<details><summary>Indice 1</summary>

Relis la fiche §1 et §4, et l'énoncé de M08.10.

</details>
<details><summary>Indice 2</summary>

Sous $H_0$, quelle est la loi d'une p-valeur continue ? Et pour un test binomial sur 10 essais, quelles issues font rejeter à 5 % ?

</details>
<details><summary>Indice 3</summary>

b) Seules 0, 1, 9 et 10 réussites donnent une p-valeur au plus 0,05. c) La part sous $H_1$ est la puissance.

</details>

### Ex M08.22 — La puissance d'un test par permutation, selon l'effet et la taille des groupes

<details><summary>Indice 1</summary>

Relis la fiche §4 (puissance) et l'énoncé : la procédure y est fixée.

</details>
<details><summary>Indice 2</summary>

Un générateur `np.random.default_rng(seed)` avant la boucle ; à chaque tour, `x` puis `y`, puis la p-valeur avec `seed=sim`.

</details>
<details><summary>Indice 3</summary>

`rejected += p <= 0.05`, puis `float(rejected / n_sims)`. d) `next(n for n in (5, 10, 20) if power(1.0, n) >= 0.8)`.

</details>

### Ex M08.23 — La loi de la statistique sous H0, et la p-valeur comme une aire

<details><summary>Indice 1</summary>

Relis « Le test exact » (fiche §3) et sa figure.

</details>
<details><summary>Indice 2</summary>

`itertools.combinations(range(len(pooled)), len(x))` donne les indices du premier groupe ; un masque booléen donne le second.

</details>
<details><summary>Indice 3</summary>

Deux `ax.hist` avec les **mêmes** classes (`bins`), l'un pour `values[~extreme]`, l'autre pour `values[extreme]` ; `ax.axvline(observed)` ; `return float(np.mean(extreme))`.

</details>

### Ex M08.24 — Chasse à l'erreur : une p-valeur nulle, un test unilatéral choisi après coup, Bonferroni à l'envers

<details><summary>Indice 1</summary>

Relis le tableau des pièges classiques de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, compare la formule à celle de la fiche : peut-elle donner 0 ? divise-t-elle quand il faut multiplier ? compte-t-elle les deux côtés ?

</details>
<details><summary>Indice 3</summary>

(B) est bien $P(K \ge 14)$ ; $z_{0{,}975} \approx 1{,}960$ ; $\Phi(1{,}8) \approx 0{,}9641$.

</details>

### Ex M08.25 — Tester un test : un pytest qui vérifie l'uniformité des p-valeurs sous H0

<details><summary>Indice 1</summary>

Relis l'énoncé, puis M02c.27 (une tolérance en erreurs types).

</details>
<details><summary>Indice 2</summary>

La part des p-valeurs sous `alpha` est une proportion estimée sur `n_sims` tirages : son erreur type est $\sqrt{\frac{\alpha(1 - \alpha)}{N}}$.

</details>
<details><summary>Indice 3</summary>

`assert abs(share - alpha) <= K_SE * se, f\"expected ... got {share:.4f}\"` : la valeur absolue attrape les deux sens d'erreur. $K_{SE}$ entre 4 et 8.

</details>

### Ex M08.26 — Défi : retrouver les trois vraies features parmi cinquante, avec au plus un faux positif

<details><summary>Indice 1</summary>

Relis la fiche §6 et M08.7.

</details>
<details><summary>Indice 2</summary>

Une p-valeur par feature avec `stats.pearsonr(X[:, j], y).pvalue` ; combien de faux positifs attends-tu au seuil de 5 % sur 47 features de bruit ?

</details>
<details><summary>Indice 3</summary>

`mymath.testing.bonferroni(p_values) <= 0.05`, puis `np.flatnonzero` pour les indices.

</details>
