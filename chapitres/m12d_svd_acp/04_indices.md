# M12d · SVD et analyse en composantes principales — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M12d.Q1 — La SVD : formes et propriétés

<details><summary>Indice 1</summary>

Relis le théorème et la SVD compacte (fiche §1).

</details>
<details><summary>Indice 2</summary>

Complète : $\mathbf{U}$ est $(m, m)$, $\mathbf{V}$ est $(n, n)$, $\mathbf{S}$ a la forme de $\mathbf{A}$ ; en compacte, on ne garde que les $r$ premières colonnes.

</details>
<details><summary>Indice 3</summary>

5 : une valeur singulière est toujours positive ; le signe passe dans $\mathbf{u}_i$. 6 : les $\mathbf{v}_i$ sont les **lignes** de `Vt`.

</details>

### M12d.Q2 — Valeurs singulières et valeurs propres

<details><summary>Indice 1</summary>

Relis « La calculer : passer par $\mathbf{A}^\top\mathbf{A}$ » et « Ce que la SVD dit d'une matrice » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Une valeur singulière est la **racine** d'une valeur propre de $\mathbf{A}^\top\mathbf{A}$.

</details>
<details><summary>Indice 3</summary>

5 : pense au cisaillement de la fiche §2, ⚠️.

</details>

### M12d.Q3 — Rang faible : ce qu'on garde, ce qu'on perd

<details><summary>Indice 1</summary>

Relis Eckart-Young et « Compresser » (fiche §3).

</details>
<details><summary>Indice 2</summary>

L'erreur au carré est la somme des $s_i^2$ oubliés ; l'énergie totale est la somme de tous les $s_i^2$.

</details>
<details><summary>Indice 3</summary>

$144 + 81 + 16 + 4 + 1 = 246$ ; stocker $\mathbf{A}_2$ coûte $2(m + n + 1)$ nombres.

</details>

### M12d.Q4 — Pseudo-inverse et conditionnement

<details><summary>Indice 1</summary>

Relis la définition de $\mathbf{A}^+$ et celle du conditionnement (fiche §4).

</details>
<details><summary>Indice 2</summary>

On inverse les valeurs singulières non nulles et l'on transpose les rôles : $\mathbf{A}^+$ a la forme de $\mathbf{A}^\top$.

</details>
<details><summary>Indice 3</summary>

4 : une valeur singulière nulle rend $\kappa$ infini. 6 : on perd environ $\log_{10}\kappa$ chiffres, et $\kappa(\mathbf{A}^\top\mathbf{A}) = \kappa^2$.

</details>

### M12d.Q5 — Ce que maximise un axe principal

<details><summary>Indice 1</summary>

Relis « La variance le long d'une direction » et « Le maximum sur la sphère » (fiche §5).

</details>
<details><summary>Indice 2</summary>

C'est un quotient de Rayleigh : son maximum est la plus grande valeur propre de $\mathbf{C}$.

</details>
<details><summary>Indice 3</summary>

3 : une covariance non nulle hors de la diagonale fait tourner le premier axe. 4 : une matrice diagonale a pour vecteurs propres les $\mathbf{e}_j$.

</details>

### M12d.Q6 — Centrer et standardiser avant une ACP ?

<details><summary>Indice 1</summary>

Relis « Centrer, et parfois standardiser » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Sans centrer, on mesure la dispersion autour de l'origine ; avec des unités différentes, l'unité décide de la variance.

</details>
<details><summary>Indice 3</summary>

5 : M12d.19. 6 : avec $k = p$, la base des axes est complète.

</details>

### M12d.Q7 — Variance expliquée et nombre de composantes

<details><summary>Indice 1</summary>

Relis « La part de variance expliquée » et « L'erreur de reconstruction » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Les parts : $5/10$, $4/10$, $1/10$ ; l'erreur moyenne : $\frac{n-1}{n}$ fois la somme des variances oubliées.

</details>
<details><summary>Indice 3</summary>

4 : les $n$ lignes centrées ont une somme nulle. 6 : le ⚠️ de la fin du §7.

</details>

### M12d.Q8 — ACP, t-SNE ou UMAP : qui garde quoi ?

<details><summary>Indice 1</summary>

Relis le §8 de la fiche, en particulier « Lire une carte avec prudence ».

</details>
<details><summary>Indice 2</summary>

