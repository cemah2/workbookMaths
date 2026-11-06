# M02b · Variables aléatoires et lois usuelles — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M02b.Q1 — Discrète ou continue ?

<details><summary>Indice 1</summary>

Relis « Discrète ou continue » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Une variable discrète prend des valeurs qu'on peut énumérer une à une (un comptage, une classe) ; une variable à densité peut prendre n'importe quelle valeur d'un intervalle (une durée, une température).

</details>
<details><summary>Indice 3</summary>

5 : le nombre de lancers peut valoir 1, 2, 3, … sans limite : ces valeurs s'énumèrent, mais il y en a une infinité. 6 : pense à 5.

</details>

### M02b.Q2 — Quelle loi pour quelle situation ?

<details><summary>Indice 1</summary>

Relis les titres des lois des §2 et §3 : chacun dit ce que la loi compte ou mesure.

</details>
<details><summary>Indice 2</summary>

Un nombre de succès en $n$ essais : binomiale. Un rang de premier succès : géométrique. Un nombre d'événements sur une durée : Poisson. Une durée jusqu'au prochain événement : exponentielle.

</details>
<details><summary>Indice 3</summary>

4 : « qui ne s'use pas » veut dire « sans mémoire », et le paramètre est l'inverse de la durée moyenne. 6 : le théorème central limite, mentionné à la fin du §3.

</details>

### M02b.Q3 — Espérance et variance : vrai ou faux

<details><summary>Indice 1</summary>

Relis le §4, en particulier « Une espérance qui n'existe pas » et le tableau des lois usuelles.

</details>
<details><summary>Indice 2</summary>

Une espérance est une moyenne pondérée : elle tombe souvent entre deux valeurs. Une variance est une moyenne de carrés.

</details>
<details><summary>Indice 3</summary>

1 : l'espérance d'une Bernoulli de paramètre 0,3. 4 : $\mathbb{V}(aX + b) = a^2\,\mathbb{V}(X)$. 6 : compare $\frac{1}{\lambda}$ et $\sqrt{\frac{1}{\lambda^2}}$.

</details>

### M02b.Q4 — La loi normale : ce que disent μ et σ

<details><summary>Indice 1</summary>

Relis « Normale : la cloche » (fiche §3), et l'avertissement sur le second paramètre.

</details>
<details><summary>Indice 2</summary>

$\mathcal{N}(\mu, \sigma^2)$ : le second nombre est la variance. La hauteur du sommet vaut $\frac{1}{\sigma\sqrt{2\pi}}$.

</details>
<details><summary>Indice 3</summary>

2 : $\frac{1}{0{,}2\sqrt{2\pi}}$, avec $\sqrt{2\pi} \approx 2{,}5$. 6 : standardise : $\frac{(\mu + \sigma) - \mu}{\sigma} = 1$.

</details>

### M02b.Q5 — Jointe, marginale, indépendance

<details><summary>Indice 1</summary>

Relis « Les marginales : sommer l'autre variable » et « L'indépendance » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Une marginale : la somme d'une ligne ou d'une colonne. L'indépendance : chaque case égale au produit de ses deux marginales.

</details>
<details><summary>Indice 3</summary>

3 : compare $P(X = 1, Y = 1)$ à $P(X = 1)\,P(Y = 1)$. 6 : remplace la somme par une intégrale (fiche §7).

</details>

### M02b.Q6 — La variance d'une somme

<details><summary>Indice 1</summary>

Relis « La variance d'une somme » (fiche §6) et ses trois conséquences.

</details>
<details><summary>Indice 2</summary>

Les variances s'additionnent (pour une somme comme pour une différence), pas les écarts-types. Un facteur compte au carré.

</details>
<details><summary>Indice 3</summary>

1 : $6^2 + 8^2$. 5 : la variance de la moyenne de $n$ variables i.i.d. vaut $\frac{\sigma^2}{n}$. 6 : relis le début du §6.

</details>

### M02b.Q7 — Simuler une loi

<details><summary>Indice 1</summary>

Relis le §8 : la loi de $aX + b$, la simulation par inversion, le tirage catégoriel.

