# M05b · Fonctions de plusieurs variables et gradient — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 📈 🗣️ Pont, lecture, graphique et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M05b.Q1 — Lire des lignes de niveau

<details><summary>Indice 1</summary>

Relis « Les lignes de niveau » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Une ligne de niveau $c$ est l'ensemble des points où $f$ vaut $c$ : une fonction n'a qu'une valeur en chaque point.

</details>
<details><summary>Indice 3</summary>

4 : $x^2 + y^2$ est le carré de la distance à l'origine. 5 : cherche une valeur que $x^2 + y^2$ ne prend jamais.

</details>

### M05b.Q2 — Dérivées partielles : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Figer une variable » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Pour $\frac{\partial}{\partial x}$, $y$ se comporte comme un nombre : $y^3$ reste en facteur, $\sin y$ est une constante.

</details>
<details><summary>Indice 3</summary>

5 : une fonction qui ne dépend que de $y$. 6 : la règle de la chaîne, avec $u = xy$.

</details>

### M05b.Q3 — Où pointe le gradient ?

<details><summary>Indice 1</summary>

Relis « La direction de plus grande pente » et « Le gradient est orthogonal aux lignes de niveau » (fiche §4).

</details>
<details><summary>Indice 2</summary>

La pente dans la direction $\mathbf{u}$ vaut $\|\nabla f\|\cos\theta$ : quand est-elle la plus grande ?

</details>
<details><summary>Indice 3</summary>

4 : $\nabla f = (-2x, -2y)$. 6 : dérive $2f$ : que deviennent les dérivées partielles ?

</details>

### M05b.Q4 — La dérivée directionnelle

<details><summary>Indice 1</summary>

Relis « La pente dans une direction » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$, avec $\mathbf{u}$ de norme 1 : un vecteur qui ne l'est pas se divise d'abord par sa norme.

</details>
<details><summary>Indice 3</summary>

5 : la plus grande pente est la norme du gradient. 6 : un vecteur orthogonal à $(a, b)$ est $(b, -a)$ ; divise-le par sa norme.

</details>

### M05b.Q5 — Le plan tangent

<details><summary>Indice 1</summary>

Relis « Le plan qui touche la surface » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Il faut $f(a, b)$ et les deux dérivées partielles en $(a, b)$, puis les décalages $(x - a)$ et $(y - b)$.

</details>
<details><summary>Indice 3</summary>

2 : $f(1, 1) = 2$, $f_x = 2x$, $f_y = 1$. 5 : relis « Quand il n'y a pas de plan tangent ».

</details>

### M05b.Q6 — Minimum, maximum ou selle ?

<details><summary>Indice 1</summary>

Relis le test du second ordre (fiche §7).

</details>
<details><summary>Indice 2</summary>

Calcule d'abord $D = f_{xx}f_{yy} - f_{xy}^2$ : son signe passe avant celui de $f_{xx}$.

</details>
<details><summary>Indice 3</summary>

3 : $f_{xx}$ et $f_{yy}$ sont positifs, mais regarde $D$. 6 : calcule $f_{yy}$ de $y^4$ en 0.

</details>

### M05b.Q7 — Descendre ou monter

<details><summary>Indice 1</summary>

Relis « Descendre la plus grande pente » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Descendre : retirer $\eta\,\nabla f$ ; monter : l'ajouter. La baisse prévue vient de l'approximation linéaire.

</details>
<details><summary>Indice 3</summary>

3 : $\nabla f = (2x, 8y)$ en $(1, 1)$. 4 : de quoi dépend la longueur d'un pas, $\eta\,\nabla f$ ? 6 : une somme de carrés est nulle quand chaque carré l'est.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M05b.R1 — Dériver une composée (R7)

<details><summary>Indice 1</summary>

$(g(u))' = g'(u)\,u'$ : la dérivée de l'extérieur, prise en $u$, fois la dérivée de l'intérieur.

</details>
<details><summary>Indice 2</summary>

1 : $(u^5)' = 5u^4 u'$. 3 : $(\ln u)' = \frac{u'}{u}$. 4 : $(\sqrt{u})' = \frac{u'}{2\sqrt{u}}$.

