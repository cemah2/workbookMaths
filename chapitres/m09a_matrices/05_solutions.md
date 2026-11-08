# M09a · Matrices et systèmes linéaires — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M09a.Q1 — Formes : ce qui se multiplie et ce qui ne se multiplie pas
1. $(5, 6)$ : $(5, 2) \times (2, 6)$, il reste les dimensions extérieures.
2. **Non** : $\mathbf{A}$ a 2 colonnes et $\mathbf{C}$ a 6 lignes.
3. $(5, 5)$ : $(5, 2) \times (2, 6) \times (6, 5)$.
4. **5** : autant que $\mathbf{A}$ a de lignes.
5. $(6, 2)$ : $(6, 5) \times (5, 2)$.
6. $(800, 15)$ : une ligne par exemple, une colonne par feature. Une colonne contient **une** feature, mesurée sur les 800 exemples.

### M09a.Q2 — Le produit matrice-vecteur, deux lectures
1. $3 \times 2 + 1 \times (-1) = 5$ : le produit scalaire de la ligne 1 avec $\mathbf{x}$.
2. $\mathbf{A}\mathbf{x} = 2\begin{pmatrix} 3 \\ -2 \end{pmatrix} - 1\begin{pmatrix} 1 \\ 4 \end{pmatrix} = \begin{pmatrix} 5 \\ -8 \end{pmatrix}$.
3. $(1, 4)$ : la **colonne 2** de $\mathbf{A}$.
4. $m\,n$ : une multiplication par élément de la matrice.
5. **Vrai** : si $\mathbf{a}_j = 2\mathbf{a}_k$, le vecteur $\mathbf{x}$ qui vaut 2 en position $k$, $-1$ en position $j$ et 0 ailleurs donne $\mathbf{A}\mathbf{x} = 2\mathbf{a}_k - \mathbf{a}_j = \mathbf{0}$.

### M09a.Q3 — Produit matriciel : vrai ou faux
1. **Faux** en général (fiche §3), même pour des matrices carrées ; parfois vrai (avec $\mathbf{I}$, ou deux matrices diagonales).
2. **Vrai** : le produit est associatif.
3. **Faux** : $\mathbf{N} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ n'est pas nulle, et $\mathbf{N}\mathbf{N} = \mathbf{0}$.
4. **Faux** : $(\mathbf{A} + \mathbf{B})^2 = \mathbf{A}^2 + \mathbf{A}\mathbf{B} + \mathbf{B}\mathbf{A} + \mathbf{B}^2$ ; l'identité remarquable ne vaut que si $\mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A}$.
5. **Vrai** : $n\,m$ éléments, chacun un produit scalaire de longueur $p$.
6. **Faux** : le résultat est le même, le coût peut changer énormément (M09a.4 : un facteur de près de 43).

### M09a.Q4 — Hadamard ou produit matriciel ?
1. Le produit de **Hadamard** $\odot$ (sans broadcasting) : il multiplie les éléments de même position.
2. Le produit de **Hadamard** : $a_{ij}b_{ij} = b_{ij}a_{ij}$.
3. `A * B` pour Hadamard, `A @ B` pour le produit matriciel.
4. $\mathbf{I}_2 \odot \mathbf{A}$ garde la diagonale de $\mathbf{A}$ et met des 0 ailleurs ; $\mathbf{I}_2\mathbf{A} = \mathbf{A}$.
5. Hadamard : le masque met à zéro les poids marqués 0 et garde les autres.
6. Le produit matriciel : $\mathbf{X}\mathbf{W}$, une ligne par exemple.

### M09a.Q5 — Les règles de la transposée
1. $(5, 2)$.
2. $\mathbf{A}$.
3. $\mathbf{B}^\top\mathbf{A}^\top$ : l'ordre s'inverse.
4. $\mathbf{C}^\top\mathbf{B}^\top\mathbf{A}^\top$.
5. $(8, 8)$ : $(8, 1000) \times (1000, 8)$, une ligne et une colonne par feature.
6. **Vrai** : $(\mathbf{X}^\top\mathbf{X})^\top = \mathbf{X}^\top(\mathbf{X}^\top)^\top = \mathbf{X}^\top\mathbf{X}$ (M09a.15).

### M09a.Q6 — Combien de solutions ?
1. **Aucune** : deux droites parallèles distinctes ne se coupent pas.
2. **Non** : deux solutions distinctes en donnent une infinité (M09a.17).
3. **Non** : $\mathbf{x} = \mathbf{0}$ est toujours solution.
4. **Exactement une** : $\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$.
5. **Aucune** : la ligne dit $0 = 5$.
6. Une **infinité** : au plus 2 pivots pour 3 inconnues, donc au moins une variable libre.

### M09a.Q7 — Les opérations permises sur les lignes
1. **Oui** : les mêmes équations, dans un autre ordre.
2. **Oui** : on peut revenir en arrière en divisant par $-3$.
3. **Non** : la ligne devient $0 = 0$, l'équation est perdue, et des solutions peuvent apparaître.
4. **Oui** : on revient en arrière en retranchant deux fois la ligne 1.
5. **Non** : ce n'est pas une opération sur l'équation ; $x + y = 2$ deviendrait $2x + 2y = 3$.
6. **Non** : les deux nouvelles lignes sont opposées, l'une est l'autre fois $-1$ : une équation est perdue. Les opérations se font **une par une**.

### M09a.Q8 — Inverse et rang
1. **Non** : l'inverse n'est définie que pour une matrice carrée.
2. **0** : aucun pivot.
3. **4** : le rang est au plus le plus petit des deux nombres de lignes et de colonnes.
4. **1** : la ligne 1 vaut $-2$ fois la ligne 2.
5. $\mathbf{B}^{-1}\mathbf{A}^{-1}$ (M09a.16).
6. **Vrai** (fiche §8).

<a id="rappels"></a>

## 🔁 Rappels

### M09a.R1 — Les systèmes 2 × 2 (R2)
1. $x = 1 + y$, puis $2 + 2y + 3y = 7$ : $y = 1$ et $x = 2$, soit $(2, 1)$.
2. Une **infinité** : la seconde équation est la première multipliée par 2.
3. **Aucune** : la même combinaison $4x + 6y$ devrait valoir 14 et 10.
4. $a \times 1 - 2 \times 3 = 0$ : $a = 6$.
5. En 2, les deux droites sont confondues ; en 3, elles sont parallèles et distinctes.

### M09a.R2 — Produit scalaire et normes (M07)
1. $2 - 4 + 0 = -2$.
2. $\sqrt{4 + 1 + 9} = \sqrt{14} \approx 3{,}742$.
3. $\mathbf{u} - \mathbf{v} = (1, -5, 3)$, et $1 + 25 + 9 = 35$.
4. $-1$ : la deuxième coordonnée de $\mathbf{u}$.
5. Un vecteur $(a, b, 0)$ avec $2a - b = 0$ : par exemple $(1, 2, 0)$ (ou tout multiple non nul).

### M09a.R3 — Moyenne et écart-type empiriques (M02c)
1. $\frac{4 + 8 + 6 + 2}{4} = 5$.
2. Les écarts valent $-1, 3, 1, -3$, leurs carrés $1, 9, 1, 9$ : $\sqrt{\frac{20}{4}} = \sqrt{5} \approx 2{,}236$.
3. $\sqrt{\frac{20}{3}} \approx 2{,}582$.
4. $(-1, 3, 1, -3)$.
5. $\frac{-1}{2{,}236} \approx -0{,}447$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M09a.1 — Un tableau de données vu comme une matrice : forme, lignes, colonnes, moyennes

**Réponses** : a) `[5, 3]` · b) `70` · c) `[2, 1]` · d) `[24, 65, 15]` · e) `[22, 60, 12]` · f) `[3, -5, 6]` · g) `2.2804`.

**Démarche.**
- a) 5 capteurs (lignes), 3 grandeurs (colonnes).
- b) et c) $x_{32}$ : ligne 3, colonne 2, soit 70 ; en Python, `X[2, 1]`.
- e) Les sommes des colonnes valent 110, 300 et 60 : $\boldsymbol{\mu} = (22, 60, 12)$.
- f) $(25, 55, 18) - (22, 60, 12) = (3, -5, 6)$.
- g) Les écarts des températures à 22 valent $0, 3, -3, 2, -2$ ; la somme de leurs carrés, 26 ; $\sqrt{\frac{26}{5}} = \sqrt{5{,}2} \approx 2{,}2804$.

Pour la copie : une ligne est un exemple (un capteur), une colonne une feature (une grandeur mesurée sur tous les capteurs). La moyenne se calcule **par colonne** : chaque ligne perd le même vecteur $\boldsymbol{\mu}$, celui des moyennes des trois grandeurs. Après centrage, chaque colonne a une moyenne nulle.

**Erreurs fréquentes.** La forme $(3, 5)$ ; lire $x_{32}$ comme ligne 2, colonne 3 (18) ; oublier de retirer 1 aux indices en Python ; une moyenne par ligne (`axis=1`) au lieu de par colonne ; $\mathrm{ddof} = 1$ en g) (2,5495).

**Variante.** L'écart-type de l'humidité, avec $\mathrm{ddof} = 0$ ? *Réponse* : les écarts à 60 valent $0, -5, 10, 5, -10$, d'où $\sqrt{\frac{250}{5}} = \sqrt{50} \approx 7{,}0711$.

### Ex M09a.2 — Le produit matrice-vecteur, par les lignes puis par les colonnes

**Réponses** : a) `3` · b) `[13, -3, 2]` · c) `12` · d) `[2, -2, 1]` · e) `[1, 0, 0, 2]` · f) `False` · g) `[1, 1.5]`.

**Démarche.**
- b) Par les lignes : $6 + 1 + 6 + 0 = 13$ ; $2 - 4 - 6 + 5 = -3$ ; $-4 + 0 + 3 + 3 = 2$.
- c) $3 \times 4$ : une multiplication par élément de $\mathbf{A}$.
- d) $\mathbf{A}\mathbf{e}_3 = 0\,\mathbf{a}_1 + 0\,\mathbf{a}_2 + 1\,\mathbf{a}_3 + 0\,\mathbf{a}_4 = \mathbf{a}_3$.
- e) $\mathbf{A}\mathbf{y} = y_1\mathbf{a}_1 + \cdots + y_4\mathbf{a}_4$ : il faut $y_1 = 1$, $y_4 = 2$, et 0 ailleurs.
- f) $\mathbf{A}$ a 4 colonnes : elle ne multiplie que des vecteurs de $\mathbb{R}^4$.
- g) Une prédiction par ligne de $\mathbf{X}$ : $(1 - 1 + 0 + 1,\ -0{,}5 - 3 + 4 + 1) = (1 ;\ 1{,}5)$.