</details>
<details><summary>Indice 2</summary>

Une transformation affine d'une uniforme est uniforme, d'une normale est normale. L'inversion applique $F^{-1}$ à $U$.

</details>
<details><summary>Indice 3</summary>

2 : résous $u = 1 - e^{-\lambda t}$ en $t$. 4 : les sommes cumulées valent 0,5 ; 0,8 ; 1. 6 : peut-on écrire $\Phi^{-1}$ avec des fonctions usuelles ?

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M02b.R1 — Espérance d'une variable discrète (R8)

<details><summary>Indice 1</summary>

Relis l'espérance et la variance de R8 §7.

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[X] = \sum x\,P(X = x)$, $\mathbb{E}[X^2] = \sum x^2\,P(X = x)$, puis $\mathbb{V}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2$.

</details>
<details><summary>Indice 3</summary>

4 : $\mathbb{E}[aX + b] = a\,\mathbb{E}[X] + b$ et $\mathbb{V}(aX + b) = a^2\,\mathbb{V}(X)$.

</details>

### M02b.R2 — Intégrales et densités (M02a)

<details><summary>Indice 1</summary>

Relis les primitives (M02a §2), les intégrales impropres (M02a §4) et la définition d'une densité (M02a §6).

</details>
<details><summary>Indice 2</summary>

Une densité : positive, d'intégrale totale 1. Pour une intégrale jusqu'à $+\infty$, une limite.

</details>
<details><summary>Indice 3</summary>

3 : une primitive de $3x^{-4}$ est $-x^{-3}$. 4 : $\int_1^2 \frac{3}{x^4}\,dx$.

</details>

### M02b.R3 — Coefficients binomiaux (R8)

<details><summary>Indice 1</summary>

Relis les combinaisons de R8 §3.

</details>
<details><summary>Indice 2</summary>

$\binom{n}{k} = \frac{n!}{k!\,(n - k)!}$, le nombre de façons de choisir $k$ objets parmi $n$.

</details>
<details><summary>Indice 3</summary>

4 : un mot est fixé par les positions de ses deux A : combien de façons de choisir 2 positions parmi 7 ?

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M02b.1 — Loi de Bernoulli et loi binomiale

<details><summary>Indice 1</summary>

Relis « Binomiale : le nombre de succès en $n$ essais » (fiche §2) : $X \sim \mathcal{B}(5 ; 0{,}8)$.

</details>
<details><summary>Indice 2</summary>

Écris $P(X = k) = \binom{5}{k}\,0{,}8^k\,0{,}2^{5-k}$ pour chaque $k$ demandé ; l'espérance et la variance sont dans le tableau du §4.

</details>
<details><summary>Indice 3</summary>

d : compare $P(X = 3)$, $P(X = 4)$ et $P(X = 5)$. h : « au moins un raté » est le contraire de « $n$ réussites » : résous $1 - 0{,}8^n \ge 0{,}9$ avec un logarithme, puis vérifie les entiers voisins.

</details>

### Ex M02b.2 — Loi géométrique : probabilités, et l'espérance par une série

<details><summary>Indice 1</summary>

Relis « Géométrique : le rang du premier succès » (fiche §2) et la somme d'une suite géométrique (R5).

</details>
<details><summary>Indice 2</summary>

$P(X = k) = q^{k-1}p$ et $P(X > k) = q^k$. Pour d, écris $S$ et $qS$ l'une sous l'autre, en décalant d'un rang.

</details>
<details><summary>Indice 3</summary>

d : $S - qS = 1 + q + q^2 + \cdots = \frac{1}{1 - q}$, donc $S = \frac{1}{(1 - q)^2}$. e : $\mathbb{E}[X] = \sum k\,q^{k-1}p = p\,S$. g : calcule $P(X \le 1)$, puis $P(X \le 2)$.

</details>

### Ex M02b.3 — Loi de Poisson : probabilités, espérance, et la somme de deux variables de Poisson indépendantes

<details><summary>Indice 1</summary>

Relis « Poisson : compter des événements rares » (fiche §2) et l'indépendance (fiche §5).

