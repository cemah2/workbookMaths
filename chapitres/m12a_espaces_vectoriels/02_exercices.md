# M12a · Espaces vectoriels et applications linéaires — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m12a_espaces_vectoriels/06_mes_reponses.md` (créée par `python tools/start_chapter.py M12a`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🧮, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, une famille de vecteurs se range dans les **colonnes** d'une matrice, et les colonnes se numérotent à partir de 1 (comme dans la fiche et dans MML) ; $\mathbf{e}_1, \mathbf{e}_2, \ldots$ est la base canonique.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M12a.Q1 — Sous-espace ou pas ? 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

Lesquels sont des sous-espaces vectoriels ? Réponds par oui ou non, et justifie chaque non par un contre-exemple.
1. $\{(x, y) : y = 3x\}$ dans $\mathbb{R}^2$.
2. $\{(x, y) : y = 3x + 1\}$ dans $\mathbb{R}^2$.
3. $\{(x, y, z) : x + y + z = 0 \text{ et } z = 2y\}$ dans $\mathbb{R}^3$.
4. $\{(x, y) : x \ge 0\}$ dans $\mathbb{R}^2$.
5. $\{(x, y) : xy = 0\}$ dans $\mathbb{R}^2$.
6. Les polynômes de degré **exactement** 2.

### M12a.Q2 — Combinaison linéaire et famille génératrice 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. $(-6, 4)$ est-il une combinaison linéaire de $(3, -2)$ seul ?
2. $(1, 2)$ et $(2, 4)$ engendrent-ils $\mathbb{R}^2$ ?
3. Combien de vecteurs faut-il, au minimum, pour engendrer $\mathbb{R}^4$ ?
4. Quel ensemble de $\mathbb{R}^3$ est $\operatorname{Vect}\big((1, 0, 0), (0, 1, 0)\big)$ ?
5. Vrai ou faux : le vecteur nul est une combinaison linéaire de n'importe quelle famille.
6. Vrai ou faux : si $\mathbf{u}$ et $\mathbf{v}$ engendrent un plan, $\mathbf{u} + \mathbf{v}$ et $\mathbf{u} - \mathbf{v}$ engendrent le même plan.

### M12a.Q3 — Libre ou liée ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

1. $(1, 2)$ et $(3, 6)$.
2. $(1, 0, 0)$, $(1, 1, 0)$, $(1, 1, 1)$.
3. Quatre vecteurs quelconques de $\mathbb{R}^3$.
4. Une famille qui contient le vecteur nul.
5. Le vecteur $(2, -1, 3)$ seul.
6. Vrai ou faux : si $(\mathbf{u}, \mathbf{v}, \mathbf{w})$ est libre, alors $(\mathbf{u}, \mathbf{v})$ est libre.

### M12a.Q4 — Base et dimension : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Trois vecteurs libres de $\mathbb{R}^3$ forment une base de $\mathbb{R}^3$.
2. L'espace des polynômes de degré au plus 4 est de dimension 4.
3. Une base d'un plan de $\mathbb{R}^3$ a trois vecteurs.
4. Les coordonnées d'un vecteur dans une base sont uniques.
5. $\mathbb{R}^3$ n'a qu'une seule base.
6. L'espace des matrices de forme $(2, 3)$ est de dimension 6.

### M12a.Q5 — Le rang d'une matrice, d'une transposée, d'un produit 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. Le plus grand rang possible pour une matrice de forme $(4, 7)$ ?
2. $\operatorname{rg}(\mathbf{A}) = 3$ : que vaut $\operatorname{rg}(\mathbf{A}^\top)$ ?
3. $\mathbf{A}$ et $\mathbf{B}$ de forme $(5, 5)$, de rangs 2 et 4 : le plus grand rang possible pour $\mathbf{A}\mathbf{B}$ ?
4. Le rang de $\mathbf{u}\mathbf{v}^\top$, pour $\mathbf{u} \in \mathbb{R}^4$ et $\mathbf{v} \in \mathbb{R}^6$ non nuls ?
5. $\mathbf{A}$ de forme $(3, 3)$ inversible, $\mathbf{B}$ de forme $(3, 5)$ de rang 2 : $\operatorname{rg}(\mathbf{A}\mathbf{B})$ ?
6. Un tableau de 6 exemples et 10 features, centré : son rang au plus ?

### M12a.Q6 — Linéaire, affine, ou ni l'un ni l'autre ? 🧠 ★ ⏱️ 4 min
*Fiche §5 et §8 · parcours C, E*

1. $f(x, y) = (3x - y, 2y)$.
2. $g(x, y) = (x + 1, y)$.
3. $h(x) = x^2$.
4. $P \mapsto P'$ sur les polynômes.
5. $\mathbf{x} \mapsto \lVert \mathbf{x} \rVert$ sur $\mathbb{R}^2$.
6. $z \mapsto 4z - 7$ sur $\mathbb{R}$.

### M12a.Q7 — Noyau et image : qui vit où ? 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

$\mathbf{A}$ a la forme $(3, 5)$.
1. $\ker\mathbf{A}$ est un sous-espace de quel $\mathbb{R}^k$ ?
2. Et $\operatorname{Im}\mathbf{A}$ ?
3. La plus petite dimension possible de $\ker\mathbf{A}$ ?
4. $\mathbf{A}$ peut-elle être injective ?
5. Si $\operatorname{rg}(\mathbf{A}) = 3$, que vaut $\operatorname{Im}\mathbf{A}$ ?
6. Si $\mathbf{x}_p$ est une solution de $\mathbf{A}\mathbf{x} = \mathbf{b}$, quelles sont toutes les solutions ?

### M12a.Q8 — Changer de base : ce qui change et ce qui reste 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C*

Les colonnes de la matrice inversible $\mathbf{S}$ forment une base $(\mathbf{s}_1, \ldots, \mathbf{s}_n)$ de $\mathbb{R}^n$.
1. Les coordonnées de $\mathbf{x}$ dans cette base ?
2. La matrice de $\mathbf{x} \mapsto \mathbf{A}\mathbf{x}$ dans cette base ?
3. Le rang de cette nouvelle matrice, comparé à celui de $\mathbf{A}$ ?
4. Vrai ou faux : $\mathbf{S}^{-1}\mathbf{A}\mathbf{S} = \mathbf{A}$ pour toute $\mathbf{S}$.
5. Que vaut $\mathbf{S}^{-1}\mathbf{I}\mathbf{S}$ ?
6. Si $\mathbf{A}\mathbf{s}_1 = 5\,\mathbf{s}_1$, quelle est la première colonne de $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ ?

<a id="rappels"></a>

## 🔁 Rappels

### M12a.R1 — Le pivot de Gauss et la forme échelonnée réduite (M09a) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

