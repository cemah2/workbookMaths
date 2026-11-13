# CP5 · Corrigé détaillé et barème de l'examen blanc

> À lire **après** l'examen, et après la vérification automatique du notebook (`02_examen_notebook.ipynb`). Pour chaque question : la réponse, la démarche, le barème, les erreurs fréquentes et les exercices à refaire si tu as eu moins de la moitié des points.

## Règles de notation

- **Barème par sous-question**, entre crochets ; sauf mention contraire, une sous-question vaut 0,25 point. Une justification demandée « sur ta copie » compte dans la sous-question à laquelle elle se rattache. Le barème suit les durées du sujet (112 minutes pour 20 points) : 2 points pour une question de calcul de 10 minutes, 1,5 pour une de 9 minutes, et toutes les sous-questions valent 0,25.
- **Crédit partiel** sur une sous-question de 0,25 point : 0,1 pour une réponse juste sans la démarche demandée, ou pour une méthode juste avec une erreur de calcul. **Erreur reportée** : si une réponse fausse est réutilisée correctement plus loin, la suite n'est pas pénalisée une seconde fois (par exemple une réponse impulsionnelle fausse en CP5.10 a, réutilisée en b) et f), ou une trajectoire fausse en CP5.7 a, réutilisée en b) et c)).
- **Arrondis** : une décimale de moins coûte au plus 0,05 point par question ; un arrondi fait trop tôt, qui change la dernière décimale demandée, aussi. Des décimales en plus ne coûtent rien (le notebook les accepte).
- **Questions rédigées** (CP5.Q1, CP5.8, CP5.9 b, les phrases demandées « sur ta copie ») : les critères sont listés ; une idée juste formulée autrement compte autant.
- **Conventions** : celles du sujet. La convolution $*$ retourne le noyau, la corrélation croisée $\star$ ne le retourne pas ; la matrice de Toeplitz est $T_{ij} = w_{i-j}$ ; les récurrences sont en convention colonne, avec $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$ ; les normes induites $\lVert\cdot\rVert_1$ (colonnes), $\lVert\cdot\rVert_\infty$ (lignes) et $\lVert\cdot\rVert_2 = s_{\max}$.

---

## CP5.Q1 — Dix affirmations sur la partie V 🧠 · 1,5 point

0,15 par affirmation : 0,05 pour le verdict, 0,1 pour la justification.

**a) Faux** (M22, M21). La sortie est la convolution de l'entrée par la réponse impulsionnelle, $y_{t+1} = (\mathbf{h} * \mathbf{u})_t$, et la réponse impulsionnelle d'un filtre récursif est en général **infinie** : avec $n = 1$, $A = 0{,}5$, $B = C = 1$ et la seule entrée $u_0 = 1$, $y_t = 0{,}5^{t-1}$ pour $t \ge 1$, qui tend vers 0 sans jamais s'annuler. ($\rho < 1$ garantit que la sortie **tend** vers 0 ; elle ne s'annule après un nombre fini de pas que dans des cas particuliers, par exemple si $\mathbf{A}$ est nilpotente.)

**b) Vrai** (M21 §4, M22 §3). $\operatorname{circ}(\mathbf{h})^\top = \operatorname{circ}(\check{\mathbf{h}})$ est encore circulante, et deux matrices circulantes commutent (ce sont des sommes de puissances du décalage $\mathbf{P}$, $\operatorname{circ}(\mathbf{h}) = \sum_m h_m\mathbf{P}^m$) : $\mathbf{M}^\top\mathbf{M} = \mathbf{M}\mathbf{M}^\top$, la matrice est **normale**, et pour une matrice normale $\lVert\mathbf{M}^t\rVert_2 = \rho(\mathbf{M})^t$. Une matrice circulante ne connaît donc pas de croissance transitoire en norme 2.

**c) Vrai** (M21 §4, M22 §4). Chaque ligne et chaque colonne de $\operatorname{circ}(\mathbf{h})$ contient une fois chaque $h_m$. Donc $\operatorname{circ}(\mathbf{h})\,(1, \ldots, 1) = \big(\sum_m h_m\big)(1, \ldots, 1)$ : $\sum_m h_m$ est une valeur propre, et $\rho \ge \sum_m h_m$. Et $\lVert\operatorname{circ}(\mathbf{h})\rVert_1$ est la somme des valeurs absolues d'une colonne, $\sum_m\lvert h_m\rvert = \sum_m h_m$ ; comme $\rho \le \lVert\cdot\rVert_1$, les trois nombres sont égaux.

**d) Vrai** (M21 §3, M22 §3). $T_{ij} = w_{i-j}$ est nul au-dessus de la diagonale ($i < j$) et sur la diagonale ($w_0 = 0$) : les $n$ premières lignes forment une matrice **strictement triangulaire inférieure**, donc nilpotente ($\mathbf{U}^n = \mathbf{0}$), de rayon spectral nul, alors qu'elle n'est pas nulle.

**e) Faux** (M22 §2 et §4). $\sqrt{\det\mathbf{A}}$ est le **module** des valeurs propres, donc $\rho(\mathbf{A})$, pas la norme : $\mathbf{A} = \begin{pmatrix} 0 & 4 \\ -1 & 0 \end{pmatrix}$ a pour valeurs propres $\pm 2i$, $\sqrt{\det\mathbf{A}} = 2$, mais $\mathbf{A}^\top\mathbf{A} = \operatorname{diag}(1, 16)$ et $\lVert\mathbf{A}\rVert_2 = 4$. L'égalité vaut pour une matrice normale (une rotation-homothétie $r\,\mathbf{R}_\theta$), pas en général.

**f) Faux** (M22 §1 et §2). $h_k$ est une combinaison des $\lambda_i^k$, avec des coefficients de signes quelconques : $\mathbf{A} = \operatorname{diag}(0{,}5 ;\ 0{,}25)$, $\mathbf{B} = (1, 1)$, $\mathbf{C} = (1, -3)$ donnent $h_k = 0{,}5^k - 3 \times 0{,}25^k$, soit $h_0 = -2$, $h_1 = -0{,}25$, puis $h_2 = 0{,}0625 > 0$.

**g) Vrai** (M21 §4, §5 et §7). Un étage de pas $s$ est équivariant pour les décalages multiples de $s$, et décale alors sa sortie de $\frac ts$. Décaler l'entrée de 6 cases (un multiple de 3) décale la sortie du premier étage de 2 cases, un multiple du pas 2 du second, dont la sortie bouge donc d'une case. C'est le pas total $S = 3 \times 2 = 6$ de la pile.

**h) Faux** (M22 §4 et §5). $\rho(\mathbf{A}_2\mathbf{A}_1) \le \lVert\mathbf{A}_2\mathbf{A}_1\rVert_2 \le \lVert\mathbf{A}_2\rVert_2\,\lVert\mathbf{A}_1\rVert_2 < 1$ : le rayon spectral est au plus une norme induite, et les normes induites sont sous-multiplicatives. (Ce sont les rayons spectraux des facteurs qui ne disent rien du produit, pas leurs normes.)

**i) Vrai** (M22 §2). Avec $\mathbf{A} = 0{,}5\,\mathbf{R}_{\pi/3}$ (la multiplication par $0{,}5\,e^{i\pi/3}$), $\mathbf{B} = (1, 0)$ et $\mathbf{C} = (1, 0)$ : $\mathbf{A}^k = 0{,}5^k\,\mathbf{R}_{k\pi/3}$, dont le coefficient $(1, 1)$ vaut $0{,}5^k\cos\frac{k\pi}{3} = h_k$.

**j) Faux** (M21 §6, M22 §4). La première égalité est juste ($\mathbf{a}\mathbf{b}^\top\mathbf{x} = (\mathbf{b} \cdot \mathbf{x})\,\mathbf{a}$, et Cauchy-Schwarz), la seconde non : la colonne $j$ de $\mathbf{a}\mathbf{b}^\top$ est $b_j\mathbf{a}$, de norme L1 $\lvert b_j\rvert\,\lVert\mathbf{a}\rVert_1$, donc $\lVert\mathbf{a}\mathbf{b}^\top\rVert_1 = \lVert\mathbf{a}\rVert_1\lVert\mathbf{b}\rVert_\infty$. Contre-exemple : $\mathbf{a} = (1)$, $\mathbf{b} = (1, 1)$, la matrice $(1\ \ 1)$ a $\lVert\cdot\rVert_1 = 1$, et non 2.

