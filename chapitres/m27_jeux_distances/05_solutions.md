# M27 · Jeux et distances entre lois — solutions

> À lire **après** avoir cherché (et ouvert les indices de `04_indices.md`). Pour chaque exercice : les réponses, la démarche, les erreurs fréquentes et une variante ; pour une démonstration, une rédaction modèle et une grille de relecture, qui accepte toute démonstration correcte. Les exercices du notebook sont corrigés dans `05_solutions.ipynb` ; leur résumé est à la fin.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M27.Q1 — Maximin, minimax et point selle : qui annonce son coup en premier, et qui y gagne ?
1. Les minimums des lignes valent 1 et 5 : maximin 5. Les maximums des colonnes valent 6, 9 et 7 : minimax 6. Pas de point selle.
2. La ligne 2, qui lui assure 5 : la colonne y répond par la colonne 2.
3. La colonne 1, qui ne coûte jamais plus de 6 : la ligne y répond par la ligne 2, et gagne 6.
4. Vrai : maximin $\le$ minimax (∂ M27.11) ; l'écart, ici 1, va à celui qui joue en second.
5. Faux : c'est l'inverse, le plus **petit** de sa ligne et le plus **grand** de sa colonne.

### M27.Q2 — Stratégies mixtes, gain espéré et valeur d'un jeu : vrai ou faux
1. Vrai : contre $\mathbf{q}$ fixé, le gain espéré $\mathbf{p}^\top(\mathbf{G}\mathbf{q})$ est une moyenne des gains des lignes pures, $(\mathbf{G}\mathbf{q})_i$, qui ne dépasse pas le plus grand d'entre eux.
2. $\mathbf{G}\mathbf{q} = (0{,}5 \times 6 - 0{,}5 \times 1 ;\ 0{,}5 \times 2 + 0{,}5 \times 3) = (2{,}5 ;\ 2{,}5)$, puis $0{,}25 \times 2{,}5 + 0{,}75 \times 2{,}5 = 2{,}5$. Le résultat ne dépend pas de $p$ : $q = 0{,}5$ est justement le $q^\star$ de ce jeu, qui rend les deux lignes indifférentes, et 2,5 sa valeur.
3. Vrai (théorème de von Neumann).
4. Faux : $p^\star$ rend l'**adversaire** indifférent entre ses deux colonnes.
5. Faux (fiche §2).

### M27.Q3 — Équilibres de Nash, arbres de jeu et descente-montée : unique ou non, le meilleur pour tous ou non, converger ou tourner ?
1. Faux : dans le dilemme du prisonnier, l'équilibre est moins bon pour les deux joueurs qu'une autre issue.
2. Vrai : un jeu de coordination a deux équilibres purs de gains différents, et un mixte.
3. 3 : après G, le second choisit 3 ; après D, il choisit 2 ; le premier joue G, et $\max(3, 2) = 3$.
4. Faux : les valeurs propres $1 \pm i\eta$ ont pour module $\sqrt{1 + \eta^2} > 1$, quel que soit $\eta > 0$.
5. Vrai : déterminant 1 et valeurs propres complexes de module 1 ; les itérés parcourent une ellipse.

### M27.Q4 — La probabilité a posteriori et la log-loss ; Jensen-Shannon et KL quand les supports se séparent
1. $t^\star(x) = \frac{0{,}2 \times 0{,}5}{0{,}2 \times 0{,}5 + 0{,}8 \times 0{,}1} = \frac{0{,}1}{0{,}18} = \frac59 \approx 0{,}556$.
2. Faux : toute prédiction différente de $t^\star(x)$ fait moins bien en moyenne (∂ M27.12), qu'elle soit plus tranchée ou moins.
3. Vrai : c'est la fréquence de la classe 1 (🔁 M27.R1, ∂ M27.12 question 4).
4. $\mathrm{JS} = \ln 2 \approx 0{,}693$ nat, soit 1 bit ; $\mathrm{KL}(p \,\|\, q) = +\infty$.
5. Faux : JS vaut déjà $\ln 2$ et n'en bouge plus.

### M27.Q5 — Couplages et distances de Wasserstein : marges, translation, dilatation, et W₁ ≤ W₂
1. Faux : les lignes ont bien pour sommes 0,5 et 0,5, mais les colonnes 0,3 et 0,7, pas 0,4 et 0,6.
2. 2,5 et 2,5 : une translation de $\theta$ donne $W_p = \lvert\theta\rvert$ pour tout $p$.
3. $Y$ suit $\mathcal{N}(0, 6^2)$, de même moyenne : $W_2 = \lvert 2 - 6\rvert = 4$.
4. Vrai (fiche §7, par Jensen).
5. Faux : $\lvert\mathbb{E}[X] - \mathbb{E}[Y]\rvert$ n'est qu'une minoration de $W_1$ (égalité si une fonction de répartition est partout au-dessus de l'autre).

### M27.Q6 — La distance de Fréchet et son estimation : rotation commune, covariances, taille des échantillons
1. Vrai (fiche §9).
2. Faux : la racine d'une matrice n'est pas la matrice des racines (M12c).
3. Seule la part des moyennes reste : $W_2 = \sqrt{2^2 + 3^2 + 6^2} = 7$.
4. $12 \times \big(\frac{1}{30} + \frac{1}{30}\big) = 0{,}8$.
5. Vrai : $\operatorname{tr}\boldsymbol{\Sigma}\,\big(\frac{1}{60} + \frac{1}{60}\big) = 0{,}4$.

### M27.Q7 — Mesurer une dérive : PSI, KS ou W₁, leurs unités, et ce que chacun ne voit pas
1. KS ne change pas (la conversion est croissante) ; $W_1$ est multiplié par 1,8 (le $+32$ ne change rien, puisqu'il décale les deux lois).
2. Vrai.
3. $\mathrm{KS} = 1$ et $W_1 = 5$.
4. $W_1 \le 30 \times 0{,}15 = 4{,}5$ (dans l'unité de la variable).
5. Faux : le PSI ne compare que les proportions des classes ; la loi peut changer à l'intérieur d'une classe (pour une variable à catégories, une classe par catégorie, un PSI nul voudrait bien dire la même loi).

<a id="rappels"></a>

## 🔁 Rappels

### M27.R1 — Le maximum de vraisemblance d'une loi de Bernoulli (des comptes entiers), et la log-loss quand la probabilité prédite tend vers 0 (M04, M13a)
1. $\ell(p) = 23\ln p + 27\ln(1 - p)$, maximale en $p = \frac{k}{n} = \frac{23}{50} = 0{,}46$ (∂ M04.12).
2. Vrai : la log-loss moyenne de la constante $t$ vaut $-\frac{1}{50}\ell(t)$ ; la minimiser revient à maximiser $\ell$.
3. $-\ln(10^{-5}) = 5\ln 10 \approx 11{,}51$ ; elle tend vers $+\infty$ quand $t$ tend vers 0.
4. Au moins $\frac{11{,}51}{50} \approx 0{,}230$ : une seule prédiction très sûre et fausse pèse sur toute la moyenne.

### M27.R2 — Les valeurs propres complexes d'une matrice réelle 2 × 2, leur module et les puissances (M22)
1. $\det(\mathbf{A} - \lambda\mathbf{I}) = (1 - \lambda)^2 + 3$, nul pour $\lambda = 1 \pm i\sqrt{3}$.
2. Module $\sqrt{1 + 3} = 2$, arguments $\pm\frac{\pi}{3}$ (60°).
3. $\lambda^6 = 2^6e^{\pm 2i\pi} = 64$ pour les deux valeurs propres, distinctes, donc $\mathbf{A}^6 = 64\,\mathbf{I}$. Directement : $\mathbf{A}^2 = \begin{pmatrix} -2 & -6 \\ 2 & -2 \end{pmatrix}$, $\mathbf{A}^3 = -8\,\mathbf{I}$, $\mathbf{A}^6 = 64\,\mathbf{I}$.
4. Faux : $\mathbf{A}$ n'est pas 2 fois une rotation ($\mathbf{A}^\top\mathbf{A} = \begin{pmatrix} 2 & -2 \\ -2 & 10 \end{pmatrix} \ne 4\,\mathbf{I}$) ; par exemple, $\lVert\mathbf{A}(1, 0)\rVert = \lVert(1, 1)\rVert = \sqrt2$. Seules les puissances multiples de 3 sont des multiples de $\mathbf{I}$.

### M27.R3 — La racine carrée d'une matrice symétrique positive, et la trace comme somme des valeurs propres (M12c)
1. $\mathbf{S} = \begin{pmatrix} 26 & 8 \\ 8 & 10 \end{pmatrix}$.
2. Vrai : $\mathbf{R}$ est symétrique, définie positive ($\operatorname{tr}\mathbf{R} = 8 > 0$, $\det\mathbf{R} = 14 > 0$), et $\mathbf{R}^2 = \mathbf{S}$ ; la racine symétrique positive est unique (M12c).
3. $\operatorname{tr}\mathbf{S} = 36$, et la somme des valeurs propres aussi.
4. Les valeurs propres de $\mathbf{S} = \mathbf{R}^2$ sont les carrés de celles de $\mathbf{R}$, positives : $\sum_i\sqrt{\lambda_i(\mathbf{S})} = \sum_i\lambda_i(\mathbf{R}) = \operatorname{tr}\mathbf{R} = 8$.
5. Faux : le carré de cette matrice a pour premier coefficient $26 + 8 = 34 \ne 26$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M27.1 — Deux enseignes se partagent un marché : réduire une matrice 3 × 4 par dominance, trouver ses deux points selles et vérifier qu'ils ont la même valeur, et ce que la réduction ne change pas (maximin, minimax)

**Réponses.** a) `[3, 3]` · b) `[[2, 2], [2, 4]]` · c) `False` · d) `[[3, 3]]`.

**Démarche.** Minimums des lignes : 1 (A1), 3 (A2), 0 (A3) : maximin 3, en A2. Maximums des colonnes : 5, 3, 7, 3 : minimax 3, en B2 (et B4). b) Dans la ligne A2, le minimum 3 est atteint en B2 et en B4, et chacune de ces cases est la plus grande de sa colonne (2, **3**, 1 et 1, **3**, 0) : deux points selles. Les autres minimums de ligne (1 en B4 pour A1 ; 0 en B1 et B4 pour A3) ne sont pas des maximums de colonne. c) B1 $= (5, 4, 0)$ n'est pas dominée au départ : sur la ligne A3, elle coûte 0, moins que B2 (1), et autant que B4 (0) ; B3, qui coûte plus qu'elle sur chaque ligne, ne la domine pas non plus. d) Au départ : A3 $= (0, 1, 4, 0)$ est strictement dominée par A1 $= (5, 2, 6, 1)$ et par A2 $= (4, 3, 7, 3)$ ; B3 $= (6, 7, 4)$ coûte plus que B1, B2 et B4 sur chaque ligne. Une fois A3 rayée, B1 $= (5, 4)$ coûte plus que B2 $= (2, 3)$ et que B4 $= (1, 3)$ : rayée. Il reste $\begin{pmatrix} 2 & 1 \\ 3 & 3 \end{pmatrix}$ (lignes A1, A2 ; colonnes B2, B4), où A1 est dominée par A2. Reste la ligne A2 contre B2 et B4, $(3, 3)$ : deux colonnes égales, aucune n'est strictement dominée.

