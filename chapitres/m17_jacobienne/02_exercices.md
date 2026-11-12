# M17 · Jacobienne et règle de la chaîne — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m17_jacobienne/06_mes_reponses.md` (créée par `python tools/start_chapter.py M17`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [📖 🗣️ Lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, comme dans la fiche : la jacobienne d'une application de $\mathbb{R}^n$ dans $\mathbb{R}^m$ a la forme $(m, n)$, **une ligne par sortie et une colonne par entrée**, $J_{ij} = \frac{\partial f_i}{\partial x_j}$ ; dans ses formules, les vecteurs sont des colonnes ; un gradient est une ligne chez MML et a la forme de la variable dans NumPy. Les angles sont en radians. Une matrice s'écrit dans le notebook comme une liste de ses **lignes**.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M17.Q1 — La forme d'une jacobienne 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. Quelle est la forme de la jacobienne d'une application de $\mathbb{R}^5$ dans $\mathbb{R}^3$ ?
2. Vrai ou faux : la ligne 2 de la jacobienne est le gradient de la deuxième sortie.
3. Quelle est la jacobienne de $\mathbf{x} \mapsto \mathbf{A}\mathbf{x} + \mathbf{b}$, avec $\mathbf{A}$ de forme $(3, 5)$ ? Et celle de $\mathbf{x} \mapsto \mathbf{x}\mathbf{W}$, en lignes, avec $\mathbf{W}$ de forme $(5, 3)$ ?
4. Une application de $\mathbb{R}$ dans $\mathbb{R}^4$ décrit la trajectoire d'un point : quelle est la forme de sa jacobienne, et comment s'appelle-t-elle en physique ?
5. Combien d'évaluations de $\mathbf{f}$ demande la jacobienne entière par différences centrées, pour $n = 5$ et $m = 3$ ?
6. Vrai ou faux : si $\det\mathbf{J}_{\mathbf{f}}(\mathbf{x}) = 0{,}5$, $\mathbf{f}$ divise environ par deux l'aire des petites figures autour de $\mathbf{x}$.

### M17.Q2 — Diagonale ou pleine ? 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

Pour chaque application de $\mathbb{R}^4$ dans $\mathbb{R}^4$, dis si sa jacobienne est diagonale (en tout point), triangulaire sans être diagonale, ou pleine (en un point quelconque).

1. $\mathbf{x} \mapsto e^{\mathbf{x}}$ (coordonnée par coordonnée).
2. $\mathbf{x} \mapsto \mathbf{x} \odot \mathbf{x}$.
3. $\mathbf{x} \mapsto (x_1,\ x_1 + x_2,\ x_1 + x_2 + x_3,\ x_1 + x_2 + x_3 + x_4)$, les sommes cumulées.
4. $\mathbf{x} \mapsto \mathbf{x}/\lVert\mathbf{x}\rVert$.
5. $\mathbf{x} \mapsto \mathbf{D}\mathbf{x}$, avec $\mathbf{D}$ diagonale.
6. Vrai ou faux : pour une application coordonnée par coordonnée, $\mathbf{J}\mathbf{v}$ se calcule avec $n$ multiplications.

### M17.Q3 — Dans quel ordre multiplier les jacobiennes ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

$\mathbf{f} : \mathbb{R}^2 \to \mathbb{R}^5$ et $\mathbf{g} : \mathbb{R}^5 \to \mathbb{R}^3$.

1. Quelle est la forme de $\mathbf{J}_{\mathbf{f}}$ ? De $\mathbf{J}_{\mathbf{g}}$ ? De $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}$ ?
2. Écris $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{x})$ en précisant où chaque jacobienne est évaluée.
3. Le produit $\mathbf{J}_{\mathbf{f}}\mathbf{J}_{\mathbf{g}}$ existe-t-il ?
4. Vrai ou faux : pour $f$, $g$ de $\mathbb{R}$ dans $\mathbb{R}$, la règle de la chaîne de R7 est un cas particulier de celle-ci.
5. Vrai ou faux : $\frac{\partial(\mathbf{g} \circ \mathbf{f})_i}{\partial x_j}$ est une somme de 5 produits.
6. Vrai ou faux : si $\mathbf{f}$ et $\mathbf{g}$ vont de $\mathbb{R}^3$ dans $\mathbb{R}^3$, $\mathbf{J}_{\mathbf{f}}\mathbf{J}_{\mathbf{g}}$ est aussi la jacobienne de $\mathbf{g} \circ \mathbf{f}$.

### M17.Q4 — Gradient en ligne ou de la forme de la variable 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

$L : \mathbb{R}^3 \to \mathbb{R}$, $\mathbf{f} : \mathbb{R}^4 \to \mathbb{R}^3$.

