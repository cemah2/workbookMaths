# M12c · Valeurs propres et matrices symétriques — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M12c.Q1 — Ce que mesure un déterminant
1. Sur le rectangle $[0 ; 2] \times [0 ; 3]$, d'aire $6 = \det\mathbf{A}$.
2. Que l'application **retourne** les figures, comme un miroir : elle change l'orientation.
3. Sur une droite (ou sur le seul point $\mathbf{0}$, si la matrice est nulle) : l'aire de toute figure devient 0.
4. $5 \times 2 = 10$.
5. Une rotation : $\cos^2\theta + \sin^2\theta = 1$. Une symétrie par rapport à une droite : $-1$ (elle conserve les aires, mais retourne).
6. **Faux** : $\det(0{,}1\,\mathbf{I}_9) = 10^{-9}$ pour une matrice parfaitement inversible (et très bien conditionnée). La taille du déterminant dépend de l'échelle ; l'inversibilité « numérique » se mesure par le conditionnement (M12d).

### M12c.Q2 — Les propriétés du déterminant et de la trace : vrai ou faux
1. **Faux** : $\det(\mathbf{I} + \mathbf{I}) = 2^n$, pas $1 + 1$ (dès que $n \ge 2$).
2. **Faux** : $\det(3\mathbf{A}) = 3^2\det\mathbf{A} = 9\det\mathbf{A}$.
3. **Vrai** : les deux valent $\det\mathbf{A}\det\mathbf{B}$, même quand $\mathbf{A}\mathbf{B} \ne \mathbf{B}\mathbf{A}$.
4. **Faux** : avec $\mathbf{A} = \mathbf{B} = \mathbf{I}_2$, $\operatorname{tr}(\mathbf{I}) = 2$ mais $2 \times 2 = 4$.
5. **Vrai** (fiche §2).
6. **Vrai**.
7. **Vrai** : la trace et le déterminant ne dépendent pas de la base.

### M12c.Q3 — Reconnaître un vecteur propre
$\mathbf{M}(2, 3) = (6, 9) = 3(2, 3)$ : **oui**, valeur propre 3. $\mathbf{M}(1, 2) = (2, 4) = 2(1, 2)$ : **oui**, valeur propre 2. $\mathbf{M}(1, 1) = (4, 5)$ : **non**. $(0, 0)$ : **non**, le vecteur nul n'est jamais un vecteur propre. $\mathbf{M}(-4, -6) = (-12, -18) = 3(-4, -6)$ : **oui**, valeur propre 3 (un multiple de $(2, 3)$). $\mathbf{M}(1, 0) = (6, 6)$ : **non**. Trace $6 - 1 = 5 = 3 + 2$, déterminant $-6 + 12 = 6 = 3 \times 2$ : cohérent.

### M12c.Q4 — Diagonalisable ou pas ?
1. **Oui** : elle est déjà diagonale (tout vecteur non nul est propre).
2. **Non** : valeur propre double 2, mais $\mathbf{A} - 2\mathbf{I} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ a un noyau de dimension 1 (un cisaillement).
3. **Oui** : triangulaire, de valeurs propres distinctes 1 et 3.
4. **Non** avec des réels : la rotation d'un quart de tour n'a pas de valeur propre réelle ($\lambda^2 + 1 = 0$).
5. **Oui** : symétrique (théorème spectral) ; ses valeurs propres sont d'ailleurs distinctes ($\det = -14 < 0$).
6. **Oui** : trois valeurs propres distinctes donnent trois vecteurs propres libres.

### M12c.Q5 — Ce que garantit le théorème spectral
1. **Vrai**. 2. **Faux** : $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ a pour valeurs propres 1 et 3 et n'est pas symétrique. 3. **Vrai**. 4. **Faux** : $\mathbf{I}$ a la valeur propre 1 double et est diagonale ; une symétrique est toujours diagonalisable. 5. **Vrai** : $(\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top)^\top = \mathbf{Q}\boldsymbol{\Lambda}^\top\mathbf{Q}^\top = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$. 6. **Vrai** : $\mathbf{q}_i\mathbf{q}_i^\top$ est la projection orthogonale sur la droite de $\mathbf{q}_i$ (M12b §5).

### M12c.Q6 — Définie positive, semi-définie positive ou indéfinie ?
1. **Définie positive** : $2 > 0$ et $10 - 1 = 9 > 0$.
2. **Semi-définie positive** : $36 - 36 = 0$ ; c'est $(2, 3)(2, 3)^\top$, et $\mathbf{x}^\top\mathbf{A}\mathbf{x} = (2x + 3y)^2$, nul sur la droite $2x + 3y = 0$.
3. **Indéfinie** : $q(0, 1) = 4 > 0$ et $q(1, -1) = 0 - 6 + 4 = -2 < 0$ (ou : $\det = -9 < 0$).
4. **Définie négative** : valeurs propres $-1$ et $-4$.
5. **Indéfinie** : diagonale positive, mais $35 - 36 = -1 < 0$.
6. **Semi-définie positive** : valeurs propres $3, 0, 1$ ; $q(\mathbf{e}_2) = 0$.

### M12c.Q7 — Cholesky, racine carrée, blanchiment : qui est quoi ?
1. Triangulaire inférieure : (A) et (C) (l'inverse d'une triangulaire inférieure l'est aussi).
2. Symétrique : (B) et (D).
3. Son produit par sa transposée redonne $\boldsymbol{\Sigma}$ : (A), avec $\mathbf{L}\mathbf{L}^\top$, et (B), avec $\boldsymbol{\Sigma}^{1/2}\boldsymbol{\Sigma}^{1/2\top} = \boldsymbol{\Sigma}$.
4. Blanchiment : (C), (D) et (E).
5. Fabriquer des données de covariance $\boldsymbol{\Sigma}$ : (A) et (B), par $\mathbf{x} = \mathbf{L}\mathbf{u}$ ou $\boldsymbol{\Sigma}^{1/2}\mathbf{u}$.

### M12c.Q8 — Trace, déterminant et valeurs propres
1. $\lambda^2 - 8\lambda + 15 = 0$ : 5 et 3.
2. Trace 6, déterminant 6 ; inversible (aucune valeur propre nulle).
3. Elle n'est pas inversible ($\det = 0$) ; son noyau contient un vecteur non nul.
4. **Non** : $\lambda^2 + 4 = 0$ n'a pas de racine réelle (ce sont $\pm 2i$).
5. $\mathbf{A}^2$ : 9 et 4 ; $\mathbf{A} + 5\mathbf{I}$ : 7 et 2 ; $\mathbf{A}^{-1}$ : $\frac{1}{2}$ et $-\frac{1}{3}$.

<a id="rappels"></a>

## 🔁 Rappels

### M12c.R1 — Le rang et le noyau (M12a)
1. Rang 2 : la ligne 2 est le double de la ligne 1, les lignes 1 et 3 sont libres.
2. $2x_1 - x_2 + 3x_3 = 0$ et $x_1 + x_3 = 0$ : $x_1 = -x_3$, $x_2 = 2x_1 + 3x_3 = x_3$ ; le noyau est $\operatorname{Vect}(-1, 1, 1)$.
3. Non : rang $2 < 3$.
4. Oui : $\mathbf{B}(-1, 1, 1) = \mathbf{0} = 0 \cdot (-1, 1, 1)$. Les vecteurs propres de 0 sont les vecteurs non nuls du noyau.
5. $\det\mathbf{B} = 0$ (non inversible).

### M12c.R2 — Bases orthonormées et matrices orthogonales (M12b)
1. $8^2 + 15^2 = 289 = 17^2$ : colonnes unitaires ; $8 \times (-15) + 15 \times 8 = 0$ : orthogonales. $\mathbf{U}^\top\mathbf{U} = \mathbf{I}$.
2. $\mathbf{U}^{-1} = \mathbf{U}^\top = \frac{1}{17}\begin{pmatrix} 8 & 15 \\ -15 & 8 \end{pmatrix}$.
3. $\lVert \mathbf{U}\mathbf{x} \rVert = \lVert \mathbf{x} \rVert = \sqrt{17} \approx 4{,}123$.
4. $\mathbf{U}^\top\mathbf{x} = \frac{1}{17}(8 + 60, -15 + 32) = (4, 1)$.
5. $\det\mathbf{U} = \frac{64 + 225}{289} = 1$ : une rotation.

### M12c.R3 — La matrice de covariance empirique (M02c)
1. $(3, 3)$.
2. $(-2, -1)$, $(1, -2)$, $(2, 3)$, $(-1, 0)$.
3. Sommes : $\sum x^2 = 10$, $\sum y^2 = 14$, $\sum xy = 2 - 2 + 6 + 0 = 6$. Avec $1/n$ : $\begin{pmatrix} 2{,}5 & 1{,}5 \\ 1{,}5 & 3{,}5 \end{pmatrix}$ ; avec $1/(n - 1)$ : $\begin{pmatrix} 10/3 & 2 \\ 2 & 14/3 \end{pmatrix}$. On passe de la première à la seconde en multipliant par $\frac{n}{n-1} = \frac{4}{3}$.
4. $\frac{6}{\sqrt{10 \times 14}} \approx 0{,}5071$ ; non, le facteur se simplifie.
5. Oui. Ce n'est pas suffisant : il faut qu'elle soit **semi-définie positive** (fiche §8) ; $\begin{pmatrix} 1 & 3 \\ 3 & 2 \end{pmatrix}$ (fiche §7) est symétrique à diagonale positive, et n'en est pas une ($\det = -7$).

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M12c.1 — Déterminants 2 × 2 et 3 × 3 : aire, volume et signe

**Réponses** : a) `14` · b) `7` · c) `175.93` · d) `15` · e) `True` · f) `-15` · g) `120` · h) `5`.

**Démarche.**
- a) $3 \times 4 - (-1) \times 2 = 14$. b) Les côtés $(3, 2)$ et $(-1, 4)$ sont les colonnes de $\mathbf{M}$ : le triangle est la moitié du parallélogramme, $14/2 = 7$.
- c) Le disque a pour aire $4\pi$, son image (une ellipse) $14 \times 4\pi = 56\pi \approx 175{,}93$.
- d) Par la première ligne : $1(3 - 2) - 2(0 - 4) + (-1)(0 - 6) = 1 + 8 + 6 = 15$. e) $15 > 0$. f) Un échange : $-15$. g) $2^3 \times 15 = 120$.
- h) Selon la dernière colonne : $1 \times (0 - 3) - 0 + 1 \times (t - 2) = t - 5$, nul pour $t = 5$.

Pour la copie : par élimination, $L_3 \leftarrow L_3 - 2L_1$ donne $(0, -3, 3)$, puis $L_3 \leftarrow L_3 + L_2$ donne $(0, 0, 5)$ : $1 \times 3 \times 5 = 15$. L'application multiplie **toutes** les aires par $|\det\mathbf{M}|$, quelle que soit la figure et sa position (une application linéaire déforme tout de la même façon). Le volume du parallélépipède est $|\det\mathbf{N}| = 15$.

**Erreurs fréquentes.** $ad + bc$ au lieu de $ad - bc$ ; oublier l'alternance des signes des cofacteurs ; $\det(2\mathbf{N}) = 2\det\mathbf{N}$ ; l'aire du disque $2\pi r$.

