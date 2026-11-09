# M12d · SVD et analyse en composantes principales — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M12d.Q1 — La SVD : formes et propriétés
1. SVD complète : $\mathbf{U}$ de forme $(5, 5)$, $\mathbf{S}$ de forme $(5, 3)$ (la forme de $\mathbf{A}$), $\mathbf{V}$ de forme $(3, 3)$. SVD compacte : $\mathbf{U}_r$ de forme $(5, 2)$, $\mathbf{S}_r$ de forme $(2, 2)$, $\mathbf{V}_r$ de forme $(3, 2)$.
2. Deux (le rang). Le noyau est de dimension $3 - 2 = 1$ : il est engendré par $\mathbf{v}_3$.
3. **Faux** : $s_i = \sqrt{\lambda_i(\mathbf{A}^\top\mathbf{A})} \ge 0$ ; un éventuel signe passe dans $\mathbf{u}_i$.
4. $\mathbf{A}\mathbf{v}_1 = s_1\mathbf{u}_1$ et $\mathbf{A}^\top\mathbf{u}_1 = s_1\mathbf{v}_1$ (la transposée $\mathbf{A}^\top = \sum s_i\mathbf{v}_i\mathbf{u}_i^\top$ échange les rôles).
5. Les valeurs singulières sont $5$ puis $3$. $\mathbf{v}_1 = \mathbf{e}_2$, et $\mathbf{u}_1 = \mathbf{A}\mathbf{e}_2/5 = -\mathbf{e}_2$ : le signe moins passe dans $\mathbf{u}_1$ ; $\mathbf{v}_2 = \mathbf{u}_2 = \mathbf{e}_1$.
6. $\mathbf{v}_2$ est la **deuxième ligne** de `Vt`, `Vt[1]`. Avec `full_matrices=False`, `U` est de forme $(5, 3)$ : NumPy garde $\min(m, n) = 3$ valeurs, la troisième étant (presque) nulle.

### M12d.Q2 — Valeurs singulières et valeurs propres
1. **Faux** : ce sont leurs **racines**.
2. **Vrai** : $\mathbf{U} = \mathbf{V} = \mathbf{Q}$ et $s_i = \lambda_i$.
3. **Vrai** : le signe de $\lambda_i$ passe dans $\mathbf{u}_i = \pm\mathbf{v}_i$.
4. **Vrai** (fiche §1, M12d.14).
5. **Faux** : le cisaillement $\begin{pmatrix} 1 & 10 \\ 0 & 1 \end{pmatrix}$ n'a que la valeur propre 1, et étire jusqu'à environ 10,1.
6. **Vrai** : $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}$.
7. **Vrai** : $\lvert\det\mathbf{U}\rvert = \lvert\det\mathbf{V}\rvert = 1$.
8. **Vrai** : $\mathbf{A}^\top = \mathbf{V}\mathbf{S}^\top\mathbf{U}^\top$.

### M12d.Q3 — Rang faible : ce qu'on garde, ce qu'on perd
1. Rang 5 ; $\lVert \mathbf{A} \rVert_F^2 = 144 + 81 + 16 + 4 + 1 = 246$.
2. En Frobenius, $\sqrt{16 + 4 + 1} = \sqrt{21} \approx 4{,}58$ ; en norme spectrale, $s_3 = 4$.
3. $\frac{144 + 81}{246} = \frac{225}{246} \approx 91{,}5\,\%$.
4. $2 \times (100 + 80 + 1) = 362$ nombres, contre $8\,000$.
5. **Vrai** : l'erreur au carré est la somme des $s_i^2$ oubliés ; elle passe de $16 + 4 + 1$ à $81 + 4 + 1$.
6. Parce que le niveau moyen domine l'énergie d'une image brute : la première couche le rend presque seul, et une part d'énergie élevée ne dit alors rien de la qualité (fiche §3, ⚠️).

### M12d.Q4 — Pseudo-inverse et conditionnement
1. $\mathbf{A}^{-1}$.
2. $\operatorname{diag}(\frac{1}{4}, 0, \frac{1}{2})$ : on inverse ce qui s'inverse.
3. $(5, 3)$.
4. $\mathbf{D}$ : $+\infty$ (une valeur singulière nulle). $\operatorname{diag}(5, -2)$ : $\frac{5}{2} = 2{,}5$ (les valeurs singulières sont 5 et 2). $7\,\mathbf{I}_4$ : 1.
5. **Faux** : $\det(10^{-2}\,\mathbf{I}_3) = 10^{-6}$, et $\kappa = 1$. Le déterminant mesure un volume, le conditionnement un aplatissement.
6. Environ 4 chiffres ; par les équations normales, $\kappa(\mathbf{A}^\top\mathbf{A}) = 10^8$ : environ 8.
7. Sur l'image de $\mathbf{A}$ (l'espace engendré par ses colonnes, ou par $\mathbf{u}_1, \ldots, \mathbf{u}_r$).

### M12d.Q5 — Ce que maximise un axe principal
1. $\mathbf{u}^\top\mathbf{C}\,\mathbf{u}$.
2. La plus grande valeur propre $\lambda_1$ de $\mathbf{C}$, atteinte en son vecteur propre unitaire $\mathbf{u}_1$ (quotient de Rayleigh, M12c §6).
3. **Faux** : une covariance non nulle entre features fait tourner l'axe. Pour $\mathbf{C} = \begin{pmatrix} 37 & 6 \\ 6 & 2 \end{pmatrix}$, la variance le long de $\mathbf{e}_1$ vaut 37, mais $\lambda_1 = 38$, le long de $\frac{1}{\sqrt{37}}(6, 1)$.
4. Le bloc $\begin{pmatrix} 2 & 2 \\ 2 & 5 \end{pmatrix}$ a pour trace 7 et déterminant 6 : $\frac{1}{\sqrt{5}}(0, 1, 2)$ (variance 6), puis $\mathbf{e}_1$ (4), puis $\frac{1}{\sqrt{5}}(0, 2, -1)$ (1).
5. $\operatorname{tr}\mathbf{C}$, la variance totale.
6. Ce sont des vecteurs propres d'une matrice symétrique (théorème spectral) ; pour des variances distinctes, ils sont forcément orthogonaux.
7. Non : un axe n'est défini qu'au signe près ; une convention (celle de la fiche) choisit.

### M12d.Q6 — Centrer et standardiser avant une ACP ?
1. Il pointe vers la moyenne du nuage (la direction de $\boldsymbol{\mu}$), au lieu de suivre son allongement (fiche §6).
2. Standardiser : les unités diffèrent, et sans cela l'unité choisie déciderait des variances, donc des axes.
3. Centrer sans réduire : même unité, et un capteur qui varie plus que les autres le dit vraiment ; la standardisation effacerait cette information.
4. **Vrai** : la covariance des données standardisées est la matrice de corrélation.
5. De moyenne nulle, oui ; corrélés, non (M12d.19).
6. L'exemple lui-même : l'erreur est nulle.

### M12d.Q7 — Variance expliquée et nombre de composantes
1. 50 %, 40 % et 10 % ; deux composantes (90 %).
2. Sinon les parts sommeraient à 1 quel que soit $k$, et ne diraient rien de ce que l'on perd.
3. $\frac{10}{11}(4 + 1) = \frac{50}{11} \approx 4{,}55$.
4. **Vrai** : les 11 lignes centrées ont une somme nulle, $\mathbf{X}_c$ est de rang au plus 10.
5. L'endroit où la courbe des $\lambda_j$ cesse de chuter et devient plate : au-delà, des variances petites et comparables, souvent du bruit.
6. Sur ces données, les $k$ premiers axes sont par construction le meilleur sous-espace (Eckart-Young) ; sur d'autres, la même projection fait **en moyenne** moins bien.

### M12d.Q8 — ACP, t-SNE ou UMAP : qui garde quoi ?
1. L'ACP garde les grandes distances (une projection) ; t-SNE et UMAP gardent les voisinages.
2. **Faux** : t-SNE optimise les positions des $n$ points donnés ; il n'y a pas de formule pour un point nouveau. L'ACP en a une (projeter sur les axes), UMAP en construit une.
3. Ses probabilités de voisinage ont l'entropie d'une loi uniforme sur 5 voisins : environ 5 voisins « effectifs ».
4. $0{,}04 \log_2 8 = 0{,}12$ bit contre $0{,}000\,5 \log_2 0{,}125 = -0{,}001\,5$ bit : écarter deux voisins coûte cher, rapprocher deux points lointains presque rien (le terme est même négatif : seule la somme est forcément positive ou nulle).
5. En 2D, il n'y a pas la place de garder les distances moyennes d'un nuage de grande dimension ; la queue lourde laisse les points modérément éloignés s'écarter davantage, ce qui sépare les groupes.
6. Leurs couples ont des $p_{ij}$ presque nuls : la divergence ne contraint presque pas leur écart, qui dépend de l'optimisation (et du point de départ) plus que des données.

<a id="rappels"></a>

## 🔁 Rappels

### M12d.R1 — Valeurs propres et théorème spectral (M12c)
1. Trace 20, déterminant $-44 - 25 = -69$ : $\lambda^2 - 20\lambda - 69 = (\lambda - 23)(\lambda + 3)$.
2. Pour 23 : $\frac{1}{\sqrt{26}}(1, 5)$ ; pour $-3$ : $\frac{1}{\sqrt{26}}(5, -1)$.
3. $\mathbf{Q} = \frac{1}{\sqrt{26}}\begin{pmatrix} 1 & 5 \\ 5 & -1 \end{pmatrix}$, $\boldsymbol{\Lambda} = \operatorname{diag}(23, -3)$, et $\mathbf{Q}^\top\mathbf{Q} = \frac{1}{26}\begin{pmatrix} 1 + 25 & 5 - 5 \\ 5 - 5 & 25 + 1 \end{pmatrix} = \mathbf{I}$.
4. $s_1 = 23$, $s_2 = 3$ ; $\mathbf{u}_1 = \mathbf{v}_1 = \frac{1}{\sqrt{26}}(1, 5)$, et pour la valeur propre négative, $\mathbf{v}_2 = \frac{1}{\sqrt{26}}(5, -1)$ et $\mathbf{u}_2 = \mathbf{K}\mathbf{v}_2/3 = -\mathbf{v}_2$.
5. Non : une valeur propre est négative.

### M12d.R2 — La projection orthogonale (M12b)
1. $\frac{64 + 81 + 144}{289} = 1$.
2. $t = \frac{88 + 81 + 120}{17} = \frac{289}{17} = 17$.
3. $\mathbf{p} = (8, 9, 12)$, $\mathbf{r} = (3, 0, -2)$, et $\mathbf{r} \cdot \mathbf{u} = \frac{24 + 0 - 24}{17} = 0$.
4. $121 + 81 + 100 = 302 = 289 + 13$.
5. Rang 1 ; $\mathbf{P}^2 = \mathbf{u}(\mathbf{u}^\top\mathbf{u})\mathbf{u}^\top = \mathbf{P}$.

### M12d.R3 — Moyenne, covariance et standardisation (M02c)
1. $(5, 45)$ ; centrées : $(-3, -10)$, $(-1, 10)$, $(1, -5)$, $(3, 5)$.
2. $\frac{20}{3} \approx 6{,}67$, $\frac{250}{3} \approx 83{,}3$ et $\frac{30}{3} = 10$.
3. $\frac{30}{\sqrt{20 \times 250}} = \frac{3}{\sqrt{50}} \approx 0{,}424$.
4. $\big(\frac{-3}{\sqrt{20/3}}, \frac{-10}{\sqrt{250/3}}\big) \approx (-1{,}16 ;\ -1{,}10)$.
5. La variance est multipliée par 100 ($\frac{25\,000}{3}$), la covariance par 10 (100), et la corrélation ne change pas ($0{,}424$) : c'est pourquoi l'ACP de données standardisées, qui est celle de la matrice de corrélation, ne dépend pas des unités.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M12d.1 — La SVD d'une matrice 2 × 2 à la main, par AᵀA

**Réponses** : a) `[[125, 110], [110, 104]]` · b) `[225, 4]` · c) `[15, 2]` · d) `[0.7399, 0.6727]` · e) `[-0.6727, 0.7399]` · f) `[0.9417, 0.3363]` · g) `-30` · h) `[14.124, -2.124]`.

