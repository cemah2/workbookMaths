# M10 · Séparabilité linéaire et convexité — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M10.Q1 — Convexe ou non ?

<details><summary>Indice 1</summary>

Relis « La définition » (fiche §1) et la figure des quatre ensembles.

</details>
<details><summary>Indice 2</summary>

Pour « non convexe », cherche deux points de l'ensemble de part et d'autre d'un « trou » ou d'un « creux ».

</details>
<details><summary>Indice 3</summary>

3 : c'est la région au-dessus de la courbe d'une fonction convexe (fiche §1, dernier paragraphe). 4 : où sont les points tels que $xy \ge 0$ ? Prends un point dans chacun des deux morceaux.

</details>

### M10.Q2 — L'enveloppe convexe : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Définition » (fiche §2).

</details>
<details><summary>Indice 2</summary>

L'enveloppe est le plus petit convexe qui contient $S$ ; ses sommets sont certains points de $S$, pas tous.

</details>
<details><summary>Indice 3</summary>

5 : le barycentre est une combinaison convexe (fiche §1). 6 : un point ajouté très loin peut-il « avaler » des sommets ?

</details>

### M10.Q3 — Séparable ou non ?

<details><summary>Indice 1</summary>

Relis « Le critère des enveloppes convexes » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Dessine chaque configuration ; pour un « non », cherche un point de l'une des classes qui est dans l'enveloppe de l'autre.

</details>
<details><summary>Indice 3</summary>

3 : $(1, 2)$ vérifie-t-il les trois inégalités du triangle ($x \ge 0$, $y \ge 0$, $x + y \le 4$) ? 5 : relis la fin de « L'astuce du biais ».

</details>

### M10.Q4 — Marge et astuce du biais

<details><summary>Indice 1</summary>

Relis « La marge d'un séparateur » et « L'astuce du biais » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Un hyperplan ne change pas quand on multiplie $\mathbf{w}$ **et** $b$ par un même nombre non nul ; la marge géométrique est un minimum.

</details>
<details><summary>Indice 3</summary>

1 : multiplie l'équation $\frac{\mathbf{w}}{2} \cdot \mathbf{x} + b = 0$ par 2. 3 : remplace $x_0$ par 1 dans l'équation du plan. 4 : la coordonnée constante d'un point relevé vaut toujours 1. 6 : relis le théorème de la plus grande marge.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M10.R1 — Hyperplans et distance à un hyperplan (M07)

<details><summary>Indice 1</summary>

Relis M07 §5, « La distance à un hyperplan ».

</details>
<details><summary>Indice 2</summary>

Distance signée : $\frac{\mathbf{w} \cdot \mathbf{x} + b}{\lVert \mathbf{w} \rVert}$ ; ici $b = -3$.

</details>
<details><summary>Indice 3</summary>

1 : $\mathbf{w} = (2, -1, 2)$, de norme 3. 5 : le point le plus proche est $\mathbf{x} - \frac{\mathbf{w} \cdot \mathbf{x} + b}{\lVert \mathbf{w} \rVert^2}\,\mathbf{w}$, avec $\mathbf{x} = \mathbf{0}$.

</details>

### M10.R2 — L'inégalité de Cauchy-Schwarz (M07)

<details><summary>Indice 1</summary>

Relis M07, l'inégalité de Cauchy-Schwarz.

</details>
<details><summary>Indice 2</summary>

$|\mathbf{u} \cdot \mathbf{v}| \le \lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert$, avec égalité quand les vecteurs sont colinéaires.

</details>
<details><summary>Indice 3</summary>

4 : applique-la à $(1, 1, 1)$ et $(a, b, c)$. 5 : écris $2a + 3b + 6c$ comme le produit scalaire de $(2, 3, 6)$ avec $(a, b, c)$.

</details>

### M10.R3 — La sigmoïde et tanh (R6)

<details><summary>Indice 1</summary>

Relis R6, la sigmoïde et tanh.

</details>
<details><summary>Indice 2</summary>

Pour 2, regarde comment varie $e^{-z}$, puis $1 + e^{-z}$, quand $z$ augmente. Pour 3, écris $1 - \sigma(z)$ avec le même dénominateur que $\sigma(z)$.