L'ACP projette (elle garde les grandes distances) ; t-SNE et UMAP gardent les voisinages.

</details>
<details><summary>Indice 3</summary>

3 : la perplexité est un nombre effectif de voisins. 5 : la queue lourde laisse de la place en 2D.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M12d.R1 — Valeurs propres et théorème spectral (M12c)

<details><summary>Indice 1</summary>

Relis M12c §3 et §6.

</details>
<details><summary>Indice 2</summary>

Trace 20, déterminant $-69$ : $\lambda^2 - 20\lambda - 69 = 0$.

</details>
<details><summary>Indice 3</summary>

Pour 23 : $-25x + 5y = 0$. Pour une matrice symétrique, $s_i = \lvert\lambda_i\rvert$ (fiche §1).

</details>

### M12d.R2 — La projection orthogonale (M12b)

<details><summary>Indice 1</summary>

Relis M12b §2 et §5.

</details>
<details><summary>Indice 2</summary>

$1 + 16 + 64 = 81$ ; $t = \mathbf{u} \cdot \mathbf{x}$.

</details>
<details><summary>Indice 3</summary>

$t = 9$, $\mathbf{p} = (1, 4, 8)$, $\mathbf{r} = (4, -1, 0)$. $\mathbf{P}^2 = \mathbf{u}(\mathbf{u}^\top\mathbf{u})\mathbf{u}^\top$.

</details>

### M12d.R3 — Moyenne, covariance et standardisation (M02c)

<details><summary>Indice 1</summary>

Relis M02c (moyenne, covariance, standardisation).

</details>
<details><summary>Indice 2</summary>

Le point moyen est $(5, 45)$ ; centre, puis divise les sommes de produits par $n - 1 = 3$.

</details>
<details><summary>Indice 3</summary>

La corrélation est $\frac{80}{\sqrt{20 \times 500}}$ ; standardiser divise chaque feature centrée par son écart-type.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M12d.1 — La SVD d'une matrice 2 × 2 à la main, par AᵀA

<details><summary>Indice 1</summary>

Relis la recette « La calculer : passer par $\mathbf{A}^\top\mathbf{A}$ » (fiche §1) et son exemple.

</details>
<details><summary>Indice 2</summary>

$\mathbf{A}^\top\mathbf{A}$ a pour trace 157 et pour déterminant $72 \times 85 - 42^2$.

</details>
<details><summary>Indice 3</summary>

Pour 121 : $(\mathbf{A}^\top\mathbf{A} - 121\,\mathbf{I})\mathbf{v} = \mathbf{0}$ donne $-49x + 42y = 0$ ; puis $\mathbf{u}_1 = \mathbf{A}\mathbf{v}_1/11$.

</details>

### Ex M12d.2 — La SVD compacte d'une matrice 3 × 2 de rang 1

<details><summary>Indice 1</summary>

Relis l'exemple rectangulaire et « Ce que la SVD dit d'une matrice » (fiche §1).

</details>
<details><summary>Indice 2</summary>

La deuxième colonne est $-5$ fois la première : $\mathbf{A} = \mathbf{a}\mathbf{b}^\top$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{a} = (2, 6, 9)$, $\mathbf{b} = (1, -5)$ : $\mathbf{v}_1$ est $\pm\mathbf{b}/\lVert \mathbf{b} \rVert$ (la convention choisit le signe), et le noyau est orthogonal à $\mathbf{b}$.

</details>

### Ex M12d.3 — Le cercle unité devient une ellipse : axes et demi-axes

<details><summary>Indice 1</summary>

Relis « L'image de la sphère unité » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Les demi-axes sont $s_1\mathbf{u}_1$ et $s_2\mathbf{u}_2$ ; le point de départ du grand axe est $\mathbf{v}_1$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{B}^\top\mathbf{B}$ a pour trace 97 et pour déterminant 1 296 ; pour 81, $-64x - 8y = 0$.

</details>

### Ex M12d.4 — L'approximation de rang 1 d'une matrice 3 × 3 et son erreur

<details><summary>Indice 1</summary>

Relis la fiche §1 (exemple rectangulaire) et Eckart-Young (fiche §3).

</details>
<details><summary>Indice 2</summary>