</details>
<details><summary>Indice 2</summary>

$P(X = k) = e^{-1{,}5}\frac{1{,}5^k}{k!}$. Pour $S$, énumère les couples $(X, Y)$ qui donnent la valeur voulue, et multiplie les probabilités de chaque couple (indépendance).

</details>
<details><summary>Indice 3</summary>

f : $P(X = 0)P(Y = 1) + P(X = 1)P(Y = 0)$, et $e^{-1{,}5}e^{-2{,}5} = e^{-4}$ se met en facteur. h : compare $e^{-4}(1{,}5 + 2{,}5)$ à $e^{-\lambda}\lambda$.

</details>

### Ex M02b.4 — Lois uniforme et exponentielle : probabilités et espérance

<details><summary>Indice 1</summary>

Relis « Uniforme sur $[a ; b]$ » et « Exponentielle » (fiche §3), puis le tableau du §4.

</details>
<details><summary>Indice 2</summary>

Uniforme : une probabilité est une longueur divisée par $b - a$. Exponentielle : $P(T > t) = e^{-\lambda t}$ et $\mathbb{E}[T] = \frac{1}{\lambda}$.

</details>
<details><summary>Indice 3</summary>

e : $\sigma = \frac{b - a}{\sqrt{12}}$. h : $P(T > \frac{1}{\lambda}) = e^{-\lambda \times \frac{1}{\lambda}}$.

</details>

### Ex M02b.5 — Loi normale : standardiser et lire la fonction Φ

<details><summary>Indice 1</summary>

Relis « Standardiser » (fiche §3) et l'exemple des paquets de pâtes.

</details>
<details><summary>Indice 2</summary>

$z = \frac{x - 30}{4}$, puis la table. Pour un $z$ négatif, $\Phi(-z) = 1 - \Phi(z)$ ; pour une probabilité « plus grand que », $1 - \Phi(z)$.

</details>
<details><summary>Indice 3</summary>

f : cherche dans la table le $z$ tel que $\Phi(z) = 0{,}9901$, puis $t = 30 + 4z$. g : $|X - 30| \le 5$ va de 25 à 35, soit $z$ de $-1{,}25$ à $1{,}25$. h : $\mathcal{N}(31, 2^2)$ a pour écart-type 2.

</details>

### Ex M02b.6 — Espérance et variance d'une variable continue (théorème de transfert)

<details><summary>Indice 1</summary>

Relis « L'espérance, discrète et continue » et « Le théorème de transfert » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[X] = \int_0^1 x \cdot 2(1 - x)\,dx$ et $\mathbb{E}[X^2] = \int_0^1 x^2 \cdot 2(1 - x)\,dx$ : développe, puis intègre terme à terme.

</details>
<details><summary>Indice 3</summary>

g : par parties avec $u = 1 - x$ et $v' = e^x$ : $\int (1 - x)e^x\,dx = (1 - x)e^x + \int e^x\,dx = (2 - x)e^x$, puis multiplie par 2. h : $e^{1/3} \approx 1{,}3956$.

</details>

### Ex M02b.7 — Un couple de variables discrètes : loi jointe, marginales, indépendance

<details><summary>Indice 1</summary>

Relis le §5 en entier, avec l'exemple du stand de glaces.

</details>
<details><summary>Indice 2</summary>

Les marginales : somme des colonnes pour $Y$, des lignes pour $X$. $\mathbb{E}[XY]$ : la somme de $x \times y \times P(X = x, Y = y)$ sur les six cases.

</details>
<details><summary>Indice 3</summary>

f : $P(X = 1) = 0{,}5$ et $P(Y = 0) = 0{,}2$ : compare leur produit à 0,15. h : la dernière case vaut $1 - 0{,}12 - 0{,}28 - 0{,}18$ ; calcule les marginales de $U$ et de $V$, puis les quatre produits.

</details>

### Ex M02b.8 — Linéarité et variance d'une somme : sommes et moyennes de variables

<details><summary>Indice 1</summary>

Relis « La variance d'une somme » (fiche §6) et ses conséquences.

</details>
<details><summary>Indice 2</summary>

