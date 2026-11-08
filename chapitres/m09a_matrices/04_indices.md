# M09a · Matrices et systèmes linéaires — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M09a.Q1 — Formes : ce qui se multiplie et ce qui ne se multiplie pas

<details><summary>Indice 1</summary>

Relis « Lignes, colonnes, forme » (fiche §1) et « La règle des formes et la définition » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$(n, p) \times (p, m) \to (n, m)$ : les dimensions intérieures doivent être égales, il reste les extérieures.

</details>
<details><summary>Indice 3</summary>

2 : compare le nombre de colonnes de $\mathbf{A}$ au nombre de lignes de $\mathbf{C}$. 6 : une ligne par exemple.

</details>

### M09a.Q2 — Le produit matrice-vecteur, deux lectures

<details><summary>Indice 1</summary>

Relis la fiche §2.

</details>
<details><summary>Indice 2</summary>

Par les lignes : $(\mathbf{A}\mathbf{x})_i$ est le produit scalaire de la ligne $i$ avec $\mathbf{x}$. Par les colonnes : $\mathbf{A}\mathbf{x} = x_1\mathbf{a}_1 + x_2\mathbf{a}_2$.

</details>
<details><summary>Indice 3</summary>

3 : quels coefficients donne $\mathbf{e}_2$ aux colonnes ? 5 : si $\mathbf{a}_j = 2\mathbf{a}_k$, que vaut $2\mathbf{a}_k - \mathbf{a}_j$ ?

</details>

### M09a.Q3 — Produit matriciel : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Les règles de calcul » et « Le coût d'un produit » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Un seul contre-exemple suffit à réfuter une règle. Le produit est associatif et distributif, mais pas commutatif.

</details>
<details><summary>Indice 3</summary>

3 : cherche une matrice $2 \times 2$ non nulle dont le carré est nul (un seul 1, hors de la diagonale). 4 : développe $(\mathbf{A} + \mathbf{B})(\mathbf{A} + \mathbf{B})$ sans échanger les facteurs. 6 : pense à M09a.4.

</details>

### M09a.Q4 — Hadamard ou produit matriciel ?

<details><summary>Indice 1</summary>

Relis « Le produit de Hadamard » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Hadamard multiplie les éléments de même position ; le produit matriciel fait des produits scalaires de lignes et de colonnes.

</details>
<details><summary>Indice 3</summary>

4 : $\mathbf{I}_2 \odot \mathbf{A}$ multiplie chaque élément de $\mathbf{A}$ par 1 ou par 0. 5 : un masque agit élément par élément.

</details>

### M09a.Q5 — Les règles de la transposée

<details><summary>Indice 1</summary>

Relis « Définition et règles » et « La matrice $\mathbf{X}^\top\mathbf{X}$ » (fiche §4).

</details>
<details><summary>Indice 2</summary>

La transposée échange lignes et colonnes ; la transposée d'un produit inverse l'ordre des facteurs.

</details>
<details><summary>Indice 3</summary>

4 : applique deux fois la règle à $(\mathbf{A}\mathbf{B})\mathbf{C}$. 5 : $(8, 1000) \times (1000, 8)$. 6 : calcule la transposée de $\mathbf{X}^\top\mathbf{X}$.

</details>

### M09a.Q6 — Combien de solutions ?

<details><summary>Indice 1</summary>

Relis la fiche §5.

</details>
<details><summary>Indice 2</summary>

Un système linéaire a 0, 1 ou une infinité de solutions ; un système homogène a toujours au moins une solution.

</details>
<details><summary>Indice 3</summary>

2 : pense à M09a.17. 5 : que dit la ligne $(0 \;\; 0 \;\; 0 \mid 5)$ ? 6 : combien de pivots au plus, pour combien d'inconnues ?

</details>

### M09a.Q7 — Les opérations permises sur les lignes

<details><summary>Indice 1</summary>

Relis « Les opérations qui ne changent pas les solutions » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Une opération est permise si l'on peut revenir en arrière par une autre opération : alors aucune solution n'est perdue ni ajoutée.

