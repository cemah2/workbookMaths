# M12c · Valeurs propres et matrices symétriques — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M12c.Q1 — Ce que mesure un déterminant

<details><summary>Indice 1</summary>

Relis « Ce que mesure un déterminant » (fiche §1).

</details>
<details><summary>Indice 2</summary>

La valeur absolue est un facteur d'aire, le signe dit si la figure est retournée.

</details>
<details><summary>Indice 3</summary>

5 : une rotation ne déforme rien et ne retourne rien ; une symétrie retourne. 6 : pense à $0{,}1\,\mathbf{I}_9$.

</details>

### M12c.Q2 — Les propriétés du déterminant et de la trace : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Les propriétés qui servent » (fiche §1) et le §2.

</details>
<details><summary>Indice 2</summary>

Le déterminant est multiplicatif ; la trace est linéaire, et $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}(\mathbf{B}\mathbf{A})$.

</details>
<details><summary>Indice 3</summary>

2 : multiplier une matrice $n \times n$ par 3 multiplie **chaque ligne** par 3.

</details>

### M12c.Q3 — Reconnaître un vecteur propre

<details><summary>Indice 1</summary>

Relis la définition (fiche §3) : un vecteur propre est **non nul**.

</details>
<details><summary>Indice 2</summary>

Calcule $\mathbf{M}\mathbf{v}$ et regarde s'il est un multiple de $\mathbf{v}$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{M}(2, 3) = (6, 9)$. Pour finir, trace et déterminant contre somme et produit des valeurs propres.

</details>

### M12c.Q4 — Diagonalisable ou pas ?

<details><summary>Indice 1</summary>

Relis « Quand est-ce possible ? » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Des valeurs propres distinctes suffisent ; une valeur propre double demande un espace propre de dimension 2 ; une symétrique est toujours diagonalisable (§6).

</details>
<details><summary>Indice 3</summary>

2 : l'espace propre de 2 est une droite. 4 : une rotation.

</details>

### M12c.Q5 — Ce que garantit le théorème spectral

<details><summary>Indice 1</summary>

Relis « Le théorème spectral » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Le théorème part de la **symétrie** ; il ne dit rien des matrices non symétriques.

</details>
<details><summary>Indice 3</summary>

2 : une matrice triangulaire non symétrique a des valeurs propres réelles. 5 : calcule $(\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top)^\top$.

</details>

### M12c.Q6 — Définie positive, semi-définie positive ou indéfinie ?

<details><summary>Indice 1</summary>

Relis « Le signe de $\mathbf{x}^\top\mathbf{A}\mathbf{x}$ » (fiche §7).

</details>
<details><summary>Indice 2</summary>

En dimension 2 : $a > 0$ et $ac - b^2 > 0$ pour définie positive ; $ac - b^2 = 0$ pour semi-définie ; $ac - b^2 < 0$ pour indéfinie.

</details>
<details><summary>Indice 3</summary>

2 : $36 - 36 = 0$. 3 : essaie $(0, 1)$ et $(1, -1)$.

</details>

### M12c.Q7 — Cholesky, racine carrée, blanchiment : qui est quoi ?

<details><summary>Indice 1</summary>

Relis « La racine carrée d'une matrice » et « Le blanchiment » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Les trois blanchiments vérifient $\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top = \mathbf{I}$ ; une seule racine est symétrique.

</details>
<details><summary>Indice 3</summary>

5 : « Le chemin inverse » (fiche §8).

</details>

### M12c.Q8 — Trace, déterminant et valeurs propres

<details><summary>Indice 1</summary>

Relis « Ce qu'on lit sans calculer » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Somme = trace, produit = déterminant ; en dimension 2, $\lambda^2 - (\operatorname{tr})\lambda + \det = 0$.

</details>
<details><summary>Indice 3</summary>

4 : $\lambda^2 + 4 = 0$. 5 : « Puissances, inverse, décalage ».

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M12c.R1 — Le rang et le noyau (M12a)

