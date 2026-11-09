# M12a · Espaces vectoriels et applications linéaires — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M12a.Q1 — Sous-espace ou pas ?

<details><summary>Indice 1</summary>

Relis « Sous-espaces » (fiche §1) : trois conditions.

</details>
<details><summary>Indice 2</summary>

Teste d'abord le vecteur nul ; puis cherche un contre-exemple simple pour la somme ou pour la multiplication par $-1$.

</details>
<details><summary>Indice 3</summary>

5 : prends un vecteur sur chaque axe. 6 : le polynôme nul, puis $x^2 + x$ et $-x^2$.

</details>

### M12a.Q2 — Combinaison linéaire et famille génératrice

<details><summary>Indice 1</summary>

Relis « Combinaisons linéaires et sous-espace engendré » (fiche §2) et « Dimension » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Deux vecteurs colinéaires n'engendrent qu'une droite ; une famille génératrice d'un espace de dimension $n$ a au moins $n$ vecteurs.

</details>
<details><summary>Indice 3</summary>

6 : écris $\mathbf{u}$ et $\mathbf{v}$ avec $\mathbf{u} + \mathbf{v}$ et $\mathbf{u} - \mathbf{v}$.

</details>

### M12a.Q3 — Libre ou liée ?

<details><summary>Indice 1</summary>

Relis « Indépendance linéaire » et les « Quatre réflexes » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Une famille est liée dès qu'un de ses vecteurs combine les autres ; le rang le dit.

</details>
<details><summary>Indice 3</summary>

2 : la matrice des trois vecteurs est triangulaire. 6 : une combinaison de $\mathbf{u}$ et $\mathbf{v}$ est une combinaison des trois, avec 0 devant $\mathbf{w}$.

</details>

### M12a.Q4 — Base et dimension : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Bases » et « Dimension » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Compte les vecteurs d'une base évidente de chaque espace.

</details>
<details><summary>Indice 3</summary>

2 : $1, x, x^2, x^3, x^4$. 6 : une matrice à un seul 1 par position.

</details>

### M12a.Q5 — Le rang d'une matrice, d'une transposée, d'un produit

<details><summary>Indice 1</summary>

Relis « Le rang est une dimension » et « Le rang d'un produit » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$\operatorname{rg} \le \min(m, n)$, $\operatorname{rg}(\mathbf{A}^\top) = \operatorname{rg}(\mathbf{A})$, $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \min(\operatorname{rg}\mathbf{A}, \operatorname{rg}\mathbf{B})$.

</details>
<details><summary>Indice 3</summary>

5 : multiplier par une matrice inversible. 6 : « Un tableau centré perd un rang ».

</details>

### M12a.Q6 — Linéaire, affine, ou ni l'un ni l'autre ?

<details><summary>Indice 1</summary>

Relis la définition d'une application linéaire (fiche §5) et celle d'une application affine (fiche §8).

</details>
<details><summary>Indice 2</summary>

Une application linéaire envoie $\mathbf{0}$ sur $\mathbf{0}$ ; une application affine est $\mathbf{A}\mathbf{x} + \mathbf{b}$.

</details>
<details><summary>Indice 3</summary>

5 : compare $\lVert -\mathbf{x} \rVert$ et $-\lVert \mathbf{x} \rVert$.

</details>

### M12a.Q7 — Noyau et image : qui vit où ?

<details><summary>Indice 1</summary>

Relis « Deux sous-espaces attachés à une application » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Le noyau vit au départ (une coordonnée par colonne), l'image à l'arrivée (une par ligne).

</details>
<details><summary>Indice 3</summary>

3 : le théorème du rang, avec un rang au plus 3.

</details>

### M12a.Q8 — Changer de base : ce qui change et ce qui reste

<details><summary>Indice 1</summary>

Relis « Les coordonnées changent, le vecteur reste » et « La matrice d'une application dans une nouvelle base » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\mathbf{x} = \mathbf{S}\mathbf{x}'$ ; la nouvelle matrice est $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$.

</details>
<details><summary>Indice 3</summary>

