# M12c · Valeurs propres et matrices symétriques — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m12c_valeurs_propres/06_mes_reponses.md` (créée par `python tools/start_chapter.py M12c`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🧮, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, les valeurs propres réelles se donnent **par ordre décroissant**, comptées avec leur multiplicité ; un vecteur propre demandé « avec telle coordonnée » est le multiple qui a cette coordonnée ; un vecteur propre **unitaire** se donne avec la convention de l'énoncé (en général : sa première coordonnée non nulle positive). Une covariance sans autre précision est une matrice donnée, sans convention $1/n$ ou $1/(n-1)$ à choisir.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M12c.Q1 — Ce que mesure un déterminant 🧠 ★ ⏱️ 4 min
*Fiche §1 · parcours C, E*

1. $\mathbf{A} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ : en quoi le carré unité est-il envoyé, et quelle est son aire ?
2. Que dit un déterminant **négatif** de l'application ?
3. Une matrice $2 \times 2$ de déterminant nul envoie le plan sur quoi ?
4. $\det\mathbf{A} = 5$ : que devient l'aire d'un triangle d'aire 2 ?
5. Que vaut le déterminant d'une rotation du plan ? d'une symétrie par rapport à une droite ?
6. Vrai ou faux : un déterminant de $10^{-9}$ prouve que la matrice est presque non inversible.

### M12c.Q2 — Les propriétés du déterminant et de la trace : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §1 et §2 · parcours C, E*

Pour des matrices carrées $\mathbf{A}$, $\mathbf{B}$ de taille $n$ et $\mathbf{S}$ inversible :
1. $\det(\mathbf{A} + \mathbf{B}) = \det\mathbf{A} + \det\mathbf{B}$.
2. Pour $n = 2$, $\det(3\mathbf{A}) = 3\det\mathbf{A}$.
3. $\det(\mathbf{A}\mathbf{B}) = \det(\mathbf{B}\mathbf{A})$.
4. $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}\mathbf{A}\,\operatorname{tr}\mathbf{B}$.
5. $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}(\mathbf{B}\mathbf{A})$.
6. $\det\mathbf{A}^\top = \det\mathbf{A}$.
7. $\operatorname{tr}(\mathbf{S}^{-1}\mathbf{A}\mathbf{S}) = \operatorname{tr}\mathbf{A}$ et $\det(\mathbf{S}^{-1}\mathbf{A}\mathbf{S}) = \det\mathbf{A}$.

### M12c.Q3 — Reconnaître un vecteur propre 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

$\mathbf{M} = \begin{pmatrix} 6 & -2 \\ 6 & -1 \end{pmatrix}$. Pour chaque vecteur, dis s'il est vecteur propre de $\mathbf{M}$ et, si oui, de quelle valeur propre : $(2, 3)$, $(1, 2)$, $(1, 1)$, $(0, 0)$, $(-4, -6)$, $(1, 0)$. Puis : que valent la trace et le déterminant de $\mathbf{M}$, et sont-ils cohérents avec tes valeurs propres ?

### M12c.Q4 — Diagonalisable ou pas ? 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

Diagonalisable avec des nombres réels, ou pas ? Justifie en une ligne.
1. $\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$.
2. $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.
3. $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$.
4. $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
5. $\begin{pmatrix} 1 & 4 \\ 4 & 2 \end{pmatrix}$.
6. Une matrice $3 \times 3$ de valeurs propres $1$, $-2$ et $5$.

### M12c.Q5 — Ce que garantit le théorème spectral 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

Vrai ou faux ?
1. Toute matrice symétrique réelle a des valeurs propres réelles.
2. Toute matrice dont les valeurs propres sont réelles est symétrique.
3. Deux vecteurs propres d'une matrice symétrique, de valeurs propres différentes, sont orthogonaux.
4. Une matrice symétrique avec une valeur propre double n'est pas diagonalisable.
5. Si $\mathbf{A} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$ avec $\mathbf{Q}$ orthogonale et $\boldsymbol{\Lambda}$ diagonale, alors $\mathbf{A}$ est symétrique.
6. Pour une matrice symétrique, $\mathbf{A} = \sum_i \lambda_i\mathbf{q}_i\mathbf{q}_i^\top$, et chaque $\mathbf{q}_i\mathbf{q}_i^\top$ est une matrice de projection.

### M12c.Q6 — Définie positive, semi-définie positive ou indéfinie ? 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

Classe chaque matrice : définie positive, semi-définie positive (sans être définie), définie négative, ou indéfinie.
1. $\begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix}$.
2. $\begin{pmatrix} 4 & 6 \\ 6 & 9 \end{pmatrix}$.
3. $\begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix}$.
4. $\begin{pmatrix} -1 & 0 \\ 0 & -4 \end{pmatrix}$.
5. $\begin{pmatrix} 5 & 6 \\ 6 & 7 \end{pmatrix}$.
6. $\operatorname{diag}(3, 0, 1)$.

### M12c.Q7 — Cholesky, racine carrée, blanchiment : qui est quoi ? 🧠 ★ ⏱️ 4 min
*Fiche §7 et §8 · parcours C*

$\boldsymbol{\Sigma}$ est symétrique définie positive, $\boldsymbol{\Sigma} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$ et $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^\top$ (Cholesky). Associe chaque matrice à **toutes** les descriptions qui lui conviennent : (A) $\mathbf{L}$ ; (B) $\boldsymbol{\Sigma}^{1/2} = \mathbf{Q}\boldsymbol{\Lambda}^{1/2}\mathbf{Q}^\top$ ; (C) $\mathbf{L}^{-1}$ ; (D) $\boldsymbol{\Sigma}^{-1/2}$ ; (E) $\boldsymbol{\Lambda}^{-1/2}\mathbf{Q}^\top$.
1. Triangulaire inférieure.
2. Symétrique.
3. Son produit par sa transposée, dans un ordre ou l'autre, redonne $\boldsymbol{\Sigma}$.
4. C'est une matrice de blanchiment : $\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top = \mathbf{I}$.
5. On s'en sert pour fabriquer des données de covariance $\boldsymbol{\Sigma}$ à partir de tirages indépendants de variance 1.

### M12c.Q8 — Trace, déterminant et valeurs propres 🧠 ★ ⏱️ 4 min
*Fiche §2 et §3 · parcours C, E*

1. Une matrice $2 \times 2$ a pour trace 8 et pour déterminant 15. Ses valeurs propres ?
2. Une matrice $3 \times 3$ a pour valeurs propres 1, 2 et 3. Sa trace ? Son déterminant ? Est-elle inversible ?
3. Une matrice a la valeur propre 0. Qu'en conclus-tu ?
4. Une matrice $2 \times 2$ a pour trace 0 et pour déterminant 4. A-t-elle des valeurs propres réelles ?
5. Les valeurs propres de $\mathbf{A}$ sont 2 et $-3$. Celles de $\mathbf{A}^2$ ? de $\mathbf{A} + 5\mathbf{I}$ ? de $\mathbf{A}^{-1}$ ?

