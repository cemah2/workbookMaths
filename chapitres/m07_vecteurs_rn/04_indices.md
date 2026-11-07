# M07 · Vecteurs et géométrie de ℝⁿ — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M07.Q1 — Vecteurs, coordonnées et one-hot

<details><summary>Indice 1</summary>

Relis « Des listes de nombres », « Opérer coordonnée par coordonnée » et « La base canonique et les vecteurs one-hot » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Un exemple décrit par $n$ nombres est un vecteur de $\mathbb{R}^n$ ; on additionne et on multiplie par un nombre coordonnée par coordonnée ; un vecteur one-hot a un seul 1, à la place de sa catégorie.

</details>
<details><summary>Indice 3</summary>

3 : calcule d'abord $2\,(1, 0, -3)$. 6 : les coefficients devant $\mathbf{e}_1$, $\mathbf{e}_2$, $\mathbf{e}_3$ sont les coordonnées elles-mêmes.

</details>

### M07.Q2 — Ce que mesure un produit scalaire

<details><summary>Indice 1</summary>

Relis « Définition » et « Le neurone : un produit scalaire plus un biais » (fiche §2).

</details>
<details><summary>Indice 2</summary>

$\mathbf{u} \cdot \mathbf{v} = \sum_i u_i v_i$ est un nombre ; $\mathbf{u} \cdot \mathbf{u} = \sum_i u_i^2$ ; le produit scalaire est linéaire par rapport à chaque vecteur.

</details>
<details><summary>Indice 3</summary>

3 : une somme de carrés n'est nulle que si chaque carré l'est. 4 : $\mathbf{e}_2 = (0, 1, 0)$. 6 : $z = \mathbf{w} \cdot \mathbf{x} + b$.

</details>

### M07.Q3 — Trois normes, trois boules unités

<details><summary>Indice 1</summary>

Relis « Trois façons de mesurer une longueur », « Ce qu'est une norme » et « Boules unités » (fiche §3).

</details>
<details><summary>Indice 2</summary>

L1 : la somme des valeurs absolues ; L2 : la racine de la somme des carrés ; L∞ : la plus grande valeur absolue. Une norme est positive, homogène, et vérifie l'inégalité triangulaire.

</details>
<details><summary>Indice 3</summary>

2 : cherche les points $(x_1, x_2)$ tels que $|x_1| + |x_2| = 1$ (quatre segments), puis tels que $\max(|x_1|, |x_2|) = 1$. 6 : essaie $\mathbf{e}_1$, $\mathbf{e}_2$ et $\mathbf{e}_1 + \mathbf{e}_2$.

</details>

### M07.Q4 — Similarité cosinus : vrai ou faux

<details><summary>Indice 1</summary>

Relis « L'inégalité de Cauchy-Schwarz » et « Angle et similarité cosinus » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert}$ ; regarde ce que devient chaque morceau quand on multiplie $\mathbf{u}$ par un nombre $\lambda$, positif ou négatif.

</details>
<details><summary>Indice 3</summary>

2 : $\lVert -10\,\mathbf{u} \rVert = 10\,\lVert \mathbf{u} \rVert$, mais le produit scalaire change de signe. 6 : compare $\mathbf{u}$ et $2\mathbf{u}$.

</details>

### M07.Q5 — Hyperplans : vecteur normal et côtés

<details><summary>Indice 1</summary>

Relis « Une équation, une frontière », « Deux demi-espaces » et « La distance à un hyperplan » (fiche §5).

</details>
<details><summary>Indice 2</summary>

L'hyperplan $\mathbf{w} \cdot \mathbf{x} + b = 0$ a pour vecteur normal $\mathbf{w}$, lu sur les coefficients ; le côté d'un point est le signe de $\mathbf{w} \cdot \mathbf{x} + b$.

</details>
<details><summary>Indice 3</summary>

3 : remplace $\mathbf{x}$ par $(0, 0, 0)$. 5 : calcule $2x_1 - x_2 + 5x_3 - 7$ en chacun des deux points, et compare les signes. 6 : la formule de la distance en $\mathbf{x} = \mathbf{0}$.

</details>

### M07.Q6 — Moyenne, barycentre et inertie

<details><summary>Indice 1</summary>

Relis la fiche §6, de « Le barycentre d'un nuage de points » à « Bien partir : k-means++ ».

</details>
<details><summary>Indice 2</summary>

Le barycentre est la moyenne coordonnée par coordonnée ; il minimise l'inertie ; k-means alterne affectation et mise à jour ; une silhouette compare $a(i)$ et $b(i)$.

</details>
<details><summary>Indice 3</summary>

