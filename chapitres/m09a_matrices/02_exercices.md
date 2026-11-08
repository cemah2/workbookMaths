# M09a · Matrices et systèmes linéaires — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/m09a_matrices/06_mes_reponses.md` (créée par `python tools/start_chapter.py M09a`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂, 📖, 🧮, 🗣️ et 💼 se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

Dans tout le chapitre, les indices des matrices commencent à 1 (comme dans la fiche et dans MML) : $a_{23}$ est l'élément de la ligne 2 et de la colonne 3. Une **forme** se donne comme dans NumPy, (lignes, colonnes).

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### M09a.Q1 — Formes : ce qui se multiplie et ce qui ne se multiplie pas 🧠 ★ ⏱️ 4 min
*Fiche §1 et §3 · parcours C, E*

$\mathbf{A}$ a la forme $(3, 4)$, $\mathbf{B}$ la forme $(4, 2)$, $\mathbf{C}$ la forme $(2, 3)$, et $\mathbf{v}$ est un vecteur de $\mathbb{R}^4$.
1. La forme de $\mathbf{A}\mathbf{B}$ ?
2. $\mathbf{A}\mathbf{C}$ existe-t-il ?
3. La forme de $\mathbf{A}\mathbf{B}\mathbf{C}$ ?
4. Combien de coordonnées a $\mathbf{A}\mathbf{v}$ ?
5. La forme de $\mathbf{C}\mathbf{A}$ ?
6. Un dataset de 500 exemples à 12 features : quelle est sa forme, et que représente une colonne ?

### M09a.Q2 — Le produit matrice-vecteur, deux lectures 🧠 ★ ⏱️ 4 min
*Fiche §2 · parcours C, E*

$\mathbf{A} = \begin{pmatrix} 3 & 1 \\ -2 & 4 \end{pmatrix}$ et $\mathbf{x} = (2, -1)$.
1. La première coordonnée de $\mathbf{A}\mathbf{x}$, par la lecture en lignes ?
2. $\mathbf{A}\mathbf{x}$, écrit comme une combinaison des colonnes de $\mathbf{A}$, puis calculé ?
3. $\mathbf{A}\mathbf{e}_2$, avec $\mathbf{e}_2 = (0, 1)$ ?
4. Combien de multiplications coûte le produit d'une matrice $(m, n)$ par un vecteur ?
5. Vrai ou faux : si une colonne de $\mathbf{A}$ est le double d'une autre, il existe un $\mathbf{x}$ non nul tel que $\mathbf{A}\mathbf{x} = \mathbf{0}$.

### M09a.Q3 — Produit matriciel : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

Pour des matrices dont les produits existent :
1. $\mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A}$.
2. $(\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C})$.
3. Si $\mathbf{A}\mathbf{B} = \mathbf{0}$, alors $\mathbf{A} = \mathbf{0}$ ou $\mathbf{B} = \mathbf{0}$.
4. $(\mathbf{A} + \mathbf{B})^2 = \mathbf{A}^2 + 2\mathbf{A}\mathbf{B} + \mathbf{B}^2$ pour des matrices carrées.
5. Un produit $(n, p) \times (p, m)$ coûte $n\,p\,m$ multiplications.
6. $(\mathbf{A}\mathbf{B})\mathbf{C}$ et $\mathbf{A}(\mathbf{B}\mathbf{C})$ coûtent toujours le même nombre de multiplications.

### M09a.Q4 — Hadamard ou produit matriciel ? 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C*

1. Lequel des deux demande des matrices de même forme ?
2. Lequel est commutatif ?
3. Leur symbole en NumPy ?
4. Que donne $\mathbf{I}_2 \odot \mathbf{A}$ pour une matrice $2 \times 2$ $\mathbf{A}$ ? Et $\mathbf{I}_2\mathbf{A}$ ?
5. Mettre à zéro les poids d'un réseau marqués par une matrice de 0 et de 1 : lequel ?
6. Calculer les sorties d'une couche pour tout un batch : lequel ?

### M09a.Q5 — Les règles de la transposée 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. La forme de $\mathbf{A}^\top$ pour $\mathbf{A}$ de forme $(2, 5)$ ?
2. $(\mathbf{A}^\top)^\top$ ?
3. $(\mathbf{A}\mathbf{B})^\top$ en fonction de $\mathbf{A}^\top$ et $\mathbf{B}^\top$ ?
4. $(\mathbf{A}\mathbf{B}\mathbf{C})^\top$ ?
5. La forme de $\mathbf{X}^\top\mathbf{X}$ pour $\mathbf{X}$ de forme $(1000, 8)$ ?
6. Vrai ou faux : $\mathbf{X}^\top\mathbf{X}$ est toujours symétrique.

### M09a.Q6 — Combien de solutions ? 🧠 ★ ⏱️ 4 min
*Fiche §5 et §6 · parcours C, E*

1. Deux équations à deux inconnues dont les droites sont parallèles et distinctes ?
2. Un système linéaire peut-il avoir exactement deux solutions ?
3. Un système homogène $\mathbf{A}\mathbf{x} = \mathbf{0}$ peut-il n'avoir aucune solution ?
4. $\mathbf{A}$ carrée et inversible : combien de solutions pour $\mathbf{A}\mathbf{x} = \mathbf{b}$ ?
5. La forme réduite de $[\mathbf{A} \mid \mathbf{b}]$ a une ligne $(0 \;\; 0 \;\; 0 \mid 5)$ : combien de solutions ?
6. Deux équations à trois inconnues, qui ont au moins une solution : combien en ont-elles ?

### M09a.Q7 — Les opérations permises sur les lignes 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C, E*

Lesquelles de ces opérations sur les lignes d'une matrice augmentée ne changent jamais les solutions ?
1. Échanger les lignes 1 et 3.
2. Multiplier la ligne 2 par $-3$.
3. Multiplier la ligne 2 par 0.
4. Ajouter à la ligne 3 deux fois la ligne 1.
5. Ajouter 1 à chaque nombre de la ligne 1.
6. Remplacer en même temps $L_1$ par $L_1 - L_2$ et $L_2$ par $L_2 - L_1$.

### M09a.Q8 — Inverse et rang 🧠 ★ ⏱️ 4 min
*Fiche §7 et §8 · parcours C, E*

