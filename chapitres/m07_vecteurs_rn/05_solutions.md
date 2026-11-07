# M07 · Vecteurs et géométrie de ℝⁿ — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M07.Q1 — Vecteurs, coordonnées et one-hot
1. Chaque exemple est un vecteur de $\mathbb{R}^{12}$ : une coordonnée par colonne.
2. **Faux** : l'addition se fait coordonnée par coordonnée, il faut le même nombre de coordonnées.
3. $(2, 0, -6) - (0, 4, 1) = (2, -4, -7)$.
4. $(0, 1, 0)$ : le 1 à la deuxième place, celle de « avion ».
5. **Vrai** : un seul 1, et des 0 ailleurs.
6. $(4, -2, 5) = 4\,\mathbf{e}_1 - 2\,\mathbf{e}_2 + 5\,\mathbf{e}_3$ : les coefficients sont les coordonnées.

### M07.Q2 — Ce que mesure un produit scalaire
1. $4 + 0 - 3 = 1$.
2. **Faux** : c'est un **nombre** (un scalaire), quelle que soit la dimension.
3. $\mathbf{u} = \mathbf{0}$ : $\mathbf{u} \cdot \mathbf{u} = \sum u_i^2$ n'est nul que si chaque coordonnée l'est.
4. $-3$ : le produit scalaire avec $\mathbf{e}_2$ lit la deuxième coordonnée.
5. **Vrai** : c'est la linéarité du produit scalaire.
6. $z = 2 \times 1 + (-1) \times 3 + 1 = 0$ : le point est exactement sur la frontière.

### M07.Q3 — Trois normes, trois boules unités
1. 5, 5 et 5 : avec une seule coordonnée non nulle, les trois normes valent sa valeur absolue.
2. L1 : un **losange** (un carré posé sur la pointe, de sommets $(\pm 1, 0)$ et $(0, \pm 1)$) ; L∞ : un **carré** de côté 2 centré à l'origine.
3. **Vrai** (fiche §3) : un maximum est au plus la racine de la somme des carrés, qui est au plus la somme des valeurs absolues.
4. $\lVert -3\mathbf{x} \rVert = 3\,\lVert \mathbf{x} \rVert$ (homogénéité : la valeur absolue de $-3$).
5. $|1 - 6| + |2 - 0| = 5 + 2 = 7$.
6. Elle viole l'**inégalité triangulaire** : $\mathbf{e}_1$ et $\mathbf{e}_2$ ont chacun la valeur 1, mais $\mathbf{e}_1 + \mathbf{e}_2$ a la valeur $(1 + 1)^2 = 4 > 2$.

### M07.Q4 — Similarité cosinus : vrai ou faux
1. **Vrai** : le facteur 10 apparaît en haut et en bas, et se simplifie.
2. **Faux** : le cosinus change de signe (l'angle $\theta$ devient $180° - \theta$).
3. **Vrai** (pour deux vecteurs non nuls) : $\cos\theta = 0$ équivaut à $\mathbf{u} \cdot \mathbf{v} = 0$.
4. **Faux** : l'inégalité de Cauchy-Schwarz vaut en toute dimension, et c'est elle qui permet de définir l'angle.
5. **Vrai** : le produit scalaire est une somme de produits positifs ou nuls.
6. **Faux** : un cosinus de 1 dit que les directions sont les mêmes, pas les longueurs. $\mathbf{u}$ et $2\mathbf{u}$ ont un cosinus de 1 et sont à la distance $\lVert \mathbf{u} \rVert$.

### M07.Q5 — Hyperplans : vecteur normal et côtés
1. 3 : un hyperplan de $\mathbb{R}^n$ est de dimension $n - 1$.
2. $(2, -1, 5)$, ou n'importe quel multiple non nul.
3. Du côté **négatif** : en $(0, 0, 0)$, l'expression vaut $-1$.
4. **Vrai** : $3\mathbf{w} \cdot \mathbf{x} + 3b = 0$ équivaut à $\mathbf{w} \cdot \mathbf{x} + b = 0$.
5. **Faux** : c'est le même hyperplan, mais les côtés positif et négatif sont **échangés**.
6. $\frac{|b|}{\lVert \mathbf{w} \rVert}$ : la formule de la distance appliquée à $\mathbf{x} = \mathbf{0}$.

### M07.Q6 — Moyenne, barycentre et inertie
1. $\big(\frac{0 + 4 + 2}{3}, \frac{0 + 0 + 6}{3}\big) = (2, 2)$.
2. **Faux** : ici, $(2, 2)$ n'est aucun des trois points.
3. Au **barycentre** du nuage, et seulement là (König-Huygens).
4. L'affectation rattache chaque point au centre le plus proche ; la mise à jour remplace chaque centre par le barycentre des points qui lui sont rattachés.
5. **Vrai** : $b(i) < a(i)$, le point est en moyenne plus près de l'autre cluster que du sien.
6. **Non** : sa distance au centre le plus proche (lui-même) est nulle, donc sa probabilité aussi.

### M07.Q7 — Intuitions de la grande dimension
1. $\sqrt{100} = 10$.
2. **Vrai** : $\cos\theta = \frac{1}{\sqrt{n}}$ tend vers 0.
3. (B) : le cosinus est de l'ordre de $\frac{1}{\sqrt{10\,000}} = 0{,}01$.
4. Environ $\sqrt{n}$ : $\mathbb{E}\big[\lVert \mathbf{X} \rVert^2\big] = n$, et la norme se concentre autour de $\sqrt{n}$.
5. **Vrai** : c'est la concentration des distances (fiche §7).
6. Le « plus proche voisin » n'est alors guère plus proche que les autres points : la notion de voisinage perd son sens, sauf si les données ont de la structure.

<a id="rappels"></a>

## 🔁 Rappels

### M07.R1 — Produit scalaire et angle dans le plan (R9)
1. $-2 + 15 = 13$.
2. $\cos\theta = \frac{-1}{1 \times 2} = -\frac{1}{2}$, donc $\theta = 120°$.
3. $(2 ; 5)$ : $5 \times 2 + (-2) \times 5 = 0$ (ou tout multiple non nul).
4. $\lVert (-5 ; 12) \rVert = 13$, d'où $\big(-\frac{5}{13} ; \frac{12}{13}\big)$.
5. $(2 ; 0)$ : projeter sur l'axe des abscisses garde l'abscisse.

### M07.R2 — Moyenne et variance empiriques (M02c)
1. $\frac{4 + 7 + 7 + 10 + 12}{5} = 8$.
2. Les écarts $-4, -1, -1, 2, 4$ ont pour carrés $16, 1, 1, 4, 16$, de somme 38 : variance $\frac{38}{5} = 7{,}6$.
3. $\frac{38}{4} = 9{,}5$.
4. 38.
5. $c = 8$, la moyenne : la dérivée de $\sum (x_i - c)^2$ est $-2\sum(x_i - c)$, nulle quand $c$ est la moyenne (c'est la dimension 1 de König-Huygens, fiche §6).

### M07.R3 — Gradient et point critique (M05b)
1. $\frac{\partial f}{\partial c_1} = 2(c_1 - 2) + 2(c_1 - 6) = 4c_1 - 16$ et $\frac{\partial f}{\partial c_2} = 2(c_2 - 1) + 2(c_2 - 5) = 4c_2 - 12$.
2. $(4, 3)$.
3. Un **minimum** : $f_{c_1c_1} = 4 > 0$, $f_{c_2c_2} = 4$, $f_{c_1c_2} = 0$, donc $D = 16 > 0$ (et $f$ est une somme de carrés, un bol).
4. Le **milieu** des points $(2, 1)$ et $(6, 5)$, c'est-à-dire leur barycentre : $f(\mathbf{c})$ est la somme des carrés des distances de $\mathbf{c}$ aux deux points.
5. $f(4, 3) = 4 + 4 + 4 + 4 = 16$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M07.1 — Combinaisons linéaires et vecteurs one-hot dans ℝ⁴

**Réponses** : a) `[4, -1, -1, 6]` · b) `[-7, -7, 3, 2]` · c) `[-2, -1, 6, 1]` · d) `[2, 1]` · e) `[0, 0, 1, 0]` · f) `[4, 3, 0, 3]` · g) `[0.4, 0.3, 0, 0.3]`.

**Démarche.** Tout se fait coordonnée par coordonnée.
- b) $2\mathbf{u} = (2, -4, 0, 8)$ et $3\mathbf{v} = (9, 3, -3, 6)$, d'où $(-7, -7, 3, 2)$.
- d) $a\,(1, -2, 0, 4) + b\,(3, 1, -1, 2) = (5, -3, -1, 10)$ donne quatre équations : $a + 3b = 5$, $-2a + b = -3$, $-b = -1$, $4a + 2b = 10$. La troisième donne $b = 1$, la première $a = 2$ ; les deux autres sont vérifiées ($-4 + 1 = -3$, $8 + 2 = 10$).
- f) La somme des one-hot compte chaque mode : $4\,(1, 0, 0, 0) + 3\,(0, 1, 0, 0) + 3\,(0, 0, 0, 1)$.
- g) Divisé par 10, le vecteur des proportions, de somme 1.

Pour la copie : deux équations suffisent à trouver $a$ et $b$ ; les deux autres **vérifient** que le vecteur est bien une combinaison de $\mathbf{u}$ et $\mathbf{v}$ (un vecteur de $\mathbb{R}^4$ pris au hasard ne l'est pas : le système n'aurait pas de solution). Coder les modes par 1, 2, 3, 4 mettrait un ordre et des distances entre eux (le métro « entre » le bus et la marche) qui n'existent pas.

**Erreurs fréquentes.** Soustraire au lieu d'ajouter (a) ; un signe perdu dans $-3\mathbf{v}$ (b) ; l'ordre $[b, a]$ en d) ; le 1 à la mauvaise place en e) ; oublier de diviser par 10 en g).

**Variante.** $\mathbf{u} - 2\mathbf{w}$ ? *Réponse* : $(1, -6, -10, 6)$.

### Ex M07.2 — Produits scalaires, ‖u + v‖² et l'identité du parallélogramme

**Réponses** : a) `3` · b) `9` · c) `12` · d) `27` · e) `"-1/4"` · f) `8` · g) `False`.

