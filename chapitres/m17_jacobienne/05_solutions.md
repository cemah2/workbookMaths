# M17 · Jacobienne et règle de la chaîne — solutions

> À lire **après** avoir cherché (et ouvert les indices de `04_indices.md`). Pour chaque exercice : les réponses, la démarche, les erreurs fréquentes et une variante ; pour une démonstration, une rédaction modèle et une grille de relecture. Les exercices du notebook sont corrigés dans `05_solutions.ipynb` ; leur résumé est à la fin.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [📖 🗣️ Lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M17.Q1 — La forme d'une jacobienne
1. $(3, 5)$ : une ligne par sortie, une colonne par entrée.
2. Vrai : la ligne $i$ contient les dérivées de $f_i$ par rapport à chaque entrée, son gradient en ligne.
3. $\mathbf{A}$, de forme $(3, 5)$ (le vecteur $\mathbf{b}$ ne change aucune dérivée). Pour $\mathbf{x} \mapsto \mathbf{x}\mathbf{W}$ : $\mathbf{W}^\top$, de forme $(3, 5)$ elle aussi.
4. $(4, 1)$, une colonne : le **vecteur vitesse** du point.
5. $2n = 10$ : deux évaluations par colonne, quel que soit $m$.
6. Vrai : près de $\mathbf{x}$, les aires sont multipliées par $\lvert\det\mathbf{J}\rvert = 0{,}5$.

### M17.Q2 — Diagonale ou pleine ?
1. Diagonale, $\mathrm{diag}(e^{x_i})$.
2. Diagonale, $\mathrm{diag}(2x_i)$.
3. Triangulaire (inférieure) : la sortie $i$ dépend de $x_1, \ldots, x_i$ ; la ligne $i$ a des 1 dans les colonnes 1 à $i$.
4. Pleine en un point quelconque : chaque sortie dépend de toutes les entrées par $\lVert\mathbf{x}\rVert$ (✏️ M17.4) ; en des points particuliers (sur les axes), certains coefficients s'annulent.
5. Diagonale, et constante : $\mathbf{D}$.
6. Vrai : $\mathbf{J}\mathbf{v} = g'(\mathbf{x}) \odot \mathbf{v}$, une multiplication par coordonnée.

### M17.Q3 — Dans quel ordre multiplier les jacobiennes ?
1. $(5, 2)$, $(3, 5)$ et $(3, 2)$.
2. $\mathbf{J}_{\mathbf{g} \circ \mathbf{f}}(\mathbf{x}) = \mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))\,\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ : $\mathbf{J}_{\mathbf{g}}$ au point intermédiaire $\mathbf{f}(\mathbf{x})$, de 5 coordonnées.
3. Non : $(5, 2) \times (3, 5)$, les dimensions intérieures (2 et 3) ne s'accordent pas.
4. Vrai : pour $n = p = m = 1$, le produit de deux matrices $1 \times 1$ est $g'(f(x))\,f'(x)$.
5. Vrai : une somme sur les 5 variables intermédiaires.
6. Faux : le produit de deux matrices ne commute pas en général ; $\mathbf{J}_{\mathbf{f}}\mathbf{J}_{\mathbf{g}}$ (évaluées n'importe où) n'est pas la jacobienne de $\mathbf{g} \circ \mathbf{f}$.

### M17.Q4 — Gradient en ligne ou de la forme de la variable
1. Chez MML, une ligne $(1, 3)$ ; dans NumPy, un tableau `(3,)`.
2. En ligne : $\nabla_{\mathbf{y}}L\;\mathbf{J}_{\mathbf{f}}$, $(1, 3) \times (3, 4)$. En colonne : $\mathbf{J}_{\mathbf{f}}^\top\nabla_{\mathbf{y}}L$, $(4, 3) \times (3, 1)$.
3. `(4,)`, la forme de $\mathbf{x}$.
4. Faux : $\mathbf{J}_{\mathbf{f}}$ a la forme $(3, 4)$, et $\nabla_{\mathbf{y}}L$ trois coordonnées : le produit n'existe pas. Il faut la transposée.
5. `(4, 2)`.
6. Vrai : seul le rangement change.

### M17.Q5 — Jacobienne-vecteur ou vecteur-jacobienne : combien d'opérations ?
1. 1 000 produits jacobienne-vecteur (un par coordonnée du gradient) ; **un seul** produit vecteur-jacobienne, $1 \cdot \mathbf{J}$.
2. L'inverse : un produit jacobienne-vecteur ($\mathbf{J}$ est une colonne, $\mathbf{J} \cdot 1$), 1 000 produits vecteur-jacobienne.
3. Deux, quel que soit $n$.
4. $\mathbf{J}_2(\mathbf{J}_1\mathbf{v})$ : deux produits matrice-vecteur, $2 \times 500^2 = 500\,000$. $(\mathbf{J}_2\mathbf{J}_1)\mathbf{v}$ : $500^3 + 500^2 = 125\,250\,000$, 250 fois plus.
5. Vrai (fiche §5).
6. Vrai : $\mathbf{J}\mathbf{e}_j$ est la colonne $j$.

### M17.Q6 — La loi de Boltzmann : populations relatives et énergie moyenne
1. $e^{-(3 - 1)/1} = e^{-2} \approx 0{,}135$.
2. $Z = 1 + e^{-1} + e^{-3} \approx 1 + 0{,}3679 + 0{,}0498 \approx 1{,}418$.
3. $0$ (tout sur le niveau d'énergie 0) et $\frac{0 + 1 + 3}{3} = \frac43$ (la loi devient uniforme).
4. $e^{-3/T} = \frac{1}{100}$, soit $T = \frac{3}{\ln 100} \approx 0{,}651$.
5. Vrai : deux états de même énergie ont le même poids $e^{-E/T}$, donc la même population, à toute température.
6. Faux : elle annule $\mathbf{1}$ (chaque ligne a une somme nulle).

<a id="rappels"></a>

## 🔁 Rappels

### M17.R1 — Dérivées partielles et gradient (M05b)
1. $\frac{\partial f}{\partial x} = 2xy$, $\frac{\partial f}{\partial y} = x^2 - 3$.
2. $(4, -2)$.
3. $4 \times 0{,}6 + (-2) \times 0{,}8 = 0{,}8$.
4. Dans la direction du gradient, $\frac{(4, -2)}{\sqrt{20}} \approx (0{,}894 ;\ -0{,}447)$.
5. $f(1, 2) = -3$, et $-3 + 4 \times 0{,}1 + (-2) \times (-0{,}1) = -2{,}4$ (exactement $-2{,}401$).

### M17.R2 — La règle de la chaîne en une variable (R7)
1. $2x\cos(x^2)$.
2. $-\sin x\,e^{\cos x}$.
3. $\frac{4x^3}{1 + x^4}$.
4. $\frac{2\sin x\cos x}{2\sqrt{1 + \sin^2x}} = \frac{\sin x\cos x}{\sqrt{1 + \sin^2x}}$.
5. $g'(f(2))\,f'(2) = g'(5) \times (-1) = -3$ ; $g'(2)$ ne sert pas : c'est le piège du point d'évaluation.

### M17.R3 — La matrice de covariance (M02c)
1. $4 + 2 + 2 \times (-1) = 4$ ; $4 + 2 - 2 \times (-1) = 8$.
2. $\mathbb{V}(\mathbf{v} \cdot \mathbf{X}) = \mathbf{v}\,\boldsymbol{\Sigma}\,\mathbf{v}^\top$.
3. Parce que $\mathbf{v}\,\boldsymbol{\Sigma}\,\mathbf{v}^\top$ est une variance, donc $\ge 0$, pour tout $\mathbf{v}$.
4. Le vecteur nul : les coordonnées de $\boldsymbol{\Sigma}'(1, 1)^\top$ sont $\mathrm{Cov}(X_i, X_1 + X_2)$, nulles puisque $X_1 + X_2$ est constant. Ce n'est pas possible pour $\boldsymbol{\Sigma}$ : $\boldsymbol{\Sigma}(1, 1)^\top = (3, 1)$, et $\mathbb{V}(X_1 + X_2) = 4 \ne 0$.
5. Toujours symétrique ($\mathrm{Cov}(X_i, X_j) = \mathrm{Cov}(X_j, X_i)$) ; pas toujours inversible (la matrice $\boldsymbol{\Sigma}'$ de la question 4).

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M17.1 — La jacobienne des coordonnées polaires

**Réponses.** a) `[3.4641, 2.0]` · b) `[[0.866, -2.0], [0.5, 3.4641]]` · c) `4` · d) `[3.4507, 2.2232]` · e) `[3.4438, 2.2249]` · f) `0.0071` · g) `0.0008`.

