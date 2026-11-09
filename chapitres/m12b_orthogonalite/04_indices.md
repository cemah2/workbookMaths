# M12b · Orthogonalité et projections — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M12b.Q1 — Produit scalaire ou pas ? Symétrie et positivité

<details><summary>Indice 1</summary>

Relis « Trois propriétés, pas une formule » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Teste dans l'ordre : bilinéaire ? symétrique ($\langle \mathbf{e}_1, \mathbf{e}_2 \rangle$ contre $\langle \mathbf{e}_2, \mathbf{e}_1 \rangle$) ? défini positif ?

</details>
<details><summary>Indice 3</summary>

2 et 5 : essaie $\mathbf{x} = (1, -1)$. 3 : complète le carré. 6 : remplace $\mathbf{x}$ par $-\mathbf{x}$.

</details>

### M12b.Q2 — Orthogonale, orthonormée, matrice orthogonale

<details><summary>Indice 1</summary>

Relis « Familles orthogonales et orthonormées » et « Matrices orthogonales » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Orthogonaux : produit scalaire nul ; orthonormés : en plus, de norme 1 ; matrice orthogonale : $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}$.

</details>
<details><summary>Indice 3</summary>

6 : « Des colonnes orthonormées, sans être carrée » (fiche §2).

</details>

### M12b.Q3 — Gram-Schmidt : ce que chaque étape retire

<details><summary>Indice 1</summary>

Relis « L'idée : retirer ce qui est déjà expliqué » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\mathbf{v}_k = \mathbf{a}_k - \sum_{j<k} \langle \mathbf{a}_k, \mathbf{q}_j \rangle\,\mathbf{q}_j$.

</details>
<details><summary>Indice 3</summary>

4 : $\mathbf{q}_1 = (1, 0)$, puis retire de $(1, 2)$ sa projection sur $\mathbf{q}_1$.

</details>

### M12b.Q4 — Le complément orthogonal : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Définition » et les « Propriétés » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$U^\perp$ est un sous-espace de dimension $n - \dim U$ ; c'est un noyau.

</details>
<details><summary>Indice 3</summary>

4 : regarde dans quel espace vit chaque objet.

</details>

### M12b.Q5 — Une matrice de projection : sur quoi, et quelles propriétés ?

<details><summary>Indice 1</summary>

Relis « La matrice de projection » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Le sous-espace est l'image de $\mathbf{P}$, l'ensemble des vecteurs qu'elle laisse fixes.

</details>
<details><summary>Indice 3</summary>

4 : applique-la à $(1, 1)$ et à $(1, -1)$.

</details>

### M12b.Q6 — Moindres carrés et projection

<details><summary>Indice 1</summary>

Relis « Le plus proche point de l'image » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Le résidu est orthogonal à chaque colonne de $\mathbf{X}$.

</details>
<details><summary>Indice 3</summary>

6 : « Deux espaces à ne pas confondre » (fiche §6).

</details>

### M12b.Q7 — QR : formes et propriétés

<details><summary>Indice 1</summary>

Relis « Gram-Schmidt écrit avec des matrices » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\mathbf{Q}$ a la forme de $\mathbf{A}$ ; $\mathbf{R}$ est carrée.

</details>
<details><summary>Indice 3</summary>

5 : « Les signes » (fiche §7).

</details>

### M12b.Q8 — Des fonctions orthogonales

<details><summary>Indice 1</summary>

Relis « Des intégrales au lieu de sommes » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Le produit d'une fonction paire et d'une impaire est impair.

</details>
<details><summary>Indice 3</summary>

6 : une fonction continue qui ne s'annule pas en $x_0$ reste loin de 0 autour de $x_0$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M12b.R1 — La projection sur une droite (M07)

<details><summary>Indice 1</summary>

Relis la projection sur une droite (M07 §4).

</details>
<details><summary>Indice 2</summary>