$\mathbf{M} = \begin{pmatrix} 2 & 4 & 2 \\ 1 & 3 & 2 \\ 1 & 1 & 0 \end{pmatrix}$.
1. La forme échelonnée réduite de $\mathbf{M}$ ?
2. Les colonnes qui portent un pivot ?
3. Le rang de $\mathbf{M}$ ?
4. Les variables libres du système $\mathbf{M}\mathbf{x} = \mathbf{0}$ ?
5. Toutes les solutions de $\mathbf{M}\mathbf{x} = \mathbf{0}$ ?
6. Les trois opérations élémentaires permises sur les lignes ?

### M12a.R2 — Produit matriciel et formes (M09a) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 1 & 0 & -2 \\ 3 & 1 & 1 \end{pmatrix}$ et $\mathbf{B} = \begin{pmatrix} 2 & 1 \\ 0 & -1 \\ 1 & 0 \end{pmatrix}$.
1. La forme de $\mathbf{A}\mathbf{B}$ ?
2. $\mathbf{A}\mathbf{B}$ ?
3. La forme de $\mathbf{B}\mathbf{A}$ ?
4. $\mathbf{A}\mathbf{e}_2$, avec $\mathbf{e}_2 = (0, 1, 0)$ ?
5. $(\mathbf{A}\mathbf{B})^\top$ s'écrit avec $\mathbf{A}^\top$ et $\mathbf{B}^\top$ : comment ?

### M12a.R3 — Combinaisons linéaires et produit scalaire dans ℝⁿ (M07) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C*

$\mathbf{u} = (1, -2, 2)$ et $\mathbf{v} = (3, 0, -1)$.
1. $2\mathbf{u} - \mathbf{v}$ ?
2. $\mathbf{u} \cdot \mathbf{v}$ ?
3. $\lVert \mathbf{u} \rVert$ ?
4. $\mathbf{u} + \mathbf{v}$ et $\mathbf{u} - \mathbf{v}$ sont-ils orthogonaux ?
5. Les nombres $\alpha$ et $\beta$ tels que $(5, -4, 3) = \alpha\mathbf{u} + \beta\mathbf{v}$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets pour un vecteur, des numéros de colonnes ou une forme, comme `[0, -2, 5]` ; une matrice comme une liste de lignes, `[[1, 0], [-2, 3]]` ; vrai ou faux par `True` ou `False`.

### Ex M12a.1 — Reconnaître des sous-espaces de ℝ³ et de l'espace des polynômes ✏️ ★ ⏱️ 15 min
**Objectif :** décider si une partie est un sous-espace, en vérifiant les trois conditions ou en trouvant un contre-exemple.
**Prérequis :** fiche §1 ; R4 (contre-exemple) · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $U_1 = \{(x, y, z) : 2x - y + 4z = 0\}$ est un sous-espace de $\mathbb{R}^3$ | `True` ou `False` |
| b | $U_2 = \{(x, y, z) : x - y = 1\}$ est un sous-espace de $\mathbb{R}^3$ | `True` ou `False` |
| c | $U_3 = \{(2t, -t, 3t) : t \in \mathbb{R}\}$ est un sous-espace de $\mathbb{R}^3$ | `True` ou `False` |
| d | $U_4 = \{(x, y, z) : x^2 + y^2 = z^2\}$ est un sous-espace de $\mathbb{R}^3$ | `True` ou `False` |
| e | $U_5 = \{(x, y, z) : x \le y\}$ est un sous-espace de $\mathbb{R}^3$ | `True` ou `False` |
| f | $\{P \in \mathbb{R}_3[x] : P(1) = 0\}$ est un sous-espace de $\mathbb{R}_3[x]$ | `True` ou `False` |
| g | $\{P \in \mathbb{R}_3[x] : P(0) = 1\}$ est un sous-espace de $\mathbb{R}_3[x]$ | `True` ou `False` |
| h | le vecteur de $U_3$ dont la première coordonnée vaut 4 | une liste de 3 nombres |

Dans ta copie : pour chaque réponse `True`, vérifie les trois conditions ; pour chaque `False`, donne un contre-exemple précis (deux vecteurs dont la somme sort, ou un vecteur et un nombre). Pour d), pourquoi la multiplication ne pose-t-elle pas de problème, et l'addition si ?

### Ex M12a.2 — Écrire un vecteur comme combinaison linéaire : un système à résoudre ✏️ ★ ⏱️ 15 min
**Objectif :** traduire « être une combinaison linéaire » en système, le résoudre, et décrire un plan engendré par une équation.
**Prérequis :** fiche §2 ; M07 §5 (hyperplans) · **Parcours :** C, E

$\mathbf{u}_1 = (1, -1, 2)$, $\mathbf{u}_2 = (3, 0, 1)$ et $\mathbf{b} = (-1, -2, 3)$.

| | Question | Réponse attendue |
|---|---|---|
| a | les nombres $(\lambda_1, \lambda_2)$ tels que $\mathbf{b} = \lambda_1\mathbf{u}_1 + \lambda_2\mathbf{u}_2$ | une liste de 2 nombres |
| b | vrai ou faux : $(1, 1, 1) \in \operatorname{Vect}(\mathbf{u}_1, \mathbf{u}_2)$ | `True` ou `False` |
| c | le nombre $k$ tel que $(5, k, 0) \in \operatorname{Vect}(\mathbf{u}_1, \mathbf{u}_2)$ | un nombre |
| d | le vecteur $\mathbf{n} = (a, b, 3)$ orthogonal à $\mathbf{u}_1$ et à $\mathbf{u}_2$ | une liste de 3 nombres |
| e | vrai ou faux : $\operatorname{Vect}(\mathbf{u}_1, \mathbf{u}_2) = \operatorname{Vect}(\mathbf{u}_1, \mathbf{b})$ | `True` ou `False` |
| f | le nombre minimal de vecteurs à ajouter à $(\mathbf{u}_1, \mathbf{u}_2)$ pour engendrer $\mathbb{R}^3$ | un entier |

Dans ta copie : écris le plan $\operatorname{Vect}(\mathbf{u}_1, \mathbf{u}_2)$ sous la forme d'une équation $ax + by + cz = 0$ avec d), et retrouve b) et c) avec cette équation. Pourquoi, en a), y a-t-il trois équations pour deux inconnues, et que signifie le fait que la troisième soit vérifiée ?

### Ex M12a.3 — L'indépendance de trois vecteurs de ℝ³ par le pivot de Gauss ✏️ ★ ⏱️ 15 min
**Objectif :** tester l'indépendance par le rang, et lire la relation de dépendance dans la forme réduite.
**Prérequis :** fiche §2 ; M09a §6 (pivot de Gauss) · **Parcours :** C, E

