# R8 · Probabilités de base — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🧮 🗣️ Pont, estimation, explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R8.Q1 — Univers, issue, événement

<details><summary>Indice 1</summary>

Relis « Issues et univers » et « Événements » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Une issue est un résultat précis de l'expérience ; un événement est un ensemble d'issues. Pour un contraire, demande-toi ce qui reste quand l'événement n'a pas lieu.

</details>
<details><summary>Indice 3</summary>

1 : chaque lancer double le nombre de suites. Pour 5, cherche deux événements sans issue commune qui ne couvrent pas tout l'univers. Pour 6, écris $A$ et $B$ comme des ensembles de numéros.

</details>

### R8.Q2 — Propriétés d'une probabilité

<details><summary>Indice 1</summary>

Relis « Définition » et « Équiprobabilité » (fiche §2), avec son encadré ⚠️.

</details>
<details><summary>Indice 2</summary>

Une probabilité est entre 0 et 1 ; $P(\bar{A}) = 1 - P(A)$ ; $P(A \cup B) = P(A) + P(B) - P(A \cap B)$. Pour 5, distingue l'aîné et le cadet.

</details>
<details><summary>Indice 3</summary>

1 : non, et non. Pour 5, liste les 4 issues équiprobables (aîné, cadet). Pour 6, une probabilité dit ce qui arrive **en moyenne**, pas à coup sûr.

</details>

### R8.Q3 — Arrangement ou combinaison ?

<details><summary>Indice 1</summary>

Relis « Le principe multiplicatif », « La factorielle », « Les combinaisons » et l'encadré ⚠️ « Ordre ou pas ordre ? » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Deux questions pour chaque situation : deux choix qui ne diffèrent que par l'ordre comptent-ils pour un ou pour deux ? Un même objet peut-il revenir ?

</details>
<details><summary>Indice 3</summary>

1 : l'or et l'argent ne sont pas interchangeables, donc l'ordre compte, et un coureur n'occupe qu'une place : un arrangement. Pose les deux mêmes questions pour les autres.

</details>

### R8.Q4 — Lire un arbre pondéré

<details><summary>Indice 1</summary>

Relis « Enchaîner des épreuves » et « Un premier contact avec le conditionnement » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Dessine l'arbre : deux branches (A, B), puis deux branches après chacune (germe, ne germe pas). Les branches issues d'un même nœud ont une somme de 1.

</details>
<details><summary>Indice 3</summary>

1 : $1 - 0{,}9$. Pour 3, deux chemins mènent à « germe » : additionne leurs probabilités, chacune étant un produit.

</details>

### R8.Q5 — Indépendants ou incompatibles ?

<details><summary>Indice 1</summary>

Relis la définition et l'encadré ⚠️ du §5.

</details>
<details><summary>Indice 2</summary>

Incompatibles : $P(A \cap B) = 0$. Indépendants : $P(A \cap B) = P(A)\,P(B)$. Compare les deux définitions quand $P(A)$ et $P(B)$ ne sont pas nulles.

</details>
<details><summary>Indice 3</summary>

1 : « 1 » et « 6 » ne peuvent pas arriver ensemble ; compare $0$ et $\frac{1}{6} \times \frac{1}{6}$. Pour 5, calcule $P(A)\,P(B)$. Pour 6, la composition du jeu change-t-elle après le premier tirage ?

</details>

### R8.Q6 — Espérance et variance : vrai ou faux

<details><summary>Indice 1</summary>

Relis le §7 : « L'espérance », « La variance et l'écart-type », « Changer d'échelle ».

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[aX + b] = a\,\mathbb{E}[X] + b$ et $\mathbb{V}(aX + b) = a^2\,\mathbb{V}(X)$ ; une variance est une moyenne de carrés.

</details>
<details><summary>Indice 3</summary>

1 : pense à une variable qui vaut 0 ou 1 avec une chance sur deux. Pour 5 et 6, applique la formule de $\mathbb{V}(aX + b)$ avec les bons $a$ et $b$.

</details>

