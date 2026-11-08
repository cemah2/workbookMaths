# M11 · Logique, induction et inégalités de concentration — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 ⚖️ 🗣️ Pont, esprit critique et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M11.Q1 — Réciproque, contraposée, négation

<details><summary>Indice 1</summary>

Relis « Ce que R4 a posé » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Réciproque : échange hypothèse et conclusion. Contraposée : non conclusion ⇒ non hypothèse. Négation : « hypothèse et non conclusion », avec un « il existe » devant.

</details>
<details><summary>Indice 3</summary>

1 : « si un entier est impair, alors il est premier et supérieur à 2 » ; essaie 9. 6 : chaque ∀ devient ∃, chaque ∃ devient ∀, et l'inégalité finale est niée.

</details>

### M11.Q2 — Un argument valide peut-il avoir une conclusion fausse ?

<details><summary>Indice 1</summary>

Relis « Argument, validité, solidité » et le « cas limite » (fiche §1).

</details>
<details><summary>Indice 2</summary>

La validité ne regarde que les lignes où toutes les prémisses sont vraies ; elle ne dit rien des autres.

</details>
<details><summary>Indice 3</summary>

1 : pense au *modus ponens* avec une prémisse fausse de la fiche. 6 : que se passe-t-il si les prémisses sont contradictoires ?

</details>

### M11.Q3 — Diagrammes de Venn et quantificateurs

<details><summary>Indice 1</summary>

Relis « Une phrase, une inclusion » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Écris $A$, $B$ et $C$ en extension (cinq, dix et six éléments) ; une inclusion se vérifie élément par élément.

</details>
<details><summary>Indice 3</summary>

5 : la contraposée de $A \subset B$. 6 : $\lvert A \cup C \rvert = \lvert A \rvert + \lvert C \rvert - \lvert A \cap C \rvert$.

</details>

### M11.Q4 — Les pièges de l'induction

<details><summary>Indice 1</summary>

Relis le §3 de la fiche, ses quatre pièges.

</details>
<details><summary>Indice 2</summary>

2 : lequel des deux, $P(\text{alerte} \mid \text{cas})$ ou $P(\text{cas} \mid \text{alerte})$, vaut 95 % ? 4 : la taille corrige-t-elle un biais de sélection ?

</details>
<details><summary>Indice 3</summary>

1 : calcule $40^2 + 40 + 41$. 6 : la règle de trois donne environ $\frac{3}{n}$.

</details>

### M11.Q5 — Markov ou Tchebychev : quelle borne s'applique ?

<details><summary>Indice 1</summary>

Relis les énoncés des §4 et §5 : quelles hypothèses demande chacune ?

</details>
<details><summary>Indice 2</summary>

Markov : une variable positive et sa moyenne. Tchebychev : la moyenne et la variance, une variable de signe quelconque.

</details>
<details><summary>Indice 3</summary>

1 : $\frac{5}{20}$. 4 : $X \ge 11$ implique $\lvert X - 5 \rvert \ge 6$. 6 : calcule les deux bornes et compare.

</details>

### M11.Q6 — Ce que garantit l'inégalité de Hoeffding, et ce qu'elle suppose

<details><summary>Indice 1</summary>

Relis « Ce que Hoeffding suppose » et la borne de l'union (fiche §6).

</details>
<details><summary>Indice 2</summary>

Le rayon est $(b - a)\sqrt{\frac{\ln(2/\delta)}{2n}}$ : regarde comment il dépend de $n$ et de $\delta$.

</details>
<details><summary>Indice 3</summary>

3 : $\sqrt{4} = 2$. 4 : le rapport $\frac{\ln(2/0{,}0005)}{\ln(2/0{,}05)}$. 5 : combien de quantités as-tu regardées avant de choisir ?

</details>

### M11.Q7 — Explorer ou exploiter : vrai ou faux

<details><summary>Indice 1</summary>

Relis le §7 de la fiche.

</details>
<details><summary>Indice 2</summary>

Le regret est une somme de termes positifs ; ε-greedy choisit chaque option avec une probabilité au moins $\frac{\varepsilon}{K}$.

</details>
<details><summary>Indice 3</summary>

4 : Thompson **tire** une valeur dans chaque loi a posteriori. 6 : le regret compare les **moyennes**, pas les récompenses tirées.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M11.R1 — Implication et contraposée (R4)

<details><summary>Indice 1</summary>

Relis R4 §2 et §6 (raisonnement par contraposée).

