# M10 · Séparabilité linéaire et convexité — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m10_separabilite_convexite/06_mes_reponses.md` (créée par `python tools/start_chapter.py M10`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : les points sont $\mathbf{x}_i \in \mathbb{R}^d$, leurs labels $y_i \in \{-1, +1\}$ ; le **score** d'un point pour le couple $(\mathbf{w}, b)$ est $\mathbf{w} \cdot \mathbf{x} + b$ ; un couple **sépare** les deux classes quand $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) > 0$ pour tout $i$ ; sa **marge** (géométrique) est $\min_i \frac{y_i(\mathbf{w} \cdot \mathbf{x}_i + b)}{\lVert \mathbf{w} \rVert}$. Le **produit vectoriel** de deux vecteurs du plan est $\mathbf{u} \times \mathbf{v} = u_1v_2 - u_2v_1$ (fiche §2).

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M10.Q1 — Convexe ou non ? 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Pour chaque ensemble, réponds « convexe » ou « non convexe » ; pour un « non convexe », donne deux points de l'ensemble dont le segment en sort.
1. Un triangle plein.
2. Un cercle : la courbe seule, sans l'intérieur.
3. L'ensemble des points $(x, y)$ du plan tels que $y \ge |x|$.
4. L'ensemble des points $(x, y)$ tels que $xy \ge 0$.
5. Une droite privée d'un de ses points.
6. L'ensemble des vecteurs de poids $\mathbf{w} \in \mathbb{R}^2$ tels que $\lVert \mathbf{w} \rVert_1 \le 3$.

### M10.Q2 — L'enveloppe convexe : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

Vrai ou faux ?
1. $\operatorname{conv}(S)$ contient $S$.
2. Si $S$ est convexe, $\operatorname{conv}(S) = S$.
3. Chaque point d'un nuage fini du plan est un sommet de son enveloppe convexe.
4. L'enveloppe convexe de trois points alignés est un triangle.
5. Le barycentre d'un nuage de points est toujours dans son enveloppe convexe.
6. Ajouter un point à un nuage ne fait jamais baisser le nombre de sommets de son enveloppe convexe.

### M10.Q3 — Séparable ou non ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

Les deux classes sont-elles linéairement séparables ? Pour chaque « non », donne un point commun aux deux enveloppes convexes.
1. En dimension 1 : la classe $+1$ en $1$ et $2$ ; la classe $-1$ en $4$ et $7$.
2. En dimension 1 : la classe $+1$ en $0$ et $6$ ; la classe $-1$ en $3$.
3. Dans le plan : la classe $+1$ en $(0, 0)$, $(4, 0)$ et $(0, 4)$ ; la classe $-1$ en $(1, 2)$.
4. Dans le plan : la classe $+1$ en huit points régulièrement répartis sur un cercle de centre $(0, 0)$ ; la classe $-1$ au centre.
5. Dans le plan : trois points non alignés, avec des labels quelconques.
6. Deux exemples au même endroit, avec deux labels différents.

### M10.Q4 — Marge et astuce du biais 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C*

1. On multiplie $\mathbf{w}$ et $b$ par 3. Que deviennent la marge géométrique, et les marges fonctionnelles $y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ ?
2. Le couple $(\mathbf{w}, b)$ sépare les deux classes. Que fait le couple $(-\mathbf{w}, -b)$, et quel est le signe de sa marge ?
3. Avec l'astuce du biais, écris $\tilde{\mathbf{x}}$ pour $\mathbf{x} = (2, -1)$ et $\tilde{\mathbf{w}}$ pour $(\mathbf{w}, b) = ((1, 4), -3)$, puis calcule $\tilde{\mathbf{w}} \cdot \tilde{\mathbf{x}}$.
4. Vrai ou faux : l'ensemble des $\tilde{\mathbf{x}} \in \mathbb{R}^3$ tels que $\tilde{\mathbf{w}} \cdot \tilde{\mathbf{x}} = 0$ passe par l'origine de $\mathbb{R}^3$.
5. Un couple $(\mathbf{w}, b)$ a une marge exactement nulle sur des données. Que peux-tu en dire ?
6. Les enveloppes convexes de deux nuages sont à la distance 6 l'une de l'autre. Quelle est la plus grande marge possible d'un séparateur ?

<a id="rappels"></a>

## 🔁 Rappels

### M10.R1 — Hyperplans et distance à un hyperplan (M07) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