</details>
<details><summary>Indice 3</summary>

4 : $\tanh(z) = 0{,}2$ donne $\sigma(2z) = 0{,}6$, dont la cote vaut $1{,}5$. 5 : $\sigma(u) = \frac{1}{2}$ seulement pour $u = 0$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M10.1 — Convexe ou non : segments, demi-plans, intersections

<details><summary>Indice 1</summary>

Relis « La définition » et « Demi-espaces et intersections » (fiche §1).

</details>
<details><summary>Indice 2</summary>

a) et b) : $(1 - t)\mathbf{a} + t\mathbf{b} = \mathbf{a} + t(\mathbf{b} - \mathbf{a})$. d) à f) : dessine les quatre droites, puis cherche les sommets aux intersections.

</details>
<details><summary>Indice 3</summary>

a) $\mathbf{b} - \mathbf{a} = (8, -4)$. c) Pour chaque ensemble, cherche deux points dont le milieu sort ; si tu n'en trouves pas, reconnais une boule, une région au-dessus d'une courbe convexe ou une intersection de demi-plans. d) Résous $2x + y = 8$ et $x + 2y = 7$ ensemble.

</details>

### Ex M10.2 — L'enveloppe convexe de huit points, à la main

<details><summary>Indice 1</summary>

Relis « La chaîne monotone d'Andrew » (fiche §2), puis dessine les huit points.

</details>
<details><summary>Indice 2</summary>

Trie les points par $x$, puis par $y$ ; pour chaque nouveau point, teste le signe du produit vectoriel des deux derniers points de la chaîne et du nouveau.

</details>
<details><summary>Indice 3</summary>

Le plus petit point est $P_3 = (-3, 1)$. Un point est au milieu d'un côté quand son produit vectoriel avec les deux extrémités du côté est nul. e) Découpe en triangles depuis $P_3$ : l'aire de chacun est la moitié d'un produit vectoriel. f) Teste $Q$ contre le côté qui va de $P_6$ à $P_1$.

</details>

### Ex M10.3 — Une droite qui sépare deux petits nuages, et sa marge

<details><summary>Indice 1</summary>

Relis « La marge d'un séparateur », « Le meilleur décalage » et « La plus grande marge possible » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Calcule d'abord $\mathbf{w} \cdot P_i$ pour les six points ; la marge est le plus petit $y_i(\mathbf{w} \cdot P_i + b)$, divisé par $\lVert \mathbf{w} \rVert$.

</details>
<details><summary>Indice 3</summary>

c) Le projeté de $\mathbf{x}$ sur la droite est $\mathbf{x} - \frac{\mathbf{w} \cdot \mathbf{x} + b}{\lVert \mathbf{w} \rVert^2}\,\mathbf{w}$ (M07). d) Il faut $\min_{+1} \mathbf{w} \cdot \mathbf{x} + b > 0$ et $\max_{-1} \mathbf{w} \cdot \mathbf{x} + b < 0$. g) Dessine les deux triangles : leur couple de points le plus proche est formé de deux sommets.

</details>

### Ex M10.4 — L'astuce du biais : une droite du plan devient un plan de ℝ³ passant par l'origine

<details><summary>Indice 1</summary>

Relis « L'astuce du biais » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\tilde{\mathbf{w}} \cdot \tilde{\mathbf{x}} = b \times 1 + w_1x_1 + w_2x_2$ : la première coordonnée de $\tilde{\mathbf{x}}$ vaut toujours 1. Deux droites parallèles ont la même normale $\mathbf{w}$ et des biais différents.

</details>
<details><summary>Indice 3</summary>

