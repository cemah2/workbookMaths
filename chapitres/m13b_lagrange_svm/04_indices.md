# M13b · Optimisation sous contraintes et SVM — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M13b.Q1 — Lagrange : ce que dit ∇f = λ ∇g

<details><summary>Indice 1</summary>

Relis le §1 de la fiche et sa figure des lignes de niveau.

</details>
<details><summary>Indice 2</summary>

Au point optimal, la ligne de niveau de $f$ touche la contrainte sans la traverser.

</details>
<details><summary>Indice 3</summary>

5 : $\frac{df^*}{dc} = -\lambda$ avec ce lagrangien. 6 : regarde ce que devient la courbe $g = 0$ là où son gradient s'annule.

</details>

### M13b.Q2 — Contrainte active ou inactive ?

<details><summary>Indice 1</summary>

Relis « Active ou inactive » (fiche §3).

</details>
<details><summary>Indice 2</summary>

La complémentarité : $\mu\,g(\mathbf{x}^*) = 0$.

</details>
<details><summary>Indice 3</summary>

3 : cherche un minimum libre qui tombe exactement sur le bord. 4 : où est le minimum libre ? 6 : passe tout du même côté.

</details>

### M13b.Q3 — Primal, dual, dualité faible

<details><summary>Indice 1</summary>

Relis le §4 de la fiche.

</details>
<details><summary>Indice 2</summary>

$D$ est un minimum, en $\mathbf{x}$, de fonctions affines des multiplicateurs.

</details>
<details><summary>Indice 3</summary>

3 : la dualité faible, $D \le f^*$. 6 : chaque valeur de $D$ minore $f^*$, chaque valeur de $f$ admissible le majore.

</details>

### M13b.Q4 — Problème convexe ou pas ?

<details><summary>Indice 1</summary>

Relis la définition du §5 de la fiche.

</details>
<details><summary>Indice 2</summary>

Trois questions : minimise-t-on ? l'objectif est-il convexe ? chaque inégalité est-elle convexe et chaque égalité affine ?

</details>
<details><summary>Indice 3</summary>

2 : l'égalité. 3 : le sens de l'optimisation. 6 : pense à $e^x$ sur $\mathbb{R}$.

</details>

### M13b.Q5 — Ce que maximise une SVM, ce que minimise son problème

<details><summary>Indice 1</summary>

Relis le §6 de la fiche, et M10 pour la marge.

</details>
<details><summary>Indice 2</summary>

Avec la forme canonique, la marge vaut $\frac{1}{\lVert\mathbf{w}\rVert}$, et la bande est deux fois plus large.

</details>
<details><summary>Indice 3</summary>

2 : un problème quadratique convexe. 5 : la stricte convexité de $\frac{1}{2}\lVert\mathbf{w}\rVert^2$.

</details>

### M13b.Q6 — La hinge loss : vrai ou faux

<details><summary>Indice 1</summary>

Relis le §7 de la fiche et la figure des losses.

</details>
<details><summary>Indice 2</summary>

Trace $\max(0, 1 - t)$ : deux morceaux de droite, un coude en $t = 1$.

</details>
<details><summary>Indice 3</summary>

3 : regarde $t = 0{,}5$. 5 : les pentes des deux morceaux. 6 : relis « Le rôle de C » (fiche §7).

</details>

### M13b.Q7 — Noyau valide ou pas ?

<details><summary>Indice 1</summary>

Relis « Quelles fonctions sont des noyaux ? » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Un noyau est symétrique et ses matrices de Gram sont semi-définies positives ; somme, produit et multiplication par une constante positive gardent un noyau.

</details>
<details><summary>Indice 3</summary>

3 : regarde $k(\mathbf{x}, \mathbf{x})$. 5 : échange $\mathbf{x}$ et $\mathbf{z}$. 6 : compare les lignes des deux points confondus.

</details>

### M13b.Q8 — Primal ou dual : lequel résoudre, et quand ?

<details><summary>Indice 1</summary>