La troisième colonne est orthogonale aux deux autres : $\mathbf{A}^\top\mathbf{A}$ est par blocs, et le bloc $2 \times 2$ a pour trace 57 et déterminant 392.

</details>
<details><summary>Indice 3</summary>

Pour 49 : $-16x + 20y = 0$. $\mathbf{A}_1 = \mathbf{A}\mathbf{v}_1\mathbf{v}_1^\top$ ; l'erreur au carré est $8 + 2$.

</details>

### Ex M12d.5 — Compter les nombres stockés : une image en rang k

<details><summary>Indice 1</summary>

Relis « Compresser » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Le rang $k$ coûte $k(m + n + 1)$ nombres.

</details>
<details><summary>Indice 3</summary>

d) $k < \frac{mn}{m + n + 1}$ ; e) $k(m + n + 1) \le 0{,}02\,mn$ ; g) une seule matrice de $900 \times 4\,800$.

</details>

### Ex M12d.6 — La pseudo-inverse d'une matrice non inversible et la solution de norme minimale

<details><summary>Indice 1</summary>

Relis « Résoudre quand on ne peut pas inverser » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Pour une matrice de rang 1, $\mathbf{A} = s_1\mathbf{u}_1\mathbf{v}_1^\top$ et $\mathbf{A}^+ = \frac{1}{s_1}\mathbf{v}_1\mathbf{u}_1^\top$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{A}^+ = \mathbf{A}^\top/s_1^2$ avec $s_1^2 = \lVert \mathbf{A} \rVert_F^2$. h) $\mathbf{A}\mathbf{A}^+$ projette sur la droite engendrée par $(2, 5)$.

</details>

### Ex M12d.7 — Le conditionnement de trois matrices, et l'erreur relative sur une solution

<details><summary>Indice 1</summary>

Relis « Le conditionnement » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$\mathbf{P}^\top\mathbf{P}$ est diagonale ; $\mathbf{Q}$ est orthogonale ; pour $\mathbf{R}$, $s_1^2 + s_2^2 = 102$ et $s_1s_2 = 1$.

</details>
<details><summary>Indice 3</summary>

c) $s_1^2$ est la plus grande racine de $x^2 - 102x + 1$, et $\kappa = s_1/s_2 = s_1^2$ puisque $s_1s_2 = 1$. f) $\mathbf{R}^{-1} = \begin{pmatrix} 2 & -3 \\ -5 & 8 \end{pmatrix}$.

</details>

### Ex M12d.8 — Les axes principaux d'un nuage de ℝ³ : covariance, polynôme caractéristique, variances et axes

<details><summary>Indice 1</summary>

Relis l'exemple du §5 de la fiche, sa structure par blocs.

</details>
<details><summary>Indice 2</summary>

Le point moyen est $(14, 9, 6)$ ; la deuxième mesure centrée est orthogonale aux deux autres.

</details>
<details><summary>Indice 3</summary>

Le bloc $\begin{pmatrix} 19 & 4 \\ 4 & 4 \end{pmatrix}$ a pour trace 23 et déterminant 60 ; pour 20, $-x + 4y = 0$.

</details>

### Ex M12d.9 — Scores, reconstruction et erreur de reconstruction moyenne avec deux composantes sur trois

<details><summary>Indice 1</summary>

Relis « Les trois étapes » (fiche §6) et « L'erreur de reconstruction » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$t_{7j} = \mathbf{u}_j^\top(\mathbf{x}_7 - \boldsymbol{\mu})$, avec $\mathbf{x}_7 - \boldsymbol{\mu} = (6, 1, 1)$ ; $\hat{\mathbf{x}}_7 = \boldsymbol{\mu} + t_{71}\mathbf{u}_1 + t_{72}\mathbf{u}_2$.

</details>
<details><summary>Indice 3</summary>

c) $\sqrt{17}\,t_{i1} = 4x_1 + x_3$ sur les objets centrés ; e) $\operatorname{Cov}(t_1, x_1) = \mathbf{u}_1^\top\mathbf{C}\,\mathbf{e}_1$ ; f) $\frac{n-1}{n}\lambda_3$ ; g) $\frac{n-1}{n}(\lambda_2 + \lambda_3)$.

</details>

### Ex M12d.10 — La variance expliquée cumulée : combien de composantes pour 95 % ?

<details><summary>Indice 1</summary>

