# M06 · Théorie de l'information — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🧮 🗣️ Pont, estimation et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M06.Q1 — La surprise et la probabilité

<details><summary>Indice 1</summary>

Relis « Plus c'est rare, plus ça informe » (fiche §1).

</details>
<details><summary>Indice 2</summary>

L'information d'un événement de probabilité $p$ est $-\log_2 p$ bits ; pour des événements indépendants, les probabilités se multiplient.

</details>
<details><summary>Indice 3</summary>

2 : résous $-\log_2 p = 11$, soit $p = 2^{-11}$. 5 : 1 bit vaut $\ln 2$ nat. 6 : que devient $-\log(p\,q)$ ?

</details>

### M06.Q2 — L'entropie : vrai ou faux

<details><summary>Indice 1</summary>

Relis « L'information moyenne » et « Ses valeurs extrêmes » (fiche §2).

</details>
<details><summary>Indice 2</summary>

L'entropie est la moyenne des surprises $-\log_2 p(x)$, pondérée par les probabilités ; elle ne dépend que des probabilités.

</details>
<details><summary>Indice 3</summary>

2 : la plus grande entropie sur $n$ issues est $\log_2 n$ ; combien vaut $\log_2 12$ ? 5 : laquelle des deux lois est la plus prévisible ?

</details>

### M06.Q3 — Conjointe et conditionnelle

<details><summary>Indice 1</summary>

Relis « L'entropie d'un couple » et « La règle de la chaîne » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$H(X, Y) = H(X) + H(Y \mid X)$, dans un sens ou dans l'autre.

</details>
<details><summary>Indice 3</summary>

6 : écris la règle de la chaîne dans les deux sens, et isole l'entropie conditionnelle.

</details>

### M06.Q4 — L'information mutuelle

<details><summary>Indice 1</summary>

Relis « Ce que $X$ apprend sur $Y$ » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$I(X ; Y)$ est la baisse de l'incertitude sur $X$ quand on connaît $Y$ ; elle est nulle exactement pour des variables indépendantes.

</details>
<details><summary>Indice 3</summary>

5 : $H(X \mid Y)$ peut-elle être négative ? 6 : regarde la figure des deux nuages de points de la fiche.

</details>

### M06.Q5 — La KL n'est pas une distance

<details><summary>Indice 1</summary>

Relis « Coder avec la mauvaise loi » (fiche §5).

</details>
<details><summary>Indice 2</summary>

$\mathrm{KL}(p \,\|\, q) = \sum p \log_2 \frac{p}{q}$, sur les issues où $p > 0$ ; un terme où $p > 0$ et $q = 0$ est infini.

</details>
<details><summary>Indice 3</summary>

3 : dans $\mathrm{KL}(q \,\|\, p)$, la troisième issue a $q > 0$ et $p = 0$. 4 : qu'exige-t-on d'une distance, en plus d'être positive ?

</details>

### M06.Q6 — L'inégalité de Jensen

<details><summary>Indice 1</summary>

Relis « L'inégalité de Jensen » et sa figure (fiche §6).

</details>
<details><summary>Indice 2</summary>

Pour $f$ convexe, la corde est au-dessus de la courbe : $\mathbb{E}[f(X)] \ge f(\mathbb{E}[X])$ ; pour $f$ concave, l'inverse.

</details>
<details><summary>Indice 3</summary>