Pour la copie : par les colonnes, $2(3, 1, -2) - (-1, 4, 0) + 3(2, -2, 1) + (0, 5, 3) = (6 + 1 + 6 + 0,\ 2 - 4 - 6 + 5,\ -4 + 0 + 3 + 3) = (13, -3, 2)$ : la même chose. En g), un million d'exemples à 20 features coûtent $2 \times 10^7$ multiplications.

**Erreurs fréquentes.** Une erreur de signe dans un produit scalaire ; donner la ligne 3 en d) ; inverser les coefficients en e) ; oublier le biais, ou l'ajouter une seule fois, en g).

**Variante.** $\mathbf{A}(1, 1, 1, 1)$ ? *Réponse* : la somme des colonnes, $(4, 8, 2)$.

### Ex M09a.3 — Produits matriciels à la main : formes compatibles et calculs

**Réponses** : a) `[2, 2]` · b) `[[5, 9], [-2, 4]]` · c) `[3, 3]` · d) `-2` · e) `False` · f) `[[1, 5, 4], [-1, 4, -1]]` · g) `[[-4, 19], [-6, 0]]`.

**Démarche.**
- b) $(\mathbf{A}\mathbf{B})_{11} = 2 + 1 + 2 = 5$, $(\mathbf{A}\mathbf{B})_{12} = 1 + 0 + 8 = 9$, $(\mathbf{A}\mathbf{B})_{21} = 0 - 3 + 1 = -2$, $(\mathbf{A}\mathbf{B})_{22} = 0 + 0 + 4 = 4$.
- d) La ligne 2 de $\mathbf{B}$, $(-1, 0)$, avec la colonne 3 de $\mathbf{A}$, $(2, 1)$ : $-2$.
- e) $(2, 3) \times (2, 2)$ : les dimensions intérieures, 3 et 2, diffèrent.
- f) $\mathbf{C}\mathbf{A}$ : $(1 + 0,\ -1 + 6,\ 2 + 2)$ et $(-1 + 0,\ 1 + 3,\ -2 + 1)$.
- g) $\begin{pmatrix} 5 & 9 \\ -2 & 4 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 5 - 9 & 10 + 9 \\ -2 - 4 & -4 + 4 \end{pmatrix}$.

Pour la copie : $\mathbf{B}\mathbf{C} = \begin{pmatrix} 1 & 5 \\ -1 & -2 \\ -3 & 6 \end{pmatrix}$, puis $\mathbf{A}(\mathbf{B}\mathbf{C}) = \begin{pmatrix} -4 & 19 \\ -6 & 0 \end{pmatrix}$ : le même résultat que g), par associativité. $\mathbf{A}\mathbf{B}$ est $(2, 2)$ et $\mathbf{B}\mathbf{A}$ est $(3, 3)$ : deux matrices de formes différentes ne peuvent pas être égales.

**Erreurs fréquentes.** Calculer $\mathbf{B}\mathbf{A}$ en b) ; prendre la ligne 2 de $\mathbf{A}$ et la colonne 3 de $\mathbf{B}$ (qui n'existe pas) en d) ; répondre `True` en e) parce que $\mathbf{C}\mathbf{A}$ existe ; mettre $\mathbf{C}$ à gauche en g).

**Variante.** L'élément $(3, 2)$ de $\mathbf{B}\mathbf{C}$ ? *Réponse* : $(1, 4) \cdot (2, 1) = 6$.

### Ex M09a.4 — Le coût d'un produit, et l'ordre des parenthèses dans ABC

**Réponses** : a) `40000` · b) `70000` · c) `3000000` · d) `42.9` · e) `[20, 300]` · f) `23000` · g) `27`.

**Démarche.**
- a) $20 \times 400 \times 5 = 40\,000$.
- b) $\mathbf{A}\mathbf{B}$ a la forme $(20, 5)$ ; $(\mathbf{A}\mathbf{B})\mathbf{C}$ coûte $20 \times 5 \times 300 = 30\,000$ de plus.
- c) $\mathbf{B}\mathbf{C}$ coûte $400 \times 5 \times 300 = 600\,000$ et a la forme $(400, 300)$ ; $\mathbf{A}(\mathbf{B}\mathbf{C})$ coûte $20 \times 400 \times 300 = 2\,400\,000$ de plus.
- d) $\frac{3\,000\,000}{70\,000} \approx 42{,}9$ : le rapport des deux coûts.
- f) $\mathbf{A}(\mathbf{B}(\mathbf{C}\mathbf{D}))$ : $\mathbf{C}\mathbf{D}$, de forme $(5, 2)$, coûte $5 \times 300 \times 2 = 3\,000$ ; puis $\mathbf{B}(\mathbf{C}\mathbf{D})$, de forme $(400, 2)$, $400 \times 5 \times 2 = 4\,000$ ; puis $20 \times 400 \times 2 = 16\,000$.
- g) $(3n)^3 = 27\,n^3$.

Pour la copie : la règle simple est d'éviter de fabriquer une grande matrice intermédiaire ; ici, $\mathbf{B}\mathbf{C}$, de forme $(400, 300)$, est énorme, alors que $\mathbf{A}\mathbf{B}$, $(20, 5)$, est minuscule. En f), $\mathbf{D}$ n'a que 2 colonnes : en partant de la droite, chaque résultat intermédiaire n'a que 2 colonnes. $((\mathbf{A}\mathbf{B})\mathbf{C})\mathbf{D}$ coûte $40\,000 + 30\,000 + 12\,000 = 82\,000$, et $(\mathbf{A}\mathbf{B})(\mathbf{C}\mathbf{D})$ coûte $43\,200$. Le résultat est le même dans tous les ordres : le produit est associatif.

**Erreurs fréquentes.** Compter $n \times m$ (le nombre d'éléments du résultat) au lieu de $n\,p\,m$ ; oublier le second produit ; inverser le rapport en d) (0,023), ou donner le surcoût relatif (41,9) ; calculer de gauche à droite en f) (82 000) ; répondre 9 en g).

**Variante.** Avec $\mathbf{C}$ de forme $(5, 3000)$ ? *Réponse* : $(\mathbf{A}\mathbf{B})\mathbf{C}$ coûte $40\,000 + 300\,000 = 340\,000$, $\mathbf{A}(\mathbf{B}\mathbf{C})$ coûte $6\,000\,000 + 24\,000\,000 = 30\,000\,000$, 88 fois plus.

### Ex M09a.5 — Une couche dense Z = XW + b à la main : deux exemples, trois entrées, deux sorties

**Réponses** : a) `[3, 2]` · b) `[[3, 5.5], [-2, 7.5]]` · c) `-2` · d) `[[3, 5.5], [0, 7.5]]` · e) `8` · f) `[2, 3]` · g) `12`.

**Démarche.**
- b) $\mathbf{X}\mathbf{W} = \begin{pmatrix} 2 + 0 + 2 & -1 + 0 + 6 \\ -2 + 0 + 1 & 1 + 3 + 3 \end{pmatrix} = \begin{pmatrix} 4 & 5 \\ -1 & 7 \end{pmatrix}$, puis on ajoute $(-1 ;\ 0{,}5)$ à **chaque ligne**.
- c) Ligne 2 (l'exemple 2), colonne 1 (le neurone 1).
- d) Seul $-2$ est négatif : il devient 0.
- e) $3 \times 2 = 6$ poids et 2 biais.
- f) PyTorch range les poids de `nn.Linear` en $(n_{\text{out}}, n_{\text{in}})$ et calcule $\mathbf{X}\mathbf{W}^\top + \mathbf{b}$.
- g) $2 \times 3 \times 2$.

Pour la copie : la colonne 2 de $\mathbf{W}$, $(-1, 1, 3)$, contient les poids du neurone 2. Le biais est le même pour tous les exemples : un nombre par neurone, ajouté à chaque ligne (le broadcasting). Pour un batch de 128 exemples, $\mathbf{Z}$ a la forme $(128, 2)$ ; $\mathbf{W}$ et $\mathbf{b}$ ne changent pas.

**Erreurs fréquentes.** Calculer $\mathbf{W}\mathbf{X}$ (il existe ici, de forme $(3, 3)$, mais ne veut rien dire : ni une ligne par exemple, ni une colonne par neurone) ; ajouter $b_1$ à la ligne 1 et $b_2$ à la ligne 2 ; oublier les biais en e) ; confondre la forme de NumPy et celle de PyTorch en f).

**Variante.** Un troisième exemple $(0, 1, -1)$ : sa ligne de $\operatorname{ReLU}(\mathbf{Z})$ ? *Réponse* : $\mathbf{z} = (-1 - 1,\ -2 + 0{,}5) = (-2 ;\ -1{,}5)$, d'où $(0, 0)$ : aucun des deux neurones ne s'active.

### Ex M09a.6 — Un embedding : une ligne one-hot fois une matrice

**Réponses** : a) `[0, 0, 0, 1, 0]` · b) `[0.5, 1.5, -0.8]` · c) `15` · d) `15` · e) `[0.9, -0.2, 0.4]` · f) `[-0.7, 0.2667, 0.5333]`.

**Démarche.**
- b) La ligne $(0, 0, 0, 1, 0)$ fois $\mathbf{E}$ est la combinaison des lignes de $\mathbf{E}$ de coefficients 0, 0, 0, 1, 0 : la ligne 4.
- c) et d) $5 \times 3 = 15$ nombres ; le produit $(1, 5) \times (5, 3)$ coûte $1 \times 5 \times 3 = 15$ multiplications, dont 12 par 0.
- e) La somme des lignes 2 et 5.
- f) $\frac{1}{3}\big((0{,}1 ;\ -0{,}4 ;\ 1{,}2) + 2(-1{,}1 ;\ 0{,}6 ;\ 0{,}2)\big) = \frac{1}{3}(-2{,}1 ;\ 0{,}8 ;\ 1{,}6)$.

Pour la copie : en pratique, on lit la ligne (`E[3]` en Python) : sélectionner coûte zéro multiplication, alors que le produit en ferait autant qu'il y a de nombres dans la table (des dizaines de millions, voire des milliards, pour un grand vocabulaire). La ligne de comptage $(1, 0, 2, 0, 0)$ compte les occurrences de chaque mot de la phrase : c'est un **sac de mots**.