Le plan $P$ de $\mathbb{R}^3$ a pour équation $2x - y + 2z - 3 = 0$.
1. Donne un vecteur normal $\mathbf{w}$ et sa norme.
2. La distance de l'origine à $P$ ?
3. La distance signée du point $(2, 1, 1)$ à $P$ ?
4. L'origine et $(2, 1, 1)$ sont-ils du même côté de $P$ ?
5. Le point de $P$ le plus proche de l'origine ?

### M10.R2 — L'inégalité de Cauchy-Schwarz (M07) 🔁 ★ ⏱️ 5 min
*Fiche §4 · parcours C, E*

1. Énonce l'inégalité de Cauchy-Schwarz pour deux vecteurs $\mathbf{u}$ et $\mathbf{v}$ de $\mathbb{R}^n$.
2. Vérifie-la pour $\mathbf{u} = (3, 0, 4)$ et $\mathbf{v} = (2, 1, -2)$.
3. Dans quel cas est-elle une égalité ?
4. Pour un vecteur $\mathbf{e}$ de norme 1, montre que $\mathbf{e} \cdot \mathbf{v} \le \lVert \mathbf{v} \rVert$. Pour quel $\mathbf{e}$ a-t-on l'égalité ?
5. Si $a^2 + b^2 + c^2 = 4$, quelle est la plus grande valeur possible de $3a + 4c$ ?

### M10.R3 — La sigmoïde et tanh (R6) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C*

$\sigma(z) = \frac{1}{1 + e^{-z}}$.
1. $\sigma(0)$, et les limites de $\sigma$ en $-\infty$ et en $+\infty$ ?
2. Montre que $\sigma(-z) = 1 - \sigma(z)$.
3. $\sigma(\ln 3)$ ?
4. Sachant que $\tanh(z) = 2\sigma(2z) - 1$, calcule $\tanh\big(\frac{\ln 3}{2}\big)$.
5. Pour quel $x$ a-t-on $\sigma(2x - 1) = \frac{1}{2}$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Fais un **dessin** pour chaque exercice du plan : il évite la moitié des erreurs. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets pour un point ou un vecteur, comme `[2, -1]` ; une liste de points comme une liste de listes, `[[1, 0], [-2, 3]]` ;
- vrai ou faux par `True` ou `False` ; une ou plusieurs lettres entre guillemets, comme `"BD"` ;
- un intervalle entre guillemets, avec des crochets tournés vers l'extérieur pour une borne exclue, comme `"]0 ; 4]"`.

### Ex M10.1 — Convexe ou non : segments, demi-plans, intersections ✏️ ★ ⏱️ 15 min
**Objectif :** paramétrer un segment, reconnaître des ensembles convexes, et décrire un polygone convexe comme une intersection de demi-plans.
**Prérequis :** fiche §1 · **Parcours :** C, E

On note $\mathbf{a} = (-3, 2)$ et $\mathbf{b} = (5, -2)$. Pour c) : $A$ est le disque $x^2 + y^2 \le 9$ ; $B$ l'ensemble $x^2 + y^2 \ge 1$ ; $C$ l'ensemble $y \ge x^2$ ; $D$ l'ensemble $y \le x^2$ ; $E$ l'ensemble $|x| + 2|y| \le 2$ ; $F$ l'ensemble des points tels que $x > 0$ et $xy \ge 1$ ; $G$ la réunion des bandes $|x| \le 1$ et $|y| \le 1$. Pour d) à g) : $K$ est l'ensemble des points qui vérifient à la fois $x \ge 0$, $y \ge 0$, $2x + y \le 8$ et $x + 2y \le 7$.

| | Question | Réponse attendue |
|---|---|---|
| a | le point $(1 - t)\mathbf{a} + t\mathbf{b}$ pour $t = 0{,}25$ | une liste de 2 nombres |
| b | le $t \in [0, 1]$ tel que $(1 - t)\mathbf{a} + t\mathbf{b} = (3, -1)$ | un nombre |
| c | les lettres des ensembles convexes, parmi $A$ à $G$ | des lettres |
| d | le sommet de $K$ qui n'est sur aucun des deux axes | une liste de 2 nombres |
| e | le nombre de sommets de $K$ | un entier |
| f | les lettres des points qui appartiennent à $K$, parmi $P = (2{,}5 ;\ 2)$, $Q = (1 ;\ 3{,}2)$, $R = (3{,}8 ;\ 0{,}5)$ et $S = (0 ;\ 3{,}5)$ | des lettres |
| g | la combinaison convexe $0{,}5\,(2, 0) + 0{,}3\,(0, 2) + 0{,}2\,(2, 2)$ | une liste de 2 nombres (1 décimale) |