5 : une silhouette négative veut dire $b(i) < a(i)$. 6 : multiplie chaque point par son poids, additionne, puis divise par la somme des poids.

</details>

### M07.Q7 — Intuitions de la grande dimension

<details><summary>Indice 1</summary>

Relis la fiche §7.

</details>
<details><summary>Indice 2</summary>

La diagonale du cube unité de $\mathbb{R}^n$ mesure $\sqrt{n}$ ; son cosinus avec un axe vaut $\frac{1}{\sqrt{n}}$ ; deux directions au hasard ont un cosinus de l'ordre de $\frac{1}{\sqrt{n}}$.

</details>
<details><summary>Indice 3</summary>

3 : $\frac{1}{\sqrt{10\,000}}$. 4 : $\mathbb{E}\big[\lVert \mathbf{X} \rVert^2\big] = \sum_i \mathbb{E}[X_i^2]$. 5 : pour que $\frac{1}{\sqrt{n}}$ soit 10 fois plus petit, par combien faut-il multiplier $\sqrt{n}$ ? 6 : la norme au carré est la somme des $n$ carrés des coordonnées.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M07.R1 — Produit scalaire et angle dans le plan (R9)

<details><summary>Indice 1</summary>

Relis R9 (produit scalaire dans le plan, angle, vecteur unitaire).

</details>
<details><summary>Indice 2</summary>

$(x ; y) \cdot (x' ; y') = xx' + yy'$, $\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert}$, et le vecteur unitaire de même sens que $\mathbf{u}$ est $\frac{\mathbf{u}}{\lVert \mathbf{u} \rVert}$.

</details>
<details><summary>Indice 3</summary>

2 : $\cos\theta = -\frac{1}{2}$. 3 : échange les coordonnées et change un signe. 4 : $\sqrt{25 + 144}$.

</details>

### M07.R2 — Moyenne et variance empiriques (M02c)

<details><summary>Indice 1</summary>

Relis M02c (moyenne, variance, $\mathrm{ddof}$).

</details>
<details><summary>Indice 2</summary>

La variance est la moyenne des carrés des écarts à la moyenne ($\mathrm{ddof} = 0$), ou leur somme divisée par $n - 1$ ($\mathrm{ddof} = 1$).

</details>
<details><summary>Indice 3</summary>

Les écarts à la moyenne sont $-4, -1, -1, 2, 4$. 5 : dérive $\sum_i (x_i - c)^2$ par rapport à $c$.

</details>

### M07.R3 — Gradient et point critique (M05b)

<details><summary>Indice 1</summary>

Relis M05b (dérivées partielles, point critique, test des dérivées secondes).

</details>
<details><summary>Indice 2</summary>

Dérive chaque carré : la dérivée de $(c_1 - a)^2$ par rapport à $c_1$ est $2(c_1 - a)$. Un point critique annule toutes les dérivées partielles.

</details>
<details><summary>Indice 3</summary>

3 : $f_{c_1 c_1} = 4$, $f_{c_2 c_2} = 4$, $f_{c_1 c_2} = 0$. 4 : écris $f(\mathbf{c})$ comme une somme de deux carrés de distances.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M07.1 — Combinaisons linéaires et vecteurs one-hot dans ℝ⁴

<details><summary>Indice 1</summary>

Relis « Opérer coordonnée par coordonnée » et « La base canonique et les vecteurs one-hot » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Calcule coordonnée par coordonnée. Pour d), écris une équation par coordonnée : $a + 3b = 5$, etc.

</details>
<details><summary>Indice 3</summary>

d) La troisième équation, $-b = -1$, donne $b$ tout de suite ; utilise la première pour $a$, et les deux autres pour vérifier. f) Chaque trajet ajoute un 1 à la place de son mode. g) Divise par 10.

</details>

### Ex M07.2 — Produits scalaires, ‖u + v‖² et l'identité du parallélogramme

<details><summary>Indice 1</summary>

Relis « Définition » et « Développer une norme au carré » (fiche §2).

</details>
<details><summary>Indice 2</summary>

$\lVert \mathbf{u} + \mathbf{v} \rVert^2 = \lVert \mathbf{u} \rVert^2 + 2\,\mathbf{u} \cdot \mathbf{v} + \lVert \mathbf{v} \rVert^2$, et avec un signe moins pour $\lVert \mathbf{u} - \mathbf{v} \rVert^2$.

</details>
<details><summary>Indice 3</summary>