Espérances : elles s'additionnent toujours. Variances : elles s'additionnent pour des variables indépendantes, y compris pour une différence. L'écart-type vient en dernier, par une racine.

</details>
<details><summary>Indice 3</summary>

f : la variance de la somme de 50 copies indépendantes vaut $50 \times 1^2$. g : la moyenne vaut la somme de f) divisée par 50 : son écart-type est celui de la somme (trouvé en f), pas celui de $T_1$) divisé par 50. h : $T_1 + T_1 = 2T_1$.

</details>

### Ex M02b.9 — Une intégrale double sur un rectangle, et une densité jointe

<details><summary>Indice 1</summary>

Relis « Intégrer une fonction de deux variables » et « Densité jointe » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Un produit $g(x)h(y)$ : le produit de deux intégrales simples. Sinon, intègre d'abord en $x$ ($y$ est une constante), puis en $y$.

</details>
<details><summary>Indice 3</summary>

c : $\int_0^1 (x^2 + xy)\,dx = \frac{1}{3} + \frac{y}{2}$. d : l'intégrale de $f$ sur le rectangle vaut $c$ fois l'intégrale de a). e : $f_X(x) = \int_0^3 c\,x\,y^2\,dy$. h : le produit $\int_0^{1/2} f_X \times \int_0^1 f_Y$, puisque $X$ et $Y$ sont indépendantes.

</details>

### Ex M02b.10 — Changement de variable : la loi de aX + b, et celle de X²

<details><summary>Indice 1</summary>

Relis « La loi d'une transformation : passer par $F$ » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Écris $F_Y(y) = P(Y \le y)$, résous l'inégalité pour la ramener à une condition sur $X$, utilise la loi de $X$, puis dérive.

</details>
<details><summary>Indice 3</summary>

b : $f_Y(y) = \frac{1}{3}f_X\big(\frac{y + 1}{3}\big)$. d : quelle loi normale suit $Y = 2X + 5$ ? Sa densité se lit en son centre. f : $X$ est positif, donc $X^2 \le y$ équivaut à $X \le \sqrt{y}$ ; utilise la fonction de répartition de $X$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M02b.11 — La variance d'une somme de variables indépendantes

<details><summary>Indice 1</summary>

Relis le §6 et « Une conséquence » à la fin du §5.

</details>
<details><summary>Indice 2</summary>

1 : développe $(X - \mu)^2$ et utilise la linéarité. 2 : remplace $P(X = x, Y = y)$ par $P(X = x)P(Y = y)$, puis factorise la double somme. 3 : pose $A = X - \mathbb{E}[X]$ et $B = Y - \mathbb{E}[Y]$, et développe $(A + B)^2$.

</details>
<details><summary>Indice 3</summary>

3 : $\mathbb{E}[AB] = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$ (développe $AB$). 5 : applique 4 à $X_1 + \cdots + X_{n-1}$ et $X_n$. 7 : $X + Y = 2X$.

</details>

### Ex M02b.12 — L'intégrale de Gauss par une intégrale double (changement en coordonnées polaires admis)

<details><summary>Indice 1</summary>

Relis « Les coordonnées polaires » et « L'intégrale de Gauss, enfin démontrée » (fiche §7).

</details>
<details><summary>Indice 2</summary>

1 : $e^{-(x^2 + y^2)} = e^{-x^2}e^{-y^2}$, un produit. 2 : en polaires, $g = e^{-r^2}$ et $dx\,dy = r\,dr\,d\theta$ ; une primitive de $r\,e^{-r^2}$ est $-\frac{1}{2}e^{-r^2}$.

</details>
<details><summary>Indice 3</summary>

3 : un point du disque $D_R$ a ses deux coordonnées entre $-R$ et $R$ ; un point du carré est à une distance au plus $R\sqrt{2}$ de l'origine (le coin). Donc $J(R) \le I(R)^2 \le J(R\sqrt{2})$. 4 : les deux bornes tendent vers $\pi$ : théorème des gendarmes (R5).

</details>

### Ex M02b.13 — La loi de Poisson, limite de lois binomiales

<details><summary>Indice 1</summary>