1. Quelle est la forme du gradient de $L$ chez MML ? Dans NumPy ?
2. Écris $\nabla_{\mathbf{x}}(L \circ \mathbf{f})$ en ligne, puis en colonne.
3. Quelle est la forme de $\nabla_{\mathbf{x}}(L \circ \mathbf{f})$ dans NumPy ?
4. Vrai ou faux : $\mathbf{J}_{\mathbf{f}}\,\nabla_{\mathbf{y}}L$ est le gradient de $L \circ \mathbf{f}$ en convention colonne.
5. Une fonction réelle d'une matrice $\mathbf{M}$ de forme $(4, 2)$ : quelle est la forme de son gradient dans NumPy ?
6. Vrai ou faux : les deux conventions donnent les mêmes nombres.

### M17.Q5 — Jacobienne-vecteur ou vecteur-jacobienne : combien d'opérations ? 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C*

1. $\mathbf{f}$ va de $\mathbb{R}^{1\,000}$ dans $\mathbb{R}$ : combien de produits jacobienne-vecteur faut-il pour avoir son gradient ? Combien de produits vecteur-jacobienne ?
2. Et pour une application de $\mathbb{R}$ dans $\mathbb{R}^{1\,000}$ ?
3. Par différences centrées, combien d'évaluations de $\mathbf{f}$ coûte $\mathbf{J}\mathbf{v}$, pour $n = 1\,000$ ?
4. $\mathbf{J}_1$, $\mathbf{J}_2$ sont $500 \times 500$ et $\mathbf{v}$ a 500 coordonnées : combien de multiplications coûte $\mathbf{J}_2(\mathbf{J}_1\mathbf{v})$ ? Et $(\mathbf{J}_2\mathbf{J}_1)\mathbf{v}$ ?
5. Vrai ou faux : $\mathbf{u}^\top\mathbf{J}$ est le gradient de $\mathbf{x} \mapsto \mathbf{u} \cdot \mathbf{f}(\mathbf{x})$.
6. Vrai ou faux : la jacobienne entière peut se calculer colonne par colonne avec $n$ produits jacobienne-vecteur.

### M17.Q6 — La loi de Boltzmann : populations relatives et énergie moyenne 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

Un système a trois niveaux d'énergies $0$, $1$ et $3$.

1. À la température $T = 1$, que vaut le rapport $\frac{p_3}{p_2}$ des populations des niveaux d'énergies 3 et 1 ?
2. À $T = 1$, que vaut la fonction de partition $Z$ (3 décimales) ?
3. Vers quoi tend l'énergie moyenne quand $T \to 0$ ? Quand $T \to \infty$ ?
4. À quelle température le niveau d'énergie 3 est-il 100 fois moins peuplé que le niveau d'énergie 0 ?
5. On ajoute un quatrième état, d'énergie 1 lui aussi : vrai ou faux, il a toujours la même population que l'autre état d'énergie 1.
6. Vrai ou faux : $\operatorname{diag}(\mathbf{p}) - \mathbf{p}^\top\mathbf{p}$ est inversible.

<a id="rappels"></a>

## 🔁 Rappels

### M17.R1 — Dérivées partielles et gradient (M05b) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

$f(x, y) = x^2y - 3y + 1$.

1. $\frac{\partial f}{\partial x}$ et $\frac{\partial f}{\partial y}$ ?
2. Le gradient de $f$ en $(1, 2)$, en ligne ?
3. La dérivée directionnelle de $f$ en $(1, 2)$ dans la direction $(0{,}6 ;\ 0{,}8)$ ?
4. Dans quelle direction $f$ croît-elle le plus vite en $(1, 2)$ ?
5. Une valeur approchée de $f(1{,}1 ;\ 1{,}9)$ par l'approximation linéaire ?

### M17.R2 — La règle de la chaîne en une variable (R7) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. La dérivée de $x \mapsto \sin(x^2)$ ?
2. La dérivée de $x \mapsto e^{\cos x}$ ?
3. La dérivée de $x \mapsto \ln(1 + x^4)$ ?
4. La dérivée de $x \mapsto \sqrt{1 + \sin^2 x}$, une composée de trois fonctions ?
5. La dérivée de $h = g \circ f$ en 2, avec $f(2) = 5$, $f'(2) = -1$, $g'(2) = 4$, $g'(5) = 3$ ?

### M17.R3 — La matrice de covariance (M02c) 🔁 ★ ⏱️ 5 min
*Fiche §7 · parcours C*

$\mathbf{X} = (X_1, X_2)$ a la matrice de covariance $\boldsymbol{\Sigma} = \begin{pmatrix} 4 & -1 \\ -1 & 2 \end{pmatrix}$.