5 : la fonction $\frac{1}{x}$ est-elle convexe sur $]0, +\infty[$ ? 6 : la formule de la variance de M02b.

</details>

### M06.Q7 — Codes préfixes

<details><summary>Indice 1</summary>

Relis « Codes de longueur variable, codes préfixes » et « L'inégalité de Kraft » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Un code est préfixe si aucun mot n'est le début d'un autre ; des longueurs sont possibles si $\sum 2^{-\ell_i} \le 1$.

</details>
<details><summary>Indice 3</summary>

2 : compare chaque paire de mots, puis calcule la somme de Kraft. 5 : la plus petite puissance de 2 au moins égale à 1 000.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M06.R1 — Logarithmes en base 2 (R6)

<details><summary>Indice 1</summary>

Relis R6 (logarithmes) : $\log_2 x$ est l'exposant $y$ tel que $2^y = x$.

</details>
<details><summary>Indice 2</summary>

$\log_2 \frac{1}{x} = -\log_2 x$, $\log_2(ab) = \log_2 a + \log_2 b$, $\log_2 \sqrt{x} = \frac{1}{2}\log_2 x$, $\log_2 x = \frac{\ln x}{\ln 2}$, et $\log_2 x = a$ équivaut à $x = 2^a$.

</details>
<details><summary>Indice 3</summary>

1 : $4096 = 2^{12}$ et $2\sqrt{2} = 2^1 \times 2^{1/2}$. 3 : $48 = 16 \times 3$. 5 : pour quelle valeur de $p$ le logarithme est-il nul ?

</details>

### M06.R2 — Probabilités jointes et conditionnelles (M03)

<details><summary>Indice 1</summary>

Relis M03 (loi jointe, lois marginales, indépendance).

</details>
<details><summary>Indice 2</summary>

Les lois marginales sont les sommes des lignes et des colonnes ; $P(Y \mid X) = \frac{P(X, Y)}{P(X)}$.

</details>
<details><summary>Indice 3</summary>

4 : compare $P(\text{en retard} \mid \text{pluie})$ à $P(\text{en retard})$, ou chaque case au produit de ses marges.

</details>

### M06.R3 — Convexité (M05a)

<details><summary>Indice 1</summary>

Relis M05a §1 (convexité, dérivée seconde).

</details>
<details><summary>Indice 2</summary>

Une fonction deux fois dérivable est convexe là où sa dérivée seconde est positive ou nulle.

</details>
<details><summary>Indice 3</summary>

3 : dérive $x \ln x$ comme un produit, puis encore une fois.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M06.1 — L'information d'événements et l'entropie d'une loi à quatre issues

<details><summary>Indice 1</summary>

Relis la fiche §1 (bits et nats) et §2 (l'entropie).

</details>
<details><summary>Indice 2</summary>

L'information d'une issue est $-\log_2 p$ ; l'entropie est la moyenne de ces informations, chacune pondérée par sa probabilité.

</details>
<details><summary>Indice 3</summary>

a) $-\log_2 0{,}55 = \frac{-\ln 0{,}55}{\ln 2}$. e) Les deux erreurs regroupées ont la probabilité $0{,}07 + 0{,}03$. f) Pour deux variables indépendantes, la règle de la chaîne s'écrit avec $H(Y \mid X) = H(Y)$.

</details>

### Ex M06.2 — L'entropie maximale : comparer des lois à quatre issues

<details><summary>Indice 1</summary>

Relis « Ses valeurs extrêmes » (fiche §2), et le regroupement de M06.1.

</details>
<details><summary>Indice 2</summary>

Pour chaque loi, la somme $\sum -p \log_2 p$. Pour e), sépare l'issue fixée des trois autres, comme le regroupement de M06.1 : $H = H(0{,}45 ;\ 0{,}55) + 0{,}55 \times (\ldots)$.

</details>
<details><summary>Indice 3</summary>

e) Le terme entre parenthèses est l'entropie de la loi des trois dernières issues, sachant que la première n'est pas sortie : pour quelle loi est-il le plus grand ?

</details>

### Ex M06.3 — Entropies conjointe et conditionnelle d'un tableau 2 × 3

<details><summary>Indice 1</summary>

Relis l'exemple des 200 élèves (fiche §3).

</details>
<details><summary>Indice 2</summary>

La loi de $Y$ sachant $X = x$ est la ligne $x$ dont chaque case est divisée par $P(X = x)$ ; $H(Y \mid X)$ est la moyenne des entropies de ces lois, pondérée par $P(X = x)$.

</details>
<details><summary>Indice 3</summary>

b) La ligne « payant » divisée par 0,6. d) La loi de $Y$ : les sommes des colonnes. e) La règle de la chaîne : $H(X \mid Y) = H(X, Y) - H(Y)$.

</details>