a) Divise les trois coordonnées de $(4, 3, -2)$ par le même nombre. b) Écris $3x_1 - 2x_2 + b' = 0$ au point $\mathbf{p}$. c) La distance entre $\mathbf{w} \cdot \mathbf{x} + b = 0$ et $\mathbf{w} \cdot \mathbf{x} + b' = 0$ est $\frac{|b - b'|}{\lVert \mathbf{w} \rVert}$. e) Au niveau « première coordonnée $= 1$ », $\tilde{\mathbf{v}} \cdot \tilde{\mathbf{x}} = 0$ devient $-6 + 2x_1 + 3x_2 = 0$. f) De même, $\tilde{\mathbf{v}}' \cdot \tilde{\mathbf{x}} = 0$ devient $x_1 - 3x_2 = 0$. g) Écris $\tilde{\mathbf{u}} \cdot (1, 2, 0) = 0$ et $\tilde{\mathbf{u}} \cdot (1, 0, 1) = 0$ avec $u_0 = -2$.

</details>

### Ex M10.5 — Borner une norme pas à pas : ‖v_{k+1}‖² ≤ ‖v_k‖² + c

<details><summary>Indice 1</summary>

Relis « Une borne qui s'accumule » et « Deux bornes pour la norme » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$\lVert \mathbf{v} + \mathbf{d} \rVert^2 = \lVert \mathbf{v} \rVert^2 + 2\,\mathbf{v} \cdot \mathbf{d} + \lVert \mathbf{d} \rVert^2$ ; la borne oublie le terme du milieu, qui est $\le 0$.

</details>
<details><summary>Indice 3</summary>

b) $\mathbf{v}_1 = (3, 1)$. e) $\lVert \mathbf{v}_k \rVert^2 \le 5 + 5k$. f) Le lemme avec $c_k = (k + 1)^2$, pour $k = 0, \ldots, 5$ : ajoute $1^2, 2^2, \ldots, 6^2$ à $\lVert \mathbf{v}_0 \rVert^2 = 9$, puis prends la racine. g) Traite les deux séries de pas l'une après l'autre.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M10.6 — Un demi-espace est convexe, et une intersection de convexes aussi

<details><summary>Indice 1</summary>

Relis « Demi-espaces et intersections » (fiche §1).

</details>
<details><summary>Indice 2</summary>

1 : développe le produit scalaire et regroupe ; $(1 - t)b + tb = b$. 2 : un mélange de deux nombres positifs, avec des poids positifs, est positif.

</details>
<details><summary>Indice 3</summary>

5 : chaque contrainte $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ est un demi-espace de l'espace des $(\mathbf{w}, b)$ : le « score » est cette fois une fonction affine des paramètres, les points étant fixés.

</details>

### Ex M10.7 — Deux nuages séparés par un hyperplan ont des enveloppes convexes disjointes

<details><summary>Indice 1</summary>

Relis « Le critère des enveloppes convexes » (fiche §3).

</details>
<details><summary>Indice 2</summary>

1 : $\sum_i t_i(\mathbf{w} \cdot \mathbf{x}_i + b) = \mathbf{w} \cdot \sum_i t_i\mathbf{x}_i + b\sum_i t_i$.

</details>
<details><summary>Indice 3</summary>

4 : cherche $t_1, t_2, t_3 \ge 0$, de somme 1, avec $t_1(0, 0) + t_2(6, 0) + t_3(2, 6) = (2, 2)$ : la deuxième coordonnée donne $t_3$. 6 : si $\max A < \min B$, prends le milieu comme seuil.

</details>

### Ex M10.8 — La marge géométrique ne change pas quand on multiplie (w, b) par un réel positif

<details><summary>Indice 1</summary>

Relis « La marge d'un séparateur » et « La forme canonique » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\lVert c\mathbf{w} \rVert = |c|\,\lVert \mathbf{w} \rVert$. Pour 2, sépare les termes de la classe $+1$ de ceux de la classe $-1$.

</details>
<details><summary>Indice 3</summary>

2 : sur la classe $+1$, le plus petit terme vaut $\frac{m_+ + b}{\lVert \mathbf{w} \rVert}$ ; une fonction affine croissante et une décroissante : où leur minimum est-il le plus grand ? 3 : divise $(\mathbf{w}, b)$ par $m = \min_i y_i(\mathbf{w} \cdot \mathbf{x}_i + b) > 0$. 5 : un minimum sur un ensemble plus grand est plus petit ou égal.

</details>

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M10.9 — Pont : seuil, sigmoïde, tanh et ReLU appliqués à un même score linéaire