<details><summary>Indice 1</summary>

Relis M12a §6 (rang, noyau, théorème du rang).

</details>
<details><summary>Indice 2</summary>

La ligne 2 est le double de la ligne 1 : le rang est au plus 2.

</details>
<details><summary>Indice 3</summary>

Résous les deux équations des lignes 1 et 3 en fonction de $x_3$.

</details>

### M12c.R2 — Bases orthonormées et matrices orthogonales (M12b)

<details><summary>Indice 1</summary>

Relis M12b §2 (matrices orthogonales).

</details>
<details><summary>Indice 2</summary>

$8^2 + 15^2 = 17^2$ ; les coordonnées dans une base orthonormée sont des produits scalaires : $\mathbf{U}^\top\mathbf{x}$.

</details>
<details><summary>Indice 3</summary>

Une matrice orthogonale conserve les normes ; son déterminant vaut $\pm 1$.

</details>

### M12c.R3 — La matrice de covariance empirique (M02c)

<details><summary>Indice 1</summary>

Relis M02c (covariance empirique) et le §8 de la fiche.

</details>
<details><summary>Indice 2</summary>

Centre d'abord : retire le point moyen de chaque exemple.

</details>
<details><summary>Indice 3</summary>

Les sommes valent $\sum x^2 = 10$ et $\sum y^2 = 14$ après centrage ; divise par $n$ ou par $n - 1$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M12c.1 — Déterminants 2 × 2 et 3 × 3 : aire, volume et signe

<details><summary>Indice 1</summary>

Relis « Ce que mesure un déterminant » et « Calculer : cofacteurs ou élimination » (fiche §1).

</details>
<details><summary>Indice 2</summary>

c) L'application multiplie toutes les aires par $|\det\mathbf{M}|$. g) $\det(c\mathbf{N}) = c^n\det\mathbf{N}$.

</details>
<details><summary>Indice 3</summary>

h) Développe selon la dernière colonne : le déterminant est une fonction affine de $t$.

</details>

### Ex M12c.2 — Le déterminant d'une matrice 4 × 4 par élimination

<details><summary>Indice 1</summary>

Relis « Calculer : cofacteurs ou élimination » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Après l'échange, $L_3 \leftarrow L_3 - 2L_1$ et $L_4 \leftarrow L_4 + L_1$ ; puis le pivot 2 de la deuxième colonne.

</details>
<details><summary>Indice 3</summary>

Le déterminant est $-1$ (un échange) fois le produit de la diagonale. d) $\det(\mathbf{F}^{-1}) = 1/\det\mathbf{F}$ ; e) $\det\mathbf{F}^\top = \det\mathbf{F}$.

</details>

### Ex M12c.3 — Les valeurs et vecteurs propres d'une matrice 2 × 2

<details><summary>Indice 1</summary>

Relis « Le polynôme caractéristique » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\lambda^2 - 3\lambda - 28 = 0$.

</details>
<details><summary>Indice 3</summary>

d) Pour $\lambda = 7$ : $-2x + 6y = 0$. f) et g) : « Puissances, inverse, décalage ».

</details>

### Ex M12c.4 — Une matrice 3 × 3 triangulaire, puis une avec une valeur propre double

<details><summary>Indice 1</summary>

Relis « Ce qu'on lit sans calculer » (fiche §3) et « Quand est-ce possible ? » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Pour $\mathbf{T}$, triangulaire, lis la diagonale, puis résous $(\mathbf{T} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$ en remontant. Pour $\mathbf{K}$, développe $\det(\mathbf{K} - \lambda\mathbf{I})$ selon la dernière ligne.

</details>
<details><summary>Indice 3</summary>

f) $\mathbf{K} - 3\mathbf{I} = \begin{pmatrix} 3 & -3 & 3 \\ 1 & -1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$ : son rang ?

</details>

### Ex M12c.5 — Diagonaliser, puis calculer une puissance dixième

<details><summary>Indice 1</summary>