**Erreurs fréquentes** : en a), confondre « tend vers 0 » et « s'annule » ; en b), ne pas voir que la transposée d'une circulante est circulante ; en c), oublier que $\rho \le \lVert\cdot\rVert_1$ ferme l'encadrement ; en d), croire qu'une matrice non nulle a un rayon spectral non nul ; en e), prendre le module des valeurs propres pour la norme ; en f), croire qu'une somme de suites géométriques positives garde son signe, alors que les coefficients peuvent être négatifs ; en g), additionner les pas ; en h), raisonner sur les rayons spectraux des facteurs ; en i), chercher une récurrence d'ordre 1 ; en j), ne vérifier que la norme 2.
**Remédiation** : a) M22.2, M22.Q1 ; b) M21.13, M22.Q3, M22.E2 ; c) M21.21, M22.12 ; d) M21.4, M21.Q3, M22.5 ; e) M22.3, M22.6, M22.Q2 ; f) M22.2, M22.R1 ; g) M21.5, M21.10, M21.Q4, M21.Q7 ; h) M22.11, M22.Q4 ; i) M22.3, M22.25 ; j) M21.R3, M22.11, M22.12.

## CP5.1 — Convolution de deux suites, corrélation croisée et matrice de Toeplitz ✏️ · 2 points

**Réponses** : a) `[2, 3, -5, -4, 5, -1]` · b) `4` · c) `[3, -5, 7]` · d) `[6, -4, 5, 7, -6, 1, 1, 1, -1]` · e) `[-4, 5, 7, -6, 1, 1]` · f) `[[2, 0, 0], [0, 2, 0], [-1, 0, 2], [1, -1, 0], [0, 1, -1], [0, 0, 1]]` · g) `120` · h) `[0, 1, -1, 0, 2, 0]`.

a) Le tableau des produits $a_ib_j$ (lignes $i$, colonnes $j$) : $(2, 0, -4, 2)$, $(3, 0, -6, 3)$, $(-1, 0, 2, -1)$. Le long des anti-diagonales : $2$ ; $0 + 3 = 3$ ; $-4 + 0 - 1 = -5$ ; $2 - 6 + 0 = -4$ ; $3 + 2 = 5$ ; $-1$. **[0,25]**
b) $\sum_m (-1)^m c_m = 2 - 3 - 5 + 4 + 5 + 1 = 4$. **[0,25]**
c) La fenêtre $i$ couvre $x_i, \ldots, x_{i+3}$, sans retournement : $2 \times 3 + 0 - 4 + 1 = 3$ ; $-4 + 0 - 1 + 0 = -5$ ; $8 + 0 - 0 - 1 = 7$. **[0,25]**
d) $(\mathbf{x} * \mathbf{w})_m = \sum_i x_i\,w_{m-i}$ : $6$ ; $-4$ ; $-3 + 8 = 5$ ; $3 + 2 + 2 = 7$ ; $-2 - 4 + 0 = -6$ ; $4 - 1 - 2 = 1$ ; $1$ ; $1$ ; $-1$. **[0,25]**
e) Le mode même taille de NumPy garde $n = 6$ valeurs de d), à partir de l'indice $\big\lfloor\frac{4 - 1}{2}\big\rfloor = 1$. **[0,25]**
f) La colonne $j$ de $\mathbf{T}$ est le noyau descendu de $j$ lignes, $T_{ij} = w_{i-j}$ ; forme $(3 + 4 - 1, 3) = (6, 3)$. **[0,25]**
g) Chaque colonne contient une copie du noyau, dont 3 coefficients sont non nuls (le 0 de $w_1$ ne donne rien) : $3 \times 40 = 120$, sur $43 \times 40 = 1\,720$ coefficients. **[0,25]**
h) Le mode valide garde les lignes $k - 1 = 3$ à $n - 1 = 5$ de la matrice pleine ; la ligne 1 de $\mathbf{V}$ est la ligne 4, de coefficients $V_{1,j} = w_{4-j}$ : $(w_4, w_3, w_2, w_1, w_0, w_{-1}) = (0, 1, -1, 0, 2, 0)$. **[0,25]**

Sur ta copie : b) est la valeur de $PQ$ en $X = -1$, donc $P(-1)\,Q(-1) = (2 - 3 - 1)(1 - 2 - 1) = (-2)(-2) = 4$, sans calculer a) ; e) commence à l'indice 1 de d) ; dans une ligne, $T_{ij} = w_{i-j}$ et l'indice du noyau **décroît** quand $j$ croît : une ligne lit le noyau retourné, comme la convolution retourne le noyau. (Pour aller plus loin, non noté : c) n'est pas la partie valide de d), $(7, -6, 1)$, parce que la corrélation ne retourne pas le noyau ; c'est la convolution valide par $\tilde{\mathbf{w}} = (1, -1, 0, 2)$, et $\mathbf{V}\mathbf{x} = (7, -6, 1)$.)

**Erreurs fréquentes** : en a), faire glisser $\mathbf{b}$ sans le retourner (une corrélation) ; en b), évaluer en $X = 1$ (la somme des termes vaut $4 \times 0 = 0$) ; en c), retourner le noyau (on obtient la partie valide de d), $(7, -6, 1)$) ; en d), ne pas le retourner ; en e), commencer à l'indice 0 ou 2 de d) ; en f), donner la matrice transposée, ou mettre le noyau retourné dans les colonnes ; en g), compter les $nk = 160$ places du noyau, zéro compris ; en h), lire le noyau dans l'ordre, $(0, 2, 0, -1, 1, 0)$.
**Remédiation** : M21.1, M21.2, M21.4, M21.Q1, M21.Q2, M21.Q3, M21.19, M21.20.

## CP5.2 — Positions d'une fenêtre, pas, dilatation, et la convolution transposée d'un signal ✏️ · 2 points

**Réponses** : a) `116` · b) `115` · c) `3` · d) `[105, 106, 107, 108]` · e) `[118, 2, 3]` · f) `[3, -2, -4, 4, 5, -6, 12, -4, 4]` · g) `149` · h) `[2, 3]`.

a) $\big\lfloor\frac{472 - 8 - 1}{4}\big\rfloor + 1 = \lfloor 115{,}75\rfloor + 1 = 116$. **[0,25]**
b) L'étendue de la fenêtre vaut $3 \times 8 + 1 = 25$ : $\big\lfloor\frac{472 + 10 - 24 - 1}{4}\big\rfloor + 1 = \lfloor 114{,}25\rfloor + 1 = 115$. **[0,25]**
c) La dernière fenêtre (numéro 115) commence à la case $4 \times 115 = 460$ et lit les cases 460 à 468 ; les cases 469, 470 et 471 ne sont jamais lues : 3. **[0,25]**
d) $\big\lfloor\frac{n - 9}{4}\big\rfloor + 1 = 25$ équivaut à $96 \le n - 9 \le 99$, soit $105 \le n \le 108$ : quatre longueurs, autant que le pas. **[0,25]**
e) $n_{\text{out}} = \big\lceil\frac{472}{4}\big\rceil = 118$ et $P_{\text{tot}} = (118 - 1) \times 4 + 8 + 1 - 472 = 5$ zéros en tout : $\lfloor\frac52\rfloor = 2$ au début, 3 à la fin. **[0,25]**
f) Les zéros insérés donnent $(1, 0, -2, 0, 3, 0, 2)$, puis la convolution pleine par $\mathbf{w}$, de $7 + 3 - 1 = 9$ valeurs. En tampons : $1 \cdot \mathbf{w} = (3, -2, 2)$ sur les cases 0 à 2, $-2\mathbf{w} = (-6, 4, -4)$ sur les cases 2 à 4, $3\mathbf{w} = (9, -6, 6)$ sur les cases 4 à 6, $2\mathbf{w} = (6, -4, 4)$ sur les cases 6 à 8 ; les cases 2, 4 et 6 en reçoivent deux : $2 - 6 = -4$, $-4 + 9 = 5$, $6 + 6 = 12$. **[0,25]**
g) $(m - 1)s - 2p + d(k - 1) + 1 + p_{\text{out}} = 147 - 4 + 4 + 1 + 1 = 149$. **[0,25]**
h) La case $j$ reçoit un tampon de chaque $i$ tel que $0 \le j - 4i \le 9$ : autant que de multiples de 4 parmi les 10 entiers consécutifs $j - 9, \ldots, j$, soit 2 ou 3 selon le reste de $j$ modulo 4 (le motif $3, 3, 2, 2$ se répète) : 4 ne divise pas 10, le nombre n'est pas constant. **[0,25]**

Sur ta copie : c) la dernière fenêtre lit les cases 460 à 468 ; e) avec 5 zéros, $\big\lfloor\frac{472 + 5 - 8 - 1}{4}\big\rfloor + 1 = 117 + 1 = 118$, et avec 4 zéros seulement on n'aurait que 117 positions ; f) les quatre tampons ci-dessus, les cases 2, 4 et 6 recevant chacune deux tampons (le pas 2 ne divise pas $k = 3$).