$\mathbf{v}_1 = (1, 2, -1)$, $\mathbf{v}_2 = (0, 1, 3)$ et $\mathbf{v}_3 = (2, 3, -5)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le rang de la matrice $[\mathbf{v}_1 \ \mathbf{v}_2 \ \mathbf{v}_3]$ | un entier |
| b | vrai ou faux : la famille $(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3)$ est libre | `True` ou `False` |
| c | les nombres $(a, b)$ tels que $\mathbf{v}_3 = a\,\mathbf{v}_1 + b\,\mathbf{v}_2$ | une liste de 2 nombres |
| d | le vecteur $(x_1, x_2, x_3)$ tel que $x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + x_3\mathbf{v}_3 = \mathbf{0}$ et $x_3 = 1$ | une liste de 3 nombres |
| e | le nombre $k$ pour lequel la famille $(\mathbf{v}_1, \mathbf{v}_2, (1, 0, k))$ est liée | un nombre |
| f | vrai ou faux : la famille $(\mathbf{v}_1, \mathbf{v}_2, (2, 3, -4))$ est libre | `True` ou `False` |

Dans ta copie : les trois vecteurs $\mathbf{v}_1$, $\mathbf{v}_2$, $\mathbf{v}_3$ sont deux à deux non colinéaires ; pourquoi la famille est-elle quand même liée ? Que veut dire, géométriquement, « trois vecteurs liés de $\mathbb{R}^3$ » ?

### Ex M12a.4 — Extraire une base d'une famille génératrice, compléter une famille libre ✏️ ★★ ⏱️ 20 min
**Objectif :** extraire une base par les colonnes à pivot, et compléter une famille libre avec la base canonique.
**Prérequis :** fiche §3 · **Parcours :** C, E

$\mathbf{a}_1 = (1, 0, 2)$, $\mathbf{a}_2 = (2, 0, 4)$, $\mathbf{a}_3 = (0, 1, 1)$, $\mathbf{a}_4 = (1, 1, 3)$, $\mathbf{a}_5 = (1, -1, 0)$ ; puis $\mathbf{u} = (1, 2, -2)$ et $\mathbf{v} = (0, 1, -1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le rang de la matrice $[\mathbf{a}_1 \ \cdots \ \mathbf{a}_5]$ | un entier |
| b | les numéros (à partir de 1) de ses colonnes à pivot | une liste d'entiers |
| c | les nombres $(x, y)$ tels que $\mathbf{a}_4 = x\,\mathbf{a}_1 + y\,\mathbf{a}_3$ | une liste de 2 nombres |
| d | $\dim\operatorname{Vect}(\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3, \mathbf{a}_4)$ | un entier |
| e | le plus petit $j$ tel que $(\mathbf{u}, \mathbf{v}, \mathbf{e}_j)$ soit une base de $\mathbb{R}^3$ | un entier |
| f | les nombres $(\alpha, \beta)$ tels que $\mathbf{e}_1 = \alpha\,\mathbf{u} + \beta\,\mathbf{v}$ | une liste de 2 nombres |

Dans ta copie : pourquoi les colonnes à pivot trouvées en b) forment-elles une base de $\mathbb{R}^3$, sans qu'il faille vérifier qu'elles engendrent ? Pourquoi $\mathbf{e}_1$ ne peut-il pas compléter $(\mathbf{u}, \mathbf{v})$ ?

### Ex M12a.5 — Les coordonnées d'un vecteur dans une base qui n'est pas la base canonique ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des coordonnées dans une base de $\mathbb{R}^3$ et dans une base d'un plan, et passer des coordonnées au vecteur.
**Prérequis :** fiche §3 · **Parcours :** C, E

$\mathbf{b}_1 = (1, 0, 1)$, $\mathbf{b}_2 = (1, 1, 0)$, $\mathbf{b}_3 = (0, 1, 1)$ ; et, dans le plan $P = \operatorname{Vect}(\mathbf{p}_1, \mathbf{p}_2)$, $\mathbf{p}_1 = (1, 2, 0)$ et $\mathbf{p}_2 = (0, 1, -1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | les coordonnées de $\mathbf{v} = (1, 4, -1)$ dans la base $(\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3)$ | une liste de 3 nombres |
| b | le vecteur qui a pour coordonnées $(2, -1, 1)$ dans cette base | une liste de 3 nombres |
| c | les coordonnées de $\mathbf{e}_1$ dans cette base | une liste de 3 nombres (1 décimale) |
| d | les coordonnées de $\mathbf{w} = (2, 7, -3)$ dans la base $(\mathbf{p}_1, \mathbf{p}_2)$ de $P$ | une liste de 2 nombres |
| e | vrai ou faux : $(3, 1, 0) \in P$ | `True` ou `False` |
| f | les coordonnées de $\mathbf{v}$ dans la base $(\mathbf{b}_3, \mathbf{b}_1, \mathbf{b}_2)$ | une liste de 3 nombres |

Dans ta copie : vérifie que $(\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3)$ est une base, puis vérifie a) en recalculant la combinaison. Quelle matrice a pour colonnes les coordonnées de $\mathbf{e}_1$, $\mathbf{e}_2$, $\mathbf{e}_3$ dans cette base ?

### Ex M12a.6 — Le rang par les colonnes et par les lignes, celui d'un produit, et celui d'un tableau centré ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des rangs, comparer celui d'un produit à la borne du cours, et voir le rang perdu en centrant.
**Prérequis :** fiche §4 ; M02c (centrer) · **Parcours :** C, E

$$\mathbf{A} = \begin{pmatrix} 1 & 2 & 0 & -1 \\ 2 & 4 & 1 & 1 \\ 3 & 6 & 1 & 0 \end{pmatrix}, \qquad \mathbf{C} = \begin{pmatrix} -2 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 1 & 0 \end{pmatrix}, \qquad \mathbf{X} = \begin{pmatrix} 2 & 1 & 5 \\ 4 & 0 & 3 \\ 3 & 2 & 1 \end{pmatrix}$$

($\mathbf{X}$ : 3 exemples, 3 features ; $\mathbf{X}_c$ est $\mathbf{X}$ centré colonne par colonne).

| | Question | Réponse attendue |
|---|---|---|
| a | $\operatorname{rg}(\mathbf{A})$ | un entier |
| b | $\operatorname{rg}(\mathbf{A}^\top)$ | un entier |
| c | $\operatorname{rg}(\mathbf{A}^\top\mathbf{A})$ | un entier |
| d | $\operatorname{rg}(\mathbf{C})$ | un entier |
| e | $\operatorname{rg}(\mathbf{A}\mathbf{C})$ | un entier |
| f | $\operatorname{rg}(\mathbf{X})$ | un entier |
| g | $\operatorname{rg}(\mathbf{X}_c)$ | un entier |