Relis « Changer de base pour rendre la matrice diagonale » et « Les puissances » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$\lambda^2 - 3\lambda + 2 = 0$ ; $\mathbf{P} = \begin{pmatrix} 4 & 3 \\ 1 & 1 \end{pmatrix}$ a pour déterminant 1.

</details>
<details><summary>Indice 3</summary>

e) $\mathbf{A}^{10} = \mathbf{P}\begin{pmatrix} 2^{10} & 0 \\ 0 & 1 \end{pmatrix}\mathbf{P}^{-1}$, avec $2^{10} = 1024$.

</details>

### Ex M12c.6 — Une matrice non diagonalisable, et une rotation sans valeur propre réelle

<details><summary>Indice 1</summary>

Relis « Multiplicités, et des valeurs propres complexes » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\operatorname{tr}\mathbf{N} = 4$ et $\det\mathbf{N} = 4$ : une racine double. Pour $\mathbf{R}$, $\cos 60° = \frac{1}{2}$.

</details>
<details><summary>Indice 3</summary>

b) Le rang de $\mathbf{N} - 2\mathbf{I} = \begin{pmatrix} 3 & -9 \\ 1 & -3 \end{pmatrix}$. h) Six fois 60°.

</details>

### Ex M12c.7 — Le théorème spectral sur une matrice symétrique 2 × 2 : Q, Λ et QΛQᵀ

<details><summary>Indice 1</summary>

Relis « Le théorème spectral » et son exemple (fiche §6).

</details>
<details><summary>Indice 2</summary>

$\lambda^2 - 31\lambda + 30 = 0$. Un vecteur propre de 30 : $(\mathbf{S} - 30\mathbf{I})\mathbf{v} = \mathbf{0}$.

</details>
<details><summary>Indice 3</summary>

Les directions $(2, 5)$ et $(5, -2)$, de norme $\sqrt{29}$. e) $\lambda_1\mathbf{q}_1\mathbf{q}_1^\top = \frac{30}{29}\begin{pmatrix} 4 & 10 \\ 10 & 25 \end{pmatrix}$.

</details>

### Ex M12c.8 — Le quotient de Rayleigh : le maximum et le minimum de xᵀAx sur le cercle unité

<details><summary>Indice 1</summary>

Relis « Le quotient de Rayleigh » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Le maximum de $\mathbf{x}^\top\mathbf{S}\mathbf{x}$ sur les vecteurs unitaires est la plus grande valeur propre, atteinte sur son vecteur propre.

</details>
<details><summary>Indice 3</summary>

$\lambda^2 - 19\lambda + 18 = 0$ ; pour 18, $-x + 4y = 0$. h) $(8, 15)$ : $17 \times 64 + 2 \times 4 \times 120 + 2 \times 225$, divisé par $17^2$.

</details>

### Ex M12c.9 — Trois itérations de la méthode de la puissance à la main

<details><summary>Indice 1</summary>

Relis « Multiplier, normaliser, recommencer » et « Ce qu'il faut savoir » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Calcule les produits sur les vecteurs non normalisés : $(1, 1) \to (5, -3) \to (1, 33) \to \ldots$, en changeant le signe si besoin.

</details>
<details><summary>Indice 3</summary>

e) Le quotient de Rayleigh de $(-101, 195)$ : $\frac{\mathbf{x}^\top\mathbf{A}\mathbf{x}}{\mathbf{x}^\top\mathbf{x}}$. f) $\lambda^2 + 4\lambda - 21 = 0$.

</details>

### Ex M12c.10 — Définie positive ? Par les valeurs propres, les mineurs et la forme quadratique ; une hessienne qui prouve la convexité

<details><summary>Indice 1</summary>

Relis « Les critères » et « La hessienne et la convexité » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Les mineurs principaux : les déterminants des sous-matrices en haut à gauche. La hessienne de $f$ : $f_{xx} = 2 + e^x$.

</details>
<details><summary>Indice 3</summary>