</details>
<details><summary>Indice 2</summary>

La contraposée de « si $n^2$ est divisible par 3, alors $n$ l'est » est « si $n$ n'est pas divisible par 3, alors $n^2$ ne l'est pas ».

</details>
<details><summary>Indice 3</summary>

4 : développe $(3k + 1)^2$ et $(3k + 2)^2$ et regarde le reste de la division par 3. 5 : $x^2 + 1 - 2x = (x - 1)^2$.

</details>

### M11.R2 — Espérance et variance (M02b)

<details><summary>Indice 1</summary>

Relis M02b, les lois usuelles, et la variance d'une somme.

</details>
<details><summary>Indice 2</summary>

Exponentielle de paramètre $\lambda$ : $\frac{1}{\lambda}$ et $\frac{1}{\lambda^2}$. Bernoulli : $p$ et $p(1 - p)$.

</details>
<details><summary>Indice 3</summary>

2 : $p(1 - p)$ est un trinôme en $p$, maximal au milieu de ses racines. 4 : $\mathbb{V}(\bar{X}) = \frac{1}{n^2} \times n\sigma^2$.

</details>

### M11.R3 — La loi Beta a posteriori (M04)

<details><summary>Indice 1</summary>

Relis M04, la loi Beta et la conjugaison.

</details>
<details><summary>Indice 2</summary>

A priori $\mathrm{Beta}(1, 1)$, puis $s$ succès et $f$ échecs : $\mathrm{Beta}(1 + s, 1 + f)$ ; moyenne $\frac{a}{a + b}$.

</details>
<details><summary>Indice 3</summary>

1 : $\mathrm{Beta}(5, 7)$. 4 : ajoute 30 et 30 aux paramètres ; la variance diminue quand $a + b$ grandit. 5 : `rng.beta(a, b)`.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M11.1 — Tables de vérité : modus ponens, modus tollens et l'affirmation du conséquent

<details><summary>Indice 1</summary>

Relis « Argument, validité, solidité » et le tableau des quatre formes (fiche §1).

</details>
<details><summary>Indice 2</summary>

Pour chaque argument, écris une colonne par prémisse et une pour la conclusion ; garde seulement les lignes où toutes les prémisses sont vraies.

</details>
<details><summary>Indice 3</summary>

b) Ligne 1 (VV) : $P \Rightarrow Q$ vraie, $Q$ vraie : les deux prémisses sont vraies ; fais de même pour les lignes 2 à 4. f) Les huit lignes, dans l'ordre VVV, VVF, …, FFF. i) Avec $P$ vraie et $R$ fausse, la première prémisse n'est vraie que si « $P$ et $Q$ » est faux.

</details>

### Ex M11.2 — Nier des phrases quantifiées sur des modèles et des features

<details><summary>Indice 1</summary>

Relis « Négation et contre-exemple » (fiche §1) et R4 §3.

</details>
<details><summary>Indice 2</summary>

Un « pour tout » se réfute par une case ; un « il existe » se prouve par un témoin. Dans « pour chaque dataset, il existe un modèle », le modèle peut changer d'une colonne à l'autre.

</details>
<details><summary>Indice 3</summary>

a) La colonne du dataset 3 contient 0,79 : $S_1$ est fausse ; cherche les autres cases sous 0,80. e) Cherche une **ligne** entière au-dessus de 0,90. h) Cherche une **colonne** entière au-dessus de 0,84.

</details>

### Ex M11.3 — Des phrases traduites en inclusions d'ensembles, et un contre-exemple

<details><summary>Indice 1</summary>

Relis « Une phrase, une inclusion » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Écris les ensembles en extension : $A = \{6, 12, 18, 24, 30\}$, puis $B$, $P$ et $Q$.

</details>
<details><summary>Indice 3</summary>

c) et d) Les contre-exemples de « $B \subset A$ » sont les éléments de $B \setminus A$. g) Les multiples de 4 qui sont aussi multiples de 6 sont les multiples de 12. h) La formule du cardinal d'une réunion.

</details>

### Ex M11.4 — Une induction trompeuse par oubli du taux de base, recalculée avec Bayes

<details><summary>Indice 1</summary>

Relis « Piège 2 : oublier le taux de base » (fiche §3), et M03 pour Bayes.

</details>
<details><summary>Indice 2</summary>

Raisonne sur 10 000 capteurs : 300 défectueux, dont combien signalés ? 9 700 bons, dont combien signalés ?