1. $\mathbb{V}(X_1 + X_2)$ ? $\mathbb{V}(X_1 - X_2)$ ?
2. Pour une ligne $\mathbf{v}$, comment s'écrit $\mathbb{V}(\mathbf{v} \cdot \mathbf{X})$ avec $\boldsymbol{\Sigma}$ ?
3. Pourquoi une matrice de covariance est-elle semi-définie positive ?
4. Pour une autre matrice de covariance $\boldsymbol{\Sigma}'$, celle d'un vecteur $(X_1, X_2)$ dont la somme $X_1 + X_2$ est constante, que vaut $\boldsymbol{\Sigma}'\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ ? Est-ce possible pour la matrice $\boldsymbol{\Sigma}$ ci-dessus ?
5. Une matrice de covariance est-elle toujours symétrique ? Toujours inversible ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une liste entre crochets, comme `[0.2, -1]` ;
- une matrice comme la liste de ses lignes, comme `[[1, 0], [-2, 3]]` ;
- une fraction entre guillemets, comme `"3/7"`, quand la question le dit.

### Ex M17.1 — La jacobienne des coordonnées polaires, son déterminant, et l'approximation linéaire près d'un point ✏️ ★ ⏱️ 15 min
**Objectif :** calculer une jacobienne, son déterminant, et s'en servir comme approximation linéaire.
**Prérequis :** fiche §1 ; M05b · **Parcours :** C, E

$\mathbf{f}(r, \theta) = (r\cos\theta,\ r\sin\theta)$, au point $(r, \theta) = (4, \frac{\pi}{6})$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{f}(4, \frac{\pi}{6})$ | une liste de 2 nombres (4 décimales) |
| b | la jacobienne $\mathbf{J}_{\mathbf{f}}(4, \frac{\pi}{6})$ | une matrice (4 décimales) |
| c | son déterminant | un nombre |
| d | l'approximation linéaire de $\mathbf{f}(4{,}1 ;\ \frac{\pi}{6} + 0{,}05)$ | une liste de 2 nombres (4 décimales) |
| e | la valeur exacte de $\mathbf{f}(4{,}1 ;\ \frac{\pi}{6} + 0{,}05)$ | une liste de 2 nombres (4 décimales) |
| f | la distance entre d) et e) | un nombre (4 décimales) |
| g | l'aire de l'image du petit rectangle $[4 ;\ 4{,}01] \times [\frac{\pi}{6} ;\ \frac{\pi}{6} + 0{,}02]$, approchée par le déterminant | un nombre (4 décimales) |

Dans ta copie : écris $\mathbf{J}_{\mathbf{f}}(r, \theta)$ en général, et montre que $\det\mathbf{J}_{\mathbf{f}}(r, \theta) = r$. Pourquoi la deuxième colonne a-t-elle la longueur $r$, et la première la longueur 1 (que fait le point quand $\theta$ bouge, puis quand $r$ bouge) ? Pourquoi l'erreur f) est-elle bien plus petite que les déplacements $0{,}1$ et $0{,}05$ ?

### Ex M17.2 — Une fonction appliquée coordonnée par coordonnée : la jacobienne diagonale, et son produit par un vecteur ✏️ ★ ⏱️ 15 min
**Objectif :** écrire la jacobienne diagonale d'une fonction appliquée coordonnée par coordonnée, et son produit par un vecteur.
**Prérequis :** fiche §2 ; M09a · **Parcours :** C, E

$g(t) = \ln(1 + t^2)$, appliquée coordonnée par coordonnée : $\mathbf{f}(\mathbf{x}) = g(\mathbf{x})$, en $\mathbf{x} = (1, -2, 0, 3)$.

| | Question | Réponse attendue |
|---|---|---|
| a | la diagonale de $\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ | une liste de 4 nombres |
| b | $\mathbf{J}_{\mathbf{f}}(\mathbf{x})\,\mathbf{v}$ pour $\mathbf{v} = (2, 1, -5, 0{,}5)$ | une liste de 4 nombres |
| c | le nombre de coefficients nuls de $\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ | un entier |
| d | pour la même fonction sur $n = 1\,000$ coordonnées, le nombre de coefficients **hors** de la diagonale | un entier |
| e | le nombre d'évaluations de $\mathbf{f}$ pour la diagonale, puis pour la jacobienne entière, par différences centrées, pour $n = 1\,000$ | une liste de 2 entiers |
| f | la diagonale de la jacobienne de $\mathbf{x} \mapsto \mathbf{x} \odot g(\mathbf{x})$ en $\mathbf{x}$ | une liste de 4 nombres (3 décimales) |

Dans ta copie : pourquoi le coefficient $(2, 3)$ de $\mathbf{J}_{\mathbf{f}}$ est-il nul ? Pourquoi un coefficient de la diagonale est-il nul lui aussi, et que dit-il de $g$ en ce point ? Pourquoi f) est-elle encore une jacobienne diagonale ?

### Ex M17.3 — Dériver une composée de trois applications par le produit de leurs jacobiennes ✏️ ★★ ⏱️ 20 min
**Objectif :** dériver une composée de trois applications par le produit de leurs jacobiennes, chacune évaluée au bon point.
**Prérequis :** fiche §3 · **Parcours :** C, E