Dans ta copie : quelle relation lie les lignes de $\mathbf{A}$ ? Calcule $\mathbf{A}$ fois chacune des deux premières colonnes de $\mathbf{C}$ : qu'en conclus-tu pour e), comparé à la borne $\min(\operatorname{rg}\mathbf{A}, \operatorname{rg}\mathbf{C})$ ? Pour un tableau centré de $n$ exemples et de $p$ features, quelle combinaison de ses lignes vaut $\mathbf{0}$, et que dit-elle de son rang ?

### Ex M12a.7 — La matrice d'une application linéaire : les images des vecteurs de base ✏️ ★ ⏱️ 15 min
**Objectif :** écrire la matrice d'une application linéaire, colonne par colonne, et s'en servir.
**Prérequis :** fiche §5 ; M07 §4 (projection sur un vecteur) · **Parcours :** C, E

$f : \mathbb{R}^3 \to \mathbb{R}^2$ est définie par $f(x, y, z) = (x - 2y + z,\ 3x + z)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice de $f$ | une matrice |
| b | $f(\mathbf{e}_2)$ | une liste de 2 nombres |
| c | $f(2, 1, -1)$ | une liste de 2 nombres |
| d | la forme de la matrice d'une application linéaire de $\mathbb{R}^5$ dans $\mathbb{R}^2$ | une liste de 2 entiers |
| e | la matrice de l'application linéaire $g$ du plan telle que $g(1, 1) = (3, 1)$ et $g(1, -1) = (1, -3)$ | une matrice |
| f | la matrice de la projection orthogonale du plan sur la droite $y = x$ | une matrice (1 décimale) |
| g | vrai ou faux : $h(x, y) = (x + y, 1)$ est linéaire | `True` ou `False` |

Dans ta copie : pour e), écris $\mathbf{e}_1$ et $\mathbf{e}_2$ comme combinaisons de $(1, 1)$ et $(1, -1)$ avant de calculer. Pour f), que valent l'image de $(1, 1)$ et celle de $(1, -1)$ ?

### Ex M12a.8 — Composer deux applications du plan, c'est multiplier leurs matrices ✏️ ★ ⏱️ 15 min
**Objectif :** écrire la matrice d'une composée dans le bon ordre, et celle d'une réciproque.
**Prérequis :** fiche §5 ; M09a §7 (inverse) · **Parcours :** C

$a(x, y) = (3x,\ y)$ étire le plan horizontalement ; $b(x, y) = (x + 2y,\ y)$ le cisaille.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice de $b \circ a$ (d'abord $a$, puis $b$) | une matrice |
| b | la matrice de $a \circ b$ | une matrice |
| c | $(b \circ a)(1, 1)$ | une liste de 2 nombres |
| d | vrai ou faux : $a \circ b = b \circ a$ | `True` ou `False` |
| e | la matrice de $b \circ b$ | une matrice |
| f | la matrice de la réciproque $b^{-1}$ | une matrice |
| g | la matrice de $(a \circ b)^{-1}$ | une matrice (4 décimales) |

Dans ta copie : vérifie c) en appliquant $a$ puis $b$ au point $(1, 1)$. Pourquoi la matrice de « $a$ puis $b$ » est-elle $\mathbf{B}\mathbf{A}$ et non $\mathbf{A}\mathbf{B}$ ? Décris $b^{-1}$ en mots.

### Ex M12a.9 — Noyau et image d'une matrice 3 × 4, et le théorème du rang ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer une base du noyau et une base de l'image, et vérifier le théorème du rang.
**Prérequis :** fiche §6 ; M07 §5 (équation d'un plan) · **Parcours :** C, E

$$\mathbf{A} = \begin{pmatrix} 1 & 1 & 1 & 3 \\ 2 & 1 & 0 & 5 \\ 1 & -1 & -3 & 1 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | $\operatorname{rg}(\mathbf{A})$ | un entier |
| b | les numéros (à partir de 1) des colonnes à pivot | une liste d'entiers |
| c | $\dim\ker\mathbf{A}$ | un entier |
| d | le vecteur de base du noyau tel que $x_3 = 1$ et $x_4 = 0$ | une liste de 4 nombres |
| e | le vecteur de base du noyau tel que $x_3 = 0$ et $x_4 = 1$ | une liste de 4 nombres |
| f | une base de $\operatorname{Im}\mathbf{A}$ : la matrice formée des colonnes à pivot de $\mathbf{A}$ | une matrice |
| g | le vecteur $\mathbf{n} = (a, b, 1)$ orthogonal à $\operatorname{Im}\mathbf{A}$ | une liste de 3 nombres |
| h | vrai ou faux : $(2, 1, -4) \in \operatorname{Im}\mathbf{A}$ | `True` ou `False` |

Dans ta copie : vérifie $\mathbf{A}\mathbf{x} = \mathbf{0}$ pour d) et e), et lis chacun comme une relation entre les colonnes de $\mathbf{A}$. Vérifie le théorème du rang. $\mathbf{A}$ est-elle injective ? surjective ?

### Ex M12a.10 — Toutes les solutions de A x = b : une solution particulière plus le noyau ✏️ ★★ ⏱️ 20 min
**Objectif :** décrire toutes les solutions d'un système comme une solution particulière plus le noyau, et dire quand il y en a.
**Prérequis :** fiche §6 ; M09a §6 · **Parcours :** C, E

$$\mathbf{A} = \begin{pmatrix} 1 & 0 & 2 & -1 \\ 0 & 1 & -1 & 3 \\ 1 & 1 & 1 & 2 \end{pmatrix}, \qquad \mathbf{b} = (4, -1, 3).$$

| | Question | Réponse attendue |
|---|---|---|
| a | la solution de $\mathbf{A}\mathbf{x} = \mathbf{b}$ telle que $x_3 = x_4 = 0$ | une liste de 4 nombres |
| b | $\dim\ker\mathbf{A}$ | un entier |
| c | le vecteur de base du noyau tel que $x_3 = 1$ et $x_4 = 0$ | une liste de 4 nombres |
| d | le vecteur de base du noyau tel que $x_3 = 0$ et $x_4 = 1$ | une liste de 4 nombres |
| e | la solution de $\mathbf{A}\mathbf{x} = \mathbf{b}$ telle que $x_3 = 2$ et $x_4 = -1$ | une liste de 4 nombres |
| f | vrai ou faux : $(2, 0, 1, 0)$ est une solution de $\mathbf{A}\mathbf{x} = \mathbf{b}$ | `True` ou `False` |
| g | le nombre $c$ pour lequel $\mathbf{A}\mathbf{x} = (4, -1, c)$ a des solutions | un nombre |
| h | le nombre de solutions de $\mathbf{A}\mathbf{x} = (4, -1, 5)$ | un entier |

