# M13b · Optimisation sous contraintes et SVM — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m13b_lagrange_svm/06_mes_reponses.md` (créée par `python tools/start_chapter.py M13b`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🧮, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : le lagrangien s'écrit $f + \sum_i \mu_i g_i + \sum_j \lambda_j h_j$ pour des contraintes $g_i(\mathbf{x}) \le 0$ et $h_j(\mathbf{x}) = 0$, avec $\mu_i \ge 0$ ; les multiplicateurs d'une SVM s'écrivent $\alpha_i$ ; la **marge** est $\rho = 1/\lVert\mathbf{w}\rVert$ et la **bande** a une largeur $2\rho$ ; la marge fonctionnelle d'un exemple est $t_i = y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$, avec $y_i \in \{-1, +1\}$ ; l'objectif de la marge souple est $J(\mathbf{w}, b) = \frac{1}{2}\lVert\mathbf{w}\rVert^2 + C\sum_i \max(0, 1 - t_i)$, une **somme** de hinges ; le noyau RBF est $e^{-\gamma\lVert\mathbf{x} - \mathbf{z}\rVert^2}$. Quand un énoncé fixe une autre convention de signe, il le dit.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M13b.Q1 — Lagrange : ce que dit ∇f = λ ∇g 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Au minimum de $f$ sous la contrainte $g(\mathbf{x}) = 0$, que peut-on dire de $\nabla f$ et de la courbe $g = 0$ ?
2. Vrai ou faux : tout point où $\nabla f + \lambda\nabla g = \mathbf{0}$ et $g = 0$ est un minimum sous contrainte.
3. Le minimum **libre** de $f$ vérifie justement $g = 0$ : que vaut le multiplicateur ?
4. Avec trois variables et deux contraintes d'égalité, combien d'inconnues compte le système de Lagrange ?
5. Un multiplicateur vaut $\lambda = -5$ pour la contrainte $g(\mathbf{x}) = c$ (lagrangien $f + \lambda(g - c)$). Le minimum monte-t-il ou baisse-t-il quand $c$ augmente de 0,1, et d'environ combien ?
6. Pourquoi le théorème demande-t-il $\nabla g(\mathbf{x}^*) \ne \mathbf{0}$ ?

### M13b.Q2 — Contrainte active ou inactive ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

1. Qu'appelle-t-on une contrainte d'inégalité **active** au point $\mathbf{x}^*$ ?
2. Vrai ou faux : une contrainte inactive a toujours un multiplicateur nul.
3. Vrai ou faux : une contrainte active a toujours un multiplicateur strictement positif.
4. Minimiser $(x - 3)^2$ sous $x \le 5$ : la contrainte est-elle active ? Et sous $x \le 1$ ?
5. On a supposé une contrainte $g \le 0$ active et trouvé $\mu = -2$. Que conclure ?
6. Comment écrire la contrainte $x_1 + x_2 \ge 4$ sous la forme $g(\mathbf{x}) \le 0$ ?

### M13b.Q3 — Primal, dual, dualité faible 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C*

1. Comment se définit la fonction duale $D(\boldsymbol{\mu})$ à partir du lagrangien ?
2. Vrai ou faux : la fonction duale est concave, même quand le problème primal ne l'est pas.
3. Un problème a pour minimum $f^* = 7$. La fonction duale peut-elle valoir 8 en un $\boldsymbol{\mu} \ge \mathbf{0}$ ? Et 5 ?
4. Qu'est-ce que le saut de dualité, et quand est-il nul ?
5. Vrai ou faux : le dual a une variable par inconnue du primal.
6. Un point admissible $\mathbf{x}$ et des multiplicateurs $\boldsymbol{\mu} \ge \mathbf{0}$ vérifient $f(\mathbf{x}) = D(\boldsymbol{\mu})$. Que peut-on en conclure ?

### M13b.Q4 — Problème convexe ou pas ? 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

Pour chaque problème, dis s'il est convexe, et pourquoi en une phrase.
1. $\min x^2 + 3y^2$ sous $2x - y = 4$.
2. $\min x^2 + 3y^2$ sous $x^2 - y = 0$.
3. $\max \mathbf{u}^\top\mathbf{C}\mathbf{u}$ sous $\lVert\mathbf{u}\rVert \le 1$, avec $\mathbf{C}$ définie positive.
4. $\min e^{x} + e^{-y}$ sous $x + y \le 2$ et $x \ge 0$.
5. $\min \lVert\mathbf{w}\rVert^2$ sous $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ pour tout $i$.
6. Vrai ou faux : un problème convexe a toujours exactement un minimum.

### M13b.Q5 — Ce que maximise une SVM, ce que minimise son problème 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

1. Quelle quantité géométrique la SVM à marge dure rend-elle la plus grande ?
2. Pourquoi minimise-t-on $\frac{1}{2}\lVert\mathbf{w}\rVert^2$ plutôt que de maximiser $\frac{1}{\lVert\mathbf{w}\rVert}$ ou de minimiser $\lVert\mathbf{w}\rVert$ ?
3. Sur des données séparables, combien de vecteurs de support y a-t-il au moins, et pourquoi ?
4. $\lVert\mathbf{w}\rVert = 0{,}25$ : que valent la marge et la largeur de la bande ?
5. Vrai ou faux : deux solutions optimales différentes peuvent avoir deux $\mathbf{w}$ différents.
6. Pourquoi la contrainte s'écrit-elle « $\ge 1$ » et pas « $\ge \rho$ » ?

### M13b.Q6 — La hinge loss : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

1. Vrai ou faux : la hinge loss $\max(0, 1 - t)$ est convexe en $t$.
2. Vrai ou faux : elle est dérivable partout.
3. Vrai ou faux : un exemple bien classé ($t > 0$) ne coûte jamais rien.
4. Vrai ou faux : pour tout $t$, $\max(0, 1 - t)$ est au moins égal à l'erreur (1 si $t \le 0$, 0 sinon).
5. Donne deux sous-gradients de la hinge en $t = 1$.
6. Vrai ou faux : pour $n = 5$ exemples et $C = 2$, la forme « hinge moyenne $+ \frac{\lambda}{2}\lVert\mathbf{w}\rVert^2$ » a $\lambda = 0{,}1$.

### M13b.Q7 — Noyau valide ou pas ? 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C, E*

Pour chacune des fonctions $k(\mathbf{x}, \mathbf{z})$ de $\mathbb{R}^p \times \mathbb{R}^p$, dis si c'est un noyau valide, en une phrase.
1. $k(\mathbf{x}, \mathbf{z}) = 3\,\mathbf{x} \cdot \mathbf{z}$.
2. $k(\mathbf{x}, \mathbf{z}) = \mathbf{x} \cdot \mathbf{z} + 5$.
3. $k(\mathbf{x}, \mathbf{z}) = -\,\mathbf{x} \cdot \mathbf{z}$.
4. $k(\mathbf{x}, \mathbf{z}) = (\mathbf{x} \cdot \mathbf{z})^3 + e^{-2\lVert\mathbf{x} - \mathbf{z}\rVert^2}$.
5. $k(\mathbf{x}, \mathbf{z}) = x_1 z_2$ (en dimension 2).
6. Vrai ou faux : si deux des points sont confondus, la matrice de Gram RBF est singulière.

