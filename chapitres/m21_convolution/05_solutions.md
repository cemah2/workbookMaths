# M21 · Convolution, matrices de Toeplitz et équivariance — solutions

> À lire **après** avoir cherché (et ouvert les indices de `04_indices.md`). Pour chaque exercice : les réponses, la démarche, les erreurs fréquentes et une variante ; pour une démonstration, une rédaction modèle et une grille de relecture. Les exercices du notebook sont corrigés dans `05_solutions.ipynb` ; leur résumé est à la fin.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M21.Q1 — Convolution ou corrélation : retourner, glisser, sommer
1. $(5, -1, 0, 2)$ : les mêmes coefficients, dans l'ordre inverse.
2. Vrai : $(-3, 0, 3)$ est antisymétrique, son retourné est $(3, 0, -3)$, son opposé.
3. $a_0b_4$, $a_1b_3$ et $a_2b_2$ : les couples $(i, 4 - i)$ dont les deux indices existent.
4. $7 + 4 - 1 = 10$.
5. `np.correlate` reçoit les poids dans l'ordre de la fenêtre, $(3, 1, -1)$ ; `np.convolve` retourne le noyau, il faut donc lui donner $(-1, 1, 3)$.
6. Vrai : c'est le lien du §2, $(\mathbf{w} \star \mathbf{x})_i = (\mathbf{x} * \tilde{\mathbf{w}})_{i+k-1}$, et les indices $k - 1$ à $n - 1$ de la convolution pleine forment le mode valide.

### M21.Q2 — Les propriétés de la convolution : vrai ou faux
1. Vrai.
2. $(2 - 1 + 3) \times (1 + 4) = 4 \times 5 = 20$ : la somme d'une convolution est le produit des sommes (évaluer les polynômes en $X = 1$).
3. Vrai : la convolution est linéaire par rapport à chaque suite.
4. Vrai : les termes restent positifs ou nuls, et leur somme vaut $1 \times 1$.
5. Faux : $(\mathbf{a} * (0, 0, 1))_m = a_{m-2}$, le signal est **retardé** de 2 cases (poussé vers la droite).
6. $5 \times (0{,}5 + 2 - 1) = 7{,}5$ : chaque valeur complète vaut la constante fois la somme du noyau.

### M21.Q3 — Lire une matrice de Toeplitz : diagonales, coefficients non nuls, nombre de lignes
1. $\mathbf{w} = (5, -2, 1)$, la première colonne lue jusqu'au dernier coefficient non nul, et $n = 3$, le nombre de colonnes ($3 + 3 - 1 = 5$ lignes).
2. $nk = 50 \times 4 = 200$ coefficients non nuls, sur $(50 + 4 - 1) \times 50 = 2\,650$ : environ 7,5 %.
3. $n - k + 1 = 47$ lignes en mode valide, $n = 50$ en mode même taille.
4. Faux : la diagonale sous la diagonale principale contient 1 puis 2.
5. Vrai : chaque colonne est la précédente descendue d'une case, la dernière case remontant en haut ; première colonne $(1, 0, 2)$, c'est $\operatorname{circ}(1, 0, 2)$.
6. $T_{7,4} = w_{7-4} = w_3$.

### M21.Q4 — Équivariant, invariant, ou ni l'un ni l'autre ? Décalages, bords, pas et pooling
1. Équivariante : c'est une convolution.
2. Invariante : décaler le signal ne change pas l'ensemble de ses valeurs.
3. Ni l'un ni l'autre : un même motif est multiplié par des nombres différents selon sa place.
4. Invariante : la même somme, dans un autre ordre.
5. Un décalage de 6 cases décale la sortie de 2 cases ; un décalage de 2 cases ne donne pas, en général, un décalage de la sortie : on lit alors les valeurs $x_{3i-2}$, que la sortie d'origine ne contenait pas.
6. Vrai : sur un cercle, rien ne sort par un bout (fiche §4, $\operatorname{circ}(\mathbf{h})\,\mathbf{P} = \mathbf{P}\operatorname{circ}(\mathbf{h})$).

### M21.Q5 — Combien de positions ? Pas, dilatation, padding et insertion de zéros
1. $40 - 5 + 1 = 36$.
2. $\lfloor\frac{41 - 5}{2}\rfloor + 1 = 18 + 1 = 19$.
3. Étendue $4 \times 2 + 1 = 9$, et $41 - 9 + 1 = 33$ positions.
4. $\frac{11 - 1}{2} = 5$ zéros de chaque côté.
5. $(6 - 1) \times 4 + 1 = 21$ valeurs.
6. Faux : $\lfloor\frac{25}{4}\rfloor + 1 = 7$ fenêtres, qui commencent en $0, 4, \ldots, 24$ ; la dernière couvre les cases 24 à 28, et la case 29 n'est jamais lue.

### M21.Q6 — Canaux, groupes, convolution 1 × 1 et noyaux séparables : compter
1. $(6, 10, 2, 4)$ ; $6 \times (10 \times 8 + 1) = 486$ paramètres.
2. $6 \times (5 \times 8 + 1) = 246$ : chaque sortie ne lit que les 5 canaux de son groupe.
3. $10 \times (9 + 1) = 100$.
4. $6 \times (10 + 1) = 66$ ; non : elle mélange les canaux d'une même case, sans regarder les cases voisines.
5. $81$ en direct, environ $9 + 9 = 18$ en deux passes (la passe intermédiaire se calcule sur un peu plus de valeurs que la sortie).
6. Vrai : la seconde ligne vaut $-\frac12$ fois la première ; c'est $(2, -1)^\top(1, -2, 3)$.

### M21.Q7 — Composer des convolutions : noyau, pas et champ récepteur
1. $5 + 8 - 1 = 12$.
2. $(3, 1) * (1, -2) = (3, -6 + 1, -2) = (3, -5, -2)$ : le noyau équivalent est la convolution des deux noyaux, sans retournement.
3. $2 \times 2 \times 5 = 20$.
4. $1 + 1 + 1 \times 2 + 1 \times 4 = 8$.
5. $1 + 3 + 5 \times 2 \times 1 = 14$.
6. Faux : $(6, 2)$ puis $(3, 1)$ donne $1 + 5 + 2 \times 2 = 10$ ; $(3, 1)$ puis $(6, 2)$ donne $1 + 2 + 5 \times 1 = 8$. Un pas multiplie les contributions des étages **suivants**.

### M21.Q8 — Le pire cas d'une perturbation bornée : quelle norme, quel vecteur ?
1. $0{,}3 \times \lVert\mathbf{g}\rVert_1 = 0{,}3 \times 9 = 2{,}7$.
2. $\boldsymbol{\delta} = 0{,}3\,(1, -1, 1, t, -1)$, pour n'importe quel $t \in [-1, 1]$ : la coordonnée où $g_i = 0$ ne compte pas, donc le vecteur n'est pas unique.
3. $0{,}3 \times \lVert\mathbf{g}\rVert_2 = 0{,}3 \times \sqrt{25} = 1{,}5$.
4. $0{,}3 \times \lVert\mathbf{g}\rVert_\infty = 0{,}3 \times 4 = 1{,}2$ : toute l'erreur sur la mesure du plus grand poids, $\boldsymbol{\delta} = (0 ;\ -0{,}3 ;\ 0 ;\ 0 ;\ 0)$.
5. Faux : $0{,}3 \times (-4) = -1{,}2$ sort de la boule, dont les coordonnées restent dans $[-0{,}3 ;\ 0{,}3]$.
6. $0{,}3\sqrt{400} = 6$.

<a id="rappels"></a>

## 🔁 Rappels

### M21.R1 — La moyenne mobile d'une suite (R5)
1. $(8, 6, 5, 7)$ : $\frac{24}{3}$, $\frac{18}{3}$, $\frac{15}{3}$, $\frac{21}{3}$.
2. $n - k + 1$.
3. Les deux moyennes ont en commun $x_{t-1}$ et $x_t$ : il reste $\frac{x_{t+1} - x_{t-2}}{3}$. Ici $\frac{6 - 12}{3} = -2 = 6 - 8$.
4. $\mathbf{h} = (\frac13, \frac13, \frac13)$ : la somme $\sum_i x_i\,h_{t-i}$ ne garde que $i = t - 2, t - 1, t$.
5. Vrai : le noyau a pour somme 1.

### M21.R2 — La matrice d'une application linéaire, son noyau et son rang (M12a)
1. $\begin{pmatrix} 1 & 2 & -1 \\ 0 & 3 & 1 \end{pmatrix}$.
2. 2 : les deux lignes ne sont pas proportionnelles.
3. $3 - 2 = 1$.
4. $(5, -1, 3)$ : $3y + z = 0$ donne $z = -3y$, puis $x = -2y + z = -5y$ ; avec $y = -1$.
5. L'image du $j$-ième vecteur de la base canonique, $\mathbf{e}_j$.
6. Vrai : le rang vaut au plus 2, donc le noyau est de dimension au moins $4 - 2 = 2$.

### M21.R3 — Le rang d'un produit extérieur u vᵀ et la décomposition en valeurs singulières (M12d)
1. $\begin{pmatrix} 8 & 0 & -6 \\ 4 & 0 & -3 \\ -8 & 0 & 6 \end{pmatrix}$.
2. 1 : toutes les lignes sont des multiples de $\mathbf{v}^\top$.
3. $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert = 3 \times 5 = 15$.
4. $\frac13(2, 1, -2)$ et $\frac15(4, 0, -3)$ : $\mathbf{u}\mathbf{v}^\top = 15\,\frac{\mathbf{u}}{3}\,\frac{\mathbf{v}^\top}{5}$.
5. Vrai : si chaque ligne vaut $c_i\,\mathbf{r}$, la matrice est $\mathbf{c}\,\mathbf{r}$, de rang 1 (une ligne non nulle au moins).
6. $\sqrt{0{,}002^2 + 0^2} = 0{,}002$ : la racine de la somme des carrés des valeurs singulières oubliées.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M21.1 — Deux dés truqués et un produit de polynômes : la même convolution

**Réponses.** a) `[3, 5, 9, 17, 10, 4]` · b) `"17/48"` · c) `"7/24"` · d) `"115/24"` · e) `3` · f) `5` · g) `"11/144"`.