Dans ta copie : écris l'ensemble des solutions sous la forme $\mathbf{x}_p + s\,\mathbf{k}_1 + t\,\mathbf{k}_2$. Pourquoi f) est-elle une solution, alors que ce n'est pas celle de a) ? Quelle relation entre les lignes de $\mathbf{A}$ explique g) ?

### Ex M12a.11 — Une base adaptée qui rend diagonale la matrice d'une application : S⁻¹AS ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer la matrice d'une application dans une nouvelle base, et s'en servir pour calculer une image.
**Prérequis :** fiche §7 ; M09a §7 (inverse $2 \times 2$) · **Parcours :** C, E

$\mathbf{A} = \begin{pmatrix} 4 & -2 \\ 1 & 1 \end{pmatrix}$ ; la nouvelle base est $\mathbf{s}_1 = (1, 1)$, $\mathbf{s}_2 = (2, 1)$, et $\mathbf{S} = [\mathbf{s}_1 \ \mathbf{s}_2]$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{A}\mathbf{s}_1$ | une liste de 2 nombres |
| b | $\mathbf{A}\mathbf{s}_2$ | une liste de 2 nombres |
| c | $\mathbf{S}^{-1}$ | une matrice |
| d | $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ | une matrice |
| e | les coordonnées de $\mathbf{x} = (5, 3)$ dans la base $(\mathbf{s}_1, \mathbf{s}_2)$ | une liste de 2 nombres |
| f | les coordonnées de $\mathbf{A}\mathbf{x}$ dans la base $(\mathbf{s}_1, \mathbf{s}_2)$, calculées avec d) et e) | une liste de 2 nombres |
| g | $\mathbf{A}\mathbf{x}$ dans la base canonique, calculé à partir de f) | une liste de 2 nombres |
| h | la matrice de $\mathbf{x} \mapsto \mathbf{A}\mathbf{x}$ dans la base $(\mathbf{s}_2, \mathbf{s}_1)$ | une matrice |

Dans ta copie : que remarques-tu en a) et b), et comment cela se voit-il dans d) ? Vérifie g) en calculant $\mathbf{A}\mathbf{x}$ directement. Comment calculerais-tu facilement $\mathbf{A}$ appliquée dix fois à $\mathbf{x}$ ?

### Ex M12a.12 — Une application affine du plan : partie linéaire, translation, inverse ✏️ ★★ ⏱️ 20 min
**Objectif :** décomposer une application affine, calculer sa réciproque, et vérifier qu'elle conserve les milieux.
**Prérequis :** fiche §8 ; M09a §7 · **Parcours :** C, E

$\varphi(x, y) = (2x + 3y - 1,\ x + 2y + 4)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la partie linéaire $\mathbf{A}$ de $\varphi$ | une matrice |
| b | le vecteur de translation de $\varphi$ | une liste de 2 nombres |
| c | $\varphi(1, -1)$ | une liste de 2 nombres |
| d | $\mathbf{A}^{-1}$ | une matrice |
| e | le vecteur de translation de $\varphi^{-1}$ | une liste de 2 nombres |
| f | $\varphi^{-1}(3, 4)$ | une liste de 2 nombres |
| g | $\varphi(1, 1)$ | une liste de 2 nombres |
| h | vrai ou faux : $\varphi$ est linéaire | `True` ou `False` |

Dans ta copie : vérifie f) en calculant son image par $\varphi$. Calcule $\varphi(0, 0)$ et $\varphi(2, 2)$, puis leur milieu, et compare avec g) : quelle propriété du cours retrouves-tu ?