</details>
<details><summary>Indice 3</summary>

2 : $(e^u)' = u'\,e^u$, avec $u = 3x^2 - x$. 4 : l'intérieur $4 - x$ a pour dérivée $-1$.

</details>

### M05b.R2 — Produit scalaire et norme (R9)

<details><summary>Indice 1</summary>

$(a, b) \cdot (c, d) = ac + bd$ et $\|(a, b)\| = \sqrt{a^2 + b^2}$.

</details>
<details><summary>Indice 2</summary>

Un vecteur unitaire : le vecteur divisé par sa norme. L'angle : $\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|}$.

</details>
<details><summary>Indice 3</summary>

5 : échange les deux composantes et change un signe.

</details>

### M05b.R3 — Dérivée seconde et convexité (M05a)

<details><summary>Indice 1</summary>

Relis M05a §1 et §2 (le test de la dérivée seconde).

</details>
<details><summary>Indice 2</summary>

Convexe là où $f'' \ge 0$.

</details>
<details><summary>Indice 3</summary>

4 : $(\cos x)' = -\sin x$ ; le test ne conclut que si $f''(c) \ne 0$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M05b.1 — Les lignes de niveau de trois fonctions

<details><summary>Indice 1</summary>

Relis « Les lignes de niveau » et l'exemple de $2x^2 + y^2$ (fiche §1).

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne de niveau, écris l'équation $f(x, y) = c$ et isole $y$ quand c'est possible (a, b, f) ; pour couper un axe, remplace l'autre variable par 0 (c, d).

</details>
<details><summary>Indice 3</summary>

b) Écris la ligne $3x - y + 2 = c$ sous la forme $y = \ldots$ : le coefficient de $x$ ne dépend pas de $c$. h) Quel est le signe de $x^2 + 9y^2$ ?

</details>

### Ex M05b.2 — Dérivées partielles

<details><summary>Indice 1</summary>

Relis « Figer une variable » et l'exemple $x^3 y + 2y^2$ (fiche §2).

</details>
<details><summary>Indice 2</summary>

Pour $\frac{\partial}{\partial x}$, traite $y$ comme un nombre, et inversement. Pour $g$, la règle de la chaîne avec $u = 2x - y$.

</details>
<details><summary>Indice 3</summary>

e) et f) Calcule d'abord $2x - y$ au point : il vaut 0. g) et h) $h = x\,y^2 z^3$ : seule la puissance de la variable dérivée descend.

</details>

### Ex M05b.3 — Le gradient en un point et sa norme

<details><summary>Indice 1</summary>

Relis « Le gradient » (fiche §3) ; une norme, R9.

</details>
<details><summary>Indice 2</summary>

Dérive par rapport à $x$ en traitant $y$ comme un nombre, puis l'inverse ; remplace ensuite par les coordonnées du point.

</details>
<details><summary>Indice 3</summary>

d) Le système $2xy = 0$, $x^2 - 3 = 0$ : la seconde équation donne $x$, puis la première donne $y$. e) Divise le gradient par sa norme.

</details>

### Ex M05b.4 — La dérivée directionnelle dans plusieurs directions

<details><summary>Indice 1</summary>

Relis « La pente dans une direction » et l'erreur classique qui suit (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\nabla f(P)$ d'abord ; puis, pour chaque direction, un vecteur **unitaire** et le produit scalaire.

</details>
<details><summary>Indice 3</summary>

c) $\|(7, 24)\| = 25$. e) La direction de $P$ vers $Q$ est celle du vecteur $Q - P$. g) $\cos\theta = \frac{\nabla f \cdot (1, 1)}{\|\nabla f\|\,\sqrt{2}}$, puis l'arc cosinus, en degrés.

</details>

### Ex M05b.5 — Monter le plus vite : la direction et la valeur de la plus grande pente

<details><summary>Indice 1</summary>

Relis « La direction de plus grande pente » et l'exemple du dôme (fiche §4) ; les angles, R9.

</details>
<details><summary>Indice 2</summary>