Relis « Des produits scalaires, puis des noyaux » (fiche §8), et son paragraphe « Primal ou dual ? ».

</details>
<details><summary>Indice 2</summary>

Le primal a une variable par feature (plus $b$ et les écarts), le dual une par exemple.

</details>
<details><summary>Indice 3</summary>

2 : la taille de la matrice de Gram, $n^2$. 6 : combien de coordonnées a le $\varphi$ du RBF ?

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M13b.R1 — La marge géométrique et l'astuce du biais (M10)

<details><summary>Indice 1</summary>

Relis M10 §3 (séparabilité, astuce du biais, marge).

</details>
<details><summary>Indice 2</summary>

Marge fonctionnelle $= y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ ; marge géométrique $=$ la plus petite, divisée par $\lVert\mathbf{w}\rVert$.

</details>
<details><summary>Indice 3</summary>

1 : le score de $(0, 3)$ vaut $-10$. 3 : la plus petite marge fonctionnelle vaut 7.

</details>

### M13b.R2 — Gradient et lignes de niveau (M05b)

<details><summary>Indice 1</summary>

Relis M05b §2 et §4, et ∂ M05b.12.

</details>
<details><summary>Indice 2</summary>

Dérive par rapport à $x$, puis par rapport à $y$.

</details>
<details><summary>Indice 3</summary>

3 : un vecteur orthogonal à $(a, b)$ est $(b, -a)$ ou $(-b, a)$.

</details>

### M13b.R3 — Matrices définies positives (M12c)

<details><summary>Indice 1</summary>

Relis M12c §7 et ∂ M12c.17.

</details>
<details><summary>Indice 2</summary>

En dimension 2 : définie positive si et seulement si la trace et le déterminant sont strictement positifs.

</details>
<details><summary>Indice 3</summary>

4 : compare le troisième vecteur aux deux premiers.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M13b.1 — Lagrange à la main : un produit maximal sous une contrainte linéaire

<details><summary>Indice 1</summary>

Relis le §1 de la fiche, son exemple et « Ce que vaut λ : un prix ».

</details>
<details><summary>Indice 2</summary>

Le système : $yz = \lambda$, $xz = 2\lambda$, $xy = 4\lambda$, plus la contrainte. Divise les équations deux à deux.

</details>
<details><summary>Indice 3</summary>

$x = 2y = 4z$, donc la contrainte devient $3x = 24$. Pour $c$ quelconque : $x = \frac{c}{3}$, $y = \frac{c}{6}$, $z = \frac{c}{12}$.

</details>

### Ex M13b.2 — La distance d'un point à un plan, retrouvée par Lagrange

<details><summary>Indice 1</summary>

Relis le §1 de la fiche, et M07 pour la distance à un plan.

</details>
<details><summary>Indice 2</summary>

La stationnarité donne $\mathbf{x} = \mathbf{x}_0 - \frac{\lambda}{2}\mathbf{n}$ ; reporte dans la contrainte.

</details>
<details><summary>Indice 3</summary>

$\mathbf{n} \cdot \mathbf{x}_0 = 37$, $\lVert\mathbf{n}\rVert^2 = 81$ : $37 - \frac{81}{2}\lambda = 10$.

</details>

### Ex M13b.3 — Un problème quadratique sous deux contraintes linéaires : le système de Lagrange

<details><summary>Indice 1</summary>

Relis « Le problème quadratique sous contraintes linéaires » (fiche §2).

</details>
<details><summary>Indice 2</summary>

$\begin{pmatrix} \mathbf{Q} & \mathbf{A}^\top \\ \mathbf{A} & \mathbf{0} \end{pmatrix}\begin{pmatrix} \mathbf{x} \\ \boldsymbol{\lambda} \end{pmatrix} = \begin{pmatrix} -\mathbf{c} \\ \mathbf{b} \end{pmatrix}$ : écris chacun de ses blocs.

</details>
<details><summary>Indice 3</summary>