<a id="rappels"></a>

## 🔁 Rappels

### M12c.R1 — Le rang et le noyau (M12a) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

$\mathbf{B} = \begin{pmatrix} 2 & -1 & 3 \\ 4 & -2 & 6 \\ 1 & 0 & 1 \end{pmatrix}$.
1. Le rang de $\mathbf{B}$ ?
2. Une base de son noyau ?
3. $\mathbf{B}$ est-elle inversible ?
4. D'après la fiche §3, 0 est-il valeur propre de $\mathbf{B}$ ? Avec quel vecteur propre ?
5. Que vaut $\det\mathbf{B}$, sans calcul ?

### M12c.R2 — Bases orthonormées et matrices orthogonales (M12b) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C, E*

$\mathbf{U} = \frac{1}{17}\begin{pmatrix} 8 & -15 \\ 15 & 8 \end{pmatrix}$.
1. Vérifie que ses colonnes sont unitaires et orthogonales. Que vaut $\mathbf{U}^\top\mathbf{U}$ ?
2. $\mathbf{U}^{-1}$ ?
3. La norme de $\mathbf{U}\mathbf{x}$ pour $\mathbf{x} = (1, 4)$ ?
4. Les coordonnées de $\mathbf{x}$ dans la base des colonnes de $\mathbf{U}$ ?
5. $\det\mathbf{U}$ ? Rotation ou symétrie ?

### M12c.R3 — La matrice de covariance empirique (M02c) 🔁 ★ ⏱️ 5 min
*Fiche §8 · parcours C, E*

Quatre exemples à deux features : $(1, 2)$, $(4, 1)$, $(5, 6)$, $(2, 3)$.
1. Le point moyen ?
2. Les données centrées ?
3. La matrice de covariance avec $1/n$ (ddof = 0), puis avec $1/(n - 1)$ (ddof = 1). Par quel facteur passe-t-on de la première à la seconde ?
4. La corrélation des deux features (4 décimales) ? Dépend-elle de la convention ?
5. Vérifie que la matrice est symétrique et que sa diagonale est positive. Est-ce suffisant pour être une matrice de covariance ?

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M12c.1 — Déterminants 2 × 2 et 3 × 3 : aire, volume et signe ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des déterminants de petite taille et les lire comme des aires et des volumes orientés.
**Prérequis :** fiche §1 ; M09a · **Parcours :** C, E

$\mathbf{M} = \begin{pmatrix} 3 & -1 \\ 2 & 4 \end{pmatrix}$ et $\mathbf{N} = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 3 & 2 \\ 2 & 1 & 1 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\det\mathbf{M}$ | un nombre |
| b | l'aire du triangle de sommets $(0, 0)$, $(3, 2)$ et $(-1, 4)$ | un nombre |
| c | l'aire de l'image par $\mathbf{M}$ d'un disque de rayon 2 | un nombre (2 décimales) |
| d | $\det\mathbf{N}$ | un nombre |
| e | vrai ou faux : l'application de matrice $\mathbf{N}$ conserve l'orientation | `True` ou `False` |
| f | le déterminant de $\mathbf{N}$ après échange de ses lignes 1 et 3 | un nombre |
| g | $\det(2\mathbf{N})$ | un nombre |
| h | la valeur de $t$ pour laquelle $\begin{pmatrix} t & 2 & 1 \\ 1 & 1 & 0 \\ 3 & 0 & 1 \end{pmatrix}$ n'est pas inversible | un nombre |

Dans ta copie : calcule d) de deux façons, par cofacteurs sur une ligne et par élimination. Pourquoi l'aire de c) ne dépend-elle que de $|\det\mathbf{M}|$, et pas de la position du disque ? Que vaut le volume du parallélépipède construit sur les colonnes de $\mathbf{N}$ ?

### Ex M12c.2 — Le déterminant d'une matrice 4 × 4 par élimination ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer un déterminant $4 \times 4$ par élimination, en suivant le signe des échanges, et utiliser les propriétés du déterminant.
**Prérequis :** fiche §1 ; M09a §5 · **Parcours :** C

$\mathbf{F} = \begin{pmatrix} 0 & 2 & 1 & 3 \\ 1 & 1 & 0 & 2 \\ 2 & 4 & 3 & 1 \\ -1 & 0 & 2 & 2 \end{pmatrix}$. On échange d'abord les lignes 1 et 2, puis on élimine sous chaque pivot sans autre échange.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice obtenue après l'échange, puis l'élimination sous le premier pivot | une matrice |
| b | les quatre éléments diagonaux de la forme triangulaire obtenue | une liste de 4 nombres (1 décimale) |
| c | $\det\mathbf{F}$ | un nombre |
| d | $\det(\mathbf{F}^{-1})$ | un nombre (4 décimales) |
| e | $\det(\mathbf{F}^\top\mathbf{F})$ | un nombre |
| f | le déterminant de la matrice obtenue en ajoutant à la colonne 4 de $\mathbf{F}$ trois fois sa colonne 1 | un nombre |
| g | vrai ou faux : les colonnes de $\mathbf{F}$ forment une base de $\mathbb{R}^4$ | `True` ou `False` |

Dans ta copie : pourquoi faut-il un échange au départ ? Vérifie c) en développant selon la première colonne, après l'élimination de la question a). Combien de produits aurait demandé un développement complet par cofacteurs ?

### Ex M12c.3 — Les valeurs et vecteurs propres d'une matrice 2 × 2 ✏️ ★ ⏱️ 15 min
**Objectif :** calculer les valeurs et vecteurs propres d'une matrice $2 \times 2$ par le polynôme caractéristique, et en déduire ceux de matrices voisines.
**Prérequis :** fiche §3 ; M12a §6 · **Parcours :** C, E

$\mathbf{M} = \begin{pmatrix} 5 & 6 \\ 3 & -2 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\operatorname{tr}\mathbf{M}$ | un nombre |
| b | $\det\mathbf{M}$ | un nombre |
| c | les valeurs propres de $\mathbf{M}$ | une liste de 2 nombres |
| d | un vecteur propre de la plus grande valeur propre, de première coordonnée 3 | une liste de 2 nombres |
| e | un vecteur propre de la plus petite valeur propre, de première coordonnée 2 | une liste de 2 nombres |
| f | les valeurs propres de $\mathbf{M} + 2\mathbf{I}$ | une liste de 2 nombres |
| g | les valeurs propres de $\mathbf{M}^2$ | une liste de 2 nombres |
| h | vrai ou faux : les deux vecteurs propres de d) et e) sont orthogonaux | `True` ou `False` |

Dans ta copie : écris le polynôme caractéristique et factorise-le. Vérifie d) et e) par un produit. Pourquoi g) se fait-il sans calculer $\mathbf{M}^2$ ? Est-ce que h) contredit le théorème spectral ?

### Ex M12c.4 — Une matrice 3 × 3 triangulaire, puis une avec une valeur propre double ✏️ ★★ ⏱️ 20 min
**Objectif :** lire les valeurs propres d'une matrice triangulaire, calculer des espaces propres en dimension 3, et décider si une matrice à valeur propre double est diagonalisable.
**Prérequis :** fiche §3 et §4 ; M12a §6 · **Parcours :** C, E