</details>
<details><summary>Indice 3</summary>

3 : peut-on retrouver la ligne de départ ? 6 : écris les deux nouvelles lignes ; que remarques-tu ?

</details>

### M09a.Q8 — Inverse et rang

<details><summary>Indice 1</summary>

Relis les fiches §7 et §8.

</details>
<details><summary>Indice 2</summary>

Seule une matrice carrée peut avoir une inverse ; le rang est le nombre de pivots, au plus le plus petit des deux nombres de lignes et de colonnes.

</details>
<details><summary>Indice 3</summary>

4 : compare les deux lignes. 5 : pense aux chaussettes et aux chaussures (on retire d'abord ce qu'on a mis en dernier).

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M09a.R1 — Les systèmes 2 × 2 (R2)

<details><summary>Indice 1</summary>

Relis R2 (systèmes de deux équations).

</details>
<details><summary>Indice 2</summary>

Par substitution : exprime $x$ avec la seconde équation, puis remplace dans la première.

</details>
<details><summary>Indice 3</summary>

2 et 3 : compare la seconde équation au double de la première. 4 : le système n'a pas une solution unique quand $ad - bc = 0$.

</details>

### M09a.R2 — Produit scalaire et normes (M07)

<details><summary>Indice 1</summary>

Relis M07 (produit scalaire, norme).

</details>
<details><summary>Indice 2</summary>

$\mathbf{u} \cdot \mathbf{v} = \sum_i u_i v_i$ et $\lVert \mathbf{u} \rVert = \sqrt{\mathbf{u} \cdot \mathbf{u}}$.

</details>
<details><summary>Indice 3</summary>

5 : un vecteur orthogonal à $(0, 0, 1)$ a une troisième coordonnée nulle ; écris $(a, b, 0) \cdot \mathbf{u} = 0$.

</details>

### M09a.R3 — Moyenne et écart-type empiriques (M02c)

<details><summary>Indice 1</summary>

Relis M02c (moyenne, variance, écart-type).

</details>
<details><summary>Indice 2</summary>

Les écarts à la moyenne, leurs carrés, puis leur somme divisée par $n$ ($\mathrm{ddof} = 0$) ou par $n - 1$ ($\mathrm{ddof} = 1$), et la racine.

</details>
<details><summary>Indice 3</summary>

La somme des carrés des écarts vaut 20. 5 : (valeur − moyenne) / écart-type.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M09a.1 — Un tableau de données vu comme une matrice : forme, lignes, colonnes, moyennes

<details><summary>Indice 1</summary>

Relis « Lignes, colonnes, forme » et « Trois façons d'opérer sur un tableau » (fiche §1).

</details>
<details><summary>Indice 2</summary>

$x_{ij}$ est à la ligne $i$ et à la colonne $j$ ; en Python, `X[i - 1, j - 1]`. Les moyennes se calculent **par colonne**.

</details>
<details><summary>Indice 3</summary>

e) Les sommes des colonnes valent 110, 300 et 60. g) Les écarts des températures à leur moyenne valent $0, 3, -3, 2, -2$.

</details>

### Ex M09a.2 — Le produit matrice-vecteur, par les lignes puis par les colonnes

<details><summary>Indice 1</summary>

Relis la fiche §2.

</details>
<details><summary>Indice 2</summary>

Par les lignes : un produit scalaire par ligne de $\mathbf{A}$. Par les colonnes : $\mathbf{A}\mathbf{x} = x_1\mathbf{a}_1 + \cdots + x_4\mathbf{a}_4$.

</details>
<details><summary>Indice 3</summary>

d) Quels coefficients $\mathbf{e}_3$ donne-t-il aux colonnes ? e) Quel coefficient faut-il pour la colonne 1, pour la colonne 4, pour les autres ? g) Une prédiction par ligne de $\mathbf{X}$, plus $b$.

</details>