**Démarche.**
- a) b) Trace 229, déterminant $125 \times 104 - 110^2 = 900$ : $\lambda^2 - 229\lambda + 900 = (\lambda - 225)(\lambda - 4)$. c) $s_1 = 15$, $s_2 = 2$.
- d) Pour 225 : $\begin{pmatrix} -100 & 110 \\ 110 & -121 \end{pmatrix}$ donne $10x = 11y$, $\mathbf{v}_1 = \frac{1}{\sqrt{221}}(11, 10)$. e) Orthogonal : $\pm(10, -11)$ ; la coordonnée de plus grande valeur absolue, $\pm 11$, positive : $\mathbf{v}_2 = \frac{1}{\sqrt{221}}(-10, 11)$. f) $\mathbf{A}(11, 10) = (210, 75) = 15\,(14, 5)$, donc $\mathbf{u}_1 = \frac{1}{\sqrt{221}}(14, 5)$.
- g) $20 - 50 = -30 = -(15 \times 2)$. h) Trace 12, déterminant $-30$ : $\lambda = 6 \pm \sqrt{66}$.

Pour la copie : $\mathbf{A}(-10, 11) = (10, -28) = 2\,(5, -14)$, donc $\mathbf{u}_2 = \frac{1}{\sqrt{221}}(5, -14)$ ; $15\,\mathbf{u}_1\mathbf{v}_1^\top + 2\,\mathbf{u}_2\mathbf{v}_2^\top = \frac{1}{221}\Big[15\begin{pmatrix} 154 & 140 \\ 55 & 50 \end{pmatrix} + 2\begin{pmatrix} -50 & 55 \\ 140 & -154 \end{pmatrix}\Big] = \frac{1}{221}\begin{pmatrix} 2\,210 & 2\,210 \\ 1\,105 & 442 \end{pmatrix} = \mathbf{A}$. $\lvert\det\mathbf{A}\rvert = s_1s_2$ ; le signe moins vient de $\det\mathbf{U}\det\mathbf{V} = -1$. Les valeurs propres de $\mathbf{A}$ disent quelles directions $\mathbf{A}$ garde ; les valeurs singulières, de combien elle étire ses deux directions privilégiées, qui ne sont pas les mêmes au départ et à l'arrivée.

**Erreurs fréquentes.** Oublier la racine ($s = 225$) ; prendre $\mathbf{A}\mathbf{A}^\top$ (mêmes valeurs propres, mais ses vecteurs propres sont les $\mathbf{u}_i$) ; ne pas diviser $\mathbf{A}\mathbf{v}_1$ par $s_1$.

**Variante.** La SVD de $\mathbf{A}^\top$ ? *Réponse* : mêmes valeurs singulières, rôles échangés : $\mathbf{A}^\top = \mathbf{V}\mathbf{S}\mathbf{U}^\top$ (ses vecteurs à droite sont les $\mathbf{u}_i$, au signe de la convention près).

### Ex M12d.2 — La SVD compacte d'une matrice 3 × 2 de rang 1

**Réponses** : a) `1` · b) `[[225, -1125], [-1125, 5625]]` · c) `[5850, 0]` · d) `76.4853` · e) `[-0.1961, 0.9806]` · f) `[-0.1333, -0.6667, -0.7333]` · g) `5850` · h) `[0.9806, 0.1961]`.

**Démarche.** La deuxième colonne vaut $-5$ fois la première : $\mathbf{A} = \mathbf{a}\mathbf{b}^\top$ avec $\mathbf{a} = (2, 10, 11)$ ($\lVert \mathbf{a} \rVert = 15$) et $\mathbf{b} = (1, -5)$ ($\lVert \mathbf{b} \rVert = \sqrt{26}$). $\mathbf{A}^\top\mathbf{A} = \lVert \mathbf{a} \rVert^2\,\mathbf{b}\mathbf{b}^\top = 225\begin{pmatrix} 1 & -5 \\ -5 & 25 \end{pmatrix}$, de valeurs propres $225 \times 26 = 5\,850$ (pour $\mathbf{b}$) et 0 (pour $\mathbf{b}^\perp$). $s_1 = 15\sqrt{26}$. $\mathbf{v}_1 = \pm\frac{\mathbf{b}}{\sqrt{26}}$ : la convention veut la coordonnée $\pm 5$ positive, donc $\mathbf{v}_1 = \frac{1}{\sqrt{26}}(-1, 5)$ ; alors $\mathbf{u}_1 = \mathbf{A}\mathbf{v}_1/s_1 = \mathbf{a}\,\frac{\mathbf{b} \cdot \mathbf{v}_1}{s_1} = \mathbf{a}\,\frac{-\sqrt{26}}{15\sqrt{26}} = -\frac{\mathbf{a}}{15}$. h) $\mathbf{v}_2 \perp \mathbf{b}$ : $\frac{1}{\sqrt{26}}(5, 1)$.

Pour la copie : $\mathbf{A} = \Big(-\frac{1}{15}\begin{pmatrix} 2 \\ 10 \\ 11 \end{pmatrix}\Big)\,(15\sqrt{26})\,\Big(\frac{1}{\sqrt{26}}\begin{pmatrix} -1 & 5 \end{pmatrix}\Big)$ : $3 + 1 + 2 = 6$ nombres, contre $9 + 2 + 4 = 15$ pour la SVD complète ($\mathbf{U}$ $3 \times 3$, deux valeurs singulières, $\mathbf{V}$ $2 \times 2$). $\mathbf{u}_1$ est négatif parce que la convention porte sur $\mathbf{v}_1$, et que $\mathbf{u}_1$ suit.

**Erreurs fréquentes.** Choisir $\mathbf{v}_1 = \frac{1}{\sqrt{26}}(1, -5)$ (le signe) ; calculer $\mathbf{u}_1$ avec un autre $\mathbf{v}_1$ que celui retenu ; écrire $s_1 = 5\,850$.

**Variante.** Une matrice $100 \times 50$ de rang 1 : combien de nombres pour sa SVD compacte ? *Réponse* : $100 + 1 + 50 = 151$, contre $5\,000$.

### Ex M12d.3 — Le cercle unité devient une ellipse : axes et demi-axes

**Réponses** : a) `[9, 4]` · b) `[0.8682, -0.4961]` · c) `[-0.124, 0.9923]` · d) `36` · e) `4.1231` · f) `8.9443` · g) `2.25` · h) `False`.

**Démarche.** $\mathbf{B}^\top\mathbf{B} = \begin{pmatrix} 17 & -8 \\ -8 & 80 \end{pmatrix}$, trace 97, déterminant 1 296 : valeurs propres 81 et 16, $s_1 = 9$, $s_2 = 4$. Pour 81 : $-64x - 8y = 0$, $\mathbf{v}_1 = \frac{1}{\sqrt{65}}(-1, 8)$ (convention). $\mathbf{B}\mathbf{v}_1 = \frac{1}{\sqrt{65}}(63, -36) = 9 \cdot \frac{1}{\sqrt{65}}(7, -4)$ : le grand axe est porté par $\mathbf{u}_1 = \frac{1}{\sqrt{65}}(7, -4)$. d) $\pi s_1s_2 = 36\,\pi = \lvert\det\mathbf{B}\rvert\,\pi$. e) $\lVert (1, 4) \rVert = \sqrt{17}$, f) $\lVert (8, -4) \rVert = \sqrt{80}$. h) $\det\mathbf{B} = -36 < 0$.

Pour la copie : e) et f) sont des $\lVert \mathbf{B}\mathbf{x} \rVert$ pour $\mathbf{x}$ unitaire, donc entre $s_2 = 4$ et $s_1 = 9$ (fiche §2). Le point $\mathbf{v}_2 = \frac{1}{\sqrt{65}}(8, 1)$ (ou son opposé) est envoyé au bout du petit axe, en $4\,\mathbf{u}_2 = \frac{4}{\sqrt{65}}(4, 7)$.

**Erreurs fréquentes.** Donner $\mathbf{v}_1$ pour la direction du grand axe (c'est le point de départ, pas l'arrivée) ; les demi-axes au carré (81 et 16) ; une aire négative.

**Variante.** L'image du cercle de rayon 2 ? *Réponse* : une ellipse de demi-axes 18 et 8, mêmes directions.

### Ex M12d.4 — L'approximation de rang 1 d'une matrice 3 × 3 et son erreur

**Réponses** : a) `59` · b) `[[33, 20, 0], [20, 24, 0], [0, 0, 2]]` · c) `[7, 2.8284, 1.4142]` · d) `[0.7809, 0.6247, 0]` · e) `[0.6247, 0.6247, 0.4685]` · f) `[[3.4146, 2.7317, 0], [3.4146, 2.7317, 0], [2.561, 2.0488, 0]]` · g) `3.1623` · h) `0.8305`.

**Démarche.** La troisième colonne $(1, -1, 0)$ est orthogonale aux deux autres : $\mathbf{A}^\top\mathbf{A}$ est par blocs. Le bloc $\begin{pmatrix} 33 & 20 \\ 20 & 24 \end{pmatrix}$ a pour trace 57 et déterminant 392 : valeurs propres 49 et 8 ; la troisième vaut 2. $s = 7$, $2\sqrt{2}$, $\sqrt{2}$. Pour 49 : $-16x + 20y = 0$, $\mathbf{v}_1 = \frac{1}{\sqrt{41}}(5, 4, 0)$. $\mathbf{A}\mathbf{v}_1 = \frac{1}{\sqrt{41}}(28, 28, 21) = 7 \cdot \frac{1}{\sqrt{41}}(4, 4, 3)$. f) $\mathbf{A}_1 = 7\,\mathbf{u}_1\mathbf{v}_1^\top = \frac{7}{41}\begin{pmatrix} 20 & 16 & 0 \\ 20 & 16 & 0 \\ 15 & 12 & 0 \end{pmatrix}$. g) $\sqrt{8 + 2} = \sqrt{10}$. h) $\frac{49}{59}$.

Pour la copie : une colonne orthogonale à toutes les autres est un vecteur propre « à elle seule » de $\mathbf{A}^\top\mathbf{A}$ ($\mathbf{e}_3$, de valeur propre $\lVert \mathbf{c}_3 \rVert^2$). $\mathbf{A} - \mathbf{A}_1 = \frac{1}{41}\begin{pmatrix} 24 & -30 & 41 \\ 24 & -30 & -41 \\ -64 & 80 & 0 \end{pmatrix}$, de somme des carrés $\frac{2 \times 1\,476 + 10\,496}{1\,681} + 2 = 10$. En norme spectrale, l'erreur vaut $s_2 = 2\sqrt{2} \approx 2{,}83$. $\mathbf{A}_1$ dit : les clients 1 et 2 ont exactement les mêmes goûts, le client 3 les mêmes, en un peu plus faible ; tous préfèrent le produit 1 au produit 2 dans le rapport 5/4 ; le produit 3, sur lequel les clients 1 et 2 s'opposent, disparaît.

**Erreurs fréquentes.** Oublier le facteur $s_1$ dans $\mathbf{A}_1$ ; l'erreur avec les $s$ au lieu des $s^2$ ($2\sqrt{2} + \sqrt{2}$) ; la part d'énergie $\frac{7}{7 + 3\sqrt{2}}$.

**Variante.** L'erreur de $\mathbf{A}_2$, en Frobenius ? *Réponse* : $s_3 = \sqrt{2}$.

### Ex M12d.5 — Compter les nombres stockés : une image en rang k

**Réponses** : a) `1440000` · b) `100040` · c) `0.0695` · d) `575` · e) `11` · f) `300120` · g) `228040`.

**Démarche.** $k(m + n + 1) = 40 \times 2\,501$. d) $k < \frac{1\,440\,000}{2\,501} \approx 575{,}8$. e) $k \le \frac{28\,800}{2\,501} \approx 11{,}5$. f) $3 \times 100\,040$. g) $40 \times (900 + 4\,800 + 1)$.