$\mathbf{T} = \begin{pmatrix} 2 & 1 & -1 \\ 0 & -1 & 3 \\ 0 & 0 & 4 \end{pmatrix}$ et $\mathbf{K} = \begin{pmatrix} 6 & -3 & 3 \\ 1 & 2 & 1 \\ 0 & 0 & 3 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs propres de $\mathbf{T}$ | une liste de 3 nombres |
| b | un vecteur propre de $\mathbf{T}$ pour la valeur propre $-1$, de première coordonnée 1 | une liste de 3 nombres |
| c | un vecteur propre de $\mathbf{T}$ pour la valeur propre 4, de troisième coordonnée 5 | une liste de 3 nombres |
| d | $\det\mathbf{T}$ | un nombre |
| e | les valeurs propres de $\mathbf{K}$, comptées avec leur multiplicité | une liste de 3 nombres |
| f | la dimension de l'espace propre de $\mathbf{K}$ pour la valeur propre 3 | un entier |
| g | un vecteur propre de $\mathbf{K}$ pour la valeur propre 5, de deuxième coordonnée 1 | une liste de 3 nombres |
| h | vrai ou faux : $\mathbf{K}$ est diagonalisable | `True` ou `False` |

Dans ta copie : pourquoi les valeurs propres de $\mathbf{T}$ se lisent-elles sur la diagonale, et pas celles de $\mathbf{K}$ ? Donne une base de l'espace propre de f). Écris une matrice $\mathbf{P}$ et une matrice diagonale $\mathbf{D}$ telles que $\mathbf{K} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$. Que faudrait-il changer dans $\mathbf{K}$ pour qu'elle ne soit plus diagonalisable ?

### Ex M12c.5 — Diagonaliser, puis calculer une puissance dixième ✏️ ★★ ⏱️ 20 min
**Objectif :** diagonaliser une matrice $2 \times 2$, et s'en servir pour calculer une puissance, un déterminant et un inverse.
**Prérequis :** fiche §4 · **Parcours :** C, E

$\mathbf{A} = \begin{pmatrix} 5 & -12 \\ 1 & -2 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs propres de $\mathbf{A}$ | une liste de 2 nombres |
| b | un vecteur propre de la plus grande valeur propre, de deuxième coordonnée 1 | une liste de 2 nombres |
| c | un vecteur propre de l'autre, de deuxième coordonnée 1 | une liste de 2 nombres |
| d | $\mathbf{P}^{-1}$, où les colonnes de $\mathbf{P}$ sont les vecteurs de b) puis de c) | une matrice |
| e | $\mathbf{A}^{10}$ | une matrice |
| f | $\det(\mathbf{A}^{10})$ | un nombre |
| g | $\operatorname{tr}(\mathbf{A}^{10})$ | un nombre |
| h | les valeurs propres de $\mathbf{A}^{-1}$ | une liste de 2 nombres (1 décimale) |

Dans ta copie : vérifie $\mathbf{A}\mathbf{P} = \mathbf{P}\mathbf{D}$. Vérifie f) et g) sans utiliser e). Que devient $\mathbf{A}^k$ quand $k$ est grand, et sur quelle droite sont alors ses colonnes ?

### Ex M12c.6 — Une matrice non diagonalisable, et une rotation sans valeur propre réelle ✏️ ★★ ⏱️ 15 min
**Objectif :** reconnaître une matrice défective par la dimension de son espace propre, et voir pourquoi une rotation n'a pas de valeur propre réelle.
**Prérequis :** fiche §3 et §4 · **Parcours :** C

$\mathbf{N} = \begin{pmatrix} 5 & -9 \\ 1 & -1 \end{pmatrix}$ et $\mathbf{R}$ la rotation d'angle $60°$, $\mathbf{R} = \begin{pmatrix} \cos 60° & -\sin 60° \\ \sin 60° & \cos 60° \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs propres de $\mathbf{N}$, comptées avec leur multiplicité | une liste de 2 nombres |
| b | la dimension de l'espace propre correspondant | un entier |
| c | un vecteur propre de $\mathbf{N}$, de deuxième coordonnée 1 | une liste de 2 nombres |
| d | vrai ou faux : $\mathbf{N}$ est diagonalisable | `True` ou `False` |
| e | le discriminant $b^2 - 4ac$ du polynôme caractéristique de $\mathbf{R}$ | un nombre |
| f | le nombre de valeurs propres réelles de $\mathbf{R}$ | un entier |
| g | $\det\mathbf{R}$ | un nombre |
| h | vrai ou faux : $\mathbf{R}^6 = \mathbf{I}$ | `True` ou `False` |

Dans ta copie : pourquoi $\mathbf{N}$ n'a-t-elle pas assez de vecteurs propres, alors que sa valeur propre est double ? Que fait $\mathbf{R}$ à toute direction du plan ? Donne les deux valeurs propres complexes de $\mathbf{R}$ et vérifie que leur produit est $\det\mathbf{R}$.

### Ex M12c.7 — Le théorème spectral sur une matrice symétrique 2 × 2 : Q, Λ et QΛQᵀ ✏️ ★ ⏱️ 15 min
**Objectif :** diagonaliser une matrice symétrique dans une base orthonormée, et écrire sa décomposition spectrale.
**Prérequis :** fiche §6 ; M12b §2 · **Parcours :** C, E

$\mathbf{S} = \begin{pmatrix} 5 & 10 \\ 10 & 26 \end{pmatrix}$. Les vecteurs propres unitaires se donnent avec leur première coordonnée positive.

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs propres de $\mathbf{S}$ | une liste de 2 nombres |
| b | le vecteur propre unitaire $\mathbf{q}_1$ de la plus grande | une liste de 2 nombres (4 décimales) |
| c | le vecteur propre unitaire $\mathbf{q}_2$ de la plus petite | une liste de 2 nombres (4 décimales) |
| d | $\mathbf{q}_1 \cdot \mathbf{q}_2$ | un nombre |
| e | la matrice $\lambda_1\mathbf{q}_1\mathbf{q}_1^\top$ | une matrice (4 décimales) |
| f | $\det\mathbf{S}$ | un nombre |
| g | les valeurs propres de $\mathbf{S}^{-1}$ | une liste de 2 nombres (4 décimales) |
| h | vrai ou faux : $\mathbf{S}$ est définie positive | `True` ou `False` |

Dans ta copie : écris $\mathbf{Q}$ et $\boldsymbol{\Lambda}$, et vérifie $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}$ puis $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top = \mathbf{S}$ (les racines carrées disparaissent). Vérifie que e) plus $\lambda_2\mathbf{q}_2\mathbf{q}_2^\top$ redonne $\mathbf{S}$. Quels sont les vecteurs propres de $\mathbf{S}^{-1}$ ?