Le terme $xy$ compte dans les deux dérivées partielles. La plus grande pente vaut $\|\nabla T\|$. Pour d), un vecteur unitaire qui va de $P$ vers $O$.

</details>
<details><summary>Indice 3</summary>

c) Dans quel quadrant pointe le gradient ? Pars de l'angle aigu $\arctan\frac{3}{5}$. e) $\cos\theta = \frac{\nabla T \cdot \mathbf{w}}{\|\nabla T\|\,\|\mathbf{w}\|}$. f) La tangente à l'isotherme est orthogonale au gradient : trouve un vecteur qui la dirige.

</details>

### Ex M05b.6 — Le plan tangent et l'approximation d'une valeur

<details><summary>Indice 1</summary>

Relis « Le plan qui touche la surface » et l'exemple de $\sqrt{x^2 + y^2}$ (fiche §5).

</details>
<details><summary>Indice 2</summary>

Dérive $x^2\sqrt{y}$ par rapport à chaque variable, l'autre restant un nombre ($\sqrt{y}$ se dérive comme $y^{1/2}$). Le plan : $z = f(3, 4) + f_x\,(x - 3) + f_y\,(y - 4)$.

</details>
<details><summary>Indice 3</summary>

d) Développe le plan et regroupe les constantes. e) Le déplacement est $(0{,}1 ;\ -0{,}1)$.

</details>

### Ex M05b.7 — Dérivées secondes croisées : le théorème de Schwarz vérifié

<details><summary>Indice 1</summary>

Relis « Quatre dérivées secondes » et « La courbure dans une direction » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Écris d'abord $f_x$ et $f_y$. Pour $f_{xy}$, dérive $f_x$ par rapport à $y$ ; $y\,e^{xy}$ est un produit de deux fonctions de $y$.

</details>
<details><summary>Indice 3</summary>

f) et g) Divise chaque vecteur par sa norme : $u_1^2 = u_2^2 = \frac{1}{2}$, et $u_1 u_2 = \pm\frac{1}{2}$. N'oublie pas le facteur 2 du terme croisé.

</details>

### Ex M05b.8 — Les points critiques et leur nature (test du second ordre)

<details><summary>Indice 1</summary>

Relis « Les candidats » et l'exemple $x^3 + y^3 - 3xy$ (fiche §7).

</details>
<details><summary>Indice 2</summary>

Résous $f_x = 0$ et $f_y = 0$, puis calcule $f_{xx}$, $f_{yy}$, $f_{xy}$ et $D$ en chaque point.

</details>
<details><summary>Indice 3</summary>

e) et f) Avec $x^2 + y^2 = 5$ et $xy = 2$ : calcule $(x + y)^2$ et $(x - y)^2$. $D = 36(x^2 - y^2)$. h) Calcule les trois dérivées secondes de $(x + y)^2$ en $(0, 0)$.

</details>

### Ex M05b.9 — Pourquoi un petit pas contre le gradient fait baisser f : le calcul au premier ordre

<details><summary>Indice 1</summary>

Relis « Pourquoi la fonction baisse » (fiche §8).

</details>
<details><summary>Indice 2</summary>

Calcule $\nabla f(P)$ (les deux dérivées partielles en $P$) ; un pas de descente retire $\eta\,\nabla f(P)$, un pas de montée l'ajoute.

</details>
<details><summary>Indice 3</summary>

d) $\|\nabla f(P)\|^2$, le carré de la norme. g) La baisse prévue vaut $\eta\,\|\nabla f(P)\|^2$ : écris l'équation en $\eta$.

</details>

### Ex M05b.10 — argmin et argmax sur un segment

<details><summary>Indice 1</summary>

Relis « min et argmin » (fiche §8) et « Extrema globaux sur une partie bornée » (fiche §7).

</details>
<details><summary>Indice 2</summary>

Remplace $x$ par $4t$ et $y$ par $2 - 2t$ dans $f$ : $g(t)$ est un trinôme. Étudie-le sur $[0, 1]$, bords compris.

</details>
<details><summary>Indice 3</summary>