Élimine : la deuxième contrainte donne $x_1 = 1 + x_3$, la première $x_2 = 2 - 2x_3$ ; il reste une équation en $x_3$. h) $\mathbf{x} = -\mathbf{Q}^{-1}\mathbf{c}$.

</details>

### Ex M13b.4 — Relire l'ACP par Lagrange : maximiser uᵀCu sous ‖u‖ = 1

<details><summary>Indice 1</summary>

Relis « L'ACP relue par Lagrange » (fiche §2), et M12d.

</details>
<details><summary>Indice 2</summary>

La stationnarité donne $\mathbf{C}\mathbf{u} = \lambda\mathbf{u}$ ; essaie des vecteurs propres à coordonnées entières.

</details>
<details><summary>Indice 3</summary>

Essaie $(1, -3, 2)$ ; la somme des valeurs propres vaut la trace 20, leur produit le déterminant 78.

</details>

### Ex M13b.5 — Une contrainte d'inégalité : active ou non, les conditions KKT à la main

<details><summary>Indice 1</summary>

Relis « Active ou inactive » et « Les conditions KKT » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Commence par le minimum libre : est-il admissible ? S'il ne l'est pas, la contrainte est active.

</details>
<details><summary>Indice 3</summary>

Le minimum libre est $(2, 2)$. Stationnarité : $x = 2 - \mu$, $y = 2 - \frac{\mu}{4}$ ; reporte dans $2x + y = 3$.

</details>

### Ex M13b.6 — La fonction duale d'un petit problème quadratique, et la dualité faible

<details><summary>Indice 1</summary>

Relis le §4 de la fiche et son exemple.

</details>
<details><summary>Indice 2</summary>

À $\mu$ fixé, $\mathcal{L} = x^2 + 2y^2 + \mu(6 - x - y)$ est une fonction quadratique de $(x, y)$ : annule son gradient.

</details>
<details><summary>Indice 3</summary>

$x = \frac{\mu}{2}$, $y = \frac{\mu}{4}$ ; $D$ est un polynôme de degré 2 en $\mu$.

</details>

### Ex M13b.7 — Reconnaître un problème convexe : fonctions, contraintes, ensembles

<details><summary>Indice 1</summary>

Relis le §5 de la fiche, et M10 pour les fonctions convexes.

</details>
<details><summary>Indice 2</summary>

Pour chaque problème : le sens (min ou max), l'objectif, chaque inégalité ($g \le 0$ avec $g$ convexe), chaque égalité (affine).

</details>
<details><summary>Indice 3</summary>

Quatre sont convexes. (G) : regarde $x^2 - y^2$ le long de l'axe des $y$.

</details>

### Ex M13b.8 — Une SVM à marge dure sur trois points, résolue par les conditions KKT

<details><summary>Indice 1</summary>

Relis le §6 de la fiche et son exemple résolu, puis « Lire les multiplicateurs » (fiche §8).

</details>
<details><summary>Indice 2</summary>

$\mathbf{x}_1$ et $\mathbf{x}_2$ sont sur le même bord : $\mathbf{w} \cdot (\mathbf{x}_2 - \mathbf{x}_1) = 0$.

</details>
<details><summary>Indice 3</summary>

$\mathbf{w} = k(-1, 2)$ ; la différence des contraintes de $\mathbf{x}_1$ et $\mathbf{x}_3$ donne $\mathbf{w} \cdot (\mathbf{x}_1 - \mathbf{x}_3) = 2$.

</details>

### Ex M13b.9 — La hinge loss et l'objectif régularisé de quelques points

<details><summary>Indice 1</summary>

Relis « Autoriser des violations », « La hinge loss » et « Le rôle de C » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Score $s = x_1 - 0{,}5\,x_2 + 0{,}5$, puis $t = y\,s$, puis $\max(0, 1 - t)$.

</details>
<details><summary>Indice 3</summary>

$J = \frac{1}{2}\lVert\mathbf{w}\rVert^2 + C \times$ la **somme** des hinges ; f) $\lambda = \frac{1}{nC}$.

</details>

### Ex M13b.10 — Un pas de sous-gradient sur l'objectif d'une SVM linéaire