**Démarche.**
- a) $2 + 3 - 2 + 0 = 3$ ; b) $4 + 1 + 4 + 0 = 9$ ; c) $1 + 9 + 1 + 1 = 12$.
- d) Avec le développement : $9 + 2 \times 3 + 12 = 27$. Directement : $\mathbf{u} + \mathbf{v} = (3, 4, -1, -1)$, et $9 + 16 + 1 + 1 = 27$.
- e) $(\mathbf{u} + t\mathbf{v}) \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{v} + t\,\mathbf{v} \cdot \mathbf{v} = 3 + 12t = 0$, d'où $t = -\frac{1}{4}$.
- f) $\lVert \mathbf{a} + \mathbf{b} \rVert^2 - \lVert \mathbf{a} - \mathbf{b} \rVert^2 = 4\,\mathbf{a} \cdot \mathbf{b}$, donc $\mathbf{a} \cdot \mathbf{b} = \frac{50 - 18}{4} = 8$.
- g) **Faux** : $\mathbf{u} \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{w}$ dit seulement que $\mathbf{u} \cdot (\mathbf{v} - \mathbf{w}) = 0$. Contre-exemple : $\mathbf{u} = (1, 0)$, $\mathbf{v} = (0, 1)$, $\mathbf{w} = (0, 2)$ ; les deux produits valent 0.

**Erreurs fréquentes.** Un signe perdu dans $(-2) \times 1$ (a : 7) ; donner la norme au lieu de son carré (b : 3) ; oublier le double produit (d : 21) ou son facteur 2 (d : 24) ; utiliser $\mathbf{u} \cdot \mathbf{u}$ au lieu de $\mathbf{v} \cdot \mathbf{v}$ en e) ; oublier de diviser par 4 en f).

**Variante.** Avec les mêmes $\mathbf{u}$ et $\mathbf{v}$, $\lVert 2\mathbf{u} + \mathbf{v} \rVert^2$ ? *Réponse* : $4 \times 9 + 4 \times 3 + 12 = 60$.

### Ex M07.3 — Normes L1, L2, L∞ et distances entre trois profils

**Réponses** : a) `[5, 3, 2]` · b) `[4, 2, 1]` · c) `2.646` · d) `"Q"` · e) `"R"` · f) `[0.3333, -0.6667, 0.6667, 0]` · g) `4.646`.

**Démarche.**
- a) $1 + 2 + 2 + 0 = 5$ ; $\sqrt{1 + 4 + 4 + 0} = 3$ ; $\max = 2$.
- b) $R - P = (1, -1, 1, -1)$ : L1 $= 4$, L2 $= \sqrt{4} = 2$, L∞ $= 1$.
- c) $R - Q = (1, 2, 1, -1)$ : $\sqrt{1 + 4 + 1 + 1} = \sqrt{7} \approx 2{,}646$.
- d) et e) $Q - P = (0, -3, 0, 0)$ : les trois distances valent 3. Pour L1, $Q$ est plus proche (3 contre 4) ; pour L2, c'est $R$ (2 contre 3), et pour L∞ aussi (1 contre 3).
- f) $\frac{P}{3} = \big(\frac{1}{3}, -\frac{2}{3}, \frac{2}{3}, 0\big)$.
- g) $d_2(P, R) + d_2(R, Q) = 2 + \sqrt{7} \approx 4{,}646$, qui dépasse bien $d_2(P, Q) = 3$.

Pour la copie : l'écart entre $P$ et $Q$ est **concentré** sur une seule coordonnée, et les trois normes valent alors la même chose (sa valeur absolue). L'écart entre $P$ et $R$ est **réparti** sur les quatre coordonnées : L1 l'additionne (4), L∞ n'en garde que le plus grand (1). La distance L1 pénalise donc surtout les écarts répartis, la distance L∞ les écarts concentrés ; L2 est entre les deux.

**Erreurs fréquentes.** Oublier la racine de L2 (a : 9 ; b : 4 ; c : 7) ; normaliser par la norme L1 (f : `[0.2, -0.4, 0.4, 0]`) ; donner le membre de gauche en g).

**Variante.** $d_1(Q, R)$ et $d_\infty(Q, R)$ ? *Réponse* : 5 et 2.

### Ex M07.4 — Similarité cosinus entre des profils d'écoute musicale

**Réponses** : a) `6` · b) `"8/15"` · c) `57.77` · d) `5.3852` · e) `1` · f) `6` · g) `"C"` · h) `"E"`.

**Démarche.**
- a) $\sqrt{4 + 0 + 16 + 16} = 6$ ; $\lVert C \rVert = \sqrt{0 + 9 + 0 + 16} = 5$.
- b) $A \cdot C = 0 + 0 + 0 + 16 = 16$, donc $\cos = \frac{16}{30} = \frac{8}{15}$.
- c) $\arccos\frac{8}{15} \approx 57{,}77°$.
- d) $A - C = (2, -3, 4, 0)$ : $\sqrt{29} \approx 5{,}3852$.
- e) et f) $E = 2A$ : même direction, cosinus 1 ; $E - A = A$, à la distance $\lVert A \rVert = 6$.
- g) et h) En distance euclidienne, $C$ est plus proche (5,39 contre 6) ; en cosinus, c'est $E$ (1 contre 0,53).

Pour la copie : $E$ a **exactement** les goûts de $A$ (les mêmes proportions de chaque genre), il écoute seulement deux fois plus. C'est le cosinus qui répond à la question des goûts ; la distance euclidienne mélange les goûts et le temps d'écoute, et se laisse tromper par la longueur des vecteurs. Pour recommander des morceaux, on prend le cosinus (ou on normalise d'abord les profils).

**Erreurs fréquentes.** Oublier les racines (a : 36 ; d : 29) ; donner l'angle en radians (c : 1,008) ; une fraction non simplifiée (b : 16/30) ; croire qu'un cosinus de 1 signifie une distance nulle (f).

**Variante.** Le cosinus de $C$ et $E$ ? *Réponse* : $\frac{32}{5 \times 12} = \frac{8}{15}$, le même qu'avec $A$ : $E$ et $A$ ont la même direction.

### Ex M07.5 — Projeter sur une droite : composante parallèle et composante orthogonale

**Réponses** : a) `18` · b) `2` · c) `[4, 0, 2, 4]` · d) `[1, -1, 0, -1]` · e) `0` · f) `39` · g) `[4, 0, 2, 4]` · h) `6`.

**Démarche.**
- a) $10 + 0 + 2 + 6 = 18$ ; $\mathbf{u} \cdot \mathbf{u} = 4 + 0 + 1 + 4 = 9$, donc b) $t = 2$.
- c) $\mathbf{p} = 2\mathbf{u} = (4, 0, 2, 4)$ ; d) $\mathbf{r} = (5 - 4, -1 - 0, 2 - 2, 3 - 4) = (1, -1, 0, -1)$.
- e) $\mathbf{r} \cdot \mathbf{u} = 2 + 0 + 0 - 2 = 0$ : le reste est orthogonal à $\mathbf{u}$, comme il se doit.
- f) $\lVert \mathbf{p} \rVert^2 = 36$ et $\lVert \mathbf{r} \rVert^2 = 3$ : $39$.
- g) Avec $-3\mathbf{u}$ : $\frac{\mathbf{x} \cdot (-3\mathbf{u})}{(-3\mathbf{u}) \cdot (-3\mathbf{u})}\,(-3\mathbf{u}) = \frac{-54}{81}\,(-3\mathbf{u}) = 2\mathbf{u}$, la même projection : seule compte la droite.
- h) $\frac{18}{\lVert \mathbf{u} \rVert} = \frac{18}{3} = 6$, la longueur de $\mathbf{p}$ (positive, car $\mathbf{p}$ a le sens de $\mathbf{u}$).

Pour la copie : $\lVert \mathbf{x} \rVert^2 = 25 + 1 + 4 + 9 = 39$. C'est le théorème de Pythagore : $\mathbf{x} = \mathbf{p} + \mathbf{r}$ avec $\mathbf{p} \perp \mathbf{r}$. Le point de la droite le plus proche de $\mathbf{x}$ est $\mathbf{p}$, à la distance $\lVert \mathbf{r} \rVert = \sqrt{3}$.

**Erreurs fréquentes.** Diviser par $\lVert \mathbf{u} \rVert$ au lieu de $\lVert \mathbf{u} \rVert^2$ (b : 6 ; c : `[12, 0, 6, 12]`) ; multiplier $\mathbf{u}$ par $\mathbf{x} \cdot \mathbf{u}$ sans diviser (c) ; prendre $\mathbf{p} - \mathbf{x}$ en d) ; croire que la longueur ou le sens du vecteur directeur changent la projection (g) ; confondre la composante (h, divisée par $\lVert \mathbf{u} \rVert$) et le coefficient (b, divisé par $\lVert \mathbf{u} \rVert^2$).

**Variante.** La projection de $\mathbf{x}$ sur la droite dirigée par $(0, 1, 0, 0)$ ? *Réponse* : $(0, -1, 0, 0)$ : projeter sur un axe garde une seule coordonnée.

### Ex M07.6 — Un plan de ℝ³ : vecteur normal, côté, distance signée

**Réponses** : a) `[2, -1, 2]` · b) `True` · c) `1` · d) `1` · e) `"-5/3"` · f) `3` · g) `[2.3333, 0.3333, 0.3333]` · h) `-8`.

**Démarche.** $\lVert \mathbf{w} \rVert = \sqrt{4 + 1 + 4} = 3$.
- b) $2 - 1 + 4 - 5 = 0$ : $A$ est sur $H$.
- c) et d) En $B$ : $6 - 0 + 2 - 5 = 3 > 0$, côté positif, distance signée $\frac{3}{3} = 1$.
- e) En $O$ : $-5$, distance signée $-\frac{5}{3}$.
- f) En $C$ : $-2 - 2 + 0 - 5 = -9$, distance $\frac{9}{3} = 3$.
- g) $B - \frac{3}{9}\mathbf{w} = (3, 0, 1) - \frac{1}{3}(2, -1, 2) = \big(\frac{7}{3}, \frac{1}{3}, \frac{1}{3}\big)$.
- h) $2 \times 3 - 0 + 2 \times 1 + b' = 0$, d'où $b' = -8$.

