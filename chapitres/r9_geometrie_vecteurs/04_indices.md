# R9 · Géométrie du plan, vecteurs et trigonométrie — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R9.Q1 — Coordonnées et distance

<details><summary>Indice 1</summary>

Relis « Un repère et des coordonnées », « La distance entre deux points » et « Le milieu d'un segment » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Place chaque point sur un quadrillage. Le milieu : les moyennes des coordonnées. La distance : Pythagore sur les écarts.

</details>
<details><summary>Indice 3</summary>

2 : $\frac{-4 + 2}{2} = -1$, et fais de même pour l'ordonnée. Pour 5, pense à un trajet fait seulement de pas horizontaux et verticaux (fiche §3). Pour 6, compare $\sqrt{2}$ et 1,5.

</details>

### R9.Q2 — Vecteurs : vrai ou faux

<details><summary>Indice 1</summary>

Relis le §2 (vecteurs, Chasles, colinéarité) et le §3 (norme, inégalité triangulaire, vecteur unitaire).

</details>
<details><summary>Indice 2</summary>

Pour chaque affirmation, cherche un contre-exemple simple avec des vecteurs du plan ; si tu n'en trouves pas, cherche la règle de la fiche qui la justifie.

</details>
<details><summary>Indice 3</summary>

2 : cherche le nombre $k$ tel que $(2 ; -6) = k(-1 ; 3)$. Pour 3, essaie $\vec{u} = (1 ; 0)$ et $\vec{v} = (-1 ; 0)$. Pour 4, relis la règle $\lVert k\vec{u} \rVert = \ldots$ du §3. Pour 6, calcule la norme de $(1 ; 1)$.

</details>

### R9.Q3 — Pente et vecteur directeur

<details><summary>Indice 1</summary>

Relis « L'équation réduite », « Vecteur directeur » et « L'équation cartésienne » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Pour $y = mx + p$, $(1 ; m)$ est directeur ; pour $ax + by + c = 0$, $(-b ; a)$ est directeur. Deux droites sont parallèles quand elles ont la même pente.

</details>
<details><summary>Indice 3</summary>

3 : avec $a = 2$ et $b = -5$, $(-b ; a) = (5 ; 2)$. Pour 5, isole $y$ dans $6x + 2y - 1 = 0$. Pour 6, remplace $x$ par 1 et $y$ par 2.

</details>

### R9.Q4 — Le signe du produit scalaire

<details><summary>Indice 1</summary>

Relis « Définition en coordonnées », « Orthogonalité » et « Le signe du produit scalaire » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Le produit scalaire est un nombre, de même signe que le cosinus de l'angle ; il est nul pour des vecteurs orthogonaux, et $\vec{u} \cdot \vec{u} = \lVert \vec{u} \rVert^2$.

</details>
<details><summary>Indice 3</summary>

2 : $1 \times (-2) + 2 \times 1$. Pour 4, relis la définition : que donne la somme $xx' + yy'$ ? Pour 6, cherche un vecteur non nul orthogonal à $(1 ; 2)$ : son quart de tour.

</details>

### R9.Q5 — Radians et valeurs remarquables

<details><summary>Indice 1</summary>

Relis « Les radians » et « Cosinus et sinus », avec le tableau des valeurs remarquables (fiche §6).

</details>
<details><summary>Indice 2</summary>

180° valent $\pi$ radians. Sur le cercle trigonométrique, le cosinus est l'abscisse et le sinus l'ordonnée.

</details>
<details><summary>Indice 3</summary>

1 : 90° est la moitié de 180°. Pour 4, le point d'angle $\frac{\pi}{2}$ est en haut du cercle. Pour 6, retrouve le tableau : les cosinus valent $\frac{\sqrt{4}}{2}, \frac{\sqrt{3}}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{1}}{2}, \frac{\sqrt{0}}{2}$.

</details>

### R9.Q6 — Le cosinus de deux vecteurs

<details><summary>Indice 1</summary>

Relis « Le produit scalaire et l'angle » et « La similarité cosinus » (fiche §7), et « Retrouver un angle : arccos » (§6).

</details>
<details><summary>Indice 2</summary>

La similarité cosinus est le cosinus de l'angle entre les deux vecteurs : 1, même sens ; 0, orthogonaux ; $-1$, sens contraires.

</details>
<details><summary>Indice 3</summary>

4 : quel angle a pour cosinus 0,9 ? Il est proche de 0 ou de 90° ? Pour 5, quel angle de $[0 ; \pi]$ a pour cosinus 0 ? Pour 6, que vaut la norme du vecteur nul ?