**Erreurs fréquentes.** Numéroter les mots à partir de 0 (a, b) ; additionner les lignes 1 et 4 en e) ; oublier le coefficient 2 ou la division par 3 en f).

**Variante.** La moyenne des embeddings de « mot 2, mot 5 » ? *Réponse* : $\frac{1}{2}\big((0{,}9 ;\ 0 ;\ -0{,}3) + (0 ;\ -0{,}2 ;\ 0{,}7)\big) = (0{,}45 ;\ -0{,}1 ;\ 0{,}2)$.

### Ex M09a.7 — Transposées de produits, et la matrice symétrique XᵀX

**Réponses** : a) `[3, 3]` · b) `[[2, -1, 5], [8, 5, -7], [0, -1, 3]]` · c) `[[6, 2], [-4, 4]]` · d) `False` · e) `[[6, 1, 1], [1, 6, 0], [1, 0, 6]]` · f) `[4, 4]` · g) `0`.

**Démarche.**
- b) $\mathbf{A}\mathbf{B} = \begin{pmatrix} 2 & 8 & 0 \\ -1 & 5 & -1 \\ 5 & -7 & 3 \end{pmatrix}$, dont on échange lignes et colonnes.
- c) $\mathbf{B}\mathbf{A} = \begin{pmatrix} 2 + 4 + 0 & 0 - 4 + 0 \\ 4 - 1 - 1 & 0 + 1 + 3 \end{pmatrix} = \begin{pmatrix} 6 & -4 \\ 2 & 4 \end{pmatrix}$, puis sa transposée.
- d) $\mathbf{A}^\top\mathbf{B}^\top$ a la forme $(2, 3) \times (3, 2) = (2, 2)$, et $(\mathbf{A}\mathbf{B})^\top$ la forme $(3, 3)$ : la bonne règle est $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$. (D'ailleurs $\mathbf{A}^\top\mathbf{B}^\top = (\mathbf{B}\mathbf{A})^\top$, la réponse c).)
- e) L'élément $(i, j)$ de $\mathbf{X}^\top\mathbf{X}$ est le produit scalaire des colonnes $i$ et $j$ de $\mathbf{X}$ : les colonnes $(1, 0, 2, 1)$, $(-1, 2, 1, 0)$, $(2, 1, 0, -1)$ ont chacune un carré de norme 6, et leurs produits scalaires valent 1, 1 et 0.
- g) Le produit scalaire des lignes 1 et 2 : $0 - 2 + 2 = 0$.

Pour la copie : $\mathbf{B}^\top\mathbf{A}^\top$, calculé directement, redonne b). La diagonale de $\mathbf{X}^\top\mathbf{X}$ contient la somme des carrés de chaque feature ; un zéro hors de la diagonale dit que deux features sont orthogonales (ici, les features 2 et 3). En g), les exemples 1 et 2 sont orthogonaux.

**Erreurs fréquentes.** Calculer $\mathbf{X}\mathbf{X}^\top$, de forme $(4, 4)$, en e) ; répondre `True` en d) sans regarder les formes ; donner $\mathbf{B}\mathbf{A}$ sans le transposer en c).

**Variante.** La somme des nombres de la diagonale de $\mathbf{X}^\top\mathbf{X}$, et la somme des carrés de tous les nombres de $\mathbf{X}$ ? *Réponse* : 18 et 18 : chaque nombre de la diagonale est la somme des carrés d'une colonne.

### Ex M09a.8 — Le pivot de Gauss sur un système 3 × 3 à solution unique

**Réponses** : a) `2` · b) `[0, 3, -5, -21]` · c) `[0, 5, -5, -25]` · d) `"5/3"` · e) `3` · f) `[1, -2, 3]`.

**Démarche.** Après l'échange, $L_1 = (1, -1, 2 \mid 9)$, $L_2 = (2, 1, -1 \mid -3)$, $L_3 = (3, 2, 1 \mid 2)$.
- b) $L_2 - 2L_1 = (0, 3, -5 \mid -21)$ ; c) $L_3 - 3L_1 = (0, 5, -5 \mid -25)$.
- d) Pour annuler le 5 avec le pivot 3 : $\frac{5}{3}$. La troisième ligne devient $(0, 0, -5 + \frac{25}{3} \mid -25 + 35) = (0, 0, \frac{10}{3} \mid 10)$.
- e) $z = 10 \times \frac{3}{10} = 3$.
- f) $3y - 15 = -21$, $y = -2$ ; $x + 2 + 6 = 9$, $x = 1$.

Pour la copie : la forme échelonnée est $\left(\begin{array}{ccc|c} 1 & -1 & 2 & 9 \\ 0 & 3 & -5 & -21 \\ 0 & 0 & \frac{10}{3} & 10 \end{array}\right)$, la forme réduite $\left(\begin{array}{ccc|c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & -2 \\ 0 & 0 & 1 & 3 \end{array}\right)$. Vérification : $2 - 2 - 3 = -3$, $1 + 2 + 6 = 9$, $3 - 4 + 3 = 2$. L'échange ne change pas les solutions : ce sont les mêmes équations, écrites dans un autre ordre.

**Erreurs fréquentes.** Oublier le second membre dans une opération ; ajouter au lieu de retrancher ; prendre $\frac{3}{5}$ en d) ; donner la solution dans l'ordre $(z, y, x)$.

**Variante.** Mêmes coefficients, seconds membres $(5, 0, 5)$ ? *Réponse* : $(2, 0, -1)$.

### Ex M09a.9 — Un système sans solution, un système à une infinité de solutions

**Réponses** : a) `[0, 0, 0, 1]` · b) `0` · c) `[[1, 0, -7, -3], [0, 1, 3, 2], [0, 0, 0, 0]]` · d) `1` · e) `[-3, 2, 0]` · f) `[4, -1, 1]` · g) `5`.

**Démarche.**
- a) $L_2 - 2L_1 = (0, 1, 3 \mid 2)$, $L_3 - 3L_1 = (0, 1, 3 \mid 3)$, puis $L_3 - L_2 = (0, 0, 0 \mid 1)$.
- b) La dernière ligne dit $0 = 1$ : aucune solution.
- c) Pour $(S_2)$, la troisième ligne devient $(0, 0, 0 \mid 0)$ ; puis $L_1 - 2L_2 = (1, 0, -7 \mid -3)$.
- d) Deux pivots (colonnes 1 et 2) pour trois inconnues : $z$ est libre.
- e) et f) $x = -3 + 7z$ et $y = 2 - 3z$.
- g) La troisième ligne des coefficients est la somme des deux premières : le système n'a de solution que si son second membre est aussi la somme, $1 + 4 = 5$.

Pour la copie : la solution générale de $(S_2)$ est $(-3, 2, 0) + t\,(7, -3, 1)$, $t \in \mathbb{R}$. La différence $(4, -1, 1) - (-3, 2, 0) = (7, -3, 1)$ vérifie $7 - 6 - 1 = 0$, $14 - 15 + 1 = 0$ et $21 - 21 = 0$ : elle résout le système homogène (M09a.17).

**Erreurs fréquentes.** Oublier le second membre dans les opérations (a : une ligne nulle) ; s'arrêter à la forme échelonnée en c) ; des signes faux en passant les termes en $z$ de l'autre côté (e, f).

**Variante.** Si le second membre de la première équation passe à 2, pour quelle valeur du troisième le système a-t-il des solutions ? *Réponse* : $2 + 4 = 6$.

### Ex M09a.10 — La forme échelonnée réduite d'une matrice 3 × 4 et la solution générale

**Réponses** : a) `[[1, 0, 3, 3], [0, 1, 1, 2], [0, 0, 0, 0]]` · b) `[1, 2]` · c) `2` · d) `[3, 2, 0]` · e) `[-3, 0, 2]` · f) `[-3, -1, 1]` · g) `True`.

**Démarche.**
- a) $L_2 - 2L_1 = (0, 1, 1 \mid 2)$ ; $L_3 - L_2 = (0, 0, 0 \mid 0)$ ; $L_1 + L_2 = (1, 0, 3 \mid 3)$.
- b) et c) Les pivots sont dans les colonnes 1 et 2 : rang 2.
- d) et e) $x = 3 - 3z$, $y = 2 - z$.
- f) Le système homogène : $x = -3z$, $y = -z$.
- g) $x = 3 - 3 \times (-1) = 6$ et $y = 2 - (-1) = 3$ : oui.

Pour la copie : la solution générale est $(3, 2, 0) + t\,(-3, -1, 1)$. La variable $z$ est libre : sa colonne n'a pas de pivot, et on peut lui donner n'importe quelle valeur.

**Erreurs fréquentes.** Oublier d'annuler le $-1$ au-dessus du second pivot (a) ; numéroter les colonnes à partir de 0 (b) ; prendre le second membre dans le système homogène (f : $(0, 1, 1)$).

**Variante.** La solution telle que $x = 0$ ? *Réponse* : $z = 1$, d'où $(0, 1, 1)$.

### Ex M09a.11 — L'inverse d'une matrice 2 × 2, par la formule, puis vérifiée

**Réponses** : a) `4` · b) `[[1.25, -0.75], [-0.5, 0.5]]` · c) `[3, 1]` · d) `[[0, 1], [1, 1]]` · e) `[[0.625, -0.375], [-0.25, 0.25]]` · f) `[[1.25, -0.5], [-0.75, 0.5]]` · g) `[[31, -21], [-14, 10]]`.

