# M17 · Jacobienne et règle de la chaîne — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [📖 🗣️ Lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M17.Q1 — La forme d'une jacobienne

<details><summary>Indice 1</summary>

Relis « Une ligne par sortie, une colonne par entrée » et « Les applications linéaires et affines » (fiche §1).

</details>
<details><summary>Indice 2</summary>

$m$ sorties, $n$ entrées : $(m, n)$. En lignes, la sortie $k$ de $\mathbf{x}\mathbf{W}$ est $\sum_j x_jW_{jk}$.

</details>
<details><summary>Indice 3</summary>

6 : $\lvert\det\mathbf{J}\rvert$ est le facteur local de changement d'aire.

</details>

### M17.Q2 — Diagonale ou pleine ?

<details><summary>Indice 1</summary>

Relis le §2 de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque sortie $i$, demande-toi de quelles entrées elle dépend : la ligne $i$ n'a de coefficients non nuls que dans ces colonnes.

</details>
<details><summary>Indice 3</summary>

3 : la sortie 3 dépend de $x_1$, $x_2$, $x_3$, pas de $x_4$. 4 : toutes les sorties dépendent de $\lVert\mathbf{x}\rVert$.

</details>

### M17.Q3 — Dans quel ordre multiplier les jacobiennes ?

<details><summary>Indice 1</summary>

Relis « L'énoncé » au §3.

</details>
<details><summary>Indice 2</summary>

$\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{x}) = \mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))\,\mathbf{J}_{\mathbf{f}}(\mathbf{x})$, de formes $(m, p) \times (p, n)$.

</details>
<details><summary>Indice 3</summary>

5 : une somme sur les variables intermédiaires, autant que $\mathbf{g}$ a d'entrées. 6 : deux matrices ne commutent pas en général.

</details>

### M17.Q4 — Gradient en ligne ou de la forme de la variable

<details><summary>Indice 1</summary>

Relis le §4.

</details>
<details><summary>Indice 2</summary>

En ligne : $\nabla_{\mathbf{y}}L\,\mathbf{J}_{\mathbf{f}}$ ; en colonne : $\mathbf{J}_{\mathbf{f}}^\top\nabla_{\mathbf{y}}L$.

</details>
<details><summary>Indice 3</summary>

4 : regarde les formes, $(3, 4)$ et $(3,)$.

</details>

### M17.Q5 — Jacobienne-vecteur ou vecteur-jacobienne : combien d'opérations ?

<details><summary>Indice 1</summary>

Relis « Qui coûte le moins ? » (§5).

</details>
<details><summary>Indice 2</summary>

Un produit jacobienne-vecteur donne une colonne de $\mathbf{J}$ (avec $\mathbf{v} = \mathbf{e}_j$) ; un produit vecteur-jacobienne une ligne.

</details>
<details><summary>Indice 3</summary>

4 : un produit matrice-vecteur $500 \times 500$ coûte $500^2$ ; un produit de deux matrices $500 \times 500$ coûte $500^3$.

</details>

### M17.Q6 — La loi de Boltzmann : populations relatives et énergie moyenne

<details><summary>Indice 1</summary>

Relis le §7 : le rapport de deux populations, puis les deux limites.

</details>
<details><summary>Indice 2</summary>

$\frac{p_i}{p_j} = e^{-(E_i - E_j)/T}$ ; quand $T \to \infty$, la loi devient uniforme.

</details>
<details><summary>Indice 3</summary>

4 : un rapport de populations, $e^{-3/T} = \frac{1}{100}$. 6 : que vaut la somme de chaque ligne de cette matrice ?

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M17.R1 — Dérivées partielles et gradient (M05b)

<details><summary>Indice 1</summary>

M05b §2 et §3.

</details>
<details><summary>Indice 2</summary>

La dérivée directionnelle dans la direction unitaire $\mathbf{u}$ est $\nabla f \cdot \mathbf{u}$.

</details>
<details><summary>Indice 3</summary>

5 : $f(1, 2) + \nabla f \cdot (0{,}1 ;\ -0{,}1)$.

</details>

### M17.R2 — La règle de la chaîne en une variable (R7)

<details><summary>Indice 1</summary>

R7 §7.

</details>
<details><summary>Indice 2</summary>