6 : $\mathbf{S}^{-1}\mathbf{s}_1 = \mathbf{e}_1$, car $\mathbf{s}_1$ est la première colonne de $\mathbf{S}$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M12a.R1 — Le pivot de Gauss et la forme échelonnée réduite (M09a)

<details><summary>Indice 1</summary>

Relis M09a §6.

</details>
<details><summary>Indice 2</summary>

Commence par diviser la première ligne par 2, puis annule la première colonne sous le pivot.

</details>
<details><summary>Indice 3</summary>

La troisième ligne s'annule ; une variable libre, $x_3$.

</details>

### M12a.R2 — Produit matriciel et formes (M09a)

<details><summary>Indice 1</summary>

Relis M09a §3 et §4.

</details>
<details><summary>Indice 2</summary>

$(n, p) \times (p, m) \to (n, m)$ ; l'élément $(i, j)$ est le produit scalaire de la ligne $i$ et de la colonne $j$.

</details>
<details><summary>Indice 3</summary>

4 : la lecture en colonnes du produit (M09a §2).

</details>

### M12a.R3 — Combinaisons linéaires et produit scalaire dans ℝⁿ (M07)

<details><summary>Indice 1</summary>

Relis M07 §1 et §2.

</details>
<details><summary>Indice 2</summary>

Coordonnée par coordonnée ; $\mathbf{u} \cdot \mathbf{v} = \sum_i u_iv_i$.

</details>
<details><summary>Indice 3</summary>

4 : développe $(\mathbf{u} + \mathbf{v}) \cdot (\mathbf{u} - \mathbf{v})$. 5 : commence par la troisième coordonnée.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M12a.1 — Reconnaître des sous-espaces de ℝ³ et de l'espace des polynômes

<details><summary>Indice 1</summary>

Relis « Sous-espaces » (fiche §1) et l'erreur classique du §1.

</details>
<details><summary>Indice 2</summary>

Une équation linéaire de second membre nul définit un sous-espace ; un second membre non nul, une inégalité ou un carré, presque jamais.

</details>
<details><summary>Indice 3</summary>

d) Essaie $(1, 0, 1)$ et $(0, 1, 1)$. e) Multiplie un vecteur par $-1$. h) $2t = 4$.

</details>

### Ex M12a.2 — Écrire un vecteur comme combinaison linéaire : un système à résoudre

<details><summary>Indice 1</summary>

Relis « Être une combinaison, c'est résoudre un système » (fiche §2).

</details>
<details><summary>Indice 2</summary>

La deuxième coordonnée de $\lambda_1\mathbf{u}_1 + \lambda_2\mathbf{u}_2$ est $-\lambda_1$ : elle donne $\lambda_1$ d'un coup.

</details>
<details><summary>Indice 3</summary>

b) Trouve $\lambda_1$ et $\lambda_2$ avec deux coordonnées, puis vérifie la troisième. d) Deux produits scalaires nuls, avec $c = 3$.

</details>

### Ex M12a.3 — L'indépendance de trois vecteurs de ℝ³ par le pivot de Gauss

<details><summary>Indice 1</summary>

Relis « Le test par le pivot de Gauss » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Mets les vecteurs en **colonnes**, et réduis : une colonne sans pivot rend la famille liée, et sa colonne dans la forme réduite donne la relation.

</details>
<details><summary>Indice 3</summary>

e) $(1, 0, k) = a\mathbf{v}_1 + b\mathbf{v}_2$ : la première coordonnée donne $a$, la deuxième $b$.

</details>

### Ex M12a.4 — Extraire une base d'une famille génératrice, compléter une famille libre

<details><summary>Indice 1</summary>

Relis « Extraire une base, compléter une famille libre » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Repère d'abord les vecteurs multiples ou sommes d'autres vecteurs ; ils ne portent pas de pivot.

</details>
<details><summary>Indice 3</summary>

e) Est-ce que $\mathbf{e}_1$ est une combinaison de $\mathbf{u}$ et $\mathbf{v}$ ? Calcule $\mathbf{u} - 2\mathbf{v}$.

</details>

### Ex M12a.5 — Les coordonnées d'un vecteur dans une base qui n'est pas la base canonique

<details><summary>Indice 1</summary>