### M13b.Q8 — Primal ou dual : lequel résoudre, et quand ? 🧠 ★ ⏱️ 4 min
*Fiche §8 · parcours C*

1. Combien de variables a le problème primal d'une SVM à marge souple, pour $n$ exemples et $p$ features ? Et le dual ?
2. Un dataset de 2 millions d'exemples et 30 features, une SVM linéaire : primal ou dual ? Pourquoi ?
3. Un dataset de 4 000 exemples, un noyau RBF : primal ou dual ? Pourquoi ?
4. Quelle matrice le dual doit-il manipuler, et de quelle taille ?
5. Vrai ou faux : pour prédire avec une SVM à noyau, il faut garder les vecteurs de support.
6. Vrai ou faux : le noyau RBF peut s'utiliser dans le primal en calculant $\varphi$.

<a id="rappels"></a>

## 🔁 Rappels

### M13b.R1 — La marge géométrique et l'astuce du biais (M10) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C, E*

Le séparateur $3x_1 - 4x_2 + 2 = 0$ ; label $+1$ pour $(1, -1)$ et $(-1, -2)$, label $-1$ pour $(0, 3)$ et $(-2, 1)$.
1. Les quatre marges fonctionnelles $y_i(\mathbf{w} \cdot \mathbf{x}_i + b)$ ?
2. La marge géométrique du séparateur ?
3. Divise $(\mathbf{w}, b)$ pour que la plus petite marge fonctionnelle vaille 1 : que deviennent $\mathbf{w}$, $b$, $\lVert\mathbf{w}\rVert$ ? Vérifie que $1/\lVert\mathbf{w}\rVert$ redonne la marge trouvée en 2.
4. Écris le séparateur avec l'astuce du biais (le biais en première coordonnée).
5. Ce séparateur a-t-il forcément la plus grande marge possible ?

### M13b.R2 — Gradient et lignes de niveau (M05b) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

$f(x, y) = x^2 - xy + 2y^2$.
1. $\nabla f(x, y)$ ?
2. $\nabla f(1, -2)$ ?
3. Une direction tangente à la ligne de niveau de $f$ qui passe par $(1, -2)$ ?
4. Dans quelle direction $f$ augmente-t-elle le plus vite en $(1, -2)$ ?
5. Pourquoi le gradient est-il orthogonal aux lignes de niveau (en une phrase) ?

### M13b.R3 — Matrices définies positives (M12c) 🔁 ★ ⏱️ 5 min
*Fiche §5 et §8 · parcours C, E*

1. La matrice $\begin{pmatrix} 6 & 2 \\ 2 & 1 \end{pmatrix}$ est-elle définie positive ? (Trace et déterminant.)
2. Et $\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$ ?
3. La matrice de Gram (des produits scalaires deux à deux) des vecteurs $(1, 2, 1)$, $(0, 1, -1)$ et $(1, 3, 0)$ ?
4. Est-elle définie positive, semi-définie positive, ou ni l'un ni l'autre ? Pourquoi ?
5. Pourquoi une matrice de Gram est-elle toujours semi-définie positive ?

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M13b.1 — Lagrange à la main : un produit maximal sous une contrainte linéaire ✏️ ★ ⏱️ 15 min
**Objectif :** résoudre un problème d'optimisation sous une contrainte d'égalité par le lagrangien, et lire le multiplicateur comme une sensibilité.
**Prérequis :** fiche §1 · **Parcours :** C, E

On maximise le produit $P = xyz$ de trois nombres positifs sous la contrainte $x + 2y + 4z = 24$. Lagrangien, pour ce maximum : $\mathcal{L} = xyz - \lambda(x + 2y + 4z - 24)$ (avec ce signe, $\lambda$ est la sensibilité $\frac{dP^*}{dc}$ du maximum quand le second membre $c = 24$ varie).

| | Question | Réponse attendue |
|---|---|---|
| a | le point $(x, y, z)$ du maximum | une liste de 3 nombres |
| b | le produit maximal $P^*$ | un nombre |
| c | le multiplicateur $\lambda$ | un nombre |
| d | l'estimation de $P^*$ pour $x + 2y + 4z = 25$ par $P^* + \lambda \times 1$ | un nombre |
| e | la vraie valeur de $P^*$ pour $x + 2y + 4z = 25$ | une fraction |
| f | $\frac{dP^*}{dc}$ en $c = 24$, à partir de la formule de $P^*(c)$ | un nombre |
| g | le produit au point admissible $(12, 2, 2)$ | un nombre |

Dans ta copie : écris les quatre équations du système et résous-les (montre que $x = 2y = 4z$). Établis la formule de $P^*(c)$ pour tout $c > 0$. Pourquoi la condition de Lagrange seule ne prouve-t-elle pas que c'est un maximum, et comment g) aide-t-il à s'en convaincre ?

### Ex M13b.2 — La distance d'un point à un plan, retrouvée par Lagrange ✏️ ★★ ⏱️ 20 min
**Objectif :** retrouver la projection orthogonale et la distance d'un point à un plan en minimisant un carré de distance sous une contrainte d'égalité.
**Prérequis :** fiche §1 et §2 ; M07 · **Parcours :** C

Le plan $\Pi : 4x - 4y + 7z = 10$ et le point $\mathbf{x}_0 = (5, 1, 3)$. On minimise $\lVert\mathbf{x} - \mathbf{x}_0\rVert^2$ sous $\mathbf{n} \cdot \mathbf{x} = 10$, avec $\mathbf{n} = (4, -4, 7)$ et le lagrangien $\lVert\mathbf{x} - \mathbf{x}_0\rVert^2 + \lambda(\mathbf{n} \cdot \mathbf{x} - 10)$.

| | Question | Réponse attendue |
|---|---|---|
| a | le multiplicateur $\lambda$ | une fraction |
| b | le point de $\Pi$ le plus proche de $\mathbf{x}_0$ | une liste de 3 fractions |
| c | le minimum de $\lVert\mathbf{x} - \mathbf{x}_0\rVert^2$ | un nombre |
| d | la distance de $\mathbf{x}_0$ à $\Pi$ | un nombre |
| e | $\mathbf{n} \cdot \mathbf{x}_0$ | un nombre |
| f | $\lVert\mathbf{n}\rVert$ | un nombre |

Dans ta copie : écris la stationnarité, déduis-en que $\mathbf{x} - \mathbf{x}_0$ est colinéaire à $\mathbf{n}$, puis la formule générale de la distance d'un point à un plan $\mathbf{n} \cdot \mathbf{x} = d$. Compare avec la formule de M07 : laquelle des deux méthodes se généralise à une surface qui n'est pas un plan ?