**Démarche.** a) Le tableau des produits $a_ib_j$, avec $\mathbf{a} = (3, 2, 1)$ et $\mathbf{b} = (1, 1, 2, 4)$ :

| | $b_0 = 1$ | $b_1 = 1$ | $b_2 = 2$ | $b_3 = 4$ |
|---|---|---|---|---|
| $a_0 = 3$ | 3 | 3 | 6 | 12 |
| $a_1 = 2$ | 2 | 2 | 4 | 8 |
| $a_2 = 1$ | 1 | 1 | 2 | 4 |

Le long des anti-diagonales : $3$ ; $3 + 2 = 5$ ; $6 + 2 + 1 = 9$ ; $12 + 4 + 1 = 17$ ; $8 + 2 = 10$ ; $4$. b) $P(A = i)\,P(B = j) = \frac{a_{i-1}}{6}\cdot\frac{b_{j-1}}{8}$, et $S = i + j = m + 2$ avec $m = (i - 1) + (j - 1)$ : $P(S = m + 2) = \frac{c_m}{48}$, où $\mathbf{c}$ est la suite de a). $P(S = 5) = \frac{c_3}{48} = \frac{17}{48}$. c) $\frac{c_4 + c_5}{48} = \frac{14}{48} = \frac{7}{24}$. d) $\frac{2 \times 3 + 3 \times 5 + 4 \times 9 + 5 \times 17 + 6 \times 10 + 7 \times 4}{48} = \frac{230}{48} = \frac{115}{24} \approx 4{,}79$. e) $m = 5 - 2 = 3$. f) Le plus grand coefficient, 17, est en $m = 3$ : $S = 5$. g) La loi de $A + B + A'$ est $\mathbf{c} * \mathbf{a}$, divisée par $48 \times 6 = 288$ (l'associativité : $(\mathbf{a} * \mathbf{b}) * \mathbf{a}$). $T = A + B + A' = m + 3$ ; $T = 9$ et $T = 10$ correspondent à $m = 6$ et $m = 7$ : $c_4a_2 + c_5a_1 = 10 + 8 = 18$ et $c_5a_2 = 4$, d'où $\frac{22}{288} = \frac{11}{144}$.

Dans ta copie : la somme des coefficients de a) est la valeur du produit en $X = 1$, $(3 + 2 + 1)(1 + 1 + 2 + 4) = 6 \times 8 = 48$. Les numéros des faces commencent à 1, les indices des suites à 0 : chaque dé décale d'une case, d'où le décalage de 2. $\mathbb{E}[A] = \frac{3 + 4 + 3}{6} = \frac53$ et $\mathbb{E}[B] = \frac{1 + 2 + 6 + 16}{8} = \frac{25}{8}$, de somme $\frac{40 + 75}{24} = \frac{115}{24}$.

**Erreurs fréquentes.** Lire $P(S = 5)$ sur le coefficient d'indice 5 ($\frac{4}{48} = \frac1{12}$) ou 4 ($\frac{10}{48} = \frac5{24}$) : l'indice n'est pas la valeur. Calculer l'espérance de l'indice $m$, $\frac{67}{24}$, en oubliant le $+2$. Inclure $S = 5$ dans c) ($\frac{31}{48}$). Oublier $T = 10$ en g) ($\frac{18}{288} = \frac1{16}$). Faire glisser $\mathbf{b}$ sans le retourner (une corrélation), ce qui donne $(12, 14, 11, 7, 3, 1)$ en a).

**Variante.** Avec un dé $B$ équilibré à quatre faces : $(3, 2, 1) * (1, 1, 1, 1) = (3, 5, 6, 6, 3, 1)$, sur 24 ; $P(S = 5) = \frac{6}{24} = \frac14$, autant que $P(S = 4)$.

### Ex M21.2 — Convoluer et corréler un signal à la main, dans les trois modes

**Réponses.** a) `[14, 2, -3, 11, 12]` · b) `[12, -11, 8, 16, -1, -7, 14, -10, 4]` · c) `[8, 16, -1, -7, 14]` · d) `[-11, 8, 16, -1, -7, 14, -10]` · e) `[2, -1, 4]` · f) `False` · g) `25`.

**Démarche.** a) La fenêtre $i$ couvre $x_i, x_{i+1}, x_{i+2}$ : $4 \times 3 + (-1)(-2) + 2 \times 0 = 14$ ; $-8 + 0 + 10 = 2$ ; $0 - 5 + 2 = -3$ ; $20 - 1 - 8 = 11$ ; $4 + 4 + 4 = 12$. b) $(\mathbf{x} * \mathbf{w})_m = \sum_i x_i\,w_{m-i}$ : $12$ ; $-3 - 8 = -11$ ; $6 + 2 + 0 = 8$ ; $-4 + 0 + 20 = 16$ ; $0 - 5 + 4 = -1$ ; $10 - 1 - 16 = -7$ ; $2 + 4 + 8 = 14$ ; $-8 - 2 = -10$ ; $4$. c) Les indices $k - 1 = 2$ à $n - 1 = 6$ de b). d) $n = 7$ valeurs à partir de l'indice $\lfloor\frac{3 - 1}{2}\rfloor = 1$. e) Le noyau retourné, $\tilde{\mathbf{w}} = (2, -1, 4)$. f) Faux. g) $(3 - 2 + 0 + 5 + 1 - 4 + 2) \times (4 - 1 + 2) = 5 \times 5 = 25$.

Dans ta copie : la première valeur de c) pose $(2, -1, 4)$ sous $(3, -2, 0)$ : $6 + 2 + 0 = 8$. Avec $k = 3$, le mode même taille ajoute un zéro de chaque côté (vu comme une corrélation par $\tilde{\mathbf{w}}$), et la fenêtre est centrée : d) commence à l'indice 1 de b). a) = c) pour tout signal exactement quand $\tilde{\mathbf{w}} = \mathbf{w}$, c'est-à-dire $w_0 = w_2$ : les noyaux symétriques.

**Erreurs fréquentes.** Ne pas retourner le noyau (c) égal à a)). Commencer d) à l'indice 0, `[12, -11, 8, 16, -1, -7, 14]`, ou à l'indice 2, `[8, 16, -1, -7, 14, -10, 4]`. Donner $\mathbf{w}$ lui-même en e). En b), oublier un produit sur une anti-diagonale.

**Variante.** Avec le noyau antisymétrique $(2, 0, -2)$ : $\mathbf{w} \star \mathbf{x} = (6, -14, -2, 18, -2)$, et la convolution valide en est l'opposée.

### Ex M21.3 — Des pochoirs de différences finies : dérivée et dérivée seconde d'un signal échantillonné

**Réponses.** a) `[1, 7, 19, 37, 61]` · b) `[4, 13, 28, 49]` · c) `[3, 6, 9, 12]` · d) `1` · e) `[4, 0.25]` · f) `False` · g) `0.25`.

**Démarche.** a) $\frac{2 - 0}{2}$, $\frac{16 - 2}{2}$, $\frac{54 - 16}{2}$, $\frac{128 - 54}{2}$, $\frac{250 - 128}{2}$. b) $\frac{16 - 0}{4}$, $\frac{54 - 2}{4}$, $\frac{128 - 16}{4}$, $\frac{250 - 54}{4}$. c) $\frac{16 - 4 + 0}{4}$, $\frac{54 - 32 + 2}{4}$, $\frac{128 - 108 + 16}{4}$, $\frac{250 - 256 + 54}{4}$. d) $f'(t) = \frac{3t^2}{4}$, $f'(4) = 12$ : $13 - 12 = 1$. e) $f'(2) = 3$ et $f'(3) = 6{,}75$ : $7 - 3 = 4$, puis $7 - 6{,}75 = 0{,}25$. f) Faux : `np.convolve` retourne les poids, et calcule $f_{i-1} - f_{i+1}$ : il donne $-$b). g) L'erreur de la différence centrée vaut $\frac{h^2}{6}f'''$, avec $f''' = \frac32$ : $\frac{h^2}{4}$, soit 1 pour $h = 2$ (c'est d)) et $0{,}25$ pour $h = 1$.

Dans ta copie : $f''(t) = \frac{3t}{2}$ vaut 3, 6, 9 et 12 aux instants 2 à 8 : c) est exact, car l'erreur de la dérivée seconde, $\frac{h^2}{12}f''''$, est nulle pour un polynôme de degré 3 ; celle de la différence centrée fait intervenir $f''' \ne 0$. Diviser $h$ par 2 divise l'erreur par 4 : l'ordre 2. e) La différence avant approche $f'$ au milieu de son intervalle avec une erreur d'ordre 2 ($\frac{h^2}{24}f''' = 0{,}25$), et au bord avec une erreur d'ordre 1. Comme corrélations : $\frac1h(-1, 1)$, $\frac1{2h}(-1, 0, 1)$ et $\frac1{h^2}(1, -2, 1)$ ; pour `np.convolve`, les poids retournés : $\frac1h(1, -1)$, les poids opposés $-\frac1{2h}(-1, 0, 1)$, et $\frac1{h^2}(1, -2, 1)$, inchangé car symétrique.

**Erreurs fréquentes.** Oublier de diviser par $h$ (`[2, 14, 38, 74, 122]` en a)), diviser par $h$ au lieu de $2h$ en b) (`[8, 26, 56, 98]`) ou par $h$ au lieu de $h^2$ en c) (`[6, 12, 18, 24]`). Écrire l'erreur comme $f'(4) - 13 = -1$. Croire l'erreur proportionnelle à $h$ (g) $= 0{,}5$).

**Variante.** Une cuve de volume $3t^2$, relevé chaque minute : $(0, 3, 12, 27, 48)$ ; les différences centrées $(6, 12, 18)$ valent exactement $f'(t) = 6t$ en $t = 1, 2, 3$ (sur une parabole, $f''' = 0$).

### Ex M21.4 — La matrice de Toeplitz d'une convolution pleine et d'une convolution valide : coefficients non nuls, rang et noyau

**Réponses.** a) `[[1, 0, 0, 0, 0], [-3, 1, 0, 0, 0], [2, -3, 1, 0, 0], [0, 2, -3, 1, 0], [0, 0, 2, -3, 1], [0, 0, 0, 2, -3], [0, 0, 0, 0, 2]]` · b) `15` · c) `[2, -6, 3, 6, -10, 3, 2]` · d) `[[2, -3, 1, 0, 0], [0, 2, -3, 1, 0], [0, 0, 2, -3, 1]]` · e) `3` · f) `2` · g) `True` · h) `5` · i) `[2, -3, 1]`.