Pour la copie : $O$ et $C$ donnent des scores négatifs, ils sont du même côté. Le point de g) vérifie $\frac{14}{3} - \frac{1}{3} + \frac{2}{3} - 5 = 0$. Les deux plans parallèles sont à la distance $\frac{|-8 - (-5)|}{3} = 1$ (M07.17, question 5), la distance de $B$ à $H$.

**Erreurs fréquentes.** Oublier un signe dans $\mathbf{w}$ (a) ; ne pas diviser le score par $\lVert \mathbf{w} \rVert$ (d : 3 ; e : $-5$ ; f : 9) ; perdre le signe en e) ou le garder en f) ; avancer au lieu de reculer le long de $\mathbf{w}$ en g), ou diviser par $\lVert \mathbf{w} \rVert$ au lieu de $\lVert \mathbf{w} \rVert^2$ ; le signe de $b'$ en h).

**Variante.** La distance de $(0, 5, 0)$ à $H$ ? *Réponse* : $\frac{|-5 - 5|}{3} = \frac{10}{3}$.

### Ex M07.7 — Un score linéaire w · x + b : calculer, décider, lire le vecteur normal

**Réponses** : a) `-0.5` · b) `2.5` · c) `0` · d) `0` · e) `1` · f) `[0.588, 0.784, -0.196]` · g) `0.9806`.

**Démarche.**
- a) $1{,}5 + 1 - 1 - 2 = -0{,}5$ ; c) négatif, donc 0 (on continue).
- b) $3 + 2 - 0{,}5 - 2 = 2{,}5$.
- d) $0 + 2 - 0 - 2 = 0$ : $M_3$ est **sur** la frontière ; la règle « strictement positif » le classe 0.
- e) $2 \times 0{,}5 = 1$ : le poids dit de combien le score change par unité de la feature.
- f) $\lVert \mathbf{w} \rVert = \sqrt{2{,}25 + 4 + 0{,}25} = \sqrt{6{,}5} \approx 2{,}550$, et $\frac{\mathbf{w}}{\lVert \mathbf{w} \rVert} \approx (0{,}588 ;\ 0{,}784 ;\ -0{,}196)$.
- g) $\frac{2{,}5}{\sqrt{6{,}5}} \approx 0{,}9806$.

Pour la copie : $M_3$ est sur la frontière, la décision se joue à rien. Le poids négatif de la troisième feature dit que, toutes choses égales par ailleurs, une révision ancienne fait **baisser** le score : c'est le contraire de ce qu'on attendrait, et un poids de signe surprenant mérite toujours d'être questionné (des features corrélées, un biais des données). Multiplier $\mathbf{w}$ et $b$ par 10 multiplie tous les scores par 10 : les décisions ne changent pas, ni la distance de g) ($\frac{25}{10\sqrt{6{,}5}}$).

**Erreurs fréquentes.** Oublier le biais (a : 1,5 ; b : 4,5) ; prendre $\mathbf{w}$ lui-même pour la direction unitaire (f) ; donner le score au lieu de la distance (g : 2,5) ; diviser par $\lVert \mathbf{w} \rVert^2$ (g : 0,385).

**Variante.** Quelle valeur de la température met $M_1$ sur la frontière, les autres features fixées ? *Réponse* : $1{,}5\,x_1 + 1 - 1 - 2 = 0$, soit $x_1 = \frac{4}{3}$.

### Ex M07.8 — Centroïde, inertie et formule de König-Huygens

**Réponses** : a) `[2, 1]` · b) `20` · c) `45` · d) `60` · e) `4` · f) `[3, 2]` · g) `80`.

**Démarche.**
- a) $\big(\frac{1 + 2 + 4 + 0 + 3}{5}, \frac{3 - 1 + 2 + 0 + 1}{5}\big) = (2, 1)$.
- b) Les écarts au barycentre $(-1, 2)$, $(0, -2)$, $(2, 1)$, $(-2, -1)$, $(1, 0)$ ont pour carrés de norme $5, 4, 5, 5, 1$ : 20.
- c) $10 + 5 + 20 + 0 + 10 = 45$ ; König-Huygens : $20 + 5 \times \lVert (2, 1) \rVert^2 = 20 + 25 = 45$.
- d) $20 + 5 \times \lVert (2, 1) - (4, 3) \rVert^2 = 20 + 5 \times 8 = 60$.
- e) $\frac{20}{5} = 4$.
- f) $\big(\frac{10 + 8}{6}, \frac{5 + 7}{6}\big) = (3, 2)$.
- g) Les cinq anciens points, autour de $(3, 2)$ : $20 + 5 \times \lVert (2, 1) - (3, 2) \rVert^2 = 20 + 10 = 30$ ; le sixième : $\lVert (5, 5) \rVert^2 = 50$. Total : 80.

Pour la copie : un point lointain ajoute le **carré** de sa distance (50 à lui seul), et il déplace en plus le barycentre, ce qui éloigne tous les autres points : les carrés donnent un poids énorme aux points isolés (M07.31).

**Erreurs fréquentes.** Additionner des distances au lieu de leurs carrés (b : 9,71) ; oublier le facteur $m$ dans König-Huygens (d : 28) ; diviser par 4 au lieu de 5 (e : 5) ; en g), oublier que les anciens points ne sont plus centrés (70) ou oublier le nouveau point (30).

**Variante.** L'inertie autour de $(2, 4)$ ? *Réponse* : $20 + 5 \times 9 = 65$.

### Ex M07.9 — Où placer un dépôt : le barycentre pondéré des livraisons

**Réponses** : a) `6` · b) `[1.6667, 1.3333]` · c) `"146/3"` · d) `"164/3"` · e) `False`.

**Démarche.**
- b) $\frac{3\,(0, 0) + 1\,(6, 0) + 2\,(2, 4)}{6} = \frac{(10, 8)}{6} = \big(\frac{5}{3}, \frac{4}{3}\big)$.
- c) $3 \times \frac{41}{9} + 1 \times \frac{185}{9} + 2 \times \frac{65}{9} = \frac{123 + 185 + 130}{9} = \frac{438}{9} = \frac{146}{3}$.
- d) Le barycentre non pondéré est $\big(\frac{8}{3}, \frac{4}{3}\big)$, à la distance 1 du barycentre pondéré ; König-Huygens avec des poids : $\frac{146}{3} + 6 \times 1^2 = \frac{164}{3}$.
- e) **Faux** : doubler les poids double le numérateur et le dénominateur du barycentre pondéré.

Pour la copie : la formule pondérée s'écrit $\sum_i \omega_i \lVert S_i - \mathbf{c} \rVert^2 = \sum_i \omega_i \lVert S_i - \bar{S}_\omega \rVert^2 + \Omega\,\lVert \bar{S}_\omega - \mathbf{c} \rVert^2$, avec $\Omega = \sum \omega_i$ (M07.16). Un coût en carrés fait payer très cher les magasins lointains ; pour des trajets, la somme des distances (non au carré) est plus réaliste. Elle est minimisée par la médiane géométrique (M07.35), ou, si l'on roule sur un quadrillage de rues, par la médiane coordonnée par coordonnée, qui minimise la somme des distances L1 (M07.31).

**Erreurs fréquentes.** Oublier les poids (b : $\big(\frac{8}{3}, \frac{4}{3}\big)$) ; oublier de multiplier le terme de König-Huygens par la somme des poids (d : $\frac{149}{3}$).

**Variante.** Où placer le dépôt si $S_3$ recevait 6 livraisons ? *Réponse* : $\frac{(0, 0) \times 3 + (6, 0) + (12, 24)}{10} = (1{,}8 ;\ 2{,}4)$.

### Ex M07.10 — La silhouette d'un point, à la main, en dimension 2

**Réponses** : a) `2.118` · b) `6.8493` · c) `0.691` · d) `0.562` · e) `-0.574` · f) `0`.

**Démarche.** Les distances utiles : $AB = 2$, $AC = \sqrt{5}$, $AD = \sqrt{37}$, $AF = \sqrt{58}$, $BC = \sqrt{5}$, $BD = \sqrt{17}$, $BF = \sqrt{34}$, $CD = \sqrt{26}$, $CF = \sqrt{37}$, $DF = \sqrt{5}$.
- a) $a(A) = \frac{2 + \sqrt{5}}{2} \approx 2{,}1180$.
- b) $b(A) = \frac{\sqrt{37} + \sqrt{58}}{2} \approx \frac{6{,}0828 + 7{,}6158}{2} \approx 6{,}8493$.
- c) $s(A) = \frac{6{,}8493 - 2{,}1180}{6{,}8493} \approx 0{,}691$.
- d) $a(D) = \sqrt{5} \approx 2{,}2361$ et $b(D) = \frac{\sqrt{37} + \sqrt{17} + \sqrt{26}}{3} \approx 5{,}1016$, d'où $s(D) \approx 0{,}562$.
- e) $B$ dans le second cluster : $a(B) = \frac{\sqrt{17} + \sqrt{34}}{2} \approx 4{,}9770$ et $b(B) = \frac{2 + \sqrt{5}}{2} \approx 2{,}1180$, d'où $s(B) = \frac{2{,}1180 - 4{,}9770}{4{,}9770} \approx -0{,}574$.
- f) 0, par convention.

Pour la copie : le signe de e) se prévoit : $B$ est bien plus près de $A$ et $C$ que de $D$ et $F$, donc $b(B) < a(B)$. Pour $D$, $a(D) \approx 2{,}24$ est voisin de $a(A) \approx 2{,}12$ ; c'est $b$ qui fait la différence : $D$ est bien plus près du premier cluster ($b(D) \approx 5{,}10$) que $A$ ne l'est du second ($b(A) \approx 6{,}85$).

**Erreurs fréquentes.** Compter le point lui-même dans $a(i)$ (a : 1,412) ; diviser par $a$ au lieu de $\max(a, b)$ (c : 2,234) ; inverser $a$ et $b$ (un signe changé).

**Variante.** $s(F)$ ? *Réponse* : $a(F) = \sqrt{5}$, $b(F) = \frac{\sqrt{58} + \sqrt{34} + \sqrt{37}}{3} \approx 6{,}5098$, d'où $s(F) \approx 0{,}657$.

### Ex M07.11 — k-means++ : des probabilités de tirage proportionnelles à D²