$\mathbf{p} = \frac{\mathbf{x} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\,\mathbf{u}$.

</details>
<details><summary>Indice 3</summary>

La distance est la norme de $\mathbf{x} - \mathbf{p}$.

</details>

### M12b.R2 — Les équations normales et la matrice chapeau (M09b)

<details><summary>Indice 1</summary>

Relis M09b §3 et §4 (équations normales, matrice chapeau).

</details>
<details><summary>Indice 2</summary>

$\mathbf{X}^\top\mathbf{X}$ contient $n$, $\sum x_i$, $\sum x_i^2$ ; ici, $\sum x_i = 0$.

</details>
<details><summary>Indice 3</summary>

La trace de $\mathbf{H}$ est le nombre de colonnes de $\mathbf{X}$ (M09b).

</details>

### M12b.R3 — Base, rang et noyau (M12a)

<details><summary>Indice 1</summary>

Relis M12a §6 (noyau, image, théorème du rang).

</details>
<details><summary>Indice 2</summary>

Réduis $\mathbf{A}$ : $L_2 \leftarrow L_2 - 2L_1$.

</details>
<details><summary>Indice 3</summary>

6 : écris $\mathbf{A}\mathbf{x} = \mathbf{0}$ ligne par ligne.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M12b.1 — Un produit scalaire défini par une matrice 2 × 2 : normes, angles, orthogonalité

<details><summary>Indice 1</summary>

Relis « Les produits scalaires de ℝⁿ » et l'exemple (fiche §1).

</details>
<details><summary>Indice 2</summary>

$\langle \mathbf{x}, \mathbf{y} \rangle_{\mathbf{M}} = \mathbf{x}^\top(\mathbf{M}\mathbf{y})$ : calcule d'abord $\mathbf{M}\mathbf{y}$, puis un produit scalaire usuel.

</details>
<details><summary>Indice 3</summary>

a) et h) : $a > 0$ et $ac - b^2 > 0$. g) $\mathbf{M}(1, 1) = (4, 2)$.

</details>

### Ex M12b.2 — Les coordonnées dans une base orthonormée : des produits scalaires au lieu d'un système

<details><summary>Indice 1</summary>

Relis « Les coordonnées dans une base orthonormée » (fiche §2).

</details>
<details><summary>Indice 2</summary>

$c_i = \mathbf{x} \cdot \mathbf{u}_i$, sans oublier le facteur $\frac{1}{5}$.

</details>
<details><summary>Indice 3</summary>

e) $\mathbf{u}_1 - \mathbf{u}_3 + 2\mathbf{u}_4$. f) Dans une base orthogonale, $c_i = \frac{\mathbf{x} \cdot \mathbf{u}_i}{\lVert \mathbf{u}_i \rVert^2}$.

</details>

### Ex M12b.3 — Une matrice orthogonale 3 × 3 conserve normes et angles

<details><summary>Indice 1</summary>

Relis « Matrices orthogonales » (fiche §2).

</details>
<details><summary>Indice 2</summary>

$\mathbf{Q}\mathbf{x}$ combine les colonnes de $\mathbf{Q}$ avec les coordonnées de $\mathbf{x}$.

</details>
<details><summary>Indice 3</summary>

e) $\mathbf{Q}^{-1} = \mathbf{Q}^\top$ : 7 fois la première **ligne** de $\mathbf{Q}$.

</details>

### Ex M12b.4 — Gram-Schmidt sur trois vecteurs de ℝ³

<details><summary>Indice 1</summary>

Relis l'exemple de Gram-Schmidt dans $\mathbb{R}^3$ (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\mathbf{q}_1 = \frac{1}{9}(4, 1, 8)$ ; $\mathbf{a}_2 \cdot \mathbf{q}_1$ est négatif : $\mathbf{v}_2 = \mathbf{a}_2 + 3\mathbf{q}_1$.

</details>
<details><summary>Indice 3</summary>

Garde les tiers et les neuvièmes ; $\mathbf{v}_3 = \mathbf{a}_3 + \mathbf{q}_1 - \mathbf{q}_2$.