$\mathbf{f}_1(x, y) = (x + y,\ xy,\ x - y)$ de $\mathbb{R}^2$ dans $\mathbb{R}^3$ ; $\mathbf{f}_2(u, v, w) = (uv,\ v + w^2)$ de $\mathbb{R}^3$ dans $\mathbb{R}^2$ ; $f_3(a, b) = a^2 - 3b$ de $\mathbb{R}^2$ dans $\mathbb{R}$. $h = f_3 \circ \mathbf{f}_2 \circ \mathbf{f}_1$, au point $(x, y) = (1, 2)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{f}_1(1, 2)$ | une liste de 3 nombres |
| b | $\mathbf{J}_{\mathbf{f}_1}(1, 2)$ | une matrice |
| c | $\mathbf{J}_{\mathbf{f}_2}$ au point où on l'applique | une matrice |
| d | $\mathbf{J}_{f_3}$ au point où on l'applique | une matrice (une ligne : `[[a, b]]`) |
| e | le gradient de $h$ en $(1, 2)$, en ligne | une liste de 2 nombres |
| f | le nombre de multiplications pour $(\mathbf{J}_{f_3}\mathbf{J}_{\mathbf{f}_2})\mathbf{J}_{\mathbf{f}_1}$, puis pour $\mathbf{J}_{f_3}(\mathbf{J}_{\mathbf{f}_2}\mathbf{J}_{\mathbf{f}_1})$ | une liste de 2 entiers |

Dans ta copie : écris les formes des trois jacobiennes et vérifie qu'elles s'enchaînent. Vérifie e) en écrivant $h(x, y)$ et en dérivant directement. Pourquoi le produit de gauche à droite est-il ici le moins cher ?

### Ex M17.4 — La normalisation x/‖x‖ : sa jacobienne (I − uuᵀ)/‖x‖, et la direction qu'elle écrase ✏️ ★★ ⏱️ 20 min
**Objectif :** dériver la normalisation, reconnaître la structure de sa jacobienne, et calculer un produit jacobienne-vecteur sans former la matrice.
**Prérequis :** fiche §3 et §5 ; M12b, M12c · **Parcours :** C

$\mathbf{n}(\mathbf{x}) = \frac{\mathbf{x}}{\lVert\mathbf{x}\rVert}$, de $\mathbb{R}^3 \setminus \{\mathbf{0}\}$ dans $\mathbb{R}^3$, et $\mathbf{u} = \mathbf{n}(\mathbf{x})$. On admet (à montrer dans ta copie) que $\mathbf{J}_{\mathbf{n}}(\mathbf{x}) = \frac{\mathbf{I} - \mathbf{u}\mathbf{u}^\top}{\lVert\mathbf{x}\rVert}$. Au point $\mathbf{x} = (3, 0, 4)$ :

| | Question | Réponse attendue |
|---|---|---|
| a | $\lVert\mathbf{x}\rVert$ et $\mathbf{u}$ | une liste de 4 nombres : $\lVert\mathbf{x}\rVert$, puis les 3 coordonnées de $\mathbf{u}$ |
| b | $\mathbf{J}_{\mathbf{n}}(\mathbf{x})$ | une matrice |
| c | $\mathbf{J}_{\mathbf{n}}(\mathbf{x})\,\mathbf{x}$ | une liste de 3 nombres |
| d | $\mathbf{J}_{\mathbf{n}}(\mathbf{x})\,\mathbf{v}$ pour $\mathbf{v} = (0, 2, 1)$, sans former la matrice : $\frac{\mathbf{v} - (\mathbf{u} \cdot \mathbf{v})\,\mathbf{u}}{\lVert\mathbf{x}\rVert}$ | une liste de 3 nombres |
| e | le rang de $\mathbf{J}_{\mathbf{n}}(\mathbf{x})$ | un entier |
| f | ses valeurs propres, dans l'ordre croissant | une liste de 3 nombres |

Dans ta copie : démontre la formule de $\mathbf{J}_{\mathbf{n}}$ (dérive $\frac{x_i}{\lVert\mathbf{x}\rVert}$ par rapport à $x_j$, avec $\frac{\partial\lVert\mathbf{x}\rVert}{\partial x_j} = \frac{x_j}{\lVert\mathbf{x}\rVert}$). Pourquoi c) est-il nul, sans calcul (que fait $\mathbf{n}$ le long de la droite de $\mathbf{x}$) ? Reconnais dans $\mathbf{I} - \mathbf{u}\mathbf{u}^\top$ une projection orthogonale (M12b) : sur quoi ? Déduis-en e) et f). Combien de multiplications coûte d), contre la matrice entière pour $n = 1\,000$ ?

### Ex M17.5 — Le gradient d'une fonction scalaire d'une composée, dans les deux conventions : J_fᵀ ∇L ✏️ ★ ⏱️ 15 min
**Objectif :** calculer le gradient d'une fonction réelle d'une composée en ligne et en colonne, et vérifier que les nombres sont les mêmes.
**Prérequis :** fiche §4 · **Parcours :** C, E

