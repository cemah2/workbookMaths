# M16 · Applications affines, graphes et variance d'un produit — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M16.Q1 — Les formes de W, de b et de x W + b, dans chaque convention
1. $\mathbf{W}$ de forme $(5, 2)$, $\mathbf{b}$ de forme $(2,)$ : une ligne de $\mathbf{W}$ par entrée, une colonne par sortie.
2. $\mathbf{A}$ de forme $(2, 5)$, et $\mathbf{A} = \mathbf{W}^\top$.
3. **Vrai** : la sortie $k$ vaut $\sum_j x_jW_{jk} + b_k$, qui n'utilise que la colonne $k$.
4. $(100, 2)$ ; $5 \times 2 + 2 = 12$ paramètres (le nombre de points n'y change rien).
5. **Faux** : pour une application de $\mathbb{R}^3$ dans $\mathbb{R}^3$, $\mathbf{W}$ et $\mathbf{W}^\top$ ont la même forme $(3, 3)$, et le calcul passe sans erreur… en calculant une autre application.
6. $100 \times 5 \times 2 = 1\,000$.

### M16.Q2 — Coordonnées homogènes et composition : vrai ou faux
1. $(4, 3)$ : $(n + 1, m + 1)$ avec $n = 3$ entrées et $m = 2$ sorties.
2. **Vrai** : la dernière colonne de $\mathbf{H}$ est $(0, \ldots, 0, 1)$, et $[\mathbf{x}, 1]$ la multiplie en $0 + \cdots + 0 + 1 = 1$.
3. **Faux** : $[\mathbf{x}, 1]\,\mathbf{H}_1\mathbf{H}_2$ ; avec des lignes, la première application appliquée est à gauche.
4. $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ a & b & 1 \end{pmatrix}$.
5. **Vrai** : les deux produits sont la matrice de la translation de vecteur la somme des deux vecteurs. Deux translations commutent ; c'est une exception (une translation et une homothétie ne commutent pas : fiche §2).
6. **Faux** : $\mathbf{H}$ est inversible si et seulement si $\mathbf{W}$ l'est (son déterminant vaut $\det\mathbf{W}$, en développant selon la dernière colonne). Une projection sur une droite donne un $\mathbf{H}$ non inversible.

### M16.Q3 — Lire une matrice d'adjacence : degrés, arêtes, chemins, cycles
1. 4 arêtes (la somme des cases) : $1 \to 2$, $1 \to 4$, $2 \to 3$, $3 \to 4$.
2. Degré entrant 2 (la colonne 4 : depuis 1 et 3), degré sortant 0 (la ligne 4).
3. Aucun de longueur 2 : $(\mathbf{A}^2)_{14} = A_{12}A_{24} + A_{13}A_{34} = 0$. Un de longueur 3 : $1 \to 2 \to 3 \to 4$.
4. Non : $\mathbf{A}$ est strictement triangulaire supérieure, toutes les arêtes vont vers un numéro plus grand.
5. **Faux** : il peut y avoir des chemins d'une autre longueur. Ici $(\mathbf{A}^2)_{14} = 0$, mais $1 \to 4$ est une arête.
6. **Vrai** : avec un cycle, aucune puissance de $\mathbf{A}$ n'est nulle (fiche §4, ∂ M16.8).

### M16.Q4 — Indépendantes, décorrélées, ou ni l'un ni l'autre ?
1. $2 \times (-1) = -2$.
2. $4 \times 9 = 36$ : les deux moyennes sont nulles, les deux autres termes disparaissent.
3. **Vrai** : les deux autres termes, $\mathbb{V}(X)\,\mathbb{E}[Y]^2$ et $\mathbb{V}(Y)\,\mathbb{E}[X]^2$, sont positifs ou nuls.
4. 5 : $\mathbb{E}[\varepsilon x] = 0$ et $\mathbb{E}[\varepsilon^2x^2] = 1 \times 5$.
5. **Faux** : il suffit que les $Z_i$ soient deux à deux **décorrélées** ; seules les covariances entrent dans la formule.
6. **Vrai** : ce sont les hypothèses du lemme du §6 ; la corrélation des $x_i$ (ici une égalité) n'y joue aucun rôle.

<a id="rappels"></a>

## 🔁 Rappels

### M16.R1 — Le produit matriciel, ses formes et son coût (M09a)
1. $(4, 0, -3)$ : on multiplie case par case.
2. $(2, 3)$ : $(2, 5) \times (5, 7) \to (2, 7)$, puis $(2, 7) \times (7, 3) \to (2, 3)$.
3. $(\mathbf{A}\mathbf{B})\mathbf{C}$ : $2 \times 5 \times 7 + 2 \times 7 \times 3 = 70 + 42 = 112$. $\mathbf{A}(\mathbf{B}\mathbf{C})$ : $5 \times 7 \times 3 + 2 \times 5 \times 3 = 105 + 30 = 135$. Même résultat (associativité), coûts différents.
4. $(\mathbf{A}\mathbf{B}\mathbf{C})^\top = \mathbf{C}^\top\mathbf{B}^\top\mathbf{A}^\top$ (l'ordre s'inverse).
5. $(7,)$ : $(2,) \times (2, 5) \to (5,)$, puis $(5,) \times (5, 7) \to (7,)$.

### M16.R2 — La variance d'une somme de variables indépendantes (M02b)
1. $\mathbb{E}[2X - Y] = 2 - (-3) = 5$ ; $\mathbb{V}(2X - Y) = 4 \times 2 + 5 = 13$ (les variances s'ajoutent, même pour une différence).
2. $\mathbb{E}[X^2] = \mathbb{V}(X) + \mathbb{E}[X]^2 = 3$.
3. 0 : des variables indépendantes ont une covariance nulle.
4. $10 \times 2 = 20$ pour la somme de 10 copies indépendantes ; $100 \times 2 = 200$ pour $10X$. Dix copies indépendantes se compensent en partie, dix fois la même variable non.
5. $\frac{(6 - 0)^2}{12} = 3$.

### M16.R3 — Les valeurs propres d'une matrice triangulaire (M12c)
1. 2, $-3$ et 7 : les coefficients diagonaux.
2. $2 \times (-3) \times 7 = -42$.
3. Toutes nulles : la diagonale est nulle.
4. **Faux** : $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ a ses deux valeurs propres nulles sans être nulle (elle est nilpotente).
5. $\mathbf{N}^2 = \begin{pmatrix} 0 & 0 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$, $\mathbf{N}^3 = \mathbf{0}$ : chaque puissance pousse les cases non nulles d'une diagonale plus haut.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M16.1 — Une application affine de ℝ³ dans ℝ² dans les deux conventions

**Réponses.** a) `[[1, 4], [0, 1], [-2, -1]]` · b) `[3, -2]` · c) `[3, 4]` · d) `[[1, 0, -2], [4, 1, -1]]` · e) `8` · f) `[[4, 2], [3, -1], [2, 2]]` · g) `427` · h) `210000`.