1. Une matrice de forme $(2, 3)$ peut-elle avoir une inverse ?
2. Le rang de la matrice nulle ?
3. Le rang maximal d'une matrice de forme $(4, 7)$ ?
4. Le rang de $\begin{pmatrix} 2 & -6 \\ -1 & 3 \end{pmatrix}$ ?
5. $(\mathbf{A}\mathbf{B})^{-1}$ en fonction de $\mathbf{A}^{-1}$ et $\mathbf{B}^{-1}$ ?
6. Vrai ou faux : une matrice carrée de taille $n$ est inversible si et seulement si son rang vaut $n$.

<a id="rappels"></a>

## 🔁 Rappels

### M09a.R1 — Les systèmes 2 × 2 (R2) 🔁 ★ ⏱️ 5 min
*Fiche §5 · parcours C, E*

1. Résous $2x + 3y = 7$ et $x - y = 1$.
2. Combien de solutions ont $2x + 3y = 7$ et $4x + 6y = 14$ ?
3. Et $2x + 3y = 7$ et $4x + 6y = 10$ ?
4. Pour quelle valeur de $a$ le système $ax + 2y = 1$, $3x + y = 4$ n'a-t-il pas une solution unique ?
5. Interprète géométriquement les réponses 2 et 3.

### M09a.R2 — Produit scalaire et normes (M07) 🔁 ★ ⏱️ 5 min
*Fiche §2 · parcours C, E*

$\mathbf{u} = (2, -1, 3)$ et $\mathbf{v} = (1, 4, 0)$.
1. $\mathbf{u} \cdot \mathbf{v}$ ?
2. $\lVert \mathbf{u} \rVert$ ?
3. $\lVert \mathbf{u} - \mathbf{v} \rVert^2$ ?
4. $\mathbf{e}_2 \cdot \mathbf{u}$, avec $\mathbf{e}_2 = (0, 1, 0)$ ?
5. Un vecteur non nul orthogonal à la fois à $\mathbf{u}$ et à $(0, 0, 1)$ ?

### M09a.R3 — Moyenne et écart-type empiriques (M02c) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C*

Une colonne d'un dataset contient les valeurs 4, 8, 6, 2.
1. Sa moyenne ?
2. Son écart-type avec $\mathrm{ddof} = 0$ (3 décimales) ?
3. Son écart-type avec $\mathrm{ddof} = 1$ (3 décimales) ?
4. La colonne centrée ?
5. La première valeur standardisée (avec $\mathrm{ddof} = 0$, 3 décimales) ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre entier, ou un nombre avec un point décimal, comme `-1.25`, arrondi comme le demande la question ;
- une fraction irréductible entre guillemets, comme `"7/9"` ;
- une liste entre crochets pour un vecteur ou une forme, comme `[2, -1, 0]` ; une matrice comme une liste de lignes, `[[1, 0], [-2, 3]]` ; vrai ou faux par `True` ou `False`.

### Ex M09a.1 — Un tableau de données vu comme une matrice : forme, lignes, colonnes, moyennes ✏️ ★ ⏱️ 15 min
**Objectif :** lire un tableau de données comme une matrice, et calculer des opérations par colonne.
**Prérequis :** fiche §1 ; M02c (moyenne, écart-type) · **Parcours :** C, E

Cinq capteurs d'une serre mesurent la température (°C), l'humidité (%) et la luminosité (klx) :

$$\mathbf{X} = \begin{pmatrix} 22 & 60 & 12 \\ 25 & 55 & 18 \\ 19 & 70 & 8 \\ 24 & 65 & 15 \\ 20 & 50 & 7 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | la forme de $\mathbf{X}$ | une liste de 2 entiers |
| b | l'élément $x_{32}$ | un nombre |
| c | les indices `[i, j]` de l'élément $x_{32}$ en Python (indices à partir de 0) | une liste de 2 entiers |
| d | la ligne 4 | une liste de 3 nombres |
| e | le vecteur des moyennes des colonnes | une liste de 3 nombres |
| f | la ligne 2 du tableau centré | une liste de 3 nombres |
| g | l'écart-type de la colonne de la température, avec $\mathrm{ddof} = 0$ | un nombre (4 décimales) |

Dans ta copie : que représente une ligne de $\mathbf{X}$ ? Une colonne ? Pourquoi centrer retire-t-il le **même** vecteur à chaque ligne ? Que vaut la moyenne de chaque colonne du tableau centré ?

### Ex M09a.2 — Le produit matrice-vecteur, par les lignes puis par les colonnes ✏️ ★ ⏱️ 15 min
**Objectif :** calculer un produit matrice-vecteur sous ses deux lectures, et prédire tout un dataset d'un coup.
**Prérequis :** fiche §2 ; M07 (produit scalaire) · **Parcours :** C, E

$$\mathbf{A} = \begin{pmatrix} 3 & -1 & 2 & 0 \\ 1 & 4 & -2 & 5 \\ -2 & 0 & 1 & 3 \end{pmatrix}, \qquad \mathbf{x} = (2, -1, 3, 1).$$

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de coordonnées de $\mathbf{A}\mathbf{x}$ | un entier |
| b | $\mathbf{A}\mathbf{x}$ | une liste de 3 nombres |
| c | le nombre de multiplications de ce produit | un entier |
| d | $\mathbf{A}\mathbf{e}_3$, avec $\mathbf{e}_3 = (0, 0, 1, 0)$ | une liste de 3 nombres |
| e | le vecteur $\mathbf{y}$ tel que $\mathbf{A}\mathbf{y}$ = colonne 1 + 2 × colonne 4 | une liste de 4 nombres |
| f | vrai ou faux : le produit de $\mathbf{A}$ par un vecteur de $\mathbb{R}^3$ existe | `True` ou `False` |
| g | les prédictions $\hat{\mathbf{y}} = \mathbf{X}\mathbf{w} + b$ pour $\mathbf{X} = \begin{pmatrix} 1{,}5 & 2 \\ 0 & 4 \\ 3 & -1 \end{pmatrix}$, $\mathbf{w} = (2 ;\ 0{,}5)$ et $b = -1$ | une liste de 3 nombres |

Dans ta copie : refais b) par la lecture en colonnes, et vérifie que tu trouves la même chose. Pourquoi d) donne-t-il une colonne de $\mathbf{A}$ ? Combien de multiplications coûterait g) pour un million d'exemples à 20 features ?

### Ex M09a.3 — Produits matriciels à la main : formes compatibles et calculs ✏️ ★ ⏱️ 20 min
**Objectif :** vérifier la compatibilité des formes, calculer des produits matriciels, et voir que l'ordre compte.
**Prérequis :** fiche §3 · **Parcours :** C, E