f) Complète le carré en $x$ (R2). h) Calcule $\nabla f$ au point trouvé en b).

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M05b.11 — La dérivée directionnelle vaut ∇f · u, et la plus grande pente

<details><summary>Indice 1</summary>

Relis « D'où vient cette formule » (fiche §3) et le §4.

</details>
<details><summary>Indice 2</summary>

1 : compare la définition de $D_{\mathbf{u}} f$ et celle de $g'(0)$. 2 : $x(t) = a + tu_1$ et $y(t) = b + tu_2$ dans la règle de la chaîne. 3 : l'inégalité de Cauchy-Schwarz (R9).

</details>
<details><summary>Indice 3</summary>

4 : pour l'unicité, calcule $\|\mathbf{u} - \mathbf{u}^*\|^2$ en développant. 5 : les vecteurs orthogonaux à $(A, B)$ sont les multiples de $(B, -A)$ ; lesquels ont pour norme 1 ?

</details>

### Ex M05b.12 — Le gradient est orthogonal aux lignes de niveau

<details><summary>Indice 1</summary>

Relis « Le gradient est orthogonal aux lignes de niveau » (fiche §4).

</details>
<details><summary>Indice 2</summary>

1 : $t \mapsto f(\boldsymbol{\gamma}(t))$ est constante ; dérive-la avec la règle de la chaîne. 3 : un point $(x, y)$ est sur la tangente si $(x - a, y - b)$ est orthogonal au gradient.

</details>
<details><summary>Indice 3</summary>

5 : avance d'une distance $s$ dans la direction $\mathbf{u}$ ; au premier ordre, $f$ change de $s\,\nabla f \cdot \mathbf{u}$. Quand ce changement vaut-il $\Delta c$ ?

</details>

### Ex M05b.13 — Le test du second ordre pour ax² + bxy + cy²

<details><summary>Indice 1</summary>

Relis « Trois natures » (fiche §7) ; la forme canonique, R2.

</details>
<details><summary>Indice 2</summary>

2 : développe $(2ax + by)^2$. 3 : distingue $y \ne 0$ et $y = 0$. 4 : cherche un point où le carré $(2ax + by)^2$ s'annule.

</details>
<details><summary>Indice 3</summary>

4 : $q(tx, ty) = t^2 q(x, y)$ permet de s'approcher de l'origine. 5 : factorise $q = y\,(bx + cy)$ et regarde $q$ sur une droite $x = ky$. 6 : $a = f_{xx}$, $b = 2f_{xy}$, $c = f_{yy}$.

</details>

<a id="reflexion"></a>

## 🔗 📖 📈 🗣️ Pont, lecture, graphique et explication

### Ex M05b.14 — La loss d'un neurone à deux poids sur deux exemples : son gradient

<details><summary>Indice 1</summary>

Relis l'exemple de descente (fiche §8) ; la loss est une fonction de $w_1$ et $w_2$.

</details>
<details><summary>Indice 2</summary>

Calcule d'abord les deux prédictions et les deux erreurs $\hat{y} - y$. La dérivée de $\frac{1}{2}(\hat{y} - y)^2$ par rapport à $w_j$ est l'erreur fois $x_j$.

</details>
<details><summary>Indice 3</summary>

f) Le gradient s'annule si les deux erreurs s'annulent : deux équations linéaires en $w_1$ et $w_2$.

</details>

### Ex M05b.15 — MML §5.2 : dérivées partielles et gradient, la convention en ligne (lecture guidée)

<details><summary>Indice 1</summary>

Lis le début du §5.2 et ses exemples avant de répondre ; le guide de lecture de la fiche dit où.

</details>
<details><summary>Indice 2</summary>

2 : la règle de la chaîne avec $u = x - 3y^2$. 5 : $\frac{df}{dt} = \frac{\partial f}{\partial x_1}\frac{dx_1}{dt} + \frac{\partial f}{\partial x_2}\frac{dx_2}{dt}$.

</details>
<details><summary>Indice 3</summary>

6 : quelle est la forme d'un produit (ligne) × (colonne) ? Et pour que $\mathbf{x} - \eta\,(\ldots)$ ait un sens, quelle forme faut-il au gradient ?