</details>

### Ex M12b.5 — Gram-Schmidt pour un produit scalaire qui n'est pas l'usuel

<details><summary>Indice 1</summary>

Relis « Classique ou modifié » (dernier paragraphe) et « En machine learning » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Toutes les formules de Gram-Schmidt, avec $\langle \cdot, \cdot \rangle_{\mathbf{D}}$ partout : chaque produit compte deux fois les deuxièmes coordonnées.

</details>
<details><summary>Indice 3</summary>

$\lVert \mathbf{a}_1 \rVert_{\mathbf{D}}^2 = 1 + 2 + 1$ ; $\langle \mathbf{a}_2, \mathbf{q}_1 \rangle_{\mathbf{D}} = -1$.

</details>

### Ex M12b.6 — Une base du complément orthogonal d'un plan de ℝ⁴

<details><summary>Indice 1</summary>

Relis « Définition » et l'exemple (fiche §4).

</details>
<details><summary>Indice 2</summary>

$U^\perp$ est le noyau de la matrice dont les **lignes** sont $\mathbf{a}$ et $\mathbf{b}$ ; elle est déjà réduite.

</details>
<details><summary>Indice 3</summary>

$x_1 = x_3 - 2x_4$ et $x_2 = -x_3 - x_4$.

</details>

### Ex M12b.7 — Projeter sur un plan de ℝ³ : avec une base quelconque, puis orthonormée

<details><summary>Indice 1</summary>

Relis « Deux façons de calculer » et l'exemple (fiche §5).

</details>
<details><summary>Indice 2</summary>

$\mathbf{A}^\top\mathbf{A}\,\mathbf{c} = \mathbf{A}^\top\mathbf{v}$ : un système $2 \times 2$ ; son déterminant vaut 81.

</details>
<details><summary>Indice 3</summary>

e) Puis $\mathbf{p} = (\mathbf{v} \cdot \mathbf{q}_1)\,\mathbf{q}_1 + (\mathbf{v} \cdot \mathbf{q}_2)\,\mathbf{q}_2$, pour vérifier d).

</details>

### Ex M12b.8 — La matrice de projection : P² = P, Pᵀ = P, trace et rang

<details><summary>Indice 1</summary>

Relis « La matrice de projection » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Le noyau de $\mathbf{P}$ est $U^\perp$, son image $U$ ; sa trace est la dimension de $U$.

</details>
<details><summary>Indice 3</summary>

f) $(\mathbf{I} - \mathbf{P})\mathbf{v} = \mathbf{v} - \mathbf{P}\mathbf{v}$. h) Compare $\mathbf{M}$ et $\mathbf{M}^\top$.

</details>

### Ex M12b.9 — La distance d'un point à un sous-espace, et le résidu orthogonal

<details><summary>Indice 1</summary>

Relis « Deux façons de calculer » (fiche §5), le cas d'une base orthogonale.

</details>
<details><summary>Indice 2</summary>

Les coefficients sont $\frac{\mathbf{v} \cdot \mathbf{u}_i}{\lVert \mathbf{u}_i \rVert^2}$, avec $\lVert \mathbf{u}_1 \rVert^2 = 4$ et $\lVert \mathbf{u}_2 \rVert^2 = 10$.

</details>
<details><summary>Indice 3</summary>

g) Par Pythagore, la distance à la droite au carré vaut $\lVert \mathbf{v} \rVert^2 - \frac{(\mathbf{v} \cdot \mathbf{u}_1)^2}{\lVert \mathbf{u}_1 \rVert^2}$.

</details>

### Ex M12b.10 — Des moindres carrés comme une projection : y, son projeté et le résidu

<details><summary>Indice 1</summary>

Relis l'exemple du §6 de la fiche.

</details>
<details><summary>Indice 2</summary>

$\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} n & \sum x_i \\ \sum x_i & \sum x_i^2 \end{pmatrix}$, $\mathbf{X}^\top\mathbf{y} = (\sum y_i, \sum x_iy_i)$.