<details><summary>Indice 1</summary>

Relis le §5 de la fiche, et R6 pour la sigmoïde et tanh.

</details>
<details><summary>Indice 2</summary>

Calcule d'abord les trois scores ; chaque activation ne regarde que le score.

</details>
<details><summary>Indice 3</summary>

$\mathbf{p}_1$ donne $z = 4 - 2{,}25 - 1$. f) À la distance signée $d$ de la frontière, le score vaut $d\,\lVert \mathbf{w} \rVert$, avec $\lVert \mathbf{w} \rVert = 5$. g) $\frac{1}{1 + e^{-z}} = 0{,}85$ donne $e^{-z} = \frac{0{,}15}{0{,}85}$ ; la ligne de niveau est la droite $\mathbf{w} \cdot \mathbf{x} + b = z_{0{,}85}$, à la distance $\frac{z_{0{,}85}}{\lVert \mathbf{w} \rVert}$ de la frontière.

</details>

### Ex M10.10 — MML §12.1 : les hyperplans séparateurs, en anglais

<details><summary>Indice 1</summary>

Lis l'introduction du chapitre 12, puis le §12.1, crayon en main, avec le §3 de la fiche à côté.

</details>
<details><summary>Indice 2</summary>

Pour 3, reprends l'argument de M07 §5 : deux points de l'hyperplan, et la différence de leurs deux équations.

</details>
<details><summary>Indice 3</summary>

Pour 3 : $(1, 3)$ et $(-1, -2)$ sont sur la droite $5x_1 - 2x_2 + 1 = 0$ ; calcule le produit scalaire de leur différence avec $(5, -2)$.

</details>

### Ex M10.11 — Expliquer la convexité et l'enveloppe convexe avec un élastique

<details><summary>Indice 1</summary>

Relis le début du §1 et du §2 de la fiche.

</details>
<details><summary>Indice 2</summary>

Une planche, des clous, un élastique : les clous qu'il touche sont les sommets ; une forme sans « creux » est convexe.

</details>
<details><summary>Indice 3</summary>

Pour la séparabilité : si les deux élastiques se croisent ou se chevauchent, une règle posée à plat devrait laisser un même morceau de planche des deux côtés à la fois.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M10.E1 — « Que veut dire « linéairement séparable », et comment le vérifier ? »

<details><summary>Indice 1</summary>

Relis le §3 de la fiche, et l'après-expérience de M10.14.

</details>
<details><summary>Indice 2</summary>

Un plan : la définition, l'image (deux demi-espaces ouverts), le critère, un test, la grande dimension, une mise en garde.

</details>
<details><summary>Indice 3</summary>

Le test : un programme linéaire de faisabilité avec $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ (pourquoi pas $\ge 0$ ?). La grande dimension : $d + 1$ points sont toujours séparables.

</details>

<a id="notebook"></a>

## Notebook

### Ex M10.12 — L'enveloppe convexe dans le plan : la chaîne monotone d'Andrew · `convex_hull_2d`

<details><summary>Indice 1</summary>

Relis « La chaîne monotone d'Andrew » (fiche §2) et le tableau de l'exemple.

</details>
<details><summary>Indice 2</summary>

Une fonction auxiliaire `cross(o, a, b)` ; une fonction qui construit une demi-chaîne à partir d'une liste de points triés ; la même fonction sur la liste retournée donne l'autre chaîne.

</details>
<details><summary>Indice 3</summary>

`pts = np.unique(P, axis=0)` trie les points distincts ; la boucle d'une demi-chaîne : `while len(chain) >= 2 and cross(chain[-2], chain[-1], p) <= 0: chain.pop()`, puis `chain.append(p)` ; à la fin, `lower[:-1] + upper[:-1]`. Traite à part le cas d'un seul point distinct.

</details>

### Ex M10.13 — Séparabilité par programmation linéaire, et marge géométrique · `is_linearly_separable, margin_of_separator`

<details><summary>Indice 1</summary>

Relis « Séparable par un hyperplan » et « La marge d'un séparateur » (fiche §3), puis la docstring de `scipy.optimize.linprog`.

</details>
<details><summary>Indice 2</summary>