$(g \circ f)'(x) = g'(f(x))\,f'(x)$ : la dérivée de l'extérieure, **évaluée en l'intérieure**, fois la dérivée de l'intérieure.

</details>
<details><summary>Indice 3</summary>

4 : trois étages, $\sqrt{u}$, $u = 1 + v^2$, $v = \sin x$. 5 : $g'$ s'évalue en $f(2) = 5$.

</details>

### M17.R3 — La matrice de covariance (M02c)

<details><summary>Indice 1</summary>

M02c §8.

</details>
<details><summary>Indice 2</summary>

$\mathbb{V}(\mathbf{v} \cdot \mathbf{X}) = \sum_{i,j}v_iv_j\,\operatorname{Cov}(X_i, X_j)$.

</details>
<details><summary>Indice 3</summary>

4 : les coordonnées de $\boldsymbol{\Sigma}(1, 1)^\top$ sont $\operatorname{Cov}(X_i, X_1 + X_2)$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M17.1 — La jacobienne des coordonnées polaires

<details><summary>Indice 1</summary>

Relis le §1 : la définition, l'approximation linéaire et le déterminant.

</details>
<details><summary>Indice 2</summary>

Ligne 1 : les dérivées de $r\cos\theta$ par rapport à $r$ puis à $\theta$ ; ligne 2 : celles de $r\sin\theta$.

</details>
<details><summary>Indice 3</summary>

d) $\mathbf{f}(4, \frac{\pi}{6}) + \mathbf{J}\,(0{,}1 ;\ 0{,}05)$. g) $\lvert\det\mathbf{J}\rvert$ fois l'aire du rectangle, $0{,}01 \times 0{,}02$.

</details>

### Ex M17.2 — Une fonction appliquée coordonnée par coordonnée

<details><summary>Indice 1</summary>

Relis le §2.

</details>
<details><summary>Indice 2</summary>

La diagonale est $g'(\mathbf{x})$, avec $g'(t) = \frac{2t}{1 + t^2}$ ; $\mathbf{J}\mathbf{v} = g'(\mathbf{x}) \odot \mathbf{v}$.

</details>
<details><summary>Indice 3</summary>

c) 12 coefficients hors de la diagonale, plus les zéros de la diagonale. f) La règle du produit : $(t\,g(t))' = g(t) + t\,g'(t)$.

</details>

### Ex M17.3 — Dériver une composée de trois applications

<details><summary>Indice 1</summary>

Relis « Plusieurs étages » (§3) : calcule d'abord tous les points intermédiaires.

</details>
<details><summary>Indice 2</summary>

$\mathbf{f}_1(1, 2) = (3, 2, -1)$, puis $\mathbf{f}_2(3, 2, -1)$ ; chaque jacobienne s'évalue au point où son application est appliquée.

</details>
<details><summary>Indice 3</summary>

e) $\mathbf{J}_{f_3}\mathbf{J}_{\mathbf{f}_2}$ d'abord (une ligne de 3), puis fois $\mathbf{J}_{\mathbf{f}_1}$. f) Un produit $(a, b) \times (b, c)$ coûte $abc$ multiplications.

</details>

### Ex M17.4 — La normalisation x/‖x‖

<details><summary>Indice 1</summary>

Relis le §3 (les formes) et le §5 (un produit sans la matrice).

</details>
<details><summary>Indice 2</summary>

$\mathbf{u} = (0{,}6 ;\ 0 ;\ 0{,}8)$ ; $\mathbf{u}\mathbf{u}^\top$ est la matrice des produits $u_iu_j$.

</details>
<details><summary>Indice 3</summary>

c) $\mathbf{x} = 5\mathbf{u}$, et $(\mathbf{I} - \mathbf{u}\mathbf{u}^\top)\mathbf{u} = \mathbf{u} - \mathbf{u}(\mathbf{u} \cdot \mathbf{u})$. e) et f) $\mathbf{I} - \mathbf{u}\mathbf{u}^\top$ est une projection orthogonale sur un plan (M12b).

</details>

### Ex M17.5 — Le gradient d'une fonction scalaire d'une composée

<details><summary>Indice 1</summary>

Relis l'exemple du §4.

</details>
<details><summary>Indice 2</summary>