### Ex M12c.8 — Le quotient de Rayleigh : le maximum et le minimum de xᵀAx sur le cercle unité ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des quotients de Rayleigh, et trouver le maximum et le minimum d'une forme quadratique sur les vecteurs unitaires grâce aux valeurs propres.
**Prérequis :** fiche §6 · **Parcours :** C, E

$\mathbf{S} = \begin{pmatrix} 17 & 4 \\ 4 & 2 \end{pmatrix}$ et $R(\mathbf{x}) = \dfrac{\mathbf{x}^\top\mathbf{S}\mathbf{x}}{\mathbf{x}^\top\mathbf{x}}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $R(1, 0)$ | un nombre |
| b | $R(0, 1)$ | un nombre |
| c | $R(1, 1)$ | un nombre (1 décimale) |
| d | les valeurs propres de $\mathbf{S}$ | une liste de 2 nombres |
| e | le maximum de $\mathbf{x}^\top\mathbf{S}\mathbf{x}$ sur les vecteurs unitaires | un nombre |
| f | un vecteur unitaire qui l'atteint, de première coordonnée positive | une liste de 2 nombres (4 décimales) |
| g | le minimum de $\mathbf{x}^\top\mathbf{S}\mathbf{x}$ sur les vecteurs unitaires | un nombre |
| h | $\mathbf{x}^\top\mathbf{S}\mathbf{x}$ pour le vecteur unitaire $\mathbf{x} = \frac{1}{17}(8, 15)$ | un nombre (4 décimales) |

Dans ta copie : écris $\mathbf{x}$ dans la base orthonormée des vecteurs propres, $\mathbf{x} = y_1\mathbf{q}_1 + y_2\mathbf{q}_2$, et explique pourquoi $R(\mathbf{x})$ est une moyenne pondérée des valeurs propres. Déduis-en les poids pour le vecteur de h), et retrouve h). Pourquoi a) n'est-il pas le maximum, bien que 17 soit le plus grand élément de $\mathbf{S}$ ?

### Ex M12c.9 — Trois itérations de la méthode de la puissance à la main ✏️ ★ ⏱️ 15 min
**Objectif :** dérouler la méthode de la puissance, avec sa normalisation et sa convention de signe, et relier sa vitesse au rapport des valeurs propres.
**Prérequis :** fiche §5 · **Parcours :** C

$\mathbf{A} = \begin{pmatrix} 2 & 3 \\ 3 & -6 \end{pmatrix}$ et $\mathbf{x}_0 = (1, 0)$. À chaque pas, $\mathbf{x}_{k+1} = \mathbf{A}\mathbf{x}_k/\lVert \mathbf{A}\mathbf{x}_k \rVert$, puis on change le signe de $\mathbf{x}_{k+1}$ si sa coordonnée de plus grande valeur absolue est négative. (Pour aller vite, calcule les produits sur les vecteurs non normalisés : seule la direction compte.)

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{A}\mathbf{x}_0$ | une liste de 2 nombres |
| b | $\mathbf{x}_1$ | une liste de 2 nombres (4 décimales) |
| c | $\mathbf{x}_2$ | une liste de 2 nombres (4 décimales) |
| d | $\mathbf{x}_3$ | une liste de 2 nombres (4 décimales) |
| e | le quotient de Rayleigh $\mathbf{x}_3^\top\mathbf{A}\mathbf{x}_3$ | un nombre (4 décimales) |
| f | les valeurs propres de $\mathbf{A}$ | une liste de 2 nombres |
| g | la limite des $\mathbf{x}_k$ : le vecteur propre unitaire de la valeur propre de plus grand module, avec la même convention de signe | une liste de 2 nombres (4 décimales) |
| h | le rapport $\lvert\lambda_2/\lambda_1\rvert$ qui règle la vitesse, $\lambda_1$ étant la valeur propre de plus grand module | un nombre (4 décimales) |

Dans ta copie : sans la convention de signe, que ferait $\mathbf{x}_k$ d'un pas à l'autre, et pourquoi ? Combien de pas faut-il, environ, pour gagner trois chiffres décimaux sur la direction ? Qu'aurait donné $\mathbf{x}_0 = (3, 1)$ ?

### Ex M12c.10 — Définie positive ? Par les valeurs propres, les mineurs et la forme quadratique ; une hessienne qui prouve la convexité ✏️ ★★ ⏱️ 20 min
**Objectif :** tester qu'une matrice est définie positive par plusieurs critères, et s'en servir pour prouver qu'une fonction est convexe.
**Prérequis :** fiche §7 ; M05b §5 ; M10 · **Parcours :** C, E

$\mathbf{H}_1 = \begin{pmatrix} 4 & -2 & 0 \\ -2 & 3 & 1 \\ 0 & 1 & 2 \end{pmatrix}$, $\mathbf{H}_2 = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 3 & 1 \\ 0 & 1 & 4 \end{pmatrix}$ et $f(x, y) = x^2 + 2xy + 3y^2 + e^x$.

| | Question | Réponse attendue |
|---|---|---|
| a | les trois mineurs principaux en haut à gauche de $\mathbf{H}_1$ ($1 \times 1$, $2 \times 2$, $3 \times 3$) | une liste de 3 nombres |
| b | vrai ou faux : $\mathbf{H}_1$ est définie positive | `True` ou `False` |
| c | les trois mineurs principaux en haut à gauche de $\mathbf{H}_2$ | une liste de 3 nombres |
| d | $\mathbf{x}^\top\mathbf{H}_2\mathbf{x}$ pour $\mathbf{x} = (2, -1, 0)$ | un nombre |
| e | la hessienne de $f$ en $(0, 0)$ | une matrice |
| f | le déterminant de la hessienne de $f$ en $(1, 0)$ | un nombre (4 décimales) |
| g | vrai ou faux : $f$ est convexe sur $\mathbb{R}^2$ | `True` ou `False` |
| h | les valeurs propres de la hessienne de e) | une liste de 2 nombres |

Dans ta copie : que dit d) sur $\mathbf{H}_2$, et est-ce cohérent avec c) ? Écris la hessienne de $f$ en un point $(x, y)$ quelconque, et prouve g) avec le critère des mineurs. $f$ a-t-elle un minimum global, et combien ?

### Ex M12c.11 — La décomposition de Cholesky d'une matrice 3 × 3 ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une décomposition de Cholesky colonne par colonne, et s'en servir pour un déterminant et un système.
**Prérequis :** fiche §7 · **Parcours :** C, E

$\mathbf{A} = \begin{pmatrix} 4 & -6 & 2 \\ -6 & 10 & 1 \\ 2 & 1 & 21 \end{pmatrix}$ et $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$, $\mathbf{L}$ triangulaire inférieure à diagonale positive.

| | Question | Réponse attendue |
|---|---|---|
| a | $l_{11}$ | un nombre |
| b | $(l_{21}, l_{31})$ | une liste de 2 nombres |
| c | $l_{22}$ | un nombre |
| d | $l_{32}$ | un nombre |
| e | $l_{33}$ | un nombre |
| f | $\mathbf{L}$ | une matrice |
| g | $\det\mathbf{A}$ | un nombre |
| h | la solution de $\mathbf{A}\mathbf{x} = (2, -7, -19)$, par deux systèmes triangulaires | une liste de 3 nombres |