Les inconnues sont $(w_1, \ldots, w_d, b)$ ; la contrainte $i$ est la ligne $(-y_i\mathbf{x}_i, -y_i)$ de `A_ub`, et `b_ub` vaut $-1$ partout.

</details>
<details><summary>Indice 3</summary>

Ajoute une colonne de 1 à droite de `X` (`np.hstack`), multiplie chaque ligne par $-y_i$ : c'est `A_ub`. L'objectif est nul, `b_ub` est rempli de $-1$, les inconnues sont libres ; le statut 0 de `linprog` veut dire « une solution existe », à convertir en `bool`. Pour la marge, après les contrôles : le plus petit $y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$, divisé par $\lVert \mathbf{w} \rVert$, converti en `float`.

</details>

### Ex M10.14 — Prédire : n points aux labels tirés au hasard en dimension d sont-ils séparables ?

<details><summary>Indice 1</summary>

Relis la fin de « L'astuce du biais » (fiche §3) : $d + 1$ points sont toujours séparables.

</details>
<details><summary>Indice 2</summary>

Avec 3 points d'une droite, quels étiquetages échouent ? Compte-les parmi les $2^3$ étiquetages possibles.

</details>
<details><summary>Indice 3</summary>

Pense au rapport entre $n$ et $d + 1$ : il est le même en b) et en c).

</details>

### Ex M10.15 — Deux nuages, leurs enveloppes convexes et un hyperplan séparateur avec sa marge

<details><summary>Indice 1</summary>

Relis la figure des deux séparateurs (fiche §3).

</details>
<details><summary>Indice 2</summary>

Pour fermer un polygone, ajoute le premier sommet à la fin : `np.vstack([hull, hull[:1]])`. La droite $\mathbf{w} \cdot \mathbf{x} + b = c$ s'écrit $x_2 = \frac{c - b - w_1x_1}{w_2}$.

</details>
<details><summary>Indice 3</summary>

Les deux bords de la marge sont les droites $\mathbf{w} \cdot \mathbf{x} + b = \pm\gamma\lVert \mathbf{w} \rVert$.

</details>

### Ex M10.16 — Chasse à l'erreur : un produit vectoriel de signe inversé, une marge non normalisée

<details><summary>Indice 1</summary>

Relis le récapitulatif des pièges de la fiche.

</details>
<details><summary>Indice 2</summary>

Calcule chaque ligne sur un petit exemple dont tu connais la réponse : $(1, 0) \times (0, 1)$, une marge sur deux points.

</details>
<details><summary>Indice 3</summary>

Deux lignes sont fausses. Pour b), refais la chaîne du bas en remplaçant chaque « à gauche » par « à droite ».

</details>

### Ex M10.17 — Des tests de propriétés pour l'enveloppe convexe

<details><summary>Indice 1</summary>

Relis « Tourner à gauche : le produit vectoriel du plan » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Un test par propriété, dans l'ordre demandé ; le tour du polygone se fait avec les indices `i - 1`, `i` et `(i + 1) % h`.

</details>
<details><summary>Indice 3</summary>

« sommets » : chaque ligne de `hull` est-elle une ligne de `points` (`np.array_equal`) ? « depart » : `min(map(tuple, points))` est le plus petit point dans l'ordre du tri.

</details>

### Ex M10.18 — Défi : la plus grande marge possible entre deux nuages donnés, à 1 % près

<details><summary>Indice 1</summary>

Commence par la médiatrice des barycentres, et mesure sa marge avec `margin_18`.

</details>
<details><summary>Indice 2</summary>

À direction fixée, le meilleur $b$ est connu (fiche §3) : il reste à choisir la direction. Ou bien : la plus grande marge est la moitié de la distance entre les deux enveloppes.

</details>
<details><summary>Indice 3</summary>

Balayer les directions $\mathbf{u} = (\cos\theta, \sin\theta)$, quelques centaines d'angles, suffit à 1 %. Par la géométrie : le couple le plus proche relie un sommet d'une enveloppe à un côté de l'autre ; le projeté d'un point sur un segment se calcule avec un $t$ ramené dans $[0, 1]$.

</details>