Dans ta copie : **rayer une ligne** $i$ strictement dominée par une ligne $k$ : $\min_jg_{ij} < \min_jg_{kj} \le$ maximin, donc le maximum des minimums de lignes ne change pas ; et, dans chaque colonne $j$, $g_{ij} < g_{kj}$, donc le maximum de la colonne est atteint ailleurs que sur la ligne $i$, et le minimax ne change pas. **Rayer une colonne** $l$ strictement dominée par une colonne $l'$ : $\max_ig_{il} > \max_ig_{il'} \ge$ minimax, donc le minimax ne change pas ; et, dans chaque ligne $i$, $g_{il} > g_{il'}$, donc le minimum de la ligne est atteint ailleurs, et le maximin ne change pas. Chaque élimination garde les deux nombres, donc toute la chaîne aussi. Les deux points selles valent 3 : la même part de marché, et ∂ M27.11 montre que c'est toujours le cas.

**Erreurs fréquentes.** Lire le minimax sur les minimums des colonnes (0). Lire le maximin sur les maximums des lignes (7). Retourner la définition du point selle : la case (A3, B3), le plus grand de sa ligne et le plus petit de sa colonne. Ne garder que le premier minimum de la ligne A2. Rayer B1 dès le départ, ou oublier de comparer de nouveau les lignes après avoir rayé B1. Rayer B2 ou B4 alors qu'elles sont égales.

**Variante.** Si la case (A2, B4) valait 2, il ne resterait qu'un point selle, (A2, B4), et maximin $=$ minimax $= 2$.

### Ex M27.2 — Tirs au but : la probabilité de tirer à gauche par indifférence, la réponse du gardien et la valeur du jeu

**Réponses.** a) `"5/13"` · b) `"7/13"` · c) `73.46` · d) `76.25` · e) `68.5`.

**Démarche.** Minimums des lignes : 55 et 60, maximin 60 ; maximums des colonnes : 85 et 95, minimax 85 : pas de point selle. $\kappa = 55 - 95 - 85 + 60 = -65$. a) $p^\star = \frac{d - c}{\kappa} = \frac{60 - 85}{-65} = \frac{5}{13} \approx 0{,}385$. b) $q^\star = \frac{d - b}{\kappa} = \frac{60 - 95}{-65} = \frac{7}{13} \approx 0{,}538$. c) $v = \frac{ad - bc}{\kappa} = \frac{3\,300 - 8\,075}{-65} = \frac{955}{13} \approx 73{,}46$ %. d) Contre $q = 0{,}65$ : tirer à gauche marque avec $0{,}65 \times 55 + 0{,}35 \times 95 = 69$ %, à droite avec $0{,}65 \times 85 + 0{,}35 \times 60 = 76{,}25$ % : le meilleur tir pur est à droite, 76,25 %. e) Avec $p = 0{,}55$ : $0{,}55 \times 55 + 0{,}45 \times 85 = 68{,}5$ contre un plongeon à gauche, $0{,}55 \times 95 + 0{,}45 \times 60 = 79{,}25$ contre un plongeon à droite ; le tireur s'assure le plus petit, 68,5 %.

Dans ta copie : contre un plongeon à gauche, $55p + 85(1 - p) = 85 - 30p$ ; à droite, $95p + 60(1 - p) = 60 + 35p$. Leur minimum croît jusqu'en $p = \frac{25}{65} = \frac{5}{13}$, où les deux droites valent $\frac{955}{13}$, puis décroît. d) par l'identité : $E(0 ;\ 0{,}65) = \frac{955}{13} - 65\,\big(0 - \frac{5}{13}\big)\big(0{,}65 - \frac{7}{13}\big) = 73{,}46 + 2{,}79 = 76{,}25$ ; comme $\kappa < 0$ et $q > q^\star$, $E(p ;\ 0{,}65)$ décroît en $p$ : le meilleur $p$ est 0, tirer à droite. Le gardien plonge trop souvent à gauche, et le tireur en profite du côté droit.

**Erreurs fréquentes.** Calculer $p^\star$ avec les lignes (on trouve $q^\star$, $\frac{7}{13}$). Donner la probabilité de tirer à droite ($\frac{8}{13}$). Prendre le milieu du maximin et du minimax (72,5). Calculer le gain espéré avec $p$ et $q$ échangés (75). En d), garder le moins bon tir (69), ou pondérer la première colonne par 0,35 (81). En e), garder le plus grand des deux gains (79,25), ou pondérer la première ligne par 0,45 (71,5).

**Variante.** Si le tir à droite contre un plongeon à droite marquait 70 % au lieu de 60 % : $\kappa = -55$, $p^\star = \frac{3}{11}$, $q^\star = \frac{5}{11}$, $v = \frac{845}{11} \approx 76{,}82$ %.

### Ex M27.3 — Les équilibres de Nash d'un dilemme du prisonnier et d'un jeu de coordination (purs et mixte), puis la valeur d'un jeu d'allumettes par induction arrière

**Réponses.** a) `[2, 2]` · b) `False` · c) `"4/7"` · d) `"3/8"` · e) `[1.875, 1.714]` · f) `[1, 4, 7, 10]` · g) `1`.

**Démarche.** a) Pour la boulangerie des lignes : contre M, B rapporte 10 contre 7 ; contre B, 2 contre 1. B domine strictement M, et de même pour l'autre. L'unique équilibre est (B, B), à 2 chacune. b) Contre M, l'autre gagne 10 en passant à B au lieu de 7 : (M, M) n'est pas un équilibre, bien qu'il donne 7 à chacune. c) L'équipe des lignes choisit $x$ pour que l'équipe des colonnes n'ait plus de préférence : X lui rapporte en moyenne $3x$, Y lui rapporte $4(1 - x)$, d'où $x = \frac47$. d) De même, $5y = 3(1 - y)$, d'où $y = \frac38$. e) Gain moyen des lignes : $5y = \frac{15}{8} = 1{,}875$ (ou $3(1 - y)$, la même chose) ; des colonnes : $3x = \frac{12}{7} \approx 1{,}714$. f) et g) Voir ci-dessous.

Dans ta copie : la coordination a deux équilibres purs, (X, X) aux gains $(5, 3)$ et (Y, Y) aux gains $(3, 4)$ : contre X, chacune préfère X, et contre Y, Y. Dans l'équilibre mixte, les équipes tombent d'accord avec la probabilité $xy + (1 - x)(1 - y) = \frac{12}{56} + \frac{15}{56} = \frac{27}{56} \approx 0{,}48$ ; chacune y gagne moins que dans chacun des deux équilibres purs. Allumettes, du point de vue du joueur qui doit jouer : 1 est perdante (il prend la dernière) ; 2 et 3 sont gagnantes (on laisse 1) ; 4 est perdante (on laisse 3 ou 2, gagnantes pour l'autre) ; 5 et 6 gagnantes (on laisse 4) ; 7 perdante ; et ainsi de suite : les positions perdantes sont les nombres de la forme $3k + 1$. Avec 11 allumettes, on en retire 1 pour laisser 10, puis on complète chaque coup de l'adversaire à 3 (il en prend 1, on en prend 2, et inversement), pour lui laisser 7, 4, puis 1.

**Erreurs fréquentes.** Donner l'issue la meilleure pour les deux, $(7, 7)$, ou dire que (M, M) est un équilibre. Calculer $x$ avec les gains de sa propre équipe ($\frac38$), ou donner la probabilité de Y ($\frac37$) ; de même pour $y$ ($\frac47$, $\frac58$). En e), calculer le gain d'une équipe avec sa propre probabilité ($\frac{20}{7}$ et $\frac98$), ou échanger les deux gains. Pour les allumettes, appliquer la règle habituelle, où celui qui prend la dernière gagne (les multiples de 3, et retirer 2 avec 11), ou permettre de retirer 3 (1, 5, 9).

**Variante.** Si l'équipe des colonnes gagnait 6 avec Y : $3x = 6(1 - x)$, $x = \frac23$. Avec 13 allumettes ($13 = 3 \times 4 + 1$), le premier joueur perd si l'autre joue bien.

### Ex M27.4 — Descente-montée sur f(x, y) = xy : la matrice d'un pas simultané puis alterné, leurs valeurs propres et leurs modules, et deux pas différents pour x et y

**Réponses.** a) `1.1662` · b) `31.0` · c) `5` · d) `34.9` · e) `[1.3784, 1]` · f) `3.73`.

**Démarche.** a) $\mathbf{M}_s = \begin{pmatrix} 1 & -0{,}6 \\ 0{,}6 & 1 \end{pmatrix}$, de valeurs propres $1 \pm 0{,}6\,i$, de module $\sqrt{1{,}36} \approx 1{,}16619$. b) $\arctan 0{,}6 \approx 30{,}96°$. c) $\mathbf{M}_s = \sqrt{1{,}36}\,\mathbf{R}_\theta$ multiplie toute distance à l'équilibre par $\sqrt{1{,}36}$ : après $k$ pas, par $1{,}36^{k/2}$ ; $1{,}36^2 = 1{,}8496 < 2$ et $1{,}36^{2{,}5} \approx 2{,}157 \ge 2$, d'où 5 pas ($\frac{\ln 2}{\ln\sqrt{1{,}36}} \approx 4{,}51$). d) $\mathbf{M}_a = \begin{pmatrix} 1 & -0{,}6 \\ 0{,}6 & 0{,}64 \end{pmatrix}$, de déterminant $0{,}64 + 0{,}36 = 1$ et de trace 1,64 ; ses valeurs propres sont $e^{\pm i\theta}$ avec $2\cos\theta = 1{,}64$, donc $\theta = \arccos 0{,}82 \approx 34{,}92°$. e) Avec deux pas : en simultané, $\begin{pmatrix} 1 & -a \\ b & 1 \end{pmatrix}$, de valeurs propres $1 \pm i\sqrt{ab}$ et de module $\sqrt{1 + ab} = \sqrt{1{,}9} \approx 1{,}3784$ ; en alterné, $y_{k+1} = y_k + b(x_k - ay_k)$, donc $\begin{pmatrix} 1 & -a \\ b & 1 - ab \end{pmatrix}$, de déterminant 1 et de trace $2 - ab = 1{,}1$ : $1{,}1^2 - 4 < 0$, deux valeurs propres complexes conjuguées de produit 1, de module 1. f) $ab = 6$ : trace $-4$, $\lambda^2 + 4\lambda + 1 = 0$, $\lambda = -2 \pm \sqrt3$, soit $-0{,}268$ et $-3{,}732$ : rayon spectral $\approx 3{,}73$ ; les itérés s'éloignent en changeant de signe à chaque pas.