**Erreurs fréquentes** : en a), oublier le $+1$ (115) ou arrondir vers le haut (117) ; en b), oublier la dilatation (119), ne compter le padding qu'une fois, ou prendre $dk$ pour l'étendue (114) ; en c), faire finir la dernière fenêtre en $si + k$ ; en d), oublier le $+1$ ($[109, \ldots, 112]$) ; en e), garder la règle du pas 1, 4 zéros de chaque côté, ou mettre le zéro en trop au début ; en f), convoluer par le noyau retourné (on obtient $(2, -2, -1, 4, 0, -6, 13, -4, 6)$) ; en g), oublier $p_{\text{out}}$ (148) ou ajouter le padding au lieu de le retirer (157) ; en h), répondre $\lfloor\frac{10}{4}\rfloor = 2$ seulement.
**Remédiation** : M21.6, M21.7, M21.14, M21.Q5, M21.26.

## CP5.3 — Une grille filtrée par un noyau séparable : paramètres, coût et champ récepteur ✏️ · 2 points

**Réponses** : a) `[[2, 1, -1], [1, -1, 3]]` · b) `[[-4, 16, 17], [16, -6, 17]]` · c) `[54, 48]` · d) `11` · e) `552` · f) `1866240` · g) `122` · h) `[16, 4]`.

a) La ligne 0 de $\mathbf{K}$ est $a_0\mathbf{b}^\top$ : avec $b_0 = 1$, $a_0 = K_{0,0} = 2$ et $\mathbf{b} = \frac12(2, -2, 6) = (1, -1, 3)$ ; la colonne 0 est $b_0\,\mathbf{a} = (2, 1, -1)$. **[0,25]**
b) En deux passes. La passe verticale par $\mathbf{a}$, $V_{i,j} = 2G_{i,j} + G_{i+1,j} - G_{i+2,j}$, donne les lignes $(5, 6, -1, 3, 7)$ et $(4, 6, 6, -2, 3)$ ; la passe horizontale par $\mathbf{b}$, $Y_{i,j} = V_{i,j} - V_{i,j+1} + 3V_{i,j+2}$ : $5 - 6 - 3 = -4$, $6 + 1 + 9 = 16$, $-1 - 3 + 21 = 17$ ; $4 - 6 + 18 = 16$, $6 - 6 - 6 = -6$, $6 + 2 + 9 = 17$. **[0,25]**
c) En direct : 6 valeurs de sortie, 9 produits chacune, 54. En deux passes : la passe verticale calcule $2 \times 5 = 10$ valeurs de 3 produits (30), la passe horizontale $2 \times 3 = 6$ valeurs de 3 produits (18) : 48. **[0,25]**
d) La convolution retourne le noyau d'un demi-tour : $\sum_{u,v}K_{2-u,\,2-v}\,G_{u,v}$. En deux passes, avec $\tilde{\mathbf{a}} = (-1, 1, 2)$ sur les colonnes 0 à 2 : $-3 + 1 + 4 = 2$, $-1 + 4 + 0 = 3$, $0 + 2 + 6 = 8$ ; puis $\tilde{\mathbf{b}} = (3, -1, 1)$ : $6 - 3 + 8 = 11$. **[0,25]**
e) $C_{\text{out}}(C_{\text{in}}k_hk_w + 1) = 12 \times (5 \times 9 + 1) = 552$. **[0,25]**
f) $H_{\text{out}} = \big\lfloor\frac{96 + 2 - 2 - 1}{2}\big\rfloor + 1 = 48$ et $W_{\text{out}} = \big\lfloor\frac{144 + 2 - 2 - 1}{2}\big\rfloor + 1 = 72$ ; une multiplication-addition par poids et par position : $48 \times 72 \times 12 \times 5 \times 9 = 3\,456 \times 540 = 1\,866\,240$. **[0,25]**
g) Par canal : $5 \times (9 + 1) = 50$ ; $1 \times 1$ : $12 \times (5 + 1) = 72$ ; en tout 122, quatre fois et demie moins que e). **[0,25]**
h) $r_\ell = r_{\ell-1} + d_\ell(k_\ell - 1)J_{\ell-1}$, $J_\ell = J_{\ell-1}s_\ell$ : $r = 1 + 2 = 3$ ($J = 1$), puis $3 + 1 = 4$ ($J = 2$), puis $4 + 2 \times 2 \times 2 = 12$ ($J = 2$), puis $12 + 2 \times 2 = 16$ ($J = 4$) : champ récepteur 16, pas total 4. **[0,25]**

Sur ta copie : les trois lignes de $\mathbf{K}$ sont proportionnelles à $(1, -1, 3)$ (coefficients 2, 1 et $-1$) : $\mathbf{K}$ est un produit extérieur, de rang 1 ; la passe verticale vaut $\begin{pmatrix} 5 & 6 & -1 & 3 & 7 \\ 4 & 6 & 6 & -2 & 3 \end{pmatrix}$ ; la sortie de la situation 2 a la forme $(12, 48, 72)$.

**Erreurs fréquentes** : en a), échanger $\mathbf{a}$ et $\mathbf{b}$ ($\mathbf{a}$ donne les lignes) ; en b), retourner le noyau, ou appliquer $\mathbf{a}$ le long des lignes ; en c), ne compter la passe verticale que sur les 3 colonnes de la sortie (36), ou donner les comptes par valeur, 9 et 6 ; en d), ne retourner le noyau que selon un axe (23 ou 8), ou donner la corrélation ($-4$) ; en e), oublier les biais (540) ; en f), oublier le pas (7 464 960) ou le padding (1 801 980) ; en g), oublier les biais (105) ; en h), oublier la dilatation (12), additionner les noyaux, ou additionner les pas (6).
**Remédiation** : M21.8, M21.9, M21.10, M21.15, M21.22, M21.Q6, M21.Q7.

## CP5.4 — Équivariance, matrice circulante et le pire cas d'une perturbation bornée ✏️ · 1,5 point

**Réponses** : a) `[8, 10, -11, 8, -3]` · b) `[3, 1, -2, 2, -1]` · c) `[8, -3, 8, 10, -11]` · d) `[-0.2, 0.2, 0.2, -0.2, 0.2]` · e) `1.8` · f) `0.872`.

a) $z_m = \sum_i x_i\,h_{(m-i) \bmod 5}$, c'est-à-dire la ligne $m$ de $\operatorname{circ}(\mathbf{h})$ fois $\mathbf{x}$. Les lignes sont $(3, 1, -2, 2, -1)$, $(-1, 3, 1, -2, 2)$, $(2, -1, 3, 1, -2)$, $(-2, 2, -1, 3, 1)$, $(1, -2, 2, -1, 3)$ : $3 + 3 + 4 + 0 - 2 = 8$ ; $-1 + 9 - 2 + 0 + 4 = 10$ ; $2 - 3 - 6 + 0 - 4 = -11$ ; $-2 + 6 + 2 + 0 + 2 = 8$ ; $1 - 6 - 4 + 0 + 6 = -3$. **[0,25]**
b) Le coefficient $(0, j)$ vaut $h_{(-j) \bmod 5}$ : $(h_0, h_4, h_3, h_2, h_1) = (3, 1, -2, 2, -1)$. **[0,25]**
c) $\operatorname{circ}(\mathbf{h})$ commute avec $\mathbf{P}$ : $(\mathbf{P}^2\mathbf{x}) \circledast \mathbf{h} = \mathbf{P}^2\mathbf{z} = (z_3, z_4, z_0, z_1, z_2)$. **[0,25]**
d) L'écart sur $z_1$ est $\mathbf{r} \cdot \boldsymbol{\delta}$, avec $\mathbf{r} = (-1, 3, 1, -2, 2)$ la ligne 1 de $\operatorname{circ}(\mathbf{h})$ : sur la boule L∞, le maximum est atteint en $0{,}2\operatorname{signe}(\mathbf{r})$, unique puisque aucun coefficient n'est nul. **[0,25]**
e) $0{,}2\,\lVert\mathbf{r}\rVert_1 = 0{,}2 \times 9 = 1{,}8$ °C. **[0,25]**
f) $0{,}2\,\lVert\mathbf{r}\rVert_2 = 0{,}2\sqrt{19} \approx 0{,}872$ (Cauchy-Schwarz, atteint en $0{,}2\,\mathbf{r}/\lVert\mathbf{r}\rVert_2$). **[0,25]**

