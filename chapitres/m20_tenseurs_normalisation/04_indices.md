# M20 · Tenseurs, axes et estimateurs pondérés — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M20.Q1 — Forme, axes et nombre d'éléments

<details><summary>Indice 1</summary>

Relis « Un tableau, sa forme, ses axes » et « Remodeler, transposer » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Fixer un indice enlève l'axe correspondant ; `:` le garde. Un remodelage garde l'ordre de la file ; une transposition change l'ordre des axes. 6. Les pas de la file sont $7 \times 24$, $24$ et $1$.

</details>
<details><summary>Indice 3</summary>

1. $600 \times 800 \times 3$. 2. `img[100]` fixe l'indice de ligne. 4. $-1$ vaut $\frac{1\,440\,000}{3}$. 5. Écris la première « ligne » de 800 nombres du remodelage : ce sont les intensités des 266 premiers pixels et deux tiers, pas un canal. 6. $(0 \times 7 + 1) \times 24 + 0$.

</details>

### M20.Q2 — Réduire le long de quel axe ?

<details><summary>Indice 1</summary>

Relis « Réduire le long d'un axe » et « La diffusion » (fiche §2).

</details>
<details><summary>Indice 2</summary>

L'axe nommé est celui qui **disparaît** : pour une valeur par élève, il faut faire disparaître les matières. 5. Aligne les formes à droite. 6. Relis « Réduire en plusieurs fois ».

</details>
<details><summary>Indice 3</summary>

1. `axis=1`. 3. Il reste l'axe des heures. 5. $(10, 365, 24)$ contre $(10, 365)$ : compare $24$ et $365$.

</details>

### M20.Q3 — Lire une formule d'einsum

<details><summary>Indice 1</summary>

Relis le tableau des formules de `einsum` et « Le coût d'une contraction » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Les lettres après `->` restent ; toutes les autres sont sommées. Un résultat sans lettre est un nombre. 6. Une multiplication par combinaison de valeurs de **toutes** les lettres.

</details>
<details><summary>Indice 3</summary>

2. $\sum_{i,j}A_{ij}B_{ij}$. 4. $\sum_j A_{ij}B_{kj} = \sum_j A_{ij}(\mathbf{B}^\top)_{jk}$. 5. Les lettres absentes de `ad`. 6. $50 \times 20 \times 30$.

</details>

### M20.Q4 — Diviser par une probabilité : sans biais ou biaisé ?

<details><summary>Indice 1</summary>

Relis l'encadré « Horvitz-Thompson », « L'estimateur naïf » et l'erreur classique du §5.

</details>
<details><summary>Indice 2</summary>

1. Le terme d'une unité tirée est $y_i/\pi_i$. 4. Les unités tirées ressemblent-elles à la population ? 5. Le terme de variance est $y_i^2(1 - \pi_i)/\pi_i$. 6. L'unité de probabilité nulle n'est jamais dans l'échantillon.

</details>
<details><summary>Indice 3</summary>

1. $1\,200/0{,}05$. 6. $\mathbb{E}[\hat Y] = \sum_{i \ne j}\pi_i\,\frac{y_i}{\pi_i}$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M20.R1 — Variance biaisée et non biaisée : ddof (M02c)

<details><summary>Indice 1</summary>

Relis « Moyenne et variance le long d'axes, et ddof » (fiche §2).

</details>
<details><summary>Indice 2</summary>

La moyenne vaut 6 ; la somme des carrés des écarts se divise par $N - \text{ddof}$. pandas utilise ddof = 1 par défaut.

</details>
<details><summary>Indice 3</summary>

Les écarts : $-2, 4, 1, -4, 1$, de carrés de somme 38. 5. $\frac{N}{N - 1} < 1{,}05$ s'écrit $N > 1{,}05\,(N - 1)$.

</details>

### M20.R2 — La projection orthogonale sur une droite (M12b)

<details><summary>Indice 1</summary>

Relis la projection sur une droite de M12b, et « La matrice de centrage » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$\mathbf{p} = \frac{\mathbf{a}^\top\mathbf{x}}{\mathbf{a}^\top\mathbf{a}}\,\mathbf{a}$. La trace de $\mathbf{a}\mathbf{a}^\top$ vaut $\mathbf{a}^\top\mathbf{a}$.