**Démarche.** $\mathbf{J}_{\mathbf{f}}(r, \theta) = \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix}$ ; en $(4, \frac{\pi}{6})$, $\begin{pmatrix} \frac{\sqrt3}{2} & -2 \\ \frac12 & 2\sqrt3 \end{pmatrix}$. c) $r\cos^2\theta + r\sin^2\theta = r = 4$. d) $\mathbf{f}(4, \frac{\pi}{6}) + \mathbf{J}\,(0{,}1 ;\ 0{,}05) = (2\sqrt3 + 0{,}0866 - 0{,}1 ;\ 2 + 0{,}05 + 0{,}1732)$. e) $4{,}1\cos(0{,}5736)$ et $4{,}1\sin(0{,}5736)$. f) $\sqrt{0{,}0069^2 + 0{,}0017^2}$. g) $\lvert\det\mathbf{J}\rvert \times 0{,}01 \times 0{,}02 = 4 \times 0{,}0002$.

Dans ta copie : la première colonne, $(\cos\theta, \sin\theta)$, est un vecteur unitaire : quand $r$ bouge, le point s'éloigne de l'origine à vitesse 1. La deuxième, $r(-\sin\theta, \cos\theta)$, est tangente au cercle de rayon $r$ : quand $\theta$ bouge, le point tourne, et parcourt $r$ unités de longueur par radian. Les deux colonnes sont orthogonales, de longueurs 1 et $r$ : le déterminant est leur produit, $r$. L'erreur f) est d'ordre 2 en les déplacements (environ $0{,}1^2$, $0{,}05^2$ et leur produit, multipliés par des dérivées secondes) : bien plus petite que les déplacements eux-mêmes.

**Erreurs fréquentes.** Ranger les dérivées par rapport à $r$ dans la première **ligne** (on obtient la transposée, de même déterminant, mais une approximation fausse). Oublier le facteur $r$ dans la deuxième colonne. Calculer en degrés.

**Variante.** En $(2, \frac{\pi}{2})$ : $\mathbf{J} = \begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix}$, de déterminant 2.

### Ex M17.2 — Une fonction appliquée coordonnée par coordonnée

**Réponses.** a) `[1, -0.8, 0, 0.6]` · b) `[2, -0.8, 0, 0.3]` · c) `13` · d) `999000` · e) `[2, 2000]` · f) `[1.6931, 3.2094, 0.0, 4.1026]`.