### Ex M06.4 — La règle de la chaîne de l'entropie, vérifiée

<details><summary>Indice 1</summary>

Relis la règle de la chaîne (fiche §3).

</details>
<details><summary>Indice 2</summary>

Divise chaque ligne par $P(X = x) = 0{,}5$ pour obtenir les lois conditionnelles, puis pondère leurs entropies.

</details>
<details><summary>Indice 3</summary>

f) La loi de $Y$ : $(0{,}35 + 0{,}2 ;\ 0{,}15 + 0{,}3)$. g) $H(X, Y) - H(Y)$.

</details>

### Ex M06.5 — L'information mutuelle de deux variables

<details><summary>Indice 1</summary>

Relis l'exemple des élèves (fiche §3 et §4).

</details>
<details><summary>Indice 2</summary>

$I(X ; Y) = H(Y) - H(Y \mid X)$ : calcule d'abord $H(Y)$ avec la loi de $Y$, puis $H(Y \mid X)$ ligne par ligne.

</details>
<details><summary>Indice 3</summary>

d) Les trois lignes, une fois divisées, sont $(\frac{1}{9}, \frac{8}{9})$, $(\frac{2}{3}, \frac{1}{3})$ et $(1, 0)$, de poids $\frac{9}{16}$, $\frac{3}{16}$, $\frac{1}{4}$. g) $H(X \mid Y) = H(X) - I(X ; Y)$.

</details>

### Ex M06.6 — Cross-entropy et KL en bits perdus : un code fait pour la mauvaise loi

<details><summary>Indice 1</summary>

Relis « Coder avec la mauvaise loi » (fiche §5).

</details>
<details><summary>Indice 2</summary>

La longueur du mot du type $i$ est $-\log_2 q_i$ ; la longueur moyenne sur les données d'aujourd'hui pondère ces longueurs par $p_i$.

</details>
<details><summary>Indice 3</summary>

c) Écris d'abord la longueur de chacun des cinq mots, puis pondère par $p_i$. d) $H(p, q) - H(p)$. g) $p_1 = \frac{1}{4}$ et $q_1 = \frac{1}{2}$.

</details>

### Ex M06.7 — L'inégalité de Jensen sur trois exemples

<details><summary>Indice 1</summary>

Relis « L'inégalité de Jensen » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Calcule séparément $\mathbb{E}[f(X)] = \sum p_i f(x_i)$ et $f(\mathbb{E}[X])$, puis la différence, dans cet ordre.

</details>
<details><summary>Indice 3</summary>

b) $\frac{1}{4} \times 1 + \frac{1}{2} \times 9 + \frac{1}{4} \times 25$. f) $\mathbb{E}[X_3] = \frac{1 + 4}{2}$.

</details>

### Ex M06.8 — Kraft : ces longueurs de code sont-elles possibles ?

<details><summary>Indice 1</summary>

Relis l'inégalité de Kraft et l'arbre du code (fiche §7).

</details>
<details><summary>Indice 2</summary>

Un mot de longueur $\ell$ prend la part $2^{-\ell}$ (ou $3^{-\ell}$ pour un alphabet de trois symboles) ; des longueurs sont possibles si la somme est au plus 1.

</details>
<details><summary>Indice 3</summary>

f) Il reste $1 - \frac{1}{2} - \frac{1}{4}$ ; combien de parts de $\frac{1}{8}$ y tiennent ? g) Compare les mots deux à deux.

</details>

### Ex M06.9 — La longueur moyenne d'un code, comparée à l'entropie

<details><summary>Indice 1</summary>

Relis « Longueur moyenne et entropie » et l'exemple des longueurs de Shannon (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\bar{L} = \sum p_i \ell_i$, avec les longueurs des mots du code, dans l'ordre des symboles ; les longueurs de Shannon sont $\lceil -\log_2 p_i \rceil$, arrondies **vers le haut**.

</details>
<details><summary>Indice 3</summary>

b) Le deuxième symbole a un mot de 3 chiffres, le troisième un mot de 2. d) $-\log_2 0{,}4 \approx 1{,}32$ donne 2, même si 1,32 est proche de 1.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M06.10 — I(X ; Y) = H(X) − H(X | Y), et l'information mutuelle est positive