d) Développe $(\mathbf{u} - 2\mathbf{v}) \cdot (\mathbf{u} - 2\mathbf{v})$ par linéarité : quatre termes, dont deux égaux. e) Écris $(\mathbf{u} + t\,\mathbf{v}) \cdot \mathbf{v} = 0$ et développe. f) Soustrais les deux développements : il reste $4\,\mathbf{a} \cdot \mathbf{b}$. g) L'égalité dit seulement $\mathbf{u} \cdot (\mathbf{v} - \mathbf{w}) = 0$.

</details>

### Ex M07.3 — Normes L1, L2, L∞ et distances entre trois profils

<details><summary>Indice 1</summary>

Relis « Trois façons de mesurer une longueur » et « Distances » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Une distance est la norme de la différence : calcule d'abord $R - P$, $R - Q$ et $Q - P$, puis leurs trois normes.

</details>
<details><summary>Indice 3</summary>

$R - P = (1, -1, 1, -1)$ et $Q - P = (0, -3, 0, 0)$. f) Divise $P$ par $\lVert P \rVert_2$. g) $d_2(P, R) + d_2(R, Q)$.

</details>

### Ex M07.4 — Similarité cosinus entre des profils d'écoute musicale

<details><summary>Indice 1</summary>

Relis « Angle et similarité cosinus » (fiche §4) et « Distances » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\cos = \frac{A \cdot C}{\lVert A \rVert\,\lVert C \rVert}$ ; l'angle est son arccosinus, en degrés. Regarde bien $E$ : que vaut $E$ en fonction de $A$ ?

</details>
<details><summary>Indice 3</summary>

$\lVert A \rVert = 6$, $\lVert C \rVert = 5$, $A \cdot C = 16$. $E = 2A$ : le cosinus vaut 1 et $E - A = A$.

</details>

### Ex M07.5 — Projeter sur une droite : composante parallèle et composante orthogonale

<details><summary>Indice 1</summary>

Relis « Projeter sur une droite » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$\mathbf{p} = t\,\mathbf{u}$ avec $t = \frac{\mathbf{x} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}$ ; le reste $\mathbf{r} = \mathbf{x} - \mathbf{p}$ est orthogonal à $\mathbf{u}$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{x} \cdot \mathbf{u} = 18$, $\mathbf{u} \cdot \mathbf{u} = 9$. g) Remplace $\mathbf{u}$ par $-3\mathbf{u}$ dans la formule : le facteur apparaît deux fois en haut et deux fois en bas. h) Divise par $\lVert \mathbf{u} \rVert = 3$, pas par $9$.

</details>

### Ex M07.6 — Un plan de ℝ³ : vecteur normal, côté, distance signée

<details><summary>Indice 1</summary>

Relis la fiche §5 (« Une équation, une frontière », « Deux demi-espaces », « La distance à un hyperplan »).

</details>
<details><summary>Indice 2</summary>

Le vecteur normal se lit sur les coefficients de $x$, $y$, $z$ ; la distance signée est $\frac{\mathbf{w} \cdot \mathbf{x} + b}{\lVert \mathbf{w} \rVert}$, avec $\lVert \mathbf{w} \rVert = 3$.

</details>
<details><summary>Indice 3</summary>

En $B$, l'expression vaut 3. g) Pars de $B$ et recule de $\frac{3}{\lVert \mathbf{w} \rVert^2}\,\mathbf{w}$ (le point $\mathbf{x}_H$ de M07.17). h) Écris que $B$ vérifie la nouvelle équation.

</details>

### Ex M07.7 — Un score linéaire w · x + b : calculer, décider, lire le vecteur normal

<details><summary>Indice 1</summary>

Relis « Le neurone : un produit scalaire plus un biais » (fiche §2) et « Frontières de décision linéaires » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Le score est $\mathbf{w} \cdot \mathbf{x} + b$ ; le score augmente le plus vite dans la direction de $\mathbf{w}$ ; la distance à la frontière est $\frac{|z|}{\lVert \mathbf{w} \rVert}$.

</details>
<details><summary>Indice 3</summary>

N'oublie pas le biais $-2$. e) Le score change de $w_2 \times 0{,}5$. f) $\lVert \mathbf{w} \rVert = \sqrt{6{,}5}$.

</details>

### Ex M07.8 — Centroïde, inertie et formule de König-Huygens

<details><summary>Indice 1</summary>

Relis « Le barycentre d'un nuage de points » et « La moyenne minimise la somme des carrés des distances » (fiche §6).

</details>
<details><summary>Indice 2</summary>

König-Huygens : $\sum_i \lVert \mathbf{x}_i - \mathbf{c} \rVert^2 = \sum_i \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert^2 + m\,\lVert \bar{\mathbf{x}} - \mathbf{c} \rVert^2$.