**Démarche.** $g'(t) = \frac{2t}{1 + t^2}$ : $1$, $-\frac{4}{5}$, $0$, $\frac{6}{10}$. b) Case par case : $(1 \times 2,\ -0{,}8 \times 1,\ 0 \times (-5),\ 0{,}6 \times 0{,}5)$. c) Les 12 coefficients hors de la diagonale, et $g'(0) = 0$ sur la diagonale. d) $1\,000^2 - 1\,000$. e) Deux évaluations (toutes les coordonnées bougées ensemble), contre deux par colonne. f) $(tg(t))' = g(t) + tg'(t) = \ln(1 + t^2) + \frac{2t^2}{1 + t^2}$ : $\ln 2 + 1$, $\ln 5 + 1{,}6$, $0$, $\ln 10 + 1{,}8$.

Dans ta copie : la sortie 2 ne dépend que de $x_2$, donc pas de $x_3$. $g'(0) = 0$ : $g$ a un minimum en 0 (sa tangente est horizontale). $t \mapsto t\,g(t)$ est encore une fonction d'une variable appliquée coordonnée par coordonnée.

**Erreurs fréquentes.** Mettre $g(x_i)$ au lieu de $g'(x_i)$ sur la diagonale. En b), faire un produit scalaire (un nombre) au lieu d'un produit case par case. En c), oublier le coefficient nul de la diagonale.

**Variante.** $g(t) = t^3$ en $(1, -1, 2)$ : diagonale $(3, 3, 12)$ ; avec $\mathbf{v} = (1, 1, 1)$, $\mathbf{J}\mathbf{v} = (3, 3, 12)$.

### Ex M17.3 — Dériver une composée de trois applications

**Réponses.** a) `[3, 2, -1]` · b) `[[1, 1], [2, 1], [1, -1]]` · c) `[[2, 3, 0], [0, 1, -2]]` · d) `[[12, -3]]` · e) `[96, 51]` · f) `[12, 16]`.

**Démarche.** b) $\mathbf{J}_{\mathbf{f}_1} = \begin{pmatrix} 1 & 1 \\ y & x \\ 1 & -1 \end{pmatrix}$ en $(1, 2)$. c) $\mathbf{J}_{\mathbf{f}_2} = \begin{pmatrix} v & u & 0 \\ 0 & 1 & 2w \end{pmatrix}$ en $(u, v, w) = (3, 2, -1)$. d) $\mathbf{f}_2(3, 2, -1) = (6, 3)$, et $\mathbf{J}_{f_3} = (2a,\ -3) = (12, -3)$. e) $\mathbf{J}_{f_3}\mathbf{J}_{\mathbf{f}_2} = (24,\ 33,\ 6)$, puis $(24 + 66 + 6,\ 24 + 33 - 6) = (96, 51)$. f) $(1 \times 2 \times 3) + (1 \times 3 \times 2) = 12$ ; $(2 \times 3 \times 2) + (1 \times 2 \times 2) = 16$.

Dans ta copie : $(1, 2) \times (2, 3) \times (3, 2) \to (1, 2)$. $h(x, y) = (x + y)^2x^2y^2 - 3xy - 3(x - y)^2$ : $\frac{\partial h}{\partial x} = 2(x + y)x^2y^2 + 2(x + y)^2xy^2 - 3y - 6(x - y) = 24 + 72 - 6 + 6 = 96$, et de même 51. De gauche à droite, on ne multiplie jamais que des **lignes** par des matrices (la sortie est une seule fonction) : c'est le produit vecteur-jacobienne du §5.

**Erreurs fréquentes.** Évaluer $\mathbf{J}_{\mathbf{f}_2}$ en $(1, 2)$ (impossible : elle attend 3 coordonnées) ou $\mathbf{J}_{f_3}$ en $\mathbf{f}_1(1, 2)$. Multiplier dans l'ordre $\mathbf{J}_{\mathbf{f}_1}\mathbf{J}_{\mathbf{f}_2}\mathbf{J}_{f_3}$.

**Variante.** Au point $(1, 0)$ : $\mathbf{f}_1 = (1, 0, 1)$, $\mathbf{f}_2 = (0, 1)$, $\nabla h = (0, -3)\,\begin{pmatrix} 0 & 1 & 0 \\ 0 & 1 & 2 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \\ 1 & -1 \end{pmatrix} = (0, -3, -6)\begin{pmatrix} 1 & 1 \\ 0 & 1 \\ 1 & -1 \end{pmatrix} = (-6, 3)$.

### Ex M17.4 — La normalisation x/‖x‖

**Réponses.** a) `[5, 0.6, 0, 0.8]` · b) `[[0.128, 0, -0.096], [0, 0.2, 0], [-0.096, 0, 0.072]]` · c) `[0, 0, 0]` · d) `[-0.096, 0.4, 0.072]` · e) `2` · f) `[0, 0.2, 0.2]`.

**Démarche.** b) $\mathbf{u}\mathbf{u}^\top = \begin{pmatrix} 0{,}36 & 0 & 0{,}48 \\ 0 & 0 & 0 \\ 0{,}48 & 0 & 0{,}64 \end{pmatrix}$, puis $\frac{\mathbf{I} - \mathbf{u}\mathbf{u}^\top}{5}$. c) $\mathbf{J}\mathbf{x} = \frac{\mathbf{x} - (\mathbf{u} \cdot \mathbf{x})\,\mathbf{u}}{5} = \frac{\mathbf{x} - 5\mathbf{u}}{5} = \mathbf{0}$. d) $\mathbf{u} \cdot \mathbf{v} = 0{,}8$, $\mathbf{v} - 0{,}8\,\mathbf{u} = (-0{,}48 ;\ 2 ;\ 0{,}36)$, divisé par 5.