Pour la copie : f) et g) ne gardent pas la même chose : g) impose aux trois canaux les **mêmes** 40 vecteurs $\mathbf{u}_i$ (les mêmes « profils de lignes »), f) en donne 40 à chacun. Les canaux d'une photo se ressemblent beaucoup (mêmes contours) : à nombre égal, g) est souvent meilleur ; on peut aussi passer d'abord dans une base où les canaux se décorrèlent (luminance, chrominance). Un format d'image compte des **bits** : il quantifie (arrondit) les coefficients et code les fréquents en peu de bits (M06), bien plus économe que des nombres flottants.

**Erreurs fréquentes.** Oublier les $k$ valeurs singulières ($k(m + n)$) ; arrondir d) ou e) vers le haut.

**Variante.** Une matrice de notes de $2\,000$ films par $50\,000$ spectateurs, stockée par son approximation de rang 20 : quelle part des nombres ? *Réponse* : $\frac{20 \times 52\,001}{10^8} \approx 1{,}04\,\%$.

### Ex M12d.6 — La pseudo-inverse d'une matrice non inversible et la solution de norme minimale

**Réponses** : a) `1` · b) `48.4665` · c) `2349` · d) `[[0.8514, 2.1286], [-3.4057, -8.5143], [6.8114, 17.0285]]` (soit $1\,000\,\mathbf{A}^+$) · e) `[0.1111, -0.4444, 0.8889]` · f) `1` · g) `9` · h) `[0.1379, 0.3448]`.

**Démarche.** $\mathbf{A} = \mathbf{a}\mathbf{b}^\top$ avec $\mathbf{a} = (2, 5)$ et $\mathbf{b} = (1, -4, 8)$ : $s_1 = \lVert \mathbf{a} \rVert\,\lVert \mathbf{b} \rVert = 9\sqrt{29}$, et $\lVert \mathbf{A} \rVert_F^2 = s_1^2 = 29 \times 81 = 2\,349$. $\mathbf{A}^+ = \frac{1}{s_1}\mathbf{v}_1\mathbf{u}_1^\top = \frac{\mathbf{b}\mathbf{a}^\top}{s_1^2} = \frac{\mathbf{A}^\top}{2\,349}$, d'où d) en multipliant par $1\,000$. e) $\mathbf{x}^+ = \mathbf{b}\,\frac{\mathbf{a}^\top\mathbf{y}}{2\,349} = \mathbf{b}\,\frac{36 + 225}{2\,349} = \frac{\mathbf{b}}{9}$. f) $\frac{\lVert \mathbf{b} \rVert}{9} = 1$. g) $(9, 0, 0)$ est aussi une solution ($2 \times 9 = 18$, $5 \times 9 = 45$), de norme 9. h) $\mathbf{A}\mathbf{A}^+\mathbf{y}' = \mathbf{a}\,\frac{\mathbf{a}^\top\mathbf{y}'}{\lVert \mathbf{a} \rVert^2} = \frac{2}{29}(2, 5)$.

Pour la copie : les solutions de $\mathbf{A}\mathbf{x} = \mathbf{y}$ forment le plan $x_1 - 4x_2 + 8x_3 = 9$ ; $\mathbf{x}^+ = \frac{9}{81}\mathbf{b}$ est le pied de la perpendiculaire menée de l'origine à ce plan (il est dans l'espace des lignes, orthogonal au noyau), à distance $\frac{9}{\lVert \mathbf{b} \rVert} = 1$. Pour $\mathbf{y}'$, hors de l'image (la droite de $(2, 5)$), h) est la projection de $\mathbf{y}'$ sur cette image ; la distance minimale est $\lVert \mathbf{y}' - \mathbf{A}\mathbf{A}^+\mathbf{y}' \rVert = \frac{1}{29}\lVert (25, -10) \rVert = \frac{5}{\sqrt{29}} \approx 0{,}93$.

**Erreurs fréquentes.** $\mathbf{A}^+ = \mathbf{A}^\top/s_1$ (une seule puissance) ; une pseudo-inverse de forme $(2, 3)$ ; donner $\mathbf{A}^+$ au lieu de $1\,000\,\mathbf{A}^+$ pour d) ; donner $\mathbf{A}^+\mathbf{y}'$ pour h).

**Variante.** La solution de norme minimale pour $\mathbf{y} = (4, 10)$ ? *Réponse* : $\frac{2}{81}(1, -4, 8)$.

### Ex M12d.7 — Le conditionnement de trois matrices, et l'erreur relative sur une solution

**Réponses** : a) `2.5` · b) `1` · c) `101.9902` · d) `0.102` · e) `[1, 2]` · f) `40.08` · g) `10402.0` · h) `True`.

**Démarche.** a) $\mathbf{P}^\top\mathbf{P} = \operatorname{diag}(4, 25)$ : $s = 5, 2$. b) $\mathbf{Q}$ est orthogonale ($5^2 + 12^2 = 13^2$). c) $s_1^2 + s_2^2 = 102$, $s_1s_2 = \lvert\det\mathbf{R}\rvert = 1$ : $s_1^2$ et $s_2^2$ sont les racines de $x^2 - 102x + 1$, $s_1^2 = 51 + 10\sqrt{26}$, et $\kappa = \frac{s_1}{s_2} = s_1^2 \approx 101{,}99$. d) $\kappa \times 0{,}001$. e) $\mathbf{R}^{-1} = \begin{pmatrix} 2 & -3 \\ -5 & 8 \end{pmatrix}$, $\mathbf{x} = (28 - 27, -70 + 72) = (1, 2)$. f) $\delta\mathbf{x} = \mathbf{R}^{-1}\delta\mathbf{b} = (0{,}02 ;\ -0{,}05)$ : $\frac{0{,}01\sqrt{29}/\sqrt{5}}{0{,}01/\sqrt{277}} = \sqrt{\frac{29 \times 277}{5}} \approx 40{,}08$. g) $\kappa^2 \approx 10\,402$. h) $1\,000\,\mathbf{R}$ a toutes ses valeurs singulières multipliées par 1 000 : même rapport.

Pour la copie : $\kappa + \frac{1}{\kappa} = \frac{s_1}{s_2} + \frac{s_2}{s_1} = \frac{s_1^2 + s_2^2}{s_1s_2} = 102$. f) est sous la borne c), sans l'atteindre : la borne est atteinte quand $\mathbf{b}$ est le long de $\mathbf{u}_1$ (grande image, petite solution) et $\delta\mathbf{b}$ le long de $\mathbf{u}_2$ (la direction la moins étirée, que $\mathbf{R}^{-1}$ amplifie le plus). $\det\mathbf{R} = 1$ et $\det\mathbf{P} = 10$ ne disent rien de la sensibilité : $\mathbf{R}$ est quarante fois plus sensible que $\mathbf{P}$.

**Erreurs fréquentes.** Le rapport des valeurs propres de $\mathbf{R}^\top\mathbf{R}$ ($\kappa^2$) au lieu de $\kappa$ ; juger par le déterminant ; f) avec les erreurs absolues.

**Variante.** $\kappa\begin{pmatrix} 4 & 0 \\ 0 & 0{,}01 \end{pmatrix}$ ? *Réponse* : 400.

### Ex M12d.8 — Les axes principaux d'un nuage de ℝ³ : covariance, polynôme caractéristique, variances et axes

**Réponses** : a) `[14, 9, 6]` · b) `[[19, 0, 4], [0, 11, 0], [4, 0, 4]]` · c) `34` · d) `660` · e) `[20, 11, 3]` · f) `[0.9701, 0, 0.2425]` · g) `[-0.2425, 0, 0.9701]` · h) `15.5`.

**Démarche.** Les données centrées : $(-4, -1, -3)$, $(-5, 5, 1)$, $(1, -5, 3)$, $(-4, -3, -2)$, $(2, 2, 0)$, $(4, 1, 0)$, $(6, 1, 1)$. Sommes de carrés 114, 66 et 24 ; sommes de produits $\sum x_1x_3 = 24$, et 0 pour les deux autres paires ; on divise par 6. Développé selon la deuxième ligne :
$$\det(\mathbf{C} - \lambda\mathbf{I}) = (11 - \lambda)\big[(19 - \lambda)(4 - \lambda) - 16\big] = (11 - \lambda)(\lambda^2 - 23\lambda + 60) = (11 - \lambda)(\lambda - 20)(\lambda - 3).$$
Pour 20 : $\begin{pmatrix} -1 & 4 \\ 4 & -16 \end{pmatrix}$ (sur les mesures 1 et 3) donne $x_1 = 4x_3$, $\mathbf{u}_1 = \frac{1}{\sqrt{17}}(4, 0, 1)$ ; $\mathbf{u}_2 = \mathbf{e}_2$ ; $\mathbf{u}_3 = \frac{1}{\sqrt{17}}(-1, 0, 4)$ (convention). h) $\frac{1}{2}(19 + 4 + 2 \times 4) = 15{,}5$.

Pour la copie : $20 + 11 + 3 = 34$ et $20 \times 11 \times 3 = 660$. Le deuxième axe est $\mathbf{e}_2$ : la deuxième mesure n'est corrélée à aucune autre. h) est un quotient de Rayleigh : il est au plus $\lambda_1$, quelle que soit la direction ; $(1, 0, 1)$ penche trop vers la troisième mesure, la moins dispersée (variance 4), alors que le premier axe $(4, 0, 1)$ suit surtout la première.

**Erreurs fréquentes.** Diviser par $n = 7$ ; oublier de centrer ; lire la variance 19 de la première mesure comme la plus grande variance ; h) avec $(1, 0, 1)$ non normé (31).

**Variante.** La variance le long de $\frac{1}{\sqrt{17}}(1, 0, 4)$ ? *Réponse* : $\frac{19 + 64 + 2 \times 4 \times 4}{17} = \frac{115}{17} \approx 6{,}76$.

### Ex M12d.9 — Scores, reconstruction et erreur de reconstruction moyenne avec deux composantes sur trois

**Réponses** : a) `[6.0634, 1]` · b) `[19.8824, 10, 7.4706]` · c) `[-19, -19, 7, -18, 8, 16, 25]` · d) `20` · e) `19.4029` · f) `2.5714` · g) `12.0` · h) `0.9118`.

**Démarche.** $\mathbf{x}_7 - \boldsymbol{\mu} = (6, 1, 1)$ : $t_{71} = \frac{24 + 1}{\sqrt{17}} = \frac{25}{\sqrt{17}}$, $t_{72} = 1$. b) $\boldsymbol{\mu} + \frac{25}{17}(4, 0, 1) + (0, 1, 0) = \big(14 + \frac{100}{17},\ 10,\ 6 + \frac{25}{17}\big)$. c) $4x_1 + x_3$ sur les objets centrés : $-16 - 3$, $-20 + 1$, $4 + 3$, $-16 - 2$, $8$, $16$, $24 + 1$. d) $\frac{361 + 361 + 49 + 324 + 64 + 256 + 625}{17 \times 6} = \frac{2\,040}{102} = 20 = \lambda_1$. e) $\operatorname{Cov}(t_1, x_1) = \mathbf{u}_1^\top\mathbf{C}\,\mathbf{e}_1 = (\mathbf{C}\mathbf{u}_1) \cdot \mathbf{e}_1 = \lambda_1 u_{11} = \frac{80}{\sqrt{17}}$. f) $\frac{6}{7} \times 3 = \frac{18}{7}$. g) $\frac{6}{7}(11 + 3) = 12$. h) $\frac{31}{34}$.

Pour la copie : les scores de c) ont pour somme 0, et ceux de $\mathbf{u}_2$ (la deuxième mesure centrée, $-1, 5, -5, -3, 2, 1, 1$) donnent $\sum \sqrt{17}\,t_{i1}t_{i2} = 19 - 95 - 35 + 54 + 16 + 16 + 25 = 0$ : covariance nulle. Les scores sur $\mathbf{u}_3$, multipliés par $\sqrt{17}$, sont $-8, 9, 11, -4, -2, -4, -2$ : $\frac{64 + 81 + 121 + 16 + 4 + 16 + 4}{17 \times 7} = \frac{306}{119} = \frac{18}{7}$. Le facteur $\frac{n-1}{n}$ vient de ce que la variance divise par $n - 1$ et l'erreur moyenne par $n$. La deuxième mesure de $\hat{\mathbf{x}}_7$ est restée 10 : $\mathbf{u}_2 = \mathbf{e}_2$ est gardé, et l'axe oublié n'a pas de deuxième coordonnée.