Dans ta copie : dessine $K$. Pour chaque ensemble non convexe de c), donne deux points dont le segment sort de l'ensemble. Vérifie que les trois points de g) sont dans $K$ : pourquoi leur combinaison convexe y est-elle aussi, sans rien calculer ?

### Ex M10.2 — L'enveloppe convexe de huit points, à la main ✏️ ★ ⏱️ 15 min
**Objectif :** construire l'enveloppe convexe d'un nuage du plan par le test d'orientation, et calculer son aire.
**Prérequis :** fiche §2 · **Parcours :** C, E

Les huit points : $P_1 = (3, 5)$, $P_2 = (-1, 2)$, $P_3 = (-3, 1)$, $P_4 = (5, 0)$, $P_5 = (3, 3)$, $P_6 = (4, 3)$, $P_7 = (-2, 0)$, $P_8 = (0, -2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de sommets de l'enveloppe convexe | un entier |
| b | les sommets, dans le sens direct, en partant du plus petit point (le plus petit $x$, puis le plus petit $y$) | une liste de points |
| c | le numéro du point qui est sur un côté de l'enveloppe sans en être un sommet | un entier |
| d | le produit vectoriel $(P_6 - P_4) \times (P_1 - P_4)$ | un nombre |
| e | l'aire de l'enveloppe convexe | un nombre |
| f | vrai ou faux : le point $Q = (4, 4)$ est dans l'enveloppe convexe | `True` ou `False` |
| g | le nombre de sommets de l'enveloppe convexe des huit points et de $Q$ | un entier |

Pour e), découpe le polygone en triangles qui partent d'un même sommet : l'aire de chacun est la moitié d'un produit vectoriel. Dans ta copie : fais tourner la chaîne monotone d'Andrew sur la chaîne du bas, en écrivant chaque test. Que dit le signe de d) sur le point $P_6$ ? Pour g), compare les sommets des deux enveloppes : lesquels changent, et pourquoi ?

### Ex M10.3 — Une droite qui sépare deux petits nuages, et sa marge ✏️ ★★ ⏱️ 20 min
**Objectif :** vérifier qu'une droite sépare deux nuages, calculer sa marge, la régler au mieux à direction fixée, puis trouver la plus grande marge possible.
**Prérequis :** fiche §3 · **Parcours :** C, E

La classe $+1$ : $P_1 = (7, 6)$, $P_2 = (7, 5)$, $P_3 = (3, 6)$. La classe $-1$ : $P_4 = (0, 2)$, $P_5 = (-2, 3)$, $P_6 = (1, 0)$. On propose $\mathbf{w} = (2, 1)$ et $b = -4$.

| | Question | Réponse attendue |
|---|---|---|
| a | les six scores $\mathbf{w} \cdot P_i + b$, de $P_1$ à $P_6$ | une liste de 6 nombres |
| b | la marge géométrique de $(\mathbf{w}, b)$ | un nombre (4 décimales) |
| c | les numéros des points les plus proches de la droite de b), dans l'ordre croissant | une liste d'entiers |
| d | l'ensemble des $b$ pour lesquels $((2, 1), b)$ sépare les deux classes | un intervalle |
| e | le $b$ qui donne la plus grande marge avec $\mathbf{w} = (2, 1)$ | un nombre |
| f | cette marge | un nombre (4 décimales) |
| g | la plus grande marge possible, toutes directions $\mathbf{w}$ confondues | un nombre |

Dans ta copie : dessine les deux nuages et les droites de b) et de e). Pour g), trouve le couple de points (un dans chaque enveloppe) le plus proche, puis l'équation de la droite de plus grande marge, et vérifie sa marge sur les six points.

### Ex M10.4 — L'astuce du biais : une droite du plan devient un plan de ℝ³ passant par l'origine ✏️ ★ ⏱️ 15 min
**Objectif :** passer d'une droite affine du plan à un plan de $\mathbb{R}^3$ qui passe par l'origine, et retour.
**Prérequis :** fiche §3 ; M07 (distance à un hyperplan) · **Parcours :** C