La hessienne en $(x, y)$ est $\begin{pmatrix} 2 + e^x & 2 \\ 2 & 6 \end{pmatrix}$ ; son déterminant vaut $8 + 6e^x$.

</details>

### Ex M12c.11 — La décomposition de Cholesky d'une matrice 3 × 3

<details><summary>Indice 1</summary>

Relis « La décomposition de Cholesky » et son exemple (fiche §7).

</details>
<details><summary>Indice 2</summary>

Colonne 1 : $l_{11} = \sqrt{a_{11}}$, puis $l_{i1} = a_{i1}/l_{11}$ ; colonne 2 : $l_{22} = \sqrt{a_{22} - l_{21}^2}$.

</details>
<details><summary>Indice 3</summary>

h) $\mathbf{L}\mathbf{z} = \mathbf{b}$ en descendant, puis $\mathbf{L}^\top\mathbf{x} = \mathbf{z}$ en remontant.

</details>

### Ex M12c.12 — Une forme quadratique réduite à une somme de carrés, et ses lignes de niveau

<details><summary>Indice 1</summary>

Relis « Les formes quadratiques » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Le terme croisé $10xy$ donne 5 de part et d'autre de la diagonale. $\lambda^2 - 28\lambda + 27 = 0$.

</details>
<details><summary>Indice 3</summary>

e) Avec $q = 27y_1^2 + y_2^2$, la ligne $q = 27$ coupe l'axe $\mathbf{q}_i$ en $\pm\sqrt{27/\lambda_i}$. g) La matrice de $2x^2 + c\,xy + 26y^2$ a $c/2$ hors de la diagonale.

</details>

### Ex M12c.13 — La covariance d'un vecteur transformé, AΣAᵀ, et le blanchiment d'une covariance 2 × 2

<details><summary>Indice 1</summary>

Relis « La covariance d'une transformation affine », « La racine carrée d'une matrice » et « Le blanchiment » (fiche §8).

</details>
<details><summary>Indice 2</summary>

b) $\mathbf{A} = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}$. e) $\lambda^2 - 97\lambda + 1296 = 0$, et $1296 = 81 \times 16$.

</details>
<details><summary>Indice 3</summary>

Les vecteurs propres sont $(2, -3)$ pour 81 et $(3, 2)$ pour 16, de norme $\sqrt{13}$ ; $\boldsymbol{\Sigma}^{1/2} = \frac{9}{13}\begin{pmatrix} 4 & -6 \\ -6 & 9 \end{pmatrix} + \frac{4}{13}\begin{pmatrix} 9 & 6 \\ 6 & 4 \end{pmatrix}$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M12c.14 — det A ≠ 0 si et seulement si A est inversible (det AB = det A det B admis)

<details><summary>Indice 1</summary>

Relis « Le déterminant et l'inversibilité » (fiche §1).

</details>
<details><summary>Indice 2</summary>

1. $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$. 2. Chaque opération sur les lignes multiplie le déterminant par un nombre non nul.

</details>
<details><summary>Indice 3</summary>

2. Une forme échelonnée carrée sans pivot dans une colonne a une diagonale qui contient un 0 : produit nul.

</details>

### Ex M12c.15 — Une matrice symétrique réelle : valeurs propres réelles, vecteurs propres de valeurs distinctes orthogonaux

<details><summary>Indice 1</summary>

Relis « Le théorème spectral » (fiche §6).

</details>
<details><summary>Indice 2</summary>

1. $(\mathbf{A}\mathbf{u}) \cdot \mathbf{v} = \mathbf{u}^\top\mathbf{A}^\top\mathbf{v}$. 2. $\lambda\,\mathbf{u} \cdot \mathbf{v} = \mu\,\mathbf{u} \cdot \mathbf{v}$.

</details>
<details><summary>Indice 3</summary>

3. Le conjugué de $\bar{\mathbf{z}}^\top\mathbf{A}\mathbf{z}$ est $\mathbf{z}^\top\mathbf{A}\bar{\mathbf{z}}$, un nombre, égal à sa transposée.