Sur ta copie : c) se lit sur a), par l'équivariance du cas périodique (décaler puis filtrer = filtrer puis décaler, sans aucun bord) ; la première ligne de $\operatorname{circ}(\mathbf{h})$ est le noyau retourné circulaire $\check{\mathbf{h}}$ (c'est la première colonne de $\operatorname{circ}(\mathbf{h})^\top = \operatorname{circ}(\check{\mathbf{h}})$) ; chaque ligne d'une matrice circulante contient tous les coefficients de $\mathbf{h}$, une fois chacun : $\lVert\mathbf{r}\rVert_1 = \lVert\mathbf{h}\rVert_1$ pour toute sortie $z_m$.

**Erreurs fréquentes** : en a), calculer la convolution pleine sans replier ses termes, ou une corrélation ; en b), donner la première colonne $\mathbf{h}$, ou le simple renversement $(1, -2, 2, -1, 3)$ ; en c), décaler dans l'autre sens ; en d), prendre les signes de $\mathbf{h}$ (la première colonne) au lieu de ceux de la ligne 1, ou de la ligne 0 ; en e), prendre $0{,}2\max\lvert h_i\rvert$ ou la somme des coefficients avec leurs signes (0,6) ; en f), oublier la racine carrée (3,8) ou garder la norme L1.
**Remédiation** : M21.5, M21.11, M21.13, M21.16, M21.21, M21.Q4, M21.Q8.

## CP5.5 — Une récurrence avec entrée : solution et réponse impulsionnelle ✏️ · 2 points

**Réponses** : a) `[9.08, 11.08]` · b) `[7.648, 10.48]` · c) `[0.646, 1.931]` · d) `[0, 0.3, 0.36, 0.336]` · e) `0.0264` · f) `2.16` · g) `[10, 10]` · h) `0.8`.

a) $\mathbf{x}_1 = \mathbf{A}\mathbf{x}_0 + \mathbf{B}u_0 = (10 + 0{,}4 + 6 ;\ 6 + 2{,}8) = (16{,}4 ;\ 8{,}8)$, puis $\mathbf{x}_2 = \mathbf{A}\mathbf{x}_1 = (8{,}2 + 0{,}88 ;\ 4{,}92 + 6{,}16) = (9{,}08 ;\ 11{,}08)$. **[0,25]**
b) $\mathbf{x}_3 = \mathbf{A}\mathbf{x}_2 + (2, 0) = (4{,}54 + 1{,}108 + 2 ;\ 2{,}724 + 7{,}756) = (7{,}648 ;\ 10{,}48)$. **[0,25]**
c) Trace $1{,}2$, déterminant $0{,}35 - 0{,}03 = 0{,}32$ : valeurs propres $0{,}8$ et $0{,}4$, de vecteurs propres $(1, 3)$ et $(1, -1)$. $\mathbf{x}_0 = 6\,(1, 3) + 14\,(1, -1)$, donc $\mathbf{A}^{10}\mathbf{x}_0 = 6 \times 0{,}8^{10}(1, 3) + 14 \times 0{,}4^{10}(1, -1) \approx (0{,}644245 + 0{,}001468 ;\ 1{,}932735 - 0{,}001468) \approx (0{,}646 ;\ 1{,}931)$. **[0,25]**
d) $h_0 = \mathbf{C}\mathbf{B} = 0$ ; $\mathbf{A}\mathbf{B} = (0{,}5 ;\ 0{,}3)$, $\mathbf{A}^2\mathbf{B} = (0{,}28 ;\ 0{,}36)$, $\mathbf{A}^3\mathbf{B} = (0{,}176 ;\ 0{,}336)$ : $(0 ;\ 0{,}3 ;\ 0{,}36 ;\ 0{,}336)$. **[0,25]**
e) $\mathbf{B} = \frac14(1, 3) + \frac34(1, -1)$, donc $\mathbf{A}^k\mathbf{B} = \frac14\,0{,}8^k(1, 3) + \frac34\,0{,}4^k(1, -1)$ et $h_k = \frac34\big(0{,}8^k - 0{,}4^k\big)$ ; $h_{15} = 0{,}75 \times (0{,}0351844 - 0{,}0000011) \approx 0{,}0264$. **[0,25]**
f) La réponse forcée de $\mathbf{x}_3$ est $\mathbf{A}^2\mathbf{B}u_0 + \mathbf{A}\mathbf{B}u_1 + \mathbf{B}u_2$, et sa sortie $h_2u_0 + h_1u_1 + h_0u_2 = 0{,}36 \times 6 + 0 + 0 = 2{,}16$. **[0,25]**
g) $(\mathbf{I} - \mathbf{A})\mathbf{x}^\star = (4, 0)$ : $0{,}5x_1 - 0{,}1x_2 = 4$ et $-0{,}3x_1 + 0{,}3x_2 = 0$, d'où $x_1 = x_2 = 10$. **[0,25]**
h) Les deux colonnes de $\mathbf{A}$ ont pour somme $0{,}8$ : $(1, 1)\,\mathbf{A} = 0{,}8\,(1, 1)$, donc $x_{t+1,1} + x_{t+1,2} = 0{,}8\,(x_{t,1} + x_{t,2})$ sans rejet. **[0,25]**

Sur ta copie : les vecteurs propres se vérifient, $\mathbf{A}(1, 3) = (0{,}8 ;\ 2{,}4)$ et $\mathbf{A}(1, -1) = (0{,}4 ;\ -0{,}4)$ ; $h_k = \frac34(0{,}8^k - 0{,}4^k)$ ; une colonne de $\mathbf{A}$ dit où va le polluant d'un lac (gardé, envoyé à l'autre) : sa somme est la part qui n'est pas éliminée, 80 % pour les deux lacs. (Pour aller plus loin, non noté : la réponse libre de $y_3$ vaut $8{,}32$ et $y_3 = 10{,}48 = 8{,}32 + 2{,}16$ ; le total à l'équilibre, 20, vérifie $20 = 0{,}8 \times 20 + 4$.)

**Erreurs fréquentes** : en a), multiplier par $\mathbf{A}^\top$ (on obtient $(10{,}04 ;\ 5{,}08)$), ou oublier le rejet $u_0$ ; en b), oublier $u_2$ ; en c), multiplier $\mathbf{x}_0$ par $0{,}8^{10}$ comme si c'était un vecteur propre ; en d), commencer à $h_1$, ou lire le coefficient $(1, 2)$ de $\mathbf{A}^k$ (le rejet dans le lac 2 mesuré dans le lac 1) ; en e), un décalage d'indice ($h_{14}$ ou $h_{16}$), ou oublier le facteur $\frac34$ ; en f), donner la réponse libre (8,32) ou $y_3$ tout entier (10,48), ou porter $u_0$ par $h_3$ ; en g), le système transposé ; en h), donner la plus petite valeur propre.
**Remédiation** : M22.1, M22.2, M22.7, M22.19, M22.Q1, M22.R1.

## CP5.6 — Valeurs propres complexes, rayon spectral, normes et croissance transitoire ✏️ · 2 points

**Réponses** : a) `[0.5, 0.5]` · b) `0.7071` · c) `"pi/4"` · d) `[[0, -1], [0.25, 0]]` · e) `[[-0.25, 0], [0, -0.25]]` · f) `[1.5, 1.5]` · g) `1.1754` · h) `[1, 2]`.

a) Trace 1, déterminant $0{,}25 + 0{,}25 = 0{,}5$ : $\lambda^2 - \lambda + 0{,}5 = 0$, de discriminant $-1$, d'où $\lambda = \frac{1 \pm i}{2} = 0{,}5 \pm 0{,}5\,i$. **[0,25]**
b) $\lvert\lambda\rvert = \sqrt{\det\mathbf{M}} = \sqrt{0{,}5} \approx 0{,}7071$. **[0,25]**
c) $\cos\theta = \frac{0{,}5}{\sqrt{0{,}5}} = \frac{\sqrt2}{2}$ et $\sin\theta > 0$ : $\theta = \frac\pi4$. **[0,25]**
d) $\mathbf{M}^2 = \begin{pmatrix} 0{,}25 - 0{,}25 & -0{,}5 - 0{,}5 \\ 0{,}125 + 0{,}125 & -0{,}25 + 0{,}25 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 0{,}25 & 0 \end{pmatrix}$. **[0,25]**
e) $\mathbf{M}^4 = (\mathbf{M}^2)^2 = \begin{pmatrix} -0{,}25 & 0 \\ 0 & -0{,}25 \end{pmatrix}$ : $\mathbf{M}$ est semblable à $\sqrt{0{,}5}\,\mathbf{R}_{\pi/4}$, et quatre pas font un demi-tour ($\mathbf{R}_\pi = -\mathbf{I}$) et un facteur $0{,}5^2$. **[0,25]**
f) Colonnes : $0{,}5 + 0{,}25 = 0{,}75$ et $1 + 0{,}5 = 1{,}5$ ; lignes : $1{,}5$ et $0{,}75$. **[0,25]**
g) $\mathbf{M}^\top\mathbf{M} = \begin{pmatrix} 0{,}3125 & -0{,}375 \\ -0{,}375 & 1{,}25 \end{pmatrix}$, de trace $1{,}5625$ et de déterminant $0{,}25$ : $\lambda_{\max} = \frac{1{,}5625 + \sqrt{1{,}5625^2 - 1}}{2} \approx 1{,}381543$, et $\lVert\mathbf{M}\rVert_2 \approx 1{,}1754$. **[0,25]**
h) $\rho(\mathbf{M}) < 1$ : les puissances tendent vers $\mathbf{0}$ (1). $\sqrt2\,\mathbf{M}$ a des valeurs propres de module 1, et $(\sqrt2\,\mathbf{M})^4 = 4\,\mathbf{M}^4 = -\mathbf{I}$ : ses puissances reviennent à $\mathbf{I}$ tous les 8 pas, bornées sans tendre vers $\mathbf{0}$ (2). **[0,25]**