**Démarche.**
- a) $2 \times 5 - 3 \times 2 = 4$.
- b) $\frac{1}{4}\begin{pmatrix} 5 & -3 \\ -2 & 2 \end{pmatrix}$ : on échange $a$ et $d$, on change le signe de $b$ et de $c$, on divise par $ad - bc$.
- c) $\mathbf{A}^{-1}\begin{pmatrix} 9 \\ 11 \end{pmatrix} = \begin{pmatrix} 11{,}25 - 8{,}25 \\ -4{,}5 + 5{,}5 \end{pmatrix}$.
- d) On multiplie $\mathbf{A}\mathbf{X} = \mathbf{C}$ **à gauche** par $\mathbf{A}^{-1}$ : $\mathbf{X} = \mathbf{A}^{-1}\mathbf{C} = \frac{1}{4}\begin{pmatrix} 15 - 15 & 25 - 21 \\ -6 + 10 & -10 + 14 \end{pmatrix}$.
- e) $(2\mathbf{A})^{-1} = \frac{1}{2}\mathbf{A}^{-1}$, car $(2\mathbf{A})(\frac{1}{2}\mathbf{A}^{-1}) = \mathbf{I}$.
- f) $(\mathbf{A}^\top)^{-1} = (\mathbf{A}^{-1})^\top$ (M09a.16).
- g) $\mathbf{A}^2 = \begin{pmatrix} 10 & 21 \\ 14 & 31 \end{pmatrix}$, et $ad - bc = 310 - 294 = 16$ : $(\mathbf{A}^2)^{-1} = \frac{1}{16}\begin{pmatrix} 31 & -21 \\ -14 & 10 \end{pmatrix}$.

Pour la copie : $\mathbf{A}\mathbf{A}^{-1} = \frac{1}{4}\begin{pmatrix} 10 - 6 & -6 + 6 \\ 10 - 10 & -6 + 10 \end{pmatrix} = \mathbf{I}$, et de même $\mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$. En d), $\mathbf{C}\mathbf{A}^{-1}$ résoudrait $\mathbf{X}\mathbf{A} = \mathbf{C}$ : le produit n'est pas commutatif, et l'inverse se place du même côté que $\mathbf{A}$. En g), $(\mathbf{A}\mathbf{A})^{-1} = \mathbf{A}^{-1}\mathbf{A}^{-1}$ par la règle de l'inverse d'un produit, et le 16 est $4^2$ : le nombre $ad - bc$ de $\mathbf{A}^2$ est le carré de celui de $\mathbf{A}$ (le déterminant d'un produit est le produit des déterminants, M12c).

**Erreurs fréquentes.** $ad + bc$ (16) ; oublier de diviser par $ad - bc$, ou de changer les signes ; $\mathbf{C}\mathbf{A}^{-1}$ en d) ; $2\mathbf{A}^{-1}$ en e) ; oublier de transposer en f) ; transposer en g).

**Variante.** L'inverse de $\begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$ ? *Réponse* : $ad - bc = 1$, d'où $\begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix}$.

### Ex M09a.12 — L'inverse d'une matrice 3 × 3 par Gauss-Jordan

**Réponses** : a) `[[-2, 1, 3], [2, -1, -2], [-1, 1, 1]]` · b) `[4, -2, 1]` · c) `[1, -1, 1]` · d) `[-2, 2, -1]` · e) `False`.

**Démarche.** Sur $[\mathbf{A} \mid \mathbf{I}_3]$ :
- $L_3 \leftarrow L_3 - L_1$ : $(0, -1, -1 \mid -1, 0, 1)$ ;
- $L_1 \leftarrow L_1 - 2L_2$ : $(1, 0, -3 \mid 1, -2, 0)$ ; $L_3 \leftarrow L_3 + L_2$ : $(0, 0, 1 \mid -1, 1, 1)$ ;
- $L_1 \leftarrow L_1 + 3L_3$ : $(1, 0, 0 \mid -2, 1, 3)$ ; $L_2 \leftarrow L_2 - 2L_3$ : $(0, 1, 0 \mid 2, -1, -2)$.

b) $\mathbf{A}^{-1}(1, 0, 2) = (-2 + 6,\ 2 - 4,\ -1 + 2)$. c) $\mathbf{A}^{-1}\mathbf{e}_2$ est la colonne 2 de $\mathbf{A}^{-1}$. d) La première ligne de $(\mathbf{A}^{-1})^\top$ est la première colonne de $\mathbf{A}^{-1}$. e) La troisième ligne est la somme des deux premières.

Pour la copie : c) $\mathbf{A}^{-1}\mathbf{e}_2$ sélectionne la colonne 2 (fiche §2) ; c'est pourquoi réduire $[\mathbf{A} \mid \mathbf{I}]$ résout d'un coup les trois systèmes $\mathbf{A}\mathbf{x} = \mathbf{e}_j$. Pour la matrice $\mathbf{B}$ de e), la réduction fait apparaître une ligne nulle à gauche : on ne peut pas obtenir $\mathbf{I}_3$, et $\mathbf{B}$ n'a pas d'inverse.

**Erreurs fréquentes.** Une opération appliquée seulement à la moitié gauche ; transposer le résultat ; donner la ligne 2 de $\mathbf{A}^{-1}$ en c).

**Variante.** La solution de $\mathbf{A}\mathbf{x} = (0, 0, 1)$ ? *Réponse* : la colonne 3 de $\mathbf{A}^{-1}$, $(3, -2, 1)$.

### Ex M09a.13 — Le rang de quatre matrices, et les colonnes redondantes

**Réponses** : a) `1` · b) `2` · c) `2` · d) `3` · e) `[2, -1]` · f) `False` · g) `2`.

**Démarche.**
- a) Les lignes 2 et 3 sont des multiples de la ligne 1 : un pivot.
- b) et e) $2\,(1, 0, 1) - (0, 1, 1) = (2, -1, 1)$ : la colonne 3 combine les deux premières. Deux pivots.
- c) Les colonnes 1 et 2 ne sont pas proportionnelles ; les colonnes 3 et 4 les combinent : rang 2.
- d) Les pivots sont sur la diagonale, non nuls : 3.
- f) Une matrice carrée de taille 3 et de rang 2 n'est pas inversible.
- g) Le rang de $\mathbf{M}^\top$ est celui de $\mathbf{M}$.

Pour la copie : $(0, 1, -2) = (2, 1, 0) - 2\,(1, 0, 1)$ et $(3, 1, 1) = (2, 1, 0) + (1, 0, 1)$. $\mathbf{M}_4$ est déjà échelonnée : on compte ses trois pivots sans calcul.

**Erreurs fréquentes.** Compter les lignes non nulles avant l'élimination ; croire que le rang de $\mathbf{M}_3$, qui a 4 colonnes, peut dépasser 3 ; échanger $a$ et $b$ en e).

**Variante.** Le rang de $\mathbf{M}_2$ si sa dernière ligne devient $(1, 1, 2)$ ? *Réponse* : 3 ; la colonne 3, $(2, -1, 2)$, ne combine plus les deux premières.

### Ex M09a.14 — Mettre un problème en système : trois engrais pour trois nutriments

**Réponses** : a) `[[200, 100, 0], [100, 0, 150], [0, 200, 100]]` · b) `[4, 3, 2]` · c) `9` · d) `"16/7"` · e) `[7, -3]`.

**Démarche.**
- a) Une ligne par nutriment (N, P, K), une colonne par engrais : la colonne $j$ est ce qu'apporte un kilogramme de l'engrais $j$. C'est la transposée du tableau de l'énoncé.
- b) Le pivot de Gauss (ou une substitution) donne $(4, 3, 2)$ ; vérification : $800 + 300 = 1\,100$, $400 + 300 = 700$, $600 + 200 = 800$.
- d) $y = 11 - 2x$ et $x = 7 - 1{,}5z$ ; la troisième équation, $2y + z = 10$, donne $4x - z = 12$, puis $28 - 7z = 12$ : $z = \frac{16}{7}$.
- e) $100x = 700$, puis $200 \times 7 + 100y = 1\,100$.

Pour la copie : $y = -3$ est une masse négative ; sans l'engrais 3, il est impossible d'avoir exactement les trois apports. Une matrice $\mathbf{A}$ singulière aurait voulu dire qu'un engrais est un mélange des deux autres : selon les besoins, aucun mélange exact, ou une infinité.

**Erreurs fréquentes.** Ranger les engrais en lignes (a) ; oublier une équation en d) ; garder une masse négative sans le remarquer (e).

**Variante.** Pour 1 100 g d'azote, 450 g de phosphore et 1 100 g de potassium ? *Réponse* : $(3, 5, 1)$, 9 kg en tout.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M09a.15 — (AB)ᵀ = BᵀAᵀ, coefficient par coefficient

**Réponse modèle.**
1. $\mathbf{A}\mathbf{B}$ a la forme $(n, m)$, donc $(\mathbf{A}\mathbf{B})^\top$ la forme $(m, n)$. $\mathbf{B}^\top$ a la forme $(m, p)$ et $\mathbf{A}^\top$ la forme $(p, n)$ : leur produit existe et a la forme $(m, n)$.
2. $\big((\mathbf{A}\mathbf{B})^\top\big)_{ij} = (\mathbf{A}\mathbf{B})_{ji} = \sum_{k=1}^{p} a_{jk}\,b_{ki}$.
3. $(\mathbf{B}^\top\mathbf{A}^\top)_{ij} = \sum_{k=1}^{p} (\mathbf{B}^\top)_{ik}\,(\mathbf{A}^\top)_{kj} = \sum_{k=1}^{p} b_{ki}\,a_{jk}$.
4. Les deux sommes ont les mêmes termes (le produit de deux nombres est commutatif). Les deux matrices ont la même forme et les mêmes éléments : $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$.
5. $(\mathbf{A}\mathbf{B}\mathbf{C})^\top = \big((\mathbf{A}\mathbf{B})\mathbf{C}\big)^\top = \mathbf{C}^\top(\mathbf{A}\mathbf{B})^\top = \mathbf{C}^\top\mathbf{B}^\top\mathbf{A}^\top$, en appliquant deux fois la règle.
6. $(\mathbf{X}^\top\mathbf{X})^\top = \mathbf{X}^\top(\mathbf{X}^\top)^\top = \mathbf{X}^\top\mathbf{X}$ : la matrice est égale à sa transposée.

**Grille.** (1) les deux formes, avec la condition d'existence de $\mathbf{B}^\top\mathbf{A}^\top$ ; (2) l'échange des indices $i$ et $j$ **avant** d'écrire la somme ; (3) le retour aux éléments de $\mathbf{A}$ et de $\mathbf{B}$ ; (4) la conclusion « même forme et mêmes éléments » ; (5) l'associativité, puis la règle deux fois ; (6) $(\mathbf{X}^\top)^\top = \mathbf{X}$.

### Ex M09a.16 — L'inverse est unique, et (AB)⁻¹ = B⁻¹A⁻¹