Dans ta copie : déterminants $1 + ab$ et $1 - ab + ab = 1$, trace $2 - ab$. En simultané, le module $\sqrt{1 + ab}$ dépasse 1 pour tous $a, b > 0$ : des pas différents ne font jamais converger ; seul le produit $ab$ compte (avec $a = 1{,}2$ et $b = 0{,}3$, on retrouve exactement les valeurs propres de $\eta = 0{,}6$). En alterné, le discriminant vaut $(2 - ab)^2 - 4 = ab\,(ab - 4)$ : pour $ab < 4$, deux valeurs propres complexes distinctes de module 1, et les itérés restent bornés ; pour $ab > 4$, deux valeurs propres réelles de produit 1, dont une de valeur absolue $> 1$, et les itérés s'éloignent, sauf pour un départ sur la droite propre de l'autre valeur propre, de valeur absolue $< 1$, où ils tendent vers 0.

**Erreurs fréquentes.** Donner $1 + \eta^2 = 1{,}36$, ou $1 + \eta = 1{,}6$, pour le module. Donner l'angle en radians (0,540), ou prendre $\eta$ radians pour l'angle (34,4°). En c), utiliser le facteur 1,36 (3 pas), ou arrondir 4,51 vers le bas. En d), reprendre l'angle du pas simultané, ou donner $\arccos 0{,}82$ en radians (0,609). En e), oublier l'un des deux pas ($\sqrt{1 + a^2} \approx 1{,}80$), ou croire que le pas alterné grandit comme le simultané. En f), donner 1, la racine du déterminant, ou prendre la trace $2 - a - b$ (3,19).

**Variante.** Avec $\eta = 0{,}9$ : module $\sqrt{1{,}81} \approx 1{,}3454$ et angle $42{,}0°$ en simultané ; angle $\arccos 0{,}595 \approx 53{,}5°$ en alterné.

### Ex M27.5 — Deux fournisseurs et un défaut noté sur quatre niveaux : la probabilité a posteriori, et la log-loss moyenne de trois prédicteurs (a priori, a posteriori, trop sûr de lui)

**Réponses.** a) `0.322` · b) `[0.050, 0.239, 0.414, 0.809]` · c) `0.6269` · d) `0.4551` · e) `0.5670`.

**Démarche.** Probabilités jointes : $P(X = x, Y = 1) = 0{,}32 \times (0{,}05 ;\ 0{,}20 ;\ 0{,}30 ;\ 0{,}45) = (0{,}016 ;\ 0{,}064 ;\ 0{,}096 ;\ 0{,}144)$ et $P(X = x, Y = 0) = 0{,}68 \times (0{,}45 ;\ 0{,}30 ;\ 0{,}20 ;\ 0{,}05) = (0{,}306 ;\ 0{,}204 ;\ 0{,}136 ;\ 0{,}034)$. a) $P(X = 0) = 0{,}016 + 0{,}306 = 0{,}322$ ; de même $P(X) = (0{,}322 ;\ 0{,}268 ;\ 0{,}232 ;\ 0{,}178)$. b) $t^\star(x) = \frac{P(X = x, Y = 1)}{P(X = x)}$ : $\frac{0{,}016}{0{,}322} \approx 0{,}0497$, $\frac{0{,}064}{0{,}268} \approx 0{,}2388$, $\frac{0{,}096}{0{,}232} \approx 0{,}4138$, $\frac{0{,}144}{0{,}178} \approx 0{,}8090$. c) $R = -\big[0{,}32\ln 0{,}32 + 0{,}68\ln 0{,}68\big] \approx 0{,}36462 + 0{,}26225 = 0{,}62687$. d) $R(t^\star) = -\sum_x\big[P(x, 1)\ln t^\star(x) + P(x, 0)\ln(1 - t^\star(x))\big]$, niveau par niveau $0{,}0636 + 0{,}1473 + 0{,}1573 + 0{,}0868 \approx 0{,}4551$. e) Même somme avec $(0{,}02 ;\ 0{,}08 ;\ 0{,}15 ;\ 0{,}96)$ : $0{,}0688 + 0{,}1787 + 0{,}2042 + 0{,}1153 \approx 0{,}5670$.

Dans ta copie : à chaque niveau, le prédicteur trop sûr de lui est plus loin de ½ que $t^\star$, et du même côté (0,02 contre 0,050 ; 0,08 contre 0,239 ; 0,15 contre 0,414 ; 0,96 contre 0,809). Classement : $R(t^\star) = 0{,}4551 < 0{,}5670 < 0{,}6269$. La probabilité a posteriori est la meilleure (∂ M27.12) ; le prédicteur trop sûr de lui perd contre elle à **chaque** niveau, mais il se sert encore du niveau observé, et reste ici meilleur que le prédicteur a priori, qui l'ignore. Plus tranché ne veut pas dire meilleur.

**Erreurs fréquentes.** Moyenner les deux fournisseurs à parts égales (0,25), ou oublier les pièces de B (0,306). Prendre $p_1(x)$, la probabilité du niveau sachant B, pour $t^\star(x)$, ou donner la probabilité de A, $1 - t^\star(x)$. Échanger les poids de $-\ln t$ et de $-\ln(1 - t)$ (0,8982). Calculer en bits (0,9044, 0,6566, 0,8180). Moyenner les quatre niveaux à parts égales (0,4783).

**Variante.** Si B livrait 36 % des pièces, $t^\star(3) = \frac{0{,}36 \times 0{,}45}{0{,}36 \times 0{,}45 + 0{,}64 \times 0{,}05} = \frac{0{,}162}{0{,}194} \approx 0{,}835$.

### Ex M27.6 — Deux lois uniformes de même largeur, translatées : JS en fonction du décalage, la KL, et ce que le décalage lui-même mesure

**Réponses.** a) `0.139` · b) `0.416` · c) `[0.693, 0.693]` · d) `False` · e) `[8, 80]`.

**Démarche.** Pour $0 < \theta < 5$, trois morceaux : sur $[0 ; \theta[$, seule $p$ est positive ($\frac15$), et $m = \frac{1}{10}$ ; sur $[\theta ; 5]$, les deux valent $\frac15$, et $m = \frac15$ ; sur $]5 ; \theta + 5]$, seule $q$ est positive, et $m = \frac{1}{10}$. Donc $\mathrm{KL}(p \,\|\, m) = \int_0^\theta\frac15\ln\frac{1/5}{1/10}\,\mathrm{d}x + \int_\theta^5\frac15\ln 1\,\mathrm{d}x = \frac{\theta}{5}\ln 2$, de même $\mathrm{KL}(q \,\|\, m) = \frac{\theta}{5}\ln 2$, et $\mathrm{JS}(\theta) = \frac{\theta}{5}\ln 2$. a) $\frac{\ln 2}{5} \approx 0{,}1386$. b) $\frac{3\ln 2}{5} \approx 0{,}4159$. c) Pour $\theta \ge 5$, les supports ne se recouvrent plus (en $\theta = 5$, ils se touchent en un seul point, qui ne compte pas dans les intégrales) : $m = \frac{1}{10}$ là où l'une vaut $\frac15$, chaque KL vaut $\ln 2$, et $\mathrm{JS} = \ln 2 \approx 0{,}693$, pour $\theta = 8$ comme pour $\theta = 80$. d) Faux : $p$ est positive sur $[0 ; 1[$, où $q$ est nulle, donc $\mathrm{KL}(p \,\|\, q) = +\infty$. e) Une translation : $W_1 = \theta$, soit 8 et 80 minutes.

Dans ta copie : JS croît en ligne droite, de pente $\frac{\ln 2}{5}$, jusqu'en $\theta = 5$, puis reste plate : au-delà, elle ne dit plus de combien l'horaire a bougé, et la KL est infinie dès le premier décalage. $W_1 = \theta$ garde une pente de 1 : le décalage lui-même, le chemin moyen que fait la masse.

**Erreurs fréquentes.** Calculer en bits (0,2, 0,6, puis 1 et 1). Oublier les facteurs ½ (0,277, 0,832). Prolonger la formule au-delà de $\theta = 5$ (1,109 et 11,09). Croire la KL finie parce que les supports se recouvrent en partie. Rapporter $W_1$ à la largeur (1,6 et 16).

**Variante.** Pour une fenêtre de 2 minutes et $\theta = 1$, $\mathrm{JS} = \frac12\ln 2 \approx 0{,}347$.

### Ex M27.7 — Trois dépôts et trois magasins le long d'une route : vérifier des couplages, leur coût, le couplage indépendant et le plan monotone (coin nord-ouest)

**Réponses.** a) `False` · b) `175` · c) `259` · d) `[[20, 0, 0], [20, 30, 0], [0, 5, 25]]` · e) `1.55`.

**Démarche.** Distances : $\begin{pmatrix} 1 & 2 & 7 \\ 2 & 1 & 4 \\ 4 & 3 & 2 \end{pmatrix}$. a) Les lignes de $\boldsymbol{\Gamma}_3$ ont pour sommes 20, 50 et 30, mais ses colonnes 40, 30 et 30 : le magasin 2 reçoit 30 t au lieu de 35, le magasin 3 en reçoit 30 au lieu de 25. b) $10 \times 1 + 10 \times 2 + 30 \times 2 + 20 \times 1 + 5 \times 3 + 25 \times 2 = 175$. c) Le dépôt $i$ envoie au magasin $j$ la part $\frac{b_j}{100}$ de son stock : $\gamma_{ij} = \frac{a_ib_j}{100}$, $\begin{pmatrix} 8 & 7 & 5 \\ 20 & 17{,}5 & 12{,}5 \\ 12 & 10{,}5 & 7{,}5 \end{pmatrix}$, de coût $8 + 14 + 35 + 40 + 17{,}5 + 50 + 48 + 31{,}5 + 15 = 259$. d) Case (1, 1) : $\min(20, 40) = 20$, le dépôt 1 est vide, on descend ; (2, 1) : $\min(50, 20) = 20$, le magasin 1 est plein, on va à droite ; (2, 2) : $\min(30, 35) = 30$, le dépôt 2 est vide, on descend ; (3, 2) : 5 ; (3, 3) : 25. Coût : $20 + 40 + 30 + 15 + 50 = 155$. e) Ramenées à une masse totale de 1, les masses sont divisées par 100 : $W_1 = 1{,}55$ km.