</details>
<details><summary>Indice 3</summary>

Le barycentre est $(2, 1)$ et l'inertie autour de lui vaut 20. g) Les cinq anciens points, autour du nouveau barycentre $(3, 2)$ : $20 + 5\,\lVert (2, 1) - (3, 2) \rVert^2$ ; ajoute le carré de la distance du sixième point.

</details>

### Ex M07.9 — Où placer un dépôt : le barycentre pondéré des livraisons

<details><summary>Indice 1</summary>

Relis « Le barycentre d'un nuage de points » (fiche §6), et la formule pondérée de M07.16.

</details>
<details><summary>Indice 2</summary>

Le barycentre pondéré est $\frac{\sum_i \omega_i S_i}{\sum_i \omega_i}$ ; avec des poids, König-Huygens s'écrit avec $\Omega = \sum_i \omega_i$ devant le dernier terme.

</details>
<details><summary>Indice 3</summary>

b) $\frac{(10, 8)}{6}$. c) Calcule les trois carrés de distances au barycentre pondéré (des neuvièmes), puis leur somme pondérée. d) Le barycentre non pondéré est à la distance 1 du barycentre pondéré.

</details>

### Ex M07.10 — La silhouette d'un point, à la main, en dimension 2

<details><summary>Indice 1</summary>

Relis « Juger un découpage : la silhouette » (fiche §6).

</details>
<details><summary>Indice 2</summary>

$a(i)$ : la distance moyenne aux **autres** points de son cluster ; $b(i)$ : la distance moyenne aux points de l'autre cluster ; $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$.

</details>
<details><summary>Indice 3</summary>

Écris d'abord les dix distances : $AB = 2$, $AC = \sqrt{5}$, $AD = \sqrt{37}$, $AF = \sqrt{58}$, $BD = \sqrt{17}$, $BF = \sqrt{34}$, $CD = \sqrt{26}$, $DF = \sqrt{5}$… e) Dans le second cluster, $B$ a pour voisins $D$ et $F$.

</details>

### Ex M07.11 — k-means++ : des probabilités de tirage proportionnelles à D²

<details><summary>Indice 1</summary>

Relis « Bien partir : k-means++ » (fiche §6).

</details>
<details><summary>Indice 2</summary>

La probabilité de tirer un point est son $D^2$ divisé par la somme des $D^2$ ; $D$ est la distance au centre **le plus proche** déjà choisi.

</details>
<details><summary>Indice 3</summary>

a) $D^2$ de $P_4$ : $4^2 + 2^2$. d) Pour chaque point, le plus petit des deux carrés de distances, à $P_1$ et à $P_5$. f) Quatre candidats, autant de chances chacun.

</details>

### Ex M07.12 — La diagonale du cube unité et son angle avec les axes, quand d grandit

<details><summary>Indice 1</summary>

Relis « La diagonale du cube » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\lVert \mathbf{1} \rVert = \sqrt{d}$ et $\mathbf{1} \cdot \mathbf{e}_1 = 1$, donc $\cos\theta = \frac{1}{\sqrt{d}}$.

</details>
<details><summary>Indice 3</summary>

e) Résous $\frac{1}{\sqrt{d}} < \cos 80°$, puis vérifie $d$ et $d - 1$. f) Le produit scalaire vaut $(d - 1) - 1$, et les deux normes valent $\sqrt{d}$.

</details>

### Ex M07.13 — La norme d'un vecteur gaussien : espérance, variance et concentration

<details><summary>Indice 1</summary>

Relis « La norme d'un vecteur gaussien » (fiche §7), M02c §9 (le même calcul, avec $\mathbb{V}(Z^2) = 2$ admis), M02a (intégration par parties) et M02b (variance d'une somme de variables indépendantes).

</details>
<details><summary>Indice 2</summary>

a) Par parties, avec $u = z^3$ et $v' = z\,\varphi(z)$, donc $v = -\varphi(z)$. b) $\mathbb{V}(Z^2) = \mathbb{E}[Z^4] - \mathbb{E}[Z^2]^2$. c) et d) $X_i^2 = 9Z_i^2$ : son espérance est 9 fois celle de $Z^2$, sa variance 81 fois celle de $Z^2$.

</details>
<details><summary>Indice 3</summary>

d) $n$ fois la variance de $X_i^2$. e) La racine de d), divisée par c). f) $P(|Y - \mathbb{E}[Y]| \ge \varepsilon) \le \frac{\mathbb{V}(Y)}{\varepsilon^2}$, avec $\varepsilon$ égal au dixième de l'espérance.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M07.14 — L'inégalité de Cauchy-Schwarz, par le discriminant