</details>

### Ex M05b.16 — Lire une carte de lignes de niveau : estimer une dérivée partielle

<details><summary>Indice 1</summary>

Relis « Lignes serrées, gradient long » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Chacun des points $A$, $B$ et $C$ est sur une ligne de niveau : lis sa valeur. Un taux d'accroissement : la différence des valeurs divisée par la distance.

</details>
<details><summary>Indice 3</summary>

f) Trace le segment $[PQ]$ à la règle et compte les lignes qu'il coupe, une à une, de $P$ à $Q$.

</details>

### Ex M05b.17 — Expliquer ce que disent des lignes de niveau serrées

<details><summary>Indice 1</summary>

Relis le §4 de la fiche, puis ferme-la.

</details>
<details><summary>Indice 2</summary>

Quatre idées : l'écart et la pente, la direction du gradient, sa longueur, le sentier plat.

</details>
<details><summary>Indice 3</summary>

Sur quel chemin l'altitude ne change-t-elle pas ? Quel angle fait-il avec le gradient ?

</details>

<a id="entretien"></a>

## 💼 Entretien

### M05b.E1 — Pourquoi le gradient est-il la direction de plus grande pente ?

<details><summary>Indice 1</summary>

Relis le §4 de la fiche et la démonstration M05b.11.

</details>
<details><summary>Indice 2</summary>

Écris la pente comme un produit scalaire, puis avec un cosinus.

</details>
<details><summary>Indice 3</summary>

Pour la descente : l'approximation linéaire avec $\mathbf{h} = -\eta\,\nabla f$.

</details>

<a id="notebook"></a>

## Notebook

### Ex M05b.18 — Une dérivée partielle par différence centrée · `partial_derivative`

<details><summary>Indice 1</summary>

Relis « Sur ordinateur » (fiche §2) et la différence centrée de M05a §5.

</details>
<details><summary>Indice 2</summary>

Dans l'ordre : la copie que demande le commentaire `TODO`, les deux vérifications (`i`, puis `h`), puis la différence centrée.

</details>
<details><summary>Indice 3</summary>

`p = np.array(point, dtype=float)` ; `step = np.zeros_like(p)` ; `step[i] = h` ; `(f(p + step) - f(p - step)) / (2 * h)`, converti par `float(...)`.

</details>

### Ex M05b.19 — Dérivée directionnelle et direction de plus grande pente · `directional_derivative, steepest_ascent_direction`

<details><summary>Indice 1</summary>

Relis « Sur ordinateur » (fiche §3) et le §4.

</details>
<details><summary>Indice 2</summary>

`directional_derivative` : normalise la direction, puis une différence centrée le long de `u`. `steepest_ascent_direction` : une `partial_derivative` par coordonnée.

</details>
<details><summary>Indice 3</summary>

`u = d / np.linalg.norm(d)` après avoir vérifié que la norme n'est pas nulle ; `np.array([partial_derivative(f, p, i, h) for i in range(p.size)])`, puis la norme, comparée à `1e-8` (pas à 0 : en un point critique, le gradient calculé est minuscule, pas forcément nul), et la division.

</details>

### Ex M05b.20 — Le plan tangent · `tangent_plane`

<details><summary>Indice 1</summary>

Relis « Le plan qui touche la surface » (fiche §5), surtout la forme développée.

</details>
<details><summary>Indice 2</summary>

$A$ et $B$ sont les deux dérivées partielles ; $C$ fait passer le plan par $(x_0, y_0, f(x_0, y_0))$.

</details>
<details><summary>Indice 3</summary>

`c = float(f(p)) - a * p[0] - b * p[1]`, et `return (float(a), float(b), float(c))`.

</details>

### Ex M05b.21 — SymPy : dérivées partielles, gradient, points critiques

<details><summary>Indice 1</summary>

Relis l'énoncé : il donne les quatre outils de SymPy.

</details>
<details><summary>Indice 2</summary>

`sp.solve([sp.diff(k, x), sp.diff(k, y)], [x, y], dict=True)` donne la liste des points critiques.