Sur ta copie : $\mathbf{M}\,(0, 1) = (-1 ;\ 0{,}5)$, de norme $\sqrt{1{,}25} \approx 1{,}118 > 1$ : un pas peut allonger, alors que $\rho < 1$ ; $\lVert\mathbf{M}^2\rVert_2 = 1$ (valeurs singulières 1 et $0{,}25$) et $\lVert\mathbf{M}^4\rVert_2 = 0{,}25$ ; $\mathbf{M}$ n'est pas normale : $\mathbf{M}^\top\mathbf{M} \ne \mathbf{M}\mathbf{M}^\top = \begin{pmatrix} 1{,}25 & -0{,}375 \\ -0{,}375 & 0{,}3125 \end{pmatrix}$. (Pour aller plus loin, non noté : $\lVert\mathbf{M}^t\rVert_2$ vaut $1{,}175$ ; 1 ; $0{,}588$ ; $0{,}25$ ; $0{,}294$ ; $0{,}25$… : elle ne décroît pas à chaque pas ; et $\mathbf{M}^8 = \frac{1}{16}\mathbf{I}$ donne $\lVert\mathbf{M}^8\rVert_2^{1/8} = \rho(\mathbf{M})$ exactement.)

**Erreurs fréquentes** : en a), la valeur propre de partie imaginaire négative ; en b), prendre la partie réelle $\frac{\operatorname{tr}}{2} = 0{,}5$, ou $\det\mathbf{M} = 0{,}5$ sans la racine ; en c), $-\frac\pi4$ ; en d), élever chaque coefficient au carré ; en e), oublier le signe ($\mathbf{R}_\pi = -\mathbf{I}$) ; en f), additionner les coefficients avec leurs signes (0,75) ; en g), oublier la racine carrée (1,3815), donner $\rho$, ou la norme de Frobenius (1,25) ; en h), croire que $\sqrt2\,\mathbf{M}$ explose ou s'éteint.
**Remédiation** : M22.3, M22.4, M22.5, M22.6, M22.23, M22.Q2, M22.Q3, M22.Q4, M22.R2.

## CP5.7 — Produits de jacobiennes le long d'une trajectoire, et sensibilité à un paramètre utilisé à chaque pas ✏️ · 1,5 point

**Réponses** : a) `[3.25, 1.25]` · b) `[[3.25, -0.5], [0, 2.25]]` · c) `[8.75, 3.75]` · d) `[-3.6, -3.75, -4]` · e) `-11.35` · f) `-1.135`.

a) $\mathbf{p}_1 = f(2, 1) = (1 + 1 ;\ 2 - 0{,}5) = (2 ;\ 1{,}5)$, puis $\mathbf{p}_2 = (1 + 2{,}25 ;\ 2 - 0{,}75) = (3{,}25 ;\ 1{,}25)$. **[0,25]**
b) $\mathbf{J}_f(x, y) = \begin{pmatrix} 0{,}5 & 2y \\ 1 & -0{,}5 \end{pmatrix}$, évaluée en $\mathbf{p}_0$ et en $\mathbf{p}_1$ ; la jacobienne du dernier pas à gauche : $\mathbf{J}_f(\mathbf{p}_1)\,\mathbf{J}_f(\mathbf{p}_0) = \begin{pmatrix} 0{,}5 & 3 \\ 1 & -0{,}5 \end{pmatrix}\begin{pmatrix} 0{,}5 & 2 \\ 1 & -0{,}5 \end{pmatrix} = \begin{pmatrix} 3{,}25 & -0{,}5 \\ 0 & 2{,}25 \end{pmatrix}$. **[0,25]**
c) Sommes de lignes : $\lVert\mathbf{J}_f(\mathbf{p}_0)\rVert_\infty = 2{,}5$, $\lVert\mathbf{J}_f(\mathbf{p}_1)\rVert_\infty = 3{,}5$, produit $8{,}75$ ; et $\lVert\cdot\rVert_\infty$ de b) vaut $\max(3{,}75 ;\ 2{,}25) = 3{,}75$, bien sous la majoration. **[0,25]**
d) Avec $\beta = 2$ : $x_1 = 36 - 12 + 1 = 25$, $x_2 = 16$, $x_3 = 9$. $J_t = 1 - \frac{\beta}{2\sqrt{x_t}} = 1 - \frac{1}{\sqrt{x_t}}$, soit $\frac56$, $\frac45$, $\frac34$ ; $b_t = -\sqrt{x_t}$, soit $-6$, $-5$, $-4$. Le terme du pas $k$ est $J_2\cdots J_{k+1}\,b_k$ : $\frac34 \times \frac45 \times (-6) = -3{,}6$ ; $\frac34 \times (-5) = -3{,}75$ ; $-4$. **[0,25]**
e) $s_3 = -3{,}6 - 3{,}75 - 4 = -11{,}35$. **[0,25]**
f) $0{,}1 \times (-11{,}35) = -1{,}135$ cm. **[0,25]**

Sur ta copie : pas à pas, $s_1 = b_0 = -6$, $s_2 = \frac45 \times (-6) - 5 = -9{,}8$, $s_3 = \frac34 \times (-9{,}8) - 4 = -11{,}35$ ; avec $\beta = 2{,}1$, $x_1 = 24{,}4$, $x_2 \approx 15{,}0268$, $x_3 \approx 7{,}8862$ : le changement exact vaut environ $-1{,}114$, un peu moins en valeur absolue que $-1{,}135$, parce que $x_3$ n'est pas affine en $\beta$ (le premier ordre néglige les termes en $(\Delta\beta)^2$).

**Erreurs fréquentes** : en a), s'arrêter à $\mathbf{p}_1$ ; en b), multiplier dans l'ordre du temps (on obtient $\begin{pmatrix} 2{,}25 & 0{,}5 \\ 0 & 3{,}25 \end{pmatrix}$), ou évaluer les deux jacobiennes au même point ; en c), prendre les sommes de colonnes, ou la norme du produit dans le mauvais ordre (3,25) ; en d), oublier les jacobiennes des pas suivants ($-6$, $-5$, $-4$), ou ranger les termes dans l'autre ordre ; en e), la somme des $b_t$ ($-15$), ou le seul dernier terme ; en f), oublier de multiplier par $\Delta\beta$.
**Remédiation** : M22.8, M22.9, M22.15, M22.21, M22.Q6, M22.Q7, M22.R3.

## CP5.8 — Une démonstration au choix ∂ · 2 points

Toute démonstration juste et complète d'une étape a tous les points de cette étape, même si elle prend un autre chemin que celui du corrigé.

### Sujet A — Une convolution pleine par un noyau non nul est injective