### Ex M09a.3 — Produits matriciels à la main : formes compatibles et calculs

<details><summary>Indice 1</summary>

Relis « La règle des formes et la définition » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Écris d'abord les formes : $(2, 3) \times (3, 2)$, $(3, 2) \times (2, 3)$… L'élément $(i, j)$ est le produit scalaire de la ligne $i$ de la première matrice et de la colonne $j$ de la seconde.

</details>
<details><summary>Indice 3</summary>

d) La ligne 2 de $\mathbf{B}$ est $(-1, 0)$, la colonne 3 de $\mathbf{A}$ est $(2, 1)$. g) Pars de b), puis multiplie à droite par $\mathbf{C}$.

</details>

### Ex M09a.4 — Le coût d'un produit, et l'ordre des parenthèses dans ABC

<details><summary>Indice 1</summary>

Relis « Le coût d'un produit, et l'ordre des parenthèses » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Un produit $(n, p) \times (p, m)$ coûte $n\,p\,m$ multiplications ; pour un produit de trois matrices, additionne les coûts des deux produits, avec la forme du résultat intermédiaire.

</details>
<details><summary>Indice 3</summary>

b) $\mathbf{A}\mathbf{B}$ a la forme $(20, 5)$. c) $\mathbf{B}\mathbf{C}$ a la forme $(400, 300)$. f) Trois produits matrice-vecteur, de droite à gauche.

</details>

### Ex M09a.5 — Une couche dense Z = XW + b à la main : deux exemples, trois entrées, deux sorties

<details><summary>Indice 1</summary>

Relis « Une couche dense : $\mathbf{Z} = \mathbf{X}\mathbf{W} + \mathbf{b}$ » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\mathbf{X}\mathbf{W}$ a une ligne par exemple et une colonne par neurone ; $\mathbf{b}$ s'ajoute à chaque ligne, $b_j$ à la colonne $j$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{X}\mathbf{W} = \begin{pmatrix} 4 & 5 \\ -1 & 7 \end{pmatrix}$. f) PyTorch range une ligne par neurone.

</details>

### Ex M09a.6 — Un embedding : une ligne one-hot fois une matrice

<details><summary>Indice 1</summary>

Relis « Un embedding est un produit par un vecteur one-hot » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Une ligne fois $\mathbf{E}$ est une combinaison des **lignes** de $\mathbf{E}$, de coefficients les nombres de la ligne.

</details>
<details><summary>Indice 3</summary>

e) Les coefficients valent 1 pour les lignes 2 et 5. f) $\frac{1}{3}(\text{ligne } 1 + 2 \times \text{ligne } 3)$.

</details>

### Ex M09a.7 — Transposées de produits, et la matrice symétrique XᵀX

<details><summary>Indice 1</summary>

Relis la fiche §4.

</details>
<details><summary>Indice 2</summary>

Calcule $\mathbf{A}\mathbf{B}$ et $\mathbf{B}\mathbf{A}$, puis échange leurs lignes et leurs colonnes. L'élément $(i, j)$ de $\mathbf{X}^\top\mathbf{X}$ est le produit scalaire des colonnes $i$ et $j$ de $\mathbf{X}$.

</details>
<details><summary>Indice 3</summary>

d) Compare les formes de $\mathbf{A}^\top\mathbf{B}^\top$ et de $(\mathbf{A}\mathbf{B})^\top$. e) Les colonnes de $\mathbf{X}$ sont $(1, 0, 2, 1)$, $(-1, 2, 1, 0)$ et $(2, 1, 0, -1)$. g) Les lignes 1 et 2 de $\mathbf{X}$.

</details>

### Ex M09a.8 — Le pivot de Gauss sur un système 3 × 3 à solution unique

<details><summary>Indice 1</summary>

Relis « Descendre l'escalier, puis remonter » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Écris la matrice augmentée après l'échange ; chaque opération porte sur les quatre nombres de la ligne, second membre compris.

</details>
<details><summary>Indice 3</summary>