Dans ta copie : $F$ (les stocks) vaut 0,2 sur $[1 ; 4[$, 0,7 sur $[4 ; 6[$, 1 ensuite ; $G$ (les commandes) vaut 0,4 sur $[2 ; 3[$, 0,75 sur $[3 ; 8[$, 1 ensuite. L'aire entre elles : $0{,}2 \times 1 + 0{,}2 \times 1 + 0{,}55 \times 1 + 0{,}05 \times 2 + 0{,}25 \times 2 = 1{,}55$. $\boldsymbol{\Gamma}_2$ coûte plus parce que deux de ses trajets se croisent (10 t du km 1 au km 3, 30 t du km 4 au km 2) : les décroiser fait gagner (∂ M27.14).

**Erreurs fréquentes.** Ne vérifier que les sommes des lignes. Lire les distances dans la matrice transposée (180). Oublier de diviser le couplage indépendant par la masse totale. Remplir le coin nord-ouest avec les magasins en lignes. Donner $W_1$ en t·km (155), ou celui du couplage indépendant (2,59).

**Variante.** Si le troisième dépôt était au km 9, le plan du coin nord-ouest ne changerait pas ; il coûterait 145 t·km, et $W_1 = 1{,}45$ km.

### Ex M27.8 — W₁ et W₂ par l'aire entre les fonctions de répartition et par les quantiles : deux lois uniformes, puis W₂ de deux gaussiennes (et W₁ quand elles ont le même écart-type)

**Réponses.** a) `"5/6"` · b) `1` · c) `1.3` · d) `1.2`.

**Démarche.** a) $F(x) = \frac{x}{4}$ sur $[0 ; 4]$ ; $G$ vaut 0 avant 1, $x - 1$ sur $[1 ; 2]$, 1 après. Sur $[0 ; 1]$, $\int\frac{x}{4} = \frac18$ ; sur $[1 ; 2]$, $\lvert F - G\rvert = \lvert 1 - \frac{3x}{4}\rvert$, nul en $\frac43$ : $\int_1^{4/3}\big(1 - \frac{3x}{4}\big) = \frac{1}{24}$ et $\int_{4/3}^{2}\big(\frac{3x}{4} - 1\big) = \frac16$ ; sur $[2 ; 4]$, $\int\big(1 - \frac{x}{4}\big) = \frac12$. Total : $\frac{3 + 1 + 4 + 12}{24} = \frac56$. b) $F^{-1}(u) = 4u$ et $G^{-1}(u) = 1 + u$ : $W_2^2 = \int_0^1(3u - 1)^2\,\mathrm{d}u = 3 - 3 + 1 = 1$, donc $W_2 = 1$. c) $W_2 = \sqrt{1{,}2^2 + 0{,}5^2} = \sqrt{1{,}69} = 1{,}3$ g. d) Même écart-type : la seconde loi est la première translatée de 1,2 g, et $W_1 = W_2 = 1{,}2$ g.

Dans ta copie : $\int_0^1\lvert 3u - 1\rvert\,\mathrm{d}u = \frac16 + \frac23 = \frac56$ redonne a). $W_1 = 0{,}833 \le W_2 = 1$. Les moyennes valent 2 et 1,5 : l'écart 0,5 n'est qu'une minoration de $W_1$, parce que les deux fonctions de répartition se croisent (la première machine coupe parfois moins, parfois plus que la seconde). En d), le couplage des quantiles déplace chaque quantile de 1,2 g : tous les trajets ont la même longueur, et $W_p = 1{,}2$ pour tout $p$.

**Erreurs fréquentes.** Prendre l'écart des moyennes, ou l'aire sans valeur absolue (½). Calculer $W_2$ par $\sqrt{\int(F - G)^2}$ (0,5). Mettre des variances dans la formule (1,733). Donner $W_2^2$ (1,69), ou $\lvert\Delta\mu\rvert + \lvert\Delta\sigma\rvert$ (1,7). En d), faire entrer l'écart-type commun dans la distance (1,92).

**Variante.** Entre $\mathcal{N}(20 ;\ 1{,}5^2)$ et $\mathcal{N}(20 ;\ 1^2)$, seule la dispersion change : $W_2 = 0{,}5$ g.

### Ex M27.9 — La distance de Fréchet de deux gaussiennes du plan à covariances diagonales, puis tournées ensemble : la part des moyennes et celle des covariances

**Réponses.** a) `[[100, 25], [225, 100]]` · b) `200` · c) `50` · d) `29` · e) `8.89`.

**Démarche.** a) $\boldsymbol{\Sigma}_1$ : trace 125, déterminant $52 \times 73 - 36^2 = 2\,500$, donc $\lambda^2 - 125\lambda + 2\,500 = 0$ : 100 et 25. $\boldsymbol{\Sigma}_2$ : trace 325, déterminant $145 \times 180 - 60^2 = 22\,500$, donc $\lambda^2 - 325\lambda + 22\,500 = 0$ : 225 et 100. Vecteurs propres : $\boldsymbol{\Sigma}_1 - 100\,\mathbf{I} = \begin{pmatrix} -48 & 36 \\ 36 & -27 \end{pmatrix}$ annule $(3, 4)$, et $\boldsymbol{\Sigma}_2 - 225\,\mathbf{I} = \begin{pmatrix} -80 & 60 \\ 60 & -45 \end{pmatrix}$ aussi ; l'autre vecteur propre, orthogonal, est $(4, -3)$ pour les deux. Le long de $\mathbf{u}_1 = \frac{(3, 4)}{5}$, les écarts-types valent 10 et 15 ; le long de $\mathbf{u}_2 = \frac{(4, -3)}{5}$, 5 et 10. b) $\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2$ a pour valeurs propres $100 \times 225 = 22\,500$ (sur $\mathbf{u}_1$) et $25 \times 100 = 2\,500$ (sur $\mathbf{u}_2$) : $\sqrt{22\,500} + \sqrt{2\,500} = 150 + 50 = 200$. c) $125 + 325 - 400 = 50$. d) $5^2 + 2^2 = 29$. e) $W_2 = \sqrt{79} \approx 8{,}89$ centièmes de mm.

Dans ta copie : $\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2 = \begin{pmatrix} 9\,700 & 9\,600 \\ 9\,600 & 15\,300 \end{pmatrix}$, symétrique, donc égale à $(\boldsymbol{\Sigma}_1\boldsymbol{\Sigma}_2)^\top = \boldsymbol{\Sigma}_2\boldsymbol{\Sigma}_1$. Cas commutatif : $(10 - 15)^2 + (5 - 10)^2 = 50$, comme c). Avec la rotation de lignes $\mathbf{u}_1^\top$ et $\mathbf{u}_2'^\top$, où $\mathbf{u}_2' = \frac{(-4, 3)}{5}$ (de déterminant 1 ; avec $\mathbf{u}_2$, on aurait une symétrie, qui convient aussi), les covariances deviennent $\operatorname{diag}(100, 25)$ et $\operatorname{diag}(225, 100)$, et le décalage des moyennes $(\mathbf{u}_1 \cdot \Delta\boldsymbol{\mu},\ \mathbf{u}_2' \cdot \Delta\boldsymbol{\mu}) = (1{,}4 ;\ -5{,}2)$, de carré de norme $1{,}96 + 27{,}04 = 29$ : $W_2$ ne change pas. Ce sont deux gaussiennes à covariances diagonales, tournées ensemble.

**Erreurs fréquentes.** Prendre les coefficients diagonaux pour les valeurs propres, ou donner les écarts-types. Associer les valeurs propres de travers ($\sqrt{100 \times 100} + \sqrt{25 \times 225} = 175$). Prendre la racine de la somme des valeurs propres (158,1). Oublier le terme croisé (450). Soustraire les variances au lieu des écarts-types. Prendre $\lvert 5\rvert + \lvert -2\rvert$ ou $\lVert\Delta\boldsymbol{\mu}\rVert$ pour la part des moyennes. Donner $W_2^2 = 79$.

**Variante.** Avec des moyennes égales, $W_2 = \sqrt{50} \approx 7{,}07$.

### Ex M27.10 — Une dérive en deux mois d'une variable à trois catégories : la divergence de Jeffreys (le PSI) et JS, puis l'approximation Σ(p_k − q_k)²/q_k d'un petit décalage ; enfin KS et W₁ entre deux petits échantillons de températures de même taille

**Réponses.** a) `0.0232` · b) `0.00289` · c) `0.0247` · d) `0.6` · e) `1.46`.

**Démarche.** a) $\mathrm{PSI} = -0{,}07\ln\frac{0{,}55}{0{,}62} + 0{,}03\ln\frac{0{,}29}{0{,}26} + 0{,}04\ln\frac{0{,}16}{0{,}12} \approx 0{,}02317$. b) $m = (0{,}585 ;\ 0{,}275 ;\ 0{,}14)$, $\mathrm{KL}(p \,\|\, m) \approx 0{,}002835$ et $\mathrm{KL}(q \,\|\, m) \approx 0{,}002945$, d'où $\mathrm{JS} \approx 0{,}00289$. c) $\frac{0{,}0049}{0{,}62} + \frac{0{,}0009}{0{,}26} + \frac{0{,}0016}{0{,}12} \approx 0{,}0247$. d) Triées : janvier $-1{,}5$ ; $-0{,}2$ ; 0,7 ; 3,2 ; 3,6 et février 1,2 ; 1,9 ; 2,3 ; 2,8 ; 4,1. Sur $[0{,}7 ; 1{,}2[$, la fonction de répartition de janvier vaut 0,6, celle de février 0 : $\mathrm{KS} = 0{,}6$. e) Appariement trié : $\frac{2{,}7 + 2{,}1 + 1{,}6 + 0{,}4 + 0{,}5}{5} = 1{,}46$ °C.