**Variante.** $\det(\mathbf{N}^{-1})$ ? *Réponse* : $\frac{1}{15}$.

### Ex M12c.2 — Le déterminant d'une matrice 4 × 4 par élimination

**Réponses** : a) `[[1, 1, 0, 2], [0, 2, 1, 3], [0, 2, 3, -3], [0, 1, 2, 4]]` · b) `[1.0, 2.0, 2.0, 7.0]` · c) `-28` · d) `-0.0357` · e) `784` · f) `-28` · g) `True`.

**Démarche.**
- a) Après l'échange, $L_3 \leftarrow L_3 - 2L_1$ donne $(0, 2, 3, -3)$ et $L_4 \leftarrow L_4 + L_1$ donne $(0, 1, 2, 4)$.
- b) Pivot 2 : $L_3 \leftarrow L_3 - L_2 = (0, 0, 2, -6)$ et $L_4 \leftarrow L_4 - \frac{1}{2}L_2 = (0, 0, \frac{3}{2}, \frac{5}{2})$ ; pivot 2 : $L_4 \leftarrow L_4 - \frac{3}{4}L_3 = (0, 0, 0, \frac{5}{2} + \frac{9}{2}) = (0, 0, 0, 7)$. Diagonale $1, 2, 2, 7$.
- c) Un échange : $\det\mathbf{F} = -(1 \times 2 \times 2 \times 7) = -28$. d) $-\frac{1}{28} \approx -0{,}0357$. e) $(\det\mathbf{F})^2 = 784$. f) Ajouter à une colonne un multiple d'une autre ne change rien : $-28$. g) $\det\mathbf{F} \ne 0$.

Pour la copie : le premier élément de $\mathbf{F}$ est nul, on ne peut pas s'en servir de pivot. Développer la matrice de a) selon sa première colonne donne $1 \times \det\begin{pmatrix} 2 & 1 & 3 \\ 2 & 3 & -3 \\ 1 & 2 & 4 \end{pmatrix} = 2(12 + 6) - 1(8 + 3) + 3(4 - 3) = 36 - 11 + 3 = 28$, et le signe de l'échange donne $-28$. Un développement complet par cofacteurs demande de l'ordre de $4! = 24$ produits de quatre nombres (plus de 70 multiplications), l'élimination une vingtaine d'opérations.

**Erreurs fréquentes.** Oublier le signe de l'échange ; diviser au lieu de soustraire un multiple ; croire que $\det(\mathbf{F}^\top\mathbf{F})$ peut être négatif.

**Variante.** Le déterminant de $\mathbf{F}$ dont on aurait multiplié la ligne 3 par $-2$ ? *Réponse* : $56$.

### Ex M12c.3 — Les valeurs et vecteurs propres d'une matrice 2 × 2

**Réponses** : a) `3` · b) `-28` · c) `[7, -4]` · d) `[3, 1]` · e) `[2, -3]` · f) `[9, -2]` · g) `[49, 16]` · h) `False`.

**Démarche.**
- a), b) $5 - 2 = 3$ et $-10 - 18 = -28$. c) $\lambda^2 - 3\lambda - 28 = (\lambda - 7)(\lambda + 4)$.
- d) $\mathbf{M} - 7\mathbf{I} = \begin{pmatrix} -2 & 6 \\ 3 & -9 \end{pmatrix}$ : $x = 3y$, $(3, 1)$. e) $\mathbf{M} + 4\mathbf{I} = \begin{pmatrix} 9 & 6 \\ 3 & 2 \end{pmatrix}$ : $3x + 2y = 0$, $(2, -3)$.
- f) Ajouter $2\mathbf{I}$ ajoute 2 à chaque valeur propre. g) $7^2 = 49$ et $(-4)^2 = 16$. h) $(3, 1) \cdot (2, -3) = 6 - 3 = 3 \ne 0$.

Pour la copie : $\mathbf{M}(3, 1) = (21, 7) = 7(3, 1)$ et $\mathbf{M}(2, -3) = (-8, 12) = -4(2, -3)$. $\mathbf{M}^2\mathbf{v} = \mathbf{M}(\lambda\mathbf{v}) = \lambda^2\mathbf{v}$ : mêmes vecteurs propres, valeurs au carré. h) ne contredit rien : $\mathbf{M}$ n'est pas symétrique.

**Erreurs fréquentes.** Le signe de $\det$ ; les valeurs propres dans le mauvais ordre ; un vecteur propre du mauvais côté du signe ; croire que $\mathbf{M}^2$ a pour valeurs propres $49$ et $-16$.

**Variante.** Les valeurs propres de $\mathbf{M}^{-1}$ ? *Réponse* : $\frac{1}{7}$ et $-\frac{1}{4}$.

### Ex M12c.4 — Une matrice 3 × 3 triangulaire, puis une avec une valeur propre double

**Réponses** : a) `[4, 2, -1]` · b) `[1, -3, 0]` · c) `[-1, 3, 5]` · d) `-8` · e) `[5, 3, 3]` · f) `2` · g) `[3, 1, 0]` · h) `True`.

**Démarche.**
- a) Triangulaire : la diagonale $2, -1, 4$, rangée. b) $\mathbf{T} + \mathbf{I} = \begin{pmatrix} 3 & 1 & -1 \\ 0 & 0 & 3 \\ 0 & 0 & 5 \end{pmatrix}$ : $x_3 = 0$, puis $3x_1 + x_2 = 0$ : $(1, -3, 0)$.
- c) $\mathbf{T} - 4\mathbf{I} = \begin{pmatrix} -2 & 1 & -1 \\ 0 & -5 & 3 \\ 0 & 0 & 0 \end{pmatrix}$ : avec $x_3 = 5$, $x_2 = 3$, puis $-2x_1 + 3 - 5 = 0$, $x_1 = -1$.
- d) $2 \times (-1) \times 4 = -8$.
- e) Selon la dernière ligne : $(3 - \lambda)\det\begin{pmatrix} 6 - \lambda & -3 \\ 1 & 2 - \lambda \end{pmatrix} = (3 - \lambda)(\lambda^2 - 8\lambda + 15) = (3 - \lambda)(\lambda - 3)(\lambda - 5)$.
- f) $\mathbf{K} - 3\mathbf{I} = \begin{pmatrix} 3 & -3 & 3 \\ 1 & -1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$ est de rang 1 : $\dim E_3 = 3 - 1 = 2$.
- g) $\mathbf{K} - 5\mathbf{I} = \begin{pmatrix} 1 & -3 & 3 \\ 1 & -3 & 1 \\ 0 & 0 & -2 \end{pmatrix}$ : $x_3 = 0$, $x_1 = 3x_2$ : $(3, 1, 0)$. h) $2 + 1 = 3$ vecteurs propres libres.

Pour la copie : $\mathbf{T} - \lambda\mathbf{I}$ est triangulaire, de déterminant $\prod(t_{ii} - \lambda)$ ; $\mathbf{K}$ n'est pas triangulaire, et sa diagonale $6, 2, 3$ n'est pas son spectre. $E_3 = \{x_1 - x_2 + x_3 = 0\}$, de base $(1, 1, 0)$, $(-1, 0, 1)$ ; $\mathbf{P} = \begin{pmatrix} 3 & 1 & -1 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ et $\mathbf{D} = \operatorname{diag}(5, 3, 3)$. Remplacer le 3 en position $(1, 3)$ par un autre nombre $c$ rend les lignes de $\mathbf{K} - 3\mathbf{I}$ non proportionnelles : rang 2, $\dim E_3 = 1$, non diagonalisable.

**Erreurs fréquentes.** Lire les valeurs propres sur la diagonale d'une matrice non triangulaire ; confondre multiplicité algébrique (2) et géométrique ; croire qu'une valeur propre double empêche toujours la diagonalisation.

**Variante.** $\det\mathbf{K}$ et $\operatorname{tr}\mathbf{K}$ ? *Réponse* : $45$ et $11$ ($5 \times 3 \times 3$ et $5 + 3 + 3$).

### Ex M12c.5 — Diagonaliser, puis calculer une puissance dixième

**Réponses** : a) `[2, 1]` · b) `[4, 1]` · c) `[3, 1]` · d) `[[1, -3], [-1, 4]]` · e) `[[4093, -12276], [1023, -3068]]` · f) `1024` · g) `1025` · h) `[1.0, 0.5]`.

**Démarche.**
- a) $\lambda^2 - 3\lambda + 2 = (\lambda - 2)(\lambda - 1)$. b) $\mathbf{A} - 2\mathbf{I} = \begin{pmatrix} 3 & -12 \\ 1 & -4 \end{pmatrix}$ : $x = 4y$. c) $\mathbf{A} - \mathbf{I} = \begin{pmatrix} 4 & -12 \\ 1 & -3 \end{pmatrix}$ : $x = 3y$.
- d) $\det\mathbf{P} = 4 - 3 = 1$ : $\mathbf{P}^{-1} = \begin{pmatrix} 1 & -3 \\ -1 & 4 \end{pmatrix}$.
- e) $\mathbf{P}\mathbf{D}^{10} = \begin{pmatrix} 4096 & 3 \\ 1024 & 1 \end{pmatrix}$, puis fois $\mathbf{P}^{-1}$ : $\begin{pmatrix} 4096 - 3 & -12288 + 12 \\ 1024 - 1 & -3072 + 4 \end{pmatrix}$.
- f) $2^{10} \times 1^{10} = 1024$. g) $2^{10} + 1^{10} = 1025$. h) Les inverses : $\frac{1}{2}$ et $1$, rangés.

Pour la copie : $\mathbf{A}\mathbf{P} = \begin{pmatrix} 8 & 3 \\ 2 & 1 \end{pmatrix} = \mathbf{P}\mathbf{D}$. f) et g) se lisent sur les valeurs propres de $\mathbf{A}^{10}$, qui sont $2^{10}$ et $1$. Pour $k$ grand, $\mathbf{A}^k \approx 2^k\begin{pmatrix} 4 & -12 \\ 1 & -3 \end{pmatrix}$ : les colonnes sont sur la droite de $(4, 1)$, le vecteur propre de la plus grande valeur propre.

**Erreurs fréquentes.** $\mathbf{A}^{10} = 10\mathbf{A}$ ou $\mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ « élevé » terme à terme ; l'ordre des colonnes de $\mathbf{P}$ différent de celui de $\mathbf{D}$ ; $\operatorname{tr}(\mathbf{A}^{10}) = (\operatorname{tr}\mathbf{A})^{10}$.

**Variante.** $\mathbf{A}^{-1}$ ? *Réponse* : $\frac{1}{2}\begin{pmatrix} -2 & 12 \\ -1 & 5 \end{pmatrix}$.

### Ex M12c.6 — Une matrice non diagonalisable, et une rotation sans valeur propre réelle

**Réponses** : a) `[2, 2]` · b) `1` · c) `[3, 1]` · d) `False` · e) `-3` · f) `0` · g) `1` · h) `True`.