Relis « La part de variance expliquée » et « Choisir $k$ » (fiche §7).

</details>
<details><summary>Indice 2</summary>

La somme vaut 20 : chaque part est $\lambda_j/20$.

</details>
<details><summary>Indice 3</summary>

Les parts cumulées : 0,48 ; 0,72 ; 0,84 ; 0,895 ; 0,93 ; 0,96… g) multiplie f) par $\frac{50}{51}$.

</details>

### Ex M12d.11 — L'ACP par la SVD de la matrice centrée : σ² / (n − 1) donne les variances

<details><summary>Indice 1</summary>

Relis « L'ACP par la SVD des données centrées » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Le point moyen est $(6, 4, 5)$ ; vérifie que chacun des trois vecteurs donnés est vecteur propre de $\mathbf{X}_c^\top\mathbf{X}_c$.

</details>
<details><summary>Indice 3</summary>

$s_j = \sqrt{\text{valeur propre}}$, $\lambda_j = s_j^2/3$, $\mathbf{u}_1 = \mathbf{X}_c\mathbf{v}_1/s_1$, scores $= \mathbf{X}_c\mathbf{v}_1$.

</details>

### Ex M12d.12 — L'ACP quand n < p : passer par la petite matrice XXᵀ

<details><summary>Indice 1</summary>

Relis « La grande dimension » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Le point moyen est $(5, 6, 3, 4, 7)$ ; $\mathbf{G}$ est $3 \times 3$, de lignes de somme nulle.

</details>
<details><summary>Indice 3</summary>

$\mathbf{G}(1, 0, -1) = 38\,(1, 0, -1)$ ; l'axe est $\mathbf{X}_c^\top\mathbf{w}$ normé, avec $\mathbf{w} = (1, 0, -1)$ ; les variances sont les valeurs propres non nulles divisées par $n - 1 = 2$.

</details>

### Ex M12d.13 — Les probabilités de voisinage de t-SNE sur quatre points, et leur perplexité 2^H

<details><summary>Indice 1</summary>

Relis « t-SNE en trois étapes » (fiche §8) et l'entropie de M06.

</details>
<details><summary>Indice 2</summary>

Avec ce $\sigma$, le poids d'un voisin à distance $d$ est $2^{-d^2}$ : $\frac{1}{2}$, $\frac{1}{4}$, $\frac{1}{8}$, à normaliser.

</details>
<details><summary>Indice 3</summary>

$P_1 = (\frac{4}{7}, \frac{2}{7}, \frac{1}{7})$ ; $H = -\sum p\log_2 p$ ; vu de $\mathbf{x}_2$, les carrés des distances sont 1, 1 et 2.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M12d.14 — Les valeurs singulières sont les racines des valeurs propres de AᵀA

<details><summary>Indice 1</summary>

Relis la fiche §1 et M12c §7 (une matrice de Gram).

</details>
<details><summary>Indice 2</summary>

2. $\mathbf{A}^\top\mathbf{A} = \mathbf{V}\mathbf{S}^\top\mathbf{U}^\top\mathbf{U}\mathbf{S}\mathbf{V}^\top$ ; 3. calcule $(\mathbf{A}\mathbf{v}_i) \cdot (\mathbf{A}\mathbf{v}_j) = \mathbf{v}_i^\top\mathbf{A}^\top\mathbf{A}\mathbf{v}_j$.

</details>
<details><summary>Indice 3</summary>

4. $\mathbf{A}\mathbf{A}^\top(\mathbf{A}\mathbf{v}) = \mathbf{A}(\mathbf{A}^\top\mathbf{A}\mathbf{v}) = \lambda\,\mathbf{A}\mathbf{v}$, et $\lVert \mathbf{A}\mathbf{v} \rVert^2 = \lambda\lVert \mathbf{v} \rVert^2 \ne 0$.

</details>

### Ex M12d.15 — La plus grande valeur singulière est le plus grand étirement : ‖A x‖ ≤ σ₁ ‖x‖

<details><summary>Indice 1</summary>

Relis « Le plus grand et le plus petit étirement » (fiche §2).

</details>
<details><summary>Indice 2</summary>

$\mathbf{A}\mathbf{x} = \sum_i c_is_i\mathbf{u}_i$, et les $\mathbf{u}_i$ sont orthonormés : Pythagore.

</details>
<details><summary>Indice 3</summary>