Relis « La loi des événements rares » (fiche §2), et les limites de R7.

</details>
<details><summary>Indice 2</summary>

1 : écris $\binom{n}{k} = \frac{n(n-1)\cdots(n-k+1)}{k!}$, et $p^k = \frac{\lambda^k}{n^k}$. 3 : $\ln\big(1 - \frac{\lambda}{n}\big) = \ln(1 + h)$ avec $h = -\frac{\lambda}{n} \to 0$.

</details>
<details><summary>Indice 3</summary>

2 : $\frac{n - i}{n} = 1 - \frac{i}{n} \to 1$, et il y a $k$ facteurs, un nombre fixe. 3 : $n\ln(1 + h) = -\lambda\,\frac{\ln(1 + h)}{h} \to -\lambda$, puis l'exponentielle est continue.

</details>

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M02b.14 — Combien d'erreurs d'annotation dans un dataset ? Binomiale et Poisson

<details><summary>Indice 1</summary>

Relis « Binomiale » et « La loi des événements rares » (fiche §2).

</details>
<details><summary>Indice 2</summary>

$X \sim \mathcal{B}(2\,000 ;\ 0{,}002)$, approchée par $\mathcal{P}(\lambda)$ avec $\lambda = np$. Pour $Y$, même chose avec $n = 500$.

</details>
<details><summary>Indice 3</summary>

c : $0{,}998^{2\,000}$ à la calculatrice. g : $1 - e^{-0{,}002\,n} \ge 0{,}9$ équivaut à $n \ge \frac{\ln 10}{0{,}002}$ ; arrondis à l'entier supérieur.

</details>

### Ex M02b.15 — MML §6.1 et §6.2 : espace probabilisé, pmf et pdf, en anglais

<details><summary>Indice 1</summary>

Garde la fiche §1 à §3 ouverte à côté du livre : elle suit le même ordre.

</details>
<details><summary>Indice 2</summary>

Cherche les mots *sample space*, *event space*, *target space*, *random variable*, *probability mass function* : chacun a son équivalent dans la fiche.

</details>
<details><summary>Indice 3</summary>

4 : $\Omega$ a quatre issues (PP, PF, FP, FF) ; $X$ compte les F de chaque issue ; regroupe les issues qui donnent la même valeur.

</details>

### Ex M02b.16 — MML §6.4 et §6.7 : espérance, variance, sommes de variables, changement de variable

<details><summary>Indice 1</summary>

Garde la fiche §4, §6 et §8 ouverte à côté du livre.

</details>
<details><summary>Indice 2</summary>

Le livre écrit $\mathbb{E}_X[g(x)]$ : la variable en indice, la fonction entre crochets. Pour la question 3, pense à deux grands nombres très proches qu'on soustrait.

</details>
<details><summary>Indice 3</summary>

5 : $P(\sqrt{X} \le y) = P(X \le y^2) = y^2$ pour $y$ dans $[0 ; 1]$, puis dérive. 6 : $F(X)$ suit la loi uniforme ; lis l'énoncé dans l'autre sens : $F^{-1}(U)$ suit la loi de $X$.

</details>

### Ex M02b.17 — Expliquer la différence entre une variable aléatoire et sa loi

<details><summary>Indice 1</summary>

Relis « Une variable aléatoire est une fonction » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Trois mots à placer : fonction (des issues vers les nombres), loi (les chances de chaque valeur), tirage (une valeur obtenue).

</details>
<details><summary>Indice 3</summary>

L'exemple de la fiche : une pièce, $X$ et $1 - X$. Pour deux normales : la taille de deux personnes tirées au hasard.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M02b.E1 — Quand modéliser un comptage par une loi de Poisson ?

<details><summary>Indice 1</summary>

Relis la description de la loi de Poisson (fiche §2) et le tableau du §4.

</details>
<details><summary>Indice 2</summary>

Les hypothèses : des événements un par un, indépendants, à un rythme constant. Le test simple vient du tableau : pour une loi de Poisson, que valent l'espérance et la variance ?

</details>
<details><summary>Indice 3</summary>