$$\mathbf{A} = \begin{pmatrix} 1 & -1 & 2 \\ 0 & 3 & 1 \end{pmatrix}, \qquad \mathbf{B} = \begin{pmatrix} 2 & 1 \\ -1 & 0 \\ 1 & 4 \end{pmatrix}, \qquad \mathbf{C} = \begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | la forme de $\mathbf{A}\mathbf{B}$ | une liste de 2 entiers |
| b | $\mathbf{A}\mathbf{B}$ | une matrice |
| c | la forme de $\mathbf{B}\mathbf{A}$ | une liste de 2 entiers |
| d | l'élément $(\mathbf{B}\mathbf{A})_{23}$, sans calculer tout $\mathbf{B}\mathbf{A}$ | un nombre |
| e | vrai ou faux : $\mathbf{A}\mathbf{C}$ existe | `True` ou `False` |
| f | $\mathbf{C}\mathbf{A}$ | une matrice |
| g | $(\mathbf{A}\mathbf{B})\mathbf{C}$ | une matrice |

Dans ta copie : calcule d) comme un produit scalaire d'une ligne et d'une colonne. Calcule aussi $\mathbf{A}(\mathbf{B}\mathbf{C})$ et compare avec g). Pourquoi $\mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A}$ n'a-t-il ici aucun sens ?

### Ex M09a.4 — Le coût d'un produit, et l'ordre des parenthèses dans ABC ✏️ ★★ ⏱️ 15 min
**Objectif :** compter les multiplications d'un produit matriciel, et choisir l'ordre des calculs le moins coûteux.
**Prérequis :** fiche §3 · **Parcours :** C

$\mathbf{A}$ a la forme $(20, 400)$, $\mathbf{B}$ la forme $(400, 5)$, $\mathbf{C}$ la forme $(5, 300)$, et $\mathbf{v}$ est un vecteur de $\mathbb{R}^{300}$.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre de multiplications de $\mathbf{A}\mathbf{B}$ | un entier |
| b | le nombre de multiplications de $(\mathbf{A}\mathbf{B})\mathbf{C}$, en tout | un entier |
| c | le nombre de multiplications de $\mathbf{A}(\mathbf{B}\mathbf{C})$, en tout | un entier |
| d | le rapport du coût de $\mathbf{A}(\mathbf{B}\mathbf{C})$ à celui de $(\mathbf{A}\mathbf{B})\mathbf{C}$ | un nombre (1 décimale) |
| e | la forme de $\mathbf{A}\mathbf{B}\mathbf{C}$ | une liste de 2 entiers |
| f | le nombre de multiplications de $\mathbf{A}(\mathbf{B}(\mathbf{C}\mathbf{v}))$, en tout | un entier |
| g | pour deux matrices carrées de taille $n$, par combien le nombre de multiplications est-il multiplié quand $n$ est multiplié par 3 | un entier |

Dans ta copie : quelle règle simple permet de choisir les parenthèses ? Compare f) au coût de $((\mathbf{A}\mathbf{B})\mathbf{C})\mathbf{v}$. Pourquoi le résultat est-il le même dans tous les ordres ?

### Ex M09a.5 — Une couche dense Z = XW + b à la main : deux exemples, trois entrées, deux sorties ✏️ ★ ⏱️ 20 min
**Objectif :** calculer la sortie d'une couche dense pour un batch, et lire ses formes et ses paramètres.
**Prérequis :** fiche §3 ; M07 (score d'un neurone) · **Parcours :** C, E

Une couche de deux neurones reçoit trois entrées. Ses poids, rangés une colonne par neurone, et ses biais sont

$$\mathbf{W} = \begin{pmatrix} 2 & -1 \\ 0 & 1 \\ 1 & 3 \end{pmatrix}, \qquad \mathbf{b} = (-1 ;\ 0{,}5),$$

et le batch contient deux exemples, $\mathbf{X} = \begin{pmatrix} 1 & 0 & 2 \\ -1 & 3 & 1 \end{pmatrix}$. La fonction ReLU vaut $\max(0, z)$, élément par élément.

| | Question | Réponse attendue |
|---|---|---|
| a | la forme de $\mathbf{W}$ | une liste de 2 entiers |
| b | $\mathbf{Z} = \mathbf{X}\mathbf{W} + \mathbf{b}$ | une matrice |
| c | $z_{21}$, la sortie du neurone 1 pour l'exemple 2 | un nombre |
| d | $\operatorname{ReLU}(\mathbf{Z})$ | une matrice |
| e | le nombre de paramètres de la couche (poids et biais) | un entier |
| f | la forme de la matrice des poids de cette couche dans PyTorch (`nn.Linear`) | une liste de 2 entiers |
| g | le nombre de multiplications de $\mathbf{X}\mathbf{W}$ | un entier |

Dans ta copie : quelle colonne de $\mathbf{W}$ contient les poids du neurone 2 ? Pourquoi $\mathbf{b}$ est-il ajouté à chaque ligne ? Que deviendrait la forme de $\mathbf{Z}$ pour un batch de 128 exemples ?

### Ex M09a.6 — Un embedding : une ligne one-hot fois une matrice ✏️ ★ ⏱️ 10 min
**Objectif :** voir qu'un embedding est un produit d'une ligne one-hot par une matrice, et en déduire des moyennes d'embeddings.
**Prérequis :** fiche §3 ; M07 (one-hot) · **Parcours :** C

Un vocabulaire de 5 mots (numérotés de 1 à 5) a la table d'embedding

$$\mathbf{E} = \begin{pmatrix} 0{,}1 & -0{,}4 & 1{,}2 \\ 0{,}9 & 0 & -0{,}3 \\ -1{,}1 & 0{,}6 & 0{,}2 \\ 0{,}5 & 1{,}5 & -0{,}8 \\ 0 & -0{,}2 & 0{,}7 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | le vecteur one-hot du mot 4 | une liste de 5 nombres |
| b | le produit de ce vecteur (en ligne) par $\mathbf{E}$ | une liste de 3 nombres |
| c | le nombre de paramètres de la table | un entier |
| d | le nombre de multiplications du produit de b), fait sans raccourci | un entier |
| e | le produit de la ligne $(0, 1, 0, 0, 1)$ par $\mathbf{E}$ | une liste de 3 nombres |
| f | la moyenne des embeddings de la phrase « mot 1, mot 3, mot 3 », écrite comme $\frac{1}{3}(1, 0, 2, 0, 0)\,\mathbf{E}$ | une liste de 3 nombres (4 décimales) |