### R8.Q7 — Ce que dit la loi des grands nombres

<details><summary>Indice 1</summary>

Relis « La loi des grands nombres » et l'encadré ⚠️ « Le hasard n'a pas de mémoire » (fiche §8).

</details>
<details><summary>Indice 2</summary>

La loi parle de la **fréquence**, pas du nombre de succès ; elle dit que la fréquence se rapproche de la probabilité, pas qu'elle l'atteint. Les écarts diminuent comme $\frac{1}{\sqrt{n}}$.

</details>
<details><summary>Indice 3</summary>

1 : les lancers sont indépendants (§5). Pour 4, cherche le nombre dont la racine carrée vaut 10. Pour 5, relis « Un générateur et une graine ».

</details>

<a id="rappels"></a>

## 🔁 Rappels

### R8.R1 — Ensembles et complémentaire (R4)

<details><summary>Indice 1</summary>

Relis les opérations sur les ensembles de R4.

</details>
<details><summary>Indice 2</summary>

$A \cap B$ : les éléments communs ; $A \cup B$ : ceux de l'un ou de l'autre ; $\bar{A}$ : ceux de $\Omega$ qui ne sont pas dans $A$.

</details>
<details><summary>Indice 3</summary>

1 : $c$ est le seul élément commun. Pour 4, liste les éléments qui ne sont ni dans $A$ ni dans $B$, puis compare avec le complémentaire de $A \cup B$.

</details>

### R8.R2 — Σ et Π (R4)

<details><summary>Indice 1</summary>

Relis les notations Σ et Π de R4.

</details>
<details><summary>Indice 2</summary>

Écris la somme ou le produit terme à terme, en remplaçant l'indice par chacune de ses valeurs, puis calcule.

</details>
<details><summary>Indice 3</summary>

1 : $1^2 + 2^2 + 3^2 + 4^2$. Pour 4, les trois facteurs sont $1 - \frac{1}{10}$, $1 - \frac{2}{10}$ et $1 - \frac{3}{10}$.

</details>

### R8.R3 — Fractions (R1)

<details><summary>Indice 1</summary>

Relis les opérations sur les fractions de R1.

</details>
<details><summary>Indice 2</summary>

Produit : on multiplie les numérateurs et les dénominateurs ; somme : on réduit au même dénominateur ; on simplifie à la fin.

</details>
<details><summary>Indice 3</summary>

1 : $\frac{2 \times 1}{6 \times 5}$, puis simplifie. Pour 4, cherche combien de fois 84 va dans 504.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R8.1 — Décrire univers et événements : dés, cartes, pièces

<details><summary>Indice 1</summary>

Relis « Issues et univers » et « Événements » (fiche §1), et la formule $\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert$ (R4).

</details>
<details><summary>Indice 2</summary>

Pour les pièces, une issue est une suite de quatre lettres ; liste-les, ou compte avec le principe multiplicatif. Pour « au moins un », passe par le contraire. Pour les cartes, compte $A$, $B$ et $A \cap B$ d'abord.

</details>
<details><summary>Indice 3</summary>

a : $2 \times 2 \times 2 \times 2$. Pour b, choisis la position des deux P. Pour g, « ni as ni noire » est le contraire de $A \cup B$.

</details>

### Ex R8.2 — Probabilités par équiprobabilité

<details><summary>Indice 1</summary>

Relis « Équiprobabilité » (fiche §2) et « Au moins un : passer par le contraire ».

</details>
<details><summary>Indice 2</summary>

Compte les issues favorables et les issues possibles. Pour les deux dés, une issue est un couple (dé à 6 faces, dé à 4 faces) : dresse le tableau des 24 couples.

</details>
<details><summary>Indice 3</summary>

a : il y a deux B parmi 11 lettres. Pour g, compte, pour chaque valeur du dé à 4 faces, les valeurs du dé à 6 faces qui la dépassent strictement. Pour h, le produit est impair seulement si les deux nombres le sont.

</details>

### Ex R8.3 — P(A ∪ B) et le complémentaire

<details><summary>Indice 1</summary>