### Ex M12a.13 — La dérivation sur les polynômes de degré au plus 3 : matrice, noyau, image ✏️ ★★ ⏱️ 20 min
**Objectif :** écrire la matrice d'une application linéaire sur un espace de polynômes, et lire son noyau et son image.
**Prérequis :** fiche §3, §5 et §6 ; R7 (dérivée d'un polynôme) · **Parcours :** C

$D : \mathbb{R}_3[x] \to \mathbb{R}_3[x]$, $D(P) = P'$, dans la base $(1, x, x^2, x^3)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice de $D$ | une matrice |
| b | les coordonnées de $P = 2 - x + 4x^2 + x^3$ | une liste de 4 nombres |
| c | les coordonnées de $P'$, calculées avec a) et b) | une liste de 4 nombres |
| d | $\operatorname{rg}(D)$ | un entier |
| e | $\dim\ker D$ | un entier |
| f | vrai ou faux : $x^3 \in \operatorname{Im} D$ | `True` ou `False` |
| g | la matrice de $D \circ D$ | une matrice |
| h | le plus petit entier $k \ge 1$ tel que $D^k$ soit l'application nulle | un entier |

Dans ta copie : décris $\ker D$ et $\operatorname{Im} D$ avec des mots. Vérifie le théorème du rang. Pourquoi $D$ n'est-elle pas inversible, alors que « dériver » se défait par « prendre une primitive » ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration dans ta copie : hypothèses, étapes justifiées, conclusion. Juge-la ensuite avec la **grille de relecture** de `05_solutions.md`.

### Ex M12a.14 — L'intersection de deux sous-espaces en est un ; la réunion, presque jamais ∂ ★ ⏱️ 15 min
**Objectif :** démontrer que l'intersection de deux sous-espaces est un sous-espace, et caractériser les réunions qui en sont.
**Prérequis :** fiche §1 ; R4 (ensembles, raisonnement par l'absurde) · **Parcours :** C, E

$U$ et $W$ sont deux sous-espaces d'un espace vectoriel $V$.
1. Montre que $U \cap W$ est un sous-espace de $V$.
2. Dans $\mathbb{R}^3$, décris l'intersection des plans $x + y + z = 0$ et $x - z = 0$ : donne un vecteur qui l'engendre.
3. Montre que, si $U \subseteq W$ ou $W \subseteq U$, alors $U \cup W$ est un sous-espace.
4. On suppose qu'aucun des deux n'est inclus dans l'autre : il existe $\mathbf{u} \in U$ avec $\mathbf{u} \notin W$, et $\mathbf{w} \in W$ avec $\mathbf{w} \notin U$. Montre que $\mathbf{u} + \mathbf{w} \notin U \cup W$ (raisonne par l'absurde). Conclus.
5. Applique à la réunion des deux axes de $\mathbb{R}^2$.

### Ex M12a.15 — Les coordonnées dans une base sont uniques ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer que l'indépendance donne l'unicité des coordonnées, et réciproquement, et que les coordonnées dépendent linéairement du vecteur.
**Prérequis :** fiche §2 et §3 · **Parcours :** C

$(\mathbf{b}_1, \ldots, \mathbf{b}_n)$ est une famille de vecteurs de $V$.
1. On suppose la famille libre, et $\mathbf{v} = \sum_i c_i\mathbf{b}_i = \sum_i d_i\mathbf{b}_i$. Montre que $c_i = d_i$ pour tout $i$.
2. Réciproquement, on suppose que tout vecteur de $\operatorname{Vect}(\mathbf{b}_1, \ldots, \mathbf{b}_n)$ s'écrit d'une seule façon comme combinaison des $\mathbf{b}_i$. Montre que la famille est libre (pense au vecteur $\mathbf{0}$).
3. On suppose maintenant que $(\mathbf{b}_1, \ldots, \mathbf{b}_n)$ est une base, et l'on note $c(\mathbf{v})$ les coordonnées de $\mathbf{v}$. Montre que $c(\lambda\mathbf{v} + \mu\mathbf{w}) = \lambda\,c(\mathbf{v}) + \mu\,c(\mathbf{w})$.
4. Avec la famille liée $(\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3)$ de la fiche (§2), écris le vecteur $\mathbf{u}_3$ de deux façons différentes comme combinaison de $\mathbf{u}_1$, $\mathbf{u}_2$, $\mathbf{u}_3$. Quelle question montre que c'était inévitable ?

### Ex M12a.16 — Le noyau est un sous-espace, et une application linéaire est injective si et seulement si son noyau est {0} ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer que noyau et image sont des sous-espaces, et le critère d'injectivité par le noyau.
**Prérequis :** fiche §1, §5 et §6 · **Parcours :** C, E

$f : V \to W$ est une application linéaire.
1. Montre que $f(\mathbf{0}) = \mathbf{0}$.
2. Montre que $\ker f$ est un sous-espace de $V$.
3. Montre que $\operatorname{Im} f$ est un sous-espace de $W$.
4. Montre que, si $f$ est injective, alors $\ker f = \{\mathbf{0}\}$.
5. Réciproquement, montre que, si $\ker f = \{\mathbf{0}\}$, alors $f$ est injective (pars de $f(\mathbf{x}) = f(\mathbf{y})$).
6. Déduis-en qu'une matrice $\mathbf{A}$ de forme $(m, n)$ avec $n > m$ n'est jamais injective (pense aux variables libres de $\mathbf{A}\mathbf{x} = \mathbf{0}$).

### Ex M12a.17 — Le théorème du rang : dim ker + rang = nombre de colonnes ∂ ★★★ ⏱️ 25 min
**Objectif :** démontrer que les vecteurs construits à partir des colonnes libres forment une base du noyau, et en déduire le théorème du rang.
**Prérequis :** fiche §4 et §6 ; M09a §6 (opérations élémentaires) · **Parcours :** C

$\mathbf{A}$ a la forme $(m, n)$, $\mathbf{R}$ est sa forme échelonnée réduite, avec $r$ pivots. Pour chaque colonne libre $j$, on note $\mathbf{k}_j$ le vecteur construit comme dans la fiche (§6) : $x_j = 1$, les autres variables libres à 0, et $x_p = -R_{ij}$ pour le pivot de la ligne $i$, dans la colonne $p$.
1. Montre que $\mathbf{A}\mathbf{x} = \mathbf{0}$ et $\mathbf{R}\mathbf{x} = \mathbf{0}$ ont les mêmes solutions.
2. Montre que $\mathbf{R}\mathbf{k}_j = \mathbf{0}$ (écris la ligne $i$ de $\mathbf{R}\mathbf{k}_j$). Déduis-en $\mathbf{k}_j \in \ker\mathbf{A}$.
3. Montre que les $\mathbf{k}_j$ forment une famille libre (regarde leurs coordonnées libres).
4. Soit $\mathbf{x} \in \ker\mathbf{A}$, et $\mathbf{y} = \mathbf{x} - \sum_{j \text{ libre}} x_j\,\mathbf{k}_j$. Montre que les coordonnées libres de $\mathbf{y}$ sont nulles, puis que $\mathbf{y} = \mathbf{0}$ (utilise $\mathbf{R}\mathbf{y} = \mathbf{0}$, ligne par ligne). Conclus que les $\mathbf{k}_j$ engendrent $\ker\mathbf{A}$.
5. Déduis-en $\dim\ker\mathbf{A} + \operatorname{rg}(\mathbf{A}) = n$.
6. Déduis-en qu'une matrice carrée est injective si et seulement si elle est surjective.

### Ex M12a.18 — rg(AB) ≤ min(rg A, rg B) ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la borne sur le rang d'un produit, par les colonnes et par le noyau, et voir qu'elle n'est pas toujours atteinte.
**Prérequis :** fiche §4 et §6 ; Ex M12a.17 · **Parcours :** C

$\mathbf{A}$ a la forme $(m, n)$ et $\mathbf{B}$ la forme $(n, p)$.
1. Montre que chaque colonne de $\mathbf{A}\mathbf{B}$ est dans $\operatorname{Im}\mathbf{A}$. Déduis-en $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \operatorname{rg}(\mathbf{A})$.
2. Avec $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$ et $\operatorname{rg}(\mathbf{M}) = \operatorname{rg}(\mathbf{M}^\top)$, déduis-en $\operatorname{rg}(\mathbf{A}\mathbf{B}) \le \operatorname{rg}(\mathbf{B})$.
3. Une autre preuve de 2 : montre que $\ker\mathbf{B} \subseteq \ker(\mathbf{A}\mathbf{B})$, puis applique le théorème du rang à $\mathbf{B}$ et à $\mathbf{A}\mathbf{B}$ (qui ont toutes deux $p$ colonnes).
4. Montre que, si $\mathbf{A}$ est carrée et inversible, $\operatorname{rg}(\mathbf{A}\mathbf{B}) = \operatorname{rg}(\mathbf{B})$ (écris $\mathbf{B} = \mathbf{A}^{-1}(\mathbf{A}\mathbf{B})$).
5. Trouve deux matrices $2 \times 2$ de rang 1 dont le produit est la matrice nulle. Que dit cet exemple de la borne ?

### Ex M12a.19 — L'inverse d'une application affine bijective est affine ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer qu'une application affine est bijective exactement quand sa partie linéaire est inversible, et que sa réciproque est affine.
**Prérequis :** fiche §6 et §8 ; Ex M12a.16 · **Parcours :** C

$\varphi(\mathbf{x}) = \mathbf{A}\mathbf{x} + \mathbf{b}$, de $\mathbb{R}^n$ dans $\mathbb{R}^n$.
1. Montre que $\varphi(\mathbf{x}) = \varphi(\mathbf{y})$ si et seulement si $\mathbf{x} - \mathbf{y} \in \ker\mathbf{A}$. Déduis-en : $\varphi$ injective $\iff$ $\ker\mathbf{A} = \{\mathbf{0}\}$.
2. Montre que $\mathbf{y}$ est atteint par $\varphi$ si et seulement si $\mathbf{y} - \mathbf{b} \in \operatorname{Im}\mathbf{A}$. Déduis-en : $\varphi$ surjective $\iff$ $\operatorname{Im}\mathbf{A} = \mathbb{R}^n$.
3. Conclus : $\varphi$ est bijective si et seulement si $\mathbf{A}$ est inversible (utilise le théorème du rang).
4. On suppose $\mathbf{A}$ inversible. Résous $\varphi(\mathbf{x}) = \mathbf{y}$, et montre que $\varphi^{-1}$ est affine ; donne sa partie linéaire et sa translation.
5. Montre que $\varphi$ conserve les combinaisons affines (coefficients de somme 1), et que ce n'est pas vrai pour une combinaison dont les coefficients ont une autre somme.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12a.20 — Pont : une feature somme de deux autres rend XᵀX singulière, et le noyau dit laquelle 🔗 ★ ⏱️ 15 min
**Objectif :** relier une feature redondante au noyau de $\mathbf{X}$, au rang de $\mathbf{X}^\top\mathbf{X}$ et à la non-unicité des poids.
**Prérequis :** fiche §4 et §6 ; M09a §8 · **Parcours :** C, E

Un tableau décrit quatre livraisons par le temps de trajet (min), le temps passé sur place (min) et le temps total (min) :

$$\mathbf{X} = \begin{pmatrix} 12 & 30 & 42 \\ 25 & 15 & 40 \\ 8 & 50 & 58 \\ 20 & 20 & 40 \end{pmatrix}.$$

Un modèle linéaire sans biais prédit $\mathbf{X}\mathbf{w}$, avec par exemple $\mathbf{w} = (0{,}5 ;\ 1 ;\ 0)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\operatorname{rg}(\mathbf{X})$ | un entier |
| b | $\operatorname{rg}(\mathbf{X}^\top\mathbf{X})$ | un entier |
| c | le vecteur de base de $\ker\mathbf{X}$ dont la dernière coordonnée vaut 1 | une liste de 3 nombres |
| d | vrai ou faux : $\mathbf{X}^\top\mathbf{X}$ est inversible | `True` ou `False` |
| e | les quatre prédictions $\mathbf{X}\mathbf{w}'$ des poids $\mathbf{w}' = \mathbf{w} + 2\,\mathbf{d}$, où $\mathbf{d}$ est le vecteur de c) | une liste de 4 nombres (1 décimale) |
| f | vrai ou faux : après avoir retiré la colonne du temps total, $\mathbf{X}^\top\mathbf{X}$ (alors de forme $(2, 2)$) est inversible | `True` ou `False` |