**Démarche.** La sortie 1 vaut $1 \cdot x_1 + 0 \cdot x_2 - 2x_3$, plus 3 : ses coefficients forment la **colonne** 1 de $\mathbf{W}$, $(1, 0, -2)$ ; la sortie 2 donne la colonne 2, $(4, 1, -1)$. D'où a), de forme $(3, 2)$, et b). c) $(2, -1, 1)\mathbf{W} = (2 + 0 - 2,\ 8 - 1 - 1) = (0, 6)$, plus $\mathbf{b}$. d) En colonnes, la matrice est $\mathbf{W}^\top$, de forme $(2, 3) $ : chaque **ligne** porte les coefficients d'une sortie. e) $3 \times 2 + 2$. f) Les points de base $(1, 0, 0)$ et $(0, 1, 0)$ ont pour images les lignes 1 et 2 de $\mathbf{W}$, plus $\mathbf{b}$ ; $(1, 1, 1)$ a pour image la somme des trois lignes, plus $\mathbf{b}$. g) $60 \times 7 + 7$. h) $500 \times 60 \times 7$.

Dans ta copie : la ligne 3 de $\mathbf{W}$, $(-2, -1)$, dit comment $x_3$ se répartit entre les sorties ; la colonne 2 sert à la sortie 2. La ligne 1 de f) ne dépend que du premier point : un produit $\mathbf{X}\mathbf{W}$ traite chaque ligne seule. Elle vaut la ligne 1 de $\mathbf{W}$ plus $\mathbf{b}$ : l'image d'un vecteur de la base canonique lit une ligne de $\mathbf{W}$. La ligne 3, image de $(1, 1, 1)$, est la somme des trois lignes de $\mathbf{W}$, plus $\mathbf{b}$ : $(1 + 0 - 2,\ 4 + 1 - 1) + (3, -2) = (2, 2)$.

**Erreurs fréquentes.** Ranger les coefficients d'une sortie dans une **ligne** de $\mathbf{W}$ (c'est la convention en colonnes : on obtient d) à la place de a)). Oublier $\mathbf{b}$, en c) et en f). Compter $nm$ paramètres sans le biais.

**Variante.** $h(x_1, x_2, x_3) = (2x_2 - x_3,\ x_1 + 1)$ : $\mathbf{W} = \begin{pmatrix} 0 & 1 \\ 2 & 0 \\ -1 & 0 \end{pmatrix}$, $\mathbf{b} = (0, 1)$, $h(1, 1, 1) = (1, 2)$, 8 paramètres.

### Ex M16.2 — Rotation, homothétie puis translation du plan

**Réponses.** a) `[[0, 1, 0], [-1, 0, 0], [0, 0, 1]]` · b) `[[2, 0, 0], [0, 2, 0], [0, 0, 1]]` · c) `[[1, 0, 0], [0, 1, 0], [1, -3, 1]]` · d) `[[0, 2, 0], [-2, 0, 0], [1, -3, 1]]` · e) `[-1, 1]` · f) `[[0, -0.5, 0], [0.5, 0, 0], [1.5, 0.5, 1]]` · g) `[4, 6]`.