</details>
<details><summary>Indice 3</summary>

a) $0{,}03 \times 0{,}92 + 0{,}97 \times 0{,}06$. e) Le nouveau taux de base est la réponse de b) : refais le même calcul avec lui. f) Résous $0{,}92\,\pi = 0{,}06\,(1 - \pi)$.

</details>

### Ex M11.5 — Markov : la queue d'une durée positive

<details><summary>Indice 1</summary>

Relis le §4 de la fiche : l'énoncé, puis « Ce que la borne vaut ».

</details>
<details><summary>Indice 2</summary>

La borne est $\min(1, \frac{\mathbb{E}[T]}{a})$ ; une exponentielle de moyenne $\mu$ a pour queue $P(T \ge a) = e^{-a/\mu}$.

</details>
<details><summary>Indice 3</summary>

a) $\frac{1{,}5}{6}$. f) La loi qui atteint la borne met la probabilité $p$ en 6, avec $6p = 1{,}5$. h) Applique Markov à $T^2$ et au seuil $36$.

</details>

### Ex M11.6 — Tchebychev : combien d'observations pour une moyenne à ± 0,1 ?

<details><summary>Indice 1</summary>

Relis « La moyenne de $n$ variables » et « Borner une variance inconnue » (fiche §5).

</details>
<details><summary>Indice 2</summary>

$P(\lvert \bar{X} - \mu \rvert \ge t) \le \frac{\sigma^2}{n t^2}$ ; il suffit que $n \ge \frac{\sigma^2}{\delta t^2}$.

</details>
<details><summary>Indice 3</summary>

a) Une variable dans $[a, b]$ a une variance au plus $\frac{(b - a)^2}{4}$. c) $\sigma^2 = 0{,}09$. e) Remplace $t$ par $\frac{3\sigma}{\sqrt{n}}$ dans la borne.

</details>

### Ex M11.7 — Hoeffding : rayon de confiance et taille d'échantillon d'une proportion

<details><summary>Indice 1</summary>

Relis « Le rayon de confiance, et la taille d'échantillon » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Rayon bilatéral : $\sqrt{\frac{\ln(2/\delta)}{2n}}$ pour des variables dans $[0, 1]$ ; taille : $n \ge \frac{\ln(2/\delta)}{2r^2}$, arrondie au-dessus.

</details>
<details><summary>Indice 3</summary>

a) $\sqrt{\frac{\ln 40}{2\,000}}$. h) Le rayon unilatéral remplace $\ln(2/\delta)$ par $\ln(1/\delta)$. f) Tchebychev avec $\sigma^2 = \frac{1}{4}$.

</details>

### Ex M11.8 — Trois bornes pour une même question : Markov, Tchebychev, Hoeffding, et l'approximation normale

<details><summary>Indice 1</summary>

Relis les §4 à §6, puis M02c pour l'approximation normale.

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[S] = 20$, $\mathbb{V}(S) = 16$ ; $S \ge 30$ équivaut à $\bar{X} - 0{,}2 \ge 0{,}1$.

</details>
<details><summary>Indice 3</summary>

a) $\frac{20}{30}$. c) $e^{-2 \times 100 \times 0{,}1^2}$. d) $z = \frac{30 - 20}{4}$, puis $P(Z \ge z)$. h) Résous $e^{-2n \times 0{,}01} \le 0{,}01$.

</details>

### Ex M11.9 — D'où vient le bonus d'UCB : Hoeffding avec un risque qui décroît avec t

<details><summary>Indice 1</summary>

Relis « UCB : une borne supérieure de confiance par option » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Le rayon unilatéral est $\sqrt{\frac{\ln(1/\delta)}{2N}}$ ; avec $\delta_t = t^{-4}$, $\ln(1/\delta_t) = 4\ln t$.

</details>
<details><summary>Indice 3</summary>

a) $\sqrt{\frac{\ln 100}{100}}$. f) Résous $\sqrt{\frac{2\ln t}{N}} < 0{,}1$ en $N$. g) $\sum_{t \ge 1} t^{-4} = \frac{\pi^4}{90}$ : retire le premier terme.

</details>

### Ex M11.10 — ε-greedy : la loi du bras joué et le regret attendu par pas

<details><summary>Indice 1</summary>