**Démarche.**
- a) $\operatorname{tr}\mathbf{N} = 4$, $\det\mathbf{N} = -5 + 9 = 4$ : $\lambda^2 - 4\lambda + 4 = (\lambda - 2)^2$. b) $\mathbf{N} - 2\mathbf{I} = \begin{pmatrix} 3 & -9 \\ 1 & -3 \end{pmatrix}$, de rang 1 : $2 - 1 = 1$. c) $x = 3y$. d) Un seul vecteur propre libre.
- e) $\operatorname{tr}\mathbf{R} = 2\cos 60° = 1$, $\det\mathbf{R} = 1$ : $1 - 4 = -3$. f) Discriminant négatif. g) $\cos^2 + \sin^2 = 1$. h) $6 \times 60° = 360°$.

Pour la copie : la valeur propre est double, mais son espace propre n'est qu'une droite : il manque une direction (un cisaillement déguisé). $\mathbf{R}$ fait tourner toute direction de 60° : aucune ne reste sur sa droite. Ses valeurs propres sont $\frac{1 \pm i\sqrt{3}}{2}$, de produit $\frac{1 + 3}{4} = 1 = \det\mathbf{R}$.

**Erreurs fréquentes.** Conclure « diagonalisable » d'une valeur propre double sans regarder l'espace propre ; $\cos 60° = \frac{\sqrt{3}}{2}$.

**Variante.** La rotation de 180° a-t-elle des valeurs propres réelles ? *Réponse* : oui, $-1$ (double) : c'est $-\mathbf{I}$, diagonalisable.

### Ex M12c.7 — Le théorème spectral sur une matrice symétrique 2 × 2 : Q, Λ et QΛQᵀ

**Réponses** : a) `[30, 1]` · b) `[0.3714, 0.9285]` · c) `[0.9285, -0.3714]` · d) `0` · e) `[[4.1379, 10.3448], [10.3448, 25.8621]]` · f) `30` · g) `[1.0, 0.0333]` · h) `True`.

**Démarche.**
- a) $\lambda^2 - 31\lambda + 30 = (\lambda - 30)(\lambda - 1)$. b) $\mathbf{S} - 30\mathbf{I} = \begin{pmatrix} -25 & 10 \\ 10 & -4 \end{pmatrix}$ : $5x = 2y$, $(2, 5)/\sqrt{29}$. c) $\mathbf{S} - \mathbf{I} = \begin{pmatrix} 4 & 10 \\ 10 & 25 \end{pmatrix}$ : $2x + 5y = 0$, $(5, -2)/\sqrt{29}$.
- d) $10 - 10 = 0$. e) $\frac{30}{29}\begin{pmatrix} 4 & 10 \\ 10 & 25 \end{pmatrix}$. f) $30 \times 1$. g) $1$ et $\frac{1}{30} \approx 0{,}0333$. h) Valeurs propres positives.

Pour la copie : $\mathbf{Q} = \frac{1}{\sqrt{29}}\begin{pmatrix} 2 & 5 \\ 5 & -2 \end{pmatrix}$, $\boldsymbol{\Lambda} = \operatorname{diag}(30, 1)$ ; $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top = \frac{1}{29}\begin{pmatrix} 120 + 25 & 300 - 10 \\ 300 - 10 & 750 + 4 \end{pmatrix} = \mathbf{S}$. Les vecteurs propres de $\mathbf{S}^{-1}$ sont les mêmes ($\mathbf{q}_2$ va alors avec la plus grande valeur propre, 1).

**Erreurs fréquentes.** Oublier de normer ; un signe de convention inversé ; $\lambda_1\mathbf{q}_1\mathbf{q}_1^\top$ calculé sans normer $\mathbf{q}_1$.

**Variante.** La matrice $\lambda_2\mathbf{q}_2\mathbf{q}_2^\top$ ? *Réponse* : $\frac{1}{29}\begin{pmatrix} 25 & -10 \\ -10 & 4 \end{pmatrix}$.

### Ex M12c.8 — Le quotient de Rayleigh : le maximum et le minimum de xᵀAx sur le cercle unité

**Réponses** : a) `17` · b) `2` · c) `13.5` · d) `[18, 1]` · e) `18` · f) `[0.9701, 0.2425]` · g) `1` · h) `8.6436`.

**Démarche.**
- a) $s_{11} = 17$, b) $s_{22} = 2$. c) $\frac{17 + 8 + 2}{2} = 13{,}5$. d) $\lambda^2 - 19\lambda + 18 = (\lambda - 18)(\lambda - 1)$.
- e) Le maximum est $\lambda_{\max} = 18$, atteint en f) $(4, 1)/\sqrt{17}$ ($\mathbf{S} - 18\mathbf{I} = \begin{pmatrix} -1 & 4 \\ 4 & -16 \end{pmatrix}$). g) $\lambda_{\min} = 1$, en $(1, -4)/\sqrt{17}$.
- h) $\frac{17 \times 64 + 8 \times 120 + 2 \times 225}{289} = \frac{2498}{289} \approx 8{,}6436$.

Pour la copie : $R(\mathbf{x}) = \frac{18y_1^2 + y_2^2}{y_1^2 + y_2^2}$, une moyenne de 18 et 1 de poids $\frac{y_i^2}{y_1^2 + y_2^2}$. Pour $\mathbf{x} = (8, 15)/17$ : $y_1 = \mathbf{x} \cdot \mathbf{q}_1 = \frac{32 + 15}{17\sqrt{17}} = \frac{47}{17\sqrt{17}}$, $y_1^2 = \frac{2209}{4913} \approx 0{,}4496$ ; $R = 1 + 17 \times 0{,}4496 \approx 8{,}644$. a) n'est pas le maximum : $\mathbf{e}_1$ n'est pas vecteur propre, il « mélange » les deux directions ; un élément diagonal est un quotient de Rayleigh parmi d'autres, toujours entre $\lambda_{\min}$ et $\lambda_{\max}$.

**Erreurs fréquentes.** Prendre le plus grand élément de $\mathbf{S}$ pour son maximum ; oublier de diviser par $\mathbf{x}^\top\mathbf{x}$.

**Variante.** Le maximum de $\mathbf{x}^\top\mathbf{S}\mathbf{x}$ pour $\lVert \mathbf{x} \rVert = 2$ ? *Réponse* : $4 \times 18 = 72$.

### Ex M12c.9 — Trois itérations de la méthode de la puissance à la main

**Réponses** : a) `[5, -3]` · b) `[0.8575, -0.5145]` · c) `[0.0303, 0.9995]` · d) `[-0.4599, 0.888]` · e) `-6.7581` · f) `[3, -7]` · g) `[-0.3162, 0.9487]` · h) `0.4286`.

**Démarche.**
- a) $\mathbf{A}(1, 1) = (5, -3)$ ; b) la coordonnée de plus grande valeur absolue, 5, est positive : on divise par $\sqrt{34}$.
- c) $\mathbf{A}(5, -3) = (10 - 9, 15 + 18) = (1, 33)$ : 33 est positive ; divisé par $\sqrt{1\,090}$.
- d) $\mathbf{A}(1, 33) = (2 + 99, 3 - 198) = (101, -195)$ : la coordonnée de plus grande valeur absolue, $-195$, est **négative** : on change le signe, $(-101, 195)$, puis on divise par $\sqrt{48\,226}$.
- e) $\mathbf{A}(-101, 195) = (383, -1\,473)$ ; $\frac{(-101) \times 383 + 195 \times (-1\,473)}{48\,226} = \frac{-325\,918}{48\,226} \approx -6{,}7581$.
- f) $\lambda^2 + 4\lambda - 21 = (\lambda - 3)(\lambda + 7)$. g) Pour $-7$ : $\mathbf{A} + 7\mathbf{I} = \begin{pmatrix} 9 & 3 \\ 3 & 1 \end{pmatrix}$, direction $(1, -3)$, et la convention donne $(-1, 3)/\sqrt{10}$. h) $3/7$.

Pour la copie : $\lambda_1 = -7 < 0$, donc $\mathbf{A}\mathbf{x}_k$ pointe, à peu près, à l'opposé de $\mathbf{x}_k$ ; sans la convention, le vecteur changerait de signe à chaque pas et ne se stabiliserait jamais (c'est ce que la convention corrige en d)). Trois chiffres : $(3/7)^k = 10^{-3}$ pour $k \approx 8$. Avec $\mathbf{x}_0 = (3, 1)$, vecteur propre de 3 : $\mathbf{A}\mathbf{x}_0 = (9, 3) = 3\mathbf{x}_0$, la méthode resterait sur la mauvaise valeur propre (en exact ; les arrondis finiraient par y glisser un peu de $\mathbf{v}_1$).

**Erreurs fréquentes.** Ne pas normaliser ; oublier la convention de signe en d) ; prendre 3 pour la valeur propre dominante (c'est le **module** qui compte).

**Variante.** $\mathbf{x}_4$ ? *Réponse* : $\mathbf{A}(-101, 195) = (383, -1\,473)$, changé de signe : $(-383, 1\,473)/\sqrt{2\,316\,418} \approx (-0{,}2516 ;\ 0{,}9678)$.

### Ex M12c.10 — Définie positive ? Par les valeurs propres, les mineurs et la forme quadratique ; une hessienne qui prouve la convexité

**Réponses** : a) `[4, 8, 12]` · b) `True` · c) `[1, -1, -5]` · d) `-1` · e) `[[3, 2], [2, 6]]` · f) `24.3097` · g) `True` · h) `[7, 2]`.

**Démarche.**
- a) $4$ ; $12 - 4 = 8$ ; $4(6 - 1) + 2(-4 - 0) = 12$. b) Trois mineurs positifs (Sylvester).
- c) $1$ ; $3 - 4 = -1$ ; $1(12 - 1) - 2(8 - 0) = -5$. d) $4 - 8 + 3 = -1$.
- e) $f_{xx} = 2 + e^x$, $f_{xy} = 2$, $f_{yy} = 6$ ; en $(0, 0)$ : $\begin{pmatrix} 3 & 2 \\ 2 & 6 \end{pmatrix}$. f) $6(2 + e) - 4 = 8 + 6e \approx 24{,}3097$.
- g) $2 + e^x > 0$ et $8 + 6e^x > 0$ partout : hessienne définie positive en tout point, $f$ (strictement) convexe. h) $\lambda^2 - 9\lambda + 14 = (\lambda - 7)(\lambda - 2)$.

Pour la copie : d) exhibe un vecteur où la forme est négative : $\mathbf{H}_2$ n'est pas définie positive, comme le disait le deuxième mineur. $f$ est strictement convexe : elle a au plus un minimum ; elle en a un, car $\nabla f = (2x + 2y + e^x, 2x + 6y)$ s'annule quand $y = -x/3$ et $\frac{4}{3}x + e^x = 0$, qui a une solution unique (en $x \approx -0{,}469$, $y = -x/3 \approx 0{,}156$).

**Erreurs fréquentes.** Ne regarder que la diagonale ($\mathbf{H}_2$ a une diagonale positive) ; oublier que $f_{xx}$ dépend de $x$ ; écrire 1 au lieu de 2 hors de la diagonale de la hessienne.

**Variante.** $g(x, y) = x^2 + 5xy + 4y^2$ est-elle convexe ? *Réponse* : non, sa hessienne $\begin{pmatrix} 2 & 5 \\ 5 & 8 \end{pmatrix}$ a pour déterminant $16 - 25 = -9$.

### Ex M12c.11 — La décomposition de Cholesky d'une matrice 3 × 3