Compare la moyenne et la variance des comptages par minute : une variance bien plus grande que la moyenne (*surdispersion*) signale des rafales, ou un rythme qui varie dans la journée.

</details>

<a id="notebook"></a>

## Notebook

### Ex M02b.18 — Lois binomiale et de Poisson · `binomial_pmf`, `poisson_pmf`

<details><summary>Indice 1</summary>

Relis les formules des lois binomiale et de Poisson (fiche §2).

</details>
<details><summary>Indice 2</summary>

Dans l'ordre : les paramètres impossibles (`raise ValueError`), puis les valeurs de $k$ impossibles (`return 0.0`), puis la formule avec `math.comb`, `math.exp` et `math.factorial`.

</details>
<details><summary>Indice 3</summary>

`return float(math.comb(n, k) * p ** k * (1 - p) ** (n - k))` ; pour Poisson, `float(math.exp(-lam) * lam ** k / math.factorial(k))`.

</details>

### Ex M02b.19 — Densité et fonction de répartition de la loi normale (avec `math.erf`) · `normal_pdf`, `normal_cdf`

<details><summary>Indice 1</summary>

Relis la densité de $\mathcal{N}(\mu, \sigma^2)$ et la formule de $\Phi$ avec `erf` (fiche §3).

</details>
<details><summary>Indice 2</summary>

Standardise d'abord : `z = (x - mu) / sigma`. Alors la densité vaut $\frac{\varphi(z)}{\sigma}$, et la fonction de répartition $\Phi(z)$.

</details>
<details><summary>Indice 3</summary>

`math.exp(-z * z / 2) / (sigma * math.sqrt(2 * math.pi))` et `(1 + math.erf(z / math.sqrt(2))) / 2`.

</details>

### Ex M02b.20 — Simuler par inversion de la fonction de répartition · `inverse_transform_sample`

<details><summary>Indice 1</summary>

Relis « Simuler par inversion » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Trois étapes : `rng = np.random.default_rng(seed)`, `uniforms = rng.random(n)`, puis `inverse_cdf` appliquée à chaque nombre (une liste en compréhension).

</details>
<details><summary>Indice 3</summary>

`np.array([float(inverse_cdf(float(u))) for u in uniforms], dtype=float)` ; la `ValueError` avant de créer le générateur.

</details>

### Ex M02b.21 — `scipy.stats` : pmf, pdf, cdf, ppf et rvs

<details><summary>Indice 1</summary>

Relis le 💻 du §2 et l'avertissement sur le second paramètre de la loi normale (fiche §3).

</details>
<details><summary>Indice 2</summary>

`stats.norm(loc, scale)` : `scale` est l'écart-type. `stats.expon` et `stats.uniform` ont aussi `loc` et `scale` : lis `help(...)` pour savoir ce que chacun représente.

</details>
<details><summary>Indice 3</summary>

e : `stats.expon(scale=1 / 2)`. h : `stats.uniform(loc=2, scale=6)` couvre $[2 ; 8]$.

</details>

### Ex M02b.22 — Prédire : la variance de la moyenne de quatre dés

<details><summary>Indice 1</summary>

Relis « La variance d'une somme » (fiche §6), et l'⚠️ sur $2X$.

</details>
<details><summary>Indice 2</summary>

Somme de $n$ copies indépendantes : variance multipliée par $n$. Une variable multipliée par $a$ : variance multipliée par $a^2$. La moyenne, c'est la somme multipliée par $\frac{1}{4}$.

</details>
<details><summary>Indice 3</summary>

a : $\mathbb{V}\big(\frac{S}{4}\big) = \frac{1}{16}\,\mathbb{V}(S) = \frac{4\,\mathbb{V}(X)}{16}$. b : la racine de a.

</details>

### Ex M02b.23 — Binomiale et Poisson côte à côte quand n grandit

<details><summary>Indice 1</summary>

Relis « La loi des événements rares » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Pour chaque $n$ : `ks = np.arange(n + 1)`, les deux arrays de probabilités, puis `np.max(np.abs(...))` de leur différence.

</details>
<details><summary>Indice 3</summary>