</details>

### R9.Q7 — Combien de composantes ?

<details><summary>Indice 1</summary>

Relis le §8 : « Trois coordonnées » et « $n$ coordonnées ».

</details>
<details><summary>Indice 2</summary>

Avec $n$ coordonnées, la norme, le produit scalaire et la distance se calculent comme dans le plan, avec une somme de $n$ termes.

</details>
<details><summary>Indice 3</summary>

2 : $\sqrt{1 + 1 + 1 + 1}$. Pour 3, compte les coordonnées de chaque vecteur. Pour 4, compte les pixels, puis les nombres de chaque pixel. Pour 5, une multiplication par coordonnée. Pour 6, le vecteur entre les deux points est $(-1, 1, 0)$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### R9.R1 — Fonctions affines (R3)

<details><summary>Indice 1</summary>

Relis R3 §3, « La droite qui passe par deux points », et le sens de variation d'une fonction affine.

</details>
<details><summary>Indice 2</summary>

La pente est le rapport $\frac{\Delta y}{\Delta x}$. Deux droites sont parallèles quand elles ont la même pente. Une fonction affine est croissante quand sa pente est positive.

</details>
<details><summary>Indice 3</summary>

1 : $\frac{4 - (-2)}{3 - 0}$. Pour 2, remplace $x$ par 5 dans $-0{,}5x + 4$. Pour 4, regarde le signe de $-0{,}5$.

</details>

### R9.R2 — Racines carrées (R1)

<details><summary>Indice 1</summary>

Relis R1, les règles des racines carrées.

</details>
<details><summary>Indice 2</summary>

$\sqrt{ab} = \sqrt{a}\sqrt{b}$ pour $a, b \ge 0$ ; cherche le plus grand carré parfait qui divise le nombre. Mais $\sqrt{a + b} \ne \sqrt{a} + \sqrt{b}$.

</details>
<details><summary>Indice 3</summary>

1 : $50 = 25 \times 2$. Pour 3, multiplie le numérateur et le dénominateur par $\sqrt{2}$. Pour 4, calcule d'abord $1 + 1$, puis compare $\sqrt{2}$ à 2.

</details>

### R9.R3 — Dériver une composée (R7)

<details><summary>Indice 1</summary>

Relis la règle de la chaîne de R7.

</details>
<details><summary>Indice 2</summary>

$(f(g(x)))' = g'(x) \times f'(g(x))$ : la dérivée de la fonction de l'intérieur sort devant.

</details>
<details><summary>Indice 3</summary>

1 : l'intérieur est $3x + 1$, de dérivée 3, et la dérivée de $u^2$ est $2u$. Pour 4, l'intérieur est $4t$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R9.1 — Coordonnées et distance

<details><summary>Indice 1</summary>

Relis le §1 : la distance, le milieu, et la réciproque du théorème de Pythagore (collège).

</details>
<details><summary>Indice 2</summary>

Calcule d'abord les vecteurs $\overrightarrow{AB}$, $\overrightarrow{AC}$ et $\overrightarrow{BC}$ (arrivée moins départ), puis leurs longueurs. Un triangle est rectangle quand le carré du plus grand côté est la somme des carrés des deux autres.

</details>
<details><summary>Indice 3</summary>

b : $\overrightarrow{AB} = (9 ; 12)$, donc $AB = \sqrt{81 + 144}$. Pour c, $\overrightarrow{AC} = (2 ; -1{,}5)$. Pour g, écris $M(x ; 0)$ et $MA^2 = MB^2$, puis développe : les $x^2$ s'en vont. Pour h, $B$ est le milieu : $x_B = \frac{x_A + x_{A'}}{2}$.

</details>

### Ex R9.2 — Vecteurs : somme, différence, produit par un nombre

<details><summary>Indice 1</summary>

Relis le §2 : coordonnées d'un vecteur, somme, produit par un nombre, parallélogramme et colinéarité.

</details>
<details><summary>Indice 2</summary>

Tout se fait coordonnée par coordonnée. Pour placer un point, pars d'un point connu et ajoute un vecteur : $C = A + \overrightarrow{AC}$.

</details>
<details><summary>Indice 3</summary>

c : $3\vec{u} = (12 ; -3)$ et $2\vec{v} = (-4 ; 6)$. Pour f, $\overrightarrow{AB} = \overrightarrow{DC}$, donc $D = C - \overrightarrow{AB}$. Pour g, calcule $xy' - x'y$.