$\nabla_{\mathbf{y}}L = (2y_1,\ 3,\ -1)$, évalué en $\mathbf{y} = \mathbf{f}(\mathbf{x})$.

</details>
<details><summary>Indice 3</summary>

d) $(6, 3, -1)\,\mathbf{J}_{\mathbf{f}}$, une ligne de 2. f) Le produit scalaire du gradient et de $(1, 1)$.

</details>

### Ex M17.6 — Dérivées à gauche et à droite, et une composée de sept copies

<details><summary>Indice 1</summary>

Relis le §6 : les dérivées latérales, puis les longues compositions.

</details>
<details><summary>Indice 2</summary>

b) et c) : les pentes des morceaux de chaque côté. d) $c(x) = 40$ en un point où $c$ est dérivable ; la valeur absolue change le signe d'un côté. e) Calcule $x_1, x_2, \ldots$ en fractions.

</details>
<details><summary>Indice 3</summary>

f) $\prod_{k=0}^{6}g'(x_k)$ avec $g'(x) = -\frac{1}{(1 + x)^2}$ : écris les $1 + x_k$ en fractions, leurs numérateurs et dénominateurs se simplifient deux à deux. g) Au point fixe, $x^*(1 + x^*) = 1$.

</details>

### Ex M17.7 — Une loi de Boltzmann à quatre niveaux d'énergie

<details><summary>Indice 1</summary>

Relis le §7.

</details>
<details><summary>Indice 2</summary>

À $T = 1$, les poids sont $e^{-E_i}$ ; $Z$ est leur somme, et $p_i = \frac{e^{-E_i}}{Z}$.

</details>
<details><summary>Indice 3</summary>

e) $p_1 = \frac{1}{Z(T)} = \frac12$ revient à $Z(T) = 2$ : dichotomie entre $T = 1$ et $T = 2$. f) Un rapport : $e^{-4/T} = 0{,}1$.

</details>

### Ex M17.11 — Le recuit simulé

<details><summary>Indice 1</summary>

Relis le §7 et la règle d'acceptation de l'énoncé.

</details>
<details><summary>Indice 2</summary>

Écris chaque poids $e^{-\ell/T}$ comme $e^{-38/T}$ fois $e^{-\Delta/T}$, où $\Delta$ est l'écart à 38 km : $(3, 0, 7, 1, 2)$ ; le facteur commun se simplifie.

</details>
<details><summary>Indice 3</summary>

a) $\frac{1}{\sum_j e^{-\Delta_j/4}}$. d) Deux tournées distinctes : additionne $P(B)$ et $P(D)$. f) Lis la règle : une tournée plus courte est toujours acceptée.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M17.8 — La règle de la chaîne à partir de l'approximation linéaire

<details><summary>Indice 1</summary>

Écris les deux approximations linéaires, celle de $\mathbf{f}$ en $\mathbf{x}$ et celle de $\mathbf{g}$ en $\mathbf{f}(\mathbf{x})$, et emboîte-les.

</details>
<details><summary>Indice 2</summary>

Le terme difficile est $\boldsymbol{\varepsilon}_{\mathbf{g}}(\mathbf{k})\,\lVert\mathbf{k}\rVert$ : il faut d'abord montrer que $\lVert\mathbf{k}\rVert$ est au plus proportionnel à $\lVert\mathbf{h}\rVert$.

</details>
<details><summary>Indice 3</summary>

Divise le reste par $\lVert\mathbf{h}\rVert$ : $\mathbf{J}_{\mathbf{g}}\boldsymbol{\varepsilon}_{\mathbf{f}}(\mathbf{h}) + \boldsymbol{\varepsilon}_{\mathbf{g}}(\mathbf{k})\frac{\lVert\mathbf{k}\rVert}{\lVert\mathbf{h}\rVert}$, et majore le second terme par $C\lVert\boldsymbol{\varepsilon}_{\mathbf{g}}(\mathbf{k})\rVert$.

</details>

### Ex M17.9 — Une fonction appliquée coordonnée par coordonnée a une jacobienne diagonale

<details><summary>Indice 1</summary>

$f_i$ ne dépend que de $x_i$.

</details>
<details><summary>Indice 2</summary>

$(\mathbf{J}\mathbf{v})_i = \sum_jJ_{ij}v_j$ : un seul terme non nul.

</details>
<details><summary>Indice 3</summary>