### Ex M13b.3 — Un problème quadratique sous deux contraintes linéaires : le système de Lagrange ✏️ ★★ ⏱️ 20 min
**Objectif :** écrire et résoudre le système par blocs d'un problème quadratique sous contraintes d'égalité, et voir l'effet d'une contrainte de plus.
**Prérequis :** fiche §2 ; M09a ; M12c.19 · **Parcours :** C, E

On minimise $f(\mathbf{x}) = \frac{1}{2}\mathbf{x}^\top\mathbf{Q}\mathbf{x} + \mathbf{c}^\top\mathbf{x}$ sous $\mathbf{A}\mathbf{x} = \mathbf{b}$, avec
$$\mathbf{Q} = \begin{pmatrix} 4 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix}, \quad \mathbf{c} = \begin{pmatrix} -2 \\ 0 \\ 1 \end{pmatrix}, \quad \mathbf{A} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & -1 \end{pmatrix}, \quad \mathbf{b} = \begin{pmatrix} 3 \\ 1 \end{pmatrix},$$
et le lagrangien $f(\mathbf{x}) + \boldsymbol{\lambda}^\top(\mathbf{A}\mathbf{x} - \mathbf{b})$.

| | Question | Réponse attendue |
|---|---|---|
| a | la taille $N$ de la matrice par blocs (elle est $N \times N$) | un entier |
| b | la solution $\mathbf{x}^*$ | une liste de 3 fractions |
| c | les multiplicateurs $\boldsymbol{\lambda}$ | une liste de 2 fractions |
| d | $f(\mathbf{x}^*)$ | une fraction |
| e | le déterminant de la matrice par blocs | un entier |
| f | la solution sous la seule première contrainte $x_1 + x_2 + x_3 = 3$ | une liste de 3 nombres |
| g | la valeur de $f$ en f) | un nombre |
| h | la valeur minimale de $f$ sans contrainte | une fraction |

Dans ta copie : écris le système par blocs en entier. Pourquoi h) < g) < d) ? Vérifie que $\mathbf{Q}$ est définie positive : qu'est-ce que cela garantit pour $\mathbf{x}^*$ ?

### Ex M13b.4 — Relire l'ACP par Lagrange : maximiser uᵀCu sous ‖u‖ = 1 ✏️ ★★ ⏱️ 20 min
**Objectif :** retrouver les axes principaux d'une matrice de covariance par les multiplicateurs de Lagrange, le premier puis le deuxième.
**Prérequis :** fiche §2 ; M12c ; M12d · **Parcours :** C

La matrice de covariance de trois features : $\mathbf{C} = \begin{pmatrix} 2 & -3 & 1 \\ -3 & 10 & -3 \\ 1 & -3 & 8 \end{pmatrix}$. Ses valeurs propres sont des entiers.

| | Question | Réponse attendue |
|---|---|---|
| a | la plus grande valeur propre | un entier |
| b | le premier axe $\mathbf{u}_1$, unitaire, avec la convention de M12d (sa coordonnée de plus grande valeur absolue est positive) | une liste de 3 nombres (4 décimales) |
| c | $\mathbf{u}_1^\top\mathbf{C}\mathbf{u}_1$ | un nombre |
| d | le multiplicateur $\nu$ de la contrainte $\mathbf{u} \cdot \mathbf{u}_1 = 0$, au deuxième axe | un nombre |
| e | la deuxième valeur propre | un entier |
| f | la part de variance du premier axe | une fraction |
| g | la part de variance des deux premiers axes | une fraction |
| h | $\mathbf{u}^\top\mathbf{C}\mathbf{u}$ pour $\mathbf{u} = (1, 0, 0)$ | un nombre |

Dans ta copie : écris le lagrangien $\mathbf{u}^\top\mathbf{C}\mathbf{u} - \lambda(\mathbf{u}^\top\mathbf{u} - 1)$, sa stationnarité, et montre que la valeur de l'objectif en un point critique est le multiplicateur. Pour le deuxième axe, écris le lagrangien avec deux multiplicateurs, $\lambda$ et $\nu$, et calcule $\nu$ (multiplie la stationnarité par $\mathbf{u}_1^\top$) : qu'en déduis-tu pour $\mathbf{u}$ ? Pourquoi la plus petite valeur propre est-elle aussi un point critique, et de quel genre ?

### Ex M13b.5 — Une contrainte d'inégalité : active ou non, les conditions KKT à la main ✏️ ★★ ⏱️ 20 min
**Objectif :** appliquer les conditions KKT à une contrainte d'inégalité, dans le cas actif et dans le cas inactif, et repérer un multiplicateur de mauvais signe.
**Prérequis :** fiche §3 · **Parcours :** C, E

On minimise $f(x, y) = x^2 + 2y^2 - 4x - 8y$ sous $2x + y \le c$, c'est-à-dire $g(x, y) = 2x + y - c \le 0$.

| | Question | Réponse attendue |
|---|---|---|
| a | vrai ou faux : pour $c = 3$, le minimum libre de $f$ est admissible | True ou False |
| b | pour $c = 3$, le multiplicateur $\mu$ | une fraction |
| c | pour $c = 3$, le point du minimum | une liste de 2 fractions |
| d | pour $c = 3$, le minimum $f^*$ | un nombre |
| e | pour $c = 8$, le minimum $f^*$ | un nombre |
| f | pour $c = 3$, la sensibilité $\frac{df^*}{dc}$ | une fraction |
| g | sous la contrainte **inverse** $2x + y \ge 3$, écrite $3 - 2x - y \le 0$ et supposée active : le multiplicateur obtenu | une fraction |

Dans ta copie : écris les quatre conditions KKT pour $c = 3$ et vérifie-les une à une. Pour $c = 8$, que vaut $\mu$, et pourquoi ? En g), que dit le signe trouvé, et quelle est la vraie solution sous la contrainte inverse ?

### Ex M13b.6 — La fonction duale d'un petit problème quadratique, et la dualité faible ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une fonction duale, vérifier qu'elle minore le minimum, et trouver son maximum.
**Prérequis :** fiche §4 · **Parcours :** C

On minimise $f(x, y) = x^2 + 2y^2$ sous $x + y \ge 6$, écrite $g(x, y) = 6 - x - y \le 0$.

| | Question | Réponse attendue |
|---|---|---|
| a | la fonction duale $D(\mu)$, pour $\mu \ge 0$ | une expression en `mu` |
| b | $D(4)$ | un nombre |
| c | le $\mu^*$ qui maximise $D$ | un nombre |
| d | $D(\mu^*)$ | un nombre |
| e | le point $(x^*, y^*)$ qui minimise $\mathcal{L}(\cdot, \mu^*)$ | une liste de 2 nombres |
| f | le minimum $f^*$ du problème | un nombre |
| g | $D(12)$ | un nombre |