La droite $\Delta$ a pour équation $3x_1 - 2x_2 + 4 = 0$, soit $(\mathbf{w}, b) = ((3, -2), 4)$. Les points : $\mathbf{p} = (1, 2)$, $\mathbf{q} = (-2, 1)$, $\mathbf{r} = (0, 3)$. Comme dans la fiche, la coordonnée constante 1 se place **en tête** : $\tilde{\mathbf{x}} = (1, x_1, x_2)$ et $\tilde{\mathbf{w}} = (b, w_1, w_2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\tilde{\mathbf{w}}$ | une liste de 3 nombres |
| b | $\tilde{\mathbf{p}}$ | une liste de 3 nombres |
| c | les scores $\tilde{\mathbf{w}} \cdot \tilde{\mathbf{p}}$, $\tilde{\mathbf{w}} \cdot \tilde{\mathbf{q}}$, $\tilde{\mathbf{w}} \cdot \tilde{\mathbf{r}}$ | une liste de 3 nombres |
| d | la distance de $\mathbf{q}$ à la droite $\Delta$, dans le plan | un nombre (4 décimales) |
| e | le plan de $\mathbb{R}^3$ d'équation $\tilde{\mathbf{v}} \cdot \tilde{\mathbf{x}} = 0$, avec $\tilde{\mathbf{v}} = (-6, 2, 3)$, coupe le niveau « première coordonnée $= 1$ » selon une droite du plan : la valeur de $x_1$ où cette droite coupe l'axe des $x_1$, puis la valeur de $x_2$ où elle coupe l'axe des $x_2$ | une liste de 2 nombres |
| f | vrai ou faux : si la première coordonnée de $\tilde{\mathbf{v}}$ est nulle, la droite obtenue comme en e) passe par l'origine du plan | `True` ou `False` |
| g | le vecteur $\tilde{\mathbf{u}}$, de première coordonnée $-2$, tel que le plan $\tilde{\mathbf{u}} \cdot \tilde{\mathbf{x}} = 0$ contienne les points relevés de $(2, 0)$ et de $(0, 1)$ | une liste de 3 nombres |

Dans ta copie : de quel côté de $\Delta$ est chacun des trois points ? Montre que, pour un point $\mathbf{x}$ du plan, $\tilde{\mathbf{v}} \cdot \tilde{\mathbf{x}} = 0$ équivaut à $\mathbf{x}$ sur la droite de e).

### Ex M10.5 — Borner une norme pas à pas : ‖v_{k+1}‖² ≤ ‖v_k‖² + c ✏️ ★★ ⏱️ 15 min
**Objectif :** suivre la norme d'une suite de vecteurs construite pas à pas, la borner par récurrence, et opposer une croissance linéaire à une croissance en $\sqrt{k}$.
**Prérequis :** fiche §4 ; M07 (produit scalaire, Cauchy-Schwarz) ; R4 (récurrence) · **Parcours :** C