5 : la coordonnée $i$ de $\mathbf{A}(\mathbf{x} + h\mathbf{1}) - \mathbf{A}(\mathbf{x} - h\mathbf{1})$ vaut $2h\sum_jA_{ij}$.

</details>

### Ex M17.10 — diag(p) − pᵀp est la covariance d'un vecteur one-hot

<details><summary>Indice 1</summary>

Chaque $Y_i$ est une variable de Bernoulli ; deux coordonnées distinctes ne valent jamais 1 ensemble.

</details>
<details><summary>Indice 2</summary>

$\operatorname{Cov}(Y_i, Y_j) = \mathbb{E}[Y_iY_j] - \mathbb{E}[Y_i]\,\mathbb{E}[Y_j]$ ; pour la semi-définie positivité, pense à $\mathbb{V}(\mathbf{v} \cdot \mathbf{Y})$.

</details>
<details><summary>Indice 3</summary>

4 : la somme de la ligne $i$ est $\operatorname{Cov}\big(Y_i, \sum_jY_j\big)$.

</details>

<a id="reflexion"></a>

## 📖 🗣️ Lecture et explication

### Ex M17.12 — MML §5.3

<details><summary>Indice 1</summary>

Lis la section une première fois sans t'arrêter, puis une deuxième fois crayon en main.

</details>
<details><summary>Indice 2</summary>

Cherche la définition de la jacobienne, la phrase sur sa disposition, et le passage sur son déterminant.

</details>
<details><summary>Indice 3</summary>

Pour l'exemple de composée, écris la forme de chaque facteur sous lui, comme dans l'exemple du cercle de la fiche §3.

</details>

### Ex M17.13 — Expliquer la règle de la chaîne avec des taux de change

<details><summary>Indice 1</summary>

Relis « Coefficient par coefficient » (§3).

</details>
<details><summary>Indice 2</summary>

Un chemin de change : on multiplie les taux. Deux chemins : on additionne les gains.

</details>
<details><summary>Indice 3</summary>

Le tableau des taux d'une étape, une ligne par monnaie d'arrivée : une jacobienne. Les taux « du jour » : le point d'évaluation.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M17.E1 — « Qu'est-ce qu'une jacobienne ? Donne un exemple hors du machine learning. »

<details><summary>Indice 1</summary>

Une définition, une interprétation, un exemple, deux propriétés.

</details>
<details><summary>Indice 2</summary>

Pense à un changement de coordonnées, à une carte, ou à une grandeur physique qui dépend de plusieurs autres.

</details>
<details><summary>Indice 3</summary>