**Démarche.** a) Avec des lignes, la ligne $j$ de $\mathbf{W}_1$ est l'image du $j$-ième vecteur de base : $(1, 0) \mapsto (0, 1)$ et $(0, 1) \mapsto (-1, 0)$, d'où $\mathbf{W}_1 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. Vérification : $(1, 0)\mathbf{W}_1 = (0, 1)$. b) $\mathbf{W}_2 = 2\mathbf{I}$, pas de translation. c) $\mathbf{W}_3 = \mathbf{I}$ et la translation sur la dernière ligne. d) $f_1$ d'abord, donc à gauche : $\mathbf{H} = \mathbf{H}_1\mathbf{H}_2\mathbf{H}_3$ ; $\mathbf{H}_1\mathbf{H}_2 = \begin{pmatrix} 0 & 2 & 0 \\ -2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$, puis $\mathbf{H}_3$ ajoute la translation sur la dernière ligne. Donc $f(x, y) = (-2y + 1,\ 2x - 3)$. e) $f(2, 1) = (-2 + 1,\ 4 - 3) = (-1, 1)$. f) $f^{-1}$ retire d'abord la translation, puis défait l'homothétie, puis la rotation : $(u, v) \mapsto (u - 1, v + 3) \mapsto \left(\frac{u - 1}{2}, \frac{v + 3}{2}\right) \mapsto \left(\frac{v + 3}{2}, -\frac{u - 1}{2}\right)$ (la rotation réciproque est $(x, y) \mapsto (y, -x)$). Donc $f^{-1}(u, v) = (0{,}5v + 1{,}5,\ -0{,}5u + 0{,}5)$, de matrice homogène f) ; c'est aussi $\mathbf{H}^{-1}$. Vérification : $f^{-1}(-1, 1) = (2, 1)$. g) $f_3$ puis $f_2$ puis $f_1$ : $(2, 1) \mapsto (3, -2) \mapsto (6, -4) \mapsto (4, 6)$.

e) et g) diffèrent parce que la translation n'est pas au même endroit de la chaîne : appliquée en dernier, elle ajoute $(1, -3)$ ; appliquée en premier, elle est ensuite doublée et tournée.

**Erreurs fréquentes.** Écrire la matrice de rotation des colonnes, $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, dans une matrice pour des lignes : on tourne dans l'autre sens. Mettre la translation dans la dernière colonne. Multiplier dans l'ordre $\mathbf{H}_3\mathbf{H}_2\mathbf{H}_1$ (c'est l'ordre des colonnes). Pour l'inverse, oublier de transformer la translation (écrire $-\mathbf{b}$ sur la dernière ligne).

**Variante.** Rotation, puis translation de $(1, -3)$, puis homothétie : $\mathbf{H}_1\mathbf{H}_3\mathbf{H}_2$, et $(2, 1) \mapsto (-1, 2) \mapsto (0, -1) \mapsto (0, -2)$.

### Ex M16.3 — Des rues à sens unique

**Réponses.** a) `[[0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [1, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]` · b) `[1, 2, 3, 1, 0]` · c) `[1, 1, 1, 2, 2]` · d) `[[0, 0, 1, 1, 0], [1, 0, 0, 1, 2], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]` · e) `1` · f) `2` · g) `3` · h) `8`.

**Démarche.** a) Un 1 en ligne $i$, colonne $j$ pour chaque rue $i \to j$. b) Les sommes des lignes ; c) celles des colonnes (les deux listes ont la même somme, 7, le nombre de rues). d) $(\mathbf{A}^2)_{ij} = \sum_l A_{il}A_{lj}$ compte les intermédiaires $l$ : par exemple $(\mathbf{A}^2)_{25} = 2$ ($2 \to 3 \to 5$ et $2 \to 4 \to 5$). e) $(\mathbf{A}^2)_{14} = 1$ : $1 \to 2 \to 4$. f) $(\mathbf{A}^3)_{15} = 2$ : $1 \to 2 \to 3 \to 5$ et $1 \to 2 \to 4 \to 5$. g) La trace de $\mathbf{A}^3$ : $1 \to 2 \to 3 \to 1$, $2 \to 3 \to 1 \to 2$ et $3 \to 1 \to 2 \to 3$, le même cycle compté depuis chacun de ses trois carrefours. h) La somme des cases de d).

Dans ta copie : le cycle $1 \to 2 \to 3 \to 1$ se parcourt autant de fois qu'on veut, donc il y a des chemins de toutes les longueurs, et aucune puissance ne s'annule. Le seul cycle est $1 \to 2 \to 3 \to 1$ : supprimer l'une de ses trois rues, $1 \to 2$, $2 \to 3$ ou $3 \to 1$, suffit. Dans les trois cas, il n'y a plus de cycle, g) vaut 0 et $\mathbf{A}^5 = \mathbf{0}$.

**Erreurs fréquentes.** Écrire la transposée ($A_{ij} = 1$ pour une rue $j \to i$). Confondre degrés entrants et sortants. Compter un cycle une seule fois en g) : la trace compte chaque chemin fermé depuis chaque point de départ.

**Variante.** Sans la rue $3 \to 1$ : les chemins de longueur 3 de 1 à 5 sont toujours 2 ; $\mathbf{A}^3$ n'a plus de diagonale non nulle.

### Ex M16.4 — Un planning de tâches

**Réponses.** a) `[[0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0]]` · b) `[2, 0, 2, 2, 1, 1]` · c) `2` · d) `6` · e) `[2, 5, 4, 1, 6, 3]` · f) `4` · g) `32`.