Dans ta copie : $\frac{\partial}{\partial x_j}\frac{x_i}{\lVert\mathbf{x}\rVert} = \frac{\delta_{ij}}{\lVert\mathbf{x}\rVert} - \frac{x_ix_j}{\lVert\mathbf{x}\rVert^3} = \frac{\delta_{ij} - u_iu_j}{\lVert\mathbf{x}\rVert}$. Le long de la droite de $\mathbf{x}$, $\mathbf{n}$ est constante ($\mathbf{n}(t\mathbf{x}) = \mathbf{n}(\mathbf{x})$ pour $t > 0$) : sa dérivée dans la direction $\mathbf{x}$ est nulle. $\mathbf{I} - \mathbf{u}\mathbf{u}^\top$ est la projection orthogonale sur le plan orthogonal à $\mathbf{u}$ : elle annule $\mathbf{u}$ et garde le plan, d'où le rang 2 et les valeurs propres $0$, $1$, $1$, divisées par $\lVert\mathbf{x}\rVert = 5$. d) coûte un produit scalaire et une combinaison, environ $3n$ multiplications, contre $n^2 = 10^6$ coefficients pour la matrice.

**Erreurs fréquentes.** Oublier la division par $\lVert\mathbf{x}\rVert$ (on obtient la projection seule). Écrire $\mathbf{u}^\top\mathbf{u}$ (un nombre, 1) au lieu de $\mathbf{u}\mathbf{u}^\top$ (une matrice). Croire que $\mathbf{J}\mathbf{x} = \mathbf{u}$.

**Variante.** En $\mathbf{x} = (0, 0, 2)$ : $\mathbf{J} = \frac12\,\mathrm{diag}(1, 1, 0)$, et $\mathbf{J}(1, 1, 1) = (0{,}5 ;\ 0{,}5 ;\ 0)$.

### Ex M17.5 — Le gradient d'une fonction scalaire d'une composée, dans les deux conventions

**Réponses.** a) `[3, -2, 1]` · b) `[6, 3, -1]` · c) `[[1, -1], [-1, 2], [0, -2]]` · d) `[3, 2]` · e) `[2, 3]` · f) `5`.

**Démarche.** c) $\mathbf{J}_{\mathbf{f}} = \begin{pmatrix} 1 & -1 \\ x_2 & x_1 \\ 0 & 2x_2 \end{pmatrix}$ en $(2, -1)$. d) En ligne : $(6, 3, -1)\,\mathbf{J}_{\mathbf{f}} = (6 - 3 + 0,\ -6 + 6 + 2) = (3, 2)$ ; en colonne, $\mathbf{J}_{\mathbf{f}}^\top(6, 3, -1)^\top$, les mêmes nombres. f) $(3, 2) \cdot (1, 1) = 5$.

Dans ta copie : $L(\mathbf{f}(\mathbf{x})) = (x_1 - x_2)^2 + 3x_1x_2 - x_2^2$, de dérivées $2(x_1 - x_2) + 3x_2 = 3$ et $-2(x_1 - x_2) + 3x_1 - 2x_2 = 2$. $\mathbf{J}_{\mathbf{f}}$ a la forme $(3, 2)$ et $\nabla_{\mathbf{y}}L$ trois coordonnées : $\mathbf{J}_{\mathbf{f}}\nabla_{\mathbf{y}}L$ n'existe pas.

**Erreurs fréquentes.** Évaluer $\nabla_{\mathbf{y}}L$ en $\mathbf{x}$. Oublier la transposée en convention colonne. Normaliser $(1, 1)$ (on trouve $\frac{5}{\sqrt2} \approx 3{,}54$) : la question demande la dérivée de $t \mapsto (L \circ \mathbf{f})(\mathbf{x} + t\,(1, 1))$, c'est-à-dire $\nabla(L \circ \mathbf{f}) \cdot (1, 1)$.

**Variante.** En $\mathbf{x} = (1, 1)$ : $\mathbf{y} = (0, 1, 1)$, $\nabla_{\mathbf{y}}L = (0, 3, -1)$, $\mathbf{J}_{\mathbf{f}} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \\ 0 & 2 \end{pmatrix}$, gradient $(3, 1)$.

### Ex M17.6 — Dérivées à gauche et à droite, et une composée de sept copies

**Réponses.** a) `67` · b) `[0.15, 0.25]` · c) `[0.25, 0.1]` · d) `[-0.25, 0.25]` · e) `"21/34"` · f) `"-1/1156"` · g) `0.382`.

**Démarche.** a) $65 + 0{,}1 \times 20$. b) et c) Les pentes des morceaux de part et d'autre. d) $c(x) = 40$ pour $15 + 0{,}25(x - 100) = 40$, soit $x = 200$, au milieu d'un morceau de pente $0{,}25$ ; à gauche, $c < 40$ et $\lvert c - 40\rvert = 40 - c$, de pente $-0{,}25$ ; à droite, $+0{,}25$. e) $x_1 = \frac12$, $x_2 = \frac23$, $x_3 = \frac35$, $x_4 = \frac58$, $x_5 = \frac{8}{13}$, $x_6 = \frac{13}{21}$, $x_7 = \frac{21}{34}$ (des quotients de nombres de Fibonacci). f) $g'(x) = -\frac{1}{(1 + x)^2}$ ; les $1 + x_k$ valent $2, \frac32, \frac53, \frac85, \frac{13}{8}, \frac{21}{13}, \frac{34}{21}$, dont le produit **se télescope** en 34 ; la dérivée vaut $(-1)^7\frac{1}{34^2} = -\frac{1}{1\,156}$. g) $x^* = \frac{\sqrt5 - 1}{2} \approx 0{,}618$ résout $x(1 + x) = 1$, et $\lvert g'(x^*)\rvert = \frac{1}{(1 + x^*)^2} = (x^*)^2 \approx 0{,}382$.