<details><summary>Indice 1</summary>

Relis « Le sous-gradient » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\mathbf{g}_{\mathbf{w}} = \mathbf{w} - C\sum_{t_i < 1} y_i\mathbf{x}_i$ et $g_b = -C\sum_{t_i < 1} y_i$.

</details>
<details><summary>Indice 3</summary>

Deux exemples comptent : $(0, 3)$ et $(-1, 2)$ ; $(3 ;\ 0{,}5)$ est au coude.

</details>

### Ex M13b.11 — Le dual d'une SVM : lire les vecteurs de support et retrouver w

<details><summary>Indice 1</summary>

Relis « Le dual de la SVM » et « Lire les multiplicateurs » (fiche §8).

</details>
<details><summary>Indice 2</summary>

$\mathbf{w} = \sum_i \alpha_i y_i\mathbf{x}_i$ ; $b$ se lit sur un vecteur libre ($0 < \alpha_i < C$), qui est sur un bord.

</details>
<details><summary>Indice 3</summary>

Vecteurs libres : 1 et 6. $b = y_1 - \mathbf{w} \cdot \mathbf{x}_1$.

</details>

### Ex M13b.12 — Le noyau (1 + x · z)² en dimension 2 : sa fonction φ à six coordonnées

<details><summary>Indice 1</summary>

Relis « Des produits scalaires, puis des noyaux » et « Le noyau polynomial » (fiche §8), puis M09b pour `count_monomials`.

</details>
<details><summary>Indice 2</summary>

Développe le carré d'une somme de trois termes : trois carrés et trois doubles produits ; chaque terme est une fonction de $\mathbf{x}$ fois la même fonction de $\mathbf{z}$.

</details>
<details><summary>Indice 3</summary>

d) $(3 + \mathbf{x} \cdot \mathbf{z})^2 = 9 + 6\,\mathbf{x} \cdot \mathbf{z} + (\mathbf{x} \cdot \mathbf{z})^2$ : la constante et les coordonnées de degré 1 changent. e) les monômes de degré **au plus** 2 en 9 variables.

</details>

### Ex M13b.13 — La matrice de Gram d'un noyau RBF sur trois points, et l'effet de γ

<details><summary>Indice 1</summary>

Relis « Le noyau RBF » (fiche §8).

</details>
<details><summary>Indice 2</summary>

$k = e^{-\gamma d^2}$, avec le **carré** de la distance ; la diagonale vaut 1.

</details>
<details><summary>Indice 3</summary>

e) $\sqrt{2 - 2k}$. g) et h) : que vaut $e^{-\gamma d^2}$ quand $\gamma \to 0$, puis quand $\gamma \to +\infty$, pour $d > 0$ ?

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M13b.14 — Au point optimal sous une contrainte d'égalité, ∇f est colinéaire à ∇g

<details><summary>Indice 1</summary>