Dans ta copie : le mode de livraison n'a pas d'ordre ni d'unité, donc ni fonction de répartition ni distance de transport. L'écart $F_{\text{janv}} - F_{\text{fév}}$ vaut successivement 0,2 ; 0,4 ; 0,6 ; 0,4 ; 0,2 ; 0 ; $-0{,}2$ (sur $[2{,}8 ; 3{,}2[$) ; 0 ; 0,2 ; 0 : son plus grand écart, 0,6, est sur $[0{,}7 ; 1{,}2[$. Borne : $[a ; b] = [-1{,}5 ; 4{,}1]$, et $5{,}6 \times 0{,}6 = 3{,}36 \ge 1{,}46$. Les moyennes valent 1,16 et 2,46 °C : l'écart 1,30 est sous $W_1$, parce que les deux courbes se croisent (sur $[2{,}8 ; 3{,}2[$, février est en avance) : une partie de la masse descend pendant que le reste monte. Le PSI et son approximation sont proches (un petit décalage), et JS est à peu près huit fois plus petite qu'eux.

**Erreurs fréquentes.** Calculer seulement $\mathrm{KL}(p \,\|\, q)$ (0,0118) ; un logarithme décimal (0,0101). JS en bits (0,00417), ou sans les facteurs ½ (0,00578). Diviser par $p_k$ (0,0220), ou oublier le carré. Prendre le plus grand écart entre valeurs triées (2,7) pour KS. Apparier dans l'ordre des relevés (2,78), ou donner l'écart des moyennes (1,30).

**Variante.** Si avril avait donné $p = (0{,}60 ;\ 0{,}27 ;\ 0{,}13)$ : $\mathrm{PSI} \approx 0{,}0018$, et l'approximation $\approx 0{,}0019$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M27.11 — Le maximin est au plus le minimax ; ils sont égaux si et seulement si le jeu a un point selle, et deux points selles ont la même valeur

**Démonstration.**
1. Comme le maximin est atteint en $i_0$, maximin $= \min_jg_{i_0j} \le g_{i_0j_0}$ ; comme le minimax est atteint en $j_0$, $g_{i_0j_0} \le \max_ig_{ij_0} =$ minimax.
2. $(i, j)$ est un point selle : $g_{ij} = \min_lg_{il} \le \max_k\min_lg_{kl} =$ maximin, et $g_{ij} = \max_kg_{kj} \ge \min_l\max_kg_{kl} =$ minimax. Avec 1 : minimax $\le g_{ij} \le$ maximin $\le$ minimax ; tout est égal.
3. Si maximin $=$ minimax $= v$, les deux inégalités de 1 sont des égalités : $g_{i_0j_0} = v = \min_jg_{i_0j}$, le plus petit de sa ligne, et $g_{i_0j_0} = v = \max_ig_{ij_0}$, le plus grand de sa colonne : un point selle.
4. Par 2, $g_{ij}$ et $g_{kl}$ valent tous deux le maximin, notons-le $v$. Comme $(i, j)$ est un point selle, $g_{il} \ge \min_{l'}g_{il'} = g_{ij} = v$ ; comme $(k, l)$ en est un, $g_{il} \le \max_{k'}g_{k'l} = g_{kl} = v$. Donc $g_{il} = v$, qui est le minimum de la ligne $i$ (il vaut $g_{ij}$) et le maximum de la colonne $l$ (il vaut $g_{kl}$) : $(i, l)$ est un point selle. De même pour $(k, j)$.

**Grille de relecture.** 1 : l'usage de $i_0$ et $j_0$ (ou l'argument direct : pour tous $i, j$, $\min_lg_{il} \le g_{ij} \le \max_kg_{kj}$, puis le maximum en $i$ et le minimum en $j$). 2 : les deux inégalités tirées de la définition du point selle, puis la chaîne avec 1. 3 : les égalités forcées dans 1, et l'identification du minimum de ligne et du maximum de colonne. 4 : l'égalité des valeurs (par 2, ou par la chaîne $g_{ij} \le g_{il} \le g_{kl} \le g_{kj} \le g_{ij}$), puis l'échange des lignes et des colonnes. Toute démonstration correcte est acceptée ; aucune stratégie mixte n'est demandée.

**Variante.** Les deux points selles de M27.1, (A2, B2) et (A2, B4), sont sur la même ligne : la question 4 n'en donne pas de nouveau.

### Ex M27.12 — La log-loss espérée est minimale pour la probabilité a posteriori : une preuve par l'inégalité de Gibbs

**Démonstration.**
1. Par Bayes et les probabilités totales, $P(Y = 1 \mid X = x) = \frac{P(Y = 1)\,P(X = x \mid Y = 1)}{P(X = x)} = \frac{\pi_1p_1(x)}{\pi_1p_1(x) + \pi_0p_0(x)} = t^\star(x)$, dans $]0, 1[$ puisque $p_0(x), p_1(x) > 0$. Ensuite $R(t) = \sum_x\sum_yP(X = x, Y = y)\,\ell(t(x), y) = \sum_xP(X = x)\big[P(Y = 1 \mid X = x)\big(-\ln t(x)\big) + P(Y = 0 \mid X = x)\big(-\ln(1 - t(x))\big)\big]$, ce qui est la formule annoncée.
2. Par différence, à $x$ fixé, $-t^\star\ln t - (1 - t^\star)\ln(1 - t) + t^\star\ln t^\star + (1 - t^\star)\ln(1 - t^\star) = t^\star\ln\frac{t^\star}{t} + (1 - t^\star)\ln\frac{1 - t^\star}{1 - t} = \mathrm{KL}\big(t^\star(x) \,\|\, t(x)\big)$ ; on somme avec les poids $P(X = x)$.
3. Par l'inégalité de Gibbs, chaque $\mathrm{KL}\big(t^\star(x) \,\|\, t(x)\big)$ est positive ou nulle, et nulle si et seulement si les deux lois de Bernoulli coïncident, c'est-à-dire $t(x) = t^\star(x)$. Les poids $P(X = x)$ sont strictement positifs : $R(t) - R(t^\star) \ge 0$, avec égalité si et seulement si $t(x) = t^\star(x)$ pour chaque $x$.
4. Une constante $t$ ne dépend pas de $X$ : $R(t) = -\pi_1\ln t - \pi_0\ln(1 - t)$, et le calcul de 2 donne $R(t) - R(\pi_1) = \mathrm{KL}(\pi_1 \,\|\, t) \ge 0$, nulle seulement en $t = \pi_1$. Sur des données, c'est la fréquence (🔁 M27.R1).

**Grille de relecture.** Bayes, avec les probabilités totales au dénominateur ; le conditionnement par $X$ écrit (une somme sur $x$ de $P(X = x)$ fois une moyenne sachant $X = x$) ; l'écart écrit comme une somme pondérée de KL entre lois de Bernoulli ; Gibbs avec son cas d'égalité, et l'usage de $P(X = x) > 0$ pour le « seulement si ». Les questions 2 et 3 demandent l'inégalité de Gibbs : une preuve par dérivées, valeur par valeur, répond à une autre question. 4 : la constante $\pi_1$, par le calcul de 2 ($R(t) - R(\pi_1) = \mathrm{KL}(\pi_1 \,\|\, t)$), par 3 avec une observation qui ne dit rien, ou par la dérivée de $-\pi_1\ln t - \pi_0\ln(1 - t)$ : toute méthode correcte est acceptée ici. On ne demande pas la valeur du minimum.

**Variante.** Avec les nombres de ✏️ M27.5 : $R(\text{trop sûr}) - R(t^\star) = \sum_xP(X = x)\,\mathrm{KL}\big(t^\star(x) \,\|\, t(x)\big) = 0{,}5670 - 0{,}4551 = 0{,}1119$.

### Ex M27.13 — 0 ≤ JS ≤ ln 2, et JS = ln 2 si et seulement si les deux lois ont des supports disjoints

**Démonstration.**
1. Si $p_k > 0$, alors $m_k = \frac{p_k + q_k}{2} \ge \frac{p_k}{2} > 0$, et le terme $p_k\ln\frac{p_k}{m_k}$ est fini ; si $p_k = 0$, le terme est nul. $\mathrm{KL}(p \,\|\, m)$ est une somme finie de termes finis, de même $\mathrm{KL}(q \,\|\, m)$. En revanche, pour $p = (1, 0)$ et $q = (0, 1)$, $\mathrm{KL}(p \,\|\, q)$ contient $1 \times \ln\frac10 = +\infty$.
2. Par Gibbs, $\mathrm{KL}(p \,\|\, m) \ge 0$, nulle si et seulement si $p = m$, et de même pour $q$. Donc $\mathrm{JS} \ge 0$, et $\mathrm{JS} = 0$ si et seulement si $p = m$ et $q = m$ ; or $p = \frac{p + q}{2}$ équivaut à $p = q$.
3. Pour $p_k > 0$, $m_k \ge \frac{p_k}{2}$ donne $\frac{p_k}{m_k} \le 2$, donc $\ln\frac{p_k}{m_k} \le \ln 2$. En moyenne avec les poids $p_k$, de somme 1 : $\mathrm{KL}(p \,\|\, m) \le \ln 2$. Comme les poids sont strictement positifs sur le support de $p$, l'égalité a lieu si et seulement si $m_k = \frac{p_k}{2}$ pour tout $k$ tel que $p_k > 0$, c'est-à-dire $q_k = 0$.
4. Donc $\mathrm{JS} \le \frac12\ln 2 + \frac12\ln 2 = \ln 2$, avec égalité si et seulement si les deux KL valent $\ln 2$ : $q_k = 0$ là où $p_k > 0$, et $p_k = 0$ là où $q_k > 0$. Aucun $k$ n'a $p_k > 0$ et $q_k > 0$ : les supports sont disjoints. Réciproquement, si les supports sont disjoints, les deux cas d'égalité de 3 ont lieu, et $\mathrm{JS} = \ln 2$.

**Grille de relecture.** La finitude par $m_k \ge \frac{p_k}{2}$, et un exemple de KL infinie. La positivité par Gibbs, avec son cas d'égalité, et l'équivalence $p = m \Leftrightarrow p = q$. La majoration terme à terme, la croissance de $\ln$, et le cas d'égalité, qui demande des poids strictement positifs. Les deux sens de l'équivalence finale. Une preuve par l'écriture $\mathrm{JS} = H(m) - \frac{H(p) + H(q)}{2}$ (M06) est aussi acceptée, si le cas d'égalité est traité.

**Variante.** En bits, la borne vaut 1 bit.

### Ex M27.14 — L'appariement trié est optimal : un argument d'échange sur deux paires, puis sur n paires, pour les coûts |x − y| et (x − y)²

**Démonstration.**
1. $(x_1 - y_2)^2 + (x_2 - y_1)^2 - (x_1 - y_1)^2 - (x_2 - y_2)^2 = 2x_1y_1 + 2x_2y_2 - 2x_1y_2 - 2x_2y_1 = 2(x_2 - x_1)(y_2 - y_1) \ge 0$.
2. Soit $\varphi$ convexe (ici $\varphi(d) = \lvert d\rvert$, ou $d^2$). Posons $u = x_1 - y_2$ et $w = x_2 - y_1$ : les deux différences de l'appariement trié, $s = x_1 - y_1$ et $s' = x_2 - y_2$, sont entre $u$ et $w$ (puisque $y_1 \le y_2$ et $x_1 \le x_2$), et $s + s' = u + w$. Si $u = w$, tout est égal. Sinon, $s = \lambda u + (1 - \lambda)w$ avec $\lambda \in [0, 1]$, et alors $s' = (1 - \lambda)u + \lambda w$ ; par convexité, $\varphi(s) + \varphi(s') \le \lambda\varphi(u) + (1 - \lambda)\varphi(w) + (1 - \lambda)\varphi(u) + \lambda\varphi(w) = \varphi(u) + \varphi(w)$.
3. Soit $i < j$ un croisement : $x_i < x_j$ et $y_{\sigma(j)} < y_{\sigma(i)}$. Par 1 et 2, appliqués à ces quatre nombres, apparier $x_i$ avec $y_{\sigma(j)}$ et $x_j$ avec $y_{\sigma(i)}$ ne coûte pas plus ; les autres termes ne bougent pas. Le nombre de croisements baisse : les paires qui ne contiennent ni $i$ ni $j$ ne changent pas ; la paire $(i, j)$ cesse d'être un croisement ; pour $l < i$ ou $l > j$, les deux paires qui contiennent $l$ et l'une des positions $i$, $j$ échangent leurs statuts, et leur total ne change pas ; pour $i < l < j$, les paires $(i, l)$ et $(l, j)$ comptaient deux croisements et n'en comptent plus aucun si $\sigma(j) < \sigma(l) < \sigma(i)$, et en comptent un, avant comme après, sinon. Le nombre de croisements baisse donc d'au moins 1. Une permutation sans croisement est croissante, donc c'est l'identité ; le nombre de croisements, un entier positif ou nul, ne peut baisser qu'un nombre fini de fois (au plus $\frac{n(n - 1)}{2}$) : en échangeant tant qu'il reste un croisement, on arrive à l'identité sans jamais augmenter le coût, et l'appariement trié coûte au plus autant que $\sigma$, pour les deux coûts. (On peut aussi n'échanger que des croisements voisins, $j = i + 1$ : il en existe un dès que $\sigma$ n'est pas l'identité, sinon $\sigma(1) < \cdots < \sigma(n)$, et l'échange retire exactement ce croisement. Cela suffit pour conclure, mais ne répond pas à la question pour un croisement quelconque.)
4. Avec $x = (2, 3)$ et $y = (7, 10)$ : trié, $5 + 7 = 12$ ; croisé, $8 + 4 = 12$ ; tout appariement de deux points de gauche avec deux points de droite coûte la même chose pour $\lvert x - y\rvert$. En carrés, $25 + 49 = 74$ contre $64 + 16 = 80$ : par 1, l'écart vaut $2(x_2 - x_1)(y_2 - y_1) = 6 > 0$ dès que les deux inégalités sont strictes.

**Grille de relecture.** 1 : le développement et le signe du produit. 2 : une preuve correcte pour la valeur absolue, par convexité comme ci-dessus, par cas selon la position des quatre points, ou en écrivant $\lvert a - b\rvert$ comme la longueur des $t$ compris entre $a$ et $b$ et en comptant, pour chaque $t$, les segments qui le contiennent. 3 : un croisement quelconque traité, ou bien un croisement voisin dont l'existence et l'effet (il retire exactement ce croisement) sont justifiés ; le coût qui ne monte pas ; la baisse d'au moins 1 du nombre de croisements ; la fin du procédé. Le croisement voisin justifié vaut la moitié des points de la question 3, pas la totalité, puisque la question porte sur un croisement quelconque. 4 : un exemple juste et l'inégalité stricte. Les égalités entre valeurs se traitent de même, avec $\le$.

**Variante.** La permutation $(2, 3, 1)$ a deux croisements ; deux échanges voisins la ramènent à l'identité.

### Ex M27.15 — E‖x̄₁ − x̄₂‖² = ‖μ₁ − μ₂‖² + tr Σ₁/n₁ + tr Σ₂/n₂ : une distance estimée sur deux échantillons est biaisée vers le haut

**Démonstration.**
1. $\mathbb{E}\lVert\mathbf{v}\rVert^2 = \sum_k\mathbb{E}[v_k^2] = \sum_k\big(\mathbb{V}(v_k) + m_k^2\big) = \operatorname{tr}\mathbf{C} + \lVert\mathbf{m}\rVert^2$, puisque les variances des coordonnées sont les coefficients diagonaux de $\mathbf{C}$.
2. Par linéarité, $\mathbb{E}[\bar{\mathbf{x}}_1] = \boldsymbol{\mu}_1$. Les $\mathbf{x}_i$ sont indépendants, donc leurs covariances croisées sont nulles : $\operatorname{Cov}(\bar{\mathbf{x}}_1) = \frac{1}{n_1^2}\sum_i\operatorname{Cov}(\mathbf{x}_i) = \frac{\boldsymbol{\Sigma}_1}{n_1}$ (M02c) ; de même pour $\bar{\mathbf{x}}_2$. Les deux échantillons sont indépendants, donc $\operatorname{Cov}(\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2) = \frac{\boldsymbol{\Sigma}_1}{n_1} + \frac{\boldsymbol{\Sigma}_2}{n_2}$, et la moyenne est $\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2$.
3. Avec 1, $\mathbb{E}\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2 = \lVert\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2\rVert^2 + \frac{\operatorname{tr}\boldsymbol{\Sigma}_1}{n_1} + \frac{\operatorname{tr}\boldsymbol{\Sigma}_2}{n_2}$. Les traces sont positives (strictement, dès qu'une variance n'est pas nulle) : en moyenne, la distance estimée dépasse la vraie.
4. $\lVert\bar{\mathbf{x}}_1 - \bar{\mathbf{x}}_2\rVert^2 - \frac{\operatorname{tr}\boldsymbol{\Sigma}_1}{n_1} - \frac{\operatorname{tr}\boldsymbol{\Sigma}_2}{n_2}$ a pour espérance $\lVert\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2\rVert^2$. Il peut être négatif : si $\boldsymbol{\mu}_1 = \boldsymbol{\mu}_2$, son espérance est nulle, et il n'est pas toujours nul (dès qu'une variance est positive) : il prend donc des valeurs négatives avec une probabilité positive. Le biais dépend des tailles : deux distances brutes calculées sur des tailles différentes n'ont pas le même biais, et leur écart peut ne venir que de là.

**Grille de relecture.** 1 : la décomposition coordonnée par coordonnée, ou $\mathbb{E}[\mathbf{v}^\top\mathbf{v}] = \operatorname{tr}\mathbb{E}[\mathbf{v}\mathbf{v}^\top]$. 2 : la covariance d'une moyenne, avec l'indépendance des points d'un même échantillon, puis l'indépendance des deux échantillons pour additionner. 3 : la conclusion et le signe du biais. 4 : un estimateur juste, sa possible négativité, et l'argument des tailles.

**Variante.** Si les covariances sont inconnues, on remplace $\operatorname{tr}\boldsymbol{\Sigma}_k$ par la trace de la covariance empirique de l'échantillon $k$ (avec $n_k - 1$ au dénominateur, M02c) ; la correction reste sans biais.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M27.16 — Pont : la distance de Fréchet en dimension 1, W₂² = (Δμ)² + (Δσ)², entre deux lois résumées par leur moyenne et leur écart-type (deux séries d'une machine, avant et après réglage) : la part de la moyenne et celle de l'écart-type, et pourquoi workbookIA 27 l'écrit avec des covariances et en rend le carré

**Réponses.** a) `0.0833` · b) `0.2886` · c) `94.1` · d) `0.0049` · e) `0.0935`.