**Réponses** : a) `[0, 1, 9, 20, 50]` · b) `"5/8"` · c) `"1/80"` · d) `[0, 1, 9, 10, 0]` · e) `"1/2"` · f) `"1/4"`.

**Démarche.**
- a) Les carrés des distances à $P_1 = (0, 0)$ : $0$, $1$, $9$, $16 + 4 = 20$, $25 + 25 = 50$ ; somme 80.
- b) $\frac{50}{80} = \frac{5}{8}$ ; c) $\frac{1}{80}$.
- d) Chaque point garde la plus petite des distances au carré à $P_1$ et à $P_5$ : $P_2$ : $\min(1, 41) = 1$ ; $P_3$ : $\min(9, 29) = 9$ ; $P_4$ : $\min(20, 1 + 9) = 10$ ; somme 20.
- e) $\frac{10}{20} = \frac{1}{2}$.
- f) Tirage uniforme parmi $P_2$ à $P_5$ : $\frac{1}{4}$.

Pour la copie : $P_2$ est collé à $P_1$ ; deux centres si proches se partageraient le même groupe et laisseraient un autre groupe sans centre. k-means++ rend ce mauvais choix 20 fois moins probable qu'un tirage uniforme ($\frac{1}{80}$ contre $\frac{1}{4}$). Revers de la médaille : un point aberrant, très loin de tout, a un grand $D^2$ et sera souvent choisi comme centre.

**Erreurs fréquentes.** Prendre les distances au lieu de leurs carrés (a) ; garder la distance au premier centre en d) au lieu de la distance au centre le plus proche ; compter $P_1$ parmi les candidats en f) ($\frac{1}{5}$).

**Variante.** Après le choix de $P_5$, la probabilité que le troisième centre soit $P_3$ ? *Réponse* : $\frac{9}{20}$.

### Ex M07.12 — La diagonale du cube unité et son angle avec les axes, quand d grandit

**Réponses** : a) `2` · b) `7.0711` · c) `60` · d) `84.26` · e) `34` · f) `"4/5"`.

**Démarche.**
- a) $\sqrt{4} = 2$ ; b) $\sqrt{50} \approx 7{,}0711$.
- c) $\cos\theta = \frac{\mathbf{1} \cdot \mathbf{e}_1}{\sqrt{4} \times 1} = \frac{1}{2}$, donc $60°$ ; d) $\cos\theta = \frac{1}{10}$, $\theta \approx 84{,}26°$.
- e) $\frac{1}{\sqrt{d}} < \cos 80° \approx 0{,}1736$ demande $d > 33{,}2$ : en dimension 33, l'angle vaut 79,98° ; en dimension 34, 80,13°.
- f) $\mathbf{1} \cdot (1, \ldots, 1, -1) = 9 - 1 = 8$, et les deux normes valent $\sqrt{10}$ : $\cos = \frac{8}{10} = \frac{4}{5}$.

Pour la copie : en dimension $d$, ce cosinus vaut $\frac{d - 2}{d}$, qui tend vers 1 : les deux directions se rapprochent. Vus depuis le centre du cube, deux sommets voisins diffèrent par une seule coordonnée sur $d$ : ils font un angle qui tend vers 0, alors que chaque sommet fait un angle qui tend vers 90° avec chaque axe.

**Erreurs fréquentes.** Oublier la racine (a : 4 ; b : 50) ; l'angle en radians ; s'arrêter à 33 en e) ; compter la coordonnée $-1$ comme $+1$ en f) ($\frac{9}{10}$).

**Variante.** La longueur de la diagonale du cube $[0, 2]^{25}$ ? *Réponse* : $\lVert (2, \ldots, 2) \rVert = 2\sqrt{25} = 10$.

### Ex M07.13 — La distance au carré moyenne de deux points tirés dans le cube [0, 1]ᵈ

**Réponses** : a) `"1/3"` · b) `"1/4"` · c) `"1/6"` · d) `2` · e) `10` · f) `0.408`.

**Démarche.**
- a) $\mathbb{E}[U^2] = \int_0^1 x^2\,dx = \frac{1}{3}$ (M02a).
- b) Par indépendance, $\mathbb{E}[UV] = \mathbb{E}[U]\,\mathbb{E}[V] = \frac{1}{4}$ (M02b).
- c) $\mathbb{E}[(U - V)^2] = \mathbb{E}[U^2] - 2\,\mathbb{E}[UV] + \mathbb{E}[V^2] = \frac{1}{3} - \frac{1}{2} + \frac{1}{3} = \frac{1}{6}$.
- d) $\lVert \mathbf{X} - \mathbf{Y} \rVert^2 = \sum_{j=1}^{d} (X_j - Y_j)^2$ : par linéarité, $\mathbb{E} = \frac{d}{6}$, soit 2 pour $d = 12$.
- e) $\sqrt{\frac{600}{6}} = 10$.
- f) $\frac{\sqrt{d/6}}{\sqrt{d}} = \frac{1}{\sqrt{6}} \approx 0{,}408$.

Pour la copie : $\mathbb{E}[U - V] = 0$ et $\mathbb{V}(U - V) = \mathbb{V}(U) + \mathbb{V}(V) = \frac{1}{12} + \frac{1}{12} = \frac{1}{6}$, donc $\mathbb{E}[(U - V)^2] = \mathbb{V}(U - V) + \mathbb{E}[U - V]^2 = \frac{1}{6}$. Le rapport f) ne dépend pas de $d$ : deux points pris au hasard sont typiquement à 41 % de la diagonale l'un de l'autre, en toute dimension. Mais la dispersion de $\lVert \mathbf{X} - \mathbf{Y} \rVert^2$ ne grandit que comme $\sqrt{d}$ : en grande dimension, presque toutes les distances sont proches de $\sqrt{d/6}$ (fiche §7).

**Erreurs fréquentes.** Prendre $\mathbb{E}[U]^2$ pour $\mathbb{E}[U^2]$ (a : $\frac{1}{4}$) ; oublier le double produit (c : $\frac{2}{3}$) ou prendre la variance de $U$ ($\frac{1}{12}$) ; oublier la racine en e).

**Variante.** $\mathbb{E}\big[\lVert \mathbf{X} \rVert^2\big]$, pour un point uniforme du cube $[0, 1]^{30}$ ? *Réponse* : $30 \times \frac{1}{3} = 10$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M07.14 — L'inégalité de Cauchy-Schwarz, par le discriminant

**Réponse modèle.**
1. Par la linéarité du produit scalaire : $q(t) = (\mathbf{u} + t\mathbf{v}) \cdot (\mathbf{u} + t\mathbf{v}) = \lVert \mathbf{v} \rVert^2\,t^2 + 2\,(\mathbf{u} \cdot \mathbf{v})\,t + \lVert \mathbf{u} \rVert^2$. Donc $\alpha = \lVert \mathbf{v} \rVert^2$, $\beta = 2\,\mathbf{u} \cdot \mathbf{v}$, $\gamma = \lVert \mathbf{u} \rVert^2$.
2. $q(t)$ est le carré d'une norme, donc $q(t) \ge 0$ pour tout $t$. Comme $\alpha > 0$ ($\mathbf{v} \ne \mathbf{0}$), $q$ est un trinôme du second degré ; s'il avait un discriminant strictement positif, il aurait deux racines distinctes et serait strictement négatif entre elles (R3). Donc $\Delta = 4(\mathbf{u} \cdot \mathbf{v})^2 - 4\lVert \mathbf{u} \rVert^2\lVert \mathbf{v} \rVert^2 \le 0$, soit $(\mathbf{u} \cdot \mathbf{v})^2 \le \lVert \mathbf{u} \rVert^2\lVert \mathbf{v} \rVert^2$, et, en prenant les racines carrées de ces nombres positifs, $|\mathbf{u} \cdot \mathbf{v}| \le \lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert$.
3. Si $\mathbf{v} = \mathbf{0}$, les deux membres sont nuls : l'inégalité est vraie, avec égalité (et $\mathbf{v} = 0\,\mathbf{u}$ est colinéaire à $\mathbf{u}$).
4. Si $\mathbf{u} = \lambda\mathbf{v}$, alors $|\mathbf{u} \cdot \mathbf{v}| = |\lambda|\,\lVert \mathbf{v} \rVert^2 = \lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert$ : égalité. Réciproquement, si l'égalité a lieu (avec $\mathbf{v} \ne \mathbf{0}$), alors $\Delta = 0$ : $q$ a une racine double $t_0$, et $q(t_0) = \lVert \mathbf{u} + t_0\mathbf{v} \rVert^2 = 0$, donc $\mathbf{u} = -t_0\,\mathbf{v}$ : $\mathbf{u}$ et $\mathbf{v}$ sont colinéaires.
5. Avec ces vecteurs, $\mathbf{u} \cdot \mathbf{v} = \sum_i |x_i| = \lVert \mathbf{x} \rVert_1$, $\lVert \mathbf{u} \rVert = \sqrt{\sum x_i^2} = \lVert \mathbf{x} \rVert_2$ et $\lVert \mathbf{v} \rVert = \sqrt{n}$. Cauchy-Schwarz donne $\lVert \mathbf{x} \rVert_1 \le \sqrt{n}\,\lVert \mathbf{x} \rVert_2$, avec égalité si et seulement si $(|x_1|, \ldots, |x_n|)$ est colinéaire à $(1, \ldots, 1)$ : toutes les coordonnées ont la même valeur absolue.
6. $\mathbf{u} \cdot \mathbf{v} = 2 + 0 + 3 = 5$ et $\lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert = \sqrt{11}\sqrt{5} = \sqrt{55} \approx 7{,}42$ : $5 \le 7{,}42$. Et $\lVert \mathbf{u} \rVert_1 = 5 \le \sqrt{3}\sqrt{11} = \sqrt{33} \approx 5{,}74$.

**Grille.** (1) le développement juste, avec $\alpha$, $\beta$ et $\gamma$ ; (2) l'argument « trinôme toujours positif, donc discriminant négatif ou nul », en utilisant $\alpha > 0$, et le passage aux racines carrées ; (3) le cas $\mathbf{v} = \mathbf{0}$ ; (4) les **deux** sens de l'équivalence ; (5) le choix des vecteurs, le calcul des trois quantités, le cas d'égalité ; (6) les deux vérifications numériques.