</details>
<details><summary>Indice 3</summary>

Le déterminant vaut 50 ; $\mathbf{w}^* = \frac{1}{50}\begin{pmatrix} 55 & -15 \\ -15 & 5 \end{pmatrix}\mathbf{X}^\top\mathbf{y}$.

</details>

### Ex M12b.11 — La décomposition QR d'une matrice 3 × 2, puis les moindres carrés par R w = Qᵀy

<details><summary>Indice 1</summary>

Relis « Gram-Schmidt écrit avec des matrices » et « Les moindres carrés par QR » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$r_{11} = \lVert \mathbf{a}_1 \rVert$, $r_{12} = \mathbf{q}_1 \cdot \mathbf{a}_2$, $r_{22} = \lVert \mathbf{a}_2 - r_{12}\mathbf{q}_1 \rVert$ ; tout est en onzièmes.

</details>
<details><summary>Indice 3</summary>

g) Commence par la dernière ligne : $r_{22}w_2 = (\mathbf{Q}^\top\mathbf{y})_2$.

</details>

### Ex M12b.12 — Le produit scalaire de fonctions sur [−1 ; 1] : orthogonaliser 1, x et x²

<details><summary>Indice 1</summary>

Relis le §8 de la fiche, et M02a pour les intégrales.

</details>
<details><summary>Indice 2</summary>

Sur $[-1 ; 1]$, l'intégrale d'une fonction impaire est nulle, celle d'une fonction paire vaut deux fois l'intégrale sur $[0 ; 1]$.

</details>
<details><summary>Indice 3</summary>

f) $\int_{-1}^1 |x|\,x^2\,dx = 2\int_0^1 x^3\,dx$. g) Les trois coefficients sur $1, x, p_2$, puis développe.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M12b.13 — L'inégalité de Cauchy-Schwarz pour tout produit scalaire

<details><summary>Indice 1</summary>

Relis « Trois propriétés, pas une formule » (fiche §1) et la projection sur une droite (fiche §5).

</details>
<details><summary>Indice 2</summary>

Développe $\langle \mathbf{x} - t\mathbf{y}, \mathbf{x} - t\mathbf{y} \rangle$ en quatre termes, puis regroupe.

</details>
<details><summary>Indice 3</summary>

Le nombre $\lVert \mathbf{x} - t\mathbf{y} \rVert^2$ est positif ; avec le bon $t$, il vaut $\lVert \mathbf{x} \rVert^2 - \frac{\langle \mathbf{x}, \mathbf{y} \rangle^2}{\lVert \mathbf{y} \rVert^2}$.

</details>

### Ex M12b.14 — Une famille orthogonale de vecteurs non nuls est libre

<details><summary>Indice 1</summary>

Relis le paragraphe « Une famille orthogonale de vecteurs non nuls est libre » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Le produit scalaire avec $\mathbf{u}_j$ fait disparaître tous les termes sauf un.

</details>
<details><summary>Indice 3</summary>

5 : développe $\langle \sum_i c_i\mathbf{q}_i, \sum_j c_j\mathbf{q}_j \rangle$ en une double somme.

</details>

### Ex M12b.15 — Gram-Schmidt donne une base orthonormée du même sous-espace

<details><summary>Indice 1</summary>

Relis le §3 de la fiche, et la récurrence (R4).

</details>
<details><summary>Indice 2</summary>