Relis « Définition » (fiche §2) : les règles du complémentaire et de la réunion ; et les lois de De Morgan (R4).

</details>
<details><summary>Indice 2</summary>

« Ni $A$ ni $B$ » est le contraire de « $A$ ou $B$ » ; « $A$ mais pas $B$ » est $A$ privé de $A \cap B$. Dans chaque question, écris la formule de la réunion et repère l'inconnue.

</details>
<details><summary>Indice 3</summary>

a : $0{,}45 + 0{,}3 - 0{,}15$. Pour f, la probabilité de « l'appli ou la newsletter » est le contraire de « ni l'une ni l'autre ». Pour h, isole $P(A \cap B)$ dans la formule de la réunion.

</details>

### Ex R8.4 — Principe multiplicatif et factorielles

<details><summary>Indice 1</summary>

Relis « Le principe multiplicatif » et « La factorielle » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Pour chaque position, combien de possibilités ? Avec répétition, toujours autant ; sans répétition, une de moins à chaque étape. Une factorielle se simplifie avec une autre plus petite.

</details>
<details><summary>Indice 3</summary>

a : $26^6$. Pour d, il y a 8 possibilités pour l'or, puis 7 pour l'argent, puis 6 pour le bronze. Pour f, la tâche A n'a qu'une place possible.

</details>

### Ex R8.5 — Combinaisons et triangle de Pascal

<details><summary>Indice 1</summary>

Relis « Les combinaisons » et « Le triangle de Pascal » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\binom{n}{k} = \frac{n(n - 1)\cdots(n - k + 1)}{k!}$ ; $\binom{n}{k} = \binom{n}{n - k}$ ; chaque nombre du triangle est la somme des deux au-dessus ; la somme de la ligne $n$ vaut $2^n$.

</details>
<details><summary>Indice 3</summary>

a : $\frac{7 \times 6 \times 5}{3 \times 2 \times 1}$. Pour b, une poignée de main est une paire de personnes. Pour g, combien de mains contiennent les 4 as ? Pour h, un chemin est une suite de 8 pas, dont 4 vers la droite.

</details>

### Ex R8.6 — Arbres pondérés : tirages successifs

<details><summary>Indice 1</summary>

Relis le §4 : « Enchaîner des épreuves » et « Tirages avec ou sans remise ».

</details>
<details><summary>Indice 2</summary>

Dessine l'arbre de chaque expérience. Sans remise, la seconde branche tient compte de la chaussette déjà sortie. Pour « au moins une », passe par le contraire.

</details>
<details><summary>Indice 3</summary>

a : $0{,}6 \times 0{,}1$. Pour d, $\frac{4}{10}$ puis $\frac{3}{9}$. Pour f, deux chemins mènent à « la seconde est noire » : noire puis noire, grise puis noire.

</details>

### Ex R8.7 — Indépendance : tester P(A ∩ B) = P(A) P(B) avec des cartes et des pièces

<details><summary>Indice 1</summary>

Relis la définition du §5 et son encadré ⚠️.

</details>
<details><summary>Indice 2</summary>

Pour chaque couple, calcule $P(A \cap B)$ en comptant les issues communes, puis compare avec le produit $P(A)\,P(B)$ : égalité exacte, ou pas.

</details>
<details><summary>Indice 3</summary>

a : une seule carte est à la fois un as et un cœur. Pour e, $F$ = {PP, FF}. Pour g, liste les suites de trois lancers qui commencent par P et ont au moins deux P.

</details>

### Ex R8.8 — La loi d'une variable aléatoire

<details><summary>Indice 1</summary>

Relis « La loi d'une variable aléatoire » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Pour chaque valeur, compte les issues qui la donnent, puis divise par le nombre d'issues. La somme d'une loi vaut 1 : vérifie-la.

</details>
<details><summary>Indice 3</summary>

a : sur les 8 suites, une seule a zéro pile. Pour c, dresse le tableau des 16 couples et écris le plus grand numéro dans chaque case. Pour g, compte les as, les figures et les autres cartes.