<details><summary>Indice 1</summary>

Relis « L'inégalité de Cauchy-Schwarz » (fiche §4), et R3 (signe d'un trinôme).

</details>
<details><summary>Indice 2</summary>

$q(t) = (\mathbf{u} + t\mathbf{v}) \cdot (\mathbf{u} + t\mathbf{v})$ se développe par linéarité. Un trinôme de coefficient dominant positif qui ne prend jamais de valeur négative a un discriminant négatif ou nul.

</details>
<details><summary>Indice 3</summary>

4 : si $\Delta = 0$, la racine double $t_0$ vérifie $\lVert \mathbf{u} + t_0 \mathbf{v} \rVert^2 = 0$, donc $\mathbf{u} + t_0\mathbf{v} = \mathbf{0}$. 5 : $\mathbf{u} \cdot \mathbf{v} = \sum_i |x_i|$, $\lVert \mathbf{v} \rVert = \sqrt{n}$.

</details>

### Ex M07.15 — L'inégalité triangulaire pour L2, L1 et L∞

<details><summary>Indice 1</summary>

Relis « Ce qu'est une norme » (fiche §3) et M07.14.

</details>
<details><summary>Indice 2</summary>

1 : majore $\mathbf{u} \cdot \mathbf{v}$ par $\lVert \mathbf{u} \rVert_2\,\lVert \mathbf{v} \rVert_2$ dans le développement, puis reconnais un carré. 2 et 3 : travaille coordonnée par coordonnée.

</details>
<details><summary>Indice 3</summary>

3 : majore chaque $|u_i + v_i|$ par $\lVert \mathbf{u} \rVert_\infty + \lVert \mathbf{v} \rVert_\infty$ avant de prendre le maximum. 4 : applique 1 à $(\mathbf{u} - \mathbf{v}) + \mathbf{v}$, puis échange $\mathbf{u}$ et $\mathbf{v}$. 5 : $N(\mathbf{e}_1 + \mathbf{e}_2)$.

</details>

### Ex M07.16 — La moyenne minimise la somme des carrés des distances, en dimension n

<details><summary>Indice 1</summary>

Relis « La moyenne minimise la somme des carrés des distances » (fiche §6) et « Développer une norme au carré » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Développe $\lVert (\mathbf{x}_i - \bar{\mathbf{x}}) + (\bar{\mathbf{x}} - \mathbf{c}) \rVert^2$ et somme sur $i$ : le double produit fait apparaître $\sum_i (\mathbf{x}_i - \bar{\mathbf{x}})$.

</details>
<details><summary>Indice 3</summary>

3 : seul le terme $m\,\lVert \bar{\mathbf{x}} - \mathbf{c} \rVert^2$ dépend de $\mathbf{c}$. 4 : $\sum_i \omega_i (\mathbf{x}_i - \bar{\mathbf{x}}_\omega) = \mathbf{0}$. 5 : $J(\mathbf{c}) = \sum_i \sum_j (x_{ij} - c_j)^2$, dérive par rapport à $c_j$.

</details>

### Ex M07.17 — La distance d'un point à un hyperplan vaut |w · x + b| / ‖w‖

<details><summary>Indice 1</summary>

Relis « La distance à un hyperplan » (fiche §5) et « Orthogonalité » (fiche §2).

</details>
<details><summary>Indice 2</summary>

1 : écris que $\mathbf{x}_0 - t\,\mathbf{w}$ vérifie l'équation de $H$, et isole $t$. 3 : deux points de $H$ ont la même valeur de $\mathbf{w} \cdot \mathbf{x}$.

</details>
<details><summary>Indice 3</summary>

3 : $\mathbf{x}_0 - \mathbf{y} = (\mathbf{x}_0 - \mathbf{x}_H) + (\mathbf{x}_H - \mathbf{y})$, avec $\mathbf{x}_0 - \mathbf{x}_H$ parallèle à $\mathbf{w}$ : Pythagore. 5 : prends un point $\mathbf{x}_0$ du premier hyperplan, il vérifie $\mathbf{w} \cdot \mathbf{x}_0 = -b_1$.

</details>

### Ex M07.18 — Les deux étapes de k-means font baisser l'inertie, ou la laissent égale

<details><summary>Indice 1</summary>

Relis « k-means : le principe » (fiche §6) et M07.16.

</details>
<details><summary>Indice 2</summary>

1 : chaque terme de $J$ ne dépend que du cluster de son point. 2 : regroupe les termes par cluster ; chaque centre n'apparaît que dans la somme de son cluster.