Relis « ε-greedy : la loi de l'option choisie » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$P(A_t = k) = (1 - \varepsilon)\,\mathbf{1}_{k = g} + \frac{\varepsilon}{K}$ ; le regret d'un pas est $\sum_k \Delta_k\,P(A_t = k)$, avec $\Delta_k = 0{,}62 - \mu_k$.

</details>
<details><summary>Indice 3</summary>

a) $0{,}85 + 0{,}03$. c) Les écarts valent $(0{,}07 ;\ 0{,}32 ;\ 0 ;\ 0{,}14 ;\ 0{,}12)$. f) Le regret du pas $t$ vaut $\frac{1}{t} \times \frac{0{,}65}{5}$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M11.11 — L'inégalité de Markov

<details><summary>Indice 1</summary>

Relis la « preuve par une indicatrice » (fiche §4).

</details>
<details><summary>Indice 2</summary>

1 : deux cas, $X \ge a$ et $X < a$ ; puis la monotonie et la linéarité de l'espérance, et $\mathbb{E}[\mathbf{1}_A] = P(A)$.

</details>
<details><summary>Indice 3</summary>

3 : une variable qui vaut $\pm 10$. 4 : si $\varphi$ est croissante, $X \ge a$ entraîne $\varphi(X) \ge \varphi(a)$ ; applique la question 1 à $\varphi(X) \ge 0$.

</details>

### Ex M11.12 — Tchebychev à partir de Markov, puis la loi faible des grands nombres

<details><summary>Indice 1</summary>

Relis le §5 de la fiche, et M02c §4.

</details>
<details><summary>Indice 2</summary>

1 : Markov pour $(X - \mu)^2$ au seuil $t^2$. 3 : la variance d'une somme de variables indépendantes est la somme des variances.

</details>
<details><summary>Indice 3</summary>

5 : développe $\mathbb{E}[(X - \mu + \mu - c)^2]$, puis prends $c = \frac{a + b}{2}$ : $\lvert X - c \rvert \le \frac{b - a}{2}$.

</details>

### Ex M11.13 — Avec ε fixé, le regret attendu d'ε-greedy croît au moins linéairement

<details><summary>Indice 1</summary>

Relis « Le problème, et ce qu'on mesure » et « ε-greedy » (fiche §7).

</details>
<details><summary>Indice 2</summary>

1 : $\mathbb{E}[\mu^\star - \mu_{A_t}] = \sum_k (\mu^\star - \mu_k)\,P(A_t = k)$ ; $N_k(T) = \sum_t \mathbf{1}_{A_t = k}$. 2 : le tirage au hasard donne déjà $\frac{\varepsilon}{K}$.

</details>
<details><summary>Indice 3</summary>

4 : pour $t \ge 2$, $\frac{1}{t} \le \int_{t-1}^{t} \frac{dx}{x}$ ; somme de $t = 2$ à $T$. 5 : que vaut le regret des pas où le choix glouton est faux ?

</details>

<a id="reflexion"></a>

## 🔗 ⚖️ 🗣️ Pont, esprit critique et explication

### Ex M11.14 — Pont : combien d'exemples de test pour connaître une accuracy à ± 2 points, garanti par Hoeffding ?

<details><summary>Indice 1</summary>

Relis le §6 de la fiche : le rayon, la taille d'échantillon, la borne de l'union.

</details>
<details><summary>Indice 2</summary>

Une accuracy est la moyenne de variables 0 ou 1 : $[a, b] = [0, 1]$.

</details>
<details><summary>Indice 3</summary>

a) $n \ge \frac{\ln 40}{2 \times 0{,}02^2}$, arrondi au-dessus. d) Le risque de chacun devient $\frac{0{,}05}{20}$, dans le logarithme. e) $1{,}96\sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$.

</details>

### Ex M11.15 — Corrélation, causalité et induction : trois titres de presse à démonter

<details><summary>Indice 1</summary>

Relis « Piège 3 » et « Piège 4 » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Pour chaque titre : qui a formé les groupes comparés ? Une troisième variable peut-elle agir sur les deux ? La cause peut-elle aller dans l'autre sens ?

</details>
<details><summary>Indice 3</summary>

Titre 1 : le revenu, l'âge ou le climat d'une ville peuvent jouer sur les pistes et sur la santé. Pour trancher : une expérience où le hasard décide qui est « traité ».

</details>

### Ex M11.16 — Expliquer « l'optimisme face à l'incertitude » à partir d'un intervalle de confiance

<details><summary>Indice 1</summary>