Une fonction `gap(n)` et la liste `[gap(n) for n in N_LIST]` ; d : `next(n for n, g in zip(N_LIST, gaps) if g < 0.01)`.

</details>

### Ex M02b.24 — Une loi jointe en carte de chaleur, ses marginales sur les bords

<details><summary>Indice 1</summary>

Relis « Les marginales : sommer l'autre variable » (fiche §5) et la figure de la loi jointe du stand de glaces.

</details>
<details><summary>Indice 2</summary>

`joint.sum(axis=1)` somme chaque ligne (sur les colonnes) ; `joint.sum(axis=0)` chaque colonne. `ax.imshow(joint.T, origin="lower")` met les lignes de `joint` à l'horizontale.

</details>
<details><summary>Indice 3</summary>

`ax_top.bar(np.arange(len(p_rows)), p_rows)` et `ax_right.barh(np.arange(len(p_cols)), p_cols)` ; puis, avec `p_rows, p_cols = marginals(JOINT_24)`, `np.max(np.abs(JOINT_24 - np.outer(p_rows, p_cols)))`.

</details>

### Ex M02b.25 — Chasse à l'erreur : une densité prise pour une probabilité, σ et σ²

<details><summary>Indice 1</summary>

Relis les ⚠️ du §3 et le tableau des pièges classiques.

</details>
<details><summary>Indice 2</summary>

Pour chaque affirmation : une densité n'est pas une probabilité ; le second paramètre de $\mathcal{N}$ est la variance ; une valeur exacte d'une variable à densité a une probabilité nulle.

</details>
<details><summary>Indice 3</summary>

(B) : $\sigma = \sqrt{4} = 2$. (A) : la valeur est juste, c'est la conclusion qui est fausse. (D) : $P(T = 1) = 0$.

</details>

### Ex M02b.26 — Documenter une loi : docstring et exemples testés (`doctest`)

<details><summary>Indice 1</summary>

Ouvre `mon_travail/mymath/distributions.py` : chaque docstring y suit le format demandé.

</details>
<details><summary>Indice 2</summary>

Copie la structure d'une docstring de `mymath` (résumé, `Parameters`, `Returns`, `Raises`, `Examples`), et choisis des exemples dont le résultat s'affiche exactement : 0,125 plutôt que 0,1.

</details>
<details><summary>Indice 3</summary>

Les exemples : `geometric_pmf(3, 0.5)` affiche `0.125`, `geometric_pmf(0, 0.5)` affiche `0.0`, et `geometric_pmf(2, 1.5)` lève l'erreur, écrite avec `Traceback (most recent call last):`, `...` et la dernière ligne `ValueError: ...`.

</details>

### Ex M02b.27 — Défi : tirer des valeurs normales avec seulement des tirages uniformes

<details><summary>Indice 1</summary>

Commence par la somme de 12 uniformes moins 6 : son espérance vaut 0 et sa variance $12 \times \frac{1}{12} = 1$. Regarde ce que donnent les vérifications, en particulier les queues. Que vaut la plus grande valeur possible ?

</details>
<details><summary>Indice 2</summary>

L'inversion de $\Phi$ par dichotomie (M02a.18) donne des tirages justes, mais `math.erf` ne prend qu'un nombre : un million de valeurs, fois une cinquantaine de coupes, c'est trop lent. Cherche une transformation de **deux** uniformes : la densité jointe de deux normales indépendantes, $\frac{1}{2\pi}e^{-(x^2 + y^2)/2}$, ne dépend que de la distance au centre (M02b.12, question 6). Quelle est la loi de cette distance, et celle de l'angle ?

</details>
<details><summary>Indice 3</summary>

La méthode polaire (Box-Muller) : tire $U_1$ et $U_2$ ; pose $R = \sqrt{-2\ln(1 - U_1)}$ (car $R^2$ suit la loi exponentielle d'espérance 2) et $\Theta = 2\pi U_2$ ; alors $R\cos\Theta$ et $R\sin\Theta$ sont deux normales indépendantes. Avec NumPy, sur des arrays de taille $\lceil n/2 \rceil$, puis `np.concatenate`.

</details>