Ajoute le déterminant (le changement d'aire), la composition (le produit) et le produit par un vecteur (le coût).

</details>

<a id="notebook"></a>

## Notebook

### M17.14 — La jacobienne par différences centrées

<details><summary>Indice 1</summary>

Fiche §1, « La calculer par différences ».

</details>
<details><summary>Indice 2</summary>

Convertis `x` en un tableau de flottants **copié** ; pour chaque $j$, un vecteur `step` nul sauf `step[j] = h` ; `np.atleast_1d` sur les valeurs de `f`.

</details>
<details><summary>Indice 3</summary>

Range les colonnes dans une liste, puis `np.column_stack(columns)` ; vérifie avant que toutes les valeurs ont la même longueur et sont 1-D.

</details>

### M17.15 — Une jacobienne diagonale avec une seule paire d'évaluations

<details><summary>Indice 1</summary>

Fiche §2, « Une seule paire d'évaluations ».

</details>
<details><summary>Indice 2</summary>

`x + h` ajoute `h` à toutes les coordonnées à la fois.

</details>
<details><summary>Indice 3</summary>

`np.diag((plus - minus) / (2 * h))`, après avoir vérifié que `f(x)` a la longueur de `x`.

</details>

### M17.16 — Un produit jacobienne-vecteur sans former la jacobienne

<details><summary>Indice 1</summary>

Fiche §5.

</details>
<details><summary>Indice 2</summary>

Le pas se fait le long de `v` : `x + h * v` et `x - h * v`.

</details>
<details><summary>Indice 3</summary>

Vérifie que `x` et `v` sont 1-D, non vides, de même longueur, et que `h > 0`.

</details>

### M17.17 — `sympy.Matrix.jacobian` et `scipy.differentiate.jacobian`

<details><summary>Indice 1</summary>

`sympy.Matrix([...]).jacobian([r, theta, phi])`, puis `.det()` et `sympy.simplify`.

</details>
<details><summary>Indice 2</summary>

`.subs({...})` puis `.evalf()` pour évaluer la jacobienne SymPy en un point ; `np.array(..., dtype=float)`.

</details>
<details><summary>Indice 3</summary>

Pour SciPy, la fonction doit accepter un tableau dont chaque colonne est un point : écris-la avec `p[0]`, `p[1]`, `p[2]`, qui sont alors des lignes de valeurs.

</details>

### M17.18 — Prédire la forme et les zéros de la jacobienne d'une composée

<details><summary>Indice 1</summary>

Fiche §3 : les formes, puis les dépendances.

</details>
<details><summary>Indice 2</summary>

Écris le motif des zéros de $\mathbf{J}_{\mathbf{f}}$ et de $\mathbf{J}_{\mathbf{g}}$, puis celui de leur produit.

</details>
<details><summary>Indice 3</summary>

La sortie 2 de $\mathbf{g} \circ \mathbf{f}$ est $(x_4 + x_1)^2$.

</details>

### M17.19 — Une longue composition

<details><summary>Indice 1</summary>

Fiche §6, « Longues compositions ».

</details>
<details><summary>Indice 2</summary>

Une boucle qui garde $x_k$ et $D_k$ : $D_{k+1} = D_k\,\varphi'(x_k)$, puis $x_{k+1} = \varphi(x_k)$ — dans cet ordre.

</details>
<details><summary>Indice 3</summary>

Pour $c = 2{,}6$, $x^* = 1 - \frac{1}{c}$ et $\varphi'(x^*) = c(1 - 2x^*)$.

</details>

### M17.20 — Une grille déformée et son approximation linéaire

<details><summary>Indice 1</summary>

Fiche §1 et sa figure.

</details>
<details><summary>Indice 2</summary>

Une ligne de la grille est un ensemble de points $\mathbf{p}$ ; trace $F(\mathbf{p})$ puis $F(\mathbf{a}) + \mathbf{J}(\mathbf{p} - \mathbf{a})$.

</details>
<details><summary>Indice 3</summary>

Pour des points rangés en colonnes dans `P`, de forme `(2, k)`, l'approximation linéaire s'écrit `F(a)[:, None] + J @ (P - a[:, None])`.

</details>

### M17.21 — Chasse à l'erreur

<details><summary>Indice 1</summary>

Fiche, les ⚠️ des §1, §3 et §4.

</details>
<details><summary>Indice 2</summary>

(A) Une ligne par sortie ? (B) Quelle application est appliquée en dernier ? (C) En quel point $\mathbf{J}_{\mathbf{g}}$ s'évalue-t-elle ?

</details>
<details><summary>Indice 3</summary>

c) $\mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))\,\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ avec $\mathbf{f}(\mathbf{x}) = (1, 3)$.

</details>

### M17.22 — Un test de propriété

<details><summary>Indice 1</summary>

Fiche §3, l'énoncé encadré.

</details>
<details><summary>Indice 2</summary>

Compare `jacobian(lambda x: g(f(x)), x)` à `jacobian(g, f(x)) @ jacobian(f, x)`, avec `np.allclose`.

</details>
<details><summary>Indice 3</summary>

Vérifie aussi la forme du résultat, et mets dans le message d'échec ce qui était attendu.

</details>

### M17.23 — Défi : la jacobienne de l'inversion

<details><summary>Indice 1</summary>

Dérive l'identité $X X^{-1} = I$ dans une direction $H$ : la dérivée d'un produit de matrices suit la règle du produit, sans changer l'ordre des facteurs.

</details>
<details><summary>Indice 2</summary>

Tu obtiens $H X^{-1} + X\,D = 0$, où $D$ est la dérivée de $X^{-1}$ dans la direction $H$ : résous en $D$.

</details>
<details><summary>Indice 3</summary>

La colonne $k$ de la jacobienne (aplatie par lignes) est la dérivée dans la direction $H = $ la $k$-ième matrice de base, aplatie : construis-la colonne par colonne, et compare à `numerical_jacobian`.

</details>