</details>
<details><summary>Indice 3</summary>

3 : après une mise à jour, l'inertie ne dépend que de l'affectation ; une affectation qui change fait baisser strictement l'inertie ; il y a au plus $k^m$ affectations. 4 : calcule les distances au carré de $(0, 0)$ aux deux centres : $6{,}25$ et $7{,}25$.

</details>

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M07.19 — Pont : changer l'unité d'une feature change le plus proche voisin

<details><summary>Indice 1</summary>

Relis « Distances » (fiche §3), et la standardisation de M02c.

</details>
<details><summary>Indice 2</summary>

Écris les écarts de puissance et de masse entre $q$ et chaque voiture, dans l'unité demandée, puis la distance euclidienne.

</details>
<details><summary>Indice 3</summary>

En kilogrammes, l'écart de masse avec $A$ vaut 700. e) Divise chaque écart par l'écart-type de sa feature **avant** d'élever au carré : $\big(\frac{10}{20}, \frac{0{,}7}{0{,}25}\big)$ pour $A$.

</details>

### Ex M07.20 — MML §3.1 et §3.2.1 : normes et produit scalaire, en anglais

<details><summary>Indice 1</summary>

Lis MML §3.1 en entier, puis §3.2.1 ; garde la fiche §2 et §3 ouverte à côté.

</details>
<details><summary>Indice 2</summary>

Le livre appelle les deux normes par des noms de lieux ou de savants ; la fiche les appelle L1 et L2.

</details>
<details><summary>Indice 3</summary>

3 : une norme plus grande, pour un même vecteur, demande des vecteurs plus courts pour valoir 1 : sa boule unité est plus petite. 4 : le livre écrit le produit scalaire usuel avec une transposée.

</details>

### Ex M07.21 — MML §3.3 et §3.4 : longueurs, distances, angles et orthogonalité

<details><summary>Indice 1</summary>

Lis MML §3.3, puis §3.4 ; garde la fiche §3 et §4 ouverte.

</details>
<details><summary>Indice 2</summary>

Longueur : la racine du produit scalaire d'un vecteur avec lui-même ; distance : la longueur de la différence. Le cosinus de l'angle est bien défini grâce à Cauchy-Schwarz.

</details>
<details><summary>Indice 3</summary>

3 : produit scalaire 4, normes 3 et 3. 5 : avec le second produit scalaire, calcule $\langle \mathbf{x}, \mathbf{y} \rangle$, $\langle \mathbf{x}, \mathbf{x} \rangle$ et $\langle \mathbf{y}, \mathbf{y} \rangle$ avant le cosinus.

</details>

### Ex M07.22 — Fermi : la mémoire d'un million d'embeddings

<details><summary>Indice 1</summary>

Relis l'énoncé : il donne la taille d'un nombre (4 octets en `float32`) et la vitesse de l'ordinateur. Écris chaque produit avec des puissances de 10.

</details>
<details><summary>Indice 2</summary>

Mémoire : nombre de vecteurs × nombre de coordonnées × octets par nombre ; un produit scalaire dans $\mathbb{R}^{768}$ coûte 768 multiplications.

</details>
<details><summary>Indice 3</summary>

$10^6 \times 768 \approx 8 \times 10^8$ nombres. Temps : divise le nombre de multiplications par $10^{10}$. 4 : combien coûte le calcul d'une norme ?

</details>

### Ex M07.23 — Expliquer la similarité cosinus à quelqu'un qui a fait le lycée

<details><summary>Indice 1</summary>

Relis « Angle et similarité cosinus » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Une flèche par profil, une direction par genre ; la longueur de la flèche, c'est le temps d'écoute.

</details>
<details><summary>Indice 3</summary>

Le cosinus mesure l'écart entre les directions des deux flèches, pas leurs longueurs ; dis ce que valent les cas « alignées » et « à angle droit ».

</details>

<a id="entretien"></a>

## 💼 Entretien

### M07.E1 — Que représente géométriquement le vecteur de poids d'un modèle linéaire ?

<details><summary>Indice 1</summary>

Relis « Frontières de décision linéaires » et « La distance à un hyperplan » (fiche §5).

</details>
<details><summary>Indice 2</summary>

La frontière est l'hyperplan $\mathbf{w} \cdot \mathbf{x} + b = 0$ : quel est son vecteur normal ? Et quel est le gradient du score $\mathbf{w} \cdot \mathbf{x} + b$ (M05b) ?

</details>
<details><summary>Indice 3</summary>