</details>

### Ex R8.9 — Espérance, variance (avec V = E[X²] − E[X]²) et écart-type

<details><summary>Indice 1</summary>

Relis le §7 : l'espérance, la formule $\mathbb{V}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2$ et « Changer d'échelle ».

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[X] = \sum x\,P(X = x)$ ; $\mathbb{E}[X^2] = \sum x^2\,P(X = x)$ ; puis la variance, l'écart-type, et les formules de $aX + b$.

</details>
<details><summary>Indice 3</summary>

a : $0 \times 0{,}2 + 1 \times 0{,}4 + 2 \times 0{,}3 + 3 \times 0{,}1$. Pour f, $a = 10$ et la constante $-4$ disparaît. Pour g et h, reprends la loi de $Y$ trouvée en R8.8 c, en fractions.

</details>

### Ex R8.10 — Un jeu est-il équitable ?

<details><summary>Indice 1</summary>

Relis « Un jeu équitable » et la variance (fiche §7).

</details>
<details><summary>Indice 2</summary>

Écris la loi du prix de chaque jeu (valeurs et probabilités), puis son espérance et sa variance. Le gain net est le prix moins la mise ; un jeu est équitable quand l'espérance du gain net est nulle.

</details>
<details><summary>Indice 3</summary>

a : deux piles ont la probabilité $\frac{1}{4}$, un seul pile $\frac{1}{2}$. Pour d, calcule $\mathbb{E}[W^2]$, puis retire $\mathbb{E}[W]^2$. Pour h, écris que l'espérance du prix est égale à la mise.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R8.11 — Démontrer C(n, k) = C(n − 1, k − 1) + C(n − 1, k)

<details><summary>Indice 1</summary>

Relis « Les combinaisons » et « Le triangle de Pascal » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Par le calcul : réduis les deux fractions au dénominateur $k!\,(n - k)!$, puis additionne. Par le comptage : partage les choix selon qu'ils contiennent ou non le premier objet.

</details>
<details><summary>Indice 3</summary>

2 : $\frac{(n - 1)!}{(k - 1)!\,(n - k)!} = \frac{(n - 1)! \times k}{k!\,(n - k)!}$ ; fais de même pour le second terme, puis factorise $(n - 1)!$. Pour 4, que compte $\sum_k \binom{n}{k}$ ? Chaque élément est pris ou non.

</details>

### Ex R8.12 — L'espérance d'une somme : E[X + Y] = E[X] + E[Y], même pour des variables liées

<details><summary>Indice 1</summary>

Relis « L'espérance » et « Linéarité » (fiche §7), et les règles des sommes Σ (R4).

</details>
<details><summary>Indice 2</summary>

Écris $\mathbb{E}[X + Y]$ comme une somme sur les issues : $\sum_\omega \big(X(\omega) + Y(\omega)\big)\,p(\omega)$, puis sépare la somme. Pour 4, une somme de variables qui valent 0 ou 1 compte des succès.

</details>
<details><summary>Indice 3</summary>

1 : écris la valeur de $X$ pour chacune des 8 suites, puis regroupe celles qui donnent la même valeur. Pour 3, une constante $c$ est une variable qui vaut $c$ pour toute issue. Pour 5, $X$ ne vaut que 0 ou 1 : que vaut $X \times X$ ?

</details>

<a id="reflexion"></a>

## 🔗 🧮 🗣️ Pont, estimation, explication

### Ex R8.13 — Comparer toutes les paires : un tournoi, C(n, 2) et une croissance en n²

<details><summary>Indice 1</summary>

Relis « Les combinaisons » (fiche §3) : $\binom{n}{2} = \frac{n(n - 1)}{2}$ compte les paires.

</details>
<details><summary>Indice 2</summary>

Un match, ou une comparaison, par **paire** : $\binom{n}{2}$. Un match aller et retour compte les couples ordonnés. Pour e, convertis des microsecondes en secondes, puis en heures.

</details>
<details><summary>Indice 3</summary>