**Démarche.** a) La colonne $j$ est le noyau descendu de $j$ lignes, $T_{ij} = w_{i-j}$ ; forme $(7, 5)$. b) $nk = 5 \times 3$. c) $(2 - X^2 + 3X^3 + X^4)(1 - 3X + 2X^2) = 2 - 6X + 3X^2 + 6X^3 - 10X^4 + 3X^5 + 2X^6$. d) Les lignes $k - 1 = 2$ à $n - 1 = 4$ de $\mathbf{T}$. e) Les trois lignes sont échelonnées (chacune a son premier coefficient non nul, 2, plus à droite que la précédente) : rang 3. f) Théorème du rang : $5 - 3 = 2$. g) $2 - 6 + 4 = 0$, $4 - 12 + 8 = 0$, $8 - 24 + 16 = 0$. h) Les colonnes de $\mathbf{T}$ sont échelonnées de même (la colonne $j$ commence en ligne $j$ par $w_0 = 1$) : rang 5. i) Par l'énoncé du §3, $\mathbf{V}^\top$ est la matrice de la convolution pleine par $\tilde{\mathbf{w}} = (2, -3, 1)$, sur des signaux de longueur $n - k + 1 = 3$ : ses colonnes sont $(2, -3, 1)$ descendu de 0, 1 et 2 lignes.

Dans ta copie : $(\mathbf{V}\mathbf{x})_r = 2x_r - 3x_{r+1} + x_{r+2} = 0$, soit $x_{r+2} = 3x_{r+1} - 2x_r$, de polynôme $q^2 - 3q + 2 = (q - 1)(q - 2)$ : $x_i = \alpha + \beta\,2^i$. Le filtre ne voit ni les signaux constants ni les signaux géométriques de raison 2 ; une base de $\ker\mathbf{V}$ : $(1, 1, 1, 1, 1)$ et $(1, 2, 4, 8, 16)$. h) Le noyau de $\mathbf{T}$ est réduit à $\{\mathbf{0}\}$ : deux signaux différents ont des convolutions pleines différentes (constaté ici ; c'est vrai pour tout noyau non nul).

**Erreurs fréquentes.** Prendre les trois premières lignes de $\mathbf{T}$ pour $\mathbf{V}$. Répondre $\mathbf{w}$ lui-même en i), `[1, -3, 2]`. Calculer c) avec le noyau retourné (`[4, -6, 0, 9, -8, 0, 1]`). Confondre le rang et la dimension du noyau (3 en f)).

**Variante.** Avec le noyau retourné $(2, -3, 1)$, $\ker\mathbf{V}$ est engendré par $(1, 1, 1, 1, 1)$ et $(16, 8, 4, 2, 1)$ : le retourné de la suite géométrique.

### Ex M21.5 — Décaler puis filtrer, ou filtrer puis décaler : l'équivariance, ses bords et son pas

**Réponses.** a) `[4, -4, 9, -4, 3, 0, 0, 0]` · b) `[0, 0, 0, 4, -4, 9, -4, 3]` · c) `2` · d) `[4, 9, 3, 0]` · e) `[0, -4, -4, 0]` · f) `2` · g) `False`.

**Démarche.** a) $y_i = x_i - x_{i+1} + 2x_{i+2}$ : $0 - 0 + 4 = 4$ ; $0 - 2 - 2 = -4$ ; $2 + 1 + 6 = 9$ ; $-1 - 3 + 0 = -4$ ; $3 - 0 + 0 = 3$ ; puis des zéros. b) a) décalé de 3 cases. c) $\tau_5\mathbf{x} = (0, 0, 0, 0, 0, 0, 0, 2, -1, 3)$ donne $(0, 0, 0, 0, 0, 4, -4, 9)$ : les valeurs $-4$ et $3$, qui tomberaient aux positions 8 et 9, n'existent pas (il n'y a que $10 - 3 + 1 = 8$ positions). d) $y_i$ est la valeur $2i$ de a) : $(4, 9, 3, 0)$. e) $\mathbf{w} \star \tau_1\mathbf{x}$ est a) décalé d'une case, $(0, 4, -4, 9, -4, 3, 0, 0)$, dont on garde les valeurs paires : $(0, -4, -4, 0)$, les valeurs impaires de a). f) $\tau_4$ décale a) de 4 cases ; ses valeurs paires sont $(0, 0, 4, 9)$, d) décalé de 2 cases. g) Faux.

Dans ta copie : décaler l'entrée de $t$ cases décale la réponse de $t$ cases, tant que la réponse reste dans les positions qui existent. Avec un pas de 2, un décalage pair $t$ décale la sortie de $\frac t2$ ; un décalage impair fait lire l'autre moitié des valeurs de a), qui n'ont rien à voir avec d).

**Erreurs fréquentes.** Calculer a) avec `np.convolve` sans retourner les poids (`[2, -3, 8, -5, 6, 0, 0, 0]`). Garder les valeurs impaires de a) en d) (`[-4, -4, 0, 0]`). Répondre d) décalé, `[0, 4, 9, 3]`, en e). Répondre 4 en f) (le décalage de l'entrée, pas celui de la sortie).

**Variante.** Avec un pas de 3 : $\mathbf{x}$ donne $(4, -4, 0)$ et $\tau_3\mathbf{x}$ donne $(0, 4, -4)$, décalé d'une case.

### Ex M21.6 — Compter les positions d'une fenêtre : pas, dilatation, padding, « même taille » avec un pas, et le problème inverse

**Réponses.** a) `994` · b) `333` · c) `976` · d) `197` · e) `122` · f) `[2, 3]` · g) `[250, 251, 252, 253, 254]` · h) `10`.

**Démarche.** a) $1\,000 - 7 + 1$. b) $\lfloor\frac{1\,000 + 4 - 6 - 1}{3}\rfloor + 1 = \lfloor 332{,}33\rfloor + 1$. c) Étendue $4 \times 6 + 1 = 25$ : $1\,000 - 25 + 1$. d) $\lfloor\frac{1\,000 + 6 - 24 - 1}{5}\rfloor + 1 = \lfloor 196{,}2\rfloor + 1$. e) $\lceil\frac{365}{3}\rceil = \lceil 121{,}67\rceil$. f) $P_{\text{tot}} = (122 - 1) \times 3 + 6 + 1 - 365 = 5$ zéros en tout : $\lfloor\frac52\rfloor = 2$ au début, 3 à la fin. g) $\lfloor\frac{n - 5}{5}\rfloor + 1 = 50$ équivaut à $245 \le n - 5 \le 249$. h) $\lfloor\frac{993}{s}\rfloor + 1 = 100$ équivaut à $99 \le \frac{993}{s} < 100$, soit $9{,}93 < s \le 10{,}03$ : $s = 10$.

Dans ta copie : b) la dernière fenêtre, numéro 332, lit les cases 996 à 1 002 du signal complété, de longueur 1 004 ; avec $\hat x_j = x_{j-2}$, ce sont $x_{994}$ à $x_{1\,000}$, et $x_{1\,000}$ n'existe pas : c'est le premier des deux zéros de fin. e) $\lfloor\frac{365 + 5 - 6 - 1}{3}\rfloor + 1 = 121 + 1 = 122$. g) Les $s$ longueurs consécutives qu'une partie entière confond (∂ M21.14, question 4). h) $s = 9$ donne $\lfloor 110{,}3\rfloor + 1 = 111$ positions, $s = 11$ en donne 91 ; le nombre de positions décroît quand $s$ croît.

**Erreurs fréquentes.** Oublier le $+1$ (993). Arrondir vers le haut en b) (334), ou ne compter le padding qu'une fois (332). Oublier la dilatation en c) (994) ou en d) (200). Prendre $\lfloor\frac{365}{3}\rfloor = 121$ en e). Inverser début et fin en f) : la règle met le zéro en trop à la fin.

**Variante.** $n = 1\,000$, $k = 7$, $s = 4$, sans padding : $\lfloor\frac{993}{4}\rfloor + 1 = 249$ positions.

### Ex M21.7 — Sous-échantillonner et insérer des zéros : la convolution transposée d'un signal et ses recouvrements

**Réponses.** a) `[5, -2, 7]` · b) `[5, 0, 0, -2, 0, 0, 7]` · c) `11` · d) `[6, 3, 9, -1, 4, 3, -5, -1, -6, 2, -2]` · e) `[1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1]` · f) `[11, 12, 13]` · g) `13` · h) `3`.

**Démarche.** a) $(x_0, x_3, x_6)$. b) $\mathbf{D}_3^\top$ remet chaque valeur à sa place et met des zéros ailleurs. c) $(m - 1)s + k = 2 \times 3 + 5$. d) Les zéros insérés, $(3, 0, 0, 1, 0, 0, -2)$, puis la convolution pleine par $\mathbf{w}$ ; ou les tampons : $3\mathbf{w} = (6, 3, 9, -3, 3)$ sur les cases 0 à 4, $1\,\mathbf{w} = (2, 1, 3, -1, 1)$ sur les cases 3 à 7, $-2\mathbf{w} = (-4, -2, -6, 2, -2)$ sur les cases 6 à 10 ; les cases 3, 4, 6 et 7 reçoivent deux tampons : $-3 + 2 = -1$, $3 + 1 = 4$, $-1 - 4 = -5$, $1 - 2 = -1$. e) La case $j$ reçoit un tampon de chaque $i$ tel que $0 \le j - 3i \le 4$. f) $\lfloor\frac{n - 5}{3}\rfloor + 1 = 3$ équivaut à $6 \le n - 5 \le 8$. g) $11 + 2$. h) $\frac{12}{4} = 3$.