</details>

### Ex R9.3 — Normes (euclidienne, avec un aperçu de L1 et L∞) et vecteurs unitaires

<details><summary>Indice 1</summary>

Relis le §3 : la norme, ses propriétés, le vecteur unitaire et les normes L1 et L∞.

</details>
<details><summary>Indice 2</summary>

L2 : la racine de la somme des carrés ; L1 : la somme des valeurs absolues ; L∞ : la plus grande valeur absolue. Normaliser : diviser par la norme L2.

</details>
<details><summary>Indice 3</summary>

a : $\sqrt{5^2 + (-3)^2}$. Pour b, écris $t^2 + 2^2 = 13$. Pour d, $\lVert (1 ; -2) \rVert = \sqrt{5}$. Pour e, additionne d'abord $\vec{u}$ et $\vec{v}$. Pour h, rends d'abord $\vec{u}$ unitaire, puis multiplie-le par 3.

</details>

### Ex R9.4 — Équations de droites

<details><summary>Indice 1</summary>

Relis le §4 : l'équation réduite, le vecteur directeur, l'équation cartésienne et les droites parallèles.

</details>
<details><summary>Indice 2</summary>

Pente $m = \frac{y_B - y_A}{x_B - x_A}$, puis $p = y_A - m x_A$. Pour une équation cartésienne, fais tout passer du même côté, puis multiplie pour obtenir le coefficient $a$ demandé.

</details>
<details><summary>Indice 3</summary>

a : $\frac{-1 - 5}{2 - (-2)}$. Pour d, $y = -1{,}5x + 2$ devient $1{,}5x + y - 2 = 0$ ; il reste à multiplier par 2. Pour g, remplace $y$ par $x$ dans l'équation réduite. Pour h, les deux points ont la même abscisse.

</details>

### Ex R9.5 — Le produit scalaire en coordonnées

<details><summary>Indice 1</summary>

Relis « Définition en coordonnées » et les règles de calcul (fiche §5).

</details>
<details><summary>Indice 2</summary>

$\vec{u} \cdot \vec{v} = xx' + yy'$. La linéarité permet de calculer e et f à partir de a, b et c.

</details>
<details><summary>Indice 3</summary>

a : $2 \times (-3) + 5 \times 1$. Pour f, sors les facteurs : $(2\vec{u}) \cdot (-3\vec{v}) = 2 \times (-3) \times (\vec{u} \cdot \vec{v})$. Pour g, écris que le produit scalaire de $(t ; 4)$ et $\vec{u}$ est nul.

</details>

### Ex R9.6 — Orthogonalité et projections simples

<details><summary>Indice 1</summary>

Relis « Orthogonalité » et « Projeter un vecteur sur une direction » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Orthogonaux : produit scalaire nul. Projection : $\vec{p} = \frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert^2}\vec{u}$, de longueur $\frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert}$ quand le produit scalaire est positif.

</details>
<details><summary>Indice 3</summary>

b : écris $5 \times 4 + (-2) \times y = 0$. Pour c, développe $3k + 2(k + 1)$. Pour e, $\vec{u} \cdot \vec{v} = 20$ et $\lVert \vec{u} \rVert = \sqrt{10}$. Pour h, compare les vecteurs directeurs $(1 ; m)$.

</details>

### Ex R9.7 — Degrés et radians, cosinus et sinus remarquables

<details><summary>Indice 1</summary>

Relis « Les radians », le tableau des valeurs remarquables et « Les symétries du cercle » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Convertis avec $\frac{\pi}{180}$ ou $\frac{180}{\pi}$. Pour un cosinus ou un sinus, écris l'angle comme $\pi \pm$ (un angle du tableau) ou $2\pi -$ (un angle du tableau), puis lis le signe sur la figure.

</details>
<details><summary>Indice 3</summary>

a : $105 \times \frac{\pi}{180}$, puis simplifie $\frac{105}{180}$. Pour d, $\frac{5\pi}{6} = \pi - \frac{\pi}{6}$, et le point est à gauche de l'axe vertical. Pour h, retire un tour complet.

</details>

### Ex R9.8 — Les courbes de cos et de sin : période, symétries, et arccos sur [0, π]

<details><summary>Indice 1</summary>

Relis « Périodicité et courbes », « Retrouver un angle : arccos » et « Dérivées (aperçu) » (fiche §6).