Dans ta copie : vérifie $\mathbf{L}\mathbf{L}^\top = \mathbf{A}$. Écris les deux systèmes de h) et résous-les. Si l'élément $21$ de $\mathbf{A}$ était remplacé par $17$, que se passerait-il à la dernière étape, et que faudrait-il en conclure ?

### Ex M12c.12 — Une forme quadratique réduite à une somme de carrés, et ses lignes de niveau ✏️ ★★ ⏱️ 20 min
**Objectif :** écrire une forme quadratique avec sa matrice symétrique, la réduire à une somme de carrés dans la base des vecteurs propres, et en déduire ses lignes de niveau.
**Prérequis :** fiche §6 et §7 · **Parcours :** C

$q(x, y) = 2x^2 + 10xy + 26y^2$.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice symétrique $\mathbf{S}$ telle que $q(\mathbf{x}) = \mathbf{x}^\top\mathbf{S}\mathbf{x}$ | une matrice |
| b | les valeurs propres de $\mathbf{S}$ | une liste de 2 nombres |
| c | le vecteur propre unitaire de la plus grande, de coordonnées positives | une liste de 2 nombres (4 décimales) |
| d | $q(5, -1)$ | un nombre |
| e | les deux demi-axes de l'ellipse $q(\mathbf{x}) = 27$, du plus grand au plus petit | une liste de 2 nombres (4 décimales) |
| f | l'aire de la région $q(\mathbf{x}) \le 27$ | un nombre (2 décimales) |
| g | la plus petite valeur positive de $c$ pour laquelle $2x^2 + c\,xy + 26y^2$ n'est plus définie positive | un nombre (2 décimales) |
| h | vrai ou faux : la ligne de niveau $q(\mathbf{x}) = 0$ est réduite à l'origine | `True` ou `False` |

Dans ta copie : écris $q$ comme une somme de deux carrés dans la base des vecteurs propres. Le long de quelle direction la ligne de niveau est-elle la plus allongée, et pourquoi est-ce la direction de la **plus petite** valeur propre ? Dessine l'allure de $q = 27$. L'aire d'une ellipse de demi-axes $a$ et $b$ vaut $\pi ab$.

### Ex M12c.13 — La covariance d'un vecteur transformé, AΣAᵀ, et le blanchiment d'une covariance 2 × 2 ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer la covariance d'une transformation linéaire, puis trois matrices de blanchiment : par Cholesky, par la racine carrée (ZCA) et par l'ACP.
**Prérequis :** fiche §8 ; M02c · **Parcours :** C, E

Un vecteur aléatoire $\mathbf{x} = (x_1, x_2)$ a pour covariance $\boldsymbol{\Sigma} = \begin{pmatrix} 36 & -30 \\ -30 & 61 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbb{V}(x_1 + x_2)$ | un nombre |
| b | la matrice de covariance de $(x_1 + x_2,\ x_1 - 2x_2)$ | une matrice |
| c | le facteur de Cholesky $\mathbf{L}$ de $\boldsymbol{\Sigma}$ | une matrice |
| d | la matrice de blanchiment $\mathbf{W} = \mathbf{L}^{-1}$ | une matrice (4 décimales) |
| e | les valeurs propres de $\boldsymbol{\Sigma}$ | une liste de 2 nombres |
| f | $\boldsymbol{\Sigma}^{1/2}$ | une matrice (4 décimales) |
| g | la matrice de blanchiment ZCA, $\boldsymbol{\Sigma}^{-1/2}$ | une matrice (4 décimales) |
| h | l'écart $\mathbf{x} - \boldsymbol{\mu} = (12, 0)$, blanchi par $\mathbf{L}^{-1}$ | une liste de 2 nombres (4 décimales) |

Dans ta copie : écris la matrice $\mathbf{A}$ de b) et vérifie b) par $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^\top$. Vérifie que $\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top = \mathbf{I}$ pour d). Donne les vecteurs propres unitaires de $\boldsymbol{\Sigma}$, puis la matrice de blanchiment de l'ACP, $\boldsymbol{\Lambda}^{-1/2}\mathbf{Q}^\top$ : pourquoi diffère-t-elle de g), alors que toutes deux blanchissent ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration dans ta copie : hypothèses, étapes justifiées, conclusion (R4). La grille de relecture de `05_solutions.md` dit ce qu'une démonstration correcte doit contenir.

### Ex M12c.14 — det A ≠ 0 si et seulement si A est inversible (det AB = det A det B admis) ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer le lien entre déterminant et inversibilité, en n'admettant que la multiplicativité et l'effet des opérations sur les lignes.
**Prérequis :** fiche §1 ; M09a §5 et §6 · **Parcours :** C

On admet : $\det(\mathbf{A}\mathbf{B}) = \det\mathbf{A}\,\det\mathbf{B}$ ; $\det\mathbf{I} = 1$ ; les effets des trois opérations sur les lignes (fiche §1) ; le déterminant d'une matrice triangulaire est le produit de sa diagonale.
1. Si $\mathbf{A}$ est inversible, montre que $\det\mathbf{A}\,\det(\mathbf{A}^{-1}) = 1$. Déduis-en $\det\mathbf{A} \ne 0$, et la valeur de $\det(\mathbf{A}^{-1})$.
2. Réciproquement, suppose $\mathbf{A}$ non inversible. Par l'élimination de M09a, $\mathbf{A}$ se ramène à une forme échelonnée $\mathbf{E}$, dont le déterminant est $c\,\det\mathbf{A}$ avec $c \ne 0$ (pourquoi ?). Montre qu'une forme échelonnée carrée d'une matrice non inversible a une ligne nulle, ou un zéro sur sa diagonale. Conclus que $\det\mathbf{A} = 0$.
3. Déduis-en : si les colonnes de $\mathbf{A}$ sont liées, $\det\mathbf{A} = 0$. Montre-le aussi directement, avec la linéarité par rapport à une colonne et l'antisymétrie.
4. Déduis de 1. que $\det(\mathbf{S}^{-1}\mathbf{A}\mathbf{S}) = \det\mathbf{A}$ pour $\mathbf{S}$ inversible.

### Ex M12c.15 — Une matrice symétrique réelle : valeurs propres réelles, vecteurs propres de valeurs distinctes orthogonaux ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer les deux premiers points du théorème spectral, et en tirer le troisième quand les valeurs propres sont distinctes.
**Prérequis :** fiche §3 et §6 ; M12b §2 · **Parcours :** C, E