**Réponses** : a) `2` · b) `[-3, 1]` · c) `1` · d) `4` · e) `2` · f) `[[2, 0, 0], [-3, 1, 0], [1, 4, 2]]` · g) `16` · h) `[1, 0, -1]`.

**Démarche.**
- a) $\sqrt{4}$. b) $-6/2$ et $2/2$. c) $\sqrt{10 - 9} = 1$. d) $(1 - 1 \times (-3))/1 = 4$. e) $\sqrt{21 - 1 - 16} = 2$.
- g) $(2 \times 1 \times 2)^2 = 16$.
- h) $\mathbf{L}\mathbf{z} = (2, -7, -19)$ : $z_1 = 1$, $z_2 = -7 + 3 = -4$, $z_3 = (-19 - 1 + 16)/2 = -2$ ; puis $\mathbf{L}^\top\mathbf{x} = \mathbf{z}$ : $x_3 = -1$, $x_2 = -4 - 4 \times (-1) = 0$, $x_1 = (1 + 0 + 1)/2 = 1$.

Pour la copie : avec 17 au lieu de 21, $l_{33}^2 = 17 - 1 - 16 = 0$ : le pivot n'est pas strictement positif, la matrice n'est pas définie positive (seulement semi-définie : $\det = 0$).

**Erreurs fréquentes.** Oublier une racine ; $\mathbf{L}^\top$ au lieu de $\mathbf{L}$ ; des signes dans $l_{32}$ ; résoudre $\mathbf{L}^\top\mathbf{x} = \mathbf{z}$ en descendant.

**Variante.** Le premier élément de $\mathbf{A}^{-1}$, par Cholesky ? *Réponse* : résous $\mathbf{A}\mathbf{x} = \mathbf{e}_1$ : $x_1 = \frac{209}{16} \approx 13{,}06$.

### Ex M12c.12 — Une forme quadratique réduite à une somme de carrés, et ses lignes de niveau

**Réponses** : a) `[[2, 5], [5, 26]]` · b) `[27, 1]` · c) `[0.1961, 0.9806]` · d) `26` · e) `[5.1962, 1.0]` · f) `16.32` · g) `14.42` · h) `True`.

**Démarche.**
- a) $10xy = 5xy + 5yx$. b) $\lambda^2 - 28\lambda + 27 = (\lambda - 27)(\lambda - 1)$. c) $\mathbf{S} - 27\mathbf{I} = \begin{pmatrix} -25 & 5 \\ 5 & -1 \end{pmatrix}$ : $y = 5x$, $(1, 5)/\sqrt{26}$.
- d) $50 - 50 + 26 = 26$ ($(5, -1)$ est vecteur propre de 1, de carré de norme 26).
- e) $q = 27y_1^2 + y_2^2 = 27$ : $\sqrt{27/1} \approx 5{,}1962$ le long de $\mathbf{q}_2$, $\sqrt{27/27} = 1$ le long de $\mathbf{q}_1$. f) $\pi\sqrt{27} \approx 16{,}32$.
- g) Matrice $\begin{pmatrix} 2 & c/2 \\ c/2 & 26 \end{pmatrix}$, de déterminant $52 - c^2/4 \le 0$ pour $c \ge \sqrt{208} \approx 14{,}42$. h) Définie positive : $q = 0$ seulement en $\mathbf{0}$.

Pour la copie : $q = 27y_1^2 + y_2^2$ avec $y_1 = \frac{x + 5y}{\sqrt{26}}$ et $y_2 = \frac{5x - y}{\sqrt{26}}$. L'ellipse est la plus allongée le long de $\mathbf{q}_2 \propto (5, -1)$ : dans cette direction, $q$ monte le moins vite (valeur propre 1), il faut aller plus loin pour atteindre 27.

**Erreurs fréquentes.** $10$ hors de la diagonale ; les demi-axes $27$ et $1$ (les carrés) ; l'ellipse allongée le long de la grande valeur propre.

**Variante.** Les demi-axes de $q = 54$ ? *Réponse* : $\sqrt{54} \approx 7{,}35$ et $\sqrt{2} \approx 1{,}41$.

### Ex M12c.13 — La covariance d'un vecteur transformé, AΣAᵀ, et le blanchiment d'une covariance 2 × 2

**Réponses** : a) `37` · b) `[[37, -56], [-56, 400]]` · c) `[[6, 0], [-5, 6]]` · d) `[[0.1667, 0.0], [0.1389, 0.1667]]` · e) `[81, 16]` · f) `[[5.5385, -2.3077], [-2.3077, 7.4615]]` · g) `[[0.2073, 0.0641], [0.0641, 0.1538]]` · h) `[2.0, 1.6667]`.

**Démarche.**
- a) $36 + 61 + 2 \times (-30) = 37$. b) $\mathbf{A} = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}$ : $\mathbb{V}(x_1 - 2x_2) = 36 + 4 \times 61 - 4 \times (-30) = 400$ ; $\operatorname{Cov} = 36 - 2(-30) + (-30) - 2 \times 61 = -56$.
- c) $l_{11} = 6$, $l_{21} = -30/6 = -5$, $l_{22} = \sqrt{61 - 25} = 6$. d) $\mathbf{L}^{-1} = \begin{pmatrix} 1/6 & 0 \\ 5/36 & 1/6 \end{pmatrix}$.
- e) $\lambda^2 - 97\lambda + 1296 = (\lambda - 81)(\lambda - 16)$, de vecteurs propres $(2, -3)$ et $(3, 2)$.
- f) $\frac{9}{13}\begin{pmatrix} 4 & -6 \\ -6 & 9 \end{pmatrix} + \frac{4}{13}\begin{pmatrix} 9 & 6 \\ 6 & 4 \end{pmatrix} = \frac{1}{13}\begin{pmatrix} 72 & -30 \\ -30 & 97 \end{pmatrix}$.
- g) $\frac{1}{9 \times 13}\begin{pmatrix} 4 & -6 \\ -6 & 9 \end{pmatrix} + \frac{1}{4 \times 13}\begin{pmatrix} 9 & 6 \\ 6 & 4 \end{pmatrix} = \frac{1}{468}\begin{pmatrix} 97 & 30 \\ 30 & 72 \end{pmatrix}$.
- h) $\mathbf{L}^{-1}(12, 0) = (2, \frac{60}{36}) = (2 ;\ 1{,}6667)$.

Pour la copie : $\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top = \mathbf{L}^{-1}\mathbf{L}\mathbf{L}^\top\mathbf{L}^{-\top} = \mathbf{I}$. Le blanchiment de l'ACP a pour lignes $\frac{1}{9}\cdot\frac{(2, -3)}{\sqrt{13}}$ et $\frac{1}{4}\cdot\frac{(3, 2)}{\sqrt{13}}$ : il passe d'abord dans la base propre, alors que g) revient dans la base de départ ($\mathbf{Q}\boldsymbol{\Lambda}^{-1/2}\mathbf{Q}^\top$). Les deux diffèrent par la matrice orthogonale $\mathbf{Q}$ : g) $= \mathbf{Q} \times$ (blanchiment de l'ACP), et si $\mathbf{W}$ blanchit, $\mathbf{R}\mathbf{W}$ blanchit aussi pour toute $\mathbf{R}$ orthogonale ($\mathbf{R}\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top\mathbf{R}^\top = \mathbf{R}\mathbf{R}^\top = \mathbf{I}$, M12c.21) : le blanchiment n'est pas unique.

**Erreurs fréquentes.** Oublier les covariances ; $\boldsymbol{\Sigma}^{1/2}$ pris élément par élément (ici impossible : $\sqrt{-30}$) ; confondre $\boldsymbol{\Sigma}^{1/2}$ et $\boldsymbol{\Sigma}^{-1/2}$ ; $\mathbf{L}$ au lieu de $\mathbf{L}^{-1}$.

**Variante.** La distance de Mahalanobis de l'écart $(12, 0)$ ? *Réponse* : $\sqrt{4 + 25/9} = \frac{\sqrt{61}}{3} \approx 2{,}60$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M12c.14 — det A ≠ 0 si et seulement si A est inversible (det AB = det A det B admis)

**Réponse modèle.**
1. $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$, donc $\det\mathbf{A}\,\det(\mathbf{A}^{-1}) = \det\mathbf{I} = 1$. Un produit égal à 1 n'a aucun facteur nul : $\det\mathbf{A} \ne 0$, et $\det(\mathbf{A}^{-1}) = 1/\det\mathbf{A}$.
2. Chaque opération de l'élimination multiplie le déterminant par un nombre non nul : $-1$ pour un échange, $c \ne 0$ pour une ligne multipliée par $c$, 1 pour l'ajout d'un multiple d'une ligne. Donc $\det\mathbf{E} = c\,\det\mathbf{A}$, $c \ne 0$. Si $\mathbf{A}$ n'est pas inversible, son rang est inférieur à $n$ (M12a) : sa forme échelonnée a moins de $n$ pivots, donc une colonne sans pivot ; la matrice carrée échelonnée a alors un zéro sur sa diagonale (et sa dernière ligne est nulle). Triangulaire, son déterminant est le produit de la diagonale : 0. D'où $c\,\det\mathbf{A} = 0$ et $\det\mathbf{A} = 0$.
3. Des colonnes liées : $\mathbf{A}$ n'est pas inversible, donc $\det\mathbf{A} = 0$ par 2. Directement : si $\mathbf{a}_k = \sum_{j \ne k} c_j\mathbf{a}_j$, la linéarité selon la colonne $k$ écrit $\det\mathbf{A}$ comme $\sum_j c_j \det(\ldots, \mathbf{a}_j, \ldots, \mathbf{a}_j, \ldots)$, des déterminants à deux colonnes égales ; échanger ces deux colonnes ne change pas la matrice mais change le signe : chacun vaut 0.
4. $\det(\mathbf{S}^{-1}\mathbf{A}\mathbf{S}) = \det(\mathbf{S}^{-1})\det\mathbf{A}\det\mathbf{S} = \frac{1}{\det\mathbf{S}}\det\mathbf{A}\det\mathbf{S} = \det\mathbf{A}$.

**Grille.** (1) le produit avec l'inverse et la conclusion ; (2) le facteur non nul de chaque opération, la colonne sans pivot, le zéro de la diagonale ; (3) l'argument des deux colonnes égales ; (4) la multiplicativité et 1.

### Ex M12c.15 — Une matrice symétrique réelle : valeurs propres réelles, vecteurs propres de valeurs distinctes orthogonaux

**Réponse modèle.**
1. $(\mathbf{A}\mathbf{u}) \cdot \mathbf{v} = (\mathbf{A}\mathbf{u})^\top\mathbf{v} = \mathbf{u}^\top\mathbf{A}^\top\mathbf{v} = \mathbf{u}^\top\mathbf{A}\mathbf{v} = \mathbf{u} \cdot (\mathbf{A}\mathbf{v})$.
2. $(\mathbf{A}\mathbf{u}) \cdot \mathbf{v} = \lambda\,\mathbf{u} \cdot \mathbf{v}$ et $\mathbf{u} \cdot (\mathbf{A}\mathbf{v}) = \mu\,\mathbf{u} \cdot \mathbf{v}$. Par 1, $(\lambda - \mu)\,\mathbf{u} \cdot \mathbf{v} = 0$, et $\lambda \ne \mu$ : $\mathbf{u} \cdot \mathbf{v} = 0$.
3. $s = \bar{\mathbf{z}}^\top\mathbf{A}\mathbf{z}$ est un nombre ; son conjugué est $\mathbf{z}^\top\mathbf{A}\bar{\mathbf{z}}$ ($\mathbf{A}$ est réelle), égal à sa transposée $\bar{\mathbf{z}}^\top\mathbf{A}^\top\mathbf{z} = \bar{\mathbf{z}}^\top\mathbf{A}\mathbf{z} = s$ : $s$ est réel. $\bar{\mathbf{z}}^\top\mathbf{z} = \sum_i \bar{z}_iz_i = \sum_i |z_i|^2 > 0$ ($\mathbf{z} \ne \mathbf{0}$). Et $s = \bar{\mathbf{z}}^\top(\lambda\mathbf{z}) = \lambda\,\bar{\mathbf{z}}^\top\mathbf{z}$, donc $\lambda = s/\bar{\mathbf{z}}^\top\mathbf{z}$ est réel.
4. Les $n$ valeurs propres, réelles (3) et distinctes, donnent $n$ vecteurs propres réels, deux à deux orthogonaux (2) ; normés, ils forment une famille orthonormée de $n$ vecteurs, donc une base (M12b). Avec $\mathbf{Q}$ leurs colonnes, $\mathbf{A}\mathbf{Q} = \mathbf{Q}\boldsymbol{\Lambda}$ et $\mathbf{Q}^{-1} = \mathbf{Q}^\top$ : $\mathbf{A} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$.
5. $\begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}$ : $\lambda^2 - 5\lambda = 0$, réelles 5 et 0 ; vecteurs propres $(1, -2)$ et $(2, 1)$, de produit scalaire $2 - 2 = 0$.