a) Le premier nombre de la ligne, 2, divisé par le pivot, 1. d) Le nombre à annuler, 5, divisé par le pivot de la deuxième ligne, 3. e) La troisième ligne devient $(0, 0, \frac{10}{3} \mid 10)$.

</details>

### Ex M09a.9 — Un système sans solution, un système à une infinité de solutions

<details><summary>Indice 1</summary>

Relis « Trois cas, et seulement trois » (fiche §5) et « La forme échelonnée réduite » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Applique les opérations de l'énoncé aux deux systèmes : seule la dernière colonne change. Une ligne $(0 \;\; 0 \;\; 0 \mid c)$ avec $c \ne 0$ n'a pas de solution.

</details>
<details><summary>Indice 3</summary>

c) Après élimination, annule le 2 au-dessus du second pivot. e) et f) Exprime $x$ et $y$ en fonction de $z$. g) Compare la troisième ligne des coefficients aux deux premières.

</details>

### Ex M09a.10 — La forme échelonnée réduite d'une matrice 3 × 4 et la solution générale

<details><summary>Indice 1</summary>

Relis « La forme échelonnée réduite » (fiche §6).

</details>
<details><summary>Indice 2</summary>

$L_2 - 2L_1$, puis la troisième ligne moins la nouvelle deuxième, puis annule le nombre au-dessus du second pivot.

</details>
<details><summary>Indice 3</summary>

La forme réduite donne $x + 3z = 3$ et $y + z = 2$. f) Remplace les seconds membres par 0.

</details>

### Ex M09a.11 — L'inverse d'une matrice 2 × 2, par la formule, puis vérifiée

<details><summary>Indice 1</summary>

Relis « Le cas $2 \times 2$ » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.

</details>
<details><summary>Indice 3</summary>

c) $\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$ avec $\mathbf{b} = (10, 7)$. d) $ad - bc = 2k - 6$. f) Que vaut $(2\mathbf{A})(\frac{1}{2}\mathbf{A}^{-1})$ ? g) Les règles de la fiche §7.

</details>

### Ex M09a.12 — L'inverse d'une matrice 3 × 3 par Gauss-Jordan

<details><summary>Indice 1</summary>

Relis « Gauss-Jordan sur $[\mathbf{A} \mid \mathbf{I}]$ » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Réduis $[\mathbf{A} \mid \mathbf{I}_3]$ jusqu'à $[\mathbf{I}_3 \mid \mathbf{A}^{-1}]$, chaque opération portant sur les six nombres de la ligne.

</details>
<details><summary>Indice 3</summary>

Commence par $L_3 \leftarrow L_3 - L_1$, puis $L_1 \leftarrow L_1 - 2L_2$ et $L_3 \leftarrow L_3 + L_2$. c) $\mathbf{A}^{-1}\mathbf{e}_2$. d) $(\mathbf{A}^\top)^{-1} = (\mathbf{A}^{-1})^\top$. e) Additionne les deux premières lignes.

</details>

### Ex M09a.13 — Le rang de quatre matrices, et les colonnes redondantes

<details><summary>Indice 1</summary>

Relis la fiche §8.

</details>
<details><summary>Indice 2</summary>

Échelonne chaque matrice et compte les pivots ; ou cherche les colonnes qui combinent les autres.

</details>
<details><summary>Indice 3</summary>

b) et e) Écris $(2, -1, 1) = a\,(1, 0, 1) + b\,(0, 1, 1)$. c) Essaie d'écrire les colonnes 3 et 4 de $\mathbf{M}_3$ avec les colonnes 1 et 2. g) Rang des lignes et rang des colonnes.

</details>

### Ex M09a.14 — Mettre un problème en système : trois engrais pour trois nutriments

<details><summary>Indice 1</summary>

Relis « Écrire un système comme $\mathbf{A}\mathbf{x} = \mathbf{b}$ » (fiche §5).

</details>
<details><summary>Indice 2</summary>

L'équation de l'azote : $200x + 100y + 0z = 1100$. Une ligne par nutriment, une colonne par engrais.