**Démarche.** $\Delta\mu = 0{,}28$ mm et $\Delta\sigma = 0{,}07$ mm. a) $0{,}0784 + 0{,}0049 = 0{,}0833$ mm². b) $\sqrt{0{,}0833} \approx 0{,}2886$ mm. c) $\frac{0{,}0784}{0{,}0833} \approx 94{,}1$ %. d) $\boldsymbol{\Sigma}_1 = [[0{,}0144]]$ et $\boldsymbol{\Sigma}_2 = [[0{,}0025]]$ : $0{,}0144 + 0{,}0025 - 2\sqrt{0{,}0144 \times 0{,}0025} = 0{,}0169 - 2 \times 0{,}006 = 0{,}0049$. e) La fonction calcule $0{,}0784 + 0{,}12 + 0{,}05 - 2\sqrt{0{,}12 \times 0{,}05} \approx 0{,}0784 + 0{,}0151 = 0{,}0935$, un nombre sans signification.

Dans ta copie : d) vaut $(0{,}12 - 0{,}05)^2$, la part de l'écart-type, et a) $=$ (part de la moyenne) $+$ d). Le réglage a surtout recentré la machine (94 % de $W_2^2$). Une tolérance s'exprime en mm, comme $W_2$ ; $W_2^2$ est en mm², et le comparer à 0,1 mm n'a pas de sens. Avant d'appeler une fonction de distance d'une bibliothèque : ce qu'elle prend (des écarts-types, des variances, des matrices de covariance ?) et ce qu'elle rend (la distance, ou son carré ?) ; `w2_gaussians_1d` prend des écarts-types et rend $W_2$.

**Erreurs fréquentes.** Mettre des variances dans la formule (0,0785). Donner $W_2$ en a). Prendre $\lvert\Delta\mu\rvert + \lvert\Delta\sigma\rvert$ (0,35) pour $W_2$. Rapporter la part de la moyenne à $W_2$ (97,0 %), ou donner celle de l'écart-type (5,9 %). En d), mettre les écarts-types dans les matrices (0,0151), ou oublier le terme croisé (0,0169). En e), oublier la part des moyennes (0,0151).

**Variante.** Si l'écart-type était resté 0,12 mm, $W_2 = 0{,}28$ mm, tout entier dû à la moyenne.

### Ex M27.17 — MML §7.2 relu : l'inégalité minimax (7.23) et sa preuve, la dualité faible (7.27) lue comme un jeu, et l'inégalité vérifiée sur une matrice de gains choisie