Relis le §1 de la fiche et M05b.12 (la règle de la chaîne le long d'une courbe).

</details>
<details><summary>Indice 2</summary>

$\frac{d}{dt}g(\mathbf{c}(t)) = \nabla g(\mathbf{c}(t)) \cdot \mathbf{c}'(t)$, et une fonction d'une variable a une dérivée nulle en un minimum intérieur.

</details>
<details><summary>Indice 3</summary>

4 : essaie une courbe avec un point de rebroussement, comme $y^2 = x^3$, et minimise $x$ dessus.

</details>

### Ex M13b.15 — La dualité faible : la fonction duale minore le minimum du primal

<details><summary>Indice 1</summary>

Relis le §4 de la fiche.

</details>
<details><summary>Indice 2</summary>

Sur un point admissible, chaque terme $\mu_i g_i(\mathbf{x})$ est négatif ou nul et chaque $\lambda_j h_j(\mathbf{x})$ est nul.

</details>
<details><summary>Indice 3</summary>

3 : l'infimum d'une somme est au moins la somme des infimums. 5 : utilise 2 dans les deux sens.

</details>

### Ex M13b.16 — Pour un problème convexe, un minimum local est global

<details><summary>Indice 1</summary>

Relis le §5 de la fiche, et la définition d'une fonction convexe (M10).

</details>
<details><summary>Indice 2</summary>

Applique la définition de la convexité au segment $[\mathbf{x}^*, \mathbf{y}]$.

</details>
<details><summary>Indice 3</summary>

3 : $\lVert\mathbf{x}_\theta - \mathbf{x}^*\rVert = \theta\lVert\mathbf{y} - \mathbf{x}^*\rVert$. 4 : la stricte convexité au milieu.

</details>

### Ex M13b.17 — Maximiser la marge revient à minimiser ½ ‖w‖²

<details><summary>Indice 1</summary>

Relis le §6 de la fiche et ∂ M10.8.

</details>
<details><summary>Indice 2</summary>

La marge ne change pas quand on multiplie $(\mathbf{w}, b)$ par un $c > 0$.

</details>
<details><summary>Indice 3</summary>

4 : si toutes les marges des $+1$ dépassent $1 + \varepsilon$, diminue $b$ de $\frac{\varepsilon}{2}$ : toutes les contraintes deviennent strictes ; puis multiplie $(\mathbf{w}, b)$ par un $c < 1$.

</details>

### Ex M13b.18 — Marge souple : la formulation avec des variables d'écart et celle avec la hinge loss sont équivalentes

<details><summary>Indice 1</summary>

Relis « Autoriser des violations » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Les deux contraintes sur $\xi_i$ disent : $\xi_i$ est au moins $1 - t_i$, et au moins 0.

</details>
<details><summary>Indice 3</summary>

3 : minimiser en $(\mathbf{w}, b, \boldsymbol{\xi})$, c'est minimiser en $(\mathbf{w}, b)$ le minimum en $\boldsymbol{\xi}$. 4 : un point admissible de (P) sans écart.

</details>

### Ex M13b.19 — La somme et le produit de deux noyaux sont des noyaux ; une matrice de Gram est semi-définie positive

<details><summary>Indice 1</summary>

Relis « Quelles fonctions sont des noyaux ? » (fiche §8), et M12c.17.

</details>
<details><summary>Indice 2</summary>

Développe $\lVert\sum_i v_i\varphi(\mathbf{x}_i)\rVert^2$ en produits scalaires.

</details>
<details><summary>Indice 3</summary>

4 : le produit de deux sommes est la somme des produits deux à deux. 6 : regarde la matrice de Gram de deux points distincts.

</details>

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M13b.20 — Pont : la décision d'une SVM à noyau, une somme pondérée sur les vecteurs de support

<details><summary>Indice 1</summary>

Relis « Des produits scalaires, puis des noyaux » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Pour chaque vecteur de support : la distance au carré, puis $e^{-0{,}3\,d^2}$, puis le poids $\alpha_i y_i$.

</details>
<details><summary>Indice 3</summary>

b) les distances au carré valent 2,5, 4,5 et 6,5. e) que vaut un noyau RBF très loin ?

</details>

### Ex M13b.21 — MML §7.2 et §7.3 : Lagrange, dualité et optimisation convexe, en anglais

<details><summary>Indice 1</summary>

Lis le guide de lecture de la fiche avant le livre : §7.2 après le §3 de la fiche, §7.3 après le §5.

</details>
<details><summary>Indice 2</summary>

Le livre écrit $\boldsymbol{\lambda} \ge \mathbf{0}$ pour les multiplicateurs des inégalités (la fiche : $\boldsymbol{\mu}$).

</details>
<details><summary>Indice 3</summary>

5 : écris M13b.6 sous la forme du livre, $\mathbf{Q} = \operatorname{diag}(2, 4)$, $\mathbf{c} = \mathbf{0}$, une contrainte $-x - y \le -6$.

</details>

### Ex M13b.22 — MML §12.2 à §12.5 : marge, primal, dual et noyaux (§12.1 a été lu en M10)