### Ex M07.15 — L'inégalité triangulaire pour L2, L1 et L∞

**Réponse modèle.**
1. $\lVert \mathbf{u} + \mathbf{v} \rVert_2^2 = \lVert \mathbf{u} \rVert_2^2 + 2\,\mathbf{u} \cdot \mathbf{v} + \lVert \mathbf{v} \rVert_2^2 \le \lVert \mathbf{u} \rVert_2^2 + 2\,\lVert \mathbf{u} \rVert_2\lVert \mathbf{v} \rVert_2 + \lVert \mathbf{v} \rVert_2^2 = \big(\lVert \mathbf{u} \rVert_2 + \lVert \mathbf{v} \rVert_2\big)^2$, par Cauchy-Schwarz ($\mathbf{u} \cdot \mathbf{v} \le |\mathbf{u} \cdot \mathbf{v}| \le \lVert \mathbf{u} \rVert_2\lVert \mathbf{v} \rVert_2$). Les deux membres sont positifs : on peut prendre les racines carrées.
2. Pour chaque $i$, $|u_i + v_i| \le |u_i| + |v_i|$ ; en additionnant, $\lVert \mathbf{u} + \mathbf{v} \rVert_1 \le \lVert \mathbf{u} \rVert_1 + \lVert \mathbf{v} \rVert_1$.
3. Pour chaque $i$, $|u_i + v_i| \le |u_i| + |v_i| \le \lVert \mathbf{u} \rVert_\infty + \lVert \mathbf{v} \rVert_\infty$ ; le plus grand des $|u_i + v_i|$ est donc lui aussi au plus $\lVert \mathbf{u} \rVert_\infty + \lVert \mathbf{v} \rVert_\infty$.
4. $\lVert \mathbf{u} \rVert = \lVert (\mathbf{u} - \mathbf{v}) + \mathbf{v} \rVert \le \lVert \mathbf{u} - \mathbf{v} \rVert + \lVert \mathbf{v} \rVert$, donc $\lVert \mathbf{u} \rVert - \lVert \mathbf{v} \rVert \le \lVert \mathbf{u} - \mathbf{v} \rVert$. En échangeant les rôles, $\lVert \mathbf{v} \rVert - \lVert \mathbf{u} \rVert \le \lVert \mathbf{v} - \mathbf{u} \rVert = \lVert \mathbf{u} - \mathbf{v} \rVert$. Les deux ensemble donnent la valeur absolue.
5. $N(\mathbf{x}) \ge 0$, et $N(\mathbf{x}) = 0$ seulement si $\sqrt{|x_1|} + \sqrt{|x_2|} = 0$, c'est-à-dire $\mathbf{x} = \mathbf{0}$. $N(\lambda\mathbf{x}) = \big(\sqrt{|\lambda|}\sqrt{|x_1|} + \sqrt{|\lambda|}\sqrt{|x_2|}\big)^2 = |\lambda|\,N(\mathbf{x})$. Mais $N(\mathbf{e}_1) = N(\mathbf{e}_2) = 1$ et $N(\mathbf{e}_1 + \mathbf{e}_2) = (1 + 1)^2 = 4 > 2$ : l'inégalité triangulaire est fausse.

**Grille.** (1) le développement, Cauchy-Schwarz au bon endroit, la justification du passage aux racines ; (2) l'inégalité des réels coordonnée par coordonnée, puis la somme ; (3) la majoration de **chaque** coordonnée avant le maximum ; (4) l'écriture $\mathbf{u} = (\mathbf{u} - \mathbf{v}) + \mathbf{v}$, et les deux sens ; (5) positivité, homogénéité, puis un contre-exemple chiffré.

### Ex M07.16 — La moyenne minimise la somme des carrés des distances, en dimension n

**Réponse modèle.**
1. $\sum_i (\mathbf{x}_i - \bar{\mathbf{x}}) = \sum_i \mathbf{x}_i - m\,\bar{\mathbf{x}} = m\,\bar{\mathbf{x}} - m\,\bar{\mathbf{x}} = \mathbf{0}$.
2. $\lVert \mathbf{x}_i - \mathbf{c} \rVert^2 = \lVert \mathbf{x}_i - \bar{\mathbf{x}} \rVert^2 + 2\,(\mathbf{x}_i - \bar{\mathbf{x}}) \cdot (\bar{\mathbf{x}} - \mathbf{c}) + \lVert \bar{\mathbf{x}} - \mathbf{c} \rVert^2$. En additionnant sur $i$, le terme du milieu donne $2\,\big(\sum_i (\mathbf{x}_i - \bar{\mathbf{x}})\big) \cdot (\bar{\mathbf{x}} - \mathbf{c}) = 2\,\mathbf{0} \cdot (\bar{\mathbf{x}} - \mathbf{c}) = 0$ (linéarité, et 1), et le dernier, qui ne dépend pas de $i$, est compté $m$ fois.
3. Dans la formule, le premier terme ne dépend pas de $\mathbf{c}$, et le second, $m\,\lVert \bar{\mathbf{x}} - \mathbf{c} \rVert^2$, est positif ou nul, nul seulement si $\mathbf{c} = \bar{\mathbf{x}}$. Le minimum est donc atteint en $\bar{\mathbf{x}}$ et en ce seul point.
4. $\sum_i \omega_i \lVert \mathbf{x}_i - \mathbf{c} \rVert^2 = \sum_i \omega_i \lVert \mathbf{x}_i - \bar{\mathbf{x}}_\omega \rVert^2 + \Omega\,\lVert \bar{\mathbf{x}}_\omega - \mathbf{c} \rVert^2$. Même preuve : $\sum_i \omega_i (\mathbf{x}_i - \bar{\mathbf{x}}_\omega) = \sum_i \omega_i \mathbf{x}_i - \Omega\,\bar{\mathbf{x}}_\omega = \mathbf{0}$ par définition de $\bar{\mathbf{x}}_\omega$, ce qui annule les doubles produits, et le dernier terme se compte avec les poids, $\sum_i \omega_i = \Omega$.
5. $J(\mathbf{c}) = \sum_i \sum_j (x_{ij} - c_j)^2$, donc $\frac{\partial J}{\partial c_j} = -2\sum_i (x_{ij} - c_j) = -2\big(\sum_i x_{ij} - m\,c_j\big)$, nul si et seulement si $c_j = \frac{1}{m}\sum_i x_{ij}$ : l'unique point critique est $\bar{\mathbf{x}}$. C'est un minimum : $J$ est une somme, sur les coordonnées $j$, de paraboles tournées vers le haut en $c_j$ (les dérivées secondes valent $2m > 0$ et les dérivées croisées sont nulles), et $J$ tend vers l'infini quand $\mathbf{c}$ s'éloigne.

**Grille.** (1) le calcul de la somme ; (2) le découpage, le développement, l'annulation du double produit **justifiée** par 1, le facteur $m$ ; (3) le minimum **et** son unicité ; (4) l'énoncé avec $\Omega$ et la propriété qui annule les doubles produits ; (5) le gradient, l'unique point critique, et un argument pour le minimum.

### Ex M07.17 — La distance d'un point à un hyperplan vaut |w · x + b| / ‖w‖

**Réponse modèle.**
1. $\mathbf{w} \cdot (\mathbf{x}_0 - t\,\mathbf{w}) + b = 0$ s'écrit $\mathbf{w} \cdot \mathbf{x}_0 + b - t\,\lVert \mathbf{w} \rVert^2 = 0$, d'où $t = \frac{\mathbf{w} \cdot \mathbf{x}_0 + b}{\lVert \mathbf{w} \rVert^2}$ (on peut diviser : $\mathbf{w} \ne \mathbf{0}$) et $\mathbf{x}_H = \mathbf{x}_0 - \frac{\mathbf{w} \cdot \mathbf{x}_0 + b}{\lVert \mathbf{w} \rVert^2}\,\mathbf{w}$.
2. $\lVert \mathbf{x}_0 - \mathbf{x}_H \rVert = |t|\,\lVert \mathbf{w} \rVert = \frac{|\mathbf{w} \cdot \mathbf{x}_0 + b|}{\lVert \mathbf{w} \rVert}$.
3. $\mathbf{w} \cdot \mathbf{y} + b = 0$ et $\mathbf{w} \cdot \mathbf{x}_H + b = 0$ : en soustrayant, $\mathbf{w} \cdot (\mathbf{x}_H - \mathbf{y}) = 0$. Or $\mathbf{x}_0 - \mathbf{y} = (\mathbf{x}_0 - \mathbf{x}_H) + (\mathbf{x}_H - \mathbf{y})$, où $\mathbf{x}_0 - \mathbf{x}_H = t\,\mathbf{w}$ est orthogonal à $\mathbf{x}_H - \mathbf{y}$. Par Pythagore (fiche §2), $\lVert \mathbf{x}_0 - \mathbf{y} \rVert^2 = \lVert \mathbf{x}_0 - \mathbf{x}_H \rVert^2 + \lVert \mathbf{x}_H - \mathbf{y} \rVert^2 \ge \lVert \mathbf{x}_0 - \mathbf{x}_H \rVert^2$, avec égalité seulement pour $\mathbf{y} = \mathbf{x}_H$. La plus petite distance de $\mathbf{x}_0$ à un point de $H$ est donc $\lVert \mathbf{x}_0 - \mathbf{x}_H \rVert$, la valeur de 2.
4. $\frac{|\lambda\,\mathbf{w} \cdot \mathbf{x}_0 + \lambda b|}{\lVert \lambda\mathbf{w} \rVert} = \frac{|\lambda|\,|\mathbf{w} \cdot \mathbf{x}_0 + b|}{|\lambda|\,\lVert \mathbf{w} \rVert}$ : le facteur se simplifie (c'est heureux : $(\lambda\mathbf{w}, \lambda b)$ décrit le même hyperplan).
5. Un point $\mathbf{x}_0$ du premier hyperplan vérifie $\mathbf{w} \cdot \mathbf{x}_0 = -b_1$ ; sa distance au second est $\frac{|-b_1 + b_2|}{\lVert \mathbf{w} \rVert} = \frac{|b_1 - b_2|}{\lVert \mathbf{w} \rVert}$, la même pour tous les points du premier : c'est la distance entre les deux hyperplans.

**Grille.** (1) l'équation en $t$, la division justifiée par $\mathbf{w} \ne \mathbf{0}$ ; (2) la norme de $t\,\mathbf{w}$ avec la valeur absolue ; (3) l'orthogonalité de $\mathbf{x}_H - \mathbf{y}$ à $\mathbf{w}$, Pythagore, et la conclusion « le plus proche » ; (4) la simplification, valable aussi pour $\lambda < 0$ ; (5) un point du premier hyperplan et la formule.

### Ex M07.18 — Les deux étapes de k-means font baisser l'inertie, ou la laissent égale

**Réponse modèle.**
1. Les centres étant fixés, $J = \sum_i \lVert \mathbf{x}_i - \boldsymbol{\mu}_{c_i} \rVert^2$ est une somme dont chaque terme ne dépend que de $c_i$. L'affectation choisit pour chaque $i$ le centre le plus proche, donc un terme au plus égal à l'ancien : la somme ne peut pas augmenter.
2. L'affectation étant fixée, $J = \sum_{j=1}^{k} \sum_{i : c_i = j} \lVert \mathbf{x}_i - \boldsymbol{\mu}_j \rVert^2$ : chaque centre n'intervient que dans la somme de son cluster. Par M07.16, cette somme est la plus petite quand $\boldsymbol{\mu}_j$ est le barycentre du cluster : remplacer chaque centre par ce barycentre ne peut pas augmenter $J$. Un cluster vide n'a aucun terme : son centre peut rester où il est sans changer $J$.
3. La suite des inerties décroît (au sens large) et reste positive : elle converge. Avec la règle « un point garde son centre en cas d'égalité », une affectation qui change fait strictement baisser $J$ (au moins un point passe à un centre strictement plus proche), puis la mise à jour ne le fait pas remonter. Après chaque mise à jour, l'inertie ne dépend que de l'affectation (les centres sont les barycentres de ses clusters ; un cluster vide n'a aucun terme). Tant que l'affectation change, cette inertie baisse strictement : une affectation déjà rencontrée ne peut donc pas revenir, elle redonnerait la même inertie. Comme il n'y a que $k^m$ affectations possibles au plus, l'algorithme s'arrête après $k^m$ étapes au plus.
4. Avec les centres $(2{,}5 ;\ 0)$ et $(2{,}5 ;\ 1)$ : $(0, 0)$ et $(5, 0)$ sont à la distance au carré $6{,}25$ du premier et $7{,}25$ du second, ils le rejoignent ; $(0, 1)$ et $(5, 1)$ rejoignent le second. Les barycentres sont $(2{,}5 ;\ 0)$ et $(2{,}5 ;\ 1)$ : les centres ne bougent plus, et l'inertie vaut $4 \times 6{,}25 = 25$. Le découpage en deux côtés courts, $\{(0, 0), (0, 1)\}$ et $\{(5, 0), (5, 1)\}$, de centres $(0 ;\ 0{,}5)$ et $(5 ;\ 0{,}5)$, a l'inertie $4 \times 0{,}25 = 1$. k-means peut donc s'arrêter sur un découpage 25 fois moins bon que le meilleur : c'est un **minimum local**. D'où l'intérêt de bons départs (k-means++) et de plusieurs lancers.