Dans ta copie : écris le lagrangien, minimise-le en $(x, y)$ à $\mu$ fixé, et déduis $D$. Pourquoi b) et g) sont-ils plus petits que f) ? Vérifie que $(x^*, y^*, \mu^*)$ satisfait les conditions KKT. Le saut de dualité est-il nul ? Était-ce prévisible ?

### Ex M13b.7 — Reconnaître un problème convexe : fonctions, contraintes, ensembles ✏️ ★ ⏱️ 15 min
**Objectif :** décider si un problème d'optimisation est convexe en examinant son objectif et chacune de ses contraintes.
**Prérequis :** fiche §5 ; M10 · **Parcours :** C, E

Huit problèmes, en $(x, y) \in \mathbb{R}^2$ :
- (A) $\min x^2 + y^2$ sous $x + y \ge 1$ ;
- (B) $\min x^2 + y^2$ sous $x^2 + y^2 \ge 1$ ;
- (C) $\max x^2 + y^2$ sous $0 \le x \le 1$ et $0 \le y \le 1$ ;
- (D) $\min e^{x} + y^2$ sous $x - y = 2$ ;
- (E) $\min x$ sous $x^2 + y^2 = 4$ ;
- (F) $\min -\ln x - \ln y$ sous $x + y \le 4$, sur le domaine $x > 0$, $y > 0$ (un ouvert convexe) ;
- (G) $\min x^2 - y^2$ sous $\lvert x \rvert \le 1$ et $\lvert y \rvert \le 1$ ;
- (H) $\min \max(0, 1 - x) + x^2 + y^2$, sans contrainte.

| | Question | Réponse attendue |
|---|---|---|
| a | les lettres des problèmes convexes, dans l'ordre alphabétique | des lettres collées, comme `"BD"` |

Dans ta copie : pour chaque problème non convexe, dis quelle partie viole la définition (objectif non convexe, maximisation d'une fonction convexe, inégalité non convexe, égalité non affine). Pour (E), trouve quand même la solution (par Lagrange) : la théorie convexe ne s'applique pas, mais le problème se résout.

### Ex M13b.8 — Une SVM à marge dure sur trois points, résolue par les conditions KKT ✏️ ★★ ⏱️ 25 min
**Objectif :** résoudre une petite SVM à marge dure en devinant l'ensemble actif, puis en vérifiant toutes les conditions KKT.
**Prérequis :** fiche §6 et §8 · **Parcours :** C, E

Trois exemples : $\mathbf{x}_1 = (3, 5)$ et $\mathbf{x}_2 = (7, 7)$ de label $+1$, $\mathbf{x}_3 = (7, 2)$ de label $-1$. On suppose les trois contraintes $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$ **actives**.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{w}$ | une liste de 2 nombres |
| b | $b$ | un nombre |
| c | les multiplicateurs $(\alpha_1, \alpha_2, \alpha_3)$ | une liste de 3 nombres |
| d | $\frac{1}{2}\lVert\mathbf{w}\rVert^2$ | un nombre |
| e | la marge $\rho$ | un nombre (4 décimales) |
| f | la marge fonctionnelle d'un quatrième exemple $(0, 8)$ de label $+1$, sous la même solution | un nombre |
| g | le nombre de vecteurs de support | un entier |
| h | la valeur du dual, $\sum_i \alpha_i - \frac{1}{2}\lVert\mathbf{w}\rVert^2$ | un nombre |

Dans ta copie : pourquoi $\mathbf{w}$ est-il orthogonal à $\mathbf{x}_2 - \mathbf{x}_1$ ? Écris le système (trois contraintes actives, $\mathbf{w} = \sum_i \alpha_i y_i \mathbf{x}_i$, $\sum_i \alpha_i y_i = 0$) et résous-le. Vérifie les quatre conditions KKT. Avec le quatrième exemple de f), pourquoi la solution ne change-t-elle pas ?

### Ex M13b.9 — La hinge loss et l'objectif régularisé de quelques points ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des marges fonctionnelles, des hinges et l'objectif d'une SVM à marge souple, et passer à la forme « loss moyenne plus pénalité ».
**Prérequis :** fiche §7 · **Parcours :** C, E

$\mathbf{w} = (1 ;\ -0{,}5)$, $b = 0{,}5$, $C = 2$. Six exemples : label $+1$ pour $(3, 0)$, $(1, 0)$, $(0 ;\ 0{,}6)$ ; label $-1$ pour $(-1, 1)$, $(2 ;\ 1{,}8)$, $(-2 ;\ 0{,}4)$.

| | Question | Réponse attendue |
|---|---|---|
| a | les six marges fonctionnelles $t_i$, dans l'ordre | une liste de 6 nombres |
| b | les six hinges $\max(0, 1 - t_i)$ | une liste de 6 nombres |
| c | la hinge moyenne | un nombre (4 décimales) |
| d | $\frac{1}{2}\lVert\mathbf{w}\rVert^2$ | un nombre |
| e | l'objectif $J(\mathbf{w}, b)$ | un nombre |
| f | le $\lambda$ de la forme $\frac{1}{n}\sum_i \max(0, 1 - t_i) + \frac{\lambda}{2}\lVert\mathbf{w}\rVert^2$ | une fraction |
| g | le nombre d'exemples de marge fonctionnelle strictement inférieure à 1 | un entier |
| h | le nombre d'exemples mal classés ($t_i < 0$) | un entier |

Dans ta copie : range les six exemples selon leur marge fonctionnelle ($t_i > 1$, $0 \le t_i \le 1$, $t_i < 0$), et situe chaque groupe par rapport au bord de sa classe et à la frontière. Que vérifie la relation $J = nC \times$ (la forme de f)) ?

### Ex M13b.10 — Un pas de sous-gradient sur l'objectif d'une SVM linéaire ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer un sous-gradient de l'objectif d'une SVM linéaire, faire un pas, et voir le choix à faire en un point du coude.
**Prérequis :** fiche §7 · **Parcours :** C

$\mathbf{w} = (0{,}5 ;\ 1)$, $b = -1$, $C = 0{,}5$, pas $\eta = 0{,}2$. Quatre exemples : $(3 ;\ 0{,}5)$ de label $+1$, $(0, 3)$ de label $-1$, $(1, -1)$ de label $-1$, $(-1, 2)$ de label $+1$. Le sous-gradient est celui de la fiche : seuls les exemples de marge fonctionnelle **strictement** inférieure à 1 comptent.

| | Question | Réponse attendue |
|---|---|---|
| a | les quatre marges fonctionnelles | une liste de 4 nombres |
| b | $J(\mathbf{w}, b)$ | un nombre (4 décimales) |
| c | $\mathbf{g}_{\mathbf{w}}$ | une liste de 2 nombres |
| d | $g_b$ | un nombre |
| e | le nouveau $\mathbf{w}$, après un pas $\mathbf{w} - \eta\,\mathbf{g}_{\mathbf{w}}$ | une liste de 2 nombres |
| f | $J$ après le pas ($b$ change de $-\eta\,g_b$) | un nombre (4 décimales) |
| g | $\mathbf{g}_{\mathbf{w}}$ si l'on compte aussi l'exemple de marge exactement 1 | une liste de 2 nombres |