<details><summary>Indice 1</summary>

Lis le guide de lecture : §12.2 après le §7 de la fiche, §12.3 à §12.5 après le §8.

</details>
<details><summary>Indice 2</summary>

Compare chaque normalisation du livre à la forme canonique de la fiche §6.

</details>
<details><summary>Indice 3</summary>

3 : le livre écrit le dual comme une minimisation ; change le signe pour retrouver la fiche.

</details>

### Ex M13b.23 — Fermi : la taille de la matrice de Gram d'une SVM à noyau sur 100 000 exemples

<details><summary>Indice 1</summary>

Relis « Des produits scalaires, puis des noyaux » (fiche §8).

</details>
<details><summary>Indice 2</summary>

$n^2$ nombres, 8 octets en `float64`.

</details>
<details><summary>Indice 3</summary>

3 : environ $2p$ opérations par distance. 5 : résous $8n^2 = 16 \times 10^9$.

</details>

### Ex M13b.24 — Expliquer un multiplicateur de Lagrange comme un prix

<details><summary>Indice 1</summary>

Relis « Ce que vaut λ : un prix » (fiche §1) et « Contrainte ou pénalité » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Trois idées : ce que coûte la contrainte, ce que rapporte une unité de plus, le prix nul d'une contrainte qui ne gêne pas.

</details>
<details><summary>Indice 3</summary>

Un exemple : un budget, et ce que rapporte un euro de plus ; puis le budget qu'on ne dépense pas en entier.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M13b.E1 — « Qu'est-ce qu'un problème d'optimisation convexe, et pourquoi est-ce une bonne nouvelle ? »

<details><summary>Indice 1</summary>

Relis le §5 de la fiche.

</details>
<details><summary>Indice 2</summary>

Définition (objectif, inégalités, égalités), puis quatre garanties.

</details>
<details><summary>Indice 3</summary>

Local = global, unicité si stricte, KKT suffisantes, dualité forte (Slater) ; ridge et SVM ; un réseau de neurones comme contre-exemple.

</details>

### M13b.E2 — « Hinge loss ou log-loss : quelles différences ? »

<details><summary>Indice 1</summary>

Relis le §7 de la fiche et M13a §2.

</details>
<details><summary>Indice 2</summary>

Écris les deux en fonction de $t = y\,s$, puis trace-les.

</details>
<details><summary>Indice 3</summary>

Trois différences : le coude, le zéro exact au-delà de $t = 1$, la probabilité en sortie.

</details>

<a id="notebook"></a>

## Notebook

### Ex M13b.25 — Un problème quadratique sous contraintes d'égalité, par le système de Lagrange · `lagrange_equality_qp`

<details><summary>Indice 1</summary>

Relis « Le problème quadratique sous contraintes linéaires » (fiche §2), puis la docstring.

</details>
<details><summary>Indice 2</summary>

Contrôle les formes d'abord : `Q` est $n \times n$ pour un `c` de longueur $n$, `A` a $n$ colonnes et autant de lignes que `b` a de valeurs. Puis `np.block([[Q, A.T], [A, np.zeros((m, m))]])` et le second membre `np.concatenate([-c, b])`.

</details>
<details><summary>Indice 3</summary>

`sol = np.linalg.solve(K, rhs)` dans un `try` qui transforme `np.linalg.LinAlgError` en `ValueError` ; rends `sol[:n], sol[n:]`. e) La contrainte écrite deux fois donne deux lignes égales : la matrice est singulière.

</details>

### Ex M13b.26 — La hinge loss et un sous-gradient de l'objectif d'une SVM linéaire · `hinge_loss, svm_subgradient`

<details><summary>Indice 1</summary>

Relis « La hinge loss » et « Le sous-gradient » (fiche §7), puis les deux docstrings.

</details>
<details><summary>Indice 2</summary>

Calcule d'un coup les marges `t = y * (X @ w + b)` ; `below = t < 1` (strictement) choisit les exemples qui comptent. $J$ prend la **somme** des hinges, `hinge_loss` leur **moyenne**.