</details>
<details><summary>Indice 2</summary>

$t \mapsto \cos(\omega t)$ a pour période $\frac{2\pi}{\omega}$ ; $\arccos$ rend un angle de $[0 ; \pi]$ ; la dérivée de $\sin(\omega x)$ est $\omega\cos(\omega x)$.

</details>
<details><summary>Indice 3</summary>

a : $\omega = 3$. Pour b et c, dessine le cercle et la droite verticale $x = 0$, puis la droite horizontale $y = 0{,}3$. Pour e, calcule d'abord $\cos\frac{5\pi}{3}$, puis cherche l'angle de $[0 ; \pi]$ qui a ce cosinus.

</details>

### Ex R9.9 — L'angle entre deux vecteurs

<details><summary>Indice 1</summary>

Relis « Le produit scalaire et l'angle » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\cos\theta = \frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert\,\lVert \vec{v} \rVert}$, puis $\theta = \arccos(\ldots)$. Reconnais les valeurs remarquables ($\frac{\sqrt{2}}{2}$, $\frac{\sqrt{3}}{2}$…) avant de prendre la calculatrice.

</details>
<details><summary>Indice 3</summary>

a : $\frac{2 \times (-1) + 1 \times 4}{\sqrt{5}\sqrt{17}}$. Pour c, $\cos = \frac{-3}{3\sqrt{2}}$. Pour l'angle en $B$, prends les vecteurs qui partent de $B$ : $\overrightarrow{BA}$ et $\overrightarrow{BC}$.

</details>

### Ex R9.10 — Distances et produits scalaires dans ℝ³ et ℝ⁴

<details><summary>Indice 1</summary>

Relis le §8 : « Trois coordonnées » et « $n$ coordonnées ».

</details>
<details><summary>Indice 2</summary>

Mêmes formules que dans le plan, avec une somme de trois ou quatre termes.

</details>
<details><summary>Indice 3</summary>

a : $\sqrt{1 + 16 + 64}$. Pour c, $\overrightarrow{PQ} = (2 ; 6 ; 3)$. Pour h, développe $(1, t, 2, -1) \cdot (2, 3, -1, 4)$ et isole $t$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R9.11 — Démontrer cos² + sin² = 1 avec Pythagore

<details><summary>Indice 1</summary>

Relis « Cosinus et sinus » (fiche §6) et « La distance entre deux points » (§1).

</details>
<details><summary>Indice 2</summary>

Dans le triangle $OHM$, $OM = 1$ est l'hypoténuse. Pour un angle quelconque, la distance de $O$ à $M(\cos\theta ; \sin\theta)$ vaut 1.

</details>
<details><summary>Indice 3</summary>

1 : $OH = \cos\theta$ et $HM = \sin\theta$, puis Pythagore. Pour 3, $\sin^2\theta = 1 - \frac{1}{9}$ : choisis le signe grâce à l'intervalle $[0 ; \pi]$. Pour 5, essaie $\frac{\pi}{3}$ et $\frac{2\pi}{3}$.

</details>

### Ex R9.12 — La formule d'Al-Kashi par la hauteur du triangle et Pythagore

<details><summary>Indice 1</summary>

Relis « La formule d'Al-Kashi » (fiche §7), les définitions de cos et sin dans un triangle rectangle (§6) et les identités remarquables de R2.

</details>
<details><summary>Indice 2</summary>

Coupe le triangle par la hauteur issue de $A$ : deux triangles rectangles. Exprime $CH$ et $AH$ dans $AHC$, puis applique Pythagore dans $ABH$.

</details>
<details><summary>Indice 3</summary>

2 : $BH = a - b\cos\hat{C}$, puis $c^2 = (b\sin\hat{C})^2 + (a - b\cos\hat{C})^2$ ; développe, et regroupe $\sin^2 + \cos^2$. Pour 4, compare $(b\cos\hat{C} - a)^2$ et $(a - b\cos\hat{C})^2$. Pour 5, l'angle cherché est opposé au côté 7 : c'est lui qui joue le rôle de $c$.

</details>

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R9.13 — Deux recettes, deux vecteurs d'ingrédients : la similarité cosinus

<details><summary>Indice 1</summary>

Relis « La similarité cosinus » (fiche §7) et « $n$ coordonnées » (§8).

</details>
<details><summary>Indice 2</summary>

Produit scalaire, normes, puis leur quotient. Pour g, calcule les trois similarités cosinus des sablés avec les autres recettes, et compare-les.