Une suite part de $\mathbf{v}_0 = (1, 2)$ et fait deux pas, $\mathbf{v}_{k+1} = \mathbf{v}_k + \mathbf{d}_k$, avec $\mathbf{d}_0 = (2, -1)$ et $\mathbf{d}_1 = (-1, 2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert \mathbf{v}_0 \rVert^2$ | un nombre |
| b | $\mathbf{v}_1 \cdot \mathbf{d}_1$ | un nombre |
| c | $\lVert \mathbf{v}_2 \rVert^2$ | un nombre |
| d | la borne de $\lVert \mathbf{v}_2 \rVert^2$ que donne le lemme de sommation de la fiche, sachant seulement que chaque pas vérifie $\mathbf{v}_k \cdot \mathbf{d}_k \le 0$ et $\lVert \mathbf{d}_k \rVert^2 \le 5$ | un nombre |
| e | avec les mêmes hypothèses sur **tous** les pas, la borne de $\lVert \mathbf{v}_{100} \rVert$ | un nombre (2 décimales) |
| f | une autre suite part d'un $\mathbf{v}_0$ tel que $\lVert \mathbf{v}_0 \rVert = 2$ et $\mathbf{e} \cdot \mathbf{v}_0 = -2$, pour un vecteur $\mathbf{e}$ de norme 1 ; chaque pas a une longueur au plus 3, vérifie $\mathbf{v}_k \cdot \mathbf{d}_k \le 0$ et avance d'au moins $0{,}5$ dans la direction $\mathbf{e}$ ($\mathbf{e} \cdot \mathbf{d}_k \ge 0{,}5$). Le plus grand nombre de pas $k$ que n'excluent pas les deux inégalités de la fiche (la progression le long de $\mathbf{e}$, et la borne du lemme sur $\lVert \mathbf{v}_k \rVert^2$), combinées par Cauchy-Schwarz | un entier |
| g | une troisième suite part d'un $\mathbf{v}_0$ de norme 1 et fait 10 pas de longueur 1 : les 5 premiers **dans la direction de la position** ($\mathbf{d}_k = \frac{\mathbf{v}_k}{\lVert \mathbf{v}_k \rVert}$), les 5 suivants **perpendiculaires** à la position. $\lVert \mathbf{v}_{10} \rVert$ | un nombre (2 décimales) |

Dans ta copie : vérifie que $\mathbf{v}_0 \cdot \mathbf{d}_0 = 0$ ; que vaut $\lVert \mathbf{v}_1 \rVert^2$, et pourquoi la borne est-elle atteinte au premier pas mais pas au second ? Pour f), écris les deux inégalités que vérifie $\mathbf{e} \cdot \mathbf{v}_k$, puis résous l'inégalité en $k$ (attention au signe de $\mathbf{e} \cdot \mathbf{v}_k$ avant d'élever au carré). Le plus grand nombre de pas réellement possible est-il celui de f) ? (Regarde le premier pas : que vaut $\mathbf{v}_0$, et que vaut alors $\mathbf{v}_0 \cdot \mathbf{d}_0$ ?) Pour g), pourquoi la borne de la fiche ne s'applique-t-elle pas aux cinq premiers pas ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration dans ta copie : hypothèses, étapes justifiées, conclusion. Juge-la ensuite avec la **grille de relecture** de `05_solutions.md`.

### Ex M10.6 — Un demi-espace est convexe, et une intersection de convexes aussi ∂ ★ ⏱️ 15 min
**Objectif :** démontrer les deux propriétés qui fabriquent presque tous les convexes utiles, et les appliquer à l'ensemble des séparateurs.
**Prérequis :** fiche §1 et §3 · **Parcours :** C, E

On note $s(\mathbf{x}) = \mathbf{w} \cdot \mathbf{x} + b$.
1. Montre que, pour tous $\mathbf{a}, \mathbf{b}$ et tout $t \in [0, 1]$, $s\big((1 - t)\mathbf{a} + t\mathbf{b}\big) = (1 - t)\,s(\mathbf{a}) + t\,s(\mathbf{b})$.
2. Déduis-en que le demi-espace $\{\mathbf{x} : s(\mathbf{x}) \ge 0\}$ est convexe, puis que $\{\mathbf{x} : s(\mathbf{x}) > 0\}$ l'est aussi.
3. Montre que l'intersection de deux convexes est convexe, puis, par récurrence, celle de $m$ convexes.
4. Déduis-en que le carré $\{(x, y) : |x| \le 1 \text{ et } |y| \le 1\}$ est convexe, en l'écrivant comme une intersection de quatre demi-plans.
5. Des points $\mathbf{x}_i$ et leurs labels $y_i$ étant fixés, montre que l'ensemble des couples $(\mathbf{w}, b) \in \mathbb{R}^{d+1}$ tels que $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ pour tout $i$ est convexe (dans l'espace des paramètres).
6. Montre, par un contre-exemple dessiné, que la réunion de deux demi-plans n'est pas toujours convexe.

### Ex M10.7 — Deux nuages séparés par un hyperplan ont des enveloppes convexes disjointes ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer le critère des enveloppes convexes, et s'en servir pour prouver qu'aucun hyperplan ne sépare deux nuages.
**Prérequis :** fiche §1 à §3 ; Ex M10.6 · **Parcours :** C, E