**Démarche.** a) Dans la numérotation donnée : Montage (1) → Expédition (3) et Contrôle (6) ; Commande (2) → Peinture (4) et Découpe (5) ; Peinture (4) → Montage (1) ; Découpe (5) → Montage (1) et Peinture (4) ; Contrôle (6) → Expédition (3). b) Les sommes des colonnes. c) $(\mathbf{A}^2)_{21} = 2$ : Commande → Découpe → Montage et Commande → Peinture → Montage. d) On note chaque tâche par son initiale (C, D, P, M, E), et K pour Contrôle. On énumère, de Commande à Montage : C → D → M, C → P → M, C → D → P → M (3 chemins) ; de Montage à Expédition : M → E et M → K → E (2 chemins) ; chaque chemin de Commande à Expédition passe par Montage (seul prédécesseur de Contrôle, et prédécesseur d'Expédition avec Contrôle) : $3 \times 2 = 6$. e) Le chemin C → D → P → M → K → E passe par les six tâches, et chacune de ses arêtes doit aller vers un numéro plus grand : les numéros 1 à 6 sont donnés dans cet ordre. On vérifie que les trois autres arêtes (C → P, D → M, M → E) montent aussi. En anciens numéros : 2, 5, 4, 1, 6, 3. f) De Découpe à Montage : D → M et D → P → M (2) ; fois 2 : 4. g) La somme des cases de $\mathbf{S} = \mathbf{A} + \cdots + \mathbf{A}^5$ (le notebook la calcule) : $3 + 15 + 0 + 4 + 9 + 1$ par lignes.

Dans ta copie : $\mathbf{A}$ n'est pas triangulaire parce que l'arête Peinture (4) → Montage (1) descend vers un numéro plus petit. La numérotation est unique parce que le graphe contient le chemin C → D → P → M → K → E, qui passe par les six tâches : chacune doit précéder la suivante. Dans la nouvelle numérotation, la matrice $\mathbf{A}' = \mathbf{P}\mathbf{A}\mathbf{P}^\top$ ($\mathbf{P}$ la matrice de permutation de la fiche §4) est strictement triangulaire supérieure, donc nilpotente : $\mathbf{A}'^6 = \mathbf{0}$. Comme $\mathbf{P}^\top\mathbf{P} = \mathbf{I}$, on a $\mathbf{A} = \mathbf{P}^\top\mathbf{A}'\mathbf{P}$, puis $\mathbf{A}^6 = \mathbf{P}^\top\mathbf{A}'^6\mathbf{P} = \mathbf{0}$ (les $\mathbf{P}\mathbf{P}^\top$ intermédiaires valent $\mathbf{I}$). Enfin, d) est le coefficient de $\mathbf{S}$, égal à celui de $(\mathbf{I} - \mathbf{A})^{-1}$ hors de la diagonale.

**Erreurs fréquentes.** Lire les flèches à l'envers (on obtient la transposée et une numérotation à l'envers). Ne compter que les chemins d'une longueur. Croire qu'une matrice qui n'est pas triangulaire dans la numérotation donnée a un cycle : il faut d'abord chercher une renumérotation.

**Variante.** Avec une arête de plus, Commande → Montage, il y a 4 chemins de Commande à Montage, donc $4 \times 2 = 8$ de Commande à Expédition, et la numérotation de e) reste valable.

### Ex M16.5 — Un prix aléatoire fois une quantité indépendante

**Réponses.** a) `360` · b) `9.16` · c) `14800` · d) `5968` · e) `77.25` · f) `64` · g) `0.2146` · h) `3600`.

**Démarche.** a) $3 \times 120$. b) $0{,}16 + 9$. c) $400 + 14\,400$. d) $\mathbb{E}[R^2] = 9{,}16 \times 14\,800 = 135\,568$, moins $360^2 = 129\,600$. Les trois termes : $\mathbb{V}(P)\,\mathbb{V}(Q) = 64$, $\mathbb{V}(P)\,\mathbb{E}[Q]^2 = 0{,}16 \times 14\,400 = 2\,304$, $\mathbb{V}(Q)\,\mathbb{E}[P]^2 = 400 \times 9 = 3\,600$. e) $\sqrt{5\,968} \approx 77{,}25$. g) $\frac{77{,}25}{360} \approx 0{,}2146$. h) Avec $\mathbb{V}(P) = 0$, il ne reste que $\mathbb{V}(Q)\,\mathbb{E}[P]^2 = 3\,600$.

Dans ta copie : le terme dû à la quantité, 3 600, domine : $Q$ varie de 17 % ($c_Q = \frac{20}{120}$), $P$ de 13 % ($c_P = \frac{0{,}4}{3}$), et le produit des deux petites variations (64) est négligeable. Vérification : $(1 + 0{,}01778)(1 + 0{,}02778) = 1{,}04605$, et $c_R^2 = \frac{5\,968}{129\,600} \approx 0{,}04605$. Si $P$ et $Q$ dépendent l'un de l'autre, $\mathbb{E}[PQ] \ne \mathbb{E}[P]\,\mathbb{E}[Q]$ et la formule ne s'applique pas : une baisse de prix les années d'abondance compense en partie la hausse de la quantité, et tend à rendre la recette **moins** variable que ne le dit la formule.

**Erreurs fréquentes.** f) au lieu de d). Oublier le terme $\mathbb{V}(P)\,\mathbb{V}(Q)$ (5 904). Confondre écart-type et variance (0,4 et 0,16).