Relis « UCB » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Un vin goûté deux fois a un intervalle large : sa borne haute peut dépasser celle des autres.

</details>
<details><summary>Indice 3</summary>

Plan : l'intervalle de chaque vin ; on choisit la borne haute la plus haute ; un vin peu goûté a sa chance ; un mauvais vin, une fois bien connu, a une borne haute basse.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M11.E1 — « À quoi sert l'inégalité de Hoeffding en apprentissage, et que suppose-t-elle ? »

<details><summary>Indice 1</summary>

Relis le §6 de la fiche, et M11.14.

</details>
<details><summary>Indice 2</summary>

Un plan : l'énoncé en mots, un usage (jeu de test, rayon d'une accuracy, UCB), les trois hypothèses, la comparaison avec le TCL.

</details>
<details><summary>Indice 3</summary>

Les hypothèses : variables indépendantes, bornées dans un intervalle connu d'avance, quantité fixée avant de regarder (sinon la borne de l'union).

</details>

<a id="notebook"></a>

## Notebook

### Ex M11.17 — Les bornes de Markov et de Tchebychev · `markov_bound, chebyshev_bound`

<details><summary>Indice 1</summary>

Relis les énoncés des §4 et §5 de la fiche, et les docstrings.

</details>
<details><summary>Indice 2</summary>

D'abord les contrôles (`raise ValueError(...)`), puis une division, puis `min(1.0, ...)`, converti en `float`.

</details>
<details><summary>Indice 3</summary>

Pour `markov_bound` : `if mean < 0:` lève une `ValueError`, de même `if a <= 0:` ; la valeur rendue est `float(min(1.0, mean / a))`. Même schéma pour `chebyshev_bound`, avec `t ** 2`.

</details>

### Ex M11.18 — La borne et le rayon de Hoeffding · `hoeffding_bound, hoeffding_radius`

<details><summary>Indice 1</summary>

Relis « L'énoncé » et « Le rayon de confiance » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Les deux fonctions partagent deux contrôles (`n < 1`, `a >= b`) : une petite fonction auxiliaire évite de les écrire deux fois.

</details>
<details><summary>Indice 3</summary>

La borne : `2 * math.exp(-2 * n * t ** 2 / (b - a) ** 2)`, plafonnée à 1. Le rayon : `(b - a) * math.sqrt(...)`, avec `math.log(2 / delta)` sous la racine.

</details>

### Ex M11.19 — La queue empirique d'un échantillon · `empirical_tail`

<details><summary>Indice 1</summary>

Relis « La queue empirique » (fiche §4).

</details>
<details><summary>Indice 2</summary>

`np.asarray(samples, dtype=float)` ; un échantillon vide a une taille (`.size`) nulle.

</details>
<details><summary>Indice 3</summary>

La moyenne d'un tableau de booléens est la proportion des `True` : `np.mean(values >= threshold)`, convertie en `float`.

</details>

### Ex M11.20 — Les vraies queues d'une loi exponentielle et d'une binomiale (`scipy.stats`) contre les bornes

<details><summary>Indice 1</summary>

Relis le §4 de la fiche (la queue d'une exponentielle) et la documentation de `scipy.stats` (méthodes `sf`, `isf`, `cdf`).

</details>
<details><summary>Indice 2</summary>

`stats.expon(scale=3)` est la loi exponentielle de moyenne 3 ; pour une loi discrète, `sf(k)` vaut $P(S > k)$.

</details>
<details><summary>Indice 3</summary>

a) `stats.expon(scale=3).sf(15)`. c) `.isf(0.01)`. d) `S.cdf(9) + S.sf(20)` avec `S = stats.binom(60, 0.25)`.

</details>

### Ex M11.21 — Prédire : laquelle des trois bornes est la plus serrée pour n = 100 ?

<details><summary>Indice 1</summary>