**Grille.** (1) l'argument terme par terme ; (2) le regroupement par cluster, l'appel à M07.16, le cas du cluster vide ; (3) la convergence de la suite, et l'argument de finitude (baisse stricte, nombre fini d'affectations) ; (4) le point fixe vérifié (affectation puis mise à jour), les deux inerties, la conclusion sur les minima locaux.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M07.19 — Pont : changer l'unité d'une feature change le plus proche voisin

**Réponses** : a) `10.02` · b) `30.0` · c) `"A"` · d) `"B"` · e) `[2.844, 1.513]` · f) `"B"`.

**Démarche.**
- a) $\sqrt{10^2 + 0{,}7^2} = \sqrt{100{,}49} \approx 10{,}02$ ; b) $\sqrt{30^2 + 0{,}05^2} \approx 30{,}00$ : $A$ est plus proche.
- d) En kilogrammes : $\sqrt{10^2 + 700^2} \approx 700{,}1$ et $\sqrt{30^2 + 50^2} \approx 58{,}3$ : c'est $B$.
- e) Écarts standardisés : pour $A$, $\big(\frac{10}{20}, \frac{0{,}7}{0{,}25}\big) = (0{,}5 ;\ 2{,}8)$, d'où $\sqrt{0{,}25 + 7{,}84} \approx 2{,}844$ ; pour $B$, $(1{,}5 ;\ 0{,}2)$, d'où $\sqrt{2{,}25 + 0{,}04} \approx 1{,}513$. f) $B$.

Pour la copie : en tonnes, la masse varie de quelques dixièmes, la puissance de dizaines de chevaux : la puissance écrase la masse. En kilogrammes, c'est l'inverse. La standardisation divise chaque écart par l'écart-type de sa feature, exprimé dans la même unité : le résultat est sans unité, et la réponse ne dépend plus du choix des unités. Le centroïde le plus proche, k-means et la silhouette de workbookIA 7 calculent tous des distances euclidiennes : ils demandent des features sur des échelles comparables.

**Erreurs fréquentes.** Diviser par l'écart-type **après** avoir élevé au carré (e) ; croire que l'unité ne change rien parce que les points restent les mêmes.

**Variante.** Avec la puissance en kilowatts (1 ch ≈ 0,735 kW) et la masse en tonnes, quelle voiture est la plus proche ? *Réponse* : $A$ : environ $\sqrt{7{,}35^2 + 0{,}7^2} \approx 7{,}38$ contre $22{,}05$.

### Ex M07.20 — MML §3.1 et §3.2.1 : normes et produit scalaire, en anglais

**Réponse modèle.**
1. *Absolutely homogeneous* : multiplier un vecteur par un nombre multiplie sa norme par la valeur absolue de ce nombre (l'homogénéité de la fiche) ; *triangle inequality* : l'inégalité triangulaire ; *positive definite* : la norme est positive, et nulle seulement pour le vecteur nul (la positivité).
2. La norme de **Manhattan** (L1) et la norme **euclidienne** (L2). Pour $(1, -3, 2, -1)$ : $1 + 3 + 2 + 1 = 7$ et $\sqrt{1 + 9 + 4 + 1} = \sqrt{15} \approx 3{,}873$.
3. Pour la norme de Manhattan, l'ensemble des vecteurs de norme 1 est un carré posé sur la pointe (un losange) ; pour la norme euclidienne, un cercle. La norme L1 donne la plus grande valeur, et son ensemble de norme 1 est **à l'intérieur** du cercle : il faut des vecteurs plus courts pour atteindre la valeur 1.
4. $\mathbf{x}^\top \mathbf{y} = \sum_i x_i y_i$ ; ici $(1, -3, 2, -1)^\top (2, 1, 0, 4) = 2 - 3 + 0 - 4 = -5$.
5. Le **produit scalaire général** (*inner product*), une application bilinéaire symétrique et définie positive. On y reconnaît les propriétés du §2 de la fiche : la linéarité (par rapport à chaque argument), la symétrie et la positivité.
6. Par exemple *absolutely homogeneous* (homogène, en valeur absolue), *positive definite* (défini positif), *dot product* (produit scalaire usuel), *inner product* (produit scalaire général).

**Grille.** (1) les trois noms et leur traduction ; (2) les deux normes et les deux calculs justes ; (3) la description des deux figures et le lien « plus grande norme, plus petite boule » ; (4) la notation $\mathbf{x}^\top \mathbf{y}$ et le calcul ; (5) le mot *inner product* et les trois propriétés ; (6) trois mots traduits. Les réponses sont écrites avec tes mots, pas recopiées.

### Ex M07.21 — MML §3.3 et §3.4 : longueurs, distances, angles et orthogonalité

**Réponse modèle.**
1. La longueur d'un vecteur est la racine du produit scalaire du vecteur avec lui-même ; la distance entre deux vecteurs est la longueur de leur différence. Une fonction de distance s'appelle une **métrique** (*metric*) ; elle est définie positive (positive, et nulle seulement entre un point et lui-même), symétrique, et vérifie l'inégalité triangulaire.
2. L'inégalité de Cauchy-Schwarz apparaît au §3.3, pour un produit scalaire quelconque. Au §3.4, elle garantit que le quotient du produit scalaire par le produit des longueurs est entre $-1$ et 1 : c'est ce qui permet de **définir** l'angle comme l'arccosinus de ce quotient (la même démarche que la fiche §4).
3. $(1, 2, 2) \cdot (2, -1, 2) = 2 - 2 + 4 = 4$, les deux normes valent 3 : $\cos\theta = \frac{4}{9}$ et $\theta \approx 63{,}61°$.
4. Deux vecteurs sont orthogonaux quand leur produit scalaire est nul ; orthonormés quand, en plus, ils sont tous deux de longueur 1.
5. Pour le produit usuel : $1 - 1 = 0$, orthogonaux. Pour $\langle \mathbf{x}, \mathbf{y} \rangle = 2x_1y_1 + x_2y_2$ : $2 - 1 = 1 \ne 0$, pas orthogonaux. Les longueurs valent alors $\sqrt{\langle \mathbf{x}, \mathbf{x} \rangle} = \sqrt{3}$ et $\sqrt{\langle \mathbf{y}, \mathbf{y} \rangle} = \sqrt{3}$, d'où $\cos\theta = \frac{1}{3}$ et $\theta \approx 70{,}53°$. L'orthogonalité dépend du produit scalaire choisi.
6. Par exemple *metric* (distance), *orthonormal* (orthonormé), *angle between two vectors* (angle entre deux vecteurs), *orthogonal matrix* (matrice orthogonale, M12).

**Grille.** (1) longueur et distance à partir du produit scalaire, le mot *metric* et ses trois propriétés ; (2) le rôle de Cauchy-Schwarz dans la définition de l'angle ; (3) le calcul juste ; (4) les deux définitions ; (5) les deux produits, les longueurs pour le second, l'angle, la conclusion ; (6) trois mots traduits.

### Ex M07.22 — Fermi : la mémoire d'un million d'embeddings

**Réponse modèle.**
1. $10^6 \times 768 \times 4 \approx 3 \times 10^9$ octets, soit environ **3 Go** ; en `float16`, environ 1,5 Go. Cela tient dans la mémoire d'un ordinateur portable récent, mais de justesse en `float32`.
2. $10^6 \times 768 \approx 8 \times 10^8$ multiplications (autant d'additions).
3. $\frac{8 \times 10^8}{10^{10}} \approx 0{,}08$ seconde : une recherche exacte est rapide pour un million de documents. Pour un milliard, 1 000 fois plus de documents : environ **80 secondes** par question, et 3 To de mémoire. D'où les méthodes de recherche **approchée**, qui ne comparent la question qu'à une petite partie des vecteurs.
4. La norme de chaque document coûte autant que le produit scalaire lui-même (768 multiplications) : la calculer à chaque question doublerait le travail. Normaliser une fois pour toutes ramène le cosinus à un simple produit scalaire.

**Grille.** Les trois produits posés avec des puissances de 10, des ordres de grandeur justes (3 Go, $10^9$ opérations, $10^{-1}$ s, une à deux minutes pour un milliard), et la raison de la normalisation préalable.

### Ex M07.23 — Expliquer la similarité cosinus à quelqu'un qui a fait le lycée

**Réponse modèle.**

> Imagine chaque profil comme une flèche : une direction par genre de musique, et une longueur par heure d'écoute. Ton frère écoute dix fois plus que toi, sa flèche est dix fois plus longue. Mais si vous écoutez les mêmes genres dans les mêmes proportions, vos flèches pointent dans la même direction. La similarité cosinus ne regarde que l'angle entre les deux flèches : 1 si elles sont alignées, 0 si elles sont à angle droit. À 0,93, vos flèches sont presque alignées : vous avez presque les mêmes goûts, même si vous n'écoutez pas autant. Une similarité de 0 voudrait dire que vous n'écoutez jamais les mêmes genres.

**Grille.** (1) le profil comme une flèche ; (2) le cosinus comme mesure de l'angle, avec ses valeurs 1 et 0 ; (3) la longueur (le temps d'écoute) qui ne compte pas ; (4) le sens d'une similarité de 0 (aucun genre en commun, pour des heures d'écoute qui ne sont jamais négatives) ; huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M07.E1 — Distance euclidienne ou similarité cosinus : laquelle pour comparer des textes ?