1. **[0,5]** Pour des réels $\lambda$, $\mu$ : $\big((\lambda\mathbf{x} + \mu\mathbf{x}') * \mathbf{w}\big)_m = \sum_i(\lambda x_i + \mu x'_i)\,w_{m-i} = \lambda(\mathbf{x} * \mathbf{w})_m + \mu(\mathbf{x}' * \mathbf{w})_m$ : $\mathcal{C}$ est linéaire. Si $\mathcal{C}$ est injective et $\mathbf{x} * \mathbf{w} = \mathbf{0} = \mathbf{0} * \mathbf{w}$, alors $\mathbf{x} = \mathbf{0}$. Réciproquement, si seul $\mathbf{0}$ a une image nulle et si $\mathbf{x} * \mathbf{w} = \mathbf{x}' * \mathbf{w}$, la linéarité donne $(\mathbf{x} - \mathbf{x}') * \mathbf{w} = \mathbf{0}$, donc $\mathbf{x} = \mathbf{x}'$.
2. **[0,5]** $(\mathbf{x} * \mathbf{w})_{p+q} = \sum_i x_i\,w_{p+q-i}$. Un terme n'est non nul que si $x_i \ne 0$, donc $i \le p$, et $w_{p+q-i} \ne 0$, donc $p + q - i \le q$, soit $i \ge p$ : il ne reste que $i = p$, et $(\mathbf{x} * \mathbf{w})_{p+q} = x_pw_q \ne 0$. Tout $\mathbf{x} \ne \mathbf{0}$ a donc une image non nulle : $\mathcal{C}$ est injective (question 1), son noyau est $\{\mathbf{0}\}$, et, par le théorème du rang, sa matrice de Toeplitz, de forme $(n + k - 1, n)$, est de rang $n$. (En polynômes : le degré du produit est la somme des degrés, et son coefficient dominant est le produit des coefficients dominants.)
3. **[0,5]** Par la question 2 appliquée à $\mathbf{x}$ de longueur 3, le dernier coefficient de $\mathbf{y}$ est $y_4 = x_2w_2$ : $x_2 = \frac{2}{-2} = -1$. Puis $y_3 = x_1w_2 + x_2w_1$ : $-1 = -2x_1 - 1$, $x_1 = 0$ ; $y_2 = x_0w_2 + x_1w_1 + x_2w_0$ : $-10 = -2x_0 + 0 - 4$, $x_0 = 3$. On vérifie les deux premières équations : $y_0 = 3 \times 4 = 12$ et $y_1 = 3 \times 1 + 0 \times 4 = 3$. $\mathbf{x} = (3, 0, -1)$ est le seul, parce que $\mathcal{C}$ est injective : deux signaux de même image sont égaux.
4. **[0,5]** $(\mathbf{x} \circledast \mathbf{h})_m = x_m - x_{(m-1) \bmod 4}$ : $\mathbf{x} = (1, 1, 1, 1)$ (tout signal constant non nul) donne $\mathbf{0}$. L'étape qui tombe est la question 2 : les indices se lisent modulo $n$, et l'indice $p + q$ « déborde » et revient au début ; ici $p = 3$, $q = 1$, et le terme $x_3h_1$ tombe à l'indice $(3 + 1) \bmod 4 = 0$, où il s'ajoute à $x_0h_0$ : $1 - 1 = 0$. Il n'y a plus de « dernier coefficient » seul. (C'est la convolution pleine repliée modulo $n$ : le repliement peut annuler des termes.)

**Grille de relecture.** (1) la linéarité écrite sur la formule, et l'équivalence « injective ⇔ seul $\mathbf{0}$ a une image nulle » dans les deux sens ; (2) le coefficient d'indice $p + q$ réduit à un seul terme, la conclusion, et le rang $n$ ; (3) le calcul à partir du dernier coefficient, une vérification des équations restantes, et l'unicité par l'injectivité ; (4) un signal non nul du noyau, et le repliement modulo $n$ comme raison. Une démonstration par le **premier** coefficient non nul (le plus petit indice), par les matrices échelonnées ou par les polynômes est aussi juste.

### Sujet B — La série I + A + A² + … quand ‖A‖ < 1

1. **[0,5]** Si $(\mathbf{I} - \mathbf{A})\mathbf{x} = \mathbf{0}$, alors $\mathbf{x} = \mathbf{A}\mathbf{x}$, et $\lVert\mathbf{x}\rVert = \lVert\mathbf{A}\mathbf{x}\rVert \le \lVert\mathbf{A}\rVert\,\lVert\mathbf{x}\rVert$, donc $(1 - \lVert\mathbf{A}\rVert)\lVert\mathbf{x}\rVert \le 0$ ; comme $1 - \lVert\mathbf{A}\rVert > 0$, $\lVert\mathbf{x}\rVert = 0$ et $\mathbf{x} = \mathbf{0}$. Le noyau de $\mathbf{I} - \mathbf{A}$ est $\{\mathbf{0}\}$ ; c'est une matrice carrée $n \times n$, de rang $n$ par le théorème du rang : elle est inversible.
2. **[0,5]** $\mathbf{x} - \mathbf{A}\mathbf{x} = \mathbf{y}$, donc $\mathbf{x} = \mathbf{y} + \mathbf{A}\mathbf{x}$ et, par l'inégalité triangulaire, $\lVert\mathbf{x}\rVert \le \lVert\mathbf{y}\rVert + \lVert\mathbf{A}\rVert\,\lVert\mathbf{x}\rVert$, d'où $\lVert\mathbf{x}\rVert \le \frac{\lVert\mathbf{y}\rVert}{1 - \lVert\mathbf{A}\rVert}$. Pour tout $\mathbf{y} \ne \mathbf{0}$, $\frac{\lVert(\mathbf{I} - \mathbf{A})^{-1}\mathbf{y}\rVert}{\lVert\mathbf{y}\rVert} \le \frac{1}{1 - \lVert\mathbf{A}\rVert}$ ; la norme induite, le maximum de ce rapport, l'est aussi.
3. **[0,5]** $(\mathbf{I} - \mathbf{A})\mathbf{M} = \mathbf{I}$ s'écrit $\mathbf{M} - \mathbf{A}\mathbf{M} = \mathbf{I}$, soit $\mathbf{M} = \mathbf{I} + \mathbf{A}\mathbf{M}$. Et $\mathbf{S}_N = \mathbf{I} + \mathbf{A}(\mathbf{I} + \cdots + \mathbf{A}^{N-1}) = \mathbf{I} + \mathbf{A}\mathbf{S}_{N-1}$. En soustrayant, $\mathbf{E}_N = \mathbf{A}(\mathbf{M} - \mathbf{S}_{N-1}) = \mathbf{A}\mathbf{E}_{N-1}$, donc $\mathbf{E}_N = \mathbf{A}^N\mathbf{E}_0$, avec $\mathbf{E}_0 = \mathbf{M} - \mathbf{I} = \mathbf{A}\mathbf{M}$ : $\mathbf{E}_N = \mathbf{A}^{N+1}\mathbf{M}$. Par la sous-multiplicativité et la question 2, $\lVert\mathbf{E}_N\rVert \le \lVert\mathbf{A}\rVert^{N+1}\,\lVert\mathbf{M}\rVert \le \frac{\lVert\mathbf{A}\rVert^{N+1}}{1 - \lVert\mathbf{A}\rVert}$, qui tend vers 0 (R5). Chaque coefficient de $\mathbf{E}_N$ est au plus sa norme induite : $\mathbf{S}_N \to \mathbf{M}$ coefficient par coefficient, c'est-à-dire $(\mathbf{I} - \mathbf{A})^{-1} = \sum_{t \ge 0}\mathbf{A}^t$.
4. **[0,5]** Colonnes : $0{,}5 + 0{,}6 = 1{,}1$ et $0{,}3 + 0{,}2 = 0{,}5$, donc $\lVert\mathbf{A}\rVert_1 = 1{,}1$ ; lignes : $0{,}8$ et $0{,}8$, donc $\lVert\mathbf{A}\rVert_\infty = 0{,}8 < 1$. Il suffit d'**une** norme induite plus petite que 1 : les questions 1 à 3 s'appliquent avec $\lVert\cdot\rVert_\infty$. $\mathbf{I} - \mathbf{A} = \begin{pmatrix} 0{,}5 & -0{,}3 \\ -0{,}6 & 1{,}2 \end{pmatrix}$, de déterminant $0{,}42$ : $(\mathbf{I} - \mathbf{A})^{-1} = \frac{1}{0{,}42}\begin{pmatrix} 1{,}2 & 0{,}3 \\ 0{,}6 & 0{,}5 \end{pmatrix} = \begin{pmatrix} \frac{20}{7} & \frac57 \\ \frac{10}{7} & \frac{25}{21} \end{pmatrix}$, de norme $\lVert\cdot\rVert_\infty = \max\big(\frac{25}{7}, \frac{55}{21}\big) = \frac{25}{7} \approx 3{,}57$, sous la borne $\frac{1}{1 - 0{,}8} = 5$. Pour $\mathbf{A} = 2\mathbf{I}$ : $\mathbf{I} - \mathbf{A} = -\mathbf{I}$ est inversible, mais $\mathbf{S}_N = (1 + 2 + \cdots + 2^N)\,\mathbf{I} = (2^{N+1} - 1)\,\mathbf{I}$ ne converge pas : l'inversibilité ne suffit pas, il faut l'hypothèse sur la norme (ou sur le rayon spectral).

**Grille de relecture.** (1) $\mathbf{x} = \mathbf{A}\mathbf{x}$, l'inégalité stricte $\lVert\mathbf{A}\rVert < 1$ utilisée, et le passage d'injective à inversible pour une matrice carrée ; (2) $\mathbf{x} = \mathbf{y} + \mathbf{A}\mathbf{x}$, l'inégalité triangulaire, et le passage au maximum qui définit la norme induite ; (3) les deux relations, la récurrence de l'écart, sa majoration par la sous-multiplicativité et la question 2, et la convergence ; (4) les deux normes, la raison pour laquelle une seule suffit, l'inverse calculé et comparé à 5, et le contre-exemple $2\mathbf{I}$ commenté. Une démonstration de la question 3 par le télescopage $(\mathbf{I} - \mathbf{A})\mathbf{S}_N = \mathbf{I} - \mathbf{A}^{N+1}$ est aussi juste.

**Erreurs fréquentes** (deux sujets) : en A, conclure de « un coefficient non nul » sans dire lequel, oublier de vérifier les équations restantes en 3, ou chercher en 4 un signal non nul qui ne soit pas dans le noyau ; en B, diviser par $1 - \lVert\mathbf{A}\rVert$ sans dire qu'il est positif, passer d'injective à inversible sans dire que la matrice est carrée, ou conclure en 4 avec $\lVert\mathbf{A}\rVert_1$.
**Remédiation** : A : M21.4, M21.12, M21.13, M21.20, M21.R2 ; B : M22.11, M22.13, M22.14, M22.Q4, M22.R2.

## CP5.9 — Corriger une copie : cinq erreurs 🐛 · 1,25 point

**Réponse de a)** : `"ABDEG"`. **[0,5]** (0,1 par lettre juste, −0,1 par lettre en trop, sans descendre sous 0)

b) Une ligne par erreur **[0,15 chacune]** :
- **(A)** La somme des termes d'une convolution est le **produit** des sommes (évaluer les polynômes en $X = 1$) : $(4 - 3 + 1) \times (2 + 5) = 2 \times 7 = 14$.
- **(B)** La matrice a 6 colonnes : son rang est au plus 6, et il vaut 6 (une convolution pleine par un noyau non nul est injective) ; 8 est le nombre de lignes.
- **(D)** Le coût est proportionnel à $k_hk_w$ : passer de $3 \times 3 = 9$ à $6 \times 6 = 36$ poids par canal multiplie les multiplications-additions par **4**.
- **(E)** $\lVert\mathbf{A}^{10}\rVert_2 \le \lVert\mathbf{A}\rVert_2^{10}$ n'est qu'une majoration : ici $\mathbf{A}^2 = \mathbf{I}$, donc $\mathbf{A}^{10} = \mathbf{I}$ et $\lVert\mathbf{A}^{10}\rVert_2 = 1$.
- **(G)** Chaque usage de $\beta$ est porté jusqu'au pas 3 par les jacobiennes des pas **suivants** : $s_3 = J_2J_1\,b_0 + J_2\,b_1 + b_2$.