Dans ta copie : $\mathbf{D}_3$ a pour lignes $\mathbf{e}_0^\top$, $\mathbf{e}_3^\top$, $\mathbf{e}_6^\top$ ; $\mathbf{D}_3^\top\mathbf{D}_3 = \operatorname{diag}(1, 0, 0, 1, 0, 0, 1)$ efface les cases 1, 2, 4 et 5 : c'est une projection, pas l'identité. La somme de d) vaut $12 = 2 \times 6$ : chaque tampon $y_i\mathbf{w}$ a pour somme $y_i\sum_u w_u$. Le pas 3 ne divise pas $k = 5$ : les cases de rang 0 et 1 modulo 3 (à l'intérieur) reçoivent deux tampons, celles de rang 2 un seul ; pour $(12, 4)$, 4 divise 12 et chaque case intérieure en reçoit $\frac{12}{4}$. f) et g) : les trois longueurs que la somme glissante confond sont les trois tailles de la convolution transposée, pour $p_{\text{out}} = 0$, 1 et 2.

**Erreurs fréquentes.** Mettre les zéros à la fin en b) (`[5, -2, 7, 0, 0, 0, 0]`). Compter $ms = 9$ ou $(m - 1)s + k - 1 = 10$ en c). Convoluer par $\tilde{\mathbf{w}}$ au lieu de $\mathbf{w}$ (`[3, -3, 9, 4, 5, 3, -1, 4, -6, -2, -4]`). Ajouter $p_{\text{out}}$ deux fois.

**Variante.** Avec un pas de 4 : 13 valeurs, $(6, 3, 9, -3, 5, 1, 3, -1, -3, -2, -6, 2, -2)$, et les recouvrements $(1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1)$.

### Ex M21.8 — Une carte de températures filtrée par un laplacien discret et par un lissage séparable

**Réponses.** a) `[[-1, -6, -5, 17], [-5, -14, -10, -3]]` · b) `[1, 4]` · c) `[2, 2]` · d) `[[15, 17.8, 20.8, 19, 13.6, 14], [15.6, 19, 22.4, 20.6, 15.8, 14.6]]` · e) `[[17.84, 19.84, 18.28, 14.76], [19, 21.36, 20, 16.52]]` · f) `[72, 60]` · g) `False`.

**Démarche.** a) La sortie $(i, j)$ est centrée sur la case $(i + 1, j + 1)$ : les quatre voisines moins 4 fois la case. En $(1, 1)$ : $15 + 21 + 15 + 20 - 72 = -1$ ; en $(1, 4)$ : $15 + 14 + 19 + 17 - 48 = 17$ ; en $(2, 2)$ : $21 + 19 + 20 + 22 - 96 = -14$ ; et ainsi de suite. b) Le plus grand, 17, est la sortie $(0, 3)$, centrée sur la case $(1, 4)$ de $\mathbf{T}$ (12 °C, entourée de 15, 14, 19 et 17). c) Le plus petit, $-14$, est la sortie $(1, 1)$, centrée sur $(2, 2)$ (24 °C). d) Colonne 0 : $\frac{14 + 45 + 16}{5} = 15$ et $\frac{15 + 48 + 15}{5} = 15{,}6$, puis les autres colonnes. e) La passe horizontale sur d) : $\frac{15 + 53{,}4 + 20{,}8}{5} = 17{,}84$, etc. f) En direct, 8 valeurs de sortie de 9 produits : 72. En deux passes, la passe verticale calcule $2 \times 6 = 12$ valeurs de 3 produits, puis la passe horizontale $2 \times 4 = 8$ valeurs de 3 produits : $36 + 24 = 60$. g) Faux : il est de rang 2.

Dans ta copie : $\mathbf{K} = \frac1{25}\begin{pmatrix} 1 & 3 & 1 \\ 3 & 9 & 3 \\ 1 & 3 & 1 \end{pmatrix}$ ; en direct, la valeur $(0, 0)$ vaut $\frac{14 + 45 + 17 + 45 + 162 + 63 + 16 + 60 + 24}{25} = \frac{446}{25} = 17{,}84$. Les deux noyaux sont symétriques selon les deux axes : les retourner ne change rien. Le laplacien d'une grille uniforme est nul (ses coefficients ont pour somme 0) : il ne regarde que les écarts ; $\mathbf{K}$ a pour somme 1 : il garde le niveau moyen. Sur une grande carte, la passe verticale a à peine plus de valeurs que la sortie : environ $3 + 3 = 6$ multiplications par valeur de sortie, contre 9 ; ici, la carte est si petite que le gain n'est que de 72 à 60.

**Erreurs fréquentes.** Donner la position dans la sortie, `[0, 3]`, au lieu de la position dans $\mathbf{T}$. Changer le signe du laplacien (compter $+4$ fois la case). Oublier le facteur $\frac1{25}$ en e). Faire en d) la passe horizontale à la place de la verticale. Répondre en f) les comptes par valeur de sortie, 9 et 6, au lieu des totaux.

**Variante.** Pour la carte $\mathbf{T} + 5$ (5 °C de plus partout), le laplacien ne change pas, et le lissage augmente de 5.

### Ex M21.9 — Paramètres et coût d'un filtrage à plusieurs canaux : standard, groupé, par canal, 1 × 1

**Réponses.** a) `(20, 12, 5, 5)` · b) `6020` · c) `360000000` · d) `1520` · e) `90000000` · f) `312` · g) `65` · h) `(20, 100, 150)` · i) `4800000`.

**Démarche.** b) $20 \times (12 \times 25 + 1) = 20 \times 301$. c) $200 \times 300 \times 20 \times 12 \times 25 = 60\,000 \times 6\,000 = 3{,}6 \cdot 10^8$. d) $20 \times (3 \times 25 + 1) = 20 \times 76$. e) Quatre fois moins : $9 \cdot 10^7$. f) $12 \times (25 + 1)$. g) $5 \times (12 + 1)$. h) $\lfloor\frac{200 + 4 - 4 - 1}{2}\rfloor + 1 = 100$ et $\lfloor\frac{300 + 4 - 4 - 1}{2}\rfloor + 1 = 150$. i) $20 \times 60\,000$ valeurs de 4 octets.

Dans ta copie : f) coûte $60\,000 \times 12 \times 25 = 1{,}8 \cdot 10^7$ multiplications-additions et g) $60\,000 \times 5 \times 12 = 3{,}6 \cdot 10^6$. Les poids sont les mêmes en chaque position : leur nombre ne dépend pas de la grille. Sur $400 \times 600$ pixels, toujours 6 020 paramètres, mais $1{,}44 \cdot 10^9$ multiplications-additions : le coût suit l'aire. Avec un pas de 2, il y a quatre fois moins de positions, donc quatre fois moins de calcul.

**Erreurs fréquentes.** Oublier les biais (6 000 en b), 300 en f), 60 en g)). Diviser tout le nombre de paramètres par $g$ (1 505) : le biais ne se divise pas. Donner en i) le nombre de valeurs, 1 200 000, au lieu des octets.

**Variante.** Avec des noyaux $3 \times 3$ et un padding de 1 : $20 \times (12 \times 9 + 1) = 2\,180$ paramètres et $1{,}296 \cdot 10^8$ multiplications-additions.

### Ex M21.10 — Le noyau équivalent de deux lissages successifs, et le champ récepteur d'une pile avec pas et dilatation

**Réponses.** a) `[1, 2, 2, 1]` · b) `[5.8333, 5.5, 6, 6.1667]` · c) `[1, 1, 1, 1, 1, 1]` · d) `2` · e) `74` · f) `8` · g) `[16, 89]` · h) `False`.

**Démarche.** a) $\frac12(1, 1) * \frac13(1, 1, 1) = \frac16(1, 2, 2, 1)$. b) $\mathbf{y} = (7 ;\ 5{,}5 ;\ 5 ;\ 6 ;\ 7 ;\ 5{,}5)$, puis $\mathbf{z} = (\frac{17{,}5}{3} ;\ \frac{16{,}5}{3} ;\ \frac{18}{3} ;\ \frac{18{,}5}{3}) = (\frac{35}{6} ;\ 5{,}5 ;\ 6 ;\ \frac{37}{6})$. c) Le second étage lit le signal d'origine avec des trous de $s_1 = 2$ cases : $\mathbf{K} = \frac12(1, 1) * \frac13(1, 0, 1, 0, 1) = \frac16(1, 1, 1, 1, 1, 1)$. d) $S = 2 \times 1$. e) $r$ passe de 1 à $1 + 1 \times 1 = 2$ ($J = 2$), puis à $2 + 4 \times 2 = 10$ ($J = 8$), puis à $10 + 4 \times 2 \times 8 = 74$ ($J = 8$). f) $2 \times 4 \times 1 = 8$ (le produit des pas, pas leur somme, 7). g) De $Sj = 16$ à $16 + 74 - 1 = 89$. h) Faux : $2 + 5 + 9 = 16$.

Dans ta copie : $\frac{5 + 18 + 4 + 8}{6} = \frac{35}{6}$, comme b). La pile de c) calcule la moyenne de 6 valeurs consécutives, une position sur deux : $z_j = \frac{x_{2j} + \cdots + x_{2j+5}}{6}$. g) $z_j$ lit les sorties $j$, $j + 4$ et $j + 8$ du deuxième étage, dont la première commence à la case $J_2\,j = 8j$ du signal d'origine ; la plage lue va de $8j$ à $8j + 73$, trous compris : la dilatation peut laisser dans la plage des cases sans effet.

**Erreurs fréquentes.** Ignorer le pas en c) (`[1, 2, 2, 1]` et $S = 1$). Oublier les pas en e) ($1 + 1 + 4 + 8 = 14$) ou la dilatation ($10 + 2 \times 8 = 26$). Additionner les pas en f) (7). Commencer $z_2$ à la case 2 au lieu de $2S$, ou finir à $Sj + r$ (90).

**Variante.** Sans dilatation au troisième étage, $(2, 2, 1)$, $(5, 4, 1)$, $(3, 1, 1)$ : $r = 10 + 2 \times 8 = 26$, pour le même pas total 8.

### Ex M21.11 — Le pire cas d'une erreur de capteurs bornée : une forme linéaire sur les boules L∞ et L2

**Réponses.** a) `12` · b) `3` · c) `[-0.25, 0.25, 0.25, -0.25, 0.25]` · d) `1.581` · e) `0.5590` · f) `1.25` · g) `2.4` · h) `[0.5, 0.01]`.