$\mathbf{f}(x_1, x_2) = (x_1 - x_2,\ x_1x_2,\ x_2^2)$ de $\mathbb{R}^2$ dans $\mathbb{R}^3$, et $L(y_1, y_2, y_3) = y_1^2 + 3y_2 - y_3$, au point $\mathbf{x} = (2, -1)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{y} = \mathbf{f}(\mathbf{x})$ | une liste de 3 nombres |
| b | $\nabla_{\mathbf{y}}L$ en $\mathbf{y}$ | une liste de 3 nombres |
| c | $\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ | une matrice |
| d | $\nabla_{\mathbf{x}}(L \circ \mathbf{f})$ | une liste de 2 nombres |
| e | la forme de $\mathbf{J}_{\mathbf{f}}^\top$ | une liste de 2 entiers |
| f | la dérivée en $t = 0$ de $t \mapsto (L \circ \mathbf{f})\big(\mathbf{x} + t\,(1, 1)\big)$ (sans normaliser $(1, 1)$) | un nombre |

Dans ta copie : calcule d) en ligne, $\nabla_{\mathbf{y}}L\,\mathbf{J}_{\mathbf{f}}$, puis en colonne, $\mathbf{J}_{\mathbf{f}}^\top\nabla_{\mathbf{y}}L$, et vérifie par la dérivation directe de $L(\mathbf{f}(\mathbf{x}))$. Pourquoi $\mathbf{J}_{\mathbf{f}}\,\nabla_{\mathbf{y}}L$ n'a-t-il pas de sens ici ?

### Ex M17.6 — Dérivées à gauche et à droite d'une fonction définie par morceaux, et la dérivée d'une composée de sept copies d'une fonction lisse ✏️ ★★ ⏱️ 15 min
**Objectif :** dériver une fonction affine par morceaux de chaque côté de ses coins, et une longue composition par le produit des dérivées.
**Prérequis :** fiche §6 ; R7 · **Parcours :** C, E

**Partie 1.** Une facture d'électricité (en €) en fonction de la consommation $x$ (en kWh) : $c(x) = 0{,}15\,x$ pour $x \le 100$ ; $15 + 0{,}25\,(x - 100)$ pour $100 \le x \le 300$ ; $65 + 0{,}1\,(x - 300)$ pour $x \ge 300$ (une remise au-delà de 300 kWh).

**Partie 2.** $g(x) = \frac{1}{1 + x}$, et $g^{\circ 7} = g \circ g \circ \cdots \circ g$ (sept copies). De $x_0 = 1$, $x_{k+1} = g(x_k)$.

| | Question | Réponse attendue |
|---|---|---|
| a | $c(320)$ | un nombre |
| b | les dérivées à gauche et à droite de $c$ en 100 | une liste de 2 nombres |
| c | les dérivées à gauche et à droite de $c$ en 300 | une liste de 2 nombres |
| d | les dérivées à gauche et à droite de $x \mapsto \lvert c(x) - 40\rvert$ au point où $c(x) = 40$ | une liste de 2 nombres |
| e | $x_7 = g^{\circ 7}(1)$ | une fraction entre guillemets (irréductible) |
| f | la dérivée de $g^{\circ 7}$ en 1 | une fraction entre guillemets (irréductible) |
| g | $\lvert g'(x^*)\rvert$, au point fixe $x^* > 0$ de $g$ | un nombre (3 décimales) |

Dans ta copie : $c$ est-elle continue ? Restreinte à $[0 ;\ 300]$, $c$ est convexe : quels sont ses sous-gradients en 100 (M13b) ? Pourquoi $c$, sur tout $[0 ;\ +\infty[$, n'est-elle pas convexe, et pourquoi n'a-t-elle aucun sous-gradient en 300 ? Pour f), écris le produit des sept dérivées $g'(x_k)$, avec les $x_k$ en fractions, et observe les simplifications. Comment le facteur g) explique-t-il l'ordre de grandeur de f) ?

### Ex M17.7 — Une loi de Boltzmann à quatre niveaux d'énergie : rapports de populations, énergie moyenne, et la température où le niveau fondamental garde la moitié ✏️ ★★ ⏱️ 15 min
**Objectif :** calculer une loi de Boltzmann, ses rapports de populations et son énergie moyenne, ses limites, et résoudre une équation en température.
**Prérequis :** fiche §7 ; R7 (dichotomie) · **Parcours :** C, E

Un atome a quatre niveaux d'énergies $0$, $1$, $2$ et $4$ (en unités où la constante de Boltzmann vaut 1).