**Variante.** $\mathbb{E}[P] = 2$, $\mathbb{V}(P) = 0{,}25$, $\mathbb{E}[Q] = 50$, $\mathbb{V}(Q) = 100$ : $\mathbb{E}[R] = 100$, $\mathbb{V}(R) = 25 + 625 + 400 = 1\,050$.

### Ex M16.6 — Des signes aléatoires d'amplitudes différentes sur des mesures corrélées

**Réponses.** a) `30` · b) `0.25` · c) `10.25` · d) `5` · e) `11.25` · f) `30` · g) `40.25`.

**Démarche.** a) La somme de toutes les cases de la matrice de covariance : $4 + 9 + 1 + 2(5 + 1 + 2) = 30$. b) $\varepsilon_2$ est centré et $\varepsilon_2^2 = 0{,}25$ toujours. c) Le lemme du §6 : $\mathbb{V}(S) = 1 \times 4 + 0{,}25 \times 9 + 4 \times 1 = 10{,}25$ (les $x_i$ sont centrés, donc $\mathbb{E}[x_i^2] = \mathbb{V}(x_i)$). d) $\varepsilon_1x_1 \cdot \varepsilon_1x_2 = \varepsilon_1^2x_1x_2 = x_1x_2$, car $\varepsilon_1^2 = 1$ ; les deux produits sont centrés (le lemme, ou simplement $x_1$ et $x_2$ centrés) : $\operatorname{Cov}(\varepsilon_1x_1, \varepsilon_1x_2) = \mathbb{E}[x_1x_2] = \operatorname{Cov}(x_1, x_2) = 5$. e) $\mathbb{E}[x_1^2]$ devient $4 + 1^2 = 5$ : $5 + 2{,}25 + 4 = 11{,}25$. f) $\varepsilon^2 = 1$ : $\mathbb{V}(\varepsilon T) = \mathbb{E}[T^2] = \mathbb{V}(T) = 30$ pour $T = x_1 + x_2 + x_3$. g) La somme vaut $T + S$, deux morceaux décorrélés (admis par l'énoncé) : $\mathbb{V}(T) + \mathbb{V}(S) = 30 + 10{,}25 = 40{,}25$.

Dans ta copie : d) n'est pas nul parce que le lemme demande des signes **différents**, indépendants entre eux ; un même signe se simplifie ($\varepsilon_1^2 = 1$) et laisse la covariance des mesures. Les covariances 5, 1 et 2 disparaissent de c) par le lemme : les trois produits sont décorrélés, quelles que soient les covariances des $x_i$. En e), $\mathbb{V}(\varepsilon_1x_1) = \mathbb{E}[\varepsilon_1^2x_1^2] - \mathbb{E}[\varepsilon_1x_1]^2 = \mathbb{E}[x_1^2] - 0$ : le signe rend aléatoire la moyenne de $x_1$ elle aussi, et elle compte. En f), il manque l'**indépendance des signes entre eux** : un seul signe, commun aux trois termes, multiplie tout ; il ne change pas la variance de $T$, et les covariances restent. En g), il manque le **centrage** : les multiplicateurs ont pour moyenne 1, et leur partie constante remet $T$ et ses covariances dans la somme ; les deux morceaux $T$ et $S$ sont décorrélés (admis), et leurs variances s'ajoutent.

**Erreurs fréquentes.** Prendre $\mathbb{V}(\pm a) = a$ au lieu de $a^2$. Utiliser $\mathbb{V}(x_i)$ au lieu de $\mathbb{E}[x_i^2]$ quand les mesures ne sont pas centrées (e). Croire qu'un signe aléatoire commun casse les corrélations (d et f).

**Variante.** Avec trois signes $\pm 1$ : $\mathbb{V}(S) = 4 + 9 + 1 = 14$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M16.7 — (Aᵏ)ᵢⱼ compte les chemins de longueur k