<details><summary>Indice 1</summary>

Relis la fiche §3 (l'entropie conditionnelle comme double somme) et §5 (la KL).

</details>
<details><summary>Indice 2</summary>

Question 1 : remplace $p(x, y)$ par $p(y)\,p(x \mid y)$ dans le quotient, sépare le logarithme en deux sommes, et regroupe les cases d'une même valeur $x$.

</details>
<details><summary>Indice 3</summary>

Question 3 : compare la définition de $I$ à celle de $\mathrm{KL}(p \,\|\, q)$ avec $q(x, y) = p(x)\,p(y)$. Question 6 : cherche une colonne où $X$ est plus incertain que dans sa loi marginale.

</details>

### Ex M06.11 — La KL est positive : la preuve par l'inégalité de Jensen

<details><summary>Indice 1</summary>

Relis l'inégalité de Jensen et son cas d'égalité (fiche §6).

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[\log_2 Z] = \sum_{p(x) > 0} p(x) \log_2 \frac{q(x)}{p(x)}$ : c'est $-\mathrm{KL}(p \,\|\, q)$. Et $\mathbb{E}[Z]$ se simplifie en une somme de valeurs de $q$.

</details>
<details><summary>Indice 3</summary>

Question 3 : Jensen pour une fonction concave, puis la croissance de $\log_2$. Question 6 : écris $\mathrm{KL}(P \,\|\, Q)$ pour $P_i = \frac{a_i}{A}$ et $Q_i = \frac{b_i}{B}$, et sépare le logarithme du quotient en deux.

</details>

<a id="reflexion"></a>

## 🔗 🧮 🗣️ Pont, estimation et explication

### Ex M06.12 — La log loss d'un classifieur, une cross-entropy moyenne

<details><summary>Indice 1</summary>

Relis « La log loss d'un classifieur » (fiche §5) et « La perplexité » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Pour une image, la cross-entropy ne garde que $-\ln(\text{probabilité donnée à la vraie classe})$ ; la log loss en est la moyenne.

</details>
<details><summary>Indice 3</summary>

a) La vraie classe de l'image 3 est C. c) Divise par $\ln 2$. f) $e^{b)}$.

</details>

### Ex M06.13 — Choisir une feature par l'information mutuelle

<details><summary>Indice 1</summary>

Relis « Choisir des features par l'information mutuelle » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Ici $H(Y) = 1$ : calcule $H(Y \mid F)$ pour chaque feature, ligne par ligne, puis $I = H(Y) - H(Y \mid F)$.

</details>
<details><summary>Indice 3</summary>

a) Chaque ligne de $F_1$, divisée par 10, vaut $(0{,}7 ;\ 0{,}3)$. c) Les lignes de $F_3$ ont les poids $\frac{4}{20}$, $\frac{6}{20}$, $\frac{10}{20}$. g) Écris le tableau regroupé (jeune ; moyen ou senior), puis calcule son information mutuelle.

</details>

### Ex M06.14 — Fermi : combien de bits pour un génome humain ?

<details><summary>Indice 1</summary>

Relis « Codes de longueur fixe » (fiche §7) et l'entropie (fiche §2).

</details>
<details><summary>Indice 2</summary>

Un code de longueur fixe pour 4 lettres prend 2 bits ; 8 bits font un octet.

</details>
<details><summary>Indice 3</summary>

2 : $H(0{,}3 ;\ 0{,}3 ;\ 0{,}2 ;\ 0{,}2)$. 4 : $0{,}1\,\%$ de $3 \times 10^9$, fois 34 bits, divisé par 8.

</details>

### Ex M06.15 — Expliquer l'information mutuelle avec deux capteurs

<details><summary>Indice 1</summary>

Relis le diagramme de l'information (fiche §4).

</details>
<details><summary>Indice 2</summary>

L'information mutuelle, c'est la part d'incertitude commune aux deux capteurs : ce que lire l'un apprend sur l'autre.

</details>
<details><summary>Indice 3</summary>