Relis « Coordonnées dans une base » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Les coordonnées $\mathbf{c}$ vérifient $c_1\mathbf{b}_1 + c_2\mathbf{b}_2 + c_3\mathbf{b}_3 = \mathbf{v}$ : un système de trois équations.

</details>
<details><summary>Indice 3</summary>

a) Additionne les trois équations : tu obtiens $c_1 + c_2 + c_3$. d) La première coordonnée donne $\alpha$, la troisième $\beta$.

</details>

### Ex M12a.6 — Le rang par les colonnes et par les lignes, celui d'un produit, et celui d'un tableau centré

<details><summary>Indice 1</summary>

Relis tout le §4 de la fiche.

</details>
<details><summary>Indice 2</summary>

Cherche une relation simple entre les lignes de $\mathbf{A}$ ; pour e), calcule $\mathbf{A}$ fois chaque colonne de $\mathbf{C}$.

</details>
<details><summary>Indice 3</summary>

e) Deux colonnes de $\mathbf{C}$ sont dans le noyau de $\mathbf{A}$. g) Les moyennes des colonnes sont des entiers.

</details>

### Ex M12a.7 — La matrice d'une application linéaire : les images des vecteurs de base

<details><summary>Indice 1</summary>

Relis « La matrice d'une application linéaire » (fiche §5).

</details>
<details><summary>Indice 2</summary>

La colonne $j$ est $f(\mathbf{e}_j)$. Pour e), écris $\mathbf{e}_1$ et $\mathbf{e}_2$ avec $(1, 1)$ et $(1, -1)$, puis utilise la linéarité.

</details>
<details><summary>Indice 3</summary>

f) La projection de $\mathbf{x}$ sur la droite dirigée par $\mathbf{u}$ est $\frac{\mathbf{x} \cdot \mathbf{u}}{\lVert \mathbf{u} \rVert^2}\,\mathbf{u}$ (M07 §4), avec $\mathbf{u} = (1, 1)$.

</details>

### Ex M12a.8 — Composer deux applications du plan, c'est multiplier leurs matrices

<details><summary>Indice 1</summary>

Relis « Composer, c'est multiplier » (fiche §5).

</details>
<details><summary>Indice 2</summary>

La matrice de « $a$, puis $b$ » est $\mathbf{B}\mathbf{A}$ : la dernière appliquée est à gauche.

</details>
<details><summary>Indice 3</summary>

g) $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$, et $\mathbf{A}^{-1} = \operatorname{diag}(\frac{1}{3}, 1)$.

</details>

### Ex M12a.9 — Noyau et image d'une matrice 3 × 4, et le théorème du rang

<details><summary>Indice 1</summary>

Relis « Les calculer par le pivot de Gauss » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Réduis $\mathbf{A}$ ; les lignes 2 et 3, après élimination dans la colonne 1, sont proportionnelles.

</details>
<details><summary>Indice 3</summary>

d) et e) $x_p = -R_{ij}$. g) Deux produits scalaires nuls avec les colonnes de f), avec $c = 1$.

</details>

### Ex M12a.10 — Toutes les solutions de A x = b : une solution particulière plus le noyau

<details><summary>Indice 1</summary>

Relis « Toutes les solutions de $\mathbf{A}\mathbf{x} = \mathbf{b}$ » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Réduis la matrice augmentée ; la troisième ligne est la somme des deux autres, second membre compris.

</details>
<details><summary>Indice 3</summary>

e) $\mathbf{x}_p + 2\mathbf{k}_1 - \mathbf{k}_2$. g) Le second membre doit vérifier la même relation que les lignes.

</details>

### Ex M12a.11 — Une base adaptée qui rend diagonale la matrice d'une application : S⁻¹AS

<details><summary>Indice 1</summary>

Relis « La matrice d'une application dans une nouvelle base » (fiche §7) et l'inverse $2 \times 2$ (M09a §7).

</details>
<details><summary>Indice 2</summary>

Compare $\mathbf{A}\mathbf{s}_1$ à $\mathbf{s}_1$, et $\mathbf{A}\mathbf{s}_2$ à $\mathbf{s}_2$ : la colonne $j$ de $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ contient les coordonnées de $\mathbf{A}\mathbf{s}_j$.