</details>
<details><summary>Indice 3</summary>

b) Classe les points par le signe de $D$ et de $k_{xx}$, puis remplace le minimum dans `k` avec `.subs`. c) `sp.hessian(k, (x, y)).det().subs({x: 1, y: 0})`.

</details>

### Ex M05b.22 — Prédire : la dérivée directionnelle le long d'une ligne de niveau

<details><summary>Indice 1</summary>

Relis le §4 de la fiche : que vaut la pente à angle droit du gradient ?

</details>
<details><summary>Indice 2</summary>

Pour b), une pente nulle ne veut pas dire une fonction constante : calcule $f(P + t\,\mathbf{u})$ en fonction de $t$.

</details>
<details><summary>Indice 3</summary>

d) La pente vaut $\|\nabla f\|\cos\theta$ : pour combien d'angles $\theta$ (entre 0° et 360°) le cosinus est-il nul ?

</details>

### Ex M05b.23 — L'erreur du plan tangent quand on s'éloigne du point

<details><summary>Indice 1</summary>

Relis « L'approximation linéaire » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Le vecteur unitaire, le point $q = \mathbf{p} + r\,\mathbf{u}$, les coefficients du plan tangent, puis l'écart en valeur absolue.

</details>
<details><summary>Indice 3</summary>

`u = np.array(direction, dtype=float)`, `u = u / np.linalg.norm(u)`, `q = p + r * u`, `a, b, c = mymath.multivar.tangent_plane(f, p)`, `abs(f(q) - (a * q[0] + b * q[1] + c))`.

</details>

### Ex M05b.24 — Lignes de niveau et flèches du gradient sur la même figure

<details><summary>Indice 1</summary>

Relis la figure du dôme (fiche §4).

</details>
<details><summary>Indice 2</summary>

Deux grilles : une fine pour `ax.contour`, une grossière pour `ax.quiver` (quelques centaines de flèches au plus), toutes deux faites par `np.meshgrid`.

</details>
<details><summary>Indice 3</summary>

`X, Y = np.meshgrid(np.linspace(*xlim, 200), np.linspace(*ylim, 200))` ; `cs = ax.contour(X, Y, f(X, Y), levels=10)` ; `ax.clabel(cs)` ; une grille de 13 × 13 points pour `U, V = grad(XA, YA)` et `ax.quiver(XA, YA, U, V)` ; `ax.set_aspect("equal")`.

</details>

### Ex M05b.25 — Chasse à l'erreur : la mauvaise variable dérivée, une direction non unitaire

<details><summary>Indice 1</summary>

Relis le tableau des pièges classiques de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, calcule à la main ce qu'elle donne, puis ce que dit son commentaire.

</details>
<details><summary>Indice 3</summary>

Trois questions utiles : quelle coordonnée chaque différence finie déplace-t-elle ? Chaque direction est-elle unitaire ? Chaque pas va-t-il dans le bon sens ?

</details>

### Ex M05b.26 — Vectoriser : une fonction de deux variables sur une grille (`np.meshgrid`)

<details><summary>Indice 1</summary>

Relis l'énoncé : il dit ce que donne `np.meshgrid(xs, ys)`.

</details>
<details><summary>Indice 2</summary>

Deux lignes suffisent.

</details>
<details><summary>Indice 3</summary>

`X, Y = np.meshgrid(xs, ys)`, puis `f(X, Y)`, converti en tableau de flottants.

</details>

### Ex M05b.27 — Défi : retrouver une fonction du second degré à partir de son gradient

<details><summary>Indice 1</summary>

Écris $\nabla f(x, y)$ en fonction des cinq coefficients.

</details>
<details><summary>Indice 2</summary>

En quel point le gradient ne dépend-il que de $d$ et $e$ ? Et en quels points ne fait-il apparaître qu'un seul coefficient de plus ?

</details>
<details><summary>Indice 3</summary>

Essaie $(0, 0)$, $(1, 0)$ et $(0, 1)$ : chacun donne deux nombres, et une soustraction isole chaque coefficient (attention au facteur 2 devant $a$ et $c$).

</details>