**Erreurs fréquentes.** Les scores de l'objet non centré ; oublier de rajouter $\boldsymbol{\mu}$ ; f) égal à $\lambda_3 = 3$, sans le facteur $\frac{n - 1}{n}$.

**Variante.** L'erreur moyenne avec $k = 3$ ? *Réponse* : 0.

### Ex M12d.10 — La variance expliquée cumulée : combien de composantes pour 95 % ?

**Réponses** : a) `20` · b) `0.48` · c) `[0.48, 0.72, 0.84]` · d) `5` · e) `6` · f) `3.2` · g) `3.1373`.

**Démarche.** Parts cumulées : 0,48 ; 0,72 ; 0,84 ; 0,895 ; 0,93 ; 0,96 ; 0,985 ; 1. f) $1{,}1 + 0{,}7 + 0{,}6 + 0{,}5 + 0{,}3$. g) $\frac{50}{51} \times 3{,}2$.

Pour la copie : le coude est après $k = 3$ (9,6 ; 4,8 ; 2,4 chutent de moitié à chaque pas, puis 1,1 à 0,3 restent petits et comparables) ; sur une échelle logarithmique, où une chute de moitié à chaque pas fait une droite, on le placerait plutôt après $k = 4$ : les deux lectures se défendent, si elles sont justifiées. Le seuil de 90 % en demande 5, celui de 95 % en demande 6 : les seuils gardent aussi des axes de bruit. Si l'ACP prépare un modèle, on règle $k$ en validation (fiche §7).

**Erreurs fréquentes.** Les parts non cumulées ; s'arrêter à 4 pour 90 % (0,895) ; oublier le facteur $\frac{n-1}{n}$.

**Variante.** La part gardée par le coude ? *Réponse* : 84 %.

### Ex M12d.11 — L'ACP par la SVD de la matrice centrée : s² / (n − 1) donne les variances

**Réponses** : a) `[6, 4, 5]` · b) `[[36, 18, 6], [18, 18, 0], [6, 0, 18]]` · c) `[48, 18, 6]` · d) `[6.9282, 4.2426, 2.4495]` · e) `[16, 6, 2]` · f) `[0.8452, 0.5071, 0.169]` · g) `[-0.6343, -0.3416, 0.4392, 0.5367]` · h) `[-4.3948, -2.3664, 3.0426, 3.7187]`.

**Démarche.** $\mathbf{X}_c$ a pour lignes $(-3, -3, -2)$, $(-3, 0, 1)$, $(3, 0, 3)$, $(3, 3, -2)$. c) $\mathbf{X}_c^\top\mathbf{X}_c(5, 3, 1) = (240, 144, 48)$, $(0, -1, 3) \mapsto (0, -18, 54)$, $(-2, 3, 1) \mapsto (-12, 18, 6)$. d) $s = \sqrt{48}, \sqrt{18}, \sqrt{6}$. e) $s^2/3$. f) $\mathbf{v}_1 = \frac{1}{\sqrt{35}}(5, 3, 1)$. h) $\mathbf{X}_c\mathbf{v}_1 = \frac{1}{\sqrt{35}}(-26, -14, 18, 22)$. g) h) divisé par $s_1 = 4\sqrt{3}$.

Pour la copie : h) est de somme nulle, et $\frac{676 + 196 + 324 + 484}{35 \times 3} = 16$. Les quatre lignes centrées ont une somme nulle : $\mathbf{X}_c$ est de rang au plus 3. $s_j^2/n$ donnerait $12$, $4{,}5$ et $1{,}5$ : les variances en $\frac{1}{n}$, incohérentes avec une covariance en $\frac{1}{n-1}$.

**Erreurs fréquentes.** Les valeurs singulières prises pour des variances ; diviser par $n$ ; les scores sur les données non centrées.

**Variante.** Le deuxième axe et sa variance ? *Réponse* : $\frac{1}{\sqrt{10}}(0, -1, 3)$, variance 6.

### Ex M12d.12 — L'ACP quand n < p : passer par la petite matrice XXᵀ

**Réponses** : a) `[5, 6, 3, 4, 7]` · b) `[[22, -6, -16], [-6, 12, -6], [-16, -6, 22]]` · c) `[38, 18, 0]` · d) `[19, 9]` · e) `3` · f) `[0.4588, 0.6882, 0.2294, 0.2294, -0.4588]` · g) `[4.3589, 0, -4.3589]`.

**Démarche.** $\mathbf{X}_c$ a pour lignes $\mathbf{r}_1 = (3, 2, 1, 2, -2)$, $\mathbf{r}_2 = (-2, 2, 0, -2, 0)$, $\mathbf{r}_3 = (-1, -4, -1, 0, 2)$ ; $\mathbf{G}_{ij} = \mathbf{r}_i \cdot \mathbf{r}_j$. $\mathbf{G}(1, 0, -1) = (38, 0, -38)$, $\mathbf{G}(1, -2, 1) = (18, -36, 18)$, $\mathbf{G}(1, 1, 1) = \mathbf{0}$. d) $38/2$ et $18/2$. f) $\mathbf{X}_c^\top(1, 0, -1) = \mathbf{r}_1 - \mathbf{r}_3 = (4, 6, 2, 2, -4)$, de norme $\sqrt{76}$ : $\mathbf{v}_1 = \frac{1}{\sqrt{19}}(2, 3, 1, 1, -2)$. g) $\mathbf{X}_c\mathbf{v}_1 = \sqrt{19}\,(1, 0, -1)$.

Pour la copie : $(1, 1, 1)$ a une valeur propre nulle parce que les lignes centrées ont une somme nulle : $\mathbf{X}_c^\top(1, 1, 1) = \mathbf{0}$. Le deuxième axe : $\mathbf{X}_c^\top(1, -2, 1) = (6, -6, 0, 6, 0)$, soit $\frac{1}{\sqrt{3}}(1, -1, 0, 1, 0)$. Diagonaliser une matrice $3 \times 3$ plutôt que $5 \times 5$ ; pour 500 images de $10^4$ pixels, une matrice $500 \times 500$ plutôt que $10^4 \times 10^4$ (fiche §7 : $10^{12}$ contre quelques $10^9$ opérations).

**Erreurs fréquentes.** Former $\mathbf{X}\mathbf{X}^\top$ sans centrer ; oublier de normer $\mathbf{X}_c^\top\mathbf{w}$ ; diviser par $n$.

**Variante.** La part de variance du premier axe ? *Réponse* : $\frac{19}{28} \approx 0{,}68$.

### Ex M12d.13 — Les probabilités de voisinage de t-SNE sur quatre points, et leur perplexité 2^H

**Réponses** : a) `[1, 2, 3]` · b) `[0.5714, 0.2857, 0.1429]` · c) `1.3788` · d) `2.6005` · e) `0.4` · f) `0.1214` · g) `3`.

**Démarche.** b) Les poids $\frac{1}{2}, \frac{1}{4}, \frac{1}{8}$, de somme $\frac{7}{8}$ : $P_1 = (\frac{4}{7}, \frac{2}{7}, \frac{1}{7})$. c) $H = \sum p\log_2\frac{1}{p} = \frac{4}{7}\log_2\frac{7}{4} + \frac{2}{7}\log_2\frac{7}{2} + \frac{1}{7}\log_2 7 = \log_2 7 - \frac{4 \times 2 + 2 \times 1}{7} = \log_2 7 - \frac{10}{7}$. d) $2^H = 7 \times 2^{-10/7}$. e) Vu de $\mathbf{x}_2$ : carrés des distances 1, 1, 2, poids $\frac{1}{2}, \frac{1}{2}, \frac{1}{4}$, donc $(\frac{2}{5}, \frac{2}{5}, \frac{1}{5})$. f) $\frac{1}{8}\big(\frac{4}{7} + \frac{2}{5}\big) = \frac{17}{140}$. g) Quand $\sigma \to \infty$, tous les poids tendent vers 1 : la loi uniforme sur 3 voisins.