Prends les deux thermomètres pour le cas « grande », le détecteur de porte et le thermomètre pour le cas « presque nulle ».

</details>

<a id="entretien"></a>

## 💼 Entretien

### M06.E1 — Information mutuelle ou corrélation : laquelle détecte quoi ?

<details><summary>Indice 1</summary>

Relis « Information mutuelle et corrélation » (fiche §4).

</details>
<details><summary>Indice 2</summary>

La corrélation ne voit que les liens linéaires ; l'information mutuelle, n'importe quel lien.

</details>
<details><summary>Indice 3</summary>

L'exemple : une feature symétrique autour de 0 et une cible égale à son carré. Un avantage de la corrélation : pense au signe, et aux petits échantillons.

</details>

<a id="notebook"></a>

## Notebook

### Ex M06.16 — Entropies conjointe et conditionnelle d'un tableau · `joint_entropy, conditional_entropy`

<details><summary>Indice 1</summary>

Relis la docstring du module `info.py`, puis la fiche §3.

</details>
<details><summary>Indice 2</summary>

D'abord les vérifications : `np.asarray(joint, dtype=float)`, deux dimensions, `np.all(table >= 0)`, une somme égale à 1 à $10^{-9}$ près, `base > 1`. Puis les seules cases positives : `table[table > 0]`.

</details>
<details><summary>Indice 3</summary>

`p = table[table > 0]`, `-np.sum(p * np.log(p)) / math.log(base)` ; pour $H(Y \mid X)$, retire l'entropie de `table.sum(axis=1)` ; convertis en `float`.

</details>

### Ex M06.17 — L'information mutuelle · `mutual_information`

<details><summary>Indice 1</summary>

Relis la fiche §4.

</details>
<details><summary>Indice 2</summary>

`np.outer(table.sum(axis=1), table.sum(axis=0))` donne $p(x)\,p(y)$ dans chaque case.

</details>
<details><summary>Indice 3</summary>

Sur les cases `table > 0` : `np.sum(p * np.log(p / product[positive])) / math.log(base)` ; une valeur entre $-10^{-12}$ et 0 devient `0.0`.

</details>

### Ex M06.18 — Codes préfixes et somme de Kraft · `kraft_sum, is_prefix_code`

<details><summary>Indice 1</summary>

Relis la fiche §7, et la remarque de l'énoncé sur les tableaux NumPy.

</details>
<details><summary>Indice 2</summary>

Kraft : un terme par mot, `float(alphabet) ** -int(length)` (ou `Fraction(1, int(alphabet) ** int(length))`). Préfixe : `str.startswith`, dans les deux sens.

</details>
<details><summary>Indice 3</summary>

Après `words.sort()`, un mot qui en commence un autre est juste avant un mot qu'il commence : compare chaque mot à son voisin. `bool(...)` et `str(...)` pour des types de Python.

</details>

### Ex M06.19 — L'écart de Jensen d'une loi discrète · `jensen_gap`

<details><summary>Indice 1</summary>

Relis la fiche §6.

</details>
<details><summary>Indice 2</summary>

Les vérifications d'abord (liste non vide, poids valides), puis $\mathbb{E}[f(X)]$ et $f(\mathbb{E}[X])$.

</details>
<details><summary>Indice 3</summary>

`sum(wi * f(float(xi)) for xi, wi in zip(x, w))` (f valeur par valeur), puis `- f(float(np.dot(w, x)))`, en `float`.

</details>

### Ex M06.20 — `sklearn.metrics.mutual_info_score` contre ta fonction, en nats

<details><summary>Indice 1</summary>

Relis l'encadré « Aujourd'hui en pratique » de la fiche §4.

</details>
<details><summary>Indice 2</summary>

`mutual_info_score(x, y)` prend les deux tableaux d'observations et renvoie des nats.

</details>
<details><summary>Indice 3</summary>

b) Divise par `math.log(2)`. d) Compare les deux résultats. e) `rng = np.random.default_rng(620)`, puis `rng.permutation(y_20)`, une seule fois.

</details>

### Ex M06.21 — Prédire : l'information mutuelle de X et X³, de X et X²