Pour 3, utilise que $\mathbf{q}_1, \ldots, \mathbf{q}_{j-1}$ sont orthonormés (l'hypothèse de récurrence).

</details>
<details><summary>Indice 3</summary>

Pour 4 : une inclusion, puis deux familles libres de $j$ vecteurs (M12a §3, dimension).

</details>

### Ex M12b.16 — L'orthogonal de l'image de A est le noyau de Aᵀ

<details><summary>Indice 1</summary>

Relis « Définition » (fiche §4) et le théorème du rang (M12a §6).

</details>
<details><summary>Indice 2</summary>

La $j$-ième coordonnée de $\mathbf{A}^\top\mathbf{y}$ est $\mathbf{a}_j \cdot \mathbf{y}$.

</details>
<details><summary>Indice 3</summary>

4 : $\mathbf{y} \cdot \mathbf{A}\mathbf{x} = (\mathbf{A}^\top\mathbf{y}) \cdot \mathbf{x}$.

</details>

### Ex M12b.17 — Le projeté orthogonal est le point le plus proche (Pythagore)

<details><summary>Indice 1</summary>

Relis « Sur un sous-espace : la caractérisation » (fiche §5) et M07.17.

</details>
<details><summary>Indice 2</summary>

Écris $\mathbf{v} - \mathbf{u} = (\mathbf{v} - \mathbf{p}) + (\mathbf{p} - \mathbf{u})$ : le second terme est dans $U$.

</details>
<details><summary>Indice 3</summary>

4 : un vecteur à la fois dans $U$ et dans $U^\perp$ est orthogonal à lui-même.

</details>

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12b.18 — Pont : retirer d'une feature ce qu'explique une autre, une projection puis un résidu

<details><summary>Indice 1</summary>

Relis « En machine learning » (fiche §3) et « Une base orthogonale de Im X simplifie tout » (fiche §6).

</details>
<details><summary>Indice 2</summary>

$t = \frac{10}{10}$ ; $\mathbf{r} = \mathbf{x}_2 - \mathbf{x}_1$.

</details>
<details><summary>Indice 3</summary>

g) Les équations normales $\begin{pmatrix} 10 & 10 \\ 10 & 14 \end{pmatrix}\mathbf{w} = (23, 29)$.

</details>

### Ex M12b.19 — Pont : projeter sur k directions orthonormées, reconstruire, et l'erreur par Pythagore

<details><summary>Indice 1</summary>

Relis « Projeter, puis reconstruire » (fiche §5) et Parseval (fiche §2).

</details>
<details><summary>Indice 2</summary>

$z_i = \mathbf{u}_i \cdot \mathbf{x}$, avec le facteur $\frac{1}{2}$ ; $\hat{\mathbf{x}} = z_1\mathbf{u}_1 + z_2\mathbf{u}_2$.

</details>
<details><summary>Indice 3</summary>

Pour la démonstration : écris $\mathbf{x}$ dans la base complète, et retranche les $k$ premiers termes.

</details>

### Ex M12b.20 — MML §3.2, §3.5 à §3.7 : produits scalaires, orthogonalité, fonctions, en anglais

<details><summary>Indice 1</summary>

Lis MML §3.2, §3.5, §3.6 et §3.7, crayon en main.

</details>
<details><summary>Indice 2</summary>

Pour 2, cherche la matrice $\mathbf{A}$ telle que l'exemple du livre s'écrive $\mathbf{x}^\top\mathbf{A}\mathbf{y}$.

</details>
<details><summary>Indice 3</summary>

Pour 3, relis la fiche §1 : $a_{ii} = \mathbf{e}_i^\top\mathbf{A}\mathbf{e}_i$.

</details>

### Ex M12b.21 — MML §3.8 et §9.4 : projections, Gram-Schmidt et moindres carrés

<details><summary>Indice 1</summary>

Lis MML §3.8 et §9.4, crayon en main.

</details>
<details><summary>Indice 2</summary>

Compare chaque formule du livre avec celle de la fiche §5 ($\mathbf{B}$ du livre = $\mathbf{A}$ de la fiche).

</details>
<details><summary>Indice 3</summary>

6 : $\mathbf{x}_0 = (1, 1, 1)$ est sur le plan, et $(3, 3, 3) - \mathbf{x}_0$ lui est normal.

</details>

### Ex M12b.22 — Fermi : le coût de Gram-Schmidt sur une matrice 100 000 × 50