Dans ta copie : compare e) avec $\mathbf{X}\mathbf{w}$. Que dit le vecteur $\mathbf{d}$ sur les features en cause ? Pourquoi aucune méthode ne peut-elle choisir entre $\mathbf{w}$ et $\mathbf{w}'$ au vu des seules données ? Que changerait une colonne « temps total » mesurée au chronomètre, qui ne serait égale à la somme qu'à quelques secondes près ?

### Ex M12a.21 — Pont : projeter sur un plan puis revenir, ce que la transformation inverse ne peut pas rendre 🔗 ★★ ⏱️ 15 min
**Objectif :** voir sur un encodeur et un décodeur linéaires que l'information écrasée par un noyau ne se récupère pas.
**Prérequis :** fiche §6 et §8 · **Parcours :** C

Un « encodeur » résume un vecteur de $\mathbb{R}^3$ en deux nombres, $\mathbf{E}\mathbf{x}$, et un « décodeur » tente de le reconstruire, $\mathbf{D}\mathbf{E}\mathbf{x}$ :

$$\mathbf{E} = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & -1 \end{pmatrix}, \qquad \mathbf{D} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | $\operatorname{rg}(\mathbf{E})$ | un entier |
| b | le vecteur de base de $\ker\mathbf{E}$ dont la dernière coordonnée vaut 1 | une liste de 3 nombres |
| c | $\mathbf{E}(0, 3, 1)$ | une liste de 2 nombres |
| d | vrai ou faux : il existe une matrice $\mathbf{D}'$ de forme $(3, 2)$ telle que $\mathbf{D}'\mathbf{E} = \mathbf{I}_3$ | `True` ou `False` |
| e | la matrice $\mathbf{D}\mathbf{E}$ | une matrice |
| f | la reconstruction $\mathbf{D}\mathbf{E}\mathbf{x}$ de $\mathbf{x} = (0, 3, 1)$ | une liste de 3 nombres |
| g | l'erreur de reconstruction $\mathbf{x} - \mathbf{D}\mathbf{E}\mathbf{x}$ pour ce même $\mathbf{x}$ | une liste de 3 nombres |

Dans ta copie : calcule aussi $\mathbf{E}(1, 2, 0)$ et compare avec c). Calcule $\mathbf{E}\mathbf{D}$ : qu'en déduis-tu pour $\mathbf{E}$ appliquée à l'erreur de g) ? Quels vecteurs $\mathbf{x}$ sont reconstruits exactement ? Pour d), utilise le rang d'un produit.

### Ex M12a.22 — MML §2.4 et §2.5 : espaces vectoriels, sous-espaces et indépendance, en anglais 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais la définition abstraite d'un espace vectoriel et de l'indépendance, et la relier à la fiche.
**Prérequis :** fiche §1 et §2 · **Parcours :** C

Lis MML §2.4 et §2.5. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Au §2.4.1, qu'est-ce qu'un groupe ? Quelles propriétés le livre demande-t-il ? $(\mathbb{R}^n, +)$ en est-il un ? Et les réels non nuls avec la multiplication ?
2. Au §2.4.2, comment le livre appelle-t-il les deux opérations d'un espace vectoriel ? Quels exemples d'espaces vectoriels donne-t-il ? Quel vocabulaire emploie-t-il pour le vecteur nul ?
3. Au §2.4.3, quelles conditions le livre vérifie-t-il pour qu'une partie soit un sous-espace ? Parmi ses exemples de parties de $\mathbb{R}^2$, lesquelles sont des sous-espaces, et pourquoi pas les autres ?
4. Au §2.5, comment le livre définit-il l'indépendance linéaire ? Quelle méthode pratique donne-t-il pour la tester, et que disent les colonnes à pivot et les colonnes sans pivot ?
5. Compare la définition du livre avec le test de la fiche (§2) : sont-ils équivalents ? Pourquoi ?
6. Note trois mots ou tournures en anglais de ces sections, avec leur traduction.