</details>
<details><summary>Indice 3</summary>

`g_w = w - C * (y[below] @ X[below])` et `g_b = -C * y[below].sum()`. Les contrôles : labels dans $\{-1, +1\}$ (`np.isin`), formes compatibles, $C > 0$. f) fais le pas sur $(\mathbf{w}, b)$ **ensemble**, puis recalcule $J$.

</details>

### Ex M13b.27 — Les noyaux RBF et polynomial · `rbf_kernel, polynomial_kernel`

<details><summary>Indice 1</summary>

Relis « Le noyau polynomial » et « Le noyau RBF » (fiche §8), puis les docstrings.

</details>
<details><summary>Indice 2</summary>

Les carrés des distances d'un coup : `(X**2).sum(1)[:, None] - 2 * X @ Z.T + (Z**2).sum(1)[None, :]`, puis `np.maximum(..., 0)` contre les petites valeurs négatives de l'arrondi.

</details>
<details><summary>Indice 3</summary>

`np.exp(-gamma * d2)` ; `(X @ Z.T + coef0) ** degree`. d) Sans `np.maximum`, un carré de distance de $-10^{-9}$ donne un noyau un peu au-dessus de 1. Refuse $\gamma \le 0$, un degré qui n'est pas un entier $\ge 1$ (attention : `True` est un entier pour Python) et `coef0 < 0`.

</details>

### Ex M13b.28 — `scipy.optimize.minimize` sous contraintes et les noyaux de scikit-learn contre tes fonctions

<details><summary>Indice 1</summary>

Relis l'énoncé : il dit ce que rend chaque fonction et quels sont ses paramètres par défaut.

</details>
<details><summary>Indice 2</summary>

a) `fun = lambda x: 0.5 * x @ Q_25 @ x + C_25 @ x`, `grad = lambda x: Q_25 @ x + C_25`, la contrainte `lambda x: A_25 @ x - B_25` de jacobienne `lambda x: A_25`. Pour b) à d), `np.allclose` avec les tolérances de l'énoncé.

</details>
<details><summary>Indice 3</summary>

e) exécute `polynomial_kernel(P_28, R_28)[0, 0]` tel quel, puis compare à $(\frac{1}{4}\,\mathbf{x} \cdot \mathbf{z} + 1)^3$. h) `try: hinge_loss(S_28, Y_28)` / `except Exception as exc: name = type(exc).__name__`.

</details>

### Ex M13b.29 — Prédire : comment change le minimum quand on relâche la contrainte, et ce que dit λ

<details><summary>Indice 1</summary>

Relis « Ce que vaut λ : un prix » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Avec ce lagrangien, $\frac{df^*}{dc} = -\lambda$. Pour c) et d), écris la nouvelle stationnarité et compare-la à l'ancienne.

</details>
<details><summary>Indice 3</summary>

b) $-\lambda \times 0{,}1$. c) $2\nabla f + \lambda'\nabla g = \mathbf{0}$ ; d) $\nabla f + \lambda'(2\nabla g) = \mathbf{0}$ : le point solution ne change pas, seul le multiplicateur s'adapte.

</details>

### Ex M13b.30 — La descente de sous-gradient sur la hinge loss : pas constant contre pas décroissant

<details><summary>Indice 1</summary>

Relis « La descente de sous-gradient » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Une boucle `for t in range(1, steps + 1)` : calcule `J, g_w, g_b`, range `J`, puis `w = w - eta(t) * g_w` et `b = b - eta(t) * g_b`. Pars de `w = np.zeros(p)`, `b = 0.0`.

</details>
<details><summary>Indice 3</summary>

a) pour chaque réglage, `min(Js) - J_STAR_30`. c) compte les `t` où `Js[t + 1] > Js[t]`, par exemple `int(np.sum(np.diff(Js) > 0))`.

</details>

### Ex M13b.31 — Lignes de niveau et contrainte : voir le point de Lagrange

<details><summary>Indice 1</summary>

Relis « Les lignes de niveau touchent la contrainte » (fiche §1) et sa figure.