**Réponse modèle.**
1. $\mathbf{B} = \mathbf{B}\mathbf{I} = \mathbf{B}(\mathbf{A}\mathbf{C}) = (\mathbf{B}\mathbf{A})\mathbf{C} = \mathbf{I}\mathbf{C} = \mathbf{C}$.
2. $(\mathbf{A}\mathbf{B})(\mathbf{B}^{-1}\mathbf{A}^{-1}) = \mathbf{A}(\mathbf{B}\mathbf{B}^{-1})\mathbf{A}^{-1} = \mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$, et $(\mathbf{B}^{-1}\mathbf{A}^{-1})(\mathbf{A}\mathbf{B}) = \mathbf{B}^{-1}(\mathbf{A}^{-1}\mathbf{A})\mathbf{B} = \mathbf{B}^{-1}\mathbf{B} = \mathbf{I}$. Par 1, c'est **l'**inverse de $\mathbf{A}\mathbf{B}$.
3. Par M09a.15, $\mathbf{A}^\top(\mathbf{A}^{-1})^\top = (\mathbf{A}^{-1}\mathbf{A})^\top = \mathbf{I}^\top = \mathbf{I}$, et $(\mathbf{A}^{-1})^\top\mathbf{A}^\top = (\mathbf{A}\mathbf{A}^{-1})^\top = \mathbf{I}$.
4. On multiplie à gauche par $\mathbf{A}^{-1}$ : $\mathbf{A}^{-1}\mathbf{A}\mathbf{B} = \mathbf{A}^{-1}\mathbf{A}\mathbf{C}$, soit $\mathbf{B} = \mathbf{C}$.
5. $\mathbf{A} = \begin{pmatrix} 1 & 3 \\ 2 & 6 \end{pmatrix}$, $\mathbf{B} = \mathbf{0}$ et $\mathbf{C} = \begin{pmatrix} 3 & 6 \\ -1 & -2 \end{pmatrix}$ : $\mathbf{A}\mathbf{C} = \mathbf{0} = \mathbf{A}\mathbf{B}$. Pas de contradiction : $\mathbf{A}$ n'est pas inversible (ses colonnes sont proportionnelles), et la question 4 suppose qu'elle l'est. Sans inverse, on ne peut pas « simplifier » par $\mathbf{A}$.

**Grille.** (1) la chaîne d'égalités, avec l'associativité citée ; (2) **les deux** produits, et le renvoi à l'unicité ; (3) l'usage de M09a.15 et de $\mathbf{I}^\top = \mathbf{I}$, dans les deux sens ; (4) la multiplication **à gauche** (à droite, $\mathbf{A}\mathbf{B}\mathbf{A}^{-1}$ ne se simplifie pas) ; (5) un exemple vérifié par le calcul, et l'hypothèse manquante nommée. D'autres exemples sont justes.

### Ex M09a.17 — Deux solutions distinctes entraînent une infinité de solutions

**Réponse modèle.**
1. $\mathbf{A}\mathbf{d} = \mathbf{A}\mathbf{y} - \mathbf{A}\mathbf{x} = \mathbf{b} - \mathbf{b} = \mathbf{0}$ (le produit est distributif).
2. $\mathbf{A}(\mathbf{x} + t\,\mathbf{d}) = \mathbf{A}\mathbf{x} + t\,\mathbf{A}\mathbf{d} = \mathbf{b} + \mathbf{0} = \mathbf{b}$.
3. Si $t \ne t'$, $(\mathbf{x} + t\,\mathbf{d}) - (\mathbf{x} + t'\,\mathbf{d}) = (t - t')\,\mathbf{d} \ne \mathbf{0}$, car $t - t' \ne 0$ et $\mathbf{d} \ne \mathbf{0}$. Il y a autant de solutions que de réels $t$ : une infinité. Un système linéaire a donc 0, 1 ou une infinité de solutions, jamais exactement 2.
4. Si $\mathbf{y}$ est une solution, $\mathbf{h} = \mathbf{y} - \mathbf{x}$ vérifie $\mathbf{A}\mathbf{h} = \mathbf{0}$ (question 1) et $\mathbf{y} = \mathbf{x} + \mathbf{h}$. Réciproquement, si $\mathbf{A}\mathbf{h} = \mathbf{0}$, $\mathbf{A}(\mathbf{x} + \mathbf{h}) = \mathbf{b} + \mathbf{0} = \mathbf{b}$.
5. Si $\mathbf{x}$ et $\mathbf{y}$ sont deux solutions, $\mathbf{y} - \mathbf{x}$ résout le système homogène, donc vaut $\mathbf{0}$ : $\mathbf{y} = \mathbf{x}$.

**Grille.** (1) la distributivité ; (2) le calcul pour un $t$ quelconque ; (3) l'argument « $t - t' \ne 0$ et $\mathbf{d} \ne \mathbf{0}$ », et la conclusion sur les trois cas ; (4) **les deux** sens ; (5) la conclusion « au plus une », qui n'affirme pas l'existence.

### Ex M09a.18 — Une matrice dont une colonne combine les autres n'est pas inversible

**Réponse modèle.**
1. $\mathbf{c} = (\lambda_1, \ldots, \lambda_{n-1}, -1)$ : par la lecture en colonnes, $\mathbf{A}\mathbf{c} = \lambda_1\mathbf{a}_1 + \cdots + \lambda_{n-1}\mathbf{a}_{n-1} - \mathbf{a}_n = \mathbf{0}$, et $\mathbf{c} \ne \mathbf{0}$ (sa dernière coordonnée vaut $-1$).
2. Si $\mathbf{A}$ avait une inverse, $\mathbf{c} = \mathbf{A}^{-1}\mathbf{A}\mathbf{c} = \mathbf{A}^{-1}\mathbf{0} = \mathbf{0}$ : contradiction.
3. Si le système a une solution $\mathbf{x}$, alors $\mathbf{x} + t\,\mathbf{c}$ en est une pour tout $t$ (M09a.17, avec $\mathbf{A}\mathbf{c} = \mathbf{0}$), et ces solutions sont distinctes : une infinité. Sinon, aucune.
4. Pour $\mathbf{M}_2$, la colonne 3 vaut $2\mathbf{a}_1 - \mathbf{a}_2$ : $\mathbf{c} = (2, -1, -1)$. Ligne par ligne : $2 - 0 - 2 = 0$, $0 - 1 + 1 = 0$, $2 - 1 - 1 = 0$.
5. Les colonnes du one-hot ont pour somme la colonne de 1 : avec $\mathbf{c} = (1, -1, \ldots, -1)$ (1 pour la colonne de 1, $-1$ pour chaque colonne du one-hot), $\mathbf{X}\mathbf{c} = \mathbf{0}$, donc $\mathbf{X}^\top\mathbf{X}\mathbf{c} = \mathbf{X}^\top\mathbf{0} = \mathbf{0}$ avec $\mathbf{c} \ne \mathbf{0}$. Par l'argument de la question 2, la matrice carrée $\mathbf{X}^\top\mathbf{X}$ n'est pas inversible. On retire donc une catégorie du one-hot quand le modèle a déjà une colonne de 1.

**Grille.** (1) un vecteur explicite, non nul, et la lecture en colonnes citée ; (2) un raisonnement par l'absurde complet ; (3) les deux cas, et l'appui sur M09a.17 ; (4) le vecteur et la vérification des trois lignes ; (5) la relation entre les colonnes, le calcul de $\mathbf{X}^\top\mathbf{X}\mathbf{c}$, et la conclusion.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M09a.19 — Pont : une passe avant à deux couches, deux produits matriciels et leurs formes

**Réponses** : a) `[64, 5]` · b) `[64, 2]` · c) `32` · d) `1600` · e) `[2, 0, 0]` · f) `2.5` · g) `[[-1], [0]]`.

**Démarche.**
- a) et b) $(64, 3) \times (3, 5) = (64, 5)$, puis $(64, 5) \times (5, 2) = (64, 2)$.
- c) $3 \times 5 + 5$ pour la couche cachée, $5 \times 2 + 2$ pour la sortie.
- d) $64 \times 3 \times 5 + 64 \times 5 \times 2 = 960 + 640$.
- e) $\mathbf{x}\mathbf{W}_1 = (1, 0, 2) - (-1, 1, 1) = (2, -1, 1)$ ; plus $\mathbf{b}_1$, $(2 ;\ -0{,}5 ;\ 0)$ ; puis ReLU.
- f) $2 \times 1 + 0 + 0 + 0{,}5$.
- g) $(2, 3) \times (3, 1) \to (2, 1)$ : $1 \times 1 + 0 \times 2 + 2 \times (-1) = -1$ et $-1 \times 1 + 1 \times 2 + 1 \times (-1) = 0$.

Pour la copie : $\mathbf{b}_1\mathbf{W}_2 + b_2 = 0 + 1 + 1 + 0{,}5 = 2{,}5$. Sans ReLU, $\mathbf{h} = (2 ;\ -0{,}5 ;\ 0)$ et $y = 2 - 1 + 0 + 0{,}5 = 1{,}5$ ; et $\mathbf{x}(\mathbf{W}_1\mathbf{W}_2) + (\mathbf{b}_1\mathbf{W}_2 + b_2) = (1 \times (-1) + (-1) \times 0) + 2{,}5 = 1{,}5$ : la même chose. En développant, $(\mathbf{x}\mathbf{W}_1 + \mathbf{b}_1)\mathbf{W}_2 + b_2 = \mathbf{x}(\mathbf{W}_1\mathbf{W}_2) + (\mathbf{b}_1\mathbf{W}_2 + b_2)$, par distributivité et associativité du produit.

**Erreurs fréquentes.** Oublier les biais en c) ; compter les multiplications d'un seul exemple en d) (25) ; ajouter le biais après ReLU en e) ; oublier ReLU (1,5) ou $b_2$ (2) en f) ; donner $\mathbf{W}_1\mathbf{W}_2$ en ligne en g).

**Variante.** La sortie pour l'exemple $(0, 2)$ ? *Réponse* : $\mathbf{x}\mathbf{W}_1 + \mathbf{b}_1 = (-2 ;\ 2{,}5 ;\ 1)$, $\mathbf{h} = (0 ;\ 2{,}5 ;\ 1)$, et $y = 5 - 1 + 0{,}5 = 4{,}5$.

### Ex M09a.20 — Pont : centrer et réduire un tableau en écriture matricielle

**Réponses** : a) `[4, 20]` · b) `[3, 2]` · c) `[[-2, -10], [0, 10], [2, 0]]` · d) `[0.6124, 0.1225]` · e) `[-1.225, -1.225]` · f) `[[2.6667, 6.6667], [6.6667, 66.6667]]` · g) `0.5`.