</details>
<details><summary>Indice 3</summary>

b) De la première équation, $y = 11 - 2x$ ; de la deuxième, $x = 7 - 1{,}5z$ ; remplace dans la troisième. d) La même méthode avec 1 000 g de potassium.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M09a.15 — (AB)ᵀ = BᵀAᵀ, coefficient par coefficient

<details><summary>Indice 1</summary>

Relis les définitions du produit (fiche §3) et de la transposée (fiche §4).

</details>
<details><summary>Indice 2</summary>

$(\mathbf{M}^\top)_{ij} = m_{ji}$ et $(\mathbf{A}\mathbf{B})_{ij} = \sum_k a_{ik}b_{kj}$.

</details>
<details><summary>Indice 3</summary>

2 : $\big((\mathbf{A}\mathbf{B})^\top\big)_{ij} = (\mathbf{A}\mathbf{B})_{ji}$. 3 : $(\mathbf{B}^\top)_{ik} = b_{ki}$ et $(\mathbf{A}^\top)_{kj} = a_{jk}$. 6 : $(\mathbf{X}^\top)^\top = \mathbf{X}$.

</details>

### Ex M09a.16 — L'inverse est unique, et (AB)⁻¹ = B⁻¹A⁻¹

<details><summary>Indice 1</summary>

Relis la définition de l'inverse (fiche §7).

</details>
<details><summary>Indice 2</summary>

Une matrice $\mathbf{M}$ est l'inverse de $\mathbf{A}$ si $\mathbf{A}\mathbf{M} = \mathbf{M}\mathbf{A} = \mathbf{I}$ : il faut vérifier **les deux** produits, et l'associativité permet de regrouper.

</details>
<details><summary>Indice 3</summary>

1 : $\mathbf{B} = \mathbf{B}(\mathbf{A}\mathbf{C})$. 3 : transpose $\mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$. 5 : prends une matrice $\mathbf{A}$ dont les colonnes sont proportionnelles, et $\mathbf{B} = \mathbf{0}$.

</details>

### Ex M09a.17 — Deux solutions distinctes entraînent une infinité de solutions

<details><summary>Indice 1</summary>

Relis « Trois cas, et seulement trois » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Le produit est distributif : $\mathbf{A}(\mathbf{u} + t\,\mathbf{v}) = \mathbf{A}\mathbf{u} + t\,\mathbf{A}\mathbf{v}$.

</details>
<details><summary>Indice 3</summary>

3 : calcule la différence de deux solutions obtenues avec $t \ne t'$. 4 : pose $\mathbf{h} = \mathbf{y} - \mathbf{x}$.

</details>

### Ex M09a.18 — Une matrice dont une colonne combine les autres n'est pas inversible

<details><summary>Indice 1</summary>

Relis « Par les colonnes : une combinaison linéaire » (fiche §2) et « Rang, inverse et solutions » (fiche §8).

</details>
<details><summary>Indice 2</summary>

$\mathbf{A}\mathbf{c} = c_1\mathbf{a}_1 + \cdots + c_n\mathbf{a}_n$ : choisis les $c_i$ pour que cette somme s'annule.

</details>
<details><summary>Indice 3</summary>

1 : la dernière coordonnée de $\mathbf{c}$ vaut $-1$. 2 : multiplie $\mathbf{A}\mathbf{c} = \mathbf{0}$ par $\mathbf{A}^{-1}$. 5 : que vaut la somme des colonnes du one-hot ?

</details>

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M09a.19 — Pont : une passe avant à deux couches, deux produits matriciels et leurs formes

<details><summary>Indice 1</summary>

Relis « Une couche dense » (fiche §3) et M09a.5.

</details>
<details><summary>Indice 2</summary>

Suis les formes : $(64, 3) \to (64, 5) \to (64, 2)$. Chaque couche a un poids par couple (entrée, neurone) et un biais par neurone.

</details>
<details><summary>Indice 3</summary>