4. $\lVert \mathbf{A}\mathbf{B}\mathbf{x} \rVert \le \lVert \mathbf{A} \rVert_2\lVert \mathbf{B}\mathbf{x} \rVert \le \lVert \mathbf{A} \rVert_2\lVert \mathbf{B} \rVert_2\lVert \mathbf{x} \rVert$, puis le maximum sur $\mathbf{x}$.

</details>

### Ex M12d.16 — L'erreur de l'approximation de rang k vaut la somme des σ² oubliés (Frobenius)

<details><summary>Indice 1</summary>

Relis « La norme de Frobenius » et Eckart-Young (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\operatorname{tr}((\mathbf{Q}\mathbf{M})^\top\mathbf{Q}\mathbf{M}) = \operatorname{tr}(\mathbf{M}^\top\mathbf{Q}^\top\mathbf{Q}\mathbf{M})$ ; pour $\mathbf{M}\mathbf{Q}$, utilise $\lVert \mathbf{X} \rVert_F = \lVert \mathbf{X}^\top \rVert_F$.

</details>
<details><summary>Indice 3</summary>

3. $\mathbf{D}$ est $\mathbf{S}$ dont on a mis à zéro les $k$ premières valeurs. 5. $\operatorname{tr}(\mathbf{A}_k^\top(\mathbf{A} - \mathbf{A}_k)) = 0$.

</details>

### Ex M12d.17 — La pseudo-inverse donne la solution des moindres carrés de plus petite norme

<details><summary>Indice 1</summary>

Relis « Résoudre quand on ne peut pas inverser » (fiche §4) et M12b §2.

</details>
<details><summary>Indice 2</summary>

Une matrice orthogonale conserve les normes : $\lVert \mathbf{A}\mathbf{x} - \mathbf{b} \rVert = \lVert \mathbf{U}^\top(\mathbf{A}\mathbf{x} - \mathbf{b}) \rVert$.

</details>
<details><summary>Indice 3</summary>

2. $y_i = c_i/s_i$ pour $i \le r$, les autres libres ; 3. les mettre à zéro ; $\mathbf{S}^+$ a pour diagonale les $1/s_i$ (et des zéros), de forme $(n, m)$.

</details>

### Ex M12d.18 — L'erreur de reconstruction moyenne est la somme des variances oubliées

<details><summary>Indice 1</summary>

Relis « L'erreur de reconstruction » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Les $\mathbf{u}_j$ forment une base orthonormée : les coordonnées de $\mathbf{x}_i - \boldsymbol{\mu}$ sont les $t_{ij}$, et Pythagore donne les normes.

</details>
<details><summary>Indice 3</summary>

2. $\sum_i t_{ij}^2 = \mathbf{u}_j^\top\mathbf{X}_c^\top\mathbf{X}_c\mathbf{u}_j$. 5. les $\lambda_j$ oubliés sont alors les plus petits.

</details>

### Ex M12d.19 — Les scores de deux composantes principales sont décorrélés

<details><summary>Indice 1</summary>

Relis « Les scores ne sont pas corrélés » (fiche §6).

</details>
<details><summary>Indice 2</summary>

La moyenne des $\mathbf{x}_i - \boldsymbol{\mu}$ est nulle ; la covariance de deux colonnes centrées est leur produit scalaire divisé par $n - 1$.

</details>
<details><summary>Indice 3</summary>

3. $\mathbf{C}\mathbf{u}_l = \lambda_l\mathbf{u}_l$. 5. $\frac{1}{169}(5 \times (-12) \times 4 + 12 \times 5 \times 1)$.

</details>

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12d.20 — Pont : détecter une anomalie par son erreur de reconstruction

<details><summary>Indice 1</summary>

Relis « Détecter une anomalie » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Avec $k = 2$, l'erreur d'un objet est le carré de son score sur $\mathbf{u}_3 = \frac{1}{\sqrt{17}}(-1, 0, 4)$.

</details>
<details><summary>Indice 3</summary>

Centre d'abord : $\mathbf{r}_1 - \boldsymbol{\mu} = (4, 3, 1)$, $\mathbf{r}_2 - \boldsymbol{\mu} = (-1, 0, 3)$, $\mathbf{r}_3 - \boldsymbol{\mu} = (16, 0, 4)$.

</details>

### Ex M12d.21 — Pont : un changement d'unités diagonal D change Σ en DΣD, et les axes principaux avec ; la standardisation non

<details><summary>Indice 1</summary>

Relis « Les unités comptent » (fiche §6) et M12c §8.

</details>
<details><summary>Indice 2</summary>

$(\mathbf{D}\mathbf{C}\mathbf{D})_{ij} = d_id_jc_{ij}$, avec $\mathbf{D} = \operatorname{diag}(1, 1, 3)$.

</details>
<details><summary>Indice 3</summary>

Le nouveau bloc $\begin{pmatrix} 19 & 12 \\ 12 & 36 \end{pmatrix}$ a pour trace 55 et déterminant 540 ; la corrélation $\frac{c_{13}}{\sqrt{c_{11}c_{33}}}$ ; f) l'arccos du produit scalaire des deux axes unitaires, en degrés.