Pour la copie : quand $\sigma \to 0$, tout le poids va au plus proche voisin, la perplexité tend vers 1. Ici elle croît de 1 à 3 avec $\sigma$ : pour atteindre une valeur fixée, on cherche $\sigma$ par dichotomie (il n'y a pas de formule). $p_{2 \mid 1} \ne p_{1 \mid 2}$ parce que chaque point normalise sur **ses** voisins : $\mathbf{x}_2$ a deux voisins proches, qui se partagent sa probabilité.

**Erreurs fréquentes.** Les distances au lieu de leurs carrés ; oublier de normaliser ; l'entropie en nats ; $2n$ oublié dans la symétrisation.

**Variante.** $p_{4 \mid 1}$ si l'on retire $\mathbf{x}_3$ ? *Réponse* : poids $\frac{1}{2}$ et $\frac{1}{8}$ : $\frac{1}{5}$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M12d.14 — Les valeurs singulières sont les racines des valeurs propres de AᵀA

**Réponse modèle.**
1. $(\mathbf{A}^\top\mathbf{A})^\top = \mathbf{A}^\top\mathbf{A}$ ; $\mathbf{x}^\top\mathbf{A}^\top\mathbf{A}\mathbf{x} = (\mathbf{A}\mathbf{x})^\top(\mathbf{A}\mathbf{x}) = \lVert \mathbf{A}\mathbf{x} \rVert^2 \ge 0$. Symétrique : valeurs propres réelles (M12c §6) ; pour un vecteur propre unitaire, $\lambda = \mathbf{v}^\top\mathbf{A}^\top\mathbf{A}\mathbf{v} = \lVert \mathbf{A}\mathbf{v} \rVert^2 \ge 0$.
2. $\mathbf{A}^\top\mathbf{A} = \mathbf{V}\mathbf{S}^\top\mathbf{U}^\top\mathbf{U}\mathbf{S}\mathbf{V}^\top = \mathbf{V}(\mathbf{S}^\top\mathbf{S})\mathbf{V}^\top$, et $\mathbf{S}^\top\mathbf{S} = \operatorname{diag}(s_1^2, \ldots, s_r^2, 0, \ldots, 0)$ de forme $(n, n)$ : une décomposition spectrale, donc $\mathbf{A}^\top\mathbf{A}\mathbf{v}_i = s_i^2\mathbf{v}_i$.
3. $\frac{\mathbf{A}\mathbf{v}_i}{\sqrt{\lambda_i}} \cdot \frac{\mathbf{A}\mathbf{v}_j}{\sqrt{\lambda_j}} = \frac{\mathbf{v}_i^\top\mathbf{A}^\top\mathbf{A}\mathbf{v}_j}{\sqrt{\lambda_i\lambda_j}} = \frac{\lambda_j\,\mathbf{v}_i \cdot \mathbf{v}_j}{\sqrt{\lambda_i\lambda_j}}$, qui vaut 0 si $i \ne j$ et 1 si $i = j$.
4. $\mathbf{A}\mathbf{A}^\top(\mathbf{A}\mathbf{v}) = \mathbf{A}(\mathbf{A}^\top\mathbf{A}\mathbf{v}) = \lambda\,\mathbf{A}\mathbf{v}$, et $\lVert \mathbf{A}\mathbf{v} \rVert^2 = \lambda\lVert \mathbf{v} \rVert^2 \ne 0$ : $\mathbf{A}\mathbf{v}$ est un vecteur propre de $\mathbf{A}\mathbf{A}^\top$, de valeur propre $\lambda$. Le même argument, en échangeant $\mathbf{A}$ et $\mathbf{A}^\top$, donne la réciproque. Si $\mathbf{A}\mathbf{v} = \mathbf{0}$ pour $\mathbf{v}$ dans l'espace propre de $\lambda \ne 0$, alors $\lambda\lVert \mathbf{v} \rVert^2 = 0$, donc $\mathbf{v} = \mathbf{0}$ : $\mathbf{v} \mapsto \mathbf{A}\mathbf{v}$ est injective sur cet espace propre, et sa dimension ne peut que se conserver d'un côté à l'autre (dans les deux sens) : les multiplicités sont égales.
5. $\lVert \mathbf{A} \rVert_F^2 = \operatorname{tr}(\mathbf{A}^\top\mathbf{A})$ (la diagonale de $\mathbf{A}^\top\mathbf{A}$ contient les normes au carré des colonnes), et la trace est la somme des valeurs propres (M12c §2) : $\sum s_i^2$.

**Grille.** (1) symétrie et positivité ; (2) le calcul de $\mathbf{A}^\top\mathbf{A}$ avec $\mathbf{U}^\top\mathbf{U} = \mathbf{I}$, la forme de $\mathbf{S}^\top\mathbf{S}$ ; (3) l'orthonormalité ; (4) les deux sens, la non-nullité de $\mathbf{A}\mathbf{v}$ et l'injectivité (les multiplicités) ; (5) la trace.

### Ex M12d.15 — La plus grande valeur singulière est le plus grand étirement : ‖A x‖ ≤ s₁ ‖x‖

**Réponse modèle.**
1. $\lVert \mathbf{x} \rVert^2 = \sum c_i^2$ (base orthonormée) ; $\mathbf{A}\mathbf{x} = \sum c_i\mathbf{A}\mathbf{v}_i = \sum c_is_i\mathbf{u}_i$ ; les $\mathbf{u}_i$ sont orthonormés (ceux des $s_i = 0$ n'interviennent pas), donc $\lVert \mathbf{A}\mathbf{x} \rVert^2 = \sum s_i^2c_i^2$.
2. $s_n^2\sum c_i^2 \le \sum s_i^2c_i^2 \le s_1^2\sum c_i^2$, puis la racine. Égalité à droite pour $\mathbf{x}$ multiple de $\mathbf{v}_1$ (ou dans l'espace des $\mathbf{v}_i$ tels que $s_i = s_1$), à gauche pour un multiple de $\mathbf{v}_n$.
3. $\frac{\lVert \mathbf{A}\mathbf{x} \rVert^2}{\lVert \mathbf{x} \rVert^2} = \frac{\mathbf{x}^\top(\mathbf{A}^\top\mathbf{A})\mathbf{x}}{\mathbf{x}^\top\mathbf{x}}$, le quotient de Rayleigh de $\mathbf{A}^\top\mathbf{A}$, entre sa plus petite et sa plus grande valeur propre, $s_n^2$ et $s_1^2$ (M12c §6).
4. L'inégalité de droite de 2. ne demande pas $n \le m$ (seule celle de gauche en a besoin) : $\lVert \mathbf{A}\mathbf{B}\mathbf{x} \rVert \le \lVert \mathbf{A} \rVert_2\lVert \mathbf{B}\mathbf{x} \rVert \le \lVert \mathbf{A} \rVert_2\lVert \mathbf{B} \rVert_2\lVert \mathbf{x} \rVert$ ; la plus grande valeur du rapport $\lVert \mathbf{A}\mathbf{B}\mathbf{x} \rVert/\lVert \mathbf{x} \rVert$ est $\lVert \mathbf{A}\mathbf{B} \rVert_2$.
5. $\lVert \mathbf{Q} \rVert_2 = 1$ (toutes ses valeurs singulières valent 1) ; $\lVert \mathbf{Q}\mathbf{A}\mathbf{x} \rVert = \lVert \mathbf{A}\mathbf{x} \rVert$, donc $\lVert \mathbf{Q}\mathbf{A} \rVert_2 = \lVert \mathbf{A} \rVert_2$.

**Grille.** (1) la décomposition dans la base des $\mathbf{v}_i$ et Pythagore ; (2) l'encadrement et les cas d'égalité ; (3) le quotient de Rayleigh de $\mathbf{A}^\top\mathbf{A}$ ; (4) les deux inégalités enchaînées et le passage au maximum ; (5) l'invariance par une matrice orthogonale.

### Ex M12d.16 — L'erreur de l'approximation de rang k vaut la somme des s² oubliés (Frobenius)

**Réponse modèle.**
1. La diagonale de $\mathbf{M}^\top\mathbf{M}$ contient $\sum_i m_{ij}^2$ pour chaque colonne $j$ : sa trace est $\sum_{i,j} m_{ij}^2$. Puis $\lVert \mathbf{Q}\mathbf{M} \rVert_F^2 = \operatorname{tr}(\mathbf{M}^\top\mathbf{Q}^\top\mathbf{Q}\mathbf{M}) = \operatorname{tr}(\mathbf{M}^\top\mathbf{M})$.
2. $\lVert \mathbf{M}\mathbf{Q} \rVert_F^2 = \operatorname{tr}(\mathbf{Q}^\top\mathbf{M}^\top\mathbf{M}\mathbf{Q}) = \operatorname{tr}(\mathbf{M}^\top\mathbf{M}\mathbf{Q}\mathbf{Q}^\top) = \operatorname{tr}(\mathbf{M}^\top\mathbf{M})$.
3. $\mathbf{A} - \mathbf{A}_k = \sum_{i > k} s_i\mathbf{u}_i\mathbf{v}_i^\top = \mathbf{U}\mathbf{D}\mathbf{V}^\top$, où $\mathbf{D}$ est $\mathbf{S}$ dont les $k$ premières valeurs sont mises à zéro. Par 1. et 2., $\lVert \mathbf{A} - \mathbf{A}_k \rVert_F^2 = \lVert \mathbf{D} \rVert_F^2 = s_{k+1}^2 + \cdots + s_r^2$.
4. $\mathbf{A} - \mathbf{A}_k = \mathbf{U}\mathbf{D}\mathbf{V}^\top$ est une SVD (une fois les valeurs rangées) : sa plus grande valeur singulière est $s_{k+1}$, qui est sa norme spectrale (M12d.15).
5. $\lVert \mathbf{A}_k \rVert_F^2 = \sum_{i \le k} s_i^2$ (même raisonnement) : la somme fait $\sum_i s_i^2 = \lVert \mathbf{A} \rVert_F^2$. C'est Pythagore pour le produit scalaire $\operatorname{tr}(\mathbf{X}^\top\mathbf{Y})$, les deux matrices $\mathbf{A}_k$ et $\mathbf{A} - \mathbf{A}_k$ étant orthogonales entre elles : $\operatorname{tr}\big(\mathbf{A}_k^\top(\mathbf{A} - \mathbf{A}_k)\big) = \sum_{i \le k < j} s_is_j\,(\mathbf{u}_i \cdot \mathbf{u}_j)(\mathbf{v}_i \cdot \mathbf{v}_j) = 0$ : $\mathbf{A}_k$ et $\mathbf{A} - \mathbf{A}_k$ sont orthogonales.

**Grille.** (1) la trace et l'invariance à gauche ; (2) l'invariance à droite, par la permutation circulaire ; (3) l'écriture de $\mathbf{A} - \mathbf{A}_k$ et la conclusion ; (4) la norme spectrale ; (5) Pythagore et l'orthogonalité des deux matrices, calculée.

### Ex M12d.17 — La pseudo-inverse donne la solution des moindres carrés de plus petite norme

**Réponse modèle.**
1. $\mathbf{A}\mathbf{x} - \mathbf{b} = \mathbf{U}(\mathbf{S}\mathbf{V}^\top\mathbf{x} - \mathbf{U}^\top\mathbf{b}) = \mathbf{U}(\mathbf{S}\mathbf{y} - \mathbf{c})$, et $\mathbf{U}$ conserve les normes ; la coordonnée $i$ de $\mathbf{S}\mathbf{y}$ vaut $s_iy_i$ pour $i \le r$ et 0 au-delà. De même $\lVert \mathbf{x} \rVert = \lVert \mathbf{V}\mathbf{y} \rVert = \lVert \mathbf{y} \rVert$.
2. Le second terme ne dépend pas de $\mathbf{y}$ ; le premier est nul, donc minimal, si et seulement si $y_i = c_i/s_i$ pour $i \le r$. Les $y_i$ pour $i > r$ sont libres (ils décrivent le noyau).
3. $\lVert \mathbf{y} \rVert^2 = \sum_{i \le r} (c_i/s_i)^2 + \sum_{i > r} y_i^2$ est minimal pour $y_i = 0$ au-delà de $r$ : $\mathbf{y} = \mathbf{S}^+\mathbf{c}$, avec $\mathbf{S}^+$ de forme $(n, m)$, de diagonale $1/s_1, \ldots, 1/s_r$ et des zéros ailleurs. Donc $\mathbf{x}^+ = \mathbf{V}\mathbf{S}^+\mathbf{U}^\top\mathbf{b} = \sum_{i \le r}\frac{1}{s_i}\mathbf{v}_i\mathbf{u}_i^\top\mathbf{b} = \mathbf{A}^+\mathbf{b}$.
4. $\sum_{i > r} c_i^2 = \sum_{i > r}(\mathbf{u}_i \cdot \mathbf{b})^2$ : le carré de la distance de $\mathbf{b}$ à l'image de $\mathbf{A}$. Nul si et seulement si $\mathbf{b}$ est dans l'image (le système a des solutions).
5. Rang $n$ : $\mathbf{A}^\top\mathbf{A} = \mathbf{V}\mathbf{S}_n^2\mathbf{V}^\top$ est inversible, et $(\mathbf{A}^\top\mathbf{A})^{-1}\mathbf{A}^\top = \mathbf{V}\mathbf{S}_n^{-2}\mathbf{V}^\top\mathbf{V}\mathbf{S}^\top\mathbf{U}^\top = \mathbf{V}\mathbf{S}^+\mathbf{U}^\top$ (avec $\mathbf{S}_n = \operatorname{diag}(s_1, \ldots, s_n)$).

**Grille.** (1) les deux normes conservées ; (2) le minimum et les coordonnées libres ; (3) le choix de norme minimale et la forme de $\mathbf{S}^+$ ; (4) le résidu et son interprétation ; (5) les équations normales retrouvées.

### Ex M12d.18 — L'erreur de reconstruction moyenne est la somme des variances oubliées

**Réponse modèle.**
1. Les $\mathbf{u}_j$ forment une base orthonormée de $\mathbb{R}^p$ : $\mathbf{x}_i - \boldsymbol{\mu} = \sum_j (\mathbf{u}_j \cdot (\mathbf{x}_i - \boldsymbol{\mu}))\,\mathbf{u}_j = \sum_j t_{ij}\mathbf{u}_j$ (M12b §2). Donc $\mathbf{x}_i - \hat{\mathbf{x}}_i = \sum_{j > k} t_{ij}\mathbf{u}_j$, de norme au carré $\sum_{j > k} t_{ij}^2$ (Pythagore).
2. Les scores sont de moyenne nulle ($\frac{1}{n}\sum_i \mathbf{u}_j^\top(\mathbf{x}_i - \boldsymbol{\mu}) = \mathbf{u}_j^\top(\boldsymbol{\mu} - \boldsymbol{\mu}) = 0$), donc leur variance est $\frac{1}{n - 1}\sum_i t_{ij}^2$ ; par M12c §8, elle vaut $\mathbf{u}_j^\top\mathbf{C}\mathbf{u}_j$, et $\mathbf{C}\mathbf{u}_j = \lambda_j\mathbf{u}_j$ avec $\lVert \mathbf{u}_j \rVert = 1$ donne $\mathbf{u}_j^\top\mathbf{C}\mathbf{u}_j = \lambda_j$ : $\sum_i t_{ij}^2 = (n - 1)\lambda_j$.
3. $\frac{1}{n}\sum_i\sum_{j > k} t_{ij}^2 = \frac{1}{n}\sum_{j > k}(n - 1)\lambda_j$.
4. $\hat{\mathbf{x}}_i - \boldsymbol{\mu} = \sum_{j \le k} t_{ij}\mathbf{u}_j$, et le même calcul donne $\frac{n-1}{n}\sum_{j \le k}\lambda_j$. La somme des deux vaut $\frac{n-1}{n}\sum_j\lambda_j = \frac{n-1}{n}\operatorname{tr}\mathbf{C}$ : la dispersion moyenne $\frac{1}{n}\sum\lVert \mathbf{x}_i - \boldsymbol{\mu} \rVert^2$, partagée entre ce que l'on garde et ce que l'on perd.
5. L'erreur est $\frac{n-1}{n}$ fois la somme des $p - k$ variances oubliées : elle est la plus petite quand on oublie les plus petites, c'est-à-dire quand on garde les $k$ premiers axes.

**Grille.** (1) la décomposition dans la base orthonormée et Pythagore ; (2) la moyenne nulle, qui fait de la variance la somme des carrés divisée par $n - 1$, la règle de M12c §8 et le vecteur propre unitaire ; (3) l'échange des sommes ; (4) le partage de la variance totale ; (5) l'argument sur les variances oubliées.

### Ex M12d.19 — Les scores de deux composantes principales sont décorrélés

**Réponse modèle.**
1. La ligne $j$ de $\mathbf{W}_k^\top$ est $\mathbf{u}_j^\top$ et la colonne $l$ de $\mathbf{W}_k$ est $\mathbf{u}_l$ : le coefficient $(j, l)$ est $\mathbf{u}_j^\top\mathbf{C}\mathbf{u}_l$. Or $\mathbf{C}\mathbf{u}_l = \lambda_l\mathbf{u}_l$, donc $\mathbf{u}_j^\top\mathbf{C}\mathbf{u}_l = \lambda_l\,\mathbf{u}_j \cdot \mathbf{u}_l$, qui vaut $\lambda_l$ si $j = l$ et 0 sinon (axes orthonormés) : $\frac{1}{n-1}\mathbf{Z}^\top\mathbf{Z} = \operatorname{diag}(\lambda_1, \ldots, \lambda_k)$.
2. Par la même règle, avec la ligne $\mathbf{a}^\top$ : $\mathbf{a}^\top\operatorname{diag}(\lambda_1, \ldots, \lambda_k)\,\mathbf{a} = \sum_j a_j^2\lambda_j$. Les scores étant décorrélés, les variances s'ajoutent, sans termes croisés.
3. $\frac{1}{169}(5, 12)\begin{pmatrix} 4 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} -12 \\ 5 \end{pmatrix} = \frac{-240 + 60}{169} = -\frac{180}{169} \ne 0$. En 1., on a utilisé que $\mathbf{u}_l$ est un **vecteur propre** de $\mathbf{C}$ ; deux directions orthogonales quelconques ne le sont pas.

**Grille.** (1) le coefficient $(j, l)$ comme forme bilinéaire $\mathbf{u}_j^\top\mathbf{C}\mathbf{u}_l$, le vecteur propre, puis l'orthogonalité, et la matrice diagonale ; (2) la variance d'une combinaison, sans termes croisés ; (3) le contre-exemple calculé et ce qu'il montre.

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M12d.20 — Pont : détecter une anomalie par son erreur de reconstruction

**Réponses** : a) `0` · b) `9.9412` · c) `7.1176` · d) `True` · e) `16.4924` · f) `6.0634` · g) `False`.