</details>

### Ex M12c.16 — La somme des valeurs propres est la trace, leur produit le déterminant

<details><summary>Indice 1</summary>

Relis « Ce qu'on lit sans calculer » (fiche §3).

</details>
<details><summary>Indice 2</summary>

1. Développe $(a - \lambda)(d - \lambda) - bc$. 2. Remplace $\lambda$ par 0 des deux côtés.

</details>
<details><summary>Indice 3</summary>

3. $\operatorname{tr}(\mathbf{P}\mathbf{D}\mathbf{P}^{-1}) = \operatorname{tr}(\mathbf{D}\mathbf{P}^{-1}\mathbf{P})$. 4. Deux nombres de somme 5 et de produit 6.

</details>

### Ex M12c.17 — Une matrice de covariance, et toute matrice de Gram XᵀX, est symétrique semi-définie positive

<details><summary>Indice 1</summary>

Relis « La matrice de covariance, une matrice symétrique positive » (fiche §8).

</details>
<details><summary>Indice 2</summary>

1. $\mathbf{w}^\top\mathbf{X}^\top\mathbf{X}\mathbf{w} = (\mathbf{X}\mathbf{w})^\top(\mathbf{X}\mathbf{w})$. 2. $\lVert \mathbf{X}\mathbf{w} \rVert = 0$ seulement si $\mathbf{X}\mathbf{w} = \mathbf{0}$.

</details>
<details><summary>Indice 3</summary>

5. Une colonne somme de deux autres, ou $p > n$ : le rang de $\mathbf{X}_c$ est inférieur à $p$.

</details>

### Ex M12c.18 — Le quotient de Rayleigh d'une matrice symétrique est entre λ_min et λ_max

<details><summary>Indice 1</summary>

Relis « Le quotient de Rayleigh » et son exemple (fiche §6).

</details>
<details><summary>Indice 2</summary>

1. $\mathbf{Q}$ est orthogonale : elle conserve les normes. 2. Encadre chaque $\lambda_i$ par $\lambda_n$ et $\lambda_1$.

</details>
<details><summary>Indice 3</summary>

3. L'égalité force $y_i = 0$ pour tout $\lambda_i < \lambda_1$. 4. Orthogonal à $\mathbf{q}_1$ veut dire $y_1 = 0$.

</details>

### Ex M12c.19 — ½ xᵀAx − bᵀx, avec A définie positive, a un unique minimum, en A⁻¹b

<details><summary>Indice 1</summary>

Relis « Le minimum d'une quadratique » (fiche §7).

</details>
<details><summary>Indice 2</summary>

1. Développe $\frac{1}{2}(\mathbf{x}^* + \mathbf{h})^\top\mathbf{A}(\mathbf{x}^* + \mathbf{h})$ ; les termes en $\mathbf{h}$ du premier ordre se simplifient grâce à $\mathbf{A}\mathbf{x}^* = \mathbf{b}$.

</details>
<details><summary>Indice 3</summary>

2. $\frac{1}{2}\mathbf{h}^\top\mathbf{A}\mathbf{h} > 0$ si $\mathbf{h} \ne \mathbf{0}$. 4. Développe $\lVert \mathbf{X}\mathbf{w} - \mathbf{y} \rVert^2$.

</details>

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12c.20 — Pont : la variance d'une somme pondérée de trois features, wᵀΣw, et pourquoi Σ doit être semi-définie positive

<details><summary>Indice 1</summary>

Relis « La covariance d'une transformation affine » (fiche §8).

</details>
<details><summary>Indice 2</summary>

$\mathbb{V}(\mathbf{w}^\top\mathbf{x}) = \mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ ; une covariance : $\operatorname{Cov}(\mathbf{a}^\top\mathbf{x}, \mathbf{b}^\top\mathbf{x}) = \mathbf{a}^\top\boldsymbol{\Sigma}\mathbf{b}$.

</details>
<details><summary>Indice 3</summary>