**Démarche.** a) $2 + 5 + 1 + 3 + 1$. b) $0{,}25 \times 12$ (fiche §8). c) $0{,}25\operatorname{signe}(\mathbf{g})$. d) $0{,}25\,\lVert\mathbf{g}\rVert_2 = 0{,}25\sqrt{40} \approx 1{,}58114$. e) $0{,}25\sqrt5 \approx 0{,}559017$. f) $0{,}25\,\lVert\mathbf{g}\rVert_\infty = 0{,}25 \times 5$, en mettant toute l'erreur sur le capteur de poids 5. g) Le pochoir $\begin{pmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \end{pmatrix}$ a pour norme L1 $1 + 1 + 1 + 1 + 4 = 8$ : $0{,}3 \times 8$. h) $\lVert\mathbf{g}\rVert_1 = 2\,500 \times 0{,}02 = 50$ et $\lVert\mathbf{g}\rVert_2 = \sqrt{2\,500 \times 0{,}0004} = 1$ : $0{,}01 \times 50$ et $0{,}01 \times 1$.

Dans ta copie : chaque terme $g_i\delta_i$ vaut au plus $0{,}25\,\lvert g_i\rvert$, atteint quand $\delta_i$ a le signe de $g_i$. Par Cauchy-Schwarz, $\mathbf{g} \cdot \boldsymbol{\delta} \le \lVert\mathbf{g}\rVert_2\,\lVert\boldsymbol{\delta}\rVert_2$, avec égalité pour $\boldsymbol{\delta} = 0{,}25\,\mathbf{g}/\lVert\mathbf{g}\rVert_2$. Le vecteur c) a cinq coordonnées de 0,25 : sa norme L2 est $0{,}25\sqrt5$, plus que le rayon. h) Le rapport $\frac{\lVert\mathbf{g}\rVert_1}{\lVert\mathbf{g}\rVert_2} = 50 = \sqrt{2\,500}$, sa plus grande valeur possible, atteinte car tous les poids ont la même valeur absolue.

**Erreurs fréquentes.** Additionner les poids avec leurs signes ($-2 + 5 + 1 - 3 + 1 = 2$). Prendre $\varepsilon\lVert\mathbf{g}\rVert_\infty$ ou $\varepsilon\lVert\mathbf{g}\rVert_2$ pour la boule L∞. Répondre $0{,}25\,\mathbf{g}$ en c) : il sort de la boule. Oublier le $-4$ du centre en g) (1,2).

**Variante.** Avec des capteurs justes à 0,5 kPa près : 6 sur la boule L∞, $0{,}5\sqrt{40} \approx 3{,}162$ sur la boule L2.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M21.12 — La convolution est commutative et associative ; la corrélation croisée ne l'est pas

**Démonstration.**
1. $(\mathbf{a} * \mathbf{b})_m = \sum_i a_i\,b_{m-i}$, sur les $i$ tels que $0 \le i \le n - 1$ et $0 \le m - i \le k - 1$. Posons $j = m - i$, soit $i = m - j$ : les conditions deviennent $0 \le j \le k - 1$ et $0 \le m - j \le n - 1$, exactement celles de $(\mathbf{b} * \mathbf{a})_m = \sum_j b_j\,a_{m-j}$, et chaque produit $a_{m-j}b_j$ est égal à $b_ja_{m-j}$. (Avec la convention « nul hors des indices », on peut aussi sommer sur tous les entiers et faire le changement d'indice sans bornes.)
2. $\big((\mathbf{a} * \mathbf{b}) * \mathbf{c}\big)_m = \sum_t (\mathbf{a} * \mathbf{b})_t\,c_{m-t} = \sum_t\sum_i a_i\,b_{t-i}\,c_{m-t}$. Avec $j = t - i$ et $l = m - t$, c'est la somme des $a_ib_jc_l$ sur les triplets tels que $i + j + l = m$. De même, $\big(\mathbf{a} * (\mathbf{b} * \mathbf{c})\big)_m = \sum_i a_i\sum_j b_j\,c_{m-i-j}$, la même somme. Les deux suites sont égales.
3. $\mathbf{u}$ a $n$ termes, $\mathbf{v}$ en a $k$, $\mathbf{u} * \mathbf{v}$ en a $n + k - 1$ : $\big(\widetilde{\mathbf{u} * \mathbf{v}}\big)_m = (\mathbf{u} * \mathbf{v})_{n+k-2-m} = \sum_i u_i\,v_{n+k-2-m-i}$. Avec $i' = n - 1 - i$ : $u_i = \tilde u_{i'}$ et $v_{n+k-2-m-i} = v_{k-1-(m-i')} = \tilde v_{m-i'}$, d'où $\sum_{i'}\tilde u_{i'}\,\tilde v_{m-i'} = (\tilde{\mathbf{u}} * \tilde{\mathbf{v}})_m$.
4. Avec $v = n - 1 - u$ : $a_u = \tilde a_v$ et $b_{u+m-(n-1)} = b_{m-v}$, donc $(\mathbf{a} \star \mathbf{b})_m = \sum_v \tilde a_v\,b_{m-v} = (\tilde{\mathbf{a}} * \mathbf{b})_m$. Alors $\mathbf{b} \star \mathbf{a} = \tilde{\mathbf{b}} * \mathbf{a} = \mathbf{a} * \tilde{\mathbf{b}}$, et, par 3, $\widetilde{\mathbf{a} \star \mathbf{b}} = \widetilde{\tilde{\mathbf{a}} * \mathbf{b}} = \mathbf{a} * \tilde{\mathbf{b}}$ : $\mathbf{b} \star \mathbf{a} = \widetilde{\mathbf{a} \star \mathbf{b}}$. Contre-exemple : $\mathbf{a} = (1, 0)$, $\mathbf{b} = (0, 1)$ ; $\mathbf{a} \star \mathbf{b} = (0, 1) * (0, 1) = (0, 0, 1)$ et $\mathbf{b} \star \mathbf{a} = (1, 0) * (1, 0) = (1, 0, 0)$.
5. Par 4 et 3, $(\mathbf{a} \star \mathbf{b}) \star \mathbf{c} = \widetilde{\mathbf{a} \star \mathbf{b}} * \mathbf{c} = \mathbf{a} * \tilde{\mathbf{b}} * \mathbf{c}$, alors que $\mathbf{a} \star (\mathbf{b} \star \mathbf{c}) = \tilde{\mathbf{a}} * (\tilde{\mathbf{b}} * \mathbf{c})$ ; par l'associativité de la convolution, les parenthèses ne comptent pas, et seule la place du retournement diffère. Contre-exemple : $\mathbf{a} = (1, 0)$, $\mathbf{b} = \mathbf{c} = (1)$ : $(\mathbf{a} \star \mathbf{b}) \star \mathbf{c} = (1, 0)$ et $\mathbf{a} \star (\mathbf{b} \star \mathbf{c}) = (0, 1)$.
6. $\mathbf{a} \star \mathbf{b} = \mathbf{b} \star \mathbf{a}$ si et seulement si $\mathbf{a} \star \mathbf{b}$ est symétrique (égal à son retourné), par exemple quand $\mathbf{a} = \mathbf{b}$. Pour composer deux sommes glissantes, ce n'est pas un problème : le noyau équivalent est la **convolution** $\mathbf{a} * \mathbf{b}$ des deux noyaux (fiche §7), qui, elle, est commutative et associative ; l'ordre de deux étages de pas 1 ne compte pas, et une pile peut se regrouper comme on veut.

**Grille de relecture.** Le changement d'indice est fait avec ses bornes (ou la convention « nul hors des indices » est dite). L'associativité passe par la somme sur les triplets $i + j + l = m$. Le lemme du retournement est démontré par un calcul d'indices. La corrélation pleine est réécrite comme $\tilde{\mathbf{a}} * \mathbf{b}$. Les deux contre-exemples sont calculés. La conclusion distingue la corrélation (ni commutative ni associative) du noyau équivalent (une convolution).

**Variante.** L'autocorrélation $\mathbf{a} \star \mathbf{a} = \tilde{\mathbf{a}} * \mathbf{a}$ est toujours symétrique : pour $\mathbf{a} = (1, 3)$, $(3, 1) * (1, 3) = (3, 10, 3)$.

### Ex M21.13 — Les applications linéaires qui commutent avec le décalage circulaire sont les convolutions circulaires ; la transposée d'une matrice circulante

**Démonstration.**
1. $(\mathbf{P}\mathbf{e}_j)_i = (\mathbf{e}_j)_{(i-1) \bmod n}$ vaut 1 si et seulement si $(i - 1) \bmod n = j$, c'est-à-dire $i = (j + 1) \bmod n$ : $\mathbf{P}\mathbf{e}_j = \mathbf{e}_{(j+1) \bmod n}$. Par récurrence, $\mathbf{P}^j\mathbf{e}_0 = \mathbf{e}_j$ pour $j = 0, \ldots, n - 1$.
2. Pour $j = 0$, c'est $v_i$. Si $(\mathbf{P}^j\mathbf{v})_i = v_{(i-j) \bmod n}$ pour tout $i$, alors $(\mathbf{P}^{j+1}\mathbf{v})_i = (\mathbf{P}^j\mathbf{v})_{(i-1) \bmod n} = v_{(i-1-j) \bmod n}$.
3. Si $\mathbf{A}\mathbf{P}^j = \mathbf{P}^j\mathbf{A}$, alors $\mathbf{A}\mathbf{P}^{j+1} = \mathbf{P}^j\mathbf{A}\mathbf{P} = \mathbf{P}^{j+1}\mathbf{A}$ : par récurrence, $\mathbf{A}$ commute avec toutes les puissances de $\mathbf{P}$. La colonne $j$ de $\mathbf{A}$ est $\mathbf{A}\mathbf{e}_j = \mathbf{A}\mathbf{P}^j\mathbf{e}_0 = \mathbf{P}^j\mathbf{A}\mathbf{e}_0 = \mathbf{P}^j\mathbf{h}$, de coefficient $i$ égal à $h_{(i-j) \bmod n}$ (question 2) : c'est la colonne $j$ de $\operatorname{circ}(\mathbf{h})$. Donc $\mathbf{A} = \operatorname{circ}(\mathbf{h})$.
4. $(\mathbf{P}^m)_{ij} = (\mathbf{P}^m\mathbf{e}_j)_i$ vaut 1 si $i = (j + m) \bmod n$, c'est-à-dire $(i - j) \bmod n = m$, et 0 sinon. Donc $\big(\sum_m h_m\mathbf{P}^m\big)_{ij} = h_{(i-j) \bmod n}$ : $\operatorname{circ}(\mathbf{h}) = \sum_m h_m\mathbf{P}^m$. Une somme de puissances de $\mathbf{P}$ commute avec $\mathbf{P}$ : $\operatorname{circ}(\mathbf{h})\,\mathbf{P} = \sum_m h_m\mathbf{P}^{m+1} = \mathbf{P}\operatorname{circ}(\mathbf{h})$.
5. $(\operatorname{circ}(\mathbf{h})\,\mathbf{x})_i = \sum_j h_{(i-j) \bmod n}\,x_j = \sum_j x_j\,h_{(i-j) \bmod n} = (\mathbf{x} \circledast \mathbf{h})_i$. Avec 3 et 4 : une matrice commute avec $\mathbf{P}$ si et seulement si c'est la matrice d'une convolution circulaire, par sa première colonne.
6. $\big(\operatorname{circ}(\mathbf{h})^\top\big)_{ij} = h_{(j-i) \bmod n}$. Or $(j - i) \bmod n = \big(-((i - j) \bmod n)\big) \bmod n$, donc ce coefficient est $\check h_{(i-j) \bmod n}$ : $\operatorname{circ}(\mathbf{h})^\top = \operatorname{circ}(\check{\mathbf{h}})$. Pour $\mathbf{h} = (2, 7, 0, 1, 3)$ : $\check{\mathbf{h}} = (h_0, h_4, h_3, h_2, h_1) = (2, 3, 1, 0, 7)$, alors que le renversement vaut $(3, 1, 0, 7, 2)$. Le renversement $r_m = h_{n-1-m} = \check h_{(m+1) \bmod n}$ est $\check{\mathbf{h}}$ **avancé** d'une case, $\mathbf{r} = \mathbf{P}^{-1}\check{\mathbf{h}} = \mathbf{P}^{n-1}\check{\mathbf{h}}$ ; sa matrice circulante est $\operatorname{circ}(\check{\mathbf{h}})\,\mathbf{P}^{-1}$, pas la transposée.