</details>
<details><summary>Indice 3</summary>

a : $5 \times 5 + 1 \times 5 + 1 \times 5 + 10 \times 0$. Pour e, $\lVert \mathbf{s} \rVert = \sqrt{36 + 4 + 9}$. Pour g, ne choisis pas la recette du plus grand produit scalaire : divise d'abord par les normes.

</details>

### Ex R9.14 — Un neurone trace une droite : w₁x₁ + w₂x₂ + b = 0

<details><summary>Indice 1</summary>

Relis « De quel côté de la droite ? » (fiche §4) et l'encadré 🔗 du §5.

</details>
<details><summary>Indice 2</summary>

$z = x_1 + 3x_2 - 6$. La frontière est la droite $x_1 + 3x_2 - 6 = 0$, une équation cartésienne : $\mathbf{w} = (a ; b)$ en est un vecteur normal, et $(-b ; a)$ un vecteur directeur.

</details>
<details><summary>Indice 3</summary>

a : $3 + 3 \times 2 - 6$. Pour c, un point de l'axe des $x_2$ a $x_1 = 0$. Pour g, la droite $z = 6$ s'écrit $x_1 + 3x_2 - 12 = 0$. Pour h, calcule $z$ pour chacun des cinq points, et compte ceux où $z > 0$.

</details>

### Ex R9.15 — Expliquer ce que mesure un produit scalaire

<details><summary>Indice 1</summary>

Relis le §5 et la formule $\vec{u} \cdot \vec{v} = \lVert \vec{u} \rVert\,\lVert \vec{v} \rVert\cos\theta$ (§7).

</details>
<details><summary>Indice 2</summary>

Le produit scalaire dépend des deux longueurs et de l'angle ; son signe est celui du cosinus. Cherche une image : une ombre, un effort dans une direction.

</details>
<details><summary>Indice 3</summary>

Par exemple : « on multiplie coordonnée par coordonnée et on additionne ; ce nombre dit à quel point les deux flèches vont dans le même sens », puis le signe, le zéro et ton image.

</details>

<a id="notebook"></a>

## Notebook

### Ex R9.16 — Le vecteur entre deux points et sa norme · `vector`, `norm`

<details><summary>Indice 1</summary>