<details><summary>Indice 1</summary>

Relis « Ce que $X$ apprend sur $Y$ » et « Information mutuelle et corrélation » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Que vaut $H(X^3 \mid X)$ ? Et $H(X \mid X^3)$ ? Écris $I(X ; X^2)$ avec une entropie conditionnelle bien choisie.

</details>
<details><summary>Indice 3</summary>

$X^3$ prend 7 valeurs différentes, $X^2$ seulement 4. Pour la corrélation de $X$ et $X^2$ : $\mathbb{E}[X^3] = 0$ par symétrie.

</details>

### Ex M06.22 — Estimer une entropie à partir d'un échantillon : le biais des petits échantillons

<details><summary>Indice 1</summary>

Relis la définition du biais d'un estimateur (M02c).

</details>
<details><summary>Indice 2</summary>

`mean_bias` : la moyenne des estimations sur les échantillons de `SAMPLES_22[n]`, moins `H_22`. `miller_madow` : $n$ est la taille de l'échantillon, et $m$ le nombre de valeurs qui y apparaissent au moins une fois.

</details>
<details><summary>Indice 3</summary>

`np.bincount(sample, minlength=k)` compte chaque valeur : $m$ est le nombre de comptes non nuls (`np.count_nonzero`). La correction est en bits : n'oublie pas le $\ln 2$.

</details>

### Ex M06.23 — Un diagramme de l'information : H(X), H(Y), H(X | Y), I(X ; Y)

<details><summary>Indice 1</summary>

Relis le diagramme de la fiche §4.

</details>
<details><summary>Indice 2</summary>

Calcule $H(X, Y)$, $H(Y \mid X)$, $H(X \mid Y)$ (le tableau transposé) et $I$, puis trois appels à `ax.barh` par barre au plus, avec `left=`.

</details>
<details><summary>Indice 3</summary>

Barre H(X) : `ax.barh(2, a)` et `ax.barh(2, I, left=a)` ; barre H(Y) : `ax.barh(1, I, left=a)` et `ax.barh(1, b, left=a + I)` ; puis `ax.barh(0, h_xy)`, `ax.set_yticks([2, 1, 0], labels=[...])` et `ax.set_xlabel("bits")`.

</details>

### Ex M06.24 — Chasse à l'erreur : log en base 10, 0 log 0, KL à l'envers

<details><summary>Indice 1</summary>

Relis le tableau des pièges classiques de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, calcule à la main ce qu'elle donne, puis ce que dit son commentaire.

</details>
<details><summary>Indice 3</summary>

Trois questions utiles : que vaut $0 \times \log_2 0$ pour NumPy ? Quelle est la base de chaque logarithme ? Dans quel ordre sont les deux lois de chaque formule ?

</details>

### Ex M06.25 — Calculer 0 log 0 proprement (`scipy.special.xlogy`)

<details><summary>Indice 1</summary>

Relis l'énoncé : il dit ce que calcule `xlogy(x, y)`.

</details>
<details><summary>Indice 2</summary>

Divise d'abord chaque ligne par sa somme (`table.sum(axis=1, keepdims=True)` garde la forme) ; `xlogy(c, c)` donne alors $c \ln c$ case par case.

</details>
<details><summary>Indice 3</summary>

Somme chaque ligne (`axis=1`), change le signe, et divise par `math.log(base)`.

</details>

### Ex M06.26 — Défi : localiser une panne parmi 100 serveurs en un minimum de questions

<details><summary>Indice 1</summary>

Relis « Longueur moyenne et entropie » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Garde l'intervalle `lo..hi` des serveurs encore possibles. Pour la loi uniforme, couper l'intervalle en deux suffit ; pour l'autre, que faut-il couper en deux parts égales ?

</details>
<details><summary>Indice 3</summary>

Coupe la **probabilité** restante en deux : avec `cumulative = np.concatenate([[0], np.cumsum(probs)])`, choisis le seuil `t` dont `cumulative[t]` est le plus proche du milieu de `cumulative[lo - 1]` et `cumulative[hi]`.

</details>