**Grille.** (1) la transposée d'un produit et la symétrie ; (2) les deux calculs et la division par $\lambda - \mu$ ; (3) le conjugué de $s$, la positivité de $\bar{\mathbf{z}}^\top\mathbf{z}$, la conclusion ; (4) réels, orthogonaux, normés, $n$ vecteurs donc une base, puis la factorisation ; (5) les deux vérifications.

### Ex M12c.16 — La somme des valeurs propres est la trace, leur produit le déterminant

**Réponse modèle.**
1. $\det(\mathbf{A} - \lambda\mathbf{I}) = (a - \lambda)(d - \lambda) - bc = \lambda^2 - (a + d)\lambda + (ad - bc)$. Les racines $\lambda_1, \lambda_2$ vérifient $\lambda_1 + \lambda_2 = a + d$ et $\lambda_1\lambda_2 = ad - bc$ (somme et produit des racines, R3).
2. $p_{\mathbf{A}}(0) = \det\mathbf{A}$ d'un côté, $\lambda_1\lambda_2\cdots\lambda_n$ de l'autre.
3. $\operatorname{tr}\mathbf{A} = \operatorname{tr}(\mathbf{P}\mathbf{D}\mathbf{P}^{-1}) = \operatorname{tr}(\mathbf{D}\mathbf{P}^{-1}\mathbf{P}) = \operatorname{tr}\mathbf{D} = \sum\lambda_i$ ; $\det\mathbf{A} = \det\mathbf{P}\,\det\mathbf{D}\,\det(\mathbf{P}^{-1}) = \det\mathbf{D} = \prod\lambda_i$.
4. $1 + \lambda_2 + \lambda_3 = 6$ et $1 \times \lambda_2\lambda_3 = 6$ : $\lambda_2 + \lambda_3 = 5$, $\lambda_2\lambda_3 = 6$, soit 2 et 3.
5. $p(\lambda) = \lambda^2 + \det\mathbf{A}$, avec $\det\mathbf{A} > 0$ : pas de racine réelle.

**Grille.** (1) le développement et les relations racines-coefficients ; (2) l'évaluation en 0 des deux écritures ; (3) l'invariance de la trace et la multiplicativité du déterminant ; (4) le système somme-produit ; (5) le discriminant négatif.

### Ex M12c.17 — Une matrice de covariance, et toute matrice de Gram XᵀX, est symétrique semi-définie positive

**Réponse modèle.**
1. $\mathbf{G}^\top = \mathbf{X}^\top(\mathbf{X}^\top)^\top = \mathbf{X}^\top\mathbf{X}$. Et $\mathbf{w}^\top\mathbf{X}^\top\mathbf{X}\mathbf{w} = (\mathbf{X}\mathbf{w})^\top(\mathbf{X}\mathbf{w}) = \lVert \mathbf{X}\mathbf{w} \rVert^2 \ge 0$.
2. $\mathbf{w}^\top\mathbf{G}\mathbf{w} = 0 \iff \mathbf{X}\mathbf{w} = \mathbf{0}$. Si les colonnes sont libres, cela force $\mathbf{w} = \mathbf{0}$ : définie positive. Sinon, un $\mathbf{w} \ne \mathbf{0}$ du noyau donne $\mathbf{w}^\top\mathbf{G}\mathbf{w} = 0$ : pas définie.
3. $\boldsymbol{\Sigma} = \frac{1}{n-1}\mathbf{G}$ avec $\mathbf{X} = \mathbf{X}_c$, et $\frac{1}{n-1} > 0$.
4. $\mathbf{a}^\top\mathbf{x} - \mathbb{E}[\mathbf{a}^\top\mathbf{x}] = \mathbf{a}^\top(\mathbf{x} - \boldsymbol{\mu})$, donc $\mathbb{V}(\mathbf{a}^\top\mathbf{x}) = \mathbb{E}[(\mathbf{a}^\top(\mathbf{x} - \boldsymbol{\mu}))^2] = \mathbb{E}[\mathbf{a}^\top(\mathbf{x} - \boldsymbol{\mu})(\mathbf{x} - \boldsymbol{\mu})^\top\mathbf{a}] = \mathbf{a}^\top\boldsymbol{\Sigma}\mathbf{a}$, une variance, positive ou nulle. $\boldsymbol{\Sigma}$ est symétrique ($\mathbf{v}\mathbf{v}^\top$ l'est) et semi-définie positive.
5. Quand les colonnes de $\mathbf{X}_c$ sont liées : une combinaison des features est constante sur les données. Exemples : $x_3 = x_1 + x_2$ donne $\mathbf{w} = (1, 1, -1)$ avec $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w} = 0$ ; avec $p > n$ features (et même dès $p \ge n$), $\mathbf{X}_c$ a un rang au plus $n - 1 < p$ (centrer fait perdre un rang : les lignes centrées ont une somme nulle).

**Grille.** (1) la symétrie et la norme au carré ; (2) les deux sens, avec le noyau ; (3) le facteur positif ; (4) le calcul de la variance et la conclusion ; (5) les deux exemples et la raison (le rang).

### Ex M12c.18 — Le quotient de Rayleigh d'une matrice symétrique est entre λ_min et λ_max

**Réponse modèle.**
1. $\mathbf{Q}$ est inversible, donc $\mathbf{y} = \mathbf{Q}^\top\mathbf{x} \ne \mathbf{0}$ ; $\mathbf{y}^\top\mathbf{y} = \mathbf{x}^\top\mathbf{Q}\mathbf{Q}^\top\mathbf{x} = \mathbf{x}^\top\mathbf{x}$ ; $\mathbf{x}^\top\mathbf{A}\mathbf{x} = \mathbf{x}^\top\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top\mathbf{x} = \mathbf{y}^\top\boldsymbol{\Lambda}\mathbf{y} = \sum\lambda_iy_i^2$.
2. $\lambda_n\sum y_i^2 \le \sum\lambda_iy_i^2 \le \lambda_1\sum y_i^2$ ; on divise par $\sum y_i^2 > 0$.
3. $R(\mathbf{x}) = \lambda_1 \iff \sum(\lambda_1 - \lambda_i)y_i^2 = 0$, une somme de termes positifs : $y_i = 0$ dès que $\lambda_i < \lambda_1$. Alors $\mathbf{x} = \mathbf{Q}\mathbf{y}$ est une combinaison des $\mathbf{q}_i$ de valeur propre $\lambda_1$ : un vecteur propre de $\lambda_1$. Réciproquement, un vecteur propre de $\lambda_1$ donne $R = \lambda_1$.
4. $\mathbf{x} \perp \mathbf{q}_1$ veut dire $y_1 = \mathbf{q}_1 \cdot \mathbf{x} = 0$ ; alors $\sum_{i \ge 2}\lambda_iy_i^2 \le \lambda_2\sum y_i^2$, avec égalité en $\mathbf{x} = \mathbf{q}_2$.
5. $\mathbf{x}^\top\mathbf{A}\mathbf{x} = R(\mathbf{x})\lVert \mathbf{x} \rVert^2 \in [2 \times 9 ;\ 7 \times 9] = [18 ; 63]$. Oui : toutes ses valeurs propres sont positives.

**Grille.** (1) les trois égalités, avec $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}$ ; (2) l'encadrement terme à terme et la division ; (3) les deux sens du cas d'égalité ; (4) la traduction de l'orthogonalité en $y_1 = 0$ ; (5) le facteur $\lVert \mathbf{x} \rVert^2 = 9$.

### Ex M12c.19 — ½ xᵀAx − bᵀx, avec A définie positive, a un unique minimum, en A⁻¹b

**Réponse modèle.** $\mathbf{A}$, définie positive, n'a pas de valeur propre nulle : elle est inversible, et $\mathbf{x}^*$ existe.
1. $f(\mathbf{x}^* + \mathbf{h}) = \frac{1}{2}\mathbf{x}^{*\top}\mathbf{A}\mathbf{x}^* + \frac{1}{2}\mathbf{x}^{*\top}\mathbf{A}\mathbf{h} + \frac{1}{2}\mathbf{h}^\top\mathbf{A}\mathbf{x}^* + \frac{1}{2}\mathbf{h}^\top\mathbf{A}\mathbf{h} - \mathbf{b}^\top\mathbf{x}^* - \mathbf{b}^\top\mathbf{h}$. Par symétrie, les deux termes croisés valent $\mathbf{h}^\top\mathbf{A}\mathbf{x}^* = \mathbf{h}^\top\mathbf{b}$, et s'annulent avec $-\mathbf{b}^\top\mathbf{h}$. Reste $f(\mathbf{x}^*) + \frac{1}{2}\mathbf{h}^\top\mathbf{A}\mathbf{h}$.
2. $\frac{1}{2}\mathbf{h}^\top\mathbf{A}\mathbf{h} > 0$ pour $\mathbf{h} \ne \mathbf{0}$ : $f(\mathbf{x}) > f(\mathbf{x}^*)$ pour tout $\mathbf{x} \ne \mathbf{x}^*$. Et $f(\mathbf{x}^*) = \frac{1}{2}\mathbf{x}^{*\top}\mathbf{b} - \mathbf{b}^\top\mathbf{x}^* = -\frac{1}{2}\mathbf{b}^\top\mathbf{x}^*$.
3. Semi-définie : si $\mathbf{A}\mathbf{x}^* = \mathbf{b}$ a une solution ($\mathbf{b}$ dans l'image), le calcul tient, avec $\frac{1}{2}\mathbf{h}^\top\mathbf{A}\mathbf{h} \ge 0$ : des minima, mais tout $\mathbf{x}^* + \mathbf{h}$ avec $\mathbf{h} \in \ker\mathbf{A}$ en est un aussi (pas d'unicité). Si $\mathbf{b}$ n'est pas dans l'image, $f$ n'a pas de minimum : prendre $\mathbf{h} \in \ker\mathbf{A}$ avec $\mathbf{b}^\top\mathbf{h} > 0$ (il existe, car $\mathbf{b} \notin \operatorname{Im}\mathbf{A} = (\ker\mathbf{A})^\perp$) et $f(t\mathbf{h}) = -t\,\mathbf{b}^\top\mathbf{h} \to -\infty$.
4. $\frac{1}{2}\lVert \mathbf{X}\mathbf{w} - \mathbf{y} \rVert^2 = \frac{1}{2}\mathbf{w}^\top\mathbf{X}^\top\mathbf{X}\mathbf{w} - (\mathbf{X}^\top\mathbf{y})^\top\mathbf{w} + \frac{1}{2}\lVert \mathbf{y} \rVert^2$ : $\mathbf{A} = \mathbf{X}^\top\mathbf{X}$, $\mathbf{b} = \mathbf{X}^\top\mathbf{y}$, $c = \frac{1}{2}\lVert \mathbf{y} \rVert^2$ ; le minimum vérifie $\mathbf{X}^\top\mathbf{X}\,\mathbf{w} = \mathbf{X}^\top\mathbf{y}$, les équations normales.