Dans ta copie : pourquoi ne calcule-t-on jamais ce produit en pratique ? Que représente la ligne de comptage de f) ?

### Ex M09a.7 — Transposées de produits, et la matrice symétrique XᵀX ✏️ ★ ⏱️ 15 min
**Objectif :** appliquer la règle de la transposée d'un produit, et calculer une matrice $\mathbf{X}^\top\mathbf{X}$.
**Prérequis :** fiche §4 · **Parcours :** C, E

$$\mathbf{A} = \begin{pmatrix} 2 & 0 \\ 1 & -1 \\ -1 & 3 \end{pmatrix}, \qquad \mathbf{B} = \begin{pmatrix} 1 & 4 & 0 \\ 2 & -1 & 1 \end{pmatrix}, \qquad \mathbf{X} = \begin{pmatrix} 1 & -1 & 2 \\ 0 & 2 & 1 \\ 2 & 1 & 0 \\ 1 & 0 & -1 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | la forme de $(\mathbf{A}\mathbf{B})^\top$ | une liste de 2 entiers |
| b | $(\mathbf{A}\mathbf{B})^\top$ | une matrice |
| c | $(\mathbf{B}\mathbf{A})^\top$ | une matrice |
| d | vrai ou faux : $(\mathbf{A}\mathbf{B})^\top = \mathbf{A}^\top\mathbf{B}^\top$ | `True` ou `False` |
| e | $\mathbf{X}^\top\mathbf{X}$ | une matrice |
| f | la forme de $\mathbf{X}\mathbf{X}^\top$ | une liste de 2 entiers |
| g | l'élément $(\mathbf{X}\mathbf{X}^\top)_{12}$ | un nombre |

Dans ta copie : vérifie b) en calculant $\mathbf{B}^\top\mathbf{A}^\top$. Que représentent les nombres de la diagonale de $\mathbf{X}^\top\mathbf{X}$ ? Et un zéro hors de la diagonale ? Que dit g) des exemples 1 et 2 ?

### Ex M09a.8 — Le pivot de Gauss sur un système 3 × 3 à solution unique ✏️ ★★ ⏱️ 25 min
**Objectif :** résoudre un système $3 \times 3$ par le pivot de Gauss, étape par étape, puis par remontée.
**Prérequis :** fiche §5 et §6 · **Parcours :** C, E

$$\left\{\begin{array}{rcl} 2x + y - z &=& -3 \\ x - y + 2z &=& 9 \\ 3x + 2y + z &=& 2 \end{array}\right.$$

Suis cette démarche : échange les deux premières équations, pour avoir le pivot 1 ; annule $x$ dans les deux autres équations avec la nouvelle première ; puis annule $y$ dans la troisième avec la nouvelle deuxième ; enfin, remonte.

| | Question | Réponse attendue |
|---|---|---|
| a | le multiple de la nouvelle première ligne à retrancher à la ligne $2x + y - z = -3$ | un nombre |
| b | cette ligne après l'élimination de $x$ (la matrice augmentée, quatre nombres) | une liste de 4 nombres |
| c | la troisième ligne après l'élimination de $x$ | une liste de 4 nombres |
| d | le multiple de la deuxième ligne à retrancher à la troisième pour annuler $y$ | une fraction irréductible |
| e | la valeur de $z$ | un nombre |
| f | la solution $(x, y, z)$ | une liste de 3 nombres |

Dans ta copie : écris la forme échelonnée complète, puis la forme échelonnée réduite. Vérifie la solution dans les trois équations de départ. Pourquoi l'échange du début ne change-t-il pas les solutions ?

### Ex M09a.9 — Un système sans solution, un système à une infinité de solutions ✏️ ★★ ⏱️ 25 min
**Objectif :** reconnaître sur une forme échelonnée un système sans solution et un système à une infinité de solutions, et décrire ces dernières.
**Prérequis :** fiche §5 et §6 · **Parcours :** C, E

$$(S_1) \left\{\begin{array}{rcl} x + 2y - z &=& 1 \\ 2x + 5y + z &=& 4 \\ 3x + 7y &=& 6 \end{array}\right. \qquad (S_2) \left\{\begin{array}{rcl} x + 2y - z &=& 1 \\ 2x + 5y + z &=& 4 \\ 3x + 7y &=& 5 \end{array}\right.$$

Les deux systèmes ne diffèrent que par le second membre de la troisième équation.

| | Question | Réponse attendue |
|---|---|---|
| a | la dernière ligne d'une forme échelonnée de la matrice augmentée de $(S_1)$, obtenue par $L_2 \leftarrow L_2 - 2L_1$, $L_3 \leftarrow L_3 - 3L_1$, puis $L_3 \leftarrow L_3 - L_2$ | une liste de 4 nombres |
| b | le nombre de solutions de $(S_1)$ | un entier |
| c | la forme échelonnée réduite de la matrice augmentée de $(S_2)$ | une matrice |
| d | le nombre de variables libres de $(S_2)$ | un entier |
| e | la solution de $(S_2)$ telle que $z = 0$ | une liste de 3 nombres |
| f | la solution de $(S_2)$ telle que $z = 1$ | une liste de 3 nombres |
| g | la seule valeur du second membre de la troisième équation pour laquelle le système a des solutions | un nombre |

Dans ta copie : écris la solution générale de $(S_2)$ avec un paramètre $t$. Montre que la différence des solutions de e) et f) résout le système homogène. Pourquoi g) était-il prévisible en regardant les trois lignes de la matrice des coefficients ?

### Ex M09a.10 — La forme échelonnée réduite d'une matrice 3 × 4 et la solution générale ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer une forme échelonnée réduite, y lire les variables de base et les variables libres, et écrire la solution générale.
**Prérequis :** fiche §6 · **Parcours :** C

La matrice augmentée d'un système de trois équations à trois inconnues $x$, $y$, $z$ est

$$\left(\begin{array}{ccc|c} 1 & -1 & 2 & 1 \\ 2 & -1 & 5 & 4 \\ 0 & 1 & 1 & 2 \end{array}\right).$$