**Réponses modèles.**
1. Dans (7.23), $\mathbf{x}$ minimise et $\mathbf{y}$ maximise. Avec la fiche, $\mathbf{y}$ est le joueur des lignes (il maximise), $\mathbf{x}$ le joueur des colonnes (il paie), et $\varphi(\mathbf{x}, \mathbf{y}) = g_{\mathbf{y}\mathbf{x}}$ : $\max_i\min_jg_{ij} \le \min_j\max_ig_{ij}$.
2. Le membre de gauche, $\min_{\mathbf{x}}\varphi(\mathbf{x}, \mathbf{y})$, ne dépend que de $\mathbf{y}$ ; celui de droite, $\max_{\mathbf{y}}\varphi(\mathbf{x}, \mathbf{y})$, que de $\mathbf{x}$. Pour une matrice : pour tous $i, j$, $\min_lg_{il} \le g_{ij} \le \max_kg_{kj}$. Pour $j$ fixé, $\max_kg_{kj}$ majore $\min_lg_{il}$ pour **toute** ligne $i$, donc aussi leur maximum : $\max_i\min_lg_{il} \le \max_kg_{kj}$. Le membre de gauche est maintenant un nombre qui minore $\max_kg_{kj}$ pour **toute** colonne $j$, donc aussi leur minimum.
3. Par exemple $\begin{pmatrix} 2 & 6 & -1 \\ 4 & 1 & 5 \end{pmatrix}$ : minimums des lignes $-1$ et 1, maximums des colonnes 4, 6 et 5 ; les six inégalités $-1 \le 4, 6, 5$ et $1 \le 4, 6, 5$ ont lieu ; maximin $1 <$ minimax 4.
4. $\mathcal{L}(x, \lambda) = (x - 2)^2 + \lambda(x + 1)$, avec $\lambda \ge 0$ (la contrainte s'écrit $x + 1 \le 0$). Si $x$ annonce d'abord : pour $x = -2$ (admissible), $\mathcal{L} = 16 - \lambda$, maximal en $\lambda = 0$, et $\max_\lambda\mathcal{L} = 16 = f(-2)$ ; pour $x = 0$ (non admissible), $\mathcal{L} = 4 + \lambda$, et $\max_\lambda\mathcal{L} = +\infty$. Donc $\min_x\max_\lambda\mathcal{L}$ est le minimum de $f$ sous la contrainte, 9, en $x = -1$. Si $\lambda$ annonce d'abord : $\mathcal{L}$ est minimal en $x = 2 - \frac{\lambda}{2}$, et $D(\lambda) = \frac{\lambda^2}{4} + \lambda\big(3 - \frac{\lambda}{2}\big) = 3\lambda - \frac{\lambda^2}{4}$, maximal en $\lambda = 6$, où $D(6) = 9$. Ici, pas de saut de dualité (le problème est convexe). Dans le primal (7.26), $\lambda$ annonce en second et punit toute contrainte violée ; dans le dual, c'est $x$ qui annonce en second.
5. *Minimax inequality* (inégalité minimax), *weak duality* (dualité faible), *primal problem* (problème primal), *Lagrangian dual problem* (problème dual de Lagrange), *dual variables* (variables duales), *Lagrange multiplier* (multiplicateur de Lagrange).

**Grille.** Les rôles de (7.23) identifiés et traduits ; la dépendance de chaque membre de (7.24) ; les deux passages justifiés (un majorant commun de toute une famille majore son maximum ; un minorant de toute une famille minore son minimum) ; une matrice $2 \times 3$ sans point selle, vérifiée ; le lagrangien avec $\lambda \ge 0$ et la contrainte sous la forme $g \le 0$ ; $+\infty$ hors de la contrainte ; $D(\lambda)$ et son maximum ; qui annonce en second dans chaque problème.

### Ex M27.18 — Expliquer avec une partie de cache-cache pourquoi jouer au hasard peut être la meilleure stratégie, et ce que le hasard garantit

**Réponse modèle (6 à 10 phrases).** Si ton neveu se cache toujours au grenier, parce que c'est la meilleure cachette, tu finis par le remarquer, et tu y montes directement : une habitude se lit, et celui qui la lit en profite. Pour ne rien laisser lire, il doit tirer sa cachette au hasard, à chaque partie, sans que le tirage dépende de ce qui s'est passé avant. Mais pas forcément à pile ou face : si le grenier est plus sûr, il peut s'y cacher plus souvent, tant que tu n'as pas intérêt à y monter à coup sûr. Le bon dosage est celui où, pour toi qui cherches, commencer par le grenier ou par la cave revient au même : tu n'as plus de préférence. À ce dosage, ses chances de ne pas être trouvé ne dépendent plus de ce que tu fais : elles sont garanties en moyenne, quelle que soit ta stratégie, même si tu connais ses probabilités. C'est tout ce que garantit le hasard : sur une partie donnée, il peut très bien être trouvé tout de suite ; c'est sur beaucoup de parties que la garantie se voit. Et tu peux faire de même de ton côté : chacun tire au hasard avec le bon dosage, et le dosage de chacun est alors une meilleure réponse à celui de l'autre.

**En 3 phrases.** Une cachette toujours la même se devine, et celui qui la devine en profite. En tirant sa cachette au hasard avec le bon dosage, celui où le chercheur n'a plus de préférence, on s'assure en moyenne les mêmes chances quoi que fasse l'autre. Le hasard ne garantit rien sur une partie : il garantit une moyenne sur beaucoup de parties.

**Grille.** Une habitude exploitée ; le tirage au hasard, indépendant d'une partie à l'autre ; un dosage qui n'est pas forcément moitié-moitié ; l'indifférence de l'adversaire ; une garantie en moyenne, même face à un adversaire qui connaît les probabilités, et rien de garanti sur une partie.

<a id="entretien"></a>

## 💼 Entretien

### M27.E1 — « Pourquoi une distance de Wasserstein reste-t-elle informative quand deux lois ne se recouvrent pas, et pas Jensen-Shannon ? »

**Réponse modèle (60 secondes).** « Jensen-Shannon compare deux lois point par point, à travers leur mélange. Dès que leurs supports sont disjoints, elle vaut ln 2, son maximum, que les lois soient à un millimètre ou à un kilomètre l'une de l'autre. Prenons deux masses ponctuelles, en 0 et en thêta : la JS vaut ln 2 pour tout thêta non nul, sa pente est nulle, et qui ajuste thêta en suivant cette pente ne sait pas de quel côté aller. La KL fait pire : elle est infinie. La distance de Wasserstein W1, elle, mesure le coût du transport d'une loi sur l'autre : la masse multipliée par le chemin parcouru. Pour les deux masses ponctuelles, elle vaut la valeur absolue de thêta, avec une pente de 1 : elle dit de combien et dans quel sens il faut bouger. Plus généralement, elle reste finie et varie continûment quand une loi se déplace, même sans recouvrement. Sa limite : en dimension 1, elle se calcule par un tri, mais en dimension plus grande, il faut un programme linéaire, ou une version approchée, et sur des échantillons elle est estimée, avec un biais. »

**Grille.** $\mathrm{JS} = \ln 2$ pour des supports disjoints, quelle que soit la distance ; la pente nulle et ce qu'elle fait à un ajustement ; la KL infinie ; $W_1$ comme coût d'un transport, $\lvert\theta\rvert$ pour une translation, pente 1 ; un exemple (deux masses ponctuelles, ou deux lois translatées) ; une limite de $W_1$.

### M27.E2 — « Deux échantillons de la même loi donnent une distance non nulle : pourquoi, et comment comparer deux mesures ? »

**Réponse modèle (60 secondes).** « Deux échantillons ne sont jamais identiques : même tirés de la même loi, leurs moyennes, leurs écarts-types et leurs histogrammes diffèrent un peu. Une distance calculée entre eux mesure donc aussi ce hasard. Pour une distance entre moyennes, le calcul est exact : l'espérance du carré de la distance entre les deux moyennes empiriques vaut le vrai carré, plus la trace de la covariance divisée par n1, plus la même divisée par n2. Entre deux échantillons de la même loi, elle vaut donc en moyenne la trace de sigma fois un sur n1 plus un sur n2, et pas zéro. Ce biais dépend des tailles : deux distances ne se comparent qu'à tailles égales. Pour s'en sortir quand les tailles diffèrent, on retire une estimation du biais : la trace de la covariance estimée, divisée par chaque taille. Et pour savoir si l'écart est plus grand que le hasard, il faut un test, qui donne une p-valeur : celui de Kolmogorov-Smirnov, ou un test par permutation. »

**Grille.** L'origine (le hasard de l'échantillonnage) ; le biais $\operatorname{tr}\boldsymbol{\Sigma}\,\big(\frac{1}{n_1} + \frac{1}{n_2}\big)$ ; les tailles égales ; une correction (retirer une estimation du biais) ; un test et sa p-valeur.

<a id="notebook"></a>

## Notebook

Le code complet est dans `05_solutions.ipynb`, exécuté ; voici les réponses et ce qu'il faut en retenir.