**Démarche.** Avec $k = 2$, l'erreur est le carré du score sur $\mathbf{u}_3 = \frac{1}{\sqrt{17}}(-1, 0, 4)$. a) $\mathbf{r}_1 - \boldsymbol{\mu} = (4, 3, 1)$ : $-4 + 4 = 0$. b) $\mathbf{r}_2 - \boldsymbol{\mu} = (-1, 0, 3)$ : $\frac{(1 + 12)^2}{17} = \frac{169}{17}$. c) Les sept scores sur $\mathbf{u}_3$ (M12d.9) : le plus grand en valeur absolue est $\frac{11}{\sqrt{17}}$, d'erreur $\frac{121}{17}$. d) $9{,}94 > 7{,}12$. e) $\mathbf{r}_3 - \boldsymbol{\mu} = (16, 0, 4) = 4\,(4, 0, 1)$ : $t_1 = 4\sqrt{17}$. f) $\frac{25}{\sqrt{17}}$ (l'objet 7). g) $\mathbf{r}_3 - \boldsymbol{\mu}$ est le long de $\mathbf{u}_1$ : erreur nulle.

Pour la copie : $\mathbf{r}_2$ combine une première mesure basse et une troisième haute, alors que dans les données elles varient ensemble (la covariance 4 et l'axe $(4, 0, 1)$) : c'est la **combinaison** qui est inhabituelle. $\mathbf{r}_3$ est dans le plan des deux premiers axes, mais très loin le long de $\mathbf{u}_1$ ($t_1 \approx 16{,}5$ contre au plus 6,1) : l'erreur de reconstruction ne voit que ce qui sort du sous-espace. Un second score, la distance dans le plan mesurée en écarts-types, $\frac{t_1^2}{\lambda_1} + \frac{t_2^2}{\lambda_2}$ (environ 13,6 pour $\mathbf{r}_3$, au plus 3,3 pour les sept objets), le signale. Le seuil fixé sur les données d'entraînement est optimiste (fiche §7, ⚠️) : sur des données que l'ACP n'a pas vues, les erreurs normales sont en moyenne plus grandes, et l'on signalerait trop.

**Erreurs fréquentes.** L'erreur comme distance (sans le carré) ; comparer à l'erreur moyenne au lieu de la plus grande ; le score de $\mathbf{r}_3$ sans centrer.

**Variante.** L'erreur de $(14, 12, 10)$ ? *Réponse* : $\mathbf{r} - \boldsymbol{\mu} = (0, 3, 4)$, $\frac{16^2}{17} \approx 15{,}06$ : signalé.

### Ex M12d.21 — Pont : un changement d'unités diagonal D change Σ en DΣD, et les axes principaux avec ; la standardisation non

**Réponses** : a) `[[19, 0, 12], [0, 11, 0], [12, 0, 36]]` · b) `[42.2054, 12.7946, 11.0]` · c) `[0.4593, 0, 0.8883]` · d) `0.6395` · e) `0.4588` · f) `48.6` · g) `[[1, 0, 0.4588], [0, 1, 0], [0.4588, 0, 1]]` · h) `True`.

**Démarche.** a) $c_{33}$ multiplié par 9, $c_{13}$ par 3. b) Le bloc $\begin{pmatrix} 19 & 12 \\ 12 & 36 \end{pmatrix}$ : trace 55, déterminant 540, $\lambda = \frac{55 \pm \sqrt{865}}{2}$ ; la variance 11 reste. c) Pour $\lambda_1 \approx 42{,}21$ : $-23{,}21\,x_1 + 12\,x_3 = 0$, normé. d) $\frac{42{,}21}{19 + 11 + 36}$. e) $\frac{4}{\sqrt{19 \times 4}} = \frac{2}{\sqrt{19}}$. f) $\cos\theta = \frac{1}{\sqrt{17}}(4 \times 0{,}4593 + 0{,}8883) \approx 0{,}661$, $\theta \approx 48{,}6°$. g) La matrice de corrélation.

Pour la copie : après le changement, $\frac{12}{\sqrt{19 \times 36}} = \frac{2}{\sqrt{19}}$, la même corrélation. $(\mathbf{D}\boldsymbol{\Sigma}\mathbf{D})_{ij} = \sum_{k,l} d_{ik}\Sigma_{kl}d_{lj} = d_id_j\Sigma_{ij}$ ($\mathbf{D}$ diagonale), donc $\frac{d_id_j\Sigma_{ij}}{\sqrt{d_i^2\Sigma_{ii}\,d_j^2\Sigma_{jj}}} = \frac{\Sigma_{ij}}{\sqrt{\Sigma_{ii}\Sigma_{jj}}}$ pour $d_i, d_j > 0$ : la matrice de corrélation, donc l'ACP standardisée, ne dépend pas des unités. Le premier axe est passé de $(0{,}97 ;\ 0 ;\ 0{,}24)$ à $(0{,}46 ;\ 0 ;\ 0{,}89)$ : c'est l'**unité** qui a décidé.

**Erreurs fréquentes.** Multiplier $c_{33}$ par 3 au lieu de 9 ; la corrélation avec les anciens écarts-types après le changement ; un angle en radians ; les axes de la standardisation confondus avec ceux de la covariance.

**Variante.** Et si l'on divisait la première mesure par 2 (unité deux fois plus grande) ? *Réponse* : $\begin{pmatrix} 4{,}75 & 0 & 2 \\ 0 & 11 & 0 \\ 2 & 0 & 4 \end{pmatrix}$ : le premier axe devient $\mathbf{e}_2$, de variance 11.

### Ex M12d.22 — MML §4.5 à §4.7 : SVD, approximation de rang faible, phylogénie des matrices

**Réponse modèle** (avec tes mots ; les tiens peuvent différer).
1. Le théorème dit que toute matrice rectangulaire réelle s'écrit comme le produit d'une matrice orthogonale, d'une matrice « diagonale » de nombres positifs et de la transposée d'une autre matrice orthogonale. Le livre note $\boldsymbol{\Sigma}$ cette matrice et $\sigma_i$ ses valeurs ; quand la matrice n'est pas carrée, $\boldsymbol{\Sigma}$ a sa forme, avec la sous-matrice diagonale complétée de lignes ou de colonnes nulles. La fiche écrit $\mathbf{S}$ et $s_i$, et garde $\boldsymbol{\Sigma}$ pour les covariances.
2. Un changement de base dans l'espace de départ ($\mathbf{V}^\top$), une mise à l'échelle des axes avec, au besoin, un ajout ou une suppression de dimensions ($\boldsymbol{\Sigma}$), puis un changement de base dans l'espace d'arrivée ($\mathbf{U}$). Avec M12d.3 : $\mathbf{v}_1 = \frac{1}{\sqrt{65}}(-1, 8)$ est amené sur $\mathbf{e}_1$, étiré de 9, puis envoyé sur $9\,\mathbf{u}_1$.
3. Il diagonalise d'abord $\mathbf{A}^\top\mathbf{A}$ (symétrique semi-définie positive, donc diagonalisable dans une base orthonormée), en déduit les vecteurs singuliers à droite et les valeurs singulières (des racines), puis obtient ceux de gauche en appliquant $\mathbf{A}$ et en normant. C'est la recette de la fiche §1.
4. La SVD existe pour toute matrice, même rectangulaire ; la décomposition en éléments propres seulement pour certaines matrices carrées. Les bases de la SVD sont orthonormées, celles de la décomposition en éléments propres en général non (sauf pour une matrice symétrique). La SVD a deux bases (départ, arrivée), la décomposition en éléments propres une seule. Les valeurs singulières sont positives, les valeurs propres de signe quelconque, voire complexes. Pour une matrice symétrique semi-définie positive, les deux coïncident.
5. Dans le livre, les films sont en lignes et les spectateurs en colonnes : les vecteurs singuliers à gauche décrivent des « films types » (des genres), ceux de droite des « spectateurs types » (des goûts), et chaque valeur singulière le poids de la couche qui relie un film type à un spectateur type. Dans M12d.4, les clients sont en lignes : les rôles s'échangent. $\mathbf{u}_1 \propto (4, 4, 3)$ décrit les clients (les trois partagent un même goût, les deux premiers un peu plus que le troisième), $\mathbf{v}_1 \propto (5, 4, 0)$ les produits (ce goût porte sur les produits 1 et 2), et $s_1 = 7$ en est la force.
6. La norme spectrale est le plus grand étirement $\max \lVert \mathbf{A}\mathbf{x} \rVert/\lVert \mathbf{x} \rVert$, qui vaut $\sigma_1$. Le livre énonce Eckart-Young dans cette norme : la troncature est la meilleure approximation de rang $k$, à distance $\sigma_{k+1}$. La fiche §3 l'énonce en norme de Frobenius (erreur au carré $\sum_{i > k} s_i^2$), où le même $\mathbf{A}_k$ est aussi le meilleur.
7. Les matrices carrées se partagent en inversibles et non inversibles ; parmi les diagonalisables, les symétriques (décomposition spectrale, bases orthonormées), dont les définies positives (Cholesky) ; les orthogonales sont un cas à part (inversibles, valeurs singulières 1) ; la SVD, elle, s'applique à toutes, carrées ou non.
8. Par exemple : *singular value decomposition* (décomposition en valeurs singulières), *left/right-singular vectors* (vecteurs singuliers à gauche, à droite), *rank-k approximation* (approximation de rang $k$), *spectral norm* (norme spectrale).