Pars d'un point $\mathbf{x}_0$ de la frontière et avance de $\delta\,\frac{\mathbf{w}}{\lVert \mathbf{w} \rVert}$ : calcule le nouveau score. Que relie-t-il, la distance à la frontière et $\lVert \mathbf{w} \rVert$ ?

</details>

<a id="notebook"></a>

## Notebook

### Ex M07.24 — Normes Lp et similarité cosinus · `norm_p, cosine_similarity`

<details><summary>Indice 1</summary>

Relis la fiche §3 et §4, et la docstring du module `vectors.py`.

</details>
<details><summary>Indice 2</summary>

`x = np.array(x, dtype=float)` ; les vérifications d'abord (une dimension, non vide, `not p >= 1`) ; puis trois cas : $p$ infini (`math.isinf`), $p = 1$, et le cas général.

</details>
<details><summary>Indice 3</summary>

Cas général : `float(np.sum(np.abs(x) ** p) ** (1 / p))`. Cosinus : les deux normes, une `ValueError` si l'une est nulle, puis `float(np.clip(np.sum(u * v) / (nu * nv), -1.0, 1.0))`.

</details>

### Ex M07.25 — La projection sur une droite · `project_onto_line`

<details><summary>Indice 1</summary>

Relis « Projeter sur une droite » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Les deux vecteurs en flottants, une `ValueError` si leurs longueurs diffèrent ou si $\mathbf{u} \cdot \mathbf{u} = 0$.

</details>
<details><summary>Indice 3</summary>

`(np.sum(x * u) / np.sum(u * u)) * u` : un tableau NumPy, sans racine carrée.

</details>

### Ex M07.26 — Barycentre et somme des carrés des distances · `centroid, sum_sq_distances_to`

<details><summary>Indice 1</summary>

Relis « Le barycentre d'un nuage de points » (fiche §6).

</details>
<details><summary>Indice 2</summary>

`points` en tableau 2-D ; poids égaux à 1 par défaut ; vérifie leur forme, leur signe (`np.all(w >= 0)`) et leur somme.

</details>
<details><summary>Indice 3</summary>

`np.sum(w[:, None] * points, axis=0) / w.sum()` ; pour l'inertie, `float(np.sum((points - c) ** 2))`, après avoir vérifié que `c` a une coordonnée par colonne.

</details>

### Ex M07.27 — Côté d'un hyperplan et distance à un hyperplan · `side_of_hyperplane, distance_to_hyperplane`

<details><summary>Indice 1</summary>

Relis la fiche §5, et le conseil de l'énoncé sur `axis=-1`.

</details>
<details><summary>Indice 2</summary>

Écris une petite fonction qui calcule les scores `np.sum(x * w, axis=-1) + b`, après avoir vérifié `w` (non nul) et `x.shape[-1] == w.size`.

</details>
<details><summary>Indice 3</summary>

Côté : `np.sign(scores).astype(int)`, puis `int(...)` si `x` est à une dimension. Distance : `scores / np.sqrt(np.sum(w * w))`, `np.abs` sauf si `signed`, puis `float(...)` pour un point.

</details>

### Ex M07.28 — `np.linalg.norm` (ord = 1, 2, inf) et `scipy.spatial.distance` contre tes fonctions

<details><summary>Indice 1</summary>

Relis l'énoncé : il donne le nom de chaque fonction.

</details>
<details><summary>Indice 2</summary>

`spd.cityblock`, `spd.chebyshev`, `spd.euclidean` et `spd.cosine` prennent les deux vecteurs ; `spd.cosine` renvoie $1 - \cos\theta$.

</details>
<details><summary>Indice 3</summary>

f) Une boucle sur 20 vecteurs `rng.normal(size=...)` et sur `[1, 2, 3, np.inf]`, avec `np.isclose(mymath.vectors.norm_p(x, p), np.linalg.norm(x, ord=p), rtol=0, atol=1e-12)` ; `all(...)` du tout.

</details>

### Ex M07.29 — Prédire : l'angle de deux vecteurs tirés au hasard en dimension 1 000

<details><summary>Indice 1</summary>

Relis « Deux directions au hasard sont presque orthogonales » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Le cosinus de deux directions au hasard est une somme de $d$ petits termes de signes variés, divisée par environ $d$ : il est de l'ordre de $\frac{1}{\sqrt{d}}$.

</details>
<details><summary>Indice 3</summary>

En dimension 1 000, $\frac{1}{\sqrt{1000}} \approx 0{,}03$ radian, soit environ 2° d'écart à 90°. En dimension 2, une direction au hasard est un angle uniforme sur le cercle.

</details>

### Ex M07.30 — La norme d'un vecteur gaussien se concentre autour de √d