Dans ta copie : pourquoi g) est-il aussi un sous-gradient valide ? Après le pas, $J$ a-t-il baissé ? Est-ce garanti pour un pas plus grand ?

### Ex M13b.11 — Le dual d'une SVM : lire les vecteurs de support et retrouver w ✏️ ★★ ⏱️ 20 min
**Objectif :** à partir des multiplicateurs d'une SVM à marge souple, retrouver $\mathbf{w}$ et $b$, et classer les exemples selon les conditions KKT.
**Prérequis :** fiche §8 · **Parcours :** C

Une SVM à marge souple, $C = 1$, a été entraînée sur six exemples. Ses multiplicateurs :

| $i$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $\mathbf{x}_i$ | $(5, 6)$ | $(3, 7)$ | $(7, 4)$ | $(5, 8)$ | $(1, 5)$ | $(2, 5)$ |
| $y_i$ | $+1$ | $+1$ | $+1$ | $-1$ | $-1$ | $-1$ |
| $\alpha_i$ | 0,9 | 1 | 0 | 1 | 0 | 0,9 |

| | Question | Réponse attendue |
|---|---|---|
| a | $\sum_i \alpha_i y_i$ | un nombre |
| b | $\mathbf{w} = \sum_i \alpha_i y_i \mathbf{x}_i$ | une liste de 2 nombres |
| c | $b$, lu sur un vecteur de support libre | un nombre |
| d | les numéros des vecteurs de support | une liste d'entiers |
| e | les six marges fonctionnelles | une liste de 6 nombres |
| f | l'objectif primal $J(\mathbf{w}, b)$ | un nombre |
| g | la valeur du dual, $\sum_i \alpha_i - \frac{1}{2}\lVert\mathbf{w}\rVert^2$ | un nombre |

Dans ta copie : quels exemples sont des vecteurs de support libres, lesquels bornés ? Vérifie que b) donne bien la même valeur de $b$ sur les deux vecteurs libres. Les marges fonctionnelles de e) sont-elles cohérentes avec le tableau de « Lire les multiplicateurs » (fiche §8) ? Que dit l'égalité de f) et g) ?

### Ex M13b.12 — Le noyau (1 + x · z)² en dimension 2 : sa fonction φ à six coordonnées ✏️ ★★ ⏱️ 20 min
**Objectif :** développer le noyau polynomial de degré 2 en dimension 2, écrire sa fonction $\varphi$, voir le rôle de la constante, et compter ses coordonnées en dimension plus grande.
**Prérequis :** fiche §8 ; M09b · **Parcours :** C

$k(\mathbf{x}, \mathbf{z}) = (1 + \mathbf{x} \cdot \mathbf{z})^2$, avec $\mathbf{x}, \mathbf{z} \in \mathbb{R}^2$. On prend $\mathbf{x} = (4, -3)$ et $\mathbf{z} = (3, -5)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\varphi(\mathbf{x})$, dans l'ordre $(1, \sqrt{2}\,x_1, \sqrt{2}\,x_2, x_1^2, \sqrt{2}\,x_1x_2, x_2^2)$ | une liste de 6 nombres (2 décimales) |
| b | $\varphi(\mathbf{z})$, dans le même ordre | une liste de 6 nombres (2 décimales) |
| c | $k(\mathbf{x}, \mathbf{z})$ | un entier |
| d | pour le noyau $(3 + \mathbf{x} \cdot \mathbf{z})^2$, $\varphi(\mathbf{x})$ dans l'ordre $(3, \sqrt{6}\,x_1, \sqrt{6}\,x_2, x_1^2, \sqrt{2}\,x_1x_2, x_2^2)$ | une liste de 6 nombres (2 décimales) |
| e | le nombre de coordonnées de $\varphi$ pour $(1 + \mathbf{x} \cdot \mathbf{z})^2$ en dimension $p = 9$ | un entier |
| f | le même pour $(1 + \mathbf{x} \cdot \mathbf{z})^3$ en dimension $p = 9$ | un entier |

Dans ta copie : développe $(1 + x_1z_1 + x_2z_2)^2$ et lis-y $\varphi$ ; d'où viennent les $\sqrt{2}$ ? Vérifie que $\varphi(\mathbf{x}) \cdot \varphi(\mathbf{z})$ redonne c). Écris $\varphi$ pour $(c + \mathbf{x} \cdot \mathbf{z})^2$ : quelles coordonnées dépendent de $c$, et pourquoi faut-il $c \ge 0$ ? Retrouve e) et f) par `count_monomials` (M09b).

### Ex M13b.13 — La matrice de Gram d'un noyau RBF sur trois points, et l'effet de γ ✏️ ★ ⏱️ 15 min
**Objectif :** calculer une matrice de Gram RBF, une distance dans l'espace des features, et voir ce que devient la matrice quand $\gamma$ est très petit ou très grand.
**Prérequis :** fiche §8 · **Parcours :** C, E

Trois points : $\mathbf{x}_1 = (0, 0)$, $\mathbf{x}_2 = (3, 0)$, $\mathbf{x}_3 = (0, -2)$. Noyau RBF de paramètre $\gamma = 0{,}2$.

| | Question | Réponse attendue |
|---|---|---|
| a | les carrés des distances $\lVert\mathbf{x}_1 - \mathbf{x}_2\rVert^2$, $\lVert\mathbf{x}_1 - \mathbf{x}_3\rVert^2$, $\lVert\mathbf{x}_2 - \mathbf{x}_3\rVert^2$ | une liste de 3 nombres |
| b | $k(\mathbf{x}_1, \mathbf{x}_2)$ | un nombre (4 décimales) |
| c | la matrice de Gram $\mathbf{K}$ | une matrice 3 × 3 (4 décimales) |
| d | $\det\mathbf{K}$ | un nombre (4 décimales) |
| e | la distance $\lVert\varphi(\mathbf{x}_1) - \varphi(\mathbf{x}_2)\rVert$ dans l'espace des features | un nombre (4 décimales) |
| f | $\ln k(\mathbf{x}_1, \mathbf{x}_2)$ pour $\gamma = 2$ | un nombre |
| g | le rang de la matrice limite quand $\gamma \to 0$ | un entier |
| h | le rang de la matrice limite quand $\gamma \to +\infty$ | un entier |

Dans ta copie : que dit d) de la matrice $\mathbf{K}$ ? Pourquoi les distances dans l'espace des features sont-elles toutes inférieures à $\sqrt{2}$ ? Qu'est-ce qu'une SVM peut apprendre avec la matrice limite de g), et avec celle de h) ?

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M13b.14 — Au point optimal sous une contrainte d'égalité, ∇f est colinéaire à ∇g ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer la condition de Lagrange en dimension 2, à l'aide d'une courbe tracée dans la contrainte et de la règle de la chaîne.
**Prérequis :** fiche §1 ; M05b.12 · **Parcours :** C