$\mathbf{A}$ est une matrice symétrique réelle $n \times n$.
1. Montre que $(\mathbf{A}\mathbf{u}) \cdot \mathbf{v} = \mathbf{u} \cdot (\mathbf{A}\mathbf{v})$ pour tous $\mathbf{u}, \mathbf{v}$ de $\mathbb{R}^n$.
2. Soient $\mathbf{A}\mathbf{u} = \lambda\mathbf{u}$ et $\mathbf{A}\mathbf{v} = \mu\mathbf{v}$ avec $\lambda \ne \mu$ (réels, vecteurs non nuls). Calcule $(\mathbf{A}\mathbf{u}) \cdot \mathbf{v}$ de deux façons et montre que $\mathbf{u} \perp \mathbf{v}$.
3. Valeurs propres réelles. Soit $\lambda$ une valeur propre, éventuellement complexe, et $\mathbf{z} \ne \mathbf{0}$ un vecteur de $\mathbb{C}^n$ avec $\mathbf{A}\mathbf{z} = \lambda\mathbf{z}$. On note $\bar{\mathbf{z}}$ le vecteur des conjugués. Montre que $\bar{\mathbf{z}}^\top\mathbf{A}\mathbf{z}$ est égal à son propre conjugué (utilise que $\mathbf{A}$ est réelle et symétrique), donc réel. Montre que $\bar{\mathbf{z}}^\top\mathbf{z} = \sum_i |z_i|^2 > 0$, et conclus que $\lambda = \frac{\bar{\mathbf{z}}^\top\mathbf{A}\mathbf{z}}{\bar{\mathbf{z}}^\top\mathbf{z}}$ est réel.
4. Si les $n$ valeurs propres de $\mathbf{A}$ sont distinctes, montre qu'il existe une base orthonormée de vecteurs propres, puis que $\mathbf{A} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$.
5. Vérifie 2. et 3. sur $\begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}$ (fiche §7), sans calculer de racine carrée.

### Ex M12c.16 — La somme des valeurs propres est la trace, leur produit le déterminant ∂ ★★ ⏱️ 20 min
**Objectif :** relier les valeurs propres à la trace et au déterminant, par le polynôme caractéristique puis par la diagonalisation.
**Prérequis :** fiche §2, §3 et §4 · **Parcours :** C

1. En dimension 2, développe $\det(\mathbf{A} - \lambda\mathbf{I})$ pour $\mathbf{A} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ et montre que $p_{\mathbf{A}}(\lambda) = \lambda^2 - (\operatorname{tr}\mathbf{A})\lambda + \det\mathbf{A}$. Avec les relations entre racines et coefficients (R3), conclus.
2. En dimension $n$, admettons que $p_{\mathbf{A}}(\lambda) = (\lambda_1 - \lambda)(\lambda_2 - \lambda)\cdots(\lambda_n - \lambda)$, où les $\lambda_i$, complexes éventuellement, sont les valeurs propres comptées avec leur multiplicité. Que vaut $p_{\mathbf{A}}(0)$ ? Déduis-en $\prod_i\lambda_i = \det\mathbf{A}$.
3. Si $\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ est diagonalisable, redémontre les deux formules avec $\operatorname{tr}(\mathbf{X}\mathbf{Y}) = \operatorname{tr}(\mathbf{Y}\mathbf{X})$ et $\det(\mathbf{X}\mathbf{Y}) = \det\mathbf{X}\,\det\mathbf{Y}$.
4. Application : une matrice $3 \times 3$ a pour trace 6, pour déterminant 6, et 1 est valeur propre. Trouve ses deux autres valeurs propres.
5. Pourquoi une matrice de trace nulle et de déterminant strictement positif, en dimension 2, n'a-t-elle aucune valeur propre réelle ?

### Ex M12c.17 — Une matrice de covariance, et toute matrice de Gram XᵀX, est symétrique semi-définie positive ∂ ★ ⏱️ 15 min
**Objectif :** démontrer qu'une matrice de Gram et une matrice de covariance sont symétriques semi-définies positives, et dire quand elles sont définies positives.
**Prérequis :** fiche §7 et §8 ; M02c ; M12a §6 · **Parcours :** C, E

1. Soit $\mathbf{X}$ de forme $(n, p)$. Montre que $\mathbf{G} = \mathbf{X}^\top\mathbf{X}$ est symétrique, puis que $\mathbf{w}^\top\mathbf{G}\mathbf{w} = \lVert \mathbf{X}\mathbf{w} \rVert^2 \ge 0$ pour tout $\mathbf{w}$.
2. Montre que $\mathbf{G}$ est définie positive si et seulement si les colonnes de $\mathbf{X}$ sont libres (M12a §6).
3. Déduis de 1. que la matrice de covariance empirique $\boldsymbol{\Sigma} = \frac{1}{n-1}\mathbf{X}_c^\top\mathbf{X}_c$ est symétrique semi-définie positive.
4. Pour un vecteur aléatoire $\mathbf{x}$ de moyenne $\boldsymbol{\mu}$ et de covariance $\boldsymbol{\Sigma} = \mathbb{E}[(\mathbf{x} - \boldsymbol{\mu})(\mathbf{x} - \boldsymbol{\mu})^\top]$, montre que $\mathbb{V}(\mathbf{a}^\top\mathbf{x}) = \mathbf{a}^\top\boldsymbol{\Sigma}\mathbf{a}$, et conclus.
5. Quand la matrice de covariance empirique n'est-elle **pas** définie positive ? Donne un exemple avec trois features dont l'une est la somme des deux autres, et un exemple avec plus de features que d'exemples.

### Ex M12c.18 — Le quotient de Rayleigh d'une matrice symétrique est entre λ_min et λ_max ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer l'encadrement du quotient de Rayleigh par la décomposition spectrale, et caractériser ses extrema.
**Prérequis :** fiche §6 ; M12b §2 · **Parcours :** C

$\mathbf{A}$ est symétrique, $\mathbf{A} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$, de valeurs propres $\lambda_1 \ge \cdots \ge \lambda_n$, et $\mathbf{x} \ne \mathbf{0}$.
1. On pose $\mathbf{y} = \mathbf{Q}^\top\mathbf{x}$. Montre que $\mathbf{y} \ne \mathbf{0}$, que $\mathbf{x}^\top\mathbf{x} = \mathbf{y}^\top\mathbf{y}$ et que $\mathbf{x}^\top\mathbf{A}\mathbf{x} = \sum_i \lambda_iy_i^2$.
2. Déduis-en $\lambda_n \le R(\mathbf{x}) \le \lambda_1$.
3. Montre que $R(\mathbf{x}) = \lambda_1$ si et seulement si $\mathbf{x}$ est un vecteur propre de $\lambda_1$.
4. Montre que, parmi les vecteurs orthogonaux à $\mathbf{q}_1$, le maximum de $R$ est $\lambda_2$.
5. Une matrice symétrique a toutes ses valeurs propres dans $[2 ; 7]$. Encadre $\mathbf{x}^\top\mathbf{A}\mathbf{x}$ pour $\lVert \mathbf{x} \rVert = 3$. Est-elle définie positive ?

### Ex M12c.19 — ½ xᵀAx − bᵀx, avec A définie positive, a un unique minimum, en A⁻¹b ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer, sans dériver, que la minimisation d'une quadratique strictement convexe revient à résoudre un système linéaire.
**Prérequis :** fiche §7 · **Parcours :** C, E