</details>
<details><summary>Indice 3</summary>

c) $\det\mathbf{S} = -1$. e) $\mathbf{S}^{-1}\mathbf{x}$. g) $\mathbf{S}$ fois les coordonnées de f).

</details>

### Ex M12a.12 — Une application affine du plan : partie linéaire, translation, inverse

<details><summary>Indice 1</summary>

Relis « La transformation inverse » (fiche §8).

</details>
<details><summary>Indice 2</summary>

$\mathbf{b} = \varphi(\mathbf{0})$, et $\varphi^{-1}(\mathbf{y}) = \mathbf{A}^{-1}(\mathbf{y} - \mathbf{b})$.

</details>
<details><summary>Indice 3</summary>

e) $-\mathbf{A}^{-1}\mathbf{b}$. f) Retire d'abord $\mathbf{b}$ : $(3, 4) - (-1, 4) = (4, 0)$.

</details>

### Ex M12a.13 — La dérivation sur les polynômes de degré au plus 3 : matrice, noyau, image

<details><summary>Indice 1</summary>

Relis « Dans d'autres bases » (fiche §5).

</details>
<details><summary>Indice 2</summary>

La colonne $j$ contient les coordonnées de la dérivée du $j$-ième vecteur de base : $D(x^2) = 2x$ a pour coordonnées $(0, 2, 0, 0)$.

</details>
<details><summary>Indice 3</summary>

e) Quels polynômes ont une dérivée nulle ? h) Combien de dérivations pour annuler $x^3$ ?

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M12a.14 — L'intersection de deux sous-espaces en est un ; la réunion, presque jamais

<details><summary>Indice 1</summary>

Relis la définition d'un sous-espace (fiche §1).

</details>
<details><summary>Indice 2</summary>

1 : vérifie les trois conditions, chacune dans $U$ et dans $W$. 4 : suppose $\mathbf{u} + \mathbf{w} \in U$, et exprime $\mathbf{w}$.

</details>
<details><summary>Indice 3</summary>

4 : $\mathbf{w} = (\mathbf{u} + \mathbf{w}) - \mathbf{u}$ serait dans $U$ ; de même avec $W$.

</details>

### Ex M12a.15 — Les coordonnées dans une base sont uniques

<details><summary>Indice 1</summary>

Relis « Indépendance linéaire » (fiche §2) et « Bases » (fiche §3).

</details>
<details><summary>Indice 2</summary>

1 : soustrais les deux écritures. 2 : $\mathbf{0}$ a une écriture évidente.

</details>
<details><summary>Indice 3</summary>

3 : écris $\lambda\mathbf{v} + \mu\mathbf{w}$ comme une combinaison des $\mathbf{b}_i$, puis invoque l'unicité. 4 : la relation de la fiche donne une seconde écriture.

</details>

### Ex M12a.16 — Le noyau est un sous-espace, et une application linéaire est injective si et seulement si son noyau est {0}

<details><summary>Indice 1</summary>

Relis la définition d'une application linéaire (fiche §5) et le §6.

</details>
<details><summary>Indice 2</summary>

1 : $\mathbf{0} = 0 \cdot \mathbf{0}$. 5 : $f(\mathbf{x}) = f(\mathbf{y})$ donne $f(\mathbf{x} - \mathbf{y}) = \mathbf{0}$.

</details>
<details><summary>Indice 3</summary>

6 : au plus $m$ pivots pour $n > m$ colonnes : une variable libre au moins.

</details>

### Ex M12a.17 — Le théorème du rang : dim ker + rang = nombre de colonnes

<details><summary>Indice 1</summary>

Relis « Les calculer par le pivot de Gauss » et « Le théorème du rang » (fiche §6).

</details>
<details><summary>Indice 2</summary>

2 : la ligne $i$ de $\mathbf{R}$ a un 1 dans la colonne de son pivot, des 0 dans les autres colonnes à pivot ; $\mathbf{k}_j$ n'a qu'une coordonnée libre non nulle.

</details>
<details><summary>Indice 3</summary>

4 : les coordonnées libres de $\mathbf{y}$ sont nulles par construction ; la ligne $i$ de $\mathbf{R}\mathbf{y} = \mathbf{0}$ donne alors $y_{p_i} = 0$.