b) $\mathbf{w} = (1, 1, 1)$. f) $\mathbf{w} = (1, -1, 0)$ avec $\boldsymbol{\Phi}$. h) Covariance divisée par le produit des écarts-types.

</details>

### Ex M12c.21 — Pont : après un blanchiment, la covariance est l'identité

<details><summary>Indice 1</summary>

Relis « Le blanchiment » (fiche §8).

</details>
<details><summary>Indice 2</summary>

$l_{11} = 3$, $l_{21} = 6/3$, $l_{22} = \sqrt{8 - l_{21}^2}$. L'inverse d'une matrice triangulaire inférieure $2 \times 2$ se fait à la main.

</details>
<details><summary>Indice 3</summary>

f) $\operatorname{Cov}(\mathbf{R}\mathbf{z}) = \mathbf{R}\operatorname{Cov}(\mathbf{z})\mathbf{R}^\top$. h) $\lVert \mathbf{W}\mathbf{d} \rVert^2 = \mathbf{d}^\top\mathbf{W}^\top\mathbf{W}\mathbf{d}$.

</details>

### Ex M12c.22 — MML §4.1 et §4.2 : déterminant, trace, valeurs propres, en anglais

<details><summary>Indice 1</summary>

Lis MML §4.1, puis §4.2, crayon en main.

</details>
<details><summary>Indice 2</summary>

Cherche les mots *Laplace expansion*, *trace*, *eigenspace*, *algebraic multiplicity*, *geometric multiplicity*, *defective*.

</details>
<details><summary>Indice 3</summary>

Pour la question 6, cherche le théorème sur $\mathbf{A}^\top\mathbf{A}$ et sa démonstration.

</details>

### Ex M12c.23 — MML §4.3 et §4.4 : Cholesky, diagonalisation et décomposition spectrale

<details><summary>Indice 1</summary>

Lis MML §4.3, puis §4.4.

</details>
<details><summary>Indice 2</summary>

Cherche les mots *Cholesky factor*, *diagonalizable*, *similar*, *eigendecomposition*.

</details>
<details><summary>Indice 3</summary>

Pour la question 3 : $\det\mathbf{A} = (\det\mathbf{L})^2$, et $\mathbf{L}$ est triangulaire.

</details>

### Ex M12c.24 — Fermi : un déterminant 20 × 20 par cofacteurs ou par élimination, combien d'opérations ?

<details><summary>Indice 1</summary>

Relis « Calculer : cofacteurs ou élimination » (fiche §1).

</details>
<details><summary>Indice 2</summary>

$20! = 20 \times 19 \times \cdots \times 1$ : regroupe par dizaines, ou utilise $n! \approx \sqrt{2\pi n}\,(n/e)^n$.

</details>
<details><summary>Indice 3</summary>

$20! \approx 2{,}4 \times 10^{18}$ ; une année dure environ $3{,}2 \times 10^7$ secondes.

</details>

### Ex M12c.25 — Expliquer un vecteur propre avec une image

<details><summary>Indice 1</summary>

Relis « Les directions qu'une matrice ne fait pas tourner » (fiche §3) et la figure.

</details>
<details><summary>Indice 2</summary>

Une image : on étire une feuille de caoutchouc ; la plupart des traits changent de direction, quelques-uns non.

</details>
<details><summary>Indice 3</summary>

N'oublie ni le retournement (valeur propre négative), ni la rotation (aucune direction propre).

</details>

<a id="entretien"></a>

## 💼 Entretien

### M12c.E1 — « Que représentent les valeurs propres d'une matrice de covariance ? »

<details><summary>Indice 1</summary>

Relis les §6 et §8 de la fiche.

</details>
<details><summary>Indice 2</summary>

Vecteurs propres : des directions orthogonales ; valeurs propres : les variances dans ces directions.

</details>
<details><summary>Indice 3</summary>

Somme = variance totale (la trace) ; une valeur propre nulle : une combinaison de features constante.

</details>

### M12c.E2 — « Comment savoir qu'une matrice est définie positive, et pourquoi est-ce important en optimisation ? »