**Grille.** (0) l'existence de $\mathbf{A}^{-1}$ ; (1) le développement et la symétrie pour les termes croisés ; (2) la stricte positivité et la valeur du minimum ; (3) les deux cas du semi-défini ; (4) l'identification et les équations normales.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12c.20 — Pont : la variance d'une somme pondérée de trois features, wᵀΣw, et pourquoi Σ doit être semi-définie positive

**Réponses** : a) `29` · b) `37` · c) `17` · d) `57` · e) `2` · f) `-2` · g) `False` · h) `0.3333`.

**Démarche.**
- a) $4 + 9 + 16$. b) $\mathbf{1}^\top\boldsymbol{\Sigma}\mathbf{1}$, la somme de tous les éléments : $29 + 2(2 - 1 + 3) = 37$. c) $4 \times 4 + 9 - 2 \times 2 \times 2 = 17$.
- d) $\boldsymbol{\Sigma}\mathbf{w} = (0, -1, 28)$, puis $\mathbf{w} \cdot (0, -1, 28) = 1 + 56 = 57$. e) $\Sigma_{13} + \Sigma_{23} = -1 + 3 = 2$.
- f) $2 + 2 - 2 \times 3 = -2$. g) Une variance ne peut pas être négative. h) $\frac{2}{2 \times 3}$.

Pour la copie : $\mathbb{V}(\sum x_i) = \sum_{i,j}\operatorname{Cov}(x_i, x_j)$, la somme de tous les éléments. Mineurs de $\boldsymbol{\Sigma}$ : $4$, $36 - 4 = 32$, $455$ : définie positive. d) est la variance de la prédiction $\hat{y} = \mathbf{w}^\top\mathbf{x}$ quand les features varient : elle dit combien la sortie du modèle bouge d'un exemple à l'autre.

**Erreurs fréquentes.** Oublier les covariances, ou ne les compter qu'une fois ; diviser la covariance par le produit des **variances**.

**Variante.** $\mathbb{V}(x_2 - x_3)$ ? *Réponse* : $9 + 16 - 6 = 19$.

### Ex M12c.21 — Pont : après un blanchiment, la covariance est l'identité

**Réponses** : a) `[[3, 0], [2, 2]]` · b) `[[0.3333, 0.0], [-0.3333, 0.5]]` · c) `[[1, 0], [0, 1]]` · d) `[2.0, -1.5]` · e) `2.5` · f) `[[1, 0], [0, 1]]` · g) `True` · h) `False`.

**Démarche.**
- a) $l_{11} = 3$, $l_{21} = 2$, $l_{22} = \sqrt{8 - 4} = 2$. b) $\mathbf{L}^{-1} = \begin{pmatrix} 1/3 & 0 \\ -2/6 & 1/2 \end{pmatrix}$. c) Par construction.
- d) $(\frac{6}{3}, -\frac{6}{3} + \frac{1}{2}) = (2 ;\ -1{,}5)$. e) $\sqrt{4 + 2{,}25} = 2{,}5$.
- f) $\mathbf{R}\mathbf{I}\mathbf{R}^\top = \mathbf{I}$ ($\mathbf{R}$ est orthogonale). g) $(\mathbf{R}\mathbf{W})\boldsymbol{\Sigma}(\mathbf{R}\mathbf{W})^\top = \mathbf{R}\mathbf{R}^\top = \mathbf{I}$. h) Non (ci-dessous).

Pour la copie : $\boldsymbol{\Sigma}^{-1} = \frac{1}{36}\begin{pmatrix} 8 & -6 \\ -6 & 9 \end{pmatrix}$ et $\frac{1}{36}(8 \times 36 - 12 \times 6 + 9) = \frac{225}{36}$, de racine $\frac{15}{6} = 2{,}5$. h) : $\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top = \mathbf{I}$ donne $\boldsymbol{\Sigma} = \mathbf{W}^{-1}\mathbf{W}^{-\top}$, donc $\mathbf{W}^\top\mathbf{W} = \boldsymbol{\Sigma}^{-1}$ pour **tout** blanchiment, et $\lVert \mathbf{W}\mathbf{d} \rVert^2 = \mathbf{d}^\top\boldsymbol{\Sigma}^{-1}\mathbf{d}$. Après blanchiment, les features ne sont plus corrélées : un modèle à distances ne voit plus la corrélation, il mesure les écarts « en nombre d'écarts-types », dans toutes les directions à la fois.

**Erreurs fréquentes.** Le signe de l'élément sous la diagonale de $\mathbf{L}^{-1}$ ; $\mathbf{z} = \mathbf{L}(\mathbf{x} - \boldsymbol{\mu})$ ; croire que la distance de Mahalanobis dépend du blanchiment choisi.

**Variante.** La distance de Mahalanobis de $\mathbf{x} - \boldsymbol{\mu} = (3, 2)$ ? *Réponse* : $\mathbf{z} = (1, 0)$, distance 1.

### Ex M12c.22 — MML §4.1 et §4.2 : déterminant, trace, valeurs propres, en anglais

**Réponse modèle** (avec tes mots ; les tiens peuvent différer).
1. Le livre part des petites matrices et du lien avec l'inversibilité : une matrice carrée est inversible si et seulement si son déterminant n'est pas nul (et, plus loin, si et seulement si son rang vaut $n$). Il appelle le développement selon une ligne ou une colonne *Laplace expansion*, avec les sous-matrices obtenues en supprimant une ligne et une colonne.
2. En dimension 2, $|\det|$ est l'aire du parallélogramme construit sur les colonnes ; en dimension 3, le volume du parallélépipède. Le signe dit l'**orientation** des vecteurs par rapport à la base canonique : c'est un volume *signé*.
3. Linéarité ($\operatorname{tr}(\mathbf{A} + \mathbf{B})$, $\operatorname{tr}(\alpha\mathbf{A})$), $\operatorname{tr}(\mathbf{I}_n) = n$, $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}(\mathbf{B}\mathbf{A})$, et plus généralement l'invariance par permutation circulaire. C'est elle qui donne $\operatorname{tr}(\mathbf{S}^{-1}\mathbf{A}\mathbf{S}) = \operatorname{tr}\mathbf{A}$ : la trace d'une application linéaire ne dépend pas de la base.
4. $\mathbf{A}\mathbf{x} = \lambda\mathbf{x}$, $\mathbf{x} \ne \mathbf{0}$ ; l'espace propre est l'ensemble des vecteurs propres de $\lambda$ avec $\mathbf{0}$ (le noyau de $\mathbf{A} - \lambda\mathbf{I}$). Formulations équivalentes : $\lambda$ est valeur propre ; $(\mathbf{A} - \lambda\mathbf{I})\mathbf{x} = \mathbf{0}$ a une solution non nulle (fiche §3, le noyau) ; $\operatorname{rk}(\mathbf{A} - \lambda\mathbf{I}) < n$ (M12a) ; $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ (fiche §1 et §3).
5. Multiplicité algébrique : la multiplicité comme racine du polynôme caractéristique ; géométrique : la dimension de l'espace propre (au plus l'algébrique). Une matrice $n \times n$ est défective si elle a moins de $n$ vecteurs propres libres. Exemple : $\begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}$, valeur propre 3 de multiplicité algébrique 2 et géométrique 1.
6. Pour toute matrice $\mathbf{A}$ de forme $(m, n)$, $\mathbf{A}^\top\mathbf{A}$ est symétrique semi-définie positive, et définie positive si le rang vaut $n$ : c'est M12c.17, démontré de la même façon ($\mathbf{x}^\top\mathbf{A}^\top\mathbf{A}\mathbf{x} = \lVert \mathbf{A}\mathbf{x} \rVert^2$).
7. Par exemple : *eigenspace* (espace propre), *defective* (défective), *characteristic polynomial* (polynôme caractéristique), *signed volume* (volume orienté).

**Grille.** (1) le lien avec l'inversibilité et le nom du développement ; (2) l'aire, le volume, le signe ; (3) les propriétés et l'invariance par changement de base ; (4) les définitions et les formulations reliées à la fiche ; (5) les deux multiplicités, « défective », un exemple refait ; (6) le théorème sur $\mathbf{A}^\top\mathbf{A}$ et M12c.17 ; (7) trois mots traduits.

### Ex M12c.23 — MML §4.3 et §4.4 : Cholesky, diagonalisation et décomposition spectrale

**Réponse modèle** (avec tes mots).
1. Toute matrice symétrique définie positive s'écrit de façon unique $\mathbf{L}\mathbf{L}^\top$, avec $\mathbf{L}$ triangulaire inférieure à diagonale positive ; $\mathbf{L}$ est le **facteur de Cholesky** (*Cholesky factor*). Le livre compare la décomposition à la racine carrée d'un nombre.
2. Les matrices de covariance d'une loi normale multivariée sont symétriques définies positives : Cholesky sert à tirer des échantillons (fiche §8, « Le chemin inverse »), à transformer des variables aléatoires (l'astuce de reparamétrisation des autoencodeurs variationnels, M25b), et à calculer des déterminants.
3. $\det\mathbf{A} = \det\mathbf{L}\,\det\mathbf{L}^\top = (\det\mathbf{L})^2 = \prod_i l_{ii}^2$. M12c.11 : $(2 \times 1 \times 2)^2 = 16$.
4. Diagonalisable : semblable à une matrice diagonale, $\mathbf{D} = \mathbf{P}^{-1}\mathbf{A}\mathbf{P}$ ; deux matrices sont semblables s'il existe une telle $\mathbf{P}$ inversible. Condition : $\mathbf{A}$ est diagonalisable si et seulement si ses vecteurs propres forment une base de $\mathbb{R}^n$.
5. Une matrice symétrique peut toujours être diagonalisée, avec une base orthonormée de vecteurs propres : $\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^\top$. Géométrie : $\mathbf{P}^{-1}$ passe dans la base propre, $\mathbf{D}$ étire chaque axe, $\mathbf{P}$ revient dans la base de départ.
6. Les puissances, $\mathbf{A}^k = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$, et le déterminant, $\det\mathbf{A} = \det\mathbf{D}$. M12c.5 : $\det(\mathbf{A}^{10}) = 2^{10} \times 1 = 1024$.
7. Par exemple : *Cholesky factor* (facteur de Cholesky), *similar* (semblables), *eigendecomposition* (décomposition en éléments propres), *basis change* (changement de base).