**Réponse modèle (60 secondes).**

> La distance euclidienne compare des positions : elle dépend à la fois de la direction et de la longueur des vecteurs. La similarité cosinus ne compare que la direction, l'angle entre les deux vecteurs. Pour des textes, la longueur du vecteur reflète surtout la longueur du document : un long article et un court résumé sur le même sujet ont des vecteurs presque alignés, mais très éloignés au sens euclidien. Je prendrais donc la similarité cosinus. Et si les vecteurs sont normalisés à la norme 1, la question disparaît : pour deux vecteurs unitaires, le carré de la distance vaut deux moins deux fois leur produit scalaire, donc deux fois un moins le cosinus. Les deux mesures classent alors les documents exactement dans le même ordre ; c'est pour cela qu'on normalise souvent les embeddings, puis qu'on utilise un simple produit scalaire, plus rapide.

**Grille.** (1) ce que compare chaque mesure (position, ou direction seule) ; (2) l'effet de la longueur des documents ; (3) le développement $\lVert \mathbf{u} - \mathbf{v} \rVert^2 = 2 - 2\,\mathbf{u} \cdot \mathbf{v} = 2(1 - \cos\theta)$ pour des vecteurs unitaires, et la conséquence (même classement) ; (4) la pratique : normaliser, puis un produit scalaire.

<a id="notebook"></a>

## Notebook

### Ex M07.24 — Normes Lp et similarité cosinus · `norm_p, cosine_similarity`

**Réponses** : a) `9.0` · b) `5.0` · c) `4.0` · d) `4.327` · e) `"ValueError"` · f) `0.6667` · g) `"ValueError"` · h) `"float"`.

**Démarche.** `norm_p` : `x = np.array(x, dtype=float)`, une `ValueError` si `x.ndim != 1` ou `x.size == 0`, ou si `not p >= 1` (ce test refuse aussi `nan`) ; puis trois cas : `p` infini (`math.isinf(p)`) donne `float(np.max(np.abs(x)))`, `p == 1` donne la somme des valeurs absolues, sinon `float(np.sum(np.abs(x) ** p) ** (1 / p))`. `cosine_similarity` : les deux vecteurs en flottants, une `ValueError` si les longueurs diffèrent ou si une norme est nulle, puis `float(np.clip(np.sum(u * v) / (nu * nv), -1, 1))`. Pour la copie : a) $1 + 2 + 2 + 4 = 9$ ; b) $\sqrt{25} = 5$ ; c) 4 ; d) $81^{1/3} \approx 4{,}327$ ; f) $\frac{4}{\sqrt{6}\sqrt{6}} = \frac{2}{3}$. La norme diminue quand $p$ augmente : la plus grande coordonnée pèse de plus en plus. Sans `np.clip`, le cosinus d'un vecteur avec lui-même vaut souvent 1,0000000000000002 (les arrondis du numérateur et du dénominateur ne se compensent pas exactement : environ un vecteur gaussien sur quatre en dimension 5), et `np.arccos` de ce nombre donne `nan`.

**Erreurs fréquentes.** Oublier les valeurs absolues (d : avec des signes, $|1 - 8 + 8 - 64|^{1/3}$) ; oublier la puissance $\frac{1}{p}$ (d : 81) ; tester `p == float("inf")` sur un `np.inf` (cela marche, mais `math.isinf` est plus sûr) ; diviser par une seule des deux normes (f) ; laisser passer un vecteur nul (g : `nan` ou `ZeroDivisionError`) ; renvoyer un `numpy.float64` (h).

### Ex M07.25 — La projection sur une droite · `project_onto_line`

**Réponses** : a) `[1.3333, 1.3333, 1.3333]` · b) `0.0` · c) `[0.0, 5.0]` · d) `[4.0, 0.0, 0.0, 0.0]` · e) `"ValueError"` · f) `"ndarray"`.

**Démarche.** `x` et `u` en flottants, une `ValueError` si les longueurs diffèrent ou si `u · u == 0`, puis `(np.sum(x * u) / np.sum(u * u)) * u`. Pour la copie : a) $\frac{4}{3}(1, 1, 1)$ ; c) $\frac{-15}{9}(0, -3) = (0, 5)$ : projeter sur un axe garde la coordonnée de cet axe ; le sens de $\mathbf{u}$ ne compte pas, car $\mathbf{u}$ apparaît deux fois dans la formule (les deux signes moins se compensent).

**Erreurs fréquentes.** Diviser par $\lVert \mathbf{u} \rVert$ au lieu de $\mathbf{u} \cdot \mathbf{u}$ (a : $\frac{4}{\sqrt{3}}$ ; c : `[0, 15]`) ; oublier de diviser (c : `[0, 45]`) ; renvoyer une liste (f).

### Ex M07.26 — Barycentre et somme des carrés des distances · `centroid, sum_sq_distances_to`

**Réponses** : a) `[2.0, 3.0]` · b) `[0.5, 2.0]` · c) `40.0` · d) `92.0` · e) `"ValueError"` · f) `"float"`.

**Démarche.** `centroid` : `points` en tableau 2-D (une `ValueError` s'il est vide), des poids égaux à 1 par défaut, une `ValueError` si leur forme n'est pas `(n,)`, si l'un est négatif (`not np.all(w >= 0)`, qui refuse aussi `nan`) ou si leur somme n'est pas positive ; puis `np.sum(w[:, None] * points, axis=0) / w.sum()`. `sum_sq_distances_to` : `float(np.sum((points - c) ** 2))`, après avoir vérifié que `c` a une coordonnée par colonne. Pour la copie : a) $\big(\frac{8}{4}, \frac{12}{4}\big) = (2, 3)$ ; b) $\frac{(1, 4) + (3, 0) + 2\,(-1, 2)}{4} = (0{,}5 ;\ 2)$ : le dernier point a un poids nul, il disparaît du numérateur comme du dénominateur ; c) $2 + 10 + 10 + 18 = 40$ ; d) $17 + 9 + 5 + 61 = 92 = 40 + 4 \times 13$ (König-Huygens, avec $\lVert (2, 3) \rVert^2 = 13$).

**Erreurs fréquentes.** Oublier `[:, None]` (les poids ne se multiplient pas ligne par ligne) ; diviser par le nombre de points au lieu de la somme des poids ; additionner des distances au lieu de leurs carrés (c) ; accepter un poids négatif (e).

### Ex M07.27 — Côté d'un hyperplan et distance à un hyperplan · `side_of_hyperplane, distance_to_hyperplane`

**Réponses** : a) `[1, 1, -1, -1]` · b) `[0.6667, 0.3333, 0.6667, 1.0]` · c) `[0.6667, 0.3333, -0.6667, -1.0]` · d) `"int"` · e) `0.6667` · f) `"ValueError"`.

**Démarche.** Une fonction auxiliaire calcule les scores : `w` en vecteur (une `ValueError` s'il est nul), `x` en tableau, une `ValueError` si `x.shape[-1] != w.size`, puis `np.sum(x * w, axis=-1) + b`, qui donne un nombre pour un point et un tableau pour plusieurs. `side_of_hyperplane` : `np.sign(scores).astype(int)`, puis `int(...)` pour un point. `distance_to_hyperplane` : `scores / sqrt(w · w)`, `np.abs` sauf si `signed`, puis `float(...)` pour un point. Pour la copie : les scores valent $2, 1, -2, -3$ et $\lVert \mathbf{w} \rVert = 3$. L'origine a le score $b = 1 > 0$ : côté positif, à la distance $\frac{1}{3}$.

**Erreurs fréquentes.** Oublier de diviser par $\lVert \mathbf{w} \rVert$ (b : les scores) ou diviser par $\lVert \mathbf{w} \rVert^2$ ; oublier la valeur absolue (b) ou la garder avec `signed=True` (c) ; renvoyer un `numpy.int64` ou un tableau pour un seul point (d) ; laisser passer un vecteur normal nul (f).

### Ex M07.28 — `np.linalg.norm` (ord = 1, 2, inf) et `scipy.spatial.distance` contre tes fonctions

**Réponses** : a) `10` · b) `3` · c) `5.099` · d) `0.7631` · e) `3` · f) `True`.