<details><summary>Indice 1</summary>

Relis le §7 de la fiche.

</details>
<details><summary>Indice 2</summary>

Définition par $\mathbf{x}^\top\mathbf{A}\mathbf{x} > 0$ ; critères : valeurs propres, mineurs, Cholesky.

</details>
<details><summary>Indice 3</summary>

Hessienne définie positive : fonction strictement convexe, un minimum unique.

</details>

<a id="notebook"></a>

## Notebook

### Ex M12c.26 — Le déterminant par élimination · `det`

<details><summary>Indice 1</summary>

Relis « Calculer : cofacteurs ou élimination » et « Le pivot partiel » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Pour la colonne $k$ : `p = k + np.argmax(np.abs(M[k:, k]))` ; si `M[p, k] == 0`, rends `0.0` ; sinon échange les lignes `k` et `p` (et change le signe si `p != k`).

</details>
<details><summary>Indice 3</summary>

Puis, pour chaque ligne `i > k` : `M[i, k:] -= (M[i, k] / M[k, k]) * M[k, k:]`. À la fin : `float(sign * np.prod(np.diag(M)))`.

</details>

### Ex M12c.27 — La méthode de la puissance et le quotient de Rayleigh · `power_iteration, rayleigh_quotient`

<details><summary>Indice 1</summary>

Relis « Multiplier, normaliser, recommencer » et « Ce qu'il faut savoir » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Une petite fonction `fix_sign(v)` : `-v if v[np.argmax(np.abs(v))] < 0 else v`, appliquée à $\mathbf{x}_0$ normalisé et à chaque nouvel itéré.

</details>
<details><summary>Indice 3</summary>

Compte un produit par tour de boucle ; arrête-toi **après** avoir remplacé $\mathbf{x}$ par le nouvel itéré ; rends `float(x @ A @ x)`.

</details>

### Ex M12c.28 — La décomposition de Cholesky et le test « définie positive » · `cholesky, is_positive_definite`

<details><summary>Indice 1</summary>

Relis « La décomposition de Cholesky » (fiche §7).

</details>
<details><summary>Indice 2</summary>

La symétrie relative : `np.any(np.abs(M - M.T) > 1e-12 * max(1, np.max(np.abs(M))))`. Puis `L = np.zeros((n, n))`.

</details>
<details><summary>Indice 3</summary>

Colonne `j` : `pivot = M[j, j] - L[j, :j] @ L[j, :j]` ; `if not pivot > 0: raise ValueError(...)` ; `L[j + 1:, j] = (M[j + 1:, j] - L[j + 1:, :j] @ L[j, :j]) / L[j, j]`.

</details>

### Ex M12c.29 — La racine carrée d'une matrice symétrique positive et la matrice de blanchiment · `sqrtm_psd, whitening_matrix`

<details><summary>Indice 1</summary>

Relis « La racine carrée d'une matrice » et « Le blanchiment » (fiche §8).

</details>
<details><summary>Indice 2</summary>

`values, Q = np.linalg.eigh(M)` ; `Q * np.sqrt(values)` multiplie chaque colonne de `Q` par une racine.

</details>
<details><summary>Indice 3</summary>

`sqrtm_psd` : `np.clip(values, 0, None)` après le contrôle des valeurs négatives. `whitening_matrix` : `(Q / np.sqrt(values)) @ Q.T`, ou `np.linalg.solve(L, np.eye(p))`.

</details>

### Ex M12c.30 — `np.linalg.eigh`, `det`, `cholesky` et `scipy.linalg.sqrtm` contre tes fonctions

<details><summary>Indice 1</summary>

Relis l'énoncé (« En pratique ») et le 💻 du §3.

</details>
<details><summary>Indice 2</summary>

`values, vectors = np.linalg.eigh(S_30)` ; l'orthonormalité : `vectors.T @ vectors` contre `np.eye(4)`.

</details>
<details><summary>Indice 3</summary>