Les lignes justes : (C) $(m - 1)s + k = 12 + 5 = 17$, la taille d'une convolution transposée sans padding ; (F) $\rho(\mathbf{A}) = 0{,}5 < 1$ (triangulaire), donc $\mathbf{A}^t \to \mathbf{0}$, quelle que soit la norme d'un pas ; (H) $\mathbf{B} = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ est la multiplication par $0{,}25 + 0{,}6\,i$, de module $\sqrt{0{,}0625 + 0{,}36} = 0{,}65$ : une rotation et une homothétie de rapport $0{,}65$, qui multiplie **toutes** les longueurs par $0{,}65$ à chaque pas.

**Erreurs fréquentes** : laisser passer (A) en additionnant les sommes ; laisser passer (B) en confondant le nombre de lignes et le rang ; laisser passer (D) en comptant le côté du noyau au lieu de son aire ; laisser passer (E) en prenant la sous-multiplicativité pour une égalité ; croire (F) fausse à cause de la norme ; laisser passer (G) en oubliant le chemin à travers l'état ; croire (H) fausse parce qu'une matrice non symétrique « ne garde pas les normes » (une rotation-homothétie est normale).
**Remédiation** : M21.4, M21.7, M21.9, M21.Q2, M21.27, M22.5, M22.11, M22.15, M22.3, M22.26.

## CP5.10 — Problème de synthèse : un filtre récursif et un filtre à réponse finie, du signal à la stabilité 🔗 · 2,25 points

**Réponses** : a) `[0, 0.4, 0.48, 0.352, 0.1536]` · b) `[0, 1.6, 1.12, 0.448, 1.1104]` · c) `0.7483` · d) `[1.1, 1.1, 0.8]` · e) `28` · f) `1.3984` · g) `"10/9"` · h) `"4/3"` · i) `2`.

a) $h_k$ est la seconde coordonnée de $\mathbf{A}^k\mathbf{B}$ : $\mathbf{B} = (1, 0)$, $\mathbf{A}\mathbf{B} = (0{,}6 ;\ 0{,}4)$, $\mathbf{A}^2\mathbf{B} = (0{,}16 ;\ 0{,}48)$, $\mathbf{A}^3\mathbf{B} = (-0{,}144 ;\ 0{,}352)$, $\mathbf{A}^4\mathbf{B} = (-0{,}2624 ;\ 0{,}1536)$. **[0,25]**
b) $y_{t+1} = \sum_{k \le t}h_{t-k}u_k$ : $y_1 = 0$ ; $y_2 = 0{,}4 \times 4 = 1{,}6$ ; $y_3 = 0{,}48 \times 4 + 0{,}4 \times (-2) = 1{,}12$ ; $y_4 = 0{,}352 \times 4 + 0{,}48 \times (-2) + 0 = 0{,}448$ ; $y_5 = 0{,}1536 \times 4 + 0{,}352 \times (-2) + 0 + 0{,}4 \times 3 = 1{,}1104$. **[0,25]**
c) Trace $1{,}2$, déterminant $0{,}36 + 0{,}2 = 0{,}56$, discriminant $1{,}44 - 2{,}24 < 0$ : $\lambda = 0{,}6 \pm i\sqrt{0{,}2}$, de module $\sqrt{0{,}56} \approx 0{,}7483$. **[0,25]**
d) Colonnes : $1$ et $1{,}1$ ; lignes : $1{,}1$ et $1$. $\mathbf{A}^\top\mathbf{A} = \begin{pmatrix} 0{,}52 & -0{,}06 \\ -0{,}06 & 0{,}61 \end{pmatrix}$, de trace $1{,}13$ et de déterminant $0{,}3136$ : valeurs propres $\frac{1{,}13 \pm 0{,}15}{2}$, soit $0{,}64$ et $0{,}49$, et $\lVert\mathbf{A}\rVert_2 = \sqrt{0{,}64} = 0{,}8$. **[0,25]**
e) $\lvert y_t - z_t\rvert = \big\lvert\sum_{k \ge K}h_ku_{t-1-k}\big\rvert \le \sum_{k \ge K}\lvert h_k\rvert \le \sum_{k \ge K}0{,}8^k = \frac{0{,}8^K}{0{,}2}$ (une série géométrique). Il faut $0{,}8^K \le 0{,}002$, soit $K \ge \frac{\ln 500}{\ln 1{,}25} \approx 27{,}85$ : $K = 28$. **[0,25]**
f) $z_t = \sum_{k=0}^{5}g_k\,u_{t-1-k}$ est une forme linéaire en les entrées, de poids $\mathbf{g}$ ; sur la boule L∞ de rayon 1, son maximum vaut $\lVert\mathbf{g}\rVert_1$ (M21 §8). $h_5 = -0{,}0128$ (la seconde coordonnée de $\mathbf{A}^5\mathbf{B} = (-0{,}23424 ;\ -0{,}0128)$), donc $\lVert\mathbf{g}\rVert_1 = 0 + 0{,}4 + 0{,}48 + 0{,}352 + 0{,}1536 + 0{,}0128 = 1{,}3984$. **[0,25]**
g) À l'équilibre, $\mathbf{x}^\star = (\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}$, et $y_t \to \mathbf{C}\mathbf{x}^\star$ puisque $\rho(\mathbf{A}) < 1$. $\mathbf{I} - \mathbf{A} = \begin{pmatrix} 0{,}4 & 0{,}5 \\ -0{,}4 & 0{,}4 \end{pmatrix}$, de déterminant $0{,}36$ : $\mathbf{x}^\star = \frac{1}{0{,}36}(0{,}4 ;\ 0{,}4)$, et $y_t \to \frac{0{,}4}{0{,}36} = \frac{10}{9}$ (c'est aussi $\sum_k h_k$). **[0,25]**
h) $\operatorname{tr}\mathbf{A}(\gamma) = \gamma + 0{,}6$ et $\det\mathbf{A}(\gamma) = 0{,}6\gamma - (-0{,}5)(0{,}4) = 0{,}6\gamma + 0{,}2$. Les valeurs propres sont les racines de $\lambda^2 - \operatorname{tr}\,\lambda + \det$, et le critère de M19 §6 (avec $p = \operatorname{tr}$ et $q = \det$) dit qu'elles sont toutes deux de module $< 1$ si et seulement si $\lvert\det\rvert < 1$ et $\lvert\operatorname{tr}\rvert < 1 + \det$. $\lvert\det\rvert < 1$ donne $-2 < \gamma < \frac43$ ; $\operatorname{tr} < 1 + \det$ donne $\gamma < 1{,}5$ et $-\operatorname{tr} < 1 + \det$ donne $\gamma > -1{,}125$. Les quatre ensemble : $-1{,}125 < \gamma < \frac43$, de borne supérieure $\frac43$, fixée par le déterminant. Autre chemin, aussi juste : quand les valeurs propres sont complexes ($\operatorname{tr}^2 < 4\det$, le cas en $\gamma = \frac43$, où $\operatorname{tr}^2 \approx 3{,}74 < 4$), leur module vaut $\sqrt{\det}$ (M22 §2), et $\rho < 1$ équivaut à $\det < 1$ ; au-delà de $\frac43$, $\det > 1$, et des valeurs propres réelles de produit $\det > 1$ ne peuvent pas non plus être toutes deux de valeur absolue $\le 1$. **[0,25]**
i) Pour $\gamma = \frac43$, $\det = 1$ et $\operatorname{tr} = \frac{29}{15} < 2$ : deux valeurs propres complexes conjuguées, distinctes, de module 1. La matrice est diagonalisable sur $\mathbb{C}$, ses puissances restent bornées sans tendre vers $\mathbf{0}$ (une ellipse) : 2. **[0,25]**