| | Question | Réponse attendue |
|---|---|---|
| a | sa forme échelonnée réduite | une matrice |
| b | les numéros (à partir de 1) des colonnes qui portent un pivot | une liste d'entiers |
| c | le rang de la matrice des coefficients ($3 \times 3$) | un entier |
| d | la solution telle que $z = 0$ | une liste de 3 nombres |
| e | la solution telle que $z = 2$ | une liste de 3 nombres |
| f | une solution non nulle du système homogène $\mathbf{A}\mathbf{x} = \mathbf{0}$, avec $z = 1$ | une liste de 3 nombres |
| g | vrai ou faux : $(6, 3, -1)$ est solution du système | `True` ou `False` |

Dans ta copie : écris la solution générale, sous la forme « une solution particulière plus $t$ fois une solution du système homogène ». Quelle variable est libre, et pourquoi ?

### Ex M09a.11 — L'inverse d'une matrice 2 × 2, par la formule, puis vérifiée ✏️ ★ ⏱️ 15 min
**Objectif :** calculer l'inverse d'une matrice $2 \times 2$, la vérifier, et s'en servir pour résoudre un système.
**Prérequis :** fiche §7 · **Parcours :** C, E

Soit $\mathbf{A} = \begin{pmatrix} 5 & 4 \\ 2 & 2 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre $ad - bc$ de $\mathbf{A}$ | un nombre |
| b | $\mathbf{A}^{-1}$ | une matrice |
| c | la solution $(x, y)$ de $5x + 4y = 6$, $2x + 2y = 2$ | une liste de 2 nombres |
| d | la valeur de $k$ pour laquelle $\begin{pmatrix} k & 4 \\ 2 & 2 \end{pmatrix}$ n'est pas inversible | un nombre |
| e | l'inverse de la matrice diagonale $\begin{pmatrix} 4 & 0 \\ 0 & -0{,}5 \end{pmatrix}$ | une matrice |
| f | $(2\mathbf{A})^{-1}$ | une matrice |
| g | $(\mathbf{A}^\top)^{-1}$ | une matrice |

Dans ta copie : vérifie b) en calculant $\mathbf{A}\mathbf{A}^{-1}$ **et** $\mathbf{A}^{-1}\mathbf{A}$. Pour d), que dire des deux colonnes de la matrice ? Justifie f) et g) par les règles de la fiche, sans recalculer.

### Ex M09a.12 — L'inverse d'une matrice 3 × 3 par Gauss-Jordan ✏️ ★★ ⏱️ 25 min
**Objectif :** calculer l'inverse d'une matrice $3 \times 3$ en réduisant $[\mathbf{A} \mid \mathbf{I}]$, et s'en servir.
**Prérequis :** fiche §7 ; Ex M09a.8 · **Parcours :** C

Soit $\mathbf{A} = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & 2 \\ 1 & 1 & 0 \end{pmatrix}$.

| | Question | Réponse attendue |
|---|---|---|
| a | $\mathbf{A}^{-1}$ | une matrice |
| b | la solution de $\mathbf{A}\mathbf{x} = (1, 0, 2)$, calculée avec $\mathbf{A}^{-1}$ | une liste de 3 nombres |
| c | la solution de $\mathbf{A}\mathbf{x} = (0, 1, 0)$ | une liste de 3 nombres |
| d | la première ligne de $(\mathbf{A}^\top)^{-1}$ | une liste de 3 nombres |
| e | vrai ou faux : $\begin{pmatrix} 1 & 2 & 1 \\ 0 & 1 & 2 \\ 1 & 3 & 3 \end{pmatrix}$ est inversible | `True` ou `False` |

Dans ta copie : écris chaque étape de la réduction de $[\mathbf{A} \mid \mathbf{I}_3]$. Pourquoi la réponse c) est-elle une colonne de $\mathbf{A}^{-1}$ ? Que se passe-t-il si l'on réduit $[\mathbf{B} \mid \mathbf{I}_3]$ pour la matrice $\mathbf{B}$ de e) ?

### Ex M09a.13 — Le rang de quatre matrices, et les colonnes redondantes ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des rangs par le pivot de Gauss, et trouver la combinaison qui rend une colonne redondante.
**Prérequis :** fiche §6 et §8 · **Parcours :** C, E

$$\mathbf{M}_1 = \begin{pmatrix} 1 & 2 \\ 3 & 6 \\ -2 & -4 \end{pmatrix}, \quad \mathbf{M}_2 = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \\ 1 & 1 & 1 \end{pmatrix}, \quad \mathbf{M}_3 = \begin{pmatrix} 2 & 1 & 0 & 3 \\ 1 & 0 & 1 & 1 \\ 0 & 1 & -2 & 1 \end{pmatrix}, \quad \mathbf{M}_4 = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 3 & 1 \\ 0 & 0 & -1 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | le rang de $\mathbf{M}_1$ | un entier |
| b | le rang de $\mathbf{M}_2$ | un entier |
| c | le rang de $\mathbf{M}_3$ | un entier |
| d | le rang de $\mathbf{M}_4$ | un entier |
| e | les nombres $[a, b]$ tels que la colonne 3 de $\mathbf{M}_2$ vaut $a$ fois la colonne 1 plus $b$ fois la colonne 2 | une liste de 2 nombres |
| f | vrai ou faux : $\mathbf{M}_2$ est inversible | `True` ou `False` |
| g | le rang de $\mathbf{M}_3^\top$ | un entier |

Dans ta copie : pour $\mathbf{M}_3$, écris les colonnes 3 et 4 comme des combinaisons des colonnes 1 et 2. Pourquoi le rang de $\mathbf{M}_4$ se lit-il sans calcul ?

### Ex M09a.14 — Mettre un problème en système : trois engrais pour trois nutriments ✏️ ★★ ⏱️ 20 min
**Objectif :** traduire un problème concret en système linéaire, le résoudre, et interpréter la solution.
**Prérequis :** fiche §5 et §6 · **Parcours :** C

Un jardinier dispose de trois engrais. Un kilogramme de chacun apporte (en grammes) :

| | azote (N) | phosphore (P) | potassium (K) |
|---|---|---|---|
| engrais 1 | 200 | 100 | 0 |
| engrais 2 | 100 | 0 | 200 |
| engrais 3 | 0 | 150 | 100 |

Il lui faut exactement 1 100 g d'azote, 700 g de phosphore et 800 g de potassium. On note $x$, $y$, $z$ les masses (en kg) des engrais 1, 2 et 3.