e) $\mathbf{x}\mathbf{W}_1 = 1 \times (1, 0, 2) - 1 \times (-1, 1, 1)$, puis $+\,\mathbf{b}_1$, puis ReLU. g) Développe $(\mathbf{X}\mathbf{W}_1 + \mathbf{b}_1)\mathbf{W}_2 + \mathbf{b}_2$.

</details>

### Ex M09a.20 — Pont : centrer et réduire un tableau en écriture matricielle

<details><summary>Indice 1</summary>

Relis « Trois façons d'opérer sur un tableau » (fiche §1) et la fiche §4.

</details>
<details><summary>Indice 2</summary>

$\mathbf{1}\boldsymbol{\mu}^\top$ répète $\boldsymbol{\mu}^\top$ sur chaque ligne. Multiplier à droite par une matrice diagonale multiplie chaque colonne par un nombre.

</details>
<details><summary>Indice 3</summary>

d) $\sigma_1 = \sqrt{\frac{8}{3}}$, $\sigma_2 = \sqrt{\frac{200}{3}}$. f) Les colonnes centrées sont $(-2, 0, 2)$ et $(-10, 10, 0)$. g) Divise la covariance par le produit des écarts-types.

</details>

### Ex M09a.21 — MML §2.1 et §2.2 : systèmes et matrices, en anglais

<details><summary>Indice 1</summary>

Lis les sections dans l'ordre, en t'arrêtant à chaque exemple pour le refaire.

</details>
<details><summary>Indice 2</summary>

Cherche les mots *intersection*, *Hadamard product*, *invertible*, *singular*, *symmetric*, *linear combination*.

</details>
<details><summary>Indice 3</summary>

Pour chaque règle trouvée au §2.2.2, retrouve la ligne de la fiche §4 ou §7 qui la donne.

</details>

### Ex M09a.22 — MML §2.3 : résoudre un système, la forme échelonnée et le « Minus-1 trick »

<details><summary>Indice 1</summary>

Lis le §2.3 en refaisant l'exemple de chaque sous-section.

</details>
<details><summary>Indice 2</summary>

Solution générale = une solution particulière + toutes les solutions du système homogène (M09a.17).

</details>
<details><summary>Indice 3</summary>

4 : la matrice complétée est $4 \times 4$ ; ajoute une ligne avec $-1$ en colonne 2, et une avec $-1$ en colonne 4. Vérifie chaque solution sur les deux lignes de départ.

</details>

### Ex M09a.23 — Fermi : combien de multiplications pour une passe avant sur un million d'images ?

<details><summary>Indice 1</summary>

Relis « Le coût d'un produit » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Pour une image, une couche de $n_{\text{in}}$ entrées et $n_{\text{out}}$ neurones coûte $n_{\text{in}}\,n_{\text{out}}$ multiplications.

</details>
<details><summary>Indice 3</summary>

$3\,072 \times 1\,024 + 1\,024 \times 256 + 256 \times 10$. Le temps est le nombre de multiplications divisé par le débit.

</details>

### Ex M09a.24 — Expliquer pourquoi on ne calcule pas l'inverse pour résoudre un système

<details><summary>Indice 1</summary>

Relis « Pourquoi on ne calcule pas l'inverse pour résoudre un système » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Trois arguments : ce que fait `solve` à la place, le coût, la précision.

</details>
<details><summary>Indice 3</summary>

Calculer $\mathbf{A}^{-1}$ revient à résoudre $n$ systèmes ; chaque opération ajoute un arrondi.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M09a.E1 — « Combien coûte un produit matriciel, et pourquoi les GPU l'accélèrent-ils ? »

<details><summary>Indice 1</summary>

Relis « Le coût d'un produit, et l'ordre des parenthèses » (fiche §3) et M09a.23.

</details>
<details><summary>Indice 2</summary>

Le coût : $n\,p\,m$. Le parallélisme : les $n\,m$ produits scalaires sont indépendants.

</details>
<details><summary>Indice 3</summary>