$f$ et $g$ sont deux fonctions de $\mathbb{R}^2$ dans $\mathbb{R}$, à dérivées partielles continues. $\mathbf{x}^*$ est un minimum de $f$ sur la courbe $\{g = 0\}$, et $\nabla g(\mathbf{x}^*) \ne \mathbf{0}$. On admet qu'il existe une courbe dérivable $t \mapsto \mathbf{c}(t)$, définie près de $t = 0$, avec $\mathbf{c}(0) = \mathbf{x}^*$, $g(\mathbf{c}(t)) = 0$ pour tout $t$ et $\mathbf{c}'(0) \ne \mathbf{0}$.
1. Dérive $t \mapsto g(\mathbf{c}(t))$ en $t = 0$ : que vaut $\nabla g(\mathbf{x}^*) \cdot \mathbf{c}'(0)$ ?
2. Pourquoi la fonction $t \mapsto f(\mathbf{c}(t))$ a-t-elle un minimum en $t = 0$ ? Déduis-en $\nabla f(\mathbf{x}^*) \cdot \mathbf{c}'(0) = 0$.
3. En dimension 2, deux vecteurs orthogonaux au même vecteur non nul sont colinéaires : conclus qu'il existe $\lambda$ avec $\nabla f(\mathbf{x}^*) + \lambda\nabla g(\mathbf{x}^*) = \mathbf{0}$.
4. Où as-tu utilisé $\nabla g(\mathbf{x}^*) \ne \mathbf{0}$ ? Donne un exemple de contrainte où il s'annule et où la conclusion tombe.
5. En dimension $n$ avec une contrainte, la même idée marche avec toutes les courbes de la contrainte qui passent par $\mathbf{x}^*$ : que dit-elle alors de $\nabla f(\mathbf{x}^*)$ ?

### Ex M13b.15 — La dualité faible : la fonction duale minore le minimum du primal ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer la dualité faible et la concavité de la fonction duale.
**Prérequis :** fiche §4 · **Parcours :** C, E

Problème : $\min f(\mathbf{x})$ sous $g_i(\mathbf{x}) \le 0$ ($i = 1, \ldots, m$) et $h_j(\mathbf{x}) = 0$ ($j = 1, \ldots, r$) ; lagrangien $\mathcal{L}$ et fonction duale $D(\boldsymbol{\mu}, \boldsymbol{\lambda}) = \inf_{\mathbf{x}} \mathcal{L}(\mathbf{x}, \boldsymbol{\mu}, \boldsymbol{\lambda})$.
1. Soit $\mathbf{x}$ admissible et $\boldsymbol{\mu} \ge \mathbf{0}$. Montre que $\mathcal{L}(\mathbf{x}, \boldsymbol{\mu}, \boldsymbol{\lambda}) \le f(\mathbf{x})$.
2. Déduis-en $D(\boldsymbol{\mu}, \boldsymbol{\lambda}) \le f(\mathbf{x})$, puis $\sup D \le \inf f$ (sur les points admissibles).
3. Montre que $D$ est concave : pour $\theta \in [0, 1]$, compare $D$ en une combinaison convexe de deux jeux de multiplicateurs à la combinaison des valeurs (écris $\mathcal{L}$ comme une fonction affine des multiplicateurs).
4. Pourquoi exige-t-on $\boldsymbol{\mu} \ge \mathbf{0}$ mais rien sur $\boldsymbol{\lambda}$ ?
5. Un $\mathbf{x}$ admissible et des multiplicateurs avec $f(\mathbf{x}) = D(\boldsymbol{\mu}, \boldsymbol{\lambda})$ : montre que $\mathbf{x}$ est un minimum et que les multiplicateurs maximisent $D$.

### Ex M13b.16 — Pour un problème convexe, un minimum local est global ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer que, pour un problème convexe, tout minimum local est global, et que la stricte convexité donne l'unicité.
**Prérequis :** fiche §5 ; M10 · **Parcours :** C, E

$K$ est un ensemble convexe, $f$ une fonction convexe sur $K$. $\mathbf{x}^* \in K$ est un minimum **local** : il existe $r > 0$ tel que $f(\mathbf{x}^*) \le f(\mathbf{x})$ pour tout $\mathbf{x} \in K$ avec $\lVert\mathbf{x} - \mathbf{x}^*\rVert < r$.
1. Supposons qu'un $\mathbf{y} \in K$ vérifie $f(\mathbf{y}) < f(\mathbf{x}^*)$. Pourquoi les points $\mathbf{x}_\theta = (1 - \theta)\mathbf{x}^* + \theta\mathbf{y}$, $\theta \in\ ]0, 1]$, sont-ils dans $K$ ?
2. Montre que $f(\mathbf{x}_\theta) < f(\mathbf{x}^*)$ pour tout $\theta \in\ ]0, 1]$.
3. Choisis $\theta$ pour que $\lVert\mathbf{x}_\theta - \mathbf{x}^*\rVert < r$, et conclus.
4. Si $f$ est strictement convexe, montre que deux minima $\mathbf{x}^*$ et $\mathbf{y}^*$ sont égaux (regarde leur milieu).
5. Pourquoi l'ensemble admissible d'un problème convexe (§5) est-il convexe ? Et que deviennent 1 à 3 si l'on maximise une fonction convexe ?

### Ex M13b.17 — Maximiser la marge revient à minimiser ½ ‖w‖² ∂ ★★ ⏱️ 20 min
**Objectif :** passer du problème « plus grande marge » au problème quadratique de la SVM, et en tirer l'unicité de $\mathbf{w}$ et la présence de vecteurs de support des deux classes.
**Prérequis :** fiche §6 ; ∂ M10.8 · **Parcours :** C, E

Les données sont séparables. Pour un séparateur $(\mathbf{w}, b)$, $\mathbf{w} \ne \mathbf{0}$, la marge est $\rho(\mathbf{w}, b) = \min_i \frac{y_i(\mathbf{w} \cdot \mathbf{x}_i + b)}{\lVert\mathbf{w}\rVert}$.
1. M10.8 a montré que maximiser $\rho$ revient à minimiser $\lVert\mathbf{w}\rVert$ sous $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1$. Rappelle l'argument en deux lignes (invariance d'échelle, forme canonique).
2. Montre que minimiser $\lVert\mathbf{w}\rVert$ ou $\frac{1}{2}\lVert\mathbf{w}\rVert^2$ sous les mêmes contraintes donne les mêmes solutions.
3. Montre que $\frac{1}{2}\lVert\mathbf{w}\rVert^2$ est strictement convexe en $\mathbf{w}$, et que l'ensemble admissible en $(\mathbf{w}, b)$ est convexe. Déduis-en que $\mathbf{w}$ est unique.
4. À l'optimum, montre qu'au moins un exemple de **chaque** classe vérifie $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) = 1$ (sinon, déplace $b$, puis réduis $\lVert\mathbf{w}\rVert$).
5. Déduis de 4 que $b$ est unique lui aussi.