$\mathbf{A}$ est symétrique définie positive, $f(\mathbf{x}) = \frac{1}{2}\mathbf{x}^\top\mathbf{A}\mathbf{x} - \mathbf{b}^\top\mathbf{x}$, et $\mathbf{x}^* = \mathbf{A}^{-1}\mathbf{b}$ (pourquoi existe-t-il ?).
1. Pour tout $\mathbf{h}$, développe $f(\mathbf{x}^* + \mathbf{h})$ et montre que $f(\mathbf{x}^* + \mathbf{h}) = f(\mathbf{x}^*) + \frac{1}{2}\mathbf{h}^\top\mathbf{A}\mathbf{h}$. (Utilise la symétrie de $\mathbf{A}$ pour regrouper les termes croisés.)
2. Conclus que $\mathbf{x}^*$ est l'unique minimum de $f$, et que $f(\mathbf{x}^*) = -\frac{1}{2}\mathbf{b}^\top\mathbf{x}^*$.
3. Que devient le raisonnement si $\mathbf{A}$ est seulement semi-définie positive ? Distingue le cas où $\mathbf{b}$ est dans l'image de $\mathbf{A}$ et celui où il n'y est pas.
4. Les moindres carrés : montre que $\frac{1}{2}\lVert \mathbf{X}\mathbf{w} - \mathbf{y} \rVert^2$ s'écrit $\frac{1}{2}\mathbf{w}^\top\mathbf{A}\mathbf{w} - \mathbf{b}^\top\mathbf{w} + c$, avec $\mathbf{A}$, $\mathbf{b}$ et $c$ à préciser, et retrouve les équations normales de M09b.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12c.20 — Pont : la variance d'une somme pondérée de trois features, wᵀΣw, et pourquoi Σ doit être semi-définie positive 🔗 ★ ⏱️ 15 min
**Objectif :** calculer des variances et des covariances de combinaisons de features à partir de leur matrice de covariance, et reconnaître une matrice qui ne peut pas être une covariance.
**Prérequis :** fiche §7 et §8 · **Parcours :** C, E

Trois features ont pour matrice de covariance $\boldsymbol{\Sigma} = \begin{pmatrix} 4 & 2 & -1 \\ 2 & 9 & 3 \\ -1 & 3 & 16 \end{pmatrix}$. Un collègue propose aussi la matrice $\boldsymbol{\Phi} = \begin{pmatrix} 2 & 3 & 1 \\ 3 & 2 & 0 \\ 1 & 0 & 2 \end{pmatrix}$ comme matrice de covariance d'autres données.

| | Question | Réponse attendue |
|---|---|---|
| a | la variance totale | un nombre |
| b | $\mathbb{V}(x_1 + x_2 + x_3)$ | un nombre |
| c | $\mathbb{V}(2x_1 - x_2)$ | un nombre |
| d | $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w}$ pour $\mathbf{w} = (1, -1, 2)$ | un nombre |
| e | $\operatorname{Cov}(x_1 + x_2,\ x_3)$ | un nombre |
| f | la « variance » de $x_1 - x_2$ calculée avec $\boldsymbol{\Phi}$ | un nombre |
| g | vrai ou faux : $\boldsymbol{\Phi}$ peut être une matrice de covariance | `True` ou `False` |
| h | la corrélation de $x_1$ et $x_2$ (pour $\boldsymbol{\Sigma}$) | un nombre (4 décimales) |

Dans ta copie : écris b) comme la somme de **tous** les éléments de $\boldsymbol{\Sigma}$, et dis pourquoi. Vérifie que $\boldsymbol{\Sigma}$ est définie positive par les mineurs. Un modèle linéaire prédit $\hat{y} = \mathbf{w}^\top\mathbf{x}$ : que représente d) ?

### Ex M12c.21 — Pont : après un blanchiment, la covariance est l'identité 🔗 ★★ ⏱️ 15 min
**Objectif :** blanchir une covariance par Cholesky, vérifier que la covariance devient l'identité, et voir ce qui ne dépend pas du blanchiment choisi.
**Prérequis :** fiche §8 · **Parcours :** C

Deux features ont pour covariance $\boldsymbol{\Sigma} = \begin{pmatrix} 9 & 6 \\ 6 & 8 \end{pmatrix}$ et pour moyenne $\boldsymbol{\mu}$. On blanchit par $\mathbf{z} = \mathbf{W}(\mathbf{x} - \boldsymbol{\mu})$, avec $\mathbf{W} = \mathbf{L}^{-1}$.

| | Question | Réponse attendue |
|---|---|---|
| a | le facteur de Cholesky $\mathbf{L}$ de $\boldsymbol{\Sigma}$ | une matrice |
| b | $\mathbf{W} = \mathbf{L}^{-1}$ | une matrice (4 décimales) |
| c | $\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^\top$ | une matrice |
| d | $\mathbf{z}$ pour $\mathbf{x} - \boldsymbol{\mu} = (6, 1)$ | une liste de 2 nombres (1 décimale) |
| e | $\lVert \mathbf{z} \rVert$, la distance de Mahalanobis de $\mathbf{x}$ à $\boldsymbol{\mu}$ | un nombre (1 décimale) |
| f | la covariance de $\mathbf{R}\mathbf{z}$, où $\mathbf{R} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ | une matrice |
| g | vrai ou faux : $\mathbf{R}\mathbf{W}$ est aussi une matrice de blanchiment de $\boldsymbol{\Sigma}$ | `True` ou `False` |
| h | vrai ou faux : la distance de Mahalanobis $\lVert \mathbf{W}(\mathbf{x} - \boldsymbol{\mu}) \rVert$ change quand on remplace $\mathbf{W}$ par un autre blanchiment | `True` ou `False` |

Dans ta copie : vérifie e) par la formule $\sqrt{(\mathbf{x} - \boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})}$, après avoir calculé $\boldsymbol{\Sigma}^{-1}$. Pourquoi h) était-il prévisible (écris $\lVert \mathbf{W}\mathbf{d} \rVert^2$ avec $\mathbf{W}^\top\mathbf{W}$) ? Après un blanchiment, un modèle de distance (des k plus proches voisins) voit-il encore la corrélation des deux features ?

### Ex M12c.22 — MML §4.1 et §4.2 : déterminant, trace, valeurs propres, en anglais 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais les définitions et les propriétés du déterminant, de la trace et des valeurs propres, et les relier à la fiche.
**Prérequis :** fiche §1 à §4 · **Parcours :** C