- **M27.19 🔨** `pure_strategy_values` : `G = np.array(G, dtype=float)`, les contrôles (2-D, non vide, `np.isfinite`), `rows = G.min(axis=1)`, `cols = G.max(axis=0)`, `row = int(np.argmax(rows))`, `col = int(np.argmin(cols))`. a) `(3.0, 3.0, 1, 1)` : A2 contre B2, le premier des deux points selles. b) `(-3.0, -3.0, 1, 1)` : $-\mathbf{G}^\top$ a pour coefficients $-g_{ji}$, et $\max_j\min_i(-g_{ij}) = -\min_j\max_ig_{ij}$. c) `(60.0, 85.0, 1, 0)` ; faux ($60 < 85$).
- **M27.20 🔨** `mixed_strategy_value_2x2` : la forme, puis `maximin, minimax, row, col = pure_strategy_values(G)` ; si `maximin == minimax`, les stratégies pures ; sinon `(a, b), (c, d) = G.tolist()` et les trois formules. a) $(0{,}3846 ;\ 0{,}5385 ;\ 73{,}4615)$, soit $\big(\frac{5}{13}, \frac{7}{13}, \frac{955}{13}\big)$. b) Les formules donneraient $p = -2$ et $q = 4$ ; la fonction rend `(1.0, 1.0, 4.0)`, le point selle (0, 0). c) 73,4615 et 73,4615.
- **M27.21 🔨** `descent_ascent_iterates` : `xs = np.empty((n_steps + 1, n))`, `ys = np.empty((n_steps + 1, m))`, puis `x_new = x - eta * (A @ y)` et `y = y + eta * (A.T @ (x_new if alternating else x))`. a) $1{,}36^2 = 1{,}8496$ et $1{,}36^{2{,}5} \approx 2{,}1570$ : 5 pas, comme M27.4 c). b) Un écart de l'ordre de $10^{-15}$ ; vrai (la plus grande distance vaut $\approx 1{,}195226$, sous $1/\sqrt{0{,}7} \approx 1{,}195229$). c) Vrai ($\eta\lVert\mathbf{A}\rVert_2 \approx 0{,}71$ : la spirale s'éloigne vite, et la somme des carrés est multipliée par $\approx 7 \times 10^8$ en 50 pas) ; un écart de l'ordre de $10^{-15}$, puisque $\eta\lVert\mathbf{A}\rVert_2 < 2$.
- **M27.22 🔨** `w2_gaussians_1d` : les contrôles (`numbers.Real`, ni `bool` ni `np.bool_`, `math.isfinite`, écarts-types $\ge 0$), puis `float(math.hypot(mu1 - mu2, sigma1 - sigma2))`. a) 1,3. b) 0,2886. c) 2.
- **M27.23 📦** a) 155 t·km, $W_1 = 1{,}55$ km ; vrai. `linprog` peut rendre un autre plan optimal, par exemple $\begin{pmatrix} 20 & 0 & 0 \\ 15 & 35 & 0 \\ 5 & 0 & 25 \end{pmatrix}$ : pour le coût $\lvert x - y\rvert$, l'optimum n'est pas unique (un trajet de 4 à 3 puis de 6 à 2 coûte autant qu'un trajet de 4 à 2 puis de 6 à 3). b) 275 t·km², $W_2 = \sqrt{2{,}75} \approx 1{,}6583$ km ; vrai : pour un coût strictement convexe, le plan optimal est unique, et c'est le plan monotone. a) redonne le $W_1$ de M27.7, que l'aire entre les fonctions de répartition donnait sans programme linéaire.
- **M27.24 🔮** Prédictions attendues : a) (C) ; b) (B) ; c) (B). d) $1{,}09^{20} \approx 5{,}6044$. e) $\frac{40\arctan 0{,}3}{2\pi} \approx 1{,}8555$ tour. f) $\approx 23{,}95$ : pour $\eta = 2{,}5$, la trace vaut $-4{,}25$ et les valeurs propres $-0{,}25$ et $-4$ ; la distance est multipliée par 4 environ à chaque pas, en changeant de côté. La vérification compare les 41 itérés tracés aux itérés exacts, et regarde l'équilibre marqué, l'échelle commune des axes, le titre ($\eta$ et le mode) et les noms d'axes ; elle fait aussi un appel caché ($\eta = 0{,}45$, 12 pas alternés).
- **M27.25 🔬** a) Moyennes $\approx 0{,}0560$ ; $0{,}0138$ ; $0{,}0036$ ; $0{,}0298$ ; $0{,}0291$, contre 0,056 ; 0,014 ; 0,0035 ; 0,02975 ; 0,02975, soit des rapports 0,999 ; 0,986 ; 1,018 ; 1,001 ; 0,978. b) Vrai. c) $\approx 0{,}0585$ et $0{,}0061$, puis $0{,}0025$ et $0{,}0026$ une fois le biais retiré. d) Vrai : $0{,}0585/0{,}0025 \approx 23$. Sur la figure, les trois points suivent la droite $2\operatorname{tr}\boldsymbol{\Sigma}/n$, de pente $-1$ en échelles logarithmiques. La vérification essaie `distance_bias_25` sur un cas caché ($n_1 = 7$, $n_2 = 3$), et regarde les points, la courbe, les deux échelles logarithmiques et la légende.
- **M27.26 🎨** a) $(1{,}200 ;\ 0{,}236)$ : $W_1$ est le décalage, et $\mathrm{KS} = 2\Phi(0{,}3) - 1 \approx 0{,}2358$, atteint au milieu, en 20,6 °C. b) $(3{,}000 ;\ 0{,}326)$ : $W_1 = 3 \times \mathbb{E}[-\ln(1 - U)] = 3$ (le couplage des quantiles), et l'écart maximal est en $x = \frac{10}{3}\ln 2{,}5 \approx 3{,}05$ min. c) $(2{,}160 ;\ 0{,}236)$. La vérification compare les deux nombres rendus aux valeurs exactes, et regarde le titre, la zone colorée, le segment vertical et la légende (`label_a`, `label_b`) ; elle fait aussi un appel caché sur deux autres lois.
- **M27.27 🐛** (1) `penalty_kick_mix` calcule `(d - b) / κ`, la formule de $q^\star$ : elle rend le joueur des lignes indifférent, au lieu de l'adversaire. Sur le jeu symétrique du collègue ($b = c = 90$), $p^\star = q^\star$ : la vérification ne pouvait rien voir. Correction : `(d - c) / κ`. a) $\frac{5}{13} \approx 0{,}3846$ ; la version fautive rend $\frac{7}{13} \approx 0{,}5385$. (2) `w2_settings` met les variances $\sigma^2$ là où la formule veut les écarts-types ; les vérifications prenaient des écarts-types égaux, ou 0 et 1, pour lesquels $\sigma^2 = \sigma$. Correction : `(sd1 - sd2) ** 2`. b) 0,2886 contre 0,2803 pour la machine (des écarts-types sous 1 mm écrasent la différence des variances) ; 3 contre 21 pour $\mathcal{N}(100 ;\ 5^2)$ et $\mathcal{N}(100 ;\ 2^2)$. (3) `pair_parts` ne trie que les bagues : elle monte la $i$-ème plus petite bague sur l'axe `i` dans l'ordre des mesures, ce qui n'est juste que si les axes arrivent déjà triés, comme dans la vérification. Correction : `partner = np.empty(n, dtype=int)`, puis `partner[np.argsort(shafts)] = np.argsort(sleeves)`. c) `[3, 4, 2, 1, 0]` ; 0,0277 mm² (des jeux 0,06 ; 0,08 ; 0,08 ; 0,08 ; 0,07) contre 0,0373 mm² (des jeux 0,03 ; 0,08 ; 0,02 ; 0,14 ; 0,10). La vérification essaie aussi des axes dans le désordre, des égalités entre diamètres, et des jeux sans symétrie.
- **M27.28 🛠️** a) Avec des entiers, tous les calculs sont exacts en flottants, ou presque : la détection du point selle (une comparaison exacte) ne bascule pas quand on ajoute $c$ ou qu'on multiplie par $k$, et les formules redonnent $p$, $q$ et $v + c$ aux arrondis près ; avec des flottants quelconques, un jeu presque à point selle pourrait changer de cas entre $\mathbf{G}$ et $\mathbf{G} + c$, et le test compterait une fausse alerte. Avec un point selle et des égalités, la règle des plus petits indices n'est pas compatible avec l'échange des rôles ou des lignes : pour $\begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$, la bonne fonction rend $(1, 1, 2)$ pour $\mathbf{G}$ comme pour $\mathbf{G}$ retournée, alors que la propriété attend $(0, 1, 2)$ ; sans point selle, les stratégies optimales sont uniques, et les deux propriétés valent. b) Vrai (260 des 400 jeux ont un point selle ; les deux dernières propriétés portent sur les 140 autres). La vérification compare tes cinq compteurs à ceux de la référence sur deux départs cachés de 150 essais, puis remplace un instant ta `mixed_strategy_value_2x2` par une version qui calcule la valeur avec $\lvert\kappa\rvert$ ; elle essaie aussi deux versions fausses cachées, qui déplacent $p$ sous $k\mathbf{G}$ ou $q$ sous $\mathbf{G} + c$, et un appel avec `tol = 1.5`, qui voit un test qui ignore `tol`. c) `swapped_pq` : `"swap_rows"` = 138, les autres nuls ; `formulas_always` : `"bounds"` = 222, les autres nuls ; `maximin_as_value` : `"transpose"` = 140, les autres nuls ; `rounded_value` : `"scale"` = 98 et `"shift"` = 3 (un arrondi au pair, comme `round(2.5) = 2`), les autres nuls. d) `swapped_pq` et `maximin_as_value`. Chaque propriété nouvelle est exigée par au moins une version fausse ; ce test ajoute à ceux de `tests/test_m27_distances.py` l'échange des rôles, l'échange des lignes, et la preuve qu'il attrape des versions fausses que les propriétés du titre laissent passer.
- **M27.29 🏆** a) $(2{,}000 ;\ 1{,}806 ;\ 0{,}858)$ (plus précisément $\sigma \approx 1{,}80639$ et $W_2 \approx 0{,}85845$). b) Vrai. c) $\frac{0{,}85845^2}{4} \approx 18{,}4$ %. La méthode la plus sûre : dans l'espace des fonctions de carré intégrable sur $]0, 1[$, les fonctions 1 et $\Phi^{-1}$ sont orthogonales ($\int_0^1\Phi^{-1} = 0$) et $\int_0^1(\Phi^{-1})^2 = 1$ ; la meilleure approximation de $F^{-1}$ par $\mu + \sigma\Phi^{-1}$ est sa projection : $\mu = \int_0^1F^{-1} = \mathbb{E}[X]$, $\sigma = \int_0^1F^{-1}\Phi^{-1}$ (positif, puisque $F^{-1}$ et $\Phi^{-1}$ croissent toutes deux), et $W_2^2 = \mathbb{V}(X) - \sigma^2$ ; trois intégrales par `scipy.integrate.quad`. Minimiser $W_2^2(\mu, \sigma)$ par `scipy.optimize.minimize`, chaque évaluation par `quad`, marche aussi. Sur 1 000 points milieux de $u$, la moyenne de $F^{-1}(u)\,\Phi^{-1}(u)$ donne $\sigma \approx 1{,}8022$ (à $4 \times 10^{-3}$), et les moindres carrés sur ces points $\sigma \approx 1{,}8046$ (à $1{,}8 \times 10^{-3}$) : trop loin, l'un comme l'autre. La vérification compare le guichet à la réponse a), à 3 décimales, puis essaie deux lois cachées, une loi uniforme sur $[1 ; 4]$ ($\approx 2{,}5$ ; $0{,}8463$ ; $0{,}1839$) et une loi Gamma de forme 2 et d'échelle 1,5 ($\approx 3$ ; $2{,}0108$ ; $0{,}6758$), déplacées à chaque exécution par un changement d'échelle et d'origine tiré au hasard ($\mu \to s\mu + t$, $\sigma \to s\sigma$, $W_2 \to sW_2$) : une table de valeurs ne passe pas, ni une fonction qui renvoie toujours les mêmes nombres.