**Grille.** (1) l'énoncé et les notations reliées à la fiche ; (2) les trois étapes, refaites sur M12d.3 ; (3) la construction par $\mathbf{A}^\top\mathbf{A}$ ; (4) au moins trois différences ; (5) l'interprétation, refaite sur M12d.4 ; (6) la norme spectrale, Eckart-Young et les deux normes ; (7) l'arbre et les décompositions placées ; (8) trois mots traduits.

### Ex M12d.23 — MML §10.1 à §10.6 : l'ACP du livre (la dérivation par Lagrange de §10.2 se survole : M13b la relit)

**Réponse modèle** (avec tes mots).
1. Trouver une projection des données sur un sous-espace de dimension plus petite qui garde le plus d'information possible. Les exemples sont les **colonnes** de $\mathbf{X}$ ($D \times N$), et la covariance divise par $N$. Pour traduire : transposer ($\mathbf{X}$ du livre $= \mathbf{X}_c^\top$ de la fiche, si les données sont centrées), et passer de $\frac{1}{N}$ à $\frac{1}{n - 1}$ (les variances du livre valent $\frac{n-1}{n}$ fois celles de la fiche ; les axes ne changent pas).
2. Chercher la direction unitaire qui maximise la variance des données projetées. La dérivation aboutit à une équation aux valeurs propres, $\mathbf{S}\mathbf{b} = \lambda\mathbf{b}$, et la variance obtenue est $\lambda$ : il faut prendre la plus grande. La fiche (§5) y arrive par le quotient de Rayleigh de M12c, sans multiplicateur.
3. Par récurrence : on retire des données ce qu'expliquent les axes déjà trouvés, et l'on cherche l'axe de plus grande variance du reste ; on obtient le vecteur propre suivant. La fiche dit la même chose : le maximum parmi les directions orthogonales aux premières.
4. Chercher le sous-espace qui rend la distance moyenne entre les données et leurs projections la plus petite. On retrouve les mêmes axes, et l'erreur minimale est la somme des valeurs propres oubliées (au facteur $\frac{n-1}{n}$ près dans les conventions de la fiche, comme en M12d.18).
5. Les axes principaux sont les vecteurs singuliers (à gauche, dans ses conventions en colonnes) de la matrice des données centrées, et les variances les carrés des valeurs singulières divisés par $N$ ; la projection est l'approximation de rang faible de §4.6, et le livre cite des méthodes itératives (la puissance) quand on ne veut que les premiers axes.
6. Quand $N < D$, on diagonalise la petite matrice $N \times N$ (le produit des données dans l'autre sens) et l'on remonte aux axes en multipliant par la matrice des données, puis en normant : c'est M12d.12.
7. Centrer (retirer la moyenne), standardiser (diviser par l'écart-type de chaque dimension, pour ne pas dépendre des unités), diagonaliser la covariance, projeter, puis revenir dans l'espace d'origine (déstandardiser, rajouter la moyenne). La fiche (§6) ne standardise que si les features ont des unités différentes.
8. Par exemple : *principal subspace* (sous-espace principal), *reconstruction error* (erreur de reconstruction), *data covariance matrix* (matrice de covariance des données), *mean subtraction* (centrage).

**Grille.** (1) le problème et la traduction des conventions ; (2) la variance maximale et le lien avec le quotient de Rayleigh ; (3) les axes suivants ; (4) le point de vue de la projection et M12d.18 ; (5) le lien avec la SVD ; (6) la grande dimension et M12d.12 ; (7) les étapes et la standardisation ; (8) trois mots traduits.

### Ex M12d.24 — Fermi : la mémoire et le temps d'une ACP sur un million de clients et 250 features

**Réponse modèle.**
1. $10^6 \times 250 \times 8 = 2 \times 10^9$ octets : 2 Go ; 1 Go en `float32`.
2. $10^6 \times 250^2 = 6{,}25 \times 10^{10}$ opérations : environ 6 secondes.
3. $250^2 = 62\,500$ nombres, 0,5 Mo ; sa diagonalisation, environ $1{,}6 \times 10^8$ opérations : quelques centièmes de seconde. La matrice de covariance n'est pas le problème ; c'est de lire les données.
4. Pour la précision : $\kappa(\mathbf{X}_c^\top\mathbf{X}_c) = \kappa(\mathbf{X}_c)^2$, et les petites variances (souvent celles qui comptent pour détecter des redondances) sont mal calculées par la covariance (🔬 M12d.33). Le temps reste du même ordre (quelques dizaines de secondes).
5. $10^6 \times 20 \times 8 = 1{,}6 \times 10^8$ octets : 160 Mo.
6. Deux lectures : la première accumule $n$ et $\sum\mathbf{x}_i$ pour obtenir $\boldsymbol{\mu}$ ; la seconde accumule, morceau par morceau, la matrice $250 \times 250$ $\sum(\mathbf{x}_i - \boldsymbol{\mu})(\mathbf{x}_i - \boldsymbol{\mu})^\top$, puis divise par $n - 1$. La formule en une lecture, $\sum\mathbf{x}_i\mathbf{x}_i^\top - n\boldsymbol{\mu}\boldsymbol{\mu}^\top$, soustrait deux grands nombres presque égaux quand la moyenne est grande devant les écarts : elle perd des chiffres (il existe des mises à jour en une lecture plus stables, en combinant les moyennes et les covariances de morceaux).

**Grille.** (1) la mémoire en `float64` et en `float32` ; (2) $np^2$ et le temps ; (3) la petite matrice, et l'étape qui coûte vraiment ; (4) l'argument du conditionnement ; (5) les scores ; (6) les deux lectures, et le piège de la soustraction.

### Ex M12d.25 — Expliquer la SVD comme « rotation, étirement, rotation »

**Réponse modèle.**

> Imagine ton logo dessiné sur une feuille de caoutchouc. Toute transformation « linéaire » de la feuille se fait en trois gestes. D'abord, tu fais tourner la feuille (ou tu la retournes) pour aligner deux directions perpendiculaires bien choisies sur l'horizontale et la verticale. Ensuite, tu tires sur la feuille le long de ces deux axes, plus fort le long de l'un que de l'autre : ces deux facteurs d'étirement sont les valeurs singulières. Enfin, tu fais tourner le résultat pour le poser là où il doit aller. Un cercle tracé sur la feuille devient une ellipse, dont le grand axe et le petit axe viennent de deux diamètres perpendiculaires du cercle. Si un facteur vaut zéro, la feuille est écrasée sur une droite : l'ellipse devient un segment, et une direction est perdue.

**Grille.** (1) les trois étapes, dans l'ordre ; (2) le cercle qui devient une ellipse, et ses axes qui viennent de deux diamètres perpendiculaires ; (3) les valeurs singulières comme facteurs d'étirement ; (4) une valeur nulle qui écrase ; huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M12d.E1 — « Comment choisissez-vous le nombre de composantes d'une ACP ? »

**Réponse modèle (60 secondes).**

> Chaque composante explique une part de la variance totale : sa valeur propre divisée par la somme de toutes. Le réflexe est de tracer la part cumulée et de fixer un seuil, 90 ou 95 % ; c'est rapide, mais arbitraire, et le seuil garde aussi des axes de bruit. On regarde aussi le coude de la courbe des variances : là où elle cesse de chuter, les composantes suivantes sont petites et comparables, souvent du bruit. Mais quand l'ACP prépare un modèle, le bon nombre est un hyperparamètre : je le choisis par validation croisée, sur la performance du modèle qui suit, en ne calculant les axes que sur les données d'entraînement pour éviter une fuite. Enfin, l'erreur de reconstruction donne une autre lecture : avec k composantes, l'erreur moyenne est la somme des variances oubliées ; si l'ACP sert à compresser ou à détecter des anomalies, je choisis k sur cette erreur, mesurée sur des données que l'ACP n'a pas vues.

**Grille.** (1) la définition de la variance expliquée ; (2) le seuil et ses limites ; (3) le coude ; (4) la validation quand l'ACP prépare un modèle, les axes sur l'entraînement seulement ; (5) l'erreur de reconstruction.

### M12d.E2 — « Que dit le conditionnement d'une matrice ? »

**Réponse modèle (60 secondes).**

> Le conditionnement est le rapport entre la plus grande et la plus petite valeur singulière : il dit à quel point la matrice aplatit l'espace. Il borne l'amplification des erreurs : une erreur relative sur le second membre d'un système peut devenir κ fois plus grande sur la solution ; on perd environ log₁₀ κ chiffres significatifs, et avec des flottants à 16 chiffres, un κ de 10¹² n'en laisse que 4. Le déterminant ne le mesure pas : une matrice de déterminant 1 peut être très mal conditionnée, et 0,1 fois l'identité a un déterminant minuscule mais un κ de 1. Un piège classique : former AᵀA, comme dans les équations normales, élève κ au carré ; c'est pourquoi on résout les moindres carrés par QR ou par la SVD. En machine learning, des features presque redondantes rendent XᵀX mal conditionnée : les poids d'une régression deviennent instables, et la régularisation ridge, en ajoutant α à chaque valeur propre, réduit κ. Le conditionnement de la hessienne règle aussi la vitesse d'une descente de gradient.

**Grille.** (1) la définition par les valeurs singulières ; (2) l'amplification et les chiffres perdus ; (3) le déterminant n'est pas le bon critère ; (4) le piège de $\kappa^2$ ; (5) un exemple en machine learning.

<a id="notebook"></a>

## Notebook

### Ex M12d.26 — La SVD par les valeurs propres de AᵀA · `svd`

**Réponses** : a) `[5.23835, 2.56119]` · b) `[[0.227908, 0.954492, 0.192361], [-0.6265, -0.00748, 0.779385]]` · c) `True` · d) `1` · e) `"((3, 3), (3,), (3, 5))"` · f) `"ValueError"` · g) `True`.

**Démarche.** `M = np.array(A, dtype=float)` (une `ValueError` si `M.ndim != 2`) ; `values, vectors = np.linalg.eigh(M.T @ M)` ; `order = np.argsort(values)[::-1]` ; `s = np.sqrt(np.clip(values[order], 0, None))` ; `r = int(np.sum(s > tol * s[0]))` (0 pour une matrice nulle) ; `V = vectors[:, order][:, :r]`, chaque colonne multipliée par le signe de sa coordonnée de plus grande valeur absolue ; `U = (M @ V) / s[:r]`. Pour la copie : $\mathbf{A}\mathbf{A}^\top = \begin{pmatrix} 14 & 10 \\ 10 & 20 \end{pmatrix}$, trace 34, déterminant 180, $\lambda = 17 \pm \sqrt{109}$ : $s \approx 5{,}238$ et $2{,}561$ (M12d.14, 4.) ; d) $\mathbf{A} = (1, 2, -1)^\top(1, -3)$, de rang 1, $s_1 = \sqrt{6 \times 10} = \sqrt{60}$, et la seconde valeur propre de $\mathbf{A}^\top\mathbf{A}$ n'est qu'un arrondi sous le seuil.

**Erreurs fréquentes.** Oublier l'écrêtage (`nan` pour un $-10^{-17}$) ; réordonner les valeurs sans les colonnes ; la convention appliquée aux lignes de `vectors` ; `>=` au lieu de `>` ; diviser `M @ V` par une matrice diagonale au lieu de `s`.

### Ex M12d.27 — Approximation de rang faible et conditionnement · `low_rank_approximation, condition_number`

**Réponses** : a) `[[3.843909, 1.855815, -1.108465], [1.421954, 0.686511, -0.410048]]` · b) `True` · c) `112.4911` · d) `True` · e) `"ValueError"` · f) `"ValueError"` · g) `True`.

**Démarche.** `low_rank_approximation` : un contrôle de `k` (entier, pas `bool`, entre 0 et $\min(m, n)$), `U, s, Vt = svd(A)`, puis `(U[:, :k] * s[:k]) @ Vt[:k]`. `condition_number` : une `ValueError` si la matrice est nulle, `math.inf` si `len(s) < min(m, n)`, sinon `float(s[0] / s[-1])`. Pour la copie : c) $s_1^2 + s_2^2 = 56{,}25$, $s_1s_2 = 0{,}5$, donc $s_1^2 \approx 56{,}2456$, $s_2^2 \approx 0{,}0044$ et $\kappa \approx 112{,}49$ ; d) les lignes $(3, -6)$ et $(-1, 2)$ sont proportionnelles ; le rang plein redonne $\mathbf{A}$ aux arrondis près, $\mathbf{U}$ venant d'une division.