Relis les §4 à §6 : chaque borne utilise une information différente (la moyenne, la variance, l'intervalle).

</details>
<details><summary>Indice 2</summary>

Calcule de tête l'ordre de grandeur de chacune : $\frac{p}{p + t}$, $\frac{p(1 - p)}{100\,t^2}$, $e^{-200t^2}$.

</details>
<details><summary>Indice 3</summary>

Quand $t$ est grand, l'exponentielle écrase tout ; quand $p$ est minuscule, la variance aussi.

</details>

### Ex M11.22 — La fréquence des écarts |x̄ − p| ≥ t comparée à la borne de Hoeffding, quand n grandit

<details><summary>Indice 1</summary>

Relis le §6 de la fiche ; `rng.binomial(n, p, size=reps)` tire `reps` nombres de succès d'un coup.

</details>
<details><summary>Indice 2</summary>

La proportion des `True` d'un tableau de booléens est sa moyenne ; `k / n` est la moyenne de chaque échantillon.

</details>
<details><summary>Indice 3</summary>

`k = rng.binomial(n, p, size=reps)`, puis la proportion des échantillons tels que `np.abs(k / n - p) >= t`.

</details>

### Ex M11.23 — La probabilité qu'un tirage d'une loi Beta dépasse celui d'une autre, par simulation

<details><summary>Indice 1</summary>

Relis « L'échantillonnage de Thompson » (fiche §7), et `integrate.quad`.

</details>
<details><summary>Indice 2</summary>

Simulation : deux tableaux de tirages, dans l'ordre de l'énoncé, puis la proportion des `x2 > x1`. Intégrale : $\int_0^1 f_2(x) F_1(x)\,dx$.

</details>
<details><summary>Indice 3</summary>

`value, error = integrate.quad(lambda x: stats.beta(a2, b2).pdf(x) * stats.beta(a1, b1).cdf(x), 0, 1)`. b) Pour $\theta_1$ uniforme, $P(\theta_1 < \theta_2) = \mathbb{E}[\theta_2]$.

</details>

### Ex M11.24 — Les bornes de Markov, de Tchebychev et de Hoeffding contre la vraie queue, en échelle log

<details><summary>Indice 1</summary>

Relis les §4 à §6 et M11.21.

</details>
<details><summary>Indice 2</summary>

Quatre listes de valeurs, une par courbe, calculées pour chaque $t$ de `ts` ; `np.minimum(1.0, ...)` plafonne un tableau.

</details>
<details><summary>Indice 3</summary>

La vraie queue : pour chaque `t`, `k = math.ceil(n * (p + t) - 1e-9)` puis `stats.binom.sf(k - 1, n, p)`. Puis `ax.plot(ts, valeurs, label=...)` quatre fois, `ax.set_yscale('log')`, `ax.legend()`.

</details>

### Ex M11.25 — Chasse à l'erreur : Markov pour une variable négative, Hoeffding sans bornes, un rayon sans racine

<details><summary>Indice 1</summary>

Relis le récapitulatif des pièges de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, vérifie les hypothèses de l'inégalité qu'elle utilise, et la formule : facteur 2, $(b - a)^2$, racine carrée.

</details>
<details><summary>Indice 3</summary>

Trois lignes sont fausses. b) et c) : les variations sont dans $[-5, 5]$, donc $b - a = 10$.

</details>

### Ex M11.26 — Un test paramétré qui vérifie l'inégalité de Markov sur dix lois

<details><summary>Indice 1</summary>

Relis « Ce que la borne vaut » (fiche §4) : quelle loi atteint la borne ?

</details>
<details><summary>Indice 2</summary>

Un dictionnaire de dix lois gelées de `scipy.stats`, une boucle sur des seuils non entiers, un `assert` avec un message.

</details>
<details><summary>Indice 3</summary>

Pour qu'une borne trop petite échoue, il faut une loi où Markov est presque atteinte, comme `stats.bernoulli(0.9)` à un seuil juste sous 1 ; pour la borne exponentielle, une loi à queue lourde (`stats.pareto(1.2)`, `stats.lognorm(1.5)`).

</details>

### Ex M11.27 — Défi : la plus petite taille d'échantillon qui garantit une moyenne à ± 0,05 avec 99 %, vérifiée sur une loi défavorable

<details><summary>Indice 1</summary>

Commence par la probabilité exacte pour un $n$ : `stats.binom.pmf(k, n, 0.5)` sur `k = np.arange(n + 1)`, puis la somme des $k$ « loin » de $\frac{n}{2}$.

</details>
<details><summary>Indice 2</summary>

Pour éviter les flottants, écris la condition $\lvert \frac{k}{n} - \frac{1}{2} \rvert \ge \frac{1}{20}$ avec des entiers : $10\,\lvert 2k - n \rvert \ge n$.

</details>
<details><summary>Indice 3</summary>

Calcule la probabilité pour tous les $n$ de 1 à 3 000 (une seconde ou deux), puis pars de 3 000 et descends tant que la propriété tient : le dernier $n$ atteint est $n_0$.

</details>