**Grille de relecture.** $\mathbf{P}\mathbf{e}_j$ est calculé, et $\mathbf{e}_j = \mathbf{P}^j\mathbf{e}_0$ obtenu par récurrence. La formule de $\mathbf{P}^j\mathbf{v}$ est démontrée. La commutation est étendue aux puissances, puis appliquée colonne par colonne. La réciproque passe par $\operatorname{circ}(\mathbf{h}) = \sum_m h_m\mathbf{P}^m$ (ou par un calcul direct de coefficients). Le lien avec $\circledast$ est écrit. La transposée est calculée avec les indices modulo $n$, et l'exemple montre que le renversement simple est faux d'un décalage.

**Variante.** Pour $n = 4$ et $\mathbf{h} = \mathbf{e}_1$ : $\operatorname{circ}(\mathbf{e}_1) = \mathbf{P}$, $\check{\mathbf{h}} = \mathbf{e}_3$, et $\mathbf{P}^\top = \operatorname{circ}(\mathbf{e}_3) = \mathbf{P}^3 = \mathbf{P}^{-1}$ : la transposée d'un décalage est le décalage dans l'autre sens.

### Ex M21.14 — Le nombre de positions ⌊(n + 2p − d(k − 1) − 1)/s⌋ + 1 quand la fenêtre tient, par un dénombrement

**Démonstration.**
1. Le signal complété a $n + 2p$ cases, numérotées de 0 à $n + 2p - 1$. Les cases lues par la fenêtre $i$ vont de $si \ge 0$ à $si + d(k - 1)$ ; elles sont toutes dans le signal si et seulement si la dernière l'est : $si + d(k - 1) \le n + 2p - 1$, soit $si \le A$, soit $i \le \frac As$ ($s > 0$).
2. Les entiers $i$ de $[0, \frac As]$ sont $0, 1, \ldots, \lfloor\frac As\rfloor$ : $\lfloor\frac As\rfloor$ est le plus grand entier inférieur ou égal à $\frac As$, et il est positif ou nul puisque $A \ge 0$. Il y en a $\lfloor\frac As\rfloor + 1$.
3. Si $A < 0$, même la fenêtre 0 dépasse : aucune position. Pour $-s \le A \le -1$, $\frac As \in [-1, -\frac1s]$ et $\lfloor\frac As\rfloor + 1 = 0$, la formule reste juste ; pour $A < -s$, elle donne un nombre négatif, qui n'a pas de sens. L'hypothèse (ou un $\max(0, \cdot)$) est donc nécessaire.
4. $A$ ne dépend de $n$ que par $n$ lui-même ($A' - A = n' - n$), et le nombre de positions ne dépend de $A$ que par $\lfloor\frac As\rfloor$. Or $\lfloor\frac As\rfloor = q$ équivaut à $qs \le A \le qs + s - 1$ : exactement $s$ valeurs consécutives de $A$, donc de $n$.
5. Avec $P_{\text{tot}}$ zéros en tout, la question 1 donne la même condition avec $P_{\text{tot}}$ à la place de $2p$ (la répartition entre début et fin ne change pas le nombre de cases) : $A = n + P_{\text{tot}} - d(k - 1) - 1 = (n_{\text{out}} - 1)s$, et $\lfloor\frac As\rfloor + 1 = n_{\text{out}}$. Avec $P_{\text{tot}} - 1$ zéros, $A = (n_{\text{out}} - 1)s - 1$, $\lfloor\frac As\rfloor = n_{\text{out}} - 2$, soit $n_{\text{out}} - 1$ positions : $P_{\text{tot}}$ est le plus petit nombre de zéros qui donne $n_{\text{out}}$ positions. (Quand la formule de $P_{\text{tot}}$ est négative, on n'ajoute aucun zéro ; alors $A = n - d(k - 1) - 1$ est à la fois $\ge (n_{\text{out}} - 1)s$ et $\le n - 1 < n_{\text{out}}\,s$, et l'on trouve encore $n_{\text{out}}$ positions.)

**Grille de relecture.** La condition d'existence porte sur la dernière case de la fenêtre. Le dénombrement des entiers de $[0, \frac As]$ est justifié, avec $A \ge 0$. Le cas $A < 0$ est discuté. Les $s$ longueurs consécutives viennent de l'encadrement de la partie entière. La règle « même taille » est vérifiée, avec la minimalité de $P_{\text{tot}}$.

**Variante.** $n = 10$, $k = 3$, $d = 2$, $s = 2$, $p = 0$ : $A = 10 - 4 - 1 = 5$ et $\lfloor\frac52\rfloor + 1 = 3$ fenêtres, qui commencent en 0, 2 et 4 ; celle qui commencerait en 6 lirait la case 10.

### Ex M21.15 — Le champ récepteur d'une pile de convolutions : récurrence et forme close

**Démonstration.**
1. Pour $\ell = 0$, la sortie $j$ est la case $j$ : l'intervalle $[j, j]$, de longueur $r_0 = 1$, avec $J_0 = 1$. Supposons le résultat vrai à l'étage $\ell - 1$. La sortie $j$ de l'étage $\ell$ lit les sorties $t_u = s_\ell j + d_\ell u$ de l'étage $\ell - 1$, et chacune lit des cases comprises entre $J_{\ell-1}t_u$ et $J_{\ell-1}t_u + r_{\ell-1} - 1$. Comme $t_0 \le t_u \le t_{k_\ell - 1}$, toutes ces cases sont entre $J_{\ell-1}t_0 = J_\ell\,j$ et $J_{\ell-1}t_{k_\ell-1} + r_{\ell-1} - 1 = J_\ell\,j + d_\ell(k_\ell - 1)J_{\ell-1} + r_{\ell-1} - 1 = J_\ell\,j + r_\ell - 1$. La case $J_\ell\,j$ est lue par $t_0$, et la case $J_\ell\,j + r_\ell - 1$ par $t_{k_\ell-1}$ (hypothèse de récurrence). Ces deux cases extrêmes ne sont atteintes que par un seul chemin (toujours $u = 0$, ou toujours $u = k_\ell - 1$), car les autres sorties commencent plus loin ou finissent plus tôt : leur coefficient est un produit de poids non nuls, la sortie en dépend vraiment.
2. $J_\ell = J_{\ell-1}s_\ell$ et $J_0 = 1$ : par récurrence, $J_\ell = s_1\cdots s_\ell$.
3. $r_L = r_0 + \sum_{\ell=1}^{L}(r_\ell - r_{\ell-1}) = 1 + \sum_{\ell=1}^{L}d_\ell(k_\ell - 1)J_{\ell-1} = 1 + \sum_{\ell=1}^{L}d_\ell(k_\ell - 1)\,s_1\cdots s_{\ell-1}$ (pour $\ell = 1$, le produit vide vaut 1).
4. $r_L = 1 + \sum_{\ell=1}^{L}3 \times 2^{\ell-1} = 1 + 3(2^L - 1) = 3 \times 2^L - 2$. Il faut $2^L \ge 334$ : $L = 9$ étages ($r_8 = 766$, $r_9 = 1\,534$).
5. Un seul étage, $k_1 = 2$ et $d_1 = 3$ : la sortie lit les cases $s_1j$ et $s_1j + 3$, deux cases sur les quatre de son champ récepteur. Si chaque sortie de l'étage $\ell - 1$ lit tout son intervalle de $r_{\ell-1}$ cases, les intervalles lus par $t_u$ et $t_{u+1}$ commencent à $J_{\ell-1}d_\ell$ cases l'un de l'autre ; si $J_{\ell-1}d_\ell \le r_{\ell-1}$, ils se touchent ou se chevauchent, et leur réunion est tout l'intervalle de l'étage $\ell$ : par récurrence, la sortie lit toutes les cases de son champ récepteur. (Ici, $J_0d_1 = 3 > r_0 = 1$ : des trous.)

**Grille de relecture.** L'initialisation et l'hérédité sont séparées ; l'hérédité utilise $t_0$ et $t_{k_\ell-1}$ et calcule les deux bornes de la plage lue, qui est le champ récepteur (trous compris) ; la dépendance réelle des cases extrêmes est justifiée par un chemin unique. $J_\ell$ est un produit de pas, et la forme close vient d'une somme télescopique. L'exemple numérique est fait. Les trous de la dilatation sont montrés, et la condition qui les évite est démontrée.