Relis le §2 (coordonnées d'un vecteur), le §3 (norme) et le §8 (dimension quelconque), puis les docstrings.

</details>
<details><summary>Indice 2</summary>

`vector` : le cas interdit (dimensions différentes), puis arrivée moins départ, coordonnée par coordonnée, dans un tuple. `norm` : la somme des carrés, puis `math.sqrt`.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
if len(A) != len(B):
    raise ValueError(...)
return tuple(b - a for a, b in zip(A, B))
```
Pour `norm`, un total qui part de 0, une boucle `for x in u`, puis `math.sqrt(total)`.

</details>

### Ex R9.17 — Produit scalaire et angle · `dot`, `angle_between`

<details><summary>Indice 1</summary>

Relis le §5 (produit scalaire) et le §7 (angle et similarité cosinus), puis les docstrings.

</details>
<details><summary>Indice 2</summary>

`dot` : le cas interdit, puis la somme des produits. `angle_between` : les deux normes (une `ValueError` si l'une est nulle), le quotient, ramené dans $[-1 ; 1]$, puis `math.acos`.

</details>
<details><summary>Indice 3</summary>

Les deux lignes clés :
```python
cosine = dot(u, v) / (length_u * length_v)
cosine = max(-1.0, min(1.0, cosine))
```
Pour la copie : $\sqrt{37} \times \sqrt{148}$ calculé en flottants ne redonne pas exactement 74.

</details>

### Ex R9.18 — La droite qui passe par deux points, et les radians · `line_through`, `deg_to_rad`

<details><summary>Indice 1</summary>

Relis « L'équation cartésienne » (fiche §4), le quart de tour (§5) et « Les radians » (§6).

</details>
<details><summary>Indice 2</summary>

Un vecteur directeur $(d_x ; d_y)$, tourné d'un quart de tour, donne un vecteur normal $(-d_y ; d_x) = (a ; b)$ ; puis $c$ s'obtient en écrivant que $A$ est sur la droite.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
dx, dy = xb - xa, yb - ya
a, b = -dy, dx
c = -(a * xa + b * ya)
```
N'oublie pas la `ValueError` quand les deux points sont égaux. Pour `deg_to_rad`, 180 doit donner `math.pi`.

</details>

### Ex R9.19 — Les mêmes calculs avec NumPy (`np.linalg.norm`, `@`)

<details><summary>Indice 1</summary>

Relis « En Python : NumPy » (fiche §8).

</details>
<details><summary>Indice 2</summary>

`np.linalg.norm(x)` pour la norme L2, `ord=1` et `ord=np.inf` pour les deux autres ; `x @ y` pour le produit scalaire ; `np.arccos` et `np.degrees` pour l'angle.

</details>
<details><summary>Indice 3</summary>

e : `x @ y / (np.linalg.norm(x) * np.linalg.norm(y))`. Pour f, la distance est la norme de `x - y`. Pour g, réutilise la valeur de e.

</details>

### Ex R9.20 — Prédire : multiplier ou décaler deux vecteurs change-t-il leur similarité cosinus ?

<details><summary>Indice 1</summary>

Relis « La similarité cosinus » (fiche §7), les règles de calcul du produit scalaire (§5) et les propriétés de la norme (§3).

</details>
<details><summary>Indice 2</summary>

Écris tes prédictions, même incertaines : l'expérience tranchera. Demande-toi, pour chaque transformation, si elle change la direction des vecteurs.

</details>
<details><summary>Indice 3</summary>

Pour a et c, écris le numérateur et le dénominateur de la similarité cosinus après la transformation. Pour b, regarde ce que deviennent les coordonnées : toutes positives, et proches les unes des autres ?

</details>

### Ex R9.21 — Dessiner des vecteurs, leur somme et un angle

<details><summary>Indice 1</summary>

Relis la figure des vecteurs (fiche §2) et le calcul de l'angle (§7).

</details>
<details><summary>Indice 2</summary>

Dans l'axe reçu : un seul `ax.quiver` pour les trois flèches, `ax.set_aspect("equal")`, des limites qui contiennent les quatre sommets du parallélogramme, puis l'angle calculé dans la fonction et écrit dans le titre.

</details>
<details><summary>Indice 3</summary>

L'appel :
```python
ax.quiver([0, 0, 0], [0, 0, 0], [u[0], v[0], s[0]], [u[1], v[1], s[1]], angles="xy", scale_units="xy", scale=1)
```
avec `s = (u[0] + v[0], u[1] + v[1])`. Le titre : `f"angle = {angle:.1f}°"`.

</details>

### Ex R9.22 — Le cercle trigonométrique : cos et sin d'un angle qui tourne

<details><summary>Indice 1</summary>

Relis « Cosinus et sinus », « Périodicité et courbes » et « Dérivées (aperçu) » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Convertis d'abord les degrés en radians avec `np.radians`, puis travaille sur des arrays : `np.sin(theta) > np.cos(theta)` est un array de booléens, et `np.argmax` donne la position de son premier `True`.

</details>
<details><summary>Indice 3</summary>

a : `np.max(np.abs(np.cos(theta) ** 2 + np.sin(theta) ** 2 - 1)) < 1e-12`. Pour b et c, `np.argmax` rend une position : l'angle est `degrees[position]` ou `whole[position]`. Pour d, `(math.sin(1 + h) - math.sin(1)) / h`.

</details>

### Ex R9.23 — Chasse à l'erreur : radians et degrés

<details><summary>Indice 1</summary>

Relis « Les radians » et « En Python : des radians, toujours » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne : la fonction reçoit-elle des radians ? Dans quelle unité répond-elle ? La conversion donne-t-elle π pour 180° ?

</details>
<details><summary>Indice 3</summary>

(A) : `math.sin(45)` calcule le sinus de 45 radians, pas de 45°. Applique les trois questions aux quatre autres lignes. Pour b, chaque phrase décrit une valeur : calcule-la correctement, que la ligne soit juste ou fausse.

</details>

### Ex R9.24 — Comparer deux flottants : `np.isclose`

<details><summary>Indice 1</summary>

Relis la section de R0 sur les flottants, et l'avertissement de la fiche §7 sur `math.acos`.

</details>
<details><summary>Indice 2</summary>

Un produit scalaire calculé en flottants vaut rarement 0 exactement : compare sa valeur absolue à une tolérance, et renvoie un booléen de Python (`return`, pas `print`).

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
dot = sum(a * b for a, b in zip(u, v))
return math.isclose(dot, 0, abs_tol=tol)
```
Pour la copie, essaie `math.isclose(1e-17, 0)` et `math.isclose(1e-17, 0, abs_tol=1e-9)`.

</details>