### Ex M13b.18 — Marge souple : la formulation avec des variables d'écart et celle avec la hinge loss sont équivalentes ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer que le problème de la marge souple avec variables d'écart est le même que la minimisation de l'objectif avec la hinge loss, et regarder la limite $C \to \infty$.
**Prérequis :** fiche §7 · **Parcours :** C

Problème (P) : $\min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2}\lVert\mathbf{w}\rVert^2 + C\sum_i \xi_i$ sous $y_i(\mathbf{w} \cdot \mathbf{x}_i + b) \ge 1 - \xi_i$ et $\xi_i \ge 0$. Problème (H) : $\min_{\mathbf{w}, b} J(\mathbf{w}, b)$, avec la hinge.
1. À $(\mathbf{w}, b)$ fixés, quelles valeurs de $\xi_i$ sont admissibles ? Montre que la plus petite est $\max(0, 1 - y_i(\mathbf{w} \cdot \mathbf{x}_i + b))$.
2. Déduis-en que, à $(\mathbf{w}, b)$ fixés, le minimum de l'objectif de (P) en $\boldsymbol{\xi}$ est $J(\mathbf{w}, b)$.
3. Conclus : (P) et (H) ont la même valeur optimale, et les mêmes $(\mathbf{w}, b)$ optimaux.
4. Données séparables : montre que l'objectif optimal de (P) est au plus $\frac{1}{2}\lVert\mathbf{w}_{\mathrm{dure}}\rVert^2$, où $\mathbf{w}_{\mathrm{dure}}$ est la solution de la marge dure.
5. Déduis de 4 que $\sum_i \xi_i \le \frac{\lVert\mathbf{w}_{\mathrm{dure}}\rVert^2}{2C}$ à l'optimum : que devient la somme des écarts quand $C \to \infty$ ?

### Ex M13b.19 — La somme et le produit de deux noyaux sont des noyaux ; une matrice de Gram est semi-définie positive ∂ ★★★ ⏱️ 25 min
**Objectif :** démontrer qu'une matrice de Gram de noyau est semi-définie positive, et construire de nouveaux noyaux par somme, produit et multiplication par une constante.
**Prérequis :** fiche §8 ; M12c.17 · **Parcours :** C

Un noyau est une fonction $k(\mathbf{x}, \mathbf{z}) = \varphi(\mathbf{x}) \cdot \varphi(\mathbf{z})$ pour une application $\varphi$ à valeurs dans un $\mathbb{R}^q$.
1. Pour des points $\mathbf{x}_1, \ldots, \mathbf{x}_n$ et un vecteur $\mathbf{v} \in \mathbb{R}^n$, montre que $\mathbf{v}^\top\mathbf{K}\mathbf{v} = \lVert\sum_i v_i\,\varphi(\mathbf{x}_i)\rVert^2$. Conclus. (Compare avec M12c.17.)
2. Soit $c > 0$ et $k$ un noyau. Montre que $c\,k$ est un noyau (donne sa fonction $\varphi$).
3. Soient $k_1$ et $k_2$ des noyaux, de fonctions $\varphi_1 : \mathbb{R}^p \to \mathbb{R}^{q_1}$ et $\varphi_2 : \mathbb{R}^p \to \mathbb{R}^{q_2}$. Montre que $k_1 + k_2$ est un noyau (empile les deux vecteurs).
4. Montre que $k_1 k_2$ est un noyau, de fonction $\varphi$ à $q_1 q_2$ coordonnées $\varphi_{1,a}(\mathbf{x})\,\varphi_{2,b}(\mathbf{x})$.
5. Déduis de 2 à 4, sans écrire $\varphi$, que $(\mathbf{x} \cdot \mathbf{z} + c)^d$ est un noyau pour $c \ge 0$ et $d \ge 1$ entier (le noyau constant égal à 1 en est un, de $\varphi \equiv 1$).
6. Montre que $k(\mathbf{x}, \mathbf{z}) = \lVert\mathbf{x} - \mathbf{z}\rVert^2$ n'est pas un noyau.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M13b.20 — Pont : la décision d'une SVM à noyau, une somme pondérée sur les vecteurs de support 🔗 ★ ⏱️ 15 min
**Objectif :** calculer la décision d'une SVM à noyau RBF à partir de ses vecteurs de support, comme le fera une SVM entraînée avec scikit-learn.
**Prérequis :** fiche §8 · **Parcours :** C, E

Une SVM à noyau RBF, $\gamma = 0{,}3$, a trois vecteurs de support : $(-1, 1)$ de label $+1$ et $\alpha = 0{,}8$ ; $(2, -1)$ de label $-1$ et $\alpha = 0{,}5$ ; $(1, 3)$ de label $-1$ et $\alpha = 0{,}3$. Son biais vaut $b = -0{,}1$. La décision est $s(\mathbf{x}) = \sum_i \alpha_i y_i\,k(\mathbf{x}_i, \mathbf{x}) + b$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\sum_i \alpha_i y_i$ | un nombre |
| b | $s(0{,}5 ;\ 0{,}5)$ | un nombre (4 décimales) |
| c | la classe prédite pour $(0{,}5 ;\ 0{,}5)$ | un entier ($-1$ ou $+1$) |
| d | $s(2, 4)$ | un nombre (4 décimales) |
| e | la limite de $s(\mathbf{x})$ quand $\mathbf{x}$ s'éloigne à l'infini | un nombre |
| f | le nombre d'évaluations du noyau pour une prédiction | un entier |

Dans ta copie : pourquoi la condition a) est-elle nécessaire ? Que prédit cette SVM loin de tous les vecteurs de support, et pourquoi ? Si l'on entraînait sur dix fois plus d'exemples, qu'est-ce qui déciderait du coût d'une prédiction ?

### Ex M13b.21 — MML §7.2 et §7.3 : Lagrange, dualité et optimisation convexe, en anglais 📖 ★★ ⏱️ 40 min
**Objectif :** lire en anglais les sections du livre sur l'optimisation sous contraintes et l'optimisation convexe, relier ses notations à la fiche, et refaire un de ses calculs.
**Prérequis :** fiche §1 à §5 · **Parcours :** C

Lis MML §7.2 et §7.3 (le §7.3.3 se survole). Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Le livre écrit d'abord le problème avec une fonction indicatrice : laquelle, et que vaut-elle ? En quoi le lagrangien en est-il une version « relâchée » ?
2. Quelle inégalité générale, entre un max d'un min et un min d'un max, le livre utilise-t-il pour démontrer la dualité faible ? Relie-la à ∂ M13b.15.
3. Comment le livre traite-t-il les contraintes d'égalité ? Pourquoi leurs multiplicateurs ne sont-ils pas contraints en signe ?
4. Quelle définition le livre donne-t-il d'un problème convexe, et quelles caractérisations d'une fonction convexe dérivable (une, puis deux fois) ? Compare avec la fiche §5.
5. Le §7.3.2 écrit le dual d'un programme quadratique : refais le calcul sur l'exemple de M13b.6, et vérifie que tu retrouves $D(\mu)$.
6. Trois mots anglais de ces sections, avec leur traduction.