**Variante.** Trois étages $(k, s) = (3, 3)$ : $r = 1 + 2 + 6 + 18 = 27$ et $S = 27$ : chaque sortie lit son propre bloc de 27 cases, sans chevaucher le bloc voisin.

### Ex M21.16 — Le maximum d'une forme linéaire sur une boule L∞ vaut ε‖g‖₁, atteint en ε signe(g)

**Démonstration.**
1. Pour $\lVert\boldsymbol{\delta}\rVert_\infty \le \varepsilon$, chaque $\lvert\delta_i\rvert \le \varepsilon$, donc $\mathbf{g} \cdot \boldsymbol{\delta} = \sum_i g_i\delta_i \le \sum_i\lvert g_i\rvert\,\lvert\delta_i\rvert \le \varepsilon\sum_i\lvert g_i\rvert = \varepsilon\lVert\mathbf{g}\rVert_1$.
2. Les coordonnées de $\boldsymbol{\delta}^\star$ valent $\pm\varepsilon$ ou 0 : $\lVert\boldsymbol{\delta}^\star\rVert_\infty \le \varepsilon$. Et $g_i\operatorname{signe}(g_i) = \lvert g_i\rvert$, donc $\mathbf{g} \cdot \boldsymbol{\delta}^\star = \varepsilon\sum_i\lvert g_i\rvert$. Pour $g_i = 0$, $\operatorname{signe}(g_i) = 0$ et $\delta^\star_i = 0$ ; mais n'importe quel $\delta_i \in [-\varepsilon, \varepsilon]$ convient, puisque $g_i\delta_i = 0$.
3. La boule est symétrique : $\boldsymbol{\delta}$ y est si et seulement si $-\boldsymbol{\delta}$ y est. Donc $\min\mathbf{g} \cdot \boldsymbol{\delta} = -\max\mathbf{g} \cdot (-\boldsymbol{\delta}) = -\varepsilon\lVert\mathbf{g}\rVert_1$, et $\lvert\mathbf{g} \cdot \boldsymbol{\delta}\rvert \le \varepsilon\lVert\mathbf{g}\rVert_1$.
4. Si $\mathbf{g} \cdot \boldsymbol{\delta} = \varepsilon\lVert\mathbf{g}\rVert_1$, toutes les inégalités du 1 sont des égalités : $g_i\delta_i = \varepsilon\lvert g_i\rvert$ pour chaque $i$. Pour $g_i \ne 0$, avec $\lvert\delta_i\rvert \le \varepsilon$, cela impose $\delta_i = \varepsilon\operatorname{signe}(g_i)$. Si aucun $g_i$ n'est nul, $\boldsymbol{\delta} = \boldsymbol{\delta}^\star$.
5. $\lVert\mathbf{g}\rVert_2^2 = \sum_i g_i^2 \le \big(\sum_i\lvert g_i\rvert\big)^2$ (le carré d'une somme de nombres positifs contient tous les carrés) ; et, par Cauchy-Schwarz appliquée à $(\lvert g_1\rvert, \ldots, \lvert g_n\rvert)$ et au vecteur de uns, $\sum_i\lvert g_i\rvert \le \lVert\mathbf{g}\rVert_2\sqrt n$. Égalité dans la seconde si et seulement si $(\lvert g_i\rvert)$ est proportionnel au vecteur de uns : tous les $\lvert g_i\rvert$ égaux.

**Grille de relecture.** La majoration terme à terme utilise $\lvert\delta_i\rvert \le \varepsilon$. $\boldsymbol{\delta}^\star$ est dans la boule, et la valeur atteinte est calculée ; le cas $g_i = 0$ est traité. Le minimum vient de la symétrie de la boule. L'unicité vient du cas d'égalité, coordonnée par coordonnée. Les deux inégalités entre normes sont démontrées, avec leur cas d'égalité.

**Variante.** Sur la boule L1 de rayon $\varepsilon$, le maximum vaut $\varepsilon\lVert\mathbf{g}\rVert_\infty$, atteint en mettant toute l'erreur, $\varepsilon\operatorname{signe}(g_j)$, sur une coordonnée $j$ où $\lvert g_j\rvert$ est le plus grand.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M21.17 — Pont : filtrer une grille à trois canaux comme les bibliothèques

**Réponses.** a) `(3, 4, 5)` · b) `(2, 3, 2, 2)` · c) `(2, 3, 4)` · d) `26` · e) `-3` · f) `1` · g) `10` · h) `288` · i) `[8, 13, 11, 22, 5]` · j) `[16, 8, 13, 11, 22]`.

**Démarche.** c) $(C_{\text{out}}, 4 - 2 + 1, 5 - 2 + 1)$. d) $2 \times (3 \times 4 + 1)$. e) La fenêtre en haut à gauche de chaque canal, $\begin{pmatrix} 2 & 1 \\ 0 & 4 \end{pmatrix}$, $\begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$, $\begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}$, multipliée case par case par les noyaux de la sortie 0 : $2 + 0 + 0 - 4 = -2$ ; $0 + 0 - 3 + 0 = -3$ ; $0 + 0 + 1 + 0 = 1$ ; plus le biais : $-4 + 1 = -3$. f) Les fenêtres des lignes 2-3 et des colonnes 3-4, avec les noyaux de la sortie 1 : $0 - 2 + 2 + 0 = 0$ ; $0 + 3 + 0 + 0 = 3$ ; $-2 + 0 + 0 + 2 = 0$ ; plus le biais : $3 - 2 = 1$. g) Les noyaux retournés selon les deux axes, $\begin{pmatrix} -1 & 2 \\ 0 & 1 \end{pmatrix}$, $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ : $-2 + 2 + 0 + 4 = 4$ ; $0 + 0 + 3 + 0 = 3$ ; $0 + 2 + 0 + 0 = 2$ ; plus le biais : 10. h) $3 \times 4$ positions, 2 sorties, $3 \times 2 \times 2$ poids : 288. i) $(4 + 4,\ 1 + 12,\ 3 + 8,\ 2 + 20,\ 5 + 0)$. j) La convolution pleine $\mathbf{x} * (4, 1) = (16, 8, 13, 11, 22, 5)$, dont le mode même taille garde les 5 premières valeurs (à partir de l'indice $\lfloor\frac{2 - 1}{2}\rfloor = 0$).

Dans ta copie : $Y_{0,0,0} = b_0 + \sum_{c=0}^{2}\sum_{u=0}^{1}\sum_{v=0}^{1}W_{0,c,u,v}\,X_{c,u,v}$. `np.convolve` retourne le noyau : pour obtenir la somme glissante de poids $(1, 4)$, on lui donne $(4, 1)$. j) est i) décalé d'une case vers la droite : NumPy met le zéro en trop à gauche (la valeur 16 vient de $4 \times x_0$ seul), PyTorch à droite (la valeur 5 vient de $x_4$ seul). Une couche de convolution de workbookIA 21 calcule la corrélation croisée, sans retournement, comme e).

**Erreurs fréquentes.** Oublier le biais ($-4$ en e), 3 en f), 24 en d)). Retourner les noyaux en e) (10, la réponse de g)). En g), ne retourner les noyaux que selon un axe (8 selon les lignes, 15 selon les colonnes). Échanger i) et j).

**Variante.** Avec un pas de 2 selon les deux axes, la sortie a la forme $(2, 2, 2)$, et son canal 0 vaut $\begin{pmatrix} -3 & 13 \\ 23 & 4 \end{pmatrix}$ (une valeur sur deux de la sortie de pas 1, en ligne et en colonne).

### Ex M21.18 — Expliquer avec une règle graduée et un pochoir pourquoi une convolution est équivariante, mais pas invariante

**Réponse modèle (6 à 10 phrases).** À chaque position, ton pochoir regarde trois relevés voisins et en fait un score, toujours avec la même recette : il ne sait pas à quel endroit de la règle il se trouve. Une crue brève produit donc le même petit groupe de scores élevés, où qu'elle se produise. Si la même crue arrive trois jours plus tard, ce groupe de scores se retrouve trois jours plus loin dans ta liste, avec exactement les mêmes valeurs. Décaler les relevés décale les scores d'autant : c'est l'équivariance. Ta liste de scores n'est pas invariante pour autant : invariante, elle resterait la même quand la crue se déplace, alors qu'elle se déplace avec elle ; c'est justement ce qui te dit **quand** la crue a eu lieu. Le pochoir répond donc « quoi » de la même façon partout, et sa liste de scores garde le « quand ». Près du bout de tes relevés, le pochoir n'a plus trois valeurs à regarder : une crue qui arrive le dernier jour n'a pas tous ses scores, et la règle « décalé d'autant » ne vaut plus. Loin des bords, en revanche, elle est exacte, quelle que soit la crue.

**En 3 phrases.** Le pochoir applique la même recette partout, donc une crue décalée de trois jours donne les mêmes scores, décalés de trois jours : c'est l'équivariance. La liste des scores n'est pas invariante, puisqu'elle bouge avec la crue, et c'est ce qui garde la date de la crue. Près du bout des relevés, des scores manquent, et l'équivariance n'est plus exacte.

**Grille.** La même recette à chaque position ; les scores décalés d'autant ; la différence entre « se déplacer avec » et « ne pas bouger », et ce que la liste garde (la date) ; les bords.

<a id="entretien"></a>

## 💼 Entretien

### M21.E1 — « Pourquoi une convolution est-elle une matrice de Toeplitz, et pourquoi ne la forme-t-on jamais ? »

**Réponse modèle (60 secondes).** « Pour un noyau fixé, convoluer est linéaire : convoluer une somme de signaux, c'est sommer leurs convolutions. Cette application a donc une matrice. Sa colonne j est l'image du j-ième vecteur de base, une impulsion à la place j, et l'image d'une impulsion est le noyau lui-même, décalé de j cases. Toutes les colonnes sont le même noyau, descendu d'une ligne à chaque fois : le coefficient (i, j) ne dépend que de i moins j, les diagonales sont constantes, c'est une matrice de Toeplitz. Elle a environ n au carré coefficients, mais seulement n fois k sont non nuls : pour un enregistrement de cent mille valeurs et un noyau de sept coefficients, moins d'un sur dix mille. La former coûterait n au carré en mémoire et en calcul, alors que la convolution directe coûte n fois k. En pratique, on fait des boucles optimisées, ou on range les fenêtres dans une matrice pour faire un seul produit matriciel, ou, pour les longs noyaux, on passe par la transformée de Fourier. La matrice sert à raisonner : elle donne le rang, ce que le filtre efface, et la transposée, qui est la convolution par le noyau retourné, dans le mode échangé. »