**Erreurs fréquentes.** Accepter `k=True` ou `k=1.0` ; rendre un `np.float64` ; comparer `len(s)` au rang au lieu de $\min(m, n)$.

### Ex M12d.28 — La pseudo-inverse · `pinv`

**Réponses** : a) `[[0.4, 0.0], [0.0, 0.333333], [0.2, 0.0]]` · b) `True` · c) `True` · d) `"(3, 2)"` · e) `[0.0, 100000000.0]` · f) `"ValueError"`.

**Démarche.** `U, s, Vt = svd(A, tol=rcond)`, puis `(Vt.T / s) @ U.T`, de forme $(n, m)$ même quand `s` est vide. Pour la copie : les lignes de $\mathbf{A}$ sont orthogonales, $\mathbf{A}\mathbf{A}^\top = \operatorname{diag}(5, 9)$ et $\mathbf{A}^+ = \mathbf{A}^\top\operatorname{diag}(\frac{1}{5}, \frac{1}{9})$ ; $\mathbf{A}\mathbf{A}^+ = \mathbf{I}_2$. e) Avec le seuil par défaut, $10^{-8}$ est traité comme nul ; avec `rcond=1e-10`, il est inversé en $10^8$. Si $10^{-8}$ est une erreur de mesure, le seuil l'empêche d'être amplifiée cent millions de fois.

**Erreurs fréquentes.** Rendre la transposée ; multiplier par `s` au lieu de diviser ; oublier de passer `rcond` à `svd`.

### Ex M12d.29 — Les axes principaux d'une matrice de covariance, et la variance expliquée · `principal_axes, explained_variance_ratio`

**Réponses** : a) `[[-0.514496, 0.0, 0.857493], [0.0, 1.0, 0.0], [0.857493, 0.0, 0.514496]]` · b) `[35.0, 6.0, 1.0]` · c) `[0.833333, 0.142857, 0.02381]` · d) `True` · e) `"(3, 1)"` · f) `"ValueError"` · g) `"ValueError"` · h) `"ValueError"`.

**Démarche.** Les contrôles de la docstring, `values, Q = np.linalg.eigh(C)`, l'ordre décroissant (`values[::-1]`, `Q[:, ::-1]`), les `k` premières colonnes avec la convention de signe, et les variances `np.maximum(values, 0.0) + 0.0`. Pour la copie : la deuxième mesure est isolée (variance 6, axe $\mathbf{e}_2$) ; le bloc $\begin{pmatrix} 10 & -15 \\ -15 & 26 \end{pmatrix}$ a pour trace 36 et déterminant 35, valeurs propres 35 et 1, vecteurs propres $(3, -5)$ et $(5, 3)$ ; la convention retourne $(3, -5)$ en $(-3, 5)$ (sa coordonnée de plus grande valeur absolue est $-5$). Les deux premiers axes gardent $\frac{41}{42} \approx 97{,}6\,\%$.

**Erreurs fréquentes.** Les axes en lignes ; l'ordre croissant de `eigh` ; une tolérance de symétrie absolue ; des parts calculées sur les seules $k$ premières variances.

### Ex M12d.30 — `np.linalg.svd`, `np.linalg.cond` et `sklearn.decomposition.PCA` contre tes fonctions : les signes

**Réponses** : a) `[7.114696, 4.939463, 3.99785]` · b) `True` · c) `True` · d) `[200, 200]` · e) `True` · f) `True` · g) `1`.

**Démarche.** b) `signs = np.where(Vt[np.arange(3), np.argmax(np.abs(Vt), axis=1)] < 0, -1.0, 1.0)`, puis `Vt * signs[:, None]` et `U * signs`. Pour la copie : $s_i\mathbf{u}_i\mathbf{v}_i^\top = s_i(-\mathbf{u}_i)(-\mathbf{v}_i)^\top$ : on peut changer le signe d'un couple, jamais d'un seul de ses deux vecteurs (le produit changerait de signe). `np.cov(X_30)` prend les **lignes** pour des variables : une matrice $200 \times 200$, sans avertissement. Les variances le long des axes ne dépendent pas de la moyenne : `PCA` centre d'abord.

**Erreurs fréquentes.** Changer le signe d'une ligne de `Vt` sans la colonne de `U` ; comparer `components_` (axes en lignes) à `principal_axes` (en colonnes) sans transposer ; oublier `rowvar=False`.

### Ex M12d.31 — Prédire l'allure des valeurs singulières d'une image, et le rang qui suffit

**Réponses** : a) `2` · b) `2` · c) `4` · d) `3`.

a) Une chute rapide puis une longue traîne : les zones lisses et les contours se répètent d'une ligne à l'autre (quelques couches), la texture fine et les arrondis des niveaux de gris donnent une traîne jamais nulle. b) 13 couches pour 90 %. c) Environ 240 : le bruit n'a aucune structure, ses valeurs singulières sont du même ordre (un rapport d'environ 10 entre la première et la dernière). d) 82,5 % : la première couche de l'image brute rend surtout le niveau moyen. Le débruitage par troncature repose sur ce contraste : le signal est dans les premières couches, le bruit partout.

### Ex M12d.32 — Compresser une image du domaine public : l'erreur en fonction du rang

**Réponses** : a) `103.65` · b) `0.8796` · c) `13` · d) `125` · e) `0.1929` · f) `0.0542` · g) `0.825`.

Eckart-Young : $\lVert \mathbf{A}_c - (\mathbf{A}_c)_k \rVert_F^2 = \sum_{i > k} s_i^2$, donc l'erreur relative vaut $\sqrt{1 - 0{,}9628} \approx 0{,}193$ au rang 50 ; rajouter la moyenne aux deux images ne change pas leur écart. La tasse est reconnaissable dès le rang 5 ; le grain du bois demande plusieurs dizaines de couches. 99 % demandent 125 couches, soit 52 % des nombres : ce n'est plus une compression. Un JPEG travaille par blocs de $8 \times 8$ pixels, dans une base fixe de cosinus, et compte des bits (il quantifie les coefficients) : c'est bien plus économe (voir le 🏆 M12d.37 pour une idée voisine, avec la SVD).

### Ex M12d.33 — La SVD par AᵀA contre `np.linalg.svd` : ce qu'on perd quand κ est grand

**Réponses** : a) `1000000.0` · b) `True` · c) `True` · d) `False` · e) `3` · f) `4`.

Le tableau : environ $2 \times 10^{-13}$, $8 \times 10^{-10}$, $3 \times 10^{-5}$ et $0{,}4$ pour ta fonction ; $3 \times 10^{-15}$ à $2 \times 10^{-9}$ pour LAPACK. L'erreur sur une valeur propre de $\mathbf{A}^\top\mathbf{A}$ est d'environ $10^{-16}\,s_{\max}^2$, soit une erreur relative d'environ $10^{-16}\kappa^2$ sur $s_{\min}^2 = \kappa^{-2}$ : elle grandit de 4 puissances de 10 quand $\kappa$ est multiplié par 100, et à $\kappa = 10^8$ il ne reste rien. LAPACK travaille sur $\mathbf{A}$ et perd environ $10^{-16}\kappa$. c) La reconstruction reste bonne : la couche fausse ne pèse que $s_{\min} = 10^{-6}$ de la matrice. d) Mais $\mathbf{U} = \mathbf{A}\mathbf{V}/s$ divise par un $s_{\min}$ faux : $\mathbf{U}^\top\mathbf{U}$ s'écarte de $\mathbf{I}$ d'environ $10^{-16}\kappa^2 = 10^{-4}$. e) f) Le rang numérique dépend du seuil : 3 avec `tol=1e-6`, 4 pour `matrix_rank` (un seuil d'environ $10^{-15}\,s_{\max}$).

### Ex M12d.34 — La SVD en images : Vᵀ, Σ puis U appliqués au cercle unité, étape par étape

Vérification manuelle (la figure). Avec $\mathbf{A} = \begin{pmatrix} 1{,}5 & 1 \\ -0{,}5 & 2 \end{pmatrix}$ : $s \approx 2{,}26$ et $1{,}55$, $\det\mathbf{A} = 3{,}5 > 0$. Les couleurs tournent dans le même sens dans le premier et le dernier dessin (l'orientation est conservée). Selon les signes rendus par LAPACK, $\det\mathbf{V} = -1$ : la deuxième étape est alors une symétrie (les couleurs tournent à l'envers), et $\det\mathbf{U} = -1$ aussi, qui la compense. L'aire de l'ellipse finale vaut $\pi s_1s_2 = 3{,}5\,\pi$.

### Ex M12d.35 — Chasse à l'erreur : une ACP sans centrer, n et n − 1 mélangés, des axes lus en lignes au lieu de colonnes

**Réponses** : a) `"AEG"` · b) `[11.9435, 2.5045, 0.4779]` · c) `[0.9148, 0.4039, -0.0024]` · d) `0.975`.

(A) $\mathbf{X}^\top\mathbf{X}/(n - 1)$ mesure la dispersion autour de l'**origine** : sa plus grande valeur propre (environ 506) est dominée par la moyenne $(20, -8, 4)$, et le « premier axe » pointe vers elle ; c'est le résultat le plus trompeur. (E) `vectors[order]` permute les **lignes** de la matrice des vecteurs propres : il faut `vectors[:, order]`. (G) `np.var` divise par $n$ par défaut, la covariance par $n - 1$ : le rapport vaut $\frac{39}{40}$ ; sans la ligne (G), cette incohérence passerait inaperçue. Les contrôles de la fiche (§6, ⚠️) : $\mathbf{C}\mathbf{u} = \lambda\mathbf{u}$ attrape (E) ; des scores de moyenne nulle et de variances $\lambda_j$ (avec `ddof=1`) attrapent (A) et (G).

### Ex M12d.36 — Un test : la reconstruction de rang plein redonne X, et l'erreur décroît avec k

Vérification par la cellule ✅/❌. L'ACP qui oublie la moyenne échoue dès la propriété 1. Celle qui prend les colonnes de `eigh` dans l'ordre croissant (les axes de plus petite variance d'abord), et celle qui ne centre pas, passent les propriétés 1 et 2 (des sous-espaces emboîtés donnent des erreurs décroissantes) ; seule la propriété 3 dit **quel** sous-espace est choisi. La propriété 3 attrape donc, seule, les trois ACP fausses. Les deux autres restent utiles : elles ne supposent aucun théorème, et leur échec oriente la recherche. Pour des scores : moyenne nulle, variances $\lambda_j$ (avec `ddof=1`), covariances nulles (M12d.19).

### Ex M12d.37 — Défi : compresser une image centrée en gardant 93,5 % de son énergie avec au plus 5 % des nombres

**Réponse** : `True` (objectif atteint).

Une solution : découper l'image en carrés de $8 \times 8$ pixels, ranger chaque carré en **ligne** d'une matrice de forme $(3\,750, 64)$, et faire l'ACP de ces lignes (centrer par le carré moyen, puis la SVD) avec 3 composantes : $64 + 3 \times 64 + 3\,750 \times 3 = 11\,506$ nombres, et 94,1 % de l'énergie, au-dessus des 93,5 % demandés. Les carrés se ressemblent (zones lisses, bords, grain) : leur matrice a des valeurs singulières qui décroissent bien plus vite que celles de l'image entière, et les trois « carrés de base » sont partagés par tous. Des carrés de $10 \times 10$ ou $20 \times 20$ font presque aussi bien (environ 94 %), ceux de $5 \times 5$ un peu moins (92,6 %). Des tuiles de $50 \times 50$, chacune décomposée par sa propre SVD au rang choisi au mieux, restent sous 92 % (89,5 % sans centrer, 91,6 % en retirant la moyenne de chaque tuile) : leurs bases ne sont pas partagées. Stocker seulement la moyenne de chaque rectangle de $4 \times 5$ pixels ($12\,000$ nombres, tout le budget) garde 93,3 % : c'est pour cela que l'objectif est à 93,5 %. Les défauts visibles sont des bords de carrés, que la norme de Frobenius ne pénalise pas plus qu'un autre écart ; JPEG les atténue, et compte des bits plutôt que des nombres.