Plan : le coût, le cas carré ($n^3$), le parallélisme et le GPU, un exemple de réseau, le piège des parenthèses (M09a.4).

</details>

<a id="notebook"></a>

## Notebook

### Ex M09a.25 — Le produit matriciel et la transposée · `matmul, transpose`

<details><summary>Indice 1</summary>

Relis la fiche §3 et §4, puis la docstring du module `matrices.py`.

</details>
<details><summary>Indice 2</summary>

Une boucle sur les lignes de $\mathbf{A}$ : la ligne $i$ de $\mathbf{A}\mathbf{B}$ est la combinaison des lignes de $\mathbf{B}$ de coefficients la ligne $i$ de $\mathbf{A}$.

</details>
<details><summary>Indice 3</summary>

`C[i] = np.sum(A[i][:, None] * B, axis=0)`. Transposée : `T[:, i] = A[i]` dans un `np.zeros((m, n))`.

</details>

### Ex M09a.26 — La forme échelonnée réduite et le rang · `rref, rank`

<details><summary>Indice 1</summary>

Relis « La forme échelonnée réduite » et « Le pivot partiel » (fiche §6), puis la docstring de `rref`.

</details>
<details><summary>Indice 2</summary>

Une ligne courante `row` ; pour chaque colonne : le plus grand élément (en valeur absolue) à partir de `row`, l'échange, la division par le pivot, l'élimination dans **toutes** les autres lignes.

</details>
<details><summary>Indice 3</summary>

`best = row + np.argmax(np.abs(R[row:, col]))` ; `R[[row, best]] = R[[best, row]]` ; si le pivot est au plus `tol`, passe à la colonne suivante sans avancer `row`.

</details>

### Ex M09a.27 — Résoudre un système par le pivot de Gauss · `solve`

<details><summary>Indice 1</summary>

Relis « Descendre l'escalier, puis remonter » et « Le pivot partiel » (fiche §6).

</details>
<details><summary>Indice 2</summary>

La matrice augmentée `np.hstack([A, b[:, None]])` ; l'élimination **sous** chaque pivot ; puis la remontée, de la dernière ligne à la première.

</details>
<details><summary>Indice 3</summary>

Remontée : `x[i] = (M[i, n] - np.sum(M[i, i + 1:n] * x[i + 1:])) / M[i, i]`. Singulière si `abs(M[k, k]) <= 1e-12 * np.max(np.abs(A))`.

</details>

### Ex M09a.28 — L'inverse par Gauss-Jordan · `inverse`

<details><summary>Indice 1</summary>

Relis « Gauss-Jordan sur $[\mathbf{A} \mid \mathbf{I}]$ » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Réduis `np.hstack([A, np.eye(n)])` avec ta fonction `rref`, et regarde où sont les pivots.

</details>
<details><summary>Indice 3</summary>

Si `pivots[:n] == tuple(range(n))`, la partie gauche est l'identité, et `R[:, n:]` est l'inverse.

</details>

### Ex M09a.29 — `@`, `*`, `.T`, `np.linalg.solve`, `matrix_rank` et `sympy.Matrix.rref` contre tes fonctions

<details><summary>Indice 1</summary>

Relis l'énoncé : chaque fonction y est nommée.

</details>
<details><summary>Indice 2</summary>

`sympy.Matrix(P).rref()` rend un couple (forme réduite, pivots) ; `.tolist()` transforme un tableau en listes.

</details>
<details><summary>Indice 3</summary>

f) Une boucle sur 20 tirages, `np.allclose(..., rtol=0, atol=1e-9)`, puis `all(...)`.

</details>

### Ex M09a.30 — Prédire la forme du résultat : `@`, `*` et broadcasting

<details><summary>Indice 1</summary>

Relis « Trois façons d'opérer sur un tableau » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Pour `*`, compare les formes en partant de la droite : égales, ou l'une vaut 1. Pour `@`, la règle des formes du produit.

</details>
<details><summary>Indice 3</summary>