Dans ta copie : $c$ est continue (les morceaux se raccordent : $c(100) = 15$, $c(300) = 65$). Restreinte à $[0 ;\ 300]$, ses pentes croissent ($0{,}15$ puis $0{,}25$) : elle y est convexe, et ses sous-gradients en 100 forment $[0{,}15 ;\ 0{,}25]$. Sur $[0 ;\ +\infty[$, la pente baisse en 300 : $c(300) = 65$ est au-dessus de la corde entre 200 et 400 ($\frac{40 + 75}{2} = 57{,}5$), donc $c$ n'est pas convexe. En 300, une droite $65 + s(x - 300)$ sous la courbe devrait avoir $s \ge 0{,}25$ (à gauche) et $s \le 0{,}1$ (à droite) : aucun sous-gradient. f) est de l'ordre de $0{,}382^7 \approx 0{,}0012$ : les sept facteurs $\frac{1}{(1 + x_k)^2}$ ($0{,}25$ ; $0{,}44$ ; $0{,}36$ ; $0{,}39$…) oscillent autour de $0{,}382$, et leur produit vaut $\frac{1}{1\,156} \approx 0{,}00087$.

**Erreurs fréquentes.** Donner une seule dérivée en un coin. Inverser gauche et droite. En f), évaluer toutes les dérivées en $x_0 = 1$ (on trouve $-\frac{1}{4^7}$) au lieu de les évaluer le long de la trajectoire.

**Variante.** Avec trois copies : $x_3 = \frac35$, et la dérivée vaut $-\frac{1}{25}$ ($= -\frac{1}{5^2}$, avec $F_5 = 5$).

### Ex M17.7 — Une loi de Boltzmann à quatre niveaux d'énergie

**Réponses.** a) `0.3679` · b) `0.6572` · c) `0.4678` · d) `[0, 1.75]` · e) `1.7781` · f) `1.7372`.

**Démarche.** À $T = 1$ : poids $1$, $e^{-1} \approx 0{,}3679$, $e^{-2} \approx 0{,}1353$, $e^{-4} \approx 0{,}0183$, de somme $Z \approx 1{,}5215$. b) $\frac{1}{Z}$. c) $\frac{0{,}3679 + 2 \times 0{,}1353 + 4 \times 0{,}0183}{1{,}5215}$. d) Le niveau fondamental, puis la moyenne $\frac{0 + 1 + 2 + 4}{4}$. e) $p_1 = \frac{1}{Z(T)} = \frac12$ équivaut à $e^{-1/T} + e^{-2/T} + e^{-4/T} = 1$ ; le membre de gauche croît strictement de 0 (quand $T \to 0$) à 3 (quand $T \to \infty$) : une seule solution, par dichotomie entre 1 et 2, $T \approx 1{,}7781$. f) $\frac{p_4}{p_1} = e^{-4/T} = 0{,}1$, soit $T = \frac{4}{\ln 10}$.

Dans ta copie : quand $T$ grandit, le fondamental se vide au profit des niveaux hauts (la population d'un niveau intermédiaire peut monter puis redescendre), et l'énergie moyenne croît : on admet que sa dérivée par rapport à $T$ vaut $\frac{\mathbb{V}(E)}{T^2} \ge 0$, où $\mathbb{V}(E)$ est la variance de l'énergie sous la loi de Boltzmann. f) ne fait intervenir qu'un **rapport** de populations, où $Z$ se simplifie.

**Erreurs fréquentes.** Oublier de normaliser par $Z$. Écrire $e^{-E/T}$ avec $E \times T$. En e), chercher $p_1 = \frac12$ sans voir que $Z = 2$.

**Variante.** Niveaux $0$, $1$, $1$ (deux états de même énergie) : à $T = 1$, $p_1 = \frac{1}{1 + 2e^{-1}} \approx 0{,}5761$, et la température où le fondamental garde la moitié vérifie $2e^{-1/T} = 1$, soit $T = \frac{1}{\ln 2} \approx 1{,}4427$.

### Ex M17.11 — Le recuit simulé

**Réponses.** a) `0.3299` · b) `0.64` · c) `38.5112` · d) `0.8803` · e) `0.1353` · f) `1`.

**Démarche.** Écarts à la plus courte : $(3, 0, 7, 1, 2)$. a) $\frac{1}{e^{-0{,}75} + 1 + e^{-1{,}75} + e^{-0{,}25} + e^{-0{,}5}}$. b) $\frac{1}{e^{-3} + 1 + e^{-7} + e^{-1} + e^{-2}} \approx 0{,}6435$. c) $\sum_ip_iE_i$ avec les probabilités de $T = 1$. d) $P(B) + P(D) = \frac{1 + e^{-1}}{e^{-3} + 1 + e^{-7} + e^{-1} + e^{-2}}$ : deux tournées distinctes, des probabilités qui s'additionnent. e) $\Delta = 1$ : $e^{-1/0{,}5} = e^{-2}$. f) La tournée B est plus courte : acceptée toujours.

Dans ta copie : à $T = 1$, les poids $e^{-\ell}$ valent $e^{-38}$ fois $e^{-3}$, $1$, $e^{-7}$, $e^{-1}$ et $e^{-2}$ ; le facteur commun $e^{-38}$ apparaît aussi dans $Z$, et se simplifie dans chaque probabilité. La probabilité d'accepter une tournée plus longue de 1 km passe de $e^{-1} \approx 0{,}37$ à $e^{-2} \approx 0{,}14$ quand $T$ passe de 1 à 0,5 : plus on refroidit, plus le recuit devient exigeant. Accepter parfois une tournée plus longue permet de sortir d'un minimum local, au lieu d'y rester bloqué.