**Démarche.**
- b) $\mathbf{1}\boldsymbol{\mu}^\top$ : $(3, 1) \times (1, 2) = (3, 2)$, chaque ligne vaut $\boldsymbol{\mu}^\top$.
- d) $\sigma_1 = \sqrt{\frac{4 + 0 + 4}{3}} = \sqrt{\frac{8}{3}} \approx 1{,}633$ et $\sigma_2 = \sqrt{\frac{100 + 100 + 0}{3}} \approx 8{,}165$ ; $\mathbf{D}^{-1}$ a pour diagonale leurs inverses.
- e) $-\frac{2}{\sigma_1} = -\frac{2}{\sqrt{8/3}} = -\sqrt{\frac{3}{2}}$ et $-\frac{10}{\sigma_2} = -\frac{10}{\sqrt{200/3}} = -\sqrt{\frac{3}{2}}$, soit $-1{,}225$ deux fois.
- f) $\frac{1}{3}\begin{pmatrix} 4 + 0 + 4 & 20 + 0 + 0 \\ 20 & 100 + 100 + 0 \end{pmatrix}$.
- g) $\frac{20/3}{\sigma_1\sigma_2} = \frac{6{,}667}{13{,}333} = 0{,}5$.

Pour la copie : $(\mathbf{X}_c\mathbf{D}^{-1})_{ij} = \sum_k (\mathbf{X}_c)_{ik}(\mathbf{D}^{-1})_{kj} = \frac{(\mathbf{X}_c)_{ij}}{\sigma_j}$ : seul le terme $k = j$ reste, et la colonne $j$ est divisée par $\sigma_j$ (multiplier à gauche diviserait les **lignes**). La diagonale de $\frac{1}{3}\mathbf{X}_s^\top\mathbf{X}_s$ vaut 1 : la variance d'une colonne standardisée. L'élément de g) est le **coefficient de corrélation** des deux features.

**Erreurs fréquentes.** $\mathrm{ddof} = 1$ en d) et e) (e : $(-1, -1)$) ; centrer avec la moyenne des lignes ; oublier le facteur $\frac{1}{3}$ en f) ; écrire $\mathbf{D}^{-1}\mathbf{X}_c$, qui n'existe pas ici.

**Variante.** La troisième ligne devient $(6, 40)$ : la corrélation ? *Réponse* : la covariance vaut 20, les écarts-types $1{,}633$ et $12{,}47$, d'où environ $0{,}982$.

### Ex M09a.21 — MML §2.1 et §2.2 : systèmes et matrices, en anglais

**Réponse modèle** (avec tes mots ; les tiens peuvent différer).
1. À deux inconnues, chaque équation est une droite du plan ; les solutions sont les points communs : aucun (droites parallèles), un seul (droites sécantes) ou une droite entière (droites confondues). À trois inconnues, chaque équation est un plan de l'espace, et l'intersection peut être vide, un point, une droite ou un plan. Dans tous les cas : aucune, une ou une infinité de solutions.
2. L'élément $(i, j)$ du produit est la somme des produits des éléments de la ligne $i$ de la première matrice par ceux de la colonne $j$ de la seconde ; le nombre de colonnes de la première doit être égal au nombre de lignes de la seconde (les dimensions « voisines »). Le produit élément par élément est le produit de **Hadamard**.
3. *Regular*, *invertible* ou *nonsingular* pour une matrice inversible ; *singular* ou *noninvertible* sinon. Pour une matrice $2 \times 2$, la formule de la fiche §7, avec le nombre $a_{11}a_{22} - a_{12}a_{21}$.
4. Une matrice est symétrique quand elle est égale à sa transposée. Parmi les règles : $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$, $(\mathbf{A}^\top)^\top = \mathbf{A}$, $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$, $(\mathbf{A} + \mathbf{B})^\top = \mathbf{A}^\top + \mathbf{B}^\top$, et l'avertissement $(\mathbf{A} + \mathbf{B})^{-1} \ne \mathbf{A}^{-1} + \mathbf{B}^{-1}$ (fiche §4 et §7, qui les donne aussi).
5. Le système s'écrit $\mathbf{A}\mathbf{x} = \mathbf{b}$, et le livre lit $\mathbf{A}\mathbf{x}$ comme une **combinaison linéaire des colonnes** de $\mathbf{A}$ (fiche §2).
6. Par exemple : *row* (ligne), *column* (colonne), *identity matrix* (matrice identité), *element-wise* (élément par élément), *neighboring dimensions* (dimensions voisines, nos dimensions intérieures).

**Grille.** (1) les droites, puis les plans, et les trois cas ; (2) la définition du produit et la condition sur les formes, le nom de Hadamard ; (3) les deux familles de mots, la formule $2 \times 2$ ; (4) la définition de symétrique et trois règles retrouvées dans la fiche ; (5) l'écriture compacte et la lecture en colonnes ; (6) trois mots traduits. Les réponses sont écrites avec tes mots, pas recopiées.

### Ex M09a.22 — MML §2.3 : résoudre un système, la forme échelonnée et le « Minus-1 trick »

**Réponse modèle** (avec tes mots).
1. Une solution particulière est **une** solution de $\mathbf{A}\mathbf{x} = \mathbf{b}$ ; la solution générale les décrit **toutes**. Trois étapes : trouver une solution particulière ; trouver toutes les solutions de $\mathbf{A}\mathbf{x} = \mathbf{0}$ ; les additionner (M09a.17).
2. Échanger deux lignes, multiplier une ligne par un nombre non nul, ajouter à une ligne un multiple d'une autre. Une forme échelonnée a ses lignes nulles en bas, et le premier nombre non nul d'une ligne (le **pivot**) est strictement à droite de celui de la ligne du dessus. Les variables des colonnes à pivot sont **de base**, les autres **libres**.
3. La forme réduite demande en plus que chaque pivot vaille 1 et soit le seul nombre non nul de sa colonne : comme la fiche §6.
4. On complète la forme réduite en une matrice carrée en insérant des lignes $(0, \ldots, 0, -1, 0, \ldots, 0)$, pour que la diagonale ne contienne que des 1 et des $-1$ ; les colonnes qui ont un $-1$ sur la diagonale sont des solutions du système homogène, et elles les engendrent toutes. Ici, la matrice complétée est $\begin{pmatrix} 1 & 2 & 0 & -1 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & -1 \end{pmatrix}$, et les colonnes 2 et 4 donnent $(2, -1, 0, 0)$ et $(-1, 0, 3, -1)$. Vérification : $2 - 2 = 0$ et $0 = 0$ ; $-1 + 1 = 0$ et $3 - 3 = 0$.
5. Le pivot de Gauss coûte de l'ordre de $n^3$ opérations : trop pour des millions d'inconnues. On utilise alors des méthodes **itératives**, qui améliorent une solution approchée pas à pas (et des décompositions, plus loin dans le livre).
6. Par exemple : *particular solution*, *general solution*, *row-echelon form*, *pivot*, *free variable*, *elementary transformations*.

**Grille.** (1) les deux notions et les trois étapes ; (2) les trois opérations, les définitions de la forme échelonnée, du pivot, des variables de base et libres ; (3) les deux conditions de la forme réduite ; (4) l'astuce en deux phrases, la matrice complétée, deux solutions **vérifiées** ; (5) le coût cubique et l'idée d'une méthode itérative ; (6) trois mots traduits.

### Ex M09a.23 — Fermi : combien de multiplications pour une passe avant sur un million d'images ?

**Réponse modèle.**
1. $32 \times 32 \times 3 = 3\,072$ nombres par image. Couche par couche : $3\,072 \times 1\,024 \approx 3{,}1 \times 10^6$, $1\,024 \times 256 \approx 2{,}6 \times 10^5$, $256 \times 10 \approx 2{,}6 \times 10^3$ ; en tout $3\,410\,432 \approx 3{,}4 \times 10^6$ multiplications.
2. $3{,}4 \times 10^{12}$, de l'ordre de $10^{12}$.
3. La première couche : plus de 90 % du coût, car elle relie les plus grands nombres d'entrées et de sorties ($3\,072 \times 1\,024$).
4. Avec 512 neurones : $3\,072 \times 512 + 512 \times 256 + 256 \times 10 \approx 1{,}7 \times 10^6$, environ deux fois moins (la première couche est divisée par 2, et la deuxième aussi). Réduire plutôt la seconde de 256 à 128 neurones ne fait gagner que 4 % environ : $1\,024 \times 128 + 128 \times 10$ au lieu de $1\,024 \times 256 + 256 \times 10$, sur un total dominé par la première couche.
5. Environ $3{,}4 \times 10^6$ poids (plus 1 290 biais), à 4 octets : de l'ordre de $1{,}4 \times 10^7$ octets, environ 14 Mo.

**Grille.** (1) le nombre d'entrées et les trois produits, avec le total ; (2) la multiplication par $10^6$ ; (3) la première couche, avec sa raison ; (4) les deux nouveaux totaux, et l'explication par la couche dominante ; (5) le nombre de poids fois 4 octets.

### Ex M09a.24 — Expliquer pourquoi on ne calcule pas l'inverse pour résoudre un système

**Réponse modèle.**

> `np.linalg.solve` ne calcule pas l'inverse : il élimine les inconnues une à une (le pivot de Gauss, avec échanges de lignes), puis remonte. Calculer l'inverse revient à résoudre 5 000 systèmes, un par colonne de l'identité (ils partagent la même élimination), puis à faire encore un produit : environ trois fois plus de calculs pour obtenir la même solution. C'est aussi moins précis : chaque opération ajoute une petite erreur d'arrondi, et le chemin par l'inverse en accumule davantage, surtout quand la matrice est presque singulière. L'inverse reste utile quand on la veut elle-même, pour l'étudier ou dans une formule, et sur le papier pour de petites matrices. Pour résoudre, on factorise une fois et on réutilise la factorisation pour chaque nouveau second membre.

**Grille.** (1) ce que fait `solve` (élimination et remontée, sans inverse) ; (2) le coût, plus élevé par l'inverse ; (3) la précision, et le cas presque singulier ; (4) un usage légitime de l'inverse ; huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M09a.E1 — « Combien coûte un produit matriciel, et pourquoi les GPU l'accélèrent-ils ? »

**Réponse modèle (60 secondes).**