<details><summary>Indice 1</summary>

Relis « La norme d'un vecteur gaussien » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Les normes de toutes les lignes : `np.sqrt(np.sum(X ** 2, axis=1))` ; `X.shape[1]` est la dimension.

</details>
<details><summary>Indice 3</summary>

Renvoie `(float(norms.mean() / math.sqrt(d)), float(norms.std()))`. La pente se lit sur `np.polyfit(np.log(dims), np.log(stds / np.sqrt(dims)), 1)[0]`.

</details>

### Ex M07.31 — Médiane ou moyenne : le centre qui minimise les distances L1 ou leurs carrés, face à des points aberrants

<details><summary>Indice 1</summary>

Relis l'énoncé (la somme des distances L1 se découpe coordonnée par coordonnée) et la fiche §6.

</details>
<details><summary>Indice 2</summary>

La médiane d'une colonne se calcule avec `np.median(..., axis=0)` ; le coût L1 est la somme de toutes les valeurs absolues des écarts.

</details>
<details><summary>Indice 3</summary>

`l1_center` : `np.median(np.asarray(points, dtype=float), axis=0)`. `l1_cost` : `float(np.sum(np.abs(points - c)))`. g) Le coût L1 au barycentre divisé par le coût L1 à la médiane.

</details>

### Ex M07.32 — Les boules unités L1, L2, L∞ et Lp dans le plan

<details><summary>Indice 1</summary>

Relis « Boules unités » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Des directions `np.column_stack([np.cos(t), np.sin(t)])`, divisées chacune par sa norme $L^p$ : le point obtenu a la norme 1.

</details>
<details><summary>Indice 3</summary>

`t = np.linspace(0, 2 * np.pi, 401)` ferme la courbe ; norme des lignes : `np.sum(np.abs(D) ** p, axis=1) ** (1 / p)`, ou `np.max(np.abs(D), axis=1)` pour L∞ ; `ax.plot(xs, ys, **style)`.

</details>

### Ex M07.33 — Chasse à l'erreur : une distance sans racine, un cosinus mal normalisé, une projection sur un vecteur non unitaire

<details><summary>Indice 1</summary>

Relis le tableau des pièges classiques de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, compare la formule écrite à celle de la fiche : une racine qui manque, une norme qui manque, un carré de trop.

</details>
<details><summary>Indice 3</summary>

$\mathbf{a} - \mathbf{b} = (-3, 4, -4)$, $\mathbf{a} \cdot \mathbf{b} = -3$, $\lVert \mathbf{a} \rVert^2 = 14$, $\lVert \mathbf{b} \rVert^2 = 21$. Une composante se divise par $\lVert \mathbf{a} \rVert$, pas par $\lVert \mathbf{a} \rVert^2$.

</details>

### Ex M07.34 — Les normes de toutes les lignes d'un tableau : axis, keepdims et broadcasting

<details><summary>Indice 1</summary>

Relis l'énoncé (axis et keepdims) et le broadcasting de 0A.

</details>
<details><summary>Indice 2</summary>

`axis=1` écrase les colonnes : une valeur par ligne. Pour diviser chaque ligne par sa norme, il faut une colonne de forme `(n, 1)` : `keepdims=True`.

</details>
<details><summary>Indice 3</summary>

`normalize_rows` : `norms = np.sqrt(np.sum(X ** 2, axis=1, keepdims=True))`, puis `X / np.where(norms > 0, norms, 1.0)`.

</details>

### Ex M07.35 — Défi : le point qui minimise la somme des distances (non au carré) à 60 villes, à 0,1 % près

<details><summary>Indice 1</summary>

Relis l'énoncé, puis M07.31 : ni le barycentre ni la médiane coordonnée par coordonnée ne suffisent.

</details>
<details><summary>Indice 2</summary>

Le gradient de $\sum_i \lVert \mathbf{c} - \mathbf{x}_i \rVert$ est $\sum_i \frac{\mathbf{c} - \mathbf{x}_i}{\lVert \mathbf{c} - \mathbf{x}_i \rVert}$. Annule-le : $\mathbf{c}$ s'écrit comme un barycentre pondéré des villes, avec des poids qui dépendent de $\mathbf{c}$.

</details>
<details><summary>Indice 3</summary>

Itère $\mathbf{c} \leftarrow \frac{\sum_i \mathbf{x}_i / d_i}{\sum_i 1 / d_i}$, avec $d_i = \lVert \mathbf{x}_i - \mathbf{c} \rVert$ (un plancher comme $10^{-12}$ évite la division par zéro), en partant du barycentre, quelques centaines de fois.

</details>