**Erreurs fréquentes.** Oublier la normalisation. En d), ne garder que $P(B)$. En e), prendre $e^{-\Delta T}$ ou $e^{-\Delta}$ sans la température. En f), appliquer la même formule à une tournée plus courte (elle donnerait $e^{2} > 1$).

**Variante.** À $T = 3$ : $P(B) \approx 0{,}3711$, et $P(B \text{ ou } D) \approx 0{,}637$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M17.8 — La règle de la chaîne à partir de l'approximation linéaire

**Démonstration.**
1. $\mathbf{k} = \mathbf{J}_{\mathbf{f}}\mathbf{h} + \boldsymbol{\varepsilon}_{\mathbf{f}}(\mathbf{h})\,\lVert\mathbf{h}\rVert$, donc $\lVert\mathbf{k}\rVert \le \lVert\mathbf{J}_{\mathbf{f}}\rVert_2\,\lVert\mathbf{h}\rVert + \lVert\boldsymbol{\varepsilon}_{\mathbf{f}}(\mathbf{h})\rVert\,\lVert\mathbf{h}\rVert$. Pour $\mathbf{h}$ assez petit, $\lVert\boldsymbol{\varepsilon}_{\mathbf{f}}(\mathbf{h})\rVert \le 1$, et $\lVert\mathbf{k}\rVert \le C\lVert\mathbf{h}\rVert$ avec $C = \lVert\mathbf{J}_{\mathbf{f}}\rVert_2 + 1$. En particulier, $\mathbf{k} \to \mathbf{0}$ quand $\mathbf{h} \to \mathbf{0}$.
2. $\mathbf{g}(\mathbf{y} + \mathbf{k}) = \mathbf{g}(\mathbf{y}) + \mathbf{J}_{\mathbf{g}}\mathbf{k} + \boldsymbol{\varepsilon}_{\mathbf{g}}(\mathbf{k})\,\lVert\mathbf{k}\rVert = \mathbf{g}(\mathbf{y}) + \mathbf{J}_{\mathbf{g}}\mathbf{J}_{\mathbf{f}}\mathbf{h} + \mathbf{J}_{\mathbf{g}}\boldsymbol{\varepsilon}_{\mathbf{f}}(\mathbf{h})\,\lVert\mathbf{h}\rVert + \boldsymbol{\varepsilon}_{\mathbf{g}}(\mathbf{k})\,\lVert\mathbf{k}\rVert$.
3. Le reste, divisé par $\lVert\mathbf{h}\rVert$, vaut $\mathbf{J}_{\mathbf{g}}\boldsymbol{\varepsilon}_{\mathbf{f}}(\mathbf{h}) + \boldsymbol{\varepsilon}_{\mathbf{g}}(\mathbf{k})\frac{\lVert\mathbf{k}\rVert}{\lVert\mathbf{h}\rVert}$. Le premier terme tend vers $\mathbf{0}$ ; le second est majoré en norme par $C\lVert\boldsymbol{\varepsilon}_{\mathbf{g}}(\mathbf{k})\rVert$, qui tend vers 0 puisque $\mathbf{k} \to \mathbf{0}$ (si $\mathbf{k} = \mathbf{0}$, ce terme est nul). Donc $\mathbf{g} \circ \mathbf{f}$ est différentiable en $\mathbf{x}$, de jacobienne $\mathbf{J}_{\mathbf{g}}(\mathbf{f}(\mathbf{x}))\,\mathbf{J}_{\mathbf{f}}(\mathbf{x})$ (la matrice d'une approximation linéaire est unique : appliquée à $t\mathbf{e}_j$, $t \to 0$, elle donne les dérivées partielles).
4. $\big(\mathbf{J}_{\mathbf{g}}\mathbf{J}_{\mathbf{f}}\big)_{ij} = \sum_{k=1}^{p}\frac{\partial g_i}{\partial y_k}\frac{\partial f_k}{\partial x_j}$ : l'effet de $x_j$ sur la sortie $i$ passe par chaque variable intermédiaire $y_k$ ; sur chaque chemin, les effets se multiplient ; les chemins s'additionnent.
5. Pour $n = p = m = 1$, les matrices sont des nombres : $(g \circ f)'(x) = g'(f(x))\,f'(x)$. Pour $m = 1$, $\mathbf{J}_{\mathbf{g}}$ est la ligne $\nabla_{\mathbf{y}}L$, et le produit est $\nabla_{\mathbf{y}}L\,\mathbf{J}_{\mathbf{f}}$.

**Grille de relecture.** La majoration $\lVert\mathbf{k}\rVert \le C\lVert\mathbf{h}\rVert$ est établie avant d'être utilisée (sans elle, $\boldsymbol{\varepsilon}_{\mathbf{g}}(\mathbf{k})\lVert\mathbf{k}\rVert$ n'est pas contrôlé). Le reste est **divisé** par $\lVert\mathbf{h}\rVert$ avant de passer à la limite. Le cas $\mathbf{k} = \mathbf{0}$ est vu. La formule par coefficients est interprétée.

**Variante.** Le même raisonnement, appliqué à trois applications, donne $\mathbf{J}_{\mathbf{f}_3}\mathbf{J}_{\mathbf{f}_2}\mathbf{J}_{\mathbf{f}_1}$ par récurrence sur le nombre d'étages.

### Ex M17.9 — Une fonction appliquée coordonnée par coordonnée a une jacobienne diagonale