| | Question | Réponse attendue |
|---|---|---|
| a | à $T = 1$, le rapport des populations des niveaux d'énergies 1 et 0 | un nombre (4 décimales) |
| b | à $T = 1$, la population du niveau fondamental (d'énergie 0) | un nombre (4 décimales) |
| c | à $T = 1$, l'énergie moyenne | un nombre (4 décimales) |
| d | les limites de l'énergie moyenne quand $T \to 0$, puis quand $T \to \infty$ | une liste de 2 nombres |
| e | la température où le niveau fondamental garde exactement la moitié de la population | un nombre (4 décimales) |
| f | la température où le niveau d'énergie 4 est dix fois moins peuplé que le fondamental | un nombre (4 décimales) |

Dans ta copie : écris $Z$ à $T = 1$. Pourquoi l'énergie moyenne croît-elle avec $T$ (regarde la figure de la fiche) ? Pour e), écris l'équation $p_1(T) = \frac12$ sous la forme $e^{-1/T} + e^{-2/T} + e^{-4/T} = 1$, explique pourquoi elle a une seule solution, et trouve-la par dichotomie (R7). Pour f), une seule exponentielle suffit : pourquoi ?

### Ex M17.11 — Le recuit simulé : une loi de Boltzmann sur cinq configurations, dont on baisse la température ✏️ ★★ ⏱️ 15 min
**Objectif :** suivre une loi de Boltzmann quand la température baisse, et la règle d'acceptation du recuit simulé.
**Prérequis :** fiche §7 · **Parcours :** C

Un livreur cherche la plus courte de cinq tournées A, B, C, D et E, de longueurs 41, 38, 45, 39 et 40 km. Le recuit simulé tire les tournées selon une loi de Boltzmann dont l'énergie est la longueur (en km), et dont on baisse peu à peu la température $T$ (en km). Partant d'une tournée, il en propose une autre : il l'accepte toujours si elle est plus courte, et avec la probabilité $e^{-\Delta/T}$ si elle est plus longue de $\Delta$.

| | Question | Réponse attendue |
|---|---|---|
| a | la probabilité de la tournée B à $T = 4$ | un nombre (4 décimales) |
| b | la probabilité de la tournée B à $T = 1$ | un nombre (2 décimales) |
| c | la longueur moyenne des tournées tirées à $T = 1$ | un nombre (2 décimales) |
| d | la probabilité de tirer la tournée B ou la tournée D, à $T = 1$ | un nombre (4 décimales) |
| e | la probabilité d'accepter le passage de B à D à $T = 0{,}5$ | un nombre (4 décimales) |
| f | la probabilité d'accepter le passage de D à B à $T = 0{,}5$ | un nombre |

Dans ta copie : écris les poids $e^{-\ell/T}$ des cinq tournées à $T = 1$ sous la forme $e^{-38}$ fois un nombre simple, et dis pourquoi le facteur $e^{-38}$ disparaît. Comment la probabilité d'accepter une tournée plus longue de 1 km évolue-t-elle quand $T$ passe de 1 à 0,5 ? Pourquoi accepte-t-on parfois une tournée plus longue ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration en phrases (R4 §8) : ce que tu supposes, chaque étape et ce qui la justifie, ce que tu conclus. `05_solutions.md` donne une grille de relecture.

### Ex M17.8 — La règle de la chaîne pour des applications de ℝⁿ dans ℝᵐ, à partir de l'approximation linéaire ∂ ★★★ ⏱️ 20 min
**Objectif :** démontrer la règle de la chaîne multivariée à partir de la définition de la jacobienne par l'approximation linéaire.
**Prérequis :** fiche §1 et §3 ; M12a, M12d · **Parcours :** C, E

On dit que $\mathbf{f} : \mathbb{R}^n \to \mathbb{R}^p$ est **différentiable** en $\mathbf{x}$, de jacobienne $\mathbf{J}_{\mathbf{f}}$, si $\mathbf{f}(\mathbf{x} + \mathbf{h}) = \mathbf{f}(\mathbf{x}) + \mathbf{J}_{\mathbf{f}}\mathbf{h} + \boldsymbol{\varepsilon}_{\mathbf{f}}(\mathbf{h})\,\lVert\mathbf{h}\rVert$ avec $\boldsymbol{\varepsilon}_{\mathbf{f}}(\mathbf{h}) \to \mathbf{0}$ quand $\mathbf{h} \to \mathbf{0}$. $\mathbf{g} : \mathbb{R}^p \to \mathbb{R}^m$ est différentiable en $\mathbf{y} = \mathbf{f}(\mathbf{x})$, de jacobienne $\mathbf{J}_{\mathbf{g}}$.