</details>

### Ex M12a.18 — rg(AB) ≤ min(rg A, rg B)

<details><summary>Indice 1</summary>

Relis « Le rang d'un produit » (fiche §4).

</details>
<details><summary>Indice 2</summary>

1 : la colonne $j$ de $\mathbf{A}\mathbf{B}$ est $\mathbf{A}\mathbf{b}_j$. 3 : si $\mathbf{B}\mathbf{x} = \mathbf{0}$, que vaut $\mathbf{A}\mathbf{B}\mathbf{x}$ ?

</details>
<details><summary>Indice 3</summary>

5 : une matrice qui garde l'axe des abscisses, et une qui envoie tout sur l'axe des ordonnées.

</details>

### Ex M12a.19 — L'inverse d'une application affine bijective est affine

<details><summary>Indice 1</summary>

Relis « La transformation inverse » (fiche §8).

</details>
<details><summary>Indice 2</summary>

1 : calcule $\varphi(\mathbf{x}) - \varphi(\mathbf{y})$. 2 : $\varphi(\mathbf{x}) = \mathbf{y}$ s'écrit $\mathbf{A}\mathbf{x} = \mathbf{y} - \mathbf{b}$.

</details>
<details><summary>Indice 3</summary>

5 : $\mathbf{b} = \big(\sum_i \lambda_i\big)\mathbf{b}$ quand $\sum_i \lambda_i = 1$.

</details>

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12a.20 — Pont : une feature somme de deux autres rend XᵀX singulière, et le noyau dit laquelle

<details><summary>Indice 1</summary>

Relis « En machine learning : des poids qui ne servent à rien » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Additionne les deux premières colonnes et compare à la troisième.

</details>
<details><summary>Indice 3</summary>

e) $\mathbf{X}\mathbf{w}' = \mathbf{X}\mathbf{w} + 2\,\mathbf{X}\mathbf{d}$.

</details>

### Ex M12a.21 — Pont : projeter sur un plan puis revenir, ce que la transformation inverse ne peut pas rendre

<details><summary>Indice 1</summary>

Relis « Ce qui ne se défait pas » (fiche §8) et « Le rang d'un produit » (fiche §4).

</details>
<details><summary>Indice 2</summary>

b) Réduis $\mathbf{E}$ : $L_1 \leftarrow L_1 - L_2$. d) Le rang de $\mathbf{D}'\mathbf{E}$ est au plus celui de $\mathbf{E}$.

</details>
<details><summary>Indice 3</summary>

e) $\mathbf{D}$ à gauche : une matrice de forme $(3, 3)$. g) $\mathbf{x}$ moins f).

</details>

### Ex M12a.22 — MML §2.4 et §2.5 : espaces vectoriels, sous-espaces et indépendance, en anglais

<details><summary>Indice 1</summary>

Lis d'abord les définitions encadrées du livre, puis ses exemples.

</details>
<details><summary>Indice 2</summary>

Pour chaque question, cherche le mot anglais correspondant dans le vocabulaire de la fiche (*closure*, *neutral element*, *linearly independent*).

</details>
<details><summary>Indice 3</summary>

5 : « toutes les colonnes à pivot » équivaut à « pas de variable libre dans $\mathbf{V}\boldsymbol{\lambda} = \mathbf{0}$ ».

</details>

### Ex M12a.23 — MML §2.6 à §2.8 : base, rang, applications linéaires, changement de base, espaces affines

<details><summary>Indice 1</summary>

Lis les définitions et les théorèmes encadrés, puis compare-les à la fiche (§3 à §8).

</details>
<details><summary>Indice 2</summary>

4 : le livre écrit $\tilde{\mathbf{A}} = \mathbf{T}^{-1}\mathbf{A}\mathbf{S}$ ; regarde ce que fait $\mathbf{S}$ aux coordonnées.

</details>
<details><summary>Indice 3</summary>

5 : avec la matrice du §4 de la fiche, $\dim\ker = 2$ et le rang vaut 2.

</details>

### Ex M12a.24 — Fermi : les paramètres d'une application linéaire, puis affine, d'images 32 × 32 en couleurs vers 100 classes