**Démonstration.**
1. Un chemin de longueur 1 de $i$ à $j$ est une arête $i \to j$ : il y en a 1 si $A_{ij} = 1$, 0 sinon. Donc $c_1(i, j) = A_{ij}$.
2. Un chemin de longueur $k + 1$ de $i$ à $j$ se coupe, de façon unique, en un chemin de longueur $k$ de $i$ à un nœud $l$ (son avant-dernier nœud), suivi de l'arête $l \to j$. Pour chaque $l$, il y a donc $c_k(i, l) \times A_{lj}$ chemins de longueur $k + 1$ dont l'avant-dernier nœud est $l$ (zéro s'il n'y a pas d'arête $l \to j$). Ces familles, pour des $l$ différents, sont disjointes, et chaque chemin est dans l'une d'elles : $c_{k+1}(i, j) = \sum_l c_k(i, l)A_{lj}$.
3. Récurrence : l'énoncé est vrai pour $k = 1$. S'il est vrai pour $k$, alors $c_{k+1}(i, j) = \sum_l(\mathbf{A}^k)_{il}A_{lj} = (\mathbf{A}^k\mathbf{A})_{ij} = (\mathbf{A}^{k+1})_{ij}$. Il est donc vrai pour tout $k \ge 1$.
4. Avec des poids, on note $p_k(i, j)$ la somme, sur les chemins de longueur $k$, des produits des poids. Le poids d'un chemin de longueur $k + 1$ est celui de sa partie de longueur $k$ multiplié par $A_{lj}$ ; en regroupant selon l'avant-dernier nœud, $p_{k+1}(i, j) = \sum_l p_k(i, l)A_{lj}$ (la distributivité fait sortir $A_{lj}$ de la somme), et la même récurrence conclut.
5. La somme de la ligne $i$ de $\mathbf{A}^k$ compte tous les chemins de longueur $k$ qui partent de $i$ ; la trace compte les chemins de longueur $k$ qui reviennent à leur départ (chaque chemin fermé, une fois par point de départ).

**Grille de relecture.** Le cas $k = 1$ est vérifié. La décomposition selon l'avant-dernier nœud (ou selon le premier) est justifiée : chaque chemin est compté **exactement une fois**. Le lien avec le produit matriciel est écrit, $(\mathbf{A}^k\mathbf{A})_{ij} = \sum_l(\mathbf{A}^k)_{il}A_{lj}$. La récurrence a son initialisation et son hérédité. La version pondérée dit où intervient la distributivité.

**Variante.** On peut aussi couper selon le **premier** pas : $c_{k+1}(i, j) = \sum_l A_{il}c_k(l, j)$, c'est-à-dire $\mathbf{A}^{k+1} = \mathbf{A}\mathbf{A}^k$.

### Ex M16.8 — Sans cycle si et seulement si nilpotente

**Démonstration.**
1. Un chemin de $n$ arêtes visite $n + 1$ nœuds (en comptant le départ), alors que le graphe n'en a que $n$ : deux de ces visites tombent sur le même nœud $u$ (principe des tiroirs, fiche §4). La portion du chemin entre ces deux visites part de $u$ et y revient, avec au moins une arête : c'est un cycle.
2. Si le graphe est sans cycle, il n'a donc aucun chemin de $n$ arêtes, et par M16.7 tous les coefficients de $\mathbf{A}^n$ sont nuls : $\mathbf{A}^n = \mathbf{0}$.
3. Un cycle de longueur $m$ qui passe par $i$ peut se lire en partant de $i$ (on le parcourt à partir de $i$ jusqu'à y revenir) ; parcouru $q$ fois de suite, est un chemin de longueur $qm$ de $i$ à $i$ : $(\mathbf{A}^{qm})_{ii} \ge 1$. Si une puissance $\mathbf{A}^k$ était nulle, toutes les puissances suivantes le seraient ($\mathbf{A}^{k'} = \mathbf{A}^k\mathbf{A}^{k' - k}$), dont une puissance $qm \ge k$ : contradiction.
4. Un graphe orienté à $n$ nœuds est sans cycle si et seulement si sa matrice d'adjacence est nilpotente, et alors $\mathbf{A}^n = \mathbf{0}$.
5. En développant, les termes se télescopent : $(\mathbf{I} - \mathbf{A})(\mathbf{I} + \mathbf{A} + \cdots + \mathbf{A}^{n-1}) = \mathbf{I} - \mathbf{A}^n = \mathbf{I}$. Les deux facteurs sont faits de puissances de $\mathbf{A}$, donc ils commutent : le produit dans l'autre ordre vaut aussi $\mathbf{I}$. Ainsi $\mathbf{I} - \mathbf{A}$ est inversible et $(\mathbf{I} - \mathbf{A})^{-1} = \mathbf{I} + \mathbf{A} + \cdots + \mathbf{A}^{n-1}$. Pour $i \ne j$, le coefficient de $\mathbf{I}$ est nul, et celui de $\mathbf{A}^k$ compte les chemins de longueur $k$ (M16.7) ; aucun chemin n'a $n$ arêtes ou plus : la somme compte tous les chemins de $i$ à $j$.

**Grille de relecture.** Le principe des tiroirs est appliqué aux $n + 1$ visites, et la portion entre deux visites est identifiée comme un cycle. Le sens « sans cycle ⇒ $\mathbf{A}^n = \mathbf{0}$ » utilise M16.7. Le sens réciproque montre qu'**aucune** puissance n'est nulle (pas seulement $\mathbf{A}^n$). Le télescopage est écrit, et la fin dit pourquoi les longueurs $\ge n$ ne manquent pas.

**Variante.** Pour une matrice strictement triangulaire supérieure $\mathbf{T}$, montre directement par récurrence que $(\mathbf{T}^k)_{ij} = 0$ dès que $j < i + k$ : une autre preuve que $\mathbf{T}^n = \mathbf{0}$.

### Ex M16.9 — La variance d'un produit de deux variables indépendantes

**Démonstration.**
1. $\{X^2 = u\} = \{X = \sqrt{u}\} \cup \{X = -\sqrt{u}\}$ (une réunion disjointe, ou un seul événement si $u = 0$, et l'événement impossible si $u < 0$, où les deux membres de l'égalité ci-dessous sont nuls), de même pour $Y^2$. Alors $P(X^2 = u, Y^2 = v)$ est une somme d'au plus quatre termes $P(X = a, Y = b) = P(X = a)\,P(Y = b)$, qui se factorise en $P(X^2 = u)\,P(Y^2 = v)$ : $X^2$ et $Y^2$ sont indépendantes.
2. M02b §5 appliqué à $X^2$ et $Y^2$ : $\mathbb{E}[X^2Y^2] = \mathbb{E}[X^2]\,\mathbb{E}[Y^2]$. Comme $\mathbb{V}(XY) = \mathbb{E}[(XY)^2] - \mathbb{E}[XY]^2$ et $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$, on obtient la formule.
3. Avec $\mathbb{E}[X^2] = \mathbb{V}(X) + \mathbb{E}[X]^2$ et de même pour $Y$, le produit $\mathbb{E}[X^2]\,\mathbb{E}[Y^2]$ a quatre termes ; le dernier, $\mathbb{E}[X]^2\,\mathbb{E}[Y]^2$, s'annule avec celui qu'on retranche.
4. $\mathbb{V}(X)\,\mathbb{E}[Y]^2 \ge 0$ et $\mathbb{V}(Y)\,\mathbb{E}[X]^2 \ge 0$, d'où l'inégalité. Égalité si et seulement si ces deux termes sont nuls : ($\mathbb{V}(X) = 0$ ou $\mathbb{E}[Y] = 0$) et ($\mathbb{V}(Y) = 0$ ou $\mathbb{E}[X] = 0$). Par exemple deux variables centrées, ou deux constantes.
5. On divise la formule de 2 par $\mathbb{E}[X]^2\,\mathbb{E}[Y]^2 = \mathbb{E}[XY]^2$ : $c_{XY}^2 = \frac{\mathbb{E}[X^2]}{\mathbb{E}[X]^2}\cdot\frac{\mathbb{E}[Y^2]}{\mathbb{E}[Y]^2} - 1 = (1 + c_X^2)(1 + c_Y^2) - 1$.

**Grille de relecture.** L'indépendance de $X^2$ et $Y^2$ est justifiée (pas seulement affirmée). La formule de 2 cite $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$ **et** $\mathbb{E}[X^2Y^2] = \mathbb{E}[X^2]\,\mathbb{E}[Y^2]$. Le cas d'égalité énumère les deux conditions. Le passage aux coefficients de variation suppose les moyennes non nulles.

**Variante.** Pour des variables à densité, la même démonstration marche avec les intégrales (M02b §7) ; et pour un produit de **trois** variables indépendantes, $1 + c_{XYZ}^2 = (1 + c_X^2)(1 + c_Y^2)(1 + c_Z^2)$.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M16.10 — Pont : n points rangés en lignes, X W + 1bᵀ

**Réponses.** a) `[4, 3]` · b) `[[1, 0, -2], [1, 0, -2], [1, 0, -2], [1, 0, -2]]` · c) `[[4, 2, -1], [3, 6, 0], [0, 4, -1], [5, -2, -2]]` · d) `[[2, -1, 0, 0], [1, 3, 1, 0], [1, 0, -2, 1]]` · e) `[[4, 2, -1, 1], [3, 6, 0, 1], [0, 4, -1, 1], [5, -2, -2, 1]]` · f) `24`.