Lis MML §4.1 et §4.2. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Au §4.1, comment le livre introduit-il le déterminant, et quel lien fait-il avec l'inversibilité ? Comment appelle-t-il le développement selon une ligne ou une colonne ?
2. Quelle interprétation géométrique le livre donne-t-il du déterminant en dimension 2 et 3, et que dit-il de son signe ?
3. Quelles propriétés de la trace énonce-t-il ? Laquelle permet de dire que la trace ne dépend pas de la base ?
4. Au §4.2, comment le livre définit-il valeur propre, vecteur propre et espace propre ? Relève les formulations équivalentes de « $\lambda$ est valeur propre » qu'il donne, et relie chacune à un énoncé de la fiche.
5. Qu'appelle-t-il multiplicités algébrique et géométrique, et matrice **défective** (*defective*) ? Refais un de ses exemples avec ta propre matrice $2 \times 2$.
6. Quel résultat sur $\mathbf{A}^\top\mathbf{A}$ le livre démontre-t-il, et quel est le lien avec M12c.17 ?
7. Note trois mots ou tournures en anglais de ces sections, avec leur traduction.

### Ex M12c.23 — MML §4.3 et §4.4 : Cholesky, diagonalisation et décomposition spectrale 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais la décomposition de Cholesky et la diagonalisation, et les relier à la fiche.
**Prérequis :** fiche §4, §6 et §7 · **Parcours :** C

Lis MML §4.3 et §4.4. Réponds dans ta copie, avec tes mots.
1. Au §4.3, comment le livre énonce-t-il la décomposition de Cholesky ? Comment appelle-t-il $\mathbf{L}$ ? Que dit-il de son unicité ?
2. Quels usages de Cholesky en machine learning cite-t-il ? Relie chacun à un passage de la fiche.
3. Comment le livre calcule-t-il un déterminant avec le facteur de Cholesky ? Vérifie-le sur M12c.11.
4. Au §4.4, comment définit-il une matrice diagonalisable, et des matrices semblables ? Quelle condition donne-t-il pour qu'une matrice soit diagonalisable ?
5. Comment énonce-t-il la décomposition d'une matrice symétrique (*eigendecomposition*), et quelle interprétation géométrique donne-t-il de $\mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ (changement de base, étirement, retour) ?
6. Quels calculs la diagonalisation rend-elle faciles, d'après le livre ? Refais-en un avec la matrice de M12c.5.
7. Note trois mots ou tournures en anglais de ces sections, avec leur traduction.

### Ex M12c.24 — Fermi : un déterminant 20 × 20 par cofacteurs ou par élimination, combien d'opérations ? 🧮 ★ ⏱️ 10 min
**Objectif :** estimer le coût des deux méthodes de calcul d'un déterminant, et comprendre pourquoi personne n'utilise les cofacteurs en grande dimension.
**Prérequis :** fiche §1 · **Parcours :** C

Ordres de grandeur seulement ; une machine fait environ $10^9$ opérations par seconde.
1. Développer récursivement un déterminant $n \times n$ par cofacteurs demande environ $n!$ produits. Estime $20!$ (une puissance de 10 suffit ; la formule de Stirling, ou des regroupements, aident).
2. Combien de temps pour un déterminant $20 \times 20$ par cofacteurs ? Exprime-le en années. Et pour un déterminant $30 \times 30$ ($30! \approx 2{,}7 \times 10^{32}$) ? Compare les deux à l'âge de l'Univers (environ $1{,}4 \times 10^{10}$ ans).
3. L'élimination demande environ $\frac{2}{3}n^3$ opérations. Combien pour $n = 20$, et combien de temps ?
4. Et pour $n = 1\,000$ ?
5. Pour quel $n$ les cofacteurs restent-ils raisonnables (moins d'une seconde) ?

### Ex M12c.25 — Expliquer un vecteur propre avec une image 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer en mots, sans formule, ce qu'est un vecteur propre et une valeur propre.
**Prérequis :** fiche §3 · **Parcours :** C, E

Un ami curieux, qui n'a jamais fait d'algèbre linéaire, te demande ce que sont les « vecteurs propres » dont il entend parler. Explique-lui, **en huit lignes au plus**, sans formule, avec une image concrète (une transformation d'une feuille de caoutchouc, d'un tissu, d'une photo…) : ce qu'une transformation linéaire fait en général aux directions, ce qu'ont de particulier les directions propres, ce que dit la valeur propre (étirement, écrasement, retournement), et un exemple où il n'y en a pas.

<a id="entretien"></a>

## 💼 Entretien

### M12c.E1 — « Que représentent les valeurs propres d'une matrice de covariance ? » 💼 ★ ⏱️ 10 min
*Fiche §6 et §8 · parcours C*

« Que représentent les valeurs propres d'une matrice de covariance ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit dire ce que sont les vecteurs propres pour un nuage de données, ce que mesure chaque valeur propre, pourquoi elles sont réelles et positives, ce que vaut leur somme, ce que signifie une valeur propre nulle ou presque nulle, et un usage (réduction de dimension, conditionnement). Compare ensuite avec la réponse modèle de `05_solutions.md`.

### M12c.E2 — « Comment savoir qu'une matrice est définie positive, et pourquoi est-ce important en optimisation ? » 💼 ★ ⏱️ 10 min
*Fiche §7 · parcours C*

« Comment savoir qu'une matrice est définie positive, et pourquoi est-ce important en optimisation ? »

Prépare une réponse orale de **60 secondes**. Elle doit donner la définition, deux ou trois critères (dont celui qu'on utilise vraiment sur ordinateur), le lien avec la hessienne et la convexité, ce que cela garantit pour un minimum, et un exemple en machine learning. Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m12c_valeurs_propres/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M12c.26 | Le déterminant par élimination · `det` | 🔨 | ★ | 20 | C, E |
| M12c.27 | La méthode de la puissance et le quotient de Rayleigh · `power_iteration, rayleigh_quotient` | 🔨 | ★★ | 25 | C, E |
| M12c.28 | La décomposition de Cholesky et le test « définie positive » · `cholesky, is_positive_definite` | 🔨 | ★★ | 25 | C, E |
| M12c.29 | La racine carrée d'une matrice symétrique positive et la matrice de blanchiment · `sqrtm_psd, whitening_matrix` | 🔨 | ★★ | 25 | C, E |
| M12c.30 | `np.linalg.eigh`, `det`, `cholesky` et `scipy.linalg.sqrtm` contre tes fonctions | 📦 | ★ | 15 | C, E |
| M12c.31 | Prédire : la méthode de la puissance quand les deux plus grandes valeurs propres sont proches | 🔮 | ★ | 10 | C, E |
| M12c.32 | La vitesse de la méthode de la puissance et le rapport \|λ₂ / λ₁\| | 🔬 | ★★ | 20 | C |
| M12c.33 | Les lignes de niveau de xᵀAx : définie positive, semi-définie positive, indéfinie | 🎨 | ★ | 20 | C, E |
| M12c.34 | Chasse à l'erreur : det(A + B) = det A + det B, un vecteur propre nul, Cholesky d'une matrice non symétrique | 🐛 | ★ | 15 | C |
| M12c.35 | Vérifier avec SymPy : polynôme caractéristique, valeurs propres exactes, diagonalisation | 🛠️ | ★ | 15 | C |
| M12c.36 | Défi : les trois plus grandes valeurs propres d'une matrice symétrique semi-définie positive 300 × 300, par la puissance avec déflation, à 1e−6 près | 🏆 | ★★★ | 30 | C |