**Grille.** La linéarité ; les colonnes comme des noyaux décalés ; les diagonales constantes ; le nombre de coefficients non nuls ; le coût comparé ; ce qu'on fait à la place ; à quoi sert la matrice.

<a id="notebook"></a>

## Notebook

Le code complet est dans `05_solutions.ipynb`, exécuté ; voici les réponses et ce qu'il faut en retenir.

- **M21.19 🔨** `convolve` : la convolution pleine par une boucle sur $\mathbf{b}$ (chaque $b_j$ ajoute $b_j\,\mathbf{a}$ à partir de la case $j$), puis les lignes du mode (« valid » de l'indice $\min(n, k) - 1$ à $\max(n, k) - 1$, « same » à partir de $\lfloor\frac{\min(n, k) - 1}{2}\rfloor$). a) Trois dés à 8 faces totalisent 12 avec la probabilité $\frac{46}{512} = \frac{23}{256}$ (la loi d'un dé convoluée deux fois avec elle-même). b) Le coefficient de $X^5$ dans $(2 - X)^7$ vaut $\binom75 \times 2^2 \times (-1)^5 = -84$. c) La première valeur du mode même taille vaut $\frac{8 + 10 + 13}{5} = 6{,}2$ : deux des cinq valeurs sont des zéros, alors que la première moyenne complète vaut 12. d) 8 valeurs sur 12 sont des moyennes de 5 vraies mesures, les $12 - 5 + 1$ du mode valide.
- **M21.20 🔨** `toeplitz_matrix` : la colonne $j$ reçoit le noyau à partir de la ligne $j$, puis on garde les lignes du mode, les mêmes que `convolve`. a) Pour $(1, -3, 2)$ et $n = 6$, les rangs valent `[6, 4]` : la matrice pleine est injective, la valide a un noyau de dimension 2. b) $\frac{7 \times 1\,000}{1\,006 \times 1\,000} \approx 0{,}696$ % de coefficients non nuls. c) `[True, False, True]` : la transposée de la matrice valide est la matrice pleine du noyau retourné ; en mode même taille, c'est vrai pour $k = 5$, faux pour $k = 4$ (le zéro en trop change de côté).
- **M21.21 🔨** `circular_convolve` : pour chaque $i$, ajouter $a_i$ fois $\mathbf{b}$ décalé circulairement de $i$ cases. a) La température lissée à 0 h vaut $\frac{9 + 9 + 8}{3} \approx 8{,}6667$ °C (l'heure 23 entre dans la moyenne : le profil est circulaire). b) Le maximum lissé est à 14 h, $\frac{20 + 21 + 20}{3} \approx 20{,}33$ °C. c) Vrai : complétées jusqu'à $4 + 3 - 1 = 6$ valeurs, rien ne se replie. d) `[True, False]` : $\check{\mathbf{h}} = (5, 4, 1, 3, 0, -2)$ donne la transposée, pas le renversement $(4, 1, 3, 0, -2, 5)$.
- **M21.22 🔨** `separable_factors` : la décomposition en valeurs singulières, le test $s_2 \le \text{tol} \cdot s_1$, puis $\mathbf{v}$ (premier vecteur singulier à droite, la première coordonnée nettement non nulle rendue positive) et $\mathbf{u} = \mathbf{K}\mathbf{v}$. a) Pour le lissage de M21.8, $\mathbf{v} = \frac{1}{\sqrt{11}}(1, 3, 1) \approx (0{,}3015 ;\ 0{,}9045 ;\ 0{,}3015)$ et $\mathbf{u} = \frac{\sqrt{11}}{25}(1, 3, 1)$. b) Vrai : le laplacien a $s_2 = s_1$. c) Le noyau bruité a pour valeurs singulières $19{,}08$, $1{,}3 \cdot 10^{-3}$ et $1{,}0 \cdot 10^{-3}$ : rejeté avec la tolérance $10^{-10}$, accepté avec $10^{-2}$ ; l'erreur de l'approximation de rang 1 vaut $0{,}00166 = \sqrt{s_2^2 + s_3^2}$.
- **M21.23 🔨** `equivalent_kernel` : $\mathbf{K} \leftarrow \mathbf{K} * (\mathbf{w}_\ell$ dilaté de $S)$, puis $S \leftarrow S\,s_\ell$, en partant de $\mathbf{K} = (1)$, $S = 1$. a) $6\,\mathbf{K}$ vaut `[1, 1, 1, 1, 1, 1]` avec $S = 2$, comme M21.10 c) et d). b) Quatre étages de noyaux de longueur 4 et de pas 2 : `[46, 16]`, soit $3 \times 2^4 - 2 = 46$ (∂ M21.15). c) Le troisième étage écrit avec ses trous, $(w_0, 0, 0, 0, w_1, 0, 0, 0, w_2)$, donne un noyau de 74 coefficients, le champ récepteur de M21.10 e) (des coefficients du noyau équivalent sont nuls : les trous de la plage). d) Vrai : la pile de noyaux de longueurs 3, 4 et 2 et de pas 2, 3 et 1 a un noyau de 15 coefficients et un pas de 6 ; sur les 31 positions de la pile, l'écart maximal est de l'ordre de $10^{-16}$.
- **M21.24 🔮** La sortie d'origine vaut $(0, 0, 7, -1, 0, \ldots)$. a) Pour $t = 3$, elle est décalée d'une case ; b) pour $t = 6$, de deux. c) et d) Faux : $t = 1$ donne $(0, 0, 9, 6, 0, \ldots)$ et $t = 2$ donne $(0, 0, 2, -5, 0, \ldots)$, d'autres nombres. e) `[0, 0, 9, 6, 0, 0, 0, 0, 0]` : la fenêtre 2 lit $x_6, \ldots, x_9 = (0, 0, 2, 5)$, d'où $0 - 0 + 4 + 5 = 9$, et la fenêtre 3 lit $(5, -1, 0, 0)$, d'où $5 + 1 = 6$. Le filtre lit d'autres paquets de valeurs que pour $t = 0$ : la sortie change de nombres, pas seulement de place.
- **M21.25 🔬** a) `[625, 50]` multiplications par valeur de sortie pour $k = 25$, selon les comptes de la fiche (en deux passes, la passe intermédiaire a un peu plus de valeurs que la sortie : environ $2{,}1\,k$ ici). b) (B) : le rapport mesuré est de l'ordre de 12 à 17 (il dépend de la machine), proche de $\frac k2 = 12{,}5$ ; pour $k = 3$, il est d'environ 2 seulement, et le gain ne vaut la peine qu'à partir de noyaux moyens. c) Vrai : l'écart maximal est de l'ordre de $10^{-14}$. Chaque passe est une addition de tranches de même taille, d'où un temps proportionnel au nombre de tranches, $k^2$ contre $2k$.
- **M21.26 🎨** Pour $(5, 2)$ et $(7, 3)$, $s$ ne divise pas $k$ : chaque axe alterne des cases couvertes par 2 et par 3 tampons, et la carte intérieure mélange 4, 6 et 9, un damier ; pour $(6, 2)$ et $(9, 3)$, chaque axe donne 3 partout à l'intérieur, et la carte vaut 9 sur tout l'intérieur. Les cartes ont $15 \times 15$, $16 \times 16$, $22 \times 22$ et $24 \times 24$ cases ($(m - 1)s + k$ avec $m = 6$) ; les bords reçoivent moins de tampons dans tous les cas.
- **M21.27 🐛** (1) `np.convolve` retourne le noyau : `sliding_sum` doit lui donner `w[::-1]` (ou appeler `np.correlate`). La vérification du collègue utilisait la dérivée seconde, symétrique, que le retournement ne change pas. a) Les vitesses de montée valent `[1, 3, 2, 5, 1]` m/h (la version fausse donnait leurs opposées). (2) La dernière fenêtre incomplète n'existe pas : `//` (ou `math.floor`) au lieu de `math.ceil`. Les trois cas du collègue tombaient juste, et les deux arrondis coïncidaient. b) 24 positions (la version fausse en comptait 25). (3) Une première colonne et une première ligne ne suffisent que pour un noyau de rang 1 (et avec $K_{0,0} \ne 0$) ; il faut tester le rang, par exemple avec `separable_factors`. c) L'écart maximal vaut 1, en ligne 1, colonne 2 ($5$ contre $6$), sans aucun message d'erreur. d) Vrai : le noyau est de rang 2, avec $\frac{s_2}{s_1} \approx 0{,}043$. e) `[-9, 3, -10, 5, -13, -17]`, alors que PyTorch donne $(3, -10, 5, -13, -17, 18)$ : les mêmes nombres, décalés d'une case.
- **M21.28 🛠️** Le test passe sur `toeplitz_matrix`, et attrape la version fausse dès le premier noyau de longueur paire tiré (pour $k$ impair, $\lfloor k/2\rfloor = \lfloor\frac{k-1}{2}\rfloor$ et les deux versions coïncident) ; son message dit d'abord ce qui était attendu, puis $k$, $n$ et le mode. Un test sur des noyaux tous impairs ne l'aurait jamais vu.
- **M21.29 🏆** a) Les poids secrets, `[-0.46, 0.18, 0.92, 0.03, 0.75, -0.35, 0.59]`, sont retrouvés à $2 \cdot 10^{-3}$ près. b) L'écart type du bruit estimé vaut $0{,}049$, soit $0{,}05$ à 2 décimales. c) Avec 10, 20, 50, 100, 200 et 500 valeurs, les erreurs maximales valent environ $0{,}069$, $0{,}029$, $0{,}020$, $0{,}009$, $0{,}005$ et $0{,}003$ : 50 valeurs suffisent pour une erreur sous 0,025. L'erreur décroît à peu près comme $\frac{1}{\sqrt m}$ : c'est la précision des moindres carrés, et la sortie est **linéaire en $\mathbf{w}$**, ce qui rend le problème si simple.