</details>
<details><summary>Indice 3</summary>

1. $\mathbf{a}^\top\mathbf{x} = 9$ et $\mathbf{a}^\top\mathbf{a} = 9$. 4. $\frac{\mathbf{1}^\top\mathbf{x}}{3}\,\mathbf{1}$ : la moyenne fois $\mathbf{1}$.

</details>

### M20.R3 — La limite (1 + x/n)ⁿ → eˣ (M14)

<details><summary>Indice 1</summary>

Relis « Le cas linéaire » (fiche §6) et la limite de M14.

</details>
<details><summary>Indice 2</summary>

3. $n\ln(1 + x/n) \approx n\left(\frac xn - \frac{x^2}{2n^2}\right)$.

</details>
<details><summary>Indice 3</summary>

3. L'écart est $-\frac{x^2}{2n}$, soit $-0{,}02$ pour $x = -2$ et $n = 100$ : le quotient des deux valeurs vaut environ $e^{-0{,}02}$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M20.1 — Un tableau de mesures (stations × jours × heures) : les formes après réductions et remodelages

<details><summary>Indice 1</summary>

Fiche §1 (l'ordre C, le remodelage, la transposition) et §2 (réductions, `keepdims`, diffusion).

</details>
<details><summary>Indice 2</summary>

d) Les pas de la file sont $28 \times 24$, $24$ et $1$. e) Divise d'abord par $28 \times 24$, puis le reste par 24. f) Le remodelage découpe l'axe des jours : le jour $d$ s'écrit $7 \times \text{semaine} + \text{jour de la semaine}$. h) Aligne les formes à droite. i) Le nouvel axe $k$ est l'ancien axe numéro $(2, 0, 1)[k]$.

</details>
<details><summary>Indice 3</summary>

d) $(3 \times 28 + 10) \times 24 + 5$. e) $1\,000 = 1 \times 672 + 328$, puis $328 = 13 \times 24 + 16$. f) La semaine 1, le jour de la semaine 3. g) L'axe 1 de `R` est celui des semaines.

</details>

### Ex M20.2 — Écrire en notation d'Einstein : produit matriciel, trace, forme bilinéaire, produits de matrices empilées le long d'un axe

<details><summary>Indice 1</summary>

Fiche §3 : les deux tableaux de traductions, et « Le coût d'une contraction ».

</details>
<details><summary>Indice 2</summary>

c) $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \sum_i(\mathbf{A}\mathbf{B})_{ii} = A_{ij}B_{ji}$ : avec les axes de $\mathbf{A}$ notés `ij`, ceux de $\mathbf{B}$ sont `ji`. f) Calcule d'abord $\mathbf{M}\mathbf{y}$. g) Pour chaque $s$, la ligne $s$ du résultat est $\mathbf{M}_s\mathbf{v}_s$. h) Le produit des longueurs de $s$, $i$, $j$, $k$. i) Un produit $(m, n) \times (n, p)$ coûte $mnp$ ; il y en a deux.

</details>
<details><summary>Indice 3</summary>

b) La ligne 2 de $\mathbf{A}$ est $(0, -1)$, la colonne 3 de $\mathbf{B}$ est $(1, 4)$. d) $\mathbf{A}\mathbf{B}$ a la diagonale $(4, 1, 7)$. f) $\mathbf{M}\mathbf{y} = (9, -3)$. i) $\mathbf{P}\mathbf{Q}$ coûte $30 \times 300 \times 5$, puis $(\mathbf{P}\mathbf{Q})\mathbf{R}$ coûte $30 \times 5 \times 50$.

</details>

### Ex M20.3 — La matrice de centrage, et une standardisation qui ne voit ni translation ni dilatation

<details><summary>Indice 1</summary>

Fiche §4 : « La matrice de centrage », « Pourquoi m − 1 », l'encadré « Invariances ».

</details>
<details><summary>Indice 2</summary>

$C_{ii} = 1 - \frac1m$, $C_{ij} = -\frac1m$. $\mathbf{C}\mathbf{x} = \mathbf{x} - \bar x\,\mathbf{1}$. $\lVert\bar x\,\mathbf{1}\rVert^2 = m\,\bar x^2$. Avec ddof = 1, $s^2 = \lVert\mathbf{C}\mathbf{x}\rVert^2/(m - 1)$.