> Un produit d'une matrice $(n, p)$ par une matrice $(p, m)$ contient $n\,m$ nombres, chacun un produit scalaire de longueur $p$ : $n\,p\,m$ multiplications, et autant d'additions. Pour deux matrices carrées de taille $n$, c'est $n^3$ : doubler la taille multiplie le travail par huit. Ces $n\,m$ produits scalaires sont indépendants les uns des autres : on peut tous les calculer en même temps. Un GPU a des milliers d'unités de calcul simples, et des circuits spécialisés dans les produits de petits blocs de matrices ; il réutilise chaque bloc chargé en mémoire pour beaucoup de multiplications. Dans un réseau dense, presque tout le temps de calcul est dans les produits $\mathbf{X}\mathbf{W}$ de chaque couche, et la première couche, qui relie le plus d'entrées au plus de neurones, domine souvent. Un piège : dans un produit de trois matrices, l'ordre des parenthèses ne change pas le résultat mais peut changer le coût d'un facteur 40 ou plus ; et, devant un vecteur, on multiplie de droite à gauche.

**Grille.** (1) $n\,p\,m$, et $n^3$ pour des matrices carrées ; (2) l'indépendance des produits scalaires, donc le parallélisme ; (3) ce qu'apporte le GPU (beaucoup d'unités, des blocs réutilisés) ; (4) un exemple de réseau où le produit domine ; (5) le piège des parenthèses.

<a id="notebook"></a>

## Notebook

### Ex M09a.25 — Le produit matriciel et la transposée · `matmul, transpose`

**Réponses** : a) `[[2.0, 10.0], [7.0, 0.0]]` · b) `[[-3.0]]` · c) `[[1.5, 0.0, 3.0], [-2.0, 4.0, 1.0]]` · d) `"ValueError"` · e) `"ndarray"` · f) `True`.

**Démarche.** `A = np.array(A, dtype=float)` (une copie de flottants), de même pour `B` ; une `ValueError` si `A.ndim != 2` ou `B.ndim != 2`, ou si `A.shape[1] != B.shape[0]` ; puis `C = np.zeros((n, m))` et, pour chaque ligne, `C[i] = np.sum(A[i][:, None] * B, axis=0)` : la ligne $i$ de $\mathbf{A}$, mise en colonne, pondère les lignes de $\mathbf{B}$, et la somme sur l'axe 0 donne la ligne $i$ du produit. `transpose` : `T = np.zeros((m, n))` et `T[:, i] = A[i]` pour chaque ligne (ou `T[j] = A[:, j]` pour chaque colonne). Pour la copie : a) $\begin{pmatrix} 2 & 10 \\ 7 & 0 \end{pmatrix}$, $2 \times 3 \times 2 = 12$ multiplications ; b) $2 - 2 - 3 = -3$. `transpose` rend un nouveau tableau : une vue partagerait ses nombres avec la matrice reçue, et modifier le résultat modifierait la matrice de l'appelant.

**Erreurs fréquentes.** `A * B` (Hadamard) ; oublier `axis=0` dans la somme ; rendre une liste ; accepter des formes incompatibles (NumPy lève alors une autre erreur que `ValueError`, ou pas d'erreur du tout avec le broadcasting) ; `A.reshape(m, n)` au lieu d'une transposée (les formes sont justes, les nombres non).

### Ex M09a.26 — La forme échelonnée réduite et le rang · `rref, rank`

**Réponses** : a) `[[1.0, 2.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]` · b) `[0, 2, 3]` · c) `[[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]]` · d) `2` · e) `"ValueError"` · f) `"int"`.

**Démarche.** `R = np.array(A, dtype=float)`, `row = 0`, `pivots = []` ; pour chaque colonne `col` (tant que `row < n`) : `best = row + np.argmax(np.abs(R[row:, col]))` ; si `abs(R[best, col]) <= tol`, on passe ; sinon `R[[row, best]] = R[[best, row]]`, `R[row] = R[row] / R[row, col]`, puis, pour chaque autre ligne `i`, `R[i] = R[i] - R[i, col] * R[row]`, et `pivots.append(col)`, `row += 1`. À la fin, `R[np.abs(R) <= tol] = 0.0` et `return R, tuple(pivots)`. `rank` : `int(len(rref(A, tol)[1]))`. Pour la copie : a) la deuxième colonne est le double de la première ; après l'élimination dans la première colonne, elle ne contient plus que des zéros sous la ligne courante : pas de pivot. d) La ligne 2 est le double de la ligne 1, et la ligne 4 la somme des lignes 1 et 3.

**Erreurs fréquentes.** N'éliminer que **sous** le pivot (une forme échelonnée, pas réduite) ; oublier de diviser la ligne par son pivot ; avancer la ligne courante même quand la colonne n'a pas de pivot ; comparer à 0 exactement au lieu de `tol` (les arrondis laissent des $10^{-16}$) ; rendre une liste de pivots, ou un `np.int64` pour le rang.

### Ex M09a.27 — Résoudre un système par le pivot de Gauss · `solve`

**Réponses** : a) `[1.0, 2.0, 0.0]` · b) `[2.0, 1.0, 3.0]` · c) `[1.0, 1.0]` · d) `"ValueError"` · e) `"ValueError"` · f) `"ndarray"`.

**Démarche.** Les vérifications (carrée, `b` de longueur $n$) ; `M = np.hstack([A, b[:, None]])` ; pour chaque colonne `k` : la ligne du pivot partiel, l'échange, le test `abs(M[k, k]) <= 1e-12 * np.max(np.abs(A))` (une `ValueError`), puis l'élimination sous le pivot ; enfin la remontée, `x[i] = (M[i, n] - np.sum(M[i, i + 1:n] * x[i + 1:])) / M[i, i]` de $i = n - 1$ à 0. Pour la copie : a) $3 - 2 + 0 = 1$, $1 + 4 - 0 = 5$, $2 + 2 + 0 = 4$. b) La colonne 1 commence par un 0 : le pivot partiel prend la ligne 3. c) Sans pivot partiel, on obtiendrait $(0, 1)$ (M09a.32). d) La ligne 2 est le double de la ligne 1 : un pivot nul apparaît.

**Erreurs fréquentes.** Choisir le pivot sur la diagonale sans échange ; chercher le plus grand élément dans toute la colonne (y compris les lignes déjà traitées) ; échanger les lignes de `A` sans échanger `b` (d'où l'intérêt de la matrice augmentée) ; un test de singularité absolu (`== 0`), que les arrondis ne déclenchent jamais ; modifier la matrice reçue.

### Ex M09a.28 — L'inverse par Gauss-Jordan · `inverse`

**Réponses** : a) `[[0.25, 0.5, -0.25], [-0.25, 0.5, 0.25], [0.5, -1.0, 0.5]]` · b) `[[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]` · c) `"ValueError"` · d) `"ValueError"` · e) `True`.

**Démarche.** Une `ValueError` si la matrice n'est pas carrée ; `R, pivots = rref(np.hstack([A, np.eye(n)]))` ; si `pivots[:n] != tuple(range(n))`, la partie gauche n'est pas l'identité : une `ValueError` ; sinon `return R[:, n:]`. Pour la copie : a) $\mathbf{A}^{-1} = \frac{1}{4}\begin{pmatrix} 1 & 2 & -1 \\ -1 & 2 & 1 \\ 2 & -4 & 2 \end{pmatrix}$. b) L'inverse de cette matrice de permutation est sa transposée (une matrice orthogonale, M12b). c) La colonne 3 vaut 3 fois la colonne 1 plus la colonne 2 : $(3 - 1,\ 0 + 1,\ 3 + 0) = (2, 1, 3)$.

**Erreurs fréquentes.** Rendre `R` entière ; regarder seulement le nombre de pivots (une matrice singulière peut avoir $n$ pivots dans $[\mathbf{A} \mid \mathbf{I}]$, dont certains à droite) ; transposer la partie droite.

### Ex M09a.29 — `@`, `*`, `.T`, `np.linalg.solve`, `matrix_rank` et `sympy.Matrix.rref` contre tes fonctions

**Réponses** : a) `[[-7, 9], [1, 0]]` · b) `[[0, -1], [-3, 0]]` · c) `2` · d) `[0, 2]` · e) `[2.0, 1.0]` · f) `True`.

**Démarche.** `(A @ B).tolist()`, `(... * ...).tolist()`, `int(np.linalg.matrix_rank(P))`, `list(sympy.Matrix(P).rref()[1])`, `np.linalg.solve(...).tolist()` ; pour f), une boucle sur 20 tirages `(rng.normal(size=(5, 5)), rng.normal(size=5))` et `all(np.allclose(...))`. Pour la copie : l'élément $(1, 2)$ de a) est le produit scalaire de la ligne 1 de $\mathbf{A}$ et de la colonne 2 de $\mathbf{B}$, $1 \times 1 + (-2) \times (-1) + 0 \times 1 + 3 \times 2 = 9$ ; `A * B` lève une erreur : les formes $(2, 4)$ et $(4, 2)$ ne se combinent pas par broadcasting.

**Erreurs fréquentes.** `A * B` pour le produit matriciel, ou `B @ A` ; les pivots de SymPy comptés à partir de 1 ; comparer des flottants avec `==` en f).

### Ex M09a.30 — Prédire la forme du résultat : `@`, `*` et broadcasting

**Réponses** : a) `2` · b) `2` · c) `2` · d) `2` · e) `1`.