a) $(3, 1)$ et $(1, 4)$ : chaque dimension vaut 1 d'un côté. e) À droite, 3 contre 2.

</details>

### Ex M09a.31 — Le temps d'un produit matriciel en fonction de n : une pente de 3 en échelle log-log

<details><summary>Indice 1</summary>

Relis « Le coût d'un produit » (fiche §3) et R6 (logarithmes).

</details>
<details><summary>Indice 2</summary>

Si $t \approx c\,n^3$, alors $\ln t \approx 3\ln n + \ln c$ : une droite de pente 3 en fonction de $\ln n$.

</details>
<details><summary>Indice 3</summary>

`start = time.perf_counter()` juste avant le produit ; `np.polyfit(np.log(ns), np.log(times), 1)[0]`.

</details>

### Ex M09a.32 — Pourquoi le pivot partiel : un petit pivot et les arrondis

<details><summary>Indice 1</summary>

Relis « Le pivot partiel » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Pour chaque $k$, la même matrice avec $\varepsilon = 10^{-k}$ ; l'écart le plus grand entre deux solutions est `np.max(np.abs(x - exact))`.

</details>
<details><summary>Indice 3</summary>

b) `round(math.log10(erreur))` pour $k = 8$. c) Parcours les couples dans l'ordre des $k$ et garde le premier dont l'erreur sans pivot dépasse $10^{-2}$.

</details>

### Ex M09a.33 — Une matrice 2 × 2 comme transformation du plan : la grille et le carré unité

<details><summary>Indice 1</summary>

Relis « Par les colonnes » (fiche §2) et R0 (matplotlib).

</details>
<details><summary>Indice 2</summary>

L'image d'une ligne droite est une ligne droite : transforme ses deux extrémités. Des points rangés en lignes d'un tableau `P` ont pour images les lignes de `P @ M.T`.

</details>
<details><summary>Indice 3</summary>

Le carré : `np.array([[0, 0], [1, 0], [1, 1], [0, 1]]) @ M.T`, puis `ax.add_patch(Polygon(..., closed=True))`.

</details>

### Ex M09a.34 — Chasse à l'erreur : `*` au lieu de `@`, une transposée oubliée, un pivot nul

<details><summary>Indice 1</summary>

Relis le tableau des pièges classiques de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, écris la forme du résultat et refais le calcul de l'élément demandé à la main.

</details>
<details><summary>Indice 3</summary>

(D) : quelle est la forme de `X @ X.T` ? (E) : que vaut `M[0, 0]` ?

</details>

### Ex M09a.35 — Tester une propriété : un pytest pour (AB)ᵀ = BᵀAᵀ sur des matrices aléatoires

<details><summary>Indice 1</summary>

Relis M09a.15, puis l'énoncé.

</details>
<details><summary>Indice 2</summary>

Un générateur créé une fois ; dans la boucle, trois dimensions au hasard, deux matrices, et un `assert` qui compare forme et valeurs.

</details>
<details><summary>Indice 3</summary>

`n, p, m = rng.integers(1, 6, size=3)` ; `assert left.shape == right.shape and np.allclose(left, right, rtol=0, atol=1e-12), f\"expected ...\"`.

</details>

### Ex M09a.36 — Défi : un système 200 × 200 résolu par ton `solve`, à 1e−8 près de NumPy, en moins d'une seconde

<details><summary>Indice 1</summary>

Relis ta fonction `solve` : quelles boucles fait-elle pour chaque pivot ?

</details>
<details><summary>Indice 2</summary>

Toutes les lignes sous le pivot subissent la même opération : retrancher un multiple de la ligne du pivot. Une seule opération NumPy sur le bloc `M[k + 1:]` suffit.

</details>
<details><summary>Indice 3</summary>

`factors = M[k + 1:, k] / M[k, k]` puis `M[k + 1:] = M[k + 1:] - factors[:, None] * M[k]` ; garde l'échange de lignes du pivot partiel.

</details>