</details>

### Ex M12d.22 — MML §4.5 à §4.7 : SVD, approximation de rang faible, phylogénie des matrices

<details><summary>Indice 1</summary>

Lis les sections dans l'ordre ; garde la fiche ouverte au §1 (📐 Notations).

</details>
<details><summary>Indice 2</summary>

Pour la construction, cherche quelle matrice symétrique le livre diagonalise d'abord, puis comment il obtient l'autre famille de vecteurs.

</details>
<details><summary>Indice 3</summary>

Pour l'exemple des notes de films, relis-le avec la matrice de M12d.4 : une ligne par client, une colonne par produit.

</details>

### Ex M12d.23 — MML §10.1 à §10.6 : l'ACP du livre (la dérivation par Lagrange de §10.2 se survole : M13b la relit)

<details><summary>Indice 1</summary>

Lis §10.1 avec la fiche §5 ouverte, puis §10.3 avec le §7 ; survole la dérivation par Lagrange de §10.2.

</details>
<details><summary>Indice 2</summary>

Traduis chaque formule : le livre range les exemples en colonnes et divise par $N$.

</details>
<details><summary>Indice 3</summary>

Pour §10.5, compare avec M12d.12 ; pour §10.6, compare la liste d'étapes avec la fiche §6.

</details>

### Ex M12d.24 — Fermi : la mémoire et le temps d'une ACP sur un million de clients et 250 features

<details><summary>Indice 1</summary>

Relis « La grande dimension » (fiche §7) et le piège des équations normales (fiche §4).

</details>
<details><summary>Indice 2</summary>

$10^6 \times 250 \times 8$ octets ; $np^2 = 10^6 \times 62\,500$ opérations.

</details>
<details><summary>Indice 3</summary>

6 : accumule, morceau par morceau, $\sum\mathbf{x}_i$ puis $\sum(\mathbf{x}_i - \boldsymbol{\mu})(\mathbf{x}_i - \boldsymbol{\mu})^\top$ (deux lectures).

</details>

### Ex M12d.25 — Expliquer la SVD comme « rotation, étirement, rotation »

<details><summary>Indice 1</summary>

Relis « Trois étapes » et « L'image de la sphère unité » (fiche §2), et la figure du §2.

</details>
<details><summary>Indice 2</summary>

Trois étapes : choisir deux directions perpendiculaires, étirer chacune, puis tourner le résultat.

</details>
<details><summary>Indice 3</summary>

Un cercle devient une ellipse ; ses deux axes viennent de deux diamètres perpendiculaires du cercle ; une valeur singulière nulle aplatit l'ellipse en un segment.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M12d.E1 — « Comment choisissez-vous le nombre de composantes d'une ACP ? »

<details><summary>Indice 1</summary>

Relis « Choisir $k$ » et le ⚠️ du §7.

</details>
<details><summary>Indice 2</summary>

Trois façons : un seuil sur la part cumulée, le coude, la validation du modèle qui suit.

</details>
<details><summary>Indice 3</summary>

Termine par l'erreur de reconstruction : la variance oubliée, au facteur $\frac{n-1}{n}$ près.

</details>

### M12d.E2 — « Que dit le conditionnement d'une matrice ? »

<details><summary>Indice 1</summary>

Relis « Le conditionnement » et le piège des équations normales (fiche §4).

</details>
<details><summary>Indice 2</summary>