**Démarche.** a) $(4, 2) \times (2, 3) \to (4, 3)$. b) Une colonne de 4 uns fois la ligne $\mathbf{b}^\top$ : quatre copies de $\mathbf{b}$. c) $\mathbf{X}\mathbf{W} = \begin{pmatrix} 3 & 2 & 1 \\ 2 & 6 & 2 \\ -1 & 4 & 1 \\ 4 & -2 & 0 \end{pmatrix}$, plus b). d) $\mathbf{W}$ en haut à gauche, $\mathbf{b}$ suivi de 1 en bas, une colonne $(0, 0, 1)$ à droite. e) c) avec une colonne de uns en plus : un seul produit fait la partie linéaire **et** la translation de tous les points. f) $4 \times 2 \times 3$.

Dans ta copie : $\mathbf{1}\mathbf{b}^\top$ est le produit d'une colonne $(4, 1)$ par une ligne $(1, 3)$ ; NumPy ne la construit pas, il **diffuse** $\mathbf{b}$, de forme $(3,)$, sur chaque ligne de `X @ W`, de forme $(4, 3)$. Avec un cinquième point, c) gagne une cinquième ligne et les quatre premières ne changent pas : chaque ligne est calculée seule.

**Variante.** Le point $(0, 0)$ a pour image $\mathbf{b} = (1, 0, -2)$ : la translation est l'image de l'origine.

### Ex M16.11 — Expliquer pourquoi la variance d'un produit n'est pas le produit des variances

**Réponse modèle (6 à 10 phrases).** Une erreur de quelques centimètres sur la longueur ne reste pas une erreur de quelques centimètres sur la surface : elle est multipliée par toute la largeur, plusieurs dizaines de mètres. La surface hérite donc de l'erreur sur la longueur, amplifiée par la largeur moyenne, et de l'erreur sur la largeur, amplifiée par la longueur moyenne. Ces deux contributions sont grandes ; le produit des deux petites erreurs, celui de ton calcul, n'en est qu'un troisième terme, minuscule. Si la largeur était mesurée exactement, il ne resterait que l'erreur de la longueur, multipliée par la largeur : ton calcul donnerait zéro, ce qui est absurde. Ton calcul n'est juste que si les deux grandeurs ont une moyenne nulle, ce qui n'arrive jamais pour une longueur. En résumé, ce sont les **moyennes** qui portent l'essentiel de la variance d'un produit.