### Ex M12a.23 — MML §2.6 à §2.8 : base, rang, applications linéaires, changement de base, espaces affines 📖 ★★ ⏱️ 45 min
**Objectif :** lire en anglais les sections du livre sur les bases, le rang, les applications linéaires et les espaces affines, et retrouver les résultats de la fiche dans ses notations.
**Prérequis :** fiche §3 à §8 · **Parcours :** C

Lis MML §2.6, §2.7 et §2.8. Réponds dans ta copie, **avec tes mots**.
1. Au §2.6.1, comment le livre définit-il une famille génératrice et une base ? Quelles caractérisations équivalentes d'une base donne-t-il ? Comment détermine-t-il une base d'un sous-espace engendré par des vecteurs ?
2. Au §2.6.2, quelles propriétés du rang le livre énonce-t-il ? Note deux propriétés que la fiche énonce aussi (§4 et §6), et une qu'elle n'énonce pas.
3. Au §2.7.1, dans quel ordre le livre range-t-il les coordonnées de $\Phi(\mathbf{b}_j)$ dans la matrice d'une application ? Compare avec la fiche (§5).
4. Au §2.7.2, que sont les matrices $\mathbf{S}$ et $\mathbf{T}$ du théorème de changement de base ? Quelle différence le livre fait-il entre matrices *equivalent* et *similar* ?
5. Au §2.7.3, comment le livre nomme-t-il le noyau, l'image et le théorème du rang ? Vérifie ce théorème sur la matrice $\mathbf{A}$ du §4 de la fiche.
6. Au §2.8, comment le livre définit-il un sous-espace affine (*support point*, direction) et une application affine ? Quelles propriétés d'une application affine énonce-t-il ?
7. Note trois mots ou tournures en anglais de ces sections, avec leur traduction.

### Ex M12a.24 — Fermi : les paramètres d'une application linéaire, puis affine, d'images 32 × 32 en couleurs vers 100 classes 🧮 ★ ⏱️ 10 min
**Objectif :** compter les paramètres d'une application linéaire et d'une application affine, et estimer ce que leur matrice peut et ne peut pas représenter.
**Prérequis :** fiche §4 à §8 · **Parcours :** C

Un classifieur linéaire reçoit des images couleur de $32 \times 32$ pixels (3 canaux), aplaties en un vecteur, et calcule un score pour chacune de 100 classes. Ordres de grandeur seulement, sauf en 1.
1. De quel $\mathbb{R}^n$ dans quel $\mathbb{R}^m$ va l'application ? Quelle est la forme de sa matrice ?
2. Combien de paramètres a l'application linéaire ? Et l'application affine (avec un biais par classe) ?
3. Quel est le plus grand rang possible de la matrice ? La plus petite dimension possible de son noyau ? Que représente un vecteur de ce noyau, pour une image ?
4. Combien d'octets occupent les paramètres en `float32` (4 octets par nombre) ?
5. On impose à la matrice d'être un produit $\mathbf{B}\mathbf{C}$, avec un rang intermédiaire $r = 16$. Combien de paramètres reste-t-il, et par combien leur nombre est-il divisé ? Quelle limite cela impose-t-il au rang ?

### Ex M12a.25 — Expliquer la dimension et le rang sans une seule formule 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer en mots ce que mesurent la dimension d'un espace et le rang d'un tableau de données.
**Prérequis :** fiche §3 et §4 · **Parcours :** C, E

Une collègue, qui n'a jamais fait d'algèbre linéaire, te demande pourquoi l'on dit qu'un tableau de 1 000 lignes et 50 colonnes « est de rang 12 ». Explique-lui, **en huit lignes au plus**, sans formule : ce qu'est la dimension (avec un exemple de la vie courante), ce que mesure le rang d'un tableau, pourquoi il ne peut pas dépasser 50, et ce que cela dit des 50 colonnes.

<a id="entretien"></a>

## 💼 Entretien

### M12a.E1 — « Que veut dire qu'une matrice est de rang plein, et pourquoi s'en soucier ? » 💼 ★ ⏱️ 10 min
*Fiche §4 et §6 · parcours C*

« Que veut dire qu'une matrice est de rang plein, et pourquoi s'en soucier ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit donner la définition, la conséquence pour les solutions d'un système et pour l'inversibilité de $\mathbf{X}^\top\mathbf{X}$, un exemple de machine learning où le rang n'est pas plein, et une précaution sur le rang calculé en virgule flottante. Compare ensuite avec la réponse modèle de `05_solutions.md`.

### M12a.E2 — « Qu'est-ce que le noyau d'une matrice, et où le croise-t-on en ML ? » 💼 ★ ⏱️ 10 min
*Fiche §6 · parcours C*

« Qu'est-ce que le noyau d'une matrice, et où le croise-t-on en ML ? »

Prépare une réponse orale de **60 secondes**. Elle doit donner la définition et l'espace où vit le noyau, le lien avec la non-unicité des solutions et avec le théorème du rang, deux situations de machine learning où il intervient, et un piège de vocabulaire (le mot « noyau » a d'autres sens en machine learning). Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m12a_espaces_vectoriels/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M12a.26 | Tester l'indépendance et extraire une base de l'espace des colonnes · `is_independent, column_space_basis` | 🔨 | ★★ | 20 | C, E |
| M12a.27 | Une base du noyau, colonne libre par colonne libre · `null_space_basis` | 🔨 | ★★ | 25 | C, E |
| M12a.28 | Coordonnées dans une base et changement de base · `coordinates, change_of_basis` | 🔨 | ★ | 20 | C |
| M12a.29 | `sympy.Matrix.nullspace`, `columnspace` et `rank` contre tes fonctions | 📦 | ★ | 15 | C, E |
| M12a.30 | Prédire le rang : matrices aléatoires, produits, colonnes répétées | 🔮 | ★ | 10 | C, E |
| M12a.31 | Le rang numérique : une colonne presque redondante et le choix de la tolérance | 🔬 | ★★ | 20 | C |
| M12a.32 | Une application linéaire du plan : l'image du carré unité, et ce qu'elle écrase quand son noyau n'est pas nul | 🎨 | ★ | 20 | C, E |
| M12a.33 | Chasse à l'erreur : une « base » liée, un noyau faux, S⁻¹AS écrit à l'envers | 🐛 | ★ | 15 | C |
| M12a.34 | Un test de propriété : A fois une base du noyau donne 0, et le théorème du rang sur des matrices aléatoires | 🛠️ | ★ | 15 | C |
| M12a.35 | Défi : retrouver les relations linéaires exactes cachées entre les colonnes d'un tableau, sans en inventer | 🏆 | ★★★ | 30 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