**Grille.** (1) l'énoncé, le nom, l'unicité ; (2) au moins deux usages reliés à la fiche ; (3) le déterminant et la vérification ; (4) les deux définitions et la condition ; (5) le cas symétrique et la géométrie ; (6) un calcul refait ; (7) trois mots traduits.

### Ex M12c.24 — Fermi : un déterminant 20 × 20 par cofacteurs ou par élimination, combien d'opérations ?

**Réponse modèle.**
1. $20! \approx 2{,}4 \times 10^{18}$ (Stirling : $\sqrt{40\pi}\,(20/e)^{20} \approx 11{,}2 \times 7{,}4^{20} \approx 2{,}4 \times 10^{18}$).
2. $2{,}4 \times 10^{18}/10^9 = 2{,}4 \times 10^9$ s, soit environ 77 ans (une année : $3{,}2 \times 10^7$ s ; en comptant aussi les $n - 1$ multiplications de chaque produit, plutôt un siècle ou deux, le même ordre de grandeur). C'est une vie humaine, rien à côté de l'âge de l'Univers. Pour $30 \times 30$ : $2{,}7 \times 10^{32}/10^9 \approx 2{,}7 \times 10^{23}$ s, soit $8 \times 10^{15}$ ans, près d'un million de fois l'âge de l'Univers. Dix lignes et colonnes de plus multiplient le temps par $30!/20! \approx 10^{14}$ : c'est la croissance de la factorielle.
3. $\frac{2}{3} \times 8\,000 \approx 5\,300$ opérations : environ 5 microsecondes.
4. $\frac{2}{3} \times 10^9$ opérations : moins d'une seconde.
5. $n! < 10^9$ : jusqu'à $n = 12$ ($12! \approx 4{,}8 \times 10^8$, $13! \approx 6{,}2 \times 10^9$).

**Grille.** (1) un ordre de grandeur juste de $20!$ ; (2) la conversion en années, les deux comparaisons et la croissance de $n!$ ; (3) et (4) la formule en $n^3$ appliquée ; (5) la limite vers $n = 12$.

### Ex M12c.25 — Expliquer un vecteur propre avec une image

**Réponse modèle.**

> Imagine une photo imprimée sur une feuille de caoutchouc, qu'on étire en tirant sur les bords. En général, un trait dessiné sur la feuille change de direction en plus de changer de longueur : il penche. Mais certaines directions sont privilégiées : un trait tracé dans l'une d'elles reste sur sa droite, il est seulement allongé, raccourci ou retourné. Ce sont les directions propres, et le facteur d'étirement est la valeur propre : plus grand que 1, le trait s'allonge ; entre 0 et 1, il rétrécit ; négatif, il se retourne. Si l'on fait tourner la feuille au lieu de l'étirer, aucune direction ne reste en place : pas de direction propre du tout.

**Grille.** (1) ce qu'une transformation fait en général (elle change les directions) ; (2) les directions qui restent sur leur droite ; (3) la valeur propre : étirement, écrasement, retournement ; (4) un exemple sans direction propre (une rotation) ; huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M12c.E1 — « Que représentent les valeurs propres d'une matrice de covariance ? »

**Réponse modèle (60 secondes).**

> Une matrice de covariance est symétrique, donc elle a des valeurs propres réelles et des vecteurs propres orthogonaux : ce sont des axes perpendiculaires dans l'espace des features. Chaque valeur propre est la variance des données projetées sur l'axe correspondant : la plus grande donne la direction où les données s'étalent le plus, la plus petite celle où elles varient le moins. Elles sont positives ou nulles, parce qu'une variance ne peut pas être négative : la matrice est semi-définie positive. Leur somme est la trace, la variance totale des features, qui ne change pas quand on tourne les axes. Une valeur propre nulle veut dire qu'une combinaison de features est constante : des features redondantes ; une valeur presque nulle annonce une matrice mal conditionnée. C'est la base de l'ACP : on garde les axes des plus grandes valeurs propres pour réduire la dimension en perdant le moins de variance.

**Grille.** (1) symétrique : axes orthogonaux ; (2) valeur propre = variance le long de son axe ; (3) positives, et pourquoi ; (4) la somme = la variance totale ; (5) une valeur propre nulle ou presque ; (6) un usage (ACP, conditionnement).

### M12c.E2 — « Comment savoir qu'une matrice est définie positive, et pourquoi est-ce important en optimisation ? »

**Réponse modèle (60 secondes).**

> Une matrice symétrique est définie positive si $x^\top A x$ est strictement positif pour tout vecteur non nul. Trois tests équivalents : toutes ses valeurs propres sont strictement positives ; les déterminants des sous-matrices en haut à gauche sont positifs (le critère de Sylvester) ; ou sa décomposition de Cholesky existe. Sur ordinateur, on essaie Cholesky : c'est rapide, et l'échec dit non. En optimisation, la hessienne joue ce rôle : si elle est définie positive en un point critique, c'est un minimum local ; si elle est semi-définie positive partout, la fonction est convexe, et tout minimum local est global. Pour une quadratique $\frac{1}{2}x^\top A x - b^\top x$ avec $A$ définie positive, le minimum est unique, solution de $Ax = b$. En machine learning, c'est le cas des moindres carrés, dont la hessienne est $X^\top X$, et de la ridge, qui ajoute $\alpha I$ pour la rendre définie positive même avec des features redondantes.

**Grille.** (1) la définition ; (2) deux ou trois critères ; (3) Cholesky sur ordinateur ; (4) hessienne, minimum local, convexité ; (5) le minimum unique d'une quadratique ; (6) un exemple en ML.

<a id="notebook"></a>

## Notebook

### Ex M12c.26 — Le déterminant par élimination · `det`

**Réponses** : a) `22.0` · b) `8.0` · c) `True` · d) `True` · e) `True` · f) `"ValueError"` · g) `True`.

**Démarche.** `M = np.array(A, dtype=float)` (une copie), une `ValueError` si `M.ndim != 2` ou si la matrice n'est pas carrée, `sign = 1.0`. Pour chaque colonne `k` : `p = k + int(np.argmax(np.abs(M[k:, k])))` ; si `M[p, k] == 0`, `return 0.0` ; si `p != k`, échanger les lignes (`M[[k, p]] = M[[p, k]]`) et `sign = -sign` ; puis retirer à chaque ligne `i > k` le multiple `M[i, k] / M[k, k]` de la ligne `k`. À la fin : `float(sign * np.prod(np.diag(M)))`. Pour la copie : a) sans pivot partiel, $L_2 + 2L_1 = (0, 6, 8)$, $L_3 - 3L_1 = (0, -8, -7)$, puis $-7 + \frac{8}{6} \times 8 = \frac{11}{3}$ : $1 \times 6 \times \frac{11}{3} = 22$ ; b) le pivot partiel remonte $(3, -1, 2)$ (un échange) ; $L_3 \leftarrow L_3 - \frac{1}{3}L_1$ donne $(0, \frac{4}{3}, -\frac{2}{3})$ ; dans la colonne 2, le pivot $2$ est plus grand que $\frac{4}{3}$ : pas d'autre échange ; $L_3 \leftarrow L_3 - \frac{2}{3}L_2$ donne $-\frac{4}{3}$ ; $\det = -(3 \times 2 \times (-\frac{4}{3})) = 8$ ; d) `repr` affiche `0.0` : la docstring promet un `float` de Python (`np.float64(0.0)` trahit un oubli de `float(...)`), et `-0.0`, égal à 0, viendrait d'un signe négatif multiplié par un produit nul, un affichage trompeur.

**Erreurs fréquentes.** Oublier le signe des échanges ; prendre le premier pivot non nul au lieu du plus grand ; rendre `np.float64` ou `-0.0` ; modifier la matrice reçue (`np.asarray`).

### Ex M12c.27 — La méthode de la puissance et le quotient de Rayleigh · `power_iteration, rayleigh_quotient`

**Réponses** : a) `4.732051` · b) `[0.788675, 0.57735, 0.211325]` · c) `4.333333` · d) `True` · e) `[-5.0, 1.0, 0.0, 0.0]` · f) `"ValueError"` · g) `"ValueError"`.

**Démarche.** `rayleigh_quotient` : formes, `x @ x != 0`, puis `float(x @ A @ x / (x @ x))`. `power_iteration` : `x = np.ones(n)` ou la copie de `x0`, normalisée puis passée dans `fix_sign` ; dans la boucle, `y = A @ x`, une `ValueError` si `‖y‖ = 0`, `x_new = fix_sign(y / ‖y‖)`, un compteur, et l'arrêt dès que `‖x_new − x‖ ≤ tol` (après avoir remplacé `x`). Rendre `(float(x @ A @ x), x, iterations)`. Pour la copie : les valeurs propres de $\mathbf{S}$ sont $3 + \sqrt{3}$, 3 et $3 - \sqrt{3}$, de rapport $3/(3 + \sqrt{3}) \approx 0{,}63$ : un chiffre gagné tous les 5 pas environ, 58 itérations pour $10^{-12}$ ; c) $\frac{13}{3}$ est un quotient de Rayleigh, une moyenne pondérée des valeurs propres, proche de la plus grande sans l'atteindre, parce que $(1, 1, 1)/\sqrt{3}$ est proche du vecteur propre b) sans lui être égal (leur produit scalaire vaut environ 0,91) ; e) sans la convention, $\mathbf{x}$ change de signe à chaque pas et l'arrêt n'arrive jamais.

**Erreurs fréquentes.** Comparer $\mathbf{x}_{\text{new}}$ à $\mathbf{x}_0$ non normalisé ; rendre $\lVert \mathbf{A}\mathbf{x} \rVert$ (toujours positif) au lieu du quotient de Rayleigh ; compter les itérations à partir de 0 ; oublier la `ValueError` quand $\mathbf{A}\mathbf{x} = \mathbf{0}$.

### Ex M12c.28 — La décomposition de Cholesky et le test « définie positive » · `cholesky, is_positive_definite`

**Réponses** : a) `[[5.0, 0.0, 0.0], [-2.0, 1.0, 0.0], [3.0, 2.0, 2.0]]` · b) `True` · c) `[True, False, False, False, True]` · d) `"ValueError"` · e) `"ValueError"` · f) `"ValueError"` · g) `True`.