</details>
<details><summary>Indice 3</summary>

$\bar x = 6$. g) $s^2 = 28/5$. h) $z_6 = 2/s$. i) et j) Applique l'encadré : $a = 2{,}5 > 0$, puis $a = -2 < 0$.

</details>

### Ex M20.4 — Un sondage à probabilités inégales : l'estimateur de Horvitz-Thompson d'un total, son espérance et sa variance

<details><summary>Indice 1</summary>

Fiche §5 : l'encadré « Horvitz-Thompson », l'exemple de la forêt et « L'estimateur naïf ».

</details>
<details><summary>Indice 2</summary>

b) Le poids de sondage est $1/\pi_i$. c) Seules les entreprises 1, 4 et 6 entrent dans la somme. f) Un terme $y_i^2(1 - \pi_i)/\pi_i$ par entreprise, tirée ou non. h) Les tirages sont indépendants : multiplie les $\pi_i$ des entreprises tirées et les $1 - \pi_i$ des autres.

</details>
<details><summary>Indice 3</summary>

c) $\frac{2}{0{,}05} + \frac{30}{0{,}9} + \frac{3}{0{,}05}$. f) Les termes valent $76$, $225$, $336$, $100$, $362{,}67$ et… le dernier, à toi. j) Que devient $\frac{1 - \pi}{\pi} = \frac1\pi - 1$ quand $\pi$ grandit ?

</details>

### Ex M20.5 — Un schéma d'Euler en L pas : la jacobienne d'un pas, celle de L pas, et la limite (1 + λT/L)ᴸ

<details><summary>Indice 1</summary>

Fiche §6 : « Un pas d'Euler et sa jacobienne », « Le cas linéaire », l'exemple de la rotation.

</details>
<details><summary>Indice 2</summary>

c) Chaque pas multiplie par $1 + h\lambda$. e) $e^{\lambda T}$. f) $\mathbf{I} + h\mathbf{J}$ avec $h = 0{,}1$. g) Si $\mathbf{U}^\top\mathbf{U} = c\,\mathbf{I}$, les valeurs singulières de $\mathbf{U}$ valent $\sqrt c$, et celles de $\mathbf{U}^L$ valent $c^{L/2}$. j) La jacobienne de $F$ est $\begin{pmatrix} 0 & 1 \\ -\cos x & 0 \end{pmatrix}$, et $h = 0{,}05$.

</details>
<details><summary>Indice 3</summary>

c) $0{,}52^5$. d) $(1 - 2{,}4/50)^{50}$. g) $(1 + 4 \times 0{,}01)^{5}$, calculé directement (passer par $\sqrt{1{,}04}$ arrondi fait perdre la troisième décimale de justesse). h) $(1 + 4 \times 10^{-4})^{50}$. k) $\det\begin{pmatrix} 1 & h \\ -h\cos x & 1 \end{pmatrix} = 1 + h^2\cos x$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M20.6 — La matrice de centrage est la projection orthogonale sur l'orthogonal de 1

<details><summary>Indice 1</summary>

Relis « La matrice de centrage » et « Pourquoi m − 1 » (fiche §4), et la caractérisation d'une projection orthogonale de M12b.

</details>
<details><summary>Indice 2</summary>

1. Développe $\left(\mathbf{I} - \frac1m\mathbf{1}\mathbf{1}^\top\right)^2$ ; le produit $\mathbf{1}\mathbf{1}^\top\mathbf{1}\mathbf{1}^\top$ contient $\mathbf{1}^\top\mathbf{1} = m$. 3. Écris $\mathbf{x} - \mathbf{C}\mathbf{x} = \bar x\,\mathbf{1}$. 4. Un vecteur de $H$ et $\mathbf{1}$ sont des vecteurs propres. 5. Pythagore sur $\mathbf{x} = \bar x\,\mathbf{1} + \mathbf{C}\mathbf{x}$.

</details>
<details><summary>Indice 3</summary>