Soit $A$ et $B$ deux ensembles finis de points de $\mathbb{R}^d$, et $s(\mathbf{x}) = \mathbf{w} \cdot \mathbf{x} + b$ avec $s > 0$ sur $A$ et $s < 0$ sur $B$.
1. Montre que $s\big(\sum_i t_i\mathbf{x}_i\big) = \sum_i t_i\,s(\mathbf{x}_i)$ dès que $\sum_i t_i = 1$. Où te sers-tu de cette hypothèse ?
2. Déduis-en que $s > 0$ sur tout $\operatorname{conv}(A)$ et $s < 0$ sur tout $\operatorname{conv}(B)$ (où te sers-tu de $t_i \ge 0$ ?).
3. Conclus : $\operatorname{conv}(A) \cap \operatorname{conv}(B) = \varnothing$.
4. Énonce la contraposée. Applique-la à $A = \{(0, 0), (6, 0), (2, 6)\}$ (label $+1$) et $B = \{(2, 2), (7, 5)\}$ (label $-1$) : écris $(2, 2)$ comme une combinaison convexe des points de $A$ (trouve les poids), et conclus.
5. Montre que, si $A$ et $B$ sont séparés par un hyperplan, leurs barycentres sont strictement de part et d'autre de cet hyperplan.
6. En dimension 1, démontre directement la réciproque : si les intervalles $\operatorname{conv}(A)$ et $\operatorname{conv}(B)$ sont disjoints, donne un $(w, b)$ qui sépare $A$ et $B$.

### Ex M10.8 — La marge géométrique ne change pas quand on multiplie (w, b) par un réel positif ∂ ★ ⏱️ 15 min
**Objectif :** démontrer l'invariance de la marge géométrique, et en déduire la forme canonique d'un séparateur.
**Prérequis :** fiche §3 ; M07 (distance à un hyperplan) · **Parcours :** C

On note $\gamma(\mathbf{w}, b) = \min_i \frac{y_i(\mathbf{w} \cdot \mathbf{x}_i + b)}{\lVert \mathbf{w} \rVert}$, pour $\mathbf{w} \ne \mathbf{0}$.
1. Montre que $\gamma(c\mathbf{w}, cb) = \gamma(\mathbf{w}, b)$ pour tout $c > 0$.
2. Exprime $\gamma(-\mathbf{w}, -b)$ à l'aide d'un **maximum**. Déduis-en que, si $(\mathbf{w}, b)$ sépare les deux classes, la marge de $(-\mathbf{w}, -b)$ est strictement négative.
3. Que deviennent les marges fonctionnelles $y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ quand on multiplie $(\mathbf{w}, b)$ par $c > 0$ ? Déduis-en que tout séparateur peut être choisi avec $\min_i y_i(\mathbf{w} \cdot \mathbf{x}_i + b) = 1$.
4. Sous cette forme, montre que $\gamma(\mathbf{w}, b) = \frac{1}{\lVert \mathbf{w} \rVert}$. Déduis-en que maximiser la marge revient à minimiser $\lVert \mathbf{w} \rVert$ sous les contraintes $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$.
5. On ajoute un exemple. Montre que la marge d'un couple fixé ne peut que baisser ou rester égale, et donne une condition pour qu'elle ne change pas.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M10.9 — Pont : seuil, sigmoïde, tanh et ReLU appliqués à un même score linéaire 🔗 ★ ⏱️ 15 min
**Objectif :** calculer la sortie de quatre activations sur un même score affine, et décrire leurs lignes de niveau dans le plan.
**Prérequis :** fiche §5 ; R6 (sigmoïde, tanh) · **Parcours :** C, E

Le score est $z = \mathbf{w} \cdot \mathbf{x} + b$ avec $\mathbf{w} = (-1, 2)$ et $b = 0{,}5$. Les trois points : $\mathbf{p}_1 = (1{,}5 ;\ 0{,}5)$, $\mathbf{p}_2 = (0, 1)$, $\mathbf{p}_3 = (3 ;\ 0{,}25)$. Le seuil vaut $H(z) = 1$ si $z > 0$, et $0$ sinon.

| | Question | Réponse attendue |
|---|---|---|
| a | les trois scores | une liste de 3 nombres |
| b | les trois sorties du seuil $H$ | une liste de 3 nombres |
| c | les trois sorties de la sigmoïde $\sigma$ | une liste de 3 nombres (4 décimales) |
| d | les trois sorties de $\tanh$ | une liste de 3 nombres (4 décimales) |
| e | les trois sorties de ReLU | une liste de 3 nombres |
| f | la valeur du score $z$ pour laquelle $\sigma(z) = 0{,}8$ | un nombre (4 décimales) |
| g | la distance entre la droite où $\sigma(\mathbf{w} \cdot \mathbf{x} + b) = 0{,}8$ et la frontière $\mathbf{w} \cdot \mathbf{x} + b = 0$ | un nombre (4 décimales) |