a : $\frac{16 \times 15}{2}$. Pour d, écris le rapport des deux formules, et simplifie. Pour f, un groupe de 3 est une combinaison de 3 exemples parmi 100.

</details>

### Ex R8.14 — Fermi : la probabilité de croiser quelqu'un que l'on connaît dans le métro

<details><summary>Indice 1</summary>

Relis « Au moins un : passer par le contraire » (fiche §2) et « Répéter une épreuve » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Écris chaque hypothèse avec un ordre de grandeur, calcule $q$ comme un rapport, puis passe par le contraire : la probabilité de ne croiser **aucune** connaissance sur $N$ voyageurs est $(1 - q)^N$.

</details>
<details><summary>Indice 3</summary>

Par exemple : 300 personnes connues, dont 30 dans le métro un jour donné, 4 millions d'usagers, donc $q \approx \frac{30}{4 \times 10^6}$. Pour 4, développe $(1 - q)^2 = 1 - 2q + q^2$ et regarde le terme $q^2$ quand $q$ est minuscule.

</details>

### Ex R8.15 — Expliquer la différence entre probabilité et fréquence

<details><summary>Indice 1</summary>

Relis le début du §2 et « La loi des grands nombres » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Une probabilité se dit **avant** d'observer ; une fréquence se mesure **après**, sur une série. Puis dis ce qui les relie quand les répétitions sont nombreuses.

</details>
<details><summary>Indice 3</summary>

Par exemple : « 30 %, c'est une prévision ; 7 sur 10, c'est un constat » ; puis la loi des grands nombres, et le fait que demain n'arrive qu'une fois.

</details>

<a id="notebook"></a>

## Notebook

### Ex R8.16 — Factorielle et combinaisons · `factorial`, `binomial`

<details><summary>Indice 1</summary>

Relis « La factorielle » et « Les combinaisons » (fiche §3), et les docstrings des deux fonctions.

</details>
<details><summary>Indice 2</summary>

`factorial` : le cas interdit (`n < 0`) avec `raise ValueError(...)`, puis un produit qui part de 1. `binomial` : 0 hors de $0 \le k \le n$, puis le produit de $k$ facteurs divisé par $k!$, avec la division entière `//`.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
result = 1
for i in range(1, k + 1):
    result = result * (n - k + i) // i
```
Chaque étape donne un entier exact (c'est $\binom{n - k + i}{i}$).

</details>

### Ex R8.17 — Une probabilité exacte par énumération · `enumerate_probability`

<details><summary>Indice 1</summary>

Relis « Au moins un : passer par le contraire » (fiche §2, le bloc Python) et la docstring.

</details>
<details><summary>Indice 2</summary>

Une seule boucle sur `outcomes`, qui compte les issues et les issues favorables ; puis la `Fraction`. Pas de `len(outcomes)` : un générateur n'en a pas.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
total = favourable = 0
for outcome in outcomes:
    total += 1
    ...
```
Pour la copie, a : les triplets de somme 6 sont les rangements de (1, 1, 4), de (1, 2, 3) et de (2, 2, 2).

</details>

### Ex R8.18 — Espérance et variance d'une loi · `expectation`, `variance`

<details><summary>Indice 1</summary>

Relis « L'espérance » et « La variance et l'écart-type » (fiche §7), et les deux docstrings.

</details>
<details><summary>Indice 2</summary>

Vérifie la loi d'abord (longueurs, signes, somme à $10^{-9}$ près), puis la somme pondérée. Pour la variance, calcule l'espérance `m`, puis la somme des `(x - m) ** 2 * p`.

</details>
<details><summary>Indice 3</summary>

La vérification de la somme : `abs(sum(probabilities) - 1) > 1e-9`. Avec des entiers et des `Fraction`, la somme est déjà une `Fraction` : ne la convertis pas en `float`.

</details>

### Ex R8.19 — Estimer une probabilité par simulation · `simulate_frequency`

<details><summary>Indice 1</summary>

Relis « Un générateur et une graine » et « Bonnes pratiques » (fiche §8), et la docstring.

</details>
<details><summary>Indice 2</summary>