<details><summary>Indice 1</summary>

Relis « La matrice d'une application linéaire » (fiche §5) et le théorème du rang (fiche §6).

</details>
<details><summary>Indice 2</summary>

Une application linéaire de $\mathbb{R}^n$ dans $\mathbb{R}^m$ a $mn$ paramètres ; son rang est au plus $\min(m, n)$.

</details>
<details><summary>Indice 3</summary>

5 : $\mathbf{B}$ de forme $(100, 16)$ et $\mathbf{C}$ de forme $(16, 3\,072)$.

</details>

### Ex M12a.25 — Expliquer la dimension et le rang sans une seule formule

<details><summary>Indice 1</summary>

Relis « Dimension » (fiche §3) et « Le rang est une dimension » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Trouve un exemple de la vie courante pour « directions indépendantes », et un exemple de colonne redondante.

</details>
<details><summary>Indice 3</summary>

« Rang 12 » : 12 colonnes bien choisies suffisent à recalculer les autres.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M12a.E1 — « Que veut dire qu'une matrice est de rang plein, et pourquoi s'en soucier ? »

<details><summary>Indice 1</summary>

Relis le §4 et la fin du §6 de la fiche.

</details>
<details><summary>Indice 2</summary>

Deux conséquences : carrée, inversible ; données, $\mathbf{X}^\top\mathbf{X}$ inversible et poids uniques.

</details>
<details><summary>Indice 3</summary>

Ajoute un exemple de feature redondante, et la tolérance du rang numérique.

</details>

### M12a.E2 — « Qu'est-ce que le noyau d'une matrice, et où le croise-t-on en ML ? »

<details><summary>Indice 1</summary>

Relis le §6 et « Ce qui ne se défait pas » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Définition, espace de départ, théorème du rang, non-unicité des solutions.

</details>
<details><summary>Indice 3</summary>

Deux usages : des features redondantes, une réduction de dimension ; et les autres sens du mot « noyau ».

</details>

<a id="notebook"></a>

## Notebook

### Ex M12a.26 — Tester l'indépendance et extraire une base de l'espace des colonnes · `is_independent, column_space_basis`

<details><summary>Indice 1</summary>

Relis ta fonction `rref` de M09a, et « Le test par le pivot de Gauss » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Une fonction privée `_rref(A, tol)` qui rend `(R, pivots)` sert aux deux : libre si chaque colonne a un pivot ; base de l'image = les colonnes de `A` aux indices des pivots.

</details>
<details><summary>Indice 3</summary>

`len(pivots) == A.shape[1]` est un `bool` de Python ; `A[:, list(pivots)]` sur la copie en flottants de `A`.

</details>

### Ex M12a.27 — Une base du noyau, colonne libre par colonne libre · `null_space_basis`

<details><summary>Indice 1</summary>

Relis « Les calculer par le pivot de Gauss » (fiche §6).

</details>
<details><summary>Indice 2</summary>

`free = [j for j in range(n) if j not in pivots]` ; un vecteur par colonne libre, rangé en colonne d'un tableau `np.zeros((n, len(free)))`.

</details>
<details><summary>Indice 3</summary>

Pour la colonne libre `j` (la `c`-ième) : `N[j, c] = 1`, et `N[p, c] = -R[i, j]` pour le pivot `p` de la ligne `i`.

</details>

### Ex M12a.28 — Coordonnées dans une base et changement de base · `coordinates, change_of_basis`

<details><summary>Indice 1</summary>

Relis « Coordonnées dans une base » (fiche §3) et « Entre deux espaces différents » (fiche §7).

</details>
<details><summary>Indice 2</summary>

`np.linalg.solve(B.T @ B, B.T @ v)`, puis la vérification relative ; `np.linalg.solve(T, A @ S)`.

</details>
<details><summary>Indice 3</summary>

Teste `is_independent(S)` **et** `is_independent(T)` avant de résoudre : `solve(T, ...)` ne voit pas une `S` singulière.

</details>

### Ex M12a.29 — `sympy.Matrix.nullspace`, `columnspace` et `rank` contre tes fonctions

<details><summary>Indice 1</summary>