1. $\mathbf{C}^2 = \mathbf{I} - \frac2m\mathbf{1}\mathbf{1}^\top + \frac{1}{m^2}\mathbf{1}(\mathbf{1}^\top\mathbf{1})\mathbf{1}^\top$. 3. Pour $\mathbf{v} \in H$, $\mathbf{v}^\top(\bar x\,\mathbf{1}) = \bar x\,(\mathbf{1}^\top\mathbf{v}) = 0$. 4. $H$ est de dimension $m - 1$ (le noyau d'une forme linéaire non nulle). 6. Une colonne de $\mathbf{C}_m\mathbf{X}$ est $\mathbf{C}_m$ fois la colonne de $\mathbf{X}$.

</details>

### Ex M20.7 — L'estimateur de Horvitz-Thompson est sans biais, et sa variance quand les inclusions sont indépendantes

<details><summary>Indice 1</summary>

Relis l'encadré « Horvitz-Thompson » (fiche §5), et l'espérance et la variance d'une variable de Bernoulli (M02b).

</details>
<details><summary>Indice 2</summary>

1. Linéarité de l'espérance, et $\mathbb{E}[I_i] = \pi_i$. 2. La variance d'une somme de variables indépendantes est la somme des variances, et la variance d'une Bernoulli est connue (M02b). 3. Écris $\hat V = \sum_i I_i\,y_i^2\,\frac{1 - \pi_i}{\pi_i^2}$. 4. Remplace $\pi_i$ par $c\,y_i$ dans la formule de la question 2. 5. L'unité $j$ n'apparaît jamais dans la somme.

</details>
<details><summary>Indice 3</summary>

2. Sors la constante $y_i/\pi_i$ de la variance, au carré. 3. $\mathbb{E}[\hat V] = \sum_i\pi_i\,y_i^2\,\frac{1 - \pi_i}{\pi_i^2}$ ; la formule de la question 2 demande les $y_i$ des unités **non** tirées. 4. Chaque unité tirée apporte $1/c$ : $\hat Y = n/c$, où $n$ est le nombre d'unités tirées.

</details>

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M20.8 — Pont : où workbookIA 20 divise par une probabilité

<details><summary>Indice 1</summary>

Dans la fiche de workbookIA 20, parcours les sous-sections de « Un tour d'horizon des couches » et cherche une division par une expression qui contient une probabilité.

</details>
<details><summary>Indice 2</summary>

La division est dans une formule écrite pour la version de la couche qu'utilisent les bibliothèques. b) Relis les titres des sections de cette fiche-ci.

</details>
<details><summary>Indice 3</summary>

a) La couche dont la version utilisée par les bibliothèques s'appelle « inversée ». b) Le §5.

</details>

### Ex M20.9 — Expliquer ce qu'est un axe d'un tableau à quelqu'un qui ne connaît que les tableurs

<details><summary>Indice 1</summary>

Relis les exemples du §1 et du §2 sur le tableau des stations.

</details>
<details><summary>Indice 2</summary>

Un onglet par station, une ligne par jour, une colonne par heure. « La moyenne le long de l'axe 1 » : une formule qui fait la moyenne d'une colonne de chaque onglet.

</details>
<details><summary>Indice 3</summary>

Le plan : le classeur ; un axe = une direction de lecture ; réduire = écrire une formule qui écrase une direction ; garder un axe de longueur 1 = garder la place de chaque résultat pour pouvoir le soustraire case par case ; la limite : un quatrième axe n'a plus d'image dans un classeur.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M20.E1 — « Pourquoi standardiser des données décalées ou dilatées donne-t-il le même résultat ? »

<details><summary>Indice 1</summary>

Relis l'encadré « Invariances » et l'exemple des degrés Fahrenheit (fiche §4).

</details>
<details><summary>Indice 2</summary>

Ce que deviennent la moyenne, les écarts à la moyenne et l'écart type quand on remplace $x_i$ par $ax_i + b$.

</details>
<details><summary>Indice 3</summary>

Le plan : la formule ; la translation retirée par le centrage ; la dilatation retirée par la division ; le signe de $a$ ; ce qui n'est pas gommé (une seule valeur modifiée, une valeur aberrante) ; l'intérêt pratique (les unités).

</details>

<a id="notebook"></a>

## Notebook