a) $(2, 3) \times (3, 1) \to (2, 1)$ : deux tableaux à deux dimensions donnent un tableau à deux dimensions, une colonne. b) $(3, 4)$ fois un tableau à une dimension de 4 nombres : NumPy le traite comme un vecteur, et rend un tableau à une dimension de 3 nombres. c) Un vecteur de 4 fois $(4, 2)$ : un vecteur de 2 (le vecteur joue le rôle d'une ligne). d) La dimension de droite, 3, coïncide : le vecteur est répété sur les 2 lignes. e) À droite, 3 et 2 diffèrent et aucun ne vaut 1 : erreur ; pour ajouter un nombre par ligne, il faut une colonne de forme `(2, 1)`, `v[:, None]` ou `v.reshape(2, 1)`.

### Ex M09a.31 — Le temps d'un produit matriciel en fonction de n : une pente de 3 en échelle log-log

**Réponse** : `True`.

**Démarche.** `naive_matmul` : `C = [[0.0] * m for _ in range(n)]`, puis trois boucles, `for i`, `for j`, `for k`, avec la somme dans une variable locale. `time_once` : la matrice, puis `start = time.perf_counter()`, le produit, `time.perf_counter() - start` (seul le produit est chronométré). `loglog_slope` : `float(np.polyfit(np.log(ns), np.log(times), 1)[0])`. La vérification garde, pour chaque $n$, le plus petit de trois temps. Pour la copie : la pente mesurée est en général entre 2,8 et 3 ; à petite taille, le temps qui ne dépend pas de $n^3$ (créer les listes, appeler la fonction) pèse un peu. Le plus petit de trois temps est le moins dérangé par le reste de la machine (une autre tâche, le ramasse-miettes) : une perturbation allonge un temps, jamais ne le raccourcit, alors qu'elle tire la moyenne vers le haut. `@` est plusieurs centaines de fois plus rapide dès $n = 120$, et l'écart grandit avec $n$ : il appelle une bibliothèque compilée qui fait les mêmes $n^3$ multiplications, sans passer par l'interpréteur Python pour chacune.

**Erreurs fréquentes.** Chronométrer aussi la création de la matrice ; prendre `np.log10` pour une seule des deux listes ; une triple boucle qui utilise `@` ou `np.dot` à l'intérieur (le temps ne varie plus comme $n^3$) ; mesurer des tailles trop petites (le temps fixe domine).

### Ex M09a.32 — Pourquoi le pivot partiel : un petit pivot et les arrondis

**Réponses** : a) `1.0` · b) `-8` · c) `16` · d) `True`.

**Démarche.** Pour chaque $k$ : `A = np.array([[10.0 ** -k, 1.0], [1.0, 1.0]])`, `b = np.array([1.0, 2.0])`, `exact = np.linalg.solve(A, b)`, puis `float(np.max(np.abs(solve_no_pivot(A, b) - exact)))` et la même chose avec `mymath.matrices.solve`. Pour la copie : sans pivot, l'élimination retranche $\frac{1}{\varepsilon}$ fois la première ligne à la seconde, qui devient $(0,\ 1 - \frac{1}{\varepsilon} \mid 2 - \frac{1}{\varepsilon})$ ; pour $\varepsilon$ minuscule, les nombres 1 et 2 disparaissent dans les arrondis de $\frac{1}{\varepsilon}$ (environ 16 chiffres significatifs, R1). $y$ reste juste, mais $x = \frac{1 - y}{\varepsilon}$ divise une erreur d'arrondi, de l'ordre de $10^{-16}$, par $\varepsilon$ : l'erreur sur $x$ croît comme $\frac{10^{-16}}{\varepsilon}$, jusqu'à donner $x = 0$ pour $\varepsilon = 10^{-18}$. Avec le pivot partiel, on élimine avec la ligne $x + y = 2$ et un multiplicateur $\varepsilon$, minuscule : les erreurs ne sont plus amplifiées.

La vérification de c) rend 0 si aucune erreur ne dépasse $10^{-2}$. **Erreurs fréquentes.** Rendre les couples dans l'ordre (avec pivot, sans pivot) ; mesurer l'erreur sur $y$ seulement ; comparer à la solution $(1, 1)$ arrondie au lieu de la solution calculée par `np.linalg.solve` (la différence est de l'ordre de $\varepsilon$, sans importance ici) ; un seuil à $10^{-3}$ au lieu de $10^{-2}$ en c).

### Ex M09a.33 — Une matrice 2 × 2 comme transformation du plan : la grille et le carré unité

**Démarche.** `M = np.asarray(M, dtype=float)` ; pour chaque $c$ de $-2$ à 2, les deux extrémités de la ligne verticale, $(c, -2)$ et $(c, 2)$, et de l'horizontale, $(-2, c)$ et $(2, c)$, rangées en lignes dans un tableau `P` ; leurs images sont les lignes de `P @ M.T` (l'image d'un point $\mathbf{x}$ est $\mathbf{M}\mathbf{x}$) ; `ax.plot(...)` en gris. Le carré : `np.array([[0, 0], [1, 0], [1, 1], [0, 1]]) @ M.T`, puis `ax.add_patch(Polygon(..., closed=True))`. Pour la copie : les colonnes de $\mathbf{M}$ sont les images de $\mathbf{e}_1$ et $\mathbf{e}_2$. La rotation envoie $\mathbf{e}_1$ sur $(0, 1)$ et $\mathbf{e}_2$ sur $(-1, 0)$ ; le cisaillement garde $\mathbf{e}_1$ et penche $\mathbf{e}_2$ en $(1{,}5 ;\ 1)$ ; la dilatation étire l'axe des $x$ par 2 et écrase celui des $y$ par 2. La matrice singulière a deux colonnes proportionnelles, $(1 ;\ 0{,}5)$ et $(2, 1)$ : tout le plan est envoyé sur une droite, et le carré unité devient un segment. Aucune matrice ne peut défaire cela : c'est pourquoi elle n'a pas d'inverse. La rotation d'un quart de tour dans l'autre sens, $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, défait la première : c'est son inverse, et aussi sa transposée.

**Erreurs fréquentes.** `P @ M` au lieu de `P @ M.T` (on applique alors $\mathbf{M}^\top$) ; ouvrir une figure dans la fonction ; tracer le carré dans l'ordre $(0, 0), (1, 0), (0, 1), (1, 1)$ (un polygone croisé).

### Ex M09a.34 — Chasse à l'erreur : `*` au lieu de `@`, une transposée oubliée, un pivot nul

**Réponses** : a) `"ADE"` · b) `[-2.0, 5.0, -1.5, -1.0, 4.0, 0.75]`.

**Démarche.** (A) `A * B` est le produit de Hadamard : son élément $(2, 1)$ vaut $3 \times 2 = 6$, alors que celui de $\mathbf{A}\mathbf{B}$ vaut $3 \times 0 + (-1) \times 2 = -2$ ; il faut `A @ B`. (B) est juste : $2 + 3 = 5$. (C) est juste : $-1 - 2 + 0{,}5 + 1 = -1{,}5$. (D) `X @ X.T` a la forme $(2, 2)$ : c'est la matrice des produits scalaires des **exemples**, et son élément $(1, 2)$ existe, d'où l'absence d'erreur ; $\mathbf{X}^\top\mathbf{X}$, de forme $(3, 3)$, s'écrit `X.T @ X`, et son élément $(1, 2)$ vaut $1 \times 0 + (-1) \times 1 = -1$. (E) Le pivot $M_{11}$ vaut 0 : la ligne divise par zéro (`inf` et `nan`) ; il faut d'abord échanger les deux lignes, et l'on trouve 4. (F) est juste : $\frac{3}{4} = 0{,}75$ (la variable `R` contient $\mathbf{D}^{-1}\mathbf{A}$).

**Erreurs fréquentes.** Citer (F) en croyant qu'il faut $\mathbf{A}\mathbf{D}^{-1}$ (multiplier à gauche par une diagonale agit sur les **lignes**, comme le dit le commentaire) ; oublier (D), qui s'exécute sans erreur : seule la forme la trahit.

### Ex M09a.35 — Tester une propriété : un pytest pour (AB)ᵀ = BᵀAᵀ sur des matrices aléatoires

**Démarche.** `rng = np.random.default_rng(seed)` une seule fois ; dans la boucle, `n, p, m = rng.integers(1, 6, size=3)`, `A = rng.normal(size=(n, p))`, `B = rng.normal(size=(p, m))`, les deux côtés en tableaux de flottants, puis `assert left.shape == right.shape and np.allclose(left, right, rtol=0, atol=1e-12), f"expected … got …"`. `test_transpose_of_product` appelle `check_transpose_of_product(mymath.matrices.matmul, mymath.matrices.transpose, seed=35)`. Pour la copie : la transposée par `reshape` garde l'ordre des nombres ligne par ligne ; elle rend la bonne forme, mais de mauvais nombres, sauf pour une seule ligne ou une seule colonne, où les deux coïncident. Un test qui ne tirerait que des vecteurs (ou des matrices $1 \times 1$) la laisserait passer ; des formes aléatoires la démasquent, dès qu'une matrice a au moins deux lignes et deux colonnes (une matrice carrée suffit : `reshape` la rend inchangée). Le produit de Hadamard de deux matrices carrées vérifie la propriété : $(\mathbf{A} \odot \mathbf{B})^\top = \mathbf{A}^\top \odot \mathbf{B}^\top = \mathbf{B}^\top \odot \mathbf{A}^\top$. Un test de propriété ne vérifie qu'une **conséquence** de la bonne réponse, qu'une fonction fausse peut partager ; pour l'attraper, il faut aussi comparer à un oracle (`@`) ou à quelques produits calculés à la main, comme le font les tests de `mymath`.

**Erreurs fréquentes.** Des vecteurs seulement, des formes $(1, n)$ ou $(n, 1)$ (la transposée par `reshape` passe) ; `==` entre flottants ; un générateur recréé à chaque tour ; un `assert` sans message ; comparer les valeurs sans comparer les formes.

### Ex M09a.36 — Défi : un système 500 × 500 résolu par ton `solve`, à 1e−8 près de NumPy, en moins d'une seconde

**Réponse** : `True`.

**Démarche.** La boucle Python sur les lignes sous le pivot se remplace par une seule opération sur le bloc : `factors = M[k + 1:, k] / M[k, k]`, de forme $(n - k - 1,)$, devient une colonne par `factors[:, None]`, et `M[k + 1:] = M[k + 1:] - factors[:, None] * M[k]` élimine d'un coup, par broadcasting. Il reste une boucle Python sur les $n$ colonnes (et une pour la remontée) : un à deux dixièmes de seconde pour $n = 500$, avec une erreur de l'ordre de $10^{-12}$. Pour la copie : une version qui traite les nombres un par un (deux boucles imbriquées sous chaque pivot) met plusieurs secondes, souvent plus de dix ; une version qui traite chaque ligne d'un coup (une boucle sur les lignes) passe aussi, en quelques dixièmes de seconde ; la version par blocs est la plus rapide. Le troisième système a une diagonale de $10^{-14}$ : sans échange de lignes, chaque élimination divise par ces pivots minuscules, et l'erreur explose (M09a.32).

**Erreurs fréquentes.** Vectoriser en oubliant le pivot partiel (le troisième système échoue) ; `M[k + 1:] -= factors * M[k]` sans `[:, None]` (une erreur de forme) ; recalculer `np.max(np.abs(A))` à chaque colonne (correct, mais inutile).