<details><summary>Indice 1</summary>

Relis « Classique ou modifié » (fiche §3) et M12a.24 (une estimation de Fermi).

</details>
<details><summary>Indice 2</summary>

Compte, pour la colonne $k$, les opérations sur des vecteurs de longueur $m$, puis additionne sur $k$.

</details>
<details><summary>Indice 3</summary>

$\sum_{k=1}^{n} (k - 1) \approx \frac{n^2}{2}$ ; chaque opération coûte $2m$.

</details>

### Ex M12b.23 — Expliquer pourquoi le projeté est le point le plus proche

<details><summary>Indice 1</summary>

Relis « Sur un sous-espace : la caractérisation » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Pense au fil à plomb et au triangle rectangle.

</details>
<details><summary>Indice 3</summary>

L'hypoténuse est le plus long côté d'un triangle rectangle ; pour l'exemple, pense aux prédictions d'une régression.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M12b.E1 — « Pourquoi résoudre des moindres carrés par QR plutôt que par les équations normales ? »

<details><summary>Indice 1</summary>

Relis « Pourquoi QR plutôt que les équations normales » (fiche §7) et M09b.32.

</details>
<details><summary>Indice 2</summary>

Deux idées : $\mathbf{X}^\top\mathbf{X}$ « met au carré » la difficulté ; $\mathbf{Q}$ conserve les normes.

</details>
<details><summary>Indice 3</summary>

Termine par les bibliothèques (Householder, LAPACK, la SVD) et le cas où les équations normales suffisent.

</details>

### M12b.E2 — « Qu'est-ce qu'une matrice orthogonale, et pourquoi est-elle agréable en calcul numérique ? »

<details><summary>Indice 1</summary>

Relis « Matrices orthogonales » et « En machine learning » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Définition, ce qu'elle conserve, son inverse.

</details>
<details><summary>Indice 3</summary>

Pour le numérique : multiplier par $\mathbf{Q}$ ne grossit pas les erreurs.

</details>

<a id="notebook"></a>

## Notebook

### Ex M12b.24 — Gram-Schmidt, classique et modifié · `gram_schmidt`

<details><summary>Indice 1</summary>

Relis « L'idée » et « Classique ou modifié » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Une boucle sur les colonnes ; dans la boucle intérieure, le coefficient est `Q[:, j] @ a` (classique) ou `Q[:, j] @ v` (modifié).

</details>
<details><summary>Indice 3</summary>

Le test de dépendance est **relatif** : `norm(v) <= tol * norm(a)` ; puis `Q[:, k] = v / norm(v)`.

</details>

### Ex M12b.25 — La projection orthogonale sur un sous-espace · `project`

<details><summary>Indice 1</summary>

Relis « Deux façons de calculer » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Vérifie les formes, puis `Q = gram_schmidt(A)` ; laisse passer sa `ValueError`.

</details>
<details><summary>Indice 3</summary>

`Q @ (Q.T @ v)`.

</details>

### Ex M12b.26 — La décomposition QR et les moindres carrés par QR · `qr, least_squares_qr`

<details><summary>Indice 1</summary>

Relis « Gram-Schmidt écrit avec des matrices » et « Les moindres carrés par QR » (fiche §7).

</details>
<details><summary>Indice 2</summary>

`R = np.triu(Q.T @ A)` ; puis `z = Q.T @ y`.

</details>
<details><summary>Indice 3</summary>

La remontée : `for i in reversed(range(p)): w[i] = (z[i] - R[i, i + 1:] @ w[i + 1:]) / R[i, i]`.

</details>

### Ex M12b.27 — `np.linalg.qr` et `lstsq` contre ta projection et ta QR : les signes de Q et de R

<details><summary>Indice 1</summary>

Relis « Les signes » (fiche §7) et l'énoncé (« En pratique »).

</details>
<details><summary>Indice 2</summary>

`np.linalg.qr(A)` rend `(Q, R)` ; `np.linalg.lstsq(...)` rend quatre objets, le rang en troisième.