Dans ta copie : pourquoi la ligne de niveau de g) est-elle une droite parallèle à la frontière ? Que vaut chaque activation en $\mathbf{p}_1$, et quelle convention changerait la réponse du seuil ? Pour quelles activations la région « sortie $> \frac{1}{2}$ » est-elle le demi-plan $z > 0$ ?

### Ex M10.10 — MML §12.1 : les hyperplans séparateurs, en anglais 📖 ★★ ⏱️ 20 min
**Objectif :** lire en anglais la mise en place d'un classifieur linéaire, et relier ses notations à celles de la fiche.
**Prérequis :** fiche §3 · **Parcours :** C

Lis l'introduction du chapitre 12 de MML, puis le §12.1. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Dans l'introduction, quel genre de problème le chapitre étudie-t-il, et quelles valeurs prennent les labels ? Pourquoi ce choix de labels est-il commode (pense au produit $y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ de la fiche) ?
2. Comment le livre écrit-il la fonction qui sert à classer ? Récris-la avec les notations de la fiche.
3. Comment le livre montre-t-il que $\mathbf{w}$ est orthogonal à l'hyperplan ? Refais l'argument avec tes propres nombres : prends la droite $5x_1 - 2x_2 + 1 = 0$, deux de ses points, et vérifie.
4. Quelle condition le livre impose-t-il aux exemples d'entraînement ? L'inégalité est-elle large ou stricte ? Compare avec la séparation stricte de la fiche (§3) : que change ce choix pour un point posé exactement sur l'hyperplan ?
5. Le livre illustre l'hyperplan par une figure : que montre-t-elle, et que fait-elle voir de la position de $\mathbf{w}$ ?
6. Note trois mots ou tournures en anglais de ces pages, avec leur traduction.

### Ex M10.11 — Expliquer la convexité et l'enveloppe convexe avec un élastique 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, sans formule, ce qu'est un ensemble convexe, ce qu'est l'enveloppe convexe d'un nuage, et pourquoi elle dit si deux nuages sont séparables.
**Prérequis :** fiche §1 à §3 · **Parcours :** C, E

Un ami qui n'a jamais fait de géométrie te demande ce que veut dire « convexe ». Explique-lui, **en huit lignes au plus**, sans formule et avec des objets du quotidien : ce qu'est un ensemble convexe (et un exemple qui ne l'est pas), ce que fait un élastique lâché autour de clous plantés dans une planche, quels clous il touche, et pourquoi deux élastiques qui se croisent disent qu'aucune règle droite posée sur la planche ne peut séparer les deux familles de clous.

<a id="entretien"></a>

## 💼 Entretien

### M10.E1 — « Que veut dire « linéairement séparable », et comment le vérifier ? » 💼 ★ ⏱️ 10 min
*Fiche §3 · parcours C*

« Que veut dire « linéairement séparable », et comment le vérifier ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit donner la définition et son sens géométrique, le critère des enveloppes convexes, une façon de le **vérifier** en pratique (et ce qu'il faut exiger pour que le test ait un sens), ce qui se passe quand la dimension est grande devant le nombre d'exemples, et une mise en garde : ce que la séparabilité des données d'entraînement ne garantit pas. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m10_separabilite_convexite/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M10.12 | L'enveloppe convexe dans le plan : la chaîne monotone d'Andrew · `convex_hull_2d` | 🔨 | ★★ | 25 | C, E |
| M10.13 | Séparabilité par programmation linéaire, et marge géométrique · `is_linearly_separable, margin_of_separator` | 🔨 | ★★ | 25 | C, E |
| M10.14 | Prédire : n points aux labels tirés au hasard en dimension d sont-ils séparables ? | 🔮 | ★ | 10 | C, E |
| M10.15 | Deux nuages, leurs enveloppes convexes et un hyperplan séparateur avec sa marge | 🎨 | ★ | 15 | C |
| M10.16 | Chasse à l'erreur : un produit vectoriel de signe inversé, une marge non normalisée | 🐛 | ★ | 10 | C |
| M10.17 | Des tests de propriétés pour l'enveloppe convexe | 🛠️ | ★ | 15 | C |
| M10.18 | Défi : la plus grande marge possible entre deux nuages donnés, à 1 % près | 🏆 | ★★★ | 20 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