Le cas interdit (`n_trials <= 0`), puis **un** générateur `np.random.default_rng(seed)` créé avant la boucle, une boucle de `n_trials` appels à `experiment(rng)`, et le nombre de succès divisé par `n_trials`.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
rng = np.random.default_rng(seed)
successes = 0
for _ in range(n_trials):
    ...
```
(`import numpy as np` en tête du fichier, ou dans la fonction).

</details>

### Ex R8.20 — Prédire : dans une classe de 30, deux élèves ont-ils le même anniversaire ?

<details><summary>Indice 1</summary>

Relis « Au moins un : passer par le contraire » (fiche §2) et le nombre de paires $\binom{n}{2}$ (fiche §3).

</details>
<details><summary>Indice 2</summary>

Écris tes prédictions, même incertaines : l'expérience tranchera. Pour d, la probabilité que les $n$ anniversaires soient tous différents est un produit de $n$ fractions.

</details>
<details><summary>Indice 3</summary>

Pour d, le $k$-ième élève (en comptant à partir de 0) doit éviter les $k$ dates déjà prises : il a $365 - k$ dates possibles sur 365. Pour e, une boucle `for n in range(1, 366)` qui s'arrête au premier $n$ qui convient.

</details>

### Ex R8.21 — La loi des grands nombres : fréquence et nombre de lancers

<details><summary>Indice 1</summary>

Relis « La loi des grands nombres » (fiche §8) et le calcul vectorisé de workbookIA 0A (§100.8.3).

</details>
<details><summary>Indice 2</summary>

Une boucle sur `sizes`, avec le générateur créé **avant** elle ; à chaque tour, la ligne de l'énoncé pour `freqs`, puis la proportion des séries qui s'écartent, ajoutée à `far`.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
rng = np.random.default_rng(81)
far, kept = [], {}
for n in sizes:
    freqs = ...
    far.append(float(...))
    kept[n] = freqs
```
Pour les histogrammes : `ax.hist(kept[n], bins=40, range=(0, 1))`.

</details>

### Ex R8.22 — Le diagramme en bâtons d'une loi

<details><summary>Indice 1</summary>

Relis « La loi d'une variable aléatoire » (fiche §6, la figure) et l'espérance (fiche §7).

</details>
<details><summary>Indice 2</summary>

Dans l'axe reçu : `ax.bar` pour les bâtons, l'espérance calculée avec `values` et `probabilities`, `ax.axvline` pour la droite, puis le titre et les deux axes.

</details>
<details><summary>Indice 3</summary>

L'espérance : `mean = sum(v * p for v, p in zip(values, probabilities))`. Ne crée pas de figure dans la fonction : la cellule suivante te donne l'axe.

</details>

### Ex R8.23 — Chasse à l'erreur : trois raisonnements de probabilités faux

<details><summary>Indice 1</summary>

Relis les règles de la réunion et l'encadré ⚠️ sur l'équiprobabilité (fiche §2), puis l'encadré ⚠️ du §5.

</details>
<details><summary>Indice 2</summary>

Pour chaque raisonnement : additionne-t-il des événements qui peuvent arriver ensemble ? Suppose-t-il équiprobables des issues qui ne le sont pas ? Confond-il incompatibles et indépendants ?

</details>
<details><summary>Indice 3</summary>

(A) : les deux « 4 » peuvent arriver ensemble ; calcule plutôt le contraire, « aucun 4 ». Pour chacun des autres, applique les trois questions ci-dessus.

</details>

### Ex R8.24 — Reproductibilité : générateur aléatoire et graine

<details><summary>Indice 1</summary>

Relis « Un générateur et une graine » et « Bonnes pratiques » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Un seul générateur, créé avec la graine **avant** la boucle, puis une liste des mesures. Compare avec `buggy_runs` : où son générateur est-il créé ?

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
rng = np.random.default_rng(seed)
return [measure(rng) for _ in range(n_runs)]
```
Pour la copie, regarde la ligne `rng = ...` de `buggy_runs`.

</details>