| | Question | Réponse attendue |
|---|---|---|
| a | la matrice $\mathbf{A}$ du système $\mathbf{A}\mathbf{x} = \mathbf{b}$, une ligne par nutriment, une colonne par engrais | une matrice |
| b | la solution $(x, y, z)$ | une liste de 3 nombres |
| c | la masse totale d'engrais | un nombre |
| d | la masse d'engrais 3 si le besoin en potassium passe à 1 000 g (les autres inchangés) | une fraction irréductible |
| e | la solution des deux équations de l'azote et du phosphore, avec seulement les engrais 1 et 2 | une liste de 2 nombres |

Dans ta copie : pourquoi la solution de e) n'a-t-elle pas de sens pour le jardinier ? Qu'aurait signifié une matrice $\mathbf{A}$ singulière ?

<a id="demonstrations"></a>

## ∂ Démonstrations

Rédige chaque démonstration dans ta copie : hypothèses, étapes justifiées, conclusion. Juge-la ensuite avec la **grille de relecture** de `05_solutions.md`.

### Ex M09a.15 — (AB)ᵀ = BᵀAᵀ, coefficient par coefficient ∂ ★ ⏱️ 15 min
**Objectif :** démontrer la règle de la transposée d'un produit à partir des définitions, et en tirer deux conséquences.
**Prérequis :** fiche §3 et §4 ; R4 (le symbole $\sum$) · **Parcours :** C, E

$\mathbf{A}$ a la forme $(n, p)$ et $\mathbf{B}$ la forme $(p, m)$.
1. Donne les formes de $(\mathbf{A}\mathbf{B})^\top$ et de $\mathbf{B}^\top\mathbf{A}^\top$, et vérifie qu'elles sont égales.
2. Écris l'élément $(i, j)$ de $(\mathbf{A}\mathbf{B})^\top$ avec un symbole $\sum$.
3. Écris l'élément $(i, j)$ de $\mathbf{B}^\top\mathbf{A}^\top$ avec un symbole $\sum$, en revenant aux éléments de $\mathbf{A}$ et de $\mathbf{B}$.
4. Conclus.
5. Déduis-en $(\mathbf{A}\mathbf{B}\mathbf{C})^\top = \mathbf{C}^\top\mathbf{B}^\top\mathbf{A}^\top$.
6. Déduis-en que $\mathbf{X}^\top\mathbf{X}$ est symétrique pour toute matrice $\mathbf{X}$.

### Ex M09a.16 — L'inverse est unique, et (AB)⁻¹ = B⁻¹A⁻¹ ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer l'unicité de l'inverse et la règle de l'inverse d'un produit, et voir ce qui change sans inverse.
**Prérequis :** fiche §3 et §7 · **Parcours :** C

$\mathbf{A}$ et $\mathbf{B}$ sont des matrices carrées de taille $n$.
1. On suppose que $\mathbf{B}$ et $\mathbf{C}$ vérifient toutes deux $\mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A} = \mathbf{I}$ et $\mathbf{A}\mathbf{C} = \mathbf{C}\mathbf{A} = \mathbf{I}$. Montre que $\mathbf{B} = \mathbf{C}$ (pars de $\mathbf{B} = \mathbf{B}\mathbf{I}$).
2. On suppose $\mathbf{A}$ et $\mathbf{B}$ inversibles. Montre que $\mathbf{A}\mathbf{B}$ est inversible, d'inverse $\mathbf{B}^{-1}\mathbf{A}^{-1}$ (calcule les deux produits).
3. Montre que, si $\mathbf{A}$ est inversible, $\mathbf{A}^\top$ l'est aussi, d'inverse $(\mathbf{A}^{-1})^\top$ (utilise M09a.15).
4. Montre que, si $\mathbf{A}$ est inversible, $\mathbf{A}\mathbf{B} = \mathbf{A}\mathbf{C}$ entraîne $\mathbf{B} = \mathbf{C}$.
5. Trouve deux matrices $2 \times 2$ $\mathbf{B} \ne \mathbf{C}$ et une matrice $\mathbf{A} \ne \mathbf{0}$ telles que $\mathbf{A}\mathbf{B} = \mathbf{A}\mathbf{C}$. Pourquoi cela ne contredit-il pas la question 4 ?

### Ex M09a.17 — Deux solutions distinctes entraînent une infinité de solutions ∂ ★★ ⏱️ 15 min
**Objectif :** démontrer qu'un système linéaire n'a jamais exactement deux solutions, et décrire ses solutions à partir de l'une d'elles.
**Prérequis :** fiche §5 · **Parcours :** C, E

Soit un système $\mathbf{A}\mathbf{x} = \mathbf{b}$, avec $\mathbf{A}$ de forme $(m, n)$.
1. On suppose que $\mathbf{x}$ et $\mathbf{y}$ sont deux solutions. Montre que $\mathbf{d} = \mathbf{y} - \mathbf{x}$ vérifie $\mathbf{A}\mathbf{d} = \mathbf{0}$.
2. Montre que, pour tout réel $t$, $\mathbf{x} + t\,\mathbf{d}$ est solution.
3. Montre que, si $\mathbf{x} \ne \mathbf{y}$, deux valeurs différentes de $t$ donnent deux solutions différentes. Conclus.
4. Montre que toute solution s'écrit $\mathbf{x} + \mathbf{h}$, avec $\mathbf{h}$ une solution du système homogène $\mathbf{A}\mathbf{h} = \mathbf{0}$, et que réciproquement tout vecteur de cette forme est solution.
5. Déduis-en que, si le système homogène n'a que la solution $\mathbf{0}$, alors $\mathbf{A}\mathbf{x} = \mathbf{b}$ a au plus une solution.

### Ex M09a.18 — Une matrice dont une colonne combine les autres n'est pas inversible ∂ ★★ ⏱️ 20 min
**Objectif :** démontrer qu'une colonne redondante rend une matrice carrée singulière, et en voir les conséquences pour les systèmes.
**Prérequis :** fiche §2, §7 et §8 ; Ex M09a.17 · **Parcours :** C