**En 3 phrases.** Une erreur sur un facteur est multipliée par la valeur de l'autre facteur, et c'est ce terme qui domine. Le produit des deux variances n'est qu'un petit terme de plus. Il n'est la bonne réponse que si les deux moyennes sont nulles.

**Grille.** Les deux termes amplifiés par les moyennes sont décrits ; le cas d'une mesure exacte montre l'absurdité ; le seul cas juste (moyennes nulles) est donné.

<a id="entretien"></a>

## 💼 Entretien

### M16.E1 — « Pourquoi l'écart-type d'une somme de n termes indépendants grandit-il comme √n ? »

**Réponse modèle (60 secondes).** « Parce que ce sont les variances qui s'additionnent, pas les écarts-types. Des termes indépendants ont des covariances nulles, et la variance de leur somme est la somme de leurs variances : $n\sigma^2$ pour $n$ termes de variance $\sigma^2$. L'écart-type, sa racine, vaut $\sigma\sqrt{n}$ : les termes se compensent en partie. Si les termes sont corrélés, les covariances s'ajoutent, et, s'ils sont tous égaux, la somme vaut $n$ fois un terme, d'écart-type $n\sigma$. Des signes aléatoires indépendants suffisent à retrouver la croissance en $\sqrt{n}$ même pour des termes corrélés, parce qu'ils rendent les produits décorrélés. Conséquence : la moyenne de $n$ termes indépendants, la somme divisée par $n$, a un écart-type $\frac{\sigma}{\sqrt{n}}$ ; c'est pour cela qu'on répète une mesure, et qu'il faut quatre fois plus de mesures pour diviser l'incertitude par deux. »

**Grille.** Les variances s'ajoutent (covariances nulles) ; l'écart-type en $\sqrt{n}$ ; le cas corrélé (jusqu'à $n$) ; les signes aléatoires ; la moyenne en $\frac{\sigma}{\sqrt{n}}$ et ce qu'elle coûte en mesures.

<a id="notebook"></a>

## Notebook

Le code complet est dans `05_solutions.ipynb`, exécuté ; voici les réponses et ce qu'il faut en retenir.

- **M16.12 🔨** `homogeneous_matrix` : empiler $[\mathbf{W} \mid \mathbf{0}]$ sur $[\mathbf{b} \mid 1]$. Le point $(2, -1)$ a pour image $(5, -3)$.
- **M16.13 🔨** `sum_over_paths` : tester l'absence de cycle sur les puissances booléennes du motif, puis additionner les coefficients de $\mathbf{A}, \mathbf{A}^2, \ldots, \mathbf{A}^{n-1}$. Dans la grille de $5 \times 5$ carrefours, 70 chemins vont d'un coin à l'autre : chacun fait 4 pas vers l'est et 4 vers le nord, dans un ordre choisi parmi $\binom{8}{4} = 70$.
- **M16.14 🔨** `variance_of_product` : les deux formules du §5. La surface du champ a un écart-type d'environ 30,54 m², dû presque entièrement aux deux termes amplifiés par les moyennes (le produit des variances, 0,0144, est négligeable).
- **M16.15 🔮** B, A, B, B : sans signes, la somme de 25 mesures égales a l'écart-type 25, celle de 25 mesures indépendantes l'écart-type 5 ; avec des signes indépendants, les deux ont l'écart-type 5.
- **M16.16 🔬** limite $\frac{1}{1 - 0{,}36} = 1{,}5625$ ; pour $g = 1$, $v_{40} = 40$ (la variance croît linéairement) ; pour $g = 1{,}1$, $v_{40} = \frac{1{,}21^{40} - 1}{0{,}21} \approx 9\,749{,}52$ ; $v_k$ est à moins de 1 % de sa limite dès $k = 5$ ($0{,}36^5 \approx 0{,}006$, alors que $0{,}36^4 \approx 0{,}017$).
- **M16.17 🎨** les images successives de la flèche, par $\mathbf{H}_1$, $\mathbf{H}_1\mathbf{H}_2$, $\mathbf{H}_1\mathbf{H}_2\mathbf{H}_3$.
- **M16.18 🐛** (A) la matrice homogène doit avoir $\mathbf{W}$ (pas $\mathbf{W}^\top$) et $\mathbf{b}$ sur la dernière **ligne** ; (B) la variance d'un produit a trois termes ; (C) vérifier l'absence de cycle avant de calculer $(\mathbf{I} - \mathbf{A})^{-1}$.
- **M16.19 🛠️** le test compare des **images de points**, ce qui suffit à attraper une translation mal placée ou un 0 au lieu du 1.
- **M16.20 🏆** $\mathbb{E}[Z] = \frac{1}{4}$, $\mathbb{V}(Z) = \frac{7}{144}$, $P(Z \le \frac{1}{4}) = \frac{1 + \ln 4}{4} \approx 0{,}5966$, médiane $\approx 0{,}1867$. La fonction de répartition : $P(UV \le z) = \int_0^1 P\big(V \le \frac{z}{u}\big)\,du = z + \int_z^1\frac{z}{u}\,du = z - z\ln z$ pour $0 < z \le 1$, d'où la densité $-\ln z$.