$\kappa = s_{\max}/s_{\min}$ ; $\log_{10}\kappa$ chiffres perdus ; le déterminant mesure un volume, pas un aplatissement.

</details>
<details><summary>Indice 3</summary>

Un exemple : des features presque redondantes et une régression instable, la ridge qui remonte les petites valeurs singulières.

</details>

<a id="notebook"></a>

## Notebook

### Ex M12d.26 — La SVD par les valeurs propres de AᵀA · `svd`

<details><summary>Indice 1</summary>

Relis la recette de la fiche §1 et la docstring de `svd`.

</details>
<details><summary>Indice 2</summary>

`values, vectors = np.linalg.eigh(M.T @ M)`, puis `order = np.argsort(values)[::-1]` : réordonne les valeurs ET les colonnes de `vectors`.

</details>
<details><summary>Indice 3</summary>

`s = np.sqrt(np.clip(values[order], 0, None))`, `r = int(np.sum(s > tol * s[0]))` ; la convention sur chaque colonne gardée ; `U = (M @ V) / s` divise chaque colonne.

</details>

### Ex M12d.27 — Approximation de rang faible et conditionnement · `low_rank_approximation, condition_number`

<details><summary>Indice 1</summary>

Relis Eckart-Young (fiche §3) et la définition de $\kappa$ (fiche §4).

</details>
<details><summary>Indice 2</summary>

`U, s, Vt = svd(A)` ; $\mathbf{A}_k$ = `(U[:, :k] * s[:k]) @ Vt[:k]`.

</details>
<details><summary>Indice 3</summary>

Pour `condition_number` : `math.inf` si `len(s) < min(A.shape)`, sinon `float(s[0] / s[-1])`.

</details>

### Ex M12d.28 — La pseudo-inverse · `pinv`

<details><summary>Indice 1</summary>

Relis la définition de $\mathbf{A}^+$ (fiche §4).

</details>
<details><summary>Indice 2</summary>

`U, s, Vt = svd(A, tol=rcond)`, puis $\mathbf{V}\operatorname{diag}(1/s)\mathbf{U}^\top$.

</details>
<details><summary>Indice 3</summary>

`(Vt.T / s) @ U.T` : diviser les colonnes de `Vt.T` par `s` évite la matrice diagonale ; une matrice nulle donne `s` vide, et le produit des formes $(n, 0)$ et $(0, m)$ est nul.

</details>

### Ex M12d.29 — Les axes principaux d'une matrice de covariance, et la variance expliquée · `principal_axes, explained_variance_ratio`

<details><summary>Indice 1</summary>

Relis la définition des axes principaux (fiche §5) et la docstring.

</details>
<details><summary>Indice 2</summary>

`values, Q = np.linalg.eigh(C)`, puis l'ordre décroissant : `values[::-1]`, `Q[:, ::-1]`.

</details>
<details><summary>Indice 3</summary>

La convention : pour chaque colonne, `np.argmax(np.abs(col))`, et le signe de cet élément ; les variances : `np.maximum(values, 0.0) + 0.0` (ni négatives ni $-0{,}0$).

</details>

### Ex M12d.30 — `np.linalg.svd`, `np.linalg.cond` et `sklearn.decomposition.PCA` contre tes fonctions : les signes

<details><summary>Indice 1</summary>

Relis les 💻 des §1, §4 et §6.

</details>
<details><summary>Indice 2</summary>

Pour b) : `signs = np.sign(Vt[np.arange(r), np.argmax(np.abs(Vt), axis=1)])`, puis `Vt * signs[:, None]` et `U * signs`.

</details>
<details><summary>Indice 3</summary>

d) `np.cov(X_30).shape` ; g) compare `np.var(scores, axis=0, ddof=0)` et `ddof=1` à `explained_variance_`.

</details>

### Ex M12d.31 — Prédire l'allure des valeurs singulières d'une image, et le rang qui suffit

<details><summary>Indice 1</summary>

Relis « Compresser » et le ⚠️ du §3, et la figure du §3.

</details>
<details><summary>Indice 2</summary>

Une photo a beaucoup de structure qui se répète ; du bruit indépendant n'en a aucune.

</details>
<details><summary>Indice 3</summary>

Sans centrer, la première couche porte surtout le niveau de gris moyen.

</details>

### Ex M12d.32 — Compresser une image du domaine public : l'erreur en fonction du rang