1. Pose $\mathbf{k} = \mathbf{f}(\mathbf{x} + \mathbf{h}) - \mathbf{f}(\mathbf{x})$. Montre que $\lVert\mathbf{k}\rVert \le C\lVert\mathbf{h}\rVert$ pour $\mathbf{h}$ assez petit, avec une constante $C$ (utilise $\lVert\mathbf{J}_{\mathbf{f}}\mathbf{h}\rVert \le \lVert\mathbf{J}_{\mathbf{f}}\rVert_2\,\lVert\mathbf{h}\rVert$, la norme spectrale de M12d). Attention : $\mathbf{k}$ peut être nul pour un $\mathbf{h}$ non nul ; prévois ce cas à l'étape 3.
2. Écris $\mathbf{g}(\mathbf{f}(\mathbf{x} + \mathbf{h})) = \mathbf{g}(\mathbf{y} + \mathbf{k})$ avec l'approximation de $\mathbf{g}$, puis remplace $\mathbf{k}$.
3. Montre que tout ce qui n'est pas $\mathbf{g}(\mathbf{y}) + \mathbf{J}_{\mathbf{g}}\mathbf{J}_{\mathbf{f}}\mathbf{h}$ est petit devant $\lVert\mathbf{h}\rVert$, et conclus : $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{x}) = \mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))\,\mathbf{J}_{\mathbf{f}}(\mathbf{x})$.
4. Écris le coefficient $(i, j)$ de ce produit, et interprète-le comme une somme sur les variables intermédiaires.
5. Retrouve la règle de la chaîne de R7 dans le cas $n = p = m = 1$, et la formule $\nabla_{\mathbf{x}}(L \circ \mathbf{f}) = \nabla_{\mathbf{y}}L\,\mathbf{J}_{\mathbf{f}}$ du §4 dans le cas $m = 1$.

### Ex M17.9 — Une fonction appliquée coordonnée par coordonnée a une jacobienne diagonale, et J v = g′(x) ⊙ v ∂ ★ ⏱️ 15 min
**Objectif :** démontrer qu'une fonction appliquée coordonnée par coordonnée a une jacobienne diagonale, et en tirer les coûts.
**Prérequis :** fiche §2 ; M09a · **Parcours :** C

$g : \mathbb{R} \to \mathbb{R}$ est dérivable, et $\mathbf{f}(\mathbf{x}) = (g(x_1), \ldots, g(x_n))$.

1. Calcule $\frac{\partial f_i}{\partial x_j}$ pour $j \ne i$, puis pour $j = i$, et conclus : $\mathbf{J}_{\mathbf{f}}(\mathbf{x}) = \operatorname{diag}\big(g'(x_1), \ldots, g'(x_n)\big)$.
2. Montre que $\mathbf{J}_{\mathbf{f}}(\mathbf{x})\,\mathbf{v} = g'(\mathbf{x}) \odot \mathbf{v}$ et que $\mathbf{u}^\top\mathbf{J}_{\mathbf{f}}(\mathbf{x}) = (\mathbf{u} \odot g'(\mathbf{x}))^\top$.
3. Combien de multiplications coûtent ces produits, contre un produit par une matrice pleine $n \times n$ ?
4. Montre que la coordonnée $i$ de $\frac{\mathbf{f}(\mathbf{x} + h\mathbf{1}) - \mathbf{f}(\mathbf{x} - h\mathbf{1})}{2h}$ tend vers $g'(x_i)$ quand $h \to 0$ : deux évaluations donnent toute la diagonale.
5. Pour une matrice $\mathbf{A}$ $n \times n$, que donne le même calcul sur $\mathbf{x} \mapsto \mathbf{A}\mathbf{x}$ ? Conclus : pourquoi ne peut-on pas faire confiance au raccourci sans savoir que la jacobienne est diagonale ?

### Ex M17.10 — diag(p) − pᵀp est la covariance d'un vecteur one-hot : symétrique, semi-définie positive, de noyau contenant 1 ∂ ★★ ⏱️ 20 min
**Objectif :** établir la covariance d'un vecteur one-hot, et en déduire ses propriétés.
**Prérequis :** fiche §7 ; M02b, M02c, M12c · **Parcours :** C, E

$I$ suit une loi $\mathbf{p} = (p_1, \ldots, p_K)$ sur $\{1, \ldots, K\}$ (une ligne, $p_i \ge 0$, $\sum_ip_i = 1$), et $\mathbf{Y} = \mathbf{e}_I$ est son vecteur one-hot.

1. Montre que $\mathbb{E}[Y_i] = p_i$, et que $\mathbb{E}[Y_iY_j] = p_i$ si $i = j$ et 0 sinon.
2. Déduis-en $\operatorname{Cov}(\mathbf{Y}) = \operatorname{diag}(\mathbf{p}) - \mathbf{p}^\top\mathbf{p}$, coefficient par coefficient.
3. Montre que cette matrice est symétrique et semi-définie positive, par un argument de variance.
4. Montre que $\sum_jY_j$ est constant, et déduis-en que chaque ligne de la matrice a une somme nulle, sans calculer la matrice ; conclus qu'elle n'est pas inversible.
5. Pour la loi uniforme sur $K = 3$ états, écris la matrice, vérifie qu'elle s'écrit $\frac13\mathbf{I} - \frac19\mathbf{1}^\top\mathbf{1}$, et trouve ses valeurs propres (cherche des vecteurs propres orthogonaux à $\mathbf{1}$).