### Ex M13b.22 — MML §12.2 à §12.5 : marge, primal, dual et noyaux (§12.1 a été lu en M10) 📖 ★★ ⏱️ 50 min
**Objectif :** lire en anglais le chapitre du livre sur les SVM, relier ses notations à la fiche, et y repérer ce que la fiche a démontré autrement.
**Prérequis :** fiche §6 à §8 · **Parcours :** C

Lis MML §12.2 à §12.5. Réponds dans ta copie, **avec tes mots**.
1. Quelle lettre le livre utilise-t-il pour la marge ? Quelles normalisations compare-t-il : celle du §12.2.1 et celle de sa « dérivation traditionnelle » (§12.2.2) ? Pourquoi donnent-elles les mêmes solutions (§12.2.3) ?
2. Le §12.2.4 décrit la marge souple géométriquement, le §12.2.5 par une loss : quelles sont ces deux descriptions, et laquelle correspond à ∂ M13b.18 ?
3. Au §12.3.1, quelles conditions de stationnarité le livre obtient-il, et quel problème dual ? Compare avec la fiche §8 (signes, borne $C$).
4. Le §12.3.2 donne une lecture du dual par les enveloppes convexes : laquelle ? Relie-la au théorème de la plus grande marge de M10.
5. Que dit le §12.4 des noyaux, et quel exemple de noyau donne-t-il ? Le §12.5 : quelles méthodes de résolution cite-t-il ?
6. Trois mots anglais du chapitre, avec leur traduction.

### Ex M13b.23 — Fermi : la taille de la matrice de Gram d'une SVM à noyau sur 100 000 exemples 🧮 ★ ⏱️ 10 min
**Objectif :** estimer la mémoire et le temps que demande la matrice de Gram d'une SVM à noyau, et en tirer la taille de dataset au-delà de laquelle elle devient impraticable.
**Prérequis :** fiche §8 · **Parcours :** C

Une SVM à noyau RBF sur $n = 100\,000$ exemples de $p = 50$ features.
1. Combien de nombres dans la matrice de Gram ? Combien en faut-il vraiment, par symétrie ?
2. Combien d'octets en `float64` pour la matrice entière ? Et en `float32` ? Compare à la mémoire vive d'un ordinateur portable (16 Go).
3. Combien d'opérations pour calculer toutes les distances au carré ? À $10^9$ opérations par seconde, combien de temps ?
4. `sklearn.svm.SVC` garde par défaut un cache de 200 Mo pour les valeurs du noyau, stockées en `float32` : quelle fraction de la matrice tient dedans ?
5. Pour quel $n$ la matrice entière en `float64` tiendrait-elle dans 16 Go ? Conclus sur les SVM à noyau et les très gros datasets.

### Ex M13b.24 — Expliquer un multiplicateur de Lagrange comme un prix 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, à quelqu'un qui sait ce qu'est un minimum mais pas un multiplicateur, ce que mesure un multiplicateur de Lagrange.
**Prérequis :** fiche §1, §3 et §4 · **Parcours :** C, E

Un ami qui gère le budget d'une petite entreprise te demande : « Dans tes calculs d'optimisation, c'est quoi ce lambda qu'on ajoute ? » Réponds-lui en 6 à 10 phrases, sans formule, en t'appuyant sur trois idées : une contrainte qui coûte (on ferait mieux sans elle), ce que l'on gagnerait à la desserrer d'une unité (le multiplicateur), et le cas d'une contrainte qui ne gêne pas (prix nul). Donne un exemple chiffré avec un budget. Ajoute une phrase sur le lien entre une contrainte et une pénalité. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

### M13b.E1 — « Qu'est-ce qu'un problème d'optimisation convexe, et pourquoi est-ce une bonne nouvelle ? » 💼 ★ ⏱️ 10 min
*Fiche §5 · parcours C*

« Qu'est-ce qu'un problème d'optimisation convexe, et pourquoi est-ce une bonne nouvelle ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit définir un problème convexe (objectif, inégalités, égalités), dire ce que cela garantit (minimum local égal au minimum global, unicité si la convexité est stricte, conditions KKT suffisantes, dualité forte sous une condition de Slater), citer deux exemples du machine learning (la régression ridge, la SVM) et un contre-exemple, et dire ce que l'on fait quand le problème ne l'est pas. Compare ensuite avec la réponse modèle de `05_solutions.md`.

### M13b.E2 — « Hinge loss ou log-loss : quelles différences ? » 💼 ★ ⏱️ 10 min
*Fiche §7 · parcours C*

« Hinge loss ou log-loss : quelles différences ? »

Prépare une réponse orale de **60 secondes**. Elle doit écrire les deux losses comme des fonctions de la marge $y\,s$, dire ce qu'elles ont en commun (convexes, majorent l'erreur après mise à l'échelle), puis trois différences : la dérivabilité, la valeur au-delà de la marge (exactement 0 ou jamais 0) et ce qu'elle entraîne (des vecteurs de support peu nombreux, ou tous les exemples qui comptent), et ce que le modèle donne en sortie (un score ou une probabilité). Termine par un critère de choix. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m13b_lagrange_svm/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M13b.25 | Un problème quadratique sous contraintes d'égalité, par le système de Lagrange · `lagrange_equality_qp` | 🔨 | ★ | 20 | C, E |
| M13b.26 | La hinge loss et un sous-gradient de l'objectif d'une SVM linéaire · `hinge_loss, svm_subgradient` | 🔨 | ★★ | 25 | C, E |
| M13b.27 | Les noyaux RBF et polynomial · `rbf_kernel, polynomial_kernel` | 🔨 | ★ | 20 | C, E |
| M13b.28 | `scipy.optimize.minimize` sous contraintes et les noyaux de scikit-learn contre tes fonctions | 📦 | ★ | 15 | C, E |
| M13b.29 | Prédire : comment change le minimum quand on relâche la contrainte, et ce que dit λ | 🔮 | ★ | 10 | C, E |
| M13b.30 | La descente de sous-gradient sur la hinge loss : pas constant contre pas décroissant | 🔬 | ★★ | 20 | C |
| M13b.31 | Lignes de niveau et contrainte : voir le point de Lagrange | 🎨 | ★ | 20 | C, E |
| M13b.32 | Chasse à l'erreur : le signe d'un multiplicateur, une largeur de bande 1/‖w‖ au lieu de 2/‖w‖, une matrice de Gram non symétrique | 🐛 | ★ | 15 | C |
| M13b.33 | Vérifier une solution KKT : faisabilité, stationnarité, complémentarité | 🛠️ | ★ | 15 | C |
| M13b.34 | Défi : une SVM linéaire entraînée par sous-gradient, un objectif à 1 % de celui de scikit-learn au même C | 🏆 | ★★★ | 30 | C |