</details>
<details><summary>Indice 2</summary>

Paramètre la parabole : `xs = np.linspace(-4, 4, 40001)`, `ys = xs**2 / 2 - 2`, puis `i = np.argmin(f_31(xs, ys))`. Les lignes de niveau : `ax.contour(GX, GY, f_31(GX, GY), levels=[...])` sur une grille `np.meshgrid`.

</details>
<details><summary>Indice 3</summary>

Pour les flèches, divise chaque gradient par sa norme et multiplie par une même longueur, puis `ax.annotate("", xy=point + v, xytext=point, arrowprops={"arrowstyle": "->"})`. N'appelle ni `plt.figure` ni `plt.subplots` : dessine dans `ax`. Termine par `return (x, y)`.

</details>

### Ex M13b.32 — Chasse à l'erreur : le signe d'un multiplicateur, une largeur de bande 1/‖w‖ au lieu de 2/‖w‖, une matrice de Gram non symétrique

<details><summary>Indice 1</summary>

Relis chaque commentaire, puis la fiche : §3 (le signe de μ), §6 (marge et bande), §7 (la somme dans $J$), §8 (la matrice de Gram et le RBF).

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, demande-toi : quelle forme a le résultat ? quel facteur, quel signe, quelle somme ? Deux lignes presque identiques calculent deux choses différentes : laquelle des deux est fausse ?

</details>
<details><summary>Indice 3</summary>

Quatre lignes sont fausses ; une matrice de Gram des exemples est carrée et symétrique ; une condition KKT a quatre parties. d) La somme des coefficients de $\mathbf{X}\mathbf{X}^\top$ vaut $\lVert\sum_i \mathbf{x}_i\rVert^2$.

</details>

### Ex M13b.33 — Vérifier une solution KKT : faisabilité, stationnarité, complémentarité

<details><summary>Indice 1</summary>

Relis « Les conditions KKT » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Calcule une fois `gs = [g(x) for g, _ in constraints]` et le gradient du lagrangien `grad_f(x) + sum(m * dg(x) for m, (_, dg) in zip(mu, constraints))`.

</details>
<details><summary>Indice 3</summary>

Rends `{"feasibility": all(v <= tol for v in gs), "stationarity": bool(np.all(np.abs(grad_L) <= tol)), "sign": all(m >= -tol for m in mu), "complementarity": all(abs(m * v) <= tol for m, v in zip(mu, gs))}`.

</details>

### Ex M13b.34 — Défi : une SVM linéaire entraînée par sous-gradient, un objectif à 1 % de celui de scikit-learn au même C

<details><summary>Indice 1</summary>

Commence par la descente de M13b.30 (un pas décroissant $\eta_0/\sqrt{t}$, le **meilleur** point vu), et regarde où elle bloque : affiche $b$, $g_b$ et $\mathbf{g}_{\mathbf{w}}$ au fil des pas.

</details>
<details><summary>Indice 2</summary>

Les exemples sont loin de l'origine : $\lvert b \rvert$ doit être grand (une vingtaine), mais chaque coordonnée de $\mathbf{g}_{\mathbf{w}}$ est dominée par la moyenne des features. Cherche un changement de variable qui ne change pas $J$ : $\mathbf{w} \cdot \mathbf{x} + b = \mathbf{w} \cdot (\mathbf{x} - \mathbf{m}) + (b + \mathbf{w} \cdot \mathbf{m})$, avec $\mathbf{m}$ la moyenne des exemples.

</details>
<details><summary>Indice 3</summary>

Descends sur les exemples centrés `X - m` (même `y`, même `C`), avec $\eta_t = 0{,}01/\sqrt{t}$ et quelques milliers de pas, en gardant le meilleur $(\mathbf{w}, b')$ ; rends $(\mathbf{w}, b' - \mathbf{w} \cdot \mathbf{m})$. Ne divise pas les features par leur écart-type : cela changerait $\lVert\mathbf{w}\rVert$, donc le problème.

</details>