<a id="reflexion"></a>

## 📖 🗣️ Lecture et explication

### Ex M17.12 — MML §5.3 : gradients de fonctions à valeurs vectorielles, en anglais 📖 ★★ ⏱️ 35 min
**Objectif :** lire une section de MML en anglais, et relier ses notations à celles de la fiche.
**Prérequis :** fiche §1, §3 et §4 · **Parcours :** C

Lis MML §5.3 (*Gradients of Vector-Valued Functions*), crayon en main, puis réponds dans ta copie, en français :
1. Comment MML définit-il la jacobienne, et quelle forme lui donne-t-il ? Quel nom donne-t-il à cette disposition, et pourquoi est-elle la même que celle de la fiche ?
2. Quel symbole MML emploie-t-il pour la jacobienne, et pour la dérivée d'une fonction réelle par rapport à un vecteur ? Le gradient y est-il une ligne ou une colonne ?
3. Que dit MML du déterminant de la jacobienne ? Relie-le au §1 de la fiche (le changement d'aire) et à ✏️ M17.1.
4. Refais à la main un exemple de MML §5.3 qui dérive une fonction composée, et écris-le avec les formes de chaque facteur, comme au §3.
5. Relève trois expressions anglaises de la section, et leur traduction dans la fiche.

### Ex M17.13 — Expliquer la règle de la chaîne multivariée avec des taux de change entre monnaies 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer sans formule pourquoi la règle de la chaîne multiplie le long des chemins et additionne entre les chemins.
**Prérequis :** fiche §3 · **Parcours :** C, E

Un ami voyage avec des euros et des dollars ; il change chaque euro et chaque dollar en partie en francs suisses, en partie en livres (selon une répartition fixée), puis paie tout en yens. Il demande : « si j'ajoute un euro au départ, combien de yens de plus ? » Réponds-lui en 6 à 10 phrases, sans formule, en t'appuyant sur trois idées : le long d'un chemin de change (euro → franc → yen), les taux se **multiplient** ; d'un chemin à l'autre (par le franc ou par la livre), les effets s'**additionnent** ; le tableau de tous les taux d'une étape est une jacobienne, et le tableau d'un bout à l'autre est leur produit. Dis aussi pourquoi les taux sont ceux du jour où l'on change, et ce que deviendrait la réponse si les taux dépendaient du montant changé. Puis réécris ta réponse en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

### M17.E1 — « Qu'est-ce qu'une jacobienne ? Donne un exemple hors du machine learning. » 💼 ★ ⏱️ 10 min
*Fiche §1 et §5 · parcours C*

« Qu'est-ce qu'une jacobienne ? Donne un exemple hors du machine learning. »

Prépare une réponse orale de **60 secondes**. Elle doit dire ce qu'est la jacobienne (la matrice des dérivées partielles, une ligne par sortie et une colonne par entrée), ce qu'elle approche (la meilleure approximation linéaire près d'un point), un exemple concret hors du machine learning (un changement de coordonnées, une carte, une grandeur physique qui dépend de plusieurs autres), ce que dit son déterminant, comment elle se compose (le produit des jacobiennes), et pourquoi on calcule souvent son produit par un vecteur plutôt que la matrice entière. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m17_jacobienne/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M17.14 | La jacobienne par différences centrées, colonne par colonne · `numerical_jacobian` | 🔨 | ★★ | 20 | C, E |
| M17.15 | Une jacobienne diagonale avec une seule paire d'évaluations · `diagonal_jacobian` | 🔨 | ★ | 15 | C, E |
| M17.16 | Un produit jacobienne-vecteur sans former la jacobienne · `jacobian_vector_product` | 🔨 | ★ | 15 | C |
| M17.17 | `sympy.Matrix.jacobian` et `scipy.differentiate.jacobian` contre ta jacobienne numérique | 📦 | ★ | 15 | C, E |
| M17.18 | Prédire la forme et les zéros de la jacobienne d'une composée, puis vérifier | 🔮 | ★ | 10 | C, E |
| M17.19 | Une longue composition : une dérivée qui s'éteint ou explose selon la pente au point fixe | 🔬 | ★★ | 20 | C |
| M17.20 | Une grille du plan déformée par une application non linéaire, et par son approximation linéaire | 🎨 | ★ | 20 | C, E |
| M17.21 | Chasse à l'erreur : une jacobienne transposée, un produit dans le mauvais ordre, une jacobienne évaluée au mauvais point | 🐛 | ★ | 15 | C, E |
| M17.22 | Un test de propriété : J_{g∘f} = J_g J_f sur des applications tirées au hasard | 🛠️ | ★ | 15 | C |
| M17.23 | Défi : la jacobienne de l'inversion X ↦ X⁻¹, vue comme une application de ℝ^{n²} dans ℝ^{n²} | 🏆 | ★★★ | 25 | C |