<details><summary>Indice 1</summary>

Relis « Compresser » (fiche §3) et M12d.31.

</details>
<details><summary>Indice 2</summary>

`U, s, Vt = np.linalg.svd(A - A.mean(), full_matrices=False)` ; la part gardée au rang $k$ est `np.cumsum(s ** 2)[k - 1] / np.sum(s ** 2)`.

</details>
<details><summary>Indice 3</summary>

Le plus petit rang qui atteint un seuil : `int(np.argmax(shares >= 0.9) + 1)` ; e) se calcule sur les matrices, avec `np.linalg.norm`.

</details>

### Ex M12d.33 — La SVD par AᵀA contre `np.linalg.svd` : ce qu'on perd quand κ est grand

<details><summary>Indice 1</summary>

Relis le piège des équations normales (fiche §4) et la docstring de `svd`.

</details>
<details><summary>Indice 2</summary>

`A = make_conditioned(kappa)` ; la plus petite valeur singulière vraie est `1 / kappa`.

</details>
<details><summary>Indice 3</summary>

Pour chaque $\kappa$ : `abs(svd_33(A, tol=1e-12)[1][-1] - 1 / kappa) * kappa` et la même chose avec `np.linalg.svd(A, compute_uv=False)[-1]`.

</details>

### Ex M12d.34 — La SVD en images : Vᵀ, Σ puis U appliqués au cercle unité, étape par étape

<details><summary>Indice 1</summary>

Relis « Trois étapes » (fiche §2) et sa figure.

</details>
<details><summary>Indice 2</summary>

`angles = np.linspace(0, 2 * np.pi, 200, endpoint=False)`, `circle = np.vstack([np.cos(angles), np.sin(angles)])` : les images sont `Vt @ circle`, `np.diag(s) @ Vt @ circle`, `A @ circle`.

</details>
<details><summary>Indice 3</summary>

Les flèches : les colonnes de `Vt.T`, puis `np.eye(2)`, `np.diag(s)` et `U * s`, avec `ax.annotate("", xy=..., xytext=(0, 0), arrowprops=...)`.

</details>

### Ex M12d.35 — Chasse à l'erreur : une ACP sans centrer, n et n − 1 mélangés, des axes lus en lignes au lieu de colonnes

<details><summary>Indice 1</summary>

Relis les ⚠️ des §5 et §6.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, demande-toi ce que serait le résultat sur un petit exemple, et compare avec le commentaire.

</details>
<details><summary>Indice 3</summary>

Trois questions : autour de quel point la ligne (A) mesure-t-elle la dispersion ? Que sélectionne `vectors[order]` ? Par quoi `var` divise-t-elle ?

</details>

### Ex M12d.36 — Un test : la reconstruction de rang plein redonne X, et l'erreur décroît avec k

<details><summary>Indice 1</summary>

Relis Eckart-Young (fiche §3), « L'erreur de reconstruction » (fiche §7) et M12d.18.

</details>
<details><summary>Indice 2</summary>

`errors = [np.mean(np.sum((X - reconstruct(X, k)) ** 2, axis=1)) for k in range(p + 1)]`.

</details>
<details><summary>Indice 3</summary>

Propriété 3 : `variances = np.linalg.eigvalsh(np.cov(X, rowvar=False))[::-1]`, puis `np.testing.assert_allclose(errors, [(n - 1) / n * variances[k:].sum() for k in range(p + 1)], ...)`.

</details>

### Ex M12d.37 — Défi : compresser une image centrée en gardant 93 % de son énergie avec au plus 5 % des nombres

<details><summary>Indice 1</summary>

Relis la fiche §3 (compresser) et §6 (l'ACP) : quelle matrice décomposer ?

</details>
<details><summary>Indice 2</summary>

Découpe l'image en petits carrés de $p \times p$ pixels (8 divise 400 et 600) et range chaque carré en **ligne** d'une matrice : ces lignes se ressemblent.

</details>
<details><summary>Indice 3</summary>

`patches = A.reshape(m // p, p, n // p, p).transpose(0, 2, 1, 3).reshape(-1, p * p)` ; une ACP de ces lignes (centrer par le carré moyen, puis SVD), avec quelques composantes ; compte : $p^2 + kp^2 + (\text{nombre de carrés}) \times k$.

</details>