</details>
<details><summary>Indice 3</summary>

d) `D = np.diag(np.sign(np.diag(R_np)))`, puis `np.allclose(Q_np @ D, Q)` et `np.allclose(D @ R_np, R)`.

</details>

### Ex M12b.28 — Prédire : Gram-Schmidt classique sur des vecteurs presque colinéaires, QᵀQ vaut-il encore I ?

<details><summary>Indice 1</summary>

Relis « Classique ou modifié » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Les colonnes ne diffèrent que de $10^{-9}$ : que valent les $\mathbf{v}_k$, et leurs erreurs d'arrondi relatives ?

</details>
<details><summary>Indice 3</summary>

Chaque colonne de $\mathbf{Q}$ est divisée par sa norme : c'est l'orthogonalité qui peut se perdre.

</details>

### Ex M12b.29 — Gram-Schmidt classique contre modifié : l'orthogonalité perdue quand les colonnes sont presque dépendantes

<details><summary>Indice 1</summary>

Relis M12b.28 et le §8 de la fiche (des features polynomiales).

</details>
<details><summary>Indice 2</summary>

Une boucle sur `DEGREES_29` ; trois appels à `orthogonality_loss`.

</details>
<details><summary>Indice 3</summary>

« Deux fois » : `gram_schmidt(gram_schmidt(A, modified=False), modified=False)`, sur le **résultat** de la première passe.

</details>

### Ex M12b.30 — Projeter un nuage de ℝ³ sur un plan : les résidus orthogonaux en image

<details><summary>Indice 1</summary>

Relis « Deux façons de calculer » (fiche §5) et la figure du §5.

</details>
<details><summary>Indice 2</summary>

Un projeté par point : `np.array([mymath.orthogonal.project(x, A) for x in X])`.

</details>
<details><summary>Indice 3</summary>

Un `ax.plot` par segment, avec trois listes de deux nombres : `[x[0], p[0]]`, `[x[1], p[1]]`, `[x[2], p[2]]`.

</details>

### Ex M12b.31 — Chasse à l'erreur : une normalisation oubliée, QQᵀ sur une base non orthonormée, R w = Qᵀy résolu dans le mauvais sens

<details><summary>Indice 1</summary>

Relis les erreurs classiques des §3, §5 et §7 de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, calcule à la main ce que dit son commentaire, puis ce que fait le code.

</details>
<details><summary>Indice 3</summary>

(A) Quelle est la norme de $\mathbf{v}_2$ ? (B) Les colonnes de $\mathbf{A}$ sont-elles orthonormées ? (D) Dans quel sens va la boucle ?

</details>

### Ex M12b.32 — Un test de propriétés pour la projection : idempotente, symétrique, résidu orthogonal

<details><summary>Indice 1</summary>

Relis « La matrice de projection » (fiche §5) et M12a.34.

</details>
<details><summary>Indice 2</summary>

Trois `assert` : `project(p, A)` contre `p`, `project(u, A) @ v` contre `u @ p`, et `A.T @ (v - p)` contre 0.

</details>
<details><summary>Indice 3</summary>

Tire $k$ avec `rng.integers(1, m)` : un sous-espace strict.

</details>

### Ex M12b.33 — Défi : des colonnes presque dépendantes, des moindres carrés à 1e−8 près de `lstsq` par l'orthogonalisation de [X | y]

<details><summary>Indice 1</summary>

Relis M12b.28 et la fin du §7 de la fiche.

</details>
<details><summary>Indice 2</summary>

Ajoute $\mathbf{y}$ comme dernière colonne, et fais le procédé **modifié** en gardant chaque coefficient $r_{jk}$ au moment où tu retires la projection.

</details>
<details><summary>Indice 3</summary>

Le second membre est la dernière colonne de ce $\mathbf{R}$ (sans sa dernière ligne) ; remonte sur $\mathbf{R}_{[:p, :p]}$.

</details>