Sur ta copie :
- Les valeurs propres de $\mathbf{A}$ : $0{,}6 \pm 0{,}4472\,i$ ; la réponse impulsionnelle oscille en s'amortissant ($h_5 < 0$) : c'est un filtre résonant, qui dépasse sa valeur finale (g) avant de s'y installer.
- $\lVert\mathbf{A}\rVert_1 = \lVert\mathbf{A}\rVert_\infty = 1{,}1 > 1$ : la majoration $\lvert h_k\rvert \le 1{,}1^k$ grandit et ne borne aucune queue ; une seule norme induite plus petite que 1 suffit, ici $\lVert\cdot\rVert_2$.
- f) est atteint, pour $t = 6$, par les entrées $u_5$ quelconque, $u_4 = u_3 = u_2 = u_1 = 1$ et $u_0 = -1$ (les signes des poids, lus dans l'ordre inverse du temps).
- Le filtre récursif coûte, par sortie, les 4 multiplications de $\mathbf{A}\mathbf{x}_t$ ($\mathbf{B}$ et $\mathbf{C}$ ne font que placer et lire une coordonnée), avec 2 nombres en mémoire ; le filtre à réponse finie de e) coûte 28 multiplications et garde 28 entrées en mémoire.
- h) Les deux conditions sont $\lvert\det\mathbf{A}(\gamma)\rvert < 1$ et $\lvert\operatorname{tr}\mathbf{A}(\gamma)\rvert < 1 + \det\mathbf{A}(\gamma)$ ; celle qui décide, à droite, est $\det < 1$ : en $\gamma = \frac43$, deux valeurs propres complexes de module 1 sortent du disque unité, alors que la condition sur la trace ne jouerait qu'à partir de $1{,}5$. (Pour aller plus loin, non noté : à gauche, en $\gamma = -1{,}125$, c'est la condition sur la trace qui tombe, et une valeur propre réelle passe par $-1$.)
- Pour aller plus loin (non noté) : la vraie queue $\sum_{k \ge 28}\lvert h_k\rvert$ vaut environ $0{,}0006$, quinze fois moins que la borne : la norme 2 ($0{,}8$) majore chaque pas, alors que le rythme réel à long terme est $\rho \approx 0{,}748$.

**Erreurs fréquentes** : en a), lire le coefficient $(1, 2)$ de $\mathbf{A}^k$, ou commencer à $h_1$ ; en b), oublier le décalage d'un pas ($y_t = (\mathbf{h} * \mathbf{u})_t$) ; en c), donner la partie réelle (0,6) ou le déterminant (0,56) ; en d), oublier la racine carrée (0,64), ou donner $\rho$ pour $\lVert\mathbf{A}\rVert_2$ ; en e), arrondir vers le bas (27), utiliser $\rho$ (ce n'est pas une majoration de chaque pas), ou oublier le facteur $\frac{1}{1 - \lVert\mathbf{A}\rVert}$ de la queue (21) ; en f), additionner les poids avec leurs signes (1,3728), ou ne garder que 4 termes ; en g), inverser $\mathbf{I} - \mathbf{A}^\top$, ou ne sommer que quelques termes de $\mathbf{h}$ ; en h), ne garder que la condition sur la trace (1,5), exiger que la partie réelle $\frac{\operatorname{tr}}{2}$ soit plus petite que 1 ($\frac75$), alors que le module dépend aussi de la partie imaginaire, ou oublier le terme $-(-0{,}5)(0{,}4)$ du déterminant ($\frac53$) ; en i), conclure à l'explosion ou à l'extinction.
**Remédiation** : M21.11, M21.16, M22.2, M22.4, M22.6, M22.11, M22.19, M22.Q3, M22.R2.

## Barème récapitulatif et remédiation

| Question | Points | Chapitres | Si tu as moins de la moitié des points, refais… |
|---|---|---|---|
| CP5.Q1 | 1,5 | M21, M22 | les exercices cités au CP5.Q1, puis les quiz et les flashcards des deux chapitres |
| CP5.1 | 2 | M21 | M21.1, M21.2, M21.4, M21.19, M21.20, M21.Q1, M21.Q2, M21.Q3 |
| CP5.2 | 2 | M21 | M21.6, M21.7, M21.14, M21.26, M21.Q5 |
| CP5.3 | 2 | M21 | M21.8, M21.9, M21.10, M21.15, M21.22, M21.Q6, M21.Q7 |
| CP5.4 | 1,5 | M21 | M21.5, M21.11, M21.13, M21.16, M21.21, M21.Q4, M21.Q8 |
| CP5.5 | 2 | M22 | M22.1, M22.2, M22.7, M22.19, M22.Q1, M22.R1 |
| CP5.6 | 2 | M22 | M22.3, M22.4, M22.5, M22.6, M22.23, M22.Q2, M22.Q3, M22.Q4, M22.R2 |
| CP5.7 | 1,5 | M22 | M22.8, M22.9, M22.15, M22.21, M22.Q6, M22.Q7, M22.R3 |
| CP5.8 | 2 | M21 ou M22 | A : M21.4, M21.12, M21.13, M21.20, M21.R2 ; B : M22.11, M22.13, M22.14, M22.Q4, M22.R2 |
| CP5.9 | 1,25 | M21, M22 | M21.4, M21.7, M21.9, M21.27, M21.Q2, M22.3, M22.5, M22.11, M22.15, M22.26 |
| CP5.10 | 2,25 | M21, M22 | M21.11, M21.16, M22.2, M22.4, M22.6, M22.11, M22.19, M22.Q3, M22.R2 |
| **Total** | **20** | | |

**Lire ta note**
- **16 à 20** : la partie V est solide. Passe au checkpoint V de workbookIA ; garde les flashcards de M21 et M22 dans tes révisions.
- **12 à moins de 16** : c'est bien. Fais la remédiation des questions où tu as eu moins de la moitié des points, puis passe au checkpoint V de workbookIA.
- **8 à moins de 12** : avant le checkpoint V de workbookIA, fais la remédiation, relis ta synthèse et les fiches de M21 et M22.
- **Moins de 8** : reprends les exercices ★★ des sections où tu as perdu le plus de points, puis refais l'examen une semaine plus tard.

Dans tous les cas, **refais dans une semaine** les questions où tu as eu moins de la moitié des points, sans regarder ce corrigé : c'est l'effort de rappel qui fixe les notions. Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`.