**Démonstration.**
1. $f_i(\mathbf{x}) = g(x_i)$ ne dépend pas de $x_j$ pour $j \ne i$ : $\frac{\partial f_i}{\partial x_j} = 0$. Pour $j = i$, c'est la dérivée de $g$ en $x_i$. La matrice n'a de coefficients non nuls que sur la diagonale, $g'(x_i)$.
2. $(\mathbf{J}\mathbf{v})_i = \sum_jJ_{ij}v_j = g'(x_i)\,v_i$ : c'est $g'(\mathbf{x}) \odot \mathbf{v}$. De même $(\mathbf{u}^\top\mathbf{J})_j = \sum_iu_iJ_{ij} = u_j\,g'(x_j)$.
3. $n$ multiplications, contre $n^2$ pour une matrice pleine.
4. $\frac{f_i(\mathbf{x} + h\mathbf{1}) - f_i(\mathbf{x} - h\mathbf{1})}{2h} = \frac{g(x_i + h) - g(x_i - h)}{2h} = \frac12\Big(\frac{g(x_i + h) - g(x_i)}{h} + \frac{g(x_i) - g(x_i - h)}{h}\Big)$, et chacun des deux quotients tend vers $g'(x_i)$ : la coordonnée $i$ ne voit que le déplacement de $x_i$. Deux évaluations de $\mathbf{f}$ suffisent.
5. Pour $\mathbf{x} \mapsto \mathbf{A}\mathbf{x}$, le même calcul donne $\frac{\mathbf{A}(\mathbf{x} + h\mathbf{1}) - \mathbf{A}(\mathbf{x} - h\mathbf{1})}{2h} = \mathbf{A}\mathbf{1}$, la somme des colonnes : la coordonnée $i$ mélange les effets de toutes les entrées, et n'a aucune raison d'être $A_{ii}$ (elle peut l'être par hasard, si les autres coefficients de la ligne se compensent). Sans savoir que la jacobienne est diagonale, on ne peut donc pas se fier au raccourci ; quand elle l'est, il est exact (point 4).

**Grille de relecture.** Les deux cas $j \ne i$ et $j = i$ sont traités. Le produit est écrit coordonnée par coordonnée. L'argument du point 4 dit **pourquoi** les autres déplacements n'interviennent pas, et justifie la limite du quotient centré. Le calcul sur $\mathbf{A}$ est fait.

**Variante.** Pour $\mathbf{f}(\mathbf{x}) = \mathbf{x} \odot \mathbf{a}$ ($\mathbf{a}$ fixe), $\mathbf{J} = \mathrm{diag}(\mathbf{a})$, constante.

### Ex M17.10 — diag(p) − pᵀp est la covariance d'un vecteur one-hot

**Démonstration.**
1. $Y_i$ vaut 1 si $I = i$, avec la probabilité $p_i$, et 0 sinon : $\mathbb{E}[Y_i] = p_i$. $Y_i^2 = Y_i$, donc $\mathbb{E}[Y_i^2] = p_i$. Pour $i \ne j$, $Y_iY_j = 0$ toujours (un seul état à la fois), donc $\mathbb{E}[Y_iY_j] = 0$.
2. $\mathrm{Cov}(Y_i, Y_j) = \mathbb{E}[Y_iY_j] - \mathbb{E}[Y_i]\,\mathbb{E}[Y_j]$ vaut $p_i - p_i^2$ si $i = j$ et $-p_ip_j$ sinon : c'est le coefficient $(i, j)$ de $\mathrm{diag}(\mathbf{p}) - \mathbf{p}^\top\mathbf{p}$ (avec $\mathbf{p}$ en ligne, $(\mathbf{p}^\top\mathbf{p})_{ij} = p_ip_j$).
3. $\mathrm{Cov}(Y_i, Y_j) = \mathrm{Cov}(Y_j, Y_i)$ : symétrique. Pour toute ligne $\mathbf{v}$, $\mathbf{v}\,\mathrm{Cov}(\mathbf{Y})\,\mathbf{v}^\top = \sum_{i,j}v_iv_j\,\mathrm{Cov}(Y_i, Y_j) = \mathbb{V}(\mathbf{v} \cdot \mathbf{Y}) \ge 0$ (M02c) : semi-définie positive.
4. $\sum_jY_j = 1$, une constante. La somme de la ligne $i$ est $\sum_j\mathrm{Cov}(Y_i, Y_j) = \mathrm{Cov}\big(Y_i, \sum_jY_j\big) = \mathrm{Cov}(Y_i, 1) = 0$. La matrice annule $\mathbf{1}^\top$, qui n'est pas nul : elle n'est pas inversible.
5. Pour $\mathbf{p} = (\frac13, \frac13, \frac13)$ : $\frac29$ sur la diagonale ($\frac13 \times \frac23$) et $-\frac19$ ailleurs, soit $\frac13\mathbf{I} - \frac19\mathbf{1}^\top\mathbf{1}$ (la matrice $\mathbf{1}^\top\mathbf{1}$ est pleine de 1). Elle envoie $\mathbf{1}^\top$ sur $\frac13\mathbf{1}^\top - \frac39\mathbf{1}^\top = \mathbf{0}$ : valeur propre 0. Pour $\mathbf{v}$ orthogonal à $\mathbf{1}$, $\mathbf{1}^\top\mathbf{1}\,\mathbf{v}^\top = \mathbf{0}$, donc la matrice envoie $\mathbf{v}^\top$ sur $\frac13\mathbf{v}^\top$ : valeur propre $\frac13$, sur un plan. Valeurs propres : $0$, $\frac13$, $\frac13$.

**Grille de relecture.** $Y_iY_j = 0$ pour $i \ne j$ est justifié (un seul état). La semi-définie positivité passe par une **variance**, pas par un calcul de valeurs propres. La somme des lignes se déduit de $\sum_jY_j$ constant, sans développer la matrice. Au point 5, les vecteurs propres sont trouvés sans polynôme caractéristique.

**Variante.** Pour $\mathbf{p} = (0{,}5 ;\ 0{,}25 ;\ 0{,}25)$ : $\begin{pmatrix} 0{,}25 & -0{,}125 & -0{,}125 \\ -0{,}125 & 0{,}1875 & -0{,}0625 \\ -0{,}125 & -0{,}0625 & 0{,}1875 \end{pmatrix}$, de lignes de somme nulle.

<a id="reflexion"></a>

## 📖 🗣️ Lecture et explication

### Ex M17.12 — MML §5.3

**Ce qu'il faut avoir relevé.**
1. MML appelle jacobienne (*Jacobian*) la collection de toutes les dérivées partielles du premier ordre d'une fonction à valeurs vectorielles $\mathbf{f} : \mathbb{R}^n \to \mathbb{R}^m$, rangées dans une matrice $m \times n$ dont la ligne $i$ est le gradient de $f_i$. Le livre nomme cette disposition le *numerator layout* : c'est celle de la fiche (une ligne par sortie, une colonne par entrée).
2. MML note la jacobienne $\mathbf{J} = \nabla_{\mathbf{x}}\mathbf{f} = \frac{\mathrm{d}\mathbf{f}(\mathbf{x})}{\mathrm{d}\mathbf{x}}$, et la dérivée d'une fonction réelle par rapport à un vecteur est, chez lui, une **ligne** (le cas $m = 1$), comme en M05b.
3. MML explique que la valeur absolue du déterminant de la jacobienne est le facteur par lequel une transformation (un changement de variables) multiplie les aires ou les volumes : c'est le §1 de la fiche ; en ✏️ M17.1, ce facteur vaut $r$.
4. Toute dérivée de composée de la section se réécrit comme au §3 : le produit des jacobiennes, la dernière application à gauche, chacune évaluée au point intermédiaire, avec les formes qui s'enchaînent.
5. Par exemple : *vector-valued function* (application à valeurs vectorielles), *Jacobian determinant* (déterminant de la jacobienne), *numerator layout* (une ligne par sortie), *chain rule* (règle de la chaîne).

**Grille.** La forme $(m, n)$ et le nom de la disposition ; la ligne pour le gradient ; le rôle du déterminant ; un exemple refait avec les formes.

### Ex M17.13 — Expliquer la règle de la chaîne avec des taux de change

**Réponse modèle (6 à 10 phrases).** Suis ton euro de plus : une partie devient des francs suisses, l'autre des livres, selon la répartition et les taux de la première étape. Ces francs et ces livres deviennent ensuite des yens, selon les taux de la deuxième étape. Le long d'un même chemin, par exemple de l'euro au franc puis du franc au yen, les taux se multiplient : ce que rapporte un euro par ce chemin est le produit des deux taux. Ton euro passe à la fois par le franc et par la livre, et les yens obtenus par les deux chemins s'additionnent. Le tableau de tous les taux d'une étape, avec une ligne par monnaie d'arrivée et une colonne par monnaie de départ, est une jacobienne. Le tableau d'un bout à l'autre s'obtient en multipliant les deux tableaux, la dernière étape à gauche. Les taux à utiliser sont ceux du jour, au moment où l'on change, comme une jacobienne s'évalue au point où l'on est. Si les taux dépendaient du montant changé, il faudrait les prendre au montant atteint à chaque étape, et la réponse ne vaudrait que pour un petit euro de plus, comme une dérivée.

**En 3 phrases.** Le long d'un chemin de change, les taux se multiplient. D'un chemin à l'autre, les gains s'additionnent. Le tableau des taux d'un bout à l'autre est le produit des tableaux de chaque étape, comme la jacobienne d'une composée.

**Grille.** La multiplication le long d'un chemin ; l'addition entre les chemins ; les tableaux de taux comme jacobiennes et leur produit ; le point d'évaluation (les taux du jour, au montant atteint).

<a id="entretien"></a>

## 💼 Entretien

### M17.E1 — « Qu'est-ce qu'une jacobienne ? Donne un exemple hors du machine learning. »

**Réponse modèle (60 secondes).** « La jacobienne d'une application qui prend $n$ nombres et en rend $m$ est la matrice $m \times n$ de ses dérivées partielles : une ligne par sortie, une colonne par entrée. Elle donne la meilleure approximation linéaire de l'application près d'un point : un petit déplacement $\mathbf{h}$ des entrées déplace les sorties d'environ $\mathbf{J}\mathbf{h}$. Exemple : le passage des coordonnées polaires $(r, \theta)$ aux coordonnées cartésiennes $(x, y)$, qu'utilise un radar ou un GPS ; sa jacobienne a pour colonnes la direction radiale et la direction tangente, et son déterminant vaut $r$ : un petit rectangle $\mathrm{d}r \times \mathrm{d}\theta$ devient une petite figure d'aire environ $r\,\mathrm{d}r\,\mathrm{d}\theta$, ce qui explique le facteur $r$ des intégrales en coordonnées polaires. Pour une composée, les jacobiennes se multiplient : c'est la règle de la chaîne. Enfin, on évite souvent de la former, car elle a $mn$ coefficients : on calcule son produit par un vecteur, qui dit comment toutes les sorties bougent dans une direction donnée, pour le prix de quelques évaluations. »

**Grille.** La définition et la forme ; l'approximation linéaire ; un exemple concret hors du machine learning, avec le sens du déterminant ; la composition ; le produit par un vecteur et son coût.

<a id="notebook"></a>

## Notebook

Le code complet est dans `05_solutions.ipynb`, exécuté ; voici les réponses et ce qu'il faut en retenir.