Relis la section « En pratique » de l'énoncé.

</details>
<details><summary>Indice 2</summary>

`P = sympy.Matrix(...)`, puis `P.rank()`, `P.nullspace()`, `P.columnspace()`.

</details>
<details><summary>Indice 3</summary>

d) `sympy.Matrix.hstack(*P.columnspace()).tolist()`. e) `np.allclose` entre ton résultat et `np.array(sympy.Matrix.hstack(*P.nullspace()).tolist(), dtype=float)`.

</details>

### Ex M12a.30 — Prédire le rang : matrices aléatoires, produits, colonnes répétées

<details><summary>Indice 1</summary>

Relis « Le rang d'un produit » et « Un tableau centré perd un rang » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Une matrice tirée au hasard est de rang plein ; un produit ne crée pas de direction ; une colonne ajoutée qui en combine d'autres non plus.

</details>
<details><summary>Indice 3</summary>

e) Écris la ligne $i$ comme une combinaison de $(1, \ldots, 1)$ et de $(1, 2, \ldots, 6)$.

</details>

### Ex M12a.31 — Le rang numérique : une colonne presque redondante et le choix de la tolérance

<details><summary>Indice 1</summary>

Relis « Le rang numérique » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Une boucle sur `KS_31` ; deux listes, `np.linalg.matrix_rank(X)` et `column_space_basis(X, tol=tol).shape[1]`.

</details>
<details><summary>Indice 3</summary>

Lis le **premier** $k$ où le rang tombe à 2, dans la bonne ligne du bon réglage.

</details>

### Ex M12a.32 — Une application linéaire du plan : l'image du carré unité, et ce qu'elle écrase quand son noyau n'est pas nul

<details><summary>Indice 1</summary>

Relis M09a.33 et la figure du §6 de la fiche.

</details>
<details><summary>Indice 2</summary>

Les sommets du carré, transformés : `np.array([[0, 0], [1, 0], [1, 1], [0, 1]]) @ M.T`. Le noyau : `null_space_basis(M)` ; s'il n'a pas de colonne, arrête-toi après le carré.

</details>
<details><summary>Indice 3</summary>

L'image : une colonne non nulle de `M` ; les segments : `p + t k` pour $t$ entre $-1$ et 1, et le point `M @ p`.

</details>

### Ex M12a.33 — Chasse à l'erreur : une « base » liée, un noyau faux, S⁻¹AS écrit à l'envers

<details><summary>Indice 1</summary>

Relis les erreurs classiques des §2, §6 et §7 de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, calcule à la main ce que dit son commentaire, puis ce que fait le code.

</details>
<details><summary>Indice 3</summary>

(A) $\mathbf{u} + \mathbf{v}$ est-il hors du plan de $\mathbf{u}$ et $\mathbf{v}$ ? (B) Le signe de $-R_{ij}$. (D) L'ordre des facteurs.

</details>

### Ex M12a.34 — Un test de propriété : A fois une base du noyau donne 0, et le théorème du rang sur des matrices aléatoires

<details><summary>Indice 1</summary>

Relis le théorème du rang (fiche §6) et M09a.35.

</details>
<details><summary>Indice 2</summary>

Trois `assert` : `np.allclose(A @ N, 0)`, `N.shape[1] + Q.shape[1] == n`, et l'indépendance des colonnes de `N`.

</details>
<details><summary>Indice 3</summary>

`matrix_rank` refuse un tableau sans colonne : teste `N.shape[1] == 0 or ...`. Tire des rangs variés, jusqu'à 0.

</details>

### Ex M12a.35 — Défi : retrouver les relations linéaires exactes cachées entre les colonnes d'un tableau, sans en inventer

<details><summary>Indice 1</summary>

Relis M12a.31 : une tolérance absolue dépend de l'échelle des nombres.

</details>
<details><summary>Indice 2</summary>

Divise chaque colonne par sa norme (sans centrer), puis cherche le noyau avec une tolérance entre les arrondis et le bruit.

</details>
<details><summary>Indice 3</summary>

`Y = null_space_basis(X / norms, tol=1e-9)`, puis `Y / norms[:, None]` pour revenir aux colonnes de départ.

</details>