Soit $\mathbf{A}$ une matrice carrée de taille $n$, de colonnes $\mathbf{a}_1, \ldots, \mathbf{a}_n$, dont la dernière est une combinaison des autres : $\mathbf{a}_n = \lambda_1\mathbf{a}_1 + \cdots + \lambda_{n-1}\mathbf{a}_{n-1}$.
1. Trouve un vecteur $\mathbf{c} \ne \mathbf{0}$ tel que $\mathbf{A}\mathbf{c} = \mathbf{0}$ (utilise la lecture en colonnes du produit).
2. Montre que $\mathbf{A}$ n'est pas inversible (raisonne par l'absurde).
3. Montre que, pour tout $\mathbf{b}$, le système $\mathbf{A}\mathbf{x} = \mathbf{b}$ a zéro ou une infinité de solutions.
4. Applique au cas de la matrice $\mathbf{M}_2$ de M09a.13 : donne $\mathbf{c}$, et vérifie $\mathbf{M}_2\mathbf{c} = \mathbf{0}$.
5. Un dataset a une colonne de 1 (pour le biais) et le one-hot de toutes les catégories d'une feature. Explique, avec la question 1, pourquoi $\mathbf{X}^\top\mathbf{X}$ n'est pas inversible (indication : calcule $\mathbf{X}^\top\mathbf{X}\mathbf{c}$).

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M09a.19 — Pont : une passe avant à deux couches, deux produits matriciels et leurs formes 🔗 ★ ⏱️ 15 min
**Objectif :** suivre les formes et les calculs d'une passe avant à deux couches, et compter ses paramètres et ses multiplications.
**Prérequis :** fiche §3 ; Ex M09a.5 · **Parcours :** C, E

Un petit réseau reçoit des exemples à 3 features, a une couche cachée de 5 neurones (activation ReLU) et une couche de sortie de 2 neurones : $\mathbf{H} = \operatorname{ReLU}(\mathbf{X}\mathbf{W}_1 + \mathbf{b}_1)$, puis $\mathbf{Y} = \mathbf{H}\mathbf{W}_2 + \mathbf{b}_2$.

| | Question | Réponse attendue |
|---|---|---|
| a | la forme de $\mathbf{H}$ pour un batch de 64 exemples | une liste de 2 entiers |
| b | la forme de $\mathbf{Y}$ pour ce batch | une liste de 2 entiers |
| c | le nombre de paramètres du réseau (poids et biais des deux couches) | un entier |
| d | le nombre de multiplications des deux produits matriciels, pour ce batch | un entier |

Un réseau plus petit, à 2 entrées, 3 neurones cachés et 1 sortie, a $\mathbf{W}_1 = \begin{pmatrix} 1 & 0 & 2 \\ -1 & 1 & 1 \end{pmatrix}$, $\mathbf{b}_1 = (0 ;\ 0{,}5 ;\ -1)$, $\mathbf{W}_2 = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$, $b_2 = 0{,}5$. On lui donne l'exemple $\mathbf{x} = (1, -1)$.

| | Question | Réponse attendue |
|---|---|---|
| e | le vecteur caché $\mathbf{h} = \operatorname{ReLU}(\mathbf{x}\mathbf{W}_1 + \mathbf{b}_1)$ | une liste de 3 nombres |
| f | la sortie $y$ | un nombre |
| g | vrai ou faux : sans la fonction d'activation, les deux couches feraient le même calcul qu'une seule couche, de poids $\mathbf{W}_1\mathbf{W}_2$ | `True` ou `False` |

Dans ta copie : quel biais aurait la couche unique de g) ? Pourquoi un réseau sans activation ne peut-il donc rien calculer de plus qu'un modèle linéaire ?

### Ex M09a.20 — Pont : centrer et réduire un tableau en écriture matricielle 🔗 ★★ ⏱️ 15 min
**Objectif :** écrire le centrage et la réduction d'un tableau avec des produits matriciels, et calculer la matrice de covariance des features.
**Prérequis :** fiche §1, §3 et §4 ; M02c (écart-type) · **Parcours :** C

$$\mathbf{X} = \begin{pmatrix} 2 & 10 \\ 4 & 30 \\ 6 & 20 \end{pmatrix}.$$

On note $\boldsymbol{\mu}$ le vecteur des moyennes des colonnes, $\mathbf{X}_c = \mathbf{X} - \mathbf{1}\boldsymbol{\mu}^\top$ le tableau centré ($\mathbf{1}$ la colonne de trois 1), $\mathbf{D}$ la matrice diagonale des écarts-types des colonnes ($\mathrm{ddof} = 0$) et $\mathbf{X}_s = \mathbf{X}_c\mathbf{D}^{-1}$ le tableau standardisé.

| | Question | Réponse attendue |
|---|---|---|
| a | $\boldsymbol{\mu}$ | une liste de 2 nombres |
| b | la forme de $\mathbf{1}\boldsymbol{\mu}^\top$ | une liste de 2 entiers |
| c | $\mathbf{X}_c$ | une matrice |
| d | les deux nombres de la diagonale de $\mathbf{D}^{-1}$ | une liste de 2 nombres (4 décimales) |
| e | la première ligne de $\mathbf{X}_s$ | une liste de 2 nombres (3 décimales) |
| f | $\frac{1}{3}\mathbf{X}_c^\top\mathbf{X}_c$, la matrice de covariance des deux features | une matrice (4 décimales) |
| g | l'élément hors diagonale de $\frac{1}{3}\mathbf{X}_s^\top\mathbf{X}_s$ | un nombre |

Dans ta copie : pourquoi multiplier **à droite** par $\mathbf{D}^{-1}$ divise-t-il chaque **colonne** par son écart-type ? Que valent les nombres de la diagonale de $\frac{1}{3}\mathbf{X}_s^\top\mathbf{X}_s$, et pourquoi ? Comment s'appelle l'élément de g) ?

### Ex M09a.21 — MML §2.1 et §2.2 : systèmes et matrices, en anglais 📖 ★★ ⏱️ 30 min
**Objectif :** lire en anglais les deux premières sections du chapitre d'algèbre linéaire du livre, et relier ses notions à la fiche.
**Prérequis :** fiche §1 à §5 · **Parcours :** C