g) `np.linalg.eig(np.array([[0.0, -1.0], [1.0, 0.0]]))[0].dtype`.

</details>

### Ex M12c.31 — Prédire : la méthode de la puissance quand les deux plus grandes valeurs propres sont proches

<details><summary>Indice 1</summary>

Relis « Ce qu'il faut savoir » (fiche §5).

</details>
<details><summary>Indice 2</summary>

L'écart du vecteur est multiplié par $|\lambda_2/\lambda_1|$ à chaque pas : $0{,}5^k$ et $0{,}99^k$.

</details>
<details><summary>Indice 3</summary>

La valeur propre (quotient de Rayleigh d'une matrice symétrique) a une erreur de l'ordre du **carré** de celle du vecteur.

</details>

### Ex M12c.32 — La vitesse de la méthode de la puissance et le rapport |λ₂ / λ₁|

<details><summary>Indice 1</summary>

Relis M12c.31 et « Ce qu'il faut savoir » (fiche §5).

</details>
<details><summary>Indice 2</summary>

$r^k = 10^{-12}$ donne $k = 12/(-\log_{10} r)$ : le nombre d'itérations attendu pour chaque $r$.

</details>
<details><summary>Indice 3</summary>

Une liste en compréhension : `[mymath.eigen.power_iteration(ratio_matrix(r), x0=np.ones(3), n_iter=10_000)[2] for r in RATIOS_32]`.

</details>

### Ex M12c.33 — Les lignes de niveau de xᵀAx : définie positive, semi-définie positive, indéfinie

<details><summary>Indice 1</summary>

Relis « Les formes quadratiques » (fiche §7) et la figure.

</details>
<details><summary>Indice 2</summary>

`classify` : `values = np.linalg.eigvalsh(A)`, puis compare chaque valeur à $\pm 10^{-12}\max|\lambda|$.

</details>
<details><summary>Indice 3</summary>

`draw_levels` : `X, Y = np.meshgrid(grid, grid)`, `Q = A[0, 0] * X**2 + 2 * A[0, 1] * X * Y + A[1, 1] * Y**2`, puis `ax.contour(X, Y, Q, levels=...)`.

</details>

### Ex M12c.34 — Chasse à l'erreur : det(A + B) = det A + det B, un vecteur propre nul, Cholesky d'une matrice non symétrique

<details><summary>Indice 1</summary>

Relis les ⚠️ des §1, §3 et §7, et le 💻 du §7.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, calcule à la main ce que dit son commentaire, puis ce que fait le code.

</details>
<details><summary>Indice 3</summary>

(A) Le déterminant est-il additif ? (C) Que rend `solve` pour un second membre nul ? (E) Que lit `np.linalg.cholesky` ?

</details>

### Ex M12c.35 — Vérifier avec SymPy : polynôme caractéristique, valeurs propres exactes, diagonalisation

<details><summary>Indice 1</summary>

Relis R0 (SymPy) et l'énoncé.

</details>
<details><summary>Indice 2</summary>

`(M35_DIAG - lam * sympy.eye(3)).det()`, puis `sympy.factor` pour le lire.

</details>
<details><summary>Indice 3</summary>

`P_35, D_35 = M35_DIAG.diagonalize()` ; `diagonalizable_35 = M35_DEFECTIVE.is_diagonalizable()`.

</details>

### Ex M12c.36 — Défi : les trois plus grandes valeurs propres d'une matrice symétrique semi-définie positive 300 × 300, par la puissance avec déflation, à 1e−6 près

<details><summary>Indice 1</summary>

Relis « La déflation » (fiche §6) et M12c.32.

</details>
<details><summary>Indice 2</summary>

Pars d'un vecteur tiré au hasard ; après chaque valeur propre trouvée, `A = A - value * np.outer(vector, vector)`.

</details>
<details><summary>Indice 3</summary>

Les rapports successifs sont proches de 0,8 : une centaine d'itérations par étape, la valeur par défaut `n_iter=1000` suffit.

</details>