**Démarche.** Copie, formes, symétrie relative (`np.abs(M - M.T) > 1e-12 * max(1, np.max(np.abs(M)))`), `L = np.zeros((n, n))`, puis pour chaque colonne `j` : `pivot = M[j, j] - L[j, :j] @ L[j, :j]`, une `ValueError` si `not pivot > 0`, `L[j, j] = np.sqrt(pivot)`, `L[j + 1:, j] = (M[j + 1:, j] - L[j + 1:, :j] @ L[j, :j]) / L[j, j]`. `is_positive_definite` : contrôle de la forme d'abord (la `ValueError` doit sortir), puis `try: cholesky(M)` / `except ValueError: return False` / `return True`. Pour la copie : a) $l_{11} = 5$, $l_{21} = -2$, $l_{31} = 3$, $l_{22} = \sqrt{5 - 4} = 1$, $l_{32} = (-4 + 6)/1 = 2$, $l_{33} = \sqrt{17 - 9 - 4} = 2$. c) La première a pour mineurs 5, 11 et 39 (définie positive) ; $\det\begin{pmatrix} 2 & 4 \\ 4 & 7 \end{pmatrix} = -2$ (indéfinie) ; $\operatorname{diag}(1, 0)$ est seulement semi-définie (pivot nul) ; $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ n'est pas symétrique ; $(6)$ est définie positive. d) n'est pas symétrique ; e) est symétrique mais indéfinie ($\det = -5$, le second pivot vaut $4 - 9 < 0$).

**Erreurs fréquentes.** Rendre $\mathbf{L}^\top$ ; une tolérance de symétrie absolue (refuse les grandes matrices) ; `pivot < 0` au lieu de `not pivot > 0` (accepte un pivot nul, puis divise par 0) ; attraper toutes les exceptions dans `is_positive_definite`.

### Ex M12c.29 — La racine carrée d'une matrice symétrique positive et la matrice de blanchiment · `sqrtm_psd, whitening_matrix`

**Réponses** : a) `[[4.0, 1.0], [1.0, 2.0]]` · b) `[[2.84605, 0.948683], [0.948683, 0.316228]]` · c) `[[0.632456, 0.316228], [0.316228, 0.948683]]` · d) `[[0.5, 0.0], [0.5, 1.0]]` · e) `True` · f) `"ValueError"` · g) `"ValueError"`.

**Démarche.** `values, Q = np.linalg.eigh(M)` ; pour `sqrtm_psd`, une `ValueError` si `values.min() < -tol * max(1, values.max())`, puis `(Q * np.sqrt(np.clip(values, 0, None))) @ Q.T` ; pour ZCA, une `ValueError` si une valeur propre est $\le 0$, puis `(Q / np.sqrt(values)) @ Q.T` ; pour Cholesky, `np.linalg.solve(cholesky(M), np.eye(p))`. Pour la copie : b) existe parce que les valeurs propres, 10 et 0, sont positives ou nulles ; $\mathbf{L} = \begin{pmatrix} 2 & 0 \\ -1 & 1 \end{pmatrix}$ pour d) ; c) vaut $\frac{1}{\sqrt{10}}\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$, symétrique par construction, et son carré est $\boldsymbol{\Sigma}^{-1}$.

**Erreurs fréquentes.** La racine des éléments ; oublier de remettre à 0 les valeurs propres de l'ordre de $-10^{-16}$ (`nan`) ; $\mathbf{Q}\sqrt{\boldsymbol{\Lambda}}$ sans $\mathbf{Q}^\top$ ; $\mathbf{L}^{-\top}$ au lieu de $\mathbf{L}^{-1}$.

### Ex M12c.30 — `np.linalg.eigh`, `det`, `cholesky` et `scipy.linalg.sqrtm` contre tes fonctions

**Réponses** : a) `[1.3289, 2.705, 5.0608, 8.9054]` · b) `True` · c) `True` · d) `True` · e) `True` · f) `True` · g) `"complex128"`.

**Démarche.** `values, vectors = np.linalg.eigh(S_30)` (ordre croissant) ; `vectors.T @ vectors` contre `np.eye(4)` ; puis tes fonctions contre celles de NumPy et SciPy. Pour la copie : `eigh` exploite la symétrie (plus rapide, valeurs réelles rangées, vecteurs orthonormés même pour une valeur multiple), `eig` peut rendre des complexes à la partie imaginaire minuscule ; `np.linalg.cholesky([[4, 7], [-3, 5]])` rend sans erreur le facteur de la matrice symétrique $\begin{pmatrix} 4 & -3 \\ -3 & 5 \end{pmatrix}$ (elle ne lit que le triangle inférieur) : un résultat faux et silencieux ; g) la rotation a pour valeurs propres $\pm i$.

**Erreurs fréquentes.** Lire la valeur propre de `eigh` en premier comme la plus grande ; comparer des vecteurs propres sans tenir compte du signe.

### Ex M12c.31 — Prédire : la méthode de la puissance quand les deux plus grandes valeurs propres sont proches

**Réponses** : a) `1` · b) `3` · c) `1` · d) `2`.

a) 40 itérations : l'écart est divisé par 2 à chaque pas. b) Il faudrait environ 2 750 pas ($0{,}99^k = 10^{-12}$) : la méthode s'arrête à 1 000. d) Après 1 000 pas, la composante sur $\mathbf{e}_2$ vaut environ $0{,}99^{1000} \approx 4{,}3 \times 10^{-5}$. c) Le quotient de Rayleigh $\frac{10x_1^2 + 9{,}9x_2^2 + x_3^2}{x_1^2 + x_2^2 + x_3^2}$ s'écarte de 10 d'environ $0{,}1 \times (4{,}3 \times 10^{-5})^2 \approx 2 \times 10^{-10}$ : l'erreur sur la valeur propre est le **carré** de celle du vecteur. Un critère d'arrêt sur la seule valeur propre s'arrêterait donc trop tôt pour le vecteur.

### Ex M12c.32 — La vitesse de la méthode de la puissance et le rapport |λ₂ / λ₁|

**Réponses** : a) `40` · b) `0.99` · c) `True` · d) `True`.

Le tableau : 13, 24, 40, 76, 242, 482 et 2 293 itérations pour $r = 0{,}1$ à $0{,}99$ ; le produit $k \times (-\log_{10} r)$ va de 13 à 10. En théorie, $r^k = 10^{-12}$ donne $k \times (-\log_{10} r) = 12$ ; les écarts viennent du point de départ, de la troisième valeur propre et du critère d'arrêt (qui compare deux itérés successifs, distants d'environ $(1 - r)$ fois l'écart). $r = 0{,}1$ demande 13 pas plutôt que 12 : l'écart de départ n'est pas exactement 1, et le critère compare deux itérés, ce qui coûte un pas de plus pour constater l'arrêt. Avec $r = 0{,}999$, $12/0{,}000\,43 \approx 28\,000$ produits d'une matrice $10^6 \times 10^6$ : on passe aux méthodes de Krylov (Lanczos, `scipy.sparse.linalg.eigsh`), qui exploitent tous les itérés à la fois.

### Ex M12c.33 — Les lignes de niveau de xᵀAx : définie positive, semi-définie positive, indéfinie

Vérification manuelle (la figure) et automatique (`classify`). L'ellipse de $\begin{pmatrix} 3 & -1 \\ -1 & 4 \end{pmatrix}$ (valeurs propres $\frac{7 \pm \sqrt{5}}{2} \approx 2{,}38$ et $4{,}62$) est la plus allongée le long du vecteur propre de la plus petite valeur propre. $\begin{pmatrix} 1 & 3 \\ 3 & 9 \end{pmatrix}$ donne $q = (x + 3y)^2$, nulle sur la droite $x + 3y = 0$, son noyau : des paires de droites parallèles. $x^2 + 4xy - 2y^2 = 0$ donne deux droites, $x = (-2 \pm \sqrt{6})\,y$, les asymptotes des hyperboles. $\operatorname{diag}(1 ;\ 10^{-9})$ a deux valeurs propres positives : définie positive pour `classify`, mais ses ellipses sont si allongées qu'à l'écran on croit voir des droites.

### Ex M12c.34 — Chasse à l'erreur : det(A + B) = det A + det B, un vecteur propre nul, Cholesky d'une matrice non symétrique

**Réponses** : a) `"ACE"` · b) `[-8.0, 3.0, 1.2247, -5.0, 3.5]` · c) `False`.

(A) Le déterminant n'est pas additif : $\det(\mathbf{A} + \mathbf{B}) = \det\begin{pmatrix} 3 & 2 \\ 4 & 0 \end{pmatrix} = -8$, et non $-5 + (-2) = -7$. (C) $\mathbf{A} - \lambda\mathbf{I}$ est singulière en théorie, mais l'arrondi de $\lambda$ la rend inversible pour la machine : `solve` rend la seule solution de $\mathbf{M}\mathbf{v} = \mathbf{0}$, le vecteur nul. Un vecteur propre nul doit toujours alerter : on prend un vecteur du noyau (`np.linalg.eig`, ou à la main $-\sqrt{6}\,v_0 + 2v_1 = 0$, $v_1/v_0 = \sqrt{6}/2 \approx 1{,}2247$). (E) `np.linalg.cholesky` ne lit que le triangle inférieur : elle factorise sans rien dire $\begin{pmatrix} 4 & -2 \\ -2 & 5 \end{pmatrix}$, alors que $\mathbf{C}$, non symétrique, n'a pas de décomposition de Cholesky ; c'est la plus dangereuse : ni erreur, ni résultat absurde. (B) est juste (la trace est linéaire, 3), (D) aussi ($(1 + \sqrt{6})(1 - \sqrt{6}) = -5$), (F) aussi ($\frac{7}{2}$).

### Ex M12c.35 — Vérifier avec SymPy : polynôme caractéristique, valeurs propres exactes, diagonalisation

Vérification par la cellule ✅/❌. $\det(\mathbf{M} - \lambda\mathbf{I}) = (2 - \lambda)\big((2 - \lambda)^2 - 2\big)$ : valeurs propres $2$ et $2 \pm \sqrt{2}$, de somme 6 (la trace) et de produit $2 \times 2 = 4$ (le déterminant). `M35_DEFECTIVE.eigenvects()` rend la valeur propre 1 (simple) et la valeur propre 3 (double) avec **un seul** vecteur propre, $(0, 1, 0)$ : $\mathbf{M} - 3\mathbf{I}$ est de rang 2, la matrice est défective. SymPy calcule en exact : pour une matrice $100 \times 100$, les expressions des racines explosent (et un polynôme de degré 100 n'a pas de formule) ; on prend NumPy.

### Ex M12c.36 — Défi : les trois plus grandes valeurs propres d'une matrice symétrique semi-définie positive 300 × 300, par la puissance avec déflation, à 1e−6 près

**Réponse** : `True` (objectif atteint).

Une solution : partir d'un vecteur tiré au hasard, appeler `power_iteration` (ou sa propre boucle) avec assez d'itérations, puis déflater, `A = A - value * np.outer(vector, vector)`, trois fois. Les rapports successifs sont $0{,}8$, $\approx 0{,}81$ et $\approx 0{,}77$ : quelques dizaines à une centaine d'itérations par étape pour le vecteur, et la valeur propre converge deux fois plus vite. La deuxième étape est la plus lente (rapport le plus proche de 1). Pour une matrice non symétrique, les autres vecteurs propres ne sont pas orthogonaux à $\mathbf{v}_1$, et $\mathbf{A} - \lambda_1\mathbf{v}_1\mathbf{v}_1^\top$ ne les garde pas. La plus petite valeur propre : la plus grande de $c\mathbf{I} - \mathbf{A}$ avec $c \ge \lambda_{\max}$ (elle vaut $c - \lambda_{\min}$), ou la méthode appliquée à $\mathbf{A}^{-1}$ (itération inverse).