Lis MML §2.1 et §2.2. Réponds dans ta copie, **avec tes mots** (ne recopie pas le livre).
1. Au §2.1, quelle lecture géométrique le livre donne-t-il d'un système de deux équations à deux inconnues ? Et à trois inconnues ? Combien de solutions un système linéaire peut-il avoir ?
2. Au §2.2.1, comment le livre définit-il le produit de deux matrices, et quelle condition sur les formes impose-t-il ? Quel nom donne-t-il au produit élément par élément ?
3. Au §2.2.2, quels mots anglais le livre emploie-t-il pour une matrice inversible et pour une matrice qui ne l'est pas ? Quelle formule donne-t-il pour une matrice $2 \times 2$ ?
4. Toujours au §2.2.2, comment le livre définit-il une matrice symétrique ? Écris trois règles de la transposée ou de l'inverse qu'il énonce, et retrouve-les dans la fiche.
5. Au §2.2.4, comment le livre écrit-il un système de façon compacte ? Quelle lecture du produit $\mathbf{A}\mathbf{x}$ met-il en avant ?
6. Note trois mots ou tournures en anglais de ces deux sections, avec leur traduction.

### Ex M09a.22 — MML §2.3 : résoudre un système, la forme échelonnée et le « Minus-1 trick » 📖 ★★ ⏱️ 30 min
**Objectif :** lire la section du livre sur la résolution des systèmes, et appliquer son astuce pour trouver les solutions d'un système homogène.
**Prérequis :** fiche §5, §6 et §8 · **Parcours :** C

Lis MML §2.3. Réponds dans ta copie, **avec tes mots**.
1. Au §2.3.1, que sont une solution particulière et la solution générale ? En combien d'étapes le livre construit-il la solution générale ?
2. Au §2.3.2, quelles opérations élémentaires le livre autorise-t-il ? Comment définit-il la forme échelonnée, le pivot, les variables de base et les variables libres ?
3. Toujours au §2.3.2, qu'ajoute la forme échelonnée **réduite** ? Compare à la fiche (§6).
4. Le §2.3.3 propose le « Minus-1 trick ». Décris-le en deux phrases. Applique-le à la forme échelonnée réduite $\begin{pmatrix} 1 & 2 & 0 & -1 \\ 0 & 0 & 1 & 3 \end{pmatrix}$ (système homogène à quatre inconnues) : quelles solutions obtiens-tu ? Vérifie-les.
5. Au §2.3.4, pourquoi le livre évoque-t-il d'autres méthodes que le pivot de Gauss pour les très grands systèmes ?
6. Note trois mots ou tournures en anglais de cette section, avec leur traduction.

### Ex M09a.23 — Fermi : combien de multiplications pour une passe avant sur un million d'images ? 🧮 ★ ⏱️ 10 min
**Objectif :** estimer le coût d'une passe avant par le nombre de multiplications de ses produits matriciels, et le traduire en temps.
**Prérequis :** fiche §3 · **Parcours :** C

Un réseau classe des images couleur de $32 \times 32$ pixels (3 canaux, aplaties en un vecteur), avec deux couches cachées de 1 024 et 256 neurones et une sortie de 10 classes. Ordres de grandeur seulement (une puissance de 10 suffit, sauf en 1).
1. Combien de nombres décrivent une image ? Combien de multiplications coûte une image, couche par couche, puis en tout ?
2. Combien pour un million d'images ?
3. Un GPU récent fait de l'ordre de $10^{14}$ multiplications par seconde sur ces produits ; un processeur, de l'ordre de $10^{11}$ ; une triple boucle Python, de l'ordre de $10^{7}$. Combien de temps dans chaque cas ?
4. Quelle couche domine le coût, et pourquoi ?
5. Combien d'octets occupent les poids du réseau en `float32` (4 octets par nombre) ?

### Ex M09a.24 — Expliquer pourquoi on ne calcule pas l'inverse pour résoudre un système 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer, sans formule, pourquoi on résout un système par élimination plutôt qu'en calculant une inverse.
**Prérequis :** fiche §6 et §7 · **Parcours :** C, E

Un collègue a écrit `x = np.linalg.inv(A) @ b` pour résoudre un système de 5 000 équations. Explique-lui, **en huit lignes au plus**, sans formule : ce que fait `np.linalg.solve` à la place, pourquoi c'est plus rapide, pourquoi c'est plus précis, et à quoi sert quand même l'inverse.

<a id="entretien"></a>

## 💼 Entretien

### M09a.E1 — « Combien coûte un produit matriciel, et pourquoi les GPU l'accélèrent-ils ? » 💼 ★ ⏱️ 10 min
*Fiche §3 · parcours C*

« Combien coûte un produit matriciel, et pourquoi les GPU l'accélèrent-ils ? »

Prépare une réponse orale de **60 secondes**, que tu dirais à voix haute en entretien. Elle doit donner le coût d'un produit $(n, p) \times (p, m)$ et celui de deux matrices carrées, dire pourquoi ces calculs se prêtent au parallélisme, citer un exemple de réseau où ce produit domine, et un piège de coût (l'ordre des parenthèses). Compare ensuite avec la réponse modèle de `05_solutions.md`.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/m09a_matrices/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| M09a.25 | Le produit matriciel et la transposée · `matmul, transpose` | 🔨 | ★ | 20 | C, E |
| M09a.26 | La forme échelonnée réduite et le rang · `rref, rank` | 🔨 | ★★ | 35 | C, E |
| M09a.27 | Résoudre un système par le pivot de Gauss · `solve` | 🔨 | ★★ | 30 | C, E |
| M09a.28 | L'inverse par Gauss-Jordan · `inverse` | 🔨 | ★ | 20 | C |
| M09a.29 | `@`, `*`, `.T`, `np.linalg.solve`, `matrix_rank` et `sympy.Matrix.rref` contre tes fonctions | 📦 | ★ | 15 | C, E |
| M09a.30 | Prédire la forme du résultat : `@`, `*` et broadcasting | 🔮 | ★ | 10 | C, E |
| M09a.31 | Le temps d'un produit matriciel en fonction de n : une pente de 3 en échelle log-log | 🔬 | ★★ | 20 | C |
| M09a.32 | Pourquoi le pivot partiel : un petit pivot et les arrondis | 🔬 | ★★ | 20 | C |
| M09a.33 | Une matrice 2 × 2 comme transformation du plan : la grille et le carré unité | 🎨 | ★ | 20 | C |
| M09a.34 | Chasse à l'erreur : `*` au lieu de `@`, une transposée oubliée, un pivot nul | 🐛 | ★ | 15 | C |
| M09a.35 | Tester une propriété : un pytest pour (AB)ᵀ = BᵀAᵀ sur des matrices aléatoires | 🛠️ | ★ | 15 | C |
| M09a.36 | Défi : un système 200 × 200 résolu par ton `solve`, à 1e−8 près de NumPy, en moins d'une seconde | 🏆 | ★★★ | 30 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