**Démarche.** `spd.cityblock(a, b)`, `spd.chebyshev(a, b)`, `spd.euclidean(a, b)`, `spd.cosine(a, b)`, `np.linalg.norm(a, ord=np.inf)` ; puis une boucle sur 20 vecteurs et quatre valeurs de $p$, avec `np.isclose(mymath.vectors.norm_p(x, p), np.linalg.norm(x, ord=p))`. Pour la copie : $\mathbf{a} \cdot \mathbf{b} = 4$, $\cos\theta = \frac{4}{\sqrt{15}\sqrt{19}} \approx 0{,}2369$, et la distance cosinus vaut $1 - 0{,}2369 \approx 0{,}7631$. Une **distance** vaut 0 entre deux points identiques et grandit quand ils s'éloignent : c'est ce qu'attendent les fonctions qui cherchent des plus proches voisins ou regroupent des points.

**Erreurs fréquentes.** Lire `spd.cosine` comme une similarité (d : 0,2369) ; confondre `cityblock` (L1) et `chebyshev` (L∞).

### Ex M07.29 — Prédire : l'angle de deux vecteurs tirés au hasard en dimension 1 000

**Réponses** : a) `3` · b) `3` · c) `2` · d) `1`.

**Démarche.** L'expérience donne, en dimension 1 000, un angle moyen de 90° avec un écart-type d'environ 1,8°, et 99,6 % des angles entre 85° et 95° ; en dimension 10, un écart-type d'environ 19° ; en dimension 2, un angle réparti uniformément (moyenne 90°, écart-type 52°, celui d'une loi uniforme sur $[0°, 180°]$). L'écart-type du cosinus est d'environ $\frac{1}{\sqrt{d}}$ : en dimension 1 000, $0{,}032$ radian, soit 1,8°. Des *embeddings* de dimension 768 sans structure seraient presque tous orthogonaux deux à deux : leurs cosinus ne diraient rien. C'est parce que les vrais *embeddings* ont de la structure que leurs cosinus sont informatifs.

### Ex M07.30 — La norme d'un vecteur gaussien se concentre autour de √d

**Réponses** : a) `1.0` · b) `0.71` · c) `0.6` · d) `-0.5`.

**Démarche.** `norms = np.sqrt(np.sum(X ** 2, axis=1))`, puis `(float(norms.mean() / math.sqrt(X.shape[1])), float(norms.std()))`. Pour la copie : d) la dispersion relative (l'écart-type divisé par $\sqrt{d}$) décroît comme $d^{-1/2}$ : en dimension 1 000, la norme est connue à environ 2 % près. c) En dimension 1, la norme est $|Z|$, d'écart-type $\sqrt{1 - \frac{2}{\pi}} \approx 0{,}603$. b) L'écart-type de la norme tend vers $\frac{1}{\sqrt{2}} \approx 0{,}707$ : $\lVert \mathbf{X} \rVert^2$ a un écart-type $\sqrt{2d}$, et la racine divise l'écart par environ $2\sqrt{d}$.

**Erreurs fréquentes.** Une norme par colonne au lieu d'une norme par ligne (`axis=0`) ; oublier de diviser la moyenne par $\sqrt{d}$ (a) ; diviser aussi l'écart-type par $\sqrt{d}$ (b).

### Ex M07.31 — Médiane ou moyenne : le centre qui minimise les distances L1 ou leurs carrés, face à des points aberrants

**Réponses** : a) `[2.0, 2.0]` · b) `[2.5556, 2.5556]` · c) `[3.0, 2.0]` · d) `[9.1818, 2.3636]` · e) `6.629` · f) `1.0` · g) `1.417`.

**Démarche.** `l1_center` : `np.median(points, axis=0)` ; `l1_cost` : `float(np.sum(np.abs(points - c)))`. Pour la copie : la médiane ne dépend que du **rang** des valeurs : deux valeurs extrêmes, aussi grandes soient-elles, ne la décalent que d'une place ou deux. La moyenne, elle, additionne les valeurs : 40 et 38 l'attirent loin du troupeau. La médiane décrit mieux le troupeau. g) confirme que la médiane fait mieux que le barycentre pour la somme des distances L1 : le barycentre coûte 42 % de plus.

**Erreurs fréquentes.** `np.median(points)` sans `axis` : une seule valeur pour tout le tableau ; `axis=1` : une médiane par point.

### Ex M07.32 — Les boules unités L1, L2, L∞ et Lp dans le plan

**Démarche.** Des directions `np.column_stack([np.cos(t), np.sin(t)])` pour 401 angles de 0 à $2\pi$ (le dernier ferme la courbe), chacune divisée par sa norme $L^p$ (`np.max(np.abs(...), axis=1)` pour L∞), puis `ax.plot(xs, ys, **style)`. Les courbes s'emboîtent : losange à l'intérieur, carré à l'extérieur, ce qui traduit $\lVert \mathbf{x} \rVert_\infty \le \lVert \mathbf{x} \rVert_2 \le \lVert \mathbf{x} \rVert_1$ (une plus grande norme donne une plus petite boule). La courbe de $p = \frac{1}{2}$ est creusée vers l'intérieur : le milieu $(\frac{1}{2}, \frac{1}{2})$ du segment qui joint $(1, 0)$ et $(0, 1)$, deux de ses points, est **hors** de la boule. La boule unité d'une norme est toujours convexe (M10) : c'est l'inégalité triangulaire en image.

**Erreurs fréquentes.** Diviser les deux coordonnées par la norme L2 quel que soit $p$ (on obtient toujours le cercle) ; des angles de 0 à $\pi$ seulement (une demi-courbe) ; ouvrir une figure dans la fonction (`plt.subplots`) au lieu de dessiner dans `ax`.

### Ex M07.33 — Chasse à l'erreur : une distance sans racine, un cosinus mal normalisé, une projection sur un vecteur non unitaire

**Réponses** : a) `"ACE"` · b) `[6.403, 11, -0.175, 4.583, -0.802, 4]`.

**Démarche.** (A) oublie la racine : la somme des carrés vaut 41, la distance $\sqrt{41} \approx 6{,}403$. (C) ne divise que par $\lVert \mathbf{a} \rVert$ : $\mathbf{a} \cdot \mathbf{b} = 4 - 3 - 4 = -3$, d'où le cosinus $\frac{-3}{\sqrt{14}\sqrt{21}} \approx -0{,}175$. (E) divise par $\lVert \mathbf{a} \rVert^2$ : c'est le **coefficient** $t$ de la projection ($\mathbf{p} = t\,\mathbf{a}$) ; la composante, une longueur avec un signe, vaut $\frac{-3}{\sqrt{14}} \approx -0{,}802$. (B) $3 + 4 + 4 = 11$, (D) $\sqrt{21} \approx 4{,}583$ et (F) $\max(3, 4, 4) = 4$ sont justes.

**Erreurs fréquentes.** Croire (E) juste parce que la formule ressemble à celle de la projection ; citer (D), qui est juste.

### Ex M07.34 — Les normes de toutes les lignes d'un tableau : axis, keepdims et broadcasting

**Démarche.** `row_norms` : `A = np.abs(np.asarray(X, dtype=float))`, puis `np.max(A, axis=1)` pour L∞, sinon `np.sum(A ** p, axis=1) ** (1 / p)`. `normalize_rows` : `norms = np.sqrt(np.sum(X ** 2, axis=1, keepdims=True))` (forme `(n, 1)`), puis `np.where(norms > 0, X / np.where(norms > 0, norms, 1.0), 0.0)` : le `np.where` intérieur évite la division par zéro, l'extérieur laisse la ligne nulle à zéro. Pour la copie : `axis=0` additionne les **colonnes** (une valeur par feature) ; sans `keepdims`, les normes, de forme `(n,)`, s'alignent sur la **dernière** dimension de `X` : une erreur de forme si $p \ne n$, et une division des colonnes sans message d'erreur quand `X` est carré. La version vectorisée est en général une dizaine de fois plus rapide que la boucle, souvent davantage (la mesure de la dernière cellule).

**Erreurs fréquentes.** `axis=0` ; oublier `keepdims=True` ; diviser par une norme nulle (des `nan`) ; une boucle Python.

### Ex M07.35 — Défi : le point qui minimise la somme des distances (non au carré) à 60 villes, à 0,1 % près

**Réponse** : `328.2` (la somme des distances au point trouvé, pour `CITIES_35`).

**Démarche.** L'algorithme de Weiszfeld (1937) : partir du barycentre $\mathbf{c}$, puis répéter $\mathbf{c} \leftarrow \frac{\sum_i \mathbf{x}_i / d_i}{\sum_i 1 / d_i}$, où $d_i = \lVert \mathbf{x}_i - \mathbf{c} \rVert$ (avec un plancher, par exemple $10^{-12}$, si $\mathbf{c}$ tombe sur une ville). Quelques centaines d'itérations suffisent largement. L'idée : le gradient de $\sum_i \lVert \mathbf{c} - \mathbf{x}_i \rVert$ est $\sum_i \frac{\mathbf{c} - \mathbf{x}_i}{\lVert \mathbf{c} - \mathbf{x}_i \rVert}$, une somme de vecteurs **unitaires** ; l'annuler revient à écrire $\mathbf{c}$ comme le barycentre des villes pondérées par $\frac{1}{d_i}$, et l'on itère cette équation. Pour la copie : pour `CITIES_35`, le barycentre fait environ 0,6 % de plus que le minimum, la médiane coordonnée par coordonnée environ 1,9 %. Le point trouvé est plus près du groupe de 26 villes (à environ 3,8 km de son centre, contre 6,2 et 6,7 km pour les deux autres groupes) que ne l'est le barycentre (4,9 km) : chaque ville tire avec une force égale (un vecteur unitaire), quelle que soit sa distance, et le groupe le plus nombreux l'emporte ; dans le barycentre, au contraire, chaque ville tire en proportion de sa distance, et les groupes lointains comptent davantage.

**Erreurs fréquentes.** Rendre le barycentre ou la médiane coordonnée par coordonnée (l'objectif de 0,1 % n'est pas atteint) ; une descente de gradient à pas fixe trop grand (elle oscille) ou trop petit (elle n'avance pas en 5 s) ; diviser par une distance nulle.
